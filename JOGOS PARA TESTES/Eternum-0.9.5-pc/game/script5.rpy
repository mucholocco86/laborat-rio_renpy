label update05:
    play sound deception
    play sound3 deception
    scene cz 16
    pause .05
    play sound2 deception
    play sound4 deception
    $ renpy.music.set_volume(0.5, delay=15.0, channel='music3')
    play music2b founder fadein 3
    stop musicb
    stop music
    stop music3
    scene black
    pause
    play sound6 hislies volume 0.6
    scene d 0
    mc "*Muttering* Ughhhh..."with Dissolve(2.6)
    mc "F-Fuck, not this headache again..."
    tf "Is anything wrong, boy?"
    mc "N-No, I just got a bit d-dizzy for a second..."
    show d 0b
    mc "Hmmm..."with dis
    mct "This damn pain came back at the worst possible time..."
    mct "Is this real? Is this man... really {i}him?!"
    show d 1
    tf "Four, Twelve, come here and get ready to leave."with dis12
    tf "We must return as soon as we are done with Mr. [lastname] here."
    pra "Yes, sir."
    play sound footsteps
    show d 2 with dis17
    mc "Y-You are..."with dis08
    mc "The Founder..."
    show d 3
    tf "That is my title, yes."
    show d 2
    mc "You... you're the creator of Eternum."
    show d 3
    tf "Hmm. I am."
    tf "My life’s work."
    show d 2
    mc "And... you know me? H-How? Why...?"
    show d 3
    tf "When a Gem of Doom is first discovered by a player, Ulysses receives a notification. We always know who the first person to track down a Gem is."
    tf "However, if a Gem transfers ownership for some reason... Ulysses is unable to know exactly who the new owner is."
    tf "So, I know it was you who found the Gem of Doom in The Red Herring."
    tf "A player at level 2 getting one of my Gems. That is not something you see everyday."
    tf "Then, you somehow managed to access a restricted server and steal one of Idriel's creations... Calypso."
    tf "You even killed two Praetorians in the process."
    show d 2
    mc "W-What? Um... I-It’s not what it sounds like..."
    mct "Idriel's creations? Not his?"
    mc "We..."
    show d 3
    tf "I know you do not have that gem in your possession currently. I also know that buffoon, Garrington, lost his gem recently. So I guess that explains your presence at this dinner."
    tf "Thieving from the casino is no simple feat. Astonishing."
    show d 2
    mc "Um..."
    show d 3
    tf "I am not easily impressed. I can count the players who’ve excited me since Eternum’s founding on one hand."
    tf "I am expecting great things from you, [mc]."
    show d 2
    mc "Uh... thank you."
    mct "Fuck, I don't know what to say."
    show d 5
    tf "I have something for you."with dis12
    tf "This is the Amulet of Blair."
    tf "I have been selecting the most promising players of Eternum and offering them this mighty artifact, in an attempt to accelerate the gathering of the 10 Gems."
    tf "I want you to have it."
    show d 6
    mct "Accelerate? Why the rush? Is he in a hurry?"
    mct "Maybe he's dying...? Maybe that's why he created the 10 Gems quest, because he wanted to find a successor..."
    mc "Uh... what does this amulet do?"
    show d 7
    tf "The Amulet of Blair has one simple, passive effect... but it is a powerful one."with dis12
    tf "With it, you can become... immortal."
    tf "You cannot die in Eternum if you have this amulet in your inventory."
    tf "No matter what happens to your body, you will be able to re-enter the game through the nearest Exit Portal. You will be completely healed, with your inventory intact."
    tf "That is... my gift."
    show d 6
    mct "Becoming immortal...?"with dis12
    menu amulet:
        with dis
        "Take the amulet":
            $ amuletofblair = True
            mc "It's an offer that's difficult to refuse."with dis08
            mc "I’ll gladly accept it. Thank you."
        "[gr]Refuse":
            mc "Um... I appreciate the offer, but... it... feels like cheating."with dis08
            mc "I prefer to play under the same conditions as everyone else."
    show d 3
    if amuletofblair:
        show screen amulet
        tf "You won't regret it, [mc]."with Dissolve(1.3)
        tf "I hope you can go even further with it."
    else:
        tf "Huh..."with Dissolve(1.3)
        tf "Very well, as you wish."
        tf "The others also refused. Interesting."
        tf "I wonder if I should feel disappointed or... proud."
        show d 2
        mct "The others? How many players did he talk to? Thanatos has to be one..."
        show d 3
        tf "Anyway... I hope you can continue your path even without this artifact, [mc]."
    show d 2
    mc "I hope so too."
    show d 3
    tf "It was a pleasure finally meeting you, but I am afraid I must leave now."
    tf "As you can understand, my position requires constant meetings and appointments."
    show d 2
    mc "Of course, I can only imagine."
    hide screen amulet
    show d 4
    tf "Before I leave, though... I have one last question for you. And please, be honest." with dis12
    tf "On all these adventures in Eternum... battling monsters, solving mysteries, embarking on quests... do you fight for yourself? Or do you fight for others?"
    mc "What? Me? I... don’t know."
    mc "Neither, I guess."
    tf "But if you had to choose one or the other... which choice describes your... ideology?"
    mc "Um..."
    menu:
        with dis
        "[gr]I fight to protect others":
            $ hero = True
            mc "I fight to protect others." with dissolve
            tf "Hmm."
        "I fight for myself":
            mc "I fight for myself." with dissolve
            tf "Hmm."
    play sound footsteps
    show d 1
    tf "So tell me..."with dis15
    if hero:
        tf "Would you sacrifice the innocent to save those whom you love?"
        menu:
            with dis
            "Yes{#0.5,founderquestion}":
                mc "What? To save the people I love?" with dissolve
                mc "Um... I... I guess."
                tf "And is that what a hero would do? Sacrificing the lives of the innocent? At that point, can you truly claim you’re protecting others?"
                mc "Uh..."
            "No{#0.5,founderquestion}":
                mc "Never." with dissolve
                tf "So you'd let your loved ones die in exchange for the lives of strangers? You’d let young Miss Bardot die to save someone you’d never even met?"
                mc "What? Uh... well... I wouldn't..."
    else:
        tf "Would you sacrifice those you care about for the chance to gain more power?"
        menu:
            with dis
            "Yes{#0.5,founderquestion}":
                mc "Um... Honestly? I think so, yeah."with dissolve
                tf "Hmm. Interesting."
                tf "Very interesting."
            "[gr]No{#0.5,founderquestion}":
                mc "Sacrifice? Well... no, not really."with dissolve
                $ hero = True
                tf "Hmm... then perhaps you do fight for others, after all...?"
                mc "Uh... Well..."
    tf ". . ."
    tf "I am sorry, these are just the ramblings of an old man."
    mc "Um... no worries, it's okay."
    tf "Good night, [mc]."
    mc "G-Good night, sir."
    play sound2 doorecho
    stop music2b fadeout 4
    play music fireplace fadein 5
    show d 8 with dis22
    mct "Holy fuck." with dis
    mct "No one on the executive board of Ulysses has ever talked face-to-face with this man, and yet... I just did."
    mct "I don't know if I should feel honored... or scared."
    x "Finally!"
    show d 9
    mc "*Turning around* Alex!" with dis
    mc "Thank god you found me!"
    show d 10
    x "Yeah, well, it wasn't easy. Your directions sucked."with dis12
    show d 11
    mc "I know! I was about to tell you more, but then something happened, and... shit, you're not gonna believe it."
    mc "I met the Founder!"
    show d 10
    x "The Founder? Really?"
    show d 11
    mc "Yeah! And right after we were beginning to think he was a fake!"
    show d 10
    x "Mm-hm, yeah, sure. And then you shared a pizza with him, Thanatos and Idriel, right?"
    show d 11
    mc "I'm serious! I was talking to him! He left less than a minute ago!"
    show d 10
    x "How convenient."
    show d 11
    mc "You have to believe me!"
    x "Hmm..."
    show d 10
    x "You met the Founder. Alone. In a dirty basement with no lights."
    show d 11
    mc "I know it sounds weird, but trust me! And we weren’t completely alone, there were Praetorians there too!"
    mc "I wouldn't lie to you about something like this!"
    mc "Give me 5 minutes to explain everything."
    show d 10
    x "I’ve gotta stop you right there. My father is giving a speech in the main hall, and I think some of the shareholders are starting to get suspicious of all our questions."
    x "I already told Calypso to leave, she's waiting for us outside."
    show d 11
    mc "Really? Dammit."
    if answersmenu:
        mct "I was supposed to meet that strange man at 12, but if we have to leave... I guess I won't be able to."
        mct "Anyways, I doubt it was anything important. My head’s full of enough info as it is. I’m having a tough time remembering everything."
    mc "Alright, why don’t you log off and head over to my house, then? I’ll tell you everything in-person."
    show d 10
    if alexpath:
        x "I can't. I have to wake up early tomorrow. I have swimming training at 8."
        show d 11
        mc "Oh... fair enough."
        mc "Well, I'll update the others with everything we learned tonight."
        mc "I can tell you everything on Monday, after school."
        mc "Fancy a coffee?"
        x ". . ."
        show d 13
        x "*Snorts*" with dis
        show d 12
        x "Smooth."
        show d 13
        mc "What?"
        show d 12
        x "Nothing, nothing."
        x "Sure, you can tell me everything while buying me some coffee."
        x "We’ve gotta prepare a plan. We’ll need someone who is a master at strategy."
        show d 13
        mc "Exactly. And I think I’ve got the perfect person in mind."
        show d 12
        x "I guess we should leave before Calypso starts disintegrating people."
        show d 13
        mc "*Laughs* True."
    else:
        x "No thanks. You can tell me on Monday at school."
        show d 11
        mc "Hmm... Okay, let's do that. In the meantime, I'll update the others with everything we learned tonight."
        show d 10
        x "Alright, can we leave now?"
        show d 11
    mc "I'll follow you!"
    stop music fadeout 4
    show black with Dissolve(2.5)
    pause
    show screen afewdayslater with dis22
    pause
    play sound birds fadein 2
    hide screen afewdayslater
    scene d 14
    with dis25
    play music2 happy12 fadein 6
    show screen fridaycorner
    pause
    x "*Yawns*"with dis
    x "What was I saying?"
    x "Ah, yeah."
    show d 15
    x "*Playing with her cross* Ms. Kellegan said I'm ready for the Olympic qualifiers, but... meh, I don't know." with dis15
    show d 19
    x "You know I love swimming, Baba, but..."with dissolve
    x "I'd have to travel across the country, and... ugh."
    show d 15
    x "Maybe next year. I have other stuff to do now."with dissolve
    x "I have to graduate and get into college."
    x "And Eternum is a priority now. It's not just a hobby anymore, you know?"
    show d 19
    x "I met this guy. He's... a total headache."with dissolve
    if alexpath:
        x "He's always in some kind of trouble. Which is exhausting, but also... entertaining. In a way."
        x "He didn't even know I was a Bardot, can you believe it?"
        show d 17
        x "Well, he didn't even know who the Bardots were! Apparently he just heard of them a week before we met."with dissolve
        x "*Laughs* He fought both Axel and Dad in less than a week!"
        x "He's a mess."
        show d 19
        x "But also... kinda sweet."with dissolve
        x "I mean..."
        show d 17
        x "He's funny. He makes me laugh."with dissolve
        show d 19
        x "Well, not always."with dissolve
        show d 18
        x "Sometimes." with dissolve
        x "I..."
        show d 16
        x "I don't know, I like spending time with him."with dissolve
        x "He..."
        show d 17
        x "He makes me feel like everything will be alright."with dissolve
        x "When I'm with him... I feel reassured and calm."
        x "It's like..."
    else:
        x "He and his friends are always in some kind of trouble. Which is exhausting, but also... entertaining. In a way."
    show d 20
    x "*Dropping the cross* Do you remember what you told me that day at the beach?"with dis12
    x "When we went fishing?"
    x "Could it be possible that..."
    show d 21
    d "At the beach? Mmmm..." with dis12
    d "I don't remember going fishing with you. Do you mean volleyball? I do remember doing that last summer."
    show d 22
    x ". . ."with dis
    play sound slap1 volume 2
    play sound2 slap1
    show d 23
    x "D-Didn't your mom ever tell you it was rude to eavesdrop?!"with hpunch
    d "*Giggles* Two people need to be present for a conversation, you know? Who the hell were you talking to?"
    x "I was talking to myself!"
    d "Oh, and were you winning the argument?"
    x "SHUT UP!"with hpunch
    d "*Giggles* I'm kidding, I'm kidding!"
    play sound dodge
    show d 24
    d "*Jumping over the bench* Make room!"with dis
    play sound2 chair2
    show d 25
    d "But seriously, if you wanna talk about something, I can lend an ear." with dis12
    show d 26
    x "It's nothing. I was just mentally reviewing some errands."
    x "Why are you even here?"
    show d 25
    d "I just went for a run, since it’s not raining for the first time in forever. I spotted you on this bench and thought I’d say hi."
    show d 26
    x "Well, you can continue your run, then. Thank you for stopping by."
    show d 25
    d "Come on! Don't be so closed off! I know something has been bothering you."
    d "I feel like I’ve seen you deep in thought all week."
    show d 26
    x "I said I'm okay!"
    show d 27
    x "And... like you're one to talk!"with dissolve
    if daliapath:
        x "You still haven't told me what happened in that private server of yours!"
        show d 29
        d "W-What? Nothing happened!"
        show d 27
        x "Nothing, my ass!"
        x "You came to me all nervous wanting to tell me something, and then you didn't!"
        show d 28
        d "Because there was nothing to tell!"
        show d 30
        x "You're blushing, babe..."
        x "Come on, you're dying to tell me."
        x "Spit it out already. You were there with a guy, right?"
        show d 29
        d "Um..."
        show d 28
        d "Well, yeah, but..." with dissolve
        show d 30
        x "But what? What happened?"
        x "I want the full truth, warts and all."
        show d 28
        d "Uhh... okay, alright, alright."
        d "I invited a guy there. Kind of."
        show d 29
        d "We talked for a bit, and... I don't know. The sea, the sunset, the mood, everything was hitting the right spot."with dissolve
        d "We were playing around, and..."
        show d 28
        d "I'm not sure how it happened, but before I knew it, I was taking my clothes off for him."with dissolve
        show d 31
        x "No way!"
        x "And then what happened?! Did he get naked too?"
        show d 29
        d "Uhh... yeah."
        d "Then I..."
        show d 28
        d "I g-gave him a blowjob, and..."with dissolve
        show d 31
        x "Holy shit! And how did that go?"
        show d 28
        d "It went well... I think. It was kinda fun. More fun than I thought, at least."
        show d 31
        x "Hah! That sounds like you, alright."
        x "I expected no less from my gluttonous friend. You're only happy when you have something in your mouth!"
        d "Hey, don't overdo it!"
        show d 32
        x "Overdo it? Come on, Dalia. If anything, I'm understating your love for meat in your mouth."with dissolve
        x "You're getting ready to chow down on a huge hot dog right now!"
        show daliahotdog1
        pause
        play sound whoosh6
        show daliahotdog2
        pause
        scene d 34
        d "It's 6:30 PM!" with dis08
        d "I need my fourth meal of the day! I can't skip it, I didn't have my second breakfast this morning."
        show d 32
        x "Aren't you going to run? You could have waited till you got home."
        show d 34
        d "Well, I saw this food cart passing by and I thought I’d make a one-time exception. No biggie, just a coincidence."
        hotd "Goodbye, Dalia!"
        show d 35
        d "Bye, Roy! Say hello to Paula!" with dis08
        show d 27
        x "YOU EVEN KNOW THE VENDOR'S NAME!" with hpunch
        play sound chew
        show d 36
        d "*Gobbling the whole hot dog in one bite* Hey, I mmdidn't come here to be judged." with dis
        d "If myou wanted a hot dog, you could have said so."
        show d 30
        x "Yeah, you're right, we should get back on topic..."
        x "You were telling me a very interesting story."
        stop sound fadeout 1
        show d 28
        d "Oh... well, the story is pretty much finished. There's not much else to tell." with dis08
        show d 32
        x "Really? What happened after you blew him?"
        show d 29
        d "Well, he... came."
        show d 30
        x "You swallowed it?"
        show d 28
        d "W-What? O-Of course not..."
        show d 32
        x "Well, and what happened then?"
        show d 29
        d "What do you mean? We stood up and left the server. That's it."
        show d 32
        x "Whaaaat? And he didn't even return the favor?"
        show d 29
        d "R-Return the favor?"
        show d 32
        x "Of course! He should have gone down on you!"
        x "Favor for a favor. Tit for tat... or twat, I guess."
        show d 29
        d "W-What?"
        d "Do you think that..."
        d "Should he?"
        show d 32
        x "Absolutely."
        x "You should DEMAND it!"
        show d 30
        x "Because... you like him, right? That's what you want, don't you?" with dis08
        show d 28
        d "Um..."
        show d 29
        d "I mean..."with dissolve
        show d 28
        d "I don't know... maybe... yeah, maybe he should."with dissolve
        show d 29
        d "Like... dick for twat."with dissolve
        show d 30
        x "You got this."
        x "Just make sure not to tell him you enjoyed giving him head. So he puts in extra effort."
        show d 29
        d "Yeah... thanks for the advice. I'll... I'll think about it."
        show d 37
        d "(God, that would...)" with dis12
        d "(I mean, do I really want him to do that?)"
        d "(It would be... fair. Right?)"
        d "(Yeah, that would be fair. Just so we're even.)"
        d "(And then we can move on... Just one more time.)"
        d "(Hmm. Yeah. That sounds right.)"
    else:
        x "I know nothing about your life!"
        x "You could tell me what's going on between you and Jerry!"
        show d 29
        d "W-What?! Nothing is going on! We're just friends!"
        show d 30
        x "I don't know... I see you playing together a lot lately."
        show d 29
        d "Because he's a friend. And a good Eternum player. That's all!"
        show d 32
        x "Okay, okay... If you say so..."
        x "I won't insist."
        show d 37
        d "(Jerry? Jesus, no.)"with dis
        d "(I don't even like him. The only guy I kinda liked lately wasn’t even into me.)"
        d "(Which was for the better, though. I can't believe I had a crush on that idiot. Thank god that's over now.)"
    p "Hi sis!"
    show d 38
    d "Hmm?" with dissolve
    $ unlock_look("penelope", 9)
    hide screen fridaycorner
    show d 39
    d "Penny!" with dis12
    d "What are you doing here?"
    show d 40
    p "I'm meeting Mom at The Roof, and this park was on the way."with dis04
    p "I had some time to kill, and I like to come here to get ideas. It's a good photo spot!"
    show d 39
    d "Oh, that’s true, definitely see its potential."with dis04
    x "You look good, Penelope. I like those high-waisted shorts."
    show d 41
    p "Oh, thank you, Alex! I just picked the first thing I saw in my closet. Nothing too special." with dis08
    p "Hale Bob shorts from the Fall collection and a Max&Co shirt. Annie recommended that shop to me!"
    x "Looks good!"
    play sound chair2
    show d 42
    p "Oh, and now that I'm with you... I wanted to ask you something, I hope you don't mind." with dis12
    show d 43
    x "Hey, we've robbed a casino together. That's what brings people together. We’re partners in crime now."with dis04
    x "Ask whatever you want."
    show d 42
    p "*Laughs* True that!"with dis04
    if penelopepath and daliapath:
        p "It's about your tattoos. I've never gotten one, but it's something I've always been curious about."
        p "Any advice?"
        show d 43
        x "Well, if it's your first tattoo, I'd recommend you get a small one."with dis04
        x "And maybe in a place that could easily be hidden, especially since you’re a model."
        x "Do you have something in mind?"
        show d 42
        p "I fell in love with the minimalist design of a flamingo I saw the other day on Pinterest!"with dis04
        show d 44
        p "And I thought of the wrist or maybe the ankle for the location."with dis12
        p "What do you think?"
        show d 45
        x "Those are both good options."with dis
        x "Do you have a pic of the tattoo you saw?"
        p "Sure! Give me a second."
        d ". . ."
        d "Um..."
        show d 47
        d "Where did you say you were going...?"with dis12
        show d 46
        p "To The Roof, that pub with a terrace. It’s near the library."with dis04
        show d 47
        d "With Mom...?"with dis04
        play sound2 chair2
        show d 49
        p "Yeah... with Mom."with dis12
        p "Why the interrogating tone?"
        show d 48
        d "What tone? This is how I always talk."
        show d 49
        p "No... not really, no. You’re kinda grilling me, to be honest."
        show d 50
        x "*Conciliatory tone* Um... You know, now that you both are wearing ponytails, I can see how much you look alike!"
        x "Right?"
        show d 48
        d "I was just curious because your outfit is quite revealing for “just a meet-up with Mom.”"
        show d 49
        p "You mean this little bit of cleavage...?"
        p "You've been very prudish lately, sis."
        play sound metalhit
        show cleavage05
        d "LITTLE bit of cleavage?!"
        d "That's not a LITTLE bit of cleavage!"
        d "Back me up here, Alex!"
        scene d 50
        x "Well, I don't want to get involved... but y-yeah, I guess it's pretty... suggestive."
        show d 49
        p "I... um... it's just..."
        p "I-It’s a cute outfit, like Alex just said! I like to dress well, no matter the occasion."
        p "And besides, there'll be more people there, so it's not “just a meet-up with Mom.”"
        show d 48
        d "Oh, really?"
        d "Who else is gonna be there? If I may be so bold as to ask."
        show d 49
        p "Annie. And Nova."
        p "And..."
        show d 48
        d "And?"
        show d 49
        p "And I think [mc] mentioned he was going to pass by, too."
        show d 48
        d "Oh..."
        d "Interesting."
        show d 49
        p "Interesting how?"
        show d 48
        d "No, it’s nothing."
        d "Just interesting."
        show d 49
        p "Okay..."
        p "*Clears throat* Well, I should get going."
        show d 48
        d "You know what? I think I'll go with you."
        show d 50
        x "No running, then?"
        show d 48
        d "Nah... I'm pretty tired today. I think I’ll grab coffee and a snack and take it easy today."
        d "You don't mind, do you?"
        play sound chair2
        show d 51
        p "*Fake giggle* Of course not, Dal!"with dis12
        p "The more the merrier!"
        d "*Fake chuckle* That's what I always say!"
        x "Uh... Well, I'll get going too. I'll see you later."
        p "Goodbye, Alex!"
        d "Bye Alex!"
        d "Let's go, sissy!"
        p "I'm sure Mom will be happy to see you there..."
    else:
        p "So... I wanted to ask about your tattoos..."

label theroof:
    show d 52 with Dissolve(2.6)
    pause
    play sound sneeze
    mc "*Sneezes*"with dissolve
    mc "Ah...."
    mc "Aaahh..."
    play sound sneeze
    show d 52b
    mc "*Sneezes* Choo!" with hpunch
    play sound chair4
    show d 53
    mc "Aghh... Jesus!"with dis
    mc "Man, tell me I didn't catch a cold, please."
    mc "Not when the weekend is around the corner..."
    show d 54
    c "My mother always says that when you sneeze, it means that someone elsewhere is talking about you."
    show d 55
    mc "Ah, I like that!"
    mc "Who do you think might be talking about me?"
    show d 54
    c "It could be a girl from school who has a crush on you!"
    show d 55
    mc "Hah! You think so?"
    show d 54
    c "Yeah!"
    show d 56
    c "Or... maybe it's Axel discussing with his hitmen about the best way to make you disappear without a trace."with dis
    show d 57
    mc "Um... yeah, thanks, Chang."
    mc "I preferred the first hypothesis."
    show d 58
    mc "Now that you mention Axel, though... I haven't seen him since the dinner at the Boyle Mansion."with dis08
    mc "He hasn't come to class since then."
    mc "I wonder why."
    show d 56
    c "Maybe he's waiting for you to get complacent so his contract killers can catch you off guard."
    show d 57
    mc "STOP."
    $ unlock_look("nancy", 6)
    play music type2 fadein 1
    show d 61
    n "Maybe he's waiting for you in Eternum, so he can murder you in the game and in the real world at the same time, like what possibly happened to Benjamin."
    show d 56
    c "Oh, that is very likely, actually, Ms. Carter. It would be poetic and, at the same time, easy to make it look like an accident."
    show d 57
    mc "C-Can you two stop already?!" with hpunch
    mc "Let me enjoy the afternoon in peace!"
    show d 58
    mc "How's that spreadsheet going, by the way?"with dis06
    show d 61
    n "I'm almost done!"
    n "I just need to update this formula here... adjust the reference here... and..."
    stop music
    n "All done!"
    play sound glasses volume 1.5
    show d 62
    n "*Taking off her glasses* Alright, guys!" with dis12
    n "I have a plan for every one of you. You're gonna love it."
    n "Nothing like an Excel spreadsheet to keep things organized!"
    n "As soon as Annie arrives, we can start. Is everyone ready?"
    show d 59
    mc "Ready! I knew it was a good idea to put you in charge of strategy."
    show d 54
    c "I was born ready!"
    $ unlock_look("nova", 6)
    if novapath:
        show d 64
        no "*Muttering* Goddammit..."
        show d 65
        no "Agggh! Why can't I draw hands?!" with dis04
        no "WHY?!"with hpunch
        show d 64
        no "*Muttering* I think I'm making them too small. They look like baby hands on an adult body." with dissolve
        mc "Nova?"
        no "Y-Yeah, yeah, sorry!"
        no "Give me a minute. I just have to finish this little thing..."
        mc "Can we finally see what the hell you’ve been drawing?"
        mc "Every single time I've seen you this week, you've had a pencil in your hands."
        no "Not yet! {w}It's a surprise! {w}No one can..."with hpunch
        show d 65
        no "Ugh, I gotta piss so bad!" with dis04
        mc "Oh, come on, go to the bathroom!"
        mc "This new artistic side of yours has absorbed you!"
        no "Ugh..."
        play sound chair4
        show d 66
        no "*Stands up* O-Okay, okay!" with dis
        no "I'm going to the toilet. But I'll be back in 30 seconds! No, 20!"
        no "N-No one take a look at my... drawing! Especially not [mc]!"
        show d 67
        mc "Why not, though?"
        show d 66
        no "Because it's unfinished! You'd make fun of me."
        show d 67
        mc "That's not true!"
        show d 66
        no "I don't care! Promise me you won't look!"
        show d 67
        mc "Okay, okay, I promise."
        play sound run
        show d 68
        no "*Running away* Thanks!"with dis
        mc "*Chuckles* (What's with all the mystery?)"
        mct "I guess she just got obsessed with something new. It happened when she got a smartphone for the first time, too."
        mct "I can't help but be intrigued, though..."
        menu:
            with dis
            "Look at the drawing":
                $ novadrawinglook = True
                mct "A small look can't hurt." with dissolve
                play soundlow chair3
                show d 69
                mc "Hmm..." with dis
                mct "What's this?"
                show d 84
                n "[mc]! She asked you not to look!"
                show d 70
                mc "It's just a little peek! She won't mind..."
                mct "Oh, she's drawing a manga comic!"
                mct "And damn, it doesn't look half bad!"
                mct "Though those hands are on the small side..."
                play sound doorold
                show d 69 with dis12
                pause .5
                show d 71
                mc "Hmm?" with dis08
                show d 72
                no ". . ."
                mc "Oh..."
                mc "Um... Y-You were quick!"
                play sound grab2
                show d 73
                blank "{i}She snatches the sketchpad right out of your hands." with hpunch
                mc "This isn’t what it looks like. There was a bug on the sketchpad and–"
                show d 74
                no "You promised me you wouldn't look!" with dis06
                show d 73
                mc "I-I know, but you were acting weird, and..."with dis06
                mc "A-And I don't know why!"
                mc "That looks awesome!"
                mc "Are you starting a manga comic?"
                show d 74
                no "I..."with dis06
                no "It's a..."
                $ nova_points -= 1
                play sound chair4
                show d 75
                no "Bah! Forget it."with dis
                no "It just was a ridiculous, dumb thing."
                mc "Nova! Don–"
                no "No. I shouldn't even have started it in the first place. It was a stupid idea."
                mct "Damn... I shouldn't have looked."
                show d 84
                n "Are you okay, Nova?"
                show d 76
                no "Yeah, I’m fine! Thanks for asking, ma'am."
                no "I was just being... dumb."
                mct "I feel bad now."
                no "Anyway, I'm ready! We can start now."
            "[gr]Don't look":
                mct "But I shouldn't look."with dissolve
                mct "Whatever it is, it seemed important to her."
                mct "She hasn't hacked me since she promised not to. It'd be wrong to break my promise and betray her trust after that."
                play sound run fadein 1.6
                show d 59
                mc "While Nova is...{nw}{w=1.7}" with dis
                play sound2 whoosh6
                play sound3 chair4 volume 2
                play sound chairmove
                show v5t
                no "*Taking a big jump* I'M BACK!" with hpunch
                mc "W-What?"
                mc "That wasn't even 20 seconds!"
                play sound chair4
                scene d 78
                no "No one looked at my drawing, right?"with dis
                mc "Nooo, don't worry."
                no "Sure?"
                mc "Hey, I promised not to look. I’d never break a promise."
                show d 76
                no "Excellent! Then I’ll promise to show it to you when it's finished."with dis12
                mc "*Chuckles* Alright, I'll be waiting."
                no "I'm ready, ma'am!"
    else:
        show d 76
        no "Ready, ma'am!"
    play sound doorold
    $ unlock_look("annie", 7)
    show d 79
    a "Hi guys!" with dis12
    n "Ah! The person we’ve been waiting for!"
    play sound chair4
    show d 80
    a "Sorry for the wait!" with dis
    show d 63b
    n "No worries! We just got here."
    show d 81
    no "Hi Annie! D-Did you see yesterday's episode?"with dis
    show d 82
    a "Of Aeternitas?! You bet I did!"
    show d 59
    mc "Ah, is that the new anime series based on the Universe of Eternum?"
    mc "I haven't started it yet."
    show d 81
    no "You'd better start soon then, because it's freaking AWESOME!"
    no "Did you see the scene in Andromeda? With the spaceships?"
    show d 82
    a "Oh my god, that was so AMAZING! Eliza is the best!"
    show d 81
    no "Right?! Eliza is the best character ever created!"
    no "When she went to the–"
    mc "No spoilers!" with hpunch
    show d 76b
    n "You're so cute together, girls."
    n "I didn't know you two got along so well."
    show d 82
    a "It's exciting to meet someone who watches as much television as me!"
    show d 76
    no "I'm sorry if I get too excited, it's just that... well, I never had a group of friends like this before, and..."
    no "Having someone to talk to about these kinds of things feels kinda new to me."
    show d 63b
    n "No need to apologize for anything, Nova."
    n "I've gotta say that I have a similar feeling when it comes to all of you."
    n "The scholarship that was granted to [mc] and his best friends is the best thing that has happened to me in a very long time."
    show d 83
    c "*Clears throat* I think it's best not to dig too deep into the \"best friend\" subject."
    c "Last time, feelings were hurt."
    show d 80
    if anniepath:
        a "*Laughs* Are you saying that for me?"
        a "No worries Chang, I'll concede that honor to you."
        a "I don't really care about the \"best friend\" status anymore, now that [mc] and I are..."
        show d 84b
        a "Um..."
        n ". . ."
        show d 80
        a "Are..."
        show d 85
        a "Um..." with dis08
        show v5annieshy
        a "N-Now that we are {b}SUPER{/b} best friends!"
        a "I-It's a rank above!"
        a "Y-Yeah!"
        a "Super-duper best friends!"
        a "Wait... did [mc] say Chang is his best friend?! And not me?!"
        mc "I didn–"
        scene d 86
        a "Oh, how could you?!" with dis
        a "Grrr... I'm so mad at you!"
        a "You're hopeless!" with hpunch
        a "I'm so pissed off at you. Grr!"
        mct "Annie pretending to be angry is possibly the most adorable thing I've ever seen."
        show d 58
        mc "*Clears throat* Soooo, now that we're all ready... What's the plan, Nancy?"with dis08
    else:
        a "*Laughs* No worries Chang, I'll concede that honor to you."
        a "I don't really mind anymore. I'm happy being just a good friend."
        mct "Yeah... I guess she's right."
        show d 58
        mc "Alright, so now that we're all ready... What's the plan, Nancy?"with dis
    show d 63
    n "Ah, yes!" with dis
    n "I tried to cover everything, so let me know if I'm missing anything."
    play sound ghost
    show d 87
    n "To summarize, a quick overview of all the open fronts we have... first, the Founder." with dis12
    n "The man everyone knows of, but nobody knows a thing about."
    n "We have no idea where he is, or how to find him, but he's the center of this whole ruckus."
    n "Even a tiny clue about his life in the real world would be helpful."
    n "We need to find out if there are any limits to his knowledge about Eternum, and his power in the servers."
    play sound ghost
    show d 88
    n "Next, we have... the Syndicate." with dis
    n "According to what you and Alex discovered at the party, it seems to be a group of people acting against Ulysses in some way."
    n "And they seem to be trying to help the players get the Gems of Doom... for some reason."
    play sound ghost
    show d 89
    n "Which brings us to the next point." with dis
    n "Whether there really is a conspiracy behind all of this, or whether our minds are just wandering, there's one thing we need to do for sure: Find the remaining Gems of Doom!"
    n "Obtaining influence, meeting powerful people, getting stronger... and maybe rich! Everything revolves around them."
    n "We have one, but we need 9 more!"
    play sound ghost
    show d 90
    n "So I'd say that our best bet is finding the third Weapon of Atlas."with dis
    n "Dione and our lovely elven princess have proven to be powerful assets, so if we can find the sword, we'd be unstoppable!"
    play sound2 ghost
    show d 91
    n "Either that, or... we’d need to locate another player with a Gem of Doom."with dis
    n "And... we know one who has 5 Gems in his possession."
    n "If we can find Thanatos somehow... and take his Gems... we'll be halfway there!"
    play sound ghost
    show d 63
    n "I think it'll be best if each one of us attacks a different front."with dis15
    n "We can cover more ground."
    show d 60
    mc "I have a pretty busy weekend, though."
    if lunapath and penelopepath and dayofthedead:
        mc "I'm going with Luna and her father to the Day of the Dead celebration tonight, and tomorrow we have that costume party on the campus."
    elif lunapath and dayofthedead:
        mc "I'm going with Luna and her father to the Day of the Dead celebration, and..."
    elif penelopepath:
        mc "Tomorrow we have that costume party on the campus, and..."
    show d 93
    n "No worries! I have it all under control."
    n "I didn't conquer the Peloponnese in less than a week by misemploying my men."
    show d 76b
    n "Let's see... First of all, Alex will try to find info about Ulysses or the Founder through her father and his belongings."with dis06
    n "I already asked her if she was comfortable with it, and she loved the idea. That's a thread that needs to be pulled!"
    show d 92
    n "Next, Penelope and Dalia will go to the Agora server and ask around to try to get some info about the Syndicate."with dis
    n "I feel like they’ve been at each other’s throats recently, so teaming up might do them some good."
    show d 63b
    n "Annie, could you and Luna go to the Plains of Denaria tomorrow evening?"with dis
    n "My men heard rumors about a Gem of Doom hidden in that server. I think it's worth checking out."
    show d 94
    a "Absolutely!" with hpunch
    a "I’m really familiar with that server!"
    a "We won’t fail you, Nancy! No stone will be left unturned!"
    n "Sweet!"
    show d 93
    n "And for the last mission... I'm gonna need you on Sunday morning, [mc]. Would that be possible?"with dis08
    show d 59
    mc "Sure! Sunday morning should be good. What's the plan?"
    show d 92
    n "We're gonna go to my office. I think we can get some useful info, now that my company is working with Ulysses."
    n "But don't worry too much about it for now, I'll explain the details when we get closer to it."
    show d 76b
    n "Which brings us to the device we talked about over the phone, Nova." with dis
    n "You know, the one that can steal the inventory of an Eternum player?"
    n "Could you look into it? I mean, I guess that was probably just a Hollywood fantasy, and no one is really capable of doing that."
    n "And definitely not on such short notice."
    show d 95
    no "Maybe a newbie hacker couldn't do it, but lucky for you, I know the best one in the country!"
    no "I'm already working on it, and it should be able to steal the inventory of any player when they log into Eternum. I just need to figure out how to link the device to an Eternum Visor."
    no "*Giggles* Don't worry, guys, I'll create the best hacking device your eyes have ever seen! I guarantee it!"
    show d 93
    n "Excellent!"
    n "We should do a catch-up next week with everything we've discovered!"
    show d 59
    mc "Sounds good!"
    show d 54
    c "Oh boy, I can't wait to hear the mission that I have been assigned!"
    show d 63b
    n "Oh..."
    n "*Awkward chuckle* W-Well, you don't play Eternum, so I didn't really prepare anything..."
    show d 54
    c "O-Oh..."
    c "Oh."
    play sound slam2
    play music2 sad1
    show d96
    pause
    n "I-I'm sorry! I didn't think that..." with dissolve
    c "It's okay, ma'am."
    c "There comes a day in the life of every man and woman when the sun stops shining. We must accept it. We came to suffer."
    c "For what is expectation but a kind of folly, and what is that folly but an excess of hope?"
    mc "Erm..."
    c "All I ask?"
    c "For this pain to seem purposeful."
    menu:
        with dis
        "[gr]Give a mission to Chang":
            $ changshirts = True
            mc "Um... D-Don't be sad, Chang! I have a mission for you! Something vital!" with dissolve
            mc "You've gotta go to the mall and buy us..."
            mc "Uh..."
            mc "M-Matching T-shirts! You can even choose the design!"
            mc "Every self-respecting team should have matching T-shirts!"
            mc "What do you say?!"
            stop music2 fadeout 1
            c ". . ."
            play sound slam2
            play music2 happy12
            scene d 97
            c "I'll get you the best matching T-shirts you've ever seen, guys!"
            c "Don't worry, I won't fail you!"
            mc "I'm sure you won't!"
            mc "*Chuckles* (It's easy to make him happy.)"
        "Don't give him any task":
            mc "Um... Come on, Chang! Don't be sad!"with dissolve
            mc "Next week, we'll go for an all day marathon of heist movies! How’s that sound? What do you say?"
            c ". . ."
            c "Extended versions? With director’s commentary?"
            mc "Of course!"
            stop music2 fadeout 1
            c ". . ."
            play sound slam2
            play music2 happy12
            scene d 97
            c "You've got yourself a deal, my friend!"
            c "I'll start selecting the movies!"
            mc "*Chuckles* It's easy to make you happy."
    play sound chair3
    show d 98
    n "*Standing up* Alright then, everything is settled!" with dis15
    n "I should get going now, I'm supposed to meet Penelope by the entrance."
    show d 80
    a "I'll stay for a bit, I just ordered a tea."
    show d 76
    no "Yeah, I'll stay too! I want to continue my drawing."
    show d 98
    n "No problem at all! I'll see you later."
    if nancypath:
        show d 100
        n "Actually, can you pay for my latte, [mc]?" with dis08
        n "I left my wallet at home, but I'll pay you back later, I promise."
        show d 59
        mc "Of course Nancy, and please, there's no need to pay me back."
        show d 100
        n "Aw, thank you sweetheart."
    else:
        show d 59
        mc "Yeah, I'll be on my way as well."
        if lunapath:
            mc "I don't want Mr. Hernandez to get angry because I'm late."
    play sound chair3
    show d 101
    mc "Goodbye, girls! Bye, Chang!" with dis15
    if anniepath:
        a "B-Bye, [mc]! I'll see you at home!"
    else:
        a "Bye!"
    if novapath and penelopepath:
        no "Bye [mc]! Don't forget about tomorrow's party!"
        mc "I won't!"
    else:
        no "See ya!"
    if not nancypath:
        jump dayofthedead
    stop music2 fadeout 9
    play music cafe fadein 5
    show d 102 with dis25
    pause
    play sound ding
    mc "Hi!" with dissolve
    mc "Can you ring me up?"
    show d 103
    clerk "One moment, please! I'll be right with you!"with dis
    mc "Of course, no problem."
    show d 104
    n "I think the door of the bathroom is jammed." with dis
    n "Could you help me with it, [mc]? I've gotta go before leaving."
    mc "Sure, let me check."
    n "Thank you."
    show d 106
    mc "Although... maybe they locked it." with dis12
    mc "We should ask the clerk."
    mc "Excuse me, is th–"
    play sound clothes1 volume 0.9
    show d 107 with hpunch
    pause
    play sound2 whoosh6
    play sound3 clothes2 volume 0.8
    $ renpy.music.set_volume(0.7, delay=10.0, channel='music')
    play music2 quirky5
    show v5n
    mc "W-What?!" with hpunch
    mc "What is going on?"
    scene d 109
    n "I’ll be honest, those spreadsheets turned me on..."with dis04
    show d 108
    mc "Um..."with dis04
    show d 109
    n "It's been quite a challenge trying to find you alone this past week, [mc]..."with dis04
    n "Every time we've gotten some time for ourselves, we've been interrupted. Annie, Penelope, Dalia, a call from work, or... a fucking war."
    show d 108
    mc "Y-Yeah, that was something else."with dis04
    show d 110
    n "When are we going to continue where we left off, [mc]...?" with dis
    mct "Oh boy..."
    n "I've been thinking about it since then..."
    show d 111
    mc "Well, we should find a day in Eternum to–"
    show d 110
    n "Fuck Eternum."
    n "We keep saying how there's literally no difference between Eternum and the \"real\" world, so... why should I care?"
    n "The people are the same, the consequences are the same, and surely... *whispering* the sensations are the same... if not better..."
    show d 111
    mc "*Gulps* I guess you're right."
    show d 110
    n "I'm not one of those young girls you hang out with, [mc], so... let's stop playing games and speak clearly, shall we?"
    n "I want you to fuck me, [mc]. Hard. And filthy."
    show d 111
    mc "You naughty..."
    mc "You're really turning me on right now, Nancy..."
    show d 110
    n "And I want you to fuck me NOW."
    show d 111
    mc "W-What? Now?"
    show d 110
    n "Now. Inside this restroom. With dozens of people right outside."
    n "*Giggles* I think I've never felt so horny. Not even when I was a teenager. I can’t wait anymore..."
    n "I feel like I'm gonna explode if I have to wait one more minute."
    show d 111
    mc "(Oh god, this is happening!)"
    mc "We're gonna have to be really quick..."
    show d 110
    n "Oh, don't worry, with what I'm planning to do to you... I don't think you’ll last too long."
    n "And this time, I won't let any–"
    play sound ding
    stop music2
    $ renpy.music.set_volume(1.0, channel='music')
    show d 112
    p "Hi! Have you seen my mother?"
    p "Tall, green eyes, similar body to mine, redhead?"
    if daliapath:
        d "She's 39 but looks 10 years younger."
    n "(This can't be happening again...)"
    clerk "Yeah! She went to the bathroom."
    play sound doorslam
    play sound2 dooropen1
    show d 113
    n "F-Fuck! Hide!" with hpunch
    play sound doorclose
    show d 114
    p "Ah! There you are!" with dis15
    n "Penny!"
    p "Are you ready to go shopping?"
    n "S-Sure! I was about to get out and wait for you."
    if daliapath:
        show d 115
        d "Hi Mom!" with dis
        n "Hi sweetie! I thought you were going for a run."
        d "Yeah, but I ran into my beloved sis at the park, and I knew I couldn't miss a chance to go to the mall!"
        n "I'm so happy to hear that."
        n "L-Let's go!"
    play musicb vent fadein 2
    stop music fadeout 3
    show d 116 with dis17
    p "So... did [mc] leave already?" with dis08
    n "Yep! Just a minute ago."
    p "Aw... that's too bad."
    if daliapath:
        d "Maybe if someone could run faster..."
        p "I'm wearing boots with heels!"
    blank "{i}You hear their voices fade away as they leave the place."
    mc "I can't believe this happened... {w}AGAIN!"
    mct "Every time Nancy is in the mood and something between us is about to happen, I get cockblocked by something or someone!"
    mct "What have I done to deserve this? What god have I pissed off?!"
    mc "*Sighs*"with dis
    if lunapath and dayofthedead:
        mc "(Anyway, I guess I should get going. I don't want Mr. Hernandez to get angry because I'm late.)"
    else:
        mc "(Anyway, I guess I should get going. I don't wanna stay here all day.)"
    pause
    mct "...As soon as my erection passes."with dis

label dayofthedead:
    stop musicb fadeout 4
    scene black with dis22
    if lunapath and dayofthedead:
        show screen afewminuteslater with dis
    else:
        show screen nextday with dis12
        jump costumeparty
    pause
    play musicb town_ambience fadein 8
    show dd 1
    hide screen afewminuteslater
    with Dissolve(2.6)
    pause
    mct "Alright... Spruce and Alder." with dis08
    mct "Luna's Dad is supposed to pick me up here."
    mct "I have to remember to..."
    show dd 2
    mct "Aww... FUCK." with dis12
    mct "I forgot the wine I bought to give to Mr. Hernandez as a thank you for inviting me."
    mct "I'm a fucking mess."
    mct "I’ll look so rude showing up with nothing to offer."
    play music2 dodd1 fadein 6
    stop musicb fadeout 9
    show dd 3
    blank "{i}You hear some music in the distance, as a car roars down the street at full throttle." with dis15
    play sound carstop2
    show dd 4 with dis3
    pause 2
    mct "Is that him?" with dis08
    her "HOLA, [mc!u]!!" with hpunch
    her "I LOVE PUNCTUAL PEOPLE!"
    play sound cardoor
    show dd 5
    her "*Taking a deep breath*" with dis12
    mc "*Chuckles* (Of course it’s Mr. H.)"
    show dd 6
    her "*Exhaling* Ahh! Isn't it a lovely day to celebrate the Day of the Dead?"
    show dd 5
    mc "*Chuckles* Well, I'm not so sure. I saw that it’s supposed to rain all afternoon."
    show dd 6
    her "EXACTLY! There’s nothing more appropriate!"
    show dd 5
    mc "Well, you have a point there!"
    mc "*Reaching out* It's a pleasure to see you again, Mr. Hernandez."
    play sound clothes1
    show dd 7
    her "Come give me a hug, [mc]!"with hpunch
    her "And no need for formalities. You can just call me Victor!"
    show dd 8
    mc "S-Sure! Thank you, Victor."with dis08
    her "Thank YOU for joining us today, [mc]. Luna and I are so glad you were able to join us!"
    mc "The pleasure is all mine, seriously."
    mc "I bought some wine, but..."
    her "Forget all about that!"
    her "*Sobbing* You remind me of the son I lost after he fell ill with smallpox. I see shadows of him in everything you do..."
    her "*Sobbing* Even now, you're almost bringing a tear to my eye..."
    play sound cardoor
    show dd 9
    l "You've never had a son, Dad."with dis
    l "And smallpox was eradicated decades ago."
    show dd 10
    her "Hey! It's just an old Mexican saying!"
    her "You're losing your roots, Luna!"
    show dd 13
    l "Hi [mc]." with dis12
    mc "Luna!"
    show dd 11
    mc "I feel like I haven’t talked to you in forever!"with dis
    show dd 12
    l "We saw each other yesterday in school. In psychology class."
    show dd 11
    mc "Oh... true. Well, I missed you anyway!"
    mct "I really did, though. Luna's sweet voice always makes me feel peaceful."
    show dd 12
    l "It’s good to see you too!"
    show dd 14
    her "Alright, alright, alright!" with dis12
    her "Are you ready to try the best tacos you've ever eaten, [mc]?"
    show dd 15
    mc "I can't wait!"
    show dd 14
    her "It'll be the best Day of the Dead lunch you've ever had, I guarantee."
    show dd 15
    mc "*Chuckles* Well, I haven't had many of those."
    mc "And it's 7:40 PM already, so... I'd say it's more of a dinner, actually!"
    show dd 14
    her "Oh no, it's a lunch. We're going to my brother's house."
    show dd 15
    mc "Mmm..."
    mc "I'm not sure if I’m understanding."
    mc "Why is it a lunch...?"
    show dd 14
    her "My brother lives in another state, 650 miles away."
    show dd 16
    l "We always gather together there to celebrate the Day of the Dead."
    l "It's a tradition. My grandmother came up from Mexico too."
    show dd 14
    her "It's a 10-hour drive, so we should be there by 7 AM."
    her "You can spend the morning at the pool while I cook."
    show dd 15
    mc "Wait..."
    mc "WHAT?! A 10-hour drive?!" with hpunch
    mc "I-I thought it was today!"
    mc "I can't tomorrow!"
    show dd 17
    her "Oh, really? I figured you already knew it was far away." with dis
    her "I thought I told you that already. I'm sorry..."
    mc "I mean..."
    if penelopepath:
        if novapath:
            mc "I already told Penelope and Nova that I'd be going with them to a costume party at the University tomorrow night, so..."
        else:
            mc "I already told Penelope that I'd be going with her to a costume party at the University tomorrow night, so..."
        show dd 14
        her "Oh... at night, you said?"with dis
        her "Then there's no problem!"
        her "Luna will stay until Monday, but I need to come back sooner since I can't keep the cafe closed for so many days."
        her "I can drive you! We’ll just have to leave after eating."
        show dd 15
        mc "Oh, really? You don't mind? And will we make it back in time?"
        show dd 14
        her "For sure. I know the road, I can make it a 7-hour drive. Or less, if the weather's good."
        show dd 15
        mc "Um..."
        mct "T-That sounds dangerous."
        menu:
            with dis
            "[gr]Get in the car":
                mc "Well, in that case..."with dissolve
                mc "Alright, let's do it!"
            "Don't risk tomorrow's party":
                mc "I appreciate the offer, but I don’t want to risk it. And I don't want to risk a car accident or getting a ticket or something for driving too quickly."with dissolve
                show dd 17
                her "Oh... are you sure? Don't worry about the risk, [mc], I’ve done the trip plenty of times, we’d almost definitely get back in time."with dis
                mc "No worries, it's okay, Victor."
                mc "And I'm so sorry, I really wanted to go. Maybe next year!"
                show dd 18
                her "Yeah... I guess we always have next year." with dis
                her "Well, it is what it is. Take care, son."
                her "Let's go, Luna, we've gotta go."
                play sound cardoor
                show dd 19
                if penelopepath:
                    l "Sorry the college party clashes with the Day of the Dead celebration, [mc]. I know you really wanted to hang out with everyone at the University."with dis12
                    l "I didn't realize the party would be on the same day."
                else:
                    l "I'm sorry about it." with dis12
                mc "Hey, it's no one's fault! It was just a misunderstanding."
                l "Yeah..."
                l "But it's okay. Thank you anyway, [mc]."
                l "I'll see you at school."
                mc "Bye! Have fun!"
                l "Goodbye."
                play sound2 caraway2
                show dd 20 with dis25
                mct "Damn..." with dis
                mct "That was cold. It kinda broke my heart to flake on her like that."
                mct "But I can’t miss that party! All those older college chicks... the University of Kredon better get ready for me!"
                mct "Anyways... I guess my plans for today are just Netflix and Eternum."
                mct "And I guess I could look into making last minute adjustments for my costume tomorrow, too."
                mct "Could be worse!"
                $ lunapath = False
                $ lunau = False
                stop music2 fadeout 4
                scene black with dis22
                show screen nextday with dis12
                jump costumeparty
    else:
        mc "Well, now that I think about it, I don't really have any plans until Sunday morning..."
        mc "We would definitely be back tomorrow?"
        show dd 14
        her "Yes!" with dis
        her "Luna will stay until Monday, but I need to come back sooner since I can't keep the cafe closed for so many days."
        her "I can drive you! We’ll just have to leave after eating."
        show dd 15
        mc "Well, in that case... alright, let's do it!"
    show dd 14
    her "EXCELLENT!" with hpunch
    her "Everyone, to the car!"
    show dd 21 with dis15
    her "Don't worry [mc], time will fly by."with dissolve
    her "Moreover, Fiero's seats are super comfortable. You'll be able to sleep better than in your own bed."
    mc "Fiero?"
    her "This beautiful car!"
    her "He's older than Luna, and he’s never let me down."
    l "My dad takes very good care of this Jeep. Fiero doesn't have a scratch."
    l "He even tried convincing me Fiero was my older brother when I was younger."
    her "Of course. He's like the son I lost after he–"
    l "Dad!"
    her "*Clears throat* But enough talking, hop in!"
    play sound cardoor
    show dd 22
    l "You can sit in the front seat. The seat’s more comfortable." with dis12
    show dd 23
    mc "Don't worry about me! I'm the guest, I'll sit in the back."
    show dd 22
    l "Seriously, I insist."
    l "I prefer to sit in the back anyway."
    show dd 23
    menu:
        with dis
        "Sit in the front":
            $ sitcarfront = True
            mc "Okay, I'll be your father's co-pilot, then. I could probably catch some Zs too."with dissolve
            show dd 28 with dis15
        "Sit in the back with Luna [luna_pts]":
            mc "How about we both go in the back!" with dissolve
            mc "...If you don't mind the company, that is?"
            $ luna_points += 1
            play sound beat
            show dd 23b
            show screen heartbeat
            l "No... not at all! I-If that’s what you want."with dis
            show dd 24 with dis15
    play sound2 cardoor
    her "Alright, is everyone ready?" with dissolve
    mc "Yes, sir!"
    if not sitcarfront:
        show dd 27
        l "Ready!"
        show dd 25
        mc "Should I look for a spot to stop at for a quick dinner on the way?"with dis
        show dd 26
        l "There are a couple of things to eat in the car, but... it'll probably be best if we stop at a diner on the road."
        show dd 29
        her "Nonsense."
    else:
        show dd 27
        l "Ready!"
        show dd 28
        her "Very well, then."
        mc "Should I look for a spot to stop at for a quick dinner on the way?"
        show dd 29
        her "Nope, totally unnecessary!" with dis08
    her "Luna woke up extra early today and cooked up a storm! There are snacks and cookies and sandwiches, just for you!"
    show dd 30
    l "They're for everyone!"
    show dd 29
    her "But you went to the cafe expressly to get carrot cake because you know [mc] loves it. And besides, how am I supposed to eat if I’m driving your brother?"
    mc "Is there cake?!"
    show dd 30
    l "Dad! Stop embarrassing me! And stop calling Fiero my brother!"
    show dd 28
    her "Okay, okay, sorry sweetie."
    her "LET'S GO!"
    play soundlow thunder
    stop music2 fadeout 9
    show dd 31 with dis2
    l "Oh, looks like the rain finally caught up with us." with dissolve
    show dd 32
    mc "*Looking through the window* Yeah, I think it's about to..." with dis
    play sound thunder
    $ renpy.music.set_volume(0.5, channel='music2')
    $ renpy.music.set_volume(1.0, channel='musicb')
    pause .5
    play music rain3 volume 3
    play musicb raincar volume 3
    play soundloop raincar volume 3
    show dd 33 with dis25
    mc "And there we go!"with dissolve
    mc "Wow, it's really coming down out there."
    show dd 34
    her "Yeah, the internet said it would be raining until early morning." with dis12
    mc "Well, at least it'll stop by the time we get there."
    her "So they said, yeah."
    if sitcarfront:
        show dd 35b
    else:
        show dd 35
    her "I hope you love the rain as much as my daughter does, [mc]." with dis12
    mc "Oh, I do!"
    mc "I’m still getting used to living in Kredon, so I'm not tired of the rain yet!"
    her "Good!"
    her "Luna could spend hours looking through a window during the rain."
    l "It's just so... relaxing."
    mc "Will this be a problem? Having to drive such a long distance in this weather?"
    her "Not at all."
    her "The more it rains, the more the car will slide and the faster we'll arrive."
    show dd 36
    mc "Um... I'm not sure that's how..."with dis12
    play sound caraway2
    her "LET'S GO!{w=2}{nw}" with hpunch
    stop musicb fadeout 4
    stop soundloop fadeout 4
    show dd 37 with dis22
    pause
    stop music fadeout 3
    scene black with dis25
    play musicb car_rain fadein 4
    pause .1
    show screen afewhourslater with dis22
    pause
    hide screen afewhourslater
    show rr0
    show dd 38
    with dis25
    pause
    if sitcarfront:
        mc "Mmmmm..."with dis12
        scene rr2
        show dd 39
        l "Are you feeling better, [mc]?"with dis
        show dd 40
        mc "Mmm yeah, I think I am, thank you."
        mc "All those curvy roads were giving me some motion sickness... too bad we can’t roll the windows in this downpour. But I've started to feel much better after sitting back here."
        show dd 51
        her "This road is basically straight for about 50 miles. That should help."with dis
        scene rr0
        show dd 38
        mc "*Looking through the window* Yeah, I noticed!"with dis
    else:
        mc "Where are we now? I'm totally lost." with dis12
        her "We left the state already!"
        her "Now we're in... the middle of nowhere, basically."
        her "This road is practically straight for about 50 miles, and then we just have to cross through some woods, and we'll be there."
        mc "Great!"
    mc "What time is it, by the way? It's pitch-dark out there already."
    her "Mmmm..."
    her "11:55 PM."
    mc "Damn, really?!"
    scene rr1
    show dd 49b
    mc "Time ran by so quickly!"with dis12
    scene rr2
    show dd 39
    l "True. It seems like we left Kredon only a few minutes ago."with dis12
    show dd 40
    mc "Must be the good company! You're really making time fly by."
    show dd 51
    her "Thank you, [mc]."with dis08
    her "Luna and I have a pretty unique rapport, but you really seem to have adapted to it quickly!"
    show dd 40
    mc "*Chuckles* Well, I was referring more to Luna, but it's impossible to get bored with you around, Victor!"
    show dd 39
    l "That horror podcast we listened to before also helped. I was on the edge of my seat."
    show dd 40
    mc "I know! It was amazing!"
    mc "Is it true that all the stories are based on real events?"
    show dd 39
    l "Yeah, it is. It’s like a true crime series."
    l "They collect stories and testimonies from all over the country."
    show dd 45
    l "I think they even had an episode about a homicide that happened around here..."with dis06
    mc "W-What? Here as in... {i}this road?"
    show dd 51
    her "Yeah, I remember what Luna’s talking about. There's a small side road about 10, maybe 20 miles from here."with dis08
    her "It leads to a farm where the son murdered his entire family."
    mc "Holy shit..."
    play soundlow thunder fadein 1
    show dd 46
    l "Found it!"with dis08
    l "According to Google, he claimed to have been obeying voices inside his head."
    l "He skinned them alive and cut off their limbs."
    mc "*Gulps*"
    l "The farm is abandoned nowadays, but this forum says that visitors have claimed to have seen visions or heard voices..."
    show dd 47
    mc "My... g-god!"
    mc "That's some pretty good nightmare fuel."
    show dd 46
    l "It would be awesome to visit that farm one day... It's too bad we're on a tight schedule today."
    show dd 47
    mc "Ah, yeah, you’re r-right. That's too bad. It would have been awesome. Darn it."
    mct "Thank you, Jesus."
    show dd 45
    l "We can definitely visit it another day, though!"with dis
    l "It's not that far. Maybe once I have my driver’s license."
    show dd 40
    mc "*Trying to change the subject* H-Hey, you know what we should do now?!"with dis
    mc "Play a game!"
    mc "Anyone have a suggestion?"
    show dd 51
    her "Why don't we play that thing we were playing the other day, Luna?"with dis
    her "That one about guessing people."
    show dd 41
    l "Sure!" with dis08
    show dd 39
    l "Do you wanna play, [mc]?"
    show dd 40
    mc "Play what?"
    show dd 39
    l "Do you know \"20 Questions\"? It's the same thing, but you only try to guess people, so we reduced it to 10 questions."
    l "You have to guess the person I'm thinking about by asking a maximum of 10 yes or no questions."
    l "It can be a fictional person or a real one, and they can be dead or alive."
    show dd 40
    menu q10game:
        with dis
        "[gr]Play the game":
            $ renpy.music.set_volume(0.4, channel='music3')
            mc "Sounds awesome! Let's do it."with dis06
            play music3 investigate
            mc "I can ask 10 questions about the person you're thinking about, and you can only say yes or no, right?"
            show dd 39
            l "Correct."
            show dd 40
            mc "Alright! I’ll start guessing, then!"
            show dd 45
            l "Okay, let me think..."with dis08
            $ q10 = renpy.random.randint(1, 3)
            show dd 39
            l "Alright, I have one." with dis08
            l "Shoot."
            $ qqq = 0
            $ qcount = 0
            menu:
                with dissolve
                mod "Play and win twice to get an extra point with Luna."
                "See possible answers":
                    mod "It can be Raul, Nova or Idriel."
                "Continue":
                    pass
            jump gamequizroad
        "Pass":
            mc "Oof, that sounds complicated. I'm not good at these things."with dis06
            mc "There's just too many people in the world. I don’t want to make a fool of myself."
            show dd 39
            l "Do you have any other ideas?"
            show dd 40
            mc "Mmmm... Let me think..."
            jump posgameroad
label gamequizroad:
    if qcount >= 10:
        show dd 45
        l "And if I'm not mistaken... that was your 10th question!"with dis
        show dd 39
        l "You have to guess now."with dis08
        show dd 40
        mc "Oh!"
        mc "Alright... I think I know..."
        $ guessq10 = renpy.input("What person is Luna thinking of?", exclude='\\[{0123456789')
        $ guessq10 = guessq10.title()
        if guessq10 == __("Raul"):
            mc "Is it..."
            play sound pop
            show draul
            mc "Raul?"
            if q10 == 1:
                $ q10 = renpy.random.randint(2, 3)
                hide draul
                jump playagainroad
            else:
                hide draul
                play sound2 ghost
                jump wrongchoiceroad
        elif guessq10 == __("Idriel"):
            mc "Is it..."
            play sound pop
            show didriel
            mc "Idriel?"
            if q10 == 2:
                $ q10 = renpy.random.randint(3, 3)
                hide didriel
                jump playagainroad
            else:
                hide didriel
                play sound2 ghost
                jump wrongchoiceroad
        elif guessq10 == __("Nova"):
            mc "Is it..."
            play sound pop
            show dnova
            mc "Nova?"
            if q10 == 3:
                $ q10 = renpy.random.randint(1, 2)
                hide dnova
                jump playagainroad
            else:
                hide dnova
                play sound2 ghost
                jump wrongchoiceroad
        else:
            mc "Is it..."
            mc "[guessq10]?"
            jump wrongchoiceroad
    show dd 40
    menu q10menu:
        with dis
        "Is this person a woman?" if qq1:
            $ qcount += 1
            $ qqq += 1
            $ qq1 = False
            show dd 39
            if q10 == 1:
                l "No!" with dis04
                show dd 40
                mc "So it's a man..."
            elif q10 == 2:
                l "Yes." with dis04
            else:
                l "Yes." with dis04
            jump gamequizroad
        "Is this person famous?" if qq2:
            $ qcount += 1
            $ qq2 = False
            show dd 39
            if q10 == 1:
                l "Not that I'm aware of!" with dis04
                $ qq5 = True
            elif q10 == 2:
                l "Yes... you could say that." with dis04
                $ qq6 = True
            else:
                l "Nope." with dis04
                $ qq5 = True
            jump gamequizroad
        "Was this person born in the USA?" if qq3:
            $ qcount += 1
            $ qq3 = False
            show dd 39
            if q10 == 1:
                l "I don't think so." with dis04
                $ qq4 = True
            elif q10 == 2:
                l "No." with dis04
                $ qq4 = True
            else:
                l "Yes." with dis04
                $ qqq += 1
            jump gamequizroad
        "Is this person living in the USA now, though?" if qq4:
            $ qcount += 1
            $ qqq += 1
            $ qq4 = False
            show dd 39
            if q10 == 1:
                l "Yeah!" with dis04
            elif q10 == 2:
                l "The answer is still no!" with dis04
            jump gamequizroad
        "Does this person go to our school?" if qq5:
            $ qcount += 1
            $ qqq += 1
            $ qq5 = False
            show dd 39
            if q10 == 1:
                l "Yes!" with dis04
            elif q10 == 3:
                l "No!" with dis04
            jump gamequizroad
        "Are they a movie star or a athlete?" if qq6:
            $ qcount += 1
            $ qqq += 1
            $ qq6 = False
            show dd 39
            l "Wrong!" with dis04
            jump gamequizroad
        "Is this person our age?" if qq7 and qqq > 0:
            $ qcount += 1
            $ qqq += 1
            $ qq7 = False
            show dd 39
            l "No!" with dis04
            if olderroad:
                show dd 40
                mct "Older or younger, then? Mmm..."
                mct "They have to be older... right?"
                $ olderroad = False
            jump gamequizroad
        "Have I ever seen this person... in Eternum?" if qq8 and qqq > 1:
            $ qcount += 1
            $ qqq += 1
            $ qq8 = False
            show dd 39
            l "Yeah, you have." with dis04
            jump gamequizroad
        "Is this person... pretty? [gr][mt](ask at least once)" if qq9 and qqq > 2:
            $ qcount += 1
            $ qqq += 1
            $ qq9 = False
            if prettyroad:
                show dd 43
                l "Um..."with dissolve
                l "Well, I guess that would be subjective, wouldn't it?"
                show dd 51
                her "Not always!"
                her "Look at me! I'm handsome!"
                her "100\% objective."
                show dd 41
                l "*Chuckles* No one can deny that!"
                show dd 51
                her "Like father, like daughter!"
                her "Don't you think Luna's pretty, [mc]?"
                her "I always tell her that, but she says I'm looking at her through a father's eyes."
                show dd 44
                l "D-Dad!"with hpunch
                show dd 44b
                her "[mc]?" with dis08
                menu:
                    with dis
                    "She's perfect [luna_pts]":
                        mc "She's perfect." with dissolve
                        $ luna_points += 1
                        play sound2 beat
                        show screen heartbeat
                        her "AH, YOU HA–"
                    "No opinion":
                        mc "*Laughs* I prefer to stay out of this discussion."with dissolve
                show dd 44
                l "S-Stop interrupting, Dad!" with dis04
                l "Can we go back to the game?"
                show dd 44b
                mc "*Chuckles* Hey, I asked a question and no one answered!"with dis03
                show dd 44
                l "Because it depends on who you ask!"with dis03
                show dd 44b
                mc "Let me rephrase it, then..."with dis03
                mc "Is this person pretty... to {i}you?"
                show dd 45
                l "Oh... to me?"with dis
            if q10 == 1:
                show dd 43
                l "Um... I wouldn't say that's their most defining trait." with dis06
                l "To me, at least."
                if prettyroad:
                    show dd 40
                    mc "*Chuckles* I understand."
                    $ prettyroad = False
            elif q10 == 2:
                show dd 39
                l "Yeah! For sure!" with dis06
                if prettyroad:
                    show dd 40
                    mc "Thank you!"
                    $ prettyroad = False
            else:
                show dd 39
                l "Yeah! Absolutely!!" with dis06
                if prettyroad:
                    show dd 40
                    mc "Thank you!"
                    $ prettyroad = False
            jump gamequizroad
        "Is this person smaller than the average person?" if qq10 and qqq > 3:
            $ qcount += 1
            $ qq10 = False
            show dd 39
            if q10 == 1:
                l "Nope." with dis04
                $ qq11 = True
            elif q10 == 2:
                l "No." with dis04
                $ qq11 = True
            else:
                l "Mmm... yeah, you could say that." with dis04
                show dd 40
                mc "Ohh, interesting..."
                $ qq12 = True
            jump gamequizroad
        "Is this person bigger than the average person, then?" if qq11:
            $ qcount += 1
            $ qq11 = False
            $ qqq += 1
            show dd 39
            if q10 == 1:
                l "You might say that, yes." with dis04
            elif q10 == 2:
                l "Mmm... no, neither." with dis04
                show dd 40
                mc "Mmmm... average then, I see." with dis04
            jump gamequizroad
        "Is their hair brown?" if qq12:
            $ qcount += 1
            $ qq12 = False
            $ qqq += 1
            show dd 39
            l "Nope!" with dis04
            show dd 40
            mc "Mmmmm... It's not who I was thinking, then..."
            jump gamequizroad
        "Is this person alive?" if qq13 and qqq > 4:
            $ qcount += 1
            $ qq13 = False
            show dd 39
            if q10 == 2:
                l "I have to say... no, I guess." with dis04
                $ qq14p = True
            elif q10 == 1:
                l "Yes." with dis04
                $ qqq += 1
            else:
                l "Yes." with dis04
                $ qqq += 1
            jump gamequizroad
        "This person's eyes are green?" if qq14p:
            $ qcount += 1
            $ qq14p = False
            show dd 39
            l "Um... *giggles* I don't know." with dis04
            show dd 40
            mc "You... don't know?"
            mc "Ohhh..."
            $ qq14 = True
            jump gamequizroad
        "Does this person usually have something covering their eyes?" if qq14:
            $ qcount += 1
            $ qq14 = False
            show dd 39
            if q10 == 2:
                l "Yes..." with dis04
                $ qq15 = True
            elif q10 == 3:
                l "Yes..." with dis04
                $ qq16 = True
            jump gamequizroad
        "Is this person an AI?" if qq15:
            $ qcount += 1
            $ qq15 = False
            show dd 39
            l "*Giggles* Yes!" with dis04
            show dd 40
            jump gamequizroad
        "Is this person a hacker?" if qq16:
            $ qcount += 1
            $ qq16 = False
            show dd 39
            l "*Giggles* Yes!" with dis04
            jump gamequizroad
        "Does this person have a brother or a sister?" if qq17 and qqq > 5:
            $ qcount += 1
            $ qq17 = False
            if q10 == 1:
                show dd 43
                l "Um... I'm not sure." with dis04
                l "But if not a brother... they have someone very close."
                $ qq18 = True
            elif q10 == 2:
                show dd 39
                l "Nope." with dis04
                $ qqq += 1
            else:
                show dd 39
                l "Nope, only child." with dis04
                $ qq14 = True
            jump gamequizroad
        "Does this person have a prominent mustache?" if qq18:
            $ qcount += 1
            $ qq18 = False
            show dd 39
            l "*Giggles* Yes!" with dis04
            jump gamequizroad
    jump q10game
label wrongchoiceroad:
    show dd 43
    l "NO!" with dis06
    l "Wrong!"
    scene rr1
    show dd 50
    mc "Really? Dammit, I was positive I had it."
    mc "Who was it?"
    scene rr2
    show dd 39
    if q10 == 1:
        l "Raul!"
    elif q10 == 2:
        l "Idriel!"
    else:
        l "Nova!"
    show dd 40
    mc "Oh... {w}OH!"
    mc "Now that you mention it, that makes sense!"
    mc "Okay, okay, now it's my turn!"
    jump posgameroad
label playagainroad:
    play sound2 ghost
    show dd 39
    l "YES!" with dis06
    l "Good job!"
    show dd 40
    mc "NICE!"with hpunch
    if endroadgame:
        $ luna_points += 1
        play sound beat
        show screen heartbeat
        show dd 39
        l "You're really good at this!" with dis04
        show dd 40
        mc "Thanks!"
        mc "It's all about asking the right questions."
        mc "Okay, okay, now it's my turn!"
        show dd 39
        l "Think of someone."
        show dd 40
        mc "Mmm... done! Are you ready?"
        show dd 39
        l "Yes!"
        l "Let me think..."
        l "Is your person a woman?"
        show dd 40
        menu:
            with dis
            "Yes":
                mc "Yes!" with dissolve
                show dd 39
                l "Is it me?"
            "No{#0.5,lunagame}":
                mc "No!" with dissolve
                show dd 39
                l "Is it my father?"
        stop music3
        scene rr1
        show dd 49b
        mc ". . ."
        show dd 49c
        mc "Dammit." with dis
        mc "Why do I always suck at games?"
        scene rr2
        show dd 39
        l "*Giggles* It's just that me and my father have played this a lot."
        l "A simple \"yes\" or \"no\" can have a lot of meanings, depending on the tone."
        show dd 40
        mc "Let me try again!"
        jump posgameroad
    $ endroadgame = True
    $ qq14p = False
    show dd 39
    l "Do you wanna play again?"
    show dd 40
    menu:
        with dis
        "[gr]Yes{#0.5,playagain}":
            mc "You bet! I'm on a roll!" with dissolve
            show dd 45
            l "Okay, let me think of another one..."with dis08
            l "Um..."
            show dd 39
            l "Alright, I'm ready." with dis08
            show dd 40
            mc "This time I'm gonna discover it even faster!"
            $ qq1 = True
            $ qq2 = True
            $ qq3 = True
            $ qq4 = False
            $ qq5 = False
            $ qq6 = False
            $ qq7 = True
            $ qq8 = True
            $ qq9 = True
            $ qq10 = True
            $ qq11 = False
            $ qq12 = False
            $ qq13 = True
            $ qq14 = False
            $ qq15 = False
            $ qq16 = False
            $ qq17 = True
            $ qq18 = False
            $ qqq = 0
            $ qcount = 0
            jump gamequizroad
        "No{#0.5,playagain}":
            mc "No way! I'm taking my unbeaten record home!" with dissolve
            show dd 39
            l "*Chuckles* Fair enough."
            jump posgameroad
label posgameroad:
    stop music3 fadeout 5
    show dd 51
    her "Hey guys, I hate to interrupt but..."with dis
    her "I'm seeing a gas station ahead, and I don't really know if there are any others beyond this point. Can anyone check?"
    show dd 46
    l "Uh... according to Google Maps, this is the last one until Uncle Hugo's house."with dis08
    show dd 51
    her "Then we're gonna make a quick stop. You don't mind, do you?"
    show dd 41
    l "No problem!"
    stop musicb fadeout 4
    play music rain2 fadein 5
    scene dd 51b with dis25
    pause
    play sound carstop2short
    show dd 52 with Dissolve(2.6)
    pause .6
    mc "Damn, this place would be perfect for one of your stories, Luna."with dis08
    mc "It could be the scenario of a horror movie."
    play sound2 cardoor
    show dd 53
    her "OH! He's very right!" with dis12
    her "It looks half-abandoned, but the sign says “Open”."
    her "I'll head inside to pre-pay the pump."
    her "If I'm not back in 3 minutes, come inside and avenge me."
    mc "*Laughs* I will, I promise."
    play sound cardoor
    show dd 54
    l "*Stretching* GGGgggg...!" with dis12
    mc "Are you feeling stiff?"
    show dd 55
    l "Well, not that much, I just needed to stretch my legs for a moment." with dis
    l "Although I do feel a bit sleepy already."
    show dd 56
    mc "Yeah, I think it would be good for us to sleep a bit now."with dis04
    mc "We'd be there by the time we wake up and we'd feel much better tomorrow."
    mc "I'm just sorry about your dad."
    show dd 55
    l "Don't be. He always sleeps very little, and today he even woke up late."with dis04
    l "He'll probably be as fresh as a daisy tomorrow."
    show dd 56
    mc "That makes me feel better, then!"with dis04
    show dd 57
    l "I think I'll go back to the car now."with dis12
    l "*Slightly trembling* It's a little chilly out here."
    show dd 58
    mc "Yeah, the rain has cooled the air!"with dis04
    mc "I'll go for a walk around the station while your father is inside."
    mc "I'll be right back!"
    play soundlow thunder fadein 2
    play sound cardoor
    show dd 52 with dis25
    pause
    mc "Ahh, I love this smell." with dis
    show dd 59
    mc "*Taking a deep breath*"with dis22
    mct "I don't care what people say, I love the rain, and I always will."
    mct "I feel like I could never grow tired of it."
    mct "It gives me... peace of mind."
    mc ". . ."
    play music3 twinkle fadein 30
    mct "Man, I want to stay here forever."
    mct "If I can convince Annie and Chang to stay in Kredon as well... there would be nothing pulling me back home."
    mct "I mean, Dad has only called me once since I got here."
    mct "He wouldn’t even care."
    mct "And the people I’ve spent time with this month have all been so amazing. I can't leave them behind."
    mct "I just... can't."
    mct "Imagine studying at the University of Kredon!"
    mct "With all the girls!"
    mct "And Chang!"
    mct "God knows what amazing things we could get up to in those 4 years..."
    show dd 60
    mct "*Trembling* Uggh, I'm starting to feel a bit cold too."with dis
    show dd 59
    mct "I should get back to the–"with dis06
    show dd 61
    mc ". . ." with dis17
    show dd 62 with dis15
    pause
    show dd 63 with dis17
    pause
    mc "What..." with dis
    show dd 64 with dis12
    pause
    mc "*Nervous laugh* What?"with dis
    mc "I-Is this a tribute of some sort or...?"
    mc "H-Has that thing always been there?"
    show dd 65
    mc "W-What the fuck is going on...?"with dis
    play soundloop whispers volume 0.7
    show ddpre
    mc "H-How...{w=1}{nw}"
    play sound deception
    play sound2 whoosh2
    show dd66
    mc "*Turning around on a whim* W-WHO'S THERE?!"with hpunch
    mc "THIS IS NOT FUNNY!" with hpunch
    mct "What the fuck are these whispers?!"
    play sound3 deception
    play sound4 whoosh2
    scene dd67
    mc "*Hyperventilating* I K-KNOW Y-YOU'RE THERE!"with hpunch
    mct "Fuck, not this goddamn migraine again..."
    mc "W-Whoever it is, show yourselves!"with hpunch
    play sound deception
    play sound2 whoosh2
    scene dd68
    mc "ENOUGH!" with hpunch
    mct "W-Where's this voice coming from?!"
    play sound3 deception
    play sound4 whoosh2
    scene dd70
    mc "*Spinning on yourself* F-FUCKERS!"with hpunch
    play sound deception
    play sound2 whoosh2
    scene dd68
    mc "STOP!!!" with hpunch
    play sound3 deception
    play sound4 whoosh2
    scene dd70 with hpunch
    pause .2
    play sound deception
    play sound2 whoosh2
    scene dd67 with hpunch
    pause .2
    play sound5 deception
    play sound6 whoosh2
    stop soundloop
    play music fireplace
    stop music3
    scene dd69 with hpunch
    pause
    mc "*Hyperventilating* Wha..."with dis12
    play soundlow fallkitchen volume 0.75
    player "I don't give a shit about who you are! If you don't pay me, I'll put some dents into you!" with dis
    player "Do you think I won't do it because you're a woman?"
    player "Because I will!"
    show dd 70
    ca "Oh, please, I just drank one cup of that thing you call “ale”." with dis15
    ca "You should be grateful that the Princess deigned to step into your filthy inn, commoner."
    player "Look, this outfit and roleplay of yours might work on horny teenagers, but not me."
    player "This is my real job, and I won't let you leave without paying."
    ca "*Sighs* As I have told you, I do not have any money with me now."
    ca "We will need to discuss a compromise. As soon as I can access the treasury housed in El–"
    play soundlow slam
    show dd 70b
    player "ENOUGH!" with hpunch
    player "PAY ME NOW, BITCH!"with hpunch
    player "OR ELSE..."
    play sound thunder
    play music firespell
    play soundloop electricity
    play sound3 spell
    scene caly05
    ca "{sc=2}...OR ELSE WHAT?!{/sc}" with hpunch
    player "H-Holy shit!"
    ca "I AM CALYPSO, PRINCESS OF THE SY-TEL-QUESSIR."
    ca "I AM THE LAST OF MY BLOODLINE."
    ca "I WAS BORN TO RULE OVER ALL RACES!"
    ca "AND NEITHER YOU NOR ANYONE ELSE CAN COMMAND ME!"
    player "O-Okay, okay!"
    player "Jesus Christ, please don't kill me, I'm level 24 already!"
    ca "Get out of my sight!"
    player "Y-Yes!"
    play sound run
    scene dd 72
    bla "The man leaves the inn running for his life."with dis12
    ca "And from now on, I can drink here without paying!"
    player "O-Of course!"
    player "It's on the house!"
    play musicb fireplace
    play sound spell
    stop music fadeout 1
    stop soundloop fadeout 1
    show dd 73 with dis12
    play sound2 doorecho
    pause 1
    ca "How dare he..." with dis12
    mc "Why..."
    mc "W-Why am I seeing this...?"
    show dd 74
    ca "Huh?" with dis
    ca "[mc]? When did you get here?"
    mc "What...?"
    mc "You can hear me?"
    ca "[mc]!"
    mc "Yeah! It's me!"
    mc "I don't know how I got here!"
    l "[mc]!"
    mc "What?"
    play sound deception
    play sound2 thunder
    play musicb rain2 fadein 8
    show caly05b
    l "[mc]!"
    scene dd 75
    mc "F-FUCK!"with dis03
    mc "Wha... What?!"
    mc "Where am I...?"
    show dd 76
    l "At the gas station. You started screaming and talking alone all of a sudden."with dis03
    show dd 75
    mc "*Recovering your breath* Oh... oh god..."with dis03
    mc "That was so scary!"
    mc "I-I don't know what happened, I started seeing Exit Portals, and voices, and then I was in some kind of medieval inn... I even saw Calypso!"
    show dd 76
    l "Like... a bleeding case?"with dis03
    show dd 75
    mc "Bleeding? Oh, that thing when people start hallucinating Eternum servers in the real world?"with dis03
    mc "God, it's possible..."
    mc "But I thought that only happened to people who had spent thousands and thousands of hours in Eternum!"
    show dd 76
    l "You've been playing a lot during the past weeks, though. While having pretty intense sessions."with dis03
    l "And maybe the 100\% compatibility accelerated things too."
    show dd 75
    mc "Mmmm... yeah, it's a possibility."with dis03
    show dd 77
    l "In any case, Ulysses made it clear that the bleeding isn't dangerous, so don't worry!" with dis
    l "A weekend without playing Eternum will do you good."
    show dd 78
    mc "Yeah... I guess you're right."
    mc "I'm not gonna log into Eternum until next week!"
    mc "I've probably been playing too much lately. And while I was logged off, I was still thinking about it..."
    mc "I needed to touch some grass!"
    show dd 77
    l "Exactly!"
    play sound storebell volume 0.8
    show dd 79
    clerk "Thank you very much, come back soon!" with dis12
    her "HAHA! We just hit the jackpot, guys!"
    her "They're having a promotion where you can get two full sacks of coal for free if you fill your tank! TWO!"
    her "I can smell next week's BBQ already!"
    her "Everyone back to the car, quickly!"
    play sound2 cardoor
    show dd 77
    l "What do you say? Should we get back on the road?"with dis
    show dd 78
    mc "For sure! I feel fine already, it was just a scare."
    mc "Let's go!"
    play music car_rain fadein 3
    stop musicb fadeout 4
    scene rr0
    show dd 38
    with dis25
    pause
    mct "I know that what happened is supposed to be “normal”, but... damn."with dis
    mct "I wasn't expecting the bleeding to feel so real. It felt like I was really playing Eternum."
    mct "I could see Calypso as if she was really in front of me... I even almost tried to talk to her."
    mct "Heh, I can't wait to tell her what happened."
    mct "Luna's right, though. A few days of not playing will do me good."
    mct "I don't want it to happen again."
    mct "I mean, what if it happened while going down some stairs? Or driving?!"
    mct "What if–"
    play sound clothes3
    scene dd 80
    blank "{i}You suddenly feel Luna's head falling over your shoulder as she falls asleep." with dis12
    show dd 81
    mc "*Chuckles* (She did say she was starting to feel sleepy.)"with dissolve
    mct "She looks so cute while she sleeps."
    menu:
        with dis
        "Do nothing":
            scene rr0
            show dd 38
            with dis12
            mc "*Yawns*" with dis
            mct "I should try to get some sleep too."
            mct "Tomorrow's an action-packed day, so I've gotta be full of energy!"
            mct "I wonder if it will still be raining when I wake up..."
        "Put your arm around her [luna_pts]":
            play sound2 clothes3
            show dd 83 with dis15
            $ luna_points += 1
            play sound beat
            show screen heartbeat
            pause
            l "*Talking in her sleep* {bt=3}Thank you for coming, [mc]...{/bt}" with dis08
            mc "*Chuckles*"
            show dd 84
            l "{bt=3}We must return the body we exhumed to kill all the zombies...{/bt}"with dis
            mc ". . ."
        "Caress her body":
            show dd 85
            mct "Sometimes it's hard to notice because of the way she dresses, but Luna has such a nice body..."with dis
            mct "Even with this hoodie... I can almost feel her figure pressed against me..."
            mct "I wonder if she's wearing a bra."
            show dd 86
            mct "Maybe I could have a little feel through her clothes?" with dis
            mct "She wouldn't notice..."
            her "*Clears throat*"
            show dd 87
            mc "*Looking up in the rearview mirror*"with dis08
            play sound jumpscare
            show dd 88
            pause
            show dd 89 with dis15
            mc "*Gulps*"with dissolve
            scene rr0
            show dd 38
            her "Is everything okay back there, [mc]?" with dis15
            mc "P-Perfectly fine, sir!"
            her "Good! Good..."
            her "You should try to get some sleep now."
            mc "I-I'll try, sir!"
            mct "Jesus, that was scary..."
            mct "He's right, though. I should try to get some sleep too."
            mct "If I can..."
    stop music fadeout 4
    show black with dis27
    pause .1
    show screen afewhourslater with dis17
    pause
    play musicb birds fadein 2
    hide screen afewhourslater
    scene dd 90
    with dis25
    pause .1
    mc "Zzzzz..." with dis
    play sound doorbell
    her "Hugo! We're here!"
    her "Come on, kids, wake up!"
    show dd 91
    l "Mmm..." with dis
    show dd 92
    l ". . . ?" with dis08
    play sound3 clothes3
    show dd 93 with dis08
    pause .4
    play sound cardoor
    pause .2
    mc "Zzzz..." with dis08
    play sound2 doorbell
    her "HUGO!" with hpunch
    show dd 94
    mc "Hmm...?" with dis
    mct "Oh, we’re already here?"
    play sound cardooropen
    play sound2 clothes3
    show dd 95 with dis15
    mc "*Yawns* AAaaaghh! G-God, I slept like a baby! This car sure is comfortable, Mr. H." with dissolve
    her "Good morning, [mc]!"
    her "Welcome to the mountain!"
    show dd 96
    mc "Ah, thanks! I can already feel the folksy..."with dis
    mc ". . ."
    play soundlow pop
    show dd96
    mc "Huh?"
    play sound metalhit
    scene dd 98b
    pause .6
    play sound2 metalhit
    show dd 98c
    pause .6
    show dd 98
    play sound3 metalhit
    play music2 dodd6 fadein 1
    mc "What?!" with hpunch
    stop musicb fadeout 7
    show dd 97
    mc "W-What is this?" with dis
    l "Huh? What do you mean?"
    mc "This house!"
    l "Uncle Hugo's house?"
    mc "I-It's a luxury mansion!"with hpunch
    mc "You're a Bardot too, or what?!"
    show dd 100
    l "*Chuckles* No!" with dis
    l "My uncle bought this house some years ago. He makes a very good living."
    show dd 99
    mc "You can say that again! Look at this house, goddamn!"
    show dd 100
    l "He even offered to help us pay the bills a few years ago when things got worse at the cafe, but my father refused."
    show dd 99
    mc "Ah, I know that feeling. I'm just as stubborn as him."
    show dd 101
    her "And that's a good quality to have, in my opinion."with dis12
    her "If you believe in something, don't let it go."
    her "Look at the cafe now, doing better than ever!"
    mc "Good advice!"
    play sound doorslam
    show dd 102
    unc "Victor, pedazo de cabrón!" (what_style='textsp') with hpunch
    show dd 103
    her "AH! Aquí está el pinche pendejo más feo que ha salido de México!" (what_style='textsp') with dis08
    her "Dame un abrazo, perro!" (what_style='textsp')
    play sound clothes2
    show dd 104
    unc "*Patting his back* JAJA! Te veo viejo y gordo, hermanito!" (what_style='textsp') with dis
    her "*Laughs* Chinga tu madre cabrón, al menos yo tengo pelo!" (what_style='textsp')
    show dd 105
    mc "What are they saying?" with dis
    l "Um..."
    l "They say they're so happy to see each other."
    l "...sort of."
    show dd 106
    her "Ah, yes, do you remember what I told you on the phone, Hugo?"with dis
    her "We should try to speak in English today, out of respect for [mc]."
    unc "Of course, of course! No problemo!"
    unc "I just got so excited when I saw my dear family after so many months, my bad."
    l "Hi, Uncle!"
    play sound2 clotheswhoosh
    show dd 107
    unc "BUT LOOK AT THIS BEAUTIFUL GIRL!" with hpunch
    unc "You've grown so much since the last time I saw you, Luna!"
    unc "I still can't believe how you can be so pretty after having a father so ugly."
    l "T-Thank you."
    unc "And look at this! You need to spend more time with us! You've lost your accent!"
    l "But I was born and raised in Kredon. I've never had an accent."
    unc "Oh, really?"
    unc "Well, you have to spend more time with us anyway!"
    show dd 108
    unc "And finally... ah, hello, young man." with dis12
    show dd 109
    mc "Hello, sir!"
    show dd 108
    unc "I guess you must be [mc], Luna's boyfriend."
    show dd 110
    l "W-What?"with hpunch
    l "What have you told them, Dad?!"
    show dd 111
    her "Oh, I'm sorry, sweetie."with dis04
    her "I just told them [mc] was your friend. And he's a boy, so... boy-friend, no? Isn't that how it works?"
    her "I'm sorry, my English is no bueno."
    show dd 112
    l "You've been living in the States for 30 years, your English is perfect!"
    show dd 111
    her "Sometimes I still have trouble with it..."
    show dd 109
    menu:
        with dis12
        "Play along [luna_pts]":
            mc "*Chuckles* That would be me, Luna's boy-friend." with dissolve
            mc "Nice to meet you."
            $ luna_points += 1
            play sound beat
            show screen heartbeat
            show dd 110
            l "[mc], don't play along!" with dis
            show dd 108
            unc "*Laughs* Nice to meet you, [mc]!"with dis08
            unc "I'm glad you came."
            show dd 109
        "Correct him":
            mc "*Chuckles* Yeah, I'm not her boyfriend. I'm just a friend from school." with dissolve
    mc "Luna and Mr. Hernandez invited me to lunch today, and I couldn't refuse."
    show dd 108
    unc "Well, we aren’t planning on anything too special, but I hope you enjoy your time here! I can guarantee you will have at least a pleasant morning and a good meal!"
    show dd 109
    mc "Oh, of that I am certain!"
    show dd 113
    unc "Please, come inside."with dis12
    unc "Feel free to explore the house and grab whatever you want from the kitchen. My home is your home."
    mc "Thank you very much!"
    show dd 114 with dis2
    mc "You have a lovely house, Mr. Hernandez." with dissolve
    unc "And you still haven't seen the views from the back balcony. They're spectacular!"
    play soundlow doorclose2
    show dd 115
    lg "*Going down the stairs* Victor? Is that you?" with dis15
    lg "Hugo? Is it him?"
    show dd 116
    her "MAMA!" with hpunch
    her "I missed you so much!"
    her "Give me a..."
    play soundlow woodhit
    play sound punch volume 0.8
    show dd 117
    lg "*Smacks him with her cane*" with vpunch
    her "Ouch."
    lg "You're late!"
    her "I-I know, sorry."
    her "I stopped to have a coffee because I was feeling sleepy."
    lg "You were driving sleepy? With Luna in the car?!"
    her "That's why I stopped!"
    lg "Mmmm... anyway, it's halfway through the morning already, we have to start cooking!"
    her "Yes, Mama!"
    unc "Hehehe..."
    play soundlow woodhit
    play sound punch volume 0.8
    show dd 118
    lg "*Smacks him with her cane* And you, what are you laughing at?!" with vpunch
    lg "Go prepare the pool for Luna and her friend! And clean your room!"
    unc "Y-Yes, Mama!"
    her "Hehehe..."
    show dd 120
    lg "Oh my sweet summer child..." with dis12
    lg "Each day you look more like an angel!"
    show dd 119
    l "Thanks, Grandma."
    show dd 120
    lg "You have your mother's flawless skin..."
    lg "Is your father feeding you well? You look so skinny!"
    show dd 119
    l "He is, yeah."
    show dd 120
    lg "Well... at least you'll eat properly during these two days."
    lg "I'll make sure to prepare enough food so you can take leftovers home."
    show dd 119
    l "Thank you!"
    show dd 121
    lg "Welcome, [mc]! It's nice to meet you." with dis15
    lg "My son has told me so many nice things about you."
    show dd 122
    mc "Thank you so much, Ms. Hernandez!"
    mc "I feel so honored to be invited. I appreciate it a lot."
    show dd 121
    lg "The pleasure is mine."
    lg "Luna never brought friends home to play with when she was little, so it was a pleasant surprise when Victor told me that she wanted to invite someone."
    show dd 122
    mc "I'm happy to hear that! Luna is a wonderful person."
    show dd 121
    lg "Oh, I know."
    lg "She'd give anything for others. Anything."
    lg "Her mother was like that too."
    lg "But anyways, go jump in the pool! We'll start cooking in the meantime."
    show dd 122
    mc "Are you sure you don't need us to help?"
    show dd 121
    lg "Absolutely! Go and have fun. We'll call you if we need anything."
    show dd 122
    mc "Alright then, thank you!"
    mct "Luna's family is so kind. I’m basically a stranger, and they’re inviting me with open arms."
    show dd 123
    her "[mc]! Luna went to wash her face and get changed." with dis15
    her "You can grab a swimsuit from the bathroom and use the pool too, if you want."
    show dd 124
    mc "That sounds wonderful! Thank you very much, Victor."with dis06
    show dd 125
    her "Actually, hang back a second... Now that we're alone, can I ask you something?" with dis08
    mc "Of course."
    show dd 126
    her "Um..." with dis08
    her "What are your intentions with my daughter?"
    show dd 127
    mc "Um..."
    mc "E-Excuse me?"
    show dd 126
    her "I mean, I know I like to joke around and everything, but... I just wanted to know how you feel about my daughter."
    her "She cares a lot about you, and I just want to make sure that her feelings are in the right place."
    show dd 127
    mc "Uh..."
    menu:
        with dis
        "She's just a friend":
            mc "I mean... she's a friend of mine."with dissolve
            mc "A very good friend!"
            mc "But... that's it. I don't see her as... anything else."
            her ". . ."
            show dd 126
            her "I see."
            her "That's perfectly fine. I'm sure you two can be great friends."
            her "Just... try not to hurt her, [mc]."
            her "I know she's not the most bubbly or affectionate girl on the outside, but I’m sure you’ve seen how big her heart is. She cares... almost too much."
            show dd 127
            mc "I'd never intentionally hurt her, Victor."
            show dd 126
            her "I know."
            show dd 123
            her "You're a good lad, [mc]. I like to think that I'm a good judge of character." with dis
            her "*Clears throat* But anyway, I don't want to keep you any longer. I have some tacos to cook!"
            her "Go have fun!"
            show dd 124
            mc "Will do! Thanks!"with dis06
        "[gr]I like her":
            $ victorcheck = True
            mc "I mean... well..." with dissolve
            mc "I like her. A lot."
            mc "Luna was basically the first new person I met in Kredon, and getting to know her has been one of the highlights of my stay here."
            mc "I don't know what will happen in the future, but... even if I'd like to be with her, I'd never try to force her into anything."
            mc "She’s been nothing but kind to me and my friends since I’ve met her."
            show dd 123
            her "I know." with dis
            her "*Chuckles* I won't get in the way, don't worry."
            her "All I want is for my daughter to be happy."
            show dd 126
            her "Growing up, Luna didn’t have the easiest childhood, and she went through a lot. Bullies, trauma... and especially her mom’s death."with dis
            her "It’s why I’m always trying to keep her laughing and keep a smile on her face, I don’t want to see my daughter that sad ever again."
            show dd 127
            mc "Yeah... Luna has told me about some of the stuff you’ve mentioned, I can only imagine what that must have been like for a young girl."
            mc "You’re a good father, Victor."
            show dd 123
            her "I've noticed her smiling a lot more often this past month. I have to believe it’s due to you."with dis
            her "Thanks for keeping a smile on my little girl’s face, [mc]."
            show dd 124
            mc "Thank you, Victor. That really means a lot to me."with dis06
            show dd 123
            her "Anyways, I don't want to keep you much longer. Thanks for having this talk with me."with dis06
            her "Just remember to follow your heart and listen to its guidance."
            show dd 124
            mc "Will do!"with dis06
            show dd 123
            her "Just one more thing..."with dis06
            stop music2
            play sound jumpscare
            play sound2 jumpscare2
            play music risinglong
            show dd128
            her "If you EVER hurt her, I will hunt you down across the outback till the day I die, [mc]."with vpunch
            mc "W-What?!"
            her "I know she's not the most bubbly or affectionate girl on the outside, but I’m sure you’ve seen how big her heart is."
            her "Don’t you DARE take advantage of her. I couldn't bear to see her suffer."
            mc "I-I'd never dare!"
            her "That girl is everything I have in this life. Everything."
            her "If you ever harm her in any way... I will kill you, [mc]."
            her "I swear to god."
            mc "I C-COULD NEVER HURT HER!"with hpunch
            mc "NEVER!"
            stop music fadeout 1
            play music2 dodd6 fadein 1
            scene dd 123
            her "I know!" with dis
            her "I know you're a good lad, [mc]. I'm a good judge of character."
            play sound swallow
            show dd 124
            mc "*Gulps* Thank you, sir."with dis08
            show dd 123
            her "Well, I have some tacos to cook!"with dis06
            her "Go have fun!"
            show dd 124
            mc "T-Thanks!"with dis06
    stop music2 fadeout 8
    play music birds volume 1.5
    scene black
    show screen afewminuteslater
    with dis22
    pause
    hide screen afewminuteslater
    show dd 129
    with dis22
    pause .1
    if victorcheck:
        mct "God, Mr. H sure knows how to be scary."with dis08
        mct "But I guess he's just a father who cares about his daughter."
        mct "I mean, I get it. In the little time I’ve known Luna, I’ve grown super fond of her."
        mct "It would kill me seeing her suffer, I can't even imagine how Victor would feel."
    else:
        mct "Hmm... did I say the right thing?"with dis08
        mct "Yeah, I think I did. I’ve only known Luna for less than two months, it’s way too early to think about relationship stuff."
        mct "Hopefully being honest will put Victor at ease a little bit."
        mct "I do agree with him though, I just want Luna to be happy."
        mct "Maybe she just has this effect on people..."
    mct "But anyway, I think I'm ready here!"
    mct "Let's go to the pool, she must be there already."
    show dd 130
    mc "Hmm... I'm gonna leave my boxers right here." with dis
    mc "I just need my swimsuit and a towel."
    show dd 131
    blank "{i}You catch a glimpse of yourself in the mirror."with dis08
    play music2 quirky4 fadein 5
    show dd 132
    mc "Hmm?" with dis12
    mct "Hey..."
    mct "Is it just my imagination..."
    mct "...or am I looking more buff lately?"
    mct "But that’s impossible. I’ve been so busy since coming to Kredon that I’m actually going to the gym less than I went back home."
    show dd 131
    mc ". . ."with dis
    show dd 133
    blank "{i}You flex your muscles and start posing."with dis12
    mct "I definitely look stronger, though."
    mct "Must be the lighting. Or maybe Nancy’s food."
    show dd 134
    mct "I mean, I've been either at school, or playing around in Eternum for the last few weeks."with dis12
    mct "Huh, imagine if all that exercise done in Eternum made you stronger in the real world too?"
    if nancypath:
        mct "It would be the end of all the gyms around the world. Kai would have to find a new way to flirt."
    else:
        mct "It would be the end of all the gyms around the world."
    show dd 133
    mct "Hmm..."with dis12
    mct "God, I feel so silly posing like this."
    show dd 131
    mct "Should I take a pic and ask someone? Both Annie and Chang saw me at the beach before we moved to Kredon."with dis12
    mct "They'll be able to tell if it’s all in my head."
    menu:
        with dis
        "Send a photo to Chang":
            mct "Chang will know." with dissolve
        "[gr]Send a photo to Annie":
            $ photoannie = True
            mct "Annie is probably the better option." with dissolve
    show dd 135
    mct "Hmm..." with dis12
    mct "Is this a good frame? I've never been much of a selfie-guy."
    play sound camera
    scene black
    pause .09
    scene dd 135
    blank "{i}You snap a few shots of yourself."
    mct "Yeah, this will do."
    if photoannie:
        mct "I'll send her the pic and check what she said later."
    else:
        mct "I'll send him the pic and check what he said later."
    show dd 129
    mct "Shit, I've gotta join Luna at the pool." with dis12
    mct "She must be thinking I'm doing something else here..."
    mct "Let's go!"
    play sound6 doorsliding
    stop music2 fadeout 4
    show dd 137 with dis25
    mct "Man, this house is amazing." with dis06
    mct "I've gotta buy one like this one day... if I ever have the money."
    mct "I’ve gotta find out what Luna’s uncle does for a living."
    play sound pool
    play sound2 drips volume 1.5
    show dd 138
    blank "{i}You hear some splashing in the water."with dis12
    stop music fadeout 7
    play music2b lunadoddins fadein 4
    show lunapool5 with dis2
    pause 11
    scene dd 139 with dis17
    pause .1
    $ unlock_look("luna", 6)
    mct "Oh my god..." with dis08
    mct "And just like that... all my cares go up in smoke."
    mct "Ms. Hernandez was right, she’s angelic."
    show dd 140
    mct "Damn..."with dis12
    mct "Look at that skin... it doesn't have a single defect."
    mct "She looks so..."
    show dd 141
    l "*Turning around* Hi [mc]!" with dis12
    mc "Oh, h-hi, Luna!"
    l "I was starting to think that something had happened to you. Toilet troubles?"
    mc "N-No! Not at all!"
    mc "Sorry, I got distracted looking at the views from upstairs."
    l "Yeah, they're great, aren't they?"
    mc "For sure..."
    play sound water
    show dd 142
    l "*Sitting down* We're lucky it's sunny today, we would have gotten cold after getting out of the water otherwise."with dis
    mc "Yep, it feels nice to be able to take advantage of the last warm days of the year."
    l "You have to try the water!"
    mc "On it! Make room!"
    play sound2 splash2 volume 1.5
    play sound3 water2
    play music underwater
    show dd 143
    blank "{i}You jump into the water with a clean jump." with dis
    mct "Man, Luna’s bikini doesn’t really leave much to the imagination..."
    mct "If she wasn't so introverted, she'd be so popular. She definitely has the looks for it."
    show dd 144 with dis
    mct "I mean, look at that."with dissolve
    if lunapoly:
        mct "I already saw her body in Warthogs, but... that wasn't really her. It wasn’t the same."
    mct "I guess she feels really comfortable around me."
    mct "Maybe we can–"
    play sound bubbles
    show dd 144 with vpunch
    mct "F-Fuck, I've gotta breathe!"with dis
    play sound3 gasp2
    play sound bubbles
    play sound2 pool
    stop music fadeout 1
    show dd 146
    mc "*Taking a gulp of air* AAah!" with dis12
    show dd 147
    l "Are you okay?"with dis03
    l "Don’t drown!"
    show dd 146
    mc "*Coughs* Y-Yeah! I overestimated my lung capacity."with dis03
    mc "The water's great, though! You were right."
    mc "Aren't you getting in again? I wouldn't want you to burn."
    show dd 147
    l "Actually, you can get sunburnt while you're swimming, too."with dis03
    l "I have to put sunscreen of the maxim–"
    play sound chickenwings
    play sound3 chicken
    show dd 148 with dis12
    pause
    mc "Um... "with dis08
    mc "Do you have a chicken on your head right now...? Or did I hit my skull against the bottom of the pool?"
    show dd 149
    l "Pancho!" with dis
    mc "Pancho?"
    play soundlow chickenwings fadein 1
    play sound chicken
    show dd 150 with dis15
    l "*Petting Pancho* He's my uncle's chicken." with dissolve
    l "He saved him from an illegal cockfight in Tijuana 4 years ago."
    show dd 151
    mc "No way!"
    mc "*Laughs* That is so awesome."
    mc "And he lives here now?"
    show dd 150
    l "Yeah! He’s always clucking around, right behind my uncle."
    l "I think he’s also become attached to me, though."
    l "I was surprised he remembered me when I visited last year."
    l "Chicken memory is better than what is believed."
    show dd 151
    mc "*Chuckles* That's pretty cool."
    mc "Now I want a chicken too!"
    play sound water
    show dd 152
    l "He probably wants to swim with us." with dis12
    l "He's not particularly fond of the water, but he loves his swan float."
    play sound2 water
    show dd 153 with Dissolve(1.4)
    pause .2
    mc "Is that it, Pancho?"with dissolve
    mc "You want to chill by the pool with us?"
    play sound chicken2
    show dd 153b with dis04
    pause .1
    show dd 153 with dissolve
    pause .2
    mc "I love this chicken."with dissolve
    play sound2 float1
    play sound3 water
    show dd 156
    mc "*Getting on the floatie* This is so nice, Luna."with dis15
    mc "It feels good to be able to relax for a bit."
    mc "Kinda hungry though, you think I should grab something to eat quickly?"
    play sound4 float1
    play sound5 water
    show dd 155
    l "*Getting on the floatie* Don’t even think about it!" with dis15
    l "If my grandma catches you snacking before their feast is prepped, she'll get mad."
    show dd 154
    mc "Oh shit, better not to piss her off, then!" with dis08
    mct "Man, it feels great to just sit back and relax with Luna."
    mct "I should probably take this chance to find out more about her. Especially after that chat with Mr. Hernandez..."
    mct "We haven’t ever really discussed her power, either. Not since the last time at her house, when it didn’t seem to work on me."
    $ qlpqn == 0
label lunapool:
    menu:
        with dis12
        "[gr]Do I look stronger to you?" if qlpq1:
            $ qlpq1 = False
            $ qlpqn += 1
            show dd 157
            mc "Hey, I wanted to ask you something..."with dis12
            mc "Do I seem... stronger to you?"
            mc "I mean, I was looking at myself in the mirror earlier when I was putting on my trunks, and I felt that I looked... different."
            mc "It’s almost like I’ve gained straight muscle, without gaining any fat, while I’ve been in Kredon!"
            mc "Which is weird, because I haven't worked out in a while, and between Nancy’s cooking and your cafe, I've been eating more than ever lately."
            show dd 158
            l "Well..." with dis
            l "It's... it's the first time I've seen you shirtless, so I can't really compare it to anything."
            show dd 159
            mct "Oh... that’s right, Luna wouldn’t have ever seen me shirtless before..."with dis04
            mct "She's not even in the same swimming class as me, Dalia, and Alex."
            mct "Oh shit, I hope she doesn’t think I’m just trying to flex how I look or something. I don’t want to come off as a cocky asshole."
            show dd 158
            l "But..." with dis04
            l "You have a very... g-good body."
            show dd 159
            mct "Guess not. Smooth move, [mc]..."with dis04
            show dd 158
            l "I wasn't expecting you to look so cut."with dis04
            l "I mean... you looked fit, but not like... this."
            l "I can tell you work out a lot."
            show dd 159
            mc "Oh, thank you, Luna!"with dis04
            mc "You look great in a bikini too..."
            show dd 158
            l "Oh please, I'm just skinny." with dis04
            show dd 159
            mc "Come off it! You look fantastic."with dis04
            mc "Do you do any sports?"
            show dd 158
            l "Not really."with dis04
            l "Sometimes I’ll ride my bike around town to pick up groceries or supplies, but that's it."
            show dd 159
            mc "Must be the taco diet, then."with dis04
            show dd 155
            l "*Chuckles* Must be that!" with dis12
            show dd 154
            jump lunapool
        "[gr]Can you speak Spanish?" if qlpq2:
            $ qlpqn += 1
            $ qlpq2 = False
            mc "You know... I'm curious, can you speak Spanish?" with dissolve
            play sound2 float1
            play sound3 water
            show dd 161
            l "Of course! What, did you think I made up what my father and uncle were saying earlier?"with dis15
            show dd 160
            mc "No, no!"with dis03
            mc "I mean, it could be that you understand it, but can’t speak it. Having grown up in Kredon and all that. A couple of my friends are like that."
            show dd 162
            l "Oh... I see."with dis03
            l "I know some people like that too, yeah."
            show dd 161
            l "But yes, I can. My father taught me when I was just a kid. He and my mother only spoke in English, though."with dis03
            l "I can speak both languages without an accent."
            show dd 160
            mc "That's awesome! I wish I had learnt a second language when I was younger."with dis03
            mc "Can you say something in Spanish?"
            show dd 162
            l "Um..."with dis03
            l "Gracias por venir, [mc]. Me gusta mucho pasar tiempo contigo."
            show dd 160
            mc "Hey! I heard my name there! What did you say?"with dis03
            show dd 161
            l "*Chuckles* I just said that I'm glad you came with us today."with dis03
            show dd 160
            mc "Ah, I'm glad to be here too, senorita!"with dis03
            play sound2 float1
            play sound3 water
            show dd 154
            mc "Your voice sounds really different when you speak in Spanish! Almost musical."with dis12
            mct "She sounded sexy as fuck... I'm not sure why. I need to get her to speak Spanish more often!"
            jump lunapool
        "[gr]Do you have any hobbies?" if qlpq3:
            $ qlpq3 = False
            $ qlpqn += 1
            mc "How do you like to spend your free time?" with dissolve
            mc "You know, besides Eternum. Any other hobbies?"
            play sound2 float1
            play sound3 water
            show dd 162
            l "Well, to be honest, when I'm not in school or helping my dad at Loco's, I spend most of my free time in Eternum."with dis15
            l "Although... sometimes I like to watch horror movies, or... shows and documentaries about serial killers."
            l "I... I know it's a little weird."
            show dd 160
            mc "It's not! I love those too."with dis03
            mc "As long as you don't watch them to get ideas..."
            show dd 161
            l "*Laughs* Of course not!"with dis03
            show dd 160
            mc "*Chuckles* No, but seriously, I know a lot of people who are “fascinated” by serial killers, me included."with dis03
            mc "It's like... it appeals to our basic instinct of survival."
            mc "Seeing what drives them to kill, what makes them “tick”. I think it's really interesting."
            show dd 161
            l "Exactly!"with dis03
            show dd 160
            mc "We should see one of these movies together some day. Have a little horror night!"with dis03
            show dd 161
            l "T-That would be great!"with dis03
            play sound2 float1
            play sound3 water
            show dd 154
            mc "I'll take a look at my collection..."with dis15
            mc "There HAS to be something good coming up on Netflix soon. All of their shows have just been okay since Ulysses bought them out."
            jump lunapool
        "[gr]Don't you want to take your gloves off? [mt](continues)" if qlpqn >= 2:
            mc "Can I ask a more personal question? And please, let me know if I'm overstepping." with dis06
            mc "Don't you want to take your gloves off? I noticed you were still wearing them earlier."
            mc "You have nothing to fear, there's only us in this pool."
            mc "Well... and Pancho."
            play sound water
            show dd 163
            l "Oh... it's just a force of habit." with dis12
            l "I'm not used to taking them off... like, ever."
            l "But I guess I could do it now. Like you said... it's just us."
            mc "Don't feel forced to! If you feel more comfortable this way then you–"
            l "No... it's okay. I want to do it."
            play sound2 float1
            play sound3 water
            show dd 164
            blank "{i}Luna gets out of the floatie and leaves her gloves poolside." with Dissolve(1.85)
            l ". . ."
            play sound water
            show dd 164b
            mc "*Approaching her* Better?" with dis
            show dd 166
            l "*Breathing rapidly* Y-Yeah." with dis03
            show dd 164b
            mct "Shit, she looks so anxious."with dis03
            mct "Maybe I shouldn't have said anything. It'd probably be better if she put them on again."
            show dd 165
            mc "S-Sorry, I shouldn't have said anything! You can–"with dis06
            show dd 166
            l "No, you're right."with dis06
            l "I need to get used to it."
            show dd 165
            mc "It's completely understandable to want them back on."with dis06
            show dd 166
            l "Can I..."with dis06
            l "Can I touch you?"
            show dd 165
            mc "Touch me...?"with dis06
            show dd 166
            l "Yeah, I mean..."with dis06
            l "Like the last time I took my gloves off."
            show dd 165
            mc "Oh... of course!"with dis06
            mct "How could I refuse when she says it with that sweet voice..."
            play sound water
            show dd 168 with dis14
            pause
            play soundlow impactwet
            show dd 169 with Dissolve(.05)
            show dd 168 with Dissolve(.05)
            pause
            play soundlow impactwet
            show dd 169 with Dissolve(.25)
            pause .1
            show dd 168 with Dissolve(.3)
            pause .12
            l ". . ." with dis
            play sound2 water
            show dd 170
            blank "{i}Small goosebumps appear all over Luna’s body as she slowly lays both of her hands on your chest." with dis15
            $ luna_points += 1
            play sound5 beat
            show screen heartbeat
            show dd 171
            l "I-I still can't believe this." with dissolve
            l "I'm touching someone with my bare hands and not having any visions!"
            l "No visions at all!"
            show dd 170
            mc "That's... still a good thing, right...?"with dis04
            show dd 171
            l "Of course!"with dis04
            l "It's amazing!"
            show dd 170
            mc "Any idea yet on why I'm the only person on whom your power doesn't work?"with dis04
            show dd 171
            l "I don't know..."with dis04
            show dd 170
            mct "It's so weird. Maybe she only has visions with {i}some{/i} people?"with dis04
            mct "I feel like we should look into it and experiment with her power a little bit. But I don't want to force her into anything."
            mct "As much as I want to help her, we should move at her pace."
            show dd 171
            l "You're... so warm."with dis04
            mc "Hmm?"
            l "You..."
            show dd 172
            blank "{i}She stops mid-sentence and stares straight into your eyes." with dis17
            l "You..."
            l ". . ."
            mct "This moment..."
            mct "It's the same as when she touched my face for the first time at her house."
            l ". . ."
            mct "All I want to do is hold her against me and crash my lips into her mouth..."
            mct "I can't waste this chance. It's now or never."
            menu:
                with dis
                "[gr]Kiss her":
                    $ trykissluna = True
                    play sound water3
                    play sound2 water2
                    play sound3 whoosh6
                    show dd173
                    blank "{i}Before you make a move, Luna quickly slips out of reach and goes back to the floatie." with hpunch
                    mct "W-Wha..."
                "Back off":
                    mc "W-Well, I guess we can go back to the floaties now."with dissolve
                    mc "Much better without the gloves, right?"
                    l "W-What? Ah, yeah, sure..."
            play sound2 float1
            play sound3 water
            scene dd 158
            l "*Clears throat* T-Thank you, [mc], I feel much better now."with dis15
            show dd 159
            mc "Um... I-I'm glad!" with dis04
            mc "You can touch me whenever you want!"
            mct "God, that sounded so bad."
            show dd 158
            l "T-Thanks. Will do."with dis04
            show dd 159
            mct "Change the subject, [mc], this is such a nice moment, don't make it awkward..."with dis04
            mc "Uh... you know what we should do now?!"
            mc "Just take a beat and listen to the sounds of the valley for a minute!"
            play sound4 float1
            play sound5 water
            show dd 161
            l "Ah! That sounds great, actually."with dis12
            l "I like the sound of the mountain."
            show dd 160
            mc "Right?"with dis03
            play sound6 float1
            play sound water
            jump poslunapool
        "Stop asking":
            mc "You know, I think I'm gonna follow Pancho's steps."with dissolve
            mc "Just take a beat and listen to the sounds of the valley."
            show dd 155
            l "Sure! That sounds great, actually."with dis08
            l "I like the silence."
            play sound2 float1
            play sound3 water
            jump poslunapool
label poslunapool:
    show dd 174b
    mc "*Lying down* Ahh..."with dis15
    mc "This is the life."
    mc "Can you imagine how it would feel to not have any obligations?"
    l "Like... not having to go to school?"
    mc "Yeah! No school, no job, no worrying about the future, no concerns at all... just a pool, your pet chicken, and the morning sunlight."
    l "*Chuckles* It doesn't sound half bad."
    play sound doorsliding
    pause .8
    lg "Luna!" with dissolve
    lg "Come on, get out of the pool!"
    play sound2 float1
    play sound3 water
    show dd 174
    l "Already? We just got into the water." with dis12
    l "Is the food already done?"
    lg "Not yet, but your father can handle the rest."
    lg "It's time to dress up!"
    l "This year too?"
    lg "Of course! I need my annual picture of my granddaughter."
    lg "Hurry up, I'll be waiting in the dining room."
    l "Okay, okay..."
    play sound2 float1
    play sound3 water
    show dd 160
    mc "Dress up?" with dis12
    show dd 162
    l "Yeah, each year, my grandma puts me in a dress and covers me in Day of the Dead makeup." with dis04
    l "I know it makes her happy, so I don't really mind."
    show dd 160
    mc "Oh boy! I've gotta see that!"with dis04
    mc "You better hurry up! She looked pretty formidable with that cane of hers!"
    show dd 161
    l "*Giggles* Okay, but promise not to laugh at me."with dis04
    show dd 160
    mc "Never!"with dis04
    play sound doorsliding
    stop music2b fadeout 8
    play music birds fadein 6
    show dd 175 with dis22
    lg "Alright! Are you ready?" with dis06
    lg "Let's go upstairs, Luna."
    show dd 176
    l "Is it the same dress as last year?"
    show dd 175
    lg "No, it's not!"
    lg "Actually, I made this one myself. I've been sewing for 4 weeks."
    lg "I hope you like it."
    show dd 176
    l "I'm sure I'll love it, yaya."
    l "Thank you!"
    show dd 175
    lg "You’re such a sweetheart, mija."
    lg "Let's do your makeup first, so you can get dressed by yourself while I do [mc]'s makeup."
    show dd 178
    mc "What? Me too? Makeup?"with dis
    show dd 177
    lg "Day of the Dead makeup!"
    lg "It's a tradi–"
    play sound6 fallkitchen fadein 0.2
    play music2 dodd6 fadein 5
    stop music fadeout 6
    show dd 179 with hpunch
    her "BE CAREFUL!" with dissolve
    unc "OH SHIT, the chilaquiles!" with hpunch
    her "AARGH! They're all over the floor!" with hpunch
    unc "Okay, okay, don't worry, we can replace them with something else..."
    unc "Ah, wait, I think I have hamburger buns!"
    her "Oh! Great idea, should we get some fries from McDonald’s too?"
    unc "Taste this beef before you talk, trust me."
    unc "This cow was raised in better living conditions than any of us. I have steak too, if you prefer."
    her "I'll see what I can do..."
    her "Hey, where's the blue cheese? It was here just a second ago."
    play sound2 chicken
    play sound3 chickenwings fadein 1
    show panchov with Dissolve(.3)
    pause 1.5
    scene dd 179
    her "HEY!" with dis04
    her "THAT FUCKING CHICKEN TOOK MY CHEESE!"with hpunch
    play sound5 slam
    her "I'M GONNA KILL HIM!"with hpunch
    unc "*Gasps* Take that back!"
    mc "Um..."
    show dd 178
    mc "Are they gonna be okay...?"with dis
    show dd 177
    lg "Of course! Don't worry about those two butterfingers."
    lg "Let's focus on our thing."
    lg "I left some clothes in the guest bedroom."
    lg "You can start getting changed, if you want."
    show dd 178
    mc "*Laughs* Alright then!"
    show dd 176
    l "I'm sorry you got dragged into this, [mc]."
    show dd 178
    mc "No problem! It actually sounds pretty fun."
    mc "See you both in a minute!"
    stop music2 fadeout 7
    play music birds fadein 5
    play sound2 dooropen1
    show dd 181 with dis22
    play sound4 doorclose
    mct "Wow, another huge room." with dissolve
    mct "A house with all these bells and whistles must cost a fortune."
    mct "Hmm... is that what I'm supposed to wear?"
    play sound clothes
    show dd 182 with dis17
    mct "Huh, country style. I like it." with dissolve
    mct "These clothes feel like pillows. How are they so comfortable?"
    play sound5 knock2
    lg "[mc]? Are you ready?"
    mc "Yes, ma'am!"
    play sound3 dooropen1
    show dd 183 with dis12
    lg "*Gasps* Dios mio..."with dis06
    lg "You remind me so much of my husband..."
    lg "You look like a true Hernandez now!"
    mc "Thanks!"
    show dd 184
    lg "Okay, time to paint your face!"with dis
    lg "*Plugging in the record player* Let me put something appropriate on..."
    stop music fadeout 5
    play sound vinyl
    play musicb llorona fadein 5
    show dd 185 with dis17
    lg "I'm gonna need you to close your eyes and stay quiet." with dis06
    lg "If this paint gets in your eye, you're gonna go blind forever."
    lg "Do you understand?"
    play sound swallow
    mc "*Gulps* Mm-hm."
    show lgpaint with dis15
    blank "{i}Luna's grandma starts painting your face at a surprisingly rapid pace." with dis06
    mc "This song sounds sad."
    lg "DON'T TALK!"
    lg "But yes, it's supposed to be."
    lg "The original song tells the story of the ghost of a woman who roams rivers and towns wailing for her children... whom she drowned."
    mc "Damn... that's terrible."
    lg "[mc]!"
    mc "Mm-hmm!"
    lg "Okay, just a bit more green here..."
    lg "Outline on the edges of this..."
    lg "Last details, and..."
    play sound clothes3
    scene dd 188
    lg "DONE!" with dis12
    lg "You're perfect!"
    show dd 189
    mc "Can I go look at myself in the mirror?"with dis08
    lg "THERE'S NO TIME!"
    lg "LET'S GO TAKE THE PICTURE!"
    play sound whoosh6
    show dd190
    pause
    play sound2 whoosh6
    scene dd191
    lg "YOU HERE!"
    play sound3 whoosh6
    scene dd192
    pause .3
    play sound4 whoosh6
    scene dd193
    $ unlock_look("luna", 7)
    lg "And you over here!"
    scene dd 194
    lg "AAAH, YES!" with dis12
    lg "You look so beautiful!"
    show dd 195
    lg "Hugo! Bring the camera!" with dis15
    lg "Take a few photos of them for the album while I make my ofrenda!"
    show dd 196
    mc "Hmm?" with dis08
    l ". . ."
    show dd 197
    mc "Oh... DAMN!" with dis
    mc "You look stunning, Luna!"
    show dd 199
    l "Thank you!" with dis12
    l "You look great too."
    show dd 198
    mc "Your grandma is an artist!"
    show dd 200
    her "*Sobbing* Oh god, is that my daughter?" with dis
    unc "You look so beautiful, Lunita! "
    l "Thank you, Uncle!"
    her "Why do they grow so fast, Hugo?"
    her "Why can't they stay small forever?"
    unc "*Laughs* Enjoy it while you can, Victor. My daughters left the nest before I'd even realized!"
    show dd 201
    her "Alright then, let's take that picture!" with dis12
    her "Pose for the camera!"
    play sound camera2 volume 1.3
    show dd 202 with Dissolve(.05)
    show dd 201 with Dissolve(.1)
    pause .2
    her "Perfecto!"with dis06
    her "Mama will love it."
    her "A last one?"
    menu:
        with dis
        "Stay in the same position":
            play sound camera2 volume 1.3
            show dd 202 with Dissolve(.05)
            show dd 201 with Dissolve(.1)
            pause .2
            her "Sweet!"with dis06
        "Hold Luna by the waist [luna_pts]":
            $ lunawaist = True
            play sound5 clothes2
            show dd 203
            mc "Better like this?"with dis12
            $ luna_points += 1
            play sound2 beat
            show screen heartbeat
            her "Ah, yes, now we're talking!"
            her "This is a photo to remember!"
            play sound camera2 volume 1.3
            show dd 204 with Dissolve(.05)
            show dd 203 with Dissolve(.1)
            pause .2
            her "Sweet!"with dis06
    show dd 205
    her "Okay, okay, okay!" with dis12
    her "It's almost time to eat!"
    her "Do you wanna join my mother at the ofrenda while we set the table, [mc]? I'm sure she'd appreciate it."
    show dd 198
    mc "The ofrenda?" with dis08
    show dd 199
    l "It's an improvised altar we place at home during the Day of the Dead celebration to remember those who passed away."
    l "My grandma takes it very seriously."
    show dd 198
    mc "Oh... I'd rather not disturb her, then."
    show dd 199
    l "On the contrary! Like my father said, I'm sure she'd appreciate it if you went."
    l "I'll go myself after you and my father leave later today."
    show dd 198
    menu:
        with dis
        "[gr]Join the ofrenda":
            mc "Well, in that case... I'd be honored to go." with dissolve
            show dd 199
            l "We'll start setting the table. I'll call you when it's ready."
            show dd 198
            mc "Sounds good!"
            show dd 199b
            unc "Luna, come here, please!" with dis08
            unc "I want a photo of Pancho with you!"
            play sound doorold
            show dd 206 with dis22
            mct "Hmm, looks like she's praying." with dissolve
            play sound footsteps
            show dd 207 with dis15
            mct "Oh, could that be... Luna's mom?"with dis08
            show dd 209
            lg "Thank you for coming, sweetheart."with dis
            show dd 208
            mc "I'm honored, Ms. Hernandez. Thank you for letting me be here."
            show dd 207
            mc "I was wondering..." with dis
            mc "Is this woman..."
            lg "Yes. That's Olivia, Luna's mother."
            mc "I see..."
            mc "She looks a lot like her."
            lg "And not only physically. She was just as sweet."
            lg "The best daughter-in-law a mother could have ever asked for."
            lg "Behind his cheerful attitude, I know Victor still hasn't fully gotten over her death, even after all these years."
            mc "I'm sure she'd be really proud of both of them."
            lg ". . ."
            lg "I wish my sister was still alive. She'd be able to talk to her."
            show dd 208
            mc "Talk to her...?" with dis
            lg ". . ."
            show dd 209
            lg "My family has always had a certain connection to... the metaphysical realms."
            lg "My sister was able to communicate with the dead."
            show dd 208
            mc "She could speak with the dead...?"
            show dd 209
            lg "Don't worry, I'm not asking you to believe me."
            lg "No one ever did anyway."
            lg "Most people always thought she was just a liar, but I always believed her and her visions."
            lg "She was no liar."
            lg "She could see them, [mc]."
            lg "Happy. Sad. Isolated. Together. She used to say that each of the dead had their own unique... “heaven”."
            show dd 208
            mct "Hmm..."
            mct "Could this be related to Luna's powers...?"
            mct "Maybe..."
            show dd 210
            lg "But anyway, forgive me."with dis
            lg "And forget what I said! Today is a day to celebrate, not to mourn!"
            show dd 211
            mc "O-Of course!"
            show dd 207
            lg "Take care, Olivia." with dis12
            lg "You still live in the hearts of the ones you left behind."
            menu:
                with dis
                "[gr]Say something":
                    $ grandmacheck = True
                    mc "I never met you, but if Luna is a testament to the kind of person you were, I can safely say you were a wonderful mother." with dissolve
                    mc "I promise to look out for her, just like the rest of her friends and family."
                    mc "Rest in peace, Olivia."
                    lg "That was very nice, [mc]. Thank you."
                "Remain silent":
                    mc ". . ." with dissolve
            play sound knock2 volume 1.8
            stop musicb fadeout 7
            play music birds fadein 2
            show dd 212
            l "Sorry to disturb you." with dis12
            l "The food is ready!"
            show dd 213
            lg "Don't worry sweetie, we were already done here."with dissolve
            lg "Let's go to eat!"
            mc "Yes! I'm starving!"
            mc "I don't know what it is, but it smells fantastic."
            stop music fadeout 9
            play music2 dodd6 fadein 5
        "Pass{#0.5,ofrenda}":
            mc "Still, this sounds like a very personal thing." with dissolve
            mc "I think I should stay here, actually."
            show dd 199
            l "O-oh. If that’s what you prefer."
            show dd 205
            her "Please help me set the table, then." with dis
            her "You can get the wine from the cellar."
            mc "On it!"
            stop musicb fadeout 5
            show black
            show screen afewminuteslater
            with dis2
            pause
            play music2 dodd6 fadein 5
            hide screen afewminuteslater
    scene dd 214
    with dis22
    mc "Damn, Victor! This is quite impressive!" with dis08
    her "Well, we were forced to change the original plan because someone forgot to buy the ingredients I asked him to... but it'll do!"
    unc "Are you blaming me?!"
    mc "There's more than enough! And everything looks delicious."
    play sound chair2
    play soundlow chairmove
    show dd 215
    mc "*Sitting down* Are these your famous tacos, Victor?" with dis12
    show dd 216
    her "Correcto!"
    her "Eat as many as you want, [mc]!"
    show dd 215
    mc "Thanks, sir!"
    show dd 218
    lg "Make sure to fill your plate too, Luna!"
    lg "You've gotta eat more!"
    show dd 219
    l "Yes, yaya..."
    show dd 215
    mc "Oh, and by the way, thank you so much for inviting me to your house, Hugo." with dis08
    show dd 217
    unc "Ah, don't even mention it, [mc]!"
    unc "It's my pleasure. I like having guests."
    unc "I wish my daughters would come visit me more often."
    show dd 215
    mc "I've gotta ask, though, what do you do for a living?"
    mc "A house this fancy MUST have cost a fortune."
    show dd 217
    unc "Oh, that's actually a good question."
    unc "You see, I'm running a cartel and a human trafficking ring."
    show dd 215
    mc "*Laughs* Okay, I see that the joking around and sarcasm are genetic!"
    $ renpy.music.set_volume(0.0, delay=30.0, channel='music2')
    play music risinglong fadein 30
    show dd 223
    mc "*Laughs* Hahaha!"
    show dd 215
    mc "*Laughs* Haha!"
    show dd 223
    mc "Haha..."
    show dd 215
    mc "Ha..."
    show dd 220
    mc "Ha...." with dis08
    show dd 221
    mc "Ha..."
    show dd 220
    mc "W-Why is no one laughing...?"
    show dd 222
    mc ". . ."with dis08
    show dd223 with dis
    pause
    mc "H-Hugo... what's your job?" with dissolve
    unc ". . ."
    mc ". . ."
    mc "U-Um... Hugo?"
    mc "V-Victor?"
    mc "Luna?!"
    unc ". . ."
    play sound slam
    stop music
    $ renpy.music.set_volume(0.5, channel='music2')
    scene dd 224
    unc "HAHAHA!" with hpunch
    unc "I'm sorry, I'm sorry! I swear I tried, but I couldn't stop myself from laughing!"
    show dd 215
    mc "*Laughs* I knew it! This was just another one of your jokes, eh, Victor?"
    show dd 216
    her "*Chuckles* Damn, you’ve caught onto me so quickly. You’re right though! I couldn't help it."
    show dd 215
    mc "Well, I'm glad that Hugo isn't involved in human trafficking."
    show dd 224
    unc "*Laughs effusively* God, no! I don't have the guts!"
    unc "I wouldn't hurt a fly, don't worry, [mc]!"
    show dd 225
    unc "*Stops laughing* I do run a cartel, though." with dis08
    show dd 226
    mc "You really had me goin–"
    show dd 227
    mc "Wait, what?" with dis04
    show dd 228
    her "Oh, mama, can you pass me that picture from the shelf?"
    mc "W-We're still joking, right?"
    lg "The one with Luna when she was little?"
    her "Yes!"
    show dd 229
    l "Dad!"
    her "Come on, sweetie! You were adorable!"
    show dd 230
    her "Here it is!" with dis
    her "Do you wanna see it, [mc]?"
    mc "Of course!"
    play sound grab2
    show dd 231 with dis14
    mc "Awwww..."with dissolve
    mc "That IS adorable!"
    mct "Luna's already wearing her gloves, so I guess this pic was taken after her mother died."
    mc "How old were you here?"
    her "She was only 5 years old. I had just picked her up from kindergarten."
    l "I was 11!"
    her "Really? Damn, it feels like ages ago."
    her "*Sobbing* My little girl's growing up, right before my eyes..."
    l "*Whispering* Dad, please, you’re embarrassing me!"
    mc "*Laughs* I love this photo."
    show dd 219
    l "Can we start eating already, please?" with dis08
    show dd 226
    mc "Hell yes! I'm so hungry!"
    show dd 216
    her "Try one of my tacos, [mc]. It's my special, secret recipe!"
    if reallyspicy:
        her "Like we discussed the other day, they're EXTRA spicy!"
        show dd 219
        l "Be careful, [mc]. When my dad says extra spicy, he means it. The sauce is {i}really{/i} spicy."
        show dd 232
        mc "I appreciate the concern, but seriously, there's no need to worry."
        mc "I can withstand spicy food."
        show dd 233
        mc "*Grabbing a taco* I don't want to brag, but I used to add Tabasco to my spaghetti when I started cooking my own meals." with dis
        mc "I think I've almost become immune to it!"
        show dd 234
        mc "Aaaah..." with dis08
        play sound chew
        play sound2 bite
        show dd 235
        mc "Mmmm..." with dis
        mc "MMMMm!"
        mc "Mthis–"
        stop sound
        play sound2 impact4
        play music mariachi
        stop music2 fadeout 4
        show dd235
        pause 0.08
        scene dd 237
        pause .02
        show dd 236
        pause .02
        show dd 237
        pause .02
        show dd 236
        show spicy1
        show spicy1b
        pause 6
        show spicy1bb
        pause 4.5
        play music2 dodd6
        stop music
        scene dd 238
        her "Is anything wrong, [mc]?"
        her "You don't like my tacos?"
        play sound chairmove volume 1.4
        show dd 239
        mc "*Hyperventilating* (JESUS FUCKING CHRIST.)" with dis08
        mct "Is my mouth on fucking FIRE?!"
        show dd 238
        her "Are you okay?"
        her "You started sweating quite a bit."
        show dd 218
        lg "[mc], your paint! I'll have to redo it!"
        show dd 239
        mc "H-Huh?"
        play sound chair2
        show dd 240
        mc "O-Oh? Haha!" with dis
        mc "N-No, no! They're p-perfect!"
        mc "Absolutely delicious!"
        show dd 216
        her "Ah, I'm glad! I knew you'd appreciate them!"
        her "You’re sure they’re not a little too spicy for you?"
        show dd 240
        mc "T-Too s-s-spicy? N-Not at all! This is just how my body typically reacts to ethnic food."
        mc "W-What's in them, o-out of curiosity?"
        show dd 217
        unc "Ground beef, tomato, cheese, avocado, fresh garnishes, and Carolina Reaper, the hottest chili pepper in the world!"
        show dd 240
        mc "Ah, yeah. I-It adds the perfect touch, I can t-taste it."
        show dd 241
        mc "C-Can I get a drink?"with dis
        her "Of course! A michelada?"
        her "It's a Mexican beer with chili-based spices, served in a salt-rimmed glass!"
        mc "C-Chili...? S-sounds like exactly w-what I need, s-sir."
        l "*Giggles*"
    else:
        her "Like we discussed the other day, these shouldn’t be too spicy."
        show dd 233
        mc "*Grabbing a taco* That was probably a good call." with dis08
        mc "I don’t have a very high spice tolerance."
        show dd 234
        mc "Aaaah..." with dis
        play sound chew
        play sound2 bite
        show dd 235
        mc "Mmmm... mmmm!" with dis
        mc "Mmm, this is mdelicious!"
        show dd 216
        her "Really? Do you like them?"
        show dd 241b
        mc "They're so tasty!"
        mc "But... are these supposed to be “slightly” spicy?! Phew, thank god I didn't ask you to prepare the extra spicy ones!"
        her "*Laughs* I'd have paid to see your face!"
        mc "Oh, can I grab one of those chicken wings?"
        her "Of course!"
    stop music2 fadeout 5
    show black with dis25
    pause .1
    show screen afewhourslater with dis
    pause
    play music birds fadein 2
    scene dd 242
    hide screen afewhourslater
    with dis22
    her "AAAaaghh..." with dissolve
    her "I can't eat another bite! I'm about to explode."
    play sound chair3
    show dd 243
    mc "Yeah, I've never been so full."with dis
    mc "Everything was just too good!"
    mc "(Thank god they had milk to counteract the spice...)"
    play sound chairmove
    show dd 244
    l "*Standing up* I'm going to clean my face and do some sunbathing on the upstairs terrace before the sun goes down."with dis12
    her "Of course honey, just make sure to put on some sunscreen."
    play sound2 chair3
    show dd 246
    mc "*Standing up* That sounds good!" with dis
    mc "Do I have enough time to join her for a bit?"
    show dd 245
    her "Sure, no problem. We'll leave for Kredon in 20 or 30 minutes."
    her "I'll do the dishes in the meantime."
    show dd 246
    mc "Sweet! Thank you, Victor."
    show dd 247 with dis22
    play sound toilet
    mct "It's too bad I can't spend some more time here with Luna." with dis08
    mct "I feel at home with their family."
    mct "But hey, better make the most of it while I’m here!"
    play sound5 dooropen1
    show dm 21 with dis17
    mc "*Entering the main bedroom* Did I hear Pancho running around up here?" with dis06
    mc "Can he climb stairs?"
    l "Yeah! Can you close the door?"
    l "My uncle gets nervous when he can't find Pancho."
    play sound doorclose
    show dm 22
    mc "*Laughs* This damn chicken is smarter than any of us." with dis14
    show dm 23
    mc "I wouldn't be surprised if he knew how to open doors too."with dis15
    mc "That's..."
    show dm 24
    mc "Oh boy..."
    play music2 lunadodd fadein 6
    stop music fadeout 9
    show dm 25 with dis25
    pause
    mct "She took her dress off and put her bikini back on..." with dis
    show dm 26
    mct "I thought I wouldn't be able to see her wearing it after we changed clothes." with dis
    mct "The God of Tits & Ass smiles on me again!"
    mc "You changed fast!"
    show dm 27
    l "Yeah, the dress was easy to take off."with dissolve
    l "And the paint fades with a little water."
    play sound clothes4
    show dm 29
    mc "Yep, I noticed that." with dis12
    mc "I almost felt bad while washing my face."
    show dm 28
    l "Don't worry! We'll always have the photos we took."
    l "And we can come back another day. Yaya loves putting make-up on people, and my uncle loves having visitors."
    show dm 31
    l "I mean... if you ever want to come back, of course."with dis04
    l "There's definitely enough rooms for an overnight stay. Like a big sleepover!"
    l "And I'm sure my family wouldn't mind. They really liked you."
    show dm 29
    mc "The feeling is mutual!"with dis04
    mc "And I'd love to come back, of course. Thanks, Luna."
    show dm 32
    mc "We could even go hiking!"with dis12
    mc "These mountains are beautiful."
    l "Right?"
    l "There's a nearby pond with a small grotto where you can swim too."
    mc "Oh man, I have to see that! Sign me up."
    mc "I could spend hours just staring at these views. I bet these woods hide a lot of secrets..."
    l "Yeah, this terrace is my uncle's favorite spot in the house, actually."
    mc "Oh, I can see why."
    show dm 29
    mc "I assume that’s why he installed this massage table here?"with dis
    show dm 28
    l "Yeah, he told us he even hired a couple of masseuses to visit from time to time."
    show dm 29
    mc "Ah, living the life!"
    show dm 28
    l "It's very comfortable and it’s water-resistant, so I usually sunbathe here after a quick swim."
    show dm 29
    mc "I see..."
    menu:
        with dis
        "[gr]Offer to give her a massage":
            mc "You know... we have a few minutes left, and I’m a pretty talented masseur myself..."with dis06
            mc "It'd be a shame to waste this table."
        "Leave":
            mct "Hmmm... nah, there's not enough time. It would be rude of me to keep Mr. Hernandez waiting."with dissolve
            mct "And... it might be a bit too much, honestly."
            mct "I don’t want to risk my friendship with Luna by offering something weird like that."
            mc "Anyway Luna, it was great hanging out with you today. Thanks so much for inviting me! You’re a really great friend – sorry I’ve gotta leave so early."
            show dm 28
            l "Don't be! Today was awesome. You really made it a great day."
            l "I know it probably wasn't worth it to come all the way up here just to spend a few hours swimming and tasting my dad's tacos, but... I really appreciate you visiting, [mc]."
            show dm 29
            mc "It was DEFINITELY worth it!"
            mc "I had so much fun."
            mc "I'll be the one inviting you somewhere next time."
            show dm 28
            l "Okay!"
            l "That sounds good."
            show dm 29
            mc "Will you be back in Kredon by Monday?"
            show dm 28
            l "Of course!"
            l "And good luck on your mission with Nancy tomorrow... whatever that is!"
            show dm 29
            mc "Thanks! I'll make sure to tell you all about it."
            mc "Goodbye, Luna."
            show dm 28
            l "Bye!"
            $ lunaunclehouse = True
            $ lunapath = False
            $ lunau = False
            stop music2 fadeout 5
            play music birds fadein 1
            jump posmassageluna
    show dm 31
    l "A massage...?" with dis06
    l "Like..."
    l "You're offering to give me one?"
    show dm 30
    mc "Yep!"
    if daliapath:
        mc "Do you remember Dalia's back injury?"
        mc "It was me who miraculously healed her in less than a week! Right in time for her competition."
        mc "And it was all thanks to my special massage technique, of course."
        show dm 28
        l "*Giggles* I remember her mentioning that, actually." with dis06
    else:
        mc "I am quite the massaging miracle worker!"
        show dm 28
        l "*Giggles* It definitely sounds promising."with dis06
    show dm 29
    mc "So... what do you say? Do you want one?"
    l "Hmm..."
    play sound clothes4
    show dm 33 with dis14
    l "*Lying down* O-Okay." with dis06
    l "If you really don't mind... I won't say no. You’ve convinced me!"
    show dm 34
    mc "Sweet! No one can refuse one of my rubdowns!"
    show dm 33
    l "Well, I don't know many people who would refuse a free massage."
    l "Unless the person offering it had some sort of ulterior motive."
    show dm 34
    mc "*Chuckles* There's no hidden agenda, I promise."
    mc "I can use some sunscreen oil too, if you want."
    show dm 33
    l "Yeah, sure. I could use some of it on my lower back."
    l "There's a bottle under the table."
    show dm 34
    mc "Excellent then!"
    mc "Thank you for signing up for our premier massage package here at [lastname] Massage Parlor."
    mc "Are you ready, ma'am?"
    play sound clothes4
    show dm 35
    l "*Giggles* Sure." with dis14
    mct "Sweet Lord have mercy..."
    mct "This view is almost too much..."
    mc "*Taking a deep breath* (But luckily, you're not an animal, [mc]. Inhale and exhale, now...)"
    mct "Though, if Luna wanted me to be an animal..."
    l "[mc]?"
    show dm 36
    mc "*Clears throat* Y-Yeah!" with dis14
    mc "I was saying..."
    mc "Ah, yeah! Please, relax and prepare to enjoy the experience, ma'am."
    l "*Giggles* Mm-hm."
    show dm 37 with dis2
    pause .1
    bla "You gently put your hands on Luna's lower back." with dis12
    bla "Her skin immediately tenses, and her breathing begins to pick up."
    show dm 38
    mc "Is everything okay?" with dis
    show dm 39
    l "Y-Yes."
    l "It's just that... your hands are cold."
    show dm 38
    mc "Oops, my bad."
    mc "On the other hand, your skin feels really warm after being exposed to the sun for such a long time."
    mc "Sorry about that!"
    show dm 39
    l "No problem..."
    scene lunaf1 with dis2
    bla "You start massaging Luna's lower back at a steady pace, squeezing your fingers in a firm but tender manner." with dis12
    mc "Your lower back muscles are really tense, Luna."
    mc "You're full of knots."
    l "Am I?"
    mc "Yeah, totally."
    l "And what's the solution?"
    mc "Well, my years of massaging experience have prepared me for this. It'll have to be a lengthy treatment."
    mc "You'll need lots of relaxing, periodic caresses from a trustworthy masseur."
    l "*Giggles* That would be you?"
    mc "You happen to be in luck, ma'am."
    l "*Giggles* I think that’s a treatment plan I can follow..."
    bla "Little by little, Luna's muscles begin to relax, as the temperatures of your hands and her body even out."
    mc "Starting to feel better?"
    scene dm 39
    l "Yeah..." with dis12
    l "It feels... {w}great."
    mc "I'm glad."
    scene lunaf1 with dis14
    mc "Do you like to sunbathe when you have the opportunity?"with dis06
    l "I do..."
    l "But my skin is so pale that, even if I manage not to get sunburned, I end up with ridiculous tan lines."
    l "So I usually avoid it."
    mc "I see."
    mc "You can remove the top of your bikini, if you want."
    scene dm 39
    l "Hmm? What...?"with dis12
    mc "Uh, I mean..."
    mct "Did that sound too forward?"
    mc "You know, if you don't want tan lines. I-I’ve heard that’s what Penny does to avoid tan lines for modeling shoots!"
    mc "I know that most women try to avoid them."
    l "Oh..."
    l "Sure... good idea. I’ll have to thank Penny next time I see her."
    play sound clothes4
    play sound2 clothes3
    show dm 40
    bla "Luna takes off her bikini top and drops it next to the table." with dis15
    l ". . ."
    mct "Damn, I didn’t think that’d work. But I'm glad it did..."
    play sound clothes2
    scene lunaf2 with dis2
    mc "Oof, your legs are super tense too." with dis
    mc "You’re lucky that I got here in time!"
    l "*Giggles* I'll have to recommend your services to everyone I know."
    l "You're very caring."
    mc "Well, it’s the duty of a good masseur to leave every one of their customers satisfied!"
    mc "Here at the [lastname] Massage Parlor, customer satisfaction is priority numero uno!"
    l "*Giggles* That's a good policy."
    mct "She's totally relaxed now."
    mct "It feels like she trusts me completely."
    mct "And for some reason that makes me feel special."
    mct "I just want to make her feel... safe."
    mct "Is that normal?"
    mct "I mean, fuck, I'm massaging a half naked girl with a 10/10 body and I can only think of how nice it is that she's feeling comfortable around me."
    mct "Although..."
    mct "Well, now that I’m thinking about it..."
    mct "Jesus, Luna's body is breathtaking."
    mct "The way she's arching her back makes her curvy butt stand out even more."
    mct "I wonder if she's doing that on purpose..."
    pause
    mc "All good, Luna?"with dissolve
    mc "You're so quiet all of a sudden."
    mc "Please tell me you didn't fall asleep. That would be devastating for my customer reviews."
    scene dm 41
    l "No... I didn't." with dis12
    l "I'm feeling better than I thought I’d be."
    l "It's just that... I love the feeling of your hands. You weren’t exaggerating about your expertise."
    l "It's like a... p-pampering sensation."
    mc "Happy to hear that..."
    scene lunaf2 with dis17
    menu:
        with dis
        "Get closer to her private parts":
            mct "God, this is so sexy."with dis06
            $ lunamassagefail = True
            mct "And Luna looks... receptive."
            mct "I wonder what would happen if things got a bit more intimate."
            mct "You know what? Fuck it."
            mct "Nothing ventured, nothing gained!"
            scene dm 42
            mc "Um... do you mind if I step it up a gear, Luna...?" with dis15
            show dm 41
            l "Step it up a gear?"
            l "What do you mean?"
            show dm 42
            mc "Well, you know..."
            mc "Something like..."
            show dm 43
            bla "You move your hand along Luna's thigh all the way up until you can feel her pussy lips through the thin fabric of her bikini." with dis15
            scene dm 41
            l "Aaah..." with dis15
            bla "She lets out a small moan from the back of her throat."
            l ". . ."
            show dm 44
            l ". . . ?"with dis
            stop music2 fadeout 6
            play music birds volume 1.5
            play sound chair4
            play sound2 clothes2
            play sound3 chair3
            show dm 73
            bla "Luna suddenly sits up and moves away from you." with dis
            show dm 73
            mct "Oh, fuck."
            mc "I-I'm sorry!"
            mc "I didn't want to..."
            mc "I m-misread the signals, sorry."
            show dm 72
            l "N-No! It's my fault."
            l "I... I-I liked it."
            l "But..."
            l "It's just that..."
            l "It startled me."
            l "I'm not used to physical contact. Yet."
            l "I'm sorry."
            show dm 73
            mc "Don't be sorry! That makes sense. The last thing I want to do is make you uncomfortable."
            mc "Let's just say that it was no one's fault!"
            show dm 72
            l "Yeah."
            l "Um... you should probably make sure you’re ready to leave, my dad’s probably almost done with packing the car. I’m gonna change too."
            l "I'll see you Monday at school!"
            show dm 73
            mc "S-Sure!"
            show dm 72
            l "Thank you for coming, [mc]."
            play sound doorsliding
            show dm 74
            bla "She flees the terrace, with her breasts covered and her back turned towards you." with dis17
            show dm 75
            mct "God, that was awkward." with dis12
            mct "I feel so... guilty. We were having such a good time and then I went and upset her like that."
            mc "*Sighs* (Anyways, I guess I should go get dressed too.)"
            mct "I just hope she's not angry."
            mct "Luckily, knowing Luna, I'm pretty sure that's not the case."
            mct "Or so I hope..."
            jump preposmassageluna
        "[gr]Don't push it":
            mc "If you want to change your position or you want me to change anything, just let me know." with dis08
    mc "The most important thing is that you are comfortable."
    scene dm 41
    l "I'm doing terrific..."with dis
    l "Just..."
    l "Do you mind if I turn around?"
    mc "*Gulps* Not at all."
    mct "Oh boy..."
    mct "Is she going to put her top back on, or...?"
    play sound clothes3
    play sound2 clothes4
    show dm 45 with dis14
    l "*Turning around* Thank you." with dissolve
    show dm 46
    mct "Doesn't seem to be the case..."with dissolve
    show dm 45
    l "T-This is a little embarrassing, though."with dissolve
    show dm 46
    mc "Nonsense!"with dissolve
    mc "You have nothing to worry about, our employees are strictly professional."
    mc "Their gaze never drifts to where it doesn't belong."
    mc "Just relax and continue enjoying your massage, ma'am."
    l "*Giggles* Mm-hm..."
    scene lunaf3 with dis22
    mct "My god, Luna's skin feels softer than silk." with dis
    mct "She barely has any body hair, and it almost looks like porcelain."
    l ". . ."
    mct "She’s completely changed since the beginning of the massage."
    mct "It almost feels like she’s asking me to touch it... to caress it..."
    mct "I know she's not used to touching other people with her bare hands, but she's probably not used to any other kind of physical contact either."
    mct "Maybe that's what makes it so special."
    pause
    bla "The birdsong above is only interrupted by the noise of your hands rubbing up against Luna's body and the soothing sound of her soft sighs and small moans." with dis08
    mct "Man, this is getting hotter and hotter every second, and we're not even saying anything."
    mct "I wonder what she's thinking right now."
    mct "She looks so... receptive."
    mct "Would it be crazy to try to make things a little more intimate...?"
    l ". . ."
    mc "Does it feel good, Luna?"
    l "Mm-hm..."
    mc "If you want me to change the position of my hands, you just have to say so."
    show dm 47
    l "Your hands...?"with dis15
    mc "Yeah, I mean..."
    mc "I wouldn't want to cross any line that could make you uncomfortable."
    l "Oh..."
    l "Don't worry..."
    l "I feel safe in your hands. I feel... good."
    mc "Alright..."
    show dm 48
    bla "You move your hand along Luna's thigh." with dis14
    mct "Alright... she didn't flinch."
    mct "So far so good..."
    show dm 49
    bla "Luna lets out a slight moan." with dis15
    mc "Are you okay? I can sto–"
    show dm 51
    l "N-No. Don't. Don’t stop."
    l "It feels good."
    l "I-I want you to touch me."
    show dm 50
    mc "Touch you?"
    show dm 51
    l "Yes. I want to... feel your hands all over my... body."
    show dm 50
    mct "Oh god."with dis06
    mct "Did she really say that?!"
    mc "Alright, ma'am..."
    mc "Here at [lastname] Parlor... the customer's always right."
    mc "Your wish... is my command..."
    scene lunaf4 with dis22
    bla "You start rubbing the palm of your hand against Luna's pussy as delicately as possible." with dis08
    l "*Slightly moaning* Aahh..."
    mct "Jesus..."
    mct "I can feel Luna's fleshy pussy through the fabric."
    mct "She's wetter now than when she was in the pool."
    l "Aaaahh..."
    pause
    mc "*Looking at Luna's chest* (Damn, Luna's tits sure are bigger than they seem at first glance)."with dis06
    mct "She can barely cover them with her arm."
    mct "Come on... let me see those pink nipples..."
    mct "Please..."
    bla "Luna's fidgeting accelerates, and her breath hastens."
    scene dm 52
    l "Ahh... ahh... ahhh..."with dis15
    play sound clothes4
    play sound2 chair4
    show dm 53
    l "*Moaning* Oh my god..." with dis15
    mct "OH YES!"
    scene lunaf5 with dis2
    l "*Moaning* O-Oh g-god..." with dissolve
    bla "Carried away by the situation, Luna’s arm drops to her side, completely freeing her breasts. Her legs twitch nervously."
    mct "That's what I'm talking about..."
    bla "Her shyness almost completely forgotten, Luna’s body begins to roll on the massage table."
    l "*Moaning* Ahh... aah... ah...."
    mct "My god, look at those perfectly round boobs... I need to stop myself from bending down and just going to town on her... I’m still not sure how she’d react."
    mct "I have to imagine we’re close to her limits, considering her lack of physical contact."
    mct "I just want to take her and make her mine..."
    mct "But... you've gotta wait, [mc]... Now’s not the proper time for it."
    pause
    l "*Moaning* Agh... aah..." with dis08
    mct "Luna's whimpers of pleasure are intoxicating."
    mct "I never thought I’d live to hear them..."
    scene lunaf6 with dis2
    l "*Panting* AAahh... ahh... aah..." with dis
    mc "You're perfect, Luna..."
    mct "Fuck, my pants are about to explode. Getting into some jeans was a bad fucking idea."
    l "*Moaning* Ahh...!"
    mct "Her back is tense and stiff, but instead of moving away, she's bringing her hips towards me."
    mct "I like that..."
    mct "Judging by her reactions to my caresses, I bet that any kind of physical touch feels way more intense to Luna."
    mct "As if her whole body had sensitivity cranked to max."
    mct "How I'd like to drive her crazy with pleasure..."
    l "Ahh... {w}ahhhh...."
    play sound clothes4
    play sound2 chair4
    show dm 54
    l "*Sitting up* Aaagh...!" with dis12
    l "Oh g-god..."
    show dm 55
    mc "Is everything okay?" with dis12
    l "*Blowing out air* No..."
    l "I mean... y-yes."
    if luna_points <= 10:
        show dm 57
        l "I mean..." with dis15
        stop music2 fadeout 5
        play music birds fadein 2
        jump jumpmassageluna
    show dm 56
    mc "We can stop here, if you want." with dissolve
    show dm 57
    l "No..." with dis
    l "I..."
    show dm 58
    bla "Luna puts her hand on your chest one more time. You can see a shiver running through her body as she sighs deliriously." with dis12
    l "I-I can feel your heart beating."
    l "It's pounding..."
    show dm 59
    l "I..." with dis14
    l "I want you to keep massaging me."
    l "B-But... I want to feel you {i}somewhere else..."
    show dm 60
    mc "Somewhere else?"with dissolve
    mc "Do you mean... that you want me to touch you directly?"
    show dm 59
    l "Y-Yes."with dissolve
    show dm 60
    mct "Oh my god... Did Luna Hernandez really just ask me what I think she asked me?"with dissolve
    show dm 61
    mc "My Luna..." with dis12
    show dm 62
    bla "You move the thin piece of clothing to the side, revealing Luna's smooth, pink pussy." with dis15
    show dm 63
    bla "You cautiously insert one finger inside her." with dis15
    l "AAaahhh..."
    show dm 64
    l "OH M-MY GOD."with dis
    l "Y-You're inside."
    mc "I am..."
    l "*Hyperventilating* Ahh..."
    scene lunaf7 with dis22
    bla "You insert both fingers inside Luna's vagina and start massaging her insides with a steady rhythm." with dis08
    l "*Panting* Oh g-god..."
    l "Aaaahh... ahhhh... aaah..."
    mct "Jesus... like I expected, Luna feels incredibly tight."
    mct "However, her pussy’s so soaked... my fingers are sliding in, like her whole body was begging me for them."
    l "*Panting* Ahhh..."
    l "*Panting* T-This is... {w}incredible..."
    bla "As you begin to increase your pace further, Luna's whole body twists and twitches. A high-pitched moan escapes her mouth."
    mct "Thank god the sounds of the mountain cover up her sounds."
    l "*Panting* AAahh... aahh..."
    pause
    mct "God, it drives me insane when she looks me in the eyes."with dis
    mct "I wonder how Luna’s sensitivity to physical touch would affect her during sex..."
    mct "Would it be counterproductive?"
    mct "Or on the contrary... would she become insatiable?"
    l "*Moaning* AHHH... "
    l "*Moaning* [mc]..."
    l "*Panting* AHHH!"
    l "*Panting* W-What is going on... "
    mct "Is she gonna cum?"
    l "*Panting* AAAahhh... I can't..."
    l "*Panting* I h-h-have to..."
    play sound cum2
    play sound2 cum2
    play sound3 chair3
    play sound4 clothes4
    scene dm 66
    l "AAAAAaaaaaAaahhh...." with hpunchlong3
    if anniepath:
        mct "You did it again, [mc]..."
    play sound5 clothes3 volume 1.5
    show dm 67 with dis15
    $ luna_points += 1
    play sound beat
    show screen heartbeat
    l "*Recovering her breath* Ahhh... ahghh... ahh... ahhh..."with dis
    mc "My god, your body is unbelievably perfect, Luna..."
    l "*Recovering her breath* Ahhh... ahh... ahhh..."
    l "*Recovering her breath* {b}F-FUCK..."
    mc "Um... excuse me?!"
    mc "Did you just say the “F” word?!"
    l "*Recovering her breath* W-What...?"
    mc "*Chuckles* Nothing..."
    mct "It's the first time I heard her swear in the time I’ve known her."
    mct "That was hot..."
    l "*Recovering her breath* My god... t-that was... the most intense thing I've ever felt..."
    mc "That's good to hear..."
    show dm 68 with dis15
    pause
    show dm 69
    bla "Luna's hand starts to move along your torso towards your jeans." with dis14
    mct "Hmm...?"
    show dm 70
    mct "Is she trying to sense my body as before? Or is she..."with dis15
    show dm 67
    mct "Oh my god, is this really happening?!" with dis12
    mct "Is she going to..."
    play soundlow carhorn
    stop music2
    play music birds volume 1.5
    show dm 71
    her "[mc]! Where are you?" with hpunch
    her "We've gotta leave!"with hpunch
    mc "W-What?"
    mct "Dammit, I completely forgot about the world for a moment."
    l ". . ."
label jumpmassageluna:
    play sound chair4
    play sound2 clothes2
    play sound3 chair3
    show dm 73
    bla "Knocked out of her trance, Luna sits up and moves away from you." with dis
    show dm 73
    mct "Oh, fuck."
    mc "Um..."
    show dm 72
    l "G-God! It's so late!"
    l "I... I-I'm sorry, I don’t want to delay you."
    show dm 73
    mc "What?! Don’t worry about that!"
    mc "I want to be with you!"
    mc "I can stay and–"
    show dm 72
    l "No!"
    l "Don't do that! You've gotta leave, and... I have things to do here too!"
    l "Um... I should go and get changed."
    l "I-I'll see you Monday at school!"
    show dm 73
    mc "Um... of course."
    show dm 72
    l "Thank you for coming, [mc]."
    play sound doorsliding
    show dm 74
    bla "She flees the terrace, with her breasts covered and her back turned towards you." with dis17
    show dm 75
    mct "God, that was awkward." with dis14
    mct "What the hell happened? Everything was perfect, and then..."
    mct "Goddammit."
    mct "I hope she doesn't regret what we did."
    mct "I know this was a huge step for Luna."
    mc "*Sighs* (Anyway, I guess I should go get dressed too.)"
    mct "I just hope she's not angry."
    mct "Luckily, knowing Luna, I'm pretty sure that's not the case."
    mct "Or so I hope..."
    jump preposmassageluna


label preposmassageluna:
    $ renpy.music.set_volume(0.0, delay=4.0, channel='music')
    show black
    show screen afewminuteslater
    with dis2
    pause
    $ renpy.music.set_volume(1.0, delay=4.0, channel='music')
    play sound5 doorsliding
    scene dm 76
    hide screen afewminuteslater
    with dis2
    mc "*Taking a deep breath* Hmm..."with dis
    mc "Alright, ready to go."
    mct "Dammit, I was kind of expecting to see her waiting for me here."
    mct "Am I really gonna leave like this...?"
    mct "That farewell was... cold."
    mc ". . ."
    mct "Agh, I ruined a perfect day."
    if not lunamassagefail:
        mct "Should I go back inside to look for her?"
        mct "Maybe I can fix it..."
        menu:
            with dis
            "[gr]Go back inside":
                mct "Yeah, of course I'm going back! I have to find her!"with dis08
                mct "I can't leave without a proper goodbye."
                $ unlock_look("luna", 8)
                play soundlow leaves2
                show dm 77
                mct "Let's..." with dis15
                play music2 love fadein 5
                stop music fadeout 9
                bla "You turn around and see Luna standing in the middle of the pathway."
                mc "L-Luna!"
                mc "I-I thought you wouldn’t come to say goodbye."
                show dm 78
                l "Of course! I..." with dis12
                l "I'm sorry I left like that."
                l "It's just that... I was startled."
                show dm 79
                mc "*Chuckles* I guess that makes sense, given the situation."
                mc "I'm honestly not sure how that escalated so fast either, but..."
                mc "I'm glad I had that moment with you."
                show dm 78
                l "It was... amazing."
                l "And not only the {i}massage{/i}, everything was amazing today."
                l "Thank you for coming today, [mc]."
                l "I know you probably had a thousand things more fun to do than spending a day with me and my family, so... I appreciate it a lot."
                show dm 79
                mc "A thousand things, surely."
                mc "But more fun? No way."
                mc "I could spend every day with you and never get bored."
                l ". . ."
                show dm 78
                l "I've never opened up to anyone about my powers, my insecurities, or my thoughts... but with you... it's different."
                l "I... I feel safe when I'm with you."
                l "As if I could tell you anything."
                l "Thank you for being there for me, [mc]."
                show dm 79
                mc "And I'll always be there, Luna."
                mc "Always."
                show dm 78
                l "T-Text me when you get to Kredon!"
                show dm 79
                mc "Will do!"
                mc "Will I see you Monday at school?"
                show dm 78
                l "Definitely!"
                if trykissluna:
                    show dm 79
                    mc "Alright then... take care, Luna."
                    mc "I'll miss you!"
                    show dm 76 with dis15
                    mc "*Turning around* (Well, that was definitely be–)"with dis08
                    play sound leaves2
                    show dm 81
                    bla "Luna grabs you by the arm with her bare hand, this time with nary a shudder." with dis15
                    mc "Huh?"
                    show dm 80
                    l "W-when we were at the pool before..." with dis04
                    l "And I touched you without my gloves..."
                    l "D-Did you try to kiss me?"
                    show dm 81
                    mc "W-What?"with dis04
                    mc "*Nervous chuckle* I thought you didn't notice."
                    mc "Um... yeah, I did."
                    play soundlow leaves2 fadein 1
                    show dm 82
                    bla "She gets closer to you." with dis15
                    mct "And here we are again..."
                    mct "This time, though..."
                    mct "She doesn't even have to say anything. Her eyes are telling me everything I need to know."
                    menu:
                        with dis
                        "Kiss her [luna_pts]":
                            play soundlow leaves2 fadein 1.5
                            show dm 83 with Dissolve(1.6)
                            $ luna_points += 1
                            play sound beat
                            show screen heartbeat
                            bla "You and Luna silently merge your lips into a long, lingering kiss." with dis12
                            l ". . ."
                            mc ". . ."
                            play soundlow leaves2 fadein 1.5
                            show dm 85
                            l "*Giggles* Sorry, that was probably very clumsy." with dis15
                            show dm 84
                            mc "It was perfect."
                            mc "I just hope I didn't taste like your dad's tacos."
                            show dm 85
                            l "*Laughs* You didn't, don't worry."
                            show dm 84
                            mc "Now I have something to think about during my return trip."
                            show dm 85
                            l "I guess so..."
                            l "W-Well, I've gotta go!"
                            l "I think my grandma wants to go for a walk. I should try to find my boots."
                            show dm 84
                            mc "Alright then..."
                else:
                    show dm 84
                    mc "Alright then..." with dis14
                mc "Take care, Luna."
                mc "I'll miss you!"
                show dm 85
                l "Me too."
                if penelopepath:
                    l "Have fun at tonight's party, and... tell my dad to be careful when driving."
                else:
                    l "Have fun and... tell my dad to be careful when driving!"
                show dm 84
                mc "*Laughs* I will!"
                mc "You have fun too!"
                show dm 76 with dis17
                mct "Now... THAT was a good goodbye!" with dis08
                play soundlow doorsliding
                bla "You hear Luna go back inside, and swear you can see her doing little jumps from the corner of your eye."
            "Don't go back inside":
                mct "Nah... it would only make things worse."with dis08
                mct "Let's go back to Kredon."
                mct "I'm sure everything will be fine after a couple of days, there's no need to make it awkward."
                jump posmassageluna
    else:
        mct "What a fucking mess."
        play soundlow carhorn
        her "[mc]! Where are you?" with hpunch
        her "We've gotta leave!"with hpunch
        mc "Y-YEAH! I'M COMING, SIR, SORRY!"


label posmassageluna:
    scene dd 98b with dis22
    stop music2 fadeout 8
    pause
    play sound dooropen2
    $ renpy.music.set_volume(0.4, channel='soundloop')
    play soundloop carengine fadein 4
    show dm 87 with dis22
    stop music fadeout 6
    mc "I'm ready, sir!"with dis08
    unc "*Sobbing* I'll miss you, brother!"with hpunch
    her "Me too, hermanito!"
    unc "Promise me you'll pop back for Christmas!"
    her "Don't worry, I'll come back sooner than that."
    her "And hey, I'll see you tomorrow! You have to bring my daughter back to me!"
    unc "Oh... I promise nothing. We love her too much."
    her "*Laughs* Don't make me come back!"
    lg "Be careful driving, Victor!"
    show dm 89
    mc "Well, I'm leaving too!" with dis14
    mc "Ms. Hernandez, Hugo, thank you so much for inviting me to your home today."
    mc "I had a lot of fun!"
    show dm 90
    unc "My pleasure, [mc]!"
    unc "We enjoyed having you here with us, you're a very nice lad."
    if reallyspicy:
        unc "A man who can survive my brother's extra spicy tacos is always worthy of my respect."
    unc "I'm glad you're friends with my little niece."
    show dm 88
    if grandmacheck:
        lg "And thanks again for joining the ofrenda of Luna's mother and saying a few words, [mc]."
        lg "It meant a lot to me."
    lg "You can come back whenever you want."
    show dm 89
    mc "Thank you very much!"
    mc "The pleasure was all mine."
    show dm 91
    her "Alright, [mc], are you ready?"with dis12
    show dm 92
    mc "Ready!"
    show dm 93
    her "Then get in the car!"with dis
    her "Fiero will take us back to Kredon in 5 hours! Or maybe even less!"
    play sound swallow
    mc "*Gulps* A-Alright."
    stop soundloop fadeout 5
    scene black with dis25
    show screen afewhourslater with dis15


label costumeparty:
    pause
    hide screen nextday
    hide screen afewhourslater
    play music2 happy11 fadein 5
    scene dm 1
    with dis27
    mct "Ah, home sweet home!" with dis
    if lunapath or lunaunclehouse:
        if penelopepath:
            mct "Hmm... there's still an hour left until the party starts."
        mct "I still can't believe Mr. Hernandez managed to arrive on time. That man sure knows the road!"
    else:
        mct "It felt good to hit the gym again."
        mct "Taking a couple of days off Eternum was the right call. I don't wanna start suffering from those hallucinations in real life that those Eternum addicts get..."
    if not novapath and not penelopepath:
        show dm 2 with dis15
        mct "Tonight's the party at Penelope's university. I guess she must have left already." with dissolve
        mct "That will probably be tons of fun... but I don't even have a costume, so I wouldn't have been able to go. Though, it’s not like I was even invited in the first place."
        mct "Well, maybe next year."
        mct "I'll go to sleep early tonight. I'm supposed to go with Nancy to her office tomorrow morning anyway."
        mct "I'll show her what I'm capable of!"
        stop music2 fadeout 6
        jump nancyworkplace
    show dm 3
    mct "I think I received some messages earlier..." with dis15
    if lunapath:
        call chat (luna_chat2) from _call_chat_12
        if annielunaserver >= 1:
            show dm 4
            mct "I wish I could play with them!"
            mct "I'm sure the two of them make a great team."
            show dm 3
        mct "Let's see what else..."with dis04
    if novapath and not novadrawinglook:
        call chat (nova_chat3) from _call_chat_9
        show dm 4
        mc "*Chuckles* (So she spent the afternoon here? That's pretty nice.)" with dis06
        mct "I'm glad to see Nova becoming friends with Penny, Dalia and Nancy."
        if lunapath or lunaunclehouse:
            show dm 3
            if photoannie:
                mct "Oh! I got a response from Annie too." with dissolve
            else:
                mc "Hmm..."with dissolve
        else:
            show dm 3
            mct "I can't really wait for her for too long, though." with dis04
            mct "I've gotta–"
            jump novamanga
    if lunapath or lunaunclehouse:
        if photoannie:
            call chat (annie_chat) from _call_chat_10
            if photoannie:
                show dm 4
                mct "Oh boy, that photo was sexy as hell." with dis06
                mct "I'm saving that to my private gallery."
                show dm 3
                mct "And... well, that was all."with dis06
                if not novapath or novadrawinglook:
                    show dm 2
                    mct "Alright, let's go inside. The shower is calling me..." with dis12
                    jump collegeparty
                mct "Anyway... I hope Nova doesn't take too long."
            else:
                mct "Meh, I guess I was just imagining things."
                mct "My mind must have been playing tricks on me."
                if not novapath or novadrawinglook:
                    show dm 2
                    mct "Alright, let's go inside. The shower is calling me..." with dis12
                    jump collegeparty
                mct "Hmm..."
                mct "Anyway, I hope Nova doesn't take too long."
            mct "I can't really wait for her much lo–"
        else:
            mct "Chang hasn't answered yet."
            mct "He read my message, though."
            show dm 4
            mct "That sneaky bastard must be too busy thinking about how to make Micaela fall in love with him."with dis04
            mct "I probably shouldn’t bother him with my bullshit."
            if not novapath or novadrawinglook:
                show dm 2
                mct "Alright, let's go inside. The shower is calling me..." with dis12
                jump collegeparty
            show dm 3
            mct "I hope Nova doesn't take too long."with dissolve
            mct "I can't really wait for her much lo–"
    if not novapath and not lunapath:
        mct "And... oh."
        mct "It was just a spam email about a new crypto platform."
        mct "Really? That's all I got in 6 hours?"
        show dm 2
        mct "I guess I'm not the most popular guy in Kredon..." with dis15
        mct "Bah, who cares. I've got a costume party waiting for me!"
        mct "But first of all... I should take a shower. I can even smell myself..."
        stop music2 fadeout 6
        jump collegeparty
label novamanga:
    play sound pop
    play sound2 whoosh6
    play sound3 whoosh6
    stop music2
    $ renpy.music.set_volume(0.5, channel='music3')
    play music3 quirkynova fadein 4
    scene dm 5
    no "{size=55}HI!" with hpunch
    mc "Gggh!"
    show dm 5b
    mc ". . ." with dis14
    show dm 7
    mc "You'll never change, will you?"with dis12
    show dm 6
    no "*Giggles* Hey, you didn't scream this time! Just a little gasp."
    show dm 7
    mc "I must be getting used to your sneak attacks."
    show dm 6
    no "I’ll have to up my game!"
    show dm 8
    if penelopepath:
        mc "Shouldn't you be dressed by now? The party will begin shortly."with dis12
        show dm 8b
        no "No worries!"
        no "I left everything I need in my room and my mom will do my hair."
        no "It won't take me more than 30 minutes!"
        show dm 8
        mc "Ah, I see you've got it covered!"
        mc "Alright girly, what do you need from me, then?"
        mc "Why did you come back?"
    else:
        mc "Well... what do you need?" with dis12
        mc "I just got back and honestly, I'm a little exhausted."
    play sound2 clothes4
    show dm 9
    no "I finished what I was drawing!" with dis08
    mc "OH! Awesome!"
    no "I came to see Penelope and I brought this with me in case you were here."
    no "Do you wanna see it?"
    mc "Of course!"
    show dm 10
    play sound paper2
    play sound3 paper
    blank "{i}Nova opens her folder with shaky hands, and gives you two sheets of paper." with dis15
    mc "Hmm?"
    mc "Holy shit, that's... a manga comic!"
    mc "And... wait."
    mc "Is that..."
    no "*Clears throat* Ahem!"
    play sound paper2
    play sound3 paper
    scene dm 11
    show nomanga1
    with dis12
    blank "{i}She starts imitating Thanatos' voice, trying to sound somber and intimidating." with dis08
    no "{bt=3}Soon, the ten Gems will be mine... \nAnd I will rule over a sea of blood!{/bt}"
    mc "*Laughs* You nailed him!"
    play sound4 shotgun
    play sound7 blood3
    hide nomanga1
    show nomanga2
    no "{sc=2}{i}BANGGGG!!!{/sc}"with hpunch
    blank "{i}She imitates the sound of a shot with her mouth."
    play sound whoosh6
    hide nomanga2
    show nomanga3
    no "It's over, Thanatos!"
    no "You are no match for Delilah Warren and Dione!"
    mc "*Laughs* Damn! I love anime Nova!"
    no "*Giggles* Thanks!"
    mc "Why is she holding the rifle like that, though?"
    no "DON'T INTERRUPT!" with vpunch
    no "{i}CLACKKK!"
    blank "{i}Nova makes a metallic sound with her mouth you can't identify."
    mc ". . ."
    no "She's reloading the magazine!"
    mc "Ohhh!"
    play sound dodge
    hide nomanga3
    show nomanga4
    no "{sc=2}{i}WHOOSH!!!{/sc}" with hpunch
    no "*Gasps* He's so fast!"
    play sound2 sword2
    hide nomanga4
    show nomanga5
    no "{bt=3}You PATHETIC creature!{/bt}"
    no "*Gasps in her normal tone of voice*"
    mc "*Chuckles* (I love how much passion and \nenthusiasm she's putting into her narration.)"
    no "{bt=3}I will kill you, just as I killed hi-{/bt}"
    play sound punch
    play sound2 bonecrush2
    play sound3 whoosh6
    hide nomanga5
    show nomanga7
    no "{sc=2}{i}BAMMMM!!!{/sc}" with pushdfast
    play sound4 whoosh6
    play sound5 gore
    play sound6 blood3
    hide nomanga7
    show nomanga8
    no "{sc=2}AAAAARGH!!!{/sc}" with vpunch
    play sound punch
    play sound2 rocks
    hide nomanga8
    if novacomicnoturgent:
        show nomanga9notu with vpunch
        no "{b}That doesn't seem very urgent..." with dis
        no "{sc=2}{b}I'VE GOT THINGS TO DO, I'LL SEE YOU LATER.{/sc}"
    elif mcsayingafterkill == 1:
        show nomanga9a with vpunch
        no "{b}The only fate of the weak... is to be crushed by the strong." with dis
        no "{sc=2}{b}KNOW YOUR PLACE, DEMON.{/sc}"
    elif mcsayingafterkill == 2:
        show nomanga9b with vpunch
        no "{b}Nothing personal, demon." with dis
        no "{sc=2}{b}JUST TAKING OUT THE TRASH.{/sc}"
    else:
        show nomanga9c with vpunch
        no "{b}You sealed your fate the moment you put your filthy hands on her, demon." with dis
        no "{sc=2}{b}GO TO HELL... AGAIN.{/sc}"
    mc "DAMN!"
    mc "That's my line!"
    no "*Giggles* Yes!"
    if novacomicnoturgent:
        mc "I mean... t-that wasn't meant for the comic, I was actually texting that to you."
        mc "But still!"
    mc "This last panel looks so cool!"
    mct "Hmm... am I crazy or did she draw herself with bigger boobs?"
    mc "Your anime self even has the same mole on your chest!"
    no "W-What?"
    no "*Nervous laugh* O-Oh, yeah...! I wanted it to be accurate, y'know."
    no "I d-didn't think you'd remember that..."
    mct "Hard to forget..."
    scene dm 11
label mangapage1:
    play sound paper2
    play sound2 paper
    call screen manga1 with dis
label mangapage2:
    play sound paper2
    play sound2 paper
    call screen manga2 with dis
label mangapageexit:
    play sound paper2
    hide manga2 dm 11
    scene dm 12
    blank "{i}You look back at Nova, who stands in front of you eagerly waiting for your final reaction." with dis12
    menu:
        with dis
        mod "Try the bad options, though :)"
        "It's not my thing, but...":
            $ novamangabad = True
            mc "Well, it's not really my thing, but... I can tell that you've worked hard on this!"with dis06
        "It looks a little amateurish":
            $ novamangabad = True
            mc "It was a good first try, definitely shows a lot of promise. But I think your strokes here look a little amateurish. You might want to look it over!"with dis06
        "[gr]I just love it":
            mc "I just love it."with dis06
    if novamangabad:
        stop music3
        play music town_ambience fadein 6
        play sound backbreak
        scene dm 14
        pause .05
        scene dm 13
        pause .05
        scene dm 14
        pause .05
        scene dm 13
        pause .05
        scene dm 14
        pause
        mc "Uh..." with dis08
        mc "Nova?"
        no ". . ."
        mc "I-I mean..."
        mc "It's awesome!"
        mc "I didn't word it well! Um... I just meant that..."
        show dm 16
        no "N-No worries! I know what you mean."with dis12
        no "I..."
        no "We can't be good at everything."
        no "I shouldn’t waste your time on stupid shit like this. I should focus on hacking so we can find the Gems."
        show dm 15
        mc "That's not what I meant!"
        show dm 16
        no "I know! I... uh..."
        no "I'm sorry, this nerdy nonsense is probably so dumb to you."
        if penelopepath:
            no "We should get ready for that party, eh?"
            no "I just hope my ridiculous costume isn't too ridiculous... haha...ha!"
            show dm 15
            mc "Come on, Nova, I'm sure it's amazing!"
            show dm 16
            no "Yeah..."
        else:
            no "Anyway, I'll just take my drawings back home."
            no "Thanks for your feedback."
        show dm 15
        mct "Dammit... I can't help but feel bad now. Really put my foot in my mouth."
        show dm 17
        if penelopepath:
            no "Alright! I'll meet you and Penelope in a few minutes!" with dis
        else:
            no "Alright! Gotta go now!" with dis
        no "See ya!"
        mc "Are you sure you're okay...?"
        no "Yeah! No worries. It's alright."
        no "Bye [mc]!"
        show dm 2 with dis2
        mct "Damn, she’s so sensitive to criticism." with dis08
        mct "I feel kinda bad, but maybe it will be good for her in the long term."
        mct "And knowing Nova, I'm sure she'll get over it in just a few minutes."
        mct "Or so I hope."
    else:
        $ nova_points += 1
        play sound beat
        show screen heartbeat
        show dm 18
        no "R-Really??" with dis
        no "Do you like it?"
        mc "Seriously, I love it!"
        mc "You aced the characters. I can't believe you were able to draw Thanatos so accurately just after seeing him once."
        no "T-Thank you!"
        no "I have a good memory. And I've always loved manga, so... I thought I’d try it out. And I know you’re into this stuff too, so..."
        mc "You're just full of surprises, miss."
        mc "And I really like how my anime self looks!"
        show dm 19
        no "Oh... you mean the guy who rescues the girl from Thanatos? It's just a random hero." with dis
        show dm 20
        mc "A random hero...?"
        show dm 19
        no "Uh... yeah. It's not supposed to be anyone in particular."
        show dm 20
        mc "I mean, he has my hairstyle and hair color, green eyes, skin, he says my quote..."
        show dm 19
        no "Well, I might have been inspired by people I know. An amalgam of the coolest guys I know."
        show dm 20
        mc "*Chuckles* Ah, yeah, that makes sense."
        mc "Well, in any case... can I keep it? Even if the hero of the manga is totally not me?"
        show dm 18
        no "Yes, you can!" with dis
        no "I'm glad you liked it!"
        if penelopepath:
            mc "Well, we should start getting ready, don't you think?"
            show dm 12
            no "Yes, you're right!"with dis
            no "I'll see you and Penny soon."
        else:
            show dm 17
            no "Well, I gotta go!"with dis
            no "I'll see you tomorrow, [mc]!"
        mc "Sure!"
        mc "Thanks again for the manga!"
        show dm 18
        no "*Giggles* You're welcome, you're welcome!"with dis
        no "Bye!"
        show dm 2 with dis2
        mc "*Chuckles* (Well, this was unexpected.)" with dis08
        mct "Not everyone gives gifts without a reason like she did."
        mct "And I really meant it, she nailed it! I can tell that she spent dozens of hours drawing this."
        mct "I should think about something to give back as a gift."
        mct "Probably not another manga, it would look like something drawn by a five-year-old..."
    if penelopepath:
        mct "But anyway, it's time to get ready."
        mct "I’m making my college debut tonight! Gotta impress all those university girls..."
        if novapath:
            mct "Especially one or two in particular..."
        else:
            mct "Especially one in particular..."
        stop music3 fadeout 6
    else:
        mc "*Yawns* (Anyway, I guess I should get inside.)"
        mct "I think all the girls are out today, and Penelope is going to that party of hers shortly, so... I’ve got the whole house to myself."
        mct "Just me, a TV, and a bag of chips."
        mc "*Sigh* (Living the dream, [mc]!)"
        stop music fadeout 6
        stop music3 fadeout 6
        jump nancyworkplace



label collegeparty:
    stop music fadeout 6
    stop music2 fadeout 6
    play soundloop shower2 fadein 5
    show df 1 with Dissolve(2.7)
    mct "Ahh... a hot shower really does wonders." with dis
    mct "I needed this so much."
    show df 2
    mct "Especially with the night I have ahead of me."with dis15
    mct "I'm not sure how wild these college parties are, but I doubt we'll be going to sleep early tonight."
    mct "I'm sure it will be fun regardless, though."
    if novapath:
        mct "I can't wait to see Penny and Nova's costumes!"
    else:
        mct "I can't wait to see Penny's costume!"
    play sound knock1 fadein 1.5
    show df 3
    p "*Knocks on the door* [mc]? Is that you?" with dis
    mct "Ah, speak of the devil..."
    mc "Yep!"
    mc "Sorry, I'm almost done. Give me 5 minutes."
    p "No, no, I took a shower already!"
    p "I just need to grab a couple of bottles from the cabinet real quick."
    p "Can I come in?"
    menu:
        with dis
        "[gr]Yes{#0.5,pennybathroom}":
            $ pennyshower = True
            mc "Um... sure." with dissolve
            mc "No problem."
            play sound doorclose
            play music2 quirky6 fadein 6
            $ unlock_look("penelope", 10)
            show df 4
            p "Thanks!" with dis12
            p "I won't look, I promise."
            mc "*Chuckles* It's okay."
            mc "I’m not too shy about my body... I’ve got nothing to hide!"
            p "Alright then... good to know."
            play sound2 cabinet
            show df 5 with dis
            p "*Grabbing some bottles from the closet* I guess we have that in common. I’m perfectly fine with showing off my body too."with dissolve
            mc "Y-Yeah."
            show df 6
            mct "Jesus, she's not even wearing a bra."with dis
            mct "Look at those huge tits... They’re basically defying gravity."
            mct "My god. Staring at these while I’m in the shower is probably a bad idea."
            mct "I should probably stop before she turns around and catches me with a boner."
            show df 2
            mc "*Clears throat* So... are you planning to drink a lot tonight?" with dis12
            p "*Giggles* I don't know... are you?"
            mc "Me? I'm gonna set some drinking records tonight!"
            p "*Giggles* Just make sure not to pass out too early..."
            p "I don't think I could carry you back home. You’re pretty... big."
            mc "*Chuckles* Don't worry, I know how to cont–"
            play sound doorglass
            play sound2 curtain2
            show df 7
            mc "*Turning around* T-To control..."with dis12
            p "*Looking at the shower shelves* Hey, is my conditioner in here?"
            p "I thought I left it in the closet, but I didn't see it."
            show df 8
            mc "W-What?"with dissolve
            show df 7
            p "My conditioner."with dissolve
            p "For my hair."
            p "I need a very specific hairstyle for my costume, and I need to nail it."
            show df 8
            mc "Um..."with dissolve
            mc "I-Is it the orange bottle? I think I saw it in the downstairs bathroom."
            show df 9
            p "Oh!" with dis
            p "Okay, cool. Thanks!"
            show df 10
            mc "Y-You're welcome."with dis04
            show df 9
            p "*Chuckles* Are you alright?"with dis04
            show df 10
            mc "Y-Yeah... *clears throat* I mean, yeah."with dis04
            show df 9
            p "I thought you said you didn't mind me coming in."with dis04
            p "That you weren't a shy person."
            show df 10
            mc "And I'm not!"with dis04
            mc "I'm totally cool with it."
            mc "It’s just that... um... the steam from the shower might mess up your hair."
            mc "Might make your hairstyle all frizzy before the party, y'know."
            show df 9
            p "I see..."with dis04
            p "Cool. Thanks for the concern."
            p "Anyway, now that we’ve both seen each other naked, there's really no reason to make a big deal about this in the future."
            show df 10
            mc "Does that mean that I can enter the bathroom while you're taking a shower too...?"with dis04
            show df 9
            p "Of course."with dis04
            p "As long as you have an urgent and compelling reason to barge into the bathroom while I’m wet and naked in the shower, of course..."
            show df 10
            mc "As urgent as hair conditioner, got it... That makes sense."with dis04
            mct "Good to know..."
            show df 9
            p "Anyway, I have what I need."with dis04
            p "I'll go start getting dressed."
            show df 11
            mc "S-Sure! I'll do the same."with dis15
            mc "See you outside."
            p ". . ."
            show df 12
            blank "{i}Fully aware of your gaze on her, Penelope shifts her eyes downwards and stares directly at your bare penis." with dis
            p ". . ."
            mct "Oh god."
            mct "This should be an awkward situation, but those fuck me eyes are turning me on so much... I think my cock just twitched."
            mct "Please don't get hard now, she'll think I'm just a horny fucking kid..."
            show df 13
            mct "W-Why isn't she saying anything, though? I-Is she smirking?" with dis14
            mct "W-What is going on?!"
            mct "Is she trying to make me feel uncomfortable or is she...?"
            show df 14
            mc "Uh... See anything interesting, Penny?" with dis08
            mc "D-Do you need anything else from the shower?"
            show df 15
            p "Yeah, I'll let you finish your shower, sorry. Didn’t mean to give you a {i}hard{/i} time." with dis
            p "We have to leave in 20 minutes, so don't take too long."
            mc "S-Sure! I'll be ready in 10."
            p "See you outside..."
            stop music2 fadeout 5
            show df 16 with dis15
            play sound doorclose
            mct "Penelope Carter... you’re gonna drive me mad." with dis08
            mct "I was already looking forward to this party, but after that..."
            mct "I should start getting dressed, I CAN'T be late!"
            mct "Let's BLOW UP that party!"
        "No{#0.5,pennybathroom}":
            mc "I'm almost done, just wait a couple of minutes, please."with dissolve
            mc "What do you need?"
            p "Just some hairspray."
            p "But it's okay, I'll grab it before leaving, no big deal."
            p "Don't take too long, though! We have to leave in 20 minutes."
            mc "Noted!"
            show df 2
            mct "Aw, man, I could stay in here for hours." with dis15
            mct "She's right, though, I should start getting dressed."
            mct "I don't want her to be late because of me."
            mc ". . ."
            mct "Just 15 seconds more..."
    stop soundloop fadeout 4
    play music epic2 fadein 4
    show df 17 with dis22
    pause 1.6
    play soundlow thunder
    play sound3 impact2
    show df 18 with hpunch
    pause
    mct "As fast as Hermes..."with dis12
    play sound6 impact2
    show eros1
    mct "As strong as Heracles..."
    show eros2
    play sound7 impact2
    play sound5 thunder
    mct "And as wise as ATHENA!"
    mct "I am..."with hpunch
    play sound5 vibration volume 2
    play sound7 notificationphone2
    stop soundlow
    stop sound3
    stop sound6
    stop music
    play soundloop vent
    scene df 21 with dis
    mc "Hmm?" with dis08
    mct "Dammit, I was just getting into the role."
    play sound switch
    show df 22 with dis12
    if novapath:
        mc "*Turning the lights on* (Oh, it's Nova.)" with dissolve
        call chat (nova_chat2) from _call_chat_11
        mct "Alright, let's not keep her waiting, then." with dis
    else:
        mc "*Turning the lights on* (Agh, goddammit, it's just spam. I have to unsubscribe from this channel.)" with dissolve
        mct "But I'll do it later."
    mct "Time to go!"
    play music night fadein 5
    stop soundloop fadeout 6
    play sound2 dooropen1
    show df 23 with dis15
    play sound doorclose
    mc "Penny? I'm ready!" with dis06
    mc "You all set?"
    play sound3 cat
    carol "*Meows*"
    show df 24
    blank "{i}You look down and notice Carolyn staring at you with begging eyes."with dis12
    mc "Hey there, pretty lady!"
    mc "What's the matter? Did the girls forget about feeding you?"
    mc "Is that it?"
    play soundlow purr2
    carol "*Purring*"
    mc "Is that so?! How dare they!"
    p "*Laughs* Don't let her fool you!"
    $ unlock_look("penelope", 11)
    show df 25
    p "She already had her dinner! If she had her way, she'd never stop eating." with dis12
    p "Dalia and her are two peas in a pod."
    play sound5 clothes3
    show df 26
    mc "Oh... my... GOD!" with dis15
    mc "Did I log into Eternum and forget?! I have the Lady of Eternum right in front of me!"
    show df 27
    p "*Giggles* Do you like it?"
    show df 26
    mc "I love it!"
    mc "You look spectacular, Penny. Really hit it out of the park!"
    mc "You somehow look better than Idriel does... in her own costume!"
    show df 27
    p "Thank you!"
    p "I thought it was appropriate, now that I'm an “Eternumite” too."
    show df 26
    mc "It's amazing! Was it hard to find? Or expensive?"
    show df 27
    p "Not at all! A brand contacted me on Instagram to sponsor me and send me the outfit, so I didn't pay anything. I just have to mention them in my next post."
    p "It’s a little tight in the bust though, these brand sponsors always think I’m exaggerating my breast size..."
    p "I thought of dyeing my hair too for a perfect cosplay, but... I didn't want to risk it."
    p "A lot of things can go wrong, and my hair is the most valuable asset in my modeling career!"
    show df 26
    mc "Well... I wouldn't say the {i}most{/i} valuable..."
    show df 27
    p "*Giggles* Don't be dirty!"
    show df 26
    mc "*Chuckles* Seriously, though, you nailed it."
    mc "Can you see anything with that blindfold, though?"
    play sound2 clothes3
    show df 28
    p "*Removing the blindfold* Yeah, I can."with dis12
    p "Although I'd rather not be wearing it all the time. I have to keep it on while taking pictures, though!"
    play sound clothes4
    show df 30
    mc "For sure! Idriel wouldn’t be Idriel without her blindfold."with dis12
    show df 31
    p "Well... now tell me, what are you supposed to be?" with dis
    show df 32
    mc "Ah... I'm Eros! The Greek god of love and desire."with dis08
    show df 31
    p "Oh my..."
    p "God of love and desire, huh? Are you planning to enchant anyone with your bow tonight?"
    show df 32
    mc "We'll see, we'll see..."
    mc "I've gotta be careful, with great power comes great responsibility."
    show df 31
    p "Of course..."
    show df 29
    p "Isn't Eros supposed to have wings, though?"with dis12
    show df 30
    mc "Yeah... but they weren't included with the costume."
    mc "*Chuckles* Don't expose me though! Not everyone is an expert on mythology like you."
    show df 29
    p "Nah, I'm no expert."
    p "Wings, a bow, son of Aphrodite and Ares, and husband of Psyche. That's all I know."
    show df 30
    mc "Curious that you mentioned that, that's how I got the idea."
    mc "Someone at that dinner where I met the Founder told me about Psyche, and that made me think about it as a costume."
    show df 33
    play sound clothes3
    p "*Putting her blindfold back on* Well, I can tell it was a great idea, Eros." with dis12
    p "You look great!"
    show df 34
    mc "Thank you!"
    show df 33
    p "It's too bad I couldn't dress up as Psyche."
    p "You know... so we could match."
    show df 34
    mct "Oh boy... She’s really laying the flirt on tonight... If she's trying to provoke me, she's definitely succeeding."
    mc "Yeah, that's too bad..."
    mc "Maybe next year?"
    show df 33
    p "For sure. Maybe next year."
    p "Shall we go... Eros?"
    show df 34
    mc "With pleasure... Idriel."
    stop music fadeout 5
    if novapath:
        show black
        show screen afewminuteslater
        with dis2
        pause
        hide screen afewminuteslater
        play soundloop rivernight fadein 5
        scene df 35
        with dis25
        mc "Alright, here we are!" with dis08
        mc "This is the place, isn't it?"
        show df 36
        p "Yep." with dis
        p "Nova sent me a message a few minutes ago saying she was on her way."
        show df 35
        mc "Yeah, me too." with dis08
        mc "She must be about to arrive, then."
        mc "Is the uni building far from here?"
        show df 36
        p "Nope, just a 7 or 8-minute walk."with dis08
        p "It's right behind those apartments."
        show df 35
        mc "Are all those student flats?"with dis08
        p "Yeah! All the students from outside Kredon have to live there."
        mc "That's where I'll be living next year if I can get into this college, I guess."
        p "*Chuckles* Don’t be silly! You're staying with us until we say so. No escaping the Carters!"
        mc "*Chuckles* I was hoping you'd say that, not gonna lie."
        play sound6 risinglong
        show screen scopenova
        show dfs1
        with dis2
        pause
        play sound zoomin
        scene dfs2
        pause
        play sound scopezooms
        scene dfs3
        pause 8.2
        scene df 38
        hide screen scopenova
        play sound6 pop
        stop sound
        mc "Ouch." with hpunch
        show df 39
        mct "What the hell was that?" with dis14
        mct "Did someone throw a ball at me?"
        play music2 quirky6 fadein 6
        stop soundloop fadeout 11
        show df 40 with dis15
        mc "*Turning around* What the fuck..." with dis
        mc "I'm sorry, can I help yo–"
        mc "Wait a second..."
        $ unlock_look("nova", 7)
        show df 41
        mc "Nova?!" with hpunch
        show df 42
        no "Bang!" with dis
        no "Headshot!"
        show df 43
        mc "Holy shit, that's really you!" with dis15
        no "TA-DA!"
        mc "Wow, you look unrecognizable!"
        mc "You nailed your costume!"
        mc "Damn, I don't think I’d be able to tell it was you if it wasn’t for your eyes."
        show df 44
        p "WOW! We bought the outfit together, but I hadn't seen her with her hair done yet..."
        p "Nova, you look incredible!"
        show df 45
        no "*Giggles* Thank you, thank you!" with dis
        p "This costume was made for you!"
        no "*Giggles* Thank you!"
        mc "*Laughs* You look so different, but your reaction to praise gives you away, Nova."
        show df 46
        no "You look great too, guys!" with dis
        show df 47
        mc "Thanks!"
        if mc == "Orion":
            show df 46
            no "Are you supposed to be “Orion”, [mc]? The Greek huntsman hero?"
            show df 47
            mc "No! I'm..."
            mc "Wait, Orion was so much better."
            mct "What the hell, why didn't I think of that...?"
            mc "Um..."
            mc "Well, I'm supposed to be Eros."
        else:
            mc "I'm supposed to be Eros."
        show df 46b
        no "Who...?"
        show df 47
        mc "Greek god. Son of Aphrodite and Ares, super cool god."
        show df 46b
        no "Uh... okay, if you say so."
        show df 47
        mc "Uh... he has a bow too. Go on, tell her Penny!"
        p "He’s Cupid, Nova."
        show df 46b
        no "What? But I thought Cupid was just a fat baby with wings and some arrows?"
        show df 47
        p "Yeah... but that wouldn’t give [mc] an excuse to dress up as a hot, half-naked model, eh?"
        show df 46
        no "Ah, I understand it now!"
        show df 47
        mc "*Laughs* Whatever, it's just something I bought online. Yours look much more elaborate!"
        show df 48
        no "Thanks! I've always loved Jinx and I've been wanting to cosplay her for a while."with dis
        no "But I never had any... party or event where I got the chance to do so."
        no "...until now!"
        show df 47
        mc "Where did you buy it? Or is it handmade?"with Dissolve(.9)
        show df 48
        no "Bit of both. Penny and my mom helped me with everything." with Dissolve(.9)
        no "I tried to be as accurate as possible!"
        no "I even dyed my hair with a special blue powder. It should disappear after washing it with shampoo."
        show df 47
        mc "What about your eye, though?" with Dissolve(.9)
        show df 49
        no "It's okay, I've got it under control." with dis
        no "The sun has already set, and since I've had it covered for two days straight, I should be able to hold out for 5 or 6 hours, which is the time we'll be there... more or less."
        show df 50
        no "Worst case scenario, I have an eye patch in case it starts hurting me. See?" with dis
        mc "Hmm... well, okay, okay, just make sure not to push it, okay?"
        show df 46
        no "For sure! Don't worry."with dis
        show df 47
        mc "Alright, girls..."
        mc "Now that everyone is here..."
        mc "Let's party!"
        show df 51
        no "Hell yeah!" with dis08
        show df 51b
        p "Can you take a pic of us before going in, [mc]?" with dis12
        p "I haven't posted anything today yet."
        mc "Sure!"
        no "W-What? Am I gonna be on your Instagram profile?"
        no "With you?"
        p "Yeah!"
        no "Oh my god."
        mc "Come on, Nova, look at the camera! Or we're gonna miss the good stuff!"
        no "Y-Yeah!"
    stop music2 fadeout 5
    show black
    show screen afewminuteslater
    with dis22
    pause
    hide screen afewminuteslater
    $ renpy.music.set_volume(0.0, channel='music3')
    play soundloop partywalla fadein 6
    play music2b partypenny fadein 6
    play music3 partyfar
    scene df 51bb
    with Dissolve(2.8)
    mc "I'm finally here!" with dis08
    mc "A college party, baby!" with hpunch
    show df 52
    mc "And before I’ve attended a single class!"with dis14
    p "*Chuckles* You're too excited, [mc]."
    p "If you think this is going to be like American Pie, you'll be disappointed."
    mc "Hey, there's a passed out Power Ranger next to a bottle of vodka by the entrance. That's promising."
    p "*Laughs* Fair enough."
    show df 58
    mc "In any case, I'm sure it'll be fun."with dis08
    if novapath:
        mc "I mean, as long as you two are here, I can't ask for more!"
    else:
        mc "I mean, as long as you're here, I can't ask for more!"
    show df 57
    p "The music's very loud, isn't it?"
    show df 58
    mc "That's one of the advantages of having a building with no neighbors, I guess."
    mc "Nobody can complain!"
    if novapath:
        show df 59
        no "And they do this every year? It looks amazing."
        mc "Is it the first time you’ve come, Nova?"
        no "Yeah..."
        show df 57
        p "They do it every year for Halloween, yeah."
        show df 59
        no "Cool..."
        no "Yesterday this place looked nothing like this."
        no "Everything seems much more... boring on a normal day."
    show df 60
    p "Alright... I think I see Judith at the counter. You should ask her before going in, she's the main organizer for all the events." with dis12
    mc "On it!"
label collegeparty1:
    hide screen heart
    if ppp10:
        scene dpp 1 with dis12
        call screen collegeparty1 with dis06
    scene df 52
    with dis12
    call screen collegeparty1 with dis06
label judithparty:
    if ppp1:
        $ ppp1 = False
        if novapath:
            scene df 61
            show screen heart
            with dis15
            bla "You approach the counter and wait for the girl to notice you." with dis06
            p "[mc] looks pretty good in his costume too, don't you think?"
            no "Yeah!"
            show df 63
            p "It makes him look very fit." with dis
            show df 62
            no "I thought the same thing!"
            show df 63
            p "Yeah..."
            p "You know..."
            p "*Giggles* Can I tell you a secret, Nova?"
            show df 62
            no "O-Of course! My mind is a steel trap."
            show df 63
            p "But you've gotta promise me you won't tell anyone."
            show df 62
            no "I'd never! My lips are sealed."
            show df 63
            p "Okay..."
            play sound clothes2
            play sound2 hit volume 2
            show df 64
            p "*Giggles* I..."with dis06
            p "I think... I might have a little crush on [mc]."
            show df 65
            no "Y-You... what?!"
            show df 64
            p "Isn't it crazy?!"
            p "I've never been attracted to guys younger than me, but I don't know... he's really cute!"
            show df 65
            no "U-Uh... a-are you sure?"
            show df 64
            p "I think so!"
            p "I thought it was just a temporary thing, but... shit, I don't know anymore."
            if pennyshower:
                p "I mean, I saw him naked in the shower earlier today and holy fuck, girl."
                p "You have no idea how much that turned me on..."
                show df 65
                no "N-Naked?"
            show df 64
            p "*Giggles* I feel like I'm 15 again!"
            p "But he might not be into me like that so... keep it secret!"
            show df 65
            no "O-Of course!"
            show df 64
            p "I just needed to tell this to someone so much!"
            p "It feels great to have a bestie I can tell stuff like this to."
            p "But anyway, let's link back up with him."
            p "*Giggles* He'll probably think we're conspiring together or something."
            show df 65
            no "Y-yeah, and we're not."
            show df 66 with dis17
            no ". . ." with dissolve
            no "(Oh my god.)"
            no "(Penelope told me a secret.)"
            no "(A BIG one!)"
            show df 67
            no "*Giggles* (And she called me her “bestie”!)" with dis04
            no "(I'm the confidant of the most popular girl in college.)"
            no "(Me!)"
            show df 66
            no "(But holy shit, did she say she has a crush on [mc] too?!)"with dis04
            no "(That's...)"
            show df 68
            no "(Wait... “too”?)"with dis04
            no "(I don't have a crush on [mc].)"
            no "(Yeah, he's cute, he's funny, he likes what I like, he has a great body, he’s super kind, he's a badass in Eternum...)"
            if not novadrawinglook:
                no "(And... well, did I spend more than a week drawing a manga for him? Yes, I did, okay.)"
            no "(But that doesn't mean anything. We're just friends.)"
            no "(Friends.)"
            no "(Do I like being with him? I mean, yeah, sure.)"
            no "(Was what happened in the Egyptian server kinda hot when it should have been scary? Maybe.)"
            no "(Do I think of him when I'm alone? Yeah, sometimes. A lot of times. Most of the time.)"
            no "(BUT, would I like to have something with him?)"
            no ". . ."
            show df 66
            no "(Oh my god, I WOULD.)"with dis04
            no "(I have a crush on [mc].)"
            no "(When did this happen?!)"with hpunch
            no "(What am I supposed to do now?!)"
            show df 68
            no "(Okay, there's no need to panic, Nova. Just act as suave as usual.)" with dis04
            no "(Nothing happened. So what if my new bestie Penny and I have a crush on the same boy?)"
            mc "NOVA!!!"
            play sound pop
            show df 69b
            no "I KNOW N-NOTHING I SWEAR SHE DIDN'T TELL ME ANYTHING IT'S A SECRET I CAN'T TELL!" with hpunch
            mc "What?"
            no ". . ."
            show df 69
            no "Erm... I mean, y-yeah, sure, I'm coming!" with dis
            no "S-Sorry, I was distracted."
        scene df 70 with dis15
        jud "Oh, and tell Costa that the pool is closed!" with dissolve
        jud "I can't have a rerun of last year!"
        mc "Hi there!"
        show df 71
        jud "Oh, hi." with dis12
        jud "Welcome to the University of Kredon's Annual Halloween Party."
        show df 72
        mc "Thanks! Can we go in?"
        show df 71
        jud "Of course, after paying the $49 fee."
        show df 72
        mc "What?! Really?"
        mc "I thought it was free."
        show df 73
        jud "It is, for college students." with dis08
        jud "But as you can imagine, we can't let every random dude from the town come scrounging."
        jud "It's an open bar, and there’s free food."
        jud "Charging $49 is little less than an outright gift."
        show df 74
        mc "Agh, I guess you're right."
        show df 75
        jud "And speaking of college students, it's so nice to see you here, Penelope."with dis
        jud "You look spectacular!"
        show df 76
        p "Thank you, Judith!"
        p "You know I wouldn't miss a party organized by you."
        jud "Ah, you’re too kind!"
        p "I'll pay the fee too. I know how much work it involves every year."
        show df 75
        jud "Nonsense."
        jud "You don't have to pay a cent. You're the star of this show!"
        show df 76
        p "*Chuckles* I wouldn't say that, but alright, thank you so much!"
        show df 75
        jud "You're very welcome."
        show df 73
        jud "You have to pay, though."with dis
        jud "We accept dollars and eternals. Wallet number E-0XA5096F333."
        show df 85
        show screen eternals
        with dis12
        play sound coins
        $ money -= 16
        pause .05
        $ money -= 16
        pause .05
        $ money -= 17
        pause .05
        mc "Okay, okay..."with dis06
        if money < 0:
            mct "Fuck, my account is overdrawn. If I don't solve this soon, Ulysses will deny me access to Eternum."
            mct "I've gotta be careful."
        else:
            mc "I just sent you the money. I hope it's worth it!"
        jud "Hmm..."
        show df 71
        hide screen eternals
        jud "Got it. Thank you for your contribution." with dis
        jud "Enjoy the party!"
        show df 72
        mc "I plan to!"
        if novapath:
            show df 77
            jud "And now you, baby." with dis08
            jud "Pony up."
            show df 78
            no "*Giggles* I understand the confusion, I guess I do look pretty much unrecognizable."
            no "I'm Nova!"
            show df 80
            jud ". . ."
            show df 79
            no ". . ."
            show df 78
            no "...Nova Johnson."with dissolve
            show df 80
            jud ". . ."
            show df 77
            jud "Uh... it doesn't ring a bell."with dissolve
            show df 81
            no "Why the hell does no one ever remember me?!"
            no "I'm a natural ginger. Long, curly hair. I wear an eye patch during the day!"
            show df 80
            jud ". . ."
            show df 77
            jud "Are you over 18?"with dissolve
            show df 81
            no "Oh, come on, Judith, we're taking 3 classes together!"
            show df 80
            jud ". . ."
            show df 82
            no ". . ."
            show df 83
            no "...I'm the one who slipped and fell down in the cafeteria 4 days ago." with dis
            show df 80
            jud ". . ."
            show df 84
            jud "*Laughs* AAAAH! I remember you!"with dis
            jud "*Laughs* All your pencils flew away and the cupcake landed on top of your laptop! That was hysterical!"
            show df 83
            no "That is one seriously selective memory."
            show df 71
            jud "*Laughs* Okay, okay, you can all pass. Enjoy the party, guys." with dis
            show df 72
            mc "*Chuckles* Thanks."
        show df 86
        p "Alright, we're all set!" with dis
        p "You ready?"
        show df 87
        mc "Absolutely!"
        show df 86
        p "Follow me! I want to introduce you to Lily and Marco."
        p "They're my friends from journalism class."
        show df 87
        mc "Sure thing!"
        if novapath:
            show df 88
            no "Ah, YEAH! I want to introduce you to all my friends too, [mc]." with dis08
            show df 89
            no "There's... eh..."with dis
            no "John..."
            show df 90
            no "Um..."with dissolve
            no "Nobara..."
            show df 91
            no "Uh... Annie..."with dissolve
            mc "Annie? Our Annie?"
            show df 88
            no "No, not our Annie. Another one. Annie... Summers. Annie Summers."with dis
            mc "Can't wait to meet them all!"
            no "W-Well, we'll see. Maybe they didn't come."
            no "They're not party people."
            mc "*Chuckles* I see."
        show df 93
        stu "Oh my GOD!" with dis12
        stu "Your Idriel costume is amazing, Penelope!"
        p "Oh, thank you!"
        stu "And look at those giant bags of milk! They're magnificent!"
        p "Um..."
        mc "What?"
        p "Thanks, I guess?"
        stu "Can I take a photo of you?"
        p "Sure, no prob-"
        play sound2 clothes1 volume 1.6
        show df 94
        stu "*Grabbing her* SHE SAID YES!" with hpunch
        stu "Come with me!" with hpunch
        p "W-What?!"
        stu "There's no good lighting here!"
        p "[mc]! H-Help! SAVE MEEE!"
        show df 95
        bla "The girl drags Penelope away." with dis
        mc "W-What the hell just happened?"
        if novapath:
            no "WHAT?!" with hpunch
            show df 96
            no "A brand new Intel Xeon Dragon X?"with dis
            stu2 "Yeah, so they said."
            no "And I just have to win a game?"
            stu2 "Yep, in pairs."
            stu2 "But if you're interested, you should join ASAP. I think there's only one spot left to participate."
            stu2 "Turn left and go to the cafeteria, then ask for Akira-san."
            no "O-Okay, thank you!"
            show df 97
            no "Did you hear that, [mc]?! A brand new Intel Xeon Dragon X!"with dis
            show df 98
            mc "A what?"
            show df 97
            no "The best CPU on the market! That thing alone costs more than $4000!"
            show df 98
            mc "Holy shit. That's even more than a neural implant."
            show df 97
            no "Do you know the things I could do with one of those, [mc]?!"
            no "I NEED it!"with hpunch
            show df 98
            mc "And they're giving it away?"
            show df 97
            no "It's the prize for winning a game!"
            no "In pairs!"
            no "You've gotta help me!"
            show df 98
            mc "You can count on me!"
            mc "Although, maybe we're late. That guy said they-"
            show df 99
            no "FUCK NO!" with hpunch
            no "This game is the reason I’m here tonight! It’s my destiny!"
            no "We can't lose!"with hpunch
            mc "B-But you didn't even know about it 3 minutes ag-"
            no "I'll run to get a spot! I'll wait for you there!"
            mc "B-But-"
            play sound run
            show df 100
            bla "Nova starts running and disappears into the crowd."with dis
            mc "What the hell is happening...?"
        show df 84
        jud "*Laughs* They've left you all alone." with dis
        mc "Very funny..."
        mc "I’m happy my predicament is at least giving someone pleasure."
        show df 71
        jud "It seems like you’ll be in for a fun night!"with dis08
        show df 72
        mc "You have no idea."
        show df 71
        jud "Alright, grab a drink and have some fun. If you need any directions, I'll be here."
        show df 72
        mc "Thanks!"
        show df 52 with dis15
        mct "Okay, so..."with dissolve
        if novapath:
            mct "Nova to the left, Penelope to the right."
            mct "Hmm."
        else:
            mct "That crazy girl took Penelope to the right."
        mct "This promises to be a bumpy night."
        mct "I should grab a drink..."
        mod "Go right twice (bucket scene)."
        hide screen heart
        call screen collegeparty1 with dis12
label collegeparty2:
    if ppp1:
        mc "I should ask at the counter before going anywhere."with dissolve
        call screen collegeparty1 with dis06
    scene df 53 with dis12
    call screen collegeparty2 with dis06
label collegeparty3:
    if not novapath:
        scene dp 0 with dis12
        mct "Hmm, I've seen a lot of people cosplaying anime characters."with dis08
        mct "Nova would have enjoyed this..."
        call screen collegeparty3b with dis06
    if ppp8 or ppp10:
        scene dp 0 with dis12
        if (novadildo or holdondildo) and ppp10:
            mct "Hmm, Nova isn't back yet." with dis08
            mct "I guess she must be with Akira getting the prize."
        call screen collegeparty3 with dis06
    if ppp5 or ppp6 or ppp7:
        scene df 54b with dis12
        call screen collegeparty3 with dis06
    scene df 54 with dis12
    call screen collegeparty3 with dis06
label novagameparty:
    if ppp7:
        jump novagame2
    if ppp2:
        $ ppp2 = False
        show df 101
        show screen heart
        with dis15
        no "Of course I study here! Computer Science!"with dis06
        mc "Sup!"
        show df 102
        no "Ah! Hi [mc]!" with dis08
        no "This is my partner for the game!"
        show df 103
        mc "Hi! You must be Akira." with dis
        show df 105
        sir "Akira-san to you!"with dis08
        sir "You've gotta show some respect, boy."
        show df 103
        mc "Um... that's gonna be kind of a challenge given that you're not even wearing pants, but sure... Akira-san."with dis08
        mc "I heard you're running a game."
        show df 104
        sir "That's correct."
        show df 105
        sir "And the prize is no small reward! An almost brand new Intel Xeon Dragon X, the best CPU on the market."with dis08
        show df 103
        mc "Why are you giving it away?"with dis08
        show df 104
        sir "I'm a robotics and hardware engineer. I created my own processing unit, faster and better than any other in the world."
        sir "So I decided to give away my old CPU, since it's of no use to me anymore."
        show df 103
        mc "Wow, that's actually very generous of you."
        show df 104
        sir "It's not about generosity."
        show df 105
        sir "The winners must prove their value! Only a truly worthy pair deserves the victory." with dis08
        sir "A piece of hardware like this must be in the hands of outstanding students."
        show df 103
        mc "That would be us!" with dis08
        no "We're super worthy!"
        show df 104
        sir "You'll have to prove that..."
        sir "You must answer a question before I allow you to participate. You know, as a filter."
        show df 103
        mc "Shoot."
        show df 104
        sir "Straight to the point, eh...? I like it."
        sir "Alright..."
        sir "What is packaging a microprocessor, and what are the different types of packaging available?"
        show df 103
        mc "Uhhh..."
        mct "Fuck."
        mc "That's when you package the..."
        show df 110
        no "Packaging is the process of connecting a microprocessor with a computer's motherboard. The types of microprocessor packaging are PGA, SPGA, SECC, and LGA."with dis08
        mc "Ah, that's just what I was about to say!"
        show df 111
        sir "Well, well, well..."with dis
        sir "Finally, someone who knows what she’s talking about."
        sir "Very well, girl!"
        sir "Haskel, Dolores, you have your rivals!"
        show df 112
        has "I was kind of hoping to get that CPU without playing the game, but beating you will be even better."with dis
        show df 113
        mc "Nice to meet you. There are no other contestants?"
        show df 114
        dol "They tried, but no one passed Akira's filter."
        dol "It was funny seeing them get all of his questions wrong."
        show df 113
        mc "Well, I'm sorry to spoil the party, but you'll have no luck tonight. We're taking that CPU home."
        mc "Right, Nova?"
        show df 109
        no "Hell yeah!"with dis08
        show df 112
        has "We'll see about that."with dis08
        has "There's no way on earth we're losing to two freshman rookies."
        show df 113
        no "What do you mean, freshman? I'm in my third year!"
        mc "Hah! We'll make you eat your words."
        show df 105
        sir "The game is simple. 90 minutes. 5 challenges."with dis08
        show df 104
        sir "You'll be competing against Haskel and Dolores. The team with the most points after completing all 5 challenges is the winner!"with dis08
        show df 103
        mc "Got it!"
        show df 104
        sir "Are you ready to begin?"
        show df 103
        menu:
            with dis
            "Ready":
                mc "We're ready!" with dissolve
                jump novagame1
            "Not yet":
                $ ppp3 = True
                mc "Not yet. I want to have a look around first." with dissolve
                show df 104
                sir "I'll be here."
                sir "Just don't rest on your laurels. I can't save your spot forever."
                show df 103
                mc "Gotcha."
                show df 106
                no "Whaaaat?" with dis
                show df 107
                mc "I just want to go and check on Penny."
                mc "I'll tell her we're here, so she doesn't worry."
                show df 106
                no "Oh... okay."
                no "But don't take too long, please!"
                no "There's only one spot left!"
                show df 107
                mc "I won't, I promise! I'll be right back."
                hide screen heart
                scene df 54
                with dis15
                call screen collegeparty3 with dis06
    if ppp3:
        show df 104
        show screen heart
        with dis15
        sir "Welcome back!" with dissolve
        sir "Are you ready to begin?"
        show df 103
        menu:
            with dis
            "Ready":
                mc "We're ready!" with dissolve
                jump novagame1
            "Not yet":
                $ ppp3 = True
                mc "Not yet." with dissolve
                show df 104
                sir "I'll be here."
                scene df 54
                hide screen heart
                with dis15
                call screen collegeparty3 with dis06
label novagame1:
    show df 104
    sir "Excellent."
    sir "Let's get started, then!"
    show df 115
    sir "This is our first challenge, ladies and gentlemen." with dis
    sir "I like to call it..."
    play sound ding volume 1.4
    scene df115
    sir "{i}The drinking."
    scene df 110
    no "What do we have to do?"
    show df 115
    sir "Simple. The team who can drink more beer in 10 minutes gets the point!"
    show df 103
    mc "*Chuckles* Really? I thought your “challenges” would be more... computer-related."with dis08
    show df 104
    sir "There are two things I know something about in this life, [mc]. Computers and parties."
    sir "My winner must demonstrate being the king of both!"
    show df 112
    has "Scared of a little drinking, [mc]? You need to be home before 12?" with dis
    show df 113
    mc "Shut up, horseface! I'll knock you out!"
    show df 108
    mc "Alright, how are your drinking skills, Nova?"with dis
    show df 106
    no "Uhh... they're probably not the best. I never drink."
    show df 108
    mc "Okay... well, don't worry."
    mc "I got you."
    mc "Just do what you can. Me and my fast metabolism will do the rest."
    mc "We're winning this!"
    show df 109
    no "Hell yes!"with dis08
    no "Thank you for helping me, [mc]."
    mc "Hey, a game where I get to drink free beer? I'd do this every week!"
    mc "Now let's show them who they're dealing with!"
    no "YEAH!" with hpunch
    play sound ding
    stop soundloop
    stop music2b
    show black
    show screen afewminuteslater
    pause
    play soundloop partywalla fadein 6
    play music2b partypenny fadein 6
    play music3 partyfar
    scene df 116
    hide screen afewminuteslater
    with dis2
    no "Oof..." with dis08
    play sound2 hiccupg volume 1.5
    no "*Hiccup* Hic!"with vpunch
    no "I'm really, really drunk, [mc]."
    no "I'm not sure I can... d-drink anymore."
    play sound whoosh6
    scene df117
    mc "W-What are you talking about?" with Dissolve(0.1)
    mc "You didn't even finish your first one!"
    scene df 118
    no "But I w-weigh like 100 pounds!"with dis04
    no "I can't-"
    play sound2 hiccupg volume 1.5
    show df 118b
    no "*Hiccup* Hic!"with vpunch
    show df 118
    no "I don't have your t-tolerance!"with dissolve
    no "With all your height, and your muscles, and your big... arms... and..."
    play sound2 hiccupg volume 1.5
    show df 118b
    no "*Hiccup* Hic!"with vpunch
    show df 118
    no "And legs..."with dissolve
    show df 117
    mc "I think we're..."with dis06
    play sound2 hiccupb
    mc "*Hiccup* Hic!"with vpunch
    mc "...we're fucked."
    mc "D-Dammit, now you've given me hiccups too."
    show df 119
    has "Do you surrender? There's only 1 minute left and we're 2 beers ahead."
    mc "N-No way!"
    mc "I can drink more!"
    play sound6 swallow
    show df 121
    bla "You finish your 5th beer in less than 10 minutes." with dis
    play sound bottlesetdown
    show df 120 with dis12
    mct "God, the worst part is having to drink them all so fast." with dis08
    mct "And I'd never seen this beer, but I'm pretty sure it has a higher amount of alcohol than usual."
    mct "Maybe I shouldn't drink anymore if I don't want to end the night early."
    mct "But I don't want to let Nova down either..."
    menu:
        with dis
        "Drink another one":
            play sound3 swallow
            show df 121
            mc "*Drinking another one* (Bah, fuck it.)" with dis
            play sound bottlesetdown
            show df 120
            mct "Six!" with dis12
            mct "And I'm fine!"
            mct "Better than fine."
            mct "I've never been finer."
            show df 122
            mct "Hey..." with dis12
            mct "Who's spinning the table...?"
            play sound fallbottle
            play sound2 fall volume 2
            show df 123
            stop soundloop fadeout 4
            $ renpy.music.set_volume(0.7, delay=4.0, channel='music3')
            $ renpy.music.set_volume(0.0, delay=4.0, channel='music2b')
            bla "You fall to the ground like a cut down tree." with dis08
            no "[mc]!"
            show black with dis2
            pause
            mc "MMmMm..."with dissolve
            no "[mc]!"
            $ renpy.music.set_volume(0.0, delay=4.0, channel='music3')
            $ renpy.music.set_volume(0.5, delay=4.0, channel='music2b')
            scene df 130
            mc "Hmm..." with dis2
            mc "Oh shit, what happened?"
            show df 131 with dis12
            mc "Nova?" with dis06
            mc "Oh fuck, did I pass out?"
            show df 132
            no "Yeah... you've been sleeping for the past 30 minutes."
            no "Those two bastards won the CPU..."
            show df 131
            mc "Oh... really?! Fuck, I'm sorry, Nova."
            show df 132
            no "Don't worry, it was my fault. It's me who couldn't even drink one-"
            play sound swallow
            show df 133
            no "*Gagging* Hmm!"with dis04
            mc "Are you okay?"
            show df 132
            no "Y-Yeah, I just need to go to the bathroom."with dis06
            no "It's just that anxiety makes me want to throw up. And combined with alcohol, even more."
            no "And when I saw you falling I worried and..."
            play sound swallow
            show df 133
            no "*Gagging* Hmm!"with dis04
            play sound2 run
            show df 134
            bla "Nova runs out of the cafeteria." with dis15
            mct "Man, I'm sorry for her. What a mess."
            mct "I wonder what other challenges Akira prepared..."
            mct "Well, I can't go back in time. What's done is done."
            mct "Let's go see what Penelope is doing..."
            $ ppp5 = True
            $ ppp3 = False
            scene df 54b
            hide screen heart
            with dis15
            call screen collegeparty3 with dis06
        "[gr]Stop here":
            mc ". . ."with dissolve
            dol "Are you gonna drink or not?"
            mc ". . ."
            show df 117
            mc "...Maybe not."with dis
            mc "We should stop here, Nova."
            mc "Think about it, if we're not drunk, we'll do better in the other challenges."
            show df 118
            no "Ahhh! Very cle-"with dis04
            play sound2 hiccupg volume 1.5
            show df 118b
            no "*Hiccup* Hic!"with vpunch
            show df 118
            no "Very clever!"with dissolve
            show df 124
            sir "That settles it, then!" with dis12
            sir "Haskel and Dolores win the first point!"
            show df 119
            has "Piece of cake!"
            show df 118
            no "We're just giving them a free head start."
            show df 124
            sir "Alright guys, it is time for our second challenge!"
            sir "I call it..."
            play sound ding volume 1.4
            show df124
            sir "{i}The hunt."
            scene df 118
            no "What are we hunting?"
            show df 124
            sir "Simple. The team who can bring me the bra with a larger cup size, wins!"
            mc "A bra?"
            show df 118
            no "And what are you going to do with it, you old pervert?"
            show df 124
            sir "Nothing. It's just for science!"
            sir "You have another 10 minutes. The time starts... now!"
            play sound chairmove
            show df 125
            dol "*Standing up* Can we give you our own? Is that allowed?" with dis12
            show df 124
            sir "Good question, my lovely Dolores."
            sir "Yes, it is allowed."
            sir "Just remember, the biggest one when the time runs out gets the point!"
            show df 126
            dol "*Giggles* I see."
            dol "*Giggles* In that case we start with a great advantage."
            show df 127 with dis12
            no "Huh? What do you mean by t...?"with dis
            show df 128
            no ". . ." with dis12
            show df 129
            no "Grrr..." with dis14
            no "{bt=2}“In tHaT cAsE wE sTaRt wIth a gReaT aDvAnTagE...”{/bt}"
            no "Ha, ha."
            show df 108
            mc "Don't worry, Nova, we got this!" with dis15
            mc "We have an unbeatable trump card to play here."
            show df 109
            no "We have to find Penny!" with dis
            mc "Yes!"
            mc "I'll go get her!"
            mc "Do you have a plan B? She wasn't wearing a bra because of her costume, so maybe she doesn't have one here."
            mc "I mean... I-I think so. I'm not sure. I didn't look that closely."
            show df 110
            no "Oh, I did! She wasn't wearing a bra."with dis
            no "The only thing holding her big boobas was the net of Idriel's dress."
            no "I'll go ask around in case she doesn't have one here."
            mc "Okay! I'll see you back here in 10 minutes!"
            show df 109
            no "Gotcha! Good luck!"with dis08
            $ ppp6 = True
            $ ppp3 = False
            mod "Go to the right hallway and locker room on the left - talk with Penny."
            scene df 54b
            hide screen heart
            with dis15
            call screen collegeparty3 with dis06
label novagame2:
    $ ppp7 = False
    show df 104
    show screen heart
    sir "Ah, [mc]! Just in time." with dis12
    show df 106
    no "I couldn't find anything, I'm sorry."with dis
    no "What about you? Any luck?"
    show df 107
    mc "Yes! I got it!"
    show df 109
    no "Ah, sweet!"with dis08
    no "I knew Penny wouldn't let us down!"
    show df 111
    sir "Okay gentlemen... show me your hunt."with dis
    show df 110
    no "All yours."
    play sound clothes3
    show df 147
    bla "You hand Penelope's bra to Akira." with dis12
    sir "MY GOD..."
    sir "Enormous cup size, but a small band."
    sir "The girl wearing this was slim, but with huge boobs. No cheating here."
    sir "What a magnificent piece."
    sir "Can I keep it?"
    mc "No."
    sir "Agh, that's too bad..."
    sir "Well, in any case... [mc] and Nova win the second challenge!"
    show df 148
    dol "Really? Where the fuck did you find that?"with dis
    no "*Giggles* A magician never explains his tricks."
    dol "Bah."
    show df 124
    sir "This is getting interesting, guys. You're tied!"with dis
    sir "And now... it is time for the third challenge of the night!"
    sir "This is..."
    play sound ding volume 1.4
    stop music3
    stop music2b
    show df124
    sir "{i}The polygraph."
    play sound4 chairmove
    play sound5 chair2
    play music2 polygraph fadein 3
    scene df 149
    sir "Please, sit around the table." with dis17
    sir "This entire challenge revolves around one of my greatest inventions."
    play sound slam
    show df 150
    bla "Akira puts a strange heavy-looking machine on top of the table." with vpunch
    sir "The DK Tron ZLF-9000!"
    show df 151
    no "Not a very commercial name."with dissolve
    show df 156
    sir "It's not the final name."
    show df 155
    sir "But anyway, what matters is that it works!" with dis08
    show df 150
    sir "The DK Tron ZLF-9000 serves the same purpose as any other polygraph, but it doesn't require cables or annoying connections."with dis08
    sir "It is capable of detecting lies just by analyzing your voice!"
    show df 151
    no "Really? Just like that?"with dissolve
    show df 152
    sir "Just like that!" with dis
    sir "See for yourself."
    sir "*Clears throat* The capital of Germany is Toronto."
    pause .1
    play sound error3 volume 0.5
    show df 152b with Dissolve(.15)
    pause .9
    show df 152 with dis
    sir "When you tell a lie, an alarm is triggered and that red bulb lights up." with dissolve
    show df 169
    has "Wow, that's honestly impressive."
    has "It's true what they say about you in the department. You're brilliant."
    show df 152
    sir "Of course, it only works if I'm aware that I'm lying. If I really believed that Toronto is the capital of Germany, the DK Tron wouldn't detect it as a lie."
    mc "And what does the “fog” button do?"
    sir "What?"
    mc "The orange button."
    sir "It produces fog. What else would it do?"
    show df 153b
    mc ". . ." with dis12
    sir ". . ."
    show df 154
    mc "What...?"with dissolve
    show df 153
    sir "It emits a dense vapor that appears similar to smoke."
    show df 154
    mc "B-But why...?"
    show df 153
    sir "Why what?"
    show df 154
    mc "Why the hell does a polygraph have a fog feature?"
    show df 153
    sir "Why not?"
    sir "It creates ambience."
    show df 153b
    mc ". . ."
    sir ". . ."
    show df 153
    sir "If you wanted to buy a polygraph and there was a model that releases fog and another one that doesn't, which one would you buy? Same price."
    show df 153b
    mc ". . ."
    sir ". . ."
    show df 154
    mc "Can I press it?"with dissolve
    show df 153
    sir "No."
    show df 153b
    mc ". . ."
    show df 163
    dol "*Clears throat* Helloooo? Can we start or not?"with dis08
    dol "Can you leave your fog-business conversations for later?"
    show df 155
    sir "Ah, yes, sorry!"with dis08
    sir "The challenge is simple. We just have to hold a conversation for 5 minutes."
    sir "The first team to lie 10 times, loses!"
    show df 151
    no "10 lies? In 5 minutes? Why would anyone do that?"
    show df 155
    sir "Probably no one..."
    sir "...unless you have something to hide."
    show df 151
    no "Uh... I certainly don't."
    show df 155
    sir "You have nothing to worry about, then!"
    sir "We shall begin."
    sir "The time starts..."
    play sound ding
    sir "NOW!"with hpunch
    show df 156
    sir "Tell me, Dolores, how old are you?"with dissolve
    play sound w1 volume 0.6
    show df 163
    dol "I'm 23."with pl
    play sound w1 volume 0.6
    show df 156b
    sir "What are you studying, Haskel?"with pr
    play sound w1 volume 0.6
    show df 169
    has "Engineering. Although... I'm very far from your level."with pr
    has "I usually escape with a “C” minus."
    play sound w1 volume 0.6
    show df 156b
    sir "Do you study here too, [mc]?"with pl
    play sound w1 volume 0.6
    show df 157
    mc "I don't. I'm still in high school, actually. I moved to Kredon a couple of months ago as part of a student exchange program."with pr
    play sound w1 volume 0.6
    show df 156
    sir "When was the last time you masturbated, Nova?"with pl
    play sound w1 volume 0.6
    show df 159
    no "W-Wait, WHAT?"with pl
    no "Why am I the only one who gets asked a lewd question?"
    show df 155
    sir "Just a question like any other."
    sir "Tell me, when was the last time you touched yourself?"
    show df 161
    no "I-I don't remember."
    play sound error3 volume 0.4
    show df 152b
    pause 1.1
    show df 155
    sir "First lie of the night!"with dis08
    show df 159
    no "What?!"
    show df 166
    dol "*Laughs* You {i}do{/i} remember!"
    dol "Come on, don't be such a prude. We're just having fun."
    show df 163
    dol "I'll answer too. I think it was... last Sunday."with dis08
    show df 162
    no "Last time...? Um... t-two days ago."with dis08
    mct "I'm starting to like this game..."
    show df 155
    sir "Were you watching porn?"
    show df 162
    no "Well... y-yeah."
    show df 155
    sir "What kind of porn do you like?"
    show df 159
    no "I-I don't wanna say it!"
    show df 156
    sir "If you don't answer the questions, you lose this challenge!"
    show df 159
    no "What?!"
    show df 161
    no "This wasn't part of the rules."with dissolve
    show df 166
    dol "Whatever, I'll start."
    dol "I like group sex, squirting, and interracial."
    show df 167
    dol "Oh, and lesbian!"with dissolve
    show df 162
    no "I like... um..."
    show df 161
    no "I'm not sure. Normal porn."with dissolve
    play sound error3 volume 0.4
    show df 152b
    pause 1.1
    show df 159b
    no "OKAY, OKAY! JEEZ!"with dis08
    show df 162
    no "It d-depends on the day."with dis
    no "I like role-play videos."
    no "And hentai."
    no "And... porn games."
    show df 166
    dol "Porn games? Like... “Press A to get fucked”?"
    show df 161
    no "Of course not. They're visual novels, but... for adults. With sex. And good stories! You wouldn't understand it."
    show df 166
    dol "It sounds like what I said but with extra steps."
    show df 168
    has "Porn categories, huh? I like big tits, and–"with dis08
    show df 156b
    sir "Shut up Haskel, no one cares."
    show df 155
    sir "So, Nova... no lesbian category, like Dolores?"with dis06
    show df 162
    no "Uhh... not really."
    no "B-But I like threesome videos. Or... group sex."
    no "Like... various girls in the same scene."
    show df 160
    no "D-Does that make me lesbian?" with dissolve
    show df 155
    sir "*Chuckles* I don't know. Have you ever been with a girl?"
    show df 159
    no "No!"
    show df 155
    sir "But if you had to hook up with another girl..."
    sir "Who would it be?"
    show df 159
    no "W-What?"
    show df 162
    no "I-I don't know."with dissolve
    play sound error3 volume 0.4
    show df 152b
    pause 1.2
    show df 159b
    no "I hate this machine!"with dissolve
    show df 162
    no "Uh..."with dis
    no "P-Probably Penelope, I guess."
    no "I've always admired her. And now that we're friends and we share some... interests... I don't know. If I had to do it, it'd be her."
    show df 166
    dol "Penelope? Penelope Carter? That IG model in the journalism program?"
    dol "*Laughs* Please, she doesn't even know you exist."
    show df 161
    no "Of course she does. We're besties!"
    show df 166
    dol "Besties? I follow her Insta and I've never seen you there."
    show df 161
    no "Because she met me not that long ago."
    no "But we play Eternum together!"
    show df 166
    dol "That doesn't mean anything. Have you gone on a trip with her? Do you usually go to lunch together? Have you seen each other naked?"
    show df 161
    no "Actually, I have, smartass!"
    show df 167
    dol "What?!"
    show df 160
    no "I mean, I saw some photos on her laptop when..."
    show df 167
    dol "She lent her personal laptop to you?"
    show df 162
    no "N-Not exactly. I saw them... remotely."
    show df 166
    dol "*Chuckles* What? Are you a hacker or something?"
    show df 160
    no "A-A what? Of course not!"
    play sound error3 volume 0.4
    show df 152b
    pause 1.2
    show df 162
    no "O-Okay, maybe something like that. But I just took a peek!" with dissolve
    show df 160
    no "And I haven't done anything like that in weeks! Not since [mc] made me realize it was wrong!"with dissolve
    no "And I'll never do it again, I swear!"
    show df 169
    has "I'd lend my laptop to my Dolores without hesitation."
    has "I have nothing to hide."
    show df 163
    dol "Yeah, I would too, honey."
    play sound error3 volume 0.4
    show df 152b
    pause 1.2
    show df 164
    dol "O-Okay, maybe not." with dissolve
    dol " But it's a natural reaction. I had some bad experiences with my ex."
    show df 155
    sir "Your ex, huh?"
    sir "How many boys have you been with?"
    show df 163
    dol "Uh... four."
    show df 169
    has "Four? When we started dating you told me I was your third."
    show df 163
    dol "Did I? You must be misremembering it."
    play sound error3 volume 0.4
    show df 152b
    pause 1.2
    show df 169
    has "Huh? What does this mean?" with dissolve
    has "Didn't you tell me I was your third?"
    show df 163
    dol "I didn't."
    play sound error3 volume 0.4
    show df 152b
    pause 1.2
    show df 164
    dol "I mean... when we started dating, I had been with four guys already."
    play sound error3 volume 0.4
    show df 152b
    pause 1.2
    play sound2 slam
    show df 165
    dol "I'll break this fucking piece of junk!"with hpunch
    show df 170
    has "You cheated on me?!"with hpunch
    show df 164
    dol "Of course not, sweetie!"
    play sound error3 volume 0.4
    show df 152b
    pause 1.2
    show df 170
    has "How could you?"
    show df 164
    dol "It was just a kiss!"
    play sound error3 volume 0.4
    show df 152b
    pause 1.2
    play sound2 slam
    show df 165
    dol "O-Okay, this machine is completely broken!"with hpunch
    dol "I-It was little more than a kiss!"
    dol "And why am I the only one answering things?"
    dol "Have YOU ever cheated on your boyfriend?"
    show df 160
    no "Who, me?!"
    no "[mc] and I aren't even dating."
    no "We're just friends."
    show df 156
    sir "What about your other relationships?"
    show df 162
    no "Uh... I mean..."
    no "I've never been in a serious relationship."
    show df 166
    dol "Hah! Really? More of a one-night stand girl, eh?"
    dol "Are your knees skinned from all the head you go around giving?"
    show df 161
    no "What are you talking about? My knees are smooth as hell."
    show df 166
    dol "How many boys have you slept with?"
    show df 162
    no "That's none of your business."
    show df 166
    dol "You have to answer! Akira said so."
    dol "How many?"
    show df 162
    no "Uh... slept with?"
    no "I don't know."
    play sound error3 volume 0.4
    show df 152b
    pause 1.2
    show df 158
    mc "Stop saying you don't know things you do know, Nova! We're gonna lose!"
    show df 160
    no "Okay, okay, sorry!"
    show df 163
    dol "Still waiting..."
    dol "How many guys have you had sex with?"
    show df 160
    no "S-Sex? As in... sex-sex?"
    show df 163
    dol "What kind of question is that? Yes, sex-sex."
    show df 162
    no "Uhh...."
    no "I'm not sure... a few."
    play sound error3 volume 0.4
    show df 152b
    pause 1.2
    show df 167
    dol "What?"
    dol "Wait... are you a virgin?"
    show df 160
    no "No!"
    play sound error3 volume 0.4
    show df 152b
    pause 1.2
    play sound2 slam
    show df 159b
    no "This machine is broken!"with hpunch
    show df 158
    mc "There's nothing wrong with that, Nova."
    show df 159
    no "I-I know, but I'm not!"
    play sound error3 volume 0.4
    show df 152b
    pause 1.2
    play sound3 slam
    show df 159b
    no "SHUT UP!"with hpunch
    show df 167
    dol "Oh my god, you're still a virgin!"
    dol "How old are you?"
    show df 161
    no "Shut up."
    show df 155
    sir "That's cute!"
    sir "You must be looking forward to having someone with whom you can test all your kinky desires."
    show df 161
    no "I'm not."
    play sound error3 volume 0.6
    show df 152b
    pause 1.2
    play sound2 slam
    show df 159b
    no "Can someone turn this shit off?!"with hpunch
    show df 155
    sir "{bt=3}Do you want [mc] to deflower you?{/bt}"
    show df 159
    no "{sc=2}WHAT?{/sc}" with hpunch
    no "{sc=2}NO!{/sc}" with hpunch
    play soundloop2 error3b volume 0.7
    show df152
    pause 2
    stop soundloop2
    scene df 152
    pause 0.01
    play music2b partypenny fadein 6
    play music3 partyfar
    stop music2 fadeout 7
    show df 171
    sir "Ladies and gentlemen... IT'S OVER!" with dis12
    sir "Nova activated the DK Tron 10 times."
    sir "Dolores and Haskel get the point!"
    show df 161
    no "I'm glad this thing is over." with dis
    no "This machine of yours doesn't work, Akira."
    no "What a scam."
    show df 165
    dol "Y-Yeah, I've gotta agree with Nova on that."
    dol "You need to fix it."
    show df 169
    has "For a moment I believed it was legit."
    show df 157
    mc "Um... well, I can't really comment on it, I barely talked."
    show df 156
    sir "You can deceive yourselves all you want, my machines are perfect."
    show df 172
    sir "But anyway..." with dis
    sir "Let's move on to the next challenge!"
    sir "You'll have to follow me to the Auditorium and put on the clothes you'll find by the entrance."
    play sound chairmove
    show df 125
    dol "*Standing up* What for?"with dis12
    show df 172
    sir "You'll see soon enough."with dis
    sir "This is..."
    play sound ding volume 1.4
    show df173
    sir "{i}The other world."
    $ renpy.music.set_volume(0.6, delay=3, channel='music3')
    $ renpy.music.set_volume(0.0, delay=3, channel='music2b')
    stop soundloop fadeout 5
    scene df 174 with dis25
    pause
    no "AAAAH YES!"with dis06
    show df 175
    no "That's more like it!" with dis
    no "Now this is a party I can fit in at!"
    show df 176
    mc "*Chuckles* I'll admit this is the last thing I was expecting to do tonight."with dis12
    mc "Looks like I can't escape from Eternum, no matter how hard I try."
    show df 177
    no "I feel right at home wearing this!"
    no "Not that the Jinx costume is uncomfortable or anything, but there's something about the E-suit... it feels like a second skin!"
    show df 176
    mc "Yep, I've gotta agree on that!"
    show df 178
    dol "Yeah, yeah, I love it too." with dis12
    dol "It really emphasizes the curves of the body."
    dol "*Chuckles* It works better than a pair of leggings! It can make the flattest of butts pop."
    show df 180
    dol "Right, Nova?"
    show df 179
    no "What do you mean “right, Nova”?"
    no "Are you implying that I have a flat butt?"
    no "Because I have a better ass than you."
    show df 180
    dol "*Chuckles* Oh please, you're drunk, girl."
    dol "Don't let alcohol embarrass you."
    show df 179
    no "I'm not..."
    no "Well, I'm a bit drunk, but that doesn't change anything."
    show df 180
    dol "Don't feel bad. Everyone has their qualities."
    dol "I have a great body, and you have... um... that funny glass eye of yours."
    show df 179
    no "*Grunting* It's not made of glass."
    no "And you won't change my mind."
    no "There are literally only three things I'm confident in: my computer skills, my marksmanship, and my butt."
    no "I have a decent butt."
    no "We even used it in a heist! As a distraction!"
    no "I take it back, I have a GREAT butt."
    show df 180
    dol "Is that what your mother tells you?"
    show df 179
    no "Uh..."
    no "Well, yes, but she's telling the truth. She always tells me everything I do wrong. Which is... a lot."
    no "So when she gives me a compliment, I know it's true."
    no "Dalia said so too! And she has the best one I've seen. She said I have good muscle genetics or something like that."
    show df 181
    dol "I have no clue who Dalia is, but fine, let’s let the guys decide, shall we?"with dis14
    mc "Hmm?"
    dol "Who has the best butt? Nova or me?"
    show df 182 with dis12
    no "Fine, whatever you want!" with dis08
    mc "Uhh..."
    mc "Well, I'm not saying this because Nova is my..."
    menu:
        with dis
        "Friend":
            mc "...my friend, but she {i}clearly{/i} has the best ass here."with dissolve
        "Teammate":
            mc "...my teammate, but she {i}clearly{/i} has the best ass here."with dissolve
        "Girl [nova_pts]{#0.5,nova}":
            mc "...my girl, but she {i}clearly{/i} has the best ass here."with dissolve
            $ nova_points += 1
            play sound beat
            show screen heartbeat
    no "Hah! See??"
    dol "Well, duh, what's he supposed to say?"
    dol "Haskel?!"
    has "Um..."
    show df 183
    has "It's obvious that you have the best butt, Dolores."with dis
    has "Clearly."
    has "It's much... better looking."
    show df 184
    mc "*Imitating the sound of Akira's polygraph* Meeeec!"with dis08
    show df 186
    sir "Okay, guys! Please take a seat!"with dis
    sir "I hope no one left their Eternum neural implant at home!"
    show df 186b
    sir "Hahaha!"
    sir "Hah!"
    show df 186
    sir "You get it? Because it can't be taken out!"
    show df 186b
    sir "No?"
    show df 186
    sir "Tough crowd... *clears throat* Okay, sit down!"
    play sound chair1
    show df 187
    no "This one will be the easiest challenge, [mc]."with dis12
    no "Between Dione and your powers, we'll destroy them!"
    show df 186
    sir "I'll send you an invite. Please join the server and wait for further instructions."
    play soundlow login
    play sound2 chair3
    show df 188
    no "*Putting the visor on* Bring it on, Akira." with dis
    no "We're ready!"
    no "Let's kick ass, [mc]!"
    play sound4 chair1
    show df 189
    mc "And here we go again..." with dis12
    play sound ai7
    blank "{i}Connected."with dis
    play sound ai8
    blank "{i}Welcome back to Eternum."
    play sound ai11
    blank "{i}Please prepare to connect..."
    show df189
    stop music3 fadeout 2
    play sound risingshort4
    pause 2
    scene login3 with flash
    pause 8
    play soundlow whoosh4
    scene white with dissolve
    play soundloop2 waves fadein 3
    scene dr 1 with dis27
    $ unlock_look("nova", 8)
    pause
    play soundloop metalbridge
    show dr 2
    mc "*Looking down* Holy cow..."with dis12
    no "Damn!"
    mc "We..."
    play sound2 eagle
    show dr 3
    mc "W-We're hanging 100 meters above the ground!"with dis
    no "*Laughs* This is so cool!"
    mc "Holy shit, slipping here would mean an instant death."
    show dr 5
    no "Can you imagine?" with dis
    no "{i}“Thanatos finds the last Gem of Doom and becomes the new CEO of Ulysses. The previous owner slipped off a crane and cracked his head.”"
    show dr 4
    mc "*Laughs* That's definitely not how I want to be remembered."with dis06
    show dr 6
    mc "*Standing up* Looks like we're in a harbor of some sort."with dis
    mc "But it's just a small island in the middle of nowhere, there's water in all directions."
    mc "Do you have any idea of what this could be?"
    show dr 7
    no "*Standing up* Hmm... I see no other players."with dis
    no "I'd bet it's one of those private servers I've heard about."
    if daliapath:
        mct "Hmm, Akira could have access to a private server just like Dalia, it's very possible. Although, I prefer Dalia's."
        mct "For several reasons..."
    no "Either that, or a Battle Royale server."
    no "Some people love that adrenaline rush, even if it means the possibility of losing everything they have."
    mc "You know, if you chose this outfit to validate your previous statement about your butt... you succeeded."
    mc "You look so sexy in it..."
    show dr 8
    no "*Giggles* Thank you!" with dis
    no "It's my combat outfit. I usually use this one in the servers where guns are allowed."
    mc "Good choice, no doubt."
    play sound metalsqueak
    show dr 9
    bla "Nova leans against the rail and the wind starts waving her curls."with dis14
    mc "*Chuckles* It feels almost weird seeing you with your normal hair again."
    show dr 10
    no "Right? It's crazy how different a person can look just by changing their hairstyle."with dis08
    show dr 9
    mc "You look good with any hair."with dis08
    show dr 11
    no "*Giggles* Thanks."with dis08
    show dr 10
    no "Your outfit is pretty cool, too!"with dis06
    show dr 9
    if anniepath:
        mc "Yeah! I found it in a space server where I played with Annie."with dis08
    else:
        mc "Yeah! Annie found it in a space server she usually plays."with dis08
    show dr 10
    no "Andromeda?"with dis08
    show dr 9
    if anniepath:
        mc "That one! We've gotta go back there and play together sometime."with dis08
    else:
        mc "That one! We've gotta go there and play together sometime."with dis08
    show dr 10
    no "For sure! We could spend our whole lives in that server and we wouldn't be able to discover everything. That server is gigantic."with dis08
    show dr 9
    mc "That sounds amazing."with dis08
    mc "Although all servers in Eternum are amazing, in a sense."
    mc "All of them have something that makes them special."
    mc "I wonder what Akira prepared for us in this one."
    show dr 10
    no "Whatever it is, we have to win!"with dis08
    no "I NEED that CPU!"
    show dr 9
    mc "Is it really that important? The one you have right now isn’t good enough?"with dis08
    show dr 10b
    no "Well... it is, but with better hardware I can do more things. And faster."with dis08
    no "So I'll be able to help you more."
    show dr 9
    mc "You do enough, Nova. We wouldn't even have a Gem of Doom if it wasn't for you."with dis08
    show dr 10b
    no "I know, but... I have to keep getting better."with dis08
    no "I feel like..."
    no "I feel like if I don't contribute something to the team, if I'm not constantly helping you by hacking some network, getting an IP address, or programming some device... I won't be needed anymore."
    no "And I... I don't want to be left out."
    show dr 9
    mct "I didn't know she felt like this."with dis08
    mct "I guess that explains her constant need for validation."
    mc "I hope you realize how stupid that is. We're not gonna shut you out, Nova."
    mc "Especially not me. I love spending time with you."
    show dr 11
    no "*Giggles* Hearing that makes me feel good. Thank you, [mc]."with dis08
    mc "Which doesn't mean that you can stop being my personal hacker, of course! I need the best of the best on my team!"
    stop soundloop fadeout 2
    show dr 10
    no "Oh, I won't let you down, rest assured!" with dis06
    play soundloop drone fadein 3
    show dr 12
    bla "A strange looking drone suddenly approaches you." with dis15
    mc "Oh? What's this?"
    sir "Sorry for the delay!"
    no "That's Akira-san's voice!"
    sir "The challenge is about to begin!"
    show dr 13
    sir "It is very simple. You four are the only players in this harbor of 2 square miles."with dis
    show dr 14
    sir "And each team has spawned on opposite sides of the island."with dis12
    no "Oh... it's true! I can see them."
    mc "Really? Where?"
    no "Right there, on top of that other crane at the end of the harbor."
    mc "*Squinting your eyes* Hmm... that's way too far. How can you see them? I can't see shit."
    sir "You have 30 minutes to eliminate the other team!"
    sir "The last one standing, wins the challenge!"
    show dr 12
    sir "Questions?"with dis12
    mc "Yeah, what happens if we die? Do we lose our level and inventory?"
    sir "You don't! This is a training server, the penalties for dying are not applied here."
    sir "If you win, you'll find an Exit Portal right in the center of the harbor."
    no "Can we use our own weapons?"
    sir "Correct! You can use any kind of weapon in your inventory."
    no "Cool!"
    show dr 15
    dol "Do you see them?"with dis12
    show dr 16
    has "Yeah, I do..."
    has "And I don't think they've spotted us. They don't have binoculars."
    has "We'll skirt those warehouses on the right and we'll take them by surprise on their way here."
    has "They won't see us coming."
    show dr 15
    dol "*Laughs* They're ours!"
    show dr 12
    sir "The countdown has officially begun, challengers."with dis12
    sir "Good luck!"
    stop soundloop fadeout 2
    show dr 17
    bla "The drone flies away from you." with dis15
    mc "Alright, Nova!"
    mc "Let's get to work!"
    mc "30 minutes is a lot of time, but this place is huge."
    mc "Here's my plan: after going down the crane, we split. I'll march forward towards their location through the warehouses. You're gonna climb on those containers and you'll cover me with your sniper."
    mc "At the end, I think it's all coming down to who spots the other team first. We need to exercise caution and watch each other’s backs."
    mc "I'll try to keep a clear line of sight so we can see each other, but whistle really loudly if you need back up!"
    show dr 18
    mc "Thoughts?"with dis
    mc ". . ."
    mc "Um..."
    mc "N-Nova?"
    mc "Is that... Dione?"
    stop soundloop2 fadeout 8
    play music novarpg volume 0.65
    scene dr 20
    pause .7
    scene dr 19
    pause .4
    scene dr 21
    pause 1.7
    scene novarpg0
    pause 5.3
    scene novarpg1 with flashfast
    pause 11.05
    scene novarpg2 with dis12
    pause 4.74
    play sound explosion2 volume 0.7
    scene dr 22
    pause 0.01
    show dr 23 with Dissolve(.15)
    pause 0.1
    show dr 22 with dis22
    mc "W-What..."with dis
    mc "WHAT?!" with hpunch
    show dr 25
    no "We won the challenge!" with dis
    no "Now there's only 1 left!"
    show dr 24
    mc "You're."
    mc "The."
    mc "Craziest."
    mc "Most unpredictable."
    mc "And downright the most amazing girl I've ever met!"
    mc "That shit was ridiculous!"with hpunch
    show dr 26
    no "*Giggles* Thank you, thank you."with dis08
    no "I had a clean shot, so I thought I couldn't waste that opportunity."
    show dr 27
    no "And besides, we lost the polygraph test because of me, so I make up for it a little with this!" with dis
    show dr 28
    mc "You definitely did! By a landslide!"
    show dr 27
    no "We're tied 2-2 now."
    no "So... let's finish the job!"
    no "No time to waste."
    show dr 28
    mc "*Laughs* For sure."
    mc "Let's go find that Exit Portal."
    play sound risingshort4
    stop music fadeout 4
    stop soundloop2 fadeout 4
    scene login3 with dis22
    pause 6.4
    play soundlow whoosh4
    scene white with dissolve
    play music3 partyfar fadein 4
    play music2b partypenny
    scene df 189 with dis27
    pause .5
    play sound3 plugin
    play sound4 clothes
    mc "*Removing your visor* Holy fuck!" with dis06
    mc "That was... fast!"
    play sound chair2
    show dr 29
    no "*Standing up* And that's how you play Eternum!" with dis12
    no "We're the best team ever."
    mc "*Laughs* I didn't do shit this time, but thanks."
    dol "What..."
    dol "What the fuck happened...?"
    show dr 30
    no "*Sticking her tongue out* AAAAAH!"with dis12
    no "Your ass got wiped out, that's what happened."
    no "You're not mocking me now? Did you run out of sarcastic comments?"
    show dr 31
    dol "Why would I? That was... AMAZING."
    show dr 30
    no "Say what you want, I–"
    show dr 32
    no "Wait, did you say amazing? Really?"with dis08
    dol "That was so cool!"
    dol "Did you really spot and hit us with a missile launcher from that distance?"
    no "*Giggles* Well, yes. I took advantage of a small moment when the wind stopped blowing."
    dol "Wow... consider me your new fan!"
    dol "If there's someone who deserves that CPU, it's you, Nova."
    show dr 33
    dol "Haskel, we're out of the competition. We'll let them win."with dis
    show dr 34
    no "Really?!"
    show dr 33
    has "WHAT?! Are you kidding me? We can still win the last challenge!"
    dol "But we won't."
    dol "Didn't you see what she did there while you were using your shitty binoculars?! We're not worthy."
    dol "Let's go back to the party. I just wanna forget about this and get drunk."
    has "Goddammit, Dolores..."
    show dr 34
    dol "Take care, guys." with dis
    mc "Bye, Dolores! Thank you!"
    no "Oh my god, [mc]!"
    no "Did you hear that?!"
    no "We won! And we don't even have to do the last challenge!"
    no "We won already!" with hpunch
    no "We-"
    play soundlow whoosh3b
    show dr 35
    sir "ABSOLUTELY NOT."with pr
    show dr 36
    mc "What?"
    mc "We're the only participants left!"
    show dr 35
    sir "I don't care. I won't give my CPU away unless you've earned it."
    sir "There's still one challenge left. If you can pass it, the prize is yours."
    sir "If not, I'll keep it myself and sell it on eBay."
    show dr 37
    no "That's not fair."
    sir "My game, my rules!"
    no "What a buzzkill..."
    show dr 38
    sir "Don't worry guys, the last challenge is probably the funnest one and the easiest by far."with dis
    mc "You say that about all your challenges."
    sir "But this time it's true!"
    sir "Please, put on your costumes again and come with me to the library."
    sir "This is..."
    play sound ding volume 1.4
    show dr38
    sir "{i}The temptation."
    mc "*Sighs* This better be the last one..."
    $ renpy.music.set_volume(0.2, delay=3.0, channel='music3')
    play sound2 doorold
    scene dr 39 with dis25
    bla "Moving away from the party, Akira leads you upstairs and enters the last room on the right."with dis12
    sir "Here it is!"
    sir "Please, sit down."
    play sound chair2
    play sound3 chairmove
    show dr 41 with dis12
    mc "Okay, Akira, we don't have all night, so... straight to the point."with dis08
    show dr 40
    sir "Of course, of course!"
    sir "You see... in this last challenge, you must prove that you're capable of controlling your impulses."
    sir "I'll leave the room for 25 minutes, and all you have to do is stay away from each other."
    show dr 42
    no "Staying away? What do you mean?"
    show dr 43
    sir "This is another one of the devices I created in my spare time."with dis
    sir "I call it... the TGF Cyberspunk-X7."
    show dr 41
    mc "...Naming your gadgets is definitely not your forte."with dis
    show dr 40
    sir "There's a sensor in this library that's capable of detecting Ulysses' neural implants, like the ones we have on the back of our necks."
    sir "If two implants get too close, an alert is triggered."
    show dr 42
    no "What if we didn't have neural implants?"
    show dr 40
    sir "Then you'd have lost already, not being able to complete either of the last two challenges."
    sir "Anyone who doesn't play Eternum isn't worthy of my prize."
    show dr 42
    no "Okay, so... if I understood this correctly, we have to keep away from each other for 25 minutes? That's it?"
    show dr 40
    sir "That is correct. You can't leave this room, and you must stay at least 6 feet apart."
    sir "Otherwise, the alarm will be triggered and you'll lose the challenge."
    show dr 47
    no "Hah! This doesn't make much sense, but it sounds easy enough!" with dis
    show dr 46
    mc "Right? I don't see the point of this “challenge” if he tells us what we're not supposed to do beforehand, but hey, I won't complain."
    show dr 44
    sir "Well... now comes the interesting part."with dis
    sir "This is a special wine I brought home from England last summer."
    sir "It's only produced in a small village of less than 100 inhabitants and it is said to be a very powerful aphrodisiac."
    sir "People there called it... “Ember’s Moan”."
    show dr 45
    no "A... powerful aphrodisiac?"
    show dr 44
    sir "Yes. But don't worry, there's only a little sip for each of you. The effects shouldn't be too extreme."
    sir "You drink the wine, you stay here for 25 minutes, and, if you can resist the temptation, you win the prize."
    sir "Easy."
    show dr 47
    no "*Laughs* What? You really think I'm gonna throw myself at [mc] and start kissing him or something just because I drank this thing?"with dis
    show dr 46
    mc "*Chuckles* Absurd."
    sir "Alright then! Let's do it."
    sir "Cheers!"
    play sound swallow2
    show dr 48
    bla "You and Nova drink the wine in one gulp." with dis15
    no "Mmmm...!"
    no "Is this really wine? It tastes like a strawberry lollipop."
    mc "Mmm! Wine or not, it’s delicious."
    play soundlow bottlesetdown
    play sound2 chairmove
    show dr 49
    sir "*Standing up* Fantastic!"with dis
    sir "I'll be downstairs getting a rum and coke."
    sir "Remember, you can't leave the room or you'll be disqualified!"
    no "Yes, yes, we got it."
    sir "See you in 25 minutes!"
    play sound3 doorold
    show dr 104
    sir "Have fun! But not too much fun!" with dis14
    sir "And everything's clean, don't worry!"
    mc "What a character."
    play sound chairmove
    show dr 50
    no "*Standing up* Okay, [mc]!" with dis
    no "We can finally say it: WE WON THE PRIZE!"
    mc "*Chuckles* Hell yes!"
    mc "This last challenge turned out to be way easier than I thought."
    no "Now all we have to do is overcome boredom for 25 minutes."
    mc "Sounds simple enough."
    play sound2 chairmove
    show dr 51
    mc "*Standing up* So, this is your library, huh?"with dis12
    mc "There are quite a lot of books."
    no "Yeah, although no one uses them, to be honest."
    no "Students simply bring their laptops or tablets. Everything has become digitized."
    show dr 52
    no "So now this place is mostly... a fuck pad where people come to make out."with dis12
    mc "*Laughs* Are those... condoms?"
    no "*Giggles* Yeah, some fraternity is probably planning to play a dirty game here later."
    no "Either that or Akira left this here for some reason."
    show dr 53
    mc "*Laughs* Yeah, I think it's the latter. I guess this is what he meant when he said that “everything was clean”."with dis12
    mc "There's more over here. Look at what I found!"
    mc "Would you be able to wear this while going around, Nova?"
    play sound chair2
    show dr 54
    no "*Giggles* Shut up!" with dis12
    show dr 55
    mc "Hey be careful, don't get too close!"
    mc "I don't want to lose the challenge just because you can't curb your irrepressible desire to kiss me."
    show dr 54
    no "*Chuckles* Me? I won't move from here."
    play sound2 chair2
    show dr 56
    mc "*Sitting down* Sounds good." with dis
    mc "I won't move from here, then. More than 6 feet away."
    show dr 54
    no "Cool."
    no "You feeling anything?"
    show dr 56
    mc "Nope. Well... apart from the alcohol I already had in my blood."
    mc "You?"
    show dr 54
    no "I'm fine. Just a little drunk."
    show dr 56
    mc "Cool."
    mc "So... now we wait."
    show dr 54
    no "We wait."
    show dr 56
    mc "Just 24 minutes left."
    show dr 54
    no "Cool. Cool."
    show dr 56
    mc "Cool."
    mc "Still good?"
    show dr 54
    no "I'm fine! You?"
    show dr 56
    mc "I'm fine."
    show dr 54
    no "C-Cool."
    show dr 56
    mc "Yeah, cool."
    play soundloop clock
    play sound whoosh6
    scene dr57
    no "Now we wait."
    mc "Cool..."
    stop music3
    play sound ding
    scene dr 58
    pause
    mc "*Taking a deep breath* (Okay...)" with dis08
    mct "This..."
    play sound4 chair3
    play soundloop2 beat2
    stop soundloop
    scene clockwhoosh05
    mc "*Hyperventilating* (THIS IS NOT COOL.)"with hpunch
    mct "What the fuck was in that wine..."
    mct "I'm hornier than an off-duty Marine in Thailand."
    mc "*Taking another deep breath* . . ."
    mct "Jesus, I'd even fuck a watermelon if there was one in front of me."
    mct "And what's with this huge erection? It's starting to hurt, even."
    mct "Was there Viagra in that damn drink?!"
    mc ". . ."
    scene dr 60
    mct "Am I the only one having a meltdown right now?" with dis
    show dr 61
    bla "You can see Nova curled up on her chair nervously jiggling her legs."with dis12
    no "(Oh god.)"
    no "(OH MY FUCKING GOD.)"
    no "(I NEED TO TOUCH MYSELF.)"
    no "(What is happening to me?!)"
    no "(At this rate I'll end up seeping through my pants.)"
    no "(I haven't felt this horny since that day in the Egyptian server.)"
    no "(Oh no, Nova, don't think about that again...)"
    no "(Not again...)"
    no "(Stop thinking about that day...)"
    no "(God, that day...)"
    if maatsex:
        if maatsexvariant:
            no "(I wish that [mc] fucked ME against the wall, not Maat...)"
        else:
            no "(I wish that [mc] fucked ME against the ground, not Maat...)"
        no "(The way she was moaning with pleasure...)"
        no "(There was... so much force in those thrusts...)"
        no "(The noise of [mc]'s hips slamming against hers...)"
        no "(I’ve never played with anything that big. C-Could I even take it...?)"
    else:
        no "(I wish [mc] would have fucked me that day...)"
        no "(Oh Jesus...)"
    mc "*Clears throat* So..."
    mc "Still good, Nova? Are you feeling anything?"
    stop soundloop2 fadeout 25
    $ renpy.music.set_volume(0.38, channel='music3b')
    play music3b silverware fadein 25
    show dr 65
    no "Um..." with dis12
    no "P-Perhaps just a tiny, liiittle, small something, y-yeah."
    no "Y-you?"
    show dr 62
    mc "I don’t think I've ever felt hornier in my life."with dissolve
    no ". . ."
    show dr 65
    no "O-Okay, I lied. ME TOO. I-I don’t think I’ve ever felt so... slick." with dis08
    no "I-I guess we’re both in this boat together, eh? Haha..."
    no "Who would have thought that drink would really work, huh?"
    mc "*Nervous laugh* Y-Yeah, right? Crazy."
    show dr 62
    no "I have like... t-this weird sensation inside..."with dissolve
    no "Like a..."
    show dr 65
    no "Burning."with dissolve
    no "It’s like something is making me just want to... tear off my clothes and go to town on myself..."
    mc "Right?!"
    show dr 64
    no "Must be the wine."with dissolve
    show dr 62
    mc "I guess so."with dissolve
    no ". . ."
    no "Are you..."
    show dr 65
    no "A-Are you hard?" with dis08
    show dr 62
    mc "Um... yep. I've been stiff for quite some time already."with dissolve
    no ". . ."
    show dr 64
    no "Makes sense. Can't blame you."with dissolve
    show dr 62
    mc "So... wetter than you’ve ever been, huh?"with dissolve
    show dr 65
    no "Well..."with dissolve
    no "Yeah. My panties are just so... damp."
    no "Y-You know, the wine."
    mc "Yeah, the wine..."
    show dr 62
    mc "Isn't it funny how we always end up stuck in the most bizarre situations?"with dissolve
    mc "First, we're taken as hostages by a crazy Egyptian nympho... and now this."
    show dr 64
    no "Oh, that day... y-yeah, I'd forgotten about it."with dissolve
    no "But... well, this is different."
    no "That time we were forced to... get intimate. This time it's just the opposite."
    no "Easier."
    show dr 65
    no "Much easier."with dis06
    show dr 62
    menu:
        with dis
        "That shit was nuts":
            mc "I wouldn't want to repeat that, that's for sure."with dis06
            mc "I hope we never get to see that woman again."
            show dr 64
            no "Yeah, I hope not..."with dissolve
        "Maat was hot, though":
            mc "I'll admit it had a certain thrill."with dis06
            if maatsex:
                mc "God, I'd pay to have Maat here and fuck her again... to throw her up against the shelves and just go to town..."
            no ". . ."
            no "I'm sure you would..."
        "That blowjob was something else [nova_pts]":
            mc "That blowjob, though?"with dis06
            mc "My god, I'd go broke just to repeat that right now."
            show dr 65
            no ". . ."with dis06
            no "You're saying that because of the wine."
            mc "Ehh... I'm not so sure, to be honest."
            mc "I've been thinking about it since that day."
            mc "It was... fucking amazing."
            mc "Those faces you made, Nova... The way you started choking..."
            $ nova_points += 1
            play sound beat
            show screen heartbeat
            show dr 64
            no "I mean... it was... entertaining, I guess. I was trying to make it look a-accurate, for Maat."with dis08
            no "I-I mean it’s not like I... wanted to..."
    show dr 65
    no "*Clears throat* B-But anyway, let's change the subject. This is not helping."with dis06
    mc "Yeah..."
    mc "How much time is left?"
    no "I don't even wanna know."
    mc "You know..."
    mc "I just had an idea that would make this much easier for both of us."
    no "I'm all ears..."
    menu:
        with dis
        "Propose touching yourselves [gr][mt](Nova's scene, +1)":
            mc "There's a way we could reduce this craving we're feeling."with dis06
        "Try getting distracted and hold on [mt](no dildo scene)":
            $ holdondildo = True
            mc "Let's try to think of other stuff. Like a naked grandma, bad food, or disgusting stuff in general."with dis06
            mc "Time will fly by."
            no "What a shitty idea."
            mc "Trust me, just do what I say."
            no "Hmm..."
            stop music3b fadeout 9
            play music2b partypenny
            play music3 partyfar fadein 6
            show dr 58
            bla "Making an effort to think about non sexual things, you start feeling the craving gradually reduce until the time is over."with dis2
            mc "Is it time? Fucking finally."
            no "I don't feel so good..."
            play sound knock3
            show dr 104
            sir "*Knocking on the door* Hey there!" with dis12
            sir "I'm back! There's only 30 seconds left for you to win the challenge!"
            sir "Nova? [mc]?"
            sir "Are you still there?"
            mc "Yeah, yeah, we're here."
            jump posnovapartyscene
    mc "We could... touch ourselves."
    show dr 63
    no "WHAT?!" with dissolve
    mc "Think about it. A quick wank and all this urge goes away."
    mc "We win the challenge, and everyone's happy."
    show dr 62
    no "You're crazy."with dissolve
    mc "Is that a no?"
    no "It's a... “do what you want”."
    no "I'm n-not touching myself in front of you."
    no "But suit yourself."
    mc "Oh thank god... I don't think I could have held back much longer."
    play sound clothes3
    play sound2 clothes3
    play sound3 clothes2
    show dr 66
    bla "You take off the robes that were covering your hips and thighs, releasing your cock in all its splendor." with dis15
    mc "*Sigh of relief* Oh god..."
    mc "Much better..."
    show dr 63
    no "Goddammit, [mc], I thought you'd go to a corner or something!"
    mc "What's the fun in that?"
    mc "And besides, don't act like we haven't seen each other naked before..."
    show dr 65
    no "*Mumbling* Hmm."with dis06
    show mchandjob05 with dis14
    bla "You begin to slowly stroke your dick." with dis12
    mc "AAAaaagh..."
    mc "Man, I needed this so much..."
    mc "No more craving."
    mc "Now the wine only makes the sensation feel... stronger."
    scene dr 65
    no ". . ." with dis12
    mc "I thought you wanted me to go to the corner, Nova? But you can’t even take your eyes off me..."
    no "*Shaking her legs nervously* Hmm."
    show mchandjob052
    mc "Ahhh, yes..."with dis12
    mc "This feels so good..."
    mc "When I close my eyes, I can see you kneeling in front of me that day, Nova..."
    scene dr 65
    mc "Do you remember?"with dis12
    no "*Shaking her legs nervously* Hmm... vaguely."
    mc "Oh fuck, you were so good..."
    mc "And when you hit my cock against your cheek..."
    mc "So fucking sloppy..."
    no "*Hyperventilating* . . ."
    mc "So warm..."
    play sound chairmove volume 1.5
    play sound2 chair2
    show dr 68
    no "OKAY, FINE." with dis
    no "Do you want me to touch myself? FINE, I'll do it."
    show dr 69
    mct "OH YEAH!"
    mc "I only proposed that because it'll help us."
    mc "All I want is for you to win that CPU."
    show dr 68
    no "Yeah... s-so do I."
    show dr 70 with dis14
    pause
    play sound belt
    play sound2 clothes4
    show dr 71 with dis15
    mc "Oh boy..."with dis08
    mc "You have a damn great butt, Nova. Dolores never stood a chance."
    no "*Little giggle* Right?"
    play sound3 chair2
    show dr 72 with dis12
    bla "Nova sits back on her chair, refusing to turn away from your erect member." with dis06
    show dr 73 with dis14
    mct "She's super petite and slim, but she has these thighs... I wish I could shove my face between them." with dis08
    mct "And the way she looks at me... goddamn."
    mc "The sooner you start, the sooner you'll feel better, Nova..."
    show dr 75 with dis14
    no "Yeah... I guess..." with dis08
    show dr 74
    mc "*Fapping faster* Oh, fuck yes..."
    show dr 75
    no "This wine is making my head spin..."
    show dr 74
    mc "If you don't feel comfortable, you can go to the corner, like you said."
    mc "I won't-"
    show dr 75
    no "Nah. I..."
    no "I don't mind."
    no "It's not as if we hadn't done anything before."
    no "This is nothing compared to that day."
    show dr 74
    mc "No arguments from me..."
    play sound clothes3
    show dr 76 with dis15
    bla "Nova moves her panties to the side, exposing her perfectly waxed pussy right in front of you." with dis12
    show dr 77 with dis15
    no "Fuck, my insides are burning..." with dis
    mc "I bet..."
    mc "Now... do it..."
    play soundlow penetration2
    show dr 78 with dis15
    no "AAaaaargh..." with dis08
    show dr 79
    no "Oh... F-FUCK!" with dis12
    mc "Better, right?"
    no "Yeah..."
    scene novadild1 with dis17
    no "*Moaning* M-Much, much better..." with dis
    mc "Told you..."
    no "Mmmm..."
    no "F-Fuck, it feels more intense than usual... for some reason..."
    no "Ahhh..."
    no "This wine..."
    mc "I'm not sure everything is the wine's fault, Nova."
    mc "Admit you enjoy seeing me stroking my cock..."
    mc "You can’t take your eyes off me jacking off, can you?"
    no "*Giggles* Perhaps a bit..."
    no "Perhaps I..."
    no "AAaaah..."
    play sound chair2
    play sound2 belt
    scene dr 80
    no "*Hyperventilating* Ahhhgh..."with dis15
    no "F-Fuck, why doesn’t this burning go away?"
    mc "I don't know, but I feel the same way..."
    play sound3 buttons
    play sound4 clothes5
    show dr 81 with dis15
    no "Aaahh... better..."with dis
    mc "Oh lord, I missed this sight..."
    scene novadild2
    bla "Nova starts fingering herself faster and deeper, turning her attention from her own labor to your dick, and vice versa."with Dissolve(1.85)
    no "AAAahhh, fuck yes..."
    mc "Better...?"
    no "M-Much better, yeah..."
    no "B-But... at the same time..."
    no "I feel hornier and hornier every second."
    no "I-It's not a bad sensation, but..."
    no "It’s as if my body wants... more."
    no "I-Is it not happening to you?"
    mc "It started happening when you started fingering yourself in front of me..."
    no "*Giggles* You're crazy."
    mc "I guess we're just two of a kind, then."
    no "*Moaning* Aaahh..."
    no "I-I guess so..."
    mc "You seem to be enjoying yourself..."
    no "I c-could say the..."
    no "*Moaning* Ahhh..."
    no "I could say the same..."
    no "I..."
    play sound2 chair2
    show dr 82
    no "*Hyperventilating* F-Fuck..." with dis12
    mc "Are you okay?"
    no "Why is this not enough?!"
    mc "You know, I have an idea..."
    play sound3 chair3
    show dr 82b
    no "D-don't move from your chair!"with dis
    mc "I won't!"
    mc "My idea is right behind you, actually..."
    show dr 83
    no "Hmm?"with dis08
    show dr 84
    no "W-Wait, what? The dildo?"
    no "I-I'm not using that."
    mc "Come on... you know you want to..."
    mc "If not for you, do it for me..."
    show dr 83
    mc "I NEED to see you using it."with dis12
    mc "Just this once..."
    no ". . ."
    mc "Imagine how good it would make you feel..."
    no ". . ."
    show dr 85
    no "Fuck."with dis12
    no "D-don't tell my mom what I'm about to do."
    mc "Good girl..."
    play sound chair2
    play sound2 jump1
    show dr 86
    bla "Replacing her embarrassment with curiosity, Nova gets on top of the table with a quick jump and grabs the toy."with dis14
    no "God, this thing is way bigger than I thought."
    mct "I can’t tear my eyes away from her pussy..."
    mct "It looks so fucking tight. She doesn't even mind showing it to me anymore."
    no "...and softer."
    mc "Is it stiff?"
    play soundlow wood
    show dr 87
    no "Um... well... not really."with dis12
    no "I mean, it's rigid, but also flexible."
    no "I guess this way it's easier to..."
    show dr 88
    mc "To put it inside your pussy."with dis
    show dr 87
    no "Y-Yeah, that."with dis
    show dr 88
    mc "You think you can take it all?"with dis
    show dr 87
    no "I can't."with dis
    show dr 88
    mc "Have you ever tried something so big?"with dis
    show dr 87
    no "I-I have toys, but... nothing even half the size of this."with dis
    show dr 88
    mc "Well, there's only one way to test yourself..."with dis
    no ". . ."
    show dr 89
    no "F-Fuck it. I can't hold it." with dis14
    mc "Attagirl..."
    show dr 90
    bla "She lets out a high-pitched whine as soon as she feels the cold surface of the dildo against her pussy lips." with dis12
    no "*Moans* F-Fuck, it's cold."
    mc "It'll get warm soon enough..."
    play sound ["<silence 0.2>", penetration2]
    show dr 91
    no "*Moans* Aaaahhhhhh..." with dis14
    mc "That's it..."
    play sound2 penetration2
    show dr 92
    bla "Nova's vagina offers no resistance as she softly sticks the dildo inside of her." with dis14
    $ renpy.music.set_volume(0.2, delay=6.0, channel='music3b')
    play soundloop wettingdildo1 fadein 3
    scene novadild3 with dis2
    no "AAAaahhh..." with dis
    no "Gggggh..."
    no "T-That's more like it..."
    mc "Is this soothing that sensation you were feeling?"
    no "D-Definitely..."
    mc "*Fapping faster* God..."
    mc "Does it feel better than your fingers?"
    no "Much f-fucking better..."
    no "I feel... f-f-filled."
    mc "I wish I could be the one filling you up..."
    no "*Giggles* AAagh..."
    scene mchandjob053
    bla "Nova stares directly at your dick."with Dissolve(1.5)
    no "Y-You'd be too big for me..."
    mc "Nonsense..."
    mc "You're handling that dildo like such a pro, Nova."
    mc "Think of it like... practice."
    scene novadild3
    no "*Giggles* T-Thank you..." with dis14
    mc "I could slide right in..."
    no "Aaaah..."
    mc "Does my cock turn you on?"
    no "*Moans* F-Fuck, it does..."
    no "Ahhh..."
    mc "Do you like thinking about me sliding all the way into you, Nova?"
    no "*Moans* I-I do..."
    pause
    play sound chair2
    scene novadild4 with dis2
    no "AAAH, FUCK..." with dis
    bla "Nova accelerates the pace of her movements and pushes the dildo as far as her untrained vagina allows her to."
    no "*Moaning* A-A-A-A-AAHH..."
    mc "You liked sucking my cock, didn't you?"
    no "I..."
    no "I did..."
    mc "You say that Maat pressured you into it... but you were already curious, right?"
    no "*Moaning* Fuck..."
    mc "Would you do it again?"
    no "A-Again?"
    no "I mean..."
    no "It was so... juicy..."
    no "So huge..."
    no "So... heavy in my hands..."
    no "*Moans* AAAH!"
    no "W-We've gotta ask Akira where he bought this wine."
    mc "I agree..."
    no "*Pinching her own nipple* It made my whole body so s-sensitive..."
    no "I need... more..."
    no "I..."
    stop soundloop fadeout 3
    play soundlow wood
    scene dr 93
    bla "Nova suddenly comes down from the table."with dis2
    play sound slam
    show dr 94 with vpunch
    pause
    show dr 95
    mc "What's going on?" with dis12
    show dr 96
    no "That pose... doesn't let me..."
    no "...go deep enough."
    show dr 95
    mc "Oh my... are you going to do what I think you're going to do?"
    play sound2 chair2
    play soundlow wood
    show dr 97
    no "*Getting on top of the table* Perhaps... are we going too far?" with dis15
    show dr 98
    mc "Why?"
    mc "We're just playing a game at a party. Nothing else."
    show dr 97
    no "A p-pretty intense game."
    show dr 98
    mc "I like to win. Don't you?"
    show dr 97
    no "I do."
    show dr 98
    mc "And do you still have that burning sensation from the wine?"
    show dr 97
    no "Fuck, I do..."
    show dr 98
    mc "Then we're doing nothing wrong."
    mc "We're gonna win this shit... but we don't have to suffer more than necessary."
    no ". . ."
    show dr 97
    no "I guess you're right..."
    play soundlow wood
    show dr 99 with dis15
    no "I hope you enjoy the show, then."with dissolve
    mc "You know I will..."
    play sound penetration2
    show dr 100
    no "AAAAAHHHH..." with dis14
    play soundloop wettingdildo2 fadein 2
    scene novadild5 with dis2
    no "Aaaaahhhh..." with dis
    no "Oh my god..."
    mc "Oh baby..."
    no "*Panting* F-Fuck..."
    mc "Are you finally feeling better now?"
    no "Better... yeah...."
    no "{bt=4}MmMMm... much better...{/bt}"
    mc "Did you ever get yourself off like this before?"
    no "*Panting* N-No..."
    no "*Panting* T-The toy I have at home can't even stand upright..."
    mc "I already know what to get you for Christmas this year, then."
    no "*Giggles* D-Don't you dare..."
    scene novadild6 with dis2
    no "AAAaaaahhh... y-yeah..." with dis08
    no "*Panting* Fuck, this feels so good..."
    bla "Nova continues to ride the dildo tirelessly while her own juices drip and soak the toy."
    mc "God, I love seeing your ass bouncing like that, Nova..."
    no "*Panting* Do you?"
    mc "But I know you can take it deeper..."
    mc "I know my personal hacker girl can do better than that..."
    no "*Panting* Aaahh... can I...?"
    no "I-Is that what you want?"
    mc "Fuck yes..."
    play soundloop2 wettingdildo3 fadein 3
    stop soundloop fadeout 2
    scene novadild7 with dis2
    bla "Following your command, Nova shoves the dildo deeper and deeper inside her with each bounce until she's able to take it almost entirely." with dis08
    no "AAAAAaaaahh..."
    mc "Good girl..."
    no "Ggggghh..."
    no "*Panting* L-Like this?"
    mc "Oh my fucking god, yes..."
    no "*Panting* AAaahh... aaahhh... ahhhh..."
    mct "She looks so gone... her mind must be going a mile a minute."
    mc "The fact that I'm watching you while you ride that dildo turns you on, doesn't it?"
    no "*Panting* It does..."
    no "I want you to watch me..."
    no "I w-want you to keep your eyes on me, without l-looking away..."
    mc "How many times have you fantasized about the Egyptian server?"
    no "*Moaning* Aahhh..."
    no "S-So many times..."
    no "God, that was s-so f-fucking hot......"
    no "I couldn’t get the sight of your... c-cock out of my head, [mc]..."
    no "And your groans when I took you into my mouth..."
    no "I think I masturbated for 2 weeks straight t-thinking about it."
    mc "Oh yes..."
    no "But it shouldn't have been so... hot... that was supposed to be... s-scary."
    no "W-Why was it so hot?"
    no "*Panting* Is it bad that I thought about it so much, [mc]? The smells, the sounds..."
    no "The way my heart was racing..."
    no "Am I... broken, [mc]?"
    mc "No, you're not, Nova..."
    mc "You’re just... curious."
    no "AAAaaaahh..."
    no "*Panting* F-Fuck..."
    no "*Panting* I g-got to the bottom..."
    mc "That's my girl..."
    mc "You're such a fast learner, Nova."
    no "*Panting* F-Fuck yess..."
    pause
    play soundloop wettingdildo3 fadein 2
    stop soundloop2 fadeout 3
    scene novadild8 with dis2
    no "*Groaning* AAAaaaAAAAaahh..." with dis
    mc "Oh sweet Lord..."
    no "HHHHhhggg... t-this is so good..."
    mct "I can't stop imagining Nova riding my cock instead of that dildo..."
    mct "She always seems to have infinite energy. I bet she'd be able to bounce up and down for hours until I passed out..."
    mct "Boy, I've gotta live to experience something like that one day..."
    pause
    no "*Groaning* Aaaaahh... f-fuck..." with dis08
    no "F-FUCK! I'm gonna cum, [mc]..."
    mc "The things you said at the cafeteria... they were all lies, right?"
    no "*Groaning with pleasure* Ehh...?"
    no "Ah... y-yes..."
    mc "You ARE looking for someone to fulfill all your kinky desires."
    no "*Groaning* YES..."
    mc "And you want ME to fuck you..."
    no "I'm gonna c-cum..."
    mc "I asked you a question..."
    no "AAAAHHhh..."
    mc "Nova..."
    no "YES!" with hpunch
    no "I want YOU to fuck me!"with hpunch
    $ nova_points += 1
    $ novadildo = True
    no "*Panting* Only you..."
    mc "Oh babe..."
    menu:
        with dis
        "Grab Nova and fuck her":
            stop soundloop fadeout 1
            play sound chair2
            play soundlow slam3
            play sound3 penetration2
            play sound7 penetration2
            scene dr 117
            no "W-What...?!"with dis08
            no "No!"
            no "I-I was almost there!"
            play sound5 chair3
            play sound6 wood
            play sound7 clothes1
            play soundlow slam3
            show dr 118
            no "[mc]! W-What the fuck are you doing?!" with dis
            show dr 119
            mc "Nova, I need to feel that tight pussy of yours..."with dissolve
            show dr 118
            no "WHAT?!" with hpunch
            no "We're gonna lose the challenge!"
            show dr 119
            mc "Fuck that challenge..."with dissolve
            show dr 118
            no "I don't... I..."with dissolve
            no "My god, y-your cock is even bigger than the dildo!"
            no "AND WAY THICKER!" with hpunch
            show dr 119
            mc "Imagine how it'd feel inside of you..."with dissolve
            show dr 118
            no "I... eh..."with dissolve
            no "I-I'm not gonna lose my virginity in a lib-"
            no "I-I mean... I don't... I can't!"
            show dr 119
            mc "You said that you wanted me to-"with dissolve
            show dr 118
            no "It was the wine talking!"with hpunch
            no "J-Just dirty talk!"
            no "And the burning is gone already!"
            no "I-It was a great idea, so now we can sto..."
            play sound knock3
            show dr 119
            sir "*Knocking on the door* Hey there, guys!" with dissolve
            show dr 120
            sir "The challenge is over!"with dissolve
            sir "Nova? [mc]?"
            no "F-Fuck! Told you!"with hpunch
            no "G-Get off me!"
            mct "Goddammit..."
            stop music3b fadeout 9
            play music2b partypenny
            play music3 partyfar fadein 6
            show dr 104
            bla "You quickly get dressed again and hide your boner as best as you can."with dis15
            mct "Fuck."
            mct "What the hell happened to me? I knew the challenge was about to end and he could be back any second."
            mct "I got carried away... I need to learn some self-control."
            play soundlow knock1
            sir "Hello?"
            mc "*Clears throat* Y-Yeah, yeah, we're here."
            $ akirawin = False
        "Let her cum":
            no "Oh god..." with dis08
            no "Yeah..."
            no "OH GOD!"with hpunch
            no "I'm cumming!"with hpunch
            play sound5 woodhit volume 0.6
            stop soundloop fadeout 1.5
            play sound7 penetration2
            play sound6 penetration2
            scene dr 101 with dis15
            play sound cum1 volume 1.3
            play sound2 cum2 volume 1.3
            play soundlow cum3
            show dr 101
            no "*Groans* AAAAAaaargh..." with hpunch
            bla "Nova lets the full length of the dildo get inside her and orgasms, contracting all the muscles of her slim body."
            play sound cum1 volume 1.3
            play sound2 cum2 volume 1.3
            play soundlow cum3
            no "*Groans* AAaaah..." with hpunch
            play sound4 slam3
            show dr 102 with dis
            no "*Collapsing* Jesus..." with dis08
            show dr 103
            mc "My god..."with dis12
            mc "That was hot as fuck, Nova..."
            no "*Panting* Yeah..."
            mc "Why can't I cum too?! This cursed wine is fucking with me..."
            mc "I'm horny as fuck, but I can't cum!"
            no "*Recovering her breath* That got a bit out of hand."
            mc "You did great. I knew you could take it all..."
            no "*Recovering her breath* It sure was... intense..."
            play sound knock3
            show dr 102
            sir "*Knocking on the door* Hey there, guys!" with dis
            sir "The challenge is over!"
            play sound penetration2
            show dr 101
            no "F-Fuck!"with dis
            no "The challenge! I almost forgot about it!"
            no "D-Distract him, p-please!"
            mc "W-What? Me?"
            no "Y-Yeah!" with hpunch
            no "I s-still have a dildo inside my p-pussy, in case you didn't notice!"
            stop music3b fadeout 9
            play music2b partypenny
            play music3 partyfar fadein 6
            show dr 104
            bla "You quickly get dressed again and hide your boner as best as you can."with dis15
            mct "Fuck."
            mct "Why the hell couldn't I cum?"
            mct "This fucking blue-balling wine..."
            sir "Nova? [mc]?"
            mc "*Clears throat* Y-Yeah, yeah, we're here."

label posnovapartyscene:
    play sound dooropen1
    play sound2 doorsqueakk
    $ renpy.music.set_volume(0.0, delay=1.0, channel='music3')
    $ renpy.music.set_volume(0.5, delay=1.0, channel='music2b')
    show dr 105
    sir "Ah, wonderful!"with dis14
    sir "Happy to see you in one piece!"
    show dr 106
    mc "Y-Yeah, thanks."
    show dr 105
    sir "You guys... won Akira-san's challenge! Congratulations!"
    show dr 106
    mc "A-Awesome!"
    if not akirawin:
        show dr 107
        sir "Or... that's what I'd say if you had really won." with dis12
        mc "Wait, what?"
        sir "Don't play dumb, [mc]."
        sir "The alarm on my receiver was triggered just a moment ago. I know you two got too close. You failed my challenge."
        show dr 108
        no "*Appearing from under a table* W-What? That's absurd!" with dis12
        no "It must have been a defect of the device."
        mct "Did she put her top on backwards...?"
        show dr 109
        sir "*Chuckles* Funny! But my devices have no defects."
        show dr 108
        no "Then... maybe someone else with a neural implant got right under me on the floor below. So... the device was triggered!"
        no "I mean, think about it."
        no "We held out for 24 minutes just to fail at the last second?"
        no "That doesn't make any sense!"
        sir "Hmm..."
        show dr 109
        sir "Well, now that you mention it..."
        sir "...yeah, the truth is that it would have been ridiculous."
        sir "And I guess that could have happened, indeed."
        show dr 108
        no "Exactly."
        mct "Phew."
        show dr 105
        sir "Let me begin again, then..."with dis
        sir "You guys... won Akira-san's challenge! Congratulations!"
        show dr 106
        no "Hell yes!"
        show dr 109
        sir "Tell me, how did it go?" with dis12
    else:
        show dr 108
        no "*Appearing from under a table* YES!" with dis12
        no "We did it!"
        if novadildo:
            mct "Did she put her top on backwards...?"
        show dr 109
        sir "Indeed."
        sir "Tell me, how did it go?"
    show dr 108
    no "W-What?"
    no "I mean, oh well, *nervous laugh* it's true that it makes you hornier."
    no "WAY hornier."
    no "But it wasn't a-anything we couldn't handle!"
    no "Right, [mc]?"
    mc "T-Totally!"
    show dr 109
    sir "Now... what if I told you that my “wine”... was just sugary fruit juice?"
    play soundlow gasp
    show dr 110
    no "*Gasps* What?" with dis
    no "You can't be serious."
    sir "Just sugar and strawberry juice."
    sir "Everything you felt... was already within yourself."
    no "Oh my god..."
    mc ". . ."
    mc "That's such bullshit."
    sir "Eh..."
    show dr 111
    sir "Okay, okay, you got me." with dis
    sir "It looks cool when they say this in movies."
    sir "Uh... yeah, it really was a powerful aphrodisiac, not fruit juice. It's actually illegal in many countries."
    show dr 112
    no "Hmm..."
    mc "Fucking trickster..."
    show dr 111
    sir "In fact, it's not recommended to drink it along with alcohol to avoid gastric problems."
    play sound2 swallow
    play sound3 swallow
    show dr 113
    no ". . ." with dis
    show dr 114
    no "Oh god, I don't feel so good..."with dis
    show dr 115
    sir "Yeah... that's what I was referring to."
    sir "It doesn't make everyone sick, but the ones affected can't stop puking for a good 30-60 minutes."
    show dr 114
    no "Fuck, you could have said that before..."
    no "Aghh..."
    no "My stomach hurts. I-I  need to go to the bathroom."
    show dr 116
    mc "Do you want me to go with you?"
    show dr 114
    no "No, no, I don’t want you to see me like that."
    no "Go and check on Penny, or... I don't know, wait for me somewhere nearby."
    show dr 115
    sir "I'll go get the CPU and bring it back to you."
    show dr 114
    no "Y-You better!"
    no "I'll come find you if you..."
    play sound2 swallow
    play sound3 swallow
    show dr 113
    no ". . ." with dis
    play sound run
    show dr 107
    bla "Nova rushes out from the room." with dis15
    sir "Yeah, she probably drank too many beers..."
    mc "She only drank one!"with hpunch
    show dr 105
    sir "But she was drunk! That's what matters!"with dis
    sir "Look at you, you drank the same amount of wine and many more beers than her, but you are fine!"
    sir "We all have different metabolisms."
    show dr 106
    mc "Is she gonna be okay?"
    show dr 105
    sir "Of course, of course, don't worry!"
    sir "I'll wait for her next to the bathroom so I can give her the CPU."
    show dr 106
    mc "Well alright..."
    mc "Tell her to join me and Penelope when she's done!"
    show dr 105
    sir "Will do!"
    sir "Farewell, [mc]. It was a pleasure playing with you."
    sir "Adios!"
    show dr 106
    mc "O-Okay, see ya."
    play sound ["<silence 1.6>", doorclose2]
    play sound2 doorsqueakk
    $ renpy.music.set_volume(0.3, delay=2.0, channel='music3')
    $ renpy.music.set_volume(0.0, delay=2.0, channel='music2b')
    show dr 104 with dis15
    mct "Man, that sure was a peculiar... game."with dis08
    mct "At least I can say the University of Kredon has a well-deserved reputation. Those inventions were mind-blowing."
    mct "I feel sorry for Nova, but there's not much I can do for her right now."
    mct "I'm certain this was an interesting experience for her, though."
    mct "I wonder if she really meant everything she said in here or if she was just playing along because of the wine."
    mct "In any case, I bet she doesn't regret it..."
    mct "Or... well, so I hope."
    mct "Let's see if Penelope managed to clean the beer from her hair."
    $ renpy.music.set_volume(0.0, delay=6.0, channel='music3')
    $ renpy.music.set_volume(0.5, delay=6.0, channel='music2b')
    scene dp 0
    hide screen heart
    with Dissolve(3.1)
    $ ppp8 = True
    call screen collegeparty3 with dis

label collegeparty4:
    if ppp1:
        mc "I should ask at the counter before going anywhere."with dissolve
        call screen collegeparty1 with dis06
    $ renpy.music.set_volume(0.0, delay=1.6, channel='music3')
    $ renpy.music.set_volume(0.5, delay=1.6, channel='music2b')
    play soundloop partywalla
    if pennyreginahate:
        play sound dooropen1
        play sound ["<silence 0.9>", doorclose2] volume 0.6
        scene dlc 10 with dis17
        mct "I've gotta find Penelope before she sees the photos." with dis08
        mct "Let's go to the main hall, she's supposed to be there."
        show dlc 12
        bla "You start heading towards the main hall, just to stumble upon Penelope checking her phone."with dis12
        mct "Oh, fuck."
        mc "Erm..."
        mc "H-Hey Penny!"
        show dlc 13
        mc "I..."with dis
        mc "I-I was looking for you!"
        mc "I went to..."
        mc "Uh..."
        show dlc 14
        p "Yeah!"with dis08
        p "I..."
        show dlc 15
        mc "Um..."with dis04
        mct "Shit, is she crying?"
        mc "D-Did you see the photos?"
        show dlc 14
        p "Y-Yeah. I... I see you two were having fun, huh?"with dis04
        show dlc 15
        mc "It's not what it seems! We didn't do any–"with dis04
        show dlc 14
        p "Hey, you don't have to give me any explanations."with dis04
        p "I'm not your mom!"
        p "Or... your girlfriend, or anything."
        p "This is a party, right?"
        show dlc 15
        mc "I-I don't know what I was thinking. I just..."with dis04
        show dlc 14
        p "It's my fault. I shouldn't have asked you to help me with my boring shit."with dis04
        p "I see it now."
        p "You just came here to drink, have fun, and meet girls, and I... just kept bugging you with..."
        show dlc 15
        mc "You didn't bug me with anything!"with dis04
        show dlc 14
        p "Hey, you can do whatever the fuck you want."with dis04
        p "It's just that..."
        show dlc 16
        p "*Crying* T-That..."with dis
        p "With {i}her{/i}?"
        p "Regina?"
        p "Really?"
        show dlc 17
        mc "Regina doesn't mean shit to me! She just tricked me!"with dis04
        show dlc 16
        p "Tricked? Then how did you end up naked with her in the locker room?"with dis04
        show dlc 17
        mc "Um..."with dis04
        mc "W-Well..."
        show dlc 14
        p "*Sobbing* God, I'm a fucking idiot."with dis
        p "I can't believe I was so damn dumb."
        show dlc 15
        mc "I'm so sorry, Penny... I didn't want any of this to happen."with dis04
        show dlc 14
        p "It's my fault. It always is."
        p "I..."
        p "I'm sorry, I'm such a drama queen, eh?"
        p "*Sighs* I... guess I'm just gonna go home."
        show dlc 15
        mc "Aw, come on, don't say that."with dis04
        show dlc 14
        p "I've embarrassed myself enough for one night."with dis04
        p "I'll see you tomorrow, [mc]."
        if novapath:
            p "Say sorry to Nova for me."
        show dlc 11
        mc "Wait!" with dis15
        show dlc 18
        mct "And... she left."with dis
        mct "Aaaaagh, what a fucking mess."
        mct "I'm such a moron."
        mct "I'd be mad too if someone had ignored me like that just to try to hook up with someone I don't like."
        mct "I'll have to think of a way for her to forgive me..."
        mct "But anyway, let's go home."
        mct "I don't feel like partying anymore."
        mct "This is not how I wanted to end the night, that's for sure..."
        stop music2b fadeout 5
        stop soundloop fadeout 5
        stop music3 fadeout 5
        $ leavepartyearly = True
        $ penelopepath = False
        $ penelopeu = False
        jump nancyworkplace
    scene df 55
    hide screen heart
    with dis12
    call screen collegeparty4 with dis06

label collegeparty5:
    play sound doorold
    $ renpy.music.set_volume(0.6, delay=1.6, channel='music3')
    $ renpy.music.set_volume(0.0, delay=1.6, channel='music2b')
    stop soundloop fadeout 1.6
    scene df 135 with dis15
    if ppplr:
        $ ppplr = False
        pause .2
        if ppp9:
            mct "Oh, the college locker rooms Penny mentioned before."with dis08
        else:
            mct "Oh, the college locker rooms."with dis08
        mct "Hmm... there are no Halloween decorations in here."
        mct "It doesn't seem to be part of the party."
    call screen collegeparty5 with dis08
label collegepartydressingroom:
    if ppp6:
        show screen heart
        mc "Um..." with dis08
        mc "*Whispering loudly* Penny? You there?"
        p "...[mc]?"
        mc "Yeah, it's me!"
        if pennybeerseen:
            mc "I thought you'd still be here after what happened earlier."
        else:
            mc "Someone told me you'd be here."
            mc "Something about... a bucket full of beer?"
        p "Are you alone?"
        mc "Yep, there's only me here."
        play sound locker
        show df 136
        bla "You hear a locker closing across the room."with dis14
        show df 137 with dis
        show df 138
        p "Hey there!" with dissolve
        show df 139
        mc "Hey Penny!"
        show df 138
        p "Are you having fun?"
        show df 139
        mc "I am!"
        mc "What about you, though? Are you okay?"
        mc "Will you be able to save your dress?"
        show df 140
        p "Nah... it's all stained and sticky."with dis04
        p "And it smells awful."
        show df 141
        p "And look at my hair... ugh... it's all greasy."with dis12
        show df 137
        mc "Agh, I'm sorry to hear that... you were rocking the party with your Idriel costume."with dis
        mc "What a bummer."
        show df 140
        p "I'd like to think it was just bad luck, but..."with dis04
        p "I know that Regina bitch isn't very fond of me."
        p "I'm sure she did that on purpose."
        show df 137
        mc "Oh, yeah, I talked to her... I think she's jealous of you. {w}{i}Very jealous."with dissolve
        show df 140
        p "Huh, interesting way to channel her frustration."with dis04
        show df 137
        mc "What are you gonna do, then?"with dis04
        show df 138
        p "Go back to the party, of course! That's not going to stop me."
        p "I have a dress in my locker that I can wear."
        show df 140
        p "I mean, it's not a costume, but... it'll do the trick."with dis04
        show df 141
        p "*Sighs* And I'll have to shampoo my hair. It's completely ruined."with dis12
        p "I'll make myself a ponytail or something to muddle through."
        show df 138
        p "This is gonna take a while, so don't worry about me."with dis
        p "I'll join the party again when I'm ready."
        show df 139
        mc "Alright! We'll be around!"
        show df 143
        p "So... did you need anything, or were you just missing me?"with dissolve
        show df 139
        mc "Oh, true! I almost forgot."with dissolve
        mc "Uh... it's a long story, but Nova and I joined a game that a weird guy with a painted-on mustache organized."
        mc "There are some challenges, and the prize is a next-gen processor."
        mc "A {i}really{/i} good one."
        mc "The current challenge is finding a bra and bringing it back to him. The team who gets the biggest one wins."
        show df 143
        p "I see..."with dissolve
        p "And you thought of asking your big titty blonde bimbo friend to lend you hers, right?"
        mc "*Laughs* You know I don't think that of you."
        p "Of course, of course..."
        play sound locker
        show df 144
        p "Hmm..." with dis14
        p "Agh, I thought I had my blue bra here."
        p "What have I done with it...? I don't remember seeing it in my drawer at home..."
        p "Mom must be taking my clothes again!"
        mc "Y-You and Nancy share your lingerie?"
        play sound2 locker
        show df 145
        p "*Chuckles* She steals mine!" with dis14
        p "She says she does it unintentionally because we use about the same cup size, but I'm not buying that!"
        show df 146
        mc "Oh boy..."
        show df 145
        p "Anyway, I just have this one. Will this do?"
        show df 146
        mc "F-For sure..."
        mc "You don't need it?"
        show df 145
        p "Nah, don't worry. It's all yours."
        show df 146
        mc "You know, you don't have to cover yourself. It's just me here..."
        show df 145
        p "*Giggles* I'm fine, thank you."
        show df 146
        mc "Not even a little peek for your manager?"
        show df 145
        p "Nope. I don't want to distract you from this game of yours."
        show df 144
        p "And I need to wash my hair before it's too late! See ya!" with dis12
        mc "*Chuckles* You're evil."
        mc "And after the game? "
        p "*Giggles* After the game? Who knows..."
        p "{bt=4}The night is young...{/bt}"
        p "Goodbye, [mc]!"
        mc "*Chuckles* Bye, Penny..."
        mct "Oh boy, she sure loves to tease me..."
        scene df 135 with dis14
        mct "Alright, I have the bra!"with dissolve
        mct "Back to the [gr]cafeteria."
        $ ppp6 = False
        $ ppp7 = True
        call screen collegeparty5 with dis06
label collegeparty6:
    play sound doorold
    scene dp 1 with dis15
    if ppp6 and not ppp4:
        pause .1
        mct "Hmm... looks like Penelope isn't back yet."with dis
        mct "Maybe she's in the locker room?"
    if ppp8:
        $ ppp8 = False
        pause .1
        mct "Hmm... Penelope isn't back yet."with dis
        mct "I'll go wait for her on that couch right there."
        jump collegepartypenny1
    if (ppp2 or ppp3 or ppp5) and ppp4:
        $ ppp4 = False
        mct "Hmm... there's the girl that dragged Penelope right off."with dis08
        show dp 2
        show screen heart
        p "Hi there!" with dis14
        show dp 3
        mc "Oh, hi there!"
        mc "*Laughs* I see you managed to escape your captor."
        show dp 2
        p "*Laughs* Yeah, she told me she's a follower of mine that started studying here this year."
        p "She just wanted a selfie together."
        show dp 3
        mc "Problems of being Insta-famous!"
        show dp 2
        p "*Chuckles* Problems of living in a small town where everyone knows each other and loves to gossip."
        show dp 4
        p "But anyway, let me show you around!"with dis
        p "This is algebra class, and right in front of it you can find the locker rooms and the gym where the basketball team plays."
        p "If you look out the win–"
        play sound splash3
        play sound2 drips volume 2
        play sound3 splash1
        play sound4 bucket
        show dp 5 with dis2
        bla "A girl throws a bucket filled with some liquid all over Penelope." with dis
        mc "What the fuck..."
        p "W-W-Wha..."
        reg "OH MY GOD, WHAT HAVE I DONE?!"
        reg "I'm so sorry, Penny!"
        reg "I lost my grip."
        show dp 6
        p "Regina..." with dis
        reg "Oh my, I'm so clumsy..."
        reg "I ruined the dress of the prettiest girl at the university!"
        reg "You have no idea how bad I feel..."
        reg "Especially considering that the smell of beer doesn't leave so easily."
        show dp 5
        p "WHAT?! This is beer?!" with dis
        p "Why are you carrying a bucket full of beer?"
        reg "One of the barrels at the other side of the building was broken, and we used this to collect what was pouring. I was taking it back to the cafeteria."
        p "Oh fuck, my hair is gonna stink all night!"
        reg "Yeah... and get very sticky. That's too bad..."
        show dp 6
        p "That sure was a huge coincidence."with dis
        reg "I wish I could do something to remedy it, but..."
        reg "*Giggles* I guess it is what it is, huh?"
        p "Yeah..."
        show dp 7 with dis12
        mc "Damn... I'm sorry, Penny." with dis06
        mc "Can I help you somehow?"
        show dp 8
        p "No, don't worry..."
        p "I'll... I'll go to my locker."
        show dp 7
        mc "Will you be able to clean it?"
        show dp 8
        p "I'll have to change my dress. This one will stink all night otherwise."
        show dp 7
        mc "You have to change your Idriel costume?!"
        show dp 8
        p "Yeah, I should have something I can use in my locker, although... it won't be a costume."
        p "And I'll have to wash my hair too. It’s a good thing I already got that Idriel pic for the IG sponsor though."
        show dp 7
        mc "Damn, that sucks..."
        show dp 9
        p "Hey, I'm not backing out now."with dis06
        p "I came to this party to have fun, and that's what I'm still planning to do. I don't care what people think."
        p "Just let me go get cleaned up."
        if novapath:
            p "You can wait for me here, or check on Nova."
        else:
            p "You can wait for me here."
        p "I'll be right back!"
        mc "Okay then, alright!"
        mc "See you later!"
        play sound doorold
        show dp 10 with dis17
        reg "Oh, damn, how unfortunate for her." with dis06
        reg "Poor, poor, Penelope."
        mc "...You did that on purpose?"
        reg "Oh please, not at all!"
        reg "As I said, it was just an unfortunate incident."
        show dp 12
        reg "*Checking you out* But anyway, I don't think we've met before... Apollo?"with dis08
        show dp 11
        mc "Close, Eros."
        mc "I'm [mc], I came with Penelope."
        show dp 12
        reg "I see..."
        reg "Are you her... boyfriend?"
        show dp 11
        mc "No, not really. We're just friends. I've been in Kredon just for a couple of months, actually."
        show dp 12
        reg "Interesting."
        reg "I like your style, [mc]."
        reg "You definitely deserve someone better than Penelope to accompany you at this party."
        show dp 11
        mc "Better than the most popular girl in college? That'll be hard to find."
        show dp 12
        reg "Well, that depends on whether you prefer a dumb, boring, walking piece of titty meat, or... something spicier."
        show dp 11
        mc "I'm sorry?"
        show dp 12
        reg "Anyway, I should leave this bucket in the cafeteria."
        reg "I'll see you around, [mc]..."
        play sound doorold
        show dp 13 with dis17
        mct "Did this girl try to sabotage Penelope's costume on purpose?" with dis
        mct "It sure looked like it..."
        mct "But anyway, I guess I'll go wait for Penny to come back."
        if novapath:
            mct "Or... I could go see what Nova is doing. I doubt Penny can get changed and wash her hair that quickly."
            mod "Go back and left twice to talk with Nova and play the game."
        $ ppp9 = True
        $ pennybeerseen = True
        show dp 1 with dis17
    if ppp6 and ppp4:
        $ ppp4 = False
        pause .1
        mct "Hmm... Penny doesn't seem to be here." with dis
        mct "But that girl is the one who dragged her off. I'll go ask her."
        reg "Hi, handsome."
        show dp 11
        mc "*Turning around* Hmm?" with dis12
        mc "Oh, hello there..."
        show dp 12
        reg "*Checking you out* I'm Regina."
        reg "I don't think we've met before... Apollo?"
        show dp 11
        mc "*Chuckles* Close! Eros."
        mc "I'm [mc]. Nice to meet you, Regina."
        show dp 12
        reg "I see..."
        reg "Can I help you somehow, [mc]?"
        show dp 11
        mc "Actually, yeah! I'm looking for Penelope. Penelope Carter. Do you know her?"
        show dp 10
        reg "Oh, of course I do! How could I not know the most popular girl in our beautiful town?"with dis06
        reg "She just left. She had an unfortunate incident."
        mc "What?! What happened?"
        reg "She was super clumsy and accidentally ran into this bucket full of beer. She went to the locker room to fix her pretty hair and get changed into something else."
        reg "She'll have a terrible smell all night, poor girl."
        show dp 11
        mc "...The bucket you're holding right now?"with dis06
        mc "You did this?"
        show dp 12
        reg "Oopsie."
        reg "I guess I was a little clumsy too, whoops."
        show dp 11
        mc "You did that on purpose...?"
        show dp 12
        reg "Of course not!"
        reg "As I said, it was just an unfortunate incident."
        reg "But... tell me a bit about yourself. Are you her... boyfriend?"
        show dp 11
        mc "Um... no, not really. We're just friends. I've been in Kredon just for a couple of months."
        show dp 12
        reg "Interesting."
        reg "I like your style, [mc]."
        reg "You definitely deserve someone better than Penelope to accompany you at this party."
        show dp 11
        mc "*Chuckles* Better than the most popular girl in college? That'll be hard to find."
        show dp 12
        reg "Well, that depends on whether you prefer a dumb, boring, walking piece of titty meat, or... something spicier."
        show dp 11
        mc "What...?"
        show dp 12
        reg "Anyway, I should leave this bucket in the cafeteria."
        reg "I'll see you around, [mc]..."
        play sound doorold
        show dp 13 with dis17
        mct "Did this girl try to sabotage Penelope's costume on purpose?" with dis
        mct "It sure sounded like it..."
        mct "Anyway, I'll go check the locker room she mentioned."
        mct "Or... I guess I could wait for her here, but if I do that I probably won't make it back to Nova in time."
        $ ppp9 = True
        show dp 1 with dis17
    call screen collegeparty6 with dis08
label precollegepartypenny1:
    bla "You prepare yourself a drink and spend some time greeting people."with dis14
label collegepartypenny1:
    play sound2 ["<silence 0.3>", chair1]
    show dp 14
    show screen heart
    with dis15
    $ ppp9 = False
    $ ppp10 = True
    mc "*Sitting down* (Man, this could be my class next year.)" with dis
    mct "I've gotta get into this university by any means."
    mct "With everything that has been happening lately, it's hard to focus on my studies, but I can't throw it all away now."
    show dp 15
    reg "Hi there!"with dis
    mc "Hmm?"
    show dp 17
    mc "Oh... hi."with dis
    mc "Regina, right?"
    show dp 16
    reg "Yes. Good to see you, [mc]."
    reg "Are you having fun?"
    show dp 17
    mc "Sure am!"
    mc "The open bar is a killer."
    show dp 16
    reg "*Giggles* Be careful not to get too drunk... it's harder to keep track of free drinks than ones you have to pay for."
    show dp 17
    mc "*Chuckles* That's true."
    show dp 16
    reg "What are you doing here all alone?"
    show dp 17
    mc "Waiting for Penelope. She went to get changed and wash her hair."
    mc "It's been a while already, so she should appear at any moment."
    show dp 16
    reg "Well... I wouldn't count on it, to be honest."
    reg "You know how those Instagram girls are... always superficial, only caring about how they look."
    reg "She arrived with that pretty Idriel costume... and now she has to improvise a costume from a dress in her locker and a ponytail?"
    reg "I'd have gone home if I was in her shoes."
    show dp 17
    if pennybeerseen:
        mc "I don't know, she told me she'd join back after getting changed."
    else:
        mc "I don't know, that would be very unlike her."
    show dp 16
    reg "Oh, and I honestly hope so."
    reg "I'd like to see her wearing whatever she had in her locker..."
    show dp 19
    p "Well, lucky for you, you don't have to wait anymore, Regi."with dis08
    p "Hi, [mc]! Sorry for the wait."
    show pennypartypan with Dissolve(1.85)
    pause 5.5
    $ unlock_look("penelope", 12)
    scene dp 20
    mc "Holy... fuck!" with dis12
    mc "Goddamn, this dress looks GREAT on you, Penny."
    show dp 22
    p "Thank you!"with dis
    p "I wish I'd have had more time to get a fancier hairstyle or better makeup, but I'll muddle through with this."
    show dp 23
    mc "“Muddle through”? You look spectacular."
    show dp 21
    reg "I see you reused the bracers from your other costume."
    show dp 22
    p "Indeed. Thanks for noticing, Regi..."
    p "Who'd have thought it'd look good with a normal dress too."
    show dp 21
    reg "Yeah, I guess that's the problem now..."
    reg "It's not a costume. Just a... {i}normal{/i} dress."
    reg "At a costume party."
    reg "It feels weird."
    show dp 22
    p "*Passive-aggressive tone* Yeah... I used to have a good costume, remember?"
    p "But because of that “incident”..."
    show dp 23
    cha "OH. MY. GOD."
    show dp 24
    cha "Who cares if it's not a costume?!" with dis12
    cha "You look even better than in your pics!"
    p "Aw, thank you, cutie."
    mct "Hey... that's Charlotte, Axel's friend."
    mc "Charlotte?"
    show dp 26 with dis12
    cha "Huh?" with dissolve
    cha "Do I know you?"
    show dp 25
    mc "Come on, I've been in your class for weeks."with dis08
    mc "I'm [mc]. The new guy. Chang's friend."
    show dp 26
    cha "Ahh... yeah... what are you doing here?"with dis08
    show dp 25
    mc "I came with Penelope. I live with her, as part of the Student Exchange Program."with dis08
    mc "What about you? What are you doing here?"
    show dp 26
    cha "Uh... partying, duh."with dis08
    cha "And I wanted to see Penelope."
    cha "I'll be studying here next year, and she's {i}literally{/i} me, just... older."
    cha "If I have to be the new most popular girl at this university next year, I've gotta take notes from my predecessor."
    show dp 25
    mc "Um... you and her are nothing alike, but... whatever."with dis08
    mc "Where's Axel, by the way?"
    mc "I'm surprised you're not following him around like a puppy."
    show dp 27
    cha "Bah, don't talk to me about him."with dis
    cha "He's been ghosting me all week."
    cha "He doesn't come to school anymore, he doesn't reply to my messages, he's never online on his social media..."
    show dp 28
    mc "Wait, really?"
    mct "It's true, though... I haven't seen him since the fancy dinner in Eternum."
    mct "Hmm... I've gotta ask Alex, perhaps she knows more."
    mct "Maybe he's ill?"
    show dp 27
    cha "Chang turned out to be a fraud, Benjamin died, and now Axel vanished from school."
    cha "What a shitty school year thus far."
    show dp 28
    mc "Can't relate, to be honest. Mine's been the best one of my life, by far."
    play sound chair1
    show dp 29
    p "*Sitting next to you* Oh, really? And does that have something to do with us?"with dis14
    mc "*Chuckles* I'd say the Carters played a big role in that, yeah..."
    p "Ah, that makes me feel accomplished."
    show dp 21
    reg "I was gonna sit there, Penelope."
    show dp 30
    p "Oh, really? I'm sorry, I must have missed the “reserved” sign."
    p "I hope you don't mind."
    play sound2 chair1
    show dp 31
    reg "*Passive-aggressive tone* Of course not, girl." with dis12
    reg "We're all friends here, and there's plenty of space."
    show dp 32
    p "Yeah, we are..."
    show dp 31
    reg "Now let's get wasted!"
    reg "This is a party, and I have an entire bottle of Jager right here, ready to be drunk."
    reg "Just be careful when you're grabbing the cups, you wouldn’t want your straps to slip and suffer another wardrobe malfunction."
    show dp 32
    p "Any problem with my dress, sweetie?"
    show dp 31
    reg "Not at all, darling."
    reg "Very revealing. Definitely seems like {i}your{/i} style."
    show dp 32
    p "Thanks, Mom, I'll keep it in mind."
    mct "{i}Something{/i} tells me they don’t like each other much... I’d better not get in the middle of this."
    mc "*Clears throat* I want a cup!"
    stop music2b fadeout 5
    stop music3
    show black with dis2
    show screen afewminuteslater with dis
    pause
    play music2 party2 fadein 6
    scene dp 33
    hide screen afewminuteslater
    with dis22
    mc "*Laughs* W-What? Are you serious?"with dis08
    show dp 34
    mc "You're a teacher?!"with dis
    show dp 35
    co "Yeah, man."
    co "Teaching is like, my passion. And these students are my life."
    co "Just don't tell the dean I'm smoking in here."
    mc "*Chuckles* I won't, don't worry."
    show dp 36
    reg "Alright, guys, this was fun, but I wanna go dance before they turn out the lights."
    show dp 37
    cha "Hell yeah! Let's decimate the dance floor."
    show dp 36
    reg "We should play a game before going, though. To set the mood."
    show dp 38
    mc "Sure, sounds fun."
    show dp 36
    reg "Let's do one final round of Truth or Dare."
    reg "Each one of us can choose the person they want. If they don't answer the question or don't perform the dare, they have to drink 3 shots."
    show dp 37
    cha "I'm in!"
    show dp 51
    stu2 "Sure!"
    show dp 49
    p "Should be fun."
    show dp 36
    reg "Alright! I'll begin, then."
    reg "And I choose... [mc]."
    reg "Truth... or dare?"
    show dp 38
    mc "Um..."
    show dp 62
    menu:
        with dis
        "Truth":
            show dp 38
            mc "Truth."with dissolve
            show dp 46
            reg "Okay..."
            reg "Tell me, [mc], how {i}big{/i} are you?"
            show dp 46b
            mc "Um... do you mean..."
            show dp 46
            reg "You know what I mean."
            show dp 39
            mc "Uhh... I don't really know, honestly. I've never measured it."
            show dp 40
            reg "All men have."
            show dp 39
            mc "Well, not me."
            show dp 40
            reg "Give us a guess."
            show dp 39
            mc "Uh..."
            mc "Maybe like... 20 cm? 21?"
            show dp 41
            reg "How much is that?"
            show dp 39
            mc "Oh... like... 8 inches? 8.5?"
            p ". . ."
            show dp 63
            cha "W-What?"
            show dp 40
            reg "Come on, seriously."
            reg "If you're embarrassed to say it, you can drink instead."
            show dp 39
            mc "I'm serious. Why would I lie?"
            mc "If you have a measuring tape I can go to the bathroom and tell you the exact length, if you want."
            show dp 41
            reg "Wait... so you're not kidding?"
            show dp 39
            mc "Nope."
            show dp 41
            reg "Boy, you've gotta be the palest Blacked actor I've seen."
            reg "Holy fuck..."
            reg "I guess that's why Penelope likes you."
            show dp 50
            p "S-Shut up, Regina. I haven't even seen it yet."
            show dp 46
            reg "Yet?"
            show dp 47
            p "Uhh... I-I mean..."
            show dp 48
            p "Alright, who's next? Let's continue!"
        "[gr]Dare":
            $ dare1 = True
            show dp 38
            mc "Dare."with dissolve
            show dp 46
            reg "Okay..."
            reg "You have to kiss... Penelope on the neck."
            show dp 52
            mc "Ohh... this is the kind of dare I like." with dis
            show dp 53
            p "*Giggles* I bet you do."
            show dp 52
            mc "It's my time to shine."
            mc "Please, stand up, m'lady."
            show dp 42 with dis14
            mc "*Grabbing her by the waist* I love this dress, Penny."with dissolve
            mc "The incident with the beer doesn't seem like such a tragedy anymore."
            show dp 43
            p "Thanks. You... smell good."
            show dp 42
            mc "Ah, my $50 cologne is paying off already!"
            mc "Do you want to take a closer sniff?"
            show dp 43
            p "*Chuckles* Show me, stud."
            show dp 44 with dis15
            bla "You approach Penelope and start giving her small, gentle kisses on her neck, slowly moving up and down." with dis08
            p "(God, this is so hot.)"
            p "(I wonder if he's kissed many girls. He's really good at this...)"
            $ penelope_points += 1
            play sound beat
            show screen heartbeat
            show dp 45
            bla "You start alternating between tiny nibbles and wide kisses using your tongue, but making sure not to leave a hickey."with dis15
            p "Mmmm..."
            show dp 46b
            reg "(Huh, I thought she'd refuse. So the bitch really likes him, eh?)"
            reg "(Interesting...)"
            show dp 46
            reg "Okay, okay, that's enough!"
            reg "Stop before you get every girl in here all wet, Eros."
            play sound chair1
            show dp 52 with dis12
            mc "How did I do?"with dissolve
            show dp 53
            p "Not bad at all..."
            p "At least an 8. Maybe a 9."
            show dp 52
            mc "Hmm... I'll have to keep practicing, then. I need to achieve perfection."
            show dp 36
            reg "Okay, guys, let's continue playing!"with dis
            show dp 48
            p "Who's next?"
    show dp 36
    reg "Let’s go with you."
    reg "Choose someone."
    show dp 47
    p "Me?"
    show dp 48
    p "Mmmm..."with dissolve
    show dp 49
    p "I'll go with Professor Connor. He's still such a mystery to all of us."with dissolve
    p "Truth or dare, professor?"
    show dp 35
    co "Uh... imma go with truth."
    co "I'm too old for dares."
    show dp 49
    p "Okay..."
    p "There's a rumor that says that you slept with Dean Meyers. I need to know, is that true?"
    show dp 35
    co "*Laughs* If I answer that, my job would be at risk, Penelope."
    show dp 49
    p "Ah! Don't worry, that answered my question sufficiently."
    show dp 36
    reg "I won't be able to look at her the same way."
    show dp 35
    co "Let's keep this between us, guys."
    show dp 49
    p "Don't worry, sir, if no one snitched that you smoke joints during your lessons, no one will say a word about this either."
    show dp 35
    co "I appreciate it."
    show dp 37
    cha "Aight, it's my turn!"with dis08
    cha "I choose Penelope!"
    show dp 47
    p "Alright... I'm gonna say... truth."
    show dp 37
    cha "Okay!"
    cha "Here's my question: if you had to do a threesome with 2 people at this party right now, who would you choose?"
    show dp 47
    p "A t-threesome? And with someone in the university right now...?"
    cha "Yeah!"
    p "And do I have to say 2 boys?"
    show dp 37
    cha "Not necessarily. Whatever you'd like!"
    show dp 49
    p "*Giggles* Alright..."
    p "In that case I'm gonna say..."
    if novapath:
        p "Nova..."
        mct "Hot..."
        p "And..."
        show dp 40
        reg "Who's Nova?"
        show dp 38
        mc "You don't know her? She studies here too."
        mc "She usually wears an eyepatch, long curly ginger hair..."
        mc "You saw her by the entrance when we arrived!"
        show dp 51
        stu2 "Me? Ah, yeah, the girl cosplaying as Jinx, right?"
        mc "Yes!"
        show dp 63
        cha "What's a Jinx?"
        show dp 51
        stu2 "A character from League of Legends."
        cha "The fuck is League of Legends?"
        show dp 40
        reg "I remember that. Isn't it one of those ancient video games people used to play before Eternum came out?"
        show dp 38
        mc "Well, technically, she's cosplaying as Jinx from Arcane, the Netflix show, not the game."
        show dp 51
        stu2 "Did you see last season? It was crazy good!"
        stu2 "When Vi goes to the-"
        show dp 63
        cha "Whatever, I don't care."
        cha "Let's go back to my question. This Nova and...?"
    else:
        p "My friend Lily and..."
    show dp 48
    p "Hmm..."
    show dp 53 with dis12
    p "Who else could I say..."with dis08
    show dp 52
    mc "*Chuckles* I swear if you don't say my name, I'm gonna grab my things and go home."
    show dp 53
    p "*Snorts* Okay, okay, I'm gonna say [mc]."
    p "Just don't let it get to your head."
    show dp 52
    mc "Penelope Carter just said that she'd like to have a threesome with me. It's difficult not to be enthusiastic."
    show dp 53
    p "I had to say someone. It's just a game."
    show dp 52
    mc "*Chuckles* Hey, don't ruin my mood!"
    show dp 35
    reg "Okay, professor, it's your turn."with dis
    co "Oh, me?"
    co "I'm gonna choose... [mc]."
    co "I want to get to know my possible future students better."
    co "What is it gonna be, my boy?"
    show dp 62
    menu:
        with dis
        "Truth":
            show dp 38
            mc "Let's go with truth."with dissolve
            show dp 35
            co "Alright."
            co "I don't know what the deal is with you young kids these days, so let me ask you..."
            co "Have you ever made love to a girl during her bleeding days?"
            show dp 34
            mc "Damn!"
            mc "Uh... no, never have, no."
            show dp 53
            p "Would you do it, though?" with dis12
            show dp 52
            mc "Have sex with a girl on her period?"
            p "Mm-hm."
            show dp 53
            p "A girl comes to you horny as fuck wanting to give you the ride of your life, but she says she's on her period. What would you say?"
            show dp 52
            mc "I'd say..."
            menu:
                with dis
                "Let's do it":
                    mc "You better have a spare change of sheets, girl, because we're gonna leave a big fucking mess..."with dis06
                    show dp 53
                    p "*Snorts* You're a dirty, horny, fucking dog."
                    show dp 52
                    mc "I'm not scared to get my hands dirty."
                    mc "And what's not to like? Extra lube and I get to fulfill my vampire fantasies."
                    mc "My future self would worry about the cleaning."
                    mc "Don't you like to get carried away sometimes?"
                    show dp 53
                    p "Can't say I don't like to sometimes, yeah..."
                "No, thanks":
                    mc "I'd politely decline and arrange a new meeting."with dissolve
                    mc "I'm a gentleman. I’d set up a time where we can both be satisfied. And maybe throw in a little extra for missing the first appointment."
                    show dp 53
                    p "Oh my, chivalry isn't dead after all..."
                    show dp 52
                    mc "Not while I'm still around."
        "[gr]Dare":
            $ dare2 = True
            show dp 38
            mc "Let's go with dare."with dissolve
            show dp 35
            co "Good choice."
            show dp 54
            co "[mc], I dare you to eat one of my magic mushrooms."with dis
            mc "*Laughs* Magic mushrooms?"
            co "Hand-picked in the Brazilian Amazon. Eating a few of them can take you on a trip that some people describe as a religious experience."
            co "The indigenous people claimed they allowed you to get in touch with your own soul and even speak with the gods."
            show dp 34
            mc "Um... I appreciate it, but I think I'm gonna pass."
            show dp 54
            co "Don't worry, just eat one."
            co "The effects are immediate, but only last a couple of minutes, at most."
            co "You'll see more vibrant colors and deeper shadows. You’ll feel more relaxed during that time, and after that there are no side effects."
            mc "Uh... well, okay then, in that case... I'll try it."
            show dp 55
            mc "And I have to eat it all at once?"with dis12
            show dp 35
            co "Yes, sir. Just eat it, close your eyes, and count to ten."
            show dp 55
            mc "Alright, I guess I can trust a professor of the University of Kredon."
            show dp 56
            mc "Aaaah..." with dis08
            play sound ["<silence 0.4>", swallow] volume 1.5
            show dp 57
            bla "You swallow the mushroom without chewing."with dis08
            co "Now keep your eyes closed for a minute and let your mind go blank."
            stop music2 fadeout 9
            stop soundloop fadeout 9
            play music2b trance fadein 50
            show dp 58 with dis2
            mct "Hmm, it's true that I feel something." with dis
            mct "Like a... slight dizziness."
            mct "How can it take effect so fast, though? Maybe it's absorbed through the taste buds?"
            mct "Hmm, well, it doesn't seem to be anything I can't handle so far."
            co "You can open your eyes."
            show dp 59 with dis2
            mc "*Taking a deep breath* Hmm..."with dis
            p "Do you feel anything different, [mc]?"
            show dp 60 with dis
            pause
            scene mush1 with dis22
            mcd "Uh..."with dis
            mcd "T-This feels a bit stronger than what you told me, Professor."
            scene mush2
            cod "Yeah, the first time always hits a bit harder."
            cod "But after a while it barely affects you."
            cod "We used to eat dozens of them every night when I was young."
            scene mush1
            pd "Do you want a glass of water, [mc]?"
            mcd "N-No..."
            mcd "I'm fine, actually! Haha!"
            pd "Oh... well, alright, then."
            mcd "Your tits look huuuuuge with this dress, Penny, did I tell you?"
            mcd "They're moving with such a hypnotic dance..."
            pd "...Moving?"
            scene mush3
            regd "Haha, is he really hallucinating?"
            mcd "H-Hey, your tits are dancing too, Regina."
            regd "I wanna try one of these mushrooms."
            mcd "I wouldn't recommend it, honestly."
            mcd "It feels waaaaay too trippy."
            scene mush4
            mcd "How long did you say the effects lasted, Professor Connor?"with dis
            mcd "Huh...?"
            mcd "Heeeyy..."
            mcd "Where did everyone go?"
            mcd "Is the party over already?"
            scene mush5
            show mush6
            mcd "I guess we're alone now, Penny..."with dis
            mcd "Oh..."
            mcd "Haha, now I see you with your Idriel costume again!"
            mcd "Crazy..."
            hide mush6
            id "{move}You need to go back, [mc].{/move}"with dis
            mcd "W-What?"
            mcd "You have her voice too..."
            id "{move}Eternum is calling you.{/move}"
            mcd "Wait... what is going on..."
            if lunapath:
                mcd "Is this the bleeding effect again? Like the gas station with Luna?"
            play sound glitch4
            scene mush7
            id "{sc=2}You have to remember.{/sc}" with flashfaster
            mcd "AAAAAH!"
            mcd "Aww shit, I might need that glass of water now, Penny."
            id "{sc=2}They need your help, [mc].{/sc}"
            mcd "W-What? Who?"
            id "{sc=2}If you had to toss a coin a hundred times...{/sc}"
            id "{sc=2}And it came up heads 99 times...{/sc}"
            id "{sc=2}What would you bet on for the last throw?{/sc}"
            mcd "What? This again?"
            id "{sc=2}What would you bet on?{/sc}"
            menu:
                mcd "Uh..."
                with dis
                "{sc=2}Heads{/sc}":
                    mcd "Heads again, of course." with dissolve
                    id "{sc=2}You still don't understand, [mc].{/sc}"
                "{sc=2}[gr]Tails{/sc}":
                    $ tailscoin2 = True
                    mcd "Tails." with dissolve
                    id "{sc=2}You’re beginning to understand, [mc].{/sc}"
            id "{sc=2}You must look beyond.{/sc}"
            id "{sc=2}Break. The. Chain.{/sc}"
            play sound glitch4
            stop music2b
            play music2 party2
            scene dp 61
            mc "AAAH!" with flashfaster
            mc "W-What the fuck?!"
            p "Are you okay, [mc]?"
            mc "*Laughs* I mean... y-yeah, I am!"
            mc "This shit is insane!"
            mc "Holy fuck, what a trip. I saw tons of colors and weird shit."
            show dp 35
            mc "You're a crazy bastard, Connor."
            co "*Laughs* I get that a lot."
            co "Before you ask, I don't have any more magic mushrooms, I'm sorry."
            mc "*Chuckles* I wasn't planning to eat any more, don't worry."
            show dp 46
            reg "Are you good to continue, then?"
            show dp 46b
            mc "S-Sure!"
            play sound2 swallow2
            mc "*Taking a sip* I just need another shot to get back to reality."
    show dp 51
    stu2 "My turn, my turn!"with dis
    stu2 "I wanna ask Penelope!"
    show dp 40
    reg "*Sighs* How original."
    show dp 47
    p "Uh... I'm gonna say truth again..."
    show dp 51
    stu2 "That works!"
    stu2 "I wanna ask..."
    stu2 "Where is the weirdest place you've ever jilled off?!"
    show dp 48
    p "Jilled off?"
    show dp 49
    p "Uh... I should stop drinking before I reveal something I shouldn't..."with dissolve
    show dp 52
    mc "Nonsense." with dis
    mc "You're doing fine."
    mc "And I really wanna hear that story."
    show dp 53
    p "*Giggles* Okay... but I'll keep it short."
    p "I guess it was probably... in a jacuzzi."
    show dp 52
    mc "Oh. That's hot."
    mc "Nothing out of the ordinary, though."
    show dp 53
    p "Well... I was in the jacuzzi with Mom and Dalia."
    show dp 52
    mc "OKAY, now this is getting interesting..."
    mc "Can you go into specifics?"
    show dp 53
    p "The three of us went to a spa like 3 years ago, for my 18th birthday."
    p "There was this hot tub in the women's baths, and we were all chilling there, relaxing in the water."
    p "Then I put my legs over the side of the hot tub in an attempt to get more comfortable and... I found a water jet."
    show dp 52
    mc "Oh god..."
    show dp 53
    p "*Giggles* I knew I should have stopped, but god, it just felt too good..."
    p "I orgasmed 2 times without any of them noticing. I had to cover my mouth with my hands."
    show dp 52
    mc "Oh my, that's so fucking HOT."
    mc "Can't wait to tell Dalia and Nancy..."
    show dp 53
    p "*Snorts* I'd kill you."
    show dp 40
    reg "Okay, okay, fascinating story."with dis
    reg "Lots of questions, and very few dares."
    reg "Booooring."
    show dp 41
    reg "There's only [mc] left, so let's do only dares now!"with dis
    reg "I don't know about you, but I think people in this party are wearing way too many clothes..."
    show dp 46b
    mc "You're not wrong there, Regina..."with dis
    show dp 46
    reg "So... who are you daring?"
    show dp 62
    mc "Hmm..."with dis
    menu:
        with dis
        "Penelope{#0.5,dare}":
            $ dare3 = True
            show dp 52
            mc "*Looking at Penelope* Who could I choose..."with dis
            bla "You stare directly at Penelope's huge attributes."
            show dp 53
            p "I'm not gonna get naked in front of everyone, [mc]."
            show dp 52
            mc "Not naked, the dare is just flashing your tits."
            show dp 53
            p "Not now, and not with 10 more beers."
            show dp 52
            mc "Let me finish!"
            mc "AND not in front of everyone. You have to flash your tits to someone. The person you choose."
            mc "Someone sitting around this table."
            show dp 53
            p "Ah, of course..."
            p "And I can choose?"
            show dp 52
            mc "Totally up to you."
            p "Mm-hm..."
            show dp 53
            p "Okay, I can do that."
            p "And I'm gonna choose Charlotte."
            show dp 63
            cha "What?! Really?"
            show dp 52
            mc "*Laughs* You're not really gonna do this to me, right?"
            show dp 53
            p "I feel more comfortable doing something like this with a girl. Nothing personal."
            show dp 52
            mc "*Chuckles* You're enjoying teasing me so much tonight, aren't you?"
            show dp 53
            p "*Giggles* You don't know how much."
            show dp 76
            bla "Penelope stands up and goes with Charlotte to a corner of the classroom." with dis17
            p "*Giggles* God, I can't believe I'm really doing this."
            show dp 77
            cha "Don't worry, I know what it’s like to be the most popular girl in school. Everyone wants to see you naked. Everyone wants to be with you."
            cha "You chose the right person."
            show dp 76
            p "Alright, there we go. A dare is a dare..."
            play sound clothes4 volume 1.3
            show dp 78 with dis14
            pause 0.5
            mct "Aw man, I wish I could be on the other side..."with dis06
            mct "She's not even wearing a bra..."
            play sound2 clothes4
            show dp 79
            p "*Putting the top of her dress back on* Oh god, this was embarrassing!"with dis
            show dp 80 with dis15
            play sound3 chair1
            p "*Sitting down* Alright, I guess this ends the game."with dis06
            cha ". . ."
            cha "H-How can they be so big and so perky at the same time? W-why doesn't gravity affect her?"
            cha "What cruel fate is this...?"
        "Regina [red][mt](Penelope -1){#0.5,dare}":
            show dp 46b
            mc "I'm gonna choose... you, Regina."with dis
            mc "And here's my dare: You have to flash your tits."
            show dp 46
            reg "Hah. In front of everyone?"
            show dp 46b
            mc "Oh, no, just... in front of the person you choose."
            show dp 46
            reg "The person I choose, huh?"
            show dp 46b
            mc "Mm-hm."
            show dp 46
            reg "*Giggles* Alright, cutie, let's go to that corner."
            show dp 46b
            mc "Oh shit, are you gonna do it?"
            show dp 46
            reg "A dare is a dare..."
            show dp 70
            bla "Regina stands up and goes with you to a corner of the classroom." with dis17
            reg "You're such a pervert, [mc], did you know that?"
            show dp 71
            mc "Hey, it was you who complained that the game was getting boring."
            show dp 70
            reg "Touché." (what_style='textsp')
            play soundlow zip volume 0.4
            play sound2 ["<silence 0.1>", clothes4] volume 1.4
            play sound3 ["<silence 0.2>", buttons]
            show dp 72
            bla "Regina unzips her vest and takes it off entirely." with dis17
            show dp 73
            mc "Goddammit..."with dis
            show dp 74
            reg "Enjoying what you see?"
            show dp 73
            mc "Very much, yes..."
            mc "Can I touch?"
            show dp 74
            reg "Oh my, this boy sounds thirsty!"
            show dp 75
            p "What is he supposed to do when you're practically putting your boobs in his face?"
            show dp 74
            reg "Someone sounds jealous..."
            show dp 75
            p "Jealous of a skank showing her tits to a guy she’s known for an hour?? Not really, no."
            show dp 73
            mc "You're hot, Regina. And your nipples are so pointy..."
            show dp 74
            reg "Thank you, [mc]."
            reg "We have to leave it here for now, but... let’s see where the night takes us."
            show dp 75
            p "Are you done back there? I wanna leave for the dance floor already."
            p "I guess this ends the game, doesn't it?"
            play sound chair1
            show dp 36
            reg "*Sitting down* Yes, it does."with dis15
            $ penelope_points -= 1
        "Charlotte":
            show dp 37b
            mc "I'm gonna go with Charlotte."with dis
            mc "And here's my dare: You have to flash your tits!"
            show dp 63
            cha "Excuse me? In front of everyone? I'm not doing that."with dis
            mc "No, not in front of everyone. Just one person."
            show dp 37
            cha "Ah, I see where this is going..." with dis
            cha "You want to see the most popular girl in school naked."
            cha "The classic nerd fantasy."
            cha "Alright, [mc]... I'm drunk, and it's your lucky day."
            cha "Let's do it."
            show dp 64
            bla "Charlotte stands up and goes with you to a corner of the classroom." with dis17
            cha "Okay, [mc]... I'll let it pass for now because you're kinda cute, but if you tell anyone at school about this, I'll ruin your life. Understood?"
            mc "Mm-hm."
            play sound clothes4 volume 1.4
            show dp 66
            bla "Charlotte lifts her top to leave her boobs exposed."with dis12
            cha "*Giggles* Enjoy the view."
            mc ". . ."
            show dp 67
            mc ". . ."with dis12
            mct "Jesus Christ, why do they sag so much?"
            mct "They almost hang down to her belly button. And are those... wrinkles??"
            show dp 68
            cha "*Going back to the couch* Okay, okay!" with dis12
            cha "That's enough!"
            cha "*Giggles* You're welcome for the dreams you're gonna have about this!"
            show dp 69
            mc "*Shivers* (Oh god, I really fucking hope not.)"with dis08
            mct "It would be my worst nightmare."
            mct "I won't doubt Dalia and Alex ever again."
            show dp 75
            p "I guess this ends the game, doesn't it?"
            show dp 36
            reg "Yes, it does."
    stop music2 fadeout 6
    play soundloop partywalla fadein 7
    play music2b partypenny fadein 7
    play music3 partyfar
    show dp 35
    co "This was fun, kids."with dis12
    co "These parties always make me feel young again."
    show dp 36
    reg "Thank you for joining us, Professor."
    show dp 40
    reg "And again, sorry for losing this cohort's yearbook, on behalf of all students."
    show dp 35
    co "No worries... it's all good."
    show dp 50
    p "Thank you for reminding us about the missing yearbook every day, Regina."
    show dp 46
    reg "It's the least I can do."
    show dp 46b
    mc "Hmm?"
    mc "A yearbook? What's this about?"
    show dp 50
    p "The University of Kredon has this tradition where they publish a yearbook with photos, signatures and notes from all the students."
    p "It’s passed from hand to hand until everyone has added something."
    show dp 36
    reg "And Penelope lost it."
    show dp 50
    p "Someone stole it from my bag."
    show dp 36
    reg "Don't worry, sweetie, no one is holding it against you."
    reg "Being a little forgetful isn’t the worst thing in the world. Besides, it fits with the old ditsy blonde stereotype, haha."
    show dp 50
    p "SOMEONE STOLE IT."
    show dp 46
    reg "Whatever you say..."
    reg "Anyway, I'll go see what music's playing in the main hall."
    reg "See y’all later!"
    show dp 37
    cha "I'm going with you!"
    stu2 "Me too!"
    play sound chair2
    show dp 81
    p "*Standing up* Yeah, I think I'm gonna head back home now."with dis12
    show dp 82
    mc "Really? So quickly?"
    mc "*Looking at your phone* Oh, damn, it's 2:30 AM already. Time really flew by."
    if novapath:
        mc "Alright then, let's go look for Nova and head back home!"
    else:
        mc "Alright then, let's go back home!"
    show dp 81
    p "No, no, don't worry, you can stay."
    p "I'll see you at home."
    show dp 82
    mc "No way I'm staying here without you."
    mc "You're the reason I came in the first place."
    show dp 81
    p "Seriously, stay."
    p "I just feel like taking the scenic route on the way home."
    p "I don't mind, really."
    show dp 82
    mc ". . ."
    mc "Scenic route? At 2:30 AM? I know you well enough to know you're up to something."
    show dp 81
    p "I'm not up to anything. I’m a good girl."
    show dp 82
    mc "Penny..."
    p ". . ."
    show dp 83
    p "Okay, it's about that damn yearbook." with dis
    show dp 84
    mc "I knew it!"
    show dp 83
    p "I KNOW it was Regina who stole it to make me look bad."
    p "She's been fucking with me all year. All 3 years of college, really!"
    p "I'm going to her dorm to retrieve it. It has to be there."
    show dp 84
    mc "Why are you so certain that she has it?"
    show dp 83
    p "Well... I have no evidence, but I have a gut feeling."
    p "I know it was her. I saw her sneering smirk when the dean chastised me about losing the book."
    p "And if it's not there... I'm sure I’ll find a clue or something."
    show dp 84
    menu:
        with dis
        "[gr]Help her":
            mc "Come on, Penny." with dis06
            mc "Whether she took it or not... do you really think revenge gets you anywhere?"
            show dp 83
            p "Yes."
            show dp 84
            mc "Yeah, I’m fucking with you, I don’t like that girl either."
            mc "I don’t think taking the high road will work on someone like her."
            mc "Let's get that bitch."
            show dp 86
            p "*Giggles* I knew I could count on you." with dis
            mc "Always."
            mc "And be honest... you like it when I play the bad boy."
            p "*Giggles* I'll admit it's kinda sexy."
            mc "What's the plan, then?"
            p "Meet me by the stairs of the main hall."
            p "The dorm building is right beside the one we're in right now."
            mc "Gotcha. See you there!"
            show dp 13 with dis2
            mct "Oh boy, I got up too fast... my head's spinning." with dis06
            if novapath and dare2 and novadildo:
                mct "Between beers, Akira's wine, shots, long drinks, and those damn mushrooms..."
            elif novapath and novadildo:
                mct "Between beers, Akira's wine, shots, and long drinks..."
            else:
                mct "Between beers, shots, and long drinks..."
            mct "My stomach is begging for a break."
            mct "Only water until next month..."
            reg "Where are you going so fast?"
            show dp 87
            mc "Hmm?" with dis
            mc "Oh, I thought you left to dance."
            show dp 88
            reg "I thought of a better activity."
            show dp 87
            mc "A better activity?"
            show dp 88
            reg "Something we could both do... together."
            show dp 87
            mc "What do you mean...?"
            show dp 88
            reg "Well, you can continue following Penelope like a puppy, like everyone else, doing what she wants and telling her how pretty she is all the time..."
            reg "Or you can come with me to the locker room and do something you’ll never forget."
            show dp 87
            mc "Uh... are you proposing that we..."
            show dp 88
            reg "You're hot, [mc]. I’m hot. And... I'm horny."
            reg "Let's just enjoy this party together."
            reg "What do you say?"
            show dp 87
            mc "Um... just to be clear, when you say “something you’ll never forget”, do you mean..."
            show dp 88
            reg "I mean that I'd let you fuck me so hard that I’d need a walking stick tomorrow."
            show dp 87
            mc "*Gulps* Damn."
            show dp 88
            reg "10 minutes. You and me. The locker room. And Penelope won’t find out, don't worry."
            reg "I'll be there waiting for you..."
            play sound doorold
            show dp 1 with dis17
            mct "Damn..." with dis06
            mct "Regina wants to shag me! I'm getting real lucky with the ladies this year."
            mct "Now I can score with college ladies without even trying!"
            mct "Maybe this new cologne really is the chick magnet it was advertised as."
            mod "Going to the locker room will close Penelope's path."
            call screen collegeparty6 with dis
        "Discourage her from doing it":
            mc "Come on, Penny." with dis06
            mc "We're better than that."
            mc "Whether she really took it or not... revenge gets you nowhere."
            show dp 85
            p "Baaaahh, really?" with dis
            p "Don't be such a bore! Where did you leave your spine, [mc]?"
            mc "I don't need to play the bad boy."
            mc "And neither do you. It doesn't suit you."
            p "You used to be way cooler..."
            show dp 81
            p "*Sighs* But you're probably right. I’m just being too rash."with dis
            p "I guess I'll go home for real."
            show dp 82
            mc "You made the right decision."
            show dp 81
            p "If you still want to accompany me..."
            show dp 82
            mc "*Chuckles* Gladly."
            $ penelopepath = False
            $ penelopeu = False
            if novapath:
                mc "Let's go find Nova."
                stop music2b fadeout 3
                jump leavingparty
            else:
                jump leavingparty2
label reginalockerfail:
    scene dlc 1
    show screen heart
    with dis14
    mct "Alright... the locker room." with dis08
    mct "I have a few minutes before Penelope or Nova start missing me..."
    mct "I wonder if Regina was actually serious or if she was just messing with me."
    reg "Hi, handsome."
    show dlc 3
    bla "You turn around and see Regina standing behind you, swaying her hips in a slow, sensual way."with dis12
    mc "Oh boy..."
    mct "I guess she was serious after all..."
    mc "Looking good, Regina."
    show dlc 2
    reg "Thank you... you too."
    show dlc 3
    mc "So... tell me, what did you have in mind?"
    show dlc 2
    reg "Oh my, wasn't I sufficiently clear?"
    reg "I want you to fuck me, [mc]."
    show dlc 3
    mc "Oh fuck yes..."
    show dlc 2
    reg "We don't have much time, though..."
    reg "You'll have to strive for it."
    reg "Just... don't worry about me."
    reg "I can handle... {i}anything..."
    show dlc 3
    mc "O-Oh god... I'm gonna make a mess out of you."
    mc "Come here, baby..."
    show dlc 4
    reg "Ah, ah, ah, not so fast!"with dis
    reg "I want you to get naked for me first."
    reg "Let's see what you're hiding under there..."
    mc "With pleasure..."
    play sound clothes3
    play sound2 clothes4
    show dlc 3
    bla "You hastily remove your robes and throw them against the wall. Your cock starts getting hard in anticipation."with dis14
    show dlc 5
    reg "Jesus fucking Christ..." with dis12
    if not dare1:
        reg "You really weren't kidding during the truth or dare game..."
    reg "I can see why Penny is so interested in you..."
    mc "To be fair she hasn't even seen me naked yet."
    if pennyshower:
        mc "Well, not hard, at least."
    mc "But... wait, she's {i}interested{/i}?"
    mc "What do you know? Did she tell you anything?"
    show dlc 2
    reg "Don't get distracted on me now, boy."with dis
    reg "Do you want me to milk that cock of yours or not?"
    show dlc 3
    mc "Oh, fuck yes, I do..."
    show dlc 4
    reg "Turn around then..."with dis
    mc "What for?"
    reg "Trust me, no one has ever done something like this to you before..."
    show dlc 1
    bla "You do as Regina says and turn around."with dis12
    mc "Oh my god..."
    reg "The question here is, do you really know how to make a girl roll her eyes upwards?"
    reg "A big dick is good for nothing if you don't know how to use it."
    mc "Oh, trust me, you're gonna..."
    play sound phonecamera
    play sound2 ["<silence 0.3>", phonecamera]
    play sound3 ["<silence 0.8>", phonecamera]
    bla "You hear the sound of a phone taking pictures."
    mc "Huh...?"
    show dlc 7
    mc "*Turning around* What the hell..." with dis12
    play sound phonecamera
    play sound2 ["<silence 0.3>", phonecamera]
    play sound3 ["<silence 0.8>", phonecamera]
    show dlc 6
    reg "Damn boy, what an erection. You really were horny, eh?"with dissolve
    show dlc 7
    mc "What the fuck are you doing?!"
    show dlc 6
    reg "Taking pictures of you."
    show dlc 7
    mc "What for?"
    show dlc 6
    reg "To send them to Penelope."
    show dlc 7
    mc "What?!"
    mc "Are you out of your fucking mind?!"with hpunch
    mc "You told me she wouldn't find out about this!"
    show dlc 6
    reg "*Snorts* Yeah, well, I also said we were gonna fuck and we're not gonna, so..."
    show dlc 7
    mc "You're a fucking bitch!"with hpunch
    mc "Why are you doing this?!"
    show dlc 6
    reg "I could explain it to you, but if you have to ask that you're too stupid to understand it. And I don't really have the time."
    show dlc 2
    reg "It was fun, though."with dis
    reg "Think of this as... your freshman initiation prank! You just got one a year earlier. Lucky you!"
    show dlc 3
    mc "You're such a cunt."
    show dlc 2
    reg "*Snorts* Whatever, I'll let you get on with your things."
    show dlc 8
    reg "*Giggles* God, can't wait to see Penelope's face!"with dis12
    reg "Take care, [mc], I'll see you around."
    reg "Welcome to the University of Kredon!"
    show dlc 9 with dis15
    play sound doorclose2 volume 0.7
    mct "Aw, man..."with dissolve
    mct "What a mess."
    mct "Thinking about it, though... I {i}really{/i} was stupid."
    mct "Goddammit, [mc]."
    mc "*Sighs* (I should get out of here and go look for Penny.)"
    $ pennyreginahate = True
    scene df 135 with dis17
    call screen collegeparty5 with dis



label pennydormscene:
    scene dpp 2
    show screen heart
    with dis15
    mc "Hello there!"with dis08
    mc "I couldn't help noticing you were sitting here all alone, babe."
    mc "Can I buy you a drink?"
    show dpp 3
    p "*Giggles* I'm sorry, I'm waiting for someone."with dissolve
    show dpp 4
    mc "Oh, my bad."
    mc "Your boyfriend, I'm guessing?"
    show dpp 3
    p "Not really, no..."
    p "Just a friend who's gonna help me sneak into the dorm room of someone who stole something from me."
    p "A mission to regain my honor, you could say."
    show dpp 4
    mc "Oh, damn, that sounds exciting! That guy sounds like a real Prince Charming!"
    mc "I don’t see him anywhere though..."
    mc "You know what? I'll help you."
    mc "Fuck that dude you were waiting for, whoever he was."
    show dpp 3
    p "*Giggles* Alright... I like you, mysterious stranger."
    p "I accept your help."
    show dpp 4
    mc "*Chuckles* Do you know where Regina’s dorm is?"
    show dpp 3
    p "Yeah, it's in a dorm building by the entrance of the campus."
    p "Most people will be at the party right now, and the ones who didn't come or left already must be sleeping or hooking up, so... we should have free rein."
    show dpp 4
    mc "Alright then, let's go!"
    mc "You lead the way."
    stop soundloop fadeout 5
    stop music2b fadeout 5
    scene black with dis2
    show screen afewminuteslater with dis
    pause
    play sound doorold
    play music sneaky5 fadein 7
    show dpp 5
    hide screen afewminuteslater
    with dis2
    mc "Hmm, you were right, there's no one here." with dis
    p "Told you!"
    p "And we'll have returned to the party before anyone misses us. It's the perfect crime."
    mc "Which one’s Regina's room?"
    show dpp 6
    p "It's the second door on the left. People here don't lock doors when they're out partying because they usually come back drunk as skunks."with dis12
    mc "You seem to know a lot about these dorms."
    p "Yeah, I used to stay over at my friend Lily’s dorm during finals weeks or longer parties."
    p "I also looked into them before starting college, but having Mom's house less than 30 minutes away? No chance!"
    p "And I know we're always at each other's throats, but I'm sure Dalia would miss me too much."
    mc "And wouldn't you miss her as well?"
    p "Uh..."
    p "Honestly?"
    p "A lot. More than what I'd ever admit in front of her."
    mc "*Chuckles* (They're more alike than they realize.)"
    show dpp 7 with dis15
    p "*Whispering* Now quiet." with dissolve
    p "*Whispering* We don't know if her roommate is in the room."
    mc "*Whispering* Is it this one?"
    p "*Whispering* Yeah."
    p "*Whispering* But I don't hear anything. I think it's empty."
    p "*Whispering* Let's just shoot for it."
    mc "*Whispering* I got your back."
    play sound dooropen1
    play sound2 ["<silence 0.3>", doorsqueakk]
    show dpp 8 with dis15
    p "Nice! It's empty!"with dissolve
    mc "Sweet!"
    play sound3 switch
    show dpp 9
    p "*Turning the light on* Okay, I'll lock the door from the inside, just in case." with Dissolve(.1)
    p "Take a look at drawers and shelves, the yearbook has to be here!"
    show dpp 10
    mc "Hmm..." with dis12
    mc "Regina's room looks way more “girly” than I imagined."
    mc "Maybe it's because of her roommate?"
    p "I doubt it. She just does this because it's what sells on social media nowadays."
    p "*Puffs* I mean, look at this."
    show dpp 11
    p "{i}“Not all those who wander are lost.”"with dis
    p "{i}“Do more of what makes you happy.”"
    p "{i}“Believe in your dreams. They know the way.”"
    p "Wow... those are some inspirational lines!"
    p "I've just heard them..."
    show dpp 12
    p "...like a thousand times before." with dis08
    p "Find a new source to steal quotes from, Regina."
    p "Maybe if you were a bit more original, you'd get those followers you yearn for."
    show dpp 12b
    mc "Original, huh?"
    play sound pop
    show catto
    mc "Something like the pic of Carolyn wearing a mini witch hat that you posted the other day?"
    mc "Is that the key to being a successful influencer?"
    scene dpp 13
    p "*Laughs* More or less, yeah."with dis
    p "Can you believe that became one of my most liked pics?"
    show dpp 14
    mc "Carolyn is just too photogenic."
    mc "It was such a great pic. Probably my favorite of yours."
    mc "I mean from the ones on your Instagram profile, of course."
    mc "My absolute favorites are still the ones from our private session..."
    show dpp 13b
    p "Hah. I bet they are..."
    p "Maybe we'll have to do another photo shoot some day."
    show dpp 14
    mc "Nothing would please me more..."
    show dpp 13b
    p "We might not be able to use the studio this time, after the Valentino incident."
    p "We’d probably have to settle for another one, or just shoot at the house. I have a pretty good spot set up in my bedroom, too..."
    show dpp 14
    mc "Sounds good..."
    show dpp 13b
    p "All in good time, though."
    p "Let's do what we came to do."
    show dpp 14
    mc "Y-Yeah, of course!"
    show dpp 15
    p "Someone could appear at any moment, so we should leave this place ASAP."with dis12
    p "Take a look at that bookcase over there, I'll go through the drawers."
    mc "On it!"
    show dpp 16
    mc "*Squatting* What exactly are we looking for?"with dis12
    p "Uhh... well, it looks like any other book. Like... a foot long, brown cover."
    mc "There're only normal books here."
    mc "“If it fits, I sits”? Hmmmm..."
    p "I have that book! It's a phrase used as a caption for photos of cats sitting in unusual locations."
    mc "Oh. I'll admit that's not what was running through my head..."
    play sound chair4
    show dpp 17
    p "*Kneeling down* [mc]! Look at this!" with dis
    p "This drawer has a lock on it!"
    show dpp 18
    mc "Hmm..." with dis12
    p "They must keep all their valuable things here."
    p "The yearbook has to be there!"
    show dpp 19
    mc "So... dead end?" with dissolve
    show dpp 19b
    p "What do you mean? We just have to open it!"
    show dpp 19
    mc "How?"
    show dpp 19b
    p "Uhh... aren't you like, super strong? Can't you just rip it out?"
    show dpp 19
    mc "...I don't think I can."
    show dpp 19b
    p "Maybe using a crowbar?"
    show dpp 19
    mc "Or... we could take the entire drawer."
    mc "And then open it at home."
    show dpp 19b
    p "Interesting..."
    p "That might be the best option."
    p "Can you rip the entire drawer out?"
    show dpp 19
    mc "I can try."
    show dpp 19b
    p "Let's do it."
    play sound doorlocked volume 1.4
    show dpp 20 with dis12
    pause .2
    reg "What?"with dis08
    reg "Goddammit, Bella locked the door again?"
    reg "*Sighs* Now where the fuck did I put my keys..."
    play sound clothes4
    show dpp 21
    p "*Whispering* F-fuck, Regina's back!"with dis
    show dpp 22
    mc "*Whispering* What is she doing here?! The party isn't over yet!"
    show dpp 21
    p "*Whispering* I don't know, maybe she came back to grab something."
    p "*Whispering* S-She can't find us here, [mc]!"
    p "*Whispering* She's friends with the dean, she'll get me expelled and bar you from getting into this university next year!"
    show dpp 22
    mc "*Whispering* Shit, w-what do we do?"
    show dpp 23
    p "*Whispering* T-The window!"with dis08
    p "*Whispering* Let's jump!"
    mc "*Whispering* Are you crazy?! It's the third floor!"
    show dpp 24
    p "*Whispering* T-Then let's hide inside the wardrobe!"with dis08
    mc "*Whispering* But that shit is too small!"
    p "*Whispering* Then crouch down! Please!"
    mc "*Whispering* But–"
    play sound dooropen1
    play sound2 ["<silence 0.3>", doorsqueakk]
    show dpp 25 with dis15
    reg "Huh??" with dis06
    reg "What the hell?"
    show dpp 9
    reg "She even left the lights on."
    reg "What a mess."
    show dpp 26
    reg "(Anyway, let's get rid of that shit.)"with dis
    reg "(That bitch is beginning to suspect.)"
    play sound3 drawer
    show dpp 27
    bla "Regina opens the drawer and takes out a book from inside."with dis14
    reg "(I'll just dump it in the river or something before someone finds it.)"
    p "*Whispering* I knew it!" with hpunch
    show dpp 32
    p "*Whispering* That's the yearbook! I knew it was her who took it!" with dis
    p "*Whispering* Fucking cunt."
    mct "God, this is such an awkward pose."
    mct "Although... Penny's literally resting her butt against my hips. I don't have any complaints there."
    play sound chair4
    show dpp 29
    reg "*Sitting down* (I can't believe I just got stood up.)" with dis
    reg "(Everyone's just a bunch of ass-kissers.)"
    show dpp 32
    p "*Whispering* Tsk, is she really gonna use her phone now?"
    mct "She smells so good..."
    show dpp 30
    p "*Whispering* I'm sorry I dragged you into this, [mc]."with dissolve
    p "*Whispering* Are you okay back there?"
    show dpp 31
    mc "*Whispering* Y-Yeah, I'll have some soreness tomorrow from holding this pose for too long, and some hanger's poking me in the back, but..."with dissolve
    mc "*Whispering* Apart from that, I'm good."
    show dpp 29
    reg "(Hmm, Ginny uploaded a photo of herself from tonight.)"
    reg "(Look at how everyone is drooling in the comments.)"
    reg "(Bunch of retards.)"
    show dpp 32
    p "*Whispering* Come on, leave already..."
    mct "Fuck, Penny’s ass is getting me hard."
    mct "If I don't move she shouldn't notice it in this pose, though."
    mct "Please, don't move..."
    show dpp 29
    reg "(Bah, let's go back to the party.)"
    play sound chair3
    show dpp 27
    reg "*Stands up* (But let's get rid of this thing first.)"with dis
    reg "Say goodbye to your reputation, Penny."
    play sound2 ["<silence 0.6>", doorclose]
    show dpp 20 with dis12
    pause
    show dpp 30
    p "Finally! I think she left, [mc]!"with dis
    p "Phew, that was close!"
    show dpp 31
    mc "C-Cool, just be careful when going out, there's a..."with dissolve
    stop music fadeout 6
    play musicb night fadein 6
    play sound2 dooropen2
    play sound doorsqueakk
    show dpp 33
    p "*Opens the wardrobe door* O-Oh SHIT!" with dis08
    mc "B-Be careful with–"
    play sound fall2 volume 1.4
    play sound2 fall
    play sound3 fall3
    scene dpp 34 with vpunch
    pause 0.9
    mc "Ouch..." with dis
    mc "A-Are you okay?"
    p "*Laughs* Hahaha!"
    mc "*Chuckles* What are you laughing at?"
    p "*Chuckles* Nothing, I'm just laughing at the absurdity of this situation."
    p "Oh god..."
    p "At this point I don't care about Regina anymore. I don't even care about that damn yearbook."
    play sound clothes4
    show dpp 35
    p "Honestly? I just want to spend time with you doing cra..."with dis12
    show dpp 36
    p "C-Crazy..." with dissolve
    play sound2 clothes2
    play sound3 clothes4
    show dpp 37
    p "*Jumping up* [mc]!!"with dis06
    show dpp 38
    mc "What?" with dis
    p "Y-Your toga! Y-You're..."
    show dpp 39
    mc "Huh?" with dissolve
    show dpp 40
    mc "*Awkward laugh* Oh... erm... shit." with dissolve
    play sound clothes4
    show dpp 42
    mc "*Standing up* It's just that... that wardrobe was way too small, and..."with dis
    show dpp 41
    p "W-Where are your underpants? Have you been going commando all night?"
    show dpp 42
    mc "Um... yeah, I didn't want them to ruin my costume."
    p ". . ."
    show dpp 41
    p "My fucking god, [mc], you're hung like a fucking horse. That cock is a weapon!"
    if not dare1:
        p "I thought you were messing with Regina when she asked you how big you were."
        p "Now I think you were underselling it."
    show dpp 42
    mc "Uh?"
    if pennyshower:
        mc "But you stared at me before the party. In the shower."
    else:
        mc "But you already caught me naked once in the bathroom by accident."
    mc "Didn't you?"
    show dpp 41
    p "Well, y-yeah, but you weren't hard. And you were in the shower."
    p "There must have been... shrinkage or something, I don't know. Now it's like... three times the size."
    show dpp 42
    mc "I-I've just been trying to keep it in check all night."
    mc "But it doesn’t help that you’ve been teasing me, Penny..."
    mc "And the fact that you can't take your eyes off it isn't helping either..."
    mc "Actually, it's turning me on even more."
    show dpp 43
    p "*Laughs* EXCUSE ME? Now your donkey dick is my fault?" with dis
    show dpp 44
    mc "Oh, absolutely."
    if novadildo or holdondildo:
        if pennyshower:
            mc "Our conversation in the bathroom, the locker room when I asked you for a bra, the truth or dare game..."
        else:
            mc "First the locker room when I asked you for a bra, then the truth or dare game..."
    else:
        mc "First our conversation in the bathroom, then the truth or dare game..."
    if dare3:
        mc "I even dared you to flash me, and you snaked your way around that! You ruined the sanctity of Truth or Dare, in my opinion."
    mc "It’s like you’re trying to set a world record for bluest balls!"
    mc "Pretty rude to your manager, if you ask me. I might have to shelve you for my other clients..."
    show dpp 43
    p "*Giggles* What other clients?"
    p "And it's not my fault that you're a horny dog."
    p "Are you telling me that I'm to blame for you getting an erection at awkward moments? I don’t think it’s my fault that you can’t control yourself around me..."
    show dpp 44
    mc "It’s your fault, a hundred percent."
    mc "It's been like torture."
    show dpp 43
    p "*Giggles* Oh my, I had no idea you were suffering this much, baby!"
    p "I'm so sorry."
    show dpp 44
    mc "Nuh-uh, I don't forgive you."
    show dpp 43
    p "*Chuckles* Pretty please... [mc]?"
    show dpp 44
    mc "Nope."
    show dpp 43
    p "Come on..."
    p "Isn’t there anything I can do for you to forgive me?"
    p "I’m {i}so{/i} very sorry for flaunting my lewd body in front of you, [mc]. I had no idea it would cause you so much stress..."
    play music2 pennysong fadein 20
    show dpp 44
    mct "I like where this is going..."
    stop musicb fadeout 10
    mc "Well, as compensation for all the teasing that you've made me go through..."
    mc "What if you let me see what you’re hiding under that dress...?"
    show dpp 43
    p "You want to see me naked? The photoshoot wasn’t enough for you, perv?"
    show dpp 44
    mc "Oh, but now it's different. That day was strictly professional."
    mc "I was just performing my due diligence as a prospective manager."
    show dpp 43
    p "And today?"
    show dpp 44
    mc "Today it's... a personal request."
    show dpp 43
    p "A personal request, huh?"
    show dpp 44
    mc "Just a quick boobie flash! That's all I’m asking for."
    show dpp 43
    p "And what's in it for me?"
    show dpp 44
    mc "Hmm... my forgiveness?"
    p "*Snorts* Hmm."
    mc "And the possibility to keep working with the most respected manager in Kredon."
    mc "It's a pretty sweet deal, if you ask me."
    show dpp 45
    p "Hmm."with dissolve
    show dpp 43
    p "Here?"with dissolve
    show dpp 44
    mc "Here..."
    show dpp 47
    p "Okay, superstud... you’ve convinced me."with dis12
    p "I guess you have a point. I really wouldn’t want to risk upsetting my manager..."
    p "*Giggles* And honestly? The truth is that I've definitely been teasing you for quite a bit... and it’s been very, VERY fun."
    show dpp 46
    mct "Oh yes... FINALLY!"
    show dpp 47
    p "Okay, take a good look, [mc]."
    p "It won't last..."
    play sound clothes4 volume 1.3
    show dpp 48 with dis15
    bla "Penelope slips off the top of her dress, her bare breasts heaving before your eyes." with dis
    mc "Oh, fuck yes..."
    show dpp 49
    mc "I'd forgotten how perfect they were, Penny." with dis12
    mc "I suspected you weren't wearing a bra when I saw you in that dress. With tits like yours, you wouldn’t even need one."
    show dpp 50
    p "Happy now, Mr. [lastname]?" with dis
    p "Do you forgive me for acting naughty? For being such a tease? For flaunting myself all around you?"
    mc "Not quite yet, Miss Carter..."
    mc "You'll have to try much harder."
    play sound clothes4 volume 1.3
    show dpp 51 with dis15
    p "*Giggles* Okay, okay..."with dis08
    p "Hmm, I wonder what else I could do...?"
    p "How about..."
    play sound2 clothes4 volume 1.3
    show dpp 52 with dis15
    mc "Much better..."with dis
    mc "My god, this was worth the wait... I’ve been wanting to see you like this ever since I saw that first pic on Instagram..."
    show dpp 53
    bla "Penelope continues stripping for you. She leans softly against the bedpost, and curves her rear into an inviting pose." with dis15
    show dpp 54
    p "Okay... I don't have a single piece of clothing left on me."
    p "This should more than compensate you for all the teasing. I hope you enjoyed the spectacle."
    show dpp 53
    mc "Penny... you're a fucking goddess."
    mc "Your face, your ass, those gumdrop nipples... you’re making a man drool..."
    show dpp 54
    p "Yeah, I can tell that you're liking the show."
    p "Your cock has been growing redder and redder throughout this little exhibition... not to mention bigger."
    show dpp 53
    mc "I’m not the only one enjoying this. You like showing off for me, don’t you?"
    mc "You like when I gaze at your bare tits..."
    mc "Admit it. You like being my personal little model, Penny."
    show dpp 54
    p "I could say the same thing about you. [mc] Junior seems to be really enjoying himself."
    p "*Giggles* You should see your face."
    p "I'd love to know what's running through your mind right now."
    show dpp 53
    mc "Well, since you asked... I was thinking about how those huge, heavy tits of yours would feel in my hands."
    show dpp 54
    p "Oh, really...?"
    p "Well..."
    p "In the interest of science... do you wanna feel for yourself?"
    show dpp 53
    mc "Wait... are you serious?"
    p "Mm-hm..."
    show dpp 54
    p "Yeah, why not? You’ve caught me in a pretty good mood."
    p "Treat yourself..."
    show dpp 55
    bla "You move closer to Penelope, frantically trying to memorize every square inch of the model’s ethereal body." with dis2
    mc "God..."
    play sound clothes3
    show dpp 56
    bla "Your hands enclose both of her breasts, indulging in their warmth and tenderness. Penny releases a little squeak of surprise." with dis14
    p "Aaah..."
    show dpp 57
    mc "Dear Lord, they feel so incredibly soft..." with dis12
    show dpp 56
    mc "They're firm enough not to sag... yet, they’re so supple."with dis12
    show dpp 57
    mc "And I can barely fit them in my hands..."with dis12
    show dpp 58
    mc "*Grabbing her by the waist* Can I try one last thing before we end this, Penny?"with dis
    p "W-What? What are you gonna do?"
    mc "Something I've been dreaming about since I first spotted you and your “assets” in Kredon."
    show dpp 59
    bla "You wrap your mouth around Penelope’s erect nipple, and begin licking the “best tits on Instagram.”" with dis14
    p "W-What are you doing...?"
    show dpp 60
    p "Oh fuck..." with dis14
    show dpp 61
    p "*Giggles* You're crazy, [mc]..." with dis
    p "Although... I've gotta say that I kinda love your cockiness."
    scene pennyparty1
    bla "You wrap your arms around Penelope's waist, holding her in place with a firm grip before beginning to suck on the blonde's voluptuous breasts." with dis2
    p "Damn, [mc]..."
    p "Mmmm..."
    p "F-Fuck, keep sucking..."
    p "I d-didn't know I was so sensitive there..."
    mct "Jesus Christ..."
    mct "Her skin, her scent, the heat she radiates..."
    mct "This feels like a goddamn dream come true."
    p "MMmmmmmm..."
    scene pennyparty2
    bla "Unable to resist, you suck on Penelope's breast as hard as you can, alternating between little nipple flicks and small bites, determined to leave some sort of mark." with dis2
    p "Aaahh... y-yeah... you're doing such a good job..."
    mct "There are thousands of men in Penelope’s DMs who would pay exorbitant amounts of money just to see her naked."
    mct "Yet here I am, seeing them up close and personal."
    mct "No... not only that... I'm feeling her... I'm tasting her..."
    mct "She's mine... For at least tonight, Penelope Carter is all mine..."
    p "Aaaah!"
    mct "I feel like I could do this all night."
    mct "I just want to devour her..."
    scene dpp 63
    p "*Shoving your face away* Okay, okay, that's enough!" with dis12
    show dpp 62
    mc "Aw, really? I was just starting to enjoy myself!"
    show dpp 63
    p "*Giggles* You've been enjoying it since the beginning."
    p "Besides, [mc] Junior was constantly poking me down here, in case you didn't notice."
    show dpp 62
    mc "Not my fault. Your tits are literally making me lose my mind, Penny."
    show dpp 63
    p "You {i}really{/i} like my tits, huh?"
    show dpp 62
    mc "“Like” is an understatement."
    mc "I want to worship them on an altar."
    show dpp 63
    p "*Giggles* You're a filthy little degenerate."
    show dpp 62
    mc "Can't deny it. What can I say, your tits bring it out of me."
    p "Hmm..."
    show dpp 64
    p "You know what..." with dis12
    p "Since you seem to like them so much..."
    play sound chair1
    show dpp 65 with dis12
    p "*Shoving you down to the couch* How about I give you a little memory that’ll truly be unforgettable..."with dis08
    show dpp 66
    mc "Oh god..."
    show dpp 65
    p "*Giggles* Jesus, [mc], how long can you keep up an erection like that?"
    show dpp 66
    mc "With your naked body in front of me? Probably hours."
    mc "I mean... holy fuck, Penny."
    mc "Your body is almost indescribably perfect. It’s like someone pushed all your body’s features to their max settings."
    show dpp 65
    p "Well, I'm not the only one with their “features” pushed to the max here..."
    play sound2 chair4
    show dpp 67
    bla "Penelope kneels between your legs and ties up her hair." with dis12
    show dpp 68
    p "Well..." with dis12
    mc "O-Ooh god..."
    p "We're gonna have to do something about this, don't you think?"
    p "We can't go back to the party with you in this state."
    if novapath:
        p "What if it slips out of your costume again? We can’t have Nova or another girl accidentally catching sight of this monster dick, can we?"
    show dpp 69
    mc "Definitely... there have already been too many wardrobe malfunctions tonight..."with dis
    mc "Did you have a plan in mind?"
    show dpp 70
    bla "Penny grabs both of her boobs and quickly buries your cock between them." with dis14
    mc "OH GOD..."
    scene pennyparty3 with dis2
    mc "Oh my fucking GOD."with dis
    mc "They're so damn warm..."
    p "*Giggles* I can imagine. Do you like feeling my big titties wrapped around your cock like this?"
    mc "Fuck me, keep going..."
    mc "I love it when you stare into my eyes, Penny..."
    mc "Keep looking at me with that face... It’s like you’re drenched in lust..."
    p "*Giggles* I confess that doing this in Regina's dorm is kind of... arousing. We could get caught at any... single... moment."
    scene dpp 71
    mc "AAAahh yeah..." with dis12
    mc "My god, Penny, please don't stop..."
    scene pennyparty4 with dis2
    bla "Your dick begins to lubricate itself with precum, and, as if motivated by the liquid, Penny increases her pace with a quiet determination." with dis
    bla "Her eyes flit back and forth between your face and the meat buried in her chest."
    mc "O-O-Ohhh fuck yes, that's it..."
    mc "T-This is amazing..."
    mc "The “{i}Best tits on Instagram{/i}”, eh...?"
    mc "How many DMs have you gotten about this exact situation?"
    p "*Giggles* I've lost count."
    p "They offer me money, gifts, and even trips sometimes!"
    mc "Aaaahh... this feels so good..."
    p "I rejected all their requests, but here I am doing it for free, for some high school kid with a fat dick."
    p "Not a very good business move, I guess..."
    mc "*Chuckles* Y-You won't catch me complaining..."
    mc "But I’m not just some high school kid, y’know..."
    pause
    play sound chair3
    scene dpp 72
    bla "You stand up and seize Penelope's breasts with your hands, your dick still trapped between them." with dis
    mc "I think it’s time for me to take the lead, Penny..."
    mc "You're okay with it, right?"
    p "Yeah, I guess you can take a shot..."
    $ renpy.music.set_volume(0.35, delay=7.0, channel='music2')
    scene pennyparty5 with dis2
    mc "Aaaahh... yeah!" with dis
    mc "YEAH!"
    mc "That's it, Penny..."
    mc "Keep staring into my eyes like that..."
    mct "My fucking god, Penny's cleavage feels like fucking a pussy..."
    mct "I'm FUCKING the best tits on Instagram!"
    pause
    mc "AAaaahh..."with dis08
    bla "You thrust into Penelope’s cleavage frantically, your balls slapping against her tummy with each stroke."
    mc "This sensation is amazing..."
    mc "AAaahhh..."
    mc "A-Am I squeezing them too hard?"
    p "I like it that way..."
    p "*Giggles* It feels good when you’re a little rough with them..."
    p "Being used for your pleasure like this is... pretty fucking hot, not gonna lie."
    mc "Oooh god... you’re a naughty girl, aren’t you..."
    mc "You're gonna make me cum way too quickly..."
    play sound clothes4
    scene dpp 73 with dis
    bla "You abruptly grab Penelope and lift her to her feet." with dis
    p "W-Why did you stop?"
    mc "I don't wanna finish yet..."
    p "You don't?"
    mc "Not yet, babe..."
    show dpp 74
    p "F-fuck... y-you're..."with dis
    show dpp 75
    p "Y-You're touching my pussy with your dick..."
    mc "Your lips are literally dripping over my cock, Penelope..."
    mc "I don’t think it would be fair if I was the only one to cum tonight... Besides, you’ve been so generous tonight..."
    mc "And you’re so... tempting..."
    show dpp 73
    p "Don’t even think about it, [mc]."with dis
    p "W-We're not gonna f-fuck. I’m not a first date kinda girl, y’know..."
    p "Besides, we don't even have a condom..."
    mc "Oh... so a condom is what’s stopping us? If I had one, we would be fucking right now?"
    show dpp 75
    p "*Giggles* I didn't say that."with dis
    p "We’ve already done so much tonight. You’re not satisfied yet?"
    play sound clothes4
    play soundlow clothes1
    scene dpp 76
    bla "You turn Penelope around and slide your penis between her thick thighs again." with dis12
    p "Aahh..."
    scene pennyparty6 with dis2
    p "AAaaaah... What are you d-doing to me?" with dis
    bla "You carefully begin to slide your dick between Penelope's legs, each thrust slightly spreading apart her pussy lips."
    mc "Oh god, Penny..."
    p "Fuck, [mc]..."
    mc "You're actually dripping..."
    mc "Did you get that turned on from having my cock between your tits?"
    p "AAaahhh..."
    pause
    mct "I know she'd get mad just for trying, but..."with dis08
    mct "I’m literally going insane trying to not bury my cock balls-deep inside of her."
    p "*Slight moan* AAaahh..."
    mc "Do you like this? Gliding your pussy along my cock?"
    p "I-I do... I like it a lot..."
    p "Move faster... please move faster..."
    mc "You want it faster? Tell me, Penny..."
    p "Y-Yesss!"
    menu:
        with dis
        mod "This choice affects minor flavor of scenes with Penny."
        "Romantic approach":
            $ pennyrough = False
            play sound2 clothes4
            scene pennyparty7 with dis2
            bla "You hasten your pace, slamming your hips against Penelope's generous buttocks while exhaling small breaths on her neck." with dis
            p "AAAAhhh..."
        "Rough approach":
            $ pennyrough = True
            play sound2 clothes4
            scene pennyparty7b with dis2
            bla "Your hands wrap around Penelope’s soft neck as you hasten your pace, your hips slamming relentlessly against the blonde's buttocks." with dis
            p "Mmmghhh... y-yess..."
    mc "Ohhh Penny..."
    mc "This feels so fucking good..."
    p "AAaaahh..."
    p "I-It d-does... s-so fucking good..."
    p "K-Keep up that pace, [mc]..."
    bla "Penelope squeezes her legs together, and more juices drip down her thighs. Your dick begins to slide even more smoothly against her lips."
    mc "Oh g-god, yes..."
    pause
    p "MmmMmmm..." with dis08
    if not pennyrough:
        mc "I know you were craving for this..."
        mc "I know you fingered yourself thinking about me..."
    else:
        mc "You love this, don't you? My hands wrapped around your neck, thrusting into you from behind..."
        if donepotions:
            mc "I know you want to be fucked roughly... I know you like ropes..."
        mc "You want everyone to treat you like a princess, but deep down you’re a kinky little girl, aren’t you, Penny...?"
    mc "Don't think I forgot what you said that day in Warthogs, miss..."
    mc "Or are you gonna tell me that was all a lie?"
    if pennyrough:
        p "*Choking* A-A-AAhhh..."
        p "*Giggles* I-It w-wasn't a lieeee..."
        p "I-I want to be fucked so hard that my pussy is sore the n-next day..."
        mc "Ohh... f-fuck me, Penny..."
        mc "You like me using your body as a toy, don't you?"
        p "*Choking* Y-Yeagh... u-use me as your fucking toy, [mc]..."
        mc "I wanna make your body writhe in pleasure, Penny..."
    else:
        p "*Giggles* A-A-AAhhh..."
        p "I-It was just because you were the only guy in the house..."
        p "*Moaning* AAaaahh..."
        p "Y-You’re telling me you haven’t jacked off to me since arriving in Kredon?"
        p "The walls aren’t that thick y’know, it’s amazing what you can hear in the hallway during a midnight b-bathroom trip..."
        mc "Aaah..."
        mc "You’re right, I haven't been able to stop dreaming of spending a night with you in weeks..."
        p "Aaaahh..."
        mc "My only wish is seeing your divine body writhe in pleasure..."
    p "AAAaaHhhh..."
    mc "After I pump it... all... night... long..."
    p "AAAAAAAAAAAGHH..."
    if pennyrough:
        p "*Choking* F-Fuck... I'm gonna cum, [mc]..."
    else:
        p "F-Fuck, [mc]... I'm gonna cum..."
    mc "M-Me too..."
    mc "God, Penny..."
    mc "F-Fuck, I'm about to..."
    p "Y-YEAH!"
    p "Cum for me, baby..."
    mc "F-Fuck, I can't stop it..."
    p "AAAAH..."
    play sound cum2 volume 1.5
    play sound2 cum1
    play sound3 cum3
    play sound4 slap1
    if pennyrough:
        scene dpp 78
    else:
        scene dpp 77
    mc "AAAAAAAGGHHH!" with hpunch
    p "Aaah!"
    play sound cum2 volume 1.5
    play sound2 cum1
    play sound3 cum3
    mc "AAAAAARRGGHHH..." with hpunch
    show dpp 79 with dis2
    mc "Goddamn..."with dis08
    mct "I needed this so badly... my blue balls were about to fucking explode..."
    stop music2 fadeout 10
    play music night fadein 7
    play sound ["<silence 0.4>", fall2]
    show dpp 80
    mc "*Sitting down on the floor* Holy shit..." with dis15
    mc "You're something else, Penny..."
    show dpp 83
    p "Me? You're fucking crazy..."
    p "How’d you convince me to get you off in my archenemy’s room?"
    show dpp 80
    mc "*Chuckles* Hah!"
    mc "Like you're one to talk!"
    show dpp 83
    p "I'm gonna have to ask you to come to all the parties I'm invited to from now on, [mc]."
    p "Tonight's was... definitely the craziest one I've ever had."
    show dpp 80
    mc "Agree with you there, that's for sure..."
    mc "But hey, going crazy sometimes is worthwhile, don't you think? Imagine if we’d never decided to sneak in here tonight..."
    show dpp 83
    p "Oh, for sure."
    p "What's life without going a little crazy from time to time?"
    show dpp 80
    mc "I like the way you think, miss."
    show dpp 82
    p "So... what should we do about that?" with dissolve
    p "You sure emptied yourself. It was like a fire hose!"
    show dpp 79
    mc "Oh, the jizz?"
    mc "Um... should I clean it? Guess I can look around for some sprays..."
    show dpp 82
    p "Uh..."
    show dpp 83
    p "Nah, fuck it." with dissolve
    p "It's my payback for the yearbook."
    show dpp 80
    mc "*Laughs* I wish I could see Regina's disgusted face when she sees that puddle."
    show dpp 83
    p "I guess I'll settle for seeing it in class."
    show dpp 80
    mc "*Chuckles* Make sure to tell me about it after!"
    show dpp 83
    p "Will do."
    p "But anyway... we should get dressed and get the fuck out of here before someone finds us."
    show dpp 80
    mc "Just let me say goodbye to my beloved twins before you cover them."
    mc "I'll miss you, girls."
    mc "I’ll always cherish the time we’ve spent together."
    show dpp 83
    p "*Snorts* You're such a dork. You’re lucky I think you’re cute."
    $ pennytitjob = True
    stop music fadeout 8
    jump leavingparty


label collegepartyexit:
    if ppp1:
        mc "I should ask at the counter before going anywhere."with dissolve
        call screen collegeparty1 with dis06
    show screen heart
    mct "On second thought... man, I think I've had enough."with dis08
    mct "This damned music is getting to me."
    if novapath:
        mct "This isn’t really my scene... I'm sure they'll survive without me."
        mct "I'm getting the fuck outta here."
        mc "*Typing on your phone* (I'll just text them that I'm leaving.)"
    else:
        mct "This isn’t my scene... I'm sure Penelope will have a great time with or without me."
        mct "I'm getting the fuck outta here."
        mc "*Typing on your phone* (I'll just text her to tell her I'm leaving.)"
    mc "*Yawns* (I need a good night of sleep...)"
    play sound doorold
    stop music2b fadeout 4
    stop music3 fadeout 4
    stop soundloop fadeout 4
    $ leavepartyearly = True
    $ penelopepath = False
    $ penelopeu = False
    jump nancyworkplace


label leavingparty:
    if not novapath:
        jump leavingparty2
    scene black
    show screen afewminuteslater
    with dis2
    pause
    play music2b partypenny fadein 6
    scene dpp 84
    hide screen afewminuteslater
    with dis2
    pause
    show dpp 85
    p "And you say Nova is supposed to be around here?" with dis14
    show dpp 86
    mc "I think so." with dis08
    if novadildo or holdondildo:
        mc "She wasn't feeling well, so she went with Akira to get the reward for that game I told you about."
        mc "I went to the cafeteria but–"
        no "Finally!!"
        show dpp 87
        mc "Huh?"with dis
        mc "Nova! We were looking for you!"
        mc "How are you feeling?"
        show dpp 88
        no "Much better, thanks!"
        no "I think I spent like an hour in the bathroom trying to vomit, but nothing came out, so... I'm s-still a bit d-drunk."
        show dpp 87
        mc "*Chuckles* I can tell."
        mc "Is that box what I think it is?"
        show dpp 88
        no "*Giggles* YES!"
        no "I was afraid it was a prank, but luckily it wasn't!"
        no "An Intel Xeon Dragon X!"
        show dpp 89
        p "Wow, congrats, guys!"
        show dpp 88
        no "*Giggles* Thanks."
        show dpp 89
        p "I want more details about the game though! Sounds like I missed out!"
        show dpp 90
        no "Oh w-well, there's not much to tell, to be honest!"with dis08
        no "Just... s-some beer-pong and card games. T-The typical party."
        no "R-right, [mc]?"
        mc "R-right!"
        show dpp 88
        no "What about you, though? How were things over on your side?"with dis08
        if pennytitjob:
            show dpp 91
        else:
            show dpp 89
        p "Oh, well, you know... pretty much the same."
        p "Just some drinking games and Jagerbombs. The... typical party."
        if pennytitjob:
            p "Right, [mc]?"
            mc "Y-Yep!"
        show dpp 88
        no "I see... Damn, sounds like you guys had a fun time too!"
        show dpp 92
        p "Well, I don't know about you guys, but I think it’s time to call it a night." with dis15
        show dpp 93
        no "Y-Yeah, I'm going with you!"
        no "It's already 4:45 AM."
        show dpp 92
        mc "Damn, really? I didn't know it was that late."
        show dpp 94
        p "What are your plans, [mc]?"with dis
        p "Are you staying over here or are you coming with us?"
        show dpp 94b
        mc "Hmm, it kinda sucks that the three of us never hung out together. What about having one last drink before leaving?"
        show dpp 94c
        no "Uhh... I d-don't know if I could take one more drink... my one beer has made me hazy enough as is..."
        show dpp 94b
        mc "Don't worry! I'll walk you two home!"
        mc "Do you really think I'd miss the opportunity to escort two pretty ladies back to their doorsteps?"
        mc "Please, I'm a gentleman."
        show dpp 94
        p "*Chuckles* Alright, mister..."
        p "In that case, let's have one last toast!"
        show dpp 94b
        mc "Sweet!"
    else:
        mc "Last I heard she was in the cafeteria, but she's not there now, so I don't–"
        no "Finally!!"
        show dpp 95
        mc "Huh?"with dis
        mc "Nova! We were looking for you!"
        show dpp 96
        no "Shut up!"
        no "Y-You abandoned me!"
        show dpp 95
        mc "What?! No, I didn't!"
        show dpp 96
        no "YES YOU DID!"with hpunch
        if ppp5:
            no "I c-came back from the bathroomm a-and you h-had... d-disappeared!"
        else:
            no "Y-You didn't come back, so Akira gave the p-prize to Dolores."
            no "I lost."
            no "B-Because of you."
        show dpp 95
        mc "Are you drunk?"
        show dpp 96
        no "W-Well yeah! W-What was I supposed to do while you were I-don't-even-know-where?"
        no "I drank... a beer."
        show dpp 95
        mc "Just one?"
        show dpp 96
        no "I-I don't handle alcohol very well."
        show dpp 89
        p "I'm sorry, Nova, I'm the one who distracted [mc]."
        p "You can blame me for this."
        show dpp 97
        no "D-don't worry, Penny."
        if ppp5:
            no "You didn't even know where I was."
        else:
            no "You didn't know about the game."
        show dpp 96
        no "[mc], on the other hand..." with dis08
        show dpp 95
        mc "Come on, Nova, don't get mad at me!"
        mc "I'll make it up to you, I promise."
        mc "It's 4:45 AM, so we should probably start heading out. I'll walk you home and... I'll buy you a huge kebab on the way there!"
        mc "There's nothing better to sober you up."
        show dpp 97
        no "Uh, t-that actually sounds pretty good." with dis
        no "Okay, let's go! I want a mixed one!"
        mc "Deal!"
        mc "*Chuckles* (It's always cute to see how easy it is to make her happy.)"
label leavingparty2:
    stop music3 fadeout 6
    stop music2b fadeout 6
    play soundloop night fadein 6
    scene black with dis2
    show screen afewhourslater with dis17
    pause
    hide screen afewhourslater
    scene dn 1
    with dis22
    if novapath:
        bla "You walk Nova to her house and come back home with Penelope."with dis12
        p "Aaah... finally!"
    else:
        p "Aah... finally!" with dis
    play soundlow chair1
    play sound2 clothes1
    show dn 2
    p "*Taking her shoes off* Those shoes were killing me!" with dis14
    play sound6 clothes3
    show dn 3
    p "Home sweet home..." with dis14
    show dn 4
    mc "Man, I'm so fucking tired."
    mc "I'm getting too old for these sorts of things."
    show dn 5
    p "*Laughs* Yeah, definitely."
    p "After 17, everything starts going downhill. Everyone knows it."
    show dn 4
    mc "*Laughs* Absolutely."
    mc "Are you feeling drunk?"
    show dn 5
    p "Nah, I usually have trouble getting {i}seriously{/i} drunk. I'm just tired."
    show dn 4
    mc "Makes sense. It was a pretty intense night..."
    show dn 5
    if penelopepath:
        p "Yeah, I guess it was..."
        p "Although... not due to dancing."
        show dn 4
        mc "Now that you mention it, I still owe you a dance."
        show dn 5
        p "Do you?"
        show dn 4
        if divinationflashback:
            mc "Yeah! I haven't forgotten what we saw with the Reminisc..."
            play sound2 hiccupb
            mc "*Hiccup* Hic!"with vpunch
            mc "...the Reminiscecombobulator at Warthogs."
            mc "You kind of missed your school dance because of me."
        else:
            mc "Didn't you tell me you didn't get to go to Kredon's Spring Dance when you were little?"
        mc "I owe you a little slow dance."
        show dn 5
        p "Oh my, so romantic."
        p "Are you a good dancer?"
        show dn 4
        mc "Good? My moves are irresistible."
        show dn 5
        p "*Laughs* Can't wait."
        show dn 3
        p "Well, I don't know about you, but I'm gonna put my pajamas on and sleep until noon."with dis04
        show dn 4
        mc "Oh, that sounds like a great plan."
    else:
        p "Yeah, I guess it was."
        p "At least you knocked some sense into me with the Regina thing."
        p "Thanks, [mc]. You're a good friend."
        show dn 4
        mc "Hey, that's what friends are for."
        show dn 3
        p "Yeah... I guess so."
        p "(God, I'm so stupid.)"
        p "Um... anyway, I'm gonna put my pajamas on and sleep until noon."
    show dn 5
    p "I had a lot of fun tonight, [mc]. Thank you."
    if penelopepath:
        show dn 4
        mc "No goodnight kiss?"
        show dn 5
        p "*Giggles* Goodnight kiss?"
        p "Hmmm... where could I give you a kiss?"
        show dn 4
        mc "On the forehead, maybe."
        mc "But if you're feeling bold tonight, the cheek might work too."
        mc "No wrong answers."
        p "*Snorts* Hmm."
        play sound clothes4
        show dn 6 with dis2
        pause
        play sound2 clothes3
        $ penelope_points += 2
        show dn 7
        bla "Penelope takes off your circlet and presses her soft lips against your mouth." with dis15
        play soundlow beat
        show screen heartbeat
        bla "Without hesitation, her mouth opens slightly, allowing your tongue to slip inside. After what feels like a matter of hours, or perhaps just several seconds, she breaks away from you and the kiss ends."with dis08
        p ". . ."
        play sound clothes3
        show dn 8 with dis17
        p "Good night, [mc]..."with dis06
        mc "Good night, Penny."
        show dn 9 with dis2
        play sound2 doorclose
        mct "Wow..." with dis08
        mct "What a way to end the night!"
        mct "That’s what I call a party."
        mc "*Yawns* (Time to sleep, though...)"
        mct "If I don't have sweet dreams even after a night like this... I'm a lost cause."
    else:
        p "I'm glad to have you as a friend."
        show dn 4
        mc "Likewise, Penny."
        mc "Goodnight!"
        scene dn 10 with dis2
        play sound doorclose
        mct "God, 6:45 AM..." with dis
        mct "It's almost dawn."
        mct "I hope I can manage to sleep at least a few hours tonight. There’s supposed to be a thunderstorm and they always seem to wake me up."
        play sound chair1
        show dn 11
        mc "*Jumping into bed* (Hmmm... this bed has never felt fluffier...)" with dis12
        mct "Finally some rest..."
        jump nancyworkplace_2

label nancyworkplace:
    if penelopepath and not leavepartyearly:
        scene dn 10 with Dissolve(1.9)
        play sound doorclose
        mct "God, 6:45 AM..." with dis
        mct "It's almost dawn."
        mct "I hope I can manage to sleep at least a few hours tonight. There’s supposed to be a thunderstorm and they always seem to wake me up."
        play sound chair1
        show dn 11
        mc "*Jumping into bed* (Hmmm... this bed never felt fluffier...)" with dis12
        mct "Finally some rest..."
    else:
        show screen nextday
        show black
        with dis27
        pause
        play soundloop night fadein 4
        hide screen nextday
        show dn 1
        with dis25
        mc "Hmmm..." with dis08
        mct "What a shitty night."
        mc "*Looking at your phone* Holy fuck, 6:45 AM!"
        if pennyreginahate:
            mct "It's almost dawn and I haven't slept a minute..."
            mc "*Sighs* (I haven't been able to stop thinking about what happened with Penny at the party.)"
        else:
            mct "It's almost dawn and I haven't slept a minute... damn insomnia."
        play sound chair1
        show dn 11
        mc "*Jumping into bed* (Hmmm... let's see if I manage to sleep for a couple or three hours at least...)" with dis12
label nancyworkplace_2:
    show dn 12
    mc ". . ." with dis12
    play soundlow snore
    mc "Zzzzz..."with dis
    stop soundloop
    play sound slam
    play soundlow horn
    play music2 "<silence 0.8>"
    queue music2 sneaky5 fadein 3
    $ unlock_look("nancy", 7)
    show dn 13
    n "GOOD MORNING, SWEETIE!" with hpunch
    play sound5 chair2
    show dn 14
    mc "*Jumping up* W-Wait, what?!" with dis
    show screen sundaycorner
    show dn 15
    n "We're going to my office, remember?"
    show dn 14
    mc "What?!" with hpunch
    mc "Now?! It's not even 7 AM!"
    if penelopepath:
        mc "W-We just arrived from the party!"
        show dn 16
        n "Yeah, I saw Penny coming out of the bathroom!" with dis08
        n "She looked so happy... super tired though! I hope you had fun!"
        mc "Um..."
    show dn 17
    n "I'm sorry, but we have to leave soon. Getting there this early is critical!"with dis
    n "You'll understand why after I explain the plan to you."
    show dn 18
    mc "Y-Yeah, don't worry. It's just that... I wasn't expecting it to be SO early."
    show dn 17
    n "I mean... I can try to handle it on my own, if you want to sleep in."
    show dn 18
    mc "Huh? And miss all the fun?"
    mc "{i}“Thanatos collects the 10 Gems of Doom and becomes the new CEO of Ulysses.”"
    mc "{i}“[mc] [lastname], the other closest competitor, fell behind because he needed to take a nap.”"
    mc "Nah, they won't say that about me."
    show dn 15
    n "That's the [mc] I know!" with dis
    show dn 14
    mc "I'll handle it. Nothing a good shower and a HUGE cup of coffee can't fix."
    show dn 15
    n "Nice!"
    n "Go take that shower and meet me downstairs!"
    show dn 14
    mc "Alright!"
    show dn 15
    n "Thanks for sacrificing your sleep for the mission, [mc]."
    show dn 14
    mc "I'm the one who pushed you all into the whole “Gems of Doom mission” in the first place."
    mc "No need to thank me for anything."
    show dn 15
    if nancypath:
        n "Still, thank you. I'll make it up to you, I promise..."
        show dn 14
        mc "That promise is just as invigorating as all the coffee in the world..."
    else:
        n "Still, thank you."
    mc "Let's go!" with hpunch
    hide screen sundaycorner
    stop music2 fadeout 8
    scene black with dis2
    play soundloop rain2 fadein 6
    show screen afewhourslater with dis
    pause

label nancyoffice:
    play sound carpasswet volume 0.7
    show dn 19
    hide screen afewhourslater
    with Dissolve(2.7)
    pause .2
    mct "Hmm..."with dis12
    mct "So this is Nancy's office, eh?"
    play music2 office fadein 5
    stop soundloop fadeout 10
    show dn 20
    mct "Pretty cool..." with Dissolve(1.8)
    mc "*Yawns* (Pretty huge place.)"
    mct "God, I'm so sleepy."
    show dn 21
    mct "If Nancy doesn't come back with that coffee soon, I might fall asleep leaning against one of these walls." with dis15
    mct "Hmm..."
    mct "Maybe I should close my eyes and just let them rest for a minute."
    mct "Yeah, that's smart..."
    show dn 22
    mct "Just for a minute..." with dis12
    show dn 23
    mct "Just resting my eyes..."with dis
    mct "Just a min..."
    $ renpy.music.set_volume(1.0, channel='soundloop')
    play soundloop snore
    show dn 24
    mc "Zzzzz..." with dis
    play sound2 ding
    play sound3 elevator
    n "[mc]!{w=0.3}{nw}" with hpunch
    stop soundloop
    show dn25
    mc "W-What?! Y-YES! X equals 47, Mr. Keating! I'm awake!" with dis08
    mc "I-I am..."
    scene dn 27
    mc "Huh?" with dis
    mc "Oh, hi there!"
    mc "Please tell me you have my drug."
    show dn 29
    n "With extra caffeine!" with dis08
    mc "Oh, thank god!"
    show dn 30
    n "I was also able to fit two more in this bag."with dis12
    show dn 30b
    menu:
        with dis
        "Thank her for the coffee [nancy_pts]":
            $ nancy_points += 1
            play sound2 sip
            mc "*Drinking the first coffee* You’re a lifesaver!"with dis08
            mc "After all these years, you’re still taking care of me like a babysitter, eh Nancy?"
            play sound beat
            show screen heartbeat
            show dn 30
            n "Aww, you're too sweet, [mc]! Of course I’ve gotta take care of you."with dis06
            n "And I need you to be so charged up for the mission!"
            show dn 30b
            mc "A mission I still know nothing about, by the way." with dissolve
        "Focus on the mission":
            play sound2 sip
            mc "*Drinking the first coffee* Good. I have to be so charged up for the... mission."with dis08
            mc "A mission I still know nothing about, by the way."
    show dn 28
    n "I know, I'll catch you up in a minute." with dis
    n "But let's go to my desk first, on the second floor."
    play sound3 sip
    show dn 27
    mc "*Gulping down your second coffee* Won't people ask what I’m doing here?"
    show dn 28
    n "Don't worry, it's Sunday, so the office will be empty."
    n "There's only a couple of security guards by the entrance, but we used the emergency exit, so they shouldn’t know about us."
    play sound4 sip
    show dn 27
    mc "*Chugging your third coffee* Ah, smart."
    mc "And I've got good news, energy is returning to my veins already!"
    show dn 28
    n "*Chuckles* Glad to hear that!"
    n "We shouldn't take unnecessary risks, though. Let's try to be as fast as possible."
    show dn 27
    mc "You're the boss!"
    play sound3 elevator
    show dn 31 with dis15
    bla "You both get inside the elevator. Nancy hits the 2nd floor button." with dis08
    mc "Holy shit, that's a lot of buttons."
    mc "How tall is this building?"
    show dn 32
    n "There's only 4 floors above ground level, but there are 13 of them below-ground."with Dissolve(1.1)
    show dn 33
    mc "Damn, thirteen?! Really?"
    show dn 32
    n "Yeah. 5 of them are parking levels, and the rest are warehouses and labs that require special temperature conditions."
    show dn 33
    mc "Oh true, sometimes I forget you work in the sciences."
    show dn 32
    n "Well... to be fair, since Ulysses subcontracted us, everything I've been doing is paperwork."
    n "I miss my labcoat days, but they brought their own researchers, and now we're not even allowed on some of the floors."
    show dn 33
    mc "It was to be expected, they're a very secretive company. NDAs and all that."
    show dn 32
    n "There are usually people around here, but the office floors are typically empty on Sundays."
    n "We're gonna be tota–"
    stop music2
    play sound2 ding
    play sound3 elevator
    show dn 34
    ger "*Mumbling* Ugh, I can't believe {i}I'm{/i} the one who has to do this! After so many years at the company!" with dis12
    ger "Don't they know who I am?"
    ger "Huh? Nan?"
    play music2 office
    show dn 35
    ger "What are you doing here, girl?" with dis12
    ger "What a coincidence!"
    show dn 36
    n "G-Gertrude?!" with dis12
    n "What are YOU doing here?"
    n "It's Sunday!"
    show dn 37
    ger "Well, you know, duty calls."
    ger "My Richie is on a business trip and my son is playing that Ethernium thing, so I thought I’d catch up on work."
    ger "Between us, I think Mr. Dunder is going to promote me next month. I've seen how he looks at me..."
    show dn 36
    n "Uh... o-okay, yeah."
    n "Good luck, Gerty."
    show dn 38
    if nancypath:
        ger "What about you, Nan? I see you brought your daughter with you!"with dis
        ger "Good to see you again, Dalia."
        show dn 39
        mct "God, does this woman never listen?"
        mc "Um..."
        menu:
            with dis
            mod "Your preference, this will affect dialogue of future sex scenes. Can be changed via Cheats."
            "Roleplay as Nancy's child":
                $ nancymommy = True
                mc "Thank you, Gertrude. Good to see you again."with dis06
                mc "I've been looking forward to seeing where my... mom works, so she invited me to come with her today."
                show dn 42
                ger "Ah, that was an excellent idea, Nan, excellent!" with dis12
                ger "Dalia will learn a lot seeing two empowered women like us at their workplace."
                show dn 43
                n "Yeah... that was exactly my idea."
                n "I thought of coming on a Sunday because this place is usually too hectic during the week."
                show dn 42
                ger "Very smart."
                ger "Watch me and your mom closely, Dalia, you'll learn great life lessons and skills."
                show dn 42b
                mc "Yeah, I won't take my eyes off her..."
                show dn 42
                ger "By the way, I just want you to know that I support your decision SO much, Dalia."
                ger "As the president of Kredon's PTA, I always try to advocate for the rights of the trans community."
                ger "Some of us even started a campaign on TikTok in favor of the LGBTTQQIAAP movement!"
                ger "How are your dancing skills, Dalia? Would you like to join us?"
                show dn 42b
                mc "T-That sounds delightful, but dancing isn't really my thing."
                mc "Thanks for the offer, though."
                show dn 42
                ger "That's too bad... but let us know if you change your mind!"
                show dn 42b
                mc "S-Sure, will do."
                show dn 44
                ger "Anyway, it's good to see you, Nan, but I should get going now." with dis12
                ger "I'm terribly busy, as you know."
                n "Of course!"
            "Correct her":
                mc "*Sighs* Please, pay careful attention to my lips as I say this to you."with dis06
                mc "I. {w}AM. {w}NOT. {w}DALIA."
                mc "I'm not a girl, and I'm not Nancy's child."
                mc "My name is [mc]."
                mc "I'm a guy! A male!"
                show dn 38
                ger "Of course! You can identify as whatever you want."
                ger "Why, recently, my husb–"
                show dn 39
                mc "I identify as a guy because I've always been one, for fuck's sake! I was born a male!"with vpunch
                ger "Hmm...?"
                show dn 40
                ger "Wait, wait, wait."with dis
                ger "{i}He{/i} was born a... {i}male{/i}?"
                show dn 41
                n "Uh... yes, I think so."
                show dn 40
                ger "Agh! You can't be serious!"with hpunch
                ger "I can’t believe you’ve been lying to me all this time, Dalia! That is SO transphobic of you..."
                show dn 40b
                mc "ME?!" with hpunch
                mc "How the hell is my being a man transphobic?!"
                show dn 40
                ger "Wow, the fact that you even have to ask that... I can't even look you in the eyes anymore."
                show dn 40b
                mc "I didn't even lie about anything, you just don't listen to me!"
                show dn 40
                ger "Hah! Of course, because a woman always has to listen to men, and do exactly what they say, right?"
                show dn 40b
                mc "What are you talking about?!"with hpunch
                show dn 40
                ger "God, you’re such a misogynist."
                ger "What values have you taught to this boy, Nancy?"
                show dn 41
                n "Uh..."
                show dn 40
                ger "When will society learn, Nan? WHEN?!"
                ger "It's like we're still living in the 19th century!"
                show dn 41
                n "Erm..."
                n "Yeah... you're t-totally right."
                n "This is absolutely... unacceptable."
                n "Actually, I brought him here to teach him how to be more tolerant. He’s been watching all these videos on YouTube and sketchy forums..."
                n "Seeing empowered women like us as leaders at their workplace might do him some good."
                show dn 44
                ger "Ahh, that's actually a brilliant idea, Nan." with dis12
                mc "*Snorts* (Nice recovery.)"
    else:
        ger "And who's this?" with dis
        ger "New hire?"
        show dn 39
        mc "Um... yes, I'm [mc], nice to meet you."
        mc "I'm the new... intern."
        show dn 38
        ger "Ah, I'm Gertrude. Nancy probably told you about me already."
        show dn 39
        mc "Y-Yeah, totally."
        mc "You look even better than what she said."
        show dn 38
        ger "Oh my, we’ve got such a charming young boy at the office..."
        show dn 44
        n "Anyway, I've gotta go with him to... show him how to photocopy some documents." with dis12
        ger "Of course, of course."
        ger "I should get going too. I'm terribly busy, as you know."
    n "We're gonna be in my office, doing some spreadsheeting."
    ger "*Hearty laugh* Yes, that sounds like a good plan. I feel like you've been falling a little behind lately."
    ger "I know you can do better."
    n "Yeah... and, oh, now that I remember... if you see that Ulysses representative arriving, could you let me know?"
    ger "Sure thing, no problem."
    n "Thanks!"
    if nancymommy:
        n "Let's go... erm... Dalia."
    else:
        n "Let's go, [mc]."
    play sound ["<silence 1.2>", doorglass]
    show dn 45 with dis2
    bla "You and Nancy walk across the floor until she opens a door to a spacious and modern-looking room."with dis
    play sound2 whistle3
    mc "*Whistles* Not bad!"
    play sound3 doorglassclose
    show dn 46
    n "*Closing the door behind her* Dammit, that was too close!" with dis12
    n "I didn't want anyone to see you here."
    mc "We'll be fine. Gertrude doesn't seem to be that sharp anyway."
    show dn 48
    n "*Chuckles* Fair enough." with dissolve
    show dn 47
    if nancymommy:
        mc "Alright, Mommy..."
    else:
        mc "Alright, Nan..."
    mc "We're finally here. What's this plan of yours?"
    mc "Enlighten me."
    show dn 48
    n "Okay..."
    n "Remember what I asked Nova last Friday at The Roof? If she could program some malware capable of stealing the Eternum inventory of someone?"
    show dn 47
    mc "Mm-hm. I do."
    show dn 48
    n "Well... we did it!"
    show dn 47
    mc "No way!"
    mc "Already?! She didn't tell me anything!"
    show dn 48
    n "I asked her to keep it a secret. I wanted to give you the surprise."
    show dn 47
    mc "Holy shit, that's amazing!"
    mc "I don’t know what was more impressive: Nova’s hacking skills to put that together, or the fact that she was able to hide it from me that long!"
    show dn 48
    n "*Chuckles* It has to be physically linked to the E-visor of the target, and then it has to be recovered."
    n "It's risky, but the reward is well worth the effort."
    n "The “victim” wouldn't even notice something missing until it was too late."
    show dn 47
    mc "Wow, that definitely sounds like a powerful tool."
    mc "Too bad we don't know the real identity of Thanatos. That could be our secret weapon!"
    play sound chair2
    show dn 49 with dis15
    n "*Sitting on the table* Actually... I'm happy you said that." with dis08
    n "Because it brings us to the next part of the plan."
    show dn 50
    mc "Huh?"with dissolve
    show dn 49
    n "The Founder told you that Ulysses knows the first person to find each Gem, correct?"with dissolve
    show dn 50
    mc "Yep. They can’t track subsequent owners, but they can track the first one."with dissolve
    show dn 49
    n "And it is public knowledge that Thanatos found the first Gem of Doom, during one of Ulysses' special events."with dissolve
    show dn 50
    mc "Also correct. And then he took the rest of them from other players."with dissolve
    show dn 49
    n "Well... it turns out that every Sunday, a representative from Ulysses comes here to collect all the data we obtained during the week."with dissolve
    n "I've done some digging, and I know who he is: Clarence Ruiz, a Ulysses senior executive and a big name in the Data and Analytics division."
    n "He has a laptop where he keeps all his reports, and I get the feeling that the information we need is in there."
    n "And you, dear [mc]... are going to retrieve that information."
    show dn 50
    mc "DAMN!"with dissolve
    mc "You want to steal Ulysses' private info right from their database?!"
    show dn 49
    n "Pretty much." with dissolve
    show dn 50
    mc "So... if I understood all this correctly... we might be able to discover Thanatos' real identity?"with dissolve
    show dn 49
    n "Or his ID number. At the very least, some sort of clue that can lead us towards him."with dissolve
    show dn 50
    mc "Amazing!"with dissolve
    mc "But how are we gonna get access to that laptop?"
    play sound chair2
    show dn 51
    n "*Giggles* Pay close attention." with dis15
    mc "*Chuckles* I feel like I'm in a movie."
    n "This represents this office. I'm the glazed donut and you're the onion."
    mc "Fair choices."
    n "The tangerine is Clarence, and this... broccoli can be Gertrude. We'll take advantage of her being here."
    mc "Mm-hm."
    n "There are two elevators, represented by the pencil case and the pineapple."
    mc "Gotcha."
    show dn 52
    n "Gertrude will come to tell us that Clarence arrived."with dis
    n "He'll use the pineapple elevator because that's the one closest to his parking space. We won't be able to see him go to his office."
    show dn 53
    n "Then I'll follow after Gertrude with some excuse, and I'll call Clarence's office pretending to be the front desk."with dis
    n "I'll tell him that he's required there immediately, for some emergency."
    show dn 54
    n "If he buys it, he'll go to the pencil case elevator, so you should see him walk past this room!"with dis
    show dn 55
    n "You’ll then have about 7 or 8 minutes to sneak into his office, before he returns."with dis
    n "Try finding all the info you can from his laptop, and then take the pineapple elevator so you can avoid him."
    mc "Simple and to the point."
    mc "I like it."
    play sound chair2
    show dn 56
    mc "What if he turns off the laptop? I guess it'll be password protected."with dis14
    show dn 57
    n "He shouldn't. I came last Sunday too, and I saw him leave the laptop open while he grabbed some coffee." with dis04
    n "The key is to make him believe there’s no one else on this floor, so make sure he doesn't see you when he walks past this room."
    show dn 56
    mc "Understood." with dis04
    show dn 57
    n "Any questions?" with dis04
    show dn 56
    mc "All clear!" with dis04
    mc "I guess all we have to do now is wait for Gertrude to come and tell us that Clarence is here."
    show dn 57
    n "That's right." with dis04
    n "Anything you want to discuss in the meantime?"
    n "Do you have better control of your powers in Eternum?"
    show dn 56
    mc "I do! Although, I haven't been able to play much this weekend." with dis04
    mc "I needed some rest."
    mc "What about you, though? I heard the ERE bent the knee!"
    show dn 57
    n "Ah, I see word travels fast!" with dis04
    show dn 56
    mc "How did you do that?!" with dis04
    show dn 58
    n "Erm... well..."with dissolve
    stop music2 fadeout 7
    play music rotundamusic fadein 8
    show screen daybeforecorner
    scene by 1 with Dissolve(2.5)
    pause
    if sparejasticus:
        scene dn 59
    else:
        scene dn 59b
    leg "Ladies and gentlemen..." with dis12
    leg "The leaders of the proud factions of Macedonia and the Eastern Roman Empire are here to make an announcement!"
    play sound crowdcheer volume 1.2
    cro "*Cheers*" with hpunch
    show dn 60
    mac "My queen, I'll admit that it is an absolute honor to join the WRE under your command."with dis12
    mac "All of my armies are at your disposal."
    show dn 61
    n "That is very generous of you, Marcellus."
    n "All your people will be treated with dignity and respect, and you have access to the resources of the WRE."
    show dn 60
    mac "You're too kind, my queen."
    mac "Thank you."
    show dn 62
    mac "Macedonia will join the Western Roman Empire!"with dis12
    mac "LONG LIVE THE EMPRESS!"
    play sound crowdcheer volume 1.2
    cro "*Cheers*"with hpunch
    play sound2 spit2 volume 1.2
    ere "*Spitting on the ground* Pathetic."
    show dn 63
    ere "I expected more from you, Marcellus." with dis
    ere "You're lame."
    show dn 64
    n "Welcome to Rome, Cicero."
    n "It is a pleasure to finally meet the proud leader of the ERE."
    n "I have heard great things about you."
    show dn 63
    ere "Shut up, whore. I will not be fooled by your false humility, like all these other clowns."
    ere "The ERE will never bend the knee!"
    show dn 64
    n "You've been defeated, Cicero. Your men are captured and your lands are devastated."
    n "Offer an honorable surrender and save your people."
    n "Some of them make a living here. The bloodbath is unnecessary."
    show dn 63
    ere "And then what? We're the last faction of this server that you haven't conquered."
    ere "If we join you, what do you think will happen?"
    ere "Treason. Riots. A bloated empire cannot equally serve its people."
    ere "Peace will not last."
    show dn 64
    n "Then I'll expand the Empire to other servers."
    n "The WRE knows no borders."
    show dn 63
    ere "*Mocking laugh* Other servers? You're out of your fucking mind."
    ere "This is a roleplaying server, and nothing more!"
    ere "Do you really intend to send your men to other worlds and form an inter-server faction?"
    show dn 64
    n "That is exactly what I intend to do."
    n "Your lack of ambition is frustrating, Cicero."
    n "Join the WRE and your people will be–"
    show dn 63
    ere "The ERE will never join you!!" with hpunch
    ere "NEVER!"with hpunch
    ere "Agh, this is why women can't be the leaders of anything... you just ruin EVERYTHING!"
    show dn 64
    n "*Sighs* In that case, I have no other choice but..."
    show dn 63
    ere "Kill me if you want!"
    ere "I will gladly accept my death! And my men will follow me!"
    show dn 64
    n "Very well."
    n "Maximo, take Cicero and–"
    show dn 63
    ere "They'd rather die than accept the orders of a fucking whore!"
    show dn 64
    n "*Sighs* Take Cicero and–"
    show dn 63
    ere "We will never surrender!"
    play sound jumpscare
    play sound2 jumpscare2
    play music2 risinglong
    stop music
    scene dn65
    n "{sc=2}And crucify him.{/sc}"with hpunch
    ere "W-What?"
    leg "Yes, my Queen."
    ere "*Nervous chuckle* You're kidding, right?"
    n "Grab three iron spikes and nail him to a cross at the entrance of the city."
    n "But station him with an Exit Portal in his line of view. The enticement of escape will only further cause him to be consumed by despair."
    leg "It will be done, my Queen."
    ere "W-What?!"
    n "How much do you think you'll endure, Cicero?"
    n "{sc=2}The nails slowly tearing your flesh.{/sc}"
    n "{sc=2}The insolation of the sun burning your skin.{/sc}"
    n "{sc=2}And the ravens feasting upon your guts...{/sc}"
    n "{sc=2}Peck{w=0.15}, {size=40}peck{w=0.15}, {size=50}peck!{/sc}"
    ere "W-WHAT THE FUCK?!"with hpunch
    ere "This is literally torture! That's against Eternum's General Code of Ethics!"
    n "I don’t seem to see any Praetorians around... do you?"
    ere "You're fucking nuts!"with hpunch
    ere "W-We're just roleplaying! T-This is just a game!"
    n "Is it?"
    n "Do you really want to put me to the test, Cicero?"
    ere "*Hyperventilating* I-I..."
    ere "*Hyperventilating* . . ."
    stop music2 fadeout 2
    play music rotundamusic fadein 2
    show dn 66 with dis17
    pause
    show dn 67
    ere "E-Erm..." with Dissolve(0.7)
    ere "Our men will aid the expansion of the WRE."
    ere "T-The ERE will join the Western Roman Empire."
    play sound crowdcheer volume 1.2
    show dn 68
    cro "*Cheers*"with dis
    n "And?"
    ere ". . ."
    show dn 67
    ere "A-And..."with dis08
    ere "Long live the Empress!"
    play sound2 crowdcheer volume 1.2
    show dn 68
    n "Excellent!"with dis08
    n "You can reach out to Maximo if you need any help from now – I have to log off to make dinner for my family. Tonight’s lasagna night!"
    n "Welcome to the WRE, Cicero."
    n "You made the right decision."
    ere "*Grunting* Hmm..."
    hide screen daybeforecorner
    stop music fadeout 7
    play soundloop rain3 fadein 8
    scene dn 58 with dis22
    n "Um..."with dis08
    n "Well, you know, it's all about diplomacy and dialogue."
    n "I don't want to bore you with it."
    if nancypath:
        show dn 57
        n "But anyway, we've still got some time to kill before the Ulysses rep shows up..."with dissolve
        show dn 56
        mc "Yep..."with dis04
        mc "Any idea about what we could do while we wait?"
        show dn 70
        n "Oh well, some entertaining pastimes come to mind, but they would take too long, I'm afraid."with dis04
        n "And we need to be prepared. No distractions."
        show dn 69
        mc "Oh, really?"with dis04
        mc "And what are those “pastimes”...?"
        show dn 70
        n "Don't tempt me."with dis04
        show dn 69
        mc "Tempting is my pastime."with dis04
        play music2b sexy3 fadein 6
        play sound clothes3
        show dn 71
        bla "Nancy takes a quick step towards you, until you’re face to face. You can feel her body breathing heavily against you." with dis15
        mct "Holy shit..."
        if penelopepath:
            mct "When I’m up close like this, it’s really clear where Penny got her boobs from..."
        else:
            mct "My god, her boobs look even bigger when I’m up close."
        mc "*Groping her butt* (And that ass...)"
        show dn 73
        mc "So... what did you have in mind...?" with dis12
        n "Well... the last time we were alone we were annoyingly interrupted, remember...?"
        mc "Yes, I remember it too well..."
        n "*Whispering* I'm {i}so{/i} fucking horny, [mc]."
        n "I haven't even been able to sleep properly the last few nights."
        mc "Is there something I can do...?"
        n "I was thinking that..."
        n "Maybe..."
        n "We could..."
        stop music2b fadeout 1
        play sound doorglass
        play sound2 doorglassclose
        show dn 74
        ger "Nan, that grumpy man from Ulysses is here." with dis
        show dn 75
        pause
        show dn 76
        n "Huh? Oh, already?"with dis08
    else:
        show dn 56
        mc "*Chuckles* Yeah, I know you can be quite persuasive."with dissolve
        play sound doorglass
        show dn 74
        ger "Nan, that grumpy man from Ulysses is here." with dis
        show dn 57
        n "Oh, already?"
    show dn 74
    ger "Yeah, do you want me to let him know you're looking for him?"
    if not nancypath:
        show dn 57
    else:
        show dn 76
    n "No, no! Don't worry about that..."
    n "How about instead, you and I get some donuts? My treat!"
    n "You deserve it for being such a good friend, Gerty."
    show dn 74
    ger "Hah! Trying to make me fat so you look better standing next to me?"
    if not nancypath:
        show dn 57
    else:
        show dn 76
    n "Guilty!"
    show dn 74
    ger "*Hearty laugh* Okay, okay, I'll accept them! But only if they’re low-fat! Can’t have these sugary foods messing with my flawless skin..."
    if not nancypath:
        show dn 57
    else:
        show dn 76
    n "Sure thing!"
    if nancypath:
        play soundlow chair3
        show dn 78
        if nancymommy:
            n "I'll be right back, Dalia."with dis12
        else:
            n "I'll be right back, [mc]."with dis12
    else:
        show dn 57
        n "I'll be right back, [mc]."
    n "Don't move from here, okay?"
    if nancypath:
        show dn 77
        mct "Oh, jeez, I'm hard as a rock..."
        mc "Um... s-sure!"
    else:
        show dn 56
    mc "I won't go anywhere!"
    if nancypath:
        show dn 78
        n "Good boy..."
    else:
        show dn 57
        n "Thank you."
    play sound2 doorglass
    play sound doorglassclose fadein 1
    show dn 45 with dis2
    bla "Nancy and Gertrude leave the room. Following Nancy's instructions, you hide and wait for your opportunity." with dis
    if nancypath:
        mct "Okay [mc], it's time to leave the horny aside and focus. This is a golden chance to obtain vital info."
    else:
        mct "Okay [mc], it's time to focus. This is a golden chance to obtain vital info."
    mct "Don't screw it up."
    play soundlow thunder fadein 3
    show dn 79
    mct "I wait for that man to leave his office, I sneak into it, I search for info about Thanatos' real identity, and I sneak out." with dis15
    mct "Easy."
    mct "I hope I can find it in time, though."
    mct "I mean, I should. I'm not Nova, but I know how to use Ctrl+F."
    bla "You hear the creak of a door opening in the distance, followed by footsteps."
    show walk05 with dissolve
    play sound footsteps2 volume 1.2
    pause 2.3
    play music2 mystery4 fadein 5
    scene dn 79
    mct "That's gotta be him!"with dis08
    mct "Let's go!"
    show dn 80 with dis17
    pause
    play sound footsteps
    show dn 81 with dis15
    mct "The laptop! Nancy was right!" with dis08
    mct "Okay, I shouldn't waste a second. Even if he doesn't know I was in here, I doubt he'll leave his laptop unprotected for too long."
    play sound chair1
    show dn 82 with dis15
    play soundloop2 type2
    mct "Alright..."with dis06
    mct "I've gotta scan everything."
    mct "Emails, archives, notes, hidden folders, cloud storage..."
    mct "It has to be here."
    mc ". . ."
    mct "There's only .csv files in here..."
    mct "Nothing over here either..."
    mct "No results for any of my keywords..."
    mct "Come on, come on, come on..."
    stop soundloop2
    mct "Hmm?"
    mct "G.O.D. Reports."
    play sound type1
    mct "{i}10th Gem - undiscovered. 9th Gem - undiscovered, 8th Gem - undiscovered. 7th Gem..."
    show dn 83
    mct "{i}[mc] [lastname], ID number 421,200,234!"with dissolve
    mct "Holy shit, it's this!"
    mct "That's the Gem I found with Luna at the Red Herring server!"
    mct "The one that Thanatos took from me in Ogygia!"
    play sound2 type1
    show dn 82
    mct "I bet he somehow had access to these files too. That's how he found me so fast after I retrieved the gem."with dissolve
    mct "So then... he must have some way to track players down inside Eternum."
    mct "I got you, motherfucker. One step closer to unraveling all your secrets."
    play sound3 type1
    mct "1st Gem..."
    show dn 83
    mct "WYATT. R. PITMAN."with dissolve
    mct "Oh my god, all his fucking info is here!"
    mct "Born February 17th, 1999."
    mct "230 Old Ridge Trail, Evergreen, WA."
    mct "Eternum ID number 002,155,727."
    mct "This is way more than I thought I’d find!"
    mct "We... We know Thanatos' identity!"
    play sound type1
    show dn 82
    mct "But I can’t get too excited, I should make a run for it before that guy gets back."with dissolve
    mct "Or... maybe I could try finding out something else?"
    menu:
        with dis12
        "Other Gem of Doom owners":
            $ gemowners = True
            play sound2 type1
            mct "What about the other first owners?" with dis06
            mct "6th Gem... Sugawara Tsuneo. Hmm... doesn't ring a bell."
            mct "Maybe this is the one that's not in Thanatos' possession?"
            play sound2 type1
            mct "5th Gem... Connor M. Kuvner."
            mct "This has to be Xet's brother. Thanatos stole their Gem in Ekabar."
            play sound2 type1
            mct "4th Gem... Sang Hyun-Ki. That's gotta be Garrington's Gem."
            mct "I suspected that he didn't find it himself... it would be easier for him to buy one, or have someone steal one for him."
            mct "In any case, that's the Gem of Doom I have now."
            play sound2 type1
            mct "And the 2nd and 3rd Gems... A. Lopes and K. Dixon. Hmm, I don’t recognize either of them."
            mct "But I guess it doesn't matter, Thanatos got to them long ago and stole their Gems."
            mct "Hmm..."
        "Next Ulysses' event":
            $ gemevents = True
            play sound2 type1
            mct "What about Ulysses' upcoming events..." with dis06
            mct "I heard some of them have very good rewards. Annie got her swords in one of those."
            mct "Hmm... there's a new special event scheduled for December."
            mct "“The Big Hunt.”"
            mct "Prize... TBD."
            play sound2 type1
            mct "There doesn't seem to be any further info about it. Too bad."
            mct "We should look into it..."
        "The Founder":
            play sound2 type1
            mct "Maybe something about the Founder?" with dis06
            mct "Hmm... nothing."
            mct "Not surprising."
            play sound2 type1
            mct "But look at this... there's a notarized contract certifying that the person who collects all 10 Gems will receive ownership of Ulysses and become its new CEO."
            mct "Typical obfuscating legal language aside, there doesn’t seem to be any loophole here. It’s fairly straightforward."
            mct "Interesting."
            mct "This still doesn't answer the biggest question, though: why is he doing this?"
            mct "Hmm..."
        "[red]Leave":
            mct "No, that's enough." with dis06
            mct "I shouldn't risk it."
    play sound doorglassclose
    play sound2 doorglass
    stop music2 fadeout 1
    show dn 84 with dis12
    cla "What the hell..." with dis
    play soundlow thunder fadein 3
    show dn 85
    cla "Who the fuck are you?!" with dis12
    mct "Fuck..."
    mc "T-This isn’t what it looks like, sir."
    cla "Are you trying to steal classified information from us?"
    mc "Um..."
    mc "Okay, maybe it {i}is{/i} what it looks like, but I can explain!"
    mc "I-I just thought I could find a cheat code or something if I..."
    cla "Don't bullshit me, kid."with hpunch
    cla "Did the Founder send you?"
    mc "No one sent–"
    mc "Wait, the Founder...?"
    mc "Aren't you supposed to be working with him?"
    cla "Fuck, William warned me that this could happen..."
    mct "William...? William Bardot?"
    mct "What’s going on?"
    mc "Um... l-look, I didn't see anything, I swear."
    mc "I'll leave immediately, but p-please, don't call the police."
    play sound thunder fadein 3
    play soundlow risinglong1 volume 0.33
    show dn 86
    cla "The police...?" with dis15
    cla "No, the police can’t know about this, boy."
    mc "What?"
    cla "I'm afraid you're not leaving this building on your own, son."
    cla "My boss can’t know about this slip-up."
    mc "W-What...?"
    cla "Someone probably should have taught you this lesson long ago."
    cla "This is what happens when you mess around where you shouldn't."
    mc "O-Okay, I think I'm gonna–"
    cla "Do you think you're the first one to try this?"
    cla "Fucking fools like you think all of this is nothing more than a game, and when they realize the truth... it's already too late."
    mct "I don't like this..."
    cla "I'm sorry, but this is how it has to be."
    cla "You. {w}Don't. {w}Fuck. {w}With."
    play sound baseballskull volume 1.2
    stop soundloop2
    stop soundlow
    stop soundloop
    show dn87 with hpunch
    pause .8
    play sound2 ["<silence 0.3>", fall3]
    play sound3 ["<silence 0.3>", fall2]
    play sound4 ["<silence 0.3>", fall]
    scene dn 88 with dis
    pause 1
    n ". . ." with dis
    mc ". . ."
    mc "H-Holy shit!"with hpunch
    play music2 office fadein 4
    show dn 89
    n "[mc]! Are you okay? I'm sorry, I thought he'd go to the front desk, but for some reason he turned around and came back here instead."with dis15
    mc "I’m fine! Damn, good hit, Nancy!"
    mc "You saved me!"
    n "He'll probably be sleeping for a while, but we should tie him up, just in case."
    n "Can you help me?"
    mc "O-Of course!"
    play sound rope
    play sound2 ["<silence 0.6>", rope2]
    play sound3 ["<silence 1.1>", knot]
    show dn 90
    bla "You muzzle Clarence’s mouth and tie up his hands and feet." with dis2
    n "There you go! Now be good and stay quiet!"
    show dn 91
    mc "Phew, okay, this certainly wasn't part of the plan." with dis12
    show dn 92
    n "It wasn't, for sure."with dis04
    n "I'm sorry, [mc], I didn't want to get you into this mess."
    show dn 91
    mc "Will we get in trouble somehow?"with dis04
    show dn 92
    n "I don't think so."with dis04
    n "No one apart from Gertrude knows you're here, and I convinced her to leave already."
    n "And honestly, I don't think he'll even try to contact security. He sounded too proud for that."
    n "Regardless, I’ll stop by security and see if I can sway them, if necessary."
    show dn 91
    mc "And he’s way too scared of his superiors. I'm sure he won't say a thing."with dis04
    show dn 92
    n "We should leave the building immediately, though."with dis04
    n "Just in case."
    show dn 91
    mc "Agreed. And hey, let's celebrate! The mission was still a success!"with dis04
    mc "I discovered Thanatos' real identity!"
    show dn 94
    n "Oh! Now we're talking!" with dis12
    if nancypath:
        n "That's my boy..."
    show dn 93
    mc "I've got everything on him."with dis04
    mc "Real name, ID number, and even his address!"
    show dn 94
    n "Really? Where does he live?"
    n "Do I need to start looking for flights to Zimbabwe?"
    show dn 93
    mc "That's the best part!"
    mc "He's American!"
    mc "He lives in Evergreen, Washington!"
    n "Hmmm..."
    show dn 94
    n "That's kind of close, actually. Maybe a 5-hour drive."
    show dn 93
    mc "It is."
    n "Hmmm..."
    show dn 94
    n "Are you thinking what I'm thinking...?"
    show dn 93
    mc "Well, if you're thinking about getting in the car and driving 5 hours right now to plant Nova's device and get that bastard where he’d never expect it..."
    mc "Then yes, we're thinking the same thing."
    show dn 94
    n "*Giggles* You seem too excited about this."
    show dn 93
    mc "I mean, stealing 5 Gems of Doom from Eternum's number one player is exciting in its own right."
    mc "But, I also have a little vendetta to settle..."
    show dn 94
    n "I see... I'll admit that I’m pretty tempted to ambush him now too."
    show dn 93
    mc "Alright then..."
    mc "The mission continues?"
    show dn 94
    n "Definitely."
    show dn 93
    mc "Let's go!" with hpunch
    stop music2 fadeout 5
    if not nancypath:
        jump thanahouse
    play soundloop vent fadein 5
    show dn 80 with dis2
    pause
    play sound elevator
    show ds 1 with dis2
    mc "Where did we leave the car?"with dis08
    mc "Was it floor negative 8?"
    mc "It was that one, right?"
    play sound2 ding
    play sound3 elevator
    mc "*Clicking on the button* Yeah, I think so."
    show ds 2
    mc "Alright!" with dis12
    mc "Let's recap what we know so far."
    mc "We know Thanatos' real identity. If we manage to steal his Gems of Doom, we'll have a total of 6, if we include the one in our possession."
    mc "Then there's another one in the hands of an unknown player... who's probably not the first owner."
    mc "We know initial owners get their names recorded, and given that Thanatos hasn't been able to track them down, it’s likely the Gem has transferred hands."
    mc "And finally, there are 3 Gems still hidden in the world of Eternum."
    n ". . ."
    mc "Um..."
    mc "Nancy? Are you listening to me?"
    show ds 3
    n "Yeah..."
    n "Can I ask you something, [mc]?"
    show ds 5
    mc "Huh? Of course."
    mc "What's the matter?"
    show ds 4
    n "It's just that..."
    show ds 3
    n "*Chuckles* I feel so silly."
    n "You know, I might not look like it, but I've been through a lot."
    n "And over the years, I’ve gotten to know myself pretty well."
    n "I know what I want. But... I was young myself once."
    n "And I feel like I've been acting on my own without actually thinking about you."
    show ds 2
    mc "Huh?"
    mct "What’s gotten into her?"
    menu:
        with dis
        "I just want what's best for you":
            show ds 5
            mc "I just want what's best for you."with dis08
            mc "I want to see you happy."
            mc "I'll do anything within my reach to accomplish that!"
            n ". . ."
            show ds 3
            n "You're too kind, [mc]."
            n "*Chuckles* That might come back around to bite you someday."
            n "But thank you, I'm glad to hear that."
        "Maybe we should forget about “us” until...":
            show ds 5
            mc "Maybe we should forget about “us” until we've dealt with the whole Gems thing." with dis08
            mc "We have a lot on our plates."
            n ". . ."
            show ds 3
            n "Yeah, that's... exactly what I meant."with dissolve
            n "*Chuckles* I mean, just look at everything that’s happened to us."
            n "The war at Semper Invicta, the risk with Penelope, Dalia, and Annie... even Gertrude interrupted us!"
            n "And that's not even taking into account our age difference or my background as your old nanny."
            n "Everything's just... too complicated."
            show ds 4
            n "I'm sorry, [mc]."
            n "I didn’t mean to make you uncomfortable."
            show ds 5
            mc "Nonsense."
            mc "I forbid you from making this something awkward."
            mc "But, as you said, it's just better if we don't overcomplicate things."
            mc "You haven’t stopped being sexy as fuck, though."
            mc "Don't blame me if I keep dropping my jaw when I see you."
            show ds 3
            n "*Chuckles* I won't, I promise."
            n "And you! Try not to walk around shirtless!"
            n "It’ll drive me crazy!"
            show ds 5
            mc "*Chuckles* I can try."
            mc "Alright, now that that's clear... ready to continue our mission, ma'am?"
            show ds 3
            n "Ready as I'll ever be."
            show ds 5
            mc "Then let's go!"with hpunch
            $ nancypath = False
            $ nancyu = False
            stop soundloop fadeout 3
            jump thanahouse
        "[gr]I know what I want, too":
            show ds 5
            mc "I know what I want, too." with dis08
            mc "And I wanna be with you."
            mc "You can call me selfish."
            n ". . ."
            $ nancy_points += 1
            show screen heartbeat
            play sound beat
            show ds 3
            n "I see..."with dissolve
            n "That's good to know."
    n "*Sighs* It's just that..."
    n "I've been thinking, you know?"
    show ds 2
    mct "Oof, thinking is not good..."
    show ds 3
    n "Our age difference, my daughters, the Student Exchange Program, my history as your former nanny..."
    n "And also my job, and everything that we've got going on with Eternum and Ulysses."
    n "Everything's just... so complicated."
    show ds 2
    mct "Aw, shit, I don’t like where this is going..."
    show ds 3
    n "*Chuckles* Every single time we’ve tried... something, we were interrupted."
    n "Penelope, Dalia, Annie, Gertrude, Maximo..."
    n "There's always something stopping us, as if... as if we’re not meant to take that next step."
    n "It’s like we’re fighting against fate or destiny or something like that."
    show ds 6
    mc "W-What?"with dis15
    mc "That's absurd!"
    mc "All this destiny thing is such bull–"
    play sound2 switch
    bla "Nancy presses the emergency stop button."
    stop soundloop
    play sound elevatorstop
    scene elevatorstop with vpunch
    pause 1.5
    mc "W-What are you doing?!" with dis06
    mc "Nancy?"
    play sound7 generator
    $ renpy.music.set_volume(0.45, channel='music3')
    play music3 nancysexy fadein 9
    show ds 7
    bla "The elevator's emergency lights flash on." with dis
    mc "Oh..."
    show ds 8
    n "But then I thought..." with dissolve
    n "...fuck that."
    n "If destiny doesn't want to give me an opportunity... I'll create my own."
    n "I'll take what I want."
    n "And what I want... is you, [mc]."
    show ds 7
    mc "I like that way of thinking..."with dissolve
    show ds 8
    n "What about you? Do you know what you want...?"with dissolve
    play sound3 clothes3
    show ds 9
    mc "*Caressing her cheek* Fuck, Nancy..." with dis12
    mc "You know exactly what I want."
    mc "We still have a yoga session pending, don't we?"
    show ds 10
    n "Ah, you're very right, mister. What an eager boy..."
    show ds 9
    mc "Should we continue it now?"
    show ds 10
    n "Hmmm... now seems like as good a time as any..."
    show ds 11
    mc "Maybe we should get a bit more comfortable, then." with dis12
    mc "These clothes look a little restrictive... Do you mind if I help you get rid of them...?"
    n "Mm-hm..."
    show ds 12 with dis12
    pause
    play sound buttons
    play sound2 clothes4
    show ds 13
    bla "You rip off the buttons of Nancy's blouse, revealing her bra and increasing your temptation to unfathomable levels."with dis
    mc "Fuck, yes..."
    mc "I'm gonna eat you up, Nancy..."
    play sound3 woodhit
    play soundlow elevatorstop
    show ds 14
    n "*Pushing you against the wall* Oh no, no chance!" with dis12
    if nancy03scene:
        n "That already happened last time, remember?"
    show ds 16
    n "Now... it's my turn." with dis
    if nancymommy:
        n "Let your mommy take care of you. You’ve been such a good boy, after all..."
    else:
        n "Let me take care of you..."
    show ds 15
    mc "With pleasure..."
    show ds 16
    n "Any special requests...?"
    show ds 15
    mc "Hmm..."
    mc "Take off your bra. I wanna see those perfectly shaped tits of yours again..."
    show ds 16
    if nancymommy:
        n "Oh my, are you not excited enough? Wanna play with my titties in front of your face again, baby boy?"
    else:
        n "Oh my, are you not excited enough? Wanna play with my titties in front of your face again?"
    show ds 15
    mc "You could say that... I’ve always been more of a... tactile learner."
    mc "Just the idea of your tits isn’t enough for a hedonist like me..."
    show ds 16
    n "*Giggles* I don't know, you look plenty excited to me, [mc]."
    n "That bulge in your pants gives you away."
    show ds 15
    mc "You're denying my request, then? Such a tease..."
    show ds 16
    n "Oh, not at all."
    n "I’m just trying to take back some control of the situation... can’t have you getting too antsy, sweetheart..."
    n "But... it'd be very rude if I refused."
    play sound clothes4
    show ds 17 with dis15
    pause
    play soundlow ["<silence 0.2>", clothes2]
    show ds 18
    if nancymommy:
        mc "That's it, Mommy..." with dis12
    else:
        mc "That's it, Nancy..." with dis12
    play sound2 clothes3
    show ds 19
    bla "Nancy removes her bra, exposing her hefty tits to the cold elevator air." with dis15
    mc "Oh god..."
    mc "Can you... can you give me a little spin?"
    show ds 21
    n "*Giggles* You're wasting your time, [mc]." with dis12
    n "This emergency stop is only temporary. If someone calls for the elevator, it’ll start up again..."
    n "Tick, tock, [mc]..."
    show ds 20
    mc "I don't give a fuck. I've been craving this moment for so long... nothing’s gonna stop me from enjoying this to the fullest."
    show ds 21
    n "*Chuckles* Living in the present, eh?"
    show ds 20
    mc "Life is too short to never take risks..."
    show ds 21
    n "I couldn't agree more. As long as what you do doesn't hurt anyone... sometimes you’ve gotta just take a chance."
    show ds 20
    mc "Taking a chance, eh? Maybe I should start taking more chances with you, too."
    show ds 21
    n "I’d like to see you try, [mc]..."
    show ds 22 with dis14
    n "*Kneeling down* You know, my mother used to say that risk-takers defy destiny with every decision. I’ve always kept that thought in my head."with dis06
    mc "Very wise woman, indeed..."
    play sound belt
    play sound2 clothes5
    show ds 23 with dis17
    n "Jesus..."with dis06
    n "What do they feed you boys nowadays?"
    mc "Do you like what you see?"
    play sound3 ["<silence 0.8>", slapsoft] volume 1.2
    show ds 25
    bla "Nancy reaches out and gently wraps her hand around your meat, before slapping it across her cheek."with dis12
    mc "O-Oh, god..."
    show ds 24
    n "Y-yeah, I guess you could say I like it..."with dissolve
    show ds 25
    mc "Fuck, Nancy..."with dissolve
    mc "You have me throbbing..."
    show ds 24
    n "You sure have a lot of love to give, [mc]."with dissolve
    show ds 25
    mc "What can I say, hot red-headed MILFs are my weakness..."with dissolve
    show ds 24
    n "MILFs, eh? I thought you’d have been playing around with all those younger girls..."with dissolve
    if nancymommy:
        n "Were you actually saving your loads for Mommy...?"
    else:
        n "Were you actually saving your loads for me...?"
    show ds 25
    mc "You can have as many loads as you want..."with dissolve
    show ds 26
    bla "Nancy moves her tongue southward and begins giving small licks to your balls. "with dis15
    mc "O-O-Ohh..."
    show ds 24
    n "*Giggles* Mmmm... guess I’ve gotta check what you’ve been saving for me..." with dis15
    show ds 26
    mc "Take it into your mouth, please..."with dis15
    mc "I need it..."
    show ds 27
    n "Mmmm..." with dis15
    mc "Oh my god..."
    show ds 28
    n "Mmmm..." with dis14
    show ds 27 with dis14
    mc "Oh... Nancy..."with dis06
    mc "That's it... suck it fast..."
    $ renpy.music.set_volume(0.15, delay=10.0, channel='music3')
    play soundloop blowjob2 fadein 2
    scene nancyele1 with dis2
    mc "AAaaaahhh..." with dis
    mc "That's it..."
    mc "J-Jesus Christ, this feels too good..."
    bla "Nancy’s pillowy lips wrap around your girth, and you can’t help but let out a noise."
    n "*Moaning* MMmMmm..."
    mc "Keep looking in my eyes, Nancy..."
    n "Mmmm..."
    mct "I’ve known Nancy all my life... yet I’m still not used to the size of her enormous bust..."
    mct "All those years, and still no sag..."
    mct "No back problems, either."
    n "*Gagging* MmmMmmm..."
    if penelopepath:
        mct "Hmm... between Nancy and Penelope... I wonder who's got the bigger pair..."
        mct "Penny did say that Nancy has a habit of stealing her bras..."
        mct "Man, I wish I could compare the two pairs."
        mct "Mother and daughter..."
        n "*Gagging* Mmmggghh..."
    mc "Aghhh... yeah..."
    mc "Keep pumping it, Nancy..."
    pause
    bla "Nancy continues to milk your cock with a steady rhythm, as her expressions grow more and more lecherous." with dis
    mc "AAaahh..."
    mc "G-God, how long can you keep that pace?"
    mc "D-Don't you need to breathe?"
    n "Mmmm...?"
    stop soundloop fadeout 1
    play sound blow4
    show ds 24
    n "*Catching her breath* I'm just breathing through my nose."with dis12
    n "You can reduce stress and anxiety just by controlling your breathing. You can learn a lot from yoga."
    mc "Ah, I guess that–"
    play soundloop blowjob2 fadein 2
    scene nancyele2 with dis2
    bla "Nancy envelops your shaft inside her mouth before you can even finish your sentence."with dis
    mc "A-a-a-a-aaaahhh..."
    mc "Jesus..."
    mct "I was hoping she’d be good at this, but she's blown me away..."
    mc "Aaaahhh, yeah, that’s it..."
    mct "Nancy doesn’t seem to be interested in stopping before sucking the life out of me..."
    mc "Please, Nancy, don't stop..."
    pause
    stop soundloop fadeout 1
    play sound blow4
    show ds 29
    n "*Recovering her breath* AAAghh... FUCK!"with dis
    mc "Ah, your nose-breathing technique failed you?"
    show ds 24
    n "I guess I'll have to keep training..." with dis
    show ds 25
    mc "I think I have some free time for practice between our yoga sessions..."with dissolve
    show ds 24
    n "Good idea! But for today... I have something else in mind."with dissolve
    show ds 25
    mc "Oh... and what might that be...?"with dissolve
    play sound3 woodhit volume 0.4
    play soundlow elevatorstop
    show ds 30
    bla "Nancy pulls you to the ground and swings her leg over you." with dis12
    mc "Oh boy..."
    mc "Wait..."
    mc "You're not wearing panties?"
    play sound clothes4
    show ds 31
    n "*Straddling you and lifting her skirt* I guess I woke up a little naughty today." with dis12
    show ds 32
    if nancymommy:
        mc "What a naughty mommy..."
    else:
        mc "How naughty..."
    show ds 31
    n "You had no right to turn my life upside down like this, [mc]."
    n "I can't get you out of my head."
    n "Every single minute."
    n "Every single day."
    n "I... {w}NEED you... {w}inside me..."
    show ds 32
    mc "Oh my god..."
    mc "Are we..."
    mc "Are we really gonna do this?"
    mc "Are we..."
    show ds 31
    n "Yes, we are. We're gonna continue right where we left off last time, [mc]."
    n "I promised you, remember?"
    show ds 32
    mc "Oh fuck, yes..."
    mct "Oh my god, I'm about to fuck Nancy."
    mct "S-She's about to fuck me!"
    mct "Is this really gonna happen?"
    show ds 31
    n "Yes, it IS going to happen."
    show ds 32
    mc "W-What? Can you read my mind?"
    show ds 31
    n "Your face is like an open book, [mc]."
    show ds 32
    mc "Oh... I can imagine..."
    mc "I can't help but get the feeling we're about to get interrupted once again."
    mc "Right before the best moment."
    mc "Something's gonna happen..."
    n "*Giggles* Hmm."
    show ds 31
    n "Not this time, baby boy."
    n "This time, I won't let anything or anyone stop me."
    n "This time..."
    show ds 33
    n "You're all mine..." with dis17
    mc "O-Oh my god..."
    scene nancyele3 with Dissolve(3)
    pause 4.5
    play soundlow penetration2
    mc "AAaaaaahh...{w=5.6}{nw}" with dis2
    scene ds 34
    n "*Squeals* AAAAAAaaaaagggghh..." with Dissolve(1.7)
    n "Y-YEAH!"
    n "A-Are you ready...?"
    mc "O-O-Oh, god..."
    $ renpy.music.set_volume(0.1, delay=5.0, channel='music3')
    scene nancyele4 with dis2
    pause .5
    mc "OH M-MY FUCKING GOD..." with dis14
    bla "Nancy starts moving up and down. Your penis spreads her wet lips apart, while quickly adjusting to the redhead's vicious pace."
    n "O-Oh m-my g-goddd, [mc]...."
    n "*Moaning* This is..."
    n "AAaahhh..."
    n "T-This is it..."
    n "You're finally inside me, baby..."
    mc "F-FUUUUCK..."
    n "*Moaning* Y-You have no idea how long I've been..."
    n "AAhhh..."
    n "...how long I've been fantasizing about this moment..."
    mc "F-Fuck, me too, Nancy..."
    mc "Your pussy feels so good..."
    mct "I'm inside Nancy... I'm fucking her..."
    mct "This is not a dream, it's happening..."
    n "*Moaning* Aaaahh..."
    pause
    scene black with dis
    scene nancyele5 with dis2
    n "AAAaaahhh..." with dis
    mc "G-God..."
    n "D-Does it feel good, [mc]?"
    mc "*Panting* I've never felt anything so incredible..."
    mc "You f-feel... absurdly good."
    n "I can feel your cock f-filling me... aahh... every inch of it pumping in and out of me..."
    n "S-So much...."
    n "*Squeals* AAaaghh..."
    n "I bet you must drive the girls at your school crazy..."
    mc "W-Well..."
    if eva1 or maatsex:
        mc "T-Truth is, I've never done something like this in the real world."
    else:
        mc "T-Truth is, I've never done something like this."
    n "Oh... well..."
    n "Let me show you what you've been missing, then..."
    mc "Oh fuck yes..."
    n "MmmmMm..."
    n "I-I want more..."
    n "I {i}need{/i} more, baby..."
    mc "More?"
    if nancymommy:
        n "Can you handle me going faster, sweetie? I’ll start slowly... and it’ll make your mommy feel so much better..."
    else:
        n "Can you handle me going faster, sweetie? I’ll start slowly... and it’ll make your old babysitter feel so much better..."
    mc "F-Faster?"
    mc "Y-Yeah, I can take it..."
    n "That's my boy..."
    pause
    play sound blow5
    play sound2 clothes3
    scene ds 35 with dis15
    bla "Nancy gets off of you and removes her skirt." with dis15
    mc "*Panting* O-Okay, I just need a second."
    mct "Come on, [mc], you can do it."
    mct "Don't cum yet, don't cum yet, don't cum yet, don't cum yet."
    show ds 36
    n "You good?"
    show ds 35
    mc "Y-Yeah! I'm fine!"
    play sound clothes4
    play soundlow clothes2
    show ds 37b with dis15
    pause .1
    bla "Nancy hops back onto you and guides your member into herself once more." with dis
    n "Good..."
    play sound3 blow4
    show ds 37
    mc "O-Oh god..."with dis15
    n "Because..."
    play sound2 blow4
    play sound4 penetration2
    play soundlow woodhit
    show ds 38 with vpunch
    mc "S-Shiiiit..." with dis
    n "Because I don't plan to stop riding you until one of us faints..."
    mc "Oh boy..."
    scene nancyele6 with dis2
    n "*Panting* AHHH..." with dis
    n "F-FUCKKK!"
    mc "OH GOD..."
    n "R-RIGHT THERE!"
    mc "Oh, fuck yeah, Nancy..."
    n "AAAAHGH..."
    bla "Nancy's pussy stretches around you, her wet folds surrounding the entire length of your dick."
    bla "The relentless onslaught of her hips is somehow balanced by the dance that her perfect breasts perform in front of you."
    mc "Jesus Christ..."
    n "YEAH... YEAH!"
    n "G-God, I needed this {i}so{/i} much, [mc]..."
    n "Y-You have no idea..."
    n "All this time..."
    n "Everything is paying off for this one moment..."
    mc "AAahhh..."
    mc "Y-Yes..."
    mc "FUCK YES!"
    mc "Are you enjoying riding me, Nancy?"
    n "Fuck yes, I am..."
    mc "Have you ever taken a cock like mine?"
    n "N-Not even close..."
    pause
    scene black with dis
    scene nancyele7 with dis2
    n "AAAAAHHH..." with dis
    bla "Nancy's screams fill the small enclosed space, echoing against the high ceiling."
    mct "I wonder how thick the walls of the elevator are... could anyone hear us?"
    n "Y-YEAH!"
    mc "G-God..."
    mc "I-I hope there are no security cameras in the elevator."
    n "H-HAH!"
    n "T-That would be quite the spectacle, eh...?"
    n "The poor security guard having to watch the two of us – AGH... FUCK! – h-having sweaty, animal sex in an elevator in the middle of the day..."
    n "O-One for the spank bank, for s-sure..."
    mc "I b-bet..."
    n "AAahh..."
    n "Luckily there are no cameras in this one, since it doesn't go to the labs..."
    mc "Too bad... I'd have liked to take a souvenir home..."
    pause
    n "AAAhh..." with dis
    n "*Panting* Jesus, my legs are going numb..."
    n "I'm not sure I can..."
    scene black with dis
    scene nancyele9 with dis2
    bla "Without letting her finish her sentence, you grab her tightly and begin to slam her." with dis
    n "AAAAAaaaGHH, BABYYYYY!"
    n "*Gritting her teeth* M-MY GOD!"with hpunch
    mc "AAAaghh, fuck, Nancy..."
    n "*Squealing* J-Jesus Christ, y-you're like a fucking bull..."
    mc "All I wish to do is to serve my queen..."
    n "AAAGH..."
    n "Y-Yeah..."
    n "That's it..."
    n "Harder..."
    n "H-HARDER!"with hpunch
    n "Fuck your queen, [mc]..."
    n "F-Fuck your queen with that m-monster fucking cock of yours..."
    n "AAAAghh!"
    mc "*Panting* I can feel you soaking my balls with your juices..."
    n "AAAhhh F-FUCK, t-this is insaaaanee..."
    n "AAAAH!"with hpunch
    mc "Let me hear you scream like that... I fucking love making you feel that way..."
    pause
    scene black with dis
    scene nancyele8 with dis2
    bla "Nancy's voice rises in pitch as you hammer away inside her, fucking her for all you're worth." with dis
    n "*Screaming* AAAAAAAGHHH!" with hpunch
    mc "Oh f-fuck yeah!"
    n "*Squealing* AAAAaaaaaahh...."
    if nancymommy:
        mc "What a naughty mommy... what if your daughters could see you being fucked like this?"
    else:
        mc "What a naughty empress... what if your subjects could see you being fucked like this?"
    n "*Screaming* AAAAAaahh..."
    mc "Do you like being fucked roughly by me?"
    n "I-I LOVE IT..."
    n "AAAaahh..."
    mc "I knew it..."
    n "*Panting* M-Make me yours, [mc]..."
    bla "Each wild slam of your hips hits the deepest parts of Nancy’s inner cavity."
    n "Oh m-my god, I'm gonna cum, [mc]..."
    n "You're gonna make me cum..."
    n "Keep fucking me like this, please..."
    n "I-I'm almost there..."
    n "AAAAAAHHH..."
    n "J-Just a bit more, baby..."
    if nancymommy:
        n "M-Make your mommy cum!"
    else:
        n "M-Make your queen cum!"
    pause
    play sound cum1
    play sound2 cum2
    play sound3 slap1
    scene ds 39
    n "AAAAAAARGH!!!!" with hpunchlong3
    bla "Nancy's body trembles as wave after wave of pleasure runs through her entire body. Her thighs squeeze against you, and you wince from the stress of not cumming right then."
    n "*Recovering her breath* My god..."
    n "GGGGggghh... This one was even better than the orgasms you gave me in Semper Invicta..."
    play sound6 clothes3
    show ds 40b with dis15
    n "*Struggling to her feet* Dear Lord..."with dis08
    n "How the hell do you do it..."
    play sound3 woodhit volume 0.5
    play soundlow elevatorstop
    show ds 40
    mc "*Pushing her against the wall* Come here..."with dis
    n "*Panting* W-What are you doing..."
    mc "We're not done yet, Nancy..."
    n "W-What?"
    n "I-I can't continue! I'm exhausted, [mc]..."
    mc "Don't worry, my queen, just lean against the wall and let me do the work here..."
    show ds 41
    n "*Giggles* Y-you're fucking nuts."with dis14
    n "Are you never satiated?"
    mc "I could never get my fill of you..."
    scene nancyele10 with dis2
    n "AAAAAARGGGHH... g-good Lord have mercy..." with dis08
    n "*Screaming* AHHHH!"
    n "[mc!u]!!!" with vpunch
    mc "M-My god..."
    mc "Your pussy is so fucking addictive..."
    mc "I can't stop myself..."
    n "AAAahh..."
    n "D-Don't stop then..."
    n "F-Fuck me again, [mc]..."
    n "P-Pin me against the wall and fucking lay into me!!"
    n "GGGGaghh!" with vpunch
    n "M-Make a mess of me, baby..."
    mc "I'm gonna fuck the shit out of you..."
    n "Oh my gggawd..."
    mct "It’s taken me everything I have not to cum already."
    mct "I want this sensation to last as long as possible, but... I can’t help but want to pound Nancy’s cunt until I collapse..."
    mc "Oh, Nancy..."
    n "Ohgaaawf..."
    mct "She's completely gone... the things she's saying don't even make sense anymore."
    bla "You pump your cock in and out of Nancy's lascivious body for several minutes until her ass cheeks start reddening."
    pause
    mct "Think I can shift up one more gear..."with dis
    scene black with dis
    scene nancyele11 with dis2
    n "*Screaming* AAAAAAAGH..." with dis
    n "AAAAH!" with vpunch
    mc "Oh god, Nancy, I'm getting close..."
    n "I'm c-c-cummingg already... a-again....."
    mc "I'm g-gonna cum too..."
    n "*Panting* I-If you’re gonna cum, then cum, baby..."
    n "*Panting* Don’t worry about this being the only time we do this... I p-promise we’ll do it again..."
    n "Now cum for me, let me take care of you..."
    if nancymommy:
        n "Cum for Mommy, baby..."
    else:
        n "Cum for your queen, baby..."
    n "G-GOD!" with vpunch
    mc "FUUUUCK, I'M..."
    n "W-WAIT! D-D-DON'T CUM INSIDE!!"
    mc "I'm almost there..."
    n "N-Not inside!" with vpunch
    n "AAAHhh!"
    n "I c-can't have another child!"
    mc "*Panting* W-Would that be that bad...? Look at these hips, Nancy... I’m p-pretty sure you’re meant to have some more kids..."
    n "[mc] s-s-stop joking!"with vpunch
    mc "Oh fuck..."
    mct "Oh god, this is gonna be harder than she thinks..."
    mct "I wanna fill her up so badly..."
    mct "I can’t upset her, though... not if I want to do this again..."
    n "[mc!u]!!!" with vpunch
    mct "Oh fuck, I'm gonna–"
    play sound ["<silence 0.4>", blow4]
    play sound2 ["<silence 0.4>", blow5]
    scene ds 43 with dis
    bla "You pull out at the last second." with dis08
    play soundlow slap1 volume 0.5
    play sound4 cum1
    play sound5 cum2
    play sound6 cum3
    show ds 44
    mc "AAAAAAAAAAAAAAHHHH..." with hpunch
    play sound cum1
    play sound2 cum2
    play sound3 cum3
    mc "AAAaaaaaahh..." with vpunch
    $ nancy_points += 2
    play sound7 beat
    show screen heartbeat
    n "*Orgasming again* AAaaaahh..."with vpunch
    stop music3 fadeout 14
    play soundloop2 vent volume 0.4 fadein 6
    show ds 45 with dis17
    mc "*Hyperventilating* Jesus fucking Christ..." with dis
    mc "Oh Nancy..."
    mc "I don’t think I've ever cummed so hard in my life..."
    n "*Exhausted chuckle* Hah..."
    n "Is it that bad?"
    mc "Well, you're definitely gonna need a shower when you get home..."
    mc "God..."
    mc "Nancy, this was..."
    n "*Still breathing heavily* D-Don't even try it. I can’t describe it either..."
    n "Where did you learn to–"
    play sound ding
    play soundloop fan volume 1.3
    stop soundloop2 fadeout 3
    show ds 45 with vpunch
    pause .3
    play sound2 woodhit
    play sound3 elevatorstop volume 0.3
    show ds 46
    n "*Leaning against the wall* Oh no."with dis12
    show ds 47
    mc "What's this?"
    show ds 46
    n "T-The elevator! Someone called it!"
    show ds 47
    mc "W-What?!"
    show ds 46
    n "F-Fuck, they can't find me like this!"
    n "What if it's my boss? They're gonna fire me!"
    n "I can't be fired, [mc], I have a family to feed!"
    show ds 47
    mc "T-Then get dressed!"
    show ds 46
    n "Yes... YES! My clothes!"
    show ds 48
    n "P-Pass me my blouse!" with dis12
    mc "And the bra?"
    n "There's no time! H-Hide it in your pants or something!"
    mc "Uh, kinky..."
    n "N-Not now, [mc]!"
    play sound2 ding
    stop soundloop
    show ds 48 with vpunch
    pause 0.6
    play sound3 elevator
    show ds 49 with Dissolve(1.6)
    pause 1.1
    play music2 office fadein 5
    show ds 50
    ger "Oh! Nancy!" with dis12
    ger "You're still here? I thought you left!"
    if nancymommy:
        ger "And hi again, Dalia."
    else:
        ger "And hi again, [mc]."
    mc "H-Hi Gerty."
    show ds 51
    n "*Coming out of the elevator* G-Gertrude!" with dis12
    n "I-I was about to ask you the same thing."
    n "I thought you left like... an hour ago."
    show ds 52
    ger "Yeah, I did, but then I noticed I left my binder on my desk, so I had to come back to get it."
    show ds 51
    n "Awww, I'm so sorry, they locked the office already!"
    show ds 52
    ger "They... locked it? Why?"
    show ds 51
    n "You know, the... fumigation."
    show ds 52
    ger "Fumigation...?"
    show ds 51
    n "Yeah! You didn't get the memo?"
    show ds 52
    ger "The... o-oh!"
    ger "Of course, of course, I was the first one to get it."
    show ds 51
    n "Yeah, we should go back home, things can get pretty dangerous with all the chemical agents and everything."
    show ds 52
    ger "Of course."
    ger "Let's leave before it ruins our perfect skin!"
    ger "See you tomorrow, I guess?"
    show ds 51
    n "S-Sure! Same time, same desk."
    n "Anyways..."
    n "I've gotta leave you now, we were going to... visit a friend."
    mc "Yep!"
    show ds 52
    ger "Sure thing, Nan."
    show ds 53
    ger "Before you leave, though..."with dissolve
    ger "I've gotta ask, do you know you're going around without shoes?"
    show ds 54
    n "Oh!"
    n "I must have left them in my office!"
    n "I'm such a scatterbrain. How embarrassing."
    mc "You had an extra pair in the car, if I remember correctly!"
    n "Ah, you're very right! I should go get them before I slip on something or hurt my feet..."
    n "*Clears throat* Alright, I'll see you tomorrow! Goodbye, Gerty!"
    show ds 55
    ger "See you tomorrow, Nan!" with dis12
    ger "I'll be in the salon if you wanna drop by later!"
    n "*Walking out the door* Sounds wonderful!"
    ger "Well... I guess I'll go back to my car too, I don't wanna get contaminated."
    show ds 56
    ger "*Sniffing* Ugh, these elevators smell more and more like sweat everyday."with dissolve
    ger "They should fire the entire cleaning staff."
    ger "And... are those Nancy's shoes?"
    ger "She left them inside the elevator! This woman is a total scatterbrain..."
    show ds 55
    ger "Good thing she has someone as observant as me in her life..." with dissolve
    stop music2 fadeout 5
    jump thanahouse


label thanahouse:
    scene black with dis25
    show screen afewhourslater with dis15
    pause
    hide screen afewhourslater with dis2
    play soundloop forest2 fadein 3
    scene de 1 with dis25
    mc "*Snoring softly* Zzzzzz..." with dis15
    n "Wake up, [mc]!"
    n "We're here!"
    show de 2
    mc "Hmmm?" with dis12
    mct "Where am I...?"
    mct "This..."
    show de 3
    mc "Oh, right! Thanatos!"with dis08
    mc "Man, I knocked out as soon as the car drove off."
    show de 4
    n "Yeah, you really needed the rest!"with dis08
    n "*Chuckles* Your eye bags were starting to terrorize children."
    play sound2 cardooropen
    show de 5 with dis15
    play sound cardoor
    pause .1
    mc "*Stretching your legs* AGHH!" with dis
    mc "Ahh, I feel like a new man!"
    mc "How long was I out?"
    n "Almost 6 hours!"
    mc "Not bad."
    if nancypath:
        mc "Damn, I had such a great dream, though..."
        mc "There was action and fear and espionage... but the best part was that it ended with me having sex with a hot redhead in an elevator."
        show de 9
        n "*Giggles* Oh, really?" with dis
        n "And how was that?"
        show de 8
        mc "Unforgettable..."
        show de 9
        n "Wow, look at that smile on your face. Seems like you definitely enjoyed yourself."
        show de 8
        mc "You took the words right out of my mouth. She gave me the ride of my life."
        mc "If I close my eyes, I can still see her gorgeous body absolutely hammering me into the ground..."
        mc "*Sighs* The sad thing about dreams is that they always seem to fade away after a while."
        mc "Do you think I'll ever be able to dream about that redhead again...?"
        show de 9
        n "I don't know..."
        n "Maybe if you're good, karma will reward you... and the woman will pay you another visit..."
        show de 8
        mc "Damn, seems like I should be on my best behavior then."
        show de 9
        n "Sounds like it!"
        n "But maybe don’t be too much of a goody two-shoes..."
        n "Fortune favors the bold."
        show de 8
        mc "Ah, I'll keep it in mind..."
        show de 9
        n "*Chuckles* Let's keep these dreams of yours between us, though. I don’t know how my daughters would take the news."
        show de 8
        mc "My lips are sealed!"
        n "*Giggles* Mm-hm."
        mc "God, that gave me enough fuel to run across the country."
        mc "I'm filled with energy and ready to kick some ass! Let's plant Nova's device and steal those Gems!"
    else:
        show de 7
        mc "I'm filled with energy and ready to kick some ass! Let's plant Nova's device and steal those Gems!"with dis12
    mc "Which way, ma'am?"
    show de 6
    n "Well, about that... we're already there, actually."with dis
    n "This is the place."
    play music2 founder fadein 7
    show de 10
    mc "Oh? T-This is... Thanatos' home?" with dis17
    mc "Are you sure?"
    n "Yep."
    mc "Isn't this a bit risky? I thought we'd park away from the house."
    n "That was my plan too, but I lost the GPS signal shortly after taking this road. Before I knew it, we were right in front of the house."
    mc "I see."
    mc "It looks a bit..."
    n "Abandoned, right?"
    mc "Yeah..."
    show de 6
    n "There's almost nothing else within a 10-mile radius, and I didn't see any other vehicle on the way up here, so it's definitely empty."with dis
    show de 7
    mc "Strange. Maybe it's a second home?"
    show de 6
    n "I don't know... if it is, they left it to decay, that's for sure."
    show de 7
    mc "Do you still want to go take a look?"
    show de 6
    n "Yeah, it's the least we should do after coming all the way up here."
    show de 7
    mc "I agree."
    mc "Let me go first. If by chance someone is inside, we're a door-to-door Bible salesman and his hot assistant."
    show de 9
    n "And where are the Bibles you're selling, Mr. Bible salesman?"with dis08
    show de 8
    mc "Trust me, they'll be too busy checking out my hot assistant to notice anything strange."
    show de 9
    n "*Chuckles* Okay, okay, if you say so... you go first."
    n "I’ll follow you."
    show de 11 with dis17
    pause
    play sound stairswood
    show de 12 with dis2
    mc "Should we knock?"with dissolve
    n "Um... well, I would."
    mc "But what if Thanatos himself is really living here?"
    n "Hmm... maybe knock and hide by the door. Let me do the talking."
    n "He doesn't know who I am, we have an advantage."
    mc "True that."
    mc "*Taking a deep breath* Alright, here goes nothing."
    play sound dooropencreak
    show de 13
    bla "The door of the old house swings open at your slightest touch." with dis22
    mc "*Gulps* Well... that pretty much confirms it."
    mc "This place was abandoned long ago."
    show de 14
    mc "*Going into the house* Jeez, everything's falling apart." with dis15
    n "Yeah, watch your step."
    play sound3 footsteps volume 1.5
    show de 15 with dis2
    mc "Abandoned places have always given me the creeps."with dissolve
    mc "Thank god we arrived before nightfall."
    n "I feel kind of uncomfortable here. Trespassing like this, y’know?"
    mc "It's a deserted house, don't worry. The door wasn't even locked. And there aren’t any cars around."
    show de 16
    n "But take a look at this." with dis
    n "It's full of... junk. As if the people who lived here had to run away all of a sudden, without being able to pack their things."
    n "Either that, or there are actually people still living here."
    mc "I don't know..."
    mc "Let's go take a quick look upstairs, and then get out of here."
    play sound stairswood
    show de 17 with dis2
    pause
    play sound3 footsteps volume 1.4
    show de 18 with dis2
    n "What's over there?" with dissolve
    mc "Nothing, just a bathroom. And there?"
    n "Just a small bedroom."
    play sound2 footsteps volume 1.5
    show de 19
    bla "You and Nancy go down the end of the hall, and find another empty bedroom." with dis2
    mc "And... nothing."
    n "*Sighs* What a disappointment."
    play sound chair1
    show de 20
    n "*Sitting down* We came all this way for nothing."with dis14
    n "It isn't even worth leaving Nova's device here, and we haven’t found any clues."
    n "I guess we got too excited, too soon."
    show de 21
    mc "Don't say that!"with dis08
    mc "We still have Thanatos' real name, and this was the address he had when he registered to play Eternum."
    mc "Let's call Nova!"
    mc "Maybe he moved somewhere nearby, I'm sure she'll be able to find out his current address."
    show de 22
    n "That's a good idea." with dis06
    n "Will she answer if you call her now?"
    play sound chair1
    show de 27
    mc "*Chuckles* I'd bet anything that she will." with dis
    mc "Ever since she got her first phone, it's been like a new toy for her."
    mc "If she doesn't answer she's either sleeping or playing Eternum. There's no other possibility."
    play soundloop2 phone2
    show de 23 with dis08
    pause 3.5
    play soundloop rain3
    stop soundloop2
    stop music2
    play sound w1
    play sound2 beep2
    $ unlock_look("nova", 9)
    show de 24
    if novapath:
        no "HI [mc!u]!!!" with pushr
        no "I was just thinking about you!"
    else:
        no "Hey, [mc]." with pushr
        no "What's new with you?"
    play soundloop forest2
    show de 27
    mc "Well, well, well... it took you a whopping 2 seconds to answer the phone this time, Nova."
    mc "Is everything alright? Did something happen?"
    play soundloop rain3
    show de 25
    no "It's not my fault! I was on the other side of the room sorting my manga collection."
    no "That's like... a solid 10 feet!"
    if novapath and penelopepath:
        show de 26
        no "And well, I'm still a little hungover, so that slowed my speed."with dissolve
        play soundloop forest2
        show de 27
        mc "Yeah, I meant to ask you about that, are you feeling better?"
        play soundloop rain3
        show de 24
        no "Definitely!"
        no "I got up at 3 PM, took a shower, washed out the blue dye from my hair, scarfed down some food, and... well, it's been raining since then, so I didn't do much else."
        show de 25
        no "Ah, and my mom scolded me for having my eye uncovered for so long last night."with dissolve
        play soundloop forest2
        show de 27
        mc "Oh, right! Does it hurt you now?"
        play soundloop rain3
        show de 26
        no "Not at all!"
        show de 25
        no "I mean... well, it hurt a little when I came back from the party, but... nothing to worry about."with dissolve
        no "I know my limits. My mom’s just being a worrywart."
    elif leavepartyearly:
        show de 26
        no "And well, I'm still a little hungover, so that slowed my speed."with dissolve
        play soundloop forest2
        show de 27
        mc "*Awkward laugh* Oh... yeah, the party... I'm sorry I left early, I wasn't feeling that well."
        play soundloop rain3
        show de 24
        no "It's okay, don't worry. We left early as well."
        show de 25
        no "Penny looked a bit sad, though. Or... maybe she was mad. I'm not sure."with dissolve
        mct "Oh shit, I hope she's not angry with me."
    show de 24
    no "But anyway, what are you up to?" with dissolve
    no "How did the mission go? Do you have Thanatos' name?"
    play soundloop forest2
    show de 28
    n "We do!"
    play soundloop rain3
    show de 24
    no "Oh, hi, Nancy!"
    no "That's great news!"
    play soundloop forest2
    show de 29
    n "We even found the address he used to initially register with Ulysses! Since it was relatively close, we decided to come immediately."
    n "Unfortunately, the house is completely abandoned."
    play soundloop rain3
    show de 25
    no "Agh, that sucks."
    no "Maybe he moved?"
    play soundloop forest2
    show de 29
    n "Yeah, we thought the same."
    n "Would you be able to discover his current address if we gave you his name?"
    play soundloop rain3
    show de 26
    no "Please, that's like asking a weightlifting champ if he can do 10 pushups."
    no "Easy peasy!"
    play soundlow chair1
    play soundloop2 type2
    show de 30
    no "I just need his full name, and I'll be able to give you his current address and all of his social networks in less than... 15 seconds."with dis12
    play soundloop forest2
    stop soundloop2
    show de 27
    mc "Really? And how are you gonna do that?"
    play soundloop rain3
    play soundloop2 type2
    show de 30
    no "A magician never reveals her tricks, [mc]!"
    play soundloop forest2
    stop soundloop2
    show de 28
    n "Okay, so... his name is Wyatt R. Pitman."
    n "He was born on February 17, 1999. And the address he registered with was 230 Old Ridge Trail, Evergreen, WA."
    play soundloop rain3
    play soundloop2 type2
    show de 30
    no "Got it!"
    no "Give me one second..."
    no "And..."
    stop soundloop2
    show de 31
    no "Uh..."with dis08
    no "Wyatt R. Pitman, Evergreen, you said?"
    no "W-Y-A-T-T R P-I-T-M-A-N?"
    play soundloop forest2
    show de 29
    n "Yes! Is there any problem?"
    play soundloop rain3
    show de 31
    no "Um... I have bad news, guys. That guy is not Thanatos."
    no "Must be a fake name."
    show de 30
    no "He's cleverer than we thought..." with dissolve
    play soundloop forest2
    show de 29
    n "Huh? Why are you so sure?"
    play soundloop rain3
    show de 31
    no "Well... you were right, he did move 5 years ago."
    no "His new address is... Section 8, Stone 19, Evergreen Cemetery."
    no "He's... dead."
    play soundloop forest2
    show de 29
    n "What?! Wyatt R. Pitman died 5 years ago?!"
    n "Are you sure?"
    play soundloop rain3
    show de 30
    no "A hundred percent. Thanatos must be using fake identities of dead people to cover his tracks."
    no "Would go with the whole “Greek god of death” thing."
    no "Although... he shouldn't be able to. I guess that reinforces our theory that he's working for Ulysses."
    play soundloop forest2
    show de 29
    n "Agh... that's {i}bad{/i} news. We might be back to square one."
    n "*Sighs* Anyway, thank you, Nova."
    play soundloop rain3
    show de 30
    no "Is there anything else you need?"
    play soundloop forest2
    show de 29
    n "Not right now... but thank you so much."
    n "We'll start heading back to Kredon now."
    play soundloop rain3
    play soundlow chair1
    show de 24
    no "Okie-dokie!" with dis
    no "I'm gonna play Eternum for a bit with Alex and Dalia."
    if novapath:
        no "But let me know when you're back! Maybe you can join!"
    no "See you later!"
    play soundloop forest2
    show de 27
    mc "Goodbye, Nova! Have fun!"
    if novapath:
        mc "And thanks once again, number one hacker girl!"
    play sound2 clothes3
    show de 20
    n "*Sighs* What a waste of time..." with dis14
    n "We really got too ahead of ourselves..."
    show de 21
    mc "Don't say that!" with Dissolve(.7)
    mc "We had to try it, it was too good of an opportunity."
    mc "So no long faces! Come on, let's go back to Kredon."
    mc "And let’s get something to eat along the way! My treat!"
    play sound clothes3
    show de 32
    n "*Chuckles* How do you do it, [mc]?"with dis14
    play music2 lovepiano fadein 8
    show de 33
    mc "Huh?"with dissolve
    mc "Do what?"
    show de 32
    n "Always staying positive. You’re so optimistic!"with dissolve
    n "During this Thanatos scheme, during the heist, even during the gladiator fight in Semper Invicta! You never seem to falter."
    show de 33
    mc "Oh... well, I don't know, I've always been a pretty hopeful person."with dissolve
    mc "You have to fuck with me a LOT to make me upset. Unless you mess with someone I care about - then it’s a different story entirely."
    mc "I learned long ago that a half-full glass is better than a half-empty one. At the end of the day, all I can do is keep moving forward."
    show de 32
    n "But the thing is that... it's not just {i}you{/i} moving forward."with dissolve
    n "I'm not sure how you do it, but you make others feel good too. Your optimism, your reassurance... it’s contagious."
    n "You have a gift! Even if you don't realize it yourself."
    show de 33
    mc "*Chuckles* I'm not so sure, to be honest. I’ve met a lot of people who can't stand me."with dissolve
    mc "But thank you, Nancy."
    mc "Your words are really touching... but I have to imagine that a lot of this optimism stuff is due to you."
    mc "Growing up under your care really affected me."
    show de 32
    n "Me? I don’t think so. I forced myself to swallow my tears and my pain when things went south a few years ago."with dissolve
    n "I kept a mask on because I was afraid that it would scare or hurt my daughters."
    n "And as they grew up, they started copying that same approach."
    n "They hide their insecurities, their fears. They always pretend to be happy, and they’ve gotten so good at it that sometimes even I can’t tell what’s an act."
    n "But... when they're with you... their smiles are genuine. The laughs are real."
    n "You’ve really made the household... authentic. It’s almost like we were missing something before you came back."
    show de 33
    mc "Come off it! You don't need me for all that!"with dissolve
    mc "All I do is point out everything that’s already around you, I didn’t add anything special."
    show de 34
    n "But that’s not an easy thing to do, [mc]. People spend their lives trying to overcome insecurities."with Dissolve(1.6)
    n "Even the prettiest girls feel ugly sometimes."
    n "The people who are always cracking jokes and leaving others with smiles on their faces... you’d be surprised how many of them cry at night."
    n "Even the most independent or popular girls feel alone."
    n "We might all be living different lives, but... when it comes down to it, we're all fighting the same monsters."
    show de 32
    n "I know that what I'm about to say might sound really selfish, but... " with Dissolve(1.6)
    n "Don't leave us again, [mc]."
    n "We need you."
    n "More than you think."
    show de 33
    mc "Well, I don't know what life or the future or destiny hold in store for me, but I can promise you one thing, Nancy."with dissolve
    mc "I'll never leave you or the girls again."
    mc "I swear on my life."
    play sound dooropen2 volume 1.4
    play sound2 ["<silence 0.1>", doorsqueakk] volume 1.4
    stop music2 fadeout 2
    show de 35 with dis2
    play sound3 gunload
    pause
    play sound clothes3
    play soundloop2 beat3 fadein 4
    show de 36
    bla "You slowly stand up and turn around. An old woman points a double-barreled shotgun at you with trembling hands."with dis2
    mc "*Putting your hands up* O-Okay..." with dis
    mc "C-Calm down everyone..."
    play sound holster2
    show de 37
    old "W-WHO ARE YOU?!" with hpunch
    old "WHAT ARE YOU DOING IN MY HOUSE?!" with hpunch
    show de 36
    mc "I-I'm gonna need you to put the gun down..."
    play sound2 holster2
    show de 37
    old "SHUT UP!"with hpunch
    old "You here to rob me? I have n-nothing! NOTHING!" with hpunch
    show de 38
    n "We didn't come to steal from you!"
    n "We..."
    n "Please, calm down, we mean no harm!"
    show de 37
    old "Then why are you trespassing in my house?!"
    old "If you try to trick me, I'm gonna shoot you both! I’ve got nothing to lose!"
    show de 38
    n "Okay, okay! Please just hear us out!"
    n "We'll tell you the truth!"
    n "We..."
    n "We came here to find a man named Wyatt Pitman and-"
    play sound holster2
    show de 37
    wym "What do you want from my son?!" with hpunch
    wym "He's dead! Can't you let him rest in peace?"
    show de 38
    n "T-That's the thing! We got the wrong person!"
    n "We came looking for someone, and we mixed him up with your son!"
    n "I-I know that we shouldn't have entered without permission, but the door was unlocked and... well, anyway, that doesn’t really matter."
    n "I'm so sorry for your loss, Ms. Pitman."
    n "We didn't mean to offend you or Wyatt's memory in any way."
    show de 37
    wym "*Breathing nervously* So..."
    wym "You didn't come to rob me?"
    show de 38
    n "Of course not! I swear on my daughters!"
    show de 36
    wym ". . ."
    show de 37
    wym "Y-You're..."with dissolve
    wym "You're a mother too?"
    show de 38
    n "I am."
    n "I have two girls, Dalia and Penelope."
    n "The younger one will start college next fall, and the older one will graduate in a couple of years."
    show de 36
    wym ". . ."
    play sound gundrop
    stop soundloop2 fadeout 6
    show de 40
    bla "The old woman drops the shotgun on the ground." with dis15
    mct "Oh Jesus, thank fucking god..."
    show de 39
    wym "I'm sorry."
    wym "I..."
    wym "I've been alone since my Wyatt left me 5 years ago. It was just me and him for years, after his father left. He was everything I had."
    wym "When I saw that car parked in the driveway, and I heard a man’s voice coming from upstairs, I thought..."
    wym "I don't even know what I thought."
    wym "I... Whatever you do, you need to hang onto your daughters for as long as you can."
    show de 40
    mct "Damn, I was scared as fuck, but now... poor woman."
    mct "I don't even know what to say."
    show de 39
    wym "Please, I’d like you to leave now."
    wym "And... I'm sorry."
    wym "I can't believe I pointed a gun at someone. I-I shouldn’t have done that."
    play sound footsteps
    show de 41 with dis17
    n "*Taking her hand* I can't even begin to imagine everything you've been through, but..." with dis08
    n "I know what it's like to be a single mother. Everything you've had to struggle with."
    n "But if you’re like me, you’d do it twice over just to see them happy."
    n "Wherever he is... I'm sure Wyatt is really proud of you."
    show de 42
    wym "You're... thanks. It’s been a long time since I’ve... Thank you, you’re a saint."with dis06
    wym "T-Thank you so much."
    show de 43
    n "We're going to leave now and stop bothering you, but I'm gonna give you my phone number." with dis14
    n "*Chuckles* I know I'm just a stranger and this whole situation was not the best way to meet someone, but... if you ever need someone to talk to, please, call me."
    n "I can always lend an ear."
    wym "*Crying* Thank you, dear. I will."
    wym "And I'm sorry again about the..."
    n "Don't even mention it. We're the ones who should be apologizing. You did nothing wrong."
    mct "Nancy really has a heart of gold."
    mct "And a way with words. I wouldn't have been able to appease this woman with just a few sentences like she did."
    show de 44
    mct "I'm glad this ended well."with dis06
    show de 43 with dis08
    pause
    mc ". . ." with dissolve
    show de 44 with dis
    pause
    show de44
    play sound risingshort
    stop music2 fadeout 1.3
    pause 1.23
    scene de 45
    pause
    mc ". . ." with dis14
    play music evil2short fadein 9
    stop soundloop fadeout 18
    show de 51 with dis17
    mc ". . ." with dis
    mc "...is this your son, ma'am?"
    show de 48
    wym "Huh?"
    show de 49
    wym "Ah, yes. That's my Wyatt."with dissolve
    wym "We took that photo a couple of months before he passed away."
    show de 51
    mc ". . ."
    mc "What is he wearing...?"
    show de 48
    wym "Do you mean the reaper shirt?"
    wym "I think it was... from a rock band maybe? Or maybe something from a movie? I know he loved that character, but I don't remember where it was from, sorry."
    show de 51
    mc ". . ."
    mc "And how tall was he? He looks huge."
    show de 49
    wym "Ah, yes, he was!"
    wym "Almost 6'9\", if memory serves."
    wym "He took after his father."
    show de 51
    mc ". . ." with dis12
    mc "And... I'm sorry, but... can I ask you one last question?"
    wym "Of course."
    mc "How..."
    mc "How did he die?"
    show de 50
    n "[mc]!"
    n "Come on, you're going too far."
    show de 49
    wym "Don't worry, it's okay."
    wym "He... he suffered a sudden stroke. Doctors said it was due to a congenital disease."
    wym "However... even if it sounds strange, there's something that gave me some peace of mind."
    wym "*Sad chuckle* You see... Wyatt had a lot of hobbies."
    play sound flashback3 volume 0.7
    scene thanaf1
    aaa "Can a man obtain the power of a god?"
    aaa "Can a human transcend the limitations of mortality?"
    scene de 51 with dis15
    wym "He liked to play basketball." with dis08
    play sound2 flashback3 volume 0.7
    scene thanaf2
    tha "Do you know why Eternum is better than the other world, boy?"
    scene de 52 with dis15
    wym "He loved rock music..."with dis08
    play sound3 flashback3 volume 0.7
    scene thanaf3
    lin "Each NPC has a chip on their neck, similar to our neural implants, that dictates their behavior."
    scene de 53 with dis15
    wym "He loved exercising too."with dis08
    play sound2 flashback3 volume 0.7
    scene thanaf4
    mc "Sometimes I feel like Eternum's NPC behavior is way too realistic..."
    scene de 53 with dis15
    wym "But..."with dis
    wym "By the whims of fate..."
    wym "Wyatt died while doing the thing he loved the most in this world..."
    play sound3 flashback3 volume 0.7
    scene thanaf5
    pause 0.26
    aaa "Will you help us?"with dis08
    play sound4 flashback3 volume 0.7
    scene thanaf6
    pause 0.26
    aaa "Will you help us?"with dis08
    play sound5 flashback3 volume 0.7
    scene thanaf7
    pause 0.26
    aaa "Will you help us?"with dis08
    stop music
    play sound6 flashback3
    show thanaf8
    pause
    wym "...playing Eternum."with dis17
    show de 56 with Dissolve(1.5)
    pause .1
    stop sound
    jump update06

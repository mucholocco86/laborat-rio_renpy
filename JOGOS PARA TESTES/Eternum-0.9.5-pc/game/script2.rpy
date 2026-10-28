label versiontwo:
    show screen afewminuteslater with Dissolve(3)
    pause
    scene aaa 1
    show screen heart
    hide screen afewminuteslater
    with Dissolve(3)
    a "W-What?" with dis
    a "Are you... Are you serious?"
    a "Benjamin..."
    a "...is d-dead?"
    $ money = 1200
    show aaa 3
    mc "I swear! Mr. Keating told us in computer class." with dis
    mc "He said he had a stroke or some shit."
    scene aaa 2
    a "Damn... That's a bizarre coincidence..."
    scene aaa 3
    mc "Coincidence?! That's bullshit!"
    scene aaa 2
    a "Bullshit...?"
    a "What are you saying? Do you think Mr. Keating made all that up?"
    scene aaa 3
    mc "Not Mr. Keating! Whoever made that information public... is trying to cover this whole thing up."
    scene aaa 2
    a "Are you... are you implying that he's dead because the Praetorians excommunicated him?"
    a "Other people have been excommunicated before... and they didn't die."
    scene aaa 3
    mc "Are you sure about that? Have you met any?"
    scene aaa 2
    a "Um... Well, no, but..."
    scene aaa 3
    mc "I'm telling you... there's something strange about this entire situation."
    show aaa 4
    mc "But we shouldn't talk about this here..." with dis
    mc "We don't know who could be eavesdropping..."
    scene aaa 2
    a "W-What? You think someone’s spying on us?!"
    scene aaa 4
    mc "I have a feeling this shit is much bigger than we think, Annie."
    mc "We witnessed the Praetorians killing Benjamin in Eternum, and somehow he's also dead in real life now. We know too much."
    scene aaa 2
    a "Y-You're starting to scare me!"
    a "Eternum is just a game!"
    mc "Just a game? I wouldn't be so sure about that..."
    show aaa 5
    mc "*Whispering* I just noticed..." with dis
    mc "*Whispering* Do you know who that guy is?"
    a "W-What?"
    mc "*Whispering* He's been standing there ever since we sat down..."
    mc "*Whispering* I've never seen him before..."
    mc "*Whispering* I don't like this, Annie..."
    a "But..."
    a "Isn't..."
    a "Isn't that Chang?"
    mc "What?"
    stop music2 fadeout 2
    play soundlow schoolbell
    show aaa 6
    c "'Sup, [mc]!" with dis
    c "All good?"
    mc "Oh..."
    play music2 happy5 fadein 5
    show aaa 7
    mc "Hi Chang!" with dis
    mc "Everything’s just peachy, yep!"
    mc "I'll text you later!"
    mc "Take care, buddy!"
    show aaa 8
    a "Aren't you being just a little too paranoid?" with Dissolve(1.2)
    scene aaa 9
    mc "Okay, maybe they're not spying on us... yet."
    mc "But seriously, there's something fishy about Benjamin's death."
    scene aaa 8
    a "Do you seriously believe the Praetorians killed him in real life?"
    scene aaa 9
    mc "Well... maybe not, but I'm sure it's all connected somehow."
    scene aaa 8
    a "I really believe you're overthinking this."
    a "Not everything has to become a conspiracy thriller, you know?"
    scene aaa 9
    mc "I don't know, Annie... him having a stroke? I'm not buying it."
    show aaa 10
    a "Well, what can we do?" with dissolve
    a "You know I love summoning my inner-Sherlock Holmes as much as you do, but we can't go to Benjamin's house and just start interrogating his parents!"
    show aaa 9
    mc "Yeah, I guess it would be a little awkward if we did that..."with dissolve
    show aaa 10
    a "We both know that Benjamin was not a good person, but it'd be disrespectful to his family..."with dissolve
    a "And we wouldn't get anything out of it anyway."
    a "I think the best thing we could do right now is put all this behind us."
    mc "*Sighs* Maybe you're right..."
    show aaa 11
    l "Hi guys... Mind if I sit with you?" with Dissolve(1.2)
    mc "Luna!"
    show aaa 12
    l "I usually eat alone, but... then I saw you two here, and..." with dis
    show aaa 17b
    mc "SEAT'S TAKEN! CAN'T SIT HERE!" with hpunch
    l ". . ."
    mc ". . ."
    mc "...Sorry, bad Forrest Gump joke. Of course Luna, you’re always welcome with us!" with dis08
    show aaa 17c
    l "Thanks!"
    show aaa 13
    a "*Laughs* Don't mind him..." with dis08
    a "Please, sit down!"
    play sound chair2
    show aaa 15
    l "Thank you." with Dissolve(1.2)
    scene aaa 14
    a "It's so nice to meet you, Luna!"
    a "I heard [mc] managed to win a neural implant at your cafe!"
    a "Giving away a prize like that is so generous of you!"
    scene aaa 15
    l "No worries. I already have my own, so I wouldn't have much use for another."
    scene aaa 14
    a "You play Eternum too?!"
    scene aaa 15
    l "Yes. Actually, [mc] and I are gonna play together later tonight."
    l "We’ll be on a server called \"The Red Herring\"."
    l "Do you wanna join us?"
    scene aaa 14
    a "Oh my god, yes! I'd love to!"
    show aaa 18
    a "Can I play with you guys, [mc]?!" with dis
    a "Please, please, please!"
    show aaa 17
    mc "Wait... Did you say the server was called \"The Red Herring\", Luna? That’s a pretty ominous-sounding name..."
    show aaa 16
    l "Yes. It's a mystery-themed server, with a hint of horror to it as well." with dissolve
    show aaa 17
    mc "Horror? Okay... maybe it'd be better if you didn't join us, Annie." with dissolve
    mc "You know how easily you get spooked."
    scene aaa 19c
    a "W-Whaaat? That's not true!"
    scene aaa 19b
    mc "*Laughs* Come on, the last time we watched a horror movie, you couldn’t sleep alone for an entire two weeks!"
    scene aaa 19c
    a "But that's because I was a kid! I've grown up since then!"
    scene aaa 19b
    mc "Oh yeah? Could’ve sworn that happened less than a month ago..."
    show aaa 20
    l "To be fair, it's definitely more of a mystery server than a horror one." with dis
    l "There’s tales of gory murders, gruesome kidnappings—all sorts of cold cases to crack. You roleplay as a detective and try to figure things out."
    l "I’ve been on a spree of success so far, but I recently ran into one case that I just can't seem to solve."
    l "Maybe with our three minds put together, we can unravel the mystery."
    show aaa 18
    a "See?! It's just a fun-filled mystery server!" with dis
    a "We both love mysteries!"
    default anniehorror = True
    show aaa 19
    l "It's not a very crowded server, so odds are we’ll be by ourselves most of the time."
    menu:
        with dis
        "Let Annie come with you [pink][mt](Annie +1)":
            mc "*Sighs* Okay, okay." with dis
            mc "I guess you can join us..."
            $ annie_points += 1
            play sound "beat.ogg"
            show aaa 18
            show heartr at topleft
            with dissolve
            hide heartr
            a "Yay!" with dissolve
            show aaa 19
            mc "But you're not allowed to complain if you’re scared, Annie!"
            show aaa 18
            a "Who, me? Scared? Never!"
            show aaa 19
            mc "We'll see about that..."
        "Don't let her come with you":
            $ anniehorror = False
            mc "I'm sorry Annie, we both know you can't handle horror... no matter how light it is." with dis
            show aaa 19c
            a "What? Seriously?!" with dis
            a "You’re just going to ditch me like that?!"
            show aaa 19b
            mc "It’s in your best interest!"
            show aaa 19c
            a "Bah! Fine. I'll go back to Ion!"
            show aaa 19b
            mc "That's a better idea!"
    show aaa 16
    l "I'm sorry if I interrupted your conversation before." with dis
    show aaa 17
    mc "Nah, no worries. We were talking about Benjamin. I was just about to head out, anyways..." with dissolve
    show aaa 16
    l "Oh, yeah... Benjamin's death... That whole situation is really tragic..."with dissolve
    scene aaa 18
    a "[mc] actually thinks there's some sort of conspiracy behind it."
    show aaa 19
    l "Conspiracy? How so?"
    show aaa 17
    mc "Well... Don't tell anyone, but..."
    mc "When we were playing yesterday, Annie and I saw Benjamin get shot by a Praetorian."
    mc "He was about to rape a girl, but then a Praetorian appeared and excommunicated him."
    mc "Between that and his death in real life... I think the timing of everything is an odd coincidence, to say the least."
    mc "I want to dig further into the cause of his death, but wouldn’t even know where to start."
    mc "So... yeah, I guess we're better off just forgetting about the whole thing."
    show aaa 16
    l "Well, actually..." with dissolve
    l "If you really want to investigate... I might know someone who could help."
    show aaa 17
    mc "Oh really? Who?"with dissolve
    show aaa 16
    l "It's someone I met at my dad's cafe. Her name is Nova." with dissolve
    l "She owes me a favor... or, at least, that’s what she said last time we were together."
    l "I wasn't going to ask her for anything, but... if you tell her I sent you, she might be able to lend a helping hand."
    l "If there’s anyone that could help in a situation like this, it’s her. She's an... \"investigator\"."
    l "To be honest, I'm a little curious about it too. Something does feel a little off about Benjamin's death..."
    show aaa 17
    mc "Awesome! She sounds like just what we need." with dissolve
    mc "I feel like in this situation, every second counts, but I don't wanna visit her today if that means we have to postpone playing together..."
    show aaa 16
    l "I think there's time for everything."with dissolve
    l "Nova lives near me, so... you can just come over to my place to play. Of course, that’s if you want to..."
    l "To save the trip of having to go all the way back to your house..."
    l "You’ll only need your neural implant — I have an extra visor and suit you can borrow."
    show aaa 17
    mc "That sounds perfect! Thanks Luna!" with dissolve
    play sound chairmove
    show aaa 20
    mc "I should get going then! I don't wanna be late." with Dissolve(1.2)
    l "Sure, I'll see you later."
    l "I'll text you my address. And Nova’s."
    mc "Sounds good!"
    mc "Take care girls, I'll see you both in a couple of hours!"
    play music2b rain3 fadein 5
    stop music2 fadeout 4
    scene aaa 21 with Dissolve(3)
    mc "(Oh shit, I got too excited and forgot I still have a couple of classes left.)" with dis
    mc "(Well, there’s only two hours left in the school day. Maybe it wouldn’t hurt if I left early. I’ll just have to make up an excuse tomorrow and tell the teachers I felt sick or something.)"
    scene aaa 22 with Dissolve(2)
    play sound vibration
    pause .5
    play sound vibration
    pause .3
    mc "*Looking at your phone* (Ah, there's Luna's message.)" with dissolve
    mc "(Hmm... Nova's house isn’t that far. I should be able to get there within the hour. I just have to make sure I make it to Luna’s place by...)"
    mc "(What?! Raining again?!)"
    mc "(But... the sun was just shining 5 minutes ago...)"
    show aaa 23 with Dissolve(1.5)
    mc "(Well, the clouds don’t look that bad.)" with dis
    mc "(Hopefully the rain will pass quickly.)"
    play sound2 punchlocker
    play soundlow thunder
    show aaa 24
    mc "WHAT THE...!" with hpunch
    ax "Grrr..."
    show aaa 25
    mc "What the fuck do you want now, Axel?!" with dis08
    show aaa 26
    ax "You..."with dissolve
    ax "You motherfucker..."
    ax "YOU KILLED BENJAMIN!!" with hpunch
    show aaa 25
    mc "What?! What the hell are you talking about?!"with dissolve
    show aaa 26
    ax "I saw you during computer class! You were nervous and sweating! You know something, don’t you?!"with dissolve
    show aaa 25
    mc "Are you out of your mind? I didn't kill Benjamin!"with dissolve
    show aaa 26
    ax "I know a fucking pussy like you could never do it, but you must’ve been involved somehow!"with dissolve
    show aaa 25
    mc "I told you! I don't know shit about that fucking bastard!"with dissolve
    show aaa 26
    ax "WHAT DID YOU JUST SAY?" with hpunch
    show aaa 25
    mc "You heard me! Benjamin was an awful person."with dissolve
    mc "Am I supposed to speak well of him just because he died? Forget that he was a jerk and a fucking rapist?!"
    mc "He deserves no respect. Not now and not ever!"
    mc "That scumbag is better off dead."
    play soundlow thunder
    show aaa 26
    ax "SHUT THE FUCK UP! YOU DON'T KNOW ANYTHING ABOUT HIM!" with hpunch
    show aaa 25
    mc "I know enough."with dissolve
    show aaa 26
    ax "You're so done!!"with dissolve
    ax "I will ruin your life! And the lives of all the whores around you!"
    show aaa 27
    mc "What?"with dis
    ax "I saw you at the cafeteria... Hanging out with that nerd and the other freak."
    ax "Probably bragging about how well your plan to kill Benjamin went!"
    default axelpunch2 = False
    menu:
        with dis
        "Punch him [pink][mt](Alex +1)":
            $ axelpunch2 = True
            play sound punch
            play sound2 bonebreak
            scene aaa 28
            ax "Aaaargh!"with hpunch
            play sound punch
            scene aaa 29
            mc "MMMPGH...!" with hpunch
        "Try to calm him down":
            mc "Okay, that's enough." with dis
            mc "I had nothing to do with Benjamin's death and neither did the girls. Now leave me alone!"
            ax "LIAR!!" with hpunch
    if axelpunch2:
        play soundlow punch
    scene aaa 30 with Dissolve(2)
    if axelpunch2:
        play soundlow punch
    prof "Huh??!" with dissolve
    prof "What in tarnation is going on here?!"
    if axelpunch2:
        show aaa 31
    else:
        show aaa 32
    prof "Axel! [mc]! THAT'S ENOUGH!" with dis
    ax "You're dead! You hear me? DEAD!"
    if axelpunch2:
        show aaa 33
    mc "In case your simple brain didn’t hear me earlier, I said I don't know shit about Benjamin's death."with dis
    mc "But I swear to God, if you ever insult Annie and Luna again, or lay even a finger on them... you’ll be reunited with Benjamin in no time!"
    play soundlow thunder
    prof "[mc]! I said that's enough!" with hpunch
    ax "You'll regret the day you ever messed with a Bardot, you fucking cocksucker!"
    ax "Just wait... When you least expect it, I’ll be there to teach you your lesson."
    play soundlow punch
    show aaa 34
    ax "AND YOU! Take your hands off me, beggar!" with hpunch
    ax "Touch me again and my family will have you fired before you know it!"
    prof "I-I'm sorry Axel, I d-didn't..."
    ax "Shut the fuck up."
    scene aaa 35 with Dissolve(2.1)
    prof "Okay, can you explain to me what the hell just happened?" with dis
    prof "Getting into fights at school already? You haven’t even made it through your first week! Seriously, [mc]?"
    mc "He's the one who..."
    prof "I don't want to hear any excuses."
    prof "I'll have to record this incident in your permanent record. One more infraction and you'll be expelled."
    prof "If that happens, you'll forfeit your scholarship and have to return to the UK."
    mc "What? Why am I being singled out here?! He's the one who threatened me!"
    prof "I said that’s enough! Consider this your final warning."
    scene aaa 22 with Dissolve(2)
    mc "*Sighs*" with dissolve
    mc "(Son of a bitch...)"
    mc "(Axel can threaten me all he wants... I'm not gonna back down.)"
    if axelpunch2:
        mc "(Although... Perhaps I shouldn't have punched him. I don't wanna be expelled...)"
        mc "(Bah, fuck it. I'd do it again in a heartbeat.)"
    mc "*Sighs* (Anyway, I need to get out of here.)"
    mc "(Let's see if Luna's contact can help me with this whole thing...)"
label novafirstencounter:
    stop music2b fadeout 6
    stop music2 fadeout 6
    play music rain2 fadein 5
    show aab 1 with Dissolve(3)
    play sound carpasswet
    play sound2 sneeze
    mc "*Sneezes*" with dis
    mc "(Hmm... More storm clouds rolled in... I guess the rain won’t be leaving any time soon.)"
    play sound2 sneeze
    mc "*Sneezes*" with hpunch
    mc "(Brrr... This wind is freezing!)"
    mc "(This damn weather...)"
    show aab 2
    mc "(Let's see if I can find this woman before I catch a cold...)" with Dissolve(1.2)
    mc "(Her house should be somewhere around here...)"
    show aab 3
    mc "(420 Maple Street.)" with dis
    mc "(Oh wait, that's Luna's address.)"
    mc "(Hmm... 369 Rue Lorain Avenue.)"
    show aab 4
    mc "(Rue Lorain? Oh, I'm already here! Lucky me.)" with dissolve
    show aab 5 with Dissolve(1.9)
    mc "(Alright, number 369. This should be the one.)" with dissolve
    mc "(It feels weird ringing the doorbell like this, with me being a stranger and all. Oddly enough, Luna knew this woman's address but not her phone number.)"
    mc "(Anyway, I guess that...)"
    play soundlow doorclose2
    scene aab 6 with Dissolve(1.3)
    play sound2 keys
    mc "(Oh...)" with dissolve
    show aab 7
    aaa "Whaaat? Rain again?! Why do I even bother listening to that stupid weatherman? Sunshine, my ass..." with dis
    aaa "*Sighs* I'm so sick of this damn weather!"
    show aab 8
    aaa "I need to move to Nevada. With the constant rain this place gets, I should probably trade my car in for a boat." with dis
    mc "*Clears throat*"
    show aab 9
    aaa "Huh?" with dissolve
    aaa "Uh, hi there. Can I help you with something?"
    mc "Hello! Um... Sorry to be so forward, but a friend gave me your address and I was wondering if you could help me with something."
    aaa "What? Me?"
    mc "Uh... well, I'm looking for... Nova."
    show aab 10
    san "Oh! My name is Sandra. I'm Nova's mother." with dis
    show aab 11
    mc "Oh... I'm sorry ma'am."
    scene aab 10
    san "No problem at all!"
    san "Are you one of Nova's friends from school?"
    scene aab 11
    mc "Um... Yes."
    mc "(Nova's still in school? How is she supposed to help me investigate Benjamin's death?)"
    mc "(I thought she'd be a police officer or a detective.)"
    scene aab 10
    san "Did you come by for some help with your studies?"
    scene aab 11
    mc "Erm... yeah, but if she's not home, I’ll get going."
    mc "(Probably not a good idea to talk about this stuff with her mother.)"
    mc "I'll come back another time."
    scene aab 10
    san "I was just leaving for work, but you can wait for her inside if you want. You shouldn't be walking around in terrible weather like this."
    scene aab 11
    mc "Thank you very much for the offer, but I can't stay long. I have a busy afternoon."
    scene aab 10
    san "Alright then, I'll let her know you stopped by."
    san "And sorry, your name is...?"
    scene aab 11
    mc "[mc]! B-But you don't need to tell her! I'll just... text her later!"
    mc "No need to worry about it!"
    mc "It was a pleasure to meet you!"
    show aab 9
    san "Text her...? But she doesn't..." with dis08
    show aab 12
    san "Oh look who it is! Hey there honey!" with dis
    mc "(Oh shit...)"
    play sound carpasswet
    show nova1 with dis12
    pause 7
    scene aab 13 with dis
    pause
    $ novau = True
    san "Nova! Agh, look at you!" with dis08
    scene aab 14
    san "You're all drenched!"
    san "I thought I told you this morning to bring an umbrella with you!"
    scene aab 15
    no "I did! But I uhh... left it on the train."
    scene aab 14
    san "Again?!"
    san "I bet you got distracted, playing on your laptop as usual."
    scene aab 15
    no "Um... perhaps. But it doesn't matter, I can buy a new one."
    scene aab 14
    san "I’m not worried about the umbrella—I’m worried about you!"
    san "Look at your clothes! You're gonna catch a cold!"
    scene aab 15
    no "I’m not worried. My immune system is too strong for that."
    no "A little rain never killed anyone."
    scene aab 14
    san "Well, in any case, I want you to change out of those wet clothes and take a warm shower immediately!"
    scene aab 15
    no "Alright, alright..."
    scene aab 14
    san "And where are your manners, young lady?"
    show aab 16
    san "Your friend [mc] came all the way here just to see you!" with dissolve
    san "Say something to him!"
    show aab 17 with Dissolve(1.2)
    pause
    mc "Um..." with dissolve
    show aab 18 with dis
    no "You... came to... see me?" with dissolve
    show aab 19
    mc "Y-Yeah!" with dissolve
    mc "(Oh god, this is awkward.)"
    mc "You were going to help me study for that upcoming quiz, remember?"
    show aab 18
    no "Quiz...?" with dissolve
    show aab 19
    mc "Yes! We talked about it this morning at school!"with dissolve
    mc "(Please, just go with it...)"
    show aab 20
    no "Ooooh... [mc]!" with dis
    no "I remember now, of course! Sorry, my mind is a little fuzzy. Didn’t get much sleep last night."
    show aab 21
    no "Please, come on in!" with dis
    no "Make yourself comfortable!"
    mc "What? Oh well, there's no need for that."
    mc "We can uhh... study... out here...?"
    no "Nonsense! I insist."
    scene aab 12
    no "You're leaving for work, right Mom?"
    san "Yes, and I'm gonna miss my bus if I stay here another minute. Though, if it keeps raining this hard, I might need a ride on Noah’s ark..."
    san "Your father left a few minutes ago and I might have to work a little bit longer today... so take good care of the house while I'm gone!"
    no "Sure thing, Mom!"
    show aab 21
    mc "Seriously, there's no need to..." with dis
    no "Nonsense, please, come in!"
    no "We can study for the quiz after we've dried off and had some coffee and pastries! The mind functions better when the body isn’t hungry!"
    mc "Um... Okay, okay, if you insist..."
    no "I do!"
    stop music fadeout 5
    play sound2 keys
    play music2b rain3 fadein 4
    scene aab 26 with Dissolve(3)
    play sound doorclose
    mc "Ahh... Well it is nice to finally get out of that rain." with dissolve
    show aab 22
    mc "Sorry to put you on the spot back there, Nova." with dis
    mc "Your mom started asking questions and I got nervous."
    mc "*Laughs* I’m sure you’ve already guessed I’m not here to study for a quiz."
    show aab 23
    no "*Laughs* Yeah, I figured. You look a little young to be my college classmate..." with dissolve
    no "*Giggles* I’m surprised my mom didn’t notice."
    show aab 24
    mc "Heh, sorry about that." with dissolve
    mc "(So she attends Kredon's college... Maybe she knows Penelope?)"
    mc "(Well, it doesn't really matter.)"
    mc "Alright then, I'll get straight to the point. It turns out that..."
    show aab 23
    no "No, no! Please, take a seat on the couch! You’ll be much more comfortable."with dissolve
    show aab 24
    mc "Don't worry, there's no need. I only need a couple minutes of your time."with dissolve
    mc "Someone told me that you..."
    show aab 23
    no "Seriously! Take a seat! And I’ll get you some coffee. What kind of hostess would I be if I didn’t at least offer you something to drink?"with dissolve
    show aab 24
    mc "But..."with dissolve
    show aab 25
    no "I won’t take no for an answer!"with dis
    no "Just give me a minute! I need to change out of these wet clothes and then I’ll join you in the living room."
    mc "Um... Well, okay."
    no "No need to be shy! Get comfy!"
    scene aab 26 with Dissolve(1.7)
    mc "(Wow, it's been a while since I’ve seen such hospitality.)" with dissolve
    mc "(Nova seems very nice. And damn, she's definitely cute, not gonna lie...)"
    show aab 27
    mc "(This apartment is a little small, but I will say it’s decorated very tastefully. Makes it feel pretty cozy.)" with dis
    mc "(Hmm... There are a lot of books here. I wonder if...)"
    no "Sugar—one teaspoon, or two?"
    mc "Two! Thank you so—"
    play sound stairsrun
    play sound3 panhit
    scene aab 28 with hpunch
    pause 1
    play sound chair1
    play sound2 punch
    show aab 29
    no "DON'T YOU DARE MOVE A MUSCLE!" with hpunch
    play music2 punk1
    mc "W-WHAT THE FUCK!!!" with hpunch
    no "You thought you were sooooo sly, huh?!"
    mc "W-What?"
    no "You thought you could come here and threaten my family just like that?"
    mc "WHAT?!"
    show aab 30
    mc "What the fuck are you talking about?!" with dis
    no "Don't play dumb, Mr. \"[mc]\"."
    no "Given the choice, you could have at least chosen a better fake identity. [mc]?! What kind of stupid name is that?!"
    scene aab 32
    mc "H-Hey! T-That's my real name! And w-what the hell is going on?!"
    scene aab 31
    no "Assumed if I saw that you knew my family’s whereabouts, I'd chicken out right?!"
    no "Well, joke's on you. I'll kill you and then I'll flee the country with them!"
    scene aab 32
    mc "What?! You must be confusing me with someone else!"
    mc "Put the knife down, please!"
    scene aab 31
    no "We can do this the easy way or the hard way."
    no "The easy way... you let me tie you up and then you tell me who you work for. Or the hard way... I just kill you instead. Both ways are actually pretty easy to me."
    scene aab 32
    mc "Who I work for?!"
    scene aab 31
    no "It’s Ulysses, isn't it? I knew it. Those bastards..."
    scene aab 32
    mc "But I don't work for anyone!"
    scene aab 31
    no "A mercenary, then? Bounty hunter, perhaps? How did you find me!!"
    no "I had nothing to do with the South Korea DDoS attack!"
    scene aab 32
    mc "I have no idea what you're talking about!"
    scene aab 31
    no "How did you find where I live?!"
    scene aab 32
    mc "L-Luna! Luna told me!"
    scene aab 31
    no "Luna? Who's Luna? I don't know any Luna."
    scene aab 32
    mc "You have to! She told me your address!"
    mc "Black hair, red eyes, pale skin... S-She likes... murder stories and stuff!"
    mc "Oh my god..."
    mc "IS THAT HOW YOU KNOW EACH OTHER?! DO YOU TWO MURDER PEOPLE TOGETHER?!!" with hpunch
    mc "DID I GET LURED INTO BEING YOUR LATEST VICTIM??!!" with hpunch
    show aab 33
    no "Oh... Luna, the girl from Loco's Cafe?" with dissolve
    mc "YES!!"
    show aab 34
    mc "She told me you owed her a favor and you could help me investigate something!" with dissolve
    no "Hmmm..."
    show aab 36
    no "I indeed owe her one..."with dis
    no "And she's the only person who knows what I do... and also my true identity..."
    no "How do you know Luna?"
    scene aab 35
    mc "We go to school together!"
    no "Hmm..."
    show aab 36
    no "Your story seems plausible..."
    no "Unless this is a carefully crafted plan to gain my trust and then attack me from behind..."
    show aab 35
    mc "Do I look like a carefully-crafting assassin to you?!"
    mc "I don't even know who you are!"
    no ". . ."
    stop music2 fadeout 7
    show aab 37 with Dissolve(2)
    pause
    show aab 38
    no "Alright, you don't seem like you're lying!" with dissolve
    no "Sorry for all the commotion, I just had to make sure!"
    mc "(Oh my god, I thought she was gonna slit my throat...)"
    mc "(This girl is fucking nuts...)"
    mc "(I don’t care how cute I thought she was, I’m not trying to stick my dick in crazy!)"
    play sound chair1
    show aab 39 with dis
    mc "Okay, are you gonna explain to me what the fuck just happened?!" with dissolve
    show aab 40
    no "Hey, better safe than sorry, as they say. I can’t take any chances."with dissolve
    no "I didn't know who you were, and then I found you talking with my mom, asking about me, making up a story about studying for a quiz..."
    no "I'm sure you can understand how it looked a little suspicious."
    show aab 39
    mc "Yeah, true. Maybe threatening me with a knife to my throat was just a tad excessive, though..."with dissolve
    show aab 40
    no "*Giggles* Yeah, alright, I’ll give you that."with dissolve
    no "Sorry about it. Sometimes I can get a little paranoid."
    show aab 39
    mc "Well, I must say, we both have that in common. Someone just told me I was paranoid earlier today at school."with dissolve
    mc "You wouldn't believe what Mr. Keating told us during class. Do you remember him at all?"
    show aab 41
    no "I've never met a \"Mr. Keating\". I’m guessing you probably attend Kredon's Private High School."with dissolve
    mc "Oh... yeah, you're right. I forgot there are other schools in Kredon too."
    no "Yes, rich boys like yourself never pay much attention to the fact that not everyone has a yacht and 3 Mercedes."
    show aab 39
    mc "*Laughs* I wouldn't exactly say I'm rich. Really, if it weren't for the student exchange program and its scholarship offering, I wouldn't have been able to come here."with dissolve
    show aab 40
    no "Oh well, I take back what I said, then."with dissolve
    no "I know not everyone who attends that school is a rich moron, but there definitely are a good amount."
    show aab 39
    mc "Oh believe me, I’ve seen that firsthand..."with dissolve
    show aab 40
    no "Anyway, back to the matter at hand... how can I help you?"with dissolve
    show aab 39
    mc "Ah, yes. The thing is..." with dissolve
    mc "There's something I wanted to investigate, and Luna mentioned you could help me with that."
    play sound type1
    show aab 42
    no "I see. That shouldn't be a problem. There's nothing in this world that my best friend and I can't investigate." with dis
    no "You've come to the right place!"
    no "But after we’re done here, you'll have to tell Luna we're even!"
    mc "Best friend huh? Are you and Luna the dynamic-detective-duo?"
    no "*Giggles* I'm talking about my trusty keyboarded friend here."
    mc "Your laptop?"
    mc "Does that mean that..."
    mc "Don't tell me you're a hacker!"
    show aab 43
    no "*Laughs* Ah, there it is."with dis
    no "Another naive consumer misled by Hollywood productions and fantasies of the Internet."
    play soundlow thunder
    no "{i}\"Could you hack the NSA, Nova?\""
    no "{i}\"Why don’t you just steal us some money from Ulysses, Nova?\""
    no "{i}\"Please erase all of my student loan debt Nova!!\""
    show aab 44
    mc "Could you do those things?" with dissolve
    show aab 45
    no "Um... W-Well, I don't know. P-Probably not." with dis
    mc "Aww... that's too bad."
    show aab 43
    no "But I can decrypt and access all sorts of databases and modify their contents without leaving behind a single trace—anything from classified documents to alterations in games like Eternum." with dissolve
    show aab 44
    mc "That's awesome!" with dissolve
    play soundlow chair1
    show aab 47
    no "Well, if you really want me to help you, you'll have to tell me all the details." with dis
    show aab 46
    mc "Of course. In fact, I'm glad you mentioned Eternum. It's related to that." with dissolve
    show aab 47
    no "If you're wondering whether I can find out where the Gems of Doom or the Weapons of Atlas are located, I'm sorry to tell you that I can't." with dissolve
    no "Believe me, they would’ve been in my possession a long time ago if that were possible."
    show aab 46
    mc "No, no, it's nothing like that." with dissolve
    mc "The thing is..."
    mc "Long story short—I saw someone being excommunicated by the Praetorians yesterday, and then shortly after that... he was found dead. They said he had a stroke or something."
    mc "I’m... not quite convinced this is all a mere coincidence."
    no "Hmm..."
    show aab 47
    no "Maybe it's not a coincidence, but why do you think this is worth investigating?" with dissolve
    no "Perhaps the guy panicked when he found out he was banned and had a meltdown over that. Even healthy people can suffer a stroke."
    show aab 46
    mc "I know, but... my gut is telling me that’s not the case." with dissolve
    show aab 48
    no "You know, between you and me, I also believe Ulysses may be up to no good." with dis
    no "If you’re skilled enough to avoid getting caught, it's totally possible to modify some in-game features to tamper with the neural implant."
    play soundlow thunder
    no "But when I tried to access the company's classified directories, where all the juicy files would be, I was unable to break their encryption."
    no "They have one of the most sophisticated Cybernetic Defense Systems I've ever seen. Though I could probably get in if I tried harder..."
    no "You know the... \"Founder\" that everyone talks about? There's no information about him anywhere. There aren’t any records... not even a single sighting of him... Nothing."
    show aab 47
    no "Anyway, as for what you want me to look into... It shouldn't be a problem." with dis
    no "I'll go through the local police records about the case. What's the guy's name?"
    show aab 46
    mc "Benjamin Dawson." with dissolve
    show aab 47
    no "Alright. Give me a couple of days. If there's something they're hiding about his death, or I notice any discrepancies about his autopsy... I'll find out." with dissolve
    show aab 46
    mc "Awesome! You're amazing!" with dissolve
    mc "Should we exchange numbers so we can keep in touch?"
    show aab 47
    no "Sorry, I don't have a phone." with dissolve
    show aab 46
    mc "Really? Why?"with dissolve
    show aab 47
    no "Phones can be hacked. All your photos and private conversations could be leaked in less than a minute, if an expert hacker wanted to do so."with dissolve
    show aab 46
    mc "Damn, no phone. That's... unusual."with dissolve
    play soundlow chair1
    show aab 49
    no "Yeah, well, I'm not your \"usual\" type of girl... I'm sorry to disappoint you." with dis
    no "The entire hacker lifestyle is dependent on anonymity."
    no "So if you're expecting me to be the typical girly-girl who wants to go for ice cream and gush all about the latest reality TV shows, you can forget it."
    no "I don't have time for any of those things."
    show aab 50
    mc "Why do you have an anime wallpaper, then?" with dissolve
    mc "Ah, is that Jujutsu Kaisen?"
    play soundlow slam
    show aab 51
    no "W-What? I mean, yeah... I might watch a couple of shows from time to time... I’m not a cavewoman or something!" with hpunch
    no " But... I don't have time for..."
    show aab 52
    no "Stop looking at my stuff!" with dissolve
    menu:
        with dis
        "That character has his eyes covered too. Is that why you like it?":
            no "What? Of course not. It's not about that at all." with dis
            no "I cover my eye because I have a condition..."
        "It's cool, I love anime too [pink][mt](Nova +1)":
            no "It’s just a dumb thi—" with dis
            $ nova_points += 1
            play sound "beat.ogg"
            show heartr at topleft with dissolve
            hide heartr
            show aab 53
            no "Huh? You... you like it too?" with dis
            mc "Hell yeah! I love it."
            mc "I have a huge collection of anime, series, movies... I’m a huge fan!"
            mc "Do you play Eternum too?"
            no "Y-Yeah."
            mc "Maybe we could play together sometime. I know you don't have a phone, but I could stop by again soon."
            no "Like... to team up on a server?"
            mc "Yeah!"
            no "I guess it could be... interesting."
            show aab 52
            no "B-But well, maybe another day." with dissolve
        "Hey, what's that tattoo?":
            no "It's a cyber-owl." with dis
            mc "*Laughs* A what?"
            no "It's a symbol!"
            no "You wouldn't get it..."
    no "*Clears throat* Anyway, you’ve made your request and I’ve told you that I'll do it. Now get out of my house!"
    mc "Copy that! I need to drop by my school again because I forgot my bag, so that's probably a good idea anyways."
    show aab 54b with Dissolve(1.7)
    play soundlow thunder
    mc "Well, it was nice meeting you!" with dissolve
    mc "See you in a couple of days!"
    mc "And if it’s not too much to ask... please don't hack me. Unless it’s to add more commas into my bank account, then by all means... fire away!"
    show aab 54
    no "Hah! I won't hack you, don't worry."
    show aab 54b
    mc "You sure? Promise me!"
    show aab 54
    no "Yessss, I promise."
    no "I only hack people who I think are interesting."
    no "You're safe."
    show aab 54b
    mc "*Laughs* For once, I'm happy to be boring!"
    mc "Alright then, take care, Nova!"
    mc "Bye!"
    scene aab 55 with Dissolve(1.2)
    play sound doorclose2
    pause
    play music2 type2 fadein 1
    scene aab 56 with Dissolve(2.3)
    no "(That password was way too easy to crack.)" with dis
    no "(He doesn't even have two-factor authentication enabled.)"
    no "(Such a newbie, [mc].)"
    show aab 57
    no "(And... done! We're inside his phone.)" with Dissolve(1.3)
    no "(Let's see...)"
    show aab 58
    no "(Hmm... Nothing suspicious. He seems to be clean.)" with dissolve
    show aab 57
    no "(Good.)" with dissolve
    no "(He doesn't seem to be a bad guy, but I can’t afford to take any chances.)"
    show aab 58
    no "(Hmm... He doesn't have an Instagram account. Or a Facebook. That’s pretty rare nowadays.)" with dissolve
    no "(Guess we're alike in that way.)"
    no "(He does use YouTube a lot, though. And he has a couple of interesting APKs installed.)"
    show aab 57
    no "(Oh, according to these GPS records, it looks like he arrived in the USA about a week ago.)" with dissolve
    no "(He got a scholarship to study in Kredon. He wasn’t lying after all...)"
    show aab 58
    no "(Mmm... His photo gallery doesn’t have many photos...)" with dissolve
    no "(Let’s see here... that must be his house in Kredon, then he’s kept a few screenshots from a game...)"
    show aab 59
    no "(Oh my god, he's almost naked in this one.)" with dissolve
    no "(He's... a lot more ripped than I thought.)"
    show aab 60
    no "(Maybe I should stop snooping...)" with dissolve
    no "(I guess I've seen enough to make sure he's not hiding anything...)"
    no "( . . . )"
    show aab 59
    no "(Eh, what the hell! A little more snooping won’t hurt.)" with dissolve
    no "(It’s only to... make sure he's not a spy, of course...)"
    show aab 58
    no "(Seems to have a bunch of pictures with this short-haired girl...)" with dissolve
    no "(Maybe his girlfriend...?)"
    show aab 60
    no "(Not that I care, of course...)" with dissolve
    show aab 58
    no "(Although he has even more photos with this Asian dude. A lot more. Maybe he’s gay? They could be lovers...)" with dissolve
    no "(Nah, I think they're all just close friends.)"
    show aab 60
    no "(Well, I guess this is enough.)" with dissolve
    no "(I should start making dinner before Dad gets home.)"
    show aab 59
    no "(But maybe I'll just take one last peek again at that photo of him in his boxers to...)" with dissolve
    no "(Uhh... make sure it’s not Photoshopped or anything... gonna have to inspect it reeeeeally closely...)"
    stop music2 fadeout 3
label lunaserver:
    scene aac 1 with Dissolve(3)
    play sound doorbell
    pause .6
    l "Coming!" with dis
    play sound dooropen1
    scene aac 2 with Dissolve(1.3)
    play sound2 doorclose
    pause .4
    mc "Hey Luna!" with dissolve
    mc "Thank you for inviting me!"
    mc "I see you're all geared up and ready to go!"
    scene aac 3
    l "Yep! This is Eternum's E-suit."
    scene aac 2
    mc "I know, they’re awesome! Annie and Dalia have one too."
    mc "It looks so futuristic."
    if anniehorror:
        mc "Speaking of which, is Annie here already?"
        scene aac 3
        l "No, she went to your house so she could use her own equipment. I only have one spare suit and visor."
        l "But she’ll be joining us as soon as we log into Eternum."
        scene aac 2
        mc "Ah, sounds good."
    scene aac 3
    l "Did you speak with Nova?"
    scene aac 2
    mc "Yeah! She said she’s willing to help investigate Benjamin's death."
    mc "I know she probably won’t find anything weird or unusual, but at least I'll get some peace of mind."
    mc "Thank you for lending me a hand, Luna."
    mc "Might I ask why she owed you a favor?"
    scene aac 3
    l "She used to come by our cafe to work on her laptop."
    l "One day she came running in and asked me to quickly dispose of a bunch of flash drives and hard disks."
    l "I threw them away in the kitchen and a minute later, the police arrived and confiscated her laptop."
    scene aac 2
    mc "Hah! Then they couldn’t find anything on it?"
    scene aac 3
    l "Exactly."
    l "That's when she told me she was some kind of hacker or computer wizard. She then gave me her address and told me to stop by if I ever needed anything."
    scene aac 2
    mc "Not everyone would’ve done what you did... risk themselves to help someone they barely knew... that’s very kind of you."
    scene aac 3
    l "I don't know, she... she didn't seem like a bad person."
    l "It just felt like the right thing to do."
    scene aac 2
    mc "You're a genuinely good person, Luna."
    scene aac 3
    l "T-Thank you."
    scene aac 2
    mc "Well, it's getting late... I think it’s about that time!"
    mc "Can't wait to jump back into Eternum!"
    scene aac 3
    l "Please, come in. Make yourself at home."
    l "Do you want anything to drink? Coffee, perhaps?"
    scene aac 2
    mc "(Man, last time I was invited inside and offered coffee, the situation escalated quickly...)"
    mc "*Shudders* N-No, don’t worry about me... I'm good."
    mc "But thank you!"
    scene aac 4 with Dissolve(1.3)
    mc "You have a really beautiful home, Luna!" with dissolve
    mc "Everything looks so spotless!"
    show aac 5
    l "Thank you. I tidied up the mess before you got here." with dis
    l "You can sit on the couch, if you want. I'll bring you the visor in a second."
    mc "Sure!"
    mc "But before I sit down..."
    show aac 6
    mc "Do you mind if I use the bathroom?" with dis
    show aac 7
    l "Um... Y-Yes, but there's something I need to tell you first." with Dissolve(.7)
    l "Can you sit down?"
    show aac 6
    mc "Yeah, but I really have to use the restroom first."with Dissolve(.7)
    mc "I've been holding it ever since I left Nova’s house..."
    show aac 7
    l "Um..." with Dissolve(.7)
    l "O-Okay, you can go to the bathroom. It’s just down the corridor..."
    l "But don't look into the room on the right."
    l "My father's corpse is still there."
    show aac 8
    mc "*Chuckles* Yeah, of course." with Dissolve(.7)
    mc "*Chuckles* Nice try Luna, but I'm already getting used to your twisted little \"jokes\"..."
    scene aac 9 with Dissolve(1.7)
    play music2 risinglong fadein 7
    stop music2b fadeout 10
    pause
    scene aac 10 with Dissolve(1.9)
    pause
    play sound thunder
    stop music3 fadeout 3
    show aac 11
    pause .05
    show aac 10
    pause .05
    show aac 11
    pause .05
    show aac 10
    pause .05
    show aac 11
    pause .05
    show aac 10
    pause .05
    show aac 11
    pause .05
    show aac 10
    pause .05
    show aac 11
    pause .05
    show aac 10 with Dissolve(2.5)
    pause
    show aac 12 with Dissolve(1.6)
    pause
    mc "What the fuck..." with dis
    l "The voices never stopped talking..."
    show aac 13
    mc "*Turning around* W-What?" with dis
    l "I tried to shut them up, but I couldn't."
    l "I found myself drowning in their cries. I tried to resist them... but I failed..."
    l "B-By the time I came to my senses, it was already too late."
    show aac 14
    l "I found myself stabbing him... ripping into his flesh." with dis
    l "One stab, after another, and another..."
    l "The blood was gushing everywhere..."
    l "*Crying* I... I did this, [mc]..."
    l "I'm a m-monster. I am insane."
    show aac 12
    mc "*Hyperventilating* Y-You did t-this...?" with dis
    mc "How... Why..."
    show aac 15
    l "I must be locked up..." with dis
    l "I can’t control the voices... the urges... no..."
    l "You must help me..."
    l "We need... We need to get rid of the body before it’s too late."
    l "We have to cut it into pieces... flush it down..."
    mc "*Hyperventilating* W-What the fuck are you t-talking about Luna..."
    her "It's okay, [mc]."
    show aac 16
    her "This is not the end." with Dissolve(1.4)
    her "Death is not the scariest fate."
    her "The denial of it... could be far worse."
    play sound thunder
    stop music2
    show aac 17
    mc "AAAAAAAAAAAAAAARGH!!!{w=0.25}{nw}" with hpunch
    mc "AAAAAAAAAAAAAAARGH!!!{w=0.25}{nw}" with hpunch
    mc "AAAAAAAAAAAAAAARGH!!!{w=0.25}{nw}" with hpunch
    mc "AAAAAAAAAAAAAAARGH!!!{w=0.25}{nw}" with hpunch
    mc "AAAAAAAAAAAAAAARGH!!!" with hpunch
    play music2 happy6 fadein 5
    show aac 18
    her "HAHAHAHA!" with Dissolve(2.5)
    mc "WHAT THE FUCK WAS THAT?!" with hpunch
    her "*Laughs* Oh god, that was hilarious!"
    show aac 19
    l "I'm sorry, I told my dad you were coming and he insisted on playing a trick on you." with dis
    mc "I... *gulps* I don’t think I have to use the bathroom anymore..."
    her "*Laughs*"
    l "He has a prop knife and a gallon of fake blood, and he loves to use them."
    l "Believe it or not, it's not the first time he's done this to someone."
    mc "Well I guess I see where you get it from, Luna... like father, like daughter..."
    l "Yeah, I couldn't help but play along with him."
    show aac 20
    her "Sorry [mc], don't hold it against me." with dis
    mc "*Laughs* I won't, sir. I have to admit that you did get me pretty good. Once my heart rate goes back to normal and I remove these bricks from my underwear, I'll have to shake your hand for that one..."
    her "Ah, I'm glad to see you've got a good sense of humor!"
    her "You've earned the right to stay at my house!"
    mc "Thanks!"
    show aac 21
    her "Well, I have to go back to the cafe." with dis
    her "I'll be back for dinner. Play nice!"
    l "Sure thing, Dad."
    her "Oh, I should probably change out of these clothes first. A lot of police frequent the cafe and I don’t think they’d enjoy my new attire very much..."
    show aac 20
    her "Now take care, [mc]."with dis
    mc "Goodbye, Mr. Hernandez!"
    mc "Have a good day at work!"
    her "Thank you."
    show aac 22 with Dissolve(1.5)
    play soundlow doorclose2
    l "Well, with that show out of the way... I guess it's time to start playing." with dissolve
    l "Sorry about my dad. He can be pretty wild sometimes..."
    mc "*Laughs* Nah, I think it's cool! I wish my father would’ve done fun things like that when I was living with him."
    mc "But yeah, you're right, let's play!"
    l "Alright, go ahead and use the bathroom... if you still can... and then meet me in the living room."
    mc "*Chuckles* Sounds good to me!"
    show aac 24 with Dissolve (1.7)
    play sound chair1
    show aac 23
    l "Okay, I'll log in first and then send you an invite." with dissolve
    if anniehorror:
        l "Annie should be waiting for us already."
    scene aac 24
    mc "Perfect!"
    mc "Is there anything I need to know before joining this server?"
    scene aac 23
    l "Nothing in particular."
    l "I'll explain everything once we're there."
    scene aac 24
    mc "Alright then, let's not waste any more time!"
    play soundlow login
    show aac 25 with Dissolve(1.4)
    pause .2
    mc "How long should I wait for your invitation?" with dissolve
    l ". . ."
    mc "(Oh, I guess she can't hear me anymore. Pretty crazy how much the game takes over all of your senses.)"
    mc "(I heard the neural implant comes with a safety system that wakes you up if it detects a physical problem, like any sort of bodily harm or trauma.)"
    mc "(It’ll even detect issues with your surrounding environment too, like the fumes of gas or even the presence of smoke.)"
    mc "(I wonder if that system has ever failed...)"
    show aac 26
    mc "(Well, that should be enough time for her to send the invite.)" with dis
    mc "(It's my turn to jump in!)"
    play sound beep
    stop music2 fadeout 4
    bla "You activate the neural implant." with dis
    play sound2 ai7
    blank "{i}Connected." with Dissolve(1.5)
    play sound2 ai8
    blank "{i}Welcome back to Eternum." with dis
    play sound2 ai9
    blank "{i}You've received an invitation from..." with dis
    play sound2 ailuna
    blank "{i}Luna." with dis
    play sound2 ai10
    blank "{i}Would you like to join her session?" with dis
    mc "Let's do it!"
    play sound2 ai11
    blank "{i}Please prepare to connect..." with dis
    stop music2 fadeout 1
    play sound risingshort4
    pause 2
    show login3 with flash
    pause 8
    play soundlow whoosh4
    scene white with dissolve
    scene aac 27 with Dissolve(2)
    pause
    mc "(Okay, I'm...)" with dis
    play music2 luna1
    mc "(I'm standing! I can feel my legs! And I'm not even dizzy!)"
    mc "(Nice! I’m getting used to Eternum after all!)"
    show aac 28 with dis
    mc "(Hmm...)" with dissolve
    mc "(Seems like a nice, family-friendly neighborhood... not ominous looking whatsoever...)"
    mc "*Shivering* (Jeez, it's cold in here.)"
    l "[mc]!"
    $ unlock_look("luna", 2)
    show aac 28b
    mc "Luna!" with dis
    mc "Wow, I love your outfit!"
    mc "It gives me sorceress vibes."
    mc "You look beautiful!"
    show aac 30
    l "Thank you. I won it in a tournament." with dis
    show aac 29
    mc "Really? Another tournament? Man, first you won the neural implant, now a cool outfit..." with dissolve
    mc "*Laughs* Something tells me it's better not to mess with you in Eternum!"
    show aac 30
    l "*Giggles* I'm not that good." with dissolve
    l "Actually, my destruction magic is rather weak."
    l "But I'm not a bad summoner."
    show aac 29
    mc "Summoner?" with dissolve
    show aac 30
    l "I can... invoke different creatures. Animals, soldiers, ghosts..." with dissolve
    l "But I can show you that another day. I doubt we'll have to deal with any kind of combat on this server."
    l "Do you like your outfit, by the way?"
    show aac 29
    mc "My outfit?" with dissolve
    show aac 30b
    mc "Oh, DAMN!" with dis
    mc "I didn’t even notice! Finally, I don't look like a noob! My peasant-looking days are behind me!"
    mc "Is this your doing?"
    show aac 30
    l "Yeah, I sent it along with your invitation. I thought a classic detective outfit suited the server." with dissolve
    show aac 29
    mc "Love it!"with dissolve
    if anniehorror:
        play sound whoosh2
        show aac 29 with flashfast
        pause .3
        a "Ughh, why is it so cold here?! Couldn’t you have picked a server in the tropics or something??" with dis
        $ unlock_look("annie", 3)
        show aac 32
        mc "Annie!" with dis
        a "Hi there!"
        mc "Glad you could make it!"
        a "Of course! I never miss an opportunity to play Eternum!"
        mc "*Laughs* Yeah, I know that firsthand."
        l "Welcome, Annie."
        show aac 33
        a "Thank you so much for inviting me, Luna!" with dis
        l "My pleasure!"
        show aac 34
        mc "I love your outfit, Annie!" with dissolve
        mc "You look beautiful too."
        show aac 35
        a "Oh... B-Beautiful? Well, t-thank you."with dis
        a "I just chose the first thing I saw in my inventory..."
        a "It's nothing special..."
        a "I just thought that since we were going to a server of..."
        a "Of..."
        show aac 36
        a "What exactly is this server about again, Luna? I know you told us earlier..." with dis
        a "It definitely looks very eerie..."
    show aac 37 with Dissolve(1.2)
    l "Well, I welcome you to \"The Red Herring\", a server dedicated to solving mysteries and uncovering the truth behind the horror." with dissolve
    show aac 39
    mc "Truth behind the horror, huh?"with dis
    show aac 37
    l "Yeah. This server consists of 12 different cities and towns, each with multiple districts within. Every district has dozens of cases waiting to be solved."with dis
    show aac 39
    mc "Man, and this is all on one server? Sometimes I forget just how big Eternum is..." with dis
    mc "Is there a case to be solved around this area?"
    show aac 38
    l "Yes. \"The Enigma of the Foggy District\"."
    l "As I mentioned before, this is the case that’s got me stumped. I've tried repeatedly to solve it by myself, just as I did with all the others, but I’m still stuck."
    show aac 39
    mc "Ah, no worries Luna, we'll solve it together!"
    mc "They don't call me [mc] Holmes for nothing!"
    if anniehorror:
        a "*Laughs* No one calls you that!"
    mc "And how should we start? I don't see anyone at all..."
    if anniehorror:
        show aac 41
        a "Actually, now that you mention it, yeah... you're right." with dis
        a "There's not a soul around."
        a "No NPCs... players... nobody. Hmm, well what’s the story behind this place, Luna?"
    show aac 40
    l "There once was a man named Jeremy Flink, a rich and powerful businessman, who opened a cement factory here." with dis
    l "He took advantage of the fact that this was a poor neighborhood and hired hundreds of workers for far less than minimum wage."
    l "All while he lived an extravagant life in the comforts of a modern, luxurious house outside the slums."
    l "After experiencing years of abuse under his watch, the workers got fed up and burned the factory down."
    l "The ashes of that fire blanketed the streets like snow, and ever since that great fire, the sun has not risen once..."
    show aac 39
    mc "Hmmm..." with dis
    mc "The sun has yet to rise, huh... maybe there could be something paranormal going on here too... Is that possible?"
    show aac 38
    l "Some of the mysteries in The Red Herring just involve simple murders or robberies with perfectly reasonable explanations, but there are others that do dive into the paranormal realm, yes."
    if anniehorror:
        show aac 39
        a "Oh god, I don't like the sound of that..."
    show aac 40
    l "With the factory destroyed, most people ended up leaving the neighborhood, and now there's only a handful left."with dis
    l "That makes investigation of this case slow and very difficult. All the other players who have tried to solve it before have given up already, so we probably won't see anyone else."
    show aac 38
    l "On the other hand, the more difficult the case, the better the bounty." with dis
    l "If we managed somehow to unravel this mystery, the reward will definitely be worth it."
    show aac 39
    mc "Interesting..."
    show aac 40
    l "So... yeah, I think our best bet would be trying to find some villagers. I've already spoken with most of them numerous times, but maybe you'll have better luck at catching something I haven’t." with dis
    if anniehorror:
        show aac 42
        a "Hmm... I wonder what’s causing the fog and the endless night." with dis
        a "Could it be a curse?"
        a "Maybe we have to find its source?"
    show aac 44
    l "I've already been to the old factory grounds, but there's nothing but a mountain of ash and iron debris now." with dis
    show aac 45
    mc "(Luna's not wearing her gloves...)"with dis
    mc "(No burns, scars, birthmarks, tentacle hands, or penis fingers...)"
    mc "(Why does she always wear gloves, then?)"
    mc "(If it’s because she likes the look of gloves, why wouldn't she wear them inside Eternum too?)"
    mc "(Should I ask again?)"
    mc "(No, it's probably not the right time for that...)"
    show aac 44 with dis08
    pause
    show aac 46 with Dissolve(.4)
    pause
    show aac 47
    mc "(Man, that dress fits her body perfectly...)"
    mc "(And it complements her breasts so much.)"
    mc "(They seem to be way bigger than I thought...)"
    mc "(She's very pretty and has a great body. Maybe if her personality was a little different, she'd be super popular at school.)"
    mc "(I hope she doesn't change one bit, though. I love how she is. If she was any different... she wouldn’t be, well, Luna.)"
    show aac 46 with dis08
    pause
    show aac 48 with Dissolve(.4)
    pause
    show aac 49
    pause
    show aac 48
    show aac 50 with dissolve
    pause .5
    show aac 51
    mc "*Clears throat* Um... W-We should..." with dis
    mc "Oh, look! There's a man over there!"
    mc "(God, that was embarrassing. Did she catch me staring at her tits?)"
    mc "L-Let's go talk to him!"
    show aac 52 with Dissolve(1.5)
    if anniehorror:
        a "Oh, you're right! Someone’s sitting on the ground!" with dissolve
        l "That's Enzo!"
    else:
        l "That's Enzo!" with dissolve
    mc "Do you know him?"
    l "Yes, he used to be a factory worker, but was one of the few that stayed behind when everyone left."
    l "He's got... nowhere to go."
    if anniehorror:
        a "Aww... that's so sad... Poor man."
    else:
        mc "Poor guy."
    show aac 53 with Dissolve(1.5)
    mc "Hello... Enzo?"with dis
    enz ". . ."
    enz "What do you want?"
    mc "I'm [mc]. Can we talk for a bit?"
    enz "No. Go away."
    mc "Okay..."
    show aac 54 with dis
    l "*Sitting on the floor* Hello Enzo." with dissolve
    show aac 55
    enz ". . ."
    enz "Miss Hernandez?"
    show aac 54
    l "Yours truly! And I told you to call me Luna, Enzo."
    l "How have you been?"
    show aac 55
    enz "Same as always. Staying out in the cold and always getting sick."
    show aac 57
    mc "He remembers you..." with dis
    show aac 56
    l "*Whispering* Of course. The memory of NPCs is never reset. Sometimes it becomes impossible to distinguish them from a real player roleplaying."with dissolve
    l "*Whispering* The Founder is a genius."
    if anniehorror:
        show aac 58
        a "Is there anything we can do to help you, Enzo?"with dis
        enz "You can't do anything. Everything is already lost."
    show aac 55
    enz "It all went to shit when they burned that damn factory down."with dis
    enz "I told them not to do it, but they didn't listen..."
    show aac 54
    l "Do you know why the sun never rises here?"
    l "What could be causing it?"
    show aac 55
    enz "I don't know... Everyone in this district either died or abandoned the city."
    enz "Only I remain, left alone to live amongst the rats and cockroaches..."
    show aac 57
    mc "Did they kill the factory owner? Mr. Flink?" with dis
    mc "Maybe he's the one who’s left a curse on this place."
    show aac 56
    l "As far as I know, no." with dissolve
    l "He was on a business trip outside the city when everything happened… and to top it all off, his insurance covered everything. He didn’t bat an eye at the destruction that took place here."
    if anniehorror:
        show aac 58
        a "Do you know of anyone who would curse this place, Enzo?" with dis
        enz "We did something terrible... We deserve it..."
        a "What did you do?"
    show aac 55
    enz "We did something terrible... We deserve it..." with dis
    show aac 54
    l "It's not your fault, Enzo. Mr. Flink was an exploitative, evil man."
    show aac 55
    enz "We did something terrible... We deserve it..."
    show aac 59
    l "*Standing up* And that's it." with dis
    l "Once he starts saying that, he enters a never-ending dialogue loop."
    show aac 60
    mc "Hmmm... Well, that didn’t help us much." with dissolve
    mc "We don't know what's causing the curse, if there is one, and have no idea how we could even lift it."
    show aac 59
    l "Yes, I know. It's frustrating." with dissolve
    l "This is why everyone stopped trying to solve this case."
    l "There are a couple more villagers, but they all end up repeating the same thing."
    l "{i}\"We did something terrible. We deserve it.\""
    show aac 60
    mc "Hmm..." with dissolve
    mc "Do you know where they are? Maybe if we..."
    stop music2 fadeout 6
    mw "It's almost midnight."
    show aac 61
    mc "Huh?" with dis
    mc "Who's that woman?"
    play music2b syndicate2 fadein 6
    l "I... I don't know. I've never seen her before..."
    if anniehorror:
        a "Why does she look so scary..."
    mc "Excuse me? Ma'am? Did you say... midnight?"
    mc "How can you tell what time it is? It's always night here."
    show aac 63
    mw "The child will wake up at midnight. You have to help her." with dis
    show aac 62
    mc "The child?"
    show aac 63
    mw "That little girl is the key to lifting this curse."
    mw "Help her, and you'll remove the curse that consumes this place."
    show aac 62
    mc "Where's the girl?"
    show aac 64
    mw "On the highest floor of the Bixen Building."with dis
    mw "In the only room with light."
    mc "Yes... I see it."
    mw "If you delay too long, the light will fade away, and with it, the hope of ever lifting this curse..."
    show aac 62
    mc "Who are you? Why are you helping us?" with dis
    show aac 63
    mw "I'm just a member of the Syndicate like any other."
    show aac 62
    mc "The Syndicate?"
    mc "From the factory that burned down?"
    mw ". . ."
    show aac 63
    mw "Good luck, [mc]."
    show aac 65 with Dissolve(1.7)
    pause
    mc "Well that was strange..." with dissolve
    if anniehorror:
        a "W-Was she an NPC?"
        mc "I guess..."
    else:
        l "I'd never seen that NPC. Well, I guess she wasn't a player."
        mc "I guess not..."
    mc "Well, in any case, we got lucky. We have a new clue."
    mc "Let’s head over to that... Bixen Building..."
    play sound doorold
    stop music2b fadeout 3
    play music fireplace fadein 4
    scene aac 66 with Dissolve(2.5)
    pause .5
    mc "Hm, the main door was left open..." with dis
    l "Weird, I thought I had already explored this building during my previous visits to the Foggy District."
    mc "Well, let's take a look anyway."
    if anniehorror:
        show aac 67
        a "Aaahh that’s more like it... It's so warm and cozy in here..." with Dissolve(1.5)
        l "Yeah, you're right, it feels so good."
        a "This fireplace is like heaven. My hands were freezing out there!"
        a "Is this server always so cold and damp?"
        l "Not at all! I once solved a case in an iron foundry, where the heat was so bad I had to strip down to my underwear."
        mc "(Oh come on now!! Why couldn’t we solve a mystery over there?!)"
        show aac 68
        l "You know, I've definitely been here before. I'm sure of it." with dis
        l "But last time the building was empty, the lights were out, and the fire wasn't lit..."
        mc "Hmm..."
        mc "Maybe they only switch the lights on at a certain time of the day?"
        l "Hmm... Could be."
    else:
        show aac 67b
        l "It's so warm and cozy in here..." with Dissolve(1.5)
        mc "Yeah, you're right, it feels so good."
        mc "It’s freezing out there!"
        mc "Is this server always so cold and damp?"
        l "Not at all! I once solved a case in an iron foundry, where the heat was so bad I had to strip down to my underwear."
        mc "(Oh now come on!! Why couldn’t we solve a mystery over there?!)"
        l "You know, I've definitely been here before. I'm sure of it."
        mc "Really?"
        l "Yeah, but last time the building was empty, the lights were out, and the fire wasn't lit..."
        mc "Hmm..."
        mc "Maybe they only switch the lights on at a certain time of the day?"
        l "Hmm... Could be."
    show aac 69
    mc "Wait a second... Do you hear that?" with dis
    l "What?"
    play soundlow noise2
    mc ". . ."
    mc "That noise... It's coming from upstairs..."
    mc "There's someone here."
    l "Perhaps it’s the child that woman mentioned?"
    mc "Probably, but I get the feeling that we're not just gonna find a normal kid who wants to see if you have any games on your phone..."
    if anniehorror:
        show aac 70
        a "W-What do you mean by that?"
        mc "I have no idea what to expect, so get ready for anything."
        mc "Maybe we’ll find a deformed kid, or perhaps the kid's already dead and we're hearing the murderer chopping their body into pieces."
        a "W-What?!"
        a "Y-You're scaring me, [mc]."
        show aac 71
    else:
        show aac 71b
    mc "Well, in any case, we have to get up there." with Dissolve(1.5)
    mc "We can’t give up... we have to solve this case!"
    l "Yes!"
    if anniehorror:
        a "Y-You guys go first... I’ll be right behind you..."
    play sound stairswood
    scene aac 72 with Dissolve(2.1)
    l "I think that's the window we saw from the street." with dissolve
    mc "Yes, I think so."
    mc "Let's take a look."
    show aac 73 with Dissolve(1.5)
    stop music fadeout 1
    play sound switch
    pause .4
    mc "Oh shit, the lights went out..."with dis
    l "The only light left is coming from that candle..."
    show aac 74 with Dissolve(1.4)
    play music2 syndicate fadein 3
    pause
    mc "*Whispering* Oh man, you have got to be kidding me..." with dis
    if anniehorror:
        a "*Whispering* Oh m-my g-god..."
    l "*Whispering* There's that little girl... The woman was telling the truth..."
    l "*Whispering* We have to talk to her."
    mc "*Whispering* A-Are you sure about that?"
    l "*Whispering* She must be the key to lift the curse and solve this mystery. There’s no way this is just a coincidence."
    play soundlow stairswood
    show aac 75 with Dissolve(1.2)
    mc "Um... Hello? Dear?" with dis
    kid ". . ."
    mc "*Whispering* Holy fuck, this is so creepy..."
    mc "*Whispering* Why isn't she answering?"
    l "*Whispering* Maybe she's scared."
    if anniehorror:
        a "*Whispering* C-Can’t be m-more scared than I am r-right n-now..."
        show aac 76
    else:
        show aac 76b
    mc "Hello? Are you lost?" with dis
    mc "We can help you."
    mc "We won't harm you..."
    if anniehorror:
        show aac 76c
    else:
        show aac 75
    l "*Whispering* Why are you talking with that voice?" with dis
    mc "*Whispering* W-What voice?"
    if anniehorror:
        a "*Whispering* Yeah, you sound like someone trying to lure a kid into your windowless van..."
    mc "*Whispering* T-This is my normal voice! A perfectly pleasant, normal voice! How else am I supposed to sound?!"
    show aac 75
    kid "Who are you?"
    mc "*Whispering* Oh, shit, she answered!"
    if anniehorror:
        a "*Whispering* Say something!"
        mc "*Whispering* But what?!"
    l "Can we come and sit next to you?"
    kid ". . ."
    kid "Yes."
    play soundlow chair2
    show aac 78
    l "Thank you." with dis
    l "I'm Luna. It’s really nice to meet you. What’s your name...?"
    show aac 77
    kid ". . ."
    kid "Where are Mommy and Daddy?"
    show aac 78
    l "If you tell us your name, we can help you find them."
    show aac 77
    kid ". . ."
    kida "I'm Annie."
    if anniehorror:
        show aac 81
        a "Oh come on, you have got to be kidding me..."
    else:
        mc "(Thank god my Annie didn't come, this would have freaked her out.)"
    show aac 78
    l "Nice to meet you, Annie. That's a beautiful name."
    show aac 77
    kida "Mommy calls me Anne, though."
    show aac 78
    l "We can call you whatever you want! Anne is a beautiful name too!"
    show aac 77
    kida "I want my toys. I have nothing to play with here."
    kida "Daddy said he'd bring me my toys."
    if anniehorror:
        show aac 81
        a "W-What do you wanna play with?"
    show aac 77
    kida "I want Mr. Nebula."
    show aac 78
    l "Mr. Nebula?"
    show aac 77
    kida "My favorite teddy bear. I left him at our house. Now I have nothing to play with here."
    show aac 78
    l "We can go get him, if you want. Where's your house?"
    show aac 77
    kida ". . ."
    show aac 78
    l "How about we go on an adventure together? An adventure to get you a new toy! Is that all right?"
    show aac 77
    kida ". . ."
    kida "Okay."
    kida "But please don’t leave me."
    show aac 78
    l "Don't worry, we won't. [mc] will go get you a new toy!"
    if anniehorror:
        l "Annie and I will stay here with you."
        l "Did you know she has the same name as you?"
        l "Only pretty girls can be named Annie!"
        show aac 81
        a "Y-Yeah, we'll stay here and play with you... A-Annie."
    else:
        l "I'll stay here with you."
    show aac 77
    kida ". . ."
    kida "Okay."
    show aac 80
    mc "A new toy? Where could I find one?" with dissolve
    show aac 79
    l "There's a man who sells all kinds of stuff in this district. He's not always around, but maybe we'll get lucky."
    l "He seems to frequent the area that’s about two blocks down, past the old schoolhouse."
    l "If he's not there, come back and we'll think of something else."
    show aac 80
    mc "Alright, count on me! I'm your man."
    show aac 77
    mc "I'll go get you the best toy you've ever had, Anne! Just wait for me here." with dissolve
    kida ". . ."
    play sound stairswood
    show aac 82 with Dissolve(1.6)
    if not anniehorror:
        mc "(I need to hurry. This whole situation is creepy as fuck... I don't wanna leave Luna here alone for too long.)" with dissolve
    else:
        mc "(I need to hurry. This whole situation is creepy as fuck... I don't wanna leave the girls here alone for too long.)" with dissolve
    stop music2 fadeout 10
    play music3 wind fadein 11
    show aac 83 with Dissolve(2.3)
    mc "(Hmm...)" with dissolve
    mc "(That looks like a trading post. It must be the merchant Luna mentioned.)"
    mc "(Lucky us!)"
    show aac 84 with Dissolve(1.2)
    mc "(Hmmm... doesn’t look like there’s going to be much of a toy selection for the girl, though.)"with dissolve
    play sound horse
    mc "(Let’s see... cabbages, some live animals, a camera, and... is that an assault rifle?)"
    mc "(What a bunch of random junk.)"
    mc "*Laughs* (Kind of reminds me of...)"
    play music2 luna1 fadein 3
    stop music3 fadeout 8
    show aac 85
    chop "OOOOHHHHHHHHHHH!" with dis
    mc "This has got to be a joke..."
    chop "WELL HELLO, FRIEND!"
    chop "WELCOME BACK TO CHOP-CHOP’S!!!"
    chop "Best shop in ALLLLL RED HERRING!"
    chop "No, no, IN ALL ETERNUM!"
    show aac 87
    mc "Chop-Chop?! What the hell are you doing here?!" with Dissolve(1.2)
    show aac 88
    chop "Why, selling goods... make big MONEY of course!"
    chop "CHA-CHING, KACHOWWWW!!!!" with hpunch
    chop "You know already! Only best materials! Best products!"
    show aac 87
    mc "But didn't you have a shop in Ion?"
    show aac 88
    chop "Ion no give enough moolah! Too many peasant-dressed players, too many tiny wallets!!"
    chop "I need work in more places, have to pay for son's college! He's gonna become a great businessman like his father and make me rich! I mean, make me proud!! HOOHYEAHHH?!"
    chop "If there's a corner in Eternum without a shop, Chop-Chop will be there!"
    chop "Monies, monies! Pretty pennies!"
    show aac 87
    mc "*Laughs* I pity your son."
    mc "Well, as much as I’d love to contribute to your son’s college fund, I don't think you can help me this time."
    mc "I was looking for children's toys and it doesn’t seem like your selection meets the criteria..."
    show aac 88
    chop "OOOOH! YOU LUCKY LUCKY BOY!"
    chop "CHOP-CHOP got best toys in ALL Eternum!"
    chop "I show top 4 items! You choose! BEST SELECTION!"
    show aac 87
    mc "Oh god, not this again..."
    mc "Um... alright fine, only because you seem to be my only hope out here. Show me what you have."
    show aac 89
    chop "First: Pickaxe of Destiny!" with dis
    show aac 90
    mc "WHAT?! NO!" with hpunch
    if chopchop == 0:
        mc "You already scammed me with that rusty shovel the first time!"
    else:
        mc "You already tried to scam me with that rusty shovel the first time!"
    mc "No more useless tools \"of Destiny\"! And a pickaxe is not something for a child to play with!"
    show aac 87
    mc "*Sighs* I was looking for a teddy bear or something like that." with dis
    mc "If you don't have any, I'll just get going."
    show aac 88
    chop "Ahhhh! Should have said sooner! I have teddy bears!"
    show aac 87
    mc "Really?"
    show aac 88
    chop "Yes, yes, most cuddly bears in all Eternum! MUCH FLUFFY!!!"
    play soundlow noise1
    show aac 91
    chop "Give me second! They round here somewhere..." with dis
    play soundlow noise1
    chop "Ah! Here they are!"
    play sound tear1
    chop "Just little longer..."
    play sound2 tear2
    chop "I'm choosing best bear!"
    play soundlow noise1
    mc ". . ."
    play sound3 tear1
    chop "Ah, yes!"
    play sound4 tear2
    chop "This one PERFECT!"
    show aac 92
    chop "Here you go, friend!" with dis
    chop "Best toy in ALL Eternum!"
    show aac 93 with dis
    mc "Um..." with dissolve
    mc "Did you just make this now with an old cushion?"
    chop "You see cushion? Kid see new best friend!!"
    mc "It smells kinda weird..."
    chop "That the smell of love and invaluable companionship!"
    mc "(Well, to be honest, it doesn't look that bad for something that was made in 30 seconds.)"
    mc "(I hope it's good enough.)"
    mc "Alright, I'll take it. How much is it?"
    mc "Don't try to con me!"
    show aac 88
    chop "Oh come now?? Can’t ever put price on childhood friendship!!" with Dissolve(.75)
    chop "...But in this case, I will."
    chop "Only 30 eternals! Good friend discount, just for you!!"
    show aac 87
    mc "(I expected worse, to be honest.)"
    mc "Okay, deal."
    show aac 88
    chop "Excellent, excellent! You won’t regret! You just solidified child’s value of loving relationships for rest of their lives! How sweet... AH AH D’AWWWWWW!!!"
    show screen eternals with dis
    play sound coins
    $ money -= 10
    pause .05
    $ money -= 10
    pause .05
    $ money -= 10
    pause .05
    chop "You won't regret it!" with dissolve
    hide screen eternals
    chop "Anything else you need?" with dissolve
    show aac 87
    mc "No, that was all, thank you."
    show aac 88
    chop "New shoes? Ring for ding-dong? Gift for lady? Tasty snack for tummy-tums?"
    show aac 87
    mc "(Hmmm... Actually...)"
    mc "(I got the neural implant thanks to Luna, I think it’d be a nice gesture to get her something as a thank you.)"
    if chopchop == 3:
        mc "(Annie loved the pendant I bought her at Chop-Chop's... maybe he has something similar.)"
    mc "You said you have something for a lady?"
    show aac 88
    chop "Of course! What does she like? How is she?"
    show aac 87
    mc "Um... Well, her name is Luna, she has red eyes and black hair. She's a summoner, I think, and..."
    show aac 88
    chop "AHHH! SHUSH SHUSH! SAY NO MORE!"
    chop "I HAVE PERFECT GIFT!"
    show aac 87
    mc "But I just said that..."
    show aac 88
    chop "Come with me!"
    show aac 94 with dis15
    chop "This Maurice."with dissolve
    show aac 95 with dissolve
    pause
    mc ". . . ."with dis
    mc "Erm..."
    mc "The goat?"
    show aac 94
    chop "Yes, yes! Best goat!"
    chop "He comes from far-off land!"
    chop "Say hi, Maurice!"
    play sound goat
    show aac 96
    mau "*Bleats*" with dis
    show aac 94
    chop "Girls with red eyes love animals!"with dis
    show aac 95
    mc "Do they?"
    show aac 94
    chop "What gift is better than receiving new best friend?!"
    chop "Maurice can do everything!"
    chop "Thirsty? He make you glass of milk. Lonely? He good company! Have valuables? Fear not, he guard home! Tired of cleaning up after him? He turn into many meals and delicious broth!"
    play sound goat
    show aac 96
    mau "*Bleats*" with dis
    show aac 95
    mc "Um..." with dis
    mc "Do you have anything else?"
    show aac 94
    chop "Ah fine, yes, yes! I have more!"
    show aac 97 with dis
    play soundlow whistle
    chop "*Whistles*" with dissolve
    chop "Come here! Client wants to buy you!"
    play sound bird_flying
    show aac 98 with Dissolve(1.5)
    show aac 99
    chop "Good boy!" with dissolve
    show aac 98
    mc "A toucan!"
    show aac 99
    chop "This Maurice."
    show aac 98
    mc "I... thought the goat was named Maur—"
    show aac 99
    chop "Maurice very intelligent! He know all the answers!"
    chop "See for yourself!"
    chop "Maurice, what's the capital of Sweden?"
    play sound toucan
    show aac 100
    mau "Stockholm!" with Dissolve(.7)
    show aac 99
    chop "Good boy!"with Dissolve(.7)
    show aac 98
    mc "Wow, impressive!"
    show aac 99
    chop "Yes!"
    chop "He knows geography, he is good friend, and he make for delicious broth!"
    show aac 98
    mc "Maurice, what's the capital of Norway?"
    play sound2 toucan
    show aac 100
    mau "Stockholm!" with Dissolve(.7)
    show aac 99
    chop "Ah, close! Same peninsula!"with Dissolve(.7)
    show aac 98
    mc "Um..."
    mc "...Maurice, what's three times three?"
    play sound3 toucan
    show aac 100
    mau "Stockholm!" with Dissolve(.7)
    show aac 101
    chop "Yeah, well, he needs bit of practice."with Dissolve(.7)
    show aac 99
    chop "But he very clever!"with dissolve
    chop "I tell you no lies! Only truth!"
    play soundlow bird_flying
    show aac 102 with Dissolve(1.5)
    chop "And finally, my best hairy companion!"with dissolve
    chop "Maurice!"
    show aac 103
    mc "Of course..."with dissolve
    show aac 102
    chop "He's been guardian of the shop!"with dissolve
    chop "He fluffy, he friendly, he cuddly..."
    chop "He also very clever!"
    chop "Say hello to the man, Maurice."
    play sound cat
    show aac 104
    mau "*Greets you*" with Dissolve(.8)
    mc "Awww..."
    show aac 103
    mc "He's adorable." with dissolve
    show aac 102
    chop "Yes, yes! He also..."with dissolve
    show aac 105
    chop "Hold up... Where you grabbed that fish?!" with dis
    play soundlow purr
    mau ". . ."
    chop "THAT'S MY FISH!"
    chop "YOU EATING MY SUPPER!"
    chop "GIVE BACK TO ME!"
    play sound5 cathiss
    mau "*Hissing*"
    play sound rifle
    play sound2 cat
    show aac 106
    chop "Come here!{w=0.25}{nw}" with hpunch
    play sound3 rifle
    chop "Come here!{w=0.3}{nw}" with hpunch
    play sound4 rifle
    chop "Come here!{w=0.5}{nw}" with hpunch
    play sound5 rifle
    chop "Come here!" with hpunch
    show aac 107
    chop "KHACH XIAN TOA LIKO CO!" with dis
    chop "IF I CATCH YOU, I TURN YOU INTO DELICIOUS BROTH!"
    mc "What the..."
    show aac 88
    chop "Well, my friend! That was all! What you going for?" with Dissolve(1.3)
    show aac 87
    mc "Um... I'm not sure if she will like any of these... \"gifts\"."
    show aac 88
    chop "Trust me! No summoner can go without their spirit animal!"
    chop "Only 300 eternals each!"
    show aac 87
    mc "Hmm..."
    default goat = False
    default toucan = False
    default cat = False
    menu:
        with dis
        "Buy the goat":
            $ goat = True
            mc "Um... Okay, I'm taking the goat." with dis
            show aac 88
            chop "Excellent, excellent!"
            show screen eternals with dis
            play sound coins
            $ money -= 100
            pause .05
            $ money -= 100
            pause .05
            $ money -= 100
            pause .05
            chop "Great choice!" with dissolve
            hide screen eternals
            show aac 87
            mc "(I hope Luna likes it...)"with dissolve
        "Buy the toucan":
            $ toucan = True
            mc "Um... Okay, I'm taking the toucan." with dis
            show aac 88
            chop "Excellent, excellent!"
            show screen eternals with dis
            play sound coins
            $ money -= 100
            pause .05
            $ money -= 100
            pause .05
            $ money -= 100
            pause .05
            chop "Great choice!" with dissolve
            hide screen eternals
            show aac 87
            mc "(I hope Luna likes it...)"with dissolve
        "Buy the cat":
            $ cat = True
            mc "Um... Okay, I'm taking the cat." with dis
            show aac 88
            chop "Excellent, excellent!"
            show screen eternals with dis
            play sound coins
            $ money -= 100
            pause .05
            $ money -= 100
            pause .05
            $ money -= 100
            pause .05
            chop "Great choice!" with dissolve
            hide screen eternals
            show aac 87
            mc "(I hope Luna likes it...)"with dissolve
        "[gr]Don't buy any":
            mc "Um... I don't think I'll take any of them." with dis
            show aac 88
            chop "Don't be like that, friend!"
            show aac 87
            mc "I'm sorry, Chop-Chop."
            show aac 88
            chop "Aaahhh, tough negotiator, huh?!"
            chop "Okay, okay, you win! I let you have this one for half price!"
            chop "Only 150 eternals! Once in a lifetime deal!"
            show aac 87
            mc "Hmm..."
            menu:
                with dis
                mod "Buy whichever you prefer."
                "Buy the goat":
                    $ goat = True
                    mc "Um... Okay, I'm taking the goat." with dis
                    show aac 88
                    chop "Excellent, excellent!"
                    show screen eternals with dis
                    play sound coins
                    $ money -= 50
                    pause .05
                    $ money -= 50
                    pause .05
                    $ money -= 50
                    pause .05
                    chop "Great choice!" with dissolve
                    hide screen eternals
                    show aac 87
                    mc "(I hope Luna likes it...)"with dissolve
                "Buy the toucan":
                    $ toucan = True
                    mc "Um... Okay, I'm taking the toucan." with dis
                    show aac 88
                    chop "Excellent, excellent!"
                    show screen eternals with dis
                    play sound coins
                    $ money -= 50
                    pause .05
                    $ money -= 50
                    pause .05
                    $ money -= 50
                    pause .05
                    chop "Great choice!" with dissolve
                    hide screen eternals
                    show aac 87
                    mc "(I hope Luna likes it...)"with dissolve
                "Buy the cat":
                    $ cat = True
                    mc "Um... Okay, I'm taking the cat." with dis
                    show aac 88
                    chop "Excellent, excellent!"
                    show screen eternals with dis
                    play sound coins
                    $ money -= 50
                    pause .05
                    $ money -= 50
                    pause .05
                    $ money -= 50
                    pause .05
                    chop "Great choice!" with dissolve
                    hide screen eternals
                    show aac 87
                    mc "(I hope Luna likes it...)"with dissolve
                "[red](Insist) Don't buy any":
                    mc "I'm sorry, but I'm not interested." with dis
                    mc "Maybe next time!"
                    show aac 88
                    chop "Well okay, okay! Next time it is!"
    show aac 108 with Dissolve(1.3)
    mc "Well, it's time for me to go back! Goodbye!" with dissolve
    chop "THANK YOU, FRIEND! COME BACK ANOTHER DAY!"
    chop "CHOP-CHOP MISS YOU ALREADY!"
    if goat or toucan or cat:
        chop "{size=19}Chop-Chop cannot be held legally liable for any bodily harm or destruction to physical property as a result of this sale. Establishment of friendships with animal is not guaranteed. No refunds or exchanges are permitted.{w=0.6}{nw}"
    chop "BYE BYE FOR NOW!!"
    play sound doorold
    stop music2 fadeout 3
    play music fireplace fadein 4
    scene aac 66 with Dissolve(2.5)
    pause .5
    mc "(Okay...)" with dis
    if goat:
        show aac 119
        mc "(It'd be better if I leave the goat here, for now. I can give it to Luna later. We should solve this case first.)" with dis
        mc "Okay buddy, I'm going upstairs."
        mc "Stay here and don't break anything!"
        play sound5 goat
        show aac 120
        mau "*Bleats*" with dis
    elif toucan:
        show aac 121
        mc "(It'd be better if I leave the toucan here, for now. I can give it to Luna later. We should solve this case first.)" with dis
        mc "Okay buddy, I'm going upstairs."
        mc "Stay here and don't break anything!"
        play sound5 toucan
        show aac 122
        mau "Stockholm!" with dissolve
    elif cat:
        show aac 123
        mc "(It'd be better if I leave the cat here, for now. I can give it to Luna later. We should solve this case first.)" with dis
        mc "Okay buddy, I'm going upstairs."
        mc "Stay here and don't break anything!"
        play soundlow purr
        show aac 124
        mau "*Purring*" with dis
        mc "Good boy!"
    if anniehorror:
        show aac 66
        mc "(Hopefully, the teddy bear will be enough to break the curse or whatever is going on in this town.)" with dis
        mc "(I hope the girls have been okay up there...)"
        show aac 109 with Dissolve(1.8)
        play soundlow chair2
        mc "I'm back!" with dissolve
        mc "You guys been... having fun...?"
        show aac 110
        a "Y-Yeah, sure."
        a "Anne and I have been talking and we're almost friends already, right?"
        a "We've had so much to discuss, and she was just about to remember how she got here."
        kida ". . ."
        a "*Nervous giggle*"
        show aac 109
        mc "It's okay Annie, I know you’re not one for spooky things, but you’ve been doing good! I’m proud of you!"
        show aac 110
        a "T-Thanks..."
    else:
        show aac 66
        mc "(Hopefully, the teddy bear will be enough to break the curse or whatever is going on in this town.)" with dis
        mc "(I hope she's been okay up there...)"
        show aac 112 with Dissolve(1.8)
        play soundlow chair2
        mc "I'm back!" with dissolve
    show aac 111
    l "Were you able to find a toy?" with Dissolve(.8)
    show aac 112
    mc "Yes!"
    show aac 111
    l "Nice! Did you hear that, Anne?"
    l "[mc] brought you a toy! Just for you!"
    show aac 113
    kida ". . ." with Dissolve(1.3)
    kida "This is not Mr. Nebula."
    mc "Y-Yeah, I know, but he's a new friend! He’s been so eager to meet you!"
    mc "He told me he wanted to play with you so bad!"
    kida ". . ."
    mc "D-Do you like him?"
    kida ". . ."
    kida "...Yes."
    mc "(Oh, thank god...)"
    mc "Are you feeling better now?"
    kida "...Yes."
    kida "I wanna see my mommy."
    mc "Of course! We want to get you back to your mom! Do you know where she is?"
    kida "I... don't remember."
    mc "(Well, at least she's talking a bit now.)"
    mc "How about your house? Do you remember where you live?"
    kida "...No."
    mc "Hmm..."
    mc "What's your mother's name?"
    kida ". . ."
    kida "...Alicia Flink."
    show aac 114
    l "*Gasps*" with dissolve
    l "Of course..."
    mc "Huh?"
    show aac 115
    l "*Whispering* Anne Flink! She's the daughter of the factory owner!"with dis
    mc "Oh! The rich guy!"
    l "Yes!"
    l "*Whispering* I heard Mr. Flink left the country after his factory was destroyed..."
    l "*Whispering* Maybe... He and his wife left their daughter here? And now we're supposed to help her?"
    mc "*Whispering* Really? What kind of parents would do such a thing?"
    l "*Whispering* Well, Mr. Flink was not known to be a good person..."
    l "*Whispering* Maybe... if we show the little girl a picture of her mother, the curse will be lifted and we'll solve the mystery of the Foggy District!"
    l "*Whispering* I once participated in a case on this server that was solved in a similar way."
    l "*Whispering* The curse of the River Severn was lifted when I showed the tormented woman, who relentlessly unleashed her anger by drowning innocent fishermen, a picture of her long-lost daughter."
    mc "Hmmm..."
    mc "Alright, it's worth a try."
    l "One of us has to go to her house and grab a picture of her mother. There must be one there."
    default flinkhouse = False
    menu:
        with dis
        "[gr]Go yourself":
            $ flinkhouse = True
            mc "I'll go." with dis
            l "You? Are you sure?"
            l "It could be... dangerous. Or... really scary."
            mc "Oh, now I definitely am going."
            mc "I can't let you have all the fun!"
            $ luna_points += 2
            play sound "beat.ogg"
            show aac 116
            show heartr at topleft
            with Dissolve(.7)
            hide heartr with Dissolve(.7)
            pause
            mc "*Chuckles* What?"with dissolve
            show aac 118
            l "Nothing. I thought I was the only one who enjoys this kind of stuff." with dis
            show aac 117
            l "I've been playing Eternum alone for so long that I forgot I could team up with other people too." with dissolve
            l "It... feels nice."
            l "Thank you."
            show aac 116
            mc "Anytime, Luna."with dissolve
            mc "I’m really enjoying getting to play with you, too."
            mc "This definitely won't be the last time we solve a scary mystery together!"
            if anniehorror:
                mc "Right, Annie?!"
                show aac 110
                a "Y-Yeah, it's s-soooo much fun!"with Dissolve(.7)
                a "T-Team Ghost H-Hunters...!!"
                a "Y-Yaaay..."
                mc "*Chuckles* Don't worry, I won't take long."
            show aac 116
            mc "Where's the Flink house?"with Dissolve(.7)
            show aac 117
            l "It's on the edge of the district... about a 10-minute walk."with dissolve
            l "I think it’ll be pretty easy to recognize because, unlike the rest of the slum, it’s particularly modern and sleek."
            show aac 116
            mc "Alright then, I'll be on my way."with dissolve
            mc "The only things worth fearing are outside Eternum!"
            show aac 117
            l "Good luck!"with dissolve
        "Ask Luna to go":
            mc "I think you should go." with dis
            mc "You're the most experienced in all this scary stuff anyway."
            show aac 114
            l "Alright, I can do it." with dis
            if anniehorror:
                l "Anne, I'm going to visit your house for a little bit. Stay here with [mc] and Annie, ok?"
            else:
                l "Anne, I'm going to visit your house for a little bit. Stay here with [mc], ok?"
            show aac 113
            kida ". . ."
            kida "...Okay."
            show aac 115
            l "I'll be right back." with dis
            l "Stay here, it shouldn't take long."
            mc "No worries, we won’t move a muscle."
            if anniehorror:
                show aac 109
                mc "Right, Annie?" with dis
                show aac 110
                a "Y-Yeah sure, I’m not planning on going anywhere..."
                show aac 115
                mc "Good luck, Luna." with dis
            else:
                mc "Good luck, Luna."
            l "Thanks."
    stop music fadeout 4
    show black
    with Dissolve(2.5)
    pause
    show screen sometimelater with dis12
    pause
    if flinkhouse:
        play music2 syndicate fadein 4
        jump survivalhorror
    else:
        play musicb fireplace fadein 3
        scene aacf 1
        hide screen sometimelater
        with Dissolve(2.4)
        mc "*Yawns*" with dis
        mc "Luna sure is taking a long time..."
        if anniehorror:
            mc "Do you think she's okay?"
            mc "Maybe I should go find her."
            a "And leave me here all alone?! No way!"
            play sound2 chair2
            pause .9
            show aacf 2
        else:
            mc "(Maybe I should go find her.)"
            mc "(But I can't leave Anne by herself...)"
            play sound2 chair2
            pause .9
            show aacf 3
        mc "Hmm?" with dis12
        mc "A-Anne? Is there something wrong?"
        kida ". . ."
        play soundlow run
        show aacf 4
        kida "*Starts running*{w=2}{nw}" with dis15
        show aacf 5 with dis15
        mc "What the... Hey! Wait!" with dissolve
        mc "Come back!"
        if anniehorror:
            mc "Fuck, we have to follow her!"
            a "I'm r-right behind you!"
        else:
            mc "(Fuck, I have to follow her!)"
        stop musicb fadeout 4
        show aacf 6 with Dissolve(2.6)
        mc "*Panting* F-Fuck, how can those little legs move so fast?!" with dis
        play music2b lu fadein 15
        mc "W-Wait, is that..."
        show aacf 7 with dis15
        mc "Luna!" with dissolve
        mc "Have you seen Anne?!"
        show aacf 8
        l "Yeah... She was reunited with her mother."
        show aacf 7
        mc "Her mother?"
        show aacf 8
        l "Yes. She was the source of the curse on this place. They both died tragically in their house, after the angry mob set it ablaze."
        show aacf 7
        mc "What? A fire?"
        mc "Wait... Anne... was dead? But how..."
        show aacf 8
        l "It's a long story. I found... things... inside the house. There was some kind of riddle... but you probably don't wanna know the details."
        l "I know I'm the only one interested in these macabre stories."
        l "Don't worry, I'm used to it..."
        show ha 58 with dis12
        l "Anyways, look. The girl gave me this mysterious  box and then vanished, but she left an Exit Portal behind." with dissolve
        mc "A portal! Thank god, we can leave..."
        jump flinkmansionskip

label survivalhorror:
    scene ha 0
    hide screen sometimelater
    with Dissolve(2.2)
    mc "(Fuck, there aren’t any street lamps around...)" with dis
    mc "(Thank god the house has a lamp, otherwise it would’ve been impossible to find this place.)"
    mc "(Damn, this house definitely looks luxurious. It must be the one... It looks nothing like the other buildings around here.)"
    show ha 0a
    mc "(Is that a... flashlight on that swing? Hm... I don't think that's just a coincidence.)" with dis
    mc "(I might be a noob in Eternum, but I've played enough video games to know that I should take it.)"
    show ha 0b with Dissolve(1.2)
    pause
    play sound switch
    pause 0.05
    scene ha 0c
    pause
    mc "(Seems to work just fine.)" with dissolve
    mc "(If Mr. Flink and his wife supposedly left town months ago, the house isn’t going to have any power.)"
    play sound switch
    scene ha 0b
    mc "(I should probably conserve these flashlight batteries, though.)"
    show ha 0d
    mc "(Well alright then, time to get this over with.)" with dis
    if anniehorror:
        mc "(Here's the plan: I’m just gonna go inside, grab a picture of Ms. Flink, bring it to the girl, and lift the curse of the abandoned child.)"
        mc "(Then Luna will shower me with hugs and Annie will gush non-stop about how I'm the bravest man she's ever met.)"
    else:
        mc "(Here's the plan: I’m just gonna go inside, grab a picture of Ms. Flink, bring it to the girl, and lift the curse of the abandoned child.)"
        mc "(Then Luna will shower me with hugs and gush non-stop about how I'm the bravest man she's ever met.)"
    mc "(Yeah. Sounds like a solid plan to me.)"
    mc "(Let's do it!)"
    play sound dooropen2
    scene ha 1 with Dissolve(2)
    mc "(The main door was unlocked...)" with dissolve
    mc "(And wow, this place looks spotless. I thought for sure it would’ve been pillaged already.)"
    mc "(I mean... I don't know how far the \"immersion\" goes in these kinds of servers. Maybe the village NPCs aren’t programmed to visit this place. Or maybe...)"
    play sound doorold
    stop music2 fadeout 1.5
    pause .6
    show ha 2 with dis
    pause
    play music2b survival fadein 3
    mc "*Gulps* (O-Okay...)" with dis
    mc "(Calm down [mc], it's just a game...)"
    mc "(L-Luna said it herself, this is only a mystery-solving server...)"
    mc "(Nothing can really harm me here...)"
    pause
    mc "(...Right?)" with dis
    play sound switch
    show ha 3 with dis
    mc "(Well at least I have this flashlight...)" with dissolve
    show flink with Dissolve(.2)
    pause 3.5
    play sound4 footsteps
    pause 4.8
    scene hb 1 with Dissolve(.2)
    mc "(F-Fuck this shit, man...)" with dissolve
    mc "(Why can't I be hanging around the servers full of hot girls wearing bikinis? Or why can’t I solve the mystery of who wins the wet T-shirt contest?!)"
    mc "(O-Okay, I need to stay calm.)"
    mc "(There are no ogres, zombies, or any weird stuff on this server. It's j-just a simple mystery server...)"
    mc "(You need to find that damn photo, [mc].)"
    mc "(Where do people keep photos of themselves...)"
    mc "(T-The bedroom? Or maybe the living room...)"
    mod "You can open the help menu at the top right for the quickest path or just explore :)"
    show screen freeroam_help
    call screen hallways with dis
    default livingfirst = True
    default gardenfirst = True
    default corridorfirst = True
    default laundryfirst = True
    default officefirst = True
    default bedroomfirst = True
    default phonesurvival = False
    default safesurvival = False
    default safefirst = True
    default safenumbers = False
    default safen1 = True
    default safen2 = True
    default safen3 = True


label halll:
    play sound5 footsteps
    scene ha 3 with Dissolve(1.5)
    call screen halls with dis
label hallwayl:
    play sound5 footsteps
    scene hb 1 with Dissolve(1.5)
    call screen hallways with dis
label corridorl:
    play sound5 footsteps
    if corridorfirst:
        $ corridorfirst = False
        scene ha 11 with Dissolve(1.5)
        mc "(This fucking house is creeping me out...)" with dis
        show ha 13 with dis
        show ha 11 with dissolve
        show ha 13 with dissolve
        play sound2 flashlight
        mc "(Oh, come on...)" with dissolve
        show ha 11
        pause .1
        show ha 13
        pause .05
        show ha 11
        pause .05
        show ha 13
        pause .4
        mc "(Please, not now...)" with dissolve
        show ha 12
        pause .05
        play sound3 waterphone2
        show ha 13
        pause .1
        show ha 12
        pause .05
        show ha 13
        pause
        mc "(This fucking flashlight... did Chop-Chop sell them this shitty thing?!)"with dis
        mc "(Please, don't fail me now...)"
        play soundlow switch
        show ha 11
        mc "(Oh, thank god.)" with dis
        call screen corridors with dis
    play sound5 footsteps
    scene ha 11 with Dissolve(1.5)
    call screen corridors with dis
label livingrooml:
    play sound5 footsteps
    if livingfirst:
        $ livingfirst = False
        scene ha 4 with Dissolve(1.5)
        mc "(The dining room...)" with dissolve
        mc "(Everything looks so stylish. You can definitely tell they were business people.)"
        show ha 5
        mc "(Hmm... You can also go into the garden from here. It seems to connect the living room and the main bedroom.)" with dis
        show ha 4
        mc "(No pictures of Ms. Flink here, though.)" with dis
        show ha 6
        mc "(In fact, there are no pictures of anyone. Just these... weird paintings everywhere.)" with dis
        show ha 6b
        mc "(This house might be fancy, but it feels so... cold... lifeless.)" with dis
        mc "(Poor Anne. I guess she didn't have a happy childhood. And her parents abandoning her was just the icing on the cake.)"
        mc "(I wonder if...)"
        play sound pianosmash
        show piano
        pause .8
        scene ha 6c with Dissolve(.2)
        pause
        mc "(W-What the fuck...)" with dis
        mc "(Is t-there... someone in this house?)"
        mc "(I need to get out of here... fast...)"
        show ha 6b with dis
        if not bedroomfirst:
            mc "*Sighs*" with dissolve
            play music3 phone
            pause
            mc "(...hmm?)"with dissolve
            mc "(Is that a phone ringing? Where is that coming from?)"
            $ phonesurvival = True
        call screen livings with dis
    scene ha 6b with Dissolve(1.5)
    call screen livings with dis
label gardenl:
    play sound doorsliding
    if safenumbers:
        if safen3:
            $ safen3 = False
            show ha 9 with Dissolve(1.5)
            mc "(Okay... The logs...)" with dissolve
            show ha 10
            mc "(Hmm... There are a lot of them.)" with dis
            mc "(I better count them right...)"
        else:
            show ha 10 with Dissolve(1.5)
            mc "(There are a lot of them. I better count them right...)" with dissolve
        show ha 8 with dis
        call screen gardens with dis
    if gardenfirst:
        $ gardenfirst = False
        scene ha 8 with Dissolve(1.6)
        mc "(Even the garden is still in pristine condition...)" with dis
        mc "(If these people left months ago, who’s been cleaning the house all this time?)"
        show ha 7
        mc "(And what's the deal with all the damn deer everywhere?)" with Dissolve(1.1)
        play soundlow waterphone2
        mc "(Statues, figures, paintings... The whole house is full of them...)"
        mc "(They look creepy as fuck...)"
        show ha 8 with Dissolve(1.1)
        call screen gardens with dis
    scene ha 8 with Dissolve(1.5)
    call screen gardens with dis
label officel:
    play sound5 dooropen1
    if phonesurvival:
        $ renpy.music.set_volume(0.9, channel='music3')
    scene ha 14 with Dissolve(1.5)
    if phonesurvival:
        mc "(Well here’s the phone...)" with dis
        $ officefirst = False
        $ phonesurvival = False
        $ safesurvival = True
        show ha 15
        mc "(Am I s-supposed to pick it up?)" with dis
        mc "(I guess so...)"
        mc "(F-Fuck, I should have asked Luna to come here instead of me...)"
        mc "(Snap out of it, [mc]! The sooner this is over, the sooner I can go back to the comfort of my home.)"
        play sound hangup
        stop music3
        show ha 16
        mc "H-Hello?" with dis
        madi "{i}Alicia?! It's me, Madison!"
        madi "{i}Are you there?!"
        mc "W-What? I'm not..."
        alic "{i}Madison? What's going on? I heard a big explosion!"
        mc "Who..."
        madi "{i}The factory! They blew it up! It’s all gone, Alicia!!!"
        mc "(Am I... Am I listening to a conversation between Anne's mother and another woman?)"
        alic "{i}What?! Oh my god, my husband warned me this would happen..."
        madi "{i}I think they're heading to your house next, Alicia! You have to get out of there!"
        alic "{i}What?! What do they want?"
        play sound3 waterphone3
        madi "{i}They want to burn it down too! You need to run away!"
        madi "{i}I'm on the bridge, in my car. Hurry up!"
        alic "{i}W-What? Oh... FUCK!"
        alic "{i}I..."
        alic "{i}Okay, okay, I'm on my way! But I need to hide something first!"
        madi "{i}What? What for?!"
        alic "{i}Remember the safe I showed you last Friday? Behind the bedroom?"
        alic "{i}It’s a fireproof safe. I have to save the family photo album, Madison!"
        alic "{i}Anne's whole life is in there! I can't lose it all! You know how much it means to me!"
        madi "{i}And where's Anne?!"
        alic "{i}She's at her grandparents' house! We can get her after I meet up with you!"
        play soundlow waterphone2
        show ha 17
        alic "{i}Just let me save the photos!" with Dissolve(1.6)
        madi "{i}Ugh... Fuck! Okay, but please move as fast as you can!"
        madi "{i}The workers are getting close, and they're blinded by hatred for your husband! They’re consumed with rage! I d-don't know what they'll do if they see you there..."
        alic "{i}O-OKAY! Thank you! Don't worry, I'll be right there!"
        madi "{i}PLEASE HURRY!!!!"
        play soundlow busyphone
        show ha 16 with Dissolve(1.2)
        pause
        play sound hangup
        stop soundlow
        show ha 15
        mc ". . ." with dis
        mc "(Well, in the end, they didn't burn the house down... But maybe the family photo album is still in there... I should check it out.)"
        show ha 18 with dis
    if officefirst:
        $ officefirst = False
        pause
        mc "(No family photos anywhere...)" with dissolve
    call screen backs with dis
label laundryl:
    play sound5 footsteps
    if laundryfirst:
        $ laundryfirst = False
        scene ha 22 with Dissolve(1.5)
        pause
        mc "(This room is empty. It almost looks as if...)" with dis
        show toy with Dissolve(.1)
        pause 3.9
        scene ha 23 with Dissolve(.1)
        pause
        mc "*Breathing heavily*" with dis
        mc "(I need to find that thing and leave this place already...)"
        if safenumbers:
            jump laundryl
        call screen backs with dis
    if safenumbers:
        if safen2:
            $ safen2 = False
            scene ha 22 with Dissolve(1.5)
            pause
            mc "(Anne's dinosaurs...)" with dissolve
            show ha 21c
            mc "(He mentioned they were dirty... maybe they’re in the washing machine?)" with dis
            mc "(Or maybe...)"
            show ha 24
            mc "(Oh... they're right here.)" with dis
            mc "(I swear these toys weren't here earlier...)"
            mc "(I g-guess I'm just nervous and I'm overlooking things.)"
            mc "(Anyway... Two dinosaurs.)"
        else:
            show ha 24 with dis
            mc "(Two dinosaurs...)" with dissolve
        call screen backs with dis
    scene ha 22 with Dissolve(1.5)
    call screen backs with dis
label bedrooml:
    play sound5 footsteps
    if bedroomfirst:
        $ bedroomfirst = False
        scene ha 19 with Dissolve(1.5)
        pause
        mc "(The bedroom... with no sign of any pictures.)" with dissolve
        mc "(Just these damn paintings...)"
        if not livingfirst:
            mc "*Sighs*"
            play music3 phone
            pause
            mc "(...Hmm?)"with dissolve
            mc "(Is that a phone ringing? Where is that coming from?)"
            $ phonesurvival = True
        call screen bedrooms with dis
    scene ha 19 with Dissolve(1.5)
    call screen bedrooms with dis
label bathrooml:
    if safenumbers:
        if safen1:
            $ safen1 = False
            show flink2 with dis
            pause 0.9
            play sound waterphone2
            pause 1.2
            scene ha 21b with Dissolve(.3)
            pause
            mc "*Breathing rapidly*" with dis
            mc "(W-What the fuck was that...)"
            mc "(My eyes must be playing tricks on me... Keep it together, [mc]! This is just a fucking Sherlock Holmes server, for god’s sake...)"
            mc "(There's no one here...)"
            mc "(N-Nothing can harm you...)"
            show ha 20
            mc "(T-T-There's no one here...)" with dis
            show ha 21
            mc "(O-Oh yeah... the candles, yeah...)" with dis
            mc "(Three candles...)"
        else:
            show ha 21 with dis
            mc "(Three candles...)" with dis
        call screen backsb with dis
    play sound5 footsteps
    scene ha 20 with Dissolve(1.5)
    call screen backsb with dis
label safel:
    play sound5 footsteps
    if safefirst:
        $ safefirst = False
        scene ha 25 with Dissolve(1.5)
        mc "(There it is! The safe Alicia mentioned on the phone!)" with dissolve
        mc "(The pictures I'm looking for must be inside.)"
        show ha 26
        mc "(Aw fuck, of course, the door is closed.)"with dis
        mc "(Well, maybe it’s...)"
        play sound safedial
        show ha 26b with dis
        mc "(Nope, just as I thought... It's fucking locked.)" with dissolve
        mc "(Goddammit...)"
        stop sound fadeout 1
        show ha 26
        mc "*Sighs*" with dis
        mc "(Well, what's in this little notebook?)"
        show ha 27 with dis
        blank "{i} I can't believe you keep forgetting the combination!" with dissolve
        blank "{i} Let's try to use a mnemonic device this time!"
        blank "{i} There are only three sets of numbers."
        blank "{i}The first number is the number of aromatic candles we keep in the bathroom."
        blank "{i}The second number is how many dinosaurs Anne is always playing with (which are in the laundry room, btw, because they got all dirty and sticky)."
        blank "{i}And finally, the third number is the number of logs we have in the garden (yeah, the ones we cut two winters ago and haven't used yet)."
        blank "{i}Maybe with this trick, you can finally remember it!"
        blank "{i}And if not... You can always come to me and ask."
        blank "{i}I love you, Alicia."
        blank "{i}-Jeremy."
        mc "(Hmmm...)"
        mc "(I guess this was written by Mr. Flink.)"
        mc "(Looks like they had a good relationship.)"
        show ha 28
        mc "(Well, in any case, I can use these clues to open the safe!)" with dis
        mc "(I remember seeing some of those things.)"
        mc "(Come on [mc], we're just about done! You’re on the home stretch!)"
        $ safenumbers = True
    show ha 25 with dis
    menu safesur:
        with dis
        "Read the notebook":
            show ha 27 with dis
            blank "{i}The first number is the number of aromatic candles we keep in the bathroom." with dissolve
            blank "{i}The second number is how many dinosaurs Anne is always playing with (which are in the laundry room, btw, because they got all dirty and sticky)."
            blank "{i}And finally, the third number is the number of logs we have in the garden (yeah, the ones we cut two winters ago and haven't used yet)."
            show ha 25 with dis
            jump safesur
        "Open the safe":
            show ha 28b with dis
            mc "(Okay...)" with dissolve
            menu:
                mod "Would you like to see the answer?"
                "Yes":
                    mod "3, 2, 18."
                "No":
                    pass
            $ combi = renpy.input("First number", allow="0123456789",length=2)
            play sound safedial
            mc "[combi]..." with dis
            $ combi2 = renpy.input("Second number", allow="0123456789",length=2)
            play sound2 safedial
            mc "[combi2]..." with dis
            $ combi3 = renpy.input("Third number", allow="0123456789",length=2)
            play sound3 safedial
            mc "[combi3]..." with dis
            if combi == "3" and combi2 == "2" and combi3 == "18":
                show ha 29
                mc "YES!" with dis
                hide screen freeroam_help
                hide screen freeroam_wt_help
                jump survivalending
            else:
                show ha 26b
                mc "(Fuck, that’s not right...)" with dis
                show ha 25 with dis
                jump safesur
        "Go back":
            jump bedrooml
label survivalending:
    play sound safeopen
    show ha 30 with dis
    mc "(Okay... What do we have here...)" with dissolve
    mc "(An old camera, a newspaper...)"
    mc "(And pictures! Here they are!)"
    mc "(Oh thank the heavens!)"
    show ha 31
    mc "(Yes!)" with dis
    mc "(This little girl looks like Anne. And the woman carrying her must be her mother, Alicia.)"
    mc "(Finally, we solved the case!)"
    mc "(Now I'll just bring this picture to Anne and then the curse will be lifted once and for all!)"
    mc "(Time to get the fuck out of this creepy house.)"
    show ha 30
    mc "(There are a few other things in the safe, but I don't think I’ll need them.)"with dis
    show ha 32
    mc "(Hmm... this newspaper...)" with Dissolve(1.3)
    mc "(It’s from the day after the burning of Flink's factory...)"
    mc "{i}FLINK’S IN FLAMES!"
    mc "{i}Two deaths and 46 reported injuries in a factory fire started yesterday at 4:30 pm in the Foggy District."
    mc "{i}Witnesses claim the fire was intentionally set by a group of workers at odds with local businessman and factory owner, Jeremy Flink."
    mc "{i}After burning the Flink factory down, the perpetrators then went to the residence of the Flink family to destroy it as further revenge. They started another fire that burned the house to the ground."
    mc "(Hmm? Burned the house to the ground? But I thought this was their house...)"
    mc "{i}Alicia Flink, wife of the magnate, panicked after discovering their daughter Anne, only 7 years old, had returned to the house after a visit to her grandparents, just before the fire started."
    mc "(...What?)"
    mc "{i}Breaking through the security barrier, she frantically hurried back into the building to save her only child. Unfortunately, despite the best efforts of firefighters on site..."
    stop music2b fadeout 2
    play sound risingshort
    pause 1.4
    mc "{i}...Both Alicia and Anne Flink were burned alive and left charred to death in their own home, on that fateful night." with dis
    play sound2 switch
    show black
    pause .1
    hide  black
    play sound3 switch
    pause .1
    show black
    pause
    $ renpy.music.set_volume(0.2, channel='music3')
    play music3 beat fadein 6
    mc "*Breathing rapidly*" with dis
    mc "(What...)"
    mc "(T-The mother...)"
    mc "(S-She died in this house...)"
    mc "(A-And she's...)"
    mc "(She's still here...)"
    mc "(Fuck, I have to get to the front door...)"
    mc "(But of course this fucking flashlight isn’t working again and now I can't see shit...)"
    mc "(What am I gonna...)"
    mc "(Wait, the camera from the safe!)"
    mc "(I can use the camera flash to help me navigate out of here!)"
    mc "*Grabbing the camera* (I hope this thing still works...)"
    play sound flashc
    scene ha 33 with flashfast
    scene black with Dissolve(1.5)
    pause .5
    mc "(O-Okay...)"with dissolve
    play sound2 footsteps
    mc "(I can do this...)"
    mc "(L-Let's go...)"
    play sound flashc
    scene ha 35 with flashfast
    scene black with Dissolve(1.5)
    mc "*Breathing heavily*" with dissolve
    play sound flashc
    scene ha 34 with flashfast
    scene black with Dissolve(1.5)
    play sound2 footsteps
    mc "(I'll c-cross the garden. It's the fastest way...)" with dissolve
    play sound3 doorlocked
    pause 1.5
    mc "(W-What?!)" with dis
    mc "(Why is the door to the garden closed?!)"
    mc "(Fuck, I can't open it!)"
    play sound2 footsteps
    mc "(Think, [mc], THINK!! Ummm... I remember you c-could access the garden from the bathroom too.)" with dis
    play sound flashc
    scene ha 34 with flashfast
    scene black with Dissolve(1.5)
    play sound2 footsteps
    pause
    play sound flashc
    play sound4 waterphone3
    scene ha 36 with flashfast
    scene black with Dissolve(1.5)
    mc "(F-Fuck...)" with dissolve
    mc "(W-What the fuck is that thing...)"
    mc "(S-S-She's in the garden...)"
    mc "(I can't go that way...)"
    play sound2 footsteps
    pause
    play sound flashc
    scene ha 35 with flashfast
    scene black with Dissolve(1.5)
    play sound2 footsteps
    pause
    play sound flashc
    scene ha 37 with flashfast
    scene black with Dissolve(1.5)
    play sound2 dooropen1
    mc "(A-Almost there, almost there...)" with dissolve
    play sound flashc
    scene ha 38 with flashfast
    scene black with Dissolve(1.5)
    play sound2 footsteps
    pause
    play sound flashc
    play sound4 waterphone2
    scene ha 39 with flashfast
    scene black with Dissolve(1.5)
    mc "(O-O-Oh s-shit...)" with dissolve
    play sound2 footsteps
    mc "(Noooo... N-Not that way...)"
    mc "(Oh my f-fucking god...)"
    play sound flashc
    scene ha 40 with flashfast
    scene black with Dissolve(1.5)
    mc "(T-The living room... I'm n-nearly there...)" with dissolve
    play sound2 footsteps
    mc "(Come on...)"
    play sound flashc
    scene ha 41 with flashfast
    scene black with Dissolve(1.5)
    mc "(Y-Yes!)" with dissolve
    mc "(The main door! I'm out of here!)"
    play sound5 doorlocked
    pause 2
    mc "(No...)" with dis
    mc "(No, no, no...)"
    mc "(You have to be kidding me...)"
    mc "(This isn't happening...)"
    mc "(Why is the door locked...)"
    play sound chair4
    mc "*Sitting on the floor against the door* O-Okay..." with dis
    play sound flashc
    scene ha 42 with flashfast
    scene black with Dissolve(1.5)
    mc "(I have to come up with a plan...)" with dissolve
    mc "(T-This is just a game, [mc]...)"
    play sound flashc
    scene ha 42 with flashfast
    scene black with Dissolve(1.5)
    mc "(They wouldn't have created this just for you to suffer and die...)" with dissolve
    mc "(...R-Right?)"
    play sound flashc
    play sound4 waterphone3
    play soundlow risinglong
    scene ha 43 with flashfast
    scene black with Dissolve(1.5)
    mc "(F-Fuck...)" with dis
    mc "E-Erm..."
    mc "A-A-Alicia?" with dis
    mc "I... I can help you!"
    mc "I know what they did to you and your daughter was horrible, but I can reunite you with her again!"
    play sound flashc
    play sound5 waterphone2
    scene ha 44 with flashfast
    scene black with Dissolve(1.5)
    mc "P-Please, listen t-to me! I know where she’s at!" with dissolve
    mc "We found her! She's in the slums!"
    mc "If y-you don't kill me I can bring her to you again!"
    mc "Please!"
    play sound flashc
    play sound4 waterphone1
    scene ha 44 with flashfast
    scene black with Dissolve(1.5)
    mc "J-Just give me 10 minutes! I'll bring her here!" with dissolve
    mc "T-Trust me!"
    mc "PLEASE!" with hpunch
    play sound flashc
    stop soundlow fadeout 4
    scene ha 42 with flashfast
    scene black with Dissolve(1.5)
    mc "(O-Oh shit...)" with dissolve
    mc "(S-She left...?)"
    play sound flashc
    stop soundlow fadeout 4
    scene ha 42 with flashfast
    scene black with Dissolve(1.5)
    mc "(Oh thank god, she left...)" with dissolve
    mc "(Now I have to...)"
    play sound3 breathh
    alic "*Raggedly breathing*" with dis
    menu:
        with Dissolve(2)
        "Use the camera":
            play sound flashc
    play sound2 pianosmash
    stop music3
    play sound3 waterphone1
    scene ha 45 with flashfaster
    scene black with Dissolve(1.5)
    mc "AAAAAAAAAAAARGH!" with hpunch
    mc "FUCK!" with hpunch
    mc "FUUUUUUUUUUUUUUUUUCK!!!" with hpunch
    play sound3 dooropen1
    play sound2 doorslam
    show lunasurvival with hpunch
    play music2 night fadein 5
    pause
    mc "W-W-What..." with dissolve
    mc "L-Luna?"
    mc "Luna!" with hpunch
    play sound standup
    if anniehorror:
        show ha 47 with Dissolve(.7)
    else:
        show ha 48b with Dissolve(.7)
    mc "*Standing up* Oh my god, it's so good to see you!" with dissolve
    mc "I've never been so happy to see someone!"
    l "What happened?"
    mc "T-The mother of the little girl! S-She was killed in the house, burned to death by the villagers!"
    mc "And she was... s-still there or... maybe it was her spirit or something, and her body was covered in burns, and..."
    if anniehorror:
        show ha 48
        a "W-What do you mean she was still there??" with dissolve
        a "L-Like a zombie?"
        mc "Yeah!"
        a "W-What?!"
        mc "I found a safe inside the house, and..."
        show ha 47
    mc "I got the photo!" with dissolve
    mc "We have to bring it to..."
    mc "Wait, where's the little girl?"
    l "She suddenly got up and started running in this direction."
    if anniehorror:
        l "We tried following her, but lost track of her shortly before we arrived here."
    else:
        l "I tried following her, but lost track of her shortly before I arrived here."
    mc "Oh, fuck!"
    mc "Now we're never gonna find her!"
    kida "Mister."
    show ha 49 with Dissolve(1.5)
    play music2b lu fadein 15
    stop music2 fadeout 20
    mc "What the..." with dissolve
    mc "Anne..."
    mc "I found your mother! I..."
    mc "I have a picture of her!"
    mc "I... also found out what happened to you and your mom."
    mc "T-That was so horrible. I can’t begin to tell you how sorry I am."
    mc "Your life... was just beginning... and to have it stolen from you, I just..."
    scene ha 50 with dis
    pause
    mc "...Is this box for me?" with dissolve
    scene ha 51 with Dissolve(.4)
    scene ha 50 with Dissolve(.4)
    scene ha 51 with Dissolve(.4)
    show ha 50 with Dissolve(.4)
    pause
    mc "Okay..." with dissolve
    show ha 52 with dis
    mc "*Picking up the box* T-Thank you..." with dissolve
    play sound run
    show ha 53
    kida "*Starts running*" with dis
    mc "Hey! Wait!"
    mc "Come with us! You have to..."
    show ha 54 with Dissolve(1.3)
    mc "Oh my god..." with dis
    if anniehorror:
        a "W-W-What is that?!?!!"
    else:
        l "Who's that..."
    show ha 55
    mc "Mrs. Flink." with dis
    if anniehorror:
        a "W-What?!"
    mc "She was the source of the curse on this place. They both died in their house, separated only by the fire set by the angry mob..."
    mc "The only thing they yearned for..."
    show ha 56
    mc "...was just to be together again." with dis
    mc "They were innocent victims caught in a war they wanted no part of."
    play soundlow eerie
    show ha 57 with Dissolve(1.4)
    pause .2
    l "That's so tragic..." with dissolve
    mc "Sometimes I feel like Eternum's NPC behavior is way too realistic..."
    l "Do you think they’re able to develop real feelings? Like what we see in the movies?"
    mc "I sincerely hope not..."
    play soundlow eerie
    show ha 58 with Dissolve(1.5)
    mc "A portal!" with dissolve
    mc "Thank god, we can leave..."
label flinkmansionskip:
    mc "Does this mean we’ve solved the case, Luna?"
    l "Yes. The Foggy District will now return to normal and a new mystery will soon surface, after some time has passed."
    if anniehorror:
        show ha 59
    else:
        show ha 60
    mc "So... this must be our reward for completing this quest." with dis
    l "I guess so."
    mc "I wonder what's inside..."
    l "Only one way to find out."
    mc "Yep."
    show ha 61 with dis
    pause
    play sound openbox
    show ha 62 with Dissolve(1.8)
    pause
    play sound2 risingshort
    pause 0.8
    stop music2b fadeout 1
    pause 0.4
    show ha 63 with dissolve
    pause
    play music2 gems fadein 10
    l "...[mc]?" with dissolve
    l "What is it?"
    mc "T-This is..."
    show ha 64
    mc "No... this can’t be real..." with Dissolve(1.1)
    mc "Is this..."
    play sound impact
    show ha 65
    l "A Gem of Doom...?" with dis
    if anniehorror:
        show ha 67
        a "You can't be serious. This has to be some sort of mistake..." with Dissolve(.75)
    else:
        l "It's impossible..."
    show ha 64
    mc "But it looks exactly like the Gems that Idriel showed me when I first joined Eternum..." with Dissolve(.75)
    mc "And then I saw another one when Dalia and I met Thanatos, and it looked just like this too!"
    show ha 65
    mc "Could it be real?" with Dissolve(.75)
    l "I..."
    show ha 66
    l "I don't know." with dissolve
    l "I've never seen one up close before."
    show ha 65
    l "We should keep it for now… maybe we can find someone who can examine it and tell us whether it’s real or not." with dissolve
    l "You should hold onto it, [mc]."
    show ha 66
    mc "What?! Why me? You're a much higher level than I am!" with dissolve
    l "I know, but the fact that you’re a newbie means you're less likely to be mugged. No one expects to gain much from looting a low-level player. It’s not worth the effort."
    mc "But... It’s so much responsibility..."
    if anniehorror:
        show ha 67
        mc "What about you, Annie?"with Dissolve (.75)
        a "No way, I can't take it..."
        a "I barely did anything in this mission."
        a "And I doubt it's a real Gem of Doom anyway..."
        a "Although... Real or not, it looks so pretty. I can't take my eyes off it."
    show ha 58
    mc "*Sighs* Okay, I guess I'll keep it in my inventory for now." with dis
    mc "The next time we log in, we can try to find someone who can examine it and tell us what it really is."
    mc "I feel like we've had enough excitement here for today."
    if anniehorror:
        a "Yeah, I’m pretty spent..."
    mc "Let's go back to the real world!"
    stop music2 fadeout 4
    play sound risingshort4
    scene login3 with dis2
    pause 6
    play soundlow whoosh4
    scene white with dissolve
    pause 2
    scene aaq 1 with Dissolve(1.5)
    play music2 happy6 fadein 5
    pause .1
    play sound5 clothes
    play sound4 beep
    mc "DAMN!" with dis
    mc "Holy shit Luna, that was intense!"
    show aaq 2
    l "Yeah, to be honest, that was way more intense than I was anticipating. Sorry about that."
    show aaq 1
    mc "Nah, don't apologize!"
    if flinkhouse:
        mc "Not gonna lie, that quest scared the shit out of me, but I had a blast the entire time!"
        mc "This is gonna be the second time today I’ll have to remove these bricks from my underwear!"
        show aaq 2
        l "I'm glad! Well, not about the bricks. I’m happy you had fun!"
    else:
        show aaq 2
    l "I'm gonna go get changed into something more comfortable, I'll be right back."
    l "Your clothes are right there on the table, by the way."
    show aaq 1
    mc "Alright, I'll get changed too. Thanks for lending me the suit and the visor!"
    play sound clothes
    show aaq 3
    mc "(Wow, it's already nine... And I haven't even had dinner yet.)" with Dissolve(1.1)
    mc "(It's crazy how quickly time passes when you're playing Eternum.)"
    mc "(I'm gonna need a few minutes to remember everything I needed to do before I started playing.)"
    mc "(Now I can understand why a few people have gone crazy by playing this game. They say when people start confusing the real world with Eternum, there's no turning back...)"
    mc "(Man, I hope that never happens to me. Good thing I have stuff to do this weekend and I won't be playing too much.)"
    $ unlock_look("luna", 3)
    play soundlow chair1
    show aaq 4
    l "Done."with Dissolve(1.5)
    scene aaq 5
    mc "Nice!"
    mc "(She's wearing her gloves again...)"
    mc "It feels a little weird to be back. I get so immersed in the game that I feel a little out of place after I log off."
    scene aaq 4
    l "Yes, that happens to me too."
    scene aaq 5
    if goat or toucan or cat:
        mc "I get a strange sense that I'm gonna open that door and find a horrible monster, ghost, or merchant selling some weird..."
        mc "Oh shit, Maurice!" with hpunch
        l "Hmm?"
        scene aaq 4
        l "Maurice?"
        scene aaq 5
        mc "Well... Uhm... I bought you a present when I went looking for a toy to get Anne Flink, but I left it in the house where we first found her."
        mc "It was..."
        if goat:
            mc "...a goat."
        elif toucan:
            mc "...a toucan."
        elif cat:
            mc "...a cat."
        mc "It sounds a little stupid now that I’ve said it out loud."
        scene aaq 4
        l "You bought me a pet? For Eternum?"
        scene aaq 5
        mc "Yeah... I guess people know that I'm a rookie and they take advantage of me. I'm sorry, I..."
        if flinkhouse:
            $ luna_points += 1
            play sound "beat.ogg"
            show aaq 4
            show heartr at topleft
            with dissolve
            hide heartr
        else:
            show aaq 4
        l "I love it! Thank you!" with dissolve
        scene aaq 5
        mc "R-Really?"
        scene aaq 4
        l "Yes!"
        l "In Eternum, an animal can passively increase the magic abilities of a summoner. I was actually trying to get one myself!"
        scene aaq 5
        mc "(I can't believe Chop-Chop was actually telling the truth for once. Guess I need to thank that goofy bastard after all...)"
        scene aaq 4
        l "And besides... No one's ever given me a gift before... other than my father."
        l "Thank you [mc], it means a lot."
        scene aaq 5
        mc "But now we lost it..."
        scene aaq 4
        l "Not at all, I'll go back to the server tomorrow morning and look for... Maurice, you said?"
        scene aaq 5
        mc "*Laughs* Yeah, that's his name."
        scene aaq 4
        l "Don't worry, things don't disappear without reason in Eternum."
        scene aaq 5
        mc "Glad to hear that, then!"
    else:
        mc "I get a strange sense that I'm gonna open that door and find a horrible monster, ghost, or merchant selling some weird stuff..."
        l "*Laughs* I can imagine."
    mc "Well, I guess I should be going now."
    scene aaq 4
    l "Sure... will I see you Monday?"
    scene aaq 5
    mc "Of course!"
    menu:
        with dis
        "[gr]Ask her about the gloves":
            mc "(You know... I think we trust each other well enough.)"with dis
            mc "(I really like Luna, and I'd like to learn more about her...)"
        "Don't ask her":
            mc "(It's probably better just to let it be. I don’t want to come off as pushy.)" with dis
            mc "Take care, Luna!"
            scene aaq 4
            l "Bye!"
            $ lunapath = False
            $ lunau = False
            jump annierub
    mc "Um..."
    mc "You don't have to answer this if you're uncomfortable about it, but..."
    mc "Why the gloves?"
    show aaq 6
    l "Oh..." with dis
    l "Uhh... I..."
    show aaq 7
    mc "Y-You know what, forget I asked. I'm sorry, Luna."
    if luna_points <= 3 or not flinkhouse:
        show aaq 6
        l "It's just that... yeah, I am a bit uncomfortable talking about this. Maybe some other day."
        scene aaq 7
        mc "No worries, I understand."
        mc "(It's probably better just to let it be. I don’t want to come off as pushy.)"
        if not flinkhouse:
            mc "(Maybe she doesn't trust me because I sent her to that damn house instead of going myself...)"
            mc "(I fucked up.)"
        mc "Take care, Luna!"
        scene aaq 6
        l "Bye..."
        $ lunapath = False
        $ lunau = False
        jump annierub
    show aaq 6
    l "No, it's okay, don't worry."
    show aaq 7
    mc "I'm just curious because I thought maybe you’d be hiding a birthmark or something, as I know some people are self-conscious about that kind of stuff... but you weren't wearing any gloves inside Eternum."
    mc "And I know it's a rather weird compliment to give to someone, but you have beautiful hands."
    show aaq 6
    l "T-Thanks..."
    show aaq 7
    mc "Hey, I completely understand you don't want to talk about this, Luna."
    mc "Forget I even mentioned it!"
    mc "*Laughs* Hey, you probably just enjoy wearing gloves and I'm here searching for a reason that doesn't even exist!"
    show aaq 6
    l "It's not that..."
    l "It’s just... When I was in middle school, I told a friend about this and she... freaked out."
    l "She stopped talking to me and then all the other kids started to call me a freak because of her."
    l "I haven't had any real friends since then."
    show aaq 7
    mc "I'm sorry to hear that, Luna... Kids can be crueler than adults sometimes."
    mc "But don't worry, no matter what you say, I'll always be there for you. We're friends now, alright??"
    show aaq 8
    l "I started wearing gloves ever since that incident and I never take them off." with dis
    mc "Seriously Luna, you don't have to explain yourself."
    play sound clothes
    show aaq 9
    l "*Takes her gloves off*" with Dissolve(2.3)
    mc "(Just like in Eternum, she has fair, gentle-looking hands.)"
    mc "(I'm so used to seeing her with gloves that she seems so vulnerable without them.)"
    show aaq 10
    l "I haven’t told this to anyone ever since that incident."  with dis
    l "Promise me that you won't think I'm crazy."
    show aaq 11
    mc "What? I could never think that of you!"
    show aaq 10
    l "Okay, and if you were to believe me... promise me that you won't freak out either."
    show aaq 11
    mc "No matter what you say to me, or even choose not to say to me..."
    mc "You're truly a wonderful person, and I'm so glad to have you in my life."
    mc "Nothing will ever change that."
    stop music2 fadeout 8
    l ". . ."
    scene aaq 10
    l "When I..."
    l "When I touch someone with my bare hands..."
    play music2b syndicate fadein 9
    l "I can see their future."
    scene aaq 11
    mc "Their... future?"
    mc "Like what will happen to them tomorrow?"
    scene aaq 10
    l "It could be the next hour, day, week, or even month."
    l "I can't really know until I touch them."
    scene aaq 11
    mc "(Wow... I wasn't expecting that. I was thinking maybe she had really clammy hands or something.)"
    mc "And what kind of things can you see?"
    scene aaq 10
    l "It could be anything, if it's close enough in time."
    l "I saw my teacher being fired, my classmate's dog having an accident, my neighbor moving to another state, and..."
    l "I s-saw my mother dying."
    scene aaq 11
    mc "Oh my god... That must have been such a horrible thing for you to witness..."
    scene aaq 10
    l "That was the first thing I saw. I was only 5."
    l "Soon after that, she was diagnosed with a heart disease, and..."
    l "She died 3 months later."
    scene aaq 11
    mc "I'm so sorry, Luna..."
    scene aaq 10
    l "It's okay. It happened a long time ago."
    l "When I was 7, I decided to start wearing gloves all the time, to avoid accidents."
    l "I don't need to wear them in Eternum because it doesn't work there."
    scene aaq 11
    mc "No one else knows about your power?"
    scene aaq 10
    l "No one. Not even my father."
    l "I thought it'd be better to keep it to myself."
    scene aaq 11
    mc "It really means a lot that you decided to trust me, Luna. I know it’s not an easy thing to do."
    show aaq 12
    mc "So, what you’re saying is..."with dis
    mc "If you touched me with your bare hands right now, you would be able to see my future?"
    scene aaq 13
    l "Y-Yeah, but that's a bad idea."
    scene aaq 12
    mc "Why? I'm both perplexed and fascinated."
    mc "I wanna know my future!"
    scene aaq 13
    l "But... what if I see something bad?"
    scene aaq 12
    mc "Eh, I'm sure it won't be anything that bad! Maybe you’ll just see me ripping my pants at school, or something."
    mc "And hey, you might be able to see something that could help us with the mystery of Benjamin's death! Or maybe something that allows me to prevent a tragedy."
    scene aaq 13
    l "But..."
    scene aaq 12
    l ". . ."
    scene aaq 13
    l "Are you sure about this, [mc]?"
    scene aaq 12
    mc "100\% sure. I want you to be the {i}real{/i} you, Luna. I don’t want you to hold back part of yourself when you’re with me."
    scene aaq 13
    l "...okay."
    l "R-Raise your hand with your palm facing down."
    show aaq 14
    mc "Like this?" with dis
    l "Yes."
    show aaq 15
    l ". . ." with dis
    l "If I do this, there's no turning back."
    mc "I know. Whatever you see, our relationship won't change. I promise."
    l ". . ."
    play sound risingshort
    pause 1
    stop music2b fadeout .2
    show aaq 16 with dissolve
    pause
    mc "(Hmm... I don't feel anything.)"with dissolve
    mc "(Just her warm hand holding mine.)"
    show aaq 17 with Dissolve(1.2)
    pause
    mc "Luna?" with dissolve
    play music2 happy6 fadein 4
    show aaq 18
    l "Oh my god..." with Dissolve(1.2)
    mc "Is it t-that bad?"
    show aaq 19
    l "No... that’s impossible..." with dis
    mc "What did you see?"
    l "Nothing."
    mc "Huh? Nothing?"
    show aaq 20
    l "Nothing! I'm touching you and I can’t see anything!" with dis
    mc "Is that... a good thing?"
    l "It's wonderful!"
    show aaq 21
    l "Look at this!" with dis
    l "I can finally touch someone with my bare hands, without having any kind of visions or feelings of dizziness!"
    mc "Did you... lose your power somehow, then?"
    show aaq 22
    l "No. I still have it. I can feel it." with dis
    l "It's just... you."
    show aaq 23
    l "I can touch your hands, your chest, your face..." with dis
    show aaq 24
    l "And I see nothing!"with dissolve
    show aaq 23
    l "It's like touching a table or... a coffee mug!"with dissolve
    mc "*Laughs* I guess I'll take that as a compliment."
    show aaq 24
    l "It's amazing..." with dissolve
    mc "(Man, I can feel her body pressing against mine.)"
    mc "(And her face is so close...)"
    mc "(I can feel her warm breath against me...)"
    mc "(She's even prettier up close.)"
    show aaq 25 with dis
    pause
    mc "(Why did she stop talking?)" with dissolve
    mc "(I can't stop gazing into her eyes... they’re so...)"
    mc "(Should we...)"
    mc "(Should I...)"
    show aaq 26 with dis
    l "*Clears throat* S-Sorry, I got carried away. It's just that... I wasn't expecting this at all." with dissolve
    mc "N-Nothing wrong with that!"
    show aaq 27 with dis
    l "Well... I, umm, guess I should start preparing dinner." with dissolve
    l "My dad will be here soon."
    $ luna_points += 1
    play sound "beat.ogg"
    show aaq 29
    show heartr at topleft
    with dissolve
    hide heartr
    l "I'm glad you convinced me to try this." with dissolve
    l "I'm happy to have someone with whom I can finally share everything."
    show aaq 28
    mc "And I'm so happy I’m lucky enough to be that person, Luna."
    mc "Whatever you need, I'll always be there for you."
    show aaq 29
    l "Thank you."
    show aaq 28
    mc "Will I see you Monday, then?"
    show aaq 29
    l "Of course. We can meet at lunchtime... if you want."
    show aaq 28
    mc "I'd love that."
    mc "Take care, Luna. Have a nice weekend!"
    show aaq 29
    l "You too."
    l "Take care... [mc]."
    jump annierub


label annierub:
    default anniethigh = False
    stop music2 fadeout 4
    show black with Dissolve(2.4)
    pause
    show screen afewhourslater with dis12
    pause
    play music2b rain3 fadein 5
    scene an 1
    hide screen afewhourslater
    with Dissolve(3)
    mc "(Ah... Tomorrow's Saturday at last.)" with dis
    if nancypath or daliapath:
        mc "(I hope I can get a restful night's sleep.)"
        if daliapath and nancypath:
            mc "(I have to train with Dalia and join Nancy's yoga class in the morning.)"
            mc "(At least both things are in the same gym.)"
        elif nancypath:
            mc "(I gotta join Nancy's yoga class tomorrow morning.)"
        elif daliapath:
            mc "(I gotta go to the gym with Dalia tomorrow morning.)"
    play sound sneeze
    mc "*Sneezes*" with dis
    mc "(Fuck, this room sure is cold... and this terrible weather isn't helping.)"
    play sound2 switch
    play music2 fluorescent fadein 2
    show an 2 with dis12
    mc "(Ahh... This will help.)" with dissolve
    mc "(Feeling warmer already.)"
    stop music2 fadeout 3
    play sound3 chair1
    show an 3 with dis
    mc "(Hmmm...)" with dissolve
    if penelopepath:
        mc "(Looks like Penny hasn't uploaded anything today.)"
        mc "(Maybe she's waiting for Sunday. I'm sure we can take a few good photos for her.)"
    if lunapath:
        mc "(And it seems that Luna isn't on any sort of social media.)"
        mc "(The thing with her hands left me pretty intrigued. I usually don't believe in that kind of stuff, but... I don't know, she seemed sincere.)"
        mc "(We should find out more about her ability. I want to help her feel normal again.)"
    if not penelopepath and not lunapath:
        mc "(Meh, nothing interesting on the news.)"
    play sound chair1
    show an 4
    mc "*Yawns* (Well, time to hit the sack.)" with dis
    mc "(I hope I don't have much trouble falling asleep...)"
    if not anniehorror:
        stop music2b fadeout 3
        show black with Dissolve(2.6)
        pause
        jump saturdaymorning
    stop music2b fadeout 4
    play music2 sneaky fadein 5
    show an 5 with Dissolve(3)
    play sound brushteeth1
    a "*Brushing her teeth*" with dis12
    play sound2 brushteeth2
    show an 6
    a "*Brushing her teeth*" with dis12
    play sound3 brushteeth1
    show an 7
    a "*Brushing her teeth*" with dis12
    a "(It's impossible...)"
    a "(That Gem of Doom can't be real.)"
    play sound brushteeth2
    show an 8
    a "(There are only 10 of them in the world.)" with dis
    a "(It has to be fake... right?)"
    play sound4 brushteeth1
    show an 7
    a "(We have to bring it to an expert. Or I could ask Idriel the next time I visit the Main Nexus.)" with dis
    a "(Well, who cares. It's gonna be a fake, for sure. Probably a knock-off... a “Gem of Boom”.)"
    play sound2 brushteeth2
    show an 8
    a "(But... what if it's not...)" with dis
    a "(We'd be the owners of a Gem of Doom! Like Thanatos!)"
    play sound3 brushteeth1
    show an 7
    a "(That server sure was scary, though... I hope we don't have to go back there ever again.)" with dis
    a "(And the worst part is that I couldn't show my powers to [mc]...)"
    play sound clothes
    show an 9
    a "(I barely did anything, actually.)" with dis15
    a "(He must think I'm a useless, scared kid...)"
    play sound2 clothes2
    show an 10
    a "(Luna seems quite strong... She told me she can summon a level 20 banshee...)" with dis12
    a "(And Dalia can carry a sacred great sword... in one hand!)"
    play sound3 clothes
    show an 11
    a "(And meanwhile... Little Annie can't do anything but cower at the sight of anything even remotely scary or dangerous.)" with dis15
    a "(Yeah, nice job impressing [mc] in Eternum, Annie.)"
    play sound4 brushteeth1
    show an 12
    a "(Well... to be fair, it didn't scare me {i}that{/i} much.)" with dis
    a "(I mean, sure... I was scared in the server, but all fear was erased shortly afterward! After I... uhh... got back to the real world... agh.)"
    play sound5 brushteeth2
    a "(But who wouldn't have been scared?!)"
    a "(There was a freaking zombie!)"
    play sound spit
    show an 13
    a "*Spitting the water*{w=1}{nw}" with dis
    play sound2 spit
    a "*Spitting the water*"
    show an 14
    a "Aaaaaaaah..." with dis12
    show an 15
    a "(That's right! I'm not scared at all right now!)" with dis
    a "(I gotta give myself some credit for that.)"
    a "(The old Annie would be in her room right now, hiding under the blankets and trembling with fear.)"
    a "(Well, not anymore!)"
    play sound toilet
    stop music2 fadeout 5
    play music2b rain3 fadein 5
    show an 16 with Dissolve(1.8)
    a "*Giggles* (I still remember when I watched The Ring a couple of years ago and I couldn't sleep for days.)" with dissolve
    a "(It took me a while, but I finally understood that the scary things in video games and movies stay there.)"
    a "(There are no ghosts or zombies in the real world.)"
    show an 17
    a "(Anyways, I should get some sleep.)"
    stop sound
    play music2b horrorsound
    show an 18
    pause 3.5
    play music2b rain3
    show an 19
    a "(S-Since when has this hallway looked so scary?)"
    a "(Why is it so dark? It seems way darker than usual!)"
    a "(I shouldn't have been the last one to go to bed...)"
    show an 16
    a "(Oh, please! That was the old, scared Annie coming out there for a second!)" with dissolve
    a "(New Annie is not afraid of a little dark corridor!)"
    a "(Let's just go to my room, come on.)"
    show an 17
    a ". . ." with dissolve
    play music2b horrorsound
    show an 18
    pause 3.5
    play music2b rain3
    show an 20
    a ". . ."
    show black with Dissolve(2.1)
    pause
    play sound knock2
    pause .8
    scene an 4 with dis12
    mc "Hmm...?" with dissolve
    show an 21
    mc "(Did someone knock on the door?)" with dis08
    mc "Uhh... yes?"
    blank ". . ."
    play sound chair2
    show an 22 with dis12
    mc "(I’m probably just imagining things...)" with dissolve
    play sound dooropen1
    show an 23 with dis
    pause .3
    mc "Annie?"with dis
    mc "Is something wrong?"
    show an 24
    a "Oh, [mc]! I wasn’t sure if you were asleep already!" with dis
    a "Nothing's wrong! I’m fine... It's just that..."
    a "Well, you know, I was heading to my room, and..."
    a "I..."
    show an 25
    mc "Let me guess. You're scared shitless after that horror server and now you're seeing ghosts and monsters everywhere."
    show an 24
    a "Erm..."
    a "P-Perhaps."
    show an 25
    mc "I told you! You shouldn't have played in Luna's server, Annie! You can't handle that scary stuff! Remember when we played Dead Space?"
    show an 24
    a "I know, b-but I didn't want you—I mean, I didn’t want Luna to think I'm a scaredy-cat!"
    a "I..."
    a "You're right, I'll go back to my room."
    a "S-Sorry to bother you."
    show an 25
    mc ". . ."
    menu:
        with dis
        "[gr]Let her sleep in your room":
            mc "*Chuckles* Oh, Annie. Never change, alright?" with dis
            mc "Do you wanna sleep here tonight?"
        "Send her to her room [red][mt](Closes Annie's path)":
            $ sendroom = True
            mc "Annie..." with dis
            mc "If you don't face your fears, you'll never get over them."
            mc "Come on, go back to sleep. Ghosts don't exist!"
            show an 24
            a "Y-You're right, I guess."
            a "I'll go back to my room."
            a "Ghosts don't exist."
            a "Ghosts don't exist..."
            show an 25
            mc "Do you want me to go with you?"
            show an 24
            a "No! It's okay. I'm an adult. I can handle myself."
            a "Ghosts... don't... exist..."
            show an 23
            mc "Alright then!" with dis
            mc "Remember, only Dalia, Penny, Nancy, and I are inside this house."
            mc "No one else. No ghosts, ok?"
            a "Mm-hm..."
            mc "Good night!"
            play sound doorclose
            show an 22 with dis12
            pause
            mc "(I kind of feel bad, but it's the only way she can overcome her fears.)" with dissolve
            play sound2 chair1
            show an 4
            mc "(I did the right thing.)" with dis
            mc "*Yawns*" with dis
            mc "(Well, back to sleep.)"
            mc "(Big day tomorrow...)"
            $ anniepath = False
            $ annieu = False
            stop music2b fadeout 3
            jump saturdaymorning
    show an 26
    a "R-Really?" with dis
    a "Can I?"
    show an 27
    mc "Of course. In the end, I only want you to feel safe. So how can I say no?"
    show an 26
    a "T-Thank you! It’ll only be tonight, I promise!"
    show an 27
    mc "You can sleep here as many times as you want. You don’t even have to ask, alright?"
    mc "But tomorrow you’re getting tasked with some eye bleach therapy. You need to spend all day watching videos of cute kittens on YouTube! I don't like seeing you scared."
    show an 26
    a "I will! Thank you!"
    show an 27
    mc "Anytime, Annie."
    show an 26
    a "Thanks!"
    show an 28
    a "D-Don't tell the people in the Ion Server that I got scared playing Eternum, though." with dis08
    a "Some of the girls there think I'm a badass. It would destroy my reputation."
    mc "*Laughs* I won't say a word, I promise."
    play sound chair1
    show an 29
    a "Hey, your room is so cozy!" with dis
    a "And you have a nice view of the backyard!"
    mc "It is pretty nice!"
    a "My room faces the front yard. It’s a nice view too, but sometimes you can hear all the cars passing by."
    play sound2 chair1
    show an 30
    a "Well, time to sleep, I guess..." with dis
    a "Luckily your bed is big enough for the both of us. You could probably even fit three or four people on here!"
    show an 31
    mc "Yeah, it is. I gotta thank Nancy for that."
    show an 30
    a "For sure... She's been super nice so far."
    a "We gotta prepare something to thank her one of these days."
    show an 31
    mc "Agreed. I'll think of something."
    show an 30
    a "G-Goodnight, [mc]."
    show an 31
    mc "Goodnight Annie."
    show an 32 with dis12
    pause
    scene an 33 with Dissolve(2.5)
    pause
    mc "(Mmm...)" with dis
    mc "(It smells so good...)"
    mc "(Smells like strawberries...)"
    show an 34
    mc "(Hmm... Since when did my room start to smell so good?)" with dis
    show an 35
    mc "(Mmmm?)" with dissolve
    mc "(Oh yeah... I forgot that Annie came to sleep in my room.)"
    mc "(She...)"
    show an 36
    mc "(S-Shit, why are we in this position?!)" with hpunch
    show an 37 with dis
    mc "(Fuck, she's holding onto my arm.)" with dissolve
    mc "(I can't move it without waking her up...)"
    show an 36
    mc "(She's probably used to hugging a pillow while she sleeps, or something.)" with dis
    show an 38
    mc "(Well, she's gonna move eventually, I guess.)" with dissolve
    mc "(I hope she doesn't wake up before doing so, though.)"
    mc "(We're in quite an... intimate position... I don't want her to think I'm trying to take advantage of her while she sleeps.)"
    mc "(I can feel her boob on my arm... It feels so...)"
    play sound thunder
    show an 39 with Dissolve(.2)
    pause .3
    show an 40 with Dissolve(3.2)
    a "Hmmm..." with dis
    mc "(I fucking hate Kredon's weather...)"
    show an 41 with dis
    a "(Mmm?)" with dissolve
    a "(Oh my god, why are we in this position?!)"
    a "(Oh shit, I'm grabbing his arm! He must be thinking I'm trying something...)"
    a "(This is so embarrassing!)"
    show an 42
    mc "Um..." with dis
    mc "A-Are you awake, Annie?"
    play sound2 chair1
    show an 43 with hpunch
    a "Y-Yeah! S-Sorry!" with dissolve
    show an 44
    mc "Sorry for what?"
    mc "I'm the one who should be sorry!"
    mc "I... Uhm... I swear I wasn't trying anything."
    show an 43
    a "I know! I was the one who grabbed your arm..."
    a "I'm used to hugging Baloo whenever I doze off, so..."
    show an 44
    mc "Baloo?"
    show an 45
    a "Oh... Well... It's a stuffed bear that my mother gave me when I was 5, and..." with dissolve
    a "Well, you know, I got so used to sleeping with it, and..."
    show an 45b
    a "(Oh my god, why did I say that?! Now I probably sound like a child to him...)" with dissolve
    show an 44
    mc "Oh... I didn't know about Baloo."with dissolve
    show an 46
    a "W-Well, I just like to hug something while I sleep... so it makes it hard when I don’t have anything..." with dissolve
    show an 45
    a "I guess I could use a... p-pillow or... I don't know..."with dissolve
    show an 45b
    a "(I'm stupid.)" with dissolve
    if annie_points >= 3:
        a "(Of course [mc] would never want to be with me.)"
    else:
        show an 45
        a "Um... I guess it'll be better if I sleep in my own bed now." with dissolve
        a "I'm not scared anymore, so... Thank you."
        a "I'll see you around."
        a "N-Night."
        play sound doorclose
        show an 21
        a "*Leaves*" with dis
        mc "(Damn, that came out of the blue.)"
        $ anniepath = False
        $ annieu = False
        mc "*Sighs* (I guess I fucked it up, just like always.)"
        play sound2 chair1
        show an 4
        mc "(Anyway, I'll talk to her tomorrow.)" with dis
        mc "*Yawns*" with dis
        mc "(I can't do much more now. Back to sleep.)"
        mc "(Big day tomorrow...)"
        stop music2b fadeout 4
        jump saturdaymorning
    a "(He probably just sees me as the little girl who still plays with stuffed animals... the tiny little thing who’s barely tall enough to ride a rollercoaster.)"
    a "(I can't blame him. He probably prefers real women... taller ones, over 5'5 at least, with a big butt and a nice rack.)"
    a "(I'll always just be Annie, the \"best friend\".)"
    show an 44
    mc "I think that's so cute!" with dissolve
    mc "You can hold onto my arm if you want!"
    mc "I don't mind!"
    mc "(Oh god, look at how embarrassed she is. She's probably thinking that I'm a filthy pervert.)"
    mc "(I'm a fucking mess. She needs someone more mature.)"
    mc "(This is why I'll always just be [mc], the \"best friend\"...)"
    show an 43
    a "Well, you woke up before I did, so I was probably making you uncomfortable."
    show an 44
    mc "Nonsense! I could never feel uncomfortable around you."
    mc "It was just... uhh... your shirt. Yeah, it feels a little itchy against my skin. That’s it. Just the shirt, not you at all."
    show an 45
    a "My shirt is bothering you...?" with dissolve
    mc "Um... Y-Yeah. Just itchy, y’know."
    mc "(Jesus Christ, I need to come up with some better excuses.)"
    if dalianaked:
        mc "(This one was even worse than when Dalia caught me in the bathtub.)"
    show an 46
    a "Well, if my shirt is bothering you..." with dissolve
    a "I... umm... I can take it off... o-only i-if you want me to."
    show an 45b
    mc ". . ." with dissolve
    mc "*Gulps*"
    mc "Uhh..."
    mc "(Did I hear her correctly?)"
    mc "W-What?"
    show an 46
    a "My... my shirt." with dissolve
    a "If it’s making you itchy, I can just take it off..."
    play music2 anniesexy fadein 12
    stop music2b fadeout 20
    a "If it makes both of us feel more comfortable... then I don’t really mind..."
    a "I'm not s-shy..."
    a "It’s just a shirt after all, right...?"
    show an 45b
    mc "(I'm not sure where she’s going with all of this...)"with dissolve
    mc "(But I sure as hell want to find out...)"
    mc "Oh, o-okay..."
    mc "I mean, yeah, as long as you don't mind..."
    mc "I think that would definitely help us both to... sleep... better..."
    show an 46
    a "Yeah, that’s umm... what I was thinking, too..."with dissolve
    show an 48
    mc "(Oh my god, is she really gonna do it?)" with dis
    mc "(This doesn't seem like the Annie I’ve known since I was young... Is she trying to prove something?)"
    a "(Oh man, what am I doing?! I... I can’t...)"
    a "(...No. You’re a woman now, Annie. It’s time to prove it to yourself... and prove it to [mc].) "
    play sound clothes
    show an 49
    mc "(Holy shit, I’ve never seen her in such an... intimate way...)" with dis
    if mrxglasses:
        mc "(Well, apart from the time I used Chop-Chop's glasses in Eternum, but I probably shouldn't mention that right now...)"
    show an 52 with dis12
    mc "(My god... I can’t keep my eyes off of her...)" with dissolve
    mc "(This is really Annie... {i}my{/i} Annie.)"
    mc "(The fact that she’s willing to be so vulnerable with me...)"
    mc "(I swear to god, I won’t let anything ever happen to her.)"
    mc "(If Axel, or anyone else, touches her again... I'm gonna kill them.)"
    show an 51
    a "T-This is... okay, right?"
    a "We're just... friends getting a little more comfortable."
    show an 52
    mc "Of c-course! Not a big deal. After all, I've seen Chang naked hundreds of times."
    mc "More times than I'd like, honestly."
    show an 53
    a "*Laughs* Yeah, I remember that one time he dove into the school pool and came out of the water missing his trunks. Everyone in class saw that!" with dissolve
    mc "*Laughs* True, I'd forgotten about that."
    show an 52
    a "(Be confident, Annie! You’ve made it this far, you can’t turn back now!)" with Dissolve(.4)
    show an 53
    a "Well... umm... hopefully you don’t forget about this..." with Dissolve(.4)
    show an 54 with dis15
    mc "(Oh my god...)" with dissolve
    mc "(I have now seen the light...)"
    mc "(My precious Annie...)"
    mc "(She's...)"
    show an 56
    a "Um, [mc]...? Oh man, I must look weird or someth—" with dis
    show an 57
    mc "Annie... you are so... beautiful..." with dissolve
    show an 56
    a "Oh, stop..." with dissolve
    a "I'm struggling trying to get over my embarrassment here... your jokes aren’t helping..."
    show an 57
    mc "I'm not making fun of you! I'm telling you the truth." with dissolve
    show an 56
    a "Come on, I'm not like the other girls at school. I’m too short, too flat, and too..." with dissolve
    show an 57
    mc "Too perfect. That’s what you are." with dissolve
    show an 57b
    a "Umm..." with dis
    show an 56
    a "W-Well... um, anyways... we should probably try to get some sleep now..." with dis08
    show an 57
    mc "Y-Yeah... you’re probably right." with dissolve
    play sound chair1
    show an 58 with dis15
    pause
    show an 59
    a "Any itchiness?"with dissolve
    show an 58
    mc "Not at all... I feel... much better."with dissolve
    show an 59
    a "Mm, good!" with dissolve
    show an 58
    mc "Your skin feels so soft, Annie. It feels... really nice holding you..."with dissolve
    show an 59
    a "T-Thank you. You f-feel really nice, too..."with dissolve
    show an 58
    mc "And I love your smell. Strawberries, right?"with dissolve
    show an 59
    a "Y-Yes. It's my perfume. You... smell like... you. B-But I like it. I’ve always found your scent comforting..."with dissolve
    show an 61
    mc "(Oh my god, am I the only one feeling all this tension in the air? I want to make a move, but... I don’t want to overstep my bounds...)"with dis
    a "(Oh god, he must feel my heartbeat going crazy. I’m so nervous, but I can’t help wanting more...)"
    mc "(She feels so good in my arms... her body against mine... her chest moving with each breath...)"
    a "(I feel so... safe in his arms... his hold is firm, yet so gentle and warm...)"
    mc "(Damn it, she feels too good, I’m getting hard...)"
    a "(Um, is that...? I think I can feel him... down there...)"
    a "(Come on, Annie. Don’t be so naive. You're topless in bed with a guy. What did you think was going to happen?)"
    a "(But it’s not just any guy. It’s [mc].)"
    a "(You've had a crush on him since you were nine years old. You’ve been fantasizing about this moment for so long. Now it’s finally here... what are you going to do about it?)"
    mc "(I really want to move things forward...)"
    mc "(But... I don't want to scare her away. Annie has always been so special to me. If I try something and it doesn't work out, I couldn’t bear the thought of losing her...)"
    a "(I can’t deny it... I want more of him...)"
    a "(But what if I screw things up? I don't want to lose him. He means too much to me... we’ve been through so much together...)"
    mc "(Then again, this is a side of her I’ve never seen before. Maybe it’s a sign. Should I...?)"
    menu:
        with dis
        "Stop here":
            mc "(I better not risk it. This is the closest we’ve ever gotten and I shouldn’t push my luck.)" with dis
            mc "(Baby steps, [mc]. Baby steps.)"
            mc "Goodnight, Annie."
            show an 59
            a "G-Good night, [mc]."with dis
            show an 61
            a ". . ." with dis
            stop music2 fadeout 4.5
            jump saturdaymorning
        "[gr]Go further":
            $ anniethigh = True
            mc "(I’ve had too many regrets in life. I’m not going to add another to the list. Time to take a chance...)" with dis
            mc "Um... Annie...?"
    show an 59
    a "Y-Yeah...?" with dis
    show an 58
    mc "I’m just going to come right out and say it. I can’t help it, you’re really turning me on right now..."with dissolve
    show an 59
    a "R-Really? W-Well... I guess that’s normal, given the circumstances."with dissolve
    a "...But, for what it’s worth, you’re really turning me on too..."
    show an 58
    mc "I’m sorry, I know I must be really poking you right now..."with dissolve
    show an 59
    a "*Nervous laughter* D-Don't worry! It's okay..."with dissolve
    a "It um... doesn't bother me."
    show an 61
    mc "(Well, here goes nothing...)" with dis
    a "(\"Doesn't bother me\"?? Really, Annie?!)"
    a "(Couldn't you think of anything better to sa—)"
    show an 62
    a ". . . !" with dis
    show an 64 with dis12
    pause
    show an 65
    a "(Is that his...?)" with dis
    mc "I’m sorry, Annie... I can’t help it... you’re driving me insane..."
    mc "Are you okay with this...?"
    show an 64
    a "Yes... " with dis
    a "You feel... good there..."
    show an 65 with dis
    a "But now I wanna know how you feel back here..." with dis
    $ renpy.music.set_volume(0.43, channel='music2')
    show an 66 with dis
    pause
    $ renpy.music.set_volume(0.37, channel='music2')
    show an 65 with dis
    $ renpy.music.set_volume(0.3, channel='music2')
    mc "Oh god, Annie..." with dissolve
    a "Does that feel okay...?"
    mc "It does... C-Come here..."
    scene black
    show annierub0 
    with dis15
    pause
    a "Ahh..." with dis
    mc "You still... good...?"
    a "Yes... But... Now I’m the one feeling a little uncomfortable..."
    a "It’s just, my pants..."
    a "They're rubbing against my..."
    mc "Maybe I can help you this time..."
    mc "Move aside for a second..."
    play soundlow chair1
    scene an 67 with dis
    a "Alright..." with dissolve
    mc "Can I... take off your pants...?"
    a "[mc]... Um, I don’t know if I’m ready to go all the way toni-"
    mc "No, no. Of course. I just want to cuddle a little closer with you..."
    a "Mmm, that does sound nice..."
    mc "I just wanna feel your soft skin..."
    a "*Giggles*"
    a "I’m sorry. I’m just a little nervous because no one has ever touched me there before, or even seen it, for that matter."
    a "Just you."
    mc "I know. If it’s too much all at once, we can just..."
    a "[mc]. I said I’m nervous, but that doesn’t mean I... don’t want to..."
    mc "Uhh—"
    play soundlow chair1
    show an 69
    a "Pants off, right?" with dis12
    a "To... feel more comfortable."
    mc "Y-Yeah. To feel more comfortable."
    a "Alright..."
    play sound chair2
    show an 70 with dis15
    mc "(If this is a dream, please god don’t wake me up now...)" with dissolve
    a "*Giggles* I can't believe I'm doing this. This is a side that I’ve never shown to anyone before..."
    play sound clothes
    show an 71 with dis15
    pause .6
    show an 72 with Dissolve(2)
    mc "Holy..." with dissolve
    show an 73
    a "Oh god... now I feel even more embarrassed..." with dis
    mc "Don’t be. Let me get a better look at you."
    a "B-Better... look...?"
    a "Are you s-sure you..."
    show an 74 with dis12
    mc "I’ve never been more sure, Annie." with dis
    mc "I've wanted you for so long."
    a "R-Really? But..."
    a "I thought you weren’t interested in me..."
    show an 75
    mc "Where did you get that idea from?" with dis
    mc "You're perfect."
    mc "And I’m not just saying that because I’m finally seeing your gorgeous body. You’ve always been perfect to me... inside and out. I just didn’t want to risk ruining our friendship."
    a "W-What? M-Me either!"
    show an 76 with dis
    pause
    show an 77
    a "W-Wait." with hpunch
    show an 78
    a "This is all happening so fast..." with dis
    a "I'm still not ready for anything... in there..."
    a "But I do believe I was promised cuddles...?"
    mc "*Chuckles* You know I’m not one to break my promises."
    play soundlow chair1
    show an 79 with dis12
    mc "*Kissing her neck* And don’t you worry. I’m perfectly fine with going as slow as you want." with dissolve
    mc "Better now? Without those pesky pants?"
    a "Y-Yeah... m-much better. You’re so warm..."
    mc "Do you mind if I move a bit? I want to feel all of you against me..."
    a "Y-Yes..."
    $ renpy.music.set_volume(0.23, channel='music2')
    show annierub5 with dis15
    a "Oh m-my god." with dissolve
    mc "Does that feel good for you too?"
    a "Y-Yes..."
    a "Oh [mc]..."
    mc "You’re... so wet..."
    mc "You like my dick gliding against you like that...?"
    a "Mm-hm..."
    mc "Agh... I need to go faster..."
    a "Please..."
    mc "You sure?"
    a "Yes..."
    scene black
    show annierub3 
    with dis15
    a "AHH..." with dissolve
    a "OH MY..."
    a "Just like that... not too fast, I’m so sensitive right now..."
    mc "Oh Annie..."
    a "Mmmm..."
    mc "(Holy shit, this is really happening! I'm fucking Annie's thighs!)"
    mc "(She feels so amazing...)"
    a "(Ahh... the way he’s grinding against my... mmmm...)"
    a "(I never would’ve thought I’d have a chance with him...)"
    a "Aaaaahh..."
    mc "Jesus, Annie..."
    mc "The way you’re dripping all over my dick..."
    $ annie_points += 1
    play soundlow "beat.ogg"
    show heartr at topleft with dissolve
    hide heartr
    a "[mc]..." with dissolve
    a "You’re making me feel so... so good down there..."
    scene black with dis
    show annierub4 with dis
    mc "AAaaahhh..." with dis
    mc "Yeah..."
    mc "Just like that..."
    a "(Oh my god...)"
    a "(His...)"
    a "(...It's bigger than my arm!)"
    a "(How...)"
    a "(Is that what they’re supposed to look like?!)"
    a "(That thing is supposed to fit inside of me...?)"
    a "(All of it?!)"
    a "(There's no way on Earth I could take all of him.)"
    a "(...Right?)"
    scene black with dis
    play sound chair1
    show annierub2 with dis
    a "Aaaahhh..." with dis
    a "My god..."
    mc "Ahhh... I'm almost there..."
    a "(How can he feel so good? I’m just rubbing against it...)"
    a "(I wonder how he’d feel inside of me...)"
    a "(But no... fitting all that... that’d be impossible...)"
    a "(I'm too small, and he's just... too big...)"
    a "Mmmmhh..."
    mc "Oh Annie..."
    mc "I'm... I’m about to..."
    a "(Well, maybe with a bit of practice...)"
    mc "I’m cumming!!!"
    a "(Together we could...)"
    $ renpy.music.set_volume(0.26, channel='music2')
    play sound cum2
    play sound3 cum1
    scene an 80
    mc "AAaahhh!!" with hpunch
    a "W-What?"
    $ renpy.music.set_volume(0.30, channel='music2')
    play sound2 cum2
    play sound3 cum1
    scene an 80
    mc "Ohhhhhh!!" with hpunch
    show an 81
    a "Oh my god..." with dis15
    mc "Ahhhh...."
    mc "Oh shit, I'm sorry, Annie..."
    a "I..."
    a "Oh god, I gotta go!"
    mc "What?"
    $ renpy.music.set_volume(0.35, channel='music2')
    play sound chair2
    show an 82 with dis15
    mc "Did I do something wrong, Annie? I’m sorry! I didn’t know it was going to be that much!" with dissolve
    show an 83
    a "N-No! It wasn’t that!" with dis
    a "It was amazing!"
    a "B-But then..."
    $ renpy.music.set_volume(0.4, channel='music2')
    show annienervous with Dissolve(1.7)
    a "T-Then you start thinking, Y-Y-YOU KNOW?!" with dissolve
    a "*Nervous giggle*"
    a "L-Like... What j-just happened?!"
    a "AGH! I got carried away, like I ALWAYS DO!"
    a "I only came here t-to sleep and then... next thing I know I’m doing that..."
    a "I mean, I just stuck your... thing... in between my thighs... before I’ve even gotten my first k-kiss!!"
    a "*Nervous giggle*"
    mc "No, no! It's okay! You’re good! I like you, Annie! We can..."
    a "I started m-moving and then I c-couldn't stop and... now I’m not going to have my fairy tale ending... because what kind of Disney princess romance begins with a THIGH JOB?! AHAHAH!!"
    mc "Annie..."
    a "I was looking forward t-to this, b-but didn’t think it’d be like {i}this{/i}!"
    a "*Nervous laughter*"
    a "I mean..."
    mc "(She's not listening to me anymore...)"
    a "We skipped like 14 steps! In one night!"
    a "We didn't even kiss!"
    a "And w-why did it feel so good?"
    a "Why am I naked?"
    a "WHY DOES THIS THING TASTE SO SALTY?!" with hpunch
    a "What will [mc] think of me after all of this?!"
    mc "What? I'm right here! I’ll tell you right now what I think..."
    a "How am I supposed to look at everyone tomorrow?!"
    a "I..."
    a "THINK! I need to think!"
    a "Um..."
    scene an 90 with dissolve
    a "I'm gonna... go... think! Good night [mc]!"
    mc "Good—"
    play music2b rain3
    stop music2
    play soundlow doorslam
    show an 91 with hpunch
    pause .6
    mc "...night." with dis12
    play soundlow chair1
    show an 21
    mc "(Shit, I hope she goes back to her normal self in the morning.)" with dis
    mc "(I'll talk to her. I'll help her overcome her embarrassment... gotta show her that this wasn’t a mistake and it actually meant something.)"
    mc "(I need to help her realize she can let her guard down and be her true self around me.)"
    mc "(After what just happened...)"
    mc "(And the things she said... how she felt...)"
    mc "(Maybe something between us could work after all.)"
    mc "( . . . )"
    mc "(HOLY SHIT! All of that really happened! That was incredible! That was my first time seeing Annie’s secret kinky side... and I loved every moment of it!)" with hpunch
    mc "(Maybe we can both explore it more together...)"
    play soundlow chair1
    show an 4
    mc "(Wow...)" with dis
    stop music2b fadeout 6



label saturdaymorning:
    play music birds fadein 4
    show ag 1 with Dissolve(3.1)
    pause
    show saturday
    mc "*Yawns*" with dis
    mc "(Holy shit! It’s not raining outside?! Maybe I should buy a lotto ticket today...)"
    mc "(I hope it stays like this all weekend.)"
    play sound chair2
    scene ag 2 with dis12
    mc "*Stretching* (Ahh, finally Saturday!!)" with dissolve
    if anniethigh:
        mc "(Man, what happened with Annie last night feels like a dream.)"
        mc "(But it definitely wasn't...)"
        mc "(I should really talk to her about what happened. I hope she isn’t regretting anything...)"
    else:
        if not sendroom and anniepath:
            mct "Oh shit, where's Annie...?"
            mct "I guess she just got up earlier."
            mct "Maybe I should–"
        $ anniepath = False
        $ annieu = False
    play sound2 knock2
    n "*Knocks* [mc]? Are you up?"
    mc "Yeah! Come on in."
    play music2 happy6 fadein 5
    stop music fadeout 8
    play sound3 dooropen1
    $ unlock_look("nancy", 3)
    show ag 3 with dis
    n "Good morning!" with dissolve
    if nancypath:
        mc "(Oh boy...)"
    show ag 5
    mc "Morning, Nancy!" with dis
    show ag 4
    n "See! I remembered to knock this time! I won’t forget after what happened the other day, don't worry." with dissolve
    show ag 5
    if latch:
        mc "It's alright. Were you able to buy a lock for my door?" with dissolve
        show ag 4
        n "Yeah I got it! I'll try to install it tomorrow... if I have time." with dissolve
        show ag 5
        mc "You look sporty." with dissolve
    else:
        mc "*Chuckles* I told you it wasn’t a big deal at all!" with dissolve
        mc "Nice outfit!"
        show ag 4
    if nancypath:
        n "Well thank you! I was just about to head out. Can’t be late for yoga class!" with dissolve
        n "Are you still planning on joining me?"
        show ag 5
        mc "Of course!" with dissolve
        show ag 4
        n "Cool! I'll see you at the gym then." with dissolve
        show ag 5
        mc "Huh? We're not going together?" with dissolve
        show ag 6
        n "Sorry but I’m in a bit of a rush. I have to leave now because I’m picking up a friend along the way." with dis
        show ag 8
        mc "A friend?" with dissolve
        show ag 6
        n "Yeah, she’s the mom of your classmate, Jamie. Do you know him? " with dissolve
        show ag 8
        mc "Hmmm... No, I don't think I've met him before." with dissolve
        show ag 7
        n "Well... to be honest, calling her a \"friend\" is a little bit of a stretch." with dis08
        n "She joined the yoga class after discovering I was going there, too."
        n "Just between you and me, I think she's a bit annoying, but I don't want to get on her bad side since she's a coworker and also happens to be the school’s PTA president."
        show ag 8
        mc "Hey, I don't blame her. She probably thought yoga was the secret to your eternal youth." with dis08
        show ag 6
        n "*Giggles* Oh, stop..." with dissolve
        if daliapath:
            n "Anyway, can you go wake up Dalia for me?"
            n "I have to start the laundry and prepare everyone a quick breakfast before I go. I'll leave the food on the kitchen counter."
            show ag 8 with dissolve
            menu:
                with dis
                "[gr]Offer to make breakfast":
                    mc "Nonsense! You’re in a rush... leave the chores to me." with dissolve
                    mc "If you don’t mind waking up Dalia, I’ll take care of the rest."
                    $ nancy_points += 1
                    play sound "beat.ogg"
                    show ag 9
                    show heartr at topleft
                    with dis
                    hide heartr
                    n "What have I done to deserve such chivalry?" with dissolve
                    mc "What can I say, I'm a real catch."
                    n "*Laughs* It definitely looks like it..."
                    n "Alright then, I'll see you at the gym in a few!"
                    mc "Sure! See you then!"
                    play sound doorclose
                    show ag 2 with dis15
                    mc "(Hmmm... What should I prepare for breakfast? Knowing Dalia... that girl can {i}eat{/i}!)" with dissolve
                    mc "(Some toast with a glass of milk won't be enough, that's for sure.)"
                    mc "(Pancakes, maybe?)"
                    mc "(I'm no Gordon Ramsay, but I think I can pull it off.)"
                "Go wake up Dalia":
                    $ dalia987 = True
                    $ dalia_points += 1
                    mc "Sure thing. Would you mind preparing me a bagel with cream cheese?" with dissolve
                    show ag 6
                    n "Of course! No problem."
                    n "I'll see you at the gym then!"
                    show ag 8
                    mc "Okay! See you later!"
                    play sound doorclose
                    show ag 2 with dis15
                    mc "(Dalia and I are supposed to work out together after yoga.)" with dissolve
                    mc "(If I remember correctly, I think they both go to the same gym.)"
                    mc "(Hmmm... I should ask her if she wants to come with me or if she's gonna come later.)"
        else:
            show ag 9
            n "Anyway, I'll go wake up Dalia. I'll see you at the gym in 40 minutes!" with dis
            mc "I'll be there!"
            $ nancy_points += 1
            play sound doorclose
            show ag 2 with dis15
            mc "(Well, let's see how Kredon's gym looks.)" with dissolve
            mc "(Man, I feel so invigorated today!)"
            mc "(Let's go!)"
            stop music2 fadeout 3
            show b with Dissolve(2.5)
            pause
            show screen afewhourslater with dis12
            pause
            jump nancygym
    else:
        n "I'm going to my yoga class."
        show ag 5
        mc "Oh, yeah, true."
        show ag 4
        if daliapath:
            $ dalia987 = True
            n "Anyway, can you go wake up Dalia? I really have to go now."
            mc "Sure, no problem."
            n "Thank you!"
            $ dalia_points += 1
            play sound doorclose
            show ag 2 with dis15
            mc "(I should prepare breakfast for Dalia one of these days. Although knowing her... that girl can {i}eat{/i}!)" with dissolve
            mc "(Some toast with a glass of milk won't be enough, that's for sure.)"
            mc "(Pancakes, maybe?)"
            mc "(I'm no Gordon Ramsay, but I might be able to pull something off.)"
        else:
            n "Penelope and Annie have left already and Dalia is getting ready for the gym, so I’m leaving you in charge of the house."
            show ag 5
            mc "I'll keep the house safe, don't worry!"
            show ag 4
            n "Alright then. Call me if you need anything. See you later."
            show ag 5
            mc "Bye!"
            play sound doorclose
            show ag 2 with dis15
            mc "(Well, I don't have anything to do until the afternoon.)" with dissolve
            mc "(I have to meet up with Alex to work on homework at 4:00 PM.)"
            mc "(But for now, I'll go take a shower and then enjoy a lazy morning on the couch.)"
            mc "(I deserve some rest!)"
            stop music2 fadeout 3
            jump alexhouse
    play music birds fadein 3
    stop music2 fadeout 6
    show ag 10 with Dissolve(2.8)
    $ unlock_look("dalia", 3)
    d "Zzzzz..." with dis
    if dalia987:
        show ag 13
        mc "Dalia? Good morning!" with dis
        d "Zzzzz..."
        mc "Dalia?"
        show ag 14 with dis15
        mc "(She must be in some deep sleep. And Carolyn looks like she’s happily off in dream land too!)" with dissolve
        mc "(Oh my god, this is adorable. I almost feel bad for waking her up.)"
        mc "(I should probably be as gentle as I can...)"
        show ag 15
        mc "Psst." with dis12
        mc "*Whispering* Dalia."
        mc "*Whispering* Daaaaliaa..."
        mc "*Whispering* Wake up, Sleeping Beauty..."
        show ag 16
        d "Hhmm..." with dis12
        mc "*Whispering* Dalia..."
        show ag 17
        d "Mmm..." with dis
        d "(Huh?)"
        play sound horrorsound fadein 1.5
        show ag 18 with dis15
        pause 1.5
        play sound punch
        stop music
        play music2 happy5 fadein 4
        show ag 19
        d "W-WHAT THE FUCK?!" with hpunch
        mc "Ouch..."
        d "The fuck is wrong with you?!"
        d "How long have you been watching me sleep, you fucking lunatic?!"
        play sound2 chair1
        show ag 33 with dis
        mc "I just got here, shit! Nancy told me to wake you up! Why did you hit me?!" with dissolve
        show ag 34
        d "W-Well, you scared me."with dissolve
        d "First thing I saw when I opened my eyes was you staring at me like a psycho!"
        show ag 33
        mc "Damn, what a kick..." with dissolve
        show ag 32
        d "Anyway, what's the rush?" with dissolve
        d "It's Saturday... it’s supposed to be the day we can actually sleep in for once!"
    else:
        show ag 11
        n "Dalia!" with dis
        n "Good morning, honey!"
        n "Come on now, it’s time to get up!"
        show ag 10
        d "Hhmm..." with dis
        show ag 11
        n "Dalia... You wanted me to wake you up..." with dis
        show ag 10
        d "Mm-hhmmm..." with dis
        show ag 11
        n "Come on Dalia, I have to go to yoga!" with dis
        n "Don’t make me do this the hard way!"
        show ag 10
        d "Hhhmm..." with dis
        play soundlow chair1
        play music2 tictoc fadein 1
        show ag 12
        d "Zzzzz..." with dis15
        n ". . ."
        d "Zzzzzzz..."
        n ". . ."
        stop music fadeout .2
        stop music2 fadeout .2
        play sound alarmclock
        play sound2 chair1
        show ag 20
        d "EEERGH! W-WHAT?! WHO?! WHERE?!! {w=0.25}{nw}" with hpunch
        play sound3 cathiss
        d "EEERGH! W-WHAT?! WHO?! WHERE?!! {w=0.25}{nw}" with hpunch
        d "EEERGH! W-WHAT?! WHO?! WHERE?!! {w=0.25}{nw}" with hpunch
        d "EEERGH! W-WHAT?! WHO?! WHERE?!! {w=0.25}{nw}" with hpunch
        d "EEERGH! W-WHAT?! WHO?! WHERE?!! {w=0.25}{nw}" with hpunch
        d "EEERGH! W-WHAT?! WHO?! WHERE?!! " with hpunch
        play sound2 chair1
        show ag 21 with dis15
        play music2 happy5 fadein 4
        d "Aghh... Why’d you have to do that..." with dis
        d "It's Saturday!"
        show ag 22
        n "You asked me to wake you up, remember?"
        show ag 21
        d "*Yawns* Well, I take it back."
        show ag 22
        n "Come on, it's 9:20 already."
        n "If you waste away your morning, you’re going to regret it later."
        n "And then you'll be in a bad mood all day!"
        show ag 21
        d "No I won’t..."
        show ag 22
        n "I don't even understand how you can sleep so much! You were the first to go to bed and now you’re the last to get up. You've slept for like... 10 hours?"
        show ag 21
        d "Because I work out a lot... and my... *yawns* body needs its recovery."
        show ag 22
        n "Well, you've recovered enough. Come on now, let’s get you up."
        show ag 21
        d "Mommmm..."
        show ag 22
        n "Now, now... don't \"Mommmm\" me."
        show ag 21
        d "Mmmmph..."
        d "Okay, okay... fine, I'm getting up..."
        show ag 22
        n "You better be!"
        show ag 23
        n "Otherwise, Miss Carolyn will come and tell me, won’t you sweetie?" with dis
        play soundlow purr2 fadein .5
        carol "*Purring*"
        n "That's right, you're such a good girl, you know that??"
        n "Unlike Sleeping Beauty over here, you can sleep as much as you want!"
        n "You deserve it for being so cute!"
        play sound chair4
        show ag 24
        n "Okay, I really have to leave now. I'll see you later, honey." with dis12
        n "Don't you fall back asleep!"
        d "I won't..."
        n "Bye Carolyn!"
        play sound cat
        carol "*Meows*"
        show ag 26 with Dissolve(2)
        pause
        play sound2 knock2
        mc "Dalia? Are you up?" with dis
        d "Arghh... Just when I thought my morning couldn’t get {i}any{/i} better..."
        show ag 27
        d "Yeah, yeah, I'm awake." with dis
        d "Tell Mom I'll be at the gym in 5 minutes."
        play sound chair1
        show ag 28
        mc "I think she left already." with dis
        d "Oh... Good."
        d "Guess I can sleep a couple more hours then..."
        mc "You sure about that? I made you breakfast..."
        show ag 29
        mc "Pancakes!" with dis
        mc "Well, considering how much you eat... it'll probably just be your first round of breakfast, but anyway..."
        d "...what? Did you say... pancakes...?"
        play sound sniff
        d "*Sniffs*"
        play sound2 chair3
        show ag 30
        d "PANCAKES!! YAY!!" with dis
        d "Are they all for me?"
        mc "Yep!"
        play sound3 chew
        show ag 31 with Dissolve(2.2)
        d "Mmmmm!" with dissolve
        mc "My god! You devoured that thing in like 10 seconds! How on earth..."
        mc "You sure have quite the appetite."
        d "What can I say... I love eating, sleeping, and working out. The foundation of a good life!"
        mc "*Laughs* Fair enough."
        $ dalia_points += 1
        play sound "beat.ogg"
        show heartr at topleft with dissolve
        hide heartr
        d "I gotta say, those were some damn good pancakes. Thank you, [mc]."with dissolve
        mc "Don't mention it."
        play soundlow chair1
        show ag 33
        mc "You know, I almost didn’t recognize you without your braids and bangs covering your eye." with dis
        show ag 34
        d "Yeah, well, I haven't done my hair and makeup yet... and I just woke up! I don't know what you were expecting."with dissolve
        d "I'd like to see your bed head first thing in the morning!"
        show ag 33
        mc "Hey, I didn’t say you looked ugly! On the contrary, I actually think you look really lovely right now..."with dissolve
        mc "(And can’t help but notice that lovely view of sideboob... mmm!)"
        mc "(No [mc]! Must... maintain... eye contact...)"
        show ag 35
        d "Y-Yeah, sure, if you say so..." with dissolve
        d "Thank you for the lie... as flattering as it is."
        show ag 32
        d "Anyway, what's the rush with you and Mom trying to get me up?" with dissolve
        d "Are we supposed to be somewhere, or something?"
    show ag 33
    mc "I thought we were going to train together today." with dissolve
    show ag 36
    d "Oh, yeah! Of course!" with dis
    d "How could I forget!"
    d "Today you're gonna learn what a {i}real{/i} workout feels like."
    mc "Hmmm... I'm not so sure about that, Dalia. I've seen broom sticks thicker than your biceps."
    show ag 37
    d "Haa... haaa..." with dissolve
    d "You’re one to talk! Your abs are only visible because you're skinny. It’s like a fat girl bragging about having boobs. It’s cheating!"
    d "It’s not my fault, women just have a tougher time building upper body strength."
    d "My real strength lies in my lower body!"
    mc "I don’t doubt you there..."
    show ag 36
    d "I can squat 285 lbs!" with dissolve
    d "And I'll show you today!"
    if nancypath:
        mc "Well alright then, I’ll hold you to it! First I'm going to yoga class with Nancy, though."
        d "Ha! Sure, go ahead. You look about as flexible as a log."
        d "I still don’t think it’s very wise of you though. Gonna exhaust yourself before the true workout begins? I’ll get the wheelchair ready..."
    play soundlow chair1
    play sound dodge
    show daliaswipe
    d "*Jumping out of bed* Come on, let's get going then!"
    stop music2
    play sound2 chair3
    scene ag 39 with dissolve
    pause
    play sound backbreak
    scene ag 40
    pause .05
    scene ag 39
    pause .05
    scene ag 40
    pause .05
    scene ag 39
    pause .05
    scene ag 40
    pause
    play soundlow cat
    carol "*Meows*" with dis12
    mc "Um..."
    mc "A-Are you okay, Dalia?"
    play sound chair1
    show ag 41 with hpunch
    mc "D-Dalia?!" with dis
    play music2 sad1
    d "{size=20}My back..."
    mc "What?!"
    d "MY BACK!!!" with hpunch
    d "I think I just tweaked it... I c-can't move."
    mc "Oh shit!"
    mc "Should I call an ambulance?"
    d "No... this has happened to me before. I must’ve lifted too much weight yesterday..."
    d "It'll heal with rest, but now I’ll be out of the gym for at least a week!!"
    mc "Oh... Thank god, I thought it was more serious."
    show ag 42
    d "Don't you understand?!" with dis
    d "The weightlifting competition is less than two weeks away!"
    d "Even if I'm healed by then, I can't afford to miss out on a whole week of training!"
    d "Not after all the progress I’ve made this entire year!"
    d "Micaela will humiliate me again! And everyone is just gonna laugh at me!"
    d "I'll be Kredon's biggest loser yet again!"
    show ag 41
    d "I'm a miserable mess..." with dis
    mc "Come on, come on... don’t talk like that! It's no big deal."
    mc "Can you sit up? Let me help you."
    stop music2 fadeout 3
    play sound chair1
    show ag 43 with dis15
    play music2b happy5 fadein 4
    mc "Why don’t I give you a massage. I am known to be quite the massaging miracle maker!" with dissolve
    mc "I remember when Chang hurt his back pretty bad when he tried to climb onto the roof of our school a few years ago."
    mc "After that incident, I watched a Cambodian masseur on YouTube and learned how to give massages for muscle injury relief. He was back to normal in no time!"
    show ag 44
    d "How romantic..." with dissolve
    d "Well I hope you know what you're doing."
    show ag 43
    mc "I do. Just trust me." with dissolve
    mc "But first, I need you to relax your muscles a bit. Try thinking about something else."
    show ag 44
    d "Thinking? About what?" with dissolve
    show ag 43
    mc "I don't know. Did you get to play Eternum last night?" with dissolve
    show ag 44
    d "Yeah, I did for a little while, but I didn't find anything good." with dissolve
    d "How about you?"
    show ag 43
    if anniehorror:
        mc "I played with Annie and Luna. We ended up finding something that could be... pretty important. But we’re not sure yet." with dissolve
    else:
        mc "I played with Luna and we ended up finding something that could be... pretty important. But we’re not sure yet." with dissolve
    show ag 44
    d "What? What’d you find?" with dissolve
    show ag 43
    mc "I'll show you when we play together next time." with dissolve
    mc "It'll be a surprise!"
    show ag 44
    d "Bahh..." with dissolve
    show ag 43
    mc "Speaking of Eternum, have you heard anything from Jerry?" with dissolve
    show ag 44
    d "Ah, yeah, he continues to text me every day..." with dissolve
    d "He ended up losing his level and entire inventory. I tried to explain that you and I couldn't recover his stuff because we ran into Thanatos, but he doesn't believe me."
    d "He's convinced that you killed him with some dirty trick."
    show ag 43
    mc "Nonsense. The ogre killed him." with dissolve
    show ag 44
    d "That's what I told him, but he didn't see any ogre." with dissolve
    show ag 43
    mc "Well yeah, probably because he pretty much got insta-killed." with dissolve
    show ag 45
    mc "Poor Jerry. Well, I hope he’s able to rebuild his account soon..." with dis08
    mc "He seemed nice. I feel so bad for him..."
    show ag 44
    d "He’s definitely a bit of a pain sometimes, but I will admit he is a good spell caster." with dis08
    d "I think he’ll be able to recover pretty quickly."
    show ag 43
    mc "Well, I think we're just about done here. Feel any better?" with dissolve
    play sound clothes
    show ag 46 with dis12
    d "Hey... y-yeah, actually! I do feel a bit better!" with dissolve
    d "Not bad, Mr. Magic Hands!"
    play sound2 chair4
    show ag 48
    mc "I’m going to grab you an ice pack real quick. Just leave that on your back and get some REST!" with dis12
    mc "Lie down, watch TV, play some Eternum... whatever you prefer."
    mc "I’m going to give you another massage tomorrow. We have to continue working your muscles."
    mc "If you listen to me and don’t try to sneak off for a secret workout, you'll be recovered before next Friday. And you’ll be stronger than ever!"
    show ag 47
    d "Okay, I trust you." with dissolve
    d "Thank you, [mc]."
    show ag 48
    mc "Anytime, Dalia." with dissolve
    if anniethigh:
        play sound dooropen1
        pause .5
        show ag 50
        d "Annie!" with dis12
        d "Good morning!"
        show ag 51
        a "D-D-D-Dalia! M-Morning!" with dis15
        mc "Annie! Do you have a minute? I wanted to talk to you!"
        a "M-M-Me? I c-c-can't! I h-have to..."
        a "Um..."
        a "You know..."
        a "*Nervously giggles* I'm late for... I gotta be at the..."
        play sound run
        show ag 52
        a "*Runs away*" with dis15
        d "Hmm?"
        show ag 53
        d "That was weird." with dis12
        d "She seemed... more shy than usual."
        mc "Y-Yeah, maybe she had a rough night or something."
        mc "(Hmph. She probably needs more time. I’ll try to talk to her again tomorrow...)"
    show ag 47
    if nancypath:
        d "Anyway, you're going with Mom to that yoga thing, right?" with dis
        show ag 48
        mc "Yep!" with dissolve
        mc "I should actually get going now or else I’ll be late."
        show ag 47
        d "Okay then, well have fun." with dissolve
    else:
        d "Anyway, do you have any plans for today?"with dis
        show ag 48
        mc "Not really. I’m going to meet with Alex this afternoon to work on our project, but until then, I'm just going to spend the morning chilling around the house." with dissolve
        show ag 47
        d "Sounds like a good plan." with dissolve
    d "Our training has obviously been postponed, but only until I’m back in action next week! Don't think you're getting off the hook that easily!"
    show ag 48
    mc "*Laughs* Of course not. I'm looking forward to it!"with dissolve
    show ag 47
    d "See you later!" with dissolve
    show ag 48
    mc "Bye! And try to take it easy!"with dissolve
    if nancypath:
        stop music2b fadeout 3
        show b with Dissolve(2.5)
        pause
        show screen afewminuteslater with dis12
        pause
        jump nancygym
    else:
        jump alexhouse



label nancygym:
    play music2 gym fadein 3
    scene ag 54
    hide screen afewhourslater
    hide screen afewminuteslater
    with Dissolve(3)
    mc "(Alright... Kredon's gym.)" with dis
    mc "(Man, there’s a lot of fit, good-looking people here.)"
    mc "(And not a single person I recognize.)"
    mc "(I probably look so out of place right now...)"
    n "Hey there, handsome."
    show ag 55
    mc "*Turning around* Oh Nancy, thank god!" with dis08
    mc "Man, I hate being the new guy at places."
    mc "I was starting to feel a little insecure around all these beautiful people."
    show ag 56
    n "*Chuckles* What are you talking about?"
    n "I think you’re better looking than anyone else here."
    show ag 55
    mc "You’re just saying that because you feel sorry for me."
    show ag 56
    n "*Giggles* That's not true at all! I meant what I said."
    show ag 55
    mc "Yeah, that’s just your maternal instinct. It’s like when a mom says that her son is the most beautiful baby in the world, even though it looks like E.T."
    show ag 56
    n "*Laughs* I don't think that's it at all..."
    show ag 54
    mc "*Chuckles* So... This is the gym where you and Dalia usually go, huh?" with dis12
    mc "It looks so modern."
    show ag 56
    n "Yeah, they just opened a few years ago." with dis08
    n "The things I love most about this place are the personal training sessions and variety of activities available."
    n "There's something for everyone."
    n "I know I wouldn’t be able to keep up with someone like Dalia in the weight room, but luckily they’ve got other activities like yoga and kickboxing that are right up my alley."
    show ag 55
    mc "Are you kidding me?! You kickbox? I didn't know that!"
    show ag 56
    n "Oh, there's a lot you don't know about me, [mc]..."
    show ag 57
    n "Come on, let's head over to the front desk!" with dis
    n "We'll get you registered as a member so you can come whenever you want."
    mc "Sounds good!"
    show ag 58 with Dissolve(1.5)
    n "Good morning, Millie!" with dissolve
    mil "Whoa, whoa, whoa! Mama-mia! The hottest Mom in Kredon has arrived!"
    n "Oh, you’re just too much!"
    mil "How are you, cutie?"
    n "All good, thanks! And you?"
    mil "Meh, you know. Living the dream. Behind this desk. Like always..."
    mil "It’s Saturday... so you’re here for your yoga session, right?"
    n "Yeah, but I brought someone with me today."
    mil "Oh, nice! Finally got yourself a hot boyfriend like I told you, huh? Pack it up gents, she’s off the market!!"
    show ag 59
    n "*Laughs* It's not that. [mc] is staying with us for a year until he finishes school. He’s part of the student exchange program." with dis
    mc "Well, I’m hoping I get accepted into Kredon’s college for next year. If I can manage that, I would love to stay here."
    n "Oh, trying to stay with us indefinitely, I see?"
    mc "Just until Dalia realizes that I'm eating her peanut-butter cookies."
    n "*Laughs* Oh, you're so dead!"
    show ag 61
    mil "Well, well, well, [mc]!" with dis
    mil "If you’ve come to get stronger, shed those peanut-butter cookie pounds, or become the best trapeze artist in North America—you've come to the right place!"
    mil "You can do it all here at {i}PUMP IT{/i}!"
    mil "We’ve got so many dumbbells, locker rooms with good smells, a coach who gently yells, and plenty of fit bombshells! Don’t believe me? Check our membership count—this place sells!"
    mil "All for the low cost of $36 a month! That’s like $1.16 a day!"
    show ag 60
    mc "*Laughs* Alright, alright! You got me. I’m sold!"
    show ag 61
    mil "Awesome! Since you’re signing up today, you can join any of the activities that we have scheduled for this beautiful Saturday morning!"
    show ag 60
    mc "Yeah, I think I was going to try out the yog-"
    show ag 61
    mil "AH, AH, AH! First, let me introduce you to our personal trainers!"
    show ag 60
    mc "Um... alright, go ahead."
    show ag 61
    mil "We’ve got four of them and they’re all amazing!"
    play soundlow whoosh2
    show gym1
    mil "Are you looking for swimming lessons? Want to step up your water polo game? Learn how to high dive? Directly from Yekaterinburg, I present to you... Nikolay!"
    mil "As Nikolay always says..."
    play sound metalhit
    show ag 63
    hide gym1
    niko "Границы России нигде не заканчиваются." with hpunch
    mc "W-What?"
    play soundlow whoosh2
    show gym2
    mil "Want to learn self-defense? Brazilian Jiu-Jitsu? How to deliver a roundhouse kick to the face?? Moon is your girl!"
    mil "As Moon always says..."
    play sound metalhit
    show ag 65
    hide gym2
    moon "I have to go. See you Monday." with hpunch
    play soundlow whoosh2
    show gym3
    mil "Are you interested in..."
    play soundlow whoosh2
    scene gym3b
    mil "Wait, what?! That's not a slogan, Moon!"
    mil "Come on, I told you to come up with a slogan!"
    hide gym3b
    show ag 65
    moon "I know, I was just letting you know I was leaving." with dissolve
    show ag 65b
    mil "But you just got here!"
    show ag 65
    moon "Someone called me. It's... something important."
    show ag 65b
    mil "Have you told the boss?"
    show ag 65
    moon "No. But I'm sure he won't find out, as long as you don’t say anything."
    show ag 64
    moon "See you Monday, Millie." with dis08
    mil "AAAAH! OKAY, OKAY!"
    mil "Okay, forget about the combat classes, [mc]."
    mil "*Clears throat* Where was I..."
    play soundlow whoosh2
    scene gym3
    mil "Are you interested in cleansing your soul, while also increasing your flexibility? Do you want to become one with the universe?! Kai is your man!"
    mil "As Kai always says..."
    play sound metalhit
    show ag 67
    hide gym2
    kai "It doesn’t matter how deep into a pose you go – what does matter is who you are when you get there." with hpunch
    play soundlow whoosh2
    scene gym4
    mil "Do you want to finally fill out the sleeves of that extra-small T-shirt of yours? Improve your endurance and stamina? Look no further than Chang!"
    mc "W-What?"
    mil "As Chang always says..."
    play sound metalhit
    show ag 69
    hide gym2
    c "It doesn’t matter how deep into a squat you go – what does matter is who you are when you get there." with hpunch
    play sound2 slam
    show ag 70
    kai "HEY! This motherfucker stole my slogan!" with hpunch
    c "What! I did not! Mine is totally different!"
    kai "Don't play dumb with me!" with hpunch
    scene ag 60 with dis15
    mc "H-How... When..." with dissolve
    mc "Why..."
    mc "You know what, forget it. I’m not even going to ask."
    mc "Yeah, I think I’ll just be off to that yoga class... with Nancy."
    show ag 61
    mil "Oh awesome! You should’ve said something earlier! Alright, I'll fill out your membership form!"
    mil "Hope you enjoy your time here at... {i}PUMP IT{/i}!!"
    show ag 60
    mc "Thank you!"
    show ag 71
    n "I’m going to drop off my bag in the locker room." with dis12
    n "I'll meet you in the yoga room. It’s on the second floor."
    show ag 72
    mc "Alright! I'll see you there." with dis
    mc "I just need to talk to... someone for a minute... then I'll be right up."
    scene ag 73 with Dissolve(2.1)
    c "Come on, Shiro!" with dissolve
    c "You need to go faster, don't stop now! Imagine there’s a donut in front of you! GET. THAT. DONUT!!"
    c "Go, go, go!"
    shiro "Yes, sensei!"
    mc "Um... C-Chang?"
    show ag 74
    c "Huh?" with dis
    show ag 75
    c "[mc]!" with dis
    c "You truly have a gift for showing up at the most unexpected times!"
    show ag 76
    mc "I should be the one telling you that!" with hpunch
    mc "Personal trainer? Strength coach? What the hell?"
    show ag 75
    c "Yeah, well, I mainly came here hoping to see Micaela. And maybe get in shape too, you know..." with dissolve
    c "The receptionist told me they were looking to hire personal trainers, and I guess I got a bit carried away when she asked me about my fitness skills."
    c "She ended up offering me a job and... what do you know, here I am!"
    show ag 76
    mc "I... *Laughs* I don't know what to say, man. Congrats, I guess." with dissolve
    show ag 75
    c "Thanks, buddy." with dissolve
    show ag 76
    mc "What the fuck is that shirt, though?" with dissolve
    show ag 75
    c "Fits me just right, huh?" with dissolve
    c "I accidentally spilled Big Mac sauce on my shirt, so I needed to change. Ended up finding some fresh clothes in the employee break room."
    show ag 76
    mc "Um..." with dissolve
    mc "It says... \"breed me\" on the back."
    show ag 75
    c "*Laughs* Now that would be hilarious!" with dissolve
    show ag 76
    mc "No, no, seriously, it says that." with dissolve
    show ag 77
    c "Wait, what?" with dis
    mc "And it has a silhouette of a pregnant woman."
    c "What?"
    c "Oh shit..."
    c "Do you think that's why the Sauna Sweaty Lovers Club said to join them when I get off shift?"
    mc "Um... it's a possibility."
    c "Fuck, I gotta go."
    show ag 78
    c "Thanks for the heads up, man." with dis12
    c "You're my savior."
    show ag 78b
    mc "*Laughs* Any time, bro." with dissolve
    mc "And I think you should keep this job!"
    mc "You'll make Micaela fall in love with you. I believe in you!"
    show ag 80
    c "Oh, yeah, now that you mention it... I wanted to ask you something." with dis
    show ag 79
    mc "Shoot."
    show ag 80
    c "Micaela's birthday is next week."
    c "I thought of getting her something special, but I’m not quite sure what yet."
    c "Do you have any idea?"
    c "Please! My future family of 13 is in your hands!"
    show ag 79
    mc "Hmm..."
    default micaflower = False
    default micadumbbell = False
    default micatickets = False
    menu:
        with dis
        "Flowers":
            $ micaflower = True
            mc "The girls who look the toughest on the outside are always the sweetest on the inside." with dis08
            mc "Get her a bouquet of flowers. Trust me, it never fails. It’s a classic for a reason."
        "A dumbbell":
            $ micadumbbell = True
            mc "She obviously is very passionate about fitness. You should get her something related to that hobby." with dis08
            mc "Maybe get her a dumbbell or something similar. Trust me, she'll love it."
        "[gr]A ticket to a show":
            $ micatickets = True
            mc "Is she a fan of any particular band or comedian? Get her a ticket to a show that you know she’ll enjoy." with dis08
            mc "You can show her that you pay attention to what she likes. Then boom, you {i}somehow{/i} have an extra ticket for yourself too, so then you end up joining her! A gift and a date! Two birds with one stone, baby."
        "Nothing":
            mc "Girls don't like men that chase. It looks desperate and needy." with dis08
            mc "Don't get her anything. Act tough, hold your ground, and then just wait. She’ll come crawling to you in no time, trust me."
    show ag 78
    c "Ah, you're the best, man!" with dis08
    c "I owe you one! Thank you!"
    show ag 78b
    mc "Anytime!" with dissolve
    show ag 78
    c "Alright, I think it’s about time I changed out of this shirt. I'll text you later!" with dissolve
    show ag 78b
    mc "Sure thing, take care!"with dissolve
    show ag 81 with Dissolve(1.5)
    mc "(I hope I've given him good advice.)" with dissolve
    mc "(Well, time will tell.)"
    mc "(Time for some yoga!)"
    show ag 82 with Dissolve(2.2)
    mc "(Oh... They have a nice spot up here.)" with dissolve
    show ag 83 with dis12
    mc "(Who do we have here...)" with dissolve
    show ag 84 with dis12
    mc "Oh... So this is yoga. It looks pretty intense!" with dis
    mc "Mind if I join you in your little nap session?"
    show ag 85
    n "I'm just stretching out the hammies, silly." with dis08
    n "And you should do it too if you want to save yourself from some embarrassment later."
    mc "*Chuckles* I think I can handle a little bit of yoga. Grandmas do this stuff all the time, don’t they?"
    show ag 87 with dis
    n "I admire your cockiness. Hold onto it while you can... you’re about to be humbled very soon." with dissolve
    show ag 86
    mc "*Laughs* What? Is this a competitive sport now?"with dissolve
    mc "I thought yoga was about finding balance in one’s mind, body, and soul..."
    show ag 87
    n "Life is always some sort of a competition, [mc]. If not against others, then against yourself." with dissolve
    n "But if this isn't enough for you... I can also kick your ass at kickboxing when we’re done here."
    show ag 86
    mc "*Laughs* I'm sure you would. Maybe another day, I can’t risk bruising this handsome face."with dissolve
    show ag 87
    n "Ahh... Smart!" with dissolve
    show ag 88
    n "*Laughs* But seriously, all joking aside, you should really stretch out a little bit." with dis12
    n "It'll help with the elasticity of your muscles."
    n "And it will also prevent injuries."
    mc "*Stretching out* You're not wrong there."
    show ag 89
    n "Ah, looks like more people are starting to arrive." with dis
    n "I guess not many people signed up today, so at least we’ll have plenty of space to ourselves."
    show ag 90
    n "Hopefully it'll only be 5 or 6 people." with dis
    mc "Hey! I know those guys!"
    n "Oh, you've met Noah and Raul? You’ll come to see that Kredon is a lot smaller than it looks, so I’m sure you’ll cross paths with familiar faces all the time."
    mc "Yeah, I know them from school."
    n "I didn't know they were teachers! How nice!"
    mc "Um... Well, no, they're actually students. They share a couple classes with me and Dalia."
    n "W-What?"
    show ag 91
    rau "Hmm?" with dis08
    show ag 92 with Dissolve(.7)
    show ag 91
    rau "M'lady." with dis08
    rau "[mc]."
    show ag 93
    mc "'Sup man! Good to see you." (multiple=2) with dis
    n "Hey Raul! Good morning!" (multiple=2)
    show ag 94
    n "Well, regardless, they're both really nice." with dis
    n "And they always seem to be together! Like two peas in a pod."
    show ag 95
    mc "Yeah, they’re the same way at school. I've never seen one without the other." with dissolve
    mc "*Laughs* I think our teacher is scared of them."
    show ag 94
    n "Really?" with dissolve
    n "That's silly. They might look intimidating at first, but you just need to talk to them and then you’ll realize they're so sweet."
    n "I guess you could say that they’re..."
    play sound whoosh3b
    show ag 96
    ger "Heyyyyy giiiiiirl!" with hpunch
    ger "I was looking for you in the locker room, Nan!"
    ger "After I came out of the bathroom, you disappeared! Where did you run off to?"
    show ag 97
    n "H-Hey there. Sorry, I had to uhh... refill my water bottle... gotta stay hydrated, you know..." with dissolve
    n "This is my... friend... Gertrude."
    n "Gertrude, this is..."
    show ag 98
    ger "Ohhh, am I finally getting to meet Dalia?!" with dissolve
    show ag 96
    ger "*Whispers loudly* I always thought that Dalia was a girl..." with dissolve
    show ag 99
    mc "What? I'm not Dalia. My name is [mc]." with dissolve
    show ag 98
    ger "Mmm, fancy yourself a yoga session, huh Dalia?"with dissolve
    ger "Did you know that your mother and I are known as the \"Forever Young Ladies\" at this gym?"
    show ag 99
    mc "Like I said, I’m not Dalia..."with dissolve
    show ag 97
    n "Yeah, well, I'm honestly not sure if anyone really calls us that."with dissolve
    mc "(If someone does, I don’t think they were applying that nickname to Gertrude...)"
    show ag 98
    ger "Everyone does! All the time! I'm even starting to hear it at work and during our PTA meetings." with dissolve
    ger "*Hearty laugh* Because... well, I don't like to brag, but... I’ll have you know I'm the president of Kredon's School PTA."
    ger "*Grinning cheekily* That’s right... {b}{i}the{/i}{/b} PTA."
    mc "(I can’t give her the satisfaction...)"
    show ag 99
    mc "PTA? Never heard of it. Is that like the... Pakistan Telecommunication Authority or something?" with dissolve
    show ag 96
    ger "You know, maybe Nancy would also hear more compliments if she ever left her lab!" with dissolve
    show ag 97
    n "Well, the most recent Ulysses contract has been keeping me very busy, you know." with dissolve
    show ag 99
    mc "Ulysses? Eternum's parent company? I thought you worked in the research field." with dissolve
    show ag 97
    n "I do! They actually hired us to conduct a stem cell study a few weeks ago. I guess when you’re the largest conglomerate on the planet, you become involved in many sectors." with dissolve
    n "I heard they're also planning to get into the narcotics industry soon."
    show ag 99
    mc "Damn... technology, entertainment, banking... and now science too? These people have their hands in everything!" with dissolve
    show ag 97
    n "But... if you're wondering if I can get a free neural implant as a perk of the job, I can't. We're just one of hundreds of subcontracts they have." with dissolve
    play sound musicstop
    stop music2
    show ag 100 with hpunch
    pause
    play sound plugin
    play music2b yoga fadein 2
    kai "*Turning on the speaker*" with dis
    show ag 101
    kai "*Taking a deep breath*" with dis12
    kai "*Exhaling slowly*"
    show ag 102
    kai "Welcome, my cherished students." with dis
    kai "Nothing brightens up my life more than seeing each of your dreamy faces."
    kai "I don’t know where life has taken you this week, but rest assured, you’ve now arrived at the destination where you ultimately belong. Yoga with Kai."
    kai "Let us take a minute to reflect on our previous journeys, and then ready our minds for purification... and prepare our bodies to be relieved from the stress of this cruel world."
    kai "As soon as I walked into this room, I sensed new auras. And now I know why, as I see some new faces. Welcome, my children."
    kai "I’m so pleased to see some familiar ones too, though. Good to see you again, Raul, Noah, Gertrude..."
    show ag 103
    kai "*Kissing her hand*" with Dissolve(1.4)
    show ag 104
    kai "And of course... my beautiful little dove, Nancy." with dis
    n "Um... Thanks, Kai. You're always so flattering."
    kai "Flattery...? No, my Nancy. I am only speaking my truth. And truth should never be told to someone who is not worthy of it."
    kai "You, my dear, are always worthy. It’s always such a pleasure whenever I see you in my class."
    kai "When I was greeted by the warmth of this morning’s sun, it reminded me of the warmth that I feel around y—"
    show ag 105
    mc "*Clears throat*" with dis08
    mc "Well uhh, shall we get to it then?? No need to waste anymore of this morning sun..."
    show ag 107
    kai "Ah! Hello, my boy. Welcome to your {i}reawakening{/i}." with dis
    kai "I'm Mr. Kainan, from {i}Kainan Engineering{/i}. But no need for the formalities... you can call me Kai."
    kai "For no matter what esteemed backgrounds we come from, when we are in this place... we are all... {i}equals{/i}."
    show ag 106
    mc "Kainan Engineering? But aren't you a yoga teacher?" with dissolve
    show ag 107
    kai "Well, isn't yoga another type of engineering after all? Engineering of the body... of the soul..." with dissolve
    show ag 106
    mc "Um... No?" with dissolve
    show ag 107
    kai "Ah, a non-believer! Are you one of Nikolay's pupils?" with dissolve
    show ag 106
    mc "No, I came with Nancy." with dissolve
    show ag 107
    kai "Oh, really? You two know each other? Well I’m glad to meet you, because I’m positive you’re going to be seeing a lot more of me soon..." with dissolve
    show ag 106
    mc "What does that mean?" with dissolve
    show ag 108
    kai "Okay my precious flowers, please take your places on your mats." with dis12
    kai "We're about to elevate ourselves and break free of this week’s chains. As always, remember to relax and let yourselves be transported by the sound of the music and my sultry voice."
    kai "First exercise..."
    show ag 109
    hide screen heart
    with Dissolve(2.4)
    show fewminutescorner
    with Dissolve(1.5)
    pause
    scene ag 110
    show screen heart
    with Dissolve(2.2)
    pause
    kai "You are all doing marvelous..." with dis
    kai "Remember... Close your eyes, take a deep breath..."
    kai "And then exhale very slowly as we transition onto our final pose..."
    show ag 111
    n "*Exhales slowly*" with Dissolve(1.5)
    kai "Perfect, Nancy... your graceful movements are simply unmatched..."
    show ag 112 with dis12
    pause
    show ag 113
    mc "Grrr..." with dis
    kai "Your foot has to touch your back, [mc]."
    mc "*Grinding your teeth* You think I don’t know that?!"
    mc "I'm f-fucking trying."
    mc "I can’t raise it any higher!"
    kai "Connect with your foot. Feel the breeze between your toes. Channel your inner energy."
    kai "You are only limiting yourself, [mc]. Focus on your elasticity."
    mc "*Whispering to yourself* I wonder how elastic your neck is..."
    show ag 114
    kai "Well done, Raul." with dis12
    mc "(How the fuck is he doing that?!)"
    play music2 gym fadein 5
    stop music2b fadeout 5
    show ag 108
    kai "Alright, fantastic efforts everyone!" with dis12
    kai "Our last movement will be an Acro pose and must be done in pairs. So... Raul should go with Noah, [mc] with Gertrude, and... oh! I guess that leaves me with you, Nancy."
    mc "(Of course...)"
    show ag 115
    kai "You were so impressive today, Nan..." with dis12
    kai "Have you been practicing a lot at home?"
    ger "Ahh... they make a really lovely couple, don't you think, Dalia?"
    show ag 116
    mc "How many times do I have to tell you that I'm not Dalia? My name is [mc]!" with dis
    mc "And no, I think they'd make a horrible couple!"
    show ag 117
    ger "I mean, obviously Kai would’ve asked me out if I wasn’t already married, but since I’m happily taken... Nancy will be a very good fit for him." with dissolve
    show ag 116
    mc "Nancy would never date a guy like that."
    show ag 117
    ger "Well, I’m not one to gossip, but she already told me that she likes him..."
    ger "And guess what else I heard?! He's going to ask her out on a date after class!"
    show ag 118
    mc "What?! That can’t be true."
    ger "Oh... it is! Just wait and watch! Ahh, there’s nothing like witnessing newfound love..."
    show ag 115
    mc "(S-She isn’t interested in him... right?)" with dis
    mc "(Oh shit, but... what if she is?)"
    mc "(Nancy could say yes... then they’ll start dating, and then...)"
    mc "(No! I can’t let that happen!)"
    mc "(Or can I? I mean... Why am I so jealous in the first place? It's not like anything could happen between Nancy and I anyways...)"
    mc "(Maybe I should let it be. She deserves to be happy. Who am I to interfere with her personal life...)"
    menu:
        with dis
        "Stay out of Nancy's private life":
            mc "(I shouldn't get involved in this.)" with dissolve
            mc "(Nancy is her own woman. She doesn't need to be protected and she’s more than capable of making her own decisions.)"
            jump nancyyogafail
        "[gr]Do something":
            mc "(Fuck that. I can’t stand the thought of her being with that hippie.)" with dissolve
            mc "(This guy isn’t going to put his fluffy hands on her.)"
            mc "(I need to figure out a way to wrap this class up already...)"
    show ag 119
    mc "Hmm..." with dis12
    mc "(Maybe the Repeaters could help me?)"
    mc "*Whispering* Psst! Hey! Raul! Noah!"
    show ag 120
    noa "Hmm?" with dis15
    show ag 121
    rau "Yes?" with dissolve
    show ag 120
    mc "Have you seen the way this... Kai... is conducting his class? A little too handsy, don't you think?" with dissolve
    show ag 121
    rau "Ehh... I don't know, he has never touched me." with dissolve
    show ag 120
    mc "Well, maybe not you, but... it just seems like he’s trying awfully hard to get close to Nancy..." with dissolve
    show ag 122
    noa ". . . ." (multiple=2) with dissolve
    rau ". . . ." (multiple=2)
    show ag 120
    mc "So... Maybe you could... I don’t know, distract him?" with dissolve
    show ag 122
    noa ". . . ." (multiple=2) with dissolve
    rau ". . . ." (multiple=2)
    show ag 121
    rau "Distract?" with dissolve
    show ag 120
    mc "Y-Yeah, I know Nancy very well, and honestly she’s been in quite a heightened emotional state lately. I can’t bear the thought of that guy taking advantage of her." with dissolve
    show ag 122
    noa ". . . ." (multiple=2) with dissolve
    rau ". . . ." (multiple=2)
    show ag 121
    rau "So you want us to get rid of him?" with dissolve
    show ag 120
    mc "*Laughs* Well, when you say it like that, it sounds like you're gonna kill him or something." with dissolve
    noa ". . . ." (multiple=2)
    rau ". . . ." (multiple=2)
    mc "Um... S-Seriously, don't hurt him."
    mc "I just think I should be the one doing that last pose with her, instead of him. Then I know she’ll be safe."
    mc "Can you just distract him so he has to leave for a moment..."
    show ag 122
    noa ". . . ." (multiple=2) with dissolve
    rau ". . . ." (multiple=2)
    show ag 121
    rau "And what's in it for us?" with dissolve
    show ag 120
    mc "I noticed you two missed class yesterday." with dissolve
    mc "I can lend you my notes! All of them!"
    show ag 122
    noa ". . . ." (multiple=2) with dissolve
    rau ". . . ." (multiple=2)
    show ag 121
    rau "We're not really interested. But we can help you in exchange for money." with dissolve
    show ag 120
    mc "Erm... well, I don’t really like to carry around cash."with dissolve
    show ag 121
    rau "Do you play Eternum? You can pay us with eternals. They're... harder to track."with dissolve
    show ag 120
    mc "Oh! I wasn't expecting you to be Eternumites too! Yeah, I can do that."with dissolve
    mc "I'll send you 5 eternals. Go get yourselves a beer, my treat!"
    show ag 121
    rau "50." with dissolve
    show ag 120
    mc "50?! I’m a new player! I’m not very rich! You guys are just joking, right?" with dissolve
    noa ". . . ." (multiple=2)
    rau ". . . ." (multiple=2)
    mc "I guess not..."
    menu:
        with dis
        "[gr]Hire Noah and Raul":
            mc "*Sighs* Okay, okay, have 10 beers then! But you better cheers to my good health!" with dis08
        "Forget it":
            mc "No way I'm paying you guys that." with dis08
            mc "You know what, forget it."
            mc "Nancy is her own woman. She doesn't need to be protected and she’s more than capable of making her own decisions."
            mc "This was a silly idea. I'll just see you guys around, then."
            show ag 121
            rau "Have a good day, sir." with dissolve
            jump nancyyogafail
    show ag 122 with dissolve
    pause
    show ag 123 with dissolve
    show ag 122 with dissolve
    pause
    show ag 124
    rau "Alright, Noah will take care of it. Pleasure doing business with you, [mc]." with dis12
    show ag 125
    show screen eternals
    with dis
    play sound coins
    $ money -= 16
    pause .05
    $ money -= 17
    pause .05
    $ money -= 17
    pause .05
    mc "Sure, I’ll think of it as treating some friends to lunch." with dissolve
    show ag 124
    hide screen eternals
    rau "My Eternum ID is 275,100,101. Don't forget to wire me the money when you go online next time." with dissolve
    show ag 125
    mc "Sure, I will."
    show ag 124
    rau "Great."
    show ag 126 with Dissolve(1.75)
    pause
    kai "Damn..." with dissolve
    kai "Look at that perfectly toned stomach... And to think she's had 2 daughters! Unbelievable."
    kai "She's perfect, isn’t she, Raul?"
    show ag 128
    rau "I don't know, Mr. Kai." with dis12
    show ag 127
    kai "It's just... there's something about redheads that... I don't know, they drive me crazy. They truly are a masterpiece and testament to the beauty of this world." with dissolve
    kai "What on earth could top a beautiful redhead, Raul?"
    show ag 128
    rau "Jesus Christ?" with dissolve
    show ag 127
    kai "I'm gonna ask her out today. When the class is over, she’s going to be mine." with dissolve
    kai "I've been fantasizing about how those beautiful tits look for far too long. Ever since she first stepped foot into my class..."
    play soundlow stairsrun
    pause 1.8
    show ag 129 with dis
    mil "Kai!" with hpunch
    kai "Hmm?"
    mil "There’s a car in the parking lot that started smoking! It looks like it's coming from the engine!"
    mil "I t-think it's your car!"
    show ag 130
    kai "What?!" with dis
    rau "Oh... yeah, that usually happens when you leave your car in the sunlight for too long. There must be some extra warmth coming from the morning sun today."
    kai "Fuck, no! I’m still paying that thing off!" with hpunch
    kai "Sorry guys, I’m going to have to conclude this class early!"
    kai "Millie, call the fire department!" with hpunch
    mil "Right away!!"
    show ag 131
    ger "Well, looks like class is ending early today. That’s a shame, I would’ve loved to try out that pose with you, Dalia!" with dis
    ger "Nan, honey, I'm going to the bathroom again. Just wait for me here!"
    n "Sure thing."
    show ag 132
    mc "Jeez, talk about bad luck. Poor Kai..." with dis15
    mc "I guess I should start rolling up my mat."
    play sound musicstop
    stop music2 fadeout 1
    play music2b yoga fadein 4
    show ag 133
    n "Not so fast!" with hpunch
    n "We still have one last pose to do! After all that hotshot talk earlier, I’m not going to let you off that easily!"
    show ag 132
    mc "Oh, the pose with a partner?"
    mc "Sounds good! I was hoping to do it with you... as uhh, lovely as Gertrude may be..."
    mc "I don't know how it's done, though."
    show ag 133
    n "No worries. Just follow my lead."
    n "I’ll do the hard part. You just have to lie down on the floor."
    show ag 132
    mc "*Chuckles* Now that sounds like something I can do!"
    play sound fall2
    show ag 134 with dis12
    mc "Like this?" with dissolve
    n "Yeah! Now place your hands on the floor and raise your legs until they are perpendicular to the ground."
    show ag 135 with dis12
    n "*Giggles* Yep, just like that!" with dissolve
    show ag 136
    n "Now hold it steady! I'm going to get on top of your feet." with dis08
    n "Take hold of my arm and don't move your legs!"
    play soundlow dodge
    show ag 137
    mc "Whoa!" with dis
    mc "You good up there?"
    n "*Giggles* Yeah, I've always had a pretty good sense of balance. But I’m trusting you here—don't let me go!"
    mc "*Chuckles* I could never do that..."
    n "Alright..."
    n "Now just relax, let the music flow through you, and try to think of us like we’ve become one being."
    show ag 138
    n "Close your eyes and synchronize your breathing with mine..." with dis
    show ag 139 with dis08
    pause 05
    mc "(Wow... What is this sensation?)" with dis
    mc "(I can feel her steady pulse and her deep breaths in sync with mine...)"
    mc "(It's as if nobody else exists... it’s only... us...)"
    show ag 140
    n "Oh no..." with dis08
    n "I think I’m losing my balance!"
    show ag 141
    play sound fall
    play sound2 fall2
    n "Ahhh!" with hpunch
    n "Oh my god, I'm so sorry! I felt like we... were having a moment there or something..."
    show ag 142
    mc "It's o-okay!" with dis08
    mc "Don't worry, you didn't hurt me."
    play soundlow clothes
    show ag 143
    mc "*Sitting up* I guess I need a little more practice..." with dis12
    n "No, no! That was all my fault."
    n "I think I relaxed a bit too much..."
    show ag 145
    mc "Well..." with dis
    mc "I guess we’re both going to have to practice a little bit more then. Together."
    $ nancy_points += 1
    play sound "beat.ogg"
    show heartr at topleft with dissolve
    hide heartr
    show ag 144
    n "Seems fair to me." with dissolve
    n "I'm sure we can both learn a lot of things from each other..."
    show ag 145
    mc "I'm looking forward to it..."
    show ag 144
    n "Me too."
    n "You know... your return to Kredon has been the best thing that has happened to me in a long time, [mc]."
    n "Just when my life began to feel so stale... so monotonous..."
    n "You showed up. And you’ve brought so much joy to our lives in just the few days you’ve been here. To my life, especially."
    n "*Giggles* Just like when I was your babysitter."
    n "How can you always turn each moment of the day into something so memorable? I’ve already caught myself numerous times giggling like a little girl as I reflected on our encounters..."
    show ag 145
    mc "Well, I kind of just... go for things. I seize the moment. I prefer to leave my regrets behind me. That's my principle."
    show ag 144
    n "Mmm, that's some good advice."
    n "Can I ask you something?"
    show ag 145
    mc "Of course."
    show ag 144
    n "Do you ever think about... whether you and I—"
    stop music2b fadeout 5
    play music2 gym fadein 4
    ger "Naaaan? How long do I have to wait for you?" with dis
    play sound clothes1
    show ag 147
    n "G-Gertrude! Y-Yeah, sure, sorry, I got distracted." with hpunch
    show ag 146
    ger "I've been waiting downstairs for ten whole minutes! It's noon already!" with dis08
    show ag 147
    n "W-Wow, I guess time sure has flown by..."
    show ag 146
    ger "Come on, I know a great vegan restaurant. I'll let you invite me to lunch."
    show ag 147
    n "S-Sure, let's go."
    play sound fall2
    show ag 132
    mc "*Standing up* Well, I guess I should go now too. I'll let you eat with your... {i}best{/i} friend." with dis
    mc "*Whispering* Good luck with that."
    show ag 133
    n "*Laughs* Thank you."
    n "Do you have any plans for today?"
    show ag 132
    mc "I'm going to grab a quick bite because I'm meeting a friend this afternoon. We’re going to work on a school project."
    show ag 133
    n "Ah, nice. Good luck! Hope you’re able to get a lot done!"
    show ag 132
    mc "Thanks! I'll see you later tonight then!"
    mc "Take care, Nancy!"
    show ag 133
    n "You too, [mc]."
    show ag 148 with Dissolve(2)
    n "*Sighs*" with dissolve
    ger "Dalia is such a good boy, isn't he?"
    show ag 149
    n "Yeah, he definitely is..." with dis
    n "Hm..."
    n "Anyways, let's get going."
    play soundlow stairsrun
    pause 2
    show ag 150
    kai "Nancy?!" with dissolve
    kai "Oh thank mother nature, you're still here!"
    n "Kai!"
    n "(Maybe he can help me...)"
    n "Gertrude, can you go on ahead? I'll join you in a minute. I wanna ask Kai something."
    ger "*Hearty laugh* But of course... have fun you two..."
    show ag 152
    kai "*Breathing heavily* I’m... so relieved... you didn't leave yet, Nancy." with dis15
    show ag 151
    n "How's your car?"
    show ag 152
    kai "*Breathing heavily* Oh it’s fine, not a big deal... completely totaled, but I’m not going to let that ruin my vibe."
    kai "I guess someone set off a homemade explosive device right underneath it. It’s all good though, the tow truck hauled it away already."
    kai "My horoscope said to not let things blow up today. I didn’t know it was referring to my car..."
    kai "But anyways, I need to ask you something! It must not wait any longer!"
    show ag 151
    n "Ah, I wanted to ask you something too..."
    show ag 152
    kai "R-Really?! Go ahead!"
    show ag 153
    n "Well... you always say that you're both a physical and spiritual guide, right?" with dis08
    show ag 154
    kai "Of course!"
    show ag 153
    n "Well, I was hoping you could give me some advice. Lately, I’ve been finding myself so distracted by a little dilemma that I’m having. I almost feel as if it’s consuming me..."
    show ag 154
    kai "Dilemma, huh? Go on..."
    show ag 153
    n "Um... God, this is a little embarrassing..."
    n "As you know, I've been single for a long time."
    show ag 154
    kai "Uh-huh..."
    show ag 153
    n "And I’ve always thought I was doing just fine on my own, but..."
    n "T-There's this... man... that has really turned my life around."
    n "I don't know why, but every time I see him my heart starts beating like crazy. I get butterflies in my stomach. I just... can't stop fantasizing about him..."
    n "He makes me feel so... alive! So young! So beautiful!"
    show ag 154
    kai "Oooh... Let me guess... He's from yoga class...?"
    show ag 155
    n "*Giggles* Perhaps..." with dis
    kai "Oh my god..."
    show ag 156
    n "But the thing is..." with dis08
    n "I can't be with him. It would be... weird. We’re not supposed to be together... like {i}that{/i}."
    n "And even if I tried to make a move, I don't know if he'd want to be with me."
    show ag 157
    kai "What? That's absurd! You're a goddess, Nancy! You’re a modern day Aphrodite!"
    show ag 156
    n "But even if he wanted me too... and he felt the same way, what would other people think? What would my daughters think of me?"
    show ag 157
    kai "Your daughters? I've seen Dalia a couple of times in the fitness room. I know she would definitely approve! She even waved at me once! Or at least... waved near me..."
    show ag 156
    n "I don't know Kai..."
    n "To be completely frank with you, I... I just get so horny whenever I think of him. And whenever I’m around him! I can’t seem to control it!"
    kai "Oh god..."
    n "I'm scared I’ll lose control if I give myself to him."
    show ag 155
    n "I've been holding back for too long... I have so much pent-up frustration. W-What if I turn into some sort of... insatiable nympho?" with dis08
    kai "Yes..."
    n "*Giggles* Kinda like a volcano that hasn’t erupted for a long time, and it’s just about ready to burst... you know what I mean?"
    kai "YES!!!"
    show ag 156
    n "I mean..." with dis08
    n "I’ve never felt this way before. What if I start asking him to do all these wild things with me? Live out my craziest fantasies? What if I discover some weird kinks I didn't know I had?"
    kai "GOD YESSSS!!!!!!"
    n "I don’t even think I would mind sharing him either. Just the thought of him having myself and someone else that’s close to me..."
    show ag 157
    kai "You mean like... a threesome with you and Dalia? Or a foursome with your other daughter too?!"
    show ag 155
    n "What!! N-No..."with dis08
    n "*Giggles* Um, maybe. No... But, I mean... could you imagine?!"
    n "I’m not sure it’d ever come to that point, but..."
    kai "OH MY GOD NANCY, YES!!!! DEAR LORD, A HUNDRED TIMES YES!!!!"
    kai "You need to go for him. GET HIM NOW!!"
    show ag 158
    n "*Giggles* You really think I should do it?" with dis08
    kai "Absoooolutely!"
    kai "Nancy, sex is a beautiful part of life. If you have needs, you need to be taken care of. You deserve to be pampered... desired... lusted after. Even more so with you being such a beautiful woman."
    kai "Surrender to pleasure, Nancy. Succumb to your carnal desires!!"
    n "*Giggles* Yay! Okay! I think I’m actually going to do it!"
    n "I’m not going to hold back anymore!"
    kai "Don’t you dare hold back!"
    kai "Fulfill all of your wildest fantasies! Life is too short!"
    n "YES!! Okay! Agh, I can’t wait!!"
    n "I'll tell you how it went next Saturday!"
    n "Thank you so much, Kai! You’re such a good friend!"
    show ag 159
    n "*Leaves*" with dis15
    stop music2 fadeout 2
    kai ". . ." with dis12
    kai ". . . ?"
    show ag 160 with dis12
    kai "W-Wait a second..." with dissolve
    kai "W-Was she not talking about m-me...?"
    play soundlow clothes1
    show ag 161
    rau "You ever think about going back to engineering, Mr. Kai?" with dis
    kai ". . ."
    stop music2 fadeout 5
    play musicb shower1 fadein 4
    show ag 162 with Dissolve(2.5)
    pause
    show ag 163 with dis15
    pause
    show ag 164 with dis15
    pause
    show ag 165 with dis15
    n "(Man, I feel so... ALIVE!!)" with dissolve
    n "(Am I really gonna do it?!)"
    n "*Giggles* (It feels like I’m 16 again!)"
    show ag 166
    n "(Although... how would I even approach him...?)" with dis15
    n "(I can't just barge in and be like, \"Hi [mc], did you know you make me feel so horny all the time? Do you wanna fuck your old babysitter?\")"
    n "(Even if, somehow, he wanted me too... and we ended up... doing it, Dalia and Penny would be furious if they ever found out.)"
    n "(No, they can’t find out. We'd have to keep it a secret... Our dirty little secret.)"
    n "(Which is also kind of exciting, I’m not gonna lie...)"
    show ag 167
    n "(What should I do? Think, Nancy, think...)" with dis15
    n "(Hmm...)"
    n "(Maybe I could try to play that game... Eternum.)"
    n "(He spends a lot of time playing it.)"
    n "(And I've heard you can do {i}anything{/i} there. And that it feels exactly like real life.)"
    show ag 169
    n "(Oh god, I'm getting horny again just thinking about it... all the things we could do together...)" with dis15
    n "(I need him to fuck me so hard... ever since I saw his dick, I can’t keep it off my mind.)"
    n "(Hmmm... And Eternum would be the perfect place to avoid getting caught, too.)"
    show ag 168
    n "(But it's so expensive!)" with dis08
    n "(I don't have an extra $3500 lying around.)"
    n "(I know my job pays well, but with Dalia and Penelope's tuition costs, I’ve barely set aside anything else.)"
    n "(I'll have to come up with something. There’s gotta be a way...)"
    show ag 167
    n "(It sure isn’t easy being a single mom.)" with dis15
    ger "Nan?! *Hearty laugh* You’re gonna get all wrinkly if you stay in there any longer!"
    show ag 170
    n "Yeah, I'm coming out!" with dis
    n "Sorry, I got a little lost in my thoughts..."
    play music bathfan fadein 4
    stop musicb fadeout 4
    show ag 171 with Dissolve(2.5)
    ger "Our table is booked for 1:40." with dissolve
    n "Ah, okay."
    n "I just need to blow dry my hair."
    play sound chair1
    show ag 172
    n "(Hmph. I just can't justify spending $3500 on that neural implant.)" (multiple=2) with dis12
    ger "You're gonna love this place, Nan." (multiple=2)
    n "(If it was cheaper then I would get it right away! But at that price? No...)" (multiple=2)
    ger "They have these hamburger patties made of celery and blended tofu that are sooo good. It almost tastes like chicken if you add their bok-bok chicken sauce." (multiple=2)
    show ag 173
    n "(I mean, what if Dalia or Penny got sick and I couldn't afford the medical bills?)" (multiple=2) with dis08
    ger "I used to go to another restaurant, but then one day they served me raw artichoke. Can you believe it?" (multiple=2)
    show ag 174
    n "(I could never forgive myself for that. I should really start building up an emergency fund.)" (multiple=2) with dis08
    ger "They told me it was cooked enough, so then I stood up and said, “EXCUSE ME?! Do you even know who I am?”" (multiple=2)
    show ag 173
    n "(I guess I'll have to find another way to get closer to [mc].)" (multiple=2) with dis08
    ger "I'm the president of the Kredon School PTA! I have the power to do it all! I can get your son a scholarship, or I can get him expelled!" (multiple=2)
    show ag 174
    n "(Which is a shame, to be honest. Eternum looks amazing! I've been wanting to try it for so long.)" (multiple=2) with dis08
    ger "*Hearty laugh* Enjoy your 1-star review and your underpaid job, kid! I bet you went to public school too, you illiterate buffoon!" (multiple=2)
    show ag 172
    n "(I bet if I tried to do anything at home, Dalia or Penny would surely notice.)" (multiple=2) with dis08
    ger "After that, I went home all angry. Then my husband tried to win me over with some little gizmos he ordered us as a gift. It’s one of those game-thingamabobs that everyone plays on now." (multiple=2)
    show ag 173
    n "(God, that would be so embarrassing.)" (multiple=2) with dis08
    ger "At first I was mad, I was like, “Why’d you buy me one of those kiddy thingamajigs?! You think the PTA president has time for such nonsense?!”" (multiple=2)
    show ag 172
    ger "But then he explained afterward how it could be good for our relationship. So I guess I'll try it once it’s delivered tomorrow." with dis
    ger "I think it’s called an Ethereum implant."
    play soundlow whoosh3b
    show gerzoom with Dissolve(.05)
    n "Wait, a w-what?"
    show ag 179
    hide gerzoom
    ger "Am I saying it wrong? Eternimum?" with dis
    show ag 178
    n "Oh! Eternum? That's so cool! I was just thinking about that game too."
    n "Your son will love it."
    show ag 179
    ger "My son? No, no, he already has his own. This one is for me."
    show ag 180
    n "You? At our age?"
    show ag 181
    n "Oh well, I guess it is for all ages, but..." with dissolve
    show ag 179
    ger "But? W-What's the problem?"
    show ag 180
    n "Nothing! It's fine. It's just that, umm..."
    n "Was it your husband's idea to play?"
    show ag 179
    ger "Yes, it was."
    show ag 181
    n "Oh no... Just as I feared."
    show ag 179
    ger "What's wrong?! Tell me, Nan!"
    show ag 181
    n "It’s that... Well, I would hate for the same thing to happen to you..."
    show ag 179
    ger "Thing? What thing?!"
    show ag 180
    n "Do you know Mindy? Randy's mother?"
    show ag 179
    ger "No, doesn't ring a bell. Must not be in the PTA..."
    show ag 180
    n "Well, it turns out that Mindy bought neural implants for herself and her husband a few weeks ago, too."
    show ag 181
    n "Everything was great at the beginning, but then she discovered the ugly truth: her husband had fallen in love with a woman 20 years younger than her! Someone he met while playing!" with dissolve
    show ag 179
    ger "Oh heavens, no!"
    show ag 181
    n "Yeah... and then he ended up leaving her and their three kids to run off with that girl."
    show ag 180
    n "I've heard Eternum is full of gold diggers, just waiting to pounce on vulnerable husbands that are exhausted from the mundane routine of their normal life."with dissolve
    show ag 182
    ger "Oh my god! That's terrible!" with dis
    ger "Do you think that my Richie could ever do something like that?"
    n "I don't know, Gerty... I don't know..."
    n "But... between you and me, if I were in your shoes, I simply wouldn't risk it."
    ger "You’re right! I can’t chance it! But what can I do now?!"
    ger "The company doesn't offer refunds!"
    n "And it's almost impossible to sell them, even if you say it’s unused. People are worried about getting an implant that’s been illegitimately modified or hacked if they buy it second-hand."
    n "I think your best bet would be just to give it to someone you know."
    ger "But who? Who would buy it from me?"
    n "*Sighs* I don't know. I hate seeing you in a situation like this, Gerty."
    n "But you know what? I guess I can take it off your hands. I can’t just stand by and do nothing while you try to save your relationship."
    n "I'll even give you $100 for it."
    ger "$100? B-But..."
    ger "But that thing cost us $3500, Nan!"
    ger "It'd be a shame to lose all that money just like that!"
    n "Do you know what else would be a shame to lose? And would ultimately cost you even more money?"
    show ag 183
    n "Your marriage." with dis15
    show ag 184
    ger "OH MY GOD." with dissolve
    ger "YOU’RE RIGHT!!!"
    ger "I have to save my marriage. Do you know how that would make me look? Being the PTA president as a {i}single mother{/i}?! UGH!!"
    ger "Oh... I mean... not that there’s anything wrong with being a single mother, of course, but..."
    ger "Just take that cursed machine away from my family! Please!"
    show ag 185
    n "What would be a good time to meet up tomorrow?" with dis08
    $ nancyyoga = True
    jump alexhouse



label nancyyogafail:
    show ag 115b with Dissolve(1.6)
    mc "Hey Nancy!" with dissolve
    mc "Um... look, I'm really sorry, but I have to get going."
    show ag 115c
    n "What?" with dissolve
    n "Why? What happened?"
    show ag 115d
    mc "Nothing! It's just that... I should really grab a quick bite before meeting with my friend to work on a school project."
    show ag 115c
    n "Oh... it’s okay..."
    n "I'm sorry... you probably got bored, huh. I know that you must be used to participating in more fast-paced activities..."
    show ag 115d
    mc "That’s not true at all! Seriously, I loved the class."
    mc "It's just that... I'm in a bit of a hurry and don’t want to be late."
    show ag 115c
    n "Uhm... well alright then. I guess I’ll see you at home."
    n "Take care, [mc]."
    show ag 115d
    mc "Sure! Bye, Nancy."
    n ". . ."


label alexhouse:
    stop music fadeout 3
    stop music2 fadeout 3
    stop music2b fadeout 3
    show b with Dissolve(2.8)
    pause
    show screen afewhourslater with dis12
    pause
    play music2 happy3 fadein 3
    hide screen afewhourslater
    scene aaz 1
    with Dissolve(2.8)
    mc "(Alright, I think this is the place where I'm supposed to meet Alex.)" with dissolve
    mc "(I mean... Alexandra. Don't wanna screw that up again...)"
    show aaz 2 with Dissolve(1.2)
    mc "(Damn! There must be something in the water here in Kredon... these women are gorgeous...)" with dissolve
    mc "(I need to convince Penelope to bring me with her to the next college party.)"
    mc "(That’ll be one adventure that I definitely won’t want to miss!)"
    show aaz 3
    mc "*Taking a deep breath*" with dis
    if nancyyoga and nancypath:
        mc "(I wonder what Nancy was about to say before Gertrude interrupted us.)"
        mc "(I don’t know if it was just me, but I definitely felt some... sexual tension? Could that be possible?)"
        mc "Hmm..."
    elif not nancyyoga and nancypath:
        mc "(I wonder if Nancy agreed to go on a date with Kai...)"
        mc "(Well, whatever she decided, I shouldn’t think much about it. It’s none of my business. I did what I thought was best. Besides, I have enough of my own stuff to worry about...)"
        $ nancypath = False
        $ nancyu = False
    play sound tires
    show aaz 4 with Dissolve(.8)
    play soundlow carhorn
    nei "WHAT THE FUCK! WATCH THE ROAD YOU OBLIVIOUS PIRATE!" with hpunch
    no "S-Sorry!"
    play soundlow caraway
    show aaz 5
    mc "(Not a cloud in the sky since yesterday.)" with dis
    stop soundlow fadeout 3
    mc "(Definitely a welcome change!)"
    play sound dodge
    show aaz 6
    no "[mc]!!!" with dis
    mc "W-Wha—whoa!!"
    play sound2 fall
    play sound3 fall2
    show aaz 7 with Dissolve(.8)
    mc "Argh... my head..." with dis
    no "*Giggles* Oops... Sorry!"
    mc "N-Nova? Where the hell did you come from?!"
    mc "(Where in the world does this girl get all her energy from?)"
    mc "Do you always appear out of nowhere like that?! You’re like a face pimple on date night..."
    no "What are you doing here anyway?"
    mc "I’m waiting for someone! What are YOU doing here?"
    no "I have some news for you!"
    mc "News?"
    no "Did you already forget?"
    no "You hired me to investigate your little mystery!"
    mc "Oh... yeah, of course."
    show aaz 9 with dis
    mc "*Standing up* Well, technically, I didn't hire you." with dissolve
    show aaz 8
    no "Hire, recruit, ask a favor... call it what you want!"
    show aaz 9
    mc "I prefer to think of us as a team."
    mc "That's why I was hoping to have some way to reach you."
    mc "That way we could..."
    mc "Wait, how did you even find me?"
    show aaz 11
    no "Um..." with dis
    no "It was purely a coincidence...!"
    mc "Hmm..."
    mc "You're a terrible liar."
    mc "You might have many talents... but lying is not one of them. You’re bad at it."
    mc "Tell me the truth."
    no "Um..."
    no "Well, I might have tapped into the GPS service on your phone..."
    mc "WHAT?!"
    no "But I just did it to find you, in case I needed to tell you something important..."
    no "It's not even that accurate anyways..."
    no "I find it’s usually off by about 50 or 60 feet..."
    mc "50 feet?! I could easily throw a football that far!"
    no "Well..."
    mc "Wait a minute... I thought you said you only hack people that interest you..."
    show aaz 15
    no "W-We're getting off track here." with dis
    show aaz 10
    no "So guess what! I was able to hack into Kredon's Police Department storage database!"with dis
    mc "Damn! Really?"
    no "Hell yeah!"
    mc "That’s badass! Totally illegal, but badass!"
    mc "What did you find out?"
    stop music2 fadeout 7
    play music2b dark2 fadein 6
    show aaz 12
    no "*Whispering* Okay, this is where things get a little more serious. We should lower our voices." with dis
    mc "*Whispering* Got it."
    show aaz 13
    no "You were right. The police files regarding Benjamin’s death were definitely modified." with dis
    show aaz 14
    mc "I knew it!"
    show aaz 13
    no "The forensic report that was filed doesn't match the public information at all."
    no "He wasn't found dead in his garage... he died of an aneurysm while playing Eternum! His estimated time of death was right after you saw him playing the game!"
    no "That leads me to believe..."
    no "That somehow..."
    show aaz 14
    mc "The Praetorian that excommunicated him in the game caused his death in the real world too."
    show aaz 13
    no "Exactly."
    show aaz 14
    mc "Have there been any other reports of real-world deaths while playing Eternum?"
    show aaz 13
    no "Not that I've seen."
    show aaz 14
    mc "And what about his family?"
    mc "Why aren’t they going public with this information?"
    mc "There are a lot of organizations that are opposed to the way Eternum operates. A story like this would be headline news!"
    show aaz  15
    no "Ah! Now comes the ugly part." with dis
    no "I took a peek at the bank account of Benjamin's parents and saw they received a transfer of $750,000... one day after Benjamin died."
    mc "What? Do you think that..."
    show aaz 16
    no "Ulysses paid for their silence." with dis
    no "I knew they were hiding something!"
    no "That means they could’ve totally done this before... Excommunicating people in the game and causing their death in real life... then bribing the families and the press for their silence."
    mc "Holy shit..."
    mc "This is all starting to sound like a conspiracy..."
    no "There’s definitely a lot of merit to this one."
    mc "What do you suggest we do now?"
    show aaz 13
    no "I'll keep digging." with dis
    no "I think our best source of information is within Eternum itself... we just need to talk to the right people."
    no "If we become high-level players, or gain prestige by attaining a Weapon of Atlas or a Gem of Doom... we might get invited to one of those high-class dinners."
    no "If those dinners happen to be attended by some Ulysses big shots, I can try to download all their private information."
    show aaz 14
    mc "(Hmm... I shouldn't tell her about the Gem we found in The Red Herring... not yet, at least.)"
    mc "Alright, that sounds like a solid plan to me."
    stop music2b fadeout 7
    play music2 happy3 fadein 6
    show aaz 8
    no "Yep! Okay, we probably shouldn’t talk about this in public anymore." with dis
    no "I'll give you my phone number in case you need to reach me."
    show aaz 9
    mc "Well, well, well! So you do have a cell phone!"
    show aaz 8
    no "It's a burner phone, obviously. Secure line."
    show aaz 9
    mc "Good, gotta make sure you’re not losing your edge!"
    show aaz 17
    no "Well...?" with dis
    no "I’m waiting..."
    no "Aren't you gonna say something?"
    mc "Alright, alright... I gotta say..."
    mc "Hacking both the police department and the bank account of Benjamin’s parents... all in just one day?"
    mc "You’re the real deal!"
    no "And don’t forget about those forensic files!"
    mc "Yes, {i}and{/i} the forensic files."
    show aaz 18
    mc "(She seems so eager for praise.)" with dis
    mc "(I guess that’s to be expected. The necessity of anonymity in her activities means she can’t really talk about her accomplishments with anybody.)"
    mc "(I don’t know shit about hacking, but I know that stuff she did couldn’t have been easy...)"
    mc "(I'm sincerely impressed.)"
    menu:
        with dis
        "Pat her head [pink][mt](Nova +1)":
            show aaz 20 with dis
            mc "Nice job, Nova!" with dissolve
            $ nova_points += 1
            play sound "beat.ogg"
            show heartr at topleft with dissolve
            hide heartr
            mc "I really am impressed!" with dissolve
            mc "You did things I thought were only possible in movies."
            mc "The way you hacked into that mainframe, firewalled those... viruses, and umm, IP’d those addresses..."
            show aaz 21
            no ". . ."with dis
            show aaz 22
            mc "You're such a good girl! You deserve a cookie, and not the web browser kind!" with dissolve
            show aaz 23
            no "H-Hey, don't overdo it!" with dis
            no "I'm not a damn puppy!"
            mc "*Laughs* I thought you needed to be buttered up!"
            no "W-Well, thank you for the compliments, but I’m not a child!"
            mc "*Laughs* You liked the head pats though, admit it..."
            no "*Huffing* Hmph."
        "Just compliment her":
            mc "Nice job, Nova!" with dis
    play sound suzukirevs volume 1.2
    stop music2 fadeout 6
    pause 1
    play music2b bikeidle fadein 5
    show aaz 24 with Dissolve(2)
    stop sound fadeout 3 
    mc "Oh, damn!" with dis06
    mc "Alex...andra?"
    show aaz 25 with dis
    pause
    play sound helmet
    show aaz 26 with dis
    $ unlock_look("alex", 1)
    mc "Wow, I didn't know you ride!"with dissolve
    show aaz 27
    x "Yeah, well, we’ve only seen each other once before so..." with dissolve
    x "It would have surprised me if you knew."
    show aaz 26
    mc "Yeah, fair point. Always so logical." with dissolve
    show aaz 27
    x "Who's your friend?"with dissolve
    show aaz 28
    no "Nova. Nice to meet you."
    x "Alexandra."
    mc "This bike looks so cool! I want to learn how to ride!"
    no "Yeah, it looks pretty badass."
    show aaz 26
    no "I wasn't expecting [mc] to be meeting up with a girl."with dis
    no "Are you two... a couple?"
    mc "W-What?"
    show aaz 27
    x "*Laughs* He wishes!" with dissolve
    show aaz 26
    mc "Yeah, I wish she’d stop fangirling over me! It’s exhausting!"with dissolve
    show aaz 27
    x "Yeah, sure... keep dreaming, dummy." with dissolve
    show aaz 28
    no "Sorry for asking, it's just that I thought he was waiting for Chang or Annie."
    no "I didn't know [mc] had more friends."
    x "Nah, I wouldn't even say that. Our teacher was the one who paired us up."
    mc "Yeah, we have to do a project about..."
    show aaz 29
    mc "Hold up a second, how the fuck do you know who Chang and Annie are?" with dis
    no "...Hmm? Who?"
    mc "Chang and Annie! You just said their names!"
    no "H-Huh, what? No I didn’t!"
    mc "Yes, you did! Stop lying! I told you, you’re terrible at it!"
    show aaz 30
    no "Ohhh... yeah, well, you mentioned them the other day. Don’t you remember?" with dis
    mc "That's not true!"
    no "Er... I meant to say that I saw the three of you the other day when..."
    mc "That's not true either!" with hpunch
    mc "Oh my god, you're a compulsive liar!"
    show aaz 31
    no "Erm..."with dis
    mc "Did you hack me?!"
    mc "OH GOD, YOU {i}DID{/i} HACK ME!"
    show aaz 32
    no "Oh shit, well would you look at the time!!" with dis
    mc "What did you see?!"
    no "Gotta go!"
    mc "Wait!"
    no "Call me if you find anything interesting...!"
    mc "NOVA!!!!"
    show aaz 27
    x "*Laughs* I think I like that girl." with Dissolve(1.5)
    show aaz 26
    mc "Did you see that?! She totally hacked me! After I specifically asked her not to!" with dissolve
    show aaz 27
    x "Got some juicy pics on your phone, [mc]?" with dissolve
    show aaz 26
    mc "Um... N-No, of course not..." with dissolve
    show aaz 27
    x "Embarrassing browser history, perhaps?" with dissolve
    show aaz 26
    mc "N-No..." with dissolve
    mc "(Oh shit...)"
    show aaz 27
    x "Then stop crying!" with dissolve
    play sound helmet
    show aaz 25
    x "Let’s go, we're late." with dis
    x "Get on."
    mc "On the bike? With you?"
    x "Are you scared?"
    mc "Me? Hah! Fearless is my middle name."
    x "*Chuckles* That's the spirit."
    play sound2 suzukitakeoff
    stop music2b fadeout 4
    play music2 garage fadein 6
    scene black with dis22
    show screen afewminuteslater with dis15
    with dis2
    pause 
    scene aaz 33 
    hide screen afewminuteslater
    with dis2
    x "Alright, here we are." with dissolve
    x "No need to be afraid anymore."
    mc "What are you talking about? I wasn't scared."
    x "I don't know about that... you were holding on to me awfully tight. I think I even heard you whimper."
    mc "You were going 60 down a residential street!!"
    x "Relaaax, it’s okay, I won’t judge you for being freaked out."
    mc "*Laughs* Oh screw you!"
    show aaz 34 with dis
    mc "*Getting off the bike* Holy shit, is that a Lambo?" with dissolve
    x "Hmm? Ah, yes. Two, actually."
    mc "(Damn, Alex's neighbors must be rich as fuck.)"
    mc "(I wonder if her family is well off, too. This is a pretty wealthy-looking neighborhood, so it's very possible.)"
    show aaz 35
    mc "(There are even security cameras all throughout this parking garage.)"with dis
    mc "(I don’t blame ‘em. I’d want surveillance too if I owned cars like that.)"
    play sound carrev
    show aaz 37 with dis
    show aaz 36
    x "Saying hello to the guards?" with dissolve
    show aaz 37
    mc "Sorry, I was lost in thought." with dissolve
    mc "It's just, I'm not used to seeing all this security. I'm the type of guy who will leave his bike padlocked to a tree, if you know what I mean."
    mc "Those cars are awesome, though."
    show aaz 38
    x "Meh, I'm not a car person." with dis
    x "They just look like a waste of money to me, to be honest."
    x "Do people actually like these gaudy things? I feel like most buy them only as a status symbol. They just want people to assume they're sooooo successful..."
    x "But hey, if it helps your fragile ego and you have a lot of cash to burn, knock yourself out..."
    show aaz 39
    x "Anyways, step back." with dis
    x "I'm gonna park over there."
    mc "Oh, sure, sorry."
    play sound carrev
    show aaz 35 with Dissolve(1.5)
    mc "I noticed all these parking spots are numbered..." with dissolve
    show aaz 40 with Dissolve(1.5)
    mc "Does that mean A2 is your apartment?" with dissolve
    x "Not really, these numbers don't mean shit."
    play sound helmet
    show aaz 41 with dis
    x "Although the staff usually parks on the right side, where there's open space." with dissolve
    mc "Oh... I see."
    mc "I guess it makes sense."
    mc "Are your neighbors pretty friendly?"
    show aaz 42
    x "What neighbors? It’s just my family that lives here." with dis
    x "Well... I guess only half of my family now."
    show aaz 43 with dis
    mc "Okay let me just pause here for a second..." with dissolve
    mc "This entire garage... is yours?"
    show aaz 44
    x "Of course." with dissolve
    show aaz 43
    mc "And... t-those supercars are... yours as well?"with dissolve
    show aaz 44
    x "Well, technically they’re my father’s..."with dissolve
    x "Those are the newest additions though. I don’t know why he even got them... he has dozens more just like them at our Upper Quarter house."
    show aaz 43
    mc "Holy shit! Is your father Jeff Bezos or something?!"with dissolve
    show aaz 44
    x "Look, cut the shit."with dissolve
    x "I’ve had enough people that’ve tried to milk a fake-friendship with me."
    x "You aren’t going to get anything out of this. My father has disowned me and my mother doesn’t speak to me, so it’s not like I even have much to give."
    x "So you can finish your little charade."
    show aaz 46
    mc "What charade?? I don’t have a fucking clue who your father is!"with dissolve
    show aaz 45
    x "...Are you serious?"with dissolve
    show aaz 46
    mc "I swear!"with dissolve
    mc "So you..."
    mc "You really are the daughter of Jeff Bezos! That’s fucking PRIME!"
    x ". . ."
    show aaz 45
    x "My father is William Bardot."with dissolve
    show aaz 46
    mc ". . ."with dissolve
    x ". . ."
    mc "{i}The{/i} W-William Bardot?"
    mc "The largest shareholder of Ulysses and number 6 on the Forbes Billionaire List?"
    x "Mm-hm."
    mc "Y-You're Alexandra Bardot?"
    show aaz 45
    x "Duh."with dissolve
    show aaz 46
    mc ". . ."with dissolve
    mc "...Axel is your brother?!"with hpunch
    show aaz 45
    x "My twin brother."with dissolve
    show aaz 46
    mc "Oh my god, I need to sit down..."with dissolve
    mc "This is..."
    mc "Holy shit! Why didn't anyone tell me?!"
    show aaz 45
    x "Are you serious? You didn’t know already?"with dissolve
    show aaz 46
    mc "I had no idea!"with dissolve
    show aaz 44
    x "Then why did you approach me the other day?"with dissolve
    if alex_points >= 1:
        x "Complimenting my... pen or whatever."
    show aaz 46
    mc "I don't know, I was just trying to be nice!"with dissolve
    mc "That’s what normal people do, you know?!"
    show aaz 45
    x "Well, whether you knew about my family or not, you’re still not getting anything out of this."with dissolve
    x "Like I said, my family doesn’t really give a shit about me."
    show aaz 46
    mc "Yeah, well that makes two of us. I’m not exactly on the best of terms with the Bardot family either." with dissolve
    show aaz 48
    x "You already met Axel?"with dissolve
    show aaz 49
    mc "Yeah, uh..."with dissolve
    mc "We've had a few encounters with each other... and let’s just say we don’t quite get along."
    if axelpunch2:
        mc "We had a little... run-in yesterday."
        show aaz 47
        x "Wait a second... Are you the one who punched him?"with dis
        x "He returned to class yesterday with a bloody nose. That was {i}you{/i}?"
        mc "I had no idea he was your brother, Alexandra. I'm so sorry."
        show aaz 48
        x "*Laughs* No fuckin’ way." with dis
        x "Nice work, [mc]."
        show aaz 49
        mc "R-Really?"with dissolve
        show aaz 48
        x "Most people are too scared of our damn last name to even think about standing up to him."with dissolve
        x "I thought you were just another one of those sheep."
        x "I guess you really can't judge a book by its cover. You're a legit badass!"
        x "So why did you hit him?"
        show aaz 49
        mc "We got into an argument because of Benjamin's sudden death."with dissolve
        if axelpunch:
            mc "And on the first day of school, I saw him harassing a close friend of mine."
            mc "Honestly, I couldn't help it."
        $ alex_points += 1
        play sound "beat.ogg"
        show aaz 48
        show heartr at topleft
        with dis
        hide heartr
        x "Well, I think I respect you a little bit more now because of what you did."with dissolve
    else:
        show aaz 48
        x "Well, I think I respect you a little bit more now because of it."with dissolve
    x "He's a fucking moron."
    show aaz 49
    mc "Thank god I’m not the only one who sees that!"with dissolve
    show aaz 48
    x "Come on, let's go up and start this project before our clothes start to smell like exhaust fumes." with dissolve
    show aaz 49
    mc "Lead the way!" with dissolve
    stop music2 fadeout 4
    scene aaz 50 with Dissolve(2.5)
    play sound doorclose
    x "Okay, well, make yourself comfortable." with dissolve
    play music2b romantic1 fadein 3
    mc "Sure!"
    x "My mother isn’t home, so don't worry about her."
    show aaz 51 with dis
    mc "You have a really nice place here, Alexandra." with dissolve
    x "Meh, if it were up to me, I’d decorate it very differently."
    x "If you want, you can take off your shoes. Just leave them by the doorway."
    x "Do you want something to drink?"
    mc "Nah, I'm good, thank you."
    show aaz 52
    mc "Are you expecting guests?" with dis
    x "Because of the dining table? Nah, it’s always set like that."
    x "Our housekeepers treat this place like a museum. Everything is always positioned perfectly and there’s never a speck of dust anywhere."
    mc "That sounds nice."
    x "It makes me sick."
    mc "Err—Y-Yeah, that's w-what I meant to say."
    x "Come on, grab a seat on the couch."
    play sound chair1
    show aaz 53 with dis
    mc "(This house looks awesome. Everything is so fancy and expensive.)" with dissolve
    play sound2 chair1
    x "*Sitting down* Alright, let's get started." with dis
    show aaz 54
    mc "(And then there's Alex.)" with dis
    mc "(She just seems so out of her element.)"
    x "*Looking at the clock* It's still early. My mother doesn't come back until dark, so we have plenty of time."
    mc "(She clearly doesn't belong here.)"
    show aaz 55
    mc "So just you and your mother live here?" with Dissolve(.8)
    show aaz 56
    x "I’m not giving you my life story. Let’s just get this project over with already."
    show aaz 55
    mc "Come on! How can we work well together if we don’t even know each other?"
    show aaz 56
    x "I prefer knowing nothing about you. It keeps things simple."
    show aaz 55
    mc "Well, you might feel that way, but I like knowing about who I’m working with!"
    show aaz 57
    x "*Sighs* I don't like talking about myself. And we're not even friends, so who gives a shit. We’re just here to do a stupid project about social control." with Dissolve(.8)
    x "And besides, what the fuck do you want to know? My life is a snooze-fest."
    mc "Come on, don't say that!"
    show aaz 55
    mc "There’s something about you that I find, I don’t know... intriguing." with dis
    mc "Like that pink toenail polish. Someone must be hiding a sweet side underneath that tough exterior..."
    show aaz 57
    x "I only u-used that color because I ran out of black!" with dis
    mc "*Laughs* Sure, sure..."
    show aaz 56
    x "You know what? You wanna play that game? Alright, I’ll bite." with dis
    x "You can ask your questions or whatever. Pour your heart out, for all I care. But every time you do, you gotta do an extra 25\% of the project. Deal?"
    show aaz 55
    mc "Okay, sounds good to me."
    show aaz 57
    x "What! You're supposed to say no." with dis
    mc "Too bad, I agreed to your terms. Can’t back out now!"
    show aaz 56
    x "Are you serious?" with dis
    show aaz 55
    mc "Completely."
    show aaz 56
    x "You’re a bigger dummy than I thought. Whatever... less work I have to do. Go ahead then."
    default alexfa = True
    default alexho = True
    default alexre = True
    default alexta = True
    show aaz 55 with dissolve
label alexquestions:
    if not alexfa and not alexho and not alexre and not alexta:
        show aaz 81
        x "I still don't get why you’re so interested." with Dissolve(1.1)
        x "I already told you earlier that my family disowned me. That’s already more than you needed to know."
        x "You would’ve gotten more enjoyment from gargling Axel's balls."
        show aaz 82
        mc "Look, I don't know if you've had a bad experience opening up to someone before, but I promise my curiosity is genuine." with dissolve
        mc "I don't give a shit about your family, or how much money and influence they have."
        mc "I didn't even know you were a Bardot until today."
        mc "I only asked about you because I honestly think you're fascinating."
        $ alex_points += 1
        play sound "beat.ogg"
        show aaz 83
        show heartr at topleft
        with dissolve
        hide heartr
        mc "I’ve been intrigued since the moment I first saw you. I like your style, and enjoy your snark and wit." with dis
        mc "I just want to get to know the real Alexandra. And I’m not sorry for it."
        x ". . ."
        mc "And... are you blushing?"
        show aaz 84
        x "W-What? Of course not." with dissolve
        mc "*Chuckles* Yeah, I think you are."
        x "I'm not."
        mc "I don't know, unless you just magically applied some makeup to your cheeks, I'm pretty sure I just witnessed some blushing."
        mc "Maybe I am getting a little closer to Miss Alexandra’s soft side..."
        x "S-Shut the fuck up!"
        x "I said I wasn’t blushing!"
        play music2 type2 fadein 1
        show aaz 85
        x "Okay, enough of this bullshit! We’ve wasted enough time already." with dis
        stop music2 fadeout 1
        show aaz 86
        mc "You know, I asked 4 questions, so... now I have to do 100\% of the work." with dissolve
        mc "A deal is a deal."
        play music2 type2 fadein 1
        show aaz 85
        x "Shut up." with dissolve
        x "I was kidding. Let’s just get this over with."
        stop music2 fadeout 1
        show aaz 86
        mc "Ah, so there is a kind heart in there after all!" with dissolve
        play music2 type2 fadein 1
        show aaz 85
        x "I told you to shut up. And it’s not even like that. I just don’t want to get an F because of your shitty work." with dissolve
        stop music2 fadeout 1
        show aaz 86
        mc "*Laughs* Fair enough." with dissolve
        mc "Have you come up with any ideas on what we could write about?"
        jump alexposq
    menu:
        with dis
        "[gr]Family" if alexfa:
            $ alexfa = False
            mc "So... tell me about your family." with dissolve
            show aaz 60
            x "Ahhh... I knew this one was coming." with dis
            x "Well, the Bardot family..."
            x "Where should I begin..."
            show aaz 61
            x "My mother Priscilla has never had to lift a finger in her life." with dis
            x "She married at 20 and got knocked up right away to have that easy, stay-at-home mom life. She wasn’t even much of a mother because our nannies did all the work."
            x "She’s never shown even the slightest care toward us. The only things I recall from my childhood are seeing her constantly coming home drunk, and arguing with father because of his repeated infidelity."
            show aaz 62
            x "Then, of course, there's my father... William Bardot himself!" with dis
            x "The Patriarch! The big man! Mr. Money Bags!"
            x "He only cares about money, power, and status. He’s an egotistic manipulator at his core, who won’t hesitate to crush whoever or whatever gets in his way."
            show aaz 63
            x "Last but certainly not least, there’s my sweet, darling of a brother... my beloved twin Axel." with dis
            x "He's like a clone of father. Simply a spoiled rotten psychopath who believes our last name allows him to do whatever he wants, without any consequence..."
            x "...which you seem to have noticed already."
            show aaz 65
            x "We’re not exactly the picture-perfect Brady Bunch family, as you can tell." with dis
            show aaz 64
            mc "Damn, I'm sorry to hear that, Alexandra."
            mc "It probably doesn’t mean much, but I can sort of understand where you’re coming from."
            mc "I never met my mother and my father was always absent in my life. He was constantly too occupied with his work."
            mc "I know what it's like to be alone."
            show aaz 65
            x "Huh... I just assumed you were one of those pampered city boys that’s never known a hard day in his life..."
            x "Thanks, but I’m not seeking anyone’s sympathy. I learned to fend for myself long ago."
            show aaz 64
            mc "(I think I’m starting to understand why she’s so guarded all the time...)"
            jump alexquestions
        "[gr]Hobbies" if alexho:
            $ alexho = False
            mc "So tell me, what do you do for fun?" with dissolve
            show aaz 66
            x "Well, I love swimming. I swim every day."with dis
            x "As soon as I’m in the water, it’s like I forget about everything else. Stress, worries, problems... they all just fade away. It’s where I really find peace."
            x "And I also like to play Eternum."
            show aaz 67
            mc "Oh, you’re an Eternumite too?!"with dissolve
            show aaz 66
            x "Of course, who isn’t nowadays?"with dissolve
            x "With my father being who he is, it’d be more weird if I wasn’t."
            x "To be honest, I almost stopped playing a few years ago out of spite. But really... having a game where you can escape reality and live in a new one? Yeah, I'll take it, thanks."
            show aaz 67
            mc "I recently became an Eternumite myself! Maybe we can play together sometime."with dissolve
            show aaz 66
            x "Um, I don't know... I’ve been very busy lately. Between school, swimming, and working at the cafe, I barely have any free time."with dissolve
            show aaz 67
            mc "Wait... you said you work at a cafe?"with dissolve
            mc "But... aren't you rich?"
            show aaz 68
            x "Ugh, I don't want any of my father's money." with dis
            x "Fuck him and fuck his dirty money."
            x "He thinks he can use that to control me, but I'm not Axel."
            x "I haven't taken a single dollar from him since I was 16."
            show aaz 69
            mc "So the motorcycle..."with dissolve
            show aaz 68
            x "Paid for with MY money."with dissolve
            x "And soon I’m going to leave this place too, once I have enough saved up."
            x "I can't stand being under his roof."
            show aaz 69
            mc "Damn... I don't know if I'd ever have the courage to do that."with dissolve
            mc "That says a lot about you."
            jump alexquestions
        "[gr]Religion" if alexre:
            $ alexre = False
            mc "Are you religious?" with dissolve
            show aaz 58
            x "Who, me? Nah." with dis
            show aaz 59
            mc "Oh, I just noticed your cross necklace and it had me wondering."
            show aaz 58
            x "Yeah, I assumed so."
            x "My grandmother gave it to me for my birthday. She was very devout."
            x "But I'm not, and never was. Our family went to Mass a few times when I was a kid, but it just wasn't my thing."
            x "I don't know if there's life after death, but if that were the case... I doubt that simply attending church on Sundays determines whether a person deserves to go to heaven or hell."
            show aaz 59
            mc "So the cross must have some sort of other significance to you, then?"
            show aaz 58
            x "Um..."
            x "Significance...? No... not at all. You’re reaching with that one. I... just wear it because it looks cool. Plain and simple."
            show aaz 59
            mc "Oh, okay. That’s a valid reason then."
            jump alexquestions
        "[gr]Tattoos" if alexta:
            $ alexta = False
            mc "I know you don't enjoy compliments, but I really like your tattoos." with dis
            mc "How many do you have?"
            show aaz 70
            x "Quite a lot." with dis
            x "Some are a lot older than others."
            x "This was the first one I got... I remember my father getting so pissed off about it."
            x "So I went back to the tattoo parlor a week later and got this other one."
            show aaz 71
            x "And this one here is from my trip to Mexico 3 years ago." with dissolve
            x "As much as I love my tattoos, I don't think I'm gonna get any more. You have to know when to stop."
            show aaz 72
            mc "You also have a few leg tattoos, right? I remember seeing them during swim class." with dis
            mc "Do you have tattoos in any other places?"
            show aaz 73
            x "*Chuckles* Nice try, this isn’t a strip club. I’m not giving you a free show." with dis
            show aaz 74
            mc "*Chuckles* I was just asking..." with dissolve
            show aaz 73
            x "What about you? Any tattoos?" with dissolve
            show aaz 74
            mc "Not yet. But if I had any, I’d definitely show them to you." with dissolve
            show aaz 73
            x "Even if you had one on, like... your ass??" with dissolve
            show aaz 74
            mc "Especially if it was on my ass!" with dissolve
            mc "But hey, I understand that you’re more embarrassed about that kind of stuff. No worries. I just have a lot of confidence in my body..."
            show aaz 73
            x "Huh. You think I’m ashamed of my body or something? Too scared to show off my other tattoos? I promise you, I’m not." with dissolve
            show aaz 74
            mc "I didn’t say that." with dissolve
            x "*Huffing* Hmph."
            mc "I just know that not everyone..."
            play soundlow chair1
            show aaz 75 with dis12
            mc "(Oh boy...)" with dissolve
            play soundlow zip
            pause .7
            play sound2 throw
            show aaz 76 with Dissolve(1.2)
            mc "(HOT DAMN.)" with dissolve
            mc "(That is one beautiful sight!)"
            play sound3 clothes2
            show aaz 77 with dis
            x "There’s this one on my left cheek, but it’s kind of faded away with time." with dissolve
            mc "Uh-huh..."
            x "Since I spend so much time swimming, the ink fades a bit faster due to all that chlorine... or salt, if I’m in the ocean."
            mc "Y-Yeah, yeah, makes sense."
            mc "(Did she get that ass just from swimming?)"
            mc "(Holy shit...)"
            show aaz 78
            x "Then I have these two over here." with dis
            mc "(Oh my god, now I wanna know how far down that one goes...)"
            mc "V-Very nice."
            show aaz 79
            x "And finally, I have this one here on my left calf." with dis
            x "Although it's pretty faded too. All that swimming isn’t doing my ink any favors."
            mc "Yeah, I suppose..."
            show aaz 80
            x "And that’s pretty much it. Hope you enjoyed the show." with dis
            mc "It was very uhh... informative. You have a really nice bod—er, bunch of tattoos."
            play sound2 clothes
            show aaz 75 with Dissolve(1.5)
            play soundlow zip
            pause
            play sound3 chair1
            show aaz 73 with dis
            x "Unfortunately for you, I don’t have any tattoos on my chest. Maybe you would’ve gotten to see those too..." with dissolve
            show aaz 74
            mc "Now that is a real tragedy. Maybe you should show me where you could get one..."with dissolve
            show aaz 73
            x "Nice try." with dissolve
            show aaz 74 with dissolve
            jump alexquestions
        "Let's get to work":
            mc "Alright, I think that’s enough extra work on my plate. Shall we?" with dis
            play music2 type2 fadein 1
            show aaz 85
            x "Finally! Okay, let’s get this thing going..." with dis
            stop music2 fadeout 1
            show aaz 86
            mc "Alright, where should we start?" with dissolve
            play music2 type2 fadein 1
            show aaz 85
            x "I guess we should decide on a topic." with dissolve
            x "Then we can divide the tasks."
            stop music2 fadeout 1
            show aaz 86
            mc "Have you come up with any ideas on what we could write about?" with dissolve
label alexposq:
    show aaz 87
    x "Actually, yes." with dissolve
    x "I liked your idea of investigating a cult."
    mc "Nice! That one interested me the most, too."
    x "Have you heard about a sect in the Netherlands that sacrifices humans to an ancient demon called Calaadia?"
    x "They’re doing this shit now! Like in the 21st century!"
    mc "What the hell! How have I never heard of this?! Tell me everything you know about it!"
    x "*Chuckles* Apparently, they operate in..."
    stop music2b fadeout 5
    show black with Dissolve(2.5)
    pause
    show screen afewhourslater with dis12
    pause
    play music2 tictoc fadein 4
    scene aaz 89
    hide screen afewhourslater
    with Dissolve(2.2)
    mc "That's what I call making good use of time!" with dissolve
    mc "We managed to get a lot done!"
    show aaz 88
    x "Yeah, I hate to admit it, but I guess there’s not just a bunch of empty space in that skull of yours. You’re not that dumb after all."
    show aaz 89
    mc "We’ll definitely get an A!"
    show aaz 88
    x "Maybe."
    show aaz 89
    mc "Well, since we managed to finish everything in one day, I wanted to ask you..."
    mc "You wanna play Eternum together? Let’s say... tomorrow morning? You’ve got all this spare time now!"
    show aaz 90
    x "With a noob like you? Nah, hard pass." with Dissolve(.8)
    show aaz 91
    mc "Come on, I can actually be a valuable teammate! Dalia had her doubts about me too, but then I ended up saving her life... more or less."
    show aaz 90
    x "I'm swimming tomorrow morning. I can't."
    show aaz 91
    mc "After lunch?"
    show aaz 90
    x "Go hang out with Idriel or something... I don’t have the patience for noobs like you. I have something more important to do."
    x "I've been after a special item in the game and I need to keep hunting for it. I think I’m getting close."
    show aaz 91
    mc "Ah, a Gem of Doom?!"
    show aaz 90
    x "Better."
    show aaz 91
    mc "Better than a Gem of Doom? Tell me, tell me!"
    show aaz 90
    x "Even if I told you what it was, it’d be of no value to you."
    show aaz 91
    mc "All the more reason to tell me then!"
    show aaz 88
    x "You're persistent, huh?" with Dissolve(.8)
    show aaz 89
    mc "You could say it’s one of my many strengths..."
    play music2b syndicate fadein 4
    stop music2 fadeout 5
    show aaz 88
    x "*Sighs* Have you heard about the Weapons of Atlas?"
    show aaz 89
    mc "Yeah! Idriel told me about them. Hyas, Dione, and Calypso."
    show aaz 88
    x "Well, I think I know where Calypso is."
    show aaz 89
    mc "You’ve got to be kidding me! Holy shit! We have to go get it!"
    show aaz 88
    x "That's the tricky part. You can't."
    x "Calypso is hidden somewhere on the Ogygia server. But that’s pretty common knowledge for most veteran players."
    show aaz 89
    mc "Okay, so what’s stopping you or anyone else from retrieving it?"
    show aaz 88
    x "That’s the thing. There's no gateway. No point of access. No one has an invitation to that server."
    x "We can't get in."
    show aaz 89
    mc "So... all we have to do is “create” some sort of door to access that server?"
    show aaz 90
    x "If it were that easy, someone would’ve done it already." with Dissolve(.8)
    show aaz 91
    mc "Hmm..."
    mc "Do you remember that crazy girl from earlier? The one with the eye patch?"
    mc "I think she might be able to help us with that."
    show aaz 90
    x "You think just by telling her the server name, she’ll be able to come up with some special spell to access it?"
    show aaz 91
    mc "It's... possible. Something like that. It's worth a try."
    show aaz 90
    x "Alright then, help me find Calypso and then I’ll share it with you."
    show aaz 91
    mc "Deal! By the way, do you know what kind of weapon it is?"
    show aaz 90
    x "No one knows for sure, but... rumor says it's some sort of code."
    show aaz 91
    mc "A... code? Meh, I was hoping it was a lightsaber crossbow or something like that. What good is a code to us?"
    show aaz 90
    x "Think bigger. Imagine a code that allows you to manipulate servers, create new weapons, or even change the laws of nature within any world of Eternum!"
    x "It'd be the ultimate weapon!"
    show aaz 91
    mc "Okay, that sounds good... but you don’t even know if that’s what it really is!"
    mc "What if it’s just a coupon code for 3\% off your next footlong at Subway?"
    show aaz 88
    x "Don't make me regret bringing you along..." with dis08
    show aaz 89
    mc "Okay, okay. Let me do my part. I'll call you tomorrow."
    show aaz 88
    x "Sure. I'll be waiting..."
    play sound keys
    stop music2b fadeout 5
    show aaz 89 with dissolve
    pause .8
    play sound doorclose
    show aaz 92 with dis
    play music2 suspense fadein 4
    x "Aw, shit..." with dissolve
    mc "Hmm?"
    x "*Whispering* It's my mother..."
    x "*Whispering* Please, don’t make a sound! Let’s just sneak down to the garage."
    x "*Whispering* I’m b-begging you!"
    mc "*Whispering* Of course..."
    mc "(She certainly sounds nervous...)"
    show aaz 93 with dis
    pause
    play sound dooropen1
    show aaz 95 with dis
    pause
    show aaz 94
    pris "A-Alexandraaaa...?" with dissolve
    mc "(Her mom seems a little drunk...)"
    pris "Lately it's becoming such a rarity to see you at home."
    pris "Who's this... boy?"
    show aaz 96
    x "He’s nobody. We were just leaving." with dis
    x "I’m not going to be home for dinner."
    play sound chairmove
    show aaz 97 with Dissolve(1.3)
    play sound2 chair2
    pris "Wait, your father is coming upstairs now." with dissolve
    pris "You don't want to give him a kiss?"
    show aaz 97b
    x "W-What? Why is he here?"
    show aaz 97
    pris "He came to sign the divorce papers, darling."
    pris "He isn’t leaving us with anything, you know?"
    pris "Not a single penny. I guess you can get away with whatever you want, if you have the finest lawyers money can buy."
    pris "He is leaving us this apartment, at least. He’ll be living in the big house with your brother."
    pris "I... I told you all of this would happen, Alexandra."
    pris "*Hic* This is all your fault..."
    show aaz 97b
    x "I..."
    x "Come on [mc], let's leave before..."
    play sound doorclose
    pause
    show aaz 98 with Dissolve(1.2)
    pause
    x "*Clenching her fists*" with dissolve
    show aaz 99
    will ". . ." with dis
    show aaz 100
    will "On top of parading yourself with those disgusting tattoos, you decided to start dressing like a fucking whore now, too?" with dis
    show aaz 98
    x "Get out of the way. I have to go."
    show aaz 100
    will "Hmm, where did I go wrong with you...?"
    will "I gave you everything you wanted, provided for all your needs, and now this is how you repay me?"
    will "By humiliating me every day? Being an utter disgrace to the family name?"
    show aaz 98
    x "I’ve been paying for everything myself."
    show aaz 100
    will "Oh, really? Are you paying for the rent? Your tuition? All of your meals?"
    will "You really think you’d make enough money to survive by selling your filthy cunt on the street corner? You have no idea how the real world works, Alexandra."
    show aaz 98
    x "*Voice breaking* I’m working as a waitress."
    show aaz 100
    will "You’re pathetic."
    will "Why can't you be like Axel?"
    show aaz 98
    x "*Voice breaking* J-Just let me through the door..."
    show aaz 100
    will "You should have never been born."
    show aaz 98
    x "*Voice breaking* Please, let me..."
    play sound slap1
    play sound2 slap1
    play sound3 slap1
    show aaz 101
    will "LOOK ME IN THE EYE WHEN I'M TALKING TO YOU!" with hpunch
    menu:
        with dis
        "Keep quiet":
            will "You ungrateful little brat." with dissolve
            play sound doorslam
            show aaz 101b
            x "*Runs off*" with dis
            will "Your one job was to raise these children and you couldn't even do that, Priscilla."
            show aaz 108 with dis
            will "Huh? And who the fuck are you?" with dissolve
            will "Are you one of my employees?"
            show aaz 109
            mc "Um... I... I am... Uh..."
            $ alexpath = False
            $ alexu = False
        "[gr]Say something":
            show aaz 102 with dis
            will "You ungrateful little brat." with dissolve
            mc "Don’t you dare speak to her like that!"
            show aaz 103
            will "Hmm?" with dissolve
            show aaz 104
            will "Excuse me...? I {i}know{/i} you aren’t talking to me like that." with dis
            show aaz 105
            mc "You've got to be the saddest excuse for a “father” that I’ve ever seen in my life." with dissolve
            mc "You're a despicable human being. Now I see why Axel is such a jerk. Like father, like son."
            show aaz 104
            will "WHAT DID YOU JUST SAY TO ME?!" with dissolve
            will "You’re going to regret the day you ran your foul mouth around me, you fucking imbecile. I’ll make damn sure you’re never able to find work again."
            will "What the hell is your name?!"
            show aaz 105
            mc "I don’t work for you. I don’t have to tell you shit." with dissolve
            show aaz 106
            will "You clearly have no idea who you’re speaking to, so let me spell it out for your simpleminded brain."with dissolve
            play sound doorslam
            show aaz 107
            x "*Runs off*" with dis
            show aaz 109
            mc "I know exactly who you are and frankly I couldn’t care less."with dis08
            show aaz 108
            will "What is your goddamn name?" with dissolve
            show aaz 109
            mc "Time will put you in your place." with dissolve
            show aaz 108
            will "I’ve had enough of you..." with dissolve
            will "I'm gonna..."
    show aaz 97
    pris "Are we doing this or not, William?!" with dis
    pris "*Hic* I thought you had business to attend to."
    show aaz 107
    will ". . ." with dis
    show aaz 108
    will "You're not even worth the trouble." with dis
    will "Get the hell out of my sight."
    show aaz 109
    mc "(Asshole...)"with dissolve
    play sound doorslam
    stop music2 fadeout 5
    play music2b garage fadein 5
    if alexpath:
        show aaz 111 with Dissolve(3)
    else:
        show aaz 110 with Dissolve(3)
        mc "Alexandra?!" with dissolve
        mc "(Fuck, she left... I guess she took her bike.)"
        mc "*Sighs* (Think it’d be best if I just went home.)"
        mc "(I'll try to call her tomorrow after I've spoken with Nova about Calypso.)"
        mc "(This isn’t how I wanted to end my Saturday, but oh well... what's done is done.)"
        mc "*Yawn* (I'm really tired...)"
        mc "(Time to go.)"
        jump dream2
    mc "Alexandra!" with dissolve
    show aaz 112 with dis
    mc "Are you okay?!" with dissolve
    mc "I know you told me to stay quiet, and I'm really sorry..."
    mc "But I..."
    mc "I couldn't just stand there and watch how that moron..."
    play sound clothes1
    show aaz 113 with hpunch
    pause
    menu:
        with dis
        "Hug her back [pink][mt](Alex +1)":
            show aaz 114 with dis
            $ alex_points += 1
            play sound "beat.ogg"
            show heartr at topleft with dissolve
            hide heartr
            with dissolve
            mc "(I think it'd be best if I didn’t say anything.)" with dissolve
            mc "(I can’t imagine how it feels to hear your own father say he wishes you were never born.)"
            mc "(I knew their relationship was bad, but I didn’t know it was {i}that{/i} bad...)"
        "Don't hug her back":
            mc "Are you alright?" with dis
    show aaz 115 with dis12
    x "*Clears throat* S-Sorry, I don't know what..." with dissolve
    mc "(Damn, he left a good mark on her cheek.)"
    x "I don’t know what came over me."
    show aaz 116
    mc "It's okay, there’s nothing to apologize for." with dissolve
    mc "Look, I’m not trying to stick my nose into your business, but if you ever need help with anything, someone to talk to, or a place to stay..."
    show aaz 115
    x "Don't worry." with dissolve
    x "It's not the first time something like this has happened. I’m used to it..."
    x "I just need to make it through the next four weeks. As soon as I receive my next paycheck, I’m leaving this damn place and never coming back."
    x "It’s a good thing you never told him your name. I’ve seen him ruin so many lives for much less than what you did."
    show aaz 116
    mc "Can I help you with anything right now? Want me to get you some ice for your face...?" with dissolve
    show aaz 115
    x "No, it's okay. You've done enough." with dissolve
    show aaz 117 with dis15
    x "You should leave now. Your house is pretty far and it's getting late." with dissolve
    x "I'll see you Monday."
    mc "Alright..."
    mc "Take care, Alexandra."
    if alex_points >= 2:
        mc "If you ever need anything at all, please don’t hesitate to call me. I’ll drop whatever I’m doing to be there for you, alright?"
        x "Alex."
        mc "Huh?"
        x "Call me Alex."
        x "My father calls me Alexandra. I hate it."
        mc "*Chuckles* Have I finally earned my place in your exclusive “cool club”?"
        show aaz 118
        x "Don’t let it get to your head." with dis
        x "I just think you’re... bearable."
        show aaz 119
        mc "*Chuckles* Coming from you, that is quite the achievement." with dissolve
        mc "Guess I'll keep chipping away at that tough exterior of yours..."
        show aaz 117
        x "*Laughs* Good luck with that." with dis
        x "Thank you, [mc]."
        x "For everything. I mean it."
    else:
        x "Goodbye, [mc]."
        $ alexpath = False
        $ alexu = False
    show aaz 110 with Dissolve(1.6)
    mc "*Sighs* (Think it’d be best if I just went home.)" with dissolve
    mc "(I can't help feeling bad for her. I wish I could help somehow.)"
    mc "(But there’s not much I can do right now. I'll try to call her tomorrow after I've spoken with Nova about Calypso.)"
    mc "*Yawn* (I'm really tired...)"
    mc "(Let's go...)"
    if alexpath:
        jump predream2
    else:
        jump dream2


label predream2:
    stop music2b fadeout 6
    show aaz 120 with Dissolve(3.1)
    play music2 forgiven
    pause
    x "*Sighs*" with dis08
    show aaz 121
    x ". . ." with dis15
    show aaz 122 with Dissolve(1.4)
    pause
    play sound chair1
    show aaz 123 with dis
    x "And the winner is... Alex Bardot!!!" with dissolve
    x "Unbelievable! Another gold medal added to the pile for Alex! She just became the top American swimmer of all time!"
    show aaz 124
    x "{i}Miss Bardot, congratulations! Would you like to share any words for those young athletes trying to achieve your levels of success?" with dis
    show aaz 125
    x "Well, I'd tell them to work hard every day and never give up on their dreams!" with dissolve
    show aaz 124
    x "{i}What wonderful advice! Congratulations again on your victory!" with dissolve
    show aaz 125
    x "Thank you, thank you!" with dissolve
    play sound keys
    pause 1.5
    play sound2 doorclose
    show aaz 126
    x "Who goes there?! Oh no!" with Dissolve(.7)
    x "It's the wicked, medal-snatching witch! She's come to steal my prize!"
    show aaz 127
    x "So we meet again!" with dis
    x "You’re never gonna take it away from me!"
    x "I’ve stopped you before and I'll stop you again, evil villain!"
    agm "You won't be able to escape me this time, Alex!"
    agm "That medal will be mine!"
    show aaz 126
    x "Not if I use my freezing gun!"
    x "One shot and you'll be frozen forever! Surrender now or else!"
    show aaz 127
    agm "NEVER!!"
    x "You’ve given me no choice!"
    show aaz 128
    x "BANG!" with dissolve
    show aaz 129
    agm "Oh, no! I'm freezing!" with dissolve
    agm "How could she have invented such an amazing weapon?!"
    x "*Giggles* Because I'm a genius!"
    play sound chair1
    show aaz 130
    agm "I guess I’ll just wrap my arms around this genius superhero before I freeze!" with dis
    agm "That way we'll be trapped together forever!"
    x "*Laughs* Let me go! That's cheating!"
    agm "*Laughs* It’s too late! The ice is taking hold! Ahhh!!"
    x "*Laughs*"
    show aaz 131
    agm "Look, honey... I’m afraid I have some bad news." with dis12
    agm "Mommy and Daddy are going to be away for a little bit longer than planned."
    agm "Your father is about to launch the big game he’s been working on for the past few years. So he has to stay in China for a couple more weeks."
    show aaz 132
    x "Whaaat? But tomorrow's my birthday!"
    show aaz 133
    agm "I know, sweetie... I’m sorry, but they won’t be able to make it this year."
    show aaz 132
    x "But only Dad works on that game! Why can't Mommy be here?!"
    show aaz 133
    agm "Because..."
    agm "She's... also busy."
    show aaz 134
    x "That's bullshit! She doesn't even have a job!" with dissolve
    show aaz 135
    agm "Hey! What did I tell you about saying bad words?!" with dissolve
    agm "No swearing!"
    agm "Who taught you those words?"
    show aaz 136
    x "Sorryyyy..." with dissolve
    x "Well, that’s okay then. I don’t need Mom and Dad here!"
    x "All I need is my Mee-Maw!"
    x "You’re gonna be with me forever!!"
    x "Right?!"
    show aaz 137
    agm "Alex..." with dissolve
    agm "I..."
    show aaz 138
    agm "You know what? How about I give you an early birthday present!" with dis08
    agm "My cross!"
    x "Your cross? Why? You never take it off."
    agm "Well, today is a very special day."
    show aaz 139
    agm "Because I want you to have it now!" with dis12
    show aaz 140
    x "But... I don't want it." with dissolve
    x "It's not very pretty... and it’s so heavy!"
    show aaz 139
    agm "It's not about it being pretty, it's about the meaning behind it!" with dissolve
    show aaz 140
    x "And what does it mean?" with dissolve
    show aaz 141
    agm "Alex... there’s going to come a day where I... can’t be around anymore." with dis08
    show aaz 142
    x "What?! Don't say that!" with dissolve
    x "Are you gonna leave me?"
    show aaz 141
    agm "I never will. That's the thing!" with dissolve
    agm "Even if I get sick and you can't visit me, or... I have to go away for a while..."
    agm "I want you to look at this cross and think of me. Remember that I’ll always be there looking after you. That you’ll always have a part of me with you."
    show aaz 142
    x "But Mee-Maw..." with dissolve
    show aaz 141
    agm "And besides! You’re going to be going to school next year and you’ll be so busy playing with all of your new friends!"with dissolve
    show aaz 143
    x "I don't need any friends. I don't like any of the other kids from school." with dissolve
    x "I'm okay with being alone. And when I get tired of that, I have you!"
    show aaz 141
    agm "We all need other people to lean on, Alex." with dissolve
    agm "It's okay to admit we need help sometimes. We can't do it all alone."
    agm "I used to be just like you! I loved being alone and used to think I was doing completely fine, until one day... I met your grandpa."
    agm "And he changed my life."
    agm "I'm sure one day you'll meet your prince too."
    show aaz 144
    x "My prince?" with dissolve
    show aaz 141
    agm "*Laughs* Or your princess, who knows." with dissolve
    agm "But one day, you're going to meet that person who changes your life forever. When that time comes, you’re going to wonder how you ever lived without them."
    show aaz 144
    x "Are you my princess?" with dissolve
    show aaz 141
    agm "*Laughs* No, I'm not. But remember Alex, I'll always be with you. If you ever have your doubts, just look at that cross..." with dissolve
    agm "...And think of me."
    show aaz 144
    x "Where will I find that person?" with dissolve
    show aaz 141
    agm "Who knows." with dissolve
    agm "Maybe you’ll run into them tomorrow! Or at school. Or maybe 20 years from now!"
    agm "But whenever that time comes, you’ll know it in your heart, honey."
    show aaz 145 with dis15
    x "My..." with dis
    x "My prince..."
    show aaz 146
    x "Bullshit..." with Dissolve(.8)
    show aaz 147
    agm "I thought I told you to watch your language, young lady!" with dissolve
    show aaz 148 with Dissolve(2.8)
    pause
    x "(My prince...)" with dis
    show aaz 149
    x "Bullshit..." with dis


label dream2:
    stop music2 fadeout 6
    stop music2b fadeout 6
    scene black with Dissolve(3.6)
    pause
    mc "Hmmm..." with dis
    mc "(Jeez, I passed out right away last night.)"
    play music twinkle fadein 50
    mc "(Fuck, where the hell is the light switch?)"
    mc "(What...)"
    mc "(What's that sound?)"
    show aaw 1 with Dissolve(2.5)
    pause
    mc "(What the...)" with dissolve
    mc "(Where the hell am I?)"
    mc "(Is that a road? Fuck, don't tell me I’ve been sleepwalking...)"
    mc "(I'd better go towards that light and see if I can get my bearings...)"
    show aaw 2 with Dissolve(3)
    mc "(This road seems to have no end. Am I even in Kredon anymore?)" with dissolve
    mc "(If I see a car ahead, I should probably try to...)"
    lad "Will you help us?"
    show aaw 3
    mc "(Holy fuck! Where the hell did she come from?!)" with dis
    show aaw 4
    mc "Miss! Do you know where we are?" with dis
    mc "I’m not really sure how I got here..."
    lad ". . ."
    mc "(W-Why isn’t she answering?)"
    mc "Um, Miss?"
    lad ". . ."
    mc "(Okay, this is creeping me out.)"
    mc "Uh... I'm just gonna keep walking and see if..."
    play sound glitch2
    show glitch6
    pause 1.5
    mc "*Hyperventilating* W-What the fuck is going on..." with dis
    lad "Will you help us?"
    scene aaw 6 with dis
    mc "W-What?" with dissolve
    lad "Will you help us?"
    mc "Who are you?"
    lad "Will you help us?"
    mc "H-Help you?"
    menu:
        lad "Will you help us?"
        with dis
        "[gr]Yes":
            $ helpdream2 = True
            mc "Y-Yes, um... I’ll try!" with dis
        "No{#0.2,lady}":
            $ helpdream2 = False
            mc "N-No! I don’t even know what’s going on!" with dis
    lad "We need your help."
    mc "My help? B-But why me? I'm not anyone special!"
    lad ". . ."
    lad "Special."
    lad "Is anyone special?"
    mc "What?"
    play musicb deception
    lad "Wolves and sheep."
    lad "Rich and poor."
    lad "Emperors and peasants."
    lad "Masters... and slaves."
    lad "Kings..."
    lad "...and pawns."
    lad "When the game is over... they all go back into the same box." with dis
    mc ". . ."
    mc "But that’s the same with life, isn’t it? There comes a time for everyone."
    mc "That's what makes us human. There’s nothing we can do to stop it."
    lad "Ahh..."
    play sound glitch2
    show glitch7
    pause 1.4
    mc "F-Fuck!" with dissolve
    hide glitch7
    show aaw 8
    lad "That's where you're wrong, [mc]." with dis
    mc "W-What?"
    play sound risingshort
    show aaw 7 with Dissolve(1.1)
    play sound2 thunder
    stop music
    stop musicb
    pause .14
    show aaw 9 with flashfaster
    play music2 rain3 fadein 5
    mc "AAAAAAARGHHH!" with hpunch
    mc "FUCK!"
    play soundlow clothes
    show aaw 10
    show sunday
    mc "(Oh my fucking god, that was terrifying!)" with Dissolve(1.2)
    mc "(I’ve never had a nightmare like that before...)"
    mc "(I hardly ever dream in the first place...)"
    mc "(Well, at least it's over...)"
    mc "(Okay, time to pull myself together.)"
    play sound chair3
    scene sc 3 with dis
    mc "*Yawns* (It's still pretty early, but I might as well just get up now.)" with dissolve
    scene aaw 11 with Dissolve(2.5)
    mc "Ahhh..." with dissolve
    mc "(Nothing like a nice cup of coffee on a cold, rainy morning.)"
    play sound chair2
    show aaw 12 with dis
    if penelopepath:
        mc "(Penelope should be waking up here soon.)" with dissolve
        mc "(I'm pretty excited for our photoshoot together.)"
        mc "(I'm no expert, but with how photogenic she is, it’s probably impossible to take a bad picture of her anyways.)"
    else:
        mc "(I have literally nothing to do today. I could get used to this!)" with dissolve
        mc "(Perfect Sunday!)"
    show aaw 13
    mc "(Oh, I should ask Nova about Calypso and see if she’s heard of that server Alex told me about.)" with Dissolve(.8)
    mc "(Maybe she knows a way to get access to it.)"
    menu:
        with dis
        "Call her [pink][mt](Nova +1)":
            mc "(I hope she won’t get nervous if I call her so soon. I know she’s still trying to get used to having a phone.)" with dis
            show aaw 14 with dis
            mc "(Let's see if she answers...)" with dissolve
            play sound phone2
            pause 1
            play sound hangup
            play soundlow slam
            show phonenova1
            pause 0.05
            $ unlock_look("nova", 1)
            hide phonenova1
            show aaw 15
            no "[mc]!!!{w=0.8}{nw}" with hpunch
            play music2b happy7 fadein 10
            stop music2 fadeout 10
            no "[mc]!!!"
            no "Good morning!"
            show aaw 16
            mc "Damn! You picked up fast!" with dissolve
            show aaw 17
            no "Yeah! I just happened to be looking at my phone and then you called!"with dissolve
            no "I guess these things are more handy than I thought!"
            show aaw 16
            mc "So you really haven’t had a cell phone at all, until now?" with dissolve
            show aaw 17
            no "Yeah, I feel like I've been missing out on so much. I even downloaded a game yesterday and ended up playing all night!" with dissolve
            show aaw 16
            mc "So you bought your first ever phone... all because of me??" with dissolve
            show aaw 17
            no "I m-mean... I wouldn’t say that exactly, but umm... I guess..." with dissolve
            no "...It was purely for the investigation! Y-Yeah! That’s right."
            show aaw 16
            mc "Uh-huh, the investigation, hmm...?" with dissolve
            mc "Well aren't you worried about someone spying on you? Through the phone?"
            show aaw 17
            no "Of course not! I eliminated all of the attack vectors I could think of! It’s practically hack-proof." with dissolve
            no "Every call or message has end-to-end encryption and all my web traffic is tunneled through a private VPN. It's the most secure line in the world!"
            play sound chair1
            show aaw 18
            no "Anyway, what can I help you with, Mr. [mc]?" with dis
            show aaw 19
            mc "Well, I wanted to ask you something, and I thought a call would be a little more personal than a text." with dissolve
            $ nova_points += 1
            play sound "beat.ogg"
            show aaw 18
            show heartr at topleft
            with dissolve
            hide heartr
            no "Oh... W-Well, thank you!" with dissolve
            no "Seeing you calling was a pleasant surprise!"
            no "I mean... I'm still in my pajamas and I haven't even done my hair yet. It’s so messy..."
            mc "(Yeah, she definitely hasn’t received a phone call in her life. It's so cute.)"
            show aaw 19
            mc "You know I can't see you, right?" with dissolve
            show aaw 20
            no "Of course I know that, dummy!" with dissolve
            no "I'm not stupid!"
            show aaw 19
            no "I meant that I just got up." with dissolve
            no "I was whippin’ up some waffles."
            mc "Oh, that sounds delicious! I’m just enjoying my morning coffee."
            mc "Is it raining over there too?"
            play soundlow thunder
            show aaw 21
            no "Yeah, hasn’t stopped since midnight." with dis
            no "Kredon isn’t really that big. If it’s raining on one side of town, it’s probably raining on the other too."
            show aaw 22
            no "Anyway, what did you want to ask me?" with dis
            show aaw 23
            mc "Ah, yeah, remember the girl who picked me up yesterday?" with dissolve
            show aaw 22
            no "Yeah! The one with the badass crotch rocket!" with dissolve
            show aaw 23
            mc "Turns out she knows the location for one of the Weapons of Atlas!" with dissolve
            show aaw 24
            no "What? Are you serious?" with dissolve
            no "Which one was it? Calypso?"
            no "The server-shaper?"
            show aaw 25
            mc "Yeah, that one! I see you know about it already." with dissolve
            show aaw 24
            no "Of course! I know all about the three ultimate weapons." with dissolve
            no "The sword Hyas, the sniper Dione, and finally, Calypso."
            no "I’ve been trying to get my hands on them for a long time."
            show aaw 25
            mc "The Eternum Lady, Idriel, told me that Hyas was missing and Dione is already in the hands of a player. Delilah something..." with dissolve
            show aaw 24
            no "Delilah Warren!! Have you heard about her? S-She's awesome, right?!" with dissolve
            show aaw 25
            mc "I don’t know much about her. Do you know her?" with dissolve
            show aaw 24
            no "Um... s-something like that. I'll introduce you to her sometime!" with dissolve
            no "Anyway, as I was saying, Calypso is the most powerful weapon of the three. Nobody has been able to find it."
            no "No one knows exactly what kind of weapon it is, but it’s rumored on some servers to be a sort of server-shaper."
            show aaw 25
            mc "Yeah, Alex said it's a code that allows you to create things in Eternum, or something like that." with dissolve
            show aaw 24
            no "A CREATION CODE! Of course!" with dissolve
            no "That would definitely make it the ultimate weapon in any game!"
            no "It makes sense!"
            show aaw 25
            mc "The problem is that it's hidden in a server that we can't access. It's called... Ogygia." with dissolve
            mc "Do you know of a way we could get in?"
            show aaw 26
            no "Accessing a server? Leave it to me!" with Dissolve(.8)
            show aaw 27
            mc "I knew I could count on you. My favorite hacker!" with dissolve
            show aaw 26
            no "Just give me a few hours. I have a few exploits in mind that I want to try out. I'll call you back!" with dissolve
            show aaw 27
            mc "Awesome!" with dissolve
            show aaw 28
            mc "Oh, by the way, if you do manage to find a way in, we’ll have to bring Alex along." with dissolve
            mc "She's the one who discovered its location, so she definitely deserves to come."
            show aaw 29
            no "Of course." with dissolve
            no "The more the merrier..."
            show aaw 31
            no "Anyway, I should get to work."  with Dissolve(.8)
            show aaw 32
            mc "Alright, thanks for all your help, Nova. I’ve really been putting you to work lately!" with dissolve
            mc "And don't worry, there's no rush. Take as much time as you need!"
            mc "If I can help out somehow, let me know."
            show aaw 34
            no "Sure!" with Dissolve(.8)
            no "Maybe we can grab a bite at Luna’s cafe sometime soon."
            no "We can talk about the last season of Jujutsu Kaisen. I also watched the last episode yesterday!"
            show aaw 33
            mc "What do you mean, \"also\"?" with dissolve
            mc "Did you hack my laptop again?"
            show aaw 34
            no "O-Of course not!" with dissolve
            no "I just assumed that..."
            show aaw 35
            no "Well, it's a very popular show, and..." with Dissolve(1.2)
            no "W-What the... is that smoke?"
            mc "What smoke?"
            play music2 firealarm
            stop music2b fadeout 8
            no ". . ."
            mc "W-What's that noise?"
            mc "Is that a fire alarm?"
            play sound chair1
            play music2b punk1
            show aaw 37
            no "OH, FUCK!" with hpunch
            no "MY WAFFLES!" with hpunch
            play sound2 doorslam
            show aaw 36
            san "NOVA?!" with hpunch
            san2 "OH JESUS CHRIST, WHY IS THE KITCHEN ON FIRE?!" with hpunch
            no "S-Sorry, I was making waffles, but then I received a phone call and..."
            san2 "WHAT THE HELL ARE YOU TALKING ABOUT! YOU DON'T EVEN HAVE A CELL PHONE!!" with hpunch
            no "I d-do now! I..."
            san2 "HURRY UP AND GO BRING ME THE FIRE EXTINGUISHER!" with hpunch
            no "Y-Yes!"
            san2 "SANDRA, I NEED A BLANKET!" with hpunch
            san "ON IT!"
            san2 "OH MY GOD, WE JUST BOUGHT THAT FRIDGE!" with hpunch
            show aaw 37
            no "Erm..." with dis08
            san2 "NOOOOO! NOT MY LUCKY OVEN MITTS!" with hpunch
            no "I'LL CALL YOU LATER! SEE YA!"
            play sound3 hangup
            stop music2b
            play music2 rain3
            show phonenova2
            pause 0.05
            scene aaw 38
            pause
            show aaw 39 with Dissolve(1.2)
            mc "(Jesus, I hope they're alright.)" with dissolve
            mc "*Laughs* (That girl is definitely something else.)"
            mc "(Never a dull moment with her.)"
        "Send her a message":
            mc "(I don’t want to make her nervous if I call. I know she still isn’t used to having a phone.)" with dis
            mc "(I'll just text her.)"
            play music2b celltype
            mc "*Typing* Hi Nova! Sorry to bother you, but my friend Alex just told me about a server that might be hiding a Weapon of Atlas... Calypso. Do you know anything about that?"
            no "{i}[mc]! So glad you texted me!"
            no "{i} Yeah, of course I do!"
            mc "*Typing* The thing is, we don’t know much else about it. So I thought maybe you could help us with your... \"hacking\" abilities."
            no "{i}For a Weapon of Atlas? Hell yeah! I can do some investigating. Do you know what the server is called?"
            mc "*Typing* Ogygia. But Alex said there's no way to access it."
            no "{i}Leave it to me! I have plenty of Eternum exploits that I can try. Give me a few hours."
            mc "*Typing* OKAY!! Thanks, Nova!"
            no "{i}I'll call you later!"
            stop music2b
            show aaw 12
            mc "(That went well. I thought she'd be much more paranoid about using a phone. She must’ve configured hers to be extra secure.)" with dis
    if penelopepath:
        play sound dooropen3
        pause 1
        play sound2 doorclose
        p "Good morning, [mc]!" with dissolve
    else:
        mc "(Guess I'll finish my coffee and then go watch a show while I wait for Nova's call.)"
        mc "(I really want to play Eternum, but I’d rather just wait to play with one of the girls. I don't wanna join the wrong server and end up dying in a fight, or something.)"
        jump novacallnopenny
    $ unlock_look("penelope", 4)
    show aaw 40
    mc "Penny! Good morning!" with dis
    mc "Whoa, I love your hair today! And your outfit!"
    show aaw 41
    p "Thank you! I'm glad you like it." with dis
    p "All that humidity outside better not turn my hair into a frizzy mess, though!"
    p "Hope you didn’t forget our photoshoot today!"
    show aaw 42
    mc "Of course not!" with dis
    mc "Do you think I got all dolled up for nothing?"
    show aaw 43
    p "*Giggles* Yeah, true, I noticed your stylish jersey." with Dissolve(.25)
    p "I'm not sure about your hair, though. If you were going for the bedhead look, you definitely achieved it."
    show aaw 42
    mc "My hair is a wild beast that cannot be tamed."with Dissolve(.25)
    show aaw 43
    p "I'll take you to my hairdresser one day. He's a good friend of mine."with Dissolve(.25)
    show aaw 42
    mc "*Laughs* No, thanks!"with Dissolve(.25)
    mc "Is he the same guy who was gonna be your photographer today, instead of me?"
    show aaw 43
    p "No, that's Philippe, who you’ll get to meet at the studio later. He works there."with Dissolve(.25)
    show aaw 42
    mc "Ah, cool. Do you know him just from the studio? Or do you guys go to college together?"with Dissolve(.25)
    show aaw 43
    p "I first met him during a photo shoot last year."with Dissolve(.25)
    p "He's actually my boyfriend."
    show aaw 42
    mc "I see."with Dissolve(.25)
    mc "W-Wait..."
    mc "I'm sorry, he’s w-what?"
    show aaw 43
    p "My boyfriend."with Dissolve(.25)
    show aaw 42
    mc "Y-You have a boyfriend?"with Dissolve(.25)
    show aaw 44
    p "Is that a hint of jealousy, I’m sensing?"with dissolve
    show aaw 42
    mc "N-No..."with dissolve
    mc "I mean... it's just that... the other night at the cafe, you mentioned you were single."
    show aaw 44
    p "I lied."with dissolve
    p "I like to keep my private life... private."
    show aaw 42
    mc "Oh..."with dissolve
    mc "And uh..."
    mc "This Philippe..."
    show aaw 44
    p "You’ll meet him soon enough. Then you can ask him all the questions you want. Shall we?"with dissolve
    show aaw 42
    mc "Sure... l-let's go."with dissolve
label photoshootpenny:
    stop music2 fadeout 4
    show black
    with Dissolve(3)
    pause
    show screen afewminuteslater with dis12
    pause
    scene aaw 45
    hide screen afewminuteslater
    with Dissolve(2.5)
    play music2b photoshot fadein 6
    p "Alright, this is the studio." with dissolve
    p "Maybe we're too early..."
    mc "(Man, I can't believe she has a boyfriend.)"
    mc "(I mean... not that I care... or even had any chance, but still...)"
    show aaw 46
    p "This studio is my absolute favorite." with dis
    p "The equipment they use here is of the highest quality!"
    show aaw 47
    mc "Mm-hm..."
    mc "(Of course she has a boyfriend. Have you even seen the way she looks, [mc]?)"
    show aaw 46
    p "I was only able to get a half-hour time slot. Every other time was fully booked."
    show aaw 47
    mc "Uh-huh..."
    mc "(It's not like I was expecting her to wait for me like a nun, but... just imagining some guy banging her... ugh.)"
    show aaw 46
    p "It's almost impossible to get an appointment here, but Philippe was able to pull a few strings and get us a booking!"
    show aaw 47
    mc "What a champ..."
    mc "(What was I expecting? She’s a popular Instagram model for god’s sake!)"
    mc "(Way out of your league.)"
    mc "(But still... Fuck, why am I so upset?)"
    play sound dooropen3
    show aaw 48 with Dissolve(1.2)
    phi "Oh my god, darling!" with dissolve
    phi "Citizens of Kredon! May I have your attention please?! Your most beautiful goddess, my gorgeous girlfriend, has finally arrived!"
    phi "How can you shine so much, sweetie? I’m going to start wearing my sunglasses around you!"
    show aaw 49
    p "Philly! How's everything going?" with dis
    show aaw 50
    phi "So much better now that you’ve returned to me, my fabulous little doll!"
    phi "What spell of beauty did you cast on your hair?! Teach me, teach me, you luscious wizard!"
    show aaw 49
    p "I used that new hairspray you recommended to me."
    show aaw 50
    phi "Just look at those gorgeous curls! We’re gonna need to get you in the studio ASAP before I gobble you all up! Can’t wait to take your pictures!"
    show aaw 49
    p "Aww! Well today you’re off the hook, remember?"
    p "[mc] here is gonna be my photographer this time."
    show aaw 50
    phi "Huh?"
    show aaw 51
    phi "Ahhh... yeah, that’s right. [mc]..." with dis
    phi "Goodness me! Would you look at that! Penny, you said you were bringing over a photographer... not a STALLION!"
    show aaw 53
    mc "Um..." with dis
    mc "T-Thanks?"
    show aaw 52
    phi "And he seems quite fit too..."
    phi "He could have a future as a model."
    phi "Can you take your shirt off? Do a little twirl for me?"
    show aaw 53
    mc "What? Do I have to?"
    show aaw 52
    phi "Maybe as an underwear model..."
    phi "How big are you down there, pretty boy? You’ve {i}got{/i} to be packing something dangerous..."
    show aaw 53
    mc "Um..."
    show aaw 49
    p "*Laughs* Come on Philly, go easy on him! What would Paul say?"
    show aaw 55
    phi "Oh god please, don't tell him! With how jealous he gets..."
    phi "Alright then, you can do a little dance for me later, [mc]. Come on in, sweeties!"
    phi "You have the whole studio all to yourselves until 12:00. Then Mr. Valentino has it booked for the rest of the day."
    show aaw 49
    p "Wow, Valentino?!"
    show aaw 55
    phi "That's right, my tulip! He's coming by later today. Be sure to take some good photos if you want to impress him."
    show aaw 49
    p "We'll try!"
    show aaw 54
    phi "I hope you're a good photographer, [mc]. My queen here deserves only the best!"
    phi "I'll stop yammering on though and leave you both to it. Ta ta!"
    show aaw 46 with Dissolve(1.3)
    p "Come on, let's go inside! We’re already on the clock!" with dissolve
    show aaw 47
    mc "Erm... S-Sure!"
    play sound doorold
    show aaw 56 with Dissolve(1.4)
    pause
    mc "Whoa, this place looks like the real deal!" with dissolve
    show aaw 57 with dis
    p "Of course, because it is!" with dissolve
    mc "Are we free to use anything in here?"
    show aaw 58
    p "Most definitely!" with dis
    p "As long as we don't break anything, of course."
    show aaw 60
    mc "*Chuckles* I'll try not to." with Dissolve(.75)
    mc "Alright, let’s get down to business! I think I’ll have to adjust the lights a bit though."
    show aaw 59
    p "I can do it, no worries."
    p "While I work on that, would you mind grabbing me something from the refreshment table?"
    show aaw 60
    mc "Sure, no problem!"
    mc "What do you want?"
    show aaw 59
    p "Surprise me! The table should be over by the entrance."
    p "Feel free to take whatever you want for yourself as well."
    show aaw 60
    mc "Cool! I'll go take a look. Be right back!"
    play sound doorold
    show aaw 61 with Dissolve(2)
    mc "(Ah, here it is.)" with dissolve
    show aaw 62
    mc "(Looks like they’ve got coffee and donuts.)"with dis
    mc "(Damn, those donuts look so good.)"
    default coffeepe = False
    $ sugarpe = 0
    menu:
        with dis
        "Get a donut for Penelope":
            mc "(I'm sure she’d love one. Who isn’t a fan of donuts?)" with dissolve
        "[gr]Get a coffee for Penelope":
            $ coffeepe = True
            mc "(I should get her a coffee to help her stay focused during the shoot.)" with dissolve
            play sound coffee
            menu:
                with dis
                "1 teaspoon of sugar":
                    $ sugarpe += 1
                "2 teaspoons of sugar":
                    $ sugarpe += 2
                "[gr]3 teaspoons of sugar":
                    $ sugarpe += 3
            mc "(This will do.)" with dissolve
    phi "Mr. Valentino! My apologies, but the studio is still taken until noon."
    show aaw 64
    mc "(Huh?)" with dis
    val "What?!"
    show aaw 63
    phi "You arrived a little early, sir. You have the place booked from 12 to 6." with dis
    show aaw 64
    val "This is ridiculous!"with Dissolve(.8)
    val "*Sighs*"
    val "Bah, whatever..."
    val "I'll just wait."
    play sound slap1
    play sound2 slap1
    play sound3 slap1
    show aaw 65
    val "If you need me, I'll be in the booth getting measurements of my model..." with vpunch
    val "30 minutes should be enough... Am I right, honey?"
    play sound4 doorold
    show aaw 51 with Dissolve(1.5)
    phi "Oh, dear..." with dissolve
    mc "Is that the Valentino fella you mentioned earlier, Philippe? What does he do?"
    phi "He's the best fashion agent in the country. Or at least... one of the best."
    show aaw 52
    phi "He's an asshole, but if he likes you, he can make your modeling career take off."with dis
    phi "I wanted to show him some pics of Penny later."
    show aaw 53
    mc "Oh... I see. Then I’ll make sure you’ll have plenty of nice pictures to choose from."
    mc "Time to head back inside!"
    show aaw 54
    phi "Sure thing. Good luck and have fun, darling!" with Dissolve(.8)
    show aaw 61 with Dissolve(1.5)
    mc "(Hmm... I'm gonna grab a donut for myself as well.)" with dis
    mc "(Or maybe two...)"
    mc "(Or I could just sneak off with the entire basket...)"
    play sound doorold
    show aaw 66 with Dissolve(1.5)
    mc "*Stuffing face with donuts* Mmm... I'm back!" with dissolve
    if not coffeepe:
        mc "I brought you a donut!"
        show aaw 67
        p "A... donut?" with dis
        mc "With extra chocolate! White chocolate!"
        p "But... isn't this pretty fattening?"
        mc "Well, the only other thing they had was coffee. I figured you would’ve preferred something to eat."
        p "Yeah but I can’t afford too many empty calories..."
        mc "But it tastes good!"
        show aaw 68
        p "Uhm... yeah, thanks I guess. I’ll probably just eat it later..." with dis
        mc "(Oops, should’ve went for the coffee.)"
        p "We should start, we only have 25 minutes left."
    else:
        mc "I brought you a coffee!"
        show aaw 69
        p "Ah, nice!" with dis
        p "I love coffee!"
        p "How many teaspoons did you put?"
        mc "[sugarpe]."
        if sugarpe == 3:
            p "Ah, yes! Just what I needed!"
            mc "I remember you mentioned preferring 3 teaspoons."
            $ penelope_points += 1
            play sound "beat.ogg"
            show heartr at topleft with dissolve
            hide heartr
            p "Exactly right!" with dissolve
            show aaw 71
            p "Someone is a good listener... thank you for remembering!" with dissolve
        else:
            show aaw 71
            p "That'll do. Thank you." with dissolve
        show aaw 70
        mc "Anytime!" with dissolve
        mc "So..."
        mc "This boyfriend of yours..."
        mc "Philippe..."
        mc "He seems a bit..."
        show aaw 71
        p "*Laughs* Gay, right?" with dissolve
        show aaw 70
        mc "*Laughs* Yeah, sorry to break the bad news to you."with dissolve
        show aaw 71
        p "*Giggles* No, but seriously, he's been a really good friend. I met him and his husband Paul last year. They always help me find auditions. He always calls me his “girlfriend”." with dissolve
        show aaw 70
        mc "He seems like a nice guy."with dissolve
        show aaw 71
        p "He is!" with dissolve
        show aaw 70
        mc "So..."with dissolve
        mc "You don’t have a {i}real{/i} boyfriend then...?"
        show aaw 72
        p "...No. My last \"boyfriend\" was in high school, and... that relationship didn’t last very long."with Dissolve(.8)
        p "I decided to focus on more important things when I started college."
        show aaw 70
        mc "(Why do I feel so relieved all of a sudden?)" with dissolve
        mc "(Wake up [mc], we're talking about Penelope here. Still not gonna happen.)"
        show aaw 72
        p "Anyway, we should start taking some photos, don't you think?" with dissolve
    show aaw 73
    mc "Sure! Where do you wanna pose?" with dis
    p "Well, since this stuff is already set up, we might as well use it."
    mc "I agree. I like the look of this scene."
    show aaw 74
    p "Yes, it has a very modern and open feel to it." with dis
    mc "(Oh Jesus.)"
    p "And the black and white colors complement my attire."
    show aaw 75 with dis
    mc "Y-Yeah." with dis
    mc "Is this a lingerie photoshoot or something?"
    show aaw 77
    p "Oh, well, not entirely." with dis
    p "But since I’m sponsored by this brand, I have to show off their bra in at least a few photos."
    mc "...Yeah, that makes sense."
    mc "(Must... not... stare...)"
    mc "That’s a nice bra."
    show aaw 76
    p "Thanks. This brand has been sponsoring me for around four months now. I’ve also had to model their bikini line before."with dis
    p "I don't know if you remember seeing those pics on my Instagram profile."
    mc "(Remember them? I fuckin’ worshipped those pictures...)"
    mc "Hm, I think I vaguely remember... yeah..."
    play sound chain
    play sound2 chair4
    show aaw 78 with dis
    p "Well, time for you to do your thing." with dissolve
    p "Do you know how to focus the lens?"
    play sound zoomin
    show aaw 79 with Dissolve(.8)
    mc "Know how to focus?" with dissolve
    mc "Are you doubting my skills here? I’ll have you know, my focus skills are magical. Time for my first spell... FOCUS POCUS!"
    show aaw 79b
    p "*Laughs* Come on, don't make me laugh!" with dis
    mc "*Chuckles* I’ll take any opportunity to see that smile!"
    show aaw 79
    mc "Okay, okay, now let’s both FOCUS here! No more silliness..." with dis
    play sound camera
    show black
    pause 0.08
    hide black
    pause
    show aaw 80
    p "Does the lighting look okay? How are the shadows?" with dissolve
    show aaw 81
    mc "It all looks good to me."
    mc "Although... I think the shorts are a bit distracting."
    show aaw 80
    p "The shorts? What do you mean?"
    show aaw 81
    mc "Like, they stand out too much against the other muted colors."
    mc "I could try to just shoot only your upper body."
    mc "(Gotta tread carefully here... don’t want to come off sounding like a pervert.)"
    show aaw 80
    p "Hmm... No, I definitely think it’s important to show off a little bit of leg in these pictures too."
    play sound chain
    play sound2 chair4
    show aaw 82 with dis
    play sound3 clothes
    p "How about I just..." with dissolve
    play sound4 clothes2
    show aaw 83
    p "There. Good call, [mc]. I definitely think the bright blue jeans were out of place." with dis
    p "Or... maybe someone was just trying to take advantage of me..."
    mc "Come on Penny, you know I'd never do that."
    p "Yeah..."
    p "I'm sorry. I’ve just had so many photographers and managers that have been total creeps. It’s really disheartening."
    mc "I can imagine."
    p "But that’s why I’m glad to have you here, [mc]."
    mc "(Maintain eye contact [mc], you can't afford to look bad now...)"
    play sound chain
    show aaw 84
    p "This thing will support my weight, right?" with dis
    mc "(Wow...)"
    p "It looks like it’s only being held up by one nail..."
    mc "I doubt it's gonna fall. How much do you weigh?"
    play sound chain
    play sound2 chair4
    show aaw 85 with dis
    p "Hey, you can't ask a lady that!" with dissolve
    mc "*Chuckles* My bad."
    p "How does it look now?"
    play sound zoomin
    show aaw 86 with Dissolve(.8)
    mc "Much better." with dissolve
    play sound camera
    show black
    pause 0.08
    hide black
    pause .5
    mc "Can you pull your hair back?" with dissolve
    mc "So your bra is more visible?"
    show aaw 87
    p "Sure, good idea." with dis
    show aaw 88 with dis
    mc "Ohhh yeah, beautiful!" with dissolve
    mc "Okay, let me try another angle..."
    show aaw 89
    mc "Perfect..."with dis
    mc "I must be a natural at this!"
    mc "Just a bit of zoom..."
    play sound zoomout
    show zoomout1
    pause .5
    mc "Oh shit." with dis
    mc "Um..."
    play sound2 zoomin
    scene zoomin1
    pause .3
    play sound3 zoomout
    scene zoomout1
    pause .5
    mc "Erm..." with dis
    mc "(Damn it, I got too cocky. How the fuck does this camera work?)"
    play sound zoomin
    scene zoomin1
    pause .5
    mc "Ah, now I got it." with dis
    play sound zoomin
    show zoomin2
    pause .5
    mc "Ah, no I don’t." with dissolve
    mc ". . ."
    mc "...Or do I?"
    play sound zoomout
    show zoomout2
    pause .5
    mc "Hmmm..." with dissolve
    play sound2 zoomin
    scene zoomin2
    pause .3
    play sound3 zoomout
    scene zoomout2
    pause .5
    mc "Ah, okay, now I got it for real." with dissolve
    menu:
        with dis
        "Take the photo with zoom in":
            play sound3 zoomin
            scene zoomin2
            pause .5
            mc "Ahh... This is {i}definitely{/i} a keeper." with dis
            mc "No doubt."
            play sound camera
            show black
            pause 0.08
            hide black
            pause 0.3
            play sound camera
            show black
            pause 0.08
            hide black
            pause 0.08
            play sound2 camera
            show black
            pause 0.08
            scene aaw 91b
            pause
            scene reflex1 with Dissolve(.1)
            pause
            p ". . ." with dis
            scene aaw 93
            p ". . ."
            show aaw 94
            mc "I thought it would be more... artistic." with dis
            p ". . ."
            mc "O-Okay, w-we can take another."
            show aaw 95
            p "And you better do it right this time." with dissolve
        "Take the photo with normal zoom [pink][mt](Penelope +1)":
            mc "Now that’s a good one." with dissolve
            play sound camera
            show black
            pause 0.08
            hide black
            pause 0.3
            play sound camera
            show black
            pause 0.08
            hide black
            pause 0.08
            play sound2 camera
            show black
            pause 0.08
            scene aaw 89b
            pause
            scene reflex2 with Dissolve(.1)
            pause
            mc "What do you think?" with dis
            scene aaw 96
            p "Whoa, it looks great!"
            p "I love that angle, very nice."
            $ penelope_points += 1
            play sound "beat.ogg"
            show heartr at topleft
            show aaw 97
            with dissolve
            hide heartr
            p "I might need you to be my photographer more often, [mc]!" with dis
            p "Do you think we can take a few more?"
        "Take the photo with zoom out":
            play sound3 zoomout
            scene zoomout1
            pause .5
            mc "Ahh... Yeah, this one... *Chef’s kiss*" with dis
            mc "In order for an artist to innovate, they must first take risks."
            mc "Now this is cutting edge!"
            play sound camera
            show black
            pause 0.08
            hide black
            pause 0.3
            play sound camera
            show black
            pause 0.08
            hide black
            pause 0.08
            play sound2 camera
            show black
            pause 0.08
            scene aaw 90b
            pause
            scene reflex3 with Dissolve(.1)
            pause
            p ". . ." with dis
            scene aaw 93
            p ". . ."
            show aaw 94
            mc "I thought it would be more artistic." with dis
            p ". . ."
            mc "O-Okay, w-we can take another."
            show aaw 95
            p "And you better do it right this time." with dissolve
    show aaw 98
    mc "Absolutely!" with dis
    mc "I think I'm getting the hang of it!"
    mc "It really helps that you’re a natural at posing too. You’re doing all this so effortlessly!"
    mc "Ah! Quickly, get over there! I'm envisioning the perfect shot!"
    play sound chain
    play sound2 chair4
    show aaw 99 with dis
    pause
    mc "Beautiful! Hold that pose!" with dissolve
    play sound camera
    show black
    pause 0.08
    hide black
    pause
    play sound camera
    show black
    pause 0.08
    scene aaw 100
    pause 0.08
    play sound2 camera
    show black
    pause 0.08
    hide black
    pause
    play sound camera
    show black
    pause 0.08
    scene aaw 101
    pause 0.3
    play sound camera
    show black
    pause 0.08
    hide black
    pause 0.08
    play sound2 camera
    show black
    pause 0.08
    hide black
    pause
    play sound3 camera
    show black
    pause 0.08
    scene aaw 102
    pause 0.08
    play sound camera
    show black
    pause 0.08
    hide black
    pause 0.08
    play sound2 camera
    show black
    pause 0.08
    hide black
    pause
    play sound camera
    show black
    pause 0.08
    scene aaw 103
    pause
    play sound camera
    show black
    pause 0.08
    scene aaw 104
    pause 0.1
    play sound camera
    show black
    pause 0.08
    hide black
    pause
    play sound camera
    show black
    pause 0.08
    scene aaw 106
    pause 0.3
    play sound camera
    show black
    pause 0.08
    hide black
    pause 0.08
    play sound2 camera
    show black
    pause 0.08
    hide black
    pause 0.08
    play sound3 camera
    show black
    pause 0.08
    hide black
    pause
    play sound2 camera
    show black
    pause 0.08
    scene aaw 105
    pause 0.08
    play sound2 camera
    show black
    pause 0.08
    hide black
    pause 0.08
    play sound2 camera
    show black
    pause 0.08
    hide black
    pause
    p "Woooow!" with dis
    p "That was fantastic!"
    show aaw 107
    p "Where did you learn about photography and lighting?" with dis
    mc "Learn? Me [mc]. Me point to pretty thing. Me press button. Me likey."
    p "Well, you sure do know how to push a button, [mc]."
    mc "I'm glad you like them, Penny!"
    p "I love them, really."
    show aaw 108
    p "These are going to be perfect for my private collection. They're too good not to keep!" with dis
    show aaw 109
    mc "What?" with dis
    mc "I thought you wanted to use these for your Instagram? Is there something wrong with them?"
    show aaw 110
    p "No! Like I said before, you did an amazing job! They look great! It's just... um... I look like I'm..." with Dissolve(.8)
    show aaw 111
    mc "Whaaat?" with Dissolve(.8)
    mc "Come on Penny, don't tell me you're actually embarrassed about yourself in these pictures?"
    show aaw 112
    p "It's not about being embarrassed. I don’t want people to view my profile and get the impression that I’m just another slutty model who’s looking for sugar daddies."with dissolve
    show aaw 111
    mc "But I saw your profile and noticed a few suggestive pictures already." with dissolve
    show aaw 112
    p "Yeah... I know I've posted some saucy content in the past. But that was before I really wanted to start taking this career path seriously." with dissolve
    p "I'm trying to steer my content into a new direction now, so I don't attract the wrong type of attention in the future. I want to be seen as legitimate."
    p "I realize a couple of revealing pictures are still on my profile, but those are of me in a bikini at the beach or the pool. That's totally different."
    p "With these pictures, I’m in my underwear, in a cold photo studio..."
    p "It just gives off a bad impression."
    show aaw 111
    mc "I get what you mean." with dissolve
    show aaw 112
    p "I don't mind you seeing me like this, because... I don't know, I just feel comfortable around you."with dissolve
    p "But I don't want anyone else to see me like this. There’s a lot of creeps out there and attracting a larger following on Instagram has opened my eyes to it."
    p "I've received a lot of disturbing messages before..."
    p "And besides, what would my mom say if she saw me posting those pictures? She'd probably think it was an introductory photoshoot to a porno or something..."
    show aaw 111
    mc "You have a spectacular body that you work hard for! You shouldn’t be ashamed to show it off. You should be proud of how beautiful you are." with dissolve
    mc "And I'm pretty sure Nancy would agree with me."
    show aaw 112
    p "I know it doesn't make much sense if I really want to be a model, because I know some photoshoots will be more risque than others, but... that's how I feel." with dissolve
    show aaw 111
    mc "Hey, no worries. I understand." with dissolve
    mc "I know you enjoy modeling, but it definitely shouldn’t define you or what you “have to do”. You should only do what you’re comfortable with."
    mc "Go on and keep these photos for yourself. We had our fun here and it was really nice to see this side of you."
    show aaw 113
    p "Exactly! I enjoyed sharing it with you too." with Dissolve(.9)
    p "Thank you for understanding my absurdities, [mc]."
    show aaw 109
    mc "Anytime, Penny. I hope you’ll tolerate mine too." with dis
    show aaw 113
    p "*Giggles* I'm sure I can do that."with dis
    p "And hey, this wasn't a complete waste of time. Maybe in 20 years, I can show these photos to my daughter to prove how pretty I used to be!"
    show aaw 109
    mc "*Chuckles* I'm sure you'll be just as beautiful in 20 years, if not more so."with dis
    show aaw 113
    p "*Giggles* We'll see. I'll let the father of my children be the judge of that."with dis
    show aaw 109
    mc "He’ll be a lucky man..."with dis
    play sound doorslam
    stop music2b
    show aaw 114 with dis
    play music2 sneaky2
    val "OKAY, EVERYBODY OUT!" with dissolve
    val "Nico Valentino needs the studio. Stop whatever you’re doing and clear out! You’re on my time now!"
    show aaw 117
    val "Huh? There’s only two people here?" with dis
    show aaw 115
    p "O-Oh my god, Mr. Valentino!"
    show aaw 116
    val "Well, well, well, who do we have here..."
    val "What's your name, pretty thing?"
    show aaw 115
    p "P-Penelope. I'm a huge fan."
    p "I loved what you showed off at the Barcelona Fashion Show last year. The blouse I brought with me is actually from your fall collection!"
    show aaw 116
    val "Are you a model too, honey?"
    show aaw 115
    p "I'm trying, yes!"
    show aaw 116
    val "Not bad, not bad... I see some potential in you."
    val "You do have a really nice body, darling. Who's your surgeon?"
    show aaw 115
    p "Thank you! I..."
    show aaw 118
    p "W-Wait, what?" with dis
    p "What surgeon? I'm all natural."
    show aaw 116
    val "What?"
    show aaw 117
    val "No way those tits are real."with dis
    show aaw 118
    p "Um, they definitely are."
    show aaw 117
    val "Oh, boy! That's even better, then."
    show aaw 120
    val "Alright, let me see them." with dis
    val "Take that thing off for me and spin a couple of times."
    show aaw 119
    p "What do you mean? Take what off...?" with dis
    show aaw 117
    val "Your bra."
    val "Come on, we're not 15 anymore."
    show aaw 119
    p "I’m not going to get naked for you..."
    show aaw 120
    val "Look, I need to inspect the merchandise before I decide to work with it." with Dissolve(.7)
    val "Hurry up now, I don't have all day."
    show aaw 121
    mc "*Clears throat*" with dis
    mc "Alright buddy, she already said she doesn't want to."
    show aaw 122
    val "Who the fuck are you? Her manager?" with dis
    show aaw 123
    mc "Um... yeah, you could say that."
    show aaw 122
    val "Well then, any good manager wants to find work for their client. So do your job and tell her to strip already."
    show aaw 123
    mc "I told you, she doesn’t want to do it."
    show aaw 122
    val "And I don't give a fuck what she said."
    val "Look, dude, do you know who I am? Are you new to this industry or something?"
    val "I can turn this girl into the next big runway star."
    val "I'm not even asking for a blowjob this time, I just want to see her damn body."
    val "I’m going to say this one last time, because I really hate repeating myself: tell this bitch to do what I’m telling her. You know how many girls would kill to be in her shoes right now?"
    default pennyval = False
    show aaw 123
    menu:
        with dis
        "Persuade Penelope to get naked":
            $ pennyval = False
            mc "(I mean, he does have a point.)" with dis
            mc "(This could be a very good chance for Penelope to hit it big.)"
            show aaw 125
            mc "Hey, Penny, I think you should really reconsider." with dis
            show aaw 126
            p "What? You can't be serious."with dissolve
            show aaw 125
            mc "You're the one making this a big deal. All you have to do is take off your bra and show this guy your tits."with dissolve
            mc "It will be quick and painless."
            mc "Philippe mentioned he's the best in the business... I'm sure he's got plenty of connections out there, Penny."
            mc "You’re finally getting the chance you’ve been waiting for. This could be the step to finally achieving your dreams! You can become a {i}real{/i} model!"
            mc "All you have to do is flash your tits in a photo studio. So what??"
            show aaw 126
            p "But..." with dissolve
            show aaw 125
            mc "Come on, you know you can trust me. I wouldn’t do you wrong."with dissolve
            p ". . ."
            show aaw 127
            p "Just my bra, right...? That’s it?" with dis
            show aaw 117
            val "Yeah, yeah... that's it."
            show aaw 128
            p ". . ."
            show aaw 129
            p "*Unhooking her bra*" with dis
            mc "(Oh god, she's shaking.)"
            play sound clip
            show aaw 130 with dissolve
            mc "(DAMN.)" with dissolve
            show aaw 131
            p ". . ." with dis
            val "Wow!"
            show aaw 117
            val "Your tits are massive!"
            val "That tiny waist of yours make them look even bigger, too!"
            val "Very nice, honey. I'm getting hard already."
            show aaw 120
            val "Come on, spin for me. I wanna see it all." with Dissolve(.8)
            show aaw 131
            pause
            show aaw 132 with Dissolve(1.2)
            val "Wow! Look at that ass! You’re the complete package!" with dis
            val "Where have you been hiding all this time, darling?"
            p ". . ."
            play sound slap1
            play sound2 slap1
            play sound3 slap1
            show aaw 133
            val "That's what I call a nice ass. Hell yeah." with vpunch
            val "Huge, but still soft as fuck. Perfect for me to grip."
            val "You must be tight in all the right places, huh, darling?"
            p ". . ."
            val "Can't wait to get to know you even better..."
            val "Mmm. Our next meeting will be in my office, so we can... sign that contract. Really {i}seal the deal{/i}. Does that sound good?"
            p ". . ."
            val "*Chuckles* Yeah, you seem like a smart girl. You’re just doing what’s best for your future..."
            show aaw 122
            val "Well alright then, get out of here." with dis
            val "I need the studio for another model. My staff will be here any minute."
            show aaw 123
            mc "What about Penelope?"
            show aaw 122
            val "Yeah, yeah, I'll call her next week."
            val "Now get out."
            show aaw 123
            mc "Okay, give us a minute."
            show aaw 134 with Dissolve(1.4)
            mc "Hey, Penny..." with dissolve
            mc "Sorry, I didn't know he was gonna be so handsy."
            mc "But hey, you got the job! He said he's gonna call you!"
            p ". . ."
            p "Yeah, g-great... let's just go."
            mc "Okay..."
            stop music2 fadeout 4
            play music tictoc fadein 4
            show aaw 166 with Dissolve(2.5)
            mc "Well, do you have all of your belongings?" with dissolve
            p ". . ."
            mc "Penny?"
            show aaw 167
            p "Um... Look, [mc]." with dis
            p "I... I didn't like that at all."
            mc "I'm sorry, I didn't want to..."
            p "Let me finish."
            p "I'm not some whore. I'm not gonna suck anyone's dick just to become a model."
            p "And I'm not posing nude for strangers. I thought I made my intentions clear earlier."
            p "I don't like it and I refuse to do it. Despite what you may think, I have standards."
            p "I guess this modeling thing just isn't for me."
            mc "But..."
            p "I think I’d rather focus on finishing my degree now. I want to leave all this nonsense behind."
            show aaw 166
            p "I'm going home." with dis
            mc "(Fuck, I didn't know it would affect her like this.)"
            mc "Okay... I understand. I'm sorry."
            mc "Let me grab another one of those donuts and we'll..."
            p "Don't worry about me. I’d rather go back alone. I’ll just take the bus."
            mc "Oh... okay then... see you home."
            p "Sure. Bye."
            show aaw 173
            mc "(Man, I feel so bad now...)" with Dissolve(1.5)
            mc "(I hope she gets over this soon. Hopefully by tomorrow...)"
            mc "(Hold up, what the...)"
            $ penelopepath = False
            $ penelopeu = False
        "[gr]Tell Mr. Valentino to fuck off":
            $ pennyval = True
            mc "You know what? I think I have a better idea." with dis
            mc "Why don't you take that tripod over there and shove it up your ass. Maybe that’ll keep you from being such a cunt."
            show aaw 124
            val "Ex{i}cuse{/i} me...?!" with dis
            val "Who do you think you are, you stupid little kid?"
            val "I'm Nico Valentino! Keep testing me and I’ll ensure your bimbo friend here can’t find a modeling gig anywhere!"
            show aaw 124b
            mc "What's up with people in this town? Everybody thinks they're the most important douchebag in the world."
            mc "I don't give a shit if your name is Valentino, Bardot, or fucking Spongebob Squarepants."
            mc "We still have 10 minutes left, so you’re actually on {i}our{/i} time."
            mc "So you can either start lubing up that tripod or get the hell out."
            show aaw 124
            val "Grrrr... fucking kid... you’re going to regret this! That dumb bitch has lost any chance of becoming a model!"
            show aaw 124b
            mc "Fuck. Off."
            show aaw 124
            val "Bah!"
            show aaw 135 with Dissolve(1.6)
            mc "Fuck that guy." with dissolve
            mc "{i}\"Thit bitch hurs lust duh chins ti bi i midil\""
            mc "What a..."
            mc "Oh my god."
            mc "Oh, SHIT!" with hpunch
            mc "I just ruined your chances of getting that modeling gig, haven’t I?!"
            mc "Oh god, I’m sorry! I just got carried away. Why does this keep happening to me? I screwed up!"
            mc "I destroyed your dream!"
            mc "I'm so sorry, I'll go apologize to Mr. Valentino right now! Let me..."
            show aaw 136
            p "*Laughs* Don't you even think about apologizing."
            $ penelope_points += 1
            show aaw 135
            mc "...No?"
            mc "Wait, you're not angry?"
            play sound "beat.ogg"
            show aaw 136
            show heartr at topleft
            with dissolve
            hide heartr
            p "Of course not." with dissolve
            p "Quite the opposite, actually. I loved what you said to him. He had it coming."
            show aaw 135
            mc "What about the modeling job, though?"
            show aaw 136
            p "Meh, it doesn't matter. I wasn't gonna use today's photos anyway."
            p "And I'm doing fine on Instagram without him. As long as I keep posting photos, I know something will turn up. I'm in no rush."
            p "And if not, that's why I'm still pursuing my degree!"
            show aaw 135
            mc "Well, I'm glad to see you keeping a positive attitude!"
            mc "I guess we should get going now."
            stop music2 fadeout 4
            show aaw 137
            p "You know... this whole thing got me thinking..." with dis
            p "And I realized, I've never had nude photos taken of me."
            play music2b photoshot fadein 6
            p "Mainly because I haven’t had anyone that I was truly comfortable with."
            show aaw 138
            mc "*Gulps* Uh-huh..." with dissolve
            show aaw 137
            p "Maybe we could use our remaining 10 minutes to take a few topless photos." with dissolve
            p "I mean, they aren’t gonna be published anyways. I really just want to have some for my own private collection."
            show aaw 138
            mc "Makes sense..." with dissolve
            show aaw 137
            p "That Valentino guy made me realize that I'll never feel comfortable doing something like this with a stranger. But you’re no stranger, [mc], and since I have you here..."with dissolve
            show aaw 138
            mc "Umm..." with dissolve
            mc "Just to recap..."
            mc "Y-You want me to take some pictures of you while you’re... topless?"
            show aaw 139
            p "Well, I mean... If you're not comfortable with it, that's okay." with Dissolve(.8)
            p "Just thought that..."
            mc "N-NO! I mean, yes, sure, no problem!"
            mc "Let’s get those puppies out! Er, I mean—let me get that camera back out!"
            mc "Whatever you need!"
            show aaw 140
            p "Awesome!" with dis
            p "Thank you, [mc]."
            play sound clothes
            show aaw 141
            p "It's nice to have someone I can truly trust. I feel like I don’t have to be ashamed around you." with Dissolve(1.5)
            p "Aside from Philippe and Paul, everyone I've ever met in the fashion world has been a pervert or a freeloader."
            mc "I can imagine..."
            mc "(Oh my god, am I about to see Penelope naked?)"
            mc "(Thank you, Jesus.)"
            show aaw 142
            p "That sleazy guy is gone, right?" with dis
            mc "Y-Yeah, I made sure of it."
            mc "Don't worry, I'll warn you if I hear him coming."
            show aaw 143
            p "Alright then." with dis
            mc "(OH SWEET BABY JESUS. LOOK AT THOSE MAGNIFICENT BEAUTIES.)"
            p "Let's get to it!"
            mc "Y-Y-Yeah!"
            show aaw 144
            p "How should we do it?" with dis
            show aaw 145
            mc "D-Do it?"
            show aaw 144
            p "What pose?"
            show aaw 145
            mc "P-P-Pose?"
            show aaw 144
            p "Yeah, for the first set of pictures. How should I pose? You’re the expert here, aren’t you?"
            show aaw 145
            mc "Ah! Yeah, of course!"
            mc "(Come on, [mc], stay focused.)"
            mc "(I think all my blood is being directed to the wrong head...)"
            mc "I like how you posed before. We can try that one again..."
            show aaw 144
            p "Sure! Sounds good."
            play sound chain
            play sound2 chair4
            show aaw 146 with dis
            mc "Y-Yeah, this is a good angle." with dissolve
            mc "(You're seeing something that many men would pay a lot of money for, [mc].)"
            mc "(How the hell did I get so lucky?)"
            play sound camera
            show black
            pause 0.08
            hide black
            pause 0.3
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
            mc "(Man, her breasts are shaped so perfectly.)" with dissolve
            mc "(And that tiny waist of hers makes them seem even bigger.)"
            show aaw 147
            p "What about this one?" with dis
            show aaw 148
            mc "A-Also really nice."
            play sound camera
            show black
            pause 0.08
            hide black
            pause 0.08
            play sound3 camera
            show black
            pause 0.08
            hide black
            pause 0.08
            play sound2 camera
            show black
            pause 0.08
            hide black
            pause 0.2
            play sound2 camera
            show black
            pause 0.08
            hide black
            pause 0.5
            mc "Sexy as hell..." with dissolve
            show aaw 149
            p "Come on, you’ve been behind the camera for too long!" with dis
            mc "What??"
            p "Let's take a picture together!"
            mc "Not a chance."
            play sound chain
            play sound2 chair4
            show aaw 150
            p "Oh don’t be like that! It'll be fun!" with dis
            mc "No, it won't!"
            p "*Pulling your jersey off* Let’s get rid of this! We both need to be topless!"
            mc "No! I'm gonna look like a deformed potato next to you!"
            p "*Laughs* That's not true! You're very handsome!"
            mc "Oh please, Penny! I'm really not photogenic, don't make me do it!"
            p "Shhh, stop complaining and come sit down!"
            play sound chain
            play sound2 chair4
            show aaw 151
            mc ". . ." with Dissolve(.8)
            p "*Looking through the camera* You look great!"
            show aaw 152
            mc "Yeah, sure."
            show aaw 151
            p "Okay, let me set the timer..."
            p "Done! On my way!"
            play sound chain
            play sound2 chair4
            show aaw 153
            p "Alright, I set the timer for 15 seconds." with dis
            show aaw 154
            p "*Giggles* Isn't this fun?!" with dis
            mc "Y-Yeah, so much fun..."
            mc "(Oh no. Please no. Not now.)"
            mc "(Bad dick! No time for boner!)"
            show aaw 155
            mc "(Alright, just calm down [mc]. Stop overthinking things. We’re just making art!)" with dis
            mc "(Don’t think about Penelope's huge, perfect tits.)"
            mc "(Try not to notice how the cold breeze is stiffening her pink, perky nipples...)"
            mc "(Not gonna think about the cute, little freckles all over her curvy body...)"
            mc "(Or how her breasts are slightly paler than the rest of her body... because she probably never sunbathes topless... meaning you’re likely the first man who’s gotten to see her breasts in who knows how long... and...)"
            play sound camera
            show black
            pause 0.08
            hide black
            pause
            p "Huh??" with dis
            show aaw 156
            p "Oh, come on, [mc]!"
            p "You're not even looking at the camera!"
            p "We have to do another one!"
            show aaw 157
            mc "I think that’s good enough, Penny. Valentino is gonna come back at any moment."
            p "I know, I know! That's why we gotta hurry!"
            p "Last one and we're done."
            p "15 seconds!"
            play sound chain
            play sound2 chair4
            show aaw 158
            mc ". . . !!!" with dis
            mc "(Oh shit.)"
            show aaw 159
            p "Am I centered? I can't tell." with dis
            play sound clothes
            show aaw 160 with Dissolve(1.5)
            mc "(Oh my fucking god...)" with dis
            mc "(My dick is rubbing up against her ass...)"
            show aaw 161
            p "Huh?" with dis
            show aaw 162
            p "(Oh my god.)" with dis08
            p "(Is this...)"
            show aawp 1
            p "(Is this huge thing I’m feeling... his...)" with dis08
            p "(His...)"
            show aawpv
            play sound5 whoosh3
            pause 1
            play sound musicstop
            play sound2 chain
            stop music2b
            play music tictoc
            pause 2.1
            scene aawp 2 with Dissolve(.3)
            p ". . ." with dissolve
            mc ". . ."
            show aaw 164
            p "Uhm..." with dis12
            show aaw 163
            mc "(Oh god...)"
            mc "(Now I feel like that Valentino pervert...)"
            mc "Um..."
            show aaw 164
            p "I'm so sorry, I didn't..."
            show aaw 163
            mc "No! I'm the one who's sorry! I didn't mean to..."
            show aaw 164
            p "It's o-okay!"
            p "I mean, I should have known that was gonna happen."
            p "I got carried away."
            p "It's just, I'm not used to..."
            show aaw 163
            mc "No no... It's my fault. I..."
            show aaw 164
            p "I'm gonna go get dressed before Valentino comes back. I'll meet you by the entrance."
            show aaw 163
            mc "S-Sure!"
            show aaw 165 with Dissolve(1.5)
            mc "(Well, this time it wasn't my fault.)" with dis
            mc "(The same thing would have happened to any man in my situation.)"
            mc "(I hope this doesn't make things awkward. I loved how uninhibited she was with me.)"
            mc "*Sighs* (Anyways, I should head to the door.)"
            show aaw 166 with Dissolve(2.5)
            mc "Um... Hey Penny, do you have all of your belongings?" with dissolve
            p ". . ."
            mc "Penny?"
            p "*Giggles*"
            play music2 happy7 fadein 6
            mc "Uhh..."
            mc "Are you laughing?"
            stop music fadeout 3
            show aaw 168
            p "*Laughs* You got a huge hard-on back there!" with dis
            mc "Um... Y-Yeah, well, what man wouldn’t have gotten one? Probably just Gandhi!!"
            p "*Laughs* Is that why you were making such a weird face in our last picture?"
            show aaw 169
            mc "W-Well, yeah." with dis
            mc "What do you expect! You pounced on me while you were half-naked!"
            show aaw 170
            p "*Giggles* Fair enough."
            p "I have to admit, this was one of the funniest photoshoots I’ve ever done!"
            p "I don't know what it is about you, but... I always have so much fun when you’re around."
            show aaw 169
            mc "Me too, Penelope."
            mc "I'm just sorry about what happened with that douchebag earlier..."
            show aaw 170
            p "I told you not to worry! I'll find some other way to achieve my goal."
            p "I don’t need to flaunt my boobs to some weirdo to succeed."
            p "Well, maybe except for one..."
            show aaw 169
            mc "Did you just call me a weirdo?"
            show aaw 170
            p "*Giggles* Me? I'd never dare."
            show aaw 169
            mc "You know, being serious..."
            mc "Have you ever thought about cosplaying as Eternum characters?"
            mc "Most of Instagram's top models do that."
            show aaw 171
            p "I've thought about it, yeah, but I'd have to play Eternum first." with dis
            p "And I'm not good at video games."
            show aaw 172
            mc "That's the thing! Eternum isn’t your typical video game!"
            mc "It's... how do I describe it... completely different from what you’d expect!"
            mc "Ever since I started playing the other day, I haven’t been able to get it off my mind. It’s incredible!"
            mc "You have to try it!"
            show aaw 171
            p "Doesn't the neural implant cost like $3500?"
            show aaw 172
            mc "Well, yeah, that's the only downside."
            p "Mmmm..."
            show aaw 171
            p "I have some money saved up from my sponsorships. Maybe it’ll be enough to buy one."
            show aaw 172
            mc "Really?! Then let's do it! What are you waiting for?!"
            show aaw 171
            p "That's all I have right now. I don’t know if I want to splurge it all on a game. I'm not sure if it's worth it."
            show aaw 172
            mc "Believe me, it is."
            mc "First of all, it's an amazing experience that’s unlike anything else. And second, you can earn all that money back once you start posting Eternum cosplay content!"
            mc "When brands see you playing the game, all those sponsorship offers will start pouring in."
            p "Hmm... well..."
            show aaw 170
            p "You know what? Screw it. Let’s do it!" with dis
            show aaw 169
            mc "Awesome! I can't wait to play with you, Penny!"
            mc "You're gonna love it!"
            show aaw 170
            p "I'll order the neural implant as soon as I get home. If I’m paying that much for it, I might as well get the expedited shipping too so it gets here in a couple of days."
            show aaw 169
            mc "Then let’s not delay! The sooner you buy it, the sooner we can play together!"
            show aaw 170
            p "Alright then, let's go. You can grab a couple more donuts before we leave, if you want. I noticed how much you were drooling every time you passed by them..."
            show aaw 169
            mc "Don’t gotta tell me twice! Be right back!"
            show aaw 170
            p "*Giggles* Okay."
            show aaw 173
            mc "(Man, Penny is gonna join us in Eternum!)" with Dissolve(1.5)
            mc "(That's awesome. Now I just have to convince Nancy...)"
            mc "(Hmm?)"
            mc "(Hold up, what the...)"
            stop music2 fadeout 5
    show aaw 174 with Dissolve(1.2)
    mc "Um..." with dis
    mc "Nova?"
    play music2b quirky1 fadein 3
    stop music fadeout 1
    $ unlock_look("nova", 2)
    show aaw 175
    no "Mmph?" with Dissolve(1.2)
    mc ". . ."
    no ". . ."
    mc ". . ."
    show aaw 176
    no "[mc]!" with dis
    no "I mmwas mmooking mor mmyou!"
    mc "What? I didn't understand any of that."
    show aaw 177
    no "*Leaving the food on the table* I said I was looking for you!" with dis
    show aaw 179
    no "*Giggles* Sorry, I saw these donuts and I couldn't resist." with dis
    show aaw 178
    mc "What are you doing here?! Don’t eat all of my donuts!" with Dissolve(.8)
    mc "A-And... are you following me?!"
    show aaw 179
    no "Of course not!"with Dissolve(.8)
    no "I called you, but you didn't answer. So I tracked down your phone and saw you were here..."
    show aaw 178
    mc "What?! Again?? You have to stop doing this!"with Dissolve(.8)
    if not pennyval:
        show aaw 180
        no "Oh, who's that?" with dis
        show aaw 181
        mc "Don't try to change the subject!"
        show aaw 180
        no "No, no, seriously, it's him!"
        show aaw 195
        no "Ohhh... false alarm. I thought I saw Keanu Reeves going to the bathroom..." with Dissolve(1.5)
        show aaw 196
        mc "Yeah, sure, that sounds super believable."
        mc "Nova, you have to stop hacking me!"
    else:
        show aaw 180
        no "Wait a second... Is that..." with dis
        show aaw 181
        mc "Don't try to change the subject!"
        show aaw 180
        no "No, no, seriously! Is that Penelope?"
        show aaw 181
        mc "Um... Yeah. Why? Do you know her?"
        mc "Oh wait... of course you know her. You probably hacked into my Instagram account and pulled up all the people I’m following!"
        show aaw 180
        no "No! I haven’t touched your Instagram..."
        no "I know her from college! She's like the most popular girl on campus!"
        show aaw 181
        mc "Oh, really?"
        mc "Wow! Finally one account of mine that you haven’t hacked into! What a relief."
        show aaw 180
        no "I was wondering why Nancy and her shared the same last name on your followers list. Nancy is her mom!"
        no "How could I miss it!"
        show aaw 181
        mc "Never mind..."
        show aaw 180
        no "Can I go say hi?"
        show aaw 181
        mc "Um... I guess."
        show aaw 182
        no "H-Hello!" with Dissolve(1.4)
        show aaw 183
        p "Hi there!"
        show aaw 182
        no "Um... I'm Nova, nice to meet you!"
        no "I’ve always wanted to say hi, but you're usually surrounded by people."
        no "And... I don't have any social media accounts, but I've seen your photos. They're so beautiful! Very artistic!"
        show aaw 183
        p "Oh well, thank you so much!"
        p "That's always nice to hear."
        show aaw 182
        no "I've never met a celebrity before!"
        show aaw 183
        p "*Chuckles* Oh god, please... I'm far from a celebrity."
        p "Almost no one knows me outside of Kredon."
        p "Are you a friend of [mc]? From high school?"
        show aaw 184
        no "N-No..." with dis08
        no "*Nervous laughter* Actually... you and I go to the same college."
        no "Erm... I usually sit right behind you in Digital Media class."
        show aaw 185
        p "Oh my god!" with dis08
        p "I'm so sorry! It's just, sometimes I'm so focused on the class that I don't notice what's around me!"
        show aaw 186
        no "NO IT'S TOTALLY OKAY!" with hpunch
        no "S-Sorry, didn’t mean to yell... I’m just a little nervous."
        no "No, it’s alright. I know you usually just do your own thing and don’t pay attention to what all the “popular” people are doing."
        no "That's actually why I like you!"
        show aaw 185
        p "Still, I'm sorry I didn't notice you before." with dis08
        show aaw 186
        no "Seriously, don't worry about it." with dis08
        no "I'm used to it. Most of our other classmates don't even know I exist."
        no "I usually go unnoticed everywhere I go."
        play soundlow whoosh3b
        show novaodd with Dissolve(.05)
        no "Which, frankly, is pretty odd because I’m always screaming, I wear a freakin’ eyepatch, and my orange hair makes me look like a Cheeto with legs."
        play soundlow whoosh3b
        scene novaodd2 with Dissolve(.05)
        no "But seriously, it's all good."
        hide novaodd2
        show aaw 189
        p "Well, thank you for not holding that against me." with dis
        p "We can sit together during class next time, if you want."
        show aaw 188
        no "That sounds great! I'd love that!"
        no "I always knew you'd be nice! You just seem like a good-natured person."
        show aaw 189
        p "I'll see you Monday then."
        p "Nice to meet you, Nova!"
        show aaw 188
        no "Good to meet you as well!"
        show aaw 190
        p "Well, I gotta go now." with dis12
        p "Take care, [mc]."
        show aaw 191
        mc "Don't you want me to go with you?"
        show aaw 190
        p "Nah, it's okay. You’ve done more than enough."
        p "Thank you for everything. I really loved spending time with you today and am looking forward to many more adventures with you."
        show aaw 191
        mc "Anytime, Penny. I loved it too."
        mc "Maybe even too much..."
        show aaw 192
        p "*Giggles* Are you having dinner at home tonight?" with dis08
        show aaw 193
        mc "Most likely. As long as I can stop myself from eating the rest of those donuts. You don't have any plans today?"
        show aaw 192
        p "Nah, I've got an early day tomorrow."
        p "Maybe I'll go on YouTube and watch a few guides on how to play Eternum."
        show aaw 193
        mc "Can't wait for your neural implant to arrive!"
        mc "You’re going to have such a blast!"
        show aaw 192
        p "Hope you’ll be my teacher because I have a lot of things to learn..."
        p "Alright. Guess I’ll see you at home!"
        show aaw 193
        mc "Take care, Penny!"
        show aaw 194
        p "Bye-bye, Nova! It was nice meeting you!" with dis12
        no "Likewise!"
        p "I'll see you in class!"
        no "Sure!"
        show aaw 196 with Dissolve(1.5)
        mc "(Was she flirting with me or am I going crazy?)" with dissolve
        mc "(I’ve never been good at taking a hint.)"
        mc "(Nah, I'm probably imagining things... just like Chang does all the time.)"
        show aaw 195
        no "Oh my god, she's super nice!"
        show aaw 196
        mc "Right? My earlier memories of her are a bit blurry, but I do remember her being nice even back then."
        mc "She never fit the stereotype of a stuck-up, popular teenage girl."
        show aaw 197
        no "I'll be honest [mc], at first you struck me as a complete bore, but you've really impressed me!" with dis08
        no "First, I discovered you were awarded a scholarship for having the top GPA at your European school."
        no "Then, I found out that you won a video game development contest when you were only 14!"
        no "And now I’ve come to learn that you’re friends with Penelope too?!"
        no "Oh, did I mention that your taste in anime is amazing too?! We’ve seen pretty much all of the same shows on Netflix! That’s a huge plus in my book!"
        show aaw 198
        mc "STOP." with hpunch
        mc "HACKING." with hpunch
        mc "ME!!!" with hpunch
        mc "Do you even know what privacy means?!"
    show aaw 199
    no "Oh come on, [mc]... I thought we were past that already!" with Dissolve(.85)
    no "I'm a hacker! I hack things. That's my thing!"
    no "Would you ask an alcoholic to stop drinking?"
    mc "Um... yes?"
    show aaw 200
    no "Anyyyyyways, there's a reason I'm here!" with dis
    no "I KNOW HOW TO FIND IT!"
    mc "Find what?"
    no "*Whispers loudly* CALYPSO!"
    mc "No way, already?!"
    mc "Are you serious?"
    no "I finished deploying my divergence malware! Now I can teleport you to any server you want. No need for invitations or a publicly accessible area, I just need the name of the server."
    no "And I already opened a path to Ogygia! Now we can see if Calypso is really there!"
    mc "That's amazing!"
    show aaw 201
    no "Yeah, well, having both extensive programming and networking knowledge is out of reach for most people. That’s why no one has been able to create something like this before..." with dis
    no "Luckily for you, you just happen to know the best hacker in the country."
    menu:
        with dis
        "Compliment her [pink][mt](Nova +1)":
            show aaw 202
            mc "Alright, you’ve outdone yourself yet again." with dis
            mc "Nova... you truly are incredible."
            $ nova_points += 1
            play sound "beat.ogg"
            show aaw 203
            show heartr at topleft
            with dis08
            hide heartr
            no "*Giggles* Thank you." with dis08
            mc "I have no idea how you’re able to pull off such computer wizardry. How are you not a fedora-wearing neckbeard who lives in their mother’s basement?!"
            no "*Laughs* Well I do still live with my parents, but thank you."
            mc "You said you were gonna do something, and you did it. I'm impressed."
            no "Yes, I did..."
            no "And... how about how fast I did it? It only took me a few hours."
            mc "*Laughs* And you were incredibly fast."
            mc "*Chuckles* I've never met a girl so hungry for praise, but honestly you deserve every bit of it!"
            no "Thank you!"
            show aaw 195
            no "Alright then, let's not waste any more time." with dis
            no "Our clock is ticking!"
            show aaw 196
            mc "How so?"
            show aaw 195
        "Don't waste any time":
            show aaw 202
            mc "Okay, let's not waste any more time, then!" with dis
            show aaw 195
            no "Yep, that's probably a good idea." with dis
    no "The malware was able to use a zero-day BGP exploit to infect the AS on which the Eternum traffic primarily traverses."
    show aaw 196
    mc "Mm-hm."
    show aaw 195
    no "Through that exploit, it remotely accessed their external routers, which foolishly weren’t utilizing OOB management, and then use CDP to find the IP address of the layer-3 switch that hosts the servers."
    show aaw 196
    mc "Uh-huh."
    show aaw 195
    no "It was able to SSH into it, execute the “do sh int stat” command, and identify the Ogygia server. Then it finally established an encrypted tunnel to the server, for us to utilize."
    show aaw 196
    mc "Makes sense."
    show aaw 195
    no "Unfortunately, this entire exploit can only run so long before it’s flagged and quarantined by the ISP’s IPS."
    show aaw 196
    mc ". . ."
    mc "Erm..."
    mc "And in English that means that..."
    show aaw 195
    no "We need to access that server in the next 30 minutes, or the \"door\" will close forever."
    show aaw 196
    mc "WHAT?!" with hpunch
    mc "Why didn't you say that before?!"
    show aaw 199
    no "We would have had more time if you had answered the phone when I called you. It's not my fault." with dis08
    show aaw 196
    mc "Dammit!" with dis
    mc "We still have time, though! I'll run back home!"
    mc "What do we have to do?"
    show aaw 195
    no "Just connect to Eternum and log into any of the public servers."
    no "I'll do the rest."
    show aaw 196
    mc "Okay! What about Alex? Can you call her?"
    show aaw 195
    no "Sure, no worries, I'll let her know."
    no "I'll connect you both once you're online."
    no "Hurry up!"
    show aaw 196
    mc "Alright! See you in a few!"
    show aaw 195
    no "Later!"
    jump calypsos


label novacallnopenny:
    show black with Dissolve(2.5)
    pause
    show screen afewhourslater with dis12
    pause
    scene novanop 1
    hide screen afewhourslater
    with Dissolve(2.2)
    mc "(Ahh... It feels good to have the house all to myself.)" with dis
    mc "(Who needs women anyway? Not me!)"
    play music vibration
    pause 1
    show novanop 2
    mc "Hmm?" with dis15
    mc "(Nova?)"
    mc "(Don't tell me she has already found a way in...)"
    stop music
    play sound beep2
    show novanop 3
    mc "Hello?" with dis
    no "[mc]!!!!" with hpunch
    mc "God! Don't scream!"
    no "I KNOW HOW TO FIND IT!" with hpunch
    mc "Find it? Calypso?!"
    no "CALYPSO!!!"
    mc "No way, already?!"
    mc "Are you serious?"
    no "I finished deploying my divergence malware! Now I can teleport you to any server you want. No need for invitations or a publicly accessible area, I just need the name of the server."
    no "And I already opened a path to Ogygia! Now we can see if Calypso is really there!"
    mc "That's amazing!"
    no "Yeah, well, having both extensive programming and networking knowledge is out of reach for most people."
    no "That’s why no one has been able to create something like this before. Luckily for you, you just happen to know the best hacker in the country."
    mc "Nova... you truly are incredible."
    no "*Giggles* Thank you."
    no "Alright then, let's not waste any more time!"
    no "Our clock is ticking!"
    mc "How so?"
    no "The malware was able to use a zero-day BGP exploit to infect the AS on which the Eternum traffic primarily traverses."
    no "Unfortunately, this entire exploit can only run so long before it’s flagged and quarantined by the ISP’s IPS."
    mc "Erm..."
    mc "And in English that means that..."
    no "We need to access that server in the next 5 minutes, or the \"door\" will close forever."
    mc "WHAT?!"
    mc "Why didn't you say that before?!"
    no "We would have had more time if you had answered the phone when I called you the first time!"
    mc "Dammit!"
    mc "We still have time, though!"
    mc "What do we have to do?"
    no "Just connect to Eternum and log into any of the public servers."
    no "I'll do the rest."
    mc "Okay! What about Alex?"
    no "No worries, I already called her. She's waiting!"
    no "I'll connect you both once you're online."
    no "Hurry up!"
    mc "Alright! See you in a few!"
    no "Later!"
    play sound beep2
    mc "Shit!"
    mc "I better hurry up!"
    jump novamissedscene

label calypsos:
    stop music2b fadeout 3
    show black
    with Dissolve(2.6)
    pause
    show screen afewminuteslater with dis12
    pause
    play sound keys
    play music2 rain3 fadein 4
    if pennyval:
        show aa 1
    else:
        show welcome 6
    hide screen afewminuteslater
    with Dissolve(2.5)
    play sound2 doorclose
    mc "*Gasping for air*" with dis
    mc "*Gasping for air* Oh g-god, I don’t think I’ve ever run so fast in my life."
    if pennyval:
        show aa 5
        p "[mc]? You're soaked!" with dis
        show aa 4
        mc "*Gasping for air* P-Penny..."
        mc "*Gasping for air* Yeah, I came running..."
        show aa 5
        p "From the studio? That's like 5 miles away! And it's pouring outside!"
        show aa 4
        mc "*Gasping for air* Yeah... w-what time is it?"
        show aa 5
        p "1:15 PM."
        show aa 4
        mc "Oh thank god, I made it! I still have 5 minutes left..."
        show aa 5
        p "For what?"
        show aa 4
        mc "S-Something very important!"
        mc "The Weapons of Atlas. There are 3 of them and..."
        mc "Never mind, it'd take too long to explain!"
        mc "Look up that stuff and the Gems of Doom on Google! It'll come in handy when you play."
        show aa 3
        p "*Laughs* Okay, okay, I will. I won't keep you any longer. Whatever you’re up to must be pretty urgent." with dis
        mc "Thank you! See you later!"
        p "Have fun playing."
    else:
        mc "F-Fuck, I'm soaked!"
        mc "Damn rain..."
        mc "*Looking at your phone* 1:15 PM..."
        mc "(Yes! I made it! I still have 5 minutes left!)"
        mc "(Thank god...)"
        mc "(Okay, let's connect to Eternum!)"
label novamissedscene:
    play soundlow stairsrun
    show sc 1 with Dissolve(2.2)
    play sound chair1
    mc "(Alright...)" with dissolve
    play sound2 plugin
    mc "(Come on, come on, come on...)"
    play soundlow login
    show evisor2
    pause 3
    play sound ai7
    blank "{i}Connected." with Dissolve(1.5)
    play sound ai8
    blank "{i}Welcome back to Eternum." with dis
    play sound ai13
    blank "{i}You do not have any server invitations." with dis
    play sound ai14
    blank "{i}You will now be redirected to the Main Nexus." with dis
    mc "Yes, yes, yes, hurry up!"
    play sound ai11
    blank "{i}Please prepare to connect..." with dis
    play sound whoosh4
    stop music2 fadeout 4
    scene white with Dissolve(1)
    pause
    scene aa 6 with Dissolve(2.5)
    play music2b idriel fadein 6
    pause
    mc "(Oh... This is the Main Nexus?)" with dis
    mc "(I remember this place from when I first connected to Eternum.)"
    id "Hello, [mc]."
    show aa 7 with dis12
    mc "(Ah, Eternum's AI.)" with dis
    mc "(It'd probably be best not to mention anything regarding our intentions. Ulysses staff members are probably monitoring all conversations.)"
    mc "(Nova said that all I had to do was join a public server.)"
    mc "Hi! It's nice to see you again."
    mc "...Idriel, right?"
    show aa 8
    id "That is correct." with dis08
    id "I see that you haven't been invited to a server this time."
    id "You can either join one of Eternum's public servers, or any of the servers that you’ve previously accessed."
    show aa 7
    id "Hmm..." with dis08
    show aa 8
    id "Ion, Ekabar, and The Red Herring." with dis08
    id "Those are all good places. You must know some experienced players."
    show aa 7
    mc "Yeah, I do. They've been helping me a lot." with dis08
    show aa 8
    id "Are you enjoying your experience in Eternum so far, [mc]?" with dis08
    id "Have you experienced... anything remarkable?"
    show aa 7
    mc "N-No... Everything's been... pretty quiet and relaxed." with dis08
    show aa 8
    id "Well, if that was what you were looking for... you're doing it right." with dis08
    show aa 7
    mc "For sure..." with dis08
    mc "(Why am I so anxious?)"
    mc "(She's just an AI. She's like any other NPC in a video game. She is incapable of judging me or accusing me of anything.)"
    mc "(She's probably talking to hundreds of other players simultaneously, doing whatever her programming dictates.)"
    mc "(And yet... I almost feel like I’m being interrogated...)"
    show aa 8
    id "So... What's it gonna be?" with dis08
    id "Ion? Ekabar?"
    show aa 7
    mc "No... I'll just join a public server this time." with dis08
    mc "Maybe there I can score myself an invitation to a new server."
    show aa 8
    id "You wish to visit a public server?" with dis08
    show aa 7
    id "Hmmm..." with dis08
    show aa 8
    id "I'll send you to Agora. It’s known as a central hub for players to meet each other and exchange invitations to other servers." with dis08
    id "I'm sure you might be able to find what you are looking for."
    show aa 7
    mc "Sounds perfect." with dis08
    show aa 8
    id "Good. Enjoy your session." with dis08
    id "Is there anything you'd like to know before you leave?"
    show aa 7
    mc "Well, since you brought it up... I'd like to know the location of the remaining Gems of Doom." with dis08
    id "*Chuckles*"
    show aa 8
    id "I'm afraid I can't give you that information." with dis08
    show aa 7
    mc "Well, I assumed so, but it was worth a try." with dis08
    show aa 8
    id "Is there anything else you'd like to know?" with dis08
    show aa 7
    mc "I'd ask you more things, but if you're gonna keep saying you can't give me that information, I'd prefer not to waste my time." with dis08
    id "*Chuckles*"
    show aa 8
    id "Well..." with dis08
    show aa 9
    id "Maybe you're not asking the right questions..." with Dissolve(1.5)
    show aa 10
    id "Don't you think..." with dis
    id "...[mc]?" with dis
    play sound snap
    stop music2b
    show aa 11
    pause .1
    scene black
    pause
    show login3 with flash
    pause 4.4
    play sound glitch2
    play sound2 error2
    scene glitchcalypso
    pause
    play music forest fadein 6
    no "[mc]?" with dis
    no "Hello?!"
    no "Oh shit, is he dead? Please don't be dead..."
    no "I should have tested this more..."
    no "This is what happens when you make me hurry!"
    no "Well, technically he said there was no rush, but..."
    show aa 12 with Dissolve(3)
    mc "Mmmm..." with dis
    mc "(Holy fuck...)"
    mc "(My head is spinning...)"
    mc "(This is even worse than the first time I joined Ion...)"
    mc "(F-F-Fuck, it's so cold out here...)"
    play sound snow
    show aa 13 with Dissolve(1.5)
    mc "(Shit, I can’t even feel my hands...)" with dissolve
    mc "(Where am I?)"
    mc "(Is this Ogygia?)"
    mc "(Where are Nova and Alex?)"
    mc "(I thought I heard Nova's voice earlier...)"
    show aa 12
    mc "(Man, thank god the sun is out, otherwise I'd probably freeze to death.)" with dis
    show aa 13
    mc "(Maybe I should start moving.)" with dis12
    show aa 14 with dis12
    pause .4
    mc "(Hmm?)" with dissolve
    mc "(Who's that?)"
    mc "(Wait, that hair...)"
    mc "(Is that...)"
    play sound snow4
    show aa 15 with Dissolve(1.5)
    mc "A-Alex?" with dissolve
    mc "Is that you?"
    mc "Are you okay?!"
    x "Mmmmhh..."
    play sound snow2
    show aa 16
    mc "*Sighs of relief* Oh, thank goodness you're alright." with dis08
    play sound snow
    show aa 17 with dis
    x "Agh... my head... is spinning..." with dissolve
    mc "I know, the same thing happened to me."
    play sound snow
    $ unlock_look("alex", 2)
    show aa 19
    x "Where are we?" with dis
    play music2 fantasy2 fadein 3
    stop music fadeout 10
    show aa 19b
    mc "(Oh...)" with dissolve
    mc "Um..."
    mc "O-O-Ogygia, I think."
    show aa 19
    x "I logged in just like that girl told me, then Idriel connected me to the Cyrodiil server and there was a weird glitch during the wormhole. I must’ve passed out after that." with dissolve
    show aa 19b
    mc "Y-Yeah, same." with dissolve
    show aa 19
    x "I'm still a little dizzy..." with dissolve
    show aa 20 with dis
    x "F-Fuck, I’m so cold." with dissolve
    mc "Yeah, I can s-see that..."
    x "Come on, let’s walk around and get the blood flowing. It'll warm us up."
    show aa 22
    mc "Y-Yeah, maybe you should..." with dis
    mc "Before we start moving..."
    mc "You know..."
    show aa 22b
    x "Hmm?" with dis
    play sound snow2
    show aa 23
    x "You son of a bitch." with hpunch
    mc "What did I do?!"
    x "When were you planning on telling me?"
    mc "I just did!"
    x "Yeah, after you took enough mental pictures for your spank bank, huh?"
    mc "Of course not!"
    play sound snow
    show aa 24
    x "Lord knows what you did while I was unconscious..." with dis
    show aa 25
    mc "I woke up right before you did!" with Dissolve(.4)
    mc "And I'd never do anything to you like that!"
    show aa 24
    x "Yeah, if you say so..." with Dissolve(.4)
    show aa 25
    mc "I didn’t know that was going to happen!" with Dissolve(.4)
    mc "And come on, you can't blame me!"
    mc "Have you seen what you’re wearing? That dress hardly covers anything!"
    show aa 24
    x "This is an elven mail woven by the Airewen." with Dissolve(.4)
    x "It increases the magical transmogrification abilities of its wearer and provides protection from fire."
    x "It can even stop bullets."
    show aa 25
    mc "Damn, really?" with Dissolve(.4)
    mc "And who decided to make it so sexy-looking?"
    show aa 26
    x "I don't know, probably some nasty pervert like you." with dis
    mc "Well, whoever did it, I need to thank them."
    mc "You look hot, Alex."
    x "Bah."
    show aa 27
    no "You're alive!" with dis
    no "Oh, thank god!"
    show aa 28
    no "Not gonna lie, I was trying to find an Exit Portal." with dis
    no "I wasn’t sure you two were going to wake up."
    show aa 33
    x "Oh... Nova, right?"
    show aa 30
    no "The one and only!"
    no "It's a pleasure to see you again."
    show aa 33
    x "Where are we? Did we make it? Is this..."
    show aa 30
    no "Yep! This is Ogygia!"
    no "The mission was a success!"
    show aa 33
    x "I'll be honest, your phone call was... unexpected."
    x "What if I didn’t answer my phone?"
    x "Would you two have visited this server without me? After I was the one who mentioned this place and its connection to Calypso?"
    show aa 28
    no "Nah, everything was under control."
    no "I knew you were at home. Your swimming lessons are from 8 to 12 on Sundays, and your next one isn’t until Monday. So you were completely free."
    show aa 33
    x "W-What?"
    x "How do you know..."
    show aa 38
    mc "Yeah... she does that."
    mc "You'll get used to it."
    show aa 36
    mc "By the way, what's with the suit, Nova?" with dis
    mc "Between that and your hair, you stand out like a polar bear in the desert."
    show aa 28
    no "Ah, this is my hitman outfit."
    no "We entered this server in a rather... unconventional manner, so the general rules can't be applied here."
    no "We have the outfits we would’ve worn in the servers we were originally connecting to."
    no "In my case, the Sin City server."
    show aa 31
    no "Alex... you were headed to some kind of fantasy world, I assume." with dis
    show aa 32
    no "And you, [mc]..." with dis
    no "Is that the basic outfit of Agora?"
    show aa 37
    mc "Yeah, Idriel suggested that server to me. I didn't give it much thought."
    show aa 34
    x "Agora... the public server? Why? You could have logged into any of your previous servers and brought along better gear!"
    show aa 38
    mc "Yeah, well, it wouldn't have made any difference."
    mc "I don't have any cool weapons or armor yet."
    mc "I just started playing a few days ago."
    show aa 34
    x "What?!" with hpunch
    show aa 35
    x "Oh my god, I brought a total noob to obtain Calypso..." with dis
    x "I knew it was a bad idea to tell you about this place."
    show aa 38
    mc "Hey, you wouldn't be here if it wasn't for me."
    mc "You just knew the name of the server and that Calypso was hidden here."
    show aa 29
    no "Well, technically I am the one who found a way in, so..."
    show aa 33
    x "Yeah, that's right. I owe you one, Nova."
    x "If we find it, we can share Calypso. We’ll keep it in a bank and use it at our convenience."
    x "But if it ever leads to the discovery of a Gem of Doom, it’s every woman for herself."
    show aa 31
    no "Sounds good, done deal."
    show aa 38
    mc "And what about me?"
    show aa 34
    x "Well yeah, you can use it too, of course."
    x "We're a team now... I guess."
    mc "Nice!"
    show aa 36
    mc "So... where's Calypso, Nova?"
    show aa 34
    x "Yeah, I was expecting this server to be a temple or a palace with a gigantic chest. Not a forest where Mr. Tumnus could live."
    show aa 28
    no "*Nervous laughter* Well, I explored the surroundings a bit while you both were unconscious, and..."
    no "There's nothing here. Just... trees."
    show aa 33
    x "What? Nothing?"
    show aa 28
    no "*Nervous laughter* Nada."
    show forest with Dissolve(1.5)
    play soundlow eagle
    pause 4.3
    scene aa 39 with dissolve
    mc "So..." with dis
    mc "We're completely lost then?"
    no "Um..."
    no "Kinda."
    show aa 40
    no "I was so excited to get into this secret server that I forgot to think of a way to get out." with dis
    x "So we don't even know which way to go?"
    no "I haven’t the faintest idea."
    show aa 41
    no "But don't worry!" with dis
    no "If we start walking in a straight path, I'm sure we'll find something!"
    no "Come on guys, you just gotta put on a brave face!"
    no "WE'RE NOT GONNA DIE HERE!"
    no "LET'S GO!"with hpunch
    mc ". . ."
    x ". . ."
    show aa 42
    show fewhourscorner
    hide screen heart
    with Dissolve(3)
    play soundlow eagle
    pause
    hide fewhourscorner
    show screen heart
    no "AAAAAAAH, WE'RE GONNA DIE HERE!" with Dissolve(2.5)
    no " This forest is endless!"
    play soundlow snow3
    show aa 43
    no "My feet are killing me!" with Dissolve(2)
    no "We've been wandering aimlessly in these woods for I don't even know how long."
    no "I'm cold, I'm tired, and I'm thirsty!"
    no "If I'm the first to die, please don't eat me... I might look like a walking Cheeto, but I promise you, I do not taste like one..."
    play soundlow snow4
    show aa 44
    x "The mountain keeps sloping down toward this direction." with dis12
    x "That looks like our best chance at finding a river."
    x "Once we get there, we'll be able to get our bearings."
    show aa 45
    no "How the hell do you still have so much energy?" with dis
    no "I’m on the verge of passing out!"
    show aa 46
    x "Well, thanks to all that swimming, I have quite a bit of stamina."
    show aa 45
    no "Well what about your body temperature? Aren't you cold?"
    no "You're almost naked!"
    show aa 46
    x "I was at first, but these robes really hold in the heat, even if it doesn't seem like it."
    x "\"Elven magic\", I guess."
    show aa 45
    no "Awww, that's so cool. If I'd known that this server was a damn frozen wasteland, I'd have taken another outfit."
    no "Yep. Definitely gonna die here."
    play soundlow snow4
    show aa 47 with Dissolve(1.5)
    mc "*Patting her* Come on, come on, Nova." with dissolve
    mc "How can the world’s greatest and cutest hacker die in a random server of Eternum, just because of a little cold weather?"
    mc "That’s not very fitting for you."
    show aa 48
    no "*Giggles* Y-Yeah, I guess you're right." with dis08
    no "I’ll keep pushing through the pain!"
    play soundlow snow3
    show aa 49
    mc "And hey, if we don’t find Calypso or an Exit Portal, I guess someone will end up disconnecting us in the real world. I know Dalia will, otherwise she’ll have to wash dishes tonight." with Dissolve(1.6)
    mc "So nobody here will be dying from hunger or the cold."
    show aa 50
    x "Oh, I recommend you not doing that to anyone... like, ever."
    show aa 49
    mc "Doing what? Disconnecting someone who's playing?"
    show aa 50
    x "Yeah. That’s a big no-no. They say the abrupt shock can cause nerve damage, leading to epilepsy or cerebral palsy."
    show aa 51
    no "There have been cases of people becoming blind or paraplegic after they were forcibly disconnected during the middle of a game session."
    show aa 50
    x "Those were rare occurrences, yes, and other people have ended up fine after a forced disconnect, but still... I wouldn't risk it."
    show aa 49
    mc "Are you serious? People know about these risks? And they still keep playing?"
    mc "How is that possible?"
    show aa 50
    x "Millions of people die worldwide from tobacco and alcohol each year, but both are perfectly legal and people continue to consume them."
    x "Why would this be any different?"
    show aa 49
    mc "Fair point... I'm not gonna stop playing because of those risks either."
    show aa 51
    no "The only way to leave a server without an Exit Portal, and at the cost of losing your levels and inventory... is by killing yourself."
    show aa 49
    mc "God, I hope it won’t come to that..."
    play soundlow snow4
    show aa 52
    mc "Do you think Calypso will be protected?" with Dissolve(1.4)
    show aa 53
    no "Yeah, it's very likely."
    no "The other Weapons of Atlas were heavily guarded. Not sure if Hyas was also, but Dione was definitely protected by Praetorians."
    show aa 52
    mc "Praetorians?! Eternum's \"police\"?"
    mc "How is that fair? Aren't they immortal?"
    show aa 53
    no "No! They're tougher than most, but they can die just like any other player or AI of Eternum."
    no "The only two people with immunity are Idriel and the Founder himself."
    no "Not even the senior managers of Ulysses are protected."
    play soundlow snow3
    show aa 54
    no "Speaking of which, what's it like to be the daughter of William Bardot, Alex?" with dis
    no "Has he ever told you any secrets about the company?"
    show aa 55
    x "No. He never talks about his job." with dis
    x "And... well, we don't even talk to each other anymore, so... I don’t have much of an answer for you."
    play soundlow snow4
    show aa 56
    no "Oh... I'm sorry I asked, I didn't know it was a more serious topic." with Dissolve(1.5)
    play soundlow snow3
    show aa 57
    x "Don't worry, I don't mind." with dis
    x "The relationship with my family is... complicated. [mc] witnessed that firsthand."
    play soundlow snow4
    show aa 58
    x "Can I ask you a personal question?" with Dissolve(1.5)
    x "What happened to your eye? If you don't mind me asking."
    show aa 59
    no "I don't mind at all."
    show aa 60
    no "Actually, I'm surprised that [mc] hasn’t asked me about it yet." with dis08
    play soundlow snow3
    show aa 61
    mc "Well, before all of this, we were pretty much strangers to each other. I thought it would be rude if I asked you point-blank."with dis12
    mc "And then... well, honestly you’re pretty flamboyant so I had forgotten you were even wearing an eyepatch. I wouldn't say that's your defining trait."
    show aa 60
    no "...I'm not sure if that was a compliment, but I'll take it as one."
    show aa 62
    no "Anyway, my left eye is still there and it works—I’m not blind or anything."with dis
    no "Actually, I have better eyesight in my left eye than in my right one."
    no "But it's highly sensitive and gets irritated if I remove my patch for longer than an hour a day."
    show aa 61
    mc "Really? Even in Eternum?"
    show aa 60
    no "Yep. That's the downside of Eternum's ultra-scan."
    no "Physical illnesses like a missing leg, or in my case a sensitive eye, are also carried over into the game."
    show aa 61
    mc "I guess I’d never really thought about it..."
    mc "That’s actually a little... sad."
    show aa 58
    x "Well, Ulysses isn't really known for its ethical practices and upstanding moral values."
    x "They could probably create something that allowed people with disabilities to play normally."
    x "But if it doesn't make them any money, then why would they?"
    x "That's all that matters to them."
    play soundlow snow4
    show aa 63
    mc "You know, sometimes, I think if Ulysses really..." with dis12
    stop music2
    play soundlow snow2
    play music forest fadein 10
    show aa 64 with dis08
    pause
    mc "Hmm? What's wrong?" with dissolve
    show aa 65 with dis
    play sound deception
    x "A..." with dissolve
    x "A village!"
    mc "Oh! Finally!"
    no "Thank god!"
    no "I was just about to accept my fate!"
    x "Let's go take a look!"
    play soundlow snow3
    show aa 66 with Dissolve(2.3)
    pause
    mc "Damn... this place is a ghost town." with dis08
    mc "HELLO?" with hpunch
    echo "{i}{size=50}Hello... {nw}{w=1}" with dis
    echo "{i}{size=40}Hello... {nw}{w=1}" with dis
    echo "{i}{size=30}Hello..." with dis
    mc "Hmmm... maybe there should be NPCs here, but they haven't been implemented yet."
    mc "Maybe that's why the server was inaccessible?"
    no "Like we're playing on an unfinished build of the server?"
    mc "Yeah, something like that."
    play sound doorold
    show aa 67
    x "That house was completely empty." with dis12
    x "No trace of anyone."
    x "No scraps of clothing, no personal belongings... nothing."
    play soundlow snow4
    show aa 68
    no "Yeah, same thing over here." with dis12
    no "The stable is empty and completely clean. There haven't been any horses here in a while."
    play soundlow snow3
    show aa 69
    x "This is weird as fuck." with Dissolve(1.6)
    x "The other Weapons of Atlas were found on servers with impressive temples."
    x "And Calypso is supposed to be hidden inside an empty hut?"
    mc "Maybe the challenge was to enter the server and find this village."
    x "Hmm... I don't know."
    x "I think we're missing something."
    show aa 70
    no "This house is also empty! Nothing!" with dis
    play soundlow snow4
    show aa 71
    x "Well, we've reached the end of the village." with Dissolve(1.6)
    x "Nova, go take a look at that house."
    no "Okay!"
    show aa 72
    x "[mc], you go to..." with dis12
    mc "Hey, what's that?"
    x "What's what?"
    mc "There!"
    mc "It's some sort of stone altar with... a box?"
    x "No way..."
    play soundlow snow3
    show aa 73 with Dissolve(2.5)
    play music2 deception
    pause
    no "T-This is it!" with dissolve
    no "This has to be!"
    mc "Just like that? No guards? No protection?"
    x "I don't know, but someone put this box here for a reason. It has to be something special. It’s gotta be..."
    play sound deception
    show aa 74
    x "Calypso." with dis
    no "Is it just me, or do you feel it emitting some sort of... negative aura?"
    x "Yeah, I can feel that too."
    x "But at the same time, it feels... calm?"
    show aa 75
    mc "So... Calypso, the third Weapon of Atlas, is inside this box?" with dis
    mc "It's rather small... I guess it's not a lightsaber crossbow like I was hoping."
    show aa 76
    x "The fuck are you talking about?" with dis
    x "Of course it's not a crossbow. I already told you that Calypso is a code to manipulate servers."
    show aa 77
    mc "Well, yeah, but it still has to be something tangible." with dis08
    mc "I doubt it's gonna be a piece of paper that says: \"Hi. Calypso's code is X342-55G. Thanks for playing.\""
    mc "It has to be something. It could have been a reality-manipulator-crossbow, or a dimension-splitting-crossbow, or a crossbow within a crossbow... I don’t know."
    show aa 76
    x "What’s with you and crossbows?" with dis08
    show aa 78
    x "Although... he has a point." with dis
    x "It should definitely be something..."
    show aa 79
    no "Maybe some kind of wand?"
    no "Like... a very powerful one?"
    no "Hyas was a sword, Dione a sniper... maybe the third weapon is magical."
    show aa 78
    x "Oh... That actually makes a lot of sense."
    x "Maybe a wizard's staff?"
    show aa 80
    no "Mmmm... No, a staff couldn’t fit into that box." with Dissolve(1.5)
    no "Magic gloves?"
    x "Could be."
    x "Or a bracelet of power."
    no "Also possible."
    mc ". . ."
    play sound4 whoosh5
    pause .5
    stop music fadeout 1
    show arrowca
    stop music2
    pause
    play sound whoosh5
    pause .5
    play sound2 arrow
    pause .2
    scene aa 81
    pause .15
    show aa 82 with hpunch
    pause
    play music forest fadein 3
    show aa 83 with Dissolve(2.5)
    pause
    play sound snow
    show aa 84
    x "Um..." with dis
    no "Whoa..."
    x "Excuse me, did you just catch an arrow in mid-air?"
    play sound2 snow
    show aa 85
    mc "Uh... it looks like it, yeah." with dis
    show aa 86
    x "You’re saying that as if it’s the most normal thing to do."
    x "How the fuck did you do that?"
    show aa 85
    mc "I don't know... I felt it coming, so I grabbed it."
    show aa 86
    x "You {i}felt{/i} it coming?"
    x "What the hell? You were standing with your back toward it! How is that possible?! Stop bullshitting me!"
    show aa 85
    mc "I don't know how! I just did it!"
    show aa 86
    x "So you're a ninja with superhuman reflexes now?"
    show aa 85
    mc "Um... maybe my reflexes improved in Eternum. I don't know what you want me to say, really."
    show aa 86
    x "It doesn't work like that. You've only been playing for a few days!"
    x "What's your compatibility level?"
    show aa 85
    mc "100\%. Oh, maybe that's it."
    show aa 86
    x "Ha. Ha. Very funny. Come on, seriously."
    show aa 85
    mc "I'm not lying, it’s 100\%. That's what Idriel told me."
    show aa 86
    x "What?? That's impossible. No one's ever gotten 100\%."
    x "Shit, I don't even know anyone who's over 85\%."
    show aa 85
    mc "Well what’s your compatibility level then?"
    show aa 86
    x "57\%."
    show aa 85
    mc "Really? Only?"
    show aa 86
    x "What do you mean, \"only\"?"
    x "That's above average!"
    show aa 85
    mc "I don't know, maybe I misheard her. Is there anywhere I can check my levels and stats?"
    show aa 86
    x "You have to connect to the Main Nexus and ask Idriel."
    show aa 85
    mc "Oh, cool. I have something to ask her next time."
    play sound snow3
    show aa 87
    no "Um... I'm sorry to interrupt, but shouldn't we be investigating where that arrow came from?" with Dissolve(1.5)
    show aa 88
    no "I doubt another human player managed to access this server, so it has to be an NPC." with dis
    show aa 89 with dis
    mc "That's weird, we didn't see anyone in the village." with dis
    x "Hmmm..."
    show aa 90
    mc "Anyway, I think we should open this box and then try to find an exit..." with dis
    show alexcal
    play sound arrow
    pause .1
    play sound2 arrow
    pause .1
    play sound3 arrow
    pause .1
    play sound4 arrow
    pause .1
    play musicb pulse
    play sound5 arrow
    scene aa 92 with hpunch
    mc "H-HOLY SHIT!" with hpunch
    no "What the fuck?!"
    mc "The arrows... they’re like... frozen!"
    x "Y-Yeah, that was me this time. I created a magical barrier."
    x "Looks like we're not alone, guys..."
    no "But who..."
    stop musicb
    stop music fadeout 10
    play sound rocks
    play sound2 slam
    show aa 93 with hpunch
    show aa 93 with hpunch
    play music2 medieval3 fadein 3
    pause
    mc "No..." with dis
    mc "No, no, no..."
    no "Who's that?"
    mc "I've seen this before..."
    play sound2 steam1 fadein 2
    pra ". . ." with dis
    play sound snow
    show aa 94
    pra "*Standing up* Eternum IDs 294057751, 301969771, and 421200234."with Dissolve(1.5)
    pra "Put your hands up and surrender at once."
    mc "Oh shit..."
    show aa 97
    x "What exactly are we being accused of?" with dis08
    x "We've done nothing wrong!"
    show aa 95
    pra "You have accessed an unauthorized server." with dis08
    pra "Calypso must not be used yet. Ogygia will remain off-limits until further notice."
    show aa 98
    x "What? You created the three Weapons of Atlas! We're just playing your damn game and using all methods available to us. There's no rule against that in Eternum's General Code of Ethics." with dis08
    x "We didn't torture anyone, we didn't rape anyone, and we didn't use the network to traffic illegal content."
    x "We haven't broken any laws!"
    show aa 96
    pra "Your case will be examined by an Ethics Jury. It is not our duty to place judgment upon you." with dis08
    pra "Lower the barrier and accompany me without resistance."
    show aa 99
    x "Yeah? Or else what?" with dis08
    play sound deception
    show aa 95
    pra "You will be excommunicated." with dis08
    mc "W-What?"
    show aa 99
    x "Fuck no!" with dis08
    x "I won't end up like Benjamin!"
    show aa 100
    mc "Y-You know about Benjamin?" with dis08
    show aa 99
    x "I know enough to suspect that there's something fishy about his case." with dis08
    x "Ulysses has been covering up mysterious deaths for years."
    show aa 96
    pra "It doesn't matter what you believe. You have reached the end of the road." with dis08
    pra "You have committed a crime and must face the consequences of your actions."
    pra "Lower the barrier. Resisting will only make things more painful for you."
    show aa 99
    x "F-Fuck!" with dis08
    show aa 100
    mc "C-Can't we fight them?" with dis08
    mc "There are only three of them!"
    show aa 101
    x "Look around you, [mc]." with dis
    x "We are surrounded."
    x "The second I remove the barrier, a flood of arrows will rain upon us."
    mc "Oh, fuck..."
    show aa 100
    x "We're fucked..." with dis
    show aa 96
    pra "Surrender now. This is your last warning." with dis08
    show aa 102
    x "*Voice breaking* I... I don't wanna die, [mc]." with dis08
    mc "(Shit, I've never seen her so scared...)"
    x "*Voice breaking* They’d just say I had a heart attack swimming or some shit and then forget all about me."
    mc "We’re gonna figure a way out of this, Alex."
    x "But they’re everywhere!"
    mc "Listen to me, this is not the end. We are not gonna die here."
    x "But what can we do?"
    play sound sniperbolt
    stop music2 fadeout 2
    play music forest fadein 5
    pause .5
    show aa 103 with Dissolve(2.4)
    no "Well... I only see one solution." with dissolve
    no "Because there’s no way in hell I’m dying here either."
    no "There's still so much I want to do in this life."
    show aa 104
    x "What?"
    x "That sniper..."
    x "I've seen it before..."
    x "T-That's... Dione! The second Weapon of Atlas!"
    show aa 103
    no "I think there’s only 2 Praetorians who are leading the charge. If we get rid of them, the warriors will lose formation."
    show aa 106
    no "The other Praetorian is up there, on top of the hill." with dis
    no "And she has a sniper rifle too. She's probably their backup plan."
    show aa 107
    pra "What? Did she see me from there?" with dis
    pra "Huh, she’s got sharp eyes."
    show aa 106
    no "I think she's about 480 yards away. Maybe 490." with dis
    no "I'd say it's a little hypocritical to accuse us of cheating, only to then use a sniper rifle on a medieval server... don't you think?"
    show aa 95
    pra "Say whatever you want. You're just delaying the inevitable."
    show aa 103
    mc "Y-Y-You have Dione?! But I thought it was owned by a... Delilah Warren, or something!" with dis
    show aa 108
    no "*Giggles* Pretty cool name, huh?" with dis
    mc "But why?"
    no "Have you forgotten? The foundation of a hacker lifestyle is anonymity, [mc]."
    no "And let's be honest, Delilah Warren is a lot catchier than Nova Johnson."
    play sound transform1
    show aa 109 with Dissolve(2)
    no "And Dione is not just a sniper. It can transform into any kind of ranged weapon." with dissolve
    no "Hmm, but I think I’ll stick with this set-up today. I’m gonna need it for that Queen of the Hill up there."
    play sound2 sniperbolt
    play sound3 snow
    show aa 110
    no "I'll take care of that one, Alex." with dis12
    no "Then I’ll deal with the archers in the trees and on the roofs."
    no "Can I count on you to kill the other Praetorian leader?"
    show aa 104
    x "The other Praetorian...?"
    show aa 105
    x "You can count on me, Nova. I got this bitch." with dis
    show aa 111
    mc "Holy shit, I can't believe it! You have Dione, the weapon whose bullets never miss their targets!" with dis
    mc "We can win this fight!"
    show aa 112
    no "*Giggles* Sorry [mc], I'm afraid that's only a rumor people have made up." with dissolve
    no "Its real unique ability is being able to transform into any type of firearm."
    no "Also, each bullet is fired with its cartridge, specially outfitted with tracking capabilities and thus allowing the user to teleport to its location."
    show aa 107
    pra "What? Is she seriously trying to snipe me from there?"
    pra "*Mockingly laughs* Good luck with that. Dione is the weakest of the three for a reason."
    show aa 111
    mc "Teleport to where its bullets travel? What the hell is the point of that?"
    show aa 112
    no "Well, very few things are faster than a bullet. So with that kind of speed, you can cover large distances in a matter of seconds, or even make for a quick escape." with dissolve
    show aa 111
    mc "But... Alex's barrier will break the moment you shoot!" with dissolve
    mc "If you miss the shot, the other Praetorian will easily snipe us! She has the high ground! Obi-Wan taught us the importance of that!"
    show aa 113
    no "Well you know what they say about rumors, [mc]?" with dissolve
    no "There’s usually a hint of truth to them."
    no "In this case, the one that never misses... isn’t Dione..."
    play soundlow whoosh5
    pause .6
    stop music fadeout 1
    show aa 114 with dis
    pause
    no "It's me." with dis
    play sound dione1
    show novashot1 with hpunch
    pause 11.6
    play sound4 rocks
    play sound5 fall2
    scene aa 115 with Dissolve(.5)
    pause .6
    play music2 dione
    no ". . ." with dis
    $ unlock_look("nova", 3)
    show aa 116
    no "47 shots fired with Dione and 46 confirmed kills." with dis
    no "Yeah, I missed a shot once, but don't tell anyone, alright? I have a reputation to uphold."
    pra ". . ."
    play sound sniperbolt
    play sound2 snow
    show aa 117 with dis
    no "I hope you don't mind me taking your spot. The view is just gorgeous up here!" with dissolve
    no "And please, don't take it personally. I’m just not ready to die quite yet."
    no "I at least have to make it to next Monday. Luna's father told me he's introducing a new taco to the menu. I’ve been {i}dying{/i} to try it..."
    no "And well, past that... I just made some new friends. We still have a lot of adventures ahead of us. I'm sure you understand."
    show aa 118
    no "My left eye helps, for sure, but the trick is to control your breathing, calculate the distance, account for the Coriolis effect, and of course factor in the wind." with dis
    no "Never rush. Take your time. Don’t stiffen up. Stay relaxed."
    no "Just keep your eye on the target..."
    no "...and then {i}slowly{/i} squeeze the trigger." with dis12
    play sound dione2
    show novashot2
    pause 2.3
    scene amache1 with hpunch
    pause 1.5
    play sound2 dione2
    pause 2.2
    scene amache2 with hpunch
    pause 3
    play sound rocks
    scene a 1 with dis
    pause
    play sound whoosh4
    show novashot3
    pause 2
    show aa 122
    pause
    show aa 123
    x "*Chuckles*" with dis
    show aa 124
    sol "W-What the fuck?!" with dis12
    sol2 "She just headshot Mia and Emma!"
    pra ". . ."
    x "You know, it always amazes me to see how you... a fucking computer program... can show such pure emotion."
    show aa 125
    pra "What?" with dis
    play music2b electricity fadein 2
    show aa 125b
    x "The look on your face... it was pure terror." with dis
    x "I must applaud the great work that Ulysses did when creating you. You almost look human."
    show aa 125
    pra "Say whatever you want. Your fate remains the same."
    pra "Seize her!"
    show aa 125b
    x "I think your friends are scared shitless."
    x "You should have brought more Praetorians. What's the problem? Storage space getting too expensive for all your buddies?"
    show aa 125
    pra "Enough. Your session is to be terminated and you will be excommunicated from the server."
    show aa 125b
    x "Always the same speech. Maybe you’re due for a software update, or something."
    show aa 125
    pra "You do not stand a chance against me."
    show aa 126
    x "We'll see about that..." with dis12
    stop music2b fadeout 2
    play sound2 bonecrushing
    show aa 127 with Dissolve(2.5)
    stop sound2 fadeout .5
    play sound dragonfoot
    play sound3 dragon
    pause
    play sound4 dragonfootsteps
    show aa 128 with Dissolve(2.5)
    play sound5 dragon
    x ". . ." with dissolve
    sol "S-She's a shapeshifter!"
    show aa 129
    pra "You will regret this..." with Dissolve(1.5)
    pra "All three of you."
    play sound dragonfire2
    show aa 129b with Dissolve(2)
    show novashot4 with dis12
    pause 3.7
    play soundlow steam1 fadein 1
    pause 0.3
    scene aa 130 with dis08
    pause 1.3
    play sound skeleton
    play sound2 snow
    scene aa 131 with dis
    pause
    scene aa 132 with Dissolve(1.5)
    play sound3 dragon
    pause
    scene aa 133 with Dissolve(1.5)
    pause
    scene aa 134
    sol "F-FUCK! RUN!" with dis
    sol2 "I told you we should have never accepted this job!"
    sol "I didn't even know Praetorians could be killed! At 300 eternals an hour, this was supposed to be the job of a lifetime!"
    sol2 "And now we're gonna lose everything we’ve earned in this lifetime!"
    sol2 "We should’ve just gotten those jobs at Aphrodite’s!"
    sol "I-It's okay!"
    sol "I think that bitch ran off already!"
    sol "Maintaining that form consumes a great deal of energy, she probably went to..."
    play sound3 dragonfar
    play sound2 rocks
    play sound dragonfoot
    show dragoncrush1
    x "*Crushing her to the ground*" with vpunch
    play sound2 rocks
    play sound dragonfoot
    show dragoncrush2
    x "*Tail swipe*" with hpunch
    stop music2 fadeout 10
    play music dragonfly fadein 2
    play musicb forest fadein 10
    scene aa 137b with Dissolve(2.4)
    play sound dragonfar
    pause
    show aa 137 with dis15
    mc "(Oh my fucking god...)" with dis
    mc "(They're all amazing...)"
    show aa 138
    mc "(Annie, Dalia, Luna, Nova, Alex...)" with dis12
    mc "(They're all such amazing players... while I’m here being about as useful as bacon at a vegan restaurant.)"
    play sound dragonfar
    show aa 139
    mc "(Alright. It’s time for me to start pulling my weight. From now on, I'll stop being useless.)" with dis12
    mc "(I'll go to the gym every day, study guides online, and play on my own to get experience and good items.)"
    mc "(I promise. You owe it to yourself, [mc].)"
    no "Holy shit, she's a shapeshifter! That's so cool!"
    stop music fadeout 2
    play sound snow
    show aa 140
    mc "Nova!" with dis
    no "My magic skills are near-zero. I wish I could do something like that."
    mc "Wow! Your left eye! It's blue!"
    show aa 142
    no "Ahhh... y-yeah." with dis
    no "I know it must be weird to look at, but I can’t find my patch. S-sorry."
    show aa 141
    mc "What are you talking about? I think you look even more beautiful." with dis08
    show aa 142
    no "O-Oh well, thank you." with dis08
    show aa 141
    mc "Will there be any negative side-effects for not wearing it?" with dis08
    show aa 142
    no "In the real world, I could lose my eyesight if I remove the patch for more than an hour a day. But in Eternum, luckily that can’t happen." with dis08
    no "However, I can still get a serious case of dry eye. I’d prefer to avoid that terrible agony..."
    show aa 141
    mc "Oh... let's get out of here quickly, then!"  with dis08
    play sound snow3
    show aa 143
    x "OH JESUS CHRIST, WHY IS IT SO FUCKING COLD HERE?!" with Dissolve(1.6)
    x "Where the hell did I put my damn elven robes?!"
    show aa 144
    mc "I think you left them in..." with dis
    play music2 electricity
    play sound2 snow2
    show aa 145
    x "Turn around. I dare you. It’ll be the last thing you do!" with hpunch
    no "They're over there, Alex! On that stone."
    stop music2 fadeout 1
    play sound snow4
    show aa 146
    x "Oh, that's right! Thank god..." with dis12
    play sound3 clothes
    x "Aaahh... much better..."
    show aa 147 with Dissolve(1.5)
    mc "Girls, where do I even begin?! That fight was incredible. I couldn't believe my eyes. I still can't believe it, actually." with dissolve
    mc "When you did that thing, I was like, “WHOA!” And then you did that other thing, and I was like, “WHOAAAAA!!!” And then... well..."
    mc "You. Two. Are. Amazing."
    show aa 149
    no "Thank you." (multiple=2) with dis
    x "Bah." (multiple=2)
    show aa 147
    mc "Alright, we don't know if the Praetorians can signal other AIs across servers, so we should probably escape while we can. But first..." with dis
    play sound snow3
    show aa 73
    mc "Finally." with Dissolve(1.5)
    mc "The Third Weapon of Atlas is ours."
    play music deception
    mc "Calypso." with dis
    show aa 150
    no "Do you really think the Praetorians were serious about this server not being ready?" with dis12
    show aa 151
    x "What do you mean?"with dissolve
    show aa 150
    no "I don't know, maybe everything has been a test."with dissolve
    no "Ulysses is the most powerful company in the world. If they really wanted to prevent us from getting here, don't you think they would have done it?"
    no "Discovering the location of Calypso, running the exploit to access this server, finding the village, fighting the Praetorians..."
    no "Maybe it was all part of some sort of challenge."
    show aa 151
    x "I don't know, they've never done anything like that before. I think they were really trying to keep Calypso from us."with dissolve
    x "However big and powerful they are, the Eternum universe is simply too immense. They can't be everywhere."
    x "Maybe we just got here, because... we're good. And we got lucky."
    show aa 150
    no "Extremely lucky, I'd say. What if I had missed the shot? What if you hadn't been a shapeshifter?"with dissolve
    no "Shit, what if we had started walking in the opposite direction when we were in the forest?"
    show aa 151
    x "I... I don't know."with dissolve
    x "I’d rather not think about it too much. I'll settle for not dying when we open that box."
    show aa 150
    no "D-Do you think it could be a trap?"with dissolve
    no "Like an Egyptian curse?"
    show aa 151
    x "Could be. That's why I'll open it."with dissolve
    show aa 150
    no "No, no, no. I'll open it. I won't let you die because of me."with dissolve
    menu:
        with dis
        "Ask Alex to open the box":
            show aa 152
            mc "I think Alex's right. She should open it." with dis
            show aa 151
            x "See? I'll open it." with dis
            x "If I die, you can keep my stuff and..."
        "Open the box yourself [pink][mt](Alex, Nova +1)":
            show aa 152
            mc "I didn't do shit during that fight." with dis
            mc "You guys have so much more to lose than me."
            mc "If someone has to die a horrible death by opening that box, I'd rather it be me than any of you."
            $ nova_points += 1
            $ alex_points += 1
            play sound "beat.ogg"
            show heartr at topleft
            show aa 153
            with dis
            hide heartr
            x "Well, I won't object." with dissolve
            no "Thank you, [mc]."
            x "Yes, thank you."
            no "We should..."
        "Ask Nova to open the box":
            show aa 152
            mc "I think Nova's right. She should open it." with dis
            show aa 150
            no "See?! Thanks, [mc]." with dis
            no "You discovered this server, so it's only fair. I'll open it, and if I die..."
    play sound gunload
    play sound2 snow2
    play music energy
    play sound3 impact
    show aa 154 with hpunch
    pause .5
    no "S-Shit!" with dissolve
    no "What's going on?!"
    x "I don't know!"
    x "Is it... Is it opening?!"
    play sound earringing
    play sound2 impact
    stop music fadeout 1
    stop musicb fadeout 1
    show aa 155 with Dissolve(2)
    show aa 155b with Dissolve(2)
    pause
    play music forest fadein 5
    show aa 156 with Dissolve(2)
    mc "Fuck, I can’t see!!" with dis
    show aa 157 with Dissolve(2)
    pause
    show aa 158
    mc "Hmm?" with dis
    play soundlow snow
    show aa 159 with Dissolve(1.6)
    stop music2b fadeout 6
    pause
    show aa 160 with Dissolve(1.6)
    pause
    show aa 161 with Dissolve(1.6)
    pause
    stop music fadeout 10
    play music2 calypso fadein 5
    show 02ending with Dissolve(1.3)
    pause 3.1
    play sound risingshort3
    pause 2.2
    jump versionthree


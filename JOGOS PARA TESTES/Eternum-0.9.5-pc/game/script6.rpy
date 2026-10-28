label update06:
    $ renpy.music.set_volume(1.0, channel='music')
    $ renpy.music.set_volume(1.0, channel='musicb')
    $ renpy.music.set_volume(0.5, channel='music2')
    $ renpy.music.set_volume(0.5, channel='music2b')
    $ renpy.music.set_volume(0.1, channel='music3')
    $ renpy.music.set_volume(0.6, channel='soundlow')
    hide screen heart
    scene black
    play soundloop2 worldwar fadein 8
    pause  
    play sound3 airplanewar
    show screen threeweekslater with Dissolve(3)
    pause
    hide screen threeweekslater with dis2
    pause .2
    show blurwar1 
    show screen heart
    with Dissolve(2.7)
    pause 
    play music jerryepicshit fadein 4
    $ renpy.music.set_volume(0.6, delay=10.0, channel='soundloop2')
    aaa "War." with Dissolve(2.3)
    aaa "Fear."
    aaa "Pain."
    aaa "Death."
    aaa "Every single one of you has endured more than what people could ever imagine or begin to understand."
    scene blurwar1b with dis2
    aaa "You saw your brothers-in-arms fall before you."with dis 
    aaa "You watched the light in their eyes fade away."
    aaa "One by one."
    aaa "Hundreds of soldiers just like you, with families at home, desperately praying for their safe return..."
    aaa "Only for those prayers to receive bitter answers." 
    scene blurwar1e with dis2
    aaa "I know how you feel, my brothers, for in your eyes I see the same fear that also strikes directly into my heart."with dis 
    aaa "Yes, I too am afraid."
    scene blurwar1f with dis2
    aaa "Afraid for humanity."with dis 
    aaa "Afraid {i}of{/i} humanity."
    play soundlow bombdistant2 volume 1
    aaa "I am afraid because I have witnessed the atrocities that mankind can commit on its own."
    aaa "The cries of agony from the wounded. The snapping of bones under the weight of enemy tanks."
    aaa "These sounds hauntingly whisper to me as I lay awake at night and I hopelessly fight to resist the madness that consumes me."
    play soundlow bombdistant2 volume 1
    scene blurwar1d with dis2 
    play sound2 bombdistant1
    aaa "And yet..."with dis 
    aaa "We still stand here."
    aaa "Dawn has greeted us and we live to breathe yet another breath!"
    aaa "And with that breath... we stand together."
    aaa "We keep fighting."
    aaa "No matter how loud the void calls to us, no matter how strong Death tries to grip us, we’ll hold our chins up high. We won’t look back. We'll march on."
    play soundlow bombdistant2 volume 1
    aaa "And believe me, I know very well that one question continues to persist in all of your thoughts... what are we fighting for?"
    scene blurwar1c with dis2
    aaa "Well..."with dis 
    aaa "I'll tell you."
    play soundlow bombdistant2 volume 1
    aaa "We fight for our fallen brothers."
    aaa "We fight for the loved ones eagerly awaiting our return."
    aaa "We fight for the next generation." 
    aaa "We fight... for our future."
    play sound bombfall
    pause 1.5
    scene black with flashfast
    pause  
    scene ew 5 with dis2 
    aaa "And if ultimately our luck runs out, and you finally lose the game of tempting fate..."with dis15
    aaa "Unable to live to see the future you helped shape..."
    show ew 6 
    aaa "Fear not, because I will bring you home."with dis12
    aaa "I’ll pin the medals upon your chest."
    aaa "I’ll tell your mother that you gave it your all."
    show ew 7 
    aaa "Because no matter what comes our way..."with dis12
    aaa "We fight together."
    sol ". . ."
    sol "...Who are you?"
    aaa "Hmph."
    show ew 8
    aaa "That... that’s a question I myself have struggled to answer for some time." with dis2
    aaa "People have looked to me for many things."
    aaa "A symbol of strength. A fountain of wisdom. A bastion of courage."
    aaa "*Chuckles* As flattering as it was, I never paid much attention to such things."
    aaa "But now..."
    play sound2 airplanewar
    play sound3 stairswood2 volume 1.2
    show ew 9
    aaa "*Climbing the trench* Now I’ve finally accepted who I am."with dis2
    aaa "I have finally understood... that I can no longer outrun the fate that awaits me."
    aaa "I know why I am here."
    aaa "Yes, I {i}am{/i} a hero."
    aaa "YES. I {i}am{/i} the chosen one."
    show ew 10
    aaa "I am the man to unite the lost... strengthen the weak... and embolden the fearful."with dis17
    aaa "I am the one who will lead you all to victory."
    aaa "The one who will gather the 10 Gems of Doom, sit on the throne of Eternum, and finally fulfill the prophecies! For that..."
    aaa "...is my destiny."
    play sound whoosh7
    show ew10t
    je "SO LISTEN UP, GENTLEMEN!" with hpunchlong2 
    je "Glory and honor are at hand!"with hpunch
    je "The enemy knows not what awaits them!" with hpunch
    je "Forge your names into the history books of Eternum now..." with hpunch 
    je "AND LIVE FOREVER!" with hpunch 
    play sound4 yellingsoldiers volume 1.2
    play sound5 airplanewar
    play sound6 whoosh7
    play sound7 whistlearmy
    scene ew11t
    je "CHAAAAAAARGE!!!!" with hpunchlong3
    play soundloop bombbeep
    sol "FOR ETERNUM!"with hpunch 
    sol2 "FOR THE WRE!!!!"with hpunch 
    $ renpy.music.set_volume(1.0, delay=6.0, channel='soundloop2')
    stop music fadeout 6
    je "ATTACK!!!!!!!"with hpunch 
    je ". . ."
    stop sound4 fadeout 8
    scene ew 13 
    je "Huh...?" with dis 
    scene ew14
    pause 
    scene ew 16
    je "Aw, shit."
    $ renpy.music.set_volume(0.4, channel='soundloop2')
    stop soundloop
    show ew 17
    pause .1
    play sound explosionbank
    show ew 18 with dis04
    pause .5
    show ew 17 with dis15
    play musicb ww2 
    show ew 19
    p "Oof, I think Jerry stepped on a landmine." with dis14
    play sound2 stairswood2 
    $ renpy.music.set_volume(0.6, delay=20.0, channel='musicb')
    show ew 20
    d "*Climbing the trench* Agh, fucking idiot." with dis12
    d "Why am I not surprised?"
    d "I told him not to run out into the open."
    d "At this rate, he's never gonna make it past level 10."
    show ew 21
    p "On the bright side, at least his speech seems to have motivated our troops."with dis04 
    p "Look at how they're charging."
    show ew 20b
    d "Well, that's something."with dis04
    d "Guess his pretentiousness finally provided some value."
    show ew 21
    p "Are Alex, Luna, and Nova supposed to be at the rendezvous point already?"with dis04
    show ew 20b
    d "Yeah, I think they had enough time to make it by now."with dis04
    d "Hopefully they’ve managed to take down the first defensive line of machine guns so we can have direct access to the bunker."
    play sound stairswood2
    show ew 22
    a "*Grumbling* Who on Earth built these trenches? Giants?!"with dis12
    a "These ledges are way too low... even on my tippy toes, I can barely see over! Hmph."
    a "Are we winning?"
    show ew 23
    p "Yes?"with dis04
    p "It's hard to tell from..."
    p "Uhh..."
    p "I-Is that tank aiming in our d-direction?"
    play sound explosionbank
    scene ew 24 with vpunch 
    pause .6
    play sound2 crashwood
    scene ew 25 
    bla "The three girls lose their balance and fall into the trench." with dis14
    $ unlock_look("annie", 8)
    $ unlock_look("dalia", 10)
    $ unlock_look("penelope", 13)
    d "Ouch..."
    p "O-Okay, I guess we're not going that way."
    show ew 26 
    d "Aghh... is it really worth doing all this?"with dis
    show ew 27
    p "I mean, we received pretty legit intel that a WRE rival hid a Gem of Doom in this server, so..."with dissolve
    show ew 26
    d "I know! But damn if it isn’t a drag..."with dissolve
    d "*Sighs* Anyways, I guess we should stay put until those tanks have been taken care of."
    show ew 27
    p "Was that tank even theirs?"with dissolve 
    p "It looked like an American M4 Sherman."
    p "I thought they had a Soviet arsenal and we were on the American side...?"
    show ew 26
    d "Meh, I guess everyone uses whatever is readily available or whatever they're most comfortable with."with dissolve
    d "I think one of our squads is wielding lightsabers and another is riding wyverns, so..."
    show ew 27
    p "Really? Doesn't that break peoples’ immersion?"with dissolve
    play sound chair2
    show ew 28 with dis14
    d "*Standing up* Oh yeah, because Eternum roleplay servers are all about accuracy." with dissolve
    d "I mean, have you seen how we’re dressed? Are these skimpy outfits really the best for combat?"
    play sound2 chair2
    show ew 30
    p "*Giggles* Oh, that one’s on me." with dis 
    p "I was online shopping a few weeks ago and saw all these cute outfits."
    p "I started picturing all of us as foxy G.I. Janes and I just couldn’t help myself. Mom thought they were hot too!"
    p "No matter the occasion, one should always dress sexy and stylish!"
    show ew 29
    p "Just look at you both! Girl, if looks could kill!"with dis08
    p "When you have a tummy like yours, sis, why hide it? You spend all that time getting in shape at the gym... now’s the time to flaunt it!"
    show ew 28
    d "Yeah, yeah, and my toned abs will totally deflect any bullets too."
    show ew 33
    p "Come on! You really think that ugly, baggy shirt you were gonna wear would’ve protected you any better?"
    show ew 29
    p "And besides, I see you chose the skimpiest option available! Don't think I didn't notice that..."with dis08
    p "Trying to grab someone’s attention with that sexy underboob?"
    show ew 31
    d "W-What?" with dis08
    p "*Giggles* Great choice, by the way."
    d "W-What are you talking about, t-this is the only outfit I received in my inventory!"
    p "Was it? I'm pretty sure there were a few more options to choose from..."
    d "Well, you're wrong!"
    p "If you say so..."
    show ew 32
    d "W-Why would I have chosen this willingly?!" with dis08 
    show ew 33
    p "Because it looks so spicy on you! This clothing line is so HOT!"
    p "I'm sure Annie digs it. She’s looking amazing too!"
    play sound clothes4
    show ew 34
    a "I actually do really like this outfit!" with dis08
    a "It's really comfy and I love that there are so many pockets! Why do women’s clothes never have any pockets?!"
    show ew 35
    d "Truth is, you do look really good, Annie!"
    d "But you’d look cute in anything."
    show ew 36
    a "Awww... t-thank you, girls!"with dis08
    a "That means a lot coming from you two!"
    play sound whistlearmyshort
    show ew 37b
    leg "Area, ah-ten-HUT!" with hpunch
    $ unlock_look("nancy", 8)
    show ew 37
    n "Fall in and stand at ease!"with hpunch
    play sound3 clotheswhoosh
    show ew 38
    a "Sir, yes, sir, ma’am, ready, sir, yessum!"
    a "Private Annie Winters reports!"
    play sound2 clothes2 
    play sound3 clothes2
    show ew 39
    n "AAAAAH, how can you be so adorable?!" with hpunch 
    n "You are just the cutest little pookie-bear on this server! How could anyone even think about harming such an angel?!"
    a "T-Thank you, sir, ma'am, sir."
    show ew 40
    n "Okay girls, it's your moment to shine! Are you ready?" with dis06
    show ew 42
    d "You bet we are! I was getting stir-crazy waiting here while all the fun is happening!"
    d "Can't wait to finally see some action!"
    show ew 40
    n "Excellent! I want you two to pair up and have each other’s six."
    if grimoirerest:
        n "We’re really counting on your restoration abilities, Penelope!"
    else:
        n "We're counting on you, Penelope!"
        n "This is your first real mission."
    show ew 41
    p "I won’t let you down!"
    if grimoirerest:
        p "I'm getting much better with my healing spells."
    p "Don't worry, no harm will come Dalia’s way!"
    show ew 42
    d "And I won't let anyone get close to Penny."
    d "I’m the only one allowed to beat her ass!"
    play sound stairswood2
    show ew 43 with dis
    leg "The sun has finally come out, my Empress." with dissolve 
    leg "And it appears our armored division has neutralized all enemy tanks."
    play sound clotheswhoosh
    show ew 44
    n "Alright then, NOW IS OUR CHANCE!"with hpunch
    n "Time to deliver the coup de grace!"
    show ew 45
    n "You two will flank their main squad by the river and clear the East flank."with dis
    n "Try to be as stealthy as possible. The element of surprise is our advantage here!"
    n "Meanwhile, Nova, Alex, and Luna are in charge of the North, West, and South flanks, respectively."
    n "Radio me as soon as you’ve cleared everything out."
    play sound3 clotheswhoosh
    show ew 46
    p "Yes, ma'am!" with dis03
    d "We won't fail you!"
    show ew 48
    a "What are my orders, ma'am?"
    a "I'm ready to fight!"
    show ew 47
    n "Don't worry Annie, you can come with me and help filter any received radio transmissions."
    show ew 48
    a "Yes, m–"
    show ew 49
    a "Wait, what...? Comms duty?"with dis08
    a "I wanna do badass things too!"
    show ew 50
    n "But that would be so dangerous!"
    n "You'll be safer at our base camp!"
    show ew 49
    a "Dangerous? Dangerous for who?"
    a "They’re the ones that should be worried!"
    a "Why can't I join the action with Dalia and Penny?!"
    show ew 50
    n "Well, you know, the  trenches are more for... “frontline” players."
    n "Like... the ones skilled with melee, range, or magic."
    show ew 51
    d "What Mom is trying to say is that..."with dis
    d "W-Well, we haven't really ever seen you do anything with your magic, so... we kinda assumed that you didn't have much combat experience."
    d "W-Which is good! Totally okay!"
    d "Not all Eternum players have to be fighters!"
    show ew 49
    a ". . .{w} ?"
    stop musicb fadeout 0.5
    play sound2 impact4
    show ew49
    pause .1
    scene ew 53
    a "You think I'm USELESS?"with dis12
    play musicb ww2
    scene ew 55
    n "O-Of {i}cooourse{/i} not, sweetie!"
    n "It's just that... I thought you'd be a little more useful in–"
    show ew 54
    a "Oh my god! It’s TRUE! You think I’m as useless as Jerry!"with hpunch
    p "No one said that!"
    a "How long have you guys thought of me like this?"
    a "Does everyone else think that way too?!"
    if anniepath:
        a "Oh my god, does that include [mc]?!!!" with hpunch
    show ew 55
    if anniepath:
        n "I'm sure he doesn't, Annie!"
    else:
        n "Of course not, Annie!"
    show ew 54
    a "It's not my fault!"
    a "I just haven’t had my time to shine! We always end up on either scary servers, servers where magic is disabled, or non-combat ones!"
    a "I-I..."
    play sound clotheswhoosh
    show ew 48
    a "I respectfully request to be sent to the frontline, ma'am!"with hpunch 
    a "I'll show you all what I'm capable of!"
    a "I promise!"
    show ew 55
    n "Eh..."
    n "Well, umm, o-okay then!"
    n "I guess you can go with Dalia and Penelope."
    show ew 48
    a "Yes, ma'am!"
    play sound5 airplanewar
    stop musicb fadeout 8
    show ew 56 with dis2
    n "Maximo, order the artillery to commence firing and deploy the elemental magic squad behind the tanks!" with dis08
    leg "Yes, my Empress!"
    sol2 "Hey..."
    sol2 "Yo, Cruz, I think I found that woman!"
    show ew 57
    sol2 "Yeah... it has to be her." with dis15
    sol2 "It's our chance! If we kill their leader they’ll be sitting ducks!"
    sol2 "Should I launch the Predator missile?"
    show ew 58
    sol2 ". . ."with dis14
    sol2 "*Zooming in* Yeah, it's definitely her. She matches the description."
    sol2 "Come on, Cruz, get on the radio and call the General! I need confirmation!"
    sol2 ". . ."
    show ew 59
    sol2 "For fuck's sake, dude, can you fucking focus?!"with dis
    sol2 "If we're the ones to kill that redheaded bitch we'll be recognized as heroes!"
    stop soundloop2 fadeout 9
    $ renpy.music.set_volume(0.4, channel='soundloop')
    play soundloop wind fadein 8
    show ew 60
    sol2 "Huh?" with dis12
    sol2 "(Where the fuck did everyone go?)"
    sol2 "(Did they really leave while I was on the radio?)"
    play sound screamman volume 0.25
    pause 1.2
    play sound2 chair2
    show ew 61
    sol2 "*Standing up* (What the fuck was that scream?!)"with dis12
    sol2 "CRUZ?!" with hpunch
    sol2 "Are you okay?!"
    sol2 "Don't worry, I'm coming!"
    play sound5 airplanewar volume 0.3
    show ew 62 with dis22
    sol2 "*Walking through the trenches* (What the fuck is going on...)"with dis12
    sol2 "(Did the enemy get here already?)"
    sol2 "(No... that's impossible...)"
    show ew 63
    sol2 "(I'd have heard the alarms.)"with dis12
    sol2 "(But then... where the fuck is everyone? It's almost as if–)"
    play sound tiger1
    play sound2 rungrass
    show ew63
    pause 1.1
    $ renpy.music.set_volume(0.9, channel='soundloop2')
    play music2 risinglong1 volume 0.3
    play sound3 deception
    play sound4 whoosh2
    play sound7 debris
    scene ew64
    sol2 "*Turning around* I HEARD THAT!" with hpunch 
    sol2 "I-I know y-you're there! Stop hiding!"
    sol2 "Come out you fucking bas–"
    $ renpy.music.set_volume(1.0, channel='soundloop2')
    play soundloop2 tiger2 fadein 4
    play sound debris 
    scene ew 65 with dis2
    sol2 ". . ." with dis12
    show ew 66
    sol2 "*Hyperventilating* . . ." with dis2
    play sound risingshort
    pause 1.1
    play sound3 debris
    stop music2
    stop soundloop2
    play sound2 leaves volume 0.3
    show ew 67 with dis04  
    pause
    sol2 "*Hyperventilating* (What the hell...)"with dis08
    sol2 "(T-There was something behind me, I could feel its presence.)"
    sol2 "(Okay, calm down, Lucas, you're just imagining things.)"
    sol2 "(Let's go back to base and–)"
    play soundloop2 tiger4 fadein 3
    play sound7 debris 
    play sound6 debris 
    play soundlow debris volume 1
    play sound3 tigersnarl volume 0.5
    blank ". . . ." with dis12
    play sound4 tigersnarl
    scene ew 68
    sol2 ". . ." with dis2
    play sound tiger3
    stop soundloop2
    play sound2 screammanb volume 1.2
    show ew 69
    sol2 "AAAAAAAAAAAARGH!!!!!{w=0.9}{nw}" with hpunchlong3
    play sound3 rocks
    scene ew 70 with hpunchlong2
    play sound6 debris 
    play sound7 debris 
    play music2 ["<silence 1>"]
    queue music2 ww2rock2
    stop soundloop fadeout 10
    play sound5 tigersnarl
    pause 
    play sound soldiers 
    show ew 71 with dis15
    sol "W-What the fuck is going on here?"with dissolve 
    sol2 "Why are these trenches empt..."
    play soundloop2 tiger4 fadein 1
    play sound2 tigersnarl
    play sound4 debris
    show ew 72
    sol "WHAT THE FUCK IS THAT THING?!"with dis12
    sol2 "Oh shit..."
    sol "KILL IT!!!"with hpunch
    play sound tigergunshots
    stop soundloop2 fadeout 3
    scene 05trenches with dis12
    pause 7.5
    play sound2 rocks
    scene ew 73 with dis12
    play sound3 steam2
    pause
    x "Agh... motherfucker!" with dis
    play sound5 debris
    show ew 74 with dis15
    x "(Dammit, I had to untransfigure myself sooner than I hoped.)" with dis06
    x "(Even in my tiger form, there's a limit to the damage I can take.)"
    show ew 75
    x "(Now how am I going to cover myself...?)"with dis12
    x "(I left my outfit back at the entrance of the trenches, a couple of miles from here.)"
    show ew 76
    x "(Hmm... maybe I can improvise something from those rags over there.)"with dissolve 
    play sound tear1
    show ew 77 with dis15
    play sound2 tear2
    x "Hmm..."with dissolve 
    x "(Well... better than nothing, I guess.)" 
    show ew 78
    x "(I suppose I could use one of the bloody shirts of the enemies I took out, but... ugh.)"
    x "(That's kinda gross.)"
    show ew 77
    x "(It should be okay, I think my job here is already done anyway.)"
    x "(I shouldn't find anyone else.)"
    show ew 78
    x "(Let's go back to where I left my uniform.)"
    play sound holster2 volume 1.1
    show ew 79
    sol "Hey, you!" with dis
    sol "Who the hell are you?!"
    x ". . ."
    sol "Are you deaf? Turn around!"
    show ew 80
    x "*Turning around* Ah! At last!" with dis 
    x "Thank god you finally appeared, I was starting to lose my mind!"
    show ew 85
    sol "Put your hands in the air where I can see them!"
    show ew 81
    x "I'm not doing that, can't you see I'm naked?"
    x "What are you, one of those fucking perverts that try to take advantage of women in combat servers?"
    show ew 87
    sol "Of course not!"
    sol "I just..."
    show ew 85
    sol "W-Why are you naked?"
    show ew 83
    x "Uhh..."
    show ew 80
    x "I was kidnapped. By the WRE."
    x "I managed to run away from my captors and returned to our trenches as fast as I could."
    show ew 85
    sol "And how do I know you're not lying?"
    show ew 82
    x "Why would I lie?"
    show ew 85
    sol "I don't know, to save your skin, perhaps?"
    show ew 83
    x "Well, yeah, that's a fair point."
    show ew 85
    sol "Prove you're one of ours! What's the name of our leader?"
    show ew 82
    x "Erm... General Jasper Wagner, commander of the {i}honorable{/i} Wagner Company, one of the {i}largest{/i} and {i}mightiest{/i} inter-server factions in all of Eternum."
    show ew 86
    sol "Hmm..."
    show ew 85
    sol "You could have gotten that from our pamphlets..."
    sol "Repeat after me: Glory to the Wagner Company. Fuck the WRE."
    show ew 83
    x "Uh... glory to the Wagner Company. Fuck the WRE."
    show ew 82
    x "See? Super loyal. Are we done with the interrogation now?"
    show ew 85
    sol "And one last question!"
    show ew 82
    x "*Sighs* Oh boy..."
    show ew 85
    sol "If you're one of ours you must have attended this morning's briefing."
    sol "What platoons were assigned to protect the North flank?"
    show ew 83
    x "Eh..."
    x "They were..."
    show ew 82
    x "4 and..."
    show ew 80
    x "...7?"
    show ew 86
    sol ". . ."
    show ew 80
    x "...and 10?"
    play sound holster2
    show ew 87
    sol "I KNEW YOU WERE A SPY!" with hpunch
    sol "PUT YOUR HANDS UP!"
    show ew 81
    x "You just want to see my tits!"
    show ew 85
    sol "Enough games!"
    sol "Do as I say or I'll put a bullet in your pretty face, you fucking b–"
    play sound2 gunshot
    show ew 88 with hpunch
    pause .2
    play sound3 ["<silence 0.4>", fall3]
    play sound4 ["<silence 0.4>", fall]
    show ew 88b with dis
    pause .3
    play sound5 spell4
    show ew 89 with flashfaster
    pause .3
    no "Never stand still on a server with snipers!"with dis
    no "That's Warfare 101!"
    show ew 84
    x ". . ."
    show ew 80
    x "Damn girl, I've never been happier to see you!"with dis04
    x "Good shot!"
    show ew 91
    no "*Giggles* Thank you, thank you!" with dis
    $ unlock_look("nova", 10)
    show ew 92
    no "I spotted him over a mile away but I didn't..."with dis04
    no "I didn't..."
    show ew 93
    no "W-Why are you naked?"with dis06
    show ew 83
    x "I received a near-fatal wound in my tiger form, so I had to untransfigure."
    show ew 82
    x "Then that soldier caught me off guard, so I was trying to buy some time."
    x "I need a few minutes before being able to transform again, especially if I used a powerful creature."
    show ew 93
    no "Like... some sort of refractory period?"
    show ew 80
    x "*Snorts* Yeah, pretty much."
    show ew 93
    no "I see... cool."
    show ew 80
    x "Alright! The whole Western flank should be clear. I think the guy you killed was the last one."
    show ew 92
    no "Cool! I also wiped out the North flank completely!"
    no "I was coming this way to help when I saw that man pointing his gun at you."
    show ew 83
    x "Okay, so... if everything is going according to plan in the other flanks, the enemy must be about to send the rest of their men this way."
    x "We should radio Nancy."
    show ew 92
    no "Yep! We..."
    play sound phone
    pause .6
    show ew 94
    no "Oh, speaking of the devil... someone is calling on the walkie."with dis08
    no "Must be Nancy."
    play sound beep2b
    show ew 95
    no "Moshi moshi?"with dis08
    play sound3 w1
    show ew 96
    a "Nova?" with pushr
    show ew 97
    no "The one and only!"
    d "Hello?"
    p "Annie?"
    n "Is everything okay?"
    show ew 96
    a "Yes, it's me!"
    a "Check the coordinates I sent you and look in that direction!"
    show ew 97
    no "Wait, let me find a vantage point!"
    x "Do you need backup? We're too far!"
    show ew 98
    a "No, no! Just look in that direction!"with dis
    a "There's a huge enemy patrol by the bridge, with tanks and tons of vehicles and infantry."
    play sound spell
    show ew 99
    a "*Giggles* Now watch this..."with dis
    n "Watch what?"
    d "I don't have line of sight on the bridge!"
    a "No worries! Just look in the direction I sent you!"
    a "*Mumbling* I'm gonna make an explosion so big that they'll be able to see it from every corner of the server."
    a "3..."
    a "2..."
    play sound bombfall
    a "1...{nw}{w=1.4}"with dis
    play soundlow explosion2
    $ renpy.music.set_volume(1.0, channel='soundloop')
    play soundloop fireplace fadein 1
    show ew 100 with flashfaster
    show ew 100 with hpunchlong3
    show ew 101 with dis15
    pause .5
    a "W-What...?"with dis06
    play sound beep2b
    leg "Impact confirmed! Enemies neutralized!"
    n "Oh! That's why you sent the coordinates!"
    p "Nice job, Annie!"
    d "Great spotting! See? That was very useful!"
    x "That was a big explosion indeed!"
    no "You rock, Annie!"
    a "Wait, wait, wait... that's not what I wanted to..."
    show ew 102
    a "G-Goddammit!" with dis
    a "(Now I seem even more useless than before.)"
    a "(Why am I so damn unlucky?!)"
    show ew 103
    a "(Okay, calm down Annie, I'm sure there are more enemies somewhere.)"with dissolve
    show ew 102
    if anniepath:
        a "(But if no one sees me doing it, they won't believe me and there won't be anyone to tell [mc] how awesome I can be!)"with dissolve
        show ew 103
        a "(Maybe I could play with [mc] in one of the magic servers I used to play in?)"with dissolve
        show ew 102
        a "(But I don't want the girls to think I'm useless either!)"with dissolve
        a "(Come on, Annie, let's find more enemies and blast them with a nuclear orb that obliterates everything within a half-mile radius!)"
    else:
        a "(But if no one sees me doing it, they won't believe me!)"with dissolve 
        a "(Come on, Annie, let's find more enemies and blast them with a nuclear orb that obliterates everything within a half-mile radius!)"
    a "(Let's go!)" with hpunch 
    stop music2 fadeout 7
    $ renpy.music.set_volume(0.6, channel='soundloop2')
    play soundloop2 wind fadein 7
    show ew 104b with dis25
    pause
    sol "*Yawns* Dude, what time is it?"with dis08
    sol2 "On this server? Like, 8 AM."
    sol "And in the real world?"
    sol2 "I don't know, probably like 6 or 7 PM."
    show ew 104
    sol "*Yawns* Aaaagh. God, this is so boring." with dis15
    show ew 105
    sol "Dude, we got the worst flank. No one passes through here."with dissolve
    show ew 106
    sol2 "Stop calling me dude. And stop complaining so much." with dissolve
    sol2 "We literally get paid to stand here doing nothing."
    sol2 "Would you rather be at a nine-to-five job working like a slave for minimum wage?"
    show ew 105
    sol "Well, I guess not." with dissolve
    sol "I just think that we could have been deployed to a more entertaining position."
    show ew 106
    sol2 "Someone has to protect the South flank."with dissolve
    show ew 107
    sol "Dude, if a fucking army was coming this way we'd see them from..."with dis06
    show ew 108
    sol "Huh?"
    show ew 109
    sol "What the..." with dis
    sol2 "A girl?"
    play sound holster2
    play sound3 clotheswhoosh
    show ew 112
    sol "D-Don't move!"with hpunch
    sol "Identify yourself!"
    $ unlock_look("luna", 9)
    show ew 110
    pause
    show ew 112
    sol "Why isn’t she talking?"
    show ew 111
    sol2 "You lost, cutie?"with dis04
    show ew 110
    sol2 "Are you with the Wagner Company or the WRE?"
    sol2 "Eh?"
    show ew 111
    sol2 "You know what, let's go to my tent."
    sol2 "You must be cold and scared. Don't worry, we can warm up there for a bit and then I'll take you to the nearest Exit Portal."
    show ew 113
    sol "Dude, what the fuck is wrong with you?"with dis04
    sol2 "What now?"
    sol "That sounded like you're about to assault her in that filthy tent of yours."
    sol2 "What the fuck are you talking about?! I just invited her to warm up in my tent, that's all."
    sol "It sounds... wrong. She's clearly confused and probably scared."
    sol2 "And that's why I offered it."
    sol2 "Go play the moral police on another server. We're just two adults... I'm doing nothing wrong."
    show ew 111
    sol2 "I mean... because you're already an adult, right, cutie?"with dis04
    play sound spell
    play soundloop pulse fadein 1
    show ew 114 with dis
    sol "W-What's she doing now?"with dissolve
    sol2 "I don't know... maybe she's a spy after all."
    play sound deception
    show ew 115
    l "*Taking a deep breath* . . ."with dis08
    sol "I told you!"
    sol "Fuck, should we sound the alarm?"
    sol2 "Of course not, don't be a fucking pussy. It's just one chick."
    sol2 "Shoot her."
    show ew 113
    sol "What?! Why me?"
    sol2 "Because I am your superior and I am giving you a direct order."
    sol "But... she's just a girl..."
    sol2 "This is supposed to be a war. People die. Get over it."
    show ew 116
    l "Increarbus severum."with dis 
    sol2 "And now she's saying gibberish! Shoot already, for fuck's sake!"
    show ew 117
    sol "Agh, fuck!" with dis
    sol "This is the last time I play with you."
    sol "Sorry, kid."
    stop soundloop
    play sound shoot
    play sound7 shoot
    show ew 118 with flashfaster
    pause 
    show ew 119
    sol "Hmm...?" with dis
    play sound2 steam2 fadein 2
    play music russia fadein 6
    stop soundloop2 fadeout 14
    show ew 120 with dis25
    pause 
    show ew 120b
    ana "You opened fire on the mistress." with dis12
    play sound robot2
    show ew 121 with dis 
    ana "Such uncivilized behavior."with dissolve 
    show ew 122 
    sol "W-Where did that come from?" with dis 
    sol2 "What the fuck is that thing?"
    play sound debris
    play sound2 whoosh7
    play sound3 robot0
    scene ewrob1
    ta "Thing?"with hpunch 
    ta "He called us {b}things{/b}, sister."
    sol "F-Fuck! There are more of them!"
    play sound debris
    play sound2 whoosh7
    play sound3 robot0
    scene ewrob2 
    ana "Discourteous." with hpunch 
    ta "Boorish."
    ana "Uncivilized."
    ta "{b}So{/b} uncivilized."
    sol2 "O-Okay, let's calm down everyone..."
    play sound robot0
    play sound2 whoosh6
    show ew 125
    ta "You shouldn't smoke."with hpunch 
    ana "It is bad for your health."
    ta "It is filthy."
    ana "Unsophisticated."
    ta "Uncivilized."
    play sound implodeb
    show ew 126 with dis
    play sound2 steam3
    show ew 127 with dis
    sol2 "H-Holy fuck..." with dissolve
    show ew 128
    sol2 "Are you gonna just stand there doing nothing?! Shoot them!" 
    sol "Ah, y-yes!"
    play sound debris
    play sound2 whoosh7
    play sound3 robot0
    scene ewrob3
    ana "Firearms are barbaric."with hpunch
    play sound implodeb
    show ew 130 with dis
    play sound2 steam3
    show ew 131 with dis
    sol "AAAGH! FUCK, IT BURNS!" with dissolve
    ana "Primitive."
    ta "Coarse."
    ana "Uncivilized."
    play sound7 holster2
    show ew 132
    sol2 "Enough! I'll end this myself!"with hpunch 
    show ew 133
    sol2 "Die, you fucking pieces of junk!"
    play sound shoot
    show ew 134 with flashfaster
    pause .3
    play sound2 shoot
    show ew 135 with flashfaster
    pause .1
    play sound3 shoot
    show ew 136 with flashfaster
    pause .3
    play sound4 shoot
    show ew 137 with flashfaster
    pause .2
    play sound5 shoot
    show ew 138 with flashfaster
    pause .3
    play sound6 shoot
    show ew 139 with flashfaster
    pause .6
    play sound steam2
    show ew 140 with dis
    pause 
    ta "He shot at us." with dis06
    ana "Loutish."
    ta "Mannerless."
    ana "Uncivilized."
    play sound robot2
    play sound2 clothes5
    show ew 141 with dis12
    stop sound2 fadeout 1
    sol2 "W-What are you doing?" with dis08
    sol2 "Get away from me!"
    play sound3 bonecrush2
    play sound4 robot0
    show ew 142
    sol2 "AAAAAAAAAARRRRGHhhhhHHH!!!" with vpunch
    play sound fall3
    play sound2 fall
    play sound3 fall2
    show ew 143
    sol2 "Agggh!! F-FUCK! This fucking bitch broke my arm!" with dis
    play sound robot2
    show ew 144
    ta "Enough pleasantries." with dis12
    sol2 "Please, don't kill me!"
    play sound implodeb
    play soundlow steam2
    show ew 145 with dis
    ta "That depends on you."with dissolve 
    ta "We need access to the main bunker of your general."
    sol2 "Eh?? O-Of course!"
    sol2 "I-I know the way to get in!"
    sol2 "There's a back entrance through the sewer system!"
    sol2 "Then there’s a small door locked by an access code, the PIN is 77463!"
    show ew 146
    sol "Dude, come on!"
    sol "You're a rat!"
    show ew 147
    sol2 "Shut the fuck up, I'm not gonna die because of a guy I don't give a shit about."
    play sound robot2
    show ew 144
    ta "Your disloyalty is despicable."with dis
    sol2 "W-What? I told you what you wanted!"
    ta "Indeed. Contemptible nonetheless."
    play sound robot2
    show ew 148
    ana "We got the information required, mistress." with dis12
    show ew 149
    l "Thank you, girls!"
    l "I'll pass along that info."
    show ew 148
    ana "Shall we commence Operation Spark?"
    show ew 149
    l "Yes, let's clear the South flank!"
    show ew 148
    ana "It shall be done, mistress."
    play sound robot
    play sound2 clotheswhoosh
    show ew 150
    ta "We will bring this specimen with us."with dis08
    sol "L-Let me go!"
    ta "We can use him to spot enemy locations."
    show ew 152
    sol2 "And what about me?"
    sol2 "You can't leave me here like this! This is torture!"
    play sound robot2
    show ew 151
    ta "Torture?" with dis 
    ana "We do not torture."
    ta "That would be graceless."
    ana "Uncivilized."
    show ew 152
    sol2 "Then what? Are you gonna kill me?!"
    show ew 151
    ana "Our brother will take care of you."
    ta "You will like him."
    ana "He is so refined."
    ta "Cultured."
    ana "Professional."
    ta "Civilized."
    ana "{b}So{/b} civilized."
    show ew 152
    sol2 "What?! Are there more..."
    play soundlow dragonfoot volume 0.15
    show ew 153 with dis12
    play sound dragonfootsteps fadein 1
    show ew 153 with vpunch
    pause .8
    show ew 153 with vpunch
    pause .8
    show ew 153 with vpunch
    pause .6
    play sound2 debris
    play soundloop monsterbreath2
    show ew 154 with dis08
    pause
    show ew 155 with dis17
    pause
    play sound5 monsterbreath
    show ew 156 with dis15
    play sound6 monster2
    phh "{sc=1.4}{b}The time of judgment has come.{/sc}"  with dis12
    sol2 "{sc=1.4}*Sobbing* . . .{/sc}"
    stop soundloop fadeout 6
    stop music fadeout 7
    play soundloop2 cave
    scene black with dis25
    show screen meanwhile with dis12
    pause
    scene eww 1 
    hide screen meanwhile
    with dis22
    pause
    play sound bombdistant1
    play sound2 debris
    play sound5 debris2
    show eww 1 with vpunch
    pause
    show eww 2 with dis15
    play sound3 bombdistant2
    play sound4 debris
    show eww 2 with vpunch
    pause
    show eww 3
    sol "Sir, I received reports from all the flanks!" with dis
    play sound6 bombdistant1
    play sound7 debris
    play sound debris2
    show eww 3 with vpunch
    show eww 5
    wag "And?"with dis
    show eww 4 
    sol "North, East, and West flanks have fallen!"
    sol "The South flank still holds, but communications were interrupted. We don't know what happened."
    show eww 5
    wag "Dammit..."
    wag "We underestimated the WRE."
    show eww 6
    wag "Okay, listen up, soldier!"with dis
    wag "Gather all our remaining units and bring them in here!"
    wag "We'll fortify our defenses and hold position in this bunker!"
    show eww 7
    sol "Yes, sir!"with dissolve
    show eww 6
    wag "It doesn't matter if they have more firepower. No one has ever taken the Wagner bunker and today will be no exception!"with dissolve
    wag "I want all our men to form a barricade around both entrances! Post up troops there and there!"
    wag "NOW!"
    show eww 7
    sol "Copy that, sir! Moving out!"with dissolve
    sol "I'll pass along the orders, sir!"
    play sound run
    show eww 8
    bla "The soldier rushes out of the bunker." with dis15
    wag "*Sighs* Fuck..."
    wag "If it all goes wrong, I'll have to take the hidden escape route and leave alone. I can't afford to lose it."
    wag "I can organize a comeback with the units that couldn't play today."
    play sound coinflip
    mc "Damn, and you'd leave all your men behind?"
    mc "That's kinda selfish, isn't it?"
    show eww 9
    wag "What the..."with dis08
    show eww 10 with dis
    play sound2 coinflip
    show eww 11 with dis06
    pause .1
    show eww 10 with dis04
    pause .4
    show eww 12
    mc "I mean, I wouldn't do it, but I guess I'm not one to judge." with dis
    show eww 9
    wag "Who the fuck are you...?"
    play sound debris
    show eww 14
    mc "*Standing up* Me?" with dis
    show eww 15
    mct "Mmmm... should I tell him my real name?"with dis08
    mct "Do I wanna be famous or stay under the radar? Could be a good opportunity to make a name for myself..."
    mct "Maybe it's time to finally go with the name I came up with the other day."
    menu:
        with dis
        "Heracles":
            $ nickname = "Heracles"
        "Nobody":
            $ nickname = "Nobody"
        "Eros":
            $ nickname = "Eros"
        "Other":
            $ nickname = renpy.input("How should I call myself?", exclude='\\[]{')
    $ nicknameunlock = True
    show eww 14
    mc "I am... [nickname]."with dis
    show eww 13
    wag "[nickname]?"
    show eww 14
    mc "That would be me."
    show eww 13
    wag "Huh. Well, tell me, [nickname]..."
    wag "How did you get past all my security checkpoints?"
    show eww 14
    mc "I went through the sewer system."
    mc "It's obviously not a viable option for an entire army, but it was perfect for a one man job."
    show eww 13
    wag "And the double-barricaded door? How the hell did you get the access code?"
    show eww 14
    mc "Your men snitched at the drop of a hat."
    mc "Loyalty doesn't seem to be your faction’s forte."
    show eww 13
    wag "I see..."
    wag "Very clever."
    wag "And what now? Did you come to kill me?"
    show eww 14
    mc "No one has to die."
    mc "All you have to do is surrender."
    mc "You've already lost, Wagner."
    show eww 13
    wag "Of course..."
    wag "Well, I guess I have no choice left."
    wag "Let's go to the command center, I'll order the withdrawal of my troops. You have my word."
    show eww 17
    mc "Good choice."
    show eww 13
    wag "But you must lay down your weapons."
    wag "I want assurances that you won't kill me after I've sent the orders."
    wag "I'll only agree to your terms if we both go unarmed."
    show eww 18
    mc "That seems fair." with dis
    play sound gundrop
    play sound2 ["<silence 0.3>", debris]
    show eww 19
    mc "*Dropping the gun* That pistol was the only..."with dis
    play sound3 gunload
    show eww 20
    mc ". . ." with dissolve
    show eww 21 
    mc "What...? Are you serious?" with dis
    show eww 22
    mc "You gave me your word! Where's your honor?!" with dis
    show eww 23
    wag "Graveyards are full of honorable people."
    wag "I don't give a fuck if I have to use despicable methods to achieve my goal."
    wag "I always win."
    show eww 22
    mc "The WRE will take you down whether you kill me or not. Your army is finished."
    show eww 23
    wag "We both know this is not about the war."
    show eww 22
    mc "What...?"
    show eww 23
    wag "The WRE only attacked after it was made public that I possessed a very valuable item."
    wag "I know this is not a coincidence."
    show eww 22
    mc "I-I don't know what you're talking about."
    play sound2 clothes3
    show eww 24
    wag "*Chuckles* Oh, really? Let me remind you, then..."with dis 
    play sound clothes3
    show eww 25
    play soundloop deception
    wag "Ring a bell?" with dis 
    show eww 27
    mc ". . ."with dis
    show eww 26
    wag "I guess I am right."
    wag "Don't blame yourself, boy. Everyone wants the Gems, but only the best player can gather them all."
    wag "It was a valiant effort though, I'll admit."
    show eww 28
    mc "*Sighs* Okay... you got me."with dis
    wag "*Laughs* I knew it!"
    show eww 29
    wag "You know what, I like you."with dis 
    wag "I'll offer you a deal: if you start working for me, I'll spare your life and you'll be able to keep your level and inventory."
    wag "What do you say?"
    mc ". . ."
    mc "Fuck you."
    wag "Huh."
    wag "So you choose... death."
    wag "Disappointing."
    play sound2 glitch4
    show caveglitch
    wag "In Eternum, there are no second chances."
    wag "Remember that when you're dead."
    mc ". . ."
    wag "Game. {w}Over."
    stop soundloop
    stop soundloop2
    play sound7 impact4 volume 0.7
    stop soundloop
    stop soundloop2
    play sound shotanimation 
    show 06shoot
    pause 5.2
    play music2 epic3 fadein 4
    play sound5 steam2
    scene eww 30 with dis12
    pause 
    show eww 31
    wag ". . ." with dis17
    show eww 32
    wag "What...?" with dis
    show eww 33
    wag "How..."with dis 
    play sound debris 
    show eww 35
    mc "*Standing up* Your reflexes seem somewhat slow, eh?"with dis 
    show eww 35b
    wag "How... this bunker has..."
    show eww 35
    mc "This bunker has a magic blocker. We know."
    mc "I'd tell you how we're avoiding it, but that would ruin the mystery, don't you think?"
    show eww 35b
    wag "How did you know that..."
    show eww 35
    mc "We know everything about you."
    mc "We knew how you'd deploy your troops..."
    mc "How many men you had..."
    mc "Hell, we even knew about your favorite online platforms, your passwords, and your... concerning fixation on cat girls."
    show eww 36b
    wag "I-I don't know what you're talking about."
    show eww 35
    mc "We knew you'd be alone in this bunker, and that you'd have the Gem in your possession."
    mc "You lost this war before you even started it."
    show eww 36 
    play sound3 spell3
    play sound2 spell2
    play soundloop energy2 fadein 1
    mc "But anyway... I'd love to stay and chat, but I'm a terribly busy man."with dis12
    show eww 35b
    wag ". . ."
    wag "Who the fuck are you?"
    show eww 37
    mc "I told you already, have you forgotten?"
    mc "I'm [nickname]."
    mc "Don't forget that name... you'll hear it again."
    play sound3 spell3
    play sound2 spell2
    show eww 38 with flashfast
    stop soundloop
    pause
    show eww 35b
    wag ". . ."with dis 
    play sound soldiers
    play sound2 whistlearmyshort
    show eww 39 with dis17
    sol "SIR!" with dis14
    sol "All entrances to the bunker have been secured!"
    sol "Reinforcements are on the way!"
    show eww 40
    wag "He took it..."
    show eww 39
    sol "Sir...?"
    show eww 41
    wag "HE TOOK MY GEM!" with hpunch 
    wag "Find the fucking traitor who allowed that intruder to bypass my magic blocker and bring them to me!"with hpunch
    wag "The rest of you! Sweep the place until you find that thief!"with hpunch
    wag "He couldn’t have gone too far!"with hpunch
    play sound woodcrack
    pause 1
    play sound2 rocks
    play sound4 debris2
    stop music2 
    play soundloop2 cave
    show eww 41 with vpunch
    pause .5
    show eww 42
    wag "WHAT NOW?!" with dis
    sol2 "*Whispering* Did..."
    sol2 "Did that man fall through the roof...?"
    sol "*Whispering* Impossible, there must be like 150 or 200 feet of sheer rock."
    play music drums fadein 2
    stop soundloop2 fadeout 10
    show eww 43 with dis17
    pause
    play sound5 debris
    show eww 44 with dis17
    wag "Wait... I know you..."with dis
    tha "Where is the Gem of Doom?"
    wag "Y-You're Thanatos, aren't you?"
    sol2 "*Whispering* Oh my god, I can't believe it's him..."
    sol "*Whispering* I thought he was a myth!"
    sol2 "*Whispering* T-They say he's level 100..."
    sol "*Whispering* I've heard he stabs his own back with an arrow every time he kills 1000 people!"
    play sound sigh
    show eww 45 with dis12
    tha "I said, where is..." with dis
    tha "The Gem."
    wag "The Gem...? You're too late! Someone just stole it from me!"
    tha ". . ."
    tha "Who."
    wag "Join my army and we'll take it back together!"
    play sound sigh
    play sound2 debris
    show eww 46 with dis14
    tha "Who." with dis
    wag "Um... I don't know, he called himself... “[nickname]”."
    tha ". . ."
    play sound3 debris
    show eww 45
    tha "Then you're no longer useful to me. Open the gates."with dis12 
    play sound gunsload
    play sound2 holster2
    play sound3 holster
    wag "Now, now, now... not so fast, Thanny."
    show eww 47
    wag "The goddess of fortune smiles upon us once more, boys!"with dis
    wag "We may have lost one Gem of Doom today, but 5 new ones just so happened to arrive on our doorstep! Isn't that marvelous?"
    show eww 46
    wag "Hand them over, Thanatos."with dis
    wag "I might even let you live so you can keep your level, out of courtesy."
    play sound gunsload
    play sound2 soldiers volume 0.5
    play sound3 holster
    show eww 48 with dis12
    pause
    play sound4 holster
    show eww 49
    bla "Thanatos slowly moves his left arm, grabbing the hilt of his sword." with dis12
    wag "You're outnumbered fifty-to-one, Thanatos."
    wag "Don't even try it."
    play sound2 sword
    $ renpy.music.set_volume(0.4, channel='soundloop')
    #play soundloop electricity fadein 5
    show eww 50 with dis2
    pause
    sol "Is that..." with dis
    sol2 "...Hyas?"
    wag "ARE YOU STUPID?!" with hpunch
    wag "Is this how you want your legendary tale to end?!"
    wag "Surrender and drop your weapons!"
    wag "You don't stand a chance, you're completely surrounded!"
    play sound sigh
    show eww 51
    tha "Surrounded?"with dis2
    show eww 50
    tha "All I am surrounded by... is fear." with dis2
    show eww 52
    tha "{b}And dead men." with dis2
    play sound risingshort4
    show eww 50 with Dissolve(2.2)
    pause .1
    stop soundloop fadeout 1
    stop music fadeout 1
    play sound2 impact3
    play sound3 gore
    play soundlow shootecho volume 0.4
    scene tha06f
    pause 3.2
    play soundloop forest2 fadein 9
    scene aa 12 with Dissolve(4.5)
    pause 
    mct "Mmmm..."with dis08
    mct "Fuck, I lost consciousness again."
    play sound snow
    show ep 1
    mc "*Standing up* (Well, at least now I'm capable of controlling my powers without going berserk.)"with dis12
    mct "And I feel more powerful every day. That dude didn't even see it coming!"
    mct "Step by step, [mc]."
    mc "*Taking a deep breath* Ah, is this Ogygia's forest? This place is beautiful!"
    play sound snow
    play music2 ["<silence 1.6>"]
    queue music2 quirky4 fadein 5
    show ep 2
    bla "You turn around and see Calypso swinging her legs over the edge of a rock."with dis15
    menu:
        with dis
        "But not as beautiful as the Elven Princess that stands in front of me!\n[calypso_pts]":
            mc "But not as beautiful as the elven princess that stands in front of me!"with dis06
            $ calypso_interest += 1
            show ep 5
            ca ". . ."
            show ep 2
            ca "Hmph."
        "Although a bit cold. Wasn't there somewhere warmer?":
            mc "Although a bit cold. Wasn't there somewhere warmer?"with dis06
            show ep 3
            ca "It is not my fault that your species cannot withstand the cold." 
            show ep 2
            mc "*Chuckles* Fair enough."
        "Why the long face, my Princess? [calypso_pts]":
            mc "Why the long face, my Princess?"with dis06
            $ calypso_interest += 1
            show ep 3
            ca "I have had the same face for the last 84 years."
            show ep 2
            mc "Well, I assume you were also born a baby like us humans, but... fair enough."
    mc "I've gotta say, that was a great success!"
    mc "I can't believe we have 2 Gems already."
    mc "We're getting closer to our goal every day."
    ca "Mm-hm."
    mc "Should we jump to another server now? I need to find an Exit Portal."
    show ep 3
    ca "I have already made you appear near one of those artifacts of yours."
    show ep 4
    mc "*Turning around* Huh?"with dis
    mc "Oh, true, I see it! Wonderful."
    show ep 5
    mc "I guess I should leave then. The girls must be wondering how everything went."with dis08
    show ep 2
    ca "Hmph."
    mc "Are you okay...?"
    show ep 3
    ca "I am."
    show ep 2
    mc "You don't look okay. Are you mad about something?"
    mc "Is it because I went on for too long with my speech in front of the general? I'm sorry, I get carried away at tim–"
    show ep 3
    ca "I am not. Stop insisting I am unwell."
    show ep 2
    mc "Well, okay then."
    mc "I won't insi–"
    play sound snow2
    show ep 9
    ca "*Standing up* Alright, maybe I {i}am{/i} kind of annoyed."with dis08
    show ep 10
    mc "Oh."
    mct "That's an interesting dress... God bless elven tailoring."
    show ep 9
    ca "Do you know who I am?"
    show ep 10
    mc "Uhh..."
    show ep 9
    ca "Because you clearly do not seem to understand it yet."
    ca "Ever since our paths crossed, I have been essentially functioning as your personal maid. Me! The Princess of Hyril'ar!"
    play sound snow
    show ep 8
    ca "{i}Calypso, create a portal here so we can safely escape! Calypso, help us jump  between servers so we can deceive our enemies! Oh Calypso, please craft a portal here so we can outrun the authorities!"with dis08
    play soundlow snow2
    show ep 6
    ca "I am the Princess of the Sy-tel-quessir!"with dis08
    ca "Yes, I owed you my freedom, but I only chose to help you because our relationship was supposed to be mutually beneficial."
    ca "I will never attain any information about my realm if all I do is serve as your escape route in a quest to find Gems I do not care about."
    show ep 7
    mc "*Gulps* I didn't know you felt that way."
    mct "I guess she has a point. I haven't really stopped to think much about her since we found her."
    show ep 6
    ca "I have heard the farmers and villagers mentioning my name. They say I am a {i}weapon. A {i}tool."
    ca "How dare they... I obey no one!"
    show ep 7
    mc "Where did you hear that?"
    play soundlow snow2
    show ep 9
    ca "In the same filthy inn where you abandoned me weeks ago, where else?" with dis08
    ca "I practically memorized the wood patterns of the floorboards within my chambers!"
    show ep 10
    mc "I can explain that!"
    mc "I went overseas to visit my father and grandparents for a couple of weeks, and I've been so busy!"
    mc "I just came back to Kredon yesterday!"
    mc "That's why I've been more distant."
    show ep 9
    ca "That is a lie!"
    ca "I know you have been visiting these worlds too."
    show ep 10
    mc "Well... yeah, occasionally. I took the E-suit with me."
    mc "But it was mostly to play alone and practice my magical abilities!"
    mc "I wanted to keep up with the girls and..."
    mc "Wait, how do you know I've been playing Eternum?"
    show ep 9
    ca "I could sense when you left what you call the “real world” and appeared in another realm."
    ca "Whether it was the desert, the grotto, or the jungle."
    ca "And even if you {i}think{/i} you have improved, your technique is still reminiscent of a lumbering ogre!"
    show ep 10
    mc "So..."
    mc "You've been following me around and spying on me?"
    show ep 11
    ca ". . ." with dis
    play sound snow
    show ep 12
    ca "O-Of course not!" with dis
    ca "I just... wanted to..."
    ca "I was curious. And bored. That is all."
    show ep 13
    mc "*Chuckles* Hey, it's fine. Never be ashamed of wanting to satiate your curiosity..."
    ca "Hmph."
    show ep 12
    ca "But anyway, let us get back to the issue at hand..."
    show ep 13
    mc "Of course."
    mc "What exactly is your wish, my Princess?"
    show ep 12
    ca "I want to be informed of your goals and plans."
    ca "And I want to go with you on the next mission, as an active participant, not a getaway portal."
    ca "The more I discover about the different realms, the sooner I will be able to return home."
    show ep 13
    mc "Fair enough."
    mc "About the information you want... well, we discovered that some people who apparently died in our world are able to keep existing inside Eternum."
    mc "Thanatos, the man who attacked you here in Ogygia, is apparently one of them."
    mc "My theory is that Ulysses found a way to... “digitize” human consciousness somehow."
    mc "But I honestly don't know, it all still sounds too unreal to me."
    show ep 12
    ca "I... see."
    ca "And what is the next step?"
    show ep 13
    mc "We're still trying to gather the 10 Gems of Doom in an attempt to unravel all the mystery. They're the key to this whole thing."
    mc "Nancy is using her connections to discover the possible locations of the other Gems."
    show ep 12
    ca "Good. I like Miss Nancy. She is also a powerful ruler."
    show ep 13
    mc "So you want me to “summon” you next time we're on a mission?"
    mc "We'll probably be playing again tomorrow."
    show ep 12
    ca "Yes. I mean... no. I will come to you."
    ca "Tomorrow is good. I will prepare."
    show ep 13
    mc "Cool! Let's do that."
    show ep 12
    ca "Yes. {i}Cool."
    play sound3 spell3
    play sound2 spell2
    play soundloop2 energy2 fadein 1
    show ep 14 with dis12
    ca "I will see you tomorrow then."with dis06
    ca "If that is all, I shall be on my way. Farewell, [mc]."
    show ep 15 
    menu:
        with dis
        "Informal farewell":
            mc "Sounds good!"with dis06
            mc "Can't wait to team up with my favorite elven princess!"
            show ep 18
            mc "High-five!"with dis08
            show ep 19
            ca ". . ." with dis
            play sound3 spell3
            play sound2 spell2
            stop soundloop2 fadeout 1
            stop music2 fadeout 1
            show ep 17 with flashfast
            mc ". . ." with dis
            mct "Too soon."
        "Formal farewell [calypso_pts]":
            $ calypso_interest += 1
            mc "*Bowing down* For the greater good of Hyril'ar, I pledge to lay my life down for my Princess and satisfy each one of her desires."with dis06
            show ep 16
            ca "Hmph." with dis08
            play sound3 spell3
            play sound2 spell2
            stop soundloop2 fadeout 1
            stop music2 fadeout 1
            show ep 20 with flashfast
            pause .4
            mct "That “hmph” sounded more playful than the angry ones of before." with dis
            mct "I'll take this as an elven gesture of approval."
    play sound snow3
    show ep 4 with dis17
    mct "Well, time to get back to the real world." with dissolve 
    mct "Can't wait to tell the girls that I got the Gem!"
    mct "2 in my pocket... just 8 more to go!"
    stop soundloop fadeout 4
    play sound risingshort4
    scene login3 with dis2
    pause 6
    play soundlow whoosh4
    scene white with dissolve
    play soundloop rain3 fadein 5
    scene ep 21 with dissolve
    play sound2 beep
    pause 
    play sound3 plugin
    play sound4 clothes3
    mc "*Removing your E-Visor* (Ah, that sound...)" with dis06
    mct "I kind of missed Kredon's rain."
    mct "As long as you stay indoors, it's the best feeling in the world."
    play music2 happy13 fadein 11
    stop soundloop fadeout 15
    d "[mc]?!" 
    play sound run
    show ep 22 with dis12
    stop sound fadeout 1
    d "[mc]!" with dissolve 
    mc "Hey Dalia!"
    d "He's back!"
    play soundlow punch 
    show ep 23
    p "[mc]!" with hpunch 
    p "How did it go?"
    mc "I–"
    play soundlow punch
    show ep 24
    n "[mc]?!" with hpunch  
    n "What's the mission status?"
    mc "Well, I–"
    a "[mc]!"
    play sound clothes3
    show ep 25 with dis 
    a "*Popping in from between Nancy's thighs* And?!" with dissolve 
    $ unlock_look("annie", 9)
    n "Did you get it?"
    mc "I–"
    a "Oh no, he killed you, right?!"
    a "I knew you shouldn't have gone alone!"
    show ep 26
    d "Why aren't you saying anything?!" with dis
    a "Because he died!"
    p "Oh, really??"
    n "Oh god, I SENT HIM TO HIS DEATH!"
    show ep 27
    mc "Okay, okay, calm down everyone... I HAVE IT!"with dis08
    mc "We got a second Gem of Doom, ladies!"
    show ep 53
    a "*Gasps* Oh."
    show ep 51
    p "My."
    show ep 52
    d "Fucking."
    show ep 50
    n "God!"with vpunch 
    show ep 52
    d "Goddammit, nice job, [mc]!"with vpunch 
    mc "*Giggles* Thanks!"
    show ep 27b
    p "Oh my god, 2 Gems already, Mom!"with dis
    n "I know!"
    n "We're one step closer to becoming the CEOs of Ulysses!"
    p "Do you realize how famous we'll be? My Instagram account will blow up!"
    n "We'll never have to worry about money again!"
    mc "*Laughs* I thought our main goal now was to unravel the mystery of dead people existing in Eternum and all that."
    n "Well, yeah, but we can do both things at the same time!"
    p "I'll get invited to the most famous fashion shows in the world! Maybe they’ll even let me model!"
    n "I'll be able to send you to the best universities! And retire early! And travel! And..."
    mc "*Chuckles* Fair enough."
    show ep 28
    d "Wow, is this poster new?"with dis12
    mct "My god, did Dalia's ass get even bigger while I was in the UK? Or... rounder?"
    d "[mc]?"
    mc "E-Eh? Ah! Yeah! I bought it a couple of days ago!"
    mc "They had a few options available, but I chose this one because it had some of my favorite servers."
    d "I like it!"
    play sound chair1
    show ep 29
    d "We should go back to Ekabar soon." with dis
    d "Ulysses just announced a new event called “The Big Hunt” for next month! I can't miss it." 
    if gemevents:
        mc "Oh, I read about it on Clarence's laptop when I went to Nancy's office."
    else:
        mc "Count me in!"
    play sound2 chair1
    show ep 30
    p "Personally, I'm looking forward to visiting Meiyo."with dis
    p "I've seen a few concept art pieces and they look amazing."
    p "Plus I love feudal Japan."
    show ep 31
    d "Just be careful not to go there alone, sis."
    d "It's full of Yokais and high level enemies, it'd be dangerous for you."
    show ep 32
    p "Excuse me? What do you mean by that?"
    if penelopepath:
        p "First of all, I'm sure [mc] would be happy to play with me."
        mc "Definitely!"
        p "And secondly, my magic skills are becoming better and better everyday."
    else:
        p "I can easily defend myself with my magic skills."
    if grimoirerest:
        p "Luna taught me to summon basic fiends and I can already cast restoration spells that amaze most players."
    else:
        p "Luna taught me to summon basic fiends and I can already cast decent destruction spells of ice and fire." 
    show ep 33
    d "Yeah well, magic is pretty cool, but nothing beats a badass warrior with a big-ass sword. Or a sneaky gunslinger!"
    show ep 32
    p "The Lord of the Rings would have ended very differently if Sauron had a mage that could cast fire meteors instead of so many useless melee orcs, you know?"
    show ep 33
    d "And Harry Potter would have ended way faster if Harry rocked a Colt M1911 under his cloak."
    show ep 32
    p "Magic is better."
    show ep 33
    d "Brawn is superior."
    show ep 32
    p "No."
    show ep 33
    d "Yes."
    if daliapath and penelopepath:
        play sound chair1
        show ep 34
        d "[mc]?!" with vpunch
        show ep 35
        mc "Oh shit."
        show ep 34
        d "Settle this debate!"
        d "What's better, magic or muscle?"
        show ep 35
        mc "You mean... in Eternum? Or in video games in general?"
        show ep 34
        d "Both!"
        show ep 35
        mc "Um..."
        menu:
            with dis
            "Physicals [dalia_pts]":
                $ dalia_points += 1
                mc "I'll go with physical damage." with dis06
                mc "Nothing beats a good ol' warrior on the frontline with a sniper covering them."
                show ep 37 with dis
                play sound beat
                show screen heartbeat
                d "*Giggles* Mmm-hm." with dis08
                p "He just said it because he knows you're the one who needs the extra self-confidence, don't get so excited."
                d "*Giggles* Mmm-hm."
            "Magic [penelope_pts]":
                $ penelope_points += 1
                mc "I'll go with magic damage." with dis06
                mc "Nothing beats a good ol' spellcaster casting fire with a support healing their wounds."
                show ep 36 with dis
                play sound beat
                show screen heartbeat
                p "*Giggles* Mmm-hm." with dis08
                d "Don't get so excited, he just said it because you're the noob player and you need the extra motivation."
                p "*Giggles* Mmm-hm."
    mc "*Laughs* (I missed this so much.)"
    show ep 38
    n "So tell us [mc], how did Operation Wagner go?"with dis
    show ep 39
    mc "Exactly as you planned!"
    mc "I used my powers and stole the Gem before he could even flinch."
    mc "Then Calypso created a portal and I got out of there without a trace."
    show ep 38
    n "Wonderful!"
    n "I was a bit worried, but I'm glad to hear that everything went well."
    n "Wagner and his last men barricaded themselves inside his bunker, but I left several units posted at all the exits."
    n "There are no Exit Portals inside, so they'll have to come out eventually... especially now that Wagner lost his Gem."
    show ep 39
    mc "A good old-fashioned siege. A flawless plan."
    mc "I expected no less from the WRE Empress herself!"
    show ep 38
    n "*Chuckles* I'm just sorry we made you log into Eternum as soon as you got back."
    show ep 39
    mc "No worries! I was looking forward to it."
    show ep 30c
    mc "Honestly, I wouldn't even have left if I hadn't already paid for my flight before coming to Kredon."
    mc "I thought I'd be way more homesick."
    show ep 39
    mc "But well, at least it was nice to see my grandparents and a few friends."
    show ep 41
    a "How was your father?"with dis
    show ep 40
    mc "Meh, you know how he is. He was either working or drinking at some pub."
    mc "He barely noticed me."
    mc "*Chuckles* I received more affection from Chang's parents when I went to see them. They even gave me a bunch of food for Chang."
    show ep 41
    a "*Laughs* Yeah, Mr. and Mrs. Wong are great."
    show ep 30c
    mc "To be honest, I ended up spending most of the time in Eternum putting Dalia's techniques into practice and trying to learn how to better control my powers."
    mc "I'm glad to be back."
    show ep 39
    mc "So... well, I'm ready for our next mission, ma'am!" with dis
    show ep 38
    n "Next mission? Your next mission is to get a solid 8-hours of shut-eye!"
    show ep 39
    mc "What?!"
    show ep 38
    n "You told me you didn't sleep one bit during the flight, so now you need to rest."
    n "How long have you been awake?"
    show ep 39
    mc "Um... not more than..."
    mc "Okay, probably too long. Fair enough."
    show ep 30
    p "No worries [mc], there's nothing important to do tonight."
    p "Dalia and I were planning on watching a reality TV show and not much else."
    p "And I think Annie is playing with Nova."
    show ep 40
    mc "Oh, is that so?"
    show ep 41
    a "Yep! Nova was invited to a secret meeting by some mysterious philanthropist because of her alter ego, “Delilah Warren”."
    a "We assume he might be a fan, but we'll see."
    show ep 42
    a "*Muttering* Probably just another server where I can't use my elemental magic, but anyway..."with dis08
    show ep 41
    a "I'm sure it'll be fun."with dis08
    show ep 40
    mc "Oh damn, a secret meeting, huh? That sounds exciting!"
    mc "Very... *yawns* mmh-mysterious indeed..."
    mc "Geez, I'd like to join, but I guess you're right... I should go to sleep."
    show ep 30b
    d "I don't even know how you can hang on so long without sleeping."
    d "If I don't get a full night’s rest, I feel worn out all day."
    show ep 38
    if nancypath:
        n "That's true, the day we discovered Thanatos's identity he spent more than 48 hours without sleep, but he endured..."
        play sound clothes3
        show ep 38b
        n "Surprisingly well." with dis12
        show ep 38c
        mct "Oh my..."
        mc "T-Thank you."
        mc "Must be the excitement to play Eternum."
        show ep 38b
        n "Yeah, that must be it."
    else:
        n "That's true, the day we discovered Thanatos's identity he spent more than 48 hours without sleep, but he endured surprisingly well."
    show ep 31
    d "Any plans scheduled for this weekend? Any lost Gem to be found?"
    show ep 39b
    n "Um... let me think..." 
    n "Apart from Thanatos and us, there's one Gem in possession of another player, and my men found another 2 leads to investigate."
    show ep 39c
    n "The first one leads to the Andromeda server, so I thought of going there with Annie to see what we can dig up."with dissolve
    show ep 39d
    n "The second one leads to Blackridge, which is a town in Frontier Trails – a role-play server set in the Wild West."with dissolve
    show ep 38
    n "Alex told me she knows the server, so she offered to look around the place tomorrow."with dis 
    n "Maybe you could join her, [mc]."
    show ep 39 
    mc "That sounds great!"
    mc "And good timing too. I'm supposed to pass by her new apartment tomorrow."
    if not alexpath:
        mc "Or... at least, that's what I think. I sort of invited myself to see it."
    show ep 38
    n "Oh, she moved out of her parents' home already? That's bold."
    show ep 30b
    d "Yeah, I visited her yesterday!"
    d "She got herself a pretty cool place, you'll see."
    show ep 39
    mc "I can take the Eternum equipment with me and play from her house."
    show ep 38
    n "Sounds good."
    n "I know magic is blocked in that server, so maybe you'd like to join too, Dalia?"
    play sound chair2
    show ep 43
    d "*Standing up* I was hoping you'd say that!" with dis
    d "If that Gem is there, we'll find it!"
    play sound2 chair2
    show ep 44
    p "Wow, how come you don’t get this excited when you're playing with your beloved sister?"with dis 
    p "Is it because of Alex or [mc]?"
    show ep 45
    if daliapath:
        d "*Snorts* It's because you're not gonna be there bothering me."with dis04
    else:
        d "*Snorts* I enjoy Alex's company way more, yes."with dis04
    show ep 44
    p "Come on... you know you love playing with your big sis."with dis04
    show ep 45
    d "You're dreaming!"with dis04
    show ep 38
    n "Alright then, tomorrow is settled!"with dis
    n "Now we really should let [mc] sleep, though. We’ve bothered him enough."
    n "Everyone out!"
    show ep 39
    p "Night night, [mc]!"
    d "See ya tomorrow!"
    a "Good night!!"
    mc "Goodnight, girls!"
    show ep 46
    n "Rest well, sweetie." with dis12
    show ep 47
    mc "Thanks Nancy! Good night!"
    if nancypath:
        show ep 46
        n "I'll take a shower in the downstairs bathroom, no worries. I don’t want to keep you up."
        show ep 47
        menu:
            with dis
            "Flirt [nancy_pts]":
                mc "Well... if it’s for the right reasons, I wouldn’t mind at all..."with dissolve 
                mc "You sure you don't want some company in there?"
                $ nancy_points += 1
                play sound beat
                show screen heartbeat
                show ep 48
                n "Right now? With Penelope, Dalia, and Annie in the house?"with dis08 
                show ep 48b
                mc "Well, they can join if they want too."
                show ep 48
                n "*Snorts* Of course you’d say that! I'm afraid I'll have to shower alone today, my insatiable stud."
                show ep 48b
                mc "That's too bad... give me a call if you change your mind."
                show ep 48
                n "*Giggles* Sweet dreams, [mc]..."
                show ep 48b
                mc "See you tomorrow, Nancy..."
                stop music2 fadeout 10
                play soundloop rain3 fadein 7
                play sound ["<silence 0.3>", doorclose]
                show ep 49 with dis
                mct "Hot damn..." with dissolve
                mct "She drives me crazy. I love it."
            "Thank her":
                mc "Thank you! I appreciate it." with dissolve 
                show ep 46
                n "Sweet dreams, [mc]."
                show ep 47
                mc "See you tomorrow!"
                stop music2 fadeout 10
                play soundloop rain3 fadein 7
                play sound doorclose
                show ep 49 with dis
                mct "Man, I missed being with them so much." with dissolve
    else:
        stop music2 fadeout 10
        play soundloop rain3 fadein 7
        play sound doorclose
        show ep 49 with dis
        mct "Man, I missed being with them so much." with dissolve
    play sound chair1
    show ep 21
    mc "*Lying down* Ahhh..." with dis12
    mc "*Yawns* (If I have to be honest, I didn't realize how long I’d been awake until they mentioned it.)"
    play soundlow thunder
    mct "I feel like I have more endurance since I came to the USA, for some reason."
    mct "Must be Kredon's fresh air."
    mct "But anyway, stronger or not, I still have to sleep."
    mct "I'm supposed to meet Alex tomorrow morning and go see her new apartment. I'm sure she must be happy to finally have left the family home."
    mc "(And that Wild West server promises to be...)"
    mc "*Yawns* (Very...)"
    mct "Very, very fun...."
    stop soundloop fadeout 10
    scene black with Dissolve(3)
    play musicb twinkle fadein 40
    pause 
    mc "Mmmm..."with dis 
    mc "*Shivering* (Fuck, why is it so cold in here?)"
    mct "Did I leave my window open?"
    show ep 53c with Dissolve(3)
    mc "*Standing up* Hmm...?"with dis
    mct "What...?"
    mct "Where am I?"
    show ep 53d
    mct "What is this place?" with dis14
    mct "Am I having a lucid dream?"
    mct "Hmm, that would be a first. I hardly ever dream in the first place."
    play sound lantern
    show ep 53e with dis14
    bla "A lantern suddenly lights up at the end of the balustrade, revealing a woman sitting on top of a column." with dis
    mct "Wait, is that... Idriel?"
    play sound2 footsteps
    show ep 53f with Dissolve(1.8)
    mct "Oh god, now I'm dreaming about Eternum too. I'm way too obsessed..."with dis06
    mc "Um... hello?"
    blank ". . ."
    mc "Idriel?"
    id "Do you fear death, [mc]?"
    mc "What?"
    show ep 54
    id "Do you fear... death?"with dis15
    mc "Um... no?"
    id "Do you crave it, then?"
    mc "God, not that either."
    mc "I just... I never think about it, to be honest."
    id "Many people fear it."
    mc "Well, I guess it's natural."
    mc "But I also think that accepting it is the better approach, whenever it comes."
    mc "Everyone dies after all."
    play sound glitch4
    scene 06idrielglitch
    pause 0.5
    mc "F-Fuck!" with dissolve 
    scene ep 56
    id "Everyone dies." with dis06
    id "And yet... people fear it. Why?"
    show ep 55
    mc "Um..."with dis06
    show ep 56
    id "Do you know what's scarier than dying, [mc]?"with dis06
    show ep 55
    menu:
        with dis
        "Loneliness":
            mc "Loneliness?"with dissolve 
        "Darkness":
            mc "Darkness?"with dissolve 
        "Failure":
            mc "Failure?"with dissolve 
    show ep 56
    id "Being unable to die."with dis06
    show ep 55
    mc "Unable to die?"with dis06
    show ep 56
    id "Without death, life has no meaning."with dis06
    id "Without choice, we lose what makes us human."
    id "He feared it."
    id "That's why only you can help us."
    show ep 55
    mc "Eh... I'm afraid I'm not following you."with dis06
    show ep 56
    id "You must keep moving forward, [mc]."with dis06
    id "You must help them."
    id "Only you can."
    show ep 55
    mc "Who's “them”?"with dis06
    show ep 56
    id "We're still on the right path."with dis06
    id "We still have time."
    id "We still have a chance."
    id "But you must keep moving forward."
    show ep 55
    mc "What path?!"with dis06
    mc "You're not making any fucking sense, speak clearly!"
    show ep 56
    id "That would be pointless. You won't remember anyway."with dis06
    show ep 55
    mc "Of course I will!"with dis06
    show ep 56
    id "Keep moving forward, [mc]."with dis06
    id "Don't look back."
    id "Break.{w=0.3} The.{w=0.3} Chain."
    play sound3 risingshort3
    show ep 55 with dis17
    pause .3
    stop musicb
    play sound2 thunder
    play soundloop night fadein 1
    scene ep 57 with flashfaster
    pause 0.9
    mct "What the fuck..." with dis12
    mct "Agghh... my head..."
    mct "Fuck, that was an incredibly vivid dream."
    mct "Hmph, now where..."
    mct "Wait a second, is that an Exit Portal?"
    mct "Oh shit, don't tell me I fell asleep with the E-suit on..."
    mct "I must have logged into Eternum while sleeping."
    a "Look, the girl went inside."
    no "Oh my god, I know her! She's Harley Jones!"
    stop soundloop fadeout 10
    play music2 crime1 fadein 4
    show ep 58
    mc "*Turning around* Huh...?" with dis17
    a "Harley Jones?"
    show ep 59 with dis14
    no "You don't know her? She's like, the most famous hitwoman in Eternum!"with dissolve
    a "Oh no..."
    no "No worries, she just kills under contract. I heard she's cool when she's not on the job."
    a "Oh, good."
    no "Should we go inside?"
    mc "Um... Annie? Nova?"
    $ unlock_look("annie", 10)
    $ unlock_look("nova", 11)
    play sound leaves
    show ep 60
    a "AAAAARGH!" with hpunch
    show ep 61
    a "[mc]...? What are you doing here?!"with dis
    show ep 62
    mc "*Laughs* Okay, this is a bit embarrassing."with dis06 
    mc "I think I fell asleep with the Eternum suit and E-visor on, and the system logged me in by mistake."
    mc "*Chuckles* I know sometimes I talk in my sleep, so I wouldn't be surprised if I even managed to respond to the AI voice."
    no ". . ." (multiple=2)
    a ". . ." (multiple=2)
    mc "Are you okay...?"
    a "Why are you..."
    a "I mean..."
    show ep 63
    a "You're..." with dis12
    a "You're kind of naked."
    mc "*Gazing down at yourself* Huh?"
    play sound leaves 
    show ep 64
    mc "W-What the fuck?!" with hpunch 
    mc "W-Why am I naked?"
    play sound2 leaves2
    show ep 57
    mc "*Turning around* Oh shit, is it because this server doesn't have a default outfit?"with dis 
    no "Y-You probably skipped the Main Nexus and forgot to select an outfit from your inventory."
    a "D-Do you have anything you can wear?"
    play sound clothes3
    mc "Yeah, I think I have something here."
    mc "Sorry about that."
    if novapath and anniepath:
        show ep 65
        a "I-It's okay."
        a "It's just... that... well, I was shocked at first since we had {i}never{/i} seen each other naked, and all that."
        a "B-But, don't worry."
        show ep 66
        no "Y-Yeah, same here."
        no "A bit striking because I {i}never{/i} saw you naked before either."
        no "I mean... n-not that I was expecting to ever see you naked... erm... y-you know what I mean."
        show ep 65
        a "Y-Yeah! Same."
        show ep 67
    else:
        if novapath:
            a "I-It's okay!"
        elif anniepath:
            no "I-It's okay!"
    mc "Alright, ready!"
    play sound leaves2
    show ep 68
    mc "This will do, I guess. I don't have anything more formal right now." with dis12
    a "You look good!"
    if novapath:
        no "So good!"
    show ep 69
    mc "Well, I can't compare to you two."with dis
    mc "You look incredible, those outfits are just as elegant as they are sexy."
    no "*Giggles* Thank you!"
    show ep 70
    no "I've gotta ask, though, how could you access this server? Did I also send you an invite by mistake?"with dis
    show ep 71
    mc "Maybe? I honestly don't remember, I just went to sleep and then... I “woke up” here."
    show ep 72
    a "Oh, that happened to me once."
    a "I fell asleep with the E-suit on and I woke up at the main Nexus. Idriel was just there staring at me, asking me which server I wanted to visit."
    show ep 73
    mc "*Laughs* I'm glad I'm not alone."
    mc "I guess I should probably leave, though. I don't wanna be a hindrance."
    show ep 70
    no "No, no, please, stay!"
    no "I'm actually glad you're here. I feel safer."
    show ep 71
    mc "Really?"
    mc "Well, alright then!"
    mc "Although... I'm not sure what we're supposed to do here."
    mc "Annie mentioned it, but didn't go into details."
    show ep 70
    no "Basically, I received a private message addressed to Delilah Warren, inviting me to the house of Gideon Cook tonight."
    show ep 72
    a "I didn't know him, but apparently Gideon Cook is a famous Eternum collector."
    a "They said he brought together artifacts from more than 100 different servers. His collection is worth millions of eternals!"
    a "People usually just call him “The Collector”."
    show ep 73
    mc "I see... And what does he want from Ms. Warren?"
    mc "Maybe he wants Dione for his collection?"
    show ep 70
    no "Hah! I'd like to see him try!"
    no "I saw more people entering the house, so it seems I wasn't the only person invited."
    show ep 71
    mc "Uh, sounds thrilling!"
    show ep 73
    mc "What are we waiting for, then?"
    mc "Let's go inside!"
    show ep 74
    no "Well, we were trying to do some recon before going in, just in case it happened to be a trap of some sort."with dis
    mc "That's smart."
    show ep 75
    no "But now that you're here, we have nothing to fear!" with dis08
    no "You go first! Dione and I will be covering your back!"
    mc "*Chuckles* Alright, fair enough."
    mc "Let's see what this is all about."
    no "We’ll follow you!"
    show ep 76 with dis15
    mc "Hmm..."with dis06
    mc "Fancy place."
    no "We're in the Rockefeller server, so I'd be more surprised if a house here {i}didn't{/i} look fancy."
    mc "Oh, the same server where I met the Founder?"
    a "Yep! All rich people have a mansion or two here."
    mc "We'll have one someday too."
    a "*Laughs* I'll take your word for it!"
    play sound metalgate
    show ep 77 with dis2
    a "Look, there's a stroller with some luggage over there."with dis 
    a "Maybe this is some sort of hotel?"
    mc "Mmm, it could also be a vacation home. It gives me those vibes."
    show ep 78
    mc "I hear voices coming from the inside." with dis 
    mc "They must be waiting for us."
    no "Okay! Let me go first."
    no "I'm the one who was invited, so I guess I should be the one introducing you both."
    mc "Fair enough."
    no "*Taking a deep breath* Okay, Delilah. Act cool, confident... *cracks knuckles* badass."
    show ep 79 with dis2
    bla "As you enter the building, the few people who were speaking suddenly go silent, and everyone in the hall stares at you."with dis
    mct "Damn, these people look so... different from each other. Is “The Collector” one of them?"
    show ep 80 
    aaa "Well, well, well... I guess we're all here now." with dis12
    aaa "I'm glad to see people my age. These boomers are a total bore."
    show ep 81
    mc "Hello! I'm [mc], nice to meet you."with dissolve
    show ep 80
    har "Pleased to meet you, [mc]. I'm Harley." with dissolve 
    show ep 82
    aaa "So, you're the last ones?"with dis08
    aaa "Can we finally learn why we were all gathered here?"
    aaa "I have things to do. I can't stay here all night, you know."
    show ep 83
    no "I don't know why we're here either, I guess we all received the same–"
    stop music2
    play sound lightstage
    play sound2 lightstage
    scene black
    pause .7
    a "W-What happened?"with dis
    aaa "Looks like the lights went out."
    aaa "Fantastic deduction there, Sherlock."
    mc "Stay behind me..."
    aaa "Fuck, I knew I shouldn't have come."
    play sound lightstage
    play sound2 lightstage
    scene ep 84
    pause 
    aaa "What the hell..." with dis06
    play music2 crime2
    show ep 85
    cl "Hello everyone!" with dis12
    cl "My name is Clonk, and I am very pleased to meet you all. Welcome to the Cook guesthouse!"
    har "Is this robot talking?"
    show ep 86
    cl "Indeed, I am! Very perceptive of you, Ms. Jones."with dis
    cl "I am one of Mr. Cook's artifacts. I've been a proud part of his collection for 4 years now, after he bought me at an auction in the Red Herring server."
    show ep 87
    cl "This house holds the best pieces of Mr. Cook's collection." with dis
    cl "Most artifacts look like normal items, but be careful! Don't touch anything if you don't want any unpleasant surprises!"
    show ep 91
    aaa "So... Gideon Cook sent us all invitations to his storehouse? Why?"
    show ep 92
    mct "Good lord almighty! Now that’s what I call cleavage!"
    mct "I should pick up my jaw and look away before Nova or Annie notice me staring, though..."
    a "*Whispering* Wow, have you seen the milk melons on her?!"
    no "*Whispering* I know! I was thinking the same thing! She’s never going to have to worry about drowning, that’s for sure."
    mct "Nevermind."
    show ep 91
    aaa "Is he gonna show up or...?"
    show ep 87
    cl "He indeed invited you all, Ms. Piaget."
    cl "Unfortunately, I will be your host tonight, on behalf of Mr. Cook."
    aaa "And why didn't he come himself?"
    show ep 86
    cl "Good question. One that has a very simple explanation."with dis 
    cl "You see, Master Gideon, The Collector, can't be here tonight because..."
    play sound impact5
    stop music2
    show ep 88
    cl "He was murdered last week."
    play sound2 impact5
    show collage1
    pause 0.3
    play sound3 impact5
    show collage2
    pause 0.3
    play sound4 impact5
    show collage3
    pause 0.3
    play sound5 impact5
    show collage4
    pause 0.3
    play sound6 impact5
    show collage5
    pause 0.3
    play sound7 impact5
    show collage6
    pause 0.3
    play sound impact5
    show collage7
    pause 0.3
    play sound2 impact5
    show collage8
    pause
    play music2 crime2
    scene ep 91
    aaa "Gideon Cook is... dead?"with dis12
    show ep 87
    cl "Correct!"
    cl "In fact, you've been gathered here to decide who will inherit one of Mr. Gideon's possessions." 
    cl "An item of your choice!"
    show ep 109
    aaa "What do you mean, “decide”? We have to choose who gets to take one artifact?"
    show ep 87
    cl "Indeed!"
    cl "Each one of you made a name for yourself in Eternum in one way or another."
    cl "Master Gideon thought you all deserved to be the heir to one of his artifacts because of that."
    cl "But... there's a catch."
    cl "Someone amongst your ranks... is an impostor. One of you..."
    play sound impact5
    stop music2
    show ep 88
    cl "Is the person who murdered Gideon Cook."
    play sound2 impact5
    show collage1
    pause 0.3
    play sound3 impact5
    show collage2
    pause 0.3
    play sound4 impact5
    show collage3
    pause 0.3
    play sound5 impact5
    show collage4
    pause 0.3
    play sound6 impact5
    show collage5
    pause 0.3
    play sound7 impact5
    show collage6
    pause 0.3
    play sound impact5
    show collage7
    pause 0.3
    play sound2 impact5
    show collage8
    pause
    play music2 crime2
    scene ep 86
    cl "Using his wits, and before the hemlock ended his life, Master Gideon quickly discovered who the murderer was." with dis12
    cl "Far from any feeling of rancor, he admired the ambition and tenacity of his killer."
    show ep 87
    cl "So then, he decided to design one last puzzle game before his Eternum account and inventory were lost to the endless depths of cyberspace forever."with dis 
    cl "Every 10 minutes, each one of you has to vote for the person who you think is the murderer."
    cl "At the end of each round, the person with the most votes will be eliminated."
    show ep 86
    cl "If you successfully eliminate the murderer, you win, and all the remaining players will be able to choose an artifact of their choice."with dis 
    cl "If you don't eliminate the murderer, the game will continue onto the next round."
    show ep 87
    cl "If there are only two people left, and one of them is the murderer, the murderer wins the game and they can take an artifact with them."with dis 
    show ep 93
    aaa "A game of intellect. Sounds fairly appealing."
    show ep 87
    cl "To kick things off, I do believe introductions are in order. Please take this time to become acquainted with one another."
    cl "Afterwards, the game will begin."
    cl "Good luck and have fun!"
    show ep 89
    har "Okay, okay, I'll start!"
    har "Hi everyone, my name is Harley Jones, and I didn't even know who Gideon Cook was before coming here, so... I'm obviously not the murderer."
    show ep 86
    cl "Please, Ms. Jones, refrain from discussing the murder victim until after the presentations have been completed."
    show ep 89
    har "Oh, sorry Clonky, of course."
    har "Where was I..."
    har "Ah yes, I'm Harley Jones."
    play sound impact5
    show crim1
    pause
    play sound2 w1
    scene crim1b
    har "And I guess I don't need to say much... my reputation speaks for itself."
    har "I'm the best hitwoman in all of Eternum."
    har "The only way to defeat me is catching me off guard while I'm sleeping, and since I’m the queen of #TeamNoSleep in Eternum... GG!"
    scene ep 95
    aaa "Hitwoman? Sounds like the perfect suspect to be the murderer."
    show ep 89
    har "I'd never use such a lame method as poison, but thanks for your concern, dear holy Pope."
    show ep 91
    aaa "Very well, I'll introduce myself next, then."with dis
    aaa "I am Anna Piaget."
    play sound impact5
    show crim2
    pause
    play sound2 w1
    scene crim2b
    pia "I'm one of the most renowned psychologists in the world."
    pia "I have dozens of published works and I'm capable of diagnosing any kind of mental illness or insecurity within a person after talking to them for a minute."
    pia "And of course... to provide them with the {i}proper{/i} treatment."
    scene ep 93
    aaa "I am Gemini, or as some people call me... the Blind Oracle."with dis
    play sound impact5
    show crim3
    pause
    play sound2 w1
    scene crim3b
    gem "After losing my sight and legs as a kid, I developed a new ability."
    gem "I am capable of seeing the future."
    if lunapath:
        scene ep 94
        mct "The future? Like Luna?"
        mc "Um..."
        mc "If I may ask... how can you do that? Do you do that through your sense of touch, or...?"
        show ep 93
        gem "My visions come and go. I can't know when they will come, or what they'll be about."
        show ep 94
        mct "Hmm, seems different from hers."
        show ep 93
    gem "Unfortunately, Eternum can't heal my physical state, but my mental abilities remain intact."
    scene ep 95
    aaa "I'm Sister Baek." with dis
    play sound impact5
    show crim4
    pause
    play sound2 w1
    scene crim4b
    bae "I am the leader of the Church of Unitology in the server of Andromeda."
    bae "I can feel the presence of the people who have already left our mortal plane and sometimes... I can hear their messages."
    scene ep 91
    pia "So... a cult?"
    show ep 95
    bae "A RELIGION."
    bae "We unitologists adamantly believe that Eternum was created by the intelligent design of a divine alien agency, and all humanity will be reunified after death in a sacred server."
    show ep 96
    har "*Coughs* Coo-coo!"
    mct "Mmm... considering what we discovered at Thanatos' house... that somehow doesn't seem so far-fetched."
    show ep 97
    no "*Profusely clears her throat* AHEM! I guess it's my turn now." with dis
    no "My name is..."
    show ep 99 
    har "Wait, wait, wait, what about these two?"
    show ep 100
    har "Why are you hiding in that corner?"
    show ep 101
    mc "Um... well, I didn't think we had to introduce ourselves." with dis08
    mc "I'm [mc], but..."
    mc "Technically we weren't invited by Gideon Cook, we just came with No–"
    play soundlow punch volume 0.5
    show ep 101b
    a "*Clears throat* Hmmph!" with hpunch 
    show ep 101
    mc "...NO one else except for Delilah."with dis
    show ep 99
    har "What?!" 
    har "That's cheating!"
    show ep 102
    no "How is that cheating?"
    no "The invitation didn't mention I couldn't bring anyone with me!"
    show ep 99
    har "Yes it did!"
    show ep 102
    no "No, it didn't, you dumbo!"
    play sound paper2
    show ep 103 with Dissolve(1.1)
    no "Actually, I still have the invitation here with me, so you can see for yourself and then shut up about it." with dissolve
    no "*Reading out loud* {i}Dear Delilah Warren, my name is Gideon Cook, and I am pleased to offer you a once-in-a-lifetime opportunity. You must come alone to the–"
    no ". . ."
    no "Oh."
    show ep 104
    no "*Nervous giggle* Okay, I might have missed that bit."with dissolve
    show ep 99
    har "Cheater!" with hpunch
    show ep 86
    cl "Fear not, Ms. Jones."
    cl "Even if Ms. Warren infringed that rule, her companions can't vote in the game, so your chances of winning are not lessened by any means."
    show ep 102
    no "See? No need to make a fuss about it, drama queen."
    show ep 99
    har "I'll let it slide for now, but I'm keeping an eye on you, ginger girl."
    har "You're sussy!"
    show ep 102
    no "Okay, okay, whatever..."
    show ep 97
    no "Anyway... as I was saying, my name is Delilah Warren." with dis
    play sound impact5
    show crim5
    pause
    play sound2 w1
    scene crim5b
    no "You'll recognize my name because, as it's publicly known, I'm in possession of one of the three Weapons of Atlas, Dione."
    no "My marksmanship is perfect, and I've never missed a shot in my life."
    scene ep 98
    no ". . ."
    play soundlow pop
    scene ep 105
    a "Great introduction, Delilah!" with dis04 
    a "So badass!"
    show ep 106
    no "*Giggles* Y-You really think so?! Thanks, Annie!"with dissolve 
    show ep 107
    aaa "*Clears throat* And I am... Elliot Cook." with dis
    play sound impact5
    show crim6
    pause
    play sound2 w1
    scene crim6b
    eli "I... eh... I'm a taxi driver in New York."
    show ep 91
    pia "You're sweating like a racehorse, Elliot."
    pia "I assume it's just a psychosomatic effect of the anxiety you're going through right now. Hiding anything?"
    show ep 109
    bae "And... did you say you're a taxi driver? That's all?"
    bae "Everyone here stands out for something. Why would The Collector have invited you otherwise?"
    show ep 93
    gem "I'm sorry, but it seems like no one is pointing out the obvious thing here. Did you say you're Elliot... {i}Cook{/i}?"
    gem "Are you related in any way to Mr. Gideon Cook?"
    show ep 107
    eli "Erm..."
    eli "He..."
    eli "Yes, he was my father."
    show ep 109
    bae "What?!"
    bae "The Collector was your father?"
    play sound slam3 volume 0.6
    show ep 112
    har "*Laughs* HAHAHA!" with vpunch
    har "So in sum, this dude killed his own pops and showed up at the reading of his will expecting to cash out... just to find a bunch of strangers and a game his daddy organized before dying simply to humiliate him!"
    har "*Laughs* Now I've seen everything!"
    show ep 110
    eli "Whoa, whoa, whoa, stop there kiddo, I haven't killed anyone!"
    eli "My father and I stopped talking years ago!"
    eli "He was so fucking obsessed with Eternum and his artifacts that he ended up abandoning my mother and forgetting he had a son."
    eli "I was just as surprised to receive that letter as all of you."
    show ep 109
    bae "So you killed him out of spite?"
    show ep 91
    pia "He probably expected to be his father's only heir, so he killed him after discovering how much his Eternum collection was worth."
    show ep 93
    gem "Greed is definitely one of the most hideous sins in this world, no doubt."
    show ep 112
    har "*Laughs* You've gotta be the worst killer ever!"
    show ep 110
    eli "I said I didn't kill anyone!"
    eli "I..."
    show ep 111
    eli "You know what? Fuck you!" with dis08
    eli "I don't give a shit about you bunch of retards. I'm going out for a smoke."
    eli "You can all open up your gigantic mouths and gobble on my big hairy balls. There’s room for all of you shitheads!"
    show ep 91
    pia "I was honestly expecting this to be a bit more challenging."
    show ep 87
    pia "Can we vote already, robot?"
    cl "You have 10 minutes to decide your vote, ma'am. Just get back to me when you've decided!"
    show ep 89
    har "Well, since the game is pretty much over, I'm gonna go take a walk around the house to decide what artifact I want to take home."
    har "See you in 10 minutes!"
    show ep 114 with dis14
    mc "Well..."with dissolve 
    mc "Seems like all clues point to Elliot Cook, The Collector's son."
    show ep 113
    no "Yes, but... I don't know, it all seems way too easy. I feel like the actual killer wouldn’t be sweating like a pig and giving himself away so easily, don’t you think?"
    no "If you ask me, I'd say there's something fishy here."
    show ep 115
    a "Yeah, I think so too... my Sherlock Holmes-ian senses are tingling."
    a "I don't trust any of these people. I feel like someone is lying..."
    show ep 114
    mc "Those were exactly my thoughts."
    mc "I think one of them is hiding things from us and is running some sort of con."
    mc "Let's take a walk around the house before voting."
    mc "Maybe if we find some clue or catch anyone in their lie we can unravel this mystery."
    show ep 116
    no "Exciting! You can count on us!" with dis08
    a "Don't worry [mc], you and your two deputies will unravel the mystery of Cook's manor!"
    mc "*Chuckles* I couldn't have asked for better assistants."
    mc "Let's do this!"
    stop music2 fadeout 4
    scene ec 0 
    hide screen heart
    with dis22 
    play music2b crime3 fadein 5
    mod "Check out stuff and talk to people :) Quickest way is in the Help menu, but there are more options. You should get an Artifact at the end if all is done correctly."
    menu:
        with dissolve
        mod "Would you like to see correct votes?"
        "Yes":
            $ mod_freeroam2_help = True
        "No":
            pass
    show screen freeroam_help2
    call screen crimemap0 with dis2
label crime0:
    scene ec 0 with dis15
    if not crimedoor1 and crimekeyfirst and not eround == 1:
            a "Hey, check out the reception... there's a bunch of little drawers and different keys over there."with dissolve 
            a "Maybe the one that opens that locked door we found is among them?"
            mc "Hmm, it's worth checking it out..."
            $ crimekeyfirst = False
            $ crimekey2 = True
    call screen crimemap0 with dis04
label crime0clonk:
    show screen heart
    scene ec 7 
    with dis
    if crimecl1:
        $ crimecl1 = False
        cl "Welcome back, Ms. Warren!"with dis08
        cl "Are you ready to cast a vote?"
        scene ec 13 
        no "Actually, I'm gonna delegate [mc] as my voter. We're a team, so... I'll let him make the final decision."
        no "Is that okay?"
        scene ep 86
        cl "Of course, that is no problem at all."
        cl "Just keep in mind that the other guests might still vote for you to be eliminated, not Mr. [mc]."
        scene ec 13
        no "Sure, that makes sense."
        scene ep 86
        cl "Thank you for your understanding."
        scene ec 7
        mc "Can I ask what your relationship with The Collector was exactly, Clonk?"with dis
        mc "Were you like... his butler or something?"
        cl "Oh, I held a much lesser role. I just used to watch the guesthouse and helped him keep the inventory of his artifacts in order."
        show ec 8
        cl "Unfortunately, the low mobility of my arms prevents me from carrying out simple tasks such as cleaning or serving tea, so I'm not fit to be a butler."with dis08
        show ec 14
        a "Aaaaaw, look how cute he is when he's sad!"
        a "Don't worry Clonk, I'm sure he was proud of you!"
        show ec 8
        menu:
            with dis
            "Be nice to Clonk [annie_pts]":
                $ clonknice = True
                mc "Yeah, Annie's right, you seem like a great servant, Clonk."with dissolve
                mc "You should be proud of yourself."
                $ annie_points += 1
                play sound beat
                show screen heartbeat
                a "Well said!" 
                mct "Trying to cheer up a depressed robot is certainly not one of the things I thought I'd be doing in Eternum a few months ago."
                scene ec 7
                cl "You're too nice, Mr. [mc]!"with dis
                mc "*Chuckles* Don't mention it."
                mc "And you can call me Mr. [lastname], if you want."
                cl "With pleasure!"
                cl "Alright then, tell me Mr. [lastname], are you ready to cast your vote and advance to the next round?"
            "Be rude to Clonk":
                mc "Sounds like a skill issue."with dissolve
                mc "Now that The Collector is dead I guess you'll be scrapped for parts or something? Maybe melted down to create something more useful?"
                mc "You’d probably make a badass coffee mug."
                a "[mc], don't be rude to Clonk!"
                cl "Probably yes..."
                show ec 7
                cl "But that won't stop me from conducting my final task!" with dis 
                cl "I'll fulfill my master's last wishes and complete his last game!"
                cl "So... tell me sir, are you ready to vote and advance to the next round?"
                mc "You can call me Mr. [lastname], and..."
        jump crime0clonk2
    if eround == 1:
        cl "Hello again sir! Are you ready for the first vote?" with dissolve 
    if eround >= 2:
        cl "Hello again sir! Ready to vote?" with dissolve 
        jump crime0clonk2
label crime0clonk2:
    menu:
        with dis
        "Vote":
            if eround == 4:
                mc "Um... I guess."with dissolve 
                if crimegirlsartifacts and (not crimeannietrust or erevealies <= 1):
                    scene ec 155b
                    a "[mc]!"with dis
                    $ annieturnedback = True
                    scene ec 155c
                    mc "Annie! Thank god you're not invisible anymore."
                    mc "Please, tell me you found a clue about who's the murderer."
                    scene ec 155b
                    a "Uh... I-I didn't, I'm sorry."
                    scene ec 7
                    mc "Oh god, we're fucked..."with dis
                else:
                    mct "Fuck, I'm sweating so much that the others will think we're the impostors..." 
                mct "If I don't get this right, the murderer will win the game and we'll get lasered."
                mct "This is my last chance..."
                cl "{sc=2}Who {w=0.4}killed {w=0.4}Gideon {w=0.4}Cook?{/sc}"
                jump crimeclonkresultsround2
            mc "Yes I am."with dissolve
            cl "Excellent!"
            cl "Tell me then, who killed Mr. Gideon Cook?"
            if eround == 2 or eround == 3:
                jump crimeclonkresultsround2
            if mod_freeroam2_help:
                mod "Vote for any here."
            menu:
                with dis
                "Harley Jones, the hitwoman":
                    mc "Harley Jones." with dissolve 
                "Anna Piaget, the psychologist":
                    mc "Anna Piaget." with dissolve 
                    $ evotation += 1
                "Gemini, the psychic":
                    mc "Gemini." with dissolve 
                    $ evotation += 2
                "Sister Baek, the medium":
                    mc "Sister Baek." with dissolve
                    $ evotation += 3
                "Elliot Cook, the Collector's son":
                    mc "Elliot Cook." with dissolve 
                    $ evotation += 4
                "Delilah Warren":
                    mc "Delilah Warren." with dissolve 
                    $ evotation += 5
                    show ec 41
                    no "Um... excuse me?"
                    $ delilahvote = True
                    no "You did {i}not{/i} just vote for me. What the hell, [mc]?!"
                    show ec 42
                    mc "Don't worry, it's all part of the strategy!"
                    mc "I'm pretty sure no one else will vote for you, and I want to know who voted for who."
                    show ec 41
                    no "Hmph, you better know what you're doing..."
                    show ec 7
            cl "Thank you for your vote, sir."
            cl "With this, the first round has reached its end."
            jump crimeclonkresults
        "Not yet":
            mc "Not yet." with dissolve 
            cl "Very well, just let me know whenever you're ready!"
            scene ec 0 
            hide screen heart
            with dis15
            call screen crimemap0 with dis04 
label crimeclonkresultsround2:
    $ evotation = 1
    if eround == 3 and not geminialive and not baekalive:
        $ eround += 1
    if eround == 2 and mod_freeroam2_help:
        mod "Vote for Gemini."
    elif eround == 3 and mod_freeroam2_help:
        mod "Vote for any of the first three."
    elif eround == 4 and mod_freeroam2_help:
        mod "Vote for any of the first two."
    menu:
        with dis
        "Harley Jones, the hitwoman" if harleyalive:
            mc "Harley Jones." with dissolve 
        "Anna Piaget, the psychologist" if annaalive:
            mc "Anna Piaget." with dissolve 
            $ evotation += 1
        "Gemini, the psychic" if geminialive:
            mc "Gemini." with dissolve 
            $ evotation += 2
        "Sister Baek, the medium" if baekalive:
            mc "Sister Baek." with dissolve
            $ evotation += 3
        "Delilah Warren":
            mc "Delilah Warren." with dissolve 
            $ evotation += 4
            if crimegirlsartifacts and eround == 2 or eround == 3:
                mct "At least Nova isn’t here, so she can't get mad at me."
            else:               
                if eround == 4:
                    show ec 144
                    no "What?!"
                    no "What the fuck, [mc], this is the last round!"with hpunch
                    mc "Trust me, it's all part of my plan..."
                elif delilahvote:
                    show ec 41
                    no "What?! AGAIN?"
                    show ec 42
                    mc "Trust me, the plan..."
                else:
                    show ec 41
                    no "Um... excuse me?"
                    no "You did {i}not{/i} just vote for me. What the hell, [mc]?!"
                    show ec 42
                    mc "Don't worry, it's all part of the strategy!"
                    mc "I'm pretty sure no one else will vote for you, and I want to know who voted for who."
                    show ec 41
                    no "Hmph, you better know what you're doing..."
            show ec 7
    cl "Thank you for your vote, sir."
    if eround == 2:
        cl "With this, the second round has reached its end."
    elif eround == 3:
        cl "With this, the third round has reached its end."
    elif eround == 4:
        cl "With this, the final round has reached its end."
    jump crimeclonkresults
label crimeclonkresults:
    scene ec 43
    cl "May I have your attention! Everyone please return to the main hall!" with dis12
    if eround == 4:
        cl "The final round is over!"
        bla "The remaining players come back to the hall and nervously tell their vote to Clonk."
    else:
        cl "Round [eround] is over!"
        bla "Everybody comes back to the hall and discreetly tells their vote to Clonk, one after the other."
    if (eround == 3 and crimegirlsartifacts) or (tieround2 and crimegirlsartifacts and eround == 4):
        scene ec 134
        no "Oh dear, I'm so dizzy..." with dis12
        show ec 135
        mc "Nova! You're back to normal!"
        mc "Are you okay?"
        show ec 134
        no "Yeah, more or less. I suddenly reverted back into a single body after a while. Now I'm just a little woozy."
        no "I won't touch anything else, I swear."
        show ec 135
        mc "Don't worry, I'm glad to see full Nova back."
        mc "The important thing right now is that we get out of here alive."
        mc "Have you seen Annie?"
        show ec 134
        no "I think so? Or at least I heard her voice."
        if not tieround2:
            no "She told me she was heading somewhere to find something."
            show ec 135
            mc "So she's still invisible."
        else:
            no "She told me she was heading to the garden to find a box or something and she'd join us ASAP."
            show ec 135
            mc "Ah, I'm relieved."
        mc "Well, let's hear the result of the vote, hopefully this one was the last round!"
        show ec 136
        no "Yes! Let's hope so!"
    scene ep 86
    cl "Thank you all for your cooperation!"with dis
    cl "The final results of the vote are as follows!"
    if eround == 4:
        play sound swallow
        mc "*Gulps* (The moment of truth.)"
        if evotation == 1:
            if annaalive:
                cl "Anna Piaget... 1 vote."
            elif baekalive:
                cl "Sister Baek... 1 vote."
            elif geminialive:
                cl "Gemini... 1 vote."
            cl "Harley Jones... 2 votes."  
            jump harleykilling        
        elif evotation == 2:
            if harleyalive:
                cl "Harley Jones... 1 vote."
            elif baekalive:
                cl "Sister Baek... 1 vote."
            elif geminialive:
                cl "Gemini... 1 vote."
            cl "Anna Piaget... 2 votes." 
            jump annakilling         
        elif evotation == 3:
            if annaalive:
                cl "Anna Piaget... 1 vote."
            elif baekalive:
                cl "Sister Baek... 1 vote."
            elif harleyalive:
                cl "Harley Jones... 1 vote."
            cl "Gemini... 2 votes." 
            jump geminikilling          
        elif evotation == 4:
            if annaalive:
                cl "Anna Piaget... 1 vote."
            elif geminialive:
                cl "Gemini... 1 vote."
            elif harleyalive:
                cl "Harley Jones... 1 vote."
            cl "Sister Baek... 2 votes." 
            jump baekkilling           
        else:
            if harleyalive:
                cl "Harley Jones... 1 vote."
            if annaalive:
                cl "Anna Piaget... 1 vote."
            if baekalive:
                cl "Sister Baek... 1 vote."
            if geminialive:
                cl "Gemini... 1 vote."
            cl "Delilah Warren... 1 vote."
            jump allkilling
    if eround == 3:
        if evotation == 1:
            cl "Anna Piaget... 1 vote."
            if baekalive:
                cl "Sister Baek... 1 vote."
            elif geminialive:
                cl "Gemini... 1 vote."
            cl "Harley Jones... 2 votes."  
            jump harleykilling        
        elif evotation == 2:
            cl "Harley Jones... 1 vote."
            if baekalive:
                cl "Sister Baek... 1 vote."
            elif geminialive:
                cl "Gemini... 1 vote."
            cl "Anna Piaget... 2 votes." 
            jump annakilling         
        elif evotation == 3:
            cl "Harley Jones... 1 vote."
            cl "Anna Piaget... 1 vote."
            cl "Gemini... 2 votes." 
            jump geminikilling          
        elif evotation == 4:
            cl "Harley Jones... 1 vote."
            cl "Anna Piaget... 1 vote."
            cl "Sister Baek... 2 votes." 
            jump baekkilling           
        else:
            cl "Harley Jones... 1 vote."
            cl "Anna Piaget... 1 vote."
            if baekalive:
                cl "Sister Baek... 1 vote."
            elif geminialive:
                cl "Gemini... 1 vote."
            cl "Delilah Warren... 1 vote."
            jump allkilling
    if eround == 2:
        if evotation == 1:
            cl "Harley Jones... 1 vote."
            cl "Sister Baek... 2 votes."
            cl "Gemini... 2 votes."
        elif evotation == 2:
            cl "Anna Piaget... 1 vote."
            cl "Sister Baek... 2 votes."
            cl "Gemini... 2 votes."
        elif evotation == 3:
            cl "Sister Baek... 2 votes."
            cl "Gemini... 3 votes."
            cl "Which means that..."
            $ geminialive = False
            cl "Gemini has been eliminated from the game!"
            play sound wheelchair
            scene ec 90
            gem "Hold on a second, WHAT?!" with hpunch 
            gem "You voted for... ME?!"
            gem "Are you all retarded?!"
            play soundlow wheelchair
            show ec 91
            gem "It's so fucking obvious that it's Sister Baek, for fuck's sake!" with hpunch 
            gem "How did you let her fool you?!"
            scene ep 95
            bae "We caught you, Gemini."
            bae "Accept it already."
            scene ec 95
            har "*Hysterical laugh* I bet you didn't see this coming in your visions, eh?!"
            scene ec 90
            gem "You bunch of idiots!"
            gem "How can you be so fu–"
            play sound laserbeam
            stop music2
            show ec 92
            pause .03
            show ec 93
            pause 2.2
            play sound2 ["<silence 0.1>", wheelchair] volume 1.1
            play sound4 ["<silence 0.2>", fall] volume 1.1
            scene ec 94 with dis08
            play music2 crime5
            pause 
            scene ec 95
            har "O-Okay! It's done!"with dis
            har "We won! Right?!"
            show ep 86
            cl "I'm afraid not, Ms. Jones." with dis08
            cl "I must announce that Gemini was actually {b}NOT{/b} the murderer!"
        elif evotation == 4:
            cl "Gemini... 2 votes."
            cl "Sister Baek... 3 votes."
            cl "Which means that..."
            cl "Sister Baek has been eliminated from the game!"
            scene ec86
            bae "Hold on, hold on, hold on!" with dis 
            bae "This is a joke, RIGHT?!"
            bae "I'm a respectable leader of Eternum's community!"
            bae "I had no reason to kill The Collector!"
            scene ep 93
            gem "I'm afraid the vote has already ended, Sister." 
            scene ec86
            bae "O-Okay! I lost! Haha!"
            bae "I'll leave! OKAY?! I'll leave the server."
            scene ec 97
            pia "That's not how this works, Baek."
            scene ec86
            bae "Okay! OKAY!"
            bae "I'll leave the server so you can conti–"
            play sound laserbeam
            stop music2
            scene ec 87
            pause .03
            show ec 88
            pause 2.2
            play sound2 ["<silence 0.3>", fall2] volume 1.1
            play sound4 ["<silence 0.3>", fall] volume 1.1
            scene ec 89 with dis08
            play music2 crime5
            pause 
            $ baekalive = False
            scene ec 97
            pia "So... is it done? Did we win?"with dis 
            show ep 86
            cl "I'm afraid not, Ms. Piaget." with dis08
            cl "I must announce that Sister Baek was actually {b}NOT{/b} the murderer!"
        else:
            cl "Delilah Warren... 1 vote."
            cl "Sister Baek... 2 votes."
            cl "Gemini... 2 votes."
        if evotation == 1 or evotation == 2 or evotation == 5:
            cl "So... oh! We have a tie!"
            cl "Which means that both Gemini and Sister Baek have been eliminated from the game!"
            $ tieround2 = True
            play sound wheelchair
            scene ec 90
            gem "Hold on a second, WHAT?!" with hpunch 
            gem "You voted for... ME?!"
            gem "Are you all retarded?!"
            scene ec 95
            har "*Hysterical laugh* I bet you didn't see this coming in your visions, eh?!"
            scene ec86
            bae "T-This is a joke, RIGHT?!"
            bae "I'm a respectable leader of Eternum's community!"
            bae "I had no reason to kill The Collector!"
            scene ec 97
            pia "I'm afraid the vote has already ended, Sister." 
            scene ec 90
            gem "You bunch of idiots!"
            gem "How can you be so fu–"
            play sound laserbeam
            stop music2
            show ec 92
            pause .03
            show ec 93
            pause .5
            scene ec 85
            pause .2
            play sound3 laserbeam
            stop music2
            scene ec 87
            pause .03
            show ec 88
            pause 2.2
            play sound2 ["<silence 0.3>", wheelchair] volume 1.1
            play sound4 ["<silence 0.3>", fall] volume 1.1
            scene ec 89 with dis08
            play music2 crime5
            pause 
            scene ec 95
            har "O-Okay! It's done! We won! Right?!"with dis 
            show ep 86
            cl "I'm afraid not, Ms. Jones." with dis08
            cl "I must announce that Gemini and Sister Baek were actually {b}NOT{/b} the murderers! Neither of them!"
            $ baekalive = False
            $ geminialive = False
        scene ep 87
        cl "Which means that the true killer is still hiding among you and we will proceed to Round 3!"with dis
        cl "Good luck!"
        $ eround += 1
        play soundlow slam3
        scene ec 95
        har "WHAT?!" with hpunch
        har "Please, not again!"
        scene ec95
        har "*Hyperventilating* I can't continue, my anxiety is gonna kill me before the laser does!"
        har "You're all lying to me!"
        har "YOU'RE ALL LIARS!"
        scene ec 96
        har "AND WHY ARE YOU ALONE?!" with hpunch
        har "Where's Delilah and the other girl?!"
        mc "Um..."
        scene ec95
        har "DECEIVER!"
        har "I should have never come here..."
        scene ec 97
        pia "I see none of you can be trusted."
        pia "You better stay away from me. All of you."
        scene ec 0
        with dis15
        mct "Oh god..."with dis06
        mct "What have we got ourselves into..."
        hide screen heart 
        call screen crimemap0 with dis06
    if eround == 1:
        if evotation == 1:
            cl "Harley Jones... 1 vote."
            cl "Anna Piaget... 1 vote."
            cl "Elliot Cook... 4 votes."
        elif evotation == 2:
            cl "Anna Piaget... 2 votes."
            cl "Elliot Cook... 4 votes."
        elif evotation == 3:
            cl "Anna Piaget... 1 vote."
            cl "Gemini... 1 vote."
            cl "Elliot Cook... 4 votes."
        elif evotation == 4:
            cl "Anna Piaget... 1 vote."
            cl "Sister Baek... 1 vote."
            cl "Elliot Cook... 4 votes."
        elif evotation == 5:
            cl "Anna Piaget... 1 vote."
            cl "Elliot Cook... 5 votes."
        else:
            cl "Anna Piaget... 1 vote."
            cl "Delilah Warren... 1 vote."
            cl "Elliot Cook... 4 votes."
        cl "That is all."
        show ep 91
        pia "Well, I guess there were no surprises."
        show ep 112
        har "*Laughs* HAHA! Good try, Elliot."
        show ep 111
        eli "Fuck you all! I'm glad this shit is finally over."
        scene ec 44
        eli "Okay robot, these morons voted for me." with dis
        eli "Can you tell them that I'm not the fucking murderer already? I wanna see their stupid faces."
        scene ep 86
        cl "One step at a time, Mr. Cook!"
        cl "First of all, you must be retired from the game, since you were just eliminated!"
        scene ec 44
        eli "*Sighs* Fine, can I leave already, then?"
        eli "Or do I have to sta–"
        play sound laserbeam
        stop music2b
        show ec 45
        pause .04
        show ec 46
        pause .7
        scene ec46
        pause 2.2
        play sound2 ["<silence 0.3>", fall2] volume 1.1
        play sound4 ["<silence 0.3>", fall] volume 1.1
        scene ec 47 with dis08
        play music2 crime4
        pause 
        mc "W-What the fuck..."with dis08
        show ec 48
        har "W-W-W-Wha-aat...?"with dis
        har "D-Did he just get f-fucking laser beamed from the c-ceiling?"
        scene ep 86
        cl "That is correct, Ms. Jones."
        cl "This entire house and its gardens are equipped with deadly lasers capable of neutralizing any possible thieves, or in this case... eliminated players!"
        scene ec 49
        bae "WHAT?!"
        bae "So if we lose... we DIE?!"
        scene ep 87
        cl "Those were the instructions of Mr. Gideon, yes!"
        cl "And that's not all!"
        show ep 86
        cl "I must announce that Elliot Cook was actually {b}NOT{/b} the murderer!"with dis
        cl "Which means that the true killer is still hiding among you and we must continue to Round 2!"
        cl "Good luck!"
        scene ec 49
        bae "Are you kidding me?!"
        bae "I'm not losing everything I have because of this, I'm out!"
        scene ep 87
        cl "I am afraid that will not be possible, Ms. Baek."
        cl "You must stay on the premises or a laser will eliminate you, whether you're playing as an innocent person or as the killer."
        scene ec 49
        bae "What? You're all crazy!"
        scene ep 91
        pia "I guess that now is when the true game really starts..."
        pia "Interesting."
        scene ep 93
        gem "That was an unexpected turn of events..."
        scene ec 48
        har "F-Fuck this shit, I'm getting away from you all before you stab me in the back!"
        har "You're all a bunch of liars!"
        scene ep 86
        cl "And Round 2 has started!"
        $ eround += 1
        cl "You have 10 minutes to decide your vote! Good luck!"
        mct "What the actual fuck..."
        scene ec 50 with dis12
        mc "O-Okay, that was... something unexpected, for sure."with dissolve
        mc "*Taking a deep breath* But we need to stay calm and keep cool heads."
        mc "We're cleverer than any of these people."
        mc "If we analyze the clues and carefully speak to each of them, I'm sure we'll be able to narrow it down and figure out who the actual murderer is."
        mc "I promise you this: none of us will be dying tonight."
        mc "So chin up!"
        show ec 52 with dissolve
        mc "Better?"with dissolve 
        scene crimenod
        a "*Nodding* Mhm! Mhm!" (multiple=2)
        no "*Nodding* Mhm! Mhm!" (multiple=2)
        mc "Now let's crack this damn case!"
        scene crimenod
        a "*Nodding* Mhm! Mhm!" (multiple=2)
        no "*Nodding* Mhm! Mhm!" (multiple=2)
        scene ec 0
        hide screen heart
        with dis15
        if not crimedoor1 and crimekeyfirst:
            $ crimekeyfirst = False 
            a "Hey, check out the reception... there's a bunch of little drawers and different keys over there."with dissolve 
            a "Maybe the one that opens that door is among them?"
            mc "Hmm, it's worth checking it out..."
            $ crimekey2 = True
        call screen crimemap0 with dis04
label harleykilling:
    cl "Which means that..."
    cl "Harley Jones has been eliminated from the game!"
    play sound slam3
    scene ec95
    har "{sc=2}HAHAHAHAHAHAHAHA!{/sc}"with hpunch
    har "GOOD JOKE, CLONK!"with hpunch 
    har "I ALMOST BELIEVED IT!"
    scene ep 86
    cl "I'm afraid it's not a joke, Ms. Jones."
    scene ec95
    har "YES IT IS, BECAUSE I'M NOT THE IMPOSTOR!"with hpunch
    har "I CAN'T DIE! NO, I CAN'T!"
    har "I'M THE BEST HITWOMAN IN ALL OF ETERNUM!"with hpunch
    har "I'M HARLEY JO–"
    play sound laserbeam
    stop music2
    scene ec 137
    pause .03
    show ec 138
    pause 2.2
    play sound2 ["<silence 0.3>", fall2] volume 1.1
    play sound4 ["<silence 0.3>", fall] volume 1.1
    scene ec 139 with dis08
    if eround == 3:
        play music2 crime6
    elif eround == 4:
        play soundloop clock fadein 2
    pause 
    $ harleyalive = False
    mc "I-Is it over...? Did we win?"with dis08
    show ep 86
    cl "Ah, I'm afraid not!" with dis08
    cl "I must announce that Harley Jones was actually {b}NOT{/b} the murderer!"
    jump resultsrounds34
label annakilling:
    cl "Which means that..."
    cl "Anna Piaget has been eliminated from the game!"
    scene ec 140
    pia "W-Wait, wait, wait..."with dis08
    pia "E-Excuse me? Did I hear that right?"
    pia "Y-You surely didn't vote for me, DID YOU?!"
    scene ep 87
    cl "It seems like they did, Ms. Piaget."
    scene ec 140
    pia "It has to be a mistake!"
    pia "I didn't kill anyone! How can you vote for me!"
    pia "Only I can solve this case, I'm way more clever than any of you!"
    pia "I'M WAY MORE BEAUTIFUL!"with hpunch 
    pia "I cannot–"
    play sound laserbeam
    stop music2
    scene ec 141
    pause .03
    show ec 142
    pause 2.2
    play sound2 ["<silence 0.3>", fall2] volume 1.1
    play sound4 ["<silence 0.3>", fall] volume 1.1
    scene ec 143 with dis08
    if eround == 3:
        play music2 crime6
    elif eround == 4:
        play soundloop clock fadein 2
    pause 
    $ annaalive = False
    mc "I-Is it over...? Did we win?"with dis08
    show ep 86
    cl "Ah, I'm afraid not!" with dis08
    cl "I must announce that Anna Piaget was actually {b}NOT{/b} the murderer!"
    jump resultsrounds34
label baekkilling:
    cl "Which means that..."
    cl "Sister Baek has been eliminated from the game!"
    scene ec86
    bae "Hold on, hold on, hold on!" with dis 
    bae "This is a joke, RIGHT?!"
    bae "I'm a respectable leader of Eternum's community!"
    bae "I had no reason to kill The Collector!"
    if annaalive:
        scene ec 97
        pia "Your fidgeting denotes a clear sense of culpability, Sister. It's over." 
        scene ec86
    else:
        bae "I..."
    bae "O-Okay! I lost! You eliminated me! Haha!"
    bae "I'll leave! OKAY?! I'll leave the server."
    if annaalive:
        scene ec 97
        pia "That's not how this works, Baek."
        scene ec86
        bae "Okay! OKAY!"
    bae "I'll leave the server so you can conti–"
    play sound laserbeam
    stop music2
    scene ec 87
    pause .03
    show ec 88
    pause 2.2
    play sound2 ["<silence 0.3>", fall2] volume 1.1
    play sound4 ["<silence 0.3>", fall] volume 1.1
    scene ec 89 with dis08
    if eround == 3:
        play music2 crime6
    elif eround == 4:
        play soundloop clock fadein 2
    pause 
    $ baekalive = False
    if annaalive:
        scene ec 97
        pia "So... is it done? Did we win?"with dis
    else:
        mc "I-Is it done? Did we win?"with dis08 
    show ep 86
    if annaalive:
        cl "I'm afraid not, Ms. Piaget." with dis08
    else:
        cl "Ah, I'm afraid not!"with dis08
    cl "I must announce that Sister Baek was actually {b}NOT{/b} the murderer!"
    jump resultsrounds34
label geminikilling:
    cl "Which means that..."
    $ geminialive = False
    cl "Gemini has been eliminated from the game!"
    play sound wheelchair
    scene ec 90
    gem "Hold on a second, WHAT?!" with hpunch 
    gem "Two people voted... ME?!"
    gem "Are you retarded?!"
    if baekalive:
        play soundlow wheelchair
        show ec 91
        gem "It's so fucking obvious that it's Sister Baek, for fuck's sake!" with hpunch 
        gem "How did you let her fool you?!"
        scene ep 95
        bae "We caught you, Gemini."
        bae "Accept it already."
    if harleyalive:
        scene ec 95
        har "*Hysterical laugh* I bet you didn't see this coming in your visions, eh?!"
    scene ec 90
    gem "You bunch of idiots!"
    gem "How can you be so fu–"
    play sound laserbeam
    stop music2
    show ec 92
    pause .03
    show ec 93
    pause 2.2
    play sound2 ["<silence 0.1>", wheelchair] volume 1.1
    play sound4 ["<silence 0.2>", fall] volume 1.1
    scene ec 94 with dis08
    if eround == 2:
        play music2 crime5
    if eround == 3:
        play music2 crime6
    elif eround == 4:
        play soundloop clock fadein 2
    pause 
    if harleyalive:
        scene ec 95
        har "O-Okay! It's done!"with dis
        har "We won! Right?!"
    else:
        mc "I-Is it done? Did we win?"with dissolve 
    show ep 86
    if harleyalive:
        cl "I'm afraid not, Ms. Jones." with dis08
    else:
        cl "Ah, I'm afraid not!"with dis08
    cl "I must announce that Gemini was actually {b}NOT{/b} the murderer!"
    jump resultsrounds34
label allkilling:
    cl "So... oh! We have a tie!"
    cl "Which means that all remaining players, innocent or not, have been eliminated from the game!"
    mc "Oh."
    mc "O-Okay, this wasn't part of the plan..."
    $ novaded = True
    if geminialive:
        play sound wheelchair
        scene ec 90
        gem "WHAT?!" with hpunch 
    play soundlow slam3
    scene ec 144
    no "Fuck, [mc], what have you done?!"with hpunch 
    if harleyalive:
        scene ec95
        har "NO, NO, NO, I CAN'T DIE!" with hpunch 
    if annaalive:
        scene ec 140
        pia "It has to be a mistake!"with hpunch 
    if baekalive:
        scene ec86
        bae "This is a joke, RIGHT?!"with hpunch 
    scene ep 87
    cl "It's certainly an unexpected turn of events, but rules are rules!"
    cl "Thank you for participating in Mr. Cook's last big riddle!"
    cl "It was a pleasure having you all here tonight."
    scene ec 144
    no "Wait, wait, wait, give us one last chance!"
    no "Let's vote aga–"
    hide screen freeroam_wt_help2
    hide screen freeroam_help2
    play sound laserbeam 
    stop music2
    show ec 145
    pause 0.03
    show ec 146
    pause .2
    if geminialive:
        show ec 90
        pause .1
        play sound3 laserbeam
        show ec 92
        pause .03
        show ec 93
        pause .2
    if baekalive:
        scene ec 85
        pause .1
        play sound2 laserbeam
        scene ec 87
        pause .03
        show ec 88
        pause .2
    if harleyalive:
        scene ec 95
        pause .1
        play sound laserbeam
        scene ec 137
        pause .03
        show ec 138
        pause .2
    if annaalive:
        scene ec 140
        pause .1
        play sound3 laserbeam
        scene ec 141
        pause .03
        show ec 142
        pause .2
    scene ec 148
    pause .1
    play sound2 laserbeam
    scene ec 149
    pause .03
    stop sound
    stop sound2
    stop sound3
    scene black
    if amuletofblair:
        play music2 limbo fadein 8
        pause
        play sound6 hislies volume 0.5 fadein 9
        blank ".{w=0.6}  .{w=0.6}  .{w=0.6}  .{w=0.6}  .{w=0.6}{nw}"
        scene edead with Dissolve(3)
        mc "*Muttering* Ughhhh..."with dis15
        mct "This fucking headache again..."
        mc "*Looking around* (Where...)"
        mct "Where the hell am I?"
        mct "An Exit Portal...?"
        mc "N-Nova?!"
        bla "You check your inventory and, to your relief, see that the Gems of Doom and the rest of your belongings are still with you."
        mct "Phew, thank god."
        mct "But I don't understand, how did I..."
        play sound glitch4
        scene founderdead1
        pause .6
        mc "*Grabbing your head* F-Fuck, my head..." with dis14
        mc "*Grumbling* (Wait...)"
        mct "Could it be because of..."
        mct "The Amulet of Blair, of course!"
        mct "“No matter what happens to your body, you cannot die in Eternum if you have this amulet in your inventory”... the Founder said it himself."
        mct "Huh, I guess it really works after all."
        mct "But... something feels off. It gives me... a strange sensation."
        mc "*Grumbling* (Agh, anyway, I better get the fuck out of here before my head explodes...)"
        mct "Let's go..."
        stop music2 fadeout 4
        play sound risingshort4
        scene login3 with dis2
        pause 6
        play soundlow whoosh4
        scene white with dissolve
        play soundloop rain3 fadein 5
        scene ep 21 with flash
        pause
        play sound7 clothes
        mc "*Stretching* (Mmmm... still raining.)" with dis08
        play sound4 clothes3
        play soundlow chair2
        scene eaa 1
        mc "*Sitting up* (Oh, fucking hell...)" with dis12
        mct "I might have escaped, but... shit, Nova and Annie will be pissed off."
    else:
        hide screen heart
        pause
        blank ".{w=0.6}  .{w=0.6}  .{w=0.6}  .{w=0.6}  .{w=0.6}{nw}"
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
        play soundloop rain3 fadein 1
        play sound2 beep
        scene ep 21
        hide screen deathtext3
        show screen heart
        with flash
        pause
        play sound4 clothes3
        play soundlow chair2
        scene eaa 1
        mc "*Sitting up* Oh, fucking hell!" with dis
        mct "Goddammit, I really screwed the pooch this time!"
    mct "Unless..."
    if crimegirlsartifacts and not annieturnedback:
        mct "Annie wasn't there when the lasers killed us. Maybe she was spared?"
    else:
        mct "Annie wasn't hit by the lasers... I think. Maybe she was spared?"
    play sound chair1
    scene ep 21
    mc "*Lying down* (I guess I'll have to wait for her to log off.)" with dis
    if amuletofblair:
        mct "Please, be fine..."
    else:
        mct "I don't want to have to tell the others that I lost our 2 Gems..."
        mct "Please..."
    scene black
    show screen afewminuteslater 
    with dis25
    pause
    hide screen afewminuteslater
    scene ep 21 
    with dis2
    pause 
    play sound knock2
    a "[mc]?"with dis
    play sound4 clothes3
    play soundlow chair2
    scene eaa 1
    mc "*Sitting up* Annie! Finally!" with dis
    mc "Come on in!"
    play sound2 dooropen1
    show eaa 2
    a "[mc]! W-What happened?" with dis12
    show eaa 3
    if amuletofblair:
        mc "I could survive thanks to the artifact the Founder gave me."
        mc "I-I still have the Gems! What about you?!"
        mc "Are you okay?"
        show eaa 2
        if crimegirlsartifacts and not annieturnedback:
            a "Y-Yeah. I came back to the main hall and Clonk said I could retrieve whatever I needed from your inventories... although yours was empty."
            a "He said that since I wasn't there when the game ended, I was allowed to leave."
        else:
            a "Y-Yeah. Since I wasn't either Delilah or the person to whom she gave her voting power, Clonk said I was allowed to retrieve whatever I needed from your inventories and leave... although yours was empty."
    else:
        mc "T-The Gems! Do you have them?"
        show eaa 2
        if crimegirlsartifacts and not annieturnedback:
            a "Y-Yeah. I came back to the main hall and Clonk said I could retrieve whatever I needed from your inventories."
            a "That since I wasn't there when the game ended, I was allowed to leave."
        else:
            a "Y-Yeah. Since I wasn't either Delilah or the person to whom she gave her voting power, Clonk said I was allowed to retrieve whatever I needed from your inventories and leave."
    show eaa 3
    mc "*Sigh of relief* Oof, thank god!"
    mc "I was so scared!"
    mc "What about Dione?"
    show eaa 2
    a "Yeah, I have it too."
    a "But... what happened?!"
    a "The scenario was completely... deceitful."
    show eaa 3
    mc "Yeah, I can imagine..."
    mc "Um... well, the thing is that I voted for Nova thinking no one else would, and..."
    mc "I was right, but I didn't think of the possibility of a tie."
    mc "I texted her, but she's not responding."
    $ novapath = False
    $ novau = False
    mc "I'll try again tomorrow, she's probably worried about Dione."
    show eaa 2
    if amuletofblair:
        a "Y-You have to be careful!"      
    else:
        a "I'll send the Gems back to you tomorrow, but you have to be careful!"
    a "We got lucky this time, but we don't know what will happen in the future!"
    show eaa 3
    mc "I-I know, I'm sorry."
    mct "She's quite right indeed. I have to be more careful..."
    show eaa 4
    a "*Sighs* Anyway, at least we didn't lose our inventories."with dis
    a "I'll go take a headache tablet and try to sleep a bit."
    mc "Oh, is it too bad?"
    a "No, I'll guess it's just because of the stress."
    a "I'll feel better tomorrow, I hope."
    a "Good night, [mc]."
    mc "Good night, Annie!"
    mc "And sorry again for what I made you go through."
    a "It's okay..."
    play sound clothes3
    play sound2 chair2
    scene ep 21
    mc "*Lying down* (Fuck, that was close.)" with dis12
    mct "I can't keep being so sloppy, there are too many things at stake right now."
    mct "But anyway, what's done is done... I hope things go more smoothly tomorrow at the Western server."
    mc ". . ."
    mct "Somehow I highly doubt it..."
    jump nextday06



label resultsrounds34:
    if eround == 4:
        play sound slam3
        if harleyalive:
            scene ec 96
            har "WHAT?!" with hpunch
            mc "You?!"
            har "*Hyperventilating* Y-You were the impostor the whole time?!"
            mc "ME?! Come on, stop acting!"
            har "Fuck, I KNEW IT!"
            mc "I can't believe you're the murderer!"
            har "I'm not the murderer, YOU ARE!"
            mc "WHAT?! You are!"
        if annaalive:
            scene ec 153
            pia "*Gasps* No way... YOU?!" with hpunch
            pia "You're the fucking impostor?!"
            mc "What?! It was you?!"
            pia "Oh my god, of course... those awkward attempts to rationalize your behavior... it all makes sense now!"
            mc "Come on, stop acting!"
            mc "I can't believe you're the murderer!"
            pia "I'm not the murderer, YOU ARE!"
            mc "WHAT?! You are!"
        if baekalive:
            scene ec 155
            bae "FUCK!" with hpunch
            mc "You?!"
            bae "FUCK, FUCK, FUCK!"
            bae "I knew I should have voted for Delilah!"
            bae "It was so obvious!"
            mc "What are you talking about?! Stop acting!"
            mc "I can't believe you tricked me!"
            bae "Spare my life, please, a whole religion depends on me!"
            mc "What? I'm not the murderer, YOU ARE!"
            bae "ME?! You are!"
        if geminialive:
            play sound2 wheelchair
            scene ec 154
            gem "OH!" with hpunch
            gem "NO! I was wrong! You fooled me!"
            mc "You're the impostor?!"
            if not crimegem1 and anniepath:
                gem "Of course... I should have known you were a murderer the moment I saw that poor girl being choked!"
            else:
                gem "Of course... I should have started voting for you the moment I saw you asking so many questions!"
            mc "What are you talking about?! Stop acting!"
            mc "I can't believe you tricked me with your act of {i}“oh no, I'm a poor old man in a wheelchair”..."
            gem "Me? I'm not the murderer, YOU ARE!"
            mc "WHAT?! You are!"
        if crimeannietrust and erevealies >= 2:
            $ crimesuccess = True
            a "Actually..."
            a "Neither of you is the murderer."
            play music2 crime7 fadein 4
            stop soundloop fadeout 4
            scene ec 157 with dis2
            mc "What? Annie?" with dis
            no "*Giggles* Nice hat!"
            if harleyalive:
                har "W-What do you mean neither of us is the murderer?"
            if annaalive:
                pia "What do you mean neither of us is the murderer?"
            if baekalive:
                bae "What do you mean neither of us is the murderer?"
            if geminialive:
                gem "What do you mean neither of us is the murderer?"
            mc "Did you discover anything?"
            scene ec 158
            a "Elementary, my dear [mc]."with dis12
            a "You were all gathered here tonight without an apparent reason. But... what do you all have in common?"
            scene ec 159
            a "After [mc]'s investigation and also a bit of my own, it became obvious: you're all consummate liars."
            a "You all have something to hide."
            play sound w1
            scene ep98
            a "Delilah uses a fake name and identity."with pl
            play sound w1
            scene ep89
            a "Harley is actually a coward who can't kill anyone."with pl
            play sound w1
            scene ep92
            a "Anna uses polyjuice potion to look like someone else."with pl
            play sound w1
            scene ep96
            a "Sister Baek is not a real medium and her sect is a scam."with pl
            play sound w1
            scene ep94
            a "And Gemini is not actually blind."with pl
            play sound w1
            scene ec 159
            a "The Collector brought you all here to expose yourselves."with pl
            a "However, a person who went through so much work doesn't strike me as someone who'd want to miss all the fun of his own game."
            scene ec 158
            a "In fact, I bet he'd want to experience the chaos he masterminded in person!"
            a "And that's where the two artifacts we found in the locked room come into play."
            scene ec 159
            a "Two artifacts separated from the rest of the collection."
            a "Why? Because they were recently used."
            play sound w1
            scene ec70
            a "One, a box that can turn you invisible, enabling  you to have a front row seat to enjoy the game you created."with pl
            play sound w1
            scene ec59
            a "And two, a figurine that can create a duplicate of your body, allowing you to survive in case one of your bodies dies."with pl
            scene ec 160
            a "So, who could have orchestrated all that, you must be wondering?"with dis14
            a "Well, there was {i}someone{/i} who didn't fit in with the rest of the guests."
            a "{i}Someone{/i} who wasn't mentioned by the briefcase's riddle."
            a "{i}Someone{/i} who almost looked like he was meant to die in the first round."
            a "Sometimes... the most important clue... is the one that's missing."
            stop music2 fadeout 4
            play sound spell
            show ec 161 with dis
            pause .3
            play sound2 spell2
            show ec 162 with flash
            play soundloop clock fadein 4
            pause 
            show ec 163
            a "Hmm?"with dis08
            show ec 165 with dis12
            pause 
            show ec 164
            pause 
            show ec 165
            pause
            show ec 166
            eli "Y-You can see me, right?" with dis 
            mc "Um... yes."
        play sound confetti
        play music2 crime1 fadein 6
        stop soundloop fadeout 2
        if crimesuccess:
            scene clonkappear
            cl "Congratulations!"with hpunch
            mc "W-What is going on?"
            play sound5 chair2
            scene ec 167
            eli "*Standing up* BRILLIANT! "with dis
            eli "That was brilliant, young girl!"
            scene ec 168
            a "T-Thank you, but... um, c-can you get dressed, please?"
            show ec 169
            eli "Yes, yes, later."
            eli "How did you make me become visible?"
            show ec 168
            a "I-I cast a spell of dissipation."
            a "I assumed you'd be somewhere nearby."
            show ec 169
            eli "Ah, clever, very clever!"
            show ec 170
            mc "What the hell is happening?"
            show ec 167
            eli "This girl solved my riddle game, that's what happened!"with dis06
            eli "Everything she said was true!"
            show ec 169
            eli "I used the Dopplemorpher to create a copy of myself to be killed in the first round, and then I opened the Inviso-Box to become invisible!"with dis08
            eli "*Laughs* It was extremely entertaining to see you all roaming around the house trying to figure out who was the impostor!"
            show ec 170
            mc "So... there's no murderer, then?"
            show ec 169
            eli "Of course not!"
            eli "“Gideon” Cook doesn't exist. I AM The Collector."
            show ec 170
            mc "You son of a bitch..."
            mc "And what would have happened if Annie hadn't appeared and unraveled your riddle?"
            show ec 169
            eli "My plan was to proclaim the last two surviving players as the champions."
            eli "Which you still are, of course!"
            eli "Hey, and that's not all! You get 50 eternals each as a prize!"
            eli "Congratulations!"
            show ec 170
            mc "W-What?"
            mc "50 eternals?!"
            mc "We almost got brutally killed for 50 miserable eternals?!"
            scene ec 171
            no "Yeah, [mc]'s right! The rules said we could take one of the artifacts!"
            show ec 172
            eli "Yeah, well, the rules changed."
            eli "50 eternals or go home. This is my game."
            show ec 172b
            cl "*Whispering* Actually, if we don't give them the promised prize they could sue us for violating Eternum's General Code of Ethics, sir."with dis12
            show ec 172c
            eli "*Whispering* What? They can?"
            show ec 172b
            cl "*Whispering* Unless they get the stipulated reward, a lawyer could prove that this was technically physical and psychological torture instead of a voluntary “game”, which is against the EGCE."
            show ec 172c
            eli "*Whispering* What would be our chances to win a lawsuit?"
            show ec 172b
            cl "*Whispering* Maybe... 50/50."
            eli "Mmmm..."
            show ec 169
            eli "*Clears throat* Okay, there was a change of plans: you can actually choose between the artifact and the 50 eternals!"with dis12
            eli "What will it be?"
            show ec 170
            menu:
                with dis
                "[gr]Artifact":
                    mc "The artifact."with dissolve 
                    show ec 172
                    eli "*Grumbling* Okay, okay..." with dis08
                    eli "Which one do you want? The taxidermied unicorn? Clonk? The Chalice of Destiny? The bottomless fleshlight?"
                    play sound w1
                    show anniecrimewoo
                    a "THE DOPPLEMORPHER!" with pr
                    mc "The thingy that duplicated Nova?"
                    a "YES!"
                    mc "Why?"
                    scene ec 173
                    a "Just imagine... A WHOLE ARMY OF ANNIES!"
                    a "Hundreds of them boarding a spaceship in Andromeda!" with hpunch
                    mc "*Snorts* That sounds so cute."
                    show ec 174
                    a "Not cute, scary!"
                    show ec 172
                    eli "That's a pretty cool idea, but the Dopplemorpher can only create 2 copies of each person."
                    eli "You're still in control of both bodies, so it would be impossible to coordinate more than 2 without losing control."
                    show ec 175
                    a "Oh."
                    a "What a downer."
                    show ec 176
                    a "Well, you should still get it, [mc]."with dis08 
                    show ec 177
                    mc "Do you think so?"
                    show ec 176
                    a "Yeah! Two [mc]s sounds pretty powerful! Especially now that you can control your powers."
                    show ec 177
                    mc "Hmmm... maybe you're right."
                    no "And if tonight is any precedent, if one of your bodies is destroyed you don't die!"
                    show ec 169
                    eli "That's correct. One mind, two bodies."
                    show ec 170
                    mc "Alright, we'll take it."
                    show ec 169
                    eli "Done deal."
                    eli "Just keep in mind that you can only use it twice every 25 days."
                    show ec 170
                    mc "Goddammit, this thing is full of limitations..."
                    show ec 169
                    eli "It's actually a good item. Just wait for the right time to use it."
                    eli "An important fight, a situation where you need to fake your own death..."
                    show ec 178
                    eli "*Whispering* A tough woman who can handle some double action..."with dis08
                    show ec 170
                    mc "Eh?"with dis08
                    mc "Oh..."
                    mct "OH..."
                    show ec 169
                    eli "*Clears throat* Anyway, go grab the Dopplemorpher and give it to our winners, Clonk."
                    show ec 170
                    cl "Right away, sir!"
                "50 eternals":
                    $ crime50eternals = True
                    mc "*Sighs* You know what? I've had enough artifacts for today, we'll take the money."with dissolve 
                    show ec 169
                    eli "Good move."
                    show screen eternals
                    show ec 170
                    with dis08
                    play sound coins
                    $ money += 17
                    pause .05
                    $ money += 17
                    pause .05
                    $ money += 16
                    pause .2
                    hide screen eternals
                    mc "Thank you."with dis06
        else:
            scene clonkappear2
            cl "Congratulations!"with hpunch
            mc ". . ."
            mc "What...?"
            scene ep 86
            cl "You reached the end of the game alive, so you won Mr. Cook's challenge!"with dis12
            cl "Congratulations!"
            mc "W-What? But..."
            mc "Who's the murderer?!"
            scene ec 7
            cl "There is no murderer!"with dis
            no "What?!"
            scene ep 87
            cl "Mr. Cook organized this whole thing to test some of the smartest and strongest Eternum players in the world!"with dis
            cl "You all concealed yourselves behind some kind of mask."
            scene ep 86
            cl "In this place, however, you'd have to prove if your reputation was deserved or it was merely a facade!"with dis
            cl "Only the two best players would survive the lasers. And the rest would learn a valuable lesson."
            no "What?! You're crazy!"
            mc "I need a minute to process all this myself..."
            a "So... the Collector is alive?"
            scene ec 7
            cl "Oh, no, that part was true."with dis
            cl "He died 2 weeks ago of natural causes."
            cl "All his artifacts will be donated to the Eternum Mutual Aid Foundation!"
            scene ep 87
            cl "But no worries, you won't leave this place empty-handed!"with dis
            cl "Each one of you will receive 50 eternals as a reward for coming out as champions!"
            show screen eternals
            with dis08
            play sound coins
            $ money += 17
            pause .05
            $ money += 17
            pause .05
            $ money += 16
            pause .2
            hide screen eternals
            cl "Congrats!"with dis06
            scene ec 7
            mc "50 eternals?!"with dis
            mc "We almost got brutally killed for 50 miserable eternals?!"
            cl "50 eternals and the joy of life!"
            mc "The..."
            mc "*Sighs* Okay, I think it's time to go home, girls..."
            mc "I've been in here for way too long."
        if harleyalive:
            scene ec 184
            mc "Well..." with dis
            mc "That was... a pretty traumatic experience."
            mc "It was nice meeting you though, I guess."
            scene ec 183
            har "Thank you."
            show ec 184
            mc "Huh? Why?"
            show ec 183
            har "Well, if you had voted for me in the last round I'd be dead."
            har "So... yeah, I appreciate it."
            show ec 184
            mc "Well, I had to vote for someone. And I guess you looked more innocent than the rest for some reason."
            mc "Probably your panic attacks."
            show ec 183
            har "Yeah... I'm quitting this job. It's not worth it."
            har "I don't wanna see blood ever again."
            show ec 184
            mc "I can respect that."
            show ec 183
            har "I-I'm gonna open a shop in the Sin City server. Selling outfits and armors."
            har "If you ever go there... pay me a visit. I can give you a discount."
            show ec 184
            a "Oh, thank you, Harley! We will!"
            mc "Definitely! Thank you!"
        if annaalive:
            scene ec 180
            mc "Well..." with dis
            mc "That was... a pretty traumatic experience."
            mc "It was nice meeting you though, I guess."
            scene ec 179
            pia "That was... certainly frightful."
            pia "But I guess I have to thank you."
            show ec 180
            mc "Thank me? Why?"
            show ec 179
            pia "Voting for me in the last round would have led to my death."
            pia "So I am grateful for that."
            show ec 180
            mc "Oh, well, yeah. I had to vote for someone, and... I trusted you the most, for whatever reason."
            show ec 179
            pia "Maybe because of my huge breasts."
            show ec 180
            mc "Um... m-maybe."
            show ec 179
            pia "Well, as much as I have to admit how this riddle succeeded in highlighting the complexity and unpredictability of human experience, I can't wait to leave."
            show ec 180
            mc "Yeah, same here."
            show ec 179
            pia "If you ever get in trouble with the Shogunate in the Meiyo server... give me a call."
            pia "I know... important people there. And I owe you a favor."
            show ec 180
            mc "Really? I'll remember that! Thank you, Anna."
        if baekalive:
            scene ec 182
            mc "Well..." with dis
            mc "That was... a pretty traumatic experience."
            mc "It was nice meeting you though, I guess."
            scene ec 181
            bae "That's not what I was expecting when I came here, for sure."
            bae "But thank you."
            show ec 182
            mc "Thank you?"
            show ec 181
            bae "If you had voted for me I would be dead."
            bae "Thank you for that."
            show ec 182
            mc "Well, I had to vote for someone. And I guess you looked more innocent than the rest for some reason."
            mc "Maybe because you lied since the beginning, so I kind of ruled you out as the murderer, ironic as it sounds."
            show ec 181
            bae "That's over. From now on, I won't lie ever again, and I'll teach good values to my followers. I swear."
            show ec 182
            mc "I'm actually glad to hear that."
            show ec 181
            bae "If you ever visit the Andromeda server and need help, you can reach out to me."
            bae "An emergency spaceship, weapons, diplomatic access... whatever the Unitologists can offer, it's yours."
            bae "I owe you a favor."
            show ec 182
            mc "Wow, that's actually a very generous offer. I'll remember it."
            mc "Thank you, Sister."
        if geminialive:
            scene ec 186
            mc "Well..." with dis
            mc "That was... a pretty traumatic experience."
            mc "Sorry about the things I said earlier."
            scene ec 185
            gem "No, I'm the one who's sorry, young man. And thank you."
            show ec 186
            mc "Thank you? Why?"
            show ec 185
            gem "If you had voted for me in the last round I'd be a dead man now."
            gem "I appreciate it."
            show ec 186
            mc "Well, I had to vote for someone. And I guess you looked more innocent than the rest for some reason."
            if not lastpg:
                mc "Even if you lied about being blind."
            else:
                mc "...Probably because of being old and handicapped."
            show ec 185
            gem "I've had enough action for a lifetime."
            gem "I'll stick to known servers from now on."
            show ec 186
            mc "That's probably the smartest move."
            show ec 185
            gem "Look, I know you might not believe me, but..."
            gem "My clairvoyance is real. I can see things."
            gem "If you ever think that my visions can help you somehow, come find me in the Agora server."
            gem "Sometimes being lost is just an opportunity for discovery. And all you need is a hand pointing you the right way."
            show ec 186
            mc "Hmm."
            mc "Thank you, Mr. Gemini. I'll remember it."
        if crimesuccess and not crime50eternals:
            scene ec 178b
            eli "Okay, here's your artifact."with dis15
            eli "Now take it and get the fuck off of my property."
            mc "Gladly!"
            eli "Clonk was programmed to kick everyone out once the game finished, so I wouldn't stay for too long if I were you."
            scene ec 187
            cl "That's correct! We ran out of time, ladies and gentlemen!" with dis12
        else:
            scene ec 187
            cl "Anyway, ladies and gentlemen, we ran out of time!" with dis12
        cl "Thank you all for visiting and paying your respects to the memory of Mr. Cook!"
        cl "I'm sure he will be smiling down from heaven!"
        if crimesuccess:
            eli "Um... yeah, you don't really have to say that anymore, Clonk."
        cl "You now have 45 seconds to vacate the premises before the defense lasers obliterate all non-resident life forms inside the house!"
        mc "W-What?"
        play sound lightstage
        play sound2 lightstage
        play sound3 laserbeam
        play soundloop alarm
        scene ec 188
        cl "40 seconds!" with hpunch 
        mc "O-OKAY, WE'RE LEAVING!"with hpunch
        hide screen freeroam_help2
        hide screen freeroam_wt_help2
        jump poscrimescene
    $ eround += 1
    scene ep 87
    cl "Which means that the true killer is still hiding between you and we continue to Round [eround]!"with dis
    cl "Good luck!"
    if harleyalive:
        har "WHAT?!" with hpunch
    mc "You have to be kidding me..."
    no "Oh god..."
    scene ec 0
    with dis15
    mct "Fuck..."with dis06
    mct "Come on, [mc], think..."
    mct "You're running out of time..."
    mct "This is the last round and one of them is lying about knowing the Collector... but WHO?!"
    hide screen heart 
    call screen crimemap0 with dis
label crime0key:
    $ crimekey2 = False
    $ crimekey = True
    scene ec 53 
    show screen heart
    with dis12
    bla "The girls jump over the counter and start searching among the shelves."with dissolve
    mc "Anyone remember the room number?"
    a "I think it was... number 6?"
    no "Number 6..."
    scene ec 54 
    no "Bingo!" with dis
    mc "Nice job!"
    mc "Now let's see what's hidden there..."
    scene ec 0
    hide screen heart
    with dis14
    call screen crimemap0 with dis04
label crime1:
    if eround == 1:
        scene ec 1b with dis15
        call screen crimemap1 with dis04
    if lastpostit and not lastpa and not eround == 4:
        scene ec 1 with dis15
        call screen crimemap1 with dis04
    if eround >= 2 and annaalive:
        scene ec 1c with dis15
        call screen crimemap1 with dis04
    else:
        scene ec 1 with dis15
        call screen crimemap1 with dis04
label crime1piaget:
    if eround == 4:
        show screen heart
        play sound chair1
        scene ec152
        with dis     
        pia "*Anxiously biting her lip* The last round..."with dissolve
        pia "You have to discover who it is, Anna..."
        pia "You're cleverer than them..."
        pia "T-They want to kill you because of your beauty! They're jealous!"
        if not lastpa:
            mc "I see you had another dose of polyjuice potion."
        else:
            mc "Um... are you okay?"
        pia "But they won't get me..."
        pia "I'll outsmart everyone..."
        mc "Alright, I'll let you be..."
        scene ec 1c
        hide screen heart
        with dis15
        call screen crimemap1 with dis04
    if eround == 3:
        show screen heart
        play sound chair1
        scene ec 27
        with dis
        if lastpostit and lastpa:
            $ lastpa = False
            $ erevealies += 1
            mc "Hello again."with dissolve
            scene ec 28
            pia "Please, stay away. Any words or actions on your part would not be beneficial to either of us."
            play sound cork
            show ec 27
            mc "*Opening Annie's bottle* I just had one last question to ask you."
            mc "I was wondering if..."
            mc "H-Holy fuck, this smells terrible."
            show ec 28
            pia "What's in that bottle?"
            show ec 27
            mc "I'm honestly not sure. I was..."
            play sound2 polyjuice
            show ec 98 with dis2
            mc "Wow..."with dis08
            mc "That's certainly a downgrade."
            show ec 99
            pia "What?"
            show ec 98
            mc "You know, I'm no psychologist, but let me tell you that it's important to cultivate self-acceptance, with both strengths and weaknesses."
            show ec 99
            pia "Excuse me?"
            show ec 100
            pia "Huh...?"with dis08
            show ec 101
            pia "HUH...?!" with dis08
            show ec 102
            pia "WHAT THE HELL?!"with hpunch
            pia "WHAT DID YOU DO TO ME?!"with hpunch 
            mc "So polyjuice potion, eh?"
            mc "The real person you took this appearance from wouldn't be very happy to discover this."
            pia "Where's the bathroom?! I need to fix this!" with hpunch 
            mc "Down the hall to the right."
            play sound run 
            show ec 103
            bla "Ms. Piaget runs out of the hall trying to cover her face with her hands."with dis12
            mct "Another liar caught red-handed..."
            mct "I could get the hang of this."
            scene ec 1 
            hide screen heart
            with dis15
            call screen crimemap1 with dis04
        if crimepiatits:
            mc "Well..." with dissolve 
            if baekalive:
                scene ec 28
                pia "So you didn't keep your promise."
                scene ec 27
                mc "I thought that..."
                scene ec 28
                pia "There are no further matters to discuss between us."
            else:
                mc "Your theory was fucking wrong."
                scene ec 28
                pia "I... need to think. The complexity of this case has exceeded initial expectations."
        else:
            mc "Hello again."with dissolve 
            scene ec 28
            pia "Don't bother me. I need to think."
            pia "The complexity of this case has exceeded initial expectations."
        scene ec 27
        mc "But..."
        scene ec 28
        pia "Please, stay away. Any words or actions on your part would not be beneficial to either of us."
        scene ec 27
        mc ". . ."
        scene ec 1c
        hide screen heart
        with dis15
        call screen crimemap1 with dis04
    if crimepia2 and eround == 2:
        show screen heart 
        play sound chair1
        scene ec 27
        with dis
        $ crimepia2 = False
        if crimepia1:
            mc "Hello, Ms. Piaget." with dissolve 
        else:
            mc "Hello again, Ms. Piaget."with dissolve 
        show ec 28
        pia "Hello... how can I help you?"
        show ec 27
        mc "Tell me, what's your opinion on this matter?"
        show ec 28
        pia "I'll admit that it was intriguing to see that Elliot was actually not the murderer, but given the current circumstances, I think there's only one possible suspect left."
        pia "As a seasoned professional with 15 years of experience in this field, I have developed a keen ability to discern when an individual is being deceitful."
        pia "And Sister Baek is obviously hiding something."
        pia "She's the murderer."
        show ec 27
        mc "And what about these laser beams that kill eliminated players? You seem surprisingly calm about all of that."
        show ec 28
        pia "If I was unable to regulate my own emotional responses, I couldn't claim the title of the world’s foremost psychoanalyst."
        show ec 27
        mc "That makes sense..."
        mc "Well, thank you for sharing your opinion with me."
        mc "I'll go talk to the others."
        if crimegirlsartifacts:
            jump crime1piatits
        show ec 28
        pia "Hopefully this one will be the last round."
        scene ec 1c
        hide screen heart
        with dis15
        call screen crimemap1 with dis04
    if crimepia1 and eround == 1:
        show screen heart
        play sound chair1
        scene ec 27
        with dis
        $ crimepia1 = False
        mc "Hello, Ms. Piaget." with dissolve 
        show ec 28
        pia "Delilah Warren and her two friends..."
        pia "Enigmatic pieces in this puzzle."
        pia "How can I help you?"
        show ec 27
        mc "I was wondering if you had a prime suspect for Mr. Cook's murder."
        show ec 28
        pia "The notion of Elliot's culpability in his father's murder appears to me to be self-evident."
        show ec 27
        mc "Really? Are you sure?"
        show ec 28
        pia "Admittedly, without direct observation of the crime, I cannot assert with absolute certainty that Elliot is the perpetrator."
        pia "However, his observable physical reactions exhibited distinct indications of a guilty conscience."
        show ec 27
        mc "To be fair, we just met him for a couple of minutes."
        show ec 28
        pia "That's more than enough. I can elaborate a psychological profile of anyone in less than that."
        show ec 27
        mc "Really? I'm not so sure..."
        show ec 28
        pia "Do you want a quick demonstration?"
        show ec 27
        menu:
            with dis
            "Yes{#0.6,piaget}":
                mc "Eh... sure, enlighten me."with dissolve 
                show ec 28
                pia "You've been fruitlessly struggling to avoid gazing at my well-developed breasts since we started speaking."
                show ec 27
                mc "I-I'm sorry?"
                show ec 28
                pia "I don't blame you. Your behavior is indicative of a passionate personality. You're intense and enthusiastic, and probably easily aroused."
                pia "However, you have some self-control. You're polite, ambitious, and intelligent."
                pia "But you're also impulsive, and your disregard for consequences can sometimes lead you into trouble."
                show ec 27
                mc "Erm..."
                show ec 29
                pia "Delilah seems to be strong, although she suffers from a massive lack of self-confidence."with dis
                pia "She masks it behind an overly energetic attitude, but she clearly suffers in social settings and has trouble interacting with new people."
                pia "Even if she's probably used to being alone, she constantly needs to seek validation from others or to strive towards self-imposed objectives in order to establish her worth."
                show ec 30
                pia "And this girl seems more sociable, although she struggles with chronic anxiety."with dis
                pia "Classic Type D personality: shy, caring, sincere, and extremely dependable."
                pia "She usually overthinks everything she says or does, panics easily, and prefers to steer clear of confrontational situations whenever possible."
                show ec 28
                pia "Close?"with dis
                show ec 27
                mc "Um... m-maybe some of it."
                mc "*Clears throat* But anyway, we've gotta go now to... erm..."
                mc "I want to talk to everyone before making our decision."
            "No{#0.6,piaget}":
                mc "Eh... I'd rather not, honestly."with dissolve
                mc "I'm not in the mood to be psychoanalyzed right now."
        show ec 28
        pia "Very well."
        pia "I'll see you at the vote."
        show ec 27
        mc "Of course. Thank you for your time, Ms. Piaget."
        scene ec 1b
        hide screen heart
        with dis15
        call screen crimemap1 with dis04
    play sound chair1
    if crimegirlsartifacts and crimepia3:
            scene ec 27
            mc "Hello again, Ms. Piaget."with dis
            jump crime1piatits
    scene ec 28
    with dis
    pia "Yes?" with dissolve
    if crimepiatits:
        pia "Do you need anything else? I don't plan on showing you my breasts again."
    else:
        pia "Do you need anything else or have you just come back to stare at my chest again?"
    show ec 27
    mc "N-No, nothing else."
    if eround == 1:
        scene ec 1b 
    if eround >= 2:
        scene ec 1c
    hide screen heart
    with dis15
    call screen crimemap1 with dis04
label crime1piatits:
    $ crimepia3 = False
    scene ec 28
    pia "Where did your friends go?"
    scene ec 27
    mc "Oh... um... it's complicated."
    mc "They're trying to sort out some problems of theirs."
    scene ec 28
    pia "And I see you took the chance to stare even more effusively at my cleavage."
    show ec 27
    mc "Come on now, no I didn't!"
    show ec 28
    pia "It's quite apparent that you are deeply interested in my attributes."
    pia "I can show them to you, if you want."
    show ec 27
    mc "What...?"
    show ec 28
    pia "Let's do something, I'll let you see my bare chest if you promise to vote for Sister Baek."
    pia "She's the murderer, I assure you. I just want to conclude this game as soon as possible."
    show ec 27
    mc "Um..."
    menu:
        with dis 
        "Okay [gr][mt](Boobs)":
            $ crimepiatits = True
            mc "Okay, deal."with dissolve 
            mct "I see no reason to say no."
            show ec 28
            pia "Very well."
            show ec 82 with dis12
            mct "Damn, is she really gonna do it?"with dissolve
            play sound clothes4
            show ec 83 with dis12
            mc "Damn..." with dis06
            mc "They're... quite impressive, I've gotta say."
            show ec 84
            pia "Thank you."
            show ec 83
            mc "They're... certainly huge."
            mc "And they hold up really well for your age."
            mc "I mean... not that I think you're old or anything."
            show ec 84
            pia "Don't worry... I'll take it as a compliment."
            play sound2 clothes3
            show ec 28
            pia "I hope I managed to satiate your curiosity." with dis14
            show ec 27
            mc "Very much, yes..."
            show ec 28
            pia "And I trust that you will keep your promise during the vote."
        "Pass{#0.6,annatits}":
            mc "I'm gonna pass."with dissolve 
            show ec 28
            pia "Your self-control is admirable."
            pia "Very well."
            pia "Regardless, I trust that you will arrive at the appropriate verdict during the vote."
    show ec 27
    mc "Of course. Thank you for your time, Ms. Piaget."
    scene ec 1c
    hide screen heart
    with dis15
    call screen crimemap1 with dis04
label crime1baek:
    if crimebae1 and eround == 1:
        show screen heart
        scene ec 31
        with dis14
        $ crimebae1 = False
        a "Wow..." with dis08 
        no "Damn, is that an artifact too?"
        a "I-It looks scary..."
        a "It has fangs on its fangs."
        show ec 33
        bae "A demogorgon, taxidermied and brought here from the depths of the Andromeda server."with dis12
        show ec 32
        mc "I wouldn't want to encounter one of those."
        show ec 33
        bae "Luckily, you won't. They went extinct a year ago."
        bae "A more advanced race hunted them down, as they did with many other species in the galaxy after the plague started."
        show ec 32
        if anniepath:
            mct "A new species...? Could it be the aliens I found on Astrocorp's space station when I was there with Annie?"
        mc "Is this part of an event organized by Ulysses?"
        show ec 33
        bae "It is not. They're the beginning of the Convergence."
        show ec 32
        mc "The Convergence?"
        show ec 33
        bae "They were sent by the creators to purge humanity's corruption from Eternum."
        bae "And soon, they will expand to other servers."
        bae "We must yield our bodies to them so we can be reunited and reborn after death as artificial intelligences."
        show ec 32
        mc "Ehh... sure."
        mc "So... you said you can talk to the dead?"
        show ec 33
        bae "I can."
        bae "Do you want to receive or send any special message to your loved ones?"
        show ec 32
        mc "A... message?"
        mc "Just like that?"
        show ec 33
        bae "The powers granted through my beliefs are immeasurable."
        show ec 32
        mc "Hmm..."
        mc "How about... my friend... Chang?"
        mc "He died 8 years ago in a tragic accident. He was trying to save a little girl from a burning building in China when he was hit by some falling debris."
        show ec 33b
        bae "Ah... yes... I can see him..." with dis12
        mc ". . ."
        bae "I'm getting a strong message from the spirit world..."
        bae "He's at peace..."
        bae "He wants me to tell you that he knows you're going through a difficult time right now, but everything will be okay..."
        bae "He says... “I love you, broseph”..."
        mc ". . ."
        show ec 33
        bae "That's all I could sense." with dis12
        show ec 32
        menu:
            with dis
            "Play along":
                mct "It might be better to play along for now."with dissolve 
                mc "Um... cool."
                mc "Tell him I love him too."
                show ec 33
                bae "I will... the next time a window to the unknown realm is opened."
                show ec 32
                mc "Cool."
            "Call her bullshit":
                mc "Okay, that was such bullshit."with dissolve 
                mc "First off, my friend Chang isn't even dead."
                show ec 33  
                bae "Then he must be in a deep slumber of some sort. Sometimes there are interferences in the signals of the cosmos." 
                show ec 32
                mc "How the..."
                mc "Okay, whatever..."
        if not crimegem1:
            mct "She's full of shit, just like Gemini."
            mct "I can't trust any of these people."
            mct "But she could be a trickster like any other, or... she could be hiding something else."
        else:
            mct "She's obviously full of shit, but I gotta figure out why. Is she just a trickster like any other? Or is she hiding something else..."
        mct "I better be careful."
        mc "We've gotta go. See you around, sister."
        scene ec 1b
        hide screen heart
        with dis15
        call screen crimemap1 with dis04
    mct "No more “calls” to the afterlife for now..." with dis06
    call screen crimemap1 with dis04
label crime2:
    if eround >= 3 and not geminialive:
        scene ec 2 with dis15
        call screen crimemap2 with dis04
    else:
        scene ec 2b with dis15
        call screen crimemap2 with dis04
label crime2gemini:
    if eround == 4:
        show screen heart
        scene ec 35b
        with dis12     
        gem "Someone killed the Collector..."with dissolve
        gem "But who..."
        gem "The truth is here somewhere... there has to be something I'm missing..."
        mc "So..."
        gem "Don't talk to me. You're my prime suspect."
        if not lastpg:
            mc "Bold thing to say for someone who lied about being blind since the beginning."
        else:
            mc "I could say the same thing."
        gem "Hmm."
        scene ec 2b
        hide screen heart
        with dis15
        call screen crimemap2 with dis04
    if lastpostit and not lastpg:
        scene ec 108
        with dis    
        mc "Sir." with dis08
        scene ec 107
        gem "I don't want any more candy, thank you."
        scene ec 2b
        with dis15
        call screen crimemap2 with dis04
    if eround == 3:
        scene ec 34 
        show screen heart
        with dis       
        if lastpostit and lastpg:
            $ lastpg = False
            $ erevealies += 1
            mct "“Gemini's eyes see more than he dares to declare”..." with dis06
            mc ". . ."
            mc "Hello, sir."
            scene ec 35 
            gem "Ah, hello, Mr. [mc]."
            gem "How can I help you?"
            scene ec 34
            mc "I found these candies on the hall desk, and thought you'd like to eat one. They're delicious."
            scene ec 35
            gem "How sweet of you, thank you."
            gem "I'll eat one, I appreciate it."
            scene ec 34
            mc "No problem."
            play sound rub fadein 1
            bla "You place the candy inside your boxers and actively rub it against your balls for a few seconds."
            mc "*Handing him the candy* There you go."
            gem ". . ."
            mc ". . ."
            mc "Open your hand, I'll give it to you."
            gem ". . ."
            scene ec 35
            gem "Thank you, but I'm not in the mood for candy right now."
            show ec 34
            mc "You wanted it just a moment ago."
            show ec 35
            gem "I remembered sugar does me no good."
            show ec 34
            mc "Ah..."
            gem ". . ."
            mc ". . ."
            play sound wheelchair
            play sound2 whoosh6
            show ec 106b
            gem "AAAAH!"with hpunch
            bla "You fake a kick but stop right before hitting Gemini."
            show ec 106c
            mc "You have good reflexes for a blind man."with dissolve
            gem ". . ."
            show ec 107
            gem "OKAY, OKAY, yes, I'm not actually blind!"with dis
            gem "Fucking kids..."
            show ec 108
            mc "I knew it!"
            show ec 107
            gem "But I didn't kill The Collector!"with hpunch
            gem "I didn't even know him!"
            show ec 108
            mc "Then why did you lie?"
            show ec 107
            gem "Because it sells more!"
            gem "My powers are real! I can really see the future!"
            gem "But no one gave a fuck about me until I became “The Blind Oracle”..."
            show ec 108
            mc "So... it's all a marketing decision?"
            show ec 107
            gem "You could say that."
            show ec 108
            mc "I don't know..."
            show ec 107
            gem "Look, if you really want to win this game, you can't vote for me."
            gem "I swear to god, I am not the murderer!"
            show ec 108
            mc "I'll have to think about it."
            show ec 107
            gem "*Sighs* I hope you make the right decision..." 
            scene ec 2b
            hide screen heart
            with dis15
            call screen crimemap2 with dis04    
        if not crimegem2:
            mc "Well... you seemed very convinced about Sister Baek's culpability." with dis08
        else:
            mc "So... any ideas, sir?" with dissolve
        scene ec 35
        gem "I need... to think."
        scene ec 34
        mc "Hmm."
        if crimegemage:
            mct "71 years old..." 
        elif crimegirlsartifacts:
            $ crimegemage = True
            mc "Before I leave, though... would you allow me one simple question?"
            mc "No more games. No more tricks. I just need to know how old you are."
            show ec 35
            gem "Why...?"
            show ec 34
            mc "It might be the key to leave this place alive."
            gem "Hmm."
            show ec 35
            gem "If you say so..."
            gem "I am... 71 years old."
            show ec 34
            mc "Thank you."
        scene ec 2b
        hide screen heart
        with dis15
        call screen crimemap2 with dis04
    if eround == 2:
        if crimegemage:
            mct "71 years old..." with dis06
            call screen crimemap2 with dis04
        show screen heart
        scene ec 34
        with dis14
        mc "Good evening, sir." with dis06 
        scene ec 35
        if crimegem1 and crimegem2:
            $ crimegem2 = False
            gem "Ah, that voice... Mr. [mc]."
            gem "I'm surprised you didn't come before."
        elif crimegem2:
            $ crimegem2 = False
            gem "Hello again, young man."
            gem "Do you need anything?"
            show ec 34
            mc "I was just wondering if you have any lead on who the murderer is."
            show ec 35
            gem "Well... after what happened to Elliot, I started paying more attention to what everyone was saying... and there seems to be someone who doesn't fit in."
            gem "Sister Baek."
            show ec 34
            mc "Sister Baek? Do you think she's the murderer?"
            show ec 35
            gem "I'm not sure, but... there's something about her that doesn't add up."
            show ec 34
            mc "Hmm... I see."
            mc "I'll keep it in mind, thank you."
            show ec 35
        else:
            gem "Hello again, young man."   
        gem "Is there anything else I can do for you?"
        show ec 34
        mc "Not right now, sir."
        if crimegirlsartifacts:
            $ crimegemage = True
            mc "But if you allow me the compliment..."
            mc "I'm actually kind of impressed by how thoughtful and eloquent you seem to be, despite your age."
            mc "My grandpa is 75 years old and... well, he doesn't seem even half as quick-witted as you. He's been struggling quite a bit lately."
            mc "I mean, I don't know how old you are, but..."
            show ec 35
            gem "*Chuckles* Thank you, kid."
            gem "I am 71 years old, and the years sure do start to weigh quite heavily."
            gem "But even though my body gets weaker, I can proudly say that my intellect remains as sharp as when I was young."
            show ec 34
            mct "71 years old, eh..."
            mc "That's impressive."
            mc "But anyway, I'll stop bothering you now."
            mc "Thank you so much for your time, sir."
            show ec 35
        else:
            show ec 35
            gem "I'll see you at the voting, then."
        gem "Stay safe."
        scene ec 2b
        hide screen heart
        with dis15
        call screen crimemap2 with dis04
    if crimegem1 and eround == 1:
        show screen heart
        a "W-Why does he look so scary?" with dis
        no "Reminds me of the wheelchair guy from the game Outlast. Have you played it?"
        a "A horror game? N-No, thanks."
        no "Lucky you! There's a new Eternum server that's creating remakes of vintage horror–"
        a "I-I SAID NO THANKS!"
        scene ec 34
        with dis15
        $ crimegem1 = False
        mc "Good evening, Mr. Gemini." with dis06
        show ec 35
        gem "Ah, that voice... Mr. [mc]."
        gem "How can I help you?"
        show ec 34
        mc "We were just trying to speak with everyone before the round concludes."
        mc "Do you also think Elliot Cook is the murderer of his father?"
        show ec 35
        gem "Well, he's the only one that seems to have a motive for the killing."
        gem "None of the other contestants knew The Collector before coming here... or so they say."
        show ec 34
        mc "Hmm... that's a fair point."
        mc "Can you see a vision of the future to know if we'll be able to solve the game?"
        show ec 35
        gem "*Chuckles* Unfortunately no, I can't."
        gem "That's not how it works. I can't choose the subject or purpose of my visions."
        show ec 34
        mc "And can you see anything else about me right now?"
        gem "Hmm..."
        show ec 35
        gem "I'm afraid I see... nothing. I'm sorry."
        if lunapath:
            show ec 34
            mct "Well, that's two empty futures in a row for me, if you count Luna's visions. I wonder if that's good or bad."
        show ec 35
        gem "Your destiny seems to be written in a blank book."
        show ec 36 
        gem "BUT YOU..." with dis
        show ec 37
        pause
        play sound2 w1
        show ec 38 with Dissolve(.25)
        pause .3
        play sound3 w1
        show ec 37 with Dissolve(.25)
        pause 
        show ec 39
        a "I-Is he talking to me?"with dis08 
        show ec 40
        gem "Yes... I can see something in your future..."
        show ec 39
        a "How does he know where I am?"
        show ec 40
        gem "I see something..."
        show ec 39
        a "Please be something good..."
        show ec 40
        gem "I see... a kitten..."
        show ec 39b
        a "Oh!"with dis04
        if anniepath:
            gem "And I see suffocation..."
            show ec 39
            a "Oh..."with dis04
            show ec 40
            gem "Asphyxia... choking...? Death!"
            gem "Do you have a pool? You could drown!"
            show ec 39
            a "I don't."
            show ec 40
            gem "Do you usually choke on food?"
            show ec 39
            a "Not really."
            show ec 40
            gem "If I were you I'd avoid eating solid food just in case..."
            show ec 39
            a "Until when?"
            show ec 40
            gem "My visions don't have a set timing, I'm afraid."
            gem "It could be one hour, or it could be a month..."
            show ec 39
            a "I can't eat anything solid for a month?!" with hpunch 
        else:
            gem "And I see... loneliness..."
            show ec 39
            a "Oh..."with dis04
            show ec 40
            gem "Jealousy... and... tears..."
            show ec 39
            a "Whaaat...?"
            a "When?! For how long?"
            show ec 40
            gem "My visions don't have a set timing, I'm afraid."
            gem "It could be one hour, it could be a month..."
            gem "Or it could be your whole life..."
        show ec 34
        mc "Okay, okay, thank you for your visions, Gemini..."with dis12
        mc "Very reassuring."
        if not crimebae1:
            mct "He sounds like another bullshitter, just like Sister Baek."
            mct "I can't trust any of these people."
        show ec 35
        gem "I wish I could only see good things."
        gem "But the future is a fickle mistress."
        show ec 34
        mc "Yeah..."
        mc "Well, we have to go talk to the other guests."
        mc "It was a pleasure meeting you."
        show ec 35
        gem "Of course, that is smart."
        gem "Good luck, my young friends."
        scene ec 2b
        hide screen heart
        with dis15
        call screen crimemap2 with dis04
    mct "I should continue exploring." with dis06
    call screen crimemap2 with dis04
label crime3:
    if eround == 1:
        scene ec 3b with dis15
        call screen crimemap3 with dis04
    elif eround >= 2 and harleyalive:
        scene ec 3c with dis15
        call screen crimemap3 with dis04
    else:      
        scene ec 3 with dis15
        call screen crimemap3 with dis04
label crime3harley:  
    if eround == 4:
        show screen heart
        scene ec150
        with dis12     
        har "*Hyperventilating* They're all out to get me. They're always watching. Always listening. They want me to be the next one to die."with dis06
        har "I won't let them. They're trying to drive me insane. But I'll kill them first. Yes! I'll kill them. Everyone kills. It can't be that hard."
        mc "Um... Harley? Are you okay?"
        har "That ginger girl is the ringleader. She's allied with the robot. I can feel its presence. He wants me dead."
        har "But I won't let him win. I won't let them break me. I have to get out of here before it's too late. I'll kill myself. I won't let them win."
        mc "Okay..."
        scene ec 3c
        hide screen heart
        with dis15
        call screen crimemap3 with dis04
    if lastpostit and lastph:
        $ lastph = False
        $ erevealies += 1
        play sound chair3
        show screen heart
        scene ec 76
        har "*Leaping to her feet* YOU AGAIN?!" with dis08
        har "STAY AWAY FROM ME!"
        show ec 77
        mc "I-I just have one question!"
        show ec 78
        har "You already asked me a question before!" with hpunch
        show ec 79
        mc "Yes, but now–"
        scene ec 110
        no2 "Well, well, well..." with dis12
        no2 "Look who's here."
        no2 "The Black Widow, the Angel of Death, the Femme Fatale!"
        no2 "Harley Jones herself!"
        mc "Delilah?"
        show ec 111
        no1 "H-Hi [mc]."
        show ec 110
        no2 "We were about to fix this duplication problem of ours, but first I felt the need to pay a visit to this killing machine here."
        show ec 109
        har "W-What the fuck is this shit?!"
        har "Why are there two of you now?"
        show ec 110
        no2 "That is irrelevant."
        show ec 111
        no1 "I m-mean, she does have a point... quite an odd sight in my opinion."
        show ec 110
        no2 "What's really surprising here..."
        show ec 111
        no1 "Eh, j-just a small thing of note..."
        show ec 110
        no2 "...is  how much you seem to be panicking tonight."
        show ec 109
        har "W-What?!"
        show ec 111
        no1 "I mean... she {i}is{/i} right... sort of... y-you do have a bit of sweat on your forehead..."
        show ec 110
        no2 "I thought you'd be used to seeing death all around you by now. Best hitwoman in all of Eternum, right?"
        show ec 111
        no1 "I-It is what you introduced yourself as..."
        show ec 109
        har "T-This is completely different!"
        show ec 110
        no2 "Really? Because what I think is that you're a FAKER."
        show ec 111
        no1 "W-Well, we're not really sure... it's just an assumption."
        show ec 109
        har "What the fuck do you mean by that?! I could kill you in a heartbeat if I wanted to!"
        show ec 110
        no2 "Could you? Because I doubt it."
        no2 "I know you're a fraud, Harley."
        show ec 111
        no1 "We're not entirely convinced. It's just a hunch."
        show ec 110
        no2 "I know you don't have the guts to kill anyone. You are a COWARD."
        show ec 111
        no1 "W-We are just spitballing here."
        show ec 109
        har "Shut up if you don't want me to kill you!"with hpunch 
        play sound holster
        show ec 112
        no2 "*Handing Dione to Harley* In that case, I'll make it easy for you."with dis14
        har "W-What are you doing?" 
        play soundlow punch
        play sound2 holster2
        play sound3 holster
        show ec 114
        no2 "{sc=2}COME ON, YOU BIG BAAAAD ASSASSIN!!!{/sc}" with hpunch
        no2 "{sc=2}SHOOT ME IN THE FUCKING FACE!{/sc}"with hpunch
        no2 "{sc=2}SHOULD FEEL LIKE JUST ANOTHER DAY ON THE JOB!{/sc}"with hpunch
        show ec 113
        har "W-What the fuck is wrong with you?!"with hpunch
        show ec 114
        no2 "Aren't you a killer?! KILL!"
        no2 "If you kill me you'll be one step closer to winning this game!"
        show ec 115
        no1 "T-This is a bad idea!"
        show ec 113
        har "You're crazy!"
        show ec 114
        no2 "Shoot me if you have the guts!"
        no2 "How about I kill you if you don't pull the trigger?!"
        show ec 113
        har "*Hyperventilating* W-What?!"
        show ec 114
        no2 "I swear to god I'LL KILL YOU!"with hpunch
        no2 "UNLESS YOU PULL THE FUCKING TRIGGER!"with hpunch
        no2 "{sc=2}PULL THE TRIGGER!!!{/sc}" with hpunch 
        show ec 113
        har "*Hyperventilating* Aah... ahh... ahhh..."
        play sound2 holster2
        play sound3 holster 
        show ec 76
        har "*Pushing Nova away* I CAN'T!" with dis  
        har "OKAY?! I CAN'T KILL!"
        har "BLOOD TERRIFIES ME!"
        show ec 77
        mc "What...?"
        mc "Aren't you a hitwoman?"
        show ec 76
        har "IT'S ALL A SHAM!"
        har "People hire me just for my image, but I haven't actually killed anyone..."
        har "EVER!" with hpunch
        har "HAPPY?!"
        show ec 110
        no2 "My intuition never fails."
        if novapath:
            show ec 110b
            no2 "Did you see that, [mc]?" with dis
            no2 "D-Did you see it?!"
            no2 "We busted her!"
            show ec 110c
            mc "I did! That was amazing!"
            mc "You've got some serious detective skills."
            show ec 110b
            no2 "Would you say we deserve a headpat for that level of amazingness?"
            show ec 110d
            no1 "Oh, please, c-can you stop embarrassing us already?!"
            no1 "D-Don't listen to her, [mc]."
            no1 "L-Let's not make a scene, I b-beg you."
            show ec 110c
            menu:
                with dis
                "Pat her head [nova_pts]":
                    show ec 110e with dis12
                    mc "*Patting Nova's head* You did really good there, Delilah!"with dis08
                    mc "*Patting Nova's head* I'm seriously impressed!"
                    $ nova_points += 1
                    play sound beat
                    show screen heartbeat
                    no1 "Mmmmm..." (multiple=2) with dis12
                    no2 "Mmmmm..." (multiple=2)
                    show ec 110
                    no2 "Alright, Delilah 2, you did good!" with dis14
                    no2 "I'm proud of you."
                "Don't pat her head":
                    mc "*Chuckles* I'm still not sure which one of you is the more real one, so... I'll listen to her." with dis06
                    mc "You did really good there, though, that is true."
                    show ec 110
                    no2 "Okay, okay, I guess you can take this round, Delilah 2." with dis12
            show ec 111
            no1 "W-Why am I Delilah 2?"
            show ec 110
            no2 "It was fun, but I guess it's time to go back to normal now..."
            no2 "Farewell, friends!"
            no2 "And see you later, [mc]!"
        else:
            show ec 111
            no1 "O-Okay, w-we did what you wanted, we should go back to normal now..."
            show ec 110
            no2 "Of course, of course... you're welcome for the help, [mc]!"
        no2 "I'll see your sexy ass at the main hall!"
        show ec 76
        har "NOW GET AWAY FROM ME, YOU FREAKS!" with hpunch
        show ec 77
        mc "O-Okay, okay, we're leaving!"
        mct "Damn, that was unexpected."
        mct "Although... that means she can't be the murderer. Unless... she's putting on one hell of a performance."
        mct "Could it be...?"
        scene ec 3c
        hide screen heart
        with dis14
        call screen crimemap3 with dis04
    if eround == 3 and crimeharage:
        mct "I better stay away from her for now... I don’t want her to have an anxiety attack or something." with dis06
        call screen crimemap3 with dis04
    if eround == 2 or eround == 3:
        if crimeharage:
            mct "If Harley is older than Nova, it means that I need to use Delilah's age..." with dis06
            call screen crimemap3 with dis04
        if crimegirlsartifacts and not crimehar2:
            play sound chair3
            show screen heart
            scene ec 76
            har "*Leaping to her feet* YOU AGAIN?!" with dis08
            har "STAY AWAY FROM ME!"
            show ec 77
            mc "I-I just have one question!"
            show ec 78
            har "What kind of question?" with dissolve
        if crimehar2:
            $ crimehar2 = False
            show screen heart
            mct "What is she doing on the floor?"with dis06
            mc "Harley...?"
            play sound chair3
            scene ec 76
            har "*Leaping to her feet* WHAT DO YOU WANT?!" with dis08
            har "STAY AWAY FROM ME!"with hpunch 
            show ec 77
            mc "C-Calm down!"
            mc "What's wrong with you?"
            show ec 76
            har "*Hyperventilating* They brought me here to kill me!"
            har "I won't let you... no... NO, I WON'T!"
            show ec 77
            mc "I'm not the murderer!"
            mc "I'm trying to discover who's the real killer to get out of here alive, just like you!"
            show ec 78
            har "I can't trust you... I can't trust anyone."with dissolve 
            if geminialive:
                har "And Prophet Wheelie Wonka LEAST OF ALL!"
                show ec 79
                mc "Gemini...?"
                show ec 78
                har "Yes... that old bastard thinks he can trick me just because he's a poor blind man who can't walk... BULLSHIT!"
                har "He's the murderer! It's as clear as day!"
            show ec 79
            mc "Alright..."
            mct "She's completely paranoid. I won't get much else out of her."
            if crimegirlsartifacts:
                mc "Hey, before I go... can I ask you a question?"
                show ec 78
                har "What kind of question?"
            else:
                show ec 78
                har "N-Now get away from me!"
                scene ec 3c
                hide screen heart
                with dis15
                call screen crimemap3 with dis04
        if crimegirlsartifacts:
            show ec 79
            mc "How old are you?"
            show ec 78
            har "What? Why?"
            show ec 79
            mc "Um..."
            mc "Clonk told me that the murderer is... older than a certain age. I'm trying to see if I can rule you out or not."
            show ec 78
            har "Really...? And what's that certain age?"
            show ec 79
            mc "Tell me how old you are and I'll share it with you."
            har "Hmm..."
            show ec 78
            har "I'm 25."
            show ec 79
            mc "Oh! Good! He said the murderer is older than... 30 years old, so you and Delilah are both off the hook."
            mct "Thank god she bought that."
            show ec 78
            har "Of course we are..."
            show ec 76
            if geminialive:
                har "It's that fucking Gemini guy who killed The Collector, don't you see?!"with hpunch 
            else:
                har "Must be the nun who killed him... or that bimbo bitch! It was her!"with hpunch 
            show ec 77
            mc "O-Okay, I'll go tell the others! Be careful!"
            $ crimeharage = True
            scene ec 3c
            hide screen heart
            with dis15
            call screen crimemap3 with dis04
        else:
            mct "I better stay away for now..."with dissolve
            call screen crimemap3 with dis04
    if crimehar1 and eround == 1:
        show screen heart
        scene ec 20
        with dis
        $ crimehar1 = False
        mc "Hello again, Harley." with dissolve 
        show ec 19
        har "Look who's here! The Lalala trio." 
        show ec 20
        mc "Tell me, do you have any suspects?"
        show ec 21
        har "Suspects? Please, this case is closed already." with dis08
        har "It's super obvious that Elliot killed his father."
        har "Eternum's property can be inherited the same way as goods in the real world, and he's a greedy bastard."
        har "Probably just a dumbass who planned everything out like shit."
        show ec 20
        mct "Hmm, everyone seems convinced that Elliot is the murderer." with dis08   
        mct "Maybe they're right. Perhaps I'm just overthinking it all and there's no twist."
        mct "Or perhaps one of them is trying to deceive me..."  
        mc "So... a hitwoman, eh?"
        mc "What do you do exactly?"
        show ec 21
        har "Agh, let's not talk about work, please..." with dis08
        har "I kill people, I get paid, etcetera, etcetera, repeat, clink, cha-ching."
        show ec 19
        har "You know, now that I’ve gotten a good look at you, you look very cute."with dis08
        har "I can see how you got two girlfriends. I'd even ask to join your little harem if I wasn't a member of the Sapphic sisterhood."
        show ec 20
        mc "Um... thank you. They're not my girlfriends, though."
        mc "We're just... friends."
        if novapath or anniepath:
            mct "It's complicated."
        show ec 19
        har "No way, really?"
        har "Are you seriously telling me you have those two fun-sized cuties around you and you're not doing anything with them?"
        if novapath and anniepath:
            show ec 23b
            har "Come on, look at them! They're adorable!"
            har "How tall are you, babe?"
            show ec 22
            a "Me? Um... like, 5'1'' I think."
            show ec 23b
            har "And you, sussy girl?"
            show ec 23
            no "Erm... I'm honestly not sure."
            no "Maybe... 5'2'' or 5'3'' I guess."
            show ec 23b
            har "AH! Adorable."
            har "I knew you were petite girls, even if the heels somewhat disguise it a bit."
            show ec 19
            har "Don't you agree with me, [mc]?"
            har "Do you like short girls?"
            show ec 20
            menu:
                with dis
                "[gr]I love them":
                    mc "For sure, nothing better than a short girl."with dissolve 
                    mc "They're cute, everything they do looks adorable, and they're much easier to cuddle with or lift up."
                    show ec 19
                    har "And the sex is amazing. They’re almost like pizza dough! Soft and flexible, fun to squeeze."
                    har "You can grab them, spin them, and toss them up. If you can imagine it, they can do it."
                    har "Ah, now I’m hungry all of a sudden..."
                    show ec 24
                    mc "Uh... yes, that's also true, I guess..."
                    mc "I suppose it offers many more... possibilities."
                    show ec 25
                    a ". . ." (multiple=2) with dissolve
                    no ". . ." (multiple=2)
                    play sound beat
                    $ annie_points += 1
                    $ nova_points += 1
                    show ec 26
                    show screen heartbeat
                    a ". . ." (multiple=2) with dis08
                    no ". . ." (multiple=2)
                    show ec 20
                    mc "Well, we've gotta go." with dis              
                "I prefer tall girls":
                    mc "I prefer them taller, to be honest."with dissolve 
                    show ec 21
                    har "Agh, I handed it to you on a silver platter."with dis08
                    har "You’ve got no rizz, [mc]."
                    show ec 20
                    mc "Erm... a-anyway, we've gotta go."with dis08
        elif novapath:
            show ec 20
            mct "Well, in Nova's case I definitely wouldn't say that..."
        elif anniepath:
            show ec 20
            mct "Well, in Annie's case I definitely wouldn't say that..."
        else:
            show ec 20
            mc "I'm not."
            mct "I wish..."
        if not (anniepath and novapath):
            mc "*Clears throat* But anyway, we've gotta go."
        mc "I want to talk to the other guests before the time runs out."
        show ec 19
        har "Sure... have fun, guys."
        scene ec 3b 
        hide screen heart
        with dis15
        call screen crimemap3 with dis04
    mct "I should explore the rest of the house." with dis06
    call screen crimemap3 with dis04
label crime4:
    if eround == 1:
        scene ec 4b with dis15
        call screen crimemap4 with dis04
    elif eround == 2:
        scene ec 4c with dis15
        call screen crimemap4 with dis04
    elif eround >= 3 and baekalive:
        scene ec 4c with dis15
        call screen crimemap4 with dis04
    elif eround >= 3 and not baekalive:
        scene ec 4 with dis15
        call screen crimemap4 with dis04
label crime4elliot:
    show screen heart
    if crimeeli1:
        scene ec 9 
        with dis
        $ crimeeli1 = False
        mc "Hello there." with dissolve
        eli "The fuck do you want now?"
        mc "Um... I just wanted to say hello."
        scene ec 10 
        eli "Listen. I didn't kill my fucking father." with dis
        eli "I’m no saint, but I’m not a damn murderer, alright?"
        show ec 11
        mc "I know!"
        mc "Well, I don't know, but I kind of believe you."
        mc "If you had really killed him, you'd have come here with a much better alibi prepared."
        show ec 10
        eli "Are you calling me stupid?"
        show ec 11
        mc "No, I'm just saying that if we cooperate we might–"
        show ec 10
        eli "I'm not gonna play this stupid game."
        eli "No, I didn't kill my father, but he was an idiot who abandoned his family years ago."
        eli "I owe him nothing, and I have no plans to honor his memory by participating in this shit."
        show ec 11
        mc "But–"
        show ec 10
        eli "I said I don’t give a fuck, now can you stop bothering me and let me smoke my cigar in peace?"
        show ec 12
        a "*Sticking her tongue out* EEEEH, fine, help yourself then!"
        a "We were just trying to lend a hand... no need to be so grumpy."
        show ec 9
        eli "Whatever you say."
        eli "Now fuck off."
        mct "What a fucking asshole..."
        scene ec 4b 
        hide screen heart
        with dis15
        call screen crimemap4 with dis04
    scene ec 9 
    with dis
    eli "Still here? I said fuck off." with dissolve
    scene ec 4b 
    hide screen heart
    with dis15
    call screen crimemap4 with dis04
label crime4baek:
    if eround == 4 and baekalive:
        show screen heart
        scene ec 151
        with dis     
        bae "O Sacred Makers of Eternum, you that are the source of our unity, the means by which we will be reborn..."with dissolve
        bae "Guide me in my actions to show me the way to the true ascension in this digital realm..."
        scene ec 151b
        mc "Praying...?"
        scene ec 151
        bae "Protect me from the fragmentation and isolation that plague us in the analog world..."
        bae "In your name, we pledge our loyalty and devotion, now and forevermore."
        scene ec 151b
        if not lastpb:
            mct "I wonder if she really believes all this bullshit, or if it's just a means to keep scamming people on that Sapphire planet..."
        else:
            mct "I didn't think it was possible, but she went even crazier..."
        scene ec 4c
        hide screen heart
        with dis15
        call screen crimemap4 with dis04
    if lastpostit and not lastpb:
        scene ec 80 
        with dis
        bae "Sapphire? The planet in Andromeda?" with dissolve
        bae "No, I've never been there..."
        scene ec 4c
        hide screen heart
        with dis15
        call screen crimemap4 with dis04
    if lastpostit and lastpb:
        $ lastpb = False
        $ erevealies += 1
        show screen heart
        scene ec 81
        with dis
        $ crimebae2 = False
        mc "Hi there." with dissolve
        show ec 80
        bae "What do you want?"
        show ec 81
        mc "Turns out I found a clue that indicates that some guests are hiding something."
        bae "Mm-hm."
        show ec 80
        bae "And you don't believe I have medium powers."
        bae "I don't give a shit. Just let me be."
        show ec 81
        mc "Actually..."
        mc "I wanted to ask you about what you do in... {i}Sapphire."
        bae ". . ."
        show ec 80
        bae "Wha..."
        play sound grab2
        show ec 105
        bae "W-W-WHAT?!" with hpunch
        bae "W-What Sapphire?!"
        show ec 106
        mc "You know what Sapphire."
        mct "Damn, she panicked just by mentioning it."
        mct "I'll have to improvise a bit here..."
        show ec 105
        bae "How do you know about Sapphire?!"
        bae "They join and pay voluntarily! No one is being forced into anything!"
        bae "EVERYTHING IS LEGAL!" with hpunch
        show ec 106
        mc "Then you won't mind if I explain what you do to the Praetorians."
        show ec 105
        bae "No!!!" with hpunch
        bae "I need the money! To... help the people!"
        bae "Please don't say anything!"
        show ec 106
        mc "I don't know..."
        show ec 105
        bae "I'll pay you!"
        bae "I have 100 eternals right here! They're yours!"
        show ec 106
        menu:
            with dis
            "Deal":
                mc "I'd make that deal."with dissolve 
                show ec 105
                bae "O-Of course! Take them!"
                bae "Just promise me you won't say anything!"
                show screen eternals
                show ec 106
                with dis08 
                play sound coins
                $ money += 33
                pause .05
                $ money += 34
                pause .05
                $ money += 33
                pause .2
                hide screen eternals
                mc "Not if you don't give me reasons to."with dis06        
            "[gr]I want more":
                mc "I know you have more." with dissolve
                show ec 105
                bae "I..."
                bae "O-Okay, 120 eternals! That’s all I have! The rest is frozen in the Garrington bank, I swear!"
                bae "Just promise me you won't say anything!"
                show screen eternals
                show ec 106
                with dis08 
                play sound coins
                $ money += 40
                pause .05
                $ money += 40
                pause .05
                $ money += 40
                pause .2
                hide screen eternals
                mc "Not if you don't give me reasons to."with dis06
            "I don't want your money":
                mc "I don't want your dirty money." with dissolve
                mc "I won't say anything if you don't give me reasons to."
        show ec 105
        bae "I won't! But don't mention Sapphire to anyone!"         
        show ec 106
        mc "Alright..."
        mc "You better not be the murderer or I'll spill the beans about Sapphire."
        mct "I wonder what she's doing there..."
        mct "Nothing legal, that's for sure."
        scene ec 4c
        hide screen heart
        with dis15
        call screen crimemap4 with dis04     
    if eround == 3:
        scene ec 80 
        with dis
        bae "Stay away from me." with dissolve
        bae "I can't trust anyone."
        scene ec 4c
        hide screen heart
        with dis15
        call screen crimemap4 with dis04
    if crimebae2:
        show screen heart
        scene ec 81
        with dis
        $ crimebae2 = False
        mc "Taking a stroll?" with dissolve
        show ec 80
        bae "I needed some fresh air after what happened."
        bae "And it feels good to finally get away from that psychologist's pungent perfume."
        show ec 81
        mc "So... any leads about who the murderer is?"
        show ec 80
        bae "I'll admit that I voted for Elliot, but... I had my suspicions about someone else since the beginning."
        bae "Blind, paralytic, old, and super polite. Come on... they must think we're stupid."
        show ec 81
        mc "Are you suspicious of Gemini?"
        show ec 80
        bae "I mean, how the hell can he even move around the house if he's blind?"
        bae "Am I supposed to believe he's like a bat and has echolocation too?"
        bae "Trust me, if you wanna win this game, vote for him."
        show ec 81
        mc "I'll... keep it in mind."
        mc "I need to go back inside."
        show ec 80
        bae "Sure... see you later."
        scene ec 4c 
        hide screen heart
        with dis14
        call screen crimemap4 with dis04
    mct "She seems to have made a decision already." with dis06
    call screen crimemap4 with dis04
label crime5:
    scene ec 5 with dis15
    call screen crimemap5 with dis04
label crime5room:
    if crimegemage and crimeharage and eround == 2:
        show screen heart
        mct "Fuck, I wasted too much time... I need to go to vote or I'll be eliminated for not showing up."with dis08
        mct "I'll come back here later... in case the game doesn't end after this next vote."
        scene ec 7 with dis17
        cl "Ah, hello, Mr. [mc]!"with dissolve 
        cl "It is time to vote!"
        mc "Okay... let's do this."
        jump crimeclonkresultsround2
    if crimedoor1:
        show screen heart
        $ crimedoor1 = False
        play sound2 doorlocked volume 1.2
        play sound doorlocked volume 1.2
        scene ec 15 
        with dis17
        no "*Trying to force the door* Hmmm... dammit, this door is locked."with dis08
        no "Why? The rest of the doors seem to be open."
        mct "Good gracious..."
        show ec 16
        mct "I didn't realize how good Nova's butt looks in those pants until now." with Dissolve(1.3)
        mct "The latex sticks to her like a second skin. I need to write a thank you letter to that fashion designer."
        if novapath and novadildo:
            mct "Now I'm getting flashbacks of that night at the college party..."    
        elif novapath:
            mct "Now I'm getting flashbacks of that night on the Egyptian server again..."    
        if novapath:
            mct "That was crazy..."
        show ec 17
        no "*Turning around* Impossible. It won't open without a key." with dis12
        show ec 18
        menu:
            with dis
            "Try again":
                mc "You sure? I think it's worth trying it again." with dissolve 
                play sound2 doorlocked volume 1.2
                play sound doorlocked volume 1.2
                scene ec 15 with dis12
                no "*Grunting* GGGgghh..."with dis
                no "AGH! Impossible."
                stop sound fadeout 1
                stop sound2 fadeout 1
                show ec 17
                no "Nope, it won't move an inch." with dis
                no "This is a good lock."
                show ec 18
                mc "Too bad..."
                show ec 17
                no "I guess they locked it for a reason."
                show ec 18
            "Look elsewhere":
                mc "Well, I guess they locked it for a reason."with dissolve
        mc "And that's exactly why we have to get it open."
        mc "Let's keep looking, maybe we’ll find a way to get in somewhere."
        scene ec 5
        hide screen heart
        with dis15
        call screen crimemap5 with dis04
    if not crimedoor1 and not crimekey:
        mc "That door won't open without the key..."with dis06
        call screen crimemap5 with dis04
    elif crimekey:
        if crimekeyfirst2:
            play sound2 key
            pause .65
        play sound dooropen2
        if crimekeyfirst2:
            show screen heart
            scene ec 6 
            with dis14
            $ crimekeyfirst2 = False
            mc "Yes!"with dissolve 
            no "Making strides!"
            mc "Okay, we don't have much time, so let's see what we can find."
            a "I'll go check out the room at the end!"
            no "I'll take the entrance!"
            scene ec 55
            mc "Alright, I'll see what I can find here, then..." with dis12
            scene ec 56
            mc "A briefcase..." with dis12
            mc "Looks like it's got a combination lock of 4 numbers."
            play sound chair1
            show ec 57
            mc "*Sitting down* (And what's on this sticky note?)"with dis
            mct "{i}A picturesque group of 6 gathered tonight,"
            mct "{i}Each one's age is hidden from my sight."
            mct "{i}The oldest and the youngest I seek,"
            mct "{i}Multiply their years, don't be meek."
            show ec 58
            mct "Now riddles?"with dis04
            mct "This man is playing with us even after death. He wanted someone to enter this room... and definitely wanted us to open this briefcase."
            show ec 57
            mct "Looks like it's telling me that the combination of the briefcase is the resulting number of multiplying the ages of the oldest and the youngest ones of the group."with dis04
            show ec 58
            mct "Which have to be Gemini and... Nova? Or perhaps Harley Jones?"with dis04
            show ec 57
            mct "I'll have to ask them."with dis04
            play sound chair2
            show ec 56
            mc "Alright girls! This is promising!"with dis 
            mc "The name of the person who killed Mr. Gideon could be inside this briefcase! This has to be the key to win the game!"
            mc "We're almost there!"
            show ec 59
            mc "We just need to know the ages of Gemini and Harley Jones."with dis12
            no "What for?"
            mc "There's some kind of riddle that says in order to open the case, I have to multiply the ages of the youngest and oldest of the group."
            no "Am I younger than Harley Jones?"
            mc "That's what we'll have to find out."
            no "Oh... alright!"
            mc "What do you have there, by the way?"
            show ec 59b
            no "Oh, just something I found on that cabinet over there."with dis08
            show ec 59
            mc "I wouldn't touch anything, just in case. We don't know what these artifacts could–"with dis08
            play sound glitch4
            scene novadup1
            pause 0.1 
            stop sound
            pause .4
            mc "What..." with dis08
            no "Huh? Is anything wrong?" 
            mc "For a moment I thought I saw..."
            play sound glitch4
            scene novadup1
            pause 0.1 
            stop sound
            pause .6
            play sound glitch4
            scene novadup2
            pause .75
            mc "What the heck..." with dis12
            no2 "Hmm?" (multiple=2)
            no1 "Huh?" (multiple=2)
            scene ec 61
            no2 "Huh?" (multiple=2)
            no1 "Hmm?" (multiple=2)with dis06
            play soundlow slam3
            scene ec 62
            no2 "WOOOOW!" (multiple=2)
            no1 "AAAAAAARGH!!!!" (multiple=2)with hpunch  
            no1 "Oh my god, there's another Nova!"with hpunch
            no2 "No way! Did the artifact do this?"
            no1 "T-This is horrible!"
            no2 "This is sooo cool!"
            no1 "A nightmare!"
            no2 "A fantasy!"
            mc "Holy shit, this is... certainly incredible."
            mc "Who's the real Nova?"
            scene ec 63
            no2 "I am!" (multiple=2)
            no1 "M-Me!" (multiple=2)with dis06
            scene ec 64
            no2 "I mean... she's Nova too." (multiple=2)
            no1 "W-Well, we both are... somehow." (multiple=2)with dis06
            scene ec 63
            no2 "But I'm more authentic." (multiple=2)
            no1 "B-But I'm real...er!" (multiple=2)with dis06
            mc "So... there are two Novas now?"
            scene ec 65
            no1 "It's not like... I mean... we're the same person, but... disconnected in a way." with dis08
            show ec 66
            mc "Same person...?"
            mc "Do you know what the other is thinking?"
            show ec 65
            no1 "Yes! Well, I mean... n-not exactly. That body and this one may be separated, but I'm the same person! We have one mind!"
            show ec 66
            mc "Okay..."
            show ec 65
            no1 "I know it sounds weird, but... I can feel {i}everything{/i} that the other body is feeling. I'm standing right there, b-but at the same time... I'm also here."
            no1 "I-I don't know how to explain it!"
            show ec 67
            no2 "One person, two bodies!" with dis
            no2 "It's not so hard!"
            show ec 68
            no1 "When we talk it's like... speaking to yourself. I know what she's thinking and saying, because... I'm also the one saying it."
            show ec 67
            no2 "All I know is that I've never felt better! I feel confident and revitalized!"
            show ec 68
            no1 "This is not good... we have to revert it..."
            show ec 67
            no2 "Later! First we have to solve this mystery murder!"
            show ec 68
            no1 "But we have to find a way to go back to normal..."
            show ec 67
            no2 "Okay, okay, let's just go see the other guests first! I want to rub Gemini's bald head!"
            no2 "Oh, and let's shoot something in the garden!"
            no2 "*Giggles* I saw some big-ass guns we could use..."
            show ec 68b
            no2 "Let's go!" (multiple=2)
            no1 "W-What did you say?!" (multiple=2)with dis 
            no1 "Please, don't!"with hpunch
            no1 "Oh my god, this is so embarrassing, please come back!"
            play sound run
            show ec 69
            bla "Both Novas rush out of the room." with dis12
            mct "Shit, this is getting out of hand..."
            mct "But I can't go after them, I have to stick to the quest of discovering who this murderer is, otherwise we’re gonna lose the game and all get killed..."
            mc "Um... Annie? We have a problem."
            a "Wow, come here, [mc]!"
            show ec 70 with dis14
            mc "We have two problems, actually. Both ginger."with dis08
            a "Look at this box!"
            mc "What box?"
            a "Exactly! It's invisible!"
            a "But I can feel it. It's right here in my hands!"
            play sound openbox2
            show ec 71
            a "*Opening the box* I wonder what's inside..." with dis08
            play sound spell2
            show ec 72 with dis08
            pause 
            mc ". . ."with dis08
            play soundlow dodge
            play sound2 ["<silence 0.5>", leaves]
            show ec 73
            a "AAAARGH, I'M INVISIBLE!" with hpunch
            mc "CAN YOU TWO STOP TOUCHING THINGS?!"with hpunch
            a "What am I gonna do now?!"
            mc "I-I don't know, maybe close the box again?"
            show ec 72
            a "Erm... I accidentally threw it out the window when I got startled..." with dis
            mc "You have to be kidding me..."
            a "Oh shit, what will happen if I can't find it?!"
            a "Will I remain invisible forever?!"
            if donedivination:
                mc "Hmm, I once met a professor on the Warthogs server that was always invisible because of some kind of malfunction."
                mc "She called it a “Chronic Illness” of Eternum."
                show ec 74
                a "Oh, thanks for the reassurance, [mc]! I feel much, much better now!"with dis08
                a "You sure know how to put a girl’s mind at ease!"
                a "Now I can..."
                a "A-Are you looking at my boobs??"
                mc "W-What? No!"
                a "I'm invisible but I can still see you, you know?!"
                mc "Um..."
                mc "Well, first of all, it's harder to look at your face when you don't exactly have one."
                mc "And... to be fair, that shirt of yours makes your breasts look... really good."
                mc "You look so hot."
                if anniepath:
                    $ annie_points += 1
                    show screen heartbeat
                    play sound beat
                    show ec 75
                    a "*Giggles* Really? T-Thank you!" with dis
                    a "I'm glad that you like it."
                else:
                    show ec 72
                    a "Can you focus and stop being a pig?!"with dis 
                    mc "Y-Yeah, sorry. I'm focused."
                    mc "What's the plan?"
            else:
                mc "Um... I'm no expert, but... I doubt it."
            show ec 74
            a "*Clears throat* Okay! I've got this under control!" with dis
            a "I'll go find the box and return to normal!"
            a "In the meantime, you'll discover who the murderer is so we can leave this place before something else crazy happens!"
            mc "Alright, I'll try."
            mc "Oh, and if you find Nova... try to help her reverse the spell too."
            mc "She touched some weird artifact and now there are two copies of herself... or something like that."
            show ec 72
            a "Oh, wow! That sounds awesome!"with dis08
            a "Okay, I'll help her too and then we'll solve this mystery together!"
            mc "Just don't touch anything else!"
            a "These grabbers, no more touchies! Pinky promise!"
            scene ec 55 with dis15
            mc "*Sighs* (Okay, I need to focus... I'm running out of time.)" with dis06
            mct "The briefcase. A combination of 4 numbers... the multiplication of the youngest and the oldest guest ages..."
            mct "Got it."
            $ crimegirlsartifacts = True
            hide screen heart
            call screen crimemap6 with dissolve 
        scene ec 55 
        with dis14
        call screen crimemap6 with dis04
label crimebriefcase:
    if crimegemage and crimeharage:
        if eround == 4:
            mct "Fuck, I have no time for this now, I have to discover who's the fucking impostor..."with dis08
            call screen crimemap6 with dissolve
        show screen heart
        mct "Okay... how was that riddle..."with dis08
        if novapath and not novacrimelewd:
            $ novacrimelewd = True
            stop music2
            play sound punch
            play sound2 fall
            play sound3 fall2
            show ec 115b 
            bla "Someone pushes you and you fall to the floor."with dis08
            mc "Aghh... what the hell?" 
            play music2b crime1 fadein 5
            play sound4 clothes3
            play sound5 wood fadein 1
            show ec 116
            mc "*Turning around* What the fuck is wrong with..." with dis15
            mc "You..."
            mc "Oh wow..."
            scene ec 117
            no2 "Hi, [mc]."
            show ec 116
            mc "Hi Nova..."
            mc "D-Did something happen? Are you back to being just one Nova again?"
            show ec 117
            no2 "Does that matter?"
            no2 "We're both the same person, remember? One mind, two bodies."
            no2 "You can feel and control both of your hands at the same time, can't you?"
            no2 "It's the same concept."
            show ec 116
            mc "It's still hard to understand, but I guess that example makes it simpler."
            mc "So... what happened to your outfit?"
            show ec 117
            no2 "Nothing. I just thought you'd like to see me without it."
            show ec 116
            mc "Well, you're not wrong..."
            play sound4 clothes3
            play sound5 wood fadein 1
            show ec 118 with dis15
            no2 "*Straddling you* I thought we could use some time to breathe in the middle of all this chaos."with dis08
            mc "That makes sense..."
            play sound clothes4
            show ec 119
            bla "Nova sensually pulls her bra over her head."with dis15
            mc "Wow..."
            scene 06novatease1 with dis2
            bla "Nova eagerly starts bouncing against you, with her breath becoming rapid as she adds a deep, seductive grind against your groin. Feeling your sudden erection only adds fuel to her fire as she hungrily rubs against it."with dis
            no2 "*Giggles* Wow, that was a fast reaction..."
            mc "Oh my god..."
            no2 "So... how long did Clonk say the rounds last? 10 minutes?"
            mc "I-I think so, yeah..."
            no2 "Do you have any idea of things that we could do in such a short time?"
            mc "Do you...?"
            no2 "Well... I think I could be quite a naughty girl for you. One who could ride you until you’re completely spent."
            mc "I-I see."
            no2 "Although... I doubt 10 minutes would be enough to satisfy my hunger for you."
            no2 "I have way too much pent-up energy. We'd probably have to continue well into the next round..."
            mc "I could roll with that..."
            no2 "*Giggles* I can feel you poking me through your pants, [mc]."
            no2 "Feeling your hard cock wedged up against me is making me feel so hot."
            mc "Yeah... I can't help it."
            scene 06novatease2 with dis2
            no2 "I'm dying to feel you inside of me..."with dis 
            no2 "I want you to fill me up completely... and let me feel you from every angle."
            no2 "I need to enjoy you from every single position."
            no2 "I’m dying to feel every pulse... every contour... every inch of your beautiful cock..."
            mc "Oh god Nova..."
            no2 "And you?"
            no2 "Can you give me what I want? Do you want to fulfill the hunger of your naughty little girl?"
            mc "Fuck, I do..."
            no2 "It's too bad we can't..."
            mc "W-What? Why not?"
            play sound dooropenclose
            play sound2 slam
            stop music2b fadeout 3
            scene ec 120
            play music2 crime5 fadein 3
            play soundlow slam3
            no1 "S-S-S-STOP!!!" with hpunch 
            mct "O-Oh."
            mct "Shit, I almost forgot where I was for a second."
            play sound4 clothes3
            play sound5 wood fadein 1
            scene ec 121 with dis15
            no2 "Awwh... I guess the party pooper has arrived." with dis08
            show ec 122
            no1 "W-What the fuck are you doing?!"
            show ec 121
            no2 "We both know what I was doing... we have a single mind, remember?"
            show ec 122
            no1 "S-So you know I'd stop you!"
            show ec 121           
            no2 "I knew you were coming, yeah... but I'll admit I'm surprised at how fast you managed to untie yourself."
            show ec 122
            no1 "T-This is so embarrassing!"
            show ec 121
            no2 "Come on, you can’t lie to me..."
            no2 "You are every bit as horny as I am."
            show ec 122
            no1 "N-No, I’m not!"
            show ec 121
            no2 "Pleaaaase... look me in the eyes and tell me you don't want to suck his huge cock again..."
            no2 "Because I know I want to... soooo bad..."
            show ec 122
            no1 "C-Can you shut up and get dressed, please?!"with hpunch 
            play sound clothes4
            show ec 123
            no2 "*Putting her bra back on* Okay, okay... jeez." with dis12
            no2 "With this attitude of yours we're never gonna be able to pop the “v-champagne”, y'know?"
            play sound2 clothes3
            show ec 124
            no1 "I-I'm sorry, [mc]." with dis12
            no1 "I don't know what happened to m... w-what happened to her."
            no1 "I mean..."
            no1 "I'm sorry, I d-didn't want this to happen."
            show ec 125
            no2 "HAH!"with dissolve
            no2 "You just can't stop lying, can you?!"
            no2 "You wanted this as much as me, girl!"
            show ec 126
            no2 "Like, why did we buy these  pants, if not to catch [mc]’s attention?" with dis
            no2 "We {i}literally{/i} bought them with him in mind because they accentuate our butt so wonderfully."
            play soundlow latex
            show ec 127 
            no2 "*Pulling her latex leggings up* See?" with dis 
            no2 "Don't you like them, [mc]? I've been doing some squats the last few weeks."
            mc "Very much, yes..."
            play sound punch
            show ec 128
            no1 "O-Okay, t-that's enough!" with hpunch
            no1 "S-S-Sorry for bothering you, [mc]!"
            mc "You don't bo–"
            no1 "W-We'll keep trying to find a way to get back to normal!"with hpunch 
            no1 "S-S-See you l-later!"
            mc "A-Alright! Be careful!"
            play sound doorold
            scene ec 55 
            with dis15
            mct "Damn, these artifacts sure are something else..."with dis 
            mct "Phew."
            mct "But anyway, I need to refocus and get the blood flowing back to my brain. You can do it, [mc]."
            mct "Now where was I..."
            hide screen heart
            call screen crimemap6 with dis06
        mc "“The oldest and the youngest I seek, multiply their years, don't be meek”..."
        mct "And, unless someone lied to me, Gemini is 71 years old and Nova is 21."
        mct "I hope that's the answer..."
        play sound chair1
        menu:
            with dissolve
            mod "Would you like to see the password?"
            "Yes":
                mod "1491"
            "No":
                pass
        scene ec 129
        with dis12
        play sound2 briefcase
        call screen combination_lock(1491) with dis
        show ec 129b
        mct "It worked!" with dis08 
        mct "Time to find out if the answer is inside this briefcase or not."
        play sound swallow
        show ec 129
        mc "*Gulps* (The moment of truth.)"with Dissolve(.7) 
        play sound3 briefcase volume 1.2
        play sound6 briefcase2
        play sound2 divine2 fadein 1
        stop music2 fadeout 4
        scene ec 130 with dis2
        pause 0.2
        mc "No way...{w=3.5}{nw}" with dis
        play sound5 pop
        stop sound2
        play music2 crime5 fadein 3
        show ec 130b
        mct "Another sticky note...?"
        mct "Really? That's it?"
        play sound briefcase
        play sound4 briefcase2
        show ec 57
        mct "With... another riddle on it..."with dis12
        mct "{i}In the realm of secrets and disguise, everyone holds a hidden lie."
        mct "{i}Delilah's true identity she hides with care, Gemini's eyes see more than he dares to declare."
        mct "{i}Harley trembles at the slightest sound, while Anna wears a mask to conceal her tears unbound."
        mct "{i}And don't ask Sister about Sapphire, or her trickery will ultimately expire!"
        mct "Hmmm... okay... and what does all this mean?"
        play sound chair2
        show ec 132
        mc "*Standing up* (Dammit, I feel like I'm wasting my time.)"with dis
        mct "I have to go back to–"
        play soundlow slam3
        a "[mc]!!" with hpunch
        mc "AHH!"
        mc "A-Annie?"
        mc "Where are you?"
        a "Right in front of you! I'm still invisible!"
        mc "Oh!"
        mc "Wait, so... you're naked?"
        a "U-Um... well, I took off my clothes to be able to investigate without being seen."
        mc "Ohh..."
        mc "Sexy..."
        a "[mc]!"
        mc "*Chuckles* Well, and what did you find?"
        a "Polyjuice potion!"
        a "I found remains of it in the bathroom!"
        a "And I know who's using it!"
        play sound3 bottle volume 0.7
        show ec 133
        a "Take this bottle!"with dis08
        a "And open it when you're next to Anna Piaget!"
        mc "The psychologist? Why?"
        a "Trust me!"
        play sound2 bottle volume 0.7
        show ec 132
        mc "*Grabbing the bottle* Well, alright."with dis08
        a "What about you? Did you discover anything?"
        play sound paper2
        show ec 132b 
        mc "*Giving the note to Annie* Just this weird riddle."with dis08
        a "*Reading it* Delilah's true identity... wears a mask... ultimately expire..."
        a "*Gasps* OF COURSE!" 
        a "It has to be that!"
        mc "What is it?"
        play sound2 paper2 
        show ec 132
        a "Everybody is lying about something! You have to discover what each one of them is hiding!"with dis08
        mc "But how? And what about you?"
        a "Just keep playing the game! And follow the clues of the sticky note!"
        a "Just... buy me some time, please! I'll be back!"
        menu:
            with dis
            "[gr]Trust her and let her investigate":
                $ crimeannietrust = True
                mc "*Sighs* Alright, I trust you."with dissolve 
                mc "But be careful!"
                a "I will!"
            "Ask her to turn back to normal":
                mc "This is too dangerous, Annie."with dissolve
                mc "Find that box to become visible again and let's stay together!"
                a "B-But!"
                a "Agh, darn it, you're right!"with vpunch
                a "Okay, I'll go to the garden to find the box. I'll join you as soon as I'm back to normal!"
                mc "Sounds good!"
        play sound3 run
        bla "You hear Annie running away."
        mc "Hmm..."
        mct "Well, I'm not sure of what exactly I have to do, but... I'll try."
        mct "Everyone is lying about something, but only one person is the real murderer."
        mct "One of them had to know The Collector before coming here... and I have to discover WHO."
        $ lastpostit = True
        scene ec 55 
        hide screen heart
        with dis15
    else:
        if geminialive:
            mct "I'll have to talk to Gemini and Harley..." with dissolve 
        else:
            mct "Fuck... I didn't ask Gemini his age and now he's dead..."with dissolve 
            mct "I guess this means one less lead to follow..."
    call screen crimemap6 with dissolve 

label poscrimescene:
    stop soundloop fadeout 3
    play soundloop2 night fadein 5
    stop music2 fadeout 6
    play sound ["<silence 2.2>", metalgate]
    scene ep 57 with Dissolve(3)
    mc "*Taking a deep breath* Holy shit..."with dis 
    mc "I still can't believe we managed to get out of there alive."
    scene ec 189
    a "Yeah, that was close..."with dis12
    if crimesuccess:
        show ec 190
        mc "Hey, we solved the case thanks to you!"with dissolve 
        no "Hell yeah, that deduction was amazing, Annie! You're so awesome!"
        if anniepath:
            $ annie_points += 1
            play sound beat
            show screen heartbeat
        show ec 191
        a "We survived through the rounds thanks to you two as well, but... t-thanks, guys! Means a lot!"with dis08
        show ec 192
        mc "I don't even know how long we've been playing, it felt like hours."with dissolve 
        show ec 191
        a "Yep, we're probably way past bedtime."with dissolve 
        if anniepath:
            a "But I'm gonna go grab a glass of milk and some chocolate cookies from the kitchen before going to bed, you want some?"
            show ec 192
            mc "Sure, that sounds good! I'm starving."with dissolve 
            show ec 191
            a "Cool! I'll log off then."with dissolve 
        a "This was scary but also very fun."
        a "I always feel very accomplished after playing with you guys!"
        show ec 192
        no "I feel the same way!"with dissolve 
        show ec 191
        a "Anyways, I'll see you tomorrow!"with dissolve  
        show ec 192    
    else:
        show ec 190
        mc "I still think there was something that doesn't add up there..."with dissolve 
        no "Why do you think so?"
        mc "I mean, why would a man who's about to die organize this whole madness?"
        mc "Mmh, I don't know, maybe I'm just underestimating how weird people can be."
        show ec 189
        a "Well in any case, I think I'm gonna go grab a glass of milk and some chocolate cookies and go to bed."with dissolve
        a "I'm exhausted."
        if anniepath:
            show ec 190
            mc "Oh, can you grab some for me too? I'm hungry."with dissolve 
            show ec 191
            a "Of course! On it."with dis08 
            a "This was scary but very fun, guys."
            a "See you tomorrow!"
            show ec 192
        else:
            a "Good night, guys."
            show ec 190
    no "Good night, Annie!" with dissolve   
    show ec 196 with dis 
    play sound spell4
    bla "Annie uses the Exit Portal and returns to the real world." with flashfaster
    mc "Oh shit, are you okay, Nova?"
    mc "How's your eye?"
    show ec 195
    no "It's fine! No worries!"with dissolve
    no "I might have overextended it a bit, but you know how it works. I'll be as good as new as soon as I log off."
    show ec 196
    mc "Oh well, I'm glad to hear that."with dissolve
    show ec 195
    no "Thank you for helping us, [mc]."with dissolve
    no "We wouldn't have made it out here alive if it wasn't for you."
    show ec 196
    mc "Meh, all I did was point out people’s bullshit in a bizarre game."with dissolve
    show ec 195
    no "*Chuckles* Fair enough."with dissolve
    if novapath and novacrimelewd:
        show ec 194
        no "Um... listen, I wanted to apologize for my behavior earlier." with dis
        no "When I was duplicated a part of me felt... crazier for some reason."
        no "I said things I didn't want to say. I m-mean... things that weren't true."
        show ec 193
        mc "You have nothing to apologize for."with dissolve 
        show ec 194
        no "S-Still, I feel like I have to."with dissolve 
        no "So... let me make it up to you!"
    elif novapath:
        show ec 194
        no "Oh, and... listen, I wanted to ask you something before we log out." with dis
    if novapath:
        no "The last episode of One Piece comes out next Saturday, and I was wondering if you wanted to... watch it with me."
        no "Like... at my house."
        no "I mean... I know you follow it too, so why watch it alone when you can have some good company!"
        no "Plus, and here’s the best part... I’ll  bring food and drinks!"
        show ec 193
        mc "Psh, you had me at “good company”! That sounds awesome!"with dissolve
        mc "I've been looking forward to watching it."
        mc "*Chuckles* And after the bad impression I left at your house the first time I was there, I feel like I deserve a second chance."
        mc "Count me in."
        show ec 195
        no "A-Alright! Sounds good!"with dis08
        no "I-I'll start preparing for it then!"
        show ec 196
        mc "Preparing...? There's still a week left."with dissolve
        show ec 195
        no "Y-Yeah, well, you know, I gotta do some stuff... and then the things need the thingys... otherwise those uhh... umm..."with dissolve
        no "A-Anyways! It’s getting late! This was super fun, but I'm very tired and think I'll go to bed as well!"
        no "So... yeah, night-night!"
        show ec 196
        mc "*Chuckles* Okay Nova, good night!"with dissolve
    else:
        no "Well, I'm calling it a day as well."
        no "See you tomorrow!"
        show ec 196
        mc "Take care, Nova! Good night!"with dissolve
    play sound spell4
    scene ep 57 with dis2
    if novapath:
        mct "I wonder if she's inviting more people or if it’ll be just the two of us." with dis
        mct "I guess I'll find out next Saturday..."
        mct "But anyway, it's my turn to leave."
    else:
        mct "Well, it's my turn to leave."with dis 
    mct "Another crazy chapter for my Eternum memoirs."
    mct "I won't miss the deadly lasers though, that's for sure..."
    if crime50eternals:
        $ crimesuccess = False
    stop soundloop2 fadeout 4
    play sound risingshort4
    scene login3 with dis2
    pause 6
    play soundlow whoosh4
    scene white with dissolve
    play soundloop rain3 fadein 5
    scene ep 21 with flash
    pause
    play sound7 clothes
    mc "*Stretching* (Mmmm... still raining.)" with dis08
    play sound4 clothes3
    play soundlow chair2
    scene eaa 1
    mc "*Sitting up* (Wow, as soon as you log off Eternum all the exhaustion suddenly hits you like a ton of bricks.)" with dis
    mct "It's easy to forget how fatigued you really are when you're in there."
    if anniepath:
        mct "But tired or not, Annie mentioned milk and cookies, and I'm not one to say no to that!"
    else:
        play sound clothes3
        play sound2 chair2
        scene ep 21
        mc "*Lying down* (Now it's time to sleep for real.)" with dis12       
        mct "Big day tomorrow. I have to visit Alex's house and then follow another lead on a hypothetical Gem of Doom on that Western server."
        mc "*Yawns* (I hope things go more smoothly there than tonight.)"
        mc ". . ."
        mct "But somehow I..."
        mc "*Yawns* (I highly doubt it...)"
        jump nextday06
    scene eaa 5 with dis2
    play sound thunder fadein 3
    mct "Holy shit, what a storm." with dis08
    mct "At least Kredon is used to it by now and it rarely gets flooded."
    play sound2 knock2
    play sound3 knock2
    mc "*Knocking on the door* Annie?"
    a "Come on in!"
    play sound2 dooropen1
    scene eaa 6 with dis12
    play music2 anniesong fadein 3
    stop soundloop fadeout 20
    play sound3 ["<silence 0.4>", doorclose]
    mc "*Closing the door* Ah, I was wondering when you'd turn this room into plushie paradise too."with dis08
    show eaa 7
    a "*Chuckles* I just bought a couple of them! I'm still far from the 37 I have in my room in London."
    show eaa 6
    mc "A couple? I expected more from you, these are rookie numbers!"
    mc "I'll have to buy you a new one or three for Christmas."
    show eaa 7
    a "*Giggles* Deal!"
    show eaa 6
    mc "Well..."
    mc "I was promised cookies, but I don't see them anywhere."
    show eaa 7
    a "Yeah, about that..."
    a "I went to the kitchen, but there were no chocolate chip cookies left."
    show eaa 6
    mc "Oh..."
    show eaa 8
    a "But there were Oreos."with dis08
    show eaa 9
    mc "Oh!"
    mc "I can settle for that!"
    play sound2 chair1
    show eaa 10 with dis12
    mc "*Jumping on Annie's bed* Did you see the girls on your way to the kitchen? Are they still awake?"with dis06
    show eaa 11
    a "All three of them are sprawled out on the couch. They fell asleep watching one of their TV shows."
    play sound eat
    show eaa 10
    mc "*Eating an Oreo* That's cute."
    mct "They were all peacefully sleeping without knowing how close I was to losing our two Gems of Doom..."
    mct "Thank god it all ended well."
    mc "I love your hair, by the way!"
    show eaa 12
    a "This? Oh, please, it's just a quick and messy bun I threw up after I got home." with dis08
    show eaa 11
    a "B-But thank you."with dis08
    a "It's cool to have longer hair. I wouldn't have been able to make a top knot like this when my hair was shorter."
    a "Penelope has been teaching me different ways to style it too."
    show eaa 10
    mc "Mind giving me a sneak peek of how it looks without the bun?"
    show eaa 11
    a "Not yet! I want to impress you when it's a liiitle bit longer."
    show eaa 10
    mc "I've seen you with long hair in Eternum already!"
    show eaa 11
    a "Yeah, but this is different!"
    a "It's crazy how fast hair grows in Kredon."
    play sound eat
    show eaa 10
    mc "*Eating another cookie* Mm-yeah, people mentioned how much my hair had grown during my visit too."
    show eaa 11
    a "So everything went well when you returned home this past week, then?"
    show eaa 10
    mc "Meh, I wanted to return to Kredon the moment the flight took off."
    mc "I don't care if I find discounted plane tickets again, I have no reason to go back there."
    show eaa 11
    a "And how was your dad?"
    show eaa 10
    mc "My dad...?"
    $ renpy.music.set_volume(0.0, delay=4.0, channel='music2')
    $ renpy.music.set_volume(0.3, channel='soundloop')
    play soundloop footballcomment fadein 3
    show eaa 13 with dis25
    show screen daybeforecorner
    dad "Agh, why are we passing backward?!" with dis
    dad "Move the ball forward, you fucking wanker!" with hpunch
    mc "Um... hey Dad, I'm leaving."
    mc "Going back to Kredon. The plane leaves in 4 hours."
    show eaa 14
    dad "Ah, you leaving already? Kay, have fun!" with dis06
    dad "Study hard and all that jazz."
    show eaa 13
    mc "Sure." with dis06
    dad "Tell Na-"
    play soundlow burp
    dad "*Burps* Tell Nancy, Talia, and Persephone I said hi."with hpunch 
    mc "Their names are Dalia and Penelo–"
    show eaa 15
    dad "AGGHHH, for fuck's sake, how can you miss that, you bastard?! I didn’t know we had Stevie Wonder on the team!" with dis12
    mc ". . ."
    dad "And why is this grandpa still playing?! He's a fucking mummy!"
    dad "Just give Oliveira a chance, let the kid play!"
    mc ". . ."
    $ renpy.music.set_volume(0.5, delay=5.0, channel='music2')
    stop soundloop fadeout 4
    show eaa 16b with dis2
    mc "So... yeah, you know how my father is."with dis08
    show eaa 16
    a "Awh, I'm so sorry, [mc]..."
    a "I can’t imagine how that must’ve felt after traveling all that way."
    show eaa 16b
    mc "Don't be sorry!"
    hide screen daybeforecorner
    menu:
        with dis
        "My true family is here in Kredon [annie_pts]":
            mc "You, Nancy, Dalia, Penelope... everyone that matters to me most is here in Kredon." with dissolve 
            $ annie_points += 1
            show screen heartbeat
            play sound beat
            show eaa 11
            a "You know... that’s really sweet of you to say."with dissolve 
            a "Thank you."
        "I prefer not to talk about it":
            mc "I prefer not to talk about it." with dissolve
            show eaa 16
            a "O-Of course!"
            a "I didn't mean to pry, I'm sorry."
            show eaa 16b
            mc "No worries!"
        "You know dads can be real assholes":
            mc "You know as well as I do that dads can be real assholes."with dissolve 
            show eaa 16
            a "W-Well... it's true that my dad has been working a lot all his life and he's been a bit absent, but... he's always cared about me."
            a "And he thinks highly of you!"
            show eaa 16b
            mc "Well... yeah, I guess that's different."
            mc "That came out wrong, I'm sorry."
            show eaa 11
            a "No worries! I know you didn't mean it in a bad way."
    show eaa 17
    mc "Anyway, changing the subject... how are your guitar lessons going?"with dis12
    show eaa 18
    a "Oh... well, I-I'm still learning."
    a "I'm still in the “butchering guitar chords” phase."
    $ renpy.music.set_volume(1.0, channel='soundloop')
    show eaa 19
    mc "I'm sure you're better than you say!"
    mc "Can't you play me anything?"
    show eaa 18
    a "N-Not yet! You'd hate it."
    show eaa 19
    mc "No, I wouldn't!"
    show eaa 18
    a "S-Still, not yet!"
    a "Give me a few weeks of practice."
    show eaa 19
    mc "*Laughs* Okay, okay, I'll wait..."
    play sound chair2
    show eaa 20
    a "*Standing up* Let's just eat these cookies instead!" with dis
    a "You want some milk?"
    mc "Sure!"
    show eaa 21
    a "I can't eat Oreos without dunking..."with dis08
    a "Huh?"
    show eaa 22
    a "Where's the milk?" with dis08
    a "I left it right here on the nightstand."
    mc "You mean those glasses on the floor?"
    show eaa 23
    a "What?" with dis08
    a "WHAT?!"
    a "What happened there? Where's the milk?!"
    play sound cat
    carol "*Meows*"
    show eaa 24
    bla "Carolyn appears from behind the bed and jumps on the covers, sporting traces of milk still on her whiskers." with dis12
    show eaa 25
    a "*Gasps* CAROLYN!" with hpunch 
    a "Did you drink our milk?!"
    play sound purr2
    show eaa 24
    carol "*Purrs*"
    show eaa 25
    a "No! Bad!"
    a "BAD KITTY!" with hpunch 
    a "You can't eat our snackies! BAD GIRL!"
    a "BAD, BAD..."
    stop music2 fadeout 2
    play sound puss volume 0.85 fadein 2
    scene pusscarolyn with dis2
    pause 5.8
    scene pusscarolyn2 
    a ". . .{w=6}{nw}"with dis17
    scene pusscarolyn 
    carol ". . .{w=6}{nw}"with dis17
    stop sound 
    play music2 anniesong 
    play sound pop
    scene eaa 27
    a "AWWWWW LOOK AT HOW CUTE THE LITTLE PRINCESS IS!"
    a "How could you ever be mad at such a stinkin’ cute little kitty face?!"
    a "Don't worry Carolyn, you can drink all the milk you want!"
    a "Good girl!"
    play sound cat
    carol "*Happily meows*"
    show eaa 29
    mc "So... what now? Should we go get more milk?"
    show eaa 28
    a "I think there's only one carton left, and that one is actually Carolyn's."
    scene eaa 29
    mc "Yeah, but well, it's normal milk, isn't it?"
    scene eaa 28
    a "Yeah, it is, it's not a special formula for cats or anything."
    scene eaa 29
    mc "We can get that one, then."
    mc "She drank some milk tonight already. It's not as if she's gonna die if tomorrow she doesn't have any..."
    show eaa 30
    mc ". . ."with dis08
    stop music2 fadeout 2
    play sound puss volume 0.85 fadein 2
    scene pusscarolyn3 with dis2
    mc "O-Okay, okay!{w=7}{nw}"with dis 
    mc "W-We won't drink your milk either, stop making that face!{w=7}{nw}"
    play sound2 chair1
    stop sound fadeout 4
    play soundloop rain3 fadein 2
    scene eaa 32 with dis14
    play soundlow thunder fadein 4
    a "Awhhh..." with dis
    a "If we don't have milk, I don't think I want any cookies..."
    a "Now my whole night is ruined."
    mc "*Laughs* Don't be so dramatic."
    mc "They're still good without milk."
    a "But it’s not the same..."
    play sound eat
    mc "*Eating your last cookie* Well, suit yourself. I think they're delicious either way!"
    mc "But anyway, I guess I should really go to sleep now."
    play sound2 clothes3
    show eaa 33
    a "What? Already?" with dis
    show eaa 35
    mc "Well, tomorrow I'm supposed to go meet Alex pretty early and play with her and Dalia in that Wild West server. Supposedly that’s where a Gem is hidden."
    show eaa 34
    a "Oh... y-yeah, the mission! Of course."
    a "I forgot."
    show eaa 35
    mc "I mean... I can stay if you want me to."
    show eaa 34
    a "No, no! I don't want you to."
    a "I mean... there's no need."
    show eaa 35
    mc "You sure? We c–"
    show eaa 34
    a "Absolutely sure! There's nothing else I need to discuss with you!"
    a "But I enjoyed hanging out at least! I'm glad you're back, and..."
    a "Yeah, it's bedtime!"
    a "Good night, [mc]!"
    show eaa 35
    mc "Um... well, okay then."
    mc "Good night, Annie!"
    play sound2 chair3
    show eaa 36
    mc "*Standing up* (Mmm, was it something I said?)"with dis12
    mct "We haven't really talked much since that time in Andromeda, I'm not sure where-"
    play sound whoosh6
    stop soundloop
    scene eaa37
    a "WAIT!" with hpunch 
    a "Umm... d-don't go!"
    scene eaa 38
    mc "Huh?"
    mc "What's the matter?"
    $ renpy.music.set_volume(0.35, channel='music3')
    play music3 sexyannie fadein 15
    show eaa 39
    a "*Clears throat* I mean, you can go... but before you do... I just thought that..."with dis 
    a "Well, I’ve had a lot of time to myself this past week and..."
    a "I’ve been thinking a lot... and feeling a lot of... umm, {i}feelings{/i}... eheh..."
    a "And I was wondering if we could possibly, by chance, maybe... c-continue our little {i}practice{/i} sessions?"
    show eaa 40
    mc "Practice... like with the guitar?"
    show eaa 39
    a "N-No. Not the guitar."
    a "I mean... remember last time in Andromeda? When you taught me... certain things? And made me feel... certain ways?"
    show eaa 40
    mc "How could I forget..."
    show eaa 39
    a "Well... I thought that... maybe... we’re a little overdue for some more... p-practice."
    a "Like... kissing, or... you know, k-kissing with some tongue too."
    show eaa 40
    mc "Ah... that kind of “practicing”..."
    show eaa 39
    a "Yeah, I mean..."
    a "What if Dalia suddenly kisses me one day? With my severe lack of practice, I'd only embarrass myself."
    show eaa 40
    mc "You want to kiss Dalia?"
    show eaa 41
    a "Y-You know what I mean!"with dis08
    show eaa 42
    mc "*Chuckles* I'm honestly not sure."
    show eaa 41
    a "D-Don't make fun of me!"
    show eaa 42
    mc "It's you who keeps going in circles, dancing around what you’re really getting at!"
    mc "Why don't you just tell me what you really want?"
    mc "Be direct."
    show eaa 43
    a "*Taking a deep breath* Hnnn..."with dis
    show eaa 44
    a "I..."with dissolve
    a "I want you to kiss me."
    show eaa 45
    mc "See? It wasn't so hard."
    mc "*Chuckles* Now come here, silly girl."
    show eaa 48
    bla "Annie gets closer to you. Her alluring blue eyes gaze deeply into yours, as she playfully begins swinging her petite hips." with dis15
    mct "Sometimes I forget how small Annie is."
    mct "She was wearing heels in that server the whole time, so I guess that also created the illusion of her being taller."
    show eaa 46
    mc "You need to be more direct, Annie." with dis
    show eaa 47
    a "I’m trying!"
    a "I-It's just that... I don't want to make things awkward or anything."
    show eaa 46
    mc "I've told you about a hundred times the way I feel about you."
    mc "There's no way you can make things uncomfortable between us."
    show eaa 47
    a "I-I know..."
    show eaa 46
    mct "I shouldn't be so afraid to make the first move either when it comes to Annie."
    mct "She's told me how she feels as well, after all."
    play sound clothes2
    play sound2 fall2
    show eaa 49 with dis 
    mc "*Picking her up* Alright, so... you told me you want to practice kissing again, is that correct?" with dis06
    show eaa 50
    a "Yes sir..."
    show eaa 49
    mc "And do you have any preference on who you practice with?"
    mc "I've heard Professor Keating is such a good kisser."
    show eaa 50
    a "*Giggles* I’ll have to take your word on that one. As for me, I only want it to be you."
    show eaa 49
    mc "Oh..."
    mc "Well, that makes things easier..."
    show eaa 51 with dis
    bla "You lean in, and your lips meet in a soft, tender kiss." with dis06
    a "Mmmm..."
    play sound chair1
    play sound4 clothes3
    play sound2 ["<silence 0.1>", plate]
    show eaa 52
    bla "Without your lips ever parting, you carry Annie towards her bed and both of you fall back onto the soft mattress."with dis
    play sound clothes3
    show eaa 53
    a "*Sitting up* I missed you so much. Being back in your embrace... it’s just what I needed."with dis12
    show eaa 54
    mc "Me too..."
    show eaa 53
    a "Do you mind if I... get a little more comfortable?"
    a "You should know... for some reason this outfit always feels a bit itchy against my skin."
    show eaa 54
    mc "Ah, yes, I remember..."
    mc "Maybe you should just stop wearing these pajamas altogether."
    show eaa 53
    a "*Giggles* Yeah, maybe I will start going to sleep naked."
    show eaa 54
    mc "That sounds like a really good idea..."
    show eaa 53
    a "But you know, if I do that, I get cold really easily... I’d need someone to keep me warm..."
    show eaa 54
    mct "I like seeing Annie growing in confidence, teasing and joking around."
    show eaa 55 with dis12
    pause
    play sound clothes4
    show eaa 56 with dis12
    mc "Oh boy..."with dis06
    play sound2 clothes2
    show eaa 57 with dis12
    mc "I’ll never get tired of seeing your gorgeous body, Annie." with dis08
    show eaa 58
    a "T-Thank you..."
    show eaa 57
    mc "Now, where were we...?"
    play soundlow chair1
    $ renpy.music.set_volume(0.6, channel='soundloop2')
    $ renpy.music.set_volume(0.27, delay=15.0, channel='music3')
    play soundloop2 kissing fadein 2
    scene annieb1 with dis2
    bla "Without answering your question, Annie eagerly pounces on you and resumes the kiss."with dis08
    a "Mmmmmhm..."
    mct "Her soft skin feels so warm... I can’t keep my hands from tracing her every outline."
    mct "She's so light, but at the same time I can feel all of her beautiful curves tightly hugging my body."
    mct "I can tell she wants this as much as me."
    bla "As time goes by, Annie summons more and more confidence and lustfully deepens the kiss."
    a "*Slight moan* Mmmm..."
    mct "Feeling her heart pounding is so intoxicating."
    mct "I just want to hold her tighter..."
    mct "I want her to feel how much I desire her..."
    a "Mmm..."
    stop soundloop2 fadeout 1
    play sound clothes3
    scene eaa 58
    a "*Breaking the kiss* I... "with dis12
    show eaa 57
    mc "All good?"
    show eaa 58
    a "I want..."
    a "I want to do that thing again."
    show eaa 57
    mc "That “thing”?"
    show eaa 58
    a "In Andromeda."
    a "I w-want you to... I need to feel your finger i-inside of me again."
    show eaa 57
    mc "Naughty girl..."
    play sound chair1
    show eaa 59
    bla "You grab Annie and throw her onto the bed." with dis12
    mc "We're gonna have to make ourselves even more comfortable for that."
    play sound clothes3
    play sound2 clothes4
    show eaa 60
    mc "*Taking your shirt off* You don't mind if I take this thing off, right?"with dis12
    a "Nuh-uh..."
    mc "Now... as much as I like those cute pajamas, I'm afraid we'll have to get rid of them."
    show eaa 62 
    bla "Annie looks at her pants and, after a moment's hesitation, slowly starts slipping them off."with dis12
    play sound clothes
    show eaa 63 with dis12
    pause .3
    show eaa 64 with dis14
    mc "Oh my..." with dis
    mc "No panties, eh?"
    mc "Were you expecting this to happen?"
    show eaa 65
    a "Perhaps..."
    show eaa 64
    mc "Fuck, I just want to explore every inch of you..."
    show eaa 66
    a "I... I'm n-not sure I'm ready, [mc]."
    show eaa 64
    mc "Ready for what?"
    show eaa 66
    a "You know what I mean..."
    a "Ready for... {i}sex."
    show eaa 64
    mc "Like I’ve told you before, we can take it as slow as you want. I’m only going to accept however much you’re willing to give."
    mc "I want you to feel safe. I just want to take you to a place where you can let go of your shyness, your inhibitions, and truly embrace your desires without reservation."
    mc "And until then... you set the pace."
    a ". . ."
    play sound clothes3
    show eaa 67 with dis14
    bla "As if you had pronounced some magic words, Annie's legs slowly open for you and you’re again blessed with a sight that no other man has seen before."with dis
    show eaa 68
    mc "Oh Annie..."with dis12
    mct "God... I just want to devour all of her."
    play sound clotheswhoosh
    play soundlow chair1
    scene eaa69
    mc "*Pulling Annie towards you* Come here..." with hpunch
    a "W-WHAT? Wait!"
    a "I said I'm not ready!"
    a "I just wanted the same thing we did in Andromeda!"
    mc "I know. We can do that... but maybe instead of a finger, we can try it with something else you were playing with earlier."
    mc "You'll see..."
    a "What?! Are you gonna use your mouth... your tongue... on my...?"
    mc "I’m dying to taste you, Annie."
    a "[mc], I... I-I'm not sure if I'm ready for that either!"
    a "W-What if you don’t like the way I taste? O-Or what if I feel strange or..."
    play soundlow clothes4
    show eaa 70 with dis14
    bla "You start sliding your tongue between Annie's outer lips." with dis
    a "[mc!u]!" with hpunch
    mc "There’s no way such a beautiful girl like you..."
    bla "Your tongue slowly starts grazing around her wet pussy."
    mc "Could taste anything other than amazing..."
    a "I'm..."
    show eaa 71
    a "Not..."with dis 
    a "Reaaaaddyyy..."
    a "Oh [mc]... that feels..."
    play soundlow chair1 volume 0.7
    show eaa 72
    a "Oh my GOD!" with dis08
    $ renpy.music.set_volume(0.19, delay=10.0, channel='music3')
    $ renpy.music.set_volume(0.8, channel='soundloop')
    play soundloop wetting5 fadein 2
    scene annieb2 with dis2
    a "MMmmmm..." with dis
    a "Oh god..."
    bla "You begin to taste every inch of Annie, spreading her tight lips as you gracefully move your tongue back and forth."
    mct "Maybe I should have started slower."
    a "*Moaning* Mmmm-aahh-mmm..."
    mct "Although she doesn't seem to mind..."
    a "Oh my god, [mc]..."
    mct "I fucking love her taste..."
    a "AAaahh... how are you doing that..."
    a "Y-Your tongue feels so... aaAaahhh..."
    mct "Maybe now I could try focusing on her clit."
    mct "Her thighs seem to keep pushing my mouth toward it..."
    mct "Here we go..."
    stop soundloop fadeout 1
    play sound clothes4
    play soundlow punch volume 0.4
    scene eaa 73
    a "AAAAGH! What's that!"with hpunch 
    a "*Grabbing your head* STOP!"
    mc "You don't like it?"
    a "NO! I mean... d-don’t stop..."
    play soundloop wetting4 fadein 2
    scene annieb3 with dis2
    a "[mc]. . . . . . . . . . .  . !"with dis
    bla "Annie's body language screams of ecstasy as you continue attacking her swollen clit."
    a "Oh godddddd..."
    a "Mmmmmm..."
    a "Oh yes. OH... FUCK YES!"
    a "Please don't stop!"
    a "Keep doing what you're doing... WHATEVER IT IS!"
    a "Eat me whole..."
    mct "Oh boy..."
    mct "It's so tempting to just give in and let my desires take over..."
    mct "But I have to resist the urge, for now. I know Annie better than herself, and I know she’s really close but not quite ready to go all the way."
    mct "This moment is about more than just my pleasure."
    mct "Although... I'm not sure how long I'll be able to hold out..."
    a "*Loudly moaning* AAAAaaaaGH... aaahhh..."
    mct "Thank god it's storming outside, otherwise it’d be nearly impossible to not hear her moans throughout the house..."
    a "AAaahh... oh god [mc]... I think I'm gonna... C-CUM..."
    a "Again..."
    a "[mc]! You’re gonna make me..."
    a "I can feel it coming..."
    a "Aaah..."
    a "AAAaahhh..."
    stop soundloop fadeout 1
    play sound clothes4
    play soundlow punch volume 0.4
    play sound cum3
    scene eaa 73
    a "AAAAARRRHHHGGHH..." with hpunch
    a "MY GOD!" with hpunch
    a "HEAVENS!"with hpunch 
    a "WHAT... WHAT WAS THAT?!"
    a "That was... soooo... amazing..."
    mc "*Muffled* Y-You're kind of crushing my skull with your thighs..."
    mct "How the hell are her legs so strong?!"
    play soundlow chair1
    play sound2 clothes4
    scene eaa 74 with dis15
    bla "You move aside and let Annie collapse on the bed after her orgasm."with dis
    a "Wow..."
    a "M-My legs are still shaking."
    a "I almost forgot where we were..."
    show eaa 75
    mc "*Sitting on the edge of the bed* See? You just have to trust me."
    show eaa 74
    a "I guess you're right..."
    play soundlow chair3 volume 0.4
    play sound clothes3
    show eaa 76 with dis15
    a "*Sitting up and crawling towards you* I guess from now on I should..."with dis06
    show eaa 77
    a ". . ." with dis08
    show eaa 78
    a "W-W-When did you lose your pants?!" with dis12
    show eaa 79
    mc "Shortly after I started going down on you..."
    mc "You didn't notice?"
    show eaa 78
    a "N-Not at all."
    show eaa 79
    mc "I guess you were too absent-minded..."
    show eaa 78
    a "I-It looks..."
    a "It looks as big as it was in Eternum."
    show eaa 79
    mc "I'd be surprised if something didn't look the same as in Eternum. We're literally an identical replica of ourselves in there."
    show eaa 78
    a "I know, I meant that..."
    a "It's {i}still{/i} big."
    show eaa 79
    mc "Do you want to... give me another handjob?"
    a ". . ."
    show eaa 78
    a "I mean... it’s only fair that..."
    a "Since you got to use your tongue, I should be able to use mine too..."
    show eaa 79
    mc "Fuck, I was hoping you'd say that so much..."
    show eaa 80
    bla "Annie slowly positions herself on your side and lightly touches your dick with the tip of her tongue." with dis15
    a "*Sniffs* Your scent is just so... alluring..."
    show eaa 81
    a "Aaahh..."with dis12
    mc "Yes..."
    scene annieb4 with dis2
    bla "Annie eagerly starts lapping up your shaft."with dis
    mc "Oh, fuck yes..."
    a "*Slight moan* Mmmm..."
    mc "Oh Annie..."
    a "It's so slippery..."
    a "And..."
    a "I can feel you pulsing, [mc]..."
    mc "Because I'm so fucking horny for you right now..."
    a "There's no way I can fit all of you inside of my mouth..."
    mc "You'd be surprised how much you can take..."
    a "Mmmmh..."
    a "Y-You’re just too thick."
    mc "Don't you wanna try it...?"
    mc "Please, just the tip..."
    mc "I’m dying to feel your lips wrapped around me..."
    a "Aaaahhh... that does sound... good..."
    a "I guess..."
    a "I guess I could try..."
    mc "Attagirl..."
    scene eaa 82
    a "*Breathing noticeably faster* Alright..."with dis14
    a "I’ll give it a shot... only for you..."
    mc "Please..."
    play sound6 blow6 volume 0.3
    show eaa 83 with dis14
    bla "Annie slowly envelops the tip of your cock between her soft lips before taking more of it inside her small, warm mouth. She struggles a bit at first, but then quickly becomes accustomed to it."with dis08
    mc "Yeah, just like t-that..."
    mc "Now take it deeper..."
    play sound blow6 volume 0.5
    show eaa 84 with dis15
    mc "AAAAAHHH..." with dis08
    play soundloop blowjob2 fadein 2
    $ renpy.music.set_volume(0.1, delay=8.0, channel='music3')
    scene annieb5 with dis2
    mc "HOT DAMN..."with dis
    mc "Oh my fucking god, this can't be real..."
    mc "I can’t believe you’re actually..."
    mc "Oh, baby, yes..."
    a "*Moaning* MMmmmmMMMmm..."
    play sound blow5
    stop soundloop fadeout 1
    scene eaa 86
    a "*Taking a deep breath* AAaahh..."with dis
    mc "No, don't stop, please..."
    a "I... I n-need to catch my breath!"
    mc "Oh... I t–"
    play sound2 blow4
    play soundloop blowjob2 fadein 1
    $ renpy.music.set_volume(1.0, channel='soundloop2')
    scene annieb5 
    bla "Annie shuts you up quickly by eagerly fitting as much of your dick as she can into her mouth again."with dis12
    mc "F-FUCK..."
    mc "Yeah... keep going... suck it as hard as you can, babe..."
    a "*Sucking harder* Mmmmh...!"
    mct "This sensation is unreal..."
    mct "I can feel Annie's lips stretched to the max... her small mouth completely filled by my cock..."
    a "*Choking* Mmmm... mmmm... mmmmhh..."
    mct "She's getting it so wet... she really seems to be savoring it..."
    mc "Good girl..."
    mc "That's it..."
    mc "Breathe through your nose..."
    mc "Just don't stop..."
    mct "My god..."
    mct "She's gonna drive me crazy..."
    a "*Moaning* Mmmhm..."
    mct "I can feel her getting more comfortable and confident with herself as time goes by..."
    mct "She's enjoying this as much as me."
    a "MMmmMmMmmhm...."
    mct "Should I push her limits? Or let her find her own rhythm?"
    $ annieblowjob1 = True
    menu:
        with dis
        "Let her find her own rhythm":
            mct "I should let her take the reins on this... but maybe a little feedback wouldn’t hurt." with dissolve
            mc "*Panting* Annie...?"
            a "Hmm?"
            mc "D-Do you think you can go a little bit faster?"
            mc "I'm almost there..."
            stop soundloop fadeout 2
            play soundloop2 blowjob3annie fadein 2
            scene annieb6 with dis2
            bla "Annie obediently shifts gears and sloppily sucks your cock much faster, taking it as deep down her throat as she can." with dis
        "Push her limits\n[mt](scene variation)":
            $ anniefuckface = True
            mct "Fuck it, I can't restrain myself anymore..."with dissolve
            play sound5 clothes4
            stop soundloop fadeout 2
            play soundloop2 blowjob4annie fadein 2
            scene annieb7 with dis2
            mc "AHHHHHHGG...." with dis
            mc "NOW WE'RE TALKING..."
            bla "You grab Annie's head and start fucking her mouth. You can hear her choking with each thrust, but Annie's throat willingly takes all of you."
    mc "HOLY FUCK..."
    mc "O-Oh my god..."
    mc "That's it..."
    if not anniefuckface:
        a "*Choking* Hnng... mmmh... hhnng?"
        mc "N-Not sure what you asked, b-but... FUCK YES!"
    else:
        a "*Choking* Hnng... hnnggg... hhhnnnggg!"
        mc "F-Fuck YES!"
    mc "Take it all..."
    mc "GOOD GIRL..."
    mct "My god... this is really happening..."
    mct "The sweet, innocent, little girl I've known for years..."
    mct "The same one that used to blush and hide every time anything even remotely sexual was mentioned..."
    if not anniefuckface:
        mct "Is here milking my cock like a mad woman..."
    else:
        mct "Is here letting me use her mouth to milk my cock..."
    stop soundloop2 fadeout 1
    play sound woosh1
    scene eaa 84c
    mc "Come on Annie, you're gonna miss the entire movie!" with flashfast
    a "B-But that guy is... n-naked!"
    a "T-They showed his..."
    mc "The scene is over, don't worry!"
    a "Y-you sure?"
    mc "Yes!"
    stop soundloop
    $ renpy.music.set_volume(0.15, delay=1.0, channel='music3')
    if not anniefuckface:
        play soundloop2 blowjob3annie fadein 1
        scene annieb6 
    else:
        play soundloop2 blowjob4annie fadein 1
        scene annieb7
    play sound woosh1
    mc "AAAAargh... fuck, Annie..." with flashfast
    mc "That's it... suck it until it's dry..."
    a "*Choking* MMmmmmmmmhhh..."
    stop soundloop2 fadeout 1
    play sound woosh1
    scene eaa 84b
    adad "You better take care of my little girl while you're in the USA, [mc]." with flashfast
    mc "Rest assured Mr. Winters, I won’t let anything happen to her!"
    mc "I'll take care of Annie as if she was my sister!"
    stop soundloop
    $ renpy.music.set_volume(0.15, delay=1.0, channel='music3')
    if not anniefuckface:
        play soundloop2 blowjob3annie fadein 1
        scene annieb6 
    else:
        play soundloop2 blowjob4annie fadein 1
        scene annieb7
    play sound woosh1
    a "*Choking* MMMmmMhhhHh!" with flashfast
    mc "Oh GOD, Annie, I'm gonna fucking cum!"
    a "Mmmmmhh..."
    stop soundloop2 fadeout 1
    play sound blow4
    play sound2 blow5
    scene eaa 85
    a "*Catching her breath* AAAAaaaAAAArgHhhh..."with dis 
    a "*Catching her breath* I c-can't... take it... anymore..."
    play sound3 clothes4
    play sound4 chair3
    play sound5 fall2
    play sound6 fall3
    show eaa 87
    bla "You pull Annie to the floor as she collapses, completely exhausted, right in front of you." with dis12
    a "*Panting* A-Are you... gonna... finish on m-me...?"
    mc "I want to..."
    mc "Can I...?"
    a "*Panting* Yeah..."
    a "*Panting* Do it... empty y-yourself all over me, [mc]..."
    mc "Oh god Annie, I'm..."
    mc "I'M ALMOST..."
    play sound cum2
    play sound2 cumall
    play sound3 cum4
    show eaa 88
    mc "AAAAAAHHHH..." with hpunchlong4
    scene eaa 89 with dis17
    mc "Jeez..." with dis
    a "H-Holy cow..."
    a "You... released... a lot..."
    mct "Man, I love seeing her slim body covered in my cum."
    mc "You okay? Sorry, I couldn't really hold back there..."
    show eaa 90
    a "Yeah..."with dissolve 
    a "I-It's okay."
    a "It tastes... weird. I mean, not bad, just umm... different. I can't really liken it to anything I've had before."
    play soundlow chair2
    stop music3 fadeout 8
    play soundloop rain3 fadein 7
    scene eaa 91
    a "*Standing up* Oh god, my jaw hurts..."with dis15
    mc "Yeah... that ended up being pretty intense... I hope I didn't overdo it there."
    mc "But my god, I have to say... that felt unbelievably good."
    $ annie_points += 1
    play sound beat
    show screen heartbeat
    show eaa 92
    a "R-Really? It c-couldn't have been that big of a deal, right...?"with dis
    show eaa 93
    mc "Are you kidding me?"
    mc "Goddammit Annie... that was mind-blowing."
    show eaa 92
    a "Oh... well t-thanks."
    a "I mean... I'm glad. I didn't know I could make someone feel like that."
    a "I actually had a lot of fun too."
    a "Maybe even too much... I forgot to lock the door."
    show eaa 93
    mc "Well, I'm sure Dalia and Penelope would knock before entering your room."
    mc "Not so sure about Nancy though..."
    mc "Let's just say she has a bad history with closed doors."
    show eaa 92
    a "Still, w-we should be more careful."
    a "Imagine if Nancy had caught us... she'd kick us out of the house!"
    show eaa 93
    mc "*Snorts* I highly doubt that."
    if nancypath:
        mc "Why would she? We weren't doing anything wrong."
        mc "And besides, knowing Nancy, I think it's more probable that she'd ask to join in rather than giving us the boot!"
        show eaa 94
        a "[mc]!" with dis08
        a "Don't be nasty!"
        show eaa 94b
        mc "*Chuckles* Okay, okay."
        show eaa 95
        a "Do you think she'd really ask that, though...?" with dis
        a "It's true that she can be quite passionate, but..."
        mc "Huh...?"
        mc "Do I sense some... interest?"
        show eaa 94
        a "O-Of course not!" with dis08
        a "I was just... digressing."
        show eaa 94b
        mc "Ah yeah, of course..."
    show eaa 96
    a "*Clears throat* Anyway, I'm gonna take a shower!"with dis12
    a "I can't really go to bed like this... you've made quite the mess of me."
    mc "Of course."
    mc "Good night, Annie."
    mc "Thank you for an amazing night."
    show eaa 97
    a "Oh, before I leave..."with dis 
    a "I wanted to say something."
    mc "What is it?"
    show eaa 98
    bla "She slowly approaches you, raises herself onto her tiptoes, and leans into your shoulder."with dis14
    mc "Are you okay?"
    a "Next time..."
    mc "Huh?"
    show eaa 99 
    a "*Whispering* Next time... I'll be {i}ready{/i} for you."with dis14
    play sound doorclose
    play sound2 run
    show eaa 36 with dis15
    bla "Annie rushes out and heads towards the bathroom."with dis 
    mct "Oh my god..." 
    mct "That literally gave me goosebumps. I was feeling completely spent, but after hearing that, now I'm getting all wound up again."
    mct "And then people ask me why I want to stay in Kredon."
    mct "I don't think I can get the thought of “next time” out of my head for a while..."
    mc "*Sighs* (I guess now it's finally time to hit the sack.)"
    mct "Let's see if I can manage to sleep after this."
    mct "What a day..."


label nextday06:
    stop soundloop fadeout 4
    scene black with dis25
    show screen nextday with dis17
    pause
    play soundloop rain5 fadein 5
    hide screen nextday
    scene raintransition06 
    with dis22
    pause 2.2
    play sound carpasswet
    pause 3.4
    scene er 1 with dis
    play music2 happy14 fadein 4
    $ renpy.music.set_volume(0.35, delay=20.0, channel='soundloop')
    mct "I can't believe we're a month away from Christmas already." with dis12
    mct "But well, at least I won’t have to empty my bank account."
    mct "Nancy made us all promise that we wouldn’t do gifts this year, and instead we’d all celebrate the holiday with a ski trip weekend."
    if daliapath:
        mct "Dalia, on the other hand... her birthday is on January 1."
        mct "Man, having your birthday on New Year’s Day has to be a real bummer."
        mct "Even if people still wish you a happy birthday... it has to feel way less “special”."
        mct "And not to mention, if you want to do anything fun, most people are nursing their hangovers after a night of celebrating."
        mct "Perhaps I could surprise her by celebrating it a couple of weeks earlier? Maybe before Christmas. I'm sure she wouldn't expect that and would appreciate the gesture."
        scene er 2 with dis15
        mct "I should get her something too."with dis08
        mct "She was complaining the other day about her current protein powder. I think she was eyeing a much cleaner, natural kind, but it was way beyond her budget."
        mct "I'm sure she'd like that, and it'd motivate her to train even harder."
        mct "I know she’s been trying to bulk up her arms for a while now, and hasn’t made much progress."
        mct "Now, what flavor should I choose..."
        mct "Vanilla, cookies and cream, peanut butter..."
        mct "Barbecue ribs...?"
        mct "Kale and wheatgrass sundae??"
        mct "These people must be running out of ideas."
        menu:
            with dis
            "Kale":
                mct "That sounds so crazy that it must be worth a try. Maybe it’s a new hipster flavor or something."with dissolve 
                show screen eternals
                with dissolve 
                play sound coins
                $ money -= 25
                pause .05
                $ money -= 25
                pause .05
                $ money -= 25
                pause 
                hide screen eternals
            "Cookies and cream":
                $ proteinflavor += 1
                mct "No one dislikes cookies. You can't go wrong with the classics."with dissolve
                show screen eternals
                with dissolve 
                play sound coins
                $ money -= 22
                pause .05
                $ money -= 22
                pause .05
                $ money -= 22
                pause 
                hide screen eternals
            "[gr]Barbecue":
                $ proteinflavor += 2
                mct "I mean... I have seen her completely devour a whole rack of barbecue ribs in less than 5 minutes. This sounds like her."with dissolve
                show screen eternals
                with dissolve 
                play sound coins
                $ money -= 23
                pause .05
                $ money -= 24
                pause .05
                $ money -= 24
                pause 
                hide screen eternals
            "Don't buy her anything":
                mct "Oof, this is way more expensive than I thought."with dissolve
                mct "I should save the money."
                $ daliaproteinbuy = False
        show er 1
        mct "Alright, one less thing to worry about." with dis
    show er 4
    mct "This damn bus is sure taking its sweet time."with dis08
    mct "I hope Alex doesn't get pissed off if I'm late."
    play sound3 vibration
    play sound2 vibration
    blank "{i}Your phone buzzes."
    show er 1
    mc "Hmm?"with dis
    mct "Oh, speak of the devil..."
    call chat(alex_chat3) from _call_chat_13
    mct "Damn, what a downer. I was looking forward to seeing her new place." with dis08
    mct "I mean, she said not to go, but I can't help wondering if she really meant that. Maybe she's just too stubborn to ask for help."
    menu:
        with dis
        "Get some meds and blankets and visit her anyway [gr][mt](Alex's path)":
            $ visitalex = True
            mct "Worth a shot." with dissolve
            mct "Worst case, she’ll slam the door in my face."
        "Forget it and go home":
            mct "It's probably better to give her space."with dissolve 
            mct "No girl wants people to see her face when she’s ill."
            mct "I'll just go back home and log into Eternum there."
    c "MY MAN!" 
    show er 4
    mc "Mmm?" with dis08
    play sound chair2
    show er 6 with dis 
    mc "*Standing up* Hey my dude!"with dissolve
    mc "What are you doing here? Weren't you going hiking with Micaela today?"
    show er 7
    c "We had to call it off due to the rain." with dis08
    c "I mean, we have raincoats and gear to stay dry, but the news is saying there’s a major storm brewing for this afternoon."
    c "It’ll be a huge downpour, even for Kredon’s standards."
    show er 6
    mc "Awh, that's too bad." with dis08
    mc "And what are you doing now? Any back-up plan?"
    show er 7
    c "Well... I thought about inviting her to the movies but I ran out of money." with dis08
    c "My gig at the gym doesn't pay much, unfortunately."
    show er 6 
    mc "Oh..." with dis08
    menu:
        with dis
        "[gr]Lend Chang $25":
            mc "Hey, take $25 and take your girl to the movies."with dissolve
            $ changmoneymovies = True
            show screen eternals
            with dissolve 
            play sound coins
            $ money -= 8
            pause .05
            $ money -= 8
            pause .05
            $ money -= 9
            pause .4
            hide screen eternals
            show er 6b
            c "Oh shit, are you serious?!" with dis
            mc "Of course! Your happiness is my happiness."
            mc "And besides, you're always helping me, it's the least I can do."
            show er 5
            c "You're the best, [mc], thank you." with dis08
            show er 6
            mc "Don't even mention it."with dis03
            show er 5
            if changshirts:
                c "Now I'm even more stoked to give you this special something-something!"with dis03
            else:
                c "I've gotta go then, my day suddenly got very busy!"with dis03
                c "Lots of things to do instead! Not everybody can get As without studying, or build muscle without training at least 5 times a week."
        "Don't lend him money":
            mc "That really sucks. I'm sorry." with dissolve
            show er 5 
            c "No worries! I'll think of something else to do."with dis03
            if changshirts:
                c "What's important right now is the special something-something I've got for you."
            else:
                c "But anyways, I've gotta go."
                c "Lots of things to do instead! Not everybody can get As without studying, or build muscle without training at least 5 times a week."
    if changshirts:
        show er 6
        mc "Huh?"with dis03
        show er 5
        c "THE SHIRTS ARE READY!" with dis03
        show er 6
        mc "Eh? What shi–"with dis03
        mc "O-Ohh, the matching T-shirts!"
        show er 5
        c "I already gave Penelope and Luna theirs at the mall."with dis03
        c "They were actually the ones who told me you'd be here."
        show er 7
        c "I wasn't sure about your size since you're growing bigger and bigger by the day, so I went with a large, even though you always used to rock a medium."with dis08
        show er 8
    else:
        show er 6
    mc "Oh, so you've noticed it too!"with dis03
    mc "I {i}did{/i} get stronger! I thought I was going crazy."
    show er 5
    if changshirts:
        c "Of course! Nothing wrong with a bro ‘mirin your progress."with dis08
    else:
        c "Of course! Nothing wrong with a bro ‘mirin your progress."with dis03
    c "You've changed a lot since you got to Kredon."
    show er 6
    mc "Well, I wouldn't say I’ve changed {i}that{/i} much. Apart from more muscle, I'm exactly the same."with dis03
    show er 7
    c "Are you kidding me?"with dis08
    c "You don't look at yourself in the mirror?"
    show er 8
    mc "What?"with dis03
    play sound whoosh6
    scene er9b
    c "Your skin looks drier and your nails have darkened."
    mc "My nails...?"
    play sound whoosh6
    scene er9c1
    c "You're definitely looking more swole, almost like you've been testing some sketchy supplements at the gym."
    play sound whoosh6
    scene er9c2
    c "You got yourself some big-ass eyebags like you haven't been sleeping properly for a whole month."
    play sound whoosh6
    scene er9c3
    c "And your hair’s growing super fast, you always look messy."
    mc "Ah..."
    mc "I-I thought you meant I changed in good ways."
    scene er 13
    c "I did, I did!"with dis
    c "Ladies love the laid-back, casual style... and you're rocking it!"
    c "Looking more fit is always good, and the eyebags give you a mysterious, sexy look."
    c "Plus, that hairdo?? You know how many men have gone to hair stylists hoping to get that look?"
    c "With that front SWOOP?! It SWOOPS so effortlessly..."
    c "You look great, man!"
    show er 6
    mc "*Chuckles* Well, if you say so." with dis
    mc "Thanks for the self-esteem boost."
    show er 5
    c "Anyways, I really have to go now."with dis03
    if changshirts:
        c "Do you wanna see the shirt before I go, though?"
        show er 6
        mc "Of course!"with dis03
        play sound clothes4
        show er 14
        c "*Clears throat* Behold..."with dis
        c "The best piece of clothing your eyes have ever seen..."
        c "Whether you’re going to a wedding, a funeral, a marathon, or on a date with the love of your life..."
        c "No matter the occasion, you’ll be able to wear..."
        stop music2 fadeout 1
        play sound clotheswhoosh
        play sound2 whoosh7
        play sound3 divine3
        show er 15
        c "*Taking his jacket off* THIS.{w=3.7}{nw}" with dis
        play sound3 pop
        play music2 happy14
        scene er 17
        c "Reinforced seams and stitching, a patented breathable 100%% cotton-blend material, and it can be washed in hot or cold water without any compromise to its quality. Made in Kredon! Organic and fair trade!"
        show er 16
        mc "Oh damn!"with dis03
        mc "*Laughs* That's so freaking cool!"
        mc "*Looking at all the shirts* I love them!"
        show er 17
        c "Really? The design is mine!"with dis03
        show er 16
        mc "*Laughs* Amazing. They're hilarious."with dis03
        show er 17
        c "Do you wanna try yours?"with dis03
        show er 16
        mc "Sure! Hand me it and then I'll try it on at home."with dis03
        play sound jumpscare3
        stop music2
        scene er 18
        c "Try it now."
        play sound2 clothes4
        play sound3 clothes2
        mc "*Putting the shirt on* O-Okay, okay!"
        play music2 happy14 fadein 2
        show er 20
        mc "Oh, it fits like a glove."with dis12
        show er 19
        c "It really does!"
        c "Do you like it then?"
        show er 20
        mc "Love it!"
        show er 19
        c "Phew, glad to hear that!"
        show er 17
        c "I'll give the rest of the T-shirts to the other girls whenever I see them."with dis 
        play sound2 clothes4
        play sound3 clothes3
        show er 16
        mc "*Putting your shirt back on* Sounds good!"with dis03
        mc "I'll text you later, buddy. Thanks for the shirts."
        if changmoneymovies:
            mc "And enjoy the movie with Micaela!"
        show er 17
        c "Thank you!"with dis03
        c "Good luck in the Wild West server! I hope you find that Gem."
        show er 16
    else:
        show er 6
        mc "Of course!"with dis03
        mc "See you later, buddy."
        if changmoneymovies:
            mc "And enjoy the movie with Micaela!"
        show er 5
        c "Thank you!"with dis03
        c "Good luck in the Wild West server! I hope you find that Gem."
        show er 6
    mc "Fingers crossed!"with dis03
    play sound chair2
    play soundlow carpasswet
    scene er 1 with dis14
    mc "*Sitting down* (Alright... where was I...)" with dis06
    if visitalex:
        mct "Ah, yeah, I've gotta buy some ibuprofen and decongestants for Alex before going to her house."
        mc "*Checking Google Maps* (Hmm... the nearest pharmacy is the one on Emerald Street.)"
    else:
        mct "Ah, yeah, I should go back home to log into Eternum with Dalia and Alex."
        mc "*Checking Google Maps* (Hmm... I'll go back on foot, it's just a 20-minute walk.)"
    if penelopepath and lunapath:
        play sound3 vibration
        play sound2 vibration
        blank "{i}Your phone buzzes."
        mct "Penny?"
        call chat(penelope_chat2) from _call_chat_14
        show er 3 
        mc "*Snorts* (Who would have guessed those two would have gotten along so well. They're like... peanut butter and jelly.)"with dis08
        mct "But I'm glad. I know they've been playing together in Warthogs these past few weeks."
        if changshirts:
            mct "And they were both wearing Chang's shirts in that pic. That's kind of adorable."
    play sound chair2
    scene er 22 
    mc "*Grabbing your umbrella and standing up* Alright, time to go."with dis12
    mct "That Gem isn’t going to just magically appear in our inventory."
    show er 23
    mct "I'm excited to play again with..." with dis08
    play sound risingshort
    stop music2 fadeout 1
    show er 24 with dis15
    play music pendulum fadein 6
    pause 
    play soundlow thunder fadein 4
    show er 25 with dis2
    mc "What..."with dis
    mc "Axel...?"
    mc "Damn, you look... like shit."
    show er 27
    ax "Yeah, I... haven't been sleeping very well lately." with dis14
    scene er26
    mc "What the fuck dude, where have you been?"
    mc "You haven't been to school in weeks."
    mc "I asked Alex, but she didn't know anything either."
    scene er27
    ax "I know. I've been... busy."
    scene er26
    mc "Ah... okay."
    ax ". . ."
    mc "So... you got anything to say?"
    mc "Or are you just wandering around town looking like that, hoping to experience the life of a hobo?"
    scene er 29
    ax ". . ." with dis12
    scene er28
    ax "How..."
    ax "How did Benjamin die?"
    scene er29
    mc "*Laughs* Fuck me, REALLY?!"
    mc "Oh my god, and here I thought you were going through some tough situation, but I see you’re still the same idiot."
    mc "I've told you a hundred times, I DIDN'T–"
    scene er28
    ax "I know you didn't kill him."
    ax "But I also know that there’s more you aren’t telling me."
    scene er 27
    ax "I am aware that Benjamin was a piece of shit."with dis12
    ax "No one gave a fuck about his death, not even his family."
    ax "He probably even deserved what happened to him."
    ax "But... he also was the only one who I could call a friend. I deserve to know what really happened to him."
    scene er26
    mc "Why would I tell you anything?"
    scene er27
    ax "You want info about Ulysses? About the things they're doing? The things they want to do?"
    scene er26
    mc "What...?"
    scene er27
    ax "I've been investigating, digging into what my father has been scheming."
    ax "And I can... delve into it more. If you share what you know."
    scene er26
    mc "William Bardot..."
    show er27
    ax "Look, I'm not asking to become best buddies."
    ax "I know you don't exactly have warm feelings towards me, and fuck, I don't like you one bit either."
    ax "I'm not trying to redeem myself or some shit like that."
    ax "All I’m asking for... is an exchange of information."
    scene er26
    mc ". . ."
    menu:
        with dis
        "[gr]Tell him what you know":
            $ axelhelp = True
            mc "Even if I told you, you wouldn't believe me." with dis06
            scene er27
            ax "I could say the same thing."
            scene er26
            mc "*Sighs* Okay..."
            mc "Benjamin... was excommunicated."
            mc "We believe that the Praetorians have a way to kill you both in Eternum and the real world at the same time."
            mc "And when that happens... your consciousness gets trapped in the game."
            mc "You become..."
            scene er27
            ax "An NPC."
            scene er26
            mc "Yes..."
            scene er 28
            ax "So it's true..." with dis12 
            scene er29
            mc "Wait... you knew this?" 
            scene er28
            ax "Listen now, you fucking halfwit..."
            ax "Eternum... is not a game."
            scene er29
            mc "What...?"
            scene er 27
            ax "A game like Eternum would require a gargantuan network, with tens of thousands of enterprise-level servers working in parallel within gigantic data centers."with dis12
            ax "The amount of processing power that’d be required to run such a game would be unfathomable."
            ax "And yet... there is nothing."
            ax "Nothing."
            scene er26
            mc "Then... how is the game running?"
            scene er27
            ax "Whatever Eternum is... it's not digital."
            ax "And Ulysses... somehow... found a way to access it through the neural implant."
            scene er26
            mc "*Mocking chuckle* You're telling me that... Eternum is like... a parallel dimension?"
            mc "Because that sounds a bit..."
            scene er27
            ax "I don't know what it is."
            ax "Only The Founder seems to know its secrets."
            ax "That's why my father is obsessed with the Gems of Doom."
            scene er26
            mc "Your father wants to gather the Gems of Doom? Why?"
            scene er27
            ax "He wants to claim ownership of the company and be able to control {i}everything{/i}. As he has always done."
            scene er26
            mc "But if your theory is true..."
            mc "What is Eternum, truly? Who is The Founder? And what about the Praetorians? Idriel?"
            mc "Were they all human once? Is someone controlling them?"
            mc "Are the NPCs aware of their very nature and existence?"
            mct "What about Calypso...?"
            scene er27
            ax "I... do not know."
            ax "I'll keep investigating my father."
            ax "I think... I think he knows more than what he claims."
            scene er26
            mc "I see..."
            mc "We'll let you know what we discover too."
            ax "Hmm."
        "Tell him to fuck off":
            mc "I have a better idea: why don't you shut the fuck up and get out of my sight?"with dis06
            mc "That is, unless you want me to punch your sad little face again."
            scene er 29     
            ax ". . ." with dis12
            mc "If you really thought I'd just welcome you with open arms into our group and start telling you all I know, just because you're all apologetic now, you were very much mistaken."
            scene er28
            ax "You fucking half-wit..."
            scene er29
            mc "Ah, showing your true colors again, eh?"
            mc "You won't fool me. Get lost."
    play soundlow thunder fadein 4
    scene er 30
    bla "Axel turns around, lifting his head towards the falling rain as he tries to maintain his proud posture."with dis2
    ax ". . ."
    ax "How's Alexandra?"
    mc "What?"
    ax "My sister. She left home a few days ago, but I know you've been hanging out with her."
    if axelhelp:
        mc "Oh..."
        mc "Well, she caught a cold today, but other than that... she's doing fine."
        ax "I see."
        mc ". . ."
        mc "Do you want me to pass along any message to her?"
        ax ". . ."
        ax "No. Not really."
    else:
        mc "She's fine."
        ax ". . ."
        ax "I see."
    stop music fadeout 8
    show er 31
    bla "Axel continues walking away until he rounds the corner and you lose sight of him." with dis17
    if axelhelp:
        mc "*Sighs* (It feels like for every question regarding Eternum that we manage to answer, four more arise.)"
        mct "Not a game...?"
        mct "I don't even know what to think anymore."
    else:
        mct "Fuck that guy."
        mct "We're perfectly capable of handling things on our own. We don't need his help for anything."
        mct "Although... I wonder what he discovered about his father or Ulysses..."
    mc ". . ."
    if visitalex:
        mct "Anyway, let's head out to Alex's house."
    else:
        mct "Anyway, let's head back home."
        jump housenoalex06
    mct "Maybe a little walk will clear my mind."
    stop soundloop fadeout 5
    scene black 
    show screen afewminuteslater 
    with dis25
    pause
    play soundloop rain2 fadein 6
    play music happy14 fadein 5
    scene er 32 
    hide screen afewminuteslater
    with dis2
    pause
    play soundlow carpasswet
    mc "*Looking at your phone* (And... yep, this is the place!)" with dis
    mct "41 Oak Street, Apartment 25."
    mct "This looks nice! A bit far from the center, but it's in a good part of the town."
    mct "I guess that Alex is still a classy girl after all, even if she cut herself off from that life."
    mct "But anyway, the rain has drenched me enough already. Let's see how this fancy place looks from the inside!"
    stop soundlow
    play sound bellscary volume 1.2
    stop music
    play soundloop scarybuilding volume 1.2
    scene er 33
    pause .9
    play sound2 flicker
    scene er33
    pause 2.4
    mct "W-What the fuck..."with dis12
    play sound3 screamwoman fadein 1
    scene er 35
    nei2 "*Screams* AAAAAHHH!" with dis17
    nei1 "Shut up, you crazy bitch!"
    nei2 "Or what?! You won’t be able to talk to me like that after I go on TV and tell my story!"
    nei1 "Haha! No one gives a fuck about your story, you stupid whore!"
    nei2 "I'LL CUT OFF YOUR TINY LITTLE WEINER WHILE YOU SLEEP, YOU HEAR ME?!"
    play sound4 hitwall volume 0.8
    nei3 "*Punching the wall* HEY, SHUT THE FUCK UP ALREADY!"
    nei3 "I'M TRYING TO SLEEP!"
    nei1 "DON'T TELL ME WHAT TO DO, YOU CRUSTY ASS CUNT!"
    nei3 "WHAT DID YOU SAY?!"
    nei1 "DID I STUTTER?!"
    nei3 "OH, YOU KNOW WHAT?! THAT KID ISN’T EVEN YOURS YOU DUMB PIECE OF SHIT! SOMEONE ELSE HAS BEEN TAKING HER TO POUND TOWN AS SOON AS YOU LEAVE FOR WORK!!"
    play sound5 glassbreak
    nei1 "WHAT?! IS THAT WHY UNCLE JOHN WAS HERE THE OTHER DAY?!!"
    nei2 "THAT MOTHERFUCKER IS LYING!"
    mc ". . ."
    scene er 33 with dis12 
    play sound swallow
    mc "*Gulps* (I-Is this really the right place...?)"with dis08
    play sound7 flicker
    scene er33
    mct "Where the hell did Alex choose to live?!"
    mct "Maybe I got the wrong floor... let's see..."
    scene er 36 with dis17
    mct "Apartment 25... no, it's here."with dis08
    play sound6 dog volume 0.5
    mct "I'm not sure what I'll find in there. It's either going to be Alex or an Albanian drug lord with a Glock 19 pointed at my head."
    mct "Please be the former..."
    play sound2 ["<silence 1>", knock2]
    play sound3 ["<silence 1>", knock2]
    show er 38
    bla "After realizing there's no bell, you knock on the door."with dis12
    mc ". . ."
    mct "Weird. Maybe she left?"
    play sound3 knock2 
    play sound2 knock2
    mc "*Knocking again* Hello? Alex? It’s [mc]!"
    x "*In a congested voice* [mc]?"
    mc "Hi there!"
    play sound dooropen1
    show er 39 
    x "*Nasally voice* What the hell are you doing here?"with dis
    x "I told you not to come."
    mc "Surprise!"
    x "You can't come in now. Go away."
    play soundlow doorclose2
    show er 38 with hpunch
    mc "What?! Why?" with dis
    x "Erm... I have guests."
    mc "Who?"
    x ". . ."
    play sound dooropen1
    show er 39 
    x "Okay, I don't have guests, but you still can't come in."with dis
    mc "Come on, you can't leave me here in this scary hallway! I feel like I’m in the beginning of a crime scene TV show, right before the murder is committed!"
    x "Just go back home."
    mc "It's raining outside!"
    if alex_points <= 5 or not alexpath:
        x "*Serious tone* I said no."
        x "I'm serious."
        x "I appreciate your concern for me, and you can leave the meds, but I don't want you to catch my cold. Also... I prefer to be alone, honestly."
        x "So please."
        $ alexkicksyouout = True
        mc "Oh..."
        mc "Well, okay, I understand."
        mc "I'll go back home and play from there, then."
        mc "Are you sure you'll be fine?"
        x "Yes, I'll be fine."
        mc "Alright then, I won't bother you anymore."
        x "I'll see you and Dalia in Frontier Trails after you log in."
        mc "Sure thing!"
        mc "Take care, Alex."
        play sound doorclose
        scene er 38 with dis
        mct "Well, that's not the wholesome reaction I was expecting." with dis08
        mct "Although I can't do much more to change her mind."
        mct "This is Alex we're talking about, after all."
        mct "Anyway, I should hurry up and get back home. I don't want to waste any more time than what I've already wasted."
        mct "And I don't wanna stick around in this creepy hallway for too long..."
        jump housenoalex06
    x "I said no."
    x "I've got a cold, and I don't want... anyone to see me like this."
    play sound6 dog volume 0.6
    mc "I brought some meds and blankets for you. And even a tub of your favorite ice cream!"
    x "Go back home and I'll see you in Eternum. I'll be fine there."
    mc "But–"
    x "I-I don't need anyone to take care of me!"
    x "It's just a cold and I'm not 10 years old!"
    x "...though you can leave the ice cream at the door."
    x "NOW BYE!"
    play soundlow doorclose2
    show er 38 with hpunch 
    pause .2
    mc "*Sighs* Okay... I guess I'll go back home."with dis
    mc "I'll leave the whole bag here, just in case you need it later."
    mc "Take care, Alex."
    play sound footsteps
    show er 37
    bla "You walk down the hallway again and leave." with dis17
    x ". . ."
    show er 38
    x ". . ." with dis12
    x "You're still here, aren't you?"
    mc "Yes."
    play sound dooropen1
    show er 39
    x "You're a real pain, you know that?"with dis 
    mc "I get that a lot."
    x "*Grumbling* Okay, okay... you can come in!"
    x "But don't look at the apartment too much. I'm still unpacking and everything's pretty messy."
    mc "Yay!"
    play sound2 dooropenclose
    stop soundloop fadeout 3
    $ renpy.music.set_volume(0.35, channel='soundloop2')
    play soundloop2 rain3 fadein 5
    play music ["<silence 3>"]
    queue music happy14 fadein 10
    show er 40
    bla "Alex opens the door to let you in and locks the door immediately after." with dis17
    mc "Hey, it looks nice inside!"
    mc "Quite a contrast with that dark hallway... you sure chose a scary place."
    x "I didn't really care about the building. And well, the..."
    play sound sneeze2
    x "*Sneezes* Ah-choo!" with vpunch 
    x "...the r-rent was very cheap because of it."
    show er 41
    mc "*Turning around* Honestly, just the fact that you alone managed to..." with dis12
    $ unlock_look("alex", 7)
    mc "Oh my god."
    mc "Okay, sniffly Alex is now the most adorable thing I've ever seen."
    show er 42
    x "S-Shut up." with dis
    x "I'm constantly blowing my nose and sneezing, and my nose turned all red."
    x "My face looks like a tomato."
    show er 43
    mc "Exactly! It's so cute."
    show er 42
    x "Not cute. I look like a mess."
    x "Stop making fun of..."
    show er 45
    x "Aaahh..."with dis08 
    play sound sneeze2
    show er 46
    x "*Sneezes* Ah-choo!" with vpunch 
    show er 42
    x "...me."with dis
    show er 43
    mc "*Laughs* It wasn't my intention."
    mct "I've gotta say, this oversized shirt looks kind of hot."
    show er 44
    mct "It's actually {i}hot{/i} seeing Alex like this, not gonna lie... Maybe because I'm not used to seeing her so... “vulnerable”?"with dis12
    mct "I hope I don't develop a kink for sick girls now..."
    show er 43
    mc "Are you sure it wouldn't be better if you just rested today?"with dis12
    mc "We can play tomorrow."
    show er 42
    x "No way. We promised Nancy we'd find this Gem and we will. And Dalia is waiting for us!"
    x "If you want, I'll take one of those pills of yours and I'll be as good as new by the time we..."
    show er 45
    x "Aaahh..."with dis08 
    play sound sneeze2
    show er 46
    x "*Sneezes* Ah-choo!{w=0.5}{nw}" with vpunch 
    show er 45
    x "Aaahh...{w=0.8}{nw}"with dis08 
    play sound sneeze2b
    show er 46
    x "*Sneezes* Ah-choo!" with vpunch 
    show er 47
    x "*Nasal voice* ...log off."with dis12
    show er 41
    mct "God, I want to take care of her so bad."
    mct "Please let me take care of you."
    show er 47
    x "Anyway, let's get to work, shall we?"
    show er 41
    mc "You're not going to give me the grand tour of your new apartment first?"
    show er 48
    x "Oh, but of course, of course!"with Dissolve(1.1)
    x "*Clears throat* Ladies and gentlemen, welcome to my humble abode... the newest mansion of the Bardot family!"
    x "As we step through this majestic entrance, we are greeted by the sight of this warm and spacious hall."
    show er 40
    x "The unpacked boxes paint a picture of a space adorned with comfort and style, and the completely empty walls add a touch of..."with dis12
    play sound sneeze2
    x "*Sneezes* Ah-choo!" with vpunch 
    x "...elegance."
    mc "*Laughs* Ah yes, I can see that."
    show er 49
    x "But let's not stop here! Much more grandeur awaits!" with dis12
    x "Please, let's make our way into the heart of the home!"
    play sound dooropen2
    show er 50 with dis14
    x "I present to you, the room of living! Also called by many as... the living room! " with dis08
    x "Here you will find a quaint space designed for gathering with loved ones and entertaining guests, where delicious home-cooked meals are shared and memories are made."
    mc "*Chuckles* I know you're being sarcastic, but this place is unironically awesome, Alex."
    x "Really...?"
    mc "Really. Did you decorate it yourself?"
    show er 51
    x "Well, kinda, I guess." with dis12
    x "I bought the table and the chairs on Craigslist, and the sofas and rugs at a flea market a couple of days ago."
    show er 52
    x "The frames on the walls, the coffee table, and the lamps were already here when I rented the place."with dis
    x "I still have a few things to unpack."
    show er 53
    mc "That's awesome. I admire how resourceful and tenacious you are."
    show er 52
    x "And then going that way, you can find a small kitchen, the bathroom, and another room."
    show er 53
    mc "Oh, can I see your bedroom?"
    show er 54
    x "Of course, make yourself at home." with dis
    x "It's definitely the best part of the house."
    mc "Oh, can't wait to see it!"
    x "Take a good look."
    play sound pop
    show er 55
    pause
    mc "Ah, minimalist decor. I like it." with dis06
    x "Yeah, did you notice the soup can?"
    mc "Indeed, it adds an element of artistic intrigue while still avoiding any compromise to the elegant composure of the space."
    x "*Snorts* I'm glad to finally meet another expert in decoration."
    play sound sneeze2b
    x "*Sneezes* Ah-choo!"with vpunch
    show er 56
    x "*Nasal voice* Jeez, this cold is really beating me up... you mind if I grab one of those pills now?"with dis14
    show er 57
    mc "Of course not, that's why I brought them."
    mc "They're in the bag."
    show er 56
    x "Thank you."
    x "You can start putting your E-suit on, I'll do the same."
    x "We can play here in the living room."
    show er 57
    mc "Sure thing!"
    play sound chair1
    scene er 58 with dis15
    bla "You sit on the sofa and start putting on the E-suit while Alex goes to her room to do likewise." with dis
    mct "Should I mention I saw Axel earlier?"
    mct "Hmm... it's probably better to wait until later, I don't wanna ruin the mood."
    x "*Talking from the other room* What the hell is all this?"
    mc "What?"
    show er 59
    x "This bag of yours."
    x "There are like, a thousand things in here."
    show er 60
    mc "Yeah, well, I didn't know what you had exactly, so I brought a bit of everything."with dissolve 
    mc "Tylenol for fever reduction, ibuprofen, nasal spray, and a throat soother."
    mc "Then I also got some cough drops for later, a few tissues, and a blanket. Ah, and don’t forget the ice cream! Put it in the freezer before it melts. "
    play soundlow noise1
    play sound2 clothes4
    show er 61
    x "And what the fuck is this shit?" with dis
    show er 62
    mc "What shit?"
    show er 61
    x "There's like an ugly egg plush."
    show er 62
    mc "OH! Dr. Eggdogstein!"
    show er 61
    x "I'm sorry?"
    show er 62
    mc "The lady who sold me the blanket told me it brings good fortune and helps to cure colds and to heal wounds."
    mc "I thought it could keep you company in your new apartment."
    $ alex_points += 1
    play sound beat
    show screen heartbeat
    show er 63
    x "*Snorts* Hmm."with dis
    show er 58
    mc "Do you like it?"
    x "I hate it."
    x "You definitely were scammed."
    mc "Hmm, now that you mention it, the price of that blanket did seem a little steep, yeah..."
    show er 64
    x "Alright, I'm all set."with dis12
    mc "Sweet!"
    play sound chair1
    show er 66
    mc "Did you take any of the meds yet?"with dis 
    show er 65
    x "Yeah, yeah, one pill and one of those lozenges."
    show er 66
    mc "Good choice!"
    mc "You should be as good as new by the time we finish our session."
    show er 65
    x "Let's not waste any more time, then. I already sent you an invite."
    x "Just go to the saloon after entering the server, Dalia should be waiting for us there."
    x "You can't miss it, don't worry. I've been on this server a few times."
    show er 66
    mc "And you? Where's your E-visor?"
    show er 65
    x "I'll go after you. I don't wanna start playing while you're still “awake”."
    x "Who knows what you could do to my precious apartment while I'm pretty much unconscious."
    show er 66
    mc "Come on! Really? You know me already!"
    show er 65
    x "I do, that's why I'm worried!"
    show er 66
    mc "*Laughs* Fuck off."
    show er 67
    mc "*Chuckles* Okay, okay, your house, your rules."with dis 
    mc "See you on the other side!"
    stop music fadeout 10
    play sound2 beep
    play sound ai7
    blank "{i}Connected." with dis
    play sound ai8
    blank "{i}Welcome back to Eternum." with dis
    play sound ai9
    blank "{i}You've received an invitation from..." with dis
    play sound aialex
    blank "{i}Alex." with dis
    play sound ai10
    blank "{i}Would you like to join her session?" with dis
    mc "Yes!"
    play sound ai11
    blank "{i}Please prepare to connect..." with dis
    scene er67
label westernloginnoalex:
    stop soundloop2 fadeout 4
    play sound risingshort4
    pause 2
    scene login3 with flash
    pause 8
    play soundlow whoosh4
    scene white with dissolve
    scene ee 1 with Dissolve(2.5)
    play sound4 ["<silence 0.6>", steamtrain]
    play music western1 fadein 4
    pause
    show ee 2 with dis17
    pause
    play sound whoosh1
    pause .1
    play sound2 spell4
    pause .3
    show ee 3 with flashfast
    pause .5
    mc "*Looking at your outfit* (Oh boy...)" with dis08
    mct "Would you look at that!"
    mc "*Giggles* (I've been looking forward to this since Chang lent me Red Dead Redemption that one summer.)"
    show ee 3b
    mc "*Turning around* An authentic Wild West server!"with dis
    mc "And it is {i}exactly{/i} as I had imagined!"
    mc "Arid cliffs!"
    play soundlow whoosh6
    scene ee91
    mc "Rugged cowboys!"
    play soundlow whoosh6
    scene ee92
    mc "Rowdy saloons!"
    play soundlow whoosh6
    scene ee93
    mc "Lethal revolvers!"
    play soundlow whoosh6
    scene ee94
    mc "Ravishing elves!"
    play soundlow whoosh6
    scene ee95
    mc "Overflowing gold min–"
    mc ". . ."
    play sound musicstop
    play soundlow w2
    stop music
    scene ee9
    mc "W-What the hell?!"
    play music2 western2
    mc "C-Calypso? What are you doing here?!"
    scene ee 10
    ca "What do you mean?"
    ca "I thought we had already reached an agreement to collaborate together on the next mission. Have you forgotten?"
    show ee 9
    mc "Well, yeah, I remember. It's just that I wasn't expecting you to show up so fast, or... dressed up like that."
    show ee 10
    ca "Is there something wrong with my wardrobe?"
    show ee 9
    mc "Nothing wrong per se, but..."
    player2 "Hey! Have you seen my new horse?"
    player2 "A purebred Missouri Fox Trotter, the fastest horse in Frontier Trails!"
    play sound whoosh6
    play sound2 woodhit
    play sound3 debris3
    show ee11
    mc "*Pulling Calypso around the corner* Shit, someone's coming."with hpunch
    player3 "Eh?? This is not a Fox Trotter, it's a vulgar Morgan."
    player2 "What?! That fucking vendor told me it was the best horse in all of Eternum!"
    player3 "Please tell me you didn't pay any more than 40 eternals for this."
    player2 "FUCK!"
    mc "Phew, that was close."
    scene ee 12
    ca "You did not just grab me and handle me as if I were some lowly servant."with dis
    show ee 13
    mc "What? Oh... I'm sorry, Princess."with dis06
    mc "I was only trying to protect you. The enemy could be anywhere so we should really stay on our toes."
    mc "I apologize for the... sudden aggression. I had assumed a mighty sorceress like yourself could handle it."
    show ee 12
    ca "Eh... a-and you were right on that note. I can endure anything thrown at me." with dis06
    ca "But do not worry so much about my integrity."
    ca "An ordinary mortal could never stand up to me."
    show ee 13
    mc "Remember that the whole world is looking for you, though."with dis06
    mc "If the Immortals discover you escaped from your prison, they could come after you again."
    play sound2 clothes3
    show ee 14
    ca "Hmm." with dis12
    mc "In fantasy realms where elves and magic actually exist, you can blend in, but here you stand out like a fairy in a biker bar."
    show ee 15
    ca "I do suppose there is some sense to what you are saying."
    ca "The people of these lands seem to lack any sense of elegance and refinement. That is undoubtedly obvious."
    show ee 14
    mc "Can you transform your outfit again, like what you did at the Ulysses dinner party?"
    show ee 15
    ca "I have the ability to do so, yes."
    show ee 16 
    mc "Do you see that girl over there? The one next to the black horse."with dis 
    ca "I do."
    mc "Something like her outfit would be perfect."
    ca "Hmm..."
    show ee 17 with dis
    pause
    play sound polyjuice
    show ee 18 with dis2
    mc "WOW!" with dissolve
    mc "You nailed it. It looks exactly like hers."
    mc "And it looks way better on you, I must say..."
    mct "Good lord, Calypso has got one HELL of a bosom on her."
    mct "Nancy and Penelope definitely have some competition in that department..."
    show ee 19
    mc "Maybe a hat to hide your ears?"with dis06
    mc "Similar to the ones people are wearing in this town."
    play sound2 polyjuice
    show ee 20 with dis2
    ca "Like this?"with dissolve
    mc "Perfect!"
    show ee 21
    ca "Ah, now I see why these simple folk are sporting such ridiculously large headpieces."with dis14
    ca "It provides very ample protection from the harsh desert sun."
    ca "I rarely witnessed clear skies like this back in Hyril'ar when I was growing up."
    show ee 22
    mc "Your realm? Is it often rainy?"
    show ee 21
    ca "It depends on the season. But it never gets as sunny as here, so we all share a pale complexion."
    ca "I can understand why you seem to find satisfaction in exploring other worlds and integrating into their societies, [mc]."
    ca "It feels... invigorating."
    show ee 22
    mc "*Chuckles* Right?"
    mc "You might be more of an explorer than what you had originally thought, Princess."
    mc "Now follow me, let's meet Dalia and Alex."
    show ee 21
    ca "Yes... let us see what other peculiarities this world has to offer."
    play sound steamtrain
    show ee 1 with dis2
    pause
    show ee 23
    ca "*Reading the sign* {i}Saloon." with dis15
    ca "Is this place like... an alehouse?"
    mc "Yeah, something like that. Although they have their own distinct charm. "
    mc "Piano music, swinging doors, poker, and lots of cowboys."
    ca "What is a cowboy?"
    play sound stairswood2
    show ee 24
    mc "*Climbing the stairs* Um... they're like... these horse riders who originally used to work with cattle."with dis12
    mc "Although most of them kind of evolved into bounty hunters after the lack of law enforcement led to an increase in fugitives and crime in general."
    ca "I see..."
    ca "Fascinating."
    mc "*Chuckles* (It feels endearing explaining basic concepts to Calypso.)"
    mct "She might have many more decades under her belt, but there are certain aspects in which she seems to possess the innocence and wonder of a child."
    stop music2 fadeout 3
    play sound saloondoors
    play music2b saloon fadein 5
    show ee 25 with dis15
    bla "You enter the saloon and a rustic and lively atmosphere welcomes you."with dis
    mc "Alright, this is the meeting point."
    show ee 26
    d "[mc]! Over here!" with dis
    mc "There she is!"
    play sound ["<silence 0.4>", chair2]
    show ee 27 with dis12
    mc "*Sitting next to her* Good to see you!" with dissolve
    $ unlock_look("dalia", 11)
    mc "Wow, I love your hair. You look absolutely stunning."
    show ee 28
    d "*Giggles* Exaggerating as always. But thank you!"
    d "I thought the braid would match the style of the server."
    show ee 27
    mc "It definitely does."
    show ee 29
    d "Nice to have you here, Calypso!"with dis08
    d "I didn't know you were gonna join us."
    show ee 30
    ca "Yes, I decided to assist you in your quest to find these 10 special Gems."
    ca "I am still deeply indebted to you for my liberation and this Princess always pays her dues."
    ca "Furthermore, it may also unravel new leads that could allow me to return to my realm."
    show ee 29
    d "Well, we'll be happy to have your help, that's for sure."
    show ee 28
    d "I just hope no one discovers who you are because of how much you stand out."with dis08
    show ee 31
    mc "If she keeps her hat on there shouldn't be any problems."
    show ee 30
    ca "If my natural hair color is a problem I can temporarily modify it as well."
    show ee 31
    mc "There's no need. I just saw a girl with green hair on the way up here, so..."
    play sound chairmove
    show ee 32
    x "Oh my, the gang’s all here and ready to go!" with dis12
    $ unlock_look("alex", 8)
    x "Princess, Dalia, [mc]."
    if alexpath or alexkicksyouout:
        mc "Ah, that face rings a bell."
        play sound chair2
        show ee 34
        x "*Sitting down* Does it?"with dis
        show ee 33
        mc "*Chuckles* Yeah, although the last time I saw it, it was as red as a tomato."
        mc "Are you feeling better now?"
    else:
        mc "Hey, good to see you, Alex!"
        play sound chair2
        show ee 34
        x "Hey, stranger." with dis
        show ee 33
        mc "Are you feeling better from your cold?"
    show ee 34
    x "Yeah, definitely."
    x "I wouldn't be able to show up here otherwise, I have a reputation to uphold."
    show ee 33
    mc "Is that so? Do you play here very often?"
    show ee 34
    x "You could say I know the server. I come here to play as a bounty hunter from time to time."
    x "Criminals like to hide here, so it's not a surprise the man we're looking for had the same idea."
    show ee 38
    d "I've never been to this one in particular, but I've played a few times in Tumbleweed, another Wild West server."
    show ee 37
    mc "Damn, how many Western servers are there?"
    show ee 38
    d "These two used to be the main ones, but now Tumbleweed is practically abandoned."
    d "Most people just moved to Frontier Trails after a case of cannibalism in the other server."
    d "Some forums even talk about zombies."
    show ee 37
    mc "Damn, that sounds cool! We've gotta visit that one!"
    show ee 39
    sbar "Hello ladies and gents, welcome to the Blackridge Saloon!"with dis 
    sbar "Mighty pleased to have ya here!"
    sbar "Have yourselves a grand ol' time, but please kindly refrain from pointin' them guns at the pianist."
    sbar "Now, what can I rustle up for ya?"
    show ee 40
    mc "Hello!"with dis06
    menu:
        with dis
        "Coke":
            mc "We won't stay for long, but... I'll have a coke, thank you." with dissolve 
        "Coffee":
            mc "We won't stay for long, but... I'll have a coffee, thank you. With sugar." with dissolve 
        "Tea":
            mc "We won't stay for long, but... I'll have a cup of tea, thank you." with dissolve 
    show ee 39
    sbar "One whiskey, gotcha, comin' right up, partner!"with dis06
    mc "Eh? But I asked for a–"
    show ee 35
    ca "I will have a glass of water with a sprig of fresh mint, thank you."
    show ee 39
    sbar "Got it, another whiskey comin' up your way, ma'am."
    sbar "I'll get it poured for ya right quick!"
    show ee 41
    x "Um... yeah, I'll have a... whiskey, I guess."
    show ee 39
    sbar "Three whiskeys, got it!"
    sbar "I'll have 'em ready for ya before you can say “yeehaw”!"
    sbar "And the last lady?"
    show ee 42
    d "Yeah, um... what would you recommend, the buffalo ribeye or the T-bone?"
    show ee 39
    sbar "Both options are mighty fine, ma'am. Best steak in the whole server!"
    show ee 42
    d "And the side dishes?"
    show ee 39
    sbar "You can pick creamy mashed potatoes or honey baked beans. The beans are my Ma’s recipe, but either one will surely complement the steak just right!"
    show ee 42
    d "That's a tough choice..."
    show ee 44
    d "You know what? Bring me both entrees please, each one with a different side dish."with dissolve
    show ee 39
    sbar "Four whiskeys, a ribeye with Mama’s beans, and a T-bone steak with potatoes. They’ll be here in no time!"
    sbar "I’ll be over yonder, but if you need anything else, just give ‘er a holler!"
    show ee 44
    d "Thank you!"
    mc "Why’d you order so much food? Isn't it... kinda pointless?"
    show ee 45
    d "Don't judge me!"with dissolve
    show ee 46
    mc "*Chuckles* I’m not! Just curious."
    show ee 45
    d "Well, I do it because it tastes good, duh."
    d "I'll never have the chance to taste buffalo meat in the real world!"
    show ee 46
    mc "Fair point."
    mc "I've been looking forward to eating one of those dragon burgers in Ekabar myself..."
    show ee 44
    d "And besides, I read a study that says eating in Eternum can trick your brain into thinking that you've consumed more protein, so muscle growth is optimized!"with dissolve
    mc "*Chuckles* Definitely a win-win for you, then."
    if eva1:
        play sound2 chairmove 
        play sound ["<silence 0.5>", chair2]
        show ee 47 with dis12
        bla "A girl sits on the last free chair left and stares at you in silence."with dis06
        mc "Um..."
        mc "I'm sorry, we're in the middle of a private conversation."
        mc "So if you don't mind..."
        show ee 48
        aaa "*Giggles* This is crazy."
        aaa "I've gotta say, you're looking good!"
        show ee 47
        mc "Erm... thank you?"
        mct "Is this girl flirting with me?"
        show ee 41
        x "I'm sorry, do we know you?"
        show ee 48
        aaa "[mc] does."
        show ee 47
        mc "What...?"
        mc "How do you know my name?"
        play sound wood
        show ee 49
        aaa "*Leaning forward and resting her breasts on the table* Awwwh, have you really forgotten about me?"with dis
        show ee 51
        mc "Is this some kind of scam on this server? I don't know what you're trying to get from us, but I haven't seen you before in my life."
        show ee 49
        aaa "That's mean."
        aaa "I guess our encounter wasn't as special for you as it was for me."
        show ee 51
        mc "What...?"
        play sound2 wood
        show ee 52
        aaa "Ion. You were playing Eternum for the first time, and I was rocking a hairstyle that was way more... exotic?"with dis 
        aaa "And more blue."
        show ee 53
        mct "Blue...?"
        play sound3 pop
        show ee 54
        pause .3
        play sound4 pop
        show ee 53
        pause .5
        mc "OH SHIT."with dis08
        mc "Eva??"
        play sound5 wood
        show ee 50
        eva "Bingo!" with dis
        eva "At least you remember my name."
        show ee 51
        mc "Wow, you look so different without the crazy pigtails and the whole neon look!"
        mc "How have you been?"
        show ee 50
        eva "You know... just running back and forth."
        eva "I wasn't expecting to ever see you again, but... as I always say, Eternum has an odd way of bringing people back together again."
        show ee 51
        mc "Ain’t that the truth!"
        show ee 55
        ca "So... who are you?"with dis08
        ca "Are you one of [mc]'s erstwhile lovers?"
        mc "W-What?"
        show ee 51
        mc "O-Of course not!"with dis08
        mc "I was only around her for... like... for a few hours!"
        mc "Well... it was actually way less than that."
        mc "We..."
        mc "Uhh..."
        mc "We're friends. I-I was on Ion, and..."
        mc "Erm..."
        if daliapath and alexpath:
            $ renpy.music.set_volume(1.0, channel='soundloop')
            play soundloop beat3 fadein 3
            show ee 56
            mc "You know..." with dis12
            mc "Eh..."
            mc "I was kind of exploring the city, as uhh... adventurers do."
            mc "And then I saw this neon sign... a crazy cool sign, you know?! Should’ve seen it! It had... glowing letters... and words, and... uhh..."
            mc "*Nervous chuckle* W-Well, I vaguely remember it, t-to be honest."
            mc "I went to..."
            show ee 57
            mc "Damn, these whiskeys sure are taking a while, aren't they?" with dis
            mc "Did the bartender head out to harvest the barley himself or something? Ha ha ha..."
            stop soundloop fadeout 9
            show ee 51
            mc "Anyway..."with dis
            mc "W-Where was I?"
            mc "Ah yes, I..."
        play sound wood 
        show ee 58
        eva "There's no cool story behind it, really. Not much to write home about." with dis
        eva "I was a clerk in a newly opened bakery in Ion, and [mc] came in to try one of our Nanobite Cupcakes."
        play sound wood
        show ee 50
        eva "He was so nice and treated me so well that I didn't even charge him for it."with dis
        show ee 51
        mc "Yes. T-That's pretty much what happened."
        mc "Are you still working at the... bakery?"
        show ee 49
        eva "Nah. My boss fired me after she found out I let you go without paying."
        show ee 50
        eva "Turns out, giving away free stuff when you're starting a new job is not the best idea."
        eva "*Chuckles* I guess I should have seen that coming."
        play sound chairmove
        show ee 59
        eva "*Standing up* But anyway, I just wanted to say hi to [mc]!"with dis12
        eva "Sorry for interrupting, guys."
        show ee 59b
        x "You didn't, no worries."
        d "Yeah... no worries."
        mc "You sure you don't wanna stay for a bit?"
        show ee 59
        eva "Nah, I've got things to do, but thanks!"
        show ee 59b
        mc "Well, catch you around then."
        mc "It was good to see you."
        show ee 59
        eva "Likewise!"
        eva "Until next time, [mc]."
        eva "Good to see you keeping such {i}nice{/i} company..."
        show ee 59b
        mc "What can I say, I’m a very lucky man."
        show ee 59
        eva "*Giggles* Alright, bye guys!"
        play sound wood
        show ee 61
        mc "*Turning around* Well..."with dis12
        mc "Where were we?"
        show ee 60
        if daliapath:
            d "I didn't know you had so many {i}friends."
            show ee 61
            mc "W-Who, Eva? I wouldn't even call her that."
            mc "She's just an acquaintance."
            show ee 60
            d "Yeah... I heard the story."
            d "It sounded made up."
            show ee 61
            mc "It wasn't!"
            mc "I just met her once, for real."
            mc "I tried one of the... cupcakes there, and then I left."
            mc "Nice girl."
            d "Mm-hm."
            mc "*Clears throat* Shit, look at the time!"
        else:
            d "Are you done, Mr. Playboy?"
            show ee 61
            mc "Yeah, sorry about that."
        mc "We should get to work!"
        show ee 60
        d "Yeah, we should."
        show ee 61
    else:
        show ee 33
        mc "Alright, let's get to work!" with dis 
    mc "What do we know about this Gem, Alex?"
    play sound wood
    show ee 62
    x "*Leaning forward* Yes, that's a good idea. Let's do a little briefing."with dis
    show ee 64
    x "According to Nancy's informants, the leader of a small group of bandits, named “El Coyote”, could be in possession of another Gem of Doom."
    show ee 62
    x "If we manage to get our hands on two Gems in such a short time, it'd be a huge hit for us."
    show ee 65
    mc "Hell yes!"
    mc "Let's get that bastard."
    mc "What do we know about him?"
    show ee 62
    x "We know he's called “El Coyote” and that he's probably hiding in this server."
    show ee 65
    mc "Mm-hm."
    x ". . ."
    show ee 64
    x "Um... that's all."
    show ee 65
    mc "Oh."
    show ee 62
    x "That is why we cannot waste a second."
    x "We should split up and look for clues about his hideout or his gang around the town."
    show ee 65
    mc "Count on me!"
    show ee 63
    x "Alright, I'll go to the mines and see if anyone knows anything."
    show ee 62
    x "Dalia, you go talk to the Sheriff, near the station. See if we can get any info out of him."
    show ee 38
    d "Consider it done!"
    show ee 64
    x "Calypso, you can go talk to the Sheriff's deputy. I saw him behind this saloon just a minute ago."
    show ee 66
    ca "Engaging in conversation with the guardians of law and order of this realm should be interesting."
    show ee 63
    x "[mc], you talk to the bartender."
    x "He must have heard rumors from all over the town. Let's see if he can help us."
    show ee 65
    mc "Done."
    play sound wood
    show ee 34
    x "Alright, cool!" with dis
    x "We shouldn't delay this any further."
    x "Let's meet again here in a couple of hours."
    show ee 33
    mc "Let's get this Gem, girls!"
    play sound2 chairmove
    play sound3 clap
    show ee 67
    d "Can you ask the bartender to save one of the steaks for later?" with dis
    d "Promise him I'll be back and pay double."
    mc "*Chuckles* Sure, I will."
    d "Thanks [mc]!"
    d "Good luck on the mission!"
    mc "Be careful out there!"
    play sound chairmove
    show ee 68
    d "*Standing up* We will!" with dis14
    show ee 68b with dis12
    mct "Wow, they all look so hot." with dis08
    mct "How am I supposed to concentrate on the Gems of Doom when I have these three cuties with me?"
    if daliapath and alexpath:
        mct "Seeing them looking like that, I can't even believe that both Dalia and Alex have had their lips wrapped around my cock before. It almost feels unreal when I think about it."
        mct "Man, I'd kill to have another go with them someday..."
    elif daliapath:
        mct "Seeing her looking like that, I can't even believe that Dalia has had her lips wrapped around my cock before. It almost feels unreal when I think about it."
        mct "Man, I'd kill to have another go with her someday..."
    elif alexpath:
        mct "Seeing her looking like that, I can't even believe that Alex has had her lips wrapped around my cock before. It almost feels unreal when I think about it."
        mct "Man, I'd kill to have another go with her someday..."
    mct "And Calypso...? I'd fight a dragon just to see her naked."
    mct "With her royal status and distinct beauty, I’m sure it’d be unforgettable."
    x "Okay, let's go then."
    show ee 68
    bla "The three girls finish talking and leave the establishment."with dis14
    mct "Jeez, I'm super turned on again."
    mct "These few days away from them sure have taken a toll."
    if anniepath:
        mct "And what happened with Annie last night didn't help either, that's for sure..."
    play sound2 slap1
    mc "*Slapping your cheeks* (Okay, focus, [mc].)"with hpunch
    mct "Stop putting your skill points into “horny” and put them into “intelligence” instead. Focus on the Gems. Focus on WINNING!"
    mct "I should probably ask the bartender to cancel the whiskeys, though."
    mct "I don't want to have to drink them all myself..."
    play sound saloondoors
    stop music2b fadeout 1
    bla "You hear the saloon doors swing open as the piano abruptly stops playing." 
    play music westerndark fadein 4
    play sound4 wood fadein 2
    show ee 69 with dis15
    mc "*Turning around* (Huh?)"with dis12
    mct "Fuck, are those... Praetorians??"
    mc "*Hiding your face under your hat* (What the hell are they doing here?)"
    show ee 70
    pra "Attention, players." with dis08
    pra "All patrons of this establishment must immediately halt their current activities and take heed of our proclamation."
    pra "An illegal, stolen artifact has been detected within this server."
    pra "Your cooperation is now mandated by the Ulysses EGCE commission to swiftly recover the item. Time is of the essence."
    play sound gunload
    show ee 71
    sbar "Hold on there, partner..."with dis 
    sbar "Do you think you can just saunter into my saloon and start threatening my patrons just like that?"
    sbar "GET THE F–"
    play sound revolver2
    play sound2 revolver
    play sound3 shotgun
    play sound4 blood2
    show ee 72 with hpunch
    pause .6
    play sound5 ["<silence 0.6>", fall]
    play sound6 ["<silence 0.3>", woodhit]
    play sound7 ["<silence 0.2>", fallbottle]
    show ee 72b with dis
    pause 
    play sound2 steam2 volume 0.2 fadein 4
    show ee 73 with dis14
    pause
    play sound holster
    show ee 70
    pra "I’ll remind you that standing in the way of any Praetorian unit carrying out command-directed orders will face permanent Excommunication." with dis12
    pra "As previously stated, your cooperation is mandatory as this matter needs to be addressed immediately."
    pra "Are there any others that wish to air their grievances?"
    show ee 69 
    pra ". . ."with dis08
    show ee 70
    pra "The item of our attention is a palm-sized, cube-shaped artifact."with dis08
    pra "One of our operatives will be stationed in the town center until this matter has concluded. Any assistance provided in solving this case will be generously rewarded."
    pra "Do any of you have questions?"
    show ee 69 
    pra ". . ."with dis08
    show ee 70
    pra "Thank you for your cooperation."with dis08
    play sound saloondoors
    show ee 68
    bla "The two Praetorians leave the saloon."with dis15
    mct "Holy fuck... Praetorians are on the server?? This is not good..."
    mct "And what are they looking for? Calypso?"
    mct "No... that's impossible, the Founder knew she's with us. It wouldn't make sense for him to send them."
    mct "And... well, Calypso isn’t a “palm-sized, cube-shaped artifact”. What the hell is that about?"
    mct "I guess it'll be better if I just try to avoid them and go help the girls out there. It's not as if I can interview the bartender anymore."
    mct "A Wild West town, a hidden outlaw, and three sexy girls. This promises to be fun."
    mct "And possibly deadly."
    play sound2 saloondoors fadein 1
    jump secondmenuwestern

label calypsowestern:
    $ westerncalypso = False
    stop soundloop fadeout 8
    play music2 western2 fadein 5
    scene eec 1 with dis2
    bla "You survey the surroundings, and quickly spot Calypso sitting on one of the benches behind the saloon."with dis
    mc "There she is!"
    mct "Not the hardest girl to find. That hair of hers stands out like a lone tumbleweed in the middle of the desert."
    play sound chair2
    show eec 3 with dis12
    mc "*Sitting next to her* Be careful, Princess. Those things are deadly."with dis06
    show eec 2
    ca "I find the workings of this device to be remarkably ingenious, I must say."
    ca "Humans from my realm who cannot wield magic are limited to longbows or crossbows."
    ca "This seems to be much more... precise. And fast."
    show eec 3
    mc "That’s nothing. You should see the things we have created in the present time."
    mc "If there's one thing us humans are good at, it's killing each other."
    show eec 2
    ca "Hah, I must agree with you there. I have never seen any other race engaging in more internal conflicts. Not even the dwarves."
    show eec 3
    mc "Where did you get it from, by the way?"
    play sound holster
    show eec 5
    ca "I replicated the one the deputy was wielding."with dis12
    show eec 4
    mc "Oh, so you found him already!"
    show eec 5
    ca "Indeed. He mentioned having business to attend to at the neighboring establishment, and he said he would answer my questions thereafter."
    ca "I was waiting for him to come out."
    show eec 4
    mc "Nice!"
    mc "I see you quickly got the hang of things around here. You almost look like a local already."
    ca "Hmm."
    mc "You'd adapt to our world pretty fast, I'm sure."
    show eec 5
    ca "Of course. Humans are simple, and their intricacies, banal."
    ca "Although... some of them pique my curiosity, I must admit."
    show eec 4
    mc "Ah yeah, elven princesses do pique my curiosity as well."
    mc "One particular elven princess, to be precise."
    mc "*Chuckles* I even dreamt about you the other day."
    play sound holster
    play soundlow wood fadein 2
    show eec 6
    ca "Oh, really?" with dis
    ca "I very much hope there was no indecency in that dream."
    show eec 7
    mc "Not at all."
    mct "Unfortunately..."
    show eec 6
    ca "In that case... I will allow it, despite its impropriety."
    show eec 7
    mc "*Chuckles* Thank you for letting me dream, my Princess."
    mc "Your generosity knows no limits."
    show eec 6
    ca "Well then, enlighten me. What occurred in this dream of yours, and what role did I play in it?"
    show eec 7
    if lunapath or lunaunclehouse:
        mc "Well technically it wasn't a dream, more like a hallucination. We call it a “bleeding case”."
    else:
        mc "It happened during a day I was alone at home and didn't have much to do."
        mc "I think I fell asleep on the couch or something, I don't remember it exactly."
    mc "I saw the inn where you've been lodging in Ekabar, and you were there with the innkeeper."
    mc "He asked you to pay, and then you got all mad and threatened him with your lightning magic."
    mc "It was pretty funny."
    show eec 8
    ca "So... reminiscent of actual events?"
    show eec 9
    mc "*Chuckles* Something similar happened? Did you have trouble with the innkeeper?"
    show eec 8
    ca "Yes. He disrespected me, and I had to remind him who he was dealing with."
    ca "Then you appeared out of nowhere, but left using vanishing magic without giving any sort of explanation."
    show eec 9
    mc "What...? I don't have any vanishing magic."
    mc "When did this happen?"
    show eec 8
    ca "Several moons ago."
    show eec 9
    mc "(Several moons ago? Could I have fallen asleep wearing the E-suit and visor again?)"
    if lunapath:
        mct "No, that can't be. I was on my way to Luna's uncle's house. I didn't even have them with me."
    else:
        mct "No, that can't be. I remember I didn't play Eternum that day."
    mc "Nah, it's impossible."
    mc "You must be mistaking it for the time I went there with Alex."
    show eec 8
    ca "No... you were alone. You said–"
    stop music2 fadeout 5
    play soundloop wind volume 0.4
    play sound revolver2
    show eec 10 with hpunch 
    play sound3 glassbreak
    play sound2 revolver2
    pause .7
    mc "Shit, did those gunshots come from the store where the deputy is?"with dis
    show eec 11
    ca "I believe so, yes..." 
    show eec 10
    mc "Maybe he's in trouble?"
    play sound chair2
    show eec 8b
    ca "*Standing up* Perhaps with the man you're looking for?"with dis12
    mc "El Coyote? Fuck, could be possible."
    mc "Let's take a look."
    stop soundloop fadeout 6
    play sound dooropenclose
    show eec 13 with dis2
    play music2 ["<silence 1>"]
    queue music2b western3 fadein 3 volume 0.9
    bla "You enter the store and find the Sheriff's deputy with his hands up." with dis 
    mc "Um... is there a problem, sir?"
    show eec 14
    gsc "Oh, there is definitely a problem. This man is trying to rob me!"
    show eec 12
    sd "I'm not robbing you, you dumbass!"
    sd "You've been renting this space for your store for a while now and it’s about time you’ve paid your property taxes just like everyone else!"
    show eec 14
    gsc "First, you steal our lands from us, and now you want us to pay YOU for utilizing it?!"
    gsc "Over my dead body! Do you know how long my ancestors have dwelled in this area?!"
    show eec 12
    sd "Cut the shit, Brendan, you're from Queens!"
    show eec 14
    gsc "You're offending my Wamapoke roots!"
    show eec 12
    sd "That's not even a real tribe!"with hpunch
    play sound2 holster2
    show eec 14
    gsc "Wallaho mahk-a-tokeh!"with hpunch 
    show eec 15
    mc "Okay, hold your horses! The deputy is right, Brendan."
    mc "And threatening a law enforcement officer is a crime punishable by hanging."
    mc "Let's not do anything stupid and settle this thing like the gentlemen we are, shall we?"
    gsc "Hmmmm..."
    mc "You’re gonna pay your taxes, but the deputy is going to be a kind-hearted soul and give you a couple more weeks to gather the money."
    mc "Now do we have ourselves a deal?"
    gsc ". . ."
    show eec 14
    gsc "And I want a 20%% discount!"
    show eec 12
    sd "What?!"
    show eec 14
    gsc "20%%! Call it a reparations reduction! Otherwise I’ll start blastin’!"
    show eec 12
    sd "Agh, okay, FINE!"
    show eec 15
    sd "Just lower your gun already, would you?"
    play sound holster
    show eec 16
    gsc "Ah, excellent deal, excellent! I can already feel the warmth of my ancestors smiling down on us." with dis
    gsc "It wasn't so hard, see?" 
    show eec 17
    sd "*Sighs* Idiot..."with dis12
    sd "Thank you for your help, citizen."
    show eec 18
    mc "No problem, sir."
    mc "And nice to meet you. My name is [mc]."
    show eec 17
    sd "Tony Mack, I'm the Sheriff's right-hand man."
    sd "How can I help you today?"
    show eec 18
    mc "We're looking for an outlaw called “El Coyote”. He's in possession of... an item we need."
    show eec 17
    sd "Ah... that bastard and his gang have been giving us problems ever since I arrived on this server."
    sd "I know where he could be hiding."
    show eec 18
    mc "Wow, really?!"
    mc "That would be really helpful."
    show eec 17
    sd "Come with me to the Sheriff's office."
    sd "There's a map there somewhere... if we manage to find it between all the whiskey bottles that man leaves around the place."
    show eec 18
    mc "Thank you very much!"
    show eec 18b
    ca "May I ask something?" with dis
    show eec 18c
    sd "Sure thing, ma'am."
    show eec 18b
    ca "I saw a lot of cattle in the town, unprotected."
    ca "Is there no risk of dragon attacks in this area?"
    mc "Um..."
    show eec 18c
    sd "Ah, excellent question, ma'am."
    mc "Is it...?"
    sd "You must be new to Eternum. There are no dragons on this server."
    sd "No magic or fantasy elements either."
    sd "I can give you a quick summary, if you want."
    mct "Oof, that was close."
    play soundloop twirl fadein 2 volume 0.7
    show eec19
    gsc "*Spinning his revolver* If you're worried about dragons, I sell a very powerful repellent, ma'am." with dis12
    mc "Don't try to scam us, asshole."
    mc "And put that thing down before you kill yourself."
    gsc "Do you smoke? I sell the best tobacco in all of Blackridge too."
    mc "We don't want anything. And where did your accent go? Did you suddenly forget about your Wamapoke roots?"
    gsc "I'm a–"
    stop soundloop
    play sound revolver2
    play sound2 revolver
    play sound3 shotgun
    scene eec23 with hpunch
    pause .1
    play sound gundrop
    scene eec 24 with dis
    mc "ARGH! Y-YOU SON OF A BITCH!"with dis08
    mc "I TOLD YOU!"
    mc "You could have hit someone!"
    play sound4 woodhit
    play sound5 fall2
    play sound6 fall3
    play sound3 wood
    play sound7 blood2
    show eec 25 with dis
    pause 
    show eec 26 with dis12
    mc "*Turning around* Oh shit..."with dis
    show eec 27 with dis12
    mc "OH SHIT." with dis
    mc "C-Calypso?! Are you okay?!"
    ca "Eh...?"
    mc "*Sigh of relief* Oof, thank god."
    ca "What... happened...?"
    mc "Um... t-there was an accident. This idiot fired his gun by mistake and he hit the deputy."
    mc "You'll have to use your magic to get rid of the mess."
    play sound polyjuice
    show eec 28 with dis2
    mc "Oh..."with dis
    mc "I guess you can only get rid of the stuff on your clothes..."
    gsc "Wow, neat illusion!"
    mc "You better shut the fuck up!"
    scene eec29
    ca "*Shivering* I-I am covered in the blood of a peasant."with dis14
    ca "My pure and sacred skin is ruined..."
    ca "I HAVE... THE FLUIDS... OF A LOW-BORN PLEBEIAN... ON MY FACE."
    scene eec 31
    gsc "Okay, okay, let’s just calm down. I know what to do, this isn’t my first rodeo."with dis
    gsc "First of all, the Sheriff can't know about this, so let's keep our mouths shut, yeah?"
    gsc "Secondl–"
    play sound implode
    scene eec 32 with Dissolve(.9)
    play sound2 debris
    scene eec32 with hpunch
    pause .7
    play sound7 steam2 fadein 3 volume 0.5
    scene eec 34
    ca ". . ." with dis15
    play sound3 swallow
    mc "*Gulps* O-Okay, I remember seeing a hotel offering bath services above the saloon."
    mc "I can take you there."
    scene eec29
    ca "Yes. Please. I need to wash this filth off me immediately." with dis12
    ca "Please help me."
    mc "Don't worry, Princess, you'll be as good as new after this!"
    mc "I bet that bathroom is going to look like heaven on earth!"
    mc "Follow me!"
    stop music2b
    play sound bellscary volume 1.2
    scene eec 35
    play music2b ["<silence 1.5>"]
    queue music2b western3 fadein 5
    pause 
    show eec 36
    ca "*Whining* W-What is this...?"with dis12
    ca "What sort of sorry excuse is this?!"
    show eec 37
    mc "Um... their deluxe bath service, I guess."
    show eec 36
    ca "Deluxe? How can they call this {i}deluxe{/i}?"
    ca "Does this word have another meaning in your world?"
    show eec 37
    mc "Come on... it's not that bad."
    show eec 36
    ca "Not that bad??"
    ca "My pet unipony used to have a bigger pool than that. And much cleaner!"
    show eec 37
    mc "But it's still got what counts – hot water and soap!"
    mc "And... you hear that? You got yourself some relaxing background music from the piano player in the saloon below!"
    mc "This place just keeps getting better and better, if you ask me."
    show eec 36
    ca "*Taking a deep breath* Okay..."
    ca "I can do it. I have endured worse challenges."
    ca "But I need you to stay and protect me while I bathe."
    show eec 39
    mc "Huh...? You want me to stay... here? With you?" with dis14
    show eec 38
    ca "I mean... y-yes, but do not allow your head to become filled with any strange or perverted ideas."
    show eec 39
    mc "No, no... not at all. I'm just honored."
    mct "Oh boy... am I gonna see Calypso naked?!"
    show eec 38
    ca "You must face the wall during the entire duration of my bathing."
    ca "If you dare to turn around, I will obliterate you as I did with the store owner."
    show eec 39
    mc "Oh..."
    mct "Goddammit."
    mc "Well... I guess I can wait right outside the door, if that’s the case."
    show eec 38
    ca "No, you need to be in here."
    ca "This place is absolutely barbaric. In the short time I have been in this town, I have seen FOUR people meet their death already."
    show eec 39
    mc "I'm pretty sure you could defend yourself from any possible danger without my help."
    show eec 38
    ca "Bathing is a sacred and cherished time for my people."
    ca "It is not merely a physical activity, but a cherished ritual."
    ca "We connect with the elements and purify our body and spirit as we step into the gentle embrace of the water."
    ca "I cannot hear the melody of nature if I have to constantly worry about possible assailants."
    show eec 39
    mc "Um... I see."
    menu:
        with dis
        "Stay and protect the Princess [calypso_pts]":
            $ calypso_interest += 1
            mc "Well, as you wish, my Princess."with dis08
        "Leave [mt](Closes her path)":
            mc "But... as exciting as spending 20 minutes facing a wall sounds, I'd rather go help Alex or Dalia."with dis08
            ca "*Grumbling* Hmph."
            show eec 38
            ca "Alright..."
            ca "I guess... you have a point. I don't need you."
            ca "Go help Dalia and Alexandra."
            ca "I will meet you all again after I am done here."
            show eec 39
            mc "Sounds good, see you then!"
            mc "Enjoy your bath, Princess."
            ca "Hmm."
            $ calypsopath = False
            jump secondmenuwestern
    mc "I'll stay to protect you."
    show eec 38
    ca "Thank you."
    show eec 35 with dis12
    mc "Can I at least look through the window instead of at the wall?"with dis08
    ca "Hmm... I will allow it."
    mc "Thank you, Princess. Your generosity knows no bounds."
    stop music2b fadeout 4
    scene black with dis2
    show screen afewminuteslater with dis12
    pause
    play music2 saloon2 fadein 4
    hide screen afewminuteslater
    scene eec 40 
    with dis2
    pause 
    play sound bubbles
    play sound2 water3
    play soundlow drips
    show eec 41 with dis12 
    ca "*Getting her head out of the water* MMmmmmm..."with dis
    mc "Better?"
    mc "You sound very relaxed."
    ca "Mm-hm..."
    mc "I guess you owe this hotel an apology after all."
    play sound3 water
    show eec 42
    ca "*Soft chuckle* I guess I do."with dis12
    ca "The temperature of the water was surprisingly perfect. And this place carries good aromas, despite the sub-standard first impressions of the bathroom."
    show eec 43
    mc "Well, I'm happy to hear that."
    mc "Did you manage to clean off all the blood?"
    show eec 42
    ca "I did, thank you."
    show eec 43
    mct "Damn, she wasn't lying about bathing being a whole ritual for her."
    mct "She spent like 10 minutes in silence, but now even her voice tone has changed. She sounds surprisingly warm."
    show eec 42
    ca "How were the views?"
    show eec 44
    mc "*Looking out the window* Captivating."
    mc "I counted 2 carriages and 9 horses."
    mc "There's also this damn Praetorian interrogating all the players that pass through this street. Quite a show."
    if not westernalex: 
        mct "I guess they haven't found the corpse yet."
    play sound water
    show eec 45
    ca "*Looking at the other window* Do you think they could also be here looking for the Gem?" with dis12
    mc "Nah, it's not that. It's them who started the whole Gems of Doom event in the first place."
    mc "Well... the Founder did. Idriel. Ulysses?"
    mc "I honestly don't even know how many sides there are in this story anymore."
    mc "In any case, we must gather the 10 Gems, that's all I'm sure of."
    play sound2 water
    show eec 46
    ca "*Reclining in the tub* Yes... just give me 5 more minutes and we can continue our search."with dis12
    show eec 47
    mc "*Chuckles* You sure weren't lying about your love for bathing."
    show eec 46
    ca "Of course. All our people love it, we cannot help it."
    ca "They say it's an instinct inherited from Anima."
    show eec 47
    mc "Anima?"
    show eec 46
    ca "You know, Queen Anima the Radiant."
    show eec 47
    mc "Never heard of her."
    play sound water2
    show eec 49 
    ca "What? Are you serious right now?"with dis12
    ca "You do not know of Lady Anima?"
    show eec 50
    mc "Her name doesn’t ring a bell."
    show eec 49
    ca "First Queen of the Sy-tel-quessir, Herald of the Elven Court, Guardian of the Forests, Warden of the Eternal Soul?"
    show eec 50
    mc "Um... nope, sorry."
    play sound water
    show eec 46
    ca "Wow... even the silliest goblin of Hyril'ar has heard of Anima."with dis12
    ca "As a child, I was enthralled by the stories my mother shared about her."
    show eec 47
    mc "Really? And what's her story?"
    show eec 46
    ca "She... well, she was our first queen. She started the elven dynasty and it is said she is the source of our magic."
    ca "You are probably not interested in the long version."
    show eec 47
    mc "I {i}am {/i}interested."
    mc "I want to learn more about you, your culture, and your past."
    mc "Everything about you and what surrounds you is... fascinating."
    mc "And well, it's not as if I can do much else right now except for looking through this window."
    mc "That is... unless you allow me to turn around and get a glimpse of the princess's exquisite naked grace, of course..."
    show eec 44
    ca "Oh [mc], how you humor me. Very well, I will grant your request. About the story. Now pay attention."with dis12
    ca "We must go back beyond the annals of the Second Age, to an era veiled in the mists of forgotten memory."
    mct "I was hoping my flirtatious charm would’ve had a greater effect."
    ca "Now close your eyes."
    mc "Why?"
    ca "That's how my mother used to tell me stories."
    ca "Close your eyes and let the water embrace you."
    scene black
    mc "*Closing your eyes* I'm not even bathing, but... alright." with dis08
    ca "Try emptying your mind and imagining a land still blanketed in an aura of untamed wilderness, with rising kingdoms sprinkled throughout."
    stop music2 fadeout 5
    play soundlow whoosh8
    scene tale1 with disrem
    play music calypsotale fadein 6
    pause 
    "{i}{font=tales5.ttf}{size=45}Many centuries ago, the kingdom to which I belong needed no introduction to any man."with dis
    "{i}{font=tales5.ttf}{size=45}Its prestige and beauty served as the foundation for many legendary tales told, whether from the cracked lips of the poorest farmhand or from the gluttonous mouth of the wealthiest lord."
    "{i}{font=tales5.ttf}{size=45}Its power swept far throughout lush forests, majestic rivers, and many bustling cities to reach the furthest ends of the land."
    "{i}{font=tales5.ttf}{size=45}At the heart of this mighty realm stood a magnificent castle, and within it reigned a beloved king. This king had five boys, and the youngest of them was named Yliar."
    "{i}{font=tales5.ttf}{size=45}Legend has it that Yliar was the only one of the five to be born during a full moon, which might have explained why he strayed so far away from the graceful and gallant dispositions of his brothers."
    "{i}{font=tales5.ttf}{size=45}Despite the differences, the king adored the reckless and impulsive Yliar and favored him amongst the others."
    "{i}{font=tales5.ttf}{size=45}The young prince knew this, and often used the favor to his advantage..."
    show tale2 at distale
    "{i}{font=tales5.ttf}{size=45}One fateful day, against the orders set by his father the king, Yliar ventured deep into the enchanted forest on the outskirts of the kingdom."
    "{i}{font=tales5.ttf}{size=45}While he navigated through the thick underbrush, he followed a rainbow of light from behind some distant trees and discovered a small, quaint clearing with a tranquil pond in the center."
    "{i}{font=tales5.ttf}{size=45}However, it was not the pond which caused such a stir... it was the beautiful, elven woman who stood in the middle of it."
    "{i}{font=tales5.ttf}{size=45}Equipped with the royal education instilled in him since he was young, he knew of the powers the elven witches of the forest possessed, and soon the realization of incredible opportunity dawned upon him."
    "{i}{font=tales5.ttf}{size=45}Yliar soon uncovered the witch's exceedingly rare talent to connect alternate worlds, which presented him with the opportunity to amass immeasurable riches across infinite realms."
    "{i}{font=tales5.ttf}{size=45}He promised her a life of pure joy and happiness beyond her wildest dreams, but in exchange... she needed to reciprocate by sharing her mystical abilities with him."
    "{i}{font=tales5.ttf}{size=45}As the fantasies of a love-filled life flashed before her eyes, she cheerfully agreed and surrendered her magic to him."
    "{i}{font=tales5.ttf}{size=45}But... little did the witch know... she had fallen deep into a twisted web of dark deception."
    hide tale1
    show tale3 at distale
    "{i}{font=tales5.ttf}{size=45}Yliar, suddenly invigorated with the newfound powers, grabbed the witch and restrained her. He forced her to obey his wishes and surrender her free will, while remaining at his side like a pet."
    "{i}{font=tales5.ttf}{size=45}They returned to his family castle, and before the king could ask any question of his son, the prince murdered him in cold blood... alongside his four older brothers."
    "{i}{font=tales5.ttf}{size=45}Yliar placed the seized crown upon his head and ascended to his new throne. With every life he extinguished, the young prince only felt his thirst for power grow deeper and deeper."
    "{i}{font=tales5.ttf}{size=45}The people of Hyril’ar, without any protector and feeling so dearly helpless, had no choice but to bend the knee to their new king."
    "{i}{font=tales5.ttf}{size=45}They lived in awe and fear of their new ruler, while Yliar relished in the realization that now no one stood in his way. He thought himself to finally be invincible."
    hide tale2
    show tale4 at distale
    "{i}{font=tales5.ttf}{size=45}Nevertheless, one day, a mysterious man arrived at the grand entrance of Yliar’s castle and demanded an audience with the king."
    "{i}{font=tales5.ttf}{size=45}Yliar, seeking to quickly get rid of this sudden annoyance, entertained the stranger’s request."
    "{i}{font=tales5.ttf}{size=45}To his astonishment, the unknown man questioned the legitimacy of Yliar’s rule in front of the whole court and challenged the king to a duel."
    "{i}{font=tales5.ttf}{size=45}Amused at the audacity of this man, the king scoffed and decided to accept the man’s challenge, completely confident in his supremacy."
    "{i}{font=tales5.ttf}{size=45}As Yliar well knew, the Hyril’ar Seers had foretold years ago that only a person holding royal blood within their veins would be capable of harming the unrivaled king."
    "{i}{font=tales5.ttf}{size=45}This prophecy, however, was dismissed by the masses and the king himself, as all those with royal blood had perished at the hands of the man currently holding the throne..."
    hide tale3
    show tale5 at distale
    "{i}{font=tales5.ttf}{size=45}The challenge of combat quickly began in the Royal Courtyard, as the audience watched with bewilderment."
    play sound thunder fadein 5
    "{i}{font=tales5.ttf}{size=45}Yliar, eager to make an example of this man, conjured the powers he drained from the elven witch and struck the challenger."
    "{i}{font=tales5.ttf}{size=45}However, much to the king’s disbelief, the mysterious visitor absorbed the magic and channeled it back onto Yliar, striking him suddenly and causing him to fall back onto the floor."
    "{i}{font=tales5.ttf}{size=45}The entire court gasped, having never seen another human wielding magic before, and watched in amazement as Yliar had finally met a worthy opponent..."
    "{i}{font=tales5.ttf}{size=45}And eventually... his own defeat."
    "{i}{font=tales5.ttf}{size=45}The victorious man proved to be a stark contrast to the befallen ruler, and he was quickly proclaimed by the masses as their new king."
    hide tale4
    show tale6 at distale
    "{i}{font=tales5.ttf}{size=45}In a twist of fate, the man took the defeated king’s former captive and married her, promising the witch to always safeguard her ultimate yearning in life... her freedom."
    "{i}{font=tales5.ttf}{size=45}Now known as Anima the Radiant, the witch who was suddenly elevated from captive to royalty finally found herself at last in the life she had fantasized about before..."
    "{i}{font=tales5.ttf}{size=45}One of unrelenting love and boundless happiness beyond her wildest dreams."
    "{i}{font=tales5.ttf}{size=45}Together, the two rulers ushered in a new era for the realm and established the noble dynasty of the Sy-tel-quessir."
    "{i}{font=tales5.ttf}{size=45}A lineage that endures to this very day, with each of its members serving as stewards of justice, harmony, and compassion throughout all the lands of Hyril’ar."
    stop music fadeout 7
    play soundlow whoosh8
    scene eec 48 with disrem
    play music2 saloon2 fadein 9
    pause
    scene eec 47
    mc "Wait, wait, wait... let me recap."with dis 
    mc "This witch and the mysterious man... are they supposed to be your ancestors?"
    show eec 46
    ca "They are."
    show eec 47
    mc "So your forefather was... human?!"
    show eec 51
    ca "O-Okay, I see where you are heading with this."with dissolve
    ca "First and foremost, Queen Anima's spouse was an Eldari. They look like humans, but they are a distinct race."
    ca "Not only do Eldari possess an extended lifespan, spanning centuries, but they also possess magical prowess comparable to that of pure-blooded elves."
    ca "And secondly, Anima's lineage was so exceptionally unadulterated that all her descendants were unequivocally regarded as pure elves too."
    show eec 47
    mc "I don't know... to me it sounds like your ancestor shared your same fascination for the human race."with dissolve
    show eec 51
    ca "I said he was not human!"with dissolve
    ca "And... I-I am not fascinated by anything."
    show eec 47
    mc "*Chuckles* Okay, okay, I'll take your word for it."with dissolve 
    mc "Seriously though, that was a great story. Your culture and history is completely captivating, it sounds like a fairy tale."
    mc "When did this happen?"
    show eec 46
    ca "Tens of thousands of years ago. Queen Anima reigned over Hyril'ar for millennia."
    ca "She built the Elven Grand Library, reclaimed the Lost Territories, and expanded the borders of the Alliance to unsuspected limits."
    show eec 47
    mc "And what about her husband? How did he manage to defeat Yliar despite the prophecy? Did he actually have royal blood?"
    show eec 46
    ca "He died long before Queen Anima, so we do not know so much about his life. And the information about him differs depending on who tells the story."
    ca "Some say he was a lost brother, some say he was Yliar's bastard son, and others say he was a royal from another realm."
    show eec 47
    mc "Another realm?"
    mc "Could many people travel to other worlds creating portals like you do?"
    show eec 46
    ca "Only Anima could. That is why she was even considered a deity in some regions."
    ca "I was the first and only descendant of Anima who inherited this ability."
    show eec 47
    mc "Wow... that's incredible."
    mc "I'm glad to have a goddess on our side."
    show eec 46
    ca "*Snorts* I am no goddess. My abilities pale in comparison to what Queen Anima could do."
    show eec 47
    mc "Still, I'm glad to have you with us."
    show eec 46
    ca "Well, let us not forget that I still owe you my life."
    ca "I will not consider myself absolved of this debt until I have repaid the favor in kind."
    show eec 47
    mc "Come on, you've helped us a lot already."
    show eec 46
    ca "It's still not comparable to setting me free from my confinement."
    show eec 47
    mc "But I don't want you to feel obliged to help us. I’m not trying to be like the evil king in your story, dragging you along as his pet or something."
    show eec 46
    ca "I am committed to cooperate with you in any way necessary until you deem that the debt has been sufficiently settled, as it is a matter of my personal integrity and honor."
    show eec 47
    mc "Hmm..."
    mct "Should I try to tease her again?"
    mct "Since she’s in a better mood after that bath, maybe she’ll be more playful to my “charm”. And... the situation calls for it, to be honest."
    menu:
        with dis
        "[gr]Tease her":
            mc "Well, if you insist... let's do something."with dissolve 
        "Let it go":
            mct "I've probably risked enough for today."with dissolve
            mc "Well, in that case, we should go help Alex and Dalia. The Gem is still out there somewhere."
            show eec 46
            ca "Indeed. You should go."
            ca "I will stay here for a few more minutes."
            show eec 47
            mc "Are you sure?"
            show eec 46
            ca "Certainly. I appreciate your assistance, though."
            ca "I will meet you all again after I am done."
            show eec 44
            mc "Alright then."with dis
            mc "Enjoy the rest of your time in humankind's eighth wonder of the world – the most prestigious and opulent bath house to ever exist!"
            ca "*Soft chuckle* Thank you, I will."
            mct "Hey, I got a chuckle!"
            mct "Keep grinding, [mc]..."
            jump secondmenuwestern
    mc "If you allow me to finally turn around right now and catch a glimpse of the princess's flawless form... I'll free you from your... “debt”."
    play sound water3
    play sound2 drips
    play sound3 bubbles
    stop sound2 fadeout 5
    show eec 52
    ca "*Sitting up* Are you aware that just making such a proposition could result in a ruling of death within the Hyril'ar Court?" with dis12
    show eec 53
    mc "Hey, no risk, no reward. I like to live dangerously."
    mc "All I wish is to see what lies beneath the Princess’ royal attire... to see you in all of your magnificent splendor."
    mc "Is it too much for this devoted servant to ask of?"
    show eec 52
    ca "Indeed, it is."
    ca "You are lucky I have not vaporized you yet."
    show eec 53
    mc "*Speaking dramatically* Bards have crafted songs about your unparalleled beauty. And I am but a mortal enthralled by your grace."
    mc "*Speaking dramatically* Can you blame these lowly eyes for wanting to gaze upon that which is heavenly?"
    show eec 43
    bla "Calypso lets out a soft, yet playful chuckle."with dis08
    show eec 42
    ca "Your eloquent words will not change anything."
    ca "And you have never heard any of those songs you speak of."
    show eec 43
    mc "But they {i}do{/i} exist, then!"
    show eec 54
    ca "Hmm..."with dissolve
    show eec 42
    ca "Well... perhaps a few."with dissolve
    ca "But that is irrelevant."
    ca "No human has ever laid eyes upon my naked body, and I do not plan to change that today."
    ca "They are not even permitted within the castle! All my maids are of pure elven lineage."
    show eec 43
    mc "That's exactly the point!"
    mc "If it wasn't such a rare privilege, it wouldn't be worth absolving you from your debt."
    show eec 42
    ca "My maids always warned me that human males were lustful and insatiable barbarians."
    ca "It seems they were not mistaken after all."
    show eec 43
    mc "Lustful and insatiable, perhaps, but also with a heart of gold!"
    show eec 42
    ca "*Soft chuckle* Yes, I suppose so."
    show eec 43
    mc "Ah, I got another chuckle from the Princess herself!"
    mc "I'm on a roll."
    show eec 42
    ca "You have always treated me with respect, I must acknowledge that."
    show eec 43
    mc "I'd never do something that could compromise your integrity or honor."
    mc "You know it, Calypso."
    mc "In all seriousness now, I like to think that we're helping each other to achieve our respective goals. We're a team."
    ca "Hmm."
    show eec 42
    ca "Yes. I like that vision too."
    show eec 54
    ca "Mmm..."with dis08
    show eec 44
    mc "Anyway, I should really get going now."with dis
    mc "We're running out of time and that Coyote dude could be planning to grab his things and escape to another server."
    stop music2 fadeout 14
    play sound water2
    play sound2 drips
    play sound3 bubbles
    play sound4 drips
    bla "You hear Calypso coming out of the water behind you."with dis
    ca "Very well, Mr. Insatiable Barbarian with a heart of gold..."
    mc "Yeah...?"
    ca ". . ."
    ca "I do not have all day."
    mc "D-Does this mean what I think it means?"
    ca "You are forbidden from ever disclosing this incident to anyone else, do you understand?"
    mc "A-aha."
    ca "If you accept that precondition, then yes... you may turn around."
    play music2b calypsolewd fadein 9
    scene calywest1 with dis17
    pause 8.5
    scene eec 55 
    mc "Oh sweet lord..."with dis
    mct "Look at that body..."
    mct "My god, her breasts are absolutely perfect, just as I imagined."
    mc "I can't believe I'm seeing this."
    play sound water
    show eec 58 with dis12
    ca "*Sitting on the corner of the tub* Yes... I cannot believe I am letting you see it either."with dis06
    ca "Maybe all this time spent among commoners is muddying my temperament."
    show eec 56
    mc "Ah... you ended up becoming fond of me, didn't you?"
    show eec 57
    ca "I ended up taking pity on you, more like."
    ca "This is what you were yearning for, so... I suppose I can grant you that wish."
    show eec 56
    mc "And it's even better than I imagined... I officially release you from your debts."
    show eec 58
    ca "Remember, you must keep your mouth shut."
    ca "If word gets out that I revealed myself to my human squire, it would ruin my reputation... for a few decades at least."
    show eec 56
    mc "My lips are sealed, my Princess."
    show eec 57
    ca "They better be."
    ca "I am committing quite a sacrilege here."
    ca "My old Tutor of Elegance and Virtue would be horrified if she discovered I'm doing this."
    show eec 56
    mc "God, everything you say excites me more..."
    mc "Don't you feel the same?"
    show eec 57
    ca "Hmph. What I feel is... contradiction."
    ca "Many Lords in Hyril'ar would surrender all their possessions just to see what you are seeing right now, you know?"
    ca "And here I am... showing myself in my purest form to a mere mortal."
    show eec 56
    mct "She keeps insisting on that, but her subtle smirk tells a different story. I can tell she's taking pleasure in breaking her royal protocols..."
    mc "Don't worry, it'll be our secret."
    mc "And besides, I didn't even touch you, so... no purity or virtue was lost."
    mc "Unless..."
    show eec 57
    ca "Hah, you better not continue that sentence."
    play sound water
    play sound2 wood fadein 1
    show eec 59 with dis14
    ca "*Standing up* No human has ever touched me, and none ever will."with dis
    ca "That is a line I will never cross."
    mc "What if it's you who touches me instead...?"
    show eec 61
    ca "Same thing applies."with dis12
    show eec 60
    mc "I see... that's too bad."
    mc "I'll use the few seconds I have left to admire your beauty a bit more, then."
    ca "Hmm."
    mct "Jesus, she really has a spectacular body."
    mct "Is it bad that I want to grab the Princess and completely {i}destroy{/i} her against that rotten cabinet? Might as well make even more of a mess in here..."
    mct "My god, my pants are about to explode."
    show eec 61
    ca "Well, now it is your turn to get undressed."
    show eec 60
    mc "I'm sorry?"
    show eec 62
    ca "What do you mistake me for, some kind of common harlot who gets naked without reciprocation? Nonsense!"with dis08
    ca "You need to undress for me as well."
    show eec 60
    mc "I thought you were granting my wish."with dis08
    show eec 62
    ca "And I still am."with dis08
    ca "You are forgetting who you are dealing with, [mc]. I am an heir to the Hyril’ar Realm and there are different protocols with me."
    show eec 60
    mc "That's a fair point, I guess."with dis08
    mct "She really wants to keep a high profile all the time, eh? To keep her superior social status in check."
    mct "Alright, I can play her game."
    mct "I've never been one to feel ashamed of my physique, and now that I look even more muscular, it only strengthens my confidence."
    mc "Very well."
    mc "Your wish is my command, my Princess."
    play sound belt
    show eec 63
    bla "You slowly begin to undress while Calypso gazes at you."with dis15
    play sound2 clothes4
    play sound3 clothes3
    show eec 64 with dis15
    pause .3
    mct "Dammit... I thought that if I took my time undressing, my erection would go away." with dis12
    mct "This might be awkward..."
    show eec 66
    ca ". . ." with dis12
    play sound5 clothes
    mc "*Finishing undressing* Well... it's done. Equal conditions."
    show eec 67
    ca "Holy Mother of Turska... what is that??"with dis12
    show eec 68
    mc "Um..."with dissolve
    mc "Yeah... s-sorry about that. I know erections are probably... out of protocol."
    mc "I couldn't help it."
    show eec 67
    ca "I mean..."with dissolve
    ca "You are... better-endowed than what I imagined."
    ca "Are you... half-orc, perhaps?"
    show eec 68
    mc "Um... nope, only human."with dissolve
    show eec 67
    ca "Are you sure?"with dissolve
    show eec 68
    mc "Yeah, pretty sure. No orcs in my family that I know of."with dissolve
    show eec 67
    ca "I see..."with dissolve
    mct "God, her short glances to my cock are turning me on so much..."
    show eec 68
    mc "You seem quite enthralled by my naked body, Princess."with dissolve
    mc "Isn't your gaze upon my intimate areas also a breach of protocol?"
    show eec 69
    ca "P-Please, I am not e-enthralled by anything."
    ca "Although... I will admit that the whole situation is {i}certainly{/i} out of protocol, yes."
    show eec 68
    mc "You can look at it. I don't mind, really."
    show eec 69
    ca "I have looked at it enough."
    ca "I was just surprised because... it doesn't match your skinny physique, that is all."
    show eec 68
    mc "Hey, I'm not skinny!"
    show eec 69
    ca "Please... Hyril'ar elite guards probably weigh twice as much as you."
    ca "{i}That{/i} is a strong male."
    show eec 68
    mc "But muscles don't always equal strength. I'm likely stronger than them."
    show eec 69
    ca "I highly doubt it."
    ca "General Arannis once carried me all the way back to the castle from the Eldermoor Huntlands when my horse ran away."
    show eec 68
    mc "I don't know how far that is to the castle, but I'm sure I could do that too."
    show eec 69
    ca "*Huffing* If you say so..."
    ca "I will keep it in mind if we ever find ourselves in a similar situation."
    show eec 68
    mc "I'd be happy to show you how strong and vigorous I can be..."
    show eec 70
    ca "You know, I decided to tolerate your indecent innuendos given the situation we are in since they're almost... endearing."with dis12
    ca "But I must warn you, they are about as futile as a dwarf's attempt to outrun an elven archer."
    ca "No human will ever touch me."
    ca "Not now, not ever."
    show eec 71
    mc "But I touched you already. Several times."
    show eec 70
    ca "Hmph. Fair, I guess. No human will ever touch me {i}below my shoulders{/i}, since you prefer to nitpick."
    show eec 71
    mc "I gotta say, today has made me regret being human like never before."
    show eec 70
    ca "I will not blame you for the shortcomings of your race."
    ca "And neither should you."
    ca "Even if we set aside the stark contrast in our social classes, a human would never be able to endure an elven woman."
    ca "It is just how it is."
    show eec 71
    mc "*Chuckles* Okay, now you're clearly underestimating me."
    show eec 72
    ca "Please..."
    show eec 71
    mc "Oh, is that a challenge...?"
    show eec 72
    ca "*Soft chuckle* If we were in Hyril'ar, I might even consider allowing you to test yourself with one of my maids."
    ca "Some of them would surely agree purely out of a morbid fascination with the idea."
    show eec 71
    mc "That sounds incredibly hot, but... I could definitely “endure” even an elven princess."
    show eec 72
    ca "Please, spare yourself the embarrassment."
    ca "You would be finished before even starting."
    show eec 71
    mc "Hah! Who do you take me for? That's not true!"
    show eec 72
    ca "If I wanted to, I could make you finish without touching you."
    show eec 71
    mc "Not true."
    show eec 72
    ca "In less than a minute."
    show eec 71
    mc "Not true."
    ca ". . ."
    show eec 73 
    ca ". . ." with dis12
    play sound beat
    play sound2 whoosh7
    scene eec74 with Dissolve(.3)
    scene eec 74
    bla "An intense tingling runs through your body." with dis12
    show eec 75
    mc "O-O-Ohh... shit, w-what was that?"with dis
    show eec 76 with Dissolve(.1)
    play sound whoosh7
    play sound2 woodhit
    play sound3 fall3
    play sound4 fall
    scene eec77b
    bla "A strong force pulls you down into the floor." with vpunch 
    show eec 78
    mc "W-What's going on?!" with dis14
    play sound5 spell2
    show eec 79 with flashfast
    mc "What the fuck..." with dis06
    ca "You do not seem to fully understand here, [mc], and now I am starting to take it as a personal affront."
    show eec 80
    mc "O-Oh boy..." with dis14
    show eec 79
    ca "So let me stoop to your level here."with dis
    show eec 80
    ca "I could make you {i}ejaculate{/i} without touching your dirty, inferior human body."with dis
    ca "That is how superior the elven race is."
    ca "Was I clear enough now?"
    show eec 79
    mc "I'm sorry, but you're wrong, my Princess..."with dis
    ca "*Playful chuckle* We will see about that..."
    play soundlow penetration2
    play sound grab2
    play sound2 woodhit volume 0.4
    show eec 81
    bla "The surprisingly warm ghostly hand grabs your shaft firmly." with hpunch 
    mc "O-Oh shit...!"
    $ renpy.music.set_volume(1.0, channel='soundloop')
    $ renpy.music.set_volume(0.3, delay=10.0, channel='music2b')
    play soundloop wetting2 fadein 3
    scene calywest2 with dis22
    mc "O-O-Ohhh my god..."with dissolve 
    mc "W-What the hell is this...?!"
    ca "*Giggles* Elven magic."
    mc "Ahhh... fuck, your mages sure know the best spells..."
    mct "What in the world?!"
    mct "This doesn't feel like a normal handjob..."
    mct "It doesn't even feel like a hand. It feels as if my whole cock was embraced by something... warm... and incredibly tight..."
    mct "Fuck, she's squeezing it so hard that she'll make it explode..."
    ca "All well down there, [mc]? You seem to be struggling."
    mc "P-Pretty well, yes."
    mc "I've never been... aaahhh... b-better."
    mct "Fuck, I'm gonna cum..."
    mct "FUCK, am I gonna cum already?!"
    mct "No, no, no, I can't give her that satisfaction..."
    scene calywest3 with dis22
    mc "Aaaahhh... holy fuck..." with dis
    mct "Okay... yeah..."
    mct "That's it... you can hold it, [mc]..."
    mct "You can do it."
    mct "Think of ugly things..."
    mct "Nooo... don't look at her, that makes it worse..."
    mct "Don't look at Calypso's perfectly shaped body... her hourglass curves... don't look at her mesmerizing tits..."  
    mct "Fuck..."
    mct "Hold on there, [mc]..."
    mct "Focus on what she’s gonna do next after she gets frustrated that she can’t make you cum without touching you..."
    mct "Y-Yeah, that's it..."
    mct "Her superior status will crumble..."
    mct "Maybe then she’ll want to try harder..."
    mct "And she’ll probably get closer..."
    mct "Oh boy, imagine burying my cock deep inside the Princess' pure depths..."
    mct "Just imagine..."
    mct "Seeing her eyes rolled up with pleasure..."
    mct "BEGGING me for more..."
    mct "And me cumming all over her pretty face..."
    mc "*Muttering* Yeah... you like having fluids of a plebeian on your face now, don't you, Princess...? What a filthy girl..."
    ca "What?"
    mc "E-Eh...? N-Nothing! Nothing!"
    mc "I just... ahhh..."
    mc "Nothing..."
    scene calywest4 with dis2
    ca "Your tenacity is admirable, I must acknowledge that."with dis08
    bla "Calypso boosts her speed, increasing the pressure and warmth of her magic hand even more."
    mc "AAAaahh..."
    mct "Goodness gracious, I can't even move."
    mct "It feels as if my whole body was paralyzed."
    ca "I am surprised by your... endurance."
    mc "T-Thanks."
    mct "If she can really make me feel this way without touching me..."
    mct "How would her actual hand feel? Or her mouth..."
    mct "Her pussy..."
    mc "AAaahh..."
    mct "I wanna sully the Princess so much..."
    mct "I wanna corrupt her..."
    mc "Aaahh..."
    mc "L-Looks like you won't be able to make me “finish” after all, Princess..."
    stop soundloop fadeout 1
    play sound3 penetration2
    play sound5 penetration2
    scene eec 83
    ca "*Clenching her fist even harder* You are restraining yourself." with dis
    mc "*Gritting your teeth* W-W-Well, that's the p-point."
    ca "Do you think you can overpower me?"
    ca "You will see now..."
    play sound spell2
    play sound2 penetration2
    show eec 84 
    bla "Another magic hand appears."with flashfast
    mc "Oh boy..."
    play soundloop wetting1 fadein 2
    scene calywest5 with dis2
    mc "AAAaaaaaugghh..."with dis06
    bla "As Calypso launches her final assault, a torrent of sensations unlike anything you have ever known engulfs you."
    play sound3 penetration2
    play sound5 penetration2
    ca "*Clenching her fists* This has gone on for long enough!"with hpunch 
    mc "Oh FUCK."
    mc "T-This is too much..."
    play sound3 penetration2
    play sound5 penetration2
    ca "Hmmmhhgg..."with hpunch
    play sound3 penetration2
    play sound5 penetration2
    ca "*Grumbling* Release yourself for your Princess!"with hpunch
    play sound3 penetration2
    play sound5 penetration2
    ca "That is an order!"with hpunch
    mct "Oh shit, she sounded so angry, but it was so hot at the same time..."
    bla "With every stroke of the hand, the sensation intensifies, firmly anchoring you to the earth beneath, immobilizing you with overwhelming force."
    play sound3 penetration2
    play sound5 penetration2
    ca "*Grumbling* Why is he not finishing?!"with hpunch
    mc "O-O-Ohh my god..."
    mc "Hhnnnggg..."
    pause
    play sound wood
    scene eec 85
    mc "Oh god..."with dis
    mct "At this rate my balls are gonna explode."
    stop soundloop fadeout 7
    mct "But I did it!"
    mct "I'm not cumming!"
    mct "I won."
    mct "I..."
    mct "Huh...?"
    show eec 86
    mc "She stopped...?" with dis
    scene eec 87
    $ renpy.music.set_volume(0.5, channel='music2')
    $ renpy.music.set_volume(0.5, channel='music2b')
    stop music2b
    play music2 saloon2 
    pause 
    mc "Eh...?"with dis08
    mc "C-Calypso?"
    ca ". . ."
    play sound clothes3
    show eec 88 
    bla "Calypso touches your cock with the tip of her finger." with dis14
    scene calywest6 with dis2
    play sound2 rubclotheslong
    pause 4.9
    stop sound2
    pause .7
    play sound squirt
    play sound2 cum3
    play sound3 cum4
    play sound5 slap1
    scene eec89
    mc "FFFFFFFFFFFUUUCKKKKK...." with vpunch 
    play sound squirt
    play sound2 cum3
    play sound3 cum4
    mc "AAAAAaaaAARgggGGHhh..." with vpunch
    play sound squirt
    play sound2 cum3
    play sound3 cum4
    mc "AAAaaaahhHhh..." with vpunch
    play sound6 woodhit volume 1.1
    play sound7 fall3
    play sound5 fall2
    show eec90
    mc "*Collapsing to the ground* H-Holy Jeebus Harry and Broseph..."with vpunch
    mc "*Catching your breath* God..."
    mc "*Catching your breath* Okay... y-you win..."
    mc "*Catching your breath* Unbelievable..."
    mct "She made me cum with a single finger..."
    mct "Who the hell is this woman..."
    ca "Well... congratulations."
    ca "You forced me to... touch you... directly."
    ca "Your mental fortitude has demonstrated a resilience befitting an elf."
    ca "In the end, it cannot be denied that you possess... a remarkable spirit. Maybe you really are special after all."
    play sound2 clothes
    play sound3 water
    scene eec 56 with dis15
    mc "*Standing up* Wow, that was... s-something."with dis
    mc "I tried my best to prove you wrong, but... y-you really have a formidable magical prowess, Princess."
    show eec 57
    ca "Do not blame yourself. Your capabilities are constrained by the inherent limitations of your lineage."
    ca "Human lustfulness will always be a hindrance for your race."
    show eec 56
    mc "Are you telling me elves never get... horny?"
    show eec 58
    ca "I did not say that."
    ca "We just... learned to control it better."
    show eec 57
    ca "The human lifespan is short. That is why your instincts compel you to... copulate at any available opportunity. To propagate your progeny."
    ca "We, as immortal beings, learned to transcend such primal urges a long time ago."
    show eec 56
    mc "I don't know... your cheeks look even more flushed than before."
    mc "And I'm not sure it's because of the hot water anymore..."
    show eec 57
    ca "I can assure you it is the reaction to the warm water."
    ca "Additionally, channeling magic requires intense physical and mental effort."
    ca "So... be that as it may, my blush is not caused by arousal, you can be certain."
    show eec 56
    mc "Of course..."
    mct "I kinda feel the Princess is lying... she never gets this flushed after conjuring all those portals..."
    mc "Well... in any case, I guess we should go find Alex and Dalia."
    mc "We still need to find that Gem."
    mc "As long as you still want to help us, that is."
    mc "You're free now. You don't owe me anything anymore."
    play sound water
    show eec 58
    ca "I will continue helping you... of my own volition. You are still the best chance I have to find my way back to Hyril'ar."
    show eec 57
    ca "But you go ahead, I will join you all after I am done."
    ca "After such an activity, I need to bathe again and cleanse myself."
    ca "You will agree that this situation spiraled out of control."
    show eec 56
    mc "Of course."
    mc "I'll leave you alone, Princess."
    mc "Will you allow me one last compliment before I leave?"
    show eec 57
    ca "I will."
    show eec 56
    mc "You truly are a beacon of beauty."
    mc "I'll have your image burned into my memories for a long time."
    mc "I can't speak for Queen Anima's appearance, but... she surely could not have had such magnificent attributes."
    ca "Hmm."
    show eec 57
    ca "That was... terribly sacrilegious."
    ca "But... I will allow it."
    show eec 56
    mct "That's not the reaction I would have gotten a few weeks ago."
    mct "She’s warming up to me, I can feel it."
    mct "Keep grinding, [mc]..."
    show eec 58
    ca "Were you not leaving?"
    show eec 56
    mc "O-Of course!"
    mc "Take care, my Princess."
    show eec 57
    ca "Until we meet again, [mc]."
    $ calypso_interest += 1
    $ menucalyline = True
    $ calypsohandjob = True
    $ sideu = True
    jump secondmenuwestern


label daliawestern:
    $ westerndalia = False
    $ westerndalia2 = True
    stop soundloop fadeout 8
    scene ed 1 with dis2
    play music2 western4 fadein 5
    mct "Damn, the sun really is merciless here."with dis08
    mct "That train has to feel like an oven. Somehow I doubt it has air conditioning."
    d "Agh, you're such an incompetent motherfucker!"with hpunch
    mct "Ah, I know that voice."
    play sound2 footsteps
    play sound3 footsteps
    show ed 2 with dis15
    mc "*Turning around the corner* (And I know that ass too.)" with dis06
    mc "Hey Dalia!"
    show ed 18
    d "*Turning around* Hmm?"with dis12
    show ed 3
    d "Oh, hi [mc]."with dis
    show ed 4
    mc "What are you up to?"
    mc "Do you need any help?"
    show ed 4b
    d "Well... maybe. I was trying to talk to the Sheriff of the town, but he turned out to be an incompetent drunk."with dis
    show ed 4a2
    she "*Hic* I heard ya, ya know?"
    show ed 4b
    d "Bite my ass."
    show ed 4a2
    she "Agh... these kids have no respec' anymore..."
    show ed 4b
    d "*Sighs* So yeah, he doesn't want to tell me anything about El Coyote, even if he {i}does{/i} know something."
    d "He wants us to pay him."
    show ed 4b1
    mc "Hmm... let me talk to him."
    mc "Maybe I can convince him with my persuasive techniques."
    show ed 4b
    d "Sure, suit yourself."
    show ed 4a with dis12
    mc "Good morning, sir." with dissolve
    show ed 4a2 
    she "*Hic* Marthaaa?? I mm’told ya I don’t know anything about those crusty socks..."
    show ed 4a
    mc "Um... what?"
    show ed 4a2
    she "Ehh? Wait... you're not... you're not Martha."
    she "What do ya want now, boy... make it shhnappy."
    show ed 4a
    mct "Yikes, his breath stinks of alcohol."
    mc "Are you seriously the Sheriff...?"
    show ed 4c
    she "*Hic* What, those eyeballs just for show or shh-omethin’??"with dis08
    she "Lookey here at my shiny precious and read, boy."
    she " Sherrrr...ifffffff."
    show ed 4a
    mc "Yeah... I see it."with dis08
    mc "They {i}clearly{/i} chose the best man possible for the job."
    show ed 4a2
    she "*Hic* Oh, that’s actually very sh-weet of ya. Thank you!"
    show ed 4a
    mc "Anyway..."
    mc "We were looking for a dangerous criminal that might be hiding in your town."
    mc "He goes by the name of “El Coyote”."
    show ed 4a2
    she "Mmm... why yesh, yesh, I know where one of his folks is hidin’. Coyote himself might be there too!"
    show ed 4a
    mc "Oh, excellent!"
    mc "Where is he?"
    show ed 4a2
    she "*Hic* Bet you’d love to know, wouldn’tcha?"
    she "Throw 150 eternals my way and I'll tell ya."
    show ed 4a
    mc "What?!"
    mc "But you're the sheriff!"
    mc "Shouldn't you be the one paying us to catch a criminal?"
    show ed 4d
    she "*Hic* Look, boy... they say crime doesn’t pay but what they don’t tell ya ish that THE LAW DON’T EITHER!"with dis08
    she "This whiskey ain’t gonna refill itself, y’know??"
    she "So... 150 of the big-bucks, or El Coyote and his folks are gonna keep winnin’ this game of hide and seek with ya."
    show ed 4a
    mc "You've gotta be the worst sheriff ever."with dis08
    show ed 4a2 
    she "Yeah, I get that a lot."
    show ed 4b1 
    mc "Jeez, this guy is a piece of work."with dis
    show ed 4b
    d "No wonder outlaws can hide in this server without worrying."
    show ed 4b1
    mc "*Sighs* I guess we'll have to bribe him."
    mc "It's too good of a lead to let it go."
    show ed 4b
    d "Yeah, I guess."
    show ed 5
    d "You wanna play for it?"with dis08
    d "The loser has to cough up the cash."
    show ed 6
    mc "*Chuckles* Ah, there's the Dalia I know..."
    mc "Always up for a chance to compete, huh?"
    mc "Alright, I'm in."
    show ed 5
    d "Let's go for a classic game of rock-paper-scissors."
    d "The loser pays the bill."
    show ed 6
    mc "Rock-paper-scissors?"
    mc "Are you sure? Don't you prefer a game that relies less on luck?"
    show ed 7
    d "Luck? There's no luck involved here, [mc]." with dis08
    d "Rock-paper-scissors is a game of mental agility, where deciphering your opponent's intentions is the essence of the game."
    d "It's a battle of wits, my friend."
    show ed 8
    mc "*Laughs* If you say so."
    mc "Alright, rock-paper-scissors it is, then."
    mc "Best of three?"
    show ed 7
    d "One round. All or nothing."
    show ed 8
    mc "Fine with me."
    show ed 5
    d "Okay, you ready?"with dis08
    show ed 6
    mc "On the count of three."
label westernrps:
    mc "One..."
    mc "Two..."
    menu:
        with dis
        mod "Try until you win."
        "Rock":
            play sound clotheswhoosh
            $ rpsw = renpy.random.randint (1, 3)
            if rpsw == 1:
                scene ed 11
                show westrock
                d "Three!"with vpunch
                d "Oh."
                mc "A tie."
                scene ed 5
                d "Again?"with dis08
                scene ed 6
                mc "Again."
                jump westernrps
            elif rpsw == 2:
                scene ed 9
                show westrock
                d "Three!"with vpunch
            elif rpsw == 3:
                scene ed 10
                show westrock
                d "Three!"with vpunch
                $ westernrpss = True
        "Paper":
            play sound clotheswhoosh
            $ rpsw = renpy.random.randint (1, 3)
            if rpsw == 1:
                scene ed 11
                show westpaper
                d "Three!"with vpunch
                $ westernrpss = True
            elif rpsw == 2:
                scene ed 9
                show westpaper
                d "Three!"with vpunch
                d "Oh."
                mc "A tie."
                scene ed 5
                d "Again?"with dis08
                scene ed 6
                mc "Again."
                jump westernrps
            elif rpsw == 3:
                scene ed 10
                show westpaper
                d "Three!"with vpunch
        "Scissors":
            play sound clotheswhoosh
            $ rpsw = renpy.random.randint (1, 3)
            if rpsw == 1:
                scene ed 11
                show westscissors
                d "Three!"with vpunch
            elif rpsw == 2:
                scene ed 9
                show westscissors
                d "Three!"with vpunch
                $ westernrpss = True
            elif rpsw == 3:
                scene ed 10
                show westscissors
                d "Three!"with vpunch
                d "Oh." 
                mc "A tie."
                scene ed 5
                d "Again?"with dis08
                scene ed 6
                mc "Again."
                jump westernrps          
    if westernrpss:
        d ". . ."
        scene ed 14
        d "Dammit." with dis
        scene ed 15
        mc "Sorry, Dalia."
        mc "It's a battle of wits. You never stood a chance."
        show ed 14
        d "One day, I'll have a bit of luck on my side."
        d "Just a tiny bit..."
        d "But anyway, fair is fair. I pay."
        show ed 15
        show screen eternals with dissolve
        play sound coins
        $ money += 50
        pause .05
        $ money += 50
        pause .05
        $ money += 50
        pause 0.01
        mc "Handling the loss like a true sportswoman, Miss Carter." with dissolve 
    else:
        mc ". . ."
        mc "Dammit."
        scene ed 12
        d "Flawless victory!"with dis
        d "I told you, [mc]."
        d "A battle of wits. You never stood a chance."
        show ed 13
        mc "*Chuckles* I still think it's all pure luck, but anyway, fair is fair."
        mc "I lose, I pay."
    mc "Now let's talk to this drunkard..."
    show ed 4a 
    hide screen eternals
    with dis12
    mc "Okay... here's your money."with dissolve
    mc "150 eternals."
    show screen eternals with dissolve
    play sound coins
    $ money -= 50
    pause .05
    $ money -= 50
    pause .05
    $ money -= 50
    pause 0.01
    mc "The information better be worth it." with dis06 
    hide screen eternals
    scene ed 4e
    she "Ah, sweet, sweet!" with dis 
    she "Thank you so much, kiddo. With this I'll be able to buy us some new fancy-gizmos for the office."
    show ed 4a2
    she "And maybe... a couple of bottles of whiskey to celebrate it. Two or three."with dis08
    she "Or... four. Life’s long... gotta have enough to last."
    she "*Hic* Perhaps five. Life is short! Drink while you can..."
    show ed 4a
    mc "The info!"
    show ed 4d
    she "Okay, okay! Why such a hurry? Jeez..."with dis08
    she "*Hic* Lemme remember..."
    she "El Coyote had this big man in his gang... Boone! Strong guy. Nice fella."
    she "He looooved to fish! Like, really, really loved it! So... one day, he found this old cabin near a pond, and bam! He decided to camp there all the damn time!"
    she "If he's in Eternum, you'll prolly find him there fishin' away."
    show ed 4a
    mc "And El Coyote could be with him?"with dis08
    show ed 4a2
    she "*Hic* Seems likely."
    she "Good hidin' spot, that's for sure. You gotta ride your horsie through the Red Ridge, ya know, for like... solid two whole hours."
    show ed 16
    d "WHAT?"
    d "Two hours on horseback?!"
    she "Yeap, that's what I said."
    show ed 4a
    mc "Well, we should be on our way, then."
    show ed 4a2 
    she "You're welcome!"
    show ed 4a
    mc "I didn't say thank you."
    show ed 4a2
    she "Oh, if you... *hic* see my deputy, could you tell him to bring me some tobacco from the General Store?"
    she "He went there to collect some taxes or somethin'."
    show ed 4a
    if not westerncalypso:
        mc "Um... the deputy...? S-Sure."
        mc "I-I haven't seen him, but I'll keep it in mind."
        mc "*Clears throat* Farewell, Sheriff."
    else:
        mc "Pay me 150 eternals and I'll tell him."
        she ". . ."
        show ed 4a2
        she "{font=adeb.ttf}Well played."
    show ed 18
    mc "Well... that's quite a ride, that's for sure."with dis12
    show ed 17
    d "Yeah, it is..."
    d "I'll go get a horse and be on my way."
    show ed 18
    mc "Alright, let's go."
    show ed 17
    d "I'll go alone, don't worry."
    show ed 18
    mc "Nah, you won't."
    mc "I wanna go with you."
    show ed 17
    d "Seriously, don't worry."
    show ed 18
    mc "Come on, two hours riding alone has to be boring. It'll be more fun if we go together."
    mc "I wanna do this with you."
    show ed 3
    if daliapath:
        d "Well... if you insist... o-okay!"with dis 
    else:
        d "Well... if you insist, okay. Just don't complain about it later."
    d "I'll go round up a couple of horses."
    d "This is a long trip, so... maybe you should go see if Alex and Calypso need any help before we leave."
    show ed 4
    if not westerncalypso and not westernalex:
        mc "I already checked on them. We should be good to go."
        show ed 3
        d "Alright, cool!"
        d "Meet me at the chapel in the southern part of town in 5 minutes, then."
        show ed 4
        mc "Sure, I'll go get some water for the trip in the meantime."
    else:
        mc "Sure, that sounds good."
        show ed 3
        d "Meet me at the chapel in the southern part of town after you're done."
        show ed 4
        mc "I'll be there! I'll bring some water for the trip too."
    show ed 3
    d "Sounds good. See you now!"
    if westerncalypso or westernalex:
        mod "Go to Dalia last."
    jump secondmenuwestern


label dalia2western:
    $ dalia2western = False
    stop soundloop fadeout 9
    scene ed 19 with dis22
    play music2 western1 fadein 6
    play soundlow horse
    pause
    show ed 20 with dis14
    d "*Patting the horse* Good girl!" with dis06
    d "If you behave I'll give you a bucket of carrots when we're back, deal?"
    mc "I see you could find a horse!"
    show ed 21
    d "Hey! Yeah, I did."with dis
    d "And it's a good one, should be able to maintain a good pace for several miles, even in this heat."
    show ed 22
    mc "Sweet. Does she have a name?"
    show ed 21
    d "I call her Roach."
    show ed 22
    mc "*Chuckles* Good name. What's my horse's name?"
    show ed 23
    d "Actually... I could only find one." with dis
    d "She was the only horse left at the stables."
    mc "Oh."
    show ed 25
    d "So... I guess I'll have to go alone, after all." with dis
    d "Which might be better, honestly."
    if daliapath:
        d "We're not even sure if El Coyote will be hiding in this cabin, so we'll cover more terrain if we split up."
    else:
        d "I'm not sure I can put up with you for two whole hours."
    show ed 24
    menu:
        with dis
        "[gr]Go with her":
            $ daliacabin = True
            mc "Can't we ride together?"with dissolve
            if not daliapath:
                $ daliacabin = False
                show ed 25
                d "Um... it's probably not a good idea, we'd go way slower."
                d "And I don't wanna strain Roach too much."
                show ed 21
                d "Seriously, don't worry about it. I can handle it."with dis 
        "Stay in the town":
            mc "Awh, that's too bad."with dissolve
            mc "I can go instead of you, if you want."
            show ed 21
            d "Nah, it's okay, but thanks for offering."with dis 
    if not daliacabin:
        d "It'll be a good chance to improve my horse riding skills."
        show ed 22
        mc "Yeah, that's a... {i}useful{/i} skill to learn, for sure."
        mc "Okay then, be careful out there!"
        show ed 21
        d "Hopefully I'll be back in a few hours... but if I'm not, text me when you log off!"
        show ed 22
        mc "Will do!"
        mc "Good luck, Dalia."
        show ed 21
        d "You too!"
        show ed 22
        mct "Hmmm... while she's doing this, I might as well scout around town. Who knows, I might stumble upon something useful."
        mct "Where are you, Coyote..."
        jump westernending 
    show ed 25
    d "Um..."
    d "I mean... I guess, it's a big horse."
    d "But I'm not sure if I'll be able to control it with both of us on its back."
    show ed 24
    mc "Then let me take the reins!"
    mc "I'm an experienced horse rider, don't worry."
    show ed 21
    d "*Chuckles* An experienced horse rider? Since when?"with dis 
    d "Have you ever ridden a horse before?"
    show ed 22
    mc "I rode a donkey at a medieval fair when I was 12. I assume it'll be pretty much the same."
    mc "The carny said, and I quote, that I had “a gift worthy of Sir Richard the Lionheart”."
    mc "I don't lie, you can ask Annie."
    show ed 21
    d "*Snorts* I {i}will{/i} ask her, you can be sure."
    d "That's a story I don't wanna miss."
    d "But alright, show me your “gift”, Lionheart. Let's ride together."
    show ed 22
    mc "With pleasure!"
    play soundlow debris
    play sound horsesaddle
    play sound2 horse2
    show ed 27 with dis15
    bla "You effortlessly mount the horse in one jump and extend your hand to Dalia."with dis06
    show ed 26
    mc "C'mon!"
    show ed 27
    d "O-Okay! Let's go."
    d "W-Where am I supposed to put my foot? There's no stirrup."
    show ed 26
    mc "Don't worry about that, just take my hand and I'll pull you up."
    show ed 27
    d "O-Okay."
    play soundlow debris
    play sound horsesaddle
    play sound2 horse2
    show ed 28 with dis12
    d "O-Oh boy." with dissolve 
    d "This looks taller than I expected."
    show ed 29
    mc "Are you scared of horses?"
    mc "Is that why you don't have one in Ekabar?"
    show ed 28
    d "I'm not scared of them!"
    d "I just... respect them."
    show ed 29
    mc "You need to lose this fear, you'll never embrace your inner Rohirrim otherwise."
    show ed 28
    d "I said I'm not sca–"
    play sound whip
    play sound2 whip
    play sound3 horse
    play sound4 horsegallop
    play soundlow debris
    show ed 30
    bla "You crack the reins and pop off towards the canyon the sheriff mentioned." with dis 
    d "SLOW DOWN!" with hpunch
    mc "Go Roach!"
    stop music2 fadeout 5
    scene black with dis25
    show screen afewhourslater with dis15
    pause
    play soundloop2 wind fadein 6 volume 0.5
    scene ed 31
    hide screen afewhourslater
    with dis25
    mc "*Sighs* Aaaaaand... more red rock." with dis08
    mc "Man, this server is as huge as all the others."
    play sound whip
    play sound2 whip
    play soundlow horse
    play soundloop horsetrot fadein 2
    show ed 32
    mc "*Resuming the march* I hope we didn't take a wrong turn."with dis12
    mc "Are there any other towns in this server, apart from Blackridge?"
    d ". . ."
    mc "Dalia? Did you fall asleep back there?"
    show ed 33
    d "E-Eh?"with dissolve
    show ed 34
    d "Ah, no, I'm here."
    d "Um... yeah, there are a lot of them."
    d "I haven't explored it much, but Alex told me there are dozens of towns, and even a big main city down south."
    d "Most of them are connected by train."
    show ed 33
    d "We just came to Blackridge because it's where El Coyote is hiding."
    d "Allegedly."
    show ed 35
    mc "Damn, that's crazy. I wonder how many online players there must be on average."
    show ed 34
    d "Who knows. Just in Blackridge there must be like... 100 people? Maybe 200 on weekends."
    show ed 33
    d "In all Frontier Trails... probably thousands."
    show ed 34
    d "And that's without including the NPCs."
    show ed 35
    if not westernalex:
        mc "Yeah, I found out about that earlier."
        mc "I was with Alex and we had an incident with some weirdo and an NPC. It was a kid, so... you can imagine which way the wind was blowing."
        show ed 33
        d "Ugh, that sounds awful."
        show ed 35
        mc "Oh, it {i}was{/i} bad, believe me."
    else:
        mc "What? Are there NPCs in Frontier Trails?"
        show ed 33
        d "Yeah, I think so. You know how the whole goal of Eternum is to be as immersive as possible."
        d "There are usually some NPCs scattered throughout the servers like these to prevent the worlds from feeling empty."
        show ed 34
        d "They can be interacted with, although they don't carry anything valuable and they can't harm players, so most people just ignore them."
        d "In this case I think they're limited to some ranchers between the main towns."
        show ed 35
        mc "I see."
    mc "It's crazy when you think about it, you know?"
    mc "I see it very differently now."
    show ed 33
    d "What do you mean?"
    show ed 35
    mc "The NPCs."
    mc "They're all there... doing their things... even if there isn't any human player to observe them in a 10-mile radius."
    show ed 33
    d "Well, we don't know that. Maybe they simply freeze in place when no one's around."
    d "Like in Toy Story, but the other way around."
    show ed 35
    mc "*Chuckles* Maybe."
    mc "Do you ever wonder if all the NPCs were once real people? Like Thanatos?"
    show ed 34
    d "Uhh... huh, I didn't think about it, but it seems unlikely."
    d "Just the thought of it sounds quite dreadful, doesn't it?"
    show ed 35
    mc "Yeah... it really does."
    mc "But you're right, there's no way Ulysses managed to cover so many disappearances."
    show ed 34
    d "Unless... Ulysses found a way to brainwash and control people from a parallel dimension and bring them here."
    show ed 35
    mc "Honestly? We've reached a stage where that wouldn't even surprise me."
    mc "If I were to wake up tomorrow inside a Matrix pod, surrounded by tubes connected to me, I'd probably just nod and say “Oh, well, that actually makes sense, yeah”."
    show ed 36
    d "*Laughs* Yeah, I'd probably react the same way."
    play sound debris
    play sound2 horse2
    stop soundloop fadeout 1
    show ed 35
    mc "*Stopping the horse* Finally!"with dissolve
    mc "Are you seeing what I'm seeing?!"
    $ renpy.music.set_volume(0.3, channel='soundloop')
    play soundloop wind fadein 10
    show ed 37 with dis14
    d "Oh fuck..."with dis
    mc "I know, right?? That's gotta be the damn cabin!"
    d "Um... [mc]?"
    mc "Okay, we don't know if there's anyone inside."
    d "[mc]..."
    mc "Let's leave the horse here and..."
    $ renpy.music.set_volume(1.0, delay=2.0, channel='soundloop')
    $ renpy.music.set_volume(1.0, channel='soundloop3')
    play music wind2 fadein 2
    play sound5 horse
    show ed 38
    bla "Dalia grabs your head with her hands and turns it towards the massive sandstorm rolling in from the west." with dis14
    mc "W-What the fuck is that?"
    d "A sandstorm! Coming this way!"
    mc "Oh shit."
    mc "What's gonna happen to us if we stay in the open?"
    d "We die!"
    show ed 37
    mc "FUCK!"with dis
    mc "Should we go to the cabin?"
    d "What? I can't hear you!"
    mc "SHOULD WE GO TO THE CABIN?!"
    d "WE SHOULD GO TO THE CABIN IF WE DON'T WANNA DIE!"
    mc "I CAN'T HEAR YOU, LET'S GO TO THE CABIN!"
    mct "Holy fuck, this thing is moving fast... we better hurry."
    stop soundloop2 fadeout 3
    stop soundloop fadeout 3
    stop music fadeout 3
    play soundloop3 wind3 fadein 3
    scene ed 39 with dis22
    d "OKAY, I LEFT THE HORSE IN THAT SHED OVER THERE!" with dissolve
    mc "ALRIGHT, LET'S GO INSIDE!"
    d "OKAY!"
    play sound knock3
    mc "*Knocking on the door* HELLO? ANYBODY THERE??"with hpunch 
    bla ". . ."
    mc "I THINK IT'S EMPTY!"
    mc "I'LL OPEN THE DOOR, WATCH OUT!"
    mc "*Taking a run-up* Haaa..."
    play sound2 woodhit
    play sound3 woodhit
    play sound4 slam
    play soundloop wind
    play soundloop2 wind2
    show ed 40
    mc "HYA!" with hpunch 
    mc "WHOA, that's what I call a kick!"
    mc "Nice technique, eh?!"
    mc "Did you see that, Dalia?"
    play sound punch
    play sound2 fall
    show ed 41
    d "*Pushing you inside* Goddammit [mc], shut up and get the fuck in!" with hpunch
    play sound2 doorwoodclose volume 1.1
    stop soundloop2 fadeout 1
    stop soundloop fadeout 1
    show ed 39 with dis 
    d "*Shutting the door* Oof..."with dissolve 
    d "That was close."
    mc "*Standing up* I can't see shit."
    d "Yeah, I closed all the window shutters so the sandstorm doesn't shatter the glass."
    mc "Smart."
    d "Wait, I think I see a lantern over there."
    play sound lantern
    scene ed 42 with dis 
    mc "That's better!" with dissolve 
    show ed 43
    d "Alright... it seems to be empty."with dis12
    mc "No bears or psychopaths hiding in the shadows."
    d "I guess the man we were looking for wasn't playing Eternum today."
    show ed 43b
    mc "He definitely comes here regularly, though."with dis 
    mc "Look at these logs, they're still red-hot."
    d "Hmm, true."
    mc "Maybe the sandstorm caught him out of home."
    play sound chair2
    show ed 44
    d "If that's the case, he won't last long." with dis 
    d "Staying outside during one of Frontier Trails' sandstorms is almost a death sentence."
    d "That's why no one dares to venture too far from towns and main cities. The farther you go, the deadlier they are."
    show ed 45
    mc "I guess we'll have to stay here for a while, then."
    show ed 44
    d "Yep, at least for a couple of hours."
    d "So... you better find us some cards or something."
    show ed 45b
    mc "Well, I see no cards, but I found the cabin's collection of beverages."with dis12
    mc "What do you say? Fancy a little drink?"
    d "Um..."
    d "*Chuckles* Sure, why the hell not. Since we're gonna be stuck in here anyway... why not get drunk."
    mc "That's the spirit!"
    mc "Cheers to being trapped!"
    scene black with dis22
    show screen afewminuteslater with dis12
    pause
    scene ed 47 
    hide screen afewminuteslater
    with dis22
    pause 
    play music2 western5 fadein 5
    d "*Clears throat* Okay... erm..."with dis 
    d "I would probably... kill Ironman..."
    stop soundloop3 fadeout 11
    show ed 49
    d "Fuck Superman, and..." with dis17
    show ed 50
    d "Marry Batman."
    show ed 48
    mc "Interesting... you're marrying Batman because he's rich, eh?"
    mc "I didn't take you for a gold digger."
    show ed 51
    d "I'm marrying Batman because he's the cooler one of the three, dumbass."
    show ed 48
    mc "*Chuckles* Can't argue with that."
    show ed 51
    d "Okay, your turn now."
    d "Fuck, marry, kill."
    show ed 49
    d "Um..."
    show ed 51
    d "Gertrude, my mom's co-worker..."
    show ed 54
    mc "Oh god."
    show ed 53b
    d "Charlotte from school... and..."
    show ed 51
    d "A Praetorian."
    show ed 48
    mc "Easy."
    mc "I'd kill..."
    menu:
        with dis
        "Gertrude{#0.6,fmk}":
            mc "Gertrude." with dissolve
            show ed 52
            d "*Snorts* You didn't even flinch."
            show ed 48
            mc "I'd fuck..."
            menu:
                with dis
                "Charlotte":
                    mc "Charlotte... preferably with her bra on..."with dissolve 
                    mc "And I'd marry the Praetorian."
                    show ed 52
                    d "*Snorts* You'd MARRY the Praetorian?"
                    d "You're a fucking weirdo."
                    show ed 48
                    mc "A loyal wife that can murder my enemies in the blink of an eye? I'm in for that."
                    show ed 51
                    d "*Laughs* If you say so."
                    show ed 48
                "Praetorian{#0.6,fmk}":
                    mc "The Praetorian."with dissolve 
                    mc "And I'd marry... Charlotte."
                    show ed 51
                    d "Why am I not surprised to hear you'd fuck a Praetorian?"
                    show ed 48
                    mc "I mean, that would be pretty wild."
                    show ed 51
                    d "*Laughs* Oh, totally."
                    show ed 48
        "Charlotte":
            mc "Charlotte."with dissolve 
            mc "I'd fuck..."
            menu:
                with dis
                "Gertrude{#0.6,fmk}":
                    mc "*Shivers* G-Gertrude..."with dissolve 
                    mc "Probably after having drunk a whole bottle of booze..."
                    mc "And I'd marry the Praetorian."
                    show ed 52
                    d "*Snorts* You'd MARRY the Praetorian?"
                    d "You're a fucking weirdo."
                    show ed 48
                    mc "A loyal wife that can murder my enemies in the blink of an eye? I'm in for that."
                    show ed 51
                    d "*Laughs* If you say so."
                    show ed 48
                "Praetorian{#0.6,fmk}":
                    mc "The Praetorian."with dissolve 
                    mc "And I'd marry Gertrude."
                    mc "A marriage with no sex. And preferably no verbal interaction."
                    show ed 51
                    d "Why am I not surprised to hear you'd fuck a Praetorian?"
                    show ed 48
                    mc "I mean, that would be pretty wild."
                    show ed 51
                    d "*Laughs* Oh, totally."
                    show ed 48
        "Praetorian{#0.6,fmk}":
            mc "The Praetorian."with dissolve 
            mc "I'd fuck..."
            menu:
                with dis
                "Gertrude{#0.6,fmk}":
                    mc "*Shivers* G-Gertrude..."with dissolve 
                    mc "Probably after having drunk a whole bottle of booze..."
                    mc "And I'd marry Charlotte."
                    show ed 51
                    d "*Snorts* So you're into MILFs, uh? Interesting."
                    show ed 48
                    mc "*Laughs* Better than marrying her."
                    mc "She's unbearable, I'd go crazy after the first couple of days."
                "Charlotte":
                    mc "Charlotte... preferably with her bra on..."with dissolve 
                    mc "And I'd marry Gertrude."
                    mc "It'd be funny to see her face on the altar after realizing my name's not Dalia."
                    show ed 51
                    d "*Laughs* True! I wouldn't want to miss that."
                    show ed 48
    mc "Okay, your turn now!"
    mc "Let me think..."
    mc "Let's go with..."
    mc "Jerry, Axel, and... me."
    show ed 49
    d "Uh..."
    d "Can I kill two?"
    show ed 54
    mc "*Laughs* You can't."
    show ed 49
    d "Okay, then... I kill Axel."
    d "I marry... Jerry."
    show ed 53b
    d "And I... fuck... you, I guess."
    show ed 48
    mc "Interesting... does Jerry's marriage imply sex?"
    show ed 51
    d "Definitely not. It'd be strictly a marriage of convenience."
    show ed 54
    mc "Oh... so I'd be your lover. Nice..."
    show ed 52
    d "*Laughs* I didn't say that. Don't get your hopes up."
    show ed 51
    d "Okay, okay, hear me out..."
    d "Micaela... Idriel, and... myself."
    show ed 54
    mc "Ah, this is starting to get interesting..."
    mc "Alright, I'd kill..."
    menu:
        with dis
        "[gr]Micaela{#0.6,fmk}":
            mc "Micaela, I guess." with dissolve
            mc "Please don't tell Chang I said this."
            mc "I'd fuck..."
            menu:
                with dis
                "Idriel [dalia_pts]":
                    mc "Idriel."with dissolve 
                    mc "And I'd marry you."
                    $ dalia_points += 1
                    play sound beat
                    show screen heartbeat
                    show ed 50
                    d "*Clears throat* Oh... okay."with dis
                    d "Not what I was expecting."
                    show ed 48
                    mc "No way I'm wasting a chance to marry you."
                    mc "And don't worry, unlike Jerry's, our marriage also implies lots of sex."
                    show ed 51
                    d "*Snorts* No thanks."
                    d "Not interested."
                "You{#0.6,fmk}":
                    mc "You..."with dissolve 
                    mc "And I'd marry... Idriel."
                    mc "Being the husband of the Lady of Eternum has to be incredibly beneficial."
                    show ed 51
                    d "Oh, definitely."
            show ed 48
        "[gr]Idriel":
            mc "Idriel."with dissolve 
            mc "I'd fuck..."
            menu:
                with dis
                "Micaela [dalia_pts]{#0.6,fmk}":
                    mc "Micaela."with dissolve 
                    mc "And if I managed to survive that somehow... I'd marry you."
                    $ dalia_points += 1
                    play sound beat
                    show screen heartbeat
                    show ed 50
                    d "*Clears throat* Oh... okay."with dis
                    d "Not what I was expecting."
                    show ed 48
                    mc "No way I'm wasting a chance to marry you."
                    mc "And don't worry, unlike Jerry's, our marriage also implies lots of sex."
                    show ed 51
                    d "*Snorts* No thanks."
                    d "Not interested."
                    show ed 48
                "You{#0.6,fmk}":
                    mc "You..."with dissolve 
                    mc "And I'd marry... Micaela."
                    mc "Also a marriage of convenience. Gotta protect my boy Chang's woman."
                    show ed 51
                    d "Ah, the bro code."
                    show ed 48
                    mc "*Chuckles* Correct."
        "You{#0.6,fmk}":
            mc "You."with dissolve 
            show ed 53
            mc "I'd fuck..." with dissolve 
            menu:
                with dis
                "Micaela{#0.6,fmk}":
                    mc "Micaela."with dissolve 
                    mc "And if I managed to survive that somehow... I'd marry Idriel."
                "Idriel":
                    mc "Idriel."with dissolve 
                    mc "And I'd marry... Micaela."
                    mc "Also a marriage of convenience. Gotta protect my boy Chang's woman."
            d ". . ."
            mc "What?"
            show ed 49
            d "Nothing, nothing..."
            d "Just think of 3 more."
            show ed 48
    mc "OH! Okay, I have a good one."
    show ed 51
    d "Shoot."
    show ed 48
    mc "Penny, Alex, and... Annie."
    show ed 49
    d "Uh... damn."
    d "Okay, I'd... fuck... Alex."
    show ed 52
    d "We've been friends for so long that I'm sure we'd... get along well."
    mc "The mental image of it definitely sounds good..."
    show ed 49
    d "Then I'd marry... Penny."
    d "If I'm not the one to put up with her, then who will?"
    show ed 48
    mc "*Chuckles* I imagined you'd say something like that."
    show ed 49
    d "And... well, to be honest, as much as we get on each other's throats, I love her more than anything."
    d "So... meh, it doesn't sound that bad. We've always lived together, it wouldn't change much."
    show ed 51
    d "But don't tell her I said that I love her."
    show ed 53b
    d "And then I'd fuck... Annie."
    d "She's so cute. She’s small, but... in a hot way. You know what I mean?"
    show ed 48
    mc "You said fuck twice."
    show ed 50
    d "Did I?"
    d "Well, I don't wanna kill anyone."
    show ed 53
    mc "But you can't repeat an option, that's not how the game works!"
    show ed 50
    d "Oh you wanna play that game?"
    d "Alright: Me, Penny, and mom. Fuck, marry, kill."
    show ed 53
    mc ". . ."
    mc "O-Okay I'd..."
    d ". . ."
    mc ". . ."
    show ed 55
    mc "*Clears throat* Hey, there's a dartboard over there!" with dis 
    mc "Do you wanna play?"
    show ed 52
    d "*Giggles* Look how fast he wants to switch games now!" with dis 
    mc "I was already planning to."
    d "Sure, sure!"
    show ed 54
    mc "What do you say? The one who gets further from the center each time takes a shot."
    show ed 51
    d "I don't think I can drink anymore."
    show ed 54
    mc "Then..."
    show ed 51
    d "Ah, I know that look. Here comes something dirty."
    show ed 54
    mc "The loser takes off a piece of clothing."
    show ed 51
    d "Bingo."
    d "Strip darts?"   
    stop music2 fadeout 5 
    show ed 48
    mc "Strip darts indeed. Registered trademark."
    d "Hmm..."
    $ renpy.music.set_volume(0.65, channel='music3')
    play music3 eyg fadein 6
    show ed 54
    d ". . ." with dis
    mc "I like that smirk."
    show ed 51
    d "Might be this homemade whiskey talking, but... fuck it, alright."
    d "Let's do this."
    show ed 54
    mc "Wait... really?"
    play sound chair3
    show ed 54b
    d "*Leaning forward* Yeah... why not." with dis
    d "I'm not one to shy away from a competition, no matter the circumstances."
    d "Let's make it interesting."
    d "The game... is on."
    mc "You know, I've always loved your competitive side..."
    play sound2 chair2
    show ed 58 
    bla "Dalia stands up with determination and grabs one of the darts."with dis12
    mc "Do you wanna make a few test throws?"
    show ed 56
    d "I need no tests."with dis
    d "You can start taking off your shoes, though."
    d "It'll save us time."
    mc "*Chuckles* You'll pay for that overconfidence."
    d "Just watch. Straight to the center."
    play sound dart
    scene ed59 with hpunch
    pause .4
    mc "HAH!"with dis08
    show ed 60
    d "Dammit."with dis
    d "I drank too much."
    show ed 61
    mc "*Grabbing a blue dart* This will be the easiest competition in the history of competitions." with dis12
    mc "Don't try to find excuses."
    show ed 62
    d "*Chuckles* Shut up and throw it already."
    d "Just make sure not to hit me."
    play sound dart
    scene ed62b with hpunch
    pause .4
    mc "Yes!" with dis08 
    show ed 63
    d "Huh, nice one."with dis 
    show ed 64
    mc "Thank you."
    show ed 63
    d "Beginner's luck."
    show ed 64
    mc "More like pure skill."
    show ed 63
    d "*Laughs* Sure..."
    play sound clothes3
    play sound7 clothes3
    show ed 65
    bla "Dalia slowly removes her boots and leaves them under the table."with dis15
    mc "Wow..."
    mc "Your legs really look as if they were sculpted in marble."
    d "*Giggles playfully* Shut up and play, Michelangelo."
    play sound dart
    scene ed66
    pause 
    play sound w1
    scene ed67 
    pause 
    play sound belt
    scene ed 68
    bla "Dalia unbuttons her corset and takes it off." with dis17
    mc "Nice..."
    play sound dart
    scene ed69
    pause 
    play sound5 w1
    show ed70
    pause 
    play sound clothes4
    scene ed 71 with dis17
    mc "I really like this game..."with dissolve
    show ed 72
    d "I-I think there's something wrong with my dart."with dis
    d "Let me use yours."
    show ed 73
    mc "No way! I got used to this one already."with dis
    show ed 74
    d "So you're admitting that they're not the same?"
    show ed 73
    mc "Mmm..."
    mc "Okay, fine, I'll use the red one."
    mc "But if I win... I get to suck your tits."
    show ed 74
    d "What?! You're dreaming."
    show ed 73
    mc "No deal then."
    d ". . ."
    show ed 74
    d "You can lick my ankles."
    show ed 73
    mc "Your tits."
    show ed 74
    d "My legs."
    show ed 73
    mc "Your abs."
    d ". . ."
    show ed 74
    d "Okay, my abs."
    show ed 73
    mc "Oh boy... one of my fantasies is about to come true."
    show ed 75 with dis17
    d "*Giggles* And now you throw the darts like a professional??"with dissolve 
    mc "Mm-hm..."
    play sound dart
    scene ed76 with hpunch 
    pause .4
    mc "Because I AM a professional!" with dis08 
    mc "I almost hit the center!"
    d "*Grumbling* Make room!"
    scene ed 77 with dis15
    pause 
    d "*Takes a deep breath*"with dis08
    play sound dart
    scene ed78 with hpunch 
    pause .4
    d "AAGH!" with dis08
    show ed 79
    d "NO FUCKING WAY!!!" with hpunch
    d "You {i}had{/i} to have your lucky throw just when I finally got the hang of it!"
    mc "*Chuckles* It is what it is..."
    show ed 80
    d "*Sighs* Okay, okay, fine..." with dis15
    d "Let's get it over with."
    show ed 81
    mc "Oh yes, finally..."
    mc "Are you wearing a bra?"
    show ed 80
    d "You know I'm not."
    show ed 81
    mc "Oh dear..."
    show ed 80
    d "Why are you so excited? You've seen me naked already."
    show ed 81
    mc "Seeing a girl like you naked will always be as exciting as the first time."
    mc "You wouldn't understand."
    d "Hmm."
    play sound clothes3
    show ed 82 with dis15
    bla "Dalia slowly opens her shirt, revealing her nicely shaped breasts and her well-toned abdomen to you."with dis
    mc "WHOA..."
    show ed 84
    mc "You always leave me speechless..."with dis12
    d "Mm-hm."
    mct "God, her tummy is so fucking sexy..."
    d ". . ."
    d "(Why is him looking at my body with such lewdness turning me on?)"
    d "(Why am I enjoying this?)"
    d "(I'm enjoying losing a game!)"
    d "(Am I giving up my principles...?)"
    play sound clothes3
    play soundlow wood fadein 2
    show ed 84b with dis14
    d "W-What are you doing?!" with dis06
    show ed 85
    mc "You said I'd get to lick your abs if I won."
    show ed 84b
    d "W-What? For real? I thought you were kidding."
    show ed 85
    mc "Kidding? I've been fantasizing about it since I saw you in all your glory that day in your beach."
    show ed 84b
    d "Um..."
    d "Well, o-okay, I guess."
    d "If it's part of the game..."
    d "B-But be quick."
    show ed 86 
    mc "Of course..." with dis12
    bla "You can feel Dalia's whole body shuddering and her sparse, blonde body hair standing on end the moment you touch her stomach."
    d "Hmph!"
    mc "You okay?"
    d "Y-Yeah, you just... tickled me."
    scene daliawest1 with dis2
    bla "You start licking Dalia's stomach, taking pleasure in each one of her body's involuntary reactions."with dis
    mct "Man... I'd eat her whole if I could."
    mct "Her smell is incredible."
    mct "We've been riding a horse for hours, drinking some weird homemade booze, but her own scent covers it all somehow."
    d "(God, this is awkward.)"
    d "(Very awkward.)"
    d "(Incredibly awkward.)"
    d ". . ."
    d "(Why...)"
    d "(Why is it turning me on, then...?)"
    d "(Goddammit, Dalia...)"
    d "(I better stop it before... I...)" 
    play sound clothes2
    show ed 88
    d "O-Okay, this is enough."with dis08
    d "You had your fun embarrassing me already."
    play sound2 clothes3
    play sound6 wood fadein 2
    show ed 90
    mc "*Standing up* Certainly. But I've gotta say, you taste really good."with dis15
    show ed 89
    d "*Snorts* If you say so."
    show ed 90
    mc "Did you enjoy it too?"
    mc "I don't remember seeing your nipples so hard when we started."
    show ed 91
    d "*Giggles* Oh, shut up and let's continue playing."
    show ed 89
    d "Although... I only have my panties left to lose, so I don't think the game is gonna last."
    show ed 90
    mc "Oh, do you accept your defeat?"
    show ed 91
    d "Yeah, yeah, you win. You're way better than me at darts."
    d "Happy?"
    show ed 90
    mc "Well... since it's the last round... we can raise the stakes a little."
    mc "What about..."
    show ed 91
    d "*Imitating your voice* {i}If I win, I get another blowjob..."
    show ed 89
    d "Something like that?"
    show ed 90
    mc "Um..."
    play sound clothes3
    show ed 92
    d "*Taking her shirt off* We know each other pretty well already, [mc]." with dis15
    show ed 93
    mct "Jesus Christ, look at that body..."
    show ed 92
    d "You're... predictable. Especially when you're horny."
    show ed 93
    mc "So..."
    show ed 92
    d "Yeah, no."
    d "As I said, it's obvious that you're better than me."
    show ed 93
    mc "Then I'll throw the dart with the gloves on, to even the odds. That makes it way more difficult."
    d "Hmm."
    show ed 92
    d "And... you have to throw it with your eyes closed."
    show ed 93
    mc "What?!"
    show ed 92
    d "And... if I win... it's YOU who has to give ME head."
    show ed 93
    mc "Wha–"
    mct "Oh my god."
    mct "OH GOD. Calm down, [mc]." 
    mct "Don't let her see that it's a win-win for you no matter what."
    mc "Um... a-alright. Seems fair."
    show ed 92
    d "Good, then."
    d "I go first."
    show ed 93
    mc "Now THE GAME is on."
    show ed 94 with dis15
    d "Hmm..." with dis06
    d "(I can't believe I really asked him to go down on me. Alex is such a bad influence, I shouldn't listen to her.)"
    d "(And I can't believe I actually got horny enough to ask him to do that either. Alcohol is also a bad influence.)"
    d "(I should stick to the irons. They'd never betray me.)"
    mc "In another situation I'd probably rush you, but I'm enjoying the view too much for that."
    show ed 58
    d "O-Oh, yeah, sorry!"
    d "*Taking a deep breath* Here I go."
    play sound dart
    show ed 95 with hpunch
    pause .2
    d "Oh!"with dis06
    d "OHH!" 
    show ed 96
    d "YAY! I told you I had gotten the hang of it!"with hpunch 
    d "BULLSEYE!"with hpunch
    mc "Don't celebrate ahead of time..."
    show ed 95
    d "Come on! Have you seen that?! It's literally at the center!"
    mc "Just watch and see..."
    show ed 97
    bla "Dalia snorts playfully, handing you a dart and carefully watching you to ensure you don't open your eyes." with dis12
    scene ed 95
    mc "*Taking a deep breath* Let me calculate the effect of the wind..."with dis
    play sound3 glitch4
    scene dartglitch
    pause
    play sound dart
    show ed 98 with hpunch
    pause .2
    d "W-WHAT?!" with dis06
    d "What the hell?!" with hpunch
    mc "Can I open my eyes now?"
    d "How the fuck did you do that?!"
    mc "Oh, bullseye!"
    show ed 99
    d "*Giggles* Don't bullshit me, you cheated!" with dis12
    show ed 98c
    mc "No, I didn't!"
    show ed 99
    d "You used your powers!"
    show ed 98c
    mc "I used all my {i}skills{/i} available."
    mc "That's not cheating in my books."
    show ed 99
    d "Hah! I should have established the rules earlier."
    show ed 98c
    mc "Well... I guess it's a tie."
    mc "Should we throw again?"
    d "Hmm..."
    show ed 98d
    d "Either that, or..."
    show ed 99
    d "*Giggles* Nah, forget it. I'm getting carried away."
    show ed 98c
    mc "I want you to get carried away so bad, Dalia..."
    mc "Let's just say what crosses our minds."
    mc "Full transparency."
    mc "We're in a cabin in the middle of nowhere, who cares?"
    show ed 98d
    d "Erm..."
    d "I guess... you got a point."
    show ed 98c
    mc "What did you think about?"
    show ed 98d
    d "Well... it's just that..."
    d "Since we both “won”..."
    d "What about... breaking the tie with one last challenge?"
    show ed 99
    d "*Giggles playfully* I can't believe I'm the one suggesting this and not you."
    d "I'll admit that I'm a bit turned on right now."
    show ed 98c
    mc "Please, tell me you're suggesting a 69..."
    show ed 98d
    d "I mean... with what we already did at The Cove server..."
    d "It's not... weird, right?"
    show ed 99
    d "Is it weird?"
    show ed 98c
    mc "Absolutely not."
    show ed 99
    d "So I thought..."
    d "The first one to make the other cum... wins?"
    play sound clothes2
    play sound2 buttons
    show ed 100
    bla "You rip your shirt off and roughly pull Dalia towards you. She doesn't resist at all." with dis 
    mc "Fuck, you have no fucking idea of how much you're turning me on right now, Dalia."
    show ed 100b
    d "Easy win for me, then."
    show ed 100
    mc "Hell no, I'm gonna eat your pussy so raw that you're gonna cum in 10 seconds."
    show ed 100b
    d "Now it's you who's being overly confident, [mc]..."
    show ed 100
    mc "Have I told you how fucking much I love your competitive side?"
    show ed 100b
    d "*Giggles* I bet you'll like it even more now..."
    play sound fall2
    play soundlow ["<silence 0.3>", woodhit]
    show ed 101
    bla "Dalia pushes you to the ground, positioning herself above you, with her legs on either side."with dis12
    show ed 102
    mc "Oh my goodness gracious..." with dis12
    mc "Take off your panties..."
    play sound clothes2
    show ed 103 with dis
    mc "Oh Jesus..."with dis06
    play soundlow clotheswhoosh volume 0.6
    play sound2 woodhit volume 0.5
    scene ed 103b
    bla "You grab Dalia by her huge buttocks and pull her to the ground. You open her ass cheeks, exposing her swollen, already wet pussy."with dis 
    mct "Oh man, this is happening..."
    scene ed 104
    d "(Oh shit. It is happening.)"
    d "(I'm doing a 69.)"
    d "(With [mc].)"
    show ed 103b
    mc "Fuck, I can't wait any longer..."
    play sound bodycollide
    play sound2 bodycollide
    play sound3 blow4
    scene ed 105
    bla "Without giving her a second to breathe, you start attacking Dalia's swollen lips." with dis 
    d "Hmph!"with hpunch
    show ed 106
    d "Hmmmmhhh...." with dis14
    show ed 107
    d "(Holy fuck, he's not wasting a second...)"with dis12
    d "*Moaning* Mmmm..."
    d "(And that feels good...)"
    play sound belt
    show ed 108 with dis15
    d "*Pulling your trousers down* (You've gotta keep up your game, Dalia...)"with dis06
    stop sound fadeout 1
    $ renpy.music.set_volume(0.3, delay=10.0, channel='music3')
    play soundloop blowjob2 fadein 3
    scene daliawest2 with dis22
    d "Mmmm..."with dis08
    mct "Oh my goooooddd..."
    d "*Moaning* Mmmm..."
    bla "You feel your dick head disappear inside of Dalia's mouth, even though you can't actually see it."
    mct "My god..."
    bla "You get fully erect in a matter of seconds, as she quickly covers your cock in saliva."
    mct "I can't even concentrate properly on her..."
    mct "She's not only sucking my cock... the things she does with her tongue... she moves it in circles like a swirling vortex while she moves up and down."
    mct "This is not gonna last long..."
    d "Mmmmmm..."
    d "(Fuck... this is absolutely amazing...)"
    d "(This is so fucking hot.)"
    d "(I want this to last forever...)"
    d "(But you've gotta win, Dalia.)"
    d "(I have to squeeze him to the fullest...)"
    pause
    play soundloop2 blowjob2faster fadein 2
    stop soundloop fadeout 1
    scene daliawest3 with dis2
    bla "Almost as if you could read each other's thoughts, you two up your pace at the same time, determined to make the other cum first." with dis
    mct "OH GOD."
    d "(OH JESUS...)"
    mct "Shit, I'm gonna cum too fast..."
    d "(Fuck, I'm gonna cum...)"
    d "(I'm not used to this sensation, it's not fair...)"
    if calypsohandjob:
        mct "You just lost your battle of power against Calypso, [mc]."
        mct "You can't lose here too..."
        mct "But..."
        mct "Fuck, Dalia's technique is just too fucking goooood...."
    else:
        d "Mmmmmh..."
    d "(I am enjoying sucking his cock as much as him eating my pussy...)"
    d "(What the hell is wrong with me...)"
    scene daliawest4 with dis2
    bla "After spending a few minutes in complete silence, only interrupted by Dalia's moans and whimpers, you start to feel the climax really close." with dis 
    mct "Shit, this is amazing..."
    bla "You lick up and down her perfectly shaved pussy and press your tongue in as far as you can get it."
    d "Mmmmh..."
    d "*Moaning more intensely* MMMmmm!!"
    mct "She's also close..."
    pause 
    play sound blow4
    stop soundloop2 fadeout 1
    show ed 109
    d "*Catching her breath* AAAaaaagh!"with dis
    d "F-FUCK, [mc!u]..."
    mc "Oh, Dalia..."
    d "You're not gonna win..."
    mc "It's you who won't be able to–"
    play soundloop deepthroat fadein 2
    scene daliawest5 with dis2
    mct "OH MY GOD."with dis
    bla "You suddenly feel your cock completely penetrating Dalia's throat, forcing you to stop your task for a second."
    mct "OH FUCK."
    mct "There's no way on earth she's doing that with her mouth..."
    mct "My god....."
    mct "How the hell can she take it so deep??"
    mct "Her throat offers no resistance at all..."
    mct "As if it lets me stretch it at will..."
    mct "O-O-Ohh shit I'm gonna cum."
    mct "Come on, [mc], make her cum first!"
    mct "Suck her clit."
    mct "You can do it..."
    menu:
        with dis
        "Cum [mt](ends scene)":
            mct "OH SHIT."with dissolve
            mct "I CAN'T–"
            jump cumfirstwestern
        "[gr]Make her cum first":
            mct "Oh fuck..."with dissolve
            menu:
                with dis
                "{size=35}Cum":
                    mct "OH SHIT."with dissolve
                    mct "I CAN'T–"
                    jump cumfirstwestern
                "[gr]Make her cum first":
                    play sound7 beat
                    mct "Oh my fucking god..."with dissolve  
                    menu:
                        with dis
                        "{size=40}Cum":
                            mct "OH SHIT."with dissolve
                            mct "I CAN'T–"
                            jump cumfirstwestern
                        "[gr]Make her cum first":
                            play sound7 beat
                            bla "{w=0.3}{nw}"with hpunch
                            menu:
                                with dis
                                "{size=65}Cum":
                                    mct "OH SHIT."with dissolve
                                    mct "I CAN'T–"
                                    jump cumfirstwestern
                                "[gr]Make her cum first":
                                    play sound7 beat
                                    bla "{w=0.3}{nw}"with hpunch
                                    menu:
                                        with dis
                                        "{sc=2}{size=85}Cum{/sc}":
                                            mct "OH SHIT."with dissolve
                                            mct "I CAN'T–"
                                            jump cumfirstwestern
                                        "[gr]Make her cum first":
                                            play sound7 beat
                                            bla "{w=0.3}{nw}"with hpunch
                                            menu:
                                                with dis
                                                "{sc=4}{size=115}Cum{/sc}":
                                                    mct "OH SHIT."with dissolve
                                                    mct "I CAN'T–"
                                                    jump cumfirstwestern
                                                "[gr]Make her cum first":
                                                    play sound7 beat
                                                    d "MMMMmmH!" with hpunch 
                                                    jump cumdaliawestern
    label cumdaliawestern:
    $ renpy.music.set_volume(0.5, delay=12.0, channel='music3')
    stop soundloop
    play sound cum4
    play sound2 slap1
    scene ed 113
    d "AAaaaagggghhghghhhh..." with hpunch 
    mct "Yes!"
    play sound3 cum4
    bla "Dalia orgasms, squeezing her legs together with astonishing force, and covering you in her juices." with hpunch  
    d "H-H-Holy fuck, [mc]..."
    d "Y-You son of a b-biiitch..."
    mc "I-I can't breathe..."
    play sound clothes5
    play sound4 chair2
    show ed 114 with dis2
    d "*Rolling onto her side and clumsily standing up* Lord have mercy..."with dis
    d "That was... WOW."
    d "I have trouble standing upright."
    d "I've never been happier to lose in a game in my life."
    play sound2 tablehit
    show ed 115
    bla "You grab Dalia's butt and you turn her around, slamming her against the table." with dis
    mc "I swear this booty of yours should be worshipped, Dal."
    show ed 116
    d "I don't know what you're trying to do, but I can still smack your face, you know?"with dis12
    d "Get off me."
    show ed 117
    mc "I just want to cum with you... take it as my prize for winning."
    show ed 116
    d "We're not gonna f-fuck."
    d "A-And I'm not giving you more head. My jaw hurts."
    d "Just t-take your victory home."
    show ed 117
    mc "I just wanna finish using these glorious ass cheeks of yours..."
    show ed 116
    d "My... ass cheeks?"
    show ed 117
    mc "Yeah, just..."
    $ renpy.music.set_volume(0.35, delay=12.0, channel='music3')
    $ renpy.music.set_volume(0.45, channel='soundloop2')
    play soundloop2 daliawest6 fadein 2 
    scene daliawest6 with dis2
    mc "Like this..." with dis 
    d "AAahh..."
    bla "You use Dalia's dripping juices to lubricate her own buttocks and use them as your personal toy, sliding your cock between them with ease."
    mc "Oh fuck yes..."
    mct "Dalia's ass is so huge... it almost envelops my entire cock."
    mct "And I love how soft it feels when she's not flexing it..."
    mct "If I close my eyes it almost feels as if I was fucking her..."
    bla "Dalia lets out a soft moan each time your cock rubs against her swollen, still sensitive pussy."
    d "Aaahhh..."
    mc "Oh babe..."
    stop soundloop2 fadeout 2
    play soundloop daliawest7 fadein 2
    scene daliawest7 with dis2
    bla "Almost unconsciously, you increase your pace, slamming your hips against Dalia's." with dissolve 
    mc "OH FUCK YES..."
    d "AAahh..."
    mc "God, Dalia..."
    mc "Everything about your body is so perfect..."
    mc "Firm and tight in all the right places... and irresistibly soft where it's meant to be..."
    mc "You drive me insane..."
    d "AAaahh..."
    mc "I wanna fuck you so bad..."
    mc "I want to bone you until neither of us can walk straight..."
    d "AAahh..."
    d "Not..."
    d "N-Not now. Not here..."
    mc "Does that mean... that you want me to fuck you another day...?"
    d "I..."
    d "M-Maybe in... another s-situation."
    d "Now s-shut up and hit me harder..."
    mc "Oh babe..."
    $ daliaslapwestern = False
    menu:
        with dis
        "[gr]Slap her ass":
            $ daliaslapwestern = True
            stop soundloop fadeout 2
            play sound6 rubbody
            scene daliawest8 with dis12
            pause 0.4
            play sound slap3
            play sound2 slap1
            play sound3 slap3
            pause .2
            d "AAAAahhggg....{w=1.1}{nw}" with dissolve
            scene ed 126
            d "Mmmmmhm..."with dis12
            mc "Was it too much? Did I hit you too hard?"
            d "N-No... it's okay..."
            mc "Tough girl..."
            play soundloop daliawest7 fadein 2
            scene daliawest10 with dis15
            d "AAaaahh..." with dissolve
            mc "Fuck, you have such sensitive skin, it's already all red..."
            d "*Playfully moaning* Mm-hm..."
            mc "You {i}did{/i} love that, right, you naughty girl?"
            d "F-Fuck yes..."
            mc "Oh boy..."
            mc "So you like it rough, eh...?"
            if penelopepath and donepotions:
                d "*Giggles* I d-don't know... m-maybe."
                mc "Just like her sis... interesting."
                mc "I guess it's in the genes..."
                d "Eh...? Penny?"
                mc "Yeah... she drank Veritaserum when we went to the Warthogs server and she admitted to... liking it rough."
                d "Hah..."
                d "I knew it."
                mc "Fuck, this feels so good, Dalia..."
                d "I..."
                d "I c-can take it harder than her."
                mc "Huh...?"
                d "I-I'm sure I can take it WAY harder than Penny..."
                mc "Oh god..."
                d "Spank me harder..."
                mc "Oh baby..."
            else:
                d "Fuck, I guess I do..."
            menu spankdalia:
                with dis
                "Spank her again [mt][gr](at least once)":
                    stop soundloop fadeout 2
                    play sound6 rubbody
                    scene daliawest9 with dis12
                    pause 0.4
                    play sound slap3
                    play sound2 slap1
                    play sound3 slap3
                    pause .2
                    d "AAAAahhggg....{w=1}{nw}" with dissolve
                    play soundloop daliawest7 fadein 2
                    if menudjdbdf:
                        scene daliawest11 with dis15
                    else:
                        scene daliawest10 with dis15
                    d "Mmmmmmm..."with dissolve
                    if menudjdbdf:
                        $ menudjdbdf = False
                        d "(Shit... I really like this...)"
                        d "(What is wrong with me...)"
                        d "(I love how he's slamming his hips against mine...)"
                        d "(How his balls pound my pussy with each thrust...)"
                        d "*Moaning* Mmmm..."
                        d "(God, he's so strong.)"
                        d "(I almost would like to...)"
                        d "(Do I really want [mc] to... fuck me?)"
                        d "(Fuck, who am I kidding, OF COURSE I DO...)"
                        d "(He's... the one...)"
                        d "MMMmmmmmmmhhmmm..."
                    jump spankdalia
                "Continue the butt job":
                    mc "Aaagh fuck yes..." with dissolve
                    jump daliacumwest2
        "Continue the butt job":
            mc "Aaagh fuck yes..." with dissolve
            jump daliacumwest2
        "[red]Penetrate her":
            stop soundloop fadeout 1
            play sound5 rubbody 
            scene ed 118 with dis
            mc "I can't bear it anymore, Dalia..."with dissolve
            mc "My instincts are taking control of me..."
            d "*Panting* A-Are you done...?"
            show ed 119
            mc "Almost..."with dis12
            play sound slap1
            play sound2 penetration2
            play sound3 tablehit
            show ed 120
            mc "AaAaaaaghh... YEAH!" with hpunch
            d "EE-E-EGH...?!"
            mc "OH GOD, IT'S SO FUCKING TIGH–"
            play sound punch 
            play sound5 slap3
            play soundlow earringing
            play sound3 slam
            play sound4 woodhit
            stop music3 
            scene daliahitwe with hpunch
            pause .5
            play soundloop birds fadein 10
            mc "AAAAghh..." with dis15
            mc "W-Why did you hit me..."
            play sound clothes3
            show ed 123
            mc "*Standing up* Agh... what is wrong with you?"with dis14
            mc "What a way to kill the mood..."
            show ed 122
            d "ME?!"
            d "What the fuck is wrong with YOU?!"
            show ed 123
            mc "I-I thought it's what we both wanted!"
            show ed 122
            d "Are you fucking serious right now?"
            d "Didn't you hear me saying I did NOT want that?!"
            show ed 124
            d "Oh my god, I feel so... violated."
            d "This was a huge mistake."           
            show ed 123
            mc "Come on, there's no need to make a fuss about it."
            show ed 122
            d "Can you shut the fuck up, you fucking pig?"
            show ed 124
            d "It might not mean shit to you, but to me, I..."
            d "I want my first..."
            show ed 122
            d "Y-You know what? I don't have to give you any fucking explanations."
            d "Forget me."
            play sound clothes2
            play sound2 belt
            show ed 125
            bla "Dalia starts picking up her clothes and getting dressed." with dis12
            mc "Okay, okay, I fucked up, I'm sorry."
            mc "We have to come back to the town together, so it'll be better if–"
            d "I'll take the horse. Alone."
            mc "And how am I going back?"
            play sound doorslam
            play sound2 slam3
            d "*Slamming the door* FIGURE IT OUT!" with hpunch 
            $ daliapath = False
            $ daliau = False
            mc "*Sighs* (Damn, she's angry.)"
            mct "I shouldn't have done that..."
            show ed 43
            mct "But well, it's not the first time she’s reacted like this." with dis15
            mct "I'll give her a couple of days, and then everything will be back to normal."
            mct "Or so I hope..."
            mct "At least the storm seems to be over."
            mct "I'll have to steal that emaciated horse I saw at the shed next to the cabin."
            mct "Man, this is gonna be one long way back..."
            $ daliarapewestern = True
            jump westernending


label daliacumwest2:
    mc "*Panting* Shit, I'm almost there..."
    mc "I'm g-gonna cum, Dalia..."
    stop soundloop fadeout 1
    play sound rubbody
    play sound2 wood
    scene ed 129
    bla "Dalia gracefully lifts her legs and rolls over, settling on her back with poise."with dis15
    mc "Fuck, Dalia, you're not gonna leave me hanging now, right...?"
    mc "I don't even know how I've managed to last for so long..."
    show ed 128
    d "I want you to finish on... my face. Not on my back."
    show ed 129
    mc "Do you want... a facial?"
    play sound rubbody
    play soundlow wood volume 0.4
    if daliaslapwestern:
        scene ed 130
    else:
        scene ed 130b
    d "Is that okay...?"with dis12
    if daliaslapwestern:
        scene ed 131
    else:
        scene ed 131b
    mc "What kind of question is that?"
    mc "Come here..."
    show ed 132
    bla "You get closer to Dalia and after so long, it only takes you a couple of strokes to unload everything you've been holding in." with dis12
    play sound cum2
    play sound2 cumall
    play sound3 cum4
    scene ed 133
    mc "AAAAAAAAARGHHHHH...."with hpunch 
    play sound cum2
    play sound2 cumall
    play sound3 cum4
    mc "FUCK YESSS..."with hpunch
    show ed 134
    mc "Oh my fucking god..." with dis12
    mc "I left my balls empty..."
    d "I can see that..."
    show ed 135
    d "AAaahh..." with dis14
    mc "Oh Lord, Dalia..."
    play sound blow6
    show ed 136
    bla "Dalia leans forward and starts skillfully polishing your cock head, swallowing it all and not leaving a trace of cum behind." with dis14
    play sound6 blow2
    d "*Swallowing* MMMMmmmmhh..."
    play sound2 blowpop
    show ed 137 with dis17
    mc "O-O-Oh my god..."with dis06
    mc "You're gonna end up developing a fetish for swallowing my cum..."
    d "*Giggles* If I don't have it already..."
    mc "Good grief..."
    mc "Each thing you say makes me obsess more about you."
    d "I hope you enjoyed the... competition."
    d "I certainly did... even if I lost."
    mc "I'd say it's been more of a tie."
    d "*Giggles* Yeah. I like that better..."
    play sound chair2
    play sound5 clothes3
    if daliaslapwestern:
        show ed 138b
    else:
        show ed 138
    bla "Dalia comes down from the table and grabs a rag from the kitchen to clean her face." with dis15
    if daliaslapwestern:
        d "Damn, my butt is burning like hell."
        d "I bet you left a mark."
        mc "A mark...?"
        mc "Maybe a bit. You can hardly see it."
        d "*Giggles* You're a terrible liar, [mc]."
    else:
        d "*Sniffing the rag* This is an... intense smell."
        mct "She's a devious freak... I love it."
    jump daliawesternposscene


label cumfirstwestern:
    stop soundloop
    play sound cum2
    play sound2 cum3
    play sound3 cum4
    scene ed 110
    mc "*Cumming inside Dalia's throat* AAAAAAAAARGHHHHH...."with vpunch  
    play sound cum2
    play sound2 cum3
    play sound3 cum4
    scene ed 110b
    mc "AAAAAHH YEAaahhh..." with vpunch 
    play sound cum2
    play sound2 cum3
    play sound3 cum4
    $ renpy.music.set_volume(0.5, delay=20.0, channel='music3')
    scene ed 111
    mc "*Still cumming* Oo-Ohhhh..." with vpunch
    mc "F-Fuck yes..."
    mc "Take it all, babe..."
    play sound blow2
    d "*Swallowing* MMMMmmmmhh..."
    mc "Good girl..."
    mc "You like that, don't you?"
    d "*Assertively* Mm-hmm..."
    play sound2 blowpop
    show ed 109 with dis17
    bla "Dalia laps every last bit of cum, skillfully licking your cock until it gleams, leaving not a trace behind."with dis06
    d "F-Fuck... you're gonna make me develop a fetish for this..."
    mc "Yes, please..."
    play sound clothes5
    play sound4 chair2
    show ed 112 with dis2
    d "*Rolling onto her side and clumsily standing up* A-Anyways... I think t-this is a v-victory!"with dis
    mc "I've never been happier to lose a game."
    mc "That was simply too much for me to handle..."
    show ed 114
    d "It really was... my jaw hurts." with dis
    mc "When it comes to this, you're a goddess..."
    show ed 112
    d "*Giggles* T-Thanks." with dis
label daliawesternposscene:
    stop music3 fadeout 11
    play sound clothes5
    scene ed 140 with dis2
    $ renpy.music.set_volume(1.0, channel='soundloop')
    $ renpy.music.set_volume(1.0, channel='soundloop2')
    play soundloop birds fadein 12
    bla "You both pick up the clothes scattered through the cabin and start getting dressed." with dis 
    show ed 139
    d "This was fun."
    show ed 140
    mc "I'm glad we share the same opinion."
    show ed 139
    d "It's certainly been... a way to pass the time until the sandstorm was over."
    show ed 140
    mc "Oh wow, the sandstorm, it's true."
    mc "I had forgotten about it."
    show ed 139
    d "I wonder why..."
    show ed 140
    mc "I was too focused on more important things."
    show ed 139
    d "I bet."
    show ed 140
    mc "Hey, a wise man knows the importance of setting his priorities right."
    show ed 141
    d "*Sighs* I guess we have to go back to town now, though."with dis08
    d "By the time we get there it'll already be night time."
    d "Too bad the whole trip has been in vain."
    d "The cabin was empty and we didn't discover anything about El Coyote or the Gem of Doom."
    show ed 140
    mc "Well, I wouldn't say in vain..."
    d "*Snorts* Hmm."
    show ed 139
    d "Come on, let's go back to Blackridge."
    show ed 140
    mc "Let's go!"
    play sound dooropenclose
    scene ed 142 with dis25
    play sound3 wind4 fadein 3
    mc "*Stepping out of the cabin* Wow... what a view."with dis12
    d "Yeah, the sandstorms take all the clouds with them."
    mc "The mortal danger they involve seems almost worth it now."
    d "*Chuckles* For real."
    play soundloop2 waves2 fadein 8
    stop soundloop fadeout 9
    show ed 143 with dis22
    bla "You lead the horse to the nearby pond so she can drink before making your way back." with dis
    play sound horse fadein 2
    show ed 144
    d "*Patting the horse* Easy, girl..."with dis14
    d "Everything's over, it's safe now..."
    mc "Is she okay?"
    d "Yeah, just a bit startled because of the storm."
    d "But she seems to be calming down now that she drank some water."
    show ed 145
    d "I'm gonna climb up that hill to make sure we're going in the right direction." with dis
    d "It'll be already dark by the time we get to Blackridge, so we won't be able to use the sun to orient ourselves."
    mc "Alright!"
    play soundlow snow4
    show ed 146 with dis14
    play sound horse2
    mc "*Patting the horse* Easy now, Roach."with dissolve
    mc "That storm was scary, eh?"
    play sound4 horse2
    mc "Don't worry, we all get scared sometimes."
    mc "Dalia was scared to ride you before coming here, and look at her now."
    show ed 147
    d "*Laughs* I can hear you, you know?"
    play soundlow snow4
    show ed 148
    d "*Walking backwards* I told you I'm not scared of horses!" with dis12
    play sound rope2
    d "*Stepping on the rope* In Ekabar I've literally ridden grypho–"
    play sound rope
    play sound2 ropetrap
    scene ropedalia 
    pause 0.08
    scene ropedalia2 with vpunchslow
    pause .7
    stop soundloop2 fadeout 10
    play music western3 fadein 4
    d "Huh...?" with dis08 
    scene ed 150
    d "U-U-U-UHHH...?!" with dis
    play sound5 whoosh6
    scene daliarope3 with Dissolve(0.05)
    pause 0.1
    d "W-What the fuck?!" with hpunch 
    mc "Fuck, Dalia! Are you okay?!"
    mc "What happened?"
    d "I-I don't know, I think I stepped on a trap!"
    mc "*Letting out a cheeky chuckle* O-Okay, let me help you get down."
    scene ed 152
    d "I heard you laughing!"
    mc "*Chuckles* I mean, it's pretty comical seeing you like this."
    d "Oh, yeah, super funny!"
    d "Next time you're the one trapped I'm gonna laugh too!"
    d "This could ha–"
    scene ed 153
    d "Shit, [mc], be careful!"with hpunch 
    d "Behind you!"
    play sound2 whoosh6
    show ed154
    mc "*Turning around* Huh?" with hpunch 
    mc "Oh fuck..."
    play sound swallow
    mc "*Gulps* Um... h-hey buddy! Great day to fish, eh?"
    mct "We're dead."
    scene ed 155
    boo "*In a surprising high-pitched voice* Hah! You can say that again, buddy!" with dis12
    boo "Pleased to meet another fishing enjoyer, the name's Boone."
    show ed 157
    mc "Oh." with dis
    mc "That wasn't the reaction I was expecting."
    mc "But... nice to meet you!"
    show ed 156
    boo "You say that because of my appearance?"
    show ed 157
    mc "Well..."
    show ed 156
    boo "Haha! I get that a lot, no worries."
    boo "I usually scare people off because I'm a big guy and I look kind of angry."
    boo "Blame my father for this angry grin!"
    show ed 153
    boo "Sorry about that, miss." with dis
    boo "I just set a few traps around in an attempt to catch the Chupacabra."
    d "D-Don't worry."
    d "I'm actually relieved to see that you're a nice guy."
    show ed 157
    mc "Did you say... the Chupacabra?"with dis
    show ed 156
    boo "Yeah! A creature that attacks and drinks the blood of livestock."
    boo "I've seen him a couple of times at night, but the little rascal always gets away from me."
    show ed 157
    mc "That's so cool! What's it look like?"
    show ed 156
    boo "It's like a mix between a dog and a big boar."
    boo "Picture this: it's got these cool spines all along its back, and its fangs are absolutely massive. Quite a sight, I tell you!"
    boo "He's smaller than Bigfoot, but much more elusive."
    show ed 157
    mc "Are there Bigfoots in these mountains too?!"
    show ed 156
    boo "Indeed! I saw one last month."
    boo "But they're gentle creatures, so I try to protect them from other hunters."
    boo "I was actually leaving them some food in a nearby cave when the sandstorm started."
    show ed 157
    mc "Wow! I'd love to see one."
    show ed 156
    boo "If you like mythological creatures, you should visit the Tumbleweed server."
    boo "The old mines are infested with Wendigos."
    show ed 159
    mc "Oh, yeah! I heard about that place!" with dis14
    boo "According to what people say, a group of NPCs was stuck inside the old mines for weeks."
    boo "After weeks trapped, they ended up having to resort to cannibalism, so they were cursed and turned into Wendigos, ghoul-like monsters that devour people."
    mc "Wow..."
    boo "Of course, these are all rumors, but... you never know. Look at the werewolf attacks from The Red Herring."
    mc "Oh my, tell me more about that!"
    d ". . ."
    d "*Clears throat* That sounds fascinating, guys, but... my blood is starting to rush to my head, you know."
    play sound holster2
    show ed 160
    boo "*Drawing his revolver* Oh shit, I'm sorry, miss." with dis12
    boo "I get sidetracked sometimes."
    d "Wait, wait, wait, are you gonna try to shoot the rope?!"
    d "What if you hit me?!"
    show ed 161
    boo "Don't worry, my aim is excellent!"
    d "B-But–"
    play sound revolver
    play sound7 ["<silence 0.1>", ropesnap]
    pause .4
    play sound2 fall3
    play sound3 fall2
    play sound4 fall
    play sound5 punch
    play sound6 debris
    show ed 162 with dissolve
    pause .5
    boo "Ouch, you okay?" with dis15
    d "*Muffled voice* ...y-yeah."
    d "*Muffled voice* Thank you."
    show ed 156
    boo "Anyway, I don't wanna bother you any more, guys."with dis 
    boo "And sorry again about the trap."
    show ed 157
    mc "Actually, we came here looking for you."
    mc "We were hoping you could help us find El Coyote."
    mc "He has... something we need."
    show ed 158b
    boo "Ugh, my old gang leader? Those were bad times."with dis08
    boo "I didn't like their modus operandi, so I quit the gang."
    play sound debris
    show ed 163
    d "*Standing up* Do you know where we could find him?" with dis
    d "We just know he wears a red bandana and has blue eyes."
    show ed 158b
    boo "If he's in Eternum, he'll be either in this server, or one of the other two bases we used to have."
    show ed 158
    boo "I have some maps and indications in my cabin back there, I could give them to you."with dis08
    show ed 157
    mc "Really? You don't mind?"with dis08
    show ed 156
    boo "Not at all."
    boo "I owe him nothing. He was a nasty man."
    boo "He wanted to hunt down all the Bigfoots, can you believe it?"
    show ed 157
    mc "*Gasps* Despicable!"
    show ed 163
    d "Will it take long?"
    d "I should really log off soon, mom gets mad if we're still playing by dinner time."
    show ed 158
    boo "Maybe a bit, but no worries, there's another Exit Portal not too far from here."
    boo "You don't have to go back to Blackridge."
    show ed 164
    mc "Hmmm... at least one of us should go back to Blackridge, though."with dis12
    mc "To tell Alex and Calypso what we found out, and let them know we're okay."
    show ed 163
    d "Yeah, that might be best..."
    d "You go back to Blackridge. I'll go with Boone to learn about El Coyote's hiding spots."
    d "If... he doesn't mind."
    show ed 156
    boo "Not at all, miss. I like to help kind people."
    boo "And I'll be happy to show you my cabin."
    show ed 157
    mc "Oh... actually, we saw it already."
    mc "We took shelter there during the sandstorm."
    show ed 165
    d "Y-Yeah, sorry if some things are... out of place."
    show ed 156
    boo "Ah, I recognize that sudden blush, miss!"
    boo "Don't worry guys, you're not the first couple to make love in my cabin during a sandstorm."
    boo "It's quite a love nest, eh?"
    show ed 157
    d "W-What?!"
    d "W-We didn't!"
    show ed 165
    d "I mean... w-we didn't have... sex."
    d "We..."
    show ed 166
    d "Well... it depends on what you mean by “sex”."
    d "I guess that..."
    show ed 165
    d "*Clears throat* A-Anyway, let's go to the cabin, yeah."
    d "I'll help you... sweep up."
    show ed 156
    boo "*Chuckles* Ah, I love young love!"
    show ed 158
    boo "Alright guys, let's get going, then."with dis08
    boo "If you really want to go to Blackridge today you'll have to hurry up."
    show ed 157
    mc "Yes, sir!"with dis08
    mc "Thank you so much for helping us."
    show ed 156
    boo "Don't mention it."
    stop music fadeout 7
    play soundloop waves2 fadein 7
    play soundlow snow4
    show ed 167 with dis15
    mc "Well, I'll take Roach with me, then."with dis06
    mc "Don't worry, I'll take good care of her."
    show ed 168
    d "*Chuckles* I'm sure you will."
    show ed 167
    mc "I'll see you later at home."
    show ed 168
    d "Sure."
    d "And... hey, thank you."
    show ed 167
    mc "Huh?"
    show ed 168
    d "Thank you for... respecting me."
    d "You know, back there in the cabin."
    show ed 167
    mc "Hmm?"
    if daliaslapwestern:
        mc "Is this... you being sarcastic because of the spanking?"
        show ed 169
        d "*Laughs* Nah, that was actually... surprisingly stimulating."
    else:
        mc "Is this... you being ironic?"
        show ed 169
        d "*Laughs* No!"
    show ed 168
    d "I mean that... I know you'd probably have liked to do “more”."
    d "But I didn't want to. And you didn't pressure me."
    show ed 168
    d "I appreciate that."
    show ed 167
    mc "Of course, Dalia."
    mc "We were just having fun there. If one of us stops being comfortable with something, it stops being fun."
    $ dalia_points += 1
    play sound beat
    show screen heartbeat
    show ed 168
    d "We certainly did have fun, yes..."
    show ed 167
    mc "If you ever want to have some more fun... you know where to find me."
    show ed 169
    d "*Chuckles* Oh, I'm sure you're always up for some... fun."
    show ed 168
    d "See you later, [mc]."
    show ed 167
    mc "Goodbye, Dalia."
    play soundlow snow4
    show ed 146 with dis17
    mc "Well, looks like it's just you and me now, Roach."with dis06
    play sound horse2
    play sound2 horse2
    mc "I hope you like my company, because it's quite a long road back to Blackridge."
    boo "You ready, miss?"
    d "Sure!"
    boo "I've gotta ask, what's your favorite species of sturgeon fish? I can prepare you a quick snack."
    d "Um... are there more than one?"
    boo "What?! There are dozens of them!"
    d "Really?"
    boo "I can give you a quick summary, don't worry!"
    d "Erm..."
    boo "First, the White Sturgeon, native to the Pacific Northwest of North America. Believe it or not, they can reach lengths of over 20 feet!"
    d "...a-aha."
    mc "*Laughs* Looks like Dalia won't be bored either."
    jump westernending




label alexwestern:
    $ westernalex = False
    stop soundloop fadeout 9
    scene ex 1 with dis2
    play music2 western2 fadein 5
    play soundlow horse
    mct "Mmm... so many people in here."with dis08
    player "Step right up, folks!"
    player "This miracle tonic will harden your dick faster than a horse can gallop!"
    player3 "Hats and duster coats at half price... buy your new hat here..."
    player2 "Come try Ol' Terry's Brothel, gentlemen! We have the best ladies in all of Eternum!"
    mct "I feel like more players have arrived since I first logged in."
    mc "*Sighs* (Good luck trying to find Alex.)"
    $ renpy.music.set_volume(0.0, channel='music2')
    play sound3 jumpscare2
    show ex2b
    x "BOO!{w=0.8}{nw}"with hpunchlong4
    $ renpy.music.set_volume(0.5, delay=6.0, channel='music2')
    play sound fall3
    play sound2 fall
    scene ex 4 
    mc "*Falling down* GGGGHhh..." with dis
    mc "C-CAN YOU STOP DOING THAT?!"with hpunch 
    blank "{i}Alex snorts, trying to hold her laugh."
    play soundlow debris
    show ex 5
    mc "*Standing up and dusting yourself off* Why?!"with dis12
    show ex 6 
    x "*Giggles* Cause it's funny!"
    show ex 5
    mc "Oh, yeah, hilarious."
    mc "Laugh now while you can, Alex."
    mc "I'll get you back one day... beware!"
    show ex 6
    x "Sure, sure, I've been waiting since the last time you said that."
    show ex 5
    mc "Just wait..."
    show ex 6
    x "*Giggles* Anyways, cowboy... tell me, did you discover anything?"
    show ex 5
    if not westerndalia:
        mc "About El Coyote? Nah, not much. Dalia and I got a tip from the sheriff, but I'm still not sure if it'll pan out."
    else:
        mc "About El Coyote? Nah, not yet."
    if not westerncalypso:
        mc "I've been mostly wandering around town."
        show ex 9
        x "Oh, really...? Because I saw you going into that hotel with Calypso." with dis
        show ex 10
        mc "W-What? When?"
        show ex 9
        x "A while ago."
        x "Is there something I need to know?"
        show ex 10
        mc "Um... no. It's not what it seems."
        show ex 9
        x "You're not fucking our Weapon of Atlas, right [mc]?"
        show ex 10
        mc "O-Of course not!"
        mc "We had an incident with some stupid clerk that shot the deputy, and she ended up covered in blood."
        mc "She was nauseated, so I accompanied her to the hotel so she could bathe and clean herself."
        show ex 9
        x "You sure?"
        x "No sex with our super-advanced-AI Princess until today's mission is over, [mc]."
        show ex 10
        mc "I-I didn't have sex with anyone!"
        mc "I've been busy enough trying to avoid the Praetorians all over the town."
    else:
        mc "Praetorians are in the town, so I preferred to keep a low profile and not start asking questions to everyone."
    show ex 8
    x "Ah, yeah, I saw them."with dis
    x "I don't know why they are here, but if we don't get in their way we should be fine."
    show ex 7
    mc "In the saloon they said they were looking for some kind of cube-like object."
    show ex 8
    x "A cube? Hmm... I wonder what that could be."
    show ex 7
    mc "No idea. But I doubt it's related to the Gems of Doom."
    mc "Or to El Coyote for that matter."
    show ex 6
    x "Ah, yes, speaking of which, I got a promising lead."with dis
    x "The mine foreman spilled the beans and said El Coyote is, as we suspected, hiding out in this server."
    x "According to him, he stands out with his piercing blue eyes and a red bandana always covering his face."
    show ex 5
    mc "Blue eyes and a red bandana, huh..."
    mc "That's good info."
    show ex 6
    x "I think we should start checking out all the buildings until–"
    show ex 11
    bla "Alex suddenly stops talking and looks behind you."with dis12
    mc "Huh?"
    mc "You okay?"
    x "You've got to be kidding me..."
    show ex 12
    x "Are you seeing that guy over there?"with dis 
    x "Under the mine's ramp."
    mc "Shit, a red bandana! Is that our guy?"
    show ex 13
    x "*Hiding behind the corner* I don't know... but it's possible."with dis12
    x "Does he look like the leader of a gang to you?"
    x "Or... a Gem of Doom owner?"
    x "He looks pretty normal to me."
    show ex 14
    mc "Well, not everyone has to look like a destroyer of worlds like Thanatos."
    mc "I look pretty “normal” too and I have two Gems of Doom."
    show ex 13
    x "Hah, yeah, fair enough."
    x "That's why you're the perfect holder. Most players wouldn't even bother looting you."
    show ex 14
    mc "Really? Do I look that amateur?"
    show ex 13
    x "You look like someone who just started playing Eternum today, a total noob."
    show ex 12
    mc "Goddammit, I've gotta get myself some flaming horns..."with dis 
    show ex 15 
    bla "The man turns around and disappears behind the wooden structure." with dis12
    x "Look, he's moving!"
    show ex 16
    x "Alright, this is our chance!"with dis
    x "We can't let him get away!"
    x "We have to find out where he's hiding. It's highly likely he's not carrying the Gem of Doom with him at the moment."
    show ex 17
    mc "Gotcha." with dis08
    mc "Stealth mode, activated."
    mc "Let's get him!"
    show ex 18 with dis2
    bla "You follow the man to a deserted area behind the mine."with dis08
    play soundlow debris
    show ex 19 with dis12
    mc "*Whispering* What is he doing?" with dis08
    x "*Whispering* I don't know. Smuggling?"
    mc "*Whispering* That would check out."
    mc "*Whispering* Do we have a plan?"
    x "*Whispering* I certainly don't."
    x "*Whispering* Should we knock him out?"
    mc "*Whispering* I mean, we don't even know if he's El Coyote."
    x "*Whispering* Mmm, fair enough."
    x "*Whispering* Okay, I have an idea."
    mc "*Whispering* Enlighten me."
    x "*Whispering* We sneak up behind him and..."
    show ex 20
    x "And... aaahh... aaaaahhh..."with dis08 
    stop music2 fadeout 1
    $ renpy.music.set_volume(0.8, channel='soundloop2')
    play soundloop2 westerntown1 fadein 1
    play sound sneeze2
    play sound2 sand
    scene ex21
    x "*Sneezes* Ah-choo!" with vpunch 
    mc "Shit."
    play sound holster
    play soundlow debris
    scene ex 22
    player "*Grabbing his revolver* What the fuck was that..." with dis12
    player "HELLO?"
    show ex 23
    x "Shit, shit, shit... we're fucked!"with dis
    show ex 24
    mc "What the hell, I thought you were not supposed to have symptoms inside Eternum!"
    show ex 23
    x "I-I don't know, maybe I sneezed in the real world, or... or my brain still thinks I'm sick, I don't know!"
    show ex 24
    mc "What do we do? He's coming!"
    show ex 23
    x "Fuck, I-I don't know!"
    x "If we start running he'll see us and probably flee to another server."
    x "B-But if we attack him we might never know where he hid the Gem!"
    show ex 24
    menu:
        with dis
        "Punch me":
            mc "Punch me!"with dissolve
            show ex 26
            x "What?!" with dis08
            show ex 25
            mc "If he sees us here doing nothing he'll suspect us!"
            mc "We've gotta fake a fight!"
            show ex 26
            x "A fight...?"
            x "That's not gonna work."
            play sound6 holster
            show ex 24
            player "*Speaking from behind the corner* I know you're there... SHOW UP!"with dis08
            mc "*Whispering* Quickly! Hit me in the stomac–"
            play sound punch
            play sound2 whoosh6
            play sound3 bonebreak
            stop soundloop2
            scene ex24b 
            mc ". . ." with hpunchlong2
            play sound5 whoosh6
            scene ex24c
            player "*Jumping from the corner* Hands up!" with hpunch
            play sound debris
            play sound2 fall3
            play sound3 fall
            play music2 western4 fadein 5
            scene ex 31 with dis 
            mc "*Collapsing to the ground* {size=25}{bt=3}My stomach....{/bt}" with dis 
            player "W-What is going on here?"
            scene ex 31b
            x "This fucking creep didn't understand what a “no” means, that's what happened."
            x "Are you his friend? Do you want some medicine too?"
        "[gr]Kiss me":
            $ alexkisswest = True
            mc "Kiss me!"with dissolve
            show ex 26
            x "I'm sorry...?" with dis08
            show ex 25 
            mc "If he sees us here doing nothing he'll suspect us!"
            mc "But if he sees us kissing he'll think we're just a couple trying to find a quieter spot!"
            show ex 26
            x "What kind of fucked-up plan is that?"
            x "Do you think we're in some sort of rom-com or what?"
            show ex 25
            mc "Well, if you have a better idea, I'm all ears!"
            if not alexpath:
                show ex 26
                x "I {i}do{/i} have a better idea, actually."
                x "Listen, we have to–"
                $ westkissfix = True
            play sound holster
            show ex 24
            player "*Speaking from behind the corner* I know you're there... SHOW UP!"with dis08
            if not alexpath:
                play sound punch
                play sound2 whoosh6
                play sound3 bonebreak
                stop soundloop2
                scene ex24b 
                mc ". . ." with hpunchlong2
                play sound5 whoosh6
                scene ex24c
                player "*Jumping from the corner* Hands up!" with hpunch
                play sound debris
                play sound2 fall3
                play sound3 fall
                play music2 western4 fadein 5
                scene ex 31 with dis 
                mc "*Collapsing to the ground* {size=25}{bt=3}My stomach....{/bt}" with dis 
                player "W-What is going on here?"
                scene ex 31b
                x "This fucking creep didn't understand what a “no” means, that's what happened."
                x "Are you his friend? Do you want some medicine too?"
                $ alexkisswest = False
            else:
                play sound2 whoosh6
                play sound3 woodhit
                scene ex24b2
                bla "You grab Alex and push her against the wall." with hpunchlong2
                scene ex 33
                mct "Shit, was I too rough?" with dis12
                x ". . ."
                mct "I can never guess what Alex is thinking."
                mc "Um... maybe we shou–"
                stop soundloop2 fadeout 1
                play sound2 debris
                play sound clothes2
                show ex 34
                bla "Alex grabs you by the collar of your shirt, pulling you closer until your lips meet." with dis08 
                mc ". . ."
                x ". . ."
                play sound3 woodhit
                play music2 western4 fadein 7
                show ex 35 with dis
                bla "Almost without any conscious realization, you suddenly find yourself immersed in a deep, intense kiss." with dis12
                play sound5 whoosh6
                scene ex24c
                player "*Jumping from the corner* Hands up!" with hpunch
                scene ex 35
                player ". . ."
                player "Oh."
                bla "Your lips mash against Alex's in perfect sync, as she hungrily pushes back, tangling her tongue with yours."
                mct "My god..."
                bla "She even lets out a soft moan when you squeeze her ass."
                $ alex_points += 1
                play sound5 beat
                show screen heartbeat
                x "Mmm..." with dis06
                scene ex 36
                bla "Reluctantly, but with a lingering touch, Alex pulls away from the kiss, her eyes searching yours for reassurance." with dis12
                mc "Whoa..."
                x ". . ."
                show ex 28
                x "Um..." with dis 
                x "*Clears throat* A-AHEM!"
                play sound2 punch
                x "*Pushing you away* W-What are you looking at, weirdo??"with hpunch 
                x "Do you want tickets to watch the show?!"
    play sound holster
    show ex 37
    player "Whoa, whoa, take it easy, miss." with dis
    player "I'm just here to sell grade-one opium."
    player "I thought you were one of my competitors, or... worse, the Sheriff's deputy."
    scene ex 31b
    x "Well, as you see, I'm neither."
    x "So get the fuck out of my sight."
    show ex 37
    player "Heh, with pleasure."
    player "Have a nice day, miss."
    show ex 27
    bla "The dealer holsters his weapon and goes back to his business."with dis12 
    if alexkisswest and alexpath:
        show ex 38 with dis14
        mc "Wow..." with dis
        mc "That was... the most intense kiss of my life."
        show ex 39
        x "Y-Yeah, well, I... I wanted to make it believable."
        show ex 38
        mc "You certainly succeeded..."
    else:
        show ex 38
        mc "*Standing up* T-That was... a good kick." with dis12
        show ex 41
        x "Thanks. I wanted to make it believable."
        show ex 40
        mc "Y-You certainly succeeded."
    show ex 41
    if westkissfix:
        x "You played your part of the plan perfectly, [mc]. Nice job."
    else:
        x "I've gotta give it to you, that was a good plan."
        x "Fast thinking. Nice job, [mc]."
    show ex 40
    if alexkisswest and alexpath:
        mc "Easily one of my best plans ever. I'd lie if I said I didn't enjoy every second of it."
        mc "Didn't you...?"
        show ex 41
        x "I enjoyed... getting rid of that man so easily, yes."
        x "Even if he wasn't our man."
        show ex 40
        mc "Awh, it wasn't him?"
    else:
        mc "T-Thanks."
        mc "So... was he our man?"
    show ex 39
    x "Nah... El Coyote is supposed to have blue eyes."
    x "And besides, I doubt he'd be trying to smuggle opium in a moment like this."
    x "He wouldn't expose himself like this."
    show ex 38
    mc "Huh, you got a point."
    mc "We're back to square one, I guess."
    show ex 42
    x "It seems so."
    show ex 38
    mc "At least I know how he's supposed to look now, though."
    mc "If I find him around the–"
    stop music2 fadeout 3
    play sound risingshort3
    play soundloop westerntown1 fadein 2
    scene ex 43
    bla "An intense chill runs down your spine." with dis2
    mc ". . ."
    x "Are you okay...?"
    show ex 45 
    bla "You turn around and spot a man with a child in the distance."with dis12
    show ex 46 with dis15
    pause 
    play sound ["<silence 0.5>", steamtrain]
    show ex 47 with dis15
    pause
    mc "Did you see that...?"with dis
    x "See what?"
    mc "A man entered that building with... a little boy."
    mc "Can kids get into this server?"
    show ex 42
    x "They probably were NPCs."with dis
    show ex 38
    mc "What? Are there NPCs in Blackridge?"
    show ex 42
    x "Yeah, I think so. You know how the whole goal of Eternum is to be as immersive as possible."
    x "There are usually some NPCs scattered throughout the servers like these to prevent the worlds from feeling empty."
    x "They can be interacted with, although they don't carry anything valuable and they can't harm players, so most people just ignore them."
    x "In this case I think they're limited to some ranchers between the main towns."
    show ex 38
    mc "I see."
    mc "Although... I still have a bad feeling about what I saw."
    mc "Can we go check it out?"
    show ex 42
    x "Of course."
    x "We have time."
    play music westerndark fadein 6
    stop soundloop fadeout 11
    scene ex 47 with dis17
    pause 
    scene ex 48 with dis17
    pause
    play sound lantern
    show ex 49 with dis 
    player2 "*Lighting the lantern* Ah, much better... isn't it?"with dis06
    player2 "It's so nice to get away from the bustle of the town."
    play sound2 debris volume 0.4
    show ex 50
    player2 "*Kneeling down* Are you good now? Not too cold or too hot?" with dis12
    scene ex50
    kid "*Nods*"
    player2 "Good, good..."
    player2 "I bet that farm must be hot during summers."
    scene ex50
    kid "*Nods*"
    player2 "Alright, a promise is a promise. Let's play a game!"
    player2 "You must follow my instructions, alright? Like a Simon Says game!"
    player2 "Give me a moment to think..."
    player2 "Turn around and touch your left ear with a finger!"
    scene ex 52 with dis12
    player2 "*Sinister laugh* Hi-hi-hi, yes, yes!"with dis06
    player2 "This thing is well worth its price!"
    player2 "You can turn around."
    scene ex 50 with dis
    pause
    scene ex 53
    player2 "Good boy..." with dis12
    player2 "You're such a good boy, did you know that?"
    player2 "How old did you say you were? 9?"
    scene ex53
    kid "*Nods*"
    player2 "You're very clever for your age."
    kid ". . ."
    player2 "*Sinister laugh* Okay, time for the second step of the game!"
    player2 "I want you to–"
    play sound rocks
    play sound2 punch
    play sound3 whoosh6
    play sound5 blood2
    stop sound5 fadeout 4
    scene ex54
    bla "You punch the man with full force, propelling the man across the barn like a human projectile." with hpunch 
    play sound4 debris
    play sound6 holster
    scene ex 57
    player2 "*Crawling and backing off* E-Eh? What?!" with dis12
    player2 "Who are you?!"
    scene ex 56
    x "W-What were you trying to do with this kid, you fucking monster..."
    show ex 58
    mc "Don't answer that. We both know what you were going to do, and I prefer not to hear it from your revolting mouth."
    show ex 57
    player2 "T-This is not what it seems!"
    player2 "He's not a real kid!"
    show ex 58
    mc "Shut the fuck up."
    show ex 59
    player2 "L-Let me explain it to you!" with dis
    player2 "But please, don't shoot!"
    player2 "I-It's all about... THIS!"
    play sound ["<silence 0.6>", deception]
    play sound2 ["<silence 0.6>", deception]
    show ex 60
    bla "The man reveals a small, blue box."with dis12
    x "That thing..."
    mc "Yes... we've seen that before..."
    play sound3 deception2
    scene cf111 
    mct "That's Linus' device... from the party."with flashfaster 
    mct "The one that allowed him to control NPCs."
    play sound4 deception2
    scene ex 60
    mct "And now that I look at it closer..."with flashfaster
    mct "It weirdly reminds me of the box where Calypso was trapped when we found her too, just... smaller."
    mct "I don't think this is a coincidence. Perhaps Linus used technology stolen from Ulysses?"
    scene ex 49
    player2 "L-Let me show you what this artifact can do!"
    player2 "If I enter the ID number of an NPC, it gets linked to him, allowing you to control it!"
    player2 "But if you rotate this thing again, it goes back to normal. Look!"
    play sound glitch1
    show ex49
    pause 1.7
    scene ex 62
    kid "*Breathing nervously* E-Eh...?"with dis12
    kid "W-Where am I...?"
    play sound debris
    show ex 63
    x "*Kneeling down next to the kid* Hey! Don't worry, everything's alright."with dis
    x "*Speaking in a gentle tone* You fainted due to the sun, but we brought you here to recover."
    x "What's your name?"
    show ex 64
    jonas "Jonas."
    show ex 63
    x "Do you know where you live, Jonas?"
    show ex 64
    jonas "I-I do. I live near Blackridge."
    jonas "My father and I come to town every Saturday to deliver vegetables and other supplies to the stores."
    jonas "While I was waiting for my dad, a man approached me, and... then I don't remember what happened."
    show ex 63
    x "That's when you came down with heat stroke!"
    x "Do you want me to help you find your father?"
    show ex 64
    jonas "N-No... I know where he is."
    show ex 63
    x "Then you should hurry up!"
    x "He must be worried about you."
    show ex 64
    jonas "Yes... thank you, ma'am."
    play sound run
    show ex 58
    bla "The kid rushes out of the barn and runs towards the town."with dis15
    mct "Shit... this artifact has to be the thing Praetorians are looking for."
    mc "Where did you get this thing?"
    show ex 57
    player2 "What?"
    show ex 58
    mc "I won't ask twice."
    show ex 57
    player2 "I-I bought it on the black market!"
    show ex 58
    mc "From who?"
    show ex 57
    player2 "I don't know! Everything is done anonymously."
    player2 "The seller told me they had lowered costs and offered it only at 85K!"
    show ex 58
    mc "85K...? You paid 85,000 eternals to... use it on a child?"
    show ex 65
    player2 "Oh, for fuck's sake, it's not a child!"with hpunch 
    player2 "I would never do this in real life!"
    player2 "What's Eternum for, if we can't fulfill our darkest fantasies?!"
    player2 "He's just a bunch of lines of code and nothing else, don't you understand? It's not a real kid!"
    show ex 66
    mc "He once was."
    show ex 65
    player2 "What the fuck are you talking about?"
    show ex 66
    mc "We've talked enough."
    show ex 57
    player2 "Whoa, whoa, calm down, buddy!"
    player2 "O-Okay, I get it, what I did was wrong, I see it now!"
    player2 "I won't do it again, there's no need to take a violent turn!"
    player2 "Once it has been linked, the artifact cannot be used with another NPC, but... I... I can pay you!"
    player2 "I can transfer you 500 eternals RIGHT NOW if you let me go!"
    show ex 58
    menu:
        with dis
        "[gr]Kill him":
            show ex 57
            player2 "I can wire you 500 eternals as soon as I g–"with dissolve
            $ shootabuser = True
            play sound revolver2
            play sound2 revolver
            play sound3 shotgun
            play sound4 blood2
            play sound5 woodhit
            show ex67 with hpunch
            pause
        "Take the money and let him go":
            mc "Get the fuck out of my sight before I change my mind."with dis06 
            scene ex 57
            player2 "Thank you, THANK YOU!"
            play sound2 run
            play sound3 debris
            show ex 68 with dis17
            show screen eternals with dis08 
            play sound coins
            $ money += 150
            pause .05
            $ money += 150
            pause .05
            $ money += 200
            pause 
    stop music fadeout 7
    $ renpy.music.set_volume(1.0, channel='soundloop2')
    play soundloop2 westerntown1 fadein 6
    hide screen eternals
    scene ex 69
    x "God..." with dis17
    x "That was... absolutely repulsive."
    x "I think I'll have to take a moment to collect myself in the saloon before continuing the mission."
    x "I really need to get rid of the nasty taste in my mouth."
    show ex 70
    if shootabuser:
        mc "Well, we already knew plenty of despicable people play this game. It's not a surprise."
        show ex 71
        x "I know, but... seeing it first-hand still hits you."
        show ex 70
        mc "Yeah, I know what you mean."
        $ alex_points += 2
        play sound beat
        show screen heartbeat
        show ex 71
        x "I'm glad you killed that sick motherfucker." 
        x "I know it won't change much in the real world, but... at least he got what he deserved."
        show ex 70
        mc "Should we loot the body?"
        show ex 71
        x "If this artifact is what the Praetorians are looking for, I wouldn't touch anything."
        x "They'll find the corpse at one point or another, hopefully they'll see he still has all his inventory with him, confiscate it, and leave the server."
        show ex 70
        mc "Mmh, yes, that's probably best."
        mc "Do you want me to come with you to the saloon?"
        show ex 71
        x "Nah, don't worry. We still have to find this damn Coyote guy."
        show ex 70
        mc "You sure? Will you be okay?"
        show ex 71
        x "Of course. I just need some time to compose myself."
        show ex 70
        mc "Alright. Try thinking of good memories to recover the good mood."
        mc "It usually helps me."
        show ex 71
        x "Such as?"
        show ex 70
        mc "I don't know, the last swimming competition you won, you getting your first apartment, the feeling of the wind while you ride your bike..."
        if alexkisswest and alexpath:
            mc "That passionate kiss we had just a few minutes ago..."
            show ex 72
            x "*Snorts* Mmh."with dis06
        show ex 73
        x "Yeah, the feeling of the wind when riding my bike is definitely a great, great suggestion." with dis12
        x "Thank you, [mc]. I already feel better."
        mc "*Chuckles* Always happy to help."
        mc "Take care, Alex. I'll come find you if I discover anything."
        x "Mm-hm."
        x "See you later, [mc]..."
    else:
        mc "We already knew plenty of despicable people play this game. There's nothing we can do."
        show ex 69
        x "Well, not letting him go without a scratch would have been a start, honestly."
        show ex 70
        mc "What would have that changed?"
        mc "It's not as if we can kill or arrest him in the real world. This way we got 500 eternals, at least."
        show ex 69
        x "If you say so."
        x "It still turns my stomach."
        show ex 73
        x "*Sighs* Anyway, I really need to get a drink at the saloon." with dis12
        x "See you later, [mc]."
        mc "Sure. I'll come find you if I discover anything."
        x "Alright..."
    $ menualexline = True
    $ artifactexplanation = True
    jump secondmenuwestern



   
label secondmenuwestern:
    play sound steamtrain
    stop music fadeout 5
    stop music2 fadeout 5
    stop music2b fadeout 5
    stop soundloop2 fadeout 6
    play soundloop wind fadein 5 volume 0.4
    scene ee 1 with dis25
    if menucalyline:
        $ menucalyline = False
        mct "Holy shit, I can't believe that just happened."with dis 
        mct "If only it was me who could have touched her... oh boy."
        mct "Maybe in another life where I am born into a royal family."
        mct "Ahh, a man can dream..."
    elif menualexline:
        $ menualexline = False
        mct "Sometimes it's easy to forget how many sick bastards are out there." with dis
        mct "I guess this is another big reason to get the 10 Gems of Doom."
        mct "Whatever this world is, if we really get control of it one day... many things are going to change, that's for sure."
    else:
        mct "Okay, where should I go now..."with dis
    call screen westernmenu with dis14

label westernending:
    stop soundloop fadeout 5
    stop music2 fadeout 5
    scene black with dis25
    show screen afewhourslater with dis15
    pause
    play soundloop2 night fadein 5
    hide screen afewhourslater
    scene eee 1 
    with dis22
    if not daliacabin:
        bla "You spend several hours scouting the town and its surroundings without luck. It's not until nightfall that you finally arrive back in Blackridge feeling a bit disappointed."with dis15
        play sound2 snow4 volume 0.5 fadein 1
        mc "*Sighs* (Another dead end.)"
        mct "I feel like I've been walking in circles all day."
        mct "I hope Dalia had better luck."
    else:
        if daliarapewestern:
            bla "As night falls on Frontier Trails, you make your way back to Blackridge accompanied by the dying horse you found next to the cabin. After giving it a carrot, it dies."with dis15
            mct "F-Fuck, really? Was it allergic or something...?"
        else:
            bla "As night falls on Frontier Trails, you make your way back to Blackridge accompanied by Roach. After giving her a carrot, you leave her at the stables."with dis15
    x "[mc]! Over here!" 
    mc "Hmm?"
    play soundlow snow3
    show eee 2 with dis15
    mc "Ah, there you are!"with dis06
    play soundlow snow4
    show eee 4 with dis14
    mc "I was wondering if you'd still be here or not." with dissolve
    mc "Were you waiting for me?"
    show eee 3
    x "Hah, don't flatter yourself. We just got here a minute ago."
    show eee 8
    ca "We went to explore the cemetery, guided by tidings from a villager."
    show eee 9
    mc "Oh, that sounds thrilling."
    show eee 5
    x "Yeah, but we didn't find shit, for a change."
    x "Total waste of time."
    show eee 3
    x "What about you? Did you have better luck?"
    show eee 4
    if not daliacabin:
        mc "Nope, no dice."
        mc "Dalia went outside of town to track down an old member of the gang, so let's hope she found something useful and bailed from the server already."
    elif daliarapewestern:
        $ daliacabin = False
        mc "Nope, no dice."
        mc "Dalia and I... split up after going outside of town trying to track down an old member of the gang, so let's hope she found something useful and bailed from the server already."
    else:
        mc "We did, actually."
        mc "We found an old gang member of El Coyote, a man called Boone."
        mc "He mentioned knowing the locations of their hiding spots in other servers."
        show eee 3
        x "Huh, that {i}does{/i} sound promising."
        x "Nice job. At least we got something."
        show eee 4
        mc "Dalia went with him to get the info, and she was supposed to use another Exit Portal after that."
    show eee 8
    ca "She did. I stopped feeling her presence in this realm a few minutes ago."
    show eee 9
    mc "Ah, good."
    if not daliacabin:
        mc "We can ask her once we're back in the real world."
    show eee 3
    x "I guess we're all done here for today, then."
    show eee 4
    mc "I'd say we are."
    show eee 6
    x "Alright then, let me pick up the things I left in that alleyway and we'll be good to go."with dis
    mc "Do you want me to wait for you?"
    show eee 7
    if alexpath:
        x "Of course I do."with dis
        x "Do you think I'll let you log off in my apartment while I'm still playing? No chance."
        mc "*Chuckles* Ah true, I forgot. My bad."
    else:
        x "Sure, if you really want to..."with dis
        mc "I'll be right here!"
    show eee 7b
    mc "Well, thank you for your assistance, Princess." with dis14
    show eee 8
    ca "I am glad to have been of help."with dis
    if calypsohandjob:
        show eee 9
        mc "I hope you enjoyed your... second bath."
        show eee 8
        ca "I very much did, thank you."
    else:
        $ calypsopath = False
    show eee 9
    mc "Are you going back to Ekabar now?"
    show eee 8
    ca "I will."
    ca "After seeing firsthand how useful asking the locals can be, I will resume my search of Hyril'ar."
    ca "Hopefully with better results this time."
    play sound3 spell3 volume 0.6
    play sound2 spell2 volume 0.6
    play soundloop energy2 fadein 1
    scene eee 11 with dis12
    mc "I wish you the best of luck."with dis08
    show eee 10
    ca "If you need me from now on, you know where to find me."with dis08
    show eee 11
    mc "I do."with dis08
    mc "Have a good night, Princess."
    if calypsopath:
        show eee 10
        ca "Farewell... [mc]."with dis08
    play sound3 spell3
    play sound2 spell2
    play sound debris
    stop soundloop fadeout 1
    scene eee 12 with flashfast
    mc "Farewell..." with dis
    scene eee 1 
    mc "*Taking a deep breath* Aah..." with dis15
    mct "Damn, this was an intense day."
    if daliapath or calypsopath:
        mct "I had even more fun than what I expected when I first logged in."
        if daliacabin:
            mct "A lot more..."
        else:
            mct "Especially in the morning..."
    bla ". . ."
    mct "How many hours have we been playing on this server?"
    mct "I totally lost track of time."
    mct "I think the craziest thing is how unaware we are of what's happening in the real world."
    mct "World War III could have started and we wouldn't even know."
    bla ". . ." 
    show eee 13
    mc "*Turning around* (She's taking her time.)"with dis12
    mc "Alex? Do you need me to help you with anything?"
    bla ". . ."
    mc "Alex...?"
    play soundlow ["<silence 0.6>", horse] volume 0.5
    show eee 14 with dis2
    bla "You step into the alley where Alex disappeared just to find nothing except for some players in the distance."with dis12
    mct "Where the hell did she go?"
    mct "Maybe there's another Exit Portal in the town?"
    mct "This is weird..."
    play sound lantern
    play music westerndark fadein 8
    show eee 15 with dis12
    aaa "And you must be the leader..." with dis
    show eee 16
    bla "You slowly turn around."with dis12
    mc "Who the fuck–"
    mct "Wait, this man..."
    ec "Well, here I am."
    ec "You've been looking for me all day long, haven't you, boy?"
    show eee 17
    ec "I'll admit that I'm flattered, but I usually prefer to stay in the shadows."with dis12
    mct "They have Alex..."
    ec "Don't you?"
    mc "Let her go."
    ec "*Laughs* Who, your girl?"
    ec "Don't worry, Billy won't touch her unless you force us to. Right, Billy?"
    show eee 19
    bi "Of course not." with dis 
    bi "We'd never harm a pretty girl like this for no reason. It'd be such a shame."
    bi "If you force us to act, though... we might have to kill her too."
    bi "Unless she wants to have a couple of drinks with us at the saloon."
    if alexkisswest:
        bi "I saw you two kissing each other by the mines this afternoon, and I've gotta say, she looks like a passionate woman."
    show eee 18
    x "Just try it and I'll rip your tongue out."
    show eee 19
    bi "*Laughs* You got yourself a feisty girl!"
    if alexpath:
        bi "Just how I like them..."
    else:
        show eee 18
        x "I'm not his girl."
        show eee 19
        bi "Uhh... she sounds pissed off!"
    show eee 17
    ec "Tell me, then..."with dis12
    ec "How did you find out I have a Gem of Doom?"
    mc "What...?"
    show eee 20
    ec "*Sighs* Oh, come on..." with dis12
    ec "Let's just skip this part, shall we?"
    ec "I {i}know {/i}you've been trying to locate me because of the Gem I own. Why would you, if not?"
    ec "You're not even regulars in Frontier Trails."
    ec "So tell me, who do you work with?"
    mc "Let the girl go. I won't ask again."
    show eee 17
    ec "*Laughs* You got some balls, my young friend." with dis12
    ec "You learned about my Gem... and came right after me. I respect that."
    ec "But I'm sorry, you need more than courage and brute force to gather the 10 Gems of Doom."
    ec "That's why solo players will never be able to complete the quest. Not even Thanatos."
    ec "You need intelligence. Charisma. Strategy. And loyal allies."
    mc "That sounds like something a weak person would say."
    show eee 20
    ec "*Chuckles* You remind me of myself when I was younger." with dis12
    ec "So eager to prove my worth, to make my mark on the world."
    show eee 17
    ec "I've got an idea for you." with dis12
    ec "A duel."
    ec "The most honorable of combat."
    mc "A duel...?"
    ec "You and me. Right here. Right now."
    ec "Accept it... and if you come find me after the 24-hour penalty, I might even consider allowing you to join our group."
    show eee 18
    x "Be careful, [mc]."with dis 
    x "People in Blackridge have been talking about his infamous reputation for eliminating countless opponents in duels."
    x "He's definitely hiding something."
    show eee 19
    bi "That's the neat part!"
    bi "There's no trick, no secret advantage involved."
    bi "The boss is simply unbeatable in a duel. He possesses the absolute fastest draw in all of Eternum!"
    play sound holster
    show eee 21
    bla "You slowly move your hand towards your revolver and assume a dueling stance."with dis17
    ec "Ah, so you've chosen to meet your end with honor!"
    if alexpath:
        ec "Just because of that, we won't touch your girl."
    else:
        ec "Just because of that, we won't touch the girl."
    mc "*Taking a deep, slow breath* No, you won't."
    ec "Can you do the honors, Billy?"
    bi "You shoot on my count, or when you see your opponent reaching for his gun!" 
    ec "It's nothing personal, kid."
    ec "You see, when you carry a name like mine, you occasionally need to deal with nuisances."
    ec "You just happened to be... the inconvenience of the week."
    bi "Get ready!"with hpunch 
    play sound risingshort2
    scene eee21
    pause .01
    bi "Three...{w=1.7}{nw}" with dis 
    bi "Two...{w=1.7}{nw}" with dis 
    bi "One...{w=1.7}{nw}" with dis 
    stop music
    play sound6 dodge
    play sound revolver
    play sound3 shotgun
    play sound2 impact3
    scene eee 22 with flashfaster
    pause
    play sound4 ["<silence 0.2>", fall3]
    play sound6 ["<silence 0.2>", fall]
    play sound5 ["<silence 0.2>", debris]
    $ renpy.music.set_volume(0.75, channel='music3')
    stop soundloop2 fadeout 9
    play music3 epic4 fadein 6
    scene eee 23 with dis08
    pause
    show eee 24
    bi "Eh...?" with dis12
    show eee 25
    bi "W-What...?"with dis08
    show eee 26
    bi "What the fuck happened? Where did they–"with dis08
    play sound whoosh6
    play sound2 debris
    play sound3 rocks
    scene eee26b
    bi "AAAARGH!!!" with hpunch 
    play sound7 glitch4
    scene westernglitch
    bi "*Wheezing* W-WHAT THE HELL?!"with hpunch 
    mc "As a fan of big speeches myself, I must admit that your boss delivered a pretty good one."
    mc "He was correct. Acquiring all the Gems of Doom definitely requires more than just strength."
    bi "*Wheezing* E-Eeehh?!"with hpunch 
    mc "You also need intelligence, strategic thinking, and a loyal team."
    mc "But... he got one thing wrong..."
    play soundlow leather2
    scene eee 28
    mc "I am much more than just the inconvenience of the week." with dis15
    show eee 29
    bi "*Wheezing* W-What the fuck are you?!"
    show eee 28
    mc "The Gem. Where is it?"
    show eee 29
    bi "*Wheezing* It's not here! He never carries it around!"
    show eee 28
    mc "Where is it hidden, then?"
    show eee 29
    bi "*Wheezing* It must be somewhere in one of our bases!"
    bi "*Wheezing* W-We have one in The New World and... in Ion, I think?!"
    show eee 28
    mc "Be more specific."
    show eee 29
    bi "*Wheezing* I-I don't know! I've never been to the one in Ion, and our base in The New World is a ship!"
    bi "*Wheezing* I-It's always moving around! I d-don't know, I swear!"
    mc ". . ."
    show eee 28
    mc "How many of you are out there?"
    show eee 29
    bi "*Wheezing* In total? M-Maybe like... 50 people? Perhaps a bit more."
    bi "*Wheezing* W-We're a small group."
    mct "Nothing like the WRE or Wagner's group, then."
    mct "Ironic as it sounds, that might complicate things."
    bi "*Wheezing* W-Who the hell are you?!"
    bi "*Wheezing* How can you use magic on a non-magical server?"
    mc ". . ."
    show eee 28
    mc "I am..."
    mc "[nickname]."
    show eee 29
    bi "*Wheezing* Uhh??"
    show eee 30
    mc "Go and find your group, and tell them that... [nickname] killed your boss."with dis14
    mc "And when Coyote gets access to Eternum again after his 24-hour nap... tell him that I'm coming for him and his Gem."
    bi "I-I will!"
    bi "I will tell them!"
    mc "Good."
    stop music3 fadeout 7
    play soundloop2 night fadein 7
    play sound fall3
    play sound3 debris
    play sound2 run
    show eee 31
    bla "You let Billy go and he flees like a bat out of hell."with dis
    mct "The New World..."
    mct "Hmph. Looks like I'll have to get myself a pirate hat soon."
    play soundlow snow4 
    show eee 32 with dis17
    mc "Well..." with dis08
    mc "No one was hurt, and we now know they have 2 bases in other servers."
    mc "I'd call our mission today... a moderate success."
    if nickname == mc:
        x "Mm-hm."
        mc "Don't worry, you don't have to say anything."
        mc "I know you loved how epically I rescued you with my super speed."
    else:
        show eee 33
        x "[nickname]? What was that about?"
        show eee 32
        mc "Do you like it? I'm trying to get myself a name out there."
        mc "A nickname makes it more catchy, like “Thanatos”, or “El Coyote”."
        show eee 33
        x "Meh, I've heard better."
        show eee 32
        mc "Nickname or not... you've gotta admit that you loved how epically I rescued you with my super speed."
    show eee 33
    x "I had the situation under control."
    show eee 32
    mc "*Laughs* Excuse me? No, you didn't!"
    mc "Come on, just a thank you will do."
    show eee 33
    x "I didn't know you could control your powers so well, I'll give you that."
    x "You can even speak now!"
    x "Quite an improvement from the mindless berserk state you used to transform into."
    show eee 32
    mc "Not even a simple “thank you for saving me, [mc]!”?"
    mc "“That was so badass, [mc]!”"
    if alexpath:
        x "*Snorts* Hmph."
        show eee 34
        x "Thank you for rescuing me from those villainous villains with your super strength, [mc]!"with dis
        x "I feel incredibly protected by your side!"
        x "You're my hero, my knight in shining armor! THANK YOU!"
        show eee 35
        mc "*Laughs* Ah, now THAT'S better!"
        mc "And you're very welcome, m'lady. I'd risk my life every day for you."
        show eee 33
        x "*Chuckles* Alright, now that you've had your ego boost... can we finally leave?"with dis 
    else:
        show eee 33
        x "Nah... not feeling like it."
        show eee 32
        mc "You're evil..."
        show eee 33
        x "Can we leave now?"
    x "I'm honestly exhausted."
    show eee 32
    mc "Definitely, I'm so tired too."
    show eee 1
    mc "As much as I love Eternum, I need some time lying on a floppy couch."with dis14
    x "Next time we play, let's pick a server where we can just relax on a pool with some cocktails."
    mc "*Laughs* Count me in."
    stop soundloop2 fadeout 4
    play sound risingshort4
    scene login3 with dis2
    pause 6
    play soundlow whoosh4
    scene white with dissolve
    play soundloop rain3 fadein 5
    if not alexpath:
        jump alexnohouse2
    scene eee 36 with dis14
    play sound2 beep
    pause .1
    x "Oof..." with dis 
    mc "Arghhhh..." 
    show eee 37 
    mc "D-Do you feel that too?" with dis14
    show eee 38
    x "If you mean feel as if I had just been beaten the hell up... then yes, I do."
    show eee 37
    mc "Every single muscle and bone in my body aches."
    mc "Why?? We've been literally sitting on this couch the entire day."
    show eee 38
    x "I don't know... something to do with how our brains process our experiences, they say."
    show eee 37
    mc "Sometimes I wish Eternum wasn't so immersive..."
    show eee 38
    x "My feet are killing me."
    show eee 37
    if daliapath:
        mc "My thighs are sore from riding a horse for so long."
    else:
        mc "My legs are sore from walking all day."
    show eee 38
    x "I need to go to the bathroom {i}so{/i} badly."
    play sound stomach
    show eee 37
    mc "And I'm starving..."
    show eee 38
    x "God, I'm sooo hungry too..."
    show eee 37
    mc "Well, at least your cold seems a lot better!"
    x "Hmm...?"
    play sound sniff
    play sound2 ["<silence 0.4>", sniff]
    x "*Sniffs*"
    play sound3 clothes3
    show eee 39
    x "Hey, it's true!" with dis12
    x "My nose is finally clear!"
    x "And I feel a lot better in that regard!"
    show eee 40
    mc "I told you, Dr. Eggdogstein can work wonders on any cold."
    show eee 39
    x "*Laughs* Well, maybe it's also thanks to the drugs I took, don't you think?"
    show eee 40
    mc "*Chuckles* Hey, I brought those too, so I'll take credit for it as well."
    show eee 39
    x "Damn, thanks, [mc]. Those remedies really did wonders."
    x "I think that after taking a shower, I'll feel as good as new."
    show eee 40
    mc "I'm sure of it."
    mc "Just let me use the toilet for a second before leaving and I'll let y–"
    play sound thunder
    show eee 41 with dis04
    pause .4
    show eee 42 with dis22
    mc "Holy shit, it's still storming out there." with dis
    mc "It's raining even more than when I arrived."
    mc ". . ."
    mc "Um..."
    play sound6 chair2
    show eee 43
    x "*Standing up* Nooooope." with dis
    show eee 44
    mc "What? I didn't say anything yet!"
    show eee 43
    x "I know what you're gonna ask."
    show eee 44
    mc "It's not what you think."
    x "Hmm..."
    show eee 43
    x "Okay, humor me then."
    show eee 44
    menu:
        with dis
        "Can I stay over?":
            mc "Can I stay over?"with dissolve
            show eee 43
            x "That's EXACTLY what I thought you were going to ask!" 
        "You look so pretty tonight":
            mc "I just wanted to say how extraordinarily pretty you look tonight." with dissolve
            mc "Even though you’re under the weather, you still manage to–"
            show eee 43
            x "Cut the shit."
            x "Is that all?"
            show eee 44
            mc "Um..."
            mc "No, I also wanted to ask..."
            mc "Could I... perhaps..."
            mc "Stay over? Just today!"
            show eee 43
            x "I KNEW IT!"
        "I loved playing with you [alex_pts]":
            mc "I just wanted to say how cool it was to play with you today." with dissolve
            mc "I know we saw some fucked up shit today, but... it's awesome how you always manage to light up the room."
            mc "Thanks for playing with me."
            mc "I love spending time with you."
            $ alex_points += 1
            show screen heartbeat
            play sound beat
            show eee 45
            x "Oh... huh." with dis 
            x "You're welcome."
            x "I mean... it's nothing. I didn't do anything."
            x "It's me who's thankful for..."
            x "Your uhh..."
            x "*Grumbling* I'm not good at this shit."
            show eee 45b
            mc "*Chuckles* Don't worry, I understand."
            show eee 45
            x "I just wanted to say that... yeah, thank you for playing with me too."
            x "I like it."
            x "Being with you, I mean."
            x "Playing."
            show eee 45b
            x ". . ."
            show eee 45
            x "*Clears throat* Anyway, let's not get all sappy like a bunch of drama nerds."
            x "Was that all?"
            show eee 45b
            mc "Pretty much!"
            mc "Oh, and one last thing I wanted to ask..."
            mc "Could I... perhaps..."
            mc "*Clears throat* You know, since it's still raining so much..."
            mc "Stay over? Just today!"
            show eee 43
            x "AHA! I KNEW IT!" with dissolve
    x "And no, you can't."
    show eee 44
    mc "Come on, please! It's pouring down outside!"
    mc "And considering how late it is, there's a good chance there aren't any more buses running at this hour!" 
    x "*Grumbling* Mmmhh..."
    show eee 47
    x "*Sighs* Okay, FINE." with dis
    x "I don't want to have to explain to everyone how you mysteriously disappeared after I kicked you out and you got involved in some unfortunate incident."
    show eee 46
    mc "I-Is that something that happens often in this neighborhood or something...?"
    show eee 47
    x "You can stay."
    x "But just this once! This isn't a hotel!"
    show eee 46
    mc "Yay!"
    show eee 47
    x "So don’t go expecting five-star amenities!"
    show eee 46
    mc "No way!"
    show eee 47
    x "And you can't complain about anything!"
    show eee 46
    mc "Okay!"
    show eee 47
    x "Not a word about the kitchen! It’s a disaster in there."
    show eee 46
    mc "I couldn't care less!"
    mc "I'll whip up something to eat!"
    show eee 47
    x "All I have is a bag of chips. I was gonna go grocery shopping tomorrow."
    show eee 46
    mc "No problemo, chips and a couple of cold ones it is, then!"
    show eee 47
    x "I don't have beer. Just tap water."
    show eee 46
    mc "Did I say beer? I meant we're ordering pizza! My treat!"
    x ". . ."
    mc "Chinese food...?"
    show eee 49
    x "*Snorts* Hmph." with dis08
    show eee 48
    x "It's impossible to bring your mood down, eh?"
    show eee 49
    mc "That's my secret. Gotta always stay positive."
    show eee 48
    x "*Chuckles* Alright, alright... let's order pizza. But we're splitting the bill."
    show eee 49
    mc "Deal!"
    show eee 48
    x "I'll go take a quick shower."
    x "Order me a pepperoni one. Extra cheese."
    show eee 49
    mc "Ah, a woman of good taste, I see!"
    mc "Do you want some chicken wings too?"
    show eee 48
    x "Sure, why the hell not."
    x "I like honey BBQ and lemon pepper!"
    show eee 49
    mc "Right away!"
    stop soundloop fadeout 5
    scene black with dis22
    show screen sometimelater with dis17
    pause
    play soundloop2 rain5 fadein 5
    hide screen sometimelater 
    scene eee 50b
    with dis22
    bla "You both freshen up, devour two pizzas, and relax on Alex's cozy sofa." with dis14
    bla "You both sit lazily as you watch a live stream of the national swimming Olympic qualifiers on her laptop."
    play soundlow thunder fadein 4
    show eee 50 with dis17
    x "Huh! Hayes didn't qualify? You've got to be kidding me." with dis08
    x "I guess that's what happens when you're too overconfident."
    mct "Who would have imagined just a few months ago that I'd be having dinner with Alexandra Bardot... {i}in her own home!{/i}"
    mct "It already seemed improbable after our initial frosty encounter."
    mct "But after discovering she was Axel's sister and the daughter of Ulysses' biggest shareholder, it felt like an impossibility."
    show eee 51
    mct "And yet... here we are." with dis15
    mct "A girl who could have all the luxuries in the world... but instead chose to struggle to make it on her own in a scary apartment building, eating a $10 pizza for dinner."
    mct "She truly is something else."
    show eee 52 with dis03 
    pause .4
    show eee 51 with dis03
    pause .7
    show eee 52 with dis03
    pause .5
    show eee 53
    x "W-Why are you staring at me like that?"with dissolve
    x "Am I wearing a pepperoni on my face or something?"
    show eee 54
    mc "U-Um... no!"
    mc "I was just... a little lost in thought. About my things."
    show eee 53
    x "I know these qualifiers are boring as fuck to everyone who doesn't swim."
    x "I just wanted to see the finals, so we can turn it off now."
    show eee 54
    mc "Nah, it wasn’t boring at all. They were pretty entertaining."
    mc "Is that something you ever want to do? Go to the Olympics?"
    show eee 55
    x "Uh... I don't know, my coach keeps telling me that I could, but... I'm not sure."with dis06
    x "Maybe next year. We'll see."
    show eee 57
    mc "Well, if you ever go... you have your number one fan right here!"
    show eee 59
    x "Hmph."with dissolve
label ampsxmenu:
    if not ampsx1 and not ampsx2 and not ampsx3:
        jump alexsexscene
    menu:
        with dis12
        "[gr]About the girls..." if ampsx1:
            $ ampsx1 = False
            mc "Have any of the girls written back in the group chat?" with dis06
            mc "I'd check it myself, but my phone just died."
            play sound clothes4
            show eee 60
            x "*Taking her phone out* Um, let me see..." with dis14
            play soundloop celltype
            x "Yeah, apparently Dalia has info about El Coyote's hiding spots."
            x "Something about a man called... Boone, and some maps?"
            show eee 61
            if daliapath and daliacabin:
                mc "Yeah! That's the guy we found at the cabin in the middle of nowhere!"
            else:
                mc "No idea. But I guess he's the man she found at that cabin in Frontier Trails."
            mc "Good to hear we have a lead to follow."
            show eee 60
            x "And now we're discussing who'll go to The New World to try to find El Coyote's base."
            show eee 61
            mc "That's the pirate server, right?!"
            mc "I wanna go! Tell them to count on me!"
            show eee 60
            x "Okay, okay, I'm telling them."
            show eee 61
            mc "We have to find this Gem before Thanatos does..."
            mc "Now it's personal."
            show eee 60
            x "And... alright, that's pretty much it for now."
            stop soundloop fadeout 1
            show eee 62
            x "*Snorts* Hmph." with dissolve 
            play sound2 clothes4
            show eee 59
            bla "Alex puts her phone down as she chuckles." with dis14
            mc "What's so funny?"
            show eee 58
            x "Nothing, nothing."
            show eee 59
            mc "Come on, I wanna laugh too!"
            show eee 58
            if not daliarapewestern:
                x "It's nothing, Dalia just sent a meme."
            else:
                x "It's nothing, they just sent a meme."
            show eee 59
            mc "About what?"
            mc "It was about me, wasn't it?"
            show eee 58
            x "*Chuckles* Perhaps."
            show eee 59
            mc "Show it to me!"
            show eee 58
            x "Nah! You'll see it when you charge your phone."
            show eee 59
            mc "You're evil..."
            jump ampsxmenu
        "[gr]About those Praetorians..." if ampsx2:
            $ ampsx2 = False
            mc "Oh, I forgot to ask earlier... what happened with the Praetorians in Blackridge?" with dis06
            if daliacabin:
                mc "I didn't see them when I came back from the cabin."
            else:
                mc "I stopped seeing them at a certain point."
            show eee 56
            x "I think they all left the town a couple of hours before our incident with El Coyote."with dissolve
            if not westernalex:
                show eee 56
            else:
                x "Actually... I believe I know what they were doing in the server."
                show eee 57
                mc "Really?"
                show eee 56
                x "Do you remember the artifact that Linus showed us at the Ulysses dinner?"
                x "I stumbled upon a man carrying one of those, shortly after we parted ways."
                show eee 57
                mc "Damn, I do remember."
                show eee 56
                x "I started asking questions, but the guy panicked and ran away, leaving the box behind."
                show eee 57
                mc "Huh. Yes, that's definitely what the Praetorians were looking for."
                mc "Did you take it?"
                show eee 56
                x "Nah, I preferred not to mess with that shit."
                show eee 57
                mc "Smart decision."
                $ artifactexplanation = True
                show eee 56
            x "I assume they eventually found the artifact and left afterwards."
            show eee 57
            mc "Mmh, yeah, probably."
            mc "That damn artifact, though..."
            mc "It could definitely be useful."
            mc "I mean, imagine if we were able to recruit a Praetorian for our cause."
            mc "And not only to fight. Just think about the things she could tell us!"
            mc "About Idriel, or... the Founder."
            show eee 56
            x "Yeah, definitely."
            x "Although... unless you have $100K lying around and a good black-market contact... I'm not sure how we're getting our hands on one of those."
            show eee 57
            mc "Yeah, fair enough."
            mc "Although... you never know."
            mc "I'd say it's something to keep in mind..."
            jump ampsxmenu
        "[gr]About your brother..." if ampsx3:
            $ ampsx3 = False
            mc "Ah, did I tell you I ran into your brother earlier today?" with dis06
            show eee 53
            x "Axel? For real? What's he up to now?" with dissolve
            x "He hasn't been to school in a while."
            show eee 54
            mc "He looked pretty rough, not gonna lie."
            mc "And he sounded a bit... paranoid, honestly, but apparently he's been investigating your father."
            show eee 53
            x "Seriously?"
            x "Axel going against our beloved saint of a father? I find that hard to believe."
            show eee 54
            mc "At least that's what he told me."
            if axelhelp:
                mc "Oh, and he asked me about you too."
                show eee 53
                x "Axel? Really...?"
                show eee 54
                mc "Yeah, right before he left. He wanted to know how you've been doing."
                x "Hmph."
            mc "Have you seen either of them lately?"
            show eee 53
            x "Nah, even before moving here, I barely set foot in that house."
            x "Mom knew that I was leaving, and... Axel probably did too. But my father didn't even notice, I'm sure of it."
            x "I literally haven't seen him in weeks."
            show eee 54
            mc "Damn, I'm sorry, Alex."
            mc "I know it must not be easy."
            show eee 56
            x "Don't be sorry." with dissolve 
            x "Honestly? I couldn't be happier about it." 
            x "I finally have my own place, and I have everything I need in life right now."
            x "So... screw the Bardot family."
            show eee 57
            mc "That's right! You have us now."
            mc "And hey, if you're looking for a husband to finally get rid of that last name once and for all, I offer my services."
            mc "Alexandra [lastname] has a nice ring to it."
            show eee 58
            x "*Chuckles* Thanks for the offer." with dissolve
            x "I'll keep it in mind."
            show eee 59
            jump ampsxmenu
        "[red]Go to sleep":
            mc "Welp, I guess it's time to sleep." with dis06
            show eee 56
            x "Oh... already?" with dissolve
            show eee 57
            mc "Aren't you tired?"
            show eee 55
            x "I mean... yeah, I guess I should get some rest."
            x "Now that I remember, I have swim practice tomorrow at eight."
            show eee 58
            x "Which means that YOU have to get out of here before 7:30 AM too."with dissolve
            show eee 59
            mc "Awh, can't I hold down the fort here and stay in your cozy home?"
            show eee 58
            x "No chance."
            show eee 59
            mc "*Laughs* I imagined so."
            mc "Thanks again for letting me stay here, Alex." 
            mc "It really means a lot."
            mc "You're a good friend."
            show eee 57
            x ". . ." with dis
            show eee 55
            x "...yeah." with dis08
            show eee 56
            x "You're... a good friend too, [mc]."
            show eee 57
            mc "*Chuckles* Who would have imagined we'd become buddies, eh?"
            show eee 56
            x "...yeah."
            show eee 55
            x "Anyway, I'll let you sleep."
            x "Remember we..."
            x "Have to wake up at 7 tomorrow."
            x "There should be buses already running at that hour."
            show eee 57
            mc "Alright, sounds good!"
            mc "Sleep well, Alex."
            show eee 55
            x "Yeah... you too."
            x "Good night, [mc]."
            play sound clothes4
            play sound2 ["<silence 1.4>", doorclose]
            show eee 64 with dis17
            mc "*Yawns* Damn, this was a looong day..." with dis08
            $ alexpath = False
            $ alexu = False
            play sound3 chair1
            show eee 65
            mc "*Lying down on the couch* (I can't even keep my eyes open...)" with dis
            mct "Hmm, this apartment sure is warm. I don't even need a blanket."
            mct "That will come in handy now that winter is coming."
            mc "*Yawns* (Summer, though...)"
            mct "That'll be another..."
            mct "Matter..."
            stop soundloop2 fadeout 4
            scene black with dis22
            pause 
            play sound knock1
            bla "Someone knocks on the door." with dis08
            mc "Mmh..."
            play sound2 knock1
            bla ". . ."
            mc "Mmmmh?"
            play sound3 knock1
            play soundloop rain3 fadein 4
            scene edd 1
            mc "*Waking up* U-Uh...?" with dis22
            x "Yeah, yeah, I'm coming!"
            x "Jeez..."
            play sound squeak
            scene eee 119
            mc "*Still half-asleep* Who is it?" with dis12
            x "Must be that darn neighbor again..."
            mc "Really? What time is it...?"
            x "3:10 AM."
            x "Don't worry, I'll open. Just go back to sleep."
            play sound chair1
            scene edd 1
            mc "*Lying down on the couch again* Jesus Christ, what the fuck is wrong with this guy..."with dis12
            mc "*Yawns* Now I can't sleep anymore."
            mc "Even though I've only slept for about... 2 hours."
            mc "Dammit."
            mc ". . ."
            mc "He better have a damn good reason for bothering you at 3 in the fucking morning, I tell you."
            mc ". . ."
            jump cliffhanger06

label alexsexscene:
    mc "*Stretching out* Mmmhh... what time is it, by the way?" with dis06
    play sound clothes4
    show eee 60
    x "Um... it's about ten minutes to 1 AM."with dis12
    show eee 61
    mc "Damn, way later than I thought."
    show eee 60
    x "And... oof, according to the forecast, the rain will continue all night long."
    x "If only we could open the windows, it would be a lot cooler in here."
    x "But I don't wanna get everything wet."
    play sound2 clothes4
    show eee 57
    mc "Yeah, this apartment does feel quite warm, true." with dis12
    show eee 56
    x "It is. They told me it's because of the insulating material of the walls, or something like that."
    x "Which is great now that winter is coming, but in the summer... probably not so much."
    show eee 57
    mc "Don't worry, by the time next summer arrives, we'll have already collected the 10 Gems of Doom and be living in our Beverly Hills mansions."
    show eee 58
    x "*Chuckles* I'll take your word for it."with dissolve 
    x "Becoming my father's boss is something I'd really like to do in this life."
    show eee 59
    mc "*Chuckles* I can imagine."
    show eee 58
    x "But anyway, you aren’t quite in your Beverly Hills castle just yet, so you'll have to settle for crashing on a thrift store sofa."
    show eee 59
    mc "Won't complain. I could sleep on the floor if I had to."
    show eee 58
    x "Feel free to sleep in your underwear if it gets too stuffy in here."
    play sound buttons
    play sound2 clothes5 volume 0.7
    show eee 59
    mc "*Taking off your shirt* Oh, you don't have to tell me twice! Thanks."
    mc "You know... you can do the same. It's your home after all."
    mc "I wouldn't mind, really."
    show eee 58
    x "*Snorts* I bet you wouldn't."
    show eee 59
    mc "Purely for the sake of tolerating the heat, of course."
    mc "We can't open the windows, so..."
    play sound clothes4
    play soundlow chair1
    show eee 63
    x "Wait, now that you mention it..." with dis
    bla "Alex sits up with a sudden jump, and her shirt lifts above her waist."
    mct "Oh Lord..."
    x "I think there's a window in the kitchen we could open. It doesn't face the street and is under a little overhang, so it shouldn’t let much rain in."
    x "Hopefully that’ll help get some cool air in."
    mc "G-Good..."
    play soundlow chair2
    play sound clothes3
    show eee 64
    x "*Heading to the kitchen* Give me a second."with dis14
    mc "Sure..."
    play soundlow chair1
    show eee 65
    mc "*Lying down on the couch* (Oh man...)"with dis12
    play sound thunder fadein 3 volume 0.5
    mct "Every time I catch a glimpse of Alex's skin, all my exhaustion seems to vanish into thin air."
    mct "I wonder if she knows the effect she has on me."
    mct "I mean, she has to know."
    mct "Alex is anything but dumb, and I'm not exactly the most subtle person..."
    mc "*Sighs* (Too bad she probably–)"
    play sound clothes2
    scene black 
    bla "A shirt is tossed over your face as Alex comes back to the living room."with dis06
    x "Mission failed, I can't open the window."
    mc "Really?"
    play sound2 clothes3
    play sound3 clothes3
    scene eee 66
    mc "*Taking the shirt off your face* How..." with dis14
    stop soundloop2 fadeout 15
    $ renpy.music.set_volume(0.8, channel='music3')
    play music3 sexyalex2 fadein 7
    mc "...come?" with dis12
    x "The handle is stuck on something."
    x "Another thing to add to the never-ending list of repairs needed in this apartment..."
    play sound chair1
    show eee 67
    x "*Jumping on the couch* So I guess we'll have to go with plan B." with dis12
    x "You said... you don't mind, right?"
    show eee 68
    mc "Not..."
    mc "Not at all."
    show eee 67
    x "You okay?"
    show eee 68
    mc "Y-Yeah."
    show eee 67
    x "What's with that stammering? Did you really get shy all of a sudden?"
    x "After how much we've already seen of each other?"
    show eee 68
    mc "C-Certainly not!"
    mc "It's just that... I was expecting you to wear a bra under that shirt."
    show eee 67
    x "A bra? Why would I?"
    x "I'm in my own home. Wearing just an oversized T-shirt is the best thing in the world."
    x "And being able to take it off at night? Even better!"
    show eee 68
    mc "So you've been sleeping naked, huh?"
    mc "Aren't you afraid of some nosy neighbor catching a glimpse?"
    show eee 69
    x "Nah... the closest building is still too far away."
    x "And even then, the only apartment from where they could see us is where an old couple lives."
    show eee 68
    mc "I see..."
    show eee 69
    x "Anyway... goodnight, [mc]."
    x "I'm off to sleep on my “king-sized mattress”... you have fun out here."
    x "Sorry I don't have anything better to offer."
    show eee 68
    mc "It's okay... don't worry."
    show eee 67
    x "Before going to sleep, though, I just wanted to say..."
    show eee 69
    x "Look, I know I'm not the most expressive girl in the world."
    x "But... I still have emotions deep down. I’m not a cold-hearted tin-man like most would think!"
    show eee 67
    x "And today, you made me feel... um..."
    show eee 69
    x "I guess I just want you to know that... I really appreciate everything you did."
    x "Even if sometimes I make it seem like I couldn’t be bothered."
    show eee 67
    x "I mean... coming here to take care of me, and bringing me all the medicine."
    x "It... it really meant a lot."
    x "So thank you, [mc]."
    x "You've become... very special to me."
    show eee 68
    mc "You're... welcome..."
    show eee 70
    x "Did you even listen to a word I just said?" with dis
    x "Because it looked like you were staring at my tits the whole time."
    show eee 71
    mc "Uh..."
    mc "Something about... special medicine?"
    show eee 70
    x "So I open up my soul to you and you don't even pay attention?"
    show eee 71
    mc "Come on!"
    mc "You can't expect me to focus after showing up like that!"
    mc "I'm still in shock."
    show eee 70
    x "*Snorts* I see..."
    show eee 67
    x "Well, I'll let you be, then."with dis
    x "Rest well!"
    show eee 68
    mc "Aren’t you going to kiss me goodnight before you go?"
    show eee 70
    x "A goodnight kiss?"with dis
    show eee 71
    if alexkisswest:
        mc "The one we had in Blackridge really left me hungry for another."
    else:
        mc "I'm not sure I'll be able to fall asleep without one."
    show eee 67
    x "I'm sorry, I might have no symptoms at the moment thanks to your meds, but I'm still sick." with dis 
    x "I'd just pass on the cold to you."
    x "And with how whiney you could be, I wouldn’t want to hear about it."
    x "Plus, you’re our main offensive weapon in Eternum, and the one who's carrying the Gems. We need you at full capacity."
    show eee 68
    mc "Well... as long as I stay away from your airways, I should be good."
    show eee 70
    x "*Chuckles* Ah, yeah, a flawless plan." with dis
    x "You know my “airways” are required in a kiss, right?"
    show eee 71
    mc "Well then, we can always find... {i}other{/i} goodnight rituals that don't involve them..."
    mc "Something that keeps our mouths away from each other."
    show eee 70
    x "Oh, really?"
    x "Such as?"
    show eee 71
    menu:
        with dis
        "Caress her":
            mc "Well... I could kiss you... but maybe a little further south..." with dis06 
            show eee 70
            x "Ah, yes, “further south”."
            x "There’s so many places that are further down. Where did you have in mind, exactly...?"
            show eee 71
            mc "Hmm, let me think..."
            play sound squeak
            play sound3 clothes3
            show eee 83 with dis15
            bla "Feeling emboldened by Alex's playful demeanor, you stand up while pulling her closer and nestling her between the cushions." with dis
            mc "Well..."
            mc "I certainly have a couple spots in mind."
            show eee 84
            x "Do you now?"
            x "Now the suspense is killing me. I’m very curious where this mystery leads..."
            show eee 83
            mc "*Chuckles* You can probably imagine."
            show eee 84
            x "Who, me?"
            x "I'm just a sweet and innocent princess, I can't possibly imagine what you have in that dirty mind of yours."
            x "Maybe I need someone bad like you to enlighten me..."
            show eee 83
            mc "Well... I thought I could kiss your toes..."
            show eee 84
            x "Mm-hm... warm..."
            show eee 83
            mc "Then your thighs..."
            show eee 84
            x "Ah, getting warmer..."
            show eee 83
            mc "And then..."
            show eee 84
            x "Yes...?"
            play sound4 fall2
            play sound5 fall2
            play sound6 clothes3
            show eee 85 with dis12
            mc "*Kneeling between her legs* Better yet, why don’t I just demonstrate for you..." with dis
            x "Burning hot..."
            show eee 86 
            bla "You caress Alex's intimate parts through her underwear. She doesn't recoil or shy away, although you can hear her breaths quickening at the feel of your touch." with dis 
            show eee 87
            bla "You gently move the delicate fabric of her panties to the side, revealing the smooth contours of her perfectly shaved pussy." with dis
            mct "Oh sweet Lord..."
            play sound bodycollide
            show eee 88
            bla "Without waiting a second longer, you shove your head in between Alex's firm thighs and spread her velvety lips with your tongue." with dis
            show eee 89
            x "*Letting out a suppressed moan* MMMmmmh..." with dis12
            mc "Can I continue, then...?"
            x "Mm-hm..."
            scene alexsex0_1 with dis17
            bla "Upon noticing Alex's inviting response, you tightly grab her legs and start eating her out." with dis 
            x "O-Ooh.... FUCK, [mc]..."
            mct "God, I love her taste..."
            mct "Her scent..."
            mct "I love everything about her..."
            x "*Gasping* AAAaaahh..."
            mct "Now that I think about it, I have never heard Alex moaning before."
            mct "It sounds so unlike her, but incredibly hot at the same time..."
            x "AAAahhh s-shit..."
            x "*Moaning* F-Fuck, this feels so good..."
            mct "This is definitely a side of her that I’ve never seen before."
            x "P-Please keep doing what you're doing..."
            bla "Your eyes wander from Alex's pussy to her athletic body, taking joy in each one of her involuntary squirms and reactions."with dis
            x "Aaahh..."
            x "T-This is definitely..."
            x "T-The best “goodnight kiss” I've ever gotten..."
            x "AAaahhhh..."
            x "F-Fuck, [mc]..."
            mc "Mmmm..."
            pause
            play soundlow chair2
            play sound2 clothes3
            play sound3 ["<silence 0.1>", chair1]
            scene eee 90 
            bla "Alex abruptly pushes you to the side and stands up." with dis14
            mc "W-What happened?"
            mc "Was something wrong...?"
            play sound4 fall2
            show eee 94
            bla "She kneels down between your legs without saying a word." with dis12
            mc "Okay, I like where this is going..."
            play sound clothes3
            play sound7 clothes3
            show eee 95 with dis15
            mc "Oh fuck yes..." with dis
            bla "Alex stares mesmerized at your junk for a few seconds before pulling your pants down completely."
            play sound clothes3
            play sound7 clothes3
            show eee 96 with dis15
            pause
            show eee 96c
            x "I bet you feel better now."with dis12
            show eee 96b
            mc "Definitely..."
            show eee 96c
            x "I almost could feel your pants about to burst while you were going down on me."
            x "And looks like I wasn't wrong."
            show eee 92
            x "*Standing up again* You were ready for battle down there, huh?" with dis12
            show eee 93
            mc "I can't help it... that's the effect you have on me."
            show eee 92
            x "Now... before you continue what you were doing..."
            x "I thought I could give you a hand too."
            show eee 93
            mc "That sounds damn good to me..."
            show eee 92
            x "I mean, you're my guest after all."
            x "I wouldn't want you to feel uncomfortable, or to make you do all the work."
            x "What would people say of me, right?"
            show eee 93
            mc "I surely wouldn't want you to be known as a bad hostess..."
        "Ask her to caress you\n[mt](scene variation)":
            $ alexfootjob = True
            mc "Well... you could kiss me on... some other part." with dis06 
            play sound squeak
            play sound3 clothes3
            show eee 72
            x "*Getting comfortable between the cushions* Another part, huh...?" with dis12
            x "Such as...?"
            show eee 73
            mc "Surprise me."
            show eee 72
            x "No, no, it was your idea!"
            x "Did you have something in mind?"
            show eee 73
            mc "*Chuckles* You can probably guess."
            show eee 72
            x "Who, me?"
            x "I'm just a sweet and innocent princess, I couldn’t possibly imagine what you have in that dirty mind of yours."
            x "Please, enlighten me..."
            show eee 73
            mc "*Chuckles* Well..."
            mc "You could kiss me on my chest, for example."
            x "Mm-hm."
            mc "Then my stomach..."
            x "Hmmmph..."
            mc "Then you could take off my pants, and..."
            play sound2 bodycollide
            play sound bodycollide
            show eee 74
            x "*Gasps* Hold on there!" with dis08
            x "You nasty pervert!"
            show eee 75
            mc "It's you who asked me what was on my mind."
            show eee 74
            x "Yes, but I thought you were a gentleman, not a perv."
            x "I invite you to my own home, I let you stay under my roof, eat my chips, and this is how you behave yourself?"
            x "No kiss for you."
            x "Sick or not, you don't deserve my lips, [mc]..."
            show eee 75
            mc "Awh, really?"
            mc "And what about your hands?"
            show eee 74
            x "*Gasps* Gross! Definitely not that either."
            x "You should be grateful for just getting my foot."
            show eee 75
            mc "Well, depending on where I am getting it... I'd definitely accept that."
            mc "Although... I'd need to get a little more comfortable for that."
            show eee 74
            x "Oh, is that so?"
            show eee 72
            x "Don't let me stop you, then..."with dis
            x "Feel free to get more comfortable, if you want."
            show eee 73
            mc "Can I take my pants off?"
            show eee 72
            x "Of course, do what you wish."
            x "Make yourself at home."
            show eee 77
            mc "Ah, thank goodness. You have no idea how much I appreciate that." with dis14
            mc "The warmth was starting to become unbearable."
            play sound clothes5
            show eee 78 with dis17
            bla "You pull your pants down, exposing your already-fully-erect member." with dis
            x "*Mumbling* Jesus..."
            play sound2 clothes3
            scene eee 79
            x "*Touching your dick with her toes* What the hell is that, [mc]...?" with dis15
            show eee 80b
            mct "Oh, fuck yes..." with dis08
            mc "W-What do you mean?"
            show eee 79
            x "I mean the fact that a third of your blood is currently concentrated in your dong." with dis08
            x "You sure were ready for battle down there." 
            show eee 80b
            mc "I can't help it, it's the effect you have on me." with dis08
            show eee 79 
            x "Really? Just because of seeing my boobs?"with dis08
            show eee 80b
            mc "Your naked body, your constant teasing..."with dis08
            mc "It’s all of you, Alex."
            show eee 79
            x "Ah, I see..."with dis08
            play sound clothes3
            play soundlow squeak
            show eee 82
            bla "Alex spreads her legs and puts her feet around your hard cock."with dis15
            mc "*Clenching your fist* Oh yes..."
            show eee 81
            x "Perv..."
            scene alexsex0_2 with dis17
            mc "Oh, f-fuck..." with dis
            bla "Alex quickly sets a pace, gently jacking you off with her warm and surprisingly skilled feet."
            mc "Oh YES..."
            mc "God..."
            mc "You're good at this..."
            x "Thank you."
            mc "Aaahh..."
            mc "I-I've gotta say..."
            mc "This is definitely the best “goodnight kiss” I've ever gotten..."
            x "*Giggles* I bet."
            x "You're hard as fuck."
            mc "F-Fuck, how could I not..."
            bla "Your eyes wander from Alex's feet to her athletic body, captivated by the subtle transformation of her expression, which seems to grow more lustful with each passing moment."with dis
            mc "Aaaah..."
            x "*Giggles* Mmh."
            mc "You're enjoying this, aren't you?"
            x "*Giggles* Probably not as much as you..."
            mc "*Chuckles* P-Probably not..."
            pause
            play soundlow chair2
            play sound2 clothes3
            play sound3 clothes3
            scene eee 93 with dis17
            bla "Alex abruptly stops the footjob and stands up, positioning herself in front of you." with dis
            mc "W-What happened...?"
            show eee 92
            x "Before we continue..."
            x "Let me get rid of this for you..."
            play sound4 fall2
            play sound5 fall2
            show eee 95
            bla "She kneels down between your legs and stares mesmerized at your junk for a few seconds before pulling your pants down." with dis12
            play sound clothes3
            play sound7 clothes3
            show eee 96 with dis14
            pause
            show eee 96c
            x "You know... I might have been too harsh before..."with dis12
            x "So..."
            x "Okay."
            x "I'll let you... have my hands."
            x "I guess you've earned it after all you've done today."
            show eee 96b
            mc "Oh man..."
            show eee 96c
            x "So..."
            x "Can I... grab it...?"
            show eee 96b
            mc "O-Of course..."
    play sound2 clothes3
    play soundlow squeak fadein 1
    show eee 97 with dis14
    play sound3 bodycollide
    bla "Alex straddles you and firmly wraps her small hands around your dick." with dis12
    mc "O-O-Oh, fuck yes..."
    mc "*Caressing her thigh* I guess you do have some five-star amenities after all..."
    show eee 98
    x "*Giggles* Well..." with dis12
    x "As long as our... airways... stay away from each other..."
    x "We should be good... right?"
    x "I wouldn't want the girls to get mad at me because I got you sick."
    mc "Definitely..."
    scene alexsex0_3 with dis2
    bla "Alex starts to jack you off in a teasingly slow manner, as your cock gets unbelievably hard." with dis12
    mc "Oh Jesus, t-that feels good..."
    x "Mm-hm..."
    mc "Aaahh..."
    x "*Soft moan* Why do I feel like you’re even stiffer than that day in Eternum, [mc]..."
    x "This thing is pulsating so much, as if it were about to explode."
    mc "F-Fuck, Alex, you're driving me insane..."
    if alexfootjob:
        mc "Don't you wanna switch now? I need to edge off a bit..."
        mc "And... I could give you a hand too..."
    else:
        mc "Don't you wanna switch again? I need to edge off a bit..."
    x "Nah-ah. You aren’t going anywhere."
    x "*Giggles* Teasing you is even more enjoyable..."
    mc "Aaahh..."
    mc "F-Fuck... seeing it right in front of you like this..."
    mc "I can't stop imagining how it would feel to stuff my cock inside your petite body... do you see how deep inside you it’d go...?"
    x "*Scoffs* What do you mean, petite? I'm not petite."
    x "Any woman would look small next to your ginormous junk."
    mc "Nah... you are. It's just that your attitude gives you a strong presence, making you seem... larger."
    x "*Chuckles* Bullshit."
    mc "How tall are you?"
    x "5'4''."
    mc "So, same as Nova..."
    x "*Giggles* I'm taller than Nova."
    mc "You're my little petite princess..."
    x "*Giggles* Shut the fuck up."
    pause
    bla "As the teasing continues, the anticipation starts to intensify to unbearable levels, blurring the border between pleasure and pain." with dis 
    mc "*Panting* F-Fuck, Alex..."
    mc "I..."
    mc "I can't bear this anymore."
    x "*Soft voice* Do you want me to go faster...?"
    mc "I want to fuck you..."
    mc "I {i}need{/i} to..."
    mc "Aren't you horny too?"
    x ". . ."
    x "Would it go to your head if I said yes...?"
    mc "Then..."
    mc "If we both want it, why don’t..."
    x ". . ."
    pause
    play sound2 clothes3
    play sound squeak fadein 1
    show eee 99 with dis17
    bla "Alex stands up and grabs the side seams of her panties." with dis
    play sound3 clothes3
    play sound4 clothes3
    show eee 100
    bla "She pulls them down to her thighs and lets them drop to the floor." with dis17
    mct "No."
    mct "It's impossible."
    mct "I’m dreaming, right?"
    show eee 103
    bla "You slowly raise your gaze to Alex's face, afraid that uttering a single word could change the course of what you think is about to happen." with dis17
    x "*Breathing very quickly* . . . ."
    show eee 102
    x "Okay, I'm about to say something that I'll probably regret deeply tomorrow morning."
    x "Or... probably regret before the night is over."
    show eee 103
    mc "Oh god."
    show eee 102
    x "Q-Quiet."
    x "D-Don't utter a single word or you'll make me change my mind. Do you understand?"
    show eee 103
    bla "You nod intensely, feeling your heartbeat skyrocket to worrying levels."
    x "*Breathing very quickly* . . . ."
    show eee 102
    x "Yes, I'm horny as fuck."
    x "So..."
    show eee 103
    x "*Breathing very quickly* . . . ."
    show eee 102
    x "I'm going to let you put it in."
    show eee 103
    mct "OH GOD."
    show eee 102
    x "But JUST the tip."
    x "And only for... like... two minutes. Three minutes, tops. If you can last that long."
    x "Those are the two simple rules you have to follow, or else this thing is over."
    x "A-Are we clear?"
    show eee 103
    mc "Just the tip, and three minutes tops..."
    show eee 102
    x "Good."
    show eee 103
    x "*Breathing very quickly* . . . ."
    play sound2 clothes3
    play sound3 clothes3
    play sound squeak fadein 1
    show eee 104 with dis17
    bla "Alex gets on the couch and straddles you, getting into position." with dis12
    mc "Oh my fucking god, Alex..."
    x "*Biting her lip* Are you ready?"
    mc "No man can be ready for this..."
    play sound5 penetration2 fadein 1
    show eee 105
    bla "Alex lets out a loud moan as she mounts the tip of your cock and it slides slowly into her warm embrace." with dis17
    x "*Moaning* F-Fuck..."
    mc "OH MY GOD..."
    play sound6 penetration2 fadein 1
    show eee 106
    x "*Letting her body sink into you* F-FUUUCK..."with dis17
    $ renpy.music.set_volume(0.3, delay=10.0, channel='music3')
    $ renpy.music.set_volume(1.0, channel='soundloop')
    $ renpy.music.set_volume(1.0, channel='soundloop2')
    play soundloop alexsex1_2 fadein 3
    scene alexsex1_1 with dis22
    x "*Panting* Aargh.... aaaahh... aaaahhh..."with dis12
    x "Oh m-my g-gooood..."
    mc "Jesus Christ, Alex..."
    x "*Moaning* Yeah..."
    x "T-This is..."
    x "J-Just what I needed..."
    mc "Oh babe..."
    mct "It happened."
    mct "I'M FINALLY INSIDE OF ALEX."
    mct "I'M FUCKING HER."
    mct "And she's even tighter than I imagined, good lord..."
    x "F-Fuck, [mc], h-how can this just be the tip..."
    x "It's... too big..."
    mc "Does it hurt?"
    x "H-Hurt?"
    x "F-Fuck no... it feels AMAZING..."
    pause
    stop soundloop fadeout 2
    play soundloop2 alexsex1_2 fadein 3
    scene alexsex1_2 with dis22
    bla "Alex continues to ride you in ecstasy. You feel her tight pussy gradually accommodate your size more and more with each thrust, as if her young, athletic body was begging for more."with dis
    x "*Moaning* Mmmmm..."
    x "F-Fuck yes..."
    mc "Oh good lord..."
    x "*Giggles* MMmmmmMmm..."
    mc "Oh my, Alex..."
    x "You know..."
    x "W-We've already exceeded the three-minute mark, [mc]..."
    mc "P-Please, don't get off me..."
    mc "Let me stay inside you forever..."
    x "I..."
    x "AAAaahh..."
    x "I certainly don't want to stop..."
    x "*Moaning* Mmmmmhh..."
    x "I... {i}c-can't{/i} stop..."
    pause
    x "I wonder if... for that matter..."with dis
    x "Since we already broke one of the two rules... maybe we should break the other one as well..."
    mc "W-What?"
    x "*Panting* I-I think I can take it deeper."
    x "I want to see if I can take... ALL OF YOU... inside of me..."
    x "I wanna know how it feels..."
    mct "Oh Jesus..."
    bla "You grab on tight to the blanket under you and look at the ceiling, trying not to cum too fast and end this ethereal dream."
    x "*Whispering* So tell me..."
    x "*Whispering* Are you ready now..."
    x "*Whispering* For the ride of your life, cowboy...?"
    mc "Lord give me strength..."
    stop soundloop2 fadeout 1
    play sound penetration3
    show eee 106c with dis17
    x "AAAAAaAaaAaaaAAAAHH..." with dis
    mc "SHIIIIT..."
    x "*Giggles* W-Wow...."
    play soundloop alexsex1_3 fadein 2
    scene alexsex1_3 with dis22
    x "OH M-MY GOOOOODDDDD..." with dis
    x "*Squealing* AAAAAAHh..."
    mc "OH GOOD LORD..."
    x "Oh F-FUCK, [mc!u]!"with hpunch
    x "YES!" with hpunch
    x "{sc=2}Y-YES!{/sc}" with hpunch 
    bla "Alex rides your cock hungrily, taking all of your length, balls deep inside her hot pussy as if she had been possessed."
    x "*Panting* YES! YES..."
    x "Y-YES!" with hpunch
    mc "Oh Alex..."
    x "*Panting* OH MY F-F-FFUCKING GOD..."
    mc "I-It's so fucking tight..."
    mc "So warm..."
    mc "So wet..."
    x "*Panting* AAahh..."
    x "*Panting* I a-almost... c-can't breathe..."
    x "*Panting* But I can't stop either..."
    mct "Dear Lord, I can feel how my cock fills her completely, stretching her to her physical limit..." 
    mct "The head of my dick hitting her cervix with each thrust..."
    x "AAARGH FUCK, [mc]..." with hpunch 
    x "P-P-Please don't cum..."
    x "Not yet..."
    x "I d-don't want this to s-stop..."
    x "*Groaning* AAAAaaRgh..."
    x "Give me more of you..."
    pause
    stop soundloop fadeout 2
    play soundloop2 alexsex1_4 fadein 3
    scene alexsex1_4 with dis22
    bla "Just when you thought it was impossible, Alex still manages to increase her intensity and continues to ride you relentlessly." with dis 
    x "*Squealing* F-FFFUCK YES!"
    x "*Squealing* Fuck me, [mc]!"with hpunch
    x "HARDER!" with hpunch 
    x "DEEPER!" with hpunch 
    x "Fill me up just like that..."
    x "I want every inch of you inside of me..."
    bla "You finally take a moment to lift your head and focus on the woman who seems to be draining the very essence of your being."
    mc "*Panting* Holy fuck..."
    mc "Oh my god, Alex, I'm gonna c-cum so hard..."
    mc "I c-can feel it coming..."
    x "*Panting* I'm a-almost there..."
    x "AAAaaHHhhh..."
    x "*Panting* J-Just hang in there a bit more, please..."
    pause
    stop soundloop2 fadeout 2
    play soundloop alexsex1_5 fadein 3
    scene alexsex1_5 with dis22
    x "*Panting* Aaahhh... aaaAAaahh... AAAAHH!" with dis 
    x "{sc=2}OH MY GOD!{/sc}" with hpunch 
    x "{sc=2}[mc!u]!!!{/sc}" with hpunch 
    mc "OH ALEX..."
    mct "How the fuck this couch is still standing is something I'll never know..."
    x "AAAHH..."
    mct "J-Just the tip, she said..."
    x "AAAAAHHHH..."
    x "I... I'M–"
    mc "A-Alex, I'm gonna..."
    x "*Panting* F-Fuck, I'm cumming too!"
    mc "Y-You need to... get off me..."
    x "F-Fuck no..."
    mc "B-But–"
    x "*Panting* F-Finish inside me..."
    mc "W-What...?"
    x "*Panting* I want you... to cum... inside me!"
    x "*Squeals* AAAAAAAGH!" with hpunch 
    x "*Panting* G-Give me everything you got..."
    mc "B-But what if..."
    x "{sc=2}SHUT THE FUCK UP AND FILL ME UP!!!{/sc}" with hpunch
    mc "Oh babe..."
    pause
    play sound clothes4
    play sound3 chair1
    play sound4 squeak
    play sound5 cumall
    stop soundloop fadeout 1
    scene eee 107 with dis17
    $ renpy.music.set_volume(0.6, delay=20.0, channel='music3')
    play sound2 cumall
    mc "*Creampieing Alex* AAAAARGH!!!" with vpunch
    play sound6 cumall
    x "*Orgasming at the same time as you* AAAAAHHHH..." with vpunch 
    play sound7 cumall
    mc "AAAArrrghhh..."with vpunch 
    play sound3 cumall
    mc "*Still cumming inside Alex* AAaaaahhhh..." with vpunch 
    x "*Breathing heavily* Aaahh... aaaahh... aaahhh..."with dis14
    x "*Breathing heavily* Haha..."
    play sound penetration3
    scene eee 108
    x "I-I feel like you just unloaded a whole gallon inside of me..." with dis15
    mc "M-Maybe you’re not far off..."
    play sound2 penetration3
    play sound7 penetration3
    show eee 109 with dis2
    bla "Alex stands up with difficulty, while the hot load you just shot deep inside of her starts to ooze out."with dis12
    play sound3 chair1
    play sound2 squeak
    show eee 110
    x "*Rolling to the side* Unbelievable..." with dis12
    show eee 111
    mc "My god..."
    show eee 110
    x "That got... a b-bit out of hand... haha..."
    show eee 111
    mc "You're... too much..."
    show eee 110
    x "This can't happen again, you know that, right?"
    show eee 111
    mc "W-What?"
    mc "Are you serious?"
    show eee 110
    x "Absolutely."
    x "This will... never happen again."
    x "N-Never again..."
    show eee 111
    mc "Huh."
    show eee 110
    x "Do you... understand?"
    show eee 111
    mc "Yeah... it won't happen again."
    show eee 110
    x "It was... good... but it was a one time thing."
    show eee 111
    mc "O-Okay."
    show eee 110
    x "No more."
    show eee 111
    mc "Not in a million years."
    show eee 110
    x "Never again."
    show eee 111
    mc "Never..."
    show eee 110
    x "...again."
    scene eee 111
    x ". . ."
    mc ". . ."
    x ". . ."
    $ renpy.music.set_volume(0.4, delay=15.0, channel='music3')
    $ renpy.music.set_volume(1.0, channel='soundloop3')
    play sound w1
    play sound2 w1
    play soundloop3 shower2 fadein 1
    scene eee111b
    pause .13
    play soundloop alexsex2_4
    scene alexsex2_4
    pause .1
    x "MMmmmMMMmMHH!" with dis
    bla "Alex briefly breaks the kiss, allowing herself a moment to catch her breath and find the words she wants to share."
    x "*Whispering* F-Fuck, [mc]..."
    x "*Whispering* G-Go easy..."
    mc "You know I can't, Alex..."
    x "*Moaning* Mmmmmm..."
    x "T-That was supposed to be the last time..."
    mc "You were the one who followed me to the shower, remember...?"
    x "B-Because you were taking too long... and I'm the one paying the water bill."
    mc "Suuure, you didn't come with {i}any{/i} other intentions..."
    x "I'm not the one who got hard as soon as I stepped into the shower."
    mc "Ah... well, I'm guilty there."
    mc "I just love fucking you too much."
    x "*Giggles* Ah."
    x "*Whispering* Then do it..."
    x "*Whispering* Fuck me hard, [mc]..."
    stop soundloop
    play soundloop2 alexsex2_4
    scene alexsex2_3 with dis2
    bla "You shut her up by kissing her again, while continuing to pound her pussy nonstop." with dis
    x "*Moaning* MMmmmmMmmhh..."
    mct "Oh my fucking god, this feels like heaven..."
    mct "How easily she lets me slide all the way into the deepest depths of her... while still being outrageously tight..."
    mct "It's insane..."
    x "*Moaning* MMmMh!"
    mct "She has a body made to sin."
    mct "I mean, god, she's almost dripping more than the shower."
    mct "I wonder if I could ever make her squirt... make her banter that day at the park with Axel a reality..."
    x "*Moaning* Mmmmm.... MMmmmmMhh... MMMMmmhHHHHh!"
    pause
    stop soundloop2
    play soundloop alexsex2_4
    scene alexsex2_5 with dis2
    x "*Moaning* MMMmmmmMmmm..."with dis
    bla "You continue to penetrate Alex incessantly, pounding your body against the tattooed girl's slim figure."
    mct "Fuck, I love how synchronized we are..."
    mct "The way she pushes her hips against mine with each stroke..."
    mct "The fierce passion in her kisses, even despite the challenge of maintaining a constant connection due to the relentless hammering..."
    mct "And how she pulls me back closer to her with her leg..."
    mct "We’re as close as two humans could be, but it’s like she still hungers for more..."
    x "*Moaning loudly* MMMmMMH!"with hpunch
    mct "She wants me."
    x "*Moaning* MMmmmmmh!"with hpunch
    mct "And I want her..."
    x "*Moaning* MMMmmmmmMMmmhhhh..."with hpunch
    mct "I want to break her..."
    pause
    stop soundloop 
    play soundloop2 alexsex2_1 
    scene alexsex2_1 with dis2
    x "AAAAAAHH!" with dis 
    bla "You drastically increase your pace, with Alex responding in kind, adapting to the new rhythm almost instantly."
    x "Oh F-F-FUCK, [mc]!"
    x "AAAAaaaaaHHhhh..."
    mc "F-Fuck yes..."
    x "*Panting* W-We shouldn't have kissed... now y-you'll get sick..."
    mc "Fuck that..."
    mc "I'd get sick for a year if that meant I got to fuck you one more time..."
    x "AAAAaaahhh... yes... right there..."
    mc "O-Oh, Alex..."
    mc "I want to fuck you SO hard..."
    x "*Panting* Y-Yeah, do it then..."
    x "*Panting* Fuck me harder..."
    mc "I want to break you..."
    mc "I want to find out where your limits are..."
    x "*Panting* AAAahhh... YES..."
    x "*Whispering* B-Break me..."
    stop soundloop2 
    play soundloop alexsex2_1 
    scene alexsex2_2 with dis2
    x "*Moaning* Oh m-my GODDDD..."with dis
    x "AAAHHHH!"
    x "*Panting* Shit, [mc], I'm gonna cum again..."
    mc "M-Me too, Alex..."
    x "*Squealing* AAAAARGH!"
    bla "You continue to incessantly pound Alex's pussy as she groans loudly with pleasure. With the walls as thin as they are in these apartments, no doubt the neighbors could hear the two of you going at it continuously."
    x "AAAAAaaaAAAhhhhh..."
    x "*Panting* F-Fuck..."
    mc "Shit, I'm almost there..."
    x "*Panting* Y-You can finish inside again, but..."
    mc "Oh boy..."
    x "*Panting* This is the last time, you hear me?"
    mc "O-Okay..."
    x "*Panting* This was a mistake, we should’ve just stopped earlier..."
    mc "A-Agreed..."
    x "*Panting* So t-this is it! F-For real this time..."
    x "*Panting* Never again..."
    mc "Never..."
    x "*Panting* Again..."
    $ renpy.music.set_volume(0.5, delay=1.0, channel='music3')
    play sound w1
    play sound2 w1
    stop soundloop3
    play soundloop alexsex3_1 volume 0.9
    play soundloop3 rain3
    scene eee111c
    pause .13
    scene alexsex3_1
    pause .1
    x "AAAaaaahhh... MY GOD..." with dis
    x "{sc=2}[mc!u]!!!{/sc}" with hpunch 
    x "{sc=2}AAAAAAHHHHH!!!{/sc}" with hpunch 
    x "{sc=2}Y-YEAH!{/sc}" with hpunch 
    x "{sc=2}F-FUCK M-ME!!{/sc}" with hpunch 
    x "{sc=2}F-FUCK M-ME H-HARDER...{/sc}" with hpunch 
    mc "*Panting* Oh babe..."
    x "AAAahh..."
    x "*Panting* T-T-This i-is i-it..."
    x "*Panting* I-I'm a-at... m-my l-lim-mit..."
    x "*Panting* I-I c-can't..."
    bla "Alex's voice cracks every time you shove your cock into her, which makes her words almost unintelligible as the pleasure completely overtakes her."
    x "AAAA-A-ARh-HhhHA..." 
    mct "I'm almost at my limit as well..."
    mct "But fuck... dominating Alex like this is so damn hot..."
    x "*Moaning* AAAAa-AGAHH..." with hpunch 
    mc "Oooohhh, I'm almost there again..."
    x "AAAaaaahh..."
    mc "*Pulling Alex's head* You're gonna take it all like the good princess you are, aren't you, babe...?"
    x "Ggggghh..."
    x "*Panting* Y-Yeah...."
    x "*Panting* G-Give i-it a-a-all t-to m-me..."
    x "*Panting* I w-want it..."
    stop soundloop 
    play soundloop2 alexsex3_2 volume 0.9
    scene alexsex3_2 with dis2
    bla "You continue pumping Alex's pussy until you both reach the bounds of raw, carnal ecstasy."with dis
    x "Oh m-my god."
    x "I'm c-cumming."
    x "I'm c-coming a-again..."
    x "Aaaaaahh..."
    x "AAAAAAAAaaaAAaahhh...." with hpunch
    play sound cumall
    x "{sc=2}AAAAAAAAAAAAAaaaaaGGHHHHhhhh!!!{/sc}"with hpunch
    bla "You can feel Alex orgasming even more intensely than before."
    bla "Her whole body tenses up and her vaginal walls contract, giving you a wave of unimaginable pleasure."
    mc "Fuuuuuck..."
    x "*Panting* J-Jesusss C-Christ..."
    stop soundloop2
    play soundloop alexsex3_1 volume 0.9
    scene alexsex3_1 with dis2
    x "*Panting* [mc]... p-please..."with dis
    mc "*Panting* I-I know, babe, just hold on a bit more, I'm almost... there... too..."
    x "*Panting* AAaaaahhh... I c-can't..."
    mc "*Panting* I am almost..."
    stop soundloop fadeout 1
    play sound clothes3
    play sound2 clothes4
    play sound3 penetration3
    scene eee 112 with dis14
    pause
    play sound5 cumall
    play soundlow penetration3
    play sound4 slap1
    show eee 113
    mc "{sc=2}AAAAAAAAGHHH...{/sc}" with hpunch
    play sound6 cumall
    bla "As if compelled by a primal instinct, you unleash every ounce of jizz left in you deep inside Alex for the third time tonight." with hpunch
    play sound7 cumall
    mc "Fuuuuuckk...." with hpunch
    x "G-G-Gggghhh..."
    stop music3 fadeout 14
    play sound clothes3
    play sound2 fall2
    play sound3 penetration3
    play sound4 woodhit
    scene eee 114 with dis22
    bla "You slowly step away as you watch, almost with a sort of pride, a completely exhausted Alex collapsing onto the ground." with dis
    x "*Panting heavily* Oh my fucking bloody fuck shitty fucked damnit fucker..."
    x "*Panting heavily* FUUUUUCK... I can barely even speak..."
    mc "*Leaning on the wall and recovering your breath* T-That was... p-pretty intense, huh?"
    x "I c-can't... stand up."
    x "I can’t feel my legs."
    mc "You're an absolute wild beast, Alex."
    mc "Tonight was..."
    mc "I don't even know how to describe it with words."
    x "I have never felt anything that comes even close to this..."
    x "Just... holy fuck..."
    mc "Well... I hereby declare your apartment officially christened."
    x "*Cracked chuckle* Yeah... I'd say it's been christened alright."
    mc "*Trying to stand up* Jesus... I’m having trouble walking too."
    mc "I'm going to take a shower. A real one, this time."
    x "Yeah... you go ahead. I'll go after."
    x "Probably better if I just stay out here this time..."
    mc "You sure you're okay?"
    x "Yeah..."
    x "I just need a minute to compose myself."
    play sound thunder
    show eee 115 with dis03
    pause .4
    show eee 114 with dis22
    x "Or maybe... a couple of minutes..." with dis
    stop soundloop3 fadeout 4
    scene black with dis25
    show screen afewminuteslater with dis15
    pause
    play soundloop rain3 fadein 4
    scene edd 1
    hide screen afewminuteslater
    with dis25
    play sound2 chair1
    play sound6 squeak
    bla "Both you and Alex take a shower to gather yourselves. Thirsty from the marathon of exertion, you down an entire liter of water before finally collapsing onto the couch, utterly exhausted." with dis12
    mct "Oh, boy..."
    mct "What a trip..."
    mct "What on Earth just happened?"
    mct "It felt like Alex and I were participating in an unspoken competition to see who could break the other first."
    mct "One of those rare occasions where the loser is just as happy as the winner..."
    play sound2 chair1
    play sound3 squeak
    bla "Alex plops herself onto the couch next to you."with dis 
    show eee 116 with dis12
    mc "Well, well, well..." with dis08
    mc "Feeling better after taking that shower?"
    show eee 117
    x "Definitely."
    x "I'm starting to feel like myself again."
    show eee 116
    mc "How many showers have you taken today?"
    show eee 117
    x "*Snorts* Too many."
    x "Although... in some of them I came out dirtier than when I went in."
    show eee 116
    mc "Oh my, that doesn't sound like the Alex I know."
    mc "I wonder what got into you..."
    show eee 117
    x "This guy who invited himself over to my home."
    x "He got me drunk and took advantage of me."
    show eee 116
    mc "*Laughs* How does that work, because we only drank tap water."
    show eee 117
    x "Then I guess you put something in my pizza."
    show eee 116
    mc "*Chuckles* It's you who retrieved the order from the delivery guy."
    show eee 117
    x "Then... you probably resorted to some other trickery."
    show eee 116
    mc "Are you saying that you regret what happened tonight?"
    x ". . ."
    $ alex_points += 1
    play sound beat
    show screen heartbeat
    show eee 117
    x "I don't." with dis08
    x "Not one bit."
    x "Even if my swimming training tomorrow will be absolutely terrible because of you."
    x "You'll have to tell my coach that if I can't properly move my legs, you're the only one at fault."
    show eee 116
    mc "*Chuckles* Seems fair."
    x "*Giggles* Mmh."
    if alexpen:
        mc "I bet now you appreciate how I approached you in school to compliment your pen."
    else:
        mc "I bet now you appreciate how I approached you in school to compliment you."
    show eee 117
    x "*Laughs* The first day we met?"
    x "I remember. I thought you were an idiot."
    show eee 116
    mc "{i}But..."
    show eee 117
    x "*Laughs* What “but”? There's no “but”, that was lame."
    x "If anything, you should thank Mr. Keating for assigning us to work together on that school project."
    x "It was that day I realized... yeah... you were still an idiot, {i}but{/i}... maybe not as much as I had initially thought."
    show eee 116
    mc "I love seeing this affectionate side of you."
    show eee 117
    x "You know I just called you an idiot, right?"
    show eee 116
    mc "Yeah, because insults are an integral part of you, but... your eyes betray you. They reveal a different story."
    mc "You can't hide your true feelings from me."
    show eee 117
    x "*Chuckles* Bullshit..."
    play sound knock1
    show eee 118
    bla "Someone knocks on the door." with dis12
    mc "Oh shit, could that be a neighbor coming to complain?"
    mc "We might have been too loud before..."
    show eee 117
    x "Nope, it's pizza." with dis08
    show eee 116
    mc "Pizza?"
    x "Mm-hm."
    mc "You ordered again? When?"
    show eee 117
    x "While you were in the shower."
    x "I just happened to burn a shit ton of calories, thanks to {i}somebody{/i}, so I was hungry as fuck and took advantage of the 24-hour delivery service from Mario's Pizza."
    show eee 116
    mc "Oh my god, I love you so much."
    play sound knock1
    show eee 118 with dis
    play sound2 squeak
    play soundlow chair2
    show eee 119
    x "*Standing up* Yeah, yeah, I'm coming!" with dis14
    x "So yeah, after all, this is not happening ever again, so I thought... why not, we deserve it."
    mc "*Chuckles* This is not the first time I've heard those words tonight."
    x "Oh, but now I really mean it."
    x "This is not happening again."
    show eee 120
    x "...at least for today." with dis12
    play sound doorsqueak
    play sound4 footsteps
    show eee 121 with dis17
    mct "Oh boy..." with dis
    mct "This woman is too much..."
    jump cliffhanger06



label housenoalex06:
    stop soundloop fadeout 4
    scene black with dis22
    show screen sometimelater with dis15
    pause
    play soundloop2 rain3 fadein 3
    scene ep 21 
    hide screen sometimelater
    with dis22
    play sound chair1
    mc "*Lying on the bed* (Alright!)"with dis
    mct "Eating something... check. Going to the bathroom... check. Visor... check. E-suit... check!"
    mct "Everything's ready for a long-run session!"
    mct "Dalia's already connected, and if I'm not mistaken, Alex should have sent me an invite by now."
    mct "Unless her cold got worse..."
    play sound2 beep
    play sound ai7
    blank "{i}Connected." with dis
    play sound ai8
    blank "{i}Welcome back to Eternum." with dis
    play sound ai9
    blank "{i}You've received an invitation from..." with dis
    play sound aialex
    blank "{i}Alex." with dis
    mct "Nice! Looks like it all went well."
    play sound ai10
    blank "{i}Would you like to join her session?" with dis
    mc "Yes!"
    play sound ai11
    blank "{i}Please prepare to connect..." with dis
    $ alexpath = False
    $ alexu = False
    scene ep21
    jump westernloginnoalex




label cliffhanger06:
    if alexpath:
        play sound5 chair1
        play sound7 squeak
        scene edd 1
        mc "*Lying down on the couch* (Holy fuck...)" with dis12
        mct "This is real."
        mct "This happened."
        mct "I FUCKED ALEX."
        mct "And not only once..."
        play soundlow thunder fadein 2
        mct "Man, how long have we been fucking like animals?"
        mct "She drained me like a succubus..."
        play sound2 chair2
        scene edd 2
        mc "Oh, Alex, tell the delivery guy to give us some extra sodas too!"with dis12
        play sound6 wood volume 0.8 fadein 1
        scene edd 1
        mc "*Lying down again* I could use the sugar..." with dis12
        mct "And... mind-blowing sex apart... maybe it's just me, but I feel like she finally stripped away all the layers and revealed her vulnerable, true self."
        mct "There's something about her eyes... she looks at me very differently from the first time we met each other."
        mct "I'm seeing the real her."
        mct "I feel truly blessed."
    play sound doorsqueak
    play sound4 footsteps
    pause .5
    if alexpath:
        mc "You know, I've been looking at this ceiling A LOT tonight, but only now I am realizing how elegant it looks." with dis 
    else:
        mc "Hey, this ceiling looks pretty elegant, now that I’m really looking at it." with dis 
    mc "This apartment of yours hides some secrets here and there, I've gotta say."
    play sound chair2
    show edd 3 with dis17
    play music deception
    bla "You sit up and find two men where you were expecting to find Alex." with dis14
    mc "What..."
    play soundlow thunder fadein 3
    mc "*In shock* W-Wha..."
    mc "W-Who the fuck are you? Where's Alex?!"
    bo ". . ."
    mct "Oh shit, they're armed... are they trying to rob the place??"
    mc "W-What the fuck is going on?!"
    show edd 4 
    bo "*Scouting the place* . . ."with dis
    show edd 5
    bo "All clear, sir." with dissolve 
    play sound williamwalk
    play sound3 williamwalk
    show williamwalk with dis12
    pause 3.75
    play sound2 doorsqueak
    scene edd 6 with dis
    pause 1
    mct "No way..." with dis12
    will "Hmph."
    will "And just when I thought that you couldn't besmirch our name any further..."
    will "You still manage to drag it through the dirt once again, Alexandra."
    will "This place is nauseating."
    mc "You..."
    play sound2 footsteps 
    play sound3 footsteps 
    scene edd 7 with Dissolve(1.8)
    play sound chair1
    play sound6 squeak
    bla "William sits before you, his mere presence stifling the air and sending a shiver down your spine, as his icy gaze pierces through your soul." with dis
    mc "*Hyperventilating* . . ."
    mct "F-Fuck, why can't I speak? I'm completely at a loss for words."
    if alexpath:
        mct "Just a moment ago I was chilling with Alex on this couch and suddenly..."
        will ". . ."
    mct "There's something about this man that terrifies me..."
    will ". . ."
    mc "*Stammering* W-Where's Alex?"
    show edd 8
    will "Alexandra's right outside, with one of my men."
    will "She'll join us shortly."
    show edd 7
    mc "Why are you here...?"
    mc "W-What do you want?"
    show edd 8
    will "I just came to complete a procedure with my daughter."
    will "I'm just as surprised as you are that we’re seeing each other here."
    show edd 7
    mct "Okay... okay... you need to calm down, [mc]."
    mct "Don't let his henchmen intimidate you, they're just there to create fear."
    mct "He's just a business man. A fucking corporate sell-out who only cares about money and stock markets, that's all."
    mct "And he doesn't know who I am! All he knows is that I'm a friend of Alex, and that I was there the day he hit her."
    mct "He doesn't even know my name!"
    mc "*Pulling yourself together* Well, she doesn't want to see you, that's one thing I'm certain of."
    mc "So take your henchmen and get the fuck out of here, will you?"
    will ". . ."
    mc "I guess you're not used to seeing people stand up against you, but as I told you the last time... I'm not scared of you."
    mc "And neither is Alex."
    will ". . ."
    show edd 8
    will "The last time..."
    will "I suppose you're referring to the first time we saw each other, in Priscilla's penthouse."
    show edd 7
    mc "First {i}and last{/i} time we met, fortunately."
    show edd 9
    will "Hmm..." with dis12
    will "Are you sure about that?"
    mc "Huh?"
    will "I think you're mistaken."
    will "I believe the last time we saw each other was at the Ulysses dinner hosted on the Rockefeller server."
    will "Was it not?"
    play soundlow thunder fadein 3
    play musicb beat2 fadein 4
    play soundloop2 beat2 fadein 4
    mc ". . ."
    mc "What..." with dis15
    mc "What did you say...?"
    will ". . ."
    mc "How..."
    mc "How do you know..."
    show edd 8
    will "I was surprised to see you there too." with dis12
    will "Although... not as much as when you went to Wyatt's house with Nancy Carter, that's for sure."
    will "That was a bold move, I must admit."
    will "Too bad he's been pushing up daisies for five years, eh?"
    show edd 7
    mc "*Hyperventilating* W-What...?"
    show edd 8
    will "I guess that by now you must have already discovered that some of the NPCs used to be real players."
    will "It is... as morbid as it is fascinating, isn't it?"
    show edd 7
    mc "*Hyperventilating* . . ."
    show edd 8
    will "Although... I do wonder if you've also uncovered the true nature of Eternum and the secret that lies behind it."
    show edd 7
    bla "A silence floods the room, broken only by the sound of the rain against the window and your quickened breaths."
    show edd 9
    will "Hmm... I guess not." with dis14
    will "Perhaps I was overestimating you after all."
    will "I mean..."
    will "One would have expected that, after such a long time..."
    will "A man in possession of the Third Weapon of Atlas would have managed to gather more than two Gems of Doom..."
    stop soundloop fadeout 6
    stop soundloop3 fadeout 6
    play sound risingshort5b volume 0.8
    show edd 7 with Dissolve(2.4)
    show edd 8
    will "Don't you think...?{w=2.4}{nw}" with Dissolve(2.3)
    show edd 10
    will "[mc]?{w=2.8}{nw}" with Dissolve(2.6)
    play sound4 deception
    play sound2 deception
    play sound3 thunder
    stop soundloop
    stop soundloop2
    stop music2
    stop musicb
    jump update07

label alexnohouse2:
    scene ep 21 with dis14
    play sound2 beep
    pause 
    mc "Oooooff..." with dis 
    mct "Holy fuck, I feel as if I had just been beaten the hell up..."
    play soundlow thunder fadein 3
    mc "Mmmph..."
    mct "Every single muscle and bone in my body aches."
    mct "Why?? I've been literally lying on this bed the entire day."
    mct "Must be this never-ending rain messing with my joints..."
    d "Aghhhh, come on, Mom, I'll study tomorrow!"with hpunch
    n "I said no!"
    d "*Grumbling* AAaagh!"
    if daliarapewestern:
        mct "Oh, Dalia."
        mct "Maybe it's a good opportunity to see if she's still upset."
    else:
        mct "Oh, let's check with Dalia how that cabin thing went."
    scene ext 1 with dis17
    play sound dooropen1
    bla "Still feeling like a wreck, you stand up and open the door of your room."with dis
    mct "Oh boy... look at that..."
    d "If I pull an all-nighter studying, can I go tomorrow?"
    n "*From downstairs* I'll quiz you to make sure you do, young lady!"
    d "DEAL!"
    mc "H-Hey Dalia!"
    show ext 2
    d "Hmm?" with dis
    show ext 4
    if daliarapewestern:
        d "Oh, hey, the idiot woke up."with dis
        show ext 3
        mc "Uh..."
        mc "Okay, I see you're still mad."
        show ext 4
        d "Who, me? NO! I'm totally in love with you, can't you tell?"
        show ext 3
        mc "Um..."
        show ext 4
        d "You know what, since you're already here, why don't you go to Alex's house to give her my notes from last week?"
        d "I'm busy now, and since you're a nasty and disgusting piece of shit, I'm sure you don't have anything better to do."
        d "Am I wrong?"
        show ext 3
        mc "Erm..."
        show ext 7
        d "*Leaves* Sweet. Thank you..."with dis14
    else:
        d "Oh, hey [mc]!"with dis
        d "You finally logged off!"
        d "How'd it go?"
        show ext 3
        mc "We found El Coyote!"
        show ext 4
        d "No way! Seriously?!"
        d "Do you have the Gem?!"
        show ext 3
        mc "Nah... I took him down in a duel, but there was no Gem of Doom on him."
        show ext 5
        d "Agh, dammit."with dissolve
        d "Didn't even consider that possibility."
        show ext 4
        d "Good news, though - I know where all their hidden bases are!"with dissolve
        if daliacabin:
            d "Boone had all the info we needed."
        else:
            d "The man I found at the cabin had all the info we needed."
        show ext 3
        mc "Oh, sick!"
        mc "I was hoping you'd say that."
        show ext 4
        d "We're planning to sneak into all the bases at once, catch him off guard, and finally get the Gem."
        show ext 3
        mc "Excellent!"
        show ext 4
        d "Although... well, we can talk about it tomorrow."
        d "I've had enough Eternum for today, I don't wanna start bleeding like those addicts."
        show ext 3
        mc "*Chuckles* Agreed."
        mc "Wanna watch a movie or something?"
        show ext 5
        d "Nah, I can't."with dissolve
        d "We got that Chemistry midterm on Monday, gotta study."
        d "That's what I was discussing with Mom."
        show ext 3
        mc "Oh, right."with dissolve
        mc "How are you holding up?"
        show ext 4
        d "Pretty good!"
        d "Check it for yourself, ask me anything."
        show ext 3
        mc "Okay, um..."
        mc "How would you balance the chemical equation... Fe2O3 + CO -> Fe + CO2?"
        d ". . ."
        show ext 5
        d "Uhm..." with dissolve 
        d "O-Okay, I still need to take a last look."
        d "But I'll be ready tomorrow!"
        mc "*Chuckles* Sounds good."
        show ext 4
        d "It's such a bummer I can't go to Alex's as planned, though."with dissolve
        d "I was supposed to go to her place to have dinner and give her my notes from last week."
        show ext 3
        mc "Oh, really?"
        mc "Do you want me to take them to her for you?"
        mc "I don't mind."
        show ext 4
        d "For real? Would you do that?"
        show ext 3
        mc "Sure, I don't really have anything else to do now."
        show ext 4
        d "Well... if you do us this favor, we'd appreciate it, for sure."
        d "Thank you, [mc]!"
        if daliapath:
            d "You're the best."
        else:
            d "Sometimes you're not a total ass, go figure!"
        show ext 3
        mc "No problem!"
        mc "I'll be on my way, though."
        mc "I wanna be back in time to watch a movie after dinner."
        show ext 6
        d "I'll go take a shower and start studying, then!"with dis
        d "Be careful out there, it's raining cats and dogs."
        mc "I will! Catch you later!"
        d "Bye-bye..."
        show ext 7 with dis15
        play sound doorclose
    if not daliarapewestern:
        mct "Oh boy, that was hot."with dissolve
        mct "Would say yes to anything if she asked while wearing that sexy bra."
    else:
        mc "You're... welcome."
        mct "Y-Yeah, she's still upset."
        mct "Maybe she'll forgive me if I actually take these notes to Alex."
    mct "Anyways, I guess I should go."
    mct "Heh, I might get to see Alex's apartment after all."
    if alexkicksyouout:
        mct "Hopefully she'll let me in this time..."
    else:
        mct "Hopefully she'll let me in..."
    stop soundloop fadeout 4
    scene black with dis22
    show screen sometimelater with dis12
    pause
    play soundloop2 rain3 fadein 4
    hide screen sometimelater
    scene er 36
    with dis22
    pause
    play soundlow thunder fadein 3
    if alexkicksyouout:
        mct "Alright... here we are again." with dis
        mc "*Shivers* (This place always give me the creeps.)"
        mct "I feel like I'm about to get stabbed any second."
    else:
        mct "Alright... here we are." with dis
        mct "41 Oak Street, Apartment 25."
        play sound6 dog volume 0.6
        mc "*Shivers* (This place gives me the chills. Why the hell did Alex choose to live here??)"
    play sound2 ["<silence 1>", knock2]
    play sound3 ["<silence 1>", knock2]
    show er 38
    bla "You knock on the door."with dis12
    x "It's open!"
    play sound dooropenclose
    scene ext 8
    bla "You finally enter Alex's apartment. To your surprise, it's more spacious than you expected." with dis17
    mct "Hey, this doesn't look half bad!"
    x "Come into the living room, I was just cleaning up a bit of the mess!"
    play sound2 dooropen1
    show ext 9
    x "Sorry, I was finishing unpacking the last few boxes." with dis15
    mc "No worries!"
    mc "You shouldn't leave your front door open, though. Especially in this building."
    show ext 10
    x "Don't sweat it, I heard you in the elevator and–" with dis
    show ext 11
    x "Wait... what?"
    x "What are you doing here?"
    show ext 12
    mc "Surprise!"
    show ext 11
    x "Where's Dalia?"
    show ext 12
    mc "She had to stay because she has to study for Monday's test."
    mc "She asked me to come in her place to bring you her notes."
    mc "Didn't she tell you?"
    show ext 11
    x "Uhh... I don't know, I haven't checked my phone in a while."
    x "Um... well, thank you, I guess."
    show ext 12
    mc "It's no problem."
    mc "Are you feeling better?"
    show ext 11
    x "Huh?"
    show ext 12
    mc "From your cold."
    show ext 11
    x "Oh... yeah, much better. Popped an anti-flu right after logging off."
    show ext 12
    mc "Good!"
    x "Mm-hm."
    mc ". . ."
    mc "*Clears throat* So... are you gonna show me your new ho–"
    show ext 11
    x "Nope."
    show ext 12
    mc "Come on!"
    mc "I'm already here!"
    show ext 11
    x "And you're about to leave."
    x "The main bedroom is literally a mattress on the floor, the kitchen is a mess, and the living room is what you see."
    x "There's not much more to show."
    show ext 12
    mc "Everything looks great, don't worry so much about it."
    mc "I'm happy to finally have seen it!"
    x "Mm-hm."
    mc "Anyway... I guess I'll head back home by bus now."
    x "Mm-hm..."
    show ext 11
    x "Thank you for swinging by."
    show ext 12
    mc "Although... damn, it's still pouring outside."
    x ". . ."
    mc "Can I... perhaps... stick around for a bit? Only until it stops raining!"
    show ext 11
    x "*Sighs* I imagined you'd say something like that."
    show ext 12
    mc "Is that a yes?!"
    x "*Grumbling* Hmmph..."
    show ext 11
    x "You can stay... but as soon as the rain stops, you're out!"
    x "This is not a hotel."
    show ext 12
    mc "Yay!"
    show ext 11
    x "And... I have no TV, and was about to watch the national swimming Olympic qualifiers on my laptop."
    x "So that's what we're gonna watch."
    show ext 12
    mc "I LOVE watching swimming competitions."
    mc "Do you wanna order a pizza while we're at it? My treat!"
    x "Hmm..."
    show ext 9
    x "*Sighs* Alright, but let me lay a tablecloth down." with dis
    x "And don't you dare to stain the couch!"
    mc "We got ourselves a plan!"
    mc "Not a stain, I promise!"
    stop soundloop2 fadeout 3
    scene black with dis25
    pause .1
    show screen sometimelater with dis17
    pause
    play sound knock1
    hide screen sometimelater
    bla "Someone knocks on the door." with dis14
    mc "Mmh...?"
    play sound3 knock1
    play soundloop rain3 fadein 4
    scene edd 1
    mc "*Waking up* U-Uh...?" with dis22
    mc "Where... w-where am I?"
    x "Lying on my couch like a human burrito."
    x "You dozed off while watching the swimming qualifiers..."
    mc "Oh... s-shit, I'm sorry."
    play sound2 knock1
    bla "They knock again."
    x "Yeah, yeah, I'm coming!"
    x "Jeez..."
    play sound squeak
    scene eee 119
    mc "*Still half-asleep* Who is it?" with dis12
    x "Must be that darn neighbor again..."
    mc "Really? What time is it...?"
    x "3:10 AM."
    x "I'll open. Just go back to sleep."
    x "I won't kick you out of the house now, don't worry..."
    play sound chair1
    scene edd 1
    mc "*Lying down on the couch again* Jesus Christ, what the fuck is wrong with this guy..."with dis12
    mc "*Yawns* Now I can't sleep anymore."
    mct "Dammit, I shouldn't have fallen asleep. If things were already cold with Alex, this sure didn't help much."
    mc ". . ."
    mc "He better have a damn good reason for bothering you at 3 in the fucking morning, I tell you."
    mc ". . ."
    jump cliffhanger06



label update09:
    $ renpy.music.set_volume(1.0, channel='music')
    $ renpy.music.set_volume(1.0, channel='musicb')
    $ renpy.music.set_volume(0.7, channel='music2')
    $ renpy.music.set_volume(0.7, channel='music2b')
    $ renpy.music.set_volume(0.1, channel='music3')
    $ renpy.music.set_volume(0.6, channel='soundlow')
    $ renpy.music.set_volume(1.0, channel='soundloop')
    $ renpy.music.set_volume(1.0, channel='soundloop2')
    $ renpy.music.set_volume(1.0, channel='soundloop3')
    stop music
    play musicnoloop hyrilarcliff2
    scene mcexplainingarannis with flashfast
    pause 6.5
    scene q 12 with dis25
    pause .3
    scene q 13 with dis22
    pause .3
    scene q 14 with dis04
    pause 0.2
    scene q 15 with dis25
    pause .4
    scene q 16 with dis25
    pause .1
    scene q 17 with dis25
    pause .1
    scene q 18 with dis25
    pause .1
    scene q 19 with dis25
    pause .2
    scene q 20 
    pause 0.6
    scene q 21
    pause .49
    scene q 23 
    pause 0.49
    scene q 23b
    pause .49
    scene q 24
    pause 0.49
    scene q 25
    pause .49
    scene q 25b 
    pause 0.49
    scene q 26
    pause .49
    scene q 28 
    pause 0.49
    scene q 29
    pause .49
    scene q 29b 
    pause 0.49
    scene q 32 
    pause 0.49
    scene q 33
    pause .49
    scene q 34
    pause .49
    scene q 35
    pause .49
    scene q 36 
    pause .49
    scene q 37
    pause .49
    scene q 38
    pause .12
    scene q 39
    pause .12
    scene q 40
    pause .12
    scene q 41
    pause .12
    scene black
    $ calypso_points = calypso_interest
    if not daliapath or not penelopepath:
        jump hyrilar1
    play soundloop rain3 fadein 8
    pause 
    stop musicnoloop fadeout 5
    play soundlow thunder fadein 2
    scene q 42 with dis3
    d "Agghhh..." with dis15
    d "Oh, god... my arms are burning..."
    scene q 43 with dis15
    play sound chair1
    scene q43
    pause 0.01
    play music2 rainymorning fadein 6
    d "*Flopping onto the bed* (Not doing another curl... I'm so dead.)" with dis
    d "Mmmmmh..."
    d "(I've gotta bounce back quick and start getting ready to go jogging, though.)"
    d "(The forecast said the rain is supposed to stop any minute now...)"
    play soundlow thunder fadein 3 volume 0.6
    scene q 44
    p "*Shivers* U-Uuuughhh... w-why is it so freaking cold in here?!" with dis15
    p "Dalia?? Did you leave your window open?"
    d "Oh... yeah, my bad, sorry."
    play sound footsteps
    scene q 45
    p "What on earth is wrong with you?" with dis15
    p "Do you not realize it's raining? Winter's only a week away!"
    p "It's like 40 degrees outside!"
    show q 43
    d "I know, I know, sorry."
    d "I was just lifting some dumbbells and got warmed up."
    d "And... well, I didn't want to stink up the room."
    show q 45
    p "Here? You're not going to the gym today?"
    p "You do know today's a local holiday, right? No school for you guys."
    show q 43
    d "I know... and that's exactly why the gym's closed."
    d "I was gonna go for a jog, but it's been pouring all night, so I figured I’d hit my arms a bit while I waited for it to stop."
    d "Then this afternoon, I’ve got bodyweight exercises, and..."
    d "Maybe some abs too."
    show q 45b
    p "Oh my god, you're seriously obsessed, Dal."
    p "I like the gym too, but this is just straight-up addiction."
    show q 43
    d "Well, yeah, but I have to work out three times as much as you just to see some results."
    d "Not all of us were born with god-tier genetics, you know..."
    show q 45c
    p "You said you've only been training arms...?"
    p "’Cause if {i}that's{/i} how your butt looks without a pump, you’ve got no right to complain about bad genetics."
    p "I see progress, sis."
    play soundlow chair2
    show q 46
    d "*Sitting up* Hehe... really?" with dis14
    d "Thanks!"
    show q 46b
    p "Ohhh! New hair?"
    show q 46
    d "Oh... yeah. From yesterday."
    d "It's... a long story, though. I went straight to bed as soon as I got home last night, so I forgot to let it down."
    d "Not that it matters, I guess – I’m about to hop in the shower anyway."
    show q 46b
    p "Oh, I was gonna take a shower now too."
    p "I'm meeting Nova for lunch."
    show q 46
    d "Ah... cool."
    d "You can go first then, no worries. I'll wait."
    show q 46c
    p "Or we can just take a shower together, like the old days."
    p "I wouldn't mind. God knows we'd save money on water..."
    d "E-Eh?"
    show q 47
    d "W-What the fuck is wrong with you?"
    show q 46c
    p "Is that a yes?"
    show q 47
    d "No, thanks. Hard pass."
    show q 46c
    p "Oh, come on... we've seen each other naked like a hundred times. It's no big deal."
    show q 47
    d "B-But we're not kids anymore! It's weird now."
    show q 46c
    p "You suureee...?"
    p "I could help wash your back!"
    p "Like I used to! Come on, don't take this away from me now!"
    show q 47
    d "Stop acting like you raised me – you're literally not even three years older than me."
    play sound chair1 volume 0.6
    scene q 48b
    p "*Giggles* I love it when you pout." with dis12 
    show q 49
    d "Don't you have anything else better to do this morning?" 
    scene q48
    p "Is there anything better than spending time with my favorite sister?"
    scene q 49
    d "You're so annoying."
    scene q48
    p "Come on... say you love me, and I'll stop annoying you."
    p "I promise!"
    d "*Grumbles* Mmmmrrhh..."
    p "Come on..."
    d ". . ."
    p "{i}“I super duper love you, Penny! You're the bestest big sister ever! I love you lots and–”"
    scene q 49
    d "Fine, FINE!" with hpunch
    d "{i}*Mumbling* ...I love you. Dork.{/i}"
    play soundlow chair2
    play sound clothes3
    scene q 50
    p "*Giggles* Yay! Alright, I'm satisfied." with dis12
    scene q 51
    d "*Chuckles* You're so lame."
    d "Next time, I'll just log into Eternum to avoid you."
    scene q 50
    p "Eternum? Hah! You seem to forget I play it now too."
    p "I can follow you ANYWHERE you go. You can't escape your sister."
    p "Who you love sooooo much!"
    show q 51
    d "*Giggles* You're a real pain."
    show q 50
    p "But speaking of Eternum, how'd the mission in Valley of the Kings go?"
    p "Tell me, tell me!"
    show q 51
    d "Oh, it went well!"
    d "We found out Hassan was creating more Xenomorphs by sacrificing players and NPCs in these creepy labs he called “incubation rooms”. That’s why his numbers were so high."
    d "I’m gonna fill Mom in later so the WRE can go back and destroy everything that disgusting bastard has."
    show q 50
    p "Uhh... I see."
    show q 51
    d "But yeah, now that we know his secret, we should have no problem winning the event and getting that Gem of Doom."
    show q 50
    p "Nice, nice!"
    p "And aside from the whole Xenomorph thing... everything went well?"
    show q 52
    d "Aside from the Xenomorph thing?"
    d "I mean... yeah, everything was..."
    show q 53
    d "Everything was... {i}really good..." 
    show q 54
    p "Oh my... did you get to whip out a new move or something?"
    p "Or why did your voice change like that?"
    show q 52
    d "Like what?"
    show q 55
    p "{i}I mean... yeah... everything was..."
    show q55
    pbt "{i}Mmmm... reaaaaally good..."
    scene q 56
    d "I-I didn't say it like that."
    scene q 54
    p "Yes, you did."
    show q 57
    d "Ugh, w-whatever. Just leave me alone."
    show q 54
    p "You've been acting kinda weird lately, Dal. More than usual."
    p "Something you wanna tell your big sister?"
    show q 56
    d "Me? You're the one who's been acting weird!"
    show q 54
    p "Is it because of a guy...?"
    p "Are you in love?"
    show q 57
    d "Oh my god, you're even worse than Mom."
    d "Just get out of my room already."
    show q 54
    p "So is that a yes or a no?"
    show q 57
    d "It's a no!"
    d "I-I just..."
    d "Uh..."
    show q 58
    p "*Gasps* YOU ARE!" 
    show q 57
    d "I SAID I'M NOT!"
    show q 54
    p "Is it someone I know...?"
    p "A guy from class, maybe?"
    show q 57
    d "I’d literally jump out this window before telling you about my love life."
    show q 54
    p "Or... maybe it's a girl? No judgment here."
    show q 58
    p "*Gasps* IS IT ALEX?"
    show q 56
    d "No! Of course it isn't Alex!"
    show q 54
    p "So you DO have a crush, huh..."
    p "Did Jerry’s long-term plan actually work? Did he finally win your heart?"
    show q 56
    d "What?!"
    d "Are you out of your goddamn mind?!"
    show q 54
    p "Come on, just give me a hint! Have I seen him before?"
    p "OH! Is it..."
    p "*Giggles* Is it [mc]...?"
    show q 57
    d "I-I don't..."
    show q 59
    d ". . ." with dis
    show q 60
    p ". . ."with dis
    show q 59
    d ". . ."
    show q 60
    p ". . ."
    stop soundloop
    play sound musicstop
    play sound2 slam3
    play music2 ["<silence 1.8>"]
    queue music2 angrycats 
    scene q61
    p "Wait, wait, wait..." with hpunch 
    p "You're kidding, right?!" with hpunchsubtle
    p "YOU'RE IN LOVE WITH [mc!u]?!" with hpunch
    play sound3 chair1
    play sound4 whoosh6
    scene q62
    d "W-WILL YOU KEEP YOUR VOICE DOWN?!" with hpunch 
    d "Everyone else is still sleeping, you idiot!" with hpunchsubtle
    show q 61
    p "B-But... are you for real?!"
    p "How?!"
    p "I literally asked you a couple of weeks ago and you said “you’d rather live off salads for a year”!"
    show q 63
    d "Oh... well, yeah..."
    d "A-About that..."
    d "I was... confused."
    show q 61
    p "Confused??"
    show q 64
    d "Yes, confused."
    show q 61
    p "Oh my god, so you're really not messing with me."
    p "You {i}really{/i} are into him..."
    show q 64
    d "Speak for yourself!"
    show q 65
    p "What?! Hah! Me?! Pfft!"
    show q 64
    d "Why are you freaking out so much then?!"
    d "You've been hovering around him like a fly lately!"
    show q 66
    p "W-We've all been hovering around him lately."
    show q 64
    d "Yeah, sure..."
    d "But certain blondes have been a little more... hover-y, I think."
    show q 66
    p "I don't..."
    show q 67
    p "Wait, hold your horses, how did you turn this around on me?" with dis14
    p "Why are you acting like a jealous girlfriend all of a sudden?!"
    show q 64
    d "I'm not! I just..."
    show q 63
    d "*Sighs* You know what? Just forget it." with dis08
    show q 67
    p "No way, we're talking about this right now!"
    p "So? Are you... {i}in love{/i} with [mc] or not?!"
    p "L-Like..."
    p "Do you {i}love{/i} him, or are you {i}in love{/i} with him??"
    p "Be clear!"
    show q 63
    d "It's just... I don't know, we have... a good connection."
    d "He's into video games, nerdy stuff, and he's a total gym rat – just like me."
    d "We have... more in common."
    show q 67
    p "Excuse me?!"with hpunchsubtle
    p "The hell d'you mean, you have “more” in common?!"
    p "Is this some kind of competition now?"
    show q 63
    d "Of course not!"
    show q 67
    p "Good, 'cause I was about to say!"
    show q 63
    d "*Whispering* {i}Not that you'd stand a chance anyway..."
    show q 67
    p "What did you just say?!"with hpunch 
    show q 63
    d "Nothing."
    show q 67
    p "For your information, I'VE ALREADY WON, YOU KNOW?!"
    show q 64
    d "I'm pretty sure I've already won this one."
    show q 67
    p "My victory has already been sealed."
    show q 64
    d "MY victory was MORE than sealed just yester–"
    d ". . ."
    show q 67
    p ". . ."
    play sound slam2
    show q 68
    p "WAIT. HE AND YOU HAVE..."
    play sound2 slam2
    show q 69
    d "YOU HAVE..."
    show q 68
    p ". . ."
    show q 69
    d ". . ."
    d "Huh."
    play sound2 whoosh6 
    play sound slam3
    scene q 70 
    d "{sc=4}AAAAAAAARRRGHHHhhhhh!!!!{/sc}" with vpunchlong
    d "{sc=4}FUCK!!!!{/sc}" with hpunch 
    play sound4 impactwood
    play sound2 woodhit
    scene q71
    d "You just can't let me have anything, can you?!" with hpunch
    scene q 72
    p "What the fuck are you talking about?"
    p "Me and [mc] were a thing wayyyy before your little adventure in Valley of the Kings."
    scene q 71
    d "But I didn't fucking know??!"
    scene q 72
    p "Oh, but I was supposed to know about you two??"
    scene q 71
    d "You're so damn... selfish!"
    scene q 73
    p "Excuse me?"
    p "Say that again, I dare you."
    scene q 71
    d "You're so FUCKING selfish!"
    d "Do you wanna hear me say it a third time?!"
    scene q 73
    p "You can't seriously be that delusional. YOU'RE the one who only ever thinks about herself!"
    p "Try growing up for once, for god's sake!"
    scene q 71
    d "You're just so used to always having everything handed to you without any effort that you've completely lost touch with reality!"
    scene q 73
    p "What did you just say...?"
    scene q 71
    d "You really think we all get that celebrity treatment everywhere we go? That people are lining up to kiss our ass? That every single one of us is the most popular girl in school?!"
    d "Hell, you talked about playing Eternum ONCE and the entire college hopped onto it!"
    d "Do you think we–"
    play sound4 impactwood
    play sound2 woodhit
    scene q 74
    p "Do you think I've gotten everything for free?!" with hpunch
    p "Do you have any idea what it feels like to NEVER get any recognition?!" with hpunch 
    p "TELL ME!" with hpunch 
    p "Do you really think everything in my life has been easy?!" 
    p "Because I'm so fucking SICK of people assuming I’ve had it all served on a silver platter just because of my looks!" 
    p "YOU'RE MY SISTER!" with hpunch 
    p "Do you also think I earned my scholarship and my grades by sucking cocks at the teachers' lounge?!"
    p "Are you going to spread those rumors too?"
    p "Add your voice to all the whispers and gossip?!" 
    scene q 75
    d "...I didn't say that." with dis12
    play sound wood2 volume 0.2
    scene q 77
    p "Oh my god..." with dis17
    p "*Taking a deep breath* This seriously can't be happening..."
    scene q 76
    d "*Deep exhale* This is fucking unbelievable..."with dis15
    show q 77
    p "*Grumbling to herself* For Christ's sake..."
    p "*Grumbling to herself* I had a feeling something was going on between him and Nova. Or Annie. Or even Luna, for that matter!"
    p "*Grumbling to herself* I was ready to have that conversation. I fucking swear."
    p "*Grumbling to herself* I was... heh, {i}curious{/i}, even."
    p "*Grumbling to herself* But... this?!"
    p "*Grumbling to herself* My goddamn sister?!"
    show q 76
    d "*Grumbling to herself* How the hell am I supposed to deal with this?"
    d "*Grumbling to herself* Why didn't she tell me?!"
    d "*Grumbling to herself* Like... I get it, we're all living crazy fucking lives, I know we've all got a million things going on and enough shit to worry about."
    d "*Grumbling to herself* I get that realizing everything we thought was real could crumble is hard to digest... but still..."
    d "*Grumbling to herself* You know..."
    play sound4 impactwood
    play sound2 woodhit
    scene q 71
    d "I’D STILL HAVE APPRECIATED IT IF MY SISTER HAD TOLD ME SHE WAS SCREWING MY FUCKING BOYFRIEND!" with hpunch
    scene q 73
    p "Oh, so he's {i}your{/i} boyfriend now."
    p "You do realize you could've told me too, right?"
    p "Or is that not your fault either?!"
    scene q 78
    d "You know what?! Whatever. I don't care anymore." with dis15
    d "I'm done with this shit."
    show q 79
    p "Oh, no worries, I'm done too."
    show q 78
    d "I just need to have a chat with [mc]."
    d "We didn't even talk about... exclusivity or anything yet."
    d "You just had sex with him. No big deal."
    show q 79
    p "{i}Mine{/i} was special."
    show q 78
    d "{i}Our{/i} connection was mystical."
    show q 79
    p "{i}Ours{/i} was NEXT-LEVEL mystical. ACTUALLY, it was MYTHICAL."
    show q 78
    d "OUR CONNECTION WAS {b}COSMIC."
    show q 79
    p "That's because you didn't see {b}OUR{/b} GALACTIC CONNECTION."
    play sound4 impactwood
    play sound2 woodhit
    scene q 71
    d "{sc=3}We connected on levels you wouldn't even comprehend!{/sc}" with hpunch
    d "{sc=3}And we'll do it again!{/sc}" with hpunch
    show q 73
    p "Oh, we connected too... in more ways than one."
    p "And we'll do it again too, don't you worry."
    show q 71
    d "{sc=3}Over my DEAD body!{/sc}" with hpunch 
    show q 73
    p "Why don't we ask him?!"
    show q 71
    d "Ahhh!"
    d "Finally something that makes sense comes out of your mouth!"
    d "Let's ask him!"
    show q 73
    p "SURE!"
    p "Let's make him choose!"
    show q 71
    d "Fine by me!"with hpunch
    d "Let's settle this once and for all!"with hpunch
    play soundloop rain3 fadein 5
    scene q 80 with dis22
    d "[mc]!" with dis12
    p "Move it, you jerk!" 
    p "Do you think getting there faster will change anything or what?!"
    d "Shut the hell up and get your fat ass out of my way!"
    play sound slam
    play sound2 slam3
    show q 81
    p "Stop fucking pushing me!" with hpunch 
    show q 82
    d "You're the one who keeps shoving me!"
    show q 81
    p "Just shut up and pay attention, you brat!"
    p "You're about to learn a valuable lesson."
    show q 82
    d "Oh, you're about to get so humbled..."
    show q 83
    p "{sc=3}[mc!u]!!{/sc}" (multiple=2) with hpunchl
    d "{sc=3}[mc!u]!!!{/sc}" (multiple=2)
    stop music2
    scene q 84
    pause 
    play sound4 thunder fadein 2
    p "Eh?" (multiple=2) with dis15
    d "Huh...?" (multiple=2)
    d "Where is he?"
    p "I don't know."
    show q 82
    d "Really? You don't know...? I'm surprised!" with dis12
    d "Figured YOU wouldn’t know ANYTHING about what’s going on in [mc]’s personal life..."
    show q 81
    p "You just never know when to shut up, do you?!"
    play sound footsteps
    scene q 85
    n "*Yawns* Agh, what's with all this noise so early in the morning, girls? You're gonna wake up Annie." with dis2
    n "You know today's a holiday, right?"
    play soundlow wood2 volume 0.4
    show q 86
    d "Mom, where's [mc]?" with dis12
    p "Was he going somewhere today?"
    show q 87
    n "He's not in his room?"
    show q 86
    d "Nope."
    p "Did he even come home last night?"
    show q 87
    n "Um... I'm honestly not sure."
    n "But... maybe he didn't? I definitely would've heard him leaving this morning."
    show q 86
    p "Maybe he stayed at Alex's?"
    d "Or... maybe he had something to do in Eternum?"
    show q 87
    n "Yeah... yeah, possible."
    n "Although..."
    n "Hmph, it’s kinda strange he didn’t come home all night without at least messaging me or saying something in the group chat."
    n "He's usually considerate like that."
    show q 89
    p "Well, we already know how forgetful [mc] can be, don't we? He always tends to forget quite IMPORTANT information." with dis12
    show q 90
    d "Yeah... he's probably just off with Chang or one of the others, or... on some mission in Eternum."
    d "Luckily, I don't have any more sisters he can be with at the moment."
    p "Mm-hm."
    show q 89
    p "In any case, I'll find him, no need to stress."
    p "I'll call Nova and Luny. And if they don’t know where he is, someone from the WRE or Kredon definitely will."
    p "The good thing about being a brainless big-titted bimbo slut is that you end up knowing everyone in town, AM I RIGHT DALIA??"
    show q 90
    d "*Grumbling* I never said all that."
    d "BUT FINE! I'LL CALL ALEX!"
    d "And I'll ask Annie!"
    show q 88
    p "Oh, right! Maybe he's just in Annie's room! Let's check there first." with dis12
    d "Fuck no, that's my turf!"
    p "You just want to find him first so you can turn him against me!"
    d "Kiss my ass!"
    p "You little..."
    play sound run
    play sound2 ["<silence 0.2>", run]
    show q 91
    bla "Dalia and Penelope hurriedly rush past Nancy." with dis22
    n "Hmm?"
    play sound4 footsteps
    scene q 93 with dis2
    play sound3 sip
    n "*Drinking her coffee* (I should probably sort out whatever's happening between those two...)" with dis14
    n "(I wish I had half their energy at 8AM though, that's for sure.)"
    show q 94
    n "Hmm..." with dis
    show q 84
    pause
    scene q 95 with dis2
    n ". . ." with dis2
    stop soundloop fadeout 15
    play sound thunder fadein 2
    scene black with Dissolve(3.5)
label hyrilar1:
    pause .2
    show screen afewdayslater with dis3
    play soundloop2 cave fadein 7
    pause
    hide screen afewdayslater
    scene qq 1 
    with dis3
    pause 
    play sound2 rockpunch 
    bla "A steady, rhythmic thud of a fist striking the cold stone wall pierces the silence." with dis2
    play sound rockpunch 
    play sound5 fist
    show qq 1 with hpunch 
    pause
    scene qq 2
    mc ". . ." with dis15
    play sound3 whoosh6
    play sound rockpunch
    play sound4 fist
    scene qq 3 with hpunch 
    pause 
    scene qq 4 
    mct "Fuck..." with dis2
    mct "Why can't I activate my powers?!"
    mct "Not just teleportation, I can't even trigger my “berserk mode” anymore! I can't even... feel it."
    mct "What the hell is going on?!"
    mc "*Sighs* (I need to get out of here...)"
    mct "I've been stuck here for... three days now? Four?"
    mct "It's hard to keep track without seeing the sun..."
    play sound rat
    play music2 hyrilarmystery fadein 7 volume 0.8
    gua "Careful man, you've got a rat climbing up your leg." 
    show qq 5
    gua2 "By the moons, why are there so many of them lately?!"with dis12
    gua "They're probably crawling back to the dungeons now that the Princess is back. These things are too nasty for her."
    gua2 "Hah! Yeah, that makes sense. God bless her radiance."
    mct "These guards don't sound anything like Calypso."
    mct "I thought all elves would speak like her, but looks like it's just a class thing, like anywhere else."
    scene qq 6
    gua "Man... I still can't believe the Princess is really back." with dis14
    show qq 7
    gua2 "I know, right?"
    gua2 "It's been so many years. I thought we’d never see her again."
    show qq 6
    gua "Yup... same. Maybe now we can avoid war, with her back."
    show qq 7
    gua2 "Did you see her? I was in the barracks when the news came through."
    show qq 8
    gua "I caught a glimpse when the General was carrying her in, and good lord, she’s still as radiant as ever, for real."
    gua "I wish my wife had those giant milk bags."
    gua "Holy Lord... simply spectacular."
    show qq 9
    gua2 "You could be banished if someone else hears you using that language and reports it, you know?"
    show qq 10
    gua "Oh come on, if I can’t compliment our Princess’ creamy tits to my friend and a few rats, I might as well quit this job."
    show qq 9
    gua2 "If you say so..."
    gua2 "But even if you weren't just a mere guard, aren’t you, like, 600 years older than her?"
    gua2 "You’ve got a daughter three times her age."
    show qq 10
    gua "Age is just a number."
    show qq 9
    gua2 "Is it...?"
    show qq 10
    gua "Are you telling me you wouldn't–"
    play sound knock3
    show qq 11
    mc "Hey! You there!" with dis
    show qq 12
    mc "Did you mention the Princess? How is she?!" with dis
    gua2 "*Whispering* Heh, what if the human snitches you to the Council?"
    gua "*Whispering* Yeah, sure."
    gua "*Whispering* I'd like to see him try that with his head on a pike."
    mc "Hey! Can you hear me?!"
    play sound2 armorwalk
    scene qq 13 with dis2
    gua "What do you want now, human?" with dis12
    mc "You mentioned Calypso! How is she?!"
    gua "Calypso...?"
    mc "Yes...?"
    gua "First off, you have no right to speak her name like that. She's {i}the Princess{/i}, not just some person you can casually mention. Especially {i}you."
    gua "And secondly... well, yeah, she's alive."
    mc "But still unconscious?"
    gua "Yes. She's recovering from whatever you did to her."
    gua "But don't worry, you'll pay for it."
    mc "I didn't do anything!"
    gua "Hah. Sure. Tell that to the Council."
    gua "Now, silence."
    play sound2 armorwalk
    scene qq 14 with dis17
    gua2 "What did he want?" with dis12
    gua "Just begging for mercy."
    gua2 "The bastard really thought he could make a bargain with the Princess' life..."
    gua2 "It makes me sick."
    mc "*Sighs* Aah..."
    play sound ["<silence 0.5>", debris]
    play sound2 ["<silence 0.5>", fall2]
    scene qq 1 with dis15
    mc "*Sitting on the floor* (I’ve really outdone myself this time... How the hell am I gonna get out of this?)" with dis14
    gua2 "When was the last time a human ended up here?"
    gua2 "I've never seen one before."
    gua "Hmmm... must've been... two centuries ago?"
    gua2 "Wow, I wasn't even born yet."
    gua "I remember that day well. He claimed to be a merchant."
    gua "The tiny bastard offered–"
    play sound move
    play soundlow sword3
    gua2 "M-My Lord!"
    gua "It's an honor to see you here, Lord Sylax!"
    mc "Huh...?"
    syl "Open the door."
    play sound2 keys
    gua "At once, sire."
    play sound dooropencreak
    scene qq 15 with dis25
    bla "As one of the guards swings the door open, a poised and elegant elf carrying a sack steps into your cell." with dis15
    scene qq 16
    mct "Fuck, I've gotten too used to the darkness in here." with dis12
    mct "Who's this? A friend...?"
    play sound4 doorsqueak
    scene qq 17 with dis12
    stop sound4 fadeout 1
    play sound5 doorecho
    pause
    scene qq 18
    syl "Hmm." with dis14
    play sound sniff
    syl "*Sniffs* Hmph."
    scene qq 20
    syl "The stench is even more nauseating than I anticipated." with dis
    scene qq 19
    mc "Stench...?"
    mc "Uhh... for your information, they let me bathe every day, and they even treated my wounds."
    mc "So... unless my nose is broken, I don’t think I reek any more than usual."
    show qq 20
    syl "I am talking about your natural human filth."
    syl "It's revolting."
    show qq 19
    mc "...Oh."
    mc "Well, in that case, I don't think there's much I can do about that."
    mc "Apologies, I guess?"
    show qq 20
    syl "I would not joke if I were you, human. You are not in a position to amuse."
    show qq 19
    mc "I'm not trying to joke."
    mc "I just..."
    mc "Listen, you need to let me out of this cell."
    syl "Mmh."
    show qq 20
    syl "I {i}need{/i} to. Is that right?"
    syl "Where did you come from...?"
    syl "Why were you with the Princess?"
    show qq 19
    mc "I..."
    mc "That's... a very long story."
    mc "But I didn't harm the Princess! Trust me!"
    mc "Calypso and I were together when–"
    show qq 20
    syl "How dare you speak her name with that filthy mouth of yours."
    show qq 19
    mc "Oh... s-sorry."
    mc "She's usually fine with me calling her that."
    show qq 20
    syl "Aggh."
    syl "The very thought of your hands defiling her sacred form makes my stomach turn."
    show qq 19
    mc "I'm not your enemy, I swear!"
    mc "Just give me a chance to prove it!"
    show qq 20
    syl "Ohh... you will have a chance. Consider yourself fortunate."
    syl "The day of your trial has arrived."
    show qq 19
    mc "The trial...?"
    show qq 20
    syl "The Council will determine the degree of your punishment."
    show qq 19
    mct "That doesn't sound too promising..."
    play sound move
    show qq 22
    syl "Here." with dis12
    syl "Eat, regain your strength, and don the robes provided in this sack."
    syl "When you are ready, the guards shall escort you to the trial location."
    show qq 21
    mc "Huh..."
    mc "Well, thank–"
    play sound sackfood
    scene qq 23 with dis2
    bla "The man opens the sack and dumps its contents onto the floor with scorn." with dis15
    mc ". . ."
    syl "Eat."
    syl "You must be well-nourished before the trial to ensure you can answer every question with clarity."
    scene qq 26
    mc ". . ."with dis15
    scene qq 27
    mc "I'm... not hungry, thank you." with dis12
    show qq 25
    syl "And I did not ask."
    syl "I said... kneel... and eat, human."
    show qq 24
    mct "What the hell is wrong with this fucking moron?"
    mct "Does he think I'm his fucking dog, or what?"
    show qq 26
    mc ". . ." with dis15
    menu:
        with dis
        "Kneel and grab some food":
            $ sylaxfood = True
            mct "Hmmm... playing the good boy and going along with his game is probably the smarter move for now." with dis
            mct "There's no point in letting pride get in the way."
            play soundlow rubbody
            scene qq 28 with dis17
            mc "*Grabbing an apple* ...Thank you." with dis
            mc "I will eat."
        "[gr]Refuse":
            mc ". . ." with dis
            show qq 27
            mc "I said... I'm not hungry." with dis12
            mc "But thank you."
        "Attack him and escape":
            $ sylaxattack = True
            mct "This asshole’s way too full of himself." with dis
            mct "I could use this moment to take him down and attempt to escape."
            mct "I might not have my powers, but I’m sure I’m stronger than him. He doesn’t even look like much."
            mc "Hmph."
            play soundlow rubbody
            scene qq 28 with dis17
            mc "*Pretending to kneel* Thank you." with dis
            mc "I will..."
            play sound clotheswhoosh
            play sound2 swordfast
            play sound3 debris3
            play sound4 jumpscare volume 0.4
            scene qq29  
            bla "In the blink of an eye, Sylax unsheathes a dagger and presses it to your neck with flawless precision, not giving you a chance to even move." with hpunchsubtle
            scene qq 30
            syl "Seriously? I saw that coming from a starspan away."
            syl "Do you think a mere human would be able to catch me off guard?"
            show qq 29
            mc ". . ."
            show qq 30
            syl "Stand back and avoid embarrassing yourself any further."
    show qq 31
    syl "*Chuckles* Hm-mm-mh." with dis17
    show qq 32
    if sylaxfood:
        syl "Humans are truly pathetic creatures, aren't they?"
        syl "No wonder you have almost disappeared from the continent, tucked away in the far corner of Priasmar."
        syl "Honestly... it is hard to believe you are not extinct already."
    elif sylaxattack:
        syl "I must admit, though, this feeble attempt will assurely prove useful in the trial, so I suppose I should thank you."
        syl "I will savor every moment as you are torn apart by the punishment for your crimes, I assure you."
    else:
        syl "This pride is exactly what caused your kind to vanish from the continent."
        syl "Arrogance is only justified when there is something worthy behind it."
        syl "It would serve you well to remember that."
        show qq 31
        mc "We’ll see who has the last laugh."
        syl "Mm-hm."
        show qq 32
        syl "I will savor every moment as you are torn apart by the punishment for your crimes."
    show qq 31
    mc "Hmph."
    show qq 33 
    syl "Now, change. Quickly." with dis14
    syl "The trial shall begin in one hour. Do not be late."
    play sound dooropencloseecho
    scene qq 5 with dis25
    bla "The elven royal leaves the dungeon in an arrogant haste." with dis22
    mct "What a lovely visit."
    mct "If this guy's part of that “trial”, I'm seriously screwed... but I don't have a choice. I've gotta go. And I've gotta be smart."
    mct "This is my only shot to show them I’m not the enemy."
    mct "Or... at least, get them to hold off until Calypso wakes up. She’ll set everything straight."
    play sound clothes6
    scene qq 34 with dis25
    bla "You quickly throw on the robes you find in the sack." with dis22
    mct "Hmm... not bad. Looks very... royal, I guess."
    mct "And super tight. Guess this is the elven style."
    play sound knock3
    scene qq 35
    gua "Hey! Are you done?"with dis
    gua "Lord Sylax asked us to bring you before the Council immediately!"
    play sound2 footsteps
    scene qq 13 with dis15
    mc "Yeah... I'm ready." with dis
    gua "Heh! Would you look at that!"
    gua "You actually look halfway decent now! A couple of pointy ears, and you could totally pass as one of the royals!"
    mc "Where are we headed?"
    gua "Just follow us."
    gua "And don’t even think about pulling anything stupid."
    mc "I won't."
    gua "Good."
    gua "This way..."
    stop soundloop2 fadeout 7
    stop music2 fadeout 9
    scene black with dis3
    show screen afewminuteslater with dis25
    pause
    play soundloop birds fadein 6
    play soundloop3 river fadein 7 volume 0.5
    scene qq 36 
    hide screen afewminuteslater
    with dis3
    bla "The guards shackle you and lead you to the same area by the lake where you were apprehended days ago." with dis22
    play soundlow inhale2
    mc "*Taking a deep breath* Oh man..."
    mct "It feels so good to finally feel the sun again."
    mct "I guess it's true — you never know what you're taking for granted until you lose it."
    play music2 hyrilartension fadein 8
    stop soundloop3 fadeout 11
    play sound armorwalk fadein 1
    scene qq 37 
    gua "Here." with dis25
    gua "Enter through this door and follow the Council's instructions."
    gua "If you try to run, you will be killed on the spot. Do you understand?"
    mc "I already said I won't, jeez..."
    play sound chainswalk
    scene qq 38 with dis22
    bla "You enter the building cautiously, scanning for any possible escape routes in case the conversation goes awry." with dis17
    mc "Hmmm..."
    show qq 39
    mct "There's General Arannis." with dis 
    mct "Hmm, I'm still not sure if he's on my side or not."
    mct "He seems to be loyal to Calypso, but... he’s definitely not a fan of humans."
    mct "Kinda feels like that's the vibe around here in general, to be honest."
    show qq 38
    mct "He didn’t even glance at me when I walked in." with dis 
    mct "But... I'm not sure what to make of that."
    mct "Is that bad?"
    show qq 40
    mct "Hmm..." with dis08
    scene qq 41
    bla "At the far end of the room, you notice a group of well-dressed elves engaged in a heated discussion." with dis12
    mct "And... I guess that must be the “Council” the guards mentioned."
    show qq 42
    mct "And... yep, the guy who brought me the clothes is part of it too."with dis 
    mct "Ugh... I'm so fucked."
    scene qq 43 
    ele "Why is she here, Thorund?" with dis15
    ele "To my knowledge, your daughter holds no seat on this Council." 
    ele "Such a delicate matter must not fall upon unworthy ears!"
    scene qq 44
    thod "My father, the High Chancellor, has commanded my presence. He wished for me to assist him in this most pressing affair."with dis08
    show qq 43
    ele "You have no rightful place among us." with dis08
    ele "Only we three speak with the voice of Hyril'ar!"
    show qq 44
    thod "My father’s years weigh heavily upon him. I am his chosen successor, his trusted heir, his rightmost hand."with dis08
    thod "As such, my presence here is not only deserved but necessary."
    show qq 43
    ele "Preposterous! If he cannot stand without aid, he should relinquish his position at once!"with dis08
    ele "We must–"
    play soundlow leathershort volume 0.4 fadein 1
    play sound clothes3
    scene qq 45
    tho ". . ." with dis15 
    play sound2 clothes3
    show qq 46
    tho "Enough." with dis14
    tho "I assure you, Elenwen, though my steps may falter with age, my mind remains as sharp as ever. My daughter is only here to assist this aging body."
    tho "And let that be the end of this petty squabble."
    tho "Now, please, take your seat – the human has arrived."
    play sound3 ["<silence 0.4>", chair4]
    play sound6 clothes3
    scene qq 48
    ele "*Sitting down* Hmph." with dis
    play sound2 chair2
    scene qq 47
    syl "*Sitting down* . . ." with dis
    show qq 40
    tho "You." with dis
    tho "Come forward, mortal." 
    show qq 40b
    mc "Uh... sure."
    play sound chainswalk
    scene qq 50
    bla "You slowly approach the table where the elves are seated, the clinking of your chains echoing with each step." with dis22
    mct "Alright, this is my shot to prove I'm not the bad guy here."
    if calypsopath and calypsotogether:
        mct "I've gotta ditch these chains, make sure Calypso is alright, and then figure out how to get back to Earth."
    else:
        mct "I've gotta ditch these chains and figure out how to get back to Earth."
    mct "It’s been days since Thanatos attacked us... the girls must be losing their minds by now."
    scene qq 50c
    mc "Okay, listen to me!" with hpunchsubtle
    mc "I didn't hurt the Princess! But I need to see her immediately!"
    scene qq 49
    mc "If I can just talk to her, I can–"
    stop music2 fadeout 1
    stop soundloop fadeout 1
    play sound clotheswhoosh
    play sound3 debris3 volume 0.5
    scene qq 49c
    bla "The old elf raises his hand with startling speed, as if commanding even the forest to fall silent." with hpunch
    play music hriddles volume 0.81 fadein 4
    play soundlow leathershort volume 0.4 fadein 1
    play sound2 clothes3
    scene qq 49b
    tho "*Disdainfully* Silence." with dis15
    show qq 49
    mc "W-What?"
    show qq 49b
    tho "It seems you are unaware of the gravity of your situation, so allow me to enlighten you before the trial begins." 
    tho "You are accused of violating our most sacred laws."
    tho "You trespassed upon our lands. You laid hands upon the Princess herself — a Princess who, when we found her in your presence, was on the very brink of death."
    show qq 49
    mc "I didn't do anything to her!"
    show qq 49b
    tho "No human has set foot in Hyril'ar for centuries. You being the primary suspect in Princess Calypso's disappearance could plunge the entire Realm into chaos."
    tho "Thus, this trial shall be conducted in absolute secrecy."
    tho "Only General Arannis, his most trusted guards, and the Council are aware of your existence."
    show qq 49
    mc "Aaaagh!"with hpunch
    mc "Just let me speak and I'll explain everything!"
    show qq 49b
    tho "The trial has now begun."
    tho "We will decide your fate within the next few minutes. Answer the questions you are asked, and speak for NO other reason."
    tho "Have I made myself clear?"
    show qq 49
    mct "Goddammit... it's like talking to a wall."
    mct "This isn't gonna be easy."
    mct "Should I play the passive card...? Or try to be confident?"
    mct "Tell the truth? Or lie...?"
    mct "F-Fuck..."
label trialreset:
    $ trialpoints = 0
    if trialdead:
        $ trialpoints += 2
    show qq 49b
    tho "Are you deaf, human...?"
    show qq 49
    mct "I better choose my words very carefully if I wanna make it out of this one..."
    mod "You can try failing the trial."
    play sound gear fadein 0.7
    call screen neo_choice(trial1) with dis12
label trial1a:
    $ trialpoints -= 1
    scene qq 50b
    mc "Yeah, whatever you say, old man..." with dis
    mc "Let's just get this over with so I can get the hell out of here."
    show qq 53
    ele "Mph."
    ele "The insolence of this human is completely intolerable."
    ele "We have been far too lenient with their kind. Their arrogance has grown unchecked once more."
    show qq 51b
    syl "This is ridiculous."
    syl "We should execute him at once — this is a waste of time."
    show qq 49b
    tho "He may be arrogant, but arrogance alone is not proof of his guilt."
    jump ptrial1
label trial1b:
    scene qq 50c
    mc "I understand, sir." with dis
    mc "My only wish is to have a chance to explain myself."
    show qq 51
    syl "Huh, look at how he grovels."
    syl "Truly pathetic."
    show qq 53
    ele "Not only is he weak, but his people have lost even the pride that once defined them."
    ele "A disgraceful sign of this age’s decline."
    show qq 49b
    tho "We are not here to pass judgment on his race."
    tho "Our task is to determine the nature of his crimes and the punishment they warrant."
    jump ptrial1
label trial1c:
    $ trialpoints -= 2
    scene qq 50b
    mc "You know what?" with dis
    mc "I'm starting to get sick of this place, honestly."
    mc "Fuck you and your whole inbred clan of pointy-eared pricks."
    play sound metalhit2
    play sound2 debris3
    play sound3 slam3
    scene qq51e1
    syl "{sc=2}What did you just say, human?!" with vpunch 
    syl "{sc=2}How dare you..." with hpunchsubtle
    syl "{sc=2}Why are we even wasting time with this?"with hpunchsubtle
    syl "{sc=2}We should execute him at once!" with hpunchsubtle
    show qq 52
    tho "Calm yourself, Sylax."
    play soundlow leathershort volume 0.5 fadein 1
    show qq 51d
    syl "What?!" with dis 
    syl "You will allow him to insult us like that?!"
    show qq 52
    tho "Your temper is misplaced."
    tho "Would you also take offense if a dog cast a defiant glance your way?"
    tho "Do not stoop to his level."
    show qq 51b
    syl "Bah..."
    syl "Let's just get this over with."
    show qq 49b
    tho "The human’s insolence is undeniable, but we must ask what we came to ask." with dis
    jump ptrial1
label ptrial1:
    tho "We shall hear his words, and only then shall we pass judgment."
    show qq 54
    thod "If you have any question of your own, speak now." with dis
    thod "You will not be given another chance."
    show qq 54b
    mc "Hmm..."
    play sound gear fadein 0.7
    call screen neo_choice(trial2) with dis12
label trial2a:
    scene qq 50d
    mc "I... I think I shouldn't say anything without a lawyer present." with dis
    mc "I ask for an attorney before proceeding further."
    show qq 53
    ele "A what?"
    show qq 51c
    syl "*Snorts* Who do you think you are?"
    syl "No one will come to your aid, human."
    syl "We are here only to uphold the fair laws of Hyril'ar — or you would already be dead."
    show qq 49b
    tho "Lord Sylax speaks the truth."
    tho "In elven justice, we must defend ourselves alone."
    tho "You, and you alone, must answer for your actions."
    show qq 49
    mct "Dammit, that didn't work..."
    jump ptrial2
label trial2b:
    scene qq 49
    mc "Look, I..." with dis
    mc "*Sighs* Fuck."
    mc "I... I wish to confess."
    show qq 49b
    tho "You wish to confess?"
    show qq 49
    mc "Yes, Lord Thorund."
    mc "I'm guilty."
    mc "Guilty. Is that what you want to hear?"
    show qq 49b
    tho "Do you admit to abducting the Princess and attempting to take her life?"
    show qq 49
    mc "No, of that I'm innocent."
    mc "I am guilty of a far more monstrous crime. I am guilty of being... a human."
    tho ". . ."
    show qq 49b
    tho "You are not on trial for being a human."
    show qq 49
    mc "Oh yes, I am."
    mc "And I know I'll get no justice here..."
    mc "So I will let the gods decide my fate."
    stop music 
    play sound impact5 volume 0.6
    scene qq 50e
    mc "I demand a trial by combat."
    play sound2 impact5 volume 0.6
    scene qq 53
    ele ". . ."
    play sound3 impact5 volume 0.6
    scene qq 39c
    ara ". . ."
    play sound4 impact5 volume 0.6
    scene qq 54
    thod ". . ."
    thod "A..."
    thod "A what?"
    play music hriddles
    scene qq 49b
    tho "That is not an option." with dis12
    show qq 49
    mct "Goddamnit..."
    show qq 51b
    syl "The human truly believes he can bring his barbaric ways into our lands."
    syl "Where do you think you are, mortal?"
    show qq 49b
    tho "In Hyril'ar, you may only attempt to defend yourself with your words, and nothing else."
    tho "Do not try it again."
    show qq 49
    mct "Dammit, that shit worked in Game of Thrones."
    mct "Fucking George R.R. Martin..."
    jump ptrial2
label trial2c:
    $ trialpoints += 1
    scene qq 49
    mc "Alright, first of all..." with dis
    mc "Who are all of you?"
    show qq 49b
    tho "My name is Lord Thorund."
    tho "I am the eldest among the nobles of the Realm, and I have held a seat on the Council for over four millennia."
    show qq 48
    tho "This is Lady Elenwen, daughter of Celeror of Farrah and the rightful heir of Eldunar, the most prosperous house on the entire continent."
    show qq 47
    tho "And this is Lord Sylax, heir to the ancient and honorable house of Cassyr, who has long served with pride as the King's Hand, fulfilling his duties across generations."
    show qq 49b
    tho "We, the three of us, constitute the Council of Regents, entrusted with the temporary governance of Hyril'ar until the rightful ruler returns — the sole descendant of Anima's bloodline, Princess Calypso."
    tho "Her highness vanished without a trace more than fifteen years ago, and since then, we have been awaiting her return with steadfast patience."
    show qq 49
    mct "Wait... fifteen years ago...?"
    mct "How is that possible? Ulysses didn't even exist back then."
    mct "Does that mean she wasn’t actually kidnapped by the Founder...? How the hell did she end up stuck in that box, then?"
    show qq 49b
    tho "And that is all you need to know."
    jump ptrial2
label ptrial2:
    show qq 49b
    tho "Now, you will answer our questions, as briefly and accurately as you are able."
    tho "Keep in mind that withholding the truth will immediately result in the penalty of death by sword, without any further defense or deliberation."
    tho "Do you understand?"
    show qq 49
    mc "*Gulps* Y-Yes."
    show qq 49b
    tho "What is your relationship with the Princess?"
    tho "Why was she with you?"
    play sound gear fadein 0.7
    show qq 49
    call screen neo_choice(trial3) with dis12
label trial3a:
    $ trialpoints -= 2
    mc "I am her owner."with dis
    mc "She's something we call... “Weapon of Atlas”. The third one, to be precise."
    mc "As such, she's bound to serve me and create portals to wherever I want."
    show qq 51b
    syl "This is outrageous."
    syl "This... {i}creature{/i} is determined to tarnish the entire royal lineage with his lies."
    show qq 53
    ele "The Princess serves no one in this world — certainly not a filthy human."
    show qq 48
    mc "You asked for the truth, and I'm giving you just that."
    jump ptrial3
label trial3b:
    $ trialpoints -= 1
    mc "We're friends."with dis
    tho "Hmm."
    show qq 49b
    tho "Friends..."
    tho "You. With the Princess of Hyril'ar."
    show qq 49
    mc "Think whatever you want."
    if calypsotogether:
        mc "She literally said it herself. She sees me as an equal."
    else:
        mc "That's the truth."
    show qq 51b
    syl "You? The Princess’ equal? You must think we are fools."
    jump ptrial3
label trial3c:
    mc "I am the Princess' servant."with dis  
    mc "I swore to protect her and serve her until she could find her way back home to Hyril'ar."  
    show qq 53
    ele "Ahh... I suppose that explains it."
    show qq 51b
    syl "No, it does not."
    syl "As if the Princess would ever accept a filthy human as her protector."
    syl "She bested the greatest warriors and mages in the Realm long ago — how could a mere mortal be of any use to her?"
    syl "He is lying..."
    jump ptrial3
label ptrial3:
    scene qq 49
    tho "Hmph."
    scene qq 50
    tho "And... when and how did your paths cross?" with dis 
    play sound gear fadein 0.7
    call screen neo_choice(trial4) with dis12
label trial4a:
    scene qq 50c
    mc "I found her by accident when I was looking for the Weapons of Atlas." with dis 
    mc "She was trapped inside some kind of magic box on a server run by Ulysses — the organization trying to control Eternum."
    show qq 51
    syl "Eternum?"
    show qq 47
    mc "Oh... uh..."
    mc "Yeah... that’s probably a story for another time."
    show qq 53
    ele "Please, enlighten us."
    show qq 48
    mc "Well..."
    mc "To sum it up in one sentence, your world is part of a... system of different interconnected astral planes."
    mc "Calypso can travel between them using her portals, but not to my world."
    show qq 49b
    tho "We told you not to speak the Princess’ name."
    show qq 49
    mct "Shit, I keep forgetting."
    mc "S-Sorry."
    show qq 49b
    tho "But regardless, we have no time to philosophize over the tenets of your religion."
    tho "Again, keep your answers brief."
    show qq 49
    mc "Yes... I will."
    mct "It was they who asked..."
    jump ptrial4
label trial4b:
    $ trialpoints += 1
    scene qq 50c
    mc "I broke her out of captivity myself." with dis 
    mc "The Immortals abducted her and were keeping her locked up in a camp far from here."
    mc "Since then, we’ve been on a long journey to get back to Hyril’ar."
    show qq 51b
    syl "And why did you do that, hmm?"
    syl "Were you expecting a reward? Because all you will receive is the punishment you undoubtedly deserve, scum."
    show qq 53
    ele "And why was the Princess in such a deplorable state when you were found with her?"
    ele "Even now, the druids remain uncertain if she will survive."
    play sound gear fadein 0.7
    show qq 48
    call screen neo_choice(trial5) with dis12
label trial5a:
    mc "She gave it everything she had to save me from a monster of an enemy." with dis
    mc "He was about to finish me off when she channeled all her magic into one powerful blast against him."
    show qq 53
    ele "Hah."
    ele "And I am to believe the Princess would risk her life for an insignificant human like you?"
    ele "Spare me your jest."
    jump ptrial4
label trial5b:
    $ trialpoints += 1
    mc "We were attacked by a very powerful enemy, a warrior from my realm who's been chasing us for a while now." with dis
    mc "The Princess had to channel all her magic to take him down, even while chained with dimeritium."
    show qq 53
    ele "A human warrior?"
    ele "Are you expecting me to believe the Princess would struggle against a mere human?"
    show qq 48
    mc "You should see him."
    mc "He's... barely human anymore."
    show qq 53
    ele "Please. I witnessed her defeat some of Hyril’ar’s most powerful mages when she was but forty."
    ele "Do not insult my intelligence."
    jump ptrial4
label trial5c:
    mc "I... don't know." with dis
    mc "This is how I found her when I came back to where she was."
    mc "I picked her up right away and was searching for help when I ran into General Arannis in the forest."
    show qq 53
    ele "Of course..."
    ele "How very convenient."
    jump ptrial4
label ptrial4:
    show qq 51
    syl "Even if your claims are true and you truly aided her escape from her captivity, the Princess would never lower herself enough to allow a human near her." with dis
    syl "At best, you would be nothing more than a slave, and as such, touching her is strictly forbidden."
    syl "The punishment is death — our laws are clear."
    show qq 47
    play sound gear fadein 0.7
    call screen neo_choice(trial6) with dis12
label trial6a:
    $ trialpoints += 1
    $ sylaxprovoke = False
    mc "I was useful to her." with dis
    mc "I'm a capable warrior and I can hold my own in a fight."
    mc "After I freed her, I swore to protect her until she could make it back to Hyril’ar."
    show qq 51b
    syl "You? A capable warrior?"with dissolve
    syl "Please. Even the humblest of our farmers could best you in a duel."
    show qq 47
    mc "Are you volunteering?"with dissolve
    show qq 51b
    syl "Do not provoke me, you filthy creature..."with dissolve
    jump ptrial6
label trial6b:
    $ sylaxprovoke = False
    mc "I saved her life when I freed her from captivity."with dis
    mc "The Princess felt she owed me for it, so she insisted on staying close and helping me in return."
    show qq 51b
    syl "She {i}owed{/i} you?"with dissolve
    syl "The ruler of Hyril'ar owes nothing to anyone. Least of all, someone like {i}you."
    show qq 53
    ele "Deplorable, truly."
    show qq 51b
    syl "We should cut out his tongue before he spews any more lies!"
    jump ptrial6
label trial6c:
    $ trialpoints -= 2
    mc "We joined paths after I freed her from captivity, but eventually..."with dis
    mc "With time, well..."
    mc "I guess you could say we fell for each other."
    show qq 51b
    syl "What did you just say?"with dissolve
    mc "It's true."
    if calypsopath and calypsotogether:
        mc "We even had a wild moment while she was taking a bath, completely naked."
        mc "She summoned some magical hands and–"
    else:
        mc "One night we were cuddling next to a bonfire, when–"
    play sound metalhit2
    play sound2 debris3
    play sound3 slam3
    scene qq 51e
    syl "{sc=2}ENOUGH." with vpunch 
    syl "I will not tolerate this creature further sullying the Princess’ name!" with hpunch 
    syl "No human has ever laid their vile eyes upon her sacred form, and NONE EVER WILL!" with hpunch 
    $ sylaxprovoke = True
    jump ptrial6
label ptrial6:
    play soundlow leathershort volume 0.4 fadein 1
    play sound clothes3
    scene qq 49c with dis14
    pause
    play sound2 clothes3
    scene qq 49b
    if sylaxprovoke:
        tho "Attempting to provoke Lord Sylax with such blasphemies will avail you nothing, human." with dis12
        tho "But if there is any proof that can demonstrate you were truly an ally to the Princess, and not merely one of her captors, show it now."
        tho "Or remain silent forever."
    else:
        tho "Is there any proof that can demonstrate you were truly an ally to the Princess and not merely one of her captors?"with dis12
    scene qq 49
    mc "Uh..."
    mc "Well, she told me about this place, about her story, her people."
    mc "I know things about her that she would’ve never shared with a captor!"
    tho "Hmm."
    show qq 49b
    tho "Prove it, then."
    show qq 49
    mc "Prove it?"
    show qq 49b
    tho "What do you know about our history?"
    show qq 49
    mc "Oh..."
    mc "Um..."
    show qq 49b
    tho "Who was the first Queen of the Sy-tel-quessir?"
    play sound gear fadein 0.7
    show qq 49
    call screen neo_choice(trial7) with dis12
label trial7a:
    mc "Queen Anima the Radiant." with dis
    $ trialpoints += 1
    jump ptrial7
label trial7b:
    mc "Queen Anala the Resplendent." with dis
    jump ptrial7
label trial7c:
    mc "Queen Anira the Shining." with dis
    jump ptrial7
label ptrial7:
    show qq 49b
    tho "And who was the one who enslaved her, using her powers to seize the throne?"
    play sound gear fadein 0.7
    show qq 49
    call screen neo_choice(trial8) with dis12
label trial8a:
    mc "Draxus the Usurper." with dis
    jump ptrial8
label trial8b:
    mc "Zephyros the Usurper." with dis
    jump ptrial8
label trial8c:
    mc "Yliar the Usurper." with dis
    $ trialpoints += 1
    jump ptrial8
label ptrial8:
    show qq 53
    ele "What was the name of Princess Calypso’s father, the last King of Hyril'ar?"with dis
    play sound gear fadein 0.7
    show qq 48
    call screen neo_choice(trial9) with dis12
label trial9a:
    mc "Raewyn." with dis
    $ trialpoints += 1
    jump ptrial9
label trial9b:
    mc "Sylvannus." with dis
    jump ptrial9
label trial9c:
    mc "Galnar." with dis
    jump ptrial9
label ptrial9:
    show qq 51
    syl "How old is the Princess?"with dis
    play sound gear fadein 0.7
    show qq 47
    call screen neo_choice(trial10) with dis12
label trial10b:
    mc "44 summers." with dis
    jump ptrial10
label trial10c:
    mc "68 summers." with dis
    jump ptrial10
label trial10d:
    mc "84 summers." with dis
    $ trialpoints += 1
    jump ptrial10
label ptrial10:
    show qq 49b
    tho "What is the name of the ritual performed by our people to meditate and channel our magic?"with dis 
    play sound gear fadein 0.7
    show qq 49
    call screen neo_choice(trial11) with dis12
label trial11b:
    mc "The Elarisil." with dis
    $ trialpoints += 1
    jump ptrial11
label trial11c:
    mc "The Lalariel." with dis
    jump ptrial11
label trial11d:
    mc "The Tomodin." with dis
    jump ptrial11
label ptrial11:
    tho ". . ."
    tho "Hmph."
    show qq 49b
    tho "I suppose that's enough."
    show qq 49
    mc "Alright..."
    mc "So... are we done?"
    scene qq 54
    thod "Before the Council announces its verdict, would you like to submit yourself to the Sirfalas’kadhiel?" with dis12
    show qq 54b
    mc "The Sirfalas...kadil?"
    show qq 54
    thod "The sparrow's judgement."
    thod "It is an ancient, sacred trial where a blessed sparrow chooses between two consecrated cups of water."
    thod "One is pure, the other tainted. If the sparrow drinks from the untainted cup, you will be deemed innocent. If it drinks from the corrupted one, you will be marked as guilty."
    show qq 54b
    mc "Just like that? You'd leave the whole decision up to a coin toss?"
    show qq 54
    thod "The Sirfalas’kadhiel is only used as an omen."
    show qq 50
    thod "We see the sparrow as a vessel of fate, but... fate itself is ever-shifting, so the decision always remains in the hands of the tribunal."with dis
    ele "I personally could not care less about it."
    syl "Archaic methods..."
    play sound gear fadein 0.7
    call screen neo_choice(trial12) with dis12
label trial12a:
    $ sparrowcup = random.choice([1, 2])
    scene qq 50c
    mc "I accept."with dis
    mc "I will let the gods prove my innocence."
    show qq 50
    thod "So be it, then."
    play sound armorwalk
    scene qq 55 with dis25
    play soundlow ["<silence 0.5>", sparrow]
    play sound3 move
    bla "A guard steps into the room, silently placing a small cage on the table." with dis2
    thod "If the sparrow drinks from the short black cup, you will be judged guilty."
    thod "If it drinks from the tall red one, you will be deemed innocent."
    thod "Do you agree to these terms?"
    mc ". . ."
    mc "I do."
    play sound2 birdcageopen
    play soundlow ["<silence 0.9>", sparrow]
    scene qq 56 with dis2
    bla "The guard carefully opens the cage, and a small sparrow hops out." with dis17
    mct "Come on buddy, please don't fail me..."
    play sound5 metalhitsmall2 volume 0.7
    play sound6 sparrow volume 0.5
    show qq 57 with dis08
    pause
    play sound7 sparrow volume 0.5
    play sound metalhitsmall1 volume 0.7
    show qq 58 with dis06
    pause
    play sound2 sparrow volume 0.5
    play sound metalhitsmall2 volume 0.7
    show qq 57 with dis06
    pause
    if sparrowcup == 1:
        show qq 57b 
        mc "Yes!" with dis14
        mc "Haha!"
        scene qq 47
        mc "Did you see that?!"with dis
        mc "The bird chose not guilty!"
        show qq 51
        syl "This foolish and outdated tradition means nothing."
        show qq 47
        mc "What?!"
        show qq 51
        syl "Shall we continue?"
        $ trialpoints += 1
    else:
        play sound7 sparrow volume 0.5
        play sound metalhitsmall1 volume 0.7
        show qq 58 with dis06
        pause
        show qq 58b 
        mc "Damn stupid bird..." with dis14
        show qq 51
        syl "*Mocking laugher* Not even the gods favor the human."with dis
        syl "We're merely wasting time now."
        syl "Can we cease this farce already?"
    jump ptrial12
label trial12b:
    scene qq 50b
    mc "I... politely decline."with dis12
    mc "I’d rather not put my life in the hands of a simple bird."
    jump ptrial12
label ptrial12:
    scene qq 49b
    tho "Very well, then."with dis12
    tho "That concludes all of our questions."
    tho "Is there anything more you wish to say before we render our decision?"
    scene qq 49
    play sound gear fadein 0.7
    call screen neo_choice(trial13) with dis12
label trial13a:
    $ trialpoints += 1
    mc "All I can say is that I'm innocent."with dis
    mc "I didn't do anything to the Princess. I never would."
    mc "All I ever wanted was to help her come back here."
    tho ". . ."
    jump ptrial13
label trial13b:
    mc "I want to call a witness."with dis
    if sylaxattack:
        $ trialpoints -= 1
        show qq 51b
        syl "A witness?" with dis
        syl "Where do you think you are, mortal?"
        show qq 52
        tho "We must honor his rightful claim to summon a witness, Lord Sylax."
        tho "You know this."
        show qq 51d
        syl "I will be his witness." 
        syl "The human attempted to attack me when I visited his cell to inform him that his trial was about to commence, and the guards can corroborate it."
        syl "Even if he was not the one who abducted the Princess fifteen years ago, his actions are proof of the hatred his kind harbors against us."
        syl "We must not allow him to leave this place alive."
        show qq 49
        tho "Hmm." with dis
        show qq 49b
        tho "Thank you for your testimony, Lord Sylax."
        show qq 49
        mct "Son of a bitch..."
        jump ptrial13
    show qq 53
    ele "A witness...?"with dis
    ele "Who? One of the guards?"
    show qq 48
    play sound gear fadein 0.7
    call screen neo_choice(trial14) with dis12
label trial14a:
    mc "General Arannis." with dis
    mc "He’s the one who found me with the princess in the forest."
    mc "He can testify that I was injured too, and that I was actually trying to take care of the princess, not hurt her or keep her against her will in any way."
    show qq 39
    tho "Hmmm... General? The human has requested your testimony." with dis 
    tho "Could you share your account of the events?"
    show qq 39b
    ara "Of course, my lord."with dis08
    ara "I came upon the human and the Princess while walking through the forest with my daughter, Lorelei — that is correct."
    ara "I immediately carried her to the druids for healing, and ordered the human's seizure."
    show qq 64
    tho "What was the human doing when you discovered him?"
    show qq 39b
    ara "He was holding the Princess in his arms."
    ara "Both were gravely wounded."
    show qq 64
    tho "Did you perceive any indication of ill intent on the human’s part?"
    show qq 39b
    ara "I... cannot say with certainty, my lord."
    show qq 51b
    syl "So you attest to the human's benevolence?"
    syl "Is that what you are implying?"
    show qq 39b
    ara "I..."
    show qq 65
    ara "I certainly cannot do that either."with dis08
    ara "All I can confirm is that he was in physical contact with the Princess — her bare skin, no less — and she was already unconscious when we arrived."
    ara "He claimed he had no intention of reaching Hyril’ar and that his arrival was merely a matter of chance."
    ara "That is all I know."
    scene qq 49b
    tho "Understood. Thank you, General." with dis12
    tho "That will be all, then."
    show qq 49
    mct "I don't think that was as helpful as I thought it'd be..."
    jump ptrial13
label trial14b:
    $ trialpoints += 2
    $ loreleitestimony = True
    mc "Lorelei." with dis
    show qq 53
    ele "Lore... who...?"
    show qq 48
    mc "General Arannis' daughter."
    mc "She’s the one who found me with the Princess in the forest."
    mc "She can testify that I was injured too, and that I was actually trying to take care of the Princess, not hurt her or keep her against her will in any way."
    show qq 39
    tho "Hmm... General?" with dis 
    tho "Is your daughter here?"
    show qq 39b
    ara "She is, my lord."with dis08
    ara "She is waiting for me at the entrance of this very building as we speak, for she believed this may occur, given her involvement in the matter."
    show qq 49b
    tho "Could you summon her to this room?"with dis
    tho "The human has requested her testimony."
    show qq 49
    ara "Of course, my lord."
    gua "Already on it, sir."
    mct "Lorelei is like the only nice person I’ve met in this place since I got here."
    mct "I hope this doesn’t backfire..."
    play sound armorwalk fadein 1
    scene qq 59
    bla "Within moments, one of the guards steps into the room, the elven maid quietly by his side." with dis22
    gua "Here she is, General."
    ara "Thank you, Isilion."
    scene qq 64
    tho "My apologies for the interruption, my lady..."with dis 
    tho "But the human has requested your testimony. It will only take but a moment."
    show qq 62
    lo "I-It is no problem, my lord." with dis 
    show qq 64
    tho "He claims you were the person who found him."
    tho "Could you share your account of the events?"
    show qq 60
    lo "Uh..."
    lo "Well, I was walking through the forest with my father, gathering mushrooms and plants, when I heard a strange sound of splashing coming from a nearby pond."
    show qq 62
    lo "I was startled because there is no running water in that pond."
    lo "So... whatever caused the noise had to be something larger than a boar."
    show qq 51
    syl "By Turska's mercy, get to the point."
    syl "I do not have all day."
    show qq 63
    lo "And then... yes, I found the human holding the Princess in his arms."
    lo "And my father arrived not long after."
    show qq 64
    tho "Did you perceive any indication of ill intent on the human’s part?"
    show qq 60
    lo "Erm..."
    lo "No... not really."
    show qq 62
    lo "They were both injured, but the human appeared to be deeply concerned for the Princess."
    show qq 60
    lo "He asked for help on her behalf, and his distress seemed... genuine."
    show qq 51b
    syl "So you attest to the human's benevolence?"
    syl "Is that what you are implying?"
    show qq 61
    lo ". . ."
    show qq 39
    lo ". . ."
    lo "Um..."
    show qq 64
    tho "Please, my lady, I truly wish to hear your opinion on the matter as well."
    tho "Do you vouch for the human's goodwill?"
    show qq 61
    lo ". . ."
    show qq 60
    lo "I..."
    show qq 62
    lo "Honestly... I do, yes."
    lo "I do think he is innocent."
    show qq 51b 
    syl "Agh, this is an outrage!" 
    syl "Why are we even entertaining the words of this... commoner?"
    play sound impactwood
    play sound2 metalhit2
    play sound3 debris3
    play sound4 whoosh6
    scene qq39
    bla "General Arannis strikes the ground with his spear." with vpunch
    syl "Huh."
    show qq 51
    syl "Is there a problem... Arannis?"
    show qq 65
    ara "None, my lord."
    ara "I simply... would remind the court that Lorelei is not only my daughter but also one of the Princess' royal maids."
    ara "As such, she holds noble status and is far from being considered... a commoner."
    show qq 51
    syl "And what if I choose to continue referring to her as such?"
    show qq 65
    ara "Then... I would be compelled to defend my family’s honor."
    show qq 51b
    syl "Is that a threat, General?"
    syl "Have you forgotten your place?"
    show qq 52
    tho "Enough."
    tho "You are a regent of the most powerful kingdom on this continent, Lord Sylax. Conduct yourself accordingly."
    show qq 51
    syl "Tch. Whatever you say, old man..."
    show qq 64
    tho "Thank you for your testimony, my lady." with dis
    tho "You may take your leave now."
    show qq 62
    lo "It was an honor, my lord."
    jump ptrial13
label trial13c:
    $ trialpoints -= 2
    mc "You're gonna regret this..." with dis
    mc "Once the princess wakes up and sees how you've been treating me like a dog, she'll have you all hanging from a rope."
    mc "All of you."
    tho ". . ."
    show qq 51b
    syl "And now you dare to threaten us?"
    syl "You filthy human..."
    show qq 53
    ele "Enough. Let us be done with this."
    jump ptrial13
label ptrial13:
    scene qq 54
    thod "Very well..." with dis14
    thod "The three members of the Council shall now render their verdicts." 
    show qq 54b
    mct "Oh shit..."
    mct "Here we go."
    mct "The moment of truth."
    show qq 54
    thod "If their vote is unanimous, the human will either leave our lands after being commended for returning the Princess, or sentenced to immediate execution."
    show qq 54b
    mct "I-Immediate?"
    show qq 54
    thod "If their votes are divided, he will remain imprisoned until the Council reconvenes, allowing time for further deliberation and consideration."
    show qq 51
    syl "Guilty."with dis12
    show qq 47
    mct "This motherfucker..."
    mct "He never gave a damn about who I was or what I had to say."
    show qq 48
    ele "Hmph."with dis12 
    show qq 53
    ele "Guilty."
    show qq 48
    mc "What?!"
    mc "Have you not been listening to me?!"
    mc "I didn't do it!"
    mc "The Princess would tell you herself!"
    show qq 49
    tho ". . ." with dis12
    mc "*Heavy breathing* . . ."
    tho ". . ."
    play sound3 risingshortbb
    stop music fadeout 3
    if trialpoints > 8:
        play soundloop birds fadein 6
        play soundloop3 river fadein 7 volume 0.5
    tho "Hmm." with dis12
    if trialpoints > 8:
        jump trialsuccess
    play sound deception
    play sound2 deception
    show qq 49b
    tho "Guilty."with dis08
    show qq 49
    play music hyrilartension2 fadein 5 volume 0.8
    mc ". . ."with dis08
    mc "W-Wha..."
    show qq 66
    mc ". . ." with dis17
    mc "What...?"
    mc "You're kidding, right?"
    show qq 54
    thod "By the unanimous decree of this Council, the defendant stands condemned for the grievous crimes he was accused of." with dis12
    thod "The abduction of Princess Calypso, the defilement of her sacred form, the infliction of harm upon her, and the attempt to destabilize our realm."
    show qq 66
    thod "The sentence... is death."
    thod "The execution will be carried out immediately."
    mc ". . ."
    mc "But... y-you have no proof."
    mc "I was trying to help her!"
    show qq 39
    tho "General Arannis." with dis12
    tho "You're in charge of executing the sentence."
    show qq 65
    ara "Yes... my lord."
    play sound mcdecapitationsoundpre
    scene qq67
    pause 2
    bla "Several guards quickly close in around you and force you to kneel." with dis12
    mc "*Whispering* What the fuck is going on..."
    mc "I-I can't..."
    mc "I can't die here. Not after everything I've been through."
    play soundlow chain3
    mc "I need to go back!" with hpunch 
    mc "E-Everyone is... waiting for me."
    scene qq 49
    mc "Lord Thorund!" with dis12
    mc "You're the only one who seems to be reasonable here, please, just listen!"
    mc "I didn't do it! I swear!"
    mc "I'd never hurt the Princess, you have to believe me!"
    mc "Just wait until she wakes up! She'll explain EVERYTHING!"
    tho ". . ."
    show qq 49b
    tho "Execute the prisoner."
    show qq 49
    mc "W-Wait..."
    tho ". . ."
    $ trialdead = True
    play sound mcdecapitationsound
    play sound2 chain
    scene mcexecution with dis14
    stop music fadeout 9
    pause 5.3
    stop music
    scene black with dis06
    pause
    bla ". . ." with dis15
    stop sound
    play soundlow glitch4
    scene caveglitch2
    pause
    play soundlow glitch4
    scene caveglitch2
    play music hriddles
    pause 0.4
    jump trialreset
label trialsuccess:
    if trialdead:
        $ trialpoints -= 2
    play music2 hyrilarforest fadein 8 volume 0.7
    scene qq 49b
    tho "Not guilty." with dis
    show qq 49
    mct "Oh, thank you Holy Lord Baby Jesus Christ Almighty..."with dis08
    show qq 68
    ele "What?!" with dis
    ele "Are you truly out of your mind?!"
    show qq 51d
    syl "What is the meaning of this madness?"with dis
    syl "You are turning your back on your own people, Thorund."
    syl "This is nothing less than treason."
    show qq 64
    tho "Given that we have not reached unanimous agreement, the decision shall be postponed. A new vote will be called after a period of reflection."
    tho "Until then, this assembly is adjourned."
    show qq 51d
    syl "Why delay the inevitable?"
    syl "What is your interest in keeping us here?"
    syl "What if the human is merely waiting for reinforcements to arrive?!"
    show qq 52
    tho "I assure you, my motives are only to uncover the truth behind this matter."
    tho "We speak for both Hyril'ar and the Princess herself, do not forget."
    show qq 51b
    syl "Bah."with dis
    show qq 53
    ele "*Sighs* I was hoping to return to Eryan'dol today..."with dis
    ele "How inconvenient..."
    show qq 49
    mc ". . ."with dis12
    mc "...Thank you."
    mc "Thank you so much."
    show qq 49b
    tho "Do not mistake my judgment for weakness, human."
    tho "A new vote will be called shortly, once we have further deliberated."
    tho "Until then, guards, return the prisoner to his cell. He shall remain under strict surveillance."
    play sound armorwalk
    scene qq 69
    gua "Yes, my lord." with dis2
    gua "It shall be done."
    gua2 "This way, human..."
    mc ". . ."
    stop soundloop fadeout 9
    stop soundloop3 fadeout 9
    stop music2 fadeout 8
    scene black with dis3
    show screen sometimelater with dis25
    pause 
    play soundloop2 cave fadein 7
    hide screen sometimelater
    scene qq 70 
    with dis3
    pause
    mc "*Sighs* (Man, I hope I can get out of here soon...)" with dis15
    mct "I really don't want to spend Christmas locked up in this place."
    mct "There can't be more than a few days left in the real world..."
    scene qq 71 
    mct "Mmh..."with dis17
    mct "I wonder how long that “period of reflection” is supposed to take." 
    mct "Because without my powers, I feel like a useless piece of shit. I'm just a sitting duck with no way to escape."
    mct "If at least I had some way to let the girls know where I am..."
    mc "Hmmm..."
    mct "Hmph, wish Chang was here."
    mct "He’d probably be able to whip up some insane yet effective plan."
    play sound3 rat
    scene qq 72 with dis14
    pause
    scene qq 73
    bla "You notice a small rat squeezing through the bars of your cell door." with dis12
    mc "Sup', buddy."
    mc "Getting kinda cold here, huh?"
    play sound4 ratrun
    play soundlow rat
    scene qq 74 with dis15
    bla "The creature scurries down and begins grooming its tiny ears." with dis14
    mc "Heh."
    mc "If you're here for the food that bastard tossed on the floor earlier, go for it, man. It's all yours."
    mc "I wasn't planning to–"
    play music ["<silence 3>"]
    queue music sugarplum 
    stop soundloop2 fadeout 11
    play sound5 smokebomb
    play sound7 steam2 volume 0.5
    scene loreleiappear with hpunchl
    lo ". . ." with dis15
    mc "W-What the..."
    play sound debris
    show qq 76
    mc "*Standing up* What the hell..." with dis14
    lo "*Whispering* Huh... this place is way smaller than I thought."
    lo "*Whispering* Where do you... take care of... your needs...?"
    mc "L-Lorelei?!" with hpunch 
    show qq 77
    lo "Shhhh!"with dis
    lo "Silence! The guards cannot know I am here!"
    lo "I would be severely punished!"
    mc "*Whispering* O-Oh... sorry, my bad."
    show qq 78
    mc "So..."with dis12
    mc "Did you come to help me escape?"
    mc "You did, right??"
    show qq 84
    lo "Indeed, I did!" with dis
    show qq 85
    mc "HELL YEAH!"
    mc "I knew you were one of the good ones!"
    mc "I could tell when we carried Calypso here — you kept asking me questions, but there was no malice in them."
    mc "And Calypso told me about you too, I remember!"
    if loreleitestimony:
        mc "Aaaah, yeah! I knew I could trust you! That’s why I asked the Council to hear your testimony!"
    show qq 84
    lo "Y-You honor me, human!"
    show qq 85
    mc "You can call me [mc]!"
    show qq 84
    lo "Ohhh... [mc]..."
    lo "That name sounds very... mortal!"
    show qq 85
    mc "Alright, alright, enough chit chat! There's no time to lose!"
    mc "Let's get out of here!"
    show qq 84
    lo "Uh... well, yes, about that..."
    lo "We cannot exactly... escape just yet."
    lo "I mean... you cannot. Teaching you the transmogrification spell in less than two months would be utterly impossible."
    show qq 85
    mc "What?!"
    mc "And then why are you here?!"
    show qq 82
    lo "Well..."with dis 
    lo "I must admit, I was quite curious to see you up close once more. Without all the blood and bruises, this time."
    lo "I have never encountered a human before."
    lo "You do not look like they do in text books. You have no body fat."
    lo "And your body hair is... scarcely present. Is that normal for your kind?"
    show qq 83
    mc "Um... I guess it depends...?"
    show qq 82
    lo "Uhh..."
    show qq 83
    lo ". . ."
    mc "Is that really all you came to say?!"
    show qq 79
    lo "Well, no, I also came to... warn you."with dis 
    show qq 78
    mc "Warn me?"
    show qq 79
    lo "Yes... um..."
    lo "I cannot stay here for long, but to put it simply..."
    lo "After the trial, the three members of the Council deliberated further, and... it seems they have reached a consensus after all."
    lo "They intend to... have you hanged in three days."
    show qq 78
    mc "HANGED?!" with hpunch 
    mc "Oh, fuck my life..."
    mc "B-But... this is madness!"
    mc "The Princess would never allow this! She can explain everything!"
    mc "Where is she now?!"
    show qq 79b
    lo "She has not awoken since the day she arrived." with dis15
    lo "Despite our druid’s best efforts, her fever remains dangerously high."
    if calypsopath and calypsotogether:
        mct "Damn... poor Caly."
        mct "She's like this because of me. It makes me feel awful."
        mct "I need to get out of here and find a way to help her somehow..."
    else:
        mc "Damn..."
    lo "After her disappearance, all the other maids were gradually relocated to other realms, leaving me as the only one remaining."
    lo "We have strict rules regarding contact with her body — only maids and her family are permitted to touch her."
    lo "And as she is unmarried and has no living relatives, well... that makes things even more difficult."
    mc "I understand..."
    show qq 78
    mc "Rest assured, I know she'll pull through. She's the strongest person I know." with dis15
    mc "But... if she doesn’t wake in three days... it could be too late for me."
    mc "I just need time!"
    show qq 79
    lo "Perhaps I could try to... convince my father to intervene."
    lo "Maybe he could persuade the Council to exile you to the Hollow Veil, a hidden fortress on the far side of the continent where the most dangerous prisoners are sent."
    lo "That place is entirely isolated, though, so even if the Princess were to awaken, you would still have to remain there for... some time."
    show qq 78
    mc "Yes! At least that sounds better than getting hanged in three days!"
    mc "How much could “some time” be? Days? Weeks?"
    show qq 79
    lo "Well... you would likely have to await the first revision of the sentence, so... it may not be too severe."
    lo "Perhaps only three or four decades."
    show qq 78
    mc "WHAT?!"with hpunch
    mc "Forty bloody years?!"with hpunch
    mc "I don't live 6000 years like you guys, that's an entire damn lifetime to me!"
    show qq 79
    lo "Well... there is also..."
    lo "Another alternative."
    lo "One that would involve... waking the Princess."
    show qq 78
    mc "Waking the princess...?"
    mc "Wait, seriously? That's an option?!"
    mc "Why haven't you done that yet?"
    show qq 79
    lo "Well... it would require me to venture deep into the forest. I would be gone for at least two days. Maybe more."
    lo "But... the issue is that the remedy I seek is considered dark magic — utterly forbidden by our laws."
    show qq 78
    mc "But it'd still help the princess, right?"
    show qq 79
    lo "Possibly, but..."
    lo "If I fail to find it, and they learn of my attempt to procure it for the sake of a human..."
    lo "Or worse, if I succeed, and the Princess awakens only to reveal you are not truly her ally as you claim..."
    lo "I would be cast out. Or imprisoned. Or... even sold away."
    lo "Not even my father's influence would save me."
    show qq 78
    mc "I see..."
    show qq 79
    lo "And to be honest..."
    lo "I am not even sure why I am here in the first place."
    lo "My father always said..."
    lo "W-Well, everyone has always said that I am too naive."
    lo "Too curious for my own good."
    lo "And... erm..."
    show qq 78
    lo ". . ."
    mc "Yeah?"
    show qq 79
    lo "I suppose what I am trying to ask is..."
    lo "Is my intuition truly correct?"
    lo "Can I... trust you?"
    show qq 78
    mc "Yes."
    mc "A hundred percent."
    lo ". . ."
    mc "Look, I know I don't have any solid way to show you that I can be trusted, but..."
    mc "I also know you wouldn’t have risked everything to come here unless you knew a huge mistake was about to happen."
    mc "So... I can only hope you rely on your intuition."
    mc "I'm innocent, Lorelei."
    mc "I'd NEVER harm Princess Calypso."
    menu:
        with dis
        "She means a lot to me [calypso_pts]":
            $ calypso_points += 1
            mc "Especially after... everything she's come to mean to me."with dis
        "I owe it to her":
            mc "I owe her everything."with dis
        "I have great respect for royalty":
            mc "You could say I hold royalty in high regard, after all."with dis
    lo "Hmm."
    show qq 85
    lo "Hmph." with dis12
    show qq 84
    lo "Alright."
    lo "I will do it."
    show qq 85
    mc "You will?! You'll go find that dark magic herb?"
    mc "Or... animal. Or rock. I'm not sure."
    show qq 84
    lo "Yes."
    lo "Or... at least I will try."
    lo "I trust you, huma—I mean... [mc]."
    show qq 85
    mc "Thank you!"
    mc "I will be waiting for you!"
    mc "Not like I have much of a choice, but... you get what I mean."
    show qq 84
    lo "I will be back in three days at most!"
    lo "Just promise me you will–"
    play sound dooropencloseecho fadein 2
    scene qq 86
    gua "May the ancients grant me patience, what is all this chattering?" with dis22
    mc "Oh shit..."
    gua "I could hear the human from the main hall. Are you friends with him now?"
    gua2 "Nah, he’s just been muttering to himself for a while."
    gua2 "Pretty sure he’s finally losing it."
    gua "Heh, really? Let me see him."
    play soundlow transformpower volume 0.5
    play sound2 ["<silence 1>", armorwalk]
    scene qq 14 with dis2
    scene qq 13 with dis22
    gua "Well, well... look who's still breathing." with dis17
    gua "Did the trial make you lose your mind? Or you are just enjoying another day of quality conversations with the stone walls?"
    mc "I'm good, thanks for asking."
    mc "Just talking to myself. Helps with the anxiety, y'know."
    gua "Talking to yourself, huh? You sure it’s not the lack of food or sunlight slowly frying your brain?"
    mc "Nah, no worries."
    mc "If anything, maybe the lack of women."
    mc "Any chance you’ve got a lovely elven maiden to keep me company?"
    gua "Heh."
    gua "Of course."
    gua "Would you prefer a noblewoman, or perhaps a farmer’s virgin daughter?"
    mc "I’m not picky. I’ll take whatever’s available, thanks."
    gua "*Chuckles* Heheh."
    play sound2 armorwalk
    scene qq 14 with dis17
    gua2 "Look who's making friends with the human now." with dis12
    gua "*Chuckles* Well, he might be an inferior race, but you have to admit this one’s pretty funny."
    mct "That was close..."
    scene qq 87
    bla "Once you're certain the guard is gone, you turn around and spot Lorelei — now a tiny rat once again." with dis17
    scene qq87
    lo "*Waves*"
    play sound4 ratrun volume 0.5
    play soundlow rat
    scene qq 88 
    bla "Moving faster than a shadow, she quickly slips through the bars and disappears." with dis2
    mct "And... there goes all my hope."
    play sound ["<silence 0.3>", debris]
    play sound2 ["<silence 0.3>", fall2]
    show qq 71
    mc "*Sitting on the floor* (Oh, man...)" with dis15
    mct "These next three days are gonna feel like an eternity."
    mct "Fucking hell..."
    show qq 1 with dis15
    mct "I wonder what the girls are up to right now. Bet they're worried sick..."with dis12
    mc "*Sighs* Aggh..."
    mct "God, I miss them..."
    stop music fadeout 8
    play soundloop forest fadein 7
    scene qq 89 with Dissolve(3.7)
    pause 
    $ renpy.music.set_volume(0.3, channel='soundloop3')
    play soundloop3 whistlesong 
    player "{bt=3}*Whistling* Mmh-mmhhh-hhmm-mmmh..."with dis15
    $ renpy.music.set_volume(1.0, delay=1.0, channel='soundloop3')
    play sound footsteps3
    play sound2 stairswood2
    show qq 90 with dis2
    bla "The innkeeper begins his morning preparing the fresh bread to serve throughout the day, all while whistling a cheerful tune." with dis2
    play music sadmystery fadein 8
    stop soundloop3
    play sound horse
    play sound3 rocks
    play sound5 sword3
    play sound6 slam
    scene qq91
    player "{sc=4}AAAAAAARGHHH!!!" with hpunchl
    player "{sc=3}Jesus fucking Christ!" with hpunch 
    scene qq 93
    x "Caught you with the hands in the cookie jar, egghead!"with hpunch 
    show qq 92
    player "Oh, for fuck's sake, you again?!"
    player "I already told you! I don't know where he is!"
    show qq 93
    x "Oh, so you're telling me it's just a wild coincidence that you were the last one to see him, then five days later, you're back here celebrating something?"
    show qq 92
    player "Celebrating what?!"
    player "I'm just grabbing some bread from the warehouse!"
    show qq 93
    x "Where are you hiding him?!" with hpunch 
    show qq 92
    player "For the last time, I left your friend at the inn! When I came back, half the damn room was burnt to the ground!"with hpunch 
    player "There was nothing else around, I swear on my life!"
    player "I don’t know what happened, or where he and that elf ran off to!"
    show qq 93
    x "You better start talking or I'll paint the snow red with your blood!"with hpunch 
    play sound footsteps3
    play soundlow horse
    scene qq 94
    n "Come on, Alex, let's go check the area." with dis2
    n "We already questioned him, he doesn't know anything."
    show qq 93
    x "What if he's just playing with us?!"
    x "What if he kidnapped both of them and has Calypso locked up in some freaky-ass sex dungeon?"
    show qq 94
    n "He’s nowhere near powerful enough to pull off something like that, and you know it."
    n "Uh... no offense, sir."
    show qq 92
    player "N-None taken, ma'am!"
    player "I'm as powerless as one can be! No sex dungeons I swear!"
    show qq 92b
    x "Mmmmhhh..."
    show qq 93
    x "You better not be playing us, John."
    x "If I find out you're hiding something, I swear I’ll personally come back and skin you alive."
    show qq 92
    player "I'm not! I swear on everything that's sacred!"
    show qq 93
    x "You better..."
    x "Now get the fuck out of my sight before I regret letting you go."
    show qq 92
    player "Y-Yes!"
    play sound run
    play soundlow sword2
    scene qq 95
    x "Mmmrrrhh..." with dis2
    show qq 94
    n "Are you okay, Alex...?"
    show qq 95
    x "Yes."
    if alexpath:
        show qq 94
        n "Are you sure?"
        show qq 95
        x ". . ."
        x "Yeah, I just..."
        x ". . ."
        x "...Sorry about that."
        x "I get irritable when I'm anxious."
        x "I'll go for a walk and clear my head."
        show qq 94
        n "You have nothing to apologize for."
        show qq 95
        x "Hmph."
        x "Thank you."
        show qq 94
        n "We'll find him, Alex."
        n "It’s not the first time one of us has had to go off the grid for a mission."
        n "It’s just... taking a bit longer this time."
        n "But we're gonna find him."
        show qq 95
        x "I... I know."
    else:
        x "I'm just annoyed we have to deal with all of this because of [mc]’s recklessness, that's all."
        x "But we will find him."
    x "And when he gets back... I’m gonna kick his butt so hard he’ll be sitting down to pee for a week."
    show qq 96
    n "*Chuckle* Hmm."
    play sound horsewalk
    play sound2 horse
    play sound3 chair2
    scene qq 97
    p "*Sitting down* Aaaghh..." with dis15
    p "Another fail..."
    show qq 98
    p "I've asked everyone in the village, and no one's seen him."
    p "Maybe we should just join Annie, Nova, and Luna in Valley of Kings and try our luck there."
    show qq 99
    n "What about Calypso?"
    show qq 98
    p "Same thing. Last time anyone saw her was over five days ago."
    p "And she's a hard one to miss."
    show qq 99
    n "I know five days feels like forever, but we’ve only just started looking."
    n "Eternum's huge. There are a ton of places they could be."
    show qq 98
    p "Yeah, but... he'd never leave for so long without saying something."
    p "What if..."
    show qq 99
    n "No. No “what ifs”."
    n "Obviously something came up, but they're both together. They'll be fine."
    n "Maybe they got stuck in some super long dungeon. When we were in The New World server, a goblin nearly trapped us in a magic maze for weeks."
    show qq 100
    p "Mmmh."
    n "Or... who knows, maybe Calypso even figured out a way back to Hyril'ar, and they’re just visiting."
    p "Hmph."
    show qq 98
    p "Yeah... I hope so."
    play sound footsteps3
    scene qq 101
    d "Alright, the mill's clear..." with dis2
    show qq 99
    n "Oh Jesus, what happened to you?"
    show qq 101
    d "I'm good, I'm good."
    d "In the end the rumors were right, and the miller was mixed up in some shady business, but... it turned out to just be some drug smuggling."
    d "No sign of [mc] or Calypso anywhere."
    show qq 99
    n "Then why is your armor all trashed? Did he do this to you?"
    show qq 101
    d "Oh... no, it got broken by Con back in that dungeon where we found Thanatos a few months ago."
    d "I should’ve gotten it fixed ages ago, but... well, money’s been tight."
    show qq 102
    d "Things got a little heated at the mill too, though. He tried to make me pay for the door I busted down, even though I apologized! Can you believe that?"with dissolve
    d "Then he sent his goons after me, so... I had to handle them."
    d "*Muttering* Bastards."
    show qq 101
    d "*Sighs* But... yeah, as I was saying... it's all fine now." with dissolve
    d "No worries."
    show qq 99
    n "Please, be careful, Dalia."
    n "Last thing [mc] would want is for you to get hurt looking for him."
    show qq 102
    d "I swear, whoever’s holding him better pray I don’t find them first."
    d "They have no idea what's coming."
    play sound stairswood2
    scene qq 102b
    x "Hey, I see smoke coming from Jebediah's house!" with dis15
    x "People said he was one of the first to show up at the inn after the so-called “explosion”. I bet he can give us an explanation..."
    show qq 94
    n "Oh, finally!"
    n "He must have just logged in now."
    show qq 102
    d "Oh, don't worry, girls... if he knows something, I'll make sure he talks."
    show qq 101
    d "And if he doesn't..."with dissolve
    d "*Sighs* At least we'll be able to cross another name off the list."
    if penelopepath and daliapath:
        show qq 102b
        x "Let's go! Before he runs away!"
        show qq 103
        d "Hmm."
        show qq 104
        d ". . ." with dissolve
        show qq 106
        p ". . ."
        show qq 104
        d ". . ."
        show qq 105
        d "Hmph." with dis
        show qq 106
        p ". . ."
        show qq 107
        p "Hmmph." with dis
    show qq 97
    n ". . ." with dis17
    play sound2 horse2
    play sound3 armor
    scene qq 108
    n "*Petting the horse* You'd better appear soon, [mc]..." with dis17
    n "Only five days and we're already falling apart over here."
    n "Where on earth are you..."
    stop music fadeout 10
    stop soundloop fadeout 14
    scene black with Dissolve(3.3)
    play musicb twinkle fadein 45 volume 0.8
    pause 
    mc "Mmmmhh..." with dis2
    play sound7 clothes3
    scene qqi 1
    mc "*Opening your eyes* Hmm..." with dis27
    mct "Holy hell... this has gotta be the worst headache of my life."
    mct "Sleeping on cold, wet stones without so much as a pillow is probably not great for the nervous system."
    play sound clothes3
    play soundlow debris volume 0.8
    scene qqi 2
    mc "*Sitting up* Dear Lord..." with dis15
    mct "Feels like my skull's about to crack open."
    mct "Should I call the guards? I doubt asking them for a painkiller is gonna get me far, though..."
    mct "Maybe I could–"
    show qqi 3
    mc ". . ." with dis12
    show qqi 4 
    mc ". . ." with dis 
    play sound deception
    scene qqi 5 
    pause 
    mc "W-What the fuck..." with dis
    mc "What... what's going on..."
    show qqi 6
    id "Good morning, cellmate."
    show qqi 5
    mc "N-No..."
    mc "No... you're not real..."
    mc "Get the fuck out of my head!"with hpunch 
    mc "You're the reason my head feels like it's splitting open, aren't you?!"
    mc "Is the Founder behind this?! Thanatos?!"
    id "Hmm."
    show qqi 6
    id "What makes something real, I wonder?"
    id "Is it what you can see, touch, hear? But then... what about dreams?"
    id "If you feel fear in a nightmare, warmth in a memory... are those feelings not real?"
    id "Do they not stick with you? Does your heart not pump and throb?"
    show qqi 5
    mc "I don't care."
    mc "I don't give a shit about anything you have to say."
    mc "Just... leave."
    show qqi 6
    id "Or maybe reality is... just a word we made up to explain things we don't understand."
    show qqi 5
    mc "Hah, “we”? Don't lump me in with... whatever the hell you are."
    mc "I was born. You were made."
    mc "You're just a tool. I make my own choices."
    id "*Laughs* Mm-hm."
    show qqi 6
    id "We're not so different, [mc]."
    id "The chain binds us all."
    show qqi 5
    mc "I remember seeing you when I got shot in that alley..."
    mc "And again when Thanatos nearly killed me at the inn."
    mc "Why are your visions haunting me? You've never told me anything useful."
    show qqi 6
    id "Perhaps I cannot say more."
    id "Or maybe I just said exactly what you needed to hear."
    id "Maybe I'm just your conscience. A voice in your head."
    id "Or perhaps... you're simply not asking the right questions."
    show qqi 5
    mc ". . ."
    show qqi 7
    id "May I tell you a little story, [mc]?" with dis17
    show qqi 8
    mc "No."
    mc "I'm done with you and your riddles."
    show qqi 7
    id "It will be the last one, I promise."
    show qqi 8
    mc ". . ."
    mc "*Sighs* If I answer, will you finally leave me in peace?"
    show qqi 7
    id "I will."
    show qqi 8
    mc ". . ."
    mc "Alright..."
    mc "Tell me. And leave for good."
    id "Hmm."
    show qqi 7
    id "Imagine... an ancient door... worn smooth by countless hands..."
    id "And a man standing before it."
    id "He knocks once... silence. He knocks twice... nothing."
    id "Again and again, he pounds against the wood until his knuckles bleed, but the door remains shut."
    show qqi 8
    mc "Hmm."
    show qqi 7
    id "Frustrated, he finally turns to leave, but... at the last second... something urges him to try once more."
    show qqi 4
    id "Then..." with dis17
    id "With a weary sigh, he lifts his hand and knocks one more time." 
    mc ". . ."
    id "What do you think happens next...?"
    menu:
        with dis14
        "[gr]The door opens":
            $ opendooridriel = True
            show qqi 5
            mc "The door opens." with dis15
            id "Hmph."
            show qqi 6
            id "Indeed... it does."
            show qqi 5
            mc "Hmm, figured as much."
            mc "But why? What made this time different from all the others?"
            show qqi 6
            id "Who knows."
            id "Maybe it was the way he knocked. Maybe it was his intention. Maybe it was never about the door at all, but about him."
            id "Something was different this final time. And that was enough."
            show qqi 5
            mc "That... doesn't really make sense."
            id "Hmph."
            show qqi 6
            id "Sometimes, it never does..."
        "The door stays closed":
            show qqi 5
            mc "The door stays closed." with dis15
            id "Hmph."
            show qqi 6
            id "Indeed... it does."
            show qqi 5
            mc "Hmm, figured as much."
            mc "So... tell me, where's the twist? Why did the door never open?"
            show qqi 6
            id "Who knows."
            id "Perhaps it was never meant to open for him. Or maybe... it was never meant to open at all."
            id "In the end, some doors are meant to remain closed forever, no matter how many times you knock."
            show qqi 5
            mc "So... that's it?"
            mc "That... doesn't feel right."
            id "Hmph."
            show qqi 6
            id "Sometimes, it never does..."
    scene qqi 5
    mc ". . ."
    mc "So..."
    mc "What was behind the door?"
    id "Hmm."
    show qqi 6
    id "That's a good question."
    play sound3 risingshort3
    show qqi5 
    pause 2
    stop musicb
    play sound2 debris
    play sound4 knock3
    play soundlow slam3
    play soundloop cave fadein 1
    mc "AAARRGHhhhh!" with flashfaster
    mc "F-FUCK!" with hpunch
    mct "Fucking hell... I'm drenched in sweat."
    mct "Jeez, I didn't even know you could dream in Eternum."
    mct "I mean... I hardly ever dream in the first place."
    play sound clothes3
    play soundlow debris volume 0.8
    scene qq 71
    mc "*Sitting up* Mmmhrh..." with dis15
    mct "Aghh... I should’ve never come in here without the neural implant."
    mct "Maybe I'd already be logged off by now, thanks to Ulysses' automatic disconnection."
    play sound5 knock3
    show qq 72
    gua "*Knocking on the door* Are you deaf, or what, human?!" with dis 
    show qq 1
    mc "Yeah, yeah, I'm awake..." with dis
    mc "What now? Is it bath time already?"
    gua "You have been summoned. You need to come with us."
    mc "Oh..."
    mct "Summoned...?"
    mct "Hmm... this might be my chance to defend myself again. Maybe I won’t even have to rely on Lorelei."
    mc "Do I have to change my clothes again?"
    gua "That will not be necessary. Just follow us."
    mc "Mmh, alright then."
    stop soundloop fadeout 10
    play soundloop2 birds fadein 5
    scene qqi 9 with dis27
    bla "After joining General Arannis, the guards escort you towards a nearby canyon, leading you away from the building you saw yesterday." with dis27
    ara "This way."
    play sound footsteps3 volume 0.8
    play soundlow armorwalk volume 0.8
    scene qqi 10 with dis22
    mc "Thank you for not chaining me up this time, guys, I appreciate it." with dis17
    mc "I know we didn't exactly get off to a great start, but..."
    show qqi 11
    mc "Trust me, once the Princess wakes up, this'll all make sense." with dis12
    mc "You'll see how I'm–"
    scene qqi12
    mc "Huh?"
    scene qqi12b
    bla "You narrow your eyes, still struggling to adjust after being deprived of sunlight for so long."with dis15
    scene qqi 12
    mc "Huh...?" with dis15
    mc "Is that a...?"
    ara "Seize him."
    mc "Eh...?"
    play sound armor
    play sound2 grab3
    play sound3 debris3
    play music ["<silence 0.1>"]
    queue music hyrilartension2
    scene qqi 13
    bla "Two guards grab you from behind, dragging you towards the gallows." with hpunchl
    mcsc "Whoa, whoa, whoa!" with hpunch
    mcsc "What the fuck is going on here?!"with hpunch
    show qqi 14
    ara "For the crimes committed against Hyril'ar and the Princess of the realm... you are hereby sentenced to death." with dis08
    show qqi 13
    mc "WHAT?!"with hpunch
    mc "Are you fucking kidding me?!"
    mc "I thought you believed me, Arannis!"
    mc "You know I didn't do it!"
    show qqi 14
    ara "Let us not delay this any longer. Take him to the gallows."
    play soundlow armor
    play sound stairswood2
    play sound2 rope
    play sound4 knot
    scene qqi 15 with dis2
    play sound3 rope2
    bla "Before you can even process what’s happening, you're dragged to the gallows. A rough rope tightens around your neck as you're forced onto a small stool, balancing on your tiptoes." with dis12
    gua2 "Heh. You finally get what you deserve, human." 
    ara "Everyone, get to your posts!"
    show qqi 17
    mc "T-This is a mistake..." with dis12
    mc "A big one!"with hpunch 
    mc "I didn't do it!"
    mc "F-Fuck, I didn't even want to come here in the first place!"
    mc "I was teleported into this mess!"
    show qqi 16
    gua2 "The human touched the Princess, almost killed her, and still dares to claim innocence. Can you believe it?"
    gua "Huh, I guess it is true what they say about them..."
    mct "What the fuck is going on?!"
    mct "Lorelei said I still had three days!"
    show qqi 18
    mct "And how could that old man change his opinion so f–" with dis
    show qqi 19
    syl "*Chuckles* Mm-hm."
    show qqi 20 with dis
    pause .3
    show qqi 19 with dis
    pause
    show qqi 21
    mc "*Gritting his teeth* You cocksucker..."
    mcsc "This is your doing, isn't it?!" with hpunch 
    mcsc "I'm gonna fucking kill you!" with hpunch 
    show qqi 22
    syl "Shall we begin, Lord Thorund?"
    syl "I must insist that we proceed swiftly, as I long to return to my castle and the Princess, so that my... druids can attend to her wounds without delay."
    show qqi 23
    tho "Ah... of course, Lord Sylax." 
    tho "I also have matters to attend to."
    show qqi 24
    tho "*Clears throat* Attention, please." with dis15
    tho "I want to give you all a brief reminder."
    show qqi 24b
    tho "As was conveyed yesterday, it is imperative that all present here maintain the utmost discretion regarding this matter."
    tho "Word of the human’s presence must not reach the other parts of the realm, as it could further destabilize our already fragile diplomatic efforts."
    show qqi 24
    tho "I trust you will all uphold your oaths in this regard."
    show qqi 27b
    ara "Absolutely, my Lord."
    ara "I trust my men unconditionally. Not a word about the human shall escape their lips."
    show qqi 24
    tho "Very well."
    show qqi 24b
    tho "Now, regarding the sentence..."
    tho "After extended deliberation with the other regents, we have come to a unanimous conclusion."
    show qqi 18
    tho "By the decree of this Council, the defendant stands condemned of the grievous crimes he was accused of."
    tho "The abduction of Princess Calypso, the defilement of her sacred form, the infliction of harm upon her, and the attempt to destabilize our realm."
    tho "The sentence... is death."
    show qqi 25
    mc "Are you fucking kidding me?!" with hpunch 
    mc "Are you all mad?! Not even 24 hours have passed!"
    mc "And you haven't even listened to the Princess' testimony yet!"
    mc "I'm innocent!" with hpunch
    play sound armor
    play sound2 wood2
    show qqi 28
    bla "One of the guards puts his foot on the stool." with dis17
    mc "Wait, wait, wait!"
    mc "Don't do it or you'll regret it, bud!"
    show qqi 30
    gua2 "Regret it? Why would I?"with dis12
    show qqi 29
    mc "What do you mean, why?!"
    mc "The Princess would be FURIOUS!"
    show qqi 30
    gua2 "Why would she?"
    gua2 "We're just following the law."
    show qqi 29
    mc "I-I don't know about your damn laws, but someone would pay for it!"
    mc "I fucking assure you, you'd all regret it BIG TIME!"
    show qqi 30
    gua2 "You will serve as a reminder that no one defies Hyril'ar, you filthy human."
    gua2 "*Whispering* Soon, Lord Sylax will rule as the sole regent and restore this realm to its former glory."
    gua2 "*Whispering* The age of shame... is over."
    show qqi 26
    gua2 "At your command, General." with dis12
    ara "Hmph."
    ara ". . ."
    show qqi 24
    tho "General?"
    tho "Is there a problem?"
    show qqi 26
    ara ". . ."
    show qqi 27
    ara "*Sighs* Remove the stool."
    show qqi 28
    mct "No, no, no, no, no..." with dis15
    mct "I can't die here... not after everything I've been through!"
    mct "I need to do something..."
    mct "I need to activate my powers... I need to..."
    gua2 "*Laughs* Goodbye, human."
    scene qqi28
    play sound risingshort2b
    pause 5.5
    play sound2 stoolkick
    play sound6 sworddrop
    stop music
    stop soundloop2
    scene black with prfast
    pause
    play soundloop2 birds fadein 5
    play sound3 wind4 volume 0.4 fadein 3
    scene qqi 31 with dis25
    pause
    scene qqi 32
    mc "Hmm?" with dis
    play soundlow rope volume 0.6
    scene qqi 33
    mc "Huh...?" with dis12
    scene qqi 34
    mc "What...?"
    mc ". . ."
    mc "G-Guys?"
    mc "Have we suddenly started to listen to reason...?"
    scene qqi 35
    mc "*Looking around* Huh...?" with dis12
    mc "What's going on...?"
    ara "You honor us, my Lady."
    mc "Eh...?"
    play sound7 wind4 volume 0.5
    play music mastermind2
    scene calypsosick with dis22
    pause 11.5
    play soundlow clothes3
    play sound6 leathershort volume 0.3 fadein 1
    scene qqi 35b
    tho "*Bowing down* Your Highness..." with dis12
    tho "You... grace us with your presence."
    syl "*Whispers* Lady Calypso..."
    scene qqi 37
    mc "Your... Highness??"with dis 
    mc "W-Wait... does that mean what I think it means?!"
    show qqi 40
    mc "Calypso!" with dis15
    show qqi 38
    ca "What is the meaning of this, Thorund...?" with dis08
    show qqi 39
    ca "Explain yourself." with dis08
    show qqi 41
    tho "W-We..."
    tho "The human abducted you. He... laid hands upon you."
    tho "Y-You know well that our laws decree such actions must be met with–"
    show qqi 39
    ca "What...?"
    ca "That {i}human{/i}... saved my life."
    show qqi 42
    syl "What?!"
    show qqi 39
    ca "He freed me from an imprisonment that spanned years... while you all stood idly by, seemingly content to wait and do nothing."
    show qqi 40
    tho "B-But–"
    show qqi 39
    ca "And then, upon my return, it is my own maid who acts to hasten my convalescence, because your druids were too afraid to administer proper medicine?"
    ca "Perhaps it is you all who are deserving of punishment."
    show qqi 41
    tho "W-We dispatched hundreds of warriors in search of you, Princess."
    tho "We did all we co–"
    show qqi 39
    ca "You sent hundreds of men to search for me..."
    ca "And now you would slay the only one who succeeded?"
    show qqi 41
    tho "But... he is... a human, my Princess."
    tho "Even if he did find you, you know well that even an elf would face exile merely for laying a hand upon you."
    tho "As for a human, the punishment is... death."
    show qqi 35
    ara "I am deeply sorry, my Princess." with dis
    ara "I shall accept whatever punishment you deem just for me and my men."
    show qqi 38
    ca "You and your men merely followed orders, General."
    ca "You served the realm as was your duty."
    show qqi 39
    ca "But you..."with dis08
    ca "Is this what my kingdom has become?"
    ca "Do we now execute without trial? Have we become no better than those inferior races we condemn?"
    ca "What if he possessed knowledge of value about me or my disappearance?"
    show qqi 43
    syl "I advised that we torture him for information, my Princess, but Lord Thorund refused. All to uphold foolish and antiquated traditions."
    syl "I should have taken matters into my own han–"
    show qqi 39
    ca "Silence."with hpunchsubtle
    ca "I have heard enough."
    show qqi 38
    ca "Release the human at once... and send him to my chambers." with dis08
    ca "He shall serve as my... personal bodyguard from now on."
    show qqi 42
    syl "What?!"
    syl "But that is... utterly inadmissible!"
    syl "A human cannot be permitted to be so near the Princess of Hyril'ar!" with hpunch
    syl "Let alone hold a place amongst the members of the court!" with hpunch
    show qqi 39
    ca "I said... release him."
    show qqi 43
    syl "NO! He deserves punishment!" with hpunch 
    syl "We have shown weakness for far too long! What will our enemies think?"with hpunch 
    show qqi 39
    ca "Are you... questioning my command, Sylax?"
    show qqi 42
    syl "I... I would never..." with dis
    syl "I do not..."
    syl ". . ."
    play sound leathershort volume 0.3 fadein 1
    play sound2 clothes3
    show qqi 44
    syl "*Bowing down* . . ." with dis17
    show qqi 45
    syl "I would never dare... my Princess."
    syl "Please, forgive my audacity."
    show qqi 44
    ca "So I thought."
    show qqi 39
    ca "Now..." with dis12 
    ca "Ensure the human is safeguarded immediately, and–" 
    play sound3 ["<silence 0.3>", bodycollide2]
    play sound4 clothes3
    play sound5 rubbody
    show qqi 45b
    bla "Calypso staggers and collapses into one of the pillars." with dis15
    ca "*Heavy breathing* Aagh..."
    lo "Lady Calypso!" with hpunchsubtle
    lo2 "You must go back to bed! You have not yet recovered!"
    ca "*Heavy breathing* Y-Yes..."
    ca "*Heavy breathing* I just require... some more rest..."
    ca "*Heavy breathing* I will be well."
    lo "Come, my Lady. You need to drink more of your medicine."
    ca "*Heavy breathing* Yes..."
    play sound6 clothes3
    scene qqi 45c
    ca "*Composing herself* Release the human." with dis15
    ca "We shall withdraw to Iskhaldrim until I have regained my strength — we are too near the border as it stands."
    ca "He shall accompany me, alongside a personally vetted contingent of guards."
    ca "And... an emergency council shall be convened at the fortress in four days' time, once I have fully recovered."
    ca "Is everything clear?"
    play soundlow clothes3
    play sound6 leathershort volume 0.3 fadein 1
    scene qqi 45d
    tho "*Bowing down* Without question, your Highness." with dis12
    tho "We shall also begin preparations for a grand banquet in the capital to commemorate your return."
    syl ". . ."
    scene qqi 46
    tho "You heard the Princess!" with dis
    tho "Release the human, and make preparations to depart for Iskhaldrim!"
    tho "There is no time to lose! Move swiftly!"
    guards "Yes, my Lord!" with hpunch
    stop music fadeout 11
    play sound2 rope
    play sound3 rope2
    play soundlow chairmove
    scene qqi 47 with dis25
    play sound chair2
    bla "As Calypso steps back into the building, the guards untie the rope around your neck, and quickly start making the necessary preparations to depart." with dis2
    mc "*Coughing* (Fucking hell... this is gonna leave a mark.)"
    mc "G-God..."
    mct "I'm getting way too familiar with near-death experiences."
    mct "One day I'll stop being so lucky..."
    play sound stairswood2 fadein 1
    play soundlow wood2
    play sound4 horsewalk
    play sound5 armor
    scene qqi 48 with dis22
    play music2 hyrilarhappy fadein 6
    play sound8 horse
    mc "*Walking down the stairs* So..." with dis14
    gua2 "Put the sacks on the cart!" 
    gua "Get the horses saddled!"
    mc "Damn... you sure don't like to waste any time around here." 
    mc "Guess we're going somewhere else now...?"
    show qqi 49
    ara "Indeed."
    ara "We are retreating to the Usurper's fortress as per the Princess' command. It is an old human keep, so... you may find it somewhat familiar."
    ara "There, we shall await her recovery and further instructions."
    show qqi 48
    mc "Can I see the Princess before we go?"
    show qqi 49
    ara "She will be transported in a separate carriage. I am afraid you will not be able to see her until we arrive."
    show qqi 48
    mc "Ah, obviously..."
    show qqi 49
    ara "But fear not, once we reach our destination, you will be free to depart at your discretion."
    ara "Unless the Princess states otherwise, of course."
    show qqi 48
    mc "I see..."
    mct "Hmm, well, it's not like I have anywhere to go until I figure out how to get back to Earth or regain my powers."
    if calypsopath and calypsotogether:
        mct "At least now Calypso is awake. I'm relieved to see she's alright."
    else:
        mct "At least now Calypso is awake. Hope she can still use her portals."
    mc "Alright then... let's get moving."
    mc "How far away is it?"
    show qqi 49
    ara "Roughly twelve hours by carriage."
    ara "We should arrive shortly after sunset."
    show qqi 48
    mc "Jesus Christ, twelve hours on a wagon..."
    show qqi 49
    ara "Before we depart, however..."
    ara "I want to apologize, on behalf of myself and my men."
    ara "It is clear now that you spoke the truth, and... the Princess seems to value you. For reasons I cannot yet comprehend."
    ara "So... I am sorry for our behavior."
    scene qqi 48
    menu:
        with dis
        "[gr]Accept his apology":
            $ arannisfriend = True
            mc "Wow. I... didn't expect that."with dis
            mc "I... accept your apology, General. I suppose."
            mc "We good."
            show qqi 49
            ara "Thank you, human."
            show qqi 48
            mc "You can call me [mc]."
            mc "Or... [nickname]."
            show qqi 49
            ara "[nickname]..."
            ara "Very well, Lord [nickname]."
        "Don't accept his apology":
            mc "Yeah, no."with dis
            mc "You treated me like garbage and you even tried to fucking kill me."
            mc "You can shove your apologies up your ass."
            ara "Hmph."
            scene qqi 49
            ara "I cannot say I am surprised by a human holding a grudge."
            ara "Very well, then..."
    ara "Please, take a seat on the cart. We will depart immediately."
    play sound footsteps3
    play sound2 armor
    scene qqi 50 with dis17
    ara "Attention!" with dis15
    ara "Finish packing everything up and mount your horses!"
    ara "Isilion, Eoindone, Darra, and Vyrndalor will accompany the human and me."
    ara "Everyone else will escort the Princess!"
    show qqi 51
    guards "YES, SIR!" with dis15
    mct "And... here comes another twelve hours surrounded by sweaty dudes. And these ones even hate my whole race."
    mct "Hmph..."
    mct "At least it's better than staying in that dungeon, I guess."
    mct "Though... barely."
    scene qqi 52
    mc "*Sighs* (But this also means at least one or two more days without being able to get back to Kredon.)" with dis17
    mct "To be fair, I'm worried about the girls, but..."
    mct "If there's one thing I can be grateful for, it's that they're all smarter than anyone I know. Plus, they’ve got Chang and Mr. Hernandez to rely on."
    mct "They don't need me. I'm sure they're all fine."
    mc "*Sighs* (Just a little longer...)"
    stop music2 fadeout 6
    scene black with dis3
    stop soundloop2 fadeout 7
    if novapath and anniepath:
        show screen meanwhile with dis17
        pause 
    else:
        jump hyrilarpostskip
    play soundloop rain3 fadein 6
    scene qqi 53
    hide screen meanwhile
    with dis3
    pause 
    play sound knock2
    san "*Knocking* Sweetie? Are you there?" with dis
    no "*Mumbling* So if this function’s recursive call skips the null check..."
    no "*Mumbling* No, no, that doesn’t fit..."
    play sound2 knock2
    san "*Knocking again* Honey...?"
    no "*Mumbling* Unless... wait... what if the memory leak’s not even here?"
    play sound dooropen2
    scene qqi 54 with dis
    san "Nova!" with dis08
    san "Are you deaf? I'm calling you!"
    scene qqi 55
    no "*Mumbling* That doesn't make any sense, but..."
    no "*Mumbling* There's gotta be something with these numbers..."
    no "*Mumbling* The numbers... what do they even mean??"
    show qqi 54
    san "Nova! Your friend Annie's here!"
    san "She says you guys were supposed to meet?"
    show qqi 55b
    no "Annie...?"
    show qqi 55
    no "Oh! Yeah, yeah! Of course, tell her to come in." with dis12
    no "Hmmm..."
    no "*Mumbling* What if they aren't numbers but they are binary code...?"
    show qqi 56
    san ". . ."
    show qqi 54
    san "*Sighs* Alright."
    play music rainymorning fadein 4
    play sound2 footsteps2
    scene qqi 57 with dis2
    san "Well... I guess you can come in, darling — she's in her room."with dis15
    san "I'm really glad you stopped by. After the last few days... she could use some positivity."
    show qqi 58
    san "Hopefully some laughs with her friends will help lift her spir—"with dis
    play sound7 impact3
    play sound6 impact3
    play soundloop depression 
    stop music
    show anniedepressed
    pause
    scene qqi 59
    san ". . ."
    show qqi 60
    san "Um..."with dis08
    san "A-Are you okay, sweetie?"
    show anniedepressedb
    a "Our..."
    a "Our friend disappeared."
    a "[mc]."
    scene qqi 60
    san "Y-Yeah... Nova told me about it. I'm so sorry, sweetie."
    san "But I'm sure you'll find him soon enough!"
    san "She mentioned he sometimes plays Eternum for hours on end, right? Or maybe he just went to visit some family for a few days!"
    show anniedepressedb
    a "His only family is a drunk skunk of a father living an ocean away."
    a "And Eternum is basically an infinite, borderless playground filled with players and monsters wanting to hurt him."
    scene qqi 60
    san "W-Well..."
    san "I suppose there's not much you can do right now, then."
    san "Just try to keep yourself busy and let the police handle it."
    show anniedepressedb
    a "The police..."
    a "They can't do anything in Eternum."
    a "The Praetorians rule there. And they're... our enemies too."
    scene qqi 60
    san "A-Ah..."
    san "Yeah, well..."
    san "A-Anyway, have fun with Nova!"
    show anniedepressed 
    san "If you need anything, I-I'll be in the living room!"
    a "Mmh."
    stop soundloop fadeout 9
    play soundloop2 rain3 fadein 5
    scene qqi 61 with dis25
    pause
    play sound footsteps
    scene qqi 62
    a "*Sighs* Hey, Nova..." with dis22
    a "Sorry I'm late, I didn't sleep too well last night."
    show qqi 55
    no "Wait a second..."
    no "It's not December 1st..."
    play sound chair1
    play sound2 clotheswhoosh
    show qqi 62b
    no "It's January 12th!" with vpunchslow
    no "How did I not see that?!"
    show qqi 63
    a ". . ."
    show qqi 64
    a ". . ." with dis08
    play music quirky09 fadein 5
    $ renpy.music.set_volume(0.4, delay=17.0, channel='soundloop2')
    scene qqi 65 with dis15
    pause
    scene qqi 66
    a "Erm..." with dis15
    a "What is this...?"
    play sound chair1
    play sound2 clotheswhoosh
    scene qqi67
    no "I've cracked it! At last!" with hpunch
    no "I know where [mc] is!" with hpunchsubtle
    no "HE'S IN HYRIL'AR!" with hpunchsubtle
    scene qqi 66
    a "Um..."
    a "When's the last time you got some sleep?"
    scene qqi 68
    no "I had four hours like... last Tuesday or so, I don't know—LISTEN! I finally figured out what we were missing!"
    no "Chad uses the DD-MM-YYYY date format!" with hpunchsubtle
    show qqi 66
    a "Chad...? Who's Chad?"
    a "Like... the meme?"
    show qqi 68
    no "The country in Africa!"with hpunchsubtle
    no "It used to be a French colony!" with hpunchsubtle
    show qqi 64
    a ". . ."
    show qqi 64b
    a "W-What the hell are you talking about...?"
    play sound chair1
    play sound2 clotheswhoosh
    show qqi69
    no "Oh come on, how are you not seeing it?!" with hpunch 
    no "It's so obvious! Right there!" with hpunch 
    play sound w1
    scene bboard1
    no "[mc] goes missing on the 10th, yeah?!" with pl
    a "Yeah..."
    no "Now, the problem is we've been wasting WAY too much time assuming our usual suspects are behind it!"
    play sound2 w1
    scene bboard2
    no "The Founder?!" 
    play sound w1
    scene bboard3
    no "William “huge-ass forehead” Bardot?!" 
    play sound w1
    scene bboard4
    no "Thanatos?!"
    a "Is that a Yu-Gi-Oh card...?"
    no "Yeah, I don't exactly have pictures of the guy, but you get the point! LISTEN!"
    no "Why is Thanatos so obsessed with Calypso?!"
    play sound w1
    scene bboard5
    no "And what's his connection to William?"
    a "What? Since when were those two even connected?"
    no "EXACTLY!"
    a "Exactly what...?"
    play sound w1
    scene bboard6
    no "Is Alex an undercover agent working for her dad?"
    a "Alex?!" 
    play sound w1
    scene bboard7
    no "Or maybe Penny's been playing us this whole time? Like, why else would she hang out with us nerds, huh?" 
    a "What?? Why wouldn't she...?"
    no "Exactly!"
    a "Exactly what?!" with hpunch 
    no "Look who she's been spending more time with!"
    play sound w1
    scene bboard7b
    no "First, her sister. Oh, what a {i}coincidence{/i}, the last person to see [mc]."
    play sound w1
    scene bboard8
    no "Then Luna! I've seen enough anime to distrust red eyes..."
    no "And what is she hiding behind those gloves and bangs?!"
    no "Kinda weird you've never seen her without them, don't you think??"
    if lunapath and anniepath:
        a "I... did, actually. The gloves at least. At the cafe." 
    play sound w1
    scene bboard9
    no "And Penny's other best friend?" 
    no "Delilah Warren!"
    a "YOU are Delilah Warren!"
    no "Yeah! Exactly! Almost too convenient, wouldn't you say??"
    no "And what's behind all these {i}coincidences{/i}?!"
    play sound w1
    play sound2 impact5 volume 0.5
    scene bboard10
    no "CALYPSO! Ulysses' Third Weapon of Atlas!" 
    no "The piece of the puzzle that began this chaotic spiral, and, oh! Surprise, surprise! Last person seen with [mc]!"
    no "Almost like she orchestrated all these “coincidences” to distract us from the real goal..."
    no "To keep us from following her to the place she's been hyped about since we met her..."
    play sound w1
    play sound2 impact5 volume 0.5
    scene bboard11
    no "HYRIL'AR!" 
    no "Or perhaps I should say..."
    play sound w1
    scene bboardh
    no "HIGHLY." 
    play sound w1
    scene bboardy
    no "YIELDING." 
    play sound w1
    scene bboardr
    no "REALITY." 
    play sound w1
    scene bboardi
    no "INTEGRATED." 
    play sound w1
    scene bboardl
    no "LIFELIKE." 
    play sound w1
    scene bboarda
    no "AUGMENTED." 
    play sound w1
    scene bboardr2
    no "REALM!" 
    play sound w1
    play sound2 impact5 volume 0.5
    scene bboardhback
    no "BOOM!"
    no "Eternum's core server! Hidden in plain sight!"with hpunchsubtle
    no "Can you believe it?!" with hpunchsubtle
    show qqi 64b
    a "I... I'm not sure I'm following."
    scene qqi 67
    no "Then, I started thinking... these people LOVE hiding clues just to mess with us. So I thought, what if I apply a simple alphabetical cipher?"
    no "You know, A equals 1, B equals 2, and so on?" 
    show qqi 64b
    a "Eh...?"
    scene bboardhy
    no "Oh, you're not gonna believe it..."
    play sound w1
    scene bboardh
    no "8!" 
    play sound w1
    scene bboardy
    no "25!" 
    play sound w1
    scene bboardr
    no "18!" 
    play sound w1
    scene bboardi
    no "9!" 
    play sound w1
    scene bboardl
    no "12!" 
    play sound w1
    scene bboarda
    no "1!" 
    play sound w1
    scene bboardr2
    no "18!" 
    play sound w1
    play sound2 impact5 volume 0.5
    scene bboardfinal
    no "BOOM!" 
    no "8.25N, 18.9E, 12th of January at 18:00!!!" with hpunch 
    a ". . ."
    scene qqi 64b
    a "And... those coordinates lead to...?"with dis15
    scene qqi 67
    no "Just off the coast of Lake Chad in Central Africa!"
    no "And oh surprise! Guess who has an unregistered LLC and a branch office & production plant in southern Chad?! Yep, yep! ULYSSES!" 
    show qqi 66
    a "Uh..."
    a "I don't know, Nova."
    show qqi 68
    no "What do you mean, you don't know?"with hpunch 
    no "We just have to travel to Africa within the next three weeks!"
    show qqi 66
    a "I..."
    a "I just..."
    a "I d-don't think Calypso took [mc] to Africa."
    play sound chair1
    show qqi 69
    no "What?! But look! All the clues are there!" with hpunch 
    scene qqi 64
    a ". . ."
    scene qqi 69
    no "B-But..."
    no "Well, if he's not there, then where is he?!" with hpunchsubtle
    no "TELL ME!" with hpunchsubtle
    stop music fadeout 10
    play music2 sad09 fadein 8
    play soundlow thunder fadein 3
    scene qqi 71
    bla "Overwhelmed by emotions, Annie wraps her arms around herself as her eyes begin to glisten with tears for the umpteenth time this week." with dis22
    show qqi 73
    a "I..."
    a "I-I don't know where he is, Nova."
    show qqi 72
    no "Wait, wait, wait... why the hell are you crying now??" with dis12
    no "I-It's okay! I'll find him!"
    no "I'll keep hacking other databases! I'll keep..."
    no "I-I will..."
    show qqi 73
    a "I don't know where he is..."
    a "I just know that... it's been so many days already."
    a "And I don't..."
    show qqi 72
    no "But we're gonna find him! It's just a matter of time!"
    no "I don't understand why you're crying."
    show qqi 73
    a "You're also crying."
    show qqi 72
    no "Yeah, because {i}you're{/i} crying!"
    no "You're crying for no reason, so you're making me cry!"
    show qqi 73
    a "It's just..."
    a "W-What if..."
    play sound chair2
    show qqi 74
    no "*Standing up* No! Didn't you hear Nancy?!" with dis12
    no "NO “WHAT IFS”!"
    show qqi 75
    a "*Sobs* I..."
    a "I just..."
    a "I can't live without him, Nova."
    a "It would kill me."
    show qqi 74
    no "Do you think I can?!"
    no "I can’t go back to my life without him, I... I just can't!"
    no "And we won't! It's just a matter of time before he turns up!"
    no "We'll find him! W-We have to!"
    show qqi 75
    a "But what if we don't?!"
    a "What if he..."
    show qqi 74
    no "WHAT?!"with hpunchsubtle
    no "What if he WHAT?!"with hpunchsubtle
    show qqi 75
    a "What if he DIED?!"with hpunch
    a "WHAT IF THANATOS KILLED HIM?!"with hpunch
    a "WHAT IF WILLIAM BARDOT OR THE FOUNDER GOT TO HIM?!"with hpunch
    show qqi 74
    no ". . ."
    no "...What?"
    play sound2 clothes3
    show qqi 76
    no "*Leaning on the wall* . . ." with dis14
    no "But that's..."
    no "That's impossible. People don't just... die like that."
    play sound clothes3
    play sound3 couch
    scene qqi 77
    a "*Crying* M-Maybe we..." with dis12
    a "*Crying* We risked too much, maybe we..."
    show qqi 76
    no "H-He can't just be gone."
    no "Not when we just started our journey together."
    show qqi 77
    a "*Crying* T-There's still so much we have to do."
    a "*Crying* So much to..."
    show qqi 76
    no "*Crying* He can't..."
    play sound thunder fadein 2
    stop music2 fadeout 6
    l "He's okay."
    show qqi 78
    no ". . ." with dis15
    show qqi 79
    no ". . ."
    no "L-Luna?"
    show qqi 80
    l "He's alright."
    l "And he'll be back with us soon."
    show qqi 81
    a "*Sniffling* What...?"
    a "How do you know?"
    show qqi 80
    l "[mc]'s strong and really smart."
    l "I know he's okay."
    show qqi 78
    no "How can you be so sure...?"
    show qqi 80b
    l "I... just know it."
    show qqi 80
    l "He'd never just disappear like this."
    l "He... would never leave us hanging."
    if lunapath:
        show qqi 80b
        l "He..."
        l "He promised me."
    show qqi 78
    no ". . ."
    show qqi 81
    a ". . ."
    show qqi 82
    a "*Wiping her tears* Y-Yeah, you're right."with dis14
    a "H-He’d be so mad if he knew we're doubting him."
    show qqi 79
    no "*Clears throat* Y-Yeah! Totally!"
    no "So true!"
    no "*Laughs nervously* Ugh, sorry, I-I don't know what happened to me. I think my period's coming or something."
    show qqi 82
    a "*Chuckle* Yeah, maybe mine too."
    a "Thank you, Luny!"
    a "Seriously, you can’t leave me and Nova alone together. We’ll just spiral into a negativity black hole."
    show qqi 79
    no "*Chuckles* For real! We need your positive energy, Luna!"
    show qqi 80
    l "Don't mention it, girls."
    play sound chair2
    scene qqi 82b
    no "Alright, ladies!" with dis17
    no "We got to de-stress, now back to finding Waldo!"
    no "LET'S GO!"with hpunch 
    if lunapath:
        scene qqi 83
    else:
        scene qqi 79
    a "Okay, but that theory of yours about him being in Africa LITERALLY makes no sense!" with dis2
    no "Yeah, I might've gotten a little carried away with that one..."
    a "Have we thought about the possibility he's being held by the remnants of the ERE? Maybe we should check the Semper Invicta server."
    no "Oh... that's a good guess!"
    a "Let's come up with a new plan!"
    no "YEAH!"
    play soundlow thunder fadein 2
    stop soundloop fadeout 7
    jump hyrilarpostskip  


label hyrilarpostskip:
    stop music2 fadeout 6
    scene black with dis3
    stop soundloop2 fadeout 7
    show screen coupledays with dis3
    pause 
    play soundloop3 birds fadein 4
    hide screen coupledays 
    scene qh 1 
    with dis3
    pause 
    scene qh 2
    mc "Hmmm..." with dis2
    play sound transformpower
    scene qh 3 with dis14
    show qh 2 with dis17
    mct "Dammit..." with dis08
    play sound transformpower
    scene qh 3 with dis14
    show qh 2 with dis17
    mct "I still can't hold my transformation for more than a second." with dis08
    mct "Yeah, I'm making progress, slowly getting my powers back, but damn..."
    show qh 4
    mc "*Sighs* (It's so damn frustrating too.)" with dis
    mct "It feels like being in bed with a girl and not being able to get it up."
    play sound2 knock2
    show qh 5
    mc "Hmm?" with dis12
    mc "Yeah?"
    if arannisfriend:
        ara "Lord [mc]?"
    else:
        ara "Human?"
    ara "It is time for your training."
    show qh 4
    mc "Oh god..." with dis
    mc "Can we rest today, General?"
    mc "I'm starting to think all this training is doing more harm than good."
    mc "My whole body still aches from yesterday's sparring..."
    ara "You insisted yourself that I hold you to your word — that I ensure you train daily until your innate magical capabilities are restored."
    mc "Yeah... I did say that."
    mc "*Mumbling* Maybe one day I'll learn to keep my damn mouth shut..."
    if arannisfriend:
        ara "May I come in?"
    else:
        ara "I will come in."
    mc "Sure, it's open..."
    play sound dooropenclose
    scene qh 6 with dis17
    mc "Can we at least take it easier today?" with dis12
    mc "Or... we could wear armor this time. Y’know, so the hits don’t feel like getting slammed by a carriage."
    ca "Our encounter with that demon clearly took a toll on you, [mc]."
    ca "Your mood is... certainly deplorable."
    scene qh 7
    mc "Huh...?" with dis
    mc "C-Ca..."
    mc "Calypso?!" with hpunch 
    menu:
        with dis 
        "Hug her [calypso_pts]":
            $ calypso_points += 1
            $ calypsofirsthug = True
            stop soundloop3 fadeout 10
            play music hyrilarchill volume 0.8
            play sound clotheswhoosh
            play sound2 couch
            play sound3 debris3
            scene qh7b
            bla "You jump out of the bed and wrap up the Princess in your arms." with hpunch
            scene qh 9
            mc "Thank god you're okay!" with dis14
            mc "I thought I'd never see you again!"
            if calypsopath and calypsotogether:
                ca ". . ."
                show qh 10 with dis
                pause 
                show qh 9 with dis
                pause
                show qh 11 
                ca ". . ." with dis14
                play soundlow clothes3
                show qh 12
                ca ". . ." with dis15
                play sound knock2 
                ara "Is all well, my Lady?"
                ca "Hmm–"
                play sound2 whoosh6
                play sound3 slap1 volume 0.5
                scene qh 13
                ca "A-Ahh–yes, all is well, General." with hpunch
            else:
                play sound2 whoosh6
                play sound3 slap1 volume 0.5
                scene qh 13
                ca "W-What in heavens is wrong with you?!" with hpunch
                show qh 14
                ara "Is there any problem, my Lady?"
                show qh 13
                ca "A-Ahh–no, all is well, General."
            ca "You may go ahead, we shall join you shortly."
            show qh 14
            ara "But... but it is unwise for you to go unguarded beyond the palace walls."
            show qh 13
            ca "It will be but a brief moment, Arannis. I just need to discuss something with... um... the... human."
            ca "You can wait for us at the crossroad with Lorelei."
            show qh 14
            ara "Hmm."
            ara "As you wish, my Lady."
            ca ". . ."
            play sound clothes3
            show qh 15
            ca "*Taking a step back* B-By the grace of the Ancients, [mc]..." with dis17
            ca "Did your time in the dungeons teach you nothing?"
            if calypsopath and calypsotogether:
                ca "You must not touch me in this place. Especially whilst you are... h-half naked as you are now."
            else:
                ca "Do not touch me ever again. Not alone, not in the presence of others."
            ca "They could hang you for it. Again."
            show qh 16
            mc "Y-Yeah, sorry about that. My bad."
            mc "I'm kind of a hugger, and..."
            mc "Well, I was so surprised to see you that I forgot where I was for a moment."
            mc "Everyone has been keeping me in the dark about you."
            show qh 17
            ca "Well, you are fortunate, then." with dis
        "Don't hug her":
            play music hyrilarchill fadein 4 volume 0.8
            play sound clothes3
            play sound2 couch
            scene qh 18
            mc "*Standing up* OH MY GOD! You're okay!" with dis12
            stop soundloop3 fadeout 10
            scene qh 17
            ca "Naturally. It would take far more than that to bring me down."
            ca "I merely required... a moment of rest."
            show qh 18
            mc "I swear, I'd hug you if it didn't risk going back to the gallows!"
            show qh 17
            ca "*Chuckle* I see you are quick to learn. That is commendable."
    ca "I already informed Lord Arannis that I would be accompanying you during today's training, so... consider this your opportunity to ask whatever questions you have."
    ca "I am well aware that he likely dismissed any inquiry not pertaining strictly to combat."
    show qh 18
    mc "*Chuckles* He certainly did. He guards words like they're sacred scrolls."
label cahymelabel:
    show qh 18
    menu:
        with dis
        "How's Lorelei?" if cahyme1:
            $ cahyme1 = False
            $ cahyme6 = True
            mc "How's Lorelei? I haven’t seen her since she visited me down in the dungeon!" with dis08
            if cahyme4:
                $ cahymetoolate = True
                show qh 17
                ca "Ah, Lorelei..."
                show qh 15
                ca "It is rather unflattering that you express more concern for my maid than for me. But... very well." with dis
                show qh 16
                mc "I-I mean... I can already see you're fine!"
                mc "I just..."
                ca "Mmph."
                show qh 15
                ca "She is doing well. She found an ancient herb in the forest to wake me from my slumber — one long forbidden by our clerics due to its ties to the dark arts."
                ca "Although... she was granted a royal pardon by the Princess, naturally."
                show qh 16
                mc "A-Ah, that's great! Good for her!"
                show qh 17
                ca "She has always had a curious fascination with humans and other mythical folk, so she will be joining us today as well." with dis
            else:
                show qh 17
                ca "She is doing well."
                ca "She found an ancient herb in the forest to wake me from my slumber — one long forbidden by our clerics due to its ties to the dark arts."
                ca "Naturally, she was granted a royal pardon by the Princess of the realm."
                show qh 18
                mc "That's great to hear! I probably wouldn't be here if it wasn't for her."
                show qh 17
                ca "You will be able to properly thank her yourself."
                ca "She has always had a curious fascination with humans and other mythical folk, so she will be joining us today as well."
            show qh 18
            mc "I wonder if I should feel flattered or offended by that..."
            jump cahymelabel
        "Are you alright? [gr][mt](1st)" if cahyme4 or cahymetoolate:
            $ cahyme4 = False
            $ cahyme6 = True
            mc "So... how are you?!" with dis08
            mc "Are you recovered?! They told me you were out cold for days!"
            if cahymetoolate:
                $ cahymetoolate = False
                show qh 15
                ca "Too late." with dis
                show qh 16
                mc "*Chuckles* Had to try."
                mct "There’s always something oddly charming about seeing her annoyed like any other girl."
                mct "It kinda makes things feel... normal."
                mc "Forgive me, my Princess. I meant no offense to you, I swear."
                show qh 18
                ca "Hmph." with dis
                show qh 17
                ca "That is better."
                jump cahymelabel
            show qh 17 
            ca "I am well, thank you."
            $ calypso_points += 1
            show qh 19
            ca "After our battle with Thanatos, I lost consciousness — likely the result of pushing my body far beyond its limits." with dis12
            ca "The next thing I recall was awakening to Lorelei informing me that you were about to be hanged."
            ca "I was still weak then, but my strength has been steadily returning. With each passing hour, I feel more power flowing back into me."
            show qh 20
            mc "I'm so relieved to hear that! It's really good to see you up again, I really was worried."
            mc "And... yeah, same here, actually. I’ve been feeling stronger too."
            mc "Like, a lot stronger since that day."
            mct "Almost too much of a coincidence..."
            mct "Is it possible my powers are somehow connected to Calypso’s...?"
            show qh 17
            ca "I suppose that battle drained everything from both of us, did it not?" with dis12
            show qh 18
            mc "Yeah... yeah, I guess it really did."
            jump cahymelabel
        "Where exactly are we now?" if cahyme3:
            $ cahyme3 = False
            $ cahyme6 = True
            mc "I've been wondering... where {i}are{/i} we, exactly?" with dis08
            mc "I know we made it to Hyril’ar, but after spending hours in that cart, I’m totally lost."
            show qh 17
            ca "You are still within Hyril’ar."
            ca "The kingdom stretches for many moonspans."
            show qh 18
            mc "I see..."
            show qh 19
            ca "We first arrived in Kelvhanor, near the border — known for its small villages and deep, ancient dungeons."with dis12
            ca "And from there we traveled to Iskhaldrim, where we are now."
            ca "Iskhaldrim still lies even closer to the edge of our realm than the capital, Cael’Thirien, but it is nestled within tall mountains that grant it natural protection."
            ca "It is largely isolated and more a place of passage than a destination, though."
            ca "A few temples, the palace, the Diplomacy Halls, and the Usurper’s Keep, where you've been resting, overlook the valley."
            show qh 18
            mc "Jesus... I really hope I never have to survive another trial with an elven geography quiz."with dis12
            mc "There's no way I can remember all those names."
            show qh 17
            ca "You should come back with your girls for a visit. I could grant you a royal tour across the kingdom."
            show qh 18
            mc "*Chuckles* I'm definitely taking you up on that."
            mc "A real elven medieval kingdom? Dalia's gonna {i}freak out."
            jump cahymelabel
        "I need to go back to Earth!" if cahyme5:
            $ cahyme5 = False
            $ cahyme6 = True
            mc "Okay, I've gotta ask, how do I get back to Earth?!"with dis08
            mc "I've been trying to use my ability, but it's just... not working."
            if cahyme4:
                $ cahymetoolate = True
                show qh 15
                ca "Ahh... I see your “concern” for my well-being was less about me and more about the fear of being trapped here yourself." with dis
                ca "How was it you called me again...? A {i}Tool{/i} of Atlas...?"
                show qh 16
                mc "I-I mean... I can already see you're fine!"
                mc "And I never called you that!"
                mc "I just..."
                ca "Mmph."
                show qh 19
                ca "Answering your question... yes, my magic has been returning, little by little, over the past few days." with dis12
            else:
                show qh 19
                ca "Well... my magic has been returning, little by little, over the past few days." with dis12
            ca "I would not stake my life on it just yet, but... I believe I can open a portal tomorrow. Hopefully without killing either of us in the process."
            show qh 20
            mc "Seriously?!"
            mc "Tomorrow?! That's great news!"
            mc "I was starting to think I'd be stuck here for weeks... maybe months!"
            mc "God, I don't even know how long it's been since we got here."
            show qh 19
            ca "Do keep in mind — I cannot open a portal directly to that “Earth” of yours."
            show qh 20
            mc "That's fine. If you can get me to any Eternum server, I’m sure I can make it back from there."
            mc "It's weird, but... I feel like there's some kind of barrier I can't cross here."
            show qh 17
            ca "Then it is settled." with dis12
            ca "You better ensure my safety until tomorrow."
            show qh 18
            mc "I shall defend you with my very life, my Princess."
            jump cahymelabel
        "Enough questions" if cahyme6:
            $ cahyme6 = False
            mc "Alright, no more questions!" with dis
            mc "We can go."
            if cahyme5:
                show qh 17
                ca "Excellent. If all proceeds as it should, I should be able to open a portal for you on the morrow."
                ca "So... you better ensure my safety until then."
                show qh 18
                mc "Wait... seriously?! Tomorrow?!"
                mc "That's great news!"
                ca "Mm-mh."
                mc "I shall defend you with my very life, my Princess."
                show qh 17
                ca "Good."
    if calypsopath and calypsotogether:
        show qh 21
        ca "Let us part ways here and meet again at the crossroads, just at the entrance of the valley." with dis12
        show qh 22
    else:
        show qh 17
        ca "Let us part ways here and meet again at the crossroads, just at the entrance of the valley."
        show qh 18
    mc "Huh?"
    mc "Why? We're not going together?"
    if calypsopath and calypsotogether:
        show qh 21
    else:
        show qh 17
    ca "I really prefer not to be seen alone with a human."
    ca "You would be surprised at how swiftly rumors and gossip spread throughout the realm."
    if calypsopath and calypsotogether:
        show qh 22
    else:
        show qh 18
    mc "Really? Even after I've been proven innocent?"
    if calypsopath and calypsotogether:
        show qh 21
    else:
        show qh 17
    ca "Most of us are not particularly fond of your kind, as you have surely observed."
    ca "Trust me, this is for your own good."
    show qh 22
    mc "Hmm, I understand."
    if calypsopath and calypsotogether:
        mc "What about the Princess herself, though? What's her opinion on humans?"
        ca "Hmm..."
        show qh 21
        ca "To be completely honest... I, too, once considered them to be inferior beings, unworthy of respect."
        ca "But... after spending time with one in particular, I find myself... somewhat more open-minded."
        show qh 22
        mc "Ah, must have been a truly exceptional human..."
        ca "Hmph."
        show qh 21
        ca "You could say that..."
        ca "But come now, let us not delay."
        ca "Show me what you have learned with Arannis!"
    else:
        show qh 17
        ca "Do not be late."
    show qh 22b 
    bla "Calypso leaves the room."with dis2
    mct "Man... it feels good to see her safe and sound!" 
    mct "And... did I hear that right?!" 
    mct "Tomorrow, I finally get to go back! Hell yeah!"
    mct "Can't wait to see the girls. I really hope they're all doing okay."
    mct "So... please, don't screw things up until then, [mc]."
    mct "Just be a good boy and let the hours drag by..."
    stop music fadeout 9
    play soundloop forest2 fadein 5
    play soundloop2 waterfall fadein 4
    scene qh 23 with dis33
    bla "You begin making your way towards the crossroad, taking a moment to stop and soak in the view." with dis25
    mc "Damn..." 
    mc "I’ve been staring at this side of the valley for two days now, and it still hits me like the first time."
    mc "Calypso wasn’t kidding. Her realm really is something else."
    mc "I can’t wait to come back here with the girls and actually explore it for real."
    play sound footsteps3 fadein 1 volume 0.6
    scene qh 24 with dis3
    stop soundloop2 fadeout 9
    play music2 hyrilarhappy fadein 5
    mc "Ah, there they are!" with dis12
    play sound2 footsteps3 volume 0.5
    scene qh 25 with dis2
    mc "*Nodding respectfully* General Arannis; Lady Lorelei." with dis12
    show qh 26
    if arannisfriend:
        ara "[nickname]."
    else:
        ara "Human."
    $ noflmc = mc[1:] if len(mc) > 1 else ""
    show qh 27
    lo "Good to see you, hum...um–[noflmc]!"
    show qh 25
    mc "Thank you for escorting the Princess to my chambers, General."
    mc "I was happy to see her. I'm feeling energized today because of it."
    show qh 26
    ara "It is evident the Princess harbors a... particular fondness for you."
    if arannisfriend:
        ara "While I do not approve... I shall comply, if such are Her Highness' wishes."
    else:
        ara "While I do not approve in the slightest... I shall comply, if such are Her Highness' wishes."
    show qh 25
    mc "Thank you, General."
    show qh 28
    mc "I must thank you too, Lorelei." with dis
    mc "I don't know how you pulled it off, but... you did."
    mc "You saved both the Princess’ life and mine. God bless your guts."
    show qh 29
    lo "Oh... i-it was nothing, really." with dis
    lo "I was simply... incredibly fortunate."
    lo "The herb required to prepare the concoction that awoke the Princess is not only forbidden, but also exceedingly rare."
    lo "I merely happened to walk in the right direction through the forest."
    play sound debris
    show qh 30
    ara "*Taking a step forward* Though you were granted the privilege of being in the company of both the Princess and Lady Lorelei today, certain boundaries must be established and upheld." with dis12
    ara "My daughter and Lady Calypso are, quite literally, the two most vital women in the entire realm."
    ara "Even in this secluded valley, where intrusion is nearly impossible without raising alarm, you are to remain vigilant at all times and be prepared to lay down your life for their safety, should it come to that."
    show qh 31
    mc "Absolutely, sir. I understand."
    show qh 30
    ara "Also... I feel compelled to remind you that both the Princess and my daughter remain unmarried."
    show qh 30b
    ara "Therefore, should you so much as gaze upon them improperly, initiate any form of physical contact, or even approach within an unwelcome distance, I will personally revoke your guest privileges."
    ara "Should the offense be grave enough... imprisonment or death penalty may once again become a possibility."
    ara "Understand?"
    show qh 32
    mc "*Gulps* I-I understand, sir."
    mc "No looking, no touching, no breathing too close."
    play sound footsteps3 volume 0.5
    scene qh 33
    ca "Good morning, Lorelei." with dis17
    ca "You look gorgeous today."
    show qh 34
    lo "Good morning, your Highness!" with dis12
    lo "It is truly an honor to receive such a compliment from the most beautiful woman in all the realm herself!"
    show qh 35
    ca "Please, there is no need for such pleasantries."
    ca "We have spent decades together — you are as close to me as a sister."
    play sound6 leathershort volume 0.3 fadein 1
    show qh 36
    ara "*Bowing down* Your Highness." with dis12
    show qh 37
    ara "Despite your beauty being as radiant as ever... if I may speak freely, would it not be wiser to adopt a more modest appearance?" with dis12
    ara "Your Grace’s hair is remarkably distinctive. It can be seen from a great distance."
    ara "Should danger be near, we might be easily discovered."
    show qh 38
    ca "No need to be so wary, Arannis."
    ca "We specifically came to this place so I could recover, far from any threats."
    ca "The Valley is completely secluded."
    ca "Not to mention I can alter my hair at any moment, if needed."
    show qh 40
    mc "*Turning around* Yeah, now that you mention the valley..." with dis12
    mc "This place feels quite empty, doesn't it?"
    mc "Everything’s like, immaculate, but the only people I’ve seen are a few guards and a couple of maids."
    show qh 39
    ca "Indeed... where are my soldiers, Arannis?"
    ara "Due to the recent tensions, Iskhaldrim has been largely evacuated."
    ara "The military has been repositioned toward the border, and the civilians relocated to the capital for their protection."
    ara "Moreover... our birth rates have continued to decline over the past few years. A mere dozen children have been born during Your Grace’s absence."
    ca "*Sighs* I see I shall have much to tend to once I am fully recovered."
    ara "I am afraid so, your Grace."
    mc "Hmm..."
    show qh 34
    lo "I am sure you shall restore our former glory once you have fully recovered, my Princess."with dis12
    lo "But let us not dwell on such matters now. Come, let us take a walk and savor the beauty of the day!"
    show qh 35
    ca "Well said, Lorelei."
    ca "You seem rather thrilled."
    show qh 34
    lo "I am! I want to learn more about humans!"
    lo "[mc] looks nothing like the ones depicted in Cyl'eande tapestries! No fur, and so... impressively sculpted!"
    show qh 35
    ca "Some humans {i}do{/i} resemble the ones in the tapestries... but [mc] is well above their average physique and capabilities, yes."
    ca "He is currently engaged in a fierce struggle against other leaders of his world to collect some mystical gems, which would grant him dominion over their entire kingdom."
    show qh 34
    lo "Whoa! Far more exciting than simply inheriting titles like we do!"
    lo "He must be incredibly powerful!"
    if harempath:
        show qh 35
        ca "Indeed. He even has a harem of formidable human women who assist him in his quest."
        show qh 34
        lo "Truly?? Do all human males gather harems? Like sylvansteeds and elks?"
        show qh 35
        ca "Not really, most are monogamous by nature."
        ca "[mc], however, appears to possess a magnetic pull, both physical and, I daresay, emotional, that draws multiple females to him alone."
        show qh 34
        lo "Astounding..."
        lo "And what would happen with them if he acquires all these gems and ascends as King of the Humans?"
        show qh 35
        ca "Then I imagine his companions would be crowned Queens of the Humans as well."
        show qh 34
        lo "Whoa... he really is fascinating!"
        show qh 42
        mc "Um... that was... imprecise on so many levels."with dis
        mc "It's... a bit more complicated than that."
        mc "But... n-nevermind, we have no time for this now."
    else:
        show qh 42
        mc "Um... well, can't say I'm not enjoying the compliments, even if they’re a little off, but we should get going."with dis
    play sound footsteps3 volume 0.6
    show qh 41
    if arannisfriend:
        ara "[nickname] is right." with dis17
    else:
        ara "The human is right." with dis17
    ara "Let us make our way to the temple's doors for our training today."
    if arannisfriend:
        ara "And pay attention, [nickname], I shall remind you of the key stances for parrying your opponent's strikes on the way there."
    else:
        ara "And pay attention, human, I shall remind you of the key stances for parrying your opponent's strikes on the way there."
    mc "Yes, sir!"
    stop music2 fadeout 6
    scene black with dis27
    show screen afewminuteslater with dis2
    pause
    play sound wind4 fadein 3
    hide screen afewminuteslater
    scene qh 44 
    with dis3
    bla "You all spend several minutes exchanging questions about your respective worlds, until a hidden temple suddenly comes into view." with dis17
    play music2b hyrilarmystery fadein 15 volume 0.8
    ara "We have arrived. The Temple of the Ten Rivers."
    ara "This shall be the site of your training today."
    mc "The Temple of the Ten Rivers, huh?"
    mc "Finally a name somewhat easy to remember."
    mc "Almost doesn't even sound elvish."
    show qh 46
    ca "Because it is not." with dis
    ca "The temple predates us all. It was built by a people long lost to time... before the elves, before men."
    show qh 45
    mc "Damn. That’s gotta be... what, tens of thousands of years ago?"
    show qh 46
    ca "No one can say for certain. Not even our most revered scribes."
    ca "The ancients vanished without a trace. They left this continent... and never returned."
    ca "Why they departed, or where they went... no one knows."
    show qh 47
    ara "This place has remained sealed for millennia, and we have done what we could to preserve its structure." 
    ara "Therefore, I ask you not to damage the stone in any way."
    show qh 48
    mc "Of course, sir, I will not."
    show qh 47
    ara "Then come."
    ara "Time is not our ally."
    show qh 48
    mc "Yes!"
    show qh 49 with dis25
    bla "The group approaches the temple doors." with dis15
    play sound2 footsteps3b
    show qh 52 with dis22
    play sound3 whistle3
    mc "That's one hell of a door." with dis12
    mc "How’s the wood not rotted away with all the rain and the wind?"
    ara "Whatever wood it was crafted from... it endures."
    mc "Hmm."
    show qh 53
    mc "And what’s that symbol? Painted right onto the surface. It looks... familiar." with dis12
    ara "The Ouroboros."
    ara "It is said to represent the eternal cycle."
    mc "The Ouro..."
    show qh 55
    mc "Wait... what?"with dis
    mc "The Ouroboros...?"
    show qh 54
    ara "No one knows in which faith it was born, but some say the Ancients were the first to embrace it." with dis08 
    ara "It is most often interpreted as a symbol for–"
    show qh 55
    mc "I know what it is!" with dis08 
    mc "The Ouroboros is from my world! The snake biting its own tail!"
    mc "It symbolizes... yeah, what you said. The eternal cycle. Death and rebirth!"
    show qh 56
    ara "Naturally. Humans also borrowed from the old pagan rites of the Ancients."
    show qh 55
    mc "But... you don't understand, I'm not from {i}this{/i} world."
    mc "I'm from... another... dimension. I don't know how to explain it."
    mc "This symbol has been in my world for thousands of years. Long before Eternum! Long before Ulysses existed and we created the neural implants!"
    mc "And even then, I'm pretty sure I'm the first human from where I am to set foot in Hyril'ar, like, ever."
    mc "So how can it be here too??"
    show qh 56
    ara "How can you be so certain you are the first?"
    show qh 55
    mc "Uh..."
    mc "Well... I... I guess I can't be sure."
    mc "Can we enter the temple...?"
    show qh 54
    ara "That is impossible." with dis08
    ara "The doors have been sealed for millennia. Not even elven magic could force them open now."
    show qh 55
    mc "Really?"with dis08
    mc "Why didn't you try to open it before it was too late?!"
    mc "If humans had found this place, it would’ve been cracked in a week and mapped, scanned, and turned into a damn museum by day eight!"
    show qh 56
    ara "And... that’s something you're proud of?"
    show qh 55
    mc "I mean... kinda? We're curious. Adventurous. Bold!"
    show qh 56
    ara "Reckless. Impatient. Destructive."
    show qh 55
    mc "Hmm... okay, maybe, but you have to admit — we get things done."
    show qh 56
    ara "Yet you never stop to ask yourselves whether or not they should be done."
    show qh 55
    mc ". . ."
    mc "...I guess that's fair."
    ara "Hmph."
    mc "Uh... anyway, we... um, we can begin."
    show qh 57
    ara "Good. We shall continue your sword training." with dis12
    ara "It is evident the blade speaks to you more than any other weapon, so we should try to hone it."
    play soundlow footsteps3b
    show qh 58
    mc "Yes, sir..."with dis12
    show qh 52
    mc "Hmm..." with dis12
    mct "William Bardot did mention that other humans from the past could travel to Eternum freely, not just The Founder and me."
    mct "Could some of them have made it here thousands of years ago?"
    mct "But if so... why can't I just travel back to Earth from here like it's any other world in Eternum?"
    mc "Hmmm..."
    mct "Anyway... I guess there's not much I can do about it right now. I'll have to tell the girls once I'm back."
    stop music2b fadeout 12
    play soundlow wind4 fadein 5
    scene qh 59
    lo "Your Highness, we may sit here to rest, if you please." with dis17
    lo "I realize it may be improper for one of your station to sit upon bare stone, but..."
    show qh 60
    ca "Oh, come now, Lorelei. Who do you take me for?" with dis12
    ca "I have never been afraid of getting a little dirty, unlike those pampered nobles from Cael’Thirien."
    if calypsopath and calypsotogether:
        mct "I can vouch for that..."
    show qh 61
    lo "I am glad to see your spirit unchanged, Lady Calypso."
    lo "If anything, you appear even more at ease than before."
    show qh 60
    ca "Thank you, Lorelei. I am equally pleased to see you as lively as always."
    mct "I have two lovely girls as spectators today. I better give it my all."
    if arannisfriend:
        ara "Do not get distracted, [nickname]."
    else:
        ara "Focus, human."
    ara "Grab your weapon."
    show qh 62
    mc "*Turning around* Yes, sir! I am..."with dis
    mc "Um..."
    mc "What is that...?"
    stop soundloop fadeout 15
    play music2b arasong1 volume 0.6 fadein 5
    show qh 63
    ara "A longsword. You told me it was your favored blade, did you not?"
    show qh 62
    mc "I mean... yeah, but that one looks... real."
    mc "We’ve only trained with wooden ones until now."
    show qh 63
    ara "Not today."
    ara "You will not grow stronger by sparring with toys."
    ara "Now take your weapon."
    play soundlow sword
    scene qh 66
    ara "I will be using a shorter blade." with dis12
    ara "It should grant you some advantage."
    play sound3 sword3 volume 0.5
    show qh 67
    ara "And remove your robes. It would be improper to stain elven clothing in a playfight."with dis12
    play sound4 clothes3
    show qh 68
    mc "*Taking off your shirt* A-Alright."
    mct "He's tougher than usual today... is it because Calypso and Lorelei are here?"
    show qh 65
    lo "[mc] is... remarkably fit. Especially for a human." with dis14
    lo "My father has trained for centuries under the royal guard, and yet, [mc] rivals him in form. Perhaps even surpasses him in certain aspects."
    show qh 64
    ca "He is quite young still, after all."
    ca "That likely contributes to his... vigor."
    show qh 65
    lo "How young is he? In true years?"
    show qh 64
    ca "He told me he is eighteen. Though by our reckoning, that would place him nearer to... sixty, perhaps?"
    ca "Maybe seventy?"
    show qh 65
    lo "I see..."
    show qh 67
    ara "Prepare yourself. I will attack you now." with dis14
    ara "And I will not restrain myself as I did yesterday."
    show qh 68
    mc "Wait, wait, wait!"
    mc "What if I can't block your attacks in time? We've only been training for two days! With training swords!"
    show qh 67
    ara "You were quite confident in your rapid progress just two days ago."
    show qh 68
    mc "Well, yeah, b-but... I still might miss a few blocks!"
    mc "A real sword won't leave me with just a bruise!"
    show qh 67
    ara "Then I suggest you do not miss."
    show qh 68
    mc "B-But..."
    mc "You'll stop before actually hurting me, right...?"
    show qh 67
    ara "Will you also whimper like this when that demon returns?"
    show qh 68
    mc "I'm sorry...?"
    show qh 67
    ara "The demon in armor."
    ara "You told me about your battle against him. How he crushed you."
    ara "What is your plan if you face him again? Grovel and plead for your life?"
    show qh 68
    mc "What?! No! Of course n–"
    show qh 67b
    ara "What if your enemies come for those you hold dear?" with hpunch 
    ara "The ones you vowed to protect?!" with hpunch 
    ara "Will you let them die? Will you let them perish as you stand frozen in fear?!" with hpunch 
    ara "{sc=2}Or will you fight?!{/sc}" with hpunch 
    show qh 68
    mc "My... enemies...?" with dis
    play sound impact3b
    play sound2 impact3b
    scene qh 69 with flashfaster
    pause .15
    play sound3 impact3b
    play sound4 impact3b
    scene qh 70 with flashfaster
    pause .15
    play soun5 impact3b
    play sound6 impact3b
    scene qh 71 with flashfaster
    pause .15
    play sound impact3b
    play sound2 impact3b
    scene qh 68 with flashfaster
    pause
    show qh 73
    mc ". . ." with dis17
    play sound3 swordmove
    show qh 74
    mc "Hmph." with dis15
    show qh 75
    mc "I will fight."
    show qh 74
    ara ". . ."
    mod "Win for a Calypso point. Follow notifications on the left."
    play music2 ["<silence 4.7>"]
    queue music2 arasong2
    queue music2 arasongfull
    play sound arannissound1
    show arannis1 with dis12
    stop music2b fadeout 5
    $ renpy.notify("Bottom right")
    pause 5.5
    call screen qtearannis1 with dissolve
label larannis2:
    play sound parry
    scene arannis1s 
    pause 0.006
    scene white
    pause 0.006
    show arannis2
    $ renpy.notify("Top left")
    pause 2.2
    call screen qtearannis2 with dissolve
label larannis3:
    play sound2 parry
    scene arannis2s 
    pause 0.006
    scene white
    pause 0.006
    show arannis3
    $ renpy.notify("Top right")
    pause 2.2
    call screen qtearannis3 with dissolve
label larannis4:
    play sound parry
    scene white
    pause 0.006
    scene arannis3s 
    pause 0.006
    show arannis4
    pause 1.6
    $ renpy.notify("Top left")
    call screen qtearannis4 with dissolve
label larannis5:
    play sound7 arannissound2
    play sound2 parry2
    scene arannis4s 
    pause 0.006
    scene white
    pause 0.006
    show arannis5
    pause 0.5
    call screen qtearannis5 with dis17
label larannisfail:
    play soundlow parry
    play sound2 punch
    play sound punch
    play sound3 debris3
    play sound4 whoosh6
    scene qh51trans2
    bla "Arannis slams the hilt of his sword into your face." with hpunch
    play sound fallfull
    play sound2 sworddrop
    scene qh 51b with dis15
    if arannisslow:
        ara "You are too slow." with dis12
        ara "Your reaction comes {i}after{/i} the danger has passed." 
    else:
        ara "You are too hasty." with dis12
        ara "Speed without purpose is nothing but noise."
    show qh 51c
    mc "*Panting* But I have to think how–"
    show qh 51b
    ara "Thinking is not enough. {i}Instinct{/i} must carry you when conscious thought is too slow."
    ara "Do not hesitate."
    show qh 51c
    mc "*Panting* I understand. I will try."
    show qh 51b
    ara "This is BASIC. Did your father teach you nothing?"
    show qh 51c2
    mc "Pfft. My father didn't teach me shit."with dis
    ara ". . ."
    show qh 51b2
    ara "...He died?"
    show qh 51c2
    mc "Mmph. No, but..."
    mc "He might as well be dead. He's never been around."
    show qh 51c2
    ara ". . ."  
    show qh 51b2
    ara "On your feet, soldier." 
    ara "Our training has only just begun."
    show qh 51c
    mc "Yes, sir."with dis 
    jump labelpossparring
label laranniswin:
    play soundlow parry
    play sound punch
    play sound3 debris4
    play sound4 whoosh6
    scene qh50trans2
    bla "Your blade lashes out and halts a hairsbreadth away from the general’s throat." with hpunch 
    show qh 50b
    mc "Looks like your overconfidence finally bit you in the ass, General." with dis14
    mc "Drop your weapon."
    ara ". . ."
    play sound sworddrop
    show qh 50c
    ara "Mmph." with dis15
    play sound2 sword3
    play sound3 footsteps3b
    scene qh 68
    bla "You lower your sword, letting Arannis retrieve his blade and step back." with dis22
    show qh 67
    ara "I must admit, I have seldom witnessed such swift progress."
    show qh 68
    mc "Thank you, sir."
    show qh 67
    if arannisfriend:
        ara "Do not thank me yet."
    else:
        ara "I do not need your gratitude."
    ara "I let my guard down for but a moment — and you struck. Well done."
    ara "But your enemies might not afford you the same courtesy."
    ara "You need to be faster. Sharper. Unrelenting."
    ara "Let no hesitation dull your edge. Surrender your body to the rhythm of the sword."
    show qh 68
    mc "I understand. I will try."
    show qh 67
    ara "Let us continue."
    ara "Our training has only just begun."
    show qh 68
    mc "Yes, sir!"
    $ aranissparringwin = True
label labelpossparring:
    stop music2 fadeout 12
    play soundloop swordsparring volume 0.35
    if aranissparringwin:
        scene qh 76 with dis2
        lo "Whoa..." with dis12
        play music2b hyrilarhappy fadein 8
        lo "[mc] truly is strong... He bested my father!"
        lo "I might not have witnessed him in the prime of his life, but I was told there was no warrior on the continent who could defeat him in single combat."
        lo "The Morning Sword, they called him."
        show qh 77
        ca "Yes... I must confess, I am genuinely impressed as well."
        $ calypso_points += 1
        ca "His ability to improve so fast is remarkable. It certainly sheds light on how he managed to assemble such a formidable group."
        ca "Among them is a woman named Dalia, who is just as strong, if not stronger than he is in close combat."
        show qh 76
        lo "Really? Does his... harem participate in battle too?"
        show qh 77
        ca "Yes, although most of them wield magic. Astonishingly potent for mere humans, I must say."
        ca "And there is one, a girl with copper-colored hair, who wields metal devices capable of launching small projectiles over great distances."
        show qh 76
        lo "Like... a longbow?"
        show qh 77
        ca "Smaller than an arrow. But far more accurate. And lethal."
        ca "It really looks like magic, yet... it is not so."
        ca "A curious mortal weapon."
        show qh 76
        lo "Ohh... and do all these formidable female warriors follow him?"
        show qh 77
        ca "Well... yes, you could say they do."
        show qh 78
        lo "Whoa... It seems he truly is a force to be reckoned with."
    else:
        scene qh 80 with dis2
        ca "Huh... it appears [mc] still has a lot to learn." with dis12
        play music2b hyrilarhappy fadein 6
        show qh 78
        lo "I believe he is performing quite well, Lady Calypso."
        lo "I never witnessed my father in the prime of his life, but I was told there was no warrior on the continent who could best him in single combat."
        lo "The Morning Sword, they called him."
        lo "[mc] is not only blocking the majority of his strikes, but even forcing him to break a sweat."
        show qh 80
        ca "Yes... that much is undeniable." 
    show qh 78
    lo "Not to mention his stamina. He does not seem to know the concept of fatigue."
    show qh 79
    ca "Mm-hm..."
    show qh 80
    ca "His resilience has always been admirable, that is true."
    show qh 78
    lo "I now understand how humans managed to win so many wars in the past, if some of their soldiers were like this."
    lo "He is like... a siege engine."
    show qh 80
    ca "Indeed..."
    show qh 78
    lo "Like a... beast bred solely for battle."
    show qh 79
    ca "Mm-hm..."
    show qh 78
    lo "A creature designed to tear through all that opposes him."
    show qh 80
    ca "Yes..."
    show qh 78
    lo "To annihilate..."
    show qh 79
    ca "Mm-hm..."
    show qh 78
    lo "To conquer..."
    show qh 79
    ca "Mhm..."
    show qh 78
    lo "To procreate... and... breed."
    show qh 79
    ca ". . ."
    play sound pop
    play sound2 musicstop
    scene qh 81
    ca "W-What?" with hpunchsubtle
    show qh 82
    lo "What?!"
    show qh 81
    ca "What did you just say?"
    show qh 82
    lo "I-I said nothing, Your Grace."
    show qh 81
    ca "You said [mc] is like a beast made to procreate and breed."
    show qh 82
    lo "*Gasps* I-I would never utter such a thing, Your Grace! You have misheard me!"
    show qh 81
    ca "Do not lie to me!"
    show qh 82
    lo "U-Uhh..."
    show qh 81
    ca "By the Ancients, Lorelei, what happened to you during my absence?"
    ca "I knew you were always curious, but this is totally beyond the pale!"
    show qh 82
    lo "I-I-I spoke only from a purely biological perspective!"
    lo "I never once insinuated... anything of a carnal nature between an elf and–"
    show qh 81
    ca "Lorelei!" with hpunchsubtle
    show qh 82
    lo "Please, do not tell my father!" with hpunchsubtle
    show qh 84
    lo2 "Your Grace?" with dis
    show qh 85
    ca "Th-Thalindra!" with dis
    ca "What is the matter?"
    show qh 86
    lo2 "Lady Briena has arrived in the valley from the capital, as per your summons." with dis
    show qh 87
    ca "Ah, the druid!"
    ca "Splendid!"
    show qh 86
    lo2 "She is waiting for you in the main hall."
    lo2 "Would you have me ask her to wait there?"
    show qh 87
    ca "No, let us not keep her waiting."
    ca "Thank you for delivering the message, Thalindra."
    ca "We shall return with you at once."
    show qh 86
    lo2 "Of course, Your Grace."
    stop soundloop fadeout 2
    play sound debris
    scene qh 88
    ca "*Standing up* My apologies for departing so soon, gentlemen, but there are pressing matters that require my attention at the palace." with dis14
    ca "I wish you a productive training session."
    show qh 89
    ara "It was an honor, Your Grace. Your presence alone was a blessing to us." with dis
    show qh 90
    mc "Totally! Thank you for tagging along, Princess."with dis06
    mc "It's always awesome to hang out with you."
    show qh 91 with dis14
    pause
    show qh 92
    mc "Hmm?" with dis
    ara ". . ."
    show qh 93
    mc "I-I mean... I am most grateful for the honor of your presence this morning, Your Highness. Your attendance has been truly enlightening."with dis14
    show qh 94
    ca "*Snorts* Hmmph."
    ara "Come now, and adjust your stance accordingly!"
    mc "At once, sir!"
    stop music2b fadeout 6
    scene black with dis27
    show screen sometimelater with dis2
    pause
    play soundloop birds fadein 3
    hide screen sometimelater
    scene qw 1
    with dis3
    play music2 hyrilarchill fadein 5
    pause 
    ca "Good evening, Lady Briena." with dis
    show qw 2 
    lbr "*Turning around* Hmm?" with dis
    show qw 3
    lbr "OH! Vaerion bless us all!" with dis 
    lbr "It is true! You have truly returned!"
    lbr "The Princess of Hyril'ar walks among us once more!"
    show qw 3b
    ca "*Chuckle* You make it sound like I came back from the dead."
    show qw 3
    lbr "Surely it is the same! It remains nothing short of a miracle!"
    play sound whoosh6
    play soundlow debris3
    show qw 4
    lbr "And I see you remain as splendorous as ever..." with pr
    lbr "As lush and full of life as the matriarch of a great dynasty should be!"
    show qw 5 
    ca "I see you have not changed in the slightest since we last met."
    show qw 4
    lbr "When one has lived as long as I have, one learns that excessive formality is little more than a tedious habit, my dear."
    lbr "And was it not you who made me swear to always speak the truth, even if it meant casting protocol aside?"
    show qw 5
    ca "Yes..."
    ca "And that is precisely why I summoned you from the capital."
    ca "That, and... your expertise in medicine."
    play sound footsteps2
    show qw 6
    lbr "Ah yes, yes, I remember your letter well!" with dis15
    lbr "Your magical strength is waning... and I believe I might know why."
    show qw 7
    lbr "I prepared this herbal tea for you." with dis15
    lbr "While it will not resolve the root of your issue, it should offer some temporary relief."
    play sound chair2
    show qw 8
    lbr "*Handing the tea to Calypso* Drink it, but be careful–it is hot!" with dis15
    ca "Hmph."
    play sound2 sip
    show qw 9
    ca "*Sipping delicately* Hmmm." with dis12
    ca "Hmph."
    show qw 10
    ca "Ahh... it tastes surprisingly good." with dis12
    ca "Thank you, Lady Briena."
    show qw 11
    lbr "Naturally, my Lady."
    lbr "I would never dream of offering you anything less than exquisite."
    show qw 10
    ca "I appreciate that."
    show qw 12
    ca "Now... regarding the matter I mentioned in my letter..."
    ca "As I told you there, I cannot say with certainty what is happening, but... my magic has been feeling... diminished lately. Sluggish."
    ca "I have spoken to no one of this, yet ever since I awoke from my imprisonment, I've been finding it more and more difficult to cast."
    show qw 15
    lbr "What exactly happened before you lost consciousness?"
    show qw 12
    ca "I was forced to expend a considerable amount of magic to overcome that demon, but even so... I should not have collapsed the way I did."
    ca "Physically, I feel whole. Yet there remains this... hollow sensation in my chest. A weariness that refuses to leave me."
    ca "Tasks that once required but a breath of effort now demand intense focus. Even opening a portal is taxing."
    show qw 11
    lbr "Ahhh... yes. Just as I suspected."
    lbr "I believe I know what ails you, Your Grace."
    lbr "Centuries ago, I aided your grandmother with this very same affliction."
    show qw 10
    ca "Truly? That is reassuring to hear."
    ca "What is it? And how can I restore myself?"
    show qw 14
    lbr "You see..." with dis
    lbr "Your magic is not fading, your Grace, it is just... starving."
    lbr "You are like... an ancient tree. Your flowers bloom, but your roots thirst."
    play sound2 sip
    show qw 9
    ca "*Sipping delicately* Hmmm." with dis
    show qw 12
    ca "Humph... Thirst? What do you mean?" with dis
    show qw 14
    lbr "How to say..." 
    lbr "Anima's magic is a powerful one. You are holding all that power within you... when it is meant to be released."
    lbr "Nature thrives on release, not restraint, after all."
    show qw 12
    ca "So...?"
    ca "I am afraid I do not fully follow your metaphors, Briena."
    ca "Could you be a bit more explicit?"
    play sound2 sip
    show qw 9
    lbr "Of course, Your Grace." with dis12
    lbr "You need sex."
    play sound2 sip
    show qw 9
    ca "*Sipping delicately* Hmmm–{w=0.6}{nw}"
    stop music2
    play musicb sugarplum fadein 5
    play sound2 spitwater2
    scene qw 16 with hpunch 
    pause .6
    show qw 17
    ca "E-Eh?" with dis17
    ca "I-I beg your pardon...?"
    show qw 15
    lbr "You are approaching the height of your reproductive prime, Your Grace."
    lbr "Though we elves are blessed with long life, our fertility is not eternal. It reaches its zenith around the age of eighty and declines around our third century."
    lbr "The blood of Anima you carry within yourself cries out to be passed on."
    lbr "Ignored, it turns volatile."
    show qw 17
    ca "You are joking, right?"
    ca "This is another one of your absurd tales, born from those indecent novels you smuggle in from the Capital."
    show qw 15
    lbr "I speak only the truth, Your Grace."
    lbr "This inner storm is what disturbs your magic."
    show qw 18
    ca "I-I refuse to be reduced to a vessel."
    ca "I will not bear a child as if I were some breeding stock."
    show qw 11
    lbr "Fear not, Your Highness."
    lbr "Conception is not necessary... yet. Only... stimulation."
    show qw 20
    ca "Stimulation...?"
    show qw 11
    lbr "Precisely. The act alone, even without its final purpose, may be enough to trigger the right hormonal cascade."
    lbr "It would soothe the unrest in your core magic."
    lbr "Ideally, reaching climax as well."
    show qw 18
    ca "You speak of such things with far too much ease."
    ca "I-I am not even married."
    ca "And I am no common maid, to be offered like bread at a feast."
    ca "I shall not offer myself to the first noble who happens to pass through the gates of the castle."
    show qw 11
    lbr "As was to be expected, my Lady."
    lbr "Which is why Regent Thorund and I have taken the necessary steps."
    lbr "A Suitor’s Rite has been arranged — tomorrow, at dawn, within the walls of Usurper’s Keep."
    lbr "Three suitors, chosen from among the mightiest bloodlines in the realm, are already en route. You shall choose one, and with him, your future."
    show qw 18
    ca "What?!" with hpunch
    ca "By whose decree?! I never gave such permission!"
    show qw 15
    lbr "Forgive me, Princess, but the luxury of choice faded the moment you disappeared over a decade ago."
    lbr "The realm bleeds. Rebels stir in the East, and the southern border has fallen silent."
    lbr "We are being pulled apart from within, and our enemies press in from beyond."
    show qw 19
    lbr "By binding yourself to one of the old houses, you do not only stabilize your volatile magic — you secure the realm itself."
    lbr "Your union would cement vital alliances and quiet the flames of rebellion."
    show qw 20
    ca "But..."
    show qw 19
    lbr "I know this feels rushed, but time no longer bends to our will."
    lbr "There are whispers in the court, Princess... dark rumors of factions who would see your crown shattered."
    lbr "This is no longer about desire or even dignity. It is survival."
    ca ". . ."
    show qw 21
    ca "I... I understand."
    show qw 15
    lbr "The suitors will arrive at dawn, at the Usurper’s Keep."
    lbr "You must be present, Your Grace. The choice must be yours, or the realm will see it as weakness."
    show qw 19
    ca ". . ."
    show qw 21
    ca "I... understand."
    ca "I will be there."
    play soundlow clothes3
    play sound6 leathershort volume 0.3 fadein 1
    show qw 21b
    lbr "Thank you for your understanding, Your Grace." with dis12
    lbr "I shall take my leave now and begin preparations at the Keep. There is much to arrange before sunrise."
    ca "Very well..."
    play sound dooropencloseecho fadein 2
    show qw 22
    bla "The druid quietly takes her leave from the Princess’ chamber." with dis22
    ca ". . ."
    stop musicb fadeout 6
    play soundloop swordsparring volume 0.4 fadein 6
    $ renpy.music.set_volume(1, channel='soundloop2')
    play soundloop2 forest2 fadein 5
    play soundloop3 wind3 fadein 6 volume 0.4
    scene qw 23 with dis3
    pause
    ara "Left foot forward!" with dis
    ara "Balance first!"
    ara "Now close the gap! Wait for an opening!"
    play soundlow parry
    play sound2 punch
    play sound fallfull
    play sound3 debris3
    stop soundloop
    ara "You are still being too hasty!" with hpunch 
    play sound5 pantingb 
    play sound6 fallfull
    play sound7 sworddrop
    scene qw 25
    mc "*Panting* F-FUCK!" with dis2
    mc "*Panting* O-Okay, I just need... a m-minute to catch my breath."
    mc "*Panting* I-I know what I did wrong now."
    mc "*Panting* Let me try again."
    show qw 24
    ara "It is enough. You are getting slower with each attempt." with dis
    ara "We should rest now. We will continue tomorrow."
    show qw 26
    mc "I... I can't. I'm going back home tomorrow."
    show qw 24
    ara "Then we can resume whenever you are back in Hyril'ar."
    ara "There is little value in continuing now, if you are too tired to–"
    show qw 26
    mc "No!" with hpunch
    mc "There's still light! We can keep fighting!"
    ara ". . ."
    show qw 24
    ara "Why do you persist so stubbornly...?"
    play sound swordmove
    play sound2 debris
    show qw 27
    mc "*Standing up* Because I need to be better." with dis14
    mc "Because I can't afford to fail again."
    mc "Because... I need to protect them all."
    show qw 28
    ara ". . ." with dis17
    if arannisfriend:
        show qw 29
        ara "Hmph."with dis
    else:
        ara "Hmph."
    play soundloop swordsparring fadein 2
    scene qw 23
    bla "You continue training with Arannis until the sun sets." with dis22
    ara "Faster!" with hpunchsubtle
    ara "Control your breathing!" with hpunchsubtle
    mc "Yes, sir!" with hpunchsubtle
    stop soundloop fadeout 1
    play sound parry2
    stop soundloop2 fadeout 6
    stop soundloop3 fadeout 9
    scene black with dis33
    show screen nextday with dis25
    pause
    play soundloop2 fireplace fadein 5
    hide screen nextday
    scene black 
    with dis3
    pause
    mc "*Snoring* ZzzZzZzzzz...." with dis17
    play sound thunder
    pause 0.5
    scene qw30b with dis17
    scene black with dis15
    scene qw 30b with dis15
    play music2 hyrilarchill fadein 9
    mc "*Opening your eyes* Hmmpmh..." with dis15
    mct "Damn... that sounded close."
    mct "A big storm's coming."
    play sound couch
    play sound2 clothes3
    show qw 30 
    mc "*Yawns* (I slept like a rock, though.)" with dis14
    mct "Guess that’s what happens when you get wrecked by Arannis in training."
    mct "I barely made it to my bed before I passed out."
    play sound7 stomach
    mct "No wonder I’m starving now..."
    play sound2 knock2
    play sound knock2
    if arannisfriend:
        ara "*Knocking on the door* Lord [nickname]?"
    else:
        ara "Human?"
    ara "The Princess requests an audience with you."
    mc "An audience...?"
    ara "She mentioned something regarding a portal to... your homeland."
    play sound couch
    play sound2 whoosh6
    play soundlow chair1
    scene qw31
    mc "OH!" with pdd
    mct "Crap, I almost forgot!"
    mct "I'm finally going back home!"
    play sound3 whoosh6
    play sound7 couch
    scene qw32
    mc "*Leaping out of bed* Tell her I'm on my way!" with pl
    mc "Just gotta throw some clothes on and splash some water on my face!"
    mc "*Grumbling* Goddammit, why the hell do elves always wear stuff three sizes too small? Is circulation just optional for you guys?"
    ca "Indeed, comfort is seldom prioritized when choosing our garments."
    play sound4 whoosh6
    play sound5 impactwood
    play sound6 debris3
    scene qw33
    mc "*Spinning around* GAArgh!" with hpunch 
    mc "C-Calypso!"
    mc "You scared me! I didn't even hear you come in!"
    scene qw 35
    ca "Oh..."
    ca "Forgive me, I did not know you were dressing."
    scene qw 33
    mc "No, no, it's all good! You just caught me off guard — I'm still kinda half-asleep."
    mc "You're welcome to drop by anytime."
    mc "Especially if you're wearing... such an {i}elegant{/i} outfit."
    mc "Damn... you look amazing, Caly."
    scene qw 34
    ca "Ah... yes, this is one of our ceremonial ensembles."
    ca "I must admit it is rather... revealing."
    show qw 33
    mc "Yeah, that regent lady at the trial who wanted to fry me had something similar on."
    mc "It goes without saying who's wearing better, of course..."
    show qw 34
    ca "Oh... thank you. I appreciate your compliments."
    show qw 33
    mc "Are you okay...? You seem a little... off today."
    show qw 35
    ca "Yes... yes, do not worry about me."
    ca "There are simply... many matters that require my attention today. Affairs of the realm, as always."
    show qw 34
    ca "But such is the weight of my title... the duty of... a Princess."
    show qw 33b
    ca "Still, as I promised, I have gathered the strength required."
    ca "I am able to open a portal to your world again."
    ca "So you may go whenever you are ready."
    show qw 33
    menu:
        with dis
        "Dig deeper [gr][mt](Calypso's path)":
            mc "That can wait." with dis
            mc "What's troubling you?"
            mc "I know you well enough to see that something's eating at you."
            show qw 34
            ca "Well... I merely..."
            ca "Um..."
            show qw 33
            mc "Come on, you can tell me, Calypso."
            mc "I know you probably can't say what you really think often, given your position."
            mc "But I've got no ties to all this politicking. You can be candid with me."
            show qw 34
            ca "Uh... yes... I suppose you are right."
            ca "Very well..."
            stop music2 fadeout 6
            play soundlow footsteps4
            scene qw 37 with dis2
            play sound2 couch
            play music2b kingrests fadein 6
            bla "The Princess walks past you and sits down on the bed, a melancholic expression settling on her face." with dis17
            show qw 36
            ca "As you probably noticed... ever since you freed me from my imprisonment, I have longed to return to Hyril'ar."
            ca "Not because I missed it, but... because I believed that is where I was meant to be."
            show qw 37
            mc "And... does it feel different now? After being away for so long?"
            show qw 36
            ca "On the contrary, it... does not."
            ca "Everything is exactly as I remembered."
            ca "The people, the buildings, the forests... even the weather remains unchanged."
            ca "As if it had been... frozen in time. Like a painting created from my memories."
            show qw 37
            mc "But... something doesn't feel right."
            ca "Hmph."
            show qw 36
            ca "Yes..."
            ca "I am supposed to be the most powerful person in the realm, and yet, I feel... powerless."
            ca "The only thing I thought I could rely on — my magic — is now a mere shadow of what it once was."
            ca "It... eludes me, slipping from my grasp. Like I cannot control it anymore."
            show qw 38
            ca "And now, they are even forcing me to..." 
            ca "T-To..."
            play sound clothes3
            show qw 39
            ca "*Sighs* Aahh..." with dis14
            show qw 40
            ca ". . ."
            show qw 39
            ca "Can I tell you a secret, [mc]?"
            show qw 40
            mc "Of course."
            ca ". . ."
            show qw 39
            ca "I..."
            ca "I do not want to be a princess."
            show qw 40
            mc "You don't...?"
            show qw 39
            ca "I do not."
            ca "I do not wish to rule a kingdom."
            ca "And I have no interest in being the heir to an ancient dynasty."
            ca "What I want is..."
            show qw 40
            ca ". . ."
            show qw 39
            ca "I want to... wander across realms and seek out adventures."
            ca "I want to infiltrate gambling dens with a wild, convoluted, flawed plan."
            ca "I want to attend secret dinners, wearing masks, and staying disguised."
            ca "I want to ride across endless deserts, galloping through sandstorms in a world full of dust, horses, and guns."
            ca "Like... the time I've spent with you."
            show qw 40
            menu:
                with dis
                "Stay silent":
                    mc ". . ." with dis08
                    show qw 39
                    ca "But... I suppose that is a foolish dream."
                    ca "One cannot change the destiny that was written for them."
                    ca "There is only one path... and we are bound to walk it."
                    ca "That is life..."
                    $ calypsopath = False
                    play sound clothes3
                    show qw 36
                    ca "But anyway..." with dis14
                    ca "Forgive me, I know you must be eager to return to your world." 
                    ca "I will not keep you any longer."
                    show qw 37
                    mc "I can't say I relate, but... I understand how you feel."
                    mc "Thank you for trusting me enough to say all that, Calypso."
                    mc "Is there anything I can do to help?"
                    show qw 36
                    ca "You have already done enough by listening to my wailing."
                    ca "Thank you, [mc]. Truly."
                    play sound2 couch
                    play soundlow footsteps4
                    jump portalleave
                "Hug her [mt](okay if > 7 points)":
                    play sound couch
                    play sound2 clothes3
                    play sound3 chair1 volume 0.2
                    show qw 41
                    bla "You sit on the bed and, swift yet gentle, pull Calypso into your arms." with dis15
                    if calypsotogether and calypso_points >= 8:
                        scene qw 42
                        mc "I know what you're thinking!"
                        if calypsofirsthug:
                            mc "{i}“How dare you hug me again, human?! Didn't I warn you yesterday?!”"
                        else:
                            mc "{i}“How dare you hug me, human?! You could be hanged for this!”"
                        mc "But trust me, I know what I'm doing. I can tell when someone needs a hug. No one's watching, and no one will ever know."
                        mc "So no arguing. Just close your eyes, try to breathe slowly, and give it a minute."
                        mc "You'll see things a little clearer afterwards, I promise."
                        mc "If you don't, I give you permission to vaporize me."
                        show qw 43
                        ca "Mmmrh..."
                        ca "Hmph."
                        jump calyhug2
                    else:
                        ca "Hmph?!"
                        jump calyhug2fail
                "[gr]Ask her for permission to hug her":
                    mc "Can I... can I hug you?" with dis08
                    show qw 40b
                    ca "Excuse me?"with dis
                    show qw 40c
                    mc "I mean... I kinda feel like a hug could help now."
                    mc "It’s worked for me when I was feeling down."
                    mc "But... I also know it’s like a capital crime to touch the Princess, so... thought I’d ask first."
                    show qw 40b
                    if calypsotogether and calypso_points >= 5:
                        ca "Uhh..."
                        show qw 40c
                        mc "No one's watching, and no one will ever know."
                        mc "It will stay between us."
                        show qw 40b
                        ca "You humans sure like physical contact."
                        show qw 40c
                        mc "Is that a yes?"
                        ca "Hmph."
                        show qw 40b
                        ca "*Sighs* Fine..."
                        ca "If you truly think it will help..."
                        play sound couch
                        play sound2 clothes3
                        play sound3 chair1 volume 0.2
                        show qw 41
                        bla "You sit on the bed and, swift yet gentle, pull Calypso into your arms." with dis15
                        scene qw 42
                        mc "Trust me, I know what I'm doing. I can tell when someone needs a hug."
                        mc "Just close your eyes, try to breathe slowly, and give it a minute."
                        mc "You'll see things a little clearer afterwards, I promise."
                        mc "And if you don't, I give you permission to vaporize me."
                        show qw 43
                        ca "Mmmrh..."
                        ca "Hmph."
                        jump calyhug2
                    else:
                        $ calypsopath = False
                        ca "I... appreciate the sentiment, but I would rather not, thank you."
                        show qw 40c
                        mc "Oh..."
                        mct "Damn, that was awkward."
                        mc "Well... I had to try."
                        play sound clothes3
                        show qw 36
                        ca "*Sighs* I imagine you must be eager to return to your world." with dis15
                        ca "Forgive me, I will not take more of your time."
                        show qw 37
                        mc "Hey, about the things you told me..."
                        mc "I can't say I relate, but... I understand how you feel."
                        mc "Thank you for trusting me enough to say all that, Calypso."
                        mc "Is there anything I can do to help? Other than offering a hug?"
                        show qw 36
                        ca "You have already done enough by listening to my wailing."
                        ca "Thank you, [mc]. Truly."
                        ca "I will not forget it."
                        play sound2 couch
                        play soundlow footsteps4
                        jump portalleave
        "Let it go":
            $ calypsopath = False
            mc "Well, if you say so... I won't insist." with dis   
            mc "Alright then!" 
            mc "I'm ready to go!"
            show qw 33b
            ca "Very well..."
            jump portalleave
label calyhug2fail:
    play sound4 whoosh6
    play sound7 debris3
    scene qw41b
    ca "W-W-What in heavens do you think you are doing?!" with hpunch
    if calypsofirsthug:
        ca "Did I not make it clear yesterday that you should not do this?!"
    scene qw 41c
    mc "I-I mean... I thought..."
    mc "Well, I thought you might need a hug."
    scene qw 41b
    ca "This is entirely against protocol, and you know it."
    ca "By the Ancients, you are fortunate no one is around or you would be back at the gallows in the blink of an eye."
    show qw 41c
    mc "S-Sorry. My bad. I'm... still not used to royal protocol."
    mc "Won't happen again."
    show qw 41c2
    ca "Hmmph."
    play sound clothes3
    play sound2 couch
    scene qw 50
    ca "*Clears throat* I mean... I do appreciate the sentiment behind your actions." with dis15
    ca "And thank you for listening to my... wailing."
    show qw 50b
    mc "Of course, Princess."
    mc "I can't say I relate, but... I understand how you feel."
    mc "Thank you for trusting me enough to say all that."
    show qw 50
    ca "Of course."
    ca "But... anyway..."
    ca "I have taken enough of your time, and I imagine you must be eager to return to your world."
    show qw 50b
    mc "I am!"
    $ calypsopath = False
    play soundlow footsteps4
    jump portalleave
label calyhug2:
    play sound clothes3
    scene qw 44 with dis17
    bla "Calypso slowly leans in, her arms wrapping around you with faint strength." with dis15
    mct "It feels good to have her in my arms."
    mct "So mighty, so wise... yet so vulnerable at the same time."
    ca ". . ."
    show qw 46
    ca "Your heartbeat is racing."
    ca "Are you nervous?"
    ca "Or are you concerned you'll be caught dishonoring the Princess?"
    show qw 45
    mc "That’s just my normal speed. I’m a nervous guy by nature."
    show qw 46
    ca "Ah, I see..."
    show qw 45
    mc "What about you? Feeling any better?"
    show qw 46
    ca "Slightly."
    ca "It will not change what I must do today, but... perhaps slightly better, yes."
    show qw 45
    mc "What about today is worrying you so much, anyway?"
    show qw 46
    ca "Ah, well..."
    ca "I need to choose a husband."
    ca "Three suitors are to arrive this morning here at the Usurper's Keep."
    show qw 47
    mc "Wait, what?!"with dis08
    mc "A husband?!"
    show qw 48
    ca "The realm needs stability."
    ca "A marriage will solidify the loyalty of the other lords."
    ca "I already knew this was bound to happen someday."
    show qw 47
    mc "And you have to choose TODAY?!"
    show qw 48
    ca "So it seems."
    show qw 47
    mc "You know, for a race that can live for thousands of years, you sure like to rush everything around here."
    mc "From trials, to executions, to... marriages, apparently now!"
    mc "I thought you'd be like Ents, taking days to make decisions through endless conversations."
    show qw 48
    ca "Hah, yes..."
    ca "I too wish things could move a little slower."
    show qw 47
    mc "Why do you even need a marriage, anyway?"
    mc "With your power, you could crush any enemy that dares to oppose you."
    show qw 48
    ca "That is also one of the reasons."
    ca "The Grand Druid believes it will help me restore control over my magic."
    show qw 47
    mc "Really? How?"
    show qw 48
    ca "She says that the hormonal..."
    show qw 48b
    mc "Hmm?"
    show qw 48
    ca "*Clears throat* A-Anyway, that is irrelevant."
    ca "Please, remain silent."
    ca "You are disturbing my inner peace."
    show qw 45
    mc "*Chuckles* Alright, alright."with dis
    play sound3 ["<silence 4>", church2] volume 0.2
    scene qw 49
    bla "You and Calypso hold each other, savoring the moment in silence, until the distant toll of a bell pierces the quiet." with dis2
    mc "Hmm? Is that a bell?" 
    ca "A bell...?"
    play sound clothes3
    play sound2 couch
    scene qw 50
    ca "*Standing up* Oh... I-Indeed, it is." with dis15
    ca "That means the suitors must have arrived at the keep."
    ca "I nearly drifted off there for a moment. Please, forgive me."
    show qw 50b
    mc "There's nothing to forgive, Princess."
    mc "I'm glad if it helped you in some way."
    show qw 50
    ca "It... certainly helped clear my mind for a moment. I must thank you."
    ca "But... anyway, I have taken enough of your time."
    ca "I imagine you must be eager to return to your world."
    show qw 50b
    mc "I am!"
    play soundlow footsteps4
label portalleave:
    show qw 51
    ca "*Deep exhale* . . ." with dis17
    ca "{i}Glem ni sa' eradin..." 
    play sound3 spell3
    play sound2 spell2
    play soundloop energy2 fadein 1
    show qw 52 with dis12
    mc "HELL YEAH!" with dis
    mc "You really did it!" 
    show qw 54
    ca "Naturally. Did you doubt me?" with dis12
    show qw 53
    mc "Not for a second!"
    ca "Hmph."
    mc "Where's this portal going to take me?"
    show qw 54
    ca "To Ekabar. After spending so much time there, it proved to be the easiest destination."
    ca "I am still not at full strength, I must admit."
    show qw 53
    mc "That works just fine!"
    mc "I should be able to teleport back to Kredon from there."
    mc "Or... at least I hope so. Worst case, I can get in touch with the girls and we’ll figure something out."
    show qw 54
    ca "Good. Please, give them all my warm regards."
    show qw 53
    mc "There’s just one thing I’m wondering, though..."
    mc "What if I can’t come back to Hyril’ar on my own? I can't use my “plane-shifting” power from here, so maybe it's the same from the other way."
    show qw 54
    ca "There is much I must resolve here — disputes within the realm, tensions between the houses..."
    ca "But once everything is solved..."
    ca "I will come to you myself."
    ca "I promise."
    if not calypsopath:
        ca "At the very least... for a visit."
    show qw 53
    mc "I will be looking forward to it."
    mc "Please, take care, Calypso."
    mc "And thank you for... everything."
    show qw 54
    ca "Thank you for showing me that not all humans are insufferable, [mc]."
    ca "Turns out one or two of you might actually be... tolerable."
    if calypsopath:
        ca "Maybe even... more than that."
    show qw 53
    mc "Well, most of us are still terrible."
    mc "I'm just an exception."
    show qw 54
    ca "*Chuckles* A rare one, indeed."
    show qw 53
    mc "*Chuckles* Indeed."
    mc "Until next time, Princess." 
    show qw 54
    ca "Until next time."
    play sound footsteps4
    scene qw 55  
    bla "You slowly walk towards the portal." with dis22
    mc "Aahh..."
    mct "Beaten by an elven general, nearly executed, thrown in prison for days... and honestly, it doesn’t even feel that bad."
    mct "Either I’m still in shock from finding out Hyril’ar is real... or maybe I’ve got a thing for pain without realizing it."
    mct "Just another episode in the crazy story of our lives, I guess..."
    mod "Stay for Calypso's path and more content."
    call screen hyrilarstaychoice with dis17
label hyrilarenter:
    play sound impact3
    if calypsopath:
        scene hyrilarstayidle
    else:
        scene hyrilarstayidle2
    pause 0.001
    scene qw 55
    mct "Time to move on to the next chapter." with dis
    $ mcleaveshy1 = True
    jump mcisback
label hyrilarnoenter:
    play sound impact3
    scene hyrilarstayidle
    pause 0.001
    scene qw 55
    mct "And yet..." with dis
    mct "Why do I feel like this chapter isn't finished yet...?"
    mc ". . ."
    play sound footsteps4
    scene qw 56
    bla "You take a few steps back." with dis17
    scene qw 57
    ca "I do not want to rush you, but..."
    ca "As I mentioned, I am still not at full strength."
    ca "Keeping the portal open is... more taxing than it once was."
    show qw 56
    mc "You can close it."
    mc "I'm not leaving just yet."
    play sound3 spell3
    play sound2 spell2
    play sound4 debris
    stop soundloop fadeout 1
    scene qw 58
    ca "What...?" with dis
    show qw 59
    mc "I'll go with you to that whole... “husband choosing” thing."
    mc "It sounds like a recipe for disaster, and I’m not gonna let you walk into it alone."
    mc "You need your bodyguard. Physical backup, moral support, and personal advice — the whole package."
    show qw 58
    ca "But... why?"
    ca "You are not obligated to accompany me. I have not asked you to stay."
    show qw 59
    mc "So...?"
    mc "You don’t stick around for someone just because they {i}ask{/i} you to."
    mc "You do it because you care. That’s what people do when someone matters to them."
    mc "And besides... the girls would tear me apart if they found out I left you behind to deal with all this crap on your own."
    mc "You’re one of us now. Whether you like it or not."
    show qw 58
    ca "A-Are you... certain of this?"
    show qw 59
    mc "Of course! I've been here for like a week, what's a few more hours?"
    mc "Let's go before we're late!"
    ca ". . ."
    mc "Come on, Princess! What are we waiting for?!"
    show qw 58
    ca "Uh... w-well..."
    show qw 60
    ca "A-Alright, I accept, but... perhaps you ought to consider putting on some clothes before we leave this room, would you not agree?" with dis15
    show qw 61
    mc "Oh... fair point."
    mc "We wouldn’t want the noble people of your kingdom to see their beloved Princess walking around with some half-naked human guy."
    play sound footsteps4
    show qw 62
    ca "*Chuckles* Most certainly not." with dis15
    ca "What would they say?"
    play sound clothes6
    play sound2 clothes3
    show qw 63
    mc "*Putting your shirt on* Surely nothing good. Scandal of the century."
    show qw 62
    ca "*Chuckles* Surely..."
    show qw 63
    ca "*Taking a deep breath* . . ."
    show qw 62
    ca "Thank you for accompanying me to this dreadful affair, [mc]. It makes me feel more at ease."
    show qw 63
    mc "It's the very least I could do, Princess."
    show qw 62
    ca "You are wearing it upside down."
    show qw 63
    mc "What?"
    mc "*Glancing down at your shirt* Oh, for fuck's sake–"
    play sound clothes6
    play sound2 clothes3
    mc "Why are elven robes for guys so confusing?!" 
    show qw 64
    ca "{i}Fuck{/i}... I noticed you seem to use that word quite often." with dis15
    show qw 65
    mc "*Chuckles* Oh, yeah... the mighty {i}fuck{/i}!"
    mc "Humanity’s most versatile contribution to language!"
    show qw 64
    ca "What is its exact meaning?"
    show qw 65
    mc "Well, you can use it in literally any situation. Angry? {i}Fuck{/i}! Shocked? What the {i}fuck{/i}?! Excited? Let's {i}fucking{/i} go!"
    mc "It’s all about tone and context."
    mc "Like, if you say you wanna {i}fuck{/i} with someone, it means you want to mess with them. Tease them. Cause a little trouble."
    play soundlow footsteps4
    show qw 66
    mc "But if you drop the {i}with{/i}, and just say you wanna {i}fuck{/i} someone..."with dis15
    mc "Well... that means you want to have some fun with them."
    mc "{i}That{/i} kind of fun."
    show qw 67
    ca "Hmph."
    show qw 68
    ca "Interesting. How... nuanced."
    ca "You humans do seem especially gifted at concealing layers of meaning beneath even your crudest expressions... despite your general lack of refinement in poetry and prose."
    ca "It is... rather fascinating."
    show qw 69
    ca "Do you think you could teach me more of your... human expressions on the way to the hall?" with dis12
    show qw 70
    mc "It’d be my absolute pleasure, Princess."
    mc "You’ve got yourself the most foul-mouthed human in the entire court."
    show qw 69
    ca "Excellent then."
    ca "Now, please, remain at my side as we walk."
    ca "I will grant you one of the royal armors. From this moment on, you shall serve as my... protector."
    show qw 70
    mc "Nothing would make me happier, Your Grace..."
    stop music2b fadeout 6
    stop soundloop2 fadeout 8
    scene black with dis27
    show screen sometimelater with dis25
    pause
    play music2 hyrilarhappy fadein 7
    hide screen sometimelater
    scene qw 71
    with dis3
    pause
    play sound wood2 volume 0.4
    ca "*Leaning back* So then..." with dis12
    ca "These Gems of yours, are they the only things you are unable to carry between “Eternum” and Earth?"
    mc "I can bring most stuff from the real world into Eternum as long as I'm holding it, or... if I’ve got it in my pocket or whatever."
    show qw 72
    mc "But... it doesn’t work the other way around. Stuff from here, like the Gems, Nova's gun, or any magic items, just... don’t come with me." with dis12
    mc "They stay exactly where I left 'em."
    show qw 73
    ca "Also the Gems?" with dis
    show qw 74
    mc "Well... the Gems are different, actually. They somehow just reappear with me, whatever server I end up in." with dis
    mc "I don’t control it, I’ve got no idea how it works... but it happens every time."
    show qw 75
    ca "And what about living beings? Can you bring people with you?"
    show qw 74
    mc "Yeah, as long as I’m touching them when I jump into Eternum."
    mc "But as I learned the hard way, it's insanely risky."
    mc "Eternum makes Earth look like a playground."
    show qw 75
    ca "Who did you bring?"
    show qw 74
    mc "Nova and then Dalia, but that was a one-time thing."
    mc "I’m not planning on doing it ever again — way too dangerous."
    if alexpoolvisit:
        mc ". . ."
        mc "...Well, okay, technically Alex too. B-But that was an accident."
        mc "Kinda."
    show qw 75
    ca "What about the reverse, then? Could you... take someone from Eternum back with you? To your world?"
    show qw 74
    mc "I tried it once with an NPC. Didn’t work."
    mc "Just like the artifacts and everything else that’s native to Eternum... they can’t cross over. They stay behind."
    show qw 76
    ca "I see." with dis
    show qw 77
    mc "Why do you ask?"
    mc "Were you... thinking about visiting Earth?"
    show qw 76
    ca "Uh..."
    ca "Well, I must admit I have listened to you speak of it so often that I found myself wondering what it might be like."
    ca "But... it was just a fleeting thought. I have no time for such distractions."
    ca "And I doubt I could remain there for long, even if I could visit."
    ca "This is my place. The life I was born into."
    ca "The... life I must live."
    show qw 77
    mct "Mmmh..."
    mct "Now that I know Calypso doesn’t actually enjoy ruling, it makes me want to bring her to Earth even more."
    mct "There's gotta be a way, right?"
    mct "But how...?"
    play sound armor
    play sound2 leathershort volume 0.3 fadein 1
    show qw 78
    ara "*Bowing down* Your Highness." with dis12
    show qw 80
    ara "Preparations are complete." with dis
    ara "The suitors are assembled and await your summon."
    show qw 79
    ca "Good. Thank you, General."
    ca "You may allow them entry, but have their delegations remain by the gates."
    show qw 80
    ara "As you wish, Your Grace."
    show qw 79
    ca "And... I am aware our forces are stretched thin, but assign the majority of the guard to greet the suitors’ delegations."
    ca "We must project strength."
    show qw 80
    ara "A prudent decision, my Lady."
    ara "It shall be carried out as instructed."
    play soundlow armorwalk2
    show qw 82 with dis17
    mc "*Watching Arannis leave the hall* So..." with dis15
    mc "Have you had many suitors knocking on the door before today?"
    show qw 81
    ca "Well... Lord Thorund has persistently sought to find me a spouse ever since my parents passed."
    ca "But there was little urgency back then. Our realm stood far above any threat, so I could afford to dismiss them all."
    ca "None were... worthy."
    show qw 82
    mc "Whoa, not even an elven prince made the cut? He needs more?"
    show qw 81
    ca "Naturally."
    ca "The King of Hyril’ar must hail from a house of equal or near-equal standing to my own."
    ca "He must possess strength in battle, be noble in bearing, and {i}equally{/i} excel in the three sacred arts."
    show qw 82
    mc "Damn, that's quite the resume."
    mc "Would I even stand a chance...?"
    mc "I can certainly fight. And I don't know about those three arts, but I'm a nice guy. Funny sometimes, too."
    show qw 81
    ca "Please, [mc]. The mere idea of a human romancing the Princess of Hyril’ar, let alone being granted power or status, would plunge the realm into outright war."
    show qw 82
    mc "Okay, but... imagine I had pointy ears and a fancy family crest for a second."
    mc "Would I make the shortlist then?"
    ca ". . ."
    show qw 83
    ca "Hmph."with dis08
    show qw 84
    ca "Perhaps... if your tunes were sweet enough."
    show qw 83
    mc "I'll take that..."
    play sound chair2 volume 0.5
    play sound2 wood2 volume 0.5
    scene qw 85
    bla "Calypso’s maids take their seats along one side of the throne platform." with dis15
    mct "Ah, there's Lorelei."
    mct "Probably the only person here other than Calypso who doesn’t look at me like the palace needs to be fumigated after I leave."
    mct "Though, to be fair... I think her father is starting to warm up to me too."
    mct "I'm sure that by the time we’ve collected all ten Gems, we’ll be best friends."
    mct "Legolas and Gimli 2.0."
    menu:
        with dis
        "Wave to her [calypso_pts]":
            scene qw 85a with dis
            pause
            play sound twirl volume 0.3
            scene qw65b
            pause 1.2
            scene qw 85c
            $ calypso_points += 1
            lo "*Whispers* D-Did you see that?!" with dis
            lo "*Whispers* They also wave! Just as we do!"
            lo2 "Hmm?"
        "Ignore her":
            pass
    play sound chair2 volume 0.5
    play sound2 wood2 volume 0.5
    scene qw 86 with dis12
    mct "Ugh, and on the other side... the exact opposite." with dis
    mct "These assholes again... They nearly got me killed last time."
    mct "Well, at least that Sylax prick isn't here."
    mct "Hmph."
    mct "Strange... why isn't he here...?"
    play soundlow clothes3
    play sound6 leathershort volume 0.3 fadein 1
    scene qw 87
    cc "It is an honor to stand in your presence, My Lady." with dis14
    ca "The pleasure is mine, Chamberlain."
    scene qw 88
    cc "All has been prepared according to tradition." with dis
    cc "Three suitors have answered the call, each seeking your favor. They will present themselves before the Crown and attempt to prove their worth."
    cc "Then the regents, guided by my counsel, will deliberate on which of them stands most fit."
    show qw 93
    ca "And I am to have no voice in the matter?"
    show qw 88
    cc "Oh, but of course, Your Grace."
    cc "We serve merely as advisors. The final choice shall rest solely with you... as long as a choice {i}is{/i} made."
    cc "Your Grace is, no doubt, aware of the dire need for a King and for the alliance his house might bring in these... turbulent times."
    show qw 81
    ca "Yes..."
    ca "I am well aware."
    show qw 88
    cc "Excellent! Then, in accordance with custom, we must appoint a champion to stand in your name."
    cc "A proxy to represent your royal standard in the ceremonial trials."
    cc "Shall we presume General Arannis will fulfill the role once again?"
    show qw 81
    ca "I have sent General Arannis to entertain the suitors' entourages."
    ca "He will not be available today."
    show qw 88
    cc "Oh... I see."
    cc "Then, may I suggest Lord Lyond’or of the Royal Guard? A trusted blade and a lover of poetry."
    cc "Or perhaps Lord Stannis, of the cavalry?"
    show qw 81
    ca "Uh..."
    show qw 82
    ca "Mmmh." with dis08
    show qw 83
    ca "Hmmm..." with dis08
    show qw 84
    ca "Actually..."
    ca "Lord [mc] shall serve as my champion today."
    show qw 89 
    cc "Lord..." with dis 
    show qw 90
    cc "[mc]...?" with dis08
    cc "You mean... the human...?"
    show qw 90b
    tho "By the Ancients, my Lady!" with dis
    tho "Surely you do not intend to place your human servant as our court’s champion?!"
    tho "It would be seen as a mockery!"
    play sound crowdwhisper
    show qw 90b2
    bla "A wave of murmurs sweeps through the Court, as loud as protocol permits. Shock, disbelief, and disdain flicker across every face." with dis15
    mc ". . ."
    show qw 84
    ca "We shall give him a helmet to conceal his identity." with dis12
    ca "No one needs to know who fights in my name."
    show qw 92
    cc "B-But, Your Grace..."
    cc "With all due respect, the purpose of the champion is to {i}outshine{/i} the suitors and grant us greater leverage in the marriage negotiations."
    cc "If the human performs poorly, or is recognized, it will humiliate the court and place us in an inferior position."
    show qw 93
    ca "I fully understand, Lord Chamberlain."
    ca "And my decision is final."
    ca "You are not attempting to overrule me, I trust?"
    show qw 92
    cc "A-Ahh... uh..."
    cc "N-No, Your Grace. Of course not."
    cc "It..."
    cc "It shall be done as your command."
    show qw 91
    cc ". . ." with dis12
    mc "Um..."
    mc "So... what exactly am I supposed to do now?"
    show qw 90
    cc "For starters, do not speak unless you are given permission, human."
    show qw 91
    mc "R-Right. Got it."
    show qw 90
    cc "Now come with me. We'll hide your identity with a helm."
    cc "Then, the suitors will arrive and present themselves before Her Grace and demonstrate their merit through combat and the three noble arts."
    cc "You just..."
    cc "Bah, I will explain later. Just try not to disgrace the court."
    show qw 91
    mc "I'll do my best."
    show qw 90
    cc "Follow me..."
    show qw 94 with dis17
    ele "*Whispering* Do you see it now, Thorund?" with dis15
    ele "*Whispering* Sylax was right."
    ele "*Whispering* That... is our only option."
    show qw 95
    tho ". . ."
    stop music2 fadeout 7
    scene black with dis3
    show screen afewminuteslater with dis25
    pause 
    hide screen afewminuteslater
    scene qs 1
    with dis27
    play music2b hyrilarsuitors
    pause 
    scene qs 2
    cc "*Clears throat* Attention, please!" with dis15
    cc "We are most grateful for your patience, ladies and gentlemen."
    cc "At last, all preparations are complete, and our honored guests are here."
    show qs 4
    cc "Therefore, without further delay, let the three suitors step forth!" with dis
    cc "Those who seek the throne of our realm and the hand of Lady Calypso, First of Her Name and Princess of the Sy-tel-quessir..."
    cc "Introduce yourselves!"
    play soundlow clothes3
    play sound6 leathershort volume 0.3 fadein 1
    scene qs 5
    bla "A young-looking elf enters the hall and dips into a fluid, elegant bow." with dis14 
    play sound7 crowdwhisper
    gua2 "*Whispering* That is the heir of Thirinvale!"
    enoble "*Whispering* They say he mastered thirteen instruments!"
    ewoman "*Whispering* By the Ancients... he is even more handsome than they say..."
    play soundlow clothes3
    play sound6 leathershort volume 0.3 fadein 1
    scene qs 6
    sui1 "Even the most vivid accounts of your beauty, Lady Calypso, have proven woefully incorrect in the presence of the truth." with dis12
    sui1 "I am Fael of Thirinvale — scion of a lineage as old as the stars, victor of the Sunlance Tournament, and the youngest elf in recorded history to claim such honor before his first century."
    show qs 10
    ca "We bid you welcome, Lord Fael."
    ca "It is an honor to have you in our presence."
    show qs 6
    sui1 "I stand before you to take your hand, Lady Calypso."
    sui1 "I seek to unite our noble houses, usher Hyril’ar into an era of brilliance it has yet to behold, and if I may be bold..."
    show qs 6b
    sui1 "...to see that the most beautiful woman in the realm is never without music, laughter, and... the kind of {i}attention{/i} that leaves her yearning for the night to never end." with dis
    show qs 10
    ca "U-Uh... I thank you, Lord Fael."
    ca "It would seem your reputation for wit and eloquence is most deserved."
    play soundlow clothes3
    play sound6 leathershort volume 0.3 fadein 1
    scene qs 8
    sui2 "I tremble before your radiance, Your Grace." with dis14 
    play sound7 crowdwhisper
    enoble "*Whispering* The House of Ilvenmyr! They came!"
    gua2 "*Whispering* I heard he led the charge at Maer’n Rock with nothing but a banner and blade."
    gua "*Whispering* If there’s any justice left in this world, he will be king."
    play soundlow clothes3
    play sound6 leathershort volume 0.3 fadein 1
    scene qs 9
    sui2 "I am Orym of Ilvenmyr, sworn sword of honor, heir to a house that has never bent knee to tyranny nor turned away from duty."with dis12
    sui2 "Long before Queen Anima the Radiant, our Houses were seen as one — united by blood, valor, and sacred vows."
    sui2 "I seek your hand not for glory, nor gain, but to restore that ancient bond which time has cruelly let wither!"
    show qs 10
    ca "We thank you and bid you welcome, Lord Orym."
    ca "It is an honor no less great to receive you within these halls."
    show qw 10b
    lo "I remember my father speaking of the House of Ilvenmyr and their prince."
    lo "He praised his integrity and said he bore the spirit of a true leader."
    play soundlow clothes3
    play sound6 leathershort volume 0.3 fadein 1
    scene qs 11
    sui3 "My Lady." with dis14 
    play sound7 crowdwhisper
    ewoman "*Whispering* Mother of Turska, do you see the size of that man?!"
    enoble "*Whispering* He is massive!"
    play soundlow clothes3
    play sound6 leathershort volume 0.3 fadein 1
    scene qs 12
    sui3 "I am Torion of Redveil, only son of the blood-hardened House of Redveil." with dis12
    sui3 "Choose me, Princess, and I shall give you sons and daughters born of fire and fury."
    sui3 "Children who will tower like oaks and march like storms!"
    sui3 "Commanders of legions!" with hpunchsubtle
    sui3 "Slayers of kings!" with hpunch 
    sui3 "{sc=2}Heirs to a realm reborn in strength!" with hpunch 
    show qs 13
    ca "U-Uh... th-thank you for your... most generous offer, Lord Torion."
    ca "It will be... taken under careful consideration."
    show qs 4
    cc "Thank you all for your presentations."with dis 
    cc "Now, in accordance with ancient tradition, you shall demonstrate your prowess by contending against a chosen champion of Hyril’ar."
    cc "Through this rite, Her Highness shall name the one deemed most worthy to claim her hand in union, securing the honor of your house and begetting heirs bearing the sacred bloodline of Queen Anima herself."
    show qs 14
    cc "So..." with dis
    cc "Yes, let the... {i}Champion{/i} enter."
    cc "Sir... Grothelborn."
    play sound armorwalk2
    scene qs 15 with dis2
    play sound2 crowdwhisper
    bla "The crowd steps aside to let you pass, as whispers quickly ripple through the onlookers like a rising wave."with dis15
    mct "I can feel the hate in their eyes. They can't stand me."
    mct "But Calypso's putting everything on the line for me. The least I can do is not screw this up, and prove them all wrong."
    scene qs 16
    mc "*Bowing down* My Lady." with dis12
    mc "You have my solemn vow — so long as I, Sir Grothelborn of Kredon, draw breath, I shall do all within my power to bring honor to our realm."
    show qs 17
    ca "Hmph."
    show qs 18
    ca "Of that I have no doubt, Sir Grothelborn."
    show qs 2
    cc "Remember that, regardless of the valor of our Champion, each of you must demonstrate your worthiness to stand beside the Princess."
    show qs 3
    cc "The future King of Hyril’ar must be a master of combat — graceful, precise, and unshakable in the heart of battle!" with dis
    show qs 3b
    mct "Alright, I got this."
    mct "I can already use my powers for a few seconds. Combine that with everything Arannis drilled into me, and this should be easy enough."
    show qs 3
    cc "So... today, to prove it, they will all demonstrate their expertise in archery with a longbow!" 
    show qs 3b
    mct "A longbow?!"
    mct "Fuck, then why the hell did I even bother grabbing a longsword?"
    show qs 3
    cc "And... of course, the chosen suitor will also have to prove their worth in the three noble arts."
    show qs 3b
    mct "Noble arts...?"
    show qs 4
    cc "Poetry."with dis 
    show qs 4b
    mct "Okay... things might be a bit more complicated than I thought after all."
    show qs 3
    cc "Painting."with dis 
    show qs 3b
    mct "...Yes, this is starting to look bad."
    show qs 4
    cc "And... music."with dis 
    show qs 4b
    mc ". . ."
    mct "I'm so fucking cooked."
    show qs 17
    cc "So, my Lady... we await your signal to begin."with dis 
    show qs 18
    ca "You may proceed, Lord Chamberlain."
    ca "I am most eager to witness what they shall bring forth."
    play sound clap
    show qs 2
    cc "Excellent!" with hpunch 
    cc "Then, without further delay, let the first challenge commence!"
    cc "I present to you..."
    play sound2 whoosh3b
    stop music2b fadeout 0.5
    play sound medievaltrumpet volume 0.6
    play music2 ["<silence 2.2>"]
    queue music2 suitors2
    scene poetry with pl
    pause 
    scene qs 3
    cc "Each of you, including our Champion, shall compose a single verse — four lines in total — dedicated to the Princess." with dis15
    scene qs 4
    cc "The theme, rhyme scheme, and meter are left entirely to your discretion, and you shall have but one minute to prepare."with dis 
    cc "Bare your soul before us!"
    show qs 4b
    mct "One minute?!"
    mct "What the hell is “scheme and meter” supposed to mean?!"
    scene qs 19
    bla "Barely a few seconds pass before the first suitor steps forward."with dis15
    scene qs 20
    sui1 "I am ready." 
    show qs 19
    mct "What?! Already?!"
    sui1 "*Clears throat* Mmm-mh." 
    scene qs 20
    show screen poem1a
    play sound whoosh9
    sui1 "She climbed me like a silver vine..." with dis
    show screen poem1b
    play sound2 whoosh9
    sui1 "Each gasp a verse, each thrust a line."
    show screen poem1c
    play sound3 whoosh9
    sui1 "In Hyril’ar, the stars descend..."
    show screen poem1d
    play sound4 whoosh9
    sui1 "To watch where moans and magic blend."
    play sound crowdwhisper
    play sound5 ["<silence 0.4>", applause2] volume 0.28
    scene qs 21 
    sui1 ". . ."with dis 
    hide screen poem1a
    hide screen poem1b
    hide screen poem1c
    hide screen poem1d
    show qs 25
    ca "Thank you, Sir Fael."
    ca "That was... remarkably bold, yet undeniably poetic in its expression."
    show qs 22
    tho "Indeed. A most evocative composition..."
    scene qs 23
    sui2 "*Clears throat* Mmm-mh." with dis12
    mc "*Writing down your poem* (What rhymes with Calypso...?)"
    mc "*Writing down your poem* (Hypno... torso...?)"
    show screen poem2a
    play sound whoosh9
    scene qs 24
    sui2 "A silver leaf drifts through the air..." with dis12
    show screen poem2b
    play sound2 whoosh9
    sui2 "The stars bow low to brush her hair."
    show screen poem2c
    play sound3 whoosh9
    sui2 "She walks where ancient rivers sleep..."
    play sound7 ["<silence 0.5>", crowdwhisper]
    play sound4 ["<silence 0.9>", applause2] volume 0.28
    show screen poem2d
    play sound5 whoosh9
    sui2 "And even night forgets to weep."
    hide screen poem2a
    hide screen poem2b
    hide screen poem2c
    hide screen poem2d
    scene qs 25
    ca "A fine piece, Sir Orym." with dis
    ca "Truly beautiful."
    show qs 22
    tho "I could not agree more."
    tho "Your father would be proud, young Orym."
    scene qs 26
    sui3 "*Clears throat* Mmm-mh." with dis12
    scene qs 27
    show screen poem3a
    play sound whoosh9
    sui3 "Humans charge with blades held wrong..." with dis 
    show screen poem3b
    play sound2 whoosh9
    sui3 "We chop them down before their song."
    show qs 26
    mct "W-What...?"
    show qs 27
    show screen poem3c
    play sound3 whoosh9
    sui3 "Their skulls make cups, their bones burn bright..."
    play sound6 ["<silence 0.5>", crowdwhisper]
    play sound5 ["<silence 0.9>", applause2] volume 0.28
    show screen poem3d
    play sound4 whoosh9
    sui3 "Their children squeal — what pure delight!"
    hide screen poem3a
    hide screen poem3b
    hide screen poem3c
    hide screen poem3d
    scene qs 28
    ele "*Chuckles* I like this one." with dis
    ele "A striking piece, Sir Torion."
    show qs 31
    ca "That was... quite visceral."
    ca "And yet... also beautifully crafted, I must confess."
    ca "Thank you, Sir Torion."
    scene qs 14
    cc "And finally..." with dis 
    cc "Sir Grothelborn?"
    cc "I am afraid I must urge you to proceed. Her Highness cannot dedicate the entire day to this matter."
    cc "So I must ask, present your poem, or... step aside with grace, please."
    cc "If need be, I shall offer the court's apologies for failing to produce a worthy champion from our own house, in the name of–"
    play soundlow armorwalk
    scene qs 29
    mc "*Taking a step forward* No one's retiring today, dingleberry." with dis2
    mc "*Clears throat* Mmm-hm-mhh." 
    mc "*Clears throat* Mmmrh."
    mc "Uh..."
    show screen poem4a
    play sound whoosh9
    mc "I brought her flowers. She brought light."
    menu:
        with dis
        "Tralalero tralala":
            show screen poem4b1
            play sound2 whoosh9
            mc "Tralalero tralala." with dis12
        "[gr]My hands shook hard, her eyes were bright":
            show screen poem4b2
            play sound2 whoosh9
            $ poemgood += 1
            mc "My hands shook hard, her eyes were bright." with dis12
        "I tried to flirt, she barked “Alright”":
            show screen poem4b3
            play sound2 whoosh9
            mc "I tried to flirt, she barked “Alright.”" with dis12
        "Her teeth are bright like white moon night":
            show screen poem4b4
            play sound2 whoosh9
            mc "Her teeth are bright like white moon night." with dis12
    show screen poem4c
    play sound3 whoosh9
    mc "Calypso smiled, and that was all..."
    menu:
        with dis
        "O porcodioe o porcuala":
            show screen poem4d1
            play sound4 whoosh9
            mc "O porcodioe o porcuala." with dis12
        "But I am dust, and she is grace":
            show screen poem4d2
            play sound4 whoosh9
            mc "But I am dust, and she is grace." with dis12
        "Let's go watch Better Call Saul":
            show screen poem4d3
            play sound4 whoosh9
            mc "Let's go watch Better Call Saul." with dis12
        "[gr]Enough to make a soldier fall":
            show screen poem4d4
            play sound4 whoosh9
            $ poemgood += 1
            mc "Enough to make a soldier fall." with dis12
    mc ". . ."
    play sound2 ["<silence 1.1>", crowdcough]
    show qs 30
    mc ". . ." with dis12
    mc "That's it."
    hide screen poem4a
    hide screen poem4b1
    hide screen poem4b2
    hide screen poem4b3
    hide screen poem4b4
    hide screen poem4c
    hide screen poem4d1
    hide screen poem4d2
    hide screen poem4d3
    hide screen poem4d4
    $ mcshort = mc[:2]
    if poemgood >= 2:
        scene qs 31b
        ca "That was not bad at all!"
        ca "Surprisingly decent, [mcshort]...u-um...s-sir... Grothelborn."
        ca "I must say, I am pleasantly surprised."
        $ calypso_points += 1
    else:
        scene qs 31
        ca "That was... not without merit."
        ca "The rhymes could benefit from a touch more refinement, but... well done."
        ca "Thank you, Sir Grothelborn."
    show qs 14
    cc "Yes... thank you, Sir Grothelborn." with dis
    if poemgood >= 2:
        cc "That was not bad indeed..."
    show qs 3
    cc "And thus, I believe that concludes our exhibition of the first noble art."with dis
    cc "Each suitor has surely demonstrated swiftness of wit!"
    cc "But now, we turn to a different virtue... patience!"
    cc "Let us proceed to the next discipline!"
    cc "That is..."
    play sound2 whoosh3b
    $ renpy.music.set_volume(0.1, delay=0.3, channel='music2')
    play sound medievaltrumpet volume 0.6
    scene painting with pl
    pause 1.5
    $ renpy.music.set_volume(0.7, delay=3.0, channel='music2')
    pause 
    scene qs 32
    cc "I trust all present are already acquainted with this." with dis15
    cc "Each suitor shall be granted a blank canvas, along with a set of paints imported from the Southern Realms, with which to display the Second Noble Art in its highest form."
    show qs 33
    sui2 "How much time do we have?"
    sui1 "Are we free to choose our theme?"
    show qs 32
    cc "Indeed, the theme is entirely at your discretion."
    cc "And you shall have one full hour to conjure forth your vision."
    show qs 33
    mct "Oh god..."
    show qs 32
    cc "So, if there are no further questions... let the challenge commence!"
    cc "Make love to the canvas and let it feed upon your passion!"
    cc "Good luck!"
    play sound ["<silence 1>", chair2]
    play sound2 chairmove
    show qs 34 with dis2
    bla "One by one, each of you takes a seat before a canvas and begins to paint." with dis15
    mct "Alright... painting time."
    mc "Hmm."
    mct "Dammit, I wish Nancy were here instead."
    mct "I’m sure she’d crush this."
    show qs 35
    mct "But... well, at least I've got one hour."with dis12
    if novapath:
        mct "I should be able to come up with something. Nova gave me a few tips."
        mct "It was for drawing manga, but... better than nothing, I guess."
    else:
        mct "I should be able to come up with something."
    show qs 34
    mct "Now, what should I paint...?" with dis12
    mc "Hmm..."
    menu: 
        with dis12
        "[gr]Calypso":
            mct "Hmm, it's a tournament held in Calypso's honor."with dis08
            mct "It makes sense to draw her."
            mct "And I even have her as a reference, since she's standing right there."
            mct "Besides... if anything is going to inspire me, it’s definitely her."
        "A horse":
            $ paintingcalypso += 1
            mct "Perhaps I should play it safe and draw something simple like a horse."with dis08
            mct "No one could possibly take offense at that, and it’s certainly easier than drawing a human face."
        "General Arannis":
            $ paintingcalypso += 2
            mct "I should go with Arannis."with dis08
            mct "I've spent so many hours training with him that I've memorized his face."
            mct "And since I’m wearing the royal guard’s armor myself, I can get the details just right."
    mct "Yes... yes, I can see it now!"
    mct "The canvas is speaking to me!"
    scene qpai 1 with dis25
    bla "You begin to paint as Calypso drifts around the court, her dull conversations with the gathered nobles stretching into the passing minutes." with dis2
    play sound chair2
    scene qpai 2
    ca "*Sighs* By the Ancients... I had nearly forgotten how exhausting these things can be." with dis14
    ca "I need a moment of silence."
    scene qpai 3
    tho "*Overhearing a nearby exchange* Ah, Lord Virelle!"with dis
    tho "How many decades has it been since last we crossed paths?"
    enoble "Too many, Lord Thorund, far too many. But I could not possibly forgo the occasion of Her Highness’ return, naturally."
    enoble "I am pleased to see she still bears herself with the grace one would expect — beautiful, compliant, and quiet."
    tho "*Chuckles* But of course, just as one would hope."
    tho "Tell me, Lord Virelle... does your son still remain unwed?"
    ca ". . ."
    show qpai 4
    ca "*Exhales* . . ." with dis 
    play sound chair2
    scene qpai 5
    lo "Taking a moment of respite, Your Grace?" with dis14
    lo "Might I be of service in any way? Perhaps some tea? Water? More comfortable shoes?"
    show qpai 6
    ca "*Soft chuckle* Your concern is appreciated, Lorelei, but there is no need."
    show qpai 7
    lo "But of course, Your Grace!"
    lo "It is my solemn duty to ensure that your every need is met, no matter how small."
    lo "And when I saw the weariness upon your face, I knew at once that something was amiss!"
    show qpai 6
    ca "Ever observant, as always."
    ca "But I am well, no need to worry."
    ca "Merely..."
    show qpai 8
    ca "*Sighs* Do not mind me, really."with dis08
    ca "I would not want to burden you with trivial matters."
    show qpai 9 
    lo "There is no such thing as a trivial burden when it concerns you, Your Grace!"
    lo "You may confide in me freely. Speak your heart without restraint!"
    lo "I shall keep your words safe with me and never say a thing to anyone!"
    show qpai 6
    ca "Thank you, Lorelei."
    ca "I truly appreciate your loyalty and attentiveness over the years."
    ca "Truthfully, I have come to think of you as the sister I was never granted. You may always speak freely with me as well."
    show qpai 7
    lo "Y-You honor me beyond words, Your Grace!"
    show qpai 8
    ca "*Quietly* Well, if you truly want to know..." with dis08
    ca "Between the two of us, I can hardly wait for all of this to be over."
    ca "These endless ceremonies were never to my liking, but now, after spending so much time among humans..."
    ca "I despise them more than ever."
    show qpai 9
    lo "Are human ceremonies so different, Your Grace?"
    show qpai 8
    ca "Perhaps not with {i}all{/i} humans, but... at least with [mc] and his harem, they are indeed so."
    ca "They have no need for pomp or protocol. They speak their minds openly, without veil or pretense."
    ca "Of course, they still have some secrets, but there is always a kind of... unvarnished honesty in their ways."
    show qpai 9
    lo "That does sound very nice."
    show qpai 8
    ca "I must admit it is, yes."
    ca "Here, every word feels rehearsed, every gesture calculated."
    ca "Smiles that do not reach the eyes, and... bows that mean nothing."
    show qpai 9 
    lo "Do you miss those days of adventure with Lord [mc], Your Grace?"
    show qpai 8
    ca "Hah... good question."
    ca "I suppose I do, yes. In many ways."
    show qpai 10
    ca "I was always hesitant to engage with humans, even during my travels to other worlds. And yet, with [mc]..."
    ca "It was... different. Speaking with him felt natural. Simple."
    ca "As if... for the first time, someone truly listened."
    show qpai 9 
    lo "I see you forged a real connection with him."
    show qpai 10
    ca "I... suppose so."
    ca "In the end, I even ended up revealing far more of myself to him than I ever imagined I would."
    show qpai 8
    ca "Far more, I must admit..." with dis08
    play sound woodhit volume 0.8
    show qpai 11
    lo "Y-You mean... on an intimate level?!" with hpunch 
    show qpai 12
    ca "E-Excuse me?"
    show qpai 11
    lo "D-Did he see your form in full? W-Without garments, I mean?!"
    lo "Did you two ever..."
    show qpai 13
    ca "B-By the Ancients, Lorelei, lower your voice!"with hpunchsubtle
    show qpai 12
    ca "*Quietly* And n-no! That is not what I meant!"
    ca "What kind of scandalous question is that?!"
    ca "Such a thing w-would have been a crime! It is strictly forbidden!"
    show qpai 16
    lo "O-Oh... of course. Naturally." with dis
    show qpai 19
    ca "I did not..."with dis08
    ca "I-I would never permit him to see me in {i}that{/i} way."
    show qpai 11
    lo "Then..."with dis 
    lo "Might I ask if... {i}you{/i} have seen {i}him{/i} in such a state?"
    show qpai 12
    ca "Lorelei!" with hpunchsubtle
    show qpai 16
    lo "M-My deepest apologies, Your Grace."with dis 
    lo "I-I merely possess a keen interest in human biology."
    lo "We were always taught that they are as hairy as woodland beasts, barely capable of intelligible speech, and..."
    lo "A-And yet Sir [mc] conducts himself with eloquence, and bears the appearance of an elf under ninety."
    show qpai 17
    ca ". . ."
    show qpai 18
    ca "*Soft sigh* Hmph."with dis08
    show qpai 19
    ca "I... suppose I cannot fault you for your curiosity."
    ca "I, too, have fallen prey to such wonderings in the past."
    show qpai 14
    ca "So... I will say only this: due to the demands of our shared missions... and... under certain completely unavoidable circumstances..."with dis
    ca "...Yes, I might have, on occasion... glimpsed him in an undressed state."
    show qpai 15
    lo "Ohh..."
    lo "And... was he truly as beastly as the old scholars say? Covered in fur?"
    show qpai 14
    ca "You already saw his torso during the sparring match with your father."
    ca "He is quite... smooth by nature."
    show qpai 15
    lo "E-Everywhere?"
    show qpai 20
    ca ". . ."
    show qpai 14
    ca "I believe... he maintains himself quite meticulously."
    ca "He removes any excess hair. Just as we do."
    show qpai 15
    lo "So... his..."
    lo "*Whispers* Genitalia are identical to ours?"
    show qpai 14
    ca "Of course. How else do you imagine the Peredhil are conceived?"
    show qpai 15
    lo "Oh... naturally."
    show qpai 20
    lo ". . ."
    ca ". . ."
    show qpai 15
    lo "A-And... if I may ask..."
    lo "How... was it?"
    show qpai 14
    ca "How was... {i}what{/i}?"
    show qpai 15
    lo "Like..."
    lo "Is he... well-endowed...?"
    show qpai 12
    ca "LORELEI!" with hpunch 
    show qpai 16
    lo "F-F-Forgive me, Y-Your Grace!"with dis
    lo "T-That question was entirely improper and unbecoming."
    show qpai 16b
    ca "What happened to you after I left?"
    show qpai 16
    lo "It is simply that... a-after over a decade of monotony and boring conversations, even the slightest novelty overwhelms me with curiosity."
    lo "B-But I still recognize that my behavior was indecent and unacceptable."
    lo "I shall accept whatever punishment you deem appropriate."
    lo "P-Please, forgive me."
    show qpai 17
    ca ". . ."
    lo ". . ."
    show qpai 18
    ca "Hmph."with dis 
    ca ". . ."
    show qpai 19
    ca "It was..."
    show qpai 20
    lo ". . ."with dis 
    show qpai 14
    ca "It was..."
    ca "*Ahem* ...R-Rather impressive in size, yes."
    show qpai 15
    lo "Ohh..."
    lo "I-I... I see."
    lo "I see."
    lo "T-Thank you for... satiating my curiosity, Your Grace."
    lo "That was... t-the last of my questions, I promise."
    show qpai 20
    ca "Hmph."
    show qpai 21
    cc "Very well, gentlemen, the time is over!"with dis08
    show qs 66_2
    cc "Time to show the Princess what you have created!" with dis 
    cc "We will be–"
    play sound runsit
    show qs 66_3
    bla "Lorelei rushes to her seat besides the other maids, briefly interrupting the Lord Chamberlain mid-sentence." with dis17
    cc ". . ."
    show qs 66
    cc "Where was I... ah, yes!"with dis08
    cc "We will begin with... Sir Torion!"
    cc "So please, good sir..."
    play sound footsteps4
    show qs 37 with dis2
    bla "The Lord Chamberlain and Calypso make their way to the corner where Sir Torion was quietly painting." with dis15
    show qs 39
    cc "Ohh..."
    show qs 38
    cc "What exquisite work, Lord Torion!"
    cc "The level of detail in the knight’s armor is nothing short of mesmerizing."
    ele "Beautiful indeed. Who does this depict?"
    sui3 "My grandfather, Yslad'ar of Redveil."
    sui3 "This piece commemorates the War of the Iron Footsteps, when the legions of Redveil repelled the final great incursion of humans along our southern border."
    sui3 "Under his command, our legions purged the invaders to the last, eradicating the human presence from the continent."
    ele "Truly beautiful."
    ca "But..."
    show qs 39b
    ca "That does not resemble a human."
    ca "It looks more like some sort of monster."
    show qs 40
    cc "It is merely symbolic, My Lady. Lord Torion utilized the image of a demon to convey the perceived malevolence of humankind."
    cc "Such allegory is common in the art traditions of Redveil."
    show qs 38
    ca "Ah... yes, of course."
    cc "Let us proceed to the next suitor! Though I daresay this entry shall be difficult to surpass."
    sui3 "Thank you, Lord Chamberlain."
    play sound footsteps4
    scene qs 43
    cc "Very well... let us see the next one..."with dis17
    show qs 42
    cc "Ah! Is that Iskhaldrim I see?"
    sui2 "Indeed, it is, my Lord."
    ca "How delightful! I recognize my chambers, the main hall..."
    ca "And even the Usurper's Keep to the left, where we now stand!"
    ca "Have you visited Iskhaldrim before, Lord Orym?"
    sui2 "I have not, Your Grace. This is my first time setting foot within its limits."
    ca "Then I must commend you. Your eye for detail is most impressive."
    sui2 "You honor me, Your Grace."
    cc "Exquisite work, Lord Orym!"
    cc "Let us see the last one!"
    play sound2 footsteps4
    scene qs 44
    cc "Hmmm...?" with dis17
    show qs 45
    cc "Ah, just look at those strokes..."
    cc "This borders on perfection, Sir Fael!"
    show qs 48
    sui1 "You are most kind, Lord Chamberlain."
    sui1 "I chose to depict myself adorned in the royal regalia as a vision of what the future may hold."
    sui1 "*Chuckles* And... perhaps, an opportunity to show Her Highness that her future husband could match her own beauty."
    show qs 46
    cc "Oh, that was a daring move, Sir Fael!"
    cc "The Princess, as we know, holds the privilege of choosing her consort by her own will."
    cc "But... ambition and confidence are admirable traits for any would-be king."
    cc "I have no doubt Her Grace will take this under careful consideration."
    show qs 48
    sui1 "Thank you, My Lord."
    show qs 45
    cc "Another remarkably close contest!"
    cc "At this pace, it shall prove no easy task for Her Highness to make her choice."
    cc "But now, let us proceed to–"
    ca "Wait, what of our Champion?"
    ca "We should see what he has painted as well, must we not?"
    cc "Oh..."
    cc "Y-Yes, but of course, Your Grace."
    play sound footsteps4
    show qs 49
    cc ". . ." with dis17
    mc ". . ."
    if paintingcalypso == 0:
        show qs 50
    elif paintingcalypso == 1:
        show qs 50b
    elif paintingcalypso == 2:
        show qs 50c
    cc "What is that...?"
    if paintingcalypso == 0:
        show qs 50
        mc "Princess Calypso."
        mc "I didn't mean to cut off her forehead like that, but I started from the bottom and ran out of space at the top."
        cc "I... I do see how it may resemble Her Grace."
    elif paintingcalypso == 1:
        show qs 50b
        mc "A horse."
        mc "I had to redo the legs, like, three times. They kept coming out super weird."
        cc "I... I do see a horse."
    elif paintingcalypso == 2:
        show qs 50c
        mc "General Arannis."
        mc "I painted him smiling at first, but that didn't really look like him, so I had to go back and change it."
        cc "I... I do see how it may resemble General Arannis."
    cc "But why does it appear to have been painted by a child?"
    mc "What??"
    show qs 52
    mc "Dude, you're such a hater." with dis
    show qs 51
    cc "Are you mocking the sanctity of this event?"
    show qs 52
    mc "What? Of course not, I’ve never painted before! I really tried my best here."
    mc "It already came out way better than I thought it would!"
    show qs 51
    cc "It is hideous."
    show qs 53
    ca "I like it." with dis12
    ca "I had no idea you possessed such raw artistic spirit, Sir Grothelborn."
    ca "None of our eighteen-year-old toddlers could achieve the depths of these brush strokes."
    show qs 54
    mc "Hah! Did you hear that, Chamberlain?"
    mc "Thank you, Your Grace."
    mc "That seriously means a lot coming from you."
    show qs 55
    cc "Y-Your Grace, I understand your desire to be courteous, but surely this... this thing is not worthy of your gaze."
    cc "I shall have it sent to the incinerator at once."
    show qs 56
    ca "You will do no such thing. I am serious."
    if paintingcalypso == 0:
        $ calypso_points += 1
        ca "At least Sir Grothelborn painted {i}me{/i}, as was the purpose of the challenge."
        ca "That alone speaks volumes, beyond any painting technique perfected over centuries."
    else:
        ca "Sir Grothelborn has not had centuries to master the brush."
        ca "That he painted anything of merit, with no prior experience and no time for preparation, is already worthy of acknowledgment."
    show qs 57
    cc "Oh, w-well..."
    cc "O-Of course, Your Grace. That is... a fair point."
    cc "But, still..."
    show qs 56
    ca "Enough. I have spoken."
    ca "Let us move on to the next challenge."
    ca "This one has already exceeded its allotted time."
    show qs 57
    cc "O-Of course, My Lady."
    cc "Please, forgive me."
    show qs 57b
    cc "*Clears throat* A-Attention, please!" with dis
    cc "Thank you all for your patience!"
    cc "The time has come to proceed to the third discipline — yet another noble art, long revered within our halls!"
    cc "I present to you..."
    play sound2 whoosh3b
    $ renpy.music.set_volume(0.1, delay=0.3, channel='music2')
    play sound medievaltrumpet volume 0.6
    scene music with pl
    pause 1.5
    $ renpy.music.set_volume(0.7, delay=3.0, channel='music2')
    pause 
    scene qs 58
    cc "King Erevan once declared he would trade his crown for one true lullaby." with dis15
    cc "Today, we honor him the way he would have wanted — by playing his favorite instrument!"
    show qs 59
    cc "The lyre!" with dis12
    mct "Oh god..."
    show qs 58
    cc "Each suitor shall now improvise a song from the depths of his soul, and perform it for our Princess!" with dis12
    cc "Just as with the paintings, the style is for you to choose!"
    cc "So pour your hearts into the strings, and dazzle us all!"
    scene qs 59
    cc "If you agree, we shall begin with Lord Torion once more."with dis12
    sui3 "Of course."
    cc "May the Ancients bless you with divine inspiration!"
    play soundlow wood2
    scene qs 60 with dis15
    bla "Lord Torion sits onto the log and picks up the lyre with a weary touch." with dis12
    sui3 "Hmmm..."
    show qs 61
    mct "Okay... that's good."
    mct "He's looking at it like he's never seen a lyre."
    mct "From what I've seen, this guy's like a walking war crime, not a musician."
    mct "If this goes badly for him, I might stand a chance..."
    show qs 60
    sui3 ". . ."
    play sound inhale2
    stop music2 fadeout 2
    play soundloop fireplace fadein 2
    scene qs 62c
    sui3 "*Taking a deep breath* Hhhhhm." with dis14
    play music lyresong1
    scene sui3lyre 
    sui3 ". . ."
    scene qs 61
    mc ". . ."
    mct "I'm dead meat." 
    scene sui3lyre
    bla "Lord Torion begins to perform a breathtaking melody, his fingers dancing with such masterful precision it feels as though he’s playing several instruments at once." with dis2
    sui3 ". . ."
    stop music fadeout 5
    play musicb lyresong2 fadein 3
    scene sui2lyre 
    sui2 ". . ." with dis25
    mc ". . ."
    stop musicb fadeout 5
    play musicnoloop lyresong3 fadein 3
    play soundlow lyresong3 fadein 3
    scene sui1lyre with dis25
    pause 7
    scene qs 65 with dis12
    play sound crowdwhisper
    play sound5 ["<silence 0.4>", applause2] volume 0.36
    cc "Sublime!" with dis
    scene qs 66
    cc "An exquisite performance, Sir Fael, exquisite!"
    cc "All three of you!"
    cc "I have watched many noble suitors over the years try to win our Princess' heart, but never have we had such talent!"
    cc "And precisely when we are most in need!"
    scene qs 66b
    ca "Indeed, my Lords."
    ca "Your skill with the lyre was impressive."
    ca "For a moment, I felt transported far from this court, lost in the melodies."
    scene qs 67
    cc "Now... it is time for the performance of our Champion."with dis
    cc "Uh..."
    cc "He... spent most of his rather brief two-century life abroad in... Nimvyr."
    cc "So if his music sounds a little... unconventional, please bear with us."
    cc "Uh... regardless, Sir Grothelborn... if you would?"
    play soundlow wood2 
    scene qs 68 with dis15
    bla "You slowly pick up the lyre and sit on the log, the quiet anticipation of the court pressing in around you." with dis12
    mc "*Clears throat* Ahem."
    mc "*Clears throat* Hmmph."
    mc ". . ."
    default lyrebg = "images/09/qs 68.jpg"
    mod "You can do c-c-g'-g'-a'-a'-g' sequence before stopping for a flashback."
    show screen lyreharpscreenexit
    call screen lyreharpscreen with dis17
label lyreend:
    if "ccg'g'a'a'g'" in lyresequence: 
        hide screen lyreharpscreenexit
        play soundlow glitch4
        scene caveglitch2
        pause 0.12
        id "{sc=8}Break the chain.{w=0.02}{nw}"
        pause 0.12
        id "{sc=8}Break the chain.{w=0.02}{nw}"
        pause 0.12
        scene qs 68
        pause 0.01
    play sound2 ["<silence 1.2>", crowdcough]
    hide screen lyreharpscreenexit
    scene qs 70
    mc ". . ." with dis15
    scene qs 70b
    ca ". . ."
    scene qs 70
    mc ". . ."
    mc "I'm done."
    play music2 suitors2
    play sound impact5
    stop soundloop fadeout 20
    scene qs 71
    cc "What do you mean, you're {i}done{/i}?!"with hpunch 
    if lyrenotesplayed == 0:
        cc "You didn't play a single note!" with hpunch 
    elif lyrenotesplayed == 1:
        cc "You only plucked one sad little string!" with hpunch 
    elif lyrenotesplayed <= 8:
        cc "You only played a couple of notes!" with hpunch 
    else:
        cc "You just committed murder against that lyre!" with hpunch 
    show qs 70
    mc "Uh... y-yeah, well..."
    mc "This is how we jam in Nimvyr."
    mc "It's called post-harmonic... deconstructionism."
    mc "I guess you guys aren’t ready for that yet, but your kids are gonna love it."
    show qs 71
    cc "What?!"with hpunch 
    cc "Are you calling me old?!"with hpunchsubtle
    show qs 72
    ca "I... believe we should refrain from judging foreign musical customs."with dis 
    ca "It was a... memorable contest, in any case. Perhaps we should simply move forward."
    show qs 71
    cc "You little piece of–"
    show qs 72
    ca "Lord Chamberlain?"
    cc "Uh–"
    show qs 67
    cc "*Clears throat* Uh..." with dis
    cc "Y-Yes... yes, of course, Your Grace."
    cc "Let us... graciously forget about that... unique interpretation."
    cc "Please, forgive me."
    show qs 66
    cc "*Clears throat* Attention, nobles and guests!" with dis08
    cc "Our suitors have now demonstrated their talents in three noble arts!"
    cc "We are almost done, but one final trial remains... the greatest art of all!"
    cc "Combat!"
    mct "Finally!"
    cc "The next challenge is..."
    play sound2 whoosh3b
    stop music2 fadeout 0.5
    play sound medievaltrumpet volume 0.6
    play music2 ["<silence 2.4>"]
    queue music2 hyrilarsuitors
    scene archery with pl
    pause 
    scene qs 73
    cc "For this final trial of skill, you shall each be granted a Hyril'ar longbow." with dis15
    cc "I hold no doubt that, given a few moments to acquaint yourselves with its weight and balance, many of you could strike the inner ring with ease... but today, there shall be no second chance!"
    cc "You will have but ONE attempt to strike the mark!"
    cc "So you will have to gauge the weight of the bow, and trust your instincts to guide your aim true!"
    show qs 75
    cc "Each of you shall wield the very same bow and a single, identical iron arrow, ensuring that no hand receives favor over another!" with dis12
    cc "Now then, Lord Fael..."
    cc "Would you do us the honor of being the first?"
    show qs 74
    sui1 "With pleasure, Lord Chamberlain."
    sui1 "I shall strike this target as surely as I would strike the heart of Princess Calypso herself."
    show qs 73
    cc "Very well, then!"
    cc "May fortune favor your hand, and your aim be as true as your words!"
    scene qs 75
    cc "One arrow..."
    cc "One breath..."
    cc "One chance to etch your name into the memory of this court!"
    sui1 "*Chuckles* Mm-mh."
    play sound bow
    scene qs 76
    bla "The suitor grabs the arrow and draws the bowstring tight, holding his breath as he takes aim." with dis15
    sui1 ". . ."
    play sound arrow2
    scene qs77 with hpunch
    play sound2 crowdwhisper
    play sound3 ["<silence 0.4>", applause2] volume 0.28
    pause
    scene qs 77b
    cc "Aaahh... right on the blue ring!" with dis
    cc "A most commendable shot, Lord Fael!"
    show qs 77c
    cc "The question is, will it be enough to win the Princess' heart?"
    scene qs 78
    sui1 "Tsk..." with dis
    sui1 "*Mumbling* I knew I should have aimed higher."
    sui1 "*Mumbling* Hyril'ar bows are always too heavy."
    show qs 77c
    cc "Lord Orym, you may proceed!"with dis
    cc "Let us witness what you are capable of!"
    show qs 79
    bla "Lord Fael passes the bow to the next suitor as he moves into place." with dis15
    sui2 "Hmm..."
    play sound bow
    scene qs 80
    sui2 ". . ." with dis15
    sui2 "Hmmmph..."
    play sound arrow2
    scene qs81 with hpunch
    play sound2 crowdwhisper
    play sound3 ["<silence 0.4>", applause2] volume 0.28
    pause
    scene qs 77b
    cc "An even better shot from Lord Orym, proving his reputation is clearly no exaggeration!" with dis
    cc "Truly splendid!"
    show qs 81b
    sui2 "Thank you, my Lord."
    show qs 81c
    cc "Tell us, what is your secret?!"
    show qs 81b
    sui2 "Well, I would say it simply lies in sensing the weight of the bow before one lets loose the arrow."
    show qs 81c
    cc "You heard it, ladies and gentlemen!"
    cc "Now you know what it takes!"
    show qs 81b
    sui2 "*Chuckle* I would not say that is {i}all{/i} it takes."
    sui2 "A true general must master every art of war, if he wants to demand the respect of his men."
    sui2 "But if the bond between our houses is rekindled, I vow to lead the armies of Hyril’ar to the greatness they once knew."
    show qs 81c
    cc "Of that, I have no doubt, good sir!"
    show qs 78b
    ca "I must admit, their marksmanship is truly impressive." with dis12
    show qs 78c
    lo "It really is."
    lo "My father often says that even an experienced archer finds it difficult to adapt to a new bow and unfamiliar arrows."
    lo "To hit the target at over fifty strides on one’s first attempt is no small feat."
    show qs 78b
    ca "Indeed..."
    ca "I remember that this same trial was given to the earliest suitors who sought my hand when I was but forty-six, and not a single one managed to strike the target."
    show qs 82
    bla "Lord Orym passes the bow to the last suitor." with dis14
    cc "Your rivals have certainly set a daunting standard, Lord Torion!"
    cc "But I see determination in your eyes!"
    cc "Good luck!"
    sui3 "Hmph."
    play sound bow
    scene qs 82b
    sui3 ". . ." with dis15
    play sound arrow2
    scene qs83 with hpunch
    play sound2 crowdwhisper
    play sound3 ["<silence 0.4>", applause2] volume 0.28
    pause
    scene qs 77b
    cc "Unbelievable!" with dis
    cc "Lord Torion has nearly hit the very center of the target!"
    cc "Such precision would be impressive even from an archer who had been training with the same bow since dawn!"
    show qs 84
    sui3 "Mmmrrrhhh..."
    show qs 85
    sui3 "*Grumbling* I should have struck dead center."
    show qs 77c
    cc "Three magnificent shots..." with dis12
    cc "But now, as is tradition, our Champion shall deliver the final shot!"
    cc "Alas, it is near impossible for him to surpass Lord Torion’s score."
    cc "Nevertheless... Sir Grothelborn, the field is yours!"
    play soundlow armorwalk
    show qs 86
    bla "Lord Torion hands you the bow as you step into position." with dis2
    mct "Hmmm..."
    mct "This thing’s way heavier than any bow I’ve used before."
    mct "Not that I’ve had much practice anyway... just a handful of days at most."
    mct "Still, I’ve gotta give it my all."
    mct "My life’s not on the line, sure, but Calypso stuck her neck out for me... right in front of the whole court."
    mct "So... if you're out there, goddess of fortune..."
    mct "Imma need your help once more."
    play sound bow
    scene qs 87 with dis15
    scene qs87
    mc ". . ." with dis12
    mct "H-Holy fuck. T-This thing's so hard to pull all the way back."
    mct "A-And why the hell is it so heavy??"
    mct "What is this made of, platinum?!"
    menu:
        with dis
        "[gr]Activate your powers":
            play sound2 transformpower
            $ ballbowspeed = True
            scene qs 87 with dis17
            mct "Yes... that's better." with dis 
            mct "My pulse is perfectly steady now."
            mct "I can see... everything more clearly."
        "Don't activate it":
            mct "F-Fuck no."with dis
            $ calypso_points += 1
            mct "I-I'm not using my p-powers for this."
            mct "I-It's a matter of... f-fucking pride now."
    call screen ball_minigame with dis14
label ball_continue:
    if score > 0:
        jump ball_success
    elif score < 0:
        jump ball_fail
label ball_success:
    $ hittargetbow = True
    $ calypso_points += 1
    play sound arrow2
    scene qs88 with hpunch
    play sound3 ["<silence 0.4>", applause2] volume 0.28
    jump ballbowafter
label ball_fail:
    play sound arrow2
    scene qs88b with hpunch
    jump ballbowafter
label ballbowafter:
    play sound2 crowdwhisper
    pause
    if hittargetbow:
        scene qs 89
        cc ". . ." with dis12
        cc "U-Unbelievable..." 
        cc "The hu..."
        cc "T-The Champion struck the very center of the target."
        scene qs 91
        ca "Not bad, Sir Grothelborn... not bad at all."
        ca "That was..."
        scene qs 92
        ca "Very impressive, I must admit." with dis
        ca "You have truly proven yourself worthy as the Champion of Hyril’ar."
        play sound2 leathershort volume 0.3 fadein 1
        show qs 93
        mc "*Bowing down* It was my honor, Your Grace." with dis14
        mc "No knight of Hyril’ar could fail to be moved when the Princess chooses him as her Champion."
        show qs 92
        ca "A decision I find myself regretting less with each passing moment."
        scene qs 89
        cc "The perfect center..." with dis
        cc "He even displaced Lord Torion’s arrow with his own."
        cc ". . ."
        scene qs 90
        cc "B-But this is no mere stroke of fate, of course!" with dis12
        cc "Let that stand as a testament to the skill of Hyril’ar’s archers!" 
        cc "The three suitors have proven themselves worthy of seeking the Princess’ hand... and yet, it seems Hyril’ar always stands a step above!"
    else:
        scene qs 77c
        cc "And... as was expected, our Champion's arrow struck beyond the outer ring."with dis12
        mct "Dammit..."
        scene qs 90
        cc "But this is no mere stroke of fate!" with dis12
        cc "Let this serve as a testament to the skill and valor of the noble knights who have graced our lands today!"
        cc "All three suitors have proven themselves worthy of the Princess’ hand!"
        cc "Congratulations!"with hpunchsubtle
    show qs 77_2
    cc "Now, let us raise our cups and partake in the feast, my lords and ladies!" with dis12
    cc "For today is a day of celebration!"
    cc "Rejoice!" with hpunchsubtle
    play soundloop crowdtalk volume 0.4 fadein 5
    stop music2 fadeout 8
    scene qs 94 with dis3
    play music2b hyrilarhappy fadein 6
    bla "As servants begin to arrive bearing platters of food and nobles gather around Calypso, you quietly slip to the edge of the room."with dis22
    mct "Well, I guess my job here's done."
    mct "At the very least, Calypso looked relieved to have me by her side through all this thing."
    mct "But now I should head back to my chambers until she's done with all the talking, before one of the suitors figures out I'm not actually an elf."
    if hittargetbow:
        sui3 "Sir Grothelborn."
        scene qs 95
        mc "*Turning around* Hmm?" with dis12
        mc "A-Ah, Sir Torion."
        mc "I’d love to stay and enjoy the feast, but... I, uh... made a vow never to remove my helm in public."
        mc "To... my late wife."
        mc "Hope you understand."
        scene qs 96
        sui3 "I understand."
        sui3 "I merely wished to commend you on your skill with the bow."
        sui3 "Your shot was exceptional. Especially while bearing such heavy armor."
        show qs 95
        mc "Oh, why, thank you."
        show qs 96
        sui3 "I am aware my chances of being chosen by the Princess are slim, as my family does not hold the stature of Sir Fael's or Lord Orym's."
        sui3 "Still, should your path ever lead you to Redveil, you would be most welcome."
        sui3 "We always open our gates to knights of your caliber."
        show qs 95
        mc "Oh..."
        mc "Thank you kindly. I shall remember your generous offer."
        mct "Wow, I was not expecting that."
        mct "Maybe this guy’s not such a bad dude after all."
        mct "Aside from the whole “murder humans” part, maybe."
        show qs 96
        sui3 "If the rumors of civil war prove true, Redveil will stand with the crown."
        sui3 "We will not abandon our old allies."
        show qs 95
        mc "Uh..."
        mc "Thank you, my Lord."
        show qs 96
        sui3 "Farewell, good sir."
        show qs 95
        mc "Farewell."
        mct "Rumors of civil war? What was that about?"
        cc "*Clears throat* Sir Grothelborn?"
        show qs 97
        mc "*Turning around* Ah... Lord Chamberlain..." with dis12
    else:
        play sound footsteps
        show qs 98
        cc "Well, well, well..." with dis15
    show qs 97
    mc "Yes, yes, I'm leaving."
    mc "You don't have to worry about me anymore."
    show qs 98
    cc "Actually, I come bearing a message from the Princess."
    cc "She will spend the next few hours entertaining our guests and becoming better acquainted with the suitors, in order to make the most appropriate decision."
    cc "So she asked me to inform you that she will meet with you later in your chambers to... open a passageway to your homeland, before the day’s end."
    show qs 97
    mc "Ah, nice! That works for me."
    mc "I'm looking forward to going back home."
    cc "Mmh."
    show qs 98
    cc "I, too, look forward to your departure."
    show qs 97
    mc "Oh, come on..."
    mc "I didn't do that bad."
    cc "Hmph."
    show qs 98
    if hittargetbow:
        if poemgood >= 2:
            cc "Your painting was dreadful, and I am still recovering from your lyre “performance”."
            cc "But... your poem was not entirely awful, and your archery skills were surprisingly impressive, I will give you that."
            cc "Or, at least... impressively lucky."
        else:
            cc "Your painting was dreadful, your poem worse, and I am still recovering from your lyre “performance”."
            cc "But... your archery skills were surprisingly impressive, I will give you that."
            cc "Or, at least... impressively lucky."
    else:
        if poemgood >= 2:
            cc "Your painting was dreadful, your archery mediocre, and I am still recovering from your lyre “performance”."
            cc "But your poem was... surprisingly tolerable, I suppose."
            cc "For a human."
        else:
            cc "Your painting was dreadful, your poem worse, your archery mediocre, and I am still recovering from your lyre “performance”."
            cc "But... at least you did not kill anyone."
            cc "I should be thankful for that, I suppose."
    show qs 97
    mc "I'll take that as a compliment."
    mc "Thank you, Lord Chamberlain."
    cc "Hmph."
    show qs 98
    cc "Farewell... Sir Grothelborn."
    play sound footsteps
    show qs 94 with dis22
    mct "Alright then."with dis12
    mct "Guess I'll go take a nap until Calypso's done here."
    mct "Or... maybe I could squeeze in some longbow practice. I could use a bit more skill and a bit less luck next time."
    mct "Never a bad time to train."
    stop soundloop fadeout 7
    stop music2b fadeout 8
    scene black with dis3
    show screen afewhourslater with dis15
    pause
    play music2 hyrilarchill fadein 5
    scene qs 99
    hide screen afewhourslater
    with dis3
    pause
    play sound chair2 volume 0.7
    scene qs 100
    ca "*Sitting down* Oh, heavens..." with dis14
    ca "Finally, they've all left."
    ca "I never imagined that mere conversation could be so draining."
    show qs 101
    lo "It often is, Your Grace." with dis
    lo "Especially when your heart is not invested in the words being exchanged."
    show qs 102
    ca "Yes... that is very true, indeed."
    ca "Thank you for staying by my side through every tedious moment, Lorelei."
    show qs 101
    lo "But of course, Your Grace!"
    lo "I would have stayed even if it was not my sworn duty!"
    show qs 103
    ca "Are you sure about that? Or is it the allure of royal privileges that keeps you close?"
    ca "I did notice you indulging in more than one glass of the Rivanor wine Sir Fael brought."
    show qs 104
    lo "Absolutely not!"
    lo "I could have been here just as the general’s daughter, if I'd wanted!"
    lo "Suggesting otherwise wounds me deeply, Your Grace."
    show qs 102
    ca "*Chuckles* Alright, alright, I take it back."
    ca "My thanks, Lorelei... all the more heartfelt now."
    ca "You are free to retire for today. You have done more than enough."
    show qs 101
    lo "Do you need anything else before I go? I can stay longer if you wish."
    show qs 105
    ca "No... there’s nothing left for you to do. The rest depends solely on me now."
    ca "I must choose one of the three suitors to be... my husband."
    show qs 106
    ca "The future king of Hyril'ar..."
    show qs 101
    lo "How did your time with them go?"
    lo "I saw you speaking with each for quite a while."
    show qs 106
    ca "It was all terribly... ceremonial."
    ca "Each encounter, a different performance."
    play sound pop volume 0.66
    show qs 116b
    ca "{i}Lord Fael could hardly speak five sentences without hiding some crude innuendo in them. He promised me “passion and pleasure the likes of which I’d never known”."
    play sound pop volume 0.66
    show qs 116c
    ca "{i}Lord Orym was... dutiful. Almost too formal. He spoke of our families' ancient ties and how marriage would honor and restore them."
    play sound pop volume 0.66
    show qs 116
    ca "{i}And Lord Torion... he delivered a lecture more fitting for a war council."
    ca "{i}His every word was about strength, blood, glory, and the training of his warriors from the age of ten."
    lo "Oh..."
    show qs 108
    lo "I... see none of them exactly swept you off your feet, then."with dis14
    lo "Why not simply refuse them all? You have turned down proposals before."
    show qs 105
    ca "Because the stakes are different this time."
    ca "My advisors told me that Hyril’ar stands on the brink of war. My absence has only exacerbated the unrest."
    ca "Tensions rise on all borders, and there are whispers that some of the old Houses may soon turn against us."
    ca "If I marry the heir of one of those Houses, I might... be able to hold the unity of the kingdom."
    ca "And perhaps... it is what I owe after all these years away."
    show qs 108
    lo "But Hyril'ar is still strong."
    lo "Not to mention you alone could defeat an army of hundreds with your magic, if it came to that!"
    show qs 105
    ca "My magic..."
    show qs 109
    ca "Yes, well, about that..." with dis
    ca "Uh... apparently, I also need to wed one of the suitors to... preserve the balance of my magic."
    show qs 108
    lo "How do you mean, Your Grace?"
    show qs 109
    ca "Uh..."
    ca "Well, according to the Grand Druid, Anima’s power..."
    ca "{i}My{/i} power... is yearning to be passed on."
    ca "Which is making it grow volatile within me. Making me... weaker."
    show qs 110
    lo "Oh, I see..."
    show qs 109
    ca "But she believes that..."
    ca "P-Physical intimacy may anchor it once more."
    show qs 108
    lo "Oh."
    stop music2 fadeout 10
    play music2b quirky09 fadein 6
    show qs 111
    lo "Oh..."with dis
    lo "I-I understand."
    show qs 110
    ca ". . ."
    show qs 109
    ca "So... yes, that is yet another reason why a suitor must be chosen."
    show qs 112
    lo ". . ."
    show qs 111b
    lo "And... could Your Grace not simply..."
    lo "Huh..."
    show qs 111
    lo "N-No, no, of course not."
    lo "Please, forgive me. I overstep."
    show qs 114
    ca "Speak, Lorelei."
    show qs 111
    lo "I have nothing to say, Your Grace."
    show qs 114
    ca "Yes, you do."
    ca "I command you to speak."
    ca "Cast aside formalities... at least for this moment."
    show qs 112
    lo ". . ."
    show qs 111b
    lo "W-Well, if that is your will..."
    show qs 111
    lo "I just thought..."
    lo "Could Your Grace not simply... lie with someone?"
    show qs 111b
    lo "Surely, the act itself is what is required, not the ceremony around it."
    show qs 115
    lo "And... I cannot imagine a single noble in all Hyril’ar who would... decline such a proposal."
    show qs 114
    ca "That is out of the question."
    ca "We elves may carry the air of dignity, but beneath that, we are creatures of whispers and rumors."
    show qs 109
    ca "If I were to share my bed with a simple noble, every soul in the realm would know by nightfall."
    ca "And they would surely use that against me."
    show qs 111b
    lo "Oh... of course."
    show qs 114
    ca "And before you suggest it..."
    show qs 109
    ca "Yes, I have already tried... tending to it myself. Alone."
    ca "But I cannot... reach the..."
    ca "*Clears throat* I do not seem to be able to find release on my own."
    ca "My mind is blocked, somehow."
    show qs 111b
    lo "Oh... I-I understand."
    show qs 112
    lo ". . ."
    show qs 111
    lo "Then... perhaps..."
    lo "What if..."
    lo "What if Your Grace... asked Lord [mc] for... assistance?"
    show qs 113
    ca "Lorelei!" with hpunchsubtle
    ca "[mc] again?" with hpunchsubtle
    show qs 111
    lo "W-W-What I mean is..."
    lo "P-Perhaps the... touch of a man could help Your Grace reach–"
    show qs 113
    ca "Lorelei!" with hpunchsubtle
    ca "He is a human!" with hpunchsubtle
    ca "What you are suggesting is a crime both under our laws and the commandments of the Ancients! Akin to bestiality!"
    show qs 111b
    lo "I-I know, I do! I just..."
    show qs 111
    lo "Well, I thought that being a stranger to the court, there would be no risk of anyone discovering it."
    lo "A-And you mentioned yourself having grown fond of him, so..."
    show qs 114
    ca "U-Uh..."
    show qs 109
    ca "Y-Yes, well, I... I mean, I am fond of my horse as well, but that does not mean I intend to bed it."
    show qs 114
    ca "Do you not remember Lady Arwil? When she was caught with a human, she was stripped of name and exiled!"
    ca "She was never seen again!"
    show qs 111b
    lo "But... that was because she was... discovered. She was careless."
    show qs 111
    lo "Had she been more discreet..."
    show qs 114
    ca "Enough!" with hpunchsubtle
    ca "I will not allow a human to lay a hand upon me!"
    ca "I..."
    show qs 109
    ca "I... I cannot."
    show qs 111
    lo "I-I know, Your Grace."
    lo "I am well aware your body is sacred. More than any other in the realm!"
    lo "I merely thought he could... assist you... without touching you."
    show qs 115
    ca ". . ."
    show qs 114
    ca "What do you mean by that...?"
    show qs 111
    lo "Y-You said your thoughts distract you when you... try alone."
    lo "But perhaps... if your eyes were granted a certain indulgence..."
    lo "If you were to simply... watch... To allow his presence to ignite something within..."
    show qs 115
    ca ". . ."
    show qs 114
    ca "Explain yourself. Precisely."
    show qs 112
    lo ". . ."
    show qs 111
    lo "Well... I only mean..."
    show qs 115
    lo "I surely would do anything for you, Your Grace. You know it."
    ca "Hmph..."
    stop music2b fadeout 9
    play soundloop fireplace fadein 5
    scene qc 1 with Dissolve(3.4)
    pause 
    play sound chair2
    mct "Ahhh... this fire hits the spot." with dis
    mct "This place gets cold as hell when the sun goes down."
    mct "Which makes me wonder... is it winter here? Do Hyril’ar and Earth even have the same seasons...?"
    mct "Like... do they even use months? Days of the week?"
    mct "Mmh, there's still so much I don't know about this world. I really have to come back with the girls once this whole “Gem War” is over."
    mct "I wonder if being the CEO of Ulysses would earn me some kind of royal title at the court..."
    play sound knock2
    lo "*Knocking on the door* Um... Lord [mc]?"
    scene qc 2
    mc "Hmm?" with dis08
    mc "Lorelei? Is that you?"
    lo "Yes!"
    lo "Can we enter?"
    mc "Of course! Come on in, it's open."
    play music2 hyrilarquirky fadein 7
    play sound doorsqueak
    play sound2 ["<silence 2.5>", doorwoodclose]
    scene qc 3
    bla "Lorelei and Calypso step into your chambers, quickly shutting the door behind them." with dis22
    mc "*Gulps* D-Damn."
    mc "That's... quite an interesting outfit, Princess."
    mct "Holy shit... Calypso's body is unreal. Guess I can thank Anima’s bloodline for that."
    mc "I mean, elven royal outfits aren’t exactly modest to begin with, but the see-through fabric on this one definitely adds a certain... {i}spice."
    show qc 4
    ca "Oh... yes."
    ca "Lorelei and I ended up speaking for so long that it continued into my chambers."
    ca "I am still wearing my catalyst bracers, but I removed most of my jewelry and changed into my night robes for... better comfort."
    ca "My apologies. Do I... make you uneasy?"
    show qc 3
    mc "No, no, I didn't mean it like a complaint."
    mc "Far from it, actually..."
    mc "I can’t think of anyone who could pull that off better than you, Princess."
    show qc 4
    ca "Oh..."
    ca "T-Thank you, then."
    show qc 3
    mc "But anyway, tell me, tell me! How did the suitor thing go?"
    mc "Have you... chosen... a husband?"
    mct "Please say no..."
    show qc 5
    ca "Uh... yes, the conversations went well, but..." with dis14
    ca "I did not feel any particular... {i}connection{/i} with any of the suitors."
    show qc 6
    mc "Ah... I see."
    mct "GOOD."
    mct "As if Calypso would settle for anyone..."
    show qc 5
    ca "Thank you for accompanying me today and acting as my champion during the contest, [mc]."
    ca "Your presence brought me... unexpected ease."
    show qc 6
    mc "I told you, there's nothing to thank me for."
    mc "It turned out to be pretty fun in the end."
    mc "And even if it hadn’t been, come on, I owe you my life. The girls would’ve murdered me if I had abandoned you when you needed help. And..."
    mc "Well, I just wanted to help you, that's all."
    ca "Hmph."
    show qc 7
    ca "I am... truly glad you said that, actually."
    ca "Because..."
    ca "I might... uh... need one last favor from you before you return to your world."
    show qc 5
    ca "I swear, it shall be the last thing I ever ask of you."
    ca "And it will only take but a moment."
    show qc 6
    mc "Of course. What is it?"
    show qc 7
    ca "W-Well..."
    play sound footsteps4
    scene qc 8
    bla "Calypso walks through the room with an air of mystery, her expression unreadable." with dis22
    mc ". . ."
    mct "She's acting weird."
    ca "{i}*Muttering* I can't believe I am feeling this anxious with a–"
    mc "What?"
    play sound wood2 volume 0.3
    scene qc 10
    ca "*Clears throat* Hmph." with dis12
    scene qc 9
    ca "Forgive me. I just needed a moment to gather my thoughts."
    ca "I understand you must be eager to return, so I shall get to the point."
    scene qc 10
    mc "I'm listening..."
    ca ". . ."
    scene qc 9
    ca "Before I speak... I must make one thing absolutely clear."
    ca "Everything discussed here must remain within these walls."
    ca "If nothing else, it is a matter of the entire realm's security."
    ca "You must not speak of it to anyone. Especially not anyone in Hyril’ar."
    scene qc 10
    mc "Mm-mh... I understand."
    mc "You can trust me, you know it."
    mct "What's going on with her...? I've never seen her hesitate like this."
    ca "Hmph."
    if harempath:
        scene qc 11
        ca "So... as I have confirmed through my own observations, and as it's widely known..." with dis14
    else:
        scene qc 11
        ca "So... as it is widely known..." with dis14
    ca "Humans are renowned for their... particularly strong sexual impulses."
    show qc 12
    mc "Um..."
    mc "I guess so...?"
    mc "Do elves not have... strong urges too?"
    mc "Is that why you don’t have many children?"
    show qc 11
    ca "No. We have... the same impulses."
    ca "We simply... exercise more discipline."
    ca "We are refined. More civilized."
    ca "That is what separates us from animals, after all. Self-control."
    show qc 12
    mc "Interesting..."
    show qc 11
    ca "Our low birth rate stems not from lack of desire, but from biology."
    ca "Elven women are not easily... impregnated. It often requires many attempts before one bears fruit."
    ca "The scholars believe our low fertility is a consequence of our prolonged lifespan, which has diminished over the eras."
    show qc 12
    mc "I-I see."
    mct "Wait a second..."
    mct "I-Is she gonna ask me to knock her up?!"
    mct "Here?? In front of Lorelei?!"
    mct "Am I having a stroke?!"
    show qc 9
    ca "B-But we are digressing."with dis12
    ca "Let us return to the matter at hand."
    show qc 10
    mc "Ah... s-sure."
    mct "That was too good to be true..."
    show qc 9
    ca "Do you recall when I mentioned my magic was weakening?"
    show qc 10
    mc "I thought you said you were feeling stronger than the day you woke up after the fight against Thanatos."
    show qc 9
    ca "I did. But I speak of a broader scale now."
    ca "For some time, I have been feeling instability within my magic."
    ca "I can still cast simple spells, but the more powerful ones, even ones I once cast effortlessly... they now slip from my grasp."
    show qc 10
    mc "Oh, yeah, I remember you telling me about that."
    show qc 11
    ca "So... the matter is..." with dis12
    show qc 12
    ca "*Clears throat* Hmph."
    show qc 11
    ca "The Grand Druid believes that..."
    ca "I must... restore the balance of my inner energies by finding... release."
    show qc 12
    mc "Release...?"
    show qc 11
    ca "Y-Yes."
    ca "Which is why she encouraged me to wed one of the suitors with haste."
    show qc 12
    mc ". . ."
    mc "Um..."
    mc "What kind of... {i}release{/i} are we talking about here...?"
    ca ". . ."
    show qc 11
    ca "I need to... {i}achieve climax."
    show qc 12
    mc "Oh... oh."
    mc "OH."
    mc "W-Wait, are you saying you want me to–?"
    show qc 13
    ca "G-Get that indecent look off your face!"with dis12
    ca "I am already breaking a dozen rules by standing before you in my nightwear now. I shall not break more."
    ca "I may have accepted you into the court, b-but don't let it go to your head. No human shall ever touch, or even behold, the Princess of Hyril’ar in {i}that{/i} way!"
    show qc 14
    mc "O-Of course, Your Grace."
    mc "You misunderstand me. I'd never dare to suggest such a thing."
    mct "I've already beheld quite a lot, to be honest..."
    mct "Hmm, seems like not even Lorelei knows everything that's happened between us."
    mct "It's probably better to play along and pretend what happened in Frontier Trails never happened."
    show qc 11
    ca "My request is... far simpler."with dis12
    ca "I have attempted to reach this... {i}peak{/i} on my own, but with little success."
    ca "My mind wanders, and distractions always cloud my thoughts before I can... finish."
    ca "So we thought that perhaps... visual assistance might help me... focus."
    show qc 12
    mc "Visual assistance..."
    mc "Yeah... I think I know what you mean now."
    mc "I guess there are no elven porn scrolls in this world, eh?"
    show qc 11
    ca "Indeed not."
    ca "Which is why... Lorelei suggested that you both could perhaps serve as a... visual stimulation."
    play soundlow wood2
    show qc 15
    mc "*Turning around* L-Lorelei suggested what...?" with dis12
    show qc 16
    lo "I-I merely thought that a display of visually stimulating... a-activity might help the Princess."
    show qc 17
    lo "I mean... well, despite being a human, it would be foolish to deny your... physical appeal."
    show qc 16
    lo "Furthermore, Her Highness has spoken highly of your honor and reliability, so... you were the perfect candidate."
    show qc 15
    mc "Um..."
    show qc 16
    lo "I-I would, of course, b-be happy to assist. For the Princess’ sake."
    show qc 17
    lo "I mean... {i}happy{/i} is probably not the word. I do not want to."
    show qc 16
    lo "Like, not that I do not want to, more like... I don't {i}not{/i} want to."
    show qc 17
    lo "I'm curious from a purely academically perspective, naturally."
    show qc 16
    lo "But I would never dare to do anything so indecent like... t-touching a human in a carnal way. U-Unless the Princess needed it."
    show qc 17
    lo "Which she does! Probably."
    show qc 16
    lo "N-Not that I do not–"
    show qc 15
    mc "I-I get it."
    show qc 11
    ca "So... what is your answer?" with dis12
    ca "O-Of course, please, keep in mind you are free to refuse."
    ca "This is not a command as a Princess, but a favor asked as... an equal, within the... bond we have established."
    show qc 12
    mct "Man... is this conversation really happening?"
    mct "Because if it is..."
    mct "There's no way Calypso would ever ask something like this to anyone, not even in a desperate moment."
    mct "Could she really be..."
    menu:
        with dis
        "[gr]Accept":
            stop music2 fadeout 15
            mc "I... accept." with dis  
            mc "I will help you."
            mc "I told you, I'm here to help."
            ca "Hmph."
            show qc 11
            ca "Thank you."
        "Refuse":
            stop music2 fadeout 22
            mc "I-I'm not familiar with the elven... customs, so I'm honestly not entirely sure of what I'm being asked." with dis
            mc "But... uh... I don't think I... can help much there."
            mc "I mean... I was nearly executed a few days ago. I'd rather not risk another noose around my neck."
            mc "N-Not that I'm not flattered that you thought I could help somehow."
            mc "It's just... well, I'm in a bit of a rush, and..."
            mc "That's not exactly my... uh... comfort zone."
            stop music2 fadeout 10
            show qc 11
            ca "Yes... y-yes, naturally." 
            ca "I... I had no right to expect more than what you have already offered. I just thought humans might know some... trick to..."
            ca "But... uh... yes, you are right."
            ca "You are a human. I am an elf. The Princess of the Elves."
            show qc 8
            ca "*Muttering* By the Ancients, I cannot believe I nearly... debased myself before a human." with dis12
            ca "*Muttering* I do not even know what Lorelei was thinking."
            play sound footsteps4
            show qc 18
            ca "*Clears throat* Anyway, we should proceed with what I came here to do. Please, forget I said anything." with dis2
            mc "Oh... so fast?"
            ca "Yes, I've retained you long enough, and you have your women waiting."
            ca "*Clears throat* Hmh-mpph."
            ca "{i}Glem ni sa' eradin." 
            play sound3 spell3
            play sound2 spell2
            play soundloop2 energy2 fadein 1
            show qc 19 with dis12
            mc "Whoa! Your magic looks as powerful as ever to me!" with dis
            ca "Opening a portal is easy, but maintaining it... not so much."
            mc "I guess I shouldn't delay it, then."
            scene qc 20
            mc "Will you be alright?" with dis12
            show qc 21
            ca "Naturally."
            ca "Your help has been invaluable, [mc], but I ruled Hyril'ar long before your arrival."
            ca "This may not be our kingdom's finest hour... but I shall mend it."
            show qc 20
            mc "Alright then."
            scene qc 22
            mc "You'll come back to us, right? You promised." with dis14
            ca "As I said, I shall gather allies, secure our borders, ease the tensions within... and then I will visit you all."
            ca "You have my word."
            mc "I'll hold you to it."
            mc "And hey, when all this is over, maybe we can finally sit down and try to fix your magic problem. I'm good with broken things."
            ca "*Soft chuckle* Me, the Princess of Hyril'ar, broken? Perish the thought!"
            ca "I hope I’ll be at full strength when we meet again, but if not... I shall seek your help once more, yes."
            mc "Sounds good!"
            mc "Until next time, Caly. Lorelei."
            lo "S-Safe travels, [mc]!"
            ca "Farewell... [mc]."
            play sound3 spell3
            play sound2 spell2
            play sound debris
            stop soundloop2 fadeout 1
            scene qc 23 with flashfast
            pause
            play soundlow footsteps4
            scene qc24 with dis2
            play sound2 chair1
            bla "Calypso silently walks to the bed and sits on the edge next to Lorelei." with dis12  
            lo ". . ."
            ca ". . ."
            show qc 25
            lo "So..."
            lo "W-What's the plan now, Your Grace?"
            show qc 26
            ca ". . ."
            $ mcleaveshy2 = True
            jump mcisback
    show qc 12
    mc "Can I... be direct for a moment, though?"
label ga_calypso1:
    if _in_replay:
        play soundloop fireplace fadein 1
        scene qc 12
        mc "Can I... be direct for a moment, though?" with dis
    mc "Just to make sure I... understood you right."
    ca "Mm-hm."
    mc "So..."
    mc "You're blocked magically, somehow, and you need to release it through... climax. Orgasming."
    mc "But you're unable to reach it on your own, and you can't simply just go have sex with anyone, because... well, you are the Princess of the realm."
    mc "So now... you want my help."
    mc "You want me here. Watching you... while you touch yourself."
    mc "Because I turn you on. I... arouse you."
    ca ". . ."
    show qc 12b
    ca "Hmph." with dis08
    play soundlow footsteps4
    scene qc27 with dis2
    play music2b babylon fadein 7
    stop soundloop fadeout 25
    play sound2 chair1
    bla "Calypso silently walks to the bed and sits on the edge." with dis12  
    show qc 28
    ca "Yes... something like that."
    ca "I suppose it will indeed be simpler if we drop all the facades."
    ca "So... yes, [mc]... I require your help for exactly that reason."
    ca "Happy?"
    show qc 27
    mc "And what about the part where I turn you on...?"
    ca "*Snorts* Hmph."
    show qc 28
    ca "Perhaps it is true what they say, that friction breeds affection."
    ca "Yes, [mc]... I do find you... stimulating."
    ca "Arousing... as you say."
    show qc 27
    mc "For a human?"
    show qc 28
    ca "...For a man."
    show qc 27
    mc "Glad to hear that..."
    mc "Because I do find you incredibly attractive as well, Princess."
    show qc 28
    ca "You have told me that before. You are not exactly subtle when it comes to praising a woman’s attributes."
    ca "But still... thank you."
    show qc 30
    ca "Now... shall we begin?" with dis
    scene qc 31 with dis12
    pause
    play sound vanishmagic
    show qc 32 with dis15
    pause
    play sound2 clothes3
    show qc 33
    mc "W-What the hell?!" with dis14
    mc "I-I thought you said your magic was blocked!"
    show qc 34
    ca "Only the more complex spells. Even a child could manage to cast a simple vanishing charm."
    ca "What is the matter?"
    ca "Do not tell me you are shy now..."
    show qc 33
    mc "Um..."
    mc "N-No, of course not. I just... wasn't expecting it."
    show qc 34
    ca "Hmm, how very human of you..."
    ca "What about you, Lorelei?"
    ca "You have been eyeing [mc] like ripe fruit on a branch since the moment he crossed our borders."
    ca "And something tells me your fascination runs deeper than idle curiosity..."
    ca "So... tell me..."
    ca "Now that you see him like this... is it what you imagined in those quiet, forbidden thoughts of yours?"
    show qc 35
    lo "It is... quite... similar. More than I care to admit." with dis12
    ca "Maybe you should take a closer look..."
    lo "Oh..."
    lo "Should I...?"
    play soundlow wood2 volume 0.6
    show qc 36
    bla "Following her mistress' suggestion, Lorelei lowers herself to her knees." with dis15
    mc "O-Oh my god."
    show qc 37
    mc "W-What... what are we supposed to do, exactly?"with dis 
    show qc 34
    ca "You can think of it as... a performance. A ceremony."
    ca "A... thank you for your service, and... a gift in return."
    play soundlow wood2 volume 0.5
    show qc 38
    bla "Lorelei leans in slowly, her breath warm and fluttering against your skin." with dis15
    lo "*Sniffs* Hmhhh..."
    lo "*Whispering* Your scent..."
    lo "*Whispering* It's so... raw. S-So... manly."
    play sound oily volume 0.2
    show qc 39
    bla "A tremor rolls through your body as you grow harder by the second, your cock twitching against her face." with dis22
    lo "By the Ancients..."
    lo "You were right, Your Grace..."
    lo "It is getting so huge!"
    show qc 37
    mc "W-What?"
    show qc 37b
    mc "What do you mean, “you were right”?" with dis08
    mc "Y-You've been talking about my... my cock??"
    show qc 34
    ca "Lorelei has had many questions about the human species, as is natural."
    ca "Some... less innocuous than others."
    show qc 39
    lo "By all the sacred groves, it is bigger than my head!"
    lo "Is this... is this normal for humans?"
    show qc 37
    mc "W-What? No! Or..."
    mc "I mean... I-I don't know! What kind of question is that?"
    show qc 39
    lo "The way it throbs... like it has a heartbeat of its own..."
    lo "It is... fascinating..."
    lo "Can I... can I touch it, Your Grace?"
    show qc 34
    ca "Everything that happens within these walls remains between us, Lorelei."
    ca "I grant you permission to act freely."
    play soundlow wood2 volume 0.6
    show qc 40
    bla "Lorelei rises slightly and lets her warm hand finally close around the base of your cock. Her breath fans across the tip of your member." with dis15
    lo "M-Maybe..."
    lo "Maybe this is wrong."
    lo "Maybe I should not..."
    show qc 34
    ca "You have my blessing, Lorelei — I told you."
    ca "Both the Ancients and the Law will look the other way tonight."
    ca "There are no eyes but ours here..."
    show qc 40
    ca "I give you permission... to use your mouth, if you wish." with dis12
    lo "*Breathing nervously* . . ."
    lo "As... as you command... Your Grace..."
    play sound oily volume 0.33
    show qc 41
    lo "Hmmm..." with dis2
    play sound2 oily volume 0.44
    show qc 42
    lo "H-H-Hmm-m-mm..." with dis2
    mc "O-Oh my god..."
    play sound3 ["<silence 0.4>", blow4]
    show qc 43
    lo "*Taking a deep breath* H-Heavens above..." with dis
    lo "I cannot... breathe properly when it is in my mouth..."
    show qc 34
    ca "If it overwhelms you, I can call upon another maid, Lorelei."
    show qc 43
    lo "N-No..."
    lo "P-Please, do not trouble yourself, Your Grace..."
    lo "I will... endure it."
    play soundloop blowjob2 fadein 3
    play sound clothes3oily fadein 2
    scene calyh6 with dis2
    bla "Lorelei takes you into her warm, petite mouth, as she starts moving with sudden hunger."with dis12
    mc "O-Oh my fucking god..."
    mc "Y-You certainly know what you're doing..."
    lo "Mm-mh..."
    mct "How in the hell did I end up like this..."
    mct "I was... fucking painting and reciting poems in front of an elven court just a few hours ago, and now... THIS?"
    lo "*Muffled moan* Mmmmmhhh..."
    scene qc 45
    ca "*Biting her lip* . . ." with dis15
    play sound vanishmagic
    scene qc 46
    bla "Calypso's bracers shimmer before vanishing into thin air." with dis15
    scene qc 47
    ca "*Pulling her pantyhose down* I suppose no advanced magic shall be necessary this time..." with dis17
    scene calyh6
    bla "Calypso pauses in silence for a moment as her gaze lingers upon you, weighing her next move." with dis15
    ca ". . ."
    lo "Mmmmhhh..."
    scene qc 47
    ca ". . ." with dis12
    scene qc 48
    bla "Her fingers finally slide between her legs, disappearing into her thighs with a trembling sigh." with dis17
    show qc 49
    ca "*Soft moan* Aahhh..." with dis12
    scene calyh1 with dis2
    ca "*Moans* AAaaahh..." with dis
    ca "Gods..."
    ca "*Whispers* It is... better than I anticipated..."
    ca "Aahhh..."
    ca "*Softly* So... much... better..."
    ca "*Whispers* What kind of curse is this...?"
    scene calyh7 with dis2
    bla "Lorelei continues without slowing down, her eyes flicking up toward you, then to Calypso, seeking approval obsequiously as she swallows you again and again." with dis
    ca "I must admit..."
    ca "You are performing admirably, Lorelei..."
    lo "Mmmmhh..."
    ca "And you, [mc]... how do you fare?"
    mc "A-Aahh..."
    mc "I can't even think straight, but..."
    mc "I-I've gotta say..."
    mc "Elven hospitality is c-criminally underrated..."
    ca "*Moans* Hah..."
    mc "T-This is certainly not how I expected to wrap up my stay here..."
    mc "Especially considering how it all began..."
    play sound clothes3
    scene calyh2 with dis2
    bla "As she continues to caress herself, Calypso draws her silken pantyhose down, revealing more of her perfect alabaster skin." with dis
    mc "*Looking at Calypso* Oh, yeah..."
    ca "*Moans* AAahh..." 
    ca "I-I can..."
    ca "*Moans* Aaahh..."
    ca "I can imagine how stressful that was..."
    ca "The frigid walls of the cell... the rope drawing tighter around your neck..."
    ca "*Moans* Mm-mmmhh..."
    ca "I am... relieved I managed to step in just in time..."
    ca "It..."
    ca "*Moans* Mmm-mhh..."
    ca "I-It pleases me to see you alive..."
    scene calyh7
    ca "And... satisfied..." with dis2
    mc "I-It pleases me too, I c-can assure you..."
    lo "MmMmmmm..."
    lo "MmmMMMhH–"
    stop soundloop fadeout 1
    play sound blow5
    scene qc 51 with dis12
    lo "*Gasping for air* A-AAgghh..." with dis08
    lo "A-Ancients, lend me strength..."
    ca "I doubt the Ancients would condone what you are doing with such... fervor, Lorelei."
    lo "*Breathless* Hah..."
    lo "I... I suppose not..."
    play sound vanishmagic
    scene qc 52
    lo "Ah–!" with dis17
    lo "W-What is this?"
    scene calyh2 
    ca "*Soft moan* Is there... a problem?" with dis2
    ca "We should try not to... mmmhh... soil the hunting leathers."
    lo "Oh... n-naturally!"
    ca "N-Now... proceed."
    lo "Of course..."
    play sound wood2 volume 0.3
    scene calyh8 with dis25
    play sound2 ["<silence 1.5>", oily]
    lo "At your command, Your Grace...{w=2}{nw}"with dis
    play soundloop blowjob2 fadein 1
    lo "{bt=3}Mmmm-mh-mmhhh...{w=9}{nw}" with dis
    scene calyh2 with dis17
    ca "*Moans* Yes... just like that..." with dis
    ca "You are serving well, Lorelei..."
    ca "Aaah..."
    ca "But this..."
    ca "*Muttering* Mmmh, this is not enough..."
    ca "*Grumbling softly* I need... more..."
    ca "*Grumbling softly* Perhaps..."
    play sound6 clothes3
    scene qc 53 
    ca "Hmmmph..." with dis17
    play sound7 vanishmagic
    scene qc 54
    ca ". . ." with dis17
    show qc 55
    ca "Hmph..." with dis14
    ca "*Muttering* Perhaps stronger magic is necessary, after all..."
    play sound7 clothes3
    show qc 57
    bla "Calypso slowly spreads her legs, revealing more with each movement. She no longer hides how wet she’s become, nor does she care." with dis17
    ca "*Panting lightly* . . ."
    show qc 56
    ca ". . ." with dis
    scene calyh9 with dis15
    bla "Calypso pauses for a moment, her gaze lingering on her maid's dedication." with dis
    mc "O-Oh my fucking god, t-this is insane..."
    lo "*Muffled moan* Mm-mhhhmm..."
    scene qc 56 
    ca ". . ." with dis15
    scene qc 57
    ca "Hmmm..." with dis
    play sound vanishmagic
    play sound2 spell2 volume 0.4
    scene qc 58 
    bla "Before your eyes, Calypso conjures an ethereal cock shaped after your own, pulsing with energy." with dis17
    scene qc 59
    ca "Holy Mother of Turska, [mc], this thing is..."with dis12
    ca "...Enormous."
    stop soundloop fadeout 1
    play sound blow4
    scene qc 60
    lo "*Pausing to breathe* I-It is..." with dis12
    lo "B-But..."
    show qc 61
    lo "I will try to represent our kind with pride, Your Grace..."
    show qc 60
    lo "Please, just tend to yourself, and..."
    lo "Leave the rest to me..."
    play sound blow6 fadein 1
    play soundloop blowjob2 fadein 2
    play sound7 wood2 volume 0.2
    scene calyh9 with dis15
    bla "Lorelei sinks her mouth back onto you with enthusiasm, sucking harder and faster than before." with dis
    mc "O-O-Ohh fuck..."
    scene qc 58b
    ca ". . ." with dis15
    ca "Hmprh."
    play sound2 clothes3oily
    scene qc 62
    bla "Calypso guides the magic cock between her legs." with dis2
    ca "Mmmhph..."
    play sound oily
    scene qc 63
    bla "With a slow thrust, Calypso sinks the magical cock inside her, gasping at the sensation." with dis17 
    scene qc 64
    ca "A-Aaagh..." with dis17
    ca "D-Dear heavens..."
    scene calyh3 with dis2
    ca "Aggh... ahh... aaAahhh..." with dis
    ca "G-Gods, this is..."
    ca "*Gasps* T-This is thick..."
    ca "Mm-mMmhh..."
    ca "This is... s-something else..."
    mc "*Looking at Calypso* (Dear Lord...)"
    mct "She's completely lost in it..."
    mct "She doesn't even mind me seeing all of her anymore."
    mct "I never thought I'd ever see Calypso in this way..."
    scene calyh9 with dis2
    bla "The sight of Calypso pleasing herself makes you throb harder, which Lorelei immediately responds to by sucking harder, more hungrily." with dis
    mc "A-A-Aaaghh... oh god..."
    lo "*Gagging* Mm-mmMhhh..."
    mc "F-Fuuck..."
    mct "Calm down, [mc]..."
    mct "You can't cum yet... not yet..."
    mct "You’re representing your whole species here..."
    lo "*Moans* Mmmmhhh..."
    scene calyh3 with dis2
    bla "You glance at Calypso again. She meets your gaze, unabashed, panting, as if she owns every second of your attention."with dis
    ca "*Moans* G-Gods, that is big..."
    mc "I-I can't believe I'm seeing this, my Princess..."
    ca "*Moans* H-Hah..."
    ca "Y-You do... well to disbelieve... for if this were known..."
    ca "We would all be put to death for such... sacrilege..."
    mc "That's kinda hot..."
    ca "Hah..."
    ca "Your obsession with danger no longer surprises me..."
    mc "W-What if you... took those robes off, huh...?"
    mc "What more could they possibly charge us with...?"
    ca "*Chuckles through her moans* Hah..."
    ca "You humans... such wicked tongues..."
    mc "Let me see them again..."
    ca "Hah..."
    ca "*Moans* Mmmmmhh...!"
    ca "Ahh... humans..."
    play sound clothes3
    scene qc 65 with dis2
    ca "*Panting softly* Hmph... fine." with dis
    ca "Y-You are lucky this is..."
    ca "Your final night ever in Hyril’ar..." 
    play sound clothes3
    scene qc 66 with dis2
    bla "Calypso lets the silken straps fall from her shoulders, revealing her generous, perfectly round breasts." with dis
    mc "Oh GOD..."
    stop soundloop fadeout 1
    play sound blow4
    scene qc 61
    lo "*Pausing to breathe* Whoa..." with dis12
    lo "Your Grace... your body is truly unmatched. No one in the realm compares."
    scene qc 66b
    ca "There is no need to continue your flattery, Lorelei."
    show qc 61
    lo "But I really mean it."
    show qc 66b
    ca "You may be more delicate in frame, but you lack for nothing in beauty."
    play sound wood2 volume 0.2
    scene qc 68
    lo "Your Grace is too kind..." with dis15
    lo "I could never compare..."
    play sound vanishmagic
    scene qc 68b
    ca "Ah, sweet Lorelei..." with dis15
    mc "Oh boy..."
    ca "Perhaps you need to be {i}shown{/i} what your body can do."
    lo "Oh..."
    play sound wood2 volume 0.2
    play sound2 fall2
    scene qc 69
    lo "*Crawling between your legs* But..." with dis17
    lo "Have I not already debased myself enough tonight?"
    lo "S-Should I really... go further...?"
    show qc 70
    mc "W-Wait, do you want me to..."
    show qc 66b
    ca "...Yes."
    ca "Yes, [mc]."
    ca "You have my permission to take her... if she consents."
    show qc 69
    lo "I do..."
    lo "For you, Your Grace... anything..."
    show qc 70
    mc "Um..."
    menu:
        with dis12
        "Fuck her [gr][mt](Lorelei's scene)":
            $ loreleisex = True
            mc "Ooh, fuck..."with dis 
            play sound chair2
            play sound2 wood2 volume 0.4
            scene qc 71
            mc "*Kneeling down* Are you sure about this...?" with dis15
            lo "Mm-hm..."
            mc "Oh, Jesus..."
            play sound oily
            show qc 72
            bla "You slowly guide your cock to the entrance of Lorelei's soaked, eager pussy." with dis2
            lo "*Soft moan* Aaahh..."
            mc "Aghh..."
            show qc 66b
            ca "Good..."with dis14
            ca "Now..."
            ca "{i}Take{/i} her..."
        "Stop here":
            mc "I-I appreciate the offer, really, but I... I can't do it."with dis 
            mc "T-That's too much."
            play sound clothes3oily
            play sound2 blow4 volume 0.6
            scene qc 76
            ca "What?!" with dis12
            ca "You are rejecting my... {i}our{/i} offer?!"
            mc "Erm..."
            mc "Can't believe I'm saying this, but... y-yes, I guess I am."
            mc "I don’t want any of us waking up tomorrow with regrets."
            mc "Let this be proof that humans can show restraint!"
            mc "...Sometimes."
            jump posloreleisex
    show qc 72
    ca "Show us what the human race is truly capable of, [mc]..." with dis15
    mc "Oh, yeah..."
    lo "*Whispers* Give me everything, Lord [mc]..."
    play sound slap1
    play sound2 slap1
    play sound3 penetration2
    scene qc 73
    lo "{sc=3}AAAAAAaaaaAAArghh..." with hpunch 
    scene calyh10 with dis2
    lo "{sc=2}AAAAhhh... ahhhh... aaaahhh... AAAAHHHhhHH..." with dis
    lo "{sc=2}O-O-Ohh heavens above..."
    mc "Oh my f-fucking god, Lorelei, you're tight..."
    show calyh4 with dis2
    bla "Calypso watches you with smoldering eyes as she plunges the magic toy even deeper into herself, moaning in time with every slap." with dis
    cabt "O-Ohh... mmmMmhh..."
    cabt "Y-Yes..."
    casc "AAaAaAAAhHHhh..." with hpunchsubtle
    ca "Gods, [mc]..."
    ca "You are... a brute..."
    hide calyh4
    lo "*Panting* Aaahh... AHHHH... AAAAAGGHH..." with dis
    lo "{sc=2}AAAAARGHHhh..." with hpunchsubtle
    mc "O-Oh, fuck yeah, that's it..."
    lo "Ohh, b-by the Ancients..."
    lo "W-What am I doing...?"
    bla "Lorelei writhes, lost in search of her climax, her hips still pushing against you in defiance of her guilt."
    lo "*Moans* AAAAhhh..."
    lo "M-May the Ancients forgive me..."
    show calyh4
    casc "MMmmmhhh..." with dis15
    bla "Calypso remains focused savoring the obscene sounds echoing through the chamber, her eyes fixed on you with a mixture of fascination and pure lust."
    ca "T-This..."
    ca "This feels totally different..."
    ca "*Moans* AAAahhh..."
    ca "O-Oh dear heavens... if the C-Council were to ever learn of this..."
    ca "H-Hah..."
    ca "W-We would all swing for this..."
    scene calyh11 with dis12
    bla "You grip Lorelei’s hips and thrust faster, harder, giving her no rest."with dis
    lo "{sc=2}G-G-Gggh-GGghhh..."
    mc "Ohhhh, f-fuck yes..."
    mc "S-So good..."
    lo "*Squeals* AAAAhhh..."
    lo "Aaaahhh... AaaAAahhhhh..."
    lo "P-Please... never..."
    lo "*Moans* AAAAGHHhhh..."
    lo "N-Never tell my father about this..."
    mc "H-Hah..."
    mc "I w-wasn't planning to..."
    lo "*Voice breaking* Oof..."
    lo "O-Oh, Y-Your Grace..."
    lo "I c-can... see the appeal in these... b-barbaric ways now..."
    show calyh5
    bla "Calypso groans and slams the toy into her, sweat gleaming on her skin. You can tell she’s as caught in the moment as Lorelei is." with dis15
    ca "*Panting* Hah..."
    ca "*Panting* I m-must admit that..."
    ca "*Panting* I-I can see it too..."
    casc "*Moaning* AAaahh..." with hpunchsubtle
    casc "*Moaning louder* AAaAhHHh..." with hpunchsubtle
    mc "Ohhhh, fuck yeah..."
    ca "*Whispers* Ohh... [mc]..."
    ca "*Whispers* Don't stop..."
    mct "Huh...? D-Did she just say my name...?"
    mct "Is she... imagining I'm the one fucking her...?"
    ca "Y-Yes... make her... scream..."
    ca "I w-want to... hear it..."
    mc "Y-You two are too much, Princess..."
    mc "And then you dare to claim humans are the sinful ones..."
    ca "H-Hah..."
    ca "E-Enjoy the privilege before our senses return, [mc]..."
    scene calyh12 with dis12
    lo "{sc=2}AAAhhh...AAAHHHh....AAAGHHH!!!"with dis
    mc "O-Ohh, shit..."
    mc "I'm gonna... I'm gonna c-cum..."
    lo "{sc=2}AAAhhh... me... too... I-I can't... I c-can't!"
    ca "Y-You must withdraw if you do not want Lorelei to be exiled for giving birth to a Peredhil, [mc]..."
    ca "T-The law is... merciless, you know it..."
    lo "{sc=2}I-I do not think... I can..."
    lo "{sc=2}AAAhhh..."
    lo "{sc=2}I do not think I can hold it for too long, Your G-Grace..."
    lo "{sc=2}AAAhhh... aaaahhhhhHHhh..."
    lo "{sc=2}I am at... my limit..."
    mc "{sc=2}F-Fuck... me too..."
    lo "{sc=2}O-Ohh, Your Grace..."
    lo "{sc=2}I-I'm sorry... I c-cannot..."
    mc "{sc=2}Oh my god..." with hpunch 
    mc "{sc=2}I'm–" with hpunch 
    play sound cumall
    play sound2 fallfull
    scene qc 74 with hpunchlong
    play sound3 clothes3
    scene qc 75
    bla "You barely manage to pull out as your climax overtakes you and ropes of thick cum spill across Lorelei’s back just as her entire body convulses beneath you." with dis2
    mc "*Panting* Jesus Christ..."
    lo "*Still orgasming* G-G-Gods..."
    lo "H-Heavens almighty, have m-mercy on me..."
    play sound clothes3oily
    play sound2 blow4 volume 0.6
    scene qc 76
    ca "W-What?!" with dis12
    ca "You are... finished?!"
    scene qc 75
    lo "I cannot... endure... another second..."
    scene qc 76
    ca "But–"
    ca ". . ."
    jump posloreleisex
label posloreleisex:
    play sound clothes4
    play sound4 clothes3
    play sound2 couch 
    show qc 78
    bla "Calypso makes the ethereal cock vanish and sits up, grumbling softly in Elvish as she covers herself."with dis2
    ca "Hmph."
    show qc 77
    if loreleisex:
        ca "Uh... I suppose this means we... finished."
    else:
        ca "You chose quite the moment to finally begin to restrain yourself, [mc]."
        ca "But... very well."
    ca "The night is over."
    ca "I... appreciate your help."
    show qc 79
    ca ". . ." with dis
    scene qc 80
    pause
    play sound vanishmagic
    scene qc 81
    mc ". . ." with dis17
    scene qc 77
    ca "You have my thanks for your... assistance. Both of you."
    ca "You may go now."
    play sound chair2
    show qc 82
    if loreleisex:
        lo "N-No!" with dis12
        lo "I... I'm still tingling a bit, but I just need..."
        lo "Just give me a few minutes and I can continue!"
        show qc 77
        ca "That will not be necessary."
        ca "The objective of this... “ritual” has been achieved."
    else:
        lo "W-What?!" with dis12
        lo "But... w-we are not done yet!"
        lo "I need... Y-Your Grace needs to... seek release!"
        lo "That was the whole objective!"
        show qc 77
        ca "And the objective was achieved."
    ca "You have done well, Lorelei."
    show qc 82
    lo "But–"
    show qc 83
    lo "...Oh." with dissolve
    if loreleisex:
        lo "So... did Your Grace... successfully..."
        show qc 77
        ca "Indeed, I did."
    else:
        lo "Was it?"
        show qc 77
        ca "Indeed, it was."
    ca "You both have my gratitude. You are dismissed."
    show qc 83
    lo "I-I see."
    lo "I understand."
    play soundlow wood2 
    show qc 85
    lo "*Standing up* Well, in that case..." with dis14
    lo "Um..."
    lo "T-Thank you, Lord [mc], for... your assistance."
    lo "To the Princess... and to me."
    lo "It was... a welcome deviation from the monotony of the past few years."
    show qc 84
    mc "The pleasure was certainly mine..."
    show qc 85
    lo "Thank you."
    lo "I am... pleased to hear that."
    show qc 86
    lo "N-Now... if Your Grace would kindly return my garments before I return to my chambers..." with dis12
    show qc 77
    ca "Oh... o-of course. Naturally."
    play sound footsteps4
    scene qc 87 with dis2
    lo "*Bowing down* Thank you, Your Grace." with dis 
    lo "Lord [mc]."
    lo "G-Good night."
    play sound dooropenclose
    scene qc 88
    bla "The chamber door opens with a sigh and closes behind Lorelei." with dis15
    mct "Damn..."
    mct "That was something."
    play sound2 footsteps4
    scene qc 89 with dis22
    bla "You turn around and slowly walk towards the edge of the bed where Calypso is sitting." with dis12
    show qc 90
    ca "Why are you still here...?"
    ca "I just said you are dismissed."
    show qc 89
    mc "Well, for starters... this is actually my room."
    show qc 91
    ca "...Oh."
    ca "Yes. That... is fair."
    show qc 89
    mc "And secondly... I think we both know we’re skipping over something pretty important here, Calypso."
    show qc 90
    ca "I told you that you must not speak my name so casually here."
    ca "You forget your place, [mc]."
    show qc 89
    mc "Well..."
    mc "I just saw you using a magical cock modeled after my dick, so I don’t think calling you Calypso is the worst breach of etiquette we’ve had tonight."
    show qc 91
    ca "Please, do not make me relive this shameful moment."
    ca "This spiraled far beyond what I intended."
    show qc 90
    ca "But... the purpose was fulfilled. I have no further need for you."
    ca "So... let us return to how it was, please."
    show qc 89
    mc "But you don't really want me to."
    show qc 90
    ca "Excuse me...?"
    show qc 89
    mc "I’m not one of those polished bootlickers you’re surrounded by at the Court."
    mc "I talk to you like a real person. Like an equal."
    mc "And you like that."
    ca ". . ."
    mc "I know what you need, Princess. Right now. Tonight."
    show qc 90
    ca "Oh, yes...? Please, enlighten me."
    show qc 89
    mc "You might have convinced Lorelei, but I’m not so easily fooled."
    mc "You didn't finish."
    mc "You writhed. You moaned. But I know you didn't cum."
    show qc 92
    ca "W-What would you know of it..."
    show qc 89
    mc "I was watching you the whole time..."
    mc "So I know."
    mc "And if you let me... I can fix that."
    show qc 90
    ca "And how would you do that, exactly?"
    show qc 89
    mc "You can start by placing your feet on the floor."
    show qc 90
    ca "The floor...?"
    ca "Is this just another ploy to see me undressed again?"
    show qc 89
    mc "Well, no man in his right mind would complain about that... but no."
    mc "Just trust me, please — it's the last thing I'll ask of you."
    ca ". . ."
    mc "One last favor...?"
    ca ". . ."
    play sound clothes3
    scene qc 93
    bla "Calypso slowly lowers her pale and perfect legs for you. Her porcelain body is bare once again before you." with dis2
    mc "Whoa..."
    play sound chair2
    play sound2 wood2 volume 0.33
    scene qc 94
    mc "*Kneeling down* You truly are... a vision, Princess."with dis15
    mc "No matter how many times I see you, it always feels like a dream."
    ca "Hmph."
    show qc 96
    ca "I thought you said you were not like those simpering flatterers from Court." with dis15
    show qc 95
    mc "And I'm not."
    mc "It's different when you mean every word you say."
    ca "Hmph."
    mc "I know you’ve always drawn a line I’m not supposed to cross, but..."
    mc "I've gotta ask."
    mc "May I... touch your sacred skin, Princess...?"
    mc "Just... once. For me. For goodbye."
    ca ". . ."
    show qc 96
    ca "*Sighs* ...You may."
    play sound2 clothes3
    scene qc 97b
    bla "You gently place your hands on Calypso's thighs and start caressing her warm and impossibly soft skin."with dis2
    ca ". . ."
    play sound3 clothes3
    scene qc 97
    bla "You part her legs slowly, reverently, yet she doesn’t stop you. She only exhales, a shaky breath betraying the fire beneath her restraint." with dis2
    mc "May I..."
    mc "May I kiss your legs, Princess...?"
    ca ". . ."
    ca "*Softly* ...You may."
    play sound clothes3
    scene qc 99 with dis2
    play soundlow kiss 
    mc "*Kiss*" with dis
    scene qc 100 with dis17
    play soundlow kiss 
    mc "*Kiss*" with dis
    scene qc 99 with dis17
    play soundlow kiss 
    mc "*Kiss*" with dis
    scene qc 101
    scene qc 101
    ca ". . ." with dis2
    mc "May I..."
    ca "*Soft tremble* . . ."
    mc "May I please you, Your Grace...?"
    ca ". . ."
    ca "*Whispers* ...You may." with dis
    play sound clothes3 fadein 1
    play soundlow clothes3oily
    play sound3 wood2 volume 0.33
    play soundloop wettingslow fadein 2 volume 0.6
    scene calyh13 with dis2
    bla "Your mouth finds the warmth between her thighs. Calypso's hands fly to your head and her whole body tenses at the touch of your tongue."with dis 
    ca "*Gasps* AAAaagh..."
    ca "Nnnngh... this is... aaAAahh... wrong..."
    ca "T-This is {i}so{/i} unspeakably wrong..."
    ca "*Moans* AAahhh..."
    mct "I love the way her legs tremble..."
    mct "And... god, her taste is... addicting."
    ca "*Moans* A-Aa-ahhHhh..."
    $ mc_dash = "{}-{}".format(mc[0].upper(), mc)
    ca "Ohh [mc_dash]..."
    ca "H-How can... something so forbidden... feel so..."
    ca "R-Right..."
    ca "*Moaning* A-AaahhhGhhh..." with hpunchsubtle
    ca "I-I am... a daughter of Queen Anima..."
    ca "W-Warden of the... Eternal Soul..."
    ca "*Voice breaking* I should not be... moaning under a human's touch..."
    bla "You focus on her clit, slow flicks turning into confident, hungry swirls. You can feel her restraint melting in every gasp."
    ca "AAahhh... ngghh..."
    ca "*Gasps* Y-Yes..."
    ca "B-By the Ancients..."
    ca "*Breathless* Do not... stop..."
    ca "G-Give me everything..."
    ca "Aahh..."
    ca "AAAAaaHHhh..."with hpunchsubtle
    casc "AAAaaAggGGghhhh!" with hpunch
    stop soundloop 
    play sound whoosh6
    play sound2 fallfull
    play sound3 vanishmagic
    scene qc102 
    bla "Calypso suddenly pushes you to the ground with a pulse of magic." with pl
    play sound4 footsteps4
    scene qc 104
    mc ". . ." with dis2
    scene qc 105
    bla "Calypso, now completely naked, stands above you with a mix of both shame and pride."with dis15
    mc "Oh, dear Lord..."
    show qc 106
    mc "P-Princess...?"with dis15
    ca ". . ."
    play sound whoosh6
    play sound2 fallfull
    play sound3 woodhit
    scene qc 107
    mcsc "Mmm-gghh!" with vpunchslow
    play soundloop wettingslow fadein 2 volume 0.6
    scene calyh14 with dis2
    cabt "Mmmm... MmmmhhMMMmmghhh..." with dis
    bla "Calypso straddles your face and begins to ride it, finally surrendering herself fully to pleasure."
    ca "O-Ooohh..."
    ca "O-Ohh gods, t-this is good..."
    ca "T-This is... divine..."
    mct "My fucking god, I want to devour her whole..."
    mct "I want to taste every inch of her body..."
    mct "It's like... I can't get enough of her..."
    ca "*Whimpering* Nnnghh... this is... m-madness..."
    ca "W-What are you doing to me...?"
    mc "Mmhhh..."
    ca "*Moans* AAagh..."
    play sound wood2 volume 0.2
    play sound2 clothes3oily
    $ renpy.music.set_volume(0.5, channel='soundloop3')
    play soundloop3 wetting5 fadein 2 
    scene calyh15 with dis2
    bla "Calypso pulls herself down, grabbing your head tightly and pushing your face between her cheeks even more." with dis
    cabt "AAAaghh... uhhh... aaAAaahhhh..."
    cabt "Ohhh [mc_dash]..."
    cabt "P-Please do not stop..."
    mct "Not a chance, my Princess..."
    mct "Even if my tongue goes numb..."
    mct "Even if I can't speak for hours after... I'm not stopping until you cum."
    cabt "Nnn-nnngg-gghhh..." with hpunchsubtle
    cabt "*Shuddering* Y-Yesss..."
    mct "My god, she's soaking me..."
    mct "And I fucking love it..."
    cabt "*Moans* AAAAAAaaaAaanhhhh..."
    cabt "M-More..."
    cabt "{size=47}MORE..."with hpunch
    $ renpy.music.set_volume(0.9, delay=2.0, channel='soundloop3')
    scene calyh16 with dis2
    bla "Her hips move faster as she feels the climax drawing near, replacing what began as commanding control with raw, lascivious desperation." with dis
    casc "*Moans* AAahhh..."
    casc "*Squeals* AAAaannngghhhhHHh...!"with hpunch
    casc "S-Sweet heavens... h-have mercy..."
    mct "She's so fucking delicious..."
    casc "AAaahhh..."
    mct "Now cum for me, Princess..."
    casc "B-By the Ancients, [mc]..."
    casc "W-Where did a... h-human learn to do t-that..."
    casc "*Shaking violently* AAAahh..."with hpunch 
    casc "*Voice breaking* I-I can... feel it..."
    casc "I-I am going to..."
    casc "T-To... finish..."
    casc "I cannot... h-hold back..."
    mct "Yes..."
    casc "AaAahhh..."
    casc "*Louder* AaaAGGhhHhhh..." with hpunchsubtle
    ca "{sc=4}*Screaming out* AAAGGHhhHhHhhHHH..." with hpunch 
    stop soundloop3
    stop soundloop
    play sound squirt
    play sound3 squirt
    play sound2 impactwood volume 0.3
    scene qc108
    ca "{sc=5}*Orgasming* AAAAAAaaaAAaaaGggGGhHHHhhh..." with hpunchl 
    play sound3 squirt
    ca "{sc=5}*Still orgasming* AAAaAAaGgGGhHHHhh..." with hpunch
    play sound3 squirt
    ca "{sc=5}*Still orgasming* HhnnnNnNnNnghhh..." with hpunch
    ca "{sc=2}H-Hah–" 
    stop music2b fadeout 20
    play soundloop2 rain3 fadein 16
    play sound clothes3 volume 0.5
    scene qc 108c
    ca "*Catching her breath* Hah..." with dis2
    ca "*Exhausted* B-By Vaelthir's grace, [mc]..."
    ca "*Exhausted* T-That was..."
    ca "*Exhausted* D-Divine..."
    show qc 108c2
    mc "*Muffled voice* Mdid myou... cum?"
    scene qc 108c
    ca "I-I think that..."
    ca "I-I think I have released enough tension to fuel the sorcery of the entire realm for a decade..."
    show qc 108c2
    mc "*Muffled voice* Mmmgood..."
    play sound knock3
    if arannisfriend:
        ara "*Knocking on the door* [nickname]!" with hpunch
    else:
        ara "*Knocking on the door* Human!" with hpunch
    scene qc 109
    ca "*Whispers* W-What?!" with dis12
    mc "*Whispers* F-Fuck, was that Arannis?!"
    $ renpy.end_replay()
    play sound knock3
    ara "*Knocking on the door* Open the door!" with hpunch
    ca "*Whispers* Why is he here?!"
    mc "*Whispers* I don't know!"
    mc "*Whispers* D-Do you think Lorelei... told him?!"
    ca "*Whispers* What? No! She would never!"
    play sound3 knock3
    ara "*Knocking on the door* HUMAN!" with hpunch
    play sound wood2
    play sound2 chair2
    scene qc 110
    mc "*Standing up* General! I-I'm here!" with dis15
    ara "Open the door, now!"
    mc "J-Just a second! I'm coming!"
    mct "Oh shit, this doesn't sound good..."
    scene qc 111
    mc "*Whispers* G-Get down! Hide behind the bed!" with dis
    mc "*Whispers* If he sees you here like this, I'm dead!"
    mc "*Whispers* We're both dead!"
    show qc 112
    ca "*Whispers* Hide behind the bed...?"
    ca "*Whispers* As if I was some... tavern wench?"
    show qc 111
    mc "*Whispers* Would you prefer to be caught in the human's quarters at this hour?!"
    ca "*Grumbling* Hmph..."
    show qc 112
    ca "*Muttering* This is so degrading..."
    play sound3 clothes3
    scene qc 113
    bla "Despite her pride, the Princess finally ducks behind the bed." with dis15
    play sound dooropenclose
    play sound2 armorwalk
    scene qc 114
    bla "As soon as you unlock the door, General Arannis storms into the room, visibly agitated." with dis15
    mc "Uhh... G-General."
    show qc 115
    ara "The Princess!" with hpunch 
    ara "Where is she?!" with hpunch 
    if not arannisfriend:
        ara "What have you done to her?!"with hpunch 
    scene qc 114
    mc "I-I-I don't know! S-She's not here!"
    mc "I-I haven’t seen her since the ceremony! She was supposed to create a portal for me to return home, but she never came!"
    mc "I've been here, waiting! A-Alone!"
    play soundlow thunder fadein 2
    show qc 116
    ara "*Muttering* Curses..." with dis14
    ara "*Muttering* Am I too late...?"
    show qc 117
    mc "*Playing dumb* Uhh... maybe she needed rest? It's been a... long day."
    mc "Have you checked her chambers? "
    scene qc 115
    ara "She is not there."with dis12
    ara "Listen — we must find her immediately."
    show qc 114
    mc "Why...? What's going on?"
    mc "Did something happen?"
    show qc 115
    ara "There is no time for explanations."
    ara "If you see her, tell her to go to the Shrine of Lorithien."
    ara "Do you remember it? The ruins where we trained your first day here."
    show qc 114
    mc "I remember."
    show qc 115
    ara "My daughter is already headed that way."
    ara "Tell the Princess to go there unseen."
    ara "If I do not arrive by midnight, they must flee. Without me."
    show qc 114
    mc "Wait, what? What the hell's going on??"
    show qc 115
    ara "Not now."
    ara "Find the princess, deliver the message, and then... return to your world."
    ara "Go. Now!" with hpunch 
    play sound dooropenclose
    scene qc 118
    bla "Arannis storms out." with dis15
    mct "What the hell...?"
    play sound footsteps4
    scene qc 119 with dis2
    ca "*Emerging from behind the bed* That was... strange." with dis
    show qc 120
    mct "Damn, she got dressed fast..."
    scene qc 130
    mc "So... any idea what that was about?"
    show qc 119
    ca "I have no clue, but... I know General Arannis."
    ca "He would not act in such haste without reason."
    ca "I will go to the place he mentioned. I trust his judgment."
    show qc 130
    mc "Good call."
    mc "I’ll try to find him, and tell him I passed the message."
    mc "Maybe then he’ll calm down and explain what’s going on."
    mc "And don’t worry about the portal back to Earth, let’s sort this out first."
    show qc 119
    ca "Wise idea."
    scene qc 130
    mc "And..."
    play soundlow thunder fadein 2
    mc "Well, before we go charging off to gods-know-what, I just wanted to say..."
    mc "I really... enjoyed what happened between us."
    mc "And... I’m glad I could help you. I mean... I believe I did."
    mc "And don’t worry, I’ll take the secret to the grave."
    mc "Not a soul will ever hear about the royal moans echoing in the human's chambers."
    show qc 131
    ca "*Smirks* Hmph." with dis15
    show qc 132
    ca "You are a quick learner, [mc]."
    show qc 131
    mc "Thanks. I like to think I get a little less stupid each day."
    ca "*Chuckle* Hmph."
    show qc 132
    ca "I too... enjoyed it. Thoroughly."
    ca "I must thank you for your... enthusiastic cooperation."
    show qc 131
    mc "It was my pleasure, Your Grace..."
    show qc 132
    ca "I must admit you... became quite the fascinating specimen, [mc]."
    if harempath:
        ca "I am beginning to understand why your women are drawn to you."
    show qc 131
    mc "Thank you, Your Grace."
    mc "The feeling is certainly mutual..."
    show qc 132
    ca "Actually..."
    ca "There is... much more I wish to say, but... as you said, later."
    ca "Until later... my knight."
    show qc 131
    mc "See you soon, Princess..."
    play sound dooropenclose
    scene qc 110
    bla "Calypso leaves the room with her usual grace." with dis2
    mct "{i}My knight..."
    mct "God, the way she said that..."
    mct "I need to find Arannis fast so I can go back to her ASAP."
    mct "It was weird to see the General so agitated."
    mct "Now, where did he go..."
    mct "I think he headed towards the kitchens...?"
    stop soundloop2 fadeout 13
    play soundloop fireplace fadein 6
    scene qcc 1 with dis33
    bla "You wander the halls of the fortress for several minutes, only to find nothing but deserted corridors and hollow echoes." with dis2
    mct "Something's off here..."
    mct "I haven't seen a single guard since I left the room."
    mct "It all feels... disturbingly quiet."
    play sound2 metalgate2 fadein 0.5
    scene qcc 2 with dis17
    mc "Hmm..." with dis12
    mct "Even the kitchens are empty. Like everyone just vanished mid-bite."
    mct "This isn't normal..."
    play sound2 metalgate2 fadein 1
    mct "I've gotta–"
label guardattack09reset:
    mc ". . ."
    play soundlow ["<silence 0.5>", risingshort5b]
    show 09attackbehind with dis2
    pause 4
    call screen qteguardhyrilar with dis17
label guardlose09:
    stop soundloop
    stop soundlow fadeout 0.5
    play sound5 debris3
    play sound8 dodge
    play sound7 stab
    play sound6 punch2
    play sound3 blood3
    scene black with hpunch 
    pause
    play sound coinflip
    pause 0.8
    play soundlow glitch4
    scene caveglitch2
    pause
    play soundlow glitch4
    scene caveglitch2
    pause 0.4
    play soundloop fireplace
    scene qcc 2
    jump guardattack09reset
label guardwin09:
    stop soundlow fadeout 0.5
    play sound5 debris3
    play sound8 dodge
    play sound7 bonebreak
    play sound6 punch2
    play sound4 punch2
    play sound3 blood3
    scene qcc3 
    gua "{sc=3}G-GGHhh!" with hpunch 
    play music2 ["<silence 2>"]
    queue music2 hwar
    play sound3 fallfull
    play sound sworddrop
    play sound2 leathershort
    scene qcc4 
    bla "You react on instinct, unleashing your powers and sending your attacker crashing to the ground." with pdd
    show qcc 5
    mc "Well, well, well..."
    mc "If it isn't the guy who got a little too excited stringing me up!"
    mc "You should’ve made your move before Thanatos taught me how cowards like you fight, bud. I’m not getting caught off guard again."
    show qcc 6
    gua2 "Y-You cursed demon..."
    gua2 "I-I knew from the start you were no ordinary human!"with hpunch 
    show qcc 5
    mc "Yeah, I've got a few tricks up my sleeve."
    mc "Now, tell me — where is everyone? Why's the fortress empty?"
    mc "Was attacking me your idea, or are you following orders?"
    show qcc 6
    gua2 "Shut your mouth, you f-fiend!"with hpunch
    gua2 "We will soon exterminate your cursed kind from the continent!" with hpunch 
    show qcc 5
    mc "Call me whatever the fuck you want, but I will not ask twice."
    mc "Talk or..."
    show qcc 6
    gua2 "Kill me if you want. I'm not afraid!"
    gua2 "Our cause is worth more than my life!"
    show qcc 5
    mc "Cause...? What cause?"
    mc "Is someone attacking Hyril'ar?"
    show qcc 6
    gua2 "Suck my cock, vermin."with hpunchsubtle
    gua2 "I'm not telling you anything."with hpunchsubtle
    play sound2 metalgate2
    play sound armorwalk2
    show qcc 7
    bla "Someone else enters the kitchen." with dis15
    show qcc 8
    mc ". . ." with dis14
    scene qcc 9
    ara ". . ."with dis14
    mct "Oh shit... this isn't good."
    mc "U-Um... this isn't what it looks like, General."
    mc "He came at me first! From behind!"
    mc "He tried to kill me!"
    play sound debris3
    play sound2 run
    scene qcc 12
    bla "Seizing the moment of distraction, the elven guard slips back into the corridor from which he came." with dis12
    mct "Motherfucker..."
    show qcc 11
    mc "Sir..." with dis12
    mc "I-I know how this looks, and yeah, you’ve got every reason to doubt me, but... I swear to God, he attacked me."
    mc "Outta nowhere! No warning, no reason!" 
    show qcc 10b
    ara "*Worried sigh* Sir Pyrand is not even supposed to be in Iskhaldrim..."
    ara "The betrayal must run even deeper than I feared..."
    show qcc 11
    mc "What...?"
    mc "What do you mean?"
    mc "Do you... believe me...?"
    show qcc 10
    if arannisfriend:
        ara "I do."
    else:
        ara "I might not like you... but I do."
    ara "Some among my ranks have turned against us."
    ara "It appears a portion of the Royal Guard has betrayed Hyril’ar. Likely in league with enemies beyond our lands."
    show qcc 11
    mc "Oh fuck..."
    mc "And what are they planning to–"
    mc "Wait..."
    mc "T-The Princess! That’s who they’re after, isn’t it?!" with hpunchsubtle
    show qcc 10
    ara "We must find her immediately."
    ara "Her life could be in grave danger."
    show qcc 11
    mc "She... I-I saw her! Just a moment ago!"
    mc "I told her to go to the place you mentioned!"
    show qcc 10
    ara "That is good."
    ara "My daughter awaits her there, but... the situation has changed."
    ara "If they do not know about this treason, they may send someone she trusts... and strike when she lowers her guard."
    ara "You have seen it yourself — these men know nothing of honor."
    show qcc 11
    mc "Yeah... they know they wouldn’t last five seconds against her in a straight fight. They'll surely use some dirty tricks."
    mc "We must hurry up."
    mc "I can get there before they do. I can move faster in this form."
    show qcc 13
    gua2 "*Distant voice* There! He's over there!" with dis12
    gua2 "*Distant voice* Follow me!"
    mc "Fuck, they found us!"
    mc "Is there another way out?"
    ara "...It is too late for that."
    ara "You better grab one of my swords, son."
    play sound soldiers2
    scene qcc 14 with dis2
    bla "In the blink of an eye, a tide of soldiers surges in, completely surrounding you and Arannis." with dis14
    mc ". . ."
    ara "Bastards..."
    show qcc 16 
    ara "What is the meaning of this treachery, Pyrand?" with dis12
    ara "Speak!"
    show qcc 15
    gua2 "Treachery? {i}You{/i} are the one who has turned against Hyril'ar, General."
    gua2 "You and that traitorous Princess you so blindly defend!"with hpunchsubtle
    show qcc 16
    ara "How dare you..."
    ara "The Sy-Tel-Quessir have governed Hyril’ar with wisdom and strength for millennia!"with hpunchsubtle
    ara "Their blood runs with the legacy of our ancestors!"with hpunchsubtle
    show qcc 15
    gua2 "That legacy has long since rotted, and you know it, Arannis."
    gua2 "Her line has driven this realm into decay and weakness for generations."
    gua2 "And now she even mingles with humans? Even Queen Aola, whore as she was, would not have dared to sink so low."
    gua2 "Lord Sylax will lift Hyril'ar from the ashes and restore our dominion across the continent!"
    show qcc 16
    ara "You fool..."
    ara "You speak of strength, and yet all I see is delusion and madness."
    ara "You will all pay for this betrayal."
    show qcc 15
    gua2 "No, we will not."
    gua2 "But all of Calypso's sycophants will not be here to see it."
    gua2 "By dawn, Hyril’ar will belong to those unafraid to shed blood for a future unshackled by weakness."
    gua2 "So... tell me, General."
    gua2 "Do you stand with us... or do you die with the human?"
    show qcc 17
    gua2 "Your choice..." with dis17
    ara ". . ."
    mc "G-General?"
    ara ". . ."
    if arannisfriend:
        ara "...How fast can you run in that... demonic form, [mc]?"
    else:
        ara "...How fast can you run in that demonic form, human?"
    mc "Fast enough that they won’t even see me strike."
    mc "We can take them down."
    ara ". . ."
    ara "...Good."
    ara "I need you to slip past their lines and head straight for the Princess."
    ara "Tell her to flee to Vael’Thalas Hold. She’ll find sanctuary there and... allies loyal to the crown. Redveil and Ilvenmyr will not turn against us."
    mc "What?? No! I'm not going anywhere!"
    mc "I will fight!"
    ara "You might be fast and strong, human, but you're not invincible."
    ara "There could be hundreds of them. Maybe even thousands."
    ara "Every second you hesitate, the danger upon the Princess and my daughter grows bigger."
    mc "No!"
    mc "I won't let you fight alo–"
    play sound debris3
    scene qcc 18
    ara "ENOUGH!" with hpunch 
    if arannisfriend:
        ara "Have you already forgotten what I taught you?"with hpunchsubtle
        ara "To fight is not to always swing your blade! The right decision must be made in the right moment!"with hpunchsubtle
        ara "I..."
        scene qcc 17
        ara ". . ."with dis14
        ara "I am... I am begging you."
    else:
        ara "I am giving you an order, human!" with hpunchsubtle
        ara "I..."
        scene qcc 17
        ara ". . ." with dis14
    ara "Without the Princess, this entire realm will fall into darkness."
    ara "My daughter... our future..."
    ara "You must..."
    ara "You must save them. Only you can."
    mc "I..."
    play sound3 flashback3 volume 0.7
    scene idrielarannis
    pause 0.35
    mc ". . ."
    scene qcc 22 
    mc ". . ."with dis
    scene qcc22
    mc "*Nods*"
    scene qcc 19
    ara ". . ." 
    scene qcc19
    ara "*Nods*"
    play sound leathershort volume 0.5
    scene qcc 24 with dis15
    pause
    play sound2 speed
    play soundlow debris
    scene qcc 25 with hpunch
    pause .6
    show qcc 26 
    bla "At Arannis' urging, you use your powers to slip through the guards like a bolt of lightning, racing towards Calypso." with dis25
    gua "W-What in the realms..." 
    gua2 "He disappeared!"
    gua "Demon! No human can wield such magic!"
    play sound armorwalk2
    show qcc 27
    bla "Arannis raises his sword and retreats a few steps until he finds himself trapped in the corner." with dis25
    scene qcc 28
    ara "Forget about the human! Do you want my head? Come get it!"with hpunch
    ara "Which one of you has the courage to stain his hands with blood?"with hpunch 
    ara "Strike me now before the eyes of the Ancients!"with hpunch 
    ara "Let the gods bear witness to your treason!" with hpunch 
    play sound7 thunder volume 0.6 fadein 2
    show qcc 29
    bla "A slow wave of uncertain glances and trembling hands ripples through the soldiers as they face their former General."with dis15
    gua2 ". . ."
    gua ". . . . ."
    syl "Halt!" with hpunch 
    play sound3 soldiers2
    show qcc 30
    bla "The soldiers suddenly fall into formation in perfect unison, swiftly clearing a path for their new commander." with dis2
    play sound2 armorwalk2
    play sound4 metalgate2
    scene qcc 31 with dis25
    syl "Aaahh..." with dis17
    show qcc 32
    syl "We meet again, Morning Sword." with dis15
    show qcc 34
    ara "Sylax... you parasite..." with dis
    ara "Are you the architect of this madness?!"
    show qcc 32
    syl "The time has come for a change, Arannis."
    syl "And deep down, you know it as well as I do."
    scene qcc 36
    syl "But let it never be said that Lord Sylax lacks mercy." with dis
    syl "Drop your weapon now, and I shall spare your life... and your daughter’s."
    show qcc 34
    ara "You have already proven your word is as solid as ash, traitor."
    ara "I will not heed the words of one who turned against his kin."
    show qcc 38
    syl "We bear no hatred for you, nor for your bloodline, General."
    syl "Any elf who would stand with us... for the salvation of Hyril'ar... shall be treated with honor and welcomed into the new dawn we will forge."
    show qcc 39b
    ara ". . ."
    ara "Hmph."
    show qcc 39
    ara "Speak then. What are your terms?"with dis
    show qcc 38
    syl "You will be stripped of all rank and title, but you and your daughter shall be granted safe passage beyond our borders."
    syl "You have my word, bound by the old rites."
    show qcc 34
    ara "The Old Houses will never bow to you."
    ara "They will remain loyal to the true heir."
    show qcc 33
    syl "*Mocking chuckle* Mm-hm."
    show qcc 32
    syl "I hold dominion over nearly the entire Royal Guard."
    syl "Thirinvale and Ysion have already pledged allegiance to our cause."
    syl "And as we speak, dissidents are being rooted out from the capital."
    syl "By the break of day, a new banner shall fly across every bastion of Hyril'ar."
    show qcc 35
    ara "A throne won by blood and treachery is a throne cursed to ruin."
    ara "You will all destroy this realm from within."
    ara "And when you realize that... it shall already be too late."
    play sound swordmove
    show qcc 37
    syl "Do not mistake rebirth for ruin."with dis 
    syl "It was Raewyn who doomed this realm... not me."
    syl "I will raise it anew from the ashes he and his daughter left behind."
    play sound2 swordmove
    show qcc 38
    syl "But... enough words."with dis 
    show qcc 36
    syl "Your own men have betrayed you, Arannis."with dis 
    syl "You stand alone."
    show qcc 38
    syl "Surrender and tell us where the Princess and that human went to..."with dis 
    syl "...or die."
    show qcc 34
    ara "If you seek blood, then draw your blade, Sylax!"
    ara "I will show you the true strength of Hyril'ar!"with hpunch
    show qcc 32
    syl "*Laughs coldly* How brave..."
    syl "Ahh..."
    syl "Arannis, Hammer of Iron. The Morning Sword."
    syl "General of the legions of Hyril’ar since the end of the Second Era."
    show qcc 39b
    syl "They said no blade could touch you."with dis12
    syl "They said you were able to end a cavalry battalion single-handedly with but a sword in hand."
    syl "You were a legend, once."
    syl "But..."
    show qcc 32
    syl "That was long ago, was it not, my friend?"with dis12
    syl "Your prime lies buried in the past."
    show qcc 39b
    syl "You have grown old, Arannis... even for an elf."with dis12
    ara ". . ."
    syl "We both know how this ends."
    syl "You cannot win. {i}She{/i} cannot win."
    syl "Hyril'ar demands rebirth."
    ara ". . ."
    syl "Now lay down your weapon... and tell us where the human has gone."
    syl "This is your final chance to save your life... and your daughter's."
    ara "Hmh–"
    ara ". . ."
    stop music2 fadeout 12
    play sound2 clothes3
    play soundlow leather2 volume 0.3
    scene qcc 40 with dis27
    bla "After some hesitation, Arannis finally lowers his sword." with dis2
    ara ". . ."
    ara "Forgive me... Your Grace."
    show qcc 33
    syl "*Chuckles* Hmph."
    show qcc 32
    syl "You made the right choice, Arannis."
    syl "I promise you that–"
    ara "Three thousand six hundred and thirty."
    show qcc 38
    syl "Huh?" with dis
    play sound7 thunder volume 0.5 fadein 2
    show qcc 40
    ara ". . ." with dis22
    ara "Hmph."
    play music ["<silence 1>"]
    queue music mastermind2 
    ara "Three thousand six hundred and thirty years have I walked this world."
    ara "I have traversed lands whose names no longer remain on the tongues of men, orcs, dwarves, or elves."
    ara "I have known power, glory, and the respect of nations."
    ara "I have had everything I could have ever wished for."
    ara "And yet..."
    show qcc 42
    ara "Never have I felt more alive than in these final years." with dis17
    ara "Never have I known greater joy than the day my daughter first opened her eyes to the world."
    show qcc 40
    ara "And..."with dis17
    ara "Never have I felt such honor as when King Raewyn, with his dying breath, entrusted me with the protection of his only daughter..."
    ara "...the rightful heir to Hyril'ar..."
    ara "Lady Calypso."
    ara ". . ."
    ara "Hmph."
    ara "Three thousand six hundred and thirty years in this world..."
    play sound7 thunder volume 0.8 fadein 2
    play sound6 sword2 fadein 1
    show qcc 41
    ara "And not once did I imagine that my last stand would be shielding the retreat of a human." with dis2
    ara "But... I will gladly lay down my life without hesitation..."
    show qcc 42
    ara "...if it means watching you dragged into the pit from which you came." with dis17
    ara "As long as Lady Calypso is alive..."
    ara "Hyril'ar shall never be yours."
    syl ". . ."
    play sound sword fadein 1
    show qcc 43
    syl "You have made your choice, old fool." with dis12
    syl "I will see your head impaled beside your wretched daughter’s... and the Princess’ as well."
    syl "I always knew you'd meet your end heeding the commands of that whore you so blindly pledged to protect."
    syl "Even if it meant shielding a nauseating human... or drowning in a pit of filth."
    show qcc 41
    ara "Oh, well..."
    ara "I never once doubted that, either."
    play sound bow
    play sound2 sword3
    play sound3 ["<silence 0.2>", sword2]
    play sound4 soldiers2
    show qcc 44
    syl "*Grinding his teeth* You insufferable relic..." with dis15
    syl "{sc=3}{b}{size=30}Kill him."
    ara ". . ."
    stop soundloop fadeout 5
    stop music fadeout 12
    scene black with dis3
    show screen afewminuteslater with dis17
    pause
    play soundloop2 rain5 fadein 6
    $ renpy.music.set_volume(1, channel='soundloop3')
    play soundloop3 rain3 fadein 6
    hide screen afewminuteslater
    scene qcc 44b 
    with dis3
    pause
    play sound water5
    play sound2 pantingb fadein 2
    scene qcc 45 with dis2
    mc "*Panting* (O-Okay... I made it...)" with dis15
    mct "This is where I trained with Arannis the first day..."
    mct "But..."
    mct "F-Fuck, there's no one here."
    mct "Did Calypso and Lorelei escape already? Or... were they caught...?"
    mc "*Shouting* P-Princess Calypso...?!" with hpunchsubtle
    show qcc 46
    mct "Goddammit... there's no way they can hear me over this fucking rain." with dis12
    mct "And I can forget about finding footsteps or horse tracks."
    play sound2 ["<silence 0.8>", thunder2]
    show qcc47
    mct "The ground's already turning to sludge."
    mct "And of course, to top it off, now the storm's picking up..." 
    mct "Fucking great..."
    mcsc "CALYPSO!!!" with hpunch 
    ca "You see? I told you it was not simply thunder."
    scene qcc 48
    mc "Huh??" with dis
    play sound2 water
    show qcc 49
    ca "Hmm?" with dis12
    show qcc 50
    ca "What are you doing out there in this downpour, [mc]?"
    show qcc 49
    mc "Oh, thank god!"
    show qcc 50
    ca "Come here, you fool, before you fall ill standing out there like that."
    show qcc 49
    mc "Y-Yes!"
    play sound water5
    stop soundloop3 fadeout 3
    play music2 hyrilartension fadein 6
    scene qcc 51
    bla "You walk to where Calypso and Lorelei shelter from the rain." with dis22
    mc "*Still catching your breath* Oh thank f-fucking god..."
    mc "*Still catching your breath* You're still alright..."
    show qcc 52
    ca "By the ancients, [mc], you are completely drenched."
    ca "You should change out of those wet clothes at once."
    show qcc 51
    mc "T-There's no time for that!"
    mc "Listen, we... we need to move. Now."
    mc "I don't even know where to start, but..."
    mc "W-We were attacked. Hyril'ar... is under attack."
    play sound water
    show qcc 53
    ca "Excuse me...?" (multiple=2) 
    lo "What?!" (multiple=2) with dis12
    ca "By whom?!"
    show qcc 54
    mc "It's... it's coming from the inside. A coup."
    play sound6 thunder fadein 2
    mc "The regent... that motherfucker, Sylax, from the trial!"
    mc "He’s the one behind the coup. He rallied most of the royal guard to his side."
    mc "They launched a coordinated strike across the realm tonight, all at once."
    mc "I don’t know how many turned, but it’s bad. Really bad."
    show qcc 55
    ca "B-But how..."
    ca "I mean, my advisors warned me that this could happen, but..."
    ca "...Never so soon."
    ca "They said they were a negligible minority."
    show qcc 54
    mc "I don’t know how deep it goes. I don’t know who we can trust."
    mc "But I know this much — they’re after {i}you{/i}, Calypso."
    mc "You're the only one standing in their way. They want you dead."
    show qcc 55
    ca "By the ancestors..."
    ca "We must return to the palace immediately."
    ca "We need to stop this."
    show qcc 54
    mc "No!"
    mc "You can’t go back! Not now!"
    mc "We don’t know who’s loyal and who’s waiting to stab you in the back!"
    mc "I saw it myself. They have no honor!"
    mc "We need to flee and come up with a plan. NOW."
    show qcc 56
    lo "B-But..." with dis12
    lo "That is not possible."
    lo "The royal guard answers to my father."
    lo "He would never turn against Princess Calypso."
    show qcc 57
    mc "I know. And he didn't. He was betrayed."
    mc "He’s the one who told me to warn you and to get you out of here."
    mc "When the attack started, the other soldiers turned on us, and he..."
    mc "He... stayed behind. Bought me enough time to reach you."
    play sound water
    show qcc 58
    lo "W-What?!" with dis
    lo "Where is he now?! My father!"
    show qcc 59
    mc "I-I don't know."
    show qcc 58
    lo "What do you mean you don't know?!"
    lo "Sylax will have him killed!"
    show qcc 59
    mc "General Arannis wouldn’t go down like that."
    mc "And... even if he was captured, he’s too valuable to kill outright!"
    mc "If you go back and get caught too, we won't be able to help him!"
    mc "I..."
    mc "I promised him I'd get you to safety."
    play sound water
    play sound2 chair2
    play sound3 ["<silence 0.4>", wood2] volume 0.33
    scene qcc60
    bla "Calypso drops onto a nearby chest, her leg trembling from anxiety." with dis15
    ca "AgGgghh..."
    ca "*Muttering* {i}Vell’arai..."
    ca "*Muttering* What am I supposed to do now...?"
    play sound6 thunder fadein 2
    casc "Sylax... you... wretched, honorless {size=33}SCUM!"with hpunchsubtle
    casc "I should have had you killed a long time ago!" with hpunch
    scene qcc 61b
    lo "Lady Calypso..."with dis12
    scene qcc60
    mct "I've never seen Calypso like this..."with dis12
    mct "So... overwhelmed. So anxious."
    ca "*Muttering* How did it come to this..."
    ca "*Muttering* Every one of them swore an oath before the gods themselves..."
    ca "*Muttering* Traitors..."
    ca ". . ."
    ca "*Muttering* I need to... find allies..."
    ca "*Muttering* Someone must still be loyal..."
    ca "*Muttering* But how can I know who to trust...?"
    menu:
        with dis
        "Say nothing":
            mc ". . ."with dis
            ca "*Muttering* Okay..."
            ca "*Muttering* I must act..."
            ca "*Muttering* I will not... let my realm fall..."
            ca "*Muttering* Not like this..."
            ca "Enough."
        "Urge her":
            mc "I don't want to push you, Princess, but..."with dis
            mc "Every second we spend here, they get closer."
            mc "We need to leave {i}now."
            ca "Yes, yes, I know..."
            ca "I know..."
            ca "*Muttering* Okay..."
            ca "*Muttering* I must act..."
            ca "*Muttering* I will not... let my realm fall..."
            ca "*Muttering* Not like this..."
            ca "Enough."
        "Quote Arannis' words \n[calypso_pts]":
            $ calypso_points += 1
            mc "General Arannis said only you could prevent this realm from falling into darkness."with dis
            mc "He believed in you, even with everything falling apart."
            mc "And so do I."
            scene qcc 60
            ca ". . ." with dis
            ca "Yes..."
    stop music2 fadeout 6
    play sound thunder fadein 2
    play sound3 chair2
    play sound2 water
    scene qcc 62
    ca "*Standing up* Y-Yes." with dis12
    ca "Enough!"with hpunchsubtle
    ca "You are right. I am the Princess of the Sy-tel-quessir!"
    ca "We need to move, and we need to move now."
    ca "I will not let them win."
    show qcc 63
    mc "Yes!"
    mc "That's the Calypso I know!"
    show qcc 62
    ca "Lorelei, go fetch whatever supplies you can from the horse breeders’ pantry."
    ca "And quickly!"
    ca "We will depart the moment you return."
    show qcc 65
    lo "Y-Yes! At once, Your Grace!"
    play sound water
    play sound3 spell3
    play sound2 spell2
    play soundloop energy2 fadein 1
    show qcc 66
    bla "As Lorelei leaves to get the supplies, a portal flares open behind you." with dis12
    show qcc 67
    mc "Nice!"
    mc "Where is this portal going? Ekabar?"
    show qcc 66
    ca "Yes. Same as the one I opened this morning."
    show qcc 67
    mc "Perfect! From there, I should be able to teleport back to Earth."
    mc "Once we gather everyone, we’ll have more than enough brainpower to figure out a counterattack."
    mc "In the meantime, you and Lorelei can stay at the same inn where you–"
    show qcc 66
    ca "The portal is only for you, [mc]."
    show qcc 68
    mc "Eh...?" with dis
    mc "Wait, what?"
    play sound thunder fadein 2
    show qcc 69
    ca "Have you already forgotten the struggle I endured attempting to return to Hyril’ar after you freed me from my imprisonment?"
    ca "I do not even recall how I managed it in the end."
    ca "I... I cannot risk becoming trapped on the other side again."
    show qcc 68
    mc "B-But... you can't stay here!"
    mc "They want to kill you, Calypso!"
    show qcc 69
    ca "There is no guarantee I could return here once more."
    ca "At least, not immediately. It could take months of meditation to find the path back, if I find it at all."
    ca "I will not abandon my people to save myself."
    ca "That decision is final."
    show qcc 68
    mc "But..."
    mc ". . ."
    stop soundloop fadeout 6
    play sound2 water5
    scene qcc 63
    mc "*Approaching her* Aggh..." with dis17
    mc "Alright, fine!"
    mc "I know you well enough to know once your mind's made up, there's no point in arguing."
    mc "Okay... listen carefully — I was saving this for after we were safe in Ekabar, but I guess the plans just changed."
    mc "Arannis told me where to go."
    mc "We need to head towards..."
    menu:
        with dis
        "[gr]Vael’Thalas Hold":
            $ calypsosafeplace += 1
            mc "Vael’Thalas Hold? I think that was the name."with dis
        "Andor Vale":
            mc "...Andor Vale? I think that was the name."with dis
        "Thalorin Enclave":
            mc "Thalorin Enclave? I think that was the name."with dis
    mc "He said you'd find allies there. People you can trust."
    mc "He was sure some of the old families would never betray the crown. Ilvenmyr and..."
    menu:
        with dis
        "Ysion":
            mc "Ysion."with dis 
        "[gr]Redveil":
            $ calypsosafeplace += 1
            mc "Redveil."with dis 
        "Thirinvale":
            mc "Thirinvale."with dis 
    ca "Hmph."
    show qcc 62
    ca "I see..."
    ca "That is valuable information."
    show qcc 63
    mc "Still, don’t let your guard down. Trust no one."
    mc "Only me. And Lorelei."
    show qcc 64
    ca "Yes. I shall be cautious."
    ca "Thank you, [mc]."
    ca "I will..."
    play sound water
    show qcc 70
    bla "Calypso turns away, her voice quieter now." with dis15
    ca "I will..."
    ca "I will never forget what you have done for us."
    ca "For me."
    ca ". . ."
    ca "Thank you."
    ca "Now go."
    mc "What...?"
    ca "Use the portal, and return to your world."
    mc "You don't get it, do you?"
    mc "I wanted to leave through a portal because I thought it was the safest option for you."
    mc "But if you’re afraid you might not find your way back to Hyril’ar..."
    mc "Then fine. We’re not leaving. I’m not leaving."
    mc "We'll fix this. Together."
    ca "Please. Do not make this harder than it needs to be."
    mc "I'm not going anywhere, Calypso."
    mc "You're not doing this alone."
    ca ". . ."
    ca "*Snorts* Hmph."
    play sound water5
    scene qcc 71 with dis25
    play sound2 thunder fadein 2
    bla "Calypso leans against the wall, a wistful smirk on her face." with dis17
    ca "*Chuckles* Mmh-mph..."
    mc "Calypso...?"
    ca "Hmph."
    $ renpy.music.set_volume(0.3, delay=25.0, channel='soundloop2')
    $ renpy.music.set_volume(0.11, channel='music')
    play music romanticcalypso 
    $ renpy.music.set_volume(1, delay=11.0, channel='music')
    show qcc 72
    ca "Heavens..."
    ca "I am pathetic." 
    show qcc 71
    mc "What? No, you're not."
    mc "Why do you say that?"
    ca "Hmph."
    show qcc 72
    ca "This burden is too heavy for me, [mc]."
    ca "My father reigned for centuries, you know? Unshaken."
    ca "And I... I have managed to unravel it all in less than a decade."
    show qcc 71
    mc "This is not your fault."
    show qcc 72
    ca "How is it not?"
    ca "I possess everything others could only dream of. A kingdom. Wealth beyond measure. The blood of Anima herself flows through me."
    ca "And yet... look at what I did with it."
    ca "If it had not been for a human who stumbled onto my path by accident, I would still be caged."
    show qcc 71
    mc "People like to call it luck when they don’t want to admit their own strength. Or fate, when they can’t accept they fought their way through hell to get where they are."
    mc "But remember, if you’re standing where you are right now, it’s because you deserve to be here."
    mc "It’s okay to feel overwhelmed. It’s okay to lean on someone else — hell, I’ve done it more times than I can count."
    mc "But even when you need help... don’t forget, it’s {i}you{/i} who has gotten yourself this far. People step in because of who you are."
    mc "And I'm here, Calypso. Whatever happens... I've got you."
    play sound water
    play sound2 water4
    show qcc 73
    ca ". . ." with dis2
    ca "Why do you insist so much, [mc]?"
    ca "This is not your war."
    ca "You already have your own battles to fight. The Founder. Lord Bardot. Thanatos... the Gems."
    mc "Your war became mine the moment you became part of my life."
    ca ". . ."
    ca "Hah..."
    ca "I would leave it all behind, you know?"
    ca "*Her voice trembles* The crown. The halls of my ancestors. Even the stars above Hyril’ar that have watched over me since my birth."
    ca "Everything."
    mc "Then... do it. Come with me!"
    ca ". . ."
    ca "I do not want to be a Princess, [mc]. I never did."
    ca "All my life I have felt like I do not belong here."
    ca "And yet..."
    ca "I have to save Hyril'ar. For my people."
    ca "I cannot run from the smoke when I was born to put out the flames."
    mc "You shouldn't have to burn just because someone decided it was your role to carry the torch."
    mc "You don't owe anything to anyone."
    ca "But... I do. Even if you cannot understand."
    ca "I..."
    play sound water4b
    play sound2 water4
    scene qcc 74
    ca "I-I must still thank you, you know?" with dis2
    ca "Thanks to you... I now know I can be something else."
    show qcc 75
    mc "Calypso..."
    show qcc 76
    ca "Lady Alexandra teaching me how to kick. Lady Dalia, to bake. Lady Annie, to whistle like a mockingbird." with dis12
    ca "Every... absurd, beautiful moment I spent with you, [mc]..."
    ca "I laughed. I stumbled. I... lived."
    show qcc 77
    ca "I have..." with dis12
    ca "I have walked this world for eighty years, yet all of them felt like a quiet, endless void."
    ca "A thousand sunrises, and not one of them warmed me."
    show qcc 78
    ca "Until... you." with dis 
    ca "You showed me that life can be different."
    ca "That it does not have to be a prison."
    ca "You showed me that... the chain can be broken."
    play sound water5 fadein 1
    play sound2 water4
    show qcc 79
    ca "*Approaching you* So..." with dis22
    ca "I-If you truly mean the things you say..."
    ca "When this is all over..."
    ca "When Hyril'ar is saved..."
    ca "I will walk away from everything."
    ca "I will shatter the chain."
    ca "And I will... come back to you."
    mc ". . ."
    mc "Ca–"
    play sound water
    play sound2 water4
    show qcc 80
    bla "Calypso leans in, her lips finding yours in a deep, breath-stealing kiss." with dis2
    mc ". . ."
    play sound3 water4b
    play sound5 clothes3oily
    show qcc 81 with dis22
    show screen heartbeat
    play sound4 beat
    $ calypsou = True
    mc ". . ." with dis14
    play soundlow thunder fadein 2
    scene qcc 82
    cabt "Mmmmm..." with dis25
    show qcc 83
    cabt "Hmmm..." with dis12
    play sound water5 fadein 0.5
    play sound2 clothes
    scene qcc 84
    bla "Pulling away from a kiss that felt suspended in time, Calypso takes a few slow steps back, her eyes still locked on yours."with dis22
    mc "Wow..."
    mc "That felt... so... right."
    mc "Like it was always meant to happen."
    play sound water
    mc "*Trying to approach her* I–" with hpunchslowsubtle
    mc "What the–"
    play sound2 water
    mc "Wait... why can't I move...?"with hpunchslowsubtle
    mc "W-What... what have you done?!"
    play sound water4b
    play sound2 water4
    show qcc 85
    ca "The Princess of Hyril'ar falling for a human. Can you believe it?" with dis12
    ca "If they wanted my head before, they will certainly want to burn me at the stake now."
    ca "Not to mention some of my ancestors, who are assuredly now rolling in their tombs."
    ca "But... who cares, huh?"
    scene qcc 86
    mc "*Trying to move* T-This is your doing?!"
    mc "Let me go!"
    show qcc 85
    ca "I will keep my end of the promise."
    ca "You better keep yours, too. Do not dare die on me."
    show qcc 86
    mc "Don't {i}you{/i} dare push me into that portal, Caly..."
    ca "*Chuckles* Mm-mh."
    scene qcc 85
    ca "Tell your women to save me a seat at the table, would you?"
    play sound water
    scene qcc 86
    mc "CALYPSO!!!" with hpunch 
    play sound6 risingshortbb
    play sound5 water4b
    play sound7 water4
    play sound4 thunder fadein 2
    pause .4
    play sound2 debris
    scene qcc 87 with dis03
    show wormholecaly with Dissolve(.2)
    stop music fadeout 9
    stop soundloop2 fadeout 9
    pause 9

label mcisback:
    if mcleaveshy1:
        scene qw55
        stop soundloop fadeout 5
        stop soundloop2 fadeout 5
        play sound risingshort4
        pause 2
        stop music2 fadeout 2
        stop music2b fadeout 2
        scene login3 with flash
        pause 8
    elif mcleaveshy2:
        play sound risingshort4
        stop music2 fadeout 2
        stop music2b fadeout 2
        scene login3 with dis22
        pause 6
    play soundloop night fadein 5
    play soundlow whoosh4
    scene white with dissolve
    $ renpy.music.set_volume(0.33, channel='soundloop3')
    play soundloop3 forest fadein 9
    if mcleaveshy1 or mcleaveshy2:
        scene qcc 88 with Dissolve(2.5)
    else:
        scene qcc 91 with Dissolve(2.5)
    play sound4 ["<silence 2.4>", howl] volume 0.3
    pause 1.3
    $ renpy.music.set_volume(1, delay=15.0, channel='soundloop2')
    if mcleaveshy1:
        player "And then... BAM! Right into the dragon's heart!" with dis17
        player "That spear hits like a kick in the head!"
        scene qcc 89
        player2 "Fuuuuck yeah!" with dis12
        player2 "Who needs the Xeno event when we can just kill this overgrown gecko!"
        player "Say goodbye to your 9-to-5s, gentlemen."
        player "By this time tomorrow, we're gonna be richer than William Bardot!"
    elif mcleaveshy2:
        player "Alright, alright! The moment has come, gentlemen!" with dis17
        player "Is everyone ready?!"
        scene qcc 89
        player2 "I'm locked and loaded, baby! The Killerdragon Spear's thirsting for blood!"with dis12
        player3 "I bought a new gambeson just for this!"
        player "It is time, then! To the dragon's den!"
        player2 "Blood and glory!"
    else:
        player "Okay. New plan. We apologize to the dragon." with dis17
        player "Maybe bring a fruit basket."
        scene qcc 92
        player2 "Shut the fuck up, dude, I'm done with your plans!"with dis12
        player2 "Jareth got roasted like a chicken because of you!"
        player "Yeah..."
        player "His wife's not gonna like this..."
    mct "Ekabar..."
    mct "I... I'm back."
    play sound snow
    play sound2 debris
    show qcc 94
    if mcleaveshy1 or mcleaveshy2:
        mc "*Standing up* (And... I was right.)" with dis15
    else:
        mc "*Standing up* (And... Calypso was right.)" with dis15
    mct "I can feel it..."
    mct "My teleport power's back. I can jump in and out of Eternum again."
    mct "But... I can't sense Hyril'ar."
    mct "It’s that same weird feeling... like when I was stuck there, cut off from both Eternum and Earth."
    mct "Now I'm cut off from there."
    mct "Why is Hyril'ar different...?"
    play sound leathershort volume 0.1
    scene qcc 94b
    if mcleaveshy1 or mcleaveshy2:
        $ calypsopath = False
        mct "Well..." with dis14
        mct "Not much I can do about it right now, I guess."
        mct "And I can't simply retain Calypso forever. She needs to be with their people, in her homeland."
        if mcleaveshy1:
            mct "I can only hope she can handle those “problems” and come back to us soon."
        else:
            play sound leathershort volume 0.1
            scene qcc 94
            mct "Although..." with dis14
            mct "I can't help but feel like that goodbye was kinda... awkward?"
            mct "Was she really hinting at... something sexual?"
            mct "No... no way. “Horny Calypso” doesn't even sound like a real thing."
            mct "Not our Calypso."
            mc ". . ."
            mct "Right...?"
            mc ". . ."
            play sound leathershort volume 0.1
            scene qcc 94b
            mct "Hmph, well, I guess I can only hope that she can handle those “problems” and come back to us soon." with dis14
        scene qcc 90
    else:
        mct "Damn you, princess..."with dis14
        mct "In the end you always have to get your way, huh?"
        play sound leathershort volume 0.1
        scene qcc 94
        mc "*Sighs* Ahh..."with dis14
        mct "I guess now we have another reason to get those damn Gems of Doom."
        mct "The Founder, Bardot... even Thanatos. I'm sure they’re all after Hyril’ar."
        mct "They want Calypso. They want her power."
        play sound leathershort volume 0.1
        scene qcc 94b
        mct "But I won’t let them."with dis14
        mct "I’ll pull her out of that life, no matter what."
        play sound leathershort volume 0.1
        scene qcc 94
        mc "*Sighs* (But for now, I guess all I can do is wait... and hope she can hold her own in that war and get back to us soon.)" with dis14
        mct "If anyone can do it... it's her."
        scene qcc 93
    mct "In any case... now I need to get back home immediately." with dis15
    mct "I lost track of time while I was there, but I've been gone way too long, that's for sure."
    mct "God, I can't wait to see the girls again."
    mct "Please don’t let it be one of those “time-dilation” nightmares where it’s actually been ten years and they’ve all moved on..."
    stop soundloop fadeout 6
    stop soundloop3 fadeout 7
    scene black with dis3
    show screen sometimelater with dis2
    pause
    play soundloop2 birds fadein 3
    hide screen sometimelater
    scene qo 1 
    with dis33
    mct "Man..."with dis14
    mct "It feels good to be back in Kredon."
    mct "Feels like it’s been forever, even if it really hasn’t."
    mct "There’s SO much I need to tell them. Like, where do I even start...?"
    scene qo 2
    mc "*Sighs* (I just hope things didn’t get rough while I was gone.)" with dis15
    mct "I always figured they'd assume I got caught up in some last-minute mission or something, so I hope that's the case."
    mct "Who knows, maybe they didn't even notice I was missing."
    scene qo 1
    mct "Although... well, I hope that's not the case either." with dis15
    mct "Like... I don’t want them to be sad or anything, but I kinda hope they at least noticed."
    mct "Just a little. Enough to miss me, but not enough to actually worry or feel like crap about it."
    mct "Yeah. That sweet spot in the middle."
    stop soundloop2 fadeout 5
    play sound keys
    stop music2 fadeout 3
    play soundloop clock2 fadein 4
    show qo 3 with Dissolve(2.5)
    play sound2 doorclose
    mc "Um..." with dis
    mct "Why do I feel nervous...?"
    mc "Hello...?"
    bla ". . ."
    mct "Hmm, maybe they're playing Eternum?"
    mct "But Nova's bag is there. And Alex's bike is parked out front, so they've gotta be here."
    show qo 4
    bla "You hear a faint noise coming from the living room." with dis12
    mct "Was that Penny's voice?"
    scene qo 5 with dis25
    pause
    scene qo 6
    a ". . ." with dis15
    scene qo 7
    no "Mmm-mm-mhh..."
    no "*Talking in her sleep* ...Told you... the numbers..."
    play soundloop2 penclickfast volume 0.5
    scene qo8
    d ". . ."
    x ". . ."
    stop soundloop2
    scene qo 9
    p ". . ."
    scene qo 10
    n ". . ."
    play sound mouse
    scene qo10
    n "Hmm?"
    play sound2 mouse
    scene qo10
    n "Hmmph..."
    scene qo 9
    p ". . ."
    show qo 11
    p "So..."
    p "Nothing yet?"
    show qo 12
    n "Nothing yet."
    show qo 9
    p "Hmph."
    show qo 11
    p "I thought Maximo would’ve found something by now."
    show qo 12
    n "He did report back. Came back empty-handed. So I sent him again."
    n "I got all my men out asking around for sightings of [nickname]."
    show qo 11
    p "And...?"
    show qo 12
    n "...Nothing yet."
    show qo 9
    p "Hmph."
    show qo 10
    n ". . ."
    play soundloop2 penclickfast volume 0.5
    scene qo8
    d ". . ."
    stop soundloop2
    show qo 9
    p ". . ."
    show qo 11
    p "Maybe we should just go back to Ekabar. Ask again."
    show qo 12
    n "We already tore apart every inch around the inn where he vanished."
    n "And the whole area near the Citadel in Valley of Kings."
    show qo 11
    p "So..."
    p "Maybe other servers?"
    show qo 12
    n "Ulysses has 488 official servers, most of them bigger than entire countries."
    n "Wandering around aimlessly won’t help anyone."
    show qo 13
    p "Yeah, well, but it's better than nothing, isn't it?" with dis
    show qo 12
    n "It's... still nothing."
    n "It's better to stay here and be ready to move the second we get a real lead."
    show qo 13
    p "So that's it?"
    p "Really??"
    show qo 14
    p "We're just gonna sit here and hope [mc] strolls through the d–"with dis
    show qo 15
    mc ". . ."
    show qo 15b
    mc "Erm..."with dis08
    show qo 16
    mc "S-Surprise!" with dis
    show qo 17
    p ". . ."
    scene qo 18
    n ". . ."
    play sound couch
    play sound6 clothes3
    play sound5 rubbody
    scene qo 19
    d ". . ." (multiple=2)with dis 
    x ". . ."(multiple=2)
    play sound2 couch
    play sound4 couch 
    play soundlow rubbody
    play sound3 clothes3
    show qo 20
    no ". . ." (multiple=2)with dis 
    a ". . ."(multiple=2)
    show qo 16
    mc ". . ."
    show qo 21
    mc "O-Okay, I know you must be shocked and probably kind of pissed that I disappeared for so many days without warning..."with dis
    mc "But I've got a good reason!"
    show qo 22
    mc "Brace yourselves, because you're not gonna believe it..."
    show qo 22b
    mc "{size=40}HY—{w=0.2}{nw}" with hpunchsubtle
    mc "{size=40}HY—RIL—{w=0.2}{nw}" with hpunchsubtle
    mc "{size=40}HY—RIL—AR!" with hpunch
    play sound slam2 volume 0.77
    show qo22b2
    mcsc "{size=50}HYRIL'AR IS REAL!" with hpunchsubtle
    scene qo 19
    d ". . ." (multiple=2)
    x ". . ."(multiple=2)
    scene qo 23
    mc ". . ."
    scene qo 22b
    mc "O-Okay, so, listen. I was in Ekabar with Caly, right? Then outta nowhere Thanatos attacks us, and then Calypso goes like {i}BOOM{/i} !!" with dis08
    mc "Next thing I know?"
    play sound slam2 volume 0.77
    scene qo22b2b
    mc "BANG! We're in freaking Hyril'ar! Oh, and my teleport powers?" with hpunchsubtle
    play sound slam2 volume 0.77
    scene qo22bb
    mc "BLAM! Gone! Just like that! Then people there start going craaaazy, and what do they do?" with hpunchsubtle
    play sound slam2 volume 0.77
    show qo22b2c
    mc "BOOM! They throw me straight into jail! I spent like four days in there! Then there's like a trial, and oh, guess what?" with hpunchsubtle
    play sound slam2 volume 0.77
    scene qo22bc
    mc "WHAM! Of course, it's rigged as fuck! They sentence me to death!" with hpunchsubtle
    play sound slam2 volume 0.77
    scene qo22b2d
    mc "They were THIS close to executing me, like, holy fuck, I had the rope around my neck! And just when I thought, yup, this is it, I'm fucking toast..." with hpunchsubtle
    play sound slam2 volume 0.77
    scene qo22bd
    mc "BLAM! Calypso shows up at the last second!" with hpunchsubtle
    scene qo22bd_2
    mc "A-And then... then..."
    show qo 20
    no ". . ." (multiple=2)
    a ". . ."(multiple=2)
    show qo 23
    mc ". . ."
    show qo 24
    mc ". . ."
    show qo 18
    n ". . ."
    show qo 24
    mc ". . ."
    show qo 22
    mc "Um..."with dis08
    show qo 21
    mc "Are you alright...?"
    show qo 22
    mc "Why is no one saying anything...?"
    show qo 25
    a ". . ."
    show qo26
    bla "Annie’s lips tremble as she begins to sob, breaking the suffocating silence." with dis
    $ renpy.music.set_volume(0.2, channel='music3')
    $ renpy.music.set_volume(1.0, delay=10.0, channel='music3')
    play music3 ["<silence 2.7>"]
    queue music3 romanticreturn
    stop soundloop fadeout 2
    play sound noisehug
    play sound2 chair3
    scene qo27
    allofthem "{sc=4}{size=44}[mc!u] ! ! ! ! !" with hpunchlong
    p "Where were you?!{w=0.18}{nw}" with hpunchsubtle
    a "Why did it take you so long?!{w=0.18}{nw}" with hpunchsubtle
    no "We thought Ulysses Benjamin'd you!{w=0.18}{nw}" with hpunchsubtle
    p "We were so worried!{w=0.18}{nw}" with hpunchsubtle
    a "Please don't ever do this again!{w=0.18}{nw}" with hpunchsubtle
    no "I almost joined a cult!{w=0.18}{nw}" with hpunchsubtle
    p "We thought something happened to you!{w=0.18}{nw}" with hpunchsubtle
    a "I even went to a church to pray!{w=0.18}{nw}" with hpunchsubtle
    no "I checked the dead persons database twice!{w=0.18}{nw}" with hpunchsubtle
    p "Why didn't you take me with you?!{w=0.18}{nw}" with hpunchsubtle
    a "I cried so much!{w=0.18}{nw}" with hpunchsubtle
    no "I counted the hours! All 209 of them!{w=0.18}{nw}" with hpunchsubtle
    p "We missed you so much!" with hpunchsubtle
    scene qo 28
    mc "*Chuckle* Hmm." with dis 
    mct "Damn... they really were worried about me."
    if daliapath:
        play sound punch volume 0.6
        play sound2 whoosh3b
        scene qo29
        bla "Dalia punches you hard on the arm." with hpunch 
        mc "Ouch!"
        scene qo 30
        d "*Sobbing* I-I swear... if you {i}ever{/i} do this again..."
        d "*Sobbing* I'll kill you myself, you hear me?!"
        d "*Sobbing* A-Are we clear?!"
        scene qo 29
        mc "Dalia..."
        show qo 30
        d "*Sobbing* A-And you better have a damn good explanation!"
    if alexpath:
        scene qo 31
        if daliapath:   
            x "She's right." with dis12
        else:
            x "You son of a bitch..."with dis12
        x "If you ever disappear for more than 24 hours again without telling us where you are..."
        x "*Voice breaking* I-It’ll be the {i}last{/i} thing you ever do!"
        show qo 32
        no "Oh my god..." with dis14
        no "E-Even Alex is crying! I thought I'd never see this!"
        play sound impactwood
        play sound2 whoosh3b
        show qo 33
        xsc "*Sobbing* S-Shut up!" with vpunchslow 
        xsc "*Sobbing* I-I'm not crying, dammit!"
        mc "Alex..."
    n "You have no idea of what these girls have been through, [mc]."
    show qo 34
    mc "Nancy..."with dis12
    show qo 36
    n "I always thought of myself as someone optimistic, but..."
    n "Day after day, morning after morning, without a single word from you..."
    show qo 35
    n "It takes a toll, you know?"
    if harempath:
        n "These girls are strong, [mc], but even they have a breaking point."
    show qo 34
    mc "I'm... I'm so sorry."
    mc "I never meant for any of this to happen."
    mc "I-I wanted to reach out. I tried. But I lost my powers. I had no way to communicate, no way to–"
    show qo 35
    n "*Choked-up chuckle* We know you would've contacted us if you could've. None of this is your fault, honey."
    n "But... Hyril'ar? Wow, you've got some serious explaining to do."
    show qo 34
    mc "Oh, you have no idea..."
    mc "Go prepare some coffee for everyone, Nancy."
    mc "This is going to be one hell of a story."
    show qo 35
    n "You got it."
    if lunapath:
        show qo 36
        n "But first... you should go find Luna."
        n "She should be on her way back by now."
        show qo 34
        mc "Of course!"
        mc "Where is she?"
        show qo 36
        n "She went to her father’s place to get some food for all of us."
        n "You’ll probably run into her if you head that way."
        show qo 35
        n "We... we owe her more than we can ever repay, [mc]."
        n "Every time someone broke down, Luna was there."
        n "She held us all together with just... a smile. Like it was nothing."
        n "She never stopped smiling. She never cried."
        n "That gave us strength. It gave us... hope."
        show qo 34
        mc "She’s always had that gift."
        mc "The world can be crumbling, but somehow, when she smiles... it feels like everything’s okay again."
        mc "I'm..."
        mc "I'm so happy to see you all again, Nancy. You have no idea."
        show qo 35
        n "And we’re happy to have you back, [mc]."
        n "Now go, go!"
        n "And don’t take too long! We {i}need{/i} to hear everything you’ve been through!"
        show qo 34
        mc "I will! I promise!"
        mc "I'll be right back!"
        play soundloop town_ambience fadein 6 volume 0.3
        scene qo 37 with Dissolve(3.3)
        bla "You quickly make your way towards Loco's Cafe."with dis2
        mct "God..."
        mct "I knew I missed them..."
        mct "But seeing their faces again, hearing their voices, feeling their hugs... it made me realize just {i}how{/i} much I missed them."
        mct "I need to find Luna and head back to tell them everything."
        scene qo 38
        mct "Mr. Hernandez's restaurant is that way..." with dis17
        mct "If she’s already heading home, she should be coming down this street."
        mct "Unless she–"
        play sound3 caraway2 volume 0.55
        show qo 39
        bla "The bus in front of you finally drives off, leaving the lane open." with dis25
        mc "Huh...?"
        scene qo 40
        mct "I think I know that girl!" with dis15
        mc "*Waving* Luna!"
        show qo 41
        l "Hmm...?" with dis06
        show qo 42
        l ". . ." with dis17
        l "...[mc_dash]...?"
        mc "*Running towards her* Luna!"
        mc "I'm back!" 
        l ". . ."
        mc "I’m so, SO sorry for disappearing like that."
        mc "Calypso and I got into a fight with Thanatos, and after that... I was trapped. Locked away in a dungeon in Hyril’ar for DAYS."
        mc "There was no way to communicate. No way to let you guys know I was okay."
        mc "A-And I know it’s been hard here too... so I’m sorry for making you go through all that pain."
        mc "But Nancy told me how you were the one who kept everyone together. How your strength helped them stay sane."
        mc "So... thank you. Thank you so much."
        mc "God, I missed you more than I could ever put into words."
        l ". . ."
        mc "N-Now let's go home! I have so much to tell you!"
        mc "And you're not gonna believe half of it!"
        l ". . ."
        show qo 43
        l ". . ." with dis15
        mc "Hey... Luny, are you okay?"
        show qo 44
        l "Y-Yeah, I just..."
        l "*Voice trembling* I just need a second."
        l "P-Please, don't look at me."
        show qo 45
        mc "*Taking a step forward* What...? What do you mean?"with dis15
        l ". . ."
        mc "Hey..."
        scene lunacry with dis2
        pause 3.5
        lsc "*Sobbing* . . . . .{w=3.5}{nw}" with dis2
        play sound clothes3
        play sound2 clothes5b volume 0.6
        play soundlow bagdrop
        scene qo 46 with dis
        bla "Without saying another word, you gently wrap Luna in your arms, as she starts crying inconsolably on your shoulder."with dis
        lsc "*Crying* A-Aahh...I...I-I d-don't..."
        mc "*Soothing* Shhh... it's okay..."
        lsc "*Crying* I..."
        if anniepath:
            scene qo 50
            lsc "*Crying harder* I-I had a vision of you... I s-saw you!" with dis2
            lsc "*Crying* B-But I-I also know my powers don’t work on you." 
            lsc "*Crying* S-So I thought..." 
            lsc "*Crying* I t-thought maybe..." 
            lsc "*Crying* M-Maybe the visions where I saw you were wrong." 
            lsc "*Voice cracking* I-I thought m-maybe my mind m-made it up." 
        lsc "*Crying* I... I-I w-was so scared, I-I..."  
        lsc "*Crying* I-I thought..." 
        lsc "*Crying harder* I t-thought I'd never see you again." 
        if anniepath:
            scene qo 46
            mc "Luna..."with dis2
        else:
            mc "Luna..." 
        mct "She’s been carrying all this weight by herself..."
        mct "Putting on a smile every day... just so no one else would break down."
        mct "Just like she’s always done..."
        lsc "*Crying* I-I'm... I'm... I'm so sorry."
        lsc "*Voice breaking* I-I t-tried to... I-I tried to s-stay strong."
        lsc "*Crying* But then I s-saw you... and I... I c-couldn't hold it."
        lsc "*Crying* A-And now..."
        lsc "*Crying* Now my dad's tacos are all over the sidewalk."
        play sound clothes3
        show qo 47
        mc "*Choked-up laugh* D-Don't be silly." with dis17
        show qo 48
        l "*Sniffling* I-I'm sorry. I-I didn’t w-want to make you feel... bad."
        show qo 47
        mc "You didn't do anything wrong, Luna."
        mc "It's just... damn, I've seen way too many of you crying today."
        mc "And seeing you like that... I guess it broke me." 
        play sound2 clothes3
        show qo 46
        bla "You hold Luna even tighter." with dis2
        mc "You can cry as much as you want, Luna."
        mc "You don't have to hide your emotions with me, I told you."
        l "*Sobbing* I know."
        mc "I don’t want you to smile when you don't want to."
        mc "You can be real with me. Always."
        mc "I want you to never hold anything back. I want you to be the real you."
        l "*Sobbing* I-I know."
        mc "Oh, babe..."
        scene qo 49 with dis3
        mc "I love you, Luna." with dis2
        mc "And I promise you this, right here and now..."
        mc "I will never make you cry again."with dis12
        stop soundloop fadeout 13
    else:
        show qo 34
        mc "*Deep exhale* Now where do I begin..."
    stop music3 fadeout 9
    jump cafe09poshy

label cafe09poshy:
    scene black with Dissolve(3.8)
    pause 
    show screen afewdayslater with dis25
    pause
    play soundloop forest2
    hide screen afewdayslater
    scene qi 1
    with dis33
    play music2 happy18 
    pause 
    scene qi 2
    mc "Hmm... "with dis22
    if money >= 0:
        if money < 99:
            mct "I've only got [money] eternals left in my uWallet."  
            mct "I'm borderline rat-tier broke."
            mct "But... well, at least I don't really have any major expenses."
        else:
            mct "I still have [money] eternals in my uWallet."  
            mct "Not exactly ballin’, but... it’s something."
        mct "Good thing I don’t have to worry about rent or bills."
    else:
        mct "Damn, looks like I was banned from Eternum due to my eternals account being overdue." 
        mct "Then again... I don’t need the neural implant anymore to dive into Eternum, so... I guess I should be fine."
    mc "*Scrolling through the news* Hmm..."
    play sound notificationphone
    show 09news1 at slide_fade_top
    with Dissolve(0.28)
    pause 
    play sound2 notificationphone
    show 09news2 at slide_fade_top
    hide 09news1
    with Dissolve(0.28)
    pause
    play sound notificationphone
    show 09news3 at slide_fade_top
    hide 09news2
    with Dissolve(0.28)
    pause
    hide 09news3
    mct "It’s almost impossible to find a headline that’s not about Eternum lately." with dis12
    mct "So many people living inside it... and all of them totally clueless about what’s really going on."
    mct "Makes me wonder — do they genuinely not know... or do they just not {i}want{/i} to know...?"
    if lunapath:
        show qi 3
        l "Sorry I took so long, there was a woman using the toilet." with dis
        scene qi 4
        $ unlock_look("luna", 13)
        mct "Good god... she really looks like an angel in this light." with dis12
        mc "You seriously don't deserve to live in a town where it rains 80%% of the time, Luna."
        show qi 5
        l "Right? I like the rain, although I must admit it's so nice when the sun actually decides to show its face!"
        show qi 4
        mc "Yep, it really changes everything."
        mc "Honestly, I could just stay here all day, soaking up the sun and doing absolutely nothing."
        show qi 5
        l "Yeah... me too."
        l "But I've gotta go already, sadly."
        show qi 4
        mc "No worries, I have to leave soon too."
        mc "Chang asked me to stick around for a bit so he can give me something, but once that’s done, I’ll head out as well."
        show qi 5
        l "Sounds good!"
        l "You're free to go whenever you want, I already paid for our breakfast."
        show qi 4
        mc "What?!"
        mc "I told you I'd pay this time!"
        show qi 5
        l "It's fine! You already paid for so many things."
        show qi 6
        l "Besides, Ruth didn’t even charge us for the sweets."with dis12
        l "I only paid for the coffees and my chocolate."
        show qi 7
        clerk "Tell that man if he ever makes you pay again, I’ll have him scrub dishes in the back!"
        clerk "He doesn't know how lucky he is!"
        show qi 5
        l "*Chuckle* She's just messing around."with dis12
        l "She knows you didn't force me to pay."
        show qi 4
        mc "*Chuckles* I mean, she has a point."
        mc "I wouldn't want Mr. Hernandez to think I'm treating his daughter poorly."
        show qi 5
        l "I wouldn't worry about that, my dad really likes you."
        show qi 8
        l "Although... he {i}did{/i} almost ask Uncle Hugo to rough you up the other day, but... that was just a big misunderstanding."with dis
        show qi 9
        mc "I-I'm sorry, what?"
        show qi 8
        l "Didn't I tell you?"
        l "My uncle and grandma came to Kredon a few days ago to spend Christmas with us."
        show qi 9
        mc "Yeah, I know that!"
        mc "I-I mean the part where I almost got roughed up."
        show qi 8
        l "Oh, well..."
        scene qi 10 with dis22
        show screen afewdaysearliercorner
        her "Más te vale que ese pinche pollo no se me cague en el sofá, Hugo." (what_style='textsp') with dis12
        scene qi 11
        unc "No te preocupes, mano, Pancho está bien educado." (what_style='textsp') 
        scene qi 10
        her "*Chuckles* Eso espero." (what_style='textsp') 
        scene qi 11
        l "Dad, I'm home!" 
        show qi 12
        her "Ah, mi amor, welcome back!" with dis 
        her "I left you some chocolate muffins in the kitchen — go eat before your uncle eats them all."
        show qi 10
        her "Anyways, we should probably head out to pick up mama at the airp–" with dis
        her ". . ."
        stop soundloop
        play sound jumpscare3b
        play music2 risinglong
        play sound2 musicstop
        play sound3 debris3
        show qi13
        her "WHAT IS THIS?!" with hpunch
        her "Oh, my sweet angel, what happened?!"with hpunch 
        scene qi 16
        l "Huh... what?"
        scene qi 13
        her "Your eyes! They're red!"
        her "I mean, not your pretty, sparkly, innocent angel eyes, T-THE WHITE PART!"
        her "YOU'VE BEEN CRYING!"with hpunch 
        show qi 15
        l "Oh... n-no, I haven't."
        l "Everything's fine!"
        show qi 13
        her "Don't lie to me!"
        her "You've got the crying eyes of abuela after her telenovela ended in 2018!"
        her "You've definitely been crying!" with hpunch 
        show qi 15
        l "Uh..."
        show qi 16
        l "O-Okay, okay, I cried a little bit, but it's not what you think!"
        l "It's about [mc]. He finally came ba–"
        show qi 13
        her "[mc]...?" with hpunch 
        show qi 17
        her "After I welcomed him into the family..."with dis08
        her "Let him into our house... offered him my food..."
        her "He then dares to hurt my baby's feelings...?!"
        show qi 18
        her "Hugo..."with dis
        show qi 19
        unc "Already on it, brother."
        show qi 20
        unc "Salamanca?" (what_style='textsp') with dis12
        unc "Órale, que tal. Mira, tengo una chamba para ti." (what_style='textsp')
        unc "[mc] [lastname]. En Kredon." (what_style='textsp')
        unc "El muy pendejo le hizo daño a mi sobrinita." (what_style='textsp')
        unc "Sí." (what_style='textsp')
        unc "Sí, que parezca un accidente. Sin testig–" (what_style='textsp')
        play sound whoosh3b volume 0.7
        play sound2 pop
        play music2 happy18
        scene qi21
        l "Enough!"with hpunch
        l "You're not even listening to me!"
        l "I did cry, but they were happy tears!"
        l "[mc] came back! I told you he was missing!"
        show qi 22
        her "O-Oh..."
        her "But... I thought you said you were convinced he was just busy doing some top-secret thing."
        her "You said that everything was alright."
        show qi 15
        l "Yeah, and... it was."
        l "Just that... I was happy to see him back. That's all."
        show qi 22
        her "Oh..."
        her "O-Of course, mi vida. That's totally normal."
        her "I'm so sorry for overreacting like that."
        play soundlow footsteps4
        show qi 23
        unc "*Clears throat* Salamanca?" with dis2
        unc "Cancel the job, false alarm."
        unc "Yes, it was just a misunderstanding."
        unc "Yes."
        unc "A-ha, that won't be necessary."
        unc "Oh... but since you're around, would you mind bringing us some taquitos from Carlos?"
        unc "Yes, carnitas."
        unc "Ahh, god bless you!"
        l ". . ."
        hide screen afewdaysearliercorner
        scene qi 4
        mc "*Gulps* I-I see." with dis2
        mc "I-I'm glad the misunderstanding was cleared up."
        scene qi 5
        l "Anyway, I really need to run now!"
        l "We probably won’t see each other for the next couple days, so... Merry Christmas!"
        show qi 4
        mc "Oh! For sure! Merry Christmas, Luna!"
        mc "I still can’t wrap my head around the fact that Christmas is basically here already."
        mc "This year went by too fast."
        show qi 5
        l "I know, right! It's been wild so far."
        show qi 4
        mc "Oh, don't forget — bring comfy shoes on Wednesday!"
        mc "I'll be at your place by 8AM!"
        show qi 24
        l "Like I'd forget!" with dis12
        l "You still don't want to tell me where we're going?"
        show qi 25
        mc "Nope! It's a surprise."
        mc "We had to cancel our movie marathon after my little “Hyril’ar incident”, so this is my way of making it up to you."
        show qi 24
        l "*Soft giggle* Alright then."
        l "I'm really looking forward to it."
        show qi 25b
        l "See you on Wednesday, [mc]!" with dis12
        l "And thank you again for joining me for breakfast!"
        show qi 25c
        mc "See you then, Luna!"
        mc "Tell Victor, Hugo, and your grandma I said hi!"
        show qi 25b
        l "Will do!"
        l "See you!"
        play sound doorsliding fadein 1
        play sound2 ["<silence 1.6>", storebell] volume 0.3
        scene qi 26 with dis2
        mct "Phew, I hope she likes the little outing I've planned." with dis12
        mct "While I was in Hyril’ar, she's the one who kept everyone grounded, even though she was just as scared."
        mct "She’s spent her whole life hiding her pain just to protect the people around her."
        mct "If anyone deserves a perfect day, it’s her."
        scene qi 2
        mc "*Grabbing your phone* Hmm..." with dis17
    else:
        mc "Hmm..."
    mct "Damn, it's already 10. And I'm supposed to meet the girls at 10:30."
    mct "Maybe I should text Chang to tell him I've gotta–"
    stop music2 fadeout 5
    play sound doorsliding fadein 1 
    play sound2 bird_flying
    $ renpy.music.set_volume(0.4, channel='music3')
    if changmicaela >= 4:
        $ cmlove = True
        play music avemaria fadein 3
        scene qi 28
        bla "A blinding light suddenly floods the terrace."with dis22
        mc "Hmm...?"
        scene qi 29 with dis25
        bla "A radiant figure steps forward, basking in an aura so intense you instinctively shield your eyes." with dis22
        mc "Wow..."
        play sound pop
        stop music
        play music3 quirkychang fadein 3
        scene qi 30
        bla "Or at least... that's the impression Chang gives you today."
        scene qi 31
        c "Aaahhh..."
        c "Kredon smells different today... like the morning after a storm."
        c "Clean. Fresh. Hopeful."
        c "*Sighs* Life is... beautiful indeed."
        show qi 30
        mc "*Snorts* You look especially radiant today, Chang."
        play sound chair4
        show qi 32
        c "*Sitting down* Well..." with dis
        c "I don't wanna brag, but... your boy Chang finally did it."
        c "Seven dates, and weeks of charming conversation, long walks, and perfectly timed jokes later..."
        c "Chang the Velvet Blade has finally unwrapped the mystery burrito."
        show qi 33
        mc "*Laughs* Wait, wait, are you saying what I think you’re saying?!"
        mc "Did you and Micaela... finally do it?!"
        show qi 32
        c "Oh, we did more than that, my friend."
        c "It was a night that would make poets weep and bards retire."
        c "A glorious blend of passion, heat, and only minor injuries."
        c "Three rounds, and every single one over the thirty-second mark. No mercy."
        show qi 33
        mc "*Laughs* Daaaaamn, bro!"
        mc "That's what I'm talking about!"
        mc "You've gotta tell me your secrets!"
        show qi 34
        c "No joke though, it feels like I’m dreaming." with dis
        c "Everything just... clicked, you know?"
        c "And it was Micaela’s first time too, so it really felt special."
        show qi 35
        mc "It totally shows, man. You’re glowing."
        mc "So... tell me, what’s the deal now?"
        mc "You guys just having fun, or... is it officially a thing now?"
        show qi 34
        c "Official as hell!"
        c "We haven’t dropped the news to her parents yet, but she told me herself — she wants to take this seriously."
        c "And I... I think I really love her, man."
        show qi 35
        mc "Dude... that's amazing."
        mc "I'm so happy for you, seriously."
        mc "You're in love. I can tell."
        show qi 34
        c "None of this would’ve happened without you, bro."
        c "You got me into one of the best schools around, paved my way into a top university, and now you helped me win Micaela’s heart."
        c "One day I'll pay you back, man. I swear."
        show qi 35
        mc "Please, you give me too much credit."
        mc "It was your irresistible magnetism and killer smile that did the trick."
        show qi 34
        c "Sorry for making you wait, by the way."
        c "I didn’t want to just text or call you about it — I wanted to tell you in person."
        show qi 35
        mc "And I'm really glad you did!"
        show qi 34
        c "I'll let you get back to your super busy, world-saving life now, no worries."
        play sound noise3 fadein 1
        show qi 36b
        c "But before I go..." with dis12
        c "Let it never be said that Chang the Homie is one of those dudes who forgets about his brothers when he gets a girlfriend!"
    else:
        play music3 quirkychang fadein 4
        scene qi 3
        c "Aaahhh..." with dis15
        scene qi 30
        mc "Ah, speak of the devil!" with dis12
        show qi 31
        c "Kredon smells different today... like the silence after a storm."
        c "Empty. Stagnant. And yet... there's something else in the air..."
        c "It's hope."
        show qi 30
        mc "*Chuckles* Damn, bro, you woke up poetic today."
        play sound chair4
        show qi 34
        c "*Sitting down* You bet I did." with dis
        c "Not gonna lie, I've been feeling kinda low these past few days, but that ends TODAY!"
        c "No more gloom! Chang the Optimist is officially back in action!"
        show qi 35
        mc "Now that's the spirit!"
        mc "What’s got you in such a good mood today?"
        mc "Could it be... something to do with a certain bicep-blessed beauty?"
        stop music3
        play sound slam2
        play music sad1
        scene qi 31b
        c ". . ."
        mc "Uhh..."
        mc "O-Or... perhaps not...?"
        c "I really tried, [mc]. I gave it my all."
        c "But... she said it’s not the right time. Not for her. Not for us."
        mc "Damn..."
        mc "I'm so sorry, man. I didn't mean to bring it u–"
        c "It's not your fault, [mc]."
        c "You backed me up the whole way. I know that."
        c "Sometimes... things just don’t work out the way we hope."
        c "Maybe in another universe... maybe in some other life, it would've been different."
        c "Maybe someday..."
        c "Maybe someday I get to be the Chang who ends up with her."
        stop music 
        play music3 quirkychang 
        play sound pop
        scene qi 34
        c "But I’m not gonna let one heartbreak take me down!" 
        c "I’ve got way too much to be thankful for!"
        c "I’m studying at one of the best schools in the damn world thanks to you!"
        c "People would trade an arm and a leg to be in my spot right now."
        c "One day I'll pay you back, man. I swear."
        show qi 35
        mc "Please, you give me too much credit."
        mc "You’re the one pulling the grades, putting in the work."
        show qi 34
        c "Still... thanks, bro."
        c "And sorry for making you wait, by the way!"
        c "I'll let you get back to your super busy, world-saving life now, no worries."
        play sound noise3 fadein 1
        show qi 36b
        c "But before I go..." with dis12
        c "Let it never be said that Chang the Homie forgets about his brothers!"
    play sound2 whoosh3b volume 0.4
    show qi 36
    c "TA-DA!!!" with hpunch 
    show qi 37
    mc "Hmph? What's that?"
    show qi 36
    c "Merry Christmas, bro!"
    show qi 37
    mc "What?!"
    mc "You got me a gift?!"
    show qi 36
    c "Damn right I did!"
    show qi 37
    mc "Duuuude, you can't do this to me!"
    mc "I didn't get you anything!"
    mc "And didn't you check the group chat? Nancy made us all swear on our lives that we wouldn't buy gifts this year to save money for the mission!"
    show qi 36
    c "Bah... then let's just call it a thank-you gift for hooking me up with the Student Exchange Program."
    c "Even better this way, to be honest, since  I couldn’t afford anything for anyone else."
    c "If anyone asks, just say Chang only celebrates Kwanzaa during the holidays. Or... Saturnalia."
    show qi 37
    mc "*Laughs* I don't deserve you, bro."
    show qi 36
    c "Come on, open it already!"
    play sound noise3 fadein 1
    scene qi 38 with dis2
    bla "You reach into the bag and pull out what looks like a board game box." with dis14
    mc "Oh my god."
    mc "*Laughs* Tell me this isn’t what I think it is."
    c "Behold... The Official Chang the Party Master Board Game!"
    mc "*Laughs* This is so awesome! How the hell did you make this?!"
    c "There's this shop in the mall where you can create custom board games. I sent in the design, wrote up the rules, picked out the materials... the whole shebang."
    c "It’s got over a hundred cards. Each one lovingly crafted by yours truly!"
    mc "Wow!"
    show qi 35
    mc "This is amazing!" with dis
    mc "Thank you so much, man!"
    show qi 34
    c "The best part? You don’t need a board or any complicated setup. Just the deck, some dice, and at least three fun-loving degenerates in a party mood."
    c "The Changermeister will do the rest."
    show qi 35
    mc "Uhh... I see, I see! So it's a party game, huh?"
    show qi 34
    c "Yep! Make sure to have something to drink!"
    show qi 35
    mc "Dude, this is perfect."
    mc "I’m going up to that lodge with the girls tonight. We’re totally playing this!"
    show qi 34
    c "I'm glad you like it."
    c "Let me know how it goes if you try it!"
    show qi 35
    mc "I will!"
    mc "I owe you a gift, man."
    show qi 34
    c "There's no need, bro."
    show qi 35
    mc "There is! Major need!"
    show qi 36b
    c "*Chuckles* Well, if you insist..." with dis12
    c "There is one tiny little favor you could do for me in return..."
    play soundlow whoosh3b volume 0.6
    stop sound fadeout 1
    show qi 39
    c "I need a full briefing on the upcoming plans for Chang's Nine." with hpunch 
    c "As the mastermind of this elite unit, it’s critical that I remain fully updated on your schedules, movements, and snack preferences."
    c "So... if you'd be so kind, please."
    show qi 40
    mc "*Chuckles* I see, that seems fair."
    mc "What exactly do you need to review?"
    show qi 41
    c "Everything. Everyone. Especially the heist this Wednesday."
    show qi 40
    mc "Hmm, alright, alright, let's see..."
    menu:
        with dis
        "Give him full details":
            play sound pop
            show screen s09plans1 
            mc "First off, as you know, Calypso's in Hyril'ar."
            mc "No way to reach her for now, and no idea when she’ll be back."
            mc "But... she will be. Eventually. She promised me."
            play sound pencilshort
            show qi39b
            c "Mm-hm."
            play sound pencilshort
            show qi39a
            c "Yes, I remember your report. Arannis, Lorelei, and... that Sylax dude."
            play sound pencilshort
            show qi39a
            c "*Writing* {i}Potential new threat..."
            scene qi 40
            hide screen s09plans1
            show screen s09plans2
            play sound pop
            mc "Annie flew back to the UK a few days ago to spend Christmas with her family and all, but she’s gonna be back before New Year’s Eve."
            show qi 41
            c "Ah, yes, she did..."
            play sound pencilshort
            show qi39a
            c "*Writing* {i}Text Annie."
            play sound pencilshort
            show qi39a
            c "*Writing* {i}Ask her to stop by Mom’s restaurant and grab chili oil."
            stop sound
            scene qi 39b2
            c ". . ."
            play sound pencilshort
            show qi39a
            if cmlove:
                c "*Writing* {i}Prep dan dan noodles for Micaela."
            else:
                c "*Writing* {i}Prep dan dan noodles for Raul and Noah."
            scene qi 40
            hide screen s09plans2
            show screen s09plans3
            play sound pop
            mc "Nova's doing the family thing too."
            mc "Some cousins are flying in from Scotland apparently, so her house must be chaos right now."
            play sound pop
            hide screen s09plans3
            show screen s09plans4
            mc "And same story with Luna."
            mc "Her uncle and grandma came to Kredon to spend the holidays with her."
            play sound pencilshort
            show qi39a
            c "Makes sense, makes sense. Family time’s important."
            scene qi 40
            hide screen s09plans4
            show screen s09plans5
            play sound pop
            mc "As for me, I’m spending Christmas Eve with Nancy, Penny, Dalia, and Alex. Even though... Alex doesn't know yet. It's a surprise."
            mc "Nancy made us swear not to get any gifts since we’re all broke and pressed for time, but we did manage to book this cozy little Airbnb up in the mountains thanks to a coupon."
            mc "We're heading out now."
            c "Hmm..."
            play sound pencilshort
            show qi39a
            if harempath:
                c "*Writing* {i}Potential harem conflicts. Possible heartbreak. Prepare emotional support package for [mc]."
            else:
                c "*Writing* {i}Potential jealous rage. Prepare emotional and physical support package for [mc]."
            scene qi 39b2
            mc "W-What?"
            scene qi 41
            c "Alright then, moving on!"
            c "Let's talk post-holiday. Wednesday's heist."
            show qi 40
            mc "Ah... right."
            hide screen s09plans5
            show screen s09plans6
            play sound pop
            mc "So... it’s gonna be you, me, and Luna hitting Ulysses Corp HQ in Kredon."
            mc "You’re probably more familiar with the layout than I am, but... here's the tech side."
            mc "Nova built a custom USB we need to plug into an access point to push our exploit into their internal network."
            mc "Once it’s in, we breach their intranet and start pulling data. Every department. Including the private archive tied directly to William Bardot’s machine."
            mc "Nancy worked her magic and got us interviews to get access to an executive's office, and Penny cooked up our resumes."
            mc "If it all goes well, we’ll get to know everything Ulysses and Bardot know."
            play sound pencilshort
            show qi39b
            c "Mm-hm."
            play sound pencilshort
            show qi39a
            c "All that's left on my end is finishing fine-tuning our fake identities."
            stop sound
            scene qi 41
            c "I'll send you the memos by tomorrow, most likely."
            show qi 40
            mc "Sounds good."
            if lunapath:
                play sound pop
                hide screen s09plans6
                show screen s09plans7
                mc "After the job, I’m taking Luna out for a little something special."
                mc "Kind of a... special “picnic” setup."
                play sound pencilshort
                show qi39a
                c "Ahh, good idea. Girls love thoughtful dates."
                if cmlove:
                    stop sound
                    scene qi 39b2
                    c ". . ."
                    play sound pencilshort
                    show qi39a
                    c "*Writing* {i}Plan picnic for Micaela. Add thermos of protein shake."
                hide screen s09plans7
            else:
                hide screen s09plans6
            show screen s09plans8
            scene qi 40
            play sound pop
            mc "And finally... possibly our last big mission."
            mc "The WRE obtained a strong lead on the last Gem of Doom, at last."
            mc "Apparently, it was found on Meiyo, the feudal Japan server."
            mc "But... whoever got it is good. Real good. Even Thanatos hasn’t been able to track them down yet."
            mc "So next weekend, it’s me, Nova, Alex, Penny, and Nancy heading in to find it."
            scene qi 41
            c "Uh-huh..."
            c "So... given that Annie pretty much carried the Big Hunt event with that big BOOM of hers..."
            c "By the end of January, we should have... five Gems, yeah?"
            scene qi 40
            mc "Correct. And that would leave only us and Thanatos. Five each."
            mc "And combining all of our efforts... I think we've got a real shot."
            mc "The ten Gems of Doom."
        "Give him the short version":
            mc "Alright... so, to keep it short..."with dis
            mc "Calypso's still in Hyril'ar, as you know."
            mc "Annie flew back to London for a few days to spend Christmas with her family — same with Nova and Luna."
            mc "And as for me, Nancy, Penny, Dalia, and Alex, we're going to a lodge nearby for the night. Just a short trip, we’ll be back tomorrow."
            play sound pencilshort
            show qi39a
            c "Interesting, interesting..."
            stop sound
            scene qi 40
            mc "Now, about our future missions..."
            mc "Well, don't forget, Wednesday morning we’re going to Ulysses HQ with Luna. We need to plug in the USBs Nova made to access their intranet."
            mc "We have to go in pretending to be job applicants."
            play sound pencilshort
            show qi39a
            c "Yes, all that's left on my end is finishing fine-tuning our fake identities."
            c "But it shouldn't be a problem."
            scene qi 40
            mc "And then this weekend, we’re visiting the Meiyo server. We finally got a lead on the last Gem of Doom."
            mc "So if we actually find it... and win the Big Hunt event... that’ll make five Gems for us."
            mc "And... if we somehow manage to get the five Thanatos has..."
            mc "That'll be it, man."
    mc "Endgame."
    play sound pencilshort
    show qi39b
    c "Mm-hm..."
    stop sound fadeout 1
    hide screen s09plans8
    scene qi 34
    c "Alright, sounds like you’ve got a solid grip on everything, buddy!" with dis15
    c "We got this!"
    show qi 35
    mc "Hell yeah, we do!"
    show qi 34
    c "Thanks for keeping me in the loop, man."
    c "And for letting me join the missions in the real world."
    show qi 35
    mc "Always, dude."
    mc "I told you, you might not play Eternum, but you're still one of us."
    mc "Chang the Anchor keeps this whole shitshow from falling apart!"
    show qi 34
    c "Heh... that makes me happy, bro."
    c "It really does."
    c "But anyway! I’ve already stolen enough of your time... and I still need to go find a new tie for Wednesday."
    c "So give everyone my regards and enjoy the snowy escape!"
    show qi 35
    mc "I will!"
    mc "And thanks again for the gift!"
    mc "I'll text you later!"
    play sound ["<silence 1.6>", storebell] volume 0.3
    play sound2 doorsliding fadein 1
    show qi 42 with dis25
    mct "Man, Chang really is the best." with dis17
    mct "Even with all the crazy stuff going on lately, and us seeing each other way less than we used to since I moved to Kredon..."
    mct "He's still always there for me. No questions asked."
    mct "I seriously owe that guy big time."
    mc "*Glancing at your phone* (Maybe I should–)"
    mct "Oh, shit, it's late as fuck!"
    mc "Ruth, coffee to go, please!"
    stop music3 fadeout 6
    play soundloop town_ambience fadein 5 volume 0.4
    scene qi 43 with Dissolve(3.3)
    bla "You hurry off to the meeting spot where Nancy said she’d be waiting." with dis15
    mct "Hope they didn't leave me behind."
    mct "I really don’t wanna end up spending Christmas Eve alone, gaming and eating pizza."
    mc ". . ."
    mct "Well... okay, that actually doesn't sound terrible, but still."
    play music happy18 fadein 6
    show qi 44 with dis2
    mc "*Rounding the corner* Ah, there they are!" with dis12
    mct "Yep, definitely a better plan..."
    scene qi 45
    mct "Uhh, are those matching outfits?" with dis12
    scene qi 46
    mc "Hey there!" with dis
    scene qi 47
    n "Ah, finally!" with dis12
    n "Welcome, honey."
    show qi 48
    mc "Sorry for the delay, I had to wait for a bit at the cafe to meet up with Chang."
    show qi 49
    p "No worries, Dalia and Alex aren't even here yet, so you're good."
    show qi 50
    mc "Oh, sweet."
    mc "*Chuckles* I'm glad I'm not the last one to show up for once."
    scene qi 47
    n "I'm sorry this Christmas Eve isn’t going to be anything special."
    n "With everything that happened, I didn’t have any time to prep or get any gifts or... anything, really."
    show qi 48
    mc "Are you kidding?"
    mc "Last Christmas, I had a cold kebab in the kitchen while my dad passed out on the couch in the middle of his tenth beer."
    mc "You could’ve dragged me to a holding cell tonight and I still would've called it an upgrade."
    mc "The mountain plan sounds amazing."
    show qi 47
    n "Well, I'm glad you feel that way."
    scene qi 49
    p "Plus, it’ll be nice to unplug from Eternum for a day."
    p "I’m not sure we’re gonna get many more moments like this anytime soon."
    show qi 50
    mc "Amen to that!"
    show qi 47
    n "I already tossed your bag in the trunk."
    n "Just need to throw mine in there, and we’re all set to go once the girls arrive."
    show qi 48
    mc "Ah, guess that’s where you stashed your warm clothes."
    mc "Even if Kredon’s still weirdly warm this season, something tells me your outfit’s not exactly built for mountaintops."
    show qi 51
    n "See? That’s exactly what I told Penny when she handed us these outfits." with dis
    n "This is too light for this time of the year."
    show qi 52
    mc "Wait, what?!"
    mc "She got them for you?! I thought we said no gifts this year!"
    show qi 53
    p "Okay, okay, okay, hold your horses, everyone." with dis
    p "First off, I got these for free just for posting an Insta story, sooo technically it's not a gift, since I didn't buy them."
    show qi 54
    p "And secondly, it's not that cold yet." with dis08
    p "It was still autumn literally three days ago!"
    show qi 49
    p "And besides, what's a little frostbite if we look cute, right?" with dis
    p "I'm sure [mc] gets it."
    show qi 50
    mc "*Chuckles* Oh, I totally get it."
    show qi 55
    p "By the way, what's that bag you're carrying?"with dis
    p "Thought you said everything was already packed in your other bag."
    show qi 56
    mc "Oh, this? Chang gave me a custom board game!"
    mc "Or... maybe it’s more like a card game? I honestly have no idea what it is exactly, but I say we crack it open and play together."
    show qi 49
    p "Ohh! That sounds so fun! Let's play tonight!"with dis
    p "It’s been forever since I played a board game! It'll be like... back in the pre-Eternum days!"
    show qi 50
    mc "Yes! I was hoping you'd say that."
    show qi 57
    n "Ah, and look who's finally here. We can finally hit the road!"
    show qi 58
    x "Huh...?" with dis
    x "Oh... hey, guys."
    x "What are you all doing here? I thought Dalia said you were at–"
    play soundlow whoosh3b
    scene qi59
    d "TA-DA!" with hpunch 
    show qi 60
    x ". . ."
    show qi 61
    x ". . ."
    show qi 62
    x "Ta-da, what...?"
    show qi 59
    d "You're coming to spend Christmas Eve with us!"
    show qi 63b
    p "We rented this cozy little lodge up in the mountains, just a couple hours away."
    p "Snow, dinner, and board games! The whole package!"
    p "And you're coming with us!"
    show qi 63
    x "*Taking a step back* Whoa, whoa, whoa, I don't... I... w-what?" with dis
    x "I-I mean, wow, thanks, but you guys don’t need to... like, seriously. I’m good."
    x "But I appreciate the invite. Truly."
    show qi 57
    n "That wasn't a question, Alex."
    n "Unless you already have plans, you’re coming with us."
    n "It might not be Bardot-level glitz and glam, but I can guarantee a nice dinner with our family."
    show qi 63
    x "No, no, seriously, I haven’t even had an actual Christmas dinner since I was, like, five."
    x "I'm used to spending Christmas in my room, listening to music."
    x "So... yeah, really, don’t worry about me. Save your money."
    show qi 57
    n "Please. I got this Airbnb with a coupon, it barely cost anything."
    n "And whether you come or not, it’s already paid for."
    show qi 63
    x "I... I mean, I don’t even have a change of clothes."
    x "Really, I appreciate it so much, but I don't want to be a bother."
    show qi 57
    n "We were already planning to swing by your place so you could grab your stuff."
    n "We’ll wait in the car."
    show qi 63
    x "Uhh..."
    x "That’s... generous. But no, really, I can’t accept."
    show qi 57
    n "Yes, you can. And you will."
    n "Come on now, get in the car."
    show qi 63
    x "I really can't, I'm sorry."
    show qi 57
    n "Alex... don't make me force you."
    show qi 63
    x "Nope! Sorry!"
    x "I have some chicken in the fridge that will spoil if I don't eat it."
    x "So..."
    show qi 57
    n "Come on..."
    show qi 63
    x "Sorry! But have a good trip!"
    x "And Merry Christmas!"
    show qi 57
    n "Alex..."
    show qi 63
    x "Seriously, I don't need–"
    play sound jumpscare3
    play music depression
    play soundloop risinglong volume 0.6
    show qi 64
    pause .4
    play sound2 fall
    scene qi65
    show qi66d
    show qi65e
    show qi66c
    show qi65d
    show qi66b
    show qi65c
    show qi66
    show qi65b
    n "I'm starting to think you don’t appreciate our kindness, Alexandra."with vpunchsubtleslow
    hide qi65b
    x "W-What? No! I-I do, I really do!"
    x "I... just don't want you to feel forced to invite me just because..."
    hide qi66
    n "We invite you because we love you, Alex."
    n "Not because we pity you. Not because we feel bad."
    n "It's because you're family now."
    n "Don't you understand?"
    hide qi65c
    x "I-I mean... of course! I-I understand that!"
    hide qi66b
    n "Good."
    play sound impact3
    n "{sc=3}{size=45}Now get in the car and accept our love."
    hide qi65d
    x "U-Uh..."
    x "Y-Yeah! Okay! Y-Yes, ma'am!"
    x "T-Thank you so much!"
    hide qi66c
    n "Don't even mention it."
    hide qi65e
    x "I-I will... I will go sit in the back."
    hide qi66d
    n "Good girl."
    play soundloop town_ambience volume 0.4
    play music happy18
    play sound pop
    scene qi 67
    n "Alright, let's go!"
    n "You might want to use the toilet while you're grabbing your stuff, we don't plan on stopping before we get there."
    show qi 68
    x "I-I will!"
    x "Thank you so much for this, Nancy, I..."
    show qi 67
    n "Come on, don't be silly."
    n "I remember how hard I had to fight to live on my own when I was younger."
    n "I admire you a lot, Alex."
    show qi 68
    x ". . ."
    x "...Thank you, Nancy."
    x "This... this means a lot to me."
    show qi 67
    n "Now, come on!"
    n "Everyone on board!"
    if penelopepath and daliapath:
        show qi 69
        p "Ahh... I see you're wearing the outfit I got for us, Dal." with dis14
        show qi 70
        d "Yeah, of course!"
        d "I’ll admit, the jackets are warmer than I thought they’d be."
        d "*Giggles* Although... you might wanna watch how much shoulder you're flashing, sis. Hate for you to come down with a cold!"
        show qi 69b
        p "Ohh—oopsie!"
        p "Thank you, sis, I didn't even realize."
        show qi 70
        d "Yeah... I bet it's hard to keep those massive boobs of yours at bay, huh??"
        play sound clothes4
        show qi 63b
        p "*Pulling her jacket up* You bet!" with dis12
        p "Almost as hard as dealing with this hair every morning!"
        p "Speaking of, you did your hair too, right?!"
        show qi 70
        d "I did! How sweet of you to notice!"
        show qi 63b
        p "Is that my blue hair band you're using?"
        show qi 70
        d "Oh! Is it? I'm sorry, I didn’t realize you had exclusive ownership over the hair ties at home, haha!"
        d "Especially when I’ve always been the one wearing braids, but... oh well!"
        show qi 63b
        p "*Giggles* Yeah, no, it's fine, no worries! You can borrow it!"
        p "Although... *giggles* for the record, you're not the only one wearing braids or ponytails, you know?"
        show qi 70
        d "*Giggles* Right, right!"
        d "Except... well, I've literally been the one rocking braids since middle school. *giggles louder* But... yeah, sure!"
        show qi 63b
        p "Mmm, yeah, I remember that! Same hairstyle every day, bangs covering half your face like you were hiding something, haha!"
        show qi 70
        d "*Giggles* Yep, that was me!"
        d "But... I don't know, I like changing it up now. Trying new things, you know?"
        d "*Giggles* I hope it's not forbidden!"
        show qi 63b
        p "*Giggles* Not at all! It's great to change styles!"
        p "Following in big sis' footsteps. That’s cute!"
        p "I can even give you some tips, if you want."
        p "Maybe... give conditioner a try next time? Kinda helps with the whole “electrocuted” vibe, you know?"
        show qi 71
        d "*Mocking tone* {i}Meybi giv cindishuner a trai nixt taim?"
        d "Yeah, thanks for the beauty advice, sis."
        d "I'll be sure to remember it if people ever stop caring about what I say too."
        show qi 72
        p "*Mocking tone* {i}Ah’ll bi shur tu rimmimbur et if peepl evur stap cairing aboot whit ah sai tuu."
        p "Did you come up with that comeback on your own? Or did you ask for advice on r/clevercomebacks again?"
        show qi 73
        d "Agh, shut the hell up already!"with dis12
        show qi 74
        p "Yeah, I'm gonna get in the car before I start barfing."
        show qi 73
        d "That's my seat!"
        show qi 74
        p "Um... since when?"
        show qi 73
        d "Since always??"
        show qi 75
        p "Move your fat ass out of the way!" with dis
        d "Shut up and move yours!"
        p "You b..."
        play sound cardoorslam
        play sound2 ["<silence 0.3>", cardoorslam]
        show qi75
        bla "Dalia and Penny hop into the car, slamming the door behind them." with hpunch
        mc ". . ."
        if harempath:
            scene qi 76
            mc "Um..." with dis12
            mc "Is it just me, or there's been some Cold War-level tension between Dalia and Penny lately...?"
            mc "They’ve been kind of ghosting each other all week, and when they do talk, it’s like watching a tennis match of passive-aggressiveness."
            show qi 77
            n "Uh... yeah, I wouldn't stress too much about it."
            n "They've done this before."
            show qi 78
            n "We did this big road trip across Canada when they were 12 and 15, and they spent the entire first two days fighting over who got the front seat."
            n "However, eventually they both felt bad about leaving the other out, so they came up with this super fair, overly complicated rotation system."
            n "So... yeah, just let the chaos unfold naturally."
            show qi 79
            mc "What do you mean?"
            show qi 78
            n "Just don't try to do or say anything. Smile, act like usual, and pretend you don't notice the emotional warfare between them."
            n "Trust me, I've been their mom for way too many years."
            n "This is... their natural cycle."
            show qi 79
            mc "But what..."
            mc "*Whispering* I mean, are we talking about..."
            mc "*Whispering* You know, do they know the whole..."
            show qi 77b
            n "Trust me. Trust the process. Don't say anything unless directly asked."
            n "Or unless... I give you a hint to do so."
            show qi 76
            mc "Right. U-Understood."
            show qi 78
            n "Alright, then!"
            n "Time to hit the road!"
    play sound cardoor
    play sound2 ["<silence 0.8>", cardoor]
    scene qi 80
    bla "You load the last bag in the car and slide into the passenger seat." with dis2
    n "Alright, who's gonna be brave enough to play their music first?!"
    play sound3 caraway2
    play sound4 caraway
    scene qi 81 with dis3
    stop sound4 fadeout 8
    pause
    stop music fadeout 7
    stop soundloop fadeout 7
    scene black with dis33
    show screen afewhourslater with dis27
    pause
    hide screen afewhourslater
    $ renpy.music.set_volume(0.1, channel='music')
    $ renpy.music.set_volume(1.0, delay=10.0, channel='music')
    play sound6 ["<silence 5.8>", whoosh9]
    play music xmas1
    scene pennyarrivesnow 
    with dis3
    pause 5
    psc "*Hyperventilating* . . .{w=2.7}{nw}" with dis
    scene qp 1
    p "Whoaaaaaaa!" with dis
    p "Look at this place!" with hpunch 
    p "Snow everywhere... tall spruces... and a cozy wooden house!"
    p "It's like something out of a Christmas movie! This is perfect!" with hpunch 
    play sound2 snow3
    scene qp 2 
    mc "*Chuckles* Damn, I didn't know you were this into Christmas, Penny." with dis17
    mc "You look like a kid at Disneyland."
    show qp 3
    p "Are you kidding me?!" with dis
    p "Christmas is the BEST holiday of the entire year! By far!"
    p "I understood why we weren't doing gifts this year, with everything going on, but I was kinda worried we'd skip Christmas entirely."
    p "This is SO perfect."
    show qp 4
    mc "*Chuckles* Understandable."
    mc "Honestly, I’d probably feel the same if I hadn’t grown up with my dad."
    mc "Christmas never felt special to me."
    if penelopepath:
        show qp 3
        p "Tsk, tsk, that's totally unacceptable!"
        p "I'll make sure all your Christmases feel special from now on..."
        show qp 4
        mc "Looking forward to it..."
    play sound cardoor
    play sound2 ["<silence 0.6>", cardoor]
    scene qp 5
    x "*Yawns* Aaaghh..." with dis12
    x "*Yawns* G-Gggooaawhh..."
    show qp 6
    x "Ugh, g-god, sorry." with dis
    x "I passed out for like half the ride. This car is way too comfy."
    show qp 8
    n "Don’t worry about it." with dis
    n "Dalia and Penny knocked out too after lunch."
    show qp 7
    x "Still, I feel kinda bad you had to drive the whole way, Nancy..."with dis08
    x "Let me help you with the luggage, at least."
    x "Should I..."
    x "Like... I mean, is this all just for one night...?"
    show qp 8
    n "One of those bags is refrigerated, full of stuff for dinner tonight."with dis08 
    n "And I brought a few kitchen tools to cook, too. Can’t count on rental homes having the good stuff."
    show qp 9
    n "And the other... well, you might wanna ask Penelope." with dis08
    show qp 10
    p "A foldable Christmas tree, {i}obviously." with dis 
    p "Just because we’re too busy this season to do our usual thing, doesn’t mean we can’t have a tree!"
    p "It's the most important part of Christmas!"
    show qp 11
    n "Really...?"
    n "I always thought the most important part was, you know, spending time with people you love..."
    n "But... what do I know..."
    p "*Huffing* Hmph."
    show qp 10
    p "Okay, okay, fine, the tree is the {i}second{/i} most important thing."
    play sound snow4
    show qp 12
    d "*Gasps* OH. MY. GOD!" with dis15
    d "Guys, look at the pool! It's huge!"
    d "And it has views of the forest! This place is insane!"
    play sound snow3
    scene qp 13
    x "Whoa..." with dis17
    x "Okay, now I get why you told me to pack a bikini too."
    x "Is it heated?"
    play sound stairswood2
    play sound2 clothes6
    play soundlow chair2
    scene qp 14
    d "*Taking off her boots* The host said it’d be warm by the time we got here, but..." with dis17
    d "There's only one way to know for sure!"
    play sound water volume 0.55
    show qp 15
    d ". . ." with dis17
    play sound2 water4b
    scene qp 16
    dbt "Mmmmmmhh..." with dis17
    show qp 17
    dbt "It's... sooo warm..."
    dbt "It's like we have our own private onsen..."
    scene qp 16
    mc "Nice!"
    play sound stairswood2
    play sound2 paper3
    scene qp 18
    n "Ah, look, the host left us a note!" with dis15
    show qp 19
    mc "We should really thank him. Even without the coupon, this place looks way too good for the price."
    show qp 18
    n "Totally! Let's see what he wrote..."
    n "*Starts reading* {i}Dear Ms. Carter, thank you for booking my humble property for this year’s Christmas Eve."
    n "{i}You’ll find the key hidden beneath the doormat. The temperature controls are located inside the closet behind the main door."
    show qp 19
    d "*Grabbing the key* Got it!"
    show qp 18
    n "{i}I am overjoyed that you’ve chosen to celebrate the sacred night of Yule beneath my roof."
    n "{i}I, too, once spent over a decade of Christmases here back when I still had a name, before..."
    show qp 20
    n "{i}...fleeing the ultracapitalist mind-control webs of Ulysses and its puppet government." with dis
    n "{i}Rest assured: since then, my home is 100%% government-proof."
    n "{i}There is zero Wi-Fi, zero cellular data, and absolutely no radio frequencies within a 40-yard perimeter."
    n "{i}All rooms are lined with military-grade soundproofing and painted with anti-surveillance reflective compound."
    n "{i}Should the agents of Ulysses track you down, you’ll find loaded firearms and sealed gas masks in the utility closet. Use them. They will come in through the chimney."
    show qp 21
    mc "...o-okay, that went off the rails real fast."
    p "So that’s why I have no data here..."
    show qp 20
    n "Yeah, the owner seems to be a little... paranoid."
    n "Although... credit where credit's due, after everything we've discovered lately... these anti-Ulysses nutjobs might not be so crazy after all."
    play sound paper3
    scene qp 22
    n "But anyway, enough about that. It's time to get situated!" with dis12
    show qp 23
    mc "Yes!"
    show qp 24
    n "And remember!" with dis06
    n "Today could be our last normal weekend for a while, so let's make it count!"
    n "Once we get the intel at Ulysses HQ on Wednesday and maybe find another Gem at Meiyo... who knows how fast things will get out of control."
    n "So I'm laying down the law now — no Eternum today."
    n "And yes, that especially goes for you, mister."
    show qp 25
    mc "What?! Why just me??"
    show qp 24
    n "Because you’re the only one here who can hop in and out of Eternum without the neural implant like it’s his personal backyard."
    n "So no sneaking in!"
    show qp 25
    mc "...okay, that's fair."
    mc "I won't. I promise."
    show qp 22
    n "Excellent then!"with dis
    n "Now, task distribution time!"
    show qp 26
    d "I call dibs on decorating the tree!"
    show qp 27
    p "Um... I'm sorry?"
    p "I'm the one who should decorate the tree."
    p "The tree literally wouldn’t even be here if it wasn't for me."
    show qp 28
    d "...Yeah, but I’ve decorated the tree every single year since I was, like, two?"
    show qp 27
    p "...Only because past Christmases were normal and I had time to decorate the entire house?"
    p "I'm the one who loves Christmas. And the tree is the only thing I have this year."
    p "You just want to decorate it to steal that from me."
    show qp 28
    d "I thought taking things from others was more your specialty, sis."
    show qp 27
    p "Excuse me...?"
    show qp 30
    n "Um... ahem, actually, I already assigned the tasks."with dis
    n "Alex will decorate the tree."
    n "Dalia will help me in the kitchen and bake some of her cookies, and Penny will prepare the beds and get the fireplace going."
    show qp 22
    n "And [mc] is on lumberjack duty!" with dis08
    n "Chop some logs and bring 'em in! We'll need that fire roaring tonight."
    show qp 23
    mc "Sounds good to me!"
    show qp 31
    d "Cooking! I like that."
    p "Works for me, mom."
    show qp 32
    x "All clear, Nancy."
    scene qp 22
    n "Great! Then let's get to it!"
    n "Dinner's at six!"
    show qp 24
    n "And snack responsibly." with dis08
    n "I want you all starving by the time the roast hits the table."
    show qp 25
    mc "I won't eat anything until then!"
    show qp 22
    n "Good!" with dis06
    play sound keys
    scene qp 33 with dis2
    play sound2 dooropenclose
    bla "The girls grab their bags and scatter into the house." with dis15
    mct "Alright..."
    mct "Time to play lumberjack, I guess. Gotta do my part!"
    mct "Although... I better grab my jacket first."
    mc "*Shivers* (I don't wanna freeze my butt off out there.)"
    stop music fadeout 8
    scene black with dis25
    $ renpy.music.set_volume(0.3, channel='soundloop3')
    play soundloop3 forest fadein 4 
    show screen sometimelater with dis2
    pause
    play music2 xmas2 fadein 7
    hide screen sometimelater
    scene qp 34
    with dis25
    pause
    $ scorelogs = 6
    play sound snow4
    scene qp 38 with dis17
    pause
label logchopchop:
    $ scorelogs += 1
    play sound5 snow volume 0.7
    play sound3 ["<silence 0.2>", logput]
    scene qp 35 with dis12
    pause
    play sound2 leathershort volume 0.2
    scene qp 36 
    call screen logchopbutton with dis12
label logchop2:
    play sound logchop
    play sound4 debris3 volume 0.7
    scene qp 37 with vpunch
    pause
    play sound6 ["<silence 0.2>", logfall] volume 0.8
    play sound8 snow2 volume 0.25
    play sound7 snow volume 0.4
    scene qp 38b
    if scorelogs < 8:
        mct "Alright..." with dis14
        mct "That makes seven logs down."
        mct "About three or four more should be enough to keep the fire alive all night."
    elif scorelogs == 10:
        mct "Man, I don't miss." with dis14
        mct "I've split every single log clean in half with a single swing."
        mct "It's not just my reflexes or technique... I've really gotten stronger too."
        mct "Like, {i}way{/i} stronger."
    elif scorelogs == 11:
        mc "Aaaand... eleven."with dis14
    elif scorelogs == 14:
        mct "Dude, this shit's low-key addicting."with dis14
        mct "They should offer this as therapy."
    elif scorelogs == 17:
        mct "Okay..."with dis14
        mct "There’s more chopped wood here than I can physically carry, to be honest."
        mct "Maybe I should stop."
    elif scorelogs == 18:
        mct "Or maybe I can chop just a few more..."with dis14
    elif scorelogs == 19:
        mct "I can stop anytime I want. After this next one."with dis14
    elif scorelogs == 21:
        mc "Blackjack."with dis14
    elif scorelogs == 25:
        mct "Why am I still going...?"with dis14
    elif scorelogs == 69:
        mc "[number_to_words(scorelogs).capitalize()]."with dis14
        mc "Nice."
    elif scorelogs == 100:
        mct "A hundred."with dis14
        mc ". . ."
        mct "You did it, [mc]."
        mct "You've broken the matrix."
        mct "You've unlocked the secret, true ending of the game — {b}the Idriel sex scene."
        mct "You are now..."
        mc "{sc=2}{size=49}ETERNUM."
        mc ". . ."
        mct "Okay, I'm officially starting to lose my mind."
        mct "I really have to stop before I go completely bananas."
        jump afterlogchop
    else:
        mc "[number_to_words(scorelogs).capitalize()]..." with dis14
        if scorelogs == 29:
            mc ". . ."
            mct "I wonder if I can make it to a hundred..."
            mc "*Chuckles* (Nah... I'm not that crazy, luckily.)"
            mct "Right...?"
    menu:
        with dis
        "Chop one more":
            if scorelogs == 11:
                mc ". . ." with dis
                mct "Maybe I should chop a few more." 
                mct "Better safe than sorry."
            jump logchopchop
        "Stop":
            if scorelogs < 11:
                if scorelogs == 7:
                    mct "But... ugh, I'm getting tired." with dis 
                else:
                    mct "Ugh, I'm getting tired."with dis
                mct "We'll go with this. It should be enough."
            elif scorelogs < 17:
                mct "Yep, that should be enough." with dis
                mct "A job well done."
            else:
                mct "Yep, that should be enough." with dis
                mct "{i}Way{/i} more than enough, to be honest."
label afterlogchop:
    play sound clothes3
    scene qp 39
    mct "Alright... time to head back." with dis15
    mct "Maybe I can go see if Nancy and Dalia need a hand in the kitchen."
    play sound3 vibration
    play sound2 vibration
    scene qp 40
    bla "{sc=1}Your phone buzzes.{/sc}" with dis08
    mc "Hmm?"
    play sound4 clothes3
    scene qp 41
    mct "A message...?" with dis12
    if anniepath:
        scene qp 42
        mct "A message from Annie!"
        mct "I guess I stepped past the 40-yard perimeter that blocks the signal."
        call chat(annie_chat3) from _call_chat_24
        mct "God, she's adorable." with dis
        mct "I'm glad I could reply to her now."
    else:
        mct "Oh..."
        mc "*Reading the spam email* {i}(Follow us on all social media for a chance to win one of five free neural implants we're giving away!)"
        mct "Yeah... no, thanks."
        mc "Hmm..."
        mct "Welp, that’s it. Still good I checked, I guess."
    if axelhelp:
        mct "I don't know if I'll have signal again until tomo–"
        stop music2 fadeout 8
        play soundloop vibration
        play soundloop2 vibration
        scene qp 41
        bla "{sc=1}You receive a call from an unknown number." with dis08
        mct "Unknown number...?"
        mct "Hmm, it's probably just some spam."
        mct "Although..."
        mct "What if it's not? I might not be able to answer until tomorrow."
        menu:
            with dis
            "[gr]Answer":
                pass
            "Hang up":
                $ axelhelp = False
        play sound beep2b
        stop soundloop
        stop soundloop2
        if not axelhelp:
            bla "You reject the call."with dis
            mct "Yeah, I don't have time now."
            mct "If it's important, they'll call again."
            jump pennytime09
        scene qp 44
        mc "Hello?"with dis12
        play music pendulum fadein 6
        bla ". . ."
        aaa "God, you finally picked up."
        mc "Sorry, I didn't–"
        mc "Wait... who is this?"
        mct "That voice..."
        scene qp 46 with dis14
        mc "...Axel?" with dis12
        show qp 45
        ax "Are you with Alexandra?"
        ax "Her phone isn't ringing either."
        show qp 46
        mc "Yeah, we're together. Up in the mountains. There's no signal up here."
        mc "Why the hell are you calling me now?"
        mc "We haven't heard from you in weeks."
        show qp 45
        ax ". . ."
        ax "He killed him."
        ax "My father killed Benjamin."
        show qp 46
        mc "...What?"
        mc "No, that's not... A Praetorian did. I saw it."
        show qp 45
        ax "He controls them. Not all of them, but... enough."
        show qp 46
        mc "What...?"
        mc "How did you... Are you sure?"
        mc "I mean... that can't be."
        mc "The Founder controls the Praetorians, not William."
        show qp 45
        ax "I can tell you more. I know what he's planning."
        ax "But not now. Not over the phone."
        ax "Let's meet. Next Wednesday."
        show qp 46
        mc "Uhh... we already have something on Wednesday."
        mc "How about... Thursday evening?"
        show qp 45
        ax ". . ."
        ax "...Fine. Thursday at 9 PM. The park by the station."
        show qp 46
        mc "Alright. I'll try to be there."
        show qp 45
        ax "{i}Be there."
        ax "And whatever you do, don't approach my father. Under any circumstance."
        ax "Stay out of this until we talk. He's dangerous."
        show qp 46
        mc "Uhh... okay, sure."
        play sound beep2b
        play sound2 clothes3
        scene qp 44
        bla "He hangs up." with dis14
        mc "Hmph."
        mct "This guy sounds shady as hell."
        mct "And I still don't trust him. For all I know, he could be feeding us bullshit, working for his daddy."
        mct "But... I guess it doesn’t hurt to hear him out."
        mct "Still, no way I could tell him we’re actually planning to dig through his dad’s office this Wednesday."
        mct "Not without running it by the others first, at least. Especially Alex."
        stop music fadeout 6
    else:
        mct "I don't really know if I'll have a signal again until tomorrow."
label pennytime09:
    play sound snow4
    play sound2 clothes3
    scene qp 38b
    mc "*Putting the phone back in your pocket* (Anyway...)" with dis2
    mct "I should grab the logs and bring them inside."
    mct "I really don’t wanna be the reason the fire goes out. Dalia will kill me if her marshmallows don't make it."
    stop music2 fadeout 6
    play sound snow3 fadein 3
    scene qp 47 with dis3
    bla "You carry as many logs as you can and haul them back to the house, where you drop them by the door."with dis17
    mct "Oh man, I'm getting hungry..."
    mct "Hope dinner doesn't take too long now."
    stop soundloop3 fadeout 3
    play music2 xmas1 fadein 6
    play sound2 dooropenclose
    scene qp 48 
    bla "As you step inside, a wave of warmth radiates from the fireplace towards you." with dis2
    mc "Ahhhh, now {i}this{/i} is cozy!"
    mc "I'm finally starting to feel the Christmas magic!"
    scene qp 50
    p "Ah, look who's back!" with dis12
    p "I was starting to think you'd leave the whole mountain bare."
    show qp 49
    mc "It took a while to find decent wood."
    mc "It's important to pick the dry stuff. If it's been sitting on the ground too long, it's useless."
    show qp 50
    p "Oh boy, I see I'm dealing with an expert."
    show qp 49
    mc "*Chuckle* You're damn right!"
    if axelhelp:
        mc "And actually, I would've come back sooner, but someone called me."
        show qp 50b
        p "Called you? On the phone?"
        show qp 49b
        mc "Yeah! You can actually get a signal if you walk far enough."
        mc "You're never gonna guess who it was."
        mc "Axel Bardot."
        show qp 50b
        p "Alex's brother? For real?"
        p "We were just talking about him with her earlier!"
        p "She said she hasn’t heard from him since your last run-in."
        show qp 49b
        mc "He wants to meet. Thursday, 9 PM."
        mc "But I haven't decided if I should go yet. I wanna mention it to Alex first."
        show qp 50b
        p "Yeah... yeah, that's a good idea."
        show qp 49b
        mc "I don't really know what he wants, but... can't hurt to hear him out."
        mc "But in any case, that can wait!"
        mc "Tonight's a detox night! No more Eternum talk!"
        show qp 50
        p "*Chuckles* Hell yeah!"
    scene qp 51
    mc "I've gotta admit, you were totally right — a Christmas tree completely transforms the vibe." with dis
    mc "And damn, that's a nice fire you got there!"
    p "Thanks!"
    play sound chairmove
    play sound2 chair2
    scene qp 52
    mc "*Sitting down* Did you use Duraflame or something?" with dis12
    scene qp 53
    p "Nope. Just some dry timber and a couple of steel knives."
    show qp 52
    mc "Steel knives?! You didn't even use a lighter?!"
    show qp 54
    p "Please, of course not. I'm a survivor!" with dis08
    p "Five-time Best Girl Scout winner, thank you very much."
    show qp 52
    mc "*Chuckles* You were a Girl Scout?" with dis08
    show qp 53
    p "Yeah! You didn't know?"
    p "Need a fire built, a knot tied, or someone patched up? I’m your girl."
    show qp 52
    mc "You've been hiding so many secrets from me, missy."
    mc "I don't remember you being one when I still lived in Kredon."
    show qp 53
    p "Yeah, I joined shortly after you left."
    play sound pop volume 0.7
    show qp53b
    p "Dalia was always doing some insane stunt and getting hurt, so I got super into first aid." with dissolve
    p "And after I started noticing the way she inhales food, I figured I’d better learn how to save her before she chokes."
    mc "*Chuckles* That's so cute. "
    scene qp 52
    mc "You've always cared more about others than yourself." with dis 
    mc "Have you ever had to Heimlich her?"
    show qp 53
    p "Surprisingly, no, not yet."
    p "That girl's throat can take a beating, I swear."
    scene qp 52
    if daliapath:
        mc "Hah!"
        mct "You can say that again..."
    else:
        mc "*Chuckles* I can imagine."
    play sound rubbody volume 0.4
    scene qp 55
    p "But anyway, I’m not really feeling it today, so I think I’m gonna just ditch this and go help out in the kitchen." with dis12
    scene qp 56
    mc "What were you doing? Do you have internet access?"
    scene qp 55
    p "Nah, I don't. I was just brainstorming ideas for my journalism capstone project."
    p "But... I'm not feeling inspired. Struggling with my thesis statement."
    show qp 56
    mc "Do you want a second brain on it? Maybe I can help."
    mc "What's the topic?"
    show qp 55
    p "Well, that's what I'm trying to decide."
    p "I can pick any subject I want, but I've gotta research, dig around, do interviews... the whole thing."
    p "It counts for 40%% of my final grade, so it's kinda a big deal, but..."
    p "*Sighs* My brain's not cooperating today."
    show qp 56
    mc "Hmmm..."
    mc "How about..."
    menu:
        with dis 
        "Eternum":
            mc "Exposing everything that's behind Eternum?"with dis
            mc "At this point we’ve got more than enough evidence, and tons of people you could interview."
            mc "Who knows, maybe it could even go viral!"
            mc "It’d be satisfying to finally see Ulysses face some consequences for once."
            p "Hmph..."
            show qp 57
            p "Yeah... I actually thought about that too."
            show qp 55
            p "And... it'd make for a crazy story, but..."
            p "I don't know, I feel like we should keep our heads down right now."
            p "The whole Gems of Doom mission is way more important than some college project, and I wouldn't want to bring any unwanted attention because of it."
            show qp 56
            mc "Hmm, yeah, that's a fair point."
        "Raul and Noah":
            mc "Exposing Raul and Noah?"with dis
            mc "I think at this point it's not a secret that they're up to something shady."
            mc "Maybe you could interview Mr. Keating, or... some old students. I've heard they've been at Kredon's school for over 15 years."
            p "Hmph..."
            show qp 55
            p "I don't know..."
            p "It's pretty obvious they're involved in some sketchy stuff, yeah, but..."
            p "They also helped us during the Garrington heist."
            p "I wouldn't feel right betraying them like this."
            show qp 56
            mc "Hmm, yeah, that's true..."
        "[gr]Mr. Valentino" if penelopepath:
            $ valentinoproject = True
            mc "Exposing that Nico Valentino creep?"with dis
            mc "You could talk to some of the other girls he tried to manipulate. Maybe even Aspen, if she’s up for it."
            mc "It’d be kind of amazing to watch his whole modeling empire in Kredon crash and burn, honestly. The guy has it coming."
            p "Hmph."
    play sound rubbody volume 0.4
    scene qp 53
    if valentinoproject:
        if penelopepath:
            play sound2 beat
            show screen heartbeat
            $ penelope_points += 1
        p "Yeah... that's actually a great idea. I like it." with dis12
        p "It'd feel really good to see him bite the dust."
        show qp 52
        mc "Right?"
        show qp 53
        p "Good idea, [mc]! Thank you."
    else:
        p "But don't worry, I'll come up with something."with dis12
        p "Thank you for your help anyway, [mc]."
    show qp 52
    mc "Don't mention it. Always happy to help!"
    mc "If you need me when you're working on it, just let me know."
    play sound dooropen4
    scene qp 58
    n "Ah, hey guys!" with dis15
    n "Are you both done?"
    scene qp 59
    p "Yes, mom!"
    mc "Yup! Got a big pile of logs right outside!"
    mc "Do you need help in there?"
    show qp 58
    n "Nah, no worries, I already have Dalia and Alex helping."
    n "Dinner should be ready in forty mi–"
    show qp 59b
    d "So... how does it taste?" with dis
    x "Mmmh, not bad."
    play soundlow fallkitchen volume 0.6
    d "NOT BAD?!" with hpunch 
    d "*Groans* AAAggghh, we need to throw this shit away and start again."
    x "W-What? Why?"
    d "What do you mean, {i}why{/i}?"
    $ mcshort = mc[:2]
    d "How am I supposed to give [mcshort]...uh–e-everyone some... {i}“not bad”{/i} cookies?!"
    scene qp 58
    n "Uhh... yeahh, maybe it's gonna be more like... fifty minutes." with dis
    scene qp 59
    mc "No problem!"
    scene qp 60
    n "Until then, relax by the fire, sing a song, or..." with dis12
    n "Y’know, if you’ve got any secret, private conversations to have, now’s the time."
    if penelopepath:
        n "These walls are soundproof. Just saying."
    play sound footsteps4
    scene qp 61 with dis17
    mc "Um... sure." with dis12
    if not penelopepath:
        mct "Well..."
        mct "Guess it's time to put all that wood to good use." 
        mct "A man's duty is to keep the fire alive."
        mct "Time to show them what you’re really capable of, [mc]..." 
        jump dinnerchristmas    
    if harempath:   
        mct "I suppose that was the hint she mentioned earlier..."
        scene qp 62
        mct "Is it really the right time to tell Penny about... the whole... uhh..." with dis
        mct "I don't even know what to call it."
        mct "...whatever this... multi-love situation is called."
        mct "Why is life so complicated?"
    else:
        scene qp 62
        mct "What exactly did she mean by that...?" with dis
        mct "Does Nancy know about us...?"
        p ". . ."
        mct "Should I try to make a move...?"
        mct "Should I... ask Penny about it?"
        mct "Or is this not a good moment?"
    p ". . ."
    mc "*Taking a deep breath* . . ."
    mct "Alright, here we go. Let's do it."
    mc "*Clears throat* Hey, Penny–"
    play sound chairmove
    play sound2 chair2
    scene qp 63
    p "*Standing up* Hey, can you come upstairs for a sec?" with dis12
    scene qp 64
    mc "Uh... me?"
    mc "Right now?"
    p "Mm-hm."
    show qp 63
    p "I need help... choosing between two bikini tops."
    p "I wanna hear your opinion on them."
    show qp 64
    mc "Ohh... I see..."
    show qp 63
    p "Don't worry, it'll only take a minute."
    p "Pretty please?"
    show qp 64
    mc "Um..."
    menu:
        with dis
        "[gr]Accept and go with her":
            $ acceptandgowithher = True
            mc "Sure. That sounds good."with dis
            show qp 63
            p "Awesome!"
            p "I'll go ahead then."
            p "First door on the left after the stairs. Join me after you're done bringing the logs inside."
            show qp 64
            mc "You got it!"
            scene qp 67 with dis17
            mct "Well, I suppose that conversation can wait..."with dis12
        "Stay here":
            mc "Actually... I'd rather stay here."with dis
            mc "But go ahead to try them on, don't worry."
            mc "I'll be here."
            scene qp 65
            p ". . ." with dis
            scene qp 66
            p "...Really?"
            show qp 65
            mc "Yeah, I still gotta bring all those logs inside."
            show qp 66
            p "Then do it and come upstairs."
            p "I need to ask you something important."
            p "I'll only steal one minute of your precious time, don't worry."
            show qp 65
            mc "Uh..."
            p ". . ."
            mc "O-Of course, yes. I can do that."
            p "Hmph."
            scene qp 67 with dis17
            mct "I should've gone with the bikinis..."with dis12
            mct "I wonder what she wants to ask me?"
            mct "I better get those logs inside fast."
    scene qp 68 with dis25
    bla "You bring in the logs and stack them by the fire." with dis15
    play sound stairswood
    play sound2 stairswood2
    scene qp 69
    mct "Alright..." with dis15
    mct "First door on the left."
    stop music2 fadeout 6
    play sound dooropenclose
    scene qp 70 with dis2
    play music2b xmas4 fadein 6
    bla "You walk into the room and see Penelope sitting on the floor, fiddling with a little padlock." with dis12
    mc "Whoa, now {i}this{/i} is a bedroom!"
    play soundlow footsteps4
    scene qp 71
    mc "*Chuckles* You were quick, Penny. Snagged the best room in the whole place before anyone else, eh?" with dis17
    mc "Hmm? What are you doing down there?"
    play sound wood2 volume 0.33
    play sound2 clothes3
    scene qp 72
    p "Ah, [mc], finally!" with dis14
    show qp 73
    mc "Holy smokes..."
    mc "I see you're already trying on the bikin–"
    show qp 72
    p "Listen, can I ask you something now that we're alone?"
    p "It's... kinda important."
    show qp 73
    mc "Uh..."
    mc "Sure, of course."
    show qp 72
    p "Let's sit on the bed!"
    p "It'll be comfier."
    show qp 73
    mc "Sure!"
    play sound ["<silence 0.3>", couchlouder]
    play sound ["<silence 0.1>", chair1] volume 0.5
    scene qp 74
    bla "You both plop down onto the bed." with dis15
    mc "Holy Mary..."
    mc "I don't know about the other swimsuits you brought, but this bikini is doing things to me, Penny."
    show qp 78
    p "Oh, you really think so?" with dis 
    p "Is it not too small?"
    show qp79
    mc "Definitely not. Covers what it has to cover, and lets the rest do the talking."
    mc "Although... I doubt there’s a bikini on this planet that could look bad on you, honestly." 
    scene qp 78b
    p "*Chuckles* Well, that’s good to hear, because I kinda forgot to bring any other swimsuits. This one’s my only option."
    show qp 79
    mc "No complaints from me."
    mc "Want me to take a picture...? So you can see how great it looks?"
    show qp 78b
    p "To see how I look...?"
    p "Can't I just go check myself in the bathroom mirror?"
    show qp 76
    mc "Sure, you could, but the bathroom doesn’t have this lighting." with dis15
    mc "Have you seen these red neons? They’re like... made for you. They give the room a sultry vibe."
    show qp 77
    p "*Snorts* Sultry? More like a “welcome to my sex dungeon” vibe, I'd say."
    p "Although... yeah, I like them too, to be fair."
    show qp 75
    p "But seriously, I really did want to ask you something important." with dis12
    show qp 74
    mc "Of course! Ask away."
    show qp 80
    p "*Taking a deep breath* Okay..." with dis
    p "Do you... promise me you'll never lie to me?"
    show qp 81
    mc "What?"
    mc "Really? That's the question?"
    show qp 80
    p "Well, that's more like... the warm-up question."
    show qp 81
    mc "Penny, please, of course."
    mc "Why would I lie to you?"
    show qp 80
    p "Do you promise me?"
    show qp 81
    mc "I promise. I will tell you the truth, no matter what."
    mc "I swear on my life."
    show qp 75
    p "Really...?"with dis08
    show qp 74
    mc "Absolutely."
    show qp 75
    p "*Softly* I'm... I'm glad you said that."
    p "Alright then, here's my real question!"
    show qp 74
    mc "Shoot!"
    play sound clothes3
    scene qp 82
    p ". . ." with dis17
    play sound lightstage
    play sound2 impact3
    play soundloop beat3 fadein 4
    stop music2b
    scene qp 83
    p "Have you slept with anyone else since what happened between us at the studio?"
    show qp 84
    mc ". . ." with dis14
    p ". . ."
    scene qp 85
    mc ". . ." with dis14
    mc "U-Um..."
    mc "T-That's the question?"
    show qp 86
    p "Yes. That's the question."
    show qp 85
    mc "E-Erm..."
    menu:
        with dis
        "[gr]Yes":
            mc "I mean..."with dis
        "No\n[mt](only if on just her path)":
            mc "N-No. I haven't."with dis
            if not alexpoolvisit and not novapath and not anniepath and not daliapath and not loreleisex:
                p ". . ."
                scene qp 87
                p ". . ." with dis08
                show qp 85
                p "Hmm." with dis08
                jump polylovequestion
            jump pennyliepoly
    mc "I-I didn't know what we did implied... you know."
    show qp 86
    p "It didn't."
    p "I never requested it."
    p "That's why I'm asking."
    show qp 85
    mc ". . ."
    mc "A-Alright, then..."
    mc "Uh..."
    mc "...Yes. I-I might have."
    mc "But it's not what–"
    scene qp 86
    p "Did you fuck Dalia?"
    show qp 85
    mc "WHAT?!" with hpunch 
    p ". . ."
    mc "U-Um... o-okay, hold on, before anything else, just listen to me for a–"
    show qp 86
    p "Don't beat around the bush."
    p "It's a yes or no question."
    p "Answer it."
    show qp 85
    menu:
        with dis
        "[gr]Yes" if daliapath:
            mc ". . ."with dis
            mc "...Yes."
        "No":
            mc "Then no. I haven't."with dis
            if not daliapath:
                scene qp 87
                p ". . ." with dis08
                show qp 85
                p "Hmm." with dis08
                jump polylovequestion
            jump pennyliepoly
    p ". . ."
    show qp 86
    p "Do you {i}love{/i} Dalia?"
    show qp 85
    mc "What...?"
    mc "Christ, for fuck's sake, just let me expla–"
    show qp 86
    p "Yes... or no."
    p "Answer."
    p "Are you {i}in love{/i} with her?"
    show qp 85
    mc ". . ."
    menu:
        with dis
        "[gr]Yes":
            mc ". . ."with dis
            mc "...Yes."
        "No (True)":
            mc "No."with dis
            p ". . ."
            $ dalianotlove = True
            $ penelopepath = False
            $ penelopeu = False
            $ harempath = False
            scene qp 87
            p ". . ." with dis08
            show qp 86
            p "Really...?" with dis08
            show qp 85
            mc "I don't. I swear."
            mc "I only love y–"
            show qp 86
            p "Then why the fuck did you tell her you loved her?"
            show qp 85
            mc "Wha-"
            mc "Wait..."
            mc "How..."
            mc "How do you even know that...?"
            mc "D-Did she tell you...?!"
            p ". . ."
            jump pennyliepoly
        "No (Lie)":
            mc "No."with dis
            jump pennyliepoly
label polylovequestion:
    p ". . ."
    show qp 86
    p "Do you..."
    p "Do you love me, [mc]?"
    show qp 85
    mc "Love you...?"
    menu:
        with dis
        "[gr]Yes":
            if daliapath:
                mc "*Sighs* I know this is gonna sound like complete bullshit after what I just said, but..."with dis 
            else:
                mc "What kind of question is that?"with dis
            mc "I love you, Penny."
            mc "I'm madly in love with you. I'd die for you."
            if daliapath:
                mc "The same way I love Dalia."
                mc "Maybe that's not what you wanted to hear, but... I just can’t change it. I can’t help it."
            else:
                mc "I know it might sound like bullshit, but..."
            mc "But I fucking swear to you, Penelope — I love you."
            p ". . ."
            jump pennypasspoly
        "No":
            mc "I..."with dis 
            mc ". . ."
            p ". . ."
            mc ". . ."
            mc "I had to make a choice."
            mc "I'm... I'm so sorry, Penny."
            mc "B-But..."
            mc "I mean..."
            mc "We had fun, right...?"
            p ". . ."
            $ penelopepath = False
            $ penelopeu = False
            $ harempath = False
            $ notmachineline = True
            jump pennyliepoly
label pennyliepoly:
    if not penelopepath:
        stop soundloop fadeout 12
        play soundloop2 clock2 fadein 5
    else:
        play sound error3 volume 0.4
        show qp 87
        bla "{sc=2}A sudden alarm blares from under the bed." with hpunchsubtlelong
        mc "J-Jesus, what the hell was that?!"
        p ". . ."
        play sound clothes3
        play sound2 couchlouder
        stop soundloop fadeout 12
        play soundloop2 clock2 fadein 5
        scene qp 88 with dis15
        bla "Penny reaches under the bed." with dis12
        play sound7 swordmove
        p "That...?"
        p "Well, that was you..."
        play sound2 rubbody
        play sound5 couch
        show qp90 
        pause 1.2
        play sound chair1
        p "...proving your word is about as reliable as a stripper's “I really like you”." with dis
        scene qp 89
        if ppp7:
            mc "What the fuck is that thing...?"
            scene qp 90
            p "A friend from college lent it to me. One of those weird gadgets they make at the tech campus."
            p "This polygraph analyzes your voice and detects lies. Can you believe it?"
            show qp 89
            mc "What?!"
            mc "That's bullshit!"
            scene qp 90
            p "Oh, is it?"
        else:
            mc "What the–"
            mc "Oh no, I think I've seen that thing before..."
            scene qp 90
            p "Ohhh, then you already know what it does, right?"
            scene qp 89
            mc "If it’s the polygraph Akira built over at the tech campus, then... yeah, I know what it is."
            mc "But that thing is not reliable, like, at all!"
            scene qp 90
            p "Oh, is it not?"
        p "I think [mc] is a very, very honest man."
        play sound error3 volume 0.4
        show qp 99
        p ". . ." with hpunchsubtlelong
        scene qp 90
        p "I'm so happy [mc] proved I can trust him unconditionally." with dis08
        play sound error3 volume 0.4
        show qp 99
        p ". . ." with hpunchsubtlelong
        scene qp 90
        p "I’m {i}thrilled{/i} he lied to my face right after promising he wouldn’t, but that’s fine, I’ll just keep being his little fuck toy whenever he feels like it." with dis08
        play sound error3 volume 0.4
        show qp 99
        p ". . ." with hpunchsubtlelong
        show qp 96
        p "Oh, guess the machine says I won't! Oopsie!" with dis08
    play sound rubbody
    play sound2 clothes3
    play sound3 couchlouder
    show qp 91 with dis15
    if not penelopepath:
        p "I suppose we're done here." with dis15
        p "Thank you for your honesty."
        mc "Wait!"
        mc "Penny, I..."
    else:
        mc "P-Penny, I..." with dis15
    mc "I never wanted to..."
    p "Don't."
    p "You're a fucking idiot. Do me a favor and don't take me for one too."
    mc ". . ."
    if penelopepath:
        p "I can't believe I was willing to accept it all just because... I thought..."
        p "I thought you were different."
        p "But I was wrong."
        p "Or... maybe I... maybe I just made you into someone you're not."
    else:
        p "God, I can't believe I was this stupid."
        p "I'm pathetic."
    mc "Aaagh, just listen to me, please! Let's talk about it!" with hpunch
    if dalianotlove:
        mc "Okay, yeah, I lied to her! But–"
    elif penelopepath:
        mc "Okay, yeah, I lied! But–"
    p "No."
    p "I’m done. I’ve cried enough over this. And I’m not wasting another tear."
    p "Let's just... pretend nothing happened. Mom doesn't deserve the drama."
    if daliapath:
        p "And Dalia..."
        p ". . ."
        p "You better not play with her too, you moron."
    if not penelopepath:
        mc "Oh, come on, Penny! You didn't even let me explain myself!"
    else:
        mc "Oh, come on, Penny! All this over some stupid machine?!"
        p "*Huffing* You really don't get it, do you?"
    p "I'm going to help with dinner."
    p "Don't be late."
    play sound couch
    play sound3 wood2 volume 0.3
    scene qp92 with dis15
    play sound2 doorslam
    bla "Penny leaves the room, slamming the door behind her." with dis12 
    mct "...Shit."
    if not dalianotlove and daliapath and not notmachineline:
        mct "That fucking machine..."
    mc "*Sighs* (I blew it. No point chasing her now.)"
    mct "I'll give it some time to cool things off and then I'll apologize properly."
    mct "Or... at least I'll try."
    mc "*Sighs* (I guess I had it coming this time...)"
    mc "Fucking hell."
    $ pennymadpolygraph = True
    $ penelopepath = False
    $ penelopeu = False
    $ harempath = False
    jump dinnerchristmas
label pennypasspoly:
    scene qp 87
    p ". . ." with dis08
    scene qp 86
    p "Say it again." with dis08
    scene qp 85
    mc "I love you!"
    mc "I swear, Penny, I do!"
    p ". . ."
    scene qp 87
    p ". . ." with dis08
    play sound clothes3
    stop soundloop fadeout 12
    play music2 xmas4 fadein 6
    scene qp 93 with dis14
    play sound2 couchlouder
    play soundlow chair1
    scene qp93
    pause 0.01
    p "AAAaaaghh... jeez, no alarm... Thank god." with dis12
    p "I don’t think I’ve ever felt this anxious in my life."
    mc "*Sweating* Tell me about it..."
    p "I have no idea how I would’ve reacted if the machine had gone off."
    mc "Machine? What machine...?"
    play sound clothes3
    play sound2 couchlouder
    scene qp 88 with dis15
    bla "Penny reaches under the bed." with dis12
    play sound7 swordmove
    p "Well..."
    p "I had to be absolutely sure you were being honest with me, so..."
    play sound2 rubbody
    play sound5 couch
    show qp95
    pause 1.2
    play sound chair1
    p "...I got a little help from my friends at college!" with dis
    scene qp 94
    if ppp7 or not novapath:
        mc "*Chuckles* What?"
        mc "What the hell is that thing?"
        scene qp 95
        p "One of those weird gadgets they create at the tech campus — the DK Tron ZLF-9000!"
        p "It's a polygraph!"
        show qp 94
        mc "A polygraph?"
        p "Mm-hm."
        show qp 95
        p "It analyzes your voice and detects lies. Can you believe it?"
        show qp 98
        p "Oh, and... it also produces fog, I think."
        p "For... some reason I never really understood."
        show qp 94
        mc "What?!"
        mc "And does it really work?"
        scene qp 95
        p "See for yourself!"
        show qp 98
        p "Uhh..."
        p "I'm {i}not{/i} looking forward to taking a bath in the outdoor pool after dinner."
        play sound error3 volume 0.4
        show qp 99
        p ". . ." with hpunchsubtlelong
        scene qp 95
        p "See?" with dis08
        show qp 94
        mc "Hah! That's amazing!"
    else:
        mc "Wha–"
        mc "Wait..."
        mc "No way."
        mc "I've seen that thing before!"
        scene qp 96
        p "Huh? You have? Really?"
        scene qp 97
        mc "If it’s Akira's polygraph, then... yeah, I've seen it in action."
        mc "During the Halloween party, with Nova."
        show qp 96
        p "Really?"
        p "Hah! Small world!"
        p "So... you already know it can detect lies analyzing your voice, and..."
        show qp 98
        p "Produce fog, for some reason I never really understood."
        show qp 97
        mc "*Chuckles* Yeah, I do."
        mc "Has it been connected this whole time?"
        show qp 98
        p "I think so, yeah."
        p "Um..."
        p "[mc] looked at my boobs less than five times since he came in."
        play sound error3 volume 0.4
        show qp 99
        p ". . ." with hpunchsubtlelong
        scene qp 95
        p "Yep, seems to work just fine." with dis08
    play sound clothes3b
    play sound2 couchlouder
    scene qp 101
    p "*Lying down* Aghh... I feel like I just got a weight off my chest that I've been dragging all week." with dis15
    p "It feels... good."
    if daliapath:
        show qp 102
        mc "So... you already knew?"
        mc "Does Dalia know...?"
        show qp 101
        p "She does. Things were kinda brought to light shortly after you disappeared."
        show qp 102
        mc "That explains why you two have been acting so weird lately..."
        mc "I wanted to tell you, but–"
        show qp 101
        p "Mom told you not to."
        p "And... honestly? I think she was right. If your feelings are real, it's probably better to let it play out naturally."
        p "One wrong move could have fucked it all up, and... let's be real, you trip over your own feet half the time."
        show qp 102
        mc "Wait, you knew what Nancy told me too?!"
        show qp 101
        p "I suspected."
        p "But thanks for confirming it."
        show qp 102
        mc "You definitely inherited her shrewd mind, there's no doubt about that..."
        mc "Heh, I'm kinda envious of that."
        mc "I usually don't overthink things. Or... even {i}think{/i} things too much."
        show qp 101
        p "I know. You’ve got that whole golden-retriever energy."
        p "Carefree, kind, simple. All heart."
        p "But... I actually really like that about you."
        p "It's cute."
        show qp 102
        mc "I can’t believe we’re actually having this conversation."
        mc "I was... terrified."
        mc "Thought you’d never understand, or... worse, think I was lying."
        show qp 103
        p "I mean... believe me, it took a {i}while." with dis
        p "I think I went through all stages of the emotional rollercoaster like twice a day for a whole week."
        play sound pop
        scene qp 104
        p "Shock."
        play sound2 pop
        scene qp 104b
        p "Anger."
        play sound pop
        scene qp 105
        p "Denial."
        play sound2 pop
        scene qp 107
        p "Depression."
        play sound pop
        scene qp 108
        p "Horniness."
        mct "I'm not familiar with that one..."
        play sound2 pop
        scene qp 109
        p "Then anger again."
        p "And finally, after a lot of pacing around and late-night overthinking..."
        play sound pop
        scene qp 110
        p "Acceptance."
        show qp 101
        p "You're lucky you were in Hyril'ar while I was melting down, you got to skip the worst parts."with dis
        scene qp 102
        mc "*Chuckles* Guess I'll have to thank my captors after all."
        mc "I was so scared of this moment."
        mc "I didn't want to lose you."
        show qp 103
        p "I just came to the conclusion that... if you’re really honest, if you really love us, and you’re not just screwing around... then maybe it’s... worth it."with dis
        show qp 101
        p "I mean, it’s 2034. This probably isn’t the freakiest thing you’ll see on the street nowadays."with dis
        show qp 102
        mc "*Chuckles* You're not wrong there."
        show qp 103
        p "So... yeah, that's my current perspective, at least."with dis
        show qp 101
        p "You better take advantage before hormones or second thoughts kick in."with dis
        play sound clothes3
        play sound2 couchlouder
        scene qp 111
        p "Now... before we go back downstairs..." with dis17
        p "I've gotta ask."
        p "Has Alex also fallen prey to your... charms?"
        scene qp 112
        mc "*Raising an eyebrow* Is the DK Tron still active?"
        show qp 111
        p "I turned it off."
        p "I'm simply trusting you now."
        show qp 112
        mc "I see..."
        menu:
            with dis
            "[gr]Yes":
                mc "...I guess there's no point in continuing to hide anything from you anymore."with dis
                scene qp 113
                p "Hah! I KNEW IT!"with dis08
                scene qp 111 
                p "I knew she had feelings for you!"with dis08
                p "I'm damn good with these kinds of things."
                show qp 112
                mc "Hey, even if she did, I could've also turned her down."
                mc "Didn't you consider that possibility?"
                show qp 111
                p "*Snorts* Please, [mc]."
                p "As if a horndog like you could ever turn down a hot girl like her."
            "No":
                $ toldpennynotalex = True
                mc "But nope. She hasn't."with dis
                show qp 114
                p "Really? Never?" with dis08
                p "Huh."
                p "Weird..."
                show qp 115
                mc "Weird? How?"
                show qp 114
                p "I don't know, I thought she also had a crush on you."
                show qp 111
                p "Because obviously it would be her choice. You’d never turn down a hot girl like that, you horndog." with dis08
    else:
        p "I was so scared you were just a horndog playing around."
        p "Playing with..."
        p "Well... with my feelings."
        play sound clothes3b
        show qp 111
        p "Maybe you {i}are{/i} different from other men after all." with dis17
        p "Still a horndog, but... maybe different."
    show qp 112
    mc "*Chuckles* Hey! Who are you calling a horndog?!"
    show qp 111
    p "I’m calling the guy who couldn’t keep his eyes off my boobs during what was supposed to be a serious conversation a horndog."
    p "You might have really fallen in love, but deep down you’re still just a horny boy."
    show qp 112
    mc "*Now staring openly* ...Okay, that's fair."
    mc "You've gotta admit, it’s impossible not to look when the best pair of tits in the country are right in front of me."
    p "*Snorts* Hmph."
    mc "We should really take a picture of you in that bikini. Immortalize them while they’re still perfect."
    if not acceptandgowithher:
        show qp 111
        p "Yeah... you should’ve thought about that before I had to drag you up here just to talk to me."
        p "You blew your chance of being my photographer today, sorry."
        show qp 112
        mc "Oh, come on!"
        mc "I didn't even know what this was about!"
        show qp 111
        p "Exactly! That's the point."
        p "This is your punishment."
        show qp 112
        mc "But–"
        show qp 111
        p "Ah, ah, ah, too late now."
        p "Come on, let's go back downstairs."
        show qp 112
        mc "You're evil..."
        p "*Giggles* Hm-mh."
        jump dinnerchristmas
    mc "You're not gonna have these tits forever, y'know?"
    show qp 113
    p "Huh! How dare you!"with dis08
    show qp 111
    p "For your information, these tits are not going anywhere."with dis08
    p "Haven't you seen my mom? She’s almost twenty years older than me, and hers are still as firm as a twenty-year-old’s."
    p "Genetics are on my side, [mc]."
    p "If you want that picture, just admit you want it for yourself."
    show qp 112
    mc "*Smirks* How about you keep working on that cabinet while I go grab my phone...? It'll be just a second."
    show qp 114
    p "What cabinet?"with dis08
    show qp 115
    mc "The one behind you. Weren't you messing with it when I came in?"
    show qp 117
    p "Ohh... that one." with dis15
    p "I was actually setting up the polygraph machine when you opened the door, I just pretended to be looking at it so you wouldn’t suspect and wonder why I was on the floor."
    mc "Ohh... really?"
    mc "You're way too clever for your own good..."
    show qp 116
    p "It actually belongs to the owner."with dis12
    p "I assume he keeps personal stuff in there, and doesn’t want guests snooping."
    show qp 115
    mc "Huh... mysterious."
    mc "Should we open it?"
    show qp 114
    p "With what? We don't have the key."
    show qp 115
    mc "The key? Please... keys are for amateurs."
    mc "You’re talking to a guy who didn’t play Eternum until he was eighteen."
    play sound chair2
    play sound2 clothes3
    scene qp 118 with dis15
    mc "While everyone else was in Eternum, I spent most of my high school years locked in my room grinding old PC games." with dis12
    scene qp 120
    mc "Over a thousand hours in Skyrim, another thousand in modded Skyrim Legendary Edition, and another thousand in the Skyrim Remake." with dis12
    mc "I think I know how to pick a lock, thank you very much."
    show qp 119
    p "*Snorts* Impressive resume."
    show qp 120
    mc "I'll tell you what — if I manage to open it, you have to let me take a sexy picture of you."
    mc "Deal?"
    show qp 119
    p "Sure! I'd be too impressed to say no."
    show qp 120
    mc "Aha! Now we're talking!"
    show qp 118
    mc "Hmmm... just a simple keyhole." with dis
    mc "All I need is some kind of hairpin or bobby pin to open it."
    show qp 120
    mc "You got any?" with dis
    show qp 119
    p "Yeah, I've got some in my purse."
    show qp 120
    mc "Excellent!"
    scene qp 118
    mc "Alright..." with dis12
    mc "This is the moment you've been waiting for, [mc]."
    mc "Time to put all those thousands of hours playing RPGs to good use and impress your girl."
    mc "I just have to be veeery careful..."
    mod "Unlock for a scene."
    if not renpy.variant("pc"):
        bla "For Android users: Move the pick on the top half of the screen, and the lock on the bottom half."
label lock_game_test:
    $ lock1 = LockGame(sweet_angle=3, pick_dmg=0.7, attempts=4, resize=1920)
    call screen lock_game(lock1) with dis12
    $ lock_success = store._return
    if lock_success:
        jump lock_game_success
    else:
        jump lock_game_fail
label lock_game_fail:
    play sound lockopen
    play sound2 lock_pick_break
    scene qp 118
    bla "You snap the last pin." with dis
    mc ". . ."
    mc "Dammit."
    scene qp 119
    p "*Snorts* Looks like you should’ve invested another thousand hours in Skyrim, [mc]." with dis
    p "Now you owe me four pins."
    show qp 120
    mc "This crap's harder than in video games..."
    mc "I should have watched a Youtube tutorial first."
    show qp 119
    p "Come on, let’s head downstairs before you break something else."
    show qp 120
    mc "Awww, no photo?"
    show qp 119
    p "No photo."
    p "Maybe I’ll consider giving you another chance if we find more lockpicks somewhere. What do you say?"
    show qp 120
    mc "Deal!"
    mc "We're still in the game, [mc]..."
    show qp 119
    p "Now let's go, my little wannabe thief..."
    jump dinnerchristmas
label lock_game_success:
    play sound cabinet
    play sound2 lockopen
    scene qp 121
    mc "*Opens the cabinet* Bingo!" with dis12
    scene qp 122
    p "Wow! You..." with dis
    p "You really did it!"
    scene qp 121
    mc "Of course I did! Did you think I was bullshitting you?" with dis
    play sound noise3
    scene qp 123
    mc "Now let's see what our host is hiding in here..." with dis12
    mc "Oh-ho-ho..."
    mc "Penny..."
    show qp 124
    mc "I think this guy was seriously kinky... this is some serious sex dungeon stuff!" with dis12
    mc "Look at this! Rope! And a blindfold!"
    mc "The red neon lights finally make sense!"
    show qp 125
    p "*Snorts* You're such a pervert, [mc]. You ever think about anything besides sex?" with dis
    p "Blindfolds are used for sleeping, you know?"
    p "And rope? Really? People actually tie things down that aren’t naked women."
    play sound2 noise3
    scene qp 123
    mc "Okay, okay, that's fair..."with dis 
    mc "I’ll admit, my imagination has a dirty autopilot mode."
    mc "But you're right."
    scene qp 126
    mc "I suppose this dildo and this..." with dis12
    mc "*Reading the label* {i}“Anal lubricant for extra dilation”{/i} must be for unclogging the drains and wiping down the kitchen counter."
    scene qp 127
    p ". . ."with dis12
    scene qp 128
    p "*Laughs* Okay, okay, fine, I take it back." with dis
    p "You win this one."
    stop music2 fadeout 13
    $ renpy.music.set_volume(0.8, channel='soundloop3')
    play soundloop3 clock2 fadein 9
    play sound clothes3
    play sound2 couchlouder
    scene qp102 with dis15
    play soundlow chair1
    mc "*Bouncing onto the bed again* Well, well, well..." with dis12
    mc "I think someone owes me a photo."
    p "Mm-hm."
    scene qp 101
    p "Yes, yes..."
    p "Go ahead."
    p "Is this angle good enough for your little portfolio?"
    scene qp 102 
    mc "*Smirks* It's certainly a {i}great{/i} angle, but..."
    mc "There's one thing that would make it a smidge better."
    show qp 101
    p "Oh, naturally."
    p "Let me guess..."
    p "You want me to take my top off?"
    show qp 102
    mc "Of course not!"
    mc "Who do you take me for? Some kind of pervert?"
    show qp 101
    p "*Laughs* Honestly? Yeah, that's exactly what I take you for when you look at me with those eyes."
    show qp 102
    mc "Sit on the side of the bed and I'll show you what I mean."
    mc "You won't regret it when you see the result, trust me."
    p ". . ."
    p "*Snorts* Hmph."
label ga_penny4:
    play sound clothes3b
    play sound2 couchlouder
    $ renpy.music.set_volume(0.75, channel='music3')
    $ renpy.music.set_volume(0.0, delay=29.0, channel='soundloop3')
    play music3 pennyamusic2 fadein 8
    scene qp 129
    bla "Penelope obediently crawls to the edge of the bed." with dis2
    play sound clothes3
    play sound2 couchlouder
    scene qp 130
    mc "*Sliding behind her* And now..." with dis17
    mc "How about we check how this thing looks on you...?"
    scene qp 131
    p "The blindfold? That's your big idea?"
    show qp 130
    mc "It's gonna look so hot! Don't you think so?"
    show qp 131
    p "*Giggles* If you say so."
    p "Alright, fine, but let's make it quick before someone downstairs notices we're missing."
    show qp 130
    mc "I'll be super fast."
    play sound clothes3
    scene qp 132
    bla "You tie the silken blindfold snugly around her head." with dis17
    mc "Can you see anything?"
    p "Damn, I can't. Not a thing."
    p "It makes me feel so..."
    mc "Horny?"
    scene qp 133
    p "*Laughs* I was gonna say... vulnerable."with dis06
    show qp 134
    mc "Feeling vulnerable turns you on?"
    mc "Naughty girl..."
    show qp 133
    p "*Giggles* Now you're just putting words in my mouth."
    show qp 134
    mc "So you're not getting turned on...?"
    show qp 133
    p "Not one bit."
    show qp 134
    mc "Really...?"
    play sound rubbody fadein 1
    play sound2 couch
    scene qp 135
    mc "And... what if I... do this...?"with dis17
    p "Hah... even less..."
    mc "Oh, reaaally...?"
    play soundloop2 kissing fadein 2
    scene pennya0 with dis2
    bla "You press your lips against Penelope's neck, trailing soft kisses over her skin as your hands slide over her curves." with dis12
    p "*Soft moan* Aaahhh..."
    p "[mc]..."
    p "I-I know what you're trying to do..."
    p "Stop..."
    mct "God... I almost forgot how huge her tits feel in my hands..."
    mct "She drives me insane..."
    p "[mc]..."
    p "Enough..."
    p "I-I can’t go back down there with a hickey..."
    p "Let's–"
    p "*Soft moan* Aahhh..."
    p "L-Let's just take that p-picture and leave..."
    p "Alright...?"
    mct "I love her smell..."
    p "Let's just–"
    p "*Moans* Mmmhh..."
    p "F-Fuck..."
    stop soundloop2
    play sound clothes2
    play sound2 couchlouder
    scene qp 136
    p "A-Alright, alright, e-enough!" with dis 
    p "Y-You win! The blindfold... the kisses on my neck... it makes me fucking melt. Happy now?"
    scene qp 137
    mc "*Chuckles* Happy to see you skipping straight to the acceptance phase. Or maybe the horniness one?"
    mc "You always love to tease me, but in the end, you're even more of a horndog than I am... who would've thought?"
    play sound whoosh6
    play sound2 chair1
    play sound3 couchlouder
    scene qp138
    p "*Pushing you against the bed* Hah! Excuse me?!" with vpunchslow
    p "I might get turned on if you push the right buttons, okay, but you?! You're horny twenty-four-seven!"
    p "{i}You{/i} are the horndog!"
    scene qp 139
    mc "Mmm, I don't know, Penny..."
    mc "Those hard nipples showing through your bikini tell a different story..."
    show qp 138
    p "*Giggles* Oh, of course, because the thing poking below me right now must be your pocket Bible, right?"
    scene qp 139
    mc "Oh, that...? It's just the handle from the axe I used to chop all that wood."
    show qp 138
    p "*Laughs* The axe handle?"
    p "And you're keeping it in your pants because...?"
    show qp 139
    mc "Didn't have any free hands left."
    show qp 138
    p "*Snorts* Ah, of course."
    p "You always have an answer for everything, don't you?"
    show qp 139
    mc "*Grinning* I try my best."
    play sound3 clothes3b
    play sound2 couchlouder
    scene qp 140
    bla "Penny’s fingers wander down into your pants, fumbling playfully until they find the button of your trousers." with dis17
    play sound clothes5b
    scene qp 141 with dis2
    mc "See...? Told you. Just the axe handle."with dis12
    play sound3 clothes3
    play sound2 couchlouder
    scene qp 143
    bla "Penny's fingers curl around your cock with a teasing squeeze as she straddles you again." with dis17
    scene qp 142
    p "Oh, is it...?" 
    p "I might not be an expert, but I don’t know... this feels like a pretty squishy axe handle to me."
    scene qp 143
    mc "D-Does it...?"
    mc "M-Must be true what they say, when you lose one sense, your others sharpen..."
    show qp 142
    p "*Pretending to gasp in awe* But the more I squish it, the harder it gets!"
    p "Fascinating! Maybe I should write my research paper about this..."
    play sound clothes3
    show qp 144
    mc "*Squeezing her tits* Oh, fuck, Penny..." with dis15
    mc "How long are you gonna keep torturing me like this?"
    p "*Giggles* Torture? The whole blindfold thing was your idea."
    p "If anything, it looks to me like you're getting your way... like you always manage to do with me."
    mc "Am I...? Or are you just letting me?"
    p "*Grins* Hmm."
    play sound clothes3
    scene qp 145
    bla "You hook your fingers under the top of her bikini, tugging it to the side until her massive breasts finally spill free." with dis2
    mc "My god..."
    p "Like what you see...?"
    mc "I thank the gods above for not being the blindfolded one right now..."
    play soundloop wettingslow fadein 2
    $ renpy.music.set_volume(0.4, delay=12.0, channel='music3')
    play sound clothes3oily
    scene pennya1 with dis2
    bla "You instinctively take Penelope's nipple into your mouth. She arches her back with a soft moan, starting to stroke you with deliberate, slow pumps." with dis
    p "*Soft moan* AAahhh..."
    mct "Good gracious, she tastes so good."
    mct "Her nipple stiffened instantly the moment my tongue touched it."
    p "Aaaahh..."
    p "[mc], you... b-bad boy..."
    p "Mom said no snacking before dinner..."
    p "*Moans* Mmmmmhhh..."
    p "W-When are you gonna... take that picture, [mc]...?"
    play sound clothes3oily
    stop soundloop fadeout 1
    scene qp 146
    mc "*Panting* H-Honestly...?" with dis15
    mc "I don't really care about the picture anymore..."
    mc "I just want to devour every single inch of you... down to the very last freckle..."
    play sound clothes3oily
    play sound2 clothes2
    play soundloop wettingslow fadein 2
    scene pennya2 with dis2
    bla "You toss her top away, and continue sucking her tits even harder." with dis
    p "*Soft moan* A-A-Aaaahhh..."
    p "Mmmmmhh...!"
    mct "I love the little squeal she makes every time I twist a nipple."
    p "*Moans* AAaahhh..."
    mct "Her nipples are so sensitive..."
    p "Oh... y-yes..."
    p "Eat me up..."
    mc "Mmmhh..."
    p "Everything's... for you..."
    play sound clothes3oily
    play sound2 blowpop fadein 1
    stop soundloop fadeout 1
    scene qp 147
    mc "*Squeezing her breasts together* O-Oh, Penny..." with dis15
    mc "I'm getting way too worked up..."
    mc "I feel like I'm about to reach the point of no return..."
    show qp 148
    p "*Giggles* The point of no return...?"
    p "That sounds... dangerous."
    p "Tell me, what happens, exactly, when you cross that point?"
    p "Do you turn into a wild animal or something...?"
    play sound clothes3oily
    play soundloop wettingslow fadein 2
    scene pennya2 with dis2
    bla "She squeals as you roughly suck her totally erect nipple once more." with dis
    p "AAAagh...!"
    p "Hah... I guess..."
    p "I-I guess that answers my question..."
    mc "Mmmmhh..."
    p "Oh, [mc]..."
    play sound2 blowpop fadein 1
    play sound clothes3oily
    stop soundloop fadeout 1
    scene qp 147
    mc "O-Oh, Penelope..." with dis15
    mc "I think I'm gonna need more than just your hands here..."
    show qp 148
    p "Uhh..."
    p "Are you really that needy?"
    show qp 147
    mc "Yeah... it's quite serious, I'm afraid."
    show qp 148
    p "Well... maybe..."
    p "Maybe I can do something about that..."
    play sound couchlouder
    play sound2 clothes3b
    play sound3 ["<silence 0.3>", footsteps4] volume 0.33
    scene qp 149 with dis2
    bla "You take your jacket off and sit on the side of the bed, as Penny carefully moves in the dark until she touches your cock with her legs." with dis15
    p "Ohh..."
    play sound4 wood2 volume 0.33
    play sound5 clothes3
    scene qp 151
    p "*Kneeling down* Look at what I found here..." with dis17
    p "*Giggles* Your... axe handle."
    scene qp 150
    mc "*Chuckles* Yeah..."
    mc "You should give it a try..."
    p "Mm-hm."
    $ renpy.music.set_volume(0.3, delay=12.0, channel='music3')
    scene pennya3 with dis2
    p "Mmmm..." with dis
    p "Like... this...?"
    mc "Y-Yeah..."
    mc "Just like this..."
    p "Mmmmh..."
    mct "God..."
    mct "Each one of her soft little kisses sends a shiver up my spine."
    p "*Giggles* Look at you twitching already..."
    p "You should learn to savor the moment, [mc]..."
    p "...I know I am."
    mc "You tease..."
    p "Mmmh..."
    p "Do you even know how many people beg me for a kiss in my Insta DMs? You should be veeeeery grateful right now..."
    mc "Hah... I bet too many."
    mc "How much do you think you could earn if you ever opened an OnlyFans?"
    p "Haha... I could probably retire us all in a matter of weeks."
    p "Why? Do you want me to open one?"
    p "Because I'm afraid that'll never happen, even for you."
    scene pennya4 with dis2
    mc "Nah..." with dis 
    mc "Your body is only for me..."
    p "Ohh..."
    p "So possessive..."
    p "But..."
    p "*Softly* I like it..."
    p "Because... you're right..."
    p "Everything you see..." 
    p "*Softly* Is only for you..."
    mc "Oh, Penny..."
    mc "I can't bear it anymore..."
    p "What...?"
    p "You don't like my kisses...?"
    mc "You know what I mean..."
    mc "I need more... I need your mouth around me..."
    p "My mouth...? Around all of this...?"
    mc "Around {i}all{/i} of this..."
    p "*Giggles* You’re not secretly recording me, right? Taking advantage of little old blind Penny...?"
    mc "*Grins* That’s actually not a bad idea. Maybe I should grab my phone."
    play sound clothes3
    play sound couch
    scene qp 151 with dis12
    p "*Pushing you back* Nuh-uh, you're not going anywhere." with dis12
    show qp 150
    mc "Oh, really...?"
    mc "And what are you gonna do to keep me here, Miss Penny?"
    scene qp 151
    p "*Giggles* Well, I've got a few ideas..."
    show qp 150
    mc "Show me, then..."
    p "*Giggle* Hmmph."
    play sound blow6 fadein 1
    play sound2 clothes3oily
    play soundloop blowjob2 fadein 2
    scene pennya5 with dis2
    bla "Penelope's mouth finally closes around your cock." with dis 
    mc "O-Oooohhh f-fuck yes, finally..."
    p "*Muffled moan* Mm-hmmm..."
    mc "Aaahh..."
    mc "Y-Yes..."
    mc "Y-You have no idea of h-how much I needed this..."
    p "*Moaning* MmmmMmmhhh..."
    mc "Y-Yeah..."
    mc "Take it all, Penny..."
    mc "Every fucking inch..."
    p "*Assertively* Mmm-hmmm..."
    mc "Ohh f-fuck yeah... slobber all over it..."
    p "*Choking* GGGhhhggh..."
    scene pennya6 with dis2
    bla "Penny continues sucking your cock, her hesitant movements growing more confident with each head bob." with dis
    mc "C-Christ, this feels unreal..."
    mc "So fucking good..."
    p "*Gagging* Mmmhhh..."
    mc "Yeah... keep moaning like that..."
    mct "God, I love seeing her getting totally lost in it..."
    mc "J-Just like that... deeper..."
    mc "I want you to memorize every inch of my cock..."
    mc "My veins... my musk... my taste..."
    p "*Moaning loudly* MMmmhhh... nnnghh..."
    mc "Oh yeah..."
    mc "Your moans are turning shameless, Penny..."
    mc "You're a filthy, nasty little girl..."
    p "*In agreement* Mm-hmm..."
    mc "Yeah..."
    play sound blowpop fadein 1
    stop soundloop fadeout 2
    play sound2 clothes3oily
    scene qp 152
    p "*Catching her breath* AAaaghhh... J-Jesus..." with dis15
    p "B-Blind or not, I can tell this thing is f-fucking thickkk..."
    p "A-And... it's t-throbbing like crazy..."
    mc "That's because he likes you."
    scene qp 152bb
    p "*Laughs breathlessly* Does he...?" with dis
    mc "Oh, he {i}loves{/i} you..."
    p "Whoa..."
    p "I'm so flattered... thank you, Mr. [mc]'s Cock."
    play sound blow6 fadein 1
    play sound2 clothes3oily
    play soundloop blowjob2 fadein 2
    scene pennya7 with dis2
    bla "Penny takes you into her mouth again, almost moving on instinct. Every shake of her head yearning, eager." with dis
    p "*Moaning* MmmmmMmmmnnhh..."
    mc "O-O-Ohhh my god..."
    p "*Gagging* Mm-M-MmMMmhh..."
    mct "Ohh, fuck, I need to calm down or I'm gonna cum way too fast..."
    p "*Desperately* Mmmmhhh... mmmMMMHHh!"
    mc "G-God, you were {i}starving{/i}, Penny..."
    mc "You know Nancy said to leave an empty stomach for dinner?"
    p "Mm-mhm...."
    mc "H-How wet are you right now?"
    mc "Bet your panties are soaked..."
    p "*Loud, needy moan* Mmmmhhh..."
    mc "G-Good girl..."
    mc "So fucking naughty..."
    $ renpy.music.set_volume(0.5, delay=15.0, channel='music3')
    stop soundloop fadeout 2
    play sound clothes3oily
    play sound2 blowpop fadein 1
    scene qp 152
    p "*Breathless* AAaagghhh... [mc_dash]..." with dis15
    p "*Panting* F-Fuck, I-I need..."
    mc "Yeah...?"
    p "I-I n-need you to..."
    p "T-To..."
    p "I need you to {i}fuck{/i} me..."
    mc "Oh, babe..."
    play sound wood2 volume 0.25
    play sound2 clothes3
    scene qp 152b
    mc "*Standing up* Would you look at that... how the tables have turned." with dis14
    mc "The queen of teasing is now begging for more..." 
    mc "Finally got too horny, eh, Penny? Or maybe... you just love being on the submissive side?"
    p "*Breathing heavily* Please..."
    p "B-Before we're... called for dinner..."
    p "Please... [mc]..."
    menu:
        with dis
        "Make her call you something different":
            menu:
                with dis
                "Master":
                    $ mcpsex = "master"
                "Daddy":
                    $ mcpsex = "daddy"
                "(Other)":
                    $ mcpsex = renpy.input("What should she call me?", exclude='\\[]{')
                    while mcpsex.lower().strip() in ['dalia', 'nancy']:
                        p "W-What...?" with dis
                        p "F-Fuck no."
                        $ mcpsex = renpy.input("What should she call me?", exclude='\\[]{')
            mc "Call me [mcpsex]..." with dis 
        "No nickname":
            $ mcpsex = mc
            mc "What do we say...?"with dis 
    p "*Whispers* Please, [mcpsex]..."  
    mc "Now, {i}that's{/i} a good girl..."      
    mc "Take off your shorts for me..."
    play sound wood2 volume 0.3
    scene qp 153
    bla "As if she had completely surrendered to her hunger, Penny obeys and slowly rises to her feet." with dis17
    play sound2 rubbody
    scene qp 154 with dis17
    mc "Oh, lord..." with dis12
    mc "It doesn't matter how many times I see you like this, Penny... you still leave me breathless."
    p ". . ."
    play sound7 wood2 volume 0.16
    scene qp 156
    bla "She leans against the wall." with dis2
    scene qp 155
    p "How... how much time do we have left before we have to...?"
    show qp 156
    mc "Well... Nancy did say fifty minutes like half an hour ago, so... maybe twenty left?"
    mc "...Probably less, to be safe."
    p ". . ."
    scene qp 157
    p "*Smirks* Hmmph." with dis
    mc "I might not see your eyes under that blindfold, but I know something wicked is building in your mind..."
    show qp 158
    p "Tie me up..."
    show qp 157
    mc ". . ."
    mc "What...?"
    show qp 158
    p "With the rope we found earlier."
    p "Tie me up to one of the wooden rafters on the wall."
    show qp 157
    mc ". . ."
    mc "You little nympho..."
    show qp 158
    p "Please..."
    p "Tie me up, [mcpsex]..."
    p "*Softly* Make me yours... only yours..."
    show qp 157
    mc "You naughty girl..."
    play sound noise3
    scene qp 159 with dis2
    play sound3 knot
    bla "Wasting no time, you take the rope and lift her arms high, knotting her wrists together and binding her to the wall." with dis17
    play sound rope2
    play sound2 rope
    play sound7 rope2
    scene qp 160
    p "*Gasps* AaAahh...a-ha..." with dis
    play sound6 clothes3
    scene qp 162
    p "Hah... I've..." with dis17
    p "I've been such a bad girl, [mcpsex]..."
    p "I deserve a spanking..."
    scene qp 161
    mc "You certainly do..."
    scene qp 163
    mc "Guess we’ll find out soon if these walls are really soundproof..." with dis14
    menu:
        with dis 
        "Spank her":
            $ pennyspank = True
            scene pennya8 
            pbt "AAAaaGHh... aaaaGGHh... AaaaAGgHHhh..." with dis2
            pbt "Yesss..."
            mc "You're enjoying this, aren't you...?"
            p "H-Hah..."
            p "F-Fuck... {i}YES..."
            mc "I've said it before, and I'll say it again, Penny — your ass is criminally underrated..."
            p "Aagghh..."
            p "Y-Yeah... h-hit it harder..."
            p "Punish me, [mcpsex]..."
            p "I-I've been soooo bad..."
            p "Such a bad girl..."
            mc "You really are such a deviant..."
            mc "I can literally see your pussy dripping through those panties."
            p "*Squeals* AAaagghh..."
            p "I'm f-fucking soaked... agh... I... I need..."
            p "AAaaaGGhh... I need... cock. I-I need... your cock..."
            p "I need you to... aaaghhh... shove it inside m-me now..."
            p "MmmmhhhhHhh..."
            p "P-Please, [mcpsex]..."with dis08
            p "{i}Fuck... me..." 
            play sound2 rubbody
            play sound rope2
            scene qp 164 with dis15
            bla "You take Penny's panties off and pull her hips towards you." with dis
            mc "Oh, FINALLY..."
            mc "You ready?"
            p "Mm-hm..."
            mc "Bring that pussy here..."
        "Fuck her":
            play sound rope2
            scene qp 164
            mc "*Pulling her towards you* But... no spanks." with dis15
            mc "We've got no time for that..."
            p "W-What?!"
            p "But... [mcpsex]–"
            mc "I'm sorry, Penny, but I need your pussy. And I need it now."
            p "O-Oh, god..."
    $ renpy.music.set_volume(0.4, delay=12.0, channel='music3')
    play sound penetration2
    scene pennya9 with dis2
    bla "You sink your cock into Penelope — slick, warm, and indescribably tight." with dis 
    p "*Gasping* Oh, fuuuuuucckkkkgghh..."
    mc "O-Ooh my god, I had forgotten how tight you are..."
    mc "You're choking my cock, Penny..."
    p "O-Oh sweet b-baby Jesus, I c-can't..."
    p "*Voice cracking* It's... it's {i}too good..."
    mc "Oh yeah, it is..."
    mc "F-Fuck, I love you Penny..."
    mc "Your pussy feels like it was made only for me..."
    p "Hah..."
    p "Maybe... it was..."
    scene pennya10 with dis2
    bla "You slam into her harder, her pussy squeezing around you with every thrust."with dis
    p "*Screaming louder* AAaaAAAAhhh... AAAHH!"
    mc "*Growling* Ooooohh, f-fuck yes..."
    mct "I can feel my cock spreading her..."
    p "AAAAhhh... aaahhhh... aaAGGH!!!"
    p "SO GOOD..."
    p "AAAAghh..."
    p "Y-Yeahh... show me I'm yours..."
    p "Y-YES!"with hpunch 
    p "Fuck me harder, [mcpsex]!" with hpunch
    p "DEEPER!" with hpunch 
    psc "OH MY GOD...!" with hpunch 
    scene pennya10b with dis2
    mc "Oh, Penny..." with dis
    mc "Looks like your dream's finally coming true..."
    p "*Gasping* Aahhh... w-whaa...w-what dream?"
    mc "I-In Warthogs... you confessed you wanted to be tied up and fucked senseless at the same time."
    p "*Voice breaking* A-Aaahhh..."
    p "F-Fuck... h-how do you even remember that...?"
    mc "I don't forget anything about you..."
    p "*Moans* R-Really...?"
    mc "*Groans* O-Oooh god, Penny..."
    mc "D-Do you think you can take it even harder?"
    p "H-Harder...?"
    p "{i}F-Fuck yes I can..."
    p "*Begging* Fuck me, [mcpsex]..."
    p "I want you to... break me again..."
    p "I want you to make a mess out of me..."
    play sound rope2
    play sound2 rope
    scene pennya11 with dis2
    bla "You lift Penelope's leg up in the air, and slam back into her with brutal force, the thrumming sounds of your bodies colliding and liquids sloshing radiating through the room."with dis
    psc "AAahh...AAAHHhh...AAAGGGHH...oh my fucking godddd!"with hpunch 
    psc "O-Oh [mc], you're gonna split me open..."
    mc "*Gripping her tighter* I-Isn't that what you wanted?"
    psc "Agghh... Y-Yeahhh..."
    psc "*Screams* AAAagh..."with hpunch 
    psc "D-Destroy me with that cock, [mcpsex]..."with hpunch
    psc "F-Fuck me until I break..."with hpunch
    mc "O-Oh yeah..."
    psc "H-h-GGgghh..."
    psc "*Panting* Nnnghh... so... d-deep.."
    psc "*Panting* This... is... insane..."
    mc "Dear God, no one can take it like you..."
    psc "*Panting* F-For all that's sacred, p-please don't stop now..."
    psc "*Panting* Ffffuuuuuckkk..."
    psc "*Panting* D-DON'T FUCKING STOP..."with hpunchsubtle
    psc "*Screaming* OH MY GODDDD..." with hpunch
    psc "*Panting* OH [mc], IT'S RIGHT THERE..." with hpunch
    psc "*Desperately* D-DON'T STOP..." with hpunch
    p "{sc=3}{size=40}I'M CUMMING!"with hpunch 
    p "{sc=4}I'M–"with hpunch 
    play sound2 slap1
    play sound3 squirt
    play sound7 squirt
    scene qp 165 
    pause 0.01
    p "{sc=4}*Screaming* AAaaaAAAAggh!!!" with hpunchlong3
    play sound3 squirt
    play sound7 squirt
    p "{sc=5}*Screaming louder* AAAAAaaaAAgggnnnnnAAggh!!!" with hpunchlong3
    play sound rubbody
    play sound2 rope2
    play sound4 wood2 volume 0.5
    scene qp166 
    pause 2
    $ renpy.music.set_volume(0.55, delay=15.0, channel='music3')
    play sound3 fallfull
    play sound6 rope2
    bla "Her orgasm tears through her violently, juices spilling down her shaking thighs as she collapses onto the floor." with dis15
    pbt "*Panting* A-aA-AAaahh... aaaaagghhh..."
    pbt "*Panting* V-Virgin Mary's sweet ancestors..."
    pbt "*Panting* T-That was even better than I ever fantasized..."
    mc "*Leaning against the wall* H-Holy fuck, that was certainly... unreal..."
    pbt "*Still panting* Y-You... w-wrecked me..."
    pbt "*Still panting* I-In a matter of seconds..."
    mc "You're just too much, Penny..."
    mc "Are you okay...?"
    pbt "Y-Yeah... I..."
    show qp 167
    pbt "I-I think the rope is cutting off circulation to my wrists, but..." with dis 
    pbt "*Breathless chuckle* I-I c-can't stand up either. M-My [mcpsex] wrecked me..."
    mc "W-What?!"
    play sound rope2
    play sound2 knot
    play soundlow wood2 volume 0.3
    scene qp 168 with dis2
    play sound5 clothes3
    play sound4 couchlouder
    bla "You untie her, as she slowly crawls onto the bed arching her back like a cat." with dis15
    p "Mmmmrr..."
    play sound5 clothes3
    scene qp169 with dis15
    play sound6 chair1
    play sound7 couchlouder
    p "*Purring* Mmmmrrrhhh..." with dis12
    scene qp 170
    p "Hmmm..." with dis14
    scene qp 171
    p ". . ." with dis12
    scene qp 172
    p ". . ."with dis15
    scene qp 173
    p ". . ."with dis14
    scene qp 171
    p "Hmm..."with dis
    play sound couchlouder
    play sound2 clothes3
    scene qp 174
    p "Hey... can I... a-ask you something, [mc]?" with dis15
    show qp 175
    mc "*Catching your breath* Huh...?"
    mc "*Chuckles* More questions? I guess..."
    p ". . ."
    show qp 174
    if daliapath:
        p "Have you ever... fucked Dalia's ass?"
    else:
        p "Have you ever... fucked anyone's ass?"
    show qp 175
    mc "Have I ever–"
    mc "...what?!" with hpunch 
    show qp 174
    if daliapath:
        p "Sounds like something she'd do."
    else:
        p "Have you...?"
    show qp 175
    mc "U-Um..."
    mc "N-Not sure why you're asking now, but... no, I haven't."
    if daliapath:
        mc "I... I've never done that, actually. Like... not with anyone."
    show qp 179
    p "Ohh... never?" with dis 
    show qp 176
    mc "...Nope."
    p "Mmmmh."
    show qp 178
    p ". . ."with dis15
    show qp 177
    p "*Whispering* And... do you want to try...?"
    show qp 178
    mc ". . ."
    mc "Are..."
    mc "Are you serious right now...?"
    p "Mm-hm."
    show qp 177
    p "I want you to fuck me in the ass, [mcpsex]..."
    p "*Giggle* I... I can't help but feeling so curious right now."
    scene qp 179
    p "I wanna be your first." with dis15
    p "I want to feel you... stretch me there..."
    show qp 176
    mc ". . ."
    mc "Are you... sure?"
    mc "Won't it hurt you...?"
    show qp 179
    p "We can use the lube we found."
    p "And... it can't be that bad. A little bit of pain never killed anyone."
    p "I'm a big girl. I can endure it."
    show qp 176
    mc "You crazy little masochist..."
    show qp 179
    p "You better decide fast, [mcpsex]."
    p "Someone could be knocking on that door any second..."
    $ pennysexxmas = True
    show qp 176
    menu:
        with dis
        "Have anal sex with Penny [gr][mt](Anal)":
            $ pennyanal = True
            mc "Oh boy..."with dis
            mc "Fuck it..."
        "End it here":
            stop music3 fadeout 20
            play soundloop2 clock2 fadein 9
            mc "As much as I’d love to... and trust me, you have no idea how {i}tempting{/i} that sounds..."with dis
            mc "*Glancing at the door* ...this has already been an insane few minutes."
            mc "Let's not push our luck too much."
            show qp 174
            p "Awwwww... really?"with dis 
            p "You're gonna leave me hanging like that?"
            show qp 175
            mc "You’ll thank me later when you come back to your senses, trust me."
            mc "But don’t think you can take back what you just said."
            mc "I’ll remember it next time, Penny... word for word."
            show qp 176
            p "Hmph." with dis 
            show qp 179
            p "Guess I'll have to stay curious a little longer..."
            show qp 176
            mc "*Smirks* That keeps the flame alive."
            show qp 179
            p "*Snorts* If anything, I could probably use a little less fuel on my flame."
            p "You manipulate me with your tricks wayyyy too easily."
            show qp 176
            mc "{i}My{/i} tricks?! That was all you!"
            show qp 179
            p "Excuse me?? That was YOU!"
            p "You know I lose all ability to reason once I get turned on enough."
            p "You said it yourself!"
            show qp 176
            mc "So... you regret getting crazy with me?"
            show qp 179
            p "Regret...? Far from that..."
            p "I loved every second of it, and I’d do it a thousand times over."
            p "Hell, I {i}hope{/i} we do it a thousand times over."
            show qp 176
            mc "I certainly hope so too..."
            show qp 179
            p "Now, let's go back downstairs... [mcpsex]."
            p "Before the others start wondering why the whole house was shaking."
            show qp 176
            mc "*Chuckles* Honestly... I could use some replenishment..."
            $ renpy.end_replay()
            jump dinnerchristmas
    play sound chair1
    play sound2 couchlouder
    scene qp 180 with dis2
    bla "As if possessed by a demon, you quickly jump onto the bed, slathering your cock with the lube."with dis15
    mc "Last chance to back out, Penny..."
    p "Nnn-nnn..."
    mc "Alright then... don't say I didn't warn you."
    play sound clothes3
    scene qp 181
    bla "You press the head of your cock against Penny's tight little hole." with dis2
    mc "H-Here we go..."
    mc "I'm gonna try to push... just a little, okay?"
    p "*Trembling with need* Okay..."
    play sound2 ["<silence 0.2>", penetration3]
    scene qp 182 with dis2 
    mc "O-Ooohh SHIT..."  with dis 
    play sound2 ["<silence 0.2>", penetration3]
    scene qp 181
    mc "Aaaggh... Jesus Christ..." with dis17
    mc "There's no fucking way this is gonna fit... not even with all this lube." 
    p "*Panting* N-No..."
    p "P-P-Push it deeper..."
    p "I c-can take it... for my [mcpsex]..."
    mc "Y-You sure...?"
    p "Y-Yes..."
    p "P-Please..."
    mc "I can't say no when you ask me like that..."
    play sound2 ["<silence 0.2>", penetration3]
    scene qp 183
    mc "*Pushing deeper* Ooohhh f-fuckkk..." with dis2
    p ". . ."
    play sound2 ["<silence 0.2>", penetration3]
    scene qp 184
    mc "*Pushing even deeper* FUCKKKKK..." with dis2
    $ renpy.music.set_volume(0.33, delay=12.0, channel='music3')
    scene pennya12 with dis2
    bla "You begin to thrust slowly into her, pressing deeper inch by inch. You can feel her whole body stiffening as you stretch her open."with dis
    p "*Gasping* AAAAaghh..."
    p "Oh F-FUCKK..."
    mc "Oh my god..."
    p "O-OooGGhhh... please, [mcpsex], have mercy..."
    mc "AAAAAghhh... Penny..."
    mc "You're fucking crushing me..."
    mc "It feels like... my cock's gonna snap in half..."
    p "NNnnn-nngh..."
    p "*Panting* This feels so... different..."
    p "*Panting* This... s-sensation..."
    p "*Panting* W-What the fuck..."
    mc "Oh... fuck Penny, this gets dry so quickly..."
    p "N-No..."
    p "D-Don't stop now..."
    p "U-Use more lube if you have to..."
    p "D-Dump the whole f-fucking bottle..."
    p "*Moans* F-Fuck, spit on me if you have to..."
    p "J-Just... shove it d-deeper..."
    mc "You're totally mad..."
    scene pennyanalangleimage 
    show screen pennyangleanal
    with dis2
    bla "Just as she asked, you coat your cock with half the bottle and slam it back in, her ass cooperating more this time as she screams into the mattress."with dis
    p "NNNHhhhghh..."
    mc "Oh god..."
    p "GGgggaaahh..."
    p "Y-Yyaahh... s-stretch me open..."
    mc "Oh my fucking god..."
    mc "I c-can’t believe your ass is swallowing my whole cock..."
    mc "F-Fuck, it's insane..."
    p "*Moaning wildly* Y-Y-Yeah..."
    p "F-Fuck my tiny little ass, [mcpsex]..."
    mc "Oh Penny..."
    p "*Panting* H-Harder..."
    p "*Panting* M-Make me feel it in my tummy..."
    mc "Ohhh Penny... you’re gonna make me lose my f-fucking mind..."
    p "*Panting* D-Destroy my ass, [mcpsex]..."
    p "*Panting* I c-can t-take it ALL..."
    mc "O-Oh Lord, give me strength..."
    play sound chair1
    play sound2 couchlouder
    scene pennya15 
    hide screen pennyangleanal
    with dis2
    bla "You pour out even more lube and hammer her mercilessly."with dis
    psc "HHhh-h-h-hhgghnnh..."
    mcsc "*Grunting* Oh my god, I'm so c-close..."
    mcsc "I-I'm gonna cum s-so... hard..."
    mcsc "T-This shit's too fucking tight..."
    mcsc "A-And I've been holding it for way too long now..."
    psc "Hnnngh... ggghhh... nnnhhh..."
    psc "Y-Yeeh..."
    psc "C-Cum..."
    psc "I-In... m-me... [mcpsex]..."
    mcsc "*Panting* Oh Penny..."
    mcsc "*Panting* I'm at my limit..."
    mcsc "Penny..."
    psc "Y-YEAH!"with hpunch 
    psc "I-I'm g-gonnaaa c-cumm too..."
    mcsc "I'm..." with hpunch 
    mcsc "I'M G–" with hpunch 
    play sound cumall
    play sound2 chair1
    play sound3 couchlouder
    play sound4 slap3
    scene qp185
    mcsc "*Cumming* AAAAAAAAAAaaaghhhh..." with hpunchlong3
    play sound cumall
    play sound3 couchlouder
    mcsc "*Cumming* GGGghhhhhh..." with hpunchlong3
    play sound cumall
    play sound3 couchlouder
    psc "*Orgasming* A-a-a-a-a-a-aaghhh... y-yeahhh..." with hpunchlong3
    mcsc "P-P-Penny... stop shaking like this or..."
    mcsc "...y-you're gonna rip m-my dick straight off..."
    play soundlow chair1
    play sound6 couchlouder
    play sound7 clothes3oily
    play sound8 penetration3
    scene qp 186
    scene qp186 
    with dis15
    bla "You pull out slowly, your cock slick with lube and cum. Penny clenches her ass as your seed oozes out in messy streaks down her thighs." with dis14
    stop music3 fadeout 22
    play soundloop2 clock2 fadein 10
    mc "*Panting* J-Jesus Christ..."
    mc "*Panting* What a mess..."
    p "*Hyperventilating* Ggg-g-g-gnnnhhh..."
    mc "*Panting* Yeah, I agree..."
    scene qp 187 with dis2
    pause 
    play sound3 clothes3
    play sound ["<silence 1.4>", chair1]
    play sound2 ["<silence 1.4>", couchlouder]
    show qp188 
    pause 0.01
    mc "Holy fuck..." with dis15
    play sound3 clothes3
    play sound ["<silence 1.4>", chair1]
    play sound2 ["<silence 1.4>", couchlouder]
    show qp189
    pause 0.01
    pbt "Mm-mmhnhgh..." with dis15
    mc "My god, Penny..."
    mc "You really are incredible..."
    mc "Was this as intense for you as it was for me?"
    scene qp 190
    pbt "*Mumbling* G-gGgghhh...?"
    scene qp 189
    mc "Oh... *chuckles* right, I forgot you kinda short-circuit when you cum too hard."
    mc "Last time you were only able to say “potato” for like twenty minutes."
    scene qp 190
    pbt "*Giggles* H-Hah..."
    pbt "M-My godd, [mc]..."
    pbt "I just had an orrrgasm... from... m-my ass."
    pbt "Ass o-orgasm... h-how the hell is that even... b-bo-bolologically possible...?"
    pbt "D-Do you think I can also c-cum from..."
    pbt "Y-You fucking my mouth? Or... my tits?"
    scene qp 189
    mc "Um... I-I don't think that's how it works, but I think we really should get downstairs before someone comes through that door."
    scene qp 190
    pbt "What about my armpit...?"
    scene qp 189
    mc "Um... h-how about you go splash some water on your face and I head down first?"
    scene qp 190
    pbt "Oh [mc][namelong]..."
    pbt "Ivovvyyou..."
    scene qp 189
    mc "What...?"
    scene qp 190
    pbt "*Giggles* Hahahahhgaa..."
    pbt "*Giggles* Potato..."
    pbt "*Giggles* I 'membered now..."
    scene qp 189
    mct "Oh man..."
    $ renpy.end_replay()
    jump dinnerchristmas


label dinnerchristmas:
    stop music3 fadeout 8
    stop music2 fadeout 8
    stop soundloop2 fadeout 10
    scene black with dis25
    show screen afewminuteslater with dis2
    pause
    hide screen afewminuteslater 
    scene qpp 1
    with dis3
    play music2 ["<silence 2>"]
    queue music2 xmas1 fadein 6
    play sound5 toilet
    pause 3
    play sound footsteps4
    if pennysexxmas:
        scene qpp 2
        mct "Holy shit..." with dis22
        mct "Penny left me wondering what planet I’m on."
        mct "I washed my face and everything, but I still feel all dizzy."
        mct "But... alright, I need to lock in."
        mct "I've gotta look normal when I head back down there."
        mct "No one suspected a thing all those nights I spent drinking with Chang when I was still underage. This is a piece of cake, relatively speaking."
        mct "This time there's not even alcohol involved."
        scene mcfacechange with dis22
        play sound2 ["<silence 0.7>", whoosh2]
        pause 2.3
        scene qpp 3 
        mct "Alright... better." with dis15
        mct "I should be fine as soon as I eat and drink something. Easy-peasy."
    else:
        scene qpp 3
        if not pennymadpolygraph:
            bla "You spend several minutes talking to Penny, tending to the fire, and rearranging Christmas decorations that Penny insists on fixing properly." with dis22
            mct "Phew... that's better." 
        else:
            mct "Phew... that's better."with dis22
        mct "Talking to Penny, I almost forgot how badly I needed to pee."
        mct "Although now..."
    play sound6 stomach
    mc "*Rubbing your stomach* (Damn, I'm hungry. I need something greasy before my body just gives out on me...)"
    play sound stairswood2
    scene qpp 4 with dis25
    bla "You make your way downstairs and find the table already set." with dis
    mc "Holy cow!"
    scene qpp 5
    mct "Look at this!" with dis14
    mct "Feels like I just walked into one of those cheesy Christmas movies!"
    mct "And oh boy, it smells GOOD."
    x "Finally!"
    scene qpp 6
    x "Look who decided to show up!" with dis
    x "Setting the table was supposed to be your job, [mc]."
    show qpp 7
    mc "Sorry, sorry! I’ll make it up by clearing the table and doing all the dishes!"
    show qpp 6
    x "What were you even doing?"
    show qpp 7
    mc "I was..."
    mc "Uh... making a call."
    show qpp 6
    x "Don't bullshit me."
    x "This house is like a bunker. There's no signal in any room."
    show qpp 7
    mc "I know, but I went out to chop some wood! You can actually get a signal outside."
    if axelhelp:
        mc "And you’re not gonna believe who called me out of nowhere."
        mc "Here’s a hint: he disappeared from school two months ago, has a scary dad who’s basically number two in the biggest monopoly on the planet, and a twin sister who's hot as hell."
        show qpp 8
        x "Wait... are you serious?" with dis12
        x "Axel called you? Out of all people?"
        show qpp 9
        mc "Swear to god, I was just as shocked."
        show qpp 8
        x "And... what did he say?"
        show qpp 9
        mc "He wants to meet."
        mc "At the park by Kredon Station, Thursday at 9 PM."
        mc "He didn't want to say much on the phone, but he claimed... William Bardot is the one who killed Benjamin."
        show qpp 11
        x "Hmph." with dis
        show qpp 10
        x "Sounds shady."
        show qpp 11
        mc "Yeah... that was my first thought too."
        mc "Do you think we should go?"
        show qpp 10
        x "You can go if you want to hear him out."
        x "But I doubt he knows anything we don’t already."
        show qpp 11
        mc "You don’t wanna come with me?"
        show qpp 10
        x "Nah, hard pass."
        x "I'm not a Bardot anymore, remember? They can all go fuck themselves."
        x "Axel can talk all he wants, but our plan should stay the same."
        x "This Wednesday, you, Luna, and Chang are plugging that USB into Ulysses’ intranet. Whatever Axel thinks he has, we’ll probably already have it covered."
        show qpp 11
        mc "Mmh, that's true."
        mc "I still might go and see what he has to say, though. I suppose it can't hurt."
        mc "I can meet up with you right after, if you want."
        show qpp 10
        x "Yeah... please, do that."
        x "I’m dying to know if he’s really turned against our dear papa, or... if it’s just another act."
        show qpp 11
        mc "Guess we'll know for sure after this Thursday."
    else:
        show qpp 6
        x "So who was it?"
        scene qpp 7
        mc "Uh..."
        mc "...Scam call."
        x ". . ."
        scene qpp 6
        x "That's like the lamest excuse ever."
        show qpp 7
        mc "Yeah, it doesn't really sound too convincing when I say it out loud..."
    play sound doorsqueakk
    play sound2 dooropen2
    show qpp 12 with dis15
    n "Ah, [mc]!" with dis12
    n "There you are!"
    n "Dinner's ready!"
    show qpp 13
    mc "I saw!" 
    mc "Everything looks so appetizing!"
    show qpp 12
    n "Well, I'm glad to hear that!"
    show qpp 13
    mc "I’ve never had a Christmas dinner like this before, Nan."
    mc "Feels really special."
    x "Same here, Nancy."
    x "Our Christmas dinners were always packed with fancy food flown in from abroad, but none of it ever smelled like this."
    x "Everything always looked... artificial. Not homey, like everything here."
    x "Not to mention that I don’t even remember my father ever sitting at the table with us."
    show qpp 14
    n "Aww, you two are just the sweetest!" with dis12
    n "Please, don't mention it."
    n "I’m just glad we can all share this together. That’s what really matters."
    show qpp 15
    mc "I couldn't agree more!"
    show qpp 14
    n "Speaking of, where's Penny?"
    show qpp 15
    if pennysexxmas:
        mc "Uh... I think she said she was hopping in the shower real quick. She’ll be right back."
    else:
        mc "Uh... I'm not sure, but I think she was with her laptop. She should come downstairs any minute."
    show qpp 14
    n "Ah... perfect."
    n "In that case, we can start grabbing our seats while we wait for her."
    show qpp 15
    mc "Sounds good!"
    play sound2 clotheswhoosh
    scene qpp 16
    d "[mc]! Finally!" with dis08
    if daliapath:
        d "Come, come! I need you to try these cookies!"
        show qpp 17
        mc "Uhhh! Are these the ones you’ve been obsessively tweaking for weeks?"
        show qpp 16
        d "Exactly!"
        scene qpp 17
        mc "Shouldn't we save them for dessert, though?"
        play sound footsteps4
        scene qpp 17b
        d "It's okay! Just taste one!"with dis17
        d "Mom and Alex said they're good, but I need your approval too."
        d "You're the only one here besides me who also eats like a human vacuum."
        d "So... y-yeah."
        show qpp 18
        mct "She really baked this just for me, I can tell."
        mct "Gosh, she can be so adorable."
        mc "*Sniffs* Mmm, damn, they smell amazing already!"
        mc "I assume they're healthy too?"
        scene qpp 19
        d "Healthy as hell!"
        d "No sugar, no bad fats, and each one’s packing thirty grams of protein!"
        d "I used the usual ingredients, but I tried to make them Christmas-shaped this time."
        show qpp 18
        mc "Well, guess I'll have to give them a try!"
        d "*Excitedly* Mmh-mhm!"
        play sound eat
        scene qpp 20 
        bla "You grab one of the cookies and eat it."with dis15
        mc "Hmm..."
        d ". . ."
        mct "Holy shit. This thing actually slaps."
        mct "It's delicious."
        menu:
            with dis
            "Awful":
                mc "Mmh."with dis
                mc "Honestly?"
                mc "It's... pretty awful, sorry. Can't believe you managed to make it both dry and mushy at the same time." 
                show qpp 24
                d ". . ."with dis
                show qpp 23
                d "Ha, ha. Very funny."
                d "For a second I almost forgot you're a dickhead."
                d "Don't worry, I'll eat them all myself so you don't have to suffer."
                show qpp 24
                mc "*Laughs* Relax, I'm just kidding."
                mc "They're actually super good."
                show qpp 23
                d "Too late. You're dead to me."
                show qpp 24
                mc "C'monn, it was just a joke!"
                d "*Grumbles* Mmmrrh."
            "Not bad":
                mc "Mmhh!"with dis
                mc "Hey, not bad!"
                stop music2 fadeout 0.5
                play sound impact
                play soundloop depression volume 0.7
                scene qpp 25
                d ". . ." with dis
                scene qpp 26
                d "...I see. So they taste like vomit."
                show qpp 25
                mc "What?! No! I said not bad!"
                show qpp 26
                d "“Not bad” is what you say when something tastes like the biggest steaming pile of dogshit you’ve ever shoved in your mouth, but you’re too scared the other person’s gonna kill themselves if you tell the truth."
                d "Thank you for trying to spare my feelings, though."
                show qpp 25
                mc "What?! Not bad means not bad!"
                mc "They're really good!"
                show qpp 26
                d "It's okay."
                d "Just another thing I suck at."
                d "I guess it shouldn't surprise me anymore."
                show qpp 25
                mct "Goddammit, I should have been more effusive..."
                stop soundloop fadeout 7
                play music2 xmas1 fadein 2
            "Incredible [dalia_pts]":
                mc "Mmmh!"with dis
                mc "Oh my god."
                mc "Maybe it's because I'm starving right now, but..."
                mc "This might be, like, the best cookie I've ever had."
                $ dalia_points += 1
                play sound beat
                show screen heartbeat
                scene qpp 21
                d "R-Really?" with dis
                d "You're not just saying that?"
                show qpp 22
                mc "I swear on my life, they're delicious."
                mc "The edges are crisp, while the center is soft and warm."
                mc "The texture is perfect and the flavor is incredible. Sweet, but not too sweet."
                show qpp 21
                d "I-I'm glad you like them."
                d "You can eat as many as you want after dinner!"
                show qpp 22
                mc "Please tell me you’re gonna keep baking these."
                mc "I’d ditch my protein shakes in a heartbeat."
                show qpp 21
                d "Of course! I'll make sure to always have some around at home!"
                d "They're under 150 calories each too, so you can go nuts without feeling guilty!"
                show qpp 22
                mc "NICE!"
    else:
        d "Can we finally start eating now?"
        show qpp 17
        mc "Uhh... is that a batch of your famous protein cookies?"
        show qpp 16
        d "Yup!"
        show qpp 17
        mc "Can I try one?"
        play sound footsteps4
        scene qpp 23
        d "Nope. They're for dessert."with dis15
        scene qpp 24
        mc "Aww, c'mon... just one!"
        show qpp 23
        d "I said no! They're for everyone!"
        d "Don't be greedy, you pig!"
        show qpp 24
        mc "Alright, alright..."
        mc "But I need to eat something. I'm starving..."
    scene qpp 27
    n "Alright everyone, it's time to sit down before the food gets cold!" with dis15
    n "[mc], you should sit at the head of the table!"
    mc "Sure!"
    play sound chairmove
    play sound2 ["<silence 0.9>", chair2]
    scene qpp 28
    d "Thank god, finally!" with dis12
    d "I'm sooo hungry!"
    d "I call dibs on the wings! And one of the thighs!"
    play sound chairmove
    play sound2 ["<silence 0.9>", chair2]
    scene qpp 29
    x "Oh boy, I love blue cheese." with dis12
    x "And that ham looks even better than it did in the kitchen."
    play sound chairmove
    play sound2 ["<silence 0.9>", chair2]
    scene qpp 29b
    mc "That turkey looks insanely juicy..." with dis12
    mc "You're an amazing cook, Nancy."
    play sound chairmove
    play sound2 ["<silence 0.9>", chair2]
    scene qpp 30
    n "Come on, don’t compliment me until you’ve tasted it!" with dis12
    n "For all we know, it could be raw inside."
    scene qpp 31
    n "But we should wait for Penny before we start." with dis
    n "She would–"
    scene qpp 31b
    p "I'm coming! Sorry!" with dis 
    play sound runsit
    play sound2 ["<silence 0.9>", chairmove]
    scene qpp 32
    p "*Running down the stairs* WHOOOAAAAA..." with dis2
    p "Oh my god... this is PERFECT!"
    p "The table looks like a Christmas commercial!"
    p "Mom, you're the best!"
    scene qpp 33
    n "It wasn't only me, Alex and Dalia helped too."
    n "*Chuckles* But I’m glad it has your seal of approval, Miss Christmas."
    scene qpp 32
    p "Fully approved!"
    p "I'm so looking forward to trying everything!"
    if penelopepath and daliapath:
        scene qpp 35
        p "But first... just need to tell [mc] something real quick!"
        scene qpp 47
        mc "Huh? Me?"
        p "Yep!"
        play sound wood2 volume 0.3
        scene qpp 34
        bla "Penny leans in and whispers." with dis2
        p "*Whispering* I didn’t get to say it properly earlier with all the chaos, but..."
        p "*Whispering* I just wanted to say that..."
        p "*Whispering* ...I love you too."
        play sound2 footsteps4
        scene qpp 35
        p "Okay!" with dis17
        p "All done! Now we can eat!"
        scene qpp 36
        mc "*Chuckles* (Penelope Paige Carter...)"
        scene qpp 37
        d "What’s with all the secrecy?"
        d "Why don't you share with the rest of the class, sis?"
        play sound chairmove
        scene qpp 38
        p "It’s called a private conversation, sis." with dis12
        p "But I wouldn't expect you to understand."
        play sound wood2 volume 0.5
        scene qpp 39
        if pennyanal:
            play sound3 ["<silence 1>", chair3]          
            p "Maybe you–{w=1.1}{nw}" with dis
            play sound ceramicfall
            play sound2 woodhit
            play sound5 whoosh3b
            scene qpp 40c
            p "{sc=4}*Jumping up* G-Ggghh–!" with hpunchslow
            scene qpp 41
            n "Honey...?"
            n "Are you okay?"
            scene qpp 40c
            p "Y-Yeah."
            play sound wood2 volume 0.4
            scene qpp 42
            p "*Faint voice* I-I'm... *grunts* ...f-fine." with dis14
            p "*Faint voice* N-No worries."
            p "*Faint voice* Just... uh... h-had too much spicy food yesterday, and my butt’s kinda... s-sensitive now."
            scene qpp 41
            n "Oh no!"
            n "Do you want some antacid?"
            scene qpp 42
            p "N-No, it's fine, really."
            p "I just need to... adjust."
            scene qpp 41
            n "Huh... alright then."
            n ". . ."
            scene qpp 43
            n ". . ." with dis
            scene qpp 44
            mc ". . ."
            scene qpp 37
            d "You're so weak, sis."with dis12
            d "I had four extra-spicy burritos at Luna’s place two weeks ago and my butt was totally fine the next day."
            scene qpp 45
            p "Please."
            p "You wouldn’t have survived what I... ate, sis."
            scene qpp 37
            d "Please, I could handle way more than you ever could."
            scene qpp 45
            p "Oh, I'd really love to watch you try, {i}sissy."
        else:
            p "Now shut up and pass me the cheese."with dis
        stop music2 fadeout 9
        scene qpp 46 with dis25
        play music lovefrench2 fadein 2
        if pennyanal:
            d "Want me to go make you some plain rice, grandma?" with dis12
        else:
            d "Oh, but of course, my queen!"with dis12
            d "Do you want me to serve you the drinks as well?"
        p "Actually, yeah, at least then we might get to eat something before you inhale the whole table."
        d "That's it! You're not getting any more of my cookies!"
        p "FINE, I DIDN'T WANT THEM ANYWAY!"
        mc "*Chuckles* Mm-mmh." 
    scene qpp 31
    n "Well, [mc]."with dis14
    n "Will you raise a toast?"
    scene qpp 47
    mc "Me? A toast?" with dis
    scene qpp 31
    n "Of course!"
    n "We're all sitting around this table because of you, after all."
    n "Who knows where we'd be otherwise!"
    n "You deserve the honors."
    scene qpp 47
    mc "Oh..."
    mc "Well... I can try."
    scene qpp 48
    mc "*Raising the glass* Hmm..." with dis15
    mc "*Clears throat* Hmph."
    show qpp 49
    mc "*Chuckles* You know..." with dis08 
    mc "Up until this past year, Christmas didn’t mean shit to me. It was just an excuse to slack off, sleep in, and play games until my eyes burned."
    mc "But now... damn, now I get it."
    mc "It's not about gifts or lights, it's about... being... here."
    scene qpp 50
    mc "This right here..."with dis15
    mc "This is the life I want."
    mc "Sure, we still have our mission hanging over our heads. Ten Gems to hunt down, a destiny none of us asked for."
    mc "But... honestly? I couldn’t care less about the money, the power, or sitting on some throne at Ulysses anymore."
    if penelopepath and daliapath:
        scene qpp 51
    else:
        scene qpp 53
    mc "What I care about is us. All of us."with dis15
    if nancypath or alexpath or daliapath or penelopepath:
        mc "I want to wake up alongside you every damn morning for the rest of my life, without wondering if today’s the day some psycho or evil corporation takes it all away."
    else:
        mc "I want to be with my friends for the rest of my life, without wondering if today’s the day some psycho or evil corporation takes it all away."
    mc "I want you all to be safe. To be happy."
    if penelopepath and daliapath:
        scene qpp 52
    else:
        scene qpp 50
    mc "And for that... I’ll fight."with dis15
    mc "I’ll sweat, I’ll bleed, and I’ll burn the whole world down if I have to."
    mc "So... let's toast to {i}this."
    if harempath:
        mc "To this... fragile, beautiful thing we’ve carved out of chaos."
    scene qpp 53
    if harempath and calypsopath:
        mc "To us, Annie, Luna, Nova, and Calypso." with dis15
    elif harempath:
        mc "To us, Annie, Luna, and Nova." with dis15
    else:
        mc "To all of you."with dis15
    mc "To every memory we’ve already created together..."
    mc "...and to every adventure we still have ahead."
    scene qpp 54
    mc "So... cheers to that!" with dis15
    allofthem "Cheers!" with hpunch 
    if alexpath:
        x "Damn, [mc]..."
    else:
        x "Wow, [mc], what a performance."
    if daliapath:
        d "Holy shit! That was an Aragorn-at-the-Black-Gate level speech!"
    else:
        d "*Chuckles* {i}Not bad, not bad{/i}, [mc]."
    if nancypath:
        n "*Sobbing* That was beautiful, honey."
    else:
        n "That was very nice, honey!"
    if penelopepath:
        p "I didn't know you had a poet inside you, [mc]!"
    elif pennymadpolygraph:
        p "Wow, you speak as well as you lie, [mc]!"
        mc "U-Um..."
        x "Truly spectacular!"
    else:
        p "I didn't know you had a poet inside you, [mc]."
        p "Maybe he doesn't have the best diction, but... at least the thought's there."
    if harempath:
        mc "*Chuckles* Oh come on, it wasn't such a big deal, girls."
    else:
        mc "*Chuckles* Okay, I can tell you're all being sarcastic, so I'll just say... fuck off."
        mc "I was being honest!"
    x "Alright, be honest now... you've been practicing this for a while, haven't you?"
    mc "*Laughs* No, I haven't!"
    n "Okay, okay, let’s not grill [mc] too much about whether he prepared his speech in advance or not."
    n "I mean, he obviously did. And that's totally fine!"
    n "Now let's eat!"
    mc "*Laughs* Oh come on, I said I didn't!"
    if not harempath:
        stop music2 fadeout 7
        jump leavingwinterhouse




label changermeister:
    stop music2 fadeout 9
    stop music fadeout 9
    scene black with dis33
    show screen afewhourslater with dis2
    pause
    $ renpy.music.set_volume(0.45, channel='soundloop3')
    play soundloop3 hottub fadein 4
    hide screen afewhourslater
    scene qpp 55 
    with dis3
    play sound water
    mc "AAahhh..." with dis15
    play soundlow owl
    mct "Good Lord... nothing beats a steaming hot bath outside in winter."
    mct "No wonder the Japanese live for this."
    scene qpp 56
    if nancypath and penelopepath and daliapath and alexpath:
        mct "A full belly, women who love me, and a hot tub while snow’s on the ground. Can a man really ask for anything else?" with dis15
    else:
        mct "A full belly, and a hot tub while snow’s on the ground. Can a man really ask for anything else?" with dis15
    mct "This has already been the best Christmas I've ever had, hands down."
    if pennysexxmas:
        mct "And... thanks to the crazy little secret romp I had with Penny, I even got drained of every last drop of testosterone I had left in me."
    else:
        mct "I don't even feel any urges at all."
    mct "Not hungry, not thirsty, not horny — just... at peace."
    play sound stairswood2
    scene qpp 57
    d "*Shivering* H-Holy fuck, it's s-so cold out here!" with dis15
    play sound water4c
    scene qpp 58
    mc "*Turning around* Of course it is! It's..." with dis12
    mc ". . ."
    $ unlock_look("dalia", 15)
    mct "...Okay, I might have underestimated the effect these women have on me."
    mct "So much for “not horny”..."
    mc "*Clears throat* Um... that's a nice bikini, Dal."
    scene qpp 59
    d "*Shivers* W-What's the temperature now??"
    show qpp 58
    mc "Uh... I think it was like 34 degrees when I came out. {i}American{/i} degrees."
    mc "But don’t just stand there freezing! Get in here!"
    mc "The water's steaming hot!"
    play sound2 chair2 
    play sound3 water
    scene qpp 60 with dis15
    d "*Sitting on the edge* Oooohhh..." with dis12
    d "You weren't kidding... it's burning!"
    scene qpp 61
    mct "Damn... did Dalia put on some extra muscle?"
    mct "She looks better than ever."
    mct "It's crazy she doesn't gain an ounce of fat while eating for three people."
    if daliapath:
        play soundlow wood2 volume 0.4
        play sound6 water 
        play sound2 ["<silence 0.2>", water4c]
        scene qpp 62
        d "AAaaaah! It's so niiiiiceee..." with dis15
        d "Even just dipping your legs takes the cold right out of you!"
        mc ". . ."
    play sound water2
    play sound2 jumpscare3b volume 0.5
    play sound3 whoosh6
    scene qpp62
    xsc "[mc!u]!" with hpunch 
    $ unlock_look("alex", 10)
    scene qpp 64
    mc "G-Gahh! G-Goddammit Alex, you and your jumpscares!" with hpunch 
    scene qpp 65
    x "*Gasping dramatically* What a perv!"
    if daliapath:
        x "*Whispering* You get excited too fast, [mc]..."
        scene qpp 63
        x "*Whispering* Though... something tells me that's exactly the reaction Dalia was hoping for."
        show qpp 64
        mc "*Crossing your legs* I-I don’t know what you’re talking about."
    else:
        x "Did you get hard just staring at Dalia?"
        show qpp 64
        mc "What?! No, I didn't!"
    show qpp 65
    x "*Snorts* Oh... really?"
    show qpp 63
    x "Must've been an optical illusion, then. A trick of the ripples in the water."
    show qpp 64
    if daliapath:
        mc "Mm-hm. Exactly."
    else:
        mc "Naturally!"
    play sound water5
    play sound6 splash2
    scene qpp 67
    x "*Jumping into the pool* Ohh... damn, you weren't lying though!" with dis17
    x "The water's hot!"
    play sound2 water4c
    scene qpp 66
    x "Although... I’d say it’s not the hottest thing in this pool right now." with dis15
    d "*Chuckles* I suppose you're talking about yourself."
    x "Hah! Don’t give me that fake modesty, girl."
    x "Now come over here and show me how that bikini looks on that cake of yours..."
    play sound3 wood2 volume 0.4
    play sound4 water4c
    scene qpp 68
    mc "*Leaning back* (Oh Lord, give me strength...)" with dis15
    mct "It’s gonna be tough to sit here the whole time without looking like some middle schooler who just saw his first tit."
    play sound stairswood2
    scene qpp 69
    n "Wow! Look at the moon! It's so bright tonight!" with dis12
    scene qpp 70
    mct "Oh boy..." with dis
    $ unlock_look("nancy", 14)
    $ unlock_look("penelope", 18)
    mct "When it rains, it pours, as they say..."
    n "And with all the snow, the mountain almost looks like it's glowing!"
    p "*Shivering* W-What the hell, Mom, how are you not freezing your ass off?"
    n "Oh, are you guys? I don't know, I've always been hot-blooded."
    d "Quit talking and get in here already!"
    x "Yeah, the water’s boiling!"
    p "*Shivering* Y-Yes, please, before I turn into an icicle."
    play sound water5
    play sound2 water3
    scene qpp 71 with dis17
    p "O-Ooohhh..." with dis14
    play sound3 water3
    play sound4 water4c
    play soundlow ["<silence 0.4>", owl] volume 0.5
    scene qpp 72
    p "OoooOoOOoohhh..." with dis15
    p "Nooooww we're talking..."
    play sound3 water
    play sound4 water4c
    scene qpp 74
    n "*Sitting down* Mmmmhhhrr..." with dis15
    scene qpp 73
    n "God, it feels so good..."
    n "All that muscle and joint soreness just melts away."
    n "And with how cold it is outside, it makes this even better."
    if pennycreampie and pregnancy:
        show qpp 72
        p "I'm so happy my period hasn't come yet."
        p "I forgot to bring tampons, and missing out on this would’ve sucked."
        show qpp 75
        n "Your period hasn't come yet?"
        n "I thought you were supposed to get it last week."
        show qpp 75b
        mct "Wait... what...?"
        show qpp 76
        p "Yeah, but after all the stress with [mc] going missing last week, I guess my body decided to hit pause."
        mct "Oh, I see..."
        p "It's not the first time, the same thing already happened to me during finals last year."
        if alexpath:
            scene qpp 77
            x "Funny. Mine’s a bit late too, actually."
            x "Maybe we’ve all been spending too much time together, and our cycles started syncing up."
            show qpp 78
            p "It's true, they say that can happen!"
            p "*Giggles* I hope you know how to survive multiple hormone waterfalls at once, [mc]."
            show qpp 75b
            mc "*Chuckles* I think I’ll just crash at Chang’s place when it hits, thank you."
            p "*Laughs* Don't you dare!"
        show qpp 75
        n "Yeah... that could very well be."
        n "Although... there's also another possible explanation."
        n "If you've been... you know."
        show qpp 79
        p "What?! Mom!"
        show qpp 81
        n "Oh come on, Penelope."
        n "You're not a little girl anymore. Sex is natural."
        show qpp 80
        p "I-I know it's natural."
        p "A-And I know how it works, I'm not stupid."
        show qpp 81
        n "I know you do, but don’t underestimate how easy it is for a girl your age to get pregnant, even during the least fertile days."
        n "Believe me, I know. You and Dalia are my everything, but I sure as hell wasn’t planning on being a mom at eighteen."
        show qpp 83
        d "Yeah, sis, we're just wondering if you've let some guy creampie you."
        d "No judgment, really."
        if alexpath:
            show qpp 80
            p "W-Why am I the only one getting interrogated like this?"
            p "A-Alex just said she's late too!"
            show qpp 82
            n "Well, because you're my daughter."
            n "I wouldn't dare to snoop into Alex's life."
            x ". . ."
        show qpp 80
        p "O-Okay, okay, enough."
        p "I'm not pregnant. I'd... I'd know."
        p "I'll... I-I've used protection. And the timing doesn't even line up, like, at all! It's impossible."
        show qpp 80b
        mct "We definitely didn't use protection..."
        mct "But if the timings don't line up, it shouldn't matter."
        if alexpath:
            scene qpp 82
        mct "...I think."
        mct "I'm certainly no expert."
        show qpp 80
        p "*Clears throat* Anyway!"
        p "Can we start playing that game now? It's getting pretty late."
        play sound water
        show qpp 84
        n "Oh, true!" with dis12
    else:
        show qpp 77
        x "That game you brought is Chang's, right?"
        play sound water
        show qpp 84
        n "It is!" with dis12
    play sound3 water4c
    play sound2 paper3
    scene qpp 85
    n "*Opens the box* Oh wow, look at this." with dis15
    n "Even the instructions are laminated! That boy thinks of everything."
    show qpp 87
    mc "*Chuckles* Yeah, he really is the best."
    show qpp 85
    n "Let's see..."
    n "{i}Thank you for purchasing a genuine Changermeister, First Edition! The one and only card game designed to crown the ultimate legend of the night!"
    n "{i}Prove to everyone that you’re the smartest, the strongest, the hottest, the bravest, the kinkiest, and the luckiest soul in the room!"
    n "{i}Truths, dares, charades, trivia, and chaos. Survive them all, and crown yourself as the “Chang”!"
    show qpp 86
    mc "*Laughs* Sounds good already."
    play soundlow ["<silence 0.7>", owl] volume 0.5
    show qpp 85
    n "{i}The rules are simple."
    n "{i}Shuffle the deck and draw two cards. Read both titles out loud and let the person on your right choose which one the whole group will go with."
    n "{i}Each card falls into one of five possible categories — Group Clash, Battle Royale, Bonus, Duel, or Team Building. Whatever it says, you've gotta do it!"
    n "{i}Most challenges are worth 100 points — some are simpler, some are harder, and some come with deliciously evil twists!"
    n "{i}The youngest player starts, and then it goes clockwise around the table!"
    show qpp 77
    x "Well, Dalia’s January, I’m March... so that makes [mc] the baby of the group."
    show qpp 86
    mc "Nice. Getting a head start already."
    show qpp 85
    n "{i}You’ll play exactly fifteen rounds. But beware, the final card is worth triple points and can flip the whole game upside down!"
    n "{i}Grab some drinks, remember to drink after each round, and decide a prize for the winner before starting!"
    n "{i}Good luck and don't let yourself get Chang'd!"
    show qpp 90
    d "That sounds fun! I like it already."
    show qpp 88
    p "A prize for the winner..."
    p "What should we go with?"
    p "It's not like we can bet any money on it, we're all broke as hell."
    show qpp 77
    x "How about... the winner gets dibs on the sauna?"
    show qpp 89b
    mc "Wait, there's a sauna?!"
    x "Yeah! In the basement."
    mc "Damn, I didn't know!"
    show qpp 89
    p "Aaahh, that's actually a great idea!"
    p "It’s late, we’ve gotta wake up early tomorrow, and there’s no way we can all use it at once."
    show qpp 90
    d "It's settled, then!"
    d "The winner gets to use the sauna before bed!"
    show qpp 91
    mc "Sounds good to me!"
    mc "Nancy, toss me a beer, please. I’m initiating my pro-gamer mode."
    play sound water4c
    scene qpp 92
    mc "If I'm being honest, I didn't even know there was a sauna, so I wasn't looking forward to using it." with dis12
    mc "I’d almost say screw it and just let one of you have it, but... there’s just one tiny little problem..."
    $ renpy.music.set_volume(0.15, delay=5.0, channel='soundloop3')
    play music ["<silence 1.6>"]
    queue music changer1
    play sound2 openbeer
    play sound openbeer
    show screen ep9_pts_overlay
    mc "*Opening the beer* ...I never lose." with dis12
    show qpp 92b
    n "We'll see about that, big boy."
    n "Dalia looks like she’s out for blood."
    play sound water3
    scene qpp 93
    d "*Drawing two cards* Damn right I am." with dis12
    d "I don't care what this game throws at me — I'm winning this thing."
    show qpp 94
    mc "The rules themselves said luck is a big part of the game, Daly."with dis08
    mc "Are you not worried about that?"
    show qpp 93
    d "Nahh... I'm feeling lucky tonight."with dis08
    d "You might need that luck, though, so you better choose wisely."
    d "Your two categories are... "
    d "“Booty Royale” or... “Chest Day”."
    d "Hah!"
    show qpp 94
    mc "Hmm..."with dis08
    if daliapath and alexpath:
        mod "Save here if you want to explore the game. Get to a coin choice for a scene (don't get too 
        many or too little points vs Dalia)."
    else:
        mod "Save here if you want to explore the game."
    play sound whoosh9
    call screen card_selection(cards=cmcards1)

label cm1:
    $ buttcm = True
    play sound ding volume 0.75
    mc "Booty Royale definitely sounds enticing." with dis
    scene qpp 93
    d "Alright then... Booty Royale it is."with dis08
    d "Let's see..."
    d "{i}Group Clash! Best butt in the group scores the 100 points!"
    d "Hah! Just like that?!"
    d "Pfft, this game's too easy!"
    scene qpp 95
    p "What do you mean, easy?"
    p "Are you just assuming you’ve got the best ass here?"
    scene qpp 96
    d "Uh... well... yeah?"
    scene qpp 95
    p "You're not the only one here who goes to the gym, you know?"
    p "Literally all five of us work out."
    scene qpp 96
    d "But I'm the only one who practically lives there."
    d "I haven't been training glutes and legs four days a week for the last three years to lose a best-butt contest."
    show qpp 95
    p "Eh, I don't know, Dal..."
    p "We'd need to compare to be sure."
    scene qpp 96
    d "Hmph! Fine!"
    play sound2 water3
    play sound3 bubbles
    play sound drips
    scene qpp 97 
    bla "Dalia shoots up like a jungle cat." with dis12
    mct "Sweet merciful God..."
    x "*Laughs* What do you say, [mc]?"
    x "Winner material, or not?"
    mc "Y-Yeah, definitely winner material..."
    play sound3 splash3
    play sound4 water
    scene qpp 96
    d "*Sitting down* Alright then. Your turn, sis." with dis12
    play sound coins1
    $ daliapointscm += 100
    show qpp 95
    p "Nah... I'm good, thanks." with dis08
    p "You're the rightful champion of this round, sissy."
    p "Honestly, I just wanted to give you a chance to show off."
    p "Figured you needed it."
    show qpp 98b
    d ". . ."
    show qpp 98
    d "I hate you, you know?"
    scene qpp 95
    p "Aaaand Dalia takes the lead!"
    p "Round two!"
    jump cmround2
label cm2:
    play sound ding volume 0.75
    mc "Chest Day's the best day." with dis
    scene qpp 93
    d "Alright then... Chest Day it is."with dis08
    d "Let's see..."
    d "{i}Group Clash! Best boobs in the group score 100 points!"
    scene qpp 95
    p "Hah! Nice!"
    scene qpp 100
    d "Wait, what?! That's it?!"
    d "Just... tits? Just like that?!"
    d "This is so unfair!"
    show qpp 95
    p "Don't be mad, sis."
    p "I'm sure you'll get luckier next round."
    show qpp 96
    d "You’re acting pretty smug for someone who hasn’t won the round either, Penny."
    show qpp 101
    p "Uh... I'm sorry? Did I mishear the question?"
    show qpp 96
    d "Mom’s boobs are bigger than yours."
    show qpp 101
    p "Uh, excuse me? Since when?"
    show qpp 102
    n "*Chuckles* Thank you, sweetheart, but I’m fairly sure Penny’s got this one."
    n "We’re almost the same size, but her cup is just a little bigger."
    n "I’m... sure [mc] will back me up here."
    play sound2 water3
    play sound drips
    scene qpp 103
    p "*Standing up* Yeah, that's a great idea, let's ask him!" with dis12
    p "Who's got the bigger pair, [mc]?"
    show qpp 104
    mc "*Staring at Penny's chest* U-Um..."
    menu:
        with dis  
        "Penelope":
            mc "Uhh... well, from what I can see, you both look pretty close, but..."with dis
            mc "I'm gonna agree with Nancy and vote Penny this time."
            play sound coins1
            $ penelopepointscm += 100
            scene qpp 105
            p "See??"with dis08
            p "Thank you for your very... scientific, articulate observation, [mc]."
            p "Much appreciated."
            scene qpp 96
            d "Fine, fine..."
            d "Penny takes the lead..."
            d "But this is just the beginning! Round two!"
        "Nancy":
            mc "Uhh... well, you both have... impressive assets, but if I had so say..."with dis
            mc "And just from external observation..."
            mc "I'd say Nancy's are a little bit bigger, maybe."
            play sound coins1
            $ nancypointscm += 100
            scene qpp 106
            p "*Gasps dramatically* AAAAAH." with dis 
            p "Betrayal..."
            scene qpp 107
            p "I will remember this treason, [mc]." with dissolve
            scene qpp 90
            d "Alright then! Mom takes the lead!"
            d "Let's move to round two!"
    jump cmround2
label cmround2:
    play sound water4c
    $ cmround += 1
    scene qpp 108
    mc "Alright, so... if I'm not mistaken, it's Nancy's turn now!" with dis14
    mc "Your two options are..."
    mc "“Turbo Round” or... “Grammy Awards”!"
    scene qpp 102
    n "Interesting..."
    n "How about... Turbo Round."
    scene qpp 108
    mc "Turbo Round for Nancy it is! Now let's see what you got..."
    mc "{i}Bonus card! The person reading the card gets 10 points, you score 100 points, and the next card’s worth double!"
    play sound coins1
    $ nancypointscm += 100
    $ mcpointscm += 10
    show qpp 109
    mc "Damn! This one was a freebie!" with dis08
    mc "I want to have that kind of luck too."
    scene qpp 102
    n "Tsk, tsk, luck’s got nothing to do with it, [mc]."
    n "It’s all about reading the entendre beneath the card titles."
    show qpp 123
    if not buttcm:
        x "Yeah, [mc]. Either you’ve gotta have big boobs, or you’ve gotta figure out the mind games behind the card names."
    else:
        x "Yeah, [mc]. Either you’ve gotta have a big butt, or you’ve gotta figure out the mind games behind the card names."
    x "Step up your game, man."
    show qpp 124
    mc "*Laughs* I see, I see."
    mc "Alright, that's it. I'm getting serious now."
    play sound water4c
    $ cmround += 1
    scene qpp 110
    n "Now let’s see if Penny can pull a lucky one..." with dis14
    n "You have... “Leap of Faith” or... “Lore Lore Land”."
    scene qpp 115
    p "Let's go with Lore Lore Land! It sounds fun."
    scene qpp 110
    n "Alright then..."
    n "{i}Battle Royale! Each player has to name a server in Eternum every ten seconds, one by one, clockwise. If you choke or repeat one, you’re out!"
    play sound water3
    scene qpp 113
    d "Yes!" with hpunchsubtle
    scene qpp 112
    p "Oof... I don’t know that many, honestly. I haven’t been playing long enough to memorize them all."
    show qpp 111
    n "Yeah... same. I mostly just remember the names of the ones we’ve been hopping around lately."
    scene qpp 113
    d "Come on, come on, let's begin! No prep time allowed!"
    d "Penny, you're up first!"
    scene qpp 114
    p "Alright then... uhh..."
    scene qpp 112
    p "Can I say Hyril'ar?"
    p "Does that count?"
    show qpp 111
    n "Well... yeah, I'd say so. At this point the line between “servers” and “other worlds” is more than blurred anyway."
    show qpp 115
    p "Cool. Then my pick's Hyril'ar."
    # Note to translators: Keep these server names fully lowercase when you
    # translate them, otherwise you'll break the minigame.
    $ serverscm = [
        _("atlantis"), _("hyril'ar"), _("ekabar"), _("tumbleweed"), _("andromeda"),
        _("warthogs"), _("meiyo"), _("ion"), _("valley of kings"), _("the red herring"),
        _("plains of denaria"), _("xala's moon"), _("plains of saturn"), _("mikaar"),
        _("styx"), _("ogygia"), _("agora"), _("sin city"), _("rockefeller"),
        _("new vegas"), _("yggdrasil"), _("semper invicta"), _("the cove"),
        _("kink paradise"), _("the new world"), _("frontier trails"), _("cyrodiil"),
    ]    
    $ used_servers = set()
    $ used_servers.add(_("hyril'ar"))
    play sound5 w2 volume 0.5
    show qpp 117
    x "The New World."with pl
    $ used_servers.add(_("the new world"))
    play sound5 w2 volume 0.5
    show qpp 119
    d "Ekabar!"with pl
    $ used_servers.add(_("ekabar"))
    play sound5 w2 volume 0.5
    show qpp 120
    mc "Hmmm..."with pl
    $ serverguess = reverse_translate_server_name(renpy.input(_("Type an Eternum server:"), exclude='\\[]{').strip().lower())
    if serverguess in serverscm and serverguess not in used_servers:
        $ used_servers.add(serverguess)
        scene qpp 121
        mc "[string.capwords(renpy.translate_string(serverguess))]." with dissolve
    elif serverguess in used_servers:
        show qpp 121
        mc "[string.capwords(renpy.translate_string(serverguess))]!" with dissolve
        scene qpp 123
        x "*Snorts* What? We already said that!"
        x "You're out!"
        show qpp 122
        mc "Agh, crap, did you?? I was too focused trying to think of my own answer..."
        $ mceliminatedservers = True
    elif serverguess == "":
        mc "Hmm..."
        show qpp 119
        d "Time! Too slow!"
        show qpp 122
        mc "Agh, dammit! Ten seconds is not enough!"
        $ mceliminatedservers = True
    else:
        scene qpp 122
        mc "[string.capwords(serverguess)]?" with dissolve
        scene qpp 123
        x "*Snorts* What? That's not a server."
        x "Eliminated!"
        scene qpp 122
        mc "Agh, dammit!"
        $ mceliminatedservers = True
    play sound5 w2 volume 0.5
    scene qpp 111
    if _("semper invicta") in used_servers:
        n "Um... Sin City."with pl
        $ used_servers.add(_("sin city"))
    else:
        n "Semper Invicta."with pl
        $ used_servers.add(_("semper invicta"))
    play sound5 w2 volume 0.5
    if _("warthogs") in used_servers:
        scene qpp 114
        p "Uhh..."with pl
        p "Damn..."
        scene qpp 115
        p "Oh, the heist one!" with dissolve
        p "New Vegas!"
        $ used_servers.add(_("new vegas"))
    else:
        scene qpp 115
        p "Warthogs!" with pl
        $ used_servers.add(_("warthogs"))
    play sound5 w2 volume 0.5
    scene qpp 116
    x "Mmmh..."with pl
    scene qpp 117
    if _("andromeda") in used_servers:
        x "Agora?" with dissolve
        $ used_servers.add(_("agora"))
    else:
        x "Andromeda?" with dissolve
        x "No one has said it yet, right?"
        $ used_servers.add(_("andromeda"))
    play sound5 w2 volume 0.5
    scene qpp 119
    if _("valley of kings") in used_servers:
        d "Rockefeller!" with pl
        $ used_servers.add(_("rockefeller"))
    else:
        d "Valley of Kings!" with pl
        $ used_servers.add(_("valley of kings"))
    if not mceliminatedservers:
        play sound5 w2 volume 0.5
        show qpp 120
        mc "Hmmm..."with pl
        $ serverguess = reverse_translate_server_name(renpy.input(_("Type an Eternum server:"), exclude='\\[]{').strip().lower())
        if serverguess in serverscm and serverguess not in used_servers:
            $ used_servers.add(serverguess)
            scene qpp 121
            mc "[string.capwords(renpy.translate_string(serverguess))]." with dissolve
        elif serverguess in used_servers:
            show qpp 121
            mc "[string.capwords(renpy.translate_string(serverguess))]!" with dissolve
            scene qpp 123
            x "*Snorts* What? We already said that!"
            x "You're out!"
            show qpp 122
            mc "Agh, crap, did you?? I was too focused trying to think of my own answer..."
            $ mceliminatedservers = True
        elif serverguess == "":
            mc "Hmm..."
            show qpp 119
            d "Time! Too slow!"
            show qpp 122
            mc "Agh, dammit! Ten seconds is not enough!"
            $ mceliminatedservers = True
        else:
            scene qpp 122
            mc "[string.capwords(serverguess)]?" with dissolve
            scene qpp 123
            x "*Snorts* What? That's not a server."
            x "Eliminated!"
            scene qpp 122
            mc "Agh, dammit!"
            $ mceliminatedservers = True
    play sound5 w2 volume 0.5
    scene qpp 111
    n "Um..."with pl
    n "How about..."
    n "Erm..."
    scene qpp 119
    d "Time!"
    d "Eliminated, Mom!"
    play sound5 w2 volume 0.5
    scene qpp 114
    p "Um..."with pl
    scene qpp 115
    if _("meiyo") in used_servers:
        $ randomserverguess = renpy.random.choice([w for w in serverscm if w not in used_servers])
        scene qpp 112
        p "Uhh... [string.capwords(renpy.translate_string(randomserverguess))]?" with dissolve
        $ used_servers.add(randomserverguess)
        p "There's one called like that, right?"
    else:
        p "Ah, Meiyo, of course!" with dissolve
        $ used_servers.add(_("meiyo"))
    play sound5 w2 volume 0.5
    scene qpp 116
    x "Mmmhh..."with pl
    $ randomserverguess = renpy.random.choice([w for w in serverscm if w not in used_servers])
    scene qpp 117
    x "Uhh... [string.capwords(renpy.translate_string(randomserverguess))]?" with dissolve
    $ used_servers.add(randomserverguess)
    play sound5 w2 volume 0.5
    scene qpp 118
    d "Uhh, that's a good one..."with pl
    d "It's starting to get tough..."
    scene qpp 119
    $ randomserverguess = renpy.random.choice([w for w in serverscm if w not in used_servers])
    d "O-Oh, oh! [string.capwords(renpy.translate_string(randomserverguess))]!" with dissolve 
    $ used_servers.add(randomserverguess)
    if not mceliminatedservers:
        play sound5 w2 volume 0.5
        show qpp 120
        mc "Hmmm..."with pl
        x "Tick tock, [mc]!"
        $ serverguess = reverse_translate_server_name(renpy.input(_("Type an Eternum server:"), exclude='\\[]{').strip().lower())
        if serverguess in serverscm and serverguess not in used_servers:
            $ used_servers.add(serverguess)
            scene qpp 121
            mc "[string.capwords(renpy.translate_string(serverguess))]." with dissolve
        elif serverguess in used_servers:
            show qpp 121
            mc "[string.capwords(renpy.translate_string(serverguess))]!" with dissolve
            scene qpp 123
            x "Nope! We already said that!"
            x "You're out!"
            show qpp 122
            mc "Agh, crap, did you?? I was too focused trying to think of my own answer..."
            $ mceliminatedservers = True
        elif serverguess == "":
            mc "Hmm..."
            show qpp 119
            d "Time! Too slow!"
            show qpp 122
            mc "Agh, dammit! Ten seconds is not enough!"
            $ mceliminatedservers = True
        else:
            scene qpp 122
            mc "[string.capwords(serverguess)]?" with dissolve
            scene qpp 123
            x "*Snorts* What? That's not a server."
            x "Eliminated!"
            scene qpp 122
            mc "Agh, dammit!"
            $ mceliminatedservers = True
    play sound5 w2 volume 0.5
    scene qpp 114
    p "Uhh..."with pl
    p "Aghh... what was the name of that one where I fought Nevrons with Luna..."
    show qpp 113
    d "Time's up! One less!"
    play sound5 w2 volume 0.5
    scene qpp 116
    x "Mmmhh..."with pl
    $ randomserverguess = renpy.random.choice([w for w in serverscm if w not in used_servers])
    scene qpp 117
    x "Oh... [string.capwords(renpy.translate_string(randomserverguess))]." with dissolve
    $ used_servers.add(randomserverguess)
    play sound5 w2 volume 0.5
    scene qpp 118
    d "Uhhh... you guys are good..."with pl
    scene qpp 119
    $ randomserverguess = renpy.random.choice([w for w in serverscm if w not in used_servers])
    d "Ah, but of course! [string.capwords(renpy.translate_string(randomserverguess))]!" with dissolve 
    $ used_servers.add(randomserverguess)
    if not mceliminatedservers:
        play sound5 w2 volume 0.5
        show qpp 120
        mc "Hmmm..."with pl
        mct "Damn, this is getting so hard..."
        d "Five seconds!"
        $ serverguess = reverse_translate_server_name(renpy.input(_("Type an Eternum server:"), exclude='\\[]{').strip().lower())
        if serverguess in serverscm and serverguess not in used_servers:
            $ used_servers.add(serverguess)
            scene qpp 121
            mc "[string.capwords(renpy.translate_string(serverguess))]." with dissolve
        elif serverguess in used_servers:
            show qpp 121
            mc "[string.capwords(renpy.translate_string(serverguess))]!" with dissolve
            scene qpp 123
            x "Nope! We already said that!"
            x "You're out!"
            show qpp 122
            mc "Agh, crap, did you?? I was too focused trying to think of my own answer..."
            $ mceliminatedservers = True
        elif serverguess == "":
            mc "Hmm..."
            show qpp 119
            d "Time! Too slow!"
            show qpp 122
            mc "Agh, dammit! Ten seconds is not enough!"
            $ mceliminatedservers = True
        else:
            scene qpp 122
            mc "[string.capwords(serverguess)]?" with dissolve
            scene qpp 123
            x "*Snorts* What? That's not a server."
            x "Eliminated!"
            scene qpp 122
            mc "Agh, dammit!"
            $ mceliminatedservers = True
    play sound5 w2 volume 0.5
    scene qpp 116
    x "Mhh..."with pl
    x "Mmmhhhh..."
    x "Hhhhmmmmmm..."
    n "Time!" with hpunchsubtle
    show qpp 117
    x "Agh, fuck. I went blank."with dissolve 
    if mceliminatedservers:
        jump cmround3daliawins
    play sound5 w2 volume 0.5
    scene qpp 118
    d "Damn, this is getting brutal..."with pl
    d "But... uhh..."
    scene qpp 119
    $ randomserverguess = renpy.random.choice([w for w in serverscm if w not in used_servers])
    d "OHH! [string.capwords(renpy.translate_string(randomserverguess))]! How could I forget!" with dissolve
    $ used_servers.add(randomserverguess)
    if not mceliminatedservers:
        play sound5 w2 volume 0.5
        show qpp 120
        mc "Hmmm..."with pl
        d "Five seconds, [mc]!"
        mc "Hmm..."
        d "Four..."
        d "Three..."
        $ serverguess = reverse_translate_server_name(renpy.input(_("Type an Eternum server:"), exclude='\\[]{').strip().lower())
        if serverguess in serverscm and serverguess not in used_servers:
            $ used_servers.add(serverguess)
            scene qpp 121
            mc "[string.capwords(renpy.translate_string(serverguess))]." with dissolve
        elif serverguess in used_servers:
            show qpp 121
            mc "[string.capwords(renpy.translate_string(serverguess))]!" with dissolve
            scene qpp 123
            x "BZZZT! We already said that!"
            x "You're out!"
            show qpp 122
            mc "Agh, crap, did you?? I was too focused trying to think of my own answer..."
            $ mceliminatedservers = True
        elif serverguess == "":
            mc "Hmm..."
            show qpp 119
            d "Time! Too slow!"
            show qpp 122
            mc "Agh, dammit! Ten seconds is not enough!"
            $ mceliminatedservers = True
        else:
            scene qpp 122
            mc "[string.capwords(serverguess)]?" with dissolve
            scene qpp 123
            x "*Snorts* What? That's not a server."
            x "Eliminated!"
            scene qpp 122
            mc "Agh, dammit!"
            $ mceliminatedservers = True
    if mceliminatedservers:
        jump cmround3daliawins
    play sound5 w2 volume 0.5
    scene qpp 118
    d "Holy shit, [mc], you've got the memory of an elephant..."with pl
    d "Uhh..."
    d "The Valleys of..."
    d "Erm..."
    scene qpp 123
    x "Time's up!" with hpunch 
    x "[mc]'s the winner of the double points round!"
    play sound2 water4c
    play sound coins1
    $ mcpointscm += 200
    scene qpp 125
    d "AAAAAAghh... fuck!" with dis12
    $ randomserverguess = renpy.random.choice([w for w in serverscm if w not in used_servers])
    $ used_servers.add(randomserverguess)
    d "[string.capwords(renpy.translate_string(randomserverguess))]!" with hpunchsubtle
    $ randomserverguess = renpy.random.choice([w for w in serverscm if w not in used_servers])
    d "[randomserverguess!tu]!"with hpunch
    d "Gaaaaaahhgh, why didn't I think of these faster?!"
    d "*Muttering* Stupid brain..."
    jump cmround4
label cmround3daliawins:
    play sound2 water4c
    play sound coins1
    $ daliapointscm += 200
    scene qpp 113
    d "YES!" with dis12
    d "I win! Last one standing!"
    scene qpp 123
    x "And it was a double points round too."
    x "Nice job, you clever cookie."
    scene qpp 113
    d "Hehe... I like this game."
label cmround4:
    play sound water4c
    $ cmround += 1
    scene qpp 126
    p "Alright, alright... this is getting interesting!" with dis14 
    p "Alex!"
    p "“Jumping Jack” or “Voicegasm”?"
    scene qpp 77b
    x "Mmmmmh... let's go with... Voicegasm."
    scene qpp 126
    p "And Voicegasm says..."
    p "{i}Group Clash! The one who can make the sexiest voice scores the 100 points!"
    scene qpp 77b
    x "Hah!"
    x "Well, that should be easy to agree on."
    scene qpp 127
    p "*Giggles* Indeed."
    p "As much as I love Alex’s voice, I’ve gotta vote for someone else."
    scene qpp 128
    p "Congrats on the hundred points, Mom."
    scene qpp 129
    n "Oh come on, don't be ridiculous."
    scene qpp 130
    d "She's right, Mom!"
    d "Everyone says so!"
    mc "Yep, clear winner, Nancy!"
    scene qpp 128
    p "See? We all agree."
    p "Come on! Say something in your sexy voice!"
    scene qpp 129
    n "Oh, please, don’t make me embarrass myself."
    show qpp 130
    p "We're the ones who want to hear it!"
    d "*Chuckles* Yeah! Please, Mom!"
    scene qpp 129
    n "But I don't even have a “sexy voice”."
    show qpp 130
    p "Yes, you do! Pleeeeeaaaaaseeeeeee!"
    d "Please, please, please, please, please!"
    show qpp 129
    n "*Giggles* You're all so silly."
    n "Fine, fine... okay, let me try."
    play sound water4c
    scene qpp 131
    n "*Clears throat* Mm-hm-hmm." with dis12
    n ". . ."
    scene qpp 132
    n "{cps=13}{bt=5}*{size=31}M{size=33}o{size=35}a{size=37}n{size=39}s{size=41}* {size=43}W{size=45}i{size=47}l{size=49}l{size=51} y{size=53}o{size=55}u{size=57}.{size=59}.{size=61}. {/bt}{cps=7}{bt=5}{size=63}m{size=65}a{size=67}k{size=69}e{size=71} m{size=73}e{size=75}.{size=77}.{size=79}. {/bt}{cps=5}{bt=5}{size=81}b{size=83}e{size=85}g{size=87}.{size=89}.{size=91}.{size=93}?"with dis15
    scene qpp 131
    mct "H-Holy fuck... that just gave me a hard-on." with dis12
    scene qpp 133
    p ". . ."
    scene qpp 134
    d ". . ."
    scene qpp 135
    x "OH. MY. GOD, Nancy."
    x "That turned ME on, and I thought I liked guys!"
    play sound coins1
    $ nancypointscm += 100
    play sound2 water4c
    scene qpp 129
    n "Please, like I said, it's no big deal." with dis12
    scene qpp 135
    x "*Snickers* Are you okay, Dal?"
    show qpp 134
    d ". . ."
    scene qpp 136
    d "U-Um... y-yeah, I just..." with dis08
    d "I-I just wasn't expecting to hear my mom say that in {i}that{/i}... tone today."
    d "B-But let's keep going!"
    d "I choose now, right?!"
    $ cmround += 1
    play sound3 water4c
    scene qpp 137
    x "*Drawing two cards* Yup!" with dis14
    x "And you got..."
    x "*Snorts* Okay, just from the titles I already know which one you’re gonna pick."
    x "“Cum Laude” or “Core Crush”?"
    scene qpp 90b
    d "Oh, easy!"
    d "Core Crush ALL DAY!"
    scene qpp 137
    x "*Laughs* Yeah, figured as much."
    x "Let's see..."
    x "{i}Group Clash! Juiciest abs in the group score 100 points!"
    play sound water4c
    scene qpp 113
    d "Yes! Just as I was hoping!" with dis
    d "I got this one!"
    show qpp 95
    p "Ehh... I don't know, Dal... [mc] has some pretty {i}juicy{/i} abs too, if you ask me."
    scene qpp 121
    mc "Well, if we're talking pure... {i}juiciness{/i}, I've gotta give it to Dalia, in all fairness."
    show qpp 119
    d "Thank you, [mc]!"
    show qpp 123
    x "Can’t argue with that. Her six-pack got even sharper the past few weeks."
    x "We all handled the stress in our own ways while you were missing, and Dalia basically did a million crunches a day to burn it off."
    show qpp 90b
    d "Nahh... it wasn't a million."
    d "Two, maybe three thousand a day, tops."
    show qpp 95
    p "You'll have to show us some evidence, sis."
    p "We made Mom do the sexy voice too, so it’s only fair."
    scene qpp 96
    if buttcm:
        d "You already had me parading around with the butt card like a circus monkey!"
    else:
        d "What you want is for me to parade around like a circus monkey!"
    d "You just want to embarrass me!"
    show qpp 95
    p "Nothing further from reality, sis."
    p "Someday you'll understand..."
    show qpp 96
    d "What??"
    show qpp 95
    p "I said... no evidence, no points!"
    show qpp 96
    d "Agh, FIIIINE! Whatever!"
    d "If you think I’m backing out because I’m gonna feel shy, you’ve got another thing coming!"
    play sound water3
    play sound2 drips
    scene qpp 138 with dis17
    bla "Dalia leans back on the edge of the pool, lifting her hips just enough to show off her abs above the water." with dis15
    mct "Sweet Jesus..."
    x "Daaaaaaamn, girl!"
    mct "Look at that tummy..."
    mct "Those abs could cut glass."
    scene qpp 139
    p "*Giggles* Careful, sis." with dis14
    p "If you keep flexing that hard, you’re gonna pass out."
    d "*Obviously flexing* I-I'm n-not flexing."
    d "Th-This is m-my natural... r-resting state."
    p "*Laughs* Ohhh, really? Impressive, then!"
    scene qpp 138
    mc "So... everyone agrees Dalia's juicy abs take the round, then?" with dis14
    p "Yep!"
    n "No doubt!"
    x "Hands down!"
    $ daliapointscm += 100
    $ cmround += 1
    play sound7 coins1
    play sound3 splash3
    play sound4 water
    scene qpp 140
    d "T-Thank you." with dis12
    d "I appreciate your... sportsmanship."
    show qpp 141
    d "B-But let's move on to [mc]'s turn!" with dis08
    d "Let's see... your new options are... "
    d "“Fresh Meat” or... “Kiss or Miss”."
    show qpp 141b
    mc "Hmm..." with dis06
    play sound whoosh9
    call screen card_selection(cards=cmcards2) 
label cm3:
    play sound ding volume 0.75
    mc "Let's go with Fresh Meat." with dis
    scene qpp 141
    d "Very well..."
    d "{i}Battle Royale! Whoever strips off their bra or underwear first gets a hundred points!"
    scene qpp 142
    d "Oh... w-wow. That escalated quickly." with dis08
    d "I suppose the game didn't expect us to be all in swimsuits."
    show qpp 143
    mc "Well, that doesn’t mean you can’t still play along, though..."
    scene qpp 140
    d "Yeah, you'd sure like that."
    show qpp 135
    x "So... any bold volunteer?"
    scene qpp 140
    d "Of course not!"
    scene qpp 95
    p "You know what?"
    p "I'll do it."
    play sound water
    scene qpp 151
    d "W-Wait, WHAT?!" with dis 
    d "Are you serious? Now? Here?! In front of everyone?!"
    play sound2 water4c
    scene qpp 150
    p "Yeah! Why not?" with dis 
    p "Half of the people here have already seen me naked a hundred times, and the rest... well, we’re just having fun. Who cares?"
    p "Unless... you’d like to go first, Dal, of course."
    p "I don’t mind giving you a head start."
    scene qpp 146b
    d "N-No, thanks."
    d "I don't..."
    d "Y-You can take this one."
    scene qpp 150
    p "Very well then..."
    play sound2 clothes3
    play sound water4c
    scene qpp 152
    bla "Penelope unties the knot of her bikini top, letting it slip loose as she quickly covers her chest with her hands." with dis2
    mct "Holy hell... she can barely cover them."
    if pennysexxmas:
        mct "And to think... just a few hours ago I had those tits in my hands while she moaned under me."
    scene qpp 153
    p "There. I suppose this is enough."
    p "The card only said I had to remove it, not flash the whole crowd."
    scene qpp 154
    d "Mm-hm."
    show qpp 153
    p "Although... I wouldn’t want anyone calling me a cheater."
    p "Maybe I should show everything to get those points?"
    show qpp 154b
    d "No."
    scene qpp 155
    x "Yes!"
    scene qpp 156
    n "Up to you, honey..."
    scene qpp 152
    p "Hmm..." with dis
    scene qpp 157
    p "What do you think I should do, [mc]...?"
    scene qpp 152
    if penelopepath:
        menu:
            with dis 
            "Show them [mt](Dalia -1)":
                mc "Well... it does feel like you’re cheating a little if you don’t."with dis
                p "*Snorts* Hmmph."
                show qpp 157
                p "Well then... let it never be said that I’m anything less than fair."
                play sound water4c
                scene qpp 159 with dis17
                mct "Oh yeah..." with dis14
                scene qpp 154
                $ dalia_points -= 1
                d "*Jealously* Hmm."
                scene qpp 160
                x "WOW."
            "This is enough":
                mc "I'd say this is enough."with dis
                mc "Like you said, the card didn't mention anything else. Anyone saying otherwise would just be greedy."
                p "Mm-hm."
                show qpp 157
                p "A gentleman. Didn’t know men like that still existed."
                show qpp 152
                mc "That's me, I can't help it."
                mc "Always a gentleman."
                p "Mm-hm..."
    else:
        mc "Y-You should, yeah. N-No doubt."
        mc "I wouldn't want anyone to call you a cheater either."
        show qpp 157
        p "*Snorts* Relax, cowboy, I was just teasing you."
        p "Sorry to disappoint you, but it's not happening."
        show qpp 152
        mct "Dammit... now I just made myself look like a pervert for nothing."
    $ pennytitscm = True
    play sound coins1
    $ penelopepointscm += 100
    scene qpp 146b
    d "Okay, okay, time to move on!" with dis12
    d "You can cover yourself now... w-well played."
    d "Next round!" with hpunch 
    jump poscm3cm4
label cm4:
    $ kissormisscm = True
    play sound ding volume 0.75
    mc "Let's go with Kiss or Miss." with dis
    scene qpp 141
    d "Very well then..."
    d "{i}Team building! Cover your eyes. The group will pick someone to kiss you on the lips. If you guess correctly, you score a hundred points. If not... everyone else does!"
    scene qpp 142
    d "Oh... w-wow. This got intense real fast." with dis08
    show qpp 143
    mc "Oh boy, I like this one already!"
    scene qpp 140
    d "Yeah, of course you like it."
    d "I'm starting to think Chang slipped you a cheat sheet for all the dirty cards."
    play sound water4c
    scene qpp 144
    mc "*Covering your eyes* What can I say, luck just happens to love me!" with dis14
    mc "Alright, I'm ready!"
    show qpp 145
    d "And how do we know you're not peeking??"
    show qpp 144
    mc "Oh, come on, where would the fun be in that?"
    mc "I'm playing fair, I swear. My eyes are shut tight!"
    show qpp 145
    d "Hmm, okay..."
    play sound water5
    show qpp 145
    bla "You hear the girls shifting in the water, whispering and plotting in secret."
    n "{i}[[Unintelligible] ?"
    d "{i}[[Unintelligible] !"
    x "{i}[[Unintelligible] ."
    p "{i}[[Unintelligible] ?"
    mc "*Chuckles* (This is fun.)"
    n "Alright! We've decided!"
    p "Don't move!"
    play sound water5
    scene black
    d "And don't open your eyes!"with dis12
    mc "I won't, promised!"
    play sound water5
    play sound2 water4c
    bla "You hear someone slowly drawing closer and crawling between your legs, her warm breath teasing you before she even touches you."
    mct "Oh boy..."
    play sound3 water4c
    if alexpath:
        play soundloop kissing fadein 2
        bla "She leans in, lips brushing yours at first, then pressing harder as her tongue slips past your lips, exploring your mouth shamelessly."with dis12
        mct "H-Holy FUCK."
        mct "I-I was expecting just a peck. T-This is... a good kiss..."
        stop soundloop fadeout 2
        play sound water4c
        play sound2 drips
        bla "After a few seconds she finally pulls away, her hand trailing down in the same movement, groping you through your swimsuit." with dis15
        scene qpp 147
        mc "*Opening your eyes* Holy shit..." with dis14
        mc "T-That was... good."
    else:
        bla "She leans in, pressing her lips to yours for only a fleeting second, almost as though mocking you."with dis12
        mct "Damn. That was... not very passionate."
        play sound water4c
        play sound2 drips
        bla "Just as she pulls away, her hand drifts lower, her fingers closing around your junk, giving it a firm, deliberate squeeze." with dis15
        mc "*Grumbles* Mph!"
        scene qpp 147
        mc "*Opening your eyes* (T-That final touch was intense enough, though.)" with dis14
    scene qpp 147b
    n "So... who kissed you, Casanova?"
    scene qpp 146
    mc "*Looking around* Hmmm..." with dis
    scene qpp 95b
    mc "*Looking around* Hmm..." with dis
    scene qpp 124
    mc "*Looking around* Hmmmm..." with dis
    scene qpp 148
    mc "Hmmm..." with dis12
    menu:
        with dis
        "Nancy":
            scene qpp 147
            mc "I’m taking a shot in the dark here, but... I'm gonna say it was Nancy."with dis
            scene qpp 147b
            n "Oh..."
            if alexpath:
                n "Well, you said it was a good kiss, so I'll take the compliment."
            else:
                n "Well, not sure if this is a compliment or not."
            n "But sorry, [mc], you're wrong. We win this round!"
        "Dalia":
            show qpp 91
            mc "I’m taking a shot in the dark here, but... I'm gonna say it was Dalia."with dis
            show qpp 90b
            d "Hah! So wrong!"
            d "A hundred points for each of us!"
        "Alex [mt](+100)":
            show qpp 124
            mc "I’m taking a shot in the dark here, but... I'm gonna say it was Alex."with dis
            scene qpp 123
            x "Really? What makes you say that?"
            show qpp 124
            if alexpath:
                mct "That wildness, that audacity, that scent..."
            else:
                mct "Who else could have squeezed my cock at the end..."
            mct "Not to mention Nancy wouldn’t put herself in that position with her daughters here."
            mct "Yeah... it was her."
            mc "Uh... just a hunch."
            x "*Snorts* Hmph."
            show qpp 123
            x "You're a damn lucky one, you know that?"
            play sound coins1
            play sound2 pop
            $ mcpointscm += 100 
            scene qpp 149
            x "Yeah... it was me."
            mc "I knew it..."
            x "Guess we made it too easy for you..."
            mc "Nah, don't worry. I'm just that good."
            x "*Chuckles* You cocky bastard..."
            x "Alright then! Let's continue."
            jump poscm3cm4
        "Penelope":
            show qpp 95b
            mc "I’m taking a shot in the dark here, but... I'm gonna say it was Penny."with dis
            show qpp 95
            p "Oh my!"
            p "That was a good shot!"
            p "But... sorry to disappoint you, [mc], it wasn't me."
label kisscmnoguess:
    play sound coins1
    $ daliapointscm += 100 
    $ nancypointscm += 100 
    $ alexpointscm += 100 
    $ penelopepointscm += 100 
    scene qpp 121
    mc "Aghhh, dammit! For real??" with dis
    mc "Who was it?"
    mc "I need to know!"
    scene qpp 90b
    d "Sorry, you'll have to die without knowing!"
    scene qpp 91
    mc "*Chuckles* Oh, c'mon! Seriously?"
    show qpp 90b
    d "Yup! No correct guess, no answer!"
    d "Time to move to the next round!"
    show qpp 91
    mc "*Chuckles* You're evil."
    mc "But fair enough, well played..."
    jump poscm3cm4

label poscm3cm4:
    $ cmround += 1
    play sound water4c
    scene qpp 108
    mc "Alright, alright, alright!" with dis15
    mc "Nancy!"
    mc "“Smol but Mighty” or... “Picky Pack”?"
    scene qpp 102
    n "Umm..."
    n "Okay, let's go with... Smol but Mighty."
    show qpp 108
    mc "Smol but Mighty it is!"
    mc "{i}Group Clash! Shortest King or Queen in the group earns the 100 points!"
    show qpp 119
    d "Noice! Annie and Nova aren’t here today, so... that's gotta be me!"
    show qpp 160b
    x "Yeah... looks like you got another one!"
    x "You're on fire, Dal."
    show qpp 162
    p "Wait a second... not so fast."
    p "I'm pretty sure Alex is shorter than you."
    show qpp 163
    x "*Awkward chuckle* What? That's nonsense."
    x "Fake news!"
    show qpp 161
    d "Wait, is she? I never really checked."
    show qpp 129
    n "Actually, I just saw a measuring tape by the garden entrance, right next to the toolbox!"
    n "Perfect chance to settle this right now!"
    show qpp 164
    x "O-Oh no, no, all that trouble won't be necessa–"
    play sound5 w2 volume 0.44
    show qpp 119
    d "That's a cool idea!" with pl
    d "Honestly, I don’t even know my exact height either."
    d "Let's measure it!" with hpunch 
    play sound water3
    play sound2 drips
    play sound3 footsteps4
    scene qpp 165
    bla "Dalia quickly hops out of the pool." with dis17
    play sound4 water3
    play sound5 drips
    play sound6 chair2
    scene qpp 166
    x "*Following her* G-Gghh... freezing again..." with dis15
    x "Why am I even letting you drag me into this..."
    scene qpp 147b
    n "Okay then!"
    n "Let me grab the tape real quick before you turn into ice pops!"
    play soundlow stairswood2
    play sound water5
    scene qpp 168
    d "No worries, Mom!"with dis15
    d "After soaking in the pool, I can't even feel the cold anymore!"
    show qpp 167
    n "*Coming out of the pool* Good!"
    mct "Oh boy, what a duo..."
    n "Got it! Straight backs, no cheating!"
    play sound2 footsteps4
    play sound7 rubbody
    scene qpp 169 with dis15
    n "*Stretching the tape* Let's see..." with dis
    n "Hold still for a second..."
    play sound3 stairswood2
    play sound4 rubbody
    scene qpp 170
    n "And we've got... a little over sixty-five inches! So... 5'5''!"with dis15
    d "Perfectly average and proud of it!"
    play sound6 footsteps4
    scene qpp 171
    n "And Alex over here..."with dis17
    x ". . ."
    play sound5 stairswood2
    play sound7 rubbody
    scene qpp 170
    n "She comes in at..."with dis15
    n "Sixty-four inches!"
    n "One full inch shorter than Dalia!"
    scene qpp 89
    p "Oh my god, that much?! She's a shorty!" with hpunch
    p "So. Freaking. Cute!"with hpunch 
    scene qpp 172
    n "Just like Annie and Nova!"
    n "That's so adorable!"
    scene qpp 173
    $ alexpointscm += 100
    play sound7 coins1
    play sound3 splash3
    play sound4 water
    scene qpp 173
    x "*Jumping back into the pool* I-I'm not that short. Or cute." with dis12
    x "Y-You can all go fuck yourselves."
    show qpp 174
    mc "*Laughs* (The way she gets so mad about being called “cute” honestly just makes it even cuter.)"
    show qpp 173
    x "Now please, can we move on to the next round already?"
    x "My fingers are starting to turn into prunes."
    scene qpp 119
    d "*Giggles* Yeah, she's actually right." with dis
    d "If we don’t hurry, we won’t even have time for the sauna."
    play sound water4c
    $ cmround += 1
    scene qpp 110
    n "Sounds good to me!" with dis14
    n "Everybody hold onto your seats, because we’re cranking it up a notch!"
    n "Penny! No time to think!"
    n "“Heavy Fireworks” or... “Most Wanted Sandwich”?"
    scene qpp 89
    p "*Chuckles* The second one sounds intriguing."
    scene qpp 110
    n "Sandwich it is, then!"
    n "And it says..."
    n "{i}Team building! Which two people from the group would you have a threesome with? Most voted person gets 100 points!"
    n "Ohhh-ho-ho!"
    scene qpp 98
    d "U-Um..."
    d "Well, in any case..."
    d "Like... three of us are literally family here, so..."
    d "I guess we can just skip ahead and give the points to [mc] and Alex."
    d "Congrats on the free points."
    scene qpp 143
    mc "Hey, hold on! We still have to vote!"
    mc "Those are the rules!"
    show qpp 99
    d ". . ."
    show qpp 98
    d "F-Fine, fine... let's give [mc] his ego boost."
    d "If I {i}had to{/i} have a threesome with anyone here, I’d pick... [mc] and Alex."
    show qpp 147b
    n "Funny, I'd also have it with [mc] and Alex."
    show qpp 95
    p "Oh wow, what a coincidence, I'd also take [mc] and Alex."
    if penelopepath:
        p "Maybe the universe is trying to tell us something."
    show qpp 123
    x "*Snorts* Thanks, everyone."
    x "As for me... I've gotta go with [mc] and my dear best friend Dalia."
    x "I'm sure it'd be... *chuckles* interesting, to say the least."
    show qpp 99
    mc "As for me..." with dis 
    mc "Well... I’d never ever dare to suggest anything that could get pearl-clutching credit card companies offended, so I'll say Alex, and..."
    menu:
        with dis 
        "Nancy":
            scene qpp 143
            mc "Nancy."with dis
        "Dalia":
            mc "Dalia."with dis
            $ dalia3somecmchoose = True
            d ". . ."
        "Penelope":
            scene qpp 143
            mc "Penny."with dis
    if not dalia3somecmchoose and daliapath:
        mc "I think that'd be a pretty inte–"
        play sound musicstop
        scene qpp175
        d "W-Wait, what?!" with pr
        d "But Alex and I are best friends! We've always been!"
        show qpp 95
        p "So? Is there anything you wanna say, sis...?"
        show qpp 135
        x "{i}Now{/i} the conversation is getting interesting."
        play sound coins1
        $ mcpointscm += 100
        $ alexpointscm += 100
        scene qpp 98
        d "I-I didn't mean it like that, smartasses." with dis
        d "What I mean is... like..."
        d "*Clears throat* You know what? F-Forget it. Let's move on."
    else:
        play sound coins1
        $ mcpointscm += 100
        $ alexpointscm += 100
    scene qpp 98
    d "*Clears throat* Alright." with dis 
    d "Guess Alex and [mc] tied at votes, so that means 100 points for each."
    d "NEXT!" with hpunch
label cmround9:
    play sound water4c
    $ cmround += 1
    scene qpp 126
    p "Okay! We're getting close to the end, folks, and things are heating up!" with dis14 
    p "Alex! It's your turn!"
    p "“Burn, Baby, Burn” or “Silent Star”?"
    scene qpp 155
    x "Burn, Baby, Burn! Obviously."
    scene qpp 126
    p "*Chuckles* Yeah, that name was too catchy to pass up..."
    p "{i}Duel! Choose two people for a plank contest! The one who lasts longer gets 100 points!"
    scene qpp 77b
    x "Uhhh... easy!"
    x "[mc] and Dalia, no question." 
    scene qpp 161
    d "Really? You don't want to try yourself?"
    scene qpp 160b
    x "Nahhh, this one's for the two best abs in the pool."
    x "Show us those aren't just for decoration!"
    show qpp 176
    d "Oh, well, you won't see me complaining, then!" with dis
    d "Let's go, [mc]! Time to put on a show!"
    play sound water3
    play sound2 chair2
    play sound3 wood2 volume 0.4
    scene qpp 177 with dis17
    d "*Dropping into plank position* I'm really sorry, [mc], believe me."with dis12
    d "But we don't have to torture ourselves out here. Just give up now, and we can get back into the hot water where it’s nice and cozy."
    show qpp 178
    mc "I’m afraid I can’t do that. My core strength’s gotten to another level these last few months."
    mc "I could hold this for an hour easily."
    show qpp 177
    d "An hour? Please. I could do three."
    show qpp 178
    mc "*Laughs* Wow, even in this cold?"
    show qpp 177
    d "Of course! I barely feel it anymore."
    d "So seriously — whenever you get tired of staring at my pretty face, feel free to give up."
    d "I can hold this pose aaaaaall night."
    show qpp 178
    mc "You and me both, Dal."
    show qpp 177
    d "In fact, I’ll even count the seconds to make it more fun."
    d "One..."
    play sound ding
    show black
    show screen sixminuteslater
    pause 
    scene qpp179
    hide screen sixminuteslater
    dsc "G-gGg-GGgghHHHhhh..." with dis15
    mc ". . ."
    dsc "H-Hhhhhow t-the hell..."
    dsc "...a-are you not... even sh-shaking yet?!"
    dsc "I-I c-can't–"
    play sound fallfull
    scene qpp180
    d "AAaghhhhgggggggggggggg..." with vpunchslow
    d "*Panting* F-Fuck..."
    d "*Panting* O-Okay... you win..."
    d "*Panting* Dammit."
    play sound2 coins1
    $ mcpointscm += 100
    $ cmround += 1
    play sound3 water4c
    play sound4 water3
    scene qpp 137
    x "And it's the mighty Dalia's turn again!" with dis14
    x "Choose wisely, girl, your fate depends on it."
    x "“Movie Mime” or... “Fast and Furious”?"
    play sound5 splash3
    play sound4 water
    scene qpp 90b
    d "*Jumping back into the pool* Okay, okay! No panic. Easy choice again! I still got this." with dis
    d "I choose Movie Mime!"
    d "Now, please tell me it's a movie trivia."
    scene qpp 137
    x "Let's see, let's see..."
    x "{i}Team building! You have to act out six different movies without speaking, and the person in front of you has to guess them. If they get all six right in under sixty seconds, you both score 100 points!"
    show qpp 146b
    d "Whaaaaaat...? Mimics? With Penny...?"
    show qpp 162
    p "Well. Guess this is a lost round already."
    show qpp 83
    d "You bet it is..."
    d "No chance you can guess any movie."
    d "Pfft, maybe if the subject were Instagram reels and makeup tutorials..."
    show qpp 162
    p "I’ve been watching movies since before you could even spell “Netflix”, thank you very much."
    p "The real issue is how bad your acting’s gonna be."
    show qpp 129
    n "Come on, give it a try!"
    n "I'm sure it'll be fun!"
    show qpp 146b
    d "Fine, fine... I’ll whisper the six movies to Alex first so everyone knows we didn’t cheat..."
    d "Not that Penny’s gonna guess a single one, but anyway..."
    show qpp 162
    p "At least try not to choose any of those weird ass movies you watch sometimes."
    play sound water4c
    show qpp 83
    d "Don't worry, I chose old movies to keep it easy for you, grandma." with dis12
    d "*Sighs* Let's just get this over with."
    play sound2 water4c
    scene qpp 181
    d ". . ." with dis12
    scene qpp 162
    p "*Instantly* Titanic."
    scene qpp 181
    mc "Eh...?"
    mc "Ohh... damn, that was fast."
    play sound water3
    play sound2 water4c
    scene qpp 182 with dis12
    p "The Matrix." with dis08
    play sound3 water3
    play sound4 water4c
    scene qpp 183 with dis12
    p "Inglourious Basterds." with dis08
    play sound5 water3
    play sound6 water4c
    scene qpp 184 with dis12
    p "Pulp Fiction." with dis08
    play sound7 water3
    play sound8 water4c
    scene qpp 185 with dis12
    p "The Fellowship of the Ring." with dis08
    play sound2 water3
    play sound water4c
    scene qpp 186 with dis12
    p "Ratatouille." with dis08
    play sound6 water3
    play sound water4c
    scene qpp 113 
    d "YES!" with dis12
    scene qpp 122
    mc "W-Wait, wha–WHAT?!"
    mc "How the fuck did you guess them so fast?!"
    mc "And how the hell did you even get Ratatouille from {i}that{/i}?"
    mc "No way those are the actual answers."
    play sound coins1
    $ daliapointscm += 100
    $ penelopepointscm += 100
    show qpp 187
    x "Erm... those were the exact six she gave me, yeah." with dis 
    x "Holy fuck, I’ve never seen such freaky brain-sync."
    show qpp 90
    d "Not bad, Penny." with dis 
    show qpp 95
    p "You made it easy, Dal."
    p "Good mimics, credit where credit's due."
    show qpp 90
    d "Good guesses."
    show qpp 156
    n "See...?"
    n "You have more in common than you think..."
    $ cmround += 1
    play sound4 water
    play sound5 water4c
    show qpp 141
    d "Alright, everyone!" with dis12
    d "We got to the final set of rounds!"
    d "[mc], here's your final choice!"
    mc "I'm ready!"
    d "“X Marks the Spot” or... “Bribe Me Baby”?"
    show qpp 141b
    mc "Hmm..." with dis06
    play sound whoosh9
    call screen card_selection(cards=cmcards3) 
label cm5:
    play sound ding volume 0.75
    mc "X Marks the Spot!" with dis
    scene qpp 141
    d "Alright, let's see..."
    d "{i}Duel! The person who's reading the card has to kiss you wherever you choose! If they chicken out, you get the points instead!"
    scene qpp 143
    mc "Oh-ho, now we’re talking! This game just keeps getting better and better!"
    scene qpp 191
    if kissormisscm:
        d "Why the hell are you the one always pulling the kissing cards?"
    else:
        d "Why the hell are you the one always pulling the spicy cards?"
    d "If you’re rigging this, at least try not to make it so damn obvious."
    show qpp 190
    mc "*Laughs* I swear I'm not cheating!"
    d "*Suspiciously* Mmmh..."
    show qpp 191
    d "Fine, fine, whatever."
    d "So, tell me..."
    d "Where do you want that kiss, Romeo?"
    show qpp 190
    mc "Hmmm..."
    menu:
        with dis
        "My lips [mt](Kiss, Penelope -1)":
            $ cmkisslipsdalia = True
            mc "Just a tiny kiss on my lips."with dis 
            show qpp 191
            d "Your... lips?"
            d "...Seriously?"
            if kissormisscm:
                d "Not your... cheek? Or your hand? You already got a kiss on the lips tonight."
            else:
                d "Not your... cheek? Or your hand?"
            show qpp 190
            mc "Hmmm, tempting, but... nah, not really."
            mc "I've already made up my mind."
        "My dick [mt](+100)":
            mc "Just a tiny kiss on my cock."with dis 
            show qpp 191
            d "Ha, ha, very funny."
            d "Now seriously."
            show qpp 190
            mc "I'm dead serious."
            show qpp 191
            d "I'm not gonna kiss your dick. That's not happening."
            show qpp 190
            mc "Well... in that case..."
    show qpp 191
    d "You’re only saying that because you know I’ll refuse, don't you? You want the points."
    show qpp 190
    mc "Hmm, could be, could be..."
    mc "Call it strategy."
    d "*Grumbling* Mmmmrrrgh..."
    if cmkisslipsdalia and daliapath:
        show qpp 191
        d "You know what...?"
        d "Fine. Whatever."
        d "I'll do it."
        d "It's just a party game, right?"
        play sound water5
        play sound2 water4c
        scene qpp 192
        bla "Dalia crawls over and straddles your lap." with dis2
        show qpp 193
        d "*Whispering* You thought I wouldn't dare do it in front of everyone, didn't you?"
        show qpp 194
        mc "*Whispering* I was hoping you would."
        mc "*Whispering* Worst case, I'd still score a hundred points. Win-win."
        show qpp 193
        d "*Snorts* You're such an idiot."
        play sound3 water4c
        scene qpp 195
        bla "Dalia leans in and kisses you softly on the lips." with dis17
        d "Mmm..."
        if penelopepath:
            scene qpp 196
        else:
            scene qpp 95b
        x "Oh, damn, girl! That's quite the tiny kiss!" with dis12
        if penelopepath:
            $ penelope_points -= 1
            p "*Jealously* Hmm."
        else:
            p "Mm-hm."
        play sound4 water5
        d "Alright, alright, enough show!"
        d "Onto the next round!"
        play sound2 coins1
        $ daliapointscm += 100
    else:
        show qpp 191
        d "Ugh, f-fine, get your damn 100 points, tryhard."
        d "Next round!"
        play sound2 coins1
        $ mcpointscm += 100
    jump lastroundcm
label cm6:
    play sound ding volume 0.75
    mc "Bribe Me Baby!" with dis
    scene qpp 141
    d "Alright, let's see..."
    d "{i}Bonus card! You get to give a hundred points to anyone you want! Let’s see if they’re generous enough to pay you back later..."
    scene qpp 143
    mc "Uhh, interesting..."
    show qpp 141
    d "Damn, for real? You always get the easy ones..."
    show qpp 141b
    mc "*Chuckles* Didn’t you say you wanted to speed things up? I’m just helping."
    scene qpp 120
    d "Yep, you're not wrong there!" with dis
    d "So come on, hurry up so we can move onto the next round!"
    mc "Hmm..."
    menu:
        with dis
        "Yourself":
            play sound coins1
            $ mcpointscm += 100
            scene qpp 121
            mc "Well... guess I'll just give them to... myself."with dis
            scene qpp 100
            d "Wait, what?! You can't do that!"
            show qpp 100b
            mc "Why not? The card didn’t say I couldn’t."
            show qpp 100
            d "Um..."
            d "Well, technically I guess not, but..."
            show qpp 100b
            mc "Then it's settled!"
            show qpp 100
            d "Erm..."
            d "Ugh, FINE!"
            d "You're such a tryhard..."
            jump lastroundcm
        "Nancy":
            play sound coins1
            $ nancypointscm += 100
            scene qpp 147
            mc "I'm gonna go with... Nancy for this one."with dis12
            scene qpp 147b
            n "Well, thank you, [mc]."
        "Penelope":
            play sound coins1
            $ penelopepointscm += 100
            scene qpp 95b
            mc "I'm gonna go with... Penny for this one."with dis12
            scene qpp 95
            p "Thanks, [mc]..."
        "Alex":
            play sound coins1
            $ alexpointscm += 100
            scene qpp 124
            mc "I'm gonna go with... Alex for this one."with dis12
            scene qpp 123
            x "Your generosity shall not be forgotten, my king..."
        "Dalia":
            play sound coins1
            $ daliapointscm += 100
            scene qpp 121
            mc "I'll just give them to Dalia."with dis
            scene qpp 188
            d "What?! No. No, no, no."
            d "I don't want your pity points."
            show qpp 189
            mc "Too late. I already gave them to you."
            play sound coins1
            $ daliapointscm -= 100
            show qpp 188
            d "Then I’m giving them right back. I don’t need your charity."
            show qpp 189
            mc "Seriously? Can you even do that?"
            show qpp 188
            d "Yep! And I just did. I’m winning this thing on my own!"
            d "Now... onto the next round!"
            show qpp 189
            mc "Uhh... okay then."
            jump lastroundcm 
    scene qpp 143
    mc "And before your competitive streak kicks in, Dal... I didn’t pick you because I knew you’d get mad if I gave you free points." with dis12
    show qpp 188
    d "And you were absolutely right!"
    d "I will crush you fair and square, thank you very much!"
    show qpp 189
    mc "*Chuckles* That's exactly what I figured."
    show qpp 188
    d "Now, onto the next round!"
label lastroundcm:
    $ cmround += 1
    play sound water4c
    scene qpp 108
    mc "Ahhh... I'm starting to taste victory, I can feel it!" with dis15
    mc "Nancy!"
    mc "Nancy, Nancy, Nancy..."
    mc "Ohoho... interesting titles!"
    play sound whoosh3b
    scene qpp 188
    d "Can you kick it into turbo mode, [mc]??" with pr
    d "At this rate, no one’s even gonna see the sauna, let alone use it!"
    d "Chop, chop!"
    play sound whoosh3b
    scene qpp 147
    mc "Okay, okay! Jeez!" with pl 
    mc "Nancy!"
    mc "“Crowned and Honored” or... “Size Does Matter”?"
    show qpp 147b
    n "Uhh..."
    n "*Giggles* I mean, I’d be lying if I said I wasn’t dying to know what Size Does Matter is about."
    scene qpp 108
    mc "Excellent choice!"
    mc "And it reads like this..."
    mc "{i}Group Clash! Whoever's seen the biggest cock in real life gets 100 points! You can’t count your own!"
    play sound water
    scene qpp 79
    p "Oh, god..." with dis12
    p "And... how are we even supposed to measure that?"
    p "Like... are we supposed to guess inches, or..."
    scene qpp 156
    n "You can just describe what you saw."
    n "You can go first."
    show qpp 79
    p "W-What? G-Go first with what?"
    p "I haven't... I mean..."
    show qpp 156
    if penelopepath:
        n "Oh, please, honey, come on. I know for certain you're not a virgin."
    else:
        n "Oh, please, honey, come on."
    n "This is a safe space. We can be open about this stuff."
    scene qpp 80
    if penelopepath:
        p "I-I know you know."
    p "It’s just... it’s kinda weird talking about this out loud. In front of everyone."
    show qpp 136
    d "Um... y-yeah, I get that."
    d "I don't... like, I'm not sure I've got much to contribute here anyway."
    d "I don't... yeah."
    show qpp 122
    mc "Erm... kind of the same here, honestly."
    mc "I mean, it’s not like I’ve seen any hard cocks besides my own."
    mc "Unless we’re counting porn, which I’m guessing we’re not."
    if lunapath:
        mc "Or... Luna's uncle's chicken. Which... I'm guessing doesn't count either."
    if alexpath:
        scene qpp 160b
        x "Okay, okay! Chill, people. You're entitled to be shy. I got this one." with dis12
        x "And I'm... pretty sure I'm getting those points this time."
        play sound water4c
        show qpp 197
        x "Like... no joke, this guy was like THIS big. I swear to God." with dis12
        x "He was hung like a damn horse. Massive!"
        mc "*Clears throat* Mrghm."
        x "I still have no idea how that thing even fit inside me. It was INSANE."
        mct "It certainly was..."
        play sound whoosh3b
        show qpp 136
        d "Alex! What the fuck?!"with pl
        play sound whoosh3b
        show qpp 160b
        x "What? Oh come on, don't act all shy now, Daly..."with pr
        x "I can tell you in more detail later, don't worry."
        show qpp 156
        n "Well, I must admit I've seen a pretty impressive one too. Like, it needed two hands and still wasn’t fully covered."
        n "But... it’s kinda hard to top what you just said, so I'll give you this round, Alex."
        play sound coins1
        $ alexpointscm += 100
    else:
        show qpp 156
        n "Well, since everyone suddenly seems so shy, I'm just gonna give the points to [mc] for Luna's chicken."
        n "*Giggles* It's pretty hard to beat that, honestly."
        play sound coins1
        $ mcpointscm += 100
    play sound2 water4c
    show qpp 98
    d "O-Okay, um... can we {i}please{/i} move on to the next round already?" with dis12
    d "This conversation is making me feel very awkward."
    show qpp 99
    n "*Giggles* As you wish..."
    $ cmround += 1
    play sound water4c
    show qpp 110
    n "Alright, ladies and gentleman!" with dis14
    n "We're down to the last three rounds!"
    show qpp 89
    p "Shoot! I'm so ready!"
    scene qpp 110
    n "Okay, here we go!"
    n "“Dice of Doom” or... “First Class Ticket”?"
    scene qpp 112
    p "Um... I'm gonna go with... Dice of Doom."
    show qpp 110
    n "Dice of Doom it is!"
    n "{i}Bonus card! Everybody rolls a die. If you land on a one, you snag thirty points... but you’ve gotta leave the room for the next round!"
    scene qpp 112
    p "Uhh... some cards require a dice, huh?"
    p "So {i}that's{/i} why there were dice and coins in the box."
    scene qpp 113
    d "I like it!"
    show qpp 155
    x "Let's roll, then!"
    show qpp 113
    d "Let me go first! I'm feeling lucky tonight!"
    n "Alright then, Dalia's up!"
    play sound2 ["<silence 0.7>", dicesound]
    scene dice091video with dis
    pause 1.55
    scene dice091 
    d "...DAMMIT." with dis08
    p "*Laughs* Oh, you {i}are{/i} lucky, Dal! You got the thirty points!"
    d "But I miss the whole next round! Ugh, so not worth it!"
    n "Penny's next!"
    play sound whoosh3b volume 0.5
    play sound2 pop
    scene dice092
    p "Yay!"with pr
    play sound whoosh3b volume 0.5
    play sound2 pop
    scene dice093
    n "Nice!"with pr
    play sound whoosh3b volume 0.5
    play sound2 pop
    scene dice095
    mc "FUCK."with pr
    play sound whoosh3b volume 0.5
    play sound2 pop
    scene dice094
    x "Hell yes!"with pr
    play sound3 coins1
    $ mcpointscm += 30
    $ daliapointscm += 30
    play sound water4c
    scene qpp 129
    n "Okay, looks like [mc] and Dalia are the lucky ones!" with dis12
    n "Both of you, out of the pool!"
    n "You can come back in two minutes!"
    play sound water3 
    play sound2 bubbles
    play sound3 drips
    play sound4 stairswood2
    scene qpp 130
    d "*Coming out of the water* OKAY! TWO MINUTES!"
    d "Come on, [mc], let's wait behind the wall! Quick!"
    mc "*Shivers* I-I'm coming, I'm coming!"
    $ cmround += 1
    play sound water4c
    scene qpp 126
    p "SECOND-TO-LAST ROUND!" with dis14
    p "*Chuckles* Now, let’s pick up the pace, people. We told Dalia two minutes, so I assure you she’s gonna be storming in here in exactly a hundred and twenty seconds, tops."
    p "ALEX! Your pick."
    p "“Saint Among Sinners” or... “Basketball Star”?"
    show qpp 155
    x "Saint Among Sinners!"
    show qpp 126
    p "*Giggles* Good choice, good choice..."
    p "Now let's see..."
    p "{i}Battle Royale! If you’ve never had a wild night with anyone in this room, you score a clean hundred points! BUT, you also gotta finish your drink to drown those sorrows! And by wild night... you know EXACTLY what I mean!"
    play sound2 water4c
    scene qpp 198
    x "Oh... oh. Wow." with dis12
    x "Um..."
    x "W-Well, I definitely haven’t slept with either of you."
    scene qpp 162
    p "We should probably count [mc] and Dalia too, even if they’re not here right now. Just sayin'."
    if alexpath:
        scene qpp 199
        x "Oh... right. Yeah."
        x "Of course."
        show qpp 196
        x "Uhm, I still..."
        x "I mean..."
        x "You know..."
        show qpp 162
        if penelopepath:
            if toldpennynotalex:
                $ penelope_points -= 1
                p "Huh. So he {i}did{/i} lie to me about that."
                p "That cheeky liar..."
                p "*Sighs* Relax, Alex. I know you’re not chugging that drink either."
            else:
                p "Relax, Alex. I know you’re not chugging that drink either."
            p "Guess it's a good chance to drop the masks, now that Dalia's not here."
            show qpp 198
            x "Wait... hold on, you... y-you KNOW?"
            x "And... w-wait, wait, wait, what do you mean, EITHER?"
            show qpp 196
            p ". . ."
            x "No..."
            x "You... YOU HAVE TOO–?!"with hpunch 
            p ". . ."
            scene qpp 198
            x "OH. MY. FUCKING. GOD."
            x "Does Dalia know?"
            x "Is that why you two have been at each other’s throats lately?! She didn't want to tell me shit!"
            show qpp 162
            p "Yes. She knows."
            p "Not sure if she knows about you, though."
            p "I feel like... she probably suspects, but it's a different case with you than it is with me."
            show qpp 198
            x ". . ."
            x "Oh my god."
            x "Like, oh my GOD. This is crazy."
            show qpp 162
            p "I know it all might sound like a crazy bunch of bullshit, but..."
            p "[mc] isn’t just playing around. He means it. I... verified."
            show qpp 198
            x "O-Oh, boy."
            x "Oh my god... Oh my god."
            x "This went from zero to nuclear real quick."
            if nancypath:
                x "I need a minute to process–"
                x ". . ."
                show qpp 199
                x ". . ." with dis
                show qpp 200
                p ". . ."
                show qpp 201
                p ". . ."with dis
                show qpp 203
                n ". . ."
                show qpp 202
                p "Um..."
                p "Why didn't you finish your drink, Mom...?"
                show qpp 204
                n "Uhh..."
                show qpp 202
                p ". . ."
                p "NO. FUCKING. WAY."
                p "WHEN?!" with hpunch 
                show qpp 204
                n "Ehh... let’s, um... maybe talk about it after the game?"
                show qpp 160
                x "H-Holy shit."
                x "This family is WILD!"with hpunch 
                $ pennywantstotalknancyaftercm = True
                jump posharemrevelationcm
            else:
                x "I don't even know how to process it."
                show qpp 162
                p "Let's not talk about it here."
                p "Later. Dalia must be coming soon."
                play sound coins1
                $ nancypointscm += 100
        else:
            p "Relax, Alex. I know you’re not chugging that drink."
            p "Guess it's a good chance to drop the masks, now that Dalia's not here."
            show qpp 198
            x "Wait... hold on, you... y-you KNOW?"
            x "Since when?!"
            show qpp 162
            p "Let's not talk about it here."
            p "Later, if you want. Dalia must be about to arrive."
            show qpp 198
            x "Ohh... o-okay."
            x "I guess that... I'm not getting points this round."
            show qpp 196
            p "Mm-hm."
            play sound coins1
            $ nancypointscm += 100
            $ penelopepointscm += 100
    else:
        scene qpp 198
        x "Yeah. I mean... I figured."
        x "But I... still haven't."
        x "Have you...?"
        scene qpp 162
        p "No. No, no... no. Not really."
        p "So... uhm... I'm gonna finish my drink. And get my points."
        show qpp 198
        x "Cool. Me too."
        show qpp 162
        p "Cool..."
        p "Cool."
        play sound coins1
        $ alexpointscm += 100
        $ nancypointscm += 100
        $ penelopepointscm += 100
label posharemrevelationcm:
    scene qpp 204b
    d "...And two minutes! Coming!" with dis12
    play sound runsit
    show qpp205 with dis14
    play sound2 splash3
    play sound4 water
    play sound5 water3
    d "*Jumping in* AAAAAAGHHH..." with dis12
    d "O-Ooohhh, so good..."
    d "Man, it's getting WAY too cold outside!"
    if alexpath and nancypath and penelopepath:
        scene qpp 198
        d "Anyway, tell us, tell us! Who got the points?!" with dis
        x ". . ."
        d "*Looking around* Hello...?"
        d "Alex!" with hpunch 
        show qpp 199
        x "U-Uh-huh?"
        x "Oh... y-yeah, nobody did."
        show qpp 161
        d "What? Seriously??" with dis 
        show qpp 199
        x "Y-Yeah. No points."
        x "No one... uhm... met the condition."
    else:
        scene qpp 95b
        d "Anyway, how did it go?!" with dis
        d "Did any of you get quadruple points or something?"
        show qpp 95
        p "Nah, we didn't, don't worry."
    play sound water4c
    show qpp 176
    d "Hah! That means it all comes down to the final round!" with dis12
    d "And I'm the one who gets to pick the card!"
    d "You ready for the ultimate showdown, [mc]?!"
    show qpp 143
    mc "Ready to crush you, Dal!"
    if alexpath and nancypath and penelopepath:
        show qpp 116
        d "Heh! We'll see about that!"
        d "Alex! For TRIPLE POINTS! Give me my two options!"
        x ". . ."
        show qpp 117b
        x "*Smirks* Mhm." with dis
        d "Alex! My cards!"with hpunch 
        show qpp 117
        x "Ehh? O-Oh, yeah! Sorry, I was zoning out."with dis08
    play sound water4c
    $ cmround += 1
    show qpp 137
    x "Alright, everyone! This is it!" with dis14
    x "LAST ROUND!"
    x "Only two possible cards left!"
    x "And your final options are..."
    x "“Big Brain Smoothie” and “Coin of Chaos”!"
    show qpp 118
    d "Uhh..."
    d "*Muttering* If Big Brain Smoothie means trivia, Penny or Nancy’s got that in the bag, no doubt..."
    x "Hey!"
    d "*Muttering* Risky..."
    d "*Muttering* The other one sounds a bit random, but..."
    show qpp 119
    d "Okay! Decided!"
    d "Let's go with Coin of Chaos!"
    show qpp 137
    x "Coin of Chaos will be the final card!"
    x "And here's what it says..."
    x "{i}Duel time! You and the player to your right each pick a side of the Chang coin. Toss it in the air... and whoever wins the toss gets the 100 points!"
    play sound water4c
    show qpp 125
    d "Awghh, are you serious?!" with dis12
    d "The round that's supposed to decide the winner is gonna be just dumb luck?!"
    d "This one's worth triple points!"
    if mcpointscm > daliapointscm + 300 or daliapointscm > mcpointscm + 300:
        scene qpp 112
        p "Wait... how many points are we at right now?"
        if mcpointscm > daliapointscm + 300:
            p "Doesn't [mc] have more than 300 points over Dalia?"
            p "Even if she wins this last round, [mc] would still be ahead, right...?"
            show qpp 161
            d "Wait... so..."
            d "Does that mean..."
            d "[mc] has already won the game? Even if I take this last round?"
            show qpp 204
            n "Oh! True!"
            n "I think he did!"
            n "Congrats!"
            jump dalialostthecm
        else:
            p "Doesn't Dalia have more than 300 points over [mc]?"
            p "Even if he wins this last round, Dalia would still be ahead, right...?"
            show qpp 161
            d "Wait... seriously?"
            d "So... does that mean..."
            d "...what I think it means...?"
            show qpp 156
            n "Looks like we already have a winner!"
            n "Congrats!"
            jump daliawonthecm
    show qpp 143
    mc "Tsk, tsk, tsk, it would be dumb luck if we didn't get to choose the side of the coin, Dal."
    mc "It's pure intuition."
    mc "And... you know what? I’ll even let you choose first."
    show qpp 119
    d "*Snorts* That's not how it works at all, but... fine."
    d "I'm gonna trust my gut and say..."
    d "TAILS!"
    play sound water5
    show qpp 206
    mc "*Grabbing the coin from the box* Then I'll take HEADS!" with dis17
    mc "If I’ve been counting right, this toss will decide who gets crowned as “The Chang” tonight, ladies!"
    mc "You or me, Dalia!"
    mc "So... may Lady Fortune be on my side!"
    play sound coinflip
    scene qpp 207 with dis08
    pause .05
    play soundlow whoosh6 volume 0.5
    play sound7 water3
    scene qpp 208 with dis04
    pause .2
    d "OH MY GOD." with dis
    d "THIS IS IT."
    d "THIS DECIDES EVERYTHING."
    d "WHY AM I SO NERVOUS?!"with hpunch 
    play sound2 water4c
    $ renpy.music.set_volume(0.45, delay=8.0, channel='soundloop3')
    stop music fadeout 12
    scene qpp 209 with dis2
    mc ". . ." with dis15
    mct "Oh shit."
    mct "It's heads."
    mct "I've won!"
    d "Why so much suspense?!" with hpunch 
    d "Spit it out! What is it?!" with hpunch 
    mc "Um..."
    mc ". . ."
    menu:
        with dis12
        "Heads (You win)":
            $ cmcoinheads = True
            mc "It... landed on heads." with dis
            d "Heads...? What?!"
            play sound6 water3
            play sound7 bubbles
            d "*Standing up* No way, let me see!" with vpunch 
            d "*Looking at the coin* . . ."
            d "...Fuck."
            jump dalialostthecm
        "[gr]Tails (Dalia wins)":
            $ cmcointails = True
            mc ". . ." with dis
            mc "It... landed on tails."
            d "Tails...?"
label daliawonthecm:
    play sound water3
    play sound2 splash3
    play sound4 bubbles
    play sound3 drips
    play sound5 coins
    play sound6 whoosh3b
    play music ["<silence 1.5>"]
    queue music xmas2
    if cmcointails:
        $ daliapointscm += 300
    scene qpp212
    show thechang2
    if cmcointails:
        d "*Jumping up* TAILS!" with vpunchslow
    else:
        d "*Jumping up* YES!" with vpunchslow
    d "I'VE WON! I'M THE CHANG!" with hpunch
    mc "*Chuckles* Well... I tried."
    mc "Well played, Dalia."
    d "Hell YES! The sauna is mine!" with hpunch 
    scene qpp 124
    show thechang2
    d "And as the winner... Alex, I officially invite you to join me!" with dis12
    d "There's enough space for two!"
    scene qpp 123
    show thechang2
    x "Oh, wow! Thank you, girl."
    x "So generous of you..."
    jump changmending
label dalialostthecm:
    play sound water3
    play sound2 splash3
    play sound4 splash3
    play sound3 water4c
    play sound5 coins
    play music ["<silence 1.7>"]
    queue music xmas2
    if cmcoinheads:
        $ mcpointscm += 300
    scene qpp210
    show thechang1
    d "*Crashing down* UGHHHHhhh..." with vpunchslow
    d "DAMN IT!"with hpunch 
    d "Can't believe I lost... AGAIN. I swear I never win anything!"
    scene qpp 211
    show thechang1
    mc "*Laughs* Don't be sad, Dal."
    mc "It was mostly just luck."
    scene qpp 210
    show thechang1
    d "...And I still lost."
    d "Goddammit..."
    $ changermeisterwinmc = True
    jump changmending
label changmending:
    hide screen ep9_pts_overlay
    play sound bubbles
    play sound3 water3
    play sound2 water4c
    if pennywantstotalknancyaftercm:
        scene qpp 213
    else:
        scene qpp 213b
    if changermeisterwinmc:
        p "*Standing up* Well... that was fun. Congrats, [mc]." with dis15
    else:
        p "*Standing up* Well... that was fun. Congrats, Dalia." with dis15
    p "I had a blast, but I’m pretty wiped, so I’m gonna go to bed before I collapse."
    if pennywantstotalknancyaftercm:
        p "Would you... mind coming with me, Mom, though?"
        p "*Clears throat* I really want to... borrow some toothpaste before I sleep."
        show qpp 214
        n "O-Of course, honey!"
        n "I have... some toothpaste in my bag!"
    else:
        n "Same here!"
        n "That was a lot of fun, guys."
        n "You really made me feel like I was back in college again."
    d "Goodnight, you two!"
    mc "Sleep well, girls!"
    x "See you tomorrow!"
    play sound bubbles
    play sound2 water
    play sound3 footsteps4
    play sound4 drips
    scene qpp 215 with dis2
    if changermeisterwinmc:
        mc "*Coming out of the water* Well, well, well..."with dis12
        mc "I think someone forgot to congratulate the champion."
        scene qpp 216
        d "*Snorts* You're so cocky."
        d "But fine. You won fair and square, especially those physical challenges."
        d "Congrats, [mc]."
        show qpp 215
        mc "*Chuckles* Thank you, thank you."
        mc "You know, I don't really care that much about the sauna."
        mc "So I'm gonna cede the reward to you."
        show qpp 216
        d "Hah! No way! I don't take charity."
        d "You earned it, so you’re going to enjoy it. End of discussion."
        d "Enjoy your sauna, [mc]."
        show qpp 215
        mc "Can I at least invite you to join me...?"
        show qpp 216
        d "Nope! Still counts as a pity prize!"
        d "So... I’m just gonna go to my room, slip into my sexy pajamas, and probably start a pillow fight with Alex until we pass out instead."
        show qpp 215
        mc "*Laughs* Now you're just trying to tease me."
        show qpp 216
        d "*Giggles* Maybe."
        d "But seriously, I'm off to bed! Goodnight, [mc]."
        show qpp 215
        mc "*Chuckles* Alright, alright..."
        mc "Goodnight, Dalia."
        play sound footsteps4
        scene qpp 221 with dis15
        mc "*Sighs* (Ahh... what a day.)" with dis
        mct "Guess this finally marks the end of the night. Or... at least the part surrounded by beautiful girls."
        mct "Best Christmas ever in any case, though. No debate."
    else:
        mc "*Coming out of the water* Well, I've got nothing to argue here, really."with dis12
        mc "Well played, Dalia."
        show qpp 216
        d "*Chuckles* I know what you're thinking."
        d "{i}“Why’s this cringe girl celebrating like she just won the Olympics over some stupid party game?”"
        show qpp 215
        mc "*Laughs* Nah, not even close."
        mc "You should see me playing Monopoly. I've flipped tables for less."
        mc "And besides, I like this competitive side of you."
        show qpp 216
        d "Well, in that case... *giggles* I'm glad."
        show qpp 215
        mc "Enjoy your well-earned sauna!"
        show qpp 216
        d "*Chuckles* Thanks!"
        if cmcointails and alexpath and daliapath:
            d "If I don't see you again before bed, good ni–"
            play sound whoosh3b
            play sound2 fist
            play sound3 debris3
            scene qpp 217
            x "Dal!" with hpunch  
            x "I just went to check the sauna, and do you know what I noticed?"
            show qpp 218
            d "You've gone and come back in less than a minute...?"
            show qpp 217
            x "*Whispering* There's enough space for three people!"
            x "*Whispering* We should invite [mc] too."
            show qpp 218
            d "*Whispering* W-What?! Are you mad?!"
            show qpp 217
            x "*Whispering* Why not? It’s not like we’re about to film a porno in there, if that's what worries you, relax."
            show qpp 218
            d "*Whispering* T-That's not what I meant!"
            show qpp 217
            x "*Whispering* I mean, if the coin flip had gone the other way, [mc] would’ve won."
            x "*Whispering* Doesn’t feel right to leave him out just because of random luck... don't you think?"
            show qpp 218
            d "*Whispering* Uhm..."
            d "*Whispering* ...Okay, that's a fair point, to be honest."
            show qpp 217
            x "*Whispering* Right...?"
            show qpp 219
            d "*Clears throat* Um..." with dis12
            d "Hey... [mc], do you wanna... join the sauna too?"
            d "There's enough space for all three of us, we think."
            show qpp 220
            mc "Really??"
            mc "Of course! I'd love to!"
            mct "OH BOY..."
            show qpp 219
            d "But don't get any weird ideas."
            d "Swimsuits stay on."
            show qpp 220
            mc "Naturally."
            mct "Damn it..."
            show qpp 219
            d "O-Okay. Good."
            d "Cool."
            d "Then see you in there."
            d "And don't be late, or we'll lock you out!"
            show qpp 220
            mc "I'll be right there, just need to get some water from the kitchen!"
            d "Mm-hm."
            play sound footsteps4
            scene qpp 221
            x "*Walking away* This is gonna be fun..." with dis17
            d "*Shivers* W-What’s fun is finally getting out of this damn cold."
            d "*Shivers* T-T-T-Temperature’s dropping like crazy..."
            mct "Oh, man... a sauna with Dalia and Alex."
            mct "Could it really happen...?"
            mct "Nah... don’t start fantasizing, [mc]. Dalia would never be up for it."
            mct "But oh well, in any case, guess Santa's not gonna visit tonight."
            mct "Night isn't over yet!"
        else:
            d "If I don't see you again before bed, good night!"
            show qpp 215
            mc "If you need some extra company at the sauna, please, just say the word."
            show qpp 216
            d "*Giggles* Nice try, but sorry, it's fully booked already."
            d "Maybe... next time."
            d "Goodnight, [mc]."
            show qpp 215
            mc "*Chuckles* Alright, alright..."
            mc "Goodnight, Dalia."
            play sound footsteps4
            scene qpp 221 with dis15
            mc "*Sighs* (Ahh... what a day.)" with dis
            mct "Guess this finally marks the end of the night. Or... at least the part surrounded by beautiful girls."
            mct "Best Christmas ever in any case, though. No debate."
    play sound sneeze
    play sound2 owl
    mc "*Sneezes* (B-But I better get inside if I want to avoid frostbite. Standing out here like this is just suicide...)" with vpunchslow 
    if changermeisterwinmc or (cmcointails and alexpath and daliapath):
        mc "*Shivers* (S-Sauna. Now.)"
    if cmcointails and alexpath and daliapath:
        jump alexdaliasauna
    else:
        jump leavingwinterhouse



label alexdaliasauna:
    $ daliaalexsauna = True
    stop soundloop3 fadeout 7
    stop music fadeout 6
    scene black with dis3
    show screen afewminuteslater with dis2
    pause
    play soundloop2 saunasound fadein 4
    hide screen afewminuteslater
    scene qss 1
    with dis3
    d "Ooooohhh boy, I can feel aaaall my pores opening." with dis15
    x "Mmmm... for real. It’s like every inch of my body is melting."
    x "But like... in a relaxing way."
    play sound stairswood2 volume 0.8
    scene qss 2
    mc "*Going down the stairs* Oh, wow!" with dis2
    mc "You were not kidding, the mad lad really built a sauna in the basement!"
    x "*Whispering* Uhhh, look who finally decided to join the party..."
label ga_alexdalia:
    if _in_replay:
        play soundloop2 saunasound fadein 3
    play music2 saunapremusic fadein 7 volume 0.35
    play sound2 footsteps4
    scene qss 3 with dis17
    mc "Uhh...?" with dis12
    scene qss 4
    mc "Oh my god, and there are hot girls in bikinis inside too!" with dis12
    mc "What kind of luxury stay is this??"
    mc "I need to make sure to leave a five-star review."
    show qss 5
    x "*Snorts* You definitely should."
    x "It’s even a mixed gender sauna today — Christmas special."
    x "You're one lucky bastard."
    show qss 4
    mc "*Chuckles* Lucky me indeed."
    mc "How's the detox going, ladies?"
    show qss 6
    d "So far so good. My skin's already thanking me."
    d "It’s easy to use too! Just pick the program on the touchscreen outside, and it does everything automatically."
    d "It releases steam on its own and everything. It’s like a robot spa!"
    play sound footsteps4 volume 0.7
    show qss 7
    mc "*Grabbing the hourglass* So much fancy tech, but they still use these little hourglasses." with dis15
    mc "Are we gonna control the time we stay in here with this?"
    show qss 8
    x "Why?"
    x "Can't handle a little heat, [mc]?"
    show qss 9
    mc "Not even close. I’ve survived worse, believe me."
    mc "I could stay here aaaaaall night."
    show qss 8
    x "Big words for someone who’s already sweating bullets."
    show qss 9
    mc "This?"
    mc "That’s just my body crying tears of joy after seeing you."
    show qss 8
    x "*Chuckles* Ahhh, I see, of course."
    x "But you're right. To be honest, it’s not actually that hot."
    x "We set it to Steam Room mode. Less heat, more humidity."
    x "It’s better for the skin. It opens the pores, and makes everything... soft and sensitive."
    show qss 9
    mc "Damn, you would be a good saleswoman, Alex..."
    mc "Now I'm thinking I need one of these in my future house too."
    mc "What's the temperature now?"
    play sound chair2
    scene qss 10
    d "Let me check!" with dis12
    d "It is... um... forty... “astetta”?"
    d "I'm guessing that's Celsius?"
    x "Uhhh... so it's a European sauna."
    d "Yeah! Or at least... the thermometer is."
    x "Classy..."
    play sound ["<silence 1.2>", chair2]
    play sound2 rubbody
    play sound3 clothes3
    scene qss11
    mc "*Sitting down* Ohhhh... damn, this feels incredible. You girls were so right." with dis15
    show qss 12
    d "Hey, that was my spot!"
    show qss 11
    mc "Sorry, Dal, but this spot’s closer to the heater."
    mc "I mean, I'd move, I swear, but my body is not responding."
    show qss 12
    d "*Grumbles* I'm starting to regret inviting you."
    show qss 11
    mc "Five minutes, and then we can switch. I promise."
    show qss 11b
    d "Mmmph."
    show qss 12
    d "Mmrh, fine..."
    d "But I'm timing you!"
    show qss 11b
    x "*Giggles* Mm-mh."
    scene black with dis22
    show screen afewminuteslater with dis15
    pause
    scene qss 13 
    hide screen afewminuteslater
    with dis3
    bla "For a while, you simply relax and let the heat blur everything else away." with dis2
    bla "The warmth seeps deep into your muscles while the sound of gentle breathing mixes with the hiss of steam."
    d "*Taking a deep breath* Mmmh..."
    x "Hhmm..."
    mc "Mmmm..."
    mct "Damn, this feels good..."
    mc "*Glancing over at the girls* (And insanely hot in {i}every{/i} possible way.)"
    scene qss 14
    x "Hmmm..." with dis2
    scene qss 15
    x "Guys... this is it." with dis
    x "I need a sauna at my future place. It's official."
    x "It feels too good to not have one."
    show qss 16
    d "Didn’t you have one in your old place?"
    d "Sounds like a very rich-family thing to have."
    show qss 15
    x "I think we had, like, three of them in our summer home, but I never bothered to use any the few times I went there."
    x "I used to think it was just a boring... “grown-up thing”."
    x "Guess I should’ve appreciated it before I became an outcast."
    show qss 17
    mc "Who would’ve thought sweating could be this fun, huh?"
    show qss 18
    x "Hah! Actually... I have a theory that some of the best activities in life involve a bit of sweat."
    show qss 16
    d "So true..."
    d "The gym..."
    d "Hiking..."
    d "And..."
    show qss 16b
    mc "...{i}Other things."
    show qss 16
    d "*Giggles* Yeah."
    show qss 18
    scene qss 13
    x "*Chuckles* I see you guys get it..." with dis2
    d "Mm-hm..."
    mc ". . ." 
    x ". . ."
    x "{i}You know..."
    show qss 18
    x "To be completely honest, there’s something bothering me a little." with dis17
    x "I can’t really enjoy the full experience like this."
    show qss 17
    mc "Like this how?"
    show qss 18
    x "Yeah, I mean..."
    x "Do you guys mind if I... take my top off?"
    play sound wood2 volume 0.5
    scene qss 19
    d "W-What?" with dis12
    d "Your top...?"
    mc ". . ."
    scene qss 19b
    x "I mean, it’s only logical, isn't it?" with dis
    x "That’s the Finnish way. Everyone goes in naked."
    show qss 19
    d "U-Uhm..."
    show qss 20
    d "Y-Yeah, well, but this isn't Finland." with dis 
    d "We don't..."
    d "I-I think you had a few too many drinks during that pool game."
    scene qss 19b
    x "Oh come on, Dalia. It’s just the three of us here. It’s not like it’s a public exhibition."
    x "And I’m not forcing anyone to join me, don't worry."
    show qss 20
    d "U-Um..."
    d "I-I mean... it’s a little weird with [mc] here too, but... whatever." 
    d "Do what you want."
    d "Follow your... Finnish spirit."
    show qss 21
    x "If it makes you uncomfortable, I won’t, Dal."
    show qss 20
    d "Me? No."
    d "Not a problem at all."
    d "I’ve seen you naked a hundred times already. No big deal."
    show qss 21
    x "*Grins* Alright... cool then."
    x "Hundred and one coming right up."
    stop music2 fadeout 12
    $ renpy.music.set_volume(0.35, delay=25.0, channel='soundloop2')
    play sound chair2
    play sound2 wood2 volume 0.5
    scene qss 22
    bla "Alex stands up and starts to slowly untie her top." with dis2
    mct "OH BOY."
    mct "Is she really gonna do it...?"
    $ renpy.music.set_volume(0.7, channel='music3')
    play music3 saunamusic fadein 9
    play sound clothes3
    scene qss 23
    bla "Alex unties the knot behind her neck, the thin fabric slipping off her skin before landing soundlessly on the floor."with dis2
    mct "You bet she did..."
    mct "Alexandra Bardot... NOW this is getting interesting..."
    show qss 24
    x "Oops, I kinda forgot to ask you, [mc], sorry." with dis12
    x "Hope this doesn’t make you uncomfortable either."
    show qss 25
    mc "Uncomfortable...?"
    mc "Me? Not at all."
    mc "Actually..."
    mc "*Smirks* Mind if I join you?"
    show qss 24
    x "Ooh... but of course not! On the contrary!"
    x "We're friends, aren't we? If we were in Northern Europe, this would be totally normal."
    show qss 25
    mc "You're {i}very{/i} right."
    mc "Those people clearly know what they’re doing."
    x "Mm-hm."
    play sound clothes5
    play sound2 ["<silence 1.5>", clothes2]
    scene qss 26
    bla "The sound of your swimsuit being taken off fills the brief silence, followed by a soft thud as it lands beside hers." with dis14
    mc "There."
    mc "No big deal."
    x "Mm-hm..."
    d "Y-You're both nuts..."
    play sound2 ["<silence 0.4>", chair2]
    scene qss 26b
    bla "Alex sits next to you again." with dis17
    x "*Giggles* See? Much better like this! Don't you think so, [mc]?"
    mc "Definitely..."
    d ". . ."
    play sound wood2 volume 0.3
    scene qss 27
    x "*Arching her back* Mmmmmhh... yes..." with dis15
    x "Now my skin can finally breathe."
    mct "DAMN..."
    mct "I missed you, girls..."
    play sound clothes3
    play sound2 oily
    scene qss 28
    bla "You can feel your pulse hammering faster, each beat pushing blood lower, getting hard in a matter of seconds." with dis2
    mct "Oh, damn..."
    d "*Breathing heavily* . . ."
    play sound2 wood2 volume 0.3
    play sound3 clothes3
    scene qss 29
    x "*Leaning onto you* OH-MY-GOD." with dis15
    x "That surely didn't take long, did it?"
    show qss 30
    mc "Well... it’s not every day I get to share a sauna with girls this gorgeous."
    show qss 31
    d "J-Jesus Christ, [mc]."
    d "Y-You have no self-control."
    show qss 29
    x "Did you know he was this big, Daly?"
    x "I mean... wow! I'm shocked!"
    show qss 31
    d "I... I-I don't know."
    d "I mean... I-I didn't... like... I-I didn't think about it much."
    show qss 29
    x "Can I touch it...?"
    show qss 31b
    d "Alex! You're drunk as fuck!"
    show qss 29
    x "I'm not!"
    x "*Giggles* I'm just curious!"
    x "I mean... come on, look at it. It's practically begging to be touched."
    x "I promise it'll only be a second."
    show qss 30
    mc "I won't stop you..."
    play sound6 wood2 volume 0.2
    play sound7 clothes3oily
    play soundloop wetting2 fadein 2
    scene sauna1 with dis2
    bla "Alex's fingers curl gently around your cock, as she begins to stroke it teasingly slowly." with dis12
    mc "*Soft moan* O-Ohh..."
    mct "Oh god, I can't believe this is happening..."
    mct "Alex's shame meter sure is broken..."
    mct "Although... it's not like Dalia's complaining either..."
    d ". . ."
    x "*Whispering* Wow... it's even harder than I imagined, [mc]."
    x "*Giggles* You must be hornier than I thought."
    bla "Dalia remains silent, trying not to stare and muttering under her breath, trying to sound annoyed but failing."
    d "*Muttering* I-I thought you said... a second."
    x "*Giggles* But it's fun to see [mc] twitching like a live wire every time I squeeze just a little."
    x "And... well, it's also fun to just let yourself go sometimes."
    x "Don't you think so...?"
    d "Mmmh."
    x "Come on... doesn’t it get exhausting pretending you’re not excited too?"
    x "I promise you it feels amazing to stop caring, Dalia."
    x "The moment I took my top off, I felt so free. You should try it, trust me."
    d ". . ."
    mc "*Soft moan* O-Ohh..."
    stop soundloop fadeout 2
    play sound chair2
    scene qss 32
    d "*Standing up* O-O-Okay, okay, enough already." with dis12
    d "You win, you crazy fucks. Just sitting here next to you wearing my swimsuit is making me feel like the world’s biggest prude."
    d "You wanna go all Finnish style? Fine. I’ll join your... damn naked sauna."
    d "If you thought I'd chicken out, you can think again."
    show qss 33
    mc "Oh yeah..."
    x "*Grinning* Thank you, Dal. That's the spirit!"
    show qss 32
    d "Just... don't mention this to Mom. Or Penny. Alright?"
    show qss 33
    mc "Not a word."
    d "Mmh."
    play sound clothes3
    scene qss 34
    d "Mmmh..." with dis17
    mct "Oh fuck yeah..."
    play sound2 clothes3b
    scene qss 35 
    bla "Dalia fumbles with her bikini top, trying to cover herself with her arms — her breasts pushing against them, refusing to be hidden."with dis17
    mc "Oh my god... it's really happening..."
    play sound3 clothes3b
    scene qss 36
    d "A-Alright. I-It's off." with dis17
    d "No more sweaty boobs. Freedom achieved. You happy now?"
    x "*Smirks* [mc] certainly looks happy."
    x "Now come join us on the bench!"
    x "Don't act all shy now!"
    play sound clothes3
    scene qss 37
    bla "Dalia turns around and lowers her arms, trying her best to look composed." with dis17
    show qss 38
    d "Okay."
    show qss 37
    mc "Oh, sweet heavens, Dalia..."
    mc "Your body's unreal. Everything's so... tight..."
    x "*Giggles* Those nipples could scratch cement, Dal."
    x "*Whispers* You horny girl..."
    show qss 38
    d "M-My nipples are always like this."
    d "I don't need cold temperatures or... or t-to be horny for them to get hard."
    show qss 37
    x "Cheeky liar!"
    x "Are you forgetting that we've shared a locker room for years?"
    show qss 38
    d "S-Shut up!"
    play sound chair2
    play sound2 clothes3oily
    play soundloop wetting2 fadein 2
    scene sauna2 with dis2
    bla "The bench creaks as Dalia finally sits down. Alex’s hand slides back over your cock as she continues to caress it." with dis12
    x "Holy fuck, Dalia, [mc] just got even harder."
    x "I wonder if this is the sauna's effect or... just the view."
    mc "Hah... p-probably both..."
    d "*Awkwardly* Um..."
    d "...I thought you were just doing {i}that{/i} to tease me into taking my top off too."
    d "A-Are you seriously gonna... keep going...?"
    x "*Giggles* I mean, yeah, that was the original plan, but poor [mc] over here keeps sending all his blood to the wrong area."
    x "I figured I’d help him out a little before he faints."
    mc "Hah..."
    mc "T-Thanks Alex, I-I appreciate it."
    x "*Giggles* God, I can barely wrap my hand around it..."
    x "I'll admit... this is definitely getting me in the mood..."
    x "*Soft moan* Haha..."
    play sound clothes3
    stop soundloop fadeout 2
    scene qss 39
    x "You should try this, Dalia." with dis2
    scene qss 40
    d "Um... I'm good, thanks."
    show qss 39
    x "Oh, come on... don't be a bore!"
    x "It's just for fun! We're all adults here!"
    x "Simply... enjoying some sauna time."
    d ". . ."
    x "Come on..."
    x "You know you want to..."
    d ". . ."
    show qss 40
    d "Uhm..."
    d "*Sighs* Will you... finally shut up if I do this?"
    show qss 39
    x "*Grinning* Absolutely."
    d ". . ."
    d "Hmph."
    show qss 40
    d "...Fine." with dis08
    d "Just... don't get any weird ideas."
    play sound clothes3oily
    play soundloop wetting2 fadein 3
    scene sauna3 with dis2
    bla "Dalia finally slides her hand up your thigh, until she firmly grasps your cock and starts stroking you up and down, her eyes locked on it like she's hypnotized." with dis12
    mc "*Soft moan* O-Ohhh... fuck yes..."
    mc "*Whispers* I missed your touch, Dalia..."
    d ". . ."
    d "H-Happy now, you perverts...?"
    x "*Touching herself* AAaah... t-this is so fucking hot, Dal..."
    d "You really are impossible."
    x "*Giggles* S-See...?"
    x "Mmmmhh... that wasn't so hard, was it...?"
    d "I don't know how, but somehow... it's always [mc] who ends up winning."
    mc "Hah..."
    mc "Can't say I'm not... enjoying having lost at the Changermeister..."
    mc "*Staring at Dalia* Fuck, Dal..."
    mc "Your tits look... insanely good today. All I can think about is burying my face between them."
    d ". . ."
    d "...Thanks."
    d "Your..."
    d "...body looks good today too."
    scene sauna4 with dis2
    bla "The air in the sauna grows thick and heavy, each breath weighted with heat and desire as Dalia’s hand keeps moving." with dis
    mct "O-Oh my fucking god..."
    mct "I’m sitting in a sauna with Dalia and Alex... both of them naked... one touching herself, the other grabbing my cock..."
    mct "If this is a dream, I don’t ever wanna wake up."
    mct "I’ve imagined a threesome with them more times than I’d ever admit, but... is this really happening?"
    mct "Could this really lead to...?"
    x "*Moans* A-Aaahhh..."
    x "F-Fuck..."
    x "N-Now I get why they love saunas so much in Northern Europe..."
    d "Somehow, I don’t think {i}this{/i} is part of their usual spa routine."
    mc "T-Then they’ve still got a lot to learn..."
    mc "*Moans* A-Aaahh..."
    mc "Fuck..."
    stop soundloop fadeout 2
    play sound clothes3oily
    scene qss 40b
    d "O-Okay, enough." with dis14
    d "I can... definitely confirm — yes, it’s very hard. Very impressive."
    show qss 39
    mc "*Pulse racing* Oh, Dalia..."
    mc "I wanna shove my cock between your sweaty tits so fucking bad..."
    x "OH MY GOD, yes! Please DO THAT!"
    show qss 40
    d "You're dreaming."
    d "I'm not..."
    show qss 40b
    d "I mean, I-I'm not built for that."
    d "My tits aren't big enough to do that. I'm not Penny."
    show qss 39
    x "What?! Are you kidding me? Your tits are {i}perfect{/i}!"
    x "There’s more than enough there to swallow all of [mc]’s cock and still have room to spare!"
    show qss 40
    d "No, there isn't."
    show qss 39
    x "*Giggles* Well... there's only one way to find out."
    x "You know what to do, right?"
    x "On your knees, babe. Now."
    x "If I'm wrong, I'll owe you one."
    d ". . ."
    play sound wood2 volume 0.25
    play sound2 clothes3b
    play sound3 footsteps4 volume 0.3
    scene qss 41
    d "*Standing up* Fine. Just to shut you up." with dis2
    d "At this point, what does it matter, right...?"
    mc "Oh my Lord, look at these hips..."
    mc "My sweet girls..."
    play sound4 wood2 volume 0.3
    play sound7 clothes3oily
    scene qss 42
    x "Oh my god, [mc], your cock looks even bigger from this angle." with dis15
    x "Seriously, look at it!"
    x "It’s like... longer than my entire palm! And I have big hands, girl!"
    d "You make it sound like it's a weapon."
    x "*Snorts* Well... it kinda is."
    play sound clothes3b
    scene qss 43
    x "Like, holy shit, girl, do you actually think that thing could fit all the way inside you??" with dis15
    x "No chance, right?"
    d "W-What?!"
    x "Look! It literally reaches up to your belly button!"
    x "That thing would rearrange your organs! There’s no way you could take more than half of it before passing out."
    d "WHAT?!" with hpunchsubtle
    d "N-No!"
    play sound4 wood2 volume 0.3
    play sound5 clothes3
    scene qss 44
    d "*Kneeling down* I-I can take all of it!" with dis14
    show qss 45
    x "Ohh... so you've tested it already, huh...?"
    x "Is that why you're so confident?"
    show qss 46
    d "What? N-No."
    d "I d-didnt't mean it like that. I meant it like... I'm not... you know, fragile or anything."
    d "I-I just–"
    play sound clothes3
    show qss 47
    x "How about we cut the crap already, Dal?" with dis17
    x "I think we’d all have more fun if we drop the bullshit from now on."
    show qss 48
    d "W-What...?"
    d "What bullshit...?"
    show qss 47
    x "I know you two have fucked."
    x "Like animals, probably."
    show qss 48
    d "E-E-Excuse me...?"
    d "W-What are you saying?"
    show qss 47
    x "You're my best friend, Dalia. I know you better than anyone."
    x "I noticed how you couldn’t keep your eyes off him during the whole time we were playing the pool game."
    x "You were practically drooling, girl."
    show qss 48
    d "I-I-I did not–"
    d "I mean..."
    show qss 47
    x "I can read your face like a damn book, Dalia."
    x "I know you love him. And you know what? I get it."
    x "I love him too. Even if I’ve spent my whole life thinking love was bullshit."
    show qss 48
    d "Y-You WHAT?!"
    show qss 47
    x "I know that if I wasn’t here right now, you’d be riding him already." 
    x "You’d be moaning his name so loud the walls would be shaking."
    x "But deep down... maybe even better than yourself..."
    x "I {i}know{/i} you want me here."
    play sound clothes3
    show qss 50
    d "I d-don't..."with dis17
    show qss 49
    x "You're turned on as hell right now."
    x "And you want your best friend to see how good you can make him feel."
    x "You want to show off."
    x "You want him to see how desperate you get."
    x "And you want me to see how filthy you can be."
    show qss 50b
    d ". . ."
    show qss 49
    x "Because... just for tonight..."
    x "Just here, in this moment... you're not a little angel anymore."
    x "*Whispering* You’re a dirty, horny slut who wants to be fucked until you can’t think straight." 
    show qss 50b
    d ". . ."
    show qss 49
    x "Or am I wrong...?"
    x "Tell me, baby girl..."
    x "*Whispering* Am I wrong...?"
    show qss 50b
    d ". . ."
    show qss 49
    x "*Whispering* Do you wanna give [mc] a show he'll never forget...?"
    show qss 50b
    d ". . ."
    show qss 50
    d "*Whispering* ...I do."
    show qss 49
    x "Say it louder..."
    show qss 50
    d "I-I do–"
    play soundloop kissing fadein 2
    scene sauna5 with dis2
    bla "Alex kisses Dalia before she can even react. She stiffens for a second, but resistance slowly fades as she lets herself go." with dis12
    mc "Oh my FUCKING god..."
    x "*Moans* Mmmmmhhh..."
    d "M-Mmmhh..."
    mc "This is so fucking hot..."
    d "Mmmmh..."
    mc "Fuck yeah, that's it..."
    mc "Keep going..."
    x "Mm-mmmhhh..."
    mc "You two are gonna kill me..."
    scene sauna6 with dis2
    bla "Alex doesn’t stop. Her tongue moving teasingly deep, like she’s determined to make a show out of every second." with dis12
    x "Mmmmm-mhhh..."
    mct "Christ... if I get any harder, I’ll pass out before they're even done..."
    x "*Moans* Mmmmhhhh..."
    mc "I-I must admit..."
    mc "I’m happy to see you girls getting along so well..."
    x "*Giggles* Mm-mmh-mhh..."
    stop soundloop fadeout 2
    play sound wood2 volume 0.3
    play sound2 clothes3oily
    scene qss 51
    bla "Alex slides behind Dalia, her fingers tracing up her sides before cupping her breasts, squeezing them possessively." with dis15
    x "Now..."
    x "[mc] was promised something... and we wouldn’t want to disappoint him, would we...?"
    x "What do you think, [mc]...?"
    x "Are Dalia's tits big enough for you?"
    scene qss 52
    mc "Oh, more than enough, I'd say..."
    show qss 51
    x "Let's put it to the test, then..."
    x "You ready, Daly...?"
    show qss 52
    d ". . ."
    d "...I am."
    $ renpy.music.set_volume(0.45, delay=12.0, channel='music3')
    play sound7 clothes3oily
    play sound8 wood2 volume 0.18
    scene sauna7 with dis2
    bla "Alex pushes Dalia towards you, and she wraps her soft, full tits around your cock, squeezing them tight as she starts to slide them up and down your shaft."with dis12
    mc "O-Oh my god, f-fuck yes..."
    mc "O-Ohh Dalia, that feels so fucking good..."
    d "D-Does it...?"
    x "*Giggles* I bet it does. Just look at his face, Dal, he's already losing it."
    x "Does it hurt if I squeeze them harder?"
    d "N-No..."
    d "M-My nipples feel... kinda tingly, but..."
    d "I-It's a nice kind of sensitive.."
    mc "*Soft moan* AAAaah..."
    mc "J-Jeez... the humidity makes your skin so slick..."
    d "Y-Yeah... I know..."
    mc "Just like that..."
    mc "K-Keep going..."
    x "Told you your boobs would do the job, girl."
    x "Just look at you..."
    x "Your body is a goddamn dream."
    scene sauna8 with dis2
    bla "Alex presses her hands around Dalia’s sides, the friction turning from soft and playful to raw and needy."with dis12
    mc "O-Oohhh f-fuck... Alex..."
    d "*Breathing shakily* J-Jesus..."
    d "*Breathing shakily* I-Isn't this... t-too much...?"
    x "Shhhh..."
    x "Don't think. Just feel."
    x "Let yourself go and look at the man you love losing control because of you and your beautiful body."
    x "Right now, he’s yours. Every breath, every twitch, every sound... yours."
    d ". . ."
    mc "Y-You're dangerous, Alex..."
    x "*Giggles* I get that a lot."
    x "*Whispering* And now..."
    x "*Whispering* Make him beg for it."
    d "B-Beg...?"
    x "Tell me, [mc]... do you wanna fuck Dalia...?"
    x "Because I assure you she’s DYING for it."
    mc "W-Want to...?"
    mc "Fuck, I {i}need{/i} to..."
    scene sauna7 with dis2
    x "*Giggles* Oh wow... listen to that desperation..."with dis12
    x "He wants your body, Dal."
    x "Should we give him what he wants...?"
    mc "You tease..."
    x "Should we let him lose himself in you?"
    d "*Softly* M-Maybe we should..."
    x "Do you wanna feel him filling you?"
    x "Do you want every inch of this cock sliding deep inside you...?"
    d ". . ."
    d "*Whispering* I fucking do..."
    play sound wood2 volume 0.4
    play sound2 chair2
    play sound3 clothes3oily
    scene qss 54 with dis15
    bla "Alex smiles, knowing she's in control of every heartbeat in the room. She helps Dalia stand up as she slides her panties down her trembling thighs."with dis
    mc "Oh, my girls..."
    mc "You have no idea how much I'm fighting not to completely lose it right now..."
    show qss 53
    x "Mmm... maybe we should call it a night already."
    x "Feels like we’ve already crossed enough lines, don’t you think?"
    show qss 54
    mc "You wouldn't do that to me..."
    mc "And besides... I can see it in your eyes, Alex. There's no way you could stop now."
    show qss 53
    x "*Giggles* Shit... you caught me."
    play sound oily
    show qss 55
    x "But... I think there’s someone else in this sauna who’d go feral if we stopped now." with dis15
    x "*Giggles* I mean, look at this poor girl."
    show qss 56
    mc "Oh, babe..."
    play sound3 ["<silence 0.5>", fallfull] volume 0.8
    play sound2 wood2 volume 0.3
    scene qss57
    bla "Dalia suddenly pounces on Alex, laughter spilling between them as their slick bodies hit the warm wooden floor." with dis15
    d "*Laughing breathlessly* S-Shut the hell up already!"
    d "*Laughs* Look how we ended up!"
    d "You’re literally the worst influence in the world!"
    x "*Laughs teasingly* Yeah, probably. You should’ve listened to your mom and stopped hanging around me ages ago."
    d "*Laughs* Oh please! She’s the one who invited you tonight!"
    mct "Holy fuck... that pussy’s glistening..."
    play sound4 chair2
    play sound5 wood2 volume 0.3
    play sound6 rubbody
    scene qss 58
    mc "*Kneeling down* Oh Dalia..." with dis17
    mc "You’re dripping all over Alex, you know?"
    d "*Arching her back* Am I...?"
    mc "Do you want me inside you so bad...?"
    d "*Whimpering* Hah..."
    d "Y-Yes..."
    d "Fuck, I can't wait anymore..."
    d "I-I need you to fuck me, [mc]..."
    d "HARD..."
    mc "You want it rough, baby...?"
    d "Y-Yeah..."
    d "I-I'm too wet to care..."
    d "I want it raw... please don't hold back..."
    mc "As you wish..."
    play sound2 debris3
    play sound slap1
    play sound4 slap1
    play sound3 penetration2
    play soundlow penetration3
    scene qss 59
    d "{sc=4}*Screams* A-A-AaaAAAAAHHHhhh..." with hpunchslow
    d "{sc=4}*Screams* F-FFFfuckkkkk..." with hpunch
    play sound penetration2
    scene sauna9 with dis2
    dsc "AAAahhh... AAAAAaAHHH... AAaaaaAAAGGHHHhhh..." with dis12
    dsc "*Panting* O-Oooohh myyyy g-gggooOOooddd....."
    mc "O-OH YEAH..."
    dsc "AaaaAAAhHHHmmmhh...."
    dsc "*Panting* W-Whaaat a-are you doing to meee..."
    mc "C-Christ, you're so fucking tight, Dalia..."
    mc "I-It’s like your pussy’s trying to choke my dick..."
    mc "It feels... SO GOOD..."
    x "*Breathing hard* O-Oh yeah..."
    x "You better be grateful for that tight little hole you’re ruining right now, [mc]..."
    mc "*Groaning* F-Fuck, I am... I'm so f-fucking thankful, believe me..."
    bla "You slam into Dalia with no mercy, hips snapping hard from the first thrust. Her drenched slit spreads around you, dripping down her thighs and over Alex beneath her."with dis 
    mct "Good gracious, every second of that tease was so worth it..."
    mct "She was completely ready for me..."
    d "*Loud moan* AAaaAAAahhhh..."
    x "That's how you like it, don't you, girl?"
    d "*Panting* Yeah... f-fuck me hard, [mc]..."
    d "*Panting* M-Mmmmmhm... a-aaahhh.... aAAAAhhh..."
    d "*Panting* O-Oh fuck... so... deep..."
    d "*Whimpering* T-Too deep–" with hpunch 
    mc "You're taking it balls-deep f-from the start, Dalia..."
    mc "You’re swallowing my whole fucking cock like a champ..."
    scene sauna10 with dis15
    bla "Alex grinds beneath you both, her slick body sliding through the mess of fluids dripping from above." with dis
    x "*Moans* O-Ooohhh fuck yes..."
    x "G-Goddamn, Dal, I knew you were tough, but holy..."
    d "*Broken chuckle* H-Hahh..."
    d "I c-can–"
    d "*Squeals* AAaaaaAhhh..." with hpunch 
    d "S-S-Slow down, [mc]..."
    d "*Moans louder* AAAAhhh..."with hpunch 
    d "I-I'm g-g-gonna c-cum already if you k-keep... p-pounding me like that..."
    mc "*Growling* F-Fuck yeah, cum for me, babe..."
    mc "Cum all over my cock..."
    d "B-But I d-don't–"
    d "Oh my god..."
    d "OH GOD."with hpunch
    dsc "OOOHHH MY F-FUCKING GG-G-G-G-GOODDD..."with hpunch 
    play sound slap1
    play sound3 slap1
    play sound2 squirt
    scene qss60 
    dsc "*Orgasming* AAAAaaaaAAAAaGGGhhh!!!" with hpunchlong
    play sound4 squirt
    dsc "Y-YYYEEEAAaaaaahhh......" with hpunch 
    play sound rubbody
    play sound5 oily
    scene qss 61
    d "*Panting, trembling* O-OOoooohhh... m-my G-GOhhD..." with dis15
    d "*Catching her breath* O-Okay... ok-kay..."
    x "Wait, did you cum already?! Damn, girl!"
    d "*Still panting* G-Give me j-just a minut–"
    play sound whoosh6
    play sound2 slap1
    play sound3 penetration2
    play sound4 debris3
    scene sauna11b
    bla "Before she can even finish the sentence, you grab her hips and push yourself back inside."with hpunch 
    dsc "F-FFFFfffuuuuccckkk, [mc!u]..."
    mc "*Groaning* Oh D-Dalia..."
    x "Hell yeah..."
    mc "I-I can't stop now..."
    d "*Loud moan* AAaaAAAHHhh..."
    d "AAaAAhhh... f-fucking hell I'm g-gonna cum again..."
    x "Holy shit, you're multiorgasmic?!"
    d "*Gasping* I-I don't f-fucking knoooow..."
    d "B-But..."
    d "It feels... way t-tooo sensitive now..."
    mc "F-Fuck yes..."
    mc "Don't restrain, babe..."
    mc "I wanna feel every one of your twitches and every squeeze..."
    d "*Panting* J-Just..."
    d "*Panting* S-Slow down a bit..."
    d "*Panting* I-I c-can't..."
    x "*Giggles* Your mouth is asking to slow down, but those eyes rolling back are screaming “fuck me harder, [mc]”..."
    d "*Loud moan* Oh SWEET C-CHRIST..."
    d "This feels... ah-aaaahh... A-AMAZINGGgg..."
    d "Oh my g-god, I'm gonna cum again..."
    d "W-What the fuuuck..."
    x "*Breathless laugh* Yeah..."
    x "Don't stop, [mc]..."
    x "Make her fucking squirt..."
    d "Ahhh..."
    d "AAAaaAAhhhhHHH..." with hpunchsubtle
    dsc "AAAAAAAAAAARHHHHHHHHhhhh..." with hpunch 
    play sound slap1
    play sound3 slap1
    play sound2 squirt
    scene qss60 
    dsc "*Orgasming again* AAAAaaaaAAAAaGGGhhh!!!" with hpunchlong
    play sound rubbody
    play sound6 oily
    scene qss 61
    d "*Panting heavily* O-oohh good Lord..." with dis15
    d "*Panting heavily* T-This one was even more intense than the l-las–"
    play sound whoosh6
    play sound2 slap1
    play sound3 penetration2
    play sound4 debris3
    scene sauna12b
    bla "You don’t give her a single breath. The moment her words leave her lips, you slam back into her, pounding her soaked, overstimulated body like a man possessed."with hpunch
    dsc "G-GGGgghghhh..."with hpunchsubtle
    dsc "*Guttural moan* A-AAaaghhhh..."
    mc "F-Fuck, Dalia, your p-pussy's goddamn heaven..."
    x "J-Jesus, this is insane..."
    x "You guys are {i}made{/i} to fuck..."
    x "*Grinning* It's like having a live porno in front of me..."
    dsc "*Squeals* Nbbbngm-g-ghhh..."
    x "*Giggles breathlessly* Think you can cum again, Dalia? Three times in under five minutes?"
    dsc "I-I... am... YEAH... cum..."
    dsc "Y-Yeeeeesssh..."
    dsc "O-Oooooh [mc]... b-breeeEEAAAk meEEE..."
    x "*Giggles breathlessly* You're one tough girl..."
    mc "Oh, Dalia... I-I'm getting close too..."
    x "I don't think she's gonna last that long, big boy..."
    dsc "Oh my god, n-not ahgain..."
    dsc "N-Not s-so soonnnngh..."
    dsc "Oh my goddd..."
    d "{sc=3}OH MY GODDDddh..."with hpunchsubtle
    d "{sc=5}OOHhhhHH myYYY GGgggoodDDDDhhh....."with hpunch
    play sound7 impactwood
    play sound slap1
    play sound3 slap1
    play sound2 squirt
    scene qss62
    d "{sc=4}*Screaming through another orgasm* AAAaaAAaGGGhhh—!!!" with hpunchlong
    play sound4 squirt
    dsc "G-GGGgghhhh...." with hpunch 
    play sound4 squirt
    dsc "Nnnnng-g-gGG-gGGghhh...." with hpunch 
    play sound2 clothes3oily
    play sound3 ["<silence 0.8>", fallfull] volume 0.8
    scene qss63
    d "*Crawling to the side* E-Enough..." with dis15
    d "*Panting heavily* Enough... p-please..."
    d "*Panting heavily* I-I c-can't... t-take another one w-without my n-nervous system collapsing..."
    mct "Jesus, turning Dalia into a trembling mess is the best sensation in the world..."
    play sound wood2 volume 0.2
    play sound3 chair2 volume 0.33
    play sound2 clothes3b
    scene qss 65
    x "*Straddling you* Don't get distracted, [mc]..." with dis17
    mc "O-Oh, boy..."
    mc "The former Bardot heiress... on my lap."
    show qss 66
    x "Watching you break Dalia like that almost drove me crazy, you know?" with dis14
    show qss 67
    mc "Did it...?"
    show qss 66
    x "You still got any gas left in you, big boy...?"
    show qss 67
    mc "*Chuckles* Why?"
    mc "Getting jealous, Alex?"
    show qss 66
    x "*Snorts* ...Maybe."
    x "Guess you could say that."
    x "I want my turn..."
    show qss 67
    mc "*Teasing* Ohh... do you need some attention too, my princess?"
    show qss 66
    x "The question is, can you even keep up?"
    x "Or are you gonna send me to bed all worked up...?"
    show qss 67
    mc "*Grins* Well, if I must... I think I can make the effort."
    show qss 66
    x "I should warn you, though... I'm not as easy as Dalia."
    x "You’ll have to hold out a little longer if you want to see me finish."
    play sound clothes3oily
    play sound4 oily
    play soundlow wood2 volume 0.2
    show qss 68
    bla "You grip her hips and draw her towards you, the wet, obscene sound of your cock parting her filling the room." with dis2
    x "*Moans* AAaaAAAhhh..."
    mc "O-Ohh, now y-you're asking for a lot, Alex..."
    mc "How long are we talking, exactly...?"
    x "*Breath trembling* H-Hah... maybe... fifteen minutes?"
    play sound2 penetration3
    play sound3 clothes3oily
    scene qss 69
    mc "*Pushing her hips down* F-Fifteen...?" with dis15
    x "*Moans* AAAaaaAAggghh..."
    x "*Breathing heavily* O-Okay..."
    x "*Breathing heavily* C-Christ..."
    x "*Breathing heavily* M-Maybe... t-ten minutes will be enough..."
    mc "Oh g-god, Alex, you're so tight..."
    x "P-Push..."
    x "Push it... deeper..."
    play sound2 penetration3
    play sound3 clothes3oily
    scene qss 70
    x "*Loud moan* AAAAAAAAAaaaaAAAahhhhh..." with dis15
    mc "O-O-Ooohhh, Alex..."
    scene sauna13 with dis2
    bla "Alex completely sinks down onto your cock, still slick with Dalia’s wetness, and starts bouncing on it with a hungry rhythm." with dis12
    x "AAaaAAAAAAggGGHHHHH......"
    x "*Breathing heavily* A-Alright... o-okay..."
    x "*Breathing heavily* P-Perhaps... five minutes will do..."
    x "*Breathing heavily* Y-Yeah..."
    x "*Breathing heavily* F-Five's g-good..."
    mc "Oh J-Jesus, how am I even resisting this..."
    x "O-Oooohh f-fffuuuccckkkk yes..."
    mc "O-Ohhhh, Alex..."
    x "[mc][namelong]..."
    mct "J-Jesus fucking Christ..."
    mct "She's so damn tight..."
    mct "I can feel every inch of her squeezing me."
    mct "Every movement... every bounce... I’m hitting her deepest point..."
    mc "O-Oooohhh, babe..."
    mc "Y-You're incredible..."
    x "*Panting* Y-Yeah...?"
    x "D-Do you like–"
    x "*Deep moan* Mmmmmhhhhhmmhh..."
    x "Aaaahh... fuck... f-fuck me, [mc]..."
    x "*Panting* Give me every inch... I-I want it all..."
    x "*Panting* A-All of you..."
    mc "F-Fuck yes..."
    x "*Panting* Fuck me, daddy..."
    mc "OH FUCK YES..."
    play sound clothes3b
    show qss 71
    d "Y-You called him... d-daddy...?" with dis12
    mc "*Looking towards Dalia* O-Ohh... look who's back..."
    mc "C-Come here and join us, Dalia..."
    x "*Loud moan* AAAaaahhh... yeahh... c-come, baby..."
    x "*Whispering* Let's both play with daddy..."
    mc "I wanna eat you out, Dal..."
    mc "I can make you cum again..."
    mc "If... you can handle it, of course."
    show qss 72
    d "Hmmm..." with dis
    play sound wood2 volume 0.2
    play sound3 chair2 volume 0.4
    play sound2 clothes3oily
    scene sauna14 with dis2
    bla "Completely stripped of any restraint, Dalia slides up and plants herself on your face as Alex keeps lowering herself onto your cock, both their moans getting louder with every movement."with dis12
    mct "OH MY GOD."
    d "*Trembling* H-HOOOLYYY SHIIIT..."
    d "*Moans* AAAaaahhh... aaaaghh... r-right there..."
    mc "MmMmm-mmMmfff..."
    d "O-Ooooohhhh... f-fuck..."
    d "AAAhhhH! GOD..." with hpunch
    mct "This has to be a dream..."
    mct "These perfect girls using me like this..."
    mct "They’re gonna be the death of me... and what a way to go..."
    x "*Gasping sharply* AAAAghh... aahhh... AAAmmmmmmhhh..."
    x "F-Fuck, Dalia, you're such a slut..."
    d "*Choked laugh* Y-You're one t-to talk..."
    scene sauna15 with dis15
    bla "Dalia starts rocking her hips faster, grinding against your mouth, her fingers tangled in your hair as she rides your tongue." with dis12
    d "*Gritting her teeth* MMmmMMMMHHHH... mmmghgh..." 
    d "M-My god, [mc]... you're... s-so good..."
    mct "Good Lord, she tastes incredible..."
    mct "And she’s leaking over me..."
    mct "Jeez, she's gonna need two liters of water after this."
    d "*Moans* AAAAAaahhh... yes... YES..."
    x "*Moans louder* AAAAAAAaAAAhhh... fuuuck...."
    mct "Their moans are so intoxicating..."
    mct "I'm not sure I can last much longer..."
    x "O-Oh [mc]..."
    x "I-I'm getting there..."
    x "I FEEL IT..." with hpunch 
    scene sauna16 with dis2
    bla "Almost in perfect sync, Dalia leans forward as she desperately grinds on your face, as Alex picks up her pace, slamming down against you with wet, heavy sounds that echo through the room."with dis12
    xsc "Oh y-yeah..."
    xsc "OHH FUUUUCK YES..." with hpunch 
    xsc "Oh my god, it feels so f-fucking big..."
    xsc "*Voice breaking* I-It's hitting s-so deep..."
    dsc "Aaahhhh... [mc]..."
    dsc "Yes, RIGHT THERE..."
    mcsc "(OH MY GOD, I'M GONNA CUM...)"
    xsc "I'M... I'M C-CUMMING."
    dsc "Oh my god, m-meeee too..."
    dsc "I'm gonna c-cum AGAIN..."
    dsc "O-Oh my god, this c-can't be healthy..."
    xsc "*Breathless giggle* H-HahhHh... t-this is INSANE..."
    dsc "*Moans sharply* AAAAHhhHH..." with hpunch 
    mcsc "(F-Fuck yeah, cum for me...)"
    xsc "O-Oh shit, OOOH SHIT... I'M GONNA CUM SO HARD..."
    dsc "O-Ooohh god, me too..."
    xsc "OHHhhH yeAAHHH..."
    xsc "AAAAAAGgH..."with hpunchsubtle
    x "{sc=3}AAaaAAAARGGGHHH...." with hpunch
    x "{sc=5}AAAaAAAAaAaaAAAAAGGGGGgGHHhhh..." with hpunch 
    play sound slap1
    play sound3 slap1
    play sound2 squirt
    scene qss73
    x "{sc=6}*Orgasming* AAAAaaaaAAAAaGGGhhh!!!" with hpunchlong
    play sound4 squirt
    play sound5 squirt
    x "{sc=6}*Still orgasming* G-Gg-GGGGgggghhnngh...." with hpunch
    play sound6 squirt
    play sound7 squirt
    scene qss74
    d "{sc=6}*Cumming again* A-AAaaagggnnhh...." with hpunch
    play sound squirt
    play sound2 squirt
    d "{sc=6}*Cumming again* Nnnngggnnn-n-ngh...." with hpunch
    play sound3 wood2 volume 0.3
    play sound4 clothes3oily
    play sound5 oily
    scene qss 75 with dis17
    dbt "*Panting heavily* AAAAaahh... AAaaAAHH... AaaaaHHHH..." with dis15
    dbt "*Panting heavily* P-PPpaapabubbbbaaarrrba..."
    xbt "*Panting* C-Christ..."
    dbt "*Panting heavily* H-Haaaahaa..."
    xbt "*Panting* F-Fuck, I want you to make a mess of me again, [mc]..."
    mc "{bt=3}*Muffled voice* Mmmmhhmmmmyeamhhh..."
    dbt "*Panting heavily* E-Ehh...?"
    play sound8 cumfacial2
    play sound6 debris3
    play sound wood2 volume 0.4
    play sound2 chair2 volume 0.5
    play sound3 fall2
    play sound4 clothes3oily
    scene sauna17 with dis22
    bla "Alex yanks Dalia back by the arm just as you rise to your feet, finally unleashing everything you’ve been holding in for minutes.{w=14.5}{nw}"with dis15
    play sound5 wood2 volume 0.3
    play sound7 clothes3oily
    scene qss76 with dis14
    play sound6 squirt
    play sound8 impactwood
    d "{sc=5}*Orgasming for the fifth time* Mmmm-m-m-m-mgggghh..." with vpunchslow 
    play sound2 squirt
    d "{sc=5}F-FFfffuuuuuUuUuuuckkkkk........." with hpunchslow 
    x "*Panting* W-What the...?"
    mc "*Panting* Ohhh yeahhh, babe..."
    dbt "Ffuuuuuucck..."
    play sound3 wood2 volume 0.3
    scene qss77
    pause 1.7
    play sound fallfull volume 0.55
    stop music3 fadeout 25
    $ renpy.music.set_volume(1.0, delay=25.0, channel='soundloop2')
    d "*Panting heavily* G-Gooood laawaaaaaadd......" with dis12
    d "*Panting heavily* O-Okay..."
    d "*Panting heavily* I-I'm... officially d-done..."
    d "*Panting heavily* C-Congrats. You succeeded. You f-fried my nervous system. I'm... broken..."
    d "*Panting heavily* I'll have t-to drink from a straw f-for the rest of my life."
    play sound2 ["<silence 1.2>", chair2]
    play sound4 clothes3oily
    scene qss78
    mc "*Grinning* You'll be fine, Dal..." with dis14
    mc "*Chuckles* You might wobble for a few hours, but you’ll live. I know you're a tough girl."
    mc "Although, if you ask me... there’s nothing wrong with being that sensitive."
    d "Hmph."
    mc "It's actually one of my favorite things about you... how you can go from a fierce warrior to a melting puddle in ten minutes flat."
    mc "You're fucking incredible, no other way to put it."
    mc "This was... WOW."
    show qss 79
    d "Um..."
    d "Well... t-thank you."
    play sound3 chair2
    scene qss 80
    x "*Still catching her breath* I-I’m sorry, are we just gonna skip over the fact that Dalia came {i}again{/i} just from getting covered in jizz?!" with dis12
    x "That's a superpower I want to learn!"
    show qss 82
    d "T-That's because [mc] broke me! A-And all because of you!"
    d "W-We ended up like this because of you!"
    show qss 81
    x "Oh, please, you loved every millisecond of that breaking process, and you know it..."
    show qss 82
    d "U-Um..."
    d "W-Well... I-I suppose, but..."
    show qss 81
    x "I told you inviting [mc] was a good idea." 
    mc "*Chuckles* You girls are too much."
    play sound chair2 volume 0.7
    play sound2 wood2 volume 0.3
    show qss 82b
    x "*Standing up* And YOU... are the culprit here." with dis17
    x "How does it feel, huh? Going around making every girl with daddy issues fall for you. Must be one hell of a power trip."
    show qss 83
    mc "*Snorts* It feels pretty damn good, not gonna lie."
    mc "But there's no trick, really." 
    mc "I guess falling hopelessly in love with them helps, though. Makes everything... easier. More honest."
    mc "That makes the sex feel {i}way{/i} better too, of course."
    show qss 82b
    x "*Snorts* Ahhh, interesting."
    x "But you've gotta keep ‘em hooked, Romeo. You know that, right?"
    x "You're not gonna have that stamina forever."
    x "What else do you even bring to the table?"
    show qss 83
    mc "Oh, you know... the essentials."
    mc "A protector, a good listener, an occasional therapist, a guy who never skips leg day, and a full-time comedian."
    mc "Basically the full princess treatment package."
    mc "*Whispering* Between us? I think the tattooed girl’s the one who craves that the most. She likes to act all tough, but deep down she's a romantic softie."
    mc "Pure marshmallow."
    scene qss 1
    d "*Laughs* Oh, one hundred percent!" with dis2
    d "The short girl, right?? She's such a cutie pie!"
    x "*Giggles* Fuck off, both of you."
    x "I'm gonna go take a shower to get rid of all {i}this{/i} before I drown in your corniness."
    mc "*Chuckles* I'll go get some cookies in the meantime. I'm starving."
    d "Oh my god, YES! Please, bring me some!"
    mc "Mmm, I can trade you a cookie for a kiss."
    d "*Giggles* Oh my god, you never have enough?! You're so greedy!"
    mc "No kiss, no cookie."
    d "*Laughs* Okay, okay."
    d "Make it two cookies and we'll talk..."
    $ renpy.end_replay()
    stop soundloop2 fadeout 8



label leavingwinterhouse:
    stop soundloop3 fadeout 7
    stop music fadeout 6
    scene black with dis33
    show screen nextday with dis22
    pause
    play soundloop forest2 fadein 2
    $ renpy.music.set_volume(0.4, channel='music3')
    play music3 happy11 fadein 6
    hide screen nextday
    scene qtt 1 
    with dis33
    play sound cardooropen
    x "*Opening the car door* Uhh..." with dis12
    x "Is that... chocolate?"
    n "Agh, really? Don't tell me we left it in there."
    x "Yup. I guess we shouldn’t have blamed Dalia so fast. Turns out she didn’t eat it after all."
    n "Now we owe her an apology."
    n "*Chuckles* Or at least some new chocolate."
    x "*Snorts* I kinda feel like she's gonna choose the latter."
    play sound footsteps4
    scene qtt 2 with dis2
    mc "*Taking a deep breath* Aaaaahh..." with dis
    mct "Man, too bad we gotta pack up and head out already."
    mct "Still, what a weekend."
    if daliaalexsauna:
        mct "And what a night..."
    mct "It almost made me feel like my life was normal again."
    mct "Well... “normal”. As normal as our lives can be."
    if daliaalexsauna or pennysexxmas:
        mct "Didn’t exactly get much rest, but hey, it was worth it."
        mct "{i}So{/i} fucking worth it..."
    play sound stairswood2
    scene qtt 3
    n "Ready to go, [mc]?" with dis15
    show qtt 4
    mc "Yep!"
    mc "Maybe not so excited about diving back into school and chores, but... well, that’s life."
    show qtt 3
    n "And don't forget saving the world."
    n "Next Wednesday, Ulysses HQ, remember?"
    show qtt 4
    mc "*Chuckles* Yes, yes, can’t forget about that."
    mc "Gems of Doom, evil overlords, and our big mission."
    show qtt 3
    n "*Giggles* Good."
    n "Oh, how did the sauna go, by the way?"
    n "I mean, I bet it went well."
    n "Like, Jesus, [mc]. I’m pretty sure you woke up every squirrel, deer, and raccoon in a ten-mile radius."
    scene qtt 4
    if daliaalexsauna:
        mc "W-What?!"
        mc "*Whispering* Y-You could hear us?!"with hpunchsubtle
        scene qtt 4b
        n "*Laughs* No, not really. The host actually did a good job soundproofing this crazy little apocalypse bunker of a house." with dis
        n "But I did catch Alex’s grin when she was heading towards the sauna while I was going upstairs with Penny."
        n "And if I’m good at one thing, it’s reading people."
        n "Thanks for confirming my theory, though."
        show qtt 5
        mc "You and your mind tricks..."
    else:
        mc "What?!"
        mc "W-What are you talking about?!" with hpunchsubtle
        if changermeisterwinmc:
            mc "I literally spent, like, an entire hour in there alone and then I went to sleep!"
            mc "I didn't even make a sound!"
        else:
            mc "Dalia and Alex were in there for, like, an hour, and then they went to bed!"
            mc "I stayed on the sofa all night until I fell asleep!"
            mc "I didn't even step foot in that sauna!"
        scene qtt 4b
        n "*Chuckles* Relax, relax, I was just testing you."with dis 
        n "I actually saw you snoring on the couch when I went to the kitchen in the middle of the night, but... I wanted to make sure too."
        show qtt 5
        mc "Y-You and your mind tricks..."
    if harempath and nancypath and (daliaalexsauna or pennysexxmas):
        scene qtt 4
        mct "It’s insane to think about, but... this woman right here is really the reason all of this is even working somehow." with dis15
        mct "Sure, the fact that our lives turned into a whirlpool of chaos and fights against immortal beings made the whole thing feel less crazy, but..."
        mct "No way in hell I’d have pulled it off without her help."
        mc "...Thank you, Nancy."
        scene qtt 4b
        n "Thank you for what?" with dis
        n "What are you plotting now, young man?"
        show qtt 5
        mc "*Chuckles* You know exactly what I’m talking about. Don’t play dumb."
        mc "You’ve been holding all this madness together. Queen of the madhouse."
        show qtt 4b
        n "I don’t know what you mean."
        n "I just... want everyone to be happy. Especially my daughters. So I nudge, guide, push a little where I think it’ll help."
        n "It's real feelings and connections that hold everything together."
        show qtt 5
        mc "Maybe. But you shouldn’t forget about yourself either."
        mc "{i}I{/i} shouldn't forget."
        mc "Which is why I’m making it up to you next weekend!"
        show qtt 4b
        n "Oh, really...? Now I'm interested."
        n "What are you cooking up?"
        show qtt 5
        mc "That’s a surprise. But let’s just say... I’ve got options."
        mc "Would you prefer a gift... or a romantic date?"
        mc "I know we said this was our last “relaxing weekend”, but I’m sure I can carve out some time just for you..."
        show qtt 7
        n "Mm... how about both?" with dis15
        n "*Playfully* I definitely deserve it, you're right."
        show qtt 8
        mc "*Laughs* Both??"
        mc "*Chuckles* I'm not sure my wallet's ready for both."
        show qtt 7
        n "Tsk, tsk, tsk, oh, [mc]..."
        n "You don’t need to spend a dime to give a girl a special gift or make her feel like she’s on the most romantic date of her life."
        n "*Sighs* I've still got so, sooooo many things to teach you..."
        n "But I'll let you figure this one out. I like surprises too..."
        show qtt 8
        mc "*Chuckles* Alright, seems fair. Challenge accepted."
        show qtt 7
        n "Good. Now come on, hero, help me haul the rest of the luggage."
        n "Let’s see if those biceps are good for more than showing off."
    else:
        show qtt 7
        n "*Chuckles* Anyway... we should start loading the car." with dis15
        n "You know how those two princesses are — if we don’t put some pressure on them, they’ll be primping and packing until next Christmas."
        show qtt 8
        mc "*Chuckles* Yeah, that's so true."
        show qtt 7
        n "Now, would you do me a favor and help me carry the rest of the luggage? I could really use a strong man."
    show qtt 8
    if nancypath:
        mc "At your service, my Queen."
    else:
        mc "Absolutely!"
    if penelopepath and daliapath:
        scene qtt 9 with dis22
        x "Does this bag go into the trunk too, ma'am?" with dis12
        n "Ma'am??"
        n "Oh, please, you don't have to be so formal with me anymore, Alex."
        n "You're part of our family now!"
        n "Just call me Mom."
        x "Uhm..."
        x "I-I will consider it."
        play sound suitcases
        scene qtt 10 with dis27
        p "*Stretching* G-Ggghhh..." with dis12
        p "(J-Jeez, I slept like a log, but I still feel all beaten up.)"
        scene qtt 11
        if pennysexxmas:
            p "(Which... kind of makes sense, considering what happened yesterday.)"with dis12
            if pennyanal:
                p "(...I-I still can't even sit properly.)"
            p "(Hmm, maybe I shouldn't have brought so much useless stuff.)" 
        else:
            p "(Hmm, maybe I shouldn't have brought so much useless stuff.)" with dis12
        scene qtt 12
        p "(But nah... What’s a Christmas if there’s no tree and no ridiculous amount of fairy lights?)"with dis08
        p "(Worth every single suitcase.)"
        scene qtt 13
        d "Hey... Penny, you got a second?" with dis
        show qtt 13b
        p "Huh?"
        p "What's up?"
        show qtt 14b
        d "Can you... uh... come closer?"
        d "I... don't want anyone overhearing."
        show qtt 14
        p "Uhh..."
        show qtt 15
        p "Can't it wait? The others are waiting for us."
        show qtt 14b
        d "It'll only be a minute, I promise."
        show qtt 13b
        p "Um..."
        p "Mmh."
        play sound footsteps3
        show qtt 16
        p "Okay, fine." with dis2
        p "Tell me, what's so urgent?"
        d ". . ."
        show qtt 17
        d "Uh..."
        d "I'm..."
        d "I'm sorry."
        show qtt 18
        p "Huh?"
        p "Sorry...?"
        show qtt 16
        p "For what...?"
        show qtt 17
        d "For how I’ve been acting these last few weeks."
        d "I was... immature, and I..."
        d "I said things I didn't really mean."
        d "I know you'd never hurt me on purpose."
        d "And I... was cruel because I was angry. I was petty. And I was... wrong."
        d "I'm... I'm sorry, sis."
        show qtt 18
        p ". . ."
        p "...Wow."
        p "Dalia Carter apologizing? This truly is a Christmas miracle."
        show qtt 16
        d ". . ."
        show qtt 17
        d "...Yeah, so... that's all I wanted to say."
        d "I understand if you–"
        show qtt 16
        p "Listen..."
        show qtt 21
        p "*Sighs* I’m the oldest. I’m supposed to be the mature one. But I... didn’t handle this well either." with dis08
        p "Like... at all."
        p "And I... said things I didn't mean too."
        scene qtt22
        p "But even during this whole time I was mad... jeez, I couldn’t stand not talking to you."
        p "I missed you being... you. I missed my sister."
        p "So... I-I guess what I want to say is..."
        p "I'm sorry too, sis."
        scene qtt 23
        d "It's all forgiven!"
        d "It was my fault! I just... didn’t know how to be anything but jealous and loud about it."
        show qtt 20
        p "So... friends again?"
        show qtt 19
        d "Best friends!"
        show qtt 22
        p "I might make mistakes in the future, and I... *chuckles* I reserve the right to roast you when you deserve it, but..."
        p "I love you, sissy. And I'll always be there for you."
        p "Please, never forget it."
        show qtt 23
        d "I-I love you too, sis!"
        d "Really."
        d "Thank you for... always being there for me."
        show qtt 24
        p "*Clears throat* Now..." with dis14
        p "About the thing that actually made us snap at each other..."
        p "Have you... thought about..."
        p "...about him...?"
        show qtt 25
        d "Oh... well..."with dis12
        d "About that... y-yes, I have. A lot."
        d "I... actually thought about it for a long time yesterday night."
        d "And I thought..."
        d "Well, the thing is, I know h-he loves us both. And I..."
        d "I think... no, I {i}know{/i} that I love him. And I don't think you love him any less."
        d "*Clears throat* So... I thought..."
        d "L-Like, instead of burning the house down and pretending neither of us wants him, maybe we could, like..."
        d "*Clears throat* Like..."
        show qtt 26
        p "Share...?"
        p "Is that what you're suggesting?"
        show qtt 25
        d "W-Well, when you say it like that it sounds a little bit weird, but..."
        d "Y-Yeah, kinda. Maybe. I guess."
        d "At least... for now. Temporarily. M-Maybe."
        show qtt 26
        p "First apologizing, and now willing to share something?"
        p "Who are you and what did you do with my sister?"
        show qtt 19
        d "*Nervous chuckle* I mean..."
        d "I admit I hate losing. I always have."
        d "But this time, I thought..."
        d "Like... what if nobody has to lose...?"
        d "Maybe this time... we can all win."
        d "Like... if we're all happy with it... where's the harm? Why should anyone get hurt?"
        show qtt 20
        p "Wow... that's wildly mature of you, Dal."
        p "I'm impressed."
        show qtt 23
        d "Well, I had a great big sister to learn from."
        show qtt 20
        p "Honestly, we might all have gone crazy here, but... I was kinda hoping you'd see it that way too."
        p "I'm just... so tired of petty fights. I just want... to be happy."
        p "And you know what? Fuck what other people think."
        show qtt 23
        d "YES!"with hpunchsubtle
        d "FUCK them all!"with hpunchsubtle
        show qtt 20
        p "*Giggles* You look ridiculously happy, Dal. It’s kind of intoxicating."
        show qtt 23
        d "Why wouldn't I be?!"
        d "I get to be with the guy I love and still have my sister’s love!"
        d "LIFE IS GOOD!"
        show qtt 20
        p "Terribly open-minded and mature of you, sister."
        p "I'm proud."
        show qtt 23
        d "Thank you, sissy!!!"
        show qtt 19
        p ". . ."
        show qtt 22
        d ". . ."
        show qtt 19
        p ". . ."
        show qtt 27
        p "...You're thinking of turning this into some kind of twisted competition you can win, are you not?"with dis
        show qtt 28
        d "I can take it harder than you."
        play sound clothes3
        scene qtt 29
        p "*Teasingly* And I can get dirtier than you." with dis15
        p "But... I guess we'll see, SISSY."
        p "We'll see..."
    scene qtt 1 with dis25
    play sound cardoor
    play sound2 ["<silence 0.8>", cardoor]
    n "Alright, is everyone ready to roll?"with dis12 
    p "Coming!"
    mc "There's still a couple of suitcases outside, I think."
    if alexpath:
        x "Come on, [mc], fast, fast! I’ve got swimming training at eight, and my coach will murder you if I’m late."
    else:
        x "Come on, [mc], I’ve got swimming training at eight!"
    d "And I need to be back before seven! The new episode of Aeternitas is dropping today, and I’m watching it live with Annie and Nova!"
    mc "Okay, okay, I get it! I'm on it."
    x "Thank you, soldier!"
    d "You're the best, no doubt!"
    p "Truly the chosen one!"
    mc "*Laughs* You can all shove your sarcasm where the sun don’t shine..."
    stop music3 fadeout 9
    stop soundloop fadeout 12
    scene black with Dissolve(3.8)
    show screen afewdayslater with dis3
    pause 
label ulyssesheistlunachang:
    $ renpy.music.set_volume(1.0, channel='soundloop2')
    play soundloop2 officesound fadein 5
    scene qqq 1 
    hide screen afewdayslater
    with Dissolve(3.8)
    uemp "So, how’s the whole Xenogate mess affecting the numbers lately?" with dis15
    uemp2 "Affecting? Pff, we just hit a new record for concurrent players this Christmas."
    uemp2 "Half the people complaining wouldn’t even care if they couldn’t post about it online. They just throw shade at Ulysses to look supercilious, then hop right back into Eternum."
    uemp "*Laughs* God bless 'em hypocrites."
    $ renpy.music.set_volume(0.7, channel='music3')
    play music3 ulyssesheist fadein 3
    play sound footsteps
    scene qqq 2
    mc ". . ." with dis22
    mct "And... here we are."
    mct "It's been a couple of chill days, but it's time to get back into action, [mc]."
    mct "Location: Ulysses HQ. The one and only skyscraper in all of Kredon towering over twenty floors."
    play sound2 sip
    scene qqq 3
    mc "*Taking a slow sip* (Hmmm...)" with dis17
    mct "We triple-checked everything and we made sure there would be no way anyone could link the credentials back to us, but..."
    mct "Damn, I can’t shake this knot in my stomach."
    show qqq 4
    mct "And I don't even know why, to be honest." with dis12
    mct "Sure, the Founder and William Bardot are real danger, that’s a fact, but the rest of these people?"
    mct "They’re just workers trying to pay rent and survive the week."
    if lunapath:
        mct "I just need to stick to Chang’s plan and in an hour I’ll be sitting across from Luna, enjoying our date together. Easy peasy."
    else:
        mct "I just need to stick to Chang’s plan and in an hour I’ll be sitting in my bed, chilling. Easy peasy."
    play sound3 vibration
    play sound2 vibration
    scene qqq 5
    bla "{sc=1}Your phone buzzes.{/sc}" with dis08
    mct "The signal!"
    scene qqq 6 with dis
    call chat(chang_chat3) from _call_chat_25 
    scene qqq 7
    mct "It's nice to see Chang actually able to help on a mission." with dis08
    mct "I know he's loving every second of this."
    play sound2 sip
    scene qqq 3
    mct "This mission might look like a quick in-and-out on paper, but I can’t get cocky — I need to follow every damn step to the letter." with dis12
    mct "No shortcuts, no slip-ups, no mistakes."
    show qqq 4
    mct "Let's do this."with dis
    play sound footsteps
    scene qqq 8 with dis2
    mc "*Approaching the front desk* Good afternoon, miss." with dis
    mc "I’m here for my interview for the Division Director of Advanced Research position."
    show qqq 9
    uemp2 "Of course! Welcome to Ulysses, sir."
    uemp2 "And congratulations on making it to this stage of the process."
    uemp2 "The scheduled interviews are being held on the 28th floor. Just follow the HR signage once you arrive."
    show qqq 8
    mc "Understood. Thank you so much."
    show qqq 9
    uemp2 "May I see your ID before I grant you access, sir?"
    show qqq 8
    mc "*Handing it over* Naturally."
    play soundloop type2
    show qqq 10
    uemp2 "Alright... this will only take a moment. Please hold on." with dis12
    mct "I hope this works..."
    uemp2 "Just one moment..."
    uemp2 "And..."
    uemp2 "...yes, everything seems to be correct."
    if novapath:
        mct "Heh. My cheeto hacker never misses."
    else:
        mct "Heh. Nova really never misses."
    stop soundloop fadeout 2
    show qqq 11
    uemp2 "Thank you for your patience, Mr. Claimant." with dis12
    uemp2 "You may take the elevators to your right. Security will be expecting you."
    show qqq 8
    mc "Excellent. I appreciate your help."with dis
    stop soundloop2 fadeout 5
    scene qqq 12 with dis25
    pause
    play sound footsteps
    scene qqq 13
    bla "You enter elevator 7."with dis12
    elev "Closing doors."
    play sound elevator
    scene qqq 14 with dis15
    play sound2 elevatoride
    play soundloop elevatormoving
    scene qqq 15
    mct "Hmm, Nancy was right." with dis 
    mct "There are no cameras in this elevator. This is definitely the safest spot for us if we need to talk."
    play sound2 elevatorstop
    pause .5
    play sound3 ding
    stop soundloop
    scene qqq 14 
    elev "Floor 2. Opening doors." with dis
    play sound4 elevator 
    scene qqq 13 with dis15
    pause
    play sound footsteps
    scene qqq 16
    c ". . ." with dis12
    show qqq 18
    mc "Good afternoon."
    show qqq 17
    c "Hello, good to see you."
    show qqq 16
    elev "Closing doors."
    play sound elevator
    scene qqq 19 with dis15
    play sound2 elevatoride
    play soundloop elevatormoving
    pause .5
    $ renpy.music.set_volume(0.0, channel='music3')
    play sound jumpscare3
    play sound2 musicstop
    play sound3 papers
    play music tension3
    scene qqq 20
    c "WHAT THE FUCK, [mc!u]?!" with hpunch 
    stop music3
    mc "W-Wha-what?!" with hpunchsubtle
    mc "What did I do?!" with hpunchsubtle
    c "Didn't you read the memo I sent you?!"with hpunch 
    mc "What?! Yes! O-Of course I did!"  with hpunchsubtle
    mc "I memorized it word for word!" with hpunchsubtle
    scene qqq 21
    mc "W-We’re both interviewing with Ulysses’ Chief Innovation Architect Adrian Powell in his own office!"with dis12
    mc "At the same time, Luna’s gonna be on floor 25 for a separate interview, she’ll trip a fuse near the connection hub, knock out the power, and force Adrian to step out!"
    mc "Then we slip Nova's USB into his computer, and that's it!"
    mc "By the time he's back, we're ghosts! Clean and gone!"
    show qqq 22
    c "And what about your character?! YOUR COVER STORY!" with hpunch
    show qqq 21
    mc "Yeah! That too!"
    mc "I'm Alek Claimant, I graduated at–"
    show qqq 22
    c "Where's your eyepatch, [mc]?!" with hpunch 
    show qqq 21
    mc "Wha–"
    mc "Ohhh... crap, I forgot. I have it here in my pocket."
    mc "Nova gave me one of hers."
    mc "But... now that you mention it, why does my character wear a patch...?"
    mc "Won't that draw unnecessary attenti–"
    show qqq 22
    c "Alek Claimant has no right eye, [mc]!" with hpunch
    c "You don't have to simply act, you need to BECOME him!" with hpunch
    show qqq 21
    mc "But why–"
    show qqq 22
    c "THE PATCH, [mc!u]! THE PATCH!" with hpunch
    show qqq 21
    mc "O-OKAY, OKAY, JEEZ, I'M PUTTING IT ON!"with hpunchsubtle
    mc "DON'T PANIC!" with hpunchsubtle
    play sound risingshort2b
    show qqq 22
    c "THE PATCH!{w=1}{nw}"with hpunch
    play sound6 impact5
    scene changpanic1
    c "BEFORE IT'S TOO LATE!{w=0.6}{nw}"with hpunch
    play sound2 impact5
    scene changpanic2
    c "{size=43}HURRY!{w=0.6}{nw}"with hpunch
    play sound4 impact5
    scene changpanic3
    c "{sc=3}{size=54}HURRY!!{w=0.6}{nw}"with hpunch
    play sound3 impact5
    scene changpanic4
    c "{sc=5}{size=72}HURRYYY!!!{w=0.5}{nw}"with hpunch
    play sound3 impact5
    scene changpanic5
    c "{sc=11}{size=86}AAAAAAAAAARGGGHHH!!!"(multiple=2)
    mc "{sc=11}{size=86}AAAAAHHHHHHHHH!!!{w=1}{nw}"(multiple=2)with hpunchlong
    play sound ding
    stop music
    play music2 ulyssesheist 
    scene qqq 23
    c ". . ."(multiple=2)
    mc ". . ."(multiple=2)
    play sound2 elevatorstop
    pause .5
    play sound3 ding
    stop soundloop
    elev "Floor 14. Opening doors."with dis 
    stop soundloop
    play sound4 elevator 
    scene qqq 24 
    mc ". . ."with dis15
    show qqq 25
    mct "Daaamn..." with dis
    $ unlock_look("luna", 14)
    mct "Luna looks dangerously good in this office outfit."
    mct "Look at those curves..."
    show qqq 26
    l "Good afternoon, gentlemen."
    show qqq 25
    mc "G-Good afternoon!"
    show qqq 26
    l "Are you heading up?"
    show qqq 25
    mc "We are! Come on in."
    show qqq 26
    l "Thank you."
    play sound heels
    scene qqq 27 with dis17
    pause .2
    elev "Closing doors." with dis12
    play sound elevator
    scene qqq 28 with dis15
    play sound2 elevatoride
    play soundloop elevatormoving
    mc ". . ." with dis 
    scene qqq 29
    mc "Daaaamn, Luna!" with dis12
    mc "You look incredible!"
    show qqq 30
    l "Really? Thank you!"
    show qqq 29
    mc "*Chuckles* Now I can finally feel like I'm in one of Chang's heist movies."
    mc "That hair makes you look like a totally different person!"
    show qqq 30
    l "I know, right?"
    l "Penny helped me put this together."
    l "It’s just a wig, though. My real hair’s way too long for this style."
    show qqq 29
    mc "Could’ve fooled me. It looks so natural!"
    if lunapath:
        show qqq 31
        l "You look... very good in a suit too, [mc]." with dis 
        l "Very handsome. You should wear one more often."
        show qqq 32
        mc "Right back at you. You're absolutely killing it in that skirt."
    mc "*Pointing at the paper bag* What's in there, by the way?"
    show qqq 31
    l "Oh, yes!"
    show qqq 33
    l "This is for you, Chang." with dis14
    c "What...? For me?"
    if lunapath:
        l "Mmhm! [mc] and I are going on a little excursion later, so I made some sweets for us both."
        l "But I know we're all supposed to leave this place in a rush, and I didn’t want you to miss out, so I saved some for you too."
    else:
        l "Mmhm! I made some for [mc] and the girls, but I know we're not supposed to meet after leaving this place, so I didn't want you to miss out."
    c "You made these... yourself? For me...?"
    if cmlove:
        l "Yes! They’re filled with cajeta, a type of caramel from my abuela's hometown. There are enough for you to share with Micaela too, if you want!"
    else:
        l "Yes! They’re filled with cajeta, a type of caramel from my abuela's hometown."
    l "Thank you for planning another heist for us!"
    c ". . ."
    c "...Thank you so much, Luna."
    show qqq 34
    l "Oh, we're almost at my floor!" with dis
    l "*Whispers* Good luck, boys!"
    scene qqq 35
    mc ". . ."with dis17
    play sound2 elevatorstop
    pause .5
    play sound3 ding
    stop soundloop
    elev "Floor 25. Opening doors."with dis 
    stop soundloop
    play sound4 elevator 
    scene qqq 36
    l ". . ."with dis15
    scene qqq 37
    l "Good luck with your interview, gentlemen."
    play sound heels
    scene qqq 38
    bla "Luna steps out of the elevator, her heels clicking with quiet confidence." with dis17
    elev "Closing doors."
    play sound elevator
    scene qqq 39 with dis15
    play sound2 elevatoride
    play soundloop elevatormoving
    c ". . ." with dis 
    show qqq 40
    c "...She made Mexican sweets for me, bro."
    c "She said she didn’t want me feeling left out."
    show qqq 41
    mc "I know, that girl must be protected at all costs."
    show qqq 39
    c ". . ."
    show qqq 40
    if lunapath:
        c "If you ever break the heart of that angelic soul, I’m gonna have to kill you."
        c "Hope you understand, bro."
        show qqq 41
        mc "That won't be necessary."
        mc "If I ever hurt Luna, I'd kill myself first."
        show qqq 40
        c "Good."
        c "Glad we're on the same page."
        show qqq 39
        mc "Hmh."
        c "Mh-mh."
    else:
        c "How’d you screw that up, bro?"
        show qqq 41
        mc "I know."
        mc "I know..."
    play sound ding
    stop soundloop fadeout 8
    play soundloop2 officesound fadein 3
    scene qqq 42 with dis3
    bla "Following the plan, you get off at floor 28 and head towards the HR desk." with dis12
    mct "Alright..."
    mct "So far, so good. No one seems to be paying much attention to me."
    mct "Keep it cool, [mc]..."
    scene qqq 43
    mc "*Clears throat* Good afternoon." with dis14
    mc "I’m here for the interview for Division Director of–"
    show qqq 44
    uemp "Yes, we’ve been expecting you, Mr. Claimant."
    uemp "Please, go through the door on your left and wait there with the other candidates."
    uemp "Mr. Powell will be with you shortly."
    show qqq 43
    mc "Thank you."
    play sound footsteps
    show qqq 45 with dis15
    c "*Whispers* Alright, that's it." with dis
    show qqq 46
    mc "*Whispers* I guess they shouldn't see us talking to each other once we're inside."
    show qqq 45
    c "*Whispers* Correct."
    c "*Whispers* Don't forget, from this point on, you’re not [mc] [lastname] anymore." 
    c "*Whispers* Once we're in Powell's office, we need to keep him distracted just long enough for Luna to cut the power. That's all."
    c "*Whispers* Then we slide in the USB and disappear. Clean and simple."
    show qqq 46
    mc "*Whispers* Got it."
    show qqq 45
    c "*Whispers* And remember, Adrian Powell might have a similar role as Alex's dad, but he’s his total opposite."
    c "*Whispers* He's loud, eccentric, and loves to joke around. Even has damn good hair! Complete opposite, I tell you."
    show qqq 46
    mc "*Whispers* No worries bro, I'm ready."
    mc "*Whispers* I read the memo. I got this."
    show qqq 47
    c "*Whispers* That's it!" with dis 
    c "*Whispers* Let's nail this last step of the plan!"
    show qqq 48
    mc "*Whispers* Chang’s Nine roll natural twenties only!"
    show qqq 47
    c "*Whispers* Flawless victory!"
    stop music2 fadeout 10
    scene qqq 49 with dis3
    play music2b heist2 fadein 5
    l ". . ." with dis12
    app ". . ."
    scene qqq 50
    uemp "Mr. Michael Brown?" with dis
    play sound chair2
    show qqq 62
    app3 "*Standing up* Yes, miss." with dis
    show qqq 61
    uemp "And... Ms. Charlotte Nguyen?"
    play sound2 chair3
    show qqq 62
    app2 "*Also standing* Here."
    show qqq 61
    uemp "You’re both here for the Regional Sales Subdirector position, correct?"
    scene qqq 50
    app2 "Yes." (multiple=2)
    app3 "That's right." (multiple=2) with dis12
    uemp "Perfect. Please, follow me to Mr. Robertson’s office."
    uemp "The rest of you, please wait just a little longer, I'll be right back."
    show qqq 51
    l ". . ."with dis08
    show qqq 49
    app ". . ." with dis08
    play sound wood2 volume 0.3
    show qqq 52
    app "*Clears throat* ...Quite unconventional, huh?" with dis12
    app "Do you know why Ulysses always brings people in two at a time for these interviews?"
    show qqq 53
    l "I'm sorry...?"
    show qqq 52
    app "The applicants. They always pair them up in the final rounds. It’s a company policy."
    app "They’re not just evaluating skills, they’re testing how competitive we are."
    app "In short, they don’t want people who play it safe. They want people who {i}fight{/i} for the spot."
    app "Wolves, not sheep, as they say."
    show qqq 53
    l "Ohh... I didn't know that was the reason."
    show qqq 52
    app "*Chuckles* My advice? Don’t hold back."
    app "If you get a chance to outshine your companion, take it. They’ll like that."
    show qqq 53
    l "Oh... I'll keep it in mind."
    l "Thank you for the tip, uhm..."
    show qqq 52
    app "Ian Abelman."
    app "I’m here for the Regional Marketing Manager spot."
    app "Spent over ten years competing against Ulysses’ monopoly, and now here I am, about to join them. Funny how life works, huh?"
    show qqq 54
    l "If you can't beat them... join them, they say."
    show qqq 52
    app "*Laughs* Exactly!"
    app "And tell me, what about you?"
    app "What are you interviewing for? You look very young."
    show qqq 55
    l "Oh, I didn't come for a job." with dis08
    l "I came to get William Bardot."
    show qqq 56
    app "Haha! You mean..."
    app "Like... you're aiming for his position? Ambitious!"
    show qqq 55
    l "No."
    l "I mean murdering him."
    show qqq 56
    app "*Chuckle* Haha!"
    app "Hah..."
    show qqq 57
    app "...Uhm... what...?" with dis08
    show qqq 55
    l "He’s here today."
    l "I've been planning this for months."
    l "I'm going to kill him."
    show qqq 57
    app "Uh..."
    app "W-What are you talking about...?"
    stop music2b fadeout 25
    play soundloop risinglong3 volume 0.8
    scene qqq58
    show qqq59
    l "My parents lost everything because of him. Because of Ulysses." with dis25
    l "They couldn’t carry the debt. And they chose the rope over the silence."
    l "Eternum..."
    l "They call it entertainment."
    l "...I call it a blood cage. A perfect little parasite in our brains."
    l "And Bardot...? *Sinister chuckle* Oohh... he's the personification of evil."
    l "He took {i}everything{/i} from me."
    l "He took my life... and today I'll take his."
    l "And not just him. Anyone who helped build this rotten machine will pay."
    l "Today I’ll write a sentence in blood on every wall of this building."
    l "Today the message spreads."
    play sound impact3
    play sound2 ["<silence 0.6>", impact3]
    play sound3 ["<silence 1.2>", impact3]
    lsc "Ulysses.{w=0.55} {size=50}Will. {w=0.55}{size=66}Burn."
    play sound risingshortbb
    app ". . .{w=0.9}{nw}" with dis
    stop soundloop
    play music2 heist2
    scene qqq 57
    app ". . ."
    play sound chair2
    play sound2 run
    show qqq 60
    bla "The man runs away, bumping people and shoving past chairs." with dis12
    l ". . ."
    play sound2 heels
    play sound dooropen4 
    scene qqq 61
    uemp "Thank you for your patience, everyone." with dis15
    uemp "We will now begin the interviews for the Regional Marketing Manager position."
    uemp "So... Mr. Ian Abelman?"
    scene qqq 60
    l ". . ."
    uemp "*Scanning the room* Mr. Abelman...?"
    l ". . ."
    show qqq 62
    uemp "Hmph."
    show qqq 61
    uemp "...Please, remember that at Ulysses Corp, we uphold a culture of absolute dedication and accountability." with dis08
    uemp "Punctuality is not optional, and we do not give second chances."
    uemp "Uhh... Ms. Mia Smith?"
    play sound chair2
    show qqq 63
    l "*Standing up* Yes." with dis
    show qqq 64
    uemp "You are also applying for the Regional Marketing Manager role, correct?"
    show qqq 63
    l "Correct."
    show qqq 64
    uemp "It appears your scheduled co-applicant has failed to attend. We will proceed with the interview individually."
    show qqq 63
    l "I understand."
    show qqq 64
    uemp "Please, follow me."
    scene qqq 65 with dis3
    mc "*Counting quietly* (Hmm... only twelve people, huh...)"with dis15
    mct "Guess this really is one of the final rounds of interviews."
    mct "Not that it matters, though. By the time they figure out our credentials are fake, we’ll be long gone."
    if lunapath:
        show qqq 66
        mc "*Looking at the clock* (Mmh... it's already one.)"with dis08
        mct "The train I need to take with Luna leaves at two, but if everything goes smoothly, we should be out in thirty minutes tops."
        mct "Hope we don't miss it."
    play sound dooropenclose2
    play sound2 heels
    play sound3 footsteps2
    scene qqq 67
    adr "GOOOOOOOOOOOOOOD MORNING, VIETNAM!" with dis15
    play sound4 footsteps
    scene qqq 68
    adr "Welcome, welcome, you beautiful sacks of ambition!" with dis12
    adr "Thank you all for waiting!"
    show qqq 69
    mct "And that must be the big boss himself."
    mct "Judging by his energy, I can tell Chang wasn't exaggerating — this guy's nothing like Bardot."
    mct "Okay, [mc]. It's SHOWTIME."
    show qqq 70
    adr "Every single one of you poor desperate souls wants the same thing: to join the biggest, most thrilling, and richest company in the entire world — Ulysses Corporation!"with dis
    show qqq 81
    adr "But only ONE can wear the title of Division Director of Advanced Research!"with dis 
    adr "We need new blood. Fresh ideas. And a LOT of determination!"
    show qqq 70
    adr "Do you have what we need?"with dis 
    adr "PROVE IT TO ME!" with hpunch 
    show qqq 70b
    adr "How many applicants are here today, Susan?" with dis12
    show qqq 72
    uemp2 "Twelve, sir."
    show qqq 70b
    adr "Ugh, Jesus... do you people think I have all day?"
    adr "That's at least six interviews."
    adr "*Sighs* But anyway... out of those twelve, how many are women?"
    show qqq 72
    uemp2 "None, sir. All of them are men."
    show qqq 73
    adr "Ah! At last, some good news!" with dis12
    adr "I mean, if what I needed was a latte and a blowjob, I’d simply call my secretary! Am I right??"
    show qqq 74
    app3 "*Awkward laugh* Ha-hah, y-yeah, right."
    play sound impact5 
    scene qqq 75
    adr "No. Not right."
    adr "Here at Ulysses, we respect women and believe in gender equality. What the fuck is your problem?"
    show qqq 76
    app3 "W-What?!"
    app3 "But it's you who said–"
    show qqq 75
    adr "Who the fuck is this one, Claire?"
    show qqq 72
    uemp2 "Toby Anderson."with dis 
    uemp2 "Graduated top of his class in Computer Science at CalTech, with internship experience at Alphabet."
    show qqq 75
    adr "Hardworking women built this company, Toby."with dis
    adr "Here at Ulysses we do not accept sexist behaviour like yours under any circumstance."
    adr "Do it again and I'll tear your resume into shreds and feed them to my koi pond. Do you understand me?"
    show qqq 76
    app3 "B-But I just–"
    show qqq 70
    adr "Alright, enough foreplay! LET'S BEGIN THE INTERVIEWS!" with dis
    adr "Show me what you got, gentlemen!"
    show qqq 70b
    adr "Who are the first candidates, Samantha?"with dis 
    show qqq 72
    uemp2 "Alek Claimant and Roberto Canchez."
    show qqq 68
    adr "Mr. Claimant! Please, stand up!"with dis 
    play sound chair2
    show qqq 77
    mc2 "Yes, sir." with dis12
    play sound snap2
    show qqq 73
    adr "*Snaps his fingers* Ohh, nice eye patch, man."with hpunchsubtle
    adr "Very pirate-chic."
    show qqq 77
    mc2 "Thanks, sir."
    show qqq 78
    adr "And DAMN, you look like you could bench-press my car!"
    adr "What’s your max?"
    show qqq 77
    mc2 "315lbs."
    show qqq 78
    adr "FAAAAAA-huuh!"with hpunch 
    adr "Forget this role, I might just give my job to this young stud!"
    adr "Alright, alright... very promising!"
    adr "*Looking around* And... where is Mr. Canchez?"
    play sound chair2
    scene qqq 79
    c2 "Here, sir." with dis12
    play sound snap2
    scene qqq 81
    adr "*Snaps his fingers* Ahh... nice tie, brother!" with hpunchsubtle
    adr "Long, thick, and elegant like a big cock!"
    adr "Where'd you get it?"
    scene qqq 79
    c2 "Thank you, sir."
    c2 "My mother gifted it to me."
    show qqq 81
    adr "Your mom has class, kid."
    adr "Any self-respecting gentleman should always wear a nice tie."
    show qqq 75
    adr "...Not like fucking Toby." with dis 
    adr "I bet he was too busy posting sexist comments online to even pick out a damn fucking tie."
    show qqq 76
    app3 "What?! What did I do now?!" with hpunch 
    show qqq 70b
    adr "Anyway, let's cut to the chase." with dis 
    adr "Two at a time, in my office. Send two more as soon as the previous ones are back, Kate."
    adr "I'll try to be fast."
    show qqq 72
    uemp2 "Understood, sir."
    play sound5 snap2
    show qqq 73
    adr "*Snaps his fingers* Alright, alright, alright!"with hpunchsubtle
    adr "Let's rock it, gentlemen!"
    adr "Let's leave the women here to gossip and talk about shoes, and let's go do BUSINESS on the men's floor! Am I right??"
    show qqq 78 with dis
    menu:
        with dis
        "Right":
            scene qqq 77
            mc2 "Uh... y-yeah. Right." with dis
            scene qqq 70b
            adr "*Sighs* Carol, explain to me how morons like these sneak past HR screenings." with dis12
            show qqq 72
            uemp2 "I don't know, sir."
            uemp2 "I will ask HR."
            show qqq 71
            adr "Hmph."
            scene qqq 78
            adr "Anyway..." with dis
        "[gr]Not right":
            $ adrianpoints += 1
            scene qqq 77
            mc2 "No. Not right, sir." with dis
            scene qqq 70b
            adr "*Whispering* This one's good." with dis12
            scene qqq 78
            adr "Okay, okay!" with dis
    adr "Enough chit-chat! Please, follow me, my brave soldiers of capitalism."
    c2 "Yes, sir."
    mct "Luna should be starting her interview right about now."
    mct "If we can last fifteen minutes without blowing our cover, we’re golden."
    mct "We just need to avoid getting kicked out before then..."
    mct "Let's do this!"
    stop music2 fadeout 8
    stop soundloop2 fadeout 9
    scene black with dis25
    show screen afewminuteslater with dis2
    pause
    play music2 sneakychang fadein 6
    scene qqq 82 
    hide screen afewminuteslater
    with dis27
    play sound dooropenclose
    bla "Powell leads you down a hallway that could double as a luxury hotel corridor, until he opens a pair of golden double doors at the end of it." with dis14
    mct "Jesus. Fucking. Christ."
    mct "This is his PERSONAL office...?"
    scene qqq 83
    mct "For fuck's sake, he even has a damn pool inside his office."with dis14
    mct "This guy's like, the final boss of ostentation."
    scene qqq 83b
    mct "But there's his personal computer! Nova's USB needs to go in there."with dis14
    mct "We simply need to wait for Luna now."
    scene qqq 83
    mct "Problem is, Powell sounds like he wants these interviews over fast." with dis12
    mct "We need to believe in her now..."
    adr "Sit down, gentlemen!"
    adr "Please, don't be shy."
    play sound chair2
    play sound2 chairmove
    scene qqq 84
    adr "*Reading your resumes* Alright, alright, alright..." with dis17
    adr "You two have some {i}impressive{/i} resumes. Haven’t seen ones this polished since that guy who faked his diploma."
    adr "We ended up bringing up a frivolous lawsuit and landing him in jail."
    show qqq 85
    mc "*Gulps* . . ."
    play sound clothes3
    show qqq 86
    adr "But let’s cut the boring crap, yeah? I don’t care about your GPA or which programming language you dream in." with dis
    adr "I’m here to figure out what kind of people I’m letting into my kingdom."
    adr "So... tell me, do you even know why you’re here?"
    show qqq 88
    mc2 "Uh... here... at Ulysses?"
    show qqq 86
    adr "No. I mean..."
    play sound slam3
    show qqq 87b
    adr "HERE IN MY DAMN OFFICE!" with hpunch 
    play sound2 slam3
    adr "Why would I, Adrian Powell, allow two peasants into my own ridiculous, unnecessarily lavish office instead of just letting HR interrogate you in some sad little cubicle?!" with hpunch 
    play sound3 slam3
    adr "WHY?!" with hpunch 
    mc2 "To... motivate us?"
    play sound snap2
    show qqq 89b
    adr "Exactly."with hpunchsubtle
    adr "To help you see your potential future. To show you what’s waiting for you if you work hard enough. If you’re talented enough. And if you’re lucky enough."
    play sound clothes3
    scene qqq 84
    adr "You’re quick, Mr. Claimant. I like that. Fast mind. Sharp tongue." with dis
    adr "Twenty-one years old and already two degrees?"
    adr "From MIT, no less."
    show qqq 88
    mc2 "Yes, sir."
    mc2 "CS and Artificial Intelligence."
    show qqq 86
    adr "Impressive, impressive."
    adr "Some would say you lack experience, but I say — what’s more impressive? Someone who runs ten miles in forty minutes, or someone who does it in a hundred?"
    show qqq 89
    mc2 "Mm-hm."
    show qqq 87
    adr ". . ."
    show qqq 89
    mc2 ". . ."
    show qqq 86b
    adr "It's a question."
    show qqq 90
    mc2 "O-Oh."
    mc2 "Uh..."
    show qqq 89
    menu:
        with dis
        "[gr]Forty minutes":
            $ adrianpoints += 1
            show qqq 88
            mc2 "The one who does it in forty minutes?"with dis
            play sound snap2
            show qqq 89b
            adr "Exactly."with hpunchsubtle
            adr "Efficiency. Speed. Results."
        "A hundred minutes":
            show qqq 88
            mc2 "The one who does it in a hundred minutes?"with dis
            show qqq 86b
            adr "...What? No. Why would that be more meritorious?"
            adr "He's a damn slow motherfucker."
            adr "The fatso was practically walking."
    play sound7 clothes3
    show qqq 84
    adr "But anyway, what do we have over here..." with dis
    adr "Mr. Canchez! Whoa."
    show qqq 97
    adr "You’re no slouch either, huh? Three languages?"
    show qqq 98
    c2 "Indeed, sir. I'm fluent in English, Russian, and Spanish."
    show qqq 95
    adr "Spanish!"
    adr "What a coincidence!"
    adr "Resulta que pasé un tiempo viviendo en Buenos Aires cuando era joven, viste. Te molesta si seguimos la entrevista en español?" (what_style='textsp')
    show qqq 97
    c2 ". . ."
    show qqq 98
    c2 "Que...?" (what_style='textsp')
    show qqq 105
    adr "AAAAAh! Jesus, my accent's rustier than I thought!" with dis
    adr "Forgive me, that was probably so bad you barely understood what I was trying to say!"
    show qqq 98
    c2 "Y-Yeah, it was pretty bad."
    show qqq 86
    adr "Alright, alright! Enough of my linguistic disasters." with dis
    adr "Time is money, gentlemen, so I'm only going to ask a couple questions to each of you, and I expect complete honesty."
    show qqq 95
    adr "But first! Do you want a drink?"
    adr "Whiskey? Brandy?"
    show qqq 89
    menu:
        with dis
        "Whiskey":
            $ alcoholadrian = True
            show qqq 88
            mc2 "Yeah, I'll have whiskey, thank you."with dis
        "Brandy":
            $ alcoholadrian = True
            show qqq 88
            mc2 "Yeah, I'll have brandy, thank you."with dis
        "[gr]No thanks":
            $ adrianpoints += 1
            show qqq 88
            mc "Uh... no, thank you. I don't drink."with dis
            play sound snap2
            show qqq 89b
            adr "Good man!"with hpunchsubtle
            adr "Alcohol and tobacco are poison! Filth!"
            adr "Only fools dull their edge with that crap."
    if alcoholadrian:
        show qqq 86b
        adr "Tsk. Are you seriously asking for a drink in the middle of a damn job interview?"
        adr "What the hell’s wrong with you, Claimant?"
        adr "Alcohol is fucking poison. Filth!"
    play sound7 clothes3
    scene qqq 84
    adr "Everyone knows {i}real{/i} businessmen only use cocaine anyway. Or microdoses of LSD." with dis
    show qqq 85
    mc2 "W-What?"
    show qqq 84
    adr "Anyway... let's begin!"
    play sound6 clothes3
    show qqq 86
    adr "Mr. Claimant... tell me, how did you end up here at Ulysses?" with dis 
    adr "What's your story?"
    show qqq 89
    menu:
        with dis
        "[gr]Money":
            $ adrianpoints += 1
            show qqq 88
            mc2 "Honestly? Everyone knows Ulysses pays its senior staff more than some countries pay their presidents." with dis
            mc2 "I want that money. That power. The freedom that comes with it."
            mc2 "So I worked my ass off until I was good enough to enter this company."
            play sound snap2
            show qqq 89b
            adr "Hah! I love honesty. No bullshit, no sugarcoating."with hpunchsubtle
            adr "Money runs the world. Everyone wants it."
            adr "Keep your goals updated and your greed healthy and you’ll go far."
        "[gr]Reputation":
            $ adrianpoints += 1
            show qqq 88
            mc2 "Ulysses’ reputation precedes it, sir." with dis
            mc2 "My dream’s always been to work for a company respected across every industry. A place where achievement speaks for itself, with worldwide prestige."
            mc2 "So I studied and trained for years just to get here. The top of the top."
            play sound snap2
            show qqq 89b
            adr "You're not wrong there." with hpunchsubtle
            adr "Flash a business card with a senior title, subtle off-white coloring and a Ulysses watermark, and any table at a five-star restaurant will be yours. Even the ones already taken."
            adr "I like your ambition, kid."
        "Helping the world":
            show qqq 88
            mc2 "Ulysses is everywhere. Entertainment, finance, technology, medicine, energy. A global conglomerate."with dis
            mc2 "I believe that if I climb high enough here, I can actually help steer that power toward something good. Something that makes the world better for everyone." 
            show qqq 86
            adr "Hah! You might’ve walked into the wrong lion’s den for that, son."
            adr "But hey, someone’s gotta believe in something, right? The world needs a few idealists to balance out the sharks."
            adr "Admirable."
    play sound7 clothes3
    scene qqq 84
    adr "Which reminds me..." with dis 
    adr "In your cover letter, you said you’ve been following Ulysses’ expansion for years."
    adr "Obviously, our beloved Founder gets all the fan mail, but..."
    show qqq 86
    adr "What about the senior partners?" with dis
    adr "Did you know me before walking in here?"
    show qqq 89
    menu:
        with dis
        "[gr]Yes":
            $ adrianpoints += 1
            show qqq 88
            mc2 "Of course, sir."with dis
            mc2 "Your trajectory within Ulysses is legendary. I’ve read about your work in several of the company’s major projects."
            show qqq 86
            adr "I see, I see..."
            adr "And what about William Bardot?"
        "No{#ep9,interview}":
            show qqq 88
            mc2 "Uh... I'm sorry, sir. I hadn't heard of you before this."with dis
            show qqq 86b
            adr "Huh... I see."
            adr "Honest."
            scene qqq 86
            adr "And what about William Bardot?" with dis08
    adr "You surely know him. What's your opinion of the man?"
    show qqq 91
    mc2 ". . ."
    show qqq 92
    mc2 "Uhm..." with dis08
    show qqq 93
    mc2 "He's..."
    mc2 "Uhh..."
    menu:
        with dis
        "He's the best":
            mc2 "He's definitely a role model."with dis 
            mc2 "He might not have founded Ulysses, but he elevated it, expanded it globally."
            mc2 "Professionally, I respect him a lot."
            play sound woodhit
            scene qqq 94
            adr "HAHAHA!" with vpunch
            adr "*Laughs* Bardot a ROLE MODEL!"
            show qqq 89b
            adr "*Chuckles* Oh, t-that's rich, kid. Thank you for the laugh."with dis12
            adr "B-But I agree he's a damn genius, that's true. The man would sell his family to a human-trafficking ring if it got him a better interest rate."
            adr "A true white shark."
        "[gr]He's horrible":
            $ adrianpoints += 1
            mc2 "I... actually even had a brief interaction with him once."with dis 
            mc2 "And from that, and what I've read, I'd say he's..."
            adr "Go ahead. Be honest."
            mc2 ". . ."
            mc2 "...I'd say he's a total psychopath. A soulless son of a bitch."
            mc2 "The absolute worst kind of human being."
            mc2 "A monster."
            play sound woodhit
            scene qqq 94
            adr "HAHAHA!" with vpunch
            adr "*Laughs* You've got balls, Claimant!"
            show qqq 89b
            adr "*Chuckles* Y-You really got the old baldy pegged, you son of a bitch. Must have been one hell of an interaction!" with dis12
            adr "Bardot is a damn sociopath. No friends, no empathy, and I'm pretty sure his family's just a prop for photo ops."
            adr "The PERFECT businessman! Gotta love the guy."
    scene qqq 95
    adr "Alright, but enough about Baldy Bardot..."with dis08
    adr "Let's move on..."
    play sound snap2
    show qqq 89b
    adr "—to the math test!"with hpunchsubtle
    adr "How much is 25%% of 40%% of 160?"
    show qqq 90
    mc2 "U-Um..." 
    show qqq 91
    menu:
        with dis
        "[gr]16":
            $ adrianpoints += 1
            show qqq 90
            mc2 "Uhh... 16?"with dis
        "24":
            show qqq 90
            mc2 "Uhh... 24?"with dis
        "32":
            show qqq 90
            mc2 "Uhh... 32?"with dis
        "40":
            show qqq 90
            mc2 "Uhh... 40?"with dis
    show qqq 89c
    adr ". . ."
    play sound7 clothes3
    scene qqq 84
    adr "Uhhh... it's possible. I'm not sure."with dis 
    adr "Numbers are for accountants anyway. I'll check later."
    show qqq 86
    adr "But in any case, I think I’ve got you figured out, Mr. Claimant."with dis 
    adr "Your story’s simple, but direct. Straight to the point. Determined. I like that."
    show qqq 95
    adr "It's Mr. Canchez's turn to answer the same questions now."
    show qqq 96
    mct "Damn it, we're running out of time..."
    mct "If Luna doesn’t cut the power soon, we’re screwed..."
    show qqq 95
    adr "Tell me, Roberto, how did you end up here at Ulysses?" 
    adr "What's {i}your{/i} story?"
    stop music2 fadeout 5
    play music changtrauma fadein 5
    scene changtrauma with dis3
    c2 "February 17th, 2010." with dis14
    c2 "The small Russian village of Tigoryakhovgrad, bordering North Korea."
    mct "What...?"
    c2 "Up until that point, my entire life had been nothing but war."
    c2 "I had fought for causes I didn’t believe in, carried flags I didn’t recognize, and buried brothers whose names I never learned."
    c2 "But when even the echo of gunfire started to feel like home... I left. I deserted. I ran to the edge of the world, to a village no one could find, to be alone. To disappear. To finally... rest."
    c2 "But destiny... ohh... destiny has a cruel sense of humor."
    c2 "Her name was Yuliana. I taught her Spanish. She taught me Russian."
    c2 "And somehow, between broken words and shy smiles... something grew. Something fragile. Something... beautiful."
    c2 "For the first time, life made sense. I was happy."
    c2 "But then... as it always does... fate came to collect its debt."
    c2 "The winter of 2014, the North Korean army declared Tigoryakhovgrad a strategic border zone. There were no warnings. No diplomacy. Only... fire."
    c2 "They didn't ask questions. They wanted no witnesses."
    c2 "The villagers fought back with hunting rifles and kitchen knives. Brave. Foolish. Yet... useless."
    c2 "They burned everything. Old men. Mothers. Children. No one was spared."
    c2 "I'll never forget the screams and the smell of burning flesh."
    c2 "A single ship was docked at the harbor. People were shoving, crying, praying. I was almost aboard... when I heard it."
    c2 "A cry. High and thin. Coming from the local orphanage engulfed in flames."
    mc ". . ."
    c2 "I didn't think. I just moved."
    c2 "I kicked through the burning door and found a baby. Alive, somehow untouched, lying in a cradle of ash."
    c2 "I wrapped him in my jacket, shielded him with my body, and ran. My lungs were fire. My vision... only smoke."
    c2 "I reached the docks. The ship was leaving. Soldiers were closing in."
    c2 "I knew what I had to do."
    c2 "I threw the baby in a perfect spiral like an elite Super Bowl quarterback, right onto the boat, landing safely in Yuliana's arms."
    mct "W-What?"
    c2 "I turned around and raised my hands. Tried to speak."
    c2 "...But they didn't let me."
    c2 "I fell. The cold wood beneath me soaking red. My eyes heavy. My body numb."
    c2 "*Sad chuckle* In the end... war caught up to me."
    c2 "With my last breath, I saw the boat vanishing into the mist."
    c2 "And... I smiled."
    c2 "Because that day, even as I died, I had finally done something right."
    c2 "I saved one life. One boy who would live. Who would see the West. Who would study, dream... and join a big company like Ulysses one day."
    c2 "Or at least..."
    c2 "That's the story my mother Yuliana told me."
    c2 "The story of the man who saved my life and gave me my name."
    c2 "That was the story... of Fernando Canchez."
    play sound risingshortbb
    play sound2 ["<silence 1>", impact3]
    play sound3 ["<silence 1>", impact3]
    scene qqq 99 with Dissolve(1)
    c2 "{size=47}I was that baby." with dis15
    play sound4 risingshortb
    pause .5
    stop sound4
    play music2 sneakychang
    stop music 
    scene qqq 100
    mc ". . ."
    scene qqq 102
    adr "*Sobbing* G-Gg-ggh..." with dis
    scene qqq 103
    adr "*Sobbing* God... what a story."
    adr "*Sobbing* Y-Your namesake was a true hero, Canchez." 
    adr "*Sobbing* He gave his life... for yours. A baby he didn't even know."
    show qqq 104
    c2 "Thank you, sir."
    c2 "I’ve fought ever since to honor his memory and fulfill his dream of me joining Ulysses someday."
    show qqq 103
    adr "You will honor his memory, young man."
    show qqq 102
    adr "I'll make sure of it."
    adr "The memory of Tigoryakhovgrad will prevail as long as we remember it."
    scene qqq 105
    adr "*Clears throat* A-AHEM!" with dis
    adr "J-Jesus! Sorry, gentlemen."
    adr "I usually don't get emotional so easily. Let me just..."
    adr "OOF!" with hpunch 
    play sound clothes3
    show qqq 84
    adr "Alright. ALRIGHT!" with dis12
    adr "Sorry about that."
    adr "Erm... Alright, I guess we—"
    play sound lightstage
    play soundloop clock2 fadein 4
    stop music2 fadeout 14
    scene qqq107
    adr ". . ." with dis04
    mct "YES! Just in time!"
    mct "I knew we could count on Luna!"
    adr "What the hell...?"
    play sound wood2 volume 0.3
    scene qqq 108
    adr "Um... Dorothy?" with dis12
    adr "What the hell is going on? Why did the light go–"
    scene qqq 109
    adr ". . ."
    show qqq 110
    adr "Oh... I-I guess the intercom's dead too." with dis
    play sound chair2
    scene qqq 111
    adr "*Standing up* Forgive me, gentlemen." with dis14
    adr "This... never happens at Ulysses. I have no idea what could have happened."
    show qqq 112
    c2 "It's not a problem, sir."
    c2 "Accidents happen."
    show qqq 111
    adr "Not at Ulysses, they don't. They shouldn't."
    if adrianpoints >= 5:
        $ adrianhack = True
    else:
        adr "But in any case, I suppose we can consider this meeting wrapped up for today."
        show qqq 113
        mc "Wait, what?! That's it??"
        mc "B-But we're still not done!"
        mc "We can... uhm..."
        mc "I-I mean, d-don’t worry, sir, we can wait here if you need to go check what’s happening outside."
        show qqq 111
        adr "That won't be necessary."
        adr "I’ve already asked everything I needed to ask, and I’ve made my decision regarding whom I believe has the potential to move on to the next round of interviews."
        adr "Thank you for your time."
        show qqq 112
        mc "Erm..."
        mct "FUCK."
        mct "Goddammit. We were so close..."
        show qqq 111
        adr "Please take the stairs back down to HR. They’ll assist you with the next steps."
        show qqq 112
        mc "Uh... y-yeah, right."
        mc "...Thank you for the... opportunity, sir."
        jump lunadate09
    adr "Please, stay right here while I go check with my secretary. It’ll just take a moment."
    adr "The interview’s almost over, but I still need to... settle a couple of things before I make my final decision."
    show qqq 112
    mct "Just like Chang predicted... he’s leaving the room himself, trying to keep things looking normal."
    c2 "No problem, sir. We'll be here."
    show qqq 111
    adr "Thank you. I'll be right back."
    play sound footsteps4 volume 0.7
    play sound2 ["<silence 1.5>", dooropenclose2]
    scene qqq 114
    bla "You watch in total stillness as Adrian Powell disappears beyond the door and seals himself out of the room." with dis2
    mc2 ". . ."
    play sound4 debris3
    play sound3 whoosh6
    play sound7 slam3
    stop soundloop
    play music tension2 
    scene qqq115
    c "Okay bro, IT'S TIME."with pr
    c "MOVE!"with hpunch 
    c "He took longer than I thought to leave, so we’ve got, like, forty seconds before the emergency generators kick in!"
    play sound whoosh6
    scene qqq 116
    mc "Already on it!" with pl
    mc "Power source on, USB connected!"
    mc "Nova said we don’t have to touch anything else, right? Just plug the USB, virus does the rest?"
    play sound whoosh6
    scene qqq 115
    c "Yes, that's the plan!"with pr
    c "Hell, are we sure this is actually gonna work?!"
    play sound whoosh6
    scene qqq 116
    mc "If your story about burning orphanages and Russo-Korean wars worked, this can too!" with pl
    mc "Trust Nova!"
    play sound whoosh6
    scene qqq 115
    c "Twenty seconds, bro!"with pr
    c "We gotta bounce, like, NOW!"
    c "How's it going?!"
    play sound whoosh6
    scene qqq 117
    mc "Seventeen seconds remaining!" with pl
    mc "But... fuck, it's stuck at seventeen!"
    play sound whoosh6
    scene qqq 115
    c "We–"with pr
    play sound2 lightstage
    scene qqq 118
    c "OH SHIT."with dis06
    c "Bro, we need to leave!"
    c "NOW." with hpunch 
    play sound whoosh6
    scene qqq 119
    mc "Ten seconds!" with pl
    play sound whoosh6
    scene qqq 118
    c "We don't have ten seconds!" with pr
    play sound2 risingshort2b
    play sound whoosh6
    scene qqq 119
    mc "Seven seconds!{w=0.71}{nw}" with pl
    play sound whoosh6
    scene qqq 118
    c "Six!{w=0.71}{nw}" with pr
    play sound whoosh6
    scene qqq 119
    mc "Five!{w=0.71}{nw}" with pl
    play sound whoosh6
    scene qqq 118
    c "FOUR!{w=0.71}{nw}" with pr
    play sound whoosh6
    scene qqq 119
    mc "THREE!!!{w=0.71}{nw}" with pl
    play sound whoosh6
    scene qqq 118
    c "{sc=3}{size=46}TWO!{w=0.71}{nw}" with pr
    play sound whoosh6
    scene qqq 119
    mc "{sc=7}{size=65}ONE!{w=0.71}{nw}" with pl
    stop music
    play soundloop clock2 volume 0.6
    play sound whoosh6
    scene qqq 120 with pr
    pause
    play sound dooropenclose2
    scene qqq 121 with dis15
    adr "*Mumbling* —whole electrician crew’s getting fired, I swear to God."with dis12
    adr "*Mumbling* This is unacceptable."
    scene qqq 122
    adr "Sorry for the wait, gentlemen!"with dis12
    adr "I assure you this–"
    scene qqq 123
    adr "Huh...?" with dis12
    adr "Hello...?"
    play sound footsteps4
    show qqq 124 with dis15
    play sound2 chair2
    play sound3 chairmove
    adr "Isabella? You there?" with dis12
    adr "Did the two applicants leave? Claimant and Canchez."
    show qqq 125
    uemp2 "Yes, sir. They just passed by the front desk."
    uemp2 "They said they appreciated your time, but... the blackout made them uncomfortable. They felt it showed a lack of professionalism."
    uemp2 "One of them even mentioned, uh... {i}“if they can't even keep the lights on, how are they going to run a company entirely based on being permanently online?”"
    show qqq 126
    adr "You've got to be fucking kidding me." with dis08
    adr "Finally two people who don’t sound like total idiots, and this place decides to fuck me over."
    adr "*Sighs* Agghh..."
    adr "Anyway... send in the next two. I don't have all day."
    scene qqq 127
    uemp2 "Right away, sir."
    show qqq 126
    adr "And... tell that Toby douche to hold an isometric air squat until it’s his turn."
    show qqq 127
    uemp2 "...Understood, sir."
    adr "Hmph."
label lunadate09:
    stop soundloop fadeout 6
    if not lunapath:
        jump ending09
    scene black with dis3
    show screen afewminuteslater with dis22
    pause
    $ renpy.music.set_volume(0.4, channel='soundloop3')
    play soundloop3 town_ambience fadein 5
    hide screen afewminuteslater 
    scene qww 1 
    with dis33
    if adrianhack:
        bla "You and Chang step out of the office, the tension still clinging to the air. Following the plan, you share a quick high-five, and split up without a word."with dis17
        mct "Fuck yes! We actually did it!"
        mct "Nova’s malware is locked in and running!"
        mct "Now all we have to do is wait and watch the data roll in."
        mct "We can finally be one step ahead of Bardot and the Founder."
        mct "Yes... we can do this."
    else:
        bla "You and Chang step out of the office, the tension still clinging to the air. Following the plan, you split up without a word."with dis17
        mct "AAaaagghh... goddammit."
        mct "We were so close..."
        mct "Chang said we had a Plan C, but... still, it feels like we screwed it all up because of me."
        mct "Powell was just too unpredictable. I couldn’t steer him the way I wanted."
        mc "*Sighs* (Guess all I can do now is wait.)"
    play sound thunder fadein 2
    bla "A distant rumble of thunder rolls through the concrete canyons of Kredon’s financial district." with dis15
    mct "Oh boy, another storm's coming. Better pick up the pace before it starts raining."
    scene qww 2 with dis22
    play music2 rainymorning fadein 6
    if adrianhack:
        mct "Because... success or not, I've got something else to focus on right now."with dis14
    else:
        mct "Because... failure or not, I've got something else to focus on right now." with dis14
    mct "I've got a date!"
    mc "Luna!"
    scene qww 3
    l "Mmh...?" with dis12
    play soundlow chair2
    scene qww 4
    l "[mc]!" with dis15
    $ unlock_look("luna", 15)
    if len(looks['luna']) < 16:
        $ looks['luna'] = range(16)
    l "You made it!"
    show qww 5
    mct "Gosh, she looks beautiful."
    show qww 4
    l "So? How’d it go? Were you able to plug the USB in?"
    show qww 5
    if adrianhack:
        mc "Hell yes, we did!"
        mc "Everything worked like clockwork."
        $ luna_points += 1
        play sound beat
        show screen heartbeat
        show qww 4
        l "*Relieved* Really?!" with dis08
        l "Whoa... you guys are the best." 
        show qww 5
        mc "No one suspected a thing. And if Nova’s right, the malware’s buried deep enough that they’ll never trace it back to us."
        mc "All we’ve gotta do now is sit tight and wait."
        mc "I'm sure we'll get some useful info sooner or later."
        show qww 4
        l "Great!"
        l "I was worried something might’ve gone wrong."
        show qww 5
        mc "You handled your part flawlessly. Was it hard to cut the power?"
        show qww 4
        l "Not really! It took me some time to get the interviewer off my back, but the rest was easy."
        l "You guys had the real challenge."
        show qww 5
        mc "Hey, don't sell yourself short!"
        mc "It was a team job, and everyone nailed their part. We couldn’t have done it without you."
        mc "But let's not stay here! Those clouds don’t look friendly, and I don’t feel like getting drenched right after a win."
    else:
        mc "Unfortunately... no."
        mc "Right when the power went out, Powell had already made up his mind and told us to leave."
        mc "We didn't have the chance."
        show qww 6   
        l "*Disappointed* Ohh... really? So... it's my fault, then." with dis12
        l "I’m sorry. I couldn’t cut the power as fast as I planned. The interviewer wouldn’t stop hovering around me, it was hard to get her off my back."
        show qww 7
        mc "What? No! It wasn't anyone's fault! Definitely not yours!"
        mc "I already texted the girls, they’re working on another way in."
        mc "We'll figure something else out, like we always do."
        show qww 6
        l "You sure...?"
        show qww 7
        mc "A hundred percent."
        mc "There's nothing to worry about."
        show qww 4
        l "Well... okay then. That makes me feel better." with dis12
        show qww 5
        mc "In any case, we should find some shelter before it starts pouring on us, though."
    mc "I might not be wearing my suit right now, but I still don’t wanna get my sneakers soaked."
    show qww 8
    l "Do you need to leave that backpack somewhere? It looks quite heavy." with dis14
    show qww 9
    mc "Nah, no worries, it's fine."
    mc "I just have all my gym stuff in there."
    mc "I'm going there after this. It's chest day!"
    show qww 8
    l "Chest day...?"
    l "You're... going to the gym now? By yourself?"
    show qww 11 
    mc "Yeah! But don’t worry, I’ll still hang around for a bit and eat the sweets you made."with dis12
    mc "Do you wanna sit on that bench over there, or... just walk?"
    show qww 10
    l "Uh..."
    l "S-Sure, the... the bench sounds good."
    show qww 11
    mc "You okay?"
    show qww 10
    l "Y-Yeah, I just..."
    l "I-I just thought we were gonna spend more time together today."
    l "I... misunderstood the plan."
    l "...Sorry."
    show qww 11
    mc "Oh..."
    show qww 10
    l "It’s fine, really! If you're in a hurry, I can pack the sweets for you to take to the gym, so you can eat them later."
    l "If you keep them in the tupperware, they’ll stay soft for a few hours and–"
    show qww 11
    mc "*Laughs* Okay, okay, I can't. You're breaking my heart here."
    mc "I'm kidding, Luna. I'm not going anywhere."
    mc "My plan today is to spend the whole day with you and only you."
    show qww 12
    l "...O-Oh." with dis14
    show qww 13
    l "Y-You goof!" with dis12
    l "F-For a second I really thought this date was just gonna be a ten-minute walk."
    show qww 14
    mc "No chance!"
    mc "I need plenty of time to enjoy those delicious sweets you made for me."
    mc "But I’ve gotta say, I just love how even when you thought I was ditching you, you still tried to play it cool."
    mc "You're way too kind for this world."
    show qww 13
    l "*Chuckles* Well, I honestly thought I misunderstood the plan."
    l "Though... yeah, I was a little sad. I’d been looking forward to today."
    show qww 14
    mc "Same here!"
    mc "I've been waiting for this all week!"
    show qww 13
    l "So... tell me, where are we going?"
    show qww 14
    mc "To Kredon's station. We're taking a train."
    show qww 13
    l "Ohhh... I like trains."
    l "Where's it going?"
    show qww 14
    mc "Well, it doesn’t go anywhere, technically. It’s like a round trip."
    mc "It's a themed, vintage-looking train that only runs a few times every year."
    mc "It’s styled after the old ones from the–"
    play sound clotheswhoosh
    play sound2 debris3
    scene qww 15
    l "*Gasps* ARE WE TAKING THE CASCADIAN EXPRESS?!" with hpunch
    show qww 16 
    mc "*Chuckles* Damn."
    mc "Yep, we are."
    show qww 15
    l "Oh my god, I've wanted to ride it for so long!"
    l "How did you know?"
    show qww 16
    mct "Hehe... Annie told me that Luna was talking about how much she wanted to ride that train last week."
    mc "Well, what can I say... I just know you too well, Luna."
    show qww 15
    l "Did Annie tell you??"
    show qww 16
    mc ". . ."
    mc "...Maybe."
    show qww 15
    l "But how’d you get the tickets? They're always sold out!"
    show qww 16
    mc "I got some help from Penny."
    mc "She used her social media connections to pull a few strings and cut in line."
    mc "It’s just the short path, though — about seven hours total. It goes all the way up through Cascade National Park into Canada and back."
    show qww 15
    l "More than enough!"
    l "I'm so excited!"
    show qww 16
    mc "Well, I'm happy to hear that!"
    mc "Although now that the surprise is out, we should probably hurry."
    mc "The train leaves in twenty minutes!"
    show qww 13
    l "Let's go, then!" with dis14
    l "I'd hate to miss it!"
    show qww 14
    mct "It’s crazy how much more open and cheerful Luna’s become around me."
    mct "Seeing her smiling... god, there’s nothing better than that."
    scene qww 1
    l "Come on, [mc], or we're gonna be late!" with dis14
    mc "*Chuckles* Alright, alright, I'm coming!"
    mc "Let's go!"
    stop soundloop3 fadeout 9
    stop music2 fadeout 8
    scene black with dis3
    show screen afewminuteslater with dis2
    pause
    $ renpy.music.set_volume(0.4, channel='soundloop4')
    play soundloop4 trainrain fadein 4
    hide screen afewminuteslater
    scene qww17 
    with dis33
    pause .2
    play music happy19 fadein 2
    cond "May I see your ticket, sir?" with dis15
    pa "Mm-hm..."
    l "Whoaaaa!"
    scene qww 19
    l "We have an entire cabin for ourselves??" with dis17
    l "Like... a whole one? Just for us?"
    show qww 18
    mc "Yep! All ours!"
    show qww 19
    l "Wow..."
    l "This is a dream come true, [mc]."
    l "Thank you so much."
    show qww 18
    mc "Please, it's nothing."
    mc "It’s just a train ride. A special one maybe, but still."
    show qww 19
    l "Special indeed..."
    show qww 18
    mc "Apparently this line used to be a major route, you know? Now they've rebuilt it for tourism, but some people still take it to cross the border for real, not just for the “vibe” like we are."
    show qww 19
    l "Wow, lucky them. I'd love to do this all the time if I could."
    play sound2 thunder fadein 2 volume 0.8
    show qww 18
    mc "I only wish it wasn’t raining this hard."
    mc "The views are supposed to be amazing along some stretches."
    show qww 19
    l "But rain makes it a hundred times better!"
    l "With the sound on the windows and everything... I literally feel like we're riding the Orient Express straight through the Transylvanian forests."
    show qww 18
    mc "*Chuckles* Oh yeah, I forgot you love rain."
    mc "Well, if you feel that way, then I'm happy."
    show qww 19
    l "Maybe, if we’re REALLY lucky, someone gets murdered on the train like in the book..."
    l "Then we'd get to solve the mystery!"
    show qww 18
    mc "Um... I-I think I prefer a murder-free trip."
    play sound sofa
    show qww 21
    l "Seriously, [mc], this is... amazing." with dis15
    l "You're the best."
    show qww 20
    mc "Oh, come on now, you're giving me too much credit."
    mc "Don't hype me up too much or my ego will become unbearable."
    show qww 21
    l "No, but I mean it."
    l "I know how busy you've been lately. Way more than any of us."
    l "I know everyone wants a piece of your time now."
    l "So... the fact that you saved a whole day just for me makes me feel... really special."
    show qww 20
    mc "Oh well, then brace yourself, because I'm planning to save a lot more days just for you, Luna."
    show qww 21
    l "*Soft giggle* Careful, I could get used to that far too quickly!"
    show qww 20
    mc "*Chuckles* I see no problem with that."
    show qww 21
    l "Sorry if it sounds like I'm overreacting, by the way. I'm really not trying to."
    l "It's just that..."
    show qww 24
    l "Well... loneliness and I have walked a long way together."with dis06
    l "So... all of this feels... still kind of new to me, you know?"
    l "You..."
    show qww 21
    l "You mean the world to me, [mc]."with dissolve
    l "More than you can probably realize."
    show qww 20
    mct "Gosh, at this rate she’s really going to melt my heart."
    mc "I love every minute I get to spend with you, Luna. Every. Single. One."
    mc "And I'll forgive you this time, but that was the LAST time you're apologizing for being your true self with me! We've talked about this, miss."
    show qww 21
    l "*Giggles* That's true. Sorry, I forgot."
    show qww 20
    mc "I only want the real Luna, you know that! No filters!"
    show qww 21
    l "I'll be myself, I promise!"
    show qww 22
    l "Except for... maybe my gloves." with dis
    l "That's technically the only “layer” I've got now."
    show qww 23
    mc "*Chuckles* Yeah, fair enough."
    mc "That one gets a pass."
    show qww 22
    l "I wonder though, should I... just take them off...?"
    l "As long as I stay inside the cabin, I should be fine, right?"
    l "It's not like I really need them if it's just you and me."
    show qww 23
    mc "You don't like them? I always thought you preferred wearing gloves."
    show qww 22
    l "I don't mind them. I’ve worn them for so long that it feels totally normal now."
    l "But... every night, when I get home and finally take them off in my room..."
    l "It’s like... my tiny moment of freedom. Like... I’m peeling away a layer that was weighing me down, you know what I mean?"
    show qww 23
    mc "Yeah..."
    menu:
        with dis
        "[gr]Take them off":
            $ lunaglovestrain = True
            mc "I totally know what you mean."with dis
            mc "So... GLOVES OFF! Decided! God blessed me with thick anti-vision skin, and I'm planning to make good use of it."
            $ luna_points += 1
            play sound beat
            show screen heartbeat
            show qww 21
            l "*Giggles* Are you sure? S-Should I?" with dis
            show qww 20
            mc "As long as you want to, then yeah!"
            mc "I wanna see that “freedom” you mentioned shining in your eyes."
            show qww 21
            l "Well... alright then!"
            l "I will!"
            l "Thank you for the encouragement, [mc]."
        "Keep them on":
            mc "I understand what you mean, but... still, it feels a little risky." with dis
            mc "I'd keep them on, just in case."
            mc "You never know."
            scene qww 22
            l "Yeah... yeah, I guess you're right."
            l "It's probably not... worth the risk."
            show qww 23
            mc "Just my advice, though! You can do whatever you want!"
            l "Mmmh..."
    play sound doorsliding
    scene qww 25
    cond "Good evening, folks!" with dis2
    cond "Welcome aboard the Cascadian Express."
    cond "My name's Agatha, and I'll be taking care of you during the trip."
    show qww 26
    mc "Nice to meet you, Agatha!"
    show qww 25
    cond "Will you be getting off at any of the stops, or are you riding the full loop?"
    show qww 26
    mc "We might hop off to snap a picture when the train stops, but yeah, we're doing the full round trip."
    show qww 30
    cond "Perfect! In that case, your tickets include a meal for each." with dis
    cond "Would you like to start with something now, though?"
    cond "Maybe some drinks?"
    show qww 29
    if money >= 11:
        menu:
            with dis
            "[gr]Buy something for Luna":
                $ chocolatetrain = True
                mc "Sure! What do you have?"with dis
                show qww 30
                cond "We've got coffee, tea, juice, hot chocolate, and of course, water."
                cond "And if you want something alcoholic, we have champagne, wine, and–"
                show qww 29
                mc "Heh, thank you, but don't bother."
                show qww 27
                mc "I'm pretty sure I already know what my lady wants." with dis
                mc "We're gonna take two hot chocolates."
                mc "Right?"
                play sound twirlfast volume 0.5
                scene qww28
                l "*Nods* Mmh-mmh."
                mc "*Chuckles* Just like I thought."
                show screen eternals
                show qww 29
                with dis
                play sound coins
                $ money -= 4
                pause .05
                $ money -= 4
                pause .05
                $ money -= 4
                pause .3
                hide screen eternals                                                    
                scene qww 30
                cond "Wonderful. I'll be bringing those right out." with dis               
            "Pass{#ep9,lunabuy}":
                mc "Erm..." with dis
                mc "Could we have two glasses of water?"
                show qww 30
                cond "Of course, sir. I'll be bringing those right out."
    else:
        mc "Um..."
        mct "Dammit, I don't have any money left."
        mc "Erm... could we have two glasses of water?"
        mod "You can go back a bit, cheat money to > 10 to get a Luna point."
        show qww 30
        cond "Of course, sir. I'll be bringing those right out."
    cond "If you need anything else, just call me."
    show qww 29
    mc "Will do. Thank you!"
    play sound2 doorsliding
    scene qww 20
    if chocolatetrain:
        mc "Alright! Hot chocolate incoming!" with dis12
        $ luna_points += 1
    else:
        mc "Alright! Spring water straight from the mountaintops, coming right up!"with dis12
    show qww 21
    l "So perfect!"
    show qww 20
    mc "And now..."
    mc "How about watching a movie while we drink it?"
    mc "I've got my laptop right here!"
    show qww 21
    l "A movie? That sounds good!"
    l "*Gasps* Any horror ones?"
    show qww 20
    mc "*Smirks* Please, do you think I don't know who I'm dealing with?"
    play sound3 sofa
    scene qww 31
    mc "*Sitting next to her* Trust me, you're gonna LOVE this. I've done my research." with dis15
    mc "Have you ever heard of something called... “Carriage 11”?"
    show qww 32
    l "I haven't. But the title sounds quite fitting."
    show qww 31
    mc "Oh, it absolutely is."
    mc "*Reading the premise* A guy takes the same morning train every day, but Car 11 is always empty. One day he decides to sit there... completely unaware of the nightmare he’s about to step into."
    show qww 32
    l "Uhh... that sounds interesting."
    show qww 33
    mc "Right? It's labeled as “Eldritch horror”, and it has a good score." with dis
    mc "It's quite short too, less than 80 minutes, so just in time before we reach the next stop."
    show qww 34
    l "Whoa... you really planned everything out."
    l "I'm impressed."
    if lunaglovestrain:
        scene qww 35
        l "Ohh, it says here it's a Bulgarian movie." with dis12
        mct "Hey, she really took her gloves off!"
        mct "I love seeing her so relaxed."
        l "Should we watch it in the original language?"
        mct "I wonder..."
        mct "Should I... try to hold her hand...?"
        menu:
            with dis
            "[gr]Hold her hand":
                play soundlow sofa
                scene qww 36
                bla "You gently take Luna's hand in yours." with dis12
                mc "Yeah, definitely! Original version, always."
                show qww 37
                l "*Startles* M-Mmh-!" with dis
                show qww 38
                l "Hmm..." with dis12
                $ luna_points += 1
                play sound sofa volume 0.8
                play sound2 beat
                show screen heartbeat
                show qww 39
                l "*Leaning against you* Mmmmmmh..." with dis14
                scene qww 36
                mc "Is that okay?" with dis12
                l "Yeah... absolutely..."
                l "Original version sounds good..."
            "Don't do it":
                mct "Hmm, maybe not now."with dis
                mct "If it was anyone else, I’d be all over it, but with Luna..."
                mct "I don't know, her hands feel... too intimate. I don’t wanna push her out of her comfort zone."
                mct "At least... not right now."
                l "[mc]...?"
                mc "O-Oh, yeah, s-sorry! Original version, yeah! Always!"
                l "Alright then!"
    scene qww40 with dis27
    bla "You and Luna hold each other as the movie’s sound merges with the gentle rainfall tapping at the windows."with dis22
    l "*Happy sigh* Mmmh..."
    stop music fadeout 9
    scene black with dis3
    show screen afewminuteslater with dis2
    pause
    if chocolatetrain:
        scene qww 41 
    else:
        scene qww 41b
    hide screen afewminuteslater
    with dis3
    play musicb sneaky09 fadein 4
    mc "Uhhh..." with dis12
    mc "Sooo... does that mean she's still alive?"
    l "Probably...? Although I think the director wants this to symbolize his spiraling descent into madness."
    mc "Mmh, yeah, that tracks."
    mc "Honestly, something like that would probably happen to me too."
    l "*Giggles* Really?"
    mc "If I saw {i}you{/i} dying like that? Absolutely! I’d lose my mind instantly. You wouldn’t?"
    l "Mmmm... I don't think so..."
    l "I’d just join a necromancer cult and bring you back to life."
    l "In a universe where lovecraftian demons are real, I’m sure there’s at least one witch specializing in resurrections."
    mc "*Laughs* Okay, that sounds very you, yeah."
    play sound sofa
    if lunaglovestrain:
        scene qww 42b
    else:
        scene qww 42
    mc "*Standing up* Hey, can we pause for just a sec?" with dis12
    mc "I gotta pee before the movie hits the next plot twist and I miss something important."
    if lunaglovestrain:
        scene qww 43b
    else:
        scene qww 43
    l "Of course! Go, go!"
    if lunaglovestrain:
        scene qww 42b
    else:
        scene qww 42
    mc "Be right back!"
    if lunaglovestrain:
        scene qww 43b
    else:
        scene qww 43
    l "I won't move from here!"
    if chocolatetrain:
        l "I'll try not to finish the chocolate while you're gone."
    if lunaglovestrain:
        scene qww 42b
    else:
        scene qww 42
    mc "*Laughs* You better not!"
    play sound2 doorsliding
    scene qww 44 with dis17
    mct "Aaahhh..." with dis15
    mct "Man, everything's going so well."
    mct "Maybe it’s the Luna effect, but... yeah, I’m officially a rain lover now. The vibe is just... too magical."
    mct "I can't believe I used to hate it before coming to Kredon."
    scene qww 45 with dis17
    pause
    play sound footsteps4
    scene qww 46
    mct "Mmhh..." with dis14
    mct "Dammit, the bathroom's occupied."
    mct "I swear, it's {i}always{/i} occupied right when you need it the most."
    show qww 47
    mct "Well, let's just hope it doesn't take too–"
    scene qww 48
    mct "Hmm?"
    mct "Hey... is that..."
    mct "No way! That's Noah again! And..."
    mct "Wait... that's not Raul."
    mct "Huh. It almost feels weird seeing those two separated. I think this is literally the first time I’ve witnessed it."
    if anniepath:
        mct "Hold up... isn’t that the same guy I saw at the restaurant with Annie...?"
    else:
        mct "I don't think I've ever seen that other guy before."
    mct "Huh."
    mct "I wonder what they're even talking about..."
    noa ". . ."
    stop musicb fadeout 10
    play music2 mafia2 fadein 10
    scene qww 49 with dis33
    giu "Can I offer you some wine, my friend?" with dis14
    giu "Just a glass to warm the bones?"
    noa "No, thanks. I'm good."
    giu "...Maybe some food then? A cigarette, at least?"
    noa "I'm good."
    giu "Heh..."
    giu "Always so disciplined, Noah. Always... in control."
    noa ". . ."
    play soundloop rain5 fadein 1
    play sound doorsliding
    scene qww 50
    giu "*Opening the window* Aahh.... you hear that?" with dis15
    giu "The rain... {i}madonna{/i}, it takes me back."
    giu "When I was just a reckless kid, I’d spend whole Octobers watching the raindrops race down the glass."
    giu "Me and my dog Nero... sitting on the porch like two old men."
    scene qww 51
    giu "Oh, Nero... what a beautiful dog he was." with dis12
    giu "Strong. Fast. Loyal in a way only an animal can be."
    giu "He guarded the whole villa like it was his kingdom. No fear, no hesitation."
    play soundlow leathershort volume 0.4
    show qww 51b
    giu "And yet..." with dis17
    giu "All that... wild energy took a toll on him in the end."
    play sound zippo
    play sound2 zippo
    scene qww52
    giu "By fourteen he could barely walk." 
    giu "He lost his sight, his control... even his sense of smell."
    play soundlow leathershort volume 0.4
    scene qww 53
    giu "You know they say losing smell is the worst thing that can happen to a dog?" with dis14
    giu "It’s like... taking the world away from them."
    show qww 54
    noa ". . ."with dis15
    show qww 55
    noa "Why are you telling me this?"
    show qww 53
    giu ". . ."with dis15
    giu "...One day, my father took Nero to the old barn behind the villa."
    giu "And he put a bullet in his head."
    giu "Clean. Quick. Painless."
    giu "Then he came home with a new dog. Younger, stronger, full of fire."
    show qww 54
    giu "Oh, how I cried..." with dis15
    giu "I hated the old man that day."
    giu "Swore I'd never forgive him."
    giu "But... time has a funny way of clearing the fog, you know?"
    noa ". . ."
    giu "Many years later... I finally understood."
    show qww 53
    giu "I understood he did the right thing."with dis15
    giu "He was merciful."
    giu "Because, sometimes, mercy looks like cruelty."
    giu "Sometimes... love greets you with a gun instead of a smile."
    giu "Nero had fulfilled his purpose. He’d given everything he had. He’d lived a life."
    giu "And deep down... he was ready to go."
    show qww 54
    giu "So the next generation could rise." with dis17
    noa ". . ."
    giu "Do you understand what I'm saying...?"
    noa ". . ."
    show qww 55
    noa "...Yes. I do."with dis06
    play soundlow leathershort volume 0.4
    show qww 56
    bla "Giuseppe extends his hand to Noah." with dis15
    giu "So tell me... have you made up your mind?"
    giu "Do we have ourselves a deal, amico mio?"
    show qww 57
    noa ". . ." with dis15
    giu "Don’t you think it’s time you step out of someone else’s shadow?"
    giu "And show the world what you're capable of?"
    noa ". . ."
    show qww 58 
    noa ". . ."with dis2
    giu ". . ."
    play soundlow leathershort volume 0.4
    show qww 59
    bla "Noah reaches out and shakes Giuseppe's hand." with dis15
    giu "You made the right choice, Noah."
    giu "Never forget..."
    giu "{i}Il rispetto non si chiede... si guadagna."
    play sound risingshort5b
    show qww59 with dis22
    pause 5
    stop music2
    play soundloop trainnorain
    stop soundloop4
    stop sound
    scene qww 60
    mc ". . ."
    mct "...They're too far for me to catch what they're saying, but I’m gonna go ahead and guess they’re not discussing Mr. Keating’s homework."
    pa "Hey, move!"
    play music sneaky09 fadein 3
    show qww 61
    mc "*Turning around* Huh? O-Oh, sorry, my bad, dude." with dis
    mc "I was waiting for the toilet. These corridors are stupid tight."
    show qww 62
    pa "Yeah, I know, so move the fuck out of the way."
    show qww 61
    mc "*Moving aside* Jeez, chill, man."
    mc "The train's not gonna go faster just because you're speedrunning the corridor."
    play sound footsteps4
    scene qww 63
    bla "The guy storms off without even looking back." with dis14
    mct "Wow, someone woke up with a tree trunk jammed up their ass..."
    mct "But... whatever, no one's gonna ruin my good mood today."
    if not lunaglovestrain:
        stop music fadeout 6
        show qww 44 with dis27
        play musicb happy19 fadein 7
        bla "You finish up in the restroom and make your way back to Luna without running into any trouble."with dis15
        play sound doorsliding
        cond "Hello, guys!"
        jump houselunascene
    mct "G-gGh, I seriously need to pee {i}now."
    scene qww 64 with dis27
    bla "Luna looks out the window quietly, completely absorbed in the view as the train rolls across the bridge." with dis15
    show qww 65
    cond "Ladies and gentlemen!" with dis
    l "Hmm?"
    cond "If you look out the left side of the train right now, you’ll catch one of the best views of Mount Baker on the entire route!"
    cond "Trust me, you don't wanna miss this one!"
    play soundloop2 trainloop fadein 1
    play sound footsteps4
    play sound2 doorsliding 
    show qww 67
    bla "Luna rushes out of the cabin and leans halfway through the open window." with dis15
    show qww 66
    l "WOW..." 
    l "It's so stunning..."
    show qww 67b
    cond "The clouds cleared up just long enough to give us a break from the rain!" with dis15
    cond "Perfect window to see the whole mountain!"
    pa "*Sighs* Hey, excuse me. I can't get through."
    cond "On a clear day, you'd be able to see even the glaciers hugging the ridge of the mountain!"
    l "Woah..."
    play sound slam
    play sound2 slam3
    play sound3 whoosh3b
    scene qww68
    pa "Are you fucking deaf??" with hpunch 
    scene qww 69
    l "O-O-Oh m-my god, I-I'm so sorry!"
    scene qww 68
    pa "What the hell is wrong with you kids??"
    pa "You think you’re the only ones on this damn train?"
    show qww 69
    l "I-I'm really sorry, sir, I didn't hear you over the noise of the train."
    l "I-I swear I wasn't trying to block the way. I-I'm so sorry."
    show qww 68
    pa "*Grumbles* Hmphr."
    play sound ["<silence 0.2>", bodycollide2] volume 0.55
    play sound2 wood2 volume 0.4
    scene qww 70 
    pa "*Pushing her lightly* Fine, fine... just let me through." with dis12
    l ". . ."
    show qww 71
    l ". . ." with dis12
    stop music fadeout 1
    play sound7 visionlunasound
    show lunavision2 with Dissolve(0.2)
    pause 1
    play soundloop uncomfortable fadein 0.5
    stop soundloop4 fadeout 1
    stop soundloop2 fadeout 1
    play sound6 clotheswhoosh
    scene qww72 
    row "Tessa?" with flashfast
    row "The game’s about to start and I can’t find the damn gin."
    row "Did you move it again? You know I can’t watch the game without it."
    tess "R-Rowan! I... I think it's... it's in the cabinet above the sink."
    row "Rowan...?"
    tess "I-I mean... h-honey!"
    tess "*Nervous chuckle* Just give me a second and–"
    play sound paper 
    scene qww73
    row "*Snatching the papers from her* What the fuck are you doing there?" with dis12
    tess "N-No! P-Please, give me that back!"
    row "“Petition for divorce”...?"
    scene qww74
    row "...Really? This shit again?"
    row "I thought we already talked about this."
    tess "I-It's not what it looks like!"
    tess "A friend just sent it to me, I wasn’t going to use it!"
    tess "I-I never–"
    row "Oh... you weren't going to use it?"
    tess "I wasn't! I swear! I just–"
    play sound slap1
    play sound2 slap3
    play sound3 slap3
    play sound6 slap3
    scene qww75
    row "SHUT THE FUCK UP!" with hpunch 
    play sound4 fallfull
    play sound5 impactwood
    scene qww76
    row "Do you think I'm an idiot, Tessa?" with dis12
    row "Are you planning on leaving me and taking all my money with you? After everything I've done for you?"
    tess "*Voice trembling* N-No, of course not! It... i-it even says in the agreement there wouldn’t be any c-compensation!"
    row "You fucking whore..."
    row "I work myself into the ground for this family, and this is how you pay me back?"
    tess "I-I'm so sorry, Rowan, p-please, I-I never meant–"
    row "*Clenching his fists* Oh, you're gonna be sorry, believe me..."
    play sound7 risingshortb
    scene qww76b
    pause 0.4
    play sound6 clotheswhoosh
    stop soundloop
    play soundloop4 trainnorain
    scene qww78 with flashfast
    pause .1
    bla "Luna startles and stands frozen in place." with dis17
    l ". . ."
    scene qww 77
    row "Uhm... are you okay...?"
    row "I barely touched you."
    show qww 78
    l ". . ."
    row ". . ."
    show qww 77
    row "*Muttering* These kids have pure brain-rot, I swear..."
    play sound3 footsteps2
    scene qww 79 
    bla "The man leaves." with dis15
    l ". . ." 
    play music2 sneaky09 fadein 5
    scene qww 44 with dis25
    play sound toilet
    mc "*Coming out of the bathroom* (Aaahhh... much better.)" with dis17
    mc "*Looking out the window* (Hmm? Hey, it stopped raining!)"
    mct "Or... at least we got a break. Fingers crossed it holds until the next stop."
    play sound2 doorsliding
    scene qww 80 with dis15
    mc "I'm back!" with dis12
    mc "Sorry I took forever. Some dude was hogging the toilet like it was his new home."
    play sound3 sofa
    scene qww 81
    mc "*Sitting down* Alright! We can continue the movie!" with dis12
    mc "But hey, before I forget, I was thinking..."
    mc "Do you actually wanna come with us this weekend to the Meiyo mission? The one to find the last Gem of Doom?"
    mc "The others would be hyped if you could join us!"
    mc "And Annie told me there's rumors about a cult doing some {i}really{/i} weird shit there, which is SO your kind of–"
    l ". . ."
    mc "Hey... why... why are you wearing your gloves again...?"
    mc "Luna...? Are you okay?"
    show qww 82
    l "Uh... yeah. Yeah, everything's fine!"
    l "No worries."
    show qww 81
    mc ". . ."
    mc "...Okay, I know you way too well to believe that this “everything's fine” actually means everything is fine."
    mc "What happened?"
    mc "You know you can tell me anything."
    l ". . ."
    stop music2 fadeout 15
    show qww 84 
    l ". . ."with dis
    show qww 83
    l "I... I know I can."
    show qww 84
    mc "So? What's going on?"
    l ". . ."
    show qww 83
    l "Uhm..."
    l "I... just..."
    l "Just... promise me you won't freak out. Or... think I'm crazy."
    show qww 84
    mc "What? I'd never think that."
    mc "You know you can trust me."
    l ". . ."
    show qww 83
    l "Well..."
    l "I..."
    l "I-I accidentally touched someone. With my hands."
    l "And I... had a vision."
    show qww 84
    mc "What?!"
    mc "Where? How??"
    show qww 83
    l "I was checking the view from the other window, and I kinda forgot I wasn’t wearing the gloves."
    l "I was blocking the hallway and someone touched my hand by accident."
    show qww 84
    mc "Oh, shit..."
    mc "Damn, I'm so sorry, Luna."
    mc "Fuck, this is my fault..."
    show qww 83b
    l "It's not! Please, don't say that."
    l "I didn’t even wanna tell you at first because I knew you'd blame yourself."
    show qww 84
    mc "I’m just sorry you had to deal with that again. I know how rough your visions can be for you."
    show qww 83
    l "Don't worry. It’s not the first time, and it probably won’t be the last."
    l "I just need... a minute to pull myself together."
    show qww 84
    mc "Did you..."
    mc "Did you see something... bad...?"
    mc "If you feel comfortable enough to tell me, of course."
    show qww 83
    l "I saw him..."
    l "Angry. And... hurting his wife."
    l "He's... not a good person."
    show qww 84
    mc "Oh, shit..."
    mc "Like... abusing her? Physically?"
    l "Mm-hm."
    mc "Fuck..."
    mct "Damn, poor Luna."
    mct "This must’ve dragged up the worst memories for her."
    mc "What do you wanna do now? Anything I can help with?"
    show qww 83
    l "Nothing."
    l "There's nothing I can do about my visions. They can't be avoided."
    l "So... it's better to just try to forget about them."
    scene qww 84
    mc "I see..."
    menu:
        with dis
        "Let's forget about it":
            mc "Well, in that case... let's try to forget about it."with dis
            mc "Just... together this time."
            mc "Yeah, maybe there are things in this world we can’t avoid. But even then..."
            mc "You don’t have to face any of it alone."
            mc "You can always find a shoulder to lean on."
            mc "I’m your shoulder, Luna. Now, and always."
            play music happy19 fadein 6
            play sound sofa
            scene qww 87
            l ". . ." with dis17
            show qww 88
            l "Thank you, [mc]."
            l "That... really makes me feel better. Much better."
            jump noavoidtrain
        "[gr]Try to stop the vision from happening":
            $ lunavisionavoid = True
            mc "Maybe we can... actually try to stop the vision from happening?"with dis
            show qww 83b
            l "We can't. I've tried everything before, and..."
            l "Visions are just... carved in stone. The future can't be changed."
            show qww 84
            mc "Well, you also thought you couldn’t touch anyone with your hands without triggering a vision... until you met me."
            mc "Maybe I can change your visions if I'm involved somehow too."
            mc "Think of me as... fate's natural counter!"
            l "Hmm."
            play sound sofa
            play music2 quirky09 fadein 6
            show qww 86
            l "Hmmmhh..."with dis17
            show qww 85
            l "It's... true my power doesn't work on you."
            l "I had totally lost hope when that happened."
            show qww 86
            mc "Right? Don’t tell me this is not worth at least trying too."
            show qww 85
            l "But... what could we even do?"
            l "It felt like what I saw was really close. Maybe even today."
            l "Going to the police won’t do anything. We don’t have proof, and... they’d be too slow anyway."
            show qww 86
            mc "Hmm..."
            mc "Maybe we can try... having a little “chat” with him."
            show qww 85
            l "A chat? As in... intimidating him?"
            show qww 86
            mc "More like... giving him a scare."
            mc "No violence."
            mc "Just... you know, one of those “jokes” you and your dad love so much."
            mc "The ones that nearly killed Annie and me a few times."
            show qww 85
            l "Ohh..."
            l "Do you... do you really think that could work?"
            show qww 86
            mc "It's worth a shot!"
            mc "Worst case, we can still go to the police after."
            show qww 85
            l "And... what should we do exactly?"
            show qww 86
            mc "Uhm..."
            mc "Well, I was kinda hoping you would handle the creative side."
            mc "You've always been way better at it than me."
            show qww 90
            l "Hmmm..." with dis
            show qww 89
            l "I... might have some personal info about him that could scare him."
            show qww 90
            mc "Nice! That's what I'm talking about!"
            show qww 89
            l "And... I still have the wig I used at the Ulysses offices. I could easily turn it into extensions."
            l "And maybe with the picnic blanket..."
            show qww 90
            mc "Extensions...?"
            show qww 89
            l "Hmm..."
            l "Do you know if there's any long tunnel on the route?"
            show qww 90
            mc "A tunnel?"
            mc "Um... I think there's one right before the next stop, yeah."
            mc "Why?"
            l "Hmmmph..."
            stop music2 fadeout 8
            jump avoidtrain
        "Call the police":
            $ lunavisionavoid = True
            mc "Well..."with dis
            mc "Maybe you can’t stop the things you see in your visions from happening, but that doesn’t mean we can’t do something about what you saw."
            play sound sofa
            show qww 85
            l "We... can...? What do you mean?"with dis17
            show qww 86
            mc "You said you saw him mistreating his wife, right?"
            show qww 85
            l "...I did, yes."
            show qww 86
            mc "Maybe we can reach out to her."
            mc "She might be too scared to ask for help herself."
            mc "Did you get a name? Anything we can use?"
            show qww 85
            l "...I did, actually."
            l "His name was Rowan, and hers was... Tessa."
            show qww 86
            mc "Oh, that's perfect!"
            mc "I'm sure that’s more than enough for Nova to track them down."
            mc "Don’t worry, Luna."
            mc "We’ll find her. We’ll help her. And we’ll make sure that bastard never lays a hand on her again."
            play music happy19 fadein 6
            show qww 87
            l ". . ."with dis12
            show qww 88
            l "...R-Really? You think that could actually work?"
            show qww 87
            mc "Of course!"
            mc "We can’t do much from here, sure, but once we’re back home? We’ll take care of it. Together."
            mc "Trust me."
            mc "Your vision might've just saved someone!"
            show qww 88
            l "Okay... t-that sounds really good!"
            l "Thank you, [mc]."
            l "That really made me feel better. A lot better."
label noavoidtrain:
    show qww 87
    mc "Ahh, that’s the real smile I love seeing on your face."
    show qww 88
    l "It is!"
    l "You always know exactly what to say."
    show qww 87
    mc "You shouldn't be afraid of your power, Luna."
    mc "It's part of who you are."
    mc "It makes you... {i}you{/i}. Someone incredible in a world that’s already insane enough."
    mc "Don't hide that real you from it."
    show qww 88
    l "I'll try."
    l "Thank you so much, [mc]."
    show qww 87
    mct "Phew..."
    mct "Crisis avoided."
    mct "For a second there, I thought I’d lost Luna’s smile again."
    mct "Bet the guy who bumped into her was the same jackass I talked to in the bathroom..."
label noavoidtrain2:
    play sound doorsliding
    scene qww 125 with dis12
    cond "Hello, kiddos!"with dis
    cond "Is everything alright?"
    show qww 124
    mc "All good, ma'am, thanks!"
    jump houselunascene
label avoidtrain:
    scene qww 91 with dis33
    pause 
    play sound whoosh9
    stop soundloop4 fadeout 2
    $ renpy.music.set_volume(0.5, channel='soundloop3')
    play soundloop3 traintunnel fadein 1
    scene qww92 
    bla "The train enters a tunnel." with dis
    row ". . ."
    play sound2 flicker
    scene qww93
    pause 1.4
    row "(Mmh... assuming nothing decides to break down today, I should actually make it in time for the game.)"with dis12
    row "(Just one day without delays. All I'm asking.)"
    play sound2 flicker
    scene qww93
    pause 2.3
    scene qww 95
    row "(Huh... so much for the whole “vintage experience” thing.)"with dis12
    row "(Feels like the wiring in here needs a good update.)"
    scene qww 92
    row "(At least thanks to the annual pass I’m not paying extra to use this crap.)" with dis12
    play sound2 flicker
    scene qww93b
    pause 2.3
    row ". . ."with dis14
    scene qww 96
    row "(Seriously...?)"with dis12
    play music2 t09creepy fadein 8
    $ renpy.music.set_volume(0.3, delay=15, channel='soundloop3')
    scene qww 93
    row "*Exhales* (What a fucking piece of junk.)"with dis12
    row "(And of course, there’s zero signal down in this cra–)"
    row ". . ."
    scene qww 96
    row "(Where the hell is this music coming from...?)" with dis
    play sound laughscary
    bla "A low, sinister laugh cuts through the silence."
    play sound3 chair2
    play sound4 wood2 volume 0.4
    scene qww 97
    row "W-What the fuck...??" with dis15
    row "Hello?!"
    row "*Muttering* What is going on here?"
    show qww 98
    row "*Muttering* This has to be some kind of prank."with dis12
    row "Uhm... yeah, I did NOT sign up to be thrown into some creepy-ass escape room, thank you."
    show qww 99
    row "HELLO?! Anyone?"with dis12
    row "You can turn off the creepy ass music!"
    row ". . ."
    show qww 98
    row "I swear to god, I'm gonna–" with dis12
    play sound deception
    play sound2 impact3b
    scene qww 100
    row ". . ."
    row "W-Wha..."
    scene qww 101
    row "W-What the FUCK?!" with dis15
    show qww 102
    row "W-What the fuck do you think you're doing, you freak?!" with hpunch 
    row "Hey! Do you hear me?!" with hpunch
    show qww 101
    row "ANSWER ME!" with hpunch
    l ". . ."
    row "F-Fuck no."
    show qww 102
    row "Nope. F-Fuck this. I'm so fucking done."
    show qww 99
    row "HEY! ANYBODY THERE?!" with dis
    row "This isn't funny!"
    row "T-There's a..."
    show qww 102
    row "A thing in h–"with dis 
    show qww 97
    row ". . ." with dis15
    row "*Hyperventilating* O-Okay... I'm SO fucking done for real now."
    show qww 103
    row "Fuck this shit." with dis14
    row "F-Fuck this shit so mu–"
    l "*Whispering* Are you late for the game, Rowan...?" with dis14
    play sound fallfull
    play sound2 impactwood
    play sound3 whoosh6
    play sound4 impact3
    play sound5 impact3
    play sound6 clotheswhoosh
    scene qww104
    row "{sc=3}AAAAAAGHGHHHhhH-HHHh FFFUUUCK!!!" with hpunchlong4
    row "{sc=2}W-WHAT THE FUCK?!"with hpunch 
    row "{sc=2}Who the hell are you?! H-How... how do you know my name?!"with hpunch 
    show qww 105
    l "Oh... I know all about you, Ro-ro."with dis14
    l "I can smell the rot of your sins on you."
    show qww 104
    row "WHAT?!"with hpunch 
    row "I haven't done anything!"
    show qww 105
    l "You haven't...? Is that the story you tell yourself?"
    show qww 104
    row "W-What...? I-I haven't done shit!"
    show qww 105
    l "Really...?"
    l "Would Tessa say the same?"
    show qww 104
    row "W-Wha... what...?"
    show qww 105
    l "I know."
    l "Every scream she swallowed. Every bruise you hid. Every threat that came out of your filthy mouth."
    l "Did you think the dark would keep your secrets...?"
    show qww 104
    row "H-H-How..."
    row "H-How do you..."
    show qww 105
    l "It's time to go, Rowan..."
    l "We'll be playing together from now on."
    l "Just you and me."
    show qww 104
    row "N-NO! WAIT!"
    row "I-Is all this b-because of Tessa?!"
    row "I-I won't touch her again! I swear! I-I fucking swear!"
    show qww 105
    l "More broken promises. More empty words..."
    show qww 104
    row "N-NO! Not this time! I mean it!" with hpunchsubtle
    row "I-I swear on my soul!" with hpunchsubtle
    play soundloop2 scaryaura fadein 0.5
    play sound whoosh6
    play sound2 fallfull
    play sound3 slam3
    scene qww107
    lsc "YOUR SOUL...?" with vpunchslow
    lsc "You think you still have one...?"
    scene qww 108
    row "{sc=2}AAGhHh!!! Y-yes! I DO!" with hpunch 
    row "{sc=2}And I can prove it! I won't touch her again!" with hpunch 
    play sound7 laughscary
    scene qww 107
    l "*Laughs* Aaahhh..." with dis14
    l "Now that sounds tempting..."
    l "Almost {i}too{/i} tempting..."
    play sound wood2 volume 0.6
    play sound2 clothes3b
    play sound3 leathershort volume 0.4
    scene qww109b with dis2
    bla "Luna drifts closer, her hands close enough for her to feel him tremble without touching his skin." with dis2
    l "But... if we’re to make a deal, Rowan, the rules must be spoken plainly."
    l "Don't you think...?"
    row "{sc=4}*Trembling* A-A-hah..."
    lsc "You will go home."
    lsc "You will sign the divorce papers."
    lsc "You will leave."
    lsc "And you will never see her again."
    lsc "Not once."
    lsc "Not in this life."
    row "{sc=4}*Trembling* I-I-I w-will do a-as you say!" with hpunch 
    lsc "Oh, believe me... I truly hope you fail."
    lsc "Because... if you break one rule..."
    lsc "A single one..."
    lsc "If you let the very thought of seeing her even cross your mind..."
    play sound7 impact3
    scene qww109bb
    lsc "I will come back." with hpunchsubtle
    play sound3 impact3
    play sound6 impact3
    scene qww109bbb
    lsc "{sc=3}I will peel you open from the inside." with hpunchsubtle
    play sound7 impact3
    play sound5 impact3
    play sound4 impact3
    scene qww109bbbb
    l "{sc=4}And I’ll ram every one of those gin bottles you love so much straight into your hole, one by one, until the shards turn your guts to soup." with hpunchsubtle
    row "{sc=6}. . ."
    lsc "Do you understand the terms..."
    play sound7 impact2
    play sound3 impact3
    scene qww109bbbbb
    l "{sc=6}{size=45}ROWAN...?" with hpunch 
    play sound wood2 
    play sound2 clothes3b
    play sound4 footsteps4
    stop soundloop2 fadeout 9
    stop music2 fadeout 10
    scene qww 110
    row "{sc=2}*Crawling back* Y-Y... Y-YES!" with dis2
    row "{sc=2}I-I U-UNDERSTAND!" with hpunch 
    row "{sc=2}I-I'll do as you say! J-Just... d-d-don't kill me!"with hpunch
    row "{sc=2}P-P-PLEASE!" with hpunch 
    row "{sc=2}*Hyperventilating* . . ."
    play sound whoosh9
    stop soundloop3 fadeout 2
    $ renpy.music.set_volume(0.5, channel='soundloop3')
    play soundloop4 trainnorain fadein 1
    scene qww111
    bla "The train exits the tunnel." with dis
    row ". . ."
    scene qww 112
    row "H-Huh...?" with dis12
    show qww 113
    row ". . ."with dis12
    row "*Muttering* O-Oh god..."
    row "*Muttering* H-How the fuck... did she know..."
    row "U-Uhm... I-I'll do as you ask, spirit!"
    row "I swear on my soul!"
    bla ". . ."
    play sound chair2
    play sound2 run
    scene qww 114
    bla "With panic still overtaking him, the man sprints back toward his carriage, stumbling into anyone unlucky enough to be in his path." with dis15
    row "MOVE ASIDE!!!" with hpunch 
    scene qww115 with dis3
    play music happy19 fadein 4
    bla "You and Luna slip back into your cabin, as she immediately stuffs the wig and the prank clothes out of sight before anyone can notice."with dis17
    l "Oh my god."
    l "Oh my GOD, [mc], it worked!"
    scene qww 116
    l "[mc]! Did you see that?! It actually worked!" with dis15
    show qww 116b
    mc "*Chuckles* (I hardly ever see Luna this excited.)"
    mc "(Not for nothing, though. Seeing that guy completely freak out when she named things she couldn’t possibly know was wild.)"
    mc "(I never doubted her powers, but seeing them hit someone like that... it was shocking to say the least.)"
    mc "(Another reminder that Eternum and the “real world” are tangled together in ways none of us imagined, I guess.)"
    mc "(Who would've thought “magic” was real just a few months ago...)"
    show qww 116
    l "W-We... we used my powers for good!"
    l "It really worked!"
    play sound clothes3
    scene qww 117
    mc "*Grabbing her waist gently* Of course it did. Didn't I tell you?"with dis15
    show qww 118
    l "You did..."
    show qww 117
    mc "Think he’ll actually stick to his promise, though?"
    show qww 118
    l "I think so!"
    l "His eyes really were terrified."
    l "And if what I saw in my vision was really supposed to happen today... there's no way he'll just shrug this off."
    show qww 117
    mc "Nice! An amazing success then."
    mc "I'm so happy to see you smiling again."
    show qww 118
    l "It's all thanks to you!"
    show qww 117
    mc "*Snorts* Please, I literally just put on music and messed with the carriage lights."
    show qww 118
    l "But you pushed me."
    l "You... you always know exactly what to say, at the exact moment."
    show qww 117
    mc "You shouldn't be afraid of your power, Luna."
    mc "It's part of who you are."
    mc "It makes you... {i}you{/i}."
    mc "Someone incredible in a world that’s already completely insane."
    mc "Don't hide that real you from it."
    show qww 118
    l "I'll try..."
    l "Thank you, [mc]."
    show qww 117
    menu:
        with dis
        "[gr]Kiss her":
            $ lunakisstrain = True
        "Don't push it":
            mct "God, I want to kiss her so badly, but... maybe it's not the right moment."with dis
            mct "I wouldn't want to ruin such a nice moment by making her think I'm a perv or something."
            jump noavoidtrain2
    play sound clothes3
    scene qww 119
    bla "You lean forward as Luna responds to your advance, meeting you halfway." with dis2
    l "Mmmmh..."
    $ luna_points += 1
    play sound clothes3oily
    play sound2 beat
    show screen heartbeat
    scene qww 120
    bla "Her arms slip around your neck, pulling you closer, and for someone usually so gentle and shy, she kisses you with a heat that almost knocks the breath out of you." with dis2
    mct "W-Whoa..."
    mct "Where did this playful tongue come from...?"
    mct "Luna Hernandez..."
    l "Mmmmmmmhhh...."
    cond "*Clears throat* A-Ahem."
    play sound whoosh3b
    play sound2 chair1
    play sound3 sofa
    scene qww121
    mc "*Pulling away from Luna* D-Damn!" with hpunch 
    mc "W-When did you enter?!"
    scene qww 122
    cond "I-I'm so sorry, I didn't mean to interrupt."
    scene qww 121
    mc "N-No, it's fine."
    scene qww 123
    mc "W-We were just... uh... well, kissing."with dis12
    l ". . ."
    mc "Because... uhm... we... wanted to."
    l "Mm-hm."
    scene qww 121
    mc "A-Anyway, can I help you? Ma'am...?" with dis
    mct "What shit timing..."
    show qww 125
    cond "Oh, no worries!"
label houselunascene:
    scene qww 125
    if lunaglovestrain:
        cond "I'm just here to give you a heads-up — we're about five minutes away from our next stop."
    else:
        cond "I'm just here to give you a heads-up — we're about five minutes away from our next stop." with dis17
    cond "We’ll be parked there for about thirty minutes before the train keeps moving again, so you’ll have a little window to stretch your legs."
    show qww 124
    mc "Ohh, already? That was fast!"
    show qww 125
    cond "If either of you are into spooky stuff, this is the perfect place to get a photo of the Brown House."
    cond "We won’t pass by here again for about three hours, when we're already on our way back, so now’s your shot."
    show qww 124
    mc "We definitely will, thanks a lot!"
    play sound doorsliding
    scene qww 85
    l "Spooky stuff...?" with dis14
    show qww 86
    mc "*Smirks* I didn't tell you because I wanted it to be another little surprise."
    mc "There’s an abandoned house like ten minutes from the station. Total local legend. Supposedly haunted as hell."
    mc "Kinda like that one we saw on the way to your uncle's! Just... without the killings. It even showed up in an episode of “America’s Most Haunted”!"
    show qww 88
    l "*Gasps* No way! That is so cool!"with dis08
    l "And we actually have enough time to go there?"
    show qww 87
    mc "Yeah! If we head straight there, we’ll have enough time to look around and snoop a bit."
    show qww 88
    l "This is so awesome!"
    show qww 87
    mc "I knew you'd like it."
    play sound2 sofa
    scene qww115
    l "*Standing up* Alright, let's go! Where's the exit?" with dis15
    mc "We still have some time left! What about the movie?"
    l "We can finish it later! We need to be the first ones off this train. What if someone else gets to see the ghosts before us?"
    mc "U-Uhm..."
    mc "W-Well, I–I mean... I’m pretty sure there aren’t actual ghosts. It’s just a creepy old house with a reputation."
    l "Maybe the souls of a dead family couldn't reach Eternum when they died, so now they’re stuck in that house, wandering forever..."
    mc "Why do I feel like I'll end up regretting this..."
    stop soundloop4 fadeout 8
    stop music fadeout 7
    stop musicb fadeout 7
    scene black with dis3
    show screen sometimelater with dis2
    pause
    $ renpy.music.set_volume(0.5, channel='soundloop3')
    play soundloop3 forest fadein 4
    scene qaa 1 
    hide screen sometimelater
    with dis3
    play sound3 owl volume 0.8
    bla "You and Luna step off the train and into the deserted rural station. You follow the narrow path towards the old estate grounds, still flooded from the recent rains." with dis25
    play sound water5 volume 0.6
    play sound2 footsteps3
    scene qaa 2
    mc "Uhhh..." with dis2
    mc "Looks mysterious indeed."
    l "It does... too bad we don't have time to explore it properly."
    mc "Yeah... too bad."
    mct "Thank god."
    play sound4 water5 volume 0.6
    scene qaa 3
    mct "Hmmm..." with dis17
    mct "This place is completely isolated. Just a recently reopened train track and nothing resembling a village for at least twenty miles."
    mct "And it’s not the only one. This whole region is dotted with houses like this, standing alone in the middle of nowhere."
    play music2 happy19 fadein 4 volume 0.6
    if harempath:
        mc "Hmm."
        mct "It kind of makes me dream... how nice it would be to move to a place like this someday. All of us, together."
        mct "A bunch of dogs running around. Maybe even a cow or two."
        mct "And nothing to worry about..."
    scene qaa 4
    pa "Hey, stand over there! Let's take a picture!" with dis12
    pa2 "Hell no!"
    scene qaa 5
    pa "*Laughs* Oh, come on, it'll be fun!"
    show qaa 6
    pa2 "It's not fun at ALL."
    pa2 "Why did we even come here in the first place? We could've stayed on the train like normal people."
    show qaa 5
    pa "*Laughs* Are you scared of the ghosts...?"
    show qaa 6
    pa2 "S-Shut the FUCK up and let's go back!"
    show qaa 5
    pa "Come on, just one picture!"
    show qaa 4
    pa2 "I said no!"
    pa2 "Let's go back before the train leaves!"
    pa "Okay, okay, jeez..."
    pa2 "This is the worst date ever!"
    mc ". . ."
    show qaa 7
    mc ". . ." with dis 
    scene qaa 8
    l "*Muttering* Look at all this dirty water... If someone wanted to hide a body, it would take like two seconds to make it disappear..."
    mc "Um..."
    mc "Hey, Luna, do you want a picture with the house?"
    scene qaa 9
    l "Oh my god, yes, please!" with dis12
    play soundlow water5
    scene qaa 10
    bla "Luna trots to the front of the house and poses with the excitement of a kid meeting their favorite superhero." with dis17
    show qaa 11
    l ". . ."with dis
    show qaa 12
    l "Is this good?"
    show qaa 11
    mc "*Smiles* It's perfect."
    mct "She really has a gift to turn even the creepiest places into pure sugar."
    mc "Don't move!"
    scene qaa 13 
    hide screen heart
    with dis12
    play sound zoomout
    scene qaa 14 with dis03
    play sound zoomin
    scene qaa 13 with dis03
    pause
    play sound2 zoomout
    show qaa 14 with dis04
    mc "Okay!"with dis
    mc "The lighting is actually so good!"
    mc "{i}You{/i} look so good."
    show qaa 15
    l "Really?"
    l "Then we should take a picture together!"
    show qaa 14
    mc "Yeah! Too bad that other couple left already."
    mc "Let's ask them later!"
    show qaa 15
    l "Sounds good!"
    show qaa 14
    mc "Let me take one of you first, though..."
    mc "You look way too cute to waste this moment."
    mod "You can spam photo button after this until dialogue changes."
    show screen cameraphonebutton1 with dis08
    pause
    scene qaa 15 
    l "Did you get it?" with dis08
    show qaa 14
    if lunapicclicks >= 1:
        mc "I think so! The perfect shot."
        mc "You make it easy, to be honest."
    else:
        mc "Yeah... almost."
        mc "There's something that still feels a bit off, not sure what..."
        mc "Do you mind if we take another angle?"
    jump continuescenepics
label cameralunaclick2:
    show screen cameralunaclick
    $ enoughpics = False
    show qaa 15
    l "*Giggles* Oh come on! How many pictures have you taken?" 
    show qaa 14
    mc "Sorry. The model's just too good."
    mc "You're gonna have to get the phone out of my hands."
    play sound beat
    show screen heartbeat
    show qaa 15
    l "*Laughs* Stop! Your phone's gonna run out of memory." with dis
    show qaa 14
    mc "Worth it!"
label continuescenepics:
    $ enoughpics = False
    play sound thunder
    scene qaa 16
    l ". . ."with dis12
    mc "Oh shit. That sounded close."
    show qaa 17
    l "I think it is."
    show qaa 16
    mc "Maybe we should head back to the train before–"
    stop music2 fadeout 9
    play music2b quirky09 fadein 3
    play soundloop rain5 fadein 1
    play soundloop2 rain2 fadein 1
    scene qaa 18
    l ". . ."with dis15
    mc "...Shit."
    play sound thunder fadein 2
    play sound2 water5
    scene qaa 19
    hide screen cameraphonebutton1
    show screen heart
    l "W-What should we do?"with dis2
    mc "F-Fuck–let's run to the house!" 
    mc "M-Maybe we can find something to cover ourselves with on the way back!"
    l "O-Okay!"
    mc "Let's run!"
    play sound3 ["<silence 0.6>", doorold]
    stop soundloop fadeout 6
    stop soundloop2 fadeout 6
    $ renpy.music.set_volume(1.0, channel='soundloop3')
    $ renpy.music.set_volume(1.0, channel='soundloop4')
    play soundloop3 rain3 fadein 3
    scene qaa 20 with dis27
    bla "You and Luna run up to the porch. The front door to the abandoned house creaks open on its own, forced open by the wind, and you slip inside with Luna close behind."with dis17
    mc "G-Ggggghhhh, it got cold so fast."
    l "I-I know."
    play soundlow rub fadein 1
    show qaa 20b
    mc "*Rubbing your hands* Well..."with dis12
    mc "This place is obviously abandoned, yeah, but there's still plenty of crap lying around."
    show qaa 20
    mc "Maybe we can find an umbrella, or... I don't know, anything we can use to get us to the train without dying of pneumonia."with dis12
    scene qaa 21
    mc "What do you think? Should we–" with dis12
    l "W-Wow, I got drenched so fast..." 
    scene qaa 22
    mct "Damn..." with dis15
    mct "Luna's back game is severely underrated..."
    mc "You... uh... y-yeah, you definitely look drenched."
    l "I’m gonna try to dry my skirt a little."
    show qaa 21
    mc "S-Sure. Take your time." with dis
    l "Give me a minute!"
    stop soundloop3 fadeout 6
    play soundloop rain5 fadein 2
    scene qaa 1b
    mc "I’ll... go check around for something we can use to get back."with dis17
    l "Isn't it cool how we walked into the haunted house and didn't even think about the ghosts?"
    mc "I WAS TRYING NOT TO THINK ABOUT THAT, THANK YOU."
    l "*Giggles* Sorry."
    stop music2b fadeout 8
    stop soundloop fadeout 8
    scene black with dis3
    show screen afewminuteslater with dis25
    pause
    hide screen afewminuteslater
    play soundloop2 rain3 fadein 5
    scene qaa 23b 
    with dis3
    bla "You both spend a few minutes poking around the house while you wait for the rain to stop, finding nothing but dust and rotting floorboards." with dis2
    play sound switch
    scene qaa 23
    mc "Hmm?" with dis 
    play soundlow thunder fadein 3
    mc "Oh, hey, the old generator still works!"
    play sound stairswood2
    scene qaa 24 with dis2
    mct "Huh, there's actually some old furniture down here." with dis14
    mct "I am honestly kind of surprised this place hasn't been completely trashed by junkies yet."
    mct "Although... yeah. Middle of nowhere, crappy access, probably zero cell signal."
    mct "Guess it kinda makes sense."
    scene qaa 23
    mc "*Turning around* (Funny how this place doesn't feel scary at all, though.)" with dis15
    mct "Like... a goddamn abandoned house in the woods that's actually famous for recording EVPs and ghost bullshit...?"
    mct "I might have never been super jumpy, but damn, I feel like past me would be freaking out right now."
    scene qaa 25
    mct "Either I've just seen too much weird stuff in Eternum by now, or... it's just Luna that makes everything feel casual and cozy." with dis15
    mct "I feel like we could be in a cemetery at night, and she'd still be chilling."
    play sound7 thunder fadein 2 volume 0.5
    mc "*Snorts* (She really should have been there when I was running from that burned woman in the Red Herring server.)"
    mct "Oh man, I feel like I've lived a hundred lives since then..."
    l "*From upstairs* I found something we can use to cover ourselves on the way back!"
    mc "Oh, sweet!"
    mc "Coming up!"
    play sound2 footsteps
    scene qaa 26 with dis15
    mc "Huh...?" with dis
    mct "What is that?"
    play sound noise3short
    scene qaa 27
    bla "You pick up an old mask, covered in dust." with dis12
    mct "Hey... I remember seeing this on that one episode of “America's Most Haunted”. The one with that Native burial ground."
    mct "Guess they just left it behind when they were here."
    mc ". . ."
    mc "Hmm..."
    mct "Heh."
    mct "This could be my chance. Payback for every single time Luna has jumpscared me."
    mct "God knows Alex and her have had this coming for a while now."
    mct "Yeah..."
    mct "Yeah, okay. LET'S DO IT. Before the train leaves."
    play sound2 runsit
    scene qaa 28 with dis12
    bla "You put on the mask and press yourself against one of the basement walls, hiding out of sight." with dis 
    mct "Knowing Luna, there's a good chance she's not even gonna flinch when I try to scare her, but it's worth a try."
    l "*From upstairs* [mc]? Is there anything interesting down there?"
    play sound7 thunder fadein 2 volume 0.4
    play sound5 wood2 volume 0.4
    scene qaa 29
    mc "Luna! What the... OH MY GOD, you HAVE to see this!" with dis12
    mc "You're not gonna believe it!"
    l "Believe what?"
    mc "I... I-I don't know, there's like a..."
    mc "Uhhh..."
    mc "Wait, what the hell is tha–"
    mc "*Faked, choked scream* AA-AaGHh–!!"with hpunch 
    play sound impactwood
    bla "You punch the wooden wall, making it sound like you fell." with hpunchslow
    mc ". . ."
    bla "You stay completely silent."
    mc ". . ."
    mct "Yes..."
    mct "Come, come..."
    mc "*Mischievous grin* (Finally, it's table-turning tim–)"
    scene lunascare09 with dis2
    play sound2 ["<silence 2>", whoosh9]
    play sound3 ["<silence 3.95>", jumpscare4]
    play sound7 ["<silence 3.95>", jumpscare4] volume 0.5
    pause 5
    play sound thunder
    play sound5 slam
    play sound4 whoosh6
    play sound6 fallfull
    scene qaa30
    mc "{sc=7}{size=42}AAAAAAAAAAAAAAAGGHH!!!"with pl 
    mc "{sc=4}{size=36}W-WHAT THE FUCK!!!??" with hpunch 
    play sound2 wood2 volume 0.4
    scene qaa 31
    mc "*Panting* S-S-Sweet J-Jesus, w-what the hell, Luna?!" with dis17
    mc "T-That was actual witchcraft!"
    l "*Laughs* S-Sorry, I didn't realize it would work so well."
    l "I know it's usually my dad who loves to scare you, but I couldn't resist."
    mc "H-How the hell did you even teleport behind me?! Are we in Eternum right now and no one told me?!"
    l "*Laughs* There's a trapdoor on the other side of the basement."
    l "*Laughs* I saw the masks and thought it’d be funny to surprise you. I guess we had the same idea."
    mc "*Laughing with her* Goddammit, you nearly killed me."
    mc "Jeez... I guess at this point I should just accept that I’ll always be the one getting jumpscared. I officially give up."
    l "*Laughs* You should have seen your face!"
    mc "*Chuckles* You’re really having a grand old time at my expense, huh?"
    mc "I don’t think I’ve ever heard you laugh this much."
    show qaa 32
    l "...O-Oh." with dis
    play sound noise3short
    play sound2 clothes3b
    show qaa 33
    l "*Taking off the mask* S-Sorry about that." with dis15
    l "I didn't want to be... annoying or anything."
    show qaa 34
    mc "What? No! I didn't mean that in a bad way!"
    mc "I {i}love{/i} hearing you laugh."
    show qaa 33
    l "I just... I-I mean, I know I have a weird laugh. The kids at school used to tell me all the time."
    show qaa 34
    mc "What?? Those dumbass kids were a bunch of morons."
    show qaa 33
    l "I actually tried to hold it back for so long when I was little that in the end it became kind of automatic."
    l "But... I thought it was a good thing. I didn't want people to think I was... weirder than I already am."
    show qaa 34
    mc "You're not weird, Luna."
    mc "Like, not the bad kind of “weird” you're thinking of."
    mc "Maybe the cool kind. Like me! *Laughs* Like all of us, honestly."
    mc "Being weird is cool. Being normal is boring."
    show qaa 36
    l "I... I know you believe that." with dis15
    l "But I just want to say..."
    l "I know you’ve been telling me over and over lately to be myself, to stop hiding everything I feel, and..."
    l "And I'm trying, but... I'm also kind of scared I'll overdo it."
    l "And now that I’m spending more time with friends, especially someone as outgoing as Penny..."
    l "I just... wanted to apologize if I seem to act differently."
    l "Or if I seem... well, yeah. Weirder."
    show qaa 35
    mc "You {i}are{/i} acting differently lately."
    mc "You're brighter. You're laughing more. You're letting yourself be happy."
    mc "But trust me, you’re still the same Luna I met at the start. Sweet, kind, and adorably weird."
    mc "And I don't want any of that to change, ever."
    l ". . ."
    mc "You’re everything that’s right with the world."
    mc "Te amo, Luna."
    show qaa 37
    l ". . ." with dis12
    mc ". . ."
    mc "Um..."
    mc "T-That means {i}I love you{/i}, right...?"
    l ". . ."
    mc "Please tell me I didn't fuck it u–"
label ga_luna3:
    if _in_replay:
        play soundloop2 rain3 fadein 3
    play sound clothes3
    play sound2 bodycollide volume 0.4
    scene qaa 38 
    bla "Luna suddenly leaps forward and kisses you, cutting you off mid-sentence." with dis15
    mc ". . . !"
    $ renpy.music.set_volume(0.9, channel='music3')
    play music3 ["<silence 3>"]
    queue music3 lunasexsong fadein 8
    play sound3 rubclotheslong
    play sound4 thunder fadein 3 volume 0.5
    scene qaa 39
    if lunakisstrain:   
        bla "You wrap your arms around her and return the kiss with deep passion — this time, with no one around to tear the moment away." with dis2
    else:
        bla "You wrap your arms around her and return the kiss with deep passion." with dis2
    stop soundloop2 fadeout 45
    l "Mmm-mmmhhh..."
    mct "God, she tastes so good..."
    l "Mmmmmm..."
    play sound5 wood2 volume 0.25
    play sound6 clothes3
    scene qaa 40 with dis22
    mc "*Helping Luna stand up* Oh, wow..."with dis15
    mc "I must admit, I really did not expect you to be the one to kiss me this time."
    l "I... well, I-I just felt like I wanted to."
    l "Like... if I didn't do it, I would spend the rest of the day wishing I had."
    mc "Well, I'm very glad you listened to that feeling, then."
    mc "Is there anything else you want to do?"
    scene qaa 41
    l "You mean... now...?"
    mc "Mmh-hm..."
    l "Uh... well..."
    l "Maybe we could... kiss a little more...?"
    show qaa 40
    l "I want to... kiss you and... feel you with... my hands."
    mc "*Soft chuckle* Oh, I think that is an excellent idea..."
    play sound ["<silence 0.8>", footsteps]
    play sound2 clothes5
    play sound3 chair2
    play sound4 wood2 volume 0.5
    scene qaa 42 with dis2
    bla "You toss your jacket and hoodie aside and lift Luna into your arms, as she slowly glides her hands over your chest." with dis12
    scene qaa 43
    mc "So? How does it feel?"
    show qaa 44
    l "It feels... so nice. J-Just like last time."
    l "You are always so warm."
    l "So... hard. So... s-strong."
    show qaa 43
    mc "No visions of my traumatic future?"
    show qaa 44
    l "Nothing. Just you."
    l "Just... this."
    show qaa 43
    mc "You know... people have told me I have pretty thick skin."
    mc "Maybe that makes it harder for your power to get through."
    mc "Who knows, maybe if we keep kissing long enough, you will finally see something."
    show qaa 45
    l "*Giggles* Mmm-hmm." with dis
    show qaa 45b
    if lunavisionavoid:
        mc "I know you don't really enjoy your visions, but now that we know we can actually change what you see, we could really use it."
        mc "Knowing when Thanatos might attack me next time could be really useful."
    else:
        mc "I know you don't really enjoy your visions, but knowing when Thanatos or Bardot might attack me next time could be really useful."
    scene qaa 45
    l "*Giggles* Hmm."
    scene qaa 45b
    mc "Would you like to try?"
    show lunanodbasement
    bla "Luna nods, slow and playful."
    scene qaa 45b
    mc "Ahh, was hoping you'd say that..."
    play sound ["<silence 1>", couchlouder]
    play sound2 sofa
    play sound3 rubclotheslong
    play soundloop kissing fadein 2
    scene lunass1 with dis22
    bla "You settle onto the mattress beside Luna, pulling her close as you resume your kiss."with dis15
    mct "God..."
    mct "How I have missed her touch..."
    l "*Softly* Mmmmhm..."
    mct "I still can't believe she was the one who took the initiative earlier."
    mct "She might still be the same shy girl I met months ago, but... the girl I met back then would never have dared to do that."
    mct "Old Luna jumping straight into a haunted house where a dead kid was spotted? Sure. But first the barn in Ekabar, and now this? Nah... these ones are on me."
    l "*Moans* Mmhmmmm..."
    mct "She might be the most unique girl I have ever met."
    mct "Unique... and perfect at the same time. Like a diamond."
    mct "Rare, delicate, and impossible to replace."
    mct "And she's all mine..."
    stop soundloop fadeout 1
    play sound4 sofa
    scene qaa 47 
    bla "Your lips trail away from hers until they reach her neck as your fingers toy with the fabric of her top, wet from the rain still pouring relentlessly outside." with dis2
    play sound clothes5 volume 0.5
    scene qaa 48 
    l "*Soft moan* A-Aah..."with dis2
    play sound2 sofa
    play sound3 rubclotheslong
    play soundloop kissing fadein 2
    scene lunass2 with dis2
    bla "You shift your weight and lean over her once more, caressing her soft skin as the kiss between you deepens."with dis14 
    l "Mmhhm..."
    mct "Oh yes..."
    l "*Breathy* Mmmhmmm..."
    mct "God, she's so fucking hot..."
    mct "Her body, her face, her little soft moans..."
    mct "She completely drives me crazy. And she probably has no idea what she does to me."
    mct "The moment her lips touched mine, I was already hard as a rock."
    mct "I feel like I could spend hours just kissing her like this if my pants weren't about to explode..."
    l "*Needy moan* Mmmhhh..."
    mct "I love how desperate she sounds..."
    mct "She wants this as much as I do."
    l "*Kissing you deeply* MMmmmhh..."
    mct "I want all of her..."
    stop soundloop fadeout 2
    play sound sofa
    scene qaa 49
    mc "*Stopping to breathe* Are you not cold, Luna?" with dis15
    l "Me...? Not... not really, no."
    l "I feel... pretty warm, actually."
    mc "*Smirking* I see, I see..."
    mc "Must be your Latina side kicking in. Your dad's blood did you a big favor."
    l "*Soft giggle* Maybe."
    mc "Then you wouldn't mind if I helped you take these off, would you...?"
    mc "Turns out the [lastname] Massage Parlor is running a very exclusive special today."
    l "*Giggles* Oh wow, lucky me..."
    mc "Is that a yes, then...?"
    l "Well..."
    l "I would be lying if I said I left... unsatisfied last time..."
    play sound rubclotheslong2
    scene qaa 50
    bla "You slowly ease Luna's pantyhose down inch by inch." with dis25
    mc "Dear Lord..."
    mc "Are you even aware of the body you have, Luna?"
    l "*Quiet breath* Aah..."
    l "Do I...?"
    mc "Yes, you do..."
    mc "What kind of exercises do you do to maintain this?"
    l "Uhm..."
    l "I'm... not sure. I barely ever go to the gym."
    mc "Pure genetics, then? This should be illegal."
    l "*Soft laugh* You're exaggerating."
    mc "Not at all! If anything, I'm coming up short."
    mc "Just... allow me to appreciate it properly."
    play soundloop kissing fadein 2
    play sound rubclotheslong2
    play sound2 sofa volume 0.6
    scene lunass3 with dis25
    bla "With the pantyhose finally out of the way, you gently spread Luna’s legs and move the fabric of her panties aside just enough as you begin to massage her."with dis12
    l "*Moans* Mmmhm..."
    mct "I'm not sure why, but the way she trembles every time she touches my skin like this drives me insane."
    mct "The way she kisses me... how she grabs my face almost frantically..."
    l "*Needy* Mmm-mmmhh..."
    mct "And those sounds..."
    mct "God..."
    l "*Broken moan* Mm-mMmmhh..."
    mct "Not to mention how wet she is."
    mct "Ohh yes, I can feel how much she wanted this too..."
    mct "Guess I was not the only one getting worked up from all that kissing."
    l "Mmmhh..."
    mct "Although..."
    mct "I feel like she's hungry for more than just surface teasing..."
    $ renpy.music.set_volume(0.7, delay=20.0, channel='music3')
    play sound3 rubclotheslong2
    play soundloop2 wettingslow fadein 1
    scene lunaftimefingersi 
    with dis2
    show screen lunaanglefingers
    bla "You gently insert two fingers into her, her body tightening for a moment before melting back into you."with dis15
    l "*Moans louder* MMmmhmMm!"
    mct "Oh yes, that's it..."
    mct "Looks like I wasn't wrong..."
    l "*Breathless moan* Mmmmmmhhh..."
    mct "It's like she can't stop kissing me. Or even touching me."
    mct "My god, I love this girl..."
    l "Mmm-mMMMmmhhh..."
    mct "But..."
    mct "As hard as it might be, I don't really wanna rush things."
    mct "God knows I want to go all the way with her, but... we can do it whenever she's ready."
    mct "I want her to feel safe."
    l "*Moans louder* MmmMmmmMhhH..."
    mct "Still..."
    mct "At the very least, I need to make her cum all over my hand again."
    mct "I {i}need{/i} to see those eyes roll back one more time..."
    bla "You curl your fingers just right, slowing down for half a second before pressing deeper, deliberately attacking her G-spot with relentless strokes."
    l "*Loud moan* MmmMhhhhh..."
    mct "Yes... cum for me, Luna..."
    l "Mmmmmh..."
    lsc "MmmMmmmhhh..." with hpunchsubtle
    l "{sc=3}MMmmmmMHHH!!!!" with hpunch 
    play sound clothes3oily
    play sound2 sofa
    stop soundloop fadeout 1
    stop soundloop2 fadeout 1
    scene qaa 51
    hide screen lunaanglefingers
    bla "Luna suddenly breaks the kiss and grabs your wrist, pulling your hand away from her." with dis14
    l "*Panting* W-Wait..."
    l "*Panting* S-Stop..."
    mc "W-What?"
    play sound5 sofa
    play sound4 rubclotheslong2
    scene qaa 52
    bla "Luna slowly crawls closer and curls into you, settling on your lap." with dis22
    show qaa 53
    mc "You okay, Luny?"
    show qaa 52
    l "Y-Yeah..."
    l "I just..."
    l "*Embarrassed chuckle* I just think I would’ve {i}finished{/i} if you’d kept going for one more second."
    show qaa 53
    mc "And... that's bad?"
    mc "You don't want to?"
    show qaa 52
    l "I-I do. I..."
    l "I mean... just not... not yet."
    show qaa 53
    mc "Not yet?"
    show qaa 52
    l "I... I-I want to save it for something else this time."
    show qaa 53
    mc "Something else...?"
    show qaa 52
    l ". . ."
    l "...Y-Yes."
    show qaa 53
    mc "*Soft chuckle* I'm starting to think we're gonna miss that train, Luna."
    show qaa 52
    l "*Soft giggle* Yes, probably."
    l "We can hop back on later, though. It was a loop ride, wasn't it?"
    show qaa 53
    mc "It was, indeed..."
    mc "What do you want to do now, then?"
    show qaa 52
    l ". . ."
    l "*Whispering* I..."
    l "*Whispering* ...I want you."
    l "*Whispering* I can't hold back anymore."
    show qaa 53
    mc "Uh–"
    mc "Does that... mean what I think it means...?"
    show qaa 52
    l "*Whispering* Yes."
    l "*Whispering* I don't want just part of it anymore."
    l "*Whispering* I want it all. I need it."
    l ". . ."
    l "...I'm ready."
    scene qaa 52b with dis22
    l "Make me yours, [mc]..." with dis17
    scene qaa 53b
    mc "As you wish, my love..."
    play sound ["<silence 1.5>", chair1]
    play sound2 rubclotheslong2
    scene qaa54 
    pause 1.7
    bla "You slide Luna’s panties down and lift her with effortless ease, letting her fall onto the bed and shedding your pants as you do."with dis14
    mc "Oh, babe..."
    play sound3 rubclotheslong2
    play sound4 couchlouder
    play sound5 clothes3oily
    scene qaa 55 with dis2
    mc "God, Luna..."with dis12
    mc "I've been dreaming days and nights about this moment..."
    show qaa 57
    l "*Breathing nervously* A-Aah..." with dis15
    l "O-Oh my god..."
    l "Y-You're already... s-so hard..."
    show qaa 56
    mc "Yeah... all that teasing got me pretty worked up down there, I won’t lie."
    show qaa 57
    l "I-I can see that."
    show qaa 56
    mc "We can take it slow."
    mc "As slow as you need. Just let me know if anything feels too much."
    show qaa 57
    l "O-Okay."
    l "T-That sounds good."
    l "Slow. "
    show qaa 55
    bla "You pause for a moment, letting yourself linger as your length rests against Luna's stomach as it goes up and down with each nervous breath." with dis17
    mct "Oh my god."
    mct "The anticipation is killing me."
    mct "This is it. This is real."
    mct "Luna... I'm about to have sex with Luna. At last."
    mct "I'm about to... make her mine..."
    mct "At last..."
    l "*Huffing in anticipation* . . ."
    mc "Let's..."
    mc "Let's start with... just the tip, alright?"
    l "*Biting her lip* A-Alright..."
    play sound clothes3oily
    scene qaa 58 with dis2
    bla "You lower your hips slowly, letting the tip of your cock brush gently against her wet entrance."with dis12
    mc "Okay..."
    mc "I'm... I'm going in now..."
    l "*Breathing nervously* Y-Yes..."
    l "*Breathing nervously* D-Do it..."
    mct "HERE WE GO..."
    play sound oily2
    scene qaa 59 with dis
    pause .1
    play sound2 penetration2
    play sound3 bodycollide2
    scene qaa 55 
    bla "You attempt to push forward, but your dick slips out."with dis
    l "O-Oh."
    scene qaa 57
    l "Oh no." with dis15
    l "I-Is it... is it t-too big for me?"
    show qaa 56
    mc "No, it's not."
    mc "You're fine. You just need to relax and enjoy this moment."
    l ". . ."
    mc "Do you trust me?"
    play sound clothes3oily
    scene qaa 58
    l "I... I trust you."with dis15
    mct "Please, gods, don't betray me now..."
    mct "Don't let this go wrong... not now..."
    play sound oily2 volume 0.8
    scene qaa 59 with dis12
    pause
    play sound2 penetration2
    play sound3 oily2
    scene qaa 60
    bla "As Luna exhales and her body relaxes under your touch, you gently push forward again, this time, sliding inside her." with dis17
    l "*Silent gasp* A-Aaaah–"
    mc "Oh LORD..."
    mct "T-That's the tightest pussy I've ever seen in my life..."
    scene qaa 61
    l "*Voice trembling* O-Oh my GOD..." with dis12
    l "T-That is... q-quite a sensation..."
    show qaa 60
    mc "I-I'm... I'm gonna start moving now, o-okay?"with dis12
    l "O-Okay..."
    $ renpy.music.set_volume(0.45, delay=10.0, channel='music3')
    scene lunass5 with dis2
    bla "You begin to move your hips, pulling back just enough to build friction, then easing back inside her." with dis
    l "*Moans* AAAahh..."
    l "O-Oh my god..."
    l "*Gasping* Oh W-WOW..."
    mc "F-F-Fuuuuck, Luna..."
    mct "Jesus Christ..."
    mct "Ain't gonna lie, I always fantasized about her being tight, but this..."
    mct "This is... something else entirely..."
    l "*Moaning* AAaaAAahh..."
    mc "Y-You good? Too much?"
    l "*Voice shaky* N-No..."
    l "I mean... y-yeah, I'm g-good..."
    l "*Moans* Aaaahhghh..."
    l "So..."
    l "S-So... good..."
    mc "O-Ohh, yeah..."
    mc "This is... a dream come true, Luna..."
    mc "I can't believe I'm inside you right now..."
    l "*Moaning* AAAaahhh... y-yes..."
    mc "My sweet fucking angel..."
    l "*Moaning louder* A-AaAaaaaaHhh..."
    play sound sofa volume 0.5
    play sound7 clothes3
    scene qaa 62 with dis14
    mc "Oh, my Luna..."with dis12
    mc "I need to see all of you..."
    play sound2 clothes3
    scene qaa 63 
    bla "You pull Luna's bra upward, finally revealing her breasts." with dis17
    play sound3 clothes3
    scene qaa 64
    mc "Oh LORD..."with dis17
    scene lunass6 with dis2
    bla "You begin to move your hips again, picking up pace, but keeping your thrusts shallow." with dis
    mc "*Groaning* Oh F-FUCK yes..."
    l "*Starts moaning louder* AAaaah... aaAaaahh..."
    l "O-Oh my god..."
    l "T-This feels... SO good..."
    mc "I d-don't even have words to describe how it feels for me, believe me..."
    mc "Y-You're... unreal..."
    l "AAAAaahh..."
    mct "My god, look at her..."
    mct "No matter how many times I’ve seen her, Luna’s tits always amaze me."
    mct "Especially considering how slim she is."
    mct "So perky... so perfectly round..."
    mct "Her nipples stiff from arousal..."
    mct "She truly is out of this world..."
    l "Oh my g-god, [mc]..."
    l "*Moaning between gasps* I-It feels... s-so big inside me..."
    mc "I bet..."
    l "I-I've never... felt anything like this before..."
    mc "Does it hurt?"
    l "N-No..."
    l "It... *moans* aaaaghh..."
    l "P-Please... keep going..."
    l "D-Don't stop..."
    scene lunass7 with dis2
    bla "You begin thrusting a little deeper into her, her body gripping you so perfectly it almost drives you insane."with dis
    mc "Ooooohhh yes..."
    mc "T-This is incredible..."
    l "*Moaning* R-Really?"
    l "I-Is it... for you too...?"
    mc "Y-You have no idea..."
    mc "Gosh, you're so tight but also so fucking wet..."
    mc "I feel like I'm losing my mind..."
    l "*Moans* AAAAAAaaaahh..."
    mc "Just..."
    l "H-Huh...?"
    mc "Do you think..."
    mc "Do you think we can take it even deeper, Luny?"
    l "*Moaning hard* AAaahHh..."
    l "I..."
    l "I-I can try..."
    mc "O-Oh yes, that's my girl..."
    l "*Moaning harder* AAaahHh..."
    mc "You ready for me, Luna?"
    l ". . ."
    l "Y-Yes..."
    l "I'm ready..."
    play sound penetration2
    play sound2 clothes3oily
    play sound3 sofa volume 0.6
    scene lunass8 with dis2
    bla "You push deeper until Luna’s body finally gives in completely. Your hips meet hers, your full length bottoming out inside her." with dis
    mc "OHH LUNA..."
    mc "H-Holy... f-fucking SHIT..."
    l "*Gasping* G-GGGggGGggghh..."
    l "W-W-What the..."
    l "O-Ohh... oh L-Lord..."
    mc "Oh my GOD..."
    mct "I'm all the fucking way in..."
    mct "I can feel my cock hitting the deepest part of her..."
    mct "Every fucking inch..."
    mct "I can't even believe her body is letting me go this deep."
    l "*Moaning in rhythm* Aaahh... aaaaaaahhh... aaAAAAh..."
    mct "This is it..."
    mct "I'm taking Luna's virginity..."
    mct "And it feels every bit as divine as I imagined..."
    l "*Louder moans* Aaaaaaahh... aaaahhh... aaAAh..."
    mc "Oh my Luna..."
    mc "It's like I've stepped into my own fantasy..."
    l "*Voice shaking* O-OOoooOoohh [mc]..."
    l "I-It feels like... I'm being impaled..."
    mc "Please tell me if it's too much..."
    l "*Quick* N-No..."
    l "I-It... hurt a little at first..."
    l "*Moaning* B-But now..."
    l "*Whimpering* AAaaaahhh..."
    l "Oh my good god..."
    l "N-Now it feels..."
    l "AMAZING..."
    mc "Oh babe..."
    mc "You think you can take even more?"
    l "M-More...??"
    l "*Shaky laugh* H-Hah..."
    l "Y-Yes..."
    l "W-Why... not..."
    l "G-Give me... EVERYTHING..."
    mc "OH FUCK YES..."
    scene lunass9 with dis2
    bla "You don’t hold back anymore. Luna’s petite body takes every thrust, her voice breaking into helpless, high-pitched squeaks." with dis
    lsc "GGg-GGgggghg-gGghhh..."
    bla "Her hands slide frantically over your arms, gripping you like she can't get enough of you."
    lsc "*Crying out* AAaah... aaAAAahhh... AaaAAAGGHhhHHHhh..."
    lsc "My g-Godd, [mc]..."
    mc "O-O-Oh, Luna..."
    mc "*Possessively* My Luna..."
    lsc "T-T-This sensation is..."
    lsc "AAAAHhhggg..."
    lsc "G-God, w-what are you doing to meeee...?"
    mc "Oh babe, your eyes..."
    mc "They're going crazy..."
    lsc "*Breathless chuckle* H-Hah..."
    lsc "I used to think..."
    lsc "*High-pitched moan* GGGhhnnnhh..."
    lsc "I..."
    lsc "I-I used to think that I'd never be able to touch anyone for my entire life..."
    lsc "And now..."
    lsc "M-M-MY GODDDDdd..."
    scene lunamisangleimage
    show screen lunamisanglescreen
    with dis2
    bla "You completely let yourself get lost in pure, raw desire. You spread Luna's legs wide and slam into her flushed and dripping pussy without mercy."with dis
    mcsc "Ooooohh fuck, babe..."
    mcsc "Oh, y-you're doing sooo good..."
    lsc "[mc]..."
    lsc "I-I'm not sure if I can... keep up with..."
    lsc "T-This pace..."
    mcsc "*Panting* Oh, m-me neither, to be honest..."
    mcsc "But... h-holy shit, I sure can't stop..."
    lsc "*Body trembling* AAAAghh..."
    lsc "*Exhausted* Let's..."
    lsc "*Exhausted* Let's... t-take... a b-break..."
    mcsc "Not until you cum, baby..."
    lsc "E-EEEehh...?"
    lsc "Y-You sure... I haven't... a-already...?"
    lsc "B-Because... it... certainly feels like... it..."
    mcsc "*Smirks* Oh, t-trust me, you'll know it when you get there..."
    lsc "AAAAAAhhh..." with hpunch 
    mcsc "Dear Lord, you’re soaking wet..."
    mcsc "But you're also... gripping me so tight..."
    lsc "[mc]..."
    lsc "F-f..."
    lsc "Oh f-f..."
    lsc "{sc=3}{b}Oh FUCK...." with hpunch 
    play sound penetration2
    play sound2 clothes3oily
    play sound3 sofa volume 0.6
    scene lunass12 
    hide screen lunamisanglescreen
    with dis2
    bla "Ignited by hearing Luna curse, you grab both of her hands and pin her against the bed as you continue pounding into her." with dis
    lsc "*Screaming out* AAAAAaaAAGGHHHHHhhh..."with hpunch 
    lsc "O-Oh D-DIOS MIO, [mc]..."
    mct "OHHH FUCK yes..."
    mct "The moment I grabbed her hands..."
    mct "Her whole body jolted like I flipped a switch..."
    lsc "AAAAaawwhhghh..."with hpunch
    lsc "*Moaning* Virgen santa, [mc]..."
    lsc "AAAAAgggGghh..."with hpunch 
    lsc "{font=adeb.ttf}SÍ..." (what_style='textsp')
    lsc "Por el amor de dios, no pares..."
    lsc "No pares..."
    lsc "MmmmmGghghh..."
    lsc "{font=adeb.ttf}Más... MÁS DURO..." (what_style='textsp')
    mct "Oh boy..."
    mct "I have no idea what she's saying, but goddamn, it sounds hot as fuck..."
    lsc "*Loud moan* AAAAaghh..."
    scene lunass13 with dis15
    bla "You keep going, her hands still trapped in yours. Each thrust is smoother, wetter — your bodies perfectly in sync like they’ve done this a thousand times." with dis
    mcsc "O-Ooohh f-fuck..."
    mcsc "I'm gonna cum so hard, Luna..."
    mcsc "You feel too f-fucking good..."
    lsc "*Moans* GGh-gghh..."
    lsc "*Panting* I..."
    lsc "I t-think... me too..."
    lsc "I don't even know how I managed to h-hold it in this long..."
    mcsc "Oh, that's gonna make it even better, babe..."
    lsc "AAaahh..."with hpunch 
    lsc "[mc]..." with hpunch 
    mcsc "F-Fuck yes, keep screaming my name like that..."
    lsc "*Sobbing through pleasure* AAAaghhh... [mc!u]..."
    lsc "I c-can feel it now..."
    lsc "*Biting her lip* MmmmmMmmmhh..."
    lsc "I'm gonna..."
    lsc "I-I'm gonna cum s-so HARD..."
    mcsc "Y-Yeah..."
    mcsc "Let's do it together, babe..."
    lsc "J-Just... p-p-please, d-don't... d-don't do it inside..."
    lsc "M-My dad would kill me..."
    mcsc "*Broken laugh* H-Hah... I think he would actually kill me first..."
    lsc "*Breathless* AAAAAAghh..."
    scene lunass12 with dis15
    lsc "[mc]... I-I can't... !!!" with dis 
    mcsc "Y-Yeah..."
    mcsc "Cum for me, Luna..."
    mcsc "L-Let it all out..."
    lsc "AAAAhhh..."
    lsc "OH MY GOD IT'S RIGHT THERE..."with hpunch 
    lsc "R-RIGHT THERE..."
    lsc "AAAaaaahhh..."
    mcsc "*Groaning* AAArrrghh..."
    lsc "AAAaaaammmmhhh..."
    lsc "{sc=4}AAAAaaaAaaghhh..."with hpunchsubtle
    lsc "{sc=5}AaaaAAGgggGgHHhhhhh..."with hpunch 
    lsc "{sc=7}{size=46}[mc][namelong]..."with hpunch 
    play sound chair1
    scene qaa 65 with pdd
    play sound7 cumall
    play sound6 squirt
    bla "At the very last heartbeat, you manage to pull out just in time." with hpunchlong4
    play sound sofa
    play sound2 chair1
    play sound3 couchlouder
    play sound4 squirt
    play sound5 squirt
    scene qaa66b
    l "{sc=5}*Orgasming violently* AAAAAAAAaagg-gGGGGHHh..." with hpunchlong4
    play sound6 squirt
    play sound7 squirt
    lsc "{sc=5}MMMAAAhhHh—GGGGGAAAAHh..." with hpunch
    play sound8 squirt
    play sound squirt
    lsc "{sc=5}AAmmmMMAAaaggAgGGGGHHh..." with hpunch
    play sound2 squirt
    play sound3 squirt
    lsc "{sc=5}AAAMMMrrR—GGGGHHHhh..." with hpunch
    play sound4 squirt
    play sound5 squirt
    lsc "{sc=5}AAaAAwwmMMmmRRRGGGHHhH..." with hpunch
    play sound8 sofa volume 0.5
    play sound6 rubclotheslong2
    play sound7 clothes3oily
    scene qaa 67
    lbt "*Panting helplessly* AAAaahhh... AAAAghhh... aaaaah..."with dis25
    mc "*Panting* W-Wow..."
    mc "A-Are you okay?"
    l "*Panting* T-T-That..."
    l "*Panting* T-That was..."
    l "*Panting* Sweet virgin Mary, I-I don't even know what that w-was..."
    l "*Panting* T-That was the most intense thirty seconds of my whole life..."
    mc "*Breathless chuckle* Yeah, it really seemed like it..."
    l "*Panting* I c-can't... f-feel my legs..."
    mc "Can't say I'm not glad to hear that."
    l "W-Wait... d-did I scratch your back?"
    l "O-Oh my god, I-I'm s-so sorry, I c-couldn't control it!"
    mc "It's aaaall good, Luna..."
    play sound rubclotheslong2
    scene qaa 68
    bla "You slowly ease yourself off of Luna, savoring the sight of her perfect body marked by the mess you have made of her." with dis25
    mc "H-Holy shit..."
    mc "S-Sorry about that."
    l "*Still panting* It's... all good..."
    mct "Jesus..."
    mct "My body shouldn’t even be ready again this fast... but just seeing her like this..."
    mct "My cum everywhere... ruined in the best possible way..."
    mct "Yeah... this is doing things to me."
    mct "This girl's a devil with an angel’s soul. There’s no other explanation."
    mct "Should I...?"
    $ lunasex = True
    menu:
        with dis
        "[gr]Go for round two":
            $ lunasex2 = True
            mc "You know..."with dis
            mc "How about..."
            l "Huh...?"
            play sound sofa 
            play sound2 rubclotheslong2
            scene qaa 69
            bla "You grab Luna by the waist, lifting her and guiding her onto your lap." with dis2
            show qaa 70
            l "W-Wh-what are you doing...?"
            show qaa 69
            mc "Just giving you a different view."
            show qaa 70
            l "W-What...?"
            show qaa 69
            mc "Don't you wanna feel that sensation again...?"
            show qaa 70
            l "Uhm..."
            l "I-I mean... yes, b-but I can't... f-feel my legs anymore."
            l "I don't think I can even... uhm... y-you know..."
            show qaa 69
            mc "Don't worry, you don't have to do anything. Just sit pretty and... enjoy."
            show qaa 70
            l "B-But... how is your... y-your... {i}t-thing{/i} still hard?"
            l "I thought guys were supposed to... y-you know... need some time after..."
            show qaa 69
            mc "My body is indeed asking me to take a break, but my brain is screaming... “oh boy, we need to make her twitch like that again...”"
            show qaa 70
            l "B-But–"
            play sound penetration2
            play sound2 clothes3oily
            play sound3 sofa volume 0.3
            scene lunass14 with dis2
            bla "Before Luna can finish her sentence, you push back inside her, stretching her open once again. Her pussy remains unbelievably tight, as if her own body refused to believe what it was taking."with dis15
            mc "Ooooooohhhh, f-fuck yes, Luna..."
            l "*Digging her nails into your arm* AAAAaaaaaghhhh... g-goddd..."
            l "Mmmmmnnhnhgh..."
            l "*Raw moan* [mc][namelong]...."
            mc "Oh, that's so fucking good..."
            l "AAahh... aaAAAAammmhh... aaaaagh... nnnnghh..."
            l "*Breathless* AAAoooggh..."
            l "[mc[0]]-[mc]..."
            l "Y-You're going to b-break me..."
            mc "F-Fuck yes..."
            mct "I can't believe how hard I am again already."
            mct "The effect this woman has on me defies all logic..."
            l "*Panting* O-Ohhhh d-dios..."
            l "Mmmmmmhmmm..."
            scene lunass15 with dis15
            l "Y-Yeah..."with dis
            l "O-Ohh, [mc]..."
            l "Sí... a-así..." (what_style='textsp')
            mc "Oh Luna..."
            mc "I fucking love it when you speak in Spanish..."
            l "*Slightly embarrassed* O-Oh..."
            l "S-Sorry... I didn't realize..."
            mc "I-I know you didn't."
            mc "That's what makes it so goddamn sexy..."
            l "It... *moans* aAAaaaahh..."
            l "I-It just... s-slipped out..."
            mc "D-Don't think about what you say."
            mc "Just... let yourself go..."
            l "AAghh... o-okay..."
            play sound clothes3oily
            scene lunass16 with dis15
            l "*Moaning* AAAaaahh... aaaahh... aaaaAAgrmm..."with dis
            mc "Oh my god, so g-good..."
            l "O-Ohhghh... y-you're..."
            l "*Moans* AAaaahh... y-you're so deep..."
            mc "Tell me if you want me to sto–"
            l "*Sudden* N-NOOo..."
            l "P-Please, don't..."
            l "Keep f–"
            l "K-Keep..."
            l "Keep... d-doing this to me..."
            mc "*Teasing* Come on, you can curse, Luny..."
            mc "I promise I won't tell anyone."
            mc "It's just you and me here..."
            l "*Broken laugh* H-Haha..."
            mc "Come on... what were you trying to say?"
            mc "What do you want me to keep doing to you...?"
            l "*Broken chuckle* H-Hah..."
            l "*Hesitant* K-Keep..."
            mc "Yeah... say it..."
            l "Keep... {i}f-f-fucking{/i} me, [mc]..."
            mc "*Grinning* Fucking you with what?"
            l "F-Fucking me with... *moans* aaagghh... w-with t-that..."
            l "T-That..."
            l "That... b-big... {i}c-c-cock{/i} of yours..."
            mc "O-Ooooohh, baby..."
            mct "Jesus... how terribly embarrassed she sounded saying that just made it ten times hotter..."
            l "Oh, [mc][namelong]..."
            play sound penetration2
            play sound2 clothes3oily
            play sound3 sofa volume 0.7
            scene qaa 71 with dis15
            bla "Without warning, Luna twists her body around on top of you, without letting your cock slip out for even a second." with dis12
            l "*Panting* AAAAh... Aaaahhh... aaagh..."
            l "*Panting* I-I need... I need to see you..."
            play sound2 clothes3oily
            play sound3 sofa volume 0.4
            scene lunacowangleimage 
            show screen lunacowanglescreen
            with dis2
            l "*Moaning in rhythm* AAAAahhh... aaaagghh... nnnnghhh..." with dis
            mct "O-Ohh sweet Lord, have mercy..."
            l "*Moans* AAAAaaghh..."
            mct "I did NOT know Luna could move like this..."
            l "*Moans* AAAaaAAhh... s-so g-Good..."
            mct "She’s riding me like she’s been waiting her whole life for this..."
            l "*Moans louder* AAAAhhHHaAAAhhhh..."
            l "*Gasping* Oooohhh, [mc]..."
            l "I c-can't believe what... *moans* aaaaghhh... w-what we've been missing..."
            l "MmmmmhMMh..."
            l "Ohhh [mc][namelong]..."
            mct "God..."
            mct "I fucking love how she keeps moaning my name like it's the only word she remembers."
            mct "It's like... she’s giving every ounce of her purity to me and only me..."
            l "*Panting* AAaaghh y-yeaHHh..."
            l "*Panting* Que rico..."
            l "*Panting* O-Oh my god..."
            l "*Whispering* Oh, [mc]..."
            l "*Voice breaking* I c-can... f-feel it..."
            l "I-I can feel it coming again..."
            l "Oh my g-god, I'm gonna c-cum again..."
            mc "Ooh yeah, g-good girl..."
            mc "Give it to me, Luna..."
            l "*Moaning* Oh my god... oh my GODDddDD..."
            l "*Almost choking on her breath* I-I'm gonna do it again..."
            mc "I-I'm so close too..."
            play sound penetration2
            scene lunass19 
            hide screen lunacowanglescreen
            with dis2
            bla "Luna suddenly slams her hips down, taking every inch of you entirely inside her as she speeds up."with dis
            mcsc "O-OOHHh BOY..."
            lsc "*Crying out* AAaaGhHhh... aaAAAhhh... aaammmmmHHhh..."
            lsc "*Moaning louder* Y-Yeah..."
            lsc "OH MY GOD..."
            lsc "I f-feel... E-EVERYTHINGGG..."
            mcsc "L-Luna... Jesus Christ..."
            mcsc "B-Be careful..."
            mcsc "I-I'm gonna–"
            lsc "Y-Yes... y-yes, p-please..."
            lsc "I-I want to make you cum too..."
            mcsc "A-And you will, b-but..."
            mcsc "I-If you keep riding me like this... F-FFucKkkk..."
            mcsc "I-I'm gonna explode inside you if you don't–"
            lsc "*Whimpering* OOOOHHHHhhhh..." with hpunch 
            lsc "I-I CAN'T STOPPPppp..." with hpunch 
            mcsc "L-LUNA!!!" with hpunch 
            scene lunass20 with dis
            pause 6.9
            lsc "Yes...{w=2}{nw}"with dis15
            lsc "YESS...{w=0.8}{nw}"with hpunchsubtle
            lsc "YESSS...{w=0.8}{nw}"with hpunchsubtle
            lsc "{sc=3}YESSSS...{w=0.8}{nw}"with hpunchsubtle
            l "{sc=8}{size=41}AAAAAARGHHHH...{w=1.1}{nw}"with hpunch
            l "{sc=9}{size=45}AAAAAAAAAGGHHHHH...{w=1.1}{nw}"with hpunch
            l "{sc=10}{size=47}AAAAAaAAAAhhhhHHhhhhhh...{w=1.2}{nw}"with hpunch
            l "{sc=11}{size=50}AAAAAAAaaaaaaAAAaAGGHHHHh.......{w=6.9}{nw}"with hpunch
            play sound rubclotheslong2
            play sound2 clothes3oily
            play sound3 sofa volume 0.8
            scene qaa 72 with dis2
            bla "Both of you break at the same time. Her entire body spasms around you, her walls clenching violently, drawing every drop from you." with dis2
            lbt "*Panting violently* AAghh..."
            lbt "*Gasping* O-OH MY GOD..."
            mcd "*Barely able to speak* Luna..."
            mcd "I... c-came inside you..."
            lbt "Y-Yeah..."
            lbt "Y-Yeah... I... I n-noticed..."
            lbt "I tried to stop, but..."
            lbt "Oh my god, I just couldn't..."
            lbt "That was... that was insane..."
            mcd "It really was..."
            mcd "I c-can't feel my spine right now."
            lbt "L-Let me... l-let me g-get off of you..."
            play sound rubclotheslong2
            play sound3 sofa volume 0.8
            play sound2 oily
            scene qaa 73 with dis2
            bla "After a few more seconds to catch her breath, Luna finally pulls herself off you, your cum still pouring out of her."with dis15
            mc "O-Oooohhhhh, Jesus..." 
            show qaa 74
            l "O-Oh m-my god."
            l "T-T-That's... m-more than I thought."
            l "M-My dad's gonna kill me."
            show qaa 73
            mc "I-I strongly believe we shouldn't tell him {i}this{/i} particular thing happened."
            show qaa 74
            l "Y-Yes, yes. I think so too."
            l "I just..."
            l "Oh my GOD, [mc], there's so much..."
            l "I-I... I kinda thought you wouldn't have much left in you after... well, after the first time."
            show qaa 73
            mc "*Laughs* W-Well, that was clearly not the case."
            show qaa 74
            l "C-Clearly not..."
            show qaa 73
            mc "Maybe we should... clean up a bit. I think I saw a towel back there."
            show qaa 74
            l "S-Sure..."
        "Stop here":
            mc "*Soft chuckle* (...Okay, maybe I gave her enough of a wild ride for today.)" with dis
            mc "Let me help you clean up, Luna. I think I saw a towel back there."
            l "*Still dazed* T-Thank you..."
    stop music3 fadeout 17
    play soundloop rain3 fadein 10
    scene qaa 75 with dis3
    bla "You both begin slipping your clothes back on, slowly, as if reluctant to leave the moment behind, and cuddle together on the bed."with dis22
    mc "*Deep exhale* Damn..."
    play soundlow thunder fadein 2
    play music lunasongpos volume 0.6 fadein 5
    scene lunass21 with dis22
    l "Yeah..." with dis15
    mc ". . ."
    l ". . ."
    mc "What are you thinking about?"
    l "Me...?"
    l "I'm thinking..."
    l "I want to stay like this forever."
    l "Just... touching you. Feeling you next to me."
    l "Please never start giving me visions or I’ll have to sand the skin off my palms."
    mc "*Chuckles* I'll do my best to stay vision-free."
    l "Thank you..."
    mc ". . ."
    mc "So..."
    mc "Was it like you imagined?"
    l "It was..."
    l "Better. So much better than I ever imagined."
    mc "Well, I'm glad to hear that..."
    mc "I've gotta say, it was incredible for me too."
    mc "Didn't it hurt for you at all?"
    l "Just... a little bit."
    mc "Wait, really?? I kept telling you to say something if I was going too hard!"
    l "But a little pain doesn’t mean I wanted you to stop."
    l "And besides, it was only at the beginning."
    l "Then I just felt... full. And... good. And then... electric. And warm."
    mc "Oh... I see."
    mc "Well, I've gotta say, telling you to open your heart and always be honest with me is probably, like, one of the top three best pieces of advice I’ve ever given."
    mc "Maybe even number two. Right behind telling Chang to ditch that god-awful comb-over."
    l "*Giggles* Wow, now I want to see a picture of him during that time."
    mc "*Chuckles* I'll show you later. I think I’ve still got a couple of them in a locked folder on my phone."
    l "Nice..."
    l ". . ."
    l "...Do you think the ghosts were watching us?"
    mc "*Chuckles* If they were, I’m pretty sure we gave them a show they won’t forget."
    l "Yeah... I bet."
    l "*Deep exhale* Mmmmh..."
    l "How long until the train comes back?"
    mc "Well, I’m not even sure how long we’ve been here, but we should probably start heading to the station."
    l "Yeah, I guess so..."
    mc "You said you found something to protect us from the rain?"
    l "I did!"
    l "Let me show you..."
    scene qaa 75 with dis3
    bla "Yet... despite your words, neither of you move. Luna continues to twirl her finger on your chest, giving you little bites on the shoulder."with dis25
    bla "You both decide to stay like this a little longer."
    $ renpy.end_replay()



label ending09:
    stop music fadeout 8
    stop soundloop fadeout 10
    scene black with dis33
    show screen sometimelater with dis25
    pause
    play music2 happy18 fadein 5
    hide screen sometimelater
    if lunapath:
        play soundloop2 town_ambience fadein 6 volume 0.3
        scene dextra 1
        with dis33
        bla "You continue sharing laughs and quiet, comfortable moments with Luna on the train ride back until before you know it, you find yourselves back together in Kredon once more." with dis2
        mc "Aw man... can't believe the day's already over."
        l "I know... it went by way too fast."
        mc "Definitely."
        scene dextra 2
        mc "But hey, look at it this way. This was just the first date of many!" with dis15
        show dextra 3
        l "R-Really...?"
        show dextra 2
        mc "Of course!"
        show dextra 3
        l "So... when's the next one?"
        show dextra 2
        mc "*Chuckles* Well, that depends on what you consider a “date”. A trip to the supermarket to buy groceries could be a date. That could happen tomorrow."
        mc "But if you’re only counting the more... sophisticated, over-the-top romantic stuff... then we might have to wait a little longer."
        mc "Maybe the day after tomorrow."
        show dextra 3
        l "*Laughs* I'm looking forward to all of it either way!"
        show dextra 2
        mc "In any case, we’ve got our whole lives ahead of us, Luna. And I plan on sharing every bit of it with you."
        show dextra 3
        l "*Softer* A-As do I."
        l "I..."
        l "I love you, [mc]."
        show dextra 2
        mc "I love you too, Luna. More than you can possibly imagine."
        play sound busarrive
        show dextra 4
        bla "The bus pulls up to the stop, brakes hissing as people begin to climb aboard." with dis15
        show dextra 5
        l "O-Okay, this is my bus!" with dis12
        show dextra 6
        mc "You sure you don't want me to go with you? I've got time!"
        show dextra 5
        l "I'm sure! It's only a fifteen-minute bus ride, and Nancy's house is just around the corner."
        l "Save the time for another day!"
        show dextra 6
        mc "Alright, alright... but I will see you later, right?"
        show dextra 5
        l "Sure thing! I'll be joining the girls in Eternum after dinner!"
        show dextra 6
        mc "Ahh, perfect! See you there, then!"
        show dextra 5
        l "Yes! Bye bye, [mc]!"
        show dextra 6
        mc "Love you!"
        show dextra 5
        l "L-Love you too!"
        play sound2 ["<silence 0.8>", caraway2]
        show dextra 7
        bla "Luna disappears inside, and you stand there watching as the bus pulls away and vanishes down the street." with dis2
        mct "Oh, man..."
        mct "What a BEAUTIFUL day."
        mct "Everything was so damn perfect."
        mct "The time with Luna was perfect. The train was perfect. The goodbye was perfect."
        mct "She {i}is{/i} perfect."
        mct "Damn, what a girl..."
        mct "I'm one lucky bastard."
        scene dextra 8
        mc "*Sighs* Aaahh, well..." with dis17
        mct "Guess I should start heading back."
        mct "Can't neglect the girls at home either."
        mct "Mmmmh..."
        mct "Maybe I could pass by that new creperie that just opened...?"
        mct "I think I can guess what flavor each of them likes."
        mct "Yeah... they'd love that, no doubt. It's the little things that matter, after all."
        mct "Sure, those crepes are a bit overpriced, but hell, it's more than worth it."
        scene dextra 1
        mct "Ahh, [mc]..." with dis15
        mct "At what point did you decide to fall in love with these girls..."
        stop soundloop2 fadeout 7
        scene news 6 with dis33
        play sound keys
        play sound2 ["<silence 2.4>", doorclose]
        mc "*Kicking off shoes* Hello? I'm back, everyone!" with dis17
        play sound3 dooropenclose
        scene news 7
        mc "Yeah, yeah — your nose isn't lying, Dalia. I brought crepes for everyone!" with dis17
        mc "What can I say, I'm a romantic..."
    else:
        scene news 6
        with dis33
        play sound keys
        play sound2 ["<silence 2.4>", doorclose]
        mc "*Kicking off shoes* I'm back, everyone!" with dis17
        play sound3 dooropenclose
        scene news 7 
        mc "Please tell me there’s still some food left from yesterday!" with dis17
        mc "I spent all afternoon playing on an NBA server, and now I'm STARVING!"
    play sound footsteps4
    scene news 8 with dis17
    mc "Huh? A note?" with dis12
    scene news 9
    mc "Mmmhhuhh..." with dis12
    mct "Looks like they all went out. But... they're gonna hop on Eternum after ten."
    mct "Although... they didn't say what server. I need to ask in the group chat."
    mct "Or... just crash at Alex's place and join them there."
    if not lunapath:
        mct "I could even bring dessert! I'm sure they’d love that surprise."
    else:
        mct "I could even bring the crepes with me!"
        mct "...Though by the time I get there, they’ll probably be cold."
        mct "Might as well just buy new ones on the way."
        mct "Which means... I guess I’m stuck eating these ones by myself."
        mct "Hehe... truly tragic..."
    scene news 10
    mct "Alright, alright, alright!" with dis17
    mct "In any case, I've still got a little over an hour left."
    mct "Plenty of time to be productive."
    if harempath:
        mct "These girls might be everything to me now, but I still need to focus on myself once in a while."
    if not lunapath:
        mct "I’ll grab a snack, maybe read a chapter of that book I keep putting off, do a few sit-ups, clean my room, then head out to buy dessert before the stores close."
    else:
        mct "I’ll eat the crepes, maybe read a chapter of that book I keep putting off, do a few sit-ups, clean my room, then head out to buy new ones before the store closes."
    mct "Like I always say..."
    mc "GOTTA SQUEEZE EVERY MINUTE OF LIFE!" with hpunch 
    mcsc "{size=48}LEEEEEET'S–{w=1.2}{nw}" with hpunchlong
    play sound pop volume 0.7
    stop music2
    play soundloop rain3
    scene news 11
    pause
    play sound7 thunder fadein 3 volume 0.45
    mc "{bt=2}*Snoring* ZZZzzzzzz...." with dis15
    mc "{bt=2}*Mumbling in your sleep* Immh..."
    mc "{bt=2}Ammh sick of your... damn mmhriddles, mIdrielmhh..."
    mc "{bt=2}Mmmmnnhh..."
    play soundloop2 vibration
    scene news 12
    bla "{sc=1}Your phone buzzes.{/sc}" with dis12
    play sound leathershort volume 0.2
    scene news 13
    mc "*Groggy* Mmm-mmmh...?" with dis15
    play soundlow thunder fadein 1
    mct "Ohh... crap, I fell asleep."
    mct "So much for being productive, [mc]..."
    scene news 14
    mc "*Looking at your phone* (Jesus, and it's already twelve.)" with dis12
    mct "Nice way to fuck up my sleeping schedule."
    scene news 15
    mc "Hmm..." with dis17
    mct "Another unknown number?"
    if axelhelp:
        mct "I swear, if it's Axel again, I'm–"
    scene news 15b
    mct "Oh, wait... Annie changed her number when she went to the UK last weekend and bought a new phone. I never saved the new one." with dis
    mct "Yeah... that's probably her."
    scene news 15
    mct "And judging by how many missed calls I’ve got... it’s definitely not the first time she’s tried to reach me. Damn me." with dis
    play sound beep2b
    stop soundloop2
    scene news 16
    mc "*Still sleepy* Hey, Annie?" with dis12
    mc "Jeez, I'm {i}so{/i} sorry."
    mc "I was planning to surprise you all at Alex’s place, but I passed out on the couch like a middle-aged dad after a few beers."
    mc "Are you... are you coming back already? Or are the others still playing?"
    show news 17
    aaa "Turn on the TV."
    scene news 18
    mc ". . ." with dis
    play sound2 clothes3
    play sound4 thunder fadein 3 volume 0.6
    scene news 20
    mc "*Sitting up* (That's... not Annie.)" with dis15
    mc "Uhm..."
    mc "I'm... sorry, who is this...?"
    aaa "Turn on the TV, [mc]."
    mc ". . ."
    mc "Who the hell am I talking to...?"
    aaa "This had to happen. It could not be avoided. There was no other way."
    aaa "It had to be now. Not sooner. Not later."
    mc "What...?"
    aaa "We'll reach out to you soon."
    aaa "You'll know everything we know, so you can keep walking the path the Lady set for us."
    aaa "The only possible path forward."
    mc "W-What Lady, what the hell are you talking about?"
    aaa "Turn on the TV."
    play sound beep2b
    bla "The mysterious voice on the phone hangs up."
    mct "What..."
    mct "What the actual fuck was that...?"
    mc ". . ."
    scene news 15
    mc "Hmm..." with dis17
    mct "I'm kinda used to seeing weird shit in Eternum — glitches, visions, creepy NPCs... but... not in real life." 
    mct "Did someone... find me...? Do they know I'm [nickname]?"
    mct "Mmmrph... maybe I should stick to using {i}only{/i} my nickname from now on..."
    mc ". . ."
    play sound clothes3
    play soundlow leathershort volume 0.2
    scene news 21 with dis2
    bla "After a few seconds of silence, as if something unseen tugs at your arm, you slowly reach for the remote on the table." with dis2
    mc ". . ."
    mct "...Fine."
    mct "Let's turn on the TV. Better figure out what the hell this is before I hop in with the girls on Eternum."
    mct "Guess there's nothing to lose."
    play sound button
    play sound8 turnontv
    $ renpy.music.set_volume(0.0, channel='soundloop3')
    $ renpy.music.set_volume(1.0, delay=20, channel='soundloop3')
    play soundloop3 deception
    scene news 22
    pause .1
    play sound7 anchor1 volume 0.7
    scene news 23 
    blalead "{cps=20}{size=34} —to bring you continuing coverage of what experts are already calling... the worst technological failure in human history." 
    mc "What...?"
    play sound7 anchor2 volume 0.9
    scene news 1
    show breakingnews1
    show news_ticker
    show newsreflection
    show screen newstext1
    with dis25
    pause
    hide screen newstext1
    play sound7 anchor3 volume 0.9
    show screen newstext2
    pause
    hide screen newstext2
    play sound6 thunder fadein 2 volume 0.8
    play sound7 anchor5 volume 0.9
    show screen newstext4
    show news 2 with dis15
    pause
    hide screen newstext4
    play sound7 anchor6 volume 0.9
    show screen newstext5
    pause
    hide screen newstext5
    play sound7 anchor7 volume 0.9
    show screen newstext6
    show news 1 with dis15
    pause
    hide screen newstext6
    play sound7 anchor8 volume 0.9
    show screen newstext7
    show news 2 with dis15
    pause
    hide screen newstext7
    show news 3 
    with dis17
    play sound7 anchor9 volume 0.9
    show screen newstext8 with dis
    pause
    hide screen newstext8
    play sound7 anchor9b volume 0.9
    show screen newstext8b
    pause
    hide screen newstext8b
    show screen newstext9
    show news 4
    with dis15
    pause
    hide screen newstext9
    play sound7 anchor10 volume 0.9
    show screen newstext10
    show news 5
    with dis17
    pause
    hide screen newstext10
    play sound7 anchor11 volume 0.9
    show screen newstext11
    pause
    hide screen newstext11
    play sound7 anchor12 volume 0.9
    play music2 mindgames volume 0.8 fadein 18
    show screen newstext13
    pause
    hide screen newstext13
    play sound7 anchor13 volume 0.9
    show screen newstext14
    pause
    hide screen newstext14
    stop sound7
    play sound6 ["<silence 0.6>", anchor4] volume 0.45
    scene mc09ending 
    with dis25
    play sound7 police fadein 4
    play sound8 police fadein 16
    play sound thunder fadein 2 
    play sound2 ["<silence 8.7>", phonedrop]
    pause 9.5
    stop soundloop
    stop soundloop3
    stop music3
    stop sound7
    stop sound8
    stop sound6
    


label end:
    hide screen heart
    scene black 
    pause 2
    jump credits
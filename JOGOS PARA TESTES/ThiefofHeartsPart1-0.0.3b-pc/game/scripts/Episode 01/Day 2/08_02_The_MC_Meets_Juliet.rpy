label lb_ep01_The_MC_meets_Juliet1:
    #scene continues with the MC on the gym floor in his uniform with a smile on his face, watching Luke while he’s on the phone with someone (his brother)
    play ambient "sound effects/01/gymnasium_ambience2.ogg" loop fadein 1.0
    scene sc gymjuliet j01
    ha"And you’re saying that she’s real?"
    show sc gymjuliet j03
    "..."
    show sc gymjuliet j02
    ha"And she was definitely a blonde."
    show sc gymjuliet j03
    "..."
    show sc gymjuliet j02
    ha"One of your regulars?"
    show sc gymjuliet j03
    "..."
    show sc gymjuliet j01
    ha"No, it’s fine, bro."
    show sc gymjuliet j04
    "..."
    show sc gymjuliet j02
    ha"Fine, I’ll talk to you later."
    ha"Bye."
    show sc gymjuliet j04
    ha"(Dammit...)"
    #he ends the call and looks disappointed
    show sc gymjuliet j05
    mc"So, do you believe me now?"
    show sc gymintro g06
    ha"I suppose I’ll be getting those first three rounds then."
    show sc gymjuliet j05
    mc"Glad we could do business."
    show sc gymintro g14
    ha"Yeah, yeah..."
    show sc gymintro g13
    mc"By the way, change of plans for tonight." 
    show sc gymintro g07
    mc"I want to go to this club that someone recommended to us." 
    show sc gymjuliet j05
    mc"It's called the {i}Eager Beaver{/i}." 
    show sc gymintro g15
    ha"Oooh... I like the sound of that."
    show sc gymintro g14
    ha"Count me in!" 
    show sc gymjuliet j05
    mc"I love that I don't to even try hard to convince you, Harry." 
    show sc gymintro g14
    ha"Haha, yeah..."
    show sc gymintro g12
    ha"Anyway, I’m gonna get to those tasks so watch the counter for me."
    show sc gymintro g09
    ha"And stick some music on. Liven this place up a bit."
    show sc gymjuliet j05
    mc"Can do."
    #Harry leaves and the MC moves behind the counter
    play music "sound effects/01/Pump It Up1.mp3" loop fadein 1.0
    show sc gymjuliet j06
    with dissolve
    mc"(Now that I've convinced Harry to go to the {i}Eager Beaver{/i} club tonight...)"
    #we show a few people training at the gym and show the MC behind the counter, watching to make sure everything is okay
    mc"(I'll need to get him out of the way so I can find this tattoo parlour owner.)"
    #the MC looks up and sees a new lady come into the gym
    #She's hot and fit, young, with short hair, and dark roots but her hair has multiple colours (green and pink).
    #Inspiration: Judy Alvarez from Cyberpunk - https://static.zerochan.net/Judy.Alvarez.full.3173191.jpg
    #she arrives in normal clothing and will change into gym clothes later
    show sc gymjuliet j07
    mc"(Woah... I haven’t seen her in here before.)"
    mc"(I definitely would have remembered.)"
    show sc gymjuliet j09
    un"Hey there."
    show sc gymjuliet j13
    mc"Hi there... Uh... How can I help you?"
    show sc gymjuliet j09
    un"I’m new in town and was looking to start a new membership."
    un"You guys have a seven-day free trial, yes?"
    show sc gymjuliet j08
    mc"That’s correct."
    show sc gymjuliet j14
    mc"I’ll need you to fill in some details first and then after seven days..."
    show sc gymjuliet j15
    mc"If you want something more permanent, then we can discuss what membership options will suit you best."
    #the MC hands her a clipboard and sheet for her to fill out
    show sc gymjuliet j16
    un"Thanks."
    show sc gymjuliet j13
    mc"So what brings you here?"
    show sc gymjuliet j18
    un"Well, fitness, obviously."
    show sc gymjuliet j20
    un"This is a gym, is it not?"
    show sc gymjuliet j16
    mc"Sorry, I should have been more specific."
    mc"What brings you to town?"
    show sc gymjuliet j17
    un"Oh..."
    show sc gymjuliet j18
    un"Well, you know, the usual. Work opportunities. Learning more about new people and the places in town."
    show sc gymjuliet j17
    un"How about you? Have you been working here long?"
    show sc gymjuliet j11
    mc"About eight months now."
    show sc gymjuliet j20
    un"And how are you finding it so far?"
    menu:
        "Honest reply":
            show sc gymjuliet j13
            mc"I like it enough."
            mc"It pays the bills and I get to use the equipment and showers for free. So that’s a plus!"
            show sc gymjuliet j18
            un"Yeah, having hot water is certainly a necessity nowadays, given how cold it gets late at night."
        "Try and be charming":
            show sc gymjuliet j13
            mc"It has it perks."
            show sc gymjuliet j16
            mc"Like getting to meet people such as yourself."
            show sc gymjuliet j17
            un"Um, right..."
            show sc gymjuliet j19
            mc"(Hmm... Maybe that was the wrong approach.)"
            mc"(I shouldn't try an act over eager.)"

    show sc gymjuliet j20
    un"Here, I'm done with this."
    #the MC looks at the sheet and reads her name
    show sc gymjuliet j21
    mc"Thanks for that..."
    show sc gymjuliet j22
    mc"Juliet."
    show sc gymjuliet j21
    mc"I'm [y_name], by the way."
    #she looks plain face for her reply
    show sc gymjuliet j09
    ju"So... Where’s the women’s changing room?"
    show sc gymjuliet j25
    mc"It’s straight over there."
    #the MC points in that direction
    show sc gymjuliet j13
    mc"My co-worker was cleaning in there a little earlier but he should be done now."
    show sc gymjuliet j11
    mc"There’ll be some fresh towels as well if you need them."
    show sc gymjuliet j09
    ju"Thanks."
    #she remains straight-faced and heads to the changing room
    show sc gymjuliet j23
    mc"(Hmm... If I can convince her to become a member then this gym might feel like less of a sausage-fest!)"
    mc"(She doesn’t seem like the type who wants to flirt and is more for small talk if anything.)"
    show sc gymjuliet j24
    mc"(I should probably just let her do her thing...)"
    stop music fadeout 1.0
    stop ambient fadeout 1.0
    #screen goes blank
    scene black
    with dissolve
    pause 1.0
    centered "A little while later...{w=2.0}{nw}" with dissolve
    show text "A little while later..."
    scene bg black with Dissolve(1)
    pause 1.0

    
    #this shows on the screen
    #scene returns with the MC behind the counter
    play music "sound effects/01/Pump It Up3.mp3" loop fadein 1.0
    play ambient "sound effects/01/gymnasium_ambience3.ogg" loop fadein 1.0
    show sc gymjuliet j27
    with dissolve
    mc"(This girl looks like a pro.)"
    mc"(And all the guys in here are taking sneaky glances at her.)"
    #We show Juliet working out alone, and she looks like a pro from the MC’s point of view.
    show sc gymjuliet j28
    mc"(If Juliet is aware, then she's is not letting it bother her.)"
    mc"(There’s definitely something about her though.)"
    #show a peeping tom checking her out/ogling her by the stand - https://www.daz3d.com/workout-gear
    show sc gymjuliet j26
    mc"(What’s that guy doing?)"
    #The MC is taking obvious glances at Juliet while she works out
    show sc gymjuliet j30
    mc"(Could he be anymore obvious?)"
    #show the guy trying to talk to Juliet while she works out
    show sc gymjuliet j31
    man"Say, girl... I haven’t seen you around here before."
    show sc gymjuliet j29
    ju"That’s probably because it’s my first time here."
    show sc gymjuliet j31
    man"Well let me welcome you by saying that if you’re interested in a more physical workout, I’d be happy to personally train you."
    show sc gymjuliet j106
    man"Among many other things."
    #he blatantly ogles her chest
    show sc gymjuliet j29
    ju"If you don’t mind, I’d like to be left alone so I can exercise without being interrupted."
    show sc gymjuliet j31
    man"Aw, come on... Are you really going to be like that?"
    #Juliet looks pissed off and the MC notices
    show sc gymjuliet j28
    ju"(Can’t a girl just train in peace?)"
    #[Handle the situation / Stay out of it]

    menu:
        "Handle the situation"(wt="Best option"):
            #the MC approaches the Peeping Tom
            show sc gymjuliet j32
            mc"Excuse me."
            #the guy turns around and sees the MC
            mc"It would be wise of you to leave the other gym members alone."
            show sc gymjuliet j33
            man"And why would I do that?"
            show sc gymjuliet j38
            mc"If you don’t then I’m going to have to ask you to leave."
            mc"This is a gym, not a club. So save your pickup lines for the clubs, buddy."
            show sc gymjuliet j36
            man"Hahaha! You don’t scare me."
            man"And I’ll keep coming here as long as this little hottie is around."
            show sc gymjuliet j39
            man"So what the hell are you going to do about it, pipsqueak?"
            #he shoves the MC
            show sc gymjuliet j37
            mc"(He shouldn’t have done that.)"
            #the MC clenches his fists
            show sc gymjuliet j40
            mc"You just won two tickets to pain town, dude."
            #The man gives a cheesy grin
            show sc gymjuliet j41
            man"Oh, you are dead, kid."
            mc"Bring it on, asshole!"
            show sc gymjuliet j42
            ju"Hey!"
            #Juliet is standing behind the man now. She places a hand on his shoulder and he he turns around
            show sc gymjuliet j43
            man"Huh?"
            #Juliet kicks him in the balls
            play sound "sound effects/01/hit_with_grunt.ogg"
            show sc gymjuliet j44
            with vpunch
            man"UHH!!"
            #the guy hits the ground - sound effects required
            #Juliet picks up her phone and sees close-up pics of her ass and chest
            stop sound fadeout 1.0
            play sound2 "sound effects/01/Falling Over Sound Effect.mp3"
            show sc gymjuliet j45
            ju"You should learn some manners, asshole!"
            stop sound2 fadeout 1.0
            show sc gymjuliet j47
            mc"(Wow... That was amazing!)"
            mc"(The guy dropped like a sack of potatoes!)"
            #Juliet looks at the MC
            stop sound fadeout 1.0
            stop sound2 fadeout 1.0
            show sc gymjuliet j46
            ju"So are you going to kick him out or not?"
            show sc gymjuliet j47
            mc"Absolutely! I was just getting to that."
            #The MC pulls up the half-conscious man and drags him out
            stop ambient fadeout 1.0
            stop music fadeout 1.0
            scene black
            with dissolve
            show sc gymjuliet j48
            with dissolve
            mc"Consider your membership, revoked..."
            #The man winces in pain
            play sound "sound effects/01/male_moaning_in_pain1.mp3"
            show sc gymjuliet j49
            man"Uhh..."
            #The MC escorts the man out with Juliet standing in the background looking cross and with her arms folded
            #screen goes blank
            stop sound fadeout 1.0
            scene black
            with dissolve
            scene black
            with Pause (2)

            #the MC returns from outside to find Juliet standing and watching
            play music "sound effects/01/Pump It Up2.mp3" loop fadein 1.0
            play ambient "sound effects/01/gymnasium_ambience2.ogg" loop fadein 1.0
            show sc gymjuliet j50
            mc"He’s gone now."
            show sc gymjuliet j55
            mc"My apologies for the disturbance."
            show sc gymjuliet j50
            mc"We’ve been looking for a reason to ban that guy for months. So, thank you."
            mc"It’s just a shame that it had to happen like this."
            show sc gymjuliet j51
            ju"No, I get it."
            ju"Some people just never learn."
            show sc gymjuliet j52
            ju"Thanks for trying to help back there."
            #THREE BONUS RENDERS OF JULIET (THREE NEW IMAGES OF HER IN HER FITNESS GEAR EXERCISING NEAR THE EQUIPMENT)
            #ADDED TO THE PHOTO GALLERY FOR HER
            show sc gymjuliet j58
            mc"I helped?"
            show sc gymjuliet j62
            ju"Long enough to distract him for me."
            #Juliet smiles
            #scene continues further below


        "Stay out of it":
            show sc gymjuliet j30
            mc"(This could be embarrassing for everyone if I do or say something.)"
            mc"(I’ll just leave it.)"
            show sc gymjuliet j81
            man"You need to relax, baby."
            #the man places a hand on her shoulder
            show sc gymjuliet j82
            ju"Just what the hell do you think you’re doing?"
            show sc gymjuliet j83
            man"What? I’m not doing anything, lady."
            #Juliet stands and confronts him
            show sc gymjuliet j82
            ju"Don’t call me lady."
            show sc gymjuliet j84
            man"So what if I did?"
            man"What the hell are you going to do about it, Aeon Flux?"
            show sc gymjuliet j86
            ju"Oh, nothing..."
            #The Man grins and gets cocky
            show sc gymjuliet j85
            man"I thought so."
            #the man smirks
            show sc gymjuliet j86
            ju"Except for this."
            play sound "sound effects/01/kick_to_the_gut.mp3"
            show sc gymjuliet j87
            with vpunch
            #Juliet grabs his nuts tightly
            if persistent.v_sounds_text_on == True:
                "(THWACK!!)"
            else:
                pause 1.0
            stop sound fadeout 1.0
            play sound2 "sound effects/01/male_moaning_in_pain1.mp3"
            man"AHH!"
            #Juliet head-butts the man and he hits the ground - sound effect required
            show sc gymjuliet j45
            ju"You should learn some manners, asshole!"
            show sc gymjuliet j47
            mc"(Wow... That was amazing!)"
            mc"(The guy dropped like a sack of potatoes!)"
            #Juliet looks at the MC
            show sc gymjuliet j46
            ju"So are you going to kick him out of here or not?"
            show sc gymjuliet j47
            mc"Yeah, I was just getting to that."
            #The MC pulls up the half-conscious man and drags him out
            stop sound2 fadeout 1.0
            stop ambient fadeout 1.0
            stop music fadeout 1.0
            show sc gymjuliet j48
            with dissolve
            mc"Consider your membership, revoked..."
            #the man winces in pain
            play sound "sound effects/01/male_moaning_in_pain1.mp3"
            show sc gymjuliet j49
            man"Uhh..."
            #The MC escorts the man out with Juliet standing in the background looking cross and with her arms folded
            #screen goes blank
            stop sound fadeout 1.0
            scene black
            with dissolve
            scene black
            with Pause (2)


            #the MC returns from outside to find Juliet standing and watching
            play music "sound effects/01/Pump It Up2.mp3" loop fadein 1.0
            play ambient "sound effects/01/gymnasium_ambience2.ogg" loop fadein 1.0
            show sc gymjuliet j58
            mc"He’s gone now."
            show sc gymjuliet j59
            ju"You know, I sure could have done with some help dealing with him."
            #she says this sarcastically
            show sc gymjuliet j55
            mc"Sorry... I should’ve come over a lot sooner."
            show sc gymjuliet j60
            mc"My apologies for the disturbance."
            show sc gymjuliet j59
            ju"It’s fine... Forget about it."
            show sc gymjuliet j55
            mc"You know, we’ve been looking for a reason to ban that guy for months. So, thank you."
            mc"It’s just a shame that it had to happen like this."
            show sc gymjuliet j59
            ju"Some people just never learn."

    #scene continues here
    show sc gymjuliet j50
    mc"So, you certainly know how to take care of yourself, huh?"
    show sc gymjuliet j59
    ju"Two years of kickboxing, three years of karate."
    show sc gymjuliet j62
    ju"Yeah, I guess you could say that."
    show sc gymjuliet j51
    ju"I also did a year of ballet when I was younger but it’s not really relevant."
    show sc gymjuliet j58
    mc"Haha!"
    mc"You never know when those special dance moves might come in handy."
    show sc gymjuliet j51
    ju"I guess so."
    show sc gymjuliet j64
    ju"Word of advice..."
    ju"If you want more women to join up here, then you have to make this gym a place where women feel safe and secure, and not have to feel like they’re being objectified."
    show sc gymjuliet j59
    ju"Not every woman is going to be able to take care of themselves like I can."
    menu:
        "Be understanding":
            show sc gymjuliet j50
            mc"I understand. And I promise that it won’t happen again."
            show sc gymjuliet j53
            mc"I’ll have a word with the boss about that to make the necessary improvements."
            show sc gymjuliet j58
            mc"And if there’s anything we can do to make your experience here a better one, then please let me know."

        "Thanks...":
            show sc gymjuliet j58
            mc"Thanks, I'll take that under consideration."
            show sc gymjuliet j60
            pause 1.5
            show sc gymjuliet j55
            mc"I mean... If there’s anything we can do to make your experience here a better one, then please let me know."
    #Juliet ponders her thoughts
    show sc gymjuliet j60
    ju"Hmm..."
    show sc gymjuliet j59
    ju"Well, maybe there is something you can do for me."
    show sc gymjuliet j58
    mc"Name it."
    show sc gymjuliet j51
    ju"If you really want to make it up to me, maybe you could offer to be my personal trainer."
    show sc gymjuliet j63
    ju"I saw your sign out the front. You’re the guy to see for one-on-one lessons, are you not?"
    show sc gymjuliet j58
    mc"Um, yeah... That’s me."
    show sc gymjuliet j55
    mc"No offence, but you don’t look like you need a personal trainer."
    show sc gymjuliet j62
    ju"I’m flattered. But I could do with a refresher."
    ju"And you did say, \"anything\". So how about it?"
    #playful back-and-forth banter and ego-stroking by both the MC and Juliet here
    show sc gymjuliet j63
    ju"Unless of course you’re all talk, and the promotion outside is all for show."
    show sc gymjuliet j58
    mc"No, I’m game. Word of warning though."
    mc"You might be pretty exhausted after you’ve endured a session with me."
    show sc gymjuliet j52
    ju"For your sake, I sure hope you live up to the hype."
    show sc gymjuliet j59
    ju"I'd hate for your ego to be bruised after only one hour of training me."
    show sc gymjuliet j54
    ju"That’s assuming you last that long."
    show sc gymjuliet j58
    mc"I’m willing to bet on myself."
    show sc gymjuliet j62
    ju"All right, deal."
    #Juliet gives him a cheeky smile
    #harry interrupts the MC and doesn’t notice that he’s talking with Juliet
    show sc gymjuliet j68
    ha"Dude, did you see the pocket rocket that was here earlier on?"
    show sc gymjuliet j65
    ha"Honestly, she had the finest set of-"
    #the MC moves so Harry can see Juliet
    show sc gymjuliet j66
    with dissolve
    ha"Cheekbones..."
    mc"Um, Juliet."
    show sc gymjuliet j70
    mc"This is Harry."
    #harry turns and sees Juliet looking at him with a closed-lip smile
    show sc gymjuliet j71
    ha"Hi there."
    show sc gymjuliet j67
    ju"Hey..."
    show sc gymjuliet j51
    ju"Thanks again for the information, [y_name]."
    show sc gymjuliet j59
    ju"You have a pretty good gym here. It certainly has a lot of potential."
    show sc gymjuliet j72
    ju"I’m just going to take a shower and then I’ll be on my way."
    #Juliet leaves and the guys watch her walk towards the showers
    show sc gymjuliet j108
    mc"(Now there's a woman who clearly won't take no crap from anyone.)"
    show sc gymjuliet j107
    mc"(She's still a tempting prospect though.)"
    show sc gymjuliet j74
    ha"You know, you could’ve told me she was still here."
    show sc gymjuliet j78
    mc"I know... But it was more fun watching you make a complete ass of yourself."
    mc"And not for the first time today."
    #Harry hangs his head in shame
    show sc gymjuliet j76
    ha"So is she going to sign up?"
    show sc gymjuliet j80
    mc"I’m not sure. She said that she’s only new to town so she could still be weighing up her options."
    mc"She did say that she was interested in a personal training session with me though."
    show sc gymjuliet j68
    ha"That’s awesome man!"
    ha"Having a hottie like her would be good for business."
    ha"You should talk to her some more when she comes back."
    ha"Maybe even ask her out."
    show sc gymjuliet j69
    mc"Why the hell would I do that?"
    show sc gymjuliet j76
    ha"Like you said. She’s only new to town, so she’s going to need someone to show her around, right?"
    show sc gymjuliet j79
    ha"And after the thing with the blond turned out to be true, the Gods are clearly shining on you right now!"
    show sc gymjuliet j77
    ha"I say let the good luck continue to ride, dude!"
    show sc gymjuliet j78
    mc"Hmm... That could be the smartest thing you’ve said all week."
    show sc gymjuliet j68
    ha"Haha! It happens, sometimes."
    # or  ha"Haha! I have my moments."
    stop ambient fadeout 1.0
    stop music fadeout 1.0
    #screen goes blank
    scene black
    with dissolve
    scene black
    with Pause (2)

    #the MC stands behind the counter and sees Juliet coming, she’s changed back into her original outfit
    play ambient "sound effects/01/gymnasium_ambience3.ogg" loop fadein 1.0
    play music "sound effects/01/Pump It Up4.mp3" loop fadein 1.0
    show sc gymjuliet j90
    with dissolve
    ju"Hey again."
    show sc gymjuliet j89
    mc"Hi..."
    show sc gymjuliet j88
    mc"So no charge today but I’m going to need you to sign out before you leave."
    show sc gymjuliet j90
    ju"Sure."
    #Juliet picks up a form and looks for her name on the sheet
    show sc gymjuliet j19
    mc"So I was thinking..."
    show sc gymjuliet j16
    mc"Seeing as you’re new to the area, I thought that maybe I could show you around, and maybe we could go for a drink or something?"
    show sc gymjuliet j13
    mc"Or perhaps we could go to a club?"
    show sc gymjuliet j18
    ju"Uh-huh..."
    #Juliet doesn’t look at the MC and continues to sign the form
    show sc gymjuliet j19
    mc"What do you think?"
    show sc gymjuliet j20
    ju"Sorry, not interested."
    #Juliet signs the form and looks up at him
    show sc gymjuliet j11
    mc"Any reason why?"
    show sc gymjuliet j09
    ju"Tell me something, [y_name]..."
    ju"Do you normally ask someone out after chatting with them for only a few minutes?"
    menu:
        "First time":
            show sc gymjuliet j89
            mc"Not normally. But as they say, there’s a first time for everything."
        "Take a chance":
            show sc gymjuliet j89
            mc"It's not usually in my nature to do so, but if you don't ask, you'll never know, right?"
    show sc gymjuliet j90
    ju"Touche."
    ju"But the answer is still no."
    show sc gymjuliet j09
    ju"Going to a club or some fancy restaurant is not my scene."
    ju"I’m just not one for getting dressed up or being around rich snobs."
    show sc gymjuliet j90
    ju"Sorry..."
    show sc gymjuliet j89
    mc"(I better back off, especially after what she did to that other guy.)"
    mc"(And also if I still plan on having kids someday.)"
    mc"Okay, duly noted. Strictly professional then."
    show sc gymjuliet j92
    ju"Thanks for the use of your equipment and everything else."
    ju"See you around."
    #she turns to leave
    show sc gymjuliet j93
    mc"(Maybe I was too eager.)"
    show sc gymjuliet j101
    mc"(I wonder if she’ll even bother coming back for that personal training session now.)"
    mc"(That’s the last time I take advice from Harry!)"
    #she then turns back
    show sc gymjuliet j104
    ju"Just to confirm... Are we still on for that one-on-one session?"
    show sc gymjuliet j102
    mc"Yes, of course."
    $ task_addfuturetask("Fitness session with Juliet",2)
    show sc gymjuliet j105
    ju"Great. I’ll give you a call to confirm a day and time."
    ju"And if you do a decent job and I get the results that I want, then who knows?"
    ju"I’ve changed my mind before."
    show sc gymjuliet j103
    mc"(Bingo.)"
    show sc gymjuliet j104
    ju"Bye, [y_name]..."
    $ task_addpoi("Juliet - New client at your gym",4)
    #she gives a cocky smile to the MC and Harry before exiting the gym
    #the MC watches her leave, staring at her ass in gym pants
    show sc gymjuliet j101
    mc"Damn..."
    #harry suddenly stands alongside the MC, watching Juliet walk away
    show sc gymjuliet j94
    ha"I take it she’s your new favorite gym member?"
    show sc gymjuliet j95
    mc"Yeah... No contest."
    show sc gymjuliet j96
    mc"But your idea didn’t work. I went down faster than a five-hundred-dollar hooker!"
    show sc gymjuliet j97
    ha"Patience, my friend."
    show sc gymjuliet j98
    ha"We both saw that sexy little smirk just before she left."
    ha"And even if nothing comes from it, you and me have got a night on the town to look forward to!"
    show sc gymjuliet j99
    ha"Where the booze will be plenty and the panties will drop!"
    show sc gymjuliet j100
    mc"Haha!"
    show sc gymjuliet j100a
    mc"(I admire his confidence, even though Harry has struck out more times than a straight guy who didn’t realise he was in a lesbian bar!)"
    show sc gymjuliet j100b
    ha"Come on, let’s get back to work..."
    stop ambient fadeout 1.0
    stop music fadeout 1.0
    #screen goes blank
    scene black
    with dissolve
    scene black
    with Pause (2)
    jump lb_ep01_The_MC_and_Harry_at_the_club

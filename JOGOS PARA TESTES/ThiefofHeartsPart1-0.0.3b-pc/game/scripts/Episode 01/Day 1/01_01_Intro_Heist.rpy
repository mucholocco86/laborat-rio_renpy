init:
    image anim_ep01_policeintro_01 = Movie(channel="movies_with_sound", loop=True, play="images/extras/Episode 01/anim_ep01_policeintro_01.webm")
    image anim_ep01_Cat_tattoo = Movie(channel="movies_with_sound", loop=False, fadeout=1.0, play='images/extras/Episode 01/anim_ep01_Cat_tattoo.webm', image=Crop((0,0,1920,1080), "#000"))
    image anim_ep01_Prologue = Movie(channel="movies_with_sound", loop=False, fadeout=1.0, play='images/extras/Episode 01/anim_ep01_Prologue.webm', image=Crop((0,0,1920,1080), "#000"))

    image sc policeintro signal interupt:
        "sc policeintro p13" with Dissolve(0.2, alpha=True)
        pause 1.0
        "sc policeintro p14" with Dissolve(0.2, alpha=True)
        "sc policeintro p14" with hpunch
        pause 1.0
        repeat

label lb_ep01_intro_01_fantasy_intro:
    #show the MC as a black shadow or silhouette so the player can't see him here"
    #Police officer appears on the screen wearing dark shades - talking to the player - https://pixhost.to/show/658/456251312_screenshot-2024-03-25-at-6-01-02-pm.jpg
    play ambient "sound effects/01/Police_Station_Ambience.ogg" loop fadein 1.0
    scene sc policeintro p01
    with dissolve
    off_justice"Hey! You there!"
    off_justice"Listen up and listen good!!"
    show sc policeintro p06
    off_justice"We need to go through some rules and regulations before you begin."
    show sc policeintro p03
    off_justice"Answer me this: Are you {b}OVER THE AGE OF 18{/b} years old?"
    #screen options: NO/YES

    menu:
        "Are you {b}OVER THE AGE OF 18{/b} years old?"
        "No":
            show sc policeintro p02
            off_justice"No? Really?"

            #the officer looks surprised and unsure what to do
            show sc policeintro p07
            off_justice"Oh..."
            show sc policeintro p06
            off_justice"Um... This is the first project I've appeared in for {i}MrDotsGames{/i}, so I'm not exactly sure what to do here."
            #She puts her finger up at the player
            show sc policeintro p09
            off_justice"Wait! I have an idea."
            show sc policeintro p01
            off_justice"Don't move a muscle, I'll be with you again shortly."
            #officer Justice looks to her side like she's talking to someone off the screen
            show sc policeintro p05
            off_justice"What am I supposed to do if they choose \"No\"?"
            #a guy speaks to the officer off the screen but we don't see him
            show sc policeintro p08
            "(Off-screen coder) How the hell should I know? I'm just a coder on minimum wage!"
            #the officer looks down and curses
            show sc policeintro p10
            off_justice"Dammit!"
            #The officer looks back at the player
            show sc policeintro p06
            off_justice"My apologies."
            show sc policeintro p02
            off_justice"Seeing as I'm playing an officer of the law, rather than one of the sexy lead characters you've seen in the previews..."
            show sc policeintro p09
            off_justice"I think I know what the right thing to do here is."
            #Officer Justice extends her arms and points for the player to leave
            show sc policeintro p06
            off_justice"Just to be safe, you better get out of here."
            show sc policeintro p01
            off_justice"So I'm going to send you back to the main menu on good behaviour."
            #The officer holds up some handcuffs
            show sc policeintro p12
            off_justice"Otherwise, I'll have to drag your ass off to juvenile detention!"
            show sc policeintro p11
            off_justice"Come back when you're older, kid..."
            stop ambient fadeout 1.0
            scene black
            with dissolve
            scene black
            with Pause (2)
            #screen goes blank - returns to the MENU
            return


        "Yes":
            show sc policeintro p06
            off_justice"Good."
            off_justice"I'd hate to have to arrest you and send you off to juvenile detention."
            show sc policeintro p09
            off_justice"Anyway, some other rules you must abide by before you can proceed."
            show sc policeintro p01
            off_justice"{b}DO NOT{/b} continue if you're easily upset or offended by foul language or lewd content."
            show sc policeintro p04
            off_justice"No whining about the characters in the story because they aren't to your liking."
            show sc policeintro p12
            off_justice"Everybody playing and also those who have made this game have different tastes, you know?"
            show sc policeintro p02
            off_justice"No jokes about my name. It wasn't funny the last fifty times!"
            show sc policeintro p09
            off_justice"And absolutely no jerking off while you're playing!"
            show sc policeintro p06
            off_justice"Are we clear on that... You daydreaming, unfunny, perverted little crybaby?"
            #The screen starts to become distorted like the feed is being taken over
            #The officer looks around and panics, she's unsure what is going on
            if persistent.v_anim_enabled:
                scene anim_ep01_policeintro_01:
                    size (config.screen_width, config.screen_height)
            else:
                play sound "sound effects/01/policeintro_signal_interupt.ogg" loop fadein 1.0
                show sc policeintro signal interupt
            pause 2.0
            off_justice"Hey! What's going on??"
            off_justice"What's happening?"
            #the screen goes blank
            off_justice"Can someone come and fix this?"
            off_justice"Where is that damn coder?"
            #the screen fades back in and we can see Ariel sitting in front of her set of computer screens
            #we can see her looking at her screens with the police officer on one, and the MC on the one next to it - https://c10.patreonusercontent.com/4/patreon-media/p/post/99666493/d40970818c8d49e2bd5eaaa84813bf17/eyJxIjoxMDAsIndlYnAiOjB9/1.jpg?token-time=1712620800&token-hash=A65J8N1y7FcG-GCd_c-TMGJ2B0XU2J-SUp5t-8rvG20%3D
            #(MC speaks)
            stop ambient fadeout 1.0
            play ambient2 "sound effects/01/town_street_night_ambience.ogg" loop fadein 1.0
            "Hey, is it done? Are you in?"
            #(Ariel speaks - https://pixhost.to/show/658/456251317_screenshot-2024-03-25-at-6-01-50-pm.jpg)

            hacker"Yeah, I'm patching you through now."
            #the screen goes fuzzy until we see Ariel taking over - she sits in front of her computer screens
            #(Ariel speaks)
            stop sound fadeout 1.0
            scene sc intro i02
            with dissolve
            hacker"Okay, you're on."
            hacker"You can talk to the player now."
            #(MC speaks)
            show sc intro i03
            "Sweet!"
            #The MC addresses the player - https://cdn.discordapp.com/attachments/396072929563246602/1221638669346275338/image.png?ex=66134eab&is=6600d9ab&hm=62d4bbfe00a28f3c1bfe2eeb96117ea689f99482e9c1d4e799835d7542ac58ba&
            #show the MC as a black shadow or silhouette so the player can't see him"
            show sc intro i06
            "Hi there!"
            show sc intro i04
            "Sorry about that folks."
            show sc intro i10
            "So if you're not aware yet, I am YOU."
            show sc intro i14
            "I know, I know. You can't see what I look like."
            show sc intro i04
            "That's kind of the point."
            show sc intro i16
            "And don't listen to that police officer. You can do anything you want in this game."
            show sc intro i15
            "Well, almost anything."
            show sc intro i01
            "I mean, you can't change the way I look or make anyone instantly fall in love with you."
            show sc intro i08
            "But hey, don't blame me."
            show sc intro i10
            "Blame the assholes that created me and this game!"
            #The MC thinks about what he said then changes his mind
            show sc intro i09
            "On second thought, don't do that."
            show sc intro i11
            "It's not good for business."
            show sc intro i01
            "Not to worry though, as there'll be plenty of hot ladies in the story to take most of your attention away from yours truly."
            show sc intro i06
            "That's what you're here for, right?"
            show sc intro i11
            "Okay, before we start, you need to choose a name."
            show sc intro i05
            ################################################################
            # Player enters their chosen name here / if empty, keep default name
            # I had to script that this "unusual way" to keep the default for the case player put in wrong names and wants default an 2nd try
            $ choice_done = False
            while not choice_done:
                $ name = renpy.input("Your first name will be (Default: [y_name]): ").strip() # Strip any leading/trailing whitespace
                if not name:
                    $ name = y_name
                $ lname = renpy.input("And your last name will be (Default: [y_lastname]): ").strip() # Strip any leading/trailing whitespace
                if not lname:
                    $ lname = y_lastname
                "So your name will be [name] [lname]."
                menu:
                    "Is this correct?"
                    "YES":
                        $ choice_done = True
                    "NO":
                        "Okay, not to worry. Let's try this again."
            $ y_name = name
            $ y_lastname = lname
            ################################################################
            play sound "sound effects/01/car_arriving.ogg"
            $ ui.timer(9.3, Play("sound2", "sound effects/01/car_idle_loop.ogg", loop=True))
            show sc intro i13
            mc"Alrighty then!"
            show sc intro i01
            mc"Now, do you have any questions?"
            show sc intro i16
            mc"It's okay, we're in a safe place here, where nobody is listening in."
            stop sound fadeout 1.0
            show sc intro i18
            off_justice"HEY!"
            off_justice"Why are you talking to the player??"
            #A police officer shines a light on the player
            play sound3 "sound effects/01/police_siren_sound_effect.mp3" fadein 1.0
            show sc intro i19
            with vpunch
            mc"Oh, shit! It's that lady cop! She's found me!"
            #the MC looks off the screen and sees the female cop
            stop sound3 fadeout 1.0
            show sc intro i20
            mc"Sorry, gotta go! See you in the game!"
            #The MC addresses the player and runs off in the opposite direction to the officer
            scene black
            with dissolve
            off_justice"Hey you! Come back here!!"
            stop sound2 fadeout 1.0
            stop ambient2 fadeout 1.0
            #We see the officer go across the screen, chasing after him
            #the screen fades and the game officially begins"
            scene black
            with Pause (2)
            $ quick_menu = False
            if persistent.v_anim_enabled:
                scene anim_ep01_Prologue:
                    size (config.screen_width, config.screen_height)
                pause 7.0
            else:
                show ep01 prologue
                with dissolve
                pause 3.0
            scene black
            with dissolve
            scene black
            with Pause (2)
            jump lb_ep01_intro_02_heist_scene


label lb_ep01_intro_02_heist_scene:
    $ quick_menu = True
    play music "sound effects/01/Spy Glass.mp3" loop fadein 1.0
    scene sc mansionoutside o01
    with dissolve
    hacker"[y_name]? Can you hear me okay?"
    #just show younger sis' face talking to the MC. She has headphones on"
    show sc mansionoutside o07
    mc"Yep, loud and clear, {i}Mini Marvel{/i}."
    #show the younger sis"
    play sound "sound effects/01/Ariel_laughing2.mp3"
    show sc mansionoutside o24
    hacker"Haha!"
    stop sound fadeout 1.0
    show sc mansionoutside o08
    mc"All good on your end, too?"
    #show the younger sis"
    show sc mansionoutside o24b
    hacker"Yep, I can hear you perfectly, {i}Comedy Crusader{/i}."
    show sc mansionoutside o07
    mc"What about you, {i}Papa Bear{/i}?"
    #(show F sitting in the van with Younger Sis)"
    show sc mansionoutside o13
    leader"Yep, I can hear you."
    show sc mansionoutside o15
    leader"And don't call me {i}Papa Bear{/i}, dammit! Focus on the job."
    show sc mansionoutside o10b
    mc"Yes, sir!"
    #show the younger sis"
    show sc mansionoutside o19
    mc"Tell me what you see."
    show sc mansionoutside o01a
    hacker"There are six security guys on the ground by my count, [y_name]. Four at the front..."
    show sc mansionoutside o01b
    hacker"Two in the back."
    show sc mansionoutside o07aa
    hacker"And I can see you, of course."
    show sc mansionoutside o05
    hacker"One of the security guys is about to walk past you."
    hacker"Once he does, you can make your move."
    show sc mansionoutside o04
    mc"Roger that."
    show sc mansionoutside o02
    #[Wait / Make your move]

    menu:
        "Wait":
            show sc mansionoutside o08
            mc"Just one more thing..."
            show sc mansionoutside o07bb
            mc"Do you think my nose looks big in this?"
            #show the MC's face, with the fake nose, wig and glasses"
            show sc mansionoutside o21
            hacker"Oh [y_name]..."
            play sound "sound effects/01/Ariel_laughing3.mp3"
            show sc mansionoutside o24
            hacker"Haha!"
            #the security is close to the MC and walks past where he is hidden"
            stop sound fadeout 1.0
            show sc mansionoutside o15
            leader"You're wasting valuable time, [y_name]!"
            show sc mansionoutside o10
            leader"Get moving."
            show sc mansionoutside o10b
            mc"Okay, okay."
            show sc mansionoutside o25
            mc"I'm making my move now, over."
            hacker"GO!"
            #(show the MC walking towards the house as soon as the security member goes by him)"

        "Make your move":

            #the security is close to the MC and walks past where he is hidden"
            show sc mansionoutside o25
            mc"All right, making my move now, over."

            #(show the MC walking towards the house as soon as the security member goes by him)"

    #(scene continues)"
    play sound "sound effects/01/fast_footsteps_on_concrete.mp3" loop fadein 1.0
    show sc mansionoutside o26
    hacker"Run [y_name]! Run!"
    mc"(Oh shit!)"
    show sc mansionoutside o12
    hacker"He's on his way past security, guys."
    stop sound fadeout 1.0
    show sc mansionoutside o21
    hacker"I've lost visual contact with you, [y_name]."
    show sc mansionoutside o20
    leader"Did they catch him?"
    hacker"I don't know."
    show sc mansionoutside o21
    hacker"Please confirm your current position."
    show sc mansionoutside o27
    mc"I'm at the back of the house."
    show sc mansionoutside o27a
    hacker"All right, I see you again now."
    show sc mansionoutside o29
    mc"Great! Tell me what to do from here."
    #thumping noise on the side of the van near where Victor is sitting
    play sound "sound effects/01/banging_on_the_van_effect.mp3"
    show sc mansionoutside o97
    pause 2.0
    #a stoner looking guy knocks on the drivers door
    #victor looks angry
    stop sound fadeout 1.0
    show sc mansionoutside o98
    leader"Huh?"
    show sc mansionoutside o100
    pause 2.0
    show sc mansionoutside o98
    leader"What the hell do you want??"
    show sc mansionoutside o101
    stoner"Yo dude, when do you open? I got me some cravings for a chilli dog."
    show sc mansionoutside o99
    leader"Fuck off! We're closed for renovations!"
    show sc mansionoutside o102
    stoner"Dude..."
    #the stoner leaves disappointed
    show sc mansionoutside o29
    mc"What was that all about?"
    show sc mansionoutside o13a
    leader"Never mind."
    show sc mansionoutside o16
    leader"Anyway, the party is currently taking place on the other side of the premises and will shortly move inside."
    leader"So what you're going to do is enter through the back entrance which leads to the kitchen."
    show sc mansionoutside o30
    leader"Can you see it?"
    #show the back entrance to the house from the MC's POV"
    mc"Yeah, I'm pretty close."
    show sc mansionoutside o01c
    leader"Security is working on a loop."
    show sc mansionoutside o12a
    leader"By my estimation, from where you are, you'll have about ten seconds to get to the back door without risking being spotted."
    show sc mansionoutside o16
    leader"Do you remember the plan from there?"
    show sc mansionoutside o30
    mc"Yeah, the door should have been left unlocked by..."
    #show the older sis in a maid's outfit"
    female_v"It's already unlocked, [y_name]. You're good to go."
    menu:
        "Open the door":
            play sound "sound effects/01/Door_Opening.mp3"
            show sc mansionoutside o31
            mc"All right, I'll see you in a bit."
            stop sound fadeout 1.0
    scene black
    with dissolve
    scene black
    with Pause (2)
    #show the older sis in her waitress outfit, just the top half"
    show sc mansionkitchen k05
    with dissolve
    mc"All right, I'm inside."
    show sc mansionkitchen k01
    female_v"Now that you're in the kitchen, you'll probably see a few staffers in there."
    mc"Yeah, I see them."
    show sc mansionkitchen k01a
    female_v"They've been preparing food for the party for the past few hours. They'll be bringing out the birthday cake shortly."
    show sc mansionkitchen k05
    mc"Where are you right now?"
    show sc mansionkitchen k01
    female_v"I'm about to head back to the main floor to serve some guests. So you'll be on your own for this next part."
    show sc mansionkitchen k04
    mc"Don't worry about me. I got this."
    #the MC enters the back entrance which takes him into the kitchen where a heap of staff are cooking"
    show sc mansionkitchen k06a
    female_v"Okay... On the other side of the room, you'll see a door that leads to the main room."
    female_v"By the time you get there you should be able to see me among all the party guests."
    show sc mansionkitchen k01
    female_v"Try not to draw attention to yourself."
    show sc mansionkitchen k06
    mc"Can do."
    #show the MC walking through the kitchen area like Arnie does in "True Lies"- have the MC moving frame by frame from one spot to another, until he is almost at the swing doors of the kitchen."
    show sc mansionoutside o20
    hacker"How's it all going, [y_name]?"
    show sc mansionkitchen k07
    mc"I'm almost there."
    show sc mansionkitchen k12
    head_chef"Excuse me, Sir?"
    #the MC turns around and the head_chef is looking at him"
    head_chef"What do you think you're doing here?"
    #[Confident reply / Smartass reply]
    show sc mansionkitchen k10
    mc"(Oh shit!)"
    show sc mansionkitchen k16c
    menu:
        "Confident reply":
            show sc mansionkitchen k21
            mc"Who, me?"
            show sc mansionkitchen k19
            head_chef"Yeah, you."
            head_chef"What are you doing in my kitchen?"
            show sc mansionkitchen k26
            mc"Well, I was observing the food outside as well as what the chefs are cooking up in here..."
            show sc mansionkitchen k20b
            mc"And, I have to say, I'm not very impressed."
            show sc mansionkitchen k12
            head_chef"Who are you?"
            show sc mansionkitchen k20d
            mc"You don't know? I'm the birthday boy's best friend."
            show sc mansionkitchen k16c
            mc"And he and all of our friends are really pissed off with what you and the staff have dished up so far."
            #the head_chef looks worried"
            show sc mansionkitchen k16g
            head_chef"Oh... I had no idea."
            show sc mansionkitchen k23
            mc"It's cool."
            show sc mansionkitchen k20f
            mc"But I can buy you some time before his father finds out."
            show sc mansionkitchen k16c
            mc"I’m sure you don’t want Mr. Walker to hear about his son’s dissatisfaction with the food being supplied for his birthday, do you?"
            #the head_chef panics"
            show sc mansionkitchen k16e
            head_chef"No, not at all."
            head_chef"Don't worry, I'll have my staff replace all the food outside, posthaste!"
            show sc mansionkitchen k20a
            mc"Be sure that you do."
            show sc mansionkitchen k21
            mc"Anyway, I gotta return to the party now. I'll tell my bestie that you're on the case."
            show sc mansionkitchen k14
            head_chef"Thank you, young man. I appreciate the advice."
            show sc mansionkitchen k13
            mc"Very good."
            #the head_chef leaves"
            show sc mansionoutside o20
            hacker"Good work, [y_name]. I think he bought it."
            show sc mansionkitchen k29a
            mc"Seems like it."
            show sc mansionoutside o15
            leader"Yeah... Not bad. But try to remain inconspicuous from here on out."
            show sc mansionkitchen k27
            mc"Can do, Sir."
            stop music fadeout 2.0
            scene black
            with dissolve
            head_chef"Hey, Joe! Get over here and try this pâté that you made!"



        "Smartass reply":
            show sc mansionkitchen k21
            mc"Who, me?"
            show sc mansionkitchen k19
            head_chef"Yeah, you."
            head_chef"What are you doing in my kitchen?"
            show sc mansionkitchen k26
            mc"Well, I was observing the food outside as well as what the chefs are cooking up in here, and, I have to say..."
            show sc mansionkitchen k20b
            mc"I wouldn't even feed this crap to my dog!"
            show sc mansionkitchen k16f
            head_chef"Why, what's wrong with it?"
            show sc mansionkitchen k16c
            mc"Well, how do I put this delicately..."
            show sc mansionkitchen k20d
            mc"I just came from the bathroom..."
            mc"And the guy who was in there before me sounded like he was absolutely dominating that toilet with what can only be described as painful diarrhea!"
            #the MC leans in and whispers into the chef's ear
            show sc mansionkitchen k20e
            mc"I think it was the pâté."
            show sc mansionkitchen k12
            head_chef"Oh my God, that's awful!"
            show sc mansionkitchen k20f
            mc"The cleaners are in there right now doing their best to get rid of the evidence before Mr. Walker finds out."
            show sc mansionkitchen k16f
            head_chef"You're close with Mr Walker?"
            show sc mansionkitchen k16c
            mc"I guess you could say that."
            show sc mansionkitchen k20d
            mc"I'm his son's best friend. And he and all of our friends have nothing nice to say about the food for this party."
            show sc mansionkitchen k12
            head_chef"Oh..."
            show sc mansionkitchen k16c
            mc"I’m sure you don’t want Mr. Walker to hear about his son’s dissatisfaction with the food being supplied for his birthday, do you?"
            #the head_chef panics"
            show sc mansionkitchen k16e
            head_chef"No, not at all."
            show sc mansionkitchen k17
            head_chef"Don't worry, I'll have my staff replace all the food outside, posthaste!"
            show sc mansionkitchen k26
            mc"Be sure that you do."
            show sc mansionkitchen k20f
            mc"Anyway, I must return to the party now. I'll tell my bestie that you're on the case."
            show sc mansionkitchen k14
            head_chef"Thank you, young man. I appreciate the advice and for your discretion."
            show sc mansionkitchen k13
            mc"Very good."
            #the head_chef leaves"
            show sc mansionoutside o20
            hacker"Good work, [y_name]. I think he bought it."
            show sc mansionkitchen k29a
            mc"Seems like it."
            show sc mansionoutside o15
            leader"Maybe trim down on the details next time, though."
            show sc mansionkitchen k27
            mc"Sure thing, Sir."
            stop music fadeout 2.0
            scene black
            with dissolve
            head_chef"Hey, Joe! I need to have word to you about this pâté that you made earlier..."

            #(scene continues)"


    scene black
    with dissolve
    scene black
    with Pause (2)

    #The MC casually enters the main room where the birthday party is in full swing."

    #There are a lot of young males and females and some hotter older women (mothers of the children or friends of the birthday boy), one being the MC's mom, which we will put in the background at this point."

    #Two of the women are the mother, Vivian, and also punk chick girl - but don't make them the focus. Have the birthday boy's friends in the foreground when the MC enters the room and the moms and Dads and punk girl in the background"
    play ambient "sound effects/01/people_talking_at_party1.ogg"  loop fadein 1.0
    $ renpy.music.set_volume(0.6, 0.0, channel="music")
    play music "sound effects/01/party_music#3.ogg" loop fadein 0.5
    show sc mansionhall h03
    with dissolve
    mc"Wow... This is a pretty big party for a twenty-first birthday."
    $ renpy.music.set_volume(0.2, 0.2, channel="ambient")
    $ renpy.music.set_volume(0.2, 0.2, channel="music")
    show sc mansionoutside o20
    hacker"It just shows what you can do when you have a lot of money."
    $ renpy.music.set_volume(1.0, 0.2, channel="ambient")
    $ renpy.music.set_volume(0.6, 0.2, channel="music")
    play ambient "sound effects/01/people_talking_at_party2.ogg"  loop fadein 0.4
    show sc mansionhall h05
    leader"Which is the main reason we're here."
    $ renpy.music.set_volume(0.2, 0.2, channel="ambient")
    $ renpy.music.set_volume(0.2, 0.2, channel="music")
    show sc mansionhall h03a
    hacker"There are small cameras setup around the room. We'll be your eyes and ears."
    #show younger sis and the father watching the MC from screens in their truck"
    mc"Sweet."
    #older sis approaches the MC in her waitress outfit with a tray of food"
    $ renpy.music.set_volume(1.0, 0.2, channel="ambient")
    $ renpy.music.set_volume(0.6, 0.2, channel="music")
    play ambient "sound effects/01/people_talking_at_party3.ogg"  loop fadein 0.4
    show sc mansionhall h12
    waitress"Something to eat, Sir?"
    show sc mansionhall h06
    mc"Uh, sure."
    #Rolling screen of the older sis in her waitress outfit"
    #the MC checks out her short dress"
    mc"Nice outfit."
    show sc mansionhall h08
    mc"Did you get it in the kid's department?"
    #MF refers to the very short skirting and her busty cleavage"
    show sc mansionhall h16
    waitress"Oh, shut up, [y_name]! This is all I could get on such short notice."
    show sc mansionhall h18
    mc"And I thought you were the expert on disguises and makeup."
    show sc mansionhall h16
    waitress"At least I don't look like that doofus from {i}Kings County Nine-Nine{/i}!"
    $ renpy.music.set_volume(0.2, 0.2, channel="ambient")
    $ renpy.music.set_volume(0.2, 0.2, channel="music")
    show sc mansionoutside o15
    leader"Cram it, you two."
    $ renpy.music.set_volume(1.0, 0.2, channel="ambient")
    $ renpy.music.set_volume(0.6, 0.2, channel="music")
    play ambient "sound effects/01/people_talking_at_party4.ogg"  loop
    show sc mansionhall h17
    leader"We're here to do a job."
    leader"And if you keep up the stupid banter, it will be all over before it even begins."
    show sc mansionhall h13
    mc"Okay, fine."
    show sc mansionhall h18
    mc"Is there anything else you can tell me?"
    #show members of security on the floor"
    $ renpy.music.set_volume(0.2, 0.2, channel="ambient")
    $ renpy.music.set_volume(0.2, 0.2, channel="music")
    show sc mansionoutside o20
    hacker"The main office is upstairs. It's the last door."
    hacker"All security is either on the ground floor or outside."
    $ renpy.music.set_volume(1.0, 0.2, channel="ambient")
    $ renpy.music.set_volume(0.6, 0.2, channel="music")
    play ambient "sound effects/01/people_talking_at_party5.ogg"  loop
    show sc mansionhall h20
    waitress"They've been doing random checks for each room to make sure everything's locked and secured."
    show sc mansionhall h24
    mc"What about those two guys over there?"
    #show two members of security standing between the MC and the stairwell"
    show sc mansionhall h111
    waitress"I'll distract them when the boy's mother brings out the birthday cake."
    show sc mansionhall h20
    waitress"That should be any second now."
    show sc mansionhall h25
    with dissolve
    waitress"There she is. She's about to place the cake down on the table."
    show sc mansionhall h21
    mc"Now's the time to make our move."
    show sc mansionhall h20
    waitress"Okay, I'll create a diversion."
    #show the birthday boy's mother pushing out the birthday cake towards the birthday boy"
    show sc mansionhall h24
    mc"All right, you do that while I slowly make my way towards the stairs."
    #the MC and older sister separate. The MC makes his way through the crowd"
    $ renpy.music.set_volume(0.2, 0.2, channel="ambient")
    $ renpy.music.set_volume(0.2, 0.2, channel="music")
    show sc mansionoutside o21
    hacker"Your path looks clear, [y_name]."
    $ renpy.music.set_volume(1.0, 0.2, channel="ambient")
    $ renpy.music.set_volume(0.6, 0.2, channel="music")
    play ambient "sound effects/01/people_talking_at_party6.ogg"  loop
    show sc mansionhall h26
    mc"Yeah, [b_name] currently has the security guys covered."
    show sc mansionhall h27
    #show the older sister chatting up the guards, offering them food as they check out her short dress and cleavage"
    mc"That's my cue."
    show sc mansionhall h28
    #show the MC walking through the crowd of people, then the MC moving frame by frame up the stairs, until he is up onto the top floor"
    mc"A walk in the park."
    show sc mansionhall h29
    mc"I'm heading up the stairs."
    $ renpy.music.set_volume(0.2, 0.2, channel="ambient")
    $ renpy.music.set_volume(0.2, 0.2, channel="music")
    show sc mansionoutside o20
    hacker"You're almost there. The two guys on the floor are still talking with [b_name]."
    $ renpy.music.set_volume(1.0, 0.2, channel="ambient")
    $ renpy.music.set_volume(0.6, 0.2, channel="music")
    play ambient "sound effects/01/people_talking_at_party.ogg"  loop
    show sc mansionhall h112
    mc"Yeah, \"talking\"..."
    show sc mansionhall h30
    mc"Okay, I'm on the top floor."
    show sc mansionhall h31
    leader"Make your way to the office door before security sees you."
    show sc mansionhall h32
    mc"Doing that right now, over..."
    stop ambient fadeout 1.0
    stop music fadeout 1.0
    $ renpy.music.set_volume(1.0, 1.0, channel="music")
    #(screen goes blank)"
    scene black
    with dissolve
    scene black
    with Pause (2)
    jump lb_ep01_intro_03_heist_scene

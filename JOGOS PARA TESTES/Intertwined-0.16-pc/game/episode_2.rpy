label Episode_2_Start:

    #KoGa3 START#
    $ KoGa3GameProgress = "Ep2"
    #KoGa3 END#

    $ achievement.grant("ACHIEVEMENT_EPISODE_1")
    $ achievement.sync()
    $ Layla_Week1_Monday_Payattention = False
    $ Layla_Week1_Monday_Four = False
    $ Layla_Week1_Monday_Legs = False
    $ Layla_Week1_Monday_Sand = False
    $ Alexis_Week1_Monday_TellZach = False
    $ Alexis_Week1_Monday_BarWait = False
    $ Elena_Week1_Tuesday_Science_Complain = False
    $ Elena_Week1_Tuesday_Intervene = False
    $ Erynn_Week2_Tuesday_AlexisFight = False

    jump Week1_Monday_Geography

label Week1_Monday_Geography:
    scene black with Dissolve(1)
    pause 2
    scene 02_001 with Dissolve(1)
    t "Good morning, [mc]."
    t "I see you've finally arrived..."
    tc "I'm Mr Coleman, your geography teacher."
    mc "Good morning, sir."
    scene 02_002 with Dissolve(1)
    tc "You know you're fifteen minutes late, right?"
    menu:
        "Apologise[KoGa3AutoWTChange1]{size=-4}(MC GoodStudent+2) {/size} {/color}":
            $ MC_GoodStudent += 2
            # MC_GoodStudent (4)
            mc "Sorry, Mr Coleman. It won't happen again."
        "Don't apologise":
            mc "Story of my life..."
            tc "Excuse me?"
            mc "It's my first day. I got lost and ended up on the wrong floor."
            x "Heh..."
    scene 02_003 with Dissolve(1)
    tc "Well... Let's not waste more time."
    tc "You can take the empty desk next to Layla."
    tc "And open your book to page sixty-eight."
    mc "I don't have my books yet. I'll pick them up later today."
    tc "Then you'll have to share with someone for now."
    scene 02_004 with Dissolve(1)
    mc "{i}(That's the girl from earlier, the one who was also late.){/i}"
    mc "{i}(Why does she look annoyed?){/i}"
    mc "{i}(Maybe Mr Coleman gave her the same speech about punctuality.){/i}"
    scene 02_005 with Dissolve(1)
    mc "{i}(Hmm... So her name is Layla.){/i}"
    la "I'll share with you."
    mc "Thanks."
    la "Let's move our desks together."
    scene 02_006 with Dissolve(1)
    la "Hey."
    mc "Hi."
    la "I'm Layla."
    mc "[mc]."
    if MC_Week1_Monday_Skip == True:
        la "Yeah, I know..."
    else:
        la "Nice to meet you."
    tc "Alright, class. Let's get back to it. Where were we? Right... Egypt!"
    scene 02_007 with Dissolve(1)
    la "You smell good."
    mc "Thanks."
    la "What perfume is that?"
    mc "Uh... It's aftershave."
    scene 02_008 with Dissolve(1)
    la "Aftershave?"
    la "Well, you kinda missed a few spots shaving. Just saying."
    mc "Heh..."
    scene black with Dissolve(1)
    pause 2
    scene 02_009 with Dissolve(1)
    mc "..."
    mc "{i}(*Sigh* This is so boring. What time is it?){/i}"
    mc "{i}(Only five minutes in...){/i}"
    mc "{i}(Come on. Are you kidding me? *Sigh*){/i}"
    scene 02_010 with Dissolve(1)
    mc "{i}(Hmm... Seems like someone is paying attention.){/i}"
    mc "{i}(Maybe she likes geography? Nah... Who actually likes geography?){/i}"
    mc "{i}(Still... She's really cute. Way more interesting than whatever Mr Coleman is droning on about.){/i}"
    menu:
        "Pay attention[KoGa3AutoWTChange1]{size=-4}(Layla Week1 Monday Payattention, MC GoodStudent+2) {/size} {/color}":
            $ Layla_Week1_Monday_Payattention = True
            $ MC_GoodStudent += 2
            # MC_GoodStudent (6)
            scene 02_011 with Dissolve(1)
            mc "{i}(Okay, okay. Better pay attention. He keeps looking over here already.){/i}"
            scene 02_012 with Dissolve(1)
            tc "[mc]!"
            mc "Yes?"
            tc "Into which sea does the Nile river flow?"
            scene 02_021 with Dissolve(1)
            mc "That would be the Mediterranean Sea."
            tc "Correct. Good to see you're paying attention."
            mc "{i}(See! I knew it! How about you focus on some other students now?){/i}"
            jump Week1_Monday_Geography_End
        "Check her out[KoGa3AutoWTChange1]{size=-4}(Layla Points+2) {/size} {/color}":
            $ Layla_Points += 2
            # Layla (4)
            scene 02_014 with Dissolve(1)
            if MC_Week1_Monday_Skip == True:
                mc "{i}(Now that I'm sitting next to her... Why did I even think she could be a teacher?){/i}"
            else:
                pass
            mc "{i}(She looks so young. Is she even eighteen yet? Looks more like sixteen.){/i}"
            mc "{i}(Could be one of those smart kids who skipped a few grades.){/i}"
            mc "{i}(Very cute face though.){/i}"
            scene black with Dissolve(1)
            transform moveup:
                xalign 0.5 yalign 1.0
                linear 5.0 yalign 0.0
            show 02_015 at moveup
            ""
            scene 02_016 with Dissolve(1)
            mc "{i}(And her skirt... Isn't that too short for school?){/i}"
            mc "{i}(Not that I'm complaining, she's got great legs.){/i}"
            tc "[mc]!"
            scene 02_017 with vpunch
            mc "{i}(!!!){/i}"
            mc "{i}(Shit, shit, shit...){/i}"
            scene 02_012 with Dissolve(1)
            tc "So?"
            mc "Yes?"
            tc "Answer the question."
            scene 02_018 with Dissolve(1)
            mc "Uh..."
            mc "{i}(Wait... What was the question?){/i}"
            mc "{i}(We were talking about Egypt, right?){/i}"
            mc "{i}(So uh... Pyramids? Pharaohs? Maybe sand? Lots of sand... Must be sand right?){/i}"
            mc "{i}(I'm totally blanking here.){/i}"
            scene 02_019 with Dissolve(1)
            la "*Whispers* Pssst... Hey..."
            mc "Huh?"
            la "*Whispers* Four!"
            tc "I'm waiting..."
            mc "{i}(What is she saying?){/i}"
            scene 02_020 with Dissolve(1)
            la "*Whisper* The answer is four!"
            menu:
                "Four[KoGa3AutoWTChange1]{size=-4}(Layla Week1 Monday Four, Layla Points+2) {/size} {/color}":
                    $ Layla_Week1_Monday_Four = True
                    $ Layla_Points += 2
                    # Layla (6)
                    scene 02_021 with Dissolve(1)
                    mc "The answer is... four!"
                    tc "Four?"
                    mc "Yes."
                    scene 02_023 with Dissolve(1)
                    tc "So, the Nile flows into the famous Four Sea?"
                    mc "{i}(Shit... Yeah, that's uh... She got me...){/i}"
                    st "Haha."
                    scene 02_024 with Dissolve(1)
                    tc "This is geography, not math!"
                    tc "Then again... I could've fore-sea-n not to expect much from someone who couldn't find his classroom."
                "Sand[KoGa3AutoWTChange1]{size=-4}(Layla Week1 Monday Sand) {/size} {/color}":
                    $ Layla_Week1_Monday_Sand = True
                    scene 02_021 with Dissolve(1)
                    mc "Uh... Sand?"
                    tc "Sand?"
                    mc "Yes."
                    scene 02_023 with Dissolve(1)
                    tc "So, the Nile flows into the mythical Sand Sea?"
                    mc "{i}(Shit... Yeah, that's uh...){/i}"
                    st "Haha."
                    scene 02_024 with Dissolve(1)
                    tc "This is geography, not arenology."
                    mc "{i}(Areno... What's that?){/i}"
                    tc "Then again, I shouldn't expect too much from someone who struggled to find the right classroom."
                "Layla's legs[KoGa3AutoWTChange1]{size=-4}(Layla Week1 Monday Legs, Layla Points+2) {/size} {/color}":
                    $ Layla_Week1_Monday_Legs = True
                    $ Layla_Points += 2
                    # Layla (6)
                    scene 02_022 with Dissolve(1)
                    mc "Honestly, no idea... I got distracted by Layla's legs."
                    tc "Excuse me?"
                    st "Haha."
                    scene 02_024 with Dissolve(1)
                    tc "You think this is funny?"
                    tc "Then again, I shouldn't expect too much from someone who struggled to find the right classroom."
            st "Hahaha..."
            mc "{i}(Thanks, asshole!){/i}"
            tc "Now start paying attention!"
            scene 02_025 with Dissolve(1)
            la "Haha..."
            if Layla_Week1_Monday_Legs == True:
                la "I can't believe you just said that..."
                mc "At least I'm honest."
                la "Haha. I liked your answer though. Thanks for the compliment!"
                tc "Layla, please answer the question."
            else:
                if Layla_Week1_Monday_Four == True:
                    la "I can't believe you actually said it..."
                    mc "Really? Four...? Thanks a lot for that!"
                    la "Haha. You're welcome."
                    mc "{i}(Can't believe I fell for that. I'll get her back for this!){/i}"
                    tc "Layla, please answer the question."
                else:
                    la "I can't believe you just said sand..."
                    mc "Yeah. Real funny... Like four was the correct answer?"
                    la "Still a better answer than sand... Haha."
                    mc "{i}(Alright, laugh it up... I'll remember this.){/i}"
                    tc "Layla, please answer the question."
            scene 02_026 with Dissolve(1)
            la "The Mediterranean Sea."
            tc "Correct!"
            tc "Good to know someone is actually paying attention."
            tc "Let's continue."
            tc "In northern Egypt, the river splits in two and forms a large delta."
            scene 02_027 with Dissolve(1)
            la "What?"
            mc "Nothing..."
            mc "{i}(I'll get her back for that... But I'd better pay attention for now.){/i}"
            jump Week1_Monday_Geography_End

label Week1_Monday_Geography_End:
    scene 02_013 with Dissolve(1)
    n "Class continued for what felt like an eternity."
    scene black with Dissolve(1)
    pause 2
    scene 02_028 with Dissolve(1)
    mc "{i}(Finally.){/i}"
    mc "{i}(And that was just the first hour... *Sigh*){/i}"
    tc "[mc], can I have a word before you go?"
    scene 02_029 with Dissolve(1)
    mc "{i}(Seriously...? What now?){/i}"
    mc "Uh... Of course, Mr Coleman."
    scene 02_030 with Dissolve(1)
    tc "I know it's your first day here, so I'll let it slide this time."
    tc "But just so you know, I run a tight ship."
    mc "{i}(Who does he think he is? A captain? 'I am the captain now.'){/i}"
    mc "{i}(Ugh... This is exactly why I get into trouble. I zone out the second something feels pointless.){/i}"
    tc "No more late arrivals. Understood?"
    if Layla_Week1_Monday_Payattention == True:
        scene 02_031 with Dissolve(1)
        mc "Understood. It won't happen again."
        tc "Good. Off you go."
        scene 02_032 with Dissolve(1)
        mc "{i}(That could've been worse...){/i}"
    else:
        scene 02_031 with Dissolve(1)
        mc "It won't hap..."
        tc "Secondly!"
        mc "{i}(I was apologising...){/i}"
        scene 02_030 with Dissolve(1)
        tc "I expect everyone to pay attention in my class."
        tc "I get it... Layla's a cute girl..."
        mc "{i}(Wait? What now?){/i}"
        scene 02_031 with Dissolve(1)
        tc "But your eyes should be on the lesson, not on her."
        mc "Yes, sir. Got it. Won't happen again."
        tc "Good. Off you go."
        scene 02_032 with Dissolve(1)
        mc "{i}(Pervert...){/i}"
        mc "{i}(Better watch out for this one.){/i}"
    jump Week1_Monday_Hallway

label Week1_Monday_Hallway:
    scene 02_033 with Dissolve(1)
    if Layla_Week1_Monday_Payattention == True:
        la "Hey..."
        mc "{i}(Layla, was it? Is she waiting for me?){/i}"
        scene 02_034 with Dissolve(1)
        la "I hope he didn't scold you too much."
        mc "Just the usual talk about being late."
        la "Yeah, he's got a thing for punctuality."
        la "Come on. I'll walk you to the next class."
        x "[mc]?"
    else:
        la "Hey..."
        mc "{i}(Great! More trouble...){/i}"
        scene 02_035 with Dissolve(1)
        la "I hope he didn't go too hard on you."
        mc "..."
        la "Don't look so grumpy."
        la "Come on. I'll walk you to the next class."
        scene 02_036 with Dissolve(1)
        if MC_Week1_Monday_Skip == True:
            mc "I've got a school plan, remember?"
        else:
            mc "I've got a school plan. I'll manage."
        la "It was a joke..."
        x "[mc]?"
    scene 02_037 with Dissolve(1)
    x "Oh, it is you!"
    menu:
        "Who are you?":
            mc "Uhm... Do I know you?"
            z "You can't have forgotten me, dude... It's Zach!"
            mc "Oh damn... Zach."
            z "Yeah!"
            mc "Nope, still no idea."
            z "..."
            mc "Just kidding, man."
            z "Geez... Don't scare me like that."
        "Zach?":
            mc "Zach?"
            z "The one and only!"
    scene 02_038 with Dissolve(1)
    mc "Hey, it's been a while. How've you been?"
    z "I've been good. How about you? When did you get back?"
    mc "Yesterday, actually."
    scene 02_039 with Dissolve(1)
    z "Yesterday? And you have to be here today?"
    z "I feel you, man."
    z "Anyway, how long has it been? Five, six, seven years?"
    mc "Yeah, something like that."
    z "Man, we seriously need to catch up. Got loads to tell you."
    z "Oh, almost forgot..."
    scene 02_040 with Dissolve(1)
    z "Hey, babe!"
    la "I told you to stop calling me 'babe', Zachary!"
    scene 02_041 with Dissolve(1)
    mc "Oh? You two dating?"
    z "Not yet..."
    la "Not ever!"
    scene 02_042 with Dissolve(1)
    t "Zach! Inside, please!"
    z "Yes, Naomi. Coming..."
    scene 02_043 with Dissolve(1)
    td "It's Ms Davis!"
    z "[mc], meet me at lunch in the cafeteria. We'll talk then."
    mc "Sure. Later, Zach."
    z "Later."
    scene 02_044 with Dissolve(1)
    z "Bye, babe..."
    la "*Sigh*"
    td "Zach! NOW!"
    scene 02_045 with Dissolve(1)
    la "So, you know Zach?"
    mc "Knowing is a stretch. We used to hang out when we were kids."
    la "Has he always been like that?"
    mc "Pretty much, yeah."
    if Layla_Week1_Monday_Payattention == True:
        la "Well... Come on. Or we'll be late for our next class."
        jump Week1_Monday_Cafeteria
    else:
        scene 02_046 with Dissolve(1)
        la "By the way."
        la "Still mad at me?"
        mc "No..."
        scene 02_047 with Dissolve(1)
        la "You so are..."
        mc "I'm not!"
        scene 02_048 with Dissolve(1)
        la "Okay, okay. Let's go then. Be...FOUR! we're late!"
        scene 02_049 with Dissolve(1)
        mc "*Sigh*"
        la "Hahaha..."
        scene 02_050 with Dissolve(1)
        mc "..."
        la "Hey... Come on. You gotta admit, that was funny. That was really funny!"
        scene 02_051 with Dissolve(1)
        la "Please wait, [mc]!"
        menu:
            "Wait for her":
                la "Thank you."
            "Keep going":
                mc "{i}(As if...){/i}"
                scene 02_052 with Dissolve(1)
                la "[mc]! You really are terrible with directions."
                la "It's this way. Haha..."
                mc "{i}(Dammit.){/i}"
        scene 02_053 with Dissolve(1)
        mc "Can you stop laughing already?"
        la "Sorry. Haha... You left me no choice."
        mc "Where's the next class?"
        la "Hehe..."
        scene 02_054 with Dissolve(1)
        mc "What now?"
        la "Can't say."
        mc "Why not?"
        la "You're gonna be mad at me again."
        mc "Just spit it out."
        scene 02_055 with Dissolve(1)
        la "Classroom 4! Hahaha."
        mc "Really? Haha."
        mc "I never thought I could hate a number... But here we go."
        la "Hahaha."
        mc "Haha."
        jump Week1_Monday_Cafeteria

label Week1_Monday_Cafeteria:
    scene black with Dissolve(2)
    pause 2
    scene 02_056 with Dissolve(1)
    z "Hey, [mc]! Over here!"
    scene 02_057 with Dissolve(1)
    mc "Hey."
    mc "Thanks for saving me a seat."
    z "Sure thing, man."
    mc "I'm starving."
    z "Same here. Let's grab something. Burgers today. They're really good!"
    mc "Sounds perfect!"
    scene 02_058 with Dissolve(1)
    z "So... How's the new school treating you?"
    menu:
        "Good":
            mc "Hmm... So far, so good."
            mc "Looks like a fun class."
        "So-so":
            mc "Not sure yet. That Coleman guy's kinda annoying."
            z "Oh yeah, the geography dude. Watch out for him."
            z "He'll fail you without batting an eye."
            mc "Good to know."
    scene 02_059 with Dissolve(1)
    mc "How about you? When did you transfer here?"
    z "Hmm... It's been a while. Three, maybe four years."
    mc "Any particular reason?"
    scene 02_060 with Dissolve(1)
    z "The reason's sitting right behind me."
    scene 02_061 with Dissolve(1)
    mc "Who? Layla?"
    mc "{i}(Shit... Did she hear that?){/i}"
    mc "So, something going on between you two?"
    scene 02_062 with Dissolve(1)
    z "Nah. But not for lack of trying."
    z "Actually, I got kicked out of my last school."
    mc "You too? What happened?"
    z "Long story. Doesn't really matter now. Besides, the football team's way better here."
    mc "Hope so. This is a sports school."
    scene 02_063 with Dissolve(1)
    el "So, I told him that he..."
    el "Are you even listening?"
    scene 02_064 with Dissolve(1)
    el "HEY! Layla!"
    scene 02_065 with Dissolve(1)
    la "What?"
    el "I was talking to you..."
    la "Sorry, El. I got distracted."
    el "I can tell."
    el "So, what's going on between you and the new guy, anyway?"
    scene 02_066 with Dissolve(1)
    la "Nothing's going on."
    la "Just a bit of harmless flirting."
    el "Harmless flirting? Remember what happened with... *Sigh*. You know who."
    la "I know..."
    el "I'm just looking out for you, Layla. Okay?"
    scene 02_067 with Dissolve(1)
    la "I know you are!"
    la "He seems different though..."
    la "{i}(Or maybe it's me who feels different?){/i}"
    el "You had two classes with him..."
    la "..."
    scene 02_068 with Dissolve(1)
    mc "{i}(Hmm... Why does she suddenly look sad?){/i}"
    z "Speaking of football..."
    mc "Sorry, what?"
    z "Football. Are you planning to join the team?"
    scene 02_069 with Dissolve(1)
    mc "I'm not sure yet. Haven't played much since I left Madison Springs."
    mc "The school in Alvarado had a shit team, and I lost interest quickly. Quit after just two weeks."
    z "How about this..."
    z "After school, we hit up this cool bar I know."
    scene 02_070 with Dissolve(1)
    z "Loads of hot college chicks hang out there."
    z "We grab some beers, talk football, maybe get lucky and meet some ladies."
    z "Trust me, I'm the perfect wingman."
    mc "{i}(Perfect wingman, huh? Can't wait to see that in action.){/i}"
    mc "Sounds awesome!"
    z "Alright, it's a plan."
    jump Week1_Monday_Bar

label Week1_Monday_Bar:
    scene black with Dissolve(2)
    pause 2
    n "Monday, 18:36."
    stop music fadeout 1.0
    scene 02_071 with Dissolve(1)
    play music "Sounds/Street_Traffic.mp3" volume 0.6
    mc "{i}(This must be the bar. Yeah... There he is.){/i}"
    mc "{i}(He wasn't kidding about the hot college chicks.){/i}"
    mc "{i}(We're not even inside, and he's already chatting one up. Maybe he really is the perfect wingman. Who would've thought?){/i}"
    scene 02_072 with Dissolve(1)
    x "Come on, let's go. Don't waste your time with this guy, Anna!"
    z "What?"
    z "Hey. Where are you going?"
    scene 02_073 with Dissolve(1)
    mc "Hey, Zach!"
    z "Girls... Wait up! My friend's here. How about a double date?"
    z "Anna?"
    z "At least give me your number..."
    z "*Sigh*"
    mc "{i}(Maybe not...){/i}"
    scene 02_074 with Dissolve(1)
    z "Yo, [mc]! You made it."
    mc "Everything alright?"
    z "Yeah..."
    mc "What's with the girls?"
    scene 02_075 with Dissolve(1)
    z "Them? Nah... not my type. And honestly, they weren't that pretty. We can do better."
    x "We heard that, you asshole!"
    mc "{i}(Not that pretty? Dude must have crazy high standards...){/i}"
    z "Let's go inside!"
    mc "Sure."
    stop music fadeout 1.0
    scene 02_076 with Dissolve(1)
    play music "Sounds/Bar_Background.mp3" volume 0.3
    z "So, this is it. Not many people here today."
    mc "It's still early, and it's Monday. Not many go drinking on Mondays."
    z "True, true."
    scene 02_077 with Dissolve(1)
    z "Let's sit at the bar. The bartender's really hot too."
    mc "What? The guy?"
    z "Wha... NO! The girl!"
    mc "Haha. Okay."
    scene 02_078 with Dissolve(1)
    z "What do you think of the place?"
    mc "From the outside, I thought it'd look different."
    z "That's what everyone says. A few years ago, they modernized all the buildings on this street."
    z "But the owner kept the old look inside and just updated the facade to match the others."
    mc "Good choice. It's got a nice vibe. Good music, too."
    z "Right?"
    scene 02_079 with Dissolve(1)
    z "On Fridays and weekends, it turns into more of a club."
    z "Sometimes they have live bands or solo acts."
    z "And you gotta come on game night. The place is packed with Marauder fans watching the game live. It's awesome."
    scene 02_080 with Dissolve(1)
    mc "Sounds like a popular spot."
    mc "Maybe I should tell my mom about it. She might get some ideas for her new café."
    z "You mean the café opening on Madison Square?"
    mc "Yeah."
    scene 02_081 with Dissolve(1)
    z "That's your mom's?"
    mc "Uh-huh."
    z "Good location. Madison Square's always crowded, especially in tourist season."
    mc "I told her the same."
    z "You'll meet tons of cute girls as a barista."
    z "..."
    scene 02_082 with Dissolve(1)
    z "Man, you gotta hook me up. Tell your mom I'm the best guy for the job."
    mc "Haha, I'll talk to her."
    z "Awesome. You're back only a day and life's already looking up."
    mc "Hehe."
    z "I've got so many plans. Our senior year is gonna be awesome..."
    mc "Can't wait!"
    if Alexis_Intro_Ignore == True:
        scene 02_083 with Dissolve(1)
        x "Hey, boys. Can I get you anything?"
        mc "Hi."
        z "Hey, Alexis. Two beers, please."
        a "Sure."
        scene 02_088 with Dissolve(1)
        z "So, what do you think? Told you she's hot."
        mc "She's pretty."
        mc "{i}(Do I know her from somewhere? Feels like I've seen her before.){/i}"
        mc "{i}(Hmm... Maybe I'm imagining things.){/i}"
        scene 02_089 with Dissolve(1)
        a "Here are your beers."
        mc "Thanks."
        scene 02_090 with Dissolve(1)
        z "Thanks, babe."
        a "Really? Still with the babe thing?"
        z "I'll stop when you give me your number..."
        a "I told you. Never gonna happen!"
        scene 02_091 with Dissolve(1)
        z "As a wise man once told me. Never say never!"
        mc "{i}(Wise man? Isn't that from that one song? What's his name again? Something with beaver?){/i}"
        a "..."
        z "Just think about it."
        a "No, thanks."
        scene 02_092 with Dissolve(1)
        play sound "Sounds/Phone_Vibrate.mp3"
        n "*Bzzzt. Bzzzt*"
        z "Man... What now? I was just getting somewhere with her."
        mc "{i}(That was 'getting somewhere'? This is gonna be something else.){/i}"
        scene 02_093 with Dissolve(1)
        z "Hello?"
        z "I'm at a bar with a friend..."
        z "What do you want?"
        scene 02_094 with Dissolve(1)
        z "Shit! That's today?"
        z "Can't it wait?"
        z "Okay, okay. I get it... I'm on my way."
        z "Twenty minutes... Yeah. Bye."
        scene 02_095 with Dissolve(1)
        z "Sorry man... That was my sister."
        z "Totally forgot I had to help her out today."
        mc "Don't worry about it."
        mc "We can do this another time."
        scene 02_096 with Dissolve(1)
        z "True."
        z "Well, see it this way. At least you got a free beer today."
        mc "Free? You haven't even paid yet."
        z "Haha... Next time, it's on me. See you tomorrow."
        mc "Later, man."
        scene 02_097 with Dissolve(1)
        mc "{i}(So much for the perfect wingman.){/i}"
        mc "{i}(Guess I'll just finish these beers and head home.){/i}"
        scene 02_098 with Dissolve(1)
        a "Hey. Another one?"
        mc "No, thanks. I had to drink my buddy's too. That's enough for a Monday."
        a "Sure. Sorry, but I've been meaning to ask..."
        a "Have we met before?"
        mc "{i}(Heh... I had the same feeling earlier.){/i}"
        scene 02_099 with Dissolve(1)
        mc "I don't think so."
        a "Hmm. You just seem familiar for some reason. Oh well, sorry to bother you."
        mc "No worries."
        jump Week1_Monday_Evening
    else:
        jump Week1_Monday_Bar_Alexis

label Week1_Monday_Bar_Alexis:
    scene 02_083 with Dissolve(1)
    a "Hey, boys. Can I get..."
    scene 02_084 with Dissolve(1)
    a "Oh..."
    mc "Hi, Alexis."
    a "{i}(Didn't think I'd see him again... Or at least not this soon.){/i}"
    scene 02_085 with Dissolve(1)
    a "Uhm... Hey, [mc]! What a surprise..."
    a "How are you?"
    mc "I'm good. You?"
    scene 02_086 with Dissolve(1)
    a "I'm fine, thanks. You cut your hair."
    mc "I did indeed."
    a "Looks good."
    mc "Thanks."
    a "So... What can I get you?"
    scene 02_087 with Dissolve(1)
    z "Two beers, please?"
    a "Coming right up."
    scene 02_088 with Dissolve(1)
    z "You know her?"
    mc "Yeah!"
    if Alexis_Intro_Join == False:
        scene 02_080 with Dissolve(1)
        mc "She sat next to me on the flight yesterday."
        z "No way. Lucky bastard. Anything happen?"
        mc "We just talked."
        z "Just talked?! Man, if it were me... Whew. The things I'd do."
        scene 02_089 with Dissolve(1)
        a "Here you go. Enjoy..."
        mc "Thanks, Alexis."
        a "You're welcome, [mc]."
        scene 02_090 with Dissolve(1)
        z "Thanks, babe."
        a "Really? Still with the 'babe' thing?"
        z "I'll stop when you finally give me your number..."
        a "Told you. Never gonna happen!"
        scene 02_091 with Dissolve(1)
        z "As a wise man once told me. Never say never!"
        mc "{i}(Wise man? Isn't that from that one song? What's his name again? Something with beaver?){/i}"
        a "..."
        z "Just think about it."
        a "No, thanks."
        scene 02_107 with Dissolve(1)
        z "Dude. You're so lucky."
        mc "Why's that?"
        z "She's into you, man. She even noticed your haircut. If she wasn't, she wouldn't even bring it up."
        mc "{i}(He might actually have a point...){/i}"
        jump Week1_Monday_Bar_Alexis2
    else:
        menu:
            "Tell him everything[KoGa3AutoWTChange1]{size=-4}(Alexis Week1 Monday TellZach, Alexis Friends, Alexis Points-6) {/size} {/color}":
                $ Alexis_Week1_Monday_TellZach = True
                $ Alexis_Friends = True
                $ Alexis_Points -= 6
                scene 02_081 with Dissolve(1)
                mc "She was sitting next to me on the plane yesterday."
                z "No way... Anything happen?"
                mc "Well... We started talking, and we kinda hit it off."
                z "Aaand?"
                mc "..."
                z "Come on, man. Don't leave me hanging!"
                mc "Let's just say... I joined a new club."
                scene 02_100 with Dissolve(1)
                z "What?"
                z "Oh... The Mile High Club?"
                mc "*Nods*"
                z "No way! Dude... You fucked her? You are so freakin' lucky!"
                scene 02_089 with Dissolve(1)
                a "Here you go. Enjoy."
                mc "Thanks, Alexis."
                a "You're welcome, [mc]."
                z "Thank you, Alexis."
                a "Heh... You're welcome too."
                scene 02_101 with Dissolve(1)
                z "Next time you're on a flight, call me, alright?"
                z "*Wink* I'd like to join that club too."
                a "Real funny..."
                scene 02_102 with Dissolve(1)
                a "I can't believe you told him."
                mc "Uhm..."
                z "So... Want my number, or should I take yours?"
                a "Asshole!"
                scene 02_103 with Dissolve(1)
                bd "Hey. You good?"
                a "I'm fine... Just taking five."
                bd "Sure."
                bd "Want me to kick them out?"
                a "No. They haven't paid yet."
                scene 02_104 with Dissolve(1)
                z "Damn. I messed that up for you. Sorry, man..."
                mc "It's alright. It was just a one-time thing anyway."
                scene 02_092 with Dissolve(1)
                play sound "Sounds/Phone_Vibrate.mp3"
                n "*Bzzzt. Bzzzt*"
                z "What now..."
                scene 02_093 with Dissolve(1)
                z "Hello?"
                z "I'm at a bar with a friend..."
                z "What do you want?"
                scene 02_094 with Dissolve(1)
                z "Shit! That's today?"
                z "Can't it wait?"
                z "Okay, okay. I get it... I'm on my way."
                z "Twenty minutes... Yeah. Bye."
                scene 02_095 with Dissolve(1)
                z "Sorry man... That was my sister."
                z "Totally forgot I had to help her out today."
                mc "Don't worry about it."
                mc "We can do this another time."
                scene 02_096 with Dissolve(1)
                z "True."
                z "Well, see it this way. At least you got a free beer today."
                mc "Free? You haven't even paid yet."
                z "Haha... Next time, it's on me. See you tomorrow."
                mc "Later, man."
                scene 02_097 with Dissolve(1)
                mc "{i}(So much for the perfect wingman.){/i}"
                mc "{i}(Guess I'll finish these and head home...){/i}"
                mc "{i}(Maybe I should apologise to Alexis before I leave?){/i}"
                menu:
                    "Leave":
                        pass
                    "Apologise[KoGa3AutoWTChange1]{size=-4}(Alexis Points+2) {/size} {/color}":
                        $ Alexis_Points += 2
                        scene 02_105 with Dissolve(1)
                        bd "Another one?"
                        mc "I'm good, thanks."
                        mc "Uh... Alexis probably doesn't want to see me, but... Could you tell her I'm sorry? I shouldn't have..."
                        bd "Heh. When I was your age, I didn't always know when to keep my mouth shut either."
                        bd "You seem like a decent guy. I'll let her know."
                        mc "Thanks. Really."
                jump Week1_Monday_Evening
            "Leave out some details[KoGa3AutoWTChange1]{size=-4}(Alexis Points+2) {/size} {/color}":
                $ Alexis_Points += 2
                # Alexis (8)
                scene 02_081 with Dissolve(1)
                mc "She sat next to me on the flight yesterday."
                z "No way. Lucky bastard. Anything happen?"
                mc "We just talked."
                z "Just talked?! Man, if it were me... Whew. The things I'd do."
                scene 02_089 with Dissolve(1)
                a "Here you go. Enjoy."
                mc "Thanks, Alexis."
                a "You're welcome, [mc]."
                scene 02_106 with Dissolve(1)
                z "Thank you, Alexis."
                a "You're welcome too..."
                scene 02_107 with Dissolve(1)
                z "Dude. You're so lucky."
                mc "Why's that?"
                z "She's into you, man. She even noticed your haircut. If she wasn't, she wouldn't even bring it up."
                mc "{i}(He might actually have a point...){/i}"
                z "Look at it this way. Even if we strike out tonight, you've still got Alexis as a backup."
                mc "Wow. Calling her a backup? That's messed up, man."
                jump Week1_Monday_Bar_Alexis2

label Week1_Monday_Bar_Alexis2:
    scene 02_092 with Dissolve(1)
    play sound "Sounds/Phone_Vibrate.mp3"
    n "*Bzzzt. Bzzzt*"
    z "Man... What now?"
    z "One second."
    scene 02_093 with Dissolve(1)
    z "Hello?"
    z "I'm at a bar with a friend..."
    z "What do you want?"
    scene 02_094 with Dissolve(1)
    z "Shit! That's today?"
    z "Can't it wait?"
    z "Okay, okay. I get it... I'm on my way."
    z "Twenty minutes... Yeah. Bye."
    scene 02_095 with Dissolve(1)
    z "Sorry man... That was my sister."
    z "Totally forgot I had to help her out today."
    mc "Don't worry about it."
    mc "We can do this another time."
    scene 02_096 with Dissolve(1)
    z "True."
    z "Well, see it this way. At least you got a free beer today."
    mc "Free? You haven't even paid yet."
    z "Haha... Next time, it's on me. See you tomorrow."
    mc "Later, man."
    scene 02_097 with Dissolve(1)
    mc "{i}(So much for the perfect wingman.){/i}"
    scene black with Dissolve(1)
    pause 2
    scene 02_108 with Dissolve(1)
    a "Hey. What's with that look? Where's your friend?"
    mc "He forgot he had to help his sister with some stuff."
    mc "And sitting alone in a bar? Not exactly a good look."
    scene 02_109 with Dissolve(1)
    a "I can help with that. Want some company?"
    mc "Uh... Don't you have to work?"
    a "Don't worry. My break's coming up. It's quiet today. Dylan can handle things."
    mc "Well, sure then."
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 02_110 at moveup
    pause 3
    mc "You look good."
    a "Heh..."
    mc "What?"
    a "You look good? That's your line?"
    mc "Haha. You probably hear that every day working here. But you do... Sorry if that was lame."
    a "No... Thank you."
    if Alexis_Intro_Join == True:
        scene 02_111 with Dissolve(1)
        mc "Can I ask you something?"
        a "Of course."
        mc "Why did you just leave after the flight?"
        a "I... Uh..."
        a "..."
        a "Well... You were sleeping. Didn't want to wake you."
        mc "I had to get off the plane anyway, so..."
        scene 02_112 with Dissolve(1)
        a "{i}(I can't...){/i}"
        a "Sorry..."
        mc "It's okay. I just wondered if I said or did something wrong."
        a "You didn't."
        a "{i}(I did!){/i}"
    else:
        pass
    scene 02_113 with Dissolve(1)
    mc "Anyway... I didn't expect our reunion to be so soon."
    a "Heh, yeah. But you did expect us to meet again?"
    mc "I was hoping, to say the least. We live in the same city. It felt inevitable."
    a "You sure about that? I've lived here twenty years and I still don't know who lives five houses down."
    mc "Haha. Fair. I barely know the guy across the street from me."
    scene 02_114 with Dissolve(1)
    a "So... What brings you out drinking tonight?"
    mc "No big reason. I started at my new school today and ran into an old friend."
    mc "He said he knew a cool bar with a 'hot bartender' and dragged me along."
    a "A hot bartender, huh?"
    mc "Uh-huh."
    a "Yeah, Dylan is kind of a snack."
    scene 02_115 with Dissolve(1)
    bd "What?"
    a "Nothing."
    bd "I heard my name."
    a "You heard wrong. Back to work, Dylan!"
    bd "Yes, boss!"
    scene 02_116 with Dissolve(1)
    mc "Haha... I had the same reaction when Zach mentioned the bartender thing."
    mc "But we both know who he was actually talking about."
    a "Do we?"
    mc "Pretty sure..."
    a "..."
    scene 02_117 with Dissolve(1)
    a "This is your first time here, right?"
    mc "Yeah. I like it."
    a "Should I go ahead and put you down as a regular? Like your friend?"
    mc "Haha. He's here that often?"
    a "Oh yeah. I see him two, three times a week. Practically part of the furniture."
    scene 02_118 with Dissolve(1)
    mc "That often?"
    a "Yep. Usually trying to charm random girls. It's... pretty entertaining, honestly."
    mc "So not just at school, huh? Does he ever actually succeed?"
    a "Still waiting for his first victim."
    mc "Victim? That's cold."
    a "I mean... I feel bad for the girls, okay?"
    mc "Haha. I shouldn't laugh, he's my friend, but you're not wrong."
    scene 02_119 with Dissolve(1)
    mc "Did he ever try with you?"
    a "Occasionally..."
    mc "Heh... Occasionally? So more than once? Classic..."
    mc "Funnily enough, he offered to be my wingman today."
    scene 02_120 with Dissolve(1)
    a "Oh no-no-no... Don't take any advice from him, [mc]."
    mc "That bad?"
    a "He seems like a nice guy, but sometimes the things he says... Yeesh."
    a "And calling every girl 'babe'? It's like he's allergic to learning names. Or can't remember them."
    mc "Right? There's a girl at school he calls 'babe' too."
    scene 02_121 with Dissolve(1)
    bd "Hey, kid... Why not buy the lovely lady a drink?"
    a "Shut up, Dylan!"
    if Alexis_Points >= 5:
        bd "Just trying to help the guy out..."
        a "He doesn't need your help. He's doing just fine on his own."
        mc "Hey! I'm right here, you know. Can hear every word..."
        a "Yeah. Don't listen to him. He's an idiot."
        x "Hey, Dylan. Can I have a Martini, please? Shaken, not stirred."
    else:
        a "Don't listen to him. He's an idiot."
        x "Hey, Dylan. Can I get a Martini, please? Shaken, not stirred."
    scene 02_122 with Dissolve(1)
    bd "Sure thing. Coming right up, Jamie!"
    mc "So... Do you own this place? I thought you said you're in college?"
    a "I am. This place is Dylan's. I just work here part-time."
    mc "Ah. He called you 'boss' earlier, so I figured..."
    a "Hehe... He does that sometimes. Probably because I can be a bit bossy sometimes."
    scene 02_123 with Dissolve(1)
    a "So you'd better stay on my good side!"
    mc "That almost sounded like a threat."
    a "Maybe it is!"
    mc "..."
    scene 02_124 with Dissolve(1)
    a "Anyway... I should get back to work before Dylan reminds me who actually is the boss of this place."
    if Alexis_Points >= 5:
        mc "Oh... Kinky!"
        a "Haha. Okay. Phrasing... I remember."
    else:
        mc "Yeah."
    mc "I've kept you long enough. Thanks for the company, though."
    a "Sure. Anytime. Want another beer?"
    mc "No, it's fine."
    scene 02_125 with Dissolve(1)
    mc "{i}(Well... Might as well finish these and head home.){/i}"
    scene black with Dissolve(1)
    pause 2
    scene 02_126 with Dissolve(1)
    a "[mc]?"
    mc "Alexis?"
    a "What are your plans tonight?"
    mc "Nothing, really. Why?"
    a "My shift ends in about an hour. If you're up for it... Maybe we could hang out?"
    menu:
        "Head home[KoGa3AutoWTChange1]{size=-4}({i}Alexis Intro Join: Alexis Friends{/i}) {/size} {/color}":
            if Alexis_Intro_Join == True:
                pass
            else:
                $ Alexis_Friends = True
            scene 02_127 with Dissolve(1)
            mc "Sorry... I'd better get home before my mom kills me for being out late on a school night."
            a "Haha, totally get it. No worries."
            mc "Rain check?"
            a "Okay."
            scene 02_128 with Dissolve(1)
            mc "What do I owe you?"
            a "Nothing. This one's on me."
            mc "Thanks, Alexis. I'll see you around?"
            a "Mm-hmm. Night, [mc]."
            mc "Night."
            jump Week1_Monday_Evening
        "Wait for her[KoGa3AutoWTChange1]{size=-4}(Alexis Week1 Monday BarWait, Alexis Sex, Alexis Points+2, MC SexCounter+1, SexCounter Alexis+1) {/size} {/color}":
            $ Alexis_Week1_Monday_BarWait = True
            $ Alexis_Sex = True
            $ Alexis_Points += 2
            # Alexis (10)
            $ MC_SexCounter += 1
            # MC_Sex (2)
            $ SexCounter_Alexis += 1
            # Alexis_Sex (2)
            scene 02_129 with Dissolve(1)
            mc "Yeah, sure. I'd like that."
            a "Great. I'll come grab you when I'm done."
            mc "I'll be here."
            scene black with Dissolve(1)
            pause 2
            scene 02_130 with Dissolve(1)
            a "Thanks for waiting. Ready to head out?"
            mc "Yes."
            a "Alright."
            scene 02_131 with Dissolve(1)
            bd "Have a nice night, Lex! Don't do anything I wouldn't do!"
            a "BYE, Dylan!"
            mc "He seems like a fun boss."
            a "He's annoying, that's what he is."
            mc "Haha..."
            jump Week1_Monday_Alexis

label Week1_Monday_Alexis:
    if _in_replay:
        $ Alexis_Intro_Join = True
    stop music fadeout 1.0
    scene 02_132 with Dissolve(1)
    play music "Sounds/Street_Traffic.mp3" volume 0.6
    mc "So... What's the plan for tonight?"
    a "Plan? Hmm... How about coffee at my place?"
    scene 02_133 with Dissolve(1)
    mc "Oh? Coffee, huh?"
    a "Yes. Coffee!"
    mc "{i}(Is she serious? Or is this one of those 'coffee' situations?){/i}"
    a "You okay with taking the bus?"
    mc "Yeah, that's how I got here anyway."
    scene black with Dissolve(1)
    pause 2
    stop music fadeout 1.0
    scene 02_134 with Dissolve(1)
    play music ("Music/LoFi Upbeat 1.mp3", "Music/LoFi Upbeat 2.mp3", "Music/LoFi Upbeat 3.mp3", "Music/LoFi Upbeat 4.mp3") volume 0.2
    a "Here we are."
    mc "Wait... This is your place?"
    a "Technically, my parents' place. I usually stay at my dorm on campus, but when I don't have early classes, I crash here. It's closer to work."
    mc "{i}(This place is massive... Who are her parents? They must be loaded.){/i}"
    scene 02_135 with Dissolve(1)
    a "Come on in."
    mc "What about your parents? They won't mind?"
    a "They won't be home until much later tonight. We're good, so let's go."
    mc "{i}(She can be bossy. Like she said.){/i}"
    mc "Alright..."
    scene 02_136 with Dissolve(1)
    mc "{i}(Wow... It's even bigger inside. This is insane.){/i}"
    mc "{i}(Are her parents celebrities or something?){/i}"
    scene black with Dissolve(1)
    pause 2
    scene 02_137 with Dissolve(1)
    a "This is my room. Make yourself comfortable, sit wherever."
    mc "Sure. Thanks."
    scene 02_138 with Dissolve(1)
    a "So... How do you take your coffee?"
    mc "What?"
    a "Your coffee. How do you drink it?"
    mc "Uh... Black, please."
    a "Black it is. Be right back!"
    scene 02_139 with Dissolve(1)
    mc "{i}(Okay, now I'm officially confused... She really meant coffee?){/i}"
    mc "{i}(What am I even doing here?){/i}"
    scene black with Dissolve(1)
    pause 2
    scene 02_140 with Dissolve(1)
    mc "{i}(Look at this view...){/i}"
    mc "{i}(You can actually see the ocean from here. Unreal.){/i}"
    a "I'm back!"
    scene 02_141 with Dissolve(1)
    mc "Hey..."
    mc "Uh. Ale...xis."
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 02_142 at moveup
    pause 3
    mc "Wow. Just... Wow!"
    a "Thanks."
    scene 02_143 with Dissolve(1)
    a "You said black, right?"
    mc "Ye...ah."
    scene 02_144 with Dissolve(1)
    mc "Wha..."
    scene 02_145 with vpunch
    mc "Hi."
    scene 02_146 with Dissolve(1)
    a "Hey..."
    a "{i}(Why does he make me feel like this? I know it's wrong... But just a simple 'Hi' from him...){/i}"
    a "{i}(It gets my heart racing.){/i}"
    scene 02_147 with Dissolve(1)
    a "{i}(*Sigh* Stop overthinking, Alexis. Just enjoy the moment.){/i}"
    a "Your turn."
    a "Take your shirt off."
    scene 02_148 with Dissolve(1)
    a "{i}(Oh? How did I miss this on the plane? He has an incredible body.){/i}"
    a "{i}(Guess it's my turn again...){/i}"
    scene 02_149 with Dissolve(1)
    mc "Here, let me help with that."
    a "..."
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 02_150 at moveup
    pause 3
    mc "{i}(She's absolutely stunning.){/i}"
    a "{i}(The way he looks at me... I like it.){/i}"
    scene 02_151 with Dissolve(1)
    a "Your heart's racing."
    mc "Heh. If you could see what I'm seeing right now... Yours would be too."
    scene 02_152 with Dissolve(1)
    a "It already is."
    a "Here... Feel it."
    mc "It's beating faster than mine..."
    menu:
        "Move your hand":
            scene 02_153 with Dissolve(1)
            a "Um... That's not my heart."
            mc "It's not? Huh... Maybe my anatomy teacher was wrong."
            a "Wait... She let you..."
            scene 02_154 with Dissolve(1)
            mc "Haha, I'm kidding."
            a "Haha. Seriously..."
            mc "By the way, did I mention how much I love coffee?"
            a "Oh, do you now?"
        "Remove your hand":
            scene 02_154 with Dissolve(1)
            mc "Did I mention how much I like coffee?"
            a "Haha... You do, huh?"
    if Alexis_Intro_Join == True:
        scene 02_155 with Dissolve(1)
        a "Good thing I'm a bartender then. Have as much as you want."
        mc "This already beats our flight."
        mc "And this time... No time limit, right?"
        a "Plenty of time!"
    else:
        a "Good thing I'm a bartender then. Have as much as you want."
    scene 02_156 with Dissolve(1)
    ""
    scene 02_157 with Dissolve(1)
    a "Ah."
    mc "{i}(I love sucking tits!){/i}"
    scene 02_158 with Dissolve(1)
    a "{i}(I didn't know my nipples were this sensitive.){/i}"
    scene 02_159 with Dissolve(1)
    a "{i}(This boy is driving me insane...){/i}"
    a "{i}(I don't think I can wait much longer.){/i}"
    scene 02_160 with Dissolve(1)
    mc "{i}(She's an incredible kisser.){/i}"
    mc "{i}(Almost as... No. I shouldn't compare.){/i}"
    mc "{i}(Just kissing her and feeling her naked body against mine feels so good.){/i}"
    scene 02_161 with Dissolve(1)
    a "Let's take these off too."
    scene 02_162 with Dissolve(1)
    mc "{i}(Damn... She's teasing me with the perfect view from that mirror.){/i}"
    mc "{i}(A full 360 view.){/i}"
    mc "{i}(That's insanely hot!){/i}"
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 02_163 at moveup
    pause 3
    mc "Fuck, you're gorgeous, Alexis!"
    a "..."
    scene 02_164 with Dissolve(1)
    mc "Come here!"
    a "Are you in a hurry?"
    mc "In a hurry? I've been holding back since the moment I saw you behind that bar."
    mc "I'd say I've been very patient."
    a "Haha... fair point."
    scene 02_165 with Dissolve(1)
    a "Then let's not waste another second."
    scene 02_166 with Dissolve(1)
    ""
    scene 02_167 with Dissolve(1)
    a "Ahhh..."
    mc "You alright?"
    a "Yes..."
    scene 02_173 with Dissolve(1)
    mc "{i}(She's so wet already...){/i}"
    show 02_169
    ""
    show 02_170
    mc "{i}(This feels so good.){/i}"
    show 02_171
    ""
    show 02_172
    ""
    scene black with Dissolve(1)
    pause 2
    scene 02_174 with vpunch
    mc "{i}(Did she just?){/i}"
    a "{i}(I can't believe I came already...){/i}"
    scene 02_175 with Dissolve(1)
    ""
    scene 02_176 with Dissolve(1)
    mc "{i}(Let's see if I can make her cum again.){/i}"
    a "{i}(Oh? Changing position...){/i}"
    a "{i}(I like how he takes charge. He surely doesn't lack confidence.){/i}"
    scene 02_177 with Dissolve(1)
    ""
    show 02_178
    a "*Moaning*"
    a "Mmm. Yes... Keep going like that!"
    scene 02_179 with Dissolve(1)
    a "{i}(I'm close to coming again. This never happened before.){/i}"
    a "[mc]! Ah... [mc]!"
    scene 02_180 with Dissolve(1)
    mc "Can I?"
    a "Yes. Mmm..."
    scene black with Dissolve(1)
    pause 2
    scene 02_181 with Dissolve(1)
    if Alexis_Intro_Join == True:
        n "*Breathing heavily*"
        a "A bed is definitely more comfortable than an airplane toilet."
        mc "Haha... I won't argue with that."
    else:
        n "*Breathing heavily*"
        a "That was... Incredible."
        mc "Haha... Couldn't agree more."
    scene 02_182 with Dissolve(1)
    a "So... How about that coffee?"
    mc "'Coffee?'"
    a "Haha... No. I mean actual coffee this time!"
    mc "Tempting, but I'm already too wired to sleep. Caffeine might just make me explode."
    a "Hehe... Fair enough. But... Cuddles?"
    mc "Now that, I'm up for."
    scene black with Dissolve(1)
    pause 2
    scene 02_183 with Dissolve(1)
    a "You're quiet. What's on your mind?"
    mc "Hmm... Well. I have a question."
    a "About?"
    mc "Okay, hear me out. When you asked how I take my coffee and I said black... You showed up in black lingerie, right?"
    a "Uh-huh."
    scene 02_184 with Dissolve(1)
    mc "So if I'd said 'with milk', would you have worn white?"
    a "Haha! Not where I thought this was going, but... Good question."
    mc "And if I'd said 'with sugar'? Maybe... edible panties?"
    a "Heh! Wow. You're creative. I'll have to remember that one."
    mc "What if I said I didn't want coffee at all?"
    scene 02_185 with Dissolve(1)
    a "Sorry. That offer expired the moment you stepped through the door!"
    mc "Really?"
    a "I'm afraid so."
    mc "Nothing I can say to change your mind??"
    a "Nope! It's final!"
    mc "*Sigh*"
    scene 02_186 with Dissolve(1)
    mc "*Sings* If I could turn back time..."
    a "Haha! Perfect choice."
    a "*Sings* If I could find a way..."
    scene 02_187 with Dissolve(1)
    mc "Haha, are you kidding me? Communications? You should consider switching your major to singing."
    a "{i}(There he goes again... Just saying things that make me melt.){/i}"
    a "{i}(I know I shouldn't feel this way... But let me hold onto this moment a little longer.){/i}"
    scene black with Dissolve(1)
    pause 2
    scene 02_188 with Dissolve(1)
    mc "I should probably get going."
    a "{i}(No... not yet.){/i}"
    a "You could stay the night... If you wanted."
    mc "I'd love to. But if I don't show up, my mom might file a missing persons report."
    a "Haha... Right."
    scene 02_189 with Dissolve(1)
    a "Oh... I forgot to ask. How did the reunion with your mom go?"
    mc "It actually went really well. She's really happy I'm back."
    a "See? Told you so."
    mc "Yeah. You were right."
    a "Glad to hear it."
    a "{i}(But I wonder... How did the other reunion go?){/i}"
    scene 02_190 with Dissolve(1)
    a "So... I guess this is goodbye until fate decides to throw us together again?"
    mc "Heh... Next time probably won't be so random."
    a "Oh? Planning to stalk me now?"
    scene 02_191 with Dissolve(1)
    mc "Hey! As far as I remember, you brought me to your place."
    a "Is that what happened? I must have been feeling generous."
    mc "Haha."
    a "See you around, [mc]!"
    mc "Bye, Alexis."
    $ renpy.end_replay()
    jump Week1_Monday_Evening

label Week1_Monday_Evening:
    stop music fadeout 1.0
    scene black with Dissolve(2)
    pause 2
    play music ("Music/LoFi Indie 3.mp3", "Music/LoFi Indie 1.mp3", "Music/LoFi Indie 2.mp3") volume 0.2
    scene 02_192 with Dissolve(1)
    mc "{i}(Hmm... All the lights are off.){/i}"
    mc "{i}(She must be asleep already. Better not make any noise.){/i}"
    scene 02_193 with vpunch
    mc "{i}(Shit! That scared me.){/i}"
    mc "{i}(She doesn't look happy. At all.){/i}"
    scene 02_194 with Dissolve(1)
    m "Where have you been?"
    mc "I wa..."
    m "Do you even know what time it is?"
    mc "Yeah... I'm sorry."
    m "Why didn't you answer your phone?"
    scene 02_195 with Dissolve(1)
    mc "I didn't get a call. Let me see..."
    mc "Oh. It's turned off. Sorry... Didn't realise."
    m "So? Where were you?"
    scene 02_196 with Dissolve(1)
    mc "I was hanging out with Zach."
    m "Zach?"
    mc "Yeah. I knew him from before. We met at school."
    mc "We went drinking, and I completely lost track of time."
    m "Drinking? When you have school tomorrow?"
    scene 02_197 with Dissolve(1)
    mc "Sorry..."
    m "Listen. I don't mind you having fun with your friends. And the occasional drink is fine too. Just do it on the weekends."
    m "You're an adult and I don't know how Andres handled things, but if you're going to be out late, please let me know."
    m "Text me. Call me. Something..."
    mc "I know, you're right. I should've checked my phone. I will next time."
    scene 02_198 with Dissolve(1)
    m "Do you have any idea how worried I was?"
    m "I just got you back... And then this."
    mc "I get it. I really do. I promise it won't happen again."
    m "Okay... Thank you."
    scene 02_199 with Dissolve(1)
    m "Now go to bed. Hopefully, you won't wake up with a hangover..."
    mc "Hehe. It'll be fine. I didn't drink that much."
    mc "Good night, Mom."
    m "Good night, honey."
    jump Week1_Tuesday_School

label Week1_Tuesday_School:
    scene black with Dissolve(2)
    pause 2
    n "Tuesday, 08:15. School."
    stop music fadeout 1.0
    scene 02_200 with Dissolve(1)
    play music ("Music/LoFi Upbeat 2.mp3", "Music/LoFi Upbeat 3.mp3", "Music/LoFi Upbeat 1.mp3", "Music/LoFi Upbeat 4.mp3") volume 0.2
    mc "{i}(Well, look who it is...){/i}"
    mc "{i}(Thirsty already? Should've finished that beer yesterday, buddy.){/i}"
    scene 02_201 with Dissolve(1)
    mc "Morning, Mr Wingman."
    z "Heh? Hey, [mc]. Morning."
    scene 02_202 with Dissolve(1)
    z "Man. Sorry about yesterday."
    z "I completely forgot I had to help my sister."
    mc "No worries. It happens. All good."
    if Alexis_Friends == True:
        scene 02_203 with Dissolve(1)
        z "Did you stay a while?"
        mc "Nah. I just finished the beers and called it a night."
        mc "Didn't feel like hanging around by myself."
        z "Yeah, drinking solo sucks."
        la "Good morning."
    else:
        scene 02_204 with Dissolve(1)
        z "Did you stay a while?"
        mc "A bit, yeah. Had to finish the beers. Chatted more with Alexis too."
        z "She's cool, right? I knew you two would hit it off. Told you I'm an awesome wingman."
        mc "..."
        scene 02_205 with Dissolve(1)
        z "So... Did you two make any plans to meet up again?"
        mc "We didn't. I'll just take it easy and see where it goes from here."
        z "Can't say I'm not jealous. I've been trying to get close to her for months. You show up for a day and boom..."
        mc "Heh."
        la "Good morning."
    scene 02_206 with Dissolve(1)
    mc "Good morning!"
    z "Morning, ba... Layla."
    scene 02_207 with Dissolve(1)
    la "Hey. You know where the science class is?"
    mc "I think so, yeah."
    la "Yeah?"
    menu:
        "Check her out":
            scene black with Dissolve(1)
            transform moveup:
                xalign 0.5 yalign 1.0
                linear 5.0 yalign 0.0
            show 02_208 at moveup
            pause 3
            mc "{i}(Damn... Sporty look today. Definitely PE on her schedule.){/i}"
            mc "{i}(I wonder what club she's in?){/i}"
            if Layla_Week1_Monday_Payattention == True:
                pass
            else:
                mc "{i}(That smirk though... She's definitely up to something.){/i}"
        "Don't":
            pass
    scene 02_209 with Dissolve(1)
    la "Wanna walk with us?"
    mc "I think I can find it."
    scene 02_210 with Dissolve(1)
    la "Hehe. Just making sure..."
    mc "Thanks, though. See you later."
    scene 02_211 with Dissolve(1)
    if MC_Week1_Monday_Skip == True:
        la "Don't be late this time!"
        mc "If I am, are you coming to rescue me?"
        la "Haha. Maybe I will. Bye-bye!"
        z "Bye, Layla!"
    else:
        la "Bye-bye. Oh, and don't be late!"
        mc "I won't. See ya..."
        z "Bye-bye."
    scene 02_212 with Dissolve(1)
    z "She's looking good again today. And that ass! Damn..."
    mc "..."
    z "And did you hear? That was the first time she's actually said good morning to me."
    z "Usually, she just ignores me. I think she's slowly warming up!"
    mc "{i}(Bless him.){/i}"
    mc "{i}(I'd love to understand how his brain works... Actually, no. I'm good.){/i}"
    scene 02_213 with Dissolve(1)
    n "*Ding-dong*"
    x "Can [mc] Moreno please come to the reception office?"
    x "I repeat. [mc] Moreno to the reception office."
    mc "What the...?"
    z "Haha. What did you do now?"
    mc "I have no idea..."
    scene 02_214 with Dissolve(1)
    mc "I'd better go. See you at lunch?"
    z "Yes. Later, man. Good luck!"
    mc "*Sigh* Yeah..."
    scene black with Dissolve(1)
    pause 2
    scene 02_215 with Dissolve(1)
    re "Ah. Good morning, [mc]!"
    mc "Morning."
    re "I called you over because we haven't received your club registration form yet."
    scene 02_216 with Dissolve(1)
    mc "Yeah... About that. I haven't submitted it because I haven't joined a club yet."
    re "You do know this is a sports school, and joining a club is mandatory?"
    mc "Yes, I know. I just haven't decided which one to join yet."
    el "Sorry..."
    scene 02_217 with Dissolve(1)
    mc "..."
    re "Again, Elena?"
    el "I know, I know."
    scene 02_218 with Dissolve(1)
    mc "{i}(Oh, Elena... Now you're in trouble. Twice in two days.){/i}"
    el "I have..."
    re "Yes-yes. Just get to class already."
    el "Thank you."
    mc "{i}(Okay, what's going on here? Is she the principal's daughter or something?){/i}"
    mc "{i}(If it were me, I'd be getting a lecture right now. How is this fair?){/i}"
    scene 02_219 with Dissolve(1)
    re "So... I'll give you until the end of the week. I want your paperwork in by then."
    re "That gives you time to explore your options, talk to the teams, maybe try a few practices before deciding."
    mc "That's perfect. I'll definitely do that."
    re "Good. Now hurry up. Class has already started."
    mc "Thanks."
    jump Week1_Tuesday_Chemistry

label Week1_Tuesday_Chemistry:
    scene black with Dissolve(1)
    pause 2
    scene 02_220 with Dissolve(1)
    t "Would you look at that, someone else who decided to grace us with his attendance."
    mc "Good morning. I had..."
    t "Just take your seat. Class already started."
    mc "Yes..."
    scene 02_221 with Dissolve(1)
    t "Count yourself lucky, Elena."
    el "Lucky? In what way?"
    t "Looks like you won't be working alone on this assignment today."
    el "Oh joy!"
    mc "{i}(What's with her attitude? She was late too. Don't take it out on me...){/i}"
    scene 02_222 with Dissolve(1)
    el "Hey, partner."
    mc "Morning."
    scene 02_223 with Dissolve(1)
    el "Late again, huh? Two days in a row."
    mc "I wasn't late. I got called to the reception office for..."
    mc "Whatever. Look who's talking!"
    el "..."
    scene 02_224 with Dissolve(1)
    el "Listen... I can't afford to fail this class. So you're going to follow my lead, got it?"
    mc "{i}(Follow her lead?){/i}"
    menu:
        "Agree":
            mc "{i}(She clearly cares about the grade, and if that means she'll do most of the work, I'm not complaining.){/i}"
            mc "Alright. You're in charge."
            el "Perfect. Let's get started."
        "Complain[KoGa3AutoWTChange1]{size=-4}(Elena Week1 Tuesday Science Complain) {/size} {/color}":
            $ Elena_Week1_Tuesday_Science_Complain = True
            mc "Actually, I'm pretty good with chemistry stuff."
            el "Chemistry stuff? No! If I..."
            mc "Relax, I get it. But we better ace this assignment!"
            el "..."
            el "Fine. Let's just start."
    scene black with Dissolve(1)
    pause 2
    scene 02_225 with Dissolve(1)
    mc "How much of this? 5 ml?"
    el "Yes. Pour it slowly."
    mc "Tell me when to stop."
    el "Okay... That's enough."
    scene 02_226 with Dissolve(1)
    el "Now, mix it with 20 ml of water."
    mc "Got it."
    la "{i}(Hmm... Looks like they're actually having a good time. Lucky her...){/i}"
    if Layla_Week1_Monday_Payattention == True:
        pass
    else:
        la "{i}(Why did she get paired up with him? I wanted to work with him again.){/i}"
        la "{i}(Wow... Jealous much, Layla?){/i}"
    scene black with Dissolve(1)
    pause 2
    scene 02_227 with Dissolve(1)
    mc "I would've never guessed you were someone who's into chemistry."
    el "I don't particularly like it. It's just fun sometimes."
    el "Mixing things to see reactions. Like little experiments... You know?"
    mc "Yeah, I get that."
    el "What about you? You into this kind of stuff?"
    scene 02_228 with Dissolve(1)
    menu:
        "Yes":
            mc "It's alright, I guess. Can be interesting at times."
            mc "You make it fun, though."
        "No":
            mc "Not really... I don't see much use for this outside the classroom."
            mc "I mean, when am I ever gonna need to mix chemicals again?"
            el "Fair point..."
            mc "Still, you make it kind of enjoyable."
    scene 02_229 with Dissolve(1)
    el "Oh. Thanks."
    mc "Alright. Let's keep going. Next is..."
    el "Here, let me help with that."
    mc "Don't worry. I got thi..."
    scene 02_230 with Dissolve(1)
    mc "Oh. Fuck!"
    el "Nooo..."
    scene 02_231 with Dissolve(1)
    el "Haha."
    el "What did you do?"
    mc "Me? You should be glad I caught the glass!"
    el "Haha. Sorry..."
    scene 02_232 with Dissolve(1)
    la "What are you two doing?"
    el "Haha."
    mc "Why are you still laughing? It's spilt everywhere."
    el "That's what she said."
    mc "Really, Elena?"
    scene 02_233 with Dissolve(1)
    mc "You got a napkin or something?"
    el "Yeah. Hold on. I'll clean it up."
    scene 02_234 with Dissolve(1)
    la "Seriously you guys... How did that even happen?"
    mc "Here too, Elena. It's dripping on the floor."
    el "Got it."
    mc "Sorry, Layla. What were you saying?"
    la "Need some help with that?"
    scene 02_235 with Dissolve(1)
    x "Hey... Instead of helping them. Why don't you pay attention here?"
    la "What? I'm just trying to help my friends, alright?"
    x "We're supposed to be partners, but you keep turning around getting distracted..."
    x "We need to finish this!"
    scene 02_236 with Dissolve(1)
    la "How about you shut up and mind your own business?"
    x "You shut up!"
    la "Go work on the task."
    la "{i}(Ugh... He's so annoying.){/i}"
    scene 02_237 with Dissolve(1)
    t "What's going on over there?"
    la "Uh... Nothing, just a small debate."
    t "Okay. Continue, but keep it down a notch."
    la "Sorry. Will do."
    scene 02_238 with Dissolve(1)
    el "*Whisper* Thanks for the distraction, Layla."
    la "*Whisper* Anytime!"
    scene 02_239 with Dissolve(1)
    el "Okay... All cleaned up."
    mc "Thanks. Let's start over and finish this assignment."
    scene black with Dissolve(1)
    pause 2
    scene 02_240 with Dissolve(1)
    el "We did it! Go us!"
    mc "Can't believe we actually finished on time. Even have a few minutes to spare."
    mc "Nice work, partner."
    el "Hehe, thanks. You too."
    scene 02_241 with Dissolve(1)
    el "Honestly? Working with you wasn't even half bad."
    mc "Gee, thanks. I think?"
    el "Haha. No, really. It was fun."
    mc "I had fun too. Except for our little 'incident'."
    el "Haha... What incident?"
    mc "Exactly!"
    if Layla_Week1_Monday_Payattention == True:
        jump Week1_Tuesday_Cafeteria
    else:
        scene 02_242 with Dissolve(1)
        la "Someone looked like they were having fun."
        el "It was alright."
        scene 02_243 with Dissolve(1)
        la "Alright?"
        la "Come on, El. You were giggling the whole time."
        scene 02_244 with Dissolve(1)
        el "That was just from laughing at all the mistakes [mc] made."
        la "That many, huh?"
        el "More than a few."
        scene 02_245 with Dissolve(1)
        la "Poor guy. Bad with directions..."
        el "Bad at chemistry..."
        la "Haha. What is he good at?"
        el "For your sake. hopefully at least at..."
        el "'The one thing'..."
        scene 02_246 with Dissolve(1)
        la "Elena Sofía Ortiz!"
        el "Haha."
        la "Hahaha."
        jump Week1_Tuesday_Cafeteria

label Week1_Tuesday_Cafeteria:
    scene black with Dissolve(1)
    pause 2
    scene 02_247 with Dissolve(1)
    el "But you're right. It was actually really sweet."
    la "See. Told you!"
    scene 02_248 with Dissolve(1)
    el "What the..."
    la "Uh?"
    el "Where do they think they're sitting?"
    el "Oh, hell no."
    scene 02_249 with Dissolve(1)
    el "Hey there... Zach!"
    z "'Sup?"
    el "You do realise this is our table, right?"
    scene 02_250 with Dissolve(1)
    la "Hey."
    mc "Hi."
    z "Hmm? Didn't see any names on it."
    el "Seriously, Zach? You know we always sit here."
    z "Last I checked, it's a free country."
    scene 02_251 with Dissolve(1)
    z "But hey, I won't be that guy."
    z "Look. I'll scoot over. Plenty of space. Feel free to join."
    el "And listen to your nonsense while I eat? I'll pass."
    z "First of all, you don't eat."
    z "Second, I was talking to Layla. I don't care where you sit."
    scene 02_252 with Dissolve(1)
    z "The table behind me is free. Grab that one."
    el "Next to the trash can..."
    z "Isn't that the perfect place for you?"
    menu:
        "Intervene[KoGa3AutoWTChange1]{size=-4}(Elena Week1 Tuesday Intervene, Layla Points+2, Elena Points+2) {/size} {/color}":
            $ Elena_Week1_Tuesday_Intervene = True
            $ Layla_Points += 2
            # Layla (8)
            $ Elena_Points += 2
            # Elena (2)
            scene 02_253 with Dissolve(1)
            mc "Hey, hey-hey. Chill! Let's not go full reality show here."
            z "Relax. I'm just messing with them."
            mc "There's messing, and then there's just being a jerk."
            scene 02_254 with Dissolve(1)
            mc "We can move. No big deal."
            la "Thanks, [mc], but it's okay."
            la "Come on, El. Let's just go sit over there."
            el "*Nods*"
        "Stay out of it":
            el "..."
            scene 02_255 with Dissolve(1)
            la "Let's just sit over there, El. No point in arguing with him."
            el "Right. He's not worth our time."
            scene 02_256 with Dissolve(1)
            el "I hate that he's at our table... He's probably grinning like an idiot right now."
            el "This isn't over."
            la "Haha. What are you planning?"
            el "Not sure yet. But karma's a bitch."
    scene black with Dissolve(1)
    pause 2
    scene 02_257 with Dissolve(1)
    z "So, what was that about this morning? The whole reception office thing?"
    mc "They still don't have my club registration. Told me I need to pick a team by the end of the week."
    z "Dude... Just join the football team. We can tear it up like old times."
    mc "I don't know. It's been a while since I've played."
    z "Doesn't matter. Muscle memory, bro."
    scene 02_258 with Dissolve(1)
    z "Tell you what. Come to practice this afternoon. Just try out. See what you think."
    z "Team's solid. You'll have fun."
    mc "Yeah, alright. I'm down."
    z "Nice. Got any gear? If not, I've got a spare set of shorts and a shirt in my locker."
    scene 02_259 with Dissolve(1)
    mc "Nah, I'm good. I have my PE bag with me."
    z "Good. Just a heads-up... Coach is kind of a hardass."
    mc "Okay... Looking forward to it."
    x "Hey, Zach."
    scene 02_260 with Dissolve(1)
    z "Yo, what's up?"
    x "We're all going out tonight. You in?"
    z "Hell yeah I'm in. If there's girls, guess who's showing up? Zach Attack!"
    mc "..."
    if Layla_Points == 8:
        mc "{i}(Why is she giving me that look?){/i}"
        show 02_261
        mc "..."
        la "Hahaha."
        scene 02_262 with Dissolve(1)
        mc "{i}(Heh... What a tease.){/i}"
    else:
        pass
    jump Week1_Tuesday_Tryouts

label Week1_Tuesday_Tryouts:
    scene black with Dissolve(2)
    pause 2
    scene 02_263 with Dissolve(1)
    z "[mc]!"
    z "Go long..."
    scene 02_264 with Dissolve(1)
    x "What the...?"
    x "How is this guy so fast?"
    scene 02_265 with Dissolve(1)
    mc "..."
    scene 02_266 with Dissolve(1)
    x "Fuck...!"
    scene 02_267 with Dissolve(1)
    mc "{i}(Damn... I lost all momentum turning around.){/i}"
    mc "{i}(I just can't shoot with my left foot...){/i}"
    scene 02_268 with Dissolve(1)
    mc "*Slips*"
    mc "Shit..."
    scene 02_269 with Dissolve(1)
    x "You alright?"
    mc "Yeah, just slipped. I'm good."
    x "It's the shoes. I would never play without studs on a pitch."
    mc "Didn't plan on playing today. This is all I had."
    scene 02_270 with Dissolve(1)
    x "Here, let me help you up."
    mc "Thanks."
    scene black with Dissolve(1)
    pause 2
    scene 02_271 with Dissolve(1)
    mc "*Sigh*"
    mc "{i}(Man... That was rough.){/i}"
    scene 02_272 with Dissolve(1)
    z "Hahaha... What happened out there, man?"
    mc "I'm so out of shape. It's not even funny. Barely did any running the last couple of weeks."
    z "Yeah. You were out of breath very quickly there."
    scene 02_273 with Dissolve(1)
    z "But I'll give you this. You're crazy fast, man. Some Flash-type shit going on there."
    mc "Haha, appreciate it."
    z "With some stamina training and the skills I know you have from a few years back, you'll be an excellent winger."
    z "If you hadn't slipped, that play would've been a highlight-reel moment."
    scene 02_274 with Dissolve(1)
    z "So... You're joining the team, then?"
    mc "I don't know. Not sure about it yet..."
    mc "Just didn't feel it. At least, not how it used to be."
    z "It'll come back. Trust me."
    mc "Hmm..."
    scene 02_275 with Dissolve(1)
    z "Oh. By the way, the team's going out drinking tonight."
    if Alexis_Friends == True:
        z "Same bar I took you to last time. Maybe a few beers will change your mind. This time, there'll definitely be girls."
        mc "Haha, tempting. But I've got to work tonight."
    else:
        z "Same bar as last time. Who knows? You might bump into Alexis again!"
        mc "Heh. Would be nice... But I've got work tonight."
    z "Damn, that sucks. Next time I'm not taking no for an answer!"
    mc "Deal. You still owe me a beer anyway."
    z "Hahaha..."
    jump Week1_Tuesday_Melissa_Backyard

label Week1_Tuesday_Melissa_Backyard:
    if _in_replay:
        $ Melissa_Points = 6
        $ Melissa_Intro_Sunbath = True
    scene black with Dissolve(2)
    pause 2
    scene 02_276 with Dissolve(1)
    mc "{i}(Alright... Let's see what needs to be done. Definitely mowing the lawn.){/i}"
    mc "{i}(Oh... she's home. And swimming too.){/i}"
    scene 02_277 with Dissolve(1)
    mc "Hey, Melissa."
    me "Oh, hey [mc]! How's it going?"
    mc "All good. Thought I'd tackle the yard today."
    scene 02_278 with Dissolve(1)
    me "Perfect! If you're looking for the lawnmower, it's next to the... Wait, I'll show you."
    mc "It's alright. Stay in the pool. I'll find it."
    scene 02_279 with Dissolve(1)
    mc "{i}(Hmm... Is this electric or gas-powered?){/i}"
    mc "{i}(Looks electric. Now where's the extension cord?){/i}"
    mc "Mel? You know where the extension cord is?"
    me "No need! It's battery-operated. Should already be charged."
    mc "Sweet. Thanks!"
    scene black with Dissolve(1)
    pause 2
    scene 02_280 with Dissolve(1)
    mc "{i}(Pfew... Should've changed first. It's scorching today. Not used to Madison Springs heat yet.){/i}"
    mc "{i}(But the best thing: no more winters!){/i}"
    me "Hey, [mc]!"
    mc "Yeah?"
    me "Aren't you melting in all those clothes? I'm sweating just watching you."
    scene 02_281 with Dissolve(1)
    mc "Nope. That's just my natural glow. Comes with being handsome!"
    me "Ha! Someone's got heatstroke already."
    mc "Haha."
    me "Seriously though. Take off your shirt. You're gonna pass out."
    scene 02_282 with Dissolve(1)
    me "{i}(Well, damn. He wasn't lying. That boy keeps in shape. You made a handsome boy, Emily.){/i}"
    me "Much better, right?"
    mc "Way better."
    scene 02_283 with Dissolve(1)
    me "Want me to grab some sunscreen?"
    mc "I'm good, thanks. Almost done here anyway."
    me "Alright. If you change your mind or need to cool off, jump in the pool."
    mc "Haha, thanks. Might take you up on that."
    scene black with Dissolve(1)
    pause 2
    scene 02_284 with Dissolve(1)
    mc "Where should I dump the grass bag?"
    me "Just leave it next to the others. Waste pickup isn't until next week."
    scene 02_285 with Dissolve(1)
    mc "Well, that's it for today!"
    me "Thanks so much, [mc]. Really appreciate it."
    mc "Anytime."
    scene 02_286 with Dissolve(1)
    me "Wanna join me in the pool for a bit? Water feels amazing right now."
    mc "Tempting... But I'm all sweaty and sticky."
    mc "Think I'll head home and shower."
    scene 02_287 with Dissolve(1)
    me "Nothing the pool water won't wash away."
    mc "{i}(Has she always been this flirty?){/i}"
    if Melissa_Points == 6:
        mc "{i}(Not that I mind... Especially when she's looking like that.){/i}"
    else:
        pass
    mc "Heh, true but..."
    me "I get it. Another time, then?"
    scene 02_288 with Dissolve(1)
    mc "..."
    me "Before you go. Can I see your other tattoo?"
    mc "Sure."
    scene 02_289 with Dissolve(1)
    mc "{i}(Wai... Wait...){/i}"
    mc "{i}(Oh shit... Her bikini is see-through?){/i}"
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 02_290 at moveup
    pause 3
    if Melissa_Intro_Sunbath == True:
        mc "{i}(I saw her half-naked last time. But this... Damn.){/i}"
    else:
        mc "{i}(I saw her in bikinis many times when I was younger, but this...){/i}"
        mc "{i}(Snap out of it, man. She's basically my aunt.){/i}"
    scene 02_291 with Dissolve(1)
    me "Oh wow. It's quite big."
    mc "{i}(Heh... *shakes head* I'm such an idiot!){/i}"
    me "Same artist who did your arm?"
    mc "You can tell just by looking?"
    me "Yep. Distinct line work. He's super talented."
    scene 02_292 with Dissolve(1)
    mc "She!"
    me "Oh? Now I like it even more. The industry can use more female artists."
    me "But that one had to hurt... Ribs are brutal. I've been there."
    mc "{i}(She's leaning in...){/i}"
    menu:
        "Look closer[KoGa3AutoWTChange1]{size=-4}(Melissa Points+2) {/size} {/color}":
            $ Melissa_Points += 2
            # Melissa (8)
            scene 02_293 with Dissolve(1)
            mc "{i}(I'm hopeless... Zero willpower.){/i}"
            mc "{i}(So happy I'm still wearing those jeans though.){/i}"
            mc "{i}(Does she even know her bikini's see-through?){/i}"
        "Don't look":
            pass
    scene 02_294 with Dissolve(1)
    mc "It definitely did. Getting my arm done felt like a massage compared to this."
    mc "{i}(What is she doing? Why is she so close?){/i}"
    mc "But this one... Yeah, no joke."
    me "Uh-huh."
    mc "..."
    mc "Uh? Melissa? Why are you..."
    scene 02_295 with Dissolve(1)
    mc "HEY! Nooo!"
    me "Oh yes. Haha!"
    mc "MELISSA!"
    scene 02_296 with Dissolve(1)
    me "Isn't that refreshing?"
    mc "Seriously, Melissa...?"
    me "Haha."
    scene 02_297 with Dissolve(1)
    mc "You shouldn't be the one laughing. My shoes were dirty, and now the pool will be, too."
    me "Oh you little drama queen. Don't worry about that."
    me "Besides. I have a nice neighbour who does my yard work. Haha."
    mc "Oh, you're hilarious... You know I'll get you back for this."
    me "Well. Bring it on!"
    me "{i}(He's still the same...){/i}"
    scene 02_298 with Dissolve(1)
    me "Watch out! I'm coming in."
    scene 02_299 with Dissolve(1)
    mc "{i}(Wow... that body though.){/i}"
    mc "{i}(Now I can't help wondering what Erynn looks like these days...){/i}"
    scene 02_300 with Dissolve(1)
    me "Sorry for the sneak attack."
    mc "You don't look apologetic at all."
    me "Haha."
    scene black with Dissolve(1)
    pause 2
    scene 02_301 with Dissolve(1)
    me "Remember when you were little? You'd beg me to come swim with you almost every day."
    mc "Well. Honestly... Erynn liked to swim back then. And I wanted you to teach me. So I could go swimming with her."
    me "Aww, that's adorable. I had no idea."
    me "I'll have to tell her that sometime."
    $ renpy.end_replay()
    jump Week1_Tuesday_Melissa_Emily

label Week1_Tuesday_Melissa_Emily:
    if _in_replay:
        $ Emily_Points = 0
    scene 02_302 with Dissolve(1)
    me "Have you met up with her yet? I haven't heard a word from her."
    mc "I..."
    m "So this is what you call helping out in the yard, huh?"
    scene 02_303 with Dissolve(1)
    mc "Uh? Oh... Hey, Mom."
    me "Hey, Emily."
    me "He's already done, so I invited him to cool off in the pool."
    scene 02_304 with Dissolve(1)
    mc "Invited? You pushed me in!"
    me "Ah. Minor detail."
    m "Heh. That explains why you're wearing your jeans and shoes in the pool."
    m "At least take them off now."
    mc "{i}(I can't really. The jeans at least...){/i}"
    scene 02_305 with Dissolve(1)
    me "It's such a perfect day. Why don't you join us?"
    m "Not dressed like this, I'm not."
    m "And don't you dare try pulling me in."
    me "Me? Never..."
    scene 02_306 with Dissolve(1)
    mc "Uh-huh. Don't trust her, Mom. She's sneaky."
    m "I know what she's like."
    me "Haha."
    m "Anyway, I should really start on dinner."
    scene 02_307 with Dissolve(1)
    me "There's plenty of time for that. You can wait a little, right?"
    mc "Sure."
    me "See? So go throw on your bikini and get that sweet little butt in here already!"
    mc "{i}(Sweet little... Wait, what? Did I just hear that right?){/i}"
    m "Alright, alright... I'll be right back."
    scene black with Dissolve(1)
    pause 2
    scene 02_308 with Dissolve(1)
    me "What's with the towel?"
    m "I'm not walking down the street in just a bikini!"
    me "Oh please, you've done worse."
    m "That was fifteen years ago!"
    mc "{i}(Eh... Do I even want to know?){/i}"
    scene 02_309 with Dissolve(1)
    me "Now you know where you get your good looks from, [mc]."
    m "Mel! Stop it..."
    me "It's true though! Who else would he get it from?"
    m "..."
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 02_310 at moveup
    pause 3
    mc "..."
    scene 02_311 with Dissolve(1)
    me "See? You've still got it, girl."
    me "Maybe I should call Erynn and see if she can hook you up with a modelling gig."
    m "Melissa... Come on."
    me "Right, [mc]? Back me up here."
    scene 02_312 with Dissolve(1)
    mc "Uh..."
    mc "{i}(Honestly. She's stunning.){/i}"
    mc "{i}(Dad, you really messed things up... Again.){/i}"
    scene 02_313 with Dissolve(1)
    me "Come on in!"
    m "How's the water?"
    me "Refreshing. Stop stalling or I'll..."
    m "Don't even think about it, Melissa. I mean it!"
    me "Then jump already!"
    scene 02_314 with Dissolve(1)
    m "I'm not jumping. I'm too old for that."
    me "Nonsense. Fun doesn't have an age limit. If you asked a stranger, they'd think you were twenty-eight."
    m "Pfft... twenty-eight? Yeah, right."
    me "Get in!"
    mc "{i}(Haha. They sound like teenagers. Were they always like this? I don't remember.){/i}"
    menu:
        "Let her get in by herself":
            scene 02_315 with Dissolve(1)
            me "Using the ladder? You should've jumped, Em!"
            m "I prefer to be safe!"
            me "Or boring!"
            m "..."
            scene 02_326 with Dissolve(1)
            mc "Well... This was fun, ladies..."
            m "Wait! You're leaving already? I just got in."
            mc "I should get out of these wet clothes. Still got some homework to do."
            m "Alright, honey. I'll be home in a bit to cook dinner."
            mc "Don't worry, take your time. Enjoy the pool."
            m "Thanks. Oh, and hang your jeans up to dry, and stuff newspaper in your shoes, or they won't be dry by tomorrow."
        "Grab her[KoGa3AutoWTChange1]{size=-4}(Emily Points+2) {/size} {/color}":
            $ Emily_Points += 2
            # Emily (2)
            scene 02_316 with vpunch
            m "Aaah...!"
            me "Yes, [mc]!"
            m "Nooo!"
            mc "You're taking forever!"
            scene 02_317 with Dissolve(1)
            m "Don't you dare!"
            me "Do it!"
            m "[mc], put me down this instant!"
            mc "..."
            m "Stop smiling and put me down!"
            scene 02_318 with Dissolve(1)
            m "[mc]!!!"
            me "Haha."
            scene 02_319 with Dissolve(1)
            mc "Haha."
            m "You're in so much trouble, young man!"
            mc "Worth it!"
            scene 02_320 with Dissolve(1)
            mc "{i}(Oh shit...){/i}"
            me "Uh... Em?"
            m "Hmm?"
            menu:
                "Look closer[KoGa3AutoWTChange1]{size=-4}(Emily Points-2) {/size} {/color}":
                    $ Emily_Points -= 2
                    scene 02_321 with Dissolve(1)
                    mc "..."
                    me "Emily... You might want to fix something."
                "Turn around":
                    scene 02_322 with Dissolve(1)
                    me "Emily... You might want to fix something."
            scene 02_323 with Dissolve(1)
            m "..."
            scene 02_324 with Dissolve(1)
            me "Or take it off completely. That's how you usually swim anyway."
            mc "{i}(Okay... Too much information, Mel.){/i}"
            m "Heh. Not with [mc] here."
            mc "{i}(Not with me here... She realises I just saw her... Why isn't she embarrassed at all?){/i}"
            scene 02_325 with Dissolve(1)
            m "Alright... Fixed."
            me "I didn't mind the little show. Reminded me of our old days in college."
            m "Yeah. That's why they're called the old days."
            mc "{i}(Okay, time to bail before I learn things I really don't want to know.){/i}"
            scene 02_326 with Dissolve(1)
            mc "Well... This was fun, ladies..."
            m "Wait! You're leaving already? I just got in."
            mc "I should get out of these wet clothes. Still got some homework to do."
            m "Alright, honey. I'll be home in a bit to cook dinner."
            mc "Don't worry, take your time. Enjoy the pool."
            m "Thanks. Oh, and hang your jeans up to dry, and stuff newspaper in your shoes, or they won't be dry by tomorrow."
    scene 02_327 with Dissolve(1)
    mc "Will do. Have fun, you two."
    me "Thanks for the hard work, [mc]."
    mc "Anytime. See you next time, Melissa. Later, Mom."
    me "Bye."
    m "Bye, honey."
    scene 02_328 with Dissolve(1)
    me "He's a good kid. At least Andres did one thing right."
    m "Yeah."
    m "By the way. Your bikini is completely see-through!"
    me "Is it?"
    $ renpy.end_replay()
    jump Episode_3_Start

# Max Points:

# Alexis (10)
# Melissa (8)
# Layla (8)
# Elena (2)
# Emily (2)

# MC_GoodStudent (6)

# MC_Sex (2)
# MC_BJ (1)
# Alexis_Sex (2)

#WTAdded
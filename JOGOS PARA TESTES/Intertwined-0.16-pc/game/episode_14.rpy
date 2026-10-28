label Episode_14_Start:

    #KoGa3 START#
    $ KoGa3GameProgress = "Ep14"
    #KoGa3 END#

    $ achievement.grant("ACHIEVEMENT_EPISODE_13")
    $ achievement.sync()
    $ Emily_Week6_Monday_FirstBikeRide = False
    $ ElenaLayla_Week6_Monday_BikeRevScare = False
    $ Week6_Monday_Relay_PickLayla = False
    $ Week6_Monday_Relay_PickTori = False
    $ Layla_Week6_Monday_Spanish_OfferHelp = False
    $ LayLena = False
    $ Valeria_Week6_Monday_EmoDate = False
    $ Week6_Monday_BBQ_Invitation = False
    $ AlexisValeria = False
    $ Zach_Week6_Monday_Punch = False
    $ Adriana_Week6_Monday_DontTell = False
    $ Zach_Week6_Monday_BikeSuspect = False
    $ Brooke_Week6_Monday_ManagerPosition = False
    $ Iris_LikeMC = False
    $ Iris_Week6_Monday_Garage_Sex = False
    $ Iris_Week6_Monday_CheatKiss = False
    $ Andres_Week6_Monday_Hug = False
    $ Erynn_Week6_Monday_ReadLetter = False
    $ Erynn_Week6_Monday_WriteLetter = False
    $ MC_Week6_Monday_WinGame = False
    $ NikkiCara_Week6_Monday_MiraLie = False
    $ NikkiCara_Week6_Monday_MiraMention = False
    $ Riverside_MiraTruth = False
    $ Melissa_Week6_Monday_Compliment = False
    $ Melissa_LikeMC = False
    $ Melissa_Week6_Monday_Sex = False

    jump Week6_Monday_Morning

label Week6_Monday_Morning:
    scene black with Dissolve(2)
    pause 2
    stop music fadeout 1.0
    play music ("Music/LoFi Indie 3.mp3", "Music/LoFi Indie 1.mp3", "Music/LoFi Indie 2.mp3") volume 0.2
    n "Monday, 07:36."
    scene 14_001 with Dissolve(1)
    mc "Morning, Mom."
    m "Hey! Good morning, honey."
    m "You remembered you have school today? I was just about to come upstairs and wake you."
    mc "Haha, yeah... No more spring break..."
    scene 14_002 with Dissolve(1)
    m "Feeling sad it's over?"
    mc "Hmm... Yes and no. Strangely, I'm kind of looking forward to going back."
    mc "{i}(Though I'm not exactly excited to see some people again...){/i}"
    m "That's... unusual. But it's a good sign you're settling in and actually liking the school!"
    mc "Yeah."
    scene 14_003 with Dissolve(1)
    m "Here you go!"
    mc "Oh, thanks."
    scene 14_004 with Dissolve(1)
    mc "Do you have a busy day ahead? Or will things calm down now that spring break and the tourist rush is over?"
    m "About the same. We'll have fewer walk-ins at the bar, but all the tables are booked solid for the next few months."
    mc "That's a good problem to have."
    m "It definitely is."
    scene 14_005 with Dissolve(1)
    m "So, yesterday you mentioned you wanted to talk about something?"
    mc "Yeah, I did."
    if Emily_Week4_Sunday_DateJohn == True:
        mc "You also said you had something you wanted to tell me, right?"
        m "Mm-hmm."
        mc "Mine might take a while though... Not sure how much time you've got right now."
    else:
        mc "It might take a while, and I'm not sure how much time you have right now."
    scene 14_006 with Dissolve(1)
    m "Not much. I actually have to leave right now."
    m "How about we talk after school then. That way we don't have to rush."
    mc "Good idea. You might need to sit down for what I'm about to ask."
    m "Now you're worrying me! Maybe you should tell me now..."
    mc "No-no. It's... more of a confirmation, I guess."
    scene 14_007 with Dissolve(1)
    m "Hmm..."
    mc "Don't look so suspicious! I promise it's nothing bad."
    m "..."
    scene 14_008 with Dissolve(1)
    m "*Sigh* Okay..."
    m "I'm leaving, then. See you later."
    mc "Later, Mom!"
    if Emily_Week5_Sunday_Hug == True:
        scene 14_009 with Dissolve(1)
        m "Hey! Hug me like you did yesterday!"
        mc "I can't! I'm holding a hot cup of coffee!"
        m "Then put it down for a second!"
        mc "..."
        scene 14_010 with Dissolve(1)
        m "So much better! I need one of these every day, now!"
        mc "Not gonna happen!"
        m "I'll make sure it does!"
        mc "*Shakes head*"
        scene 14_011 with Dissolve(1)
        m "Bye, honey."
        mc "Bye, Mom."
    else:
        m "Bye, honey."
    scene 14_012 with Dissolve(1)
    mc "..."
    mc "{i}(Eclipse won again... Now they have a better W/L record than us. Fuck...){/i}"
    mc "{i}(In two weeks, we face them again. We'd better win that game!){/i}"
    if Valeria_Week5_Friday_Date == False:
        pass
    else:
        scene 14_013 with Dissolve(1)
        mc "..."
        mc "{i}(Again... Straight to voicemail. Come on, Valeria!){/i}"
        mc "{i}(Did she turn off her phone? She's definitely awake by now...){/i}"
        mc "{i}(Maybe she blocked me? Does it go to voicemail if someone blocks you? I honestly don't know.){/i}"
        mc "{i}(But why would she block me, anyway? There's got to be a reason she can't pick up. I guess I'll see her at school later.){/i}"
    scene 14_014 with Dissolve(1)
    play sound "Sounds/CarStalling.mp3" volume 0.5
    n "*Car stalling*"
    mc "{i}(Is that Mom's car?){/i}"
    play sound "Sounds/CarStalling2.mp3" volume 0.5
    mc "{i}(Let's check it out.){/i}"
    scene 14_015 with Dissolve(1)
    play sound "Sounds/CarStalling.mp3" volume 0.5
    mc "{i}(Doesn't want to start, huh?){/i}"
    scene 14_016 with Dissolve(1)
    play sound "Sounds/CarStalling2.mp3" volume 0.5
    m "..."
    m "FUCK!"
    mc "{i}(Why do I always find it funny when Mom swears?){/i}"
    mc "{i}(At least I know where I got it from.){/i}"
    stop sound
    scene 14_017 with Dissolve(1)
    mc "Not starting?"
    m "No. I don't know what's wrong. I drove it on Saturday and everything was fine."
    mc "Hmm... Can you pop the hood?"
    m "You know how to fix cars?"
    mc "No. Just checking if maybe a cable's loose or something obvious."
    scene 14_018 with Dissolve(1)
    mc "{i}(Why am I even looking? I have no idea what I'm doing!){/i}"
    mc "{i}(Do I think I'm John or something?){/i}"
    m "Anything?"
    mc "Nothing I can see. I'll call John later and ask if he can take a look."
    m "Thanks."
    scene 14_019 with Dissolve(1)
    m "*Sigh* Of all days, it had to be today! Now I'm going to be late."
    m "Guess I'll have to call an Uber or head to the bus stop."
    mc "Can't Melissa drive you?"
    m "She's not home. She had an early appointment this morning."
    if MC_Bike == True:
        $ Emily_Week6_Monday_FirstBikeRide = True
        scene 14_021 with Dissolve(1)
        mc "Then there's one other option!"
        m "That is?"
        mc "I'll take you!"
        m "With what car?"
        mc "Not a car..."
        scene 14_022 with Dissolve(1)
        m "On your bike? No way!"
        mc "Why not?"
        m "Because it scares me, for starters..."
        mc "But who knows when the Uber will get here or when the next bus will come? If you want to be on time..."
        scene 14_023 with Dissolve(1)
        m "..."
        mc "I'll ride really slow and safe!"
        mc "Come on, Mom! It'll be fun. Something you'll never forget."
        mc "{i}(She's thinking about it. Say yes. Say yes!){/i}"
        scene 14_024 with Dissolve(1)
        m "You have to go to school!"
        mc "I still have almost an hour. Plenty of time to get there."
        mc "Please? Come on!"
        m "..."
        scene 14_025 with Dissolve(1)
        m "*Sigh* Fine! Just don't make me regret this!"
        mc "You won't!"
        scene 14_026 with vpunch
        m "Aaah..."
        mc "Haha."
        mc "I'm so excited about this!"
        m "Alright, alright. Let's go then."
        scene 14_027 with Dissolve(1)
        mc "One more thing, maybe."
        mc "You might want to change your outfit. At least some pants..."
        mc "Unless you want to flash your butt to everyone when your skirt flips up."
        m "[mc]!"
        mc "What? I'm just looking out for you!"
        scene 14_028 with Dissolve(1)
        m "Let me change real quick, then."
        mc "Hurry though. We don't have much time to spare."
        m "I know, I know. Be right back."
        mc "I'll get the bike ready and grab the helmets."
        scene black with Dissolve(1)
        pause 2
        scene 14_029 with Dissolve(1)
        mc "{i}(Still can't believe she agreed to let me take her to the restaurant on my bike.){/i}"
        mc "{i}(I'm happy she trusts me with this.){/i}"
        mc "{i}(But remember, [mc]! Drive slow! No showing off...){/i}"
        m "Will this do?"
        scene black with Dissolve(1)
        transform moveup:
            xalign 0.5 yalign 1.0
            linear 5.0 yalign 0.0
        show 14_030 at moveup
        pause 3
        mc "Oh damn... Yeah... That will do! You look great!"
        m "Thank you."
        mc "Where did you get that outfit from?"
        m "I've had it since my college days. I was pleasantly surprised it still fits."
        scene 14_031 with Dissolve(1)
        m "No flashing my butt now!"
        mc "Heh..."
        scene 14_032 with Dissolve(1)
        mc "At least not like that..."
        m "What?"
        mc "Nothing... Let's get going."
        scene 14_033 with Dissolve(1)
        mc "Here's your helmet."
        m "Thank you."
        mc "Need help putting it on, or...?"
        m "I think I've got it."
        scene 14_034 with Dissolve(1)
        m "Do I sit like this?"
        mc "No, you'll fall off that way."
        mc "Lean against me and put your arms around me."
        scene 14_035 with Dissolve(1)
        mc "Tighter! Like really squeeze me."
        if Emily_Week5_Sunday_Hug == True:
            mc "Remember our hug in the kitchen?"
            mc "Like that!"
            m "Okay."
        else:
            m "Okay."
        scene 14_036 with Dissolve(1)
        mc "Ready to go?"
        m "I don't know... I'm so scared... Even more than before."
        mc "It's only scary for the first few seconds when I accelerate. After that, it's smooth sailing."
        m "*Sigh...* Go really slow, okay?"
        scene 14_037 with Dissolve(1)
        mc "Your first bike ride!"
        m "And my last!"
        mc "Don't say that yet. You might enjoy it."
        mc "And don't forget to close your visor if you don't want to eat bugs!"
        m "Ew..."
        mc "Haha."
        scene 14_038 with Dissolve(1)
        mc "Here we go!"
        scene 14_039 with Dissolve(1)
        m "Aaah..."
        scene black with Dissolve(1)
        pause 2
        scene 14_040 with Dissolve(1)
        ""
        scene 14_041 with Dissolve(1)
        n "*Beep-beep. Beep-beep*"
        mc "..."
        scene 14_042 with Dissolve(1)
        x "Looking good!"
        mc "{i}(Fucking idiot!){/i}"
        mc "{i}(I knew that was gonna happen.){/i}"
        scene 14_043 with Dissolve(1)
        ""
        scene 14_044 with Dissolve(1)
        m "Looks like someone else likes your bike."
        mc "That's not what he was honking at, Mom..."
        m "Hmm?"
        scene 14_045 with Dissolve(1)
        mc "Anyway, how do you like it so far?"
        m "It's less scary than I thought it'd be."
        m "Like you said, it's just the first few seconds when you accelerate, but after that... Yeah, it's not bad."
        mc "See!"
        scene black with Dissolve(1)
        pause 2
        scene 14_046 with Dissolve(1)
        m "Haah... We made it!"
        mc "Yeah, you survived..."
        m "Haha, that's not what I meant."
        scene 14_047 with Dissolve(1)
        m "Thanks so much for bringing me, honey!"
        m "It was actually fun."
        mc "Haha, you're welcome."
        scene 14_048 with Dissolve(1)
        m "I'm taking the helmet with me."
        mc "Want me to pick you up later?"
        m "No-no. That way you don't have to carry it around at school. I'll figure out a way home."
        mc "Well, if anything changes and you need me to come get you, just call me."
        m "Thanks, will do."
        scene 14_049 with Dissolve(1)
        m "Are you gonna be on time now?"
        mc "Hmm... It'll be close. I might just speed a little."
        m "No! No speeding!"
        m "If you're gonna be late, tell the school to call me. I'll explain."
        mc "Haha, okay."
        scene 14_050 with Dissolve(1)
        mc "And I'll call John later to see if he can check the car."
        m "Thanks."
        m "You'd better get going. Drive safe!"
        mc "I will."
        scene 14_051 with Dissolve(1)
        m "No speeding!"
        mc "Haha... I won't, I won't."
        m "Bye!"
        mc "Bye, Mom!"
        jump Week6_Monday_School_Entrance
    else:
        scene 14_020 with Dissolve(1)
        m "Anyway, thanks for having a look at it."
        mc "Yeah, no problem."
        mc "Like I said, I'll call John after school and see if he has some time today to check it out."
        m "Thank you."
        jump Week6_Monday_School_Entrance

label Week6_Monday_School_Entrance:
    scene black with Dissolve(1)
    pause 2
    stop music fadeout 1.0
    play music ("Music/LoFi Upbeat 3.mp3", "Music/LoFi Upbeat 2.mp3", "Music/LoFi Upbeat 1.mp3", "Music/LoFi Upbeat 4.mp3") volume 0.2
    if Layla_End == True:
        if MC_Bike == True:
            scene 14_052 with Dissolve(1)
            mc "{i}(Still made it on time.){/i}"
            scene 14_053 with Dissolve(1)
            mc "{i}(Layla and Elena...){/i}"
            mc "{i}(Haven't seen them in a while. I saw Layla briefly on Friday, but Elena... Probably before spring break.){/i}"
            scene 14_054 with Dissolve(1)
            mc "Hey. Good morning."
            el "..."
            la "Morning..."
            scene 14_055 with Dissolve(1)
            mc "*Sigh...*"
            mc "{i}(I really need to figure out how to at least get back to friendly terms with them.){/i}"
            mc "{i}(But how...?){/i}"
            jump Week6_Monday_Track
        else:
            scene 14_056 with Dissolve(1)
            ""
            scene 14_057 with Dissolve(1)
            mc "{i}(Layla and Elena...){/i}"
            mc "{i}(Haven't seen them in a while. I saw Layla briefly on Friday, but Elena... Probably before spring break.){/i}"
            scene 14_058 with Dissolve(1)
            mc "Hey. Good morning."
            el "..."
            la "Morning..."
            scene 14_059 with Dissolve(1)
            mc "*Sigh...*"
            mc "{i}(I really need to figure out how to at least get back to friendly terms with them.){/i}"
            mc "{i}(But how...?){/i}"
            jump Week6_Monday_Track
    else:
        if Layla_Dating == False:
            if Layla_Week5_Wednesday_BreakUp == True:
                if MC_Bike == True:
                    scene 14_052 with Dissolve(1)
                    mc "{i}(Still made it on time.){/i}"
                    scene 14_053 with Dissolve(1)
                    mc "{i}(Oh... Layla and Elena... Together...){/i}"
                    mc "{i}(Looks like they're talking again.){/i}"
                    mc "{i}(Layla probably called her yesterday after I talked to her. Or tried to, at least.){/i}"
                    mc "{i}(Good.){/i}"
                    scene 14_060 with Dissolve(1)
                    mc "Hey. Good morning."
                    la "..."
                    scene 14_061 with Dissolve(1)
                    la "Can we go inside?"
                    el "Uhm, sure."
                    mc "{i}(What did I expect? Just because they're talking again, doesn't mean they'll talk to me.){/i}"
                    mc "{i}(It'll probably take some time. If it happens at all.){/i}"
                    scene 14_062 with Dissolve(1)
                    el "*Whispers* Thank you."
                    mc "*Nods*"
                    jump Week6_Monday_Track
                else:
                    scene 14_056 with Dissolve(1)
                    ""
                    scene 14_063 with Dissolve(1)
                    mc "{i}(Oh... Layla and Elena... Together...){/i}"
                    mc "{i}(Looks like they're talking again.){/i}"
                    mc "{i}(Layla probably called her yesterday after I talked to her. Or tried to, at least.){/i}"
                    mc "{i}(Good.){/i}"
                    scene 14_061 with Dissolve(1)
                    mc "Hey. Good morning."
                    la "..."
                    la "Can we go inside?"
                    el "Uhm, sure."
                    mc "{i}(What did I expect? Just because they're talking again, doesn't mean they'll talk to me.){/i}"
                    mc "{i}(It'll probably take some time. If it happens at all.){/i}"
                    scene 14_064 with Dissolve(1)
                    el "*Whispers* Thank you."
                    mc "*Nods*"
                    jump Week6_Monday_Track
            else:
                if MC_Bike == True:
                    scene 14_052 with Dissolve(1)
                    mc "{i}(Still made it on time.){/i}"
                    scene 14_053 with Dissolve(1)
                    mc "{i}(Oh... Layla and Elena...){/i}"
                    mc "{i}(They don't know yet that I have a bike.){/i}"
                    if Alexis_Dating == True:
                        mc "{i}(Maybe Layla knows because of Lexi?){/i}"
                    else:
                        pass
                    mc "{i}(Should I scare them?){/i}"
                    menu:
                        "Rev your bike[KoGa3AutoWTChange1]{size=-4}(ElenaLayla Week6 Monday BikeRevScare) {/size} {/color}":
                            $ ElenaLayla_Week6_Monday_BikeRevScare = True
                            scene 14_065 with Dissolve(1)
                            play sound "Sounds/Motorcycle_Revving.mp3"
                            el "Aaah..."
                            la "..."
                            scene 14_066 with Dissolve(1)
                            el "Asshole!"
                            el "Was that really necessary?"
                            scene 14_067 with Dissolve(1)
                            mc "Haha. Sorry, sorry... Didn't mean to scare you like that."
                            la "[mc]!"
                            mc "Morning, girls!"
                        "Don't scare them":
                            scene 14_068 with Dissolve(1)
                            mc "Hey. Morning, girls!"
                            la "[mc]! Good morning."
                            el "Hey..."
                else:
                    scene 14_056 with Dissolve(1)
                    ""
                    scene 14_069 with Dissolve(1)
                    mc "Hey. Morning, girls!"
                    la "Good morning, [mc]."
                    el "Hey."
                scene 14_070 with Dissolve(1)
                mc "Hey, Layla. How's it going?"
                la "Pretty good! You?"
                mc "Good, good."
                scene 14_071 with Dissolve(1)
                mc "And hey! Long time no see, Elena!"
                el "Not long enough!"
                mc "I missed you, too!"
                scene 14_072 with Dissolve(1)
                mc "Come here, you!"
                el "Haha."
                scene 14_073 with Dissolve(1)
                mc "Did you enjoy spring break?"
                la "We did. But it could've been a week longer."
                mc "Haha. Never enough vacation days."
                la "They should swap school days with vacation days."
                scene 14_074 with Dissolve(1)
                mc "Your mom's the principal. Why don't you go and ask her?"
                la "She'd just laugh and send me right back to class."
                mc "Haha. Probably."
                if Valeria_Week5_Friday_Date == True:
                    scene 14_075 with Dissolve(1)
                    mc "By the way... Is Valeria here yet?"
                    la "Not that I've seen. Haven't spotted her so far."
                    mc "Hmm... I've tried calling her a few times, but she never picked up. Didn't reply to my messages either."
                    la "Yeah, I wanted to go running with her, but my calls just went straight to voicemail."
                    mc "Same here..."
                    scene 14_076 with Dissolve(1)
                    mc "That's weird."
                    la "She's probably just busy. Or maybe they went on a quick trip and she forgot her charger."
                    la "She could already be here, running laps around the track."
                    mc "That sounds like her."
                else:
                    pass
                scene 14_077 with Dissolve(1)
                n "*School bell*"
                mc "Guess we should head inside."
                la "Mm-hmm."
                scene 14_078 with Dissolve(1)
                mc "You've got cheer practice now, Elena?"
                el "I do. Want to join us?"
                mc "Haha. You never give up, do you?"
                el "Not until you come to a try-out, I won't."
                mc "Haha..."
                jump Week6_Monday_Track
        else:
            if MC_Bike == True:
                scene 14_052 with Dissolve(1)
                mc "{i}(Still made it on time.){/i}"
                scene 14_053 with Dissolve(1)
                mc "{i}(Oh... Layla and Elena...){/i}"
                mc "{i}(They probably don't know that it's me on the bike.){/i}"
                if Elena_LikeMC == True:
                    scene black with Dissolve(1)
                    transform moveup:
                        xalign 0.5 yalign 1.0
                        linear 5.0 yalign 0.0
                    show 14_079 at moveup
                    pause 3
                    mc "{i}(They're looking good again!){/i}"
                else:
                    scene black with Dissolve(1)
                    transform moveup:
                        xalign 0.5 yalign 1.0
                        linear 5.0 yalign 0.0
                    show 14_080 at moveup
                    pause 3
                    mc "{i}(My baby's looking good!){/i}"
                mc "{i}(Definitely happy to be back at school.){/i}"
                mc "{i}(Solely for this reason.){/i}"
                mc "{i}(Should I scare them a little?){/i}"
                menu:
                    "Rev your bike[KoGa3AutoWTChange1]{size=-4}(ElenaLayla Week6 Monday BikeRevScare) {/size} {/color}":
                        $ ElenaLayla_Week6_Monday_BikeRevScare = True
                        scene 14_065 with Dissolve(1)
                        play sound "Sounds/Motorcycle_Revving.mp3"
                        el "Aaah..."
                        la "..."
                        scene 14_066 with Dissolve(1)
                        el "Asshole!"
                        el "Was that really necessary?"
                        scene 14_067 with Dissolve(1)
                        mc "Haha. Sorry, sorry... Didn't mean to scare you like that."
                        la "[mc]!"
                        mc "Morning, girls!"
                    "Don't scare them":
                        scene 14_068 with Dissolve(1)
                        mc "Hey. Morning, girls!"
                        la "[mc]! Good morning."
                        el "Hey..."
                scene 14_081 with Dissolve(1)
                la "Hey!"
                mc "Haha. Hey, cutie!"
                scene 14_082 with Dissolve(1)
                ""
                if Elena_LikeMC == True:
                    scene 14_083 with Dissolve(1)
                    el "..."
                else:
                    pass
                scene 14_084 with Dissolve(1)
                mc "How are you?"
                la "I'm good. You?"
                mc "Perfect, now!"
                la "Haha."
                scene 14_085 with Dissolve(1)
                mc "Let me say hi to my favourite Latina."
                la "*Nods*"
                el "Dios mío..."
                scene 14_086 with Dissolve(1)
                mc "Hola, Elena Sofía Ortiz! Mi Latina favorita!"
                el "Idiota!"
                mc "Cuánto tiempo sin verte!\n(Long time no see!)"
                el "No lo suficiente!\n(Not long enough!)"
                mc "Haha. Yo también te quiero!\n(Love you, too!)"
                scene 14_087 with Dissolve(1)
                mc "Ven aquí! Como estás?\n(Come here, you! How are you?)"
                el "Haha. Estoy bien, y tú?"
                mc "Bien, gracias."
                if Elena_LikeMC == True:
                    scene 14_088 with Dissolve(1)
                    el "..."
                else:
                    pass
                scene 14_089 with Dissolve(1)
                la "Again with the Spanish, huh?"
                la "Are you talking about me again?"
                scene 14_090 with Dissolve(1)
                mc "Sí. Le dije a Elena que eres la más linda. \n(Yes. I told Elena that you are the cutest.)"
                la "..."
                la "Oh, that Linda again! I remember her!"
                mc "Haha."
                scene 14_091 with Dissolve(1)
                mc "Sólo superada por Elena.\n(Only second to Elena.)"
                el "*Shakes head* Heh..."
                la "Qué?"
                scene 14_092 with Dissolve(1)
                mc "Haha. Nada, nada..."
                la "One day! One day I'll understand everything you say, Prosciutto!"
                mc "Haha."
                el "Did you mean Perrito?"
                la "Yes, that!"
                scene 14_093 with Dissolve(1)
                mc "Haha... Prosciutto... Layla..."
                la "Stop laughing! I'm trying, okay?"
                mc "Haha... Try harder!"
                la "What? Let me hit you!"
                scene 14_094 with Dissolve(1)
                la "Aaah..."
                mc "You wanna fight again?"
                la "Nooo... [mc]..."
                scene 14_095 with Dissolve(1)
                n "*School bell*"
                mc "Saved by the bell..."
                mc "Lucky you! Someone must be looking out for you!"
                la "..."
                if Elena_LikeMC == True:
                    scene 14_097 with Dissolve(1)
                    mc "Come on, let's go."
                    la "Wait... I need to fix my hair."
                    mc "There's nothing to fix. You look cute, as always!"
                    scene 14_098 with Dissolve(1)
                    mc "Hey! Haha..."
                    la "At least piggyback me inside for what you did!"
                    mc "Haha. What I did?"
                    la "Yes!"
                    mc "Fine..."
                    scene 14_099 with Dissolve(1)
                    la "Yay!"
                    scene 14_100 with Dissolve(1)
                    el "..."
                else:
                    scene 14_096 with Dissolve(1)
                    mc "Come on. Let's go, girls!"
                    mc "You've got cheer practice now, Elena?"
                    el "I do. Want to join us?"
                    mc "Haha. You never give up, do you?"
                    el "Not until you come to a try-out, I won't."
                    mc "Haha..."
                jump Week6_Monday_Track
            else:
                scene 14_056 with Dissolve(1)
                ""
                scene 14_069 with Dissolve(1)
                mc "Hey. Morning, girls!"
                la "Good morning, [mc]."
                el "Hey."
                if Elena_LikeMC == True:
                    scene black with Dissolve(1)
                    transform moveup:
                        xalign 0.5 yalign 1.0
                        linear 5.0 yalign 0.0
                    show 14_101 at moveup
                    pause 3
                    mc "{i}(They're looking good again!){/i}"
                else:
                    scene black with Dissolve(1)
                    transform moveup:
                        xalign 0.5 yalign 1.0
                        linear 5.0 yalign 0.0
                    show 14_102 at moveup
                    pause 3
                    mc "{i}(My baby's looking good!){/i}"
                mc "{i}(Definitely happy to be back at school.){/i}"
                mc "{i}(Solely for this reason.){/i}"
                mc "{i}(Should I scare them a little?){/i}"
                scene 14_103 with Dissolve(1)
                la "Hey!"
                mc "Haha. Hey, cutie!"
                scene 14_082 with Dissolve(1)
                ""
                if Elena_LikeMC == True:
                    scene 14_083 with Dissolve(1)
                    el "..."
                else:
                    pass
                scene 14_104 with Dissolve(1)
                mc "How are you?"
                la "I'm good. You?"
                mc "Perfect, now!"
                la "Haha."
                scene 14_105 with Dissolve(1)
                mc "Let me say hi to my favourite Latina."
                la "*Nodding*"
                el "Dios mío..."
                scene 14_086 with Dissolve(1)
                mc "Hola, Elena Sofía Ortiz! Mi Latina favorita."
                el "Idiota!"
                mc "Cuánto tiempo sin verte!\n(Long time no see!)"
                el "No lo suficiente!\n(Not long enough!)"
                mc "Haha. Yo también te quiero!\n(Love you, too!)"
                scene 14_087 with Dissolve(1)
                mc "Ven aquí! Como estas?\n(Come here, you! How are you?)"
                el "Haha. Estoy bien, y tú?"
                mc "Bien, gracias."
                if Elena_LikeMC == True:
                    scene 14_088 with Dissolve(1)
                    el "..."
                else:
                    pass
                scene 14_106 with Dissolve(1)
                la "Again with the Spanish, huh?"
                la "Are you talking about me again?"
                scene 14_107 with Dissolve(1)
                mc "Sí. Le dije a Elena que eres la más linda.\n(Yes. I told Elena that you are the cutest.)"
                la "..."
                la "Oh, that Linda again! I remember her!"
                mc "Haha."
                scene 14_091 with Dissolve(1)
                mc "Sólo superada por Elena.\n(Only second to Elena.)"
                el "*Shakes head* Heh..."
                la "Qué?"
                scene 14_092 with Dissolve(1)
                mc "Haha. Nada, nada..."
                la "One day! One day I will understand everything you say, Prosciutto!"
                mc "Haha."
                el "Did you mean Perrito?"
                la "Yes, that!"
                scene 14_093 with Dissolve(1)
                mc "Haha... Prosciutto... Layla..."
                la "Stop laughing! I'm trying, okay?"
                mc "Haha... Try harder!"
                la "What? Let me hit you!"
                scene 14_108 with Dissolve(1)
                la "Aaah..."
                mc "You wanna fight again?"
                mc "Didn't you learn your lesson yesterday, together with your sister, about what happens to bad girls?"
                la "Nooo... [mc]..."
                scene 14_095 with Dissolve(1)
                n "*School bell*"
                mc "Saved by the bell..."
                mc "Lucky you! Someone must be looking out for you!"
                la "..."
                if Elena_LikeMC == True:
                    scene 14_097 with Dissolve(1)
                    mc "Come on, let's go."
                    la "Wait... I need to fix my hair."
                    mc "There's nothing to fix. You look cute, as always!"
                    scene 14_098 with Dissolve(1)
                    mc "Hey! Haha..."
                    la "At least piggyback me inside for what you did!"
                    mc "Haha. What I did?"
                    la "Yes!"
                    mc "Fine..."
                    scene 14_099 with Dissolve(1)
                    la "Yay!"
                    scene 14_109 with Dissolve(1)
                    el "..."
                else:
                    scene 14_096 with Dissolve(1)
                    mc "Come on. Let's go, girls!"
                    mc "You've got cheer practice now, Elena?"
                    el "I do. Want to join us?"
                    mc "Haha. You never give up, do you?"
                    el "Not until you come to a try-out, I won't."
                    mc "Haha..."
                jump Week6_Monday_Track

label Week6_Monday_Track:
    scene black with Dissolve(2)
    pause 2
    if Layla_End == True:
        scene 14_110 with Dissolve(1)
        ""
        scene 14_112 with Dissolve(1)
        mc "*Sigh...*"
    else:
        if Layla_Dating == False:
            if Layla_Week5_Wednesday_BreakUp == True:
                scene 14_111 with Dissolve(1)
                ""
                scene 14_112 with Dissolve(1)
                mc "*Sigh...*"
                scene 14_113 with Dissolve(1)
                to "Trouble in paradise?"
                mc "..."
                to "What did you do? Break her little heart?"
                mc "{i}(I don't need this now!){/i}"
                scene 14_114 with Dissolve(1)
                mc "Shut up, Tori!"
                mc "How about you go annoy someone else!"
                to "Haha. I must've guessed right."
                if MC_Week3_Saturday_TC_Win == True:
                    scene 14_115 with Dissolve(1)
                    to "Don't worry, you'll get over it."
                    to "And if you need help with that, I have some ideas that'll cheer you up!"
                    scene 14_116 with Dissolve(1)
                    la "..."
                else:
                    pass
            else:
                scene 14_117 with Dissolve(1)
                ""
                scene 14_118 with Dissolve(1)
                mc "Hey, again."
                la "Haha. Hey!"
                la "I meant to say this earlier, but I really like your new haircut!"
                la "I think you get your hair cut more often than I do."
                mc "Probably. Perks of having your hairstylist as your neighbour."
                la "Haha, yeah."
                if Valeria_Week5_Friday_Date == True:
                    scene 14_119 with Dissolve(1)
                    mc "By the way... Still no sign of Valeria, huh?"
                    la "Nope. I tried calling her a few minutes ago, but just got her voicemail again."
                    mc "Hmm..."
                    mc "Maybe Coach knows something? I'll ask him when he gets here."
                    la "Yeah."
                else:
                    scene 14_120 with Dissolve(1)
                    mc "By the way. Valeria's not here?"
                    la "No, haven't seen her. I tried calling over the weekend, but it went straight to voicemail every time."
                    mc "Hmm... Maybe she's sick?"
                    la "Could be. If she doesn't show up, I'll ask Coach later. Maybe he knows something."
                    mc "Yeah."
                if Alexis_Week5_Thursday_BreakUp == True:
                    scene 14_121 with Dissolve(1)
                    la "[mc]... Can we talk for a minute?"
                    mc "Aren't we talking now?"
                    la "I mean somewhere away from everyone else."
                    mc "Uhm... Okay?"
                    scene 14_122 with Dissolve(1)
                    mc "So, what's up?"
                    la "Uhm..."
                    mc "Come on, just say it."
                    scene 14_123 with Dissolve(1)
                    la "Lex told me you guys... broke up..."
                    mc "Oh... Yeah... We did..."
                    mc "I think it all went too fast and... I don't know. It just wasn't the right time for us."
                    la "*Nods* That's what she told me, too."
                    mc "We're still friends, but, well... Not together anymore."
                    scene 14_124 with Dissolve(1)
                    mc "How's she doing?"
                    la "I think she's alright. I heard her crying a few times..."
                    mc "{i}(Fuck...){/i}"
                    la "But it helps that Lakeyn is here. She keeps her distracted."
                    mc "That's good to hear."
                    scene 14_125 with Dissolve(1)
                    la "How about you?"
                    mc "I'm okay, I guess. Haven't really had time to process it all yet."
                    mc "I was away over the weekend and... A lot happened."
                    mc "Maybe it'll hit me eventually."
                    la "Yeah..."
                    scene 14_126 with Dissolve(1)
                    la "Want a hug?"
                    mc "I could definitely use one."
                    scene 14_127 with Dissolve(1)
                    mc "Thanks, Layla."
                    la "..."
                else:
                    pass
        else:
            scene 14_128 with Dissolve(1)
            ""
            scene 14_129 with Dissolve(1)
            mc "..."
            mc "{i}(All the motivation I need!){/i}"
            scene 14_130 with Dissolve(1)
            mc "Hey again, cutie!"
            la "Haha, hey!"
            scene 14_131 with Dissolve(1)
            ""
            scene 14_132 with Dissolve(1)
            to "..."
            to "They have rooms for that, you know!"
            to "Not everyone wants front-row seats to your PDA!"
            scene 14_133 with Dissolve(1)
            mc "That's rich coming from you, Victoria!"
            to "It's Tori!"
            la "*Whispers* Don't aggravate her, or we'll be stuck with her attitude all day."
            mc "*Whispers* You're right."
            scene 14_134 with Dissolve(1)
            mc "Hmm..."
            la "What?"
            mc "Just realised. Valeria's not here..."
            scene 14_135 with Dissolve(1)
            la "Yeah, I have no idea where she is."
            la "I tried calling her a few times over the weekend. Just voicemail..."
            la "Tried again a few minutes ago when I didn't see her, same thing."
            mc "Weird. She's usually the first one here."
            scene 14_136 with Dissolve(1)
            mc "Maybe she's sick? Unlikely, but possible."
            la "Could be, but she could at least pick up then, or message me back."
            mc "Hmm, yeah..."
            la "I'll ask Coach later. Maybe he knows something."
    scene 14_137 with Dissolve(1)
    tm "Good morning, everyone!"
    st "Morning, Coach!"
    to "Hey, Mike!"
    tm "Alright, gather around."
    scene 14_138 with Dissolve(1)
    tm "Everyone here? Yes? Good."
    tm "I hope you all had a great spring break..."
    tm "And I hope you didn't slack off on your training!"
    tm "Trust me, I'll know if you did."
    scene 14_139 with Dissolve(1)
    tm "Anyway... This week's training will be a bit different, and there's a reason for that."
    mc "{i}(Probably something to do with the relay tournament.){/i}"
    tm "I've got some good news... And some bad news!"
    if Valeria_Week5_Friday_Date == True:
        scene 14_140 with Dissolve(1)
        mc "{i}(Bad news?){/i}"
        mc "{i}(Wait... Is this about Valeria? Is that why she's not here.){/i}"
    else:
        pass
    scene 14_141 with Dissolve(1)
    tm "Let's start with the good news."
    tm "Our school's been invited to compete in the Southern Relay Tournament!"
    st "Hell yeah!"
    tm "One of the schools had to drop out due to a bunch of injuries. And thanks to our strong performance at training camp, we were offered their spot."
    tm "Naturally, we accepted."
    if Layla_End == True:
        pass
    else:
        if Layla_Week5_Wednesday_BreakUp == True:
            pass
        else:
            scene 14_142 with Dissolve(1)
            la "*Whispers* A relay race! That sounds fun!"
            mc "*Whispers* Yeah! Can't wait for it."
    scene 14_143 with Dissolve(1)
    tm "Now for the bad news..."
    tm "The tournament is happening this weekend, which means we only have a few days to prepare."
    if Valeria_Week5_Friday_Date == True:
        mc "{i}(So the bad news isn't about Val... That's a relief...){/i}"
    else:
        pass
    tm "And since there's not enough time to organise everything, we won't be taking the full team."
    tm "Only the four runners competing in the tournament will come along. Sorry, everyone."
    scene 14_144 with Dissolve(1)
    tm "I know that's a bit of a letdown..."
    tm "But I still want everyone to take part in relay training this week."
    tm "Another event might be just around the corner, and in a few weeks, we've got our rivalry tournament against Palm City High!"
    da "Heh... Rivalry..."
    scene 14_145 with Dissolve(1)
    tm "Oh, and did I mention? It's a mixed relay race!"
    tm "Two boys, two girls!"
    mc "{i}(Mixed... That's interesting.){/i}"
    scene 14_146 with Dissolve(1)
    tm "I'll be choosing the runners later today."
    tm "That way, the team can start training together and build some chemistry right away."
    tm "We're still finalising travel and lodging details."
    tm "Once we have everything sorted, I'll share more info."
    scene 14_147 with Dissolve(1)
    tm "Any questions?"
    tm "..."
    tm "No?"
    tm "Alright. let's get to it!"
    tm "Start with a few laps around the track to warm up!"
    if Layla_End == True:
        pass
    else:
        if Layla_Week5_Wednesday_BreakUp == True:
            pass
        else:
            scene 14_148 with Dissolve(1)
            la "Coach, can I ask something?"
            tm "Sure, Layla. What's on your mind?"
            scene 14_149 with Dissolve(1)
            la "Do you know why Valeria isn't here today?"
            tm "Hmm... She's not here? I thought she was around."
            tm "No, I haven't heard anything. I don't know where she is."
            mc "{i}(Even Coach has no idea...){/i}"
            scene 14_150 with Dissolve(1)
            tm "I'll check with the front office after practice. Maybe she left a message."
            la "Thanks, Coach."
    scene black with Dissolve(1)
    pause 2
    scene 14_151 with Dissolve(1)
    ""
    if Valeria_Week5_Friday_Date == True:
        scene 14_152 with Dissolve(1)
        mc "{i}(Seriously... Where is that girl?){/i}"
        mc "{i}(This is starting to worry me. No one seems to know anything...){/i}"
    else:
        pass
    scene black with Dissolve(1)
    pause 2
    scene 14_153 with Dissolve(1)
    tm "It's a pretty long stretch to make this exchange."
    tm "You might think you need to be closer for the handover, but this distance is fine."
    tm "Everyone's handover style is a bit different, so you'll figure out what works best during training."
    if Tori_End == False:
        scene 14_154 with Dissolve(1)
        to "Shouldn't [mc] be the one handing me his dick?"
        tm "Tori..."
        to "I mean stick! Stick..."
        tm "Focus!"
        to "I am, Mike!"
    else:
        scene 14_155 with Dissolve(1)
        to "Long stretch..."
        to "Need to be closer... I'll gladly accept your stick anytime, Mike!"
        mc "*Shakes head*"
        tm "Focus, Tori!"
        to "I am!"
    scene 14_156 with Dissolve(1)
    tm "The incoming runner will give a signal, a call."
    tm "When that call is made, the outgoing runner keeps their elbows tight..."
    tm "Raises their arm, opens their hand, fingers pointed outward..."
    scene 14_157 with Dissolve(1)
    tm "The incoming runner's job is to land the baton in their hand."
    tm "It doesn't have to be instant. You'll be coming in fast, and the other runner is just accelerating."
    tm "The key is to stay calm."
    tm "Call the stick and push it in their hand. Watch the elbow, watch the hand!"
    tm "Everyone got it? We'll test this in practice first, and then go over the exchange zones."
    scene 14_158 with Dissolve(1)
    if Tori_End == False:
        to "Here's my stick, handsome!"
        mc "..."
    else:
        to "Get ready, loser!"
        mc "..."
    scene 14_159 with Dissolve(1)
    tm "Okay, not bad, but I've got a few notes."
    tm "Tori... When you're calling for the handoff, let's keep it to 'stick' or just 'hand', alright?"
    tm "[mc], start accelerating a bit earlier next time. And don't look back when Tori passes you the baton."
    tm "Focus on picking up speed. It's her job to get it into your hand."
    mc "Got it."
    tm "Let's run it again!"
    scene 14_160 with Dissolve(1)
    to "Stick!"
    tm "Much better already!"
    tm "Tori, don't slow down. Give your call earlier so [mc] can match your pace more easily."
    to "..."
    tm "Again!"
    scene 14_161 with vpunch
    mc "..."
    scene 14_162 with Dissolve(1)
    mc "What the fuck, Tori!"
    to "Haha."
    to "I forgot to call stick! My bad!"
    tm "*Shakes head*"
    scene 14_163 with Dissolve(1)
    tm "Alright, that's enough, you two."
    tm "I'd really appreciate it if you took this a bit more seriously."
    tm "Go take a break."
    tm "Next pair... TJ and Layla. TJ, you'll hand off to Layla."
    scene 14_164 with Dissolve(1)
    mc "Thanks a lot for that, Tori!"
    mc "Some of us are actually trying to do this properly!"
    to "Heh... How hard can it be to pass a stick..."
    to "Don't act like you've got one shoved up your ass!"
    scene 14_165 with Dissolve(1)
    to "Oh wait... You did!"
    to "Haha."
    mc "*Sigh*"
    scene 14_166 with Dissolve(1)
    tj "Hand!"
    tm "Yes! Very nice!"
    scene black with Dissolve(1)
    pause 2
    scene 14_167 with Dissolve(1)
    tm "Darryl, [mc], can I talk to you both for a moment?"
    tm "Everyone else, keep practising the handoff."
    scene 14_168 with Dissolve(1)
    tm "Alright, listen. We all know you're our fastest runners."
    tm "But we also know there's been... some tension between you two."
    tm "This relay is all about teamwork, so I need to know... Can you both set your differences aside and work together?"
    tm "Is that possible?"
    scene 14_169 with Dissolve(1)
    da "..."
    mc "..."
    scene 14_170 with Dissolve(1)
    da "Yes..."
    if Mike_Name == True:
        mc "Of course, Mike."
    else:
        mc "Of course, Coach."
    tm "That's what I like to hear!"
    tm "If you two work together, we've got a real shot at an amazing result in this tournament."
    scene 14_171 with Dissolve(1)
    tm "So, you two will be our male runners."
    tm "Now, for the girls... I could use a little help deciding."
    tm "I'm leaning toward Valeria for the first spot. She's our fastest, and has real tournament experience."
    tm "But that depends on whether she's just out sick or something more serious. If she's good to go, that decision's basically made. I'll find out after training."
    scene 14_172 with Dissolve(1)
    tm "Now, for the second girl..."
    tm "It's really close between Tori and Layla. They've both been performing at a similar level, lately."
    tm "So I'm leaving that choice up to you. Think about who will mesh better with the team."
    tm "I'll give you a few minutes to talk it over."
    mc "*Nods*"
    scene 14_173 with Dissolve(1)
    da "*Sigh...*"
    da "You'd better bring your A-game and not screw this up for me!"
    mc "..."
    mc "{i}(Here we go again... Maybe I should just try to keep things civil for once.){/i}"
    scene 14_174 with Dissolve(1)
    mc "So, uhm... Any preference on who you'd rather have on the team?"
    da "I wish Ramirez was still running so we wouldn't even need to have this conversation..."
    mc "{i}(Ramirez? Is he talking about Gabi? That can't be right...){/i}"
    if Gabi_End == True:
        pass
    else:
        mc "{i}(I saw those pictures of Gabi from when she was on a track team... but how would Darryl know about that?){/i}"
    scene 14_175 with Dissolve(1)
    mc "Ramirez? As in Gabi? The Spanish teacher?"
    da "What the fuck? No! Why would I mean her?"
    da "Daniela Ramirez, her sister!"
    mc "{i}(Gabi has a sister? I didn't know that.){/i}"
    scene 14_176 with Dissolve(1)
    mc "Daniela...? Hmm..."
    da "Seriously? How long have you been at this school and you still don't know half the people in your class?"
    da "She literally sits next to you in geography. Always wearing a cap."
    scene 14_177 with Dissolve(1)
    mc "Oh... Her..."
    mc "I didn't know she and Gabi were related. Sisters..."
    scene 14_178 with Dissolve(1)
    da "You really don't seem to know many people around here."
    da "Maybe spend less time hanging out with that Zach weirdo and get to know others."
    mc "Yeah... you're probably right."
    da "Heh..."
    scene 14_179 with Dissolve(1)
    mc "So, Daniela... She was fast?"
    da "Fast? You have no idea. If she was still running, we'd sweep this tournament."
    da "You know Sha'Carri, right?"
    mc "Yeah, she won the girls' event at training camp."
    da "Before Sha'Carri was number one, it was Daniela."
    da "She used to beat her every single time."
    scene 14_180 with Dissolve(1)
    mc "Whoa... Faster than Sha'Carri? That's insane."
    mc "But if she was that good, why'd she quit?"
    da "Car accident."
    mc "She was in a car accident?"
    scene 14_181 with Dissolve(1)
    da "A drunk driver hit her and her mom while they were crossing the street."
    mc "Damn..."
    da "They both survived, thankfully. But Daniela broke both legs and a bunch of other bones too. I don't know the full extent."
    mc "Was that recent?"
    da "No... happened a while ago."
    scene 14_182 with Dissolve(1)
    mc "And she hasn't wanted to run since?"
    da "I don't know if she doesn't want to... or if she can't."
    da "She distanced herself from everyone after she came back. After months of physical therapy, she just stopped showing up to track stuff."
    mc "{i}(The way he's talking about her... Did he have feelings for her?){/i}"
    scene 14_183 with Dissolve(1)
    mc "Man... That's uh... Yeah..."
    mc "{i}(Darryl's right. I don't really know anyone here, or what they've been through.){/i}"
    mc "{i}(I actually want to learn more about Daniela and what happened to her.){/i}"
    mc "{i}(And somehow, I'm having a normal conversation with Darryl. Weird.){/i}"
    scene 14_184 with Dissolve(1)
    mc "Did they at least catch the driver?"
    da "I think so... not sure though."
    da "It's strange... There was a lot about the accident in the news, but nothing about the driver or what happened to him."
    mc "Hmm..."
    scene 14_185 with Dissolve(1)
    to "What have those two been talking about all this time?"
    la "..."
    to "They barely said two sentences to each other before, and now they're just sitting there chatting for like ten minutes..."
    scene 14_186 with Dissolve(1)
    to "But don't you think they're kinda alike?"
    la "Not really..."
    to "Both stubborn, definitely. And super competitive."
    scene 14_187 with Dissolve(1)
    to "And look at them..."
    to "Same outfit... Red shoes, grey joggers, black tank top."
    la "..."
    scene 14_188 with Dissolve(1)
    da "Should we get on with it?"
    da "Who do you want? Tori or Layla? I don't really care."
    mc "..."
    scene 14_189 with Dissolve(1)
    if Layla_End == True:
        mc "{i}(Who should I pick?){/i}"
        mc "{i}(Layla and I aren't exactly on good terms. Or any terms, really.){/i}"
        mc "{i}(But maybe this could be a chance to patch things up.){/i}"
        mc "{i}(Training together, going to the tournament...){/i}"
    else:
        if Layla_Dating == False:
            if Layla_Week5_Wednesday_BreakUp == True:
                mc "{i}(Who should I pick?){/i}"
                mc "{i}(Layla and I aren't on great terms right now.){/i}"
                mc "{i}(But maybe this could be a chance to patch things up.){/i}"
                mc "{i}(Training together, going to the tournament...){/i}"
            else:
                mc "{i}(Who should I pick?){/i}"
                mc "{i}(Layla's the obvious choice. We're friends, we get along well.){/i}"
                mc "{i}(And we already train together.){/i}"
                mc "{i}(I'm sure she'd love this opportunity.){/i}"
        else:
            mc "{i}(It's pretty clear I want to pick Layla.){/i}"
            mc "{i}(She would love that too.){/i}"
            mc "{i}(Spending a day away with her...){/i}"
            mc "{i}(This could be great.){/i}"
    if Tori_End == True:
        mc "{i}(And Tori is... well, Tori.){/i}"
    else:
        if Tori_Week3_Saturday_TC_Sex == False:
            mc "{i}(And Tori is... well, Tori.){/i}"
        else:
            mc "{i}(If I pick Tori, we'll probably just end up hooking up. Not the worst either.){/i}"
            mc "{i}(Does Darryl even know about that?){/i}"
    menu:
        "Layla[KoGa3AutoWTChange1]{size=-4}(Week6 Monday Relay PickLayla) {/size} {/color}":
            $ Week6_Monday_Relay_PickLayla = True
            scene 14_190 with Dissolve(1)
            mc "I'd choose Layla."
            da "Knew you would."
        "Tori[KoGa3AutoWTChange1]{size=-4}(Week6 Monday Relay PickTori) {/size} {/color}":
            $ Week6_Monday_Relay_PickTori = True
            scene 14_190 with Dissolve(1)
            mc "I think I'll go with Tori."
            da "Didn't see that coming."
    mc "Are you okay with that?"
    da "Like I said, I don't really care. I want to win!"
    scene 14_191 with Dissolve(1)
    if Week6_Monday_Relay_PickLayla == True:
        da "Layla it is."
        da "If Coach agrees, that's our team."
        mc "Mm-hmm."
    else:
        da "Tori it is."
        da "If Coach agrees, that's our team."
        mc "Mm-hmm."
    mc "{i}(Why the fuck am I smiling...?){/i}"
    scene black with Dissolve(1)
    pause 2
    scene 14_192 with Dissolve(1)
    tm "That was an amazing training session! Thanks to everyone for the hard work!"
    tm "I hope you'll keep this up all the way through the end of the school year."
    tm "Now, about the relay race... I haven't made the final decision yet, but I will before the day's over."
    tm "I'll post the team roster in our group chat once it's decided."
    scene 14_193 with Dissolve(1)
    tm "Alright, that's all for today. Thanks again, everyone!"
    tm "Go hit the showers, and I'll see you tomorrow."
    tm "Oh, and don't forget to check your schedules! We've got practice every day this week!"
    if Layla_End == True:
        jump Week6_Monday_Hallway
    else:
        if Layla_Dating == False:
            if Layla_Week5_Wednesday_BreakUp == True:
                jump Week6_Monday_Hallway
            else:
                pass
        else:
            pass
    scene 14_194 with Dissolve(1)
    la "Nggh... That was a fun training session, right?"
    mc "Yeah. It was nice doing something different for a change."
    la "Can't wait to see what else we have planned this week."
    scene 14_195 with Dissolve(1)
    la "So, what were you and Darryl talking about?"
    mc "{i}(I knew she'd be curious.){/i}"
    mc "Uhm... Coach wanted us to clear the air and start working together."
    la "Oh... And did you?"
    mc "We'll see."
    scene 14_196 with Dissolve(1)
    la "Tori said you guys are a lot alike."
    mc "Really?"
    la "I don't usually listen to Tori, but she was right about you guys wearing the same stuff. It was kinda funny."
    mc "Wearing the same stuff?"
    la "Yeah. Red shoes, grey joggers, and black tank tops. Both of you."
    scene 14_197 with Dissolve(1)
    mc "..."
    mc "That's just a coincidence. Doesn't mean we're alike."
    mc "Remember when we both wore t-shirts with skulls on them?"
    la "Mm-hmm."
    mc "Tori's probably just messing with you again."
    la "Yeah, I think so too."
    scene 14_198 with Dissolve(1)
    la "Anyway... I can't wait to find out who'll be picked for the relay tournament."
    mc "Yeah..."
    mc "Who do you think it's gonna be?"
    mc "{i}(Even though I already know, I still want to know what she thinks.){/i}"
    la "Hmm..."
    scene 14_199 with Dissolve(1)
    la "For the boys, it's gonna be you and Darryl."
    la "You're easily the fastest runners on the team."
    la "As for the girls..."
    la "If Valeria's not sick, Coach is picking her. No doubt."
    la "Otherwise..."
    scene 14_200 with Dissolve(1)
    la "I hope it's gonna be me!"
    mc "Haha."
    if Layla_Dating == True:
        mc "{i}(She really has such a cute side to her.){/i}"
    else:
        mc "{i}(Look at this cutie!){/i}"
    scene 14_201 with Dissolve(1)
    la "What about you? Who do you think it'll be?"
    if Week6_Monday_Relay_PickTori == True:
        mc "{i}(I can't exactly tell her I picked Tori... And that's why she probably won't be in the tournament...){/i}"
        mc "{i}(Why did I pick Tori...?){/i}"
        mc "Uhm... I think I'd go with the same people you just said."
        scene 14_202 with Dissolve(1)
        la "So, you're hoping it'll be me too?"
        mc "{i}(That look on her face...){/i}"
        mc "{i}(What the hell did I do?){/i}"
        mc "Yeah..."
        scene 14_203 with Dissolve(1)
        la "It's going to be so much fun!"
        mc "{i}(Or a complete disaster...){/i}"
        mc "I hope so, yeah..."
    else:
        mc "Hmm..."
        scene 14_204 with Dissolve(1)
        mc "Okay... I gotta let you in on a little secret."
        la "*Whispers* Okay!"
        mc "{i}(Haha. The way she immediately starts whispering.){/i}"
        mc "*Whispers* But you have to promise to keep it quiet."
        la "*Nods eagerly*"
        scene 14_205 with Dissolve(1)
        mc "*Whispers* I already know who's going to be picked for the tournament."
        la "*Whispers* You do?"
        la "*Whispers* How?"
        mc "*Whispers* That part stays a secret."
        scene 14_206 with Dissolve(1)
        mc "*Whispers* Want to know who?"
        la "Yes!"
        mc "*Whispers* It's going to be Valeria, me, Darryl and..."
        mc "*Whispers* You!"
        scene 14_207 with Dissolve(1)
        la "KYAAA!"
        mc "Shhh! I told you to keep it down!"
        la "Haha, sorry, sorry. I'm just so happy!"
        la "You're not joking, right?"
        mc "Nope, I'm not..."
        if Layla_Dating == False:
            scene 14_208 with Dissolve(1)
            la "This is going to be so much fun!"
            mc "Yeah, it will."
            mc "But seriously... No telling anyone! Okay?"
            la "I won't, I promise."
            scene 14_209 with Dissolve(1)
            mc "And act surprised when Coach makes the announcement."
            la "I won't have to act. I'll be happy no matter what!"
            mc "Haha."
        else:
            scene 14_210 with vpunch
            la "Kyaa..."
            mc "Haha. You crazy girl!"
            scene 14_211 with Dissolve(1)
            la "Aaah-haha..."
            la "[mc]..."
            mc "Remember, not a word to anyone, alright?"
            la "Haha. I won't, I won't."
            scene 14_212 with Dissolve(1)
            ""
            scene 14_213 with Dissolve(1)
            mc "Can't wait to spend a whole day away with you."
            la "*Nods*"
            scene 14_214 with Dissolve(1)
            mc "..."
            scene 14_215 with Dissolve(1)
            mc "Let's go hit the showers, so you're ready for your favourite class."
            la "It's not my favourite class!"
            mc "No? Could've sworn it was."
            la "It's yours! So you can stare at Ramirez again! I mean *mockingly* Gabi..."
            mc "Haha."
            scene 14_216 with Dissolve(1)
            mc "Hey? Wanna shower together?"
            la "..."
            la "You know you can't go in the girls' showers."
            mc "Who said anything about that? You can come to mine."
            scene 14_217 with Dissolve(1)
            la "I'm not going into the boys' showers!"
            la "It's probably all dirty and sticky in there..."
            mc "Haha. Dirty and sticky? What do you think we're doing in there?"
            la "I don't know and I don't want to know!"
            mc "Haha."
            if Layla_Week1_Piggyback == False:
                jump Week6_Monday_Hallway
            else:
                scene 14_218 with Dissolve(1)
                mc "Another piggyback ride..."
                mc "I should've never started this!"
                la "But they're so much fun!"
                mc "For you!"
                scene 14_219 with Dissolve(1)
                mc "Or... Did you change your mind and you're coming with me to the boys' showers?"
                la "No!"
                mc "Too late! You're coming with me now!"
                scene 14_220 with Dissolve(1)
                la "Nooo! [mc]!"
    jump Week6_Monday_Hallway

label Week6_Monday_Hallway:
    scene black with Dissolve(1)
    pause 2
    scene 14_221 with Dissolve(1)
    ""
    if Erynn_Week5_Tuesday_Photoshoot_Join == False:
        pass
    else:
        scene 14_222 with Dissolve(1)
        x "No, I think it's him."
        x "It can't be."
        x "Why not? Just look. He cut his hair, sure, but..."
        scene 14_223 with Dissolve(1)
        x "The tattoos are the same!"
        x "Hmm..."
        x "Okay... You might be right."
        scene 14_224 with Dissolve(1)
        x "Should we ask him?"
        x "No!"
        mc "{i}(What's going on?){/i}"
        mc "{i}(Whatever...){/i}"
    if Layla_End == True:
        scene 14_227 with Dissolve(1)
        mc "{i}(Looks like Elena had cheer practice.){/i}"
        if Week6_Monday_Relay_PickTori == True:
            mc "{i}(We really do have some stunning cheerleaders at this school.){/i}"
        else:
            mc "{i}(If I can patch things up with Layla during the relay... Maybe Elena will come around too?){/i}"
            mc "{i}(I kinda miss her snarky comments, not gonna lie.){/i}"
    else:
        scene 14_225 with Dissolve(1)
        mc "..."
        scene black with Dissolve(1)
        transform moveup:
            xalign 0.5 yalign 1.0
            linear 5.0 yalign 0.0
        show 14_226 at moveup
        pause 3
        mc "{i}(Elena in a cheerleading outfit...){/i}"
        mc "{i}(Yes please!){/i}"
        if Layla_Week5_Wednesday_BreakUp == True:
            scene 14_228 with Dissolve(1)
            mc "Hey..."
            el "Hey."
            mc "Elena... Can we maybe talk?"
            scene 14_229 with Dissolve(1)
            el "How about after school?"
            mc "Yeah, that's fine."
            el "I'll text you later."
            mc "Okay."
            scene 14_230 with Dissolve(1)
            mc "*Sigh...*"
            mc "{i}(I said I want to talk, but I don't even know what to say.){/i}"
            mc "{i}('Hey Elena, since you and Layla are friends again... Can we start dating now?'){/i}"
            mc "{i}(That sounds so dumb...){/i}"
        else:
            scene 14_231 with Dissolve(1)
            mc "Hey again!"
            el "Hey..."
            mc "Morning, Sienna."
            si "Hi, [mc]."
            scene 14_232 with Dissolve(1)
            mc "What are you girls doing to me!"
            el "What?"
            mc "The cheerleading outfits... You two look amazing!"
            scene 14_233 with Dissolve(1)
            mc "Can't you walk around like that every day?"
            el "I pretty much do!"
            el "And if you want to keep seeing it, you know what to do."
            mc "It's getting harder to resist each day!"
            el "Haha."
            scene 14_234 with Dissolve(1)
            el "See you later, in geography!"
            mc "Yeah. Bye, girls."
            si "Bye."
            if Elena_LikeMC == True:
                scene 14_235 with Dissolve(1)
                mc "..."
                el "..."
                scene 14_236 with Dissolve(1)
                el "*Sigh*"
            else:
                pass
    scene 14_237 with Dissolve(1)
    mc "{i}(Weird that I haven't seen Zach yet.){/i}"
    mc "{i}(Not that I'm complaining. It's not like I'm looking for him.){/i}"
    mc "{i}(Maybe he's not even here today...){/i}"
    jump Week6_Monday_Spanish

label Week6_Monday_Spanish:
    scene black with Dissolve(1)
    pause 2
    scene 14_238 with Dissolve(1)
    mc "{i}(Wait... Am I the first one here?){/i}"
    mc "{i}(That never happens!){/i}"
    scene 14_239 with Dissolve(1)
    mc "{i}(Gabi's already here...){/i}"
    mc "{i}(So I'm not in the wrong classroom.){/i}"
    if Gabi_End == True:
        mc "Buenos días."
        scene 14_240 with Dissolve(1)
        tr "Buenos días."
        mc "Estoy en la clase correcta, verdad?\n(I'm in the correct class, right?)"
        tr "Sí."
        mc "Vale. Sólo pensaba que como no hay nadie aquí.\n(Okay. I just wondered because no one is here.)"
        scene 14_243 with Dissolve(1)
        mc "*Sigh*"
        if Layla_End == True:
            pass
        else:
            if Layla_Dating == False:
                pass
            else:
                scene 14_256 with Dissolve(1)
                la "Here you are!"
                mc "Hey."
                la "I was looking for you in the hallways."
                mc "If you'd showered with me, you wouldn't have had to!"
                la "Haha."
                scene 14_257 with Dissolve(1)
                ""
    else:
        scene 14_241 with Dissolve(1)
        mc "{i}(I missed that ass!){/i}"
        mc "{i}(The way she squeezes it when she's writing on the blackboard...){/i}"
        mc "{i}(Class hasn't even started and I'm already getting horny.){/i}"
        mc "Hola. Buenos días, Gabi!"
        scene black with Dissolve(1)
        transform moveup:
            xalign 0.5 yalign 1.0
            linear 5.0 yalign 0.0
        show 14_242 at moveup
        pause 3
        tr "Buenos días! Y es la señorita Ramírez!\n(Good morning. And it's Ms Ramirez!)"
        mc "Sí, perdón. Señorita Ramírez!"
        tr "..."
        scene 14_240 with Dissolve(1)
        mc "Estoy en la clase correcta, verdad?\n(I'm in the correct class, right?)"
        tr "Sí."
        mc "Vale. Sólo pensaba que como no hay nadie aquí.\n(Okay. I just wondered because no one is here.)"
        menu:
            "Go to your seat":
                scene 14_243 with Dissolve(1)
                mc "*Sigh*"
                scene 14_244 with Dissolve(1)
                tr "..."
                if Layla_End == True:
                    pass
                else:
                    if Layla_Dating == False:
                        pass
                    else:
                        $ Gabi_Jealousy += 2
                        # Gabi_Jealousy = 2
                        scene 14_256 with Dissolve(1)
                        la "Here you are!"
                        mc "Hey."
                        la "I was looking for you in the hallways."
                        mc "If you'd showered with me, you wouldn't have had to!"
                        la "Haha."
                        scene 14_257 with Dissolve(1)
                        ""
                        scene 14_258 with Dissolve(1)
                        tr "..."
                        scene 14_259 with Dissolve(1)
                        tr "Layla, can you go to your desk?"
                        la "Why? Class hasn't started yet!"
                        tr "..."
                        mc "*Whispers* Just go. Don't push it. You're sitting next to me anyway."
                        la "*Whispers* Fine..."
            "Have a conversation with Gabi[KoGa3AutoWTChange1]{size=-4}(Gabi Suspicion+2) {/size} {/color}":
                $ Gabi_Suspicion += 2
                # Gabi_Suspicion = 2
                scene 14_245 with Dissolve(1)
                tr "..."
                scene 14_246 with Dissolve(1)
                mc "Cómo estás?\n(How are you?)"
                tr "Bien, gracias. Cómo estás tú?\n(I'm good, thank you? How are you?)"
                mc "Sí, estoy bien. Te ves hermosa!\n(Yeah, also good. You look beautiful!)"
                tr "Heh... Gracias!"
                scene 14_247 with Dissolve(1)
                mc "Qué estabas dibujando en la pizarra?\n(What were you drawing on the blackboard?)"
                tr "Por qué iba a estar dibujando algo?\n(Why would I be drawing something?)"
                mc "No lo sé. Tal vez es un pasatiempo o algo así?\n(I don't know. Maybe it's a hobby or something?)"
                tr "Estaba a punto de escribir el título de la lección de hoy.\n(I was about to write the title for today's lesson.)"
                scene 14_248 with Dissolve(1)
                mc "Te eché de menos durante las vacaciones de primavera.\n(I missed you during spring break.)"
                mc "Me alegré cuando te vi en el restaurante.\n(I was happy when I saw you at the restaurant.)"
                mc "No sabía que eras amiga de Ximena Vergara.\n(I didn't know you're friends with Ximena Vergara.)"
                mc "De qué se conocen?\n(How do you know each other?)"
                tr "Nos dijimos...\n(We said...)"
                scene 14_249 with Dissolve(1)
                ca "Gabi!!!"
                tr "It's Ms Ramirez!"
                ca "We missed you!"
                scene 14_250 with Dissolve(1)
                ca "Yo, [mc]. What's up?"
                mc "Hey, Callum."
                ca "Flirting with our Gabi, huh? Sneaky, sneaky!"
                tr "..."
                mc "Haha... Just trying to bump my grades a bit."
                scene 14_251 with Dissolve(1)
                ca "Didn't you ace every test so far?"
                mc "Uh... I wish!"
                ca "If it works, let me know your secret."
                mc "Heh..."
                mc "{i}(I need to be more careful.){/i}"
                if Layla_End == True:
                    pass
                else:
                    if Layla_Dating == False:
                        pass
                    else:
                        $ Gabi_Jealousy += 2
                        # Gabi_Jealousy = 2
                        scene 14_252 with Dissolve(1)
                        la "Here you are!"
                        mc "Hey."
                        la "I was looking for you in the hallways."
                        mc "If you'd showered with me, you wouldn't have had to!"
                        la "Haha."
                        scene 14_253 with Dissolve(1)
                        ""
                        scene 14_254 with Dissolve(1)
                        tr "..."
                        scene 14_255 with Dissolve(1)
                        tr "Can you get off my desk and go to your seats!"
                        mc "Yeah... Sorry."
    scene black with Dissolve(1)
    pause 2
    scene 14_260 with Dissolve(1)
    tr "Today, we're going to do something different."
    tr "I want to hear what you did during spring break."
    tr "One by one, you'll come to the front and talk about your past week. En español!"
    st "*Sigh* Seriously..."
    scene 14_261 with Dissolve(1)
    tr "I'll give you ten minutes to write something down before we start."
    tr "It doesn't have to be a full story. Just a few sentences will do."
    st "What if we didn't do anything? I just slept!"
    tr "Then that's what you'll say."
    mc "{i}(Well, looks like I've got a free ten minutes.){/i}"
    scene 14_262 with Dissolve(1)
    mc "..."
    mc "{i}(She doesn't look thrilled about this assignment.){/i}"
    mc "{i}(Should I help her?){/i}"
    menu:
        "Help Layla[KoGa3AutoWTChange1]{size=-4}(Layla Points+2, Layla Week6 Monday Spanish OfferHelp) {/size} {/color}":
            $ Layla_Points += 2
            # Layla (102)
            $ Layla_Week6_Monday_Spanish_OfferHelp = True
            if Layla_End == True:
                mc "{i}(If she lets me that is.){/i}"
                scene 14_263 with Dissolve(1)
                mc "*Whispers* Hey..."
                mc "*Whispers* Hey, Layla?"
                la "..."
                mc "*Whispers* Want some help?"
                la "*Whispers* No!"
                mc "{i}(I didn't expect her to say yes... At least I offered.){/i}"
            else:
                if Layla_Dating == False:
                    if Layla_Week5_Wednesday_BreakUp == True:
                        mc "{i}(If she lets me that is.){/i}"
                        scene 14_264 with Dissolve(1)
                        mc "*Whispers* Hey..."
                        mc "*Whispers* Hey, Layla?"
                        la "..."
                        mc "*Whispers* Need some help?"
                        scene 14_265 with Dissolve(1)
                        la "*Nods*"
                        mc "Uh..."
                        mc "{i}(Wasn't expecting her to say yes so quickly.){/i}"
                        mc "Alright, let's see."
                        scene 14_266 with Dissolve(1)
                        mc "{i}(Okay... She wrote... Sleep? Just sleep?){/i}"
                        mc "{i}(Seriously, Layla? She wants me to translate that?){/i}"
                        mc "{i}(I'd better add a little more to help her out.){/i}"
                        scene 14_267 with Dissolve(1)
                        mc "{i}(I know she went running in the park...){/i}"
                        mc "{i}(Probably hung out with friends too... maybe throw in a beach day for good measure?){/i}"
                        scene 14_268 with Dissolve(1)
                        la "..."
                        scene 14_269 with Dissolve(1)
                        mc "Here you go."
                        la "Thank you."
                        scene 14_270 with Dissolve(1)
                        mc "Can you read my handwriting?"
                        la "*Nods*"
                        mc "{i}(I hope this helps her.){/i}"
                    else:
                        scene 14_271 with Dissolve(1)
                        mc "*Whispers* Hey..."
                        mc "*Whispers* Hey, Layla?"
                        la "Mmm?"
                        mc "*Whispers* Need some help?"
                        scene 14_272 with Dissolve(1)
                        la "Yes, please!"
                        la "Here!"
                        mc "Haha, thanks..."
                        scene 14_266 with Dissolve(1)
                        mc "{i}(Let's see what she wro...){/i}"
                        mc "{i}(Sleep? Just sleep? Seriously, Layla...){/i}"
                        scene 14_273 with Dissolve(1)
                        mc "Really, Layla? Just sleep?"
                        la "*Shrugs*"
                        mc "I know you did more than just sleep!"
                        mc "Looks like we need some extra private lessons, huh?"
                        la "*Nods*"
                        scene 14_276 with Dissolve(1)
                        mc "{i}(Okay... What to write?){/i}"
                        mc "{i}(She went running in the park... Hung out with friends... Maybe a beach trip? Even if not, it sounds good.){/i}"
                        scene 14_278 with Dissolve(1)
                        mc "Here you go!"
                        la "Thank you so much, [mc]."
                        mc "You're welcome."
                        scene 14_279 with Dissolve(1)
                        mc "Can you read my handwriting?"
                        la "Mm-hmm, I can."
                        la "It's prettier than I thought."
                        mc "Haha. Thanks?"
                        scene 14_280 with Dissolve(1)
                        la "..."
                        mc "What?"
                        mc "Can't read it after all?"
                        scene 14_281 with Dissolve(1)
                        la "You didn't write anything inappropriate, right? I have a feeling you're making me say something different..."
                        mc "Haha, no. Don't worry."
                        mc "{i}(Damn... What a missed opportunity.){/i}"
                        mc "{i}(Should've slipped in a joke or something.){/i}"
                        mc "{i}(Next time for sure...){/i}"
                        scene 14_282 with Dissolve(1)
                        la "..."
                        mc "Haha. I swear I didn't!"
                        mc "{i}(She's hilarious sometimes.){/i}"
                else:
                    scene 14_271 with Dissolve(1)
                    mc "*Whispers* Hey..."
                    mc "*Whispers* Hey, Layla?"
                    la "Mmm?"
                    mc "*Whispers* Need some help?"
                    scene 14_272 with Dissolve(1)
                    la "Yes, please!"
                    la "Here!"
                    mc "Haha, thanks..."
                    scene 14_266 with Dissolve(1)
                    mc "{i}(Let's see what she wro...){/i}"
                    mc "{i}(Sleep? Just sleep? Seriously, Layla...){/i}"
                    scene 14_273 with Dissolve(1)
                    mc "Really, Layla? Just sleep?"
                    la "*Shrugs*"
                    mc "I know you did more than just sleep!"
                    mc "Looks like we need some extra private lessons, huh?"
                    la "*Nods*"
                    scene 14_274 with Dissolve(1)
                    mc "Oh..."
                    mc "*Whispers* Or did you mean sleep with me? Now I get it."
                    la "[mc]! Don't say that!"
                    mc "Haha."
                    scene 14_275 with Dissolve(1)
                    tr "Por favor, trabaja en silencio!\n(Please, work in silence!)"
                    mc "Sí, lo sentimos.\n(Yes, we're sorry.)"
                    scene 14_276 with Dissolve(1)
                    mc "{i}(Okay... What to write?){/i}"
                    mc "{i}(She went running in the park... Hung out with friends... Maybe a beach trip? Even if not, it sounds good.){/i}"
                    scene 14_277 with Dissolve(1)
                    la "..."
                    scene 14_278 with Dissolve(1)
                    mc "Here you go!"
                    la "Thank you so much, [mc]."
                    mc "You're welcome."
                    scene 14_279 with Dissolve(1)
                    mc "Can you read my handwriting?"
                    la "Mm-hmm, I can."
                    la "It's prettier than I thought."
                    mc "Haha. Thanks?"
                    scene 14_280 with Dissolve(1)
                    la "..."
                    mc "What?"
                    mc "Can't read it after all?"
                    scene 14_281 with Dissolve(1)
                    la "You didn't write anything inappropriate, right? I have a feeling you're making me say something different..."
                    mc "Haha, no. Don't worry."
                    mc "{i}(Damn... What a missed opportunity.){/i}"
                    mc "{i}(Should've slipped in a joke or something.){/i}"
                    mc "{i}(Next time for sure...){/i}"
                    scene 14_282 with Dissolve(1)
                    la "..."
                    mc "Haha. I swear I didn't!"
                    mc "{i}(She's hilarious sometimes.){/i}"
        "Let Layla do it on her own":
            mc "{i}(No... Maybe it's better to let her do it on her own.){/i}"
    scene black with Dissolve(1)
    pause 2
    scene 14_283 with Dissolve(1)
    tr "Alright. I think you've had enough time."
    tr "Who wants to go first?"
    st "Not me!"
    tr "..."
    tr "No one?"
    scene 14_284 with Dissolve(1)
    mc "{i}(I can go, so I'll be done with it.){/i}"
    mc "I will!"
    tr "Okay, [mc]. Come to the front."
    scene 14_285 with Dissolve(1)
    mc "{i}(It's been a while since I had to stand in front of a class and give a speech.){/i}"
    mc "{i}(Why am I so nervous about this? I'm just talking about what I did during spring break.){/i}"
    mc "{i}(And probably no one except Gabi will understand what I'm saying...){/i}"
    if Gabi_End == True:
        pass
    else:
        scene 14_286 with Dissolve(1)
        mc "..."
        mc "{i}(Or maybe it's because she's watching me so intensely that I'm nervous?){/i}"
        mc "{i}(She does look good...){/i}"
    scene 14_287 with Dissolve(1)
    mc "Bueno..."
    mc "Han ocurrido muchas cosas estas vacaciones.\n(A lot happened during spring break.)"
    scene black with Dissolve(1)
    pause 2
    scene 14_288 with Dissolve(1)
    mc "Y ya está.\n(That's about it.)"
    tr "Gracias, [mc]."
    st "What the fuck? Why are you even taking this class?"
    mc "Haha."
    if Gabi_End == True:
        pass
    else:
        scene 14_289 with Dissolve(1)
        tr "En serio? Por qué estás en esta clase?\n(Seriously? Why are you taking this class?)"
        mc "..."
        menu:
            "Easy credits":
                scene 14_290 with Dissolve(1)
                mc "Para sacar créditos fáciles!"
                tr "Heh..."
                tr "Siéntese!\n(Go sit down!)"
            "Gabi[KoGa3AutoWTChange1]{size=-4}(Gabi Suspicion+2) {/size} {/color}":
                $ Gabi_Suspicion += 2
                # Gabi_Suspicion = 4
                scene 14_291 with Dissolve(1)
                mc "Me gusta la profesora!"
                tr "..."
                st "Haha, I understand that! Me gusta too! Me gusta Gabriela!"
                scene 14_292 with Dissolve(1)
                tr "*Sigh...*"
                tr "Siéntese!\n(Go sit down!)"
    scene 14_293 with Dissolve(1)
    tr "Who's next?"
    st "No way I'm going after that!"
    st "Same here..."
    scene 14_294 with Dissolve(1)
    tr "The next person will get extra credit!"
    st "No extra credit will get me up there!"
    tr "No one? Then I'll just pick someone."
    tr "Callum! Please come to the front."
    ca "Damn..."
    scene 14_295 with Dissolve(1)
    tr "Vale, Callum..."
    tr "Por favor, cuéntenos qué hizo durante las vacaciones de primavera."
    ca "Qué?"
    tr "*Sigh* Please tell us what you did during spring break..."
    scene 14_296 with Dissolve(1)
    ca "Uh... Dormir!"
    st "Haha."
    tr "..."
    tr "Qué más?\n(What else?)"
    ca "Uh..."
    scene 14_297 with Dissolve(1)
    ca "Quizás fui a la playa, quizás no.\n(Maybe I went to the beach, maybe not.)"
    st "Hahaha..."
    mc "{i}(Why does he pronounce quizás as kiss-ass? Haha, that idiot...){/i}"
    tr "..."
    mc "{i}(I think she's regretting making us talk about our spring break.){/i}"
    if Gabi_End == True:
        mc "{i}(I'm happy I went first though...){/i}"
        jump Week6_Monday_Spanish_End
    else:
        jump Week6_Monday_Spanish_Gabi

label Week6_Monday_Spanish_Gabi:
    if _in_replay:
        $ Layla_Dating = True
        $ Layla_End = False
    scene 14_298 with Dissolve(1)
    mc "{i}(She looks cute when she's annoyed.){/i}"
    mc "{i}(I wouldn't mind her looking at me like that.){/i}"
    scene 14_299 with Dissolve(1)
    mc "..."
    if Layla_Dating == True:
        scene 14_300 with Dissolve(1)
        la "..."
    else:
        pass
    scene 14_301 with Dissolve(1)
    mc "{i}(Still can't believe that I had sex with her.){/i}"
    mc "{i}(Multiple times, by this point...){/i}"
    mc "{i}(And I want to again!){/i}"
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 14_302 at moveup
    pause 3
    mc "{i}(Maybe next time she'll wear that sexy lingerie again.){/i}"
    mc "{i}(She looked so fucking hot!){/i}"
    mc "{i}(Imagine having sex with her here at school. In this class...){/i}"
    mc "{i}(How would that go?){/i}"
    scene 14_303 with Dissolve(1)
    tr "What are you waiting for?"
    tr "Come here and claim your prize for best student!"
    scene 14_304 with Dissolve(1)
    tr "It's been way too long!"
    tr "Why didn't you come visit me during spring break?"
    mc "I..."
    tr "Don't say anything, just ravish me!"
    mc "{i}(I don't know if she would say ravish...){/i}"
    scene 14_305 with Dissolve(1)
    mc "{i}(First thing I would do is grab that ass though.){/i}"
    mc "{i}(Feel her soft skin and...){/i}"
    scene 14_306 with Dissolve(1)
    mc "{i}(Kiss her!){/i}"
    scene 14_307 with Dissolve(1)
    mc "{i}(Taste her all over.){/i}"
    scene 14_308 with Dissolve(1)
    mc "{i}(Then take a look at her amazing boobs!){/i}"
    scene 14_309 with Dissolve(1)
    mc "{i}(Yeah, I'd probably take off her bra immediately.){/i}"
    scene 14_310 with Dissolve(1)
    mc "{i}(And suck on her breasts.){/i}"
    scene 14_311 with Dissolve(1)
    mc "{i}(Feel her nipples getting hard in my mouth...){/i}"
    scene 14_312 with Dissolve(1)
    mc "{i}(While I draw circles around them with my tongue.){/i}"
    mc "{i}(Fuck... I'm so horny imagining all this.){/i}"
    mc "{i}(What next?){/i}"
    scene 14_313 with vpunch
    tr "Ahh..."
    mc "{i}(I'll probably push her up against the blackboard.){/i}"
    scene 14_314 with Dissolve(1)
    mc "{i}(Kiss her shoulders...){/i}"
    scene 14_315 with Dissolve(1)
    mc "{i}(Go lower until I...){/i}"
    scene 14_316 with Dissolve(1)
    mc "{i}(See this!){/i}"
    scene 14_317 with Dissolve(1)
    mc "{i}(There's no way I wouldn't put my mouth on it!){/i}"
    mc "{i}(Give her a little nibble.){/i}"
    scene 14_318 with Dissolve(1)
    tr "*Moans* Ah... [mc]..."
    mc "{i}(Listen to her cute moan...){/i}"
    scene 14_319 with Dissolve(1)
    mc "{i}(I'd lick her whole body...){/i}"
    scene 14_320 with Dissolve(1)
    mc "{i}(And press my head between her cheeks...){/i}"
    scene 14_321 with Dissolve(1)
    mc "{i}(Again, I probably won't be able to resist for long until I take off her panties.){/i}"
    scene 14_322 with Dissolve(1)
    mc "{i}(To see her already wet pussy...){/i}"
    scene 14_323 with Dissolve(1)
    tr "Mmm..."
    scene 14_324 with Dissolve(1)
    mc "{i}(Taste her sweet nectar...){/i}"
    mc "{i}(Who the fuck talks like that?){/i}"
    scene 14_325 with Dissolve(1)
    mc "{i}(Lick her fucking pussy, I mean!){/i}"
    scene 14_326 with Dissolve(1)
    mc "{i}(Her moans from back when I was at her apartment still ring in my head.){/i}"
    mc "{i}(I want to hear them again. Again. And again...){/i}"
    scene 14_327 with Dissolve(1)
    mc "{i}(What would you want me to do, Gabi?){/i}"
    scene 14_328 with Dissolve(1)
    mc "{i}(I want to fuck her so badly!){/i}"
    scene 14_329 with Dissolve(1)
    tr "..."
    scene 14_330 with Dissolve(1)
    mc "{i}(Feeling her warmth again.){/i}"
    scene 14_331 with Dissolve(1)
    tr "Ahh..."
    show 14_332
    mc "{i}(Shove my dick inside her and fuck her!){/i}"
    show 14_333
    ""
    show 14_334
    mc "{i}(Oh yeah! Take that, Gabi!){/i}"
    show 14_335
    mc "{i}(You like my cock inside you?){/i}"
    show 14_336
    ""
    scene 14_337 with Dissolve(1)
    mc "{i}(I'd fuck her so hard.){/i}"
    scene 14_338 with Dissolve(1)
    mc "Do you like this, Gabi?"
    mc "Want me to fuck you more?"
    tr "*Nods*"
    scene 14_339 with Dissolve(1)
    mc "I want to fuck you on your desk!"
    scene 14_340 with Dissolve(1)
    mc "Let's get rid of these..."
    scene 14_341 with vpunch
    tr "Aaah..."
    scene 14_342 with Dissolve(1)
    mc "I want you to say it!"
    tr "Fuck me."
    mc "Say it again!"
    tr "Fuck me, [mc]!"
    scene 14_343 with Dissolve(1)
    tr "*Moaning*"
    scene 14_344 with Dissolve(1)
    ""
    show 14_345
    ""
    show 14_346
    ""
    show 14_347
    ""
    scene 14_348 with vpunch
    pause 2
    scene 14_348 with vpunch
    mc "Fuck..."
    scene 14_349 with Dissolve(1)
    mc "{i}(Damn...){/i}"
    mc "{i}(That would be so hot.){/i}"
    if Layla_End == True:
        pass
    else:
        la "..."
    $ renpy.end_replay()
    jump Week6_Monday_Spanish_End

label Week6_Monday_Spanish_End:
    scene black with Dissolve(1)
    pause 2
    scene 14_350 with Dissolve(1)
    tr "Ahora le toca a Layla.\n(Okay... Next is Layla.)"
    tr "Por favor, pasa al frente.\n(Please, come to the front.)"
    la "..."
    scene 14_351 with Dissolve(1)
    mc "{i}(She looks so nervous.){/i}"
    if Layla_Week6_Monday_Spanish_OfferHelp == False:
        mc "{i}(Maybe I should've offered her my help.){/i}"
    else:
        if Layla_End == True:
            mc "{i}(I offered her to help her out, but she didn't want me to...){/i}"
        else:
            mc "{i}(Just read of off your paper and it will be fine.){/i}"
    scene 14_352 with Dissolve(1)
    tr "Muy bien, Layla."
    tr "Qué hiciste en las vacaciones de primavera?\n(What did you do during spring break?)"
    if Layla_End == True:
        scene 14_353 with Dissolve(1)
        la "Dormir..."
        tr "*Sigh*"
        mc "{i}(She just copied Callum?){/i}"
        scene 14_354 with Dissolve(1)
        tr "Y no hiciste nada más que dormir?\n(And did you maybe do something besides sleeping?)"
        la "Uh..."
        la "No?"
        tr "Saliste con tus amigos? Fuiste a una discoteca o a la playa?\n(Going out with your friends? To a club maybe? Or to the beach?)"
        la "No..."
        scene 14_355 with Dissolve(1)
        tr "*Sigh* Para qué estoy haciendo esto?\n(Why am I even doing this?)"
        tr "*Shakes head* Debería haber...\n(I should've just...)"
        mc "{i}(I feel a little bad for her.){/i}"
    else:
        if Layla_Week6_Monday_Spanish_OfferHelp == False:
            scene 14_353 with Dissolve(1)
            la "Dormir..."
            tr "*Sigh*"
            mc "{i}(Oh, Layla...){/i}"
            scene 14_354 with Dissolve(1)
            tr "Y no hiciste nada más que dormir?\n(And did you maybe do something besides sleeping?)"
            la "Uh..."
            la "No?"
            tr "Saliste con tus amigos? Fuiste a una discoteca o a la playa?\n(Going out with your friends? To a club maybe? Or to the beach?)"
            la "No..."
            scene 14_355 with Dissolve(1)
            tr "*Sigh* Para qué estoy haciendo esto?\n(Why am I even doing this?)"
            tr "*Shakes head* Debería haber...\n(I should've just...)"
            mc "{i}(I feel a little bad for her.){/i}"
        else:
            scene 14_356 with Dissolve(1)
            la "Uhm..."
            mc "{i}(Come on! You can do this.){/i}"
            scene 14_357 with Dissolve(1)
            la "En las vacaciones de primavera, entrené un poco en el parque.\n(During spring break, I did some training in the park.)"
            la "Salí con mis amigos, fuimos de compras y más cosas.\n(I hung out with my friends. We went shopping together and some other things.)"
            la "Y también me fui a la playa a relajarme.\n(I also went to the beach to relax.)"
            la "Y también hice mi tarea de español.\n(And I did my Spanish assignment.)"
            scene 14_358 with Dissolve(1)
            tr "Haha. Muy bien."
            tr "Parece que lo pasaste bien.\n(Looks like you had fun.)"
            la "Uh..."
            scene 14_359 with Dissolve(1)
            mc "*Nodding*"
            la "Uh... Sí!"
            tr "Buen trabajo. Gracias, Layla!\n(Well done. Thank you, Layla!)"
    if Layla_End == True:
        scene 14_362 with Dissolve(1)
        la "*Sigh*"
        mc "..."
    else:
        if Layla_Week6_Monday_Spanish_OfferHelp == False:
            scene 14_362 with Dissolve(1)
            la "*Sigh*"
            if Layla_Week5_Wednesday_BreakUp == True:
                mc "..."
            else:
                mc "Really, Layla? Sleep?"
                la "Leave me alone!"
                mc "Haha."
        else:
            if Layla_Week5_Wednesday_BreakUp == True:
                scene 14_360 with Dissolve(1)
                la "*Whispers* Thank you."
                mc "*Whispers* You're welcome!"
            else:
                scene 14_361 with Dissolve(1)
                la "*Whispers* Thank you."
                mc "*Whispers* You're welcome!"
    scene black with Dissolve(1)
    pause 2
    if Layla_End == True:
        scene 14_363 with Dissolve(1)
        ca "See you tomorrow, Gabi."
        tr "Señorita Ramírez!"
        if Gabi_End == True:
            jump Week6_Monday_Lunchbreak
        else:
            scene 14_364 with Dissolve(1)
            mc "Adiós, señorita Ramírez."
            tr "Heh... Adiós..."
            jump Week6_Monday_Lunchbreak
    else:
        if Layla_Week5_Wednesday_BreakUp == True:
            scene 14_363 with Dissolve(1)
            ca "See you tomorrow, Gabi."
            tr "Señorita Ramírez!"
            if Gabi_End == True:
                jump Week6_Monday_Lunchbreak
            else:
                scene 14_364 with Dissolve(1)
                mc "Adiós, señorita Ramírez."
                tr "Heh... Adiós..."
                jump Week6_Monday_Lunchbreak
        else:
            if Layla_Dating == False:
                scene 14_365 with Dissolve(1)
                ca "See you tomorrow, Gabi."
                tr "Señorita Ramírez!"
                scene 14_401 with Dissolve(1)
                la "*Sigh* Finally, this class is over!"
                mc "Haha. It wasn't that bad."
                mc "You just had to stand in front of the class for about a minute, then the rest of the time you could do whatever you wanted."
                la "Still..."
                scene 14_402 with Dissolve(1)
                la "What class do you have now?"
                mc "I need to check my schedule, but I think it's math."
                la "Ew..."
                mc "Haha."
                scene 14_403 with Dissolve(1)
                mc "And what class do you have?"
                la "English literature."
                mc "Oh... Mr Donovan..."
                la "Yes!"
                if Valeria_Week5_Friday_Date == False:
                    scene 14_404 with Dissolve(1)
                    mc "I still don't know who he is."
                    la "Want me to introduce you?"
                    mc "No, thanks..."
                    la "Haha."
                else:
                    scene 14_405 with Dissolve(1)
                    mc "I actually know who he is, now."
                    la "You do?"
                    mc "Yeah. I met him briefly at the beach last week."
                    la "He goes very often. He surfs."
                    mc "I saw that."
            else:
                scene 14_365 with Dissolve(1)
                ca "See you tomorrow, Gabi."
                tr "Señorita Ramírez!"
                if Gabi_End == True:
                    scene 14_401 with Dissolve(1)
                    la "*Sigh* Finally, this class is over!"
                    mc "Haha. It wasn't that bad."
                    mc "You just had to stand in front of the class for about a minute, then the rest of the time you could do whatever you wanted."
                    la "Still..."
                    scene 14_402 with Dissolve(1)
                    la "What class do you have now?"
                    mc "I need to check my schedule, but I think it's math."
                    la "Ew..."
                    mc "Haha."
                    scene 14_403 with Dissolve(1)
                    mc "And what class do you have?"
                    la "English literature."
                    mc "Oh... Mr Donovan..."
                    la "Yes!"
                    if Valeria_Week5_Friday_Date == False:
                        scene 14_404 with Dissolve(1)
                        mc "I still don't know who he is."
                        la "Want me to introduce you?"
                        mc "No, thanks..."
                        la "Haha."
                    else:
                        scene 14_405 with Dissolve(1)
                        mc "I actually know who he is, now."
                        la "You do?"
                        mc "Yeah. I met him briefly at the beach last week."
                        la "He goes very often. He surfs."
                        mc "I saw that."
                else:
                    scene 14_366 with Dissolve(1)
                    tr "..."
                    scene 14_367 with Dissolve(1)
                    tr "Hasta mañana, Layla, [mc]."
                    la "..."
                    mc "Adiós, señorita Ramírez."
                    if Gabi_Jealousy == 2:
                        scene 14_368 with Dissolve(1)
                        la "What class do you have now?"
                        mc "I need to check my schedule, but I think it's math."
                        la "Ew..."
                        mc "Haha."
                        scene 14_369 with Dissolve(1)
                        tr "*Shakes head*"
                        scene 14_370 with Dissolve(1)
                        tr "..."
                        scene 14_371 with Dissolve(1)
                        tr "[mc]!"
                        la "..."
                        mc "Uh... Yes?"
                        tr "Please stay for a minute. I need to ask you something."
                        mc "Okay?"
                        tr "And close the door!"
                        scene 14_372 with Dissolve(1)
                        mc "What's up?"
                        mc "{i}(Why is she looking so angry?){/i}"
                        mc "{i}(Did I do something?){/i}"
                        scene 14_373 with vpunch
                        mc "..."
                        mc "{i}(What is she...?){/i}"
                        scene 14_374 with Dissolve(1)
                        mc "{i}(Damn...){/i}"
                        mc "{i}(I imagined kissing her earlier but that didn't even come close to the real thing.){/i}"
                        mc "{i}(I missed these lips!){/i}"
                        scene 14_375 with Dissolve(1)
                        mc "..."
                        scene 14_376 with Dissolve(1)
                        mc "{i}(Was she jealous I grabbed Layla's butt?){/i}"
                        mc "{i}(If she wants me to grab hers, I'll gladly comply!){/i}"
                        scene 14_377 with Dissolve(1)
                        tr "Mmm..."
                        scene 14_378 with Dissolve(1)
                        ""
                        scene 14_379 with Dissolve(1)
                        tr "..."
                        scene 14_380 with vpunch
                        tr "*Whispers* Stop. Stop! We can't!"
                        mc "{i}(You were the one who told me to stay and started making out!){/i}"
                        mc "{i}(And now you...){/i}"
                        scene 14_381 with Dissolve(1)
                        tr "*Whispers* You should leave now."
                        mc "*Nods*"
                        mc "{i}(I kinda understand.){/i}"
                        mc "{i}(Even though I wanted to... It was crazy what we were doing here.){/i}"
                        scene 14_382 with Dissolve(1)
                        mc "..."
                        show 14_383
                        tr "Estúpido, estúpido, estúpido!"
                        scene 14_384 with Dissolve(1)
                        tr "{i}(Think Gabriela! Think!){/i}"
                        tr "{i}(Because I got jealous of a student, I'm risking everything?){/i}"
                        tr "{i}(What is wrong with me?){/i}"
                        tr "{i}(I need to stop this. I need to end this! Before...){/i}"
                        scene 14_385 with Dissolve(1)
                        ""
                        scene 14_386 with Dissolve(1)
                        mc "Hey!"
                        la "Finally!"
                        la "Why do you always have to stay longer?"
                        la "What did she want this time?"
                        scene 14_387 with Dissolve(1)
                        mc "Uh..."
                        la "Was it because you grabbed my ass?"
                        menu:
                            "Yes[KoGa3AutoWTChange1]{size=-4}(Gabi Jealousy+2) {/size} {/color}":
                                $ Gabi_Jealousy += 2
                                # Gabi_Jealousy = 4
                                scene 14_391 with Dissolve(1)
                                mc "Mm-hmm..."
                                mc "She said it was inappropriate in school."
                                la "..."
                                scene 14_392 with Dissolve(1)
                                la "Inappropriate? Heh..."
                                la "Next time slap my ass!"
                                mc "Haha."
                                mc "{i}(Can't believe she just said that!){/i}"
                                scene 14_393 with Dissolve(1)
                                mc "Do you want to see your mom that badly?"
                                la "What? No! Why?"
                                mc "Because that's where you... and me would be going if I slapped your ass."
                                la "I don't care!"
                                scene 14_394 with Dissolve(1)
                                mc "Okay then!"
                                la "..."
                                scene 14_395 with Dissolve(1)
                                mc "Regretting it already?"
                                la "*Shakes head*"
                                scene 14_396 with Dissolve(1)
                                ""
                                scene 14_397 with Dissolve(1)
                                tr "..."
                                scene 14_398 with Dissolve(1)
                                mc "Maybe let's wait until school is over to continue, before we actually do have to go see your mom."
                                la "*Nods*"
                            "Something else":
                                scene 14_388 with Dissolve(1)
                                mc "No, something else."
                                mc "She asked me again why I'm taking that class."
                                la "And what did you say?"
                                mc "Easy credits..."
                                scene 14_389 with Dissolve(1)
                                mc "And I wanted to be in one more class with you!"
                                la "You didn't even know I take Spanish!"
                                mc "Maybe I did!"
                                la "..."
                                la "Did you?"
                                scene 14_390 with Dissolve(1)
                                mc "That's a secret!"
                                la "..."
                                scene 14_399 with Dissolve(1)
                                mc "What class do you have now?"
                                la "English literature."
                                mc "Oh... Mr Donovan..."
                                la "Yes!"
                                scene 14_400 with Dissolve(1)
                                mc "I still don't know who he is."
                                la "Want me to introduce you?"
                                mc "No, thanks..."
                                la "Haha."
                    else:
                        scene 14_401 with Dissolve(1)
                        la "*Sigh* Finally, this class is over!"
                        mc "Haha. It wasn't that bad."
                        mc "You just had to stand in front of the class for about a minute, then the rest of the time you could do whatever you wanted."
                        la "Still..."
                        scene 14_402 with Dissolve(1)
                        la "What class do you have now?"
                        mc "I need to check my schedule, but I think math."
                        la "Ew..."
                        mc "Haha."
                        scene 14_403 with Dissolve(1)
                        mc "And what class do you have?"
                        la "English literature."
                        mc "Oh... Mr Donovan..."
                        la "Yes!"
                        scene 14_404 with Dissolve(1)
                        mc "I still don't know who he is."
                        la "Want me to introduce you?"
                        mc "No, thanks..."
                        la "Haha."
        scene 14_406 with Dissolve(1)
        mc "Alright, I've gotta go this way."
        la "Look at you. Finally figuring out your way around school!"
        mc "About time, right? I might have secretly practiced during spring break."
        la "Haha."
        mc "Anyway... Catch you at lunch?"
        la "Mm-hmm. Catch me!"
        if Layla_Dating == False:
            pass
        else:
            scene 14_407 with Dissolve(1)
            ""
        scene 14_408 with Dissolve(1)
        mc "Idiot!"
        la "Haha."
        mc "Later, Layla!"
        la "Bye..."
        jump Week6_Monday_Lunchbreak

label Week6_Monday_Lunchbreak:
    scene black with Dissolve(2)
    pause 2
    if Layla_End == True:
        scene 14_409 with Dissolve(1)
        mc "*Sigh*"
        mc "{i}(I was actually looking forward to being back at school, but...){/i}"
        mc "{i}(I can't believe that talking to Darryl has been the highlight of my day so far.){/i}"
        scene 14_410 with Dissolve(1)
        x "I told you, it's him."
        x "Yeah, you're right."
        mc "..."
        scene 14_411 with Dissolve(1)
        x "I think he's on the track team."
        mc "{i}(What's going on?){/i}"
        mc "{i}(That's the second group of girls who... I don't know why they're talking about me...){/i}"
        mc "{i}(Weird.){/i}"
        scene 14_412 with Dissolve(1)
        mc "{i}(And there's Layla and Elena.){/i}"
        mc "{i}(Maybe they know what's going on?){/i}"
        scene 14_413 with Dissolve(1)
        mc "{i}(Doesn't seem like it.){/i}"
        scene 14_414 with Dissolve(1)
        mc "{i}(Oh...){/i}"
        mc "{i}(Or maybe they do?){/i}"
        mc "{i}(Maybe sitting here wasn't the smartest choice.){/i}"
        mc "{i}(At least their faces don't say 'I want to punch this guy' anymore.){/i}"
    else:
        if Layla_Week5_Wednesday_BreakUp == True:
            scene 14_409 with Dissolve(1)
            mc "*Sigh*"
            mc "{i}(I was actually looking forward to being back at school, but...){/i}"
            mc "{i}(I can't believe that talking to Darryl has been the highlight of my day so far.){/i}"
            scene 14_410 with Dissolve(1)
            x "I told you, it's him."
            x "Yeah, you're right."
            mc "..."
            scene 14_411 with Dissolve(1)
            x "I think he's on the track team."
            mc "{i}(What's going on?){/i}"
            mc "{i}(That's the second group of girls who... I don't know why they're talking about me...){/i}"
            mc "{i}(Weird.){/i}"
            scene 14_412 with Dissolve(1)
            mc "{i}(And there's Layla and Elena.){/i}"
            mc "{i}(Maybe they know what's going on?){/i}"
            scene 14_415 with Dissolve(1)
            mc "{i}(I could ask Elena later.){/i}"
            mc "{i}(If she still wants to talk, that is.){/i}"
            el "..."
            scene 14_414 with Dissolve(1)
            mc "{i}(Maybe sitting here wasn't the smartest choice.){/i}"
            mc "{i}(I'd better finish this quickly and find somewhere else to sit... Outside or something.){/i}"
        else:
            if Layla_Dating == False:
                scene 14_416 with Dissolve(1)
                ""
                scene 14_417 with Dissolve(1)
                x "I told you, it's him."
                x "Yeah, you're right."
                mc "..."
                scene 14_418 with Dissolve(1)
                x "I think he's on the track team."
                mc "{i}(What's going on?){/i}"
                mc "{i}(That's the second group of girls who... I don't know why they're talking about me...){/i}"
                mc "{i}(Weird.){/i}"
                scene 14_419 with Dissolve(1)
                el "Look at that!"
                el "Lonely boy sitting at our table again."
                scene 14_420 with Dissolve(1)
                mc "I can move if you want."
                la "No!"
                el "If you still don't know I'm joking, you're hopeless..."
                mc "Yeah, yeah, I know."
            else:
                if Elena_LikeMC == True:
                    $ LayLena = True
                    scene 14_416 with Dissolve(1)
                    ""
                    scene 14_417 with Dissolve(1)
                    x "I told you, it's him."
                    x "Yeah, you're right."
                    mc "..."
                    scene 14_418 with Dissolve(1)
                    x "I think he's on the track team."
                    mc "{i}(What's going on?){/i}"
                    mc "{i}(That's the second group of girls who... I don't know why they're talking about me...){/i}"
                    mc "{i}(Weird.){/i}"
                    scene 14_423 with Dissolve(1)
                    mc "Hey!"
                    la "Hey..."
                    scene 14_424 with Dissolve(1)
                    la "*Sigh...*"
                    mc "You okay? What's wrong?"
                    la "*Shrugs*"
                    scene 14_425 with Dissolve(1)
                    mc "Where's Elena?"
                    la "I don't know."
                    la "Feels like she's avoiding and ignoring me since this morning."
                    mc "What?"
                    scene 14_426 with Dissolve(1)
                    mc "Why?"
                    la "No idea."
                    mc "Did you two have a fight?"
                    la "No..."
                    scene 14_427 with Dissolve(1)
                    mc "..."
                    scene 14_428 with Dissolve(1)
                    mc "{i}(There she is.){/i}"
                    mc "{i}(Why's she sitting over there?){/i}"
                    mc "{i}(Did nothing really happen?){/i}"
                    scene 14_429 with Dissolve(1)
                    mc "Hey, uhm..."
                    mc "I'll be right back, okay?"
                    la "Mm-hmm..."
                    scene 14_430 with Dissolve(1)
                    mc "Hey, Elena."
                    el "Hey."
                    scene 14_431 with Dissolve(1)
                    mc "Can I sit next to you?"
                    el "Sure."
                    scene 14_432 with Dissolve(1)
                    mc "..."
                    el "..."
                    scene 14_433 with Dissolve(1)
                    mc "So..."
                    mc "What's going on? Why aren't you with us?"
                    el "Uhm..."
                    mc "Did you and Layla have a fight?"
                    scene 14_434 with Dissolve(1)
                    el "What?"
                    el "No!"
                    el "I just... I just thought I'd give you guys some space."
                    scene 14_435 with Dissolve(1)
                    mc "Just because Layla and I are together doesn't mean we don't want you around."
                    mc "If we wanted alone time, we have plenty of that after school."
                    mc "Even during school, if we want some alone time, we'll tell you."
                    mc "But honestly? That's never gonna happen."
                    scene 14_436 with Dissolve(1)
                    mc "We like to have you around."
                    mc "I like to have you around!"
                    el "..."
                    scene 14_437 with Dissolve(1)
                    mc "You two come first! I'm the one who messes up the dynamic."
                    mc "It's always been Layla and Elena!"
                    mc "Laylena!"
                    scene 14_438 with Dissolve(1)
                    el "Dios mío..."
                    mc "Haha. There she is!"
                    scene 14_439 with Dissolve(1)
                    el "..."
                    scene 14_440 with Dissolve(1)
                    mc "Now, come on!"
                    el "Later... Okay? I just..."
                    mc "*Sigh* Okay..."
                    scene 14_441 with Dissolve(1)
                    el "AAAH..."
                    la "..."
                    scene 14_442 with Dissolve(1)
                    mc "You didn't think I was just gonna leave, did you?"
                    el "[mc]!"
                    st "*Whistles*"
                    mc "Let's go!"
                    scene 14_443 with Dissolve(1)
                    mc "Here you go, Layla!"
                    mc "This is what you ordered, right? One pretty Latina!"
                    la "Haha, yes!"
                    el "You'd better put me down, [mc]!"
                    scene 14_444 with vpunch
                    mc "*Slap* But be careful! This one's spicy!"
                    el "Aaah!"
                    scene 14_445 with Dissolve(1)
                    el "You're so dead, Prosciutto!"
                    la "Haha."
                    scene 14_446 with Dissolve(1)
                    mc "Hey, don't look so mad."
                    mc "I'm sorry, alright?"
                    el "..."
                    scene 14_447 with Dissolve(1)
                    mc "Here, have a bite! Peace offering."
                    el "Cabrón!"
                    mc "Haha."
                else:
                    scene 14_416 with Dissolve(1)
                    ""
                    scene 14_417 with Dissolve(1)
                    x "I told you, it's him."
                    x "Yeah, you're right."
                    mc "..."
                    scene 14_418 with Dissolve(1)
                    x "I think he's on the track team."
                    mc "{i}(What's going on?){/i}"
                    mc "{i}(That's the second group of girls who... I don't know why they're talking about me...){/i}"
                    mc "{i}(Weird.){/i}"
                    scene 14_419 with Dissolve(1)
                    el "Look at that!"
                    el "Lonely boy sitting at our table again."
                    la "Hey!"
                    mc "What can I say? I miss you, Elena."
                    scene 14_421 with Dissolve(1)
                    el "Layla, this has gone on long enough. Please, break up with [mc] already!"
                    la "What? No way!"
                    scene 14_422 with Dissolve(1)
                    mc "Wait, why do you want us to break up?"
                    mc "So you can finally have me all to yourself?"
                    el "Dios mío... He's delirious too."
                    mc "Haha."
            scene 14_448 with Dissolve(1)
            mc "Anyway. I've got a question."
            mc "Do you have any idea what's been going on with me today?"
            el "Today? I've been wondering the same thing since day one."
            mc "Haha. Fair enough."
            la "What do you mean?"
            scene 14_449 with Dissolve(1)
            mc "Several times today, groups of people have walked by and said stuff like, 'Hey, I think it's him', or 'Should we ask him?'"
            mc "But I have no clue what they're talking about."
            mc "Do either of you know?"
            la "Hmm..."
            if MC_Bike == True:
                scene 14_452 with Dissolve(1)
                la "Maybe it's because they saw you arrive on your bike?"
                mc "Oh, that makes sense! I didn't even think of that."
                scene 14_453 with Dissolve(1)
                el "Right. You got a bike now, huh?"
                mc "Mm-hmm."
                el "Well, it was nice knowing you!"
                mc "What's that supposed to mean?"
                scene 14_454 with Dissolve(1)
                el "As reckless as you are, you're probably going to crash that thing. And die..."
                mc "Wow... Elena, way to be supportive."
                mc "This is what I get after not seeing you for a while?"
                el "That's exactly the reason!"
                mc "Haha. I actually missed your snarky comments."
                scene 14_455 with Dissolve(1)
                mc "But seriously, I'm a good rider... Just saying."
                la "Still. Be careful!"
                mc "I will."
                scene 14_456 with Dissolve(1)
                mc "Have either of you ever ridden a bike?"
                el "*Shakes head*"
                la "Nope."
                mc "No? Well if you ever..."
                el "No!"
                scene 14_457 with Dissolve(1)
                mc "If you change your..."
                el "No!"
                mc "Haha. Not a fan, huh?"
            else:
                scene 14_450 with Dissolve(1)
                la "No, I have no clue either."
                la "What about you, Elena?"
                el "*Shakes head*"
                la "Do you know who they are?"
                mc "Not really, but I think some might be on the cheer squad."
                scene 14_451 with Dissolve(1)
                el "I can ask around later, if you want."
                mc "Yeah? Thanks."
                mc "I really want to figure out what's going on. It feels kinda weird."
            scene black with Dissolve(1)
            pause 2
            scene 14_458 with Dissolve(1)
            mc "Are you going to eat, or just watch me?"
            la "Not hungry yet."
            el "Same here. I had an apple after cheer practice."
            mc "*Shakes head*"
            scene 14_459 with Dissolve(1)
            la "Oh, by the way. Have you heard anything about Valeria?"
            mc "No. You?"
            la "Nothing so far. I'm going to ask Coach before class, or maybe Mom. She might know why Valeria's not here today."
            mc "Mm-hmm."
            scene 14_460 with Dissolve(1)
            la "I haven't seen Zach either, today."
            la "Is he even here? He usually sits with you...?"
            mc "{i}(That won't be happening again. Honestly, I'm fine if I don't see that guy.){/i}"
            mc "No idea."
            if Alexis_Dating == True:
                $ Week6_Monday_BBQ_Invitation = True
                scene 14_461 with Dissolve(1)
                la "Oh, before I forget..."
                la "Lex will call you later, but Mom wanted me to let you know now."
                la "It's about the barbecue."
                scene 14_462 with Dissolve(1)
                la "I hope you can make it, because it's happening tomorrow."
                mc "Tomorrow?"
                mc "I thought it'd be over the weekend or something."
                la "It was planned for Friday at first, but Mom knew about the possible relay tournament, so they moved it to tomorrow."
                scene 14_463 with Dissolve(1)
                la "It'll be from six to around nine or ten. Is that okay?"
                mc "Yeah, I don't have anything planned."
                la "Great. Like I said, Lex will call you later about it."
                la "Oh! One more thing. Since we have school the next day, no drinking. Mom said one beer, max."
                mc "That's fine."
                scene 14_464 with Dissolve(1)
                la "You're also invited, Elena."
                el "Thanks, but..."
                la "No... No buts..."
                el "Sorry. I can't tomorrow. I have to look after Diego and Mateo."
                la "*Sigh*"
                scene 14_472 with Dissolve(1)
                mc "Is anyone else coming?"
                la "I'm not sure if Mom or Dad invited anyone else."
                la "Lex asked Erynn, but I don't know if she's coming."
                la "So, for now, it's just you and your da... I mean, Santiago."
                mc "Okay."
            else:
                if Layla_Dating == True:
                    $ Week6_Monday_BBQ_Invitation = True
                    scene 14_461 with Dissolve(1)
                    la "Oh, before I forget..."
                    mc "Hmm?"
                    la "It's about the barbecue."
                    scene 14_462 with Dissolve(1)
                    la "I hope you can make it, because it's happening tomorrow."
                    mc "Tomorrow?"
                    mc "I thought it'd be over the weekend or something."
                    la "It was planned for Friday at first, but Mom knew about the possible relay tournament, so they moved it to tomorrow."
                    scene 14_463 with Dissolve(1)
                    la "It'll be from six to around nine or ten. Is that okay?"
                    mc "Uhm, yeah. It's not that I have anything planned for tomorrow evening."
                    la "Great. I'll let Mom know."
                    la "Oh! One more thing. Since we have school the next day, no drinking. Mom said one beer, max."
                    mc "That's fine."
                    scene 14_464 with Dissolve(1)
                    la "You're also invited, Elena."
                    el "Thanks, but..."
                    la "No... No buts..."
                    el "Sorry. I can't tomorrow. I have to look after Diego and Mateo."
                    la "*Sigh*"
                    scene 14_465 with Dissolve(1)
                    mc "I guess we'll have to throw another hot tub party sometime, instead."
                    la "Yes! Let's do that!"
                    if Week6_Monday_Relay_PickLayla == False:
                        la "Maybe Saturday after the relay? Depending on when you, and maybe I, get back? Or Sunday? Are you free then?"
                    else:
                        la "Maybe Saturday after the relay? Depending on when we get back? Or Sunday? Are you free then?"
                    el "I think so, yes."
                    la "Yay!"
                    scene 14_466 with Dissolve(1)
                    la "But no spicy chicken!"
                    mc "Haha, you don't have to eat them!"
                    mc "Though, it was pretty funny."
                    la "It wasn't! I almost died!"
                    mc "Haha."
                    scene 14_467 with Dissolve(1)
                    mc "{i}(Now I can't wait for the weekend.){/i}"
                    mc "{i}(I might even be more excited about that than the relay.){/i}"
                    mc "{i}(Imagine if we actually continue what we...){/i}"
                    if Elena_LikeMC == True:
                        scene 14_468 with Dissolve(1)
                        mc "{i}(Fuck...){/i}"
                    else:
                        scene 11_1081 with Dissolve(1)
                        mc "{i}(Fuck...){/i}"
                    scene 14_472 with Dissolve(1)
                    mc "Is anyone else coming to the barbecue?"
                    la "I don't know if Mom or Dad invited anyone else."
                    la "I know Lex asked Erynn, but I'm not sure if she'll come."
                    if Erynn_End == True:
                        mc "{i}(I'm not sure it's a good idea having both Erynn and me there...){/i}"
                    else:
                        pass
                    la "So for now, it's just you and your da... I mean Santiago."
                    mc "Okay."
                    if Erynn_End == True:
                        mc "{i}(I just hope it stays that way!){/i}"
                    else:
                        pass
                else:
                    pass
            scene 14_469 with Dissolve(1)
            ""
            scene black with Dissolve(1)
            pause 2
            scene 14_470 with Dissolve(1)
            mc "Nggh..."
            mc "Next up is geography, right?"
            el "Yeah."
            mc "I'm gonna hit the bathroom before class starts."
            scene 14_471 with Dissolve(1)
            mc "See you in class."
            la "See you later."
            el "Bye."
            if LayLena == True:
                scene 14_473 with Dissolve(1)
                la "Hey... Why were you avoiding me earlier?"
                el "Uh..."
                el "I wasn't avoiding you. Sorry if it felt that way. I just thought you two might want some space."
                el "I'm always around, and I didn't want to crowd you."
                scene 14_474 with Dissolve(1)
                la "..."
                el "..."
                scene 14_475 with Dissolve(1)
                la "Okay, now tell me the real reason!"
                el "Layla..."
            else:
                pass
    jump Week6_Monday_Hallway_Valeria

label Week6_Monday_Hallway_Valeria:
    scene black with Dissolve(1)
    pause 2
    scene 14_476 with Dissolve(1)
    ""
    scene 14_477 with Dissolve(1)
    mc "..."
    if Layla_End == True:
        scene 14_479 with Dissolve(1)
        mc "Hey, Valeria."
        va "Hi."
        mc "We were wondering where you'd been."
        va "I had an appointment."
        mc "Oh... Gotcha."
        scene 14_480 with Dissolve(1)
        mc "Did you hear about the relay?"
        va "I did."
        mc "Should be fun."
        va "Mm-hmm."
        scene 14_481 with Dissolve(1)
        z "..."
        scene 14_482 with Dissolve(1)
        mc "Well... I'm gonna head to the bathroom. See you in class, I guess."
        va "Yeah. See you."
    else:
        if Valeria_LikeMC == False:
            scene 14_483 with Dissolve(1)
            mc "Val! Hey!"
            va "Hi."
            scene 14_484 with Dissolve(1)
            mc "We were wondering where you've been."
            mc "Did something happen? Are you okay?"
            va "Yeah, I just had an appointment this morning."
            scene 14_485 with Dissolve(1)
            mc "Ah, okay."
            mc "We were worried. Tried calling you but it always went straight to voicemail."
            va "Sorry about that. I dropped and broke my phone. I'll get a new one later today."
            scene 14_486 with Dissolve(1)
            mc "Well, that's good news. Not about the phone, but that nothing worse happened."
            va "Haha, got it."
            if Valeria_Week5_Friday_Date == True:
                scene 14_491 with Dissolve(1)
                mc "Also, I'm sorry about Friday. The way I left... and handled things wasn't great."
                mc "I shouldn't have... I'm really sorry, Val."
                va "Honestly, I've already moved past it. Let's just forget about it."
                va "Strictly friends, yeah?"
                mc "Thanks."
            else:
                pass
            scene 14_487 with Dissolve(1)
            mc "By the way... You missed an interesting training this morning."
            mc "There was an announcement, too."
            va "The relay?"
            mc "Oh... You already know?"
            va "Mm-hmm."
            scene 14_488 with Dissolve(1)
            mc "How'd you find out? Coach tell you?"
            va "No. I've got my connections."
            mc "Hmm... Connections..."
            mc "Do you know who's going?"
            scene 14_489 with Dissolve(1)
            va "You, Darryl, and me."
            mc "{i}(So that was decided before today.){/i}"
            va "I don't know who the second girl will be."
            if Week6_Monday_Relay_PickLayla == True:
                mc "Layla."
                scene 14_490 with Dissolve(1)
                va "Layla? That's awesome."
                va "She must be so happy."
                mc "She is!"
                scene 14_492 with Dissolve(1)
                va "Did Coach announce it already?"
                mc "Nope."
                va "Then how do you know?"
                mc "Connections!"
                va "Haha. I see, I see."
            else:
                mc "Tori."
                scene 14_491 with Dissolve(1)
                va "Tori? Okay."
                va "What did Layla say? She must've been upset."
                mc "She doesn't know yet."
                va "How do you know?"
                scene 14_492 with Dissolve(1)
                mc "Connections!"
                va "Haha. I see, I see."
            scene 14_493 with Dissolve(1)
            mc "Either way, it'll be fun."
            va "Mm-hmm. I think so, too."
            scene 14_481 with Dissolve(1)
            z "..."
            scene 14_494 with Dissolve(1)
            mc "Anyway. I need to hit the bathroom before class starts."
            va "Alright. See you there."
            va "I mean in class, not the bathroom!"
            mc "Haha, stop copying me!"
            va "Haha."
        else:
            $ Valeria_Week6_Monday_EmoDate = True
            scene black with Dissolve(1)
            transform moveup:
                xalign 0.5 yalign 1.0
                linear 5.0 yalign 0.0
            show 14_478 at moveup
            pause 3
            mc "Val!"
            scene 14_495 with Dissolve(1)
            va "Uh..."
            mc "Hey."
            va "Hi. How are you?"
            scene 14_496 with Dissolve(1)
            mc "We were worried about you. I was worried!"
            mc "No one knew where you were."
            mc "I tried calling you all weekend, today... Even Layla called a bunch of times, but it just went straight to voicemail."
            mc "Are you okay? Did something happen?"
            scene 14_497 with Dissolve(1)
            va "..."
            scene 14_498 with Dissolve(1)
            va "No, nothing serious."
            va "I dropped and broke my phone, so I couldn't answer. I'm planning to get a new one today."
            va "Plus, I had an appointment this morning, which is why I wasn't here."
            va "Sorry if I worried you."
            mc "Don't be sorry. I'm just glad you're okay and here now."
            scene 14_499 with Dissolve(1)
            mc "{i}(Why is this girl so damn cute...?){/i}"
            if Valeria_Week5_Thursday_CancelDate == True:
                scene 14_500 with Dissolve(1)
                mc "Hey, I'm really sorry about Friday. Cancelling our beach date was rough."
                va "It's okay. Honestly, I was a little mad. I was really looking forward to it."
                mc "Me too. I'll make it up to you. Promise."
                va "Okay..."
                scene 14_501 with Dissolve(1)
                ""
            else:
                scene 14_502 with Dissolve(1)
                va "Aah..."
                mc "I'm just happy to see you!"
                va "Haha."
                scene 14_503 with Dissolve(1)
                mc "Here I go again. Picking you up..."
                va "I told you, I'm cool with it."
                scene 14_504 with Dissolve(1)
                ""
            scene 14_505 with Dissolve(1)
            z "..."
            scene 14_506 with Dissolve(1)
            mc "By the way... You missed an interesting training this morning."
            mc "There was also an announcement."
            va "The relay?"
            mc "Oh... You already heard?"
            va "Mm-hmm."
            scene 14_507 with Dissolve(1)
            mc "How? Did Coach tell you?"
            va "No. I've got have my connections."
            mc "Hmm... Connections..."
            mc "Do you know who's going?"
            scene 14_508 with Dissolve(1)
            va "You, Darryl, and me."
            mc "{i}(So that was decided before today.){/i}"
            va "I don't know who the second girl will be, though."
            if Week6_Monday_Relay_PickLayla == True:
                mc "Layla."
                scene 14_490 with Dissolve(1)
                va "Layla? That's awesome."
                va "She must be so happy."
                mc "She is!"
                scene 14_492 with Dissolve(1)
                va "Did Coach announce it already?"
                mc "Nope."
                va "Then how do you know?"
                mc "Connections!"
                va "Haha. I see, I see."
            else:
                mc "Tori."
                scene 14_491 with Dissolve(1)
                va "Tori? Okay."
                va "What did Layla say? She must've been upset."
                mc "She doesn't know yet."
                va "How do you know?"
                scene 14_492 with Dissolve(1)
                mc "Connections!"
                va "Haha. I see, I see."
            scene 14_512 with Dissolve(1)
            mc "Either way, it's going to be fun."
            va "Mm-hmm. I think so too."
            scene 14_513 with Dissolve(1)
            mc "You mentioned wanting to go somewhere this week, right?"
            mc "What was that hint you gave me? Something emotional?"
            va "That's right."
            scene 14_514 with Dissolve(1)
            mc "You didn't want to tell me last week, but I guessed maybe watching a sad movie. Was I close?"
            va "*Shakes head*"
            mc "No?"
            mc "Hmm... Not a movie..."
            scene 14_515 with Dissolve(1)
            mc "Come on, tell me."
            va "Guess again, first."
            mc "Fine. Something emotional... Emotional... Was I close with the movie guess?"
            va "Not really."
            scene 14_516 with Dissolve(1)
            mc "It's not something like a graveyard visit, right?"
            va "Haha, no."
            va "Well..."
            mc "What?"
            va "Just kidding."
            scene 14_517 with Dissolve(1)
            mc "*Sigh*"
            mc "Honestly, I'm stumped."
            va "Stumped?"
            va "Alright, I'll just tell you. You probably wouldn't have guessed, anyway."
            scene 14_518 with Dissolve(1)
            va "An emo party."
            mc "Emo party?"
            mc "You mean the music? Like MCR? And the people with the bangs over their eyes?"
            va "Mm-hmm. Exactly."
            mc "Emo... Okay, now I see where the 'emotional' hint came from. You were right. No way I'd have guessed."
            scene 14_519 with Dissolve(1)
            va "So, are you in?"
            mc "Uhm... Yeah, I guess?"
            va "Haha."
            va "But you have to dress the part."
            mc "Only if you do, too."
            va "I will."
            scene 14_520 with Dissolve(1)
            mc "Looks like I need to do some shopping. I don't have much 'emo' stuff besides a couple of black tees... This is going to be so weird."
            va "Haha, definitely."
            mc "When is it? We have the relay this weekend."
            va "Tomorrow night, seven to nine. Yeah, it's kinda last minute. I wanted to tell you earlier, but then my phone broke and..."
            mc "I'm cool with last minute. I booked a flight a day before leaving for Alvarado last week. No big deal."
            scene 14_521 with Dissolve(1)
            va "Cool. I'll text you the details once I have my new phone."
            mc "Sounds good."
            if Alexis_Dating == True:
                $ AlexisValeria = True
                scene 14_522 with Dissolve(1)
                mc "{i}(No, wait!){/i}"
                mc "{i}(The barbecue is tomorrow...){/i}"
                mc "{i}(Fuck!){/i}"
                mc "{i}(I really don't want to cancel, either. What do I do? I already agreed...){/i}"
                scene 14_523 with Dissolve(1)
                va "What's wrong?"
                mc "Ah, nothing. Just... I need to go to the bathroom."
                va "Then what are you waiting for? Go!"
                scene 14_524 with Dissolve(1)
                mc "See you in class."
                va "Yeah. Good luck!"
                mc "Haha. Good luck..."
                scene 14_525 with Dissolve(1)
                mc "{i}(Why does this always happen to me...?){/i}"
                mc "{i}(I have to make a decision. Like right now!){/i}"
                mc "{i}(But who do I choose...? This is impossible.){/i}"
                if Valeria_Week5_Thursday_CancelDate == True:
                    mc "{i}(If I cancel on Valeria again, that's it. She'll never want to hang out with me.){/i}"
                    mc "{i}(And I can't cancel on a whole family... FUCK!){/i}"
                else:
                    pass
            else:
                mc "I have so many questions now. But I'll save them for tomorrow."
                mc "Right now, I really need to go to the bathroom."
                va "Haha, then go already!"
                scene 14_524 with Dissolve(1)
                mc "See you in class."
                va "Mm-hmm. Good luck!"
                mc "Haha. Good luck..."
                scene 14_526 with Dissolve(1)
                va "..."
                mc "..."
                scene 14_527 with Dissolve(1)
                mc "What?"
                va "Just realised you cut your hair."
                mc "We've been talking for a couple minutes and now you notice?"
                va "Sorry..."
                scene 14_528 with Dissolve(1)
                mc "So, do you like it?"
                va "..."
                va "Nope!"
                scene 14_529 with Dissolve(1)
                mc "No?"
                mc "Wait! What?"
                scene 14_530 with Dissolve(1)
                mc "Heh..."
                mc "You asshole!"
                scene 14_531 with Dissolve(1)
                va "Haha."
                mc "You know what?"
                va "What?"
                scene 14_532 with Dissolve(1)
                mc "Moist-moist-moist-moist-moist!"
                scene 14_533 with Dissolve(1)
                va "Nooo!"
                mc "Haha."
                mc "Moist-moist-moist..."
                va "Stop..."
                mc "That's what you get!"
    scene black with Dissolve(1)
    pause 2
    scene 14_534 with Dissolve(1)
    mc "{i}(Oh...){/i}"
    mc "{i}(Isn't that Daniela? Gabi's sister?){/i}"
    scene 14_535 with Dissolve(1)
    mc "Hey, Dani."
    dr "..."
    dr "Hey?"
    mc "Geography now, huh?"
    dr "Uh, yeah..."
    scene 14_536 with Dissolve(1)
    mc "{i}(Okay... That was a little awkward.){/i}"
    mc "{i}(I've never even spoken to her before, and now I'm calling her Dani like we're friends... Smooth.){/i}"
    mc "{i}(But now that I know she's Gabi's sister, I can definitely see the resemblance.){/i}"
    mc "{i}(Well, except for the eyes...){/i}"
    scene 14_537 with Dissolve(1)
    mc "*Sigh*..."
    mc "{i}(I shouldn't have taken geography...){/i}"
    scene 14_538 with Dissolve(1)
    stop music fadeout 1.0
    play music ("Music/Battle_Rock2.mp3", "Music/Battle_Rock2.mp3") volume 0.5
    z "Hey!"
    mc "..."
    scene 14_539 with Dissolve(1)
    z "Yo! What's up?"
    z "I've been looking for you all day."
    z "How've you been?"
    scene 14_540 with Dissolve(1)
    mc "..."
    z "..."
    scene 14_541 with Dissolve(1)
    z "Hey! Wait up!"
    mc "Don't touch me!"
    z "Whoa, what's wrong?"
    scene 14_542 with Dissolve(1)
    mc "'What's wrong?' Really...?"
    mc "Did you already forget what happened before spring break?"
    z "What are you talking about?"
    mc "..."
    scene 14_543 with Dissolve(1)
    mc "You sucker-punched me!"
    z "Oh... That..."
    z "I was gonna apologise for that."
    scene 14_544 with Dissolve(1)
    mc "Gonna..."
    z "Look! Friends fight sometimes..."
    mc "We're not friends!"
    z "*Sigh* Dude! Come on! I was frustrated, okay...? Then you said that stuff to me..."
    mc "I didn't say anything!"
    scene 14_545 with Dissolve(1)
    z "You did!"
    z "Ethan also..."
    mc "Exactly! Ethan!"
    scene 14_546 with Dissolve(1)
    to "Oh... What's going on here?"
    da "..."
    to "Tweedle Dee and Tweedle Dum fighting..."
    scene 14_547 with Dissolve(1)
    mc "What else should I have expected after finding out you're hanging around with Ethan?"
    mc "He completely mind-fucked you."
    mc "Though honestly, probably not just your mind... Considering how you kiss guys and treat girls like shit. No wonder you don't..."
    z "What the hell did you just say, motherfucker?"
    scene 14_548 with Dissolve(1)
    mc "..."
    da "Oh shit!"
    scene 14_549 with Dissolve(1)
    mc "If you think I'll let you hit me again, you're mistaken."
    z "Fuck off!"
    scene 14_550 with Dissolve(1)
    da "Oh wow, he goes for a second swing... and whiffs again!"
    mc "..."
    da "Learn to throw a punch, dude. You're embarrassing yourself."
    mc "{i}(What the fuck is he doing?){/i}"
    menu:
        "Punch him back[KoGa3AutoWTChange1]{size=-4}(Zach Week6 Monday Punch) {/size} {/color}":
            $ achievement.grant("ACHIEVEMENT_ZACH_ATTACKED")
            $ achievement.sync()
            $ Zach_Week6_Monday_Punch = True
            scene 14_551 with Dissolve(1)
            mc "..."
            z "Ahh..."
            da "Damn..."
        "Push him away":
            scene 14_552 with Dissolve(1)
            mc "Get off me already!"
            z "Aaah..."
    scene 14_553 with vpunch
    z "Argh..."
    to "Hey! Watch out where you're falling!"
    to "You almost hit me!"
    scene 14_554 with Dissolve(1)
    z "You fatherless piece of shit!"
    da "Whoa... Now it's getting personal."
    scene 14_555 with Dissolve(1)
    tr "HEY! What's going on here?"
    mc "..."
    mc "{i}(Of course... At the worst time...){/i}"
    scene 14_556 with Dissolve(1)
    z "That motherfucker hit me!"
    tr "Language!"
    if Zach_Week6_Monday_Punch == True:
        mc "You swung first, asshole!"
    else:
        mc "I didn't hit you, asshole!"
    scene 14_557 with Dissolve(1)
    tr "ENOUGH!"
    tr "Both of you! That's it!"
    tr "On your feet. Get to class. Now."
    tr "That goes for the rest of you too. Show's over!"
    scene 14_558 with Dissolve(1)
    z "*Whispers* This is all your fault! This isn't over!"
    mc "*Shakes head*"
    scene 14_559 with Dissolve(1)
    stop music fadeout 1.0
    play music ("Music/LoFi Upbeat 1.mp3", "Music/LoFi Upbeat 2.mp3", "Music/LoFi Upbeat 3.mp3", "Music/LoFi Upbeat 4.mp3") volume 0.2
    ""
    if Layla_End == True:
        pass
    else:
        if Layla_Week5_Wednesday_BreakUp == True:
            pass
        else:
            scene 14_560 with Dissolve(1)
            la "Hey!"
            mc "Hey..."
    scene 14_561 with Dissolve(1)
    if Zach_Week6_Monday_Punch == True:
        da "About time someone clocked that guy!"
        to "Right? Took over two years for it to happen..."
        to "And an unexpected someone at that."
        da "Shame Ramirez showed up. I wanted round two."
    else:
        da "Damn... it was just getting good."
        da "And then Ramirez had to kill the vibe."
    if Layla_End == True:
        pass
    else:
        if Layla_Week5_Wednesday_BreakUp == True:
            pass
        else:
            scene 14_562 with Dissolve(1)
            la "Do you know what they are talking about?"
            mc "..."
            mc "Yeah. I'll tell you after class."
    scene 14_563 with Dissolve(1)
    x "Zachery Gallagher to the principal's office, please."
    x "Zachery Gallagher to the principal's office!"
    mc "{i}(Shit...){/i}"
    mc "{i}(That means I'm next.){/i}"
    scene 14_564 with Dissolve(1)
    la "Did Zach do something again?"
    el "Most likely."
    la "*Shakes head* Heh..."
    scene 14_565 with Dissolve(1)
    tc "Good afternoon, everyone."
    tc "Please take your seats!"
    scene 14_566 with Dissolve(1)
    tc "Before we begin today's lesson, let's talk about a fun little project you'll be working on, due next week."
    st "*Groans*"
    tc "It's a group project. Well... You'll be working in pairs."
    scene 14_567 with Dissolve(1)
    la "Elena? Us two?"
    el "Sure!"
    to "Jasmine!"
    jz "Mm-hmm."
    scene 14_568 with Dissolve(1)
    da "Hey, Valeria. Wanna pair up with me?"
    va "Uhm... Sure?"
    mc "{i}(Damn, everyone's pairing up fast.){/i}"
    scene 14_569 with Dissolve(1)
    tc "Hold on, hold on! Not so fast!"
    tc "I know you all love picking the same partners every time. This time, I will be assigning the groups."
    st "What? No!"
    scene 14_570 with Dissolve(1)
    tc "Alright... Let's see..."
    tc "Tori and..."
    mc "{i}(Please not me!){/i}"
    if Tori_End == True:
        mc "{i}(She's going to be a nightmare to work with.){/i}"
    else:
        if Tori_Week3_Saturday_TC_Sex == False:
            mc "{i}(She's going to be a nightmare to work with.){/i}"
        else:
            mc "{i}(I love fucking her, but I know she'll be a pain to work with.){/i}"
    scene 14_571 with Dissolve(1)
    tc "Elena!"
    el "..."
    mc "{i}(I'm happy it's not me...){/i}"
    mc "{i}(Dodged a bullet... But poor Elena.){/i}"
    if LayLena == True:
        mc "{i}(I would've actually liked teaming up with her.){/i}"
    else:
        pass
    scene 14_572 with Dissolve(1)
    tc "Next... Layla and..."
    mc "{i}(Can it get any worse than the Elena and Tori pairing?){/i}"
    if Layla_End == True:
        mc "{i}(It could be nice to be paired with Layla... Maybe a chance to fix things.){/i}"
    else:
        if Layla_Week5_Wednesday_BreakUp == True:
            mc "{i}(It could be nice to be paired with Layla... Maybe a chance to fix things.){/i}"
        else:
            mc "{i}(I'd be happy working with Layla.){/i}"
    scene 14_573 with Dissolve(1)
    tc "Darryl."
    mc "{i}(Oh. I take that back... It can get worse.){/i}"
    mc "{i}(She does not look thrilled, either.){/i}"
    scene 14_574 with Dissolve(1)
    mc "{i}(That's two bullets dodged already.){/i}"
    tc "Caleb and TJ."
    mc "{i}(Still wondering who I'll get stuck with...){/i}"
    mc "{i}(Is there anyone I don't want?){/i}"
    scene 14_575 with Dissolve(1)
    tc "Next is..."
    tc "Valeria..."
    if Layla_End == True:
        pass
    else:
        if Valeria_LikeMC == False:
            mc "{i}(I wouldn't mind being teaming up with Valeria.){/i}"
        else:
            mc "{i}(Me-me-me! Come on, say my name!){/i}"
    scene 14_576 with Dissolve(1)
    x "[mc] Moreno to the principal's office, please."
    x "[mc] Moreno to the principal's office!"
    mc "..."
    mc "{i}(Fuck! I completely forgot about that...){/i}"
    mc "{i}(And my name is not fucking Moreno! I still need to change that!){/i}"
    if Layla_End == True:
        pass
    else:
        if Layla_Week5_Wednesday_BreakUp == True:
            pass
        else:
            scene 14_577 with Dissolve(1)
            la "Why do you have to go?"
            la "Did something happen with Zach?"
            mc "I'll explain after school."
    scene 14_578 with Dissolve(1)
    to "It was nice knowing you!"
    mc "*Shakes head* Shut up, Tori!"
    to "Haha."
    scene 14_579 with Dissolve(1)
    mc "{i}(This happened at the worst time possible.){/i}"
    mc "{i}(Why did I have to run into that guy, today?){/i}"
    mc "{i}(Now I don't even know who I'm paired with... or what the assignment is.){/i}"
    mc "{i}(But that's the least of my worries right now. I've got bigger problems coming.){/i}"
    scene black with Dissolve(1)
    pause 2
    scene 14_580 with Dissolve(1)
    mc "{i}(This sucks... Just sitting here, waiting.){/i}"
    mc "{i}(It's making me even more nervous...){/i}"
    scene 14_581 with Dissolve(1)
    mc "{i}(Oh... He was still inside?){/i}"
    mc "{i}(And what the fuck is he smirking at?){/i}"
    mc "{i}(Just leave already. I can't stand that smug face another second.){/i}"
    scene 14_582 with Dissolve(1)
    mc "..."
    scene 14_583 with Dissolve(1)
    am "Aren't you coming in?"
    mc "Oh, sorry. I didn't know I was okay to, yet."
    am "I asked Zach to tell you."
    mc "He didn't say a word."
    mc "{i}(Thanks a lot, douchebag!){/i}"
    scene 14_584 with Dissolve(1)
    am "Come on! Let's go!"
    mc "{i}(Why do I suddenly have a really bad feeling about this?){/i}"
    scene 14_585 with Dissolve(1)
    am "Have a seat."
    mc "Thanks."
    scene 14_586 with Dissolve(1)
    am "..."
    mc "..."
    if Week6_Monday_BBQ_Invitation == False:
        pass
    else:
        scene 14_587 with Dissolve(1)
        am "*Sigh...*"
        mc "{i}(That sigh... it says everything.){/i}"
        mc "{i}(This feels worse than disappointing my mom.){/i}"
        mc "{i}(I feel terrible right now.){/i}"
        scene 14_588 with Dissolve(1)
        mc "I'm sorry, Adriana. I..."
        am "..."
        mc "Sorry. I mean, Principal Moore."
    scene 14_589 with Dissolve(1)
    am "So... why don't you tell me what happened?"
    am "I was under the impression that you and Zach were friends."
    mc "..."
    menu:
        "Stay quiet[KoGa3AutoWTChange1]{size=-4}(Adriana Week6 Monday DontTell, Adriana Points-6) {/size} {/color}":
            $ Adriana_Week6_Monday_DontTell = True
            $ Adriana_Points -= 6
            scene 14_591 with Dissolve(1)
            am "So?"
            mc "..."
            am "Nothing? You're not even going to try to explain?"
            mc "..."
            scene 14_601 with Dissolve(1)
            am "*Sigh* Okay, fine!"
            am "You're not giving me much of a choice here."
            am "You know we have a strict policy on fighting, right?"
        "Tell her what happened":
            scene 14_590 with Dissolve(1)
            mc "Uhm..."
            mc "It actually started before spring break."
            mc "Zach invited me to a show after school."
            mc "On the way, we ran into Ethan."
            scene 14_591 with Dissolve(1)
            mc "He used to bully me when I was younger. Honestly, he hasn't changed much."
            mc "You might know him."
            am "Ethan Bloomberg?"
            mc "Mm-hmm."
            if Alexis_Dating == False:
                am "Yes, I've heard about him."
            else:
                am "Yes, Alexis has mentioned him."
            scene 14_592 with Dissolve(1)
            mc "He started spewing all kinds of bullshit..."
            mc "And Zach believed every word."
            mc "He said I was never his friend, that I only used him and never helped out."
            scene 14_593 with Dissolve(1)
            mc "Then, out of nowhere, he punched me in the face."
            am "..."
            mc "They left shortly after."
            scene 14_594 with Dissolve(1)
            mc "I haven't seen or spoken to him since."
            mc "Until a few minutes ago in the hallway."
            mc "He acted like nothing happened."
            mc "So I told him I didn't want to talk and tried to walk away."
            scene 14_595 with Dissolve(1)
            mc "But he stopped me and asked what was wrong."
            mc "I reminded him about what happened before spring break."
            mc "Instead of apologising, he doubled down, blaming me..."
            mc "Things escalated, and he started swinging at me again."
            if Zach_Week6_Monday_Punch == True:
                scene 14_596 with Dissolve(1)
                mc "*Sigh...*"
                mc "I defended myself... And punched him back."
                am "You shouldn't have done that."
                mc "I know... But..."
                am "No buts..."
                scene 14_597 with Dissolve(1)
                mc "Sorry, I know. But what else could I have done?"
                am "Walk away!"
                mc "I tried, but he stopped me."
                mc "If I'd turned my back, he would've hit me from behind."
                am "..."
            else:
                scene 14_598 with Dissolve(1)
                mc "*Sigh...*"
                mc "I only started defending myself because I didn't want to get hit."
                mc "So I pushed him away. He stumbled and fell."
                mc "That's when Ms Ramirez showed up, and Zach started screaming that I hit him."
                scene 14_596 with Dissolve(1)
                am "Did you hit him?"
                mc "No! I didn't! I just pushed him away."
                mc "There were enough people who saw that."
                mc "{i}(Darryl and Tori... Not exactly on my side... Who else was there?){/i}"
                if Adriana_Week2_Monday_Truth == False:
                    $ Adriana_Points -= 4
                    scene 14_599 with Dissolve(1)
                    am "Here's the problem."
                    am "That's not what Zach and Ms Ramirez reported."
                    mc "What? He's lying and she wasn't even there. She didn't see a thing!"
                    if Gabi_End == False:
                        mc "{i}(Why would Gabi say that? What the fuck?){/i}"
                    else:
                        pass
                    am "And this isn't the first time you've lied to me."
                    mc "{i}(Fuck...){/i}"
                else:
                    scene 14_600 with Dissolve(1)
                    am "I believe you. But here's the problem."
                    am "That's not what Zach and Ms Ramirez said."
                    mc "What? He's lying and she wasn't even there. She didn't see a thing!"
                    if Gabi_End == False:
                        mc "{i}(Why would Gabi say that? What the fuck?){/i}"
                    else:
                        pass
                        mc "*Shakes head*"
            scene 14_601 with Dissolve(1)
            am "I'll look into it further, but for now, I don't have much choice."
            am "We have a very strict policy about fighting."
            mc "{i}(I really should've read the manual...){/i}"
    scene 14_602 with Dissolve(1)
    am "You and Zach are both suspended for three days!"
    mc "What? No!"
    if Week6_Monday_BBQ_Invitation == True:
        mc "Adriana... I mean, Principal Moore, please!"
    else:
        mc "Principal Moore... Please!"
    scene 14_603 with Dissolve(1)
    mc "We have the relay race coming up this week."
    mc "And if I'm suspended, I can't train with the team and..."
    am "You should've thought about that before you fought with Zach."
    if Zach_Week6_Monday_Punch == True:
        mc "..."
    else:
        mc "But I didn't hit him!"
        if Adriana_Week6_Monday_DontTell == True:
            am "You didn't say anything when I asked you!"
            mc "..."
        else:
            pass
    scene 14_604 with Dissolve(1)
    mc "Can't we just move the suspension to next week or something?"
    am "It doesn't work like that."
    mc "{i}(Fuck!){/i}"
    mc "{i}(All because of that fucking asshole!){/i}"
    mc "How about detention for a week? A month?"
    am "*Shakes head*"
    scene 14_605 with Dissolve(1)
    am "I also have to inform your mom..."
    mc "Please, no! If she hears about this, she'll..."
    am "I'm sorry but..."
    mc "Please?"
    scene 14_606 with Dissolve(1)
    mc "Can you at least give me the chance to talk to her first?"
    mc "So I can explain it..."
    am "I'll do that. I'll call her this afternoon."
    mc "Thank you."
    scene 14_607 with Dissolve(1)
    mc "..."
    am "..."
    scene 14_608 with Dissolve(1)
    am "That's everything. You may collect your things and go home."
    mc "I have one question."
    am "Sure. Go ahead."
    mc "The three-day suspension. Does that include today?"
    am "No, it starts tomorrow."
    scene 14_609 with Dissolve(1)
    mc "{i}(Until Friday... That means I basically miss the whole week. Fuck...){/i}"
    mc "{i}(Coach will probably find someone else to run.){/i}"
    mc "*Sigh*"
    scene 14_610 with Dissolve(1)
    mc "Thank you, Principal Moore."
    mc "See you Friday."
    if Week6_Monday_BBQ_Invitation == True:
        am "..."
    else:
        pass
    am "Come by my office before class starts, okay?"
    mc "Will do. Bye..."
    am "Bye, [mc]."
    if Week6_Monday_BBQ_Invitation == True:
        scene 14_611 with Dissolve(1)
        am "*Sigh...*"
        scene 14_612 with Dissolve(1)
        zo "Hey!"
        am "Hey..."
        zo "It's not often you call me from work."
        zo "What's up?"
        scene 14_613 with Dissolve(1)
        am "*Sigh*"
        am "I hate this job, sometimes."
        zo "What happened?"
    else:
        pass
    if Layla_End == True:
        pass
    else:
        scene 14_614 with Dissolve(1)
        la "He's been gone a while now."
        la "Isn't he coming back?"
        el "No idea. Maybe Darryl knows what happened. Wanna ask him?"
        la "..."
        if Layla_Week5_Wednesday_BreakUp == True:
            pass
        else:
            la "I'll call [mc] after class, if he still hasn't returned."
    scene 14_615 with Dissolve(1)
    mc "{i}(This is really the worst possible time for this to happen.){/i}"
    mc "{i}(I'll probably miss the relay race now. And who knows what else.){/i}"
    if Week6_Monday_BBQ_Invitation == True:
        mc "{i}(And I can forget about the barbecue tomorrow. Adriana probably won't be keen on seeing me there.){/i}"
        if AlexisValeria == False:
            pass
        else:
            mc "{i}(At least I won't have to choose between that and the emo party with Valeria anymore.){/i}"
            mc "{i}(If she even still wants to go after all this.){/i}"
    else:
        pass
    scene 14_616 with Dissolve(1)
    mc "{i}(A suspension... It's definitely going on my record.){/i}"
    mc "{i}(This could ruin everything... My chances for a scholarship, too.){/i}"
    mc "{i}(Mom's going to be so mad.){/i}"
    mc "{i}(Fuck!){/i}"
    mc "{i}(Can this day get any worse?){/i}"
    if MC_Bike == True:
        scene 14_617 with Dissolve(1)
        mc "..."
        scene 14_618 with Dissolve(1)
        mc "No-no-no-no-no..."
        scene 14_619 with Dissolve(1)
        mc "Fuck-fuck-FUCK!"
        scene 14_620 with Dissolve(1)
        mc "{i}(Who did this?){/i}"
        mc "..."
        mc "{i}(Why am I asking? I know exactly who did it.){/i}"
        mc "{i}(That fucking asshole!){/i}"
        scene 14_621 with Dissolve(1)
        mc "..."
        scene 14_622 with Dissolve(1)
        mc "Come on, come on!"
        scene 14_623 with Dissolve(1)
        mc "*Heavy breathing*"
        mc "{i}(Fuck!){/i}"
        mc "{i}(It's way too heavy. No way I can get it up by myself.){/i}"
        scene black with Dissolve(1)
        pause 2
        scene 14_624 with Dissolve(1)
        mc "Hey, John."
        jo "Hey, [mc]. Perfect timing! Come help me for a sec."
        mc "What happened? Did you drop the bike?"
        jo "No-no. It's easier to work on it like this. Since I don't have a lift, this was the only way."
        scene 14_625 with Dissolve(1)
        mc "You want me to help get it back up?"
        jo "No, I need to tighten some bolts. Can you hold this bar straight for me?"
        mc "Okay."
        scene 14_626 with Dissolve(1)
        jo "Thanks, I appreciate it."
        mc "Anytime."
        scene 14_627 with Dissolve(1)
        mc "Now the hard part... Getting it back up."
        jo "It's not that difficult."
        mc "No? That bike's really heavy."
        jo "Yeah, but you just have to use your legs. I'll show you."
        scene 14_628 with Dissolve(1)
        jo "Hold the handlebar with one hand, the other hand here on the side, and push up with your legs."
        mc "Easier said than done... You're way stronger than me."
        jo "Iris can do it."
        mc "With this bike?"
        jo "With this one! Come on, give it a try!"
        scene black with Dissolve(1)
        pause 2
        scene 14_629 with Dissolve(1)
        mc "..."
        scene 14_630 with Dissolve(1)
        mc "*Sigh*"
        mc "Thanks, John!"
        scene 14_631 with Dissolve(1)
        ""
    else:
        pass
    jump Week6_Monday_Afternoon_MCroom

label Week6_Monday_Afternoon_MCroom:
    scene black with Dissolve(1)
    pause 2
    stop music fadeout 1.0
    play music ("Music/LoFi Indie 3.mp3", "Music/LoFi Indie 1.mp3", "Music/LoFi Indie 2.mp3") volume 0.2
    scene 14_632 with Dissolve(1)
    ""
    scene 14_633 with vpunch
    mc "..."
    scene 14_634 with Dissolve(1)
    mc "*Muffled* FUCK!"
    scene 14_635 with Dissolve(1)
    mc "*Sigh...*"
    if Erynn_Week5_Tuesday_Photoshoot_Join == False:
        pass
    else:
        scene 14_636 with Dissolve(1)
        mc "..."
        scene black with Dissolve(1)
        transform moveup:
            xalign 0.5 yalign 1.0
            linear 5.0 yalign 0.0
        show 14_637 at moveup
        pause 3
        mc "What the fuck?"
        scene 14_638 with Dissolve(1)
        mc "{i}(That's one of the photos from the shoot...){/i}"
        mc "{i}(Is this the final ad?){/i}"
        scene 14_639 with Dissolve(1)
        mc "{i}(It looks amazing. Erynn looks incredible!){/i}"
        mc "{i}(I wish I could feel happier about it, but after everything that's happened today...){/i}"
        mc "*Sigh*"
        scene 14_640 with Dissolve(1)
        mc "{i}(Honestly, I don't mind having it on my wall.){/i}"
        if Alexis_Dating == True:
            mc "{i}(Alexis might, though.){/i}"
        else:
            if Nikki_Girlfriend == True:
                mc "{i}(Nikki might, though.){/i}"
                mc "{i}(Maybe I should take it down before she visits later this week?){/i}"
            else:
                pass
        mc "{i}(I'll leave it up for a while. Erynn would be sad if I took it down immediately.){/i}"
        scene 14_641 with Dissolve(1)
        mc "{i}(When did she put it up?){/i}"
        mc "{i}(I'm sure it wasn't here this morning when I woke up.){/i}"
        mc "{i}(And neither Mom nor I were home...){/i}"
        mc "{i}(Does she have a key? Melissa probably keeps a spare for emergencies. She must've taken it.){/i}"
        mc "Seriously... This girl."
        scene 14_642 with Dissolve(1)
        mc "{i}(Wait... Is this what the other students were talking about?){/i}"
        mc "{i}(Maybe they saw the ad somewhere? Yeah, that makes sense!){/i}"
        mc "{i}(Now I wonder where these ads are being shown.){/i}"
        mc "{i}(Erynn probably knows. I'll have to ask her next time I see her.){/i}"
    scene 14_643 with Dissolve(1)
    if Week6_Monday_BBQ_Invitation == True:
        mc "{i}(I should call Mom before Adriana does.){/i}"
    else:
        mc "{i}(I need to call Mom before Principal Moore does.){/i}"
    mc "*Sigh*"
    mc "{i}(What do I even say?){/i}"
    mc "{i}(She's gonna be so mad...){/i}"
    scene 14_644 with Dissolve(1)
    mc "..."
    mc "{i}(Maybe she won't pick up...){/i}"
    mc "{i}(She might be busy.){/i}"
    scene 14_645 with Dissolve(1)
    m "Hey!"
    mc "{i}(Not too busy to not pick up...){/i}"
    mc "Hey, Mom."
    if MC_Bike == False:
        scene 14_646 with Dissolve(1)
    else:
        scene 14_654 with Dissolve(1)
    m "Are you done with school already?"
    mc "Uhm... yeah, I guess you could say that."
    mc "Mom?"
    m "Hmm?"
    if MC_Bike == False:
        scene 14_647 with Dissolve(1)
    else:
        scene 14_655 with Dissolve(1)
    mc "I need to tell you something, but please promise me you won't be mad."
    m "Did something happen?"
    mc "Please don't be angry, okay?"
    m "I can't promise that if I don't know what it's about."
    mc "..."
    if MC_Bike == False:
        scene 14_648 with Dissolve(1)
    else:
        scene 14_656 with Dissolve(1)
    mc "I've been expelled."
    m "EXPELLED?"
    mc "No, not expelled... I mean suspended!"
    mc "{i}(Why did I say expelled?){/i}"
    scene 14_649 with Dissolve(1)
    m "Expelled or suspended?"
    mc "Suspended... For three days."
    m "*Sigh*"
    mc "I'm sorry, Mom."
    if MC_Bike == False:
        scene 14_650 with Dissolve(1)
    else:
        scene 14_657 with Dissolve(1)
    m "What happ... No!"
    m "Can you come to the restaurant?"
    m "I don't want to talk about this over the phone."
    mc "Yeah... I'm on my way. About thirty minutes."
    if Erynn_Week5_Tuesday_Photoshoot_Join == False:
        scene 14_651 with Dissolve(1)
    else:
        scene 14_652 with Dissolve(1)
    m "Okay, see you then."
    mc "Bye, Mom."
    m "Bye."
    scene 14_653 with Dissolve(1)
    mc "*Sigh*"
    mc "{i}(Let's just get this over with.){/i}"
    mc "{i}(I hope she won't be too mad.){/i}"
    jump Week4_Monday_Restaurant

label Week4_Monday_Restaurant:
    scene black with Dissolve(1)
    pause 2
    stop music fadeout 1.0
    play music ("Sounds/Restaurant_Background.mp3","Sounds/Restaurant_Background2.mp3","Sounds/Restaurant_Background3.mp3") volume 0.2
    scene 14_658 with Dissolve(1)
    br "Hey!"
    mc "Hi, Brooke."
    scene 14_659 with Dissolve(1)
    br "How are you? No school today?"
    mc "You haven't heard?"
    br "Okay... I kinda did... I was standing right next to Emily when you called."
    br "I just wanted to..."
    mc "Haha, it's okay. Thanks."
    scene 14_660 with Dissolve(1)
    mc "You know where Mom is?"
    br "Yes. She's..."
    if MC_Bike == False:
        scene 14_661 with Dissolve(1)
        m "Right here!"
        br "There you go."
        mc "Heh, thanks... See you later, Brooke. Maybe..."
        br "Haha."
        scene 14_663 with Dissolve(1)
        mc "Hey, Mom."
        m "Hey. Are you alright?"
        mc "Yeah..."
        scene 14_664 with Dissolve(1)
        m "Want to talk in my office?"
        mc "..."
        mc "Can't we just sit here at one of the tables?"
        scene 14_665 with Dissolve(1)
        m "Why? Want to eat something?"
        mc "No, it's... because I'm a little scared of you."
        m "Scared of me? Why would you be scared?"
        mc "I don't know... Maybe you'll hit me or yell at me."
        scene 14_666 with Dissolve(1)
        m "First of all, I would never hit you!"
        m "And second... Is there a reason I would yell at you?"
        if Zach_Week6_Monday_Punch == True:
            mc "I don't know? Maybe?"
        else:
            mc "No, not really."
        m "..."
        scene 14_667 with Dissolve(1)
        m "Brooke, can you bring us two coffees, please?"
        br "Of course."
        m "Thank you."
    else:
        scene 14_668 with Dissolve(1)
        m "Right here!"
        br "There you go."
        mc "Heh, thanks... See you later, Brooke. Maybe..."
        br "Haha."
        scene 14_662 with Dissolve(1)
        mc "Hey, Mom."
        m "Hey. Are you alright?"
        mc "Yeah..."
        scene 14_669 with Dissolve(1)
        m "Want to talk in my office?"
        mc "..."
        mc "Can't we just sit here at one of the tables?"
        scene 14_670 with Dissolve(1)
        m "Why? Want to eat something?"
        mc "No, it's... because I'm a little scared of you."
        m "Scared of me? Why would you be scared?"
        mc "I don't know... Maybe you'll hit me or yell at me."
        scene 14_671 with Dissolve(1)
        m "First of all, I would never hit you!"
        m "And second... Is there a reason I would yell at you?"
        if Zach_Week6_Monday_Punch == True:
            mc "I don't know? Maybe?"
        else:
            mc "No, not really."
        m "..."
        scene 14_672 with Dissolve(1)
        m "Brooke, can you bring us two coffees, please?"
        br "Of course."
        m "Thank you."
    if MC_Bike == False:
        scene 14_673 with Dissolve(1)
        m "So... What happened?"
        m "Why did the school suspend you? I thought everything was going well."
        mc "*Sigh*"
        mc "It was... It's nothing like last time, I promise."
        mc "I'll tell you everything. It actually started before spring break..."
        scene black with Dissolve(1)
        pause 2
        if Zach_Week6_Monday_Punch == True:
            scene 14_674 with Dissolve(1)
            m "You shouldn't have hit him."
            mc "I know, but..."
            m "I get it. That's all that happened?"
            mc "*Nods* Yeah."
            m "Hmm..."
        else:
            scene 14_674 with Dissolve(1)
            m "And you didn't hit him?"
            mc "No, I didn't. The teacher wasn't even there, so I don't know why she said I did..."
            mc "I just pushed him away."
            m "I believe you. If you say you didn't hit him, you didn't. Was that everything?"
            mc "*Nods* Yeah, nothing else."
            m "Hmm..."
        scene 14_675 with Dissolve(1)
        mc "You're not mad?"
        m "No. I'm just glad you're okay and that it didn't get worse."
        m "The suspension is final?"
        mc "I think so. Adriana said she'd look more into it."
        scene 14_676 with Dissolve(1)
        m "I'll call her later."
        mc "She's supposed to call you in about an hour."
        mc "If anything serious happens at school, they have to notify parents or guardians."
        m "That makes sense. I'll wait for her call, then."
        scene 14_677 with Dissolve(1)
        m "*Sigh*"
        mc "..."
        mc "{i}(I expected a very different reaction from her.){/i}"
        mc "{i}(Anger, disappointment... Maybe even yelling.){/i}"
        mc "{i}(But she seems... relieved. Maybe she thought it was something worse.){/i}"
        scene 14_678 with Dissolve(1)
        mc "Thanks for not being angry, Mom."
        m "You didn't start this. From what I see, you were just defending yourself."
        if Zach_Week6_Monday_Punch == True:
            m "Am I happy you hit him? No. But... Boys will be boys."
            mc "Heh..."
        else:
            m "Boys will be boys."
            mc "Heh..."
        scene 14_739 with Dissolve(1)
        mc "There's something I wanted to ask you about Santiago."
        m "Santiago?"
        mc "Yeah, I've been meaning to talk about it for a while, now."
        m "Okay, go ahead."
        scene 14_740 with Dissolve(1)
        mc "I'm pretty sure I'm right about this, but is his last name Navarro?"
        m "*Nods*"
        mc "And he's a sports agent?"
        m "He is."
        mc "{i}(That settles it. It's definitely him!){/i}"
        scene 14_741 with Dissolve(1)
        mc "So... he really is my dad."
        m "..."
        m "*Nods*"
        m "Have you met him before?"
        mc "I have. A few times, actually. But I didn't know he was my dad until last week."
        scene 14_742 with Dissolve(1)
        mc "We were sitting next to each other at the bar."
        mc "We started talking about the game and some other stuff and then he mentioned you. 'Little Emi'."
        m "..."
        mc "That's when I connected the dots."
        m "I see."
        scene 14_743 with Dissolve(1)
        mc "Does he know who I am?"
        m "I haven't spoken to him since you came back, so he probably still thinks you're living in Alvarado."
        m "If he knew, I think he would've at least called me to confirm."
        if Week6_Monday_BBQ_Invitation == False:
            pass
        else:
            mc "That's also what Enzo said. He's too caught up to think about all this right now."
            scene 14_744 with Dissolve(1)
            m "Enzo Monroe? Adriana's husband?"
            mc "Yeah. Definitely not my dad!"
            m "What?"
            mc "It's a long story. I'll explain it another time."
            m "Alright."
        scene 14_745 with Dissolve(1)
        mc "If he knew who I was, do you think he'd want to meet me?"
        m "Yes, I believe he would."
        m "..."
        m "Do you want to reach out to him?"
        mc "I'm not sure yet. So much has happened. I haven't really had the chance to think it over."
        scene 14_746 with Dissolve(1)
        m "Hey!"
        m "Whatever you decide, I'll support you. Always."
        m "And if you have questions, just ask me, okay?"
        mc "Thanks, Mom."
        scene 14_747 with Dissolve(1)
        m "Anything else on your mind?"
        mc "No, I'm okay for now."
        m "Alright. I'm off to the kitchen to start prepping for the evening rush."
        m "What about you? Got any plans?"
        scene 14_748 with Dissolve(1)
        mc "I'm heading to the garage."
        mc "See if John has time to check the car."
        m "Thank you for handling that. It really helps me out."
        mc "Of course."
        scene 14_749 with Dissolve(1)
        m "Want to grab a bite before you go?"
        mc "I already ate at school."
        m "So, no then?"
        mc "Yeah, I'm good for now. Might swing by later for a snack."
        m "Sounds good."
        scene 14_750 with Dissolve(1)
        m "And if John figures out what's wrong with the car, please call me, okay?"
        mc "Will do."
        m "Thanks again."
        jump Week6_Monday_Garage
    else:
        scene 14_679 with Dissolve(1)
        m "So... What happened?"
        m "Why did the school suspend you? I thought everything was going well."
        mc "*Sigh*"
        mc "It was... It's nothing like last time, I promise."
        mc "I'll tell you everything. It actually started before spring break..."
        scene black with Dissolve(1)
        pause 2
        if Zach_Week6_Monday_Punch == True:
            scene 14_680 with Dissolve(1)
            m "You shouldn't have hit him."
            mc "I know, but..."
            m "I get it. That's all that happened?"
        else:
            scene 14_680 with Dissolve(1)
            m "And you didn't hit him?"
            mc "No, I didn't. The teacher wasn't even there, so I don't know why she said I did..."
            mc "I just pushed him away."
            m "I believe you. If you say you didn't hit him, you didn't. Was that everything?"
        scene 14_681 with Dissolve(1)
        mc "Uhm... My bike got scratched."
        m "What? Scratched? When did that happen? Did you crash it?"
        mc "No..."
        scene 14_682 with Dissolve(1)
        mc "When I left school earlier, it was lying on the ground in the parking lot."
        m "Lying on the ground? You mean it fell over?"
        mc "It normally doesn't just fall like that."
        mc "Someone must have pushed it."
        scene 14_683 with Dissolve(1)
        m "Why would someone do that? Do you have any idea who?"
        menu:
            "No idea":
                mc "No idea."
                m "Did you tell the school?"
            "Suspect Zach[KoGa3AutoWTChange1]{size=-4}(Zach Week6 Monday BikeSuspect) {/size} {/color}":
                $ Zach_Week6_Monday_BikeSuspect = True
                mc "Maybe Zach. He got suspended too and left before me."
                mc "But I didn't see it happen, so I can't just blame him."
                m "Did you tell the school?"
        scene 14_684 with Dissolve(1)
        mc "No."
        m "Well, you should! It happened on school grounds."
        m "Maybe someone saw something. Or they have cameras."
        mc "Yeah, you're right. I should have taken pictures, too!"
        scene 14_685 with Dissolve(1)
        m "Is the damage bad?"
        mc "There are scratches on one side, maybe a few dents..."
        m "Nothing else broken?"
        mc "Not that I've noticed. I haven't checked closely yet. Looks mostly only cosmetic damage."
        scene 14_686 with Dissolve(1)
        mc "I'm going to see John later about the car, anyway."
        mc "I'll ask him to take a look at the bike, too."
        m "Make sure to take pictures before you do anything!"
        mc "I will."
        scene 14_687 with Dissolve(1)
        mc "You're not mad?"
        m "I'm upset about the bike, but I'm just glad you're okay and nothing worse happened."
        m "Is the suspension final?"
        mc "I think so. Adriana said she'll look more into it, though."
        scene 14_688 with Dissolve(1)
        m "I'll call her later."
        mc "She should be calling you in about an hour."
        mc "If anything serious happens at school, they have to inform parents or guardians."
        m "Makes sense. I'll wait for her call. And I'll bring up the bike, too."
        mc "Thanks."
        scene 14_689 with Dissolve(1)
        m "*Sigh*"
        mc "..."
        mc "{i}(I expected a very different reaction from her.){/i}"
        mc "{i}(Angry, mad, disappointed...) {/i}"
        mc "{i}(But she seems relieved. Maybe she expected it to be worse.){/i}"
        scene 14_690 with Dissolve(1)
        mc "Thanks for not being angry, Mom."
        m "You didn't start this. From what I see, you were just defending yourself."
        if Zach_Week6_Monday_Punch == True:
            m "Am I happy you hit him? No. But... Boys will be boys."
            mc "Heh..."
        else:
            m "Boys will be boys."
            mc "Heh..."
        scene 14_691 with Dissolve(1)
        mc "Sorry for giving you more grey hairs, Mom."
        m "More? What do you mean by more? Do I even have any?"
        mc "I don't know."
        m "Well, I hope not!"
        mc "If you do, it's probably because of me!"
        scene 14_692 with Dissolve(1)
        m "You might be right."
        mc "Soon, you'll look like Melissa's bleached hair."
        m "Oh, please no!"
        mc "Haha."
        scene 14_693 with Dissolve(1)
        mc "Did you ever get suspended from school?"
        m "..."
        mc "You did, didn't you!"
        scene 14_694 with Dissolve(1)
        mc "Come on, tell me! What did you do?"
        m "Nothing! It wasn't my fault."
        mc "Then whose fault was it?"
        m "Santiago's..."
        scene 14_695 with Dissolve(1)
        mc "What did he do to get you suspended?"
        m "He made me skip class one too many times."
        mc "He made you skip? Wasn't it your choice? You could've just said no..."
        m "..."
        scene 14_696 with Dissolve(1)
        mc "And they suspended you for skipping class?"
        mc "Basically they made you skip class for skipping class..."
        mc "That sounds totally counterproductive."
        m "Haha."
        scene 14_697 with Dissolve(1)
        mc "Melissa was right. You were quite the wild child back then."
        m "Did she say anything else?"
        mc "No..."
        m "Besides... Melissa didn't know me before college!"
        mc "{i}(Judging by her reaction, there's clearly a lot more to that story.){/i}"
        scene 14_698 with Dissolve(1)
        mc "Since we're on the topic, there's something I've been wanting to ask about Santiago."
        mc "I've been meaning to talk about this for a while."
        m "Hmm, okay."
        scene 14_699 with Dissolve(1)
        mc "I'm pretty sure I'm right about this, but is his last name Navarro?"
        m "*Nods*"
        mc "And he's a sports agent?"
        m "He is."
        mc "{i}(That settles it. It's definitely him!){/i}"
        scene 14_700 with Dissolve(1)
        mc "So... he really is my dad."
        m "..."
        m "*Nods*"
        m "Have you met him before?"
        mc "I have. A few times, actually. But I didn't know he was my dad until last week."
        scene 14_701 with Dissolve(1)
        mc "We were sitting next to each other at the bar."
        mc "We started talking about the game and some other stuff and then he mentioned you. 'Little Emi'."
        m "..."
        mc "That's when I connected the dots."
        m "I see."
        scene 14_702 with Dissolve(1)
        mc "Does he know who I am?"
        m "I haven't spoken to him since you came back, so he probably still thinks you're living in Alvarado."
        m "If he knew, I think he would've at least called me to confirm."
        if Week6_Monday_BBQ_Invitation == False:
            pass
        else:
            mc "That's also what Enzo said. He's too caught up to think about all this right now."
            scene 14_703 with Dissolve(1)
            m "Enzo Monroe? Adriana's husband?"
            mc "Yeah. Definitely not my dad!"
            m "What?"
            mc "It's a long story. I'll explain it another time."
            m "Alright."
        scene 14_704 with Dissolve(1)
        mc "If he knew who I was, do you think he'd want to meet me?"
        m "Yes, I believe he would."
        m "..."
        m "Do you want to reach out to him?"
        mc "I'm not sure yet. So much has happened. I haven't really had the chance to think it over."
        scene 14_705 with Dissolve(1)
        m "Hey!"
        m "Whatever you decide, I'll support you. Always."
        m "And if you have questions, just ask me, okay?"
        mc "Thanks, Mom."
        scene 14_706 with Dissolve(1)
        m "Don't you have any grey hairs yet?"
        mc "Haha, probably do!"
        m "Let me check!"
        mc "Haha."
        if Emily_Week4_Sunday_DateJohn == True:
            scene 14_707 with Dissolve(1)
            mc "Since we're talking..."
            mc "You wanted to tell me something too, right?"
            m "Mm-Hmm..."
            scene 14_708 with Dissolve(1)
            m "I went on a date with John."
            mc "Oh, did you?"
            mc "How was it?"
            m "It was nice."
            mc "Yeah?"
            scene 14_709 with Dissolve(1)
            mc "What did you do?"
            m "Uhm..."
            m "We went to a restaurant and got to know each other."
            m "Mostly chatted about you and Iris."
            mc "Heh."
            scene 14_710 with Dissolve(1)
            mc "So, you're dating now?"
            m "It takes a bit more than just one date."
            m "But I'm not opposed to going on another date with him."
            scene 14_711 with Dissolve(1)
            mc "But you like him?"
            m "I'm not sure yet."
            m "I had fun, and he seems like a cool guy."
            mc "A cool guy?"
            m "What?"
            mc "It's just funny hearing you say that. Cool guy..."
            scene 14_712 with Dissolve(1)
            m "What else should I say? He's sexy?"
            mc "Uhm... Okay... Let's stick with cool. I don't need to know more!"
            m "Haha."
        else:
            pass
        scene 14_713 with Dissolve(1)
        m "Anything else on your mind?"
        mc "No, I'm good for now."
        m "Alright, I'm heading to the kitchen to start prepping for the evening rush."
        m "What about you? Got any plans for today?"
        scene 14_714 with Dissolve(1)
        mc "I'm heading to the garage."
        mc "See if John has time to check the car."
        m "Thanks for taking care of that. It'll really save me a lot of time."
        mc "No problem."
        scene 14_715 with Dissolve(1)
        m "Want to eat something before you go?"
        mc "I already ate at school."
        m "Nothing at all?"
        mc "..."
        mc "Maybe just a quick snack."
        scene 14_716 with Dissolve(1)
        m "I'll grab you a menu."
        mc "No need. I'm gonna try those goat-cheese balls."
        m "Alright."
        mc "Just the balls, though. No sides, please."
        m "Got it. Five minutes."
        mc "Thanks."
        if Brooke_Points >= 7:
            $ Brooke_Week6_Monday_ManagerPosition = True
            scene 14_717 with Dissolve(1)
            br "Oh, let me do that, Emily!"
            m "It's fine. I'm heading to the kitchen anyway."
            m "You can take your break now."
            br "Thanks."
            scene 14_718 with Dissolve(1)
            br "..."
            scene 14_719 with Dissolve(1)
            mc "..."
            scene 14_720 with Dissolve(1)
            mc "Not hiding it anymore, huh?"
            br "Not around you. Since you know!"
            mc "You're welcome, by the way."
            mc "She's wearing that because of me."
            scene 14_721 with Dissolve(1)
            br "Yeah, I heard you gave her a bike ride."
            br "The car wouldn't start?"
            mc "Mm-hmm."
            scene 14_722 with Dissolve(1)
            mc "So, how are you doing?"
            mc "Mommy Brooke..."
            br "Keep that up and school won't be the only place you're suspended from!"
            mc "Haha."
            scene 14_723 with Dissolve(1)
            br "What happened? Can I know?"
            mc "Sure."
            mc "Basically, I defended myself, but officially it's 'fighting in school'."
            br "Oh..."
            scene 14_724 with Dissolve(1)
            br "How long is the suspension?"
            mc "Three days."
            br "So, you'll be working here then for the next three days?"
            mc "Haha. Who knows? I haven't talked to Mom about it, yet. Maybe."
            scene 14_725 with Dissolve(1)
            mc "Is it still as crazy as last week?"
            br "We're booked solid for months."
            br "But since spring break's over, today's a bit calmer. Fewer walk-ins."
            scene 14_726 with Dissolve(1)
            br "And we're getting a new manager next week."
            mc "Oh? Mom found someone? Girl? Boy?"
            br "Girl. But it's temporary. She'll manage the café when it opens."
            scene 14_727 with Dissolve(1)
            mc "So the manager position here is still open?"
            br "Yeah."
            mc "Why don't you apply?"
            br "Uhm..."
            scene 14_728 with Dissolve(1)
            mc "You know all the ins and outs here."
            br "I don't know..."
            br "I don't think I'm ready."
            mc "I think you are. You've basically been doing the manager's job these past few weeks."
            scene 14_729 with Dissolve(1)
            mc "Maybe that's why Mom hasn't hired anyone yet."
            mc "She's waiting for you to take the initiative..."
            br "You think so?"
            mc "*Nods*"
            scene 14_730 with Dissolve(1)
            mc "What's the worst that could happen?"
            mc "You don't get the job and keep doing what you're doing..."
            mc "Or you do get it. Keep doing what you're doing and... More money!"
            br "..."
            mc "And you said you like money!"
            scene 14_731 with Dissolve(1)
            br "Alright. I'll think about it."
            mc "Don't wait too long."
            mc "Who knows when another opportunity like this will come."
            scene 14_732 with Dissolve(1)
            m "Here you go!"
            mc "Thanks, Mom."
            m "Is this enough?"
            mc "Yeah, that's plenty. Just wanted a snack."
            scene 14_733 with Dissolve(1)
            m "Need something else? A drink?"
            mc "No, I'm good."
            m "You, Brooke?"
            br "No-no... Thank you, Emily."
            m "Okay. Enjoy."
            scene 14_734 with Dissolve(1)
            mc "Mmm..."
            br "Good?"
            mc "Mm-hmm!"
            scene 14_735 with Dissolve(1)
            mc "I'd offer you some balls, but you don't swing that way, right?"
            br "Ha-ha-ha... Good one!"
            br "Do you?"
            mc "Haha. Touché!"
            scene 14_736 with Dissolve(1)
            br "I'm gonna take two!"
            mc "Hey! My balls!"
            scene 14_737 with Dissolve(1)
            br "..."
            mc "Haha."
            mc "You look like a hamster stuffing her cheeks with nuts."
            mc "In your case... Balls!"
            scene 14_738 with Dissolve(1)
            br "Haha."
            mc "Haha..."
            stop music
            jump Week6_Monday_Garage
        else:
            stop music
            jump Week6_Monday_Garage

label Week6_Monday_Garage:
    scene black with Dissolve(2)
    pause 2
    stop music fadeout 1.0
    play music ("Music/LoFi Indie 1.mp3", "Music/LoFi Indie 2.mp3", "Music/LoFi Indie 3.mp3") volume 0.2
    scene 14_751 with Dissolve(1)
    ""
    scene 14_752 with Dissolve(1)
    mc "..."
    mc "No one's here?"
    mc "Maybe in his office?"
    scene 14_753 with Dissolve(1)
    mc "John?"
    ir "Hey!"
    if Iris_Points >= 1:
        scene black with Dissolve(1)
        transform moveup:
            xalign 0.5 yalign 1.0
            linear 5.0 yalign 0.0
        show 14_754 at moveup
        pause 3
        mc "Oh... Hey, Iris!"
        scene 14_755 with Dissolve(1)
        mc "How are you?"
        ir "I'm good. You?"
        mc "Eh..."
        scene 14_756 with Dissolve(1)
        ""
    else:
        scene 14_755 with Dissolve(1)
        mc "Oh... Hey, Iris!"
        mc "How are you?"
        ir "I'm good. You?"
        mc "Eh..."
    scene 14_757 with Dissolve(1)
    ir "Eh?"
    mc "Long story..."
    ir "..."
    mc "What are you doing here? Shouldn't you be in school?"
    scene 14_758 with Dissolve(1)
    ir "Says you!"
    ir "I only had morning classes. What's your excuse?"
    mc "Let's just say... it's part of that long story."
    scene 14_759 with Dissolve(1)
    ir "..."
    scene 14_760 with Dissolve(1)
    mc "What?"
    ir "Come on! Spill it, already!"
    mc "*Sigh* Fine..."
    scene black with Dissolve(1)
    pause 2
    scene 14_761 with Dissolve(1)
    ir "They suspended you for that?"
    mc "Yeah. They've got a strict policy when it comes to fighting on school grounds."
    if Zach_Week6_Monday_Punch == False:
        ir "But you didn't even do anything! You just pushed him away!"
        mc "That's what I said, but... *Sigh* Nothing I can do about it now."
        scene 14_763 with Dissolve(1)
        ir "I would've punched that idiot."
        mc "I thought about it. If he hadn't fallen when I pushed him, and he kept swinging..."
        mc "Yeah. I probably would've hit him."
        ir "You still can! Wanna go find him?"
        mc "Haha, no. But I appreciate the offer."
    else:
        ir "You were just defending yourself! I would've hit him more than once!"
        mc "So would I, honestly. If he didn't fall after the first punch..."
        scene 14_762 with Dissolve(1)
        ir "I hope he ends up with a huge bruise on his face..."
        ir "So every time he looks in the mirror, he remembers what a total idiot he is!"
        mc "Heh..."
    scene 14_764 with Dissolve(1)
    ir "Anyway... Are you looking for Dad?"
    mc "Mm-hmm."
    if Erynn_Week3_Monday_Blackmailhelp == True:
        ir "You hanging out with him again?"
        mc "I just needed his help with... something."
        ir "Something, huh..."
        mc "{i}(Sorry, Iris. I promised I wouldn't tell.){/i}"
        if Iris_Points >= 1:
            scene 14_765 with Dissolve(1)
            ir "You remember saying we'd spend time together too?"
            mc "I remember. And we will!"
            ir "Feels like old times, doesn't it? Just us, hanging out in Dad's garage."
            mc "Yeah. It really does."
        else:
            pass
    else:
        pass
    scene 14_766 with Dissolve(1)
    mc "Is he here?"
    ir "Not at the moment. He'll be back in an hour or two."
    mc "Hmm, okay."
    ir "What do you need him for? Maybe I can help?"
    scene 14_767 with Dissolve(1)
    mc "Mom's car wouldn't start this morning."
    mc "I was hoping he could take a look at it."
    ir "Yeah, I'm not much use there. I barely know anything about cars."
    ir "Guess you'll have to wait till he's back."
    mc "No worries."
    scene 14_768 with Dissolve(1)
    mc "I see you're working on your bike?"
    ir "Yep!"
    mc "What's up with it?"
    ir "Needs a new stator, and I'm replacing the tires."
    ir "Figured I'd give it a full check-up while I'm at it."
    scene 14_769 with Dissolve(1)
    ir "But since you've got some time..."
    ir "Wanna help me out?"
    mc "Sure thing."
    ir "Yeah? Thanks!"
    scene 14_770 with Dissolve(1)
    mc "Let's see if I still remember where the stator is."
    mc "Been a while since I worked on a bike."
    ir "..."
    scene 14_771 with Dissolve(1)
    mc "Ah, there it is. Still got it!"
    ir "Before you dive in... Want an old shirt or something?"
    ir "Don't wanna mess up the one you're wearing."
    mc "Nah, I'll just take it off."
    ir "That works too!"
    if Iris_Points >= 1:
        scene 14_772 with Dissolve(1)
        ir "..."
        mc "Don't look at me like that!"
        scene 14_773 with Dissolve(1)
        ir "Like what?"
        mc "Like... You know exactly what."
        ir "This is how I always look."
        mc "Right..."
        ir "I like the no-shirt look, though. I might just join you!"
        scene 14_774 with Dissolve(1)
        mc "Iris!"
        ir "Haha."
        menu:
            "Check her out":
                scene 14_775 with Dissolve(1)
                mc "{i}(I always loved her small, perky boobs...){/i}"
                ir "..."
                mc "{i}(If...){/i}"
                mc "{i}(No! Don't start thinking about this now!){/i}"
            "Look away":
                scene 14_776 with Dissolve(1)
                ir "Since when are you shy?"
                mc "I'm not shy. Just... Never mind."
        scene 14_777 with Dissolve(1)
        ir "..."
        scene 14_778 with Dissolve(1)
        ir "I'll go change and grab my toolbox."
        ir "Be right back!"
        mc "Okay."
        scene 14_779 with Dissolve(1)
        mc "{i}(This girl.){/i}"
        mc "{i}(Seriously...){/i}"
        mc "{i}(She's dangerous!){/i}"
        scene black with Dissolve(1)
        pause 2
        scene 14_780 with Dissolve(1)
        ir "I'm back. Got my toolbox!"
        mc "Weren't you going to change too?"
        ir "Oh, right... Forgot about that."
        mc "..."
        scene 14_781 with Dissolve(1)
        mc "Can you pass me the eleven?"
        ir "Yeah, one sec."
        scene 14_782 with Dissolve(1)
        ir "Here you go!"
        mc "Uh..."
        scene 14_783 with Dissolve(1)
        mc "..."
        mc "Pretty sure you forgot something else too."
        ir "Did I?"
        scene 14_784 with Dissolve(1)
        ir "I'm using all my willpower not to just sit down."
        mc "Heh..."
        menu:
            "You're crazy":
                mc "Haha. You're crazy!"
                ir "..."
                scene 14_785 with Dissolve(1)
                ir "Here's the eleven."
                mc "Thanks."
                ir "I'll go change now. Wouldn't want to distract you."
                scene 14_786 with Dissolve(1)
                ir "..."
                jump Week6_Monday_Garage_BikeRepair
            "Sit down[KoGa3AutoWTChange1]{size=-4}(Iris Points+2, Iris LikeMC, Iris Week6 Monday Garage Sex, {i}Alexis Dating: Iris Week6 Monday Garage SexFalse{/i}) {/size} {/color}":
                $ Iris_Points += 2
                # Iris_Points = 4
                $ Iris_LikeMC = True
                $ Iris_Week6_Monday_Garage_Sex = True
                scene 14_787 with Dissolve(1)
                mc "Why don't you just do it?"
                ir "..."
                if Alexis_Dating == True:
                    $ Iris_Week6_Monday_Garage_Sex = False
                    scene 14_788 with Dissolve(1)
                    ir "I was just joking..."
                    ir "You're with Alexis now, remember?"
                    mc "Yeah..."
                    scene 14_785 with Dissolve(1)
                    ir "Here's the eleven."
                    mc "Thanks."
                    ir "I'll go change now. Wouldn't want to distract you."
                    scene 14_789 with Dissolve(1)
                    ir "..."
                    scene 14_790 with Dissolve(1)
                    mc "{i}(I didn't even think about Alexis just now...){/i}"
                    mc "{i}(If Iris hadn't said anything... Would I have stopped?){/i}"
                    scene black with Dissolve(1)
                    pause 2
                    scene 14_884 with Dissolve(1)
                    ir "I'm back!"
                    ir "Ready to get to work!"
                    mc "Great!"
                    scene 14_885 with Dissolve(1)
                    ir "What?"
                    mc "Hmm?"
                    ir "Why are you looking at me like that?"
                    mc "Just... Admiring your shirt."
                    scene 14_886 with Dissolve(1)
                    mc "Though I'm not sure if we can still call it a shirt. It's on its way to becoming rags."
                    ir "Haha!"
                    ir "Hey, this thing's been with me for years."
                    mc "Yeah, I can tell."
                    jump Week6_Monday_Garage_BikeRepair
                else:
                    if Alexis_Week5_Thursday_BreakUp == True:
                        scene 14_788 with Dissolve(1)
                        ir "I was just joking..."
                        ir "You're with Alexis now..."
                        mc "I'm not. We broke up!"
                        scene 14_791 with Dissolve(1)
                        ir "What?"
                        ir "Wait? Really? Why?"
                        mc "Do you really want to know?"
                        ir "..."
                        scene 14_792 with Dissolve(1)
                        mc "I wasn't joking when I said you can sit down!"
                        ir "..."
                        ir "I wasn't either!"
                        mc "I know!"
                        scene 14_793 with Dissolve(1)
                        mc "Then come here!"
                        jump Week6_Monday_Garage_IrisSex
                    else:
                        scene 14_793 with Dissolve(1)
                        mc "I'm not joking!"
                        ir "I wasn't either!"
                        mc "Then come here!"
                        jump Week6_Monday_Garage_IrisSex
    else:
        scene 14_778 with Dissolve(1)
        ir "I'll go change. My toolbox is right there."
        mc "Alright."
        ir "Be right back!"
        scene black with Dissolve(1)
        pause 2
        scene 14_884 with Dissolve(1)
        ir "I'm back!"
        ir "Ready to get to work!"
        mc "Great!"
        scene 14_885 with Dissolve(1)
        ir "What?"
        mc "Hmm?"
        ir "Why are you looking at me like that?"
        mc "Just... Admiring your shirt."
        scene 14_886 with Dissolve(1)
        mc "Though I'm not sure if we can still call it a shirt. It's on its way to becoming rags."
        ir "Haha!"
        ir "Hey, this thing's been with me for years."
        mc "Yeah, I can tell."
        jump Week6_Monday_Garage_BikeRepair

label Week6_Monday_Garage_IrisSex:
    if _in_replay:
        $ Cara_Week5_Saturday_Anal = True
        $ Iris_Points = 4
        $ SexCounter_Iris = 3
        $ MC_SexCounter = 3
    $ SexCounter_Iris += 1
    $ MC_SexCounter += 1
    scene 14_794 with Dissolve(1)
    ir "..."
    scene 14_795 with Dissolve(1)
    ""
    scene 14_796 with Dissolve(1)
    ir "Ahh..."
    scene 14_797 with Dissolve(1)
    ir "Mmm..."
    ir "Keep going!"
    scene 14_798 with Dissolve(1)
    ir "*Moaning*"
    scene 14_799 with Dissolve(1)
    mc "{i}(She's so wet already.){/i}"
    mc "{i}(I always loved eating her out!){/i}"
    scene 14_800 with Dissolve(1)
    ir "[mc]..."
    scene 14_801 with Dissolve(1)
    ir "Ahh..."
    scene 14_802 with Dissolve(1)
    ir "Mmm... Yes, baby!"
    scene 14_803 with Dissolve(1)
    ir "I'm almost... Yes..."
    scene 14_804 with Dissolve(1)
    ir "..."
    scene 14_805 with Dissolve(1)
    ir "I'm... I'm..."
    scene 14_806 with vpunch
    ir "Aaah..."
    ir "*Heavily breathing* Damn..."
    scene 14_807 with Dissolve(1)
    mc "Haah..."
    mc "Finally free from that nightmarish hell! I thought I'd never see daylight again..."
    ir "Nightmarish...?"
    mc "Haha, I'm kidding, I'm kidding!"
    mc "You came fast!"
    scene 14_808 with Dissolve(1)
    ir "The thing you did with your tongue... Where did you learn that?"
    mc "I..."
    ir "Wait... It was me! I taught you that! I'm amazing!"
    ir "It feels good to be rewarded for the hard work I put into training you."
    mc "*Shakes head* Haha. Hard work? You always loved it!"
    scene 14_809 with Dissolve(1)
    ir "I know."
    ir "And this time was no different! It was incredible."
    scene 14_810 with Dissolve(1)
    mc "I figured..."
    mc "My stomach's soaked from all your juices."
    ir "Whose fault is that?"
    mc "Yours! You said it yourself. You trained me!"
    ir "Right... Haha."
    scene 14_811 with Dissolve(1)
    mc "..."
    ir "Go ahead!"
    mc "I was just looking..."
    ir "Of course you were. You wanted to suck them the moment I lifted my shirt earlier."
    ir "And I know you! You always liked sucking my boobs!"
    mc "I sure do!"
    scene 14_812 with Dissolve(1)
    mc "{i}(She doesn't have the biggest boobs...){/i}"
    mc "{i}(But the shape and her puffy nipples...){/i}"
    mc "{i}(They're perfect to me!){/i}"
    scene 14_813 with Dissolve(1)
    ir "Mmm..."
    scene 14_814 with Dissolve(1)
    ir "Your tongue game really has improved!"
    ir "I love it!"
    scene 14_815 with Dissolve(1)
    ir "..."
    scene 14_816 with Dissolve(1)
    ""
    scene 14_817 with Dissolve(1)
    ir "Mmm..."
    scene 14_818 with vpunch
    ir "Aaah!"
    mc "Let's switch it up. The floor's a little hard."
    ir "It's not the only thing that is!"
    mc "Heh..."
    ir "So, what are you thinking?"
    mc "You'll find out."
    scene 14_819 with Dissolve(1)
    ""
    scene 14_820 with Dissolve(1)
    ""
    scene 14_821 with vpunch
    ir "Aah-haha."
    mc "{i}(Maybe I went a bit too hard there.){/i}"
    mc "{i}(Hope I didn't dent the car.){/i}"
    scene 14_822 with Dissolve(1)
    ""
    scene 14_823 with Dissolve(1)
    mc "{i}(I can't get enough of her.){/i}"
    mc "{i}(Never could!){/i}"
    scene 14_824 with Dissolve(1)
    ir "Mmm..."
    scene 14_825 with Dissolve(1)
    ""
    scene 14_826 with Dissolve(1)
    mc "Let's ditch these. You said you wanted to change anyway, right?"
    ir "As if that's the only reason you want to get them off..."
    mc "Haha. I could give you a dozen reasons, but I'd rather just keep going."
    ir "I'm not stopping you!"
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 14_827 at moveup
    pause 3
    ir "..."
    scene 14_828 with Dissolve(1)
    ""
    scene 14_829 with Dissolve(1)
    ir "Mmm... Getting a second round?"
    mc "Don't you always get what you want?"
    ir "Most of the time..."
    scene 14_830 with Dissolve(1)
    ir "But not always..."
    mc "This time you do!"
    ir "..."
    scene 14_831 with Dissolve(1)
    ir "Ahh..."
    scene 14_832 with Dissolve(1)
    ir "*Moaning*"
    scene 14_833 with Dissolve(1)
    ir "Do that thing with your tongue again!"
    scene 14_834 with Dissolve(1)
    ir "Fuck!"
    scene 14_835 with Dissolve(1)
    ir "Nggh... [mc]..."
    scene 14_836 with Dissolve(1)
    mc "{i}(I feel like she's close again.){/i}"
    mc "{i}(She's always been a horny girl, but this horny?){/i}"
    scene 14_837 with Dissolve(1)
    ir "Ahh... Yes!"
    mc "{i}(Here we go...){/i}"
    scene 14_838 with Dissolve(1)
    mc "{i}(She looks satisfied.){/i}"
    scene 14_839 with Dissolve(1)
    mc "Up for round three?"
    ir "With you? Always!"
    scene 14_840 with Dissolve(1)
    mc "..."
    show 14_841
    ""
    scene 14_842 with Dissolve(1)
    ir "..."
    mc "Haha. I know, I know."
    scene 14_843 with Dissolve(1)
    ""
    scene 14_844 with Dissolve(1)
    mc "This feels so good."
    mc "Your pussy is amazing, Iris!"
    scene 14_845 with Dissolve(1)
    ir "Ah, [mc]..."
    scene 14_846 with Dissolve(1)
    mc "You good?"
    ir "Yeah... Don't put it in so fast!"
    ir "Give me time to adjust."
    mc "Sorry. Can I...?"
    ir "Yeah, I'm good now. Fuck me hard!"
    show 14_847
    ""
    show 14_848
    ""
    show 14_849
    ir "Yes, baby!"
    scene 14_850 with Dissolve(1)
    ir "*Moaning*"
    scene 14_851 with Dissolve(1)
    ""
    show 14_852
    ""
    scene 14_853 with Dissolve(1)
    mc "Turn around!"
    ir "..."
    if Cara_Week5_Saturday_Anal == False:
        pass
    else:
        scene 14_855 with Dissolve(1)
        mc "You know what we never did?"
        ir "What's that?"
        mc "Anal."
        ir "That's not gonna happen today!"
        scene 14_854 with Dissolve(1)
        mc "Not today? You mean we could? Some other time?"
        ir "If you want to try, we can. But not today, not here."
    scene 14_856 with Dissolve(1)
    ir "Aah..."
    scene 14_857 with Dissolve(1)
    ""
    scene 14_858 with Dissolve(1)
    ir "Mmm..."
    show 14_859
    ""
    show 14_860
    mc "I'm about to..."
    mc "Can I... inside?"
    ir "Yes."
    scene 14_861 with vpunch
    pause 2
    scene 14_861 with vpunch
    mc "Fuck!"
    ir "Ahh..."
    scene black with Dissolve(1)
    pause 2
    scene 14_862 with Dissolve(1)
    n "*Heavy breathing*"
    scene 14_863 with Dissolve(1)
    $ achievement.grant("ACHIEVEMENT_GREASY")
    $ achievement.sync()
    mc "I didn't expect this when I came over."
    ir "I'm glad it happened!"
    mc "*Nods*"
    mc "When I'm with you, I should be ready for anything."
    ir "You should know that by now!"
    mc "I should..."
    scene 14_864 with Dissolve(1)
    mc "Whose car is this?"
    ir "I don't know."
    mc "You should bill them for 'extra' services!"
    ir "Haha."
    scene 14_865 with Dissolve(1)
    ir "..."
    mc "..."
    scene 14_866 with Dissolve(1)
    mc "{i}(I still like this girl so very much.){/i}"
    mc "{i}(Maybe even...){/i}"
    scene 14_867 with Dissolve(1)
    mc "..."
    scene 14_868 with Dissolve(1)
    mc "{i}(I think I do.){/i}"
    scene 14_869 with Dissolve(1)
    mc "{i}(Even this kiss feels different than before...){/i}"
    scene 14_870 with Dissolve(1)
    mc "{i}(What should I do?){/i}"
    mc "{i}(Get back together with her?){/i}"
    scene 14_871 with Dissolve(1)
    mc "Why do we always have sex in your dad's garage?"
    ir "Haha... We do, don't we?"
    ir "Maybe it's the thrill of getting caught?"
    mc "I don't want your dad catching us!"
    ir "Me neither. Let's pick somewhere else next time."
    scene 14_872 with Dissolve(1)
    ir "Remember, you promised to spend some time with me!"
    ir "You still owe me a date, and this doesn't count."
    mc "I know."
    mc "Let's finish your bike so we can ride somewhere together this week or next."
    scene 14_873 with Dissolve(1)
    ir "This was amazing, by the way!"
    mc "..."
    ir "Thank you!"
    ir "Next time, I'll treat you!"
    scene 14_874 with Dissolve(1)
    ""
    scene 14_875 with Dissolve(1)
    ir "I'll go change now."
    mc "Don't forget your panties this time!"
    ir "I'm gonna wear jeans, no need for panties."
    mc "Heh..."
    scene 14_876 with Dissolve(1)
    mc "Hey! Put some clothes on first before you go!"
    ir "Why? I'll have to take them off again anyway."
    mc "What if someone sees you like this?"
    ir "I don't care..."
    scene 14_877 with Dissolve(1)
    mc "I know you don't, but..."
    ir "But what?"
    menu:
        "Nothing":
            mc "Nothing... Just go."
            ir "..."
            scene 14_878 with Dissolve(1)
            ir "Okay..."
            mc "*Shakes head*"
        "I care[KoGa3AutoWTChange1]{size=-4}(Iris Points+2) {/size} {/color}":
            $ Iris_Points += 2
            # Iris_Points = 6
            scene 14_879 with Dissolve(1)
            mc "I care!"
            mc "I don't want anyone else seeing you like this!"
            ir "..."
            scene 14_880 with Dissolve(1)
            ir "Okay..."
            ir "But only for you!"
            scene 14_881 with Dissolve(1)
            ""
            scene 14_882 with Dissolve(1)
            ir "Better?"
            mc "*Nods*"
            ir "Be right back, then!"
    scene 14_883 with Dissolve(1)
    mc "{i}(This girl...){/i}"
    mc "{i}(She still has me wrapped around her finger...){/i}"
    $ renpy.end_replay()
    scene black with Dissolve(1)
    pause 2
    scene 14_884 with Dissolve(1)
    ir "I'm back!"
    ir "Ready to get to work!"
    mc "Great!"
    scene 14_885 with Dissolve(1)
    ir "What?"
    mc "Hmm?"
    ir "Why are you looking at me like that?"
    mc "Just... Admiring your shirt."
    scene 14_886 with Dissolve(1)
    mc "Though I'm not sure if we can still call it a shirt. It's on its way to becoming rags."
    ir "Haha!"
    ir "Hey, this thing's been with me for years."
    mc "Yeah, I can tell."
    jump Week6_Monday_Garage_BikeRepair

label Week6_Monday_Garage_BikeRepair:
    scene black with Dissolve(1)
    pause 2
    scene 14_887 with Dissolve(1)
    ""
    scene 14_888 with Dissolve(1)
    ir "*Humming*"
    scene 14_889 with Dissolve(1)
    mc "..."
    mc "{i}(She looks happy.){/i}"
    scene 14_890 with Dissolve(1)
    mc "You look happy!"
    ir "I am!"
    ir "I missed this more than I thought."
    ir "Feels just like back then, right?"
    scene 14_891 with Dissolve(1)
    ir "The two of us in Dad's garage... working on my bike."
    mc "Mm-hmm."
    mc "Except you were the one working on it, I was cleaning it."
    ir "That's because I was the one riding you everywhere. You had to keep it clean!"
    scene 14_892 with Dissolve(1)
    mc "Only for the first month or so."
    mc "Once I learned how to ride, I was the one who was riding you everywhere!"
    ir "I love the way you say that. Riding me..."
    scene 14_893 with Dissolve(1)
    mc "Iris..."
    ir "Haha."
    if Iris_Week6_Monday_Garage_Sex == True:
        mc "We just did it!"
        ir "Once..."
        mc "*Shakes head*"
    else:
        pass
    scene black with Dissolve(1)
    pause 2
    scene 14_894 with Dissolve(1)
    mc "Alright, I'm done here."
    mc "What's next?"
    ir "You can help me with the front suspension and wheel. That's all that's left."
    mc "Okay."
    scene black with Dissolve(1)
    pause 2
    scene 14_895 with Dissolve(1)
    mc "I'll tighten this bolt, and we're good."
    ir "..."
    scene 14_896 with Dissolve(1)
    ir "Thanks!"
    scene 14_897 with Dissolve(1)
    ir "Be right back."
    mc "Changing again?"
    ir "No. Getting my gorgeous helper something to drink."
    mc "Haha, thanks."
    scene 14_898 with Dissolve(1)
    ""
    scene 14_899 with Dissolve(1)
    ir "Here you go!"
    ir "Water okay?"
    mc "Perfect. Thanks, Iris."
    if Iris_Points >= 5:
        scene 14_900 with Dissolve(1)
        ir "..."
        scene 14_901 with Dissolve(1)
        mc "Mmm?"
        ir "Thanks."
        scene 14_902 with Dissolve(1)
        mc "{i}(No...){/i}"
        mc "{i}(Don't start thinking about that now!){/i}"
    else:
        pass
    scene 14_903 with Dissolve(1)
    mc "Nggh..."
    mc "That was exactly what I needed!"
    ir "The water?"
    mc "That too."
    scene 14_904 with Dissolve(1)
    mc "I meant coming here and working on your bike. Thanks."
    ir "I'm the one who should thank you!"
    ir "This would've taken me days, alone."
    mc "You're welcome. It was nice to just work and not think about the expulsion."
    scene 14_905 with Dissolve(1)
    ir "Expulsion? I thought you were suspended?"
    mc "I meant suspension! Why do I keep saying that I'm expelled...?"
    ir "Maybe you're foreshadowing?"
    mc "Hope not!"
    scene 14_906 with Dissolve(1)
    mc "Mom took the suspension news better than I expected."
    mc "*Sigh*"
    mc "I don't want to imagine if I actually got expelled."
    scene 14_907 with Dissolve(1)
    ir "If it ever happens, and knock on wood it won't, I'm sure I can get you a job here!"
    mc "Haha, thanks."
    ir "But let's try to stay in school!"
    mc "I will."
    scene 14_908 with Dissolve(1)
    jo "Hi, guys."
    mc "Oh hey, John!"
    ir "Hey, Dad."
    scene 14_909 with Dissolve(1)
    jo "How are you doing, [mc]?"
    mc "Uh... good, yeah."
    mc "What about you?"
    jo "No complaints."
    scene 14_910 with Dissolve(1)
    jo "No school today?"
    mc "Nah... Took a few days off."
    jo "You can just take days off now? Times really have changed since I was in school."
    ir "Haha, Dad... He's suspended."
    scene 14_911 with Dissolve(1)
    jo "Suspended? What happened?"
    ir "He punched some asshole in the face!"
    if Zach_Week6_Monday_Punch == False:
        mc "I didn't punch him..."
        ir "Well, you should've! That guy deserved it and more!"
    else:
        mc "More like self-defence, really."
    mc "Official reason? Fighting at school."
    scene 14_912 with Dissolve(1)
    jo "Hmm... Happens sometimes, right?"
    mc "Yeah..."
    jo "How long's the suspension?"
    mc "Three days."
    jo "Oh, that's not too bad."
    scene 14_913 with Dissolve(1)
    mc "Still bad timing though."
    mc "We've got a relay race this weekend. I can't train with the team, now."
    jo "That sucks. Maybe you can train after school hours?"
    mc "I'm thinking about it. If they still let me compete, that is."
    scene 14_914 with Dissolve(1)
    jo "You're suspended, not expelled. Shouldn't be a problem."
    ir "I told [mc] already. If he ever gets expelled, he can work here! For us!"
    jo "'For us', huh?"
    ir "Yes! For us!"
    scene 14_915 with Dissolve(1)
    jo "Haha, well then, you'd better stay in school."
    jo "You don't want to work for this one!"
    ir "HEY!"
    mc "Haha. I already did today, and I had fun."
    ir "See? I'm fun!"
    scene 14_916 with Dissolve(1)
    jo "I never denied that."
    ir "And a lot of other things!"
    jo "I don't want to hear about those!"
    mc "{i}(No, you don't.){/i}"
    scene 14_917 with Dissolve(1)
    mc "We fixed up her bike."
    jo "Nice! Did you get the stator swapped out?"
    mc "Yep. No trouble there."
    scene 14_918 with Dissolve(1)
    jo "Maybe you should come work for me."
    ir "Us!"
    jo "For us... I've got room for an apprentice."
    jo "But seriously. Don't get expelled. Go to college!"
    mc "That's the plan."
    scene 14_919 with Dissolve(1)
    mc "Speaking of apprenticeships..."
    mc "I was in Alvarado last weekend and met up with Nathan."
    mc "He's not planning on college and might be looking for an apprenticeship at a garage."
    mc "I told him you're in Madison Springs now and suggested he reach out."
    scene 14_920 with Dissolve(1)
    jo "He's willing to move here?"
    mc "More than willing, honestly."
    jo "Tell him to contact me."
    mc "He's planning a visit, maybe this week, more likely next. We'll stop by."
    jo "Perfect. We'll have a proper chat then."
    scene 14_921 with Dissolve(1)
    ir "Nate might move here too?"
    mc "Maybe, yeah."
    ir "Awesome. You could use some more guy friends around. You keep punching the local ones."
    if Zach_Week6_Monday_Punch == False:
        mc "I didn't punch him!"
        ir "Haha. It's a better story."
    else:
        mc "Very funny!"
        ir "Haha."
    if MC_Bike == True:
        scene 14_922 with Dissolve(1)
        jo "I saw your bike outside. What happened to it?"
        mc "Oh yeah... Uhm..."
        ir "Wait? Something happened to your bike?"
        scene 14_923 with Dissolve(1)
        jo "It's dented and scratched all along one side. Did it fall over or something?"
        mc "Not exactly. Someone pushed it over."
        jo "What? Are you serious?"
        scene 14_924 with Dissolve(1)
        mc "Yeah. Right after I got suspended... When I got to the parking lot, it was already on the ground."
        jo "Any idea who did it?"
        mc "I've got a pretty good guess..."
        ir "It was that jerk you punched, wasn't it? He was suspended too, and left before you."
        mc "Probably him, yeah."
        scene 14_925 with Dissolve(1)
        jo "Did you report it to the school?"
        mc "Not yet. Mom mentioned that too. Maybe a security camera caught something."
        scene 14_926 with Dissolve(1)
        mc "*Sigh* I'm really sorry, John."
        mc "You trusted me with that bike, and I messed it up within days..."
        scene 14_927 with Dissolve(1)
        jo "Hey! First of all, it's not your fault."
        jo "Secondly... It's just a bike. Scratches and dents are part of the ride. Do you think I kept all my bikes spotless?"
        mc "Pretty much, yes!"
        scene 14_928 with Dissolve(1)
        jo "I have a garage for a reason!"
        mc "Heh..."
        mc "Can it be fixed?"
        jo "Let's take a look at it together. Come on."
        scene 14_929 with Dissolve(1)
        ""
        scene 14_930 with Dissolve(1)
        jo "Okay... the dents along the side panel aren't deep, just cosmetic. A body shop can hammer those out easily."
        jo "Now this scratch here? See it catches the light? That's into the primer."
        jo "We'll need to sand it down, level it, and give it a fresh coat."
        mc "Would it be better to repaint the whole thing?"
        jo "Definitely. Matching matte finishes is tough, especially with age and wear. Repainting the entire surface will make it look brand new and seamless."
        scene 14_931 with Dissolve(1)
        jo "When can you bring the bike in?"
        mc "I'll probably need it for the next couple of days... But I can drop it off before the weekend."
        jo "If you bring it in on Friday, I can take care of the scratches, then send it to the body shop for the dents and repainting. Should be ready by Saturday."
        mc "Actually, if I'm cleared to race in the relay, I'll be gone Friday. I could bring it in Thursday, instead."
        jo "That works just as well."
        scene 14_932 with Dissolve(1)
        jo "Don't worry. We'll get it looking better than ever."
        jo "And hey! Since we're repainting anyway, now's your chance to make it yours. Pick any colour you like."
        mc "I like the matte finish but I'll think on it. Thanks again, John."
        ir "I vote red!"
        mc "Red might not be a bad idea..."
    else:
        pass
    scene black with Dissolve(1)
    pause 2
    scene 14_933 with Dissolve(1)
    mc "Actually, John, the main reason I came by..."
    mc "I wanted to ask if you might have some time today or tomorrow to take a look at my mom's car."
    jo "What's going on with it?"
    mc "No idea. It was running fine until this morning, then just wouldn't start. Kept stalling every time."
    jo "Hmm..."
    scene 14_934 with Dissolve(1)
    mc "I gave it a quick look. Checked a few cables, made sure nothing was loose, but I couldn't spot anything obvious."
    jo "Could be anything. Might be something simple, or it could be more serious."
    scene 14_935 with Dissolve(1)
    jo "I've got some paperwork to finish, but I can swing by in an hour or two. That work?"
    mc "Yeah, that'd be perfect. Thanks a lot."
    jo "Alright, I'll get started now. See you later."
    mc "Cool."
    scene 14_936 with Dissolve(1)
    mc "Guess I'll head home too, then."
    ir "Already?"
    mc "What do you mean 'already'? I've been here for what? Two hours?"
    ir "..."
    scene 14_937 with Dissolve(1)
    ir "You can go... but only if I get a big, long hug!"
    mc "Deal."
    scene 14_938 with Dissolve(1)
    ir "Thank you so much for helping me with my bike!"
    mc "You're welcome. Any time!"
    if Iris_LikeMC == True:
        scene 14_939 with Dissolve(1)
        ir "..."
        scene 14_940 with Dissolve(1)
        mc "..."
        mc "{i}(She used to do that all the time!){/i}"
        scene 14_941 with Dissolve(1)
        ir "Aaah!"
        mc "You wanted a big long hug!"
        ir "I'm not complaining... Just wasn't expecting the full bear-hug treatment!"
        if Erynn_LikeMC == False:
            pass
        else:
            mc "{i}(Bear-hug... Erynn would say the same thing...){/i}"
        scene 14_942 with Dissolve(1)
        ir "..."
        if Alexis_Dating == False:
            scene 14_943 with Dissolve(1)
            ""
            scene 14_944 with Dissolve(1)
            ""
        else:
            scene 14_945 with Dissolve(1)
            mc "..."
            scene 14_946 with Dissolve(1)
            mc "Uh, Iris..."
            ir "I couldn't help myself."
            ir "Don't worry. You didn't cheat on Alexis. I kissed you!"
            ir "Besides... You're cheating on me with Alexis, remember?"
            mc "Heh..."
            scene 14_947 with Dissolve(1)
            ir "..."
            menu:
                "Kiss Iris[KoGa3AutoWTChange1]{size=-4}(Iris Week6 Monday CheatKiss, Iris Points+2) {/size} {/color}":
                    $ Iris_Week6_Monday_CheatKiss = True
                    $ Iris_Points += 2
                    scene 14_948 with Dissolve(1)
                    ir "Mmm..."
                    scene 14_949 with Dissolve(1)
                    ""
                    scene 14_950 with Dissolve(1)
                    mc "I couldn't help myself."
                    ir "Don't cheat!"
                    mc "Technically, I wasn't! And didn't you kiss me back?"
                    ir "*Shakes head*"
                "Put her back down":
                    pass
        scene 14_951 with Dissolve(1)
        ir "One more hug!"
        ir "Next time, let's take a bike ride. Explore a little around Madison Springs."
        ir "I haven't done that yet. There must be a lake nearby, right?"
        mc "Haha."
    else:
        pass
    scene 14_952 with Dissolve(1)
    mc "Bye, Iris. See you next time!"
    ir "Bye, [mc]."
    ir "..."
    scene 14_953 with Dissolve(1)
    ir "Hey, sexy!"
    mc "Mmm?"
    ir "Aren't you forgetting something?"
    mc "Right... My t-shirt."
    scene 14_954 with Dissolve(1)
    mc "Thanks!"
    if Iris_LikeMC == True:
        scene 14_955 with Dissolve(1)
        ir "Daddy!"
        jo "*Sigh* What?"
        scene 14_956 with Dissolve(1)
        jo "What, Iris?"
        ir "..."
        jo "Just ask him!"
        ir "*Deep sigh*"
    else:
        pass
    jump Week6_Monday_Afternoon_Home

label Week6_Monday_Afternoon_Home:
    scene black with Dissolve(2)
    pause 2
    stop music fadeout 1.0
    play music ("Music/LoFi Indie 3.mp3", "Music/LoFi Indie 1.mp3", "Music/LoFi Indie 2.mp3") volume 0.2
    scene 14_957 with Dissolve(1)
    ""
    scene 14_958 with Dissolve(1)
    mc "{i}(Huh? Why is my phone off?){/i}"
    mc "{i}(Did the battery die...?){/i}"
    if Erynn_Week5_Tuesday_Photoshoot_Join == True:
        scene 14_959 with Dissolve(1)
        mc "{i}(Oh...){/i}"
        mc "{i}(Two missed calls from Erynn.){/i}"
        mc "{i}(Did something happen?){/i}"
        mc "{i}(No way she knows about my suspension yet...){/i}"
        mc "{i}(Got some messages too. But let's call her first.){/i}"
        scene 14_960 with Dissolve(1)
        mc "{i}(Is she home now? Or still at MSU?){/i}"
        mc "..."
        er "Hey!"
        scene 14_961 with Dissolve(1)
        mc "Hi, Erynn. How are you?"
        er "I'm good. How about you?"
        mc "Good, good."
        mc "{i}(Yeah... She definitely doesn't know about the suspension. She'd have opened with that.){/i}"
        scene 14_962 with Dissolve(1)
        mc "So, why'd you call? Did something happen?"
        er "Hmm? No, no, everything's fine."
        mc "{i}(Lately, every time she calls, I brace for bad news... I really hope this Ethan crap ends soon.){/i}"
        er "Just wanted to know if you're home."
        mc "Why? Want to come over?"
        er "I can't today. I'm at the apartment now, but heading out soon for some appointments."
        scene 14_963 with Dissolve(1)
        er "Are you home yet?"
        mc "Why do you want to know that?"
        er "No reason... Just asking..."
        mc "{i}(She's definitely fishing about the poster. Wants to know my reaction.){/i}"
        mc "{i}(Heh. Let's let her squirm a little.){/i}"
        scene 14_964 with Dissolve(1)
        er "Call me when you get home!"
        mc "Why so eager to know when I'm home?"
        er "Just do it!"
        mc "Haha. Okay, okay."
        scene 14_965 with Dissolve(1)
        er "Talk to you later, then."
        if Erynn_LikeMC == False:
            mc "Alright. Bye, Erynn."
            er "Bye-bye."
        else:
            mc "Alright. Bye, Rinny."
            er "Heh... Bye-bye."
            scene 14_966 with Dissolve(1)
            er "..."
            scene 14_967 with Dissolve(1)
            er "Why aren't you home yet!"
    else:
        pass
    if Layla_End == True:
        pass
    else:
        if Layla_Dating == False:
            if Layla_Week5_Wednesday_BreakUp == True:
                scene 14_968 with Dissolve(1)
                mc "{i}(Elena texted me.){/i}"
                mc "{i}(I wanted to talk to her today, but with the suspension...){/i}"
                el "{i}(Hey. You and Zach got suspended? What happened?){/i}"
                el "{i}(Tori said you fought in the hallway. Not sure if that's true or if she was just running her mouth again.){/i}"
                scene 14_969 with Dissolve(1)
                mc "{i}(Hey, Elena. Yeah, it's true.){/i}"
                mc "{i}(I'll tell you the whole story next time.){/i}"
                mc "{i}(Sorry I couldn't meet you after school.){/i}"
                mc "{i}(Can we meet up another time? I really want to talk. Let me know.){/i}"
                scene 14_970 with Dissolve(1)
                mc "*Sigh*"
                mc "{i}(I was really looking forward to going back to school.){/i}"
                mc "{i}(Seeing Elena... Training with the team... Maybe making up with Layla...){/i}"
                mc "{i}(And now this shit!){/i}"
            else:
                scene 14_968 with Dissolve(1)
                mc "{i}(Got a few texts from Layla.){/i}"
                la "{i}(Aren't you coming back?){/i}"
                la "{i}(What happened?){/i}"
                la "{i}(Tori's saying you fought with Zach in the hallway. Is that true?){/i}"
                la "{i}(You're suspended?){/i}"
                la "{i}([mc]?){/i}"
                scene 14_969 with Dissolve(1)
                mc "{i}(Hey, Layla. Yes, it's true.){/i}"
                mc "{i}(I'll tell you the whole story next time.){/i}"
                scene 14_970 with Dissolve(1)
                mc "*Sigh*"
                mc "{i}(I was really looking forward to going back to school.){/i}"
                mc "{i}(And now this shit!){/i}"
        else:
            scene 14_968 with Dissolve(1)
            mc "{i}(Got a few texts from Layla.){/i}"
            la "{i}(Aren't you coming back?){/i}"
            la "{i}(What happened?){/i}"
            la "{i}(Tori's saying you fought with Zach in the hallway. Is that true?){/i}"
            la "{i}(You're suspended?){/i}"
            la "{i}([mc]?){/i}"
            scene 14_971 with Dissolve(1)
            mc "{i}(Let's call her.){/i}"
            mc "{i}(She must be back home by now.){/i}"
            scene 14_972 with Dissolve(1)
            la "Hey!"
            mc "Hey, Layla."
            la "Are you okay?"
            mc "Yeah..."
            scene 14_973 with Dissolve(1)
            mc "You know already, huh?"
            la "Tori said you fought Zach in the hallway. I didn't believe her at first, but when you didn't come back to class..."
            la "I asked Mom, and she said you got suspended."
            mc "Mm-hmm..."
            la "What happened?"
            scene 14_974 with Dissolve(1)
            mc "Well..."
            la "Wait! Can I put you on speaker?"
            la "Elena's here too and wants to know."
            mc "Uh, sure..."
            scene 14_975 with Dissolve(1)
            el "Hey, bad boy!"
            mc "Hi, Elena."
            el "Ya sabía que esto iba a pasar.\n(I knew this would happen at some point.)"
            el "Pero yo pensaba que iba a ser yo quien le partiera la cara!\n(But I thought I would be the one to kick his ass!)"
            mc "Haha. You're welcome. Thanks for making me laugh."
            scene 14_976 with Dissolve(1)
            mc "It started before spring break."
            mc "Zach invited me to a show."
            mc "On the way, we ran into Ethan. You might know who he is."
            la "I've heard about him from Alexis."
            scene black with Dissolve(1)
            pause 2
            scene 14_977 with Dissolve(1)
            la "Why didn't you tell us sooner?"
            mc "I just... didn't want to get anyone involved. *Sigh* Sorry."
            la "I can't believe he actually hit you like that!"
            el "Yeah, no way I'm ever talking to that guy again."
            scene 14_978 with Dissolve(1)
            mc "And then today... I ran into Zach in the hallway."
            mc "He acted like everything was fine... No apology, no nothing."
            mc "So I tried to avoid him and head to class."
            scene 14_979 with Dissolve(1)
            mc "But he stopped me a few times and we started arguing."
            mc "Then suddenly, he threw the first punch."
            la "What?!"
            mc "And it wasn't just one punch..."
            if Zach_Week6_Monday_Punch == True:
                scene 14_980 with Dissolve(1)
                mc "I'd had enough."
                mc "So I punched back to defend myself, and he went down."
                mc "Right then the teacher showed up and broke it up."
            else:
                scene 14_981 with Dissolve(1)
                mc "I was trying to avoid getting hit."
                mc "So I pushed him away, and he lost his balance and fell."
                mc "That's when the teacher stepped in and ended it."
                scene 14_982 with Dissolve(1)
                la "You didn't punch him? Then why the suspension?"
                la "Did you tell Mom you only pushed him?"
                mc "Yeah, but the teacher said otherwise..."
                scene 14_983 with Dissolve(1)
                la "Which teacher was it?"
                mc "Ramirez. She was the one who stopped the fight."
                la "Ugh, that's why I don't like her. That lying bitch!"
                mc "{i}(Haha, Layla...){/i}"
                scene 14_984 with Dissolve(1)
                la "I'm gonna talk to Mom again and clear things up."
                mc "No, there's nothing to be done, now."
                la "Are you sure? I can try..."
                mc "I'm sure. And I don't want you to get involved in this, either. But thanks."
            scene 14_985 with Dissolve(1)
            la "How long are you suspended for?"
            mc "Three days. Until Friday."
            la "Until Friday? What about the relay tournament and training?"
            mc "I'm not sure. I don't know if I'll still be allowed to participate."
            la "I'll ask Coach tomorrow and let you know what's going on."
            mc "Thanks, Layla."
            scene 14_986 with Dissolve(1)
            la "And we can train together after school like before."
            mc "Yeah, maybe we can find a stick in the park."
            la "Haha, sounds like a plan."
            scene 14_987 with Dissolve(1)
            la "So, what are your plans for the next few days?"
            mc "I don't know yet. Mom might have me work some shifts at the restaurant."
            mc "Or I'll hit the gym and train on my own."
            mc "Or maybe just relax..."
            scene 14_988 with Dissolve(1)
            la "Now I kinda wish *I* was suspended..."
            la "Could use some free time, too."
            mc "Really? With your mom being the principal?"
            la "Hmm... Yeah, maybe that's not such a good idea."
            mc "Probably not."
            scene 14_989 with Dissolve(1)
            la "Looks like it'll be just me and Elena for the next few days."
            el "Finally!"
            el "It took long enough to get rid of you."
            mc "Haha, Elena! Love you too!"
            scene 14_990 with Dissolve(1)
            mc "Well... Enjoy your time without me, then!"
            el "We will!"
            mc "Haha. Bye, Elena! Bye, Layla. Talk to you tomorrow."
            el "Bye..."
            la "Bye, [mc]. I'll keep you updated about the relay."
            mc "Thanks."
            scene 14_991 with Dissolve(1)
            mc "*Sigh*"
            mc "They always know how to make me smile."
            play sound "Sounds/Phone_Message.mp3"
            n "*Bzzzt*"
            mc "{i}(Message?){/i}"
            scene 14_992 with Dissolve(1)
            mc "Haha. These two."
            if Elena_LikeMC == True:
                scene 14_993 with Dissolve(1)
                mc "{i}(If you're trying to make me jealous...){/i}"
                mc "{i}(You'll have to kiss for real!){/i}"
                scene 14_994 with Dissolve(1)
                play sound "Sounds/Phone_Message.mp3"
                n "*Bzzzt*"
                mc "No way!"
                scene 14_995 with Dissolve(1)
                mc "I didn't expect them to actually do it."
                mc "Is this for real?"
                scene 14_996 with Dissolve(1)
                el "Haha. He's calling again."
                la "He wants to FaceTime. Pick up?"
                el "Sure."
                scene 14_997 with Dissolve(1)
                la "Hey again!"
                mc "Did you kiss for real, or was that some AI filter?"
                el "Haha, no filter here!"
                scene 14_998 with Dissolve(1)
                la "We kissed for real!"
                mc "No way!"
                la "Haha, yes way!"
                mc "Then prove it! Do it again!"
                la "Fine!"
                scene 14_999 with Dissolve(1)
                mc "Oh shit!"
                scene 14_1000 with Dissolve(1)
                zo "..."
                zo "Sorry, I didn't know anyone was here."
                scene 14_1001 with Dissolve(1)
                la "DAD!"
                zo "Sorry for interrupting... Please, continue..."
                la "NO, DAD!"
                scene 14_1002 with Dissolve(1)
                la "I can explain!"
                zo "No need."
                la "It was a joke! We were just trying to make [mc] jealous!"
                scene 14_1003 with Dissolve(1)
                zo "ADRIANA!"
                la "NOOO! DAD!"
                la "WAIT!"
                scene 14_1004 with Dissolve(1)
                la "DAD! LISTEN!"
                zo "Haha."
                scene 14_1005 with Dissolve(1)
                mc "Why is the screen black?"
                mc "What's going on?"
                mc "Hello?"
                scene 14_1006 with Dissolve(1)
                el "Hey!"
                mc "Hey... What happened? I just heard screaming and..."
                el "Well... Layla's dad saw us kissing... Now she's running after him to explain."
                mc "What? Haha."
                scene 14_1007 with Dissolve(1)
                la "STOP!"
                zo "I'm just heading back inside!"
                la "No, you're not! You're going to tell Mom!"
                scene 14_1008 with Dissolve(1)
                zo "What are you trying to accomplish here?"
                la "..."
                scene 14_1009 with Dissolve(1)
                la "AAAH!"
                zo "It's hot today, right?"
                zo "How about some cooling off?"
                scene 14_1010 with Dissolve(1)
                la "DAD!"
                la "No! Don't you dare!"
                la "I'm gonna tell Mom!"
                zo "Okay-okay... You win!"
                la "Now put me down!"
                scene 14_1011 with Dissolve(1)
                la "DAAAAD!"
                scene 14_1012 with Dissolve(1)
                mc "Was that Layla again?"
                el "Yeah. She just got thrown into the pool."
                mc "Haha, really? I wish I'd seen that."
                scene 14_1013 with Dissolve(1)
                el "I'm gonna go help her."
                mc "Do that!"
                mc "I'm gonna do... Something... I don't know."
                el "Heh..."
                scene 14_1014 with Dissolve(1)
                el "See you... Uhm... Friday, I guess!"
                mc "Thanks for reminding me!"
                el "Any time!"
                scene 14_1015 with Dissolve(1)
                mc "Next time we're gonna talk about that kiss!"
                mc "Along with the one on the train! Oh, and the hot tub! We can compare!"
                el "No, we're not! And we won't!"
                mc "Haha. We'll see. Bye, Elena."
                el "Bye, [mc]..."
                scene 14_1016 with Dissolve(1)
                mc "*Shakes head*"
                mc "{i}(I wish I was there right now, with them...){/i}"
            else:
                pass
    if Alexis_Dating == False:
        pass
    else:
        scene 14_1017 with Dissolve(1)
        play sound "Sounds/Phone_Vibrate.mp3"
        n "*Bzzzt. Bzzzt*"
        mc "{i}(Lexi is calling...){/i}"
        mc "{i}(She probably heard the news already.){/i}"
        mc "{i}(Before I tell her, I'll mess with her a little. Sorry, Lexi!){/i}"
        mc "{i}(But she always makes me laugh, and I need that now.){/i}"
        scene 14_1018 with Dissolve(1)
        mc "Hello?"
        a "Hello? What do you mean hello?"
        mc "Oh hey, Lexi. How are you?"
        a "No-no-no. What did you mean by 'hello' with a question mark?"
        mc "It was an unknown number, so..."
        scene 14_1019 with Dissolve(1)
        a "Why am I an unknown number? Don't you have my number saved?"
        mc "{i}(Lexi's so easy to rile.){/i}"
        mc "Haha, I'm just kidding! Of course I have your number saved!"
        a "..."
        a "Are you sure? Under what name?"
        scene 14_1020 with Dissolve(1)
        mc "Lexi."
        a "Just 'Lexi'?"
        mc "Yeah... What? Want me to put your full name? Alexis Monroe?"
        a "No... At least it's not 'Girl #7', I guess."
        mc "Haha. You remember that, huh?"
        a "I do. But maybe you could change it to 'girlfriend' or add a heart or something!"
        scene 14_1021 with Dissolve(1)
        mc "How about 'darling'?"
        a "No, not darling!"
        mc "Haha."
        a "But that's a good idea. I'll change yours to that."
        mc "Haha. What is it now?"
        scene 14_1022 with Dissolve(1)
        a "'Boyfriend' with your name in brackets."
        mc "Why my name behind it? Do you have multiple boyfriends?"
        mc "Boyfriend ([mc]), boyfriend (Sean), boyfriend (Frankie)..."
        scene 14_1023 with Dissolve(1)
        a "Who are Sean and Frankie?"
        mc "I don't know. You tell me!"
        a "Haha."
        a "No, it's just you!"
        scene 14_1024 with Dissolve(1)
        a "Do you want me to change it?"
        mc "{i}(I don't really care, but I'm not saying that. Girls get mad over random stuff like this.){/i}"
        mc "No, it's fine. Want me to change yours?"
        a "..."
        mc "I'll take that as a yes? What do you want me to put?"
        scene 14_1025 with Dissolve(1)
        mc "Girlfriend with Lexi between brackets?"
        a "Okay, that sounds worse the more I think about it."
        a "I'll change mine."
        scene 14_1026 with Dissolve(1)
        a "You know, I used to have you saved as 'Aeroplane-boy'."
        mc "So you not only called me that to Lakeyn but also saved me as that?"
        a "Haha, sorry."
        mc "When did you change it?"
        a "After you dared me to be your girlfriend."
        scene 14_1027 with Dissolve(1)
        mc "I was Aeroplane-boy for that long?"
        a "You still are, in some conversations!"
        mc "Okay, I'm changing yours now!"
        a "What are you changing it to?"
        mc "Not telling you but it starts with a 'B'."
        scene 14_1028 with Dissolve(1)
        a "Bitch?"
        mc "Haha. Really? That's the first word you think of for 'B'?"
        mc "It could be beautiful, you know."
        a "Just keep it as Lexi... I'm good with that."
        mc "Haha. You sure?"
        a "Positive!"
        scene 14_1029 with Dissolve(1)
        gi "Hey, girl."
        a "Hey, Gigi."
        gi "You're early!"
        a "Yeah. I can't make it tomorrow, so I'm putting in a few extra hours today."
        scene 14_1030 with Dissolve(1)
        gi "*Whispers* Who's that on the phone?"
        a "Aeroplane-boy."
        mc "HEY!"
        gi "Oh..."
        scene 14_1031 with Dissolve(1)
        gi "You're still talking to him?"
        a "Mm-hmm."
        gi "Does your boyfriend know?"
        a "He does."
        gi "He does? And he..."
        scene 14_1032 with Dissolve(1)
        gi "Oh! Duh... Aeroplane-boy is the boyfriend."
        a "Correct."
        gi "I'm clearly not awake yet."
        a "Haha. Is that also why you're wearing that t-shirt?"
        scene 14_1033 with Dissolve(1)
        gi "Oh, this?"
        a "Don't tell me Dylan finally talked you into it."
        gi "Nope. Rejected it every time."
        gi "But today I'm asking him for a raise, and I figured... wearing this might give me an edge."
        scene 14_1034 with Dissolve(1)
        a "Haha. Bold move!"
        a "Let me know if it works. I might try the same trick."
        gi "Deal."
        mc "Wait, what t-shirt are we talking about?"
        scene 14_1035 with Dissolve(1)
        a "Gianna's wearing the Dylan's BBQ t-shirt."
        mc "Can I see it?"
        a "Hang on..."
        a "Hey, Gigi, mind if I snap a pic to show [mc] the shirt?"
        gi "Sure!"
        scene 14_1036 with Dissolve(1)
        a "You don't have to pose like that!"
        a "It's just a picture of the t-shirt."
        gi "Still gotta look good!"
        scene 14_1037 with Dissolve(1)
        a "Sent!"
        mc "Mm-hmm. Got it."
        if Gianna_Week5_Thursday_CheckOut == True:
            mc "{i}(Damn Gianna!){/i}"
        else:
            pass
        mc "Why aren't you wearing that t-shirt? It's freakin' awesome!"
        a "Uh-huh..."
        scene 14_1038 with Dissolve(1)
        a "You'd better delete that picture, now!"
        mc "Haha."
        scene 14_1039 with Dissolve(1)
        mc "Think you can hook me up with one of those shirts?"
        a "You seriously want one?"
        mc "Yeah, but the guy version, obviously."
        scene 14_1040 with Dissolve(1)
        gi "Tell him he still owes me a shift."
        gi "He gets a shirt when he pays up!"
        a "You hear that?"
        mc "Yeah, yeah... I'm 'busy' this week, but I'll cover a shift next week for sure!"
        a "He says next week works!"
        gi "He'd better stick to it!"
        scene 14_1041 with Dissolve(1)
        gi "Alright, I'm heading in."
        gi "Time to charm the bossman for that raise."
        a "Good luck!"
        gi "Thanks, I'll need it."
        scene 14_1042 with Dissolve(1)
        a "So, where were we?"
        mc "Uhm... Changing each other's contact names?"
        a "Right... But forget that for now."
        a "There's something else I want to talk about."
        scene 14_1043 with Dissolve(1)
        mc "You already heard, didn't you? I figured that's why you were calling."
        a "There are plenty of reasons I call you, okay?"
        mc "Haha, alright, fair enough."
        mc "So, who told you?"
        scene 14_1044 with Dissolve(1)
        a "Layla called me first. I thought she was joking, so I called my mom to double-check."
        a "She wasn't joking."
        mc "No, she wasn't."
        mc "What did Adriana say?"
        a "That she had to suspend you... because of a fight with Zach?"
        scene 14_1045 with Dissolve(1)
        mc "Wasn't much of a fight."
        if Zach_Week6_Monday_Punch == False:
            mc "He took a swing at me, I pushed him away, and he fell. That's it."
        else:
            mc "He took a swing at me, I defended myself, hit him back, and he fell."
        a "Why were you fighting in the first place? I thought you two were friends?"
        mc "No."
        a "Seriously? What happened? This doesn't sound like it came out of nowhere..."
        scene 14_1046 with Dissolve(1)
        mc "Trust me, it did. The first time he hit me was out of the blue."
        a "The first time?"
        mc "Yeah. That was before spring break."
        scene black with Dissolve(1)
        pause 2
        scene 14_1047 with Dissolve(1)
        a "I can't believe that guy..."
        a "Next time he shows up at the bar, I'm kicking him out."
        mc "Haha. I'd pay to see that."
        scene 14_1048 with Dissolve(1)
        a "*Sigh*"
        a "I'll talk to Mom later, maybe try to explain..."
        mc "No, don't. It's not her fault. She acted on the info she had."
        a "Do you know which teacher told her?"
        mc "I think it was Ramirez. She was the one who stepped in and broke it up."
        scene 14_1049 with Dissolve(1)
        a "Ramirez? The one Layla can't stand?"
        mc "That's the one."
        a "Yeah, I'm thinking of a certain B-word right now."
        mc "Beautiful?"
        a "No! The other one!"
        mc "Haha."
        scene 14_1050 with Dissolve(1)
        a "Hey, do you have time to swing by the bar?"
        a "I want to give you a hug! And some kisses!"
        mc "Heh... I'd love to, but I can't right now."
        mc "Mom's car broke down, and I've got someone coming over to check it out."
        scene 14_1051 with Dissolve(1)
        mc "No clue how long it'll take..."
        a "No worries."
        mc "I might drop by MSU tomorrow, though. Check out campus a bit. Got some unexpected free time now, anyway..."
        a "Yes! Please do!"
        scene 14_1052 with Dissolve(1)
        a "I'm gonna head inside now and start my shift."
        mc "Do that."
        mc "I'll talk to you later or see you tomorrow."
        a "Mm-hmm."
        scene 14_1053 with Dissolve(1)
        a "Love you! Bye, babe."
        mc "Love you too! Bye, another B-word Lexi!"
        a "Bitch, right?"
        mc "This time, yes!"
        a "HEY!"
        scene 14_1054 with Dissolve(1)
        play sound "Sounds/Phone_Message.mp3"
        n "*Bzzzt*"
        mc "What did she send now?"
        scene 14_1055 with Dissolve(1)
        mc "Heh..."
    scene black with Dissolve(1)
    pause 2
    scene 14_1056 with Dissolve(1)
    mc "*Sings* Disarm you with a smile..."
    n "*Ding-dong*"
    mc "*Sings* And cut..."
    scene 14_1057 with Dissolve(1)
    mc "{i}(That must be John.){/i}"
    scene 14_1058 with Dissolve(1)
    ""
    scene 14_1059 with Dissolve(1)
    mc "..."
    mc "Da..."
    scene 14_1060 with Dissolve(1)
    d "Hey, [mc]."
    mc "..."
    d "Can we talk for a minute?"
    scene 14_1061 with Dissolve(1)
    mc "..."
    d "Thanks!"
    d "You look good!"
    d "Did you grow taller?"
    scene 14_1062 with Dissolve(1)
    d "A lot's changed since I was last here."
    d "Is Emily around?"
    mc "No. She's at the restaurant."
    d "Ah. I saw a car outside, thought she might be here too."
    mc "It's hers. It broke down. I'm waiting for a mechanic."
    scene 14_1063 with Dissolve(1)
    d "What's wrong with it?"
    d "I could take a look, if you want."
    mc "It's fine. The mechanic's on their way."
    d "Right... Okay."
    scene 14_1064 with Dissolve(1)
    mc "..."
    scene 14_1065 with Dissolve(1)
    d "..."
    scene 14_1066 with Dissolve(1)
    d "How's your mom?"
    mc "She's good."
    d "And you?"
    mc "Fine."
    d "How's school?"
    mc "Also fine..."
    scene 14_1067 with Dissolve(1)
    d "I see..."
    mc "..."
    scene 14_1068 with Dissolve(1)
    mc "Why are you here?"
    d "I... moved back to Madison Springs."
    mc "What?"
    mc "{i}(I just saw him in Alvarado on Saturday...){/i}"
    mc "When?"
    scene 14_1069 with Dissolve(1)
    d "Officially? Yesterday."
    mc "Yesterday?"
    mc "{i}(Was he on the same flight as me?){/i}"
    mc "Why? What about the woman you were seeing?"
    scene 14_1070 with Dissolve(1)
    d "We broke up a couple of weeks ago."
    mc "{i}(So the woman I saw him with wasn't her...){/i}"
    mc "{i}(Why is he really back?){/i}"
    d "*Sigh*"
    scene 14_1071 with Dissolve(1)
    d "The last few months have been... the worst of my life."
    d "I made a lot of mistakes. And I lost everything that mattered to me."
    d "Especially you."
    d "I just..."
    scene 14_1072 with Dissolve(1)
    d "I'm so sorry, [mc]."
    d "For what I did. For what I said. For everything."
    d "You were the one good thing I had left, and I ruined that too."
    d "You don't have to forgive me now. But I hope you will one day."
    scene 14_1073 with Dissolve(1)
    d "I still love you as a real son!"
    d "No, not like. You are my son. And you always will be."
    mc "..."
    scene 14_1074 with Dissolve(1)
    d "I know it may sound like empty words right now."
    d "But I promise. I'll do whatever it takes to fix our relationship."
    d "Not just with you. With Emily, too."
    mc "{i}(I don't know if that's even possible.){/i}"
    scene 14_1075 with Dissolve(1)
    d "..."
    mc "..."
    scene 14_1076 with Dissolve(1)
    d "Uhm..."
    d "I won't take up more of your time. I know you're expecting the mechanic soon."
    d "But maybe we can talk again sometime?"
    d "I've got a place in the city. I'll text you the address. Come by if you feel like it."
    mc "*Nods*"
    scene 14_1077 with Dissolve(1)
    d "Oh, and I found something while packing up in Alvarado."
    mc "What is it?"
    d "A letter."
    mc "A letter?"
    d "Yeah. It's addressed to you."
    scene 14_1078 with Dissolve(1)
    mc "{i}(Who's it from?){/i}"
    d "I'll let myself out."
    menu:
        "Let Andres leave":
            scene 14_1079 with Dissolve(1)
            d "Bye, [mc]!"
            mc "Bye..."
        "Hug Andres[KoGa3AutoWTChange1]{size=-4}(Andres Week6 Monday Hug, Andres Points+2) {/size} {/color}":
            $ Andres_Week6_Monday_Hug = True
            $ Andres_Points += 2
            scene 14_1079 with Dissolve(1)
            mc "Hey!"
            d "Hmm?"
            scene 14_1080 with Dissolve(1)
            mc "Thanks for coming by."
            d "Thank you for talking to me!"
            d "Thank you, [mc]."
    scene 14_1081 with Dissolve(1)
    mc "*Sigh*"
    mc "What the fuck just happened...?"
    mc "{i}(And what's Mom going to say when she finds out he's back in Madison Springs...?){/i}"
    scene black with Dissolve(1)
    pause 2
    scene 14_1082 with Dissolve(1)
    mc "{i}(Alright... Back to the letter.){/i}"
    mc "{i}(That handwriting... It looks like Erynn's.){/i}"
    mc "{i}(Could this be one of those letters?){/i}"
    mc "{i}(I thought I threw them all away...){/i}"
    menu:
        "Read the letter[KoGa3AutoWTChange1]{size=-4}(Erynn Week6 Monday ReadLetter) {/size} {/color}":
            stop music fadeout 1.0
            play music "Music/Valeria - Emptiness.mp3" volume 0.5
            $ Erynn_Week6_Monday_ReadLetter = True
            scene 14_1084 with Dissolve(1)
            mc "{i}(I've regretted tossing them ever since... So holding one again...){/i}"
            mc "{i}(I don't know. It hits different.){/i}"
            mc "{i}(I'm excited to see what she wrote... but also kind of scared.){/i}"
            scene 14_1085 with Dissolve(1)
            mc "{i}(Some of the ink is smudged...){/i}"
            mc "{i}(Did she cry while writing this?){/i}"
            mc "{i}(My hands are literally shaking right now.){/i}"
            scene 14_1086 with Dissolve(1)
            mc "Hey [mc],"
            mc "I don't even know where to begin, because every time I write to you, my hands tremble and my heart aches a little more."
            mc "It's been days... Weeks... Maybe longer, without you here."
            mc "Everything feels quieter, colder, duller..."
            mc "I miss you. I miss you so much it physically hurts sometimes."
            scene black with Dissolve(1)
            pause 2
            scene 14_1087 with Dissolve(1)
            er "I catch myself checking my phone a hundred times a day, hoping to see your name light up on the screen."
            er "Just one message. One word. One sign that you still think about me, that you haven't forgotten about me."
            er "I haven't forgotten you!"
            scene 14_1088 with Dissolve(1)
            er "I still don't know what happened, or why this silence grew between us. Maybe you need space? Maybe you're hurting?"
            er "I don't want to pressure you or make you feel like you owe me anything... I just... I want to hear from you."
            er "To know that you're okay. To hear your voice, even if it's just for a moment."
            er "To feel like I still exist in the corners of your mind, even if just a little."
            scene 14_1089 with Dissolve(1)
            er "There's so much I want to say, and yet nothing I say feels like enough. No words can really capture how empty it feels not having you here."
            er "I miss your squeaky voice, your mischievous smile, your not-always-funny jokes."
            er "I miss the way you'd say my name. Rinny or Rin-rin."
            er "I miss... Us..."
            er "I don't even know if that us still exists anymore."
            scene 14_1090 with Dissolve(1)
            er "If there's even the smallest part of you that thinks of me... Please, reach out!"
            er "Even if it's just to say you're okay. Even if it's not what I want to hear."
            er "Even if it's just the word hello."
            er "The silence is the hardest part. Please give me something to hold on to."
            scene black with Dissolve(2)
            pause 1
            scene 14_1091 with Dissolve(1)
            mc "Take care of yourself. Please! I'll always be here."
            mc "Your Rinny."
            scene 14_1092 with Dissolve(1)
            mc "{i}(Damn...){/i}"
            mc "{i}(I didn't expect a letter to hit me this hard...){/i}"
            scene 14_1093 with Dissolve(1)
            mc "{i}(Fuck man... Why didn't I read them when I had the chance?){/i}"
            mc "{i}(If I had just known how much you were hurting too.){/i}"
            mc "{i}(I was so wrapped up in my own anger. I was such a little shit.){/i}"
            scene 14_1094 with Dissolve(1)
            mc "*Sigh*"
            mc "{i}(I'm sorry, Rinny... Really, truly sorry.){/i}"
            menu:
                "Write a response letter[KoGa3AutoWTChange1]{size=-4}(Erynn Week6 Monday WriteLetter) {/size} {/color}":
                    $ Erynn_Week6_Monday_WriteLetter = True
                    scene 14_1096 with Dissolve(1)
                    mc "{i}(I should write her back. Even if it's years too late... Maybe it still matters.){/i}"
                    mc "{i}(Maybe it'll mean something to her... To know that I finally read it.){/i}"
                    scene 14_1095 with Dissolve(1)
                    mc "{i}(What do I even say...?){/i}"
                "Put the letter away":
                    scene 14_1095 with Dissolve(1)
                    mc "{i}(I'll just put it away for now.){/i}"
            stop music fadeout 1.0
            play music ("Music/LoFi Indie 3.mp3", "Music/LoFi Indie 1.mp3", "Music/LoFi Indie 2.mp3") volume 0.2
        "Throw the letter away":
            scene 14_1083 with Dissolve(1)
            mc "{i}(This is from years ago.){/i}"
            mc "{i}(And I didn't read the others.){/i}"
            mc "{i}(Not starting now...){/i}"
    scene black with Dissolve(1)
    pause 2
    scene 14_1097 with Dissolve(1)
    n "*Ding-dong*"
    mc "{i}(Please let that be John.){/i}"
    mc "{i}(I've had enough surprises for one day.){/i}"
    scene 14_1098 with Dissolve(1)
    mc "Hey, John."
    jo "Hey."
    mc "Thanks for coming over so quickly. Really appreciate it."
    jo "No problem at all. Shall we take a look?"
    mc "Yeah, I'll grab the keys."
    scene 14_1099 with Dissolve(1)
    jo "I like this new model."
    jo "Big step up from the previous one."
    mc "Yeah, it's a cool car."
    scene 14_1100 with Dissolve(1)
    mc "Let me pop the hood."
    if Emily_Week4_Sunday_DateJohn == True:
        jo "Actually... Before we check the engine, there's something I want to talk about."
        jo "I was going to bring it up at the garage, but I haven't told Iris anything yet, so..."
        scene 14_1101 with Dissolve(1)
        jo "I went on a date with Emily."
        mc "Yeah, I know. She told me."
        jo "And... Are you okay with that? I meant to talk to you before we went, but..."
        mc "It's fine, John. It's her call, not mine."
        jo "Still, I felt like I owed you a conversation. With everything we've been through... it just felt right to be honest."
        scene 14_1102 with Dissolve(1)
        mc "I appreciate that. Really. And I'm glad you told me."
        jo "Thanks, [mc]."
        scene 14_1103 with Dissolve(1)
        mc "So, how was it? The date?"
        jo "Honestly? It was nice. She's a remarkable woman and a great mom."
        mc "Planning a second one?"
        jo "I'd like to. I'd like to know her better."
        mc "She said she enjoyed herself, too."
        jo "That's nice to hear."
    else:
        jo "Yes, please do."
    scene 14_1104 with Dissolve(1)
    ""
    scene 14_1105 with Dissolve(1)
    jo "Alright, try starting it up."
    mc "Got it."
    play sound "Sounds/CarStalling.mp3" volume 0.5
    jo "Okay, that's enough."
    jo "Give me a sec."
    scene 14_1106 with Dissolve(1)
    stop sound
    jo "Alright, try again."
    play sound "Sounds/CarStalling2.mp3" volume 0.5
    jo "Keep it going."
    jo "Hmm..."
    stop sound
    scene 14_1107 with Dissolve(1)
    mc "Any idea?"
    jo "Hard to say, but it sounds like the engine isn't getting fuel."
    jo "Could be a problem with the fuel injection system."
    mc "Doesn't sound minor."
    scene 14_1108 with Dissolve(1)
    jo "No, but it might be something simpler. Maybe just a faulty wire."
    jo "I'll check a few more things before making any calls."
    scene 14_1109 with Dissolve(1)
    mc "Man, I wish I knew more about this stuff."
    jo "You're welcome to swing by the garage. I can show you a few basics."
    mc "You know what? That might be good. I've got some 'free time' and I can use a little distraction."
    jo "Wanna talk about it?"
    scene 14_1110 with Dissolve(1)
    mc "Just before you got here, someone rang the doorbell."
    mc "Thought it was you... But it was Andres."
    jo "Wait... Andres?"
    scene 14_1111 with Dissolve(1)
    mc "Yep."
    jo "He came to see you?"
    mc "Not just that. He's moved back to Madison Springs."
    scene 14_1112 with Dissolve(1)
    jo "Wow. Did he say why?"
    mc "He says he wants to fix things. Make amends."
    jo "I see."
    mc "..."
    scene 14_1113 with Dissolve(1)
    mc "I swear, it's like everything decides to crash down at once."
    jo "Tell me about it."
    scene black with Dissolve(1)
    pause 2
    scene 14_1114 with Dissolve(1)
    jo "Yeah, still leaning toward the fuel injection."
    jo "But I can't be sure without lifting it up at the shop."
    mc "Alright."
    scene 14_1115 with Dissolve(1)
    jo "I'll head back and grab the truck."
    jo "I'll also bring another car. Something your mom can use while I work on this."
    mc "She'll really appreciate that. Thanks, John."
    scene 14_1116 with Dissolve(1)
    jo "See you in about an hour."
    mc "Sounds good."
    if Valeria_LikeMC == True:
        scene black with Dissolve(1)
        pause 2
        scene 14_1117 with Dissolve(1)
        x "Only four teams left, we've got this."
        mc "I see a guy on top of the hill to the right."
        x "I see him. Don't shoot yet. Don't give away our position."
        x "Unless you've got a clean shot?"
        mc "Yeah..."
        scene 14_1118 with Dissolve(1)
        mc "Fuck! I could only knock him. He's behind the tree now."
        mc "Teammate probably ressing him."
        x "No worries. We've gotta move, though. Zone's closing in."
        play sound "Sounds/Phone_Vibrate.mp3"
        n "*Bzzzt. Bzzzt*"
        mc "{i}(Come on... Not now...){/i}"
        scene 14_1119 with Dissolve(1)
        n "*Bzzzt. Bzzzt*"
        mc "{i}(Who the hell is calling?){/i}"
        mc "{i}(Val? Must've got a new phone.){/i}"
        play sound "Sounds/Phone_Vibrate.mp3"
        n "*Bzzzt. Bzzzt*"
        x "Hey! What are you doing?"
        menu:
            "Keep playing[KoGa3AutoWTChange1]{size=-4}(MC Week6 Monday WinGame) {/size} {/color}":
                $ MC_Week6_Monday_WinGame = True
                scene 14_1120 with Dissolve(1)
                play sound "Sounds/Phone_Vibrate.mp3"
                n "*Bzzzt. Bzzzt*"
                mc "{i}(I'll call her after the game.){/i}"
                mc "Sorry, sorry."
                n "*Bzzzt. Bzzzt*"
                x "Let's move behind the rock. Got any smokes?"
                mc "Yeah."
                scene 14_1121 with Dissolve(1)
                x "FUCK!"
                mc "I've got you."
                x "No-no, no time. Go for the win."
                x "They're both in the house. Second floor."
                if Erynn_Week5_Tuesday_Photoshoot_Join == False:
                    scene 14_1122 with Dissolve(1)
                else:
                    scene 14_1123 with Dissolve(1)
                x "NICE!"
                x "One-on-one! You've got this!"
                mc "..."
                scene 14_1124 with Dissolve(1)
                x "YES! That's how we do... THAT'S HOW WE DO!"
                mc "Fuck yeah!"
                x "Nice one!"
                mc "You too!"
                scene 14_1125 with Dissolve(1)
                x "Let's run it again!"
                mc "Sorry, can't now. Gotta go."
                x "Kay, no problem. Let me add you though."
                mc "Sure."
                x "GG!"
                mc "GG, man."
                scene 14_1126 with Dissolve(1)
                mc "{i}(Let's call Val back.){/i}"
                scene 14_1127 with Dissolve(1)
                mc "{i}(Now she's not picking up?){/i}"
                mc "{i}(That's so typical Val!){/i}"
                scene 14_1128 with Dissolve(1)
                va "Hey!"
                mc "Finally! Are you doing that on purpose?"
                va "Doing what?"
                mc "Not picking up."
                va "You were the one who didn't pick up!"
                mc "Haha."
            "Pick up the phone":
                scene 14_1129 with Dissolve(1)
                mc "Sorry, I gotta go."
                x "What? What do you mean? We're in a top-three situation! You can't leave now!"
                play sound "Sounds/Phone_Vibrate.mp3"
                n "*Bzzzt. Bzzzt*"
                mc "Sorry, man..."
                x "Whatever!"
                scene 14_1130 with Dissolve(1)
                mc "Hey, Val."
                va "Hey."
                mc "You just cost me a game!"
                va "What?"
                mc "Haha. Never mind!"
        scene 14_1131 with Dissolve(1)
        mc "Got a new phone?"
        va "Mm-hmm."
        mc "Still got all your data?"
        va "I do, I do."
        mc "That's good."
        scene 14_1132 with Dissolve(1)
        va "How are you?"
        mc "I'm fine..."
        va "Okay."
        va "Look, I'm guessing you know why I'm calling."
        scene 14_1133 with Dissolve(1)
        mc "My suspension..."
        mc "You don't know what happened yet?"
        va "I heard one side of the story."
        mc "One side of the story? You spoke with Zach?"
        va "Yeah, I ran into him downtown while I was picking up my phone."
        mc "..."
        scene 14_1134 with Dissolve(1)
        mc "What did he say?"
        va "He said he didn't really understand what happened. He wanted to talk, you looked upset, and then suddenly you punched him."
        mc "What?"
        if Zach_Week6_Monday_Punch == False:
            mc "I didn't punch him! I pushed him away because he was swinging at me..."
        else:
            mc "I did punch him, but only after he kept coming at me."
        scene 14_1135 with Dissolve(1)
        mc "Let me tell you what he conveniently left out."
        mc "Remember those guys in the city who were about to beat me up, and you showed up and kicked one right in the balls?"
        va "..."
        scene 14_1136 with Dissolve(1)
        et "Hey, there!"
        et "Remember us?"
        et "We've been looking for you! Why don't you come with us for a moment?"
        scene 14_1137 with Dissolve(1)
        va "I remember..."
        mc "Before you showed up, Zach was with those guys."
        mc "Ethan fed him a bunch of lies, and he believed every word."
        mc "Then he said I 'stole' you from him... and out of nowhere, he punched me."
        va "..."
        mc "I haven't seen or spoken to him since."
        scene 14_1138 with Dissolve(1)
        mc "But today at school, he acted like nothing happened."
        mc "No apology. Nothing."
        mc "I told him I didn't want to talk to him."
        mc "But he kept pushing, so I reminded him what went down."
        mc "He tried to brush it off like 'friends' fight sometimes."
        scene 14_1139 with Dissolve(1)
        mc "I tried to walk away, but he kept stopping me."
        mc "Then we started arguing, and suddenly, he was swinging again."
        if Zach_Week6_Monday_Punch == False:
            mc "I pushed him away because I didn't want to get hit. He stumbled and fell."
            mc "Then the teacher came, suspension, and all that."
        else:
            mc "I wasn't about to get hit again, so I punched him. He stumbled and fell."
            mc "Then the teacher came, suspension, and all that."
        scene 14_1140 with Dissolve(1)
        va "..."
        mc "You still there?"
        va "..."
        mc "Val?"
        va "Sorry... I'm here. Just... thinking."
        scene 14_1141 with Dissolve(1)
        mc "About what?"
        va "No matter what I do, I'm going to lose a friend."
        mc "..."
        mc "You've heard both sides now."
        mc "Take all the time you need..."
        scene 14_1142 with Dissolve(1)
        va "No, I already made up my mind."
        mc "Uh..."
        va "I'm still on the phone with you. Does that answer your question?"
        mc "Heh, yeah..."
        scene 14_1143 with Dissolve(1)
        mc "I'm sorry for putting you in the middle of this."
        va "You didn't."
        mc "Can I ask you a favour?"
        va "Of course."
        mc "Can you stay away from Zach?"
        scene 14_1144 with Dissolve(1)
        va "I will..."
        va "But first, I need one last talk with him. To explain why..."
        mc "Please don't meet him alone. With everything going on, I don't trust him."
        va "Okay."
        scene 14_1145 with Dissolve(1)
        va "So, you're suspended until Friday?"
        mc "Yeah... Unfortunately."
        va "What about the relay?"
        mc "I don't know yet. They might not let me participate, since I won't be able to train with you all."
        scene 14_1146 with Dissolve(1)
        va "I'll talk to Coach tomorrow."
        va "And hey, we can always train together after school."
        mc "Thanks."
        scene 14_1147 with Dissolve(1)
        va "Hey. Are we still on for tomorrow?"
        if AlexisValeria == False:
            mc "Of course. I'm looking forward to it."
            mc "And now I have some time to find an outfit."
            va "Haha, yeah."
        else:
            mc "{i}(I still haven't made the decision between this and the barbecue.){/i}"
            mc "{i}(But after my suspension, I don't think Adriana wants me there...){/i}"
            mc "Of course. Looking forward to it."
            va "Great."
        scene 14_1148 with Dissolve(1)
        va "So, what's the plan for the next few days?"
        mc "Not sure yet. Maybe Mom wants me to pick up some shifts at the restaurant."
        mc "Or I'll hit the gym and train solo."
        mc "Or just chill... Play some video games like earlier."
        if MC_Week6_Monday_WinGame == False:
            scene 14_1149 with Dissolve(1)
            va "Ah, so that's what you meant by 'you made me lose a game'..."
            mc "Haha, yeah."
            mc "I was mid-game when you called, and I bailed on my teammate."
            va "Such a terrible teammate!"
            mc "Haha, I know."
        else:
            scene 14_1149 with Dissolve(1)
            va "Ah, that's why you didn't pick up!"
            mc "Haha, yeah."
            mc "I was in the middle of a game and couldn't just leave my teammate hanging."
            va "Not even for me?"
            mc "Yeah... I really messed up!"
            va "Haha, I'm just teasing! You're a great teammate. I'd have finished the game too."
        scene 14_1150 with Dissolve(1)
        va "What game were you playing?"
        mc "PSV. Protocol: Shadow Veil."
        va "Oh, that one. I heard some people at school talk about it."
        va "Shooter game."
        mc "Indeed."
        scene 14_1151 with Dissolve(1)
        va "Are you any good?"
        mc "I win now and again. So... I'd say I'm decent."
        mc "But I don't play that often. When I do, it's mostly RPGs."
        scene 14_1152 with Dissolve(1)
        mc "Do you play any games?"
        va "I do. Sometimes... Not as often as I used to."
        va "Whenever I feel like it, I play Avendor."
        mc "Oh, that's the card game based on that TV show, right?"
        va "Yes."
        if Ximena_Week5_Thursday_Watch == True:
            scene 14_1153 with Dissolve(1)
            mc "Hmm..."
            va "What is it?"
            mc "Just had a thought. Give me a sec."
            scene 14_1154 with Dissolve(1)
            mc "I knew it!"
            va "Knew what?"
            scene 14_1155 with Dissolve(1)
            mc "{i}(She's in some amazing TV shows.){/i}"
            mc "{i}(Another one I need to watch!){/i}"
            scene 14_1156 with Dissolve(1)
            mc "Ximena Vergara. She's an actress. Do you know her?"
            va "I know her."
            mc "I actually met her at the restaurant last week."
            mc "She was there with Gabi, the Spanish teacher from our school."
            va "Really?"
            scene 14_1157 with Dissolve(1)
            mc "Mm-hmm."
            mc "I didn't really know who she was..."
            if Erynn_Week5_Tuesday_Photoshoot == True:
                mc "Only that she has a role in Entanglement."
            else:
                pass
            mc "But when you mentioned Avendor, it all clicked."
            mc "Can't believe I didn't recognise her before."
            scene 14_1158 with Dissolve(1)
            mc "I watched like the first three seasons."
            va "Then you've got some serious catching up to do. They're on season eight now."
            mc "Eight? Damn... I need more hours in a day."
            va "Haha, who doesn't?"
            mc "Anyway... Back to the game."
        else:
            pass
        scene 14_1159 with Dissolve(1)
        mc "Maybe we could play together sometime?"
        va "Sure. Want to come over?"
        mc "Uh... what? Now? I meant online, but are you actually inviting me to your place?"
        va "Maybe!"
        mc "Haha."
        scene 14_1160 with Dissolve(1)
        mc "I'd love to, but I can't right now."
        va "Too bad..."
        mc "Don't make this harder than it already is!"
        va "Make what harder?"
        scene 14_1161 with Dissolve(1)
        mc "Stop it!"
        va "Haha..."
        scene 14_1162 with Dissolve(1)
        mc "{i}(Fuck...){/i}"
        mc "{i}(That would've been amazing!){/i}"
        scene 14_1163 with Dissolve(1)
        mc "Maybe we... Now I keep using maybe too... You've infected me!"
        va "Haha."
        mc "*Sigh...*"
        mc "Maybe we can play something online together later?"
        scene 14_1164 with Dissolve(1)
        va "I'm going to my dad's first, not sure how long I'll be."
        mc "I need to download the game anyway. I'll call you later, and if you're free then?"
        va "Sounds good."
        scene 14_1165 with Dissolve(1)
        mc "Okay. Uhm... Talk to you later then!"
        va "Yeah. Bye, [mc]."
        mc "Bye, Val."
        scene 14_1166 with Dissolve(1)
        va "..."
    else:
        $ MC_Week6_Monday_WinGame = True
        scene black with Dissolve(1)
        pause 2
        scene 14_1117 with Dissolve(1)
        x "Only four teams left, we've got this."
        mc "I see a guy on top of the hill to the right."
        x "I see him. Don't shoot yet. Don't give away our position."
        x "Do you have a clean shot?"
        mc "Yeah..."
        scene 14_1118 with Dissolve(1)
        mc "Fuck! I could only knock him. He's behind a tree now."
        mc "Teammate probably ressing him."
        x "No worries. We've gotta move though. Zone is coming in."
        scene 14_1120 with Dissolve(1)
        x "Let's move behind the rock. Got any smokes?"
        mc "Yeah."
        scene 14_1121 with Dissolve(1)
        x "FUCK!"
        mc "I've got you."
        x "No-no, no time. Go for the win."
        x "They're both in the house. Second floor."
        if Erynn_Week5_Tuesday_Photoshoot_Join == True:
            scene 14_1123 with Dissolve(1)
        else:
            scene 14_1122 with Dissolve(1)
        x "NICE!"
        x "One-on-one! You've got this!"
        mc "..."
        scene 14_1124 with Dissolve(1)
        x "YES! That's how we do... THAT'S HOW WE DO!"
        mc "Fuck yeah!"
        x "Nice one!"
        mc "You too!"
        scene 14_1125 with Dissolve(1)
        x "Let's run it again!"
        mc "Sure."
    if MC_Week5_Friday_RiversideVisit == True:
        if Mira_Week5_Saturday_Like == True:
            $ Nikki_SPoints -= 4
            scene black with Dissolve(1)
            pause 2
            scene 14_1167 with Dissolve(1)
            mc "*Nggh*"
            play sound "Sounds/Phone_Vibrate.mp3"
            n "*Bzzzt. Bzzzt*"
            mc "{i}(Next person who wants to ask why I'm suspended...){/i}"
            n "*Bzzzt. Bzzzt*"
            scene 14_1168 with Dissolve(1)
            if Nikki_Girlfriend == False:
                mc "{i}(Oh, it's Nikki...){/i}"
                mc "{i}(Why is she calling me? Did something happen with Cara?){/i}"
                mc "{i}(And she wants to FaceTime?){/i}"
            else:
                mc "{i}(Oh, it's Nikki...){/i}"
                mc "{i}(And she wants to FaceTime?){/i}"
                mc "{i}(She can't know about my suspension... Or did Mike tell her?){/i}"
            scene 14_1169 with Dissolve(1)
            mc "Hey, Nikki!"
            mc "How are you?"
            mc "..."
            mc "Everything okay?"
            scene 14_1170 with Dissolve(1)
            mc "Nikki?"
            mc "Say something, please!"
            if Nikki_Girlfriend == False:
                mc "Did something happen with Cara?"
            else:
                mc "Did something happen?"
            scene 14_1171 with Dissolve(1)
            ni "..."
            mc "What is that?"
            mc "Are those panties?"
            scene 14_1172 with Dissolve(1)
            mc "Why are you showing me your panties?"
            ni "They're not mine."
            mc "Cara's?"
            ni "No..."
            scene 14_1173 with Dissolve(1)
            mc "I don't get it."
            mc "Why show me those? Whose are they, then?"
            ni "That's what I'd like to know!"
            mc "Huh?"
            scene 14_1174 with Dissolve(1)
            ni "I found them in my car!"
            mc "Okay?"
            ni "After you borrowed it to drive to Alvarado!"
            scene 14_1175 with Dissolve(1)
            mc "What does that have to do with me? You're really confusing me."
            mc "Is this supposed to be a joke?"
            ni "No! It's not a joke, [mc]!"
            mc "..."
            scene black with Dissolve(1)
            pause 1
            scene 14_1176 with Dissolve(1)
            ""
            scene black with Dissolve(1)
            pause 1
            scene 14_1177 with Dissolve(1)
            mc "{i}(Mira...){/i}"
            mc "{i}(Oh fuck!){/i}"
            mc "{i}(Oh shit!){/i}"
            mc "{i}(I'm so fucked!){/i}"
            mc "{i}(Did she forget her panties, or leave them there on purpose?){/i}"
            mc "{i}(Why does that even matter now? What am I supposed to do?){/i}"
            menu:
                "Lie[KoGa3AutoWTChange1]{size=-4}(NikkiCara Week6 Monday MiraLie, Cara Points-4, Nikki Points-4, Nikki SPoints-10, Nikki SPFalse) {/size} {/color}":
                    $ NikkiCara_Week6_Monday_MiraLie = True
                    $ Cara_Points -= 4
                    $ Nikki_Points -= 4
                    $ Nikki_SPoints -= 10
                    $ Nikki_SP = False
                    scene 14_1178 with Dissolve(1)
                    mc "I honestly have no idea how or when those panties got into your car."
                    ni "..."
                    mc "I only used it to drive to Alvarado and back."
                    mc "Where exactly did you find them?"
                    scene 14_1179 with Dissolve(1)
                    ni "Passenger seat. Not on the seat itself, but by the footwell."
                    mc "I don't want to make excuses, but when you go to the gym, do you usually bring your bag?"
                    ni "Yeah, I do."
                    mc "Maybe someone's panties got stuck on your bag in the locker room and ended up there?"
                    mc "{i}(What the hell am I even saying?){/i}"
                    scene 14_1180 with Dissolve(1)
                    ni "I don't know. I didn't check the car before handing you the keys."
                    ni "This morning when I got in, I saw them and just freaked out."
                    ni "You know I've been cheated on before and... *Sigh*"
                    scene 14_1181 with Dissolve(1)
                    ni "Sorry..."
                    mc "No, it's okay. I'd freak out too."
                    mc "{i}(I'm such a terrible person.){/i}"
                    if Nikki_Girlfriend == False:
                        scene 14_1182 with Dissolve(1)
                        mc "Did you tell Cara about this?"
                        ni "No. I wanted to talk with you first, before jumping to conclusions. Glad I did."
                        ni "I don't see a reason to worry her over this."
                        mc "Thanks, Nikki."
                    else:
                        pass
                    scene 14_1183 with Dissolve(1)
                    ni "I feel awful about this!"
                    ni "I'm so sorry, [mc]!"
                    mc "It's okay."
                    scene 14_1184 with Dissolve(1)
                    mc "How are you holding up? Are you okay?"
                    ni "Much better now..."
                    mc "You're still coming to visit this week?"
                    if Nikki_Girlfriend == False:
                        ni "Yeah. I spoiled the surprise at the airport, but we're still coming."
                        mc "Can't wait!"
                    else:
                        ni "Yes, and I'll make it up to you with a big apology when I get there!"
                        mc "Haha, looking forward to it!"
                    scene 14_1185 with Dissolve(1)
                    ni "What are you up to right now?"
                    mc "Waiting for John."
                    mc "Mom's car broke down, and he's bringing it to the garage."
                    mc "Should be here any minute."
                    scene 14_1186 with Dissolve(1)
                    ni "I'll let you go then. I'm just gonna lie here and wallow in shame a bit."
                    mc "Don't think about it. Let's just pretend this never happened."
                    ni "I'll try."
                    scene 14_1187 with Dissolve(1)
                    ni "Bye, [mc]. See you soon."
                    mc "See you soon, Nikki!"
                    if Nikki_Girlfriend == False:
                        pass
                    else:
                        mc "Love you!"
                        ni "Love you, too!"
                    scene 14_1188 with Dissolve(1)
                    mc "{i}(FUUUUUUCK!!!){/i}"
                    mc "{i}(I almost ruined everything.){/i}"
                    mc "{i}(If she ever finds out the truth...){/i}"
                "Mention Mira[KoGa3AutoWTChange1]{size=-4}(NikkiCara Week6 Monday MiraLie, NikkiCara Week6 Monday MiraMention, Cara Points-8, Nikki Points-8, Nikki SPoints-10, Nikki SPFalse) {/size} {/color}":
                    $ NikkiCara_Week6_Monday_MiraLie = True
                    $ NikkiCara_Week6_Monday_MiraMention = True
                    $ Cara_Points -= 8
                    $ Nikki_Points -= 8
                    $ Nikki_SPoints -= 10
                    $ Nikki_SP = False
                    scene 14_1189 with Dissolve(1)
                    mc "Wait... They could be Mira's..."
                    ni "WHO THE FUCK is Mira and why would HER panties be in MY car?"
                    mc "She's an old friend."
                    mc "We ran into each other at the diner I was at with Nathan."
                    scene 14_1190 with Dissolve(1)
                    ni "That doesn't explain why her panties were in my car!"
                    mc "She was visiting her grandparents."
                    mc "Since it was on my way back to Riverside, I gave her a ride."
                    mc "They must've slipped out of her bag."
                    mc "{i}(What the fuck am I doing. Now I'm using the same lie Mira used on Owen...){/i}"
                    scene 14_1191 with Dissolve(1)
                    ni "Slipped out of her bag?"
                    mc "Or maybe she left them on purpose?"
                    ni "..."
                    ni "Why would she do that?"
                    scene 14_1192 with Dissolve(1)
                    if Nikki_Girlfriend == False:
                        mc "Uhm..."
                        mc "She wasn't really an ex but we had a thing a while ago."
                        mc "Before I moved to Riverside."
                        mc "Maybe she left them as a joke."
                    else:
                        mc "Uhm..."
                        mc "We never really talked about it, but she's an ex."
                        mc "Well, not exactly an ex, but we had a thing."
                        mc "So maybe she left them as a joke."
                    scene 14_1193 with Dissolve(1)
                    ni "As a joke?"
                    mc "I don't know, Nikki."
                    mc "Just guessing here. Maybe they're not even hers."
                    mc "{i}(Why am I getting mad at her? I know I'm at fault. Gaslighting at its finest...){/i}"
                    ni "..."
                    scene 14_1194 with Dissolve(1)
                    ni "You only gave her a ride to her grandparents?"
                    mc "Well..."
                    ni "Well?"
                    mc "She tried to kiss me, but I pushed her away."
                    scene 14_1195 with Dissolve(1)
                    ni "..."
                    mc "Nikki?"
                    mc "Are you still there?"
                    scene 14_1196 with Dissolve(1)
                    ni "Is that all that happened?"
                    mc "Yes! I told her we can't do this because I have a girlfriend."
                    ni "..."
                    if Nikki_Girlfriend == False:
                        pass
                    else:
                        scene 14_1197 with Dissolve(1)
                        ni "Promise?"
                        mc "I promise, Nikki! I'd never do this to you!"
                        mc "{i}(When did I start believing my own lies?){/i}"
                    scene 14_1183 with Dissolve(1)
                    ni "*Sigh*"
                    ni "This morning when I got in, I saw them and just freaked out."
                    ni "You know I've been cheated on before and... *Sigh*"
                    ni "Sorry..."
                    mc "No, it's okay. I'd freak out too."
                    mc "{i}(I'm such a terrible person.){/i}"
                    if Nikki_Girlfriend == False:
                        scene 14_1182 with Dissolve(1)
                        mc "Did you tell Cara about this?"
                        ni "No. I wanted to talk with you first, before jumping to conclusions. Glad I did."
                        ni "I don't see a reason to worry her over this."
                        mc "Thanks, Nikki."
                    else:
                        pass
                    scene 14_1184 with Dissolve(1)
                    mc "How are you holding up? Are you okay?"
                    ni "Much better now..."
                    mc "You're still coming to visit this week?"
                    if Nikki_Girlfriend == False:
                        ni "Yeah. I spoiled the surprise at the airport, but we're still coming."
                        mc "Can't wait!"
                    else:
                        ni "Yes, and I'll make it up to you with a big apology when I get there!"
                        mc "Haha, looking forward to it!"
                    scene 14_1185 with Dissolve(1)
                    ni "What are you up to right now?"
                    mc "Waiting for John."
                    mc "Mom's car broke down, and he's bringing it to the garage."
                    mc "Should be here any minute."
                    scene 14_1186 with Dissolve(1)
                    ni "I'll let you go then. I'm just gonna lie here and wallow in shame a bit."
                    mc "Don't think about it. Let's just pretend this never happened."
                    ni "I'll try."
                    scene 14_1187 with Dissolve(1)
                    ni "Bye, [mc]. See you soon."
                    mc "See you soon, Nikki!"
                    if Nikki_Girlfriend == False:
                        pass
                    else:
                        mc "Love you!"
                        ni "Love you, too!"
                    scene 14_1188 with Dissolve(1)
                    mc "{i}(FUUUUUUCK!!!){/i}"
                    mc "{i}(I almost ruined everything.){/i}"
                    mc "{i}(If she ever finds out the whole truth...){/i}"
                "Truth[KoGa3AutoWTChange1]{size=-4}(Riverside End, Riverside Friends, MC Week5 Friday RiversideVisitFalse, Riverside MiraTruth, Nikki SPFalse, Cara Points-20, Nikki Points-20, Nikki SPoints-10, {i}Nikki GirlfriendFalse: Cara GirlfriendFalse, Cara Cheat{/i}, {i}else: Nikki GirlfriendFalse, Nikki Cheat{/i}) {/size} {/color}":
                    $ Riverside_End = True
                    $ Riverside_Friends = True
                    $ MC_Week5_Friday_RiversideVisit = False
                    $ Riverside_MiraTruth = True
                    $ Nikki_SP = False
                    $ Cara_Points -= 20
                    $ Nikki_Points -= 20
                    $ Nikki_SPoints -= 10
                    scene 14_1198 with Dissolve(1)
                    stop music fadeout 1.0
                    play music ("Music/Slow.mp3", "Music/Slow4.mp3") volume 0.5
                    mc "{i}(I don't know...){/i}"
                    mc "{i}(I got myself in this mess, and...){/i}"
                    mc "{i}(Should I just... tell her the truth?) {/i}"
                    ni "Why aren't you saying anything?"
                    scene 14_1199 with Dissolve(1)
                    mc "I'm sorry, Nikki..."
                    ni "What do you mean you're sorry?"
                    mc "..."
                    ni "What did you do?"
                    scene 14_1200 with Dissolve(1)
                    mc "It... It just happened..."
                    ni "What happened?"
                    mc "While I was with Nathan at the diner, I ran into Mira, an old friend."
                    mc "Afterwards, I offered her a ride home..."
                    if Nikki_Girlfriend == False:
                        $ Cara_Girlfriend = False
                        $ Cara_Cheat = True
                        scene 14_1201 with Dissolve(1)
                        mc "And then..."
                        ni "..."
                        scene 14_1202 with Dissolve(1)
                        ni "You had sex with her!"
                        ni "In my car!"
                        mc "..."
                        scene 14_1203 with Dissolve(1)
                        mc "I'm sorry... It was a moment of weakness and..."
                        ni "Don't give me that crap! A moment of weakness..."
                        ni "You cheated! You cheated on Cara!"
                        scene 14_1204 with Dissolve(1)
                        ni "You know I've been cheated on and now you're doing the same to her!"
                        mc "I'm sorry, I..."
                        ni "You're only sorry because you got caught!"
                        ni "You weren't sorry when you came home and slept with Cara like nothing happened!"
                        scene 14_1205 with Dissolve(1)
                        mc "..."
                        ni "..."
                        scene 14_1206 with Dissolve(1)
                        mc "Is Cara home?"
                        mc "Please, can I talk to her?"
                        ni "You don't get to talk to her!"
                        ni "She's right here. She heard everything."
                        show 14_1207
                        mc "..."
                        scene 14_1208 with Dissolve(1)
                        mc "I'm sorry, Cara!"
                        mc "It was a mistake!"
                        mc "I wasn't thinking. I never wanted to hurt you."
                        scene 14_1209 with Dissolve(1)
                        mc "Can we talk?"
                        ni "No."
                        ni "Don't text her, don't call her, don't do anything. Ever."
                        ni "You're just like Aiden. No, worse. At least he had the guts to tell me. You're a piece of shit."
                        ni "Like father, like son."
                        scene 14_1210 with Dissolve(1)
                        mc "Nikki... I..."
                        mc "..."
                        mc "{i}(She hung up.){/i}"
                        scene 14_1188 with Dissolve(1)
                        mc "FUUUUCK!!!"
                        mc "{i}(Why am I so fucking stupid?){/i}"
                        mc "{i}(And that last thing she said... Like father, like son.){/i}"
                        mc "{i}(Didn't expect those words to hurt this much.){/i}"
                        mc "{i}(Because she's fucking right!){/i}"
                        scene 14_1211 with Dissolve(1)
                        c "*Crying*"
                    else:
                        $ Nikki_Girlfriend = False
                        $ Nikki_Cheat = True
                        scene 14_1212 with Dissolve(1)
                        mc "And then..."
                        ni "..."
                        scene 14_1213 with Dissolve(1)
                        ni "*Whispers* You had sex with her..."
                        mc "What?"
                        ni "You had sex with her!"
                        ni "In my car!"
                        mc "..."
                        scene 14_1214 with Dissolve(1)
                        mc "I'm sorry... It was a moment of weakness and..."
                        ni "Don't come at me with that shit, [mc]! A moment of weakness..."
                        ni "You cheated! You cheated on me!"
                        scene 14_1215 with Dissolve(1)
                        ni "You know I've been cheated on and now you do the same to me!"
                        mc "I'm sorry, I..."
                        ni "You're only sorry because you got caught!"
                        ni "You weren't sorry when you came back and slept with me like nothing happened!"
                        scene 14_1205 with Dissolve(1)
                        mc "..."
                        ni "..."
                        scene 14_1216 with Dissolve(1)
                        ni "I quit my job, wanted to go to college with you..."
                        ni "How could I have been this stupid?"
                        mc "I'm sorry, Nikki!"
                        mc "It was a mistake!"
                        mc "I wasn't thinking... It will never happen again!"
                        scene 14_1217 with Dissolve(1)
                        ni "The only thing that's never going to happen again is us!"
                        mc "Nikki..."
                        ni "You're just like Aiden. No, worse. At least he had the guts to tell me! You're a piece of shit."
                        ni "Like father, like son!"
                        scene 14_1210 with Dissolve(1)
                        mc "Nikki... I..."
                        mc "..."
                        mc "{i}(She hung up.){/i}"
                        scene 14_1188 with Dissolve(1)
                        mc "FUUUUCK!!!"
                        mc "{i}(Why am I so fucking stupid?){/i}"
                        mc "{i}(And that last thing she said... Like father, like son.){/i}"
                        mc "{i}(Didn't expect those words to hurt this much.){/i}"
                        mc "{i}(Because she's fucking right!){/i}"
                        scene 14_1218 with Dissolve(1)
                        ni "*Crying*"
        else:
            pass
    else:
        pass
    scene black with Dissolve(2)
    pause 2
    stop music fadeout 1.0
    play music ("Music/LoFi Upbeat 1.mp3", "Music/LoFi Upbeat 2.mp3", "Music/LoFi Upbeat 3.mp3", "Music/LoFi Upbeat 4.mp3") volume 0.2
    scene 14_1219 with Dissolve(1)
    jo "Let's push it out onto the street."
    jo "Makes it easier to load onto the truck that way."
    mc "What car did you bring?"
    jo "Nothing special. Got it a few days ago as a trade-in. It's a good car, though."
    if Iris_Week6_Monday_Garage_Sex == False:
        scene 14_1220 with Dissolve(1)
        mc "Is that it?"
        jo "Yes."
        mc "I think I saw that car in your garage earlier."
        jo "Correct."
    else:
        scene 14_1220 with Dissolve(1)
        mc "Haha."
        mc "{i}(Can't believe it's that car. The one Iris and I had sex on. Special service... Sorry, Mom!){/i}"
        jo "Why are you laughing?"
        mc "Oh, nothing. Just thought I'd seen that car before."
    scene 14_1221 with Dissolve(1)
    mc "Is it an automatic?"
    jo "It is. I checked earlier to see if this one was manual or automatic, so I could get her the same."
    mc "Good! Because I don't know if Mom can drive stick."
    if Emily_Week4_Sunday_DateJohn == True:
        scene 14_1222 with Dissolve(1)
        jo "*Clears throat*"
        mc "What?"
        jo "Nothing, nothing. Just being childish."
    else:
        pass
    scene 14_1223 with Dissolve(1)
    jo "And?"
    mc "It drives better than I expected. Really smooth."
    jo "It's a good car."
    mc "Mom will be happy! How much does something like this go for?"
    scene 14_1224 with Dissolve(1)
    jo "New, or this one here?"
    mc "This one."
    jo "Hmm... Around 18k."
    mc "Eeeh... Never mind."
    scene 14_1225 with Dissolve(1)
    jo "Haha. Interested in a car?"
    if MC_Bike == True:
        mc "I've got my bike for now. Maybe in a few years, once I've saved up a bit more."
    else:
        mc "I might be, but I'm a bit short on cash right now. Need to save more."
    jo "How much are you short?"
    mc "Let's see... Uhm..."
    mc "18k!"
    jo "Haha."
    scene 14_1226 with Dissolve(1)
    jo "Maybe you should take Iris up on her offer and work at the garage."
    jo "You could afford one within a year."
    mc "Hmm..."
    jo "I'm joking! You go to college!"
    mc "Yes, sir!"
    scene 14_1227 with Dissolve(1)
    mc "Any paperwork I need to sign?"
    jo "Haven't had time to print anything yet. We'll do that when you pick up your car."
    mc "Sounds good."
    scene 14_1228 with Dissolve(1)
    jo "Before I go, mind if I use your bathroom?"
    mc "Go ahead."
    mc "When you get inside, turn left immediately, then straight ahead."
    jo "Thanks."
    scene 14_1229 with Dissolve(1)
    mc "{i}(18k...){/i}"
    mc "{i}(Cars are so expensive these days.){/i}"
    scene 14_1230 with Dissolve(1)
    me "New car..."
    m "Looks like it."
    m "Must've been more wrong with mine than I thought."
    scene 14_1231 with Dissolve(1)
    mc "..."
    mc "No way!"
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 14_1232 at moveup
    pause 3
    mc "There's just no way!"
    mc "Melissa!"
    mc "You never fail to surprise me!"
    scene 14_1233 with Dissolve(1)
    me "Haha."
    me "I was waiting for your reaction!"
    m "Looks great, right?"
    mc "Mm-hmm! Totally!"
    scene 14_1234 with Dissolve(1)
    mc "Let me have a proper look."
    mc "Yep. Looks amazing!"
    me "Thank you."
    scene 14_1235 with Dissolve(1)
    mc "Back to the original colour after all these years, huh?"
    me "I'm not even sure if this is my natural colour, but it should be close. At least I hope so."
    mc "And extensions too?"
    me "Yes. Still deciding if I want to grow it out again. It's going to take a while with my shaved sides."
    if Emily_Week5_Sunday_Hug == True:
        menu:
            "Compliment Melissa[KoGa3AutoWTChange1]{size=-4}(Melissa Week6 Monday Compliment, {i}Emily Week4 Sunday DateJohn: Melissa LikeMC{/i}) {/size} {/color}":
                $ Melissa_Week6_Monday_Compliment = True
                if Emily_Week4_Sunday_DateJohn == True:
                    $ Melissa_LikeMC = True
                else:
                    pass
                scene 14_1236 with Dissolve(1)
                mc "Damn, you're looking hot!"
                m "Excuse me?"
                me "Haha, thanks."
                mc "You're gorgeous, too, Mom!"
                m "Thank you! But still not what I meant."
                scene 14_1237 with Dissolve(1)
                me "Let him be, Em. He's the only guy who compliments me these days."
                mc "I seriously doubt that. But you're welcome, Mel!"
                mc "And hey! You look younger with the long hair. It really suits you!"
                scene 14_1238 with Dissolve(1)
                me "Come here! That deserves a Melissa hug!"
                mc "YES! Melissa hugs are the best!"
                m "*Sigh* Here we go again..."
                scene 14_1239 with Dissolve(1)
                mc "My day's officially better now!"
                me "Haha. Thank you for all the sweet words."
                scene 14_1240 with Dissolve(1)
                me "..."
                me "I'll allow it this one time!"
                scene 14_1241 with Dissolve(1)
                mc "Mom, I think I'm in love with Melissa."
                m "Get in line, honey. Right behind me!"
                me "Oh god... You two are going to make me blush!"
                m "You asked for compliments!"
                scene 14_1242 with Dissolve(1)
                mc "Did Mel pick you up from the restaurant?"
                m "Mm-hmm."
                mc "What was Mom's reaction when she saw you?"
                scene 14_1243 with Dissolve(1)
                me "Uh..."
                m "..."
                m "That... That's rated PG above your age!"
                mc "Haha, what? Come on, spill!"
                m "Nope!"
                scene 14_1244 with Dissolve(1)
                mc "I wanna jump your bones?"
                m "[mc]!"
                me "Something like that."
                m "Melissa!"
                me "You're the one who said it!"
                mc "{i}(I want to know so badly...){/i}"
                scene 14_1245 with Dissolve(1)
                mc "*Whispers* You're telling me later, right?"
                m "What are you two whispering about?"
                mc "Sorry but that's rated PG under your age!"
                m "..."
                m "Melissa's older than me!"
                me "Haha."
            "Why not":
                mc "Yeah, why not."
    else:
        mc "Yeah, why not."
    scene 14_1246 with Dissolve(1)
    m "So, what's the deal with this car?"
    mc "John stopped by to check out what's wrong with yours."
    mc "He thinks it might be something with the fuel injection system."
    m "Ugh, that doesn't sound good."
    scene 14_1247 with Dissolve(1)
    mc "Yeah, nothing he could fix here on the spot."
    mc "So he brought his tow truck to take it to the garage."
    mc "And he even brought a loaner for you to use in the meantime."
    mc "That's this one."
    scene 14_1248 with Dissolve(1)
    if Emily_Week4_Sunday_DateJohn == True:
        m "That's really sweet of him."
        m "I'll call him later to thank him."
        mc "He's still here, actually. Just using the bathroom."
        m "Oh, perfect then."
        scene 14_1249 with Dissolve(1)
        me "I guess I finally get to meet your mysterious John."
        m "Looks like it."
    else:
        m "I really should go see him and thank him."
        mc "He's still here. He's using the bathroom."
        m "Oh, even better."
    scene 14_1250 with Dissolve(1)
    m "Let's head inside. I'll make us some coffee."
    if MC_Bike == True:
        m "Want one too, honey?"
        mc "Nah, I'm good. Thanks, though."
        scene 14_1251 with Dissolve(1)
        m "Thanks again for handling everything today!"
        mc "Of course. Anytime."
        scene 14_1252 with Dissolve(1)
        ""
    else:
        m "Want one too, [mc]?"
        mc "Nah, I'm good. Thanks though."
        scene 14_1253 with Dissolve(1)
        m "Thank you for taking care of this!"
        mc "You're welcome."
    if Melissa_Week6_Monday_Compliment == True:
        scene 14_1254 with Dissolve(1)
        m "So... What did [mc] whisper to you earlier?"
        me "Geez, you're so nosy! Not telling!"
        m "No coffee for you, then!"
        me "Haha!"
    else:
        pass
    scene 14_1255 with Dissolve(1)
    if MC_Bike == False:
        jo "Oh, hello. You must be [mc]'s mom."
        m "Hi! I am and you must be..."
    else:
        jo "Hey there, Emily and..."
        m "Hi! Let me introduce you to my bestie here."
        m "This is..."
    scene 14_1256 with Dissolve(1)
    me "John...?"
    me "How..."
    m "..."
    m "Oh no..."
    scene 14_1257 with Dissolve(1)
    jo "Uhm, sorry. Do we know each other?"
    me "..."
    scene 14_1258 with Dissolve(1)
    jo "Wait... No way!"
    jo "Melissa?"
    me "*Nods*"
    jo "I'm so sorry. I didn't recognise you at first... The hair, the tattoos..."
    if Emily_Week4_Sunday_DateJohn == True:
        scene 14_1259 with Dissolve(1)
        m "*Whispers* What have I done..."
        me "..."
    else:
        pass
    scene 14_1260 with Dissolve(1)
    jo "This is... Wow, I'm speechless."
    jo "How long has it been?"
    me "Twenty-two years."
    jo "Uhm... How are you?"
    scene 14_1261 with Dissolve(1)
    m "I think I should give you two a moment..."
    me "No. Stay."
    me "Let's go get those coffees."
    scene black with Dissolve(1)
    pause 2
    scene 14_1262 with Dissolve(1)
    mc "..."
    mc "{i}(What's taking so long?){/i}"
    scene 14_1263 with Dissolve(1)
    mc "Oh... Here..."
    me "You think I haven't? I've spent years..."
    m "Mel... One second."
    scene 14_1264 with Dissolve(1)
    mc "What's going on? You can cut the tension in here..."
    m "[mc], can you go to your room, please?"
    mc "Did something happen?"
    m "Please. Just for a bit."
    mc "..."
    mc "Alright..."
    scene 14_1265 with Dissolve(1)
    mc "*Sigh*"
    mc "{i}(Seriously... What the hell is going on?){/i}"
    mc "{i}(Do they know each other?){/i}"
    mc "{i}(It sure seemed like it... the way they looked at each other, the way they spoke.){/i}"
    scene black with Dissolve(1)
    pause 2
    scene 14_1266 with Dissolve(1)
    mc "{i}(I can still hear them talking...){/i}"
    mc "{i}(What are they even saying? It sounds serious.){/i}"
    mc "{i}(Ugh... This is driving me crazy.){/i}"
    mc "{i}(Screw it... I'll go take a quick shower.){/i}"
    scene black with Dissolve(1)
    pause 2
    scene 14_1267 with Dissolve(1)
    mc "{i}(Are they still at it?){/i}"
    mc "{i}(I'm gonna take a look.){/i}"
    mc "{i}(I'll just walk in like I'm grabbing a drink. Casual. No big deal.){/i}"
    if Emily_Week4_Sunday_DateJohn == False:
        scene 14_1268 with Dissolve(1)
        mc "{i}(Looks like they're gone.){/i}"
        mc "Did both of them leave?"
        mc "..."
        mc "Mom?"
        scene 14_1269 with Dissolve(1)
        m "Hmm?"
        mc "Did they leave?"
        m "Yeah..."
        scene 14_1270 with Dissolve(1)
        mc "Can you tell me what happened?"
        m "A lot!"
        mc "A lot?"
        m "*Sigh* A lot..."
        scene 14_1271 with Dissolve(1)
        m "Let me take a quick shower first. I've been in these clothes all day."
        m "And honestly, I need a few minutes to clear my head."
        mc "Is it that serious?"
        m "No, but it's... It's something. I'll come to your room and explain everything, okay?"
        mc "Alright. I'll wait."
        scene 14_1272 with Dissolve(1)
        mc "{i}(She said it's not bad, but it still sounded serious...){/i}"
        mc "..."
        jump Week6_Monday_MCRoom_EmilyTalk
    else:
        scene 14_1273 with Dissolve(1)
        m "I'm sorry, Melissa..."
        m "I didn't know. You know I would never if..."
        m "Please, wait!"
        me "I don't want to talk right now!"
        m "Melissa!"
        scene 14_1274 with Dissolve(1)
        me "..."
        mc "{i}(She looks... Sad and angry at the same time?){/i}"
        mc "{i}(What happened? What did they talk about?){/i}"
        scene 14_1275 with Dissolve(1)
        mc "Mom?"
        mc "What just happened?"
        mc "Mom...?"
        scene 14_1276 with Dissolve(1)
        m "..."
        mc "Mom!"
        scene 14_1277 with Dissolve(1)
        m "*Crying*"
        mc "Hey, it's going to be okay."
        scene 14_1278 with Dissolve(1)
        mc "I've never seen you and Melissa fight."
        m "Because we never have. Until now..."
        mc "Can you tell me what happened?"
        scene 14_1279 with Dissolve(1)
        m "A lot!"
        mc "A lot?"
        m "*Sigh* A lot..."
        scene 14_1280 with Dissolve(1)
        m "Let me take a quick shower first. I've been in these clothes all day."
        m "And honestly, I need a few minutes to clear my head."
        mc "Is it that serious?"
        m "No, but it's... It's something. I'll come to your room and explain everything, okay?"
        mc "Alright. I'll wait."
        scene 14_1281 with Dissolve(1)
        mc "{i}(She said it's not bad, but it still sounded serious...){/i}"
        mc "..."
        jump Week6_Monday_Emily_Shower

label Week6_Monday_Emily_Shower:
    scene black with Dissolve(1)
    pause 2
    play music ("Music/Slow.mp3", "Music/Slow4.mp3") volume 0.5
    scene 14_1282 with Dissolve(1)
    m "*Sigh*"
    scene 14_1283 with Dissolve(1)
    ""
    scene 14_1284 with Dissolve(1)
    ""
    scene 14_1285 with Dissolve(1)
    ""
    scene 14_1286 with Dissolve(1)
    ""
    scene 14_1287 with Dissolve(1)
    ""
    scene 14_1288 with Dissolve(1)
    ""
    scene 14_1289 with Dissolve(1)
    ""
    scene 14_1290 with Dissolve(1)
    ""
    scene 14_1291 with Dissolve(1)
    ""
    scene 14_1292 with Dissolve(1)
    ""
    scene 14_1293 with Dissolve(1)
    ""
    scene 14_1294 with Dissolve(1)
    m "*Crying*"
    $ renpy.end_replay()
    jump Week6_Monday_MCRoom_EmilyTalk

label Week6_Monday_MCRoom_EmilyTalk:
    scene black with Dissolve(1)
    pause 2
    stop music fadeout 1.0
    play music ("Music/LoFi Upbeat 3.mp3", "Music/LoFi Upbeat 2.mp3", "Music/LoFi Upbeat 1.mp3", "Music/LoFi Upbeat 4.mp3") volume 0.2
    scene 14_1295 with Dissolve(1)
    m "Hey."
    mc "Hey. That was a long shower!"
    m "Yeah... I needed a moment to clear my head."
    mc "No worries. You alright?"
    if Erynn_Week5_Tuesday_Photoshoot_Join == False:
        scene 14_1305 with Dissolve(1)
        m "*Sigh*"
        mc "Still feeling off?"
        m "Yeah... Just trying to process everything. It's a lot."
    else:
        scene 14_1296 with Dissolve(1)
        m "Oh..."
        m "What's that?"
        mc "What?"
        scene 14_1297 with Dissolve(1)
        m "Is that you and Erynn?"
        mc "Ah, the poster? Yeah."
        m "When did you get it?"
        scene 14_1298 with Dissolve(1)
        mc "Uhm... Today?"
        mc "I think Erynn snuck in this morning and put it up."
        mc "Does she have a key to our house?"
        m "Melissa does."
        mc "Tell her to hide it better."
        scene 14_1299 with Dissolve(1)
        m "I love it! It's beautiful?"
        m "When did you take that photo? It really looks like a real ad. Was that on purpose?"
        mc "It is an actual ad."
        m "Hmm?"
        scene 14_1300 with Dissolve(1)
        mc "I was at one of Erynn's photo shoots."
        mc "They were shooting for this perfume campaign."
        mc "Normally they'd have a male model who would shoot with Erynn but for some reason he couldn't make it."
        mc "They were on a time crunch and saw me sitting there. So they asked if I could step in."
        mc "I signed a few forms, got paid... And voilà, this is the result."
        scene 14_1301 with Dissolve(1)
        m "Wow... It really turned out amazing! You look so handsome."
        mc "Thanks."
        m "Will it be in magazines or stores?"
        mc "Not sure. I'll have to ask Erynn."
        if MC_Bike == True:
            scene 14_1302 with Dissolve(1)
            m "Think Erynn can get me a copy too? I'd love to have one."
            mc "She probably can. I'll ask her."
            m "Thanks. And I want one of us, too! A nice, big picture like this."
            m "It would look great next to this one!"
            scene 14_1303 with Dissolve(1)
            mc "I'm not putting up a photo of the two of us on my wall..."
            m "What? Why not?"
            mc "I'm not even sure if I'm keeping this one up."
            m "No! Keep it! It actually brings some colour into your dull, grey room."
            if Alexis_Dating == False:
                pass
            else:
                scene 14_1304 with Dissolve(1)
                mc "Alexis might not be thrilled about it."
                mc "What girl wants her boyfriend hanging a poster of another girl in his room?"
                m "Hmm... fair point."
                m "Well, if you don't want it, I'll take it! I want one for my office anyway."
                mc "Heh..."
        else:
            pass
        scene 14_1306 with Dissolve(1)
        m "*Sigh*"
        mc "Still feeling off?"
        m "Yeah... Just trying to process everything. It's a lot."
    scene 14_1307 with Dissolve(1)
    mc "Can you tell me now what happened?"
    m "I will, but..."
    mc "But?"
    scene 14_1308 with Dissolve(1)
    m "This stays between us, okay?"
    mc "Okay..."
    m "You can't tell anyone. Especially not Erynn."
    mc "What?"
    m "At least for now."
    scene 14_1309 with Dissolve(1)
    mc "So it has something to do with Erynn?"
    m "Yes."
    if Erynn_Week3_Monday_Blackmailhelp == True:
        mc "{i}(Is this connected to the blackmail situation?){/i}"
        mc "{i}(Could they have found out John's involved with us?){/i}"
        mc "{i}(But then... why keep it from Erynn? That doesn't make sense...){/i}"
    else:
        pass
    scene 14_1310 with Dissolve(1)
    m "John is Erynn's father."
    mc "WHAT?"
    mc "This isn't some kind of joke, right?"
    m "It's not..."
    scene 14_1311 with Dissolve(1)
    mc "What? How?!"
    mc "*Shakes head* No... I mean, not how like that, but... What the hell?!"
    mc "Are you serious?"
    m "Dead serious. I was just as shocked as you are."
    m "Melissa... For her own reasons, even more so."
    scene 14_1312 with Dissolve(1)
    mc "Holy shit..."
    mc "I can't believe this..."
    mc "This... This is insane..."
    if Erynn_Week3_Monday_Blackmailhelp == False:
        pass
    else:
        scene 14_1313 with Dissolve(1)
        mc "Erynn's been looking for her dad for a while now... And she's already met him without even knowing it."
        m "What? She's been trying to find him?"
        mc "Yeah... But don't tell Melissa. Please."
        m "..."
        mc "It's not like she was actively searching. She just wanted to know who he was."
    scene 14_1314 with Dissolve(1)
    mc "So... what happens now?"
    m "I'm not sure. That's up to them."
    m "They talked a bit today. I imagine they'll talk more tomorrow."
    m "Eventually, they'll decide how and when they'll tell Erynn."
    mc "But they will tell her?"
    m "Yeah. That much is certain. They've agreed on it."
    scene 14_1315 with Dissolve(1)
    mc "Man..."
    mc "I can't even imagine what John and Melissa are feeling right now."
    mc "Their whole world's about to change. As will Erynn's."
    m "It is... In a big way."
    mc "*Shakes head*"
    scene 14_1316 with Dissolve(1)
    m "How do you feel about it all?"
    m "You've known John longer than anyone."
    mc "Honestly...? It doesn't really change anything for me."
    mc "My view of them doesn't shift because of this."
    mc "If anything... the family just got a little bigger."
    m "Yeah... That's one way to look at it."
    scene 14_1317 with Dissolve(1)
    mc "Wait..."
    mc "That means Erynn and Iris are sisters... Half-sisters or whatever."
    m "Right..."
    m "John and Melissa haven't even started unpacking that part yet."
    m "That's another conversation waiting to happen."
    if Erynn_End == True:
        scene 14_1318 with Dissolve(1)
        m "Do they know each other?"
        mc "Iris and Erynn?"
        m "Yeah."
        mc "They do."
    else:
        scene 14_1319 with Dissolve(1)
        mc "And then there's the fact that Iris likes Erynn..."
        m "What?"
        mc "Iris has a crush on Erynn."
        m "Oh... That complicates things..."
        mc "Uh-huh. This is going to be... I don't know what it's going to be... Just... Crazy..."
        scene 14_1320 with Dissolve(1)
        m "So, they know each other?"
        mc "They do. Pretty well I'd say."
        mc "Both go to MSU, and Iris shares a dormroom with Alexis."
    scene 14_1321 with Dissolve(1)
    m "Well, maybe that familiarity will help."
    mc "Maybe..."
    mc "Or it could backfire. They might start resenting each other now that everything's different."
    m "I don't think it'll come to that."
    scene 14_1322 with Dissolve(1)
    mc "John's probably going to want to spend time with Erynn... Get to know her."
    mc "Erynn might want the same. So, they both spend more time together. Which means less time with Iris..."
    m "They don't have to be kept apart. They could all be part of each other's lives."
    mc "True... You're right."
    mc "Whatever happens, though... This is gonna be one wild ride."
    scene 14_1323 with Dissolve(1)
    mc "*Sigh*"
    mc "John is Erynn's dad..."
    if Emily_Week4_Sunday_DateJohn == False:
        pass
    else:
        scene 14_1324 with Dissolve(1)
        mc "So that whole conversation you had in the kitchen... It was about John, Melissa, and Erynn?"
        m "Mm-hmm."
        mc "Then why did you and Melissa end up fighting?"
        mc "It doesn't sound like any of that involved you directly."
        scene 14_1325 with Dissolve(1)
        m "..."
        m "It's because of John and me..."
        mc "Oh... right. The date."
        scene 14_1326 with Dissolve(1)
        mc "Still... You didn't know he was Erynn's father."
        m "Exactly. That's what I tried to explain to her."
        m "But emotions were already running high and... *Sigh*"
        mc "Yeah. I get it. It's messy... But I don't think any of this is on you."
        scene 14_1327 with Dissolve(1)
        m "Maybe I should've picked up on it."
        m "I mean... I had a pretty good idea what John looked like. Tall, muscular, blonde, tattoos..."
        m "And his name was John."
        m "When I told Melissa about the date, I even joked he looked like how I imagined her 'John' would."
        scene 14_1328 with Dissolve(1)
        mc "Come on. Don't do that to yourself."
        mc "There are probably hundreds of tall, blonde, tattooed guys named John out there."
        mc "And it's not like Melissa and John were together in the first place."
        mc "She probably just needed space. Give it a day. Things will cool down."
        scene 14_1329 with Dissolve(1)
        m "..."
        mc "..."
        scene 14_1330 with Dissolve(1)
        mc "So... What happens now between you and John?"
        m "..."
        m "Nothing..."
        m "I'm not... Uhm... I just can't."
    scene black with Dissolve(2)
    pause 2
    scene 14_1331 with Dissolve(1)
    mc "You ready for the next shock of the day?"
    m "There's more?"
    mc "Yeah. Something else happened earlier."
    m "Is this about your suspension?"
    mc "No... something different."
    scene 14_1332 with Dissolve(1)
    mc "Andres is back."
    m "Andres?"
    m "What do you mean 'back'?"
    scene 14_1333 with Dissolve(1)
    mc "He showed up at the house a couple of hours ago."
    m "What? Seriously?"
    mc "Yeah. The doorbell rang, I opened the door and... There he was."
    scene 14_1334 with Dissolve(1)
    m "What did he want? Why now?"
    mc "Apparently, he's moved back to Madison Springs."
    m "He moved back?"
    mc "Mm-hmm."
    scene 14_1335 with Dissolve(1)
    mc "He said he's sorry... That he messed up a lot."
    mc "And now he's trying to make things right."
    m "What?"
    mc "That's what he told me."
    scene 14_1336 with Dissolve(1)
    m "Make what right, exactly?"
    mc "He meant between him and me... And also between you two."
    mc "He wants to talk to you."
    m "That's not happening. Not after what he said to me the last time."
    m "Did he say anything else?"
    scene 14_1337 with Dissolve(1)
    mc "Just that he got an apartment in the city."
    m "..."
    mc "Didn't stay long. I told him John was on his way to check the car."
    scene 14_1338 with Dissolve(1)
    m "*Sighs* What is this day, even?"
    m "My car breaks down..."
    m "You get suspended..."
    m "John turns out to be Erynn's father..."
    m "And now Andres shows up out of nowhere."
    scene 14_1339 with Dissolve(1)
    mc "Yeah..."
    mc "It's been one hell of a day."
    if MC_Bike == False:
        scene 14_1340 with Dissolve(1)
        m "I'm going to bed."
        mc "What? Already? It's not even that late."
        m "I know... I'm just... Exhausted."
        scene 14_1341 with Dissolve(1)
        m "If you're hungry, order something in."
        m "I didn't get a chance to shop because... No car..."
        mc "No worries. I'll figure something out. You want me to get you anything?"
        m "No, I'm good. Thanks though."
        scene 14_1342 with Dissolve(1)
        m "Good night, [mc]."
        mc "Night, Mom!"
        scene 14_1343 with Dissolve(1)
        mc "*Sigh*"
        mc "Just one normal day... Is that too much to ask?"
        mc "{i}(I was also planning to take care of Melissa's yard today...){/i}"
        mc "{i}(Yeah... probably not the best idea right now.){/i}"
        jump Week6_Monday_Ethan
    else:
        scene 14_1344 with Dissolve(1)
        m "Can I get a hug?"
        m "I need one badly."
        mc "Sure. Come here."
        scene 14_1345 with Dissolve(1)
        m "This is perfect!"
        m "Thank you."
        mc "Anytime."
        scene 14_1346 with Dissolve(1)
        m "Good night!"
        mc "Haha. What do you mean good night?"
        mc "You're not sleeping here!"
        scene 14_1347 with Dissolve(1)
        mc "Besides, it's still way too early."
        m "Just ten minutes, please? Let me rest a little."
        mc "*Sigh* Fine. Ten minutes. That's all you get."
        m "I'll take it!"
        if Alexis_Dating == False:
            pass
        else:
            scene 14_1348 with Dissolve(1)
            mc "Hold up... Is that raspberry?"
            m "Yeah... I might've swiped it from your bathroom."
            mc "Seriously? I got that for Alexis."
            m "Sorry! I'll replace it tomorrow, I promise."
            mc "It's fine. It does smell good, right."
            m "Mm-hmm. I like it."
        scene 14_1349 with Dissolve(1)
        ""
        jump Week6_Monday_Ethan

label Week6_Monday_Ethan:
    if Erynn_Week3_Monday_Blackmailhelp == False:
        jump Episode_15_Start
    else:
        scene black with Dissolve(2)
        pause 2
        stop music fadeout 1.0
        play music ("Music/Battle_Rock2.mp3", "Music/Battle_Rock3.mp3") volume 0.5
        scene 14_1350 with Dissolve(1)
        et "Erynn..."
        et "Yes... Keep going!"
        scene 14_1351 with Dissolve(1)
        et "Yes!"
        et "Suck it, you little bitch!"
        play sound "Sounds/Phone_Vibrate.mp3"
        n "*Bzzzt. Bzzzt*"
        scene 14_1352 with Dissolve(1)
        et "..."
        n "*Bzzzt. Bzzzt*"
        scene 14_1353 with Dissolve(1)
        et "Yes?"
        x "Evening, Mr Bloomberg."
        et "Find anything?"
        scene 14_1354 with Dissolve(1)
        x "It was..."
        et "Hey! Did I tell you to stop?"
        x "..."
        scene 14_1355 with Dissolve(1)
        et "Sorry. What was that?"
        x "It was much easier to find information on John Vančura than that elusive Kyle Johnson."
        et "I bet... Tell me everything you found!"
        scene 14_1356 with Dissolve(1)
        x "John Vančura, forty-one years old, widowed."
        x "Was married to Evelyn Silvan. She passed away fourteen years ago from cancer, leukaemia."
        x "They have a daughter, Iris Vančura."
        scene 14_1357 with Dissolve(1)
        et "Hmm... Iris, you say?"
        x "Yeah, she's a freshman at MSU and works as an accountant at her dad's garage."
        x "Want me to dig into her, too?"
        et "I've got that covered."
        scene 14_1358 with Dissolve(1)
        x "Anyway. He grew up in Alvarado. Was a professional motorbike racer in the NMC."
        et "NMC?"
        x "National Moto Circuit."
        x "Two-time champion, high risk, but very skilled."
        scene 14_1359 with Dissolve(1)
        x "He retired when his wife got sick to care for her and their daughter."
        x "Later worked as a mechanic at the track before opening Vančura Motors in Madison Springs eight months ago."
        et "Only eight months? That's recent. How's his financial status?"
        x "Stable. The garage makes a modest but steady income, no debts or red flags."
        scene 14_1360 with Dissolve(1)
        et "Why did he..."
        et "Wait!"
        et "Give me a second!"
        scene 14_1361 with Dissolve(1)
        et "..."
        x "Mmm..."
        scene 14_1362 with Dissolve(1)
        et "Make sure you don't get anything on my clothes!"
        x "..."
        scene 14_1363 with vpunch
        pause 2
        scene 14_1363 with vpunch
        et "Ohh... Erynn..."
        scene 14_1364 with Dissolve(1)
        et "Swallow it!"
        x "..."
        et "Good girl!"
        scene 14_1365 with Dissolve(1)
        n "*Slap*"
        x "..."
        et "Now clean yourself up and take a seat. I have business to attend to."
        scene 14_1366 with Dissolve(1)
        et "Sorry about that, had to finish... something."
        x "No worries."
        et "So, why'd he move to Madison and not open a garage in..."
        x "Alvarado."
        et "Yeah..."
        scene 14_1367 with Dissolve(1)
        x "He was planning to leave Alvarado for Novasota. Got offered a mechanic job on a racing team there."
        x "But then the Madison Springs garage became available."
        x "He took the opportunity and bought it."
        et "Hmm..."
        scene 14_1368 with Dissolve(1)
        et "Why Madison? Did you find anything suspicious about the sale?"
        x "No, all clean. Previous owner retired and sold it legitimately. Paperwork checked out."
        et "*Sigh*"
        et "Seems like an ordinary guy. So why is he...?"
        scene 14_1369 with Dissolve(1)
        x "That's what I thought, until I came across some more information."
        et "More information?"
        x "It cost me some favours to get this."
        et "I'll compensate you for it. Just tell me!"
        scene 14_1370 with Dissolve(1)
        x "Over twenty years ago, someone was searching for him."
        et "Oh? Why?"
        x "No details, just a name so far."
        x "Wanted to check if you're interested before digging deeper."
        scene 14_1371 with Dissolve(1)
        et "Of course I am! I told you I want everything!"
        et "What's the name?"
        x "Uhm... Let's see... Melissa Orlandi."
        scene 14_1372 with Dissolve(1)
        et "..."
        et "Orlandi?"
        x "Yes, Melissa Orlandi."
        et "..."
        scene 14_1373 with Dissolve(1)
        et "Haha."
        et "Hahaha..."
        x "..."
        scene 14_1374 with Dissolve(1)
        et "Haha."
        et "There's just no way..."
        et "He's her dad?! Does he know? Does she? I don't think so..."
        scene 14_1375 with Dissolve(1)
        x "What's going on?"
        et "Nothing, nothing. You did great."
        x "Want me to look more into Melissa Orlandi?"
        et "No, no need. I have what I wanted."
        et "I'll get you the money tomorrow."
        scene 14_1376 with Dissolve(1)
        et "Haha."
        et "The last piece of the puzzle..."
        et "You're gonna be mine! Very soon!"
        et "My sweet Erynn!"
        scene 14_1377 with Dissolve(1)
        et "..."
        if Erynn_Week5_Tuesday_Photoshoot_Join == False:
            if Melissa_LikeMC == False:
                jump Episode_15_Start
            else:
                jump Week6_Monday_Melissa
        else:
            scene 14_1378 with Dissolve(1)
            x "Hmm? Who's that?"
            et "Who's who?"
            x "The handsome guy with Erynn in the new Allure ad."
            et "You mean Zane?"
            x "That's not Zane!"
            scene 14_1379 with Dissolve(1)
            et "What do you mean?"
            et "You're talking about the Desire perfume ad?"
            x "Yes."
            et "That's Zane."
            x "I know Zane. This isn't him."
            scene 14_1380 with Dissolve(1)
            et "Yes it is. I signed the contract myself."
            x "And I'm telling you, it's not him."
            et "Show me!"
            scene 14_1381 with Dissolve(1)
            et "WHAT THE FUCK?"
            et "Why is he in those pictures?"
            x "Who is he?"
            et "A fucking pain in the ass, that's who!"
            scene 14_1382 with Dissolve(1)
            et "AAAH!"
            et "Ruining my good mood, again!"
            x "..."
            scene 14_1383 with Dissolve(1)
            et "He always gets in my way... But enough is enough!"
            et "..."
            et "Hey, it's me again!"
            et "I forgot something. There's something else I need."
            et "And I need it by tomorrow!"
            scene black with Dissolve(1)
            pause 2
            scene 14_1384 with Dissolve(1)
            et "..."
            scene 14_1385 with Dissolve(1)
            et "Put your wig back on."
            x "Uhm..."
            et "I said, put your wig back on!"
            scene 14_1386 with Dissolve(1)
            et "Yes!"
            et "Much better! My sweet Erynn!"
            x "..."
            scene 14_1387 with Dissolve(1)
            x "Hey!"
            scene 14_1388 with Dissolve(1)
            x "Ethan!"
            scene 14_1389 with vpunch
            x "Ethan, wait!"
            scene 14_1390 with vpunch
            x "Ahh..."
            scene 14_1391 with Dissolve(1)
            et "If you act like a bitch, Erynn! You're gonna get treated like one!"
            scene 14_1392 with Dissolve(1)
            x "Ethan..."
            x "I'm not Erynn! I'm just pretending to be her. Remember?"
            et "Shut up!"
            scene 14_1393 with Dissolve(1)
            x "Ethan!"
            scene 14_1394 with vpunch
            x "Aaah..."
            scene 14_1395 with Dissolve(1)
            et "You like it raw, huh? You bitch!"
            et "Do you like my big dick in your wet pussy?"
            et "Do you like it, Erynn!"
            scene 14_1396 with Dissolve(1)
            et "Answer me!"
            x "Yes..."
            x "I... Like it..."
            if Melissa_LikeMC == False:
                jump Episode_15_Start
            else:
                jump Week6_Monday_Melissa

label Week6_Monday_Melissa:
    if _in_replay:
        $ Erynn_Week5_Tuesday_Photoshoot_Join = True
        $ Zach_Week6_Monday_Punch = False
        $ SexCounter_Melissa = 0
        $ MC_SexCounter = 0
    $ SexCounter_Melissa += 1
    $ MC_SexCounter += 1
    $ Melissa_Week6_Monday_Sex = True
    scene black with Dissolve(2)
    pause 2
    stop music fadeout 1.0
    play music ("Music/LoFi Upbeat 1.mp3", "Music/LoFi Upbeat 2.mp3", "Music/LoFi Upbeat 3.mp3", "Music/LoFi Upbeat 4.mp3") volume 0.2
    scene 14_1397 with Dissolve(1)
    mc "I think I've given you plenty of time now."
    m "You have!"
    scene 14_1398 with Dissolve(1)
    m "Thank you!"
    m "I really needed this."
    scene 14_1340 with Dissolve(1)
    m "I'm going to bed."
    mc "What? Already? It's not even that late."
    m "I know... I'm just... Exhausted."
    scene 14_1341 with Dissolve(1)
    mc "Alright, I'll go grab something to eat, then."
    m "We don't have much, since I couldn't go shopping without a car."
    mc "No worries. I'll just order something. Want anything?"
    m "I'm good, thanks."
    scene 14_1342 with Dissolve(1)
    m "Good night, honey."
    mc "Night, Mom!"
    scene 14_1399 with Dissolve(1)
    m "Hey, can you do me a favour?"
    mc "Sure."
    m "Can you check on Melissa? I don't think Erynn's there today, and I want to make sure she's okay."
    mc "You don't want to go yourself?"
    m "I'm scared."
    scene 14_1400 with Dissolve(1)
    m "Please?"
    mc "Sure. I'll go."
    m "Thank you."
    if Erynn_Week5_Tuesday_Photoshoot_Join == False:
        scene 14_1401 with Dissolve(1)
    else:
        scene 14_1402 with Dissolve(1)
    mc "If I'm not back by tomorrow, go check if I'm floating in her pool."
    m "Don't say that!"
    mc "Haha."
    scene black with Dissolve(1)
    pause 2
    scene 14_1403 with Dissolve(1)
    mc "{i}(Now I'm the one who's getting scared...){/i}"
    mc "{i}(No! Nervous! I'm nervous! Not scared!){/i}"
    mc "{i}(But what exactly am I nervous about?){/i}"
    mc "*Sigh*"
    mc "{i}(Also, I didn't do her yard today. So much happened, I completely forgot.){/i}"
    mc "{i}(Guess I can do it tomorrow.){/i}"
    scene 14_1404 with Dissolve(1)
    mc "{i}(Alright...){/i}"
    mc "{i}(Is she here? Hard to tell with the glare. The tinted windows aren't helping either.){/i}"
    mc "{i}(I didn't want to ring the doorbell in case she's...){/i}"
    mc "{i}(Sleeping... Is she sleeping?) {/i}"
    mc "{i}(I'll just knock softly. If she doesn't respond, I'll leave her be.){/i}"
    scene 14_1405 with Dissolve(1)
    n "*Knock-knock*"
    me "..."
    me "Come on in! It's open."
    scene 14_1406 with Dissolve(1)
    me "Hey!"
    mc "Hey, Mel! Did I wake you?"
    me "No-no. I was just resting my eyes."
    mc "Come here!"
    scene 14_1407 with Dissolve(1)
    me "..."
    mc "..."
    scene 14_1408 with Dissolve(1)
    mc "{i}(Always at the worst moments!){/i}"
    mc "{i}(Stop getting hard every time Mel hugs you, you fool!){/i}"
    mc "{i}(Still...){/i}"
    mc "{i}(I could stay like this forever!){/i}"
    scene 14_1409 with Dissolve(1)
    me "You heard, huh?"
    mc "Mm-hmm."
    mc "Is it okay that Mom told me?"
    me "Yes."
    scene 14_1410 with Dissolve(1)
    mc "Maybe a stupid question, but how are you feeling?"
    me "I'm good, I think?"
    mc "I guess it's normal to feel... confused?"
    me "Among other things..."
    scene 14_1411 with Dissolve(1)
    mc "I know you talked with Mom for a long time and she told me a bit..."
    mc "But... do you want to talk about it with me?"
    me "We can talk."
    me "But if we do, I'll need a beer. Or a few..."
    mc "Hehe."
    scene 14_1412 with Dissolve(1)
    mc "Can you grab me one too?"
    me "No! It's a school night!"
    mc "I don't have school tomorrow."
    me "Yes, you do!"
    scene 14_1413 with Dissolve(1)
    mc "Nope. In fact, I don't have school until Friday."
    me "Why's that?"
    mc "Mom didn't tell you? I'm suspended."
    me "You're lying!"
    mc "No, I'm not!"
    scene 14_1414 with Dissolve(1)
    me "You're really suspended?"
    mc "Yeah. Nothing to brag about."
    me "What happened?"
    mc "Get me a beer and I'll tell you."
    scene 14_1415 with Dissolve(1)
    me "..."
    me "Fine!"
    me "But if you're fooling me, there will be consequences!"
    mc "Haha, okay."
    scene black with Dissolve(1)
    pause 2
    scene 14_1416 with Dissolve(1)
    me "Getting comfortable already, huh?"
    mc "You bet."
    me "Here's your beer. Alcohol-free, of course."
    mc "Yeah, right. Like you keep alcohol-free beer at home, Melissa... I know you too well."
    me "Haha, you're making me sound like an alcoholic. And no, it's definitely not alcohol-free..."
    scene 14_1417 with Dissolve(1)
    me "Cheers!"
    mc "Cheers."
    scene 14_1418 with Dissolve(1)
    me "You first!"
    me "So, why'd they suspend you?"
    mc "Fighting at school."
    me "Fighting? What happened?"
    scene 14_1419 with Dissolve(1)
    if Zach_Week6_Monday_Punch == True:
        mc "I punched someone in the face."
        mc "He deserved it though."
        me "Why's that?"
    else:
        mc "Supposedly, I punched someone."
        me "Supposedly? Did you?"
        mc "No. I just pushed him away and he fell."
        me "What made you push him?"
    scene 14_1420 with Dissolve(1)
    mc "We argued, and then he started swinging."
    mc "I just defended myself."
    me "Over a girl?"
    mc "Something like that. He's an idiot."
    mc "If it wasn't me, someone else would've thrown down sooner or later."
    scene 14_1421 with Dissolve(1)
    me "So, you're suspended until Friday?"
    mc "Yeah, three days. Plus a nice note in my permanent record."
    me "Good thing it's just suspension, not expulsion."
    if Zach_Week6_Monday_Punch == False:
        scene 14_1422 with Dissolve(1)
        mc "Like I said, I didn't even do anything. Shouldn't have been suspended."
        mc "But the teacher, who didn't even see what happened, might I add, told the principal I was fighting."
        mc "I'm gonna confront her!"
        me "Don't bother. It'll only make things worse, and you don't want a teacher against you."
        mc "*Sigh* Yeah... You're probably right..."
    else:
        mc "*Sigh* Yeah..."
    scene 14_1423 with Dissolve(1)
    mc "Now to you. That must've been a shock. Running into John like that."
    me "It was... something..."
    mc "Yeah..."
    me "I've been searching for him for years."
    me "And then, suddenly, he's right there, in your house..."
    scene 14_1424 with Dissolve(1)
    mc "What did he say when he saw you?"
    me "At first, nothing. He didn't recognise me right away."
    mc "Probably the hair and tattoos... You look different from those old photos of you at eighteen."
    me "That's exactly what he said."
    mc "And when he did realise who you were, was he as 'something' as you were?"
    me "Heh... yeah."
    scene 14_1425 with Dissolve(1)
    me "After the initial shock, we went to the kitchen for coffee and started talking."
    me "He asked how I've been, what I'm up to now. The usual small talk."
    me "He shared what he's done all these years, but honestly, I wasn't really listening."
    me "There was only one thing on my mind."
    mc "That he's Erynn's dad."
    me "Exactly."
    scene 14_1426 with Dissolve(1)
    me "I'd wanted to tell him for years and had rehearsed what I'd say if I ever saw him again."
    me "My blood was boiling and I just blurted it out."
    me "He stared at me like he was trying to process what I'd said."
    me "So, I repeated it. We have a daughter together."
    scene 14_1427 with Dissolve(1)
    me "After a tense silence, the conversation heated up."
    me "He asked if she was really his, why I hadn't reached out before, and I explained I had, and so on."
    me "That's when you walked in and Emily told you to go to your room."
    mc "Yeah... Walking in then was pretty tense."
    scene 14_1428 with Dissolve(1)
    me "..."
    mc "{i}(Did she just down that beer in one go?){/i}"
    scene 14_1429 with Dissolve(1)
    me "Eventually, we calmed down and he started asking about Erynn."
    me "I told him her name, her age..."
    me "And then something happened."
    me "I don't know what it was. The way he looked at me after hearing her name... It was strange."
    scene 14_1430 with Dissolve(1)
    mc "{i}(Because he's already met her...){/i}"
    mc "{i}(Oh, Melissa... If only you knew. There's so much more.){/i}"
    mc "{i}(I want to tell her, but it's probably best they figure this out themselves.){/i}"
    scene 14_1431 with Dissolve(1)
    me "Anyway, I kept talking about her."
    me "Despite that strange look, he seemed genuinely interested."
    me "It felt good. A little relief."
    mc "Did he say he wants to meet her?"
    me "He did. But I told him it'd have to be on my terms. I need to talk to Erynn first."
    me "I have no idea how to bring it up."
    scene 14_1432 with Dissolve(1)
    mc "Are you okay if John wants to build a relationship with her?"
    me "More than okay. Honestly, I'd prefer it."
    me "When she was little, she always wondered who he was. I told her what little I knew."
    me "It faded as she got older, but deep down, I think she still wants to meet him."
    mc "{i}(She said the same. That's good.){/i}"
    scene 14_1433 with Dissolve(1)
    me "I kept going. I even told him that..."
    me "..."
    me "Never mind."
    mc "{i}(The blackmail stuff?){/i}"
    mc "{i}(I promised to stay out of that, so better not bring it up.){/i}"
    scene 14_1434 with Dissolve(1)
    mc "{i}(If John wasn't sure Erynn was the Erynn before, he definitely is now.){/i}"
    mc "{i}(What's going through his head?){/i}"
    mc "{i}(He's not just helping a friend... He's helping his daughter. The one he didn't know he had.){/i}"
    mc "{i}(I should call him tomorrow.){/i}"
    scene 14_1435 with Dissolve(1)
    me "After that, things got quiet again."
    me "He said he needed time to process everything."
    me "We exchanged numbers, and he promised to call to meet again."
    me "That's where we left things today."
    scene 14_1436 with Dissolve(1)
    mc "So, in the end, it wasn't that bad, huh?"
    me "No, it wasn't. For a surprise meeting, if you can even call it that, I think we handled it pretty well."
    mc "Mm-hmm."
    mc "But what about Mom? When I came downstairs, you looked upset and she was trying to stop you from leaving."
    scene 14_1437 with Dissolve(1)
    mc "Did you two have a fight after?"
    me "Not really. Did Emily say we fought?"
    mc "Yeah. She seemed pretty shaken up."
    me "I might've been a bit harsh. I just needed some space."
    me "I'll talk to her tomorrow and apologise."
    scene 14_1438 with Dissolve(1)
    mc "Was it because Mom and John..."
    me "*Sigh* Not exactly, but in some way, yeah."
    mc "She blames herself. Said she should've known."
    me "Emily..."
    scene 14_1439 with Dissolve(1)
    me "Okay... uh..."
    me "You're old enough, and I've already told you about Emily and me back in college, so..."
    me "Here goes..."
    scene 14_1440 with Dissolve(1)
    me "Back then, when I talked about John and described him..."
    me "Emily always joked, 'Damn, he sounds so hot. If I ever met him, I'd probably fuck him'."
    mc "{i}(Weird, but funny that Mom talked like that when she was younger.){/i}"
    me "I knew she was joking. She even promised me she wouldn't actually do that."
    scene 14_1441 with Dissolve(1)
    me "But today, in the kitchen, when she was apologising, saying she didn't know it was him..."
    me "And yesterday, when she told me about her date. She said she imagined, just for a moment, that it was the John I..."
    me "*Sigh*"
    mc "{i}(Mom and John had sex? I know they went on a date, but...){/i}"
    mc "{i}(No... Stop thinking about that!) {/i}"
    scene 14_1442 with Dissolve(1)
    me "Even though I don't think that way, and she didn't do anything wrong, I felt betrayed for a second."
    me "I just needed to get away from that situation."
    me "That's why I left."
    mc "No, I get it."
    scene 14_1443 with Dissolve(1)
    me "Again. Your mom and I are good."
    me "I'm not mad at her at all. I'll talk to her tomorrow."
    me "And if she wants to date John, I'm okay with that."
    scene 14_1444 with Dissolve(1)
    mc "What about you? Would you want to get to know John? Or maybe even date him?"
    me "..."
    me "Get to know him? Sure."
    me "Date him? No. We met for one day, twenty-two years ago. Had a one-night stand. Never saw each other again until today."
    me "Yes, he's Erynn's father. We might become friends... That's about it."
    scene 14_1445 with Dissolve(1)
    mc "Sorry for being so nosy but can I ask why?"
    mc "Don't you find him attractive, or...?"
    me "I think he's very attractive. Even more now than back then."
    scene 14_1446 with Dissolve(1)
    me "But when I saw him earlier, besides the shock and him being Erynn's dad, there was nothing."
    me "No spark, no old feelings, no emotions stirring... Nothing."
    me "It's not like I ever loved him."
    me "That one day was beautiful. He gave me the love of my life. And... Yeah, that's it."
    scene 14_1447 with Dissolve(1)
    me "*Sigh*"
    me "I must be getting drunk, spilling all this."
    mc "Haha. I'm glad you feel comfortable enough to, though."
    mc "I really love the stories you tell from when you were younger."
    me "..."
    scene 14_1448 with Dissolve(1)
    me "Next time, you tell me one of your stories from back in Alvarado, alright?"
    mc "Sure. Though they might not be as crazy as yours."
    me "Mine only seem crazy because of your mom! Emily was the wild one!"
    mc "Haha."
    scene 14_1449 with Dissolve(1)
    me "Thanks for coming over and checking on me."
    me "I didn't want to talk about this today, but... It actually felt good."
    mc "You're welcome! I'm here anytime you want to hang out, drink beer, and talk."
    me "Haha."
    scene 14_1450 with Dissolve(1)
    me "Come here. One more hug for you!"
    mc "I'm getting spoiled today!"
    scene 14_1451 with Dissolve(1)
    me "Haha..."
    me "Not exactly what I had in mind, but okay..."
    scene 14_1452 with Dissolve(1)
    mc "What a crazy day, huh?"
    me "Mm-hmm. Definitely!"
    mc "It'll be even crazier for John when he gets the bill for child support backpay."
    me "Haha. That's funny."
    scene 14_1453 with Dissolve(1)
    me "But no, he doesn't have to pay anything."
    me "He missed out on Erynn growing up, that's worth way more than money."
    mc "Yeah, true."
    scene 14_1454 with Dissolve(1)
    me "Want another beer?"
    mc "I can have another one?"
    me "No school tomorrow, right?"
    mc "No school tomorrow!"
    scene 14_1455 with Dissolve(1)
    ""
    scene black with Dissolve(1)
    pause 2
    scene 14_1456 with Dissolve(1)
    me "Mostly like that, yeah..."
    mc "Haha. Can't imagine doing that nowadays."
    scene 14_1457 with Dissolve(1)
    mc "..."
    scene 14_1458 with Dissolve(1)
    me "What?"
    mc "I really like the blonde hair."
    mc "You look very pretty!"
    me "Thank you."
    scene 14_1459 with Dissolve(1)
    mc "Can I ask you something?"
    me "Sure."
    mc "Why didn't you ever get married?"
    mc "Now that I think about it, I don't think I've ever seen you date anyone, either."
    scene 14_1460 with Dissolve(1)
    me "It's not that I never dated."
    me "It just never really worked out."
    me "I dated in college, but most of the time, when I mentioned I had a kid, things stopped there."
    me "There were some who seemed okay with it..."
    me "But when they heard how old she was, I could see them doing the math in their heads, and their attitude changed."
    scene 14_1461 with Dissolve(1)
    me "I could almost hear them thinking, 'She got pregnant at eighteen?'"
    me "*Sigh*"
    me "Second dates were rare."
    me "Eventually, I just gave up."
    me "I have Erynn, and that's enough for me."
    scene 14_1462 with Dissolve(1)
    mc "Would you have preferred something different?"
    me "Hmm..."
    me "Hard to say. Maybe."
    me "Not just for me, but for Erynn. Having a father figure would've been nice."
    scene 14_1463 with Dissolve(1)
    mc "Well... if I were in that situation back then, I think I would've dated you."
    mc "I'd even date you now!"
    me "Haha. Thanks."
    mc "{i}(She might think I'm joking, but I'm not.){/i}"
    scene 14_1464 with Dissolve(1)
    mc "Ever thought of dating Mom?"
    me "Emily? No."
    mc "No? But didn't you... you know... in college?"
    me "How do... Right. I told you about that."
    scene 14_1465 with Dissolve(1)
    me "We were just experimenting back then."
    mc "I also saw you kiss a few weeks ago."
    me "..."
    me "I don't really know what that was. We'd been drinking, and it just happened."
    me "Emily likes to kiss when she drinks. Always has. She likes to kiss in general, I think."
    scene 14_1466 with Dissolve(1)
    mc "Speaking of Mom, what did she say when she saw your new hair at the restaurant?"
    me "Haha. I can't say."
    mc "Oh come on, Mel! It won't leave this room! Please?"
    me "I'm gonna clear out the restaurant and fuck you on this table right here."
    mc "{i}(Not just back in college, she still talks like that. Haha.){/i}"
    scene 14_1467 with Dissolve(1)
    mc "Haha, what? She said that?"
    mc "She actually said 'fuck'? In that meaning?"
    me "She did. She's got a little potty mouth."
    mc "Yeah, I know. I've experienced it a few times myself."
    me "Haha."
    scene 14_1468 with Dissolve(1)
    mc "..."
    mc "{i}(How many is that now? The fifth, sixth?){/i}"
    mc "{i}(She can easily drink me under the table.){/i}"
    mc "{i}(My head's been spinning for a while now.){/i}"
    scene 14_1469 with Dissolve(1)
    mc "{i}(She's so damn beautiful...){/i}"
    scene 14_1470 with Dissolve(1)
    mc "Did you know you were my first crush?"
    me "What? I was? I thought it was Erynn."
    mc "No, it was you!"
    me "When was that?"
    mc "I can't remember how old I was, but I remember the exact moment."
    scene black with Dissolve(2)
    pause 2
    scene 14_1471 with Dissolve(1)
    m "Stop squirming and sit still for a second."
    mc "I don't need sunscreen..."
    m "Yes, you do! Almost done."
    scene 14_1472 with Dissolve(1)
    me "You're already here."
    m "Hey, sexy mama!"
    me "Haha, hey Em! Right back at you!"
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 14_1473 at moveup
    pause 3
    mc "..."
    scene 14_1474 with Dissolve(1)
    me "Hey, handsome! How's my little heartbreaker?"
    mc "Hey, Melissa."
    scene 14_1475 with Dissolve(1)
    me "Sorry, Erynn's not here right now."
    mc "..."
    me "So, you'll have to hang out with me today."
    mc "That's fine."
    me "Lucky me!"
    scene 14_1476 with Dissolve(1)
    m "Rough day at work?"
    me "Not too bad. Got a new client. Young actress, Ximena Vergara. Super pretty."
    m "Do I know her?"
    me "She was in that teen show Lunch Table Rules."
    m "Oh. I don't think I watched that one."
    scene 14_1477 with Dissolve(1)
    m "Since my hands are already full of sunscreen..."
    m "Want me to get your back?"
    me "Yes, please. Thank you!"
    scene 14_1478 with Dissolve(1)
    m "Where's Erynn?"
    me "At a friend's house. Sleepover night."
    m "I remember ours."
    me "Except we did everything but sleep!"
    m "Haha. I had so much drama to spill."
    scene 14_1479 with Dissolve(1)
    mc "..."
    scene 14_1480 with vpunch
    n "*Slap*"
    me "Ahh! Hey!"
    m "All done!"
    me "Thanks. You could've told me without the slap!"
    m "Where's the fun in that?"
    me "Heh... Want me to do your back?"
    m "I've already put two layers on, as pale as I am."
    scene 14_1481 with Dissolve(1)
    ""
    scene 14_1482 with Dissolve(1)
    ""
    scene 14_1483 with Dissolve(1)
    mc "..."
    scene 14_1484 with vpunch
    me "Aaah!"
    m "[mc]!"
    mc "Hahaha."
    scene 14_1485 with Dissolve(1)
    me "See what you've taught him!"
    m "Me?"
    me "Yes, you! Who slapped my butt earlier? Now he's gonna be slapping every girl's butt!"
    m "Haha."
    scene 14_1486 with Dissolve(1)
    m "Better run, [mc]!"
    me "Come here, you!"
    mc "Hahaha!"
    me "Fast, but not fast enough! You're still a few years too young to outrun me!"
    scene 14_1487 with Dissolve(1)
    me "Gotcha!"
    mc "Hahaha."
    mc "Mom! Help me! Mamaaa..."
    m "Actions have consequences, honey!"
    scene 14_1488 with Dissolve(1)
    mc "Melissa... Nooo..."
    me "*Kiss-kiss-kiss-kiss-kiss*"
    mc "Hahaha."
    scene black with Dissolve(2)
    pause 2
    scene 14_1489 with Dissolve(1)
    me "I remember that."
    me "But that wasn't the first time you saw me in a bikini, you know."
    mc "I know, but... Something about that day felt different."
    scene 14_1490 with Dissolve(1)
    me "Hard to believe it's been that long already..."
    me "Now I'm this old lady."
    mc "No way. You're still as stunning as you were back then. Maybe even more."
    me "Aw... Thank you."
    scene 14_1491 with Dissolve(1)
    mc "And my crush never really went away, Melissa."
    me "..."
    scene 14_1492 with Dissolve(1)
    me "..."
    scene 14_1493 with Dissolve(1)
    me "[mc]..."
    me "I..."
    scene 14_1494 with Dissolve(1)
    me "..."
    scene 14_1495 with Dissolve(1)
    me "No..."
    me "[mc]... We ca..."
    scene 14_1496 with Dissolve(1)
    n "[mc] captures Melissa's mouth once more, this time with a fiercer urgency. He pulls her closer, his arms tightening around her as his tongue meets hers in a deep, searching kiss."
    n "His hands move instinctively, mapping the contours of her body."
    scene 14_1497 with Dissolve(1)
    n "Melissa finally gives in, no longer holding back. She crushes her lips to his in a hungry, open-mouthed kiss."
    scene 14_1498 with Dissolve(1)
    n "Her tongue slipping past his lips to tangle with his in a rhythm that makes the world fall away."
    n "A soft moan escapes her as she grips his hair, fingers curling tight, drawing him even closer."
    scene 14_1499 with Dissolve(1)
    n "Breathless and dazed, [mc] pulls back slightly, his lips still tingling from the ferocity of their kiss."
    n "His eyes drift to the elegant line of her neck, damp with the heat between them."
    n "Unable to resist, he lowers his head and presses a slow kiss to the hollow just below her jaw."
    n "Melissa exhales, a soft, breathy sound that makes his pulse quicken. She tilts her head instinctively, offering him more."
    scene 14_1500 with Dissolve(1)
    n "Encouraged, [mc] lets his lips trail downward, planting kisses across the tender skin of her throat."
    n "One hand finds her breast, still covered by the thin fabric of her tank top, and he cups it gently, reverently."
    n "The softness fills his hand as he can feel her increasing heartbeat."
    scene 14_1501 with Dissolve(1)
    n "Their kisses turn feverish again. Rougher, messier... Tongues clash, breaths collide..."
    scene 14_1502 with Dissolve(1)
    n "Their tongues continue to dance in a deep, breathless kiss."
    n "[mc] slides his hand up to cup Melissa's breast. Her warmth fills his palm, the softness and weight of her against his hand making his pulse surge."
    n "Their mouths never part, but the intensity between them deepens..."
    scene 14_1503 with Dissolve(1)
    n "[mc] stills, his gaze drawn to the quiet elegance of her bare, unhidden, unguarded breast. Time seems to narrow to that single, breathless moment."
    n "Melissa watches him closely, her breath shallow but steady."
    n "There is no trace of shyness in her eyes, only the smouldering glow of anticipation, fierce and unwavering. Desire shimmers there, but something deeper too."
    scene 14_1504 with Dissolve(1)
    n "[mc] lowers his head slowly, his breath warm against her skin. His tongue flicks softly over her nipple. Deliberate... Slow..."
    n "Melissa's eyes never leave him. She gasps, but it's quiet. The heat in her gaze deepens, her body arching subtly toward his mouth in silent invitation."
    scene 14_1505 with Dissolve(1)
    n "[mc]'s lips press to her skin again, this time drawing her erect nipple into his mouth."
    n "Melissa's breath catches a soft moan slipping from her lips. Her body trembles slightly under his touch."
    n "Her head falls back slightly, eyes closing, but the desire remains as her body responds to his every movement."
    scene 14_1506 with Dissolve(1)
    n "They sit up slowly, eyes locked on each other, the air thick with unspoken words."
    n "Melissa's breath quickens, her chest rising and falling in rhythm with the beat of her heart. She holds his gaze, the desire in her eyes matching his own."
    n "Without a word, [mc] reaches for her tank top, his hands gentle but sure. Melissa doesn't flinch, her eyes never leaving his, as he slowly exposes her skin, inch by inch."
    scene 14_1507 with Dissolve(1)
    n "The fabric slides over her breasts, revealing more of her to him, and he pauses for a brief moment, taking in the sight of her."
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 14_1508 at moveup
    pause 3
    mc "Fuck, Melissa! You're so hot!"
    me "..."
    scene 14_1509 with Dissolve(1)
    n "[mc]'s gaze drops to her bare chest, and for a moment, time seems to slow. His eyes trace the curves of her body, drinking in the sight of her exposed skin."
    n "Melissa remains still, her breath shallow, her heart beating louder in her ears. The intensity of his gaze sends a wave of heat through her."
    scene 14_1510 with Dissolve(1)
    n "[mc] pulls Melissa closer, his hands gripping her firmly as he presses their bodies together."
    n "The heat between them intensifies, and he crashes his lips against hers in a deep, passionate kiss."
    n "Melissa responds immediately, her arms wrapping around him, pulling him closer as their bodies melt into each other."
    scene 14_1511 with Dissolve(1)
    n "The kiss deepens, their tongues moving in sync, tasting and exploring with a need that's been building between them for what feels like forever."
    n "[mc]'s hands roam over her back, feeling the soft, warm skin beneath his fingertips."
    scene 14_1512 with Dissolve(1)
    n "His left hand slides lower, finding the curve of her ass. He grips it firmly, feeling the toned, supple shape beneath his fingers."
    n "The firmness of her body, the way she fits perfectly against him, only heightens the intensity of the moment."
    n "Melissa gasps softly, her breath mingling with his, her body arching toward him in response to his touch."
    scene 14_1513 with Dissolve(1)
    n "[mc] pulls back just enough to trail soft kisses along Melissa's neck. He starts at her collarbone, lips brushing against her skin with a tenderness that contrasts the heat between them."
    n "Slowly, he moves upward, his breath warm against her sensitive skin, sending shivers down her spine."
    n "Melissa tilts her head again to give him better access. Her hands tighten around him as she closes her eyes, lost in the sensation."
    scene 14_1514 with Dissolve(1)
    n "[mc] bends down slowly, his lips grazing the delicate skin of her chest before he takes her breast in his mouth."
    n "As [mc] gently sucks on her nipple, a soft moan escapes Melissa's lips."
    scene 14_1515 with Dissolve(1)
    n "Her back arches slightly, pressing herself closer to him, craving more of the heat his mouth stirs in her."
    n "The soft pull of his lips and the flick of his tongue send tingling sensations racing through her."
    n "Her breath quickens, her body fully attuned to every tender, intoxicating touch."
    scene 14_1516 with Dissolve(1)
    n "As [mc] circles her nipple with his tongue, he lifts his gaze, watching Melissa's face."
    n "Her eyes flutter closed, her mouth falling open with a soft, breathy sound."
    n "The sight of her being lost in sensation sends a fresh wave of heat through him. He lingers there, savouring both the taste of her and the way her body responds to his tongue."
    scene 14_1517 with Dissolve(1)
    n "[mc]'s grip tightens just slightly as he suckles harder at her breast, his mouth drawing more firmly against her skin."
    n "The change in pressure pulls a sharper moan from Melissa, her fingers digging into his shoulders."
    scene 14_1518 with Dissolve(1)
    n "Overwhelmed by the heat coursing through her, Melissa reaches for him, and without a word, she pulls him into another kiss."
    n "Melissa pours herself into it, her lips moving hungrily against his. Her hands hold him close, refusing to let go, needing to feel him just as much as he feels her."
    scene 14_1519 with Dissolve(1)
    n "As their kiss breaks, they remain close, breathing each other in. Melissa's fingers slide up beneath the hem of his tank top."
    n "Their eyes lock. Intense... Unblinking... Holding each other in a moment that feels both electric and tender."
    scene 14_1520 with Dissolve(1)
    n "Melissa lets the tank top fall to the floor, her eyes drawn to the bare skin now revealed before her."
    n "Her gaze moves slowly over [mc]'s chest, taking in the contours of muscle and the warmth of his skin."
    n "She lifts a hand and places it on him, her fingers trailing lightly across his chest, mapping the shape of him with a mixture of admiration and desire."
    n "[mc] watches her with a soft smile. He doesn't speak. Just lets her look, lets her touch... Relishing the way she studies him like he's something she's been craving and is finally allowed to hold."
    scene 14_1521 with Dissolve(1)
    n "Melissa leans in slowly, her lips brushing lightly against [mc]'s collarbone. Her kiss is soft at first, lingering, then trails lower to the centre of his chest."
    n "[mc] exhales, his eyes never leaving her as his hand cups her breast, his thumb brushing gently across her skin."
    n "The contact sends a subtle shiver through her, but she doesn't stop... Her lips continue downward, tasting him, breathing him in."
    scene 14_1522 with Dissolve(1)
    n "Melissa pauses and slowly lifts her gaze to meet his. Her eyes, wide and full with desire, lock onto his."
    n "She doesn't say a word, but she doesn't need to. Everything she feels, everything she wants, is there in the way she looks at him."
    n "The trust, the longing, the hunger, and something deeper still... Vulnerable... Open... Real..."
    scene 14_1523 with Dissolve(1)
    n "With a smooth, deliberate motion, [mc] pulls Melissa onto his lap, her back pressing against his body."
    n "Then, without hesitation, he leans in and claims her mouth again."
    n "Melissa responds instantly, turning her head to meet him fully, her lips parting for him as the kiss deepens, wild and consuming."
    scene 14_1524 with Dissolve(1)
    n "Their mouths part fully, and their tongues find each other with a slow, simmering hunger. The kiss is open, wet, and unrestrained, driven by raw longing rather than finesse."
    n "Each flick and glide of their tongues sends a jolt through her spine, the sensation overwhelming in its intensity."
    scene 14_1525 with Dissolve(1)
    n "Their mouths remain fused in a deep, open kiss."
    n "His hands claim the curves of her chest. He cups both of her breasts in his hands, thumbs brushing across her bare skin."
    n "Melissa arches into him slightly, a soft gasp slipping between their lips as their kiss continues."
    scene 14_1526 with Dissolve(1)
    n "[mc]'s hand glides down from her waist, fingers trailing along the curve of her hip before slipping lower."
    n "He finds the soft waistband of her leggings and rests his hand there, feeling the tension in her body rise beneath his touch."
    n "Melissa exhales shakily against his mouth, her kiss faltering for just a heartbeat as anticipation coils through her."
    n "But she doesn't pull away, if anything, she leans in closer, her body silently inviting his next move."
    scene 14_1527 with Dissolve(1)
    n "[mc]'s fingers trace lower, pressing gently against the heat between her thighs."
    n "Only the thin, stretchy fabric of her leggings separates his touch from her center."
    n "As his fingers press more firmly against her throbbing warmth, he feels a subtle dampness seeping through the fabric. An undeniable sign of her desire."
    scene 14_1528 with Dissolve(1)
    n "[mc] pushes Melissa back onto the couch. She lands softly, her body melting into the cushions beneath her, and he follows, lying next to her."
    n "Their bodies press together, and [mc]'s hand slides to the back of her neck, pulling her closer as if trying to consume every bit of her."
    scene 14_1529 with Dissolve(1)
    n "[mc] moves his hand back to the spot where he'd felt her warmth before, his fingers brushing lightly against the fabric, teasing just a little."
    n "He circles his fingers gently, feeling the growing pulse beneath the fabric while he watches her closely."
    n "Melissa's chest rises and falls with each breath. She's aware of every shift, every movement, and her lips part slightly as she clutches his arm."
    scene 14_1530 with Dissolve(1)
    n "Driven by the heat pulsing between them, [mc] boldly slips his hand beneath the waistband of Melissa's leggings."
    n "His touch is slow but certain. The moment his fingers find her, a soft, unguarded moan slips from her lips. Sweet and breathy, as if pulled from somewhere deep within."
    n "Melissa's eyes flutter closed, her body leaning into his touch."
    scene 14_1531 with Dissolve(1)
    n "[mc] leans in again and places his lips over her breast. Savouring every inch of Melissa's peaked nipple."
    n "His fingers circle Melissa's most sensitive spot."
    scene 14_1532 with Dissolve(1)
    n "[mc] withdraws, locking eyes with Melissa before settling down on the floor in front of the couch, his hands gently placed on her waist."
    n "He glances up at her, his fingers lightly brushing the soft material of her leggings, silently seeking her consent."
    n "Melissa returns his gaze, her expression a blend of tenderness and anticipation, and with a slow, intentional nod, she grants him the approval he seeks."
    scene 14_1533 with Dissolve(1)
    n "Slowly, he pulls her leggings down, his eyes never leaving hers."
    n "As the fabric slides over her skin, she shifts slightly, helping him ease the pants off."
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 14_1534 at moveup
    pause 3
    n "Melissa lies before him, her posture just a little tentative, as if unsure how to be fully seen."
    n "The soft contours of her body are highlighted by the sun coming through the windows."
    n "[mc]'s eyes scan over her, taking in every detail, the way her skin glows, the way her tattoos trace elegant lines across her curves, adding to the story her amazing body tells."
    n "His voice is low, filled with awe, as he leans closer."
    mc "You look incredible, Melissa!"
    scene 14_1535 with Dissolve(1)
    n "[mc] gets up, his gaze never leaving hers as he crawls over her, his hands braced on either side of her."
    n "Melissa watches him with parted lips and wide eyes, her heartbeat quickening as the space between their bodies slowly disappears."
    scene 14_1536 with Dissolve(1)
    n "[mc] lowers himself over her, his body pressing against hers."
    n "Clothed in only his joggers, he aches to feel every inch of her naked body."
    n "Their lips meet in a deep, fervent kiss. Slow at first, then growing more insistent."
    scene 14_1537 with Dissolve(1)
    n "With the sight of her naked body etched into his mind, [mc] feels an irresistible pull to taste every part of her."
    n "He leans in from their kiss, his lips moving to her neck, where he begins to explore her skin with slow, deliberate kisses."
    scene 14_1538 with Dissolve(1)
    n "A soft gasp escapes Melissa as [mc]'s mouth moves lower, his tongue tracing a warm path across her skin."
    n "She arches her back instinctively, offering more of herself. The swell of her breast rises to meet him as he lingers there once more, savouring all of her."
    scene 14_1539 with Dissolve(1)
    n "[mc] continues to trail soft kisses down her body, his lips finding the gentle curve of her stomach."
    n "A faint giggle escapes Melissa as his lips brush her stomach. It tickles, just a little, but the warmth of the sensation quickly overcomes it."
    n "Melissa draws in a sharp breath, biting her lip as her legs instinctively wrap around him."
    scene 14_1540 with Dissolve(1)
    n "[mc] turns his head, his cheek brushing the smooth skin of Melissa's inner thigh wrapped snugly around him."
    n "He presses a slow, deliberate kiss there, then traces a line with his tongue along her skin."
    scene 14_1541 with Dissolve(1)
    n "[mc] shifts, moving back to where he started. Kneeling in front of the couch, framed between Melissa's legs."
    n "She wraps them around his shoulders with ease, drawing him closer, her breath catching as their eyes meet again."
    n "His hands slide up her sides, anchoring her gently as the tension deepens."
    scene 14_1542 with Dissolve(1)
    n "[mc]'s gaze lowers, lingering for a moment on the soft curve of Melissa's hips."
    n "His expression shifts. Part admiration, part awe."
    n "Melissa watches him with a quiet, knowing smile, her legs still gently resting around his shoulders."
    n "Now in front of him, Melissa's delicate and beautiful pink pussy."
    scene 14_1543 with Dissolve(1)
    mc "You ready?"
    n "[mc]'s voice is low, a whisper that seems to vibrate through the room, sending a shiver down Melissa's spine."
    n "Melissa's response is a nod, barely perceptible, her throat too tight to form words."
    n "Her breath catches as [mc] leans in, his lips brushing against the sensitive skin of her inner thigh, a teasing prelude to what is to come."
    scene 14_1544 with Dissolve(1)
    n "The touch is feather-light, a deliberate tease that makes Melissa arch her back slightly, a soft gasp escaping her lips."
    n "[mc] takes his time, his mouth trailing kisses along the curve of her thigh, his tongue darting out to taste the salt of her skin."
    n "Each touch is a promise, a hint of what is to come, and Melissa's body responds eagerly, her muscles tensing, her breath quickening."
    me "[mc]... Don't tease..."
    scene 14_1545 with Dissolve(1)
    n "The words are barely out of her mouth before [mc] obliges."
    n "[mc]'s lips hover just above her core, his breath warm against her sensitive skin."
    n "She feels [mc]'s hair brushing against her thighs, his hands smoothing over her hips, grounding her even as her mind spins with wanting."
    n "Melissa's eyes close, her head falling back against the couch cushion as she surrenders to the sensation."
    scene 14_1546 with Dissolve(1)
    n "[mc]'s mouth descends, his lips pressing softly against her, a gentle kiss that makes Melissa's toes curl."
    n "Her hands form fists in the couch cushions, her body arching involuntarily as [mc]'s tongue traces a slow, deliberate path along her folds."
    mc "Fuck, you taste so good!"
    scene 14_1547 with Dissolve(1)
    n "[mc]'s hands grip her hips firmly, holding her in place as his mouth works its magic, his tongue delving deeper, his lips sucking gently at her most sensitive spot."
    n "The sensation is overwhelming, a tidal wave of pleasure that threatens to sweep her away."
    n "Her fingers are tangled in his hair, holding him in place as she grinds her hips against his face, prolonging the pleasure that was building inside her."
    me "Yes, just like that!"
    scene 14_1548 with Dissolve(1)
    n "Melissa's head thrashes from side to side, her body writhing beneath [mc]'s touch."
    n "She is lost in the moment, her mind a blank canvas painted only with the colours of desire."
    n "The room is filled with the sounds of their passion. Melissa's ragged breaths, the soft wet sounds of [mc]'s mouth against her, the faint creak of the couch as they move in sync."
    scene 14_1549 with Dissolve(1)
    n "As [mc]'s tongue flicks over her clit, Melissa's body goes rigid, her back arching sharply as a cry tears from her throat."
    n "Her orgasm crashes over her like a wave, a surge of pleasure that leaves her shaking."
    me "Oh God, [mc]!"
    n "[mc]'s lips brush against her one last time, a soft kiss that makes her shudder, before they pull back."
    scene 14_1550 with Dissolve(1)
    mc "We're not done yet!"
    n "Melissa's eyes widen, her breath catching as she realises what is coming next."
    n "[mc] drops his pants on the floor, revealing his already erect member to Melissa."
    mc "You look so fucking sexy! I can't wait to be inside you."
    scene 14_1551 with Dissolve(1)
    n "The space between them charges with anticipation."
    n "Melissa's legs wrap once more around [mc]'s waist, her ankles digging into his back as she pulls him closer, her lips seeking his in a hungry kiss."
    n "Their tongues tangle, a desperate dance that mirrors the rhythm of their bodies."
    scene 14_1552 with Dissolve(1)
    n "[mc] grabs and rubs the head of his cock through her wet folds."
    me "Teasing me again?"
    n "Melissa is more than ready, lifting her hips to take him in."
    scene 14_1553 with Dissolve(1)
    n "They both groan as he slowly enters her, inch by delicious inch..."
    scene 14_1554 with Dissolve(1)
    n "Until he is fully seated inside her soaked pussy."
    n "They take a moment to adjust, savouring the feeling of finally being joined together."
    scene 14_1555 with Dissolve(1)
    n "The sensation is overwhelming, a fullness that makes Melissa gasp, her nails digging into [mc]'s shoulders as they begin to move."
    n "Their hips rocking in a steady rhythm that sends shivers of pleasure through her."
    n "The couch creaks beneath them, the white velvet cushions a soft backdrop to the raw, primal act unfolding on it."
    show 14_1556
    n "Melissa watches intensely, biting her lip as [mc]'s thrusts grow deeper, more urgent."
    n "The room is filled with the sounds of their passion."
    n "The soft slap of skin against skin, the creak of the couch, the ragged breaths that escape their lips."
    show 14_1557
    mc "Oh, Melissa!"
    n "Melissa's body is a live wire, every nerve ending humming with anticipation as she feels the familiar coil of pleasure tightening inside her, a promise of another orgasm that is building."
    scene 14_1558 with Dissolve(1)
    n "As their movements quicken, Melissa's hands tangle in [mc]'s hair, pulling him down for another kiss."
    n "Their lips crash together in a desperate, hungry embrace."
    scene 14_1559 with Dissolve(1)
    n "Just when she thinks it can't get any better, in one fluid motion, [mc] flips her over."
    n "Melissa gasps softly as she finds herself on top. They pause for a breath, eyes meeting..."
    mc "Ride me!"
    scene 14_1560 with Dissolve(1)
    n "Without hesitation, Melissa lifts up."
    n "She straddles [mc]'s hips, her hands resting on his chest as she positions herself above his throbbing cock."
    n "His hands rest lightly on her hips, but his gaze is fixed upward, captivated."
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 14_1561 at moveup
    pause 3
    n "There's a quiet awe in his eyes, as if seeing her like this... Confident, radiant, and so close, leaves him momentarily breathless."
    mc "You're so beautiful!"
    n "Melissa smiles down at him, her fingers tracing the lines of his chest, as if she can feel the effect she has on him without a word."
    scene 14_1562 with Dissolve(1)
    n "Slowly, Melissa lowers herself onto [mc]'s tip, gasping as she feels it press against her aching entrance."
    n "She pauses there for a moment, relishing the anticipation, the way [mc]'s breath hitches in his throat as he waits for her to continue."
    me "That's for teasing me earlier!"
    mc "Haha."
    scene 14_1563 with Dissolve(1)
    n "Then, with a roll of her hips, Melissa sinks onto [mc]'s cock, taking him deep inside her."
    n "A low moan escapes her lips as she is stretched and filled, his thickness fitting perfectly inside her."
    mc "Fuck, Melissa!"
    show 14_1564
    n "Melissa begins to move, raising herself until just the tip remains inside her, then slamming back down."
    n "She sets a steady rhythm, riding [mc] with long, deep strokes that have them both panting with pleasure."
    scene 14_1565 with Dissolve(1)
    n "As Melissa rides [mc], he reaches out and grabs two handfuls of her ass."
    n "The firm, round globes fit perfectly in his palms, and [mc] can't resist giving them a squeeze."
    me "Grab my ass harder!"
    scene 14_1566 with Dissolve(1)
    n "[mc] slaps her ass and tightens his grip."
    n "Melissa lets out a little yelp of surprise, followed by a moan of pleasure as [mc]'s fingers dig into her flesh."
    n "Each slap of her ass against his thighs, each jiggle and bounce of her cheeks in his hands only adds to the intensity of the moment."
    scene 14_1567 with Dissolve(1)
    n "Melissa's eyes roll back in her head, her moans growing louder and more desperate as [mc] manhandles her ass."
    me "I love it when you touch me like that!"
    mc "I love touching you!"
    show 14_1568
    n "Melissa keeps riding [mc], her breasts bouncing rhythmically with each roll of her hips. They jiggle and sway, the soft mounds rising and falling in time with her movements."
    n "[mc]'s eyes are glued to the mesmerising sight, his gaze flicking from Melissa's face to her chest and back again."
    n "The way her hardened nipples dance in the air, the slight sheen of sweat that makes her breasts glisten in the low light, it is all incredibly arousing."
    scene 14_1569 with Dissolve(1)
    n "Unable to resist, [mc] reaches up and cups Melissa's breasts in his hands, kneading the soft flesh and rolling her nipples between his fingers."
    n "Melissa lets out a gasp of pleasure, her head falling back as [mc] continues his exploration."
    scene 14_1570 with Dissolve(1)
    n "Sweat drips down their bodies as they move together, lost in a haze of pleasure. Melissa can feel another orgasm building, her walls starting to flutter around [mc]'s thick length."
    me "I'm so close!"
    n "With a final, hard thrust, Melissa flies apart, screaming [mc]'s name as her orgasm crashes over her in waves."
    me "[mc]... [mc]..."
    show 14_1571
    stop music fadeout 1.0
    play music "Music/Suspense.mp3" volume 0.5
    me "[mc]!"
    scene 14_1572 with Dissolve(1)
    me "*Heavy breathing*"
    me "Why do I keep having that same dream?"
    me "And how much did I drink last night?"
    me "*Sigh...*"
    scene 14_1573 with Dissolve(1)
    me "..."
    $ renpy.end_replay()
    jump Episode_15_Start

# Max Points:

# Alexis (46)
# Melissa (18)
# Layla (102)
# Elena (48)
# Emily (22)
# Erynn (64)
# Tori (18)
# Cara (16)
# Nikki (20)
# Lakeyn (6)
# Brooke (10)
# Adriana (6)
# Naomi (2)
# Valeria (28)
# Zach (10)
# Darryl (4)
# ShaCarri (4)
# Iris (6)
# Sienna (4)
# Andres (2)

# MC_GoodStudent (14)

# Nikki_Weekend (10)
# Nikki_Visit (40)
# Nikki_SP (4)
# Cara_Weekend (6)
# Cara_Visit (44)
# Alexis_SP (20)
# Alexis_Jealous (16)
# Alexis_Beach (16)
# Gabi_Jealousy (4)
# Gabi_Suspicion (4)

# MC_Sex (47)
# Alexis_Sex (10)
# Tori_Sex (3)
# Lakeyn_Sex (1)
# Nikki_Sex (9)
# Cara_Sex (10)
# Julia_Sex (1)
# Rachel_Sex (1)
# Gabi_Sex (3)
# Iris_Sex (4)
# Layla_Sex (2)
# Mira_Sex (2)
# Melissa_Sex (1)

# Emily_Sex (1)

#WTAdded
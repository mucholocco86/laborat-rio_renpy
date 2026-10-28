label Episode_7_Start:

    #KoGa3 START#
    $ KoGa3GameProgress = "Ep7"
    #KoGa3 END#

    $ achievement.grant("ACHIEVEMENT_EPISODE_6")
    $ achievement.sync()
    $ Emily_Week2_Saturday_Checkup = False
    $ Brooke_Week2_Saturday_TurnDown = False
    $ Team_Triss = False
    $ Team_Yennefer = False
    $ Adriana_Week2_Sunday_Dinner = False
    $ Alexis_Week2_Sunday_Honest = False
    $ Layla_Week2_Sunday_TV_Makeout = False
    $ Alexis_Week2_Sunday_PhoneSex = False
    $ Valeria_Week3_Monday_Meet = False
    $ Valeria_Week3_Monday_NotMyType = False
    $ Week3_Monday_Spanish_Steal = False
    $ Week3_Monday_Spanish_Blackmail = False
    $ Layla_Week3_Monday_Spanish_Fail = False
    $ Elena_Week3_Monday_Help = False
    $ Elena_Week3_Monday_CheerTraining = False
    $ Elena_Week3_Monday_Backflip = False
    $ Erynn_Week3_Monday_Help = False
    $ Erynn_Week3_Monday_Blackmailhelp = False
    $ Erynn_End = False
    $ Alexis_End = False
    $ Elena_Friends = False
    $ Valeria_Friends = False
    $ Erynn_Week3_Monday_Alexis_Mention = False
    $ Erynn_Week3_Monday_Makeout = False
    $ Erynn_Week3_Tuesday_Sandwich = False
    $ Layla_Week3_Tuesday_Train = False
    $ Layla_Week3_Tuesday_Race = False
    $ Layla_Week3_Tuesday_Race_Win = False
    $ Alexis_Week3_Tuesday_Date = False
    $ Alexis_Week3_Tuesday_LexySexySong = False

    if Andres_FB_Punch == False:
        jump Week2_Saturday_Restaurant
    else:
        jump Week2_Saturday_Restaurant2

label Week2_Saturday_Restaurant:
    scene black with Dissolve(2)
    pause 2
    stop music fadeout 1.0
    play music ("Sounds/Restaurant_Background.mp3", "Sounds/Restaurant_Background2.mp3", "Sounds/Restaurant_Background3.mp3") volume 0.2
    n "Saturday, 15:42. Rue Madison restaurant."
    scene 07_001 with Dissolve(2)
    mc "Hey, Mom. Hi, Brooke."
    br "Hi."
    scene 07_002 with Dissolve(1)
    m "Hey... What are you doing here?"
    m "I told you I'd pick you up at the airport."
    mc "..."
    scene 07_003 with Dissolve(1)
    m "Wait... It's Saturday. Why are you back already?"
    m "Isn't the wedding today?"
    scene 07_004 with Dissolve(1)
    mc "*Sigh*"
    m "What happened? Come sit down."
    scene black with Dissolve(1)
    pause 2
    scene 07_005 with Dissolve(1)
    m "..."
    m "I can't believe this. That again? I don't know how many times I've tried to explain."
    m "He's still accusing me of cheating while he's the actual cheat..."
    m "I misjudged him completely."
    scene 07_006 with Dissolve(1)
    m "Why is he still hung up about that after all these years?"
    m "I know that meeting up with Santiago wasn't the smartest thing to do. But I told him the same day that I ran into him."
    m "After that, I told Andres whenever I was going to meet him. I asked him if he wanted to join us."
    m "But he was fuming that I even considered asking him."
    m "So after that, I didn't mention it again."
    scene 07_007 with Dissolve(1)
    mc "Do you know why Andres hates Santiago so much?"
    m "*Sigh* Yes..."
    m "He told me once we were married."
    m "Before we met, there was another girl Andres really liked."
    m "The day they were supposed to go on a date, he saw Santiago making out with her."
    mc "She cheated on him?"
    m "As far as I know, they weren't dating."
    scene 07_008 with Dissolve(1)
    mc "So, that's why Andres started talking to you? To get revenge?"
    m "What?"
    scene 07_009 with Dissolve(1)
    m "..."
    mc "Mom?"
    m "..."
    mc "I..."
    scene 07_010 with Dissolve(1)
    mc "Sorry. I was just..."
    m "No, it's fine. Give me a moment."
    mc "Uh... Yeah."
    scene black with Dissolve(1)
    pause 2
    scene 07_011 with Dissolve(1)
    m "How could you do this?"
    mc "..."
    m "So you just used me?"
    mc "..."
    m "At first? AT FIRST? That doesn't change anything... Who are you?"
    scene 07_012 with Dissolve(1)
    br "Is Emily alright?"
    mc "I don't know..."
    scene 07_013 with Dissolve(1)
    m "*Crying* That motherfucker!"
    mc "..."
    menu:
        "Check up on her[KoGa3AutoWTChange1]{size=-4}(Emily Week2 Saturday Checkup, Brooke Points+2, Emily Points+2) {/size} {/color}":
            $ Emily_Week2_Saturday_Checkup = True
            $ Brooke_Points += 2
            # Brooke (4)
            $ Emily_Points += 2
            # Emily (12)
            scene 07_014 with Dissolve(1)
            mc "I'm going to check up on her."
            br "Thanks."
            scene black with Dissolve(1)
            pause 2
            scene 07_016 with Dissolve(1)
            mc "Mom... Are you alright?"
            scene 07_017 with Dissolve(1)
            m "I'm so sorry. Andres, he..."
            mc "There's nothing to be sorry about."
            scene 07_018 with Dissolve(1)
            m "*Crying*"
            scene black with Dissolve(1)
            pause 2
            scene 07_019 with Dissolve(1)
            mc "Give me your phone."
            m "You're not going to call him, are you?"
            mc "I'm not. I'm deleting his number and blocking him."
            scene 07_020 with Dissolve(1)
            mc "Done! It's over now. Let's close this chapter for good."
            m "..."
            mc "Yeah."
            scene black with Dissolve(1)
            pause 2
            scene 07_021 with Dissolve(1)
            m "*Sigh* I feel so bad for Haley. How is she doing?"
            mc "I don't know actually. I haven't spoken to her."
            scene 07_022 with Dissolve(1)
            m "What? Why not?"
            mc "I don't know. Lots happened that day and I thought it was better not to."
            m "Call her, and give me her number too. I'd like to talk to her."
            mc "..."
            mc "Okay."
            scene 07_023 with Dissolve(1)
            mc "Here you go."
            m "Thanks."
            m "Can you check if Brooke needs some help?"
            mc "Uhm sure."
            m "Thank you."
            scene black with Dissolve(1)
            pause 2
            scene 07_024 with Dissolve(1)
            br "How is Emily doing?"
            mc "She'll be fine."
            mc "Do you need some help?"
            scene 07_025 with Dissolve(1)
            br "I'm okay for now. Not many customers at this moment and Jaylen will be arriving in twenty minutes."
            mc "New guy?"
            br "Yeah."
            scene 07_026 with Dissolve(1)
            br "Here you go, sir."
            x "Thank you."
            br "You're welcome."
            menu:
                "Check her out":
                    scene black with Dissolve(1)
                    transform moveup:
                        xalign 0.5 yalign 1.0
                        linear 5.0 yalign 0.0
                    show 07_027 at moveup
                    pause 3
                    mc "{i}(She has a really cute smile.){/i}"
                    mc "{i}(Must be getting lots of tips that way.){/i}"
                    scene black with Dissolve(2)
                    pause 2
                "Don't":
                    scene black with Dissolve(2)
                    pause 2
            scene 07_028 with Dissolve(1)
            m "Hey."
            mc "Everything alright? Did you call Haley?"
            m "I did."
            scene 07_029 with Dissolve(1)
            mc "How is she?"
            m "*Sigh* As good as she can be in her situation."
            m "Please give her a call later. She'd really appreciate that."
            mc "I will."
        "Stay here[KoGa3AutoWTChange1]{size=-4}(Brooke Points-4) {/size} {/color}":
            $ Brooke_Points -= 4
            scene 07_014 with Dissolve(1)
            br "Are you going to check up on her?"
            mc "I wouldn't know what to say."
            br "..."
            br "I'll go. Can you cover me for a minute?"
            mc "Yeah, sure."
            br "Thanks."
            scene black with Dissolve(1)
            pause 2
            scene 07_015 with Dissolve(1)
            mc "Is she alright?"
            br "She will be."
            mc "Thanks, Brooke."
            br "Anytime."
            scene black with Dissolve(1)
            pause 2
            scene 07_028 with Dissolve(1)
            mc "Are you alright, Mom?"
            m "Yes, don't worry. I'll be fine."
    scene 07_030 with Dissolve(1)
    mc "Want me to help out for the rest of the day?"
    m "It's fine. I think you could use some rest too. Shifts are covered anyway. Thank you, though."
    scene 07_031 with Dissolve(1)
    m "Here. You can take the car to drive home."
    mc "Uhm thanks. But how will you get home, then?"
    m "I'll take the bus later."
    menu:
        "Pick her up[KoGa3AutoWTChange1]{size=-4}(Emily Points+2) {/size} {/color}":
            $ Emily_Points += 2
            # Emily (14)
            scene 07_032 with Dissolve(1)
            mc "You don't have to take the bus. I'll come to pick you up. When are you finishing?"
            m "Hmm... Let's say nine-ish?"
            mc "Okay. If earlier or something comes up, let me know."
            m "Thanks [mc]."
            scene 07_033 with Dissolve(1)
            mc "Bye, Mom."
            m "Bye, honey."
            scene 07_034 with Dissolve(1)
            mc "See you next time, Brooke."
            br "Bye-bye."
        "Let her take the bus":
            scene 07_032 with Dissolve(1)
            mc "Okay... Thanks, Mom."
            mc "See you later."
            scene 07_034 with Dissolve(1)
            m "Bye, honey."
            mc "Later, Brooke."
            br "Bye-bye."
    jump Week2_Saturday_Phone

label Week2_Saturday_Restaurant2:
    scene black with Dissolve(2)
    stop music fadeout 1.0
    play music ("Sounds/Restaurant_Background.mp3", "Sounds/Restaurant_Background2.mp3", "Sounds/Restaurant_Background3.mp3") volume 0.2
    pause 2
    n "Saturday, 08:17. Rue Madison restaurant."
    scene 07_035 with Dissolve(1)
    br "Oh... Hey, [mc]. Good morning."
    mc "Good morning, Brooke."
    br "You're helping out today?"
    mc "Yeah. Until four or so."
    scene 07_036 with Dissolve(1)
    mc "Are you working the whole day?"
    br "No. Just like you, until four. Morning shift."
    br "Do you want a coffee?"
    mc "I could use one, yes."
    scene 07_037 with Dissolve(1)
    br "Black, was it?"
    mc "Yes, thanks."
    scene 07_038 with Dissolve(1)
    br "Here you go."
    mc "Thank you."
    br "Let's sit down. We still have a few minutes before we need to set up."
    mc "Sure."
    scene black with Dissolve(1)
    pause 2
    scene 07_039 with Dissolve(1)
    br "Is Emily here too?"
    mc "Yeah. She's in her office."
    br "Ah. She mostly comes here to drink her coffee first."
    mc "She had to make a call."
    scene 07_040 with Dissolve(1)
    mc "And there she is."
    br "Hmm?"
    m "And it got quiet all of a sudden. Talking about me?"
    scene 07_041 with Dissolve(1)
    br "Uh. Good morning, Emily."
    m "Good morning, Brooke."
    scene 07_042 with Dissolve(1)
    br "Do you want me to get you a coffee?"
    m "No, no, stay seated. I'll get it, thank you."
    scene 07_043 with Dissolve(1)
    m "It will be a very busy day. We're fully booked."
    m "I asked Jaylen and Monique to come earlier today. They'll be here at ten."
    scene 07_044 with Dissolve(1)
    br "Okay."
    mc "..."
    mc "{i}(Hmm...){/i}"
    scene black with Dissolve(1)
    pause 2
    scene 07_045 with Dissolve(1)
    mc "She wasn't kidding about being busy."
    br "Yeah, it's mostly like this during the weekend."
    mc "Happy our shifts are over."
    br "Hehe."
    scene 07_046 with Dissolve(1)
    mc "I'm going to change. Can't wait to get out of these clothes."
    br "I'll finish up, too."
    scene black with Dissolve(1)
    pause 2
    scene 07_047 with Dissolve(1)
    mc "{i}(Oh... She's already gone? Maybe changing too?){/i}"
    menu:
        "Wait for Brooke[KoGa3AutoWTChange1]{size=-4}(Brooke Week2 Saturday TurnDown, Brooke Points+2) {/size} {/color}":
            $ Brooke_Week2_Saturday_TurnDown = True
            $ Brooke_Points += 2
            # Brooke (4)
            mc "{i}(I guess I can wait for her.){/i}"
            br "Hey! Still here? Not waiting for me, are you?"
            scene black with Dissolve(1)
            transform moveup:
                xalign 0.5 yalign 1.0
                linear 5.0 yalign 0.0
            show 07_049 at moveup
            pause 3
            ""
            scene 07_050 with Dissolve(1)
            mc "Me? What? No... Yeah, maybe..."
            br "Haha."
            scene 07_051 with Dissolve(1)
            br "What's up?"
            mc "Do you have plans for tonight, or rather now?"
            br "Oh..."
            br "Yeah, sorry. I've made plans already."
            mc "Don't worry about it."
            scene 07_052 with Dissolve(1)
            mc "Well, see you somewhere next week, then."
            br "You're not coming tomorrow?"
            mc "Nope!"
            br "Haha okay."
            br "See you next week, then."
            mc "Yeah, bye, Brooke."
            br "Bye-bye."
            scene black with Dissolve(1)
            pause 2
            scene 07_053 with Dissolve(1)
            mc "Now, this is awkward..."
            br "Haha... Isn't it?"
            mc "Heading to the bus stop?"
            br "Yeah, you too?"
            mc "Uh-huh."
            scene 07_054 with Dissolve(1)
            mc "How long have you been working at the restaurant?"
            br "Hmm... A little over a year now."
            mc "And do you like it?"
            scene 07_055 with Dissolve(1)
            br "Haha."
            mc "What?"
            br "You're Emily's son."
            mc "Yeah, and?"
            br "I can't give you an honest answer."
            mc "Why? Because you don't really like it?"
            br "No. I love working there. Your mom is really great."
            scene 07_056 with Dissolve(1)
            mc "See, wasn't that hard..."
            mc "One down, six to go."
            br "HEY! I knew it! Don't tell her I said that."
            mc "Haha... I won't."
            scene 07_057 with vpunch
            n "*Bump*"
            scene 07_058 with Dissolve(1)
            mc "Watch where you're going, man..."
            br "..."
            mc "Are you alright?"
            br "Yeah."
            menu:
                "Watch[KoGa3AutoWTChange1]{size=-4}(Brooke Points-4) {/size} {/color}":
                    $ Brooke_Points -= 4
                    scene 07_059 with Dissolve(1)
                    mc "{i}(Not bad. I hope she won't have any plans next time I ask her out.){/i}"
                    jump Week2_Saturday_Gaming
                "Help her":
                    scene 07_060 with Dissolve(1)
                    mc "Your screen isn't broken, but it's scratched up real good."
                    br "What an asshole! He could've at least apologised."
                    mc "At the very least."
                    scene 07_061 with Dissolve(1)
                    br "Thank you."
                    mc "Sure."
                    jump Week2_Saturday_Gaming
        "Go home":
            mc "{i}(I guess I'll see her next time.){/i}"
            scene 07_048 with Dissolve(1)
            mc "Bye, guys."
            mo "Bye, [mc]."
            ja "Later, man."
            jump Week2_Saturday_Gaming

label Week2_Saturday_Phone:
    scene black with Dissolve(2)
    pause 2
    stop music fadeout 1.0
    play music ("Music/LoFi Indie 3.mp3", "Music/LoFi Indie 1.mp3", "Music/LoFi Indie 2.mp3") volume 0.2
    scene 07_062 with Dissolve(1)
    mc "*Sigh*"
    mc "{i}(I'm doing nothing for the rest of the day.){/i}"
    mc "{i}(Well... Maybe I should give Haley a call. Or maybe not, after all that's happened?){/i}"
    menu:
        "Don't call[KoGa3AutoWTChange1]{size=-4}({i}Nikki Girlfriend: Nikki GirlfriendFalse, Riverside Friends{/i}) {/size} {/color}":
            mc "{i}(I'd rather not.){/i}"
            if Nikki_Girlfriend == True:
                $ Nikki_Girlfriend = False
                $ Riverside_Friends = True
                jump Week2_Saturday_Gaming
            else:
                if Cara_Girlfriend == True:
                    $ Cara_Girlfriend = False
                    $ Riverside_Friends = True
                    $ Nikki_SP = False
                    jump Week2_Saturday_Gaming
                else:
                    jump Week2_Saturday_Gaming
        "Call her":
            mc "{i}(I guess I'll give her a call.){/i}"
            scene 07_063 with Dissolve(1)
            mc "{i}(Hmm. Doesn't seem to be picking up.){/i}"
            mc "..."
            if Nikki_FB_Choose == True:
                if Nikki_Girlfriend == True:
                    scene 07_064 with Dissolve(1)
                    ni "Hello?"
                    mc "..."
                    mc "Nikki?"
                    scene 07_065 with Dissolve(1)
                    ni "Yes."
                    mc "..."
                    ni "..."
                    scene 07_066 with Dissolve(1)
                    mc "How are..."
                    mc "{i}(What a stupid question...){/i}"
                    mc "Uhm... Is Haley there?"
                    ni "No."
                    mc "..."
                    mc "Hmm... I'll try again later."
                    scene 07_068 with Dissolve(1)
                    ni "Okay. I'll tell her you called."
                    mc "Thanks."
                    mc "Bye, Nikki."
                    ni "[mc]?"
                    mc "Yes?"
                    scene 07_069 with Dissolve(1)
                    ni "..."
                    ni "Never mind. Bye."
                    mc "..."
                    scene 07_070 with Dissolve(1)
                    mc "Nikki?"
                    mc "..."
                    mc "{i}(She hung up.){/i}"
                    scene 07_071 with Dissolve(1)
                    mc "*Sigh*"
                    mc "{i}(I guess that's it?){/i}"
                    mc "{i}(Sorry...){/i}"
                    jump Week2_Saturday_Gaming
                else:
                    if Nikki_Cheat == True:
                        scene 07_064 with Dissolve(1)
                        ni "Hello?"
                        mc "..."
                        mc "Nikki?"
                        scene 07_065 with Dissolve(1)
                        ni "Yes."
                        mc "..."
                        ni "..."
                        scene 07_066 with Dissolve(1)
                        mc "How are..."
                        mc "{i}(What a stupid question...){/i}"
                        mc "Uhm... Is Haley there?"
                        ni "No."
                        mc "..."
                        mc "Hmm... I'll try again later."
                        scene 07_067 with Dissolve(1)
                        ni "No. Don't call here again!"
                        mc "..."
                        scene 07_070 with Dissolve(1)
                        mc "Nikki?"
                        mc "..."
                        mc "{i}(She hung up. At least I tried...){/i}"
                        jump Week2_Saturday_Gaming
                    else:
                        scene 07_064 with Dissolve(1)
                        ni "Hello?"
                        mc "..."
                        mc "Nikki?"
                        scene 07_065 with Dissolve(1)
                        ni "Yes."
                        mc "..."
                        ni "..."
                        scene 07_066 with Dissolve(1)
                        mc "How are..."
                        mc "{i}(What a stupid question...){/i}"
                        mc "Uhm... Is Haley there?"
                        ni "No."
                        mc "..."
                        mc "Hmm... I'll try again later."
                        scene 07_068 with Dissolve(1)
                        ni "Okay. I'll tell her you called."
                        mc "Thanks."
                        mc "Bye, Nikki."
                        jump Week2_Saturday_Gaming
            else:
                if Cara_Girlfriend == True:
                    scene 07_064 with Dissolve(1)
                    c "Hello?"
                    mc "..."
                    mc "Cara?"
                    scene 07_065_01 with Dissolve(1)
                    c "Yes."
                    mc "..."
                    c "..."
                    scene 07_066 with Dissolve(1)
                    mc "How are..."
                    mc "{i}(What a stupid question...){/i}"
                    mc "Uhm... Is Haley there?"
                    c "No."
                    mc "..."
                    mc "Hmm... I'll try again later."
                    scene 07_068_01 with Dissolve(1)
                    c "Okay. I'll tell her you called."
                    mc "Thanks."
                    mc "Bye, Cara."
                    c "[mc]?"
                    mc "Yes?"
                    scene 07_069_01 with Dissolve(1)
                    c "..."
                    c "Never mind. Bye."
                    mc "..."
                    scene 07_070 with Dissolve(1)
                    mc "Cara?"
                    mc "..."
                    mc "{i}(She hung up.){/i}"
                    scene 07_071 with Dissolve(1)
                    mc "*Sigh*"
                    mc "{i}(I guess that's it?){/i}"
                    mc "{i}(Sorry...){/i}"
                    jump Week2_Saturday_Gaming
                else:
                    if Cara_Cheat == True:
                        scene 07_064 with Dissolve(1)
                        c "Hello?"
                        mc "..."
                        mc "Cara?"
                        scene 07_065_01 with Dissolve(1)
                        c "Yes."
                        mc "..."
                        c "..."
                        scene 07_066 with Dissolve(1)
                        mc "How are..."
                        mc "{i}(What a stupid question...){/i}"
                        mc "Uhm... Is Haley there?"
                        c "No."
                        mc "..."
                        mc "Hmm... I'll try again later."
                        scene 07_067_01 with Dissolve(1)
                        c "No. Don't call here again!"
                        mc "..."
                        scene 07_070 with Dissolve(1)
                        mc "Cara?"
                        mc "..."
                        mc "{i}(She hung up. At least I tried...){/i}"
                        jump Week2_Saturday_Gaming
                    else:
                        scene 07_064 with Dissolve(1)
                        c "Hello?"
                        mc "..."
                        mc "Cara?"
                        scene 07_065_01 with Dissolve(1)
                        c "Yes."
                        mc "..."
                        c "..."
                        scene 07_066 with Dissolve(1)
                        mc "How are..."
                        mc "{i}(What a stupid question...){/i}"
                        mc "Uhm... Is Haley there?"
                        c "No."
                        mc "..."
                        mc "Hmm... I'll try again later."
                        scene 07_068_01 with Dissolve(1)
                        c "Okay. I'll tell her you called."
                        mc "Thanks."
                        mc "Bye, Cara."
                        jump Week2_Saturday_Gaming

label Week2_Saturday_Gaming:
    scene black with Dissolve(2)
    pause 2
    scene 07_072 with Dissolve(1)
    mc "Yennefer or Triss... Why does this game have this stupid choice?"
    mc "Can't I have both? Like, come on... What stupid developer creates a game where you have to choose between different girls?"
    mc "That's just ridiculous! Ever heard of a harem?"
    menu:
        "Yennefer[KoGa3AutoWTChange1]{size=-4}(Team Yennefer) {/size} {/color}":
            $ Team_Yennefer = True
            mc "Team Yen all the way!"
            if Layla_Week2_Wednesday_Knows == True:
                jump Week3_Monday_School
            else:
                play sound "Sounds/Phone_Vibrate.mp3"
                n "*Bzzzt. Bzzzt*"
                scene 07_073 with Dissolve(1)
                mc "{i}(Oh, it's Layla. Probably for another Spanish lesson.){/i}"
        "Triss[KoGa3AutoWTChange1]{size=-4}(Team Triss) {/size} {/color}":
            $ Team_Triss = True
            mc "Team Triss all the way!"
            if Layla_Week2_Wednesday_Knows == True:
                jump Week3_Monday_School
            else:
                play sound "Sounds/Phone_Vibrate.mp3"
                n "*Bzzzt. Bzzzt*"
                scene 07_073a with Dissolve(1)
                mc "{i}(Oh, it's Layla. Probably for another Spanish lesson.){/i}"
    menu:
        "Answer in English":
            scene 07_074 with Dissolve(1)
            mc "Hey Layla, how are you?"
            la "Hey. I'm good, but..."
            mc "But?"
        "Answer in Spanish":
            scene 07_074 with Dissolve(1)
            mc "Hola, cómo estás?"
            la "No..."
            mc "Haha."
            mc "How are you?"
            la "I'm good, but..."
            mc "But?"
    scene 07_075 with Dissolve(1)
    la "Bored..."
    mc "How can you be bored? It's the weekend."
    mc "No plans with Elena?"
    scene 07_076 with Dissolve(1)
    la "Her mother has the weekend shift, so she has to take care of her brothers."
    mc "Sienna?"
    la "Date with her boyfriend."
    mc "{i}(Oh, didn't know she has a boyfriend.){/i}"
    mc "Tori?"
    scene 07_077 with Dissolve(1)
    la "Hey! I'm not that bored."
    mc "Haha."
    la "What are you doing?"
    scene 07_078 with Dissolve(1)
    mc "Playing a video game."
    la "Hmm... What's it about?"
    mc "A monster slayer in a fantasy world, searching for his adopted daughter."
    la "What's happened so far?"
    mc "You really want to know?"
    la "Yes."
    mc "{i}(Wow, she must be bored.){/i}"
    scene 07_079 with Dissolve(1)
    mc "Well... Uhm... You're on the road to White Orchard."
    mc "Looking for a woman, raven hair, violet eyes, smells of lilac and gooseberries, dresses in black and white."
    scene black with Dissolve(1)
    pause 2
    scene 07_080 with Dissolve(1)
    la "It's a game about choices and they impact the game further?"
    mc "Exactly. Someone's been paying attention."
    la "Hehe."
    scene 07_081 with Dissolve(1)
    mc "What about Spanish? Do you still remember that?"
    if Layla_Week2_Wednesday_Chichis == True:
        la "The important parts. Like chichis..."
        mc "Haha. Well... That's a start."
        la "Haha."
        #Maybe a joke about Gabi's chichis when Layla called her cute? (This is for the remake for the people who snoop in the code!)
    else:
        la "Some of it."
    scene 07_082 with Dissolve(1)
    la "Do you have time tomorrow to give me a refresher?"
    mc "Sure, no problem."
    la "Let's say around four in the afternoon?"
    mc "Sounds good."
    scene 07_083 with Dissolve(1)
    if Alexis_Friends == True:
        la "I'll text you the address."
        mc "Okay, thanks."
    else:
        la "I'll text you the address."
        mc "Don't worry, I know where it is."
        la "You do?"
        scene 07_084 with Dissolve(1)
        mc "{i}(Oh shit...){/i}"
        mc "Heh..."
        scene 07_085 with Dissolve(1)
        mc "Uh... Yeah, just text me."
        la "Hehe okay. Will do."
        mc "{i}(I really need to tell her soon. I almost messed up...){/i}"
    scene 07_086 with Dissolve(1)
    la "Well. Thanks for the story. I'll see you tomorrow, then?"
    mc "Yeah. See you tomorrow. Bye, Layla."
    la "Bye, [mc]."
    if Layla_Points >= 34:
        scene 07_087 with Dissolve(1)
        la "..."
        if Alexis_Friends == True:
            jump Week2_Sunday_LaylaHome
        else:
            scene 07_088 with Dissolve(1)
            a "Hey!"
            la "Lexi! You scared me..."
            scene 07_089 with Dissolve(1)
            la "What's up?"
            a "Nothing. I'm bored."
            la "It's the weekend."
            a "*Sigh* I know..."
            scene 07_090 with Dissolve(1)
            la "Want to hear a story?"
            a "Uh... Sure."
            la "So, it's about this monster slayer..."
            scene 07_091 with Dissolve(1)
            a "Monster slayer?"
            la "Yeah."
            a "What kind of story is this?"
            la "A love story."
            a "Really?"
            scene black with Dissolve(1)
            pause 2
            scene 07_092 with Dissolve(1)
            a "So, who did he choose? Yennefer or Triss?"
            la "Hmm... I don't know actually."
            a "..."
            jump Week2_Sunday_LaylaHome
    else:
        jump Week2_Sunday_LaylaHome

label Week2_Sunday_LaylaHome:
    scene black with Dissolve(2)
    pause 2
    stop music fadeout 1.0
    play music ("Music/LoFi Upbeat 1.mp3", "Music/LoFi Upbeat 2.mp3", "Music/LoFi Upbeat 3.mp3", "Music/LoFi Upbeat 4.mp3") volume 0.2
    n "Sunday, 15:48. Layla's home."
    scene 07_093 with Dissolve(1)
    if Alexis_Friends == True:
        mc "..."
    else:
        mc "{i}(*Sigh* Will Alexis be here?){/i}"
        mc "{i}(Why am I hoping she is, but at the same time...?){/i}"
    scene 07_094 with Dissolve(1)
    la "Hey."
    mc "Hi."
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 07_095 at moveup
    pause 3
    if Layla_Points >= 34:
        la "Come on in."
        scene 07_096 with Dissolve(1)
        la "Thank you for coming."
        mc "Of course."
    else:
        la "Thanks for coming."
    scene 07_097 with Dissolve(1)
    la "I've set it up in the backyard. You don't mind, right?"
    mc "Not at all. It's nice outside."
    la "Cool. Follow me."
    scene 07_098 with Dissolve(1)
    mc "Someone's eager to study."
    la "Haha... Not really, but the earlier we start, the earlier we finish."
    la "Do you want a house tour first maybe?"
    if Alexis_Friends == True:
        mc "It's fine, thanks."
    else:
        mc "It's fine, thanks."
        mc "{i}(I've seen it already...){/i}"
    scene black with Dissolve(1)
    pause 2
    scene 07_099 with Dissolve(1)
    mc "Oh... A jacuzzi."
    la "Hehe, yeah."
    scene 07_100 with Dissolve(1)
    mc "Well, I'll never invite you to my place, now."
    la "What? Why not?"
    mc "For starters. We don't have a jacuzzi..."
    la "Haha... Doesn't matter. I don't use it that often."
    scene 07_101 with Dissolve(1)
    mc "Really? If I had one, I'd be in there every day."
    la "I thought so too at first, but after a few times..."
    mc "Hmm..."
    scene black with Dissolve(1)
    pause 2
    scene 07_102 with Dissolve(1)
    if Layla_Points >= 34:
        la "Next time you come, bring your bathing suit. We'll have a little hot-tub party."
        mc "I won't say no to that."
        scene 07_103 with Dissolve(1)
        la "Or do you want to go in now?"
        mc "Uh..."
        scene 07_104 with Dissolve(1)
        mc "Yes."
        la "Haha. Yes?"
        mc "Sure..."
        scene 07_105 with Dissolve(1)
        la "Next time..."
        mc "So mean. You're such a tease, you know that?"
        scene 07_106 with Dissolve(1)
        mc "..."
        scene 07_107 with Dissolve(1)
        la "Next time!"
    else:
        la "Next time you come, bring your bathing suit."
        la "I'll also invite Elena, maybe bring Zach and we can have a little hot-tub party."
        mc "Yeah, will be fun."
    scene 07_108 with Dissolve(1)
    mc "Is anyone else here?"
    if Alexis_Friends == True:
        la "No, we're alone for now."
    else:
        la "No, we're alone for now."
        mc "{i}(Maybe for the best...){/i}"
    scene 07_109 with Dissolve(1)
    la "Okay. Let's get this over with."
    la "I just need to not fail this test and I'll be good."
    mc "Don't worry. You've got this."
    scene black with Dissolve(1)
    pause 2
    scene 07_110 with Dissolve(1)
    ""
    scene 07_111 with Dissolve(1)
    ""
    scene black with Dissolve(1)
    pause 2
    scene 07_112 with Dissolve(1)
    la "Let's take a short break."
    mc "You've done well so far. You remembered a lot from last time."
    la "Thanks."
    mc "Just two more chapters, and those aren't that bad. We should be done in no time."
    la "Do you know what time it is?"
    scene 07_113 with Dissolve(1)
    mc "Hmm, let me check."
    mc "Quarter past five."
    scene 07_114 with Dissolve(1)
    la "Oh shit! Already?"
    la "{i}(Why didn't I just tell him at the beginning...){/i}"
    mc "Something wrong?"
    la "Uhm..."
    la "..."
    la "I think I need to tell you something..."
    scene 07_115 with Dissolve(1)
    la "It's about the principal."
    mc "Oh? Did something happen since last time?"
    la "No... It's..."
    am "That's a sight I like to see!"
    scene 07_116 with Dissolve(1)
    mc "..."
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 07_117 at moveup
    pause 3
    la "Mom!"
    mc "{i}(Mom? What?){/i}"
    mc "Hi, Principal Moore."
    am "Hey, [mc]."
    am "And it's Adriana here."
    scene 07_118 with Dissolve(1)
    am "You've been studying?"
    la "Yes. [mc] is helping me out."
    am "I see. Thank you very much."
    scene 07_119 with Dissolve(1)
    am "Hmm..."
    la "What?"
    am "[mc] is your guest, helping you study, and you didn't even offer him something to drink?"
    la "Sorry, I forgot."
    am "*Sigh* Layla..."
    scene 07_120 with Dissolve(1)
    la "Sorry."
    mc "It's fine, don't worry."
    scene 07_121 with Dissolve(1)
    am "Would you like something to drink, [mc]? Water, soda, coffee maybe?"
    mc "I'd take a coffee if it isn't too much of a hassle."
    am "Of course not. I was going to make one myself."
    scene 07_122 with Dissolve(1)
    am "Milk, sugar?"
    if Alexis_Friends == True:
        mc "Black, please."
    else:
        mc "Black, please."
        am "Oh? Alexis would like you."
        la "..."
        mc "{i}(That's right. She's also Alexis's mom. See, I knew they looked alike.){/i}"
        mc "{i}(What a gorgeous family.){/i}"
    scene 07_123 with Dissolve(1)
    am "Do you want a coffee, Layla?"
    la "Cappuccino, please."
    if Alexis_Friends == True:
        am "Okay."
    else:
        scene 07_124 with Dissolve(1)
        am "LEXI, do you want a coffee?"
        mc "{i}(Oh... I thought she wasn't here?){/i}"
        la "She isn't here."
        mc "{i}(My heart started pounding like crazy for a second...){/i}"
        scene 07_125 with Dissolve(1)
        am "No? Do you know where she is?"
        la "I don't. She left early afternoon."
        am "Hmm okay."
        am "I'll get the coffees."
    scene black with Dissolve(1)
    pause 2
    scene 07_126 with Dissolve(1)
    mc "So... The principal is your mom."
    la "Yes."
    mc "Why didn't you tell me?"
    scene 07_127 with Dissolve(1)
    la "*Sigh* Why do you think I only have a few friends?"
    la "A few years ago, no one knew except Elena."
    la "But once they found out they stopped hanging out with me."
    la "Saying that I have an advantage with the exams, or they were asking for favours."
    la "I can't change their grades or get them out of detention..."
    mc "..."
    scene 07_128 with Dissolve(1)
    mc "I'm not going to end our friendship based on the fact that the principal is your mother."
    mc "And the people who did weren't your friends to begin with and are missing out."
    menu:
        "Cool[KoGa3AutoWTChange1]{size=-4}(Layla Points+2) {/size} {/color}":
            $ Layla_Points += 2
            # Layla (48)
            scene 07_130 with Dissolve(1)
            mc "Come here."
            mc "I think you're pretty cool."
            la "Heh... Thanks."
            mc "Your mom is cool, too!"
            la "Haha. Sometimes."
            scene 07_131 with Dissolve(1)
            mc "Tori is..."
            la "NO!"
            mc "Haha."
        "Angry[KoGa3AutoWTChange1]{size=-4}({i}Layla Points > 35: Adriana Week2 Sunday Dinner{/i}) {/size} {/color}":
            scene 07_129 with Dissolve(1)
            mc "But honestly. I didn't like that you didn't tell me earlier and put me in the same category as those other idiots."
            if Alexis_Friends == True:
                la "Yeah, you're right. I'm sorry."
            else:
                la "Yeah, you're right. I'm sorry."
                mc "{i}(I'm such a hypocrite... I shouldn't be mad at her at all. I'm the one who's hiding stuff from her. Alexis...){/i}"
    scene black with Dissolve(1)
    pause 2
    scene 07_132 with Dissolve(1)
    am "Here you go."
    mc "Thank you very much, Prin... Adriana."
    am "You're welcome."
    scene 07_133 with Dissolve(1)
    la "What are you doing?"
    am "Hmm? Drinking my coffee and enjoying the sun."
    la "Here?"
    am "Yes, why not?"
    scene 07_134 with Dissolve(1)
    la "We're studying here!"
    am "Don't mind me. Keep on studying."
    la "..."
    scene 07_135 with Dissolve(1)
    am "What are you studying?"
    la "Spanish. We have a test tomorrow."
    am "Español divertido!\n(Spanish, fun!)"
    la "..."
    scene 07_136 with Dissolve(1)
    am "That reminds me. How did you do on the geography test?"
    la "Uh... We didn't get it back yet."
    if Adriana_Week2_Monday_TestBack == False:
        am "Hmm, okay. I thought Mr Coleman was faster in scoring tests."
    else:
        am "Really? How come [mc] got it back but you didn't?"
        scene 07_137 with Dissolve(1)
        la "Did you tell her?"
        mc "Uh... No, I..."
        am "Hey! Don't blame him. I asked him about it at school."
        scene 07_138 with Dissolve(1)
        la "Sorry... I'm not blaming him. Sorry, [mc]."
        la "..."
        am "So, what did you get?"
        la "D!"
        am "What? D? Didn't you study?"
        la "..."
        scene 07_139 with Dissolve(1)
        if Alexis_Friends == True:
            am "We're going to talk about this another day!"
            la "..."
            am "And all of next week, you can do the chores!"
            la "*Sigh* Yes..."
        else:
            am "We're going to talk about this another day!"
            la "..."
            am "And all of next week, you can help out Alexis with the chores!"
            la "..."
            am "Make that two! One for the bad grade, the other for lying!"
            la "*Sigh* Yes..."
    scene black with Dissolve(1)
    pause 2
    scene 07_140 with Dissolve(1)
    if Adriana_Points >= 2:
        if Alexis_Friends == False:
            $ Adriana_Week2_Sunday_Dinner = True
            am "I'm heading to the supermarket now."
            am "Are you staying for dinner, [mc]?"
            mc "Uh... I wasn't planning to."
            am "I'll take that as a yes!"
            am "Do you need anything, Layla?"
        else:
            if Layla_Points >= 35:
                $ Adriana_Week2_Sunday_Dinner = True
                am "I'm heading to the supermarket now."
                am "Are you staying for dinner, [mc]?"
                mc "Uh... I wasn't planning to."
                am "I'll take that as a yes!"
                am "Do you need anything, Layla?"
            else:
                am "I'm heading to the supermarket now."
                am "Do you need anything, Layla?"
    else:
        am "I'm heading to the supermarket now."
        am "Do you need anything, Layla?"
    scene 07_141 with Dissolve(1)
    la "Hmm... Not really?"
    am "Those sports drinks or something?"
    la "Oh yeah, you can get a few of those. But only the red ones. Thanks."
    am "Okay. See you later."
    scene 07_108 with Dissolve(1)
    mc "Let's finish those last two chapters."
    la "Yes."
    scene black with Dissolve(1)
    pause 2
    scene 07_142 with Dissolve(1)
    mc "Pfew... Teaching is exhausting. And I only had one student."
    la "Haha. A good student, might I add."
    scene 07_143 with Dissolve(1)
    mc "You'd better not fail that test, or I'll be mad."
    la "I'll do my best."
    la "Or I'll write your name on my paper and mine on yours."
    la "That way I'll ace it for sure."
    mc "And you called me a cheater before?"
    la "Haha..."
    if Layla_Points >= 35:
        scene 07_144 with Dissolve(1)
        la "Thank you for helping me out."
        mc "Anytime."
        scene 07_145 with Dissolve(1)
        mc "Uh... Layla?"
        mc "What are you doing?"
        scene 07_146 with Dissolve(1)
        la "Your payment, remember?"
        menu:
            "Push her off":
                scene 07_147 with Dissolve(1)
                mc "We shouldn't. What if your mom sees us?"
                if Alexis_End == True:
                    la "..."
                    n "*Bzzzt. Bzzzt*"
                else:
                    mc "{i}(And what if Alexis shows up now...){/i}"
                    la "..."
                    n "*Bzzzt. Bzzzt*"
            "Kiss her[KoGa3AutoWTChange1]{size=-4}(Layla Points+2) {/size} {/color}":
                $ Layla_Points += 2
                # Layla (50)
                scene 07_148 with Dissolve(1)
                ""
                scene 07_149 with Dissolve(1)
                mc "{i}(She has such soft lips...){/i}"
                scene 07_150 with Dissolve(1)
                la "Ah..."
                mc "{i}(And an amazing ass.){/i}"
                n "*Bzzzt. Bzzzt*"
                la "{i}(Not now...){/i}"
                scene 07_151 with Dissolve(1)
                n "*Bzzzt. Bzzzt*"
                mc "Do you need to pick that up?"
                la "No..."
                scene 07_152 with Dissolve(1)
                n "*Bzzzt. Bzzzt*"
                la "{i}(Just stop calling me!){/i}"
                scene 07_153 with Dissolve(1)
                n "*Bzzzt. Bzzzt*"
                la "{i}(STOP!){/i}"
                scene 07_154 with Dissolve(1)
                n "*Bzzzt. Bzzzt*"
                la "Sorry... One second."
                mc "It's fine... Maybe it's important."
    else:
        n "*Bzzzt. Bzzzt*"
        la "{i}(What now...){/i}"
    scene 07_155 with Dissolve(1)
    la "What?"
    la "..."
    scene 07_156 with Dissolve(1)
    la "Sorry, Mom."
    am "I forgot to pull the meat out of the freezer. Can you get it out so it can defrost a little?"
    la "Yes, will do."
    am "And can you peel some potatoes?"
    la "Uh..."
    am "Thanks. Okay. See you later."
    la "Bye."
    la "..."
    if Adriana_Week2_Sunday_Dinner == True:
        scene 07_157 with Dissolve(1)
        la "I guess I have to peel some potatoes."
        menu:
            "Offer help[KoGa3AutoWTChange1]{size=-4}(Layla Points+2) {/size} {/color}":
                $ Layla_Points += 2
                # Layla (52)
                mc "Do you need some help?"
                la "It's fine. You helped me plenty today. You can watch some TV in the meantime. Won't take too long."
                mc "Sure."
            "Don't offer help":
                pass
        jump Week2_Sunday_Layla_TV
    else:
        $ Alexis_Friends = True
        $ Alexis_Week2_Wednesday_Breakup = True
        scene 07_157 with Dissolve(1)
        la "I guess I have to peel some potatoes."
        menu:
            "Offer help[KoGa3AutoWTChange1]{size=-4}(Layla Points+2) {/size} {/color}":
                $ Layla_Points += 2
                # Layla (52)
                mc "Do you need some help?"
                la "It's fine. You helped me plenty today."
                mc "Sure."
                mc "I guess I'll be leaving then."
                scene 07_157a with Dissolve(1)
                la "Thank you for helping me out. I promise I won't fail the test!"
                mc "Anytime, Layla."
            "Don't offer help":
                mc "I guess I'll be leaving then."
                scene 07_157a with Dissolve(1)
                la "Thank you for helping me out. I promise I won't fail the test!"
                mc "Anytime, Layla."
        jump Week3_Monday_School

label Week2_Sunday_Layla_TV:
    scene black with Dissolve(1)
    pause 2
    scene 07_158 with Dissolve(1)
    la "Make yourself comfortable. If you need anything, just shout."
    mc "Will do."
    if Layla_Points >= 37:
        scene 07_159 with Dissolve(1)
        mc "Off you go, Chef Layla."
        la "Aah... Hey!"
        scene 07_160 with Dissolve(1)
        la "I'll get you back for that! You'd better chew very carefully later..."
        mc "Haha... What if your mom accidentally gets that piece?"
        la "Collateral damage!"
        mc "You can be really scary, you know that?"
        scene 07_161 with Dissolve(1)
        la "I know."
        la "Be right back."
    else:
        la "I'll be right back."
    scene black with Dissolve(1)
    pause 2
    scene 07_162 with Dissolve(1)
    mc "{i}(Even the TV is huge...){/i}"
    mc "{i}(We're pretty well off, but compared to them...){/i}"
    scene 07_163 with Dissolve(1)
    a "Hey, why did you start watching without me?"
    mc "..."
    scene 07_164 with Dissolve(1)
    a "Did I miss anything?"
    mc "..."
    scene 07_165 with Dissolve(1)
    a "Oh..."
    mc "Hi."
    scene 07_166 with Dissolve(1)
    a "Uh... I'm so sorry. I wasn't even paying attention to who was actually sitting here. And I..."
    mc "It's fine."
    a "Why are..."
    scene 07_167 with Dissolve(1)
    la "What are you doing, Lexi?"
    a "Oh, there you are."
    a "Sorry. I thought you were watching the new episode already and I just jumped on the sofa."
    la "..."
    scene 07_168 with Dissolve(1)
    la "Yeah, [mc] and I totally look alike..."
    a "Haha... I was looking at the screen."
    if Alexis_Friends == False:
        scene 07_169 with Dissolve(1)
        la "..."
        a "What?"
        la "Can you get off him now?"
        scene 07_170 with Dissolve(1)
        a "Oh, sorry! Yes."
        a "Sorry, [mc]."
    else:
        pass
    scene black with Dissolve(1)
    pause 2
    scene 07_171 with Dissolve(1)
    la "Do you watch Entanglement?"
    mc "I've heard of it, but never watched it."
    la "It's really good. Full of intrigue and drama. And somehow all the characters are connected to each other."
    if Layla_Points >= 37:
        mc "Sounds interesting."
        scene 07_172 with Dissolve(1)
        la "Oh yeah. And lots of sex..."
        a "..."
        mc "Uh, okay?"
        scene 07_173 with Dissolve(1)
        n "*Sex noises*"
        if Alexis_Friends == False:
            scene 07_174 with Dissolve(1)
            a "..."
            mc "..."
        else:
            pass
        scene 07_175 with Dissolve(1)
        la "That's Lexi's favourite there."
        a "Layla stop!"
        la "She has the hots for him. Totally her type."
        a "LAYLA!"
        scene 07_176 with Dissolve(1)
        la "Hey, where are you going? Not going to watch it?"
        a "Not when you're making stupid comments..."
        la "I'm kidding. Lex... I'm sorry."
    else:
        mc "Sounds interesting."
        la "Oh yeah. And lots of sex..."
        a "..."
        mc "Uh, okay?"
        scene 07_173a with Dissolve(1)
        n "*Sex noises*"
        if Alexis_Friends == False:
            scene 07_174 with Dissolve(1)
            a "..."
            mc "..."
        else:
            pass
        scene black with Dissolve(1)
        pause 2
        scene 07_175a with Dissolve(1)
        la "That's Lexi's favourite there."
        a "Layla stop!"
        la "She has the hots for him. Totally her type."
        a "LAYLA!"
        scene 07_176a with Dissolve(1)
        la "Hey, where are you going? Not going to watch it?"
        a "Not when you're making stupid comments..."
        la "I'm kidding. Lex... I'm sorry."
    scene 07_177 with Dissolve(1)
    mc "Is she alright?"
    la "I hope so... I shouldn't have said that."
    if Alexis_Sex == True:
        la "*Sigh* Remember I told you that she might be seeing someone and it probably ended badly?"
        mc "Yeah, I remember."
        la "I think it's still a sore subject."
        mc "Hmm..."
    else:
        pass
    la "I'll apologise later."
    scene 07_178 with Dissolve(1)
    la "Anyway, I'm going to get us something to drink. Soda okay?"
    mc "Yes, thank you. I'll go visit the restroom in the meantime."
    la "You can use the one upstairs. First door to the left."
    scene black with Dissolve(1)
    pause 2
    scene 07_179 with Dissolve(1)
    if Alexis_Friends == True:
        jump Week2_Sunday_Layla_TV2
    else:
        mc "{i}(Should I go talk to Alexis?){/i}"
        menu:
            "Go to Alexis's room":
                jump Week2_Sunday_Alexis_Room
            "Go to bathroom[KoGa3AutoWTChange1]{size=-4}(Alexis Friends, Alexis Week2 Wednesday Breakup) {/size} {/color}":
                $ Alexis_Friends = True
                $ Alexis_Week2_Wednesday_Breakup = True
                jump Week2_Sunday_Layla_TV2

label Week2_Sunday_Alexis_Room:
    scene black with Dissolve(1)
    pause 2
    scene 07_203 with Dissolve(1)
    mc "Hey. Are you okay?"
    a "He's not my type, you know!"
    mc "I know."
    scene 07_204 with Dissolve(1)
    a "And why do you keep showing up everywhere I am?"
    a "I'm trying to get over you, but you aren't making it easy on me."
    menu:
        "Leave[KoGa3AutoWTChange1]{size=-4}(Alexis Friends, Alexis Week2 Wednesday Breakup) {/size} {/color}":
            $ Alexis_Friends = True
            $ Alexis_Week2_Wednesday_Breakup = True
            scene 07_205 with Dissolve(1)
            mc "Yeah, you're right. I'm sorry... I'll try to stay away."
            scene 07_206 with Dissolve(1)
            a "[mc], I..."
            a "*Sigh*"
            jump Week2_Sunday_Layla_TV2
        "Hug her[KoGa3AutoWTChange1]{size=-4}(Alexis Points+2) {/size} {/color}":
            $ Alexis_Points += 2
            # Alexis (32)
            scene 07_207 with Dissolve(1)
            mc "Maybe I don't want you to get over me?"
            a "..."
            scene 07_208 with Dissolve(1)
            a "[mc], I... We..."
            scene 07_209 with Dissolve(1)
            a "..."
            scene 07_210 with Dissolve(1)
            ""
            scene 07_211 with Dissolve(1)
            a "Ah..."
            scene 07_212 with vpunch
            a "Stop!"
            mc "Lexi?"
            a "What about Layla?"
            if Layla_Points >= 37:
                menu:
                    "Honest[KoGa3AutoWTChange1]{size=-4}(Alexis Week2 Sunday Honest, Alexis Points-2) {/size} {/color}":
                        $ Alexis_Week2_Sunday_Honest = True
                        $ Alexis_Points -= 2
                        scene 07_213a with Dissolve(1)
                        if Tori_Week1_Interested == True:
                            mc "Honestly, Lexi. I don't know. We're really good friends, and yes, we flirt sometimes."
                        else:
                            mc "Honestly, Lexi. I don't know. We're really good friends, and yes, we flirt sometimes. We did kiss too."
                        a "..."
                        mc "I don't know if there will be more between us, but the thing I know is that I like you and want to be with you."
                        a "..."
                        mc "I'll talk to her and tell her about us."
                    "Nothing's going on":
                        scene 07_213 with Dissolve(1)
                        mc "Nothing is going on between Layla and me."
                        a "But she likes you."
                        mc "I like her too, as a friend."
                        a "..."
                        mc "I'll talk to her and tell her about us."
                        a "I think she'll be sad though. And angry..."
                        mc "Don't worry. It'll be fine."
                        mc "Nothing will change between Layla and me. I'll still be her friend and hang out with her or help her if she needs it."
                        a "Thank you."
            else:
                scene 07_213 with Dissolve(1)
                mc "Layla and I are just friends. Yes, we flirt sometimes, but that's about it."
                a "But..."
                mc "I'll talk to her and tell her about us. So don't worry. It'll be fine."
                a "I think she'll be angry though."
                mc "Why? Nothing will change between Layla and me. I'll still be her friend and hang out with her or help her if she needs it."
                a "Thank you."
            scene 07_214 with Dissolve(1)
            a "And Erynn?"
            mc "This has nothing to do with Erynn."
            a "Did you talk to her?"
            if Erynn_Week2_Thursday_Confront == True:
                $ Alexis_Points += 2
                # Alexis (34)
                mc "We did talk about some stuff, but that doesn't change how I feel about you."
            else:
                $ Alexis_Points -= 2
                mc "She was too busy with Ethan. Besides. It doesn't matter what she has to say. It doesn't change the way I feel about you."
                a "..."
            scene 07_215 with Dissolve(1)
            mc "Hey. Come here. It's going to be alright, you know."
            mc "I like you!"
            a "..."
            scene 07_216 with Dissolve(1)
            a "Can you say that again?"
            mc "I like you, Alexis!"
            a "I like you too."
            mc "Want to give this a shot?"
            a "Yes..."
            scene 07_217 with Dissolve(1)
            a "But I still think we shouldn't meet up. At least until Layla knows. I don't want the Erynn scenario repeating."
            mc "I agree. Once the tests are done, I'll talk to her."
            a "Thank you."
            scene 07_218 with Dissolve(1)
            ""
            scene 07_219 with Dissolve(1)
            mc "And come back down. I can't have you miss those sexy scenes with your favourite character."
            a "He's not my favourite!"
            mc "I know..."
            scene 07_219a with Dissolve(1)
            a "{i}(I'm not doing anything wrong this time, right?){/i}"
            jump Week2_Sunday_Layla_TV2

label Week2_Sunday_Layla_TV2:
    scene black with Dissolve(1)
    pause 2
    scene 07_180 with Dissolve(1)
    la "So... What do you think of Entanglement?"
    mc "As you said. Lots of sex scenes."
    la "Haha, right?"
    la "What were you doing upstairs before?"
    if Alexis_Friends == True:
        scene 07_221 with Dissolve(1)
        mc "I had to poop."
        la "Ew... TMI!"
        mc "Haha. You asked."
        scene 07_181 with Dissolve(1)
        la "We can watch something else if you want?"
        mc "No, I don't mind."
        scene 07_182 with Dissolve(1)
        la "Let me sit a bit closer to you."
        mc "Uh, sure..."
        scene 07_183 with Dissolve(1)
        n "*Sex noises*"
        scene black with Dissolve(1)
        pause 2
        if Layla_Points >= 37:
            $ Layla_Week2_Sunday_TV_Makeout = True
            scene 07_184 with Dissolve(1)
            la "And that's my favourite character. Mariposa."
            la "She's so gorgeous."
            if Layla_Week1_Saturday_Beach == False:
                scene 07_185 with Dissolve(1)
                la "Do you have a favourite already?"
            else:
                la "She's also the woman on your beach towel."
                scene 07_185 with Dissolve(1)
                mc "Oh, really?"
                la "Mm-hmm."
                la "Do you have a favourite already?"
            menu:
                "Layla[KoGa3AutoWTChange1]{size=-4}(Layla Points+2) {/size} {/color}":
                    $ Layla_Points += 2
                    # Layla (54)
                    mc "I do."
                    la "Yeah? Who?"
                    scene 07_186 with Dissolve(1)
                    mc "Her name is Layla."
                    la "..."
                "No":
                    mc "No, not yet. Haven't seen enough yet to pick a favourite."
                    la "Gotcha."
                "Same as you":
                    if Layla_Week1_Saturday_Beach == False:
                        mc "Same as you. Mariposa. She seems fun."
                        la "Yeah, she is."
                    else:
                        mc "Now I have to pick Mariposa. I have a beach towel of her!"
                        la "Haha, yeah!"
                    scene 07_187 with Dissolve(1)
                    la "She's also very forward."
                    mc "Is she?"
            scene 07_188 with Dissolve(1)
            ""
            scene 07_189 with Dissolve(1)
            ""
            scene 07_190 with Dissolve(1)
            mc "{i}(Should we go to her room?){/i}"
            am "Uh-hum..."
            scene 07_191 with vpunch
            la "MOM!"
            mc "{i}(Oh shit!){/i}"
            scene 07_192 with Dissolve(1)
            am "Enjoying yourselves?"
            la "Mom, stop! This is so embarrassing."
            scene 07_193 with Dissolve(1)
            am "Dinner will be ready in half an hour."
            la "..."
            la "Okay."
            scene 07_194 with Dissolve(1)
            la "Haha... That was so embarrassing."
            mc "And scary. Haha."
        else:
            pass
        jump Week2_Sunday_Adriana_Dinner
    else:
        scene 07_221a with Dissolve(1)
        mc "Talked to Alexis."
        la "Oh... What about?"
        mc "Her favourite character."
        la "Haha, really?"
        mc "I asked her to come back down."
        la "Thank you."
        scene black with Dissolve(1)
        pause 2
        scene 07_223 with Dissolve(1)
        la "Hey, you're back. Sorry about before, Lexi."
        a "It's okay."
        la "Come sit with me so I can give you an apology cuddle."
        a "Apology cuddle? Is that a thing?"
        la "It will be."
        scene 07_224 with Dissolve(1)
        ""
        scene 07_225 with Dissolve(1)
        a "..."
        mc "..."
        scene black with Dissolve(2)
        pause 2
        scene 07_226 with Dissolve(1)
        am "Would you look at that."
        la "Hey, Mom."
        scene 07_227 with Dissolve(1)
        am "Don't let them fool you, [mc]. They aren't that nice most of the time."
        mc "Haha, okay."
        a "We're always nice!"
        la "Uh-huh..."
        scene 07_228 with Dissolve(1)
        la "See..."
        a "Haha, Layla, stop."
        scene 07_229 with Dissolve(1)
        am "Yeah, yeah."
        am "I'm starting to cook dinner. Will be ready in half an hour."
        la "Okay."
        jump Week2_Sunday_Adriana_Dinner

label Week2_Sunday_Adriana_Dinner:
    scene black with Dissolve(1)
    pause 2
    scene 07_235 with Dissolve(1)
    am "Hey."
    x "Hey, gorgeous. Smells good."
    am "Are you done for today?"
    x "No. I still have lots of paperwork."
    scene 07_236 with Dissolve(1)
    am "So, you won't be eating now?"
    x "Once I'm done."
    am "Okay. I'll put a plate aside."
    x "Thank you."
    scene 07_237 with Dissolve(1)
    x "By the way. Who's the boy?"
    am "He's a new student at my school. Tutored Layla for tomorrow's Spanish test."
    x "Is he her boyfriend?"
    if Layla_Week2_Sunday_TV_Makeout == False:
        am "I don't know. They seem pretty close."
    else:
        am "I don't know. I caught them making out on the couch."
        x "What?"
    scene black with Dissolve(1)
    pause 2
    scene 07_238a with Dissolve(1)
    am "Food is almost ready. Layla, please set the table."
    la "Coming."
    if Alexis_Friends == True:
        scene black with Dissolve(1)
        pause 2
        scene 07_239 with Dissolve(1)
        am "Alexis, food is ready."
        a "I'm not hungry."
        am "..."
        scene 07_240 with Dissolve(1)
        am "If there's anything you don't eat, just put it aside."
        mc "Don't worry. My mom is a chef and owns a restaurant. She taught me to eat everything."
        mc "She would literally smack me if I left food on my plate."
        am "Oh? Which restaurant? In the city?"
        mc "Yeah. Rue Madison."
        scene 07_241 with Dissolve(1)
        am "..."
        am "You're Emily's son! I've no idea why I didn't make the connection when I called her on Monday."
        scene 07_242 with Dissolve(1)
        la "You know his mom?"
        am "Yeah. We shared a dorm at MSU for a while."
        la "What? Really?"
        scene black with Dissolve(1)
        pause 2
        scene 07_243 with Dissolve(1)
        mc "That was delicious, Adriana. Thank you very much."
        am "You're welcome."
        am "Nice to hear someone appreciates my food once in a while."
        scene 07_244 with Dissolve(1)
        la "Thank you, Mom."
        am "*Sigh* You had plenty of opportunities..."
        scene black with Dissolve(1)
        pause 2
        scene 07_245 with Dissolve(1)
        mc "I guess I'll be leaving now."
        mc "Thank you again for having me, Adriana."
        am "No, thank you for helping Layla. I really appreciate it."
        mc "Anytime."
        am "Say hi to Emily for me, and ask her to call me so we can have coffee sometime."
        mc "Will do."
        scene 07_246 with Dissolve(1)
        la "I'll see you out."
        mc "Okay. Thanks."
        mc "Bye, Adriana."
        am "Bye, [mc]."
        scene 07_196 with Dissolve(1)
        la "Bye, [mc]."
        la "See you tomorrow, then."
        mc "Yes. Bye, Layla."
        if Layla_Points >= 37:
            scene black with Dissolve(1)
            pause 2
            scene 07_198 with Dissolve(1)
            mc "{i}(What would have happened if her mom didn't show up?){/i}"
            scene 07_199 with Dissolve(1)
            la "Pssst."
            mc "..."
            scene 07_200 with Dissolve(1)
            mc "Hey."
            la "I forgot one thing."
            mc "Yeah?"
            scene 07_201 with Dissolve(1)
            ""
            scene 07_202 with Dissolve(1)
            la "Bye, now."
            mc "Haha..."
            mc "{i}(She's too funny.){/i}"
        else:
            pass
        jump Week2_Weekend_Emily_Adriana
    else:
        scene 07_240a with Dissolve(1)
        am "If there's anything you don't eat, just put it aside."
        mc "Don't worry. My mom is a chef and owns a restaurant. She taught me to eat everything."
        mc "She would literally smack me if I left food on my plate."
        am "Oh? Which restaurant? In the city?"
        mc "Yeah. Rue Madison."
        scene 07_241 with Dissolve(1)
        am "..."
        am "You're Emily's son! I've no idea why I didn't make the connection when I called her on Monday."
        scene 07_242a with Dissolve(1)
        a "You know his mom?"
        am "Yeah. We shared a dorm at MSU for a while."
        la "What? Really?"
        scene black with Dissolve(1)
        pause 2
        scene 07_243 with Dissolve(1)
        mc "That was delicious, Adriana. Thank you very much."
        am "You're welcome."
        am "Nice to hear someone appreciates my food once in a while."
        scene 07_244a with Dissolve(1)
        la "Thank you, Mom."
        a "Thank you."
        am "*Sigh* You had plenty of opportunities..."
        scene black with Dissolve(1)
        pause 2
        scene 07_245 with Dissolve(1)
        mc "I guess I'll be leaving now."
        mc "Thank you again for having me, Adriana."
        am "No, thank you for helping Layla. I really appreciate it."
        mc "Anytime."
        am "Say hi to Emily for me, and ask her to call me so we can have coffee sometime."
        mc "Will do."
        scene 07_246 with Dissolve(1)
        la "I'll see you out."
        mc "Okay. Thanks."
        mc "Bye, Adriana."
        am "Bye, [mc]."
        scene 07_247 with Dissolve(1)
        mc "Bye, Alexis."
        a "Bye-bye!"
        scene 07_196 with Dissolve(1)
        la "Bye, [mc]."
        la "See you tomorrow, then."
        scene black with Dissolve(1)
        pause 2
        scene 07_232 with Dissolve(1)
        a "Hey."
        a "I forgot one thing."
        scene 07_233 with Dissolve(1)
        mc "Yeah?"
        mc "What's that?"
        a "This!"
        scene 07_234 with Dissolve(1)
        ""
        scene 07_234a with Dissolve(1)
        a "Call me later, okay?"
        jump Week2_Weekend_Emily_Adriana

label Week2_Weekend_Emily_Adriana:
    scene black with Dissolve(2)
    pause 2
    scene 07_248 with Dissolve(1)
    m "Hey, you were gone for quite a while."
    scene 07_249 with Dissolve(1)
    mc "Hey, Mom. Yeah. I've been tutoring a classmate."
    scene 07_250 with Dissolve(1)
    mc "You'll never guess who her mom is."
    m "Hmm... Do I know her?"
    mc "Yeah. At least you did."
    scene 07_251 with Dissolve(1)
    m "Let's see..."
    m "So she has a daughter who's the same age as you."
    mc "She has two daughters."
    m "Two? Hmm..."
    m "..."
    m "No, can't think of anyone."
    scene 07_252 with Dissolve(1)
    mc "Adriana."
    m "Adriana Moore?"
    mc "Yes. Your old dormmate at MSU."
    scene 07_253 with Dissolve(1)
    m "Wow... The last time I saw her was at the restaurant. But that was also a while ago."
    m "We didn't speak though. I didn't want to interrupt."
    mc "You actually spoke to her earlier this week. She's also the principal at my school."
    m "Principal Moore... Of course."
    scene 07_254 with Dissolve(1)
    mc "She wants to have coffee sometime with you."
    m "I'll definitely take her up on that offer."
    if Alexis_Friends == True:
        jump Week3_Monday_School
    else:
        jump Week2_Sunday_Alexis_Phone

label Week2_Sunday_Alexis_Phone:
    scene black with Dissolve(2)
    pause 2
    scene 07_256 with Dissolve(1)
    mc "{i}(Maybe she's asleep already? But she asked me to call her. Well, she told me to, actually...){/i}"
    scene 07_258 with Dissolve(1)
    a "Hello?"
    n "*Heavy breathing*"
    mc "Hi. Are you alright?"
    a "Hey. Yeah sorry. I was just about to step into the shower when I heard the phone."
    scene 07_257 with Dissolve(1)
    mc "Hehe. Great minds think alike."
    mc "So, you're basically naked right now?"
    scene 07_259 with Dissolve(1)
    a "..."
    a "I'm wearing a towel!"
    scene 07_260 with Dissolve(1)
    a "What are you wearing?"
    mc "..."
    mc "What am I wearing? Haha... Okay, that was unexpected."
    scene 07_261 with Dissolve(1)
    mc "Uhm... Boxer shorts. That's about it."
    a "Let me take my towel off."
    scene 07_262 with Dissolve(1)
    a "Mmm [mc]... I'm touching my breasts."
    mc "..."
    a "My nipples are so hard."
    a "What do you want me to do?"
    scene 07_263 with Dissolve(1)
    mc "Haha, sorry, Lexi. This is..."
    a "Oh, come on. Just play along."
    a "Please?"
    menu:
        "Sorry":
            scene 07_264 with Dissolve(1)
            mc "Sorry. This isn't for me. It's just awkward and weird..."
            a "*Sigh* Hmm. Okay."
            a "..."
            mc "Sorry, Lexi."
            a "No, it's fine. I've never done this and was just curious."
            scene 07_265 with Dissolve(1)
            a "I'm going to shower then. Speak to you next time?"
            mc "Yeah. Good night, Lexi."
            a "Night, [mc]. Bye."
            $ renpy.end_replay()
            jump Week3_Monday_School
        "Play along[KoGa3AutoWTChange1]{size=-4}(Alexis Week2 Sunday PhoneSex) {/size} {/color}":
            $ Alexis_Week2_Sunday_PhoneSex = True
            mc "I'll try."
            scene 07_266 with Dissolve(1)
            a "How about you take those boxers off and grab your big cock?"
            mc "..."
            scene 07_267 with Dissolve(1)
            mc "What are you doing?"
            a "I'm touching myself for you."
            mc "Where are you touching?"
            a "My breasts..."
            scene 07_268 with Dissolve(1)
            a "And slowly working my way down..."
            a "Are you stroking your cock for me?"
            scene 07_269 with Dissolve(1)
            mc "I am..."
            a "Good!"
            a "*Moaning*"
            a "I'm so horny, [mc]."
            a "Can you help me? What should I do? "
            mc "Slowly rub your clit."
            scene 07_270 with Dissolve(1)
            a "*Moaning*"
            a "This feels so good."
            mc "Are you wet?"
            a "Yes!"
            scene 07_271 with Dissolve(1)
            a "I want you so bad... To feel you inside me..."
            a "Mmm... [mc]."
            scene 07_272 with Dissolve(1)
            a "*Moaning*"
            mc "Now slowly move your finger inside."
            a "How many?"
            mc "Two."
            scene 07_273 with Dissolve(1)
            a "Mmm..."
            scene 07_274 with Dissolve(1)
            ""
            scene 07_275 with Dissolve(1)
            a "[mc]! I'm cumming... [mc]... [mc]..."
            scene 07_276 with Dissolve(1)
            a "*Heavy breathing*"
            scene 07_277 with Dissolve(1)
            mc "Lexi? Still there?"
            a "*Heavy breathing*"
            a "Yeah..."
            scene 07_278 with Dissolve(1)
            a "Haha... That was awkward, but not bad for the first time, right?"
            mc "{i}(Awkward is right.){/i}"
            mc "It was definitely an experience."
            scene 07_279 with Dissolve(1)
            a "*Sigh*"
            mc "What?"
            a "{i}(I want to see you now.){/i}"
            a "Nothing..."
            mc "..."
            scene black with Dissolve(1)
            pause 2
            scene 07_280 with Dissolve(1)
            a "I guess I'm going to shower now."
            mc "Yeah, I might need another one as well."
            a "Haha... Sorry."
            a "I'll call you tomorrow, okay?"
            mc "Okay. Bye, Lexi."
            a "Good night, [mc]."
            mc "Good night!"
            $ renpy.end_replay()
            jump Week3_Monday_School

label Week3_Monday_School:
    scene black with Dissolve(2)
    pause 2
    stop music fadeout 1.0
    play music ("Music/LoFi Upbeat 3.mp3", "Music/LoFi Upbeat 4.mp3", "Music/LoFi Upbeat 1.mp3", "Music/LoFi Upbeat 2.mp3") volume 0.2
    if Layla_Week2_Wednesday_Knows == True:
        $ Valeria_Week3_Monday_Meet = True
        scene 07_281 with Dissolve(1)
        n "Monday, 08:22. School."
        scene 07_282 with Dissolve(1)
        mc "Hey, good morning."
        la "..."
        mc "Can we talk, Layla?"
        scene 07_283 with Dissolve(1)
        la "I need to go to class."
        mc "..."
        mc "Please?"
        scene 07_284 with Dissolve(1)
        mc "*Sigh*"
        mc "I didn't know Alexis was her sister..."
        mc "I met her before I met you guys."
        el "It's not that."
        el "It's the way you told Layla. Well, you didn't even tell her, as far as I know. You were just arguing with Alexis in front of her."
        mc "I know. That's why I want to apologise."
        el "Well, you made this mess, so you'd better figure out how to fix it."
        scene black with Dissolve(1)
        pause 2
        scene 07_295 with Dissolve(1)
        mc "*Sigh*"
        mc "{i}(I hope she won't fail her test because of this...){/i}"
        x "Morning."
        scene black with Dissolve(1)
        transform moveup:
            xalign 0.5 yalign 1.0
            linear 5.0 yalign 0.0
        show 07_296 at moveup
        pause 3
        mc "Hey. Uhm..."
        va "Valeria."
        scene 07_297 with Dissolve(1)
        mc "Oh... You're the new girl. Zach mentioned you."
        va "Yeah, kinda took your role. Heard you just transferred here yourself."
        mc "Yup, still fresh."
        scene 07_298 with Dissolve(1)
        mc "Well, it's nice to meet you, Valeria. I'm [mc]."
        va "Nice to meet you, too."
        mc "So are you..."
        scene 07_299 with vpunch
        z "Heeeey!"
        va "Aaah!"
        scene 07_300 with Dissolve(1)
        va "Zach!"
        z "That's me. The one and only."
        va "Can you put me down, please."
        mc "Hey, Zach."
        scene 07_301 with Dissolve(1)
        z "Hey, man. So, you guys finally met, huh?"
        z "How are you, Val?"
        va "Good, I..."
        scene 07_302 with Dissolve(1)
        z "What did you do on the weekend?"
        va "I..."
        z "Oh yeah, that reminds me. Do you know that we're going to training camp this week?"
        va "Yes, I..."
        z "It's going to be so much fun."
        va "..."
        n "*School bell*"
        scene 07_303 with Dissolve(1)
        va "I'm heading to class. See you guys later. Bye-bye."
        z "Wait, I'm coming with you."
        va "No need. I have to go to the bathroom first."
        z "Okay, see you later then. I'll save you a spot in the cafeteria."
        mc "Bye, Valeria."
        scene 07_304 with Dissolve(1)
        z "See! I told you she's cute. What do you think?"
        menu:
            "Not my type[KoGa3AutoWTChange1]{size=-4}(Valeria Week3 Monday NotMyType) {/size} {/color}":
                $ Valeria_Week3_Monday_NotMyType = True
                mc "Not really my type."
                z "What? Are you kidding me?"
                z "Well, then you'd better get your hand off her butt."
                mc "What?"
            "Cute":
                mc "Yeah, she's very cute."
                z "Right. But she's mine, so you'd better get your hand off her butt."
                mc "What?"
        scene 07_305 with Dissolve(1)
        z "Look! Your shadow hand is touching her butt."
        mc "... Shadow hand? Really Zach?"
        z "Let me..."
        scene 07_306 with Dissolve(1)
        z "Haha, look. I'm smacking it. Haha."
        mc "You are so hopeless."
        z "What do you mean? It's pre... Premo... Pre...tion."
        mc "Precognition?"
        z "Yeah, that."
        scene 07_307 with Dissolve(1)
        va "..."
        z "Shit! Did she hear us?"
        mc "For your sake, I hope not. But I think she did."
        z "Fuck!"
        scene 07_308 with Dissolve(1)
        z "I'd better go after her."
        mc "I need to head to class anyway. Spanish test."
        z "Oooh... Say hi to Gabi for me! And Layla."
        z "Later, man."
        mc "See you later."
        scene 07_309 with Dissolve(1)
        z "VAL! I'm sorry, I was just playing around."
        mc "*Sigh*"
        jump Week3_Monday_Spanish_Test
    else:
        $ Valeria_Week3_Monday_Meet = False
        scene 07_281 with Dissolve(1)
        n "Monday, 08:22. School."
        scene 07_286 with Dissolve(1)
        mc "Hey, good morning."
        la "Good morning, [mc]."
        el "Morning."
        scene 07_287 with Dissolve(1)
        mc "How are you feeling about the test?"
        la "Pretty good actually. Confident I won't fail!"
        mc "Haha. Great!"
        scene 07_288 with Dissolve(1)
        el "Hmm..."
        mc "What?"
        el "Don't tell me you guys are colour coordinating already..."
        menu:
            "Jealous?":
                scene 07_289 with Dissolve(1)
                mc "Jealous much?"
                el "Pfff... As if."
            "Joke":
                scene 07_289 with Dissolve(1)
                mc "What? No. My mom put this out for me this morning."
                el "Your mom still does..."
                mc "I'm kidding, Elena."
                la "Haha."
                el "Yeah, I'm not so sure about that."
        scene 07_290 with Dissolve(1)
        mc "No, seriously, pure coincidence. Nothing more."
        el "Yeah right. You both wear red. Both have skulls on your shirts."
        la "Oh yeah. Didn't even notice. Funny."
        el "Uh-huh..."
        scene 07_291 with Dissolve(1)
        mc "Hey. Don't be sad. Tomorrow we'll coordinate, okay?"
        el "Sure. Let's wear hotpants then."
        scene 07_292 with Dissolve(1)
        mc "..."
        el "Don't look like that! You failed to specify the conditions."
        mc "Well, I don't have hotpants."
        el "I can lend you a pair. Not like it would be the first time I've given you clothes, right?"
        scene 07_293 with Dissolve(1)
        la "Haha... Don't worry, [mc]. I'll take your place and wear them."
        mc "Thanks."
        el "Hey! Don't give him an easy way out. He has..."
        n "*School bell*"
        scene 07_294 with Dissolve(1)
        mc "Saved by the bell! Sorry, Elena. I have to go. Spanish test, you know?"
        mc "See you later."
        el "This conversation isn't over."
        la "[mc], wait for me."
        jump Week3_Monday_Spanish_Test

label Week3_Monday_Spanish_Test:
    scene black with Dissolve(1)
    pause 2
    if Layla_Week2_Wednesday_Knows == True:
        scene 07_310 with Dissolve(1)
        mc "Hey, can we please talk, Layla?"
        la "No. I need to concentrate on the test."
        scene 07_311 with Dissolve(1)
        tr "I'm handing out the tests now. Leave them face down until I say you can start."
        mc "Thanks."
        scene 07_312 with Dissolve(1)
        mc "I'm really sorry, Layla! I..."
        tr "No more talking once you've received your test."
        mc "Sorry."
    else:
        scene 07_310_01 with Dissolve(1)
        mc "Hey, good luck!"
        la "Haha, thanks, you too. Not that you need it, though."
        scene 07_311_01 with Dissolve(1)
        tr "I'm handing out the tests now. Leave them face down until I say you can start."
        mc "Thanks."
        scene 07_312_01 with Dissolve(1)
        mc "Just remember the..."
        tr "No more talking once you've received your test."
        mc "Sorry."
    scene black with Dissolve(1)
    pause 2
    scene 07_313 with Dissolve(1)
    mc "{i}(I hope she's doing alright...){/i}"
    mc "{i}(Maybe I can help her somehow.){/i}"
    scene 07_313a with Dissolve(1)
    mc "Ga... Ms Ramirez."
    tr "Yes, [mc]?"
    mc "I have a question about... a question."
    mc "{i}(That sounded weird.){/i}"
    tr "Wait, I'm coming."
    scene 07_313b with Dissolve(1)
    mc "It's this one."
    tr "Let me see."
    la "..."
    mc "So, if it's..."
    scene 07_313c with Dissolve(1)
    tr "Parece que ya sabes la respuesta.\n(Seems to me you know the answer.)"
    mc "Gracias."
    scene black with Dissolve(1)
    pause 2
    scene 07_314 with Dissolve(1)
    tr "Se acabó el tiempo!\n(Time's up!)"
    tr "Pens down and pass the tests to the front."
    if Layla_Week2_Wednesday_Knows == True:
        scene 07_315 with Dissolve(1)
        la "Fuck!"
        tr "Lenguaje!\n(Language!)"
        mc "Hey. Are you alright?"
        la "..."
        scene 07_316 with Dissolve(1)
        mc "Layla?"
        la "Go away. Leave me alone."
        mc "Listen. I'm so sorry. Can we please talk? Let me explain?"
        la "..."
        mc "Please?"
        scene 07_317 with Dissolve(1)
        la "Not here... Follow me."
        mc "One second. I have to talk to the teacher first."
        la "Meet me outside, then."
        mc "Okay."
        scene 07_328 with Dissolve(1)
        mc "Do you have a minute, Ms Ramirez?"
        tr "Of course, [mc]. What can I help you with?"
        scene 07_329 with Dissolve(1)
        mc "It's about Layla."
        mc "I know she has to get at least a B on this test to not fail this class."
        mc "And... Well. She didn't do as well as she hoped."
        mc "I was supposed to help her study, but I messed it up."
        mc "So it's kinda my fault."
        scene 07_330 with Dissolve(1)
        tr "It's not your fault. I warned Layla before and I gave her plenty of opportunities."
        tr "I offered her some tutoring, gave her assignments to gain some extra credits."
        tr "This is on her."
        scene 07_331 with Dissolve(1)
        mc "Can't she just retake this test?"
        mc "Please?"
        scene 07_332 with Dissolve(1)
        tr "That's not how this works, [mc]."
        tr "She knew the consequences."
        scene 07_333 with Dissolve(1)
        mc "*Sigh*"
        mc "..."
        if Gabi_End == False:
            menu:
                "Steal the tests[KoGa3AutoWTChange1]{size=-4}(Week3 Monday Spanish Steal) {/size} {/color}":
                    $ Week3_Monday_Spanish_Steal = True
                    mc "{i}(I hope this will be worth it...){/i}"
                    mc "Okay, thanks anyway."
                    scene 07_334 with Dissolve(1)
                    tr "{i}(Why is he so concerned about Layla?){/i}"
                    tr "{i}(Are they dating?){/i}"
                    tr "{i}(Why do I even care?){/i}"
                    tr "..."
                    tr "{i}(Why am I thinking about that again...){/i}"
                "Blackmail Gabi[KoGa3AutoWTChange1]{size=-4}(Week3 Monday Spanish Blackmail, Gabi End) {/size} {/color}":
                    $ Week3_Monday_Spanish_Blackmail = True
                    $ Gabi_End = True
                    mc "{i}(So sorry do to this.){/i}"
                    scene 07_335 with Dissolve(1)
                    mc "Well, you kinda owe me..."
                    tr "What do you mean?"
                    scene 07_336 with Dissolve(1)
                    mc "For keeping my mouth shut about... You know what."
                    tr "You promised already not to tell."
                    mc "Now there's a condition attached to it."
                    scene 07_337 with Dissolve(1)
                    tr "Unbelievable... I should've known."
                    mc "..."
                    tr "How can I trust that you'll keep the promise this time?"
                    mc "You can't."
                    tr "..."
                    tr "I totally misjudged you!"
                    menu:
                        "Be mean":
                            mc "Not the first time you've misjudged me."
                            tr "..."
                            scene 07_338 with vpunch
                            ""
                            scene 07_339 with Dissolve(1)
                            tr "Oh no... I'm sorry. I'm so sorry. I didn't mean..."
                            mc "I deserved that."
                            tr "No, you didn't. What am I doing?"
                            mc "{i}(Damn. This is going way too far just for a test...){/i}"
                            mc "Uhm..."
                            scene 07_340 with Dissolve(1)
                            tr "*Sigh*"
                        "Don't react":
                            scene 07_340 with Dissolve(1)
                            tr "*Sigh*"
                    tr "Fine! So you want me to let her retake the test?"
                    mc "No. Just give her a B and leave it at that."
                    tr "..."
                    tr "A B won't help her if she fails on her exams."
                    mc "That will be on her then."
                    tr "..."
                    scene 07_341 with Dissolve(1)
                    mc "So?"
                    tr "..."
                    tr "I'll give her a B."
                    mc "Thank you."
                    tr "Don't thank me. Just get out."
                    scene black with Dissolve(1)
                    pause 2
                    scene 07_342 with Dissolve(1)
                    tr "*Crying*"
                    tr "{i}(Should I just quit my job?){/i}"
                "Leave[KoGa3AutoWTChange1]{size=-4}(Layla Week3 Monday Spanish Fail) {/size} {/color}":
                    $ Layla_Week3_Monday_Spanish_Fail = True
                    mc "Okay, thanks anyway."
                    scene 07_334 with Dissolve(1)
                    tr "{i}(Why is he so concerned about Layla?){/i}"
                    tr "{i}(Are they dating?){/i}"
                    tr "{i}(Why do I even care?){/i}"
                    tr "..."
                    tr "{i}(Why am I thinking about that again...){/i}"
        else:
            menu:
                "Steal the tests[KoGa3AutoWTChange1]{size=-4}(Week3 Monday Spanish Steal) {/size} {/color}":
                    $ Week3_Monday_Spanish_Steal = True
                    mc "{i}(I hope this will be worth it...){/i}"
                    mc "Okay, thanks anyway."
                "Leave[KoGa3AutoWTChange1]{size=-4}(Layla Week3 Monday Spanish Fail) {/size} {/color}":
                    $ Layla_Week3_Monday_Spanish_Fail = True
                    mc "Okay, thanks anyway."
        scene black with Dissolve(1)
        pause 2
        scene 07_343 with Dissolve(1)
        mc "{i}(Didn't Layla say she'll wait outside?){/i}"
        mc "..."
        scene 07_344 with Dissolve(1)
        z "[mc]. Good timing."
        mc "Hey, what's up?"
        z "Have you seen Valeria?"
        mc "No."
        z "Hmm... Where could she be?"
        scene 07_345 with Dissolve(1)
        mc "Hiding would be my guess."
        z "Why would she be hiding?"
        mc "..."
        mc "I don't know, man..."
        scene 07_346 with Dissolve(1)
        z "Well, if you see her, please tell her I'm looking for her."
        mc "Will do. See you at lunch?"
        z "Sure."
        scene 07_347 with Dissolve(1)
        if Week3_Monday_Spanish_Steal == True:
            mc "{i}(Okay, where can she be? She said outside... Did she actually mean outside the school?){/i}"
            mc "{i}(But first, I have to hide these tests.){/i}"
        else:
            mc "{i}(Okay, where can she be? She said outside... Did she actually mean outside the school?){/i}"
        scene black with Dissolve(1)
        pause 2
        scene 07_348 with Dissolve(1)
        mc "Ah... There you are."
        la "..."
        mc "When you said outside, I thought... Never mind."
        scene 07_349 with Dissolve(1)
        mc "*Sigh* Okay..."
        mc "Alexis and I met before my first day here at school."
        mc "I didn't know you were sisters until... You know."
        la "I'm not mad about that. Just the way I had to find out."
        mc "I'm really sorry. That was really a bad moment to bring it up. Especially how I did it."
        mc "Sorry!"
        scene 07_350 with Dissolve(1)
        mc "We met on the plane when I moved back here."
        la "..."
        scene black with Dissolve(1)
        pause 2
        scene 07_351 with Dissolve(1)
        la "So... You and Lexi... Are you..."
        mc "No, we're not together, not dating either. We aren't even friends at this point."
        mc "We hooked up and that's about it."
        mc "We haven't even talked since."
        la "..."
        la "Okay. Thanks for telling me."
        scene 07_352 with Dissolve(1)
        mc "Still mad at me?"
        la "Just a little."
        mc "Are we friends again?"
        la "Yes..."
        la "But before that. I have one more thing. I need to come clean about something too..."
        scene 07_353 with Dissolve(1)
        la "Principal Moore... She's my mom."
        mc "Really?"
        la "Sorry. I just couldn't tell you earlier..."
        scene 07_354 with Dissolve(1)
        mc "Well, that explains some things."
        mc "If my mom was the principal, I wouldn't mention it either."
        mc "There are always some people who will try to ask for favours because of that."
        la "Yeah..."
        mc "Let's just forget about all that and have fun again, right?"
        scene 07_355 with Dissolve(1)
        la "I don't know about fun."
        la "Now I have to take Spanish again in my last semester... Mom's going to be so pissed."
        if Layla_Week3_Monday_Spanish_Fail == True:
            mc "I'll help you this time. I promise."
            la "Thanks."
        else:
            mc "Well, maybe... Let's see first when we get the test back."
        scene 07_356 with Dissolve(1)
        el "Finally... I've been looking for you guys."
        el "I'm happy to see you talked, but didn't you hear the announcement?"
        scene 07_357 with Dissolve(1)
        la "No? What announcement?"
        el "All seniors need to assemble in the cafeteria. Information about training camp."
        la "Oh, okay. Let's go then."
        jump Week3_Monday_Cafeteria
    else:
        scene 07_318 with Dissolve(1)
        mc "So?"
        la "I think I did it. I answered all questions. I'm not sure about a few but, yeah..."
        mc "Great."
        scene 07_319 with Dissolve(1)
        la "Thank you so very much!"
        menu:
            "Look closer[KoGa3AutoWTChange1]{size=-4}({i}Layla Points > 37: Layla Points-2{/i}) {/size} {/color}":
                scene 07_320 with Dissolve(1)
                ""
                if Layla_Points >= 37:
                    scene 07_321a with Dissolve(1)
                    if Layla_Week2_Wednesday_Chichis == True:
                        la "I'm not even mad that you're checking out my chichis."
                    else:
                        la "I'm not even mad that you're checking out my boobs."
                    mc "Haha, sorry."
                    la "It's fine..."
                    scene 07_322 with Dissolve(1)
                    tr "Uh-hum..."
                    scene 07_323 with Dissolve(1)
                    la "What?"
                    tr "Do I really need to read the school rules to you?"
                    la "..."
                    la "No, we're leaving."
                else:
                    $ Layla_Points -= 2
                    scene 07_321 with Dissolve(1)
                    la "Hey. This isn't an invitation to look, okay?"
                    mc "Sorry."
            "Don't look":
                mc "Thank me after you've got the results back."
                if Layla_Points >= 37:
                    scene 07_322 with Dissolve(1)
                    tr "Uh-hum..."
                    scene 07_323 with Dissolve(1)
                    la "What?"
                    tr "Do I really need to read the school rules to you?"
                    la "..."
                    la "No, we're leaving."
                else:
                    tr "Uh-hum..."
        if Gabi_End == False:
            scene 07_324 with Dissolve(1)
            tr "[mc], can I talk to you for a moment?"
            la "*Sigh*"
            mc "Sure."
            la "I'll wait outside for you."
            scene black with Dissolve(1)
            pause 2
            scene 07_325 with Dissolve(1)
            tr "Are you and Layla dating?"
            mc "Uh... That's none of your business..."
            scene 07_326 with Dissolve(1)
            tr "Do you know that she's the principal's daughter?"
            mc "I know, and I fail to see what's the problem with that."
            tr "..."
            mc "If that's all, I'll be leaving..."
            scene black with Dissolve(1)
            pause 2
            scene 07_327 with Dissolve(1)
            tr "{i}(What am I doing?){/i}"
            tr "{i}(Why did I even ask that?){/i}"
            scene 07_343 with Dissolve(1)
            mc "{i}(Didn't Layla say she'll wait outside?){/i}"
            mc "..."
            scene 07_344 with Dissolve(1)
            z "[mc]. Good timing."
            mc "Hey, what's up?"
            z "Have you seen Valeria?"
            mc "Even if I have, I wouldn't know. I haven't met her yet."
            z "You still haven't met her? Dude... Anyway. Where could she be?"
            scene 07_345 with Dissolve(1)
            mc "Hiding would be my guess."
            z "Why would she be hiding?"
            mc "..."
            mc "I don't know, man..."
            scene 07_346 with Dissolve(1)
            z "Well, if you see her, tell her I'm looking for her."
            mc "{i}(I just told you I don't know who she is!){/i}"
            mc "Sure... See you at lunch?"
            z "Yeah. Later dude."
            scene 07_347 with Dissolve(1)
            mc "{i}(Okay, where can she be? She said outside... Did she actually mean outside the school?){/i}"
            scene black with Dissolve(2)
            pause 2
            scene 07_348a with Dissolve(1)
            mc "Ah... There you are."
            la "You took your sweet little time."
            mc "When you said outside, I thought you meant outside the classroom..."
            la "Hehe, sorry. Should've been more specific."
        else:
            pass
        jump Week3_Monday_Layla_Outside

label Week3_Monday_Layla_Outside:
    scene 07_358 with Dissolve(1)
    mc "So? You think you'll get a B?"
    la "Yes. I did really well. I could answer all the questions."
    scene 07_359 with Dissolve(1)
    la "Thank you so very much for helping me."
    mc "Of course."
    la "Now I only need to not fail the exams and then..."
    la "Sayonara, español!"
    mc "That's Japanese..."
    scene 07_360 with Dissolve(1)
    la "What?"
    mc "Sayonara is goodbye in Japanese. Did you mean adiós?"
    scene 07_361 with Dissolve(1)
    la "Oh shit!"
    mc "Did you write sayonara on the test?"
    la "I did..."
    mc "Haha."
    scene 07_362 with Dissolve(1)
    la "Don't laugh!"
    la "Aaah... Now I'm not so sure anymore if I actually did as well as I thought."
    mc "Haha."
    la "Stop laughing!"
    mc "You'll be fine."
    scene 07_363 with Dissolve(1)
    la "[mc]!"
    mc "There, there..."
    el "What's going on here?"
    scene 07_364 with Dissolve(1)
    la "Elena!"
    mc "Konnichiwa, Elena."
    el "Ohayo gozaimasu. Nani desu ka?"
    scene 07_365 with Dissolve(1)
    la "Oh my god you guys, stop with the Spanish!"
    mc "Haha. That was Japanese!"
    el "Huh? What's her deal? And why are we speaking Japanese?"
    la "..."
    scene 07_366 with Dissolve(1)
    mc "This one here wrote sayonara instead of adiós on the test."
    el "Seriously, Layla..."
    la "I know, I know! But doesn't sayonara sound Spanish?"
    el "Not really!"
    scene 07_367 with Dissolve(1)
    la "Can I have a hug?"
    el "No... I don't want your stupidity all over me!"
    if Layla_Points >= 37:
        scene 07_371 with Dissolve(1)
        mc "Ew... That's what this is. I knew I felt something."
        la "You too, now?"
        el "Haha."
        scene 07_372 with Dissolve(1)
        la "I'm leaving..."
        el "Where are you going?"
        la "Anywhere."
        scene 07_373 with Dissolve(1)
        el "Haha. No, you're not."
        la "Hey! Do you think you can stop me?"
        el "I know I can!"
        scene 07_374 with vpunch
        la "Haha. You're cheating!"
        el "How am I cheating?"
        la "You're using your whole body weight."
        scene 07_375 with Dissolve(1)
        la "[mc]! Help me!"
        el "No! Help me!"
        menu:
            "Help Elena[KoGa3AutoWTChange1]{size=-4}(Elena Week3 Monday Help, Elena Points+2) {/size} {/color}":
                $ Elena_Week3_Monday_Help = True
                $ Elena_Points += 2
                # Elena (16)
                scene 07_376 with Dissolve(1)
                la "Aaah... I'm getting squished! Haha..."
                el "I don't see how this is helping me?"
                mc "More weight on top of her."
                el "Yeah, and on me!"
                mc "{i}(Damn... I'm actually getting a hard-on.){/i}"
                scene black with Dissolve(1)
                pause 2
                scene 07_377 with Dissolve(1)
                la "Why are we fighting each other? We girls should stick together against him."
                el "True!"
                mc "What? How can you switch teams so fast..."
            "Help Layla[KoGa3AutoWTChange1]{size=-4}(Layla Points+2) {/size} {/color}":
                $ Layla_Points += 2
                # Layla (56)
                scene 07_378 with Dissolve(1)
                el "Nooo... I was winning!"
                la "Haha."
                la "Thank you, [mc]!"
                scene black with Dissolve(1)
                pause 2
                scene 07_379 with Dissolve(1)
                la "Why are we fighting each other? We girls should stick together against him."
                el "True!"
                mc "What? How can you switch teams so fast..."
            "Don't get involved":
                mc "I'm not going to get involved. I'm enjoying this too much."
                el "What?"
                scene 07_377 with Dissolve(1)
                la "He's right though. Why are we fighting each other? We girls should stick together against him."
                el "True!"
                mc "What? How can this situation change so quickly?"
        scene 07_380 with Dissolve(1)
        la "I've got him, Elena. Take him down!"
        if Elena_Points >= 13:
            scene 07_381 with Dissolve(1)
            mc "Hey now..."
            el "It's not working."
            la "Try something else."
            scene 07_382 with Dissolve(1)
            mc "Elena! Be careful!"
            el "Haha..."
            la "Wait, I'll help."
            scene 07_383 with Dissolve(1)
            mc "Seriously? You guys are crazy..."
            la "He's wobbling."
            scene 07_384 with vpunch
            el "Ouch..."
            mc "Are you..."
            el "..."
            scene 07_385 with Dissolve(1)
            mc "{i}(Shit!){/i}"
            mc "Sorry."
            el "It's okay."
            scene 07_386 with Dissolve(1)
            if Elena_Week3_Monday_Help == True:
                mc "Are you okay?"
                el "Yeah."
                el "You really like lying on top of me, huh?"
                mc "..."
                mc "{i}(Getting a hard-on again...){/i}"
            else:
                mc "Are you okay?"
                el "Yeah."
            scene 07_387 with Dissolve(1)
            la "Are you guys okay?"
            la "Sorry, I might have taken it too far."
            el "We're good."
            scene 07_388 with Dissolve(1)
            el "You held out pretty long."
            el "You sure you don't want to join the cheerleading squad?"
            mc "Haha, still trying, huh? Thanks, but I'm sure."
        else:
            el "I'm good. I'll let you handle it."
            la "..."
        scene black with Dissolve(1)
        pause 2
        scene 07_389 with Dissolve(1)
        mc "Question. How come you speak Japanese, Elena?"
        el "I don't speak it, I just know a few words. I have two little brothers who love watching anime and are shouting random Japanese words all the time."
        el "I just picked up a few."
        mc "Haha, okay."
        si "Ah, there you are."
        scene 07_390 with Dissolve(1)
        la "Hey, Sienna."
        si "Didn't you hear the announcement?"
        el "No? What announcement?"
        scene 07_391 with Dissolve(1)
        si "They asked for all students to assemble in the cafeteria."
        la "Hmm, okay? Do you know what it's about?"
        si "Info about training camp."
        jump Week3_Monday_Cafeteria
    else:
        $ Elena_Week3_Monday_Help = False
        scene 07_368 with Dissolve(1)
        la "ELENA!"
        el "Haha. Come here, my dumdum."
        la "..."
        scene 07_369 with Dissolve(1)
        la "Haha. I'm not a dumdum."
        el "Haha. Your new name will be though!"
        la "ELENA!"
        scene 07_370 with Dissolve(1)
        n "Announcement. Can all students assemble in the cafeteria? I repeat. All students to the cafeteria, please."
        el "I guess we'll be going there, now."
        jump Week3_Monday_Cafeteria

label Week3_Monday_Cafeteria:
    scene black with Dissolve(1)
    pause 2
    scene 07_392 with Dissolve(1)
    t "The rooms are split into four or six students."
    t "I think you're all old enough to create your own groups."
    t "So put the four or six names you want to room with on this sheet here and hand it over to your teacher."
    t "Boys and girls will have separate rooms!"
    x "Booo..."
    x "Come on!"
    scene 07_393 with Dissolve(1)
    t "Students who aren't in a group will be assigned by us."
    el "Ooh... Will be interesting to see who you get assigned with."
    mc "Funny. I'll be able to find three people to room with."
    el "Haha sure..."
    scene 07_394 with Dissolve(1)
    t "Three other schools will be attending."
    t "There will be a competition on Saturday."
    mc "Oh, a competition."
    la "Yeah, should be fun."
    mc "If I knew that, I would've trained a bit more the last couple of weeks."
    scene 07_395 with Dissolve(1)
    la "I could use some more training too. How about we go run together?"
    mc "Sounds good."
    la "Tomorrow, after school?"
    mc "Sure."
    scene 07_396 with Dissolve(1)
    t "The whole schedule will be handed out by the end of the day."
    t "Don't worry. You'll have some free time too."
    t "But remember. This training camp is mandatory and your performance will be evaluated."
    t "Are there any questions?"
    scene 07_397 with Dissolve(1)
    el "So, are we going with four or six?"
    la "I'd rather have only four."
    el "Yeah, I agree. You, me, Sienna and MacKenzie?"
    la "Uh-huh."
    scene 07_398 with Dissolve(1)
    el "Hey Sienna. Can you come here for a second?"
    si "Sure."
    scene 07_399 with Dissolve(1)
    el "So, we were thinking about you, MacKenzie, me and Layla."
    si "Sounds good."
    el "Can you ask MacKenzie if she's okay with it?"
    si "I'm sure she will be."
    scene 07_400 with Dissolve(1)
    z "[mc]!"
    z "Do you already have a group?"
    mc "No, not yet."
    z "Awesome. We need one more. You in?"
    mc "Sure. Thanks."
    scene 07_401 with Dissolve(1)
    el "Oh, look at that. Lucky you."
    mc "You sound disappointed that I have some friends after all, Elena."
    el "Totally."
    scene 07_402 with Dissolve(1)
    z "By the way. Do you guys still have room? Val here needs a group."
    va "Uhm... Zach, I..."
    el "We have our group already."
    scene 07_403 with Dissolve(1)
    la "Sorry, Val."
    va "It's okay Layla. Don't worry."
    scene 07_404 with Dissolve(1)
    si "Hey, I've got us the document we need to fill in for the group."
    la "Thanks, Sienna."
    si "Want to fill it out now?"
    el "Sure."
    scene 07_405 with Dissolve(1)
    la "See you guys later."
    el "Bye-bye."
    if Layla_Week2_Wednesday_Knows == False:
        scene 07_406 with Dissolve(1)
        z "You guys don't really know each other yet, right?"
        z "Let me introduce you. This is [mc]."
        z "[mc], this is Valeria."
        scene 07_407 with Dissolve(1)
        mc "Hi, nice to meet you."
        va "Hey. You too, [mc]."
        mc "Even though it feels like I know you already. Zach's told me so much."
        va "Haha. I feel the same about you."
        z "Hey, I talk about other things too..."
        scene 07_408 with Dissolve(1)
        z "I'm gonna get us one of those group documents too."
    else:
        scene 07_408 with Dissolve(1)
        z "I'm gonna get us one of those group documents too."
    mc "Okay, thanks."
    z "Are you coming with me?"
    va "Uhm..."
    z "We might find a group for you."
    va "Hmm... Sure, I guess."
    scene 07_409 with Dissolve(1)
    z "[mc], see you later."
    mc "Later, man."
    va "Bye."
    mc "Bye, Valeria."
    jump Week3_Monday_Elena_Phone

label Week3_Monday_Elena_Phone:
    scene black with Dissolve(1)
    pause 2
    scene 07_410 with Dissolve(1)
    el "But this is important. We need to train for the competition."
    el "..."
    el "I know that."
    scene 07_411 with Dissolve(1)
    el "Isn't there someone else who can do it?"
    el "..."
    el "*Sigh* Fine!"
    menu:
        "Talk to her[KoGa3AutoWTChange1]{size=-4}(Elena Points+2) {/size} {/color}":
            $ Elena_Points += 2
            # Elena (18)
            scene 07_412 with Dissolve(1)
            mc "Hey. Is everything okay?"
            el "Yeah. Don't worry about it."
            mc "..."
            mc "Okay. See you tomorrow."
            el "Bye [mc]."
            if Elena_Points >= 15:
                mc "Bye."
                scene 07_413 with Dissolve(1)
                el "Actually..."
                mc "Yeah?"
                el "You might be able to help me out."
                mc "Shoot."
                scene 07_414 with Dissolve(1)
                el "We arranged a few more training sessions with the squad after school. To prepare for the competition on Saturday."
                el "But my mom has a late shift and I have to watch my brothers. So I can't go."
                mc "Uhm... So you want me to watch them?"
                scene 07_415 with Dissolve(1)
                el "No. You're basically a stranger to my mom, so she wouldn't agree to that."
                el "Besides, if it was that easy, I would've asked Layla."
                el "I was actually hoping you could come over and help me train?"
                mc "..."
                scene 07_416 with Dissolve(1)
                mc "You know... Just because I still have that t-shirt, doesn't mean I know anything about cheerleading."
                el "Haha. Are you sure about that?"
                el "Well, I have to work on my balance when I'm held in the air."
                el "So basically all I need you to do is lift me up and hold me there."
                scene 07_417 with Dissolve(1)
                mc "Isn't that dangerous? As I said, I have zero experience."
                el "You're strong, and you did it before. In the ocean, remember?"
                mc "Yeah, in the ocean... Water..."
                el "It will be fine."
                scene 07_418 with Dissolve(1)
                mc "*Sigh*"
                el "Please? It would help me out immensely."
                menu:
                    "I can't":
                        scene 07_419 with Dissolve(1)
                        mc "Sorry, Elena. I can't. If something goes wrong, I don't want you to get hurt."
                        el "I understand. Better safe than sorry."
                        scene 07_420 with Dissolve(1)
                        mc "When we visit the beach again, I can help you out. I'm much more comfortable doing it in the water."
                        el "Cool. I'll hold you to that."
                        scene 07_421 with Dissolve(1)
                        el "Thanks, [mc]. See you tomorrow?"
                        mc "Yeah. Bye, Elena."
                        el "Bye."
                        jump Week3_Monday_Afternoon_Home
                    "Okay[KoGa3AutoWTChange1]{size=-4}(Elena Week3 Monday CheerTraining, Elena Points+2) {/size} {/color}":
                        $ Elena_Week3_Monday_CheerTraining = True
                        $ Elena_Points += 2
                        # Elena (20)
                        scene 07_422 with Dissolve(1)
                        mc "Okay, we can try."
                        el "Really?"
                        mc "But if it's not working out or gets too dangerous, we stop."
                        el "Deal."
                        scene 07_423 with Dissolve(1)
                        el "Thank you, [mc]."
                        mc "Uh-huh."
                        scene 07_420 with Dissolve(1)
                        el "So, let's say seven o'clock at my place?"
                        mc "Works for me."
                        el "I'll text you the address."
                        el "See you later, then."
                        scene 07_421 with Dissolve(1)
                        mc "Yeah. Bye, Elena."
                        el "Bye, [mc]."
                        jump Week3_Monday_Afternoon_Home
            else:
                mc "Bye."
                jump Week3_Monday_Afternoon_Home
        "Go home":
            scene 07_412a with Dissolve(1)
            mc "See you tomorrow, Elena."
            el "Bye, [mc]."
            jump Week3_Monday_Afternoon_Home

label Week3_Monday_Afternoon_Home:
    scene black with Dissolve(1)
    pause 2
    stop music fadeout 1.0
    play music ("Music/LoFi Indie 3.mp3", "Music/LoFi Indie 1.mp3", "Music/LoFi Indie 2.mp3") volume 0.2
    scene 07_424 with Dissolve(1)
    mc "See you later, Mom."
    m "Oh? You're going out?"
    if Elena_Week3_Monday_CheerTraining == False:
        mc "Yeah. Going for a run."
    else:
        $ Elena_Week3_Monday_Backflip = True
        mc "I need to help out a friend."
    m "Okay. Have fun."
    scene 07_425 with Dissolve(1)
    m "Before I forget. Can you get some groceries on your way back?"
    m "I have to go to the restaurant and do inventory, and I don't have time to go to the store."
    mc "Sure. What do you need?"
    m "I'll text you a list."
    scene 07_426 with Dissolve(1)
    mc "A list? How long of a list are we talking about?"
    m "Not that long."
    scene 07_427 with Dissolve(1)
    mc "By the way. Have you seen my white tank top? I can't find it anywhere."
    m "Did you put it in the laundry basket? I haven't done white laundry yet, might be still in there."
    mc "Hmm... Could be."
    scene 07_428 with Dissolve(1)
    mc "Well, see you later, then."
    m "I don't know when I'm going to be home yet, might be very late."
    mc "Okay. Bye, Mom."
    m "Bye, honey."
    if Elena_Week3_Monday_CheerTraining == False:
        jump Week3_Monday_Erynn_Ethan
    else:
        jump Week3_Monday_Elena_CheerTraining

label Week3_Monday_Elena_CheerTraining:
    if _in_replay:
        $ Elena_Points = 20
        $ Elena_Week1_TrainKiss = True
        $ Elena_Week1_Saturday_Beach_Reminder = True
        $ Elena_Week3_Monday_Help = True
    scene black with Dissolve(1)
    pause 2
    stop music fadeout 1.0
    play music ("Music/LoFi Spanish 1.mp3", "Music/LoFi Spanish 2.mp3", "Music/LoFi Spanish 3.mp3") volume 0.2
    scene 07_429 with Dissolve(1)
    mc "This is it."
    scene 07_430 with Dissolve(1)
    n "*Knock-knock*"
    el "One second."
    scene 07_431 with Dissolve(1)
    mc "Uhm... Hi."
    mc "..."
    scene 07_432 with Dissolve(1)
    el "Mateo, what did I say about answering the door?"
    ma "Not to open it."
    el "Exactly..."
    scene 07_433 with Dissolve(1)
    el "Sorry about that."
    mc "No worries."
    el "Thank you for coming. Come on in."
    mc "Thanks."
    scene 07_434 with Dissolve(1)
    ma "Elena has a boyfriend. Elena has a boyfriend."
    el "He's not my boyfriend."
    ma "Elena has a boyfriend."
    el "..."
    el "Go watch TV with your brother."
    scene 07_435 with Dissolve(1)
    ma "Elena has a boyfriend."
    el "*Sigh*"
    el "Please just ignore him."
    scene black with Dissolve(1)
    pause 2
    scene 07_436 with Dissolve(1)
    el "Can you wait here for a moment?"
    el "I need to check up on the boys and change real quick."
    el "Do you want something to drink?"
    mc "Thanks, I'm good for now."
    scene 07_437 with Dissolve(1)
    el "Be right back. Don't go anywhere."
    mc "Haha. No worries."
    scene black with Dissolve(1)
    pause 2
    scene 07_438 with Dissolve(1)
    mc "{i}(Let's warm up already.){/i}"
    scene black with Dissolve(1)
    pause 2
    scene 07_439 with Dissolve(1)
    el "READY! OKAY!"
    mc "Haha..."
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 07_440 at moveup
    pause 3
    el "Haha. Don't ever tell anyone I just did that..."
    mc "Isn't that what cheerleaders do? Cheer?"
    el "Uh-huh... Exactly like this. Haha."
    scene 07_441 with Dissolve(1)
    mc "I totally misjudged you, you know?"
    el "Yeah? In what way."
    mc "Personality."
    scene 07_442 with Dissolve(1)
    el "Oh? You thought I'd be a bitch?"
    menu:
        "Yes":
            scene 07_443 with Dissolve(1)
            mc "Yes."
            el "Haha."
        "No":
            scene 07_443 with Dissolve(1)
            mc "What? Of course not."
            el "Liar!"
    scene 07_444 with Dissolve(1)
    el "I'm a bitch most of the time. But not to the people I like."
    mc "What changed your mind about me?"
    el "Who said I did?"
    mc "Ouch..."
    el "No, honestly. I got to know you and the way you are with Layla."
    scene 07_445 with Dissolve(1)
    mc "Can you do a cheer for me?"
    el "I don't like you that much! Besides, you already got one."
    mc "True. But I'd really like to see you cheer for real."
    el "..."
    el "Well, come watch us at training camp, then."
    mc "I just might. And if you win, I'll cheer for you."
    scene 07_446 with Dissolve(1)
    mc "GO ELENA, GO!"
    el "Haha, stop! You'll never make me forget that, huh?"
    if Elena_Week1_Saturday_Beach_Reminder == True:
        mc "Nope, just like that drunken kiss."
        el "..."
        scene 07_447 with Dissolve(1)
        el "I totally forgot about that. Thanks for bringing it up again."
        mc "I told you I would remind you."
        el "I thought you were joking."
        mc "I am."
        el "..."
        scene 07_448 with Dissolve(1)
        el "Enough about drunk kisses and awful cheers. How about we start?"
    else:
        scene 07_448 with Dissolve(1)
        el "Enough about awful cheers. How about we start?"
    mc "Sure, I'm good to go. All warmed up."
    scene 07_449 with Dissolve(1)
    el "Let me stretch a bit."
    scene 07_450 with Dissolve(1)
    mc "You're very flexible."
    el "I need to be."
    scene 07_451 with Dissolve(1)
    mc "..."
    if Elena_Week3_Monday_Help == False:
        mc "{i}(This is the second time today Elena has given me a hard-on...){/i}"
    else:
        mc "{i}(This is the third time today Elena has given me a hard-on...){/i}"
    mc "{i}(Now isn't really the time though.){/i}"
    mc "{i}(Okay [mc], start thinking about other stuff...){/i}"
    scene 07_451b with Dissolve(1)
    mc "{i}(Mr Coleman...){/i}"
    mc "{i}(The neighbour's dog puking...){/i}"
    mc "{i}(Smelly feet...){/i}"
    mc "{i}(Okay... It's working.){/i}"
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 07_451a at moveup
    pause 3
    el "No-no-no. Not so fast."
    mc "{i}(FUCK!){/i}"
    scene black with Dissolve(1)
    pause 2
    scene 07_443 with Dissolve(1)
    el "Hey, are you okay?"
    mc "Butt."
    el "Huh?"
    mc "I mean what! What did you say? Ha... Ha..."
    el "Nothing..."
    scene black with Dissolve(1)
    pause 2
    scene 07_448 with Dissolve(1)
    mc "Do you also do all that flippy stuff?"
    el "Flippy stuff?"
    mc "Yeah. Like backflips, cartwheels and so on."
    el "I do."
    mc "Oh, you gotta teach me how to do a backflip some time."
    el "Sure."
    el "Okay, let's start with me sitting on your shoulders."
    mc "Easy enough."
    scene black with Dissolve(1)
    pause 2
    scene 07_452 with Dissolve(1)
    el "How's this?"
    mc "No problem. Not much different from a piggyback ride."
    el "I'll try standing up now."
    mc "Do I have to hold something?"
    el "Yeah, my ankles."
    scene 07_453 with Dissolve(1)
    el "How are you holding up?"
    mc "Still fine."
    scene 07_454 with Dissolve(1)
    mc "Just your shoes are digging into my shoulders."
    el "Sorry..."
    menu:
        "Look up[KoGa3AutoWTChange1]{size=-4}(Elena Points-2) {/size} {/color}":
            $ Elena_Points -= 2
            scene 07_455 with Dissolve(1)
            mc "..."
            scene 07_456 with Dissolve(1)
            mc "{i}(Being a male cheerleader isn't that bad after all. Especially with these views.){/i}"
            scene 07_457 with Dissolve(1)
            el "Hey! Keep it steady!"
            mc "What? Oh shit!"
            scene 07_458 with Dissolve(1)
            el "Aaah!"
            scene 07_464 with vpunch
            el "Ouch..."
            mc "Are you alright?"
            el "Yeah. Thanks for catching me."
            scene 07_465 with Dissolve(1)
            mc "Who's lying on top of who now?"
            el "Haha..."
            scene 07_466 with vpunch
            ma "What are you doing there Elena?"
        "Keep steady":
            scene 07_459 with Dissolve(1)
            el "Okay, cradle!"
            mc "Wait, what? Cradle?"
            el "I jump down and you catch me."
            mc "Uhm..."
            el "Here I go!"
            mc "Wait..."
            scene 07_460 with Dissolve(1)
            el "..."
            scene 07_461 with Dissolve(1)
            el "Not really a cradle, but it works I guess."
            scene 07_462 with Dissolve(1)
            el "..."
            scene 07_463 with vpunch
            ma "What are you doing there? Elena, I can see your butt."
            el "Uhm..."
    scene 07_467 with Dissolve(1)
    el "Mateo! Uhm... Aren't you watching TV?"
    ma "I'm hungry."
    el "Okay. I'll make you something."
    scene 07_468 with Dissolve(1)
    el "Sorry. Give me a few minutes."
    mc "Take your time."
    el "Are you hungry? Do you want anything?"
    mc "I'm good, thanks."
    el "Okay. Be right back."
    scene black with Dissolve(1)
    pause 2
    scene 07_469 with Dissolve(1)
    ma "Haha."
    mc "You will never defeat me!"
    ma "Yes, we will!"
    mc "*Evil laugh*"
    scene 07_470 with Dissolve(1)
    el "..."
    el "{i}(What's going on there?){/i}"
    scene 07_471 with Dissolve(1)
    mc "You are no match for me!"
    ma "Shoot him!"
    scene 07_472 with Dissolve(1)
    mc "Aaah. No... I got hit. How can this be?"
    ma "We got him. We got him."
    scene 07_473 with Dissolve(1)
    el "..."
    el "{i}(Boys.){/i}"
    scene black with Dissolve(1)
    pause 2
    scene 07_474 with Dissolve(1)
    el "Guys. Food is ready. Come on in."
    ma "We're not hungry."
    el "*Sigh*"
    scene 07_475 with Dissolve(1)
    el "You can watch TV while eating."
    ma "Yay!"
    scene black with Dissolve(1)
    pause 2
    scene 07_476 with Dissolve(1)
    el "Here, catch!"
    mc "Thanks."
    scene 07_477 with Dissolve(1)
    mc "Damn. Those burgers looked good. Bit bummed I said no earlier."
    el "Haha. Do you want one?"
    mc "No, no. I'm good."
    el "You sure?"
    mc "Yeah. Thanks."
    scene 07_478 with Dissolve(1)
    el "..."
    el "{i}(Stop looking already, Elena!){/i}"
    scene 07_479 with Dissolve(1)
    el "Up for another round?"
    mc "Let's do it."
    scene black with Dissolve(1)
    pause 2
    el "And cradle..."
    scene 07_480 with Dissolve(1)
    el "Wow... That was really good!"
    scene 07_481 with Dissolve(1)
    mc "Yeah?"
    el "Uh-huh. I'm impressed."
    el "I think..."
    mc "I'm not joining the cheer squad."
    scene 07_482 with Dissolve(1)
    el "Haha... Okay!"
    el "But if I need a training partner again. I'm calling you."
    mc "Haha, sure."
    scene black with Dissolve(1)
    pause 2
    scene 07_483 with Dissolve(1)
    el "Thank you very much, [mc], for helping me out."
    mc "Anytime, Elena."
    el "I owe you one."
    mc "Well, teach me how to do a backflip and we're even."
    el "Haha okay."
    scene 07_484 with Dissolve(1)
    el "Bye, [mc]."
    mc "See you tomorrow, Elena."
    ma "Elena has a boyfriend."
    scene 07_485 with Dissolve(1)
    el "Here we go again..."
    mc "Haha."
    ma "Elena has a boyfriend."
    scene 07_486 with Dissolve(1)
    el "Bye, [mc]."
    mc "*Sings* Elena has a boyfriend."
    scene 07_487 with Dissolve(1)
    el "Dios mío..."
    mc "What? It's catchy..."
    el "*Sigh*"
    el "Just go home..."
    mc "Haha. See you tomorrow."
    scene 07_488 with Dissolve(1)
    el "{i}(I know what you mean, Layla...){/i}"
    $ renpy.end_replay()
    jump Week3_Monday_Erynn_Ethan

label Week3_Monday_Erynn_Ethan:
    scene black with Dissolve(1)
    pause 2
    stop music fadeout 1.0
    play music "Music/Battle_Rock.mp3" volume 0.6
    if Elena_Week3_Monday_CheerTraining == True:
        scene 07_492 with Dissolve(1)
        mc "{i}(Oh, a message from Mom... Right, I still need to get those groceries.){/i}"
        mc "{i}(That's quite the list. Didn't she say it wouldn't be too much?){/i}"
    else:
        scene 07_489 with Dissolve(1)
        ""
        scene 07_490 with Dissolve(1)
        mc "{i}(That's enough for today. I still need to get those groceries.){/i}"
        scene 07_491 with Dissolve(1)
        mc "{i}(Let's see. Well, that's quite the list, actually.){/i}"
    scene black with Dissolve(1)
    pause 2
    scene 07_493 with Dissolve(1)
    mc "{i}(I think I've got everything.){/i}"
    x "What do you want now?"
    mc "{i}(That sounded just like Erynn...){/i}"
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 07_493a at moveup
    pause 3
    mc "{i}(It is her.){/i}"
    scene 07_494 with Dissolve(1)
    mc "..."
    et "I have several complaints about you."
    mc "{i}(Ethan! Again... What's going on here?){/i}"
    scene 07_495 with Dissolve(1)
    et "You cry all the time or you're on your phone. You're hired to give them a good time. All the other stuff you can do at home."
    et "You know how much they pay me. And I hate to lose money."
    et "So if they want to touch your butt. You let them touch your butt!"
    scene 07_496 with Dissolve(1)
    er "No!"
    et "Yes!"
    er "NO!"
    et "YES! And start being more flirty. Actually make it look like you enjoy being there."
    scene 07_497 with Dissolve(1)
    er "I don't enjoy this. I HATE this. I don't want to do this. Please, Ethan."
    et "You hate this? You're the one who wanted to be a model."
    er "A model, not what you make me do."
    scene 07_498 with Dissolve(1)
    et "What's the difference? You get paid, wear expensive clothes, and show your body. Hey, they even take pictures of you. All things a model does."
    er "..."
    er "You are unbelievable."
    et "But I ain't wrong, right?"
    scene 07_499 with Dissolve(1)
    er "Shut up, Ethan!"
    scene 07_500 with Dissolve(1)
    et "Heh... Look at you. Since your little buddy got back, you've became much more mouthy again... I don't like it. I don't like him."
    et "He's a bad influence. So how about you stay away from him."
    er "Leave him out of it. He has nothing to do with this."
    et "How wrong you are, Erynn. This feels just like years ago."
    er "..."
    scene 07_501 with Dissolve(1)
    mc "{i}(What's he on about?){/i}"
    scene 07_502 with Dissolve(1)
    et "We'll talk about this another day. Let's go back inside and make the client happy."
    er "Haven't I done enough? Why do you keep doing this to me? Please, Ethan. Let's just stop this."
    scene 07_503 with Dissolve(1)
    et "This can all be over today. You know what I want."
    er "You must be delusional if you still think that's ever going to happen..."
    scene 07_504 with Dissolve(1)
    et "Come on. I know you want to. I see how you look at me. Let's just have some fun."
    er "Don't touch me!"
    scene 07_505 with Dissolve(1)
    et "Well, if you don't want to do it, you'd better get used to this."
    scene 07_506 with vpunch
    er "Get your filthy hands off me!"
    et "..."
    scene 07_507 with vpunch
    er "Aaah..."
    et "BITCH! Know your place!"
    mc "{i}(What the fuck!){/i}"
    menu:
        "Stay out of it[KoGa3AutoWTChange1]{size=-4}(Erynn End, Erynn Points-20, Alexis Points-20, Layla Points-20, Elena Points-20, Valeria Points-20, Melissa Points-10, Emily Points-10, Layla Friends, Elena Friends, Valeria Friends) {/size} {/color}":
            $ Erynn_End = True
            $ Erynn_Points -= 20
            $ Alexis_Points -= 20
            $ Layla_Points -= 20
            $ Elena_Points -= 20
            $ Valeria_Points -= 20
            $ Melissa_Points -= 10
            $ Emily_Points -= 10
            $ Layla_Friends = True
            $ Elena_Friends = True
            $ Valeria_Friends = True
            mc "{i}(I don't know what happened to you, Erynn.){/i}"
            mc "{i}(This is not who I thought you were.){/i}"
            mc "{i}(I'm not getting involved in this shit.){/i}"
            $ achievement.grant("ACHIEVEMENT_ERYNN_HELP")
            $ achievement.sync()
            scene 07_524 with Dissolve(1)
            er "{i}([mc]?){/i}"
            er "..."
            er "{i}(Please?){/i}"
            et "Listen, I'm sorry Erynn. But you shouldn't have hit me."
            jump Week3_Tuesday_School
        "Help Erynn[KoGa3AutoWTChange1]{size=-4}(Erynn Week3 Monday Help, Erynn Points+2) {/size} {/color}":
            $ Erynn_Week3_Monday_Help = True
            $ Erynn_Points += 2
            # Erynn (30)
            scene 07_508 with Dissolve(1)
            mc "HEY!"
            scene 07_509 with Dissolve(1)
            er "[mc]!"
            er "{i}(What's he doing here?){/i}"
            scene 07_510 with vpunch
            mc "Fucking asshole."
            scene 07_511 with Dissolve(1)
            mc "Hitting girls. You really are the lowest of the low!"
            menu:
                "Punch[KoGa3AutoWTChange1]{size=-4}(Ethan Punch+1) {/size} {/color}":
                    jump Week3_Monday_Ethan_Hit1
                "Help Erynn":
                    jump Week3_Monday_Erynn_Help

label Week3_Monday_Ethan_Hit1:
    $ Ethan_Punch += 1
    if Ethan_Punch >= 50:
        $ achievement.grant("ACHIEVEMENT_FATALITY")
        $ achievement.sync()
    else:
        pass
    scene 07_512 with vpunch
    ""
    menu:
        "Punch[KoGa3AutoWTChange1]{size=-4}(Ethan Punch+1) {/size} {/color}":
            jump Week3_Monday_Ethan_Hit2
        "Help Erynn":
            jump Week3_Monday_Erynn_Help

label Week3_Monday_Ethan_Hit2:
    $ Ethan_Punch += 1
    if Ethan_Punch >= 50:
        $ achievement.grant("ACHIEVEMENT_FATALITY")
        $ achievement.sync()
    else:
        pass
    scene 07_513 with vpunch
    ""
    menu:
        "Punch[KoGa3AutoWTChange1]{size=-4}(Ethan Punch+1) {/size} {/color}":
            jump Week3_Monday_Ethan_Hit3
        "Help Erynn":
            jump Week3_Monday_Erynn_Help

label Week3_Monday_Ethan_Hit3:
    $ Ethan_Punch += 1
    if Ethan_Punch >= 50:
        $ achievement.grant("ACHIEVEMENT_FATALITY")
        $ achievement.sync()
    else:
        pass
    scene 07_514 with vpunch
    ""
    menu:
        "Punch[KoGa3AutoWTChange1]{size=-4}(Ethan Punch+1) {/size} {/color}":
            jump Week3_Monday_Ethan_Hit4
        "Help Erynn":
            jump Week3_Monday_Erynn_Help

label Week3_Monday_Ethan_Hit4:
    $ Ethan_Punch += 1
    if Ethan_Punch >= 50:
        $ achievement.grant("ACHIEVEMENT_FATALITY")
        $ achievement.sync()
    else:
        pass
    scene 07_515 with vpunch
    ""
    menu:
        "Punch":
            jump Week3_Monday_Ethan_Hit1
        "Help Erynn":
            jump Week3_Monday_Erynn_Help

label Week3_Monday_Erynn_Help:
    scene 07_516 with Dissolve(1)
    mc "I should've done this years ago..."
    scene 07_517 with Dissolve(1)
    mc "*Heavy breathing*"
    er "[mc]?"
    scene 07_518 with Dissolve(1)
    mc "Are you alright?"
    er "..."
    scene 07_519 with Dissolve(1)
    mc "Erynn?"
    scene 07_520 with Dissolve(1)
    er "*Crying*"
    scene 07_521 with Dissolve(1)
    mc "Come here."
    mc "Hey, it'll be alright. Come on, I'll take you home."
    er "*Nods*"
    scene black with Dissolve(1)
    pause 2
    stop music fadeout 1.0
    play music ("Music/Valeria - Emptiness.mp3", "Music/Slow.mp3", "Music/Slow4.mp3") volume 0.5
    scene 07_522 with Dissolve(1)
    mc "Did you drive here?"
    er "No... Ethan brought me here."
    mc "Okay. We'll take the bus then."
    scene 07_523 with Dissolve(1)
    mc "Hold on. I need to grab the groceries."
    scene black with Dissolve(1)
    pause 2
    scene 07_525 with Dissolve(1)
    er "[mc], I..."
    mc "Tell me at home."
    scene 07_526 with Dissolve(1)
    mc "Just close your eyes for now."
    mc "I'll tell you when we arrive."
    scene black with Dissolve(2)
    pause 2
    scene 07_527 with Dissolve(1)
    mc "Feeling better?"
    er "Yes, thank you."
    mc "Do you want to change first, or..."
    er "No... Let's just sit down."
    scene black with Dissolve(1)
    pause 2
    scene 07_528 with Dissolve(1)
    mc "So, what's the deal between you and Ethan? Why are you still hanging around with that asshole?"
    mc "Especially if he treats you like that."
    er "Because I have no other choice."
    mc "What do you mean? No other choice?"
    scene 07_529 with Dissolve(1)
    er "Ethan's dad is the CEO of the model agency I work for, I didn't know that until Ethan joined the company last year and became my agent."
    mc "..."
    mc "Why don't you just quit and join another company?"
    er "I can't."
    mc "Why not? Is it because of a non-compete clause in your contract or something?"
    er "No..."
    scene 07_530 with Dissolve(1)
    mc "*Sigh*"
    mc "Erynn... I can only help if you tell me."
    er "You're going to hate me for this."
    scene 07_531 with Dissolve(1)
    er "Ethan he... He has a..."
    mc "Erynn..."
    er "..."
    mc "He has what?"
    er "He has a... A sex tape."
    mc "What? A sex tape? Of you?"
    er "Yes..."
    scene 07_532 with Dissolve(1)
    mc "Wait, what? How? You slept with Ethan?"
    er "NO! Why would you even think that?"
    mc "Heh?"
    scene 07_533 with Dissolve(1)
    mc "Then why does he... I don't get it."
    er "*Sigh*"
    mc "Don't tell me you sent it to him..."
    er "..."
    mc "Tell me everything. From the beginning."
    scene black with Dissolve(1)
    pause 2
    scene 07_534 with Dissolve(1)
    er "Ethan was... Is always jealous of you. Because of the relationship we had."
    er "But all those years ago, when you left, he changed. Can you believe that he actually became friendlier... Or so I thought."
    er "Once he knew you and I weren't in contact anymore, he asked me out."
    scene 07_535 with Dissolve(1)
    er "I never liked him in that way, so I rejected him. Multiple times! He didn't handle it very well..."
    er "He stopped his friendly facade and went back to his old ways of being jealous and bullying everyone I was talking to."
    er "It was so bad for a while that Alexis was the only one left who would talk to me."
    er "He tried to break that friendship too. He almost succeeded when he told me that Alexis slept with him."
    if Alexis_Friends == False:
        scene 07_536 with Dissolve(1)
        mc "{i}(She would never, right?){/i}"
        mc "Did she?"
        er "She always denied it and I believed her, but..."
        mc "But because she didn't tell you about us you think she lied about that?"
        er "..."
        mc "{i}(Fuck! I have to ask her. I hope she didn't...){/i}"
    else:
        scene 07_536 with Dissolve(1)
        mc "Did she?"
        er "No. Alexis would never. She actually hates Ethan."
    scene 07_537 with Dissolve(1)
    er "After all that, I broke my friendship with Ethan. Something I should've done way earlier. We didn't hang out anymore, didn't even speak to each other."
    er "Everything became somewhat normal again."
    er "*Sigh*"
    mc "That normal didn't last long?"
    er "A while..."
    scene 07_538 with Dissolve(1)
    er "In my senior year, I started dating Zane."
    mc "{i}(Zane... I was never good at remembering people, but he sounds familiar.){/i}"
    mc "{i}(This isn't the right time to ask her about him though...){/i}"
    er "We were getting serious. We went on a date, and after..."
    er "..."
    scene 07_539 with Dissolve(1)
    mc "After?"
    er "*Sigh* I don't even know how he knew..."
    mc "Uhm Erynn... Who knew what? I can't follow anymore."
    scene 07_540 with Dissolve(1)
    er "Ethan..."
    er "He recorded us having..."
    mc "{i}(The sex tape.){/i}"
    scene 07_541 with Dissolve(1)
    er "*Crying*"
    mc "Hey, it's alright. Let it all out."
    scene black with Dissolve(1)
    pause 2
    scene 07_542 with Dissolve(1)
    mc "So what did he do with the video? Did he blackmail you?"
    er "He said he'd delete it if I went to prom with him."
    mc "That explains the prom picture..."
    mc "What did Zane say or do about that?"
    er "He didn't know. I never told him. We broke up when I declined his prom proposal and went with Ethan instead."
    scene 07_543 with Dissolve(1)
    mc "*Sigh* Erynn..."
    er "..."
    mc "But continue... He deleted the video, then what?"
    er "..."
    scene 07_544 with Dissolve(1)
    er "He didn't delete it."
    mc "What? Wasn't that the deal? Didn't you check?"
    er "I didn't want to see it."
    scene 07_545 with Dissolve(1)
    mc "Wait, wait... Hold on a second."
    mc "You actually never saw the video?"
    er "No... I'm disgusted even thinking about it."
    mc "How do you know for sure that he really has a video if you didn't see it?"
    scene 07_546 with Dissolve(1)
    er "..."
    mc "Erynn, seriously. You are one of the smartest people I know. I'm sorry, but that's pretty dumb!"
    mc "For fuck's sake... You know he can't be trusted..."
    er "..."
    scene 07_547 with Dissolve(1)
    mc "So, now he uses the video to blackmail you into staying with that modelling agency?"
    er "No. He makes me do other things."
    mc "Like?"
    er "..."
    scene 07_548 with Dissolve(1)
    er "*Sigh*"
    er "I have to accompany shady clients to all kinds of events and provide 'entertainment'."
    mc "Like eye candy... You're basically an escort?"
    er "Yes, it's so degrading."
    mc "Do you have to... Sleep with them?"
    er "No. But that doesn't stop them from trying and touching me..."
    er "And the way things are going, it's just a matter of time before..."
    scene 07_549 with Dissolve(1)
    mc "Why didn't you go to the police and report it?"
    er "He can simply make it out to be a normal modelling job."
    mc "I meant the video."
    er "He can deny it. Or say he deleted it. I can't prove anything."
    er "And if that video ever leaks, I can say goodbye to my teaching career..."
    mc "Yeah, I can believe that. The educational department is really strict when it comes to those things."
    scene 07_550 with Dissolve(1)
    mc "But then, how long do you have to do this? He must want something..."
    er "..."
    er "He wants to have sex with me."
    mc "Bastard... What's wrong with this guy? I should've punched him more..."
    scene 07_551 with Dissolve(1)
    er "I don't know what do to anymore, [mc]. I want to stop. I can't do this anymore."
    menu:
        "Don't help[KoGa3AutoWTChange1]{size=-4}(Erynn Friends, Erynn Points-15, Alexis Points-10, Melissa Points-5, {i}Alexis FriendsFalse: Erynn Week3 Monday Alexis Mention{/i}) {/size} {/color}":
            $ Erynn_Friends = True
            $ Erynn_Points -= 15
            $ Alexis_Points -= 10
            $ Melissa_Points -= 5
            scene 07_552 with Dissolve(1)
            mc "I don't know either Erynn... I can't help you with that."
            mc "I'll be lucky if he doesn't report me for assault."
            er "I'm sorry."
            mc "I'm sorry this happened to you."
            scene 07_553 with Dissolve(1)
            mc "Thank you for trusting me and telling me this."
            mc "Does anyone else know?"
            er "No..."
            mc "Maybe talk to Zane? Maybe he can help?"
            er "..."
            scene 07_554 with Dissolve(1)
            mc "How are you feeling though? Better?"
            er "Yes. I'm happy I could talk to someone about this."
            mc "You'll figure it out Erynn."
            if Alexis_Friends == False:
                $ Erynn_Week3_Monday_Alexis_Mention = True
                scene 07_557 with Dissolve(1)
                mc "I need to tell you something too."
                er "Okay."
                scene 07_558 with Dissolve(1)
                mc "Alexis and I..."
                er "I know."
                mc "You do?"
                er "I saw a text message and the pictures on your phone. Are you dating her?"
                mc "I don't know what we are just yet. But I like her."
                er "..."
                scene 07_559 with Dissolve(1)
                er "You're actually her type."
                mc "I am?"
                er "When we talked about our types, she basically described you."
                mc "{i}(I thought she only said that to be flirty...){/i}"
                mc "But how are you feeling about that?"
                er "..."
                scene 07_560 with Dissolve(1)
                mc "Can't you guys talk it out? You've been friends for so long. You must miss each other."
                mc "You can't be mad at her for liking someone."
                er "I'm not. I'm angry that she lied to me. I was disappointed she didn't tell me, and it took me by surprise."
                er "She could have just told me and I would've been fine with it."
                mc "Yeah, it wasn't great the way it was handled. I gave her shit too, which wasn't nice, but we talked it out."
                mc "Maybe one day..."
                er "..."
                scene 07_561 with Dissolve(1)
                mc "We're good though, right?"
                er "Yes."
                mc "Good."
                scene 07_562 with Dissolve(1)
                mc "I guess I'm heading home, then."
                mc "Try to get some sleep, and if you need anything, call me, okay?"
                er "I will. Thank you, [mc]."
                scene 07_563 with Dissolve(1)
                mc "Sorry I can't do more."
                er "No... It's my fault. I should've never trusted Ethan, or even been friends with him to begin with."
                mc "You'll figure something out, Erynn. You always do. Don't let him win."
                er "..."
                scene 07_564 with Dissolve(1)
                mc "Good night, Erynn."
                er "Good night."
                jump Week3_Tuesday_School
            else:
                scene 07_562 with Dissolve(1)
                mc "I guess I'll be heading home then."
                mc "Try to get some sleep, and if you need anything, call me, okay?"
                er "I will. Thank you, [mc]."
                scene 07_563 with Dissolve(1)
                mc "Sorry I can't do more."
                er "No... It's my fault. I should've never trusted Ethan, or even been friends with him to begin with."
                mc "You'll figure something out, Erynn. You always do. Don't let him win."
                er "..."
                scene 07_564 with Dissolve(1)
                mc "Good night, Erynn."
                er "Good night."
                jump Week3_Tuesday_School
        "Help her[KoGa3AutoWTChange1]{size=-4}(Erynn Week3 Monday Blackmailhelp, Erynn Points+2) {/size} {/color}":
            $ Erynn_Week3_Monday_Blackmailhelp = True
            $ Erynn_Points += 2
            # Erynn (32)
            scene 07_554 with Dissolve(1)
            mc "I don't know either, Erynn... But we'll figure something out."
            mc "I'm here for you."
            er "Thank you."
            mc "Come here."
            scene 07_555 with Dissolve(1)
            mc "Thank you for trusting me and telling me this."
            er "Thank you for being here for me."
            if Erynn_Points >= 23:
                er "{i}(I'm so happy you're back.){/i}"
                scene 07_556 with Dissolve(1)
                er "..."
                mc "What?"
                scene 07_565 with Dissolve(1)
                mc "..."
                menu:
                    "Move away":
                        if Alexis_Friends == True:
                            scene 07_567 with Dissolve(1)
                            mc "Erynn. This isn't a good idea."
                            er "..."
                            scene 07_568 with Dissolve(1)
                            er "Sorry, you're right. It was just..."
                            mc "I know..."
                            scene 07_569 with Dissolve(1)
                            er "Can you stay over tonight, though? I don't want to be alone."
                            mc "Of course."
                            jump Week3_Monday_Erynn_StayOver
                        else:
                            scene 07_567 with Dissolve(1)
                            mc "Erynn, we can't."
                            menu:
                                "Mention Alexis[KoGa3AutoWTChange1]{size=-4}(Erynn Week3 Monday Alexis Mention) {/size} {/color}":
                                    $ Erynn_Week3_Monday_Alexis_Mention = True
                                    mc "I'm kinda seeing Alexis."
                                    er "Uhm... What?"
                                    mc "Yeah..."
                                    er "You're dating her?"
                                    scene 07_570 with Dissolve(1)
                                    mc "I don't know what we are just yet. But I like her."
                                    er "..."
                                    er "{i}(I like you too...){/i}"
                                    scene 07_559 with Dissolve(1)
                                    mc "Can't you guys talk it out? You've been friends for so long. You must miss each other."
                                    mc "You can't be mad at her for liking someone."
                                    er "I'm not. I'm angry that she lied to me."
                                    scene 07_560 with Dissolve(1)
                                    er "She should've told me when you met."
                                    mc "Yeah, it wasn't great the way it was handled. I gave her shit too, which wasn't nice, but we talked it out."
                                    er "I just don't know. I'm not in the right headspace at the moment."
                                    mc "I totally understand."
                                    scene black with Dissolve(2)
                                    pause 2
                                    scene 07_569 with Dissolve(1)
                                    mc "I guess I'll be heading home then."
                                    er "Can't you stay over? I don't want to be alone tonight."
                                    mc "Uhm... Sure."
                                    scene 07_564 with Dissolve(1)
                                    er "Thank you."
                                    jump Week3_Monday_Erynn_StayOver
                                "Don't mention Alexis":
                                    mc "Erynn. This isn't a good idea."
                                    er "..."
                                    scene 07_568 with Dissolve(1)
                                    er "Sorry, you're right. It was just..."
                                    mc "I know..."
                                    scene black with Dissolve(2)
                                    pause 2
                                    scene 07_569 with Dissolve(1)
                                    mc "I guess I'll be heading home then."
                                    er "Can't you stay over? I don't want to be alone tonight."
                                    mc "Uhm... Sure."
                                    scene 07_564 with Dissolve(1)
                                    er "Thank you."
                                    jump Week3_Monday_Erynn_StayOver
                    "Kiss her[KoGa3AutoWTChange1]{size=-4}(Erynn Week3 Monday Makeout) {/size} {/color}":
                        $ Erynn_Week3_Monday_Makeout = True
                        jump Week3_Tuesday_Erynn_Kiss
            else:
                $ Erynn_Friends = True
                if Alexis_Friends == False:
                    $ Erynn_Week3_Monday_Alexis_Mention = True
                    scene 07_557 with Dissolve(1)
                    mc "I need to tell you something, too."
                    er "Okay."
                    scene 07_558 with Dissolve(1)
                    mc "Alexis and I..."
                    er "I know."
                    mc "You do?"
                    er "I saw a text message and the pictures on your phone. Are you dating her?"
                    mc "I don't know what we are just yet. But I like her."
                    er "..."
                    scene 07_559 with Dissolve(1)
                    er "You're actually totally her type."
                    mc "I am?"
                    er "When we talked about our types, she basically described you."
                    mc "{i}(I thought she only said that to be flirty...){/i}"
                    mc "But how are you feeling about that?"
                    er "..."
                    scene 07_560 with Dissolve(1)
                    mc "Can't you guys talk it out? You've been friends for so long. You must miss each other."
                    mc "You can't be mad at her for liking someone."
                    er "I'm not. I'm angry that she lied to me. I was disappointed she didn't tell me, and it took me by surprise."
                    er "She could have just told me and I would've been fine with it."
                    mc "Yeah, it wasn't great the way it was handled. I gave her shit too, which wasn't nice, but we talked it out."
                    mc "Maybe one day..."
                    er "..."
                    scene 07_561 with Dissolve(1)
                    mc "We're good though, right?"
                    er "Yes."
                    mc "Good."
                    scene black with Dissolve(1)
                    pause 2
                    scene 07_569 with Dissolve(1)
                    mc "I guess I'll be heading home then."
                    er "Can't you stay over? I don't want to be alone tonight."
                    mc "Uhm... Sure."
                    scene 07_564 with Dissolve(1)
                    er "Thank you."
                    jump Week3_Monday_Erynn_StayOver
                else:
                    scene black with Dissolve(1)
                    pause 2
                    scene 07_569 with Dissolve(1)
                    mc "I guess I'll be heading home then."
                    er "Can't you stay over? I don't want to be alone tonight."
                    mc "Uhm... Sure."
                    scene 07_564 with Dissolve(1)
                    er "Thank you."
                    jump Week3_Monday_Erynn_StayOver

label Week3_Tuesday_Erynn_Kiss:
    if _in_replay:
        $ Erynn_Points = 26
    scene 07_566 with Dissolve(1)
    mc "{i}(I'm kissing Erynn... I'm actually kissing Erynn.){/i}"
    scene 07_571 with Dissolve(1)
    mc "{i}(I've wanted this for so long. And it's finally happening, after all these years...){/i}"
    scene 07_572 with Dissolve(1)
    ""
    scene 07_573 with Dissolve(1)
    er "Ah... [mc]..."
    scene 07_574 with Dissolve(1)
    mc "{i}(I want her. I want her so bad...){/i}"
    scene black with Dissolve(1)
    pause 2
    scene 07_575 with Dissolve(1)
    mc "{i}(This isn't a dream, right? Don't let this be a dream.){/i}"
    scene 07_576 with Dissolve(1)
    mc "{i}(She's so beautiful.){/i}"
    mc "{i}(I can't hold back any longer...){/i}"
    scene 07_577 with vpunch
    er "Ah..."
    er "*Heavy breathing*"
    scene 07_578 with Dissolve(1)
    er "Let's go to the bed."
    scene black with Dissolve(2)
    pause 2
    scene 07_579 with vpunch
    mc "{i}(We're actually gonna do it.){/i}"
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 07_580 at moveup
    pause 3
    ""
    scene 07_581 with Dissolve(1)
    mc "{i}(I want to keep kissing her. I can't get enough.){/i}"
    scene 07_582 with Dissolve(1)
    mc "Still the most beautiful eyes I've ever seen."
    er "Thank you."
    scene 07_583 with Dissolve(1)
    ""
    scene 07_584 with Dissolve(1)
    mc "{i}(She's so soft.){/i}"
    scene 07_585 with Dissolve(1)
    ""
    scene 07_586 with Dissolve(1)
    mc "{i}(And she tastes amazing...){/i}"
    scene 07_587 with Dissolve(1)
    ""
    scene 07_588 with Dissolve(1)
    mc "{i}(Wow. She's so wet.){/i}"
    scene 07_589 with Dissolve(1)
    er "Uh... [mc]?"
    scene 07_590 with Dissolve(1)
    ""
    scene 07_591 with Dissolve(1)
    er "..."
    scene 07_592 with Dissolve(1)
    mc "{i}(I can't wait much longer. She's making me so hard.){/i}"
    scene 07_593 with Dissolve(1)
    er "[mc] stop..."
    mc "What's wrong?"
    scene 07_594 with Dissolve(1)
    $ Erynn_Points -= 8
    er "Please stop. I... I can't do this."
    er "I'm sorry."
    mc "You don't have to be sorry. It's alright."
    mc "{i}(She's right. Maybe this wasn't the best thing to do after today's events.){/i}"
    scene black with Dissolve(2)
    pause 2
    scene 07_595 with Dissolve(1)
    mc "Are you okay?"
    er "Yeah... Sorry..."
    mc "You have nothing to apologise for."
    scene 07_596 with Dissolve(1)
    er "Can you stay with me, though? I don't want to be alone tonight."
    mc "Of course."
    scene 07_597 with Dissolve(1)
    mc "I won't be going anywhere this time."
    mc "I'm here for you."
    er "Thank you."
    scene 07_598 with Dissolve(1)
    mc "Let's try to get some sleep, yes?"
    er "Hmm."
    $ renpy.end_replay()
    jump Week3_Monday_Erynn_StayOver

label Week3_Monday_Erynn_StayOver:
    scene black with Dissolve(2)
    pause 2
    n "Tuesday, 06:12. Erynn's apartment."
    stop music fadeout 1.0
    play music ("Music/LoFi Indie 3.mp3", "Music/LoFi Indie 1.mp3", "Music/LoFi Indie 2.mp3") volume 0.2
    if Erynn_Points >= 23:
        scene 07_599 with Dissolve(1)
        mc "{i}(She looks so cute when she's sleeping.){/i}"
        mc "{i}(I guess I'll let her know I'm leaving. And I need to bring Mom the groceries.){/i}"
    else:
        scene 07_606 with Dissolve(1)
        mc "{i}(This damn couch...){/i}"
        mc "{i}(I guess I'll let her know I'm leaving. And I need to bring Mom the groceries.){/i}"
    scene 07_600 with Dissolve(1)
    mc "Hey, Erynn."
    er "..."
    scene 07_601 with Dissolve(1)
    mc "Erynn?"
    er "Ngggh... It's still early, [mc]..."
    mc "I know, sorry. But I need to go."
    scene 07_602 with Dissolve(1)
    er "What? Now?"
    mc "Yeah. I still need to bring the groceries home and get ready for school."
    scene 07_603 with Dissolve(1)
    er "Okay. Can you wait a minute? I'll get ready and I'll drive you."
    mc "Thank you, but it's fine. Just sleep a bit more."
    scene 07_604 with Dissolve(1)
    er "I'm awake now. I'll be really quick, just one minute."
    mc "Heh... Sure."
    scene 07_605 with Dissolve(1)
    er "Don't go anywhere."
    mc "I'll stay right here."
    scene black with Dissolve(1)
    pause 2
    scene 07_607 with Dissolve(1)
    er "Ready. See... I told you it will be quick."
    mc "I'm positively surprised."
    er "Haha."
    scene 07_608 with Dissolve(1)
    mc "Looks like we're about to do some running."
    er "We can go for a run, but I don't think I'll be able to keep up with you."
    mc "I can lower my pace to yours."
    er "Maybe another time."
    er "By the way. Do you like my hoodie? It's cute, right?"
    mc "Very cute. Looks comfortable."
    er "It is. Come on, let's go."
    scene black with Dissolve(1)
    pause 2
    scene 07_609 with Dissolve(1)
    mc "How are you feeling after what happened yesterday?"
    er "Better. Thank you for staying. It felt really good to talk to someone about it."
    mc "Of course."
    scene 07_610 with Dissolve(1)
    mc "Don't take this the wrong way but I still think you should talk to Melissa about this."
    er "I don't know. She always worries about me, and when she hears this... I... I just can't."
    mc "Or maybe talk to my mom?"
    er "..."
    scene 07_611 with Dissolve(1)
    mc "Erynn... I mean, I won't be able to be here all the time."
    mc "Take this week, for example. We have training camp and I won't be back until Sunday."
    mc "What if something happens again with Ethan?"
    scene 07_612 with Dissolve(1)
    er "I know... But... *Sigh* Let me think about it, okay? Can we keep it between us for now?"
    mc "..."
    mc "Sure."
    mc "{i}(I think this is affecting her much more than she's letting on...){/i}"
    scene 07_613 with Dissolve(1)
    er "So... Training camp. That will be fun, huh?"
    mc "..."
    mc "Yeah. Really stoked about it, actually."
    scene black with Dissolve(2)
    pause 2
    scene 07_614 with Dissolve(1)
    mc "Thank you for driving me. This was so much quicker."
    er "No problem. You help me, I help you, right?"
    scene 07_615 with Dissolve(1)
    mc "Are you hungry, or do you want something to drink? Coffee, tea?"
    er "I'm good, thanks."
    scene 07_616 with Dissolve(1)
    m "I knew I heard something."
    mc "Hey, Mom."
    scene 07_617 with Dissolve(1)
    er "Good morning, Emily. Did we wake you?"
    m "Good morning. No, no, don't worry, sweetheart."
    scene 07_618 with Dissolve(1)
    m "Why are you up so early?"
    mc "I had to bring the groceries you asked for."
    mc "I... forgot yesterday, sorry."
    scene 07_619 with Dissolve(1)
    er "It was my fault. I needed his help. That's why I'm here. I offered to drive him today."
    m "Thank you."
    scene 07_620 with Dissolve(1)
    m "Cappuccino, Erynn?"
    er "I'd love one, thank you."
    scene 07_621 with Dissolve(1)
    mc "What? When I offered, you declined."
    er "Sorry... But Emily makes the best cappuccino. Can't say no to that."
    m "Thanks!"
    scene 07_622 with Dissolve(1)
    er "Hehe."
    mc "Whatever..."
    mc "{i}(At least she's smiling today.){/i}"
    scene 07_623 with Dissolve(1)
    mc "I'm going to take a shower and get ready for school."
    mc "Enjoy your cappuccinos..."
    m "Thank you, we will."
    mc "..."
    scene 07_624 with Dissolve(1)
    m "How are you, Erynn?"
    er "Uhm... I'm good."
    m "Yeah?"
    er "..."
    m "You know, you can always talk to me. If you need anything or..."
    er "Thank you, Emily."
    scene black with Dissolve(1)
    pause 2
    scene 07_625 with Dissolve(1)
    mc "Oh... You're still here?"
    er "Yep."
    scene 07_626 with Dissolve(1)
    m "Let her enjoy her cappuccino. She's my guest and we're having a nice conversation."
    mc "Just thought she might have to get ready for classes too..."
    scene 07_627 with Dissolve(1)
    er "No classes in the morning today. Just two in the afternoon. So plenty of time."
    mc "Lucky you!"
    scene 07_628 with Dissolve(1)
    er "I can drive you to school later."
    mc "You don't have to. It isn't that far."
    er "I don't mind. Besides, I have plenty of time, like I said."
    mc "..."
    mc "{i}(Maybe she wants to keep busy and doesn't want to be alone after what happened yesterday?){/i}"
    mc "Okay, thanks."
    er "Cool."
    scene 07_629 with Dissolve(1)
    mc "I guess I have some more time then. I'll go play some video games. I'll come down when we have to go."
    er "Do you want me to make you some sandwiches for lunch?"
    mc "..."
    mc "We have a cafeteria at school."
    scene 07_630 with Dissolve(1)
    m "He can have one with Nutella, the others with cheese or meat."
    er "Haha."
    scene 07_631 with Dissolve(1)
    mc "*Sigh* You guys think you're so funny..."
    m "Don't you think?"
    mc "..."
    mc "{i}(I can play this game too.){/i}"
    mc "You know what? Yeah, make me those sandwiches. No Nutella!"
    er "Okay."
    scene black with Dissolve(1)
    pause 2
    scene 07_632 with Dissolve(1)
    mc "{i}(Heh? She's actually making me sandwiches...){/i}"
    mc "Hey. Ready to leave?"
    er "Uh... Yeah. Let me wrap this up."
    scene 07_633 with Dissolve(1)
    er "Is this enough?"
    mc "I was kidding about the sandwiches, you know?"
    er "Oh... You don't want them?"
    menu:
        "No[KoGa3AutoWTChange1]{size=-4}(Erynn Points-2) {/size} {/color}":
            $ Erynn_Points -= 2
            scene 07_633a with Dissolve(1)
            mc "I'll get something at the cafeteria."
            mc "Sorry for the trouble, I thought you knew I was joking."
            er "It's okay. I'll eat them later, then."
        "Eat them[KoGa3AutoWTChange1]{size=-4}(Erynn Week3 Tuesday Sandwich, Erynn Points+2) {/size} {/color}":
            $ Erynn_Week3_Tuesday_Sandwich = True
            $ Erynn_Points += 2
            # Erynn (34)
            scene 07_633b with Dissolve(1)
            mc "I'll eat them. They actually look delicious."
            mc "Thank you, Erynn."
            er "You're welcome."
    scene black with Dissolve(1)
    pause 2
    scene 07_634 with Dissolve(1)
    er "Where should I drop you off?"
    mc "There is fine, next to the entrance."
    scene 07_635 with Dissolve(1)
    er "Oh, they have parking spaces here, I'll just go there."
    mc "Uhm... That's the teachers' parking."
    er "I'm studying to become a teacher, so it's fine."
    mc "Uh-huh... Perfect logic."
    scene black with Dissolve(1)
    pause 2
    scene 07_636 with Dissolve(1)
    mc "Well, thank you for driving me."
    er "You're welcome. Want me to pick you up too?"
    mc "Haha no. You have classes too. Besides, I have plans already after school."
    er "Okay."
    mc "{i}(She really doesn't want to be alone...){/i}"
    scene 07_637 with Dissolve(1)
    mc "Hey Erynn, it'll be fine. We'll figure it out once I'm back from training camp."
    er "Thank you."
    mc "Maybe stay at Melissa's for a while?"
    er "Yeah, I might do that."
    scene 07_638 with Dissolve(1)
    mc "If you want to talk, you can always call me."
    er "When will you be back, exactly?"
    mc "Sunday, around noon, I think."
    er "Okay."
    mc "Bye Erynn."
    scene black with Dissolve(1)
    pause 2
    scene 07_639 with Dissolve(1)
    mc "Uhm... Are you escorting me to the door, or what's happening?"
    er "Haha. Are you embarrassed by that?"
    scene 07_640 with Dissolve(1)
    mc "Not at all. No man would be embarrassed by you walking next to him."
    er "Oh..."
    mc "He'd be a lot of other things though."
    er "Haha... Thanks, I guess."
    scene 07_641 with Dissolve(1)
    da "Look at that bombshell... Damn, she's hot."
    tj "Isn't that Erynn?"
    da "Who?"
    tj "She's a model."
    da "Really? Then what's she doing with that guy? Don't tell me they are together."
    scene 07_644 with Dissolve(1)
    mc "See them all watching you. They're asking themselves who this hot new teacher is."
    er "Why a teacher? I could still be a student... As a matter of fact, I am a student!"
    mc "Eh..."
    er "Besides, a teacher wearing this... I'd get fired my first day."
    if Erynn_Points >= 25:
        mc "True. Or promoted."
        scene 07_645 with Dissolve(1)
        er "Haha."
        er "Well, let's make them change their opinion."
        mc "What?"
        er "Teachers don't do this to their students."
        if Week2_Monday_Bar_Stay == False:
            scene 07_646 with Dissolve(1)
            mc "..."
        else:
            scene 07_646 with Dissolve(1)
            mc "{i}(There's one teacher who did...){/i}"
        scene 07_642 with Dissolve(1)
        da "That shit annoys me."
        to "Hey... Sup, Darryl."
        da "Bugger off, Tori."
        scene 07_643 with Dissolve(1)
        to "The fuck is your problem?"
        scene 07_647 with Dissolve(1)
        mc "Hey! Didn't you read the school rules? No PDA!"
        er "..."
    else:
        mc "True. Or promoted."
    scene 07_648 with Dissolve(1)
    er "Haha."
    er "Off you go. Have fun at school..."
    mc "Uhm... Okay. Bye, Erynn."
    er "Bye."
    scene black with Dissolve(1)
    pause 2
    scene 07_649 with Dissolve(1)
    er "..."
    scene black with Dissolve(1)
    pause 2
    scene 07_650 with Dissolve(1)
    mc "{i}(What's he smiling about?){/i}"
    scene 07_651 with Dissolve(1)
    z "Dude... Okay... Who was that just now, because she totally looked like Erynn."
    mc "Yeah, that was Erynn."
    z "Yeah, yeah, funny. I mean the model named Erynn."
    mc "That was her!"
    scene 07_652 with Dissolve(1)
    z "..."
    z "What? Stop fooling around."
    mc "I'm not..."
    scene 07_653 with Dissolve(1)
    z "You're telling me that was the actual Erynn? How would you even know her?"
    mc "I thought you knew her, too..."
    z "No, but I'd do everything to get to know her. She's like number one on my list."
    mc "{i}(Of course, he has a list.){/i}"
    mc "Well, I've known her my whole life, she was my neighbour back then. Did you guys never meet when you came over?"
    scene 07_654 with Dissolve(1)
    z "No... Not that I remember."
    z "I still feel like you're joking..."
    mc "We even met her at Heaven. Last time we were there with Layla and Elena. Ask them."
    scene 07_655 with Dissolve(1)
    z "What the fuck? How did I miss that? I remember everything from that night!"
    z "Where was I?"
    mc "Preoccupied with piggybacking Elena."
    scene 07_656 with Dissolve(1)
    z "ELENA!"
    z "See, that's why I hate her."
    z "She always gets in the way."
    scene 07_657 with Dissolve(1)
    el "The feeling is mutual!"
    mc "..."
    z "Shit!"
    scene 07_658 with Dissolve(1)
    z "Good morning, Elena. How are you? You look nice."
    el "..."
    mc "Hey."
    el "Hey, [mc]."
    scene 07_659 with Dissolve(1)
    z "Of course she ignores me now."
    z "Typical!"
    mc "..."
    scene 07_660 with Dissolve(1)
    z "Okay, back on topic. Erynn!"
    mc "How do you know Erynn, then?"
    z "It's not that I know her. I'm a fan."
    z "She's a model, I have tons of pictures of her."
    mc "Really?"
    z "Yeah, did I never send any of her to you?"
    mc "No..."
    scene 07_661 with Dissolve(1)
    z "Let me see."
    z "Here."
    scene 07_662 with Dissolve(1)
    z "This one is pretty tame."
    scene 07_662b with Dissolve(1)
    z "Here's a close-up."
    scene 07_662c with Dissolve(1)
    z "Look at that ass, so hot!"
    mc "..."
    scene 07_662d with Dissolve(1)
    z "This is one of my favourites."
    z "Erynn in a bikini."
    scene 07_662e with Dissolve(1)
    z "Look, when you zoom in, you see her hard nipples."
    z "Either it was very cold or she had lots of fun."
    mc "..."
    z "I masturbated so many times to this picture."
    mc "{i}(Shut the fuck up, Zach... Ever heard of TMI?){/i}"
    scene 07_663 with Dissolve(1)
    mc "Can I see for a second?"
    z "Haha. I knew you couldn't resist."
    scene 07_664 with Dissolve(1)
    mc "{i}(She looks really happy doing that.){/i}"
    mc "{i}(But that fucker Ethan ruined this for her!){/i}"
    scene 07_665 with Dissolve(1)
    mc "Where did you get all those pictures from?"
    z "From the modelling agency website. She has a portfolio there. Also online magazines she was in."
    z "Still can't believe you know her."
    z "Next time we go out, invite her, okay?"
    mc "Uhm... I'll ask her, but what about Valeria?"
    z "She doesn't have to know. There's enough Zach to go around."
    mc "..."
    scene 07_666 with Dissolve(1)
    z "Man... I'm so excited already!"
    mc "{i}(I guess I'll have to spell it out.){/i}"
    mc "Too much information."
    z "Haha, not like that. Well... Maybe."
    mc "Okay... I'm gonna go."
    scene 07_667 with Dissolve(1)
    z "See you later!"
    mc "Later, Zach."
    jump Week3_Tuesday_School

label Week3_Tuesday_School:
    scene black with Dissolve(2)
    pause 2
    stop music fadeout 1.0
    play music ("Music/LoFi Upbeat 1.mp3", "Music/LoFi Upbeat 2.mp3", "Music/LoFi Upbeat 3.mp3", "Music/LoFi Upbeat 4.mp3") volume 0.2
    scene 07_668 with Dissolve(1)
    n "Tuesday, 08:24. School."
    scene 07_669 with Dissolve(1)
    mc "..."
    if Layla_Points >= 39:
        menu:
            "Whistle":
                mc "*Whistle*"
                scene 07_670 with Dissolve(1)
                la "Okay, enough. We know it already."
                mc "..."
                scene 07_671 with Dissolve(1)
                la "Oh... Hey, [mc]."
                mc "Haha, what's with the different response?"
                el "You're like the tenth guy who's whistled at us."
                mc "I'm sorry."
            "Scare them":
                scene 07_672 with vpunch
                mc "Hey, lovely girls..."
                la "Aaah..."
                scene 07_673 with Dissolve(1)
                la "[mc]!"
                el "Seriously?"
                mc "Haha, sorry, sorry."
        mc "I see you actually went with the hotpants look today."
        scene black with Dissolve(1)
        transform moveup:
            xalign 0.5 yalign 1.0
            linear 5.0 yalign 0.0
        show 07_674 at moveup
        pause 3
        la "You like it?"
        menu:
            "Yes":
                mc "Muy bueno!"
                mc "Your bu... You look amazing."
                la "Thanks."
            "Skirts":
                mc "Eh... Honestly, I think I prefer skirts."
                mc "On girls... Just to be clear."
        scene 07_675 with Dissolve(1)
        el "Anyway. Where are your hot pants? Didn't we all agree to wear them today?"
        mc "Yeah, like that's gonna happen..."
        el "It's gonna happen one way or another."
        scene 07_676 with Dissolve(1)
        mc "Is that a threat?"
        el "Definitely!"
        mc "Haha. Let's see what you can come up with."
        el "You're so going to regret this."
    else:
        scene 07_671 with Dissolve(1)
        mc "Hey, good morning."
        la "Hey, [mc]."
        mc "Going for the hotpants look today?"
        scene black with Dissolve(1)
        transform moveup:
            xalign 0.5 yalign 1.0
            linear 5.0 yalign 0.0
        show 07_674 at moveup
        pause 3
        la "Yeah, you like it?"
        menu:
            "Yes":
                mc "I do..."
                mc "Your bu... You look amazing."
                la "Thanks."
            "Skirts":
                mc "Eh... Honestly, I think I prefer skirts."
                mc "On girls... Just to be clear."
    scene 07_677 with Dissolve(1)
    la "[mc], are we still on for this afternoon?"
    mc "The running? Of course."
    la "Cool. We can go where I usually run. It's not as busy as the park we've been to before."
    mc "Can you text me the address?"
    scene 07_678 with Dissolve(1)
    la "We can go together immediately after school."
    mc "I need to go home first and change. Didn't bring my gear with me."
    la "Ah okay. I'll text you."
    n "*School bell*"
    scene 07_679 with Dissolve(1)
    la "See you later then."
    el "Bye, [mc]."
    if Layla_Friends == True:
        mc "Bye."
    else:
        mc "Bye... Uhm... I mean sayonara..."
        scene 07_680 with Dissolve(1)
        la "Ha... Ha... Ha..."
        la "Now you're really going to regret what Elena has planned!"
        el "Haha."
    if Alexis_Friends == True:
        jump Week3_Tuesday_Layla_Park
    else:
        jump Week3_Tuesday_Afternoon

label Week3_Tuesday_Afternoon:
    scene black with Dissolve(2)
    pause 2
    n "Tuesday, 16:37. Home."
    scene 07_681 with Dissolve(1)
    mc "Seriously, where is my white tank..."
    play sound "Sounds/Phone_Vibrate.mp3"
    n "*Bzzzt. Bzzzt*"
    if Erynn_Week3_Monday_Help == False:
        $ Alexis_End = True
        $ Alexis_Friends = True
        stop music fadeout 1.0
        play music "Music/Battle_Rock2.mp3" volume 0.6
        scene 07_682 with Dissolve(1)
        mc "Hey Lexi. How are you?"
        a "..."
        scene 07_686 with Dissolve(1)
        a "Not good!"
        mc "What happened?"
        a "What happened? Seriously?"
        a "Erynn getting hit by Ethan and you just walked away? That happened!"
        scene 07_686 with Dissolve(1)
        mc "How do you..."
        a "Because she called me! Crying her eyes out."
        a "Do you have any idea how bad she must have felt that she had to call me of all people?"
        scene 07_687 with Dissolve(1)
        mc "I'm sorry. I just didn't know what to do."
        a "You're sorry? You're sorry?"
        scene 07_688 with Dissolve(1)
        a "Do you know what I'm not sorry about?"
        a "Calling you an asshole!"
        a "I didn't expect that from you!"
        scene 07_689 with Dissolve(1)
        mc "Lexi, I..."
        a "No! You don't get to call me Lexi. As a matter of fact, you don't get to call me at all, anymore."
        a "We are done!"
        scene 07_684 with Dissolve(1)
        mc "Lexi... Alexis."
        mc "..."
        scene 07_685 with Dissolve(1)
        mc "*Sigh*"
        mc "{i}(I fucked that up completely.){/i}"
        mc "{i}(Why didn't I help her?){/i}"
        mc "{i}(And now I don't really feel like running with Layla either...){/i}"
        mc "{i}(I'd better call her and cancel.){/i}"
        scene black with Dissolve(1)
        pause 2
        scene 07_683 with Dissolve(1)
        mc "Hey, Layla."
        la "Hey [mc]. What's up?"
        mc "Bad news. Something came up and I can't make it today. Sorry."
        la "*Sigh* Really?"
        la "It's fine, it happens. No problem. We have a whole week we can train together, right?"
        mc "Yeah."
        scene 07_697 with Dissolve(1)
        mc "..."
        mc "I need to get ready. See you tomorrow then."
        la "Alright. Bye, [mc]."
        mc "Bye, Layla. And sorry again..."
        scene 07_698 with Dissolve(1)
        mc "..."
        jump Episode_8_Start
    else:
        scene 07_682 with Dissolve(1)
        mc "Hey, Lexi. How are you?"
        a "Hi."
        scene 07_690 with Dissolve(1)
        a "..."
        mc "What? I can hear you smiling."
        a "Haha. Cause I am."
        mc "What makes you smile like that? Did something good happen?"
        a "You happened."
        scene 07_691 with Dissolve(1)
        mc "So corny! I think I have to hang up."
        a "Haha... No!"
        a "I miss you."
        mc "I miss you too."
        a "I want to see you. Can we meet up?"
        mc "We saw each other two days ago. Besides, wasn't it you who said to keep this on the down-low until Layla knows?"
        scene 07_692 with Dissolve(1)
        a "*Sigh* I know..."
        mc "We're going to training camp this week. I'll talk to her there."
        a "Okay. So you'll be gone the whole week then?"
        mc "Yeah, until Sunday."
        a "..."
        scene 07_693 with Dissolve(1)
        a "I really want to see you. I don't want to wait until Sunday."
        menu:
            "Meet Alexis[KoGa3AutoWTChange1]{size=-4}(Alexis Points+2, Layla Points-4) {/size} {/color}":
                $ Alexis_Points += 2
                # Alexis (36)
                $ Layla_Points -= 4
                mc "{i}(I really want to see her.){/i}"
                mc "Where are you now?"
                scene 07_694 with Dissolve(1)
                a "You're coming?"
                mc "Yeah."
                a "I'm at home at the moment, but I'm heading to my dorm. Just needed to grab some stuff."
                mc "Shall I come over?"
                a "No, we can meet in the city and go from there."
                mc "Sure."
                a "Six-thirty at Alba station?"
                mc "I'll be there."
                scene 07_695 with Dissolve(1)
                a "Great. See you later then."
                a "Bye, [mc]."
                mc "Bye, Lexi."
                scene 07_696 with Dissolve(1)
                mc "*Sigh* Now I have to call Layla and cancel..."
                mc "I hope she won't be too disappointed."
                scene black with Dissolve(1)
                pause 2
                scene 07_683 with Dissolve(1)
                mc "Hey, Layla."
                la "Hey, [mc]. What's up?"
                mc "Bad news. Something came up and I can't make it today. Sorry."
                la "*Sigh* Really?"
                la "It's fine, it happens. No problem. We have a whole week we can train together, right?"
                mc "Yeah."
                scene 07_697 with Dissolve(1)
                mc "..."
                mc "I need to get ready. See you tomorrow then."
                la "Alright. Bye, [mc]."
                mc "Bye, Layla. And sorry again..."
                scene 07_698 with Dissolve(1)
                mc "{i}(Why do I feel so bad about that?){/i}"
                scene black with Dissolve(1)
                pause 2
                scene 07_699 with Dissolve(1)
                la "Hey, Lexi."
                a "Oh hey, Lays."
                scene 07_700 with Dissolve(1)
                a "Going for a run?"
                la "*Sigh* No... I was about to but my friend had to cancel."
                la "What are you doing?"
                a "Just packing some stuff I'm taking to the dorm."
                scene 07_701 with Dissolve(1)
                la "You're not staying here anymore?"
                a "Just the weekends."
                la "I liked having you around more though..."
                a "Me too. I'll try to come home more often, okay?"
                scene 07_702 with Dissolve(1)
                la "Just tell Mom you don't like your roommate, and move back."
                a "Haha. Mom won't agree to that. Besides, Iris is cool."
                a "I'm not moving away, Layla. I'll be here whenever you need me."
                jump Week3_Tuesday_Alexis_Date
            "Train with Layla":
                mc "{i}(I want to see you too but I promised Layla I'd go running with her.){/i}"
                mc "Sorry, I can't today. I've made plans already."
                a "..."
                a "Then it will be Sunday, I guess?"
                scene 07_694 with Dissolve(1)
                mc "Yeah. I'll call you every day though, as compensation?"
                a "I'd like that."
                mc "Sorry, I have to keep this short. I need to get ready. I'll speak to you tomorrow, okay?"
                a "Don't forget!"
                mc "Hehe, I won't. Bye, Lexi."
                a "Bye, [mc]."
                scene 07_696 with Dissolve(1)
                mc "{i}(Sorry, Lexi... I really want to see you, but I made that promise already.){/i}"
                mc "{i}(*Sigh* Why do I feel bad about it though...){/i}"
                jump Week3_Tuesday_Layla_Park

label Week3_Tuesday_Layla_Park:
    $ Layla_Week3_Tuesday_Train = True
    scene black with Dissolve(1)
    pause 2
    stop music fadeout 1.0
    play music "Sounds/Park.mp3" volume 0.6
    n "Tuesday, 17:22. Horizon Park."
    scene 07_703 with Dissolve(1)
    mc "Hey there, Layla."
    scene 07_704 with Dissolve(1)
    la "Hey, [mc]."
    mc "What's with the bag? I thought you said running, not running away..."
    scene 07_705 with Dissolve(1)
    la "Very funny..."
    scene 07_706 with Dissolve(1)
    la "I actually brought water, bananas and protein bars."
    mc "Wow, this training session is more serious than I thought."
    la "Yeah, I also brought you a towel, so you can wipe your sweat, which you will do a lot of if you try to keep up."
    mc "Haha, thanks."
    scene 07_707 with Dissolve(1)
    mc "This is a nice park. Never been here before."
    la "It's relatively new and not as busy as Brighton Park."
    mc "Yeah, no one around."
    scene 07_708 with Dissolve(1)
    la "And the best thing about it. This straight right here from the entrance to the tree at the back is exactly a hundred meters."
    mc "Oh, that's perfect."
    la "Right?"
    scene 07_709 with Dissolve(1)
    mc "Okay, let's do this. Some warm-up laps first?"
    la "Exactly my thought."
    scene 07_710 with Dissolve(1)
    mc "{i}(I'm getting warm already.){/i}"
    scene 07_711 with Dissolve(1)
    mc "{i}(Oh? She's also taking her pants off?){/i}"
    if Layla_Points >= 39:
        scene 07_712 with Dissolve(1)
        mc "{i}(Damn...){/i}"
        scene 07_713 with Dissolve(1)
        mc "{i}(I absolutely love women's track clothes...){/i}"
    else:
        scene 07_712 with Dissolve(1)
        mc "{i}(Damn...){/i}"
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 07_714 at moveup
    pause 3
    la "Ready to go?"
    scene 07_715 with Dissolve(1)
    mc "When did you actually join the track team?"
    la "As a freshman."
    mc "And why track?"
    scene 07_716 with Dissolve(1)
    la "Well, I joined the cheerleading team first, together with Elena."
    la "Mostly because my mom was a cheerleader in high school and college."
    mc "Principal Moore a cheerleader? Who would've thought?"
    la "It's so funny you call my mom Principal Moore."
    mc "Well, yeah... I can't call her 'Mom' like you do."
    if Adriana_Points >= 2:
        la "Haha. Why don't you try it sometime? I really want to see her reaction."
        mc "{i}(Now I'm really curious what Adriana would look like in a cheerleading outfit){/i}"
        scene black with Dissolve(1)
        transform moveup:
            xalign 0.5 yalign 1.0
            linear 5.0 yalign 0.0
        show 07_717 at moveup
        pause 3
        mc "{i}(Something like that?){/i}"
        if Alexis_Friends == False:
            mc "{i}(Damn...){/i}"
            mc "{i}(What did she look like when she was younger? Like Alexis but with red hair?){/i}"
            scene 07_718 with Dissolve(1)
            mc "..."
            mc "{i}(I'm in trouble.){/i}"
        else:
            mc "{i}(Damn...){/i}"
        scene 07_719 with Dissolve(1)
        la "... my thing."
        mc "{i}(What did she say?){/i}"
    else:
        la "Haha. Why don't you try it sometime? I really want to see her reaction."
        scene 07_719 with Dissolve(1)
        la "Anyway, I quit after a few weeks. Cheerleading wasn't really my thing."
    scene 07_720 with Dissolve(1)
    la "Since this is a sports school, I had to choose a new team to join."
    la "I talked to my dad about different options. He was an athlete himself."
    mc "Yeah? What did he play?"
    scene 07_721 with Dissolve(1)
    la "He played basketball and did some running also. Oh, and football. But not the one you play with your feet."
    mc "American Football?"
    la "Yeah. But only in college. And nowadays, besides going for a run, he only watches sports. Marauders fan, of course."
    scene 07_722 with Dissolve(1)
    mc "Haha. Same here."
    la "Yeah?"
    mc "Uh-huh."
    la "Funny."
    scene 07_723 with Dissolve(1)
    la "He suggested I try track."
    la "I went to my first training and never looked back."
    scene black with Dissolve(1)
    pause 2
    scene 07_724 with Dissolve(1)
    mc "So, how are we doing this? One runs, and the other is at the finish line timing it?"
    la "Yeah. But we don't have to time every run. Maybe check the form, so we can improve?"
    mc "Sounds great."
    mc "How about you start?"
    la "Sure."
    scene 07_725 with Dissolve(1)
    mc "Oh-oh. Putting the hair up. Someone's getting serious here."
    la "That's right, haha."
    scene 07_726 with Dissolve(1)
    mc "Do you have any pre-run routines? Like that one girl who does the dancing, forgot her name."
    la "Haha, I know who you mean."
    show 07_727
    la "Like this!"
    mc "..."
    if Layla_Points >= 39:
        scene 07_728 with Dissolve(1)
        mc "That was actually pretty sexy."
        la "Haha, thanks."
    else:
        scene 07_728 with Dissolve(1)
        mc "Yeah, like that."
        la "Haha."
    scene 07_729 with Dissolve(1)
    mc "Okay, get ready girl. Show me what you've got."
    scene black with Dissolve(1)
    pause 2
    scene 07_730 with Dissolve(1)
    mc "Let's see. Clock, stopwatch. Here we go."
    scene 07_731 with Dissolve(1)
    mc "Are you ready, Layla?"
    la "Yes!"
    mc "Get in your starting position."
    scene 07_732 with Dissolve(1)
    mc "Ready!"
    scene 07_733 with Dissolve(1)
    mc "Set!"
    scene 07_734 with Dissolve(1)
    mc "GO!"
    scene black with Dissolve(1)
    pause 2
    scene 07_735 with Dissolve(1)
    n "*Beep*"
    scene 07_736 with Dissolve(1)
    mc "Damn Layla... 11.83 on your first run on this track... Street? Path? Whatever you wanna call it."
    la "What? Really?"
    scene 07_737 with Dissolve(1)
    mc "Yeah. That's impressive."
    la "Thanks. You sure you timed it correctly?"
    mc "I think so, yeah."
    mc "Maybe you should start doing that dance routine..."
    la "Haha. I just might."
    scene 07_738 with Dissolve(1)
    mc "Do you want to go again, or..."
    la "No, I'll take a quick breather. Your turn."
    scene black with Dissolve(1)
    pause 2
    scene 07_739 with Dissolve(1)
    mc "{i}(Concentrate... Concentrate.){/i}"
    la "GO!"
    scene black with Dissolve(1)
    pause 2
    scene 07_740 with Dissolve(1)
    la "10.67!"
    mc "..."
    scene 07_741 with Dissolve(1)
    la "You don't look happy about that."
    mc "I'm not, I messed up the start... Again. Seems like Tori was right after all."
    la "Don't let Tori get in your head."
    mc "Let me go again."
    scene black with Dissolve(1)
    pause 2
    scene 07_742 with Dissolve(1)
    mc "*Heavy breathing* How was that?"
    la "10.42!"
    mc "That's better already."
    la "Did you change something?"
    mc "Yeah, I slightly increased the pace of my first two steps."
    mc "Before it felt like I'd actually stumble and fall over."
    mc "Your turn."
    scene black with Dissolve(2)
    pause 2
    scene 07_743 with Dissolve(1)
    mc "So, our best times of the day were 10.37 and... 11.83, was it?"
    la "Yeah, my first run was actually my best."
    mc "I told you to do that dancing routine."
    la "Haha, yeah."
    scene 07_744 with Dissolve(1)
    mc "So, how is the competition at the training camp?"
    la "Pretty tough, actually. The bar is set high."
    mc "What place did you finish last year?"
    if Layla_Week2_Monday_LucasHelp == False:
        la "Sixth... Was not my best performance."
    else:
        la "Sixth... Was not my best performance."
        scene 07_745 with Dissolve(1)
        mc "{i}(Hmm... Maybe that Lucas fiasco had something to do with it.){/i}"
        mc "{i}(I'd better not bring that up right now. Besides, I haven't seen or heard anything from him in days...){/i}"
    scene 07_746 with Dissolve(1)
    mc "Out of how many?"
    la "Twenty."
    mc "Well, then sixth place is good."
    la "The margin to the top three was pretty big, though."
    scene 07_747 with Dissolve(1)
    la "I have an idea."
    mc "Tell me."
    la "Let's race. You against me!"
    menu:
        "Enough for today":
            scene 07_748 with Dissolve(1)
            mc "Honestly. I think we've done enough running for a day."
            mc "We'll have to save a bit for training camp."
            la "You're just scared you're going to lose to a girl."
            mc "That too..."
            la "I knew it. Next time we race, though!"
            mc "Deal."
            jump Week3_Tuesday_Layla_Park_End
        "Race her[KoGa3AutoWTChange1]{size=-4}(Layla Week3 Tuesday Race, Layla Points+2) {/size} {/color}":
            $ Layla_Week3_Tuesday_Race = True
            $ Layla_Points += 2
            # Layla (58)
            scene 07_749 with Dissolve(1)
            mc "Haha, you sure?"
            la "Yes."
            mc "Let's do this."
            scene 07_750 with Dissolve(1)
            la "There will be a slight condition change though."
            mc "Aha. Now it comes, I had a feeling there was a catch. What's that slight change?"
            la "I'll get a ten-meter head start."
            mc "Haha. No!"
            la "Scared you're going to lose?"
            scene 07_748 with Dissolve(1)
            mc "Not really."
            mc "Ten meters is unreasonable."
            mc "How about this. You get five meters and you can start whenever. Once I see you go, I go."
            la "..."
            la "Okay, I'll take that."
            scene 07_751 with Dissolve(1)
            mc "Show me what you've got, girl..."
            la "Haha, you sound so confident."
            scene black with Dissolve(1)
            pause 2
            scene 07_752 with Dissolve(1)
            la "Don't cheat!"
            mc "I won't. I'll start when I see you move."
            if Layla_Points >= 41:
                scene 07_753 with Dissolve(1)
                mc "{i}(She's really taking her time...){/i}"
                mc "{i}(What's she doing now?){/i}"
                menu:
                    "Check her out[KoGa3AutoWTChange1]{size=-4}(Layla Week3 Tuesday Race Win) {/size} {/color}":
                        $ Layla_Week3_Tuesday_Race_Win = True
                        scene 07_754 with Dissolve(1)
                        mc "..."
                        mc "{i}(She's doing that on purpose.){/i}"
                        scene 07_755 with Dissolve(1)
                        mc "{i}(Dammit, missed the start.){/i}"
                        scene 07_758 with Dissolve(1)
                        mc "{i}(Shit... I'm actually not going to catch her.){/i}"
                        scene 07_759 with Dissolve(1)
                        la "YAY!"
                        scene 07_764 with Dissolve(1)
                        la "Haha. Easy!"
                        mc "Easy? Ha... Ha... Cheater!"
                        la "What?"
                        mc "You know what I'm talking about. You distracted me."
                        scene 07_765 with Dissolve(1)
                        la "How so?"
                        mc "Wiggling your cute butt in front of me."
                        la "Haha. I did no such thing."
                        mc "Uh-huh..."
                        scene 07_766 with Dissolve(1)
                        la "Do you mean this?"
                        scene black with Dissolve(1)
                        transform moveup:
                            xalign 0.5 yalign 1.0
                            linear 5.0 yalign 0.0
                        show 07_767 at moveup
                        pause 3
                        mc "Exactly!"
                        la "Haha..."
                        scene 07_768 with Dissolve(1)
                        mc "Come here, you little tease."
                        la "Noooo..."
                    "Concentrate":
                        mc "{i}(It's not going to work, Layla.){/i}"
                        scene 07_756 with Dissolve(1)
                        ""
                        scene 07_757 with Dissolve(1)
                        la "{i}(Oh no...){/i}"
                        scene 07_760 with Dissolve(1)
                        mc "{i}(Close, but I won.){/i}"
                        scene 07_761 with Dissolve(1)
                        mc "And the crowd goes wild. He did it, against all odds..."
                        la "Pfff... I told you we should've made it ten meters... So unfair."
                        mc "Unfair... Haha. Loser!"
                        la "HEY!"
                        scene 07_762 with vpunch
                        la "AAAH!"
                        mc "Haha... What are you trying to do!"
                        la "Beat you up!"
                        scene 07_763 with Dissolve(1)
                        mc "Oh no... The ever so popular [mc] is getting attacked by a crazed fan..."
                        la "Popular... Fan... Yeah right!"
                        mc "Authorities! Where are the authorities?"
                jump Week3_Tuesday_Layla_Park2
            else:
                scene 07_756 with Dissolve(1)
                ""
                scene 07_757 with Dissolve(1)
                la "{i}(Oh no...){/i}"
                scene 07_760 with Dissolve(1)
                mc "{i}(Close, but I won.){/i}"
                scene 07_761 with Dissolve(1)
                mc "And the crowd goes wild. He did it, against all odds..."
                la "Pfff... I told you we should've made it ten meters... So unfair."
                mc "Unfair... Haha. Loser!"
                la "HEY!"
                jump Week3_Tuesday_Layla_Park_End

label Week3_Tuesday_Layla_Park2:
    scene 07_769 with vpunch
    la "Haha."
    mc "Haha."
    scene 07_770 with Dissolve(1)
    la "..."
    mc "You are awesome!"
    menu:
        "Kiss[KoGa3AutoWTChange1]{size=-4}(Layla Points+2) {/size} {/color}":
            $ Layla_Points += 2
            # Layla (60)
            scene 07_771 with Dissolve(1)
            ""
            scene black with Dissolve(1)
            pause 2
            scene 07_772 with Dissolve(1)
            la "Thank you for joining me today. We should do this more often."
            mc "The running or the making out?"
            la "..."
            scene 07_773 with Dissolve(1)
            la "Both! Maybe the latter a bit more."
            mc "Haha. I agree."
        "Lie down":
            scene black with Dissolve(1)
            pause 2
            scene 07_772 with Dissolve(1)
            la "Thank you for joining me today. We should do this more often."
            mc "I agree. Was really fun."
    scene 07_774 with Dissolve(1)
    mc "Ah... Shit!"
    la "What's up with you all of a sudden?"
    scene 07_775 with Dissolve(1)
    mc "I hate this..."
    la "Haha, what are you doing?"
    mc "When I'm sweaty and lie in the grass, I always get itchy."
    mc "So annoying."
    scene 07_776 with Dissolve(1)
    mc "Aaah..."
    la "Haha."
    mc "Don't laugh. This is serious."
    la "Haha."
    if Layla_Points >= 43:
        scene 07_777 with Dissolve(1)
        la "Come here, sit down. I'll rub your back for you."
        mc "Thank you."
        scene 07_778 with Dissolve(1)
        la "Is this okay?"
        mc "Yeah, you can actually use your nails."
        la "I don't want to scratch you..."
        mc "Don't worry about it."
        scene 07_779 with Dissolve(1)
        la "Better?"
        mc "Yes! This is amazing!"
        mc "I love back rubs."
        la "Hehe."
        scene black with Dissolve(1)
        pause 2
        scene 07_780 with Dissolve(1)
        la "That's enough for today."
        mc "Thank you, Layla."
        la "Uh-huh."
        mc "You want one too?"
        la "I'm good. But I'll collect someday."
        mc "Haha good. My list of favours is growing."
        la "You'd better start writing them down."
    else:
        pass
    jump Week3_Tuesday_Layla_Park_End

label Week3_Tuesday_Layla_Park_End:
    scene black with Dissolve(1)
    pause 2
    scene 07_781 with Dissolve(1)
    mc "Got everything?"
    la "Yeah. I have a banana left if you'd like?"
    mc "I'm good, thanks."
    scene 07_782 with Dissolve(1)
    mc "Do you know how long the bus ride is tomorrow?"
    la "A little over three hours."
    mc "Oh, it's that far away?"
    scene 07_783 with Dissolve(1)
    la "We can play some games to pass the time or you can try to sleep."
    mc "Sleeping on a bus with forty or so students? No... I'd like my face not to be a canvas."
    la "Haha... You're probably right."
    scene black with Dissolve(1)
    pause 2
    scene 07_784 with Dissolve(1)
    la "Thank you for walking me home."
    mc "You're welcome!"
    if Layla_Points >= 43:
        menu:
            "Hug":
                scene 07_785 with Dissolve(1)
                mc "See you tomorrow."
                la "Bye, [mc]."
            "Kiss on cheek":
                scene 07_786 with Dissolve(1)
                mc "See you tomorrow."
                la "Bye, [mc]."
            "Kiss":
                scene 07_787 with Dissolve(1)
                mc "See you tomorrow."
                la "Bye, [mc]."
        if Layla_Week3_Tuesday_Race_Win == True:
            scene black with Dissolve(2)
            pause 2
            scene 07_788 with Dissolve(1)
            n "*Bzzzt. Bzzzt*"
            scene 07_789 with Dissolve(1)
            mc "{i}(Message from Layla.){/i}"
            scene 07_790 with Dissolve(1)
            la "Here, this might make you feel better about losing to a girl."
            mc "Let's see."
            scene black with Dissolve(1)
            transform moveup:
                xalign 0.5 yalign 1.0
                linear 5.0 yalign 0.0
            show 07_791a at moveup
            pause 3
            mc "Oh damn..."
            scene 07_791 with Dissolve(1)
            mc "Strategically held phone..."
            mc "You're such a tease!"
            mc "{i}(I just showered... Fuck it...){/i}"
        else:
            pass
        jump Episode_8_Start
    else:
        scene 07_785 with Dissolve(1)
        mc "See you tomorrow."
        la "Bye, [mc]."
        jump Episode_8_Start

label Week3_Tuesday_Alexis_Date:
    $ Alexis_Week3_Tuesday_Date = True
    scene black with Dissolve(1)
    pause 2
    scene 07_792 with Dissolve(1)
    a "Haha."
    a "I miss you too."
    mc "..."
    mc "{i}(Who's she talking to?){/i}"
    a "Yeah, can't wait."
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 07_793 at moveup
    pause 3
    a "Hey."
    scene 07_794 with Dissolve(1)
    a "One second. It's my cousin."
    mc "Sure, take your time. Say hi to her for me."
    scene 07_795 with Dissolve(1)
    a "What? I wasn't talking to you."
    a "..."
    a "No, this weirdo started talking to me and said to say hi to you."
    mc "..."
    a "Haha, yeah."
    scene 07_796 with Dissolve(1)
    mc "Weirdo?"
    a "Haha."
    a "Stop!"
    a "Haha..."
    scene 07_797 with Dissolve(1)
    a "He started kissing me."
    a "..."
    a "No, I kinda like it."
    scene 07_798 with Dissolve(1)
    a "Sorry, I gotta go. I'll tell you next time."
    a "I'll call you tomorrow, okay?"
    a "..."
    a "No. Tomorrow!"
    a "..."
    a "I will."
    a "Bye-bye."
    scene 07_799 with Dissolve(1)
    a "Sorry."
    mc "No worries."
    mc "Hi!"
    a "Hey."
    scene 07_800 with Dissolve(1)
    ""
    scene 07_801 with Dissolve(1)
    a "How are you?"
    n "*Stomach rumbling*"
    scene 07_802 with Dissolve(1)
    mc "Uh..."
    a "Haha, hungry, I assume?"
    scene 07_803 with Dissolve(1)
    mc "I'm good. Our bus will be here any minute, anyway."
    a "..."
    scene 07_804 with Dissolve(1)
    a "Well, I'm hungry. Let's go eat something first. We can take the next bus."
    mc "{i}(Did I say something wrong?){/i}"
    mc "Sure."
    scene 07_805 with Dissolve(1)
    mc "Lexi, wait up. Are you angry at me?"
    a "..."
    scene 07_806 with Dissolve(1)
    a "No."
    mc "And you say I'm the weirdo..."
    a "Haha."
    mc "No wonder guys don't understand girls... You're all so confusing."
    a "Are we though?"
    mc "Totally!"
    scene 07_807 with Dissolve(1)
    mc "So, where do you want to go eat?"
    a "I don't know. You pick."
    scene 07_808 with Dissolve(1)
    mc "Well, I hope you like burgers, because that's where we're going."
    a "And here I was hoping you'd say your mom's restaurant..."
    mc "Tough luck."
    a "..."
    scene 07_809 with Dissolve(1)
    mc "If you really don't like burgers, we can go somewhere else."
    a "I don't mind. As I said, you can pick."
    scene 07_810 with Dissolve(1)
    mc "I'll take you on a proper date next time and then we can go eat there."
    a "*British accent* A proper date?"
    a "Haha."
    scene 07_811 with Dissolve(1)
    mc "Okay, never mind..."
    a "Nooo! I'm sorry."
    mc "..."
    a "It was so funny the way you said it. I couldn't help it."
    scene 07_812 with Dissolve(1)
    a "[mc]!"
    a "Please..."
    mc "{i}(Why does this always work?){/i}"
    mc "*Sigh*"
    scene 07_813 with Dissolve(1)
    a "Hehe..."
    scene black with Dissolve(2)
    pause 2
    scene 07_814 with Dissolve(1)
    mc "That's a strange combination. A frappé and a turkey wrap."
    a "Is it? It's basically a cold coffee."
    mc "Hmm... You have enough with that?"
    a "Yeah."
    scene 07_815 with Dissolve(1)
    mc "We can share the fries. I'm not going to finish them by myself anyway."
    a "Thank you."
    if Erynn_Week3_Monday_Alexis_Mention == True:
        scene 07_816 with Dissolve(1)
        mc "I talked to Erynn about us."
        a "Oh? You did? What did she say?"
        scene 07_817 with Dissolve(1)
        mc "I think she's fine with it. She's mad because..."
        a "Because I lied and kept it from her."
        mc "Yeah."
        scene 07_818 with Dissolve(1)
        a "I tried to contact her, but she doesn't want to talk."
        mc "I asked her, too. She's hurt and needs some time."
        a "I hope she'll forgive me one day. I miss her so much."
        mc "She misses you too, she just doesn't want to admit it."
    else:
        pass
    mc "{i}(Shall I ask Alexis about Ethan?){/i}"
    menu:
        "Ask her":
            scene 07_819 with Dissolve(1)
            mc "I was at Erynn's yesterday."
            mc "By the way. Do you know what's going on between her and Ethan? Did she tell you anything?"
            a "I know that they meet sometimes. They aren't together or anything, she would've told me. Besides, she can't stand the guy."
            a "So I don't even know why she hangs around with him."
            a "Back in high school, he..."
            mc "He made your lives miserable. She told me."
            scene 07_820 with Dissolve(1)
            a "I hate that guy."
            mc "I don't like to bring this up, but Erynn mentioned that Ethan tried to break your friendship by telling her you slept with him."
            a "I would never sleep with that guy! He disgusts me..."
            mc "No, I believe you."
            scene 07_821 with Dissolve(1)
            a "Why would she bring that up? Does Erynn think..."
            a "Oh my god... This is all my fault. Why was I so stupid and lying to her."
            a "Now she thinks I lied about that..."
            mc "I'm sorry to bring the mood down with this."
            a "No, I'm sorry."
            scene 07_822 with Dissolve(1)
            a "I'm happy we can talk about this so openly, I should've done the same with Erynn."
            mc "Anyway, let's forget about it and start eating before it's completely cold."
        "Leave it be":
            mc "{i}(No, I trust her.){/i}"
    jump Week3_Tuesday_Alexis_Date_Wrap

label Week3_Tuesday_Alexis_Date_Wrap:
    scene black with Dissolve(1)
    pause 2
    scene 07_823 with Dissolve(1)
    mc "How's your turkey wrap? Is it good?"
    a "It's alright."
    mc "Never had that before."
    a "No?"
    scene 07_824 with Dissolve(1)
    a "Here, try it."
    scene 07_825 with Dissolve(1)
    a "..."
    a "Uh?"
    scene 07_826 with Dissolve(1)
    a "I said to try it..."
    mc "Mmm? Hai mhonly tais hit."
    scene 07_827 with Dissolve(1)
    a "Haha. I didn't understand a single word."
    mc "I said, I only tasted it."
    a "Uh-huh... You just tasted half my wrap."
    scene black with Dissolve(1)
    pause 2
    scene 07_828 with Dissolve(1)
    a "..."
    mc "..."
    scene 07_829 with Dissolve(1)
    mc "Okay, what?"
    a "Nothing."
    mc "My mom does the same thing. She stares while I'm eating and when I ask why, it's always nothing..."
    mc "Do I eat funny or something?"
    scene 07_830 with Dissolve(1)
    a "No."
    mc "Then please enlighten me. Why?"
    a "Maybe it's because we like the person we look at..."
    mc "..."
    a "I can stop, if it makes you that uncomfortable."
    a "{i}(But I'd rather not.){/i}"
    mc "It's not that. It was just... I don't know."
    scene 07_831 with Dissolve(1)
    mc "How do you feel when I stare at you like this?"
    a "I really like it, to be honest. It somewhat turns me on."
    mc "..."
    scene 07_832 with Dissolve(1)
    mc "What if I told you that I can look inside your top when you lean in like that?"
    a "Look all you want. Maybe I did that on purpose."
    scene 07_833 with Dissolve(1)
    a "..."
    mc "Alexis!"
    scene 07_834 with Dissolve(1)
    a "Haha..."
    mc "You're crazy. In a sexy kinda way..."
    scene black with Dissolve(1)
    pause 2
    scene 07_835 with Dissolve(1)
    a "Let's get outta here."
    mc "Yes!"
    $ renpy.end_replay()
    jump Week3_Tuesday_Alexis_Date_Iris

label Week3_Tuesday_Alexis_Date_Iris:
    scene black with Dissolve(1)
    pause 2
    scene 07_836 with Dissolve(1)
    mc "Yeah. And then a few days later, I find out that the principal is actually your and Layla's mom."
    a "The week of revelations."
    mc "Absolutely."
    scene 07_837 with Dissolve(1)
    a "This is my room."
    mc "I hope you cleaned beforehand."
    a "I haven't been here myself for a while."
    scene 07_838 with vpunch
    a "Ah!"
    scene 07_839 with Dissolve(1)
    ir "Oh hey, Lexi."
    scene 07_840 with vpunch
    a "Please wait outside for a minute."
    mc "Uh? What's going on?"
    a "I'll tell you later."
    scene 07_841 with Dissolve(1)
    a "Hey, Iris. What are you doing here?"
    ir "Dancing..."
    a "I meant why are you here? Didn't you say you'll be gone for another week?"
    ir "Yeah, I decided to come back earlier."
    scene 07_842 with Dissolve(1)
    ir "Don't I get a hug?"
    a "You're naked and your hair is wet."
    ir "Well yeah, I just came out of the shower. Besides, it wouldn't be the first time."
    scene 07_843 with Dissolve(1)
    a "..."
    scene 07_844 with Dissolve(1)
    a "What are you doing?"
    ir "Haha sorry. I always wanted to check something."
    a "..."
    ir "Not even a little?"
    a "No!"
    scene 07_845 with Dissolve(1)
    ir "If you ever change your mind..."
    a "..."
    a "What is up with you? Did something happen?"
    ir "Not really. Just met someone I thought I'd never see again."
    a "Okay?"
    scene 07_846 with Dissolve(1)
    ir "Oh, by the way. Who was that at the door? Am I messing up your plans? Do you need the room for some... You know?"
    a "..."
    ir "Hmm..."
    ir "Is he still waiting outside?"
    a "Yes."
    ir "Let him in."
    a "No."
    ir "Are you embarrassed? Haven't you told him about me?"
    a "Not yet."
    scene 07_847 with Dissolve(1)
    ir "Who is he? A hookup?"
    ir "No! It's more than just a hookup. You like him."
    ir "You'd better introduce me next time. I want to meet the guy who makes you smile like this."
    scene 07_848 with Dissolve(1)
    ir "Just give me a few minutes and you can have the room."
    a "It's fine. Stay. We'll do something else."
    ir "No, I don't want to clam jam you."
    a "I said it's fine, Iris."
    ir "Lexi..."
    scene 07_849 with Dissolve(1)
    a "See you later."
    ir "*Sigh*"
    ir "Bye-bye. Have fun. And sorry..."
    ir "Oh, and let's go out tomorrow and catch up."
    a "Sure."
    $ renpy.end_replay()
    jump Week3_Tuesday_Alexis_Date_MC

label Week3_Tuesday_Alexis_Date_MC:
    if _in_replay:
        $ SexCounter_Alexis = 5
        $ MC_SexCounter = 5
    $ SexCounter_Alexis += 1
    $ MC_SexCounter += 1
    $ Alexis_Week3_Tuesday_LexySexySong = True
    scene black with Dissolve(1)
    pause 2
    scene 07_850 with Dissolve(1)
    a "I'm sorry."
    mc "It's okay."
    a "My roommate is here. I thought she would be gone for another week."
    scene 07_851 with Dissolve(1)
    mc "Next time then. Or maybe she wants to watch?"
    a "Haha. I honestly think she wouldn't say no to that."
    mc "Really?"
    scene 07_852 with Dissolve(1)
    a "Stop imagining it. It's not going to happen!"
    mc "Haha. I'm not."
    a "Uh-huh..."
    scene 07_853 with Dissolve(1)
    mc "Let's go to my place."
    a "After your wild imagination just now... No!"
    scene 07_854 with vpunch
    a "Aaah!"
    scene 07_855 with Dissolve(1)
    mc "That wasn't up for debate!"
    a "It wasn't?"
    mc "Let's go."
    scene 07_856 with Dissolve(1)
    ""
    scene black with Dissolve(1)
    pause 2
    scene 07_857 with Dissolve(1)
    a "Still clean I see."
    mc "Well, you told me to keep it that way or else you wouldn't come over."
    a "Hehe."
    scene 07_858 with Dissolve(1)
    mc "Wait a minute. Is that the real reason why you didn't let me see your dorm?"
    a "What?"
    scene 07_859 with Dissolve(1)
    mc "There was no roommate. It was probably just a mess in there. Like clothes everywhere..."
    a "Oh totally. You got me."
    mc "I knew it!"
    scene 07_860 with Dissolve(1)
    a "And your bed is so much bigger. I just have a single."
    mc "Well, then we just have to snuggle up closer, which isn't bad."
    a "Also true."
    scene 07_861 with Dissolve(1)
    a "Oh?"
    a "I almost forgot. You have a guitar."
    scene 07_862 with Dissolve(1)
    a "Can I?"
    mc "Go ahead."
    scene 07_863 with Dissolve(1)
    a "How do I look?"
    mc "Total rockstar!"
    a "Haha. Thanks."
    mc "Let me take a picture. Pose for your first album cover."
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 07_864 at moveup
    pause 3
    mc "The rocker look really suits you!"
    scene 07_865 with Dissolve(1)
    mc "Now play me a song, Lexi Monroe."
    a "I can't play. I wish I could."
    scene 07_866 with Dissolve(1)
    a "But you can. How about you play a song?"
    mc "Eh... I don't know about that."
    a "You promised me last time."
    mc "Did I?"
    scene black with Dissolve(1)
    pause 2
    scene 07_867 with Dissolve(1)
    mc "*Sigh* I'm not that good."
    a "I don't believe that."
    mc "Don't be shocked, I warned you. Ready?"
    a "I'm really excited, actually."
    scene 07_868 with Dissolve(1)
    mc "*Sings* Oh Lexi, you are so se..."
    a "NO!"
    a "Sing a real song."
    mc "That's a real song."
    a "You know what I mean."
    scene 07_869 with Dissolve(1)
    mc "What do you want me to play?"
    a "Have you written a song?"
    scene 07_870 with Dissolve(1)
    mc "I have, but I don't think it's a good idea."
    a "No, please play that one. I really want to hear it."
    a "Please?"
    mc "{i}(I hope this doesn't backfire.){/i}"
    scene 07_871 with Dissolve(1)
    mc "*Sings* We used to walk on sunlight, hands in each other's dreams."
    mc "*Sings* But the storm came crashing, tore apart the woven seams."
    mc "*Sings* The silence grew between us, like a canyon wide and strong."
    mc "*Sings* We lost the map to find us, but time still hums our song."
    scene 07_872 with Dissolve(1)
    mc "*Sings* Tied by threads we can't escape, though years have drawn their line."
    mc "*Sings* The roads we took have bent and broke, yet here we intertwine."
    mc "*Sings* Your face still tells the story, your eyes still hold the truth."
    mc "*Sings* A spark that once was broken, now glows to light our youth..."
    scene black with Dissolve(1)
    pause 2
    scene 07_873 with Dissolve(1)
    mc "*Sings* Now glows to light our youth..."
    scene 07_874 with Dissolve(1)
    a "Liar!"
    mc "What?"
    a "You can actually play. And sing!"
    mc "Thanks."
    a "That was about Erynn, right?"
    mc "Yeah. Sorry..."
    a "No, don't be sorry. It was beautiful! Thank you for letting me listen to it."
    a "Can you play me another one?"
    scene black with Dissolve(1)
    pause 2
    scene 07_875 with Dissolve(1)
    a "I wish I knew how to play the guitar."
    mc "You can always learn."
    a "Only if you teach me!"
    mc "I'm not that good, but I think I can show you the basic chords."
    a "I'd love that."
    scene 07_876 with Dissolve(1)
    mc "Here, you take the guitar."
    a "Wait, let me get in the zone first."
    scene 07_877 with Dissolve(1)
    mc "{i}(In the zone...){/i}"
    scene 07_878 with Dissolve(1)
    mc "Are you doing that on purpose, too?"
    a "Doing what?"
    mc "Never mind."
    scene black with Dissolve(1)
    pause 2
    scene 07_879 with Dissolve(1)
    a "How do you even hold this properly?"
    mc "You held it good the first time."
    mc "I'll make it easier for you though. One second."
    mc "Let me put the strap on."
    scene 07_880 with Dissolve(1)
    a "Phrasing... Do you remember?"
    mc "I realised the moment I said it."
    a "Haha."
    mc "Damn it."
    scene 07_881 with Dissolve(1)
    a "Maybe Dylan was right after all..."
    a "Hahaha."
    mc "You think you're so funny."
    scene 07_882 with Dissolve(1)
    mc "You'd better put that guitar down and start running, girl!"
    a "What about my free guitar lessons?"
    mc "Hah... Free? You know what's free?"
    a "Tell me?"
    scene 07_883 with Dissolve(1)
    mc "One..."
    a "Why are you counting? I've put the guitar down."
    mc "Two..."
    a "[mc], stop!"
    scene 07_884 with Dissolve(1)
    mc "Three!"
    a "Aaah!"
    scene 07_885 with Dissolve(1)
    mc "Haha. What was that scream?"
    a "Haha. I tried."
    scene 07_886 with Dissolve(1)
    mc "I know you can scream better than that."
    a "Make me!"
    scene 07_887 with vpunch
    a "Haha."
    scene black with Dissolve(1)
    pause 2
    scene 07_888 with Dissolve(1)
    ""
    scene 07_889 with Dissolve(1)
    mc "{i}(It hasn't been that long since last I saw her naked, but somehow it excites me more and more.){/i}"
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 07_889a at moveup
    pause 3
    mc "{i}(She's so freakin' gorgeous. The way she softly bites her lower lip with that hint of a smile is so cute.){/i}"
    mc "{i}(I want to touch her, feel her, smell her, lick her... Just... everything.){/i}"
    scene 07_890 with Dissolve(1)
    mc "Come here!"
    scene 07_891 with Dissolve(1)
    a "A-ah..."
    mc "{i}(I love sucking her puffy nipples.){/i}"
    scene 07_892 with Dissolve(1)
    mc "{i}(Somehow it feels as if they're swelling even bigger in my mouth.){/i}"
    scene black with Dissolve(2)
    pause 2
    scene 07_893 with Dissolve(1)
    mc "{i}(Let's turn her around and get rid of those pants.){/i}"
    scene 07_894 with vpunch
    a "Aaah..."
    a "{i}(That took me by surprise, but it turns me on so much when he takes control...){/i}"
    scene 07_895 with Dissolve(1)
    mc "Even though your ass looks amazing in these pants, they're in the way and need to go!"
    a "Do whatever you need to."
    scene black with Dissolve(1)
    pause 2
    scene 07_896 with Dissolve(1)
    mc "Oh... Sexy lingerie. Did you plan this?"
    a "Maaaybe."
    mc "Hehe..."
    scene 07_897 with Dissolve(1)
    mc "{i}(The fabric is so thin but soft. This turns me on so much.){/i}"
    mc "{i}(I'd love to fuck her ass one day.){/i}"
    scene black with Dissolve(2)
    pause 2
    scene 07_898 with Dissolve(1)
    a "Yeah, strip for me! I really enjoy this part."
    mc "You'll enjoy the next part even more!"
    scene 07_899 with Dissolve(1)
    a "I'm sure I will."
    scene black with Dissolve(1)
    pause 2
    scene 07_900 with Dissolve(1)
    a "*Softly moaning*"
    mc "{i}(Her panties are so wet already.){/i}"
    scene 07_901 with Dissolve(1)
    ""
    scene 07_902 with Dissolve(1)
    mc "{i}(Either she's ticklish, or she's very sensitive down here.){/i}"
    scene 07_903 with Dissolve(1)
    a "Haah..."
    mc "{i}(She tastes so sweet.){/i}"
    scene black with Dissolve(1)
    pause 2
    scene 07_904 with Dissolve(1)
    ""
    scene 07_906 with Dissolve(1)
    a "Ah... Keep going [mc]!"
    scene 07_907 with Dissolve(1)
    a "*Moaning*"
    a "A-ah... Fuck!"
    scene 07_905 with Dissolve(1)
    a "*Heavy breathing*"
    a "That was... That wa... Haah... [mc]..."
    scene black with Dissolve(1)
    pause 2
    scene 07_908 with Dissolve(1)
    mc "Did you enjoy that?"
    a "*Nods*"
    scene 07_909 with Dissolve(1)
    ""
    scene 07_910 with Dissolve(1)
    a "{i}(I've never done this before, but I'll try.){/i}"
    mc "{i}(Is she going to give me a blowjob? That's new...){/i}"
    scene 07_911 with Dissolve(1)
    mc "{i}(My dick feels so good in her hands.){/i}"
    a "{i}(It's so warm.){/i}"
    scene 07_912 with Dissolve(1)
    a "{i}(This is the first time I've tasted it. It's salty, maybe?){/i}"
    scene 07_913 with Dissolve(1)
    mc "Fuck yes!"
    scene 07_914 with Dissolve(1)
    mc "Oh my... Lexi..."
    mc "Keep going."
    scene black with Dissolve(1)
    pause 2
    scene 07_915 with Dissolve(1)
    a "What's with you and my butt today?"
    mc "I don't know... I couldn't keep my eyes off it the whole day and now I just want to..."
    scene 07_916 with Dissolve(1)
    a "..."
    scene black with Dissolve(1)
    pause 2
    scene 07_917 with Dissolve(1)
    mc "{i}(I love this pussy. It's so tight.){/i}"
    scene 07_918 with Dissolve(1)
    a "Ah [mc], slowly..."
    scene 07_919 with vpunch
    a "AAAH!"
    mc "See, that scream is more like it."
    a "Fuck you. Aw... I said slowly."
    mc "Haha... Sorry."
    scene 07_921 with Dissolve(1)
    mc "Are you okay?"
    a "Shut up and keep going."
    mc "{i}(I knew she likes it...){/i}"
    scene 07_920 with Dissolve(1)
    a "*Moaning*"
    scene black with Dissolve(1)
    pause 2
    scene 07_922 with Dissolve(1)
    mc "{i}(She keeps on twitching whenever I touch her down here.){/i}"
    scene 07_923 with Dissolve(1)
    a "{i}(Yes [mc], fuck me! Fuck me harder!){/i}"
    scene 07_924 with Dissolve(1)
    a "*Heavy moaning*"
    scene 07_925 with Dissolve(1)
    mc "Lexi, I'm cuming."
    a "Cum inside me!"
    scene 07_926 with vpunch
    pause 2
    scene 07_926 with vpunch
    mc "Aah... Haah..."
    a "Mmm-hmm..."
    mc "{i}(She came again?){/i}"
    scene black with Dissolve(1)
    pause 2
    scene 07_927 with Dissolve(1)
    mc "*Heavy breathing*"
    a "Haha. You sound exhausted."
    mc "I am."
    a "I thought you were an athlete."
    mc "I am. Didn't you witness my world-class performance?"
    a "Haha. Not only did I witness it, I felt it! It was amazing."
    a "{i}(But there is one more thing...){/i}"
    scene 07_928 with Dissolve(1)
    a "*Bite*"
    mc "AAAH LEXI! LEXI STOP! LEXI!"
    scene 07_929 with Dissolve(1)
    mc "What the fuck, Alexis!"
    mc "What was that for? That hurt, you know?"
    a "See! I can make you scream, too!"
    mc "*Sigh*"
    scene 07_930 with Dissolve(1)
    a "Did I really hurt you?"
    mc "Yes, but it's fine. You're forgiven."
    a "Sorry..."
    scene 07_931 with Dissolve(1)
    mc "Will I become a vampire now?"
    a "Haha. I hope not."
    a "I don't want you to burst into flames when we go to the beach."
    mc "{i}(She's planning a beach date already? Can't wait!){/i}"
    mc "I won't burst into flames... I'll sparkle."
    a "Haha. Oh please, no!"
    mc "Haha."
    scene 07_932 with Dissolve(1)
    mc "Want to stay the night?"
    a "Yes!"
    mc "Good."
    mc "Now I have plenty of time to do this..."
    a "Hmm?"
    scene 07_933 with Dissolve(1)
    a "Aaah!"
    $ renpy.end_replay()
    if Erynn_Week3_Monday_Blackmailhelp == False:
        pass
    else:
        scene black with Dissolve(2)
        pause 2
        n "Wednesday, 07:37. Melissa's house."
        scene 07_934 with Dissolve(1)
        er "Morning, Mom."
        me "Hey, morning. Could you sleep in your old bed?"
        er "Yeah, I slept really well."
        scene 07_935 with Dissolve(1)
        me "Are you going somewhere this early?"
        er "Yes, next door. Giving [mc] a ride to school. So he doesn't have to walk the whole way with his backpack."
        er "He'll be going to training camp until Sunday."
        me "That sounds like fun."
        scene 07_936 with Dissolve(1)
        er "For him, yes. I'm going to be bored in the meantime."
        me "... You have other friends. Where's Alexis? Haven't seen her for quite some time."
        er "..."
        er "She's busy."
        me "Invite her over sometime. She's so much fun."
        er "..."
        scene 07_937 with Dissolve(1)
        er "Well, I have to go now."
        me "See you later. Oh, and can you tell Emily I'll come over for breakfast?"
        er "Will do. Bye, Mom."
        me "Bye-bye."
    jump Episode_8_Start

# Max Points:

# Alexis (36)
# Melissa (14)
# Layla (60)
# Elena (20)
# Emily (14)
# Erynn (34)
# Tori (2)
# Cara (16)
# Nikki (20)
# Lakeyn (6)
# Brooke (4)
# Adriana (4)
# Naomi (2)

# MC_GoodStudent (14)

# Nikki_Weekend (10)
# Cara_Weekend (6)

# MC_Sex (16)
# Alexis_Sex (6)
# Tori_Sex (1)
# Lakeyn_Sex (1)
# Nikki_Sex (3)
# Cara_Sex (3)
# Julia_Sex (1)
# Rachel_Sex (1)

#WTAdded
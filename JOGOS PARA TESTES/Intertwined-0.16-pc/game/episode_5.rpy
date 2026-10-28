label Episode_5_Start:

    #KoGa3 START#
    $ KoGa3GameProgress = "Ep5"
    #KoGa3 END#

    $ achievement.grant("ACHIEVEMENT_EPISODE_4")
    $ achievement.sync()
    $ Layla_Week2_Detention = False
    $ Adriana_Week2_Monday_TestBack = False
    $ Mike_Week2_Monday_Surname = False
    $ Adriana_Week2_Monday_Truth = False
    $ Layla_Week2_Monday_Wait = False
    $ Layla_Week2_Monday_LucasHelp = False
    $ Week2_Monday_Erynn_Help = False
    $ Week2_Monday_Erynn_Hair = False
    $ Melissa_Week2_Monday_Milf = False
    $ Week2_Monday_Erynn_Ethan = False
    $ Erynn_Week2_Monday_GoToErynn = False
    $ Week2_Monday_Bar_Stay = False
    $ Zach_Week2_Monday_House = False
    $ Zach_Week2_Monday_Sister = False
    $ Gabi_End = False
    $ Erynn_Week2_Monday_Bed = False
    $ Cara_Week2_Tuesday_Phonecall = False
    $ Nikki_Week2_Tuesday_Phonecall = False
    $ Erynn_Week2_Tuesday_Shirt = False
    $ Natasha_Week2_Tuesday_MikeSex = False
    $ Layla_Week2_Tuesday_Lie = False
    $ Layla_Week2_Tuesday_Sergeant = False
    $ Gabi_Week2_Tuesday_Pullout = False
    $ Elena_Week2_Tuesday_CheerHot = False
    $ Elena_Week2_Tuesday_RecruitJoke = False
    $ Erynn_Week2_Tuesday_CorrectHer = False
    $ Erynn_Week2_Tuesday_Gift = False
    $ Erynn_Week2_Tuesday_Pickup = False
    $ Erynn_Week2_Tuesday_AlexisFight = False

    jump Week2_Monday

label Week2_Monday:
    if Alexis_Friends == True:
        scene black with Dissolve(2)
        pause 2
        n "Monday. 08:12."
        stop music fadeout 1.0
        play music "Music/Battle_Rock3.mp3" volume 0.6
        jump Week2_Monday_Park
    else:
        scene black with Dissolve(2)
        pause 2
        scene 05_001 with Dissolve(1)
        m "Honey! It's time to wake up."
        mc "Five more minutes, Mom."
        m "I gave you ten already. Come on. Get up."
        scene 05_002 with Dissolve(1)
        mc "*Yawn* Alright, alright... Nggh..."
        m "Wash up and come downstairs. Breakfast is ready. I made French toast."
        mc "Thanks."
        scene 05_003 with Dissolve(1)
        mc "{i}(Oh shit! Alexis...){/i}"
        m "She already left."
        mc "..."
        scene 05_004 with Dissolve(1)
        m "She's a sweet girl."
        mc "Wait... You talked to her?"
        m "Mm-hmm. We had a nice conversation."
        mc "About what?"
        m "Oh... You know... Stuff."
        mc "Mom!"
        scene 05_005 with Dissolve(1)
        m "Get ready or you'll be late."
        mc "Mom!"
        mc "{i}(What did they talk about?){/i}"
        scene black with Dissolve(1)
        pause 2
        scene 05_006 with Dissolve(1)
        mc "..."
        mc "What?"
        scene 05_007 with Dissolve(1)
        m "Nothing."
        mc "..."
        mc "Why are you staring at me like that then?"
        m "Can't I look at my beautiful boy?"
        scene 05_008 with Dissolve(1)
        mc "*Shakes head* Don't you have to go to the restaurant?"
        m "I'll go in the afternoon, I took the morning off to do all the paperwork for yesterday's... event."
        mc "Right."
        m "{i}(Why am I so curious? I really want to know...){/i}"
        scene 05_009 with Dissolve(1)
        m "Is Alexis your girlfriend?"
        mc "{i}(She even knows her name...){/i}"
        mc "You didn't answer my question. I'm not answering yours."
        m "..."
        m "*Sigh* We talked about coffee."
        mc "{i}(Coffee?){/i}"
        scene 05_010 with Dissolve(1)
        m "She drinks it black. Just like you."
        if Alexis_Week1_Monday_BarWait == True:
            mc "I know."
            mc "{i}(We really should stop calling it coffee. This conversation is so weird now. For a second I thought she meant...){/i}"
        else:
            pass
        mc "That's it?"
        m "And how you met."
        mc "Hmm... Okay."
        m "She didn't stay long. I could see she was worried about something."
        scene 05_011 with Dissolve(1)
        mc "{i}(She said multiple times yesterday that she couldn't stay.){/i}"
        m "So... Is she your girlfriend?"
        mc "{i}(Is she going to be in trouble? Shit. I'd better call her.){/i}"
        m "[mc]?"
        scene 05_012 with Dissolve(1)
        mc "Sorry. I need to go or I'll be late."
        m "Uhm... [mc]!"
        m "What about..."
        if Emily_Points == 4:
            mc "Later, Mom. Love you."
            scene 05_013 with Dissolve(1)
            m "Bye, honey. Love you, too."
        else:
            mc "Later, Mom."
            scene 05_013 with Dissolve(1)
            m "Bye, honey."
        m "..."
        m "*Sigh* This is going to bother me all day."
        scene black with Dissolve(1)
        pause 2
        stop music fadeout 1.0
        scene 05_014 with Dissolve(1)
        play music ("Music/LoFi Upbeat 1.mp3", "Music/LoFi Upbeat 2.mp3", "Music/LoFi Upbeat 3.mp3", "Music/LoFi Upbeat 4.mp3") volume 0.2
        a "{i}(I guess it's time to face the music.){/i}"
        a "{i}(Has she been waiting here this whole time?){/i}"
        scene 05_015 with Dissolve(1)
        a "Mom. I'm so sorry!"
        a "I was..."
        scene 05_016 with Dissolve(1)
        x "Thank god, Alexis, you're alright!"
        x "The car was gone, we couldn't reach you on your phone... We were this close to calling the police."
        x "We have been worried sick. Where were you?"
        a "Sorry. I was out and..."
        scene 05_017 with Dissolve(1)
        x "Out? The whole night?"
        a "Uhm..."
        scene 05_018 with Dissolve(1)
        x "Did you drink?"
        a "No, I didn't. I slept at a friend's place."
        x "And your phone doesn't work?"
        a "I had it on silent and forgot to check."
        x "Car keys, please!"
        scene 05_019 with Dissolve(1)
        a "Here."
        x "You're in big trouble, missy."
        a "I know... Is Dad angry that I took his car?"
        x "You can ask him yourself when he's back."
        a "He isn't home?"
        x "No. He had an important meeting and couldn't wait."
        scene 05_020 with Dissolve(1)
        a "Sorry."
        x "Ever since you got back from Lakeyn, you have been acting differently."
        x "I also know you didn't go to all your classes last week."
        x "You aren't staying at your dorm."
        x "Did something happen?"
        scene 05_021 with Dissolve(1)
        a "No."
        x "..."
        x "*Sigh*"
        scene 05_022 with Dissolve(1)
        x "I don't have time to get into this right now, but we'll talk later, alright?"
        a "*Nods*"
        x "Now go inside. Change and get to class! Maybe a shower too."
        scene 05_023 with Dissolve(1)
        a "I'm sorry, Mom."
        x "I'm happy you're okay."
        x "Bye, Lex."
        a "Bye."
        scene black with Dissolve(1)
        pause 2
        scene 05_024 with Dissolve(1)
        play sound "Sounds/Phone_Vibrate.mp3"
        n "*Bzzzt. Bzzzt*"
        scene 05_025 with Dissolve(1)
        x "*Sigh* Now she forgot her phone."
        x "I really don't know where her head is at these last few days."
        x "Something's going on."
        scene black with Dissolve(1)
        pause 2
        stop music fadeout 1.0
        play music "Music/Battle_Rock3.mp3" volume 0.6
        scene 05_026 with Dissolve(1)
        mc "{i}(Hmm... Still can't reach her.){/i}"
        mc "{i}(Why did she leave without saying anything?){/i}"
        mc "{i}(I have a bad feeling all of a sudden.){/i}"
        jump Week2_Monday_Park

label Week2_Monday_Park:
    scene 05_027 with Dissolve(1)
    x "Will you look at that. Right on time."
    da "That's him?"
    x "Yeah. I saw him a few times already with Layla."
    da "Haha. That's the new guy at our school. Something was going on between him and Tori too."
    x "Figures... Guy thinks he can just walk in and take whatever he wants. We're doing society a favour!"
    da "..."
    scene 05_028 with Dissolve(1)
    if Layla_Week1_Wednesday_ParkHelp == False:
        x "Hey!"
    else:
        x "Hey there! Remember me?"
    if Alexis_Friends == False:
        mc "{i}(Should I try again? Maybe leave a voicemail or just text her, maybe?){/i}"
        x "Hey you!"
        mc "{i}(Maybe she's avoiding me on purpose?){/i}"
        if Alexis_Week1_Wednesday_PhoneHome == True:
            scene 05_029 with Dissolve(1)
            mc "{i}(And who was that girl at her house? I completely forgot to ask her about that.){/i}"
            x "HEY! I'm talking to you!"
        else:
            pass
    else:
        x "Hey."
        scene 05_029 with Dissolve(1)
        x "HEY! You deaf or something?"
    menu:
        "Apologetic":
            scene 05_030 with Dissolve(1)
            mc "Sorry, did you say something?"
            mc "I was busy on my phone."
        "Annoyed":
            scene 05_031 with Dissolve(1)
            mc "Holy shit, you're annoying!"
            mc "Just shut the fuck up!"
            mc "Can't you see I'm busy?"
    scene 05_032 with vpunch
    mc "..."
    x "What did you say?"
    scene 05_033 with Dissolve(1)
    mc "What's your problem?"
    x "..."
    mc "Who even are you?"
    scene 05_034 with vpunch
    x "SHUT THE FUCK UP!"
    x "That's what you get for being disrespectful."
    scene 05_035 with Dissolve(1)
    mc "Seriously... What the fuck is wrong with you?"
    x "*Shakes head* This idiot still doesn't get it."
    scene 05_036 with Dissolve(1)
    x "Did I give you permission to talk, you son of a bitch?"
    x "Stay the fuck down!"
    scene 05_037 with vpunch
    x "Stay away from our girls! Or this won't be the last time you eat dirt."
    da "Stop, man! I think he's got the message."
    x "What are you guys waiting for?"
    da "We go to the same school. I'm not getting expelled over this shit."
    scene 05_038 with Dissolve(1)
    x "FUCK YOU GUYS! Just pathetic! I knew you were pussies."
    tj "Let's go, Darryl. This is messed up."
    scene 05_039 with Dissolve(1)
    mc "*Cough-cough*"
    x "Now you listen and listen carefully!"
    x "You never disrespect me ever again or this was just the beginning."
    x "Do you really think Layla is interested in you? Come on, man... Look at you! Tattoos don't make you tough, you know."
    x "You're a pathetic loser."
    scene 05_040 with Dissolve(1)
    x "She wants me!"
    x "Last year, she was all over me. She uses you because she misses me."
    x "You're just a stand-in. She'll be running back to me in no time."
    x "Now... Be a good boy and go to school, yes? You have so much to learn."
    x "*Spits*"
    scene 05_041 with Dissolve(1)
    if Layla_Week1_Wednesday_ParkHelp == False:
        mc "{i}(Still no idea what this was all about...){/i}"
        mc "{i}(But you gotta watch out, Layla... This guy is trouble.){/i}"
    else:
        mc "{i}(Shit, Layla... What have you gotten yourself into? This guy is actual trouble.){/i}"
        mc "{i}(Fuck!){/i}"
    mc "{i}(My head hurts like crazy now...){/i}"
    jump Week2_Monday_School

label Week2_Monday_School:
    scene black with Dissolve(1)
    pause 2
    stop music fadeout 1.0
    scene 05_042 with Dissolve(1)
    play music ("Music/LoFi Upbeat 1.mp3", "Music/LoFi Upbeat 2.mp3", "Music/LoFi Upbeat 3.mp3", "Music/LoFi Upbeat 4.mp3") volume 0.2
    mc "{i}(*Sigh* Should I tell Layla about this? At least I need to warn her about this psycho, right?){/i}"
    mc "{i}(What happened between them last year?){/i}"
    scene 05_043 with Dissolve(1)
    if Alexis_Friends == False:
        x "Seems like I'm not the only one who's late today."
        mc "Hey! I tried to... Uh... never mind."
        mc "{i}(For a second, I thought this was Alexis. That guy must have messed me up pretty bad.){/i}"
    else:
        x "Seems like I'm not the only one who's late today."
        mc "Uhm... Yeah."
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 05_044 at moveup
    pause 3
    if Alexis_Friends == False:
        mc "{i}(Is she another teacher?){/i}"
        mc "{i}(Hmm... She actually looks like Alexis. Well, Alexis looks like her, I guess. And they drive the same car.){/i}"
        mc "{i}(Maybe it's her mom. Wouldn't that be something?){/i}"
        mc "{i}(The more I look at her, I can actually see it.){/i}"
        mc "..."
        if Alexis_Week1_Wednesday_PhoneHome == True:
            mc "{i}(Oh. She could be the woman who interrupted Alexis and me in the shower.){/i}"
            mc "{i}(I can't stop thinking about that.){/i}"
        else:
            pass
    else:
        mc "{i}(Is she another teacher?){/i}"
        mc "{i}(They must make good money here. Driving that cabrio.){/i}"
    scene 05_045 with Dissolve(1)
    x "Did you miss the bus?"
    menu:
        "Yes[KoGa3AutoWTChange1]{size=-4}(MC GoodStudent-2) {/size} {/color}":
            $ MC_GoodStudent -= 2
            mc "Yeah. I was just a bit late and couldn't catch up."
        "No":
            mc "I don't take the bus."
            mc "I got held up on the way and lost track of time."
    x "Okay..."
    x "What happened to your eye?"
    scene 05_046 with Dissolve(1)
    mc "Uh, it's nothing. I just stumbled and hit my head."
    x "Ouch. That must have been a hard fall. It looks painful."
    mc "It's... alright."
    x "Let's go inside?"
    mc "*Nods*"
    scene 05_047 with Dissolve(1)
    x "You can count yourself lucky today."
    mc "{i}(Yeah... Such a lucky day.){/i}"
    x "If I were to punish you for being late, I'd be a hypocrite, right? Since I'm late myself."
    x "I don't know about your teacher, though. What class are you in?"
    scene 05_048 with Dissolve(1)
    mc "3A."
    x "3A. First hour... Hmm... That would be Mr Coleman, right?"
    mc "Yes."
    x "Okay. Have a good day at school. And if your eye gets worse, go see the nurse, please."
    mc "Will do."
    scene 05_049 with Dissolve(1)
    mc "{i}(Good thing she was late too. Else this would've been much less friendly, I bet.){/i}"
    mc "{i}(She seems to be the nicest teacher so far. I wonder what class she teaches.){/i}"
    scene black with Dissolve(1)
    pause 2
    scene 05_050 with Dissolve(1)
    tc "Good morning."
    mc "Morning."
    tc "Nice of you to finally show up, [mc]."
    tc "Do you remember what I said the first day?"
    menu:
        "Answer[KoGa3AutoWTChange1]{size=-4}(MC GoodStudent+2) {/size} {/color}":
            $ MC_GoodStudent += 2
            # MC_GoodStudent (8)
            scene 05_051 with Dissolve(1)
            mc "Zero tolerance for latecomers."
            tc "You did pay attention. Very good."
            tc "Go to your seat. We are on page 128."
        "Be a smartass[KoGa3AutoWTChange1]{size=-4}(MC GoodStudent-2) {/size} {/color}":
            $ MC_GoodStudent -= 2
            scene 05_051 with Dissolve(1)
            mc "Yeah. Something about Egypt and sand, right?"
            tc "..."
            tc "Zero tolerance for latecomers."
            mc "Oh yeah, that too."
            tc "Go to your seat. We are on page 128."
    scene 05_052 with Dissolve(1)
    la "..."
    la "*Whispers* Your eye... What happened?"
    tc "[mc]! One more thing."
    mc "..."
    tc "Detention!"
    scene 05_053 with Dissolve(1)
    mc "What?"
    mc "This is my first time being late."
    scene 05_054 with Dissolve(1)
    la "*Whispers* No, [mc]... Don't argue with him."
    tc "Correction. Second!"
    mc "..."
    scene 05_055 with Dissolve(1)
    tc "And do you know what zero tolerance means?"
    mc "Oh... Enlighten me, Mr Teacher."
    tc "Make that a week of detention."
    mc "Just like old times."
    scene 05_056 with Dissolve(1)
    mc "You know what? Screw this!"
    tc "Where do you think you're going?"
    mc "I don't know. Detention maybe or visiting the pyramids in Egypt. Haven't decided yet."
    tc "I can help you with that. How about the principal's office."
    tc "And don't think you can leave the school grounds. I'll check up if you were there or not."
    mc "You do that."
    if Layla_Points >= 25:
        $ Layla_Week2_Detention = True
        scene 05_057 with Dissolve(1)
        la "[mc]... Wait!"
        tc "Layla, stay seated!"
        el "*Whispers* What are you doing? Sit back down."
        la "I just..."
        tc "Detention!"
        scene 05_058 with Dissolve(1)
        tc "Now take your seat!"
        la "..."
        tc "Or do you want to join him in the principal's office?"
        scene 05_059 with Dissolve(1)
        la "No..."
        tc "Alright. We can finally continue."
    else:
        pass
    scene black with Dissolve(1)
    pause 2
    scene 05_060 with Dissolve(1)
    mc "{i}(Okay... What is the best way to do this?){/i}"
    play sound "Sounds/Phone_Message.mp3"
    n "*Bzzzt*"
    scene 05_061 with Dissolve(1)
    mc "{i}(Oh? A message from Layla.){/i}"
    la "What happened? Can we talk after class, please? When you're at the principal's office, be honest with her!"
    mc "{i}(Be honest with her? About what? The detention?){/i}"
    scene 05_062 with Dissolve(1)
    n "*Knock-knock*"
    x "Yes, come in."
    scene 05_063 with Dissolve(1)
    mc "{i}(*Sigh* Of course she's the principal.){/i}"
    mc "{i}(Fuck! What is wrong with this day.){/i}"
    mc "Morning."
    scene 05_064 with Dissolve(1)
    x "Oh... Good morning again."
    x "[mc] Moreno, right?"
    mc "Yes."
    x "Please, have a seat."
    scene 05_065 with Dissolve(1)
    am "I'll officially introduce myself."
    am "I am Adriana Moore. Principal of MS Athletics."
    mc "Nice to meet you, Principal Moore."
    scene 05_066 with Dissolve(1)
    am "I was just reading your file."
    am "You transferred from Riverside last week."
    mc "Yes."
    am "Really good scores. Impressive, actually!"
    am "You're not cheating, right?"
    mc "Heh..."
    scene 05_067 with Dissolve(1)
    am "What?"
    menu:
        "It's nothing":
            mc "Oh no... It's nothing."
            mc "Stupid inside joke."
            am "Hmm..."
        "Heard that before[KoGa3AutoWTChange1]{size=-4}(Adriana Week2 Monday TestBack) {/size} {/color}":
            $ Adriana_Week2_Monday_TestBack = True
            mc "Someone asked me the same question when they saw my score on the geography test."
            am "Really? Class 3A, was it?"
            mc "Yes."
            am "You've gotten the test back already? Interesting..."
            mc "{i}(Why would she care about that?){/i}"
    scene 05_068 with Dissolve(1)
    am "How do you like this school so far?"
    menu:
        "Good[KoGa3AutoWTChange1]{size=-4}(MC GoodStudent+2, Adriana Points+2) {/size} {/color}":
            $ MC_GoodStudent += 2
            # MC_GoodStudent (10)
            $ Adriana_Points += 2
            # Adriana (2)
            $ Mike_Week2_Monday_Surname = True
            mc "Yeah, I like it."
            mc "I really enjoy the athletic department."
            am "That's good to hear. Since this is a sports academy."
            am "What team did you join?"
            mc "Track and field."
            scene 05_069 with Dissolve(1)
            am "Oh... With Mr Morgan."
            mc "Mr Morgan?"
            am "Yes. Coach Morgan."
            mc "Ah! He only introduced himself as Mike and coach. I didn't know his surname."
            mc "{i}(Morgan, huh... What a coincidence.){/i}"
        "It's a school":
            mc "It's a school. It makes no difference to me."
            am "Heh... Gotcha."
    scene 05_070 with Dissolve(1)
    am "So... What brings you to my office?"
    mc "I've got detention."
    scene 05_071 with Dissolve(1)
    am "Detention is after classes, not during."
    mc "..."
    mc "*Sigh* I didn't agree with the detention and I argued. Got more detention and was sent here."
    scene 05_072 with Dissolve(1)
    am "{i}(I've only heard good news about him so far from the teachers. Something must have happened before.){/i}"
    am "Let me take a look at your eye again."
    scene 05_073 with Dissolve(1)
    am "That doesn't look good. I think it's getting worse."
    mc "It's fine. It will heal up in no time."
    am "It happened this morning?"
    mc "Yes."
    scene 05_074 with Dissolve(1)
    am "Hmm... How did it happen again?"
    menu:
        "Lie[KoGa3AutoWTChange1]{size=-4}(MC GoodStudent-2) {/size} {/color}":
            $ MC_GoodStudent -= 2
            mc "I fell and hit my head."
            am "{i}(He's sticking to his story. Somehow I don't believe it. Does he have problems at home?){/i}"
            am "{i}(I need to contact his parents.){/i}"
            scene 05_075 with Dissolve(1)
            am "I'm worried about your eye."
            am "I'll excuse you for today so you can see a doctor."
            am "And I'll let your teachers know you won't be coming back today."
            mc "Thank you very much."
            am "Okay. Take care of yourself and I'll see you tomorrow then. Bye, [mc]."
            mc "Goodbye, Principal Moore."
        "Truth[KoGa3AutoWTChange1]{size=-4}(Adriana Week2 Monday Truth, Adriana Points+2, MC GoodStudent+2) {/size} {/color}":
            $ Adriana_Week2_Monday_Truth = True
            $ Adriana_Points += 2
            # Adriana (2)
            $ MC_GoodStudent += 2
            # MC_GoodStudent (12)
            mc "*Sigh* Someone hit me."
            am "{i}(I didn't expect him to tell me what actually happened.){/i}"
            am "{i}(It happened before he arrived at school. Does he have problems at home? This is bad.){/i}"
            scene 05_076 with Dissolve(1)
            am "Did it happen at home?"
            mc "No."
            am "{i}(Oh, thank god...){/i}"
            scene 05_077 with Dissolve(1)
            mc "It was in the park on my way to school."
            am "Was it someone from this school?"
            mc "No... He went here last year, I think."
            am "Do you know his name?"
            mc "No."
            scene 05_078 with Dissolve(1)
            am "I'm worried about your eye."
            am "I'll excuse you for today so you can see a doctor."
            am "And I'll let your teachers know you won't be coming back today."
            mc "Thank you very much."
            am "Okay... Take care of yourself and I'll see you tomorrow then. Bye, [mc]."
            mc "Goodbye, Principal Moore."
            scene 05_079 with Dissolve(1)
            am "{i}(I'm so relieved that didn't happen at home.){/i}"
            am "{i}(He seems like a good kid. Honest too.){/i}"
            am "{i}(I guess I'll have a talk with Mr Coleman so the issue won't escalate.){/i}"
            am "{i}(But he'll still have to go to detention. Can't help him with that.){/i}"
    scene 05_080 with Dissolve(1)
    mc "{i}(That went better than expected. I think I caught her on a good day.){/i}"
    menu:
        "Go home[KoGa3AutoWTChange1]{size=-4}(Layla Points-4) {/size} {/color}":
            $ Layla_Points -= 4
            mc "{i}(I'd better go home then before something else happens today...){/i}"
            jump Week2_Monday_AfterSchool
        "Wait for Layla":
            scene black with Dissolve(1)
            pause 2
            scene 05_081 with Dissolve(1)
            el "Hola."
            mc "Hola, Elena."
            el "De verdad quiero saberlo?\n(Do I even want to know?)"
            mc "Depende...\n(Depends...)"
            scene 05_082 with Dissolve(1)
            mc "Is Layla coming?"
            el "No... The teacher asked her to stay behind. So, she sent me."
            if Layla_Week2_Detention == True:
                el "But you'll see her in detention."
                mc "What do you mean? She's also got detention?"
                el "Yeah. Because of you!"
                mc "Because of me? What did I do?"
                scene 05_083 with Dissolve(1)
                el "She tried to go after you when you left."
                mc "Why would she do that?"
                el "..."
                mc "I guess I'll talk to her tomorrow then."
            else:
                mc "I guess I'll see her tomorrow then."
                el "Or your next class."
            mc "The principal excused me for today. So... I'm actually leaving."
            el "Really? How did you manage that?"
            scene 05_084 with Dissolve(1)
            mc "It's kinda obvious."
            el "Right..."
            el "Okay. I'm curious now. How did that happen?"
            menu:
                "Go home[KoGa3AutoWTChange1]{size=-4}(Elena Points-2) {/size} {/color}":
                    $ Elena_Points -= 2
                    mc "I'll tell you next time."
                    el "So you have time to come up with a better story?"
                    mc "Exactly. The real one is kinda lame."
                    scene 05_085 with Dissolve(1)
                    el "Heh..."
                    el "See you tomorrow then."
                    mc "Yeah. Bye, Elena."
                    el "Bye, [mc]."
                    jump Week2_Monday_AfterSchool
                "Tell her[KoGa3AutoWTChange1]{size=-4}(Layla Week2 Monday Wait, Elena Points+2) {/size} {/color}":
                    $ Layla_Week2_Monday_Wait = True
                    $ Elena_Points += 2
                    # Elena (12)
                    scene 05_086 with Dissolve(1)
                    mc "Did Layla have a boyfriend last year?"
                    el "What does that have to do with your eye?"
                    mc "Well... He gave me my makeup."
                    el "Layla never had a boyfriend!"
                    el "..."
                    scene 05_087 with Dissolve(1)
                    el "Wait... Don't tell me that was Lucas?"
                    mc "I don't know his name, but he was pretty obsessed with Layla."
                    scene 05_088 with Dissolve(1)
                    el "It's definitely him then."
                    el "*Sigh* What is that guy's problem?"
                    el "It was a stupid dare."
                    scene 05_089 with Dissolve(1)
                    el "It was last year at training camp. We played truth or dare."
                    el "Someone dared Layla to flirt with a guy. And so she did."
                    el "She randomly picked someone and that someone was Lucas."
                    scene 05_090 with Dissolve(1)
                    el "It was all fun and games but Lucas didn't see it that way."
                    el "He kept joining us, asking Layla out, making advances."
                    el "Layla declined every time, even ignored him, but he just didn't get it."
                    scene 05_091 with Dissolve(1)
                    el "We thought it would all be over once he switched schools, but even now, he still shows up."
                    mc "Yeah... I saw him in the park with Layla a few days ago."
                    el "..."
                    el "We don't know what to do about him."
                    menu:
                        "Help[KoGa3AutoWTChange1]{size=-4}(Layla Week2 Monday LucasHelp, Elena Points+2) {/size} {/color}":
                            $ Layla_Week2_Monday_LucasHelp = True
                            $ Elena_Points += 2
                            # Elena (14)
                            mc "{i}(I hope I won't regret this.){/i}"
                            scene 05_092 with Dissolve(1)
                            mc "I can help. We can figure something out."
                            el "Really? Thank you very much, [mc]."
                            n "*School bell*"
                        "Don't help[KoGa3AutoWTChange1]{size=-4}(Elena Points-2) {/size} {/color}":
                            $ Elena_Points -= 2
                            scene 05_093 with Dissolve(1)
                            mc "I'm sorry, but I don't know what to do either about that."
                            el "It's fine. It's our problem anyway. We started it."
                            n "*School bell*"
                    scene 05_094 with Dissolve(1)
                    el "I guess my next class is about to start. I have to go."
                    mc "Yeah, don't be late or you might join me in detention."
                    if Layla_Week2_Detention == True:
                        mc "Or rather Layla."
                        el "Heh, yeah..."
                    else:
                        el "That might actually be true."
                    el "One more thing. Can you please not tell Layla about this? She will just freak out."
                    scene 05_095 with Dissolve(1)
                    mc "What do you want me to say?"
                    el "Just... I don't know. Tell her something."
                    mc "I can't lie to her."
                    el "She's my best friend. I don't want to either, but if I can protect her that way, I will."
                    mc "Hmm... Okay."
                    scene 05_096 with Dissolve(1)
                    el "Thank you, [mc]. I will tell Layla you went home. See you tomorrow?"
                    mc "Thanks, Elena. See you tomorrow."
                    el "Nos vemos.\n(See you.)"
                    if Elena_Points == 14:
                        scene 05_097 with Dissolve(1)
                        el "Oh, and [mc]... You really should get that eye checked out."
                        mc "It will be fine. Not the first time I've got hit."
                        el "Somehow that doesn't surprise me."
                        mc "Haha."
                        scene 05_098 with Dissolve(1)
                        mc "But thanks for worrying."
                        mc "You can steal another kiss from me anytime you want!"
                        el "Dios mío..."
                    else:
                        pass
                    jump Week2_Monday_AfterSchool

label Week2_Monday_AfterSchool:
    scene black with Dissolve(1)
    pause 2
    stop music fadeout 1.0
    scene 05_099 with Dissolve(1)
    play music "Music/Battle_Rock2.mp3" volume 0.6
    mc "{i}(*Sigh* Damn, I'm nervous...){/i}"
    mc "{i}(What should I even tell her? She's going to be so mad. First the restaurant, and now this.){/i}"
    mc "{i}(I'm back for just a week and I have detention already. Seems like nothing has changed from before.){/i}"
    mc "{i}(But it's better to hear the story from me rather than getting a phone call from the school, I guess.){/i}"
    mc "{i}(*Shakes head* What a shitty day.){/i}"
    scene 05_100 with Dissolve(1)
    mc "Mom?"
    mc "{i}(Hmm... Maybe upstairs?){/i}"
    scene 05_101 with Dissolve(1)
    mc "Mom? Are you here?"
    mc "{i}(Didn't she say she'd stay the morning for paperwork?){/i}"
    mc "{i}(Maybe she's shopping. Clearing her head or something.){/i}"
    scene 05_102 with Dissolve(1)
    mc "{i}(I guess I'll wait until she's back then.){/i}"
    n "*Laughing*"
    mc "..."
    scene 05_103 with Dissolve(1)
    mc "{i}(Oh? Right... She's probably at Melissa's.){/i}"
    mc "{i}(Okay... What's the best way to explain this?){/i}"
    scene black with Dissolve(1)
    pause 2
    scene 05_104 with Dissolve(1)
    mc "{i}(Here goes nothing.){/i}"
    mc "{i}(What's with all those glasses and bottles?){/i}"
    mc "{i}(Looks like they've been drinking a lot. She probably needed that after the Rachel fiasco.){/i}"
    mc "{i}(This might work in my favour if she's a little tipsy. Possibly drunk?){/i}"
    scene 05_105 with Dissolve(1)
    mc "{i}(What are they even doing?){/i}"
    mc "Mom... I need to ta..."
    scene 05_106 with Dissolve(1)
    mc "..."
    mc "What the fuck?"
    scene 05_107 with Dissolve(1)
    me "Oh no."
    me "Emily... Stop! [mc] is here."
    m "What are you talking about? He's at school."
    me "He's here..."
    scene 05_108 with Dissolve(1)
    m "..."
    m "[mc]!"
    m "What are you doing here?"
    m "Your eye... What happened to..."
    scene 05_109 with Dissolve(1)
    mc "So this is what you call paperwork?"
    mc "Or more likely, the reason why dad left. You actually cheated on him! With Melissa!"
    m "What? No... No! This isn't..."
    mc "This isn't what I think it is?"
    scene 05_110 with Dissolve(1)
    mc "Spare me the bullshit."
    m "[mc]... Wait!"
    me "Emily, you are..."
    scene 05_111 with Dissolve(1)
    me "Naked..!"
    m "[mc]!"
    scene 05_112 with Dissolve(1)
    m "Please, wait. Let me explain."
    mc "There's nothing to explain."
    scene 05_113 with Dissolve(1)
    mc "You cheated. Dad left. End of story!"
    m "No! That's not..."
    scene 05_114 with Dissolve(1)
    m "Please!"
    mc "..."
    scene 05_115 with Dissolve(1)
    mc "Do you have any idea how much shit I gave dad the last five years?"
    m "{i}(Stop!){/i}"
    mc "Dad was the one who left. Dad was the one who destroyed this family."
    m "{i}(Stop!){/i}"
    mc "But, no. Not Dad. It was you!"
    m "..."
    m "{i}(Stop calling him dad!){/i}"
    scene 05_116 with Dissolve(1)
    mc "Dad was..."
    m "HE'S NOT YOUR DAD!"
    mc "..."
    scene 05_117 with Dissolve(1)
    m "Oh no... [mc], I mean... "
    m "{i}(What did I do?){/i}"
    mc "What?"
    m "{i}(Why did I say that? I promised.){/i}"
    m "..."
    scene 05_118 with Dissolve(1)
    mc "Is this for real?"
    m "I'm sorry... I..."
    mc "What is happening? Is this all a big joke?"
    scene 05_119 with Dissolve(1)
    m "[mc], please. I will explain everything."
    m "What happened to your eye?"
    mc "Really? My eye? That's what you're worried about right now?"
    mc "What's next? You're going to tell me I'm adopted? Are you even my mom?"
    m "[mc]. Of course, I am!"
    scene 05_120 with Dissolve(1)
    mc "Don't touch me!"
    m "Please, [mc]."
    mc "I said don't touch me!"
    m "..."
    scene 05_121 with Dissolve(1)
    m "Where are you going?"
    mc "None of your business. Away from... you! Whoever you are."
    m "[mc], please. Just let me explain."
    mc "There's nothing to explain."
    m "[mc]!"
    scene 05_122 with Dissolve(1)
    m "*Crying*"
    m "I'm so sorry."
    m "Please, don't leave."
    scene 05_123 with Dissolve(1)
    me "It will be alright, Emily."
    m "*Crying* No... The way he looked at me. Mel, he..."
    me "He's just shocked. Give it some time."
    scene 05_124 with Dissolve(1)
    m "You were right. I should've told him much sooner."
    me "No! Don't blame yourself now. Andres is the one who should've told him as he promised!"
    me "You kept your promise not telling him."
    m "Until now."
    scene 05_125 with Dissolve(1)
    m "He's gonna hate me. What if he doesn't come back?"
    m "I won't forgive myself for this."
    me "This isn't your fault, Em!"
    scene 05_126 with Dissolve(1)
    m "It is! I have to go after him and tell him everything."
    me "No. Let him cool off. He'll come back when he's ready to talk."
    m "But he has nowhere to go."
    me "He'll be fine. I'll call Erynn later to check up on him."
    scene 05_127 with Dissolve(1)
    m "..."
    m "Why did I kiss you anyway? I know we drank a lot but this hasn't happened since..."
    me "College!"
    m "Yes. So why now?"
    me "You were stressed out because of the restaurant. I should've pushed you away."
    m "No... This is on me, Mel."
    $ renpy.end_replay()
    jump Week2_Monday_Erynn

label Week2_Monday_Erynn:
    scene black with Dissolve(2)
    pause 2
    stop music fadeout 1.0
    play music "Music/Slow.mp3" volume 0.3
    if Alexis_Friends == False:
        scene 05_128 with Dissolve(1)
        mc "Come on, Alexis. Pick up!"
        mc "..."
        mc "Why isn't she answering? Is she ignoring me?"
        mc "Fuck!"
        scene 05_129 with Dissolve(1)
        mc "*Sigh* Who else can I call?"
        mc "Erynn, maybe? Does she know about this?"
        scene 05_130 with Dissolve(1)
        mc "Come on... Don't tell me you're not picking up either, Erynn!"
    else:
        scene 05_129 with Dissolve(1)
        mc "Should I call Erynn?"
        mc "Maybe she knows about all this shit."
        scene 05_130 with Dissolve(1)
        mc "Come on... Please pick up, Erynn!"
    scene 05_131 with Dissolve(1)
    er "Hey, [mc]. How are you?"
    mc "Hi. Uhm... Where are you?"
    er "I'm in class at the moment."
    mc "Right... Sorry. Uh... Bye."
    scene 05_132 with Dissolve(1)
    er "No, wait! Aren't you in school? Is everything alright?"
    mc "..."
    er "[mc]?"
    mc "I don't know."
    scene 05_133 with Dissolve(1)
    er "Okay... Where are you right now?"
    mc "I'm just walking around."
    er "Text me the address. I'll come to pick you up."
    mc "You don't have to. You're in class."
    er "No. I want to! Text me the address."
    er "See you soon."
    scene 05_134 with Dissolve(1)
    er "..."
    er "{i}(Something is wrong.){/i}"
    scene black with Dissolve(1)
    pause 2
    scene 05_135 with Dissolve(1)
    er "{i}(There he is.){/i}"
    er "{i}(Why is he sitting on the ground?){/i}"
    scene 05_136 with Dissolve(1)
    er "[mc]!"
    mc "..."
    if Alexis_Friends == False:
        scene black with Dissolve(1)
        transform moveup:
            xalign 0.5 yalign 1.0
            linear 5.0 yalign 0.0
        show 05_137 at moveup
        pause 3
        mc "{i}(Alexis?){/i}"
        mc "{i}(What..?){/i}"
        er "Are you okay?"
        mc "*Shakes head*"
        scene black with Dissolve(1)
        transform moveup:
            xalign 0.5 yalign 1.0
            linear 5.0 yalign 0.0
        show 05_138 at moveup
        pause 3
        mc "Erynn!"
        mc "{i}(Why did I mistake her for Alexis? The clothes, maybe?){/i}"
        mc "{i}(Alexis was wearing something similar yesterday.){/i}"
    else:
        scene black with Dissolve(1)
        transform moveup:
            xalign 0.5 yalign 1.0
            linear 5.0 yalign 0.0
        show 05_138 at moveup
        pause 3
        er "Are you okay?"
        mc "Erynn!"
    scene 05_139 with Dissolve(1)
    er "[mc]! Your eye! What happened? Were you in a fight?"
    mc "Heh... It wasn't much of a fight."
    er "At school?"
    mc "No. It happened before."
    scene 05_140 with Dissolve(1)
    er "Who did that?"
    mc "I don't know. Some jealous asshole."
    if Layla_Week2_Monday_LucasHelp == False:
        pass
    else:
        mc "I think his name was Lucas or something."
        er "Don't know any Lucas."
    scene 05_141 with Dissolve(1)
    er "Are you alright? Does it hurt?"
    mc "It doesn't hurt."
    scene 05_142 with Dissolve(1)
    er "Did you see a doctor?"
    mc "If you continue like this, we will be done with those thousand questions in five minutes."
    scene 05_143 with Dissolve(1)
    er "..."
    er "*Sigh* Sorry... I'm just worried, okay?"
    mc "Thanks."
    scene 05_144 with Dissolve(1)
    er "But why are you sitting here instead of going home? Emily won't be mad if you explain what happened."
    mc "I was home. I saw her in the pool, making out with your mom."
    er "..."
    scene 05_145 with Dissolve(1)
    er "What?"
    mc "Yeah."
    er "..."
    mc "Did you know? Are they like... together?"
    er "No... They never said anything. If they were in a relationship, Mom would've told me."
    scene 05_146 with Dissolve(1)
    mc "..."
    mc "I confronted her. Asked her if that was the reason why dad left."
    mc "She then drops another bomb. Tells me that he isn't my father."
    er "Wait... This isn't a joke, right?"
    mc "It's not."
    er "Please tell me everything."
    scene black with Dissolve(1)
    pause 2
    scene 05_147 with Dissolve(1)
    er "..."
    er "I'm so confused. Why tell you now? And like this."
    mc "That's what I'm asking myself. Is it even true?"
    mc "Maybe she just said it because she was angry that I accused her of cheating and that's the reason why dad... or rather Andres left."
    er "I don't know. This is serious. Emily wouldn't just say something like that. Even in the heat of the moment."
    scene 05_148 with Dissolve(1)
    er "You really need to talk to her."
    mc "At this point, I'm not even sure if she's my real mom or if I'm adopted."
    er "Don't even think about that. But that gives you even more reason to talk to her and find out the truth."
    mc "I know... But if she lied about my dad this whole time, she can easily lie about me being adopted."
    er "I don't believe she would lie about that. Besides, there are pictures of her when she was pregnant."
    mc "..."
    scene 05_149 with Dissolve(1)
    mc "{i}(Was I too harsh?){/i}"
    mc "{i}(With all the stuff that happened at the restaurant and now this... Dammit...){/i}"
    er "Just talk to her."
    mc "I can't... Not like this. I'll just snap at her again."
    mc "That's why I'm sitting here. I can't go home and face her right now."
    er "I understand."
    scene 05_150 with Dissolve(1)
    er "Come on. You can stay at my place for now. We'll figure something out."
    mc "Thank you, Erynn."
    menu:
        "Get up":
            scene 05_151 with Dissolve(1)
            er "Let's go home."
            mc "*Nods*"
            jump Week2_Monday_Erynn_Apartment
        "Let her help you[KoGa3AutoWTChange1]{size=-4}(Week2 Monday Erynn Help, Erynn Points+2) {/size} {/color}":
            $ Week2_Monday_Erynn_Help = True
            $ Erynn_Points += 2
            # Erynn (10)
            scene 05_152 with Dissolve(1)
            er "Here... I'll help you up."
            mc "Thanks."
            scene 05_153 with vpunch
            er "Ouch."
            er "Hey! What was that?"
            scene 05_154 with Dissolve(1)
            er "Did you really think I could pull you up by myself? I expected you to help a little."
            er "You're not as light as you were back then."
            mc "Sorry..."
            er "Come on. Let's get up. With a little help this time."
            scene 05_155 with Dissolve(1)
            mc "You okay? Did you hurt yourself when you fell?"
            er "NO, I'm good."
            mc "Oh... Your pantyhose are torn. Sorry!"
            er "Don't worry about it. Not the first ones which I've torn and won't be the last."
            scene 05_151 with Dissolve(1)
            er "Let's go home."
            mc "*Nods*"
            jump Week2_Monday_Erynn_Apartment

label Week2_Monday_Erynn_Apartment:
    scene black with Dissolve(1)
    pause 2
    stop music fadeout 1.0
    scene 05_156 with Dissolve(1)
    play music ("Music/LoFi Upbeat 1.mp3", "Music/LoFi Upbeat 2.mp3", "Music/LoFi Upbeat 3.mp3", "Music/LoFi Upbeat 4.mp3") volume 0.2
    if Erynn_Week1_Stay == False:
        er "Well... This is it. Nothing much but."
        mc "Nah. Looks great. It has all you need, right? And it's in the middle of the city, so."
        er "Yeah."
        er "Make yourself comfortable. I'll change real quick."
    else:
        er "Well... You know the place. Make yourself comfortable."
        er "I'll change real quick."
        mc "Sure. Take your time."
    scene black with Dissolve(1)
    pause 2
    scene 05_157 with Dissolve(1)
    mc "*Sigh*"
    mc "{i}(What should I do now?){/i}"
    mc "{i}(I can't stay here forever. But what other options do I have?){/i}"
    er "Hey. What are you thinking about? You look so serious."
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 05_158 at moveup
    pause 3
    mc "..."
    mc "Damn... I almost didn't recognise you."
    mc "It has been ages since I last saw you without a ponytail."
    er "Hehe."
    scene 05_159 with Dissolve(1)
    er "Sometimes I wear it loose. Not that often though."
    er "It's much more convenient to just tie it."
    er "That way I don't have to wash it every day."
    menu:
        "Compliment hair[KoGa3AutoWTChange1]{size=-4}(Week2 Monday Erynn Hair, Erynn Points+2) {/size} {/color}":
            $ Week2_Monday_Erynn_Hair = True
            $ Erynn_Points += 2
            # Erynn (12)
            scene 05_160 with Dissolve(1)
            mc "Looks good. I quite like it!"
            er "Thank you."
            mc "I think you should wear it this way more often."
        "Don't":
            pass
    scene 05_161 with Dissolve(1)
    mc "Reminds me of the time when I had long hair."
    er "Wait... You had long hair? No?"
    mc "No, I'm kidding."
    er "Haha. I was hoping to see some pictures. I just can't imagine you with long hair."
    scene 05_162 with Dissolve(1)
    er "..."
    mc "What?"
    er "Do you want me to get some ice for your eye? It will keep the swelling down."
    mc "No-no, it's fine. It's not bothering me or anything."
    er "But if it's getting worse, I'll drag you to a doctor!"
    mc "Haha."
    scene 05_163 with Dissolve(1)
    mc "..."
    mc "{i}(Just like old times.){/i}"
    mc "{i}(Always worrying about me.){/i}"
    mc "{i}(I remember one time when we played outside and I fell down, she went into panic mode for a small scratch...){/i}"
    scene 05_164 with Dissolve(1)
    er "*Sigh*"
    mc "That was a big sigh."
    er "I was just thinking.. Seems like we are in the same situation now. I mean with our dads."
    mc "Right... You don't know about your dad either."
    mc "How do you actually feel about that?"
    scene 05_165 with Dissolve(1)
    er "I'm fine with it. Mom did a good job on her own. I never missed not having a dad."
    er "Well... I don't have anything to compare it to, actually."
    er "So, to be honest... I don't know."
    mc "When did Melissa tell you?"
    scene 05_166 with Dissolve(1)
    er "I asked her a few times why I didn't have a dad when I was younger. She always said that she'll tell me when I was older."
    er "And she did when I was fifteen."
    er "Mom told me what she knows, which isn't much. It was basically a one-night stand."
    er "They never met again after that day."
    scene 05_167 with Dissolve(1)
    mc "Hmm. Are you okay with that?"
    mc "I mean, not knowing anything?"
    scene 05_162 with Dissolve(1)
    er "I've actually been looking for him for some time now."
    mc "Really? Any luck with that?"
    er "No... Nothing yet. I only know his first name and what he looked like back then. Or at least an idea of what he looked like."
    er "So, not much to go on. But even if I never find him, I'm okay with it."
    er "Because... What if I don't like the guy?"
    mc "You turned out great. He can't be that bad, right?"
    er "*Shrugs*"
    scene 05_168 with Dissolve(1)
    er "Please don't tell Mom I'm doing this."
    mc "I won't."
    er "Thank you, [mc]."
    scene 05_169 with Dissolve(1)
    mc "Heh..."
    er "What?"
    mc "I just thought of something."
    scene 05_170 with Dissolve(1)
    mc "Maybe we have the same dad and we're actually siblings. Wouldn't that be something?"
    er "Don't even joke about that. I don't want that!"
    mc "Do you want to take a DNA test and know for sure?"
    er "No, [mc]. No... I don't want to know. And don't put that idea in my head."
    er "We're not siblings! No!"
    menu:
        "Joke":
            scene 05_171 with Dissolve(1)
            mc "Hmm... I'm not so sure."
            mc "Taking a closer look at you... We kinda look alike."
            er "No, we don't! Not at all! Not even a little!"
            er "If we would be siblings, you'd at least have blonde hair and blue eyes!"
            scene 05_172 with Dissolve(1)
            mc "Hey, Sis!"
            er "{i}(And now I've started imagining it. NO...){/i}"
            er "{i}(I don't want to be your sister!){/i}"
            mc "What are you doing? Are you picturing me as a blonde?"
            scene 05_173 with Dissolve(1)
            er "..."
            er "This is your fault with your stupid thoughts..!"
            mc "Haha."
        "Not siblings":
            pass
    scene 05_174 with Dissolve(1)
    mc "*Stomach rumbles*"
    er "Someone's hungry."
    mc "Haven't eaten anything since this morning."
    scene 05_175 with Dissolve(1)
    er "I'll cook you something."
    er "It won't be as good as your mom's but..."
    er "..."
    scene 05_176 with Dissolve(1)
    er "{i}(Shit.){/i}"
    er "Sorry... I didn't meant to..."
    mc "It's fine. Thank you, Erynn."
    scene black with Dissolve(1)
    pause 2
    if Erynn_Week1_Stay == False:
        scene 05_177 with Dissolve(1)
        mc "Heh..."
        mc "Can't believe you still have this picture of us."
        scene 03_602 with Dissolve(1)
        er "Which one?"
        mc "The one where you carried me."
        scene 05_178 with Dissolve(1)
        er "Why wouldn't I have it? It's cute, right?"
        mc "Mm-hmm."
        er "I have a lot more pictures of us if you want to take a look."
        mc "That'd be great!"
        er "Let me get them for you."
    else:
        scene 05_178 with Dissolve(1)
        mc "Erynn... Last time you mentioned you had lots of pictures of us."
        er "I do. Do you want to take a look?"
        mc "That'd be great!"
        er "Let me get them for you."
    scene 05_179 with Dissolve(1)
    er "Here you go."
    mc "Thanks."
    mc "By the way... What are you making?"
    er "Paprika, onion and chicken on top of rice. That okay?"
    mc "Sounds good. Can't wait to taste it."
    scene 05_180 with Dissolve(1)
    mc "{i}(Really? First picture and fucking Ethan is in it.){/i}"
    mc "{i}(Just look at him. Such an idiot.){/i}"
    mc "{i}(Are they still friends?){/i}"
    scene 05_181 with Dissolve(1)
    mc "{i}(This must have been a photo shoot.){/i}"
    mc "{i}(Skater clothing line? A little punk, maybe?){/i}"
    mc "{i}(I can see Lakeyn wear something like that.){/i}"
    scene 05_182 with Dissolve(1)
    mc "{i}(Little Erynn with Melissa.){/i}"
    mc "{i}(Cute!){/i}"
    mc "{i}(That's what I remember her looking like...){/i}"
    mc "{i}(And look at her now.){/i}"
    scene 05_183 with Dissolve(1)
    mc "{i}(Ethan again...){/i}"
    mc "*Shakes head*"
    mc "{i}(What's with that dress? Prom?){/i}"
    mc "Did you go to Prom with... Ethan?"
    er "*Sigh* Yeah... Don't remind me."
    scene 05_184 with Dissolve(1)
    mc "Why go with him?"
    er "..."
    er "You didn't ask me."
    mc "..."
    mc "{i}(I wasn't here at the time, how could I... Would she even want to go with me? Never mind...){/i}"
    scene 05_185 with Dissolve(1)
    mc "{i}(Haha. Me sitting on Melissa's shoulders.){/i}"
    mc "{i}(I think that was when I couldn't swim just yet. Melissa taught me almost every day.){/i}"
    scene 05_186 with Dissolve(1)
    mc "{i}(That's right. She used to tickle me every opportunity she had.){/i}"
    mc "{i}(I think it's about time I return that favour.){/i}"
    scene 05_187 with Dissolve(1)
    mc "{i}(What?){/i}"
    mc "Wait a minute... You had blue hair? And pink contacts?"
    mc "When was that?"
    er "Haha, yeah.... Like a year or so ago? It was for a shoot."
    scene 05_188 with Dissolve(1)
    er "I was supposed to be some crazy game character."
    mc "Oh? Which character?"
    er "Hmm... I can't remember. I think she was called Jinx?"
    mc "You got the crazy part right."
    er "Haha."
    scene 05_187 with Dissolve(1)
    mc "{i}(Jinx... I'll look her up later.){/i}"
    er "I only had the colour for about a week. Mom really liked it, though."
    mc "Heh... I can believe that."
    scene 05_189 with Dissolve(1)
    mc "{i}(Holy shit! That's Melissa. When was that?){/i}"
    mc "{i}(Wow... She hasn't changed much at all.){/i}"
    menu:
        "Milf[KoGa3AutoWTChange1]{size=-4}(Melissa Week2 Monday Milf) {/size} {/color}":
            $ Melissa_Week2_Monday_Milf = True
            mc "Your mom is a milf!"
            scene 05_190 with Dissolve(1)
            er "[mc]! I can't believe you just called my mom a milf."
            mc "{i}(Shit!){/i}"
            mc "Uh... Not what I meant. I meant to say she's very pretty."
            er "Uh-huh."
            mc "Can you put the knife down, please? You're scaring me!"
            mc "{i}(I can see why they hired her for that crazy game character.){/i}"
            er "..."
        "Pretty":
            scene 05_191 with Dissolve(1)
            mc "Here's a picture of Melissa when she was younger."
            mc "She's very pretty."
            er "Yeah she is."
    scene 05_189 with Dissolve(1)
    mc "She had no tattoos yet. Weird to see her like that."
    er "It's very hard to imagine her without them now."
    mc "She already coloured her hair back then though."
    er "Yeah..."
    mc "Now that I think about it... I've never seen her natural hair colour."
    mc "To be honest. I wouldn't even know what her natural hair colour is."
    scene 05_192 with Dissolve(1)
    er "Blonde. Like me."
    mc "Blonde? Really? I didn't picture her as a blonde."
    mc "Do you have a picture of that?"
    er "Sadly, no. Those pictures are rare. I think Mom has one at home. I'll look for it next time."
    scene 05_189 with Dissolve(1)
    mc "Cool. I really want to see that."
    scene 05_193 with Dissolve(1)
    mc "{i}(Oh?){/i}"
    mc "{i}(Mom... She looks so young, too.){/i}"
    mc "*Sigh*"
    mc "..."
    scene 05_194 with Dissolve(1)
    mc "{i}(Here we have Erynn again with a friend.){/i}"
    mc "{i}(They hung out very often or wasn't that her?){/i}"
    scene 05_195 with Dissolve(1)
    mc "{i}(Here she is again. It was definitely her.){/i}"
    mc "{i}(Hmm. She looks so familiar.){/i}"
    mc "{i}(Wait...){/i}"
    mc "Hey, Erynn. Who's the girl who was always with you? The one with the long brown hair."
    scene 05_196 with Dissolve(1)
    er "Oh come on. Don't tell me you can't remember her."
    er "To be fair... You probably wouldn't recognise her nowadays."
    er "She's changed a lot. She doesn't have those cute hamster cheeks anymore."
    er "But that's Lexi. My best friend!"
    if Alexis_Intro_Ignore == True:
        mc "Hmm... Can't really remember her."
        mc "{i}(I saw her somewhere though.){/i}"
        jump Week2_Monday_Erynn_Apartment_Ethan
    else:
        if Alexis_Friends == True:
            scene 05_195 with Dissolve(1)
            mc "Lexi? As in Alexis?"
            er "Yeah. See! I knew you'd remember."
            if Alexis_Sex == True:
                mc "{i}(I better keep it at that. Erynn doesn't have to know I've hooked up with Alexis.){/i}"
            else:
                mc "{i}(I better keep it at that. Erynn doesn't have to know I've met Alexis already.){/i}"
            jump Week2_Monday_Erynn_Apartment_Ethan
        else:
            stop music fadeout 1.0
            play music "Music/Battle_Rock2.mp3" volume 0.6
            mc "..."
            scene 05_195 with Dissolve(1)
            mc "Lexi? As in Alexis?"
            er "Yeah. See! I knew you'd remember."
            er "You have to see her now. I think there is another picture of her from a year ago or so. She's so pretty."
            er "Let's all go out together next time."
            scene 01_132 with Dissolve(1)
            n "Hahaha.."
            mc "..."
            scene 05_197 with Dissolve(1)
            mc "{i}(Alexis... Why?){/i}"
            mc "{i}(What is going on here? Is this all just...){/i}"
            mc "{i}(Fuck this shit!){/i}"
            jump Week2_Monday_Erynn_Apartment_Alexis

label Week2_Monday_Erynn_Apartment_Ethan:
    $ Week2_Monday_Erynn_Ethan = True
    n "*Ding-dong*"
    stop music fadeout 1.0
    play music "Music/Battle_Rock2.mp3" volume 0.6
    scene 05_188 with Dissolve(1)
    mc "Are you expecting someone?"
    er "No... Not really."
    er "Can you go check, please?"
    mc "Sure."
    scene 05_198 with Dissolve(1)
    mc "Uh?"
    mc "{i}(Is that... Ethan?){/i}"
    et "Who the hell are you? And what are you doing here?"
    er "[mc]? Who is it?"
    scene 05_199 with Dissolve(1)
    et "Wait... [mc]? Can it be? Is it really you? That little dweeb from back then?"
    et "Haha. How do I even remember you?"
    mc "..."
    et "What happened to your eye? Still a punching bag, huh? Some things just don't change."
    scene black with Dissolve(1)
    pause 2
    scene 05_200 with Dissolve(1)
    et "Just go away!"
    et "Erynn doesn't want to play with little kids like you."
    mc "But today is my..."
    scene 05_201 with vpunch
    et "But but but... Are you stupid? She doesn't want to see you. She doesn't like you."
    mc "..."
    et "LEAVE!"
    scene black with Dissolve(1)
    pause 2
    scene 05_202 with Dissolve(1)
    er "Ethan... What are you doing here?"
    et "Came to see you, of course. What did you do to this poor guy's eye, babe?"
    mc "{i}(Babe?){/i}"
    er "What?"
    scene 05_203 with Dissolve(1)
    mc "So this is how it is? With him?"
    er "No."
    mc "After all he... Never mind."
    scene 05_204 with Dissolve(1)
    mc "I'm out of here."
    et "Don't show up here again!"
    er "Wait!"
    er "This is not... [mc]... Please!"
    scene 05_205 with Dissolve(1)
    et "Let him be. He's good at running away."
    er "Ethan... Just shut up!"
    scene 05_206 with Dissolve(1)
    er "[mc]?"
    et "..."
    er "Let me pass!"
    et "We need to talk."
    er "We don't! We have nothing to talk about."
    et "I disagree."
    scene black with Dissolve(1)
    pause 2
    scene 05_207 with Dissolve(1)
    mc "{i}(What the fuck is wrong with this day? It's just one thing after another.){/i}"
    mc "AAAH!"
    jump Week2_Monday_Bar

label Week2_Monday_Erynn_Apartment_Alexis:
    scene 05_208 with Dissolve(1)
    er "Uh, [mc]... Where are you going?"
    er "[mc]?"
    mc "Something came up."
    er "Can't it wait? Food is almost..."
    scene 05_209 with Dissolve(1)
    er "[mc]?"
    er "..."
    er "What just happened?"
    scene 05_210 with Dissolve(1)
    mc "{i}(Who the fuck is this guy?){/i}"
    mc "{i}(Is that... Ethan?){/i}"
    mc "{i}(What is he doing here?){/i}"
    scene 05_211 with Dissolve(1)
    er "{i}(He was just looking at those pictures.){/i}"
    er "{i}(Did they upset him?){/i}"
    scene 05_212 with Dissolve(1)
    er "She's so pretty."
    er "Right... We still need to take our yearly picture at the tree."
    er "I have to ask [mc] if he can take the picture for us. I think he'd enjoy that!"
    er "I should call her later to see if she has time this week."
    scene 05_207 with Dissolve(1)
    mc "{i}(What the fuck is going on here?){/i}"
    mc "{i}(Does she know?){/i}"
    mc "{i}(Of course she knows. I told her about Erynn on the plane.){/i}"
    mc "{i}(Is this all just a big joke?){/i}"
    mc "AAAH!"
    scene black with Dissolve(1)
    pause 2
    scene 05_213 with Dissolve(1)
    mc "{i}(Good! She's working today.){/i}"
    a "Oh, hey! This is a nice surprise."
    a "What are you doing here? No school today?"
    scene 05_214 with Dissolve(1)
    a "Sorry I left so suddenly this mor..."
    a "Wait... Your eye? What happened?"
    menu:
        "Be Angry[KoGa3AutoWTChange1]{size=-4}(Alexis Points-2) {/size} {/color}":
            $ Alexis_Points -= 2
            scene 05_215 with Dissolve(1)
            mc "Oh... Now you care?"
            a "What? Did you try to call me? Sorry, I left my phone somewhere. So..."
            mc "Did you know?"
            a "What do you mean?"
            scene 05_216 with Dissolve(1)
            mc "Did you fucking know who I was, Alexis?"
            a "{i}(He knows... Why did I wait so long to tell him?){/i}"
            scene 05_217 with Dissolve(1)
            a "I'm sorry. I wanted... I tried to..."
            mc "Don't touch me!"
            a "[mc]..."
            scene 05_218 with Dissolve(1)
            mc "Since when? From the beginning?"
            a "No... I knew the moment you told me about Erynn."
            mc "..."
            mc "Oh yeah... That's such a difference."
            scene 05_219 with Dissolve(1)
            a "[mc], I can explain."
            mc "Oh yeah... You can explain, mom can explain, everyone can explain..."
            mc "If you didn't lie, to begin with, there wouldn't be any need for an explanation."
            a "{i}(His mom? Did she tell him? It looked like she didn't recognise me. What did she say?){/i}"
            scene 05_220 with Dissolve(1)
            mc "If I didn't find out, would you have ever told me?"
            a "I'm so sorry. I was scared. I didn't know how. Erynn is..."
            mc "Is this all just a big ongoing joke?"
            mc "[mc] is back, we can finally continue where we left off."
            a "What?"
            scene 05_221 with Dissolve(1)
            a "No... [mc]. Please!"
            mc "Then why? Is it so hard to tell me who you are?"
            a "..."
            a "Because I..."
            mc "..."
        "Ask her":
            scene 05_215 with Dissolve(1)
            mc "Nothing happened."
            a "But..."
            mc "Did you know?"
            a "What do you mean?"
            scene 05_216 with Dissolve(1)
            mc "Back on the plane. Did you know who I was?"
            a "{i}(He knows... Why did I wait so long to tell him?){/i}"
            scene 05_217 with Dissolve(1)
            a "I'm sorry. I tried to..."
            mc "..."
            a "[mc]..."
            scene 05_218 with Dissolve(1)
            mc "Since when? From the beginning?"
            a "No. I knew the moment you told me about Erynn."
            mc "..."
            scene 05_219 with Dissolve(1)
            a "[mc], I can explain."
            mc "If you didn't lie, to begin with, there wouldn't be any need for an explanation."
            a "Sorry... I just..."
            scene 05_220 with Dissolve(1)
            mc "If I didn't find out, would you have ever told me?"
            a "I'm so sorry. I was scared. I didn't know how. Erynn is..."
            mc "Is that a no?"
            scene 05_221 with Dissolve(1)
            a "No... [mc]. Please!"
            mc "Then why? Is it so hard to tell me who you are?"
            a "..."
            a "Because I..."
            mc "..."
    menu:
        "Leave":
            scene 05_222 with Dissolve(1)
            a "Where are you going?"
            if Alexis_Points >= 19:
                mc "I actually really liked you, Alexis. But now... I'm not so sure anymore."
            else:
                pass
            a "[mc]... Please let me explain."
            mc "..."
        "Angry response[KoGa3AutoWTChange1]{size=-4}(Alexis Points-2) {/size} {/color}":
            $ Alexis_Points -= 2
            scene 05_222 with Dissolve(1)
            mc "You know what? I don't even care anymore."
            mc "Fuck this! Fuck you, fuck everyone!"
            a "[mc]... Don't go! I can..."
            a "[mc]!"
    scene 05_223 with Dissolve(1)
    a "*Crying*"
    if Alexis_Points >= 19:
        a "{i}(It's because I'm falling in love with you.){/i}"
    else:
        pass
    jump Week2_Monday_Bar

label Week2_Monday_Bar:
    scene black with Dissolve(1)
    pause 2
    stop music fadeout 1.0
    scene 05_224 with Dissolve(1)
    play music "Sounds/Bar_Background.mp3" volume 0.3
    bt "Hey, there. What can I get you?"
    mc "A beer, please."
    bt "Can I see some ID?"
    mc "Sure."
    scene 05_225 with Dissolve(1)
    bt "Here you go."
    mc "Thanks, man."
    scene 05_226 with Dissolve(1)
    mc "*Sigh*"
    mc "{i}(What now?){/i}"
    mc "{i}(This day is insane.){/i}"
    menu:
        "Keep drinking[KoGa3AutoWTChange1]{size=-4}(Week2 Monday Bar Stay) {/size} {/color}":
            $ Week2_Monday_Bar_Stay = True
            jump Week2_Monday_Gabi
        "Go to Erynn[KoGa3AutoWTChange1]{size=-4}(Erynn Week2 Monday GoToErynn, Gabi End, Erynn Points+2) {/size} {/color}":
            $ Erynn_Week2_Monday_GoToErynn = True
            $ Gabi_End = True
            $ Erynn_Points += 2
            # Erynn (14)
            jump Week2_Monday_GoToErynn
        "Call Zach[KoGa3AutoWTChange1]{size=-4}(Zach Week2 Monday House, Zach Week2 Monday Sister, Gabi End) {/size} {/color}":
            $ Zach_Week2_Monday_House = True
            $ Zach_Week2_Monday_Sister = True
            $ Gabi_End = True
            jump Week2_Monday_Zach

label Week2_Monday_Gabi:
    scene black with Dissolve(1)
    pause 2
    scene 05_227 with Dissolve(1)
    x "Whiskey, please!"
    x "And keep 'em coming."
    scene 05_228 with Dissolve(1)
    x "What?"
    mc "..."
    mc "{i}(I didn't say anything... Should I even?){/i}"
    mc "Shitty day?"
    scene 05_229 with Dissolve(1)
    bt "Here you go, miss."
    x "Thanks."
    x "The shittiest!"
    scene 05_230 with Dissolve(1)
    mc "Welcome to the club."
    x "..."
    x "Cheers."
    mc "To idiots like us."
    x "Heh..."
    scene 05_231 with Dissolve(1)
    x "What happened?"
    mc "Oh, this?"
    mc "I got..."
    scene 05_232 with Dissolve(1)
    x "Actually, never mind. I don't really care."
    mc "..."
    mc "{i}(Okay? Suit yourself...){/i}"
    scene 05_233 with Dissolve(1)
    x "..."
    scene 05_234 with Dissolve(1)
    x "You know what? I changed my mind. I want to know."
    mc "You sure?"
    x "Yeah! Entertain me."
    scene 05_235 with Dissolve(1)
    mc "Well..."
    mc "Got sucker punched in the face. Kneed in the stomach, then spit on."
    mc "Learned that my dad isn't actually my dad."
    if Alexis_Friends == True:
        mc "Found out that my childhood friend dates the guy who bullied me when I was younger."
    else:
        mc "Found out that the girl I'm seeing lied to me."
    x "..."
    scene 05_236 with Dissolve(1)
    x "You win."
    mc "I win?"
    x "Mm-hmm..."
    mc "{i}(Doesn't feel like I'm winning today...){/i}"
    scene black with Dissolve(1)
    pause 2
    scene 05_237 with Dissolve(1)
    x "Why are men always such idiots?"
    mc "You're asking the wrong guy..."
    scene black with Dissolve(1)
    pause 2
    scene 05_238 with Dissolve(1)
    mc "Haha..."
    x "Hey, bartender!"
    x "Another round for me and my friend here!"
    scene black with Dissolve(1)
    pause 2
    scene 05_239 with Dissolve(1)
    x "I'm a catch! Ain't I? Look at me!"
    x "I'm pretty. I'm smart. I dress nice."
    mc "I think so!"
    x "I can cook too, you know! So why..."
    scene black with Dissolve(1)
    pause 2
    stop music fadeout 1.0
    scene 05_240 with Dissolve(1)
    play music ("Music/LoFi Indie 3.mp3", "Music/LoFi Indie 1.mp3", "Music/LoFi Indie 2.mp3") volume 0.2
    mc "..."
    scene 05_241 with Dissolve(1)
    mc "{i}(Damn... My head's pounding like crazy.){/i}"
    mc "{i}(How much did I drink last night?){/i}"
    scene 05_242 with Dissolve(1)
    mc "..."
    mc "{i}(Wait... Where the hell am I?){/i}"
    mc "{i}(How did I even end up here? I can't remember anything.){/i}"
    scene 05_243 with Dissolve(1)
    mc "Uh..."
    mc "{i}(Who's this?){/i}"
    mc "{i}(I've seen her before, I think. Why am I so bad with faces?){/i}"
    mc "{i}(Seriously... What happened last night? Did we..?){/i}"
    menu:
        "Lift blanket":
            scene 05_244 with Dissolve(1)
            mc "{i}(She's naked, alright.){/i}"
            mc "*Sigh*"
            mc "{i}(Did we have sex? We probably did... I wish I'd remember.){/i}"
            scene 05_245 with Dissolve(1)
            mc "{i}(At least she's pretty, I guess?){/i}"
        "Leave it be":
            mc "*Sigh*"
    scene 05_246 with Dissolve(1)
    mc "{i}(Okay... Think!){/i}"
    mc "{i}(I went to the bar, had a beer, and then... Nothing. Just blank.){/i}"
    mc "..."
    mc "{i}(Oh, shit. I was at Erynns' place before.){/i}"
    mc "{i}(What time is it? My phone... It should be in my pants...){/i}"
    mc "{i}(Where are my clothes?){/i}"
    scene 05_247 with Dissolve(1)
    mc "{i}(Fuck!){/i}"
    mc "{i}(She's probably worried sick...){/i}"
    mc "{i}(I need to get out of here.){/i}"
    scene black with Dissolve(1)
    pause 2
    scene 05_248 with Dissolve(1)
    mc "{i}(Oh, no... She's married?){/i}"
    mc "{i}(Shit shit shit! What did I do?){/i}"
    mc "{i}(I'm lucky her husband didn't walk in.){/i}"
    mc "{i}(Otherwise I'd be leaving with a couple black eyes instead of one... Or worse.){/i}"
    mc "*Shakes head*"
    scene 05_249 with Dissolve(1)
    mc "{i}(Goodbye, beautiful stranger.){/i}"
    mc "{i}(Sorry about whatever this was.){/i}"
    $ renpy.end_replay()
    jump Week2_Monday_GoToErynn2

label Week2_Monday_Zach:
    scene 05_250 with Dissolve(1)
    z "Hey, [mc]."
    mc "Hey."
    z "What's up?"
    mc "Drama!"
    z "Oh... Girl drama?"
    scene 05_251 with Dissolve(1)
    mc "All kinds of drama..."
    z "Sounds bad. Where you at?"
    mc "Some bar."
    mc "Listen... Any chance I can crash at your place tonight?"
    z "Yeah, man. Of course. Just come over."
    scene 05_252 with Dissolve(1)
    mc "Thanks. I’ll be there in like half an hour."
    z "Cool. I'll grab a couple of dad's beers in the meantime."
    mc "Heh... See you."
    z "Later."
    scene black with Dissolve(1)
    pause 2
    stop music fadeout 1.0
    scene 05_253 with Dissolve(1)
    play music ("Music/LoFi Indie 3.mp3", "Music/LoFi Indie 1.mp3", "Music/LoFi Indie 2.mp3") volume 0.2
    z "Welcome to the love dungeon. The place where all the good stuff happens, if you know what I mean."
    mc "{i}(I don't even wanna know...){/i}"
    mc "Uh... I think this room itself could use some love."
    mc "Seems like it hasn't changed in the last ten years."
    scene 05_254 with Dissolve(1)
    z "Of course not. It has everything I need."
    mc "Okay... Just don't invite any girls here."
    z "What? Why not? They'll love this."
    mc "{i}(Oh boy.){/i}"
    mc "Anyway... Thanks for letting me crash here. Your parents are fine with it?"
    z "Of course, they are. I'll get us those beers."
    mc "Cool."
    scene black with Dissolve(1)
    pause 2
    scene 05_255 with Dissolve(1)
    z "Here you go."
    mc "Thanks."
    scene 05_256 with Dissolve(1)
    mc "Is your sister also here?"
    z "Why are you asking about her all of a sudden? Do you have a thing for her?"
    mc "Heh... No. Just curious. Haven't seen her in a long time."
    z "You must have met her. She works as a receptionist at our school."
    mc "Oh... That's Natasha? I didn't recognise her at all..."
    z "Well, she moved out a long time ago. I think you must have been eight years old when you last saw her."
    scene 05_257 with Dissolve(1)
    mc "It has been that long already?"
    z "Yeah... So, what's all your drama about? Is that why you have a black eye?"
    mc "Part of it. But I just don't know anymore. So much stuff going on."
    mc "Honestly, I just want to forget everything for a day."
    z "I have an idea. I just got this new game. Protocol: Shadow Veil, a multiplayer shooter. Wanna play a few rounds?"
    mc "Sure."
    scene 05_258 with Dissolve(1)
    z "Let's kick some ass and be totally toxic to those little wannabe pro gamers."
    mc "You know... Ten years ago, we were those little wannabes."
    z "Yeah, and we got flamed like there was no tomorrow... Now it's our turn."
    z "Come on! This will be so much fun."
    mc "Haha. Sure... Why not."
    scene black with Dissolve(1)
    pause 2
    scene 05_259 with Dissolve(1)
    z "Take that you camping bitch!"
    z "Teabagging your ass!"
    z "How does it feel to have my balls in your face?"
    mc "*Shakes head*"
    scene 05_260 with Dissolve(1)
    x "Fuck you! You're so lucky. My gun wouldn't shoot."
    menu:
        "Ignore":
            mc "..."
            x "What? Don't you have a mic?"
            x "You're so bad at this game. Such a loser!"
            mc "{i}(Haha, this guy.){/i}"
            x "Oh my god, FUCK YOU! YOU FUCKING LUCKER!"
            mc "{i}(Haha... Why did he pick XxNoScopeGodxX as his name? He better starts aiming or he won't hit shit!){/i}"
        "React":
            mc "The only thing that was lucky was your conception."
            z "Haha."
            x "What? You're so bad at this game."
            mc "I'm not the one with 17 deaths."
            x "FUCK YOU! That's all your fault."
            mc "Well yeah, I've shot you so many times."
            scene 05_261 with Dissolve(1)
            x "Just SHUT THE FUCK UP!"
            mc "Haha..."
            x "You laugh now, but I was laughing when I fucked your mom!"
            mc "Oh... That was you?"
            x "Yeah that was me!"
            mc "Hey, dad. Funny to meet you here of all places."
            z "Haha. I can't play like that. Dude's too funny!"
    scene black with Dissolve(2)
    pause 2
    scene 05_262 with Dissolve(1)
    z "*Snoring*"
    mc "{i}(Oh man... I've such a headache.){/i}"
    mc "{i}(What time is it anyway.){/i}"
    scene 05_263 with Dissolve(1)
    mc "{i}(Oh shit...){/i}"
    mc "{i}(I'd better head over to Erynn's and apologise.){/i}"
    mc "{i}(She's probably worried sick...){/i}"
    scene 05_264 with Dissolve(1)
    z "*Snoring*"
    mc "{i}(Thanks for letting me stay.){/i}"
    mc "{i}(I'll let you sleep and see you later at school.){/i}"
    jump Week2_Monday_GoToErynn2

label Week2_Monday_GoToErynn:
    scene black with Dissolve(1)
    pause 2
    stop music fadeout 1.0
    scene 05_265 with Dissolve(1)
    play music ("Music/LoFi Indie 3.mp3", "Music/LoFi Indie 1.mp3", "Music/LoFi Indie 2.mp3") volume 0.2
    n "*Knock-knock*"
    scene 05_266 with Dissolve(1)
    mc "Hey!"
    er "Oh... You're back!"
    er "Are you alright?"
    mc "..."
    scene 05_267 with Dissolve(1)
    er "Hey, what's wrong?"
    mc "*Sigh* I don't know."
    if Week2_Monday_Erynn_Ethan == True:
        er "Hey. Listen. I'm so sorry about Ethan. I didn't know he was coming."
        er "And nothing's going on between us. I promise. It was job-related."
        mc "{i}(Job-related? What does Ethan have to do with modelling?){/i}"
        mc "I might have overreacted, too. Sorry. I just don't like that guy."
    else:
        mc "It's just... All the stuff that happened today."
        er "I understand."
        mc "Sorry to be such a downer."
    scene 05_268 with Dissolve(1)
    er "It's alright."
    er "Come on in."
    if Week2_Monday_Erynn_Ethan == False:
        scene 05_269 with Dissolve(1)
        er "I have to tell you something. Ethan was here when you left."
        mc "{i}(I knew it was him!){/i}"
        mc "{i}(At least someone is honest today.){/i}"
        mc "Yeah. I saw him in the hallway."
        scene 05_270 with Dissolve(1)
        er "You did? Did he say anything to you?"
        mc "No. Nothing... Maybe he didn't recognise me."
        er "{i}(Trust me. He did. He was fuming...){/i}"
        mc "What did he want? Are you two?"
        scene 05_271 with Dissolve(1)
        er "No! Nothing like that... It was... job-related."
        mc "Hmm... Okay."
        mc "{i}(Job-related? What does Ethan have to do with modelling?){/i}"
        er "Are you still hungry?"
    else:
        er "Are you still hungry?"
    scene 05_272 with Dissolve(1)
    mc "I don't have an appetite at the moment. Sorry for making you cook for nothing."
    er "It's fine... Don't worry. Now we have something to eat for tomorrow, right?"
    mc "Heh, yeah."
    er "What do you want to do now? Watch some TV?"
    mc "Sure."
    scene black with Dissolve(1)
    pause 2
    scene 05_273 with Dissolve(1)
    er "What do you normally watch?"
    mc "Besides sports..."
    mc "I actually haven't watched much TV lately."
    scene 05_274 with Dissolve(1)
    er "Okay... Let's see if we can find something."
    mc "You don't have to. Just switch to something you enjoy."
    er "I don't mind."
    er "Oh, look! Basketball! You like basketball, right?"
    if Erynn_Points >= 11:
        mc "I do."
        scene 05_275 with Dissolve(1)
        er "That better be your answer in 3 years!"
        mc "Heh, what?"
        er "Never mind... Stupid joke."
    else:
        mc "I do."
    scene 05_276 with Dissolve(1)
    er "Do you still play any sports? You used to play football, right?"
    mc "Uh-huh. But I joined the track and field team at my new school."
    er "Oh... Interesting! Are you any good?"
    menu:
        "I do alright":
            mc "Yeah. I'm doing alright I guess."
            scene 05_277 with Dissolve(1)
            er "How come you chose track and field?"
            mc "Hmm... I enjoy running and people at training always told me that I'm really fast."
            mc "So, I thought... Why not give track a shot?"
        "Joke":
            mc "The best!"
            er "Oh, really? The best?"
            mc "Uh-huh."
            scene 05_278 with Dissolve(1)
            er "Haha... I need to see that first. Maybe the others are just slow!"
            mc "Wow... You can be really mean sometimes."
            er "Haha."
            mc "But... That could be a possibility."
            scene 05_279 with Dissolve(1)
            er "How come you chose track and field?"
            mc "Well... I had so many girls chasing after me that I actually became really good at running."
            if Erynn_Points >= 11:
                er "Is that right?"
                scene 05_280 with Dissolve(1)
                er "Would you run away from me if I chased you?"
                mc "Uh?"
                er "I'm kidding."
                mc "You really need to work on your jokes."
                er "Haha."
                er "..."
            else:
                er "Is that right?"
    scene 05_281 with Dissolve(1)
    mc "How about you? Do you play any sports?"
    er "No... Not anymore. I did play volleyball though, in high school."
    mc "Oh yeah. I remember. Didn't you want to join the college team?"
    er "I was thinking about that. But then I started modelling, so I didn't really have time for it."
    mc "Bummer... Would've loved to see you play!"
    er "..."
    scene black with Dissolve(1)
    pause 2
    scene 05_282 with Dissolve(1)
    mc "Nice!"
    er "Touch down!"
    mc "..."
    scene 05_283 with Dissolve(1)
    mc "*Shakes head*"
    er "Haha..."
    er "I know it's a basket... I only wanted to see your reaction."
    er "Totally worth it!"
    er "But some people call it a goal. Which is a little weird, right?"
    scene 05_284 with Dissolve(1)
    mc "Oh come on! How can you miss that easy lay-up?"
    er "{i}(He's cute when he's annoyed.){/i}"
    scene 05_285 with Dissolve(1)
    mc "..."
    scene 05_286 with Dissolve(1)
    er "..."
    if Erynn_Points >= 11:
        scene 05_287 with Dissolve(1)
        er "..."
    else:
        pass
    scene black with Dissolve(1)
    pause 2
    scene 05_288 with Dissolve(1)
    mc "Just look at that!"
    mc "Why does he keep shooting? He hasn't made a single basket."
    mc "Freakin' pass the ball or sit down! Seriously!"
    show 05_289
    pause 2
    mc "Heh... Tired or bored?"
    er "Definitely not bored."
    mc "You can go to bed if you want."
    er "I'm good for now."
    mc "Or we can watch something else..."
    er "No-no... Keep watching. I'm just going to rest my eyes for a bit."
    scene 05_290 with Dissolve(1)
    ""
    scene black with Dissolve(1)
    pause 2
    scene 05_291 with Dissolve(1)
    mc "Erynn?"
    mc "..."
    mc "{i}(Only resting your eyes, huh?){/i}"
    scene 05_292 with Dissolve(1)
    mc "{i}(You shouldn't let your guard down like this...){/i}"
    mc "{i}(Someone could take advantage of that.){/i}"
    mc "*Sigh*"
    mc "{i}(I'd better carry her to her bed.){/i}"
    scene 05_293 with Dissolve(1)
    mc "{i}(She must be very tired.){/i}"
    mc "{i}(She isn't even waking up now...){/i}"
    if Nikki_FB_Club_Carry == False:
        pass
    else:
        mc "{i}(She's not pretending like Nikki always did, right?){/i}"
        mc "{i}(At least I don't have to carry her up some stairs...){/i}"
        mc "{i}(She's lighter than Nikki, too.){/i}"
    scene 05_294 with Dissolve(1)
    ""
    scene 05_295 with Dissolve(1)
    mc "*Sigh*"
    mc "{i}(I should've moved the duvet first...){/i}"
    mc "{i}(Hope she doesn't wake up now...){/i}"
    scene 05_296 with Dissolve(1)
    mc "{i}(Good night, Erynn.){/i}"
    mc "{i}(Now... Where should I sleep?){/i}"
    menu:
        "Couch":
            scene black with Dissolve(1)
            pause 2
            scene 05_297 with Dissolve(1)
            mc "{i}(Damn... I should've picked the bed. This couch is way too small.){/i}"
        "Bed[KoGa3AutoWTChange1]{size=-4}(Erynn Week2 Monday Bed, Erynn Points+2) {/size} {/color}":
            $ Erynn_Week2_Monday_Bed = True
            $ Erynn_Points += 2
            # Erynn (16)
            scene 05_298 with Dissolve(1)
            mc "{i}(I hope you don't mind, Erynn.){/i}"
            mc "{i}(But this is much more comfortable than your small couch.){/i}"
    jump Week2_Tuesday

label Week2_Monday_GoToErynn2:
    scene black with Dissolve(1)
    pause 2
    scene 05_265 with Dissolve(1)
    n "*Knock-knock*"
    mc "{i}(I hope she won't be too angry that I'm waking her up.){/i}"
    scene 05_299 with Dissolve(1)
    mc "Hey, Erynn. I'm so..."
    er "[mc]! You just left. I tried to call you, but you... So I thought..."
    mc "I'm sorry, Erynn."
    scene 05_300 with Dissolve(1)
    er "Are you alright?"
    mc "More or less, yeah."
    er "Did something happen? Uhm... Come on in."
    scene 05_301 with Dissolve(1)
    if Week2_Monday_Erynn_Ethan == True:
        er "Hey. Listen. I'm so sorry about Ethan. I didn't know he was coming."
        er "And nothing's going on between us. I promise. It was job-related."
        mc "{i}(Job-related? What does Ethan have to do with modelling?){/i}"
        mc "*Sigh* I might have overreacted, too. Sorry. I just don't like that guy."
    else:
        er "I have to tell you something. Ethan was here when you left."
        mc "{i}(I knew it was him!){/i}"
        mc "{i}(At least someone is honest today.){/i}"
        mc "Yeah. I saw him in the hallway."
        scene 05_302 with Dissolve(1)
        er "You did? Did he say anything to you?"
        mc "No... Nothing. Maybe he didn't recognise me."
        er "{i}(Trust me. He did. He was fuming...){/i}"
        mc "What did he want? Are you two?"
        scene 05_303 with Dissolve(1)
        er "No! Nothing like that... It was... job-related."
        mc "Hmm, okay."
        mc "{i}(Job-related? What does Ethan have to do with modelling?){/i}"
        scene 05_304 with Dissolve(1)
        er "*Yawn*"
        mc "Tired?"
        er "Yeah."
        scene 05_305 with Dissolve(1)
        mc "Were you awake this whole time?"
        er "I couldn't sleep. You didn't answer your phone and..."
        mc "Sorry..."
        scene 05_306 with Dissolve(1)
        mc "You can go to bed now. Try to at least get a few hours in before you need to wake up."
        er "Aren't you tired?"
        mc "I am. I'll make myself comfortable on the couch."
        er "You can sleep in my bed. There's enough space."
        menu:
            "Couch":
                scene black with Dissolve(1)
                pause 2
                scene 05_297 with Dissolve(1)
                mc "{i}(Damn... I should've picked the bed. This couch is way too small.){/i}"
            "Bed[KoGa3AutoWTChange1]{size=-4}(Erynn Week2 Monday Bed, Erynn Points+2) {/size} {/color}":
                $ Erynn_Week2_Monday_Bed = True
                $ Erynn_Points += 2
                scene 05_298 with Dissolve(1)
                mc "{i}(Yeah, she is right.){/i}"
                mc "{i}(This is much more comfortable than the couch.){/i}"
        jump Week2_Tuesday

label Week2_Tuesday:
    scene black with Dissolve(2)
    pause 2
    n "Tuesday, 07:30. Erynn's apartment."
    if Erynn_Week2_Monday_Bed == True:
        if Erynn_Points >= 13:
            scene 05_307 with Dissolve(1)
            er "..."
            scene 05_308 with Dissolve(1)
            er "Good morning, cutie."
            if Erynn_Week2_Monday_GoToErynn == True:
                er "Snuck into my bed, huh?"
                er "Lucky for you. I don't mind!"
                er "You're the only boy who can sleep in my bed."
            else:
                pass
            scene 05_309 with Dissolve(1)
            er "..."
            scene 05_310 with Dissolve(1)
            er "{i}(Sorry... I had to!){/i}"
            er "{i}(I'll keep this a secret, though.){/i}"
            scene black with Dissolve(1)
            pause 2
        else:
            scene 05_307 with Dissolve(1)
            er "..."
            scene 05_308 with Dissolve(1)
            er "Good morning."
            er "{i}(I'll let him sleep a bit longer.){/i}"
            scene black with Dissolve(1)
            pause 2
        scene 05_311 with Dissolve(1)
        mc "{i}(Hmm. She's up early. Maybe she left already for classes?){/i}"
        if Alexis_Friends == False:
            mc "{i}(*Sigh* What a day yesterday... Was I too harsh on Alexis? A lot happened yesterday and I kind of took everything out on her. Maybe I should've listened to her explanation?){/i}"
            mc "{i}(But then again. Why did she hide this? Was it because of Erynn?){/i}"
            mc "{i}(I don't know. Maybe it's better this way.){/i}"
            mc "{i}(And then the same with Mom.){/i}"
            mc "..."
            mc "{i}(Fuck!){/i}"
        else:
            mc "{i}(Stupid headache!){/i}"
            mc "{i}(Was I too harsh on Mom? Why did they keep this from me?){/i}"
            mc "..."
            mc "{i}(Fuck!){/i}"
        scene 05_312 with Dissolve(1)
        mc "{i}(Let's take a quick shower. I guess I'll be smelling like a girl today.){/i}"
        mc "{i}(Erynn always smells good... It won't be too bad, I guess...){/i}"
        scene 05_313 with Dissolve(1)
        mc "Oh!"
        er "..."
        scene 05_314 with Dissolve(1)
        er "Aah... [mc]!"
        mc "I'm so sorry, Erynn!"
        mc "I thought you left already and..."
        er "[mc]! Now is not the time for small talk."
        er "Can you please leave and close the door."
        scene 05_315 with Dissolve(1)
        menu:
            "Joke":
                mc "I thought girls don't poop..."
                er "Ew! I'm not poo..."
                mc "Hey! Nothing to be ashamed of. I guess I should've read the book called 'Everyone poops'!"
                er "[mc], STOP! This is not funny!"
                er "Let's just forget about this, please. This never happened!"
            "Sorry":
                mc "Sorry, Erynn!"
                er "Let's just forget about this, please. This never happened!"
                mc "..."
                mc "{i}(I give other people shit about not knocking, and now I do it myself.){/i}"
                mc "{i}(I'm such a hypocrite!){/i}"
    else:
        scene 05_316 with Dissolve(1)
        if Alexis_Friends == False:
            mc "{i}(*Sigh* What a day yesterday... Was I too harsh on Alexis? A lot happened yesterday and I kind of took everything out on her. Maybe I should've listened to her explanation?){/i}"
            mc "{i}(But then again. Why did she hide this? Was it because of Erynn?){/i}"
            mc "{i}(I don't know. Maybe it's better this way.){/i}"
            mc "{i}(And then the same with Mom.){/i}"
            mc "..."
            mc "{i}(Fuck!){/i}"
        else:
            mc "{i}(Stupid headache!){/i}"
            mc "{i}(Was I too harsh on Mom? Why did they keep this from me?){/i}"
            mc "..."
            mc "{i}(Fuck!){/i}"
    scene black with Dissolve(1)
    pause 2
    scene 05_317 with Dissolve(1)
    mc "{i}(*Sigh* I hope this day will be better than yesterday.){/i}"
    play sound "Sounds/Phone_Vibrate.mp3"
    n "*Bzzzt. Bzzzt.*"
    scene 05_318 with Dissolve(1)
    if Andres_FB_Punch == True:
        mc "{i}(Oh... It's Nikki.){/i}"
        menu:
            "Ignore":
                mc "{i}(Sorry, but I'm really not in the best headspace to talk to you right now.){/i}"
            "Pick up":
                scene 05_319 with Dissolve(1)
                mc "Hey, Nikki."
                mc "How are you?"
                scene 05_320 with Dissolve(1)
                ni "Hey, [mc]... I'm good, thank you. How about you?"
                mc "*Sigh*"
                ni "Oh-oh. That was a big sigh!"
                scene 05_321 with Dissolve(1)
                mc "Yeah... Not that good at this moment, to be honest."
                ni "How come?"
                mc "Hmm... A lot has happened the last few days and I'm not so sure anymore if I made the right decision of coming back here."
                scene 05_322 with Dissolve(1)
                ni "That bad?"
                mc "I just don't know."
                scene 05_323 with Dissolve(1)
                ni "You're always welcome to live with us again."
                mc "Thank you... But that would be a bit weird, no?"
                ni "Well... We miss you!"
                mc "I miss you, too."
                scene 05_324 with Dissolve(1)
                c "Who's that?"
                ni "It's [mc]."
                scene 05_325 with Dissolve(1)
                c "Oh... Hey, [mc]!"
                c "How are you? We miss you!"
                ni "Did you hear that?"
                scene 05_326 with Dissolve(1)
                mc "Hehe, yeah..."
                mc "Hey, Cara!"
                ni "He says hi back."
                scene 05_327 with Dissolve(1)
                ni "It's so quiet without you in the house."
                mc "I doubt that. I know you two. You're anything but quiet!"
                ni "Haha."
                scene 05_328 with Dissolve(1)
                ni "Did you hear from your dad after what happened here?"
                mc "No... Nothing. And listen to this. Supposedly, he isn't even my real dad."
                ni "Wait... What?"
                mc "Yeah. I don't know myself yet. As I said. A lot of things happened."
                scene 05_329 with Dissolve(1)
                ni "You weren't kidding."
                ni "How did you find out?"
                mc "Mom dropped this bomb when we had an argument."
                ni "That's all you know?"
                mc "For now, yes."
                ni "I think you really should talk to your mom about that."
                scene 05_330 with Dissolve(1)
                mc "I know, but now isn't the right time."
                ni "It's never the right time with something like that."
                mc "You might be right!"
                scene 05_331 with Dissolve(1)
                ni "I really want to talk some more but I have to get ready for work. I'm sorry..."
                mc "That's fine. I need to get ready for school anyway."
                mc "It was good to hear from you, Nikki. I really needed to hear a friendly voice."
                ni "Anytime. If you need to talk, just call me. I'm here for you."
                mc "Thank you. Say hello to Haley for me!"
                ni "Will do. Bye, [mc]."
                mc "Bye, Nikki."
                scene 05_332 with Dissolve(1)
                mc "{i}(Nice of her to call.){/i}"
                mc "{i}(Actually perfect timing...){/i}"
                mc "{i}(That made me feel so much better already.){/i}"
    else:
        if Cara_Girlfriend == True:
            mc "{i}(Oh... It's Cara.){/i}"
            menu:
                "Ignore":
                    mc "{i}(I'm sorry, but I'm really not in the best headspace to talk to you right now.){/i}"
                "Pick up[KoGa3AutoWTChange1]{size=-4}(Cara Week2 Tuesday Phonecall) {/size} {/color}":
                    $ Cara_Week2_Tuesday_Phonecall = True
                    scene 05_319 with Dissolve(1)
                    mc "Hey, Cara. How are you?"
                    scene 05_335 with Dissolve(1)
                    c "Hey, [mc]... I'm good, thank you. How about you?"
                    mc "*Sigh*"
                    c "Oh-oh. That was a big sigh!"
                    scene 05_321 with Dissolve(1)
                    mc "Yeah... Not that good at the moment, to be honest."
                    c "How come?"
                    mc "Hmm. A lot has happened the last few days and I'm not so sure anymore if I made the right decision of coming back here."
                    scene 05_336 with Dissolve(1)
                    c "That bad?"
                    mc "I just don't know."
                    scene 05_337 with Dissolve(1)
                    c "Well, you're always welcome to live with us again."
                    mc "Thank you."
                    c "I... We miss you!"
                    mc "I miss you, too."
                    scene 05_338 with Dissolve(1)
                    ni "Who's that?"
                    c "It's [mc]."
                    scene 05_339 with Dissolve(1)
                    ni "Oh! Hey [mc]. How are you? We miss you!"
                    c "Did you hear that?"
                    scene 05_340 with Dissolve(1)
                    mc "Hehe, yeah..."
                    mc "Hey, Nikki!"
                    c "He says hi back."
                    scene 05_341 with Dissolve(1)
                    c "It's so quiet without you in the house."
                    mc "I doubt that. I know you two. You're anything but quiet!"
                    c "Haha."
                    scene 05_342 with Dissolve(1)
                    c "Our parents are getting married this weekend. Time flies, huh?"
                    mc "Wait... That's this weekend? I totally forgot."
                    c "Haha, That's what I thought. Hence this reminder."
                    c "You're coming, right?"
                    mc "I don't know yet. With all that has been going on here."
                    scene 05_343 with Dissolve(1)
                    c "No. It's your dad's marriage."
                    mc "{i}(Supposedly he isn't even my dad, but I shouldn't tell her that over the phone.){/i}"
                    c "You have to come! [mc]... Please!"
                    c "This will be good. You can clear your head too."
                    mc "You might be right. I'll let you know tomorrow, okay?"
                    scene 05_334 with Dissolve(1)
                    c "You better!"
                    c "Well, I really want to talk some more but I have to get ready to go to the dentist, I'm sorry."
                    mc "That's fine. I need to get ready for school anyway."
                    c "We'll talk tomorrow then, right?"
                    mc "I'll call you."
                    c "Good!"
                    scene 05_344 with Dissolve(1)
                    mc "Nice to hear from you, Cara. I really needed to hear a friendly voice."
                    c "Anytime. If you need to talk, just call me. I'm here for you."
                    mc "Thank you. Say hello to our parents for me!"
                    c "Will do. Bye, [mc]."
                    mc "Bye, Cara."
                    scene 05_332 with Dissolve(1)
                    mc "{i}(Nice of her to call.){/i}"
                    mc "{i}(Actually perfect timing...){/i}"
                    mc "{i}(That made me feel so much better already.){/i}"
        else:
            mc "{i}(Oh... It's Nikki.){/i}"
            menu:
                "Ignore":
                    mc "{i}(I'm sorry, but I'm really not in the best headspace to talk to you right now.){/i}"
                "Pick up[KoGa3AutoWTChange1]{size=-4}(Nikki Week2 Tuesday Phonecall) {/size} {/color}":
                    $ Nikki_Week2_Tuesday_Phonecall = True
                    scene 05_319 with Dissolve(1)
                    mc "Hey, Nikki. How are you?"
                    scene 05_320 with Dissolve(1)
                    ni "Hey, [mc]... I'm good, thank you. How about you?"
                    mc "*Sigh*"
                    ni "Oh-oh. That was a big sigh!"
                    scene 05_321 with Dissolve(1)
                    mc "Yeah... Not that good at the moment, to be honest."
                    ni "How come?"
                    mc "Hmm. A lot has happened the last few days and I'm not so sure anymore if I made the right decision of coming back here."
                    scene 05_322 with Dissolve(1)
                    ni "That bad?"
                    mc "I just don't know."
                    scene 05_323 with Dissolve(1)
                    ni "Well, you're always welcome to live with us again."
                    mc "Thank you."
                    ni "I... We miss you!"
                    mc "I miss you, too."
                    scene 05_324 with Dissolve(1)
                    c "Who's that?"
                    ni "It's [mc]."
                    scene 05_325 with Dissolve(1)
                    c "Oh... Hey, [mc]!"
                    c "How are you? We miss you!"
                    ni "Did you hear that?"
                    scene 05_326 with Dissolve(1)
                    mc "Hehe, yeah..."
                    mc "Hey, Cara!"
                    ni "He says hi back."
                    scene 05_327 with Dissolve(1)
                    ni "It's so quiet without you in the house."
                    mc "I doubt that. I know you two. You're anything but quiet!"
                    ni "Haha."
                    scene 05_333 with Dissolve(1)
                    ni "Our parents are getting married this weekend. Time flies, huh?"
                    mc "Wait... That's this weekend? I totally forgot."
                    ni "Haha, That's what I thought. Hence this reminder."
                    ni "You're coming, right?"
                    mc "I don't know yet. With all that has been going on here."
                    scene 05_329 with Dissolve(1)
                    ni "No. It's your dad's marriage."
                    mc "{i}(Supposedly he isn't even my dad, but I shouldn't tell her that over the phone.){/i}"
                    ni "You have to come! [mc]... Please!"
                    ni "This will be good. You can clear your head too."
                    mc "You might be right. I'll let you know tomorrow, okay?"
                    scene 05_334 with Dissolve(1)
                    ni "You better!"
                    ni "Well, I really want to talk some more but I have to get ready for work, I'm sorry."
                    mc "That's fine. I need to get ready for school anyway."
                    ni "We'll talk tomorrow then, right?"
                    mc "I'll call you."
                    ni "Good!"
                    scene 05_331 with Dissolve(1)
                    mc "Nice to hear from you, Nikki. I really needed to hear a friendly voice."
                    ni "Anytime. If you need to talk, just call me. I'm here for you."
                    mc "Thank you. Say hello to our parents for me!"
                    ni "Will do. Bye, [mc]."
                    mc "Bye, Nikki."
                    scene 05_332 with Dissolve(1)
                    mc "{i}(Nice of her to call.){/i}"
                    mc "{i}(Actually perfect timing...){/i}"
                    mc "{i}(That made me feel so much better already.){/i}"
    scene black with Dissolve(1)
    pause 2
    scene 05_345 with Dissolve(1)
    mc "Good morning!"
    er "Good morning. Are you going to wear the same clothes you wore yesterday?"
    mc "Uhm... I don't really have a choice, right? I didn't bring any clothes when I left."
    er "Your pants are fine. But that t-shirt... No. I can still smell the alcohol on it."
    mc "I guess I'll have to skip school then."
    scene 05_346 with Dissolve(1)
    er "What? No! You're not. I'm not letting you skip school."
    mc "Right... Then what am I supposed to wear? Shops aren't open yet. One of your t-shirts?"
    er "Yes!"
    mc "Haha. Stop joking."
    scene 05_347 with Dissolve(1)
    er "I might have something that will fit you."
    mc "Erynn!"
    er "Just wait... Let me check."
    er "I know I have some oversized shirts."
    mc "{i}(Oversized for you is probably still small for me...){/i}"
    scene 05_348 with Dissolve(1)
    er "Here! Why don't you try this one for now?"
    er "This might look good on you!"
    mc "..."
    scene 05_349 with Dissolve(1)
    mc "Really, Erynn?"
    er "Haha... I'm just kidding. Let me check again."
    mc "You're really enjoying this, huh?"
    er "Haha. Is it that obvious?"
    menu:
        "Try it on[KoGa3AutoWTChange1]{size=-4}(Erynn Week2 Tuesday Shirt, Erynn Points+2) {/size} {/color}":
            $ Erynn_Week2_Tuesday_Shirt = True
            $ Erynn_Points += 2
            # Erynn (18)
            scene 05_350 with Dissolve(1)
            mc "Well... You won't believe this, but..."
            mc "It actually fits."
            er "What?"
            scene 05_351 with Dissolve(1)
            er "[mc]!"
            er "There's no way..."
            mc "What do you think? Yay or nay?"
            scene 05_352 with Dissolve(1)
            er "Haha. I don't know what to say. That is uh... Yeah, I'm speechless!"
            mc "That good, huh?"
            er "Uh-huh."
            er "I guess it's yours now."
            scene 05_353 with Dissolve(1)
            mc "Got some underwear too?"
            er "Haha, sure! What's your bra size?"
            scene 05_354 with Dissolve(1)
            if Erynn_Week1_Cupsize == False:
                mc "..."
                mc "Not the reaction I expected."
                er "Oh... You meant panties?"
                mc "Erynn..."
            else:
                mc "32C!"
                er "Haha... Someone paid attention."
            scene 05_355 with Dissolve(1)
            er "While we're at it. Want me to do your make-up too?"
            mc "Okay... Enough. Let's be serious for a second."
            scene 05_356 with Dissolve(1)
            mc "I'm just gonna wear my t-shirt and switch to my gym shirt at school."
            er "Really? I have a nice skirt that would look good with that tank top, though."
            mc "..."
            er "*Sigh* Okay-okay. I'll stop."
        "Don't wear it":
            scene 05_357 with Dissolve(1)
            er "Hmm... I don't really have anything here. Those t-shirts must be at Mom's house."
            mc "I'll switch this one for my gym shirt at school. It will be fine."
            er "*Sigh* Okay..."
    scene black with Dissolve(1)
    pause 2
    scene 05_358 with Dissolve(1)
    er "Can you come sit down here for a second?"
    if Erynn_Week2_Tuesday_Shirt == True:
        mc "You're not gonna put make-up on me, Erynn."
        er "I wasn't. Just a little bit of conceiler to hide your bruise."
        mc "Hmm... Okay."
    else:
        er "I'm gonna hide your bruise."
        mc "Uhm... Okay."
    scene 05_359 with Dissolve(1)
    er "I'm gonna make you look pretty again."
    mc "Heh..."
    mc "Don't I look like a badass like this?"
    er "No. You look like someone who got beaten up."
    mc "Haha."
    if Erynn_Points >= 15:
        scene 05_360 with Dissolve(1)
        er "..."
        mc "{i}(Damn... She's so pretty...){/i}"
        mc "{i}(I can look into her eyes for hours.){/i}"
    else:
        pass
    scene black with Dissolve(1)
    pause 2
    scene 05_361 with Dissolve(1)
    er "All done."
    mc "Thanks."
    er "Go check it the mirror if you're happy with it."
    scene 05_362 with Dissolve(1)
    mc "Oh wow..."
    mc "Like nothing was even there."
    mc "You did a great job. Thanks, Erynn."
    er "*Nods*"
    scene 05_363 with Dissolve(1)
    er "I need to go now. I don't have a spare key that I can give you, though."
    er "So you won't be able to get in when I'm not here."
    mc "That's fine. When do your classes end?"
    er "At five."
    mc "Okay... Uh... I'll figure something out. I'll see you then."
    menu:
        "Don't hug":
            scene 05_364 with Dissolve(1)
            er "Bye, [mc]."
            mc "Bye, Erynn. See you later."
        "Hug[KoGa3AutoWTChange1]{size=-4}(Erynn Points+2) {/size} {/color}":
            scene 05_365 with Dissolve(1)
            $ Erynn_Points += 2
            # Erynn (20)
            er "Bye, [mc]."
            mc "Bye, Erynn. See you later."
    jump Week2_Tuesday_School_Natasha

label Week2_Tuesday_School_Natasha:
    if _in_replay:
        $ Zach_Week2_Monday_House = True
    scene black with Dissolve(2)
    pause 2
    stop music fadeout 1.0
    play music ("Music/LoFi Upbeat 1.mp3", "Music/LoFi Upbeat 2.mp3", "Music/LoFi Upbeat 3.mp3", "Music/LoFi Upbeat 4.mp3") volume 0.2
    n "Tuesday, 08:26. School."
    scene 05_366 with Dissolve(2)
    mc "{i}(Erynn was right. This shirt really stinks of alcohol.){/i}"
    mc "{i}(Good thing I leave a spare workout shirt here.){/i}"
    mc "{i}(Let's change real quick.){/i}"
    scene 05_367 with Dissolve(1)
    mc "{i}(This will do for today, I guess.){/i}"
    mc "{i}(There wasn't a dress code for class, right?){/i}"
    mc "{i}(Reminder to finally read the student handbook.){/i}"
    x "Mmm... Yeah, keep going."
    scene 05_368 with Dissolve(1)
    mc "{i}(What was that? Is someone here?){/i}"
    x "Yeah. Right there!"
    mc "{i}(What's going on?){/i}"
    x "Ooh... Mike!"
    mc "{i}(Mike? Wait... Coach? With whom?){/i}"
    scene 05_369 with Dissolve(1)
    if Zach_Week2_Monday_House == False:
        mc "{i}(Oh shit! With the receptionist who has the hots for him.){/i}"
        mc "{i}(And here of all places. Aren't they worried they'll be seen? Or rather caught...){/i}"
    else:
        mc "{i}(Oh shit! That's Zach's sister... Natasha... With Coach!){/i}"
        mc "{i}(And here of all places. Aren't they worried they'll be seen? Or rather caught...){/i}"
        mc "{i}(Does Zach know?){/i}"
    menu:
        "Leave":
            mc "{i}(Okay... Let's leave before they notice someone else is here...){/i}"
            $ renpy.end_replay()
        "Keep watching[KoGa3AutoWTChange1]{size=-4}(Natasha Week2 Tuesday MikeSex) {/size} {/color}":
            $ Natasha_Week2_Tuesday_MikeSex = True
            scene 05_370 with Dissolve(1)
            mc "{i}(I should leave, but...){/i}"
            mc "{i}(This is pretty hot, actually.){/i}"
            mc "{i}(I'll stay and watch for a few seconds. No longer!){/i}"
            scene 05_371 with Dissolve(1)
            mc "{i}(Not bad...){/i}"
            mc "{i}(I'd suck on those.){/i}"
            scene 05_372 with vpunch
            re "..."
            mc "{i}(Shit!){/i}"
            scene 05_373 with Dissolve(1)
            mc "{i}(Did she see me?){/i}"
            mc "{i}(Of course, she saw me... She was looking straight at me...){/i}"
            mc "{i}(Fuck!){/i}"
            re "*Moaning*"
            mc "{i}(But why isn't she telling coach to stop?){/i}"
            scene 05_374 with Dissolve(1)
            mc "{i}(She's still looking at me...){/i}"
            mc "{i}(Does she want me to watch?){/i}"
            mc "{i}(Maybe this turns her on?){/i}"
            mc "{i}(This is so crazy... I should leave, but somehow I want to stay and...){/i}"
            scene 05_375 with Dissolve(1)
            re "Oh, yes... Fuck me harder, Mike!"
            mc "{i}(She definitely wants me to keep watching...){/i}"
            re "Yes!"
            show 05_376
            ""
            show 05_377
            ""
            show 05_378
            ""
            scene 05_379 with Dissolve(1)
            re "Ahhh..."
            mc "{i}(I'd love to stay longer... But I better leave before coach figures out what's going on.){/i}"
            if Zach_Week2_Monday_House == False:
                mc "{i}(I hope to see more of you one day, receptionist lady...){/i}"
            else:
                mc "{i}(I hope to see more of you one day, Natasha...){/i}"
            $ renpy.end_replay()
    jump Week2_Tuesday_School

label Week2_Tuesday_School:
    scene black with Dissolve(1)
    pause 2
    scene 05_380 with Dissolve(1)
    mc "*Shakes head*"
    mc "{i}(That was something else...){/i}"
    mc "{i}(Before heading to class... I should try to look for Layla and apologise for not replying yesterday to all of her texts.){/i}"
    scene 05_381 with Dissolve(1)
    mc "{i}(And there she is...){/i}"
    mc "{i}(Perfect.){/i}"
    scene 05_382 with Dissolve(1)
    el "Oh, look! He actually came today."
    el "Hey..."
    la "[mc]!"
    mc "Hi, girls."
    scene 05_383 with Dissolve(1)
    la "How are you?"
    if Layla_Points >= 25:
        mc "I'm good. How..."
        scene 05_384 with Dissolve(1)
        la "I was so worried. I texted and tried to call you."
        mc "Yeah... Sorry about that. A lot happened and I..."
        la "It's okay."
        scene 05_385 with Dissolve(1)
        la "Your eye looks so much better already."
        mc "{i}(Thanks, Erynn.){/i}"
        la "Does it still hurt?"
        mc "No... It's fine."
    else:
        mc "I'm good. How about you guys?"
        el "Peachy."
        la "Also good. Your eye looks better. Does it still hurt?"
        mc "No... It's fine."
        mc "{i}(Thanks, Erynn.){/i}"
    scene 05_386 with Dissolve(1)
    la "Can you tell me what happened?"
    if Layla_Week2_Monday_Wait == False:
        mc "*Sigh* The guy you argued with in the park last week. Well... He punched me."
        la "Wait... Lucas?"
        mc "I think? I don't know his name."
        scene 05_387 with Dissolve(1)
        la "Why would he punch you?"
        mc "He said to stay away from you. That you're just toying with me and you guys are getting back together once you graduate. And all kinds of rubbish."
        el "Why is he still? He's so delusional!"
        scene 05_388 with Dissolve(1)
        la "This is all my fault..."
        la "And now I dragged you into this mess."
        scene 05_389 with Dissolve(1)
        mc "Uh... Layla?"
        el "Layla, wait!"
        scene 05_390 with Dissolve(1)
        el "Why did you tell her that?"
        mc "I didn't know that was supposed to be a secret."
        el "*Sigh* I knew this would happen..."
        jump Week2_Tuesday_School_Layla_Bathroom
    else:
        jump Week2_Tuesday_School_Layla

label Week2_Tuesday_School_Layla:
    el "*Shaking Head*"
    menu:
        "Lie[KoGa3AutoWTChange1]{size=-4}(Layla Week2 Tuesday Lie, Layla Week2 Tuesday Sergeant) {/size} {/color}":
            $ Layla_Week2_Tuesday_Lie = True
            $ Layla_Week2_Tuesday_Sergeant = True
            scene 05_391 with Dissolve(1)
            mc "Hmm. Nothing special. I just fell very awkwardly and bumped my head."
            la "Oh... That's it?"
            mc "Wow! You sound very disappointed. Thank you!"
            scene 05_392 with Dissolve(1)
            la "Haha, no... I thought someone might have hit you."
            la "As you can see. I was already dressed for war."
            mc "{i}(Haha... This girl is so cute.){/i}"
            scene black with Dissolve(1)
            transform moveup:
                xalign 0.5 yalign 1.0
                linear 5.0 yalign 0.0
            show 05_393 at moveup
            pause 3
            mc "{i}(I really like those skin-tight clothes on her.){/i}"
            la "Are you checking me out?"
            scene 05_394 with Dissolve(1)
            mc "Haha. You look very... warlike, Private Layla."
            la "I told you I'm ready for war! And it's Sergeant!"
            mc "I'm so sorry, Sergeant."
            el "Dios Mío..."
            scene 05_395 with Dissolve(1)
            el "I'm going to class. Good luck with Spanish."
            la "Heh... Yeah. Later, Elena."
            el "Bye."
            mc "See you."
            scene 05_396 with Dissolve(1)
            la "We should go, too."
            menu:
                "Let's go":
                    mc "Yes. Let's go."
                "Joke":
                    mc "Yeah... You can't miss your favourite class, right?"
                    mc "Ándale, ándale!"
                    scene 05_397 with Dissolve(1)
                    la "Ha...Ha... Very funny."
                    la "I know what that means, by the way!"
                    mc "Muy buena!"
                    la "..."
            jump Week2_Tuesday_School_Spanish
        "Tell her[KoGa3AutoWTChange1]{size=-4}(Elena Points-2) {/size} {/color}":
            $ Elena_Points -= 2
            mc "{i}(I don't want to lie to her... Sorry, Elena){/i}"
            mc "*Sigh* The guy you argued with in the park last week. Well... He punched me."
            el "..."
            la "Wait... Lucas?"
            mc "Yeah."
            scene 05_387 with Dissolve(1)
            la "Why would he punch you?"
            mc "He said to stay away from you. That you're just toying with me and you guys are getting back together once you graduate. And all kinds of rubbish."
            scene 05_388 with Dissolve(1)
            la "This is all my fault..."
            la "And now I dragged you into this mess."
            scene 05_389 with Dissolve(1)
            mc "Uh... Layla?"
            el "Layla, wait!"
            scene 05_390 with Dissolve(1)
            el "Why did you tell her? I asked you not to."
            mc "Sorry... I don't want to lie to her."
            el "Sometimes a little white lie is better than the truth!"
            el "*Sigh* I knew this would happen."
            scene 05_398 with Dissolve(1)
            mc "I think she should know. Now she'll be more careful around him."
            el "Yeah... You're right. It would be stupid to keep it from her. She would probably find out anyway."
            el "Sorry that I asked you..."
            mc "Don't worry."
            jump Week2_Tuesday_School_Layla_Bathroom

label Week2_Tuesday_School_Layla_Bathroom:
    menu:
        "Go after her[KoGa3AutoWTChange1]{size=-4}(Layla Points+2, Elena Points+2) {/size} {/color}":
            $ Layla_Points += 2
            # Layla (36)
            $ Elena_Points += 2
            # Elena (14)
            scene 05_399 with Dissolve(1)
            mc "I'll talk to her."
            el "Thank you. I have to go to class. Don't let her skip Spanish. She can't fail that class."
            mc "I won't. I'll drag her there if I have to."
            el "Haha."
            mc "Later, Elena."
            el "Bye."
            scene 05_404 with Dissolve(1)
            mc "{i}(*Sigh* Why do girls always run into the bathroom?){/i}"
            mc "{i}(Tough luck, Layla. This isn't going to stop me!){/i}"
            scene 05_405 with Dissolve(1)
            x "HEY! What are you doing here? This is the girls' bathroom."
            menu:
                "Joke":
                    mc "Yeah. I know. Can't you see? I'm a girl."
                    x "Really?"
                    x "..."
                    x "Aren't you leaving?"
                    mc "No!"
                    x "Idiot!"
                "Sorry":
                    mc "Sorry. I just need to talk to someone."
                    x "Can't you wait until she comes out?"
                    mc "It's really important."
                    x "Hmm... Okay. Be quick, though."
                    mc "Thank you!"
            mc "Layla?"
            scene 05_406 with Dissolve(1)
            mc "Have you seen her?"
            x "I think she's in the second to last stall."
            scene black with Dissolve(1)
            transform moveup:
                xalign 0.5 yalign 1.0
                linear 5.0 yalign 0.0
            show 05_407 at moveup
            pause 3
            mc "{i}(Haven't seen her before...){/i}"
            mc "Thank you."
            x "No worries."
            scene 05_408 with Dissolve(1)
            mc "Layla?"
            mc "Can you open up, please?"
            la "..."
            mc "It's not your fault!"
            la "It is..."
            scene 05_409 with Dissolve(1)
            mc "You weren't even there. How could you know what he'd do?"
            mc "Please... Open up. Or I'll climb over the door. Your choice."
            la "You're bluffing."
            scene 05_410 with Dissolve(1)
            if Layla_Week1_Saturday_Beach_Slap == False:
                mc "Do you really want to test me?"
            else:
                mc "Do you really want to test me again?"
                mc "Remember what happened at the beach?"
                la "Uh..."
            la "What if I'm... on the toilet?"
            mc "Are you?"
            n "*Click*"
            scene 05_411 with Dissolve(1)
            la "Sorry."
            mc "It's not your fault."
            la "I don't know what to do anymore."
            if Layla_Week2_Monday_LucasHelp == True:
                mc "You don't have to do anything. I'll figure something out, okay?"
                scene 05_412 with Dissolve(1)
                la "But..."
                mc "Let me handle it please."
                mc "Come on, let's go."
            else:
                scene 05_412 with Dissolve(1)
                mc "It will be fine. Don't worry about that guy anymore."
                mc "Come on. let's go."
            scene 05_413 with Dissolve(1)
            la "Thank you!"
            mc "Sure. I can't have you miss your favourite class... Spanish!"
            mc "Ándale, ándale!"
            scene 05_414 with Dissolve(1)
            la "Ha...Ha... Very funny."
            la "I know what that means, by the way!"
            mc "Muy buena!"
            la "..."
            scene 05_415 with Dissolve(1)
            $ Layla_Week2_Tuesday_Sergeant = True
            mc "By the way... I like your camo top."
            la "Yeah? Thanks."
            la "When I saw your eye yesterday... The first thing I thought was that someone must've hit you."
            la "So, I came dressed today, ready for war."
            scene 05_416 with Dissolve(1)
            mc "Haha. Thanks for having my back, Private Layla."
            la "Uhm... It's Sergeant!"
            mc "Oh, I'm sorry. Sergeant Layla!"
            if Layla_Points >= 29:
                scene 05_417 with Dissolve(1)
                la "..."
            else:
                pass
            jump Week2_Tuesday_School_Spanish
        "Leave her be":
            scene 05_400 with Dissolve(1)
            el "Let me handle it. I'll talk to her."
            mc "Okay... I'll wait here."
            mc "Sorry, Elena."
            scene black with Dissolve(2)
            pause 2
            scene 05_401 with Dissolve(1)
            el "And we are back."
            mc "Hey. Are you okay?"
            la "Yeah. Sorry."
            scene 05_402 with Dissolve(1)
            el "I'm going to class. Good luck with Spanish."
            la "Heh... Later, Elena."
            el "Bye."
            mc "See you."
            scene 05_403 with Dissolve(1)
            mc "Don't worry about it, okay?"
            la "*Nods*"
            mc "Let's learn some Spanish."
            jump Week2_Tuesday_School_Spanish

label Week2_Tuesday_School_Spanish:
    scene black with Dissolve(1)
    pause 2
    scene 05_418 with Dissolve(1)
    x "Buenos días, Layla."
    la "Morning."
    x "En español por favor."
    la "Días."
    x "*Sigh*"
    if Gabi_End == True:
        scene 05_419 with Dissolve(1)
        x "Buenos días!"
        x "Debes ser el estudiante nuevo.\n(You must be the new student.)"
        mc "Sí. Buenos días."
        scene 05_420 with Dissolve(1)
        tr "Soy Gabriela Ramirez, tu profesora de español.\n(I'm Gabriela Ramirez, your Spanish teacher.)"
        mc "Mucho gusto, soy [mc].\n(Nice to meet you. I'm [mc].)"
        tr "{i}(His pronunciation is on point. Is he bi-lingual?){/i}"
        tr "Por favor, toma asiento.\n(Please take a seat.)"
        jump Week2_Tuesday_School_Spanish2
    else:
        jump Week2_Tuesday_School_Gabi

label Week2_Tuesday_School_Gabi:
    if _in_replay:
        $ SexCounter_Gabi = 0
        $ MC_SexCounter = 0
    $ SexCounter_Gabi += 1
    $ MC_SexCounter += 1
    scene 05_421 with Dissolve(1)
    x "Beunos dí..."
    x "..."
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 05_422 at moveup
    pause 3
    mc "{i}(She looks very familiar.){/i}"
    mc "..."
    mc "{i}(Wait... Is that? There's just no way.){/i}"
    mc "{i}(Oh no!){/i}"
    scene black with Dissolve(2)
    pause 2
    n "The day before. 23:34."
    scene 05_423 with Dissolve(1)
    mc "Damn... My head is spinning. What about you?"
    mc "..."
    scene 05_424 with Dissolve(1)
    mc "Hey... Are you alright?"
    x "Uh... Yeah... I might have drunk one too many."
    mc "Oh, you too? That last one always gets you, huh?"
    mc "Come on... I'll take you home."
    scene black with Dissolve(1)
    pause 2
    scene 05_425 with Dissolve(1)
    ""
    scene 05_426 with Dissolve(1)
    x "*Stumbles*"
    mc "Be careful..."
    x "Haha. Why? I have you, to catch me."
    mc "Heh..."
    mc "{i}(If this continues, she won't be home before breakfast.){/i}"
    mc "{i}(I better call her an uber.){/i}"
    scene 05_427 with Dissolve(1)
    mc "Give me a second. Just try not to fall."
    x "What are you doing?"
    mc "Calling an uber to get you home."
    mc "{i}(Hmm... How do I do this? Never used this app before.){/i}"
    mc "Have you ever called an uber?"
    scene 05_428 with Dissolve(1)
    x "No... I don't need a ride. I live close by!"
    x "It's just around the corner."
    mc "Okay."
    scene black with Dissolve(1)
    pause 2
    scene 05_429 with Dissolve(1)
    x "It's this one here."
    mc "*Nods*"
    scene 05_430 with Dissolve(1)
    x "Thank you. This would've been much harder without you."
    mc "You're welcome. Don't forget to drink lots of water or you'll end up having an headache tomorrow."
    mc "{i}(She probably will. Even with drinking lots of water. We both will!){/i}"
    x "Are you worried about me?"
    mc "Uhm... A little?"
    x "..."
    scene 05_431 with Dissolve(1)
    x "You're actually very cute."
    mc "Thanks?"
    scene 05_432 with vpunch
    mc "{i}(Uh?){/i}"
    mc "{i}(What is she..?){/i}"
    mc "{i}(A thank you for bringing her home?){/i}"
    scene 05_433 with Dissolve(1)
    mc "What are you doing?"
    x "I want you to make me feel good..."
    mc "..."
    x "Can you make me feel good?"
    mc "{i}(Fuck it!){/i}"
    scene 05_434 with Dissolve(1)
    x "Mmm..."
    x "{i}(I told you many times I need affection.){/i}"
    x "{i}(And if I won't get it from you... I'll get it from someone else.){/i}"
    scene 05_435 with Dissolve(1)
    ""
    scene 05_436 with Dissolve(1)
    x "..."
    scene 05_437 with Dissolve(1)
    x "Come!"
    x "{i}(That's what you get if you never have time for me and work all the time!){/i}"
    x "{i}(Can't remember when I was this excited.){/i}"
    scene 05_438 with Dissolve(1)
    mc "{i}(We're really doing this, huh?){/i}"
    mc "{i}(She's wasting no time...){/i}"
    mc "{i}(Straight to the point. I quite like it.){/i}"
    scene 05_439 with Dissolve(1)
    mc "{i}(I thought she was pretty when she was sitting next to me at the bar...){/i}"
    mc "{i}(Now seeing her here...){/i}"
    mc "{i}(She's gorgeous!){/i}"
    mc "{i}(I know I should be undressing too, but I just can't keep my eyes off her.){/i}"
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 05_440 at moveup
    pause 3
    mc "{i}(The way she looks at me right now...){/i}"
    mc "{i}(And then this body... Damn!){/i}"
    scene 05_441 with Dissolve(1)
    x "..."
    mc "*Shakes head*"
    mc "You're so sexy!"
    scene 05_442 with Dissolve(1)
    mc "{i}(Fuck...){/i}"
    scene 05_443 with Dissolve(1)
    x "{i}(Yes... Touch me! Touch me all you want.){/i}"
    x "{i}(Feeling his hands on my body gives me goosebumps.){/i}"
    x "{i}(How long has it been..?){/i}"
    scene 05_444 with Dissolve(1)
    mc "So you want me to make you feel good?"
    x "*Nods*"
    scene 05_445 with Dissolve(1)
    x "Mmm..."
    scene 05_446 with Dissolve(1)
    x "..."
    x "Touch me more!"
    scene 05_447 with Dissolve(1)
    ""
    scene 05_448 with Dissolve(1)
    ""
    scene 05_449 with vpunch
    mc "Uh..."
    scene 05_450 with Dissolve(1)
    x "..."
    scene 05_451 with Dissolve(1)
    x "Take me however you want!"
    mc "{i}(That just turned me on even more!){/i}"
    scene 05_452 with Dissolve(1)
    x "We should skip the rest of the foreplay."
    x "I want you to put it in and fuck me!"
    mc "*Nods*"
    scene 05_453 with Dissolve(1)
    ""
    scene 05_454 with Dissolve(1)
    x "..."
    scene 05_455 with Dissolve(1)
    x "Ahh..."
    x "*Whispers* Finally..."
    scene 05_456 with Dissolve(1)
    x "Mmm..."
    show 05_457
    ""
    show 05_458
    x "Ah-ah-ah..."
    x "Yes!"
    show 05_459
    ""
    scene 05_460 with Dissolve(1)
    x "*Moaning*"
    x "Keep going!"
    scene 05_461 with Dissolve(1)
    x "..."
    x "Why are you stopping?"
    mc "Turn around."
    scene 05_462 with Dissolve(1)
    ""
    scene 05_463 with Dissolve(1)
    mc "{i}(If I didn't stop there for a second. I would've finished already...){/i}"
    mc "{i}(Her pussy is so good!){/i}"
    mc "{i}(But maybe not the smartest decision to take her doggy...){/i}"
    mc "{i}(Look at that ass!){/i}"
    show 05_464
    ""
    show 05_465
    ""
    show 05_466
    ""
    show 05_467
    ""
    scene 05_468 with Dissolve(1)
    mc "{i}(I can't hold it for much longer...){/i}"
    menu:
        "Pull out[KoGa3AutoWTChange1]{size=-4}(Gabi Week2 Tuesday Pullout) {/size} {/color}":
            $ Gabi_Week2_Tuesday_Pullout = True
            scene 05_469 with vpunch
            pause 2
            scene 05_470 with vpunch
            mc "{i}(Fuck...){/i}"
            n "*Heavy breathing*"
        "Cum inside":
            scene 05_471 with vpunch
            pause 2
            scene 05_472 with vpunch
            mc "{i}(Fuck...){/i}"
            n "*Heavy breathing*"
    $ renpy.end_replay()
    scene black with Dissolve(1)
    pause 2
    scene 05_473 with Dissolve(1)
    mc "{i}(We sure did...){/i}"
    x "Uhm... Buenos días."
    x "Debes ser el estudiante nuevo.\n(You must be the new student.)"
    mc "Sí. Buenos días."
    scene 05_474 with Dissolve(1)
    x "{i}(I can't believe I had sex with a student. This is bad.){/i}"
    x "{i}(I'm not just going to lose my teaching license. Let's hope he can keep a secret.){/i}"
    x "{i}(I better talk to him after class.){/i}"
    x "{i}(Let's just concentrate on the lesson for now.){/i}"
    scene 05_475 with Dissolve(1)
    tr "Soy Gabriela Ramirez, tu profesora de español.\n(I'm Gabriela Ramirez, your Spanish teacher.)"
    mc "{i}(So, her name is Gabriela...){/i}"
    mc "Mucho gusto, soy [mc].\n(Nice to meet you. I'm [mc].)"
    tr "{i}(His pronunciation is on point. Is he bi-lingual?){/i}"
    scene 05_476 with Dissolve(1)
    tr "Por favor, toma asiento.\n(Please take a seat.)"
    mc "*Nods*"
    mc "{i}(This is going to be very... something.){/i}"
    scene 05_477 with Dissolve(1)
    tr "*Sigh*"
    scene 05_478 with Dissolve(1)
    tr "..."
    jump Week2_Tuesday_School_Spanish2

label Week2_Tuesday_School_Spanish2:
    scene 05_479 with Dissolve(1)
    mc "Días? Really?"
    la "What? It means morning, right?"
    mc "Heh... Eres linda.\n(You're cute.)"
    scene 05_480 with Dissolve(1)
    la "Uhm... Excuse me?"
    la "It's Layla! Not Linda!"
    mc "Haha. I can't..."
    scene 05_481 with Dissolve(1)
    tr "Tranquilo por favor.\n(Calm down, please.)"
    mc "Sí, lo siento.\n(Yes, I'm sorry.)"
    scene 05_482 with Dissolve(1)
    mc "I think it's time we start those private lessons."
    la "..."
    la "What does it mean then?"
    mc "I don't know. Ask the teacher."
    la "Oh... You think I won't?"
    scene 05_483 with Dissolve(1)
    la "Miss Ramirez... What does..."
    tr "En español, Layla."
    la "..."
    scene 05_484 with Dissolve(1)
    la "{i}(*Sigh* What was it again?){/i}"
    la "Eres linda!"
    tr "Uhm... Gracias, Layla."
    tr "{i}(Where did that come from?){/i}"
    tr "Por favor, presta atención ahora.\n(Please pay attention now.)"
    scene 05_485 with Dissolve(1)
    mc "Haha... *Whispers* I thought you didn't like the teacher?"
    la "*Whispers* Why are you laughing? What did I just say?"
    mc "*Whispers* You told her she's cute."
    la "What? Oh my god! [mc]!"
    scene 05_486 with Dissolve(1)
    tr "Por favor, guarda silencio. Última advertencia!\n(Please be quiet. Last warning!)"
    scene 05_487 with Dissolve(1)
    if Layla_Week1_Monday_Payattention == True:
        mc "Haha."
        la "*Whisper* Okay... We can play this game! Just wait."
    else:
        mc "*Whisper* Haha. That was payback for geography!"
        la "*Whisper* Okay... We can play this game!"
    scene black with Dissolve(1)
    pause 2
    n "One hour later."
    scene 05_488 with Dissolve(1)
    la "*Sigh* Even more homework and then the test next week. I'm going to fail this class."
    mc "Hey... You're not!"
    la "Mom is going to be so mad."
    mc "You won't fail, Layla. I'll help you out. We've got this."
    mc "Come on... Let's get out of here."
    scene 05_489 with Dissolve(1)
    la "Do you have time this week?"
    mc "I..."
    if Gabi_End == True:
        tr "Layla. Can I speak with you, please?"
        scene 05_490 with Dissolve(1)
        la "Uh? Sure..."
        mc "I'll wait outside."
        la "Okay, thank you."
        scene black with Dissolve(1)
        pause 2
        scene 05_491 with Dissolve(1)
        mc "That was quick. What did she want from you?"
        la "She offered me some private lessons, so I won't fail this class."
        scene 05_492 with Dissolve(1)
        mc "That's pretty nice of her."
        la "Heh... Nice... Yeah right..."
        la "She's just trying to suck up to my... To the principal."
    else:
        tr "[mc]... Can I speak with you, please?"
        scene 05_493 with Dissolve(1)
        mc "Uh? Sure."
        la "I'll wait outside."
        mc "Okay, thank you."
        scene 05_494 with Dissolve(1)
        tr "Uhm... I didn't know you were a student."
        tr "No... That doesn't even matter..."
        tr "Listen... *Sigh* it was a mistake."
        scene 05_495 with Dissolve(1)
        tr "That should never have happened..."
        tr "I just had a bad day. I was lonely and drank too much."
        tr "{i}(*Sigh* Why am I telling this boy all that?){/i}"
        tr "The reason doesn't really matter, right? Nothing will change what happened."
        scene 05_496 with Dissolve(1)
        tr "I need you to keep this a secret. I'll lose my job and..."
        mc "Don't worry about it. I'll keep my mouth shut."
        scene 05_497 with Dissolve(1)
        tr "Thank you, [mc]."
        scene 05_498 with Dissolve(1)
        tr "..."
        scene 05_499 with Dissolve(1)
        tr "Uhm... Sorry."
        tr "I didn't mean to make it even more awkward."
        mc "It's fine. If there's nothing else, I think I should leave now..."
        tr "*Nods*"
        mc "Bye, Ms Ramirez."
        scene 05_500 with Dissolve(1)
        tr "*Sigh* Dammit dammit, dammit..."
        tr "{i}(How could I have been so stupid?){/i}"
        tr "{i}(Can I really trust him? I hope he keeps his promise.){/i}"
        tr "{i}(And why did I hug him?){/i}"
        scene 05_501 with Dissolve(1)
        mc "Hey. Thanks for waiting."
        la "Sure. What did she want from you?"
        mc "Uh..."
        mc "{i}(Shit! What do I say? I don't want to lie to her but I can't really tell her that we...){/i}"
        mc "She was impressed with my Spanish skills and asked me if I could help you out."
        la "She did?"
        scene 05_502 with Dissolve(1)
        mc "Yeah... Pretty nice of her to think about you, huh?"
        la "Heh... Nice... Yeah right. She's just trying to suck up to my... To the principal."
    scene 05_503 with Dissolve(1)
    la "Let's go to the track?"
    mc "Yeah. I'm so ready to run. Lots of energy I need to spend."
    la "Hehe... You'd better beat Darryl again then."
    mc "Not just Darryl."
    la "Do you want to do some stretching together before the warm-up?"
    mc "Sure."
    n "*Ding-dong*"
    scene 05_504 with Dissolve(1)
    re "Can [mc] Moreno come to the principal's office."
    la "Uhm?"
    mc "What? Again?"
    re "I repeat. [mc] Moreno to the principal's office, please."
    mc "{i}(I hope it's not about what I saw in the locker room.){/i}"
    if Layla_Points >= 27:
        scene 05_505 with Dissolve(1)
    else:
        scene 05_506 with Dissolve(1)
    la "Just go. Don't let her wait. You'd better stay on her good side."
    mc "Seems like you know the principal very well."
    la "Yeah... You can say that. I've been in her office many times."
    mc "Oh? So, there's a little rebel inside of you?"
    la "Maybe..."
    mc "Okay. See you later then, I guess. Don't start stretching without me, though."
    scene 05_507 with Dissolve(1)
    la "I'll wait for you."
    mc "Just look at this amazing stretch. I'm so good at stretching."
    la "Haha... [mc]!"
    scene black with Dissolve(1)
    pause 2
    scene 05_508 with Dissolve(1)
    mc "Good morning, Principal Moore."
    am "Good morning, [mc]."
    scene 05_509 with Dissolve(1)
    mc "Uhm..."
    am "Don't worry. You didn't do anything wrong. I just called you here to check up on you."
    am "How is your eye doing?"
    mc "It's fine."
    scene 05_510 with Dissolve(1)
    am "Yeah... It's healed pretty well already. You can barely notice it."
    am "That's good."
    am "I called your mother yesterday."
    scene 05_511 with Dissolve(1)
    mc "What..? Uhm... You didn't have..."
    am "It's procedure."
    scene 05_512 with Dissolve(1)
    am "Seemed like she didn't know what happened. You haven't told her?"
    mc "No... Something else came up."
    am "She sounded really worried. So, please tell her what happened."
    mc "*Nods* Yeah..."
    scene 05_513 with Dissolve(1)
    am "Well... That's it actually. Or is there anything else you want to tell me?"
    mc "*Shakes head*"
    am "Alright. You can go back to class then."
    am "And [mc]... If there ever is something you want to talk to me about... My door is always open. Please, don't hesitate."
    mc "Thank you."
    scene 05_514 with Dissolve(1)
    am "*Sigh*"
    am "{i}(I have a feeling that more is going on...){/i}"
    am "{i}(I better keep an eye on him. Things can turn bad quickly.){/i}"
    jump Week2_Tuesday_School_Cafeteria

label Week2_Tuesday_School_Cafeteria:
    scene black with Dissolve(1)
    pause 2
    n "Tuesday, 12:17. School cafeteria."
    scene 05_515 with Dissolve(1)
    la "Hey! Don't worry about it. You'll beat Darryl next time."
    mc "*Sigh* Yeah... But now I have to listen to his gloating the whole day."
    mc "I don't know what happened. I was thinking about... something and I completely missed the start."
    scene 05_516 with Dissolve(1)
    mc "Did you see his stupid victory dance?"
    la "Haha... I did."
    mc "Like what was that? Was that really necessary?"
    scene 05_517 with Dissolve(1)
    mc "Eh-eeh-eh-ehh..."
    mc "Fucking idiot!"
    la "Hahaha..."
    scene 05_518 with Dissolve(1)
    mc "*Sigh*"
    mc "Good thing you beat Tori, though. You were amazing."
    la "Thank you, [mc]."
    mc "What classes do you have in the afternoon?"
    scene 05_519 with Dissolve(1)
    la "English and history. Bleh..."
    la "What about you?"
    mc "Also English and... Detention."
    if Layla_Week2_Detention == True:
        scene 05_520 with Dissolve(1)
        la "Oh, Right... You weren't in detention yesterday. I missed you there."
        mc "Yeah... About that. Sorry, you got detention because of me."
        scene 05_521 with Dissolve(1)
        la "It wasn't your fault."
        mc "Well... I have detention every day this week. You're welcome to join me."
        la "Haha. Thanks, but no thanks. My mom was angry enough yesterday."
    else:
        scene 05_520 with Dissolve(1)
        la "Oh Right. You have detention. For a whole week..."
        mc "Yeah. Don't remind me."
    scene 05_522 with Dissolve(1)
    la "Oh... That reminds me. What did Mo... Uh... Principal Moore want from you?"
    mc "She just wanted to check up on how I was doing."
    mc "She's actually really nice. I like her."
    scene 05_523 with Dissolve(1)
    la "{i}(That's good.){/i}"
    la "Heh... She can be nice. As long as you're on her good side. She's very strict."
    mc "Yeah. I somehow got that feeling about her, too."
    el "Hey, guys."
    scene 05_524 with Dissolve(1)
    la "Hey, Elena."
    mc "Hi..."
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 05_525 at moveup
    pause 3
    mc "{i}(Oh, damn...){/i}"
    el "Sorry, I'm late."
    la "*Shakes head* Don't worry about it."
    scene 05_526 with Dissolve(1)
    el "I can't stay, though. I just came to tell you that the squad has some meetings during lunch break. So just eat without me."
    la "Ah, okay. Have fun."
    el "Yeah, thanks."
    scene 05_527 with Dissolve(1)
    el "..."
    el "What are you looking at?"
    mc "Just haven't seen you in your cheerleading outfit yet..."
    scene 05_528 with Dissolve(1)
    el "Hmm..."
    el "So... What do you think?"
    menu:
        "Hot[KoGa3AutoWTChange1]{size=-4}(Elena Week2 Tuesday CheerHot) {/size} {/color}":
            $ Elena_Week2_Tuesday_CheerHot = True
            mc "You're making it difficult to look away. It's hot!"
            if Layla_Points >= 27:
                la "..."
            else:
                pass
            el "Heh... Thank you..."
            el "Training camp is coming soon... So you'll be seeing a lot more of me in this."
            menu:
                "Joke":
                    scene 05_529 with Dissolve(1)
                    mc "Oh joy... More Elena. That's what everyone wants!"
                    if Elena_Points >= 11:
                        el "Don't pretend you don't like me."
                    else:
                        el "Haha."
                "Can't wait":
                    scene 05_529 with Dissolve(1)
                    mc "Can't wait to see you cheer!"
                    el "Then you better start winning your races. I saw you earlier against Darryl."
                    mc "Wow, Elena... What a low blow. I complimented you and that's what I get?"
                    el "Haha. You know me."
        "Meh":
            scene 05_530 with Dissolve(1)
            mc "Meh... Doesn't really do it for me."
            el "Is that right? Then why are you still looking me up?"
            mc "..."
            el "Besides... You better get used to it."
            scene 05_529 with Dissolve(1)
            el "Training camp is coming soon. So you'll be seeing a lot more of me in this."
            mc "Oh joy..."
    scene 05_531 with Dissolve(1)
    el "By the way... While we are on the subject. Why are you still wearing your gym shirt? Don't you shower after you're done running?"
    mc "I do but I didn't have a spare shirt."
    el "So you'll wear your sweaty one all day?"
    mc "Didn't really have a choice."
    scene 05_532 with Dissolve(1)
    el "Layla! You can't let him run around like this. This way he'll never make friends and he'll keep hanging around us with his smelly clothes."
    la "Elena!"
    mc "Wow thanks, Elena. You're like a gift that keeps on giving."
    la "I don't mind lending him my clothes but they won't really fit him."
    scene 05_533 with Dissolve(1)
    el "You know what? Wait here. I'll get you something."
    mc "Uhm... Thanks but yours won't fit me either."
    el "*Sigh* Just wait!"
    menu:
        "Check her out[KoGa3AutoWTChange1]{size=-4}(Layla Points-4) {/size} {/color}":
            $ Layla_Points -= 4
            scene 05_534 with Dissolve(1)
            la "Really, [mc]?"
            mc "{i}(Shit. That was maybe a bit too obvious.){/i}"
            scene 05_535 with Dissolve(1)
            la "Was that really necessary?"
            mc "Sorry."
        "Don't":
            scene 05_536 with Dissolve(1)
            mc "Somehow I have a bad feeling about this."
            la "Haha. I can't wait to see what she comes up with."
    scene black with Dissolve(1)
    pause 2
    scene 05_537 with Dissolve(1)
    el "Here!"
    mc "Uhm... Thanks, Elena."
    mc "What's this?"
    el "It's a cheerleading uniform for guys."
    menu:
        "Joke[KoGa3AutoWTChange1]{size=-4}(Elena Week2 Tuesday RecruitJoke) {/size} {/color}":
            $ Elena_Week2_Tuesday_RecruitJoke = True
            scene 05_538 with Dissolve(1)
            mc "Ah... Is this your recruitment shtick?"
            mc "Like. Here try on this shirt, it will look really good on you."
            mc "And then BAM. Welcome. You're now in the cheerleading squad."
            la "Haha."
            scene 05_539 with Dissolve(1)
            el "Heh... How funny! But so wrong."
            el "You have no idea how many boys come to tryouts to join the squad."
            mc "Uh-huh. Obviously for the right reasons."
            el "..."
        "Thank you":
            mc "Thank you. Let's try it on and see if it fits."
    scene 05_540 with Dissolve(1)
    el "Wait... Why are you changing here?"
    mc "It's a quick shirt swap. Just turn around if you don't want to see."
    if Layla_Week1_Saturday_Beach_Ocean == True:
        mc "And I think you've seen more before, when we were at the beach!"
        el "..."
    else:
        el "..."
    if Layla_Points >= 31:
        scene 05_541 with Dissolve(1)
        la "{i}(Or just run around without a shirt...){/i}"
    else:
        pass
    scene 05_542 with Dissolve(1)
    el "Will you look at that. It actually fits you perfectly."
    mc "Uh-huh..."
    scene 05_543 with Dissolve(1)
    el "He looks good in it. Right, Layla?"
    la "Honestly... Yeah!"
    if Elena_Week2_Tuesday_RecruitJoke == True:
        scene 05_544 with Dissolve(1)
        mc "See... I told you. This is how you guys recruit!"
        la "Haha. [mc] has a point, Elena."
        el "*Sigh*"
        scene 05_545 with Dissolve(1)
        si "Elena, are you coming? We're waiting for you."
        el "Uh... Sorry. Yeah."
        mc "{i}(Oh... Sienna is also on the squad.){/i}"
    else:
        scene 05_545 with Dissolve(1)
        si "Elena, are you coming? We're waiting for you."
        el "Uh... Sorry. Yeah."
        mc "{i}(Oh... Sienna is also on the squad.){/i}"
    scene 05_546 with Dissolve(1)
    el "I gotta go. See you later Layla, [mc]."
    la "Later, El."
    if Elena_Points >= 11:
        mc "Bye, Elena. And thank you. You can be really nice sometimes."
        el "I have my moments."
        scene 05_547 with Dissolve(1)
        el "But only to the people I like."
        mc "Oh? You like me now? I'm growing on you, huh?"
        el "You aren't that bad."
    else:
        mc "Bye, Elena. And thank you."
        el "Sure."
    scene 05_548 with Dissolve(1)
    mc "Should I go to tryouts with this, just for fun?"
    la "Haha... Sure why not. I'd actually pay to see you try for real."
    la "I can help you with some routines. And I think I still have my pompoms at home."
    mc "Great. Do you think I can make the squad?"
    la "Of course! Haha."
    la "Come on. Let's get something to eat. I'm hungry."
    z "Hey, guys."
    scene 05_549 with Dissolve(1)
    mc "Hey. What's up?"
    la "Hi, Zach."
    scene 05_550 with Dissolve(1)
    z "You have to come with me for a second. This is urgent."
    mc "Okay?"
    z "Wait... I'm confused. Did you join the cheerleading squad?"
    la "Haha."
    mc "No. I didn't..."
    z "Hmm... Weird choice of clothing then."
    mc "You can say that."
    scene 05_551 with Dissolve(1)
    z "Sorry, Layla. I need my friend here for a moment."
    la "It's alright. Go ahead."
    scene 05_552 with Dissolve(1)
    z "Come on... No time to lose."
    mc "See you later, Layla."
    la "Bye, [mc]."
    scene 05_553 with Dissolve(1)
    la "*Sigh*"
    la "I don't want to eat alone."
    scene 05_554 with Dissolve(1)
    x "Hi."
    la "Hey."
    scene 05_555 with Dissolve(1)
    x "Do you mind if I sit here?"
    la "Sure. Go ahead. I was leaving anyway."
    x "Uh. You don't..."
    scene black with Dissolve(1)
    pause 2
    scene 05_556 with Dissolve(1)
    if Zach_Week2_Monday_House == False:
        mc "So... What's up?"
        mc "Must be a big secret if you dragged me all the way out here."
    else:
        mc "Hey... Thanks again for letting me stay at your place."
        z "No problem, any time. You left pretty early."
        mc "Yeah, I had to go somewhere before school."
        mc "So... What's up? Must be a big secret if you dragged me all the way out here."
        mc "{i}(I hope this isn't about Natasha and what I saw this morning.){/i}"
    scene 05_557 with Dissolve(1)
    z "Dude!"
    z "I'm in love."
    mc "Yeah? What's different with any other day?"
    z "This is different."
    mc "Hmm, okay... How so?"
    scene 05_558 with Dissolve(1)
    z "Have you seen the new girl?"
    mc "I don't know. I just started here a week ago. I don't know who's new or who isn't."
    z "You'll know once you see her."
    scene 05_559 with Dissolve(1)
    z "But listen to this."
    z "So, I talked to her. Her name is Valeria. Isn't that the cutest name ever?"
    mc "Uhm... Sure."
    scene 05_560 with Dissolve(1)
    z "And the best thing is. She'll be joining the track and field team."
    mc "And why is that the best thing? You aren't even on the team."
    z "But you are. You can talk to her. Tell her I'm a great guy and stuff, you know?"
    mc "No more Layla then?"
    scene 05_561 with Dissolve(1)
    if Layla_Points >= 27:
        z "Man. I don't know. I'm so conflicted."
        z "I think Layla is more into you anyway. So..."
    else:
        z "Man. I don't know. I'm so conflicted."
    z "You need to help me out with this one, [mc]."
    mc "I'll try my best."
    scene 05_558 with Dissolve(1)
    z "I knew I can count on you."
    mc "Any time, man..."
    scene 05_562 with Dissolve(1)
    z "Well, I'm going to look for her and get to know her some more. Wish me luck."
    mc "Yeah... Good luck."
    z "Thanks, bro. I'm so nervous. Hahaha."
    scene 05_563 with Dissolve(1)
    z "VALERIA!"
    mc "*Shakes head*"
    mc "{i}(This poor girl. I feel so bad for her already.){/i}"
    jump Week2_Tuesday_Erynn_Pickup

label Week2_Tuesday_Erynn_Pickup:
    scene black with Dissolve(1)
    pause 2
    stop music fadeout 1.0
    play music ("Music/LoFi Indie 3.mp3", "Music/LoFi Indie 1.mp3", "Music/LoFi Indie 2.mp3") volume 0.2
    n "16:12. Erynn's apartment."
    scene 05_564 with Dissolve(1)
    n "*Knock-knock*"
    mc "{i}(Hmm... Isn't she back yet?){/i}"
    mc "..."
    mc "{i}(Right... She said her classes go until five.){/i}"
    menu:
        "Wait for her":
            scene 05_565 with Dissolve(1)
            mc "{i}(Guess I'll just wait here for a while.){/i}"
            scene black with Dissolve(1)
            pause 2
            scene 05_566 with Dissolve(1)
            er "Hey, [mc]. Did you wait here this whole time?"
            mc "Hi, Erynn. Yeah... I didn't mind. Wasn't really in a mood to go somewhere."
            er "Uhm? What's up with that t-shirt? Are you on the cheerleading squad?"
            scene 05_567 with Dissolve(1)
            mc "Yeah! Didn't I tell you?"
            if Erynn_Week2_Monday_GoToErynn == True:
                er "No... Didn't you say you joined the track and field team?"
            else:
                er "No... I would've definitely remembered."
            scene 05_568 with Dissolve(1)
            mc "I'm kidding."
            er "Haha... Okay. You almost had me there."
            mc "I couldn't run around in my gym shirt the whole day while at school, so a friend gave me this."
            er "Oh... That's nice. I have to say. It actually suits you."
            mc "You're not the first to say that. Maybe I should join the squad."
            er "Haha. Who knows?"
            scene 05_569 with Dissolve(1)
            er "By the way... Can you do a cheer for me?"
            mc "Oh, hell no!"
            er "Please, [mc]?"
            er "Please-please-please?"
            scene 05_570 with Dissolve(1)
            mc "No... No-no-no. If I do, you'll never let me forget it. Nuh-uh... Not gonna happen!"
            er "Aw..."
            er "Can I take a picture then?"
            mc "Sure. A normal picture is fine."
            scene 05_571 with Dissolve(1)
            er "Okay... Can you do a cheer pose at least?"
            mc "This is a cheer pose."
            er "Really?"
            mc "Yeah... The 'Ready', as in the 'let's take this picture already' pose."
            er "Uh-huh. Haha..."
            mc "If you were on the cheerleading squad instead of the volleyball team, you would know that."
            scene 05_572 with Dissolve(1)
            er "Wait... Let's take one more."
            er "We haven't taken one of the two of us yet."
            jump Week2_Tuesday_Erynn_Apartment
        "Pick her up[KoGa3AutoWTChange1]{size=-4}(Erynn Week2 Tuesday Pickup, Erynn Points+2) {/size} {/color}":
            $ Erynn_Week2_Tuesday_Pickup = True
            $ Erynn_Points += 2
            # Erynn (22)
            mc "{i}(I might as well go pick her up. Let's surprise her.){/i}"
            scene black with Dissolve(1)
            pause 2
            scene 05_573 with Dissolve(1)
            mc "{i}(17:05. She must be coming out soon. I hope I won't miss her or I'll be sitting here for a while.){/i}"
            if Alexis_Friends == False:
                scene 05_574 with Dissolve(1)
                a "{i}(Oh... What is he doing here?){/i}"
                a "{i}(Did he come to talk? I'm actually really happy to see him.){/i}"
                a "{i}(I hope I can explain everything to him.){/i}"
                scene 05_575 with Dissolve(1)
                a "Hey, [mc]."
                er "Hey there!"
                scene 05_576 with Dissolve(1)
                a "..."
                a "{i}(I guess he didn't come for me.){/i}"
                scene 05_577 with Dissolve(1)
                er "What a nice surprise."
                mc "Hey, Erynn."
                er "Hi!"
                er "What are you doing here?"
            else:
                scene 05_577 with Dissolve(1)
                er "What a nice surprise."
                mc "Hey, Erynn."
                er "Hi!"
                er "What are you doing here?"
            menu:
                "Checking out girls":
                    if Alexis_Friends == False:
                        scene 05_578 with Dissolve(1)
                        mc "Checking out some college girls."
                    else:
                        mc "Checking out some college girls."
                    er "Did you find any whom you fancy?"
                    mc "There were a few."
                    scene 05_579 with Dissolve(1)
                    er "Am I included?"
                    mc "You know what?"
                    er "What?"
                    mc "You know what happens?"
                    er "Haha. What?"
                    mc "You just made the list!"
                    scene 05_580 with Dissolve(1)
                    er "Good answer!"
                    mc "{i}(Heh. Good answer? I think she didn't get that reference.){/i}"
                    mc "{i}(I think we should watch some wrestling next time...){/i}"
                "Picking you up":
                    if Alexis_Friends == False:
                        scene 05_578 with Dissolve(1)
                        mc "Picking you up of course"
                    else:
                        mc "Picking you up of course"
                    scene 05_580 with Dissolve(1)
                    er "Good answer!"
            scene 05_581 with Dissolve(1)
            mc "How are you?"
            er "Really happy now."
            mc "How come?"
            er "Hmm... I don't know. Maybe because you're here."
            er "Is there some room for me?"
            mc "Of course. Come sit down."
            scene 05_582 with Dissolve(1)
            er "Uhm... What's up with that t-shirt? Are you on the cheerleading squad?"
            mc "Yeah. Didn't I tell you?"
            if Erynn_Week2_Monday_GoToErynn == True:
                er "No... Didn't you say you joined the track and field team?"
            else:
                er "No... I would've definitely remembered."
            mc "I'm kidding."
            scene 05_583 with Dissolve(1)
            er "Haha... Okay. You almost had me there."
            mc "I couldn't run around in my gym shirt the whole day while at school, so a friend gave me this."
            er "Oh... That's nice. I have to say. It actually suits you."
            mc "You're not the first to say that. Maybe I should join the squad."
            er "Haha. Who knows?"
            scene 05_584 with Dissolve(1)
            er "By the way. Can you do a cheer for me?"
            mc "No-no-no."
            er "Please-please-please, pretty please?"
            mc "If I do, you'll never let me forget it. Nuh-uh. Not gonna happen!"
            er "Aw..."
            er "Can I have a picture then?"
            mc "Sure... A normal picture is fine."
            scene 05_585 with Dissolve(1)
            er "But let's take one together first. We haven't taken one yet."
            mc "Okay."
            menu:
                "Tickle her":
                    mc "What's up with that model stare?"
                    er "I have to look good. It's our first picture in years."
                    scene 05_586 with Dissolve(1)
                    er "Hey! Hahaha... Stop... I'm ticklish."
                    er "[mc]... Haha..."
                    mc "See... This picture is so much better."
                "Take the picture":
                    mc "What's up with that model stare?"
                    er "I have to look good. It's our first picture in years."
            scene 05_587 with Dissolve(1)
            er "Okay... Now do a cheer pose."
            mc "This is a cheer pose."
            er "Really?"
            mc "Yeah... The 'Ready', as in the 'let's take this picture already' pose."
            er "Uh-huh. Haha..."
            mc "If you were on the cheerleading squad instead of the volleyball team, you would know that."
            scene 05_588 with Dissolve(1)
            er "Come on. let's go. I've seen enough of this place for today."
            er "We can stop by a clothes store before we go home. I'll buy you a new t-shirt."
            mc "I thought you liked this one."
            er "I do. But you need one for tomorrow, right?"
            scene black with Dissolve(1)
            pause 2
            scene 05_589 with Dissolve(1)
            er "Hmm... How about this one?"
            er "What do you think?"
            mc "You're the model. I trust your judgement."
            er "Alright. Try it on."
            scene 05_590 with Dissolve(1)
            mc "Can you close the curtain please?"
            er "Since when are you shy?"
            mc "I'm not. Just common courtesy towards other people in the shop."
            scene 05_591 with Dissolve(1)
            er "Better?"
            mc "{i}(Of course she stays in here. Why did I even bother asking?){/i}"
            mc "Uhm... Yeah... Whatever."
            scene 05_592 with Dissolve(1)
            er "..."
            scene 05_593 with Dissolve(1)
            mc "What?"
            er "Hmm?"
            mc "Why are you staring at me like that?"
            er "..."
            er "I wasn't... Just... waiting."
            scene 05_594 with Dissolve(1)
            mc "What do you think?"
            er "..."
            er "Yeah... It looks good. Are you happy with it?"
            mc "Uhm, sure. It's a t-shirt."
            er "Okay. Then we'll take this one. Quick and easy."
            scene 05_595 with Dissolve(1)
            x "I'll be right with you."
            er "Sure."
            scene 05_596 with Dissolve(1)
            mc "Hey! That's you!"
            er "Mm-hmm."
            mc "Didn't see that when we came in."
            scene black with Dissolve(1)
            transform moveup:
                xalign 0.5 yalign 1.0
                linear 5.0 yalign 0.0
            show 05_597 at moveup
            pause 3
            mc "Wow!"
            mc "First model picture I see of you."
            mc "Looks great."
            er "Thanks."
            scene 05_598 with Dissolve(1)
            mi "Hey, Erynn. How are you?"
            er "Hey, Michelle."
            er "I'm good, thank you. How about you?"
            scene 05_599 with Dissolve(1)
            mi "Can't complain. I see you brought your boyfriend along."
            er "Uh..."
            menu:
                "Correct her[KoGa3AutoWTChange1]{size=-4}(Erynn Week2 Tuesday CorrectHer) {/size} {/color}":
                    $ Erynn_Week2_Tuesday_CorrectHer = True
                    mc "We're friends."
                    mi "Oh... I'm sorry."
                "Leave it be[KoGa3AutoWTChange1]{size=-4}(Erynn Points+2) {/size} {/color}":
                    $ Erynn_Points += 2
                    # Erynn (24)
                    mc "Yes. Hi."
                    mc "Needed a new t-shirt, and she's the expert."
                    mi "She is."
                    show 05_600
                    er "{i}(Oh...){/i}"
                    mi "You look good together. A gorgeous couple!"
                    mc "Thank you."
            scene 05_601 with Dissolve(1)
            mc "Thank you, Erynn."
            er "You're welcome."
            if Week2_Monday_Erynn_Help == True:
                er "Shall we head home?"
                menu:
                    "Yes":
                        mc "Yeah."
                        er "Let's grab something to eat along the way."
                        mc "Sounds good."
                        jump Week2_Tuesday_Erynn_Apartment
                    "Buy her something[KoGa3AutoWTChange1]{size=-4}(Erynn Week2 Tuesday Gt, Erynn Points+2) {/size} {/color}":
                        $ Erynn_Week2_Tuesday_Gift = True
                        $ Erynn_Points += 2
                        # Erynn (26)
                        mc "One second. I forgot something."
                        mc "Can you wait here for a moment."
                        er "Uh... Sure."
                        scene black with Dissolve(1)
                        pause 2
                        scene 05_602 with Dissolve(1)
                        er "Oh... You bought something else?"
                        mc "Uh-huh..."
                        er "What is it?"
                        mc "A surprise."
                        scene 05_603 with Dissolve(1)
                        er "Let's head home then. We can grab something to eat along the way."
                        mc "Sounds good."
            else:
                er "Shall we head home?"
                mc "Yeah."
                er "Let's grab something to eat along the way."
                mc "Sounds good."
                jump Week2_Tuesday_Erynn_Apartment

label Week2_Tuesday_Erynn_Apartment:
    scene black with Dissolve(1)
    pause 2
    scene 05_604 with Dissolve(1)
    if Erynn_Week2_Tuesday_Pickup == False:
        mc "I'm not doing anything today besides relaxing on the couch."
        er "Hehe... You old man."
        er "By the way. I bought you a new t-shirt earlier."
        mc "Oh you did? Thank you. What do I owe you?"
        er "Nothing. It's a present. So you have something to wear tomorrow."
        mc "Thank you, Erynn."
        er "Uh-huh."
    else:
        if Erynn_Week2_Tuesday_Gift == False:
            mc "I'm not doing anything today besides relaxing on the couch."
            er "Hehe... You old man."
        else:
            mc "I'm not doing anything today besides relaxing on the couch."
            er "Hehe... You old man."
            er "So what is the surprise you bought earlier?"
            mc "Well, open it up and see for yourself."
            er "Oh... It's for me?"
            mc "Yeah."
            er "Thank you, [mc]."
            scene 05_605 with Dissolve(1)
            er "Haha. Stockings?"
            mc "Wait... Those aren't pantyhoses?"
            er "Hmm... Sort of, but not really."
            mc "What's the difference?"
            er "Panthyhoses are thinner."
            scene 05_606 with Dissolve(1)
            mc "Shit. I wanted to get you new ones because you tore your others because of me."
            mc "I can bring them back and exchange them."
            er "You didn't have to buy me new ones, but thank you."
            er "I quite like these."
            scene 05_607 with Dissolve(1)
            mc "Okay. Try them on and let's see."
            er "..."
            mc "What?"
            mc "Just to see if they'll fit, obviously."
            scene 05_608 with Dissolve(1)
            er "..."
            mc "Maybe they aren't long enough or something?"
            er "*Sigh* Okay..."
            er "Give me a minute."
            scene black with Dissolve(1)
            pause 2
            scene 05_609 with Dissolve(1)
            mc "What's taking so long?"
            er "Don't rush me. I need to find matching underwear."
            mc "Why would you need underwear?"
            er "If I'll put my pants back on, you won't be able to see them now, will you?"
            mc "Right... Continue. Take all the time you need."
            mc "{i}(Seems like she's making a fashion show out of it.){/i}"
            scene 05_610 with Dissolve(1)
            er "Okay... Ready."
            er "Coming out now."
            mc "{i}(Can't wait to see this. I hope it looks good!){/i}"
            scene black with Dissolve(1)
            transform moveup:
                xalign 0.5 yalign 1.0
                linear 5.0 yalign 0.0
            show 05_611 at moveup
            pause 3
            mc "{i}(Wow...){/i}"
            mc "{i}(I didn't expect her to walk out like this.){/i}"
            scene 05_612 with Dissolve(1)
            er "What do you think?"
            mc "Uh... Yeah... They look great. You look great!"
            er "Thank you. I like them, too."
            mc "Can you turn around? I want to see how it looks from the back."
            scene 05_613 with Dissolve(1)
            er "..."
            er "I know what you're up to."
            mc "What? Maybe they look different from the back. A different pattern or something."
            if Erynn_Points >= 21:
                er "Uh-huh. Nice try."
                scene 05_614 with Dissolve(1)
                er "{i}(Okay... Just this once.){/i}"
                mc "..."
                scene 05_615 with Dissolve(1)
                mc "{i}(Damn! Like mother like daughter.){/i}"
                scene 05_616 with Dissolve(1)
                er "I think you've seen enough now."
                mc "Heh..."
                mc "Thanks for showing me! It really does look good on you!"
                er "*Nods*"
            else:
                er "Uh-huh. Nice try."
    scene black with Dissolve(1)
    pause 2
    scene 05_617 with Dissolve(1)
    mc "What are you doing?"
    mc "Looking for something?"
    er "Yes... My phone."
    scene 05_618 with Dissolve(1)
    mc "Why would it be there?"
    er "I don't know... I can't find it. So, I'm looking everywhere."
    scene 05_619 with Dissolve(1)
    er "*Sigh* Seriously... Where did I put it? Have you seen it?"
    mc "Want me to just call your phone?"
    er "..."
    er "Right... *Shakes head* Why haven't I thought about that..."
    er "Please, do."
    scene 05_620 with Dissolve(1)
    mc "Hmm... Straight to voicemail."
    mc "Did the battery die?"
    er "Could be. It was pretty low."
    scene 05_621 with Dissolve(1)
    er "*Sigh* Dammit."
    mc "Do you have an important call?"
    er "I was going out with a friend. But I'm going to cancel because you're here."
    mc "You don't have to cancel because of me. Just go."
    er "It's fine. I'd like to spend some time with you if you don't mind?"
    scene 05_622 with Dissolve(1)
    mc "Uhm, sure..."
    mc "Use my phone to call your friend. If you know the number."
    er "Yeah? Thank you, [mc]."
    scene 05_623 with Dissolve(1)
    er "Be right back."
    mc "Take your time."
    if Alexis_Friends == False:
        $ Erynn_Week2_Tuesday_AlexisFight = True
        scene 05_624 with Dissolve(1)
        er "{i}(What was the number again? 04...){/i}"
        play sound "Sounds/Phone_Message.mp3"
        n "*Bzzzt*"
        er "{i}(Oh... He got a message.){/i}"
        scene 05_625 with Dissolve(1)
        er "{i}(Alexis?){/i}"
        er "{i}(Why would she..?){/i}"
        er "{i}(*Shakes head* It's probably someone else named Alexis.){/i}"
        scene 05_626 with Dissolve(1)
        er "..."
        er "{i}(Sorry...){/i}"
        scene 05_627 with Dissolve(1)
        a "I'm sorry! I'm so sorry! Can we please talk? I will explain everything."
        a "Can you meet me at the bar? Please?"
        er "{i}(The bar?){/i}"
        er "{i}(No... It can't be...){/i}"
        if Alexis_Week1_Sunday_Concert_Sing == True:
            scene 05_628 with Dissolve(1)
            er "{i}(It's definitely her!){/i}"
            er "{i}(Wait... Where was this?){/i}"
            er "{i}(Was it the Yellow Snow concert? She told me she couldn't go.){/i}"
            er "..."
            scene 05_629 with Dissolve(1)
            er "{i}(They drove there together?){/i}"
        else:
            scene 05_629 with Dissolve(1)
            er "{i}(It's definitely her!){/i}"
            er "{i}(Where did they drive to?){/i}"
        if Alexis_Week1_Saturday_Picture == True:
            scene 05_630 with Dissolve(1)
            er "{i}(Looks like they've met a few times already.){/i}"
            er "{i}(Why hasn't she said anything?){/i}"
        else:
            pass
        if Alexis_Week1_Saturday_Picture_Night == True:
            scene 05_631 with Dissolve(1)
            er "{i}(Okay... What the fuck, Alexis!){/i}"
            er "{i}(Why?){/i}"
        else:
            pass
        scene 05_632 with Dissolve(1)
        er "{i}(Are they dating? She wouldn't, right? How did they even meet?){/i}"
        er "{i}(I can't believe this is happening...){/i}"
        scene 05_633 with Dissolve(1)
        er "..."
        scene 05_634 with Dissolve(1)
        mc "Hey. Are you okay?"
        er "..."
        mc "Uh... Are you going out?"
        er "Yes!"
        scene 05_635 with Dissolve(1)
        mc "What's going on?"
        er "That's what I'd like to know."
        er "Bye..."
        mc "Erynn?"
        mc "{i}(What happened during that phone call?){/i}"
        jump Week2_Tuesday_AlexisErynnFight
    else:
        scene 05_624 with Dissolve(1)
        er "{i}(What was the number again? 04...){/i}"
        scene 05_636 with Dissolve(1)
        er "..."
        er "{i}(Why isn't she picking up?){/i}"
        er "{i}(Maybe because it's an unknown number?){/i}"
        er "{i}(I'll try again later. And maybe I've found my phone by then.){/i}"
        scene 05_627 with Dissolve(1)
        er "*Sigh*"
        er "{i}(There's someone else I need to call.){/i}"
        scene 05_637 with Dissolve(1)
        er "Hey..."
        x "Ah, perfect! I was just on my way to you because I couldn't reach you."
        x "You got a new phone?"
        er "No. It's a friend's. I couldn't find mine."
        scene 05_638 with Dissolve(1)
        er "What do you want?"
        x "I need you for a job."
        er "What job?"
        x "You know what job."
        er "..."
        scene 05_639 with Dissolve(1)
        er "I can't... I have company."
        x "Who?"
        er "..."
        er "Friends."
        x "Well, I don't care. Tell them you'll be back in two hours."
        scene 05_640 with Dissolve(1)
        x "Be at Prestige in 15 minutes!"
        x "Just come as you are. No need to dress up. We already lost too much time since I couldn't reach you."
        er "I don't want to do this!"
        x "Fifteen minutes!"
        scene 05_641 with Dissolve(1)
        er "..."
        scene 05_634 with Dissolve(1)
        mc "Hey. Are you okay?"
        er "..."
        mc "Uh... Are you going out?"
        er "Yes!"
        scene 05_635 with Dissolve(1)
        mc "What's going on?"
        er "Sorry... It's uh... work related."
        er "Bye."
        mc "Erynn?"
        mc "{i}(Who did she call? Work related? Ethan again?){/i}"
        jump Episode_6_Start

label Week2_Tuesday_AlexisErynnFight:
    scene black with Dissolve(1)
    pause 2
    stop music fadeout 1.0
    play music "Music/Valeria - Emptiness.mp3" volume 0.5
    scene 05_642 with Dissolve(1)
    a "Oh... Hey, Erynn. What a surprise."
    a "{i}(I hope [mc] doesn't show up right now.){/i}"
    a "{i}(But this is maybe a good time to explain to her.){/i}"
    er "What a surprise indeed."
    a "Sorry. What?"
    scene 05_643 with Dissolve(1)
    er "How could you?"
    a "{i}(She knows... Did [mc] tell her? This is bad.){/i}"
    er "I thought we were best friends!"
    scene 05_644 with Dissolve(1)
    a "Erynn... We are!"
    er "Best friends don't do this to each other."
    er "I just can't believe it."
    er "We used to tell each other everything! And now I found out about this?"
    scene 05_645 with Dissolve(1)
    er "You know how I feel about him."
    er "I came to you to talk about him so many times. That I miss him. That I can't wait to finally see him again one day."
    er "I even told you two days ago that he's back..."
    scene 05_646 with Dissolve(1)
    er "But you knew that already for quite a while, right?"
    er "And didn't say a word."
    a "Uhm..."
    scene 05_647 with Dissolve(1)
    er "Yeah... I saw the pictures. I know what you've been up to."
    er "You even lied about the concert."
    a "{i}(That was terrible, I shouldn't have done that...){/i}"
    scene 05_648 with Dissolve(1)
    a "I'm sorry. I..."
    er "Did you sleep with him?"
    a "..."
    scene 05_649 with Dissolve(1)
    er "Did you sleep with him?"
    a "Erynn... Please?"
    er "Answer the question, Alexis! Did you sleep with him?"
    scene 05_650 with Dissolve(1)
    a "Yes."
    er "..."
    scene 05_651 with Dissolve(1)
    a "Erynn... I'm sorry."
    er "..."
    scene 05_652 with Dissolve(1)
    a "Erynn..."
    er "Don't!"
    scene 05_653 with Dissolve(1)
    er "When were you going to tell me?"
    a "I was... I just didn't know how."
    er "So, in other words. Never!"
    er "Just like what happened with Ethan, huh?"
    scene 05_654 with Dissolve(1)
    a "What are you talking about?"
    a "Nothing happened between me and Ethan. Ever! You know I don't like the guy."
    scene 05_655 with Dissolve(1)
    er "You lied about [mc]. Maybe you lied about that, too."
    a "He's the one lying, Erynn. You of all people should know that... He tried so many times to break us apart."
    er "Looks like you did the job for him."
    scene 05_656 with Dissolve(1)
    a "Erynn..."
    a "Trust me."
    er "Trust you? After all this? After all YOUR lies?"
    scene 05_657 with Dissolve(1)
    a "..."
    er "..."
    scene 05_658 with Dissolve(1)
    a "I met him on the plane. We were seated next to each other and started to talk."
    er "..."
    a "I was already attracted to him before I realised who he was."
    er "But that didn't stop you?"
    scene 05_659 with Dissolve(1)
    er "After you figured out who he was, you still slept with him..."
    a "I like him."
    er "Heh... *Shakes head* Now you like [mc]?"
    a "..."
    er "You never even talked to him before."
    a "{i}(That's not true.){/i}"
    scene black with Dissolve(1)
    pause 2
    n "A few years ago."
    scene 05_660 with Dissolve(1)
    et "Hey, buddy. Nice try. How about you grow a few inches first?"
    a "Ethan! Don't be mean."
    scene 05_661 with Dissolve(1)
    et "Haha... What a loser!"
    er "[mc]..."
    er "Dammit, Ethan."
    a "*Shakes head* I'm going home!"
    scene 05_662 with Dissolve(1)
    a "Hey, are you okay?"
    mc "Go away. Just leave me alone!"
    a "Ethan is an idiot. I don't like him either."
    mc "..."
    scene 05_663 with Dissolve(1)
    a "I think what you did was really cute."
    a "Nobody ever gave me flowers."
    mc "It's just one flower."
    a "That doesn't matter. I'd love to get flowers from a boy one day."
    scene 05_664 with Dissolve(1)
    mc "{i}(Uh?){/i}"
    mc "Hey! What are you doing?"
    scene 05_665 with Dissolve(1)
    a "Happy Birthday, [mc]!"
    scene black with Dissolve(1)
    pause 2
    scene 05_666 with Dissolve(1)
    er "You know what? I can't listen to you anymore. I've had enough. We are done."
    a "Erynn..."
    er "What, Alexis?"
    a "We've known each other for 15 years. You can't just say that we're done. Can we please talk?"
    er "What is there to talk about? You betrayed our friendship."
    a "I know, that's why I want to explain."
    er "No."
    scene 05_667 with Dissolve(1)
    a "Erynn..."
    a "Please!"
    scene 05_668 with Dissolve(1)
    a "..."
    scene 05_669 with Dissolve(1)
    ""
    scene 05_670 with Dissolve(1)
    ""
    scene 05_671 with Dissolve(1)
    ""
    scene 05_672 with Dissolve(1)
    ""
    scene 05_673 with Dissolve(1)
    ""
    scene 05_674 with Dissolve(1)
    ""
    jump Episode_6_Start

# Max Points:

# Alexis (26)
# Melissa (12)
# Layla (36)
# Elena (14)
# Emily (4)
# Erynn (26)
# Tori (2)
# Cara (16)
# Nikki (20)
# Lakeyn (6)
# Brooke (2)
# Adriana (4)

# MC_GoodStudent (12)

# MC_Sex (13)
# Alexis_Sex (5)
# Tori_Sex (1)
# Lakeyn_Sex (1)
# Nikki_Sex (2)
# Cara_Sex (2)
# Julia_Sex (1)
# Rachel_Sex (1)


# Max Points:

# Alexis (26)
# Melissa (12)
# Layla (36)
# Elena (14)
# Emily (4)
# Erynn (26)
# Tori (2)
# Cara (16)
# Nikki (20)
# Lakeyn (6)
# Brooke (2)
# Adriana (4)

# MC_GoodStudent (12)

# MC_Sex (13)
# Alexis_Sex (5)
# Tori_Sex (1)
# Lakeyn_Sex (1)
# Nikki_Sex (2)
# Cara_Sex (2)
# Julia_Sex (1)
# Rachel_Sex (1)

#WTAdded
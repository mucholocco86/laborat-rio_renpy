label Episode_3_Start:

    #KoGa3 START#
    $ KoGa3GameProgress = "Ep3"
    #KoGa3 END#

    $ achievement.grant("ACHIEVEMENT_EPISODE_2")
    $ achievement.sync()
    $ Layla_Week1_Wednesday_HallwayTalk = False
    $ Layla_Week1_Wednesday_ParkHelp = False
    $ Layla_Week1_Wednesday_ParkStay = False
    $ Alexis_Week1_Wednesday_PhonePickup = False
    $ Alexis_Week1_Wednesday_PhoneHome = False
    $ Alexis_Week1_Wednesday_PhoneIgnore = False
    $ Alexis_Lexi = False
    $ Mike_Name = False
    $ Tori_Sex = False
    $ Sienna_Name = False
    $ Dylan_Week1_Assumption = False
    $ Tori_Week1_Interested = False
    $ Elena_Cute = False
    $ Erynn_Week1_Stay = False
    $ Erynn_Week1_ShowerJoin = False
    $ Elena_Week1_TrainKissLayla = False
    $ Elena_Week1_TrainKiss = False
    $ Layla_Week1_Piggyback = False
    $ Erynn_Week1_Cupsize = False

    jump Week1_Wednesday_School

label Week1_Wednesday_School:
    scene black with Dissolve(2)
    pause 2
    n "Wednesday, 08:24. School."
    scene 03_001 with Dissolve(1)
    mc "{i}(Oh. There's Layla.){/i}"
    la "You can't be serious...!"
    x "I warned you last time, Layla!"
    mc "{i}(She looks upset... Is that a teacher she's arguing with?){/i}"
    scene 03_002 with Dissolve(1)
    la "But..."
    x "No more discussion. If you change your mind, come see me."
    la "..."
    scene 03_003 with Dissolve(1)
    x "Good morning."
    mc "{i}(Who's that? I haven't seen her around before.){/i}"
    mc "Uh... Good morning."
    scene 03_004 with Dissolve(1)
    mc "{i}(She doesn't look too happy...){/i}"
    mc "{i}(Maybe I should give her some space?){/i}"
    menu:
        "Talk to her[KoGa3AutoWTChange1]{size=-4}(Layla Week1 Wednesday HallwayTalk, Layla Points+2) {/size} {/color}":
            $ Layla_Week1_Wednesday_HallwayTalk = True
            $ Layla_Points += 2
            # Layla (10)
            scene 03_005 with Dissolve(1)
            mc "Hey. Morning, Layla."
            la "Hmm? Oh... Morning."
            mc "You okay?"
            scene 03_006 with Dissolve(1)
            la "..."
            la "I'm fine."
            mc "{i}(If this is her being fine, I'd hate to see her when she's actually upset... or worse, angry.){/i}"
            scene 03_007 with Dissolve(1)
            z "Hey you GUUUYS!"
            la "*Sigh* Ugh."
            scene 03_008 with Dissolve(1)
            la "Not now."
            la "I really can't deal with him today."
            la "Bye."
            mc "Uh?"
            scene 03_009 with Dissolve(1)
            mc "Layla, wait! Layla?"
            z "Wow. Someone definitely woke up on the wrong side of the bed."
            scene 03_010 with Dissolve(1)
            z "Hey, man."
            mc "Morning. You're in a good mood, huh?"
        "Leave her alone":
            scene 03_011 with Dissolve(1)
            z "Hey, man."
            mc "Heh... Morning."
    jump Week1_Wednesday_Hallway

label Week1_Wednesday_Hallway:
    if Alexis_Friends == True:
        scene 03_012 with Dissolve(1)
        z "Dude..."
        mc "Why are you grinning like that? Looks like you had a good night."
        z "Hmm. It was alright."
        mc "Just alright? Come on, you look like you won the lottery. Spill it."
        scene 03_013 with Dissolve(1)
        z "Alright, alright. So, me and the team hit up the bar last night."
        z "And man, I met this girl. Total knockout. You had to see her."
        mc "Uh-huh..."
        z "We flirted, I bought her a few drinks... Got my hand on her thigh."
        scene 03_014 with Dissolve(1)
        mc "You had your hand on her thigh?"
        z "She was totally into it. But then she got a call and had to leave."
        z "Still, dude... One of the best nights of my life."
        scene 03_015 with Dissolve(1)
        mc "Did you at least get her number?"
        z "Nah. But she gave me a kiss on the cheek before leaving."
        mc "So... No number?"
        z "Not yet. I'll see her next time."
        scene 03_016 with Dissolve(1)
        mc "Oh? You've got another date lined up?"
        z "Nope. But we just clicked, y'know? I've got a good feeling about it."
        mc "{i}(Hopeless. I should just buy him a copy of Dating 101.){/i}"
        scene 03_017 with Dissolve(1)
        z "Anyway, I'm off. Can't be late for my favourite class."
        mc "Which is?"
        z "Spanish."
        mc "You? Spanish? Really?"
        scene 03_018 with Dissolve(1)
        z "Haha."
        mc "What?"
        z "You'll see soon enough, lil' grasshoppa."
        mc "{i}(*Sigh* This guy.){/i}"
    else:
        scene 03_012 with Dissolve(1)
        z "Dude..."
        mc "Why are you grinning like that? Looks like you had a good night."
        z "Hmm. It was alright."
        mc "Just alright? Come on, you look like you won the lottery. Spill it."
        z "You'll figure it out soon enough!"
        scene 03_013 with Dissolve(1)
        mc "What? How am I involved in this all of a sudden."
        z "Haha. Patience lil' grasshoppa... Patience."
        mc "Seriously? You're not making any sense."
        z "Soon. Just... Hmm. Never mind. Not saying a word."
        scene 03_017 with Dissolve(1)
        z "Anyway, I'm off. Can't be late for my favourite class."
        mc "Which is?"
        z "Spanish."
        mc "You? Spanish? Really?"
        scene 03_018 with Dissolve(1)
        z "Haha. You'll understand soon enough."
        mc "What's with all the riddles today?"
        z "Like I said. Patience..."
        mc "{i}(*Sigh* This guy. Should I be watching my back? With him, you never really know.){/i}"
    scene 03_019 with Dissolve(1)
    x "Who was that bitch, Darryl?"
    mc "{i}(Yikes. Someone else is having a rough morning...){/i}"
    da "Listen. It's not what you think. I swear, nothing happened."
    x "Nothing happened? I saw you! You had your tongue down her throat."
    scene 03_020 with Dissolve(1)
    da "What no... She's my cousin. We were just talking..."
    x "Your cousin? Wow... That's disgusting."
    x "You know what Darryl? We are so done!"
    scene 03_021 with Dissolve(1)
    da "What are you staring at?"
    mc "Just walking by, man."
    da "Then keep walking."
    mc "{i}(Seriously... What is with everyone today?){/i}"
    jump Week1_Wednesday_Park

label Week1_Wednesday_Park:
    scene black with Dissolve(2)
    pause 2
    n "Wednesday, 15:07. Clearview Meadows."
    stop music fadeout 1.0
    scene 03_022 with Dissolve(1)
    play music "Sounds/Park.mp3" volume 0.6
    mc "*Heavy breathing*"
    mc "{i}(Just a few laps and I'm already out of breath...){/i}"
    mc "{i}(I really should start running daily again. I slacked off too much the last few weeks.){/i}"
    scene 03_023 with Dissolve(1)
    mc "{i}(Is that... Layla?){/i}"
    mc "{i}(And who's that guy with her? Her boyfriend, maybe? I don't recognise him.){/i}"
    la "NO!"
    mc "{i}(What is this? Déjà vu? Looks like she's arguing again. Must be something in the air.){/i}"
    scene 03_024 with Dissolve(1)
    la "NO! And that's not going to change!"
    x "Layla, listen!"
    la "Let go of me! You're hurting me...!"
    menu:
        "Keep on running":
            scene 03_025 with Dissolve(1)
            mc "{i}(Well... This is none of my business.){/i}"
            x "Layla! Just hear me out!"
            la "I said no...! Why can't you get that?! Just leave me alone!"
            jump Week1_Wednesday_Park_Alexis
        "Help her out[KoGa3AutoWTChange1]{size=-4}(Layla Week1 Wednesday ParkHelp, Layla Points+2) {/size} {/color}":
            $ Layla_Week1_Wednesday_ParkHelp = True
            $ Layla_Points += 2
            # Layla (12)
            scene 03_026 with Dissolve(1)
            mc "There you are, Layla...! I've been running all over the place looking for you."
            la "..."
            mc "Next time, maybe text me where exactly we're supposed to meet?"
            la "Uh? [mc]? What are you...?"
            scene 03_027 with Dissolve(1)
            mc "I'll be borrowing her now, thanks!"
            x "..."
            mc "Appreciate it!"
            scene 03_028 with Dissolve(1)
            mc "Alright... Enough standing around. Let's go!"
            x "Hey! What do you think you're doing?"
            mc "Going for a run, obviously."
            x "I'm not done talking to her."
            mc "Looked to me like she was done with you. That's good enough for me."
            scene 03_029 with Dissolve(1)
            x "I'll remember this. It's not over."
            mc "Yeah, yeah..."
            mc "{i}(Does this guy ever shut up? He reminds me of someone...){/i}"
            mc "{i}(Oh right. The douche guy. Haha.){/i}"
            mc "{i}(Seems like they have them everywhere.){/i}"
            scene black with Dissolve(1)
            pause 2
            scene 03_030 with Dissolve(1)
            la "Pfew... Thank you, [mc]. You couldn't have shown up at a better time."
            mc "Hey, no worries."
            scene black with Dissolve(1)
            transform moveup:
                xalign 0.5 yalign 1.0
                linear 5.0 yalign 0.0
            show 03_031 at moveup
            pause 3
            mc "..."
            mc "Are you okay? Did he hurt you?"
            la "I'm good. Thanks."
            scene 03_032 with Dissolve(1)
            mc "So... What was all that about? Seems like you can't catch a break today."
            la "*Sigh* Just a guy I know."
            mc "{i}(Just a guy? Didn't look like that to me.){/i}"
            scene 03_033 with Dissolve(1)
            mc "It looked pretty intense. What were you arguing about?"
            la "Nothing..."
            mc "Nothing? I know it's none of my business, but that sure didn't look like nothing, Layla."
            la "..."
            mc "Does it have anything to do with what happened at school earlier?"
            scene 03_034 with Dissolve(1)
            la "What? No!"
            la "What's with all the questions anyway? Like you said. It's none of your business."
            la "So just drop it, okay?"
            mc "{i}(This escalated quickly. She's really on edge today.){/i}"
            scene 03_035 with Dissolve(1)
            mc "Alright... Sorry. I was just trying to help."
            la "Did I ask for your help?"
            mc "No, but..."
            la "Do I have a sign on my forehead which says 'please save me'?"
            scene 03_036 with Dissolve(1)
            mc "Wow. Okay. Never mind..."
            mc "I don't have time for this. I'm done here. Take care, Layla."
            mc "{i}(Is this what you get for helping someone? Screw that...){/i}"
            scene 03_037 with Dissolve(1)
            la "{i}(What am I doing? He's the only one who has been nice to me today.){/i}"
            la "{i}(Why do I always keep pushing people away? I'm such an idiot.){/i}"
            la "..."
            scene 03_038 with Dissolve(1)
            la "Sorry..."
            la "[mc]. I'm so sorry."
            la "Hey... Please, stop."
            scene 03_039 with Dissolve(1)
            la "It's just... *Sigh*"
            la "It's just one of these days, you know? Everything's going wrong. One thing after another."
            scene 03_040 with Dissolve(1)
            la "I shouldn't have snapped at you. You didn't deserve that."
            la "Can we sit for a while?"
            menu:
                "Leave":
                    scene 03_041 with Dissolve(1)
                    mc "Sorry... Gotta go."
                    la "Okay. I'm sorry."
                    jump Week1_Wednesday_Park_Alexis
                "Stay[KoGa3AutoWTChange1]{size=-4}(Layla Week1 Wednesday ParkStay, Layla Points+2) {/size} {/color}":
                    $ Layla_Week1_Wednesday_ParkStay = True
                    $ Layla_Points += 2
                    # Layla (14)
                    scene 03_042 with Dissolve(1)
                    la "Please?"
                    mc "Sure."
                    scene black with Dissolve(1)
                    pause 2
                    scene 03_043 with Dissolve(1)
                    la "So... That guy from earlier? He was a senior at our school last year."
                    la "He asked me out a few times, but I turned him down every single time. I thought he'd eventually get the hint."
                    la "Guess I was wrong. He's still trying, and I honestly don't know why he's so hung up on me."
                    mc "{i}(I might have an idea why.){/i}"
                    scene 03_044 with Dissolve(1)
                    mc "He's persistent, that's for sure."
                    mc "Did he hurt you back there?"
                    la "..."
                    la "No. Just... being pushy. Like always."
                    scene 03_045 with Dissolve(1)
                    mc "Does he usually come here when you run?"
                    la "Not really. I've seen him around before, but this was the first time he actually came up to me here."
                    mc "Maybe don't run alone for a while?"
                    la "..."
                    scene 03_046 with Dissolve(1)
                    if Layla_Week1_Wednesday_HallwayTalk == True:
                        mc "Can I ask about what happened this morning? In the hallway?"
                        la "That was Gabriela Ramirez... Or Gabi, as the guys call her."
                    else:
                        mc "Earlier today... I saw you arguing with someone at school. What was that about?"
                        la "Oh that... That was Gabriela Ramirez... Or Gabi, as the guys call her."
                    la "She teaches Spanish. Told me if I don't score at least a B on the next test, I'm going to fail the class."
                    mc "{i}(Oh? She's the Spanish teacher...){/i}"
                    mc "{i}(That explains why Spanish is Zach's favourite class.){/i}"
                    mc "Can't Elena help you with that? She's Hispanic, no? Well, I heard her speak Spanish before, at least."
                    scene 03_047 with Dissolve(1)
                    la "No. She rarely has time for herself, let alone to teach me Spanish."
                    la "Besides school and cheerleading practice, she has to take care of her two younger siblings."
                    la "She's the one getting them to and from school... Preparing dinner..."
                    la "Her mom's a nurse and works very inconsistent hours and can't be home all the time."
                    scene 03_048 with Dissolve(1)
                    mc "Wow... I didn't know any of that. Makes me see her in a totally different light."
                    mc "Also explains why she's often late."
                    la "Yeah. But the school knows about her situation. They usually let it slide."
                    mc "I figured she must've been related to the principal or something. Always seemed to get a free pass."
                    la "..."
                    la "Haha. Nope. Not even close. Though that would've explained a lot."
                    scene 03_049 with Dissolve(1)
                    mc "Hmm..."
                    la "What?"
                    mc "Well, I could help you with Spanish, if you want."
                    la "You speak Spanish?"
                    mc "Claro que sí!"
                    la "Seriously? That's unexpected."
                    scene 03_050 with Dissolve(1)
                    mc "Didn't get it from my last name? Moreno?"
                    la "Hey, in my defense, lots of people have Spanish last names and can't speak a word."
                    mc "Fair point."
                    mc "So? Is that a yes, or a no?"
                    la "It's an 'I'll think about it'. Cool?"
                    mc "Cool."
                    scene 03_051 with Dissolve(1)
                    mc "So... You're on the cheerleading squad?"
                    la "What? No. Why would you think that?"
                    mc "I guess... You mentioned Elena and I just assumed."
                    scene 03_052 with Dissolve(1)
                    la "No-no... Haha. You think every girl in our school is into cheerleading?"
                    mc "They aren't? Shit... I think I picked the wrong school. I swear that was in the brochure!"
                    la "Haha. [mc]..."
                    scene 03_053 with Dissolve(1)
                    la "Okay, fine. I did try out a couple years ago. Wasn't my thing."
                    mc "I won't be seeing you in a cheerleading outfit then?"
                    if Layla_Points >= 11:
                        la "Haha. Maybe one day."
                        la "But hey, I can always ask Elena for you."
                    else:
                        la "Haha. I could always ask Elena for you, though."
                    scene 03_054 with Dissolve(1)
                    mc "What team are you on then?"
                    la "Track and field!"
                    mc "Of course. That explains the running today."
                    scene 03_055 with Dissolve(1)
                    la "Yeah, well... At least before I got interrupted and dragged into the grass."
                    mc "Dragged? Wow. That's what I get for trying to help?"
                    la "Haha, I'm kidding. I'm glad you showed up."
                    scene 03_056 with Dissolve(1)
                    la "Anyway, I should actually get those laps in. Only have about twenty minutes before I need to head home."
                    la "How about you?"
                    mc "I'm good for today. Exhausted already from my few laps earlier."
                    scene 03_057 with Dissolve(1)
                    la "Alright, I'll let you off the hook this time. But next time, we run together, got it?"
                    la "Well... If you can keep up."
                    mc "Haha. Deal."
                    scene 03_058 with Dissolve(1)
                    mc "Hey! If that guy shows up again, call me, okay?"
                    mc "Here, take my number."
                    la "Smooth move... Is this how you usually get girls' numbers?"
                    mc "Damn, Busted. Guess it's time to find a new park."
                    la "Haha. No need. I'll gladly take it!"
                    if Layla_Points >= 11:
                        la "Thank you, [mc]."
                        show 03_059
                        pause 3
                        mc "..."
                        scene 03_060 with Dissolve(1)
                        la "Hehe. Bye."
                        mc "Bye, Layla..."
                        mc "{i}(That came as a surprise.){/i}"
                    else:
                        scene 03_060 with Dissolve(1)
                        la "Thank you, [mc]."
                        mc "Bye, Layla."
                        la "Bye."
                    jump Week1_Wednesday_Park_Alexis

label Week1_Wednesday_Park_Alexis:
    scene black with Dissolve(1)
    pause 2
    scene 03_061 with Dissolve(1)
    if Layla_Week1_Wednesday_ParkStay == False:
        mc "{i}(I've been running for a while now, but I still can't decide which team to join.){/i}"
        mc "{i}(Should I go with Zach's suggestion and join his team? Or maybe try out for basketball?){/i}"
        mc "{i}(Then there's the obvious one. Track and field... That's definitely on the table too.){/i}"
        mc "{i}(Something to consider, for sure.){/i}"
        play sound "Sounds/Phone_Vibrate.mp3"
        n "*Bzzzt. Bzzzt*"
        scene 03_062 with Dissolve(1)
        mc "{i}(Unknown number?){/i}"
    else:
        mc "{i}(Didn't expect Layla to be on the track team...){/i}"
        mc "{i}(But that might be a solid choice. I've always liked running, and people say I'm pretty fast.){/i}"
        mc "{i}(Something to consider, for sure.){/i}"
        play sound "Sounds/Phone_Vibrate.mp3"
        n "*Bzzzt. Bzzzt*"
        scene 03_062 with Dissolve(1)
        mc "{i}(Is she calling me already? Don't tell me that guy is still around.){/i}"
        mc "{i}(No... It's an unknown number...){/i}"
    if Alexis_Friends == True:
        $ Alexis_Week1_Wednesday_PhoneIgnore = True
        mc "{i}(Whatever...){/i}"
        mc "{i}(Probably just a wrong number.){/i}"
        jump Week1_Wednesday_Home
    else:
        menu:
            "Ignore[KoGa3AutoWTChange1]{size=-4}(Alexis Week1 Wednesday PhoneIgnore, Alexis Points-4) {/size} {/color}":
                $ Alexis_Week1_Wednesday_PhoneIgnore = True
                $ Alexis_Points -= 4
                mc "{i}(Whatever...){/i}"
                mc "{i}(Probably just a wrong number.){/i}"
                jump Week1_Wednesday_Home
            "Pick up[KoGa3AutoWTChange1]{size=-4}(Alexis Week1 Wednesday PhonePickup, Alexis Points+2) {/size} {/color}":
                $ Alexis_Week1_Wednesday_PhonePickup = True
                $ Alexis_Points += 2
                # Alexis (12)
                scene 03_063 with Dissolve(1)
                mc "Hello?"
                x "Come over! Now!"
                mc "{i}(What?){/i}"
                mc "Who is this?"
                scene 03_064 with Dissolve(1)
                a "You get so many girls calling you that you don't know who this is?"
                mc "Alexis?"
                if Alexis_Week1_Monday_BarWait == False:
                    a "Uh-huh. Wanna hang out?"
                else:
                    a "Uh-huh. Now get your ass over here!"
                scene 03_065 with Dissolve(1)
                mc "I just finished my run. Kinda need to shower first."
                a "We have a shower."
                mc "Uh... What?"
                scene 03_066 with Dissolve(1)
                a "You need a shower. We have a shower. So stop wasting time and get over here."
                if Alexis_Week1_Monday_BarWait == False:
                    a "I'll text you the address."
                else:
                    a "You remember the way, right?"
                    mc "{i}(How could I forget?){/i}"
                menu:
                    "Go home[KoGa3AutoWTChange1]{size=-4}({i}Alexis Week1 Monday BarWaitFalse: Alexis Friends, Alexis Points-4{/i}) {/size} {/color}":
                        if Alexis_Week1_Monday_BarWait == False:
                            $ Alexis_Friends = True
                            $ Alexis_Points -= 4
                            scene 03_067 with Dissolve(1)
                            mc "Sorry. I can't..."
                            a "Okay. I get it."
                            mc "..."
                            mc "Alexis?"
                            mc "She hung up."
                            mc "{i}(Whatever...){/i}"
                        else:
                            scene 03_067 with Dissolve(1)
                            mc "Sorry, Alexis. Not today. Maybe tomorrow?"
                            a "Hmm... Can't tomorrow."
                            a "But hey, I've got your number now. I'll call again sometime."
                            mc "Sure. Sounds good. Speak to you then. Bye, Alexis."
                            a "Bye, [mc]."
                            mc "{i}(How did she get my number?){/i}"
                        jump Week1_Wednesday_Home
                    "Go to her place[KoGa3AutoWTChange1]{size=-4}(Alexis Week1 Wednesday PhoneHome, Alexis Points+2, MC SexCounter+1, SexCounter Alexis+1) {/size} {/color}":
                        $ Alexis_Week1_Wednesday_PhoneHome = True
                        $ Alexis_Points += 2
                        # Alexis (14)
                        $ MC_SexCounter += 1
                        $ SexCounter_Alexis += 1
                        # Alexis_Sex (3)
                        scene 03_068 with Dissolve(1)
                        mc "Alright. I..."
                        a "Kay. See you in ten!"
                        mc "Wait! Alex..."
                        mc "..."
                        scene 03_069 with Dissolve(1)
                        if Alexis_Week1_Monday_BarWait == False:
                            mc "She hung up..."
                            mc "{i}('See you in ten'. I don't even know where you live yet!){/i}"
                            mc "{i}Hopefully it's not too far from here...{/i}"
                        else:
                            mc "She hung up..."
                            mc "{i}('See you in ten'. I'm not even close to her house.){/i}"
                            mc "{i}Looks like I'll be doing some more running after all...{/i}"
                        jump Week1_Wednesday_Alexis_Shower

label Week1_Wednesday_Alexis_Shower:
    if _in_replay:
        $ Alexis_Week1_Monday_BarWait = True
    scene black with Dissolve(2)
    pause 2
    if Alexis_Week1_Monday_BarWait == False:
        scene 03_070 with Dissolve(1)
        mc "{i}(There's no way...){/i}"
        mc "{i}(This is the correct address, right?){/i}"
        mc "{i}(Why would someone like her work at a bar if she's loaded?){/i}"
        mc "{i}(Maybe she owns the bar after all, just didn't want to say anything?){/i}"
    else:
        pass
    scene 03_071 with Dissolve(1)
    mc "{i}(Man... why am I so nervous all of a sudden? Are her parents home?){/i}"
    mc "..."
    mc "{i}(Probably not. She wouldn't have invited me if they were...){/i}"
    stop music fadeout 1.0
    scene 03_072 with Dissolve(1)
    play music ("Music/LoFi Upbeat 1.mp3", "Music/LoFi Upbeat 2.mp3", "Music/LoFi Upbeat 3.mp3", "Music/LoFi Upbeat 4.mp3") volume 0.2
    a "Hi."
    mc "Hey."
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 03_073 at moveup
    pause 3
    mc "{i}(Damn...){/i}"
    a "You weren't kidding about needing a shower. You're soaked."
    a "Did you miss me that much? Ran the whole way here?"
    scene 03_074 with Dissolve(1)
    mc "..."
    mc "You gave me ten minutes and hung up before I could even say anything."
    a "Sorry..."
    scene 03_075 with Dissolve(1)
    mc "Uh... and you? You always answer the door like this?"
    mc "Not that I'm complaining..."
    a "Haha, no. I knew it was you."
    mc "What if it wasn't? What if it was like... The mailman or something?"
    scene 03_076 with Dissolve(1)
    a "Well... Lucky him, I guess?"
    mc "..."
    a "What?"
    mc "Nothing. Just... Never mind."
    a "Heh..."
    scene 03_077 with Dissolve(1)
    a "Come on, don't just stand there. Get inside already."
    mc "Jeez. So bossy..."
    a "Told you I was."
    scene 03_078 with Dissolve(1)
    mc "So... How are you?"
    a "I'm good. You?"
    mc "Can't complain."
    a "Mm-hmm."
    scene 03_079 with Dissolve(1)
    a "Shower's upstairs."
    mc "Got it."
    scene 03_080 with Dissolve(1)
    mc "Hey, just curious... How'd you even get my number?"
    a "Hmm? I have my ways. I can be very resourceful."
    mc "Alexis..."
    a "Haha. Just teasing."
    scene black with Dissolve(1)
    pause 2
    scene 03_081 with Dissolve(1)
    z "Hey, Alexis. Mind grabbing me an iced tea?"
    a "Sure, Zach."
    a "..."
    a "{i}(Maybe I could just ask him...){/i}"
    a "Hey, do you happen to have [mc]'s number?"
    scene 03_082 with Dissolve(1)
    z "Of course I do, babe."
    a "*Sigh* Can you give it to me?"
    z "Oho... Someone had a good time, huh?"
    a "..."
    a "Just the number, Zach. Please."
    scene 03_083 with Dissolve(1)
    z "Hehe. What's in it for me?"
    a "An iced tea!"
    z "Nah, I meant something a little more... exciting."
    a "..."
    scene 03_084 with Dissolve(1)
    a "*Shakes head* You know what? Forget it."
    z "Whoa, hey! I'm just messing with you. Chill, Alexis..."
    a "..."
    scene 03_085 with Dissolve(1)
    z "Here you go."
    a "Thanks."
    a "And one more thing. Don't tell him I asked, okay?"
    z "Haha. My lips are sealed. This is gonna be fun..."
    scene 03_086 with Dissolve(1)
    z "Wait... Take my number too."
    a "Yeah, I'm good. I'll get you that iced tea."
    a "{i}(He really doesn't quit, does he?){/i}"
    scene black with Dissolve(1)
    pause 2
    scene 03_087 with Dissolve(1)
    mc "Well, that explains why he was acting weird at school this morning."
    a "At least he kept his word."
    mc "Yeah. He's a bit much sometimes, but honestly, he's a decent guy."
    menu:
        "Look closer":
            scene 03_088 with Dissolve(1)
            a "The shower's the first door on the right."
            mc "Sorry. What?"
            scene 03_089 with Dissolve(1)
            a "Shower. First door on the right."
            mc "Right. Got it. See you in a bit."
        "Don't":
            a "The shower's the first door on the right."
            mc "Cool. Thanks. See you in a bit."
    scene black with Dissolve(1)
    pause 2
    stop music fadeout 1.0
    scene 03_090 with Dissolve(1)
    play music ("Sounds/Shower.mp3") volume 0.2
    mc "{i}(Nothing beats a shower after a run...){/i}"
    mc "{i}(And this walk-in shower? So nice.){/i}"
    mc "{i}(Wish we had one back home...){/i}"
    scene 03_091 with Dissolve(1)
    mc "*Humming*"
    a "..."
    scene 03_092 with Dissolve(1)
    mc "Alexis!"
    a "Why are you taking forever in there? We've got stuff to do!"
    mc "Stuff we... Wait, what are you...?"
    scene 03_093 with Dissolve(1)
    a "Patience has never been my thing."
    mc "Uh..."
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 03_094 at moveup
    pause 3
    mc "{i}(Damn...){/i}"
    scene 03_095 with Dissolve(1)
    a "Can I join you?"
    mc "You... Uh..."
    show 03_096
    a "..."
    show 03_097
    pause 3
    a "I'll take that as a yes!"
    mc "Eh..."
    scene 03_098 with Dissolve(1)
    mc "Wait... Is this the infamous no-coffee option?"
    a "Haha, you remember that? This might just be."
    mc "Kinda hard to forget..."
    mc "But apparently, I do forget to lock doors."
    a "Lucky for me! Otherwise, I'd look pretty stupid standing in front of a locked door in my towel."
    mc "I wouldn't say stupid. Silly? Yeah! Stupid? No..."
    scene 03_099 with Dissolve(1)
    mc "Communi..."
    a "Haha. Don't say it! Why does that keep happening? You are stupid and silly, you know that?"
    mc "Yeah. Can't deny that."
    scene 03_100 with Dissolve(1)
    mc "Anyway. I just need like five more minutes and..."
    a "..."
    mc "Uhm..."
    scene 03_101 with Dissolve(1)
    a "Do I look like I want to wait five more minutes?"
    mc "Alex..."
    a "Shush and kiss me already!!"
    scene 03_102 with Dissolve(1)
    a "..."
    mc "{i}(There's no way I can say no to her...){/i}"
    scene 03_103 with Dissolve(1)
    ""
    scene 03_104 with Dissolve(1)
    ""
    scene 03_105 with vpunch
    a "Ah..."
    scene 03_106 with Dissolve(1)
    ""
    scene 03_107 with Dissolve(1)
    a "Mmm..."
    scene 03_108 with Dissolve(1)
    ""
    scene 03_109 with Dissolve(1)
    ""
    scene 03_110 with Dissolve(1)
    a "Stop teasing me and put it in!"
    mc "Are you that horny?"
    a "..."
    mc "No... Impatient was the word!"
    a "Both!"
    scene 03_111 with Dissolve(1)
    ""
    scene 03_112 with Dissolve(1)
    a "Ahh..."
    show 03_113
    ""
    show 03_114
    ""
    scene 03_115 with Dissolve(1)
    mc "..."
    mc "{i}(I love the way she looks at me.){/i}"
    scene 03_116 with vpunch
    a "Ahh..."
    mc "Sorry. I didn't mean to push you that hard."
    scene 03_117 with Dissolve(1)
    a "Someone's a little rough today!"
    mc "Too much?"
    a "No, it's fine. Keep going."
    scene 03_118 with Dissolve(1)
    mc "If it's getting too much, tell me, okay?"
    a "Mmm..."
    scene 03_119 with Dissolve(1)
    ""
    scene 03_120 with Dissolve(1)
    mc "..."
    scene 03_121 with Dissolve(1)
    a "Ahh..."
    show 03_122
    ""
    scene 03_123 with Dissolve(1)
    a "Mmm..."
    show 03_124
    a "*Moaning*"
    show 03_125
    ""
    show 03_126
    mc "{i}(This feels so good!){/i}"
    mc "{i}(Her pussy is amazing!){/i}"
    show 03_127
    ""
    scene 03_128 with Dissolve(1)
    a "Haah..."
    a "I'm..."
    scene 03_129 with Dissolve(1)
    a "I'm close..."
    x "Lexi!"
    scene 03_130 with vpunch
    a "Shit!"
    mc "{i}(Who's that?){/i}"
    scene 03_131 with Dissolve(1)
    a "Hey. Uh... You're back early."
    x "Yeah. Something came up."
    x "Do you need much longer? I need to use the bathroom."
    stop music fadeout 1.0
    scene 03_132 with Dissolve(1)
    play music ("Music/LoFi Upbeat 3.mp3", "Music/LoFi Upbeat 2.mp3", "Music/LoFi Upbeat 4.mp3", "Music/LoFi Upbeat 1.mp3") volume 0.2
    a "Uh... Not much longer. Almost done."
    x "Why's the door locked?"
    a "Just needed some privacy, that's all."
    mc "{i}(Good thing she remembered to lock it.){/i}"
    x "You never do that."
    a "Just use the other bathroom!"
    x "My stuff is in here, though."
    scene 03_133 with Dissolve(1)
    mc "*Whisper* Who's that?"
    a "Sssh..."
    a "Let me dry off real quick. I'll come get you when it's clear."
    x "Alright..."
    scene 03_134 with Dissolve(1)
    a "Talk about bad timing..."
    mc "Yeah. Couldn't have been worse..."
    mc "So. Who..."
    a "No time for that now. Let's hurry."
    scene black with Dissolve(1)
    pause 2
    scene 03_135 with Dissolve(1)
    a "Okay, get dressed, and I'll make sure no one sees you leave."
    a "Let yourself out, yeah?"
    mc "Got it..."
    scene 03_136 with Dissolve(1)
    a "Hey, I'm sorry. Don't look so sad. I feel bad..."
    a "I'll make it up to you. Promise."
    mc "*Nods*"
    show 03_137
    pause 3
    a "Bye, [mc]."
    mc "Bye, Lexi..."
    scene 03_138 with Dissolve(1)
    $ Alexis_Lexi = True
    a "Hey!"
    a "{i}(That just made my heart skip a beat.){/i}"
    $ renpy.end_replay()
    jump Week1_Wednesday_Home

label Week1_Wednesday_Home:
    scene black with Dissolve(2)
    pause 2
    stop music fadeout 1.0
    scene 03_139 with Dissolve(1)
    play music ("Music/LoFi Indie 3.mp3", "Music/LoFi Indie 1.mp3", "Music/LoFi Indie 2.mp3") volume 0.2
    m "Oh... Hey, honey."
    mc "Hey, Mom."
    m "How was your day?"
    mc "Eventful... To say the least."
    scene 03_140 with Dissolve(1)
    m "Let me introduce you. This is Rachel."
    if Rachel_End == True:
        mc "Hi."
        ra "Hello. Nice to meet you."
        m "Rachel will be managing the new café once it opens."
        mc "Oh, that's great. Congratulations. And good luck."
        ra "Thanks. I appreciate it."
        scene 03_141 with Dissolve(1)
        mc "Mom, before I forget. There are some school forms you need to sign."
        m "Sure. Just put them on my desk."
        mc "Will do."
        scene 03_142 with Dissolve(1)
        mc "{i}(She looks familiar... Where have I...?){/i}"
        mc "{i}(Wait. Right. The flight attendant...){/i}"
    else:
        mc "{i}(Oh, fuck!){/i}"
        mc "{i}(What is she doing here?){/i}"
        mc "Uhm... Hi."
        ra "Hello. Nice to meet you."
        scene 03_143 with Dissolve(1)
        m "Rachel will be managing the new café once it opens."
        mc "Oh, that's great. Congratulations. And good luck."
        ra "Thank you."
        scene 03_141 with Dissolve(1)
        mc "Mom, before I forget. There are some school forms you need to sign."
        m "Sure. Just put them on my desk."
        mc "Will do."
        scene 03_142 with Dissolve(1)
        mc "{i}(Seriously? Of all people...){/i}"
        mc "{i}(Please don't say anything about the plane...){/i}"
        scene black with Dissolve(1)
        pause 2
        scene 03_144 with Dissolve(1)
        mc "{i}(Alright. Time to finish this assignment and forget about that awkward moment.){/i}"
    if Alexis_Week1_Wednesday_PhoneHome == True:
        play sound "Sounds/Phone_Message.mp3"
        n "*Bzzzt*"
        scene 03_145 with Dissolve(1)
        mc "{i}(Hmm? A message from Alexis...){/i}"
        a "Hey. I'm sorry about earlier. I hope you're not mad at me. I swear I'll make it up to you. Lexi."
        mc "{i}(Heh... She thinks I'm mad. Cute.){/i}"
        mc "..."
        scene 03_146 with Dissolve(1)
        mc "{i}(Now I can't stop thinking about the shower again... Focus, man.){/i}"
        mc "{i}(But who was that at her place?){/i}"
        mc "{i}(Her mom, maybe? Or a sister? She never mentioned having one...){/i}"
    else:
        pass
    if Rachel_End == True:
        jump Week1_Thursday_School
    else:
        jump Week1_Wednesday_Rachel

label Week1_Wednesday_Rachel:
    scene 03_147 with Dissolve(1)
    ra "Hey there."
    mc "Uhm... Hey?"
    mc "If you're looking for the bathroom, it's the next door."
    scene 03_148 with Dissolve(1)
    ra "I'm exactly where I want to be."
    ra "Don't you remember me?"
    mc "How could I forget the flight assistant who blue balled me!"
    ra "Heh..."
    scene 03_149 with Dissolve(1)
    ra "Let me make it up to you."
    ra "How about we finish what we started on the plane?"
    mc "You must not be too impressed with the new job if you're already chasing your boss's son."
    scene 03_150 with Dissolve(1)
    ra "Just a little fun on the side. Maybe we both stand to gain something from this relationship."
    mc "And what kind of 'relationship' would that be?"
    ra "Why don't I show you?"
    menu:
        "Reject[KoGa3AutoWTChange1]{size=-4}(Rachel End) {/size} {/color}":
            $ Rachel_End = True
            scene 03_151 with Dissolve(1)
            mc "Not interested."
            mc "And you better leave now or this won't be the only door that will be slammed in your face."
            ra "..."
            scene 03_152 with Dissolve(1)
            ra "I always knew you were just a foolish boy."
            mc "Hehe yup, that's me. A foolish boy. Bye, Raquelle."
            ra "It's Rachel!"
            mc "Whatever..."
            mc "{i}(Back to the assignment.){/i}"
            $ renpy.end_replay()
            jump Week1_Thursday_School
        "Agree":
            scene 03_153 with Dissolve(1)
            mc "You know what I think? Our encounter on the plane wasn't so random after all."
            ra "That's why you leave the thinking to me."
            ra "Now just sit back and enjoy."
            scene 03_154 with Dissolve(1)
            mc "{i}(Oh shit...){/i}"
            mc "{i}(This is really happening!){/i}"
            scene 03_155 with Dissolve(1)
            ra "..."
            scene 03_156 with vpunch
            mc "Heh..."
            mc "You don't waste any time, huh?"
            scene 03_157 with Dissolve(1)
            mc "{i}(It is weird that she scares me a bit?){/i}"
            mc "{i}(She doesn't really scare me... What's the word? Intimidate!){/i}"
            scene 03_158 with Dissolve(1)
            ra "Your friend here doesn't want to join?"
            mc "Uh..."
            ra "Good thing I brought toys!"
            scene 03_159 with Dissolve(1)
            mc "{i}(Can't wait to see those puppies!){/i}"
            mc "{i}(They must be huge!){/i}"
            scene black with Dissolve(1)
            transform moveup:
                xalign 0.5 yalign 1.0
                linear 5.0 yalign 0.0
            show 03_160 at moveup
            pause 3
            mc "{i}(They are!){/i}"
            mc "{i}(Holy shit!){/i}"
            scene 03_161 with Dissolve(1)
            ra "So, what do you think?"
            mc "They... They look incredible."
            ra "They better! They cost me a fortune!"
            scene 03_162 with Dissolve(1)
            mc "Uh..."
            mc "{i}(So that's what fake boobs feel like.){/i}"
            scene 03_163 with Dissolve(1)
            ra "And there he is!"
            ra "Knew he wouldn't be able to resist playing!"
            ra "Now lean back and keep quiet. Don't want your mother barging in and interrupting us. I need this job."
            mc "{i}(Would she really be doing this if she needed the job?){/i}"
            scene 03_164 with Dissolve(1)
            mc "{i}(Something's definitely off about her... But hell, might as well enjoy this.){/i}"
            show 03_165
            ""
            show 03_166
            mc "{i}(This is so hot!){/i}"
            scene 03_167 with Dissolve(1)
            mc "Oh, fuck...!"
            scene 03_168 with Dissolve(1)
            ra "You like this, don't you?"
            mc "Just don't stop halfway, like last time."
            scene 03_169 with Dissolve(1)
            ra "How about we pick up where we left off on the plane?"
            ra "I'll make sure you finish!"
            scene 03_170 with Dissolve(1)
            mc "{i}(If she keeps going like this, finishing won't be a problem.){/i}"
            mc "{i}(In fact, I'm close already...){/i}"
            mc "{i}(Very close...){/i}"
            scene 03_171 with Dissolve(1)
            mc "{i}(Damn...){/i}"
            mc "{i}(She took my whole...){/i}"
            mc "{i}(I can feel my dick in her throat.){/i}"
            scene 03_172 with Dissolve(1)
            ra "Haah-haah..."
            mc "Fuck! Do you suck dick as a profession or something?"
            ra "Heh... Just gifted!"
            show 03_173
            ""
            show 03_174
            ""
            show 03_175
            mc "..."
            mc "{i}(I'm...){/i}"
            scene 03_176 with vpunch
            pause 2
            scene 03_177 with vpunch
            mc "Haa... Haa..."
            scene 03_178 with Dissolve(1)
            ra "Tasty."
            mc "Fuck, that was amazing!"
            mc "You did more than make up for last time."
            ra "Heh..."
            scene 03_179 with Dissolve(1)
            ra "If you want more of this, it stays just between us. Got it?"
            mc "Sure..."
            ra "I'd better head back downstairs now, before your mom starts looking for me."
            scene 03_180 with Dissolve(1)
            ra "I'll be in touch. See you around."
            mc "Yeah. See you."
            mc "{i}(She's crazy... But somehow... I like it.){/i}"
            $ renpy.end_replay()
            jump Week1_Thursday_School

label Week1_Thursday_School:
    scene black with Dissolve(2)
    pause 2
    n "Thursday, 08:22. School."
    stop music fadeout 1.0
    scene 03_181 with Dissolve(1)
    play music ("Music/LoFi Upbeat 3.mp3", "Music/LoFi Upbeat 2.mp3", "Music/LoFi Upbeat 1.mp3", "Music/LoFi Upbeat 4.mp3") volume 0.2
    mc "Good morning."
    re "Good morning, [mc]."
    re "What can I do for you?"
    scene 03_182 with Dissolve(1)
    mc "I brought the documents you asked for last time."
    re "Ah, perfect. Let me take a look."
    scene 03_183 with Dissolve(1)
    re "Hmm..."
    re "Track and field. Good choice. Mike's an excellent coach."
    mc "Mike?"
    x "Yes?"
    scene 03_184 with Dissolve(1)
    re "Oh... Speak of the devil. Good morning, Mike."
    tm "The devil, huh? Good morning."
    scene 03_185 with Dissolve(1)
    tm "What can I do for you, Natasha?"
    re "Well... Meet [mc]."
    re "Your new track and field student."
    scene 03_186 with Dissolve(1)
    tm "Hey, [mc]. Welcome to the team! Great to have you aboard."
    mc "Good morning, sir. Thank you."
    tm "No need for sir. Mike or Coach works just fine."
    menu:
        "Mike[KoGa3AutoWTChange1]{size=-4}(Mike Name) {/size} {/color}":
            $ Mike_Name = True
            mc "Mike."
        "Coach":
            mc "Coach."
    scene 03_187 with Dissolve(1)
    tm "I saw you try out for football a few days ago."
    tm "The moment I saw you sprint, I figured I'd come talk to you about giving track a shot."
    tm "Looks like I don't have to anymore."
    mc "Yeah, football wasn't really my thing. But I've always enjoyed running, so..."
    tm "Good call! We definitely need some fresh competition to shake things up."
    scene 03_188 with Dissolve(1)
    tm "Alright, no time to waste."
    tm "Change into your gear and meet me on the field. Warm-up starts in five."
    mc "Will do."
    scene 03_189 with Dissolve(1)
    tm "See you later, Natasha!"
    re "Uh, yes. Later, Mike..."
    scene 03_190 with Dissolve(1)
    re "Isn't he just dreamy!"
    mc "What?"
    scene 03_191 with Dissolve(1)
    re "What?"
    re "{i}(Did I say that out loud?){/i}"
    re "*Clears throat* Nothing! Off you go. Coach Mike's waiting."
    mc "Yeah... Uh, bye."
    scene black with Dissolve(2)
    pause 2
    stop music fadeout 1.0
    play music ("Music/Indie-Electro 1.mp3", "Music/Indie-Electro 2.mp3", "Music/Indie-Electro 3.mp3", "Music/Indie-Electro 4.mp3") volume 0.2
    scene 03_192 with Dissolve(1)
    tm "Ah, you're here."
    tm "Listen up, everyone. Let me introduce you to [mc]. He's joining our team."
    tm "[mc], you might already know a few people here. I'm sure you'll get to know everyone else in no time."
    if Mike_Name == True:
        mc "Thanks, Mike."
        da "Mike..."
    else:
        mc "Thanks, Coach."
    scene 03_193 with Dissolve(1)
    la "Hey, [mc]. Welcome!"
    mc "Hey. Good morning, Layla."
    tm "Okay, no time to waste. Warm-up laps! Let's go!"
    if Layla_Week1_Wednesday_ParkHelp == False:
        scene 03_194 with Dissolve(1)
        la "I'm happy you decided to join the track team."
        mc "Same. Seems like a fun group."
        la "Ehh..."
        mc "What?"
        la "You'll find out soon enough."
    else:
        if Layla_Week1_Wednesday_ParkStay == False:
            scene 03_194 with Dissolve(1)
            la "Hey, about yesterday at the park. I'm sorry for snapping at you."
            la "I had a bad day, and I'm sorry I took it out on you, especially since you were helping me."
            mc "No worries. I've already forgotten about all that."
            la "Thanks. Seriously, I'm glad you're here."
            mc "Same. Seems like a fun group."
        else:
            scene 03_194 with Dissolve(1)
            la "I'm happy you decided to join the track team."
            mc "Same. Seems like a fun group."
            la "Ehh..."
            mc "What?"
            la "You'll find out soon enough."
    scene black with Dissolve(1)
    pause 2
    scene 03_195 with Dissolve(1)
    tm "Come on, Darryl! Pick it up! No slacking!"
    da "..."
    da "Hey, it's not just me here!"
    scene 03_196 with Dissolve(1)
    mc "So, who's who?"
    la "Uhm... Let's see..."
    la "Behind us are Darryl, Tori and TJ. I think you have some classes with them."
    la "The girls up front are Emma and Zola..."
    scene black with Dissolve(1)
    pause 2
    scene 03_197 with Dissolve(1)
    ""
    scene 03_198 with Dissolve(1)
    mc "*Heavy breathing*"
    da "Look at the new guy. He looks done already. Probably the first and last time we see him on the track."
    la "..."
    da "Ten bucks says he's puking before we're done."
    tj "Yeah, not taking that bet."
    scene 03_199 with Dissolve(1)
    la "Are you okay, [mc]?"
    mc "*Heavy breathing*"
    mc "Yeah... I just... Need a... Minute..."
    scene 03_200 with Dissolve(1)
    mc "Are the warm-ups always this brutal?"
    la "Uhm... I don't want to discourage you or anything but... Normally, they are a lot harder."
    la "I think Coach took it easy today since you're new."
    mc "{i}(What? This was supposed to be easy? Are you kidding me? I'm in trouble.){/i}"
    scene 03_201 with Dissolve(1)
    mc "I'm a natural sprinter. Very dangerous over short distances!"
    la "Hmm? Okay."
    mc "{i}(Right... Guess she's never seen Lord of the Rings...){/i}"
    mc "Gotta start working on my endurance first though."
    la "Yeah, might be a good idea."
    scene 03_202 with Dissolve(1)
    tm "Alright, team! Split up. Guys and girls."
    tm "Girls, you'll be working on your start. Boys, on acceleration with interval training."
    scene 03_203 with Dissolve(1)
    mc "Guess we're training separately then."
    la "Today we are."
    mc "Well, have fun, and see you later then."
    la "You too. And try to make some friends with the other members."
    mc "Haha. You sound like my mom."
    la "I'm serious. Just... don't isolate yourself, okay? It's better that way. Trust me."
    scene 03_204 with Dissolve(1)
    mc "{i}(Hmm...){/i}"
    mc "{i}(Did something happen before?){/i}"
    mc "{i}(Was she the odd person out? Maybe someone else?){/i}"
    scene 03_205 with Dissolve(1)
    da "Keep on moving!"
    mc "{i}(What's this guy's problem?){/i}"
    mc "{i}(I haven't even spoken to him. Chill, dude.){/i}"
    scene black with Dissolve(1)
    pause 2
    scene 03_206 with Dissolve(1)
    tm "And go!"
    mc "{i}(What?){/i}"
    scene 03_207 with Dissolve(1)
    mc "{i}(Oh... Fuck!){/i}"
    scene 03_208 with Dissolve(1)
    mc "{i}(Damn that Darryl guy is fast...){/i}"
    da "..."
    da "*Shakes head*"
    tm "Let's do that again. Line up!"
    scene black with Dissolve(1)
    pause 2
    scene 03_209 with Dissolve(1)
    la "How're you doing? Still holding on?"
    mc "Barely. I feel like my lungs are about to explode."
    la "Haha, come on... It's not that bad."
    la "I was watching you. You held your own out there."
    mc "You think? Thanks..."
    scene 03_210 with Dissolve(1)
    tm "Nice work, everyone! That's the kind of effort I want to see every day!"
    tm "Since we've got a bit of time left... How about a little fun?"
    tm "It's been a while since we did some one-on-one races."
    tm "Let's bring it back. Who's up first...?"
    tm "Alright... Tori, you're racing... Layla!"
    scene 03_211 with Dissolve(1)
    mc "You got this, Layla!"
    la "Thanks."
    to "Heh... She's gonna need more than luck!"
    la "..."
    scene 03_212 with Dissolve(1)
    tm "Ready, girls?"
    tm "On my whistle!"
    n "*Whistle*"
    scene 03_213 with Dissolve(1)
    mc "{i}(They got a pretty even start I'd say.){/i}"
    mc "{i}(Let's see who pushes on ahead.){/i}"
    scene 03_214 with Dissolve(1)
    mc "{i}(Halfway, and they're still neck and neck... Maybe Tori has the edge?){/i}"
    mc "{i}(It's a good match up.){/i}"
    mc "{i}(This is way more intense up close than on TV.){/i}"
    mc "{i}(Come on, Layla!){/i}"
    scene 03_215 with Dissolve(1)
    mc "{i}(Damn... That must've been so close.){/i}"
    mc "{i}(Who actually won? Did Layla manage to catch her at the end?){/i}"
    scene 03_216 with Dissolve(1)
    mc "{i}(Looks like Tori won.){/i}"
    tm "Well done, Tori. Well done, Layla. Great race!"
    tm "Next..."
    scene 03_217 with Dissolve(1)
    tm "Darryl..."
    tm "You're up against... [mc]!"
    da "What?"
    mc "{i}(Oh... Me already?){/i}"
    scene 03_218 with Dissolve(1)
    da "Are you serious, Coach?"
    da "I know there is no competition for me here but at least give me someone who can make it a tiny bit interesting."
    tm "You racing, or running your mouth?"
    da "..."
    scene 03_219 with Dissolve(1)
    da "Do yourself a favour and just stay at the starting line."
    da "That way you won't embarrass yourself even more than you already did."
    mc "..."
    scene 03_220 with Dissolve(1)
    mc "{i}(He's right about one thing. There's no way I can win but let's try my best and not embarrass myself.){/i}"
    mc "{i}(Come on! I can do this!){/i}"
    da "*Shakes head*"
    tm "Ready?"
    scene 03_221 with Dissolve(1)
    n "*Whistle*"
    mc "{i}(Holy shit!){/i}"
    mc "{i}(How is he this fast off the line?! That acceleration...){/i}"
    scene 03_222 with Dissolve(1)
    mc "{i}(Faster... Faster!){/i}"
    mc "{i}(Don't let the gap grow!){/i}"
    scene 03_223 with Dissolve(1)
    da "{i}(Wait... What the hell? He's keeping up?){/i}"
    da "{i}(Not just that, he's...){/i}"
    scene 03_224 with Dissolve(1)
    da "Fuck...!"
    mc "{i}(Wait... Did I win?){/i}"
    scene 03_225 with Dissolve(1)
    la "..."
    tj "Darryl lost?"
    to "Oh wow... This just got interesting!"
    scene 03_226 with Dissolve(1)
    tm "Looks like you've got some real competition now, Darryl!"
    da "Heh..."
    tm "Anyway. Good race, boys!"
    tm "Next up! Emma versus Zola."
    scene 03_227 with Dissolve(1)
    to "Here you go!"
    mc "Uh... Thanks."
    la "..."
    scene 03_228 with Dissolve(1)
    tj "Can't believe the new guy beat you, Darryl."
    da "Shut up! I was just taking it easy. Besides, I'm wearing my high-tops. Didn't know we were going to race."
    da "Next time, I'll make him regret joining the team."
    scene 03_229 with Dissolve(1)
    tj "So what's going on with you and Tori?"
    da "Beats me. Probably just playing her usual games."
    da "She'll come running back soon enough."
    scene 03_230 with Dissolve(1)
    to "Nice race. Seriously impressive. About time Darryl got his ass handed to him."
    mc "Heh? Thanks, I guess."
    scene 03_231 with Dissolve(1)
    da "What did you say, bitch?"
    to "Did I stutter? Keep moving, loser. Don't you have another cousin to make out with?"
    mc "{i}(Here we go again...){/i}"
    scene 03_232 with Dissolve(1)
    da "Who are you calling a loser?"
    to "Haha. Not only are your legs slow. Your hearing is as well."
    da "Shut up, Tori."
    scene 03_233 with Dissolve(1)
    tj "Let it go, Darryl. She's baiting you."
    da "She's lucky she's a girl. I want to punch her so badly."
    to "Haha. Bye, Felicia."
    da "..."
    scene 03_234 with Dissolve(1)
    to "Don't mind him. He's a bonehead."
    mc "..."
    to "I'm Tori, by the way."
    mc "[mc]."
    to "Oh, I know who you are."
    scene 03_235 with Dissolve(1)
    to "So... I noticed you checking me out earlier."
    mc "{i}(Did I? Well, she was racing Layla and I was watching the race, but...){/i}"
    menu:
        "Yeah":
            mc "Yeah. You looked great out there. Super fast."
            mc "I was impressed."
        "Not really":
            mc "I was watching the race and..."
            to "Mmm, sure you were..."
            mc "{i}(Guess I'll play along...){/i}"
            mc "Uh yeah. Nice running..."
    scene 03_236 with Dissolve(1)
    to "You've seen nothing yet."
    to "You need work on your start, though. I could give you some pointers."
    to "Still room for improvement."
    scene 03_237 with Dissolve(1)
    mc "I agree."
    mc "This was my first time sprinting like this. I mean one-on-one on a track. So, I'm starting basically from zero."
    mc "But I'll get there... Trust the process, right?"
    scene 03_238 with Dissolve(1)
    to "Cute. But we're a long way from Philly."
    mc "Haha. You got that reference?"
    to "Babe, please. There's a lot of things I get."
    to "Especially when it's something I want."
    scene 03_239 with Dissolve(1)
    to "Well... See you around, [mc]."
    to "And if you ever want that advice, you know where to find me."
    mc "Heh... See you, Tori"
    jump Week1_Thursday_Cafeteria

label Week1_Thursday_Cafeteria:
    scene black with Dissolve(2)
    pause 2
    stop music fadeout 1.0
    play music ("Music/LoFi Upbeat 1.mp3", "Music/LoFi Upbeat 2.mp3", "Music/LoFi Upbeat 3.mp3", "Music/LoFi Upbeat 4.mp3") volume 0.2
    scene 03_240 with Dissolve(1)
    mc "{i}(Looks like she gave it everything at training.){/i}"
    mc "{i}(Or maybe she's still upset about losing to Tori?){/i}"
    menu:
        "Leave":
            mc "{i}(Better not bother her right now.){/i}"
        "Bring her coffee[KoGa3AutoWTChange1]{size=-4}(Layla Points+2) {/size} {/color}":
            scene 03_241 with Dissolve(1)
            $ Layla_Points += 2
            # Layla (16)
            mc "{i}(Maybe some coffee will do the trick?){/i}"
            mc "{i}(I was getting one anyway. Let's get her one too.){/i}"
            scene 03_242 with Dissolve(1)
            la "..."
            scene 03_243 with Dissolve(1)
            la "Oh... is this for me?"
            mc "Sorry if I woke you. Yeah, it's for you. Thought you could use one."
            la "Thanks, [mc]."
            la "This is exactly what I needed."
            la "Come on. Sit with me."
            scene 03_244 with Dissolve(1)
            mc "You sure?"
            la "Haha, yes! You're officially invited to my table."
            mc "Haha, thanks."
            scene 03_245 with Dissolve(1)
            mc "All alone today? Where's your other half?"
            la "Elena? She's still at cheer practice. Should be done soon."
            mc "Got it."
            la "Your race against Darryl was awesome. You're really fast!"
            mc "You think so? Thanks, Layla! So are you. I hope you don't mind me joining the team."
            la "Not at all! I'm actually glad. It'll shake things up a bit. Plus, it's a fun group."
            scene 03_246 with Dissolve(1)
            la "Well... most days. Except when Tori and Darryl are at each other's throats."
            mc "Yeah, I've seen those two go at it before."
            la "It's constant drama. Every week, something new."
            if Layla_Points >= 11:
                scene 03_247 with Dissolve(1)
                la "Hmm..."
                mc "What?"
            else:
                pass
            scene 03_248 with Dissolve(1)
            la "I saw you talking to Tori earlier."
            mc "Yeah, she was giving me tips about my start. Said it needs work."
            la "Just... be careful with her, [mc]. She has a bit of a reputation."
            mc "Oh? What kind of reputation?"
            scene 03_249 with Dissolve(1)
            el "Hey, guys."
            la "Hi, El."
            mc "Hey."
            scene 03_250 with Dissolve(1)
            mc "Well... I should get going."
            el "Uhm. You don't have to leave because of me..."
            mc "I was just dropping off coffee for Layla."
            la "Yeah, don't rush off! Stay a while."
            scene 03_251 with Dissolve(1)
            mc "Next time, alright?"
            la "Okaaay..."
            mc "Enjoy, girls."
            el "Bye, [mc]."
            scene 03_252 with Dissolve(1)
            el "Sorry. Did I scare him off?"
            el "Was I interrupting something? Or... does he not like me?"
            la "What? No, nothing like that. Well... maybe he doesn't..."
            el "What?"
            la "Kidding! I'm kidding. Why would he hate you? You two had a blast in chemistry, didn't you?"
            el "*Nods*"
            scene 03_253 with Dissolve(1)
            el "What were you two talking about?"
            la "Him joining the track team... and Tori."
            el "Oh, he joined? That's cool. As for Tori... *sigh* He better be careful. She's gonna be all over him."
            la "Yeah, she already started chatting him up."
            el "Dios mío!"
    scene 03_254 with Dissolve(1)
    n "*Bzzzt*"
    mc "{i}(Hmm... Message from Mom.){/i}"
    scene 03_255 with Dissolve(1)
    m "{i}(Hey honey. How's your day? I'll be home late, so I won't be able to make dinner. Just grab something or order out. Love you!){/i}"
    mc "{i}(Guess I'll go somewhere to eat. You'd think being a restaurant owner's kid, I'd know how to cook... but yeah, not even close.){/i}"
    mc "{i}(Maybe I'll check out the food at the bar. Zach said it's actually really good.){/i}"
    if Alexis_Friends == False:
        mc "{i}(And maybe I'll run into Alexis while I'm there.){/i}"
    else:
        pass
    jump Week1_Thursday_DylanBar

label Week1_Thursday_DylanBar:
    scene black with Dissolve(2)
    pause 2
    n "Thursday, 17:46. Dylan's Bar and BBQ."
    stop music fadeout 1.0
    scene 03_256 with Dissolve(1)
    play music "Sounds/Bar_Background.mp3" volume 0.3
    if Alexis_Friends == False:
        bd "Hey there."
        mc "Hey."
        mc "Alexis working today?"
        bd "Not today, no. Can I pass on a message?"
        mc "No, it's fine. I was just curious. I actually came by to grab a bite."
        bd "Good choice of establishment. What can I get you?"
    else:
        bd "Hey there."
        mc "Hey."
        bd "What can I get you?"
    scene 03_257 with Dissolve(1)
    mc "I'll have the steak with fries, please."
    bd "How would you like your steak?"
    mc "Medium-rare."
    bd "And to drink?"
    mc "An iced tea."
    bd "Alright. Coming right up."
    mc "Thanks."
    scene 03_258 with Dissolve(1)
    bt "One iced tea."
    mc "*Nods* Thank you!"
    bt "Cool sleeve!"
    mc "Appreciate it. You too, man. Both of 'em."
    bt "Haha, thanks, man."
    scene black with Dissolve(1)
    pause 2
    scene 03_259 with Dissolve(1)
    bd "Here you go!"
    mc "Now this is a steak. Looks and smells incredible!"
    bd "Tastes even better. You'll see."
    mc "{i}(Perfect grill marks... nice char...){/i}"
    mc "{i}(Let's find out if Zach was telling the truth about this place.){/i}"
    scene black with Dissolve(1)
    pause 2
    scene 03_260 with Dissolve(1)
    mc "{i}(Damn... That was a good steak!){/i}"
    mc "{i}(One of the best I've ever had. Maybe the best?){/i}"
    mc "{i}(You got some competition here, Mom!){/i}"
    scene 03_261 with Dissolve(1)
    bd "Looks like you enjoyed it?"
    mc "I did. I did!"
    mc "The flavour, the texture... it was juicy and perfectly cooked. Amazing steak."
    bd "That's what I like to hear."
    scene 03_262 with Dissolve(1)
    bd "So... you're new around here, right? I haven't seen you before."
    mc "Yeah. Just moved back to Madison about a week ago."
    scene 03_263 with Dissolve(1)
    bd "Moved back? So you're originally from here?"
    mc "Yeah. Grew up here until I was maybe twelve or so. Been a while."
    to "..."
    scene 03_264 with Dissolve(1)
    to "Would you look at that!"
    to "Couldn't have planned it better myself."
    x "Hmm?"
    scene 03_265 with Dissolve(1)
    to "Go ahead without me. I'll catch up later."
    x "Alright. Have fun, Tori."
    to "You know I will."
    scene 03_266 with Dissolve(1)
    to "Heeey... Guess who."
    mc "What...? Uhm?"
    scene 03_267 with Dissolve(1)
    mc "{i}(That voice...){/i}"
    mc "{i}(I've definitely heard it before. Someone from school?){/i}"
    menu:
        "Tori":
            mc "{i}(Hmm... Could this be Tori? Maybe... Sounds like her, no?){/i}"
            mc "Tori?"
            scene 03_268 with Dissolve(1)
            to "Correct! I knew you'd recognise my beautiful voice."
            mc "Heh... Right."
        "Zach":
            mc "{i}(Let's see how she reacts to this.){/i}"
            mc "Uh... Zach?"
            scene 03_269 with Dissolve(1)
            to "What?"
            mc "Oh... Hey, Tori."
            to "Do I sound like a guy to you? How can you not recognise my beautiful voice?"
            mc "Heh. Right."
        "Guess[KoGa3AutoWTChange1]{size=-4}(Sienna Name) {/size} {/color}":
            $ Sienna_Name = True
            mc "{i}(Let's just make a random guess. How about...){/i}"
            mc "Sienna?"
            to "What? No. Who is Sienna?"
            scene 03_268 with Dissolve(1)
            mc "Oh... Hey, Tori."
            to "Hey! How could you not recognise my beautiful voice?"
            mc "Heh. Right."
    scene 03_270 with Dissolve(1)
    to "So... What brings you out tonight?"
    mc "Hunger, mostly. Just came to get something to eat."
    scene 03_271 with Dissolve(1)
    to "Here? *Sigh...* You have so much to learn. There are better places to go eat, you know?"
    bd "{i}(What is she talking about? She knows nothing about my grilling techniques.){/i}"
    mc "Actually, the steak I had was really good. You should try it."
    bd "{i}(He gets it!){/i}"
    mc "What about you? What brings you here?"
    to "Out with the girls. But then I saw this cutie at the bar."
    scene 03_272 with Dissolve(1)
    mc "Cutie?"
    mc "Damn. Dylan gets all the good compliments. Hot, sexy, and now cute."
    bd "What's that now?"
    mc "Heh... Nothing man."
    to "Why are you listening to our conversation? Don't you have glasses to clean or something?"
    mc "{i}(That was uncalled for, Tori...){/i}"
    scene 03_273 with Dissolve(1)
    to "Anyway... Back to us. Well... To me!"
    to "What do you think of me?"
    mc "{i}(Straight to the point, huh?){/i}"
    mc "{i}(Wait...? Is she...?){/i}"
    scene 03_274 with Dissolve(1)
    to "..."
    mc "{i}(Yup... her hand's already on my thigh.){/i}"
    scene 03_275 with Dissolve(1)
    la "..."
    la "{i}(Tori... Of course. Please, [mc]... Just don't.){/i}"
    menu:
        "Interested":
            jump Week1_Thursday_DylanBar_Tori
        "Not interested":
            jump Week1_Thursday_DylanBar_Layla

label Week1_Thursday_DylanBar_Tori:
    if _in_replay:
        $ Layla_Points = 14
        $ Tori_Points = 0
        $ Tori_Week1_Interested = True
        $ MC_SexCounter = 0
        $ SexCounter_Tori = 0
    scene 03_276 with Dissolve(1)
    $ Tori_Sex = True
    $ Layla_Points -= 4
    $ Tori_Week1_Interested = True
    $ Tori_Points += 2
    # Tori (2)
    $ MC_SexCounter += 1
    $ SexCounter_Tori += 1
    # Tori_Sex (1)
    to "I think I got my answer."
    to "Actions speak louder than words!"
    mc "{i}(Can't help it if you rub my...){/i}"
    scene 03_277 with Dissolve(1)
    mc "{i}(She's not wasting any time, that's for sure.){/i}"
    scene 03_278 with Dissolve(1)
    la "..."
    la "{i}(*Shakes head* Really, Tori? Him too?){/i}"
    scene 03_279 with Dissolve(1)
    mc "{i}(I've gotta admit... those plump lips of hers. Kind of addictive.){/i}"
    to "{i}(Mmm... He's a good kisser. I could get used to this...){/i}"
    to "..."
    to "{i}(Who am I kidding...?){/i}"
    scene 03_280 with Dissolve(1)
    to "Let's get out of here and continue this somewhere else."
    mc "Alright. Where are we going?"
    to "I know a nice place."
    scene black with Dissolve(1)
    pause 2
    stop music fadeout 1.0
    play music ("Music/LoFi Indie 1.mp3", "Music/LoFi Indie 3.mp3", "Music/LoFi Indie 2.mp3") volume 0.2
    scene 03_281 with vpunch
    mc "So... This is your idea of a 'nice place'?"
    to "Babe. Any place with me in it is nice. Period!"
    mc "..."
    scene 03_282 with Dissolve(1)
    mc "So, why are we really here?"
    to "Oh, come on. Don't play dumb. You know exactly why we're here."
    mc "I mean... Aren't you with Darryl?"
    to "Who?"
    to "Besides... that didn't stop *you* from coming with *me*."
    mc "{i}(Touché...){/i}"
    scene 03_283 with Dissolve(1)
    to "You looked so hot during the race against Darryl."
    mc "Who?"
    to "Haha. I knew you were fun!"
    scene 03_284 with Dissolve(1)
    ""
    scene 03_285 with Dissolve(1)
    to "..."
    scene 03_286 with Dissolve(1)
    to "No! We're not doing that!"
    mc "What? Changed your mind?"
    to "Let's just fuck!"
    scene 03_287 with Dissolve(1)
    mc "..."
    scene 03_288 with Dissolve(1)
    to "{i}(He's bigger than I thought. I might actually enjoy this.){/i}"
    scene 03_289 with Dissolve(1)
    to "Mmm..."
    mc "{i}(Uh...){/i}"
    mc "{i}(I thought she...){/i}"
    scene 03_290 with Dissolve(1)
    mc "I thought we're just going to fuck?"
    to "See this as a prize for beating Darryl!"
    scene 03_291 with Dissolve(1)
    ""
    scene 03_292 with Dissolve(1)
    mc "{i}(Fuck yeah...){/i}"
    show 03_293
    ""
    show 03_294
    ""
    scene 03_295 with Dissolve(1)
    mc "Damn, this is amazing!"
    to "You think that's amazing?"
    to "Wait until you put your dick in my pussy!"
    to "And I think it's about time you put this thing to work and show me what you can do."
    scene 03_296 with Dissolve(1)
    mc "..."
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 03_297 at moveup
    pause 3
    to "What are you looking at?"
    to "Never seen a pussy before?"
    mc "I have..."
    to "Admittedly... It's the prettiest pussy you've ever seen!"
    scene 03_298 with vpunch
    to "What are you waiting for?"
    to "Put it in and fuck me already!"
    scene 03_299 with Dissolve(1)
    ""
    scene 03_300 with Dissolve(1)
    to "Mmm..."
    scene 03_301 with Dissolve(1)
    to "Give it to me!"
    scene 03_302 with vpunch
    to "Ahh..."
    to "This is more like it! I knew you were fun!"
    show 03_303
    ""
    show 03_304
    ""
    show 03_305
    to "{i}(Oh my god... Darryl who?){/i}"
    to "Holy shit!"
    to "{i}(Who would've thought?){/i}"
    to "Yeah... Ah... Keep going."
    show 03_306
    ""
    show 03_307
    ""
    show 03_308
    to "*Moaning*"
    scene 03_309 with vpunch
    pause 1
    scene 03_309 with vpunch
    mc "..."
    scene black with Dissolve(1)
    pause 2
    scene 03_310 with Dissolve(1)
    to "I guess I'll have to teach you more than just sprinting."
    mc "..."
    to "Still... that wasn't too bad."
    mc "Not too bad? I heard your moans... I think it was better than not too bad!"
    to "Heh..."
    scene 03_311 with Dissolve(1)
    to "We'll keep it at not too bad!"
    to "Anyway... I'm heading back inside. Thanks for the... fun."
    mc "Anytime. See you around, Tori."
    to "Anytime? I like that!"
    scene 03_312 with Dissolve(1)
    to "{i}(This was supposed to be a one-time thing... but he surprised me.){/i}"
    to "{i}(Maybe I'll keep him around a bit longer... For a little more fun now and then.){/i}"
    $ renpy.end_replay()
    jump Week1_Friday_School

label Week1_Thursday_DylanBar_Layla:
    scene 03_313 with Dissolve(1)
    mc "Sorry, Tori. I'm not interested."
    mc "You're just... not my type."
    la "..."
    to "What are you even saying? Not your type? I'm everyone's type!"
    mc "{i}(Heh... That's a little presumptuous.){/i}"
    scene 03_314 with Dissolve(1)
    to "Let me prove it to you!"
    mc "Not interested, Tori!"
    mc "..."
    mc "{i}(She just doesn't stop, huh? How do I shut this down?){/i}"
    if Alexis_Friends == False:
        mc "{i}(Hmm...){/i}"
        mc "{i}(If Alexis were here, she'd probably back me up...){/i}"
    else:
        mc "{i}(Maybe someone can bail me out in a way...){/i}"
    scene 03_315 with Dissolve(1)
    mc "{i}(Wait... Layla's here? Perfect timing, I guess...){/i}"
    mc "{i}(Sorry to drag you into this, Layla, but I don't know what else I should do.){/i}"
    scene 03_316 with Dissolve(1)
    to "Come on. Let's just get out of here and have a little fun. You won't regret it."
    mc "How many more times do I have to repeat myself? I'm not interested, Tori!"
    to "Like hell you aren't. I saw you stare at me. You want this. Me!"
    mc "What? When? I never stared... And besides... I have a girlfriend."
    to "Sure you do. The girlfriend card. How convenient. How come I don't believe you?"
    scene 03_317 with Dissolve(1)
    mc "Believe what you want. But she's right over there."
    mc "{i}(I hope this works...){/i}"
    to "Who? Layla?"
    scene 03_318 with Dissolve(1)
    la "Why are they looking over here? Are they talking about us?"
    x "Seems like it."
    scene 03_319 with Dissolve(1)
    mc "Yes, Layla!"
    to "Really? Miss 'never had a boyfriend'?"
    to "You expect me to buy that? Haha."
    to "Then why isn't she with you right now?"
    mc "..."
    scene 03_320 with Dissolve(1)
    to "How about you prove it?"
    mc "What?"
    to "If she's really your girlfriend, show me!"
    mc "Why do I have to prove anything to you?"
    to "It's either that or the whole school will know what a pathetic liar you are."
    scene 03_321 with Dissolve(1)
    mc "{i}(Damn it... Should've listened to the people who warned me about her.){/i}"
    mc "{i}(And who is she to call me pathetic? She can't take rejection. That's pathetic!){/i}"
    to "So... What's it gonna be?"
    mc "*Sigh* Alright."
    mc "{i}(Why didn't I just walk away when I had the chance?){/i}"
    scene 03_322 with Dissolve(1)
    mc "Hey there."
    la "Hi, [mc]."
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 03_323 at moveup
    pause 3
    mc "{i}(And I thought the skirt she wore at school was short... Damn...){/i}"
    mc "{i}(She looks good!){/i}"
    scene 03_324 with Dissolve(1)
    la "I don't think you two have met properly yet, right? This is Sienna!"
    if Sienna_Name == True:
        mc "{i}(Sienna? What are the odds?){/i}"
        mc "Hi. Nice to meet you, Sienna."
    else:
        mc "Hi. Nice to meet you, Sienna."
    si "Hey. You too, [mc]."
    scene 03_325 with Dissolve(1)
    la "How are you? Having fun back there with... Tori?"
    mc "Yeah. So... much... fun..."
    la "Haha."
    la "Looked like you guys were talking about us back there."
    mc "Hmm...? Yeah, kinda... That's actually why I came over. I need a favour."
    scene 03_326 with Dissolve(1)
    la "Oh? Intriguing..."
    la "Okay. Shoot."
    mc "Well... I think I figured out what kind of person Tori is."
    la "Uh-huh."
    mc "She's... intense. Doesn't handle rejection well at all."
    mc "I tried turning her down, but she just wouldn't back off. So... I kinda told her you were my girlfriend... To get her off my back."
    scene 03_327 with Dissolve(1)
    la "Your...? Your girlfriend?"
    mc "Yeah... Sorry to involve you in this. I didn't know what else to do."
    la "No, it's... It's... It's fine."
    la "Is that all?"
    mc "Not quite. She didn't believe me. Told me to 'prove it' or she'd tell the whole school I'm a liar."
    scene 03_328 with Dissolve(1)
    la "Technically she's not wrong. You did lie."
    mc "I know. It was a dumb move. I just panicked..."
    mc "*Sigh* Well, I'll figure something out. Sorry again for dragging you into it."
    scene 03_329 with Dissolve(1)
    la "Hey! I never said no..."
    la "Besides... I don't like Tori either. Last thing you want is a rumour from her spreading. Trust me."
    la "I'll help you."
    mc "Really? Thank you so much, Layla."
    la "Sure."
    scene 03_330 with Dissolve(1)
    la "Sorry to leave you alone, Sienna. Won't take long."
    si "No worries. Go do your thing. I'll grab some popcorn and enjoy the drama."
    la "Hehe. Be right back."
    scene 03_331 with Dissolve(1)
    la "Let's show her we are the cutest cou... 'fake' couple at school."
    mc "Haha... Thanks."
    scene 03_332 with Dissolve(1)
    la "Hey... Tori..."
    to "Layla..."
    la "So, I heard you can't keep your hands off my boyfriend."
    to "Yeah... Your 'boyfriend'. Funny..."
    scene 03_333 with Dissolve(1)
    to "What, you think just standing next to each other proves anything?"
    mc "You're being ridiculous. What else do you want?"
    to "Make out with her..."
    mc "Heh... We're not just gonna kiss for your entertainment."
    mc "And even if we did, what would that prove?"
    mc "I could make out with Dylan. Doesn't mean we're dating."
    scene 03_334 with Dissolve(1)
    bd "..."
    bd "{i}(First he calls me cute... Now he wants to make out with me?){/i}"
    if Alexis_Friends == False:
        $ Dylan_Week1_Assumption = True
        bd "{i}(Is he into me?){/i}"
        bd "{i}(Maybe that's why he didn't mind that Alexis isn't working tonight...){/i}"
        bd "{i}(I better give her a heads-up before she gets the wrong idea about him.){/i}"
    else:
        bd "{i}(Is he into me?){/i}"
    scene 03_335 with Dissolve(1)
    mc "Sorry, Layla. Looks like there's no reasoning with her. Let's just go."
    la "Actually no... It's fine."
    la "Let's shut her up for good!"
    mc "What?"
    scene 03_336 with Dissolve(1)
    mc "..."
    mc "{i}(She really...?){/i}"
    scene 03_337 with Dissolve(1)
    mc "{i}(Let's make this even more convincing!){/i}"
    to "..."
    scene 03_338 with Dissolve(1)
    to "Okay-okay! I get it... You can stop now!"
    to "Ugh, what a waste of time..."
    x "Tori? Where are you going? Wait up...!"
    scene 03_339 with Dissolve(1)
    la "Haha. I think it worked."
    mc "Is she gone?"
    la "Yup, she stormed right out."
    if Layla_Points <= 13:
        scene 03_340 with Dissolve(1)
        mc "Thank you so much for this, Layla!"
        mc "You really saved me. I don't know what I would've done without you."
        la "My pleasure. I've always wanted to get back at Tori."
        mc "If there's anything I can do to return the favour, just say the word, okay?"
        scene 03_341 with Dissolve(1)
        la "Hmm... Let's see..."
        la "Oh! I've got something."
        scene 03_342 with Dissolve(1)
        if Layla_Week1_Wednesday_ParkStay == False:
            la "You speak Spanish, right?"
            mc "I do."
            la "Would you mind helping me out with some Spanish lessons?"
        else:
            la "Is your offer to teach me Spanish still open?"
            mc "Of course."
            la "Great! Could really use the help."
        scene 03_343 with Dissolve(1)
        mc "Yeah, sure. I'd be happy to."
        la "Cool."
        mc "Anything else?"
        la "There might be something else but I'll save that for later."
        mc "Hehe, alright."
        scene 03_344 with Dissolve(1)
        la "Well... I think I've left Sienna alone long enough."
        mc "Yeah. Tell her I'm sorry for stealing you away."
        la "You don't wanna come join us?"
        mc "Thanks, but I should head out. You two enjoy yourselves."
        la "Okay. See you tomorrow?"
        mc "I'll be at school, yeah."
        scene 03_345 with Dissolve(1)
        mc "Thanks again! Seriously, you're the best!"
        la "You're welcome."
        mc "Bye, Layla!"
        la "Bye."
        jump Week1_Friday_School
    else:
        mc "{i}(I was so into that kiss I didn't even realise...){/i}"
        scene 03_346 with Dissolve(1)
        mc "Thank you so much for this, Layla!"
        mc "You really saved me. I don't know what I would've done without you."
        la "My pleasure. I've always wanted to get back at Tori."
        mc "{i}(It was my pleasure kissing you!){/i}"
        scene 03_347 with Dissolve(1)
        mc "..."
        la "..."
        scene 03_348 with Dissolve(1)
        la "{i}(What's wrong with me?){/i}"
        la "{i}(I just want to keep kissing him...){/i}"
        la "{i}(Is it because he said I was his girlfriend? I know it was just to get rid of Tori, but... I actually liked it.){/i}"
        scene 03_349 with Dissolve(1)
        mc "Uh? What was that for?"
        mc "Not that I mind... I..."
        scene 03_350 with Dissolve(1)
        mc "Layla?"
        la "Sorry, I..."
        mc "It's fine."
        scene 03_340 with Dissolve(1)
        mc "Besides, I owe you big time for this."
        la "Yeah, you do!"
        mc "So, anything I can do to return the favour?"
        scene 03_341 with Dissolve(1)
        la "Hmm... Let's see..."
        la "Oh! I've got something."
        scene 03_342 with Dissolve(1)
        if Layla_Week1_Wednesday_ParkStay == False:
            la "You speak Spanish, right?"
            mc "I do."
            la "Would you mind helping me out with some Spanish lessons?"
        else:
            la "Is your offer to teach me Spanish still open?"
            mc "Of course."
            la "Great! Could really use the help."
        mc "Uh yeah. Sure."
        la "Cool."
        scene 03_343 with Dissolve(1)
        la "There might be one more thing."
        mc "Shoot!"
        scene 03_351 with Dissolve(1)
        mc "Oh..."
        mc "{i}(Another kiss, huh?){/i}"
        scene 03_352 with Dissolve(1)
        mc "{i}(Not saying no to that!){/i}"
        if Alexis_Friends == True:
            pass
        else:
            mc "{i}(Suddenly not so upset Alexis isn't working today!){/i}"
        scene 03_353 with Dissolve(1)
        mc "That was easy enough."
        la "Oh no... That wasn't it."
        mc "It wasn't? Then... Was that maybe our breakup kiss?"
        la "Haha. Sure, why not."
        scene 03_354 with Dissolve(1)
        la "..."
        la "{i}(I wouldn't mind if we just kept pretending.){/i}"
        la "{i}(Or maybe not even pretending?){/i}"
        la "{i}(God, what am I thinking? I barely know him...){/i}"
        scene 03_343 with Dissolve(1)
        mc "So what's the other thing I can do for you?"
        la "*Whispers* That's a secret for later."
        mc "Hehe. Okay."
        scene 03_344 with Dissolve(1)
        la "Well... I think I've left Sienna alone long enough."
        mc "Yeah. Tell her I'm sorry for stealing you away."
        la "You don't wanna come join us?"
        mc "Thanks, but I should head out. You two enjoy yourselves."
        scene 03_355 with Dissolve(1)
        la "Okay. See you tomorrow?"
        mc "I'll be at school, yeah."
        mc "Thanks again! Seriously, you're the best!"
        la "You're welcome."
        scene 03_345 with Dissolve(1)
        mc "Bye, Layla!"
        la "Bye."
        jump Week1_Thursday_Layla_Home

label Week1_Thursday_Layla_Home:
    scene black with Dissolve(2)
    pause 2
    stop music fadeout 1.0
    scene 03_356 with Dissolve(1)
    play music ("Music/LoFi Upbeat 1.mp3", "Music/LoFi Upbeat 2.mp3", "Music/LoFi Upbeat 3.mp3", "Music/LoFi Upbeat 4.mp3") volume 0.2
    la "*Happy scream* KYAAA..."
    la "{i}(I can't stop thinking about it...){/i}"
    la "{i}(I really kissed him...){/i}"
    scene 03_357 with Dissolve(1)
    la "Haha..."
    la "{i}(Can't wait to see him again tomorrow.){/i}"
    la "{i}(But what should I even say to him?){/i}"
    la "..."
    scene 03_358 with Dissolve(1)
    x "Hey, Layla. What's with all the screaming?"
    la "Hmm...?"
    scene 03_359 with Dissolve(1)
    la "Kyaaaa..."
    x "Okay. Now I really need to know what's going on."
    scene 03_360 with Dissolve(1)
    x "So? What happened?"
    la "Well..."
    scene 03_361 with Dissolve(1)
    la "There's this boy at my school."
    x "Oh? I should've guessed it's about a boy..."
    x "Don't keep me waiting! Spill everything!"
    jump Week1_Friday_School

label Week1_Friday_School:
    scene black with Dissolve(2)
    pause 2
    n "Friday, 08:17. School."
    stop music fadeout 1.0
    play music ("Music/LoFi Upbeat 3.mp3", "Music/LoFi Upbeat 2.mp3", "Music/LoFi Upbeat 1.mp3", "Music/LoFi Upbeat 4.mp3") volume 0.2
    if Tori_Week1_Interested == True:
        scene 03_362 with Dissolve(1)
        mc "Hey, Zach."
        z "Heya! What's up?"
        mc "I finally joined a team yesterday."
        z "Oh, you did? Which one?"
        mc "Track and field."
        scene 03_363 with Dissolve(1)
        z "That's actually a good choice for you. I told you before that you're fast."
        z "And hey... you'll be running with Layla, right? Those tight training outfits... Damn, lucky you!"
        z "Just thinking about that makes me want to switch teams!"
        mc "Haha..."
        scene 03_364 with Dissolve(1)
        mc "Oh... Morning, Tori."
        to "Hmm? What? Do I know you?"
        mc "..."
        to "Yeah! That's what I thought. Don't talk to me!"
        scene 03_365 with Dissolve(1)
        to "You show someone a good time once, and they suddenly can't leave you alone..."
        mc "{i}(What the fuck? I just said good morning...){/i}"
        scene 03_366 with Dissolve(1)
        z "You know Tori?"
        mc "Hmm... Not really."
        z "Right. She's on the track team too."
        z "But trust me. Keep it that way. She's got a... reputation. Half the school's been with her. She's trouble, man."
        mc "{i}(Yup. Figured as much...){/i}"
        z "She's nasty man. I wouldn't touch her with a ten-foot pole."
        scene 03_367 with Dissolve(1)
        mc "Anyway... Got any plans for the weekend?"
        z "Not yet, but we should definitely do something."
        scene 03_368 with Dissolve(1)
        z "It's your first weekend back—we've gotta go big!"
        z "I'll ask around, check what my teammates are up to. There's always something going on."
        z "Hit you up later."
        mc "Sounds good."
        z "Cool. Time for class. Gabi's waiting! Later!"
        mc "Haha... Later, Zach."
        jump Week1_Friday_Geography
    else:
        scene 03_362 with Dissolve(1)
        mc "Hey, Zach."
        z "Heya. What's up?"
        mc "I finally joined a team yesterday."
        z "Oh, you did? Which one?"
        mc "Track and field."
        scene 03_369 with Dissolve(1)
        z "That's actually a good choice for you. I told you before that you're fast."
        z "And hey... you'll be running with Layla, right? Those tight training outfits... Damn, lucky you!"
        z "Just thinking about that makes me want to switch teams!"
        mc "Haha..."
        scene 03_370 with hpunch
        mc "Aah!"
        z "..."
        scene 03_371 with Dissolve(1)
        mc "{i}(What the...? That really caught me off guard...){/i}"
        scene 03_372 with Dissolve(1)
        el "Hey there, loverboy."
        mc "{i}(Loverboy?){/i}"
        mc "Elena... You scared me!"
        scene 03_373 with Dissolve(1)
        el "Haha."
        la "Morning, guys."
        z "Hey, Layla."
        mc "Good morning."
        scene 03_374 with Dissolve(1)
        el "I know what you did last night. Naughty boy!"
        mc "..."
        el "We'll talk later."
        scene 03_375 with Dissolve(1)
        la "Oh my god, Elena! I told you not to say anything."
        el "Sorry, Layla. I couldn't resist."
        la "Ugh, this is so embarrassing... How am I supposed to look him in the eye now?"
        el "Same way you always do. Flirt with him."
        scene 03_376 with Dissolve(1)
        z "What was that all about?"
        z "Feels like you're hiding something from me."
        mc "Let's just say... I owe Layla a big favour."
        z "Oh really? You better spill the details later."
        scene 03_367 with Dissolve(1)
        z "Anyway... Any plans for the weekend?"
        mc "No, nothing yet."
        scene 03_368 with Dissolve(1)
        z "It's your first weekend back—we've gotta go big!"
        z "I'll ask around, check what my teammates are up to. There's always something going on."
        z "Hit you up later."
        mc "Sounds good."
        z "Cool. Time for class. Gabi's waiting! Later!"
        mc "Haha... Later, Zach."
        jump Week1_Friday_Geography

label Week1_Friday_Geography:
    scene black with Dissolve(1)
    pause 2
    scene 03_377 with Dissolve(1)
    tc "I've got your results from yesterday's test."
    tc "There were some good ones, some bad ones, and a few surprises."
    tc "I'm going to hand them out now and we'll discuss them."
    scene 03_378 with Dissolve(1)
    tc "I expected more from you, Layla. Not your best."
    la "Sorry..."
    scene 03_379 with Dissolve(1)
    la "*Sigh*"
    mc "{i}(Looks like she didn't do too well...){/i}"
    mc "{i}(What did she get?){/i}"
    scene 03_380 with Dissolve(1)
    tc "And here we have a surprise."
    tc "Way to prove me wrong, [mc]. Good job. Keep it up!"
    mc "Thank you."
    scene 03_381 with Dissolve(1)
    la "Surprise?"
    la "Meaning you didn't fail?"
    mc "Funny..."
    la "What grade did you get? Can I see?"
    mc "Uh... Sure."
    scene 03_382 with Dissolve(1)
    la "Thanks."
    la "Let's see..."
    scene 03_383 with Dissolve(1)
    la "..."
    scene 03_384 with Dissolve(1)
    la "You've gotta be kidding me."
    la "Is this a joke?"
    scene 03_385 with Dissolve(1)
    mc "What do you mean?"
    la "This! How? Did you cheat?"
    mc "What? No..."
    scene 03_386 with Dissolve(1)
    la "Then how? I thought you were bad at geography."
    mc "I never said that. You just assumed."
    la "..."
    scene 03_387 with Dissolve(1)
    la "Whatever..."
    mc "Haha. What now?"
    la "Nothing."
    scene 03_388 with Dissolve(1)
    mc "What's your score?"
    la "Aaah! No!"
    la "That's none of your business!"
    scene 03_389 with Dissolve(1)
    mc "Heh... That good, huh?"
    la "..."
    mc "Come on, just let me see!"
    scene 03_390 with Dissolve(1)
    la "Don't talk to me, cheater!"
    mc "Haha. I didn't cheat though."
    scene 03_391 with Dissolve(1)
    el "Hey... What are you two lovebirds bickering about?"
    scene 03_392 with Dissolve(1)
    la "Here..."
    la "Look at this."
    el "Alright."
    scene 03_393 with Dissolve(1)
    el "Oh... An A+. Good job, Layla."
    el "Was Coleman being sarcastic earlier? I thought you didn't do too well..."
    la "No. Check the name."
    el "Hmm? Oooh... Wait! What?"
    scene 03_394 with Dissolve(1)
    el "Did you cheat?"
    mc "Oh come on. You too, Elena? I didn't cheat."
    el "Yeah, right."
    scene 03_395 with Dissolve(1)
    la "See! Two versus one. Meaning you cheated."
    mc "Where's the logic in that? And of course you two stick together..."
    la "Hehe."
    scene 03_396 with Dissolve(1)
    mc "*Sigh* You girls are something else."
    la "Haha."
    tc "Alright. Let's start with the first question."
    scene black with Dissolve(1)
    pause 2
    n "Friday, 12:08. School cafeteria."
    scene 03_397 with Dissolve(1)
    "..."
    scene 03_398 with Dissolve(1)
    el "Would you look at that. Who do we have here?"
    mc "Don't say it."
    el "How do you know what I'm about to say?"
    mc "Just a feeling."
    el "Haha..."
    scene 03_399 with Dissolve(1)
    la "Come join us at our table."
    mc "Uh, okay. Thanks."
    if Layla_Points >= 13:
        scene 03_400 with Dissolve(1)
        el "So what were you doing here all alone, lonely boy?"
        el "Still no friends? You've been here for a week already."
        mc "You might be right about that."
        el "That's sad...!"
        scene 03_401 with Dissolve(1)
        la "He has me!"
        la "I'll be your friend."
        scene 03_402 with Dissolve(1)
        la "Right?"
        mc "Uh..."
        scene 03_403 with Dissolve(1)
        mc "..."
        scene 03_404 with Dissolve(1)
        mc "Layla..."
        el "*Clears throat* Uhum..."
        scene 03_405 with Dissolve(1)
        el "I know I told you to flirt with him, Layla. But can't this wait until tonight?"
        la "Haha. I was just teasing."
        mc "{i}(She's not even trying to hide it. She really is a tease...){/i}"
        scene 03_406 with Dissolve(1)
        mc "What's happening tonight?"
        el "Well... If you don't have plans, why not join Layla and me?"
        el "We're going clubbing tonight."
        scene 03_407 with Dissolve(1)
        mc "Yeah? Sounds great. I'm in."
        mc "Which club?"
        la "It's called Heaven. It's in the city."
        mc "Hmm... Never heard of it. It is new?"
        la "No, not really."
        scene 03_408 with Dissolve(1)
        z "You guys are going to Heaven tonight?"
        el "Of course he heard that."
        z "Can I come?"
        el "Mmm..."
        scene 03_409 with Dissolve(1)
        z "Please? I'll behave. I promise."
        el "Sure. Whatever."
        la "The more the merrier, right?"
        z "Woohoo... This will be awesome!"
        el "Dios mío... I'm already regretting it."
        jump Week1_Friday_Club
    else:
        scene 03_401 with Dissolve(1)
        la "What are your plans for the weekend? Or more specifically, tonight?"
        mc "Actually, nothing yet."
        mc "I'm waiting for Zach to fill me in."
        scene 03_406 with Dissolve(1)
        el "Well, if you're free, how about joining Layla and me?"
        el "We're going clubbing later."
        scene 03_407 with Dissolve(1)
        mc "Yeah? Sounds great. I'd love to join you. Thanks."
        mc "Which club?"
        la "It's called Heaven. It's in the city."
        mc "Hmm... Never heard of it. Is it new?"
        la "No, not really."
        scene 03_408 with Dissolve(1)
        z "You guys are going to Heaven tonight?"
        el "Of course he heard that."
        z "Can I come?"
        el "Mmm..."
        scene 03_409 with Dissolve(1)
        z "Please? I'll behave. I promise."
        el "Sure. Whatever."
        la "The more the merrier, right?"
        z "Woohoo... This will be awesome!"
        el "Dios mío... I'm already regretting it."
        jump Week1_Friday_Club

label Week1_Friday_Club:
    scene black with Dissolve(2)
    pause 2
    n "Friday, 19:48. Madison Springs city."
    stop music fadeout 1.0
    scene 03_410 with Dissolve(1)
    play music "Sounds/Street_Traffic.mp3" volume 0.3
    z "I can't believe you've never been to Heaven before."
    mc "I've only been back for five days, and when I left Madison, I was like twelve or so...?"
    mc "When exactly was I supposed to go?"
    z "Time to make up for lost time, then!"
    scene 03_411 with Dissolve(1)
    z "I'm so happy they asked me to join."
    mc "What? You literally begged them to let you come with."
    z "Nah, you got it all wrong. That was all part of the plan. Reverse psychology, you know?"
    mc "Right..."
    mc "{i}(Does he even know what reverse psychology is?){/i}"
    scene 03_412 with Dissolve(1)
    z "Man... I can't wait. I'm pumped!"
    z "Looking good, feeling good, rocking my lucky shirt... Tonight's the night!"
    z "Yeah, baby!"
    mc "{i}(This guy...){/i}"
    scene 03_413 with Dissolve(1)
    z "So we're meeting them at Heaven?"
    mc "No, Layla said to meet in front of Dylan's and we'll head there together."
    z "Cool-cool."
    scene black with Dissolve(1)
    pause 2
    scene 03_414 with Dissolve(1)
    z "Nice. They're already here."
    z "And damn... They look sexy."
    z "And by they, I mean Layla!"
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 03_415 at moveup
    pause 3
    mc "I think they both look amazing!"
    scene 03_416 with Dissolve(1)
    el "Hey, guys."
    mc "Hi. Have you been waiting long?"
    la "Nope, just got here, what, two minutes ago?"
    el "Yeah, not even that, I think."
    scene 03_417 with Dissolve(1)
    mc "So, what's the plan? Drinks here at Dylan's first, then head to Heaven?"
    la "We were thinking of going straight to Heaven. But if you want a drink first, that's fine too."
    mc "Ah, no-no! I just assumed since we were meeting here..."
    la "Heaven it is then?"
    mc "Yes!"
    scene 03_418 with Dissolve(1)
    la "Yay!"
    la "Let's go then. Come on!"
    mc "Someone's excited."
    la "Yeah. I haven't been to Heaven in a while. Really looking forward to it."
    mc "Same. It's my first time!"
    scene 03_419 with Dissolve(1)
    el "Mind if I take your other arm? I'm not used to walking in these heels."
    mc "You can just grab my arm. You don't need an excuse."
    el "..."
    la "She's wearing my shoes!"
    mc "Oh... My bad. Here you go."
    scene 03_420 with Dissolve(1)
    el "Thank you!"
    mc "*Nods*"
    z "..."
    z "I feel like the fourth wheel."
    scene 03_421 with Dissolve(1)
    el "The saying is third wheel!"
    z "But there are four of us."
    el "..."
    z "Besides. Aren't cars supposed to have four wheels?"
    la "*Sigh* Just come here..."
    scene 03_422 with Dissolve(1)
    z "Haha. Thanks."
    z "This looks so much better already! We should walk like this all the time, Layla. Especially at school!"
    la "Do you want me to let go?"
    z "No-no... I'll shut up."
    scene black with Dissolve(1)
    pause 2
    stop music fadeout 1.0
    scene 03_423 with Dissolve(1)
    play music ("Music/Kyroflux - Drop the Night.mp3", "Music/Kyroflux - Starlight.mp3", "Music/Kyroflux - Circuit Breaker.mp3", "Music/Kyroflux - After Hours.mp3") volume 0.4
    # Copyright NyxVN
    mc "Oh wow... This place is way bigger than I expected."
    z "That's what she said! Haha."
    el "Let's go, Layla!"
    scene 03_424 with Dissolve(1)
    z "This is one of my favourite clubs."
    mc "Seems like any place with girls is your favourite."
    z "Haha, you're right about that. You know me too well."
    la "Oh! Free table over there. Come on, guys. This place fills up fast."
    scene 03_425 with Dissolve(1)
    mc "Hey, what's back there?"
    z "That, my friend, is what they call 'two people making out'..."
    mc "Really?"
    z "Yup. Believe it or not."
    mc "I meant the room with the guard, Sherlock."
    z "Oh. Uh... no idea actually."
    scene 03_426 with Dissolve(1)
    el "That room leads to the backdoor entrance and to the VIP section upstairs."
    z "Okay."
    z "Wait... How do you know? Have you been up there?"
    el "..."
    scene 03_427 with Dissolve(1)
    z "You have, haven't you? When? With who? What's it like?"
    el "*Sigh* Who let you tag along again?"
    z "Come on, Elena. Tell me..."
    z "Was it some rich guy? I bet it was."
    el "Dios mío..."
    scene 03_428 with Dissolve(1)
    z "Elena!"
    mc "Let it go, Zach..."
    z "But aren't you curious?"
    mc "Let's just join the girls. And no more questions about the VIP room!"
    z "*Sigh* Fine, fine..."
    scene 03_429 with Dissolve(1)
    z "Okay, first round's on me. What are you all drinking?"
    la "Glass of wine for me. Red, please."
    el "Same here."
    z "Wine? In a club? Really? Who does that?"
    scene 03_430 with Dissolve(1)
    z "You're going with beer, right?"
    mc "Beer's good."
    z "Alright. Two beers, two wines."
    el "Red."
    z "I know..."
    scene 03_431 with Dissolve(1)
    el "So... Now tell us. Just between us."
    mc "Tell you what?"
    el "How you pulled it off. Cheating, I mean."
    mc "Still on this? Hate to disappoint you, but I didn't cheat."
    el "Uh-huh..."
    scene 03_432 with Dissolve(1)
    el "Do you believe him, Layla?"
    la "Hmm... Let's say innocent until proven guilty?"
    el "For now... We'll get to the bottom of it."
    la "Besides, I still need him to teach me Spanish."
    el "Oh right!"
    scene 03_433 with Dissolve(1)
    el "Me dijo Layla que eres hispano.\n(Layla told me you're Hispanic.)"
    el "Y estás tomando clases de español?\n(And you're taking Spanish classes?)"
    mc "Sí. Créditos fáciles.\n(Yes. Easy credits.)"
    scene 03_434 with Dissolve(1)
    el "No lo llamaría fácil. Ramírez puede ser una verdadera perra.\n(I wouldn't say easy. Ramirez can be a real bitch.)"
    mc "Haha... Okay."
    scene 03_435 with Dissolve(1)
    la "Hey! Can we chill with the Spanish until after my private lessons?"
    mc "Lo siento."
    scene 03_436 with Dissolve(1)
    la "Oh, I know that one. Sorry, right?"
    mc "Nice. You're learning already."
    la "Gracias. Must be the teacher."
    el "Dios Mío!"
    scene 03_437 with Dissolve(1)
    z "Here you go."
    mc "Thanks."
    la "Thank you, Zach."
    z "You're welcome, Layla. Anything for you!"
    el "*Shakes head*"
    scene 03_438 with Dissolve(1)
    el "What do you think you're doing?"
    z "Sitting down..."
    el "Not next to me you're not."
    el "Go sit over there."
    z "..."
    la "Elena!"
    scene 03_439 with Dissolve(1)
    mc "Cheers."
    el "Cheers, guys."
    z "To an awesome night."
    scene 03_440 with Dissolve(1)
    z "So what were you talking about?"
    la "Spanish. [mc] is going to tutor me."
    z "Oh, you take Spanish too, Layla? Why don't we have classes together, then?"
    z "By the way. Gabi's awesome, right? My favourite teacher."
    scene 03_441 with Dissolve(1)
    el "Of course she is..."
    z "How would you know? You don't take Spanish. She's a good teacher."
    el "Uh-huh. Totally your favourite for her teaching skills, right?"
    z "Exactly!"
    scene 03_442 with Dissolve(1)
    z "Did you have Spanish class yet, [mc]? Or do you even take it?"
    mc "I do. Haven't had a class yet though. Skipped yesterday."
    z "She'll be your favourite too. Just wait..."
    el "..."
    scene black with Dissolve(1)
    pause 2
    scene 03_443 with Dissolve(1)
    la "I don't want to sit around all night. Let's go dance, Elena."
    el "*Nods* Mm-hmm."
    scene 03_444 with Dissolve(1)
    la "Come on. What are you guys waiting for?"
    z "Dancing? Nope. Hard pass."
    la "Pfff. Boring..."
    scene 03_445 with Dissolve(1)
    z "Seriously though... how lucky are we?"
    z "Out with two hot chicks."
    menu:
        "Joke":
            mc "Eh, just another Friday night for me."
            z "Haha! You cocky bastard."
        "Agree":
            mc "Yeah. They're really cute."
    scene 03_446 with Dissolve(1)
    z "Look at them!"
    z "Damn..."
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 03_447 at moveup
    pause 3
    mc "Wouldn't you rather be over there... dancing with them?"
    z "Dance and make a fool of myself? No thanks. I dance like a drunk giraffe."
    mc "Same here. But who cares? It's about having fun. Especially with girls like that."
    z "Hmm... You've got a point."
    scene 03_448 with Dissolve(1)
    z "Okay, serious talk now. If we play this right, we could get lucky tonight."
    mc "You're optimistic."
    z "I've got my lucky shirt on, and you, my wingman, is finally back. The stars are aligning!"
    z "So... we need a plan."
    mc "{i}(I can't wait to see where this is going.){/i}"
    scene 03_449 with Dissolve(1)
    z "Step one! Who do you like more? Layla or Elena? You know I'm more into Layla, but I could take Elena for the team."
    mc "Take her for the team? Come on? Seriously?"
    mc "She deserves way better than that."
    z "So... that a yes? She's your type?"
    menu:
        "Not really":
            mc "Not really. But she's fun to hang out with."
            z "I don't know about fun. She's always bitchy towards me. Like nonstop."
        "She's cute[KoGa3AutoWTChange1]{size=-4}(Elena Cute, Elena Points+2) {/size} {/color}":
            $ Elena_Cute = True
            $ Elena_Points += 2
            # Elena (4)
            scene 03_450 with Dissolve(1)
            mc "I think she's cute. Don't know her that well yet, but she's got something. Fun to hang with."
            z "I don't know, man. She's always bitchy towards me. Like nonstop."
            mc "She's blunt and doesn't shy away from speaking her mind. Part of her charm. Kinda refreshing imo."
            z "Sounds like a bitch to me."
            mc "*Shakes head*"
            scene 03_451 with Dissolve(1)
            el "..."
    scene 03_452 with Dissolve(1)
    la "Come on... Enough sitting around."
    la "I can see you want to join us!"
    mc "Is she talking to us?"
    z "No clue. I can barely hear you over this music!"
    scene 03_453 with Dissolve(1)
    la "I'm not taking no for an answer this time!"
    mc "What?"
    la "Dance! With us?"
    scene 03_454 with Dissolve(1)
    la "Please?"
    mc "{i}(How can anyone say no to that?){/i}"
    mc "Sure!"
    scene 03_455 with Dissolve(1)
    la "Yay!"
    la "Come on. Faster!"
    scene 03_456 with Dissolve(1)
    la "Elena! Look who I dragged onto the dancefloor!"
    mc "Hey!"
    el "Hey. About time! What finally convinced you to come dance?"
    menu:
        "Pretty girls":
            mc "Layla's very persuasive and..."
            el "And?"
            scene 03_457 with Dissolve(1)
            mc "...I'd rather be dancing with the two most beautiful girls in the club than watch some random guys try."
            el "The most beautiful, huh?"
            mc "Without question."
            el "You hear that, Layla?"
            la "Uh-huh."
        "Joke":
            mc "Layla's very persuasive and..."
            el "And?"
            scene 03_458 with Dissolve(1)
            mc "...honestly, I couldn't just stand by and let the whole club suffer watching you two dance. Just horrible!"
            el "Horrible, huh?"
            mc "Had to step in and save your dignity. You're welcome, by the way."
            el "You heard that, Layla? Our knight in shining sarcasm."
            la "Then let's show him just how 'terrible' we really are."
    scene 03_459 with Dissolve(1)
    mc "..."
    scene 03_460 with Dissolve(1)
    ""
    scene 03_461 with Dissolve(1)
    mc "Okay, now I get why this place is called Heaven."
    el "Dios mío..."
    la "Haha."
    scene 03_462 with Dissolve(1)
    ""
    scene 03_463 with Dissolve(1)
    z "{i}(Haha. He was right. He can't dance.){/i}"
    z "{i}(Still... they look like they're having a blast. Should've joined after all.){/i}"
    scene 03_464 with Dissolve(1)
    z "*Sigh*"
    z "{i}(Guess I'll go grab us some shots...){/i}"
    scene 03_465 with Dissolve(1)
    ""
    scene 03_466 with Dissolve(1)
    mc "Come on, Elena! Lower!"
    el "Haha, I can't! Not in this outfit..."
    scene 03_467 with Dissolve(1)
    ""
    scene 03_468 with Dissolve(1)
    ""
    scene 03_469 with Dissolve(1)
    ""
    scene 03_470 with Dissolve(1)
    la "Aaah-haha..."
    la "..."
    la "...Hey! Where's Zach?"
    mc "What?"
    scene 03_471 with Dissolve(1)
    la "Where's Zach?"
    la "He's not at our table."
    mc "Hmm..."
    scene 03_472 with Dissolve(1)
    la "Where could he have gone?"
    el "Do we really care?"
    la "No... No, I mean..."
    mc "I see him. He's at the bar. Looks like he bought a drink for..."
    scene 03_473 with Dissolve(1)
    mc "Huh?"
    la "What? Do you know her?"
    mc "Not really... But I think Zach doesn't realise that's actually a guy."
    la "That's a guy? How can you tell?"
    scene 03_474 with Dissolve(1)
    mc "Choker to hide the Adam's apple, heavy makeup, and that jawline's kind of a giveaway."
    la "Hmm... I still don't see it. You sure?"
    el "I think he's right."
    la "Yeah?"
    scene 03_475 with Dissolve(1)
    el "Look how happy he is. I can't wait to see his face when we tell him."
    mc "Haha, Elena. You're so mean."
    mc "Don't tell him, though."
    el "Oh, come on!"
    mc "Not yet, at least."
    scene 03_476 with Dissolve(1)
    el "I'll head back to the table before someone else snags it."
    mc "I can go if you want. You should keep dancing with Layla."
    el "Nah, it's fine. You two go ahead! I need a break anyway."
    la "We'll be back soon. Just a song or two."
    scene 03_477 with Dissolve(1)
    mc "Just the two of us now."
    la "Mm-hmm."
    mc "Having fun?"
    la "Yeah. You?"
    mc "Me too. I like dancing with you."
    scene black with Dissolve(1)
    pause 1
    scene 03_478 with Dissolve(1)
    z "Heeey!"
    el "Hey..."
    z "I brought a few shots!"
    el "A few...? Who's supposed to drink all these?"
    z "We are, of course!"
    scene 03_479 with Dissolve(1)
    el "How's your new friend?"
    z "Who?"
    el "The one you bought a cocktail for at the bar."
    z "Someone sounds jealous."
    el "Why would I be jealous that you bought someone a cocktail?"
    scene 03_480 with Dissolve(1)
    z "Because I can pull a pretty girl while you're sitting here alone."
    el "A gi..."
    el "*Smirks* Yeah, that must be it."
    el "Why didn't you invite her to join us?"
    z "I did. But sadly, she had to leave."
    el "Right..."
    scene 03_481 with Dissolve(1)
    z "Anyway. Cheers!"
    el "Cheers..."
    if Layla_Points <= 13:
        scene 03_482 with Dissolve(1)
        z "Heh. Look at them. They're having fun."
        z "It pains me to say it... But they look good together."
        el "Yeah. Let's see what happens."
    else:
        scene 03_483 with Dissolve(1)
        la "You actually got some moves, huh?"
        mc "Hey! Don't make fun of me. I'm trying."
        la "No... I actually mean it. You aren't as bad as you think."
        mc "Thanks. I'm just following your lead."
        scene 03_484 with Dissolve(1)
        la "..."
        mc "..."
        scene 03_485 with Dissolve(1)
        mc "Did I mention that you look cute tonight?"
        la "You didn't."
        mc "Layla! You look very cute tonight. You always do!"
        la "Thanks..."
        scene 03_486 with Dissolve(1)
        mc "I really like the pantyhose with the short skirt..."
        la "Yeah?"
        mc "Uh-huh. Sexy!"
        scene 03_487 with Dissolve(1)
        la "..."
        scene 03_488 with Dissolve(1)
        la "Aah-haha..."
        scene 03_489 with Dissolve(1)
        z "Heh. Look at them. Seems like they are hitting it off."
        z "It pains me to say it... But they look good together."
        scene 03_490 with Dissolve(1)
        el "Have you been living under a rock? They've been flirting since day one."
        z "What? I must have been living under a rock. I had no idea..."
        el "Blind too!"
        z "What do you think of them?"
        el "*Sigh* As you said. They look very good together."
        if Elena_Cute == True:
            scene 03_491 with Dissolve(1)
            z "You really are the jealous type."
            el "Maybe I am..."
            z "{i}(Wow. She's being honest. Must be the alcohol talking...){/i}"
            z "{i}(Let's test how much she actually likes [mc].){/i}"
            z "I asked [mc] earlier what he thought of you."
            el "Oh? And what did he say?"
            scene 03_492 with Dissolve(1)
            z "He said you're cute. And fun to be around."
            el "..."
        else:
            pass
    scene 03_493 with Dissolve(1)
    z "..."
    scene 03_494 with Dissolve(1)
    z "Hey, Elena... What does Layla think of me?"
    el "Yes..."
    z "Yes? What do you mean? She thinks about me?"
    z "So I still have a chance?"
    el "Yes..."
    scene 03_495 with Dissolve(1)
    z "Haha, I knew it!"
    z "Man... My lucky shirt is extra lucky tonight!"
    z "Fuck, I'm feeling good."
    z "Here! Let's drink to that!"
    scene 03_496 with Dissolve(1)
    z "Cheers!"
    el "Cheers..."
    scene black with Dissolve(1)
    pause 2
    scene 03_497 with Dissolve(1)
    z "Uh... Guys?"
    z "A little help over here, please."
    scene 03_498 with Dissolve(1)
    mc "..."
    la "Elena!"
    la "What happened?"
    scene 03_499 with Dissolve(1)
    la "Elena?"
    el "..."
    la "Hey, Elena?"
    el "Nggh..."
    la "Are you okay?"
    scene 03_500 with Dissolve(1)
    la "What the hell, Zach!"
    z "What are you mad at me for? I didn't do anything..."
    la "How much did she drink?"
    z "I don't know. One maybe two shots..."
    scene 03_501 with Dissolve(1)
    la "It looks like she had more than two! Let's get out of here!"
    la "[mc]? Can you help me get her up?"
    mc "Of course."
    la "Hey, Elena? Time to leave."
    el "Mmmh..."
    scene 03_502 with Dissolve(1)
    mc "Come on, Elena! Let's go."
    mc "Time to head home!"
    scene 03_503 with Dissolve(1)
    mc "Hey, Zach! Can you take over for a sec?"
    mc "I'm gonna get some water for Elena."
    z "Uhm... Sure."
    mc "Thanks."
    mc "Just head to the train station, I'll catch up. Be right back."
    scene 03_504 with Dissolve(1)
    mc "Hey, excuse me."
    bt "Hi. What can I get you?"
    mc "Could I have a water, please?"
    bt "Of course. Gimme a sec."
    mc "Bottled if possible."
    bt "No problem."
    scene 03_505 with Dissolve(1)
    mc "*Humming*"
    x "..."
    scene 03_506 with Dissolve(1)
    x "{i}(He looks like...){/i}"
    x "Hmm?"
    x "{i}(Wait... Is he?){/i}"
    scene 03_507 with Dissolve(1)
    x "[mc] Moreno?"
    mc "Yes?"
    x "Oh my god! It is you!"
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 03_508 at moveup
    pause 3
    mc "Uh..."
    mc "{i}(It's... Erynn... Right?){/i}"
    mc "{i}(Uhm... Shit. What? Damn...){/i}"
    mc "{i}(I'm not prepared for this at all... I didn't expect to meet her like this.){/i}"
    mc "Erynn...?"
    scene 03_509 with Dissolve(1)
    er "Yes!"
    mc "Uh..."
    er "I can't believe this. Oh my god! Hi!"
    mc "{i}(Uh... What do I even say? Shit. I'm panicking...){/i}"
    scene 03_510 with Dissolve(1)
    er "Look at you!"
    er "This is... Wow..."
    er "What are you doing here? Are you..."
    bt "Here's your water."
    scene 03_511 with Dissolve(1)
    mc "Thank you very much."
    mc "{i}(I still don't know what to say.){/i}"
    mc "{i}(This... I should...){/i}"
    scene 03_512 with Dissolve(1)
    mc "I'm sorry, Erynn. I can't do... Can't talk right now."
    mc "My friends are waiting for me."
    er "Wait? What? [mc]?"
    scene 03_513 with Dissolve(1)
    mc "{i}(Of all people it had to be her...){/i}"
    mc "{i}(It had to be Erynn?){/i}"
    scene 03_514 with Dissolve(1)
    er "No! No... Not again..."
    stop music fadeout 1.0
    scene 03_515 with Dissolve(1)
    play music "Sounds/Street_Traffic.mp3" volume 0.6
    mc "Oh, you're still here?"
    z "You try walking with this piece of work..."
    mc "Alright, I've got it. I'll take over."
    scene 03_516 with Dissolve(1)
    el "Where are we going?"
    la "Home!"
    el "What? I thought we were going to Heaven?"
    z "Haha... How fucking drunk are you?"
    scene 03_517 with Dissolve(1)
    er "[mc]!"
    er "Please... wait."
    mc "..."
    scene 03_518 with Dissolve(1)
    mc "{i}(Erynn, why?){/i}"
    mc "{i}(I guess there's no avoiding this.){/i}"
    mc "Sorry, guys. She's... an old friend. Give me a second."
    la "Be quick. Our train leaves in five minutes."
    mc "Got it."
    scene 03_519 with Dissolve(1)
    er "*Catching her breath*"
    er "Thanks for stopping."
    mc "Sure. What's up?"
    er "..."
    scene 03_520 with Dissolve(1)
    er "What's up? That's it?"
    er "We haven't seen each other in I don't know how long anymore and that's what I get? What's up?"
    er "No how are you? Let alone maybe a hug?"
    mc "Uh... I panicked, okay...? I didn't know what to say. I didn't expect to see you here. It caught me completely off guard."
    er "You think this isn't sudden for me too?"
    scene 03_521 with Dissolve(1)
    mc "You're right. Sorry... How are you, Erynn?"
    er "Right now? Confused. How long have you been back? Are you just visiting, or back for good?"
    mc "For about a week. Well, last Sunday. And yeah, I moved back."
    scene 03_522 with Dissolve(1)
    er "A week? And it didn't cross your mind to contact me? I have to find out by chance?"
    mc "About that..."
    er "Does Mom know?"
    mc "Yes."
    er "Yes?"
    scene 03_523 with Dissolve(1)
    er "..."
    er "The pool boy... *Sigh* I should've known."
    mc "The what?"
    er "Forget it."
    scene 03_524 with Dissolve(1)
    la "Hey, Erynn."
    er "Oh... Hey, Layla."
    er "You were at Heaven too?"
    la "Mm-hmm."
    scene 03_525 with Dissolve(1)
    mc "You two know each other?"
    la "Yes. Small town."
    mc "Small town... Right..."
    la "Are you coming? Train leaves soon. We need to hurry."
    menu:
        "Go with Layla[KoGa3AutoWTChange1]{size=-4}(Layla Points+2) {/size} {/color}":
            $ Layla_Points += 2
            # Layla (18)
            jump Week1_Friday_Train
        "Stay with Erynn[KoGa3AutoWTChange1]{size=-4}(Erynn Week1 Stay, Erynn Points+2) {/size} {/color}":
            $ Erynn_Week1_Stay = True
            $ Erynn_Points += 2
            # Erynn (2)
            jump Week1_Friday_Erynn

label Week1_Friday_Train:
    scene 03_526 with Dissolve(1)
    mc "Yes, I'm coming."
    mc "Sorry, Erynn... I..."
    scene 03_527 with Dissolve(1)
    er "[mc]? But..."
    mc "Elena's drunk and we need to get her home. We'll talk soon, I promise."
    er "I understand."
    scene 03_528 with Dissolve(1)
    er "...Bye."
    mc "Bye, Erynn."
    scene 03_529 with Dissolve(1)
    la "She looked really sad."
    mc "Yeah. We haven't seen each other in years. Total surprise running into her tonight. I'll call her tomorrow and apologise properly."
    la "You definitely should."
    scene 03_530 with Dissolve(1)
    la "How do you know Erynn?"
    mc "She used to be my neighbour, way back."
    la "Oh wow! So you must know Melissa too?"
    scene 03_531 with Dissolve(1)
    mc "Her mom? Yeah, of course."
    la "She's my hairstylist."
    mc "No way. You were right about your 'small town' comment."
    la "Haha. Yeah."
    scene 03_532 with Dissolve(1)
    mc "She cuts my hair too."
    la "Really? Haha."
    la "Well, come on. Let's catch up with Zach and Elena."
    mc "Uh-huh."
    scene 03_533 with Dissolve(1)
    mc "I see you found an easier way."
    z "I did. Except for the 'she's almost choking me' part."
    mc "Haha. Want me to take over again?"
    z "Uh... No, it's fine. We're almost there anyway."
    scene 03_534 with Dissolve(1)
    mc "Hey! What's wrong? Why the pouty face all of a sudden?"
    la "No reason..."
    mc "Layla!"
    scene 03_535 with Dissolve(1)
    la "It's not fair, alright."
    mc "What's not fair?"
    la "I wear heels too and my feet hurt."
    mc "Are you seriously jealous of a drunk girl?"
    scene 03_536 with Dissolve(1)
    la "You don't get it."
    mc "*Sigh* Okay..."
    la "I wish I were drunk..."
    z "Haha. Guess it's your turn."
    menu:
        "Go to the train station":
            la "Come on! Let's hurry or we'll miss the train!"
        "Piggyback ride[KoGa3AutoWTChange1]{size=-4}(Layla Week1 Piggyback, Layla Points+2) {/size} {/color}":
            $ Layla_Week1_Piggyback = True
            $ Layla_Points += 2
            # Layla (20)
            scene 03_537 with Dissolve(1)
            mc "Hop on."
            la "Really?"
            mc "Yes!"
            la "Yay!"
            scene 03_538 with Dissolve(1)
            mc "Ready?"
            la "Mm-hmm...!"
            scene 03_539 with Dissolve(1)
            la "This is awesome!"
            la "Can we walk like this all the time?"
            z "Haha."
            scene 03_540 with Dissolve(1)
            mc "Does this count as the favour I owe you?"
            la "Nope!"
            mc "Didn't think so."
            la "But. Thanks, [mc]!"
            mc "Anytime."
            scene 03_541 with Dissolve(1)
            la "You're the best."
            scene 03_542 with Dissolve(1)
            la "To the train station!"
            la "Zach... Let's race!"
            mc "Uhm? How about no!"
            z "Haha..."
            scene 03_543 with Dissolve(1)
            z "I'll race with you Layla, if we switch!"
            la "No way. I'm comfy right here."
            la "*Whispers* On these broad, manly shoulders..."
            mc "*Shaking head* Are you sure you're not the drunk one?"
            la "Kyahaha."
            mc "Haha. What kind of laugh is that..."
    scene black with Dissolve(1)
    pause 2
    stop music fadeout 1.0
    scene 03_544 with Dissolve(1)
    play music ("Music/LoFi Upbeat 1.mp3", "Music/LoFi Upbeat 2.mp3", "Music/LoFi Upbeat 3.mp3", "Music/LoFi Upbeat 4.mp3") volume 0.2
    la "Made it just in time."
    mc "Yeah! Literally two seconds later and we would've missed it!"
    scene 03_545 with Dissolve(1)
    la "El... How are you feeling?"
    el "Little dizzy, but I'm fine."
    z "Of course she's fine. She isn't the one with the sore back."
    scene 03_546 with Dissolve(1)
    el "I'm not heavy at all..."
    z "I carried you. So I'll be the judge of that."
    el "You should be happy I let you carry me."
    el "Don't think for a second I didn't feel your hands on my ass..."
    z "You wish!"
    if Layla_Points >= 17:
        $ Elena_Week1_TrainKissLayla = True
        scene 03_547 with Dissolve(1)
        el "Hey, Layla?"
        la "Hmm?"
        el "I'm not heavy, right?"
        la "Of course not. You're perfect just the way you are!"
        scene 03_548 with Dissolve(1)
        el "Has anyone told you that you look really cute today, Layla?"
        la "Haha. Actually yes. [mc] told me earlier."
        el "Good. He's right."
        la "Thank you, Elena. You look very cute yourself."
        scene 03_549 with Dissolve(1)
        el "That's because I'm wearing your clothes."
        la "No. You always look cute."
        el "..."
        scene 03_550 with Dissolve(1)
        mc "..."
        z "Okay? What's going on here?"
        scene 03_551 with Dissolve(1)
        la "{i}(Uhm... What?){/i}"
        mc "{i}(Elena?){/i}"
        la "{i}(What do I even do right now?){/i}"
        scene 03_552 with Dissolve(1)
        la "Uh... Elena?"
        la "We..."
        el "Hmm?"
        z "Haha. Layla's face. This is too funny!"
        if Elena_Points == 4:
            $ Elena_Week1_TrainKiss = True
            scene 03_553 with Dissolve(1)
            el "What are you looking at?"
            z "I'm not looking!"
            el "Not talking to you!"
            el "You!"
            scene 03_554 with Dissolve(1)
            mc "Me? Uh... Well... Nothing..."
            el "..."
            mc "You're the one staring!"
            scene 03_555 with Dissolve(1)
            el "Are you jealous I kissed your Layla?"
            mc "{i}(My Layla?){/i}"
            mc "What?"
            scene 03_556 with Dissolve(1)
            el "..."
            mc "..."
            mc "{i}(She looks so drunk.){/i}"
            scene 03_557 with Dissolve(1)
            la "Elena... Be careful... Just sit back down."
            mc "Yeah, listen to Layla. Sit down before you fall over."
            scene 03_558 with Dissolve(1)
            el "I'm sitting down..."
            mc "Heh. True... Not what I meant though."
            el "You should've been more specific."
            mc "I can see that."
            scene 03_559 with Dissolve(1)
            el "You know what I see?"
            mc "Hmm?"
            el "Seeing you this up close. You're very handsome."
            mc "Thanks. You're very pretty yourself."
            scene 03_560 with Dissolve(1)
            mc "..."
            scene 03_561 with Dissolve(1)
            mc "{i}(I know I shouldn't but...){/i}"
            mc "{i}(Even though she's drunk. She surely knows how to kiss.){/i}"
            scene 03_562 with Dissolve(1)
            el "..."
            scene 03_563 with Dissolve(1)
            el "Cheeky!"
            mc "Sorry. It's a habit of mine."
            el "You're a good kisser though."
            mc "So are you!"
            el "Let me try again."
            scene 03_564 with Dissolve(1)
            la "Elena! That's enough!"
            scene 03_565 with Dissolve(1)
            la "How drunk are you?"
            el "I'm not."
            la "Uh-huh..."
            la "Now sit here. And stay here. On your seat!"
        else:
            pass
    else:
        el "Who are you again?"
        el "I'm tired..."
        la "Go to sleep, I'll wake you when we arrive at our stop."
    scene black with Dissolve(1)
    pause 2
    scene 03_566 with Dissolve(1)
    la "Well, this is my stop."
    z "One more for us."
    mc "Will you be okay getting her home? I can come along."
    la "Don't worry. She's staying at my place tonight. I called my sister earlier. She's picking us up at the station."
    mc "{i}(Didn't know she had a sister...){/i}"
    scene 03_567 with Dissolve(1)
    la "Let's go, Elena."
    la "I'll call you tomorrow, okay?"
    mc "Yeah. Bye, Layla, Elena."
    la "Bye-bye."
    scene 03_568 with Dissolve(1)
    z "That was a fun day, huh?"
    mc "Mm-hmm."
    z "Too bad Elena got that drunk. Who knows what might've happened otherwise."
    mc "{i}(Nothing...){/i}"
    scene 03_569 with Dissolve(1)
    z "I had such a hard-on while piggybacking Elena."
    z "I'm not even into her, but she was pressing her boobs into my back..."
    z "And yeah... I kinda grabbed her ass. Couldn't help it. No clue how she noticed, considering how out of it she was."
    mc "*Shakes head*"
    if Elena_Week1_TrainKissLayla == True:
        z "And who would've thought that Elena turns into a full-on lesbian when she's drunk. Haha."
    else:
        pass
    jump Week1_Saturday_Morning

label Week1_Friday_Erynn:
    scene 03_570 with Dissolve(1)
    mc "Uhm... Layla? Would it be okay if I stayed here with Erynn? We haven't seen each other in a long time, and..."
    la "No, it's fine."
    mc "Are you sure you'll be alright? I can come with you to the train station if needed."
    la "Don't worry about it. I called my sister earlier. She's picking us up. You two catch up."
    mc "{i}(Didn't know she had a sister.){/i}"
    scene 03_571 with Dissolve(1)
    mc "Thank you. I'll call you tomorrow, alright?"
    la "Mm-hmm."
    mc "Bye, Layla."
    la "Bye-bye."
    scene 03_572 with Dissolve(1)
    la "..."
    scene 03_573 with Dissolve(1)
    er "Thank you for staying. But you didn't have to ditch your friends for me."
    er "Will they be okay?"
    mc "Yes. Zach's with them. He's a good guy."
    scene 03_574 with Dissolve(1)
    er "Oh? That was Zachary? Your little buddy from back in the day?"
    mc "Indeed."
    er "Wow. He got tall. Who would've guessed? Good for him."
    mc "Heh, yeah..."
    scene 03_575 with Dissolve(1)
    er "Uhm... [mc]...?"
    mc "Hmm?"
    er "..."
    mc "What is it?"
    er "Layla. Is she your... your girlfriend?"
    menu:
        "Just friends":
            scene 03_576 with Dissolve(1)
            mc "We're friends from school. We have a few classes together."
            er "Just friends?"
            mc "Yeah."
        "We flirt":
            scene 03_576 with Dissolve(1)
            mc "We're friends from school. We have a few classes together."
            er "Just friends?"
            mc "We flirt a little... Maybe more than just friends, I'm not sure yet. I've only known her for about a week."
            er "Hmm..."
    if Layla_Points >= 13:
        scene 03_577 with Dissolve(1)
        er "It looked like it..."
        mc "If she were my girlfriend, I wouldn't have just kissed her on the cheek!"
        er "..."
        mc "{i}(Is she... jealous? This might be the first time I've seen her like this.){/i}"
    else:
        pass
    scene black with Dissolve(1)
    pause 2
    stop music fadeout 1.0
    scene 03_578 with Dissolve(1)
    play music ("Music/Kyroflux - Circuit Breaker.mp3", "Music/Kyroflux - After Hours.mp3", "Music/Kyroflux - Drop the Night.mp3", "Music/Kyroflux - Starlight.mp3") volume 0.4
    # Copyright NyxVN
    er "Want to order something? A beer, cocktail maybe?"
    er "You're old enough to drink now, right?"
    mc "I'm old enough..."
    mc "But I've had plenty for today. Besides, I can't stay too long. I think the last train leaves in about half an hour."
    er "Oh, don't worry about that. You can stay at my place tonight. I have an apartment here in the city."
    scene 03_579 with Dissolve(1)
    mc "You're inviting a stranger to your place the first night you meet him?"
    er "You're not a stranger!"
    mc "We haven't seen each other in years. We're practically strangers. Or... estranged?"
    er "..."
    er "We're just going there to talk! I have a ton of questions."
    scene 03_580 with Dissolve(1)
    mc "Okay... Let me text Mom to let her know. She was already mad at me a few days ago for not saying where I was."
    er "You deserved that! You've barely been back a week and you're already staying out all night without checking in? Of course she'll be worried!"
    er "Just talk to her. She's amazing. Do you have any idea how much she missed you all this time?"
    mc "Trust me... I know."
    scene 03_581 with Dissolve(1)
    mc "You look nice, by the way."
    er "Thank you. Still the little charmer, aren't you?"
    mc "Well... Some things never change."
    er "I hope they didn't..."
    scene 03_582 with Dissolve(1)
    mc "So... How long have you been here? I mean, at the club."
    er "A couple of hours."
    mc "That long? Hmm... I didn't see you until I went to grab a water at the bar."
    er "I was upstairs, in the VIP lounge."
    mc "Oh, nice. Was there a special occasion? Private party or something?"
    scene 03_583 with Dissolve(1)
    er "..."
    er "Something like that..."
    mc "Hmm?"
    scene 03_584 with Dissolve(1)
    er "You know what? Let me grab my stuff. Let's get out of here."
    er "I don't want to be here any longer."
    mc "Uhm... Sure..."
    mc "{i}(What's with the sudden mood change?){/i}"
    scene black with Dissolve(2)
    pause 2
    n "Saturday, 00:51. Erynn's apartment."
    stop music fadeout 1.0
    scene 03_585 with Dissolve(1)
    play music ("Music/LoFi Upbeat 1.mp3", "Music/LoFi Upbeat 2.mp3", "Music/LoFi Upbeat 3.mp3", "Music/LoFi Upbeat 4.mp3") volume 0.2
    mc "{i}(Erynn's apartment...){/i}"
    mc "{i}(Never would've guessed I'd end up here tonight...){/i}"
    scene 03_586 with Dissolve(1)
    er "Well... This is it. Nothing much but... what do you think?"
    mc "Nothing much? Are you kidding me? It looks great."
    mc "It has all you need, right? Kitchen, bathroom, bed, even a TV..."
    mc "And it's right in the middle of the city, so..."
    er "Yeah."
    scene 03_587 with Dissolve(1)
    mc "How far is it from the beach?"
    er "Five-minute walk."
    mc "Wow... five minutes to the beach."
    mc "Any chance there's another room you could rent out to me?"
    scene 03_588 with Dissolve(1)
    er "Sadly, no. But my bed is big enough for two."
    mc "Oooh..."
    er "Kidding!"
    scene 03_589 with Dissolve(1)
    mc "Don't tease me like that!"
    er "Haha. Sorry... Not really..."
    mc "Heh..."
    scene 03_590 with Dissolve(1)
    mc "Can you see the beach from here?"
    er "No. It's on the other side."
    er "I could've gotten a beach-view apartment, but rent would've been twice as much."
    er "If I want to see the beach, I just go there."
    mc "It's just a five-minute walk..."
    er "Haha, right!"
    scene 03_591 with Dissolve(1)
    er "Mind if I take a quick shower?"
    er "Need to get out of these clothes and wash off the alcohol and cigarette smell."
    mc "No, go ahead."
    mc "You smoke, by the way?"
    er "I don't. But a lot of people in the VIP lounge did. I can't stand the smell..."
    scene 03_592 with Dissolve(1)
    er "Want me to get you something else to wear as well?"
    mc "Why? Do I smell bad?"
    er "No."
    mc "Then, I'm good. Thanks."
    scene 03_593 with Dissolve(1)
    er "What? Are my skirts not good enough for you anymore?"
    mc "Funny..."
    er "Wouldn't be the first time you wore them... Or the second..."
    mc "*Sigh* You still remember that?"
    er "That... and a whole lot more."
    scene 03_594 with Dissolve(1)
    mc "..."
    scene 03_595 with Dissolve(1)
    mc "{i}(Uhm...){/i}"
    mc "{i}(Did she forget I'm here?){/i}"
    scene 03_596 with Dissolve(1)
    er "..."
    scene 03_597 with Dissolve(1)
    mc "Have you ever thought about hanging more pictures or paintings?"
    mc "You've got a lot of empty wall space."
    er "..."
    er "I used to have some pictures of myself up. Took them down."
    er "Thought it might look a little... tacky. Especially when others see them."
    scene 03_598 with Dissolve(1)
    mc "It's your apartment."
    mc "Do whatever makes you happy."
    mc "Who cares what anyone else thinks?"
    scene 03_599 with Dissolve(1)
    er "Alright... I'm going to shower now. After that, we'll talk, okay?"
    er "Make yourself at home. And if you're hungry, help yourself. Fridge has all kinds of stuff."
    mc "Will do. Thanks."
    scene 03_600 with Dissolve(1)
    mc "Haha... What?"
    er "Nothing... Just looking..."
    mc "Uh-huh!"
    jump Week1_Friday_Erynn_Apartment

label Week1_Friday_Erynn_Apartment:
    if _in_replay:
        $ Erynn_Points = 2
    scene black with Dissolve(2)
    pause 2
    scene 03_601 with Dissolve(1)
    mc "..."
    mc "{i}(She still has this?){/i}"
    mc "{i}(How long ago was this taken?){/i}"
    scene 03_602 with Dissolve(1)
    mc "Can't believe you still have this picture of us."
    er "Which one?"
    mc "The one where you're giving me a piggyback ride."
    er "Why wouldn't I? It's cute, right?"
    mc "Yeah... it is."
    scene 03_603 with Dissolve(1)
    er "I've got a bunch more of us in the drawer, if you wanna look."
    mc "Which drawer?"
    er "..."
    er "...I can't really..."
    scene 03_604 with Dissolve(1)
    er "Uhm..."
    er "Right there. The small one!"
    mc "Are you naked?"
    scene 03_605 with Dissolve(1)
    er "Yes, I'm naked. I'm taking a shower. Do you shower with clothes on?"
    mc "Haha. No, I don't. I was just surprised, for some reason."
    er "Be right back."
    mc "Take your time!"
    scene 03_606 with Dissolve(1)
    mc "{i}(Damn... Totally lost my train of thought...){/i}"
    mc "{i}(Still can't believe I'm in Erynn's apartment.){/i}"
    mc "{i}(And she's naked right now...){/i}"
    mc "{i}(Man...){/i}"
    mc "{i}(If I knew this would happen, I wouldn't have avoided her this whole week.){/i}"
    scene 03_607 with Dissolve(1)
    mc "{i}(Wait... she left the door open...){/i}"
    mc "{i}(Did she do that on purpose?){/i}"
    mc "{i}(Does she...?){/i}"
    scene 03_608 with Dissolve(1)
    mc "{i}(What am I doing?){/i}"
    mc "{i}(She probably left the door open to hear if I ask something.){/i}"
    menu:
        "Peek":
            mc "{i}(Just one quick peek...){/i}"
            scene 03_609 with Dissolve(1)
            ""
            scene 03_610 with Dissolve(1)
            mc "..."
            scene black with Dissolve(1)
            transform moveup:
                xalign 0.5 yalign 1.0
                linear 5.0 yalign 0.0
            show 03_611 at moveup
            pause 3
            mc "{i}(Wow... I've known her for so long and this is the first time I've seen her naked...){/i}"
            mc "{i}(I know this is wrong but... Damn... She's so gorgeous.){/i}"
            mc "{i}(She's always been pretty, but she became even more beautiful.){/i}"
            scene 03_612 with Dissolve(1)
            mc "{i}(Her boobs...){/i}"
            scene 03_613 with Dissolve(1)
            mc "{i}(Her... Pussy...){/i}"
            scene 03_614 with Dissolve(1)
            mc "{i}(She's perfect.){/i}"
            mc "{i}(And I'm so hard right now...){/i}"
            scene 03_615 with Dissolve(1)
            mc "{i}(What would've happened between us if I hadn't left?){/i}"
            mc "..."
            mc "{i}(Maybe... I can find out now?){/i}"
            mc "{i}(And maybe that's why she left the bathroom door open?){/i}"
            mc "{i}(She was flirting with me earlier...){/i}"
            menu:
                "Go back":
                    scene 03_616 with Dissolve(1)
                    mc "{i}(But I shouldn't...){/i}"
                    mc "{i}(Flirting doesn't mean 'Hey, join me in the shower'.){/i}"
                    mc "{i}(And I don't want to risk our friendship or whatever we are at this point for my curiosity.){/i}"
                    mc "{i}(I've pushed my luck far enough as it is.){/i}"
                    $ renpy.end_replay()
                    jump Week1_Friday_Erynn_Apartment2
                "Join her[KoGa3AutoWTChange1]{size=-4}(Erynn Week1 ShowerJoin, Erynn Points-4) {/size} {/color}":
                    $ Erynn_Week1_ShowerJoin = True
                    $ Erynn_Points -= 4
                    scene 03_617 with Dissolve(1)
                    mc "{i}(Getting nervous...){/i}"
                    mc "{i}(Come on, [mc]! You got this!){/i}"
                    mc "{i}(There's no turning back now.){/i}"
                    scene 03_618 with Dissolve(1)
                    mc "Hey..."
                    er "[mc]!"
                    scene 03_619 with Dissolve(1)
                    er "Why are you in here? Naked!"
                    mc "I wanted to shower with you."
                    er "What? No!"
                    er "Get out! NOW!"
                    mc "Uh... Sorry..."
                    scene 03_620 with Dissolve(1)
                    er "Oh my god, oh my god, oh my god..."
                    er "Nooo..."
                    scene 03_621 with Dissolve(1)
                    mc "{i}(I fucked this up royally.){/i}"
                    mc "{i}(Why did I even do this? I misread the situation completely...){/i}"
                    mc "{i}(I'm so embarrassed right now.){/i}"
                    mc "{i}(*Sigh* I should just leave at this point before I embarrass myself even more.){/i}"
                    scene black with Dissolve(1)
                    pause 2
                    scene 03_622 with Dissolve(1)
                    er "[mc]?"
                    er "..."
                    er "[mc], are you there?"
                    scene 03_623 with Dissolve(1)
                    er "[mc]?"
                    er "..."
                    scene 03_624 with Dissolve(1)
                    er "{i}(Did he leave...? Did I react too harshly on him?){/i}"
                    er "{i}(I invited him here. He probably thought that...){/i}"
                    er "*Sigh...*"
                    $ renpy.end_replay()
                    jump Week1_Saturday_Morning
        "Go back[KoGa3AutoWTChange1]{size=-4}(Erynn Points+2) {/size} {/color}":
            $ Erynn_Points += 2
            # Erynn (4)
            mc "{i}(Let's check the fridge instead.){/i}"
            $ renpy.end_replay()
            jump Week1_Friday_Erynn_Apartment2

label Week1_Friday_Erynn_Apartment2:
    scene black with Dissolve(1)
    pause 2
    scene 03_625 with Dissolve(1)
    mc "{i}(Damn... I'm getting tired.){/i}"
    mc "{i}(How long has she been in there now?){/i}"
    mc "{i}(So much for a quick shower...){/i}"
    scene black with Dissolve(1)
    pause 2
    scene 03_626 with Dissolve(1)
    er "[mc]..."
    er "Sorry I took so long..."
    er "[mc]?"
    er "{i}(Did he leave?){/i}"
    scene 03_627 with Dissolve(1)
    er "[mc]...?"
    er "Oh..."
    scene 03_628 with Dissolve(1)
    er "*Whispers* Are you sleeping?"
    er "*Whispers* [mc]?"
    scene 03_629 with Dissolve(1)
    er "*Whispers* So much for talking, huh?"
    er "*Sigh*"
    er "*Whispers* I had so many questions."
    scene 03_630 with Dissolve(1)
    er "..."
    scene 03_631 with Dissolve(1)
    er "*Whispers* You grew up so handsome. I couldn't believe it when I saw you again."
    er "*Whispers* Do you have any idea how much I missed you?"
    er "*Whispers* Did you miss me?"
    er "..."
    scene 03_632 with Dissolve(1)
    er "*Whispers* Why did you leave, [mc]? Why didn't you ever contact me?"
    er "*Whispers* Did you get my letters?"
    er "*Sigh...*"
    er "*Whispers* I made so many mistakes..."
    er "*Whispers* I needed you here. Who else was going to watch out for me?"
    scene 03_633 with Dissolve(1)
    er "..."
    scene 03_634 with Dissolve(1)
    ""
    scene 03_635 with Dissolve(1)
    er "*Whispers* Please don't ever leave me again... Okay?"
    er "*Whispers* Besides... I still owe you an answer. Do you remember?"
    scene black with Dissolve(2)
    pause 2
    scene 03_636 with Dissolve(1)
    mc "..."
    scene 03_637 with Dissolve(1)
    mc "{i}(Right... I stayed at Erynn's last night.){/i}"
    mc "{i}(Looks like she was in tears.){/i}"
    mc "{i}(Did I make her cry? Can't remember saying something that would make her cry.){/i}"
    mc "{i}(Still looks beautiful even with smudged mascara all over her face.){/i}"
    scene 03_638 with Dissolve(1)
    mc "{i}(What time is it anyway? Feels like it's still very early.){/i}"
    mc "{i}(Guess I'll just head home and let her sleep some more.){/i}"
    mc "{i}(I'll probably do the same...){/i}"
    scene 03_639 with Dissolve(1)
    mc "{i}(I'll try calling you later.){/i}"
    mc "{i}(Bye, Erynn...){/i}"
    jump Week1_Saturday_Morning

label Week1_Saturday_Morning:
    scene black with Dissolve(2)
    n "Saturday, 09:58."
    pause 2
    stop music fadeout 1.0
    scene 03_640 with Dissolve(1)
    play music ("Music/LoFi Indie 3.mp3", "Music/LoFi Indie 1.mp3", "Music/LoFi Indie 2.mp3") volume 0.2
    er "Good morning, Emily."
    m "Oh, good morning, sweetheart. How are you? It's been a while."
    scene 03_641 with Dissolve(1)
    er "See? That wasn't that hard, right?"
    m "Excuse me?"
    er "Sorry! I just meant... Yesterday I... Never mind."
    scene 03_642 with Dissolve(1)
    er "I'm fine, thank you. And you? Enjoying the morning sun?"
    m "Yes, it's lovely out. At least before it gets too hot later. Are you looking for [mc]?"
    er "Yes, actually. Is he home?"
    m "He might still be sleeping. He was out pretty late last night."
    er "Uh-huh."
    scene 03_643 with Dissolve(1)
    m "You can go up and wake him if you'd like. He's supposed to help your mom with the yard today, anyway."
    er "It'll be my pleasure."
    m "Oh no... I know that smirk. What did he do this time?"
    er "If you hear some screaming, just ignore it."
    m "Haha."
    scene black with Dissolve(1)
    pause 2
    scene 03_644 with Dissolve(1)
    er "Good morning, sunshine."
    mc "Nggh..."
    mc "It's the weekend, Mom. Let me sleep a little longer."
    scene 03_645 with Dissolve(1)
    er "..."
    er "{i}(Mom?){/i}"
    er "Hmm..."
    scene 03_646 with Dissolve(1)
    er "Hey, honey."
    mc "Not now. I have a headache."
    mc "{i}(Why can't she just leave me alone?){/i}"
    scene 03_647 with Dissolve(1)
    er "{i}(Sorry...){/i}"
    er "{i}(But this is too much fun.){/i}"
    scene 03_648 with Dissolve(1)
    er "*Whispers* Hey..."
    er "*Whispers* Wake up...!"
    scene 03_649 with Dissolve(1)
    mc "Mom! Can you stop alrea..."
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 03_650 at moveup
    pause 3
    mc "...dy."
    mc "{i}(Shit!){/i}"
    mc "Erynn..."
    er "Hi."
    mc "Uhm... Hi... What are you doing here?"
    scene 03_651 with Dissolve(1)
    if Erynn_Week1_Stay == False:
        er "First of all... What's with the yelling? Do you talk to your mother like that?"
        mc "No... I..."
        er "Second... I came because we didn't get to talk yesterday!"
    else:
        if Erynn_Week1_ShowerJoin == True:
            er "First of all... What's with the yelling? Do you talk to your mother like that?"
            mc "No. I..."
            er "Second... why did you just leave yesterday? You walked into the shower... naked..."
            er "Did you think inviting you over was some kind of cheap hookup?"
            mc "What... No! I just..."
        else:
            er "First of all... What's with the yelling? Do you talk to your mother like that?"
            mc "No. I..."
            er "Second... you stayed over and just left without saying anything? Do you know how worried I was when I woke up?"
            mc "I didn't want..."
    scene 03_652 with Dissolve(1)
    er "Third..."
    mc "Okay. I get it, I get it... I messed up."
    mc "{i}(But...){/i}"
    scene black with Dissolve(1)
    pause 2
    scene 03_653 with Dissolve(1)
    mc "{i}(Why is this coming up again? I thought I was over it... It's been years...){/i}"
    scene 03_654 with Dissolve(1)
    mc "{i}(Can't I just forget about it and move on?){/i}"
    scene black with Dissolve(1)
    pause 2
    scene 03_655 with Dissolve(1)
    mc "..."
    mc "{i}(Maybe I should talk about it with her. But how do I even start?){/i}"
    mc "{i}(She might not even remember that.){/i}"
    mc "{i}(I'm getting nervous. Do I still have feelings for her?){/i}"
    mc "{i}(I shouldn't. So much time has passed. She's probably not the same person.){/i}"
    scene 03_656 with Dissolve(1)
    mc "{i}(We're basically strangers again.){/i}"
    mc "{i}(Right... Why am I stuck in the past? We were kids. Time to move on.){/i}"
    mc "{i}(Besides, I missed having her as a friend. Maybe I can start there.){/i}"
    scene 03_657 with Dissolve(1)
    mc "Uhm. Erynn? You know what? How about we start over? Let's pretend yesterday didn't happen!"
    er "*Sigh*"
    mc "Please?"
    er "*Nodding* Yeah okay. Go ahead. Start over."
    scene 03_658 with Dissolve(1)
    mc "Hi. How are you?"
    mc "..."
    mc "I missed you."
    mc "..."
    mc "I'm sorry for everything."
    scene 03_659 with Dissolve(1)
    mc "{i}(Hmm... Still nothing?){/i}"
    mc "{i}(No, I know her...){/i}"
    mc "I bet you're smiling!"
    er "I'm not smiling!"
    mc "Then turn around!"
    scene 03_660 with Dissolve(1)
    er "..."
    mc "{i}(I knew it. She's trying so hard...){/i}"
    mc "You look very cute when you're trying so hard not to smile."
    er "{i}(Damn it. I can't keep my composure. Why can't I stay mad at this boy?){/i}"
    scene 03_661 with Dissolve(1)
    er "*Sigh*"
    er "Alright... Come here. I missed you too."
    mc "Haha. You can smile now, you know?"
    scene 03_662 with Dissolve(1)
    er "Aaah-haha... [mc]."
    mc "Works every time!"
    scene 03_663 with Dissolve(1)
    er "{i}(I like his arms around me...){/i}"
    er "{i}(This boy really grew up, huh?){/i}"
    er "Sorry if this is awkward, but just a little longer. I need to make up for all the years without hugs from you."
    mc "I don't mind at all. You smell really nice."
    scene 03_664 with Dissolve(1)
    mc "{i}(She really does smell good!){/i}"
    er "Did you just smell me?"
    mc "What? No! I... I just took a deep breath."
    er "..."
    mc "*Deep breath* See!"
    scene 03_665 with Dissolve(1)
    er "Hahaha... you doofus."
    er "Way to ruin my moment."
    mc "Hey. I'm not going anywhere this time. So anytime you need a hug... I'll be here."
    er "Don't make promises you can't keep."
    scene 03_666 with Dissolve(1)
    er "Hey, I have a good idea."
    mc "Yeah? What's that?"
    er "Come. Let's sit on the bed."
    mc "Wow... I don't know where you get these brilliant ideas. Sitting on the bed? Ingenious."
    er "Haha. Stop it."
    scene 03_667 with Dissolve(1)
    mc "Okay... We're on the bed. Now what?"
    er "We play a thousand questions!"
    mc "A thousand? Isn't it twenty questions?"
    er "Normally, yes. But I've got a few more."
    mc "That's a few more?"
    er "Uh-huh. Let's get comfortable."
    scene 03_668 with Dissolve(1)
    er "Alright. First question."
    mc "Wait-wait-wait-wait-wait... Wait..."
    mc "Why do you get to go first?"
    er "Well, I could list several reasons why I should, but technically you just asked me the first question, and I answered it. So now it's my turn."
    mc "{i}(Yup. She just outsmarted me.){/i}"
    scene 03_669 with Dissolve(1)
    mc "*Sigh* Fine..."
    m "{i}(Those two... Just like nothing's changed.){/i}"
    mc "Shoot."
    scene 03_670 with Dissolve(1)
    er "Why did you leave?"
    mc "Really? Right off the bat? But skip..."
    er "What? No! It doesn't work like that!"
    menu:
        "Cup size[KoGa3AutoWTChange1]{size=-4}(Erynn Week1 Cupsize) {/size} {/color}":
            $ Erynn_Week1_Cupsize = True
            mc "Of course you can skip questions."
            mc "Else I could ask you questions like, what's your cup size? You wouldn't want to answer that."
            scene 03_671 with Dissolve(1)
            er "32C..."
            mc "Uh? What?"
            er "My turn."
            mc "..."
            er "Why did you move back now?"
        "My turn":
            mc "Of course you can skip questions. My turn."
            er "No-no. You didn't answer mine. So I go again."
            er "Why did you move back now?"
    scene 03_672 with Dissolve(1)
    mc "..."
    mc "Next."
    er "Nuh-uh... It's either this or the first question. No more backing down."
    mc "*Sigh* Alright..."
    scene 03_673 with Dissolve(1)
    mc "So... Dad got engaged."
    jump Episode_4_Start

# Max Points:

# Alexis (14)
# Melissa (8)
# Layla (20)
# Elena (4)
# Emily (2)
# Erynn (4)
# Tori (2)

# MC_GoodStudent (6)

# MC_Sex (4)
# MC_BJ (2)
# Alexis_Sex (3)
# Tori_Sex (1)

#WTAdded
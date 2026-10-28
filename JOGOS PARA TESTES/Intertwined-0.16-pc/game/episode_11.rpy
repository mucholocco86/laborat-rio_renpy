label Episode_11_Start:

    #KoGa3 START#
    $ KoGa3GameProgress = "Ep11"
    #KoGa3 END#

    $ achievement.grant("ACHIEVEMENT_EPISODE_10")
    $ achievement.sync()
    $ Erynn_Week5_Tuesday_Photoshoot = False
    $ Erynn_Week5_Tuesday_Wakeup = False
    $ Erynn_Week5_Tuesday_SlapAss = False
    $ Erynn_Week5_Tuesday_Photoshoot_Join = False
    $ Erynn_Week5_Tuesday_Photoshoot_HiddenFeelings = False
    $ Erynn_Week5_Tuesday_Photoshoot_Checkout = False
    $ Alexis_Week5_Photoshoot_DogPicture = False
    $ Erynn_Week5_Tuesday_Room_Kiss = False
    $ Sienna_Week5_Tuesday_Hottest = False
    $ Layla_Week5_Tuesday_Hottub_Towel = False
    $ Elena_Week5_Tuesday_Hottub_69 = False
    $ Layla_Week5_Tuesday_Hottub_69 = False
    $ Sienna_Week5_Tuesday_Hottub_Sex = False
    $ Elena_Week5_Tuesday_Hottub_Grab = False
    $ Layla_Week5_Tuesday_Hottub_Grab = False
    $ Layla_Week5_Tuesday_Hottub_Chickenbreast = False
    $ Elena_Week5_Tuesday_Hottub_Threeway = False
    $ Elena_LikeMC = False
    $ Alexis_Week5_Wednesday_Run = False
    $ Emily_Week5_Wednesday_BeachInvite_Adriana = False
    $ Alexis_Week5_Wednesday_Beach = False
    $ Alexis_Week5_Wednesday_Beach_SP = False
    $ Tori_Week5_Wednesday_Beach_Sex = False
    $ Tori_Week5_Wednesday_Beach_LickAss = False
    $ Iris_Week5_Wednesday_Beach_Sex = False
    $ Alexis_Week5_Wednesday_Beach_Sex = False
    $ KFM_Kill_Alexis = False
    $ KFM_Kill_Erynn = False
    $ KFM_Kill_Iris = False
    $ KFM_Fuck_Alexis = False
    $ KFM_Fuck_Erynn = False
    $ KFM_Fuck_Iris = False
    $ KFM_Marry_Alexis = False
    $ KFM_Marry_Erynn = False
    $ KFM_Marry_Iris = False
    $ Alexis_Week5_Wednesday_Beach_Join = False
    $ Erynn_Week5_Wednesday_Beach_Join = False
    $ Iris_Week5_Wednesday_Beach_Join = False
    $ Alexis_Week5_Wednesday_Beach_CumMouth = False
    $ Alexis_Week5_Wednesday_Beach_CumFace = False
    $ Alexis_Week5_Wednesday_Beach_CumTits = False
    $ Alexis_Week5_Wednesday_Club_KissIris = False
    $ Adriana_Week5_Wednesday_Kiss = False
    $ Layla_Week5_Wednesday_ClubDate = False
    $ Layla_Week5_Wednesday_FirstTime = False
    $ Layla_Week5_Wednesday_LikeElenaKnow = False
    $ Layla_Girlfriend = False
    $ Layla_Week5_Wednesday_BreakUp = False



    if Erynn_Week3_Monday_Blackmailhelp == False:
        jump Week5_Tuesday_Kitchen
    else:
        jump Week5_Tuesday_Erynn

label Week5_Tuesday_Erynn:
    $ Erynn_Week5_Tuesday_Photoshoot = True
    scene black with Dissolve(2)
    pause 2
    stop music fadeout 1.0
    play music ("Music/LoFi Indie 3.mp3", "Music/LoFi Indie 1.mp3", "Music/LoFi Indie 2.mp3") volume 0.2
    n "Tuesday, 08:07."
    scene 11_001 with Dissolve(1)
    n "*Door opening*"
    scene 11_002 with Dissolve(1)
    er "*Whispers* Gotcha!"
    scene 11_003 with Dissolve(1)
    er "*Whispers* You look cute when you're sleeping."
    er "*Whispers* But that won't save you today."
    er "*Whispers* I just... I just have to, you know?"
    menu:
        "Wake up[KoGa3AutoWTChange1]{size=-4}(Erynn Week5 Tuesday Wakeup) {/size} {/color}":
            $ Erynn_Week5_Tuesday_Wakeup = True
            scene 11_004 with Dissolve(1)
            mc "You just have to, huh?"
            er "Aah... [mc]! No... How?"
            mc "{i}(She looks different, somehow...){/i}"
            scene 11_005 with Dissolve(1)
            er "How are you awake? I was so quiet this time."
            mc "Quiet? You call this quiet?"
            mc "You're sitting mere inches away from me, breathing and whispering in my face."
            er "..."
            if Erynn_Week4_Saturday_Jump_Cara == True:
                er "I had to double-check if it was really you!"
            else:
                if Erynn_Week4_Saturday_Jump_Nikki == True:
                    er "I had to double-check if it was really you!"
                else:
                    pass
            scene 11_006 with Dissolve(1)
            er "*Sigh* It's not fair! It used to be so easy."
            mc "Haha. How about you give up?"
            er "NO! I'll get you one of these days."
        "Wait and see what Erynn is up to":
            scene 11_007 with vpunch
            er "Time to wake up!"
            mc "Erynn!"
            er "Haha. I got you at last! You didn't expect this, huh?"
            mc "..."
            scene 11_008 with Dissolve(1)
            er "Morning, sunshine."
            mc "{i}(She looks happy today. Also different?){/i}"
            mc "Good morning, Erynn. How are you?"
            er "Fantastic!"
            scene 11_009 with Dissolve(1)
            er "Haha... I knew I still had it!"
            mc "Heh. Glad you're enjoying yourself so much."
    scene 11_010 with Dissolve(1)
    mc "What time is it anyway?"
    mc "Eight? Uh... Didn't you say you'll be here around ten?"
    er "Yeah..."
    mc "Then why are you here so early?"
    scene 11_011 with Dissolve(1)
    er "Uhm..."
    er "You see... You work out, right?"
    er "So I wanted you to show me some exercises to get a... Like a six-pack or something... To look better for the photo shoot."
    mc "A six-pack... For today's photo shoot...?"
    er "Uh-huh!"
    scene 11_012 with Dissolve(1)
    mc "Because you'll get a six-pack after doing ten sit-ups, right?"
    mc "Bullshit!"
    er "Haha. I had to come up with something."
    mc "And getting a six-pack was the best you could think of?"
    er "Haha."
    scene 11_013 with Dissolve(1)
    er "Okay, but I could really use some kind of exercise. Get rid of a little body fat here and there."
    mc "Body fat? Where do you have body fat?"
    er "Like here, my sides and around my stomach..."
    menu:
        "Ask Melissa":
            scene 11_014 with Dissolve(1)
            mc "*Shakes head* Do girls use different mirrors or something? You see things that aren't even there."
            if Alexis_Dating == True:
                mc "{i}(Alexis does the same shit. Every time she looks in a mirror, she's... I don't know... Disappointed?){/i}"
            else:
                pass
            mc "I think you look great as you are now. But if you want to do some exercises. Why don't you ask Melissa?"
            mc "She does yoga and Pilates and stuff. I'm sure she can help you."
            er "..."
            if Erynn_LikeMC == True:
                scene 11_015 with Dissolve(1)
                er "*Mumbles* But I want you to show me..."
                mc "What?"
                er "Nothing."
            else:
                pass
        "Show me[KoGa3AutoWTChange1]{size=-4}(Erynn Points+2) {/size} {/color}":
            $ Erynn_Points += 2
            # Erynn (56)
            scene 11_016 with Dissolve(1)
            mc "Show me where, exactly. I don't see anything."
            mc "Do girls use different mirrors or something? You see things that aren't even there."
            if Alexis_Dating == True:
                mc "{i}(Alexis does the same shit. Every time she looks in a mirror, she's... I don't know... Disappointed?){/i}"
            else:
                pass
            er "No, here. Feel it."
            scene 11_017 with Dissolve(1)
            mc "Ah, you mean this!"
            er "Haha. [mc]... That... [mc]!"
            mc "What?"
            er "That... Haha..."
            scene 11_018 with Dissolve(1)
            er "[mc]! Haha. Please... Haha. Stop..."
            mc "Where are you going? You wanted to exercise. And laughing is a really good exercise! Can't you feel all those muscles? Because I can."
            er "Haha. I can't... My stomach is hurting... [mc]. Haha..."
            mc "See! It's working already. Two more sets!"
            er "Haha... What...?"
            scene 11_019 with Dissolve(1)
            er "I meant it though. Please show me some exercises next time."
            mc "Sure."
            er "Easy ones!"
            mc "Maybe."
            er "Haha."
    scene 11_020 with Dissolve(1)
    er "Come on! It's time to get out of bed now!"
    mc "No. Erynn... Wait!"
    scene 11_021 with Dissolve(1)
    mc "AAAH!"
    scene 11_022 with Dissolve(1)
    er "..."
    scene 11_023 with Dissolve(1)
    er "Why are you naked?"
    mc "Because it was hot last night and... What does it matter? Why did you...?"
    er "I don't know. I wanted to get you out of bed... I didn't know you weren't wearing anything..."
    mc "I tried to warn you!"
    er "I..."
    scene 11_024 with Dissolve(1)
    er "..."
    er "Sorry."
    mc "It's fine."
    scene 11_025 with Dissolve(1)
    mc "What are you doing?"
    er "Looking for your underwear."
    mc "Uh... They're in the drawers... Just give me a minute."
    scene 11_026 with Dissolve(1)
    er "Alright. You go find some underwear and I'll pull up your blinds in the meantime."
    mc "..."
    mc "You can also wait outside, Erynn."
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 11_027 at moveup
    pause 3
    mc "{i}(And she's worried about her body?){/i}"
    mc "{i}(She has curves in all the right places.){/i}"
    mc "{i}(I think most people would do anything to have her figure.){/i}"
    scene 11_028 with Dissolve(1)
    er "Are you ready, or...?"
    mc "Yeah, you can turn around."
    scene 11_029 with Dissolve(1)
    er "..."
    mc "..."
    scene 11_030 with Dissolve(1)
    er "Haha..."
    mc "Haha. This never happened, okay?"
    if Erynn_LikeMC == True:
        er "..."
    else:
        er "Sure."
    scene 11_031 with Dissolve(1)
    er "What?"
    mc "I noticed earlier. You look different today."
    er "I don't have on the makeup I usually wear, since they do my makeup at the shoot."
    er "So I keep it somewhat clean."
    scene 11_032 with Dissolve(1)
    mc "Yeah, that's it. Less eyeshadow and stuff."
    er "Haha. And stuff..."
    mc "You look good."
    er "Thanks."
    if Alexis_Week5_Monday_Makeup == False:
        pass
    else:
        scene 11_033 with Dissolve(1)
        mc "I was with Alexis yesterday and she wasn't wearing any makeup either when I picked her up."
        mc "I actually did the makeup for her."
        er "I heard."
        mc "Of course you did..."
        mc "{i}(It's like dating the both of them without having all the perks...){/i}"
        scene 11_034 with Dissolve(1)
        mc "She said that I did a very good job. Especially for the first time."
        er "She must like you a lot!"
        mc "Hey! I really did well, okay?"
        er "Uh-huh."
        scene 11_035 with Dissolve(1)
        mc "Should I prove it to you and do yours?"
        er "Haha. No, no! I'm good."
        mc "..."
    scene 11_036 with Dissolve(1)
    mc "What did you do yesterday?"
    er "I was out with Iris."
    mc "Oh, you were?"
    mc "{i}(Seems like Iris got her date.){/i}"
    er "Mm-hmm. We went shopping. She wanted a new bikini. Oh, and we got some ice cream."
    scene 11_037 with Dissolve(1)
    mc "Heh, ice cream? She didn't do anything inappropriate, right?"
    er "Uhm... No? Like what?"
    mc "Nothing. Just Iris stuff, I guess."
    er "No. Everything was fine. She insisted that I try a few bikinis also."
    mc "{i}(Haha. I knew it.){/i}"
    scene 11_038 with Dissolve(1)
    mc "Did you get anything?"
    er "Yeah. I got a new one too."
    if Alexis_Dating == True:
        if Alexis_Week5_Monday_Date_Cancel == False:
            er "If you want to see it, we're going to the beach either tomorrow or Thursday."
            scene 11_039 with Dissolve(1)
            mc "You and Iris?"
            er "And Alexis. Hasn't she said anything yet? Iris wanted you to come too. Alexis will probably call you later and ask you to come."
            mc "{i}(The double date... I guess I'll do Iris the favour.){/i}"
            mc "Sounds like fun. I'll definitely come."
            er "Great!"
        else:
            pass
    else:
        if Alexis_SecretPath == True:
            er "If you want to see it, we're going to the beach either tomorrow or Thursday."
            scene 11_039 with Dissolve(1)
            mc "You and Iris?"
            er "And Alexis. If you want to come too, you're welcome to join us."
            mc "{i}(Hanging out with three hotties at the beach. Doesn't sound bad!){/i}"
            mc "Yeah, I'll think about it."
            er "Alright."
        else:
            pass
    scene 11_040 with Dissolve(1)
    er "Nggh..."
    mc "Tired or getting nervous?"
    er "For the photo shoot? No. When I first started yes, but I've done plenty since then."
    er "I usually don't get nervous anymore. Maybe I will today, since you're going to watch."
    mc "I'm excited to see you in your element."
    scene 11_041 with Dissolve(1)
    mc "Will there be more models?"
    er "Uh... One more."
    mc "So, you'll be fighting with another girl for the perfume bottle?"
    er "No. It's... a guy."
    mc "Oh..."
    scene 11_042 with Dissolve(1)
    mc "A guy... Now I'm a little less excited."
    er "Haha. You don't have to watch him."
    mc "Why is there a guy in an ad for female perfume anyway?"
    er "That's what the marketing team of the client decided."
    scene 11_043 with Dissolve(1)
    mc "Does he work at the same agency you do?"
    er "I don't know who they hired, so I don't know."
    mc "Hmm..."
    scene black with Dissolve(1)
    pause 2
    scene 11_044 with Dissolve(1)
    er "Hey."
    mc "Yeah?"
    er "How long have you been back now? A month?"
    mc "I think so, yes. Something like that."
    scene 11_045 with Dissolve(1)
    er "Why is your room still so empty?"
    mc "What do you mean? I think it looks clean."
    er "It looks like you're ready to leave at any moment."
    scene 11_046 with Dissolve(1)
    mc "You don't have to worry about that. I'm not going anywhere."
    mc "You won't get rid of me that easily."
    er "*Nods*"
    scene 11_047 with Dissolve(1)
    er "Why don't you put up some posters on the wall there? There's so much empty space."
    er "You used to have so many. What happened to them?"
    mc "They were old gaming posters and stuff. I'm not gonna hang them up there again."
    er "Get some new posters then. Or hang some pictures or paintings."
    scene 11_048 with Dissolve(1)
    mc "But I don't know of what. Any ideas?"
    er "I can give you some pictures."
    mc "I'm not going to hang pictures of you there."
    er "Why not?"
    mc "Really? Why not?"
    scene 11_049 with Dissolve(1)
    mc "Well... If I have other girls over or something. It'd be awkward if they saw your picture."
    er "What other girls?"
    if Alexis_Dating == True:
        mc "Alexis, for starters."
        er "Lexi wouldn't mind."
        mc "..."
    else:
        if Erynn_Week4_Saturday_NikkiLie == True:
            mc "I don't know. Just saying. A future girlfriend, maybe?"
            er "..."
        else:
            if Erynn_Week4_Saturday_CaraLie == True:
                mc "I don't know. Just saying. A future girlfriend, maybe?"
                er "..."
            else:
                if Nikki_Girlfriend == True:
                    mc "Nikki, for starters."
                    er "Nikki knows who I am. She wouldn't mind, I think. Actually, no. I think she would. And I don't want her to tackle me again."
                    mc "Erynn..."
                else:
                    if Cara_Girlfriend == True:
                        mc "Cara, for starters."
                        er "Cara knows me. I think she wouldn't mind."
                    else:
                        mc "I don't know. Just saying. A future girlfriend, maybe?"
                        er "..."
    scene 11_050 with Dissolve(1)
    er "Let's go shopping next time, and look for stuff, okay?"
    mc "We can do that."
    mc "Anyway. I'd better go shower now and get ready."
    er "Okay. I'll wait downstairs with Emily."
    scene 11_051 with Dissolve(1)
    mc "Is there a specific dress code or anything?"
    er "No, look at what I'm wearing."
    mc "Yeah but you're getting dressed there."
    er "Casual is fine. Wear the stuff you usually wear."
    menu:
        "Go shower":
            pass
        "Slap her ass[KoGa3AutoWTChange1]{size=-4}(Erynn Week5 Tuesday SlapAss, Erynn Points+2) {/size} {/color}":
            $ Erynn_Week5_Tuesday_SlapAss = True
            $ Erynn_Points += 2
            # Erynn (58)
            scene 11_052 with vpunch
            mc "Let's go!"
            er "Ahh... [mc]!"
            scene 11_053 with Dissolve(1)
            er "Stop slapping my ass!"
            mc "Haha. That's what you get for waking me!"
            if Erynn_Week5_Tuesday_Wakeup == True:
                er "I didn't even wake you!"
                mc "You tried, but failed. Again!"
                er "One day..."
            else:
                er "..."
    scene 11_054 with Dissolve(1)
    m "Could you wake him?"
    if Erynn_Week5_Tuesday_Wakeup == True:
        er "Seems like he's getting used to waking up early."
    else:
        er "Mm-hmm. I got him this time!"
    scene 11_055 with Dissolve(1)
    m "Can I get you anything? Some breakfast, a coffee?"
    er "Thanks but I can't eat or drink before the photo shoot."
    m "Ah, you poor thing."
    er "It's alright. The shoot should only take about an hour."
    scene black with Dissolve(1)
    pause 2
    scene 11_056 with Dissolve(1)
    m "How long have you been modelling now?"
    er "A little over three years."
    m "It's been three years already? Wow."
    mc "{i}(Mom's still here?){/i}"
    scene 11_057 with Dissolve(1)
    mc "Morning, Mom."
    m "Good morning, honey."
    mc "Why are you still here? Don't you have to be at the restaurant?"
    scene 11_058 with Dissolve(1)
    m "I'll go later. I have to... Uhm... I have to go to the police station first."
    mc "Police station? Why? Did something happen?"
    m "I'll tell you later. I have to leave now anyway."
    mc "Okay...?"
    scene 11_059 with Dissolve(1)
    m "Thank you for helping me with the dishes, Erynn."
    er "No problem."
    m "And good luck with the photo shoot."
    er "Thanks."
    scene 11_060 with Dissolve(1)
    m "I don't know when I'll be back. Probably late tonight."
    m "You can always come by the restaurant if you're hungry."
    mc "Will do."
    if Erynn_Week5_Tuesday_SlapAss == False:
        scene 11_065 with Dissolve(1)
        m "Anyway. Have fun, you two."
        m "See you later, [mc]. Bye, Erynn."
        er "Bye, Emily."
        mc "Later, Mom."
    else:
        scene 11_061 with vpunch
        mc "What? Hey..."
        mc "Mom! What are you doing?"
        m "Okay, Erynn. Now! I've got him!"
        mc "What?"
        scene 11_062 with Dissolve(1)
        er "Now it's your turn!"
        mc "What are you doing with that spoon?"
        mc "Erynn!"
        scene 11_063 with Dissolve(1)
        mc "Don't do it, Erynn!"
        er "..."
        mc "You're making a mistake, and you know it."
        mc "This won't stop here."
        m "Don't listen to him, Erynn."
        scene 11_064 with Dissolve(1)
        er "*Sigh* I want to do this... But... I just can't..."
        er "Sorry, Emily."
        m "You're way too nice to him, Erynn."
        mc "I'm just very charming. Besides, I didn't do anything wrong to get spoon-slapped!"
        m "Uh-huh."
        scene 11_065 with Dissolve(1)
        m "Anyway. Have fun, you two."
        m "See you later, [mc]. Bye, Erynn."
        er "Bye, Emily."
        mc "Later, Mom."
        scene 11_066 with Dissolve(1)
        er "What are you smiling about?"
        mc "Nothing... Just being my usual smiley self."
        er "It wasn't because you're charming. I felt sorry for you!"
        mc "Hmm... Is that so?"
        scene 11_067 with Dissolve(1)
        mc "I am charming though!"
        er "Haha. No!"
        mc "You literally just admitted it!"
        if Erynn_LikeMC == True:
            scene 11_068 with Dissolve(1)
            mc "So are you, by the way."
            er "..."
        else:
            pass
    scene 11_069 with Dissolve(1)
    mc "Do we still have time for me to eat some breakfast?"
    er "We have time. Go ahead."
    mc "Do you want anything?"
    er "I'm good."
    scene 11_070 with Dissolve(1)
    mc "Sure you don't want anything?"
    er "I can't eat before the shoot. Especially carbs."
    if Nikki_Visit == True:
        mc "And you say you and Nikki won't get along..."
        er "What?"
        mc "Carbs and stuff..."
        er "Still don't get it."
    else:
        mc "Let's grab something after the shoot, then."
        er "Thanks."
    scene black with Dissolve(1)
    pause 2
    scene 11_077 with Dissolve(1)
    er "Mom's also still here."
    mc "She didn't have to go to the police station?"
    er "Heh, no. She has an appointment with a high-end client to do her hair."
    mc "Someone famous?"
    er "I haven't asked."
    scene 11_078 with Dissolve(1)
    er "Give me a minute. I'll get my stuff."
    er "Be right back."
    mc "Sure, I'll wait here."
    scene 11_079 with Dissolve(1)
    me "Hey there."
    mc "Hey, Melissa."
    me "Waiting for Erynn?"
    mc "Yeah. She needed to quickly grab her stuff."
    scene 11_080 with Dissolve(1)
    me "I think it will take a little longer. She just went into the bathroom."
    mc "Nervous poo?"
    me "*Shakes head* Haha, [mc]! Don't tell her that. And I didn't say anything."
    mc "Haha."
    scene 11_081 with Dissolve(1)
    mc "Who's hair are you doing today? Erynn said she's a high-end client."
    me "Ximena Vergara."
    mc "Hmm... Don't know who that is."
    me "She's playing the mother in Entanglement."
    mc "Ah, that TV show. Lots of people seem to watch it."
    scene 11_082 with Dissolve(1)
    me "Mm-hmm. It's pretty popular."
    mc "By the way. Do you know why Mom had to go to the police station?"
    me "The police station? That's the first I've heard about it. No, I have no idea."
    scene 11_083 with Dissolve(1)
    me "But don't worry. It's probably just some sort of formality or something like that."
    me "I'll call her later."
    mc "Thanks."
    me "I've gotta leave. I can't be late."
    scene 11_084 with Dissolve(1)
    mc "Later, Mel."
    me "Bye, [mc]."
    scene black with Dissolve(1)
    pause 2
    scene 11_085 with Dissolve(1)
    er "Sorry. Took a little longer."
    er "Something came up."
    mc "..."
    menu:
        "Joke":
            scene 11_086 with Dissolve(1)
            er "Why are you smiling like that again?"
            mc "Something came up? Didn't you mean out?"
            er "..."
            scene 11_087 with Dissolve(1)
            er "Ew... You are so disgusting sometimes."
            er "And... I wasn't... I didn't..."
            er "*Sigh*"
            mc "Haha. Sorry, Erynn."
            scene 11_088 with Dissolve(1)
            er "Here. You drive!"
            mc "Haha. Don't be mad. It was a joke."
            scene 11_090 with Dissolve(1)
            mc "Hey! I said I was sorry."
            mc "Aren't you going to talk to me the whole drive?"
            er "..."
            scene 11_091 with Dissolve(1)
            mc "Want to continue playing a thousand questions?"
            er "..."
            mc "I'll let you ask all the questions! Hmm?"
            er "Fine. And no skipping!"
        "Take her bag":
            scene 11_086 with Dissolve(1)
            er "Why are you smiling like that again?"
            mc "No reason..."
            mc "Let me carry that."
            er "Thanks."
            scene 11_089 with Dissolve(1)
            er "Do you mind driving?"
            mc "Sure, I'll drive."
            scene 11_092 with Dissolve(1)
            er "Want to continue with our game?"
            mc "The questions?"
            er "Yeah. But no rules this time. I can ask as many questions as I want."
            mc "Fine. Go ahead."
    jump Week5_Tuesday_Erynn_Photoshoot

label Week5_Tuesday_Kitchen:
    scene black with Dissolve(2)
    pause 2
    stop music fadeout 1.0
    play music ("Music/LoFi Indie 3.mp3", "Music/LoFi Indie 1.mp3", "Music/LoFi Indie 2.mp3") volume 0.2
    n "Tuesday, 09:14."
    scene 11_071 with Dissolve(1)
    mc "{i}(Mom's still here?){/i}"
    scene 11_072 with Dissolve(1)
    mc "Morning, Mom."
    m "Good morning, honey."
    mc "Why are you still here? Don't you have to be at the restaurant?"
    scene 11_073 with Dissolve(1)
    m "I'll go later. I have to... Uhm... I have to go to the police station first."
    mc "Police station? Why? Did something happen?"
    m "I'll tell you later, because I actually have to leave now."
    mc "Okay...?"
    scene 11_074 with Dissolve(1)
    m "Can you do me a favour and finish the dishes, please? It's just a few plates left."
    mc "Sure, no problem."
    m "Thanks."
    m "I don't know when I'll be back. Probably late tonight."
    m "You can always come by the restaurant if you're hungry, or order something."
    mc "Will do."
    scene 11_075 with Dissolve(1)
    m "See you later, [mc]."
    mc "Bye, Mom."
    scene 11_076 with Dissolve(1)
    mc "{i}(Police station, huh?){/i}"
    mc "{i}(I'm actually curious what it's about.){/i}"
    jump Week5_Tuesday_Room

label Week5_Tuesday_Erynn_Photoshoot:
    scene black with Dissolve(1)
    pause 2
    stop music fadeout 1.0
    play music ("Music/LoFi Upbeat 2.mp3", "Music/LoFi Upbeat 4.mp3", "Music/LoFi Upbeat 3.mp3", "Music/LoFi Upbeat 1.mp3") volume 0.2
    scene 11_093 with Dissolve(1)
    er "This is it."
    mc "Oh... It's just a small photo studio."
    mc "Somehow I expected a whole movie set with props and stuff."
    er "It's just a few pictures for an ad campaign in a magazine. If it were for a TV commercial, we'd probably be in a different location."
    mc "I see."
    scene 11_094 with Dissolve(1)
    ph "A little to the right."
    ph "The other right!"
    x "So to the left?"
    ph "To the right!"
    scene 11_095 with Dissolve(1)
    er "*Whispers* Oh no..."
    mc "*Whispers* What?"
    er "*Whispers* That's the same photographer as the shoot on Friday."
    mc "*Whispers* Haha. The 'I can't work like this' guy?"
    er "*Sigh* That's him."
    scene 11_096 with Dissolve(1)
    mc "*Whispers* Maybe he's a little more chill today."
    er "*Whispers* I hope so."
    ph "Seriously... What don't you understand about moving it to the right? It's not that difficult."
    er "..."
    mc "Maybe not."
    scene 11_097 with Dissolve(1)
    er "Hey guys."
    x "Hello. You must be Erynn."
    x "I'm Jenna. I'm doing your makeup today."
    er "Nice to meet you, Jenna."
    scene 11_098 with Dissolve(1)
    er "This is my friend, [mc]."
    mc "Hi."
    je "Hey. Let me introduce you to the others and then we can start doing your makeup already."
    er "Alright."
    scene 11_099 with Dissolve(1)
    mc "Erynn. I'm gonna sit in one of those chairs there. I don't wanna be standing in the way."
    mc "You do your thing."
    er "Hehe, my thing... I will."
    scene 11_100 with Dissolve(1)
    er "See you later then."
    mc "Have fun."
    er "Thanks."
    scene 11_101 with Dissolve(1)
    mc "{i}(How many people are needed at a photo shoot? Like damn.){/i}"
    mc "{i}(Photographer, model, makeup artist, hairstylist, the client themself...){/i}"
    mc "{i}(Never mind. I guess I just answered my own question.){/i}"
    mc "{i}(I hope one specific guy doesn't show up today though!){/i}"
    scene black with Dissolve(1)
    pause 2
    scene 11_102 with Dissolve(1)
    mc "{i}(I guess this will take a while.){/i}"
    scene black with Dissolve(1)
    pause 2
    scene 11_103 with Dissolve(1)
    er "*Waves*"
    mc "{i}(Oh wow. She looks so different already.){/i}"
    mc "{i}(Honestly. Makeup is such a scary thing.){/i}"
    scene black with Dissolve(1)
    pause 2
    scene 11_104 with Dissolve(1)
    er "Hey."
    mc "Hey. Small break?"
    er "You could say that. Makeup and hair is done and I'm waiting for the dress now."
    er "They decided on another dress last minute, but that one needs a slight adjustment."
    scene 11_105 with Dissolve(1)
    er "How are you holding up?"
    mc "Eh..."
    er "Sorry, this must be boring for you."
    mc "Nah, it's alright. Okay, maybe a little bit, but the good stuff has yet to come."
    er "Just a few more minutes and we start shooting."
    scene 11_106 with Dissolve(1)
    er "By the way. What do you think?"
    mc "Of the makeup?"
    er "Uh-huh."
    menu:
        "Looks good":
            scene 11_107 with Dissolve(1)
            mc "Mm-hmm."
            er "Haha. Mm-hmm? That's your answer?"
            mc "It is. It looks good. It looks really good, Erynn."
            er "Thanks."
            scene 11_108 with Dissolve(1)
            mc "Now with the right dress, you're gonna look so sexy."
            mc "Can't wait to see those pictures."
            mc "Maybe I should hang one up in my room after all."
            er "..."
        "Natural":
            scene 11_109 with Dissolve(1)
            mc "*Whispers* I'm not going to say this too loud because I don't want to upset the makeup artist."
            mc "*Whispers* But I liked the one you had before better. A little more natural."
            er "Heh. Thanks."
    scene 11_110 with Dissolve(1)
    mc "You said earlier there would be a guy in the shoot. It's not one of them, right?"
    er "No. He isn't here yet. I have some solo pictures first, so I guess he's coming a little later."
    er "Don't worry. You'll meet him soon."
    mc "Funny..."
    scene 11_111 with Dissolve(1)
    je "Erynn, we're ready with the dress."
    er "Okay, I'm coming."
    scene black with Dissolve(1)
    pause 2
    scene 11_112 with Dissolve(1)
    mc "{i}(We've been here an hour already?){/i}"
    mc "{i}(Didn't feel like that at all.){/i}"
    er "Hey."
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 11_113 at moveup
    pause 3
    mc "..."
    mc "{i}(Holy shit!){/i}"
    mc "{i}(How can she become even more beautiful?){/i}"
    scene 11_114 with Dissolve(1)
    mc "You look incredible, Erynn."
    er "Thank you."
    scene 11_115 with Dissolve(1)
    x "Let me take a look."
    x "Yes! This is exactly what we had envisioned for this campaign. Greek Goddess! Perfect."
    x "Let's get this started then. Frank, I'll leave her in your hands."
    scene 11_116 with Dissolve(1)
    ""
    scene 11_117 with Dissolve(1)
    ""
    scene black with Dissolve(1)
    pause 2
    scene 11_118 with Dissolve(1)
    ph "Walk towards me."
    ph "One more time. Tilt your head a bit higher."
    ph "Yes."
    scene 11_119 with Dissolve(1)
    ph "Beautiful."
    scene 11_120 with Dissolve(1)
    ph "Look seductive."
    ph "Yes! That's it."
    scene 11_121 with Dissolve(1)
    x "Hey."
    menu:
        "Jenna":
            mc "Hi. Jenna, was it?"
            je "Correct."
        "Jenny":
            mc "Hi. Jenny, was it?"
            je "Jenna."
            mc "Sorry. Jenna."
            je "Close enough."
    scene 11_122 with Dissolve(1)
    je "Gorgeous, isn't she?"
    mc "She always has been."
    je "You've known each other for long?"
    mc "We pretty much grew up together."
    scene 11_123 with Dissolve(1)
    je "Oh. Childhood sweethearts..."
    mc "Eh... We're friends."
    je "What do you do? Also in the modelling business?"
    mc "{i}(Do I look like a model to her?){/i}"
    mc "Heh, no. I'm a student."
    if Erynn_LikeMC == True:
        scene 11_124 with Dissolve(1)
        er "..."
        ph "Yes! That's the look I'm after. Desire!"
    else:
        pass
    scene 11_125 with Dissolve(1)
    je "MSU?"
    mc "{i}(I'm a student, so...){/i}"
    mc "Yeah..."
    je "Anyway I was about to take a quick break. Do you smoke?"
    mc "I don't."
    scene 11_126 with Dissolve(1)
    x "Jenna. Can you try calling again?"
    x "We're running out of time."
    je "Sure."
    scene 11_127 with Dissolve(1)
    je "..."
    je "Zane! Finally! We're waiting for you. Where are you?"
    mc "{i}(Zane?){/i}"
    scene 11_128 with Dissolve(1)
    ph "Pete, can you turn on the wind machine."
    ph "Start with thirty per cent."
    scene 11_129 with Dissolve(1)
    er "Aaah!"
    mc "{i}(Hot damn...){/i}"
    if Erynn_LikeMC == True:
        mc "{i}(I wouldn't mind having that picture.){/i}"
    else:
        pass
    scene 11_130 with Dissolve(1)
    ph "What are you doing? I said thirty per cent!"
    x "I'm changing it right now."
    ph "How about you switch it before you turn it on?"
    ph "Turn it off now, first! Redo her hair, please."
    scene 11_131 with Dissolve(1)
    er "I'm sorry for screaming. That just took me by surprise."
    x "It's fine. Don't worry about it. Let me fix your hair."
    scene 11_132 with Dissolve(1)
    ph "All good?"
    er "Yes."
    ph "Let's continue. Thirty per cent this time!"
    scene 11_133 with Dissolve(1)
    ph "Yes! Very nice."
    ph "Tilt your head up and close your eyes."
    mc "{i}(That looks like the pose we did yesterday... She should nail this one.){/i}"
    scene black with Dissolve(1)
    pause 2
    scene 11_134 with Dissolve(1)
    mc "{i}(Can't wait to see those pictures.){/i}"
    mc "{i}(And see which one they'll choose for the magazine.){/i}"
    scene 11_135 with Dissolve(1)
    ""
    scene 11_136 with Dissolve(1)
    ph "Yes, Erynn. Give me fuel, give me that fire. Show me everything you desire!"
    mc "..."
    mc "{i}(What? Aren't they some kind of lyrics?){/i}"
    if Erynn_LikeMC == True:
        scene 11_137 with Dissolve(1)
        mc "{i}(She's so sexy. But why is she looking at me?){/i}"
        mc "{i}(Look to the camera, Erynn!){/i}"
    else:
        pass
    scene black with Dissolve(1)
    pause 2
    scene 11_138 with Dissolve(1)
    ph "That's a wrap for the solo pictures."
    ph "Has the other model shown up now?"
    x "Jenna, did you get a hold of him?"
    scene 11_139 with Dissolve(1)
    je "Uhm... Well... I've got some bad news."
    je "He won't make it. He broke his nose."
    ph "He broke his nose? Today?"
    je "Friday."
    scene 11_140 with Dissolve(1)
    x "Friday? And it didn't come to mind to let us know?"
    je "He hoped the swelling would be gone by today, but alas."
    ph "*Sigh* I can't work like this!"
    mc "{i}(Oh, here we go!){/i}"
    x "What are our other options?"
    scene 11_141 with Dissolve(1)
    x "Erynn, you can go take a break."
    x "We'll need to discuss some things first before we continue."
    er "Okay, thanks."
    x "You did great. I'm happy with the pictures so far."
    er "Thank you."
    scene 11_142 with Dissolve(1)
    er "Hey."
    mc "Hey. You were amazing, Erynn. You look so pretty. Those pictures are gonna be great."
    er "Thank you."
    mc "I don't know what to say. Just watching you was..."
    scene 11_143 with Dissolve(1)
    er "So, you're not bored anymore?"
    mc "I'm not. Quite the opposite."
    er "Which one was your favourite?"
    mc "Hmm..."
    menu:
        "All of them":
            scene 11_144 with Dissolve(1)
            mc "I can't decide. I liked them all to be honest."
            mc "Will they only take one for the magazine?"
            er "They will have a few for different designs."
        "The pose we did at home":
            scene 11_145 with Dissolve(1)
            mc "The pose we also did back at home."
            er "Oh, haha. The moment I did it, it reminded me of Sunday, actually."
            er "I had to concentrate hard not to start laughing."
            mc "Haha."
        "Lying down":
            scene 11_144 with Dissolve(1)
            mc "The one where you were lying down."
            mc "That one was really sexy."
        "Wind machine":
            scene 11_146 with Dissolve(1)
            mc "Uh... The one when the guy messed up with the wind machine."
            er "I knew it!"
            mc "Haha. I think you looked great. No posing or anything. Just pure Erynn. I hope he took a picture of that."
            er "..."
    scene 11_147 with Dissolve(1)
    mc "What happens now since that Zane guy isn't showing up?"
    er "Zane?"
    mc "I heard the name when Jenna was talking to him on the phone before. Do you think it might be..."
    er "I haven't seen him for quite some time, but I don't think that it's him."
    scene 11_148 with Dissolve(1)
    er "And I don't know what they'll do now."
    er "Probably postpone the shoot, but it needs to be soon. They were pressed for time already."
    mc "Hmm..."
    scene 11_149 with Dissolve(1)
    ph "How about him? Can't we use him?"
    mc "*Whispers* Eh... Are they talking about me?"
    er "*Whispers* I think so."
    ph "Do you mind taking off your shirt for a moment?"
    menu:
        "Take off shirt.":
            scene 11_151 with Dissolve(1)
            x "What do you think?"
            ph "Mm-hmm... I can definitely work with this!"
            mc "..."
            scene 11_152 with Dissolve(1)
            ph "He has the height and the build. He fits the profile."
            x "Yes and they'll look good together."
            scene black with Dissolve(1)
            pause 2
            scene 11_153 with Dissolve(1)
            gb "I guess it's time for introductions. I'm Gil Burke from Allure Cosmetics."
            mc "Hello, sir. I'm [mc]."
            gb "Nice to meet you, [mc]."
            gb "I'm gonna get straight to the point."
            scene 11_154 with Dissolve(1)
            gb "As you may have heard, we require a new male model for this shoot."
            gb "You actually fit the profile we're looking for and we're wondering if you might be interested in taking some pictures."
            mc "Uhm..."
            gb "Of course, you're gonna get compensated for your time."
            mc "Can you give me a minute?"
            scene 11_155 with Dissolve(1)
            mc "What do you think?"
            er "It's completely up to you, [mc]. You don't have to do it for me."
            er "If you don't feel comfortable taking these pictures, don't do it."
            menu:
                "Don't take pictures[KoGa3AutoWTChange1]{size=-4}(Erynn Points-4, Erynn Friends, Erynn LikeMCFalse) {/size} {/color}":
                    $ Erynn_Points -= 4
                    $ Erynn_Friends = True
                    $ Erynn_LikeMC = False
                    scene 11_156 with Dissolve(1)
                    mc "Yeah, it's not really something for me. I'm sorry."
                    er "Don't be sorry. As I said, it's fine either way."
                    er "And it's their problem to begin with."
                    jump Week5_Tuesday_Erynn_Photoshoot_End
                "Do the photo shoot[KoGa3AutoWTChange1]{size=-4}(Erynn Points+2, Erynn Week5 Tuesday Photoshoot Join, {i}Alexis Dating: Alexis JealousyPoints+2{/i}) {/size} {/color}":
                    $ Erynn_Points += 2
                    # Erynn (62)
                    $ Erynn_Week5_Tuesday_Photoshoot_Join = True
                    if Alexis_Dating == True:
                        $ Alexis_JealousyPoints += 2
                        # Alexis_Jealous (6)
                    else:
                        pass
                    scene 11_157 with Dissolve(1)
                    mc "I think I'll do it. It should be fun, and maybe a once-in-a-lifetime experience."
                    er "Yeah?"
                    mc "Why are you looking so happy?"
                    er "I don't know. I'm excited we're going to take some pictures together."
                    scene 11_158 with Dissolve(1)
                    mc "I'm in."
                    gb "Perfect. Thank you very much, [mc]."
                    gb "We'll have to do some paperwork, but we'll do that after the shoot."
                    mc "That's fine with me."
                    scene 11_159 with Dissolve(1)
                    gb "Jenna, can you get him ready."
                    je "Of course. Come, follow me."
                    gb "Eddy. Contact HQ and ask them to create a contract for a freelance model."
                    gb "We also need release papers for the pictures. Very important!"
                    jump Week5_Tuesday_Erynn_Photoshoot_MC
        "Don't take off shirt.[KoGa3AutoWTChange1]{size=-4}(Erynn Points-4, Erynn Friends, Erynn LikeMCFalse) {/size} {/color}":
            $ Erynn_Points -= 4
            $ Erynn_Friends = True
            $ Erynn_LikeMC = False
            scene 11_150 with Dissolve(1)
            mc "I'm sorry but I'm not really interested in being in a photo shoot."
            mc "I'm only here to support Erynn."
            ph "..."
            jump Week5_Tuesday_Erynn_Photoshoot_End

label Week5_Tuesday_Erynn_Photoshoot_MC:
    if _in_replay:
        $ Erynn_LikeMC = True
    scene black with Dissolve(1)
    pause 2
    scene 11_160 with Dissolve(1)
    er "You okay? Nervous?"
    mc "Not nervous, per se."
    er "It's gonna be fine!"
    scene 11_161 with Dissolve(1)
    mc "I'm just a little concerned about how they'll turn out."
    mc "I don't want to make you look bad."
    er "You won't! You never have!"
    scene 11_162 with Dissolve(1)
    er "And where's your confidence all of a sudden?"
    er "You've got this, [mc]."
    er "You're very handsome, and they think so too. Or else they wouldn't have asked you."
    scene 11_163 with Dissolve(1)
    mc "Have I told you already that you look amazing in that dress?"
    er "There it is! And thanks."
    ph "Okay, guys. Are you ready?"
    scene 11_164 with Dissolve(1)
    ph "The name of the perfume is Alluring Desire. And that's what I want to see in the pictures."
    ph "[mc], Erynn is the object of desire."
    ph "Imagine she's wearing the perfume and you're drawn to that smell."
    scene 11_165 with Dissolve(1)
    mc "{i}(That won't be a problem, Erynn always smells amazing.){/i}"
    ph "Yes! Very nice!"
    scene 11_166 with Dissolve(1)
    ph "Keep concentrating on her."
    ph "Beautiful."
    if Erynn_LikeMC == True:
        scene 11_167 with Dissolve(1)
        mc "..."
        scene 11_168 with Dissolve(1)
        er "*Whispers* Enjoying the view?"
        mc "..."
        mc "*Whispers* Sorry. But I have to desire you, you heard him."
        er "Uh-huh..."
    else:
        pass
    scene 11_169 with Dissolve(1)
    gb "How are they doing?"
    ph "I think we got fortunate with him."
    if Erynn_LikeMC == True:
        $ Erynn_Week5_Tuesday_Photoshoot_HiddenFeelings = True
        ph "They have this natural connection. Like they're drawn to each other. Hidden feelings."
        ph "You can see it in all the pictures. You can't fake something like this."
        gb "Hidden feelings... That's also a good name for perfume. I'll have to write that down."
    else:
        gb "Yeah. The pictures are looking great so far."
        gb "Keep it up, guys!"
    scene 11_170 with Dissolve(1)
    ph "Yes!"
    ph "Hold her a little longer like that."
    scene black with Dissolve(1)
    pause 2
    scene 11_171 with Dissolve(1)
    ph "Alright. Last picture before the outfit change."
    scene 11_172 with Dissolve(1)
    er "*Whispers* Oh no..."
    mc "*Whispers* What?"
    er "*Whispers* I forgot about that."
    mc "*Whispers* Erynn... What?"
    er "*Whispers* No... It's... It's nothing. I'll be right back."
    scene 11_173 with Dissolve(1)
    mc "{i}(Why is she so flustered all of a sudden?){/i}"
    mc "Uh... Do I have to change too?"
    ph "No. The pictures will only be from the waist up. You'll only need to remove the shirt."
    mc "Alright."
    scene black with Dissolve(1)
    pause 2
    scene 11_174 with Dissolve(1)
    mc "{i}(A bathrobe?){/i}"
    mc "{i}(Is she going to be in lingerie?){/i}"
    mc "{i}(I had a hard time keeping my composure before, but this...){/i}"
    scene 11_175 with Dissolve(1)
    mc "*Whispers* Uhm... Is everything okay? You look uncomfortable."
    er "*Whispers* It's..."
    ph "Alright. Let's take this last set of pictures. Erynn, please remove the robe."
    er "..."
    scene 11_176 with Dissolve(1)
    er "*Whispers* I'm sorry."
    mc "*Whispers* Why are you apologising?"
    er "*Deep breath*"
    scene 11_177 with Dissolve(1)
    mc "Uh..."
    mc "*Whispers* Erynn..."
    scene 11_178 with Dissolve(1)
    mc "..."
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 11_179 at moveup
    pause 3
    mc "{i}(She looks incredible.){/i}"
    mc "{i}(I don't know what to say. Should I even say anything?){/i}"
    menu:
        "Check her out[KoGa3AutoWTChange1]{size=-4}(Erynn Week5 Tuesday Photoshoot Checkout, {i}Erynn LikeMC: Erynn Points-4{/i}) {/size} {/color}":
            $ Erynn_Week5_Tuesday_Photoshoot_Checkout = True
            if Erynn_LikeMC == True:
                pass
            else:
                $ Erynn_Points -= 4
            scene 11_180 with Dissolve(1)
            ""
            scene 11_181 with Dissolve(1)
            mc "{i}(Fuck!){/i}"
        "Don't":
            pass
    scene 11_182 with Dissolve(1)
    mc "Uh..."
    mc "{i}(Why is she...?){/i}"
    er "*Whispers* Sorry. I was so happy when you agreed to do the pictures and I completely forgot about this."
    mc "*Whispers* It... It's fine."
    mc "{i}(It's not fine. I'm so hard.){/i}"
    scene 11_183 with Dissolve(1)
    mc "*Whispers* That's why you were so uncomfortable before?"
    er "*Whispers* No, not uncomfortable. Nervous. I would've been uncomfortable if it were with the other guy."
    mc "{i}(Right! Normally she would be doing this shoot with someone else. Just thinking about that now makes me jealous... And angry...){/i}"
    er "*Whispers* With you... I just... I didn't know how you would react."
    scene 11_184 with Dissolve(1)
    mc "*Whispers* You look incredible, Erynn. You are so beautiful."
    mc "*Whispers* And if I wasn't nervous before, I am now."
    er "Heh."
    if Erynn_LikeMC == True:
        mc "{i}(I can't describe this feeling. Holding her in my arms like this. Her naked boobs pressing up against me. My heart is absolutely racing.){/i}"
    else:
        pass
    scene 11_185 with Dissolve(1)
    er "*Whispers* I'm sorry I just pressed up against you. I didn't want to stand here like this and let them..."
    mc "*Whispers* If someone should be sorry, it's me, Erynn."
    er "*Whispers* Why?"
    mc "*Whispers* Don't make me say it..."
    er "*Whispers* Oh... That..."
    scene 11_186 with Dissolve(1)
    mc "*Whispers* Let's take some beautiful pictures now."
    er "Mm-hmm."
    scene black with Dissolve(1)
    pause 2
    scene 11_187 with Dissolve(1)
    ""
    scene 11_188 with Dissolve(1)
    ph "Yes! Very nice!"
    ph "Now pick her up. Her head above yours while you're smelling her neck."
    if Erynn_LikeMC == True:
        scene 11_189 with Dissolve(1)
        mc "{i}(Why does she smell so good?){/i}"
        mc "{i}(I don't know if it's the perfume or this situation we're in, but I...){/i}"
        scene 11_190 with Dissolve(1)
        er "..."
    else:
        scene 11_189 with Dissolve(1)
        ""
    scene 11_191 with Dissolve(1)
    ph "Alright. You can put her down."
    ph "Get the duvet."
    scene 11_192 with Dissolve(1)
    mc "{i}(Fuck! All these positions... Thanks photographer, but do you have any idea what Erynn is doing to me right now?){/i}"
    mc "{i}(If I knew this was going to happen. I'd have brought another pair of underwear...){/i}"
    scene 11_193 with Dissolve(1)
    ""
    scene 11_194 with Dissolve(1)
    ph "Move your arm down and look up a bit. [mc], cover her breasts with your arm."
    er "Uh..."
    mc "*Whispers* Are you okay with that? If not, just say no."
    er "*Whispers* No, you can..."
    scene 11_195 with Dissolve(1)
    er "..."
    mc "{i}(Don't squeeze, don't squeeze them... Just cover them...){/i}"
    mc "{i}(They feel incredible though. So soft...){/i}"
    $ renpy.end_replay()
    scene black with Dissolve(1)
    pause 2
    scene 11_196 with Dissolve(1)
    $ achievement.grant("ACHIEVEMENT_MODEL")
    $ achievement.sync()
    ph "That's a wrap."
    gb "Thank you everyone for your hard work."
    er "Thank you, Jenna."
    je "You're welcome. The pictures look amazing."
    jump Week5_Tuesday_Erynn_Photoshoot_End

label Week5_Tuesday_Erynn_Photoshoot_End:
    scene black with Dissolve(1)
    pause 2
    stop music fadeout 1.0
    play music "Sounds/Street_Traffic.mp3" volume 0.5
    if Erynn_Week5_Tuesday_Photoshoot_Join == False:
        scene 11_197 with Dissolve(1)
        mc "So now you'll have to go to another shoot?"
        er "Yeah. It should be in the next couple of days."
        mc "You'll get paid twice then?"
        er "Not really. I get paid by the hour and this shoot ended early."
        er "It's gonna be about the same in the end. Maybe a little more."
        scene 11_198 with Dissolve(1)
        mc "You must be hungry now. Shall we get something to eat?"
        er "Actually, I'm not hungry. But we can go somewhere you like. My treat."
        mc "I'm good, too."
        er "You don't have to hold back just because I'm not hungry."
        scene 11_199 with Dissolve(1)
        mc "I had a big bowl of cereal this morning and it's not even noon yet. But... I could use a coffee."
        er "Same. You want to go to a café, or take it to go?"
        mc "I've been sitting this whole time. Let's get some to go and walk along the pier or something."
        er "Okay. Let's cross here and get some at the Italian café."
    else:
        scene 11_200 with Dissolve(1)
        er "What are you thinking about?"
        mc "I don't know. This still feels unreal. Did we really do that photo shoot together, or am I still dreaming or something?"
        scene 11_201 with Dissolve(1)
        mc "Uh..."
        er "Does this feel like you're dreaming?"
        mc "..."
        mc "{i}(Yes and no!){/i}"
        er "By the way. Thank you very much, [mc]!"
        if Erynn_LikeMC == True:
            scene 11_202 with Dissolve(1)
            mc "{i}(Now she's pressing her boobs against me again.){/i}"
            mc "{i}(Please don't look at me like that.){/i}"
            mc "{i}(I'm trying to get rid of my boner and not walk around with one the whole day.){/i}"
        else:
            pass
        scene 11_203 with Dissolve(1)
        er "Did you sign all the papers?"
        mc "I did. Three copies of the contract and release papers. Even got a nice envelope with some cash in it. Guess how much I've got."
        er "I don't know. How much?"
        mc "Two hundred dollars!"
        er "Two hundred? That's good! That's really good! You deserved that!"
        scene 11_204 with Dissolve(1)
        mc "How much will you get?"
        er "Uhm..."
        mc "I know it's more than what I've got."
        er "..."
        mc "Is it that much more?"
        scene 11_205 with Dissolve(1)
        mc "Now I feel like they ripped me off with those two hundred dollars."
        er "No, it's actually a lot."
        mc "Yeah? How much does a model make an hour for a photo shoot?"
        er "Well, that depends on what kind of shoot it is and of course who the model is."
        scene 11_206 with Dissolve(1)
        er "If the model is famous and gets asked for a lot of shoots, especially in the fashion industry, the price goes up real quick."
        er "But if you just start out, it's around twenty dollars or so."
        mc "Twenty? That's it? And here I thought I should quit school and become a model."
        er "No, you don't! You finish school first!"
        mc "Haha. Yes, Mom."
        scene 11_207 with Dissolve(1)
        mc "Anyway. You must be hungry now. Shall we get something to eat? My treat."
        er "No, no. I'm not letting you pay after you helped me. Besides. I'm not hungry. But we can go somewhere you like. And I'll pay!"
        mc "I'm good too, actually."
        er "You don't have to hold back just because I'm not hungry."
        scene 11_208 with Dissolve(1)
        mc "I had a big bowl of cereal this morning and it's not even noon yet. But... I could use a coffee."
        er "Same. You want to go to a café, or take it to go?"
        mc "We've been sitting and standing still this whole time. Let's get some to go and walk along the pier or something."
        er "I like that. Let's cross here and get some at the Italian café."
    scene black with Dissolve(2)
    pause 2
    stop music fadeout 1.0
    play music "Sounds/Ocean.mp3" volume 0.5
    scene 11_209 with Dissolve(1)
    ""
    scene 11_210 with Dissolve(1)
    er "When does Emily open up her café?"
    mc "Hmm, I don't know. There were some setbacks and everything has been pushed to a later date."
    er "I hope it will be soon, so we can get our coffees there."
    mc "Yeah. What did you get anyway?"
    scene 11_211 with Dissolve(1)
    er "Here! Try it and have a guess."
    mc "Uhm, sure."
    mc "{i}(This has happened before...){/i}"
    scene 11_212 with Dissolve(1)
    mc "..."
    mc "{i}(No way.){/i}"
    er "Aaaand...?"
    scene 11_213 with Dissolve(1)
    mc "Heh..."
    er "What?"
    mc "Caramel macchiato!"
    er "Yeah! Good job. It's my favourite."
    scene 11_214 with Dissolve(1)
    mc "Now this is getting weird and a little scary."
    er "What?"
    mc "This whole scene and caramel macchiato being your favourite. Did you talk with Iris about us yesterday when you were shopping together?"
    er "A little bit. But mostly we were talking fashion. Why?"
    scene 11_215 with Dissolve(1)
    mc "Never mind."
    mc "{i}(They're even more similar than I thought. Minus the crazy.){/i}"
    mc "{i}(Is that the reason why I was so attracted to Iris right away?){/i}"
    mc "Want to try mine?"
    scene 11_216 with Dissolve(1)
    er "Eh... Okay, I have to be honest."
    er "I tried a little sip already when I got them. I'd never had cold brew before so I was curious how it tastes."
    mc "You cheater!"
    er "Sorry... I..."
    scene 11_217 with vpunch
    er "Aaah..."
    mc "..."
    scene 11_218 with Dissolve(1)
    er "Uh... Hey there... I have nothing for you."
    x "I'm so sorry!"
    scene 11_219 with Dissolve(1)
    bd "I'm training him to walk without a leash. But as you saw, it didn't work out as planned."
    bd "You know the rules. If you don't listen, it's back on the leash!"
    mc "Hey, Dylan."
    scene 11_220 with Dissolve(1)
    bd "Oh, it's you guys. Hey, Erynn, [mc]! How are you?"
    er "Hey, Dylan."
    mc "I didn't know you had a dog."
    bd "I've had him for nine months now."
    scene 11_221 with Dissolve(1)
    er "Hey, there. You scared me a bit. But you seem like a good boy, right? Or girl?"
    bd "He's a boy."
    er "What's his name?"
    bd "Kobe."
    er "Hey, Kobe! You're gorgeous!"
    scene 11_222 with Dissolve(1)
    mc "Oh, like the basketball player."
    mc "{i}(RIP Mamba!){/i}"
    bd "No, no. As in Kobe steak."
    mc "Haha, right."
    scene 11_223 with Dissolve(1)
    bd "Did you watch the game on Sunday?"
    mc "No, sadly I missed that one. But it must have been a great game."
    mc "Gatlin with another triple-double."
    bd "His twenty-second this season. I tell ya, he'll be the MVP this year."
    scene 11_224 with Dissolve(1)
    bd "Thursday's game against Eclipse will be interesting."
    mc "Gatlin versus Adler, yeah. Should've got tickets for that."
    bd "There's another great place where you can watch the game."
    mc "Haha. I see what you did there. But I'll probably do that."
    scene 11_225 with Dissolve(1)
    bd "Anyway. I'll leave you guys to it. Maybe see you on Thursday then."
    mc "Yeah. See you, Dylan."
    er "Bye, Kobe..."
    scene 11_226 with Dissolve(1)
    er "What a beautiful dog."
    mc "Yeah. Huskies are cool. You never had a pet, right?"
    er "No. Did you? I know you didn't have one here, but when you were living in Alvarado, maybe?"
    mc "Not there, either."
    scene 11_227 with Dissolve(1)
    er "Did you ever want one?"
    mc "I can't remember if I ever asked for a dog or another pet."
    if Alexis_Dating == False:
        mc "But since I didn't know anyone with a dog back then, I think that I wasn't really interested, either."
    else:
        $ Alexis_Week5_Photoshoot_DogPicture = True
        mc "But since I didn't know anyone with a dog back then, I think that..."
        er "Alexis did."
        scene 11_228 with Dissolve(1)
        mc "Alexis had a dog?"
        er "Two!"
        mc "Two? No, I didn't know that. Well, I didn't really know Lexi back then, either."
        er "Two big Dobermanns. Scary sight when you saw them for the first time. But they were actually so sweet."
        mc "{i}(That shows that Lexi and I still don't know much about each other.){/i}"
        scene 11_229 with Dissolve(1)
        er "She has this amazing picture where she looks like some kind of cartel leader and the dogs are protecting her."
        mc "I've gotta see that!"
        er "Ask her next time. I think she has it on her phone."
        mc "I will. What happened to them?"
        scene 11_230 with Dissolve(1)
        er "They passed away a few years ago."
        mc "Oh..."
        er "Yeah, she was heartbroken about that. Layla even more so."
    scene black with Dissolve(1)
    pause 2
    scene 11_231 with Dissolve(1)
    er "It's so hot again today."
    mc "It is. Why don't you take your hoodie off and put it in the bag?"
    er "..."
    scene 11_232 with Dissolve(1)
    er "I didn't even realise. You've been carrying this the whole time?"
    er "We should've put it in the car before we came here."
    er "I'm so sorry!"
    mc "Don't worry. It's not heavy."
    er "Still..."
    if Erynn_Week5_Tuesday_Photoshoot_Join == True:
        scene 11_233 with Dissolve(1)
        mc "..."
        er "That's so much better already!"
        scene 11_234 with Dissolve(1)
        mc "{i}(Here we go again.){/i}"
        mc "{i}(Why...? Why did I even look?){/i}"
        scene 11_235 with Dissolve(1)
        er "What?"
        mc "Hmm?"
        er "Did you say something?"
        mc "Uhm... No."
    else:
        pass
    scene 11_236 with Dissolve(1)
    er "I like coming here."
    mc "Why's that?"
    er "The smell of the ocean and hearing the waves crash below against the rocks."
    er "No. I don't know. It just feels nice."
    scene 11_237 with Dissolve(1)
    er "..."
    er "What are you doing?"
    mc "Sitting?"
    er "Not there you're not!"
    scene 11_238 with Dissolve(1)
    mc "Haha. Why not?"
    er "There's a sign that says it's not allowed, for starters!"
    er "And most importantly, it's dangerous!"
    er "If you fall, you'll hit the rocks, not the water."
    scene 11_239 with Dissolve(1)
    mc "Oh, come on. Live a little."
    er "..."
    er "Live a little? That's what Iris said to me yesterday when she wanted me to try on a skimpy bikini."
    mc "Haha, sounds like her."
    er "Now get off, please!"
    menu:
        "Get off":
            scene 11_240 with Dissolve(1)
            mc "Fine! Happy?"
            er "Yes, thanks."
            scene 11_241 with Dissolve(1)
            mc "Come here."
            mc "I've told you before to stop worrying so much about others and think of yourself first."
            er "I am... You're an exception though."
            er "And Lexi... And Mom... And Emily!"
            mc "Haha."
            scene 11_259 with Dissolve(1)
            mc "By the way. When can we see the pictures?"
        "Joke":
            scene 11_242 with Dissolve(1)
            mc "Aaah..."
            er "[mc]!"
            scene 11_243 with Dissolve(1)
            mc "Haha..."
            er "Are you fucking kidding me?"
            scene 11_244 with Dissolve(1)
            mc "Sorry, sorry, Erynn."
            mc "You were so serious and I just had to..."
            er "Not funny. NOT FUNNY!"
            er "Now get off or I'll push you over myself!"
            scene 11_245 with Dissolve(1)
            mc "There. Happy?"
            er "Don't do that to me. That was not funny!"
            mc "Haha. I'm sorry."
            scene 11_241 with Dissolve(1)
            mc "Come here."
            mc "I've told you before to stop worrying so much about others and think of yourself first."
            er "I am... You're an exception though."
            er "And Lexi... And Mom... And Emily!"
            mc "Haha."
            scene 11_259 with Dissolve(1)
            mc "By the way. When can we see the pictures?"
        "Invite her up":
            scene 11_246 with Dissolve(1)
            mc "Or you can get up here."
            er "What? No!"
            mc "Come on!"
            er "[mc]..."
            scene 11_247 with Dissolve(1)
            mc "Do you trust me?"
            er "Yes..."
            mc "I'll help you up."
            scene 11_248 with Dissolve(1)
            er "Don't let go."
            mc "I won't."
            scene 11_249 with Dissolve(1)
            mc "Why are you closing your eyes?"
            er "Because I'm scared."
            mc "The hardest part was getting up here."
            er "This was such a stupid idea."
            mc "{i}(She's shaking so much. This was probably a stupid idea.){/i}"
            scene 11_250 with Dissolve(1)
            mc "See! Not that bad, right?"
            er "..."
            mc "Want to turn around so we're facing the ocean? It's a nicer view."
            er "No!"
            mc "Haha."
            scene 11_251 with Dissolve(1)
            mc "Alright. I see you're uncomfortable."
            mc "I'll help you down again."
            er "Thanks."
            scene 11_252 with Dissolve(1)
            mc "On three!"
            mc "One... two... three!"
            scene 11_253 with Dissolve(1)
            er "Aaah... Haha."
            scene 11_254 with Dissolve(1)
            mc "Now you're laughing."
            er "Well, I like it up here."
            er "It's so much better. I like this view too!"
            if Erynn_LikeMC == True:
                scene 11_255 with Dissolve(1)
                mc "{i}(Same!){/i}"
                mc "{i}(Her nipples are hard again.){/i}"
                mc "{i}(I want to see them naked again. Not just see... Touch, squeeze, taste...){/i}"
                scene 11_256 with Dissolve(1)
                er "This feels familiar."
                mc "With one exception."
                er "That's not gonna happen here!"
                mc "I wish I had that picture. In fact, all of those pictures."
                scene 11_257 with Dissolve(1)
                er "..."
                mc "..."
                scene 11_258 with Dissolve(1)
                er "Thank you for helping me down."
                mc "{i}(For a second I thought we would...){/i}"
                mc "Sure."
                scene 11_259 with Dissolve(1)
                mc "Speaking about the pictures."
                mc "When can we see them?"
            else:
                scene 11_259 with Dissolve(1)
                mc "By the way. When can we see the pictures?"
    er "Once they're released in the magazine."
    mc "You won't see them before?"
    er "No."
    scene 11_260 with Dissolve(1)
    mc "Do you at least know which one will be featured?"
    er "No, they'll probably pick out three or four..."
    mc "Three or four? That's it? What happens to all the other ones."
    er "As of now, nothing."
    if Erynn_Week5_Tuesday_Photoshoot_Join == True:
        scene 11_261 with Dissolve(1)
        mc "What a waste. We should've asked for some copies."
        if Erynn_LikeMC == True:
            er "Hehe. We can always make our own pictures. Or recreate them."
            mc "..."
            mc "{i}(Recreate them? I wouldn't mind that. Especially the second part.){/i}"
        else:
            er "Hehe. We can always make our own pictures."
            mc "True."
    else:
        scene 11_261 with Dissolve(1)
        mc "What a waste. We should've asked for some copies."
        er "Hehe. We can always make our own pictures."
    scene 11_262 with Dissolve(1)
    er "*Stomach growling*"
    er "..."
    mc "I guess someone's finally hungry."
    scene 11_263 with Dissolve(1)
    mc "Let's go home, then. We can grab something to eat along the way."
    er "Mm-hmm."
    if Erynn_LikeMC == False:
        pass
    else:
        scene 11_264 with Dissolve(1)
        mc "Uh..."
        er "..."
        mc "Erynn?"
        er "Just for a moment."
        scene 11_265 with Dissolve(1)
        mc "..."
        mc "{i}(I can feel her heart beating fast again.){/i}"
        scene 11_266 with Dissolve(1)
        er "Thank you!"
        mc "You can hug me any time you want."
        er "I will. Also, thanks for today. You made this so much better."
        er "I feel so at ease and relaxed when I'm with you."
        scene 11_267 with Dissolve(1)
        er "Sometimes it feels like you're the one who's three years older, and not me."
        mc "I feel like that most of the time."
        scene 11_268 with Dissolve(1)
        er "HEY!"
        mc "Haha. See you're hitting me again. So mature!"
        er "Because you are so mature, right?"
        mc "Haha."
        if Erynn_Week5_Tuesday_SlapAss == True:
            scene 11_269 with Dissolve(1)
            mc "I've never hit you, for example."
            er "Bullshit!"
            mc "What? When did I ever?"
            er "This morning when you slapped my ass! And then the other day when..."
            mc "That's different. It's not hitting when you're enjoying it."
            scene 11_270 with Dissolve(1)
            er "..."
            er "Who says I enjoyed it?"
            mc "You trying to be angry while keeping your laughter in right now says it all."
            scene 11_271 with Dissolve(1)
            er "Idiot!"
            er "Let's go home before you say any more stupid stuff."
            mc "Haha. I bet you're still smiling."
            er "I'm not!"
            scene 11_272 with Dissolve(1)
            mc "..."
            mc "{i}(And then she does stuff like this!){/i}"
            scene 11_273 with vpunch
            er "Aaah..."
            scene 11_274 with Dissolve(1)
            er "See! I told you!"
            mc "You definitely asked for that."
            er "I did not! I just grabbed our coffee!"
            mc "Uh-huh."
        else:
            scene 11_275 with Dissolve(1)
            er "Let's go home before you say any more stupid stuff."
            mc "Haha."
    scene black with Dissolve(2)
    pause 2
    stop music fadeout 1.0
    play music ("Music/LoFi Indie 3.mp3", "Music/LoFi Indie 1.mp3", "Music/LoFi Indie 2.mp3") volume 0.2
    scene 11_276 with Dissolve(1)
    mc "Melissa not back yet? That must be one serious haircut."
    er "Haha. She has probably more than one appointment."
    mc "That makes more sense."
    scene 11_277 with Dissolve(1)
    mc "Here's your bag."
    er "Thank you for carrying it for me."
    mc "No problem."
    scene 11_278 with Dissolve(1)
    er "What are your plans for the rest of the day?"
    mc "Hmm... I don't know yet."
    if Layla_Dating == True:
        mc "Layla wanted to have a hot tub party at her place."
        er "That's fun."
        mc "Yeah, but I haven't heard anything from her yet, so I don't know if that's going on or not."
        mc "But first I'll nap a bit, probably."
    else:
        if MC_Bike == True:
            mc "Maybe go ride on the bike. Check out some streets I can race a bit."
            mc "But first I'll nap a bit, probably."
        else:
            mc "Probably just have a little nap first and then I'll see."
    mc "How about you?"
    scene 11_279 with Dissolve(1)
    if Erynn_LikeMC == True:
        er "I don't know either. I have nothing planned for the rest of the day."
        er "But a nap doesn't sound bad. Can I join you?"
        mc "Uh... Sure."
        scene 11_282 with Dissolve(1)
        er "Kay. Just give me a minute. I'll just put my stuff inside."
        mc "Is it going to be the same kind of minute as this morning?"
        er "It wasn't that long."
        mc "Twenty minutes!"
        er "Heh, sorry. I'll be quick this time."
        mc "..."
        scene 11_283 with Dissolve(1)
        mc "{i}(Maybe it wasn't a good idea to let her come over.){/i}"
        mc "{i}(Now she won't just be in my head all day but...){/i}"
        mc "{i}(Fuck! Stop thinking about it! It was just a photo shoot!){/i}"
        mc "{i}(A photo shoot where she had to be naked...){/i}"
        scene 11_284 with Dissolve(1)
        mc "Oh... You're back already."
        er "I told you I was gonna be quick."
        jump Week5_Tuesday_Room_Erynn
    else:
        er "I don't know either. I have nothing planned for the rest of the day."
        er "But a nap doesn't sound bad."
        scene 11_280 with Dissolve(1)
        er "Well. Thank you very much for joining me today."
        mc "It surely was an experience. Call me anytime you need someone to tag along."
        if Alexis_Dating == False:
            if Alexis_SecretPath == False:
                er "Hehe, I will. Bye, [mc]."
                mc "Later, Erynn."
                jump Week5_Tuesday_Room
            else:
                er "We'll see each other tomorrow then?"
                mc "Tomorrow?"
                scene 11_281 with Dissolve(1)
                er "Yeah. The beach with Alexis and Iris."
                mc "Right. Yeah. I'll see you then."
                er "I'll let you know once I know the time."
                mc "Alright. See you then, Erynn."
                er "Bye, [mc]."
                jump Week5_Tuesday_Room
        else:
            if Alexis_Week5_Monday_Date_Cancel == True:
                er "Hehe, I will. Bye, [mc]."
                mc "Later, Erynn."
                jump Week5_Tuesday_Room
            else:
                er "We'll see each other tomorrow then?"
                mc "Tomorrow?"
                scene 11_281 with Dissolve(1)
                er "Yeah. The beach with Alexis and Iris."
                mc "Right. Yeah. I'll see you then."
                er "I'll let you know once I know the time."
                mc "Alright. See you then, Erynn."
                er "Bye, [mc]."
                jump Week5_Tuesday_Room_Alexis

label Week5_Tuesday_Room_Erynn:
    if _in_replay:
        $ Alexis_Dating = False
        $ Nikki_Girlfriend = False
        $ Cara_Girlfriend = False
        $ Erynn_Week5_Tuesday_SlapAss = True
        $ Alexis_Week5_Monday_Date_Cancel = False
    scene black with Dissolve(1)
    pause 2
    stop music fadeout 1.0
    play music ("Music/LoFi Indie 2.mp3", "Music/LoFi Indie 1.mp3", "Music/LoFi Indie 3.mp3") volume 0.2
    scene 11_285 with Dissolve(1)
    er "What are we going to do now?"
    mc "Nap!"
    er "Oh... You were serious about that."
    scene 11_286 with Dissolve(1)
    er "That's fine with me!"
    mc "..."
    scene 11_287 with Dissolve(1)
    mc "{i}(Seriously... Again?){/i}"
    scene 11_288 with Dissolve(1)
    mc "{i}(Why did I look again?){/i}"
    mc "{i}(I have to take care of it now... The whole freakin' day I've been running around like this.){/i}"
    scene 11_289 with Dissolve(1)
    er "Where are you going?"
    mc "Uh... Shower..."
    mc "I'm a little sweaty from... walking in the sun earlier. Need to switch clothes."
    mc "I'll be right back."
    er "Alright."
    scene black with Dissolve(1)
    pause 2
    scene 11_290 with Dissolve(1)
    mc "{i}(It's the same feeling as years ago...){/i}"
    mc "{i}(I'm still in love with her! Even more so now.){/i}"
    mc "{i}(I thought we could be friends like we used to be... But I want so much more.){/i}"
    mc "{i}(Every time I see her, my feelings for her grow.){/i}"
    mc "{i}(I don't know if I can keep doing this without... Fuck!){/i}"
    if Alexis_Dating == True:
        scene 11_291 with Dissolve(1)
        mc "{i}(I'm with Lexi. I love Lexi. She's absolutely amazing.){/i}"
        mc "{i}(We have so much fun together and grow closer every day.){/i}"
        mc "{i}(But...){/i}"
        mc "{i}(But why is it different when I'm with Erynn?){/i}"
        mc "{i}(Is it just desire... Fuck... That stupid perfume ad...){/i}"
    else:
        if Nikki_Girlfriend == True:
            mc "{i}(I'm with Nikki. I love Nikki. She's absolutely amazing.){/i}"
            mc "{i}(We have so much fun together and grow closer every time we see each other.){/i}"
            mc "{i}(But...){/i}"
            mc "{i}(But why is it different when I'm with Erynn?){/i}"
            mc "{i}(Is it just desire... Fuck... That stupid perfume ad...){/i}"
        else:
            if Cara_Girlfriend == True:
                mc "{i}(I'm with Cara. I love Cara. She's absolutely amazing.){/i}"
                mc "{i}(We have so much fun together and grow closer every time we see each other.){/i}"
                mc "{i}(But...){/i}"
                mc "{i}(But why is it different when I'm with Erynn?){/i}"
                mc "{i}(Is it just desire... Fuck... That stupid perfume ad...){/i}"
            else:
                pass
    scene 11_292 with Dissolve(1)
    mc "*Sigh...*"
    mc "{i}(I don't know what to do.){/i}"
    mc "{i}(And I can't get that photo shoot out of my head...){/i}"
    mc "{i}(Not the photo shoot... Just... Erynn...){/i}"
    scene 11_137 with Dissolve(1)
    ph "Show me what you desire most!"
    mc "..."
    scene 11_293 with Dissolve(1)
    mc "*Heavy breathing*"
    mc "Erynn... Erynn..."
    scene 11_181 with Dissolve(1)
    mc "Erynn!"
    scene 11_234 with Dissolve(1)
    mc "Erynn..."
    scene 11_294 with vpunch
    pause 2
    scene 11_294 with vpunch
    mc "Erynn... Ahhh..."
    scene 11_295 with Dissolve(1)
    mc "Fuuuck..."
    mc "*Heavy breathing*"
    mc "{i}(I can't remember the last time I was this horny...){/i}"
    mc "{i}(Let's hope I don't keep running around with a boner the whole day after this.){/i}"
    scene 11_296 with Dissolve(1)
    mc "{i}(OH, COME ON!){/i}"
    mc "..."
    mc "What are you doing?"
    scene 11_297 with Dissolve(1)
    er "[mc]! You scared me!"
    er "Don't sneak up on me like that!"
    mc "Sneak? I just walked normally into the room."
    mc "Snooping around?"
    scene 11_298 with Dissolve(1)
    er "What? No! I was just... looking."
    mc "Uh-huh. Looking with your hands."
    er "..."
    mc "Caught in the act, Snoopy!"
    er "No! I wasn't... And don't call me Snoopy!"
    scene 11_299 with vpunch
    er "Aaah! [mc]!"
    if Erynn_Week5_Tuesday_SlapAss == True:
        mc "You so deserved that one."
        er "..."
    else:
        pass
    scene 11_300 with Dissolve(1)
    er "That was so hard!"
    er "You're going to regret it this time."
    mc "Haha. Make me!"
    scene 11_301 with Dissolve(1)
    er "I've got you now with the bear hug technique. I learned it from Emily this morning!"
    mc "Because that worked so well..."
    mc "{i}(If you knew what I did to you in the shower, you wouldn't be this close to me right now.){/i}"
    mc "It's so cute you keep on trying. But it's just not gonna work, Erynn."
    er "Try to get out then!"
    scene 11_302 with Dissolve(1)
    mc "{i}(This keeps on happening today. Erynn pressing her boobs against my chest...){/i}"
    if Nikki_Girlfriend == False:
        pass
    else:
        mc "{i}(If this was Nikki, I'd probably have a hard time getting out.){/i}"
    er "See! You can't!"
    mc "{i}(I wouldn't mind being like this for longer, but...){/i}"
    mc "You asked for it!"
    scene 11_303 with Dissolve(1)
    er "..."
    er "Hey!"
    scene 11_304 with Dissolve(1)
    er "Ahh... [mc]! You..."
    er "That's so unfair!"
    mc "How is this unfair now? You said to try to get out..."
    er "Not like this! You wouldn't do this to Emily!"
    mc "First of all, you're not Mom. And secondly, all is fair in love and war!"
    scene 11_305 with Dissolve(1)
    er "It's not gonna stop me this time!"
    er "Instead I'll do this and just tighten the grip."
    mc "..."
    er "What will you do now?"
    menu:
        "Throw her on the bed":
            scene 11_319 with Dissolve(1)
            mc "How about this?"
            er "Aaah..."
            scene 11_320 with Dissolve(1)
            er "Haha. That's so unfair."
            mc "Now it's unfair again? Seems like every time I'm winning, it's unfair."
            er "I see you're finally getting it."
            scene 11_321 with Dissolve(1)
            mc "..."
            mc "{i}(Fuck, she's pretty!){/i}"
            mc "{i}(I need to think about something else before I...){/i}"
            if Alexis_End == False:
                scene 11_322 with Dissolve(1)
                mc "Let's take this nap then."
                er "Yeah..."
            else:
                scene 11_323 with Dissolve(1)
                mc "Let's take this nap then."
                er "..."
            scene 11_324 with Dissolve(1)
            er "Don't wake me for at least an hour."
            mc "Same goes for you."
            if Alexis_Dating == True:
                if Alexis_Week5_Monday_Date_Cancel == False:
                    scene black with Dissolve(1)
                    pause 2
                    scene 11_325 with Dissolve(1)
                    play sound "Sounds/Phone_Vibrate.mp3"
                    n "*Bzzzt. Bzzzt*"
                    er "..."
                    n "*Bzzzt. Bzzzt*"
                    er "Pick up or I will!"
                    mc "Go ahead..."
                    scene 11_326 with Dissolve(1)
                    play sound "Sounds/Phone_Vibrate.mp3"
                    n "*Bzzzt. Bzzzt*"
                    er "Oh..."
                    scene 11_327 with Dissolve(1)
                    er "Hey, girly."
                    a "Uhm... Hey?"
                    a "Did I call the wrong number? I was about to call [mc]."
                    er "No, this is his phone. I'm at his place."
                    scene 11_328 with Dissolve(1)
                    a "Ah, okay."
                    a "How was the photo shoot?"
                    er "Uhm... It was... good. I'll tell you later."
                    a "Alright."
                    scene 11_329 with Dissolve(1)
                    mc "Who is it?"
                    er "Your girlfriend!"
                    mc "Say hi to her from me."
                    scene 11_330 with Dissolve(1)
                    er "[mc] says hi."
                    a "Haha, what?"
                    a "Give me that idiot."
                    scene 11_331 with Dissolve(1)
                    er "Here. You talk to her."
                    er "I'll be leaving then. Thanks again for today."
                    scene 11_355 with Dissolve(1)
                    mc "Sure. See you later, Erynn."
                    er "Bye, [mc]."
                    scene 11_332 with Dissolve(1)
                    mc "Hey."
                    a "Hi..."
                    mc "Haha. Sorry about that. How are you?"
                    a "I'm good. How are you? How was the photo shoot?"
                    scene 11_333 with Dissolve(1)
                    mc "It was uh... interesting..."
                    a "Did something happen? Erynn was vague, too."
                    mc "We'll tell you later. Nothing to worry about."
                    mc "{i}(I hope...){/i}"
                    a "Hmm..."
                    scene 11_334 with Dissolve(1)
                    a "Anyway. Erynn probably told you this already. She, Iris and I are going to the beach, either tomorrow or Thursday."
                    a "And we were wondering if you wanted to join."
                    if Erynn_Week5_Tuesday_Photoshoot_Join == True:
                        mc "{i}(Shit! Should I even go now after what happened earlier? But I told Erynn already that I'll go. Fuck!){/i}"
                    else:
                        pass
                    mc "Yeah. I'll join you. It'll be fun."
                    a "Great. I didn't want to go with Iris and Erynn alone."
                    scene 11_335 with Dissolve(1)
                    mc "Why?"
                    a "This stays between us. But I think Iris has a thing for Erynn."
                    mc "{i}(I know...){/i}"
                    mc "Does she?"
                    a "Uh-huh."
                    scene 11_336 with Dissolve(1)
                    mc "What makes you say that?"
                    a "The way she talks to her. Always flirty."
                    a "And then the way she looks at her."
                    mc "Lustful?"
                    a "[mc]! But yeah."
                    mc "Haha."
                    scene 11_337 with Dissolve(1)
                    mc "{i}(Should I tell her I know?){/i}"
                    mc "{i}(Nah... This is just too much fun.){/i}"
                    scene 11_338 with Dissolve(1)
                    a "What are you doing the rest of the day?"
                    mc "I don't know yet. Can I come over? Or maybe you can come here?"
                    a "I want to, but I have to get ready for work soon."
                    mc "Ah, you're working today. Maybe I'll come by later, then."
                    scene 11_339 with Dissolve(1)
                    a "Are you working at the restaurant this week?"
                    mc "I am. I think Thursday."
                    a "So it would be better to go to the beach tomorrow, or else you won't be able to come."
                    mc "It depends on the hours. I'll make sure I have time whatever day it is."
                    a "Okay."
                    scene 11_340 with Dissolve(1)
                    n "*Knock-knock*"
                    la "Lex, can I come in?"
                    a "Give me a minute, [mc]."
                    a "Yeah."
                    scene 11_341 with Dissolve(1)
                    la "Hey."
                    a "Hey. What's up?"
                    la "Question."
                    scene 11_342 with Dissolve(1)
                    la "Are you gonna be here this evening?"
                    a "No, I'm working today. Why?"
                    la "I'm having a hot tub party."
                    a "Oh, that's fun. But don't worry. I won't interrupt you guys."
                    scene 11_343 with Dissolve(1)
                    la "No, you can join us after work if you want."
                    a "Thanks. Maybe I will. Who's coming? Elena?"
                    la "Yes, Elena. Sienna, Kenz. Maybe Valeria. She wasn't sure yet if she'll make it."
                    a "Only girls?"
                    la "Why? You want there to be boys?"
                    scene 11_344 with Dissolve(1)
                    a "Not for me, for you!"
                    la "..."
                    la "So just join us after work if you want."
                    a "Thanks, Lays."
                    la "Oh and Elena will stay the night. Just so you know."
                    a "Alright."
                    scene 11_345 with Dissolve(1)
                    a "I'm back."
                    mc "Did I hear something about a hot tub party?"
                    a "Haha. Of course you heard that."
                    a "But I have bad news for you. It's girls only."
                    scene 11_346 with Dissolve(1)
                    mc "Damn. I knew I should've bought that long-haired wig."
                    a "Haha."
                    mc "Or I can use yours! Pretend to be Adriana."
                    scene 11_347 with Dissolve(1)
                    a "Haha. And get slapped on your ass by my dad who mistakes you for her."
                    mc "Thanks for reminding me!"
                    a "Haha. I'll never let you forget!"
                    mc "Never mind. Go have fun at your hot tub party!"
                    scene 11_348 with Dissolve(1)
                    a "Hey. Next time you're here, we can have our own little hot tub party."
                    a "Just the two of us."
                    mc "I like the sound of that."
                    n "*Knock-knock*"
                    scene 11_349 with Dissolve(1)
                    am "Alexis?"
                    a "Sorry. Give me another minute."
                    a "Yeah?"
                    scene 11_350 with Dissolve(1)
                    am "Hey. I'm leaving now. If you want to come with, get ready."
                    a "I'll be right there. Five minutes."
                    scene 11_351 with Dissolve(1)
                    a "Sorry, I've gotta go."
                    a "I'll call you once I know more about the beach date."
                    mc "Alright. Have fun today. Bye, Lexi."
                    a "Thanks, you too. Bye, [mc]. Love you."
                    menu:
                        "Say it back[KoGa3AutoWTChange1]{size=-4}(Alexis Points+2) {/size} {/color}":
                            $ Alexis_Points += 2
                            # Alexis (46)
                            mc "Love you too."
                        "Hang up":
                            pass
                    $ renpy.end_replay()
                    jump Week5_Tuesday_Room
                else:
                    scene black with Dissolve(1)
                    pause 2
                    scene 11_325 with Dissolve(1)
                    play sound "Sounds/Phone_Vibrate.mp3"
                    n "*Bzzzt. Bzzzt*"
                    er "..."
                    n "*Bzzzt. Bzzzt*"
                    scene 11_352 with Dissolve(1)
                    er "Erynn Orlandi."
                    er "Yes..."
                    er "I have the documents on my laptop."
                    scene 11_353 with Dissolve(1)
                    er "I'll be on my way home now and I'll send them over."
                    er "Okay. Yes."
                    er "Bye."
                    scene 11_354 with Dissolve(1)
                    er "[mc]?"
                    mc "Hmm?"
                    er "I have to go. I have to email some documents."
                    mc "Do you want me to come with?"
                    er "Thanks, but it's fine."
                    scene 11_355 with Dissolve(1)
                    er "I'll call you later, okay."
                    er "And thanks again for today."
                    mc "Anytime, Erynn."
                    er "Bye-bye."
                    mc "Later."
                    $ renpy.end_replay()
                    jump Week5_Tuesday_Room
            else:
                scene black with Dissolve(1)
                pause 2
                scene 11_325 with Dissolve(1)
                play sound "Sounds/Phone_Vibrate.mp3"
                n "*Bzzzt. Bzzzt*"
                er "..."
                n "*Bzzzt. Bzzzt*"
                scene 11_352 with Dissolve(1)
                er "Erynn Orlandi."
                er "Yes..."
                er "I have the documents on my laptop."
                scene 11_353 with Dissolve(1)
                er "I'll be on my way home now and I'll send them over."
                er "Okay. Yes."
                er "Bye."
                scene 11_354 with Dissolve(1)
                er "[mc]?"
                mc "Hmm?"
                er "I have to go. I have to email some documents."
                mc "Do you want me to come with?"
                er "Thanks, but it's fine."
                scene 11_355 with Dissolve(1)
                er "I'll call you later, okay."
                er "And thanks again for today."
                mc "Anytime, Erynn."
                er "Bye-bye."
                mc "Later."
                $ renpy.end_replay()
                jump Week5_Tuesday_Room
        "Kiss her[KoGa3AutoWTChange1]{size=-4}(Erynn Week5 Tuesday Room Kiss) {/size} {/color}":
            $ Erynn_Week5_Tuesday_Room_Kiss = True
            scene 11_306 with Dissolve(1)
            er "..."
            if Alexis_Dating == True:
                scene 11_307 with vpunch
                er "What are you doing?"
                mc "..."
                er "You're with Lexi! You can't..."
                scene 11_308 with Dissolve(1)
                mc "Uh... I..."
                mc "{i}(Fuck. I messed up big time.){/i}"
                mc "{i}(Why did I even kiss her? What did I expect would happen?){/i}"
                mc "{i}(What did I want to happen?){/i}"
                scene 11_309 with Dissolve(1)
                mc "Uhm... Sorry, Erynn. I don't know what happened."
                mc "I... I wasn't really thinking. I was just caught up in the moment and... Sorry."
                er "..."
                er "I'm sorry too. I'm not blameless either. I was flirting as well and... Yeah..."
                scene 11_310 with Dissolve(1)
                er "Please, don't tell Lexi."
                mc "What?"
                er "This will just... Please don't tell her."
                er "As you said. We were caught up in the moment. I guess emotions were high after that photo shoot and... You know..."
                er "Let's just forget about this. It never happened."
                mc "Yeah..."
                scene 11_311 with Dissolve(1)
                er "I think I'd better leave for today."
                mc "Sorry. I didn't want to make it awkward between us."
                er "It's not. It was just an emotional day, and everything will be back to normal tomorrow."
                mc "{i}(What is normal...?){/i}"
                scene 11_312 with Dissolve(1)
                mc "Uh..."
                er "..."
                scene 11_313 with Dissolve(1)
                er "Haha. Now that is awkward!"
                mc "Haha."
                er "Come here!"
                scene 11_314 with Dissolve(1)
                er "Thank you very much for today, [mc]. For the photo shoot and just being there for me in general."
                if Alexis_Week5_Monday_Date_Cancel == True:
                    er "I'll see you next time, then."
                    scene 11_315 with Dissolve(1)
                    er "Bye, [mc]."
                    mc "Later, Erynn..."
                    scene 11_316 with Dissolve(1)
                    mc "{i}(Was this really only because of all the things that happened today?){/i}"
                    mc "{i}(Maybe Erynn was right, and tomorrow everything will be normal again.){/i}"
                    scene 11_317 with Dissolve(1)
                    ""
                    scene 11_318 with Dissolve(1)
                    er "..."
                    $ renpy.end_replay()
                    jump Week5_Tuesday_Room
                else:
                    er "I'll see you tomorrow, then?"
                    mc "Tomorrow?"
                    er "Or Thursday. The beach."
                    mc "Right. You told me Alexis will call me later to let me know."
                    scene 11_315 with Dissolve(1)
                    er "Bye, [mc]."
                    mc "Later, Erynn..."
                    scene 11_316 with Dissolve(1)
                    mc "{i}(Was this really only because of all the things that happened today?){/i}"
                    mc "{i}(Maybe Erynn was right, and tomorrow everything will be normal again.){/i}"
                    scene 11_317 with Dissolve(1)
                    ""
                    scene 11_318 with Dissolve(1)
                    er "..."
                    $ renpy.end_replay()
                    jump Week5_Tuesday_Room_Alexis
            else:
                scene 11_307 with Dissolve(1)
                er "What are you doing?"
                mc "..."
                scene 11_308 with Dissolve(1)
                mc "Uh... I..."
                mc "{i}(Fuck. Did I read this wrong?){/i}"
                mc "{i}(Why did I even kiss her? What did I expect would happen?){/i}"
                mc "{i}(What did I want to happen?){/i}"
                scene 11_360 with Dissolve(1)
                mc "Uhm... Sorry, Erynn. I don't know what happened."
                mc "I... I wasn't really thinking. I was just caught up in the moment and... Sorry."
                er "..."
                scene 11_361 with Dissolve(1)
                mc "{i}(Now this is going to be awkward...){/i}"
                mc "{i}(Should I say something? Apologise again?){/i}"
                scene 11_362 with Dissolve(1)
                mc "..."
                scene 11_363 with Dissolve(1)
                mc "Erynn...?"
                scene 11_364 with Dissolve(1)
                mc "{i}(Okay?){/i}"
                mc "{i}(What's happening right now?){/i}"
                scene 11_365 with Dissolve(1)
                mc "{i}(Erynn is kissing me!){/i}"
                mc "{i}(I'm not dreaming, am I?){/i}"
                scene 11_366 with Dissolve(1)
                mc "{i}(Nope...){/i}"
                mc "{i}(This definitely feels real!){/i}"
                scene 11_367 with Dissolve(1)
                ""
                scene 11_368 with Dissolve(1)
                mc "{i}(I want this.){/i}"
                mc "{i}(I want this so much!){/i}"
                scene 11_369 with Dissolve(1)
                er "Mmm..."
                scene 11_370 with Dissolve(1)
                er "Ahh..."
                mc "Sorry. Too much?"
                er "*Shakes head*"
                scene 11_371 with Dissolve(1)
                er "Go ahead."
                mc "{i}(Is she serious?){/i}"
                scene 11_372 with Dissolve(1)
                er "Ahhh..."
                mc "{i}(They feel so good!){/i}"
                scene 11_373 with Dissolve(1)
                mc "{i}(A perfect handful.){/i}"
                mc "{i}(More than a handful, actually.){/i}"
                scene 11_374 with Dissolve(1)
                er "Mmm..."
                scene 11_375 with Dissolve(1)
                mc "{i}(I have to see them again.){/i}"
                mc "{i}(And this time. I want to do more...){/i}"
                er "..."
                scene 11_376 with Dissolve(1)
                mc "Why are you shy, now? I saw them before at the shoot."
                er "That's different. That's completely different."
                mc "How is that different?"
                er "Those were for pictures, now there's a different intention."
                scene 11_377 with Dissolve(1)
                mc "There wasn't a different intention. Just not the right place."
                er "..."
                mc "Can I see them again, please?"
                mc "They're beautiful!"
                er "*Nods*"
                scene 11_378 with Dissolve(1)
                mc "..."
                scene black with Dissolve(1)
                transform moveup:
                    xalign 0.5 yalign 1.0
                    linear 5.0 yalign 0.0
                show 11_379 at moveup
                pause 3
                mc "{i}(Fuck me...){/i}"
                mc "You are so gorgeous, Erynn!"
                scene 11_380 with Dissolve(1)
                ""
                scene 11_381 with Dissolve(1)
                mc "{i}(Such beautiful boobs!){/i}"
                scene 11_382 with Dissolve(1)
                mc "{i}(Does she like this?){/i}"
                mc "{i}(I can't read her expression.){/i}"
                mc "{i}(I don't want to wait any longer. I have to...){/i}"
                scene 11_383 with Dissolve(1)
                er "..."
                scene 11_384 with Dissolve(1)
                er "Ahh... [mc]..."
                scene 11_385 with Dissolve(1)
                mc "{i}(Her nipples are so hard.){/i}"
                scene 11_386 with Dissolve(1)
                mc "{i}(I could do this for hours.){/i}"
                mc "{i}(These boobs are made to be sucked!){/i}"
                scene 11_387 with Dissolve(1)
                ""
                scene 11_388 with Dissolve(1)
                er "..."
                mc "{i}(She's taking her shirt off?){/i}"
                scene 11_389 with Dissolve(1)
                mc "{i}(She's doing more than just taking her shirt off...){/i}"
                scene black with Dissolve(1)
                transform moveup:
                    xalign 0.5 yalign 1.0
                    linear 5.0 yalign 0.0
                show 11_390 at moveup
                pause 3
                mc "{i}(Are we really?){/i}"
                mc "{i}(This day is getting better by the second.){/i}"
                scene 11_391 with Dissolve(1)
                mc "{i}(I'm getting crazy here.){/i}"
                mc "{i}(I can't hold back my excitement.){/i}"
                mc "{i}(I'm so fucking hard again.){/i}"
                scene black with Dissolve(1)
                transform moveup:
                    xalign 0.5 yalign 1.0
                    linear 5.0 yalign 0.0
                show 11_392 at moveup
                pause 3
                mc "{i}(Holy shit!){/i}"
                mc "{i}(This can't be real... This is too good to be true...){/i}"
                scene 11_393 with Dissolve(1)
                mc "Come here."
                scene 11_394 with Dissolve(1)
                mc "Your body is insane, Erynn!"
                scene 11_395 with Dissolve(1)
                mc "Can you turn around?"
                er "..."
                er "Why?"
                mc "I want to see everything."
                scene 11_396 with vpunch
                er "Aaah..."
                er "I knew it!"
                er "That's why I hesitated."
                mc "Last time. I promise. For today. Maybe."
                er "..."
                scene 11_397 with Dissolve(1)
                er "Aahaha. [mc]..."
                scene 11_398 with Dissolve(1)
                er "Aaah..."
                er "I'm getting dizzy!"
                mc "Haha."
                scene 11_399 with Dissolve(1)
                er "That was fun."
                er "And you're strong!"
                er "I realised that when you picked me up at the photo shoot so easily."
                mc "You give me lots of energy!"
                scene 11_400 with Dissolve(1)
                mc "Still the prettiest girl I know!"
                er "..."
                scene 11_401 with Dissolve(1)
                ""
                scene 11_402 with Dissolve(1)
                mc "You're mine now!"
                scene 11_403 with Dissolve(1)
                er "Ahhh..."
                scene 11_404 with Dissolve(1)
                mc "{i}(How far can I go with her?){/i}"
                mc "{i}(I don't know if I'll be able to stop.){/i}"
                scene 11_405 with Dissolve(1)
                mc "Do you like it when I play with your boobs?"
                er "*Nods*"
                scene 11_406 with Dissolve(1)
                er "Haha... That tickles!"
                scene 11_407 with Dissolve(1)
                mc "{i}(I can't get enough of them.){/i}"
                scene 11_408 with Dissolve(1)
                mc "{i}(She's getting into it now, too.){/i}"
                mc "{i}(She's squeezing her own boob.){/i}"
                scene 11_409 with Dissolve(1)
                ""
                scene 11_410 with Dissolve(1)
                mc "{i}(Is she touching herself?){/i}"
                scene 11_411 with Dissolve(1)
                er "*Moaning*"
                mc "{i}(This is so hot!){/i}"
                mc "{i}(Can I...?){/i}"
                scene 11_412 with Dissolve(1)
                er "..."
                mc "{i}(That just made her twitch.){/i}"
                mc "{i}(I think she didn't even realise she was doing it herself.){/i}"
                scene 11_413 with Dissolve(1)
                mc "{i}(She looks so nervous now.){/i}"
                mc "Are you comfortable with that?"
                er "..."
                er "*Nods*"
                mc "If not, tell me, okay? We can stop at any time."
                er "*Nods*"
                scene 11_414 with Dissolve(1)
                mc "{i}(I'm touching her...){/i}"
                scene 11_415 with Dissolve(1)
                mc "{i}(Her panties are soaked already.){/i}"
                mc "{i}(And my boxers are full of precum...){/i}"
                scene 11_416 with Dissolve(1)
                er "*Moaning*"
                scene 11_417 with Dissolve(1)
                ""
                scene 11_418 with Dissolve(1)
                mc "{i}(I've never seen her like this.){/i}"
                mc "{i}(I'm slowly circling her clit.){/i}"
                mc "{i}(I wanna make her cum!){/i}"
                scene 11_419 with Dissolve(1)
                er "Ahhh... [mc]..."
                er "Mmm..."
                scene 11_420 with Dissolve(1)
                er "Nggh..."
                mc "{i}(I think she just did...){/i}"
                mc "{i}(No, she definitely did!){/i}"
                scene 11_421 with Dissolve(1)
                ""
                scene black with Dissolve(1)
                pause 2
                scene 11_422 with Dissolve(1)
                er "*Heavy breathing*"
                er "Give me a second."
                mc "Heh. You okay?"
                er "Mm-hmm."
                scene 11_423 with Dissolve(1)
                mc "You're still shaking."
                er "No. That's because... This was... The first time that..."
                scene 11_424 with Dissolve(1)
                mc "What? You had an orgasm? You don't masturbate?"
                er "I do, but..."
                scene 11_425 with Dissolve(1)
                er "Why are you asking me that? That's so embarrassing!"
                er "And why did I even answer you...?"
                mc "It's nothing to be embarrassed about. I do, too."
                er "I don't wanna know!"
                mc "Haha."
                scene 11_426 with Dissolve(1)
                er "..."
                scene 11_427 with Dissolve(1)
                er "What I meant was... It was... It was the first time someone else did it to me."
                mc "{i}(I'm the first to give her an orgasm?){/i}"
                mc "{i}(Take that Zane. You fucking loser!){/i}"
                mc "{i}(Still wish I could've been her first for that, too...){/i}"
                mc "Did you enjoy it?"
                er "*Nods*"
                scene 11_428 with Dissolve(1)
                er "..."
                mc "Erynn?"
                scene 11_429 with Dissolve(1)
                er "I just realised what happened and what we... What we did."
                mc "Haha. You just realised?"
                mc "Did you think you were dreaming or something?"
                er "No..."
                scene 11_430 with Dissolve(1)
                er "But everything felt so surreal. Too good to be true."
                er "It started with you joining the photo shoot and me being in your arms..."
                er "And then..."
                er "How did we even end up here?"
                mc "{i}(I guess I'm not the only one who thought this was a dream...){/i}"
                scene 11_431 with Dissolve(1)
                mc "The whole day felt surreal for me, too. But I really enjoyed it."
                mc "Do you regret it?"
                scene 11_432 with Dissolve(1)
                er "No! No, [mc]. Of course not."
                er "I wanted... Want this."
                er "I just... *Sigh* I don't know. I can't explain."
                er "I'm happy. I haven't been happy and had this much fun the whole day for a long time."
                scene 11_433 with Dissolve(1)
                er "I want to do... You know... With you."
                er "But..."
                mc "I understand. We have time, Erynn. No need to rush anything."
                mc "{i}(Just doing this with me must have been huge for her.){/i}"
                mc "{i}(I'm happy she's slowly trusting me more and more to be able to be this comfortable around me.){/i}"
                scene 11_434 with Dissolve(1)
                er "Thanks."
                mc "{i}(I'll wait for you as long as it takes, Erynn.){/i}"
                mc "{i}(Even though I wish we could've gone all the way.){/i}"
                mc "{i}(I guess I'll have another date with the shower later.){/i}"
                scene black with Dissolve(1)
                pause 2
                scene 11_435 with Dissolve(1)
                er "I like this."
                mc "Same."
                er "Let's stay like this for a while."
                scene 11_436 with Dissolve(1)
                mc "Naked? Sure!"
                er "That's not what I mean..."
                mc "I like seeing you naked, though. You're gorgeous."
                er "..."
                scene 11_437 with Dissolve(1)
                ""
                scene 11_438 with Dissolve(1)
                er "Hey."
                mc "Hmm?"
                er "I have some questions."
                mc "Haha. Of course you do. Go ahead."
                er "But they're a little... Uhm... Like, personal."
                mc "I don't mind."
                scene 11_439 with Dissolve(1)
                er "Uhm... When you... You know... Do the thing..."
                mc "Do the thing?"
                er "Yeah... Uh... Masturbate..."
                mc "That kind of personal? Okay."
                er "Too much?"
                mc "Nah, it's fine. What's your question?"
                scene 11_440 with Dissolve(1)
                er "So, when you... Do you think of someone, or do you watch something?"
                mc "Both. Sometimes I watch porn or look at a picture, other times I just imagine someone."
                er "Hmm."
                scene 11_441 with Dissolve(1)
                er "Do you... Did you ever think of me when...?"
                mc "{i}(I love this cute side of her. I don't see it that often.){/i}"
                mc "..."
                mc "I do. In fact, I did today."
                scene 11_442 with Dissolve(1)
                er "What...? [mc]!"
                mc "Haha. You asked!"
                er "When? This morning?"
                er "Is that why you were naked in bed?"
                mc "No. Earlier in the shower."
                scene 11_443 with Dissolve(1)
                er "Earlier? You mean after we came back from the photo shoot?"
                mc "Yeah."
                er "What? You did? Then? Why?"
                mc "Seriously? Why? I think you can figure out why. I'm looking right at it."
                mc "And if I'm completely honest. I'll do it again later."
                scene 11_444 with Dissolve(1)
                er "..."
                mc "Why are you looking so happy?"
                er "I'm not. I just thought I'd be weirded out by that, but I'm not."
                mc "*Shakes head*"
                scene 11_445 with Dissolve(1)
                er "When was the first time you..."
                mc "Around twelve."
                er "I meant when you thought of... me and..."
                mc "Also twelve."
                scene 11_446 with Dissolve(1)
                er "Oh..."
                er "Was I your first?"
                mc "Heh, yeah."
                er "I was?"
                mc "Of course. It was your fault to begin with."
                scene 11_447 with Dissolve(1)
                er "How was it my fault?"
                mc "You always grabbed me, lay on top of me when we 'fought' and tickled me."
                mc "You pressed your boobs against me all the freaking time, basically."
                er "..."
                scene 11_448 with Dissolve(1)
                er "Like this?"
                mc "..."
                scene 11_449 with Dissolve(1)
                mc "Yes! But you were wearing more clothes back then."
                er "I'd hope I was."
                scene 11_450 with Dissolve(1)
                ""
                scene black with Dissolve(1)
                pause 2
                scene 11_451 with Dissolve(1)
                mc "What about you?"
                er "Have I ever..."
                mc "Yes, while thinking of me."
                er "I have."
                mc "Oh... How many times?"
                scene 11_452 with Dissolve(1)
                er "Once..."
                mc "Only once?"
                er "Maybe twice..."
                mc "Haha. Maybe three times?"
                er "No. Twice!"
                scene 11_453 with Dissolve(1)
                mc "When?"
                er "The first time was after we were in the pool together."
                mc "The see-through bikini?"
                er "Yes..."
                mc "Heh. I did too, that day."
                scene 11_454 with Dissolve(1)
                mc "And the second?"
                er "..."
                er "When you showed me that game on your PC."
                scene 11_455 with Dissolve(1)
                mc "Haha. I knew you were horny."
                er "Hey! I wasn't..."
                scene 11_456 with Dissolve(1)
                mc "If Mom hadn't interrupted us then, maybe..."
                er "Maybe..."
                scene 11_457 with Dissolve(1)
                mc "Let's make up for it now then."
                er "Mmm..."
                scene 11_458 with Dissolve(1)
                er "[mc]..."
                scene 11_459 with Dissolve(1)
                er "Ahh..."
                scene 11_460 with Dissolve(1)
                er "*Moaning*"
                play sound "Sounds/Phone_Vibrate.mp3"
                n "*Bzzzt. Bzzzt*"
                scene 11_461 with Dissolve(1)
                er "..."
                mc "{i}(Come on!){/i}"
                mc "Your phone?"
                er "Yeah..."
                scene 11_462 with Dissolve(1)
                er "Sorry, I need..."
                mc "No, go ahead."
                scene 11_463 with Dissolve(1)
                er "Hello?"
                x "Am I speaking to Erynn Orlandi?"
                er "Yes, this is she."
                scene 11_464 with Dissolve(1)
                er "..."
                er "Not on me right now but I have those documents on my laptop."
                er "..."
                er "I'm on my way home, and I'll send them as soon as possible."
                scene 11_465 with Dissolve(1)
                er "Yes."
                er "..."
                er "Thank you. Goodbye."
                scene 11_466 with Dissolve(1)
                er "Sorry. I need to go."
                mc "{i}(I guess that's it for today. *Sigh*){/i}"
                er "Let's... We..."
                mc "Sure. Another time."
                scene 11_467 with Dissolve(1)
                er "What are your plans?"
                mc "Masturbate!"
                er "I regret I asked."
                mc "Haha."
                scene 11_468 with Dissolve(1)
                mc "Next time you do it. Be sure to think of me!"
                er "[mc]!"
                mc "Or I can help."
                er "..."
                scene 11_469 with Dissolve(1)
                er "I'll call you later, okay?"
                mc "Alright. Bye, Rinny."
                er "Heh... Bye, [mc]. And thanks again for today."
                scene 11_470 with Dissolve(1)
                mc "..."
                scene 11_471 with Dissolve(1)
                er "One more thing."
                mc "Ya?"
                er "A little inspiration as a thank you."
                scene black with Dissolve(1)
                transform moveup:
                    xalign 0.5 yalign 1.0
                    linear 5.0 yalign 0.0
                show 11_472 at moveup
                pause 3
                mc "Uh..."
                scene 11_473 with Dissolve(1)
                mc "Thanks..."
                mc "That will definitely help!"
                scene 11_474 with Dissolve(1)
                er "Haha. Bye!"
                mc "Later, Rin!"
                scene 11_475 with Dissolve(1)
                mc "{i}(That's the second time today she's reminded me of Iris.){/i}"
                mc "{i}(And that's such an Iris thing to do.){/i}"
                mc "{i}(The more I get to know Erynn again and the more comfortable she gets around me, the more similarities I see with Iris.){/i}"
                mc "{i}(Not just looks, but also personality.){/i}"
                scene 11_476 with Dissolve(1)
                mc "{i}(It seems like I have a type...){/i}"
                $ renpy.end_replay()
                jump Week5_Tuesday_Room

label Week5_Tuesday_Room_Alexis:
    scene black with Dissolve(1)
    pause 2
    stop music fadeout 1.0
    play music ("Music/LoFi Indie 2.mp3", "Music/LoFi Indie 1.mp3", "Music/LoFi Indie 3.mp3") volume 0.2
    scene 11_356 with Dissolve(1)
    play sound "Sounds/Phone_Vibrate.mp3"
    n "*Bzzzt. Bzzzt*"
    mc "..."
    n "*Bzzzt. Bzzzt*"
    mc "{i}(Who the fuck is calling now...?){/i}"
    scene 11_357 with Dissolve(1)
    mc "Hello?"
    x "Hey, cutie."
    mc "Who's this?"
    scene 11_358 with Dissolve(1)
    a "Uhm... Alexis!"
    mc "Oh. Hey, Lexi! Sorry... I was still half asleep."
    mc "How are you?"
    a "I'm good. How are you? How was the photo shoot?"
    if Erynn_Week5_Tuesday_Photoshoot_Join == True:
        scene 11_359 with Dissolve(1)
        mc "Uhm... It was... interesting."
        a "Interesting? Did something happen?"
        mc "I'll tell you later. Nothing to worry about."
        mc "{i}(I hope...){/i}"
        a "Hmm... You're being vague..."
    else:
        mc "It was good. It ended early because one of the models didn't show."
    scene 11_334 with Dissolve(1)
    a "Anyway. Erynn probably told you already. She, Iris, and I are going to the beach, either tomorrow or Thursday."
    a "And we were wondering if you wanted to join us."
    if Erynn_Week5_Tuesday_Photoshoot_Join == True:
        mc "{i}(Shit! Should I even go now after what happened earlier? But I told Erynn already that I'll go. Fuck!){/i}"
    else:
        pass
    mc "Uhm, yeah. I'll join you."
    a "Great. I didn't want to go with Iris and Erynn alone."
    scene 11_335 with Dissolve(1)
    mc "Why?"
    a "This stays between us. But I think Iris has a thing for Erynn."
    mc "{i}(I know...){/i}"
    mc "Does she?"
    a "Uh-huh."
    scene 11_336 with Dissolve(1)
    mc "What makes you say that?"
    a "The way she talks to her. Always flirty."
    a "And then the way she looks at her."
    mc "Lustful?"
    a "[mc]! But yeah."
    mc "Haha."
    scene 11_337 with Dissolve(1)
    mc "{i}(Should I tell her I know?){/i}"
    mc "{i}(Nah... This is just too much fun.){/i}"
    scene 11_338 with Dissolve(1)
    a "What are you doing the rest of the day?"
    mc "I don't know yet. Can I come over? Or maybe you can come here?"
    a "I want to but I have to get ready for work soon."
    mc "Ah, you're working today. Maybe I'll come by later, then."
    scene 11_339 with Dissolve(1)
    a "Are you working at the restaurant this week?"
    mc "I am. I think Thursday."
    a "So it would be better to go to the beach tomorrow, or else you won't be able to come."
    mc "It depends on the hours. I'll make sure I have time whatever day it is."
    a "Okay."
    scene 11_340 with Dissolve(1)
    n "*Knock-knock*"
    la "Lex, can I come in?"
    a "Give me a minute, [mc]."
    a "Yeah."
    scene 11_341 with Dissolve(1)
    la "Hey."
    a "Hey. What's up?"
    la "Question."
    scene 11_342 with Dissolve(1)
    la "Are you gonna be here this evening?"
    a "No, I'm working today. Why?"
    la "I'm having a hot tub party."
    a "Oh, that's fun. But don't worry. I won't interrupt you guys."
    scene 11_343 with Dissolve(1)
    la "No, you can join us after work, if you want."
    a "Thanks. Maybe I will. Who's coming? Elena?"
    la "Yes, Elena. Sienna, Kenz. Maybe Valeria. She wasn't sure yet if she'll make it."
    a "Only girls?"
    la "Why? You want there to be boys?"
    scene 11_344 with Dissolve(1)
    a "Not for me, for you!"
    la "..."
    la "So just join us after work, if you want."
    a "Thanks, Lays."
    la "Oh and Elena will stay the night. Just so you know."
    a "Alright."
    scene 11_345 with Dissolve(1)
    a "I'm back."
    mc "Did I hear something about a hot tub party?"
    a "Haha. Of course, you heard that."
    a "But I have bad news for you. It's girls only."
    scene 11_346 with Dissolve(1)
    mc "Damn. I knew I should've bought that long-haired wig."
    a "Haha."
    mc "Or I can use yours! Pretend to be Adriana."
    scene 11_347 with Dissolve(1)
    a "Haha. And get slapped on your ass by my dad who mistakes you for her."
    mc "Thanks for reminding me!"
    a "Haha. I'll never let you forget!"
    mc "Never mind. Go have fun at your hot tub party!"
    scene 11_348 with Dissolve(1)
    a "Hey. Next time you're here, we can have our own little hot tub party."
    a "Just the two of us."
    mc "I like the sound of that."
    n "*Knock-knock*"
    scene 11_349 with Dissolve(1)
    am "Alexis?"
    a "Sorry. Give me another minute."
    a "Yeah?"
    scene 11_350 with Dissolve(1)
    am "Hey. I'm leaving now. If you want to come with, get ready."
    a "I'll be right there. Five minutes."
    scene 11_351 with Dissolve(1)
    a "Sorry, I've gotta go."
    a "I'll call you once I know more about the beach date."
    mc "Alright. Have fun today. Bye, Lexi."
    a "Thanks, you too. Bye, [mc]. Love you."
    menu:
        "Say it back[KoGa3AutoWTChange1]{size=-4}(Alexis Points+2) {/size} {/color}":
            $ Alexis_Points += 2
            # Alexis (46)
            mc "Love you, too."
        "Hang up":
            pass
    jump Week5_Tuesday_Room

label Week5_Tuesday_Room:
    stop music fadeout 1.0
    play music ("Music/LoFi Indie 3.mp3", "Music/LoFi Indie 1.mp3", "Music/LoFi Indie 2.mp3") volume 0.2
    if Erynn_Week3_Monday_Blackmailhelp == False:
        if Alexis_Dating == True:
            scene 11_477 with Dissolve(1)
            mc "{i}(I'm bored already.){/i}"
            mc "{i}(I can't believe it's spring break and I don't know what to do.){/i}"
            mc "{i}(Maybe I should just train a bit on my own?){/i}"
            mc "{i}(I'll call Alexis first. Maybe we can hang out today.){/i}"
            scene 11_478 with Dissolve(1)
            mc "Hey, Lexi."
            a "Hi, [mc]. How are you?"
            mc "Good but bored."
            scene 11_479 with Dissolve(1)
            a "Bored? How come?"
            mc "I don't know."
            mc "What are you doing? Can I maybe come over or can we hang out?"
            a "Sorry. I'm not home right now."
            scene 11_480 with Dissolve(1)
            mc "You at work?"
            a "No. I'm at a photo shoot with Erynn."
            mc "Oh... Taking pictures together?"
            a "No, just her. It's for a perfume campaign."
            scene 11_481 with Dissolve(1)
            mc "How long will you be there?"
            a "I don't know. They're still waiting on another model. So, might take a while."
            mc "How about after?"
            a "I'm at the bar then. You can always come by if you're still bored. Even if you're not bored."
            mc "Hehe. I might do that."
            scene 11_482 with Dissolve(1)
            mc "Wanna do something tomorrow then?"
            a "Sorry. Can't tomorrow either."
            a "Made plans with Erynn and Iris already. We're going to the beach."
            mc "Cool."
            mc "{i}(Damn. I wish I could go with them. Well... Maybe not.){/i}"
            scene 11_483 with Dissolve(1)
            a "Thursday?"
            mc "I'm working at the restaurant."
            a "Hmm."
            mc "*Sigh* Are we going to see each other at all this spring break..."
            if Alexis_Week5_Monday_Date_Cancel == True:
                a "I'm not the one who cancelled our date yesterday."
                mc "True. Sorry about that. Something came up."
            else:
                a "We'll find time, don't worry."
            scene 11_484 with Dissolve(1)
            mc "I guess I'll leave you be, then."
            a "Okay. I'll call you once the shoot is done."
            a "Bye, [mc]."
            mc "Later, Lexi."
            scene 11_485 with Dissolve(1)
            mc "*Sigh*"
            mc "{i}(For a second it felt like she's avoiding me for some reason.){/i}"
            mc "Whatever... I guess I'll go run for a bit."
        else:
            pass
    else:
        pass
    if Layla_End == False:
        if Layla_Dating == True:
            scene black with Dissolve(2)
            pause 2
            scene 11_486 with Dissolve(1)
            play sound "Sounds/Phone_Vibrate.mp3"
            n "*Bzzzt. Bzzzt*"
            scene 11_487 with Dissolve(1)
            mc "Hey, Layla."
            la "Hey."
            mc "I was waiting for your call."
            scene 11_488 with Dissolve(1)
            la "Why?"
            mc "The hot tub party."
            la "What hot tub party?"
            scene 11_489 with Dissolve(1)
            mc "Weren't you planning a hot tub party today?"
            mc "Elena told me yesterday at the beach."
            la "Uhm... No?"
            mc "No? What the fuck? Elena... That little b-word. She got me good. I was looking forward to it, too."
            scene 11_490 with Dissolve(1)
            la "Haha."
            la "And I got you too, this time! You sounded so mad!"
            mc "..."
            mc "Funny!"
            scene 11_491 with Dissolve(1)
            mc "So there will be a party today?"
            la "Yes. You're coming, right?"
            mc "Now I'm not so sure anymore."
            scene 11_492 with Dissolve(1)
            la "No, you have to come!"
            la "Please?"
            mc "Fine."
            la "Yay!"
            scene 11_493 with Dissolve(1)
            la "Did Elena tell you to invite Zach?"
            mc "{i}(Like hell I'm inviting that idiot.){/i}"
            mc "She did."
            la "Is he joining?"
            mc "No. He's on a family vacation."
            la "Oh. Then there will only be two boys."
            scene 11_494 with Dissolve(1)
            mc "{i}(Two boys? Who's the other one? Miguel?){/i}"
            mc "Who else is coming?"
            la "Elena, Sienna, and her boyfriend."
            mc "{i}(Sienna's boyfriend... Haven't met him yet, or have I?){/i}"
            la "Maybe Valeria. She wasn't sure if she could make it. She'll let me know later."
            scene 11_495 with Dissolve(1)
            la "I asked Lexi but she had to work. She might come by after, though."
            if Alexis_Sex == True:
                mc "{i}(Alexis too? I don't know if she'd want to see me...){/i}"
            else:
                pass
            mc "How about Tori?"
            la "..."
            mc "Haha. I can hear you pouting."
            la "How about I invite Darryl too, then?"
            scene 11_496 with Dissolve(1)
            mc "Hey. The more the merrier, right? Your words at training camp."
            la "No! They're not invited!"
            mc "Haha."
            scene 11_497 with Dissolve(1)
            mc "What time should I come over?"
            la "Like six or so?"
            mc "Do you want me to bring anything? Snacks, or...?"
            la "Hmm, no need. Elena will be coming over soon and we'll get some stuff."
            scene 11_498 with Dissolve(1)
            la "Do you want anything specific?"
            mc "No. I'm good with whatever you're getting."
            mc "Need help with anything else? Setup?"
            la "Thanks, but I'm almost finished already. Just refilling the hot tub at the moment."
            scene 11_499 with Dissolve(1)
            mc "Do you need to refill it often?"
            la "After every use."
            mc "Really? I thought it was more like a swimming pool. Once every so many weeks or even months."
            la "That's when you use chemicals like chlorine and stuff."
            la "We don't use any chemicals in the water for the hot tub, so we have to drain and refill it after each use."
            scene 11_500 with Dissolve(1)
            mc "Especially after the last time, when I was there."
            la "Ew... Don't tell me you peed in the hot tub!"
            mc "What...? No... Why would I..."
            mc "I meant the thing we did..."
            scene 11_501 with Dissolve(1)
            mc "Right. Never mind. You swallowed."
            la "[mc]!"
            mc "Haha."
            scene 11_502 with Dissolve(1)
            la "..."
            mc "..."
            scene 11_503 with Dissolve(1)
            mc "Maybe we can repeat that?"
            la "We can't. There'll be other people there this time."
            mc "After they leave?"
            la "Elena's sleeping over, today."
            scene 11_504 with Dissolve(1)
            mc "Hmm..."
            mc "Then we'll just have to put her to bed early so we can have some alone time."
            if Elena_Points >= 29:
                mc "{i}(Or maybe... Damn. I'm getting hard just thinking about that.){/i}"
            else:
                pass
            la "Haha."
            scene 11_505 with Dissolve(1)
            mc "By the way. I missed you yesterday at the beach."
            la "Yeah?"
            mc "Yeah!"
            la "Sorry about that. Mom made me take some private lessons... With Ramirez..."
            if Gabi_End == False:
                mc "{i}(I know.){/i}"
                mc "I thought you were good on points after you received that B on the last test."
            else:
                mc "Spanish? I thought you were good on points after you received that B on the last test."
            scene 11_506 with Dissolve(1)
            la "I thought so too, but there was a slight miscalculation on my part."
            mc "Layla..."
            mc "Want some tutoring in math too?"
            la "No! We aren't even in the same class..."
            mc "Haha. Alright."
            scene 11_507 with Dissolve(1)
            if Elena_Points >= 29:
                la "I heard you had fun though."
                mc "Yeah. Elena had to look after her brothers, so I played a little with them."
                la "They like you."
                mc "Probably 'cause they can be a little rougher with me than with Elena."
                scene 11_508 with Dissolve(1)
                la "Or because you're still a kid too."
                mc "Haha."
                la "I'm kidding."
                mc "Nah, it's true though."
            else:
                la "Did you have fun at least?"
                mc "I did. We didn't stay too long, though. Elena had to look after her brothers."
                la "Oh... She did? I thought she had time yesterday."
                mc "Her mother had an extra shift."
                la "Hmm, okay. Her grandma is there now, though. So she has a little more free time."
            scene 11_509 with Dissolve(1)
            am "Layla?"
            la "I'm back here!"
            la "Give me a second, [mc]."
            mc "Sure."
            scene 11_510 with Dissolve(1)
            am "We'll be leaving then."
            la "Oh, you look beautiful, Mom!"
            mc "{i}(Beautiful? I want to see, too!){/i}"
            am "Thank you!"
            scene 11_511 with Dissolve(1)
            la "When will you be back?"
            am "Depends on your dad. Most likely way into the night."
            la "Okay."
            scene 11_512 with Dissolve(1)
            am "See you tomorrow then."
            la "Have fun, Mom."
            am "Thank you."
            scene 11_513 with Dissolve(1)
            am "Oh..."
            am "And not too crazy tonight, okay?"
            la "It's just a few people."
            am "Mm-hmm..."
            if Alexis_SecretPath == False:
                scene 11_514 with Dissolve(1)
                la "Kay, I'm back."
                mc "So Adriana isn't joining us later? What a pity."
                la "..."
                mc "Kidding, kidding."
                scene 11_515 with Dissolve(1)
                la "Wasn't it embarrassing enough the first time?"
                mc "Embarrassing? Why? Your mom is pretty cool, and I think she could hang with us."
                la "What...? You clearly don't know my mom."
                la "Weirdo!"
                mc "Haha."
                scene 11_516 with Dissolve(1)
                mc "{i}(I enjoyed our conversation last time.){/i}"
                mc "{i}(Probably because she was wearing a bikini.){/i}"
                mc "{i}(Damn. She looked good, too.){/i}"
            else:
                pass
            scene 11_517 with Dissolve(1)
            la "Anyway. I'm gonna finish up here before Elena arrives."
            mc "Alright. I'll see you a little later, then. Can't wait."
            la "Hehe, yeah. Bye, [mc]."
            mc "Later, Layla."
        else:
            pass
    else:
        pass
    scene black with Dissolve(1)
    pause 2
    stop music fadeout 1.0
    play music "Music/Alessio Acierno - To Light Our Youth.mp3" volume 0.5
    # Copyright NyxVN
    scene 11_518 with Dissolve(1)
    mc "*Sings* We used to walk on sunlight, hands in each other's dreams."
    mc "*Sings* But the storm came crashing, tore apart the woven seams."
    mc "*Sings* The silence grew between us, like a canyon wide and strong."
    mc "*Sings* We lost the map to find us, but time still hums our song."
    scene 11_519 with Dissolve(1)
    mc "*Sings* Tied by threads we can't escape, though years have drawn their line."
    mc "*Sings* The roads we took have bent and broke, yet here we intertwine."
    mc "*Sings* Your face still tells the story, your eyes still hold the truth."
    mc "*Sings* A spark that once was broken, now glows to light our youth."
    scene 11_520 with Dissolve(1)
    mc "*Sings* Now glows to light our youth..."
    m "Beautiful!"
    mc "..."
    stop music fadeout 1.0
    play music ("Music/LoFi Indie 3.mp3", "Music/LoFi Indie 1.mp3", "Music/LoFi Indie 2.mp3") volume 0.2
    scene 11_521 with Dissolve(1)
    mc "Mom!"
    m "That was beautiful, honey!"
    mc "Thanks. But what are you doing here so early? Didn't you say you'll be coming home late?"
    m "I was just dropping off some stuff. I'm heading to work now."
    scene 11_522 with Dissolve(1)
    m "Who's the girl?"
    mc "What girl?"
    m "The girl the song's about."
    mc "Uhm... No one in particular. Just... Uh... Random, I guess..."
    m "Hmm..."
    scene 11_523 with Dissolve(1)
    m "It sounds beautiful."
    mc "It's not ready yet. I'm still messing around with the chorus and lyrics."
    m "Have you written other songs?"
    mc "I have a couple more."
    scene 11_524 with Dissolve(1)
    m "..."
    mc "..."
    scene 11_525 with Dissolve(1)
    mc "What?"
    m "Aren't you going to play them?"
    mc "Not when you're here."
    m "Why not? I'd love to hear them."
    mc "It's embarrassing!"
    scene 11_526 with Dissolve(1)
    stop music fadeout 1.0
    play music ("Music/Slow4.mp3", "Music/Slow.mp3") volume 0.2
    m "*Sigh* Fine. I'll leave."
    mc "Mom! Wait!"
    mc "The police station. How was it? What happened?"
    scene 11_527 with Dissolve(1)
    m "Honestly. I didn't want to tell you this, but..."
    mc "It's that serious?"
    m "It is."
    m "Look. You can't tell anyone about this, alright? It's still an ongoing investigation."
    mc "Uhm, okay..."
    scene 11_528 with Dissolve(1)
    if Rachel_End == True:
        m "Do you remember Rachel?"
        mc "The manager you had to fire some weeks ago?"
        m "Mm-hmm."
        mc "What did she do this time?"
    else:
        m "You remember Rachel, right?"
        mc "Uhm... Yeah..."
        mc "{i}(Haven't heard anything from her since last time we...){/i}"
        mc "Something happened again?"
    scene 11_529 with Dissolve(1)
    m "Last week. They... They found her body."
    mc "Her body...? Wait... You mean she's..."
    m "Yeah."
    mc "Oh... Uhm..."
    scene 11_530 with Dissolve(1)
    mc "What happened?"
    m "They didn't tell me."
    mc "Was it an accident, or was she...?"
    m "I don't know."
    scene 11_531 with Dissolve(1)
    m "*Crying* She made some... Questionable decisions, but..."
    m "*Crying* This is something I wouldn't wish on anyone."
    menu:
        "Hug her[KoGa3AutoWTChange1]{size=-4}(Emily Points+2) {/size} {/color}":
            $ Emily_Points += 2
            # Emily (22)
            scene 11_532 with Dissolve(1)
            mc "Yeah."
            mc "I'm sorry you have to go through this."
        "Don't":
            pass
    if Rachel_End == False:
        scene 11_533 with Dissolve(1)
        m "What about you?"
        m "How are you feeling? Because you and her..."
        mc "Yeah, I know... I just... I don't know. I have to process this first."
    else:
        pass
    scene 11_534 with Dissolve(1)
    mc "Why did you have to go to the station? Did they think you were involved or something?"
    m "No. They had some questions regarding her."
    m "Why she was fired. If I'd seen her after... Stuff like that."
    if Rachel_End == False:
        scene 11_535 with Dissolve(1)
        mc "Do I have to go too? Because..."
        m "No. I haven't told them that. It has nothing to do with their case."
        m "Besides. I don't want you involved in this. They don't need to know."
        mc "..."
    else:
        pass
    scene 11_536 with Dissolve(1)
    m "*Sigh*"
    m "Anyway. I need to change and head to the restaurant now."
    mc "You're still going after that?"
    m "It's impossible to take a day off at this time. We're so busy."
    m "And work lets me focus on other stuff so I won't be thinking of this the whole day."
    mc "Hmm, true."
    scene 11_537 with Dissolve(1)
    m "See you later this evening, then?"
    if Layla_Dating == False:
        mc "Yeah."
    else:
        mc "I'm invited to a party later today. So I don't know when I'll be back."
        if MC_Bike == True:
            m "No driving the bike if you're going to drink!"
            m "I'd rather have you call me in the middle of the night and I'll pick you up."
            mc "Don't worry. I'll take the bus."
        else:
            pass
        m "Alright. Have fun."
        mc "Thanks."
    scene 11_538 with Dissolve(1)
    m "Don't think about this too much, okay?"
    mc "I'll try. Bye, Mom."
    m "Bye, honey."
    if Rachel_End == False:
        scene 11_539 with Dissolve(1)
        mc "{i}(I had sex with someone who's now dead...){/i}"
        mc "{i}(That's so weird somehow.){/i}"
        mc "{i}(Why am I even thinking about that?){/i}"
    else:
        scene 11_539 with Dissolve(1)
        mc "{i}(It's kinda weird to know someone who got murdered.){/i}"
        mc "{i}(If she got murdered. They found her body... What else could've happened?){/i}"
    if Valeria_LikeMC == True:
        scene black with Dissolve(1)
        pause 2
        stop music fadeout 1.0
        play music ("Music/EDM 1.mp3", "Music/EDM 2.mp3", "Music/EDM 3.mp3", "Music/EDM 4.mp3") volume 0.2
        scene 11_540 with Dissolve(1)
        mc "{i}(I really need to stop thinking about this now. But what to do?){/i}"
        mc "{i}(Maybe call Valeria? She said she would call me but...){/i}"
        mc "{i}(Yeah, I want to see her.){/i}"
        scene 11_541 with Dissolve(1)
        mc "{i}(I just can't forget about our kiss in the photo booth...){/i}"
        mc "{i}(I hope she has time today to hang.){/i}"
        scene 11_542 with Dissolve(1)
        play sound "Sounds/Phone_Vibrate.mp3"
        n "*Bzzzt. Bzzzt*"
        va "..."
        scene 11_543 with Dissolve(1)
        x "Good! Two more."
        va "*Heavy breathing*"
        play sound "Sounds/Phone_Vibrate.mp3"
        n "*Bzzzt. Bzzzt*"
        x "Come on! You can do it."
        scene 11_544 with Dissolve(1)
        play sound "Sounds/Phone_Vibrate.mp3"
        n "*Bzzzt. Bzzzt*"
        x "Look up!"
        x "And tighten your core!"
        scene 11_545 with Dissolve(1)
        va "Nggh..."
        play sound "Sounds/Phone_Vibrate.mp3"
        n "*Bzzzt. Bzzzt*"
        x "A little more."
        scene 11_546 with Dissolve(1)
        mc "{i}(Hmm...){/i}"
        mc "{i}(Not picking up. Is she watching TV again?){/i}"
        scene 11_547 with Dissolve(1)
        play sound "Sounds/Phone_Vibrate.mp3"
        n "*Bzzzt. Bzzzt*"
        x "Wait. I'll help you."
        scene 11_548 with Dissolve(1)
        va "*Heavy breathing*"
        x "Good job! I knew you can manage this."
        va "Haha. Thanks. I'm beat though."
        scene 11_549 with Dissolve(1)
        va "Before we continue. Let me check real quick who called me."
        x "Let's take a five-minute break, then."
        va "Alright."
        scene 11_550 with Dissolve(1)
        x "I'll be right back. I need to drop a deuce."
        va "Seriously...?"
        x "Take a shit! Better?"
        va "No, that's not better."
        scene 11_551 with Dissolve(1)
        x "Drop the kids off at the pool?"
        va "Haha... Oh my god..."
        x "Answer the call of nature."
        va "I get it! Will you just go already... You're so annoying!"
        x "Haha."
        scene 11_552 with Dissolve(1)
        x "I've got one more. Pinch a loaf."
        va "What? Pinch a loaf? Haha. Never heard that before. Gross!"
        scene 11_553 with Dissolve(1)
        mc "Hey."
        va "Hi."
        mc "So absorbed in a TV show again that you didn't pick up?"
        va "Finishing up my set."
        scene 11_554 with Dissolve(1)
        mc "Oh. You're training?"
        va "Uh-huh."
        mc "I can call later if..."
        va "It's fine. What's up?"
        scene 11_555 with Dissolve(1)
        mc "I can't forget about what happened yesterday."
        va "Yeah. Sucks that Layla lost her hoodie."
        mc "Heh... True. But that's not what I meant."
        va "..."
        scene 11_556 with Dissolve(1)
        mc "I meant what happened in the photo booth."
        va "Hmm. The photo booth... I remember. Vaguely."
        mc "Haha. Vaguely..."
        mc "You should have a picture. That might refresh your memory."
        scene 11_557 with Dissolve(1)
        va "Right. The picture."
        va "Mom said you're handsome."
        mc "You showed your mom? And she thinks I'm handsome?"
        va "Okay... Don't let it go to your head now."
        scene 11_558 with Dissolve(1)
        va "She snuck up on me and saw it."
        mc "Snuck up on you while you were looking at the picture?"
        va "Maybe..."
        mc "Haha."
        scene 11_559 with Dissolve(1)
        mc "Talking about a maybe."
        mc "Yesterday I asked if you wanted to hang out today and you said maybe."
        mc "So I was hoping to turn that maybe into a yes."
        va "Wow... Did you google that?"
        mc "Haha, okay. Fair enough."
        x "Excuse me."
        scene 11_560 with Dissolve(1)
        x "Are you finished with the squat rack?"
        va "Uhm... No. But I'm taking a short break. Feel free to use it."
        x "Thanks. I won't change the weights. Just a few warmup sets."
        va "No worries."
        scene 11_561 with Dissolve(1)
        mc "You're at the gym?"
        mc "{i}(Squat rack... No wonder she has such an amazing ass.){/i}"
        va "I am. Doing some weight training today."
        mc "{i}(I wish I was there with her...){/i}"
        mc "So nice of you to let someone else use the same machine."
        scene 11_562 with Dissolve(1)
        mc "Most times I let them wait until I'm finished with all my sets."
        va "Same, but I'm not really using it at the moment. And if you saw this guy, I think you'd change your mind too."
        mc "Yeah?"
        va "Mm-hmm. He's huge."
        scene 11_563 with Dissolve(1)
        da "Huge? Someone is talking about me!"
        va "..."
        va "Hey, Darryl."
        mc "{i}(Darryl? Why's he there?){/i}"
        scene 11_564 with Dissolve(1)
        da "Sup baby girl? How you doin'? Lookin' fine today!"
        va "Thanks. I'm good. How are you? Enjoying the break?"
        da "Not only the break."
        va "..."
        scene 11_565 with Dissolve(1)
        da "Cool seeing you at the gym. Finally, someone on the team who takes this as seriously as I do."
        da "Didn't expect less of someone who went to Nationals."
        da "We should train together sometime."
        va "Uhm... Sure..."
        scene 11_566 with Dissolve(1)
        da "Watcha doin' later?"
        da "Wanna hang out?"
        scene 11_567 with Dissolve(1)
        va "..."
        scene 11_568 with Dissolve(1)
        va "I'm busy today."
        mc "{i}(Yeah. Just piss off, Darryl!){/i}"
        scene 11_569 with Dissolve(1)
        da "Tomorrow then. We're all going to the beach. Tori, TJ, Jazz..."
        va "Maybe."
        mc "{i}(Maybe? No! Just say no!){/i}"
        va "Look. I'm on the phone right now. How about I call you later?"
        mc "{i}(Call him later? Does she have his number? Why do you have his number? You don't need it!){/i}"
        da "Sure."
        scene 11_570 with Dissolve(1)
        da "I'll see you tomorrow, then."
        va "..."
        da "Later, Val!"
        va "Bye."
        scene 11_571 with Dissolve(1)
        da "Yo, Shaq!"
        sq "Sup, Darryl."
        va "Hey. Sorry."
        scene 11_572 with Dissolve(1)
        mc "So, uhm... You're busy today? Or did you just say that to get rid of Darryl?"
        va "No, I'm actually busy."
        mc "Hmm..."
        mc "And you're going to the beach with them tomorrow?"
        scene 11_573 with Dissolve(1)
        va "Maybe. I don't know yet."
        mc "Damn. I wanted to be the first to show you the beach."
        mc "After we go buy that swimsuit you tried on yesterday."
        va "..."
        scene 11_574 with Dissolve(1)
        va "You still can."
        va "Let's go running together tomorrow morning. At the beach."
        va "Minus the swimsuit though."
        mc "But you looked so amazing in it. I want to see you wearing it again."
        scene 11_575 with Dissolve(1)
        va "I guess the picture will have to do for now!"
        mc "You still need to send me the second one."
        va "Do I?"
        mc "Uh-huh."
        scene 11_576 with Dissolve(1)
        va "Maybe!"
        mc "Aaah! I hate your maybes!"
        va "Haha."
        scene 11_577 with Dissolve(1)
        mc "Well, I'll leave you to it then. Finish up your sets."
        va "I will."
        mc "Oh yeah. What time?"
        va "Let's meet at seven at the boardwalk."
        mc "Great."
        scene 11_578 with Dissolve(1)
        mc "Bye, Vaaal."
        va "Why did you say it like that?"
        mc "Haha. Like what?"
        va "..."
        scene 11_579 with Dissolve(1)
        va "*Mockingly* Bye, [mc]..."
        mc "Haha."
        scene 11_580 with Dissolve(1)
        mc "..."
        mc "{i}(I can't stop smiling now.){/i}"
        play sound "Sounds/Phone_Message.mp3"
        n "*Bzzzt*"
        scene black with Dissolve(1)
        transform moveup:
            xalign 0.5 yalign 1.0
            linear 5.0 yalign 0.0
        show 11_581 at moveup
        pause 3
        mc "Oh damn..."
        scene 11_582 with Dissolve(1)
        mc "Haha, this is amazing."
        mc "{i}(She really loves her pictures.){/i}"
        mc "{i}(And she looks good too. I really need to step up my training.){/i}"
        scene 11_583 with Dissolve(1)
        x "Looking good!"
        x "Getting back in shape, huh?"
        scene 11_584 with vpunch
        n "*Slap*"
        va "Ahh... Hey!"
        x "C'mon. Enough playing around. Let's finish those sets, first."
        scene 11_585 with Dissolve(1)
        x "And send me a copy of that picture."
        va "No, I won't!"
        x "Haha."
    else:
        pass
    if Layla_Dating == True:
        jump Week5_Tuesday_Layla_Hottub
    else:
        jump Week5_Wednesday_Morning

label Week5_Tuesday_Layla_Hottub:
    scene black with Dissolve(1)
    pause 2
    stop music fadeout 1.0
    play music ("Music/TropiPop 1.mp3", "Music/TropiPop 2.mp3", "Music/TropiPop 3.mp3", "Music/TropiPop 4.mp3", "Music/TropiPop 5.mp3", "Music/TropiPop 6.mp3", "Music/TropiPop 7.mp3") volume 0.2
    scene 11_586 with Dissolve(1)
    mc "{i}(I've been here a few times now, but I'm still speechless every time I see their house...){/i}"
    scene 11_587 with Dissolve(1)
    mc "..."
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 11_588 at moveup
    pause 3
    mc "{i}(And I've seen her a few times now, and I'm still speechless every time I see this cutie...){/i}"
    scene 11_589 with Dissolve(1)
    mc "Hi."
    la "Finally!"
    mc "Finally? I thought I was early."
    la "Everyone is here already."
    mc "Oh..."
    scene 11_590 with Dissolve(1)
    la "Hey!"
    mc "Hehe. Hi."
    scene 11_591 with Dissolve(1)
    ""
    scene 11_592 with Dissolve(1)
    la "Aah-haha..."
    la "Let's go inside first..."
    mc "You started it!"
    scene 11_593 with Dissolve(1)
    mc "You look cute."
    mc "I love those hotpants on you."
    la "Thanks."
    mc "Your butt looks amazing in them."
    la "Haha. Thanks."
    scene 11_594 with Dissolve(1)
    la "What's in the bag."
    mc "A few beers, a bottle of wine..."
    la "You didn't have to bring anything. We have plenty here."
    mc "Yeah, but I felt bad coming empty-handed."
    scene 11_595 with Dissolve(1)
    mc "And I've got my own towel this time."
    la "Oh? You brought the Elena towel?"
    mc "No..."
    scene 11_596 with Dissolve(1)
    la "You should've brought that one. Still disappointed I wasn't there to see her reaction."
    mc "Well, I don't have it. Elena took it home."
    la "What? No!"
    scene 11_597 with Dissolve(1)
    la "Then I guess I'll just have to make a new one."
    la "I have plenty of pictures of her."
    mc "Haha. Poor Elena."
    if Elena_Points >= 29:
        mc "{i}(I feel a little bad, but then again. I want that towel!){/i}"
    else:
        pass
    menu:
        "Make Layla towel[KoGa3AutoWTChange1]{size=-4}(Layla Points+2, Layla Week5 Tuesday Hottub Towel) {/size} {/color}":
            $ Layla_Points += 2
            # Layla (78)
            $ Layla_Week5_Tuesday_Hottub_Towel = True
            scene 11_598 with Dissolve(1)
            mc "How about we make one of you?"
            mc "We can take some nice pictures for it today."
            la "Yeah? Sure. Maybe we can make one together, too?"
            mc "Of course."
            scene 11_599 with Dissolve(1)
            la "Yay!"
            mc "Haha."
        "Don't":
            pass
    scene 11_600 with Dissolve(1)
    la "Let's get this party started!"
    mc "Someone is excited."
    la "You're not?"
    mc "I am."
    mc "{i}(I so am!){/i}"
    scene 11_601 with Dissolve(1)
    mc "{i}(They actually are here already.){/i}"
    mc "{i}(I thought she was joking.){/i}"
    mc "{i}(That must be Sienna's boyfriend. Don't think I've seen him before.){/i}"
    scene 11_602 with Dissolve(1)
    mc "Hey, guys."
    el "You're late!"
    mc "How am I late? Layla said six. It's not even six yet. You're all just early!"
    menu:
        "Hug Elena":
            scene 11_603 with Dissolve(1)
            mc "Hey again. How are you?"
            el "Hey. I'm good. How are you?"
            mc "Amazing!"
            el "Haha."
        "Kiss Elena[KoGa3AutoWTChange1]{size=-4}({i}Elena Points > 29: Elena Points-2{/i}) {/size} {/color}":
            if Elena_Points >= 29:
                pass
            else:
                $ Elena_Points -= 2
            scene 11_604 with Dissolve(1)
            mc "Hey again. How are you?"
            el "Hey. I'm good. How are you?"
            mc "Amazing!"
            el "Haha."
    menu:
        "Hug Sienna":
            scene 11_605 with Dissolve(1)
            mc "Nice to see you, Sienna."
            si "Hey, [mc]."
        "Kiss Sienna[KoGa3AutoWTChange1]{size=-4}(Sienna Points+2) {/size} {/color}":
            $ Sienna_Points += 2
            # Sienna (2)
            scene 11_606 with Dissolve(1)
            mc "Nice to see you, Sienna."
            si "Hey, [mc]."
    scene 11_607 with Dissolve(1)
    mc "Hey. We haven't met yet. I'm [mc]."
    ih "Isaiah. Nice to meet you."
    mc "You too."
    scene 11_608 with Dissolve(1)
    la "[mc]. What do you want to drink?"
    mc "Uhm... I'll start with a beer."
    la "I'll get you one."
    mc "Thanks."
    scene 11_609 with Dissolve(1)
    la "Here you go."
    mc "Thanks."
    la "And why are you sitting there? Come join us on the sofa. Plenty of space."
    scene 11_610 with Dissolve(1)
    mc "I'm happy you could make it today, Elena."
    el "Me too. My grandma is here for three days. She'll take care of the boys."
    mc "You definitely deserve some time off."
    el "Hehe, thanks."
    if Elena_Week5_Monday_Beach == False:
        pass
    else:
        scene 11_611 with Dissolve(1)
        el "And thanks again for yesterday. Playing with them."
        mc "Of course. It was fun."
        el "They kept talking about it until they went to sleep."
        mc "Hehe."
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 11_612 at moveup
    pause 3
    mc "..."
    scene 11_613 with Dissolve(1)
    el "What?"
    mc "You look different."
    el "Layla did my makeup earlier."
    scene 11_614 with Dissolve(1)
    la "And I won! Haha. I told you!"
    el "Dios mío..."
    mc "Huh?"
    el "She and I made a bet over whether you'd notice or not. I said you wouldn't. So, she won!"
    scene 11_615 with Dissolve(1)
    la "I know you're very observant! Easiest bet of my life!"
    el "..."
    mc "What was the bet?"
    la "Nothing. Just to see who was right."
    mc "No running a lap in the backyard, completely naked?"
    scene 11_616 with Dissolve(1)
    la "Oh yeah, we could do that!"
    el "Like hell I'd do that!"
    mc "Haha."
    if Elena_Points >= 29:
        scene 11_617 with Dissolve(1)
        mc "You look really nice, though."
        el "Thanks!"
    else:
        pass
    scene 11_618 with Dissolve(1)
    mc "By the way. We should put those drinks away. They'll be warm in no time in this heat."
    la "Yeah. I just put them all out so everyone can take what they want."
    mc "Do you have a cooler box with ice or something?"
    la "The bar there has a fridge."
    scene 11_619 with Dissolve(1)
    mc "Of course you have a fridge outside... A cooler box? What was I thinking?"
    la "What?"
    el "Haha."
    scene black with Dissolve(1)
    pause 2
    scene 11_620 with Dissolve(1)
    mc "Cheers everyone."
    la "Cheers!"
    scene 11_621 with Dissolve(1)
    mc "So Isaiah. What school do you go to?"
    ih "MSU."
    mc "Oh, you go to MSU?"
    ih "Yeah. I'm a freshman."
    mc "Cool."
    scene 11_622 with Dissolve(1)
    mc "Then you must know Layla's sister, Alexis?"
    ih "I've seen her around, but I don't really know her. We don't have classes together, either."
    if Erynn_Week5_Tuesday_Photoshoot == True:
        mc "What about Erynn?"
        ih "Everyone knows Erynn. She's something of a celebrity."
        mc "Heh..."
    else:
        pass
    scene 11_623 with Dissolve(1)
    mc "How did you and Sienna meet, then?"
    ih "I also went to Madison Athletic. We were actually on the cheer team together."
    mc "That's awesome."
    mc "I also contemplated joining."
    scene 11_624 with Dissolve(1)
    el "Yeah fucking right!"
    mc "Haha. I'm kidding. I just wanted to see your reaction."
    el "You're laughing now, but one day I'll make you!"
    mc "Is that your new recruitment shtick? Since the uniform one didn't work?"
    el "..."
    scene 11_625 with Dissolve(1)
    la "You looked good in the uniform though!"
    mc "So did you. And that cheer at training camp was sexy, too!"
    mc "I knew I should've recorded that."
    la "Haha. No!"
    scene 11_626 with Dissolve(1)
    mc "How did it go again?"
    mc "Something with I hate this. Yes, I hate this."
    la "Oh my god. Stop! That was so embarrassing."
    mc "Haha. I liked it."
    la "I hated it!"
    scene 11_627 with Dissolve(1)
    mc "Okay. How about this? I'll join if you join, Layla."
    el "Yes!"
    mc "{i}(Shit. Maybe I shouldn't have said that. This may backfire.){/i}"
    la "Never gonna happen."
    mc "{i}(Sigh of relief! Thanks, Layla.){/i}"
    scene 11_628 with Dissolve(1)
    el "Layla, please!"
    la "Nope."
    el "We could use more guys on the team!"
    la "Oh... So you only wanted [mc], to begin with!"
    mc "Haha. Now the truth comes out."
    scene 11_629 with Dissolve(1)
    el "No. You're really good, too!"
    mc "I sense a but coming."
    el "There's no but!"
    el "But..."
    mc "See!"
    scene 11_630 with Dissolve(1)
    el "Aah... No! You made me say it!"
    mc "Yeah. Blame it on me, now."
    mc "We all know you're mean."
    scene 11_631 with Dissolve(1)
    mc "Hey! What are you doing? Why are you always ganging up on me!"
    mc "You should be fighting each other!"
    la "This is more fun!"
    mc "But I'm all for love, peace and happiness!"
    el "Haha."
    scene 11_632 with Dissolve(1)
    mc "{i}(What am I talking about? This is happiness!){/i}"
    mc "{i}(Having Layla's boobs next to my face!){/i}"
    mc "{i}(They asked for it.){/i}"
    scene 11_633 with Dissolve(1)
    la "Aah-haha... Elena! Do something!"
    el "I'm trying!"
    la "Hold him back."
    el "What do you think I'm doing!"
    la "Do it better!"
    scene 11_634 with Dissolve(1)
    ih "Haha. Are they always like that?"
    si "Oh yeah. Even at school."
    scene 11_635 with Dissolve(1)
    la "Haha. You're so heavy! Why am I always the one on the bottom?"
    el "Because you always start this."
    la "Not this time! I only tried to help you!"
    scene 11_636 with Dissolve(1)
    mc "{i}(I need to stop this.){/i}"
    mc "{i}(I'm getting turned on way too much by this sort of 'fighting'.){/i}"
    mc "{i}(Especially with these two.){/i}"
    scene 11_637 with Dissolve(1)
    mc "Okay, okay. You guys win!"
    la "What? You're giving up?"
    mc "Yes... This time!"
    mc "{i}(Fuck. She looks so good lying there. If Sienna and Isaiah weren't here...){/i}"
    scene 11_638 with Dissolve(1)
    mc "*Heavy breathing* Man... I'm all sweaty now."
    la "Haha. Take your shirt off then."
    mc "I'm about to. And I need a refreshing beer."
    scene black with Dissolve(1)
    pause 2
    scene 11_639 with Dissolve(1)
    mc "Anyway. Back on topic. How long have you been together now?"
    ih "Oh man... You're putting me on the spot."
    mc "Haha, sorry. Never mind then."
    scene 11_640 with Dissolve(1)
    si "No, no. He'll answer. And you'd better get it right!"
    ih "Uhm..."
    ih "Almost one and a half years now?"
    scene 11_641 with Dissolve(1)
    si "Yeah. We started dating at the start of last school year."
    la "It's been that long, already?"
    la "Congrats. You guys are so cute."
    si "Thanks."
    scene 11_642 with Dissolve(1)
    mc "Do you still cheer? Are you on the MSU cheer squad?"
    ih "No, I didn't join them. To be honest. I wasn't that good anyway."
    el "Yeah, you weren't."
    scene 11_643 with Dissolve(1)
    la "Elena!"
    el "What? He wasn't. He even admitted it himself."
    mc "Haha."
    scene 11_644 with Dissolve(1)
    ih "It's true. Maybe because I was mostly distracted by this one here."
    si "Aw..."
    scene 11_645 with Dissolve(1)
    la "Shall we move this to the hot tub, now?"
    mc "Sure."
    si "Let me change into my bikini first."
    scene 11_646 with Dissolve(1)
    la "We'll be right back."
    mc "And we'll move the drinks to the hot tub in the meantime."
    la "Thanks. I'll also get a bucket with ice where we can put the bottles in so we don't have to get out all the time for refills."
    mc "A bucket? You don't have a fridge at the hot tub?"
    la "What? Why would we have a fridge there? Anyway. We'll be right back."
    scene black with Dissolve(1)
    pause 2
    scene 11_647 with Dissolve(1)
    mc "*Singing* Two bros, chillin' in a hot tub, five feet apart 'cause they're not gay."
    ih "Haha. I saw that video. That's funny."
    mc "Haha, yeah. This just reminded me of that."
    ih "Oh man..."
    scene 11_648 with Dissolve(1)
    ih "So, question. You're with Layla?"
    mc "Hmm... We're sorta dating, I guess? We haven't made it official or anything yet."
    ih "Okay. I got confused earlier since it seems that you're also close to Elena."
    mc "We play around a lot. Elena is a lot of fun."
    scene 11_649 with Dissolve(1)
    ih "I saw that. Kinda jealous. The way you talk with them and as you said, play around. I would never be able to."
    ih "I'm way too shy in that regard."
    mc "I kinda grew up hanging around girls and my previous girlfriend taught me a lot."
    mc "When girls are comfortable around you, they'll get playful on their own and you just join in the fun."
    scene 11_650 with Dissolve(1)
    ih "Still. You make it look easy. Especially with Elena. Layla was always the more outgoing of the two, but Elena..."
    ih "I didn't expect her to be that way. I've known her for years and she's always been... Hmm..."
    mc "Bitchy?"
    ih "Uh... For a lack of a better word, yes."
    scene 11_651 with Dissolve(1)
    mc "Trust me. We weren't that close in the beginning. She was cold towards me, too."
    mc "But once you hang around with her and get to know her, she opens up."
    mc "Now I think she's amazing. Still bitchy, but amazing."
    scene 11_652 with Dissolve(1)
    ih "Haha. Don't tell her that."
    mc "I have already. A couple of times."
    ih "And you're still here to tell the story?"
    mc "Haha. I'm still watching my back. Just to be sure."
    ih "Haha."
    scene 11_653 with Dissolve(1)
    mc "How long have you known the girls?"
    ih "Four years now? Something like that. First Elena and Layla when they joined the squad. Sienna joined a year later."
    mc "And then it was love at first sight?"
    scene 11_654 with Dissolve(1)
    ih "No, it wasn't. And don't get me wrong. I love Sienna."
    ih "But I would be lying if I said I wasn't attracted to Elena first. Both her and Layla to be fair."
    mc "Can't blame you. All three of them are gorgeous girls."
    ih "They are."
    scene 11_655 with Dissolve(1)
    ih "But now it's all Sienna. Every day she gets more beautiful to me."
    mc "Yeah, she's a cutie."
    ih "Which of the girls are you most attracted to? Lookswise."
    mc "Lookswise...? Hmm..."
    menu:
        "Layla[KoGa3AutoWTChange1]{size=-4}(Layla Points+2) {/size} {/color}":
            $ Layla_Points += 2
            # Layla (80)
            scene 11_656 with Dissolve(1)
            mc "Layla!"
            mc "Cute face, banging body. Big boobs. What's not to like?"
            ih "I agree. She has a great set of boobs."
        "Elena[KoGa3AutoWTChange1]{size=-4}(Elena Points+2) {/size} {/color}":
            $ Elena_Points += 2
            # Elena (42)
            scene 11_656 with Dissolve(1)
            mc "Elena!"
            mc "There's this way she looks at you, which draws you in."
            mc "And let's not forget that ass."
            ih "Haha."
        "Sienna[KoGa3AutoWTChange1]{size=-4}(Sienna Week5 Tuesday Hottest, Sienna Points+2) {/size} {/color}":
            $ Sienna_Week5_Tuesday_Hottest = True
            $ Sienna_Points += 2
            # Sienna (4)
            scene 11_656 with Dissolve(1)
            mc "Not to step on your toes, but it's Sienna. She's hot man."
            ih "Don't worry about it. I take it as a compliment."
            ih "It makes me happy that a good-looking guy finds my girlfriend hot."
            ih "She also said she finds you attractive, so..."
    scene 11_657 with Dissolve(1)
    si "We're back."
    ih "Is that a new bikini? I haven't seen that one before."
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 11_658 at moveup
    pause 3
    mc "{i}(Look at those three hotties!){/i}"
    scene 11_659 with Dissolve(1)
    si "It is."
    ih "You look beautiful!"
    si "Thanks, babe."
    scene 11_660 with Dissolve(1)
    mc "Hand me the bucket. I'll put it here in the corner."
    la "Thanks."
    scene 11_661 with Dissolve(1)
    el "The water is cold!"
    la "Yeah... About that. I thought because it's so warm outside, it would be better with colder water."
    el "Then we could have just used the pool and called it a pool party..."
    la "But the pool doesn't have bubbles and this is cosier."
    la "We can warm it up if you want?"
    scene 11_662 with Dissolve(1)
    mc "It's fine like this."
    mc "Nice and refreshing. Just get in Elena, you'll get used to it quickly."
    el "Give me a second."
    menu:
        "Grab Elena[KoGa3AutoWTChange1]{size=-4}({i}Elena Points > 31: Elena Points-4{/i}) {/size} {/color}":
            scene 11_663 with Dissolve(1)
            mc "Come on. What are you waiting for? Sienna is in already."
            el "[mc]! Don't you dare!"
            scene 11_664 with Dissolve(1)
            el "Hey!"
            el "Don't drop me!"
            scene 11_665 with Dissolve(1)
            el "Aaah..."
            el "[mc]! I swear! Pendejo!"
            mc "Haha."
            scene 11_666 with Dissolve(1)
            el "..."
            la "Haha."
            scene 11_667 with Dissolve(1)
            el "Qué cabrón!"
            mc "What? I helped you."
            if Elena_Points >= 31:
                scene 11_668 with Dissolve(1)
                mc "Perdón! Perdón!"
                el "..."
                scene 11_669 with Dissolve(1)
                mc "Truce?"
                el "Sure."
                scene 11_670 with vpunch
                mc "He..."
                mc "..."
                mc "{i}(So much for truce!){/i}"
                scene 11_671 with Dissolve(1)
                mc "{i}(But if this is my punishment. I'll take it anytime!){/i}"
                scene 11_672 with Dissolve(1)
                mc "Haha. I get it."
                mc "Don't mess with Elena!"
                el "See Layla. Perrito is learning!"
                la "Hehe."
            else:
                $ Elena_Points -= 4
        "Let her get in by herself":
            pass
    scene 11_673 with Dissolve(1)
    mc "Why are you still standing there?"
    mc "Aren't you coming in?"
    la "I am, I am..."
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 11_674 at moveup
    pause 3
    mc "{i}(I wish there was a real-life slow-motion option!){/i}"
    scene 11_675 with Dissolve(1)
    la "..."
    la "Why are you all watching me take off my pants?"
    la "This isn't a free striptease!"
    la "Go talk to each other or something!"
    scene 11_676 with Dissolve(1)
    mc "Turn around, then."
    la "You think I'm stupid? You'll still be watching!"
    mc "Haha."
    scene 11_677 with Dissolve(1)
    mc "Hey!"
    el "Go ahead, Layla. I've got you."
    la "Thanks, El!"
    mc "That's not fair! Isn't this what hot tub parties are all about? Watching pretty girls in bikinis?"
    if Elena_Points >= 31:
        scene 11_678 with Dissolve(1)
        el "*Whispers* Here! See this as a thank you for yesterday."
        mc "*Whispers* You're quickly becoming my favourite, Elena!"
        mc "*Whispers* Thanks."
        el "..."
        scene 11_679 with Dissolve(1)
        mc "{i}(And where is the repeat option?){/i}"
    else:
        pass
    scene 11_680 with Dissolve(1)
    la "Hmm..."
    scene 11_681 with Dissolve(1)
    la "You're right. The water is colder than I expected."
    la "Want me to put the heater on?"
    mc "For me it's fine. But if you're too cold, put it on."
    scene 11_682 with Dissolve(1)
    mc "Now that we're all in here, this is a big hot tub."
    mc "We're five and there's easily enough space for another five to be comfortable in here."
    mc "You should've invited more people, Layla."
    la "I did."
    scene 11_683 with Dissolve(1)
    la "I invited Val but she couldn't make it."
    la "Kenz is on vacation. As is Zach."
    la "Daniela wasn't interested."
    mc "{i}(I don't even know who that is.){/i}"
    la "Alexis will maybe come later though, after her shift."
    scene 11_684 with Dissolve(1)
    mc "You need more friends, Layla."
    la "I have plenty! How many friends do you have?"
    mc "Haha. Touché."
    scene 11_685 with Dissolve(1)
    mc "But I don't need many friends. I've got you two!"
    mc "Right?"
    el "See! That's exactly what I said a few weeks back at school."
    el "Now we're stuck with him."
    scene 11_686 with Dissolve(1)
    mc "Forever!"
    el "Dios mío..."
    mc "I love you too, Elena!"
    el "..."
    scene 11_687 with Dissolve(1)
    la "Wait. Is that what Dios mío means?"
    mc "Dios mío... So much for those tutoring lessons..."
    el "I hope you're joking, Layla! I really hope you're joking!"
    la "Haha. I am, I am..."
    scene 11_688 with Dissolve(1)
    mc "What is the most people that were in here?"
    la "I think it was twelve."
    mc "Twelve? When was that?"
    scene 11_689 with Dissolve(1)
    la "Alexis's eighteenth birthday."
    mc "That must have been quite the party."
    la "Yeah. It was fun."
    scene 11_690 with Dissolve(1)
    la "Shall we play a game?"
    mc "Sure. What game?"
    la "Try the alphabet game again?"
    mc "The one we played on the bus?"
    la "Yes."
    scene 11_691 with Dissolve(1)
    mc "Let's change the rules though."
    la "To what?"
    mc "First of all. No boys against girls!"
    la "Haha. Okay."
    scene 11_692 with Dissolve(1)
    mc "Then instead of one person getting a letter, everyone needs to name something for that letter."
    mc "And the people who can't name anything, need to drink."
    la "Hmm... That's fine for me."
    si "Same. But depending on the topic, some may get drunk real quick."
    mc "True. Any idea for a topic? Something different than animals."
    scene 11_693 with Dissolve(1)
    ih "We can do movies."
    el "Bands?"
    si "Celebrities maybe?"
    la "I vote for celebrities. That sounds fun. First or last name?"
    si "Either? And if someone comes up with a celebrity whose first and last name starts with the same letter, everyone needs to drink."
    scene 11_694 with Dissolve(1)
    la "I'll start. Anne Hathaway."
    mc "Ana de Armas."
    ih "Noo!"
    mc "Haha, what? That was also your pick?"
    scene 11_695 with Dissolve(1)
    si "She's his favourite actress."
    mc "I have a thing for her too. She's so hot."
    ih "Right?"
    la "..."
    scene 11_696 with Dissolve(1)
    el "Antonio Banderas."
    si "Ariana Grande."
    ih "Hmm... I was so focused on Ana de Armas that I can't think of someone else now..."
    scene 11_697 with Dissolve(1)
    ih "Fuck it."
    mc "First round and someone has to drink already."
    mc "Sienna. You were right. Someone's gonna get drunk quick."
    scene black with Dissolve(1)
    pause 2
    scene 11_698 with Dissolve(1)
    el "Leonardo DiCaprio."
    si "Johnny Depp."
    ih "Matt Damon."
    scene black with Dissolve(1)
    pause 2
    scene 11_699 with Dissolve(1)
    la "Hugh Jackman."
    mc "Harry Potter."
    el "Haha."
    la "That doesn't count!"
    scene 11_700 with Dissolve(1)
    mc "Why not? He's famous."
    la "He isn't real, and the actor's name isn't Harry Potter..."
    mc "Henry Cavill then."
    la "No! You've gotta drink 'cause you're trying to cheat."
    mc "I wasn't trying to cheat!"
    scene black with Dissolve(1)
    pause 2
    scene 11_701 with Dissolve(1)
    la "Rachel McAdams."
    mc "Madonna."
    el "I can't believe neither of you said this one."
    el "Marilyn Monroe."
    mc "Oh yeah..."
    el "And it's double M... Drink up!"
    scene 11_702 with Dissolve(1)
    mc "Thanks a lot, Elena..."
    la "Yeah! Thanks a lot, Elena!"
    el "Haha. You're welcome."
    scene 11_703 with Dissolve(1)
    si "My turn, right?"
    el "Yes."
    si "Bruno Mars."
    ih "Hmm... Mia Khalifa."
    mc "{i}(No, he didn't. Haha!){/i}"
    scene 11_704 with Dissolve(1)
    la "Who's that? Never heard of her. Is she even a celebrity?"
    mc "You could say..."
    la "You know her?"
    scene 11_705 with Dissolve(1)
    mc "Uhm... Well... I've seen some of her movies."
    la "Oh... So she's an actress?"
    mc "Hmmyeah...?"
    scene 11_706 with Dissolve(1)
    ih "Hahaha."
    mc "Haha."
    scene 11_707 with Dissolve(1)
    la "Why are you laughing? I don't believe you guys!"
    la "Did you make her up, Isaiah? Or is it another Harry Potter character?"
    ih "Haha. Definitely not. But that'd be interesting though."
    mc "{i}(Oh man... You're a wizard, Harry.){/i}"
    la "Do you know her, El?"
    el "I don't."
    scene 11_708 with Dissolve(1)
    la "Let's look her up."
    mc "No!"
    la "So you guys admit you're cheating?"
    mc "We're not cheating!"
    scene 11_709 with Dissolve(1)
    la "I guess there's only one way..."
    mc "What? Where are you going?"
    scene 11_710 with Dissolve(1)
    la "I'm gonna get my phone!"
    mc "{i}(This is either gonna end up bad or hilarious.){/i}"
    scene 11_711 with Dissolve(1)
    el "You look nervous."
    mc "Me? Nervous? I'm not. Why should I be nervous?"
    el "Mm-hmm..."
    scene 11_712 with Dissolve(1)
    la "What was her name again? Mia?"
    el "Khalifa."
    la "How do you spell that?"
    el "Probably the same as the rapper."
    scene 11_713 with Dissolve(1)
    la "..."
    el "You found something?"
    la "..."
    el "Layla?"
    scene 11_714 with Dissolve(1)
    la "Here. Look for yourself."
    el "Alright."
    scene 11_715 with Dissolve(1)
    el "Oh... She's a pornstar."
    el "And seems like she's famous. I guess it counts."
    el "Now you know he's watching porn, Sienna."
    scene 11_716 with Dissolve(1)
    si "I knew that already. I've caught him before."
    ih "You watch porn too!"
    si "Everyone does."
    la "I don't."
    scene 11_717 with Dissolve(1)
    mc "You're watching that Entanglement TV show. That's basically porn. All those sex scenes..."
    la "No! That's not the same!"
    mc "So you've really never watched a porn video?"
    la "No."
    scene 11_718 with Dissolve(1)
    mc "Care to prove it?"
    la "How can I prove that?"
    mc "Can I look at your browser history on your phone?"
    scene 11_719 with Dissolve(1)
    la "..."
    mc "Not so sure anymore?"
    la "I am! Just..."
    scene 11_720 with Dissolve(1)
    la "Never mind. Here."
    mc "Thanks."
    mc "{i}(I didn't expect her to give me her phone. That's like sacred for most people.){/i}"
    scene 11_721 with Dissolve(1)
    mc "{i}(Let's see...){/i}"
    la "..."
    mc "Don't worry. I won't look anywhere else."
    scene 11_722 with Dissolve(1)
    mc "That was quick. Found something already."
    la "What?"
    mc "In fact today!"
    la "Can't be..."
    scene 11_723 with Dissolve(1)
    mc "Mia Khalifa."
    la "That's because I just looked her up for the game, you idiot!"
    mc "Haha."
    la "That clearly doesn't count!"
    mc "I know, I know."
    scene 11_724 with Dissolve(1)
    mc "{i}(Oh... Here's something.){/i}"
    mc "{i}(How to give a blowjob.){/i}"
    menu:
        "Tell the group[KoGa3AutoWTChange1]{size=-4}(Layla Points-8) {/size} {/color}":
            $ Layla_Points -= 8
            scene 11_726 with Dissolve(1)
            mc "How to give a blowjob..."
            la "What... No..."
            la "No! That... That isn't..."
            scene 11_727 with Dissolve(1)
            la "I was just..."
            la "This is so embarrassing!"
            scene 11_728 with Dissolve(1)
            mc "Layla, wait!"
            el "Lays..."
            scene 11_729 with Dissolve(1)
            mc "Sorry. I wanted to make it sound funny. Clearly, I failed."
            mc "And you have nothing to be embarrassed about."
            mc "We all watch these kinds of videos. Probably much worse ones."
            scene 11_730 with Dissolve(1)
            mc "Forgive me?"
            la "..."
            la "No!"
            scene 11_731 with Dissolve(1)
            mc "No?"
            la "Haha. [mc]!"
            scene 11_732 with Dissolve(1)
            la "Aaah..."
            mc "Let's go back to the hot tub. I mean cold tub!"
            la "Haha."
        "Keep it to yourself":
            mc "{i}(She probably didn't see this as porn but more for... Educational purposes, I guess?){/i}"
            mc "{i}(This girl...){/i}"
            scene 11_725 with Dissolve(1)
            mc "She's clean."
            la "I told you!"
            mc "Here you go."
            la "Thanks."
    scene black with Dissolve(2)
    pause 2
    scene 11_733 with Dissolve(1)
    mc "My turn? Uhm..."
    mc "What do the Mafia and pussies have in common?"
    mc "One slip of the tongue, and you’re in deep shit."
    el "Haha. Ew..."
    scene 11_734 with Dissolve(1)
    si "What's the difference between being hungry and being horny?"
    si "Where you put the cucumber."
    la "SIENNA!"
    mc "Haha."
    scene 11_735 with Dissolve(1)
    ih "I've got a good one."
    ih "What is 6.9?"
    ih "A great time, interrupted by a period."
    mc "Haha. Haven't heard that one before."
    el "That's disgusting."
    scene 11_736 with Dissolve(1)
    la "Hmm... I don't get it."
    mc "Uh, it's about the sex position 69 and being on your period."
    la "Ah..."
    mc "You still don't get it, huh?"
    scene 11_737 with Dissolve(1)
    la "I don't know what sex position 69 is."
    mc "Are you serious?"
    la "Do you know all the positions and their numbers? Like missionary is number fourteen or something?"
    mc "Haha. Layla! The position is called 69. It's not the..."
    scene 11_738 with Dissolve(1)
    mc "How about I show you instead of trying to explain?"
    la "Sure...?"
    if Elena_Points >= 31:
        menu:
            "Pick Layla[KoGa3AutoWTChange1]{size=-4}(Layla Week5 Tuesday Hottub 69, Layla Points+2) {/size} {/color}":
                $ Layla_Week5_Tuesday_Hottub_69 = True
                $ Layla_Points += 2
                # Layla (82)
                scene 11_739 with Dissolve(1)
                mc "Come on then."
                la "Wait... like now?"
                mc "Yes."
                scene 11_741 with Dissolve(1)
                la "What do I have to do?"
                mc "Lie on top of me."
                scene 11_742 with Dissolve(1)
                mc "{i}(I'm loving this already. But now I wish the others weren't here.){/i}"
                la "Is that it?"
                la "I still don't get it."
                scene 11_743 with Dissolve(1)
                mc "Heh..."
                mc "This is missionary. Now we need to make it 69."
                mc "Turn around."
                scene 11_744 with Dissolve(1)
                mc "..."
                la "Like this?"
                mc "Are you doing this on purpose?"
                la "What?"
                scene 11_745 with Dissolve(1)
                la "You said to turn around."
                mc "Yeah..."
                mc "I guess that's on me."
                scene 11_746 with Dissolve(1)
                mc "Your butt needs to be where my face is."
                la "..."
                scene 11_747 with Dissolve(1)
                la "Like this then?"
                mc "Yes, exactly. This is 69!"
                scene 11_748 with Dissolve(1)
                mc "{i}(This is such a turn on.){/i}"
                mc "{i}(I wouldn't mind if she would just sit on my face right now so I can taste her!){/i}"
                scene 11_749 with Dissolve(1)
                la "Oh..."
                mc "What?"
                la "I get it now! Why would anyone do that while... Just Ew..."
                mc "That's the joke."
                scene 11_750 with Dissolve(1)
                ih "This just gave me an idea for a game."
                ih "Why don't we give you the name of a sex position and you have to execute it."
                ih "If it's correct, you'll get a point. If you don't know it or get it wrong, you have to switch out."
                ih "The couple with the most points wins."
                scene 11_751 with Dissolve(1)
                mc "That sounds like fun. I'm in."
                la "Me too, but I'm not going first!"
                si "Let's rock-paper-scissors and switch pairs every round."
                scene black with Dissolve(1)
                pause 2
                scene 11_752 with Dissolve(1)
                mc "I guess it's us."
                el "Mm-hmm..."
                mc "{i}(I'm kinda excited to do this with Elena.){/i}"
            "Pick Elena[KoGa3AutoWTChange1]{size=-4}(Elena Week5 Tuesday Hottub 69, Elena Points+2) {/size} {/color}":
                $ Elena_Week5_Tuesday_Hottub_69 = True
                $ Elena_Points += 2
                # Elena (44)
                scene 11_740 with Dissolve(1)
                mc "Can you help out for a second, Elena?"
                el "Wait? What? Me? Take Layla. She wants to know how..."
                la "No, no, it's fine. You go, Elena! Then I can watch."
                el "..."
                scene 11_753 with Dissolve(1)
                el "*Sigh* Why do I always end up in this kind of situation?"
                mc "Hehe."
                scene 11_754 with Dissolve(1)
                el "Let's get this over with."
                mc "..."
                mc "{i}(I'm hard already.){/i}"
                scene 11_755 with Dissolve(1)
                el "No stupid comments, okay?"
                mc "I didn't say anything."
                scene 11_756 with Dissolve(1)
                mc "{i}(I'm thinking a lot of things, though.){/i}"
                mc "{i}(Damn, Elena!){/i}"
                mc "{i}(I want to push my face in between those buttcheeks so badly!){/i}"
                scene 11_757 with Dissolve(1)
                la "Oh..."
                la "I get it now! Why would anyone do that while... Just Ew..."
                si "Haha."
                scene 11_758 with Dissolve(1)
                el "About time!"
                el "I was getting worried we'd have to explain too, while demonstrating..."
                mc "{i}(I wouldn't have minded if this had taken longer.){/i}"
                scene 11_759 with Dissolve(1)
                ih "This just gave me an idea for a game."
                ih "Why don't we give you the name of a sex position and you have to execute it."
                ih "If it's correct, you'll get a point. If you don't know it or get it wrong, you have to switch out."
                ih "The couple with the most points wins."
                scene 11_760 with Dissolve(1)
                mc "That sounds like fun. I'm in."
                la "Me too, but I'm not going first!"
                si "Let's rock-paper-scissors and switch pairs every round."
                scene black with Dissolve(1)
                pause 2
                scene 11_752 with Dissolve(1)
                mc "I guess we can stay here."
                el "Mm-hmm..."
                mc "{i}(I'm kinda excited to keep doing this with Elena.){/i}"
    else:
        $ Layla_Week5_Tuesday_Hottub_69 = True
        $ Layla_Points += 2
        # Layla (84)
        scene 11_739 with Dissolve(1)
        mc "Come on then."
        la "Wait... like now?"
        mc "Yes."
        scene 11_741 with Dissolve(1)
        la "What do I have to do?"
        mc "Lie on top of me."
        scene 11_742 with Dissolve(1)
        mc "{i}(I'm loving this already. But now I wish the others weren't here.){/i}"
        la "Is that it?"
        la "I still don't get it."
        scene 11_743 with Dissolve(1)
        mc "Heh..."
        mc "This is missionary. Now we need to make it 69."
        mc "Turn around."
        scene 11_744 with Dissolve(1)
        mc "..."
        la "Like this?"
        mc "Are you doing this on purpose?"
        la "What?"
        scene 11_745 with Dissolve(1)
        la "You said to turn around."
        mc "Yeah..."
        mc "I guess that's on me."
        scene 11_746 with Dissolve(1)
        mc "Your butt needs to be where my face is."
        la "..."
        scene 11_747 with Dissolve(1)
        la "Like this then?"
        mc "Yes, exactly. This is 69!"
        scene 11_748 with Dissolve(1)
        mc "{i}(This is such a turn on.){/i}"
        mc "{i}(I wouldn't mind if she would just sit on my face right now so I can taste her!){/i}"
        scene 11_749 with Dissolve(1)
        la "Oh..."
        mc "What?"
        la "I get it now! Why would anyone do that while... Just Ew..."
        mc "That's the joke."
        scene 11_750 with Dissolve(1)
        ih "This just gave me an idea for a game."
        ih "Why don't we give you the name of a sex position and you have to execute it."
        ih "If it's correct, you'll get a point. If you don't know it or get it wrong, you have to switch out."
        ih "The couple with the most points wins."
        scene 11_751 with Dissolve(1)
        mc "That sounds like fun. I'm in."
        la "Me too, but I'm not going first!"
        si "Let's rock-paper-scissors and switch pairs every round."
        scene black with Dissolve(1)
        pause 2
        scene 11_752 with Dissolve(1)
        mc "I guess it's us."
        el "Mm-hmm..."
    scene 11_761 with Dissolve(1)
    ih "Let's start off with an easy one."
    ih "Cowgirl."
    mc "Yeah, that's an easy point. Let's go, Elena."
    if Elena_Points >= 33:
        scene 11_762 with Dissolve(1)
        mc "{i}(Shit!){/i}"
        mc "{i}(Maybe this won't be as easy as I thought.){/i}"
        scene black with Dissolve(1)
        transform moveup:
            xalign 0.5 yalign 1.0
            linear 5.0 yalign 0.0
        show 11_763 at moveup
        pause 3
        mc "..."
    else:
        pass
    scene 11_764 with Dissolve(1)
    el "Cowgirl done!"
    el "What's the next one?"
    if Elena_Points >= 33:
        mc "{i}(I don't know if she's into it or if she wants this to be over with quickly.){/i}"
    else:
        pass
    scene 11_765 with Dissolve(1)
    ih "Let's step it up a little."
    ih "Wheelbarrow!"
    el "Wheelbarrow?"
    scene 11_766 with Dissolve(1)
    el "I have no idea. I've never even heard of the wheelbarrow."
    el "Do you know it?"
    mc "I do. It's a bit like doggy but I'm standing up and holding your legs up as... Well... A wheelbarrow."
    el "Okay? What do I have to do?"
    mc "Just lie down on your stomach and I'll pick you up."
    scene 11_767 with Dissolve(1)
    mc "I'll grab your legs now and you push yourself up from the ground."
    el "Like a push-up?"
    mc "Exactly."
    scene 11_768 with Dissolve(1)
    mc "This is it, right?"
    ih "Yes! That's correct. Another point for you guys."
    si "Good job!"
    scene 11_769 with Dissolve(1)
    la "Now I know why they call this the wheelbarrow."
    la "This looks just like the wheelbarrow races we used to do when we were younger."
    mc "{i}(That's the stuff she thinks about in this situation?){/i}"
    el "..."
    el "This is so uncomfortable. Why do people wanna have sex like this?"
    if Elena_Points >= 33:
        scene 11_770 with Dissolve(1)
        mc "{i}(I know why!){/i}"
        mc "{i}(Fuck. I really want to try this.){/i}"
    else:
        pass
    scene 11_771 with Dissolve(1)
    ih "You pick a position now, Layla."
    la "I don't know any of those names. Sienna, you can go instead."
    si "Alright. Hmm..."
    si "The eagle!"
    ih "Good one! One of my favourites."
    scene 11_772 with Dissolve(1)
    mc "Eagle, huh?"
    el "Again. I have no idea."
    mc "Me neither this time. I guess that's it then? Two points."
    ih "Just try it. Do something."
    ih "If you're close enough it will still count and you'll get another point."
    scene 11_773 with Dissolve(1)
    mc "Wanna give it a shot then?"
    el "Why not?"
    mc "Let's think about it. Eagle. Bird. Flying. Wings?"
    mc "I'll lie on my back, you on top and we'll go from there?"
    el "Sure."
    scene 11_774 with Dissolve(1)
    if Elena_Points >= 33:
        el "*Whispers* You're enjoying this, huh? Good thing I'm used to it since you're always lying on top of me."
        mc "*Whispers* So are you! I can feel your hard nipples!"
        el "..."
    else:
        pass
    el "So, what now?"
    mc "Uhm... Maybe spread your arms out like wings?"
    scene 11_775 with Dissolve(1)
    el "Want me to flap them and kawkaw too?"
    mc "No. You're an eagle, not a raven!"
    el "Dios mío."
    la "Haha."
    mc "Do you have a better idea?"
    scene 11_776 with Dissolve(1)
    el "..."
    scene 11_777 with Dissolve(1)
    el "This is... This doesn't seem right."
    mc "This looks more like you're nailed to a cross... Well to me..."
    el "*Shakes head* Haha."
    ih "Yeah, it's not correct. But a good try."
    ih "You might be on to something new though."
    scene 11_778 with Dissolve(1)
    la "The Elena on a cross!"
    el "I can't wait for your turn, Layla!"
    mc "Were we at least somewhat close?"
    ih "No, not really."
    scene black with Dissolve(1)
    pause 2
    scene 11_779 with Dissolve(1)
    la "Nooo!"
    mc "Haha. That's Sienna and Layla as the next pair."
    el "Good luck!"
    scene 11_780 with Dissolve(1)
    mc "Let's start where we left off, I guess."
    mc "Show us the eagle!"
    scene 11_781 with Dissolve(1)
    la "I have no idea. I hope you do, Sienna?"
    si "I know it."
    la "Good! What shall I do?"
    si "Lie down on your back."
    scene 11_782 with Dissolve(1)
    la "This is kinda exciting!"
    mc "{i}(I couldn't agree more.){/i}"
    scene 11_783 with Dissolve(1)
    la "Haha, Sienna. I didn't know you were this rough."
    si "Haha."
    mc "..."
    mc "{i}(That's so fucking hot!){/i}"
    scene 11_784 with Dissolve(1)
    si "That's basically it."
    mc "{i}(I think I've done that before.){/i}"
    ih "Yes. Point for Layla and Sienna."
    la "Yay! Two more to go, Sienna!"
    mc "We weren't that far off though, to be honest. Right, Elena?"
    scene 11_785 with Dissolve(1)
    el "Well..."
    el "Instead of the arms, the legs needed to be spread and you had to be on top."
    if Elena_Points >= 33:
        mc "{i}(Yes! Keep on talking dirty to me, Elena!){/i}"
    else:
        pass
    mc "Anyway. You can pick the next position."
    el "Can I use my phone? I don't know all their names."
    mc "Sure. I don't know them either. I'd have to look them up too."
    scene 11_786 with Dissolve(1)
    el "*Whispers* How about this one here?"
    mc "*Whispers* That looks like a fun one."
    la "Why are you whispering?"
    scene 11_787 with Dissolve(1)
    el "We want to see the spider!"
    la "Spider? Do all of them have animal names?"
    ih "No, just a few. It's a good one, but Sienna knows it."
    mc "Oh? She does?"
    mc "{i}(I didn't expect Sienna to be so... experienced?){/i}"
    scene 11_788 with Dissolve(1)
    la "Haha. Easy points! I like having you as my partner!"
    si "Hehe."
    la "Can I be the guy this time?"
    si "Sure. But it's almost the same for both. Just do as I do."
    scene 11_789 with Dissolve(1)
    la "Haha. This is like doing the crabwalk."
    mc "{i}(There she goes again with her games...){/i}"
    si "It is!"
    la "Maybe they should have called it the crab instead of the spider."
    scene 11_790 with Dissolve(1)
    mc "Spiders have eight legs. Your four arms and four legs make eight."
    mc "I don't know how many legs crabs have. Six?"
    el "Ten."
    mc "Really? That many?"
    scene 11_791 with Dissolve(1)
    la "I can see the appeal for men in this position."
    la "Even I'm starting to blush, looking at you, Sienna."
    si "Haha. Thanks."
    scene black with Dissolve(1)
    pause 2
    scene 11_792 with Dissolve(1)
    mc "Good job, you guys."
    ih "That's four points for team Layla and Sienna!"
    la "Yay! Thank you, Sienna! Couldn't have done it without you!"
    si "You're welcome. You did great too!"
    ih "Let's see the next pairing."
    scene 11_793 with Dissolve(1)
    mc "..."
    ih "..."
    scene 11_794 with Dissolve(1)
    mc "Two bros..."
    ih "Haha."
    mc "Yeah, that's not going to happen!"
    scene 11_795 with Dissolve(1)
    la "What do you mean it's not going to happen?"
    mc "Well, uhm... We're two guys. That'd be... weird, to say the least."
    la "We were two girls before, and we did it!"
    mc "Two girls is different."
    scene 11_796 with Dissolve(1)
    el "No, it's not!"
    la "Exactly. Guys always think that way."
    la "But for us girls, it's just the same..."
    mc "..."
    scene 11_797 with Dissolve(1)
    mc "Alright, alright. Fair is fair."
    mc "But only one!"
    la "That's fine."
    scene 11_798 with Dissolve(1)
    la "We wanna see doggy!"
    mc "{i}(No, she didn't...){/i}"
    mc "Doggy!?"
    la "Uh-huh."
    mc "..."
    scene 11_799 with Dissolve(1)
    mc "Why are you guys smiling like that? And I can see you hiding your phone, Layla!"
    la "That... I... I just have that to look up positions, as you did before."
    mc "You didn't look up anything. You immediately said doggy! You were going to record us!"
    la "I..."
    scene 11_800 with Dissolve(1)
    mc "Come here!"
    mc "We'll show you some doggy!"
    la "Aaah!"
    ih "Nowhere to run, Sienna!"
    scene 11_801 with Dissolve(1)
    ""
    scene 11_802 with Dissolve(1)
    mc "Gotcha!"
    la "Nooo! Haha."
    mc "You like doggy?"
    la "Haha, [mc]!"
    scene 11_803 with Dissolve(1)
    la "Elena, help!"
    el "Don't get me involved. It was your idea to take the picture!"
    if Elena_Points >= 33:
        mc "She won't help you. She'll suffer the same fate!"
        el "What?"
        scene 11_804 with Dissolve(1)
        mc "You thought you'd get off scot-free?"
        mc "You get some doggy too!"
        el "[mc]..."
        el "Don't you dare!"
        scene 11_805 with Dissolve(1)
        mc "{i}(The risk will be worth it!){/i}"
        mc "{i}(Just look at that ass!){/i}"
        scene 11_806 with Dissolve(1)
        el "[mc]! Haha."
        scene 11_807 with Dissolve(1)
        la "Don't worry, I'll save you, Elena!"
        mc "Haha."
        el "You're squishing me!"
        scene 11_808 with Dissolve(1)
        el "I thought you were on my side?"
        la "I am! I'm beating him at his own doggy game!"
        mc "A doggy sandwich."
        la "Haha."
    else:
        pass
    scene black with Dissolve(1)
    pause 2
    scene 11_809 with Dissolve(1)
    el "I guess we gave him the perfect name."
    la "Yeah?"
    el "Perrito."
    la "Haha. You're right."
    mc "Haha."
    if Elena_Points >= 33:
        scene 11_811 with Dissolve(1)
        la "My little perrito!"
        el "..."
    else:
        scene 11_810 with Dissolve(1)
        la "My little perrito!"
        mc "..."
    scene 11_812 with Dissolve(1)
    ih "I need a quick bathroom break. Layla, can you tell me where the bathroom is?"
    la "If you..."
    si "I can show him. I have to go too."
    la "That works too."
    scene 11_813 with Dissolve(1)
    la "They're such a cute couple, right?"
    el "Mm-hmm. They're good together."
    la "What do you think of Isaiah?"
    menu:
        "Cool dude":
            scene 11_814 with Dissolve(1)
            mc "He seems like a cool dude."
            mc "He's funny. Has good chat."
            mc "He's punching a little though."
            el "A little?"
            la "Haha, Elena. She's happy, though."
        "Don't know yet":
            scene 11_815 with Dissolve(1)
            mc "I don't know yet, to be honest."
            la "Hmm? Seems like you get along, though."
            mc "We do but you never know. It's the first time meeting him."
            mc "And I've been wrong about a few people already, so..."
    scene 11_816 with Dissolve(1)
    mc "El, can you hand me the wine, please?"
    el "You're drinking wine now?"
    mc "We're out of beer, so yeah."
    la "We still have some in the fridge in the kitchen. I'll get them."
    scene 11_817 with Dissolve(1)
    mc "No, it's fine. I'll go."
    mc "Want me to get something else?"
    la "You can also bring another wine bottle. Or two."
    mc "Will do."
    scene 11_818 with Dissolve(1)
    mc "Don't have too much fun without me."
    el "This is the moment we've been waiting for."
    la "Mm-hmm. This was all a setup to be alone with Elena."
    mc "Is that right?"
    scene 11_819 with Dissolve(1)
    el "..."
    la "..."
    scene 11_820 with Dissolve(1)
    la "Aaah..."
    el "What are... I thought you would pull away at the end."
    la "I thought you would!"
    mc "Haha."
    mc "{i}(They're hilarious when they're tipsy.){/i}"
    scene black with Dissolve(1)
    pause 2
    scene 11_821 with Dissolve(1)
    ""
    scene 11_822 with Dissolve(1)
    mc "{i}(Does it matter which one I take?){/i}"
    mc "..."
    mc "{i}(Some of them might be really expensive...){/i}"
    mc "{i}(This one is from Australia. Does Australia have good wine?){/i}"
    mc "{i}(Must be. Why would you import it otherwise...? Let's look for something else.){/i}"
    scene 11_823 with Dissolve(1)
    n "*Whispering noises*"
    mc "{i}(Who's that?){/i}"
    menu:
        "Go back":
            mc "{i}(Whatever...){/i}"
            jump Week5_Tuesday_Layla_Hottub_End
        "Check it out[KoGa3AutoWTChange1]{size=-4}(Sienna Week5 Tuesday Hottub Sex) {/size} {/color}":
            $ Sienna_Week5_Tuesday_Hottub_Sex = True
            mc "{i}(Damn... Why must I be so curious all the time?){/i}"
            jump Week5_Tuesday_Layla_Hottub_Sienna

label Week5_Tuesday_Layla_Hottub_Sienna:
    scene 11_824 with Dissolve(1)
    mc "{i}(Oh shit...){/i}"
    mc "{i}(It's Sienna and Isaiah...){/i}"
    scene 11_825 with Dissolve(1)
    mc "{i}(Are they really having sex right here?){/i}"
    scene 11_826 with Dissolve(1)
    si "Mmm..."
    mc "{i}(They are one kinky couple...){/i}"
    mc "{i}(No wonder they know so many sex positions.){/i}"
    scene 11_827 with Dissolve(1)
    ih "Look at this gorgeous pussy!"
    si "Don't just look! I'm horny."
    scene 11_828 with Dissolve(1)
    si "*Moaning*"
    mc "{i}(I never expected this of Sienna.){/i}"
    mc "{i}(I always thought she was a quiet girl.){/i}"
    scene 11_829 with Dissolve(1)
    si "Yeah. Right there."
    mc "{i}(But then again, at training camp, she had no issue licking my nipple.){/i}"
    scene 11_830 with Dissolve(1)
    ih "Seeing you doing those positions with Layla was so hot!"
    ih "Such a turn-on!"
    scene 11_831 with Dissolve(1)
    si "Ahh..."
    ih "I saw you were turned on by her, too!"
    show 11_832
    ""
    show 11_833
    mc "{i}(Why am I enjoying watching those two having sex?){/i}"
    mc "{i}(I should just leave...){/i}"
    mc "{i}(But I can't...){/i}"
    scene 11_834 with Dissolve(1)
    ih "Turn around! Let's do doggy!"
    mc "{i}(Heh...){/i}"
    si "Be quick though. We can't be gone for too long."
    scene 11_835 with Dissolve(1)
    ih "I love this cute little butt of yours."
    scene 11_836 with Dissolve(1)
    si "Mmm..."
    si "Fuck me hard!"
    show 11_837
    mc "{i}(I'd better head back before they notice I'm watching them.){/i}"
    mc "{i}(Let them have their fun.){/i}"
    mc "{i}(But damn... Unexpected!){/i}"
    $ renpy.end_replay()
    jump Week5_Tuesday_Layla_Hottub_End

label Week5_Tuesday_Layla_Hottub_End:
    scene black with Dissolve(1)
    pause 2
    scene 11_838 with Dissolve(1)
    if Sienna_Week5_Tuesday_Hottub_Sex == True:
        la "What took you so long?"
        mc "Uhm..."
        mc "Lots of wine bottles to choose from."
    else:
        la "Did you find anything?"
        mc "Yeah. There were a lot of bottles. Didn't know which I could or couldn't take."
        mc "I found an opened one though."
    scene 11_839 with Dissolve(1)
    el "Cheers."
    la "Cheers!"
    scene 11_840 with Dissolve(1)
    la "They've been gone a while."
    mc "Maybe they're having trouble finding the bathroom."
    la "Sienna should know. She's been here before. Should I go check?"
    mc "Just give them a few more minutes."
    scene black with Dissolve(1)
    pause 2
    scene 11_841 with Dissolve(1)
    si "We're back."
    la "Finally!"
    la "Wait! Why are you dressed? Don't tell me you..."
    scene 11_842 with Dissolve(1)
    ih "Sorry. Something came up and I have to go."
    if Sienna_Week5_Tuesday_Hottub_Sex == True:
        mc "{i}(Something definitely came up...){/i}"
    else:
        pass
    la "Already? Can't you stay a bit longer?"
    ih "Sorry."
    scene 11_843 with Dissolve(1)
    mc "Was nice to meet you, Isaiah."
    ih "You too, [mc]. Let's hang out sometime."
    mc "Sure."
    la "Bye, Sienna. We'll see each other over the weekend?"
    si "Yeah. See you then."
    scene 11_844 with Dissolve(1)
    la "*Sigh* I didn't expect them to have to leave this early."
    la "So, what now?"
    la "Do you have to leave too, and shall we continue this another time?"
    mc "No. I've plenty of time. We can still have fun with the three of us."
    if Elena_Points >= 33:
        menu:
            "Grab Layla[KoGa3AutoWTChange1]{size=-4}(Layla Week5 Tuesday Hottub Grab, Layla Points+2) {/size} {/color}":
                $ Layla_Week5_Tuesday_Hottub_Grab = True
                $ Layla_Points += 2
                # Layla (86)
                scene 11_845 with Dissolve(1)
                la "Hey!"
                la "What are you doing?"
                mc "Getting you back in the water!"
                scene 11_846 with Dissolve(1)
                la "That's not the way to the hot tub."
                mc "We're not going to the hot tub! I've always wanted to try out your pool."
                la "What? [mc]!"
                scene 11_847 with Dissolve(1)
                la "Elena! Help!"
                el "You're on your own."
                el "Remember training camp?"
                la "You bitch!"
                el "Haha."
                scene 11_848 with Dissolve(1)
                la "[mc]! Haha."
                scene 11_849 with Dissolve(1)
                la "..."
                scene 11_850 with Dissolve(1)
                la "Aaah!"
                mc "Haha. You wanna fight again?"
                scene 11_851 with Dissolve(1)
                la "I'll get you this time!"
                mc "{i}(You can get me all you want.){/i}"
                scene 11_852 with Dissolve(1)
                la "Elena, come help me."
                el "You're doing fine just on your own."
                scene 11_853 with Dissolve(1)
                la "*Whispers* Hey."
                mc "Hmm?"
                la "*Whispers* I have an idea."
                el "I can still hear you!"
                scene 11_854 with Dissolve(1)
                el "..."
                scene 11_855 with Dissolve(1)
                el "What do you think you're doing?"
                mc "Sorry, Elena. I have to."
                el "You have to what? Make a mistake?"
                mc "Hah..."
                scene 11_856 with Dissolve(1)
                el "You'd better let go of me!"
                el "This won't end up well for you!"
                mc "..."
                mc "Now I want to do it even more."
                scene 11_857 with Dissolve(1)
                el "[mc]!"
                scene 11_858 with Dissolve(1)
                el "Nooo..."
                scene 11_859 with Dissolve(1)
                el "Qué cabrón!"
                scene 11_860 with Dissolve(1)
                mc "..."
                scene 11_861 with Dissolve(1)
                el "[mc]!"
                el "You're so gonna regret this!"
                mc "Haha."
                el "Por qué te ríes?\n Why are you laughing?"
                mc "Lo siento. No puedo tomarte en serio con ese pelo.\n Sorry. I just can't take you seriously with that hair."
                scene 11_862 with Dissolve(1)
                el "You!"
                mc "Haha."
                mc "{i}(They are so different but similar at the same time...){/i}"
                scene 11_863 with Dissolve(1)
                el "And you!"
                el "I haven't forgotten about you!"
                la "Haha."
                scene 11_864 with Dissolve(1)
                el "And why are you laughing now?"
                la "That's what you get for stealing the towel!"
                el "What?"
                el "Yeah... About that towel!"
                scene 11_865 with Dissolve(1)
                el "How dare you make a towel from that picture!"
                la "Haha."
                el "And even worse, give it to [mc]!"
                la "He liked it, though."
                scene 11_866 with Dissolve(1)
                la "We can take a new picture and..."
                el "No! No pictures! No towels!"
                la "Haha."
                mc "{i}(I can watch this all day.){/i}"
                if Elena_Points >= 33:
                    scene 11_867 with Dissolve(1)
                    mc "{i}(Especially this.){/i}"
                    mc "{i}(You have a great ass, Elena!){/i}"
                else:
                    pass
                scene 11_868 with Dissolve(1)
                el "What are you looking at?"
                mc "Uhm... Nothing..."
                mc "I'm just happy you're fighting each other this time and not ganging up against me."
                scene 11_869 with Dissolve(1)
                el "..."
                la "..."
                scene 11_870 with Dissolve(1)
                la "Aaah!"
                mc "Haha. I should've kept my mouth shut."
                mc "{i}(Who am I kidding? I'm loving this.){/i}"
            "Grab Elena[KoGa3AutoWTChange1]{size=-4}(Elena Week5 Tuesday Hottub Grab, Elena Points+2) {/size} {/color}":
                $ Elena_Week5_Tuesday_Hottub_Grab = True
                $ Elena_Points += 2
                # Elena (46)
                scene 11_871 with Dissolve(1)
                el "Hey!"
                el "What are you doing?"
                mc "Getting you back in the water!"
                la "Haha."
                scene 11_872 with Dissolve(1)
                el "No you don't!"
                el "Remember training camp? It's gonna be worse this time!"
                mc "Haha."
                el "Just laugh. You'll regret this soon!"
                scene 11_873 with Dissolve(1)
                la "Don't worry, El. I'll save you!"
                scene 11_874 with Dissolve(1)
                la "Grab my hand!"
                mc "Too late!"
                scene 11_875 with Dissolve(1)
                el "Aaah!"
                la "ELENA!"
                scene 11_876 with vpunch
                mc "..."
                scene 11_877 with Dissolve(1)
                mc "{i}(I'm so dead.){/i}"
                scene 11_878 with Dissolve(1)
                mc "Are you okay?"
                el "..."
                mc "Haha. Why are you looking so mad?"
                scene 11_879 with Dissolve(1)
                el "I told you, you're going to regret this!"
                mc "Haha. There she is!"
                scene 11_870 with Dissolve(1)
                mc "Of course you're ganging up on me again."
                la "You should've thought about that before you threw us in the pool."
                mc "You jumped in by yourself!"
                la "To save Elena!"
                mc "Haha. 'Save'."
                scene 11_880 with Dissolve(1)
                la "We've got him again, Elena."
                mc "{i}(Since we're in the water this time. I think I can be a little rougher with them.){/i}"
                mc "{i}(No more letting them win!){/i}"
                scene 11_881 with Dissolve(1)
                la "Hey!"
                mc "Layla take-off number two!"
                la "What number two?"
                scene 11_882 with Dissolve(1)
                mc "Lift off!"
                la "Aaah-haha..."
                scene 11_883 with Dissolve(1)
                mc "Don't worry. I haven't forgotten about you, my little spider monkey."
                el "Spider monkey?"
                el "Have you seen Twilight?"
                mc "Uhm... No!"
                el "You have!"
                scene 11_884 with Dissolve(1)
                mc "Let's see if you can keep holding on."
                el "Don't change the subject and aaah!"
                scene 11_885 with Dissolve(1)
                el "You've gotta do better than that, Edward!"
                mc "Oh shut up!"
                la "Hold on, Elena! I'm coming!"
                scene 11_886 with Dissolve(1)
                el "Haha."
                mc "{i}(I haven't done a shoulder press in a while.){/i}"
                mc "{i}(But Elena weighs like nothing.){/i}"
                scene 11_887 with Dissolve(1)
                el "Aaah!"
                la "ELENA!"
                mc "You'd better watch out, Layla."
                scene 11_888 with Dissolve(1)
                mc "..."
                mc "{i}(I didn't even realise where I was touching her.){/i}"
                scene 11_889 with Dissolve(1)
                el "[mc]!"
                la "I want to do that too..."
                scene 11_890 with Dissolve(1)
                mc "You okay?"
                el "That was fun!"
                el "[mc], you should..."
                mc "No! Not joining!"
                el "Haha."
                scene 11_891 with Dissolve(1)
                la "Round two!"
                mc "Just give up already."
                la "Never!"
    else:
        $ Layla_Week5_Tuesday_Hottub_Grab = True
        $ Layla_Points += 2
        # Layla (86)
        scene 11_845 with Dissolve(1)
        la "Hey!"
        la "What are you doing?"
        mc "Getting you back in the water!"
        scene 11_846 with Dissolve(1)
        la "That's not the way to the hot tub."
        mc "We're not going to the hot tub! I've always wanted to try out your pool."
        la "What? [mc]!"
        scene 11_847 with Dissolve(1)
        la "Elena! Help!"
        el "You're on your own."
        el "Remember training camp?"
        la "You bitch!"
        el "Haha."
        scene 11_848 with Dissolve(1)
        la "[mc]! Haha."
        scene 11_849 with Dissolve(1)
        la "..."
        scene 11_850 with Dissolve(1)
        la "Aaah!"
        mc "Haha. You wanna fight again?"
        scene 11_851 with Dissolve(1)
        la "I'll get you this time!"
        mc "{i}(You can get me all you want.){/i}"
        scene 11_852 with Dissolve(1)
        la "Elena, come help me."
        el "You're doing fine just on your own."
        scene 11_853 with Dissolve(1)
        la "*Whispers* Hey."
        mc "Hmm?"
        la "*Whispers* I have an idea."
        el "I can still hear you!"
        scene 11_854 with Dissolve(1)
        el "..."
        scene 11_855 with Dissolve(1)
        el "What do you think you're doing?"
        mc "Sorry, Elena. I have to."
        el "You have to what? Make a mistake?"
        mc "Hah..."
        scene 11_856 with Dissolve(1)
        el "You'd better let go of me!"
        el "This won't end up well for you!"
        mc "..."
        mc "Now I want to do it even more."
        scene 11_857 with Dissolve(1)
        el "[mc]!"
        scene 11_858 with Dissolve(1)
        el "Nooo..."
        scene 11_859 with Dissolve(1)
        el "Qué cabrón!"
        scene 11_860 with Dissolve(1)
        mc "..."
        scene 11_861 with Dissolve(1)
        el "[mc]!"
        el "You're so gonna regret this!"
        mc "Haha."
        el "Por qué te ríes?\n Why are you laughing?"
        mc "Lo siento. No puedo tomarte en serio con ese pelo.\n Sorry. I just can't take you seriously with that hair."
        scene 11_862 with Dissolve(1)
        el "You!"
        mc "Haha."
        mc "{i}(They are so different but similar at the same time...){/i}"
        scene 11_863 with Dissolve(1)
        el "And you!"
        el "I haven't forgotten about you!"
        la "Haha."
        scene 11_864 with Dissolve(1)
        el "And why are you laughing now?"
        la "That's what you get for stealing the towel!"
        el "What?"
        el "Yeah... About that towel!"
        scene 11_865 with Dissolve(1)
        el "How dare you make a towel from that picture!"
        la "Haha."
        el "And even worse. Give it to [mc]!"
        la "He liked it though."
        scene 11_866 with Dissolve(1)
        la "We can take a new picture and..."
        el "No! No pictures! No towels!"
        la "Haha."
        mc "{i}(I can watch this all day.){/i}"
        scene 11_868 with Dissolve(1)
        el "What are you looking at?"
        mc "Uhm... Nothing..."
        mc "I'm just happy you're fighting each other this time and not ganging up against me."
        scene 11_869 with Dissolve(1)
        el "..."
        la "..."
        scene 11_870 with Dissolve(1)
        la "Aaah!"
        mc "Haha. I should've kept my mouth shut."
        mc "{i}(Who am I kidding? I'm loving this.){/i}"
    scene black with Dissolve(1)
    pause 2
    scene 11_892 with Dissolve(1)
    mc "*Sigh* All that fighting made me hungry."
    mc "Do we still have some snacks?"
    la "No, we finished everything."
    la "But we can order something maybe?"
    mc "Sounds good."
    scene 11_893 with Dissolve(1)
    la "Alright. Let's see."
    la "We've got a few options here."
    mc "Let's hear them."
    scene 11_894 with Dissolve(1)
    la "We have pizza."
    la "Chinese takeout."
    la "Burgers."
    if Elena_Points >= 33:
        scene 11_895 with Dissolve(1)
        mc "Oh, burgers. I want one of those Elena buns... Burgers."
        el "..."
        mc "I still regret that I said no."
        el "Haha."
        la "What?"
        scene 11_896 with Dissolve(1)
        el "When [mc] was at my place, I made burgers for the boys."
        el "I offered to make one for [mc] but he, regretfully, said no."
        la "Oh..."
        mc "Yeah, just rub it in."
        scene 11_897 with Dissolve(1)
        el "I'll make some for you next time, okay?"
        mc "Yes, please!"
    else:
        pass
    scene 11_898 with Dissolve(1)
    mc "What else?"
    la "Hmm... Chicken wings, tacos..."
    la "We can also get something from Sandwish."
    scene 11_899 with Dissolve(1)
    mc "That's such a stupid name for a sandwich shop."
    mc "The owner probably wanted to call it 'The Sandwich Bar' or something."
    mc "But he misspelt sandwich with sandwish on his application and just went with it."
    mc "'At Sandwish, we make all your sandwich wishes come true...' So stupid!"
    scene 11_900 with Dissolve(1)
    el "Haha. The things you think about sometimes."
    la "Haha."
    scene 11_901 with Dissolve(1)
    la "So no sandwiches. What do you guys want?"
    el "I vote for chicken wings."
    mc "I'm good with chicken wings."
    scene 11_902 with Dissolve(1)
    la "They have several here."
    la "Classic, barbeque, honey soy, hot spicy..."
    mc "The spicy one!"
    el "I agree."
    scene 11_903 with Dissolve(1)
    la "I'm not good with spicy food."
    mc "Let's get two servings then. One spicy and one whatever you want."
    la "I can't finish them by myself."
    mc "Don't worry. I'll eat the rest."
    scene 11_904 with Dissolve(1)
    la "Are you okay with the classic one?"
    mc "As I said, whatever you want."
    la "Alright. I'll order then."
    scene 11_905 with Dissolve(1)
    la "The food will be here in twenty-two minutes."
    mc "Will we hear the doorbell from here?"
    la "No. I'll..."
    mc "It's fine. I'll go wait at the door, then."
    la "Thanks."
    scene black with Dissolve(1)
    pause 2
    scene 11_906 with Dissolve(1)
    n "*Ding-dong*"
    mc "{i}(Perfect timing!){/i}"
    scene 11_907 with Dissolve(1)
    mc "..."
    da "..."
    scene 11_908 with Dissolve(1)
    da "Here's your order."
    mc "Thanks."
    menu:
        "Take the food":
            scene 11_909 with Dissolve(1)
            da "That explains a lot!"
        "Tip him[KoGa3AutoWTChange1]{size=-4}(Darryl Points+2) {/size} {/color}":
            $ Darryl_Points += 2
            # Darryl (4)
            scene 11_910 with Dissolve(1)
            mc "Here you go."
            da "It's already paid."
            mc "I know. It's a tip."
            da "I don't need..."
            mc "For fuck's sake. Just take it, Darryl!"
            scene 11_911 with Dissolve(1)
            mc "By the way. Five stars!"
            da "Heh... Shut up!"
    scene 11_912 with Dissolve(1)
    mc "I've got the stuff!"
    la "Yay!"
    scene 11_913 with Dissolve(1)
    mc "This smells so good!"
    la "It does."
    mc "Here. This one is yours."
    la "Thanks."
    scene 11_914 with Dissolve(1)
    el "That's actually a lot."
    la "Yeah. And I took the small bucket."
    el "That's the small bucket? [mc], you're definitely going to eat most of it."
    la "From my bucket too!"
    mc "Haha. I'll try."
    scene 11_915 with Dissolve(1)
    la "Shall we eat in the hot tub?"
    mc "Sure."
    la "Can you take my bucket? I'll get some more wine."
    mc "Is the other bottle empty already? How much do you guys drink?"
    la "Hehe."
    scene black with Dissolve(1)
    pause 2
    scene 11_916 with Dissolve(1)
    el "How are they?"
    mc "Good, but really spicy!"
    el "Yeah?"
    scene 11_917 with Dissolve(1)
    el "You're right. They are pretty spicy."
    mc "Heh. Pretty spicy?"
    mc "I'm sweating already after a few bites."
    scene 11_918 with Dissolve(1)
    mc "So I take it you like spicy food?"
    el "Mm-hmm. But we don't eat it too often."
    mc "Because of your brothers?"
    el "Yeah. They can't handle it yet. We're slowly getting them used to it."
    scene 11_919 with Dissolve(1)
    la "I'm back!"
    la "And look what I've found."
    mc "What's that?"
    scene 11_920 with Dissolve(1)
    la "Mini bananas!"
    mc "What's up with you and bananas?"
    la "I don't know. I just saw them in the kitchen."
    la "Cute, right? They're so small!"
    scene 11_921 with Dissolve(1)
    mc "*Whiny* They aren't small. They are at least average, okay!"
    la "You think?"
    el "Dios mío, Layla..."
    scene 11_922 with Dissolve(1)
    mc "Haha."
    el "Haha."
    scene 11_923 with Dissolve(1)
    la "Why are you laughing now?"
    la "Sometimes I think you guys have some kind of inside joke and leave me out of it."
    la "It's not fair!"
    scene 11_924 with Dissolve(1)
    la "Whatever..."
    mc "Wait, Layla!"
    mc "Those are the..."
    scene 11_925 with Dissolve(1)
    la "..."
    mc "Spicy ones."
    scene 11_926 with Dissolve(1)
    la "Why are they so spicy?"
    mc "Because that was a spicy one!"
    la "Why did you give me one of those?"
    mc "I didn't give you anything. You grabbed it yourself!"
    la "Aaah..."
    scene 11_927 with Dissolve(1)
    la "..."
    mc "No! Don't!"
    el "..."
    scene 11_928 with Dissolve(1)
    la "Now it's even worse!"
    mc "I tried to stop you. Twice!"
    la "And it's getting worse by the second... Aaah..."
    el "Are you okay, Layla?"
    scene 11_929 with Dissolve(1)
    la "I can't breathe. *Hiccup* Am I going to die? I *hiccup* think I'm dying!"
    mc "No, you're not."
    la "I don't *hiccup* wanna die!"
    mc "Layla! You're not going to die!"
    la "My *hiccup* whole body feels so hot... This bikini..."
    scene 11_930 with Dissolve(1)
    la "Aaah!"
    mc "Uh..."
    el "Lay...?"
    scene 11_931 with Dissolve(1)
    el "Layla! What are you doing?"
    mc "{i}(I feel bad for her, but at the same time it's a little funny.){/i}"
    mc "{i}(And why am I getting turned on in this situation?){/i}"
    mc "{i}(I can't help but stare at her tits!){/i}"
    scene 11_932 with Dissolve(1)
    el "Layla, stop. That won't make a difference."
    la "..."
    mc "Do you have yoghurt or tomatoes in the kitchen?"
    la "Why are you *hiccup* asking me about tomatoes now? I *hiccup* don't know."
    mc "I'll be right back."
    scene black with Dissolve(1)
    pause 2
    scene 11_933 with Dissolve(1)
    mc "{i}(She took it completely off?){/i}"
    mc "I found some tomato slices."
    scene 11_934 with Dissolve(1)
    mc "Here you go!"
    mc "Put it in your mouth and suck and chew on it."
    mc "It should give you some relief."
    la "Okay."
    scene 11_935 with Dissolve(1)
    mc "Is it helping?"
    la "*Nods*"
    mc "Good."
    scene 11_936 with Dissolve(1)
    mc "I've never met a person with such a reaction to spicy food."
    la "I told you I'm not good with spicy."
    la "Besides. They weren't just spicy. They were really spicy!"
    mc "True. I'll give you that. I was sweating too, when I ate one."
    scene 11_937 with Dissolve(1)
    mc "Want to try the normal one?"
    la "No! I'll never eat chicken wings ever again!"
    mc "Haha."
    scene 11_938 with Dissolve(1)
    mc "{i}(I keep getting distracted by her boobs.){/i}"
    mc "{i}(I'd rather suck on them than on a chicken wing!){/i}"
    la "What are you looking at?"
    mc "..."
    scene 11_939 with Dissolve(1)
    la "Aaah!"
    el "*Shakes head*"
    scene 11_940 with Dissolve(1)
    la "Why are you...?"
    mc "Really? Now you react? You've been sitting here like this for the last ten minutes!"
    el "Haha."
    la "You still shouldn't just look!"
    mc "I tried my best."
    scene 11_941 with Dissolve(1)
    la "Aaah!"
    mc "{i}(Here we go again.){/i}"
    mc "It's not my fault they're so nice to look at."
    la "[mc]!"
    scene 11_942 with Dissolve(1)
    mc "You do realise you're making it worse, right?"
    la "Close your eyes!"
    mc "Haha."
    scene 11_943 with Dissolve(1)
    mc "Elena, help me!"
    el "Help you? Why would I help you?"
    scene 11_944 with Dissolve(1)
    mc "I'm dying."
    la "That's not funny! I really thought I was dying!"
    mc "Haha. Seems to me you're more lively than ever."
    scene 11_945 with Dissolve(1)
    mc "..."
    mc "{i}(Does she even know what's she's doing?){/i}"
    menu:
        "Bite her[KoGa3AutoWTChange1]{size=-4}(Layla Week5 Tuesday Hottub Chickenbreast, Layla Points+2) {/size} {/color}":
            $ Layla_Week5_Tuesday_Hottub_Chickenbreast = True
            $ Layla_Points += 2
            # Layla (88)
            scene 11_946 with Dissolve(1)
            la "..."
            mc "{i}(I just can't resist.){/i}"
            scene 11_947 with Dissolve(1)
            la "Aaah..."
            la "[mc]."
            el "What happened?"
            scene 11_948 with Dissolve(1)
            la "He... He bit... He bit my..."
            el "He what?"
            if Layla_Week2_Wednesday_Chichis == True:
                la "My chichi."
            else:
                la "My boob."
            mc "Sorry. I thought it was a chicken breast."
            la "[mc]!!!"
            scene 11_949 with Dissolve(1)
            mc "Haha."
            la "You..."
            mc "Oh? You're giving me another taste?"
            la "Nooo!"
        "Don't do anything":
            pass
    scene black with Dissolve(1)
    pause 2
    scene 11_950 with Dissolve(1)
    el "I'm so full. I've never eaten that much chicken before."
    mc "Especially since we also had to eat Layla's share. I couldn't even finish..."
    la "Sorry."
    el "I probably won't touch a chicken wing for months."
    mc "Haha."
    scene 11_951 with Dissolve(1)
    mc "How are you doing? Your mouth still burning?"
    la "It's fine now."
    mc "Do we still have some wine?"
    la "I emptied it."
    scene 11_952 with Dissolve(1)
    mc "You drank it all? How many bottles did you guys have?"
    mc "Three, four?"
    la "That was the fifth one."
    mc "Five? Adriana's gonna be mad once she sees how many bottles are missing."
    la "Oh yeah."
    scene 11_953 with Dissolve(1)
    mc "Are you drunk?"
    la "No."
    la "Yes!"
    mc "Haha. You definitely are!"
    scene 11_954 with Dissolve(1)
    mc "How about you?"
    el "I'm on the verge of tipsy to drunk."
    el "The spicy chicken helped postpone it a bit."
    mc "True."
    el "Aren't you?"
    scene 11_955 with Dissolve(1)
    mc "A little tipsy, maybe."
    mc "But I didn't drink nearly as much as you guys did."
    la "Pfff..."
    scene 11_956 with Dissolve(1)
    la "Did you have fun at least?"
    mc "I had the greatest time. Correction. Am having!"
    mc "Best hot tub party ever!"
    la "Yay!"
    scene 11_957 with Dissolve(1)
    mc "Just sitting here with two beautiful girls is amazing."
    la "I have an idea how to make it more amazing."
    mc "Mmm?"
    scene 11_958 with Dissolve(1)
    mc "..."
    scene 11_959 with Dissolve(1)
    mc "{i}(This makes it more amazing!){/i}"
    if Elena_Points >= 33:
        scene 11_960 with Dissolve(1)
        el "..."
        scene 11_961 with Dissolve(1)
        mc "{i}(Why is she looking so sad?){/i}"
        mc "{i}(Does she want to join?){/i}"
        mc "{i}(It wouldn't be the first time we've had a three-way kiss.){/i}"
        mc "{i}(But in this situation...?){/i}"
        menu:
            "Grab Elena":
                jump Week5_Tuesday_Layla_Hottub_End_Elena
            "Don't":
                mc "{i}(Sorry... That wouldn't be right.){/i}"
                jump Week5_Tuesday_Layla_Hottub_End_Layla
    else:
        jump Week5_Tuesday_Layla_Hottub_End_Layla

label Week5_Tuesday_Layla_Hottub_End_Elena:
    if _in_replay:
        $ Elena_Points = 46
    $ Elena_Week5_Tuesday_Hottub_Threeway = True
    $ Elena_LikeMC = True
    $ Elena_Points += 2
    # Elena (48)
    scene 11_964 with Dissolve(1)
    el "Uh..."
    scene 11_965 with Dissolve(1)
    el "..."
    scene 11_966 with Dissolve(1)
    mc "{i}(This is my first real kiss with Elena!){/i}"
    scene 11_967 with Dissolve(1)
    mc "{i}(Has she ever been prettier?){/i}"
    mc "{i}(Fuck. I think I'm falling for Elena.){/i}"
    la "It's my turn now!"
    scene 11_968 with Dissolve(1)
    el "..."
    mc "{i}(Okay...){/i}"
    scene 11_969 with Dissolve(1)
    mc "{i}(I don't want to be left out!){/i}"
    scene 11_970 with Dissolve(1)
    ""
    scene 11_971 with Dissolve(1)
    mc "{i}(Would we be doing this if they weren't drunk?){/i}"
    scene 11_972 with Dissolve(1)
    la "You stay there!"
    mc "Uhm. Okay...?"
    mc "{i}(What is she up to now?){/i}"
    scene 11_973 with Dissolve(1)
    el "Uhm... Layla...?"
    la "He's seen them before."
    la "And since I'm naked, you have to be too!"
    scene 11_974 with Dissolve(1)
    mc "{i}(Fuck...){/i}"
    mc "{i}(Yes, I've seen them before, but...){/i}"
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 11_975 at moveup
    pause 3
    mc "{i}(This is the prettiest thing I've ever seen...){/i}"
    mc "Damn, you girls are beautiful!"
    scene 11_976 with Dissolve(1)
    mc "I remember that. You sent me that exact picture after the first time we went to the beach!"
    la "Haha. That's right."
    la "Do you still have it?"
    mc "Of course I still have it!"
    scene 11_977 with Dissolve(1)
    mc "But that's enough teasing!"
    mc "You can't expect me stay here while you guys are looking like that!"
    la "Haha."
    scene 11_978 with Dissolve(1)
    mc "I think I'm getting hungry again all of a sudden."
    la "Nooo!"
    el "Haha."
    scene 11_979 with Dissolve(1)
    ""
    scene 11_980 with Dissolve(1)
    ""
    scene 11_981 with Dissolve(1)
    mc "{i}(I never imagined this day would turn into this...){/i}"
    mc "{i}(Maybe with Layla, but with both of them?){/i}"
    mc "{i}(They look so amazing... And tasty...){/i}"
    mc "{i}(I hope this will be okay.){/i}"
    scene 11_982 with Dissolve(1)
    la "[mc]..."
    el "..."
    scene 11_983 with Dissolve(1)
    ""
    scene 11_984 with Dissolve(1)
    mc "{i}(I really want to suck Elena's boobs too, but...){/i}"
    mc "{i}(Would that be going too far?){/i}"
    mc "{i}(Layla didn't mind me kissing her, but this is different.){/i}"
    mc "{i}(Maybe Elena doesn't even want me to.){/i}"
    mc "{i}(She has such great nipples to suck on though.){/i}"
    scene 11_985 with Dissolve(1)
    el "*Nods*"
    mc "{i}(Did she just nod or was that wishful thinking?){/i}"
    mc "{i}(Fuck it! I might never get this chance again.){/i}"
    scene 11_986 with Dissolve(1)
    el "Ahh..."
    mc "{i}(I'm sucking Elena's...){/i}"
    scene 11_987 with Dissolve(1)
    el "Mmm..."
    scene 11_988 with Dissolve(1)
    mc "{i}(This isn't real. This can't be real.){/i}"
    scene 11_989 with Dissolve(1)
    el "..."
    mc "{i}(I can't get enough!){/i}"
    scene 11_990 with Dissolve(1)
    ""
    scene 11_991 with Dissolve(1)
    mc "{i}(How far are they willing to go?){/i}"
    scene 11_992 with Dissolve(1)
    la "Haha. That tickles!"
    scene 11_993 with Dissolve(1)
    la "Mmm..."
    scene 11_994 with vpunch
    a "LAYLA?"
    la "..."
    mc "{i}(Fuck. Was that Alexis?){/i}"
    $ renpy.end_replay()
    scene 11_995 with Dissolve(1)
    mc "Did you know she was here?"
    la "She must be done with her shift. I kinda invited her after her shift was done."
    mc "Oh..."
    mc "{i}(She probably didn't plan for us to do... This...){/i}"
    la "Where are our tops?"
    scene 11_996 with Dissolve(1)
    mc "Uhm... You know you switched..."
    la "We know! We had to be quick."
    if Alexis_Sex == True:
        scene 11_997 with Dissolve(1)
        a "There you are."
        la "Yeah."
        mc "Hi, Alexis."
        a "..."
        a "Hey."
        scene 11_998 with Dissolve(1)
        la "We're having a small hot tub party."
        a "Oh..."
        la "Do you want to join us?"
        a "No, it's fine."
        scene 11_999 with Dissolve(1)
        la "No, come in."
        a "No, I... I have other plans."
        la "Okay."
        scene 11_1000 with Dissolve(1)
        a "Have fun you guys. Bye."
        el "Bye, Lex."
        la "Bye..."
        scene 11_1001 with Dissolve(1)
        la "She looked sad, right?"
        el "She did."
        mc "{i}(Seeing someone you hooked up with with your sister must not be easy.){/i}"
        scene 11_1002 with Dissolve(1)
        mc "Maybe she just had a bad day?"
        la "Yeah, that must be it."
        la "Lately, there have been a few guys at the bar who keep flirting with her to the point of annoyance."
        mc "Can't she kick them out?"
        la "Probably. But... I don't know."
    else:
        scene 11_1003 with Dissolve(1)
        a "Hey."
        mc "Hi, Alexis."
        el "Hey, Lex. How are you."
        a "I'm good."
        a "Weren't you having a party?"
        scene 11_1004 with Dissolve(1)
        la "I was... Still am!"
        a "Hmm..."
        la "What?"
        a "I just thought there would be more people here."
        la "There were. They left earlier."
        scene 11_1005 with Dissolve(1)
        mc "You know. Every party has that one guy who stays too long or just doesn't leave."
        mc "In this case, that's me."
        a "Haha."
        a "Admitting it is the first step..."
        scene 11_1006 with Dissolve(1)
        a "What have you guys been doing?"
        mc "..."
        la "Uhm... It's a hot tub party, so we were mostly in here."
        la "Do you wanna join us?"
        scene 11_1007 with Dissolve(1)
        a "Thanks but I have other plans. Next time."
        a "The water is cold! Didn't you turn on the heater?"
        la "It was so hot today, it was more refreshing to have cooler water."
        scene 11_1008 with Dissolve(1)
        a "..."
        la "What now?"
        a "You're wearing each other's bikinis?"
        mc "{i}(That didn't take her long to notice. But there's no chance she knows what happened, right?){/i}"
        scene 11_1009 with Dissolve(1)
        la "Yeah. And? We wanted to switch. It's not like you and Erynn never switch clothes."
        a "I wasn't judging or anything."
        a "I just noticed."
        la "..."
        scene 11_1010 with Dissolve(1)
        la "By the way. Are you hungry, Lex?"
        la "We still have some chicken wings."
        a "Aren't they cold?"
        la "You can eat them cold. They still taste great."
        scene 11_1011 with Dissolve(1)
        a "I am a little hungry, actually."
        a "Okay. I'll try one."
        mc "{i}(Aren't those the spicy ones?){/i}"
        mc "{i}(Layla... You can be so mean!){/i}"
        scene 11_1012 with Dissolve(1)
        a "It smells good!"
        a "What flavour is it? Are they spicy?"
        la "A little. Just try it!"
        menu:
            "Warn her[KoGa3AutoWTChange1]{size=-4}({i}Alexis SecretPath: Alexis SP+2{/i}) {/size} {/color}":
                if Alexis_SecretPath == True:
                    $ Alexis_SP += 2
                    # Alexis_SP (4)
                else:
                    pass
                scene 11_1013 with Dissolve(1)
                mc "{i}(If she's as bad with spicy as Layla is, this will turn so ugly.){/i}"
                mc "{i}(I'd better warn her.){/i}"
                mc "*Shakes head*"
                scene 11_1014 with Dissolve(1)
                a "..."
                scene 11_1015 with Dissolve(1)
                a "Aah..."
                la "Ew... Why did you drop it in the hot tub?"
                a "Sorry. It slipped out of my hand... I'll get it out!"
                la "You're so clumsy! And you're cleaning the hot tub!"
                mc "{i}(Haha.){/i}"
                scene 11_1016 with Dissolve(1)
                a "*Whispers* Thanks!"
                mc "*Nods*"
                scene 11_1017 with Dissolve(1)
                a "I'll leave you guys to it."
                la "Wait! You want another one?"
                a "No, thanks. This wet thing here made me lose my appetite."
                a "I'm gonna throw it away."
                scene 11_1018 with Dissolve(1)
                a "Have fun guys!"
                mc "Bye, Alexis."
                la "Bye..."
                scene 11_1019 with Dissolve(1)
                la "That was so close!"
                mc "And you're so mean! She's your sister."
                la "Haha. It was just a little prank."
                scene 11_1028 with Dissolve(1)
                la "She was a little suspicious, right? About the bikinis."
                la "Do you think she...?"
                mc "I don't know. Maybe..."
                mc "{i}(Well... That put a damper on the situation...){/i}"
                mc "{i}(What would've happened if she didn't show up? And now that she's here, we can't really continue. Damn.){/i}"
            "Let her eat it":
                scene 11_1020 with Dissolve(1)
                mc "{i}(This could turn bad so quickly.){/i}"
                mc "{i}(Any second now.){/i}"
                mc "{i}(Three... two... one...){/i}"
                scene 11_1021 with Dissolve(1)
                a "..."
                mc "{i}(Here we go!){/i}"
                scene 11_1022 with Dissolve(1)
                a "*Cough-cough*"
                a "This is so spicy!"
                la "Haha."
                a "*Cough* And it's actually getting worse..."
                scene 11_1023 with Dissolve(1)
                a "Did you put something on this?"
                la "No. Those are just the spicy ones."
                mc "{i}(She's tearing up. Maybe I should've warned her. I feel a little bad.){/i}"
                scene 11_1024 with Dissolve(1)
                a "*Cough-cough*"
                la "I'm sorry. It was just a prank."
                a "..."
                la "I didn't think it would be that bad."
                mc "{i}(Really?){/i}"
                scene 11_1025 with Dissolve(1)
                la "Go chew on a tomato slice. That helps."
                la "Sorry, Lexi!"
                scene 11_1026 with Dissolve(1)
                la "*Sigh* She likes spicy food, so I thought she could handle it."
                mc "Yeah, but those were..."
                la "I know. I feel bad now. I really need to stop pranking her..."
                scene 11_1027 with Dissolve(1)
                la "And now I ruined the party too!"
                mc "No, you didn't!"
                la "When she started talking about the bikinis, I thought she might... You know..."
                scene 11_1028 with Dissolve(1)
                la "Do you think she...?"
                mc "I don't know. She might have, but after the chicken, I think she has other things on her mind."
                mc "{i}(Well... That put a damper on the situation...){/i}"
                mc "{i}(What would've happened if she didn't show up? And now that she's here, we can't really continue. Damn.){/i}"
    scene black with Dissolve(1)
    pause 2
    scene 11_1029 with Dissolve(1)
    mc "I think it's time I was leaving too."
    la "Hmm..."
    mc "Besides. If we stay any longer in the hot tub, we'll look like old shrivelled people."
    la "I don't wanna look like that!"
    scene 11_1030 with Dissolve(1)
    mc "Shall we clean up first?"
    la "No, I'll do that tomorrow."
    mc "Call me then. I'll come and help you."
    la "You don't have to. It's not that much anyway. Thanks for offering."
    scene 11_1031 with Dissolve(1)
    la "How will you get home?"
    mc "Uh, the same way I came here? Take the bus."
    la "I can ask Lexi to drive you. It'll be faster."
    mc "No, it's fine. Thanks. I can also call my mom if I'll miss the bus or something."
    scene 11_1032 with Dissolve(1)
    mc "Happy you made it today, Elena."
    el "Same."
    mc "It was fun!"
    el "Uh-huh. Fun..."
    scene 11_1033 with Dissolve(1)
    el "Aah-haha..."
    el "Dios mío..."
    mc "There it is!"
    el "*Shakes head*"
    scene 11_1034 with Dissolve(1)
    mc "{i}(I'll be thinking about those the whole night.){/i}"
    mc "{i}(Damn. I wanna see them again!){/i}"
    mc "{i}(Not just see...){/i}"
    scene 11_1035 with Dissolve(1)
    mc "Bye, Elena."
    mc "Maybe we'll see each other later, otherwise it's back in school, I guess."
    el "Yeah. Bye, [mc]!"
    scene 11_1036 with Dissolve(1)
    la "I'll walk you to the door."
    mc "Thanks."
    scene 11_1037 with Dissolve(1)
    el "..."
    el "{i}(No...){/i}"
    scene 11_1038 with Dissolve(1)
    la "Today was fun, right?"
    mc "It was amazing!"
    mc "We definitely should do this again!"
    la "Haha, yeah."
    scene 11_1039 with Dissolve(1)
    la "How about tomorrow?"
    mc "Another hot tub party tomorrow?"
    la "No. Let's do something else. Just the two of us."
    scene 11_1040 with Dissolve(1)
    mc "Like a date?"
    la "*Nods*"
    mc "I like it!"
    scene 11_1041 with Dissolve(1)
    la "Aah-haha."
    scene 11_1042 with Dissolve(1)
    ""
    scene 11_1043 with Dissolve(1)
    la "[mc]..."
    la "I'm getting dizzy."
    mc "Haha. That happens when you drink that much!"
    scene 11_1044 with Dissolve(1)
    la "Here's a little thank you for today."
    mc "Hmm?"
    scene 11_1045 with Dissolve(1)
    mc "..."
    scene 11_1046 with Dissolve(1)
    mc "I'll gladly accept!"
    la "Ahh..."
    scene 11_1047 with Dissolve(1)
    la "Aaah! Hey!"
    la "No biting!"
    la "If you're still hungry, I can get you some chicken wings!"
    scene 11_1048 with Dissolve(1)
    mc "I'd rather eat you!"
    mc "You taste so much better!"
    scene 11_1049 with Dissolve(1)
    la "..."
    scene 11_1050 with Dissolve(1)
    la "Bye-bye, [mc]."
    mc "Later, Layla."
    mc "We'll see each other tomorrow then!"
    la "Uh-huh."
    scene 11_1051 with Dissolve(1)
    la "Tomorrow..."
    scene black with Dissolve(2)
    pause 2
    stop music fadeout 1.0
    play music ("Music/LoFi Indie 2.mp3", "Music/LoFi Indie 1.mp3", "Music/LoFi Indie 3.mp3") volume 0.2
    if MC_Bike == True:
        scene 11_1134 with Dissolve(1)
    else:
        scene 11_1134a with Dissolve(1)
    mc "Oh... Hey. I didn't think you'd still be awake."
    m "Hey. What do you mean? It's not even ten..."
    m "I didn't expect you to be back so early."
    scene 11_1135 with Dissolve(1)
    m "Did something happen?"
    mc "No. It just ended naturally. We've been there since six or so."
    mc "That's plenty of time for being in a hot tub."
    m "That's a long time. Aren't you all shrivelled up?"
    mc "Haha. I was."
    scene 11_1136 with Dissolve(1)
    m "Well, I'm glad you had fun."
    mc "..."
    m "What have you..."
    mc "{i}(Everywhere I go, I see boobs now...){/i}"
    scene 11_1137 with Dissolve(1)
    mc "Aaah!"
    m "You okay?"
    mc "I'm going to bed."
    m "Alright... Good night, honey!"
    scene 11_1138 with Dissolve(1)
    m "*Shakes head*"
    scene 11_1139 with Dissolve(1)
    mc "{i}(What a day...){/i}"
    mc "{i}(I can't believe all the things that happened today.){/i}"
    scene 11_1140 with Dissolve(1)
    el "Thinking about me?"
    scene 11_1141 with Dissolve(1)
    mc "FUCK!"
    scene 11_1142 with Dissolve(1)
    m "..."
    scene black with Dissolve(2)
    pause 2
    scene 11_1143 with Dissolve(1)
    n "*Beep-Beep-Beep*"
    mc "Ngggh..."
    scene 11_1144 with Dissolve(1)
    mc "{i}(Why do I have such a hard time waking up early?){/i}"
    mc "{i}(I was so used to it back in Riverside.){/i}"
    mc "{i}(Where is Nikki when you need her?){/i}"
    if Nikki_Girlfriend == True:
        mc "{i}(I wish Nikki was here...){/i}"
    else:
        pass
    scene 11_1145 with Dissolve(1)
    mc "{i}(I still can't believe what happened yesterday.){/i}"
    mc "{i}(Elena...){/i}"
    scene 11_1146 with Dissolve(1)
    mc "..."
    scene 11_1147 with Dissolve(1)
    mc "..."
    scene 11_1148 with Dissolve(1)
    mc "{i}(What the fuck am I doing?){/i}"
    mc "{i}(I'm the worst!){/i}"
    scene 11_1149 with Dissolve(1)
    mc "{i}(I like Layla!){/i}"
    mc "{i}(It was just something... Something...){/i}"
    mc "{i}(Fuck! It messed up my mind! I can't even think anymore. Stupid hot tub party!){/i}"
    jump Week5_Wednesday_Morning

label Week5_Tuesday_Layla_Hottub_End_Layla:
    if _in_replay:
        $ Layla_Week2_Wednesday_Chichis = True
    $ Elena_Friends = True
    scene 11_962 with Dissolve(1)
    el "Okay... That's my cue to leave."
    el "Have fun you guys."
    scene 11_963 with Dissolve(1)
    la "Haha. Sorry, El."
    el "I'll be in your room. If I don't see you later. Bye, [mc]."
    mc "Bye, Elena. It was fun!"
    scene 11_1052 with Dissolve(1)
    mc "I guess it's just us now."
    mc "Is that what you've been waiting for?"
    la "Mm-hmm."
    scene 11_1053 with Dissolve(1)
    mc "{i}(So was I!){/i}"
    scene 11_1054 with Dissolve(1)
    la "Mmm..."
    scene 11_1055 with Dissolve(1)
    mc "Your boobs are so pretty!"
    la "Thanks."
    la "But no more biting!"
    scene 11_1056 with Dissolve(1)
    mc "{i}(No biting? Okay...){/i}"
    scene 11_1057 with Dissolve(1)
    la "He... Hey..."
    mc "What? You said no biting. I wasn't biting."
    la "That... either."
    mc "Not even a little?"
    la "..."
    scene 11_1058 with Dissolve(1)
    la "Just a... Ahh..."
    scene 11_1059 with Dissolve(1)
    mc "{i}(This hot tub is magical.){/i}"
    scene 11_1060 with Dissolve(1)
    mc "{i}(Every time I'm in here, something good happens.){/i}"
    la "[mc]?"
    scene 11_1061 with Dissolve(1)
    la "Can you stand up?"
    mc "Sure."
    scene 11_1062 with Dissolve(1)
    mc "Uh... Okay."
    mc "{i}(I like where this is going.){/i}"
    scene 11_1063 with Dissolve(1)
    la "It's already hard."
    mc "For quite some time now."
    scene 11_1064 with Dissolve(1)
    la "..."
    scene 11_1065 with Dissolve(1)
    la "Now it's my turn."
    scene 11_1066 with Dissolve(1)
    mc "{i}(Oh... Fuck!){/i}"
    scene 11_1067 with Dissolve(1)
    mc "This feels so good, Layla!"
    scene 11_1068 with Dissolve(1)
    mc "{i}(I like her tight grip, too.){/i}"
    scene 11_1069 with Dissolve(1)
    mc "{i}(The way she looks at me...){/i}"
    mc "{i}(This turns me on even more!){/i}"
    mc "Damn, Layla!"
    scene 11_1070 with Dissolve(1)
    la "*Bites*"
    mc "Aaah! Lay...!"
    scene 11_1071 with Dissolve(1)
    la "Haha."
    la "Revenge!"
    mc "I guess I deserved that."
    la "I'll make it better!"
    scene 11_1072 with Dissolve(1)
    mc "Aah... Fuck..."
    scene 11_1073 with Dissolve(1)
    mc "{i}(This is so amazing.){/i}"
    mc "{i}(And to think she learned all this from watching a video?){/i}"
    scene 11_1074 with Dissolve(1)
    mc "{i}(I'm about to cum already.){/i}"
    scene 11_1075 with Dissolve(1)
    mc "If you don't want the same thing to happen as last time, you'd better pull away now."
    mc "Layla?"
    mc "{i}(Why is she still going?){/i}"
    mc "Layla?"
    scene 11_1076 with vpunch
    pause 2
    scene 11_1076 with vpunch
    mc "Fuck..."
    scene 11_1077 with Dissolve(1)
    la "*Cough-cough*"
    mc "Are you okay?"
    la "*Nods*"
    mc "I warned you! Again!"
    la "*Cough* I know. I just wanted to try it one more time."
    scene 11_1078 with Dissolve(1)
    mc "Next time, pull away or spit it out."
    la "I'm not good at spitting."
    mc "Haha."
    la "What?"
    mc "The things you say sometimes."
    scene 11_1079 with Dissolve(1)
    la "Aaah..."
    mc "Let me return the favour this time."
    scene 11_1080 with Dissolve(1)
    mc "Are you okay with that?"
    la "*Nods*"
    scene 11_1081 with Dissolve(1)
    la "Haha."
    mc "Right here!"
    scene 11_1082 with Dissolve(1)
    ""
    scene 11_1083 with Dissolve(1)
    la "Mmm..."
    scene 11_1084 with Dissolve(1)
    la "Aah... Hey!"
    la "We said no more biting!"
    scene 11_1085 with Dissolve(1)
    mc "That was the last time. I promise! Today!"
    la "Haha."
    la "Do you like them that much?"
    if Layla_Week2_Wednesday_Chichis == True:
        mc "Mm-hmm. Your chichis are amazing."
    else:
        mc "Mm-hmm. Your boobs are amazing."
    scene 11_1086 with Dissolve(1)
    mc "{i}(I'll never get enough of them!){/i}"
    scene 11_1087 with Dissolve(1)
    mc "{i}(Why do I love sucking on boobs so much?){/i}"
    mc "{i}(Did I like breastfeeding so much as a baby that now I...){/i}"
    mc "{i}(What the fuck am I even thinking about right now...?){/i}"
    mc "{i}(Did Mom even...? NO! STOP!){/i}"
    scene 11_1088 with Dissolve(1)
    ""
    scene 11_1089 with Dissolve(1)
    mc "{i}(How far will we go?){/i}"
    scene 11_1090 with Dissolve(1)
    mc "You're really okay with this, right?"
    la "*Nods*"
    scene 11_1091 with Dissolve(1)
    mc "{i}(I can't even hide my excitement anymore.){/i}"
    mc "{i}(I wanna bite it, suck it, lick it... Oh man...){/i}"
    scene 11_1092 with Dissolve(1)
    a "Layla?"
    la "..."
    mc "..."
    la "Shit!"
    $ renpy.end_replay()
    scene 11_1093 with Dissolve(1)
    la "Where did I put my top?"
    mc "No idea. You threw it somewhere."
    la "Please help me find it."
    if Alexis_Sex == True:
        scene 11_997 with Dissolve(1)
        a "There you are."
        la "Yeah."
        mc "Hi, Alexis."
        a "..."
        a "Hey."
        scene 11_1094 with Dissolve(1)
        la "We're having a small hot tub party."
        a "I can see that."
        scene 11_1095 with Dissolve(1)
        la "You can stay if you want."
        a "No, I... I have other plans."
        la "Okay."
        scene 11_1096 with Dissolve(1)
        a "Have fun you guys. Bye."
        mc "Bye, Alexis."
        la "Bye..."
        mc "{i}(Well... That put a damper on the situation...){/i}"
        mc "{i}(What would've happened if she didn't show up? And now that she's here, we can't really continue. Damn.){/i}"
        scene 11_1097 with Dissolve(1)
        la "She looked sad, right?"
        mc "A little."
        mc "{i}(Seeing someone you hooked up with with your sister must not be easy.){/i}"
        scene 11_1098 with Dissolve(1)
        mc "Maybe she just had a bad day?"
        la "Yeah, that must be it."
        la "Lately there have been a few guys at the bar who keep flirting with her to the point of annoyance."
        mc "Can't she kick them out?"
        la "Probably. But... I don't know."
    else:
        scene 11_1003 with Dissolve(1)
        a "Hey."
        mc "Hi, Alexis."
        la "Hey, sis."
        a "Weren't you having a party?"
        scene 11_1099 with Dissolve(1)
        la "I was... Still am!"
        a "Hmm..."
        la "What?"
        a "I just thought there would be more people here."
        la "There were. They left earlier."
        scene 11_1005 with Dissolve(1)
        mc "You know. Every party has that one guy who stays too long or just doesn't leave."
        mc "In this case, that's me."
        a "Haha."
        a "Admitting it is the first step..."
        scene 11_1100 with Dissolve(1)
        a "What have you guys been doing?"
        mc "..."
        la "Uhm... It's a hot tub party, so we were mostly in here."
        la "Do you wanna join us?"
        scene 11_1007 with Dissolve(1)
        a "Thanks but I have other plans. Next time."
        a "The water is cold! Didn't you turn on the heater?"
        scene 11_1101 with Dissolve(1)
        la "It was so hot today, it was more refreshing to have cooler water."
        scene 11_1102 with Dissolve(1)
        la "By the way. Are you hungry, Lex?"
        la "We still have some chicken wings."
        scene 11_1103 with Dissolve(1)
        a "Aren't they cold?"
        la "You can eat them cold. They still taste great."
        scene 11_1104 with Dissolve(1)
        a "I am a little hungry, actually."
        a "Okay. I'll try one."
        mc "{i}(Aren't those the spicy ones?){/i}"
        mc "{i}(Layla... You can be so mean!){/i}"
        scene 11_1105 with Dissolve(1)
        a "It smells good!"
        a "What flavour is it? Are they spicy?"
        la "A little. Just try it!"
        menu:
            "Warn her[KoGa3AutoWTChange1]{size=-4}({i}Alexis SecretPath: Alexis SP+2{/i}) {/size} {/color}":
                if Alexis_SecretPath == True:
                    $ Alexis_SP += 2
                    # Alexis_SP (4)
                else:
                    pass
                scene 11_1013 with Dissolve(1)
                mc "{i}(If she's as bad with spicy as Layla is, this could turn so ugly.){/i}"
                mc "{i}(I'd better warn her.){/i}"
                mc "*Shakes head*"
                scene 11_1014 with Dissolve(1)
                a "..."
                scene 11_1106 with Dissolve(1)
                a "Aah..."
                la "Ew... Why did you drop it in the hot tub?"
                a "Sorry. It slipped out of my hand... I'll get it out!"
                la "You're so clumsy! And you're cleaning the hot tub!"
                mc "{i}(Haha.){/i}"
                scene 11_1016 with Dissolve(1)
                a "*Whispers* Thanks!"
                mc "*Nods*"
                scene 11_1107 with Dissolve(1)
                a "I'll leave you guys to it."
                la "Wait! You want another one?"
                a "No, thanks. This wet thing here made me lose my appetite."
                a "I'm gonna throw it away."
                scene 11_1108 with Dissolve(1)
                a "Have fun guys!"
                mc "Bye, Alexis."
                la "Bye..."
                scene 11_1109 with Dissolve(1)
                la "That was so close!"
                mc "And you're so mean! She's your sister."
                la "Haha. It was just a little prank."
                scene 11_1110 with Dissolve(1)
                la "She looked a little suspicious, right?"
                la "Do you think she knows what we were doing?"
                mc "A boy and a girl alone in the hot tub. I think she might have an idea."
                la "..."
                mc "{i}(Well... That put a damper on the situation...){/i}"
                mc "{i}(What would've happened if she didn't show up? And now that she's here, we can't really continue. Damn.){/i}"
            "Let her eat it":
                scene 11_1020 with Dissolve(1)
                mc "{i}(This could turn bad so quickly.){/i}"
                mc "{i}(Any second now.){/i}"
                mc "{i}(Three... two... one...){/i}"
                scene 11_1021 with Dissolve(1)
                a "..."
                mc "{i}(Here we go!){/i}"
                scene 11_1111 with Dissolve(1)
                a "*Cough-cough*"
                a "This is so spicy!"
                la "Haha."
                a "*Cough* And it's actually getting worse..."
                scene 11_1023 with Dissolve(1)
                a "Did you put something on this?"
                la "No. Those are just the spicy ones."
                mc "{i}(She's tearing up. Maybe I should've warned her. I feel a little bad.){/i}"
                scene 11_1112 with Dissolve(1)
                a "*Cough-cough*"
                la "I'm sorry. It was just a prank."
                a "..."
                la "I didn't think it would be that bad."
                mc "{i}(Really?){/i}"
                scene 11_1113 with Dissolve(1)
                la "Go chew on a tomato slice. That helps."
                la "Sorry, Lexi!"
                scene 11_1114 with Dissolve(1)
                la "*Sigh* She likes spicy food, so I thought she could handle it."
                mc "Yeah, but those were..."
                la "I know. I feel bad now. I really need to stop pranking her..."
                scene 11_1115 with Dissolve(1)
                la "And now I ruined the party too!"
                mc "No, you didn't!"
                scene 11_1110 with Dissolve(1)
                la "She looked a little suspicious, right?"
                la "Do you think she knows what we were doing?"
                mc "I don't know. She might have, but after the chicken, I think she has other things on her mind."
                mc "{i}(Well... That put a damper on the situation...){/i}"
                mc "{i}(What would've happened if she didn't show up? And now that she's here, we can't really continue. Damn.){/i}"
    scene black with Dissolve(1)
    pause 2
    scene 11_1116 with Dissolve(1)
    mc "I think it's time I was leaving too."
    la "Hmm..."
    mc "Besides. If we stay any longer in the hot tub, we'll look like old shrivelled people."
    la "I don't wanna look like that!"
    scene 11_1117 with Dissolve(1)
    mc "Shall we clean up first?"
    la "No, I'll do that tomorrow."
    mc "Call me then. I'll come and help you."
    la "You don't have to. It's not that much anyway. Thanks for offering."
    scene 11_1118 with Dissolve(1)
    la "How will you get home?"
    mc "Uh, the same way I came here? Take the bus."
    la "I can ask Lexi to drive you. It'll be faster."
    mc "No, it's fine. Thanks. I can also call my mom if I miss the bus or something."
    scene 11_1119 with Dissolve(1)
    la "I'll walk you to the door."
    mc "Thanks."
    scene 11_1120 with Dissolve(1)
    la "Today was fun, right?"
    mc "It was amazing!"
    mc "We definitely should do this again!"
    la "Haha, yeah."
    scene 11_1121 with Dissolve(1)
    la "How about tomorrow?"
    mc "Another hot tub party tomorrow?"
    la "No. Let's do something else. Just the two of us."
    scene 11_1122 with Dissolve(1)
    mc "Like a date?"
    la "*Nods*"
    mc "I like it!"
    scene 11_1123 with Dissolve(1)
    la "Aah-haha."
    scene 11_1124 with Dissolve(1)
    ""
    scene 11_1125 with Dissolve(1)
    la "[mc]..."
    la "I'm getting dizzy."
    mc "Haha. That happens when you drink that much!"
    scene 11_1126 with Dissolve(1)
    la "Here's a little thank you for today."
    mc "Hmm?"
    scene 11_1127 with Dissolve(1)
    mc "..."
    scene 11_1128 with Dissolve(1)
    mc "I'll gladly accept!"
    la "Ahh..."
    scene 11_1129 with Dissolve(1)
    la "Aaah! Hey!"
    la "You promised no more biting!"
    la "If you're still hungry, I can get you some chicken wings!"
    scene 11_1130 with Dissolve(1)
    mc "I'd rather eat you!"
    mc "You taste so much better!"
    scene 11_1131 with Dissolve(1)
    la "..."
    scene 11_1132 with Dissolve(1)
    la "Bye-bye, [mc]."
    mc "Later, Layla."
    mc "We'll see each other tomorrow then!"
    la "Uh-huh."
    scene 11_1133 with Dissolve(1)
    la "Tomorrow..."
    jump Week5_Wednesday_Morning

label Week5_Wednesday_Morning:
    scene black with Dissolve(2)
    pause 2
    stop music fadeout 1.0
    play music ("Music/LoFi Indie 3.mp3", "Music/LoFi Indie 1.mp3", "Music/LoFi Indie 2.mp3") volume 0.2
    n "Wednesday, 06:23."
    scene 11_1150 with Dissolve(1)
    m "I knew I heard something."
    m "What are you doing up so early? Couldn't sleep?"
    mc "Hey. Morning, Mom. Did I wake you?"
    scene 11_1151 with Dissolve(1)
    m "Morning, honey."
    m "No. I was awake already. Just snoozing a little."
    m "Are you going somewhere?"
    scene 11_1152 with Dissolve(1)
    if Valeria_LikeMC == True:
        mc "Yeah. I'm going running with a friend."
    else:
        mc "Yeah. I'm going running for a bit."
    mc "Coach gave us all a training schedule."
    mc "And I need to start focusing a little more on track if I want a scholarship."
    scene 11_1153 with Dissolve(1)
    m "Don't worry too much about a scholarship."
    m "If you want to go to college, scholarship or not, it's covered."
    mc "Thanks, Mom."
    scene 11_1154 with Dissolve(1)
    m "When will you be back?"
    mc "I don't know. In an hour or two?"
    scene 11_1155 with Dissolve(1)
    m "Okay, have fun. I'm going back to bed."
    mc "Go snooze a bit more."
    m "Trust me, I will!"
    mc "Haha."
    if Valeria_LikeMC == True:
        jump Week5_Wednesday_Morning_ValeriaRun
    else:
        if Alexis_Dating == True:
            if Alexis_Week5_Monday_Date_Cancel == False:
                jump Week5_Wednesday_Morning_AlexisRun
            else:
                if Cara_Girlfriend == True:
                    jump Week5_Wednesday_Morning_Room_Cara
                else:
                    jump Week5_Wednesday_Morning_Room
        else:
            if Cara_Girlfriend == True:
                jump Week5_Wednesday_Morning_Room_Cara
            else:
                jump Week5_Wednesday_Morning_Room

label Week5_Wednesday_Morning_AlexisRun:
    $ Alexis_Week5_Wednesday_Run = True
    scene black with Dissolve(2)
    pause 2
    scene 11_1156 with Dissolve(1)
    ""
    scene 11_1157 with Dissolve(1)
    mc "{i}(Pick up! Pick up...){/i}"
    mc "{i}(Maybe she's still sleeping? Or her phone is on silent and she doesn't hear it?){/i}"
    mc "{i}(Is she a morning person? I don't think so, but...){/i}"
    mc "{i}(She'll probably be angry that I woke her.){/i}"
    scene 11_1158 with Dissolve(1)
    a "Hello?"
    mc "{i}(She was definitely still asleep.){/i}"
    mc "Hey!"
    a "Who's this?"
    mc "Really, Lexi?"
    scene 11_1159 with Dissolve(1)
    a "[mc]?"
    mc "Ding-ding-ding!"
    a "Why are you calling so early? It's seven!"
    mc "{i}(Not a morning person...){/i}"
    mc "Did I wake you?"
    scene 11_1160 with Dissolve(1)
    a "Yes! Of course you did!"
    a "I worked late and after that, Layla had a party here."
    mc "{i}(Oh yeah, I remember. Something about a girls-only hot tub party...){/i}"
    mc "Sorry..."
    scene 11_1161 with Dissolve(1)
    a "So, why are you calling?"
    a "Did something happen?"
    mc "No... Just wanted to hear your pretty voice."
    a "Liar!"
    mc "Haha. I do like your voice, though!"
    scene 11_1162 with Dissolve(1)
    mc "I'm actually waiting outside."
    a "Wait... What?"
    a "No, you're not."
    mc "I am."
    scene 11_1163 with Dissolve(1)
    mc "Can you come down?"
    a "Uhm... Okay... Give me a second. Be right there."
    mc "Sure."
    a "But I swear. If you're not there when I open the door, I'll be coming for you!"
    mc "Haha. I'm here!"
    scene black with Dissolve(1)
    pause 2
    stop music fadeout 1.0
    play music ("Music/LoFi Upbeat 1.mp3", "Music/LoFi Upbeat 2.mp3", "Music/LoFi Upbeat 3.mp3", "Music/LoFi Upbeat 4.mp3") volume 0.2
    scene 11_1164 with Dissolve(1)
    a "Oh... You are here!"
    mc "Well, yeah... Told you."
    a "For a second I thought you were pranking me or something."
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 11_1165 at moveup
    pause 3
    mc "..."
    mc "{i}(Morning person or not. She still looks amazing.){/i}"
    mc "{i}(Was she even sleeping?){/i}"
    scene 11_1166 with Dissolve(1)
    a "What are you looking at?"
    a "It's your fault this time I'm opening the door dressed like this."
    scene 11_1167 with Dissolve(1)
    mc "I think you look amazing."
    mc "Besides, I don't mind as long as it's for me!"
    a "Idiot!"
    scene 11_1168 with Dissolve(1)
    mc "Morning, Lexi!"
    a "*Shakes head* Hey!"
    mc "Sorry for waking you."
    a "You'll be forgiven after you kiss me!"
    scene 11_1169 with Dissolve(1)
    ""
    scene 11_1170 with Dissolve(1)
    a "Did you go for a run this early?"
    mc "Not yet. I'm about to. That's why I came here."
    a "Hmm?"
    mc "To go running together."
    scene 11_1171 with Dissolve(1)
    a "Did you call the wrong number?"
    a "I'm Alexis, not Layla."
    mc "Haha. No, I got the right number."
    scene 11_1172 with Dissolve(1)
    mc "You told me last time about your ankle and stuff."
    mc "And that your dad asks you to go running with him, but you're always saying no because you're scared to hurt it again."
    mc "But you also said that your ankle is fine now. So..."
    mc "Why not try and go run with me and see how it goes?"
    scene 11_1173 with Dissolve(1)
    a "I don't know, I..."
    mc "It'll be okay, Lexi."
    a "Besides, I won't be able to keep up with you. I haven't been running for years."
    mc "We'll keep it to some light jogging."
    scene 11_1174 with Dissolve(1)
    a "But I don't want to mess with your training and..."
    mc "Stop with the excuses already. We're doing this! Whether you like it or not!"
    a "..."
    scene 11_1175 with Dissolve(1)
    a "I don't have anything to wear."
    mc "What did I just say? And I'm sure you have something."
    mc "And if not, go raid your sister's closet. She has plenty of workout clothes."
    a "..."
    scene 11_1176 with Dissolve(1)
    a "FINE!"
    mc "See! Wasn't that difficult."
    a "*Sigh* Be right back!"
    scene 11_1177 with vpunch
    n "*Slap*"
    a "Ahh..."
    mc "And I want to see a smile on your face!"
    a "..."
    scene 11_1178 with Dissolve(1)
    mc "Two minutes!"
    a "Shut up! Don't push it!"
    mc "Haha."
    scene 11_1179 with Dissolve(1)
    mc "{i}(Messing with her is so much fun!){/i}"
    scene black with Dissolve(1)
    pause 2
    scene 11_1180 with Dissolve(1)
    a "Alright, let's go."
    mc "..."
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 11_1181 at moveup
    pause 3
    mc "Look at you. And you said you didn't have anything..."
    mc "You look cute!"
    a "Thanks."
    scene 11_1182 with Dissolve(1)
    mc "*Rawr*"
    a "I knew you were going to comment on that."
    mc "Haha. The kitty t-shirt turned into a full-grown tiger."
    a "..."
    scene 11_1183 with Dissolve(1)
    mc "I love cats."
    mc "Especially yours!"
    a "Oh my god..."
    scene 11_1184 with Dissolve(1)
    a "You have way too much energy in the morning, you know that?"
    mc "It's because I'm excited to be with you."
    a "Yeah-yeah..."
    mc "I mean it."
    scene 11_1185 with Dissolve(1)
    a "So, where are we..."
    a "..."
    a "What are you doing?"
    scene 11_1186 with Dissolve(1)
    a "Are you looking at my butt?"
    mc "Mm-hmm. I need to see if it looks good in those pants or not."
    a "Why does that even matter?"
    mc "Oh, it matters. It matters! That way I know if I'll run in front or behind you!"
    scene 11_1187 with vpunch
    a "[mc]!"
    mc "Haha."
    mc "I'm kidding. I'm kidding."
    mc "It's a compliment, you know?"
    scene 11_1188 with Dissolve(1)
    a "I'm this close to hitting you!"
    a "What's wrong with you today?"
    mc "Nothing..."
    scene 11_1189 with Dissolve(1)
    mc "Sorry..."
    mc "But just an FYI. It looks good!"
    a "Thanks..."
    a "But you're still not going to run behind me! We're running side by side or not at all."
    mc "Deal!"
    if Erynn_Week5_Tuesday_Photoshoot == True:
        scene 11_1190 with Dissolve(1)
        mc "Oh, by the way. Since we're talking about animals."
        mc "Erynn told me you had two dogs."
        a "Mm-hmm. Dakota and Arizona."
        mc "Dakota and Arizona? That's cool."
        scene 11_1191 with Dissolve(1)
        a "Wanna see a picture?"
        mc "Yes! Erynn mentioned a specific one."
        a "Heh... I know which one."
        scene 11_1192 with Dissolve(1)
        mc "..."
        mc "Holy shit! They're huge!"
        mc "Erynn said they were big, but this... Damn. This is intimidating."
        a "Yeah, they were pretty big."
        mc "Could you even go on a walk with them, or did they walk you?"
        a "Haha. They were well trained."
        scene 11_1193 with Dissolve(1)
        mc "You look like a boss-ass-bitch."
        mc "Like: 'Are you sure you want to mess with me?'"
        a "Haha. I did, didn't I?"
        mc "That's an awesome picture."
        scene 11_1194 with Dissolve(1)
        mc "Can you zoom in on your face?"
        mc "I wanna have a better look."
        a "Uhm. Sure."
        scene 11_1195 with Dissolve(1)
        mc "You look so young! What a cutie!"
        a "..."
        scene 11_1195a with Dissolve(1)
        mc "How old were you there?"
        a "Seventeen."
        scene 11_1196 with Dissolve(1)
        mc "I wish I knew you back then already."
        a "You did..."
        mc "Yeah, but not really. I wasn't even living here at that time. *Sigh* Regrets."
        scene 11_1197 with Dissolve(1)
        mc "Do you still have that outfit?"
        a "I might have."
        mc "Mmm."
        scene 11_1198 with Dissolve(1)
        mc "Show me some more."
        a "Pictures?"
        mc "Yeah. With the dogs."
        a "Heh, okay."
        scene 11_1199 with Dissolve(1)
        mc "I was never a pet person, but after seeing all those pictures. I kinda want a dog now."
        a "Haha."
        mc "Oh... Who's this?"
        a "Come on... You know who it is!"
        mc "Layla?"
        a "Uh-huh."
        scene 11_1200 with Dissolve(1)
        mc "She had long hair!"
        a "It was even longer at some point."
        a "She cut it when she turned sixteen."
        scene 11_1201 with Dissolve(1)
        mc "Look at those puppies..."
        a "The bigger the dog, the more they think they are small."
        mc "Haha. Not much room for anyone else on the couch."
        a "When Mom was sitting there, they wanted to be there too. They'd even push us from the sofa to sit next to her."
        mc "Haha, really?"
        scene 11_1202 with Dissolve(1)
        mc "They must have really liked your mom."
        a "They did. They liked her the most out of all of us."
        mc "Did you want a dog, or..."
        scene 11_1203 with Dissolve(1)
        a "No. Dad got them after Layla was born."
        a "Because of his job, he couldn't be home every day and sometimes he was gone for a whole week."
        a "He didn't want Mom to be alone in the house with two little kids so he got two guard dogs to protect us."
        scene 11_1204 with Dissolve(1)
        mc "Didn't you guys ever want a new dog? Not immediately after, of course. It's been a few years now, right?"
        a "We all did, but we were so heartbroken when we lost them."
        a "Layla was bawling her eyes out for weeks."
        a "But I think it hit Mom the worst. For her, it felt like she lost two of her babies."
        scene 11_1205 with Dissolve(1)
        a "And we don't have the time we used to have anymore."
        a "Mom works again, I'm at college, and Layla is out of the house most days."
        a "But maybe one day. Who knows."
    else:
        pass
    scene black with Dissolve(1)
    pause 2
    scene 11_1206 with Dissolve(1)
    mc "Ready... Set..."
    a "What? Wait, wait, wait..."
    mc "Go!"
    a "[mc]!"
    scene 11_1207 with Dissolve(1)
    mc "Haha."
    a "I thought we were doing only some simple jogging."
    mc "We are, we are. I was kidding."
    mc "Come on. I'll follow your pace."
    scene black with Dissolve(1)
    pause 2
    scene 11_1208 with Dissolve(1)
    mc "You're doing great! How are you feeling?"
    a "Still good for now."
    mc "And your ankle?"
    a "No issues there."
    mc "Perfect."
    scene 11_1209 with Dissolve(1)
    a "How often do you run?"
    mc "Honestly. Not as often as I should."
    mc "But I try to go at least three to four times a week."
    a "Did you..."
    scene 11_1210 with Dissolve(1)
    x "On your left."
    mc "Uh..."
    mc "Sorry."
    scene 11_1211 with Dissolve(1)
    a "I guess we're running a little too slow?"
    mc "No. This is actually a really good pace. Especially since you haven't run in years."
    mc "I don't know what he's doing. Thinks he's a superhero or something..."
    scene 11_1212 with Dissolve(1)
    mc "What were you saying earlier?"
    a "Oh... Uhm. Did you ever get... What's it called again? Runner's high? Yeah, runner's high."
    mc "I don't think I have. I heard it's pretty rare. Did you?"
    a "No, but I could use one pretty soon."
    mc "Haha."
    scene black with Dissolve(1)
    pause 2
    scene 11_1213 with Dissolve(1)
    mc "Still doing okay?"
    a "*Heavy breathing* I'm reaching my limit."
    a "Don't know if I can finish this lap."
    mc "You don't have to. Don't overexert yourself."
    scene 11_1214 with Dissolve(1)
    mc "We..."
    x "On your left!"
    mc "..."
    scene 11_1215 with Dissolve(1)
    mc "He's starting to piss me off! That's the third time now!"
    a "Haha."
    mc "I think I've seen him before, too."
    a "Just let it be. He isn't doing anything wrong."
    scene 11_1216 with Dissolve(1)
    mc "He's mocking us."
    a "No, he's not. He's just letting us know he's passing us so we won't run into each other."
    scene 11_1217 with Dissolve(1)
    a "*Heavy breathing* That's it... for me. *Heavy breathing* I can't go anymore."
    a "Sorry."
    mc "Don't apologise. You did great!"
    scene 11_1218 with Dissolve(1)
    a "Haha. What are you doing?"
    a "I'm all sweaty!"
    mc "I don't mind."
    scene 11_1219 with Dissolve(1)
    a "..."
    scene 11_1220 with Dissolve(1)
    mc "You did much better than I expected. Even without doing any exercise, your endurance is pretty good."
    a "Working in a bar is practically running."
    mc "Yeah, it seems like it."
    scene 11_1221 with Dissolve(1)
    mc "How are you feeling now? No pain or anything?"
    a "Exhausted. But that's about it."
    mc "You might feel your legs tomorrow, though. Some muscle aches."
    mc "Actually... Since you're used to walking so much at the bar, you're probably going to be fine."
    scene 11_1222 with Dissolve(1)
    mc "Did you have fun?"
    a "I did!"
    a "Thank you, [mc]!"
    a "Thank you for always pushing me."
    scene 11_1223 with Dissolve(1)
    a "..."
    a "Are you having fun?"
    scene 11_1224 with Dissolve(1)
    mc "Oh this? No. That's payment!"
    a "Haha."
    a "I have to pay with my body?"
    mc "Would you prefer another method?"
    a "No. That's fine!"
    scene 11_1225 with Dissolve(1)
    a "I love you!"
    mc "I love you, too!"
    scene 11_1226 with Dissolve(1)
    ""
    scene 11_1227 with Dissolve(1)
    x "On your left."
    a "..."
    scene 11_1228 with Dissolve(1)
    a "WE KNOW!"
    a "There's plenty of space to get past us..."
    mc "Haha."
    scene 11_1229 with Dissolve(1)
    mc "Come on. Let's get out of here before I have to explain to your parents why you're in prison."
    a "Haha. Me?"
    a "You're not taking the fall for me?"
    scene 11_1230 with Dissolve(1)
    mc "Hell no!"
    a "..."
    if Erynn_Week5_Tuesday_Photoshoot == True:
        mc "I won't survive there. You just have to show the picture of you and the dogs and you'll be fine."
        mc "You'll probably run the place."
    else:
        mc "I won't survive there. But you'll probably run the place."
    scene 11_1231 with Dissolve(1)
    mc "Me on the other hand, I'm way too cute and they'll look at me as a snack!"
    a "Haha."
    mc "Have you seen my butt?"
    a "Haha. Oh my god!"
    scene 11_1232 with Dissolve(1)
    n "*Slap*"
    a "You have a nice butt!"
    a "Maybe I should get that strap-on after all."
    mc "NO!"
    a "Haha."
    scene 11_1233 with Dissolve(1)
    mc "What are the plans for today?"
    a "The beach! Did you forget?"
    mc "Oh yeah... The double date."
    a "What?"
    mc "Nothing. Just uhm... Because we are four..."
    scene 11_1234 with Dissolve(1)
    mc "What time was it? And where do we meet up?"
    a "We'll pick you up in the afternoon. Around two or so."
    mc "Alright."
    if Cara_Girlfriend == True:
        jump Week5_Wednesday_Morning_Room_Cara
    else:
        jump Week5_Wednesday_Morning_Room

label Week5_Wednesday_Morning_ValeriaRun:
    if _in_replay:
        $ Valeria_Week3_Saturday_TC_Swap = True
        $ MC_Week3_Saturday_TC_Win = True
        $ Nikki_Girlfriend = True
        $ MC_Bike = True
    scene black with Dissolve(2)
    pause 2
    stop music fadeout 1.0
    play music "Sounds/Ocean.mp3" volume 0.5
    scene 11_1235 with Dissolve(1)
    mc "{i}(I can't see her anywhere.){/i}"
    scene 11_1236 with Dissolve(1)
    va "..."
    mc "{i}(Did she forget?){/i}"
    mc "{i}(Maybe I should give her a call.){/i}"
    scene 11_1237 with Dissolve(1)
    va "Pssst!"
    mc "..."
    scene 11_1238 with Dissolve(1)
    mc "There you are!"
    va "Hey."
    mc "Almost walked past you."
    va "Almost? You did!"
    scene 11_1239 with Dissolve(1)
    mc "To be fair, I didn't recognise you without your mustard-yellow beanie."
    va "Orange!"
    mc "It's definitely mustard yellow!"
    va "..."
    scene 11_1240 with Dissolve(1)
    mc "Oh and good morning!"
    va "Hi."
    mc "{i}(This girl is just too cute.){/i}"
    mc "{i}(I want to kiss her again. But we aren't even...){/i}"
    mc "{i}(Why am I so nervous around her all of a sudden? Just fucking do it!){/i}"
    scene 11_1241 with Dissolve(1)
    va "..."
    mc "{i}(Wow... A kiss on her cheek. I'm such a pussy!){/i}"
    scene 11_1242 with Dissolve(1)
    mc "What are you listening to?"
    mc "Can I?"
    va "Sure."
    scene 11_1243 with Dissolve(1)
    stop music fadeout 1.0
    play music "Music/Cloverfield Road Swim Team - Room 202.mp3" volume 0.5
    mc "This is good!"
    mc "Who are they?"
    va "Cloverfield Road Swim Team."
    mc "Cloverfield Road Swim Team? Where do they get these band names from?"
    mc "I really need to steal your playlist! I'm finding one gem after another."
    va "Haha."
    scene 11_1244 with Dissolve(1)
    va "Come on. We're not here to listen to music the whole time."
    va "Let's run."
    mc "And get you to finally visit the beach!"
    va "Mm-hmm."
    scene 11_1245 with Dissolve(1)
    stop music fadeout 1.0
    play music "Sounds/Ocean.mp3" volume 0.5
    mc "Do you need your bag, or should we put it in a locker?"
    va "Yeah, I wanted to ask if there was a place to store it."
    mc "There are some lockers at the beach next to the changing cabins."
    scene black with Dissolve(1)
    pause 2
    scene 11_1246 with Dissolve(1)
    va "I'm good to go."
    mc "Cool."
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 11_1247 at moveup
    pause 3
    mc "{i}(I swear she's a different person when she takes off that beanie.){/i}"
    mc "{i}(Holy shit.){/i}"
    mc "{i}(This is all the motivation I need...){/i}"
    scene 11_1248 with Dissolve(1)
    va "You good?"
    mc "I'm... I'm good... Yeah..."
    va "Kay. Let's go, then."
    scene 11_1249 with Dissolve(1)
    ""
    scene 11_1250 with Dissolve(1)
    mc "First impressions?"
    va "I love it. I should've come earlier."
    mc "Haha, right?"
    scene 11_1251 with Dissolve(1)
    va "Is it always this empty? I expected it to be full of people."
    mc "It's very early. And not many come to this part of the beach. As you can see, it has many small rocks in the sand."
    va "Or because this is a private beach."
    mc "Uh... You think? I didn't see any signs."
    va "We went through a gate, though."
    scene 11_1252 with Dissolve(1)
    mc "Oh well... If someone comes, we'll just pretend to be lost tourists."
    mc "No hablo inglés!"
    va "Haha."
    scene black with Dissolve(1)
    pause 2
    scene 11_1253 with Dissolve(1)
    mc "What have you been doing so far this spring break?"
    va "Besides training, not much, to be honest."
    mc "And here we are at the beach with endless opportunities, and guess what we're doing? Training..."
    va "Haha. I don't mind. I enjoy it."
    scene 11_1254 with Dissolve(1)
    va "And I hated losing at training camp."
    va "If I want to have a chance against Sha'Carri next time, I have to put in some extra work."
    mc "{i}(I really need to step up, too.){/i}"
    if MC_Week3_Saturday_TC_Win == False:
        mc "{i}(I can't let Darryl beat me again...){/i}"
    else:
        pass
    scene 11_1255 with Dissolve(1)
    if Nikki_Girlfriend == True:
        mc "She's here."
        va "Who?"
        mc "Sha'Carri. I saw her a few days ago. I think she might be here on holiday."
        va "Oh? I'm gonna call her later, then."
        mc "You've got her number?"
        va "Mm-hmm. We exchanged them after our race."
    else:
        pass
    scene 11_1256 with Dissolve(1)
    va "What about you?"
    mc "I had lots of plans, but I haven't done much either."
    mc "But we still have some days."
    if MC_Bike == True:
        mc "I got a motorcycle though, so I've been driving around a little on that."
        va "You do?"
        mc "I can show you next time."
    else:
        pass
    scene black with Dissolve(1)
    pause 2
    scene 11_1257 with Dissolve(1)
    mc "I didn't know that running on the sand was so much more exhausting. Don't you think?"
    va "..."
    mc "I can see you smirking!"
    mc "Do you think I haven't realised you've been increasing the pace?"
    scene 11_1258 with vpunch
    n "*Bump*"
    mc "Hey!"
    scene 11_1259 with Dissolve(1)
    mc "VALERIA!"
    va "..."
    scene 11_1260 with Dissolve(1)
    va "I'm sorry... Are you okay? That wasn't on purpose! I lost my balance. The sand, you know?"
    mc "Uh-huh. Just like the time at training camp when you 'accidentally' pushed me into the pool..."
    va "No, no. That was totally on purpose."
    scene 11_1261 with Dissolve(1)
    mc "You'd better start running! Because when I..."
    va "You sure? Will you be able to catch up?"
    va "You were complaining before already about me increasing the pace."
    scene 11_1262 with Dissolve(1)
    va "I guess I'll slow down a little, or else we'll be here all day."
    mc "VAL!"
    scene 11_1263 with Dissolve(1)
    va "Haha."
    mc "You won't be laughing for long!"
    scene 11_1264 with Dissolve(1)
    va "Are you even trying?"
    mc "It's not easy sprinting on sand."
    va "Here come the excuses."
    scene 11_1265 with Dissolve(1)
    mc "{i}(This feels like I'm chasing tail.){/i}"
    mc "{i}(Literally...){/i}"
    mc "{i}(And this one looks particularly amazing!){/i}"
    scene 11_1266 with Dissolve(1)
    va "Aah..."
    mc "You felt that? I felt it too."
    mc "That's your overconfidence leaving your body!"
    va "..."
    scene 11_1267 with Dissolve(1)
    mc "Gotcha!"
    va "Ahhh..."
    scene 11_1268 with Dissolve(1)
    va "[mc]!"
    mc "{i}(Shit!){/i}"
    scene black with vpunch
    pause 2
    scene 11_1269 with Dissolve(1)
    va "Aw..."
    scene 11_1270 with Dissolve(1)
    mc "{i}(At least we landed on the soft and...){/i}"
    mc "{i}(Bouncy sand?){/i}"
    scene 11_1271 with Dissolve(1)
    mc "{i}(What's this?){/i}"
    mc "..."
    mc "{i}(Oh shit){/i}"
    scene 11_1272 with Dissolve(1)
    mc "Sorry! I didn't mean to..."
    va "..."
    scene 11_1273 with Dissolve(1)
    mc "Are you okay?"
    va "*Nods*"
    mc "Good. Because..."
    scene 11_1274 with vpunch
    va "Ah, [mc]!"
    mc "I caught you!"
    scene 11_1275 with Dissolve(1)
    mc "Now what? Where's that big mouth of yours now?"
    va "Heh..."
    scene 11_1276 with Dissolve(1)
    mc "{i}(She's just so freakin' cute!!!){/i}"
    mc "{i}(I want to kiss her so bad, but no more cheek kisses...){/i}"
    mc "Cute but crazy..."
    scene 11_1277 with Dissolve(1)
    ""
    scene 11_1278 with vpunch
    mc "..."
    va "Ahh..."
    scene 11_1279 with Dissolve(1)
    mc "*Cough-cough*"
    mc "What the hell. Did the tide just change?"
    va "Haha. I think it was a rogue wave."
    scene 11_1280 with Dissolve(1)
    mc "Let's move a little before we get hit again."
    mc "I'll help you up."
    va "Thanks."
    scene 11_1281 with Dissolve(1)
    mc "..."
    mc "{i}(Holy...){/i}"
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 11_1282 at moveup
    pause 3
    va "What?"
    va "Something wrong?"
    mc "{i}(Something right. Something so right!){/i}"
    scene 11_1283 with Dissolve(1)
    mc "Uhm..."
    mc "No... But... I can uhm..."
    mc "Your... Your shirt is... Well... See-through..."
    scene 11_1284 with Dissolve(1)
    va "Hmm?"
    va "..."
    scene 11_1285 with Dissolve(1)
    va "Uh..."
    mc "Sorry. I didn't mean to..."
    va "It's not your fault."
    mc "{i}(This is the first time I've seen her that shy.){/i}"
    scene 11_1286 with Dissolve(1)
    mc "Here. Wear mine. It's not see-through."
    mc "A little wet, though."
    va "I don't mind. Thanks."
    scene 11_1287 with Dissolve(1)
    va "Can you turn around for a second?"
    mc "Sure."
    scene 11_1288 with Dissolve(1)
    mc "{i}(It's taking everything not to turn around and...){/i}"
    mc "{i}(Oh man...){/i}"
    scene 11_1289 with Dissolve(1)
    va "Thanks!"
    scene 11_1290 with Dissolve(1)
    mc "Let me have a look."
    mc "Not bad. A little long maybe?"
    if Valeria_Week3_Saturday_TC_Swap == True:
        scene 11_1291 with Dissolve(1)
        va "Soon I'll have a whole wardrobe full of your clothes."
        mc "Right, haha. We did the underwear swap at training camp!"
        mc "That reminds me. I still have to give you your panties back. I keep forgetting to bring them."
    else:
        pass
    scene 11_1292 with Dissolve(1)
    mc "Wanna go sit on the rocks over there so we can dry up a bit?"
    va "Mm-hmm. Sounds good."
    scene black with Dissolve(1)
    pause 2
    scene 11_1293 with Dissolve(1)
    ""
    scene 11_1294 with Dissolve(1)
    mc "{i}(I could just lie here and watch her all day.){/i}"
    mc "{i}(We don't even have to talk.){/i}"
    mc "{i}(She's just so damn cute!){/i}"
    scene 11_1295 with Dissolve(1)
    mc "{i}(Her body is...){/i}"
    mc "{i}(Fuck...){/i}"
    mc "{i}(She'd easily win every wet t-shirt contest.){/i}"
    scene 11_1296 with Dissolve(1)
    mc "{i}(That image is burned into my brain forever.){/i}"
    va "Hey..."
    scene 11_1297 with Dissolve(1)
    mc "Uh... Hey."
    mc "{i}(That scared me...){/i}"
    va "Were you daydreaming?"
    mc "Something like that."
    scene 11_1298 with Dissolve(1)
    va "What were you thinking about?"
    mc "I don't want to say it, but I think you know the answer."
    va "..."
    va "Yeah... Stupid question."
    scene 11_1299 with Dissolve(1)
    va "Third try?"
    mc "..."
    va "If you need help finding my lips this time... Let me know."
    mc "{i}(She knows... This is so embarrassing! Why am I so nervous?){/i}"
    scene 11_1300 with Dissolve(1)
    mc "{i}(Finally!){/i}"
    scene 11_1301 with Dissolve(1)
    ""
    scene 11_1302 with Dissolve(1)
    va "Mmm..."
    mc "You taste of ocean!"
    scene 11_1303 with Dissolve(1)
    va "..."
    scene 11_1304 with Dissolve(1)
    va "*Whispers* [mc]..."
    va "*Whispers* Stop. Someone's coming."
    mc "What?"
    va "*Whispers* Someone's coming!"
    scene 11_1305 with Dissolve(1)
    x "Excuse me!"
    x "This beach is private property!"
    mc "..."
    mc "{i}(Just my luck...){/i}"
    scene 11_1306 with Dissolve(1)
    mc "Uhm... No hablo inglés."
    va "..."
    scene 11_1307 with Dissolve(1)
    x "*Sigh* The bea... Los beachos es... Uhm... Privatos."
    mc "Privada?"
    x "Yes! Sí... Privada!"
    mc "Lo siento, no lo sabíamos.\n Sorry, we didn't know."
    scene 11_1308 with Dissolve(1)
    mc "Nos vamos. We... We leave."
    x "Thank you!"
    scene 11_1309 with Dissolve(1)
    va "Sorry..."
    x "It's okay."
    scene 11_1310 with Dissolve(1)
    va "..."
    mc "..."
    scene 11_1311 with Dissolve(1)
    va "Haha. I can't believe you did that and kept a straight face."
    va "It took everything to not burst into laughter."
    mc "I saw that. You almost made me laugh, too."
    scene 11_1312 with Dissolve(1)
    mc "By the way. That was the cutest sorry I've ever heard."
    va "Because you pretended to be Hispanic, so I had to..."
    mc "We are Hispanic."
    va "You know what I mean."
    scene 11_1313 with Dissolve(1)
    mc "Do that accent again."
    va "No!"
    mc "Please?"
    scene 11_1314 with Dissolve(1)
    va "*Sigh*"
    va "Sorry..."
    mc "Can you keep talking like that?"
    va "No!"
    scene 11_1315 with Dissolve(1)
    mc "How was that for a first beachos experience?"
    va "Don't be mean. She tried and was nice about it. She could've called the police for us trespassing."
    mc "You're right."
    va "But it was definitely memorable."
    scene 11_1316 with Dissolve(1)
    mc "We didn't do much running today, though."
    va "I'll make up for it tomorrow."
    mc "Sorry."
    scene 11_1317 with Dissolve(1)
    mc "Haha. Hey!"
    mc "I said I was sorry."
    va "It's the way you said it!"
    mc "Haha. Wasn't it cute?"
    stop music fadeout 1.0
    scene black with Dissolve(1)
    pause 2
    scene 11_1318 with Dissolve(1)
    va "Here's your shirt back."
    mc "Thank you."
    va "Thanks for lending it to me."
    scene 11_1319 with Dissolve(1)
    va "If you ever want to wear my clothes, let me know."
    mc "Haha."
    mc "If I had to switch clothes with a girl again, it will probably be you."
    va "Yeah? Why's that?"
    scene 11_1320 with Dissolve(1)
    mc "You wear the least 'girly' clothes of the girls I know."
    va "Hmm?"
    mc "I mean. Take Layla and Elena for example. They often wear skirts and hot pants."
    mc "You don't. It's mostly leggings and hoodies. More casual, I suppose. Sporty-casual?"
    scene 11_1321 with Dissolve(1)
    va "I see."
    mc "I like the stuff you wear though. You look good in them."
    va "Thanks."
    mc "Especially those leggings!"
    va "..."
    scene 11_1322 with Dissolve(1)
    mc "And white tops when you go in the water."
    va "Hey!"
    va "Don't tell anyone about that!"
    scene 11_1323 with Dissolve(1)
    mc "Don't worry. It won't ever leave my mouth!"
    va "..."
    va "I wouldn't mind you forgetting about it, either."
    mc "Then give me something else to think about."
    mc "What are you doing later?"
    scene 11_1324 with Dissolve(1)
    va "Going to the beach with Darryl."
    mc "What?"
    mc "{i}(I didn't expect her to say something that would make me think of something other than her wet shirt. Fuck...){/i}"
    mc "{i}(Is she serious, or...?){/i}"
    va "Among other people."
    scene 11_1325 with Dissolve(1)
    va "You can come with us."
    mc "Uh-huh. Darryl and I hanging out together... No."
    mc "But I want to hang out with you again. Just not in a group setting."
    mc "Just the two of us, like today."
    scene 11_1326 with Dissolve(1)
    mc "How about Friday or Saturday?"
    va "Hmm... Maybe."
    mc "No. Not the maybe again."
    va "Make me change it!"
    scene 11_1327 with Dissolve(1)
    va "Uh..."
    scene 11_1328 with Dissolve(1)
    va "..."
    scene 11_1329 with Dissolve(1)
    mc "{i}(How is this?){/i}"
    scene 11_1330 with Dissolve(1)
    mc "{i}(I knew she would enjoy this!){/i}"
    scene 11_1331 with vpunch
    mc "Haha. I thought you didn't like being picked up."
    mc "And now you're doing it yourself."
    va "Shut up."
    mc "Make me!"
    scene 11_1332 with Dissolve(1)
    mc "..."
    scene 11_1333 with Dissolve(1)
    mc "{i}(Her tongue-kisses are the best!){/i}"
    scene 11_1334 with Dissolve(1)
    mc "Did that change your maybe into a yes?"
    va "..."
    mc "Haha. I can see you want to say maybe again..."
    mc "I still have a few days to change your mind!"
    scene black with Dissolve(1)
    pause 2
    stop music fadeout 1.0
    play music "Sounds/Street_Traffic.mp3" volume 0.5
    scene 11_1335 with Dissolve(1)
    va "Hmm... Good question."
    va "I think..."
    play sound "Sounds/CarHonk.mp3" volume 0.1
    n "*Beep-beep*"
    scene 11_1336 with Dissolve(1)
    va "Oh..."
    va "Give me a second."
    mc "Sure."
    scene 11_1337 with Dissolve(1)
    va "Hey."
    x "Hola cariño."
    x "Weren't you going for a run?"
    va "We were. Kinda..."
    scene 11_1338 with Dissolve(1)
    mc "{i}(Is that Val's mom?){/i}"
    mc "{i}(I can't really see her with the glare and the tinted windows.){/i}"
    mc "{i}(Should I go closer, or would that be weird?){/i}"
    scene 11_1339 with Dissolve(1)
    x "Are you on your way home?"
    va "Mm-hmm."
    x "Do you want to get in, or...?"
    va "Can we drive past Dad's? I need to get something."
    x "Sure."
    va "Give me a second."
    scene 11_1340 with Dissolve(1)
    va "Hey. That's my mom."
    va "Sorry, but I have..."
    mc "No, it's fine. We were on our way home and we had to take different buses anyway."
    scene 11_1341 with Dissolve(1)
    mc "Here's your bag."
    va "Thank you."
    va "And thank you for showing me the beach. I had fun."
    mc "Me too."
    scene 11_1342 with Dissolve(1)
    mc "..."
    scene 11_1343 with Dissolve(1)
    va "See you Friday or Saturday then?"
    mc "Oh, it's not a..."
    va "Maybe."
    mc "Haha. I felt both happy and disappointed in less than a second."
    scene 11_1344 with Dissolve(1)
    va "Sorry..."
    mc "Stop being cute!"
    va "..."
    scene 11_1345 with Dissolve(1)
    va "Bye!"
    mc "Later, Val."
    scene 11_1346 with Dissolve(1)
    x "That's the boy from the pictures, right?"
    va "Mm-hmm."
    x "[mc]?"
    va "*Nods*"
    x "He looks even better in person."
    scene 11_1347 with Dissolve(1)
    x "Bye, [mc]!"
    va "Mom! What are you doing? Stop!"
    x "He's waving too."
    va "That's because you are! Just drive!"
    scene 11_1348 with Dissolve(1)
    x "What did you guys do?"
    va "Train."
    x "Train? Nothing else?"
    va "Maybe."
    x "Oh, come on! You always tell me everything!"
    $ renpy.end_replay()
    if Cara_Girlfriend == True:
        jump Week5_Wednesday_Morning_Room_Cara
    else:
        jump Week5_Wednesday_Morning_Room

label Week5_Wednesday_Morning_Room_Cara:
    scene black with Dissolve(1)
    pause 2
    stop music fadeout 1.0
    play music ("Music/LoFi Indie 3.mp3", "Music/LoFi Indie 1.mp3", "Music/LoFi Indie 2.mp3") volume 0.2
    scene 11_1349 with Dissolve(1)
    mc "{i}(The best part of running is the shower after.){/i}"
    play sound "Sounds/Phone_Vibrate.mp3"
    n "*Bzzzt. Bzzzt*"
    mc "..."
    n "*Bzzzt. Bzzzt*"
    scene 11_1350 with Dissolve(1)
    mc "{i}(Is that my phone?){/i}"
    n "*Bzzzt. Bzzzt*"
    mc "{i}(It is!){/i}"
    scene 11_1351 with Dissolve(1)
    mc "{i}(Cara...){/i}"
    mc "{i}(Facetime, huh?){/i}"
    scene 11_1352 with Dissolve(1)
    mc "Hey there, cutie."
    c "Hey!"
    mc "How are you?"
    c "I'm good. You?"
    scene 11_1353 with Dissolve(1)
    mc "I'm good too."
    c "Why are you wet?"
    mc "I was in the shower."
    c "Oh. So you're naked?"
    scene 11_1354 with Dissolve(1)
    mc "Yup!"
    c "[mc]!"
    scene 11_1355 with Dissolve(1)
    c "I just asked if you were naked!"
    mc "I answered by showing."
    c "I didn't need to see it."
    mc "Haha."
    c "..."
    scene 11_1356 with Dissolve(1)
    mc "Let me dry off real quick."
    mc "Want me to place the phone so you can see?"
    c "No!"
    mc "Haha. Be right back then."
    scene black with Dissolve(1)
    pause 2
    scene 11_1357 with Dissolve(1)
    mc "Alright. I'm all yours now."
    c "Heh."
    mc "By the way. Don't you have school today?"
    c "I did. I'm back already."
    scene 11_1358 with Dissolve(1)
    mc "At ten in the morning?"
    c "It's the afternoon here. And I don't have classes this afternoon."
    mc "Right. Time zones... Always forget that."
    c "Wait... Are you still naked?"
    scene 11_1359 with Dissolve(1)
    mc "Uh-huh."
    c "I hope you at least closed your door. You know what can happen if you don't."
    mc "Haha. I remember. But don't worry. I'm home alone."
    scene 11_1360 with Dissolve(1)
    c "So am I."
    mc "You are?"
    mc "Then the better question would be why you aren't naked!"
    c "..."
    scene 11_1361 with Dissolve(1)
    mc "Take 'em off!"
    c "Should I?"
    mc "{i}(I expected her to say no immediately.){/i}"
    mc "Uh-huh."
    c "Okay."
    scene 11_1362 with Dissolve(1)
    mc "..."
    mc "{i}(What the fuck? Did we disconnect?){/i}"
    mc "Cara?"
    scene 11_1363 with Dissolve(1)
    c "Still here."
    mc "The screen went black, I thought we lost connection."
    c "No, I just put the phone down so I could take my clothes off."
    mc "Don't put it down. I want to see!"
    scene 11_1364 with Dissolve(1)
    c "It's not easy holding the phone up and undressing."
    mc "Just lean the phone on your desk or something."
    c "Give me a second."
    mc "{i}(I'm so excited already.){/i}"
    scene 11_1365 with Dissolve(1)
    c "How about this?"
    c "Can you see me?"
    mc "That's perfect!"
    scene 11_1366 with Dissolve(1)
    c "..."
    mc "{i}(She's actually doing it. That's amazing.){/i}"
    mc "{i}(I'm getting turned on already.){/i}"
    scene 11_1367 with Dissolve(1)
    mc "What's wrong? Why are you stopping?"
    c "Don't you think this is weird?"
    mc "No. Not at all. I think it's sexy!"
    mc "But if it makes you uncomfortable, don't do it."
    scene 11_1368 with Dissolve(1)
    c "It's not that."
    c "Maybe it's only because it's over the phone. I've never done this."
    mc "Yeah. I'd rather be there with you right now. And do all kinds of things to you."
    scene 11_1369 with Dissolve(1)
    c "[mc]..."
    c "Fine. I'll continue."
    c "But only this one time, and only for you."
    mc "Well I hope only for me!"
    scene 11_1370 with Dissolve(1)
    mc "So pretty!"
    c "..."
    scene 11_1371 with Dissolve(1)
    mc "Damn, Cara!"
    scene 11_1372 with Dissolve(1)
    mc "{i}(She hasn't even stripped down completely and I'm so hard already.){/i}"
    mc "{i}(Fuck...){/i}"
    mc "{i}(She's changed so much in the last few months. From a shy girl, to this...){/i}"
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 11_1373 at moveup
    pause 3
    mc "So fucking sexy!"
    c "Thanks."
    scene 11_1374 with Dissolve(1)
    c "Alright. That's it."
    c "I hope you liked it."
    scene 11_1375 with Dissolve(1)
    mc "Wait. What?"
    mc "You're still wearing your panties. Can you go all the way?"
    c "Uhm... Fully nude?"
    mc "Uh-huh. Please?"
    c "..."
    scene 11_1376 with Dissolve(1)
    c "Don't tell anyone I'm doing this."
    mc "Why would I tell anyone?"
    mc "And can you turn around and come closer?"
    scene 11_1377 with Dissolve(1)
    mc "{i}(This is gonna be so good!){/i}"
    scene 11_1378 with Dissolve(1)
    mc "..."
    mc "{i}(I wish I was there right now to take her from behind.){/i}"
    scene 11_1379 with Dissolve(1)
    mc "{i}(Such a pretty pussy!){/i}"
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 11_1380 at moveup
    pause 3
    mc "Damn, Cara..."
    mc "You're so fucking perfect!"
    c "..."
    scene 11_1381 with Dissolve(1)
    mc "No..."
    mc "Don't pick it up yet. Let me see a bit more."
    scene black with Dissolve(1)
    mc "{i}(I can't see anything anymore.){/i}"
    mc "{i}(Did she put the phone down again?){/i}"
    mc "Cara?"
    scene 11_1382 with Dissolve(1)
    mc "{i}(Okay? What's happening?){/i}"
    mc "{i}(She repositioned her phone?){/i}"
    scene 11_1383 with Dissolve(1)
    mc "{i}(What's she doing?){/i}"
    mc "{i}(I'm getting more excited by the second.){/i}"
    mc "{i}(Just look at that ass!){/i}"
    scene 11_1384 with Dissolve(1)
    mc "What are you doing?"
    c "..."
    mc "And what's with that devious smile?"
    scene 11_1385 with Dissolve(1)
    mc "Oh shit..."
    scene 11_1386 with Dissolve(1)
    mc "{i}(I can't believe what's happening right now...){/i}"
    scene 11_1387 with Dissolve(1)
    mc "{i}(Cara masturbating...){/i}"
    mc "{i}(Over the phone...){/i}"
    scene 11_1388 with Dissolve(1)
    mc "{i}(Where's the zoom function?){/i}"
    mc "{i}(Is there a zoom function?){/i}"
    scene 11_1389 with Dissolve(1)
    c "*Moaning*"
    scene 11_1390 with Dissolve(1)
    mc "{i}(This is better than any porn movie...){/i}"
    scene 11_1391 with Dissolve(1)
    mc "{i}(This is so fucking hot.){/i}"
    mc "Yes, stroke that pussy for me, Cara!"
    scene 11_1392 with Dissolve(1)
    c "Ahhh..."
    scene 11_1393 with Dissolve(1)
    mc "{i}(Wow...){/i}"
    mc "{i}(She's going all the way?){/i}"
    scene 11_1394 with Dissolve(1)
    mc "Damn, Cara!"
    mc "That is so sexy!"
    scene 11_1395 with Dissolve(1)
    c "Mmm..."
    scene 11_1396 with vpunch
    c "Ah... Ahh..."
    scene 11_1396 with vpunch
    mc "Yes! Cum for me, Cara!"
    c "[mc]..."
    scene black with Dissolve(1)
    pause 2
    scene 11_1397 with Dissolve(1)
    c "*Heavy breathing*"
    mc "Did you orgasm?"
    c "*Nods*"
    mc "That was the best thing I've ever seen!"
    scene 11_1398 with Dissolve(1)
    mc "Look at that smile!"
    mc "You enjoyed that, huh?"
    scene 11_1399 with Dissolve(1)
    c "I can't believe I just did that."
    c "But stripping in front of the camera for you made me horny all of a sudden."
    mc "Whenever you get horny again, please call me so I can watch!"
    c "Haha."
    scene 11_1400 with Dissolve(1)
    mc "You become sexier by the day, Carebear."
    c "Carebear?"
    scene 11_1401 with Dissolve(1)
    mc "Haha, I don't know. It was just something I..."
    c "No, I like it. It's cute."
    scene 11_1402 with Dissolve(1)
    mc "When is your next holiday?"
    c "Easter break isn't that far off."
    mc "Right."
    scene 11_1403 with Dissolve(1)
    mc "And I might just come over for a weekend before that."
    c "Yeah? I'd love that!"
    mc "But until then, we have Facetime now."
    mc "Damn... Still mind blown about what just happened. That was so fucking hot."
    c "Haha."
    scene 11_1404 with Dissolve(1)
    c "..."
    mc "What?"
    c "I just heard a car pull up."
    mc "Your mom?"
    scene 11_1405 with Dissolve(1)
    c "No. She's still at work."
    c "Must be Nikki. We wanted to go shopping together once she was done with work."
    mc "Fun. I guess I'll let you put on some clothes, then..."
    c "Heh, yeah."
    scene 11_1406 with Dissolve(1)
    mc "How's Nikki?"
    c "She's doing good. She was a bit sad she didn't come with me to Madison Springs."
    mc "Bring her next time. Your dad lives here too, so she can visit him as well."
    scene 11_1407 with Dissolve(1)
    c "Oh, I totally forgot. I haven't told you yet but Dad's visiting tomorrow."
    mc "He is?"
    c "Uh-huh. He's staying for a few days."
    mc "That's good."
    scene 11_1408 with Dissolve(1)
    n "*Knock-knock*"
    ni "Cara? Are you in there?"
    c "Yes."
    ni "Are you ready? Can I come in?"
    c "Sure."
    scene 11_1409 with Dissolve(1)
    ni "Hey."
    c "Hey. I just need to find a skirt and I'm good to go."
    ni "Okay. Were you talking to someone?"
    c "Yeah, I'm on Facetime with [mc]."
    ni "Oh... Let me talk to him."
    scene 11_1410 with Dissolve(1)
    ni "Hey, gorgeous!"
    mc "Haha. Right back at ya, Nikki."
    mc "How are you?"
    ni "I'm good. But next time Cara visits you, I'll join too. I really want to go to the beach!"
    scene 11_1411 with Dissolve(1)
    mc "Cara told me already. You're always welcome here. We've plenty of space."
    c "..."
    ni "Thanks."
    scene 11_1412 with Dissolve(1)
    mc "Besides. Your dad lives here too. So..."
    ni "Right. How crazy is that?"
    ni "And not just the fact that he lives there but he's also your coach!"
    scene 11_1413 with Dissolve(1)
    mc "And here I thought, now I've left Riverside I don't have to train with this Morgan chick anymore."
    ni "Hey!"
    mc "Little did I know... I'm still training with a Morgan."
    ni "Haha."
    scene 11_1414 with Dissolve(1)
    ni "I miss our morning runs."
    ni "It was really nice having someone run with me."
    c "Nikki!"
    mc "..."
    scene 11_1415 with Dissolve(1)
    c "What do you think? Is this fine or should I wear another skirt?"
    ni "Yeah. Wear whatever you want, Cara."
    c "Are you going to change?"
    ni "No..."
    scene 11_1416 with Dissolve(1)
    c "Let's go then!"
    c "Can I have my phone?"
    ni "Of course."
    scene 11_1417 with Dissolve(1)
    ni "Bye, [mc]."
    mc "Bye, Nikki. Was nice to speak to you!"
    ni "Call me too once in a while, okay? I miss you too!"
    c "..."
    mc "Will do! Bye-bye!"
    scene 11_1418 with Dissolve(1)
    ni "I'll wait in the kitchen."
    c "Okay. Be right there. Give me two minutes."
    scene 11_1419 with Dissolve(1)
    c "Hey."
    mc "Hey. So what skirt did you choose?"
    c "A solid black pleated skirt."
    mc "Yeah, I have no idea what that is. Don't even know why I asked."
    c "Haha."
    scene 11_1420 with Dissolve(1)
    c "Looks like this!"
    mc "Oh... A mini skirt?"
    c "Not really but it's kinda short so I'll give you that."
    mc "It's sexy!"
    c "Thanks."
    scene 11_1421 with Dissolve(1)
    mc "I don't wanna keep you any longer. Nikki's waiting for you."
    c "Yeah. I'll call you tomorrow after school."
    mc "Alright. I'll probably be at the restaurant so I might not be able to pick up immediately."
    mc "But I'll call you back the moment I can."
    scene 11_1422 with Dissolve(1)
    c "Okay. Bye, [mc]. Love you!"
    mc "Love you too. Bye, Carebear! Have fun."
    c "Haha, thanks. Bye."
    $ renpy.end_replay()
    jump Week5_Wednesday_Morning_Room

label Week5_Wednesday_Morning_Room:
    if Erynn_Week5_Tuesday_Photoshoot == True:
        if Alexis_Dating == True:
            if Alexis_Week5_Monday_Date_Cancel == False:
                $ Alexis_Week5_Wednesday_Beach = True
                jump Week5_Wednesday_Beach_Alexis
            else:
                jump Week5_Wednesday_End
        else:
            if Alexis_SecretPath == True:
                $ Alexis_Week5_Wednesday_Beach_SP = True
                jump Week5_Wednesday_Beach_Alexis_SP
            else:
                if Layla_Dating == True:
                    jump Week5_Wednesday_Layla_Date
                else:
                    jump Week5_Wednesday_End
    else:
        if Layla_Dating == True:
            jump Week5_Wednesday_Layla_Date
        else:
            jump Week5_Wednesday_End

label Week5_Wednesday_Beach_Alexis:
    scene black with Dissolve(1)
    pause 2
    stop music fadeout 1.0
    play music ("Music/LoFi Upbeat 1.mp3", "Music/LoFi Upbeat 2.mp3", "Music/LoFi Upbeat 3.mp3", "Music/LoFi Upbeat 4.mp3") volume 0.2
    scene 11_1423 with Dissolve(1)
    mc "Wait..."
    mc "Is she gonna get eaten...?"
    mc "I hope not!"
    play sound "Sounds/CarHonk.mp3" volume 0.1
    n "*Beep-beep*"
    scene 11_1424 with Dissolve(1)
    mc "{i}(That sounded close.){/i}"
    play sound "Sounds/CarHonk.mp3" volume 0.1
    n "*Beep-beep*"
    mc "{i}(Kay. What's going on?){/i}"
    scene 11_1425 with Dissolve(1)
    mc "{i}(Oh... It's them.){/i}"
    if Alexis_Week5_Wednesday_Run == True:
        mc "{i}(Didn't she say two?){/i}"
    else:
        mc "{i}(I didn't think we'd be going this early.){/i}"
    scene 11_1426 with Dissolve(1)
    er "Are you coming?"
    ir "Get in, loser! We're going to the beach!"
    mc "..."
    mc "I'll get my stuff."
    scene 11_1427 with Dissolve(1)
    mc "Hey girls!"
    er "Hey."
    mc "Your dad knows you took his car?"
    a "Haha, yes."
    scene 11_1428 with Dissolve(1)
    mc "Hi."
    a "Hey."
    scene 11_1429 with Dissolve(1)
    a "You can put your bag in the trunk."
    mc "Will do."
    er "Do you want to sit in the front here next to your girlfriend?"
    mc "No, it's fine. Just stay there. I'll hop in the back."
    scene 11_1430 with vpunch
    ir "Hey!"
    ir "Is that really the best way to get in the car?"
    mc "Definitely not the best. But the most fun? Hell yeah!"
    a "Haha."
    scene 11_1431 with Dissolve(1)
    mc "Hey, Erynn."
    er "Hey."
    scene 11_1432 with Dissolve(1)
    ir "..."
    ir "Where's mine?"
    mc "Hey, Iris."
    ir "I mean my kiss!"
    mc "You called me a loser, you don't get one!"
    scene 11_1433 with Dissolve(1)
    ir "I didn't. That was a scene from a movie."
    ir "We even watched it together some time ago."
    a "It's from Mean Girls."
    ir "See!"
    scene 11_1434 with Dissolve(1)
    mc "Fine!"
    ir "Thanks."
    scene 11_1435 with Dissolve(1)
    ir "*Whispers* Besides. I'd never call you a loser."
    ir "*Whispers* You should know that!"
    scene black with Dissolve(1)
    pause 2
    stop music fadeout 1.0
    play music "Music/Mia Rodriguez - California Girls.mp3" volume 0.6
    scene 11_1436 with Dissolve(1)
    ""
    scene 11_1437 with Dissolve(1)
    mc "Are you serious? This song?"
    mc "Did you plan this?"
    a "No. It's the radio."
    mc "..."
    scene 11_1438 with Dissolve(1)
    er "You want it louder?"
    mc "No! Please change the channel."
    er "Louder it is!"
    scene 11_1439 with Dissolve(1)
    n "*Singing* California Girls..."
    mc "{i}(Are you kidding me? What have I done?){/i}"
    mc "Nooo..."
    mc "None of you are actually from California!"
    er "Haha."
    scene 11_1440 with Dissolve(1)
    mc "This song is so stupid!"
    mc "{i}(I'm just gonna hide here for a bit.){/i}"
    ir "What are you doing?"
    mc "Nothing."
    scene 11_1441 with Dissolve(1)
    ir "You're sitting in a car with three extremely hot girls."
    ir "You should be lots of things, but embarrassed isn't one of them!"
    ir "Let's have some fun!"
    scene 11_1442 with Dissolve(1)
    ir "Come on!"
    mc "*Singing* California Girls..."
    a "Haha. Sounds great, babe!"
    scene 11_1443 with Dissolve(1)
    er "Oh..."
    er "You decided on babe?"
    a "Uh... No. I just... It kinda just slipped out."
    er "Didn't you say it would come naturally?"
    scene 11_1444 with Dissolve(1)
    er "I guess you're babe now, [mc]."
    mc "Anything is better than darling!"
    er "Haha."
    play sound "Sounds/CarHonk.mp3" volume 0.1
    n "*Beep-beep*"
    scene 11_1445 with Dissolve(1)
    a "..."
    scene 11_1446 with Dissolve(1)
    x "Hey, Alexis. What's up? Sweet car you've got there."
    mc "{i}(Seems like they know each other.){/i}"
    x "Not working at the bar today?"
    a "As you can see!"
    x "Oh, I can see! Looking good in a bikini!"
    scene 11_1447 with Dissolve(1)
    x "Going to the beach? Why not hang out with us?"
    a "Not interested!"
    x "Don't be like that. It will be fun! Bring your friends."
    x "And your gay friend can come too!"
    scene 11_1448 with Dissolve(1)
    mc "{i}(Okay. That's enough.){/i}"
    ir "Don't!"
    scene 11_1449 with Dissolve(1)
    er "He..."
    ir "He wasn't gay when he fucked the three of us this morning."
    x "What?"
    ir "Exactly! What do you boys know about fucking a girl?"
    ir "Nothing! You're too busy jerking each other's small dicks off."
    scene 11_1450 with Dissolve(1)
    x "What did you say, slut?"
    ir "LOSERS!"
    scene 11_1451 with Dissolve(1)
    er "Oh my god, Iris..."
    mc "{i}(Yeah, that's Iris for you.){/i}"
    a "Haha. Thanks, Iris!"
    ir "Sure. They're just a bunch of idiots."
    scene 11_1452 with Dissolve(1)
    er "You know those guys, Lex?"
    a "Don't really know them. They come to the bar quite often."
    mc "{i}(Maybe those are the guys who hit on her all the time?){/i}"
    scene 11_1453 with Dissolve(1)
    mc "Thanks for sticking up for me."
    ir "Always."
    mc "But you really need to be more careful. One day you won't get away with that."
    scene 11_1454 with Dissolve(1)
    ir "*Whispers* Thanks for still worrying about me!"
    a "..."
    scene black with Dissolve(1)
    pause 2
    stop music fadeout 1.0
    play music "Sounds/Ocean.mp3" volume 0.5
    scene 11_1455 with Dissolve(1)
    ""
    scene 11_1456 with Dissolve(1)
    mc "You okay?"
    mc "You haven't said a word since we left the car."
    a "I'm good. Just thinking."
    mc "About?"
    a "Random stuff. Nothing important."
    scene 11_1457 with Dissolve(1)
    mc "By the way. I really dig those hot pants. You look good."
    a "Thanks."
    mc "And you smell good too! Raspberry shampoo?"
    a "Haha, yes."
    mc "Love it."
    scene 11_1458 with Dissolve(1)
    mc "Let me carry your bag."
    a "It's..."
    mc "Just give it!"
    scene 11_1459 with Dissolve(1)
    a "Thanks!"
    scene 11_1460 with Dissolve(1)
    mc "And why are you looking like that all of a sudden?"
    mc "Your bag isn't nearly as big or heavy as Lexi's!"
    scene 11_1461 with Dissolve(1)
    er "..."
    mc "{i}(Are you kidding me?){/i}"
    mc "Puppy dog eyes... Really?"
    er "..."
    mc "Fine... FINE!"
    scene 11_1462 with Dissolve(1)
    er "Hehe. Still works!"
    er "Have you used it before, Lexi?"
    mc "She has!"
    a "Haha."
    mc "It's so dumb. It's. So. Dumb!"
    scene 11_1463 with Dissolve(1)
    ir "And here's mine!"
    mc "Really, Iris? I thought you were on my side?"
    ir "I am."
    mc "..."
    ir "Thank you!"
    scene 11_1464 with Dissolve(1)
    mc "Now I know why I was invited. To carry all your shit!"
    er "You offered!"
    mc "I offered to carry Lexi's. The rest of you weaselled your way to me carrying your bags."
    er "Weaselled... Haha."
    scene 11_1465 with Dissolve(1)
    er "He's cute when he's angry."
    a "Haha, yeah."
    ir "You need to see him when he's really angry and not pretending. So cute!"
    mc "..."
    scene 11_1466 with Dissolve(1)
    mc "{i}(Heh...){/i}"
    mc "{i}(She isn't wasting any time, huh?){/i}"
    if Erynn_LikeMC == True:
        mc "{i}(I wish it was my hand though.){/i}"
    else:
        pass
    scene 11_1467 with Dissolve(1)
    ir "..."
    mc "*Shakes head*"
    scene black with Dissolve(1)
    pause 2
    scene 11_1468 with Dissolve(1)
    er "Shall we set up here? It's a little away from where all the tourists go."
    a "Seems good to me."
    er "Or we can..."
    mc "Nope! This is the spot!"
    er "Haha. Sure. Thanks for carrying our stuff."
    scene 11_1469 with Dissolve(1)
    ""
    menu:
        "Watch Alexis[KoGa3AutoWTChange1]{size=-4}(Alexis BeachPoints+2) {/size} {/color}":
            $ Alexis_BeachPoints += 2
            # Alexis_Beach (2)
            scene 11_1470 with Dissolve(1)
            mc "..."
            a "*Whispers* Enjoying the view?"
            ir "Let me help you, Erynn."
            scene 11_1473 with Dissolve(1)
            mc "*Whispers* I am!"
            mc "*Whispers* Can't wait to sunscreen them up!"
            a "Heh."
            scene 11_1474 with Dissolve(1)
            mc "Uh..."
            scene 11_1475 with vpunch
            a "Aah-haha."
            scene 11_1476 with Dissolve(1)
            er "Really guys? I just finished straightening the blanket..."
            a "Sorry!"
            a "[mc], stop. And help me fix the blanket."
            mc "*Sigh*"
        "Watch Erynn[KoGa3AutoWTChange1]{size=-4}(Alexis JealousyPoints+2) {/size} {/color}":
            $ Alexis_JealousyPoints += 2
            # Alexis_Jealous (8)
            scene 11_1471 with Dissolve(1)
            mc "..."
            a "Enjoying the view?"
            mc "Yeah."
            scene 11_1477 with Dissolve(1)
            mc "{i}(Oh shit!){/i}"
            mc "Ha-ha... Sorry..."
            a "Uh-huh."
            scene 11_1478 with Dissolve(1)
            mc "No, really. I'm sorry."
        "Watch Iris[KoGa3AutoWTChange1]{size=-4}(Alexis JealousyPoints+2) {/size} {/color}":
            $ Alexis_JealousyPoints += 2
            # Alexis_Jealous (8)
            scene 11_1472 with Dissolve(1)
            a "Enjoying the view?"
            mc "Yeah."
            mc "..."
            scene 11_1477 with Dissolve(1)
            mc "{i}(Oh shit!){/i}"
            mc "Ha-ha... Sorry..."
            a "Uh-huh."
            scene 11_1478 with Dissolve(1)
            mc "No, really. I'm sorry."
        "Do nothing":
            pass
    scene black with Dissolve(1)
    pause 2
    scene 11_1479 with Dissolve(1)
    ir "Is it weird for you that you're hanging out with your ex and your current girlfriend?"
    mc "{i}(And the girl I had a crush on.){/i}"
    if Erynn_LikeMC == True:
        mc "{i}(Still have.){/i}"
    else:
        pass
    mc "A little maybe? But it's the same for you guys, no?"
    ir "I'm fine with it."
    if Zach_Week3_Wednesday_TC_Girlshower == False:
        mc "{i}(Course you are. You even watched us having sex.){/i}"
    else:
        pass
    scene 11_1480 with Dissolve(1)
    mc "Are you cool with it? Otherwise we can go somewhere else by ourselves."
    er "Hey! You're not leaving us!"
    a "I'm okay with it."
    a "We can go another time. Let's stay together for today."
    scene 11_1481 with Dissolve(1)
    a "What are you doing?"
    mc "I want to see your pretty eyes!"
    a "Hmm-really..."
    mc "No. Well, you do have pretty eyes but I like your sunglasses and want to try them. Can I?"
    a "Haha. Sure."
    scene 11_1482 with Dissolve(1)
    mc "What do you think?"
    a "Looks good. They suit you."
    mc "Yeah? Let me get my phone. I want to see for myself."
    scene 11_1483 with Dissolve(1)
    er "Let me take the picture for you."
    mc "Thanks."
    er "You get in the picture too, Lexi!"
    scene 11_1484 with Dissolve(1)
    er "Alright."
    er "Smile!"
    scene 11_1485 with Dissolve(1)
    er "So cute, right?"
    ir "The cutest!"
    scene 11_1486 with Dissolve(1)
    mc "Let's see!"
    mc "Damn, I'm so good-looking!"
    a "Haha. And not at all conceited."
    mc "Right? Where do you find guys like that? You're such a lucky girl!"
    a "*Shakes head*"
    scene 11_1487 with Dissolve(1)
    mc "By the way. I'm keeping these. They're mine now!"
    a "No-no-no! Like hell they are! You can borrow them. For today only!"
    mc "At least tell me where you got them."
    a "We can go shopping next time and get you a pair."
    if Erynn_Week5_Tuesday_Photoshoot_Join == True:
        mc "Deal. I earned two hundred bucks from the photo shoot, so I have some money to spend."
    else:
        mc "Deal."
    scene 11_1488 with Dissolve(1)
    mc "You want me to take a picture of you guys?"
    ir "Yes! YES!"
    er "Sure."
    mc "Get a little closer then."
    scene 11_1489 with Dissolve(1)
    mc "{i}(A little closer...){/i}"
    mc "{i}(Seeing them together last time and now this...){/i}"
    mc "{i}(I can't unsee it.){/i}"
    scene 11_1490 with Dissolve(1)
    mc "When I saw you together last time, I thought this already..."
    mc "You actually look so much alike. You two could be sisters."
    er "You think?"
    a "Yeah. Now that you mention it. I can see some similarities."
    ir "What? NO! Don't say that! We can't be sisters! Don't ruin our moment! Let's take another picture!"
    mc "Haha."
    scene 11_1491 with Dissolve(1)
    er "Iris! What are you doing?"
    ir "Proving we are not sisters!"
    er "Haha."
    scene 11_1492 with Dissolve(1)
    er "Since we're taking pictures, I have to show you one."
    er "You guys went to a costume shop a few days ago, right?"
    a "Mm-hmm."
    mc "{i}(Is it Erynn dressed up? For a photo shoot maybe?){/i}"
    scene 11_1493 with Dissolve(1)
    a "Oh no... Erynn... What did you do?"
    a "The poor boy."
    mc "{i}(Boy?){/i}"
    ir "Well that explains a lot of things!"
    a "Please, send me that."
    er "Haha. Sure."
    scene 11_1494 with Dissolve(1)
    mc "What's so funny?"
    a "You don't want to see this."
    er "Just my old dress-up doll."
    mc "{i}(Dress-up doll...? No...){/i}"
    mc "Show me!"
    scene 11_1495 with Dissolve(1)
    mc "..."
    mc "Are you kidding me?"
    er "Remember this?"
    mc "I don't want to remember that! Why do you even have that?"
    er "I told you I have lots of pictures from when you were younger."
    a "You've gotta show me all of them."
    mc "How about no!"
    scene 11_1496 with Dissolve(1)
    a "Let me see that one again."
    a "I didn't notice before, but you even put makeup on him."
    er "He didn't mind the blush and the eyeliner."
    er "But he drew the line at lipstick. Said it was too girly."
    scene 11_1497 with Dissolve(1)
    a "Honestly. You don't look bad with makeup on. It's kinda cute."
    a "Let me put some makeup on you next time."
    mc "Uh-huh..."
    mc "That reminds me. Two can play that game, Lexi!"
    scene 11_1498 with Dissolve(1)
    mc "What do you think?"
    a "..."
    er "Lex! What happened there?"
    scene 11_1499 with Dissolve(1)
    a "That's when you did my makeup."
    a "Layla must have sent you that!"
    mc "Indeed!"
    scene 11_1500 with Dissolve(1)
    a "Delete it!"
    mc "Nope. Not gonna happen!"
    a "Give me your phone!"
    mc "Not gonna happen, either."
    scene 11_1501 with Dissolve(1)
    a "[mc], give it!"
    mc "No!"
    ir "Haha. Are you taking a picture?"
    er "Uh-huh."
    scene 11_1502 with Dissolve(1)
    er "Oh... Hey, Valeria!"
    va "Hey, Erynn."
    mc "{i}(Val?){/i}"
    scene 11_1503 with Dissolve(1)
    mc "..."
    a "Hey!"
    va "Hey, Alexis, [mc]."
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 11_1504 at moveup
    pause 3
    mc "Hey..."
    if Valeria_LikeMC == True:
        scene 11_1505 with Dissolve(1)
        mc "White?"
        mc "Haven't you learned?"
        va "Shhh..."
    else:
        pass
    scene 11_1506 with Dissolve(1)
    if Valeria_LikeMC == True:
        mc "{i}(She wasn't kidding when she said she'll go to the beach with Darryl...){/i}"
    else:
        mc "{i}(What's she doing with those guys?){/i}"
    mc "{i}(Why does Darryl have a guitar?){/i}"
    mc "{i}(Trying to serenade Valeria?){/i}"
    mc "{i}(I bet he can't even play.){/i}"
    scene 11_1507 with Dissolve(1)
    a "Got it!"
    a "Thanks for the distraction, Valeria!"
    mc "..."
    va "Uhm... You're welcome?"
    scene 11_1508 with Dissolve(1)
    da "Three girls this time..."
    da "Seriously. Who is this guy?"
    tj "No idea, man."
    da "You know them, Val?"
    scene 11_1509 with Dissolve(1)
    va "A little? The long-haired blonde is Erynn."
    da "Yeah, I know who Erynn is."
    va "The brunette is Alexis, Layla's sister."
    da "Layla? As in Layla from the track team? Didn't know she had a sister."
    va "I don't know who the other blonde is."
    if Tori_Week3_Saturday_TC_Sex == True:
        scene black with Dissolve(1)
        transform moveup:
            xalign 0.5 yalign 1.0
            linear 5.0 yalign 0.0
        show 11_1510 at moveup
        pause 3
        mc "{i}(Looking good, Tori!){/i}"
        mc "{i}(I get horny just from looking at her.){/i}"
    else:
        pass
    scene 11_1511 with Dissolve(1)
    a "Your phone is locked. Can you unlock it?"
    mc "What?"
    a "Your phone? It's locked."
    mc "Oh. Yeah..."
    scene 11_1512 with Dissolve(1)
    mc "{i}(Look at his smug face.){/i}"
    mc "{i}(Like you have a chance with her...){/i}"
    a "What are you looking at?"
    mc "The guitar..."
    a "You should've brought yours!"
    scene 11_1513 with Dissolve(1)
    a "I didn't know you know Valeria."
    er "I met her when I drove [mc] to school right before the training camp. She's Zach's girlfriend."
    a "Zach's girlfriend? We're talking about the same Zach, right? [mc]'s friend?"
    mc "{i}(Friend...){/i}"
    mc "She isn't Zach's girlfriend!"
    scene 11_1514 with Dissolve(1)
    er "No? Hmm... I thought she was. She seemed very annoyed when Zach tried to flirt with me."
    a "Who isn't annoyed with Zach?"
    mc "Exactly."
    scene 11_1515 with Dissolve(1)
    er "Back to the pictures."
    er "Do you still have pictures of you and [mc]?"
    ir "I have some, yeah."
    er "Can we look at them?"
    scene 11_1516 with Dissolve(1)
    er "Sorry, Lexi. I should've asked you first if you'd mind..."
    a "It's fine. They had a history together and nothing will change that."
    mc "What about me? Maybe I mind?"
    ir "No, you don't."
    mc "Heh... I guess I have no say in this..."
    scene 11_1517 with Dissolve(1)
    er "Iris! You had long hair?"
    er "I didn't know that."
    ir "I cut it when I moved here."
    scene 11_1518 with Dissolve(1)
    er "Was there a special reason for it?"
    ir "Not really. New beginning, I guess."
    er "I like the long hair."
    ir "Yeah? I might grow it out again."
    mc "{i}(Don't try too hard, Iris!){/i}"
    scene 11_1519 with Dissolve(1)
    er "Look at his face! So cute."
    er "Can you send me that picture? I don't have any of [mc] from his time in Alvarado."
    ir "Sure."
    scene 11_1520 with Dissolve(1)
    mc "{i}(It's fine...){/i}"
    mc "{i}(That doesn't look like it's fine.){/i}"
    menu:
        "Comfort her[KoGa3AutoWTChange1]{size=-4}(Alexis BeachPoints+2) {/size} {/color}":
            $ Alexis_BeachPoints += 2
            # Alexis_Beach (4)
            scene 11_1521 with Dissolve(1)
            a "..."
        "Don't[KoGa3AutoWTChange1]{size=-4}(Alexis JealousyPoints+2) {/size} {/color}":
            $ Alexis_JealousyPoints += 2
            # Alexis_Jealous (10)
            mc "{i}(Well... She could've said no.){/i}"
    scene 11_1522 with Dissolve(1)
    er "Haha. That looks fun."
    a "Hmm... I think I've seen that guy before. He seems familiar. But I can't remember where from."
    ir "Nathan?"
    a "I don't know. I could be wrong though."
    scene 11_1523 with Dissolve(1)
    er "John teaching [mc] to ride a bike."
    a "That's your dad, Iris?"
    ir "Uh-huh."
    er "He's a hottie, right?"
    a "He is!"
    mc "..."
    scene 11_1524 with Dissolve(1)
    er "Oh..."
    ir "Ups!"
    scene 11_1525 with Dissolve(1)
    a "Uhm..."
    er "Iris!"
    ir "Haha. Sorry. Didn't mean to show that one."
    scene 11_1526 with Dissolve(1)
    mc "What picture are you talking about?"
    mc "Can I see for a sec?"
    er "No!"
    a "No, you can't!"
    scene 11_1527 with Dissolve(1)
    mc "Oh, come on!"
    mc "I've probably seen it before!"
    er "Another reason why you don't need to see it!"
    mc "..."
    scene 11_1528 with Dissolve(1)
    er "How did you guys actually meet? Did you go to school together?"
    a "They met in a park."
    er "Oh, you know?"
    a "[mc] told me. But I'd like to hear Iris's story too."
    scene 11_1530 with Dissolve(1)
    ir "Funny enough. It started with a picture."
    mc "Not this again..."
    er "Let her tell the story!"
    mc "*Sigh*"
    if Valeria_LikeMC == True:
        scene 11_1531 with Dissolve(1)
        mc "..."
        scene 11_1532 with Dissolve(1)
        mc "{i}(Get your hands off of her!){/i}"
        mc "{i}(Remove his hand from your leg, Val!){/i}"
    else:
        pass
    scene 11_1533 with Dissolve(1)
    mc "I'm going to the bar and get an iced coffee or something."
    mc "Anyone want anything?"
    ir "Can you get me caramel macchiato? Thanks."
    er "Same for me."
    a "Make that three."
    scene 11_1534 with Dissolve(1)
    mc "Alright. Be right back."
    a "Thank you!"
    er "Thanks, [mc]."
    scene black with Dissolve(1)
    pause 2
    scene 11_1535 with Dissolve(1)
    ""
    if Tori_End == False:
        scene 11_1538 with Dissolve(1)
        mc "..."
        to "Guess who. And you'd better answer correctly!"
        scene 11_1539 with Dissolve(1)
        mc "Sup, Tori."
        mc "What do you want?"
        scene 11_1540 with Dissolve(1)
        to "I think you know what I want!"
        mc "Uh..."
        mc "I'm here with my friends."
        if Tori_Week3_Saturday_TC_Sex == True:
            to "What does that matter? I saw you looking at me!"
        else:
            to "What does that matter?"
            mc "{i}(I rejected her last time, but she keeps on trying.){/i}"
            menu:
                "Reject Tori[KoGa3AutoWTChange1]{size=-4}(Tori End) {/size} {/color}":
                    $ Tori_End = True
                    scene 11_1541 with Dissolve(1)
                    mc "How many times do I have to tell you that I'm not interested?"
                    mc "Leave already."
                    to "..."
                    if Tori_Sex == True:
                        to "If you weren't interested, we wouldn't have fucked!"
                    else:
                        pass
                    scene 11_1543 with Dissolve(1)
                    to "*Sigh*"
                    to "*You're so fucking boring!"
                    mc "{i}(That girl has problems.){/i}"
                    scene 11_1536 with Dissolve(1)
                    bt "Hi."
                    mc "Hey."
                    bt "What can I get you?"
                    mc "Four caramel macchiato, please."
                    scene 11_1537 with Dissolve(1)
                    bt "Here you go!"
                    mc "Thanks."
                    scene 11_1586 with Dissolve(1)
                    er "That was quick."
                    mc "Yeah. Wasn't that busy."
                    jump Week5_Wednesday_Beach2_Alexis
                "Go with Tori[KoGa3AutoWTChange1]{size=-4}(Tori Points+2, Tori Week5 Wednesday Beach Sex, Valeria Friends, Valeria LikeMCFalse) {/size} {/color}":
                    $ Tori_Points += 2
                    # Tori (18)
                    $ Tori_Week5_Wednesday_Beach_Sex = True
                    $ Valeria_Friends = True
                    $ Valeria_LikeMC = False
                    jump Week5_Wednesday_Beach_Tori
        scene 11_1541 with Dissolve(1)
        mc "What about Darryl?"
        to "What about him?"
        mc "Aren't you here with him?"
        to "He's busy with Valeria. Besides. I have more fun with you!"
        scene 11_1542 with Dissolve(1)
        to "Can we go already?"
        to "I'm fucking horny!"
        menu:
            "Go with her[KoGa3AutoWTChange1]{size=-4}(Tori Points+2, Tori Week5 Wednesday Beach Sex) {/size} {/color}":
                $ Tori_Points += 2
                # Tori (18)
                $ Tori_Week5_Wednesday_Beach_Sex = True
                jump Week5_Wednesday_Beach_Tori
            "Stay[KoGa3AutoWTChange1]{size=-4}(Tori Points-2) {/size} {/color}":
                $ Tori_Points -= 2
                mc "I can't, Tori. I..."
                scene 11_1543 with Dissolve(1)
                to "*Sigh*"
                to "*Why is everyone so fucking boring?"
                mc "{i}(What the fuck is her problem again?){/i}"
                scene 11_1536 with Dissolve(1)
                bt "Hi."
                mc "Hey."
                bt "What can I get you?"
                mc "Four caramel macchiato, please."
                scene 11_1537 with Dissolve(1)
                bt "Here you go!"
                mc "Thanks."
                scene 11_1586 with Dissolve(1)
                er "That was quick."
                mc "Yeah. Wasn't that busy."
                jump Week5_Wednesday_Beach2_Alexis
    else:
        scene 11_1536 with Dissolve(1)
        bt "Hi."
        mc "Hey."
        bt "What can I get you?"
        mc "Four caramel macchiato, please."
        scene 11_1537 with Dissolve(1)
        bt "Here you go!"
        mc "Thanks."
        scene 11_1586 with Dissolve(1)
        er "That was quick."
        mc "Yeah. Wasn't that busy."
        jump Week5_Wednesday_Beach2_Alexis

label Week5_Wednesday_Beach_Tori:
    if _in_replay:
        $ SexCounter_Tori = 2
        $ MC_SexCounter = 2
        $ Tori_Sex = True
    $ SexCounter_Tori += 1
    $ MC_SexCounter += 1
    scene 11_1544 with Dissolve(1)
    to "Come on!"
    mc "Where are we going?"
    to "Just follow me."
    scene 11_1545 with Dissolve(1)
    mc "{i}(I guess this place is as good as any.){/i}"
    mc "{i}(Fuck. This girl gets me excited like no one else...){/i}"
    scene 11_1546 with vpunch
    to "Heh..."
    scene 11_1547 with Dissolve(1)
    to "See! So much more fun!"
    mc "{i}(She should smile more often.){/i}"
    scene 11_1548 with Dissolve(1)
    mc "{i}(This kiss is amazing.){/i}"
    mc "{i}(These plump lips. Perfect to suck on.){/i}"
    scene 11_1549 with vpunch
    mc "..."
    mc "What now?"
    if Tori_Sex == False:
        $ Tori_Sex = True
        to "We're not kissing!"
    else:
        to "I've told you before. We're not doing the kissing shit."
    mc "What's the big deal? Scared you'll grow feelings for me?"
    to "Don't flatter yourself. You have a good dick, that's it!"
    scene 11_1550 with vpunch
    to "Ahh..."
    mc "*Whispers* Fine!"
    mc "No kissing!"
    to "..."
    scene 11_1551 with Dissolve(1)
    mc "{i}(I'll keep this for later!){/i}"
    scene 11_1552 with Dissolve(1)
    ""
    scene 11_1553 with Dissolve(1)
    to "How about you take them off?"
    mc "Stop being so impatient and let me do my thing!"
    scene 11_1554 with Dissolve(1)
    ""
    scene 11_1555 with Dissolve(1)
    to "Mmm... Yeah. Suck that pussy!"
    to "Suck it hard!"
    scene 11_1556 with Dissolve(1)
    ""
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 11_1557 at moveup
    pause 3
    mc "Your body is fucking insane, Tori!"
    to "Of course it is!"
    mc "..."
    scene 11_1558 with Dissolve(1)
    mc "{i}(So are those tits!){/i}"
    scene 11_1561 with Dissolve(1)
    mc "Were you in the water? Why is this pussy so wet?"
    to "Shut up and continue!"
    scene 11_1560 with Dissolve(1)
    to "Ahh..."
    scene 11_1559 with Dissolve(1)
    to "*Moaning*"
    scene 11_1562 with Dissolve(1)
    to "You really like your foreplay, huh?"
    mc "You only said no to kissing! Nothing about sucking your tits or fingering you!"
    to "You need to look up the definition of a quickie!"
    mc "Who says this is a quickie? I have time. Do you need to be somewhere?"
    to "Stop talking and fuck me already!"
    scene 11_1563 with Dissolve(1)
    mc "You're cute when you're annoyed."
    to "Oh my god... Are we here to fuck or to talk?"
    to "If it's the latter, get out and I'll find someone else."
    mc "Haha. You won't find anyone else who fucks you as well as I do."
    mc "That's why you keep coming back!"
    to "..."
    scene 11_1564 with Dissolve(1)
    to "Do I have to do everything myself?"
    to "See!"
    to "Not that difficult!"
    scene 11_1565 with Dissolve(1)
    to "Your dick goes in my pussy! Simple!"
    to "And now fuck me hard!"
    scene 11_1566 with Dissolve(1)
    to "Ahhh..."
    scene 11_1567 with Dissolve(1)
    to "I said hard!"
    show 11_1568
    to "*Moaning*"
    to "Ah-ah-ah..."
    show 11_1569
    mc "Your pussy feels so good!"
    mc "{i}(When I'm finished with you, you won't want to fuck anyone else anymore!){/i}"
    scene 11_1570 with Dissolve(1)
    to "Put it back in! We're not done here!"
    mc "Gimme a sec..."
    scene 11_1571 with Dissolve(1)
    to "Ready to shoot your load already? I expected more of you!"
    mc "How about you shut up now!?"
    to "Heh..."
    menu:
        "Eat her pussy":
            scene 11_1572 with Dissolve(1)
            to "Ahhh..."
            mc "{i}(I knew you'd enjoy this!){/i}"
            scene 11_1574 with Dissolve(1)
            mc "{i}(So do I!){/i}"
            mc "{i}(She tastes so great!){/i}"
        "Lick her ass[KoGa3AutoWTChange1]{size=-4}(Tori Week5 Wednesday Beach LickAss, Tori LickAss) {/size} {/color}":
            $ Tori_Week5_Wednesday_Beach_LickAss = True
            $ Tori_LickAss = True
            scene 11_1572 with Dissolve(1)
            to "Ahhh..."
            mc "{i}(I knew you'd enjoy this!){/i}"
            scene 11_1573 with Dissolve(1)
            mc "{i}(So do I!){/i}"
            mc "{i}(I love eating her ass!){/i}"
    scene 11_1575 with Dissolve(1)
    mc "You'd better be ready now!"
    to "I hope those aren't empty words."
    mc "You know I don't do empty!"
    scene 11_1577 with Dissolve(1)
    to "Aaah..."
    mc "You like that!"
    scene 11_1576 with Dissolve(1)
    mc "{i}(This feels so fucking good!){/i}"
    scene 11_1578 with Dissolve(1)
    to "Faster... Faster!"
    show 11_1579
    ""
    scene 11_1580 with vpunch
    mc "..."
    mc "{i}(I wanted to hold out for longer, but...){/i}"
    scene 11_1581 with vpunch
    mc "Ah..."
    scene 11_1582 with Dissolve(1)
    mc "Fuck, this was great!"
    mc "You were right. We should do this more often!"
    to "You're finally realising!"
    scene 11_1583 with Dissolve(1)
    mc "How about we hang out sometime?"
    to "Heh... Just get out! We fuck, that's it!"
    mc "Wait..."
    mc "Let me at least put my pants back on first."
    $ renpy.end_replay()
    scene 11_1584 with Dissolve(1)
    mc "{i}(She's got me wrapped around her finger.){/i}"
    mc "{i}(But somehow, I don't mind.){/i}"
    mc "{i}(I wouldn't mind spending some more time with her, though!){/i}"
    scene 11_1536 with Dissolve(1)
    bt "Hi."
    mc "Hey."
    bt "What can I get you?"
    mc "Four caramel macchiato, please."
    scene 11_1585 with Dissolve(1)
    mc "..."
    scene 11_1537 with Dissolve(1)
    bt "Here you go!"
    mc "Thanks."
    scene 11_1586 with Dissolve(1)
    er "You were gone a while."
    mc "Yeah. There was quite a line."
    if Alexis_SecretPath == True:
        jump Week5_Wednesday_Beach2_Alexis_SP
    else:
        jump Week5_Wednesday_Beach2_Alexis

label Week5_Wednesday_Beach2_Alexis:
    scene 11_1587 with Dissolve(1)
    mc "Here you go. Everyone take one."
    er "Thank you. They're all the same?"
    mc "Yeah."
    a "Thanks, babe."
    scene 11_1588 with Dissolve(1)
    er "Iris told us how you met. About that picture..."
    mc "*Sigh* I know, okay? It was a mistake and I was punished for it."
    ir "That's what I was? Punishment?"
    mc "Oh, come on... You know what I mean."
    scene 11_1589 with Dissolve(1)
    er "..."
    a "..."
    scene 11_1590 with Dissolve(1)
    er "..."
    mc "{i}(What the fuck are they doing?){/i}"
    scene 11_1591 with Dissolve(1)
    mc "Are you seriously having a conversation by just looking at each other?"
    mc "Girls are so weird."
    er "..."
    mc "Oh... I know what those looks mean! Run!"
    scene 11_1592 with Dissolve(1)
    mc "That reminds me of that one meme."
    mc "When that guy says run and then the music. Duuh-duh-duh-duh-duh. You know it?"
    er "And you say girls are weird..."
    mc "Haha."
    scene black with Dissolve(1)
    pause 2
    scene 11_1593 with Dissolve(1)
    ir "Let's play a game, [mc]."
    ir "Us three girls. Kill-Fuck-Marry. Go!"
    mc "Hell no!"
    ir "What? Why not?"
    mc "Because girls are emotional and someone will get their feelings hurt. And I'll be labelled as the bad guy."
    scene 11_1594 with Dissolve(1)
    ir "No... It's just for fun."
    ir "We'll play too, right?"
    er "Yeah, why not?"
    scene 11_1595 with Dissolve(1)
    mc "*Sigh* Fine... I guess..."
    ir "Cool. You start."
    mc "Alright. Let's see."
    mc "{i}(This can only end badly, no?){/i}"
    mc "Kill... Hmm..."
    menu:
        "Alexis[KoGa3AutoWTChange1]{size=-4}(Alexis BeachPoints-2, KFM Kill Alexis) {/size} {/color}":
            $ Alexis_BeachPoints -= 2
            $ KFM_Kill_Alexis = True
            scene 11_1604 with Dissolve(1)
            mc "Sorry, but I'll have to kill you, Lexi..."
            a "What? Why me? I'm your girlfriend!"
            mc "I had to pick someone to kill, and..."
            scene 11_1605 with Dissolve(1)
            a "Not if I kill you first!"
            mc "Haha."
            mc "Don't spill your coffee!"
            scene 11_1606 with Dissolve(1)
            ir "Who do you fuck and marry?"
            a "He won't be able to do either when he's dead!"
            mc "Haha."
            mc "{i}(Maybe I should've picked someone else.){/i}"
            scene 11_1607 with Dissolve(1)
            ir "So?"
            mc "I still have to answer?"
            ir "Well yeah!"
            mc "Hmm... Okay. I'll..."
            menu:
                "Fuck Erynn[KoGa3AutoWTChange1]{size=-4}(KFM Fuck Erynn, KFM Marry Iris, {i}Erynn LikeMC: Alexis JealousyPoints+4{/i}, {i}else: Alexis JealousyPoints+2{/i}) {/size} {/color}":
                    $ KFM_Fuck_Erynn = True
                    $ KFM_Marry_Iris = True
                    scene 11_1608 with Dissolve(1)
                    if Erynn_LikeMC == True:
                        $ Alexis_JealousyPoints += 4
                        # Alexis_Jealous (14)
                        mc "{i}(If I'm being honest. I'd love to have sex with Erynn at least once.){/i}"
                    else:
                        $ Alexis_JealousyPoints += 2
                    mc "I'll fuck Erynn and marry Iris."
                    er "Oh..."
                    ir "I was fine with either one. But sure. I'll marry you."
                    a "..."
                "Fuck Iris[KoGa3AutoWTChange1]{size=-4}(Alexis JealousyPoints+2, KFM Fuck Iris, KFM Marry Erynn) {/size} {/color}":
                    $ Alexis_JealousyPoints += 2
                    $ KFM_Fuck_Iris = True
                    $ KFM_Marry_Erynn = True
                    scene 11_1609 with Dissolve(1)
                    mc "I'll fuck Iris and marry Erynn."
                    er "Oh... Thanks."
                    ir "I was fine with either one. So, sure. Let's fuck."
                    a "..."
        "Erynn[KoGa3AutoWTChange1]{size=-4}(KFM Kill Erynn, {i}Erynn LikeMC: Erynn Points-4{/i}) {/size} {/color}":
            $ KFM_Kill_Erynn = True
            if Erynn_LikeMC == True:
                $ Erynn_Points -= 4
            else:
                pass
            scene 11_1610 with Dissolve(1)
            mc "Sorry, Erynn. But I'll have to kill you."
            er "What? Why would you kill me? I'm always nice to you..."
            mc "I can't kill my girlfriend and if I kill Iris, John kills me."
            mc "And you've seen John. It won't be pretty!"
            ir "Haha. You're right about that."
            er "Still..."
            scene 11_1611 with Dissolve(1)
            mc "Sorry."
            mc "You can kill me when it's your turn."
            er "..."
            menu:
                "Fuck Alexis[KoGa3AutoWTChange1]{size=-4}(Alexis BeachPoints+2, KFM Fuck Alexis, KFM Marry Iris) {/size} {/color}":
                    $ Alexis_BeachPoints += 2
                    # Alexis_Beach (6)
                    $ KFM_Fuck_Alexis = True
                    $ KFM_Marry_Iris = True
                    scene 11_1597 with Dissolve(1)
                    mc "Fuck and marry... I'll fuck Alexis."
                    mc "I'm doing that already, so..."
                    a "[mc]!"
                    mc "What? As if they don't know."
                    a "*Shakes head*"
                    scene 11_1612 with Dissolve(1)
                    mc "And then marry Iris."
                    ir "Sure. I'd marry you!"
                    a "..."
                    a "You'd rather marry Iris than me?"
                    mc "I knew this would happen. I hate this game."
                    scene 11_1599 with Dissolve(1)
                    mc "See it this way. If I marry you and fuck Iris. I'd be cheating on you."
                    a "Hmm... I see your point."
                    ir "We can have a threesome!"
                    a "No, thanks!"
                "Fuck Iris[KoGa3AutoWTChange1]{size=-4}(Alexis BeachPoints+4, KFM Fuck Iris, KFM Marry Alexis) {/size} {/color}":
                    $ Alexis_BeachPoints += 4
                    # Alexis_Beach (8)
                    $ KFM_Fuck_Iris = True
                    $ KFM_Marry_Alexis = True
                    scene 11_1613 with Dissolve(1)
                    mc "I guess I'll fuck Iris and marry Lexi."
                    ir "I was okay with both choices. So yeah, let's fuck!"
                    a "..."
                    mc "{i}(I hope Alexis won't be mad that I picked Iris to fuck and not her.){/i}"
                    scene 11_1601 with Dissolve(1)
                    a "But we'll wait like three years until we get married!"
                    mc "{i}(Okay. She's not mad.){/i}"
                    mc "Three? That's way too early. More like ten years!"
                    a "Ten? I'll be thirty! That's way too late! I wanna have kids by that age."
                    mc "What? Kids?"
                    if Erynn_LikeMC == False:
                        scene 11_1602 with Dissolve(1)
                        ir "They sound like an old married couple already."
                        er "Haha."
                    else:
                        scene 11_1603 with Dissolve(1)
                        ir "They sound like an old married couple already."
                        er "..."
        "Iris[KoGa3AutoWTChange1]{size=-4}(KFM Kill Iris) {/size} {/color}":
            $ KFM_Kill_Iris = True
            scene 11_1596 with Dissolve(1)
            mc "I'll kill you, Iris!"
            mc "Because you made us play this stupid game!"
            ir "Haha."
            ir "If that's the only reason, I'm fine with it."
            menu:
                "Fuck Alexis[KoGa3AutoWTChange1]{size=-4}(Alexis BeachPoints+2, Alexis JealousyPoints+4, KFM Fuck Alexis, KFM Marry Erynn) {/size} {/color}":
                    $ Alexis_BeachPoints += 2
                    # Alexis_Beach (6)
                    $ Alexis_JealousyPoints += 4
                    # Alexis_Jealous (14)
                    $ KFM_Fuck_Alexis = True
                    $ KFM_Marry_Erynn = True
                    scene 11_1597 with Dissolve(1)
                    mc "I'll fuck Alexis."
                    mc "I'm doing that already, so..."
                    a "[mc]!"
                    mc "What? As if they don't know."
                    a "*Shakes head*"
                    scene 11_1598 with Dissolve(1)
                    mc "And then marry Erynn."
                    er "Oh... Thanks."
                    a "You'd rather marry Erynn than me?"
                    mc "I knew this would happen. I hate this game."
                    scene 11_1599 with Dissolve(1)
                    mc "See it this way. If I marry you and fuck Erynn. I'd be cheating on you."
                    a "Hmm... I see your point."
                    if Erynn_LikeMC == True:
                        mc "{i}(If I'm being honest. I'd love to have sex with Erynn at least once.){/i}"
                    else:
                        pass
                    ir "You guys are still better off than me. He killed me!"
                "Fuck Erynn[KoGa3AutoWTChange1]{size=-4}(Alexis BeachPoints+4, Alexis JealousyPoints+2, KFM Fuck Erynn, KFM Marry Alexis) {/size} {/color}":
                    $ Alexis_BeachPoints += 4
                    # Alexis_Beach (8)
                    $ Alexis_JealousyPoints += 2
                    $ KFM_Fuck_Erynn = True
                    $ KFM_Marry_Alexis = True
                    scene 11_1600 with Dissolve(1)
                    mc "I guess I'll fuck Erynn and marry Lexi."
                    er "Oh..."
                    mc "{i}(I hope Alexis won't be mad that I picked Erynn to fuck and not her.){/i}"
                    if Erynn_LikeMC == True:
                        mc "{i}(If I'm being honest. I'd love to have sex with Erynn at least once.){/i}"
                    else:
                        pass
                    scene 11_1601 with Dissolve(1)
                    a "But we'll wait like three years until we get married!"
                    mc "{i}(Okay. She's not mad.){/i}"
                    mc "Three? That's way too early. More like ten years!"
                    a "Ten? I'll be thirty! That's way too late! I wanna have kids by that age."
                    mc "What? Kids?"
                    if Erynn_LikeMC == False:
                        scene 11_1602 with Dissolve(1)
                        ir "They sound like an old married couple already."
                        er "Haha."
                    else:
                        scene 11_1603 with Dissolve(1)
                        ir "They sound like an old married couple already."
                        er "..."
    scene 11_1614 with Dissolve(1)
    mc "Alright. That was actually tough..."
    mc "Now it's your turn."
    mc "Let's hear your choices, Iris."
    ir "Sure."
    scene 11_1615 with Dissolve(1)
    ir "I'll kill Alexis!"
    mc "Wow. Right off the bat."
    er "That's unexpected. Why Lex?"
    ir "That way I don't have to share the dorm room anymore."
    a "Heh... Good to know. But if I'm not there you'll probably get a new roommate. And who knows what she'd be like..."
    mc "{i}(Catfight incoming.){/i}"
    scene 11_1616 with Dissolve(1)
    ir "I'll fuck Erynn. And marry [mc]!"
    er "Uh..."
    mc "Wanna explain those choices?"
    ir "Because... Reasons."
    mc "{i}(Reasons...){/i}"
    scene 11_1617 with Dissolve(1)
    mc "Next. Let's go with Lexi, now."
    a "Kill Iris! Because reasons!"
    mc "Haha."
    mc "{i}(Round two!){/i}"
    mc "{i}(I'm so happy I picked first. This is only getting worse.){/i}"
    scene 11_1618 with Dissolve(1)
    a "Fuck and marry..."
    a "Hmm... Normally I wouldn't have sex with another woman but if I had to, I'd pick Erynn."
    a "So, I'll fuck Erynn and marry [mc]."
    if KFM_Fuck_Erynn == True:
        scene 11_1619 with Dissolve(1)
        mc "Everyone wants to have sex with Erynn, it seems."
        er "..."
        mc "{i}(She's blushing.){/i}"
        mc "{i}(I don't know if she's uncomfortable with that, or happy.){/i}"
    else:
        pass
    scene 11_1620 with Dissolve(1)
    mc "I'm actually curious now."
    mc "Here's a question."
    mc "Have you two ever kissed each other?"
    scene 11_1621 with Dissolve(1)
    a "..."
    er "..."
    mc "Holy shit! You have!"
    scene 11_1622 with Dissolve(1)
    mc "Was it just a peck on the lips or a full make-out sesh?"
    mc "Or more like a dare or something?"
    a "We're not telling you!"
    mc "Oh, come on!"
    a "No!"
    mc "{i}(I really want to know, now.){/i}"
    scene 11_1623 with Dissolve(1)
    mc "{i}(Damn...){/i}"
    mc "{i}(Just imagining it makes me hard.){/i}"
    scene 11_1624 with Dissolve(1)
    a "I can see you're thinking about it."
    mc "Well yeah..."
    mc "I'll get you or Erynn drunk one day and have you tell me the full story."
    er "Haha."
    scene 11_1625 with Dissolve(1)
    mc "Okay-okay. So you would kill Iris, fuck Erynn and marry me."
    a "Mm-hmm."
    mc "Erynn. Your turn."
    scene 11_1626 with Dissolve(1)
    er "Hmm... This is difficult."
    mc "Just kill me."
    er "No! I could never kill you!"
    scene 11_1627 with Dissolve(1)
    er "I'm so sorry, Iris! But I'll have to pick you."
    er "Lex is like a sister to me and..."
    ir "Haha, it's fine. I understand."
    mc "{i}(That must sting! You're breaking her heart, Erynn.){/i}"
    scene 11_1628 with Dissolve(1)
    er "And then..."
    er "I think I'll fuck Lex and marry [mc]."
    if Erynn_LikeMC == True:
        mc "{i}(Somehow I have a feeling she wanted to say it the other way around...){/i}"
    else:
        pass
    scene 11_1629 with Dissolve(1)
    er "This game is pretty stressful."
    a "Isn't it? Maybe we should've drunk some cocktails before playing."
    mc "Yeah. It would also be nice to know if any answers would change if you were drunk."
    scene black with Dissolve(1)
    pause 2
    scene 11_1630 with Dissolve(1)
    er "Mmm... I'm going in the water for a bit."
    a "I'll join you."
    ir "I'll stay here and tan a bit more."
    ir "I'm so pale compared to you guys. I need to catch up."
    scene 11_1631 with Dissolve(1)
    er "Are you coming?"
    mc "In a bit. I'll finish my coffee first."
    mc "Go on ahead."
    scene 11_1632 with Dissolve(1)
    mc "Heh..."
    mc "You run like a girl!"
    er "I am a girl!"
    scene 11_1633 with Dissolve(1)
    ir "*Sigh*"
    mc "..."
    mc "You okay?"
    ir "Yeah."
    scene 11_1634 with Dissolve(1)
    mc "We were together for like quite a while. I know when something's up."
    mc "You haven't been acting like yourself since we sat down."
    mc "Is it because of Erynn?"
    ir "No."
    scene 11_1635 with Dissolve(1)
    ir "I'm gonna be completely honest."
    ir "I thought I didn't mind seeing you with other girls."
    mc "..."
    ir "I know I have no right to be, but... I'm jealous."
    ir "Maybe this double date wasn't such a good idea after all."
    scene 11_1636 with Dissolve(1)
    mc "We don't have to do this. If it's too difficult for you, we can..."
    ir "No. It's... I'm just being selfish. Sorry."
    ir "I'll get over it. Alexis must feel even worse than me."
    mc "She said she's fine with it."
    scene 11_1637 with Dissolve(1)
    ir "Come on, [mc]."
    ir "You know better than that. She's not okay with it. She's just putting on a brave face for you."
    mc "{i}(So are you!){/i}"
    ir "No girl wants her boyfriend spending time with his ex."
    scene 11_1638 with Dissolve(1)
    a "What do you think they're talking about?"
    er "I don't know."
    er "They've known each other for a while, so it could be anything."
    scene 11_1639 with Dissolve(1)
    ir "You're basically cheating on me. You know that?"
    mc "On you? How am I cheating on you? We broke up months ago."
    ir "Did we?"
    scene 11_1640 with Dissolve(1)
    mc "What?"
    ir "Did we break up?"
    mc "Now you're confusing me."
    ir "It's fine. I'm just messing with you."
    mc "No... You're not messing with me. I know when you are. Tell me!"
    scene 11_1641 with Dissolve(1)
    ir "Last summer. When I told you I was moving away."
    ir "We talked about breaking up because of the whole long-distance thing and stuff."
    ir "But we never did. We never really said 'Hey, let's break up now' or officially ended it."
    ir "Summer went by, I moved away and that's about it."
    mc "Yeah. Now that I think about it, I guess we didn't."
    scene 11_1642 with Dissolve(1)
    mc "In that case. I hate to tell you, but I've cheated on you a lot! And not only with Alexis."
    ir "Haha. Really?"
    ir "I don't even know why I'm laughing."
    ir "I should be FURIOUS!"
    mc "Haha."
    scene 11_1643 with Dissolve(1)
    ir "How many?"
    mc "A few..."
    mc "And every girl from your school back in Alvarado."
    ir "Haha. Liar."
    ir "Actually. It could be true. There were lots of hoes in my class."
    mc "Haha."
    scene 11_1644 with Dissolve(1)
    ir "Remember Tiffany? I almost fought her because she couldn't keep her hands off you."
    ir "You didn't sleep with her, right?"
    mc "No."
    ir "Good! Because I wouldn't forgive you if you did."
    scene 11_1645 with Dissolve(1)
    ir "But really. How many?"
    mc "A few..."
    ir "[mc]... What's a few? Like five, ten?"
    mc "Yeah. Around that number."
    scene 11_1646 with Dissolve(1)
    ir "All in Alvarado?"
    mc "Some of 'em, yes."
    ir "Okay... Let me guess. Hmm..."
    scene 11_1647 with Dissolve(1)
    ir "Aaliyah?"
    mc "No."
    ir "Lakeyn?"
    if Lakeyn_FB_Sex == True:
        scene 11_1648 with Dissolve(1)
        mc "Yes!"
        ir "You had sex with Lakeyn? How did you manage that? Did she also do the tattoos on you?"
        mc "She did."
        ir "I always thought she was into girls. Hmm..."
        ir "Good on you. She's hot!"
    else:
        mc "Nope."
        ir "Did Nate? I remember he fancied her."
        mc "He didn't either."
        ir "I think she's into girls, anyway."
    scene 11_1649 with Dissolve(1)
    ir "Hmm..."
    ir "Mira?"
    mc "..."
    ir "I knew it! I so knew it!"
    ir "But I can't blame you there. She's a cutie. And she always had a thing for you!"
    scene 11_1650 with Dissolve(1)
    er "Hey! Come join us now!"
    mc "Yeah-yeah. We're coming."
    if Erynn_LikeMC == True:
        scene 11_1651 with Dissolve(1)
        mc "This girl..."
        ir "You like her, huh?"
        mc "Alexis? Well, yeah. Or else she wouldn't be my girlfriend."
        ir "I'm talking about Erynn."
        scene 11_1652 with Dissolve(1)
        mc "I like Erynn too."
        mc "I've known her for a long time, and..."
        ir "That's not what I mean."
        mc "What?"
        scene 11_1653 with Dissolve(1)
        ir "You know what I'm talking about. I see the way you talk and look at her. It's the same way you used to look at me!"
        mc "..."
        ir "She's the girl, right? The one that..."
        mc "*Nods*"
        ir "I guess we'll talk about that another time. Come, give me a hug!"
        scene 11_1654 with Dissolve(1)
        ir "I hate to admit it, but she likes you too."
        ir "But that doesn't matter, because she'll be mine soon."
        mc "You've gotta step up your flirting game, then. Your previous attempts were pretty pathetic."
        scene 11_1655 with Dissolve(1)
        mc "'Maybe I'll grow it out again.'"
        ir "Hey!"
        mc "Haha."
    else:
        pass
    scene 11_1656 with Dissolve(1)
    er "Aren't you coming, Iris?"
    ir "I'll stay here and guard our stuff."
    er "Oh... Okay. Thanks!"
    scene 11_1657 with Dissolve(1)
    mc "She actually can't swim and she's too embarrassed to say anything."
    er "I didn't know that."
    a "Don't listen to him! She can swim just fine. I've been to the beach with her before."
    scene 11_1658 with Dissolve(1)
    er "[mc]!"
    er "You always do that!"
    mc "Haha."
    if Iris_Points >= 1:
        scene 11_1659 with Dissolve(1)
        ir "*Sigh*"
        ir "{i}(Fuck...){/i}"
    else:
        pass
    scene 11_1660 with Dissolve(1)
    a "Hey."
    mc "Hey."
    a "What were you talking about with Iris?"
    mc "Uh... Old friends from Alvarado."
    scene 11_1661 with Dissolve(1)
    mc "So, what do you want to do now?"
    er "I don't know..."
    mc "You wanted to go in the water!"
    er "Just to cool off a bit."
    scene 11_1662 with Dissolve(1)
    mc "We should've brought a ball or something."
    er "We can play volleyball a little later."
    er "They have balls at the bar that you can rent."
    mc "Good idea. Let's do that. I've never seen you guys play."
    if Erynn_Week2_Tuesday_Fly == True:
        scene 11_1663 with Dissolve(1)
        mc "I have another idea for now, though."
        er "Yeah?"
        mc "You always wanted to do that Dirty Dancing flying scene, right?"
        er "Uh, yeah... How do you know that?"
        scene 11_1664 with Dissolve(1)
        mc "Melissa mentioned it before and showed me a picture where she picked you up."
        er "Oh..."
        mc "Up for it? The both of you?"
        er "I want to try."
        a "Sure."
        scene 11_1665 with Dissolve(1)
        a "I can't believe you've watched Dirty Dancing."
        mc "I haven't. I had to google it."
        a "Haha, okay."
        scene 11_1666 with Dissolve(1)
        mc "Where are you going?"
        er "I need some space to run towards you and..."
        mc "Because we've done this so many times already, right?"
        mc "Let's start here in the water first so I can figure out how to pick you up."
        if Erynn_Week5_Tuesday_Photoshoot_Join == True:
            scene 11_1667 with Dissolve(1)
            mc "{i}(This reminds me of the photo shoot again.){/i}"
            mc "{i}(She has such great boobs!){/i}"
        else:
            pass
        scene 11_1668 with Dissolve(1)
        er "How are we doing this?"
        mc "Hmm... I think I have to hold you on your hips so you can turn and balance once in the air."
        mc "Just jump and... We'll see, I guess."
        a "Looks like you guys are about to slow-dance."
        menu:
            "Touch her ass[KoGa3AutoWTChange1]{size=-4}(Alexis JealousyPoints+2, Alexis BeachPoints-2, {i}Erynn LikeMC: Erynn Points+2{/i}, {i}else: Erynn Points-4{/i}) {/size} {/color}":
                $ Alexis_JealousyPoints += 2
                # Alexis_Jealous (16)
                $ Alexis_BeachPoints -= 2
                if Erynn_LikeMC == True:
                    $ Erynn_Points += 2
                    # Erynn (60)
                else:
                    $ Erynn_Points -= 4
                scene 11_1669 with Dissolve(1)
                mc "If we were slow-dancing, I would hold her like this!"
                er "[mc]!"
                a "Hey! That wasn't an invitation to touch her butt!"
                scene 11_1670 with Dissolve(1)
                mc "I was just showing you how I would slow-dance."
                a "You can show me later when we go to the club!"
                mc "Oh? We're going to the club after?"
                a "Not if you keep touching Erynn's butt we aren't!"
            "Don't":
                mc "Heh. A little, yeah."
        scene 11_1671 with Dissolve(1)
        mc "Alright. Lexi, can you move back a little."
        mc "If I drop Erynn, I don't want her to fall on you."
        er "Then don't drop me!"
        mc "We're in the water. It's not gonna hurt."
        scene 11_1672 with Dissolve(1)
        mc "Ready?"
        er "Uh-huh."
        mc "Jump on three!"
        mc "One... two... three..."
        scene 11_1673 with Dissolve(1)
        mc "JUMP!"
        er "Aaah!"
        scene 11_1674 with Dissolve(1)
        mc "{i}(This is harder than I thought.){/i}"
        mc "{i}(She isn't nearly as high up as she needs to be.){/i}"
        mc "{i}(Shit!){/i}"
        scene 11_1675 with vpunch
        mc "..."
        scene 11_1676 with Dissolve(1)
        er "Aaah!"
        a "Be careful!"
        scene 11_1677 with Dissolve(1)
        a "Are you guys alright?"
        er "Haha, yeah."
        mc "Well, that was a fail."
        scene 11_1678 with Dissolve(1)
        er "Did I do something wrong, or...?"
        mc "I don't know. It's really difficult."
        mc "Maybe try to jump a little higher and I'll get a bit lower and push more with my legs."
        er "Or maybe you're not as strong as Patrick Swayze?"
        mc "..."
        scene 11_1679 with Dissolve(1)
        mc "The girl in the movie was tiny!"
        mc "You guys are much bigger."
        er "Much bigger..."
        mc "Bigger as in... I mean taller, okay? Dios mío..."
        mc "Let's just go again!"
        scene 11_1680 with Dissolve(1)
        er "..."
        a "..."
        scene 11_1681 with Dissolve(1)
        mc "And stop that talking without talking bullshit!"
        a "We were just looking at each other."
        mc "Yeah right!"
        er "Haha."
        scene 11_1682 with Dissolve(1)
        mc "Are you ready?"
        er "Uh-huh."
        mc "Jump as high as you can!"
        mc "In three... two... one..."
        scene 11_1683 with Dissolve(1)
        er "Aah..."
        a "Yes! That's it!"
        mc "Is it?"
        scene 11_1684 with Dissolve(1)
        a "Try to straighten your legs, Erynn."
        mc "Give me a second. I need to balance her first."
        if Erynn_LikeMC == True:
            scene 11_1685 with Dissolve(1)
            mc "{i}(What a sight!){/i}"
        else:
            pass
        scene 11_1686 with Dissolve(1)
        er "Oh no..."
        mc "Don't lean so far forward!"
        a "Be careful!"
        scene 11_1687 with Dissolve(1)
        er "[mc]!"
        mc "Shit!"
        scene 11_1688 with Dissolve(1)
        da "What the fuck are they doing?"
        tj "No idea. Looks fun though."
        da "Fun?"
        tj "Our girls are just lying here, doing nothing. They seem to be having fun, at least."
        if Valeria_LikeMC == True:
            scene 11_1689 with Dissolve(1)
            va "..."
        else:
            pass
        scene 11_1690 with Dissolve(1)
        da "Mm-mm-mm..."
        scene 11_1691 with Dissolve(1)
        va "Darryl!"
        da "Come on, babygirl. Get up!"
        va "Get off me!"
        to "Leave her alone, Darryl!"
        da "Are you jealous I'm not on top of you?"
        scene 11_1692 with Dissolve(1)
        da "*Whispers* You're so fucking sexy! I want you!"
        va "Seriously, Darryl! Get off!"
        da "Then let's do something other than just lying here."
        va "Fine..."
        scene 11_1693 with Dissolve(1)
        a "Are you guys okay?"
        er "Haha, yeah."
        a "It looked good for a moment."
        mc "Not bad for a second try, right? Take that Swayze!"
        scene 11_1694 with Dissolve(1)
        a "..."
        mc "Why are you looking like that?"
        scene 11_1695 with Dissolve(1)
        a "I like having a strong boyfriend! That was kinda sexy!"
        mc "Yeah?"
        a "Mm-hmm."
        a "*Whispers* Turned me on a little..."
        scene 11_1696 with Dissolve(1)
        a "Aaah!"
        mc "Your turn!"
        a "No. I'm good, I'm good."
        er "You should try it. It's fun."
        a "No, no. I'm good."
        scene 11_1697 with Dissolve(1)
        ""
        scene 11_1698 with vpunch
        a "Aaah... [mc]!"
        mc "Shall we head back?"
        a "Maybe Erynn wants another go."
        er "It's fine. We can try again another time."
        er "Iris has been alone for a while now."
    else:
        scene 11_1698 with vpunch
        a "Aaah... [mc]!"
        mc "Shall we head back then?"
        er "Yeah. I don't like that Iris is alone."
    scene 11_1699 with vpunch
    mc "Let's go then!"
    er "Aaah!"
    a "Haha."
    scene 11_1700 with Dissolve(1)
    mc "What are you guys giggling about back there?"
    mc "Are you making out?"
    a "Who knows?"
    mc "At least let me look!"
    er "Haha."
    scene 11_1701 with Dissolve(1)
    mc "..."
    scene 11_1702 with Dissolve(1)
    da "Yeah, exactly like that."
    da "Now throw it!"
    scene 11_1703 with Dissolve(1)
    da "Not bad, babygirl."
    da "You'd better catch that, TJ!"
    scene 11_1704 with Dissolve(1)
    va "Aaah!"
    da "Haha. Nice try shawty!"
    va "..."
    scene 11_1705 with Dissolve(1)
    mc "Look, Iris. I found two bongos in the ocean!"
    a "Bongos?"
    ir "Oh, I always wanted to try those."
    scene 11_1706 with Dissolve(1)
    er "Hey!"
    ir "They don't make much sound though."
    mc "Hit them harder!"
    er "No!"
    mc "Haha."
    scene black with Dissolve(1)
    pause 2
    scene 11_1707 with Dissolve(1)
    ir "Let me do your back for you, Erynn."
    er "Thank you."
    scene 11_1708 with Dissolve(1)
    mc "Want me to do yours too?"
    a "Sure. Thanks."
    scene 11_1709 with Dissolve(1)
    ir "Here. You'll need this."
    mc "Thanks."
    mc "{i}(I know that look. She's planning something.){/i}"
    scene 11_1710 with Dissolve(1)
    er "..."
    a "..."
    scene 11_1711 with Dissolve(1)
    ir "Erynn. Can I loosen your top?"
    er "I'll take it off for a moment."
    ir "That works too."
    mc "Lexi?"
    a "Sure..."
    scene 11_1712 with Dissolve(1)
    ir "Is this alright?"
    er "Mm-hmm. Feels nice."
    scene 11_1713 with Dissolve(1)
    mc "*Whispers* I see what you're doing."
    ir "*Whispers* I'm not doing anything!"
    ir "You have very soft skin, Erynn."
    er "Thanks."
    mc "Lexi. You have the softest skin!"
    scene 11_1714 with Dissolve(1)
    a "Okay... What are you doing back there?"
    a "Are you having a competition or something?"
    er "Haha."
    mc "No... Just complimenting you! Lie down and enjoy."
    scene 11_1715 with Dissolve(1)
    mc "{i}(What the fuck is she doing now?){/i}"
    mc "{i}(Is she pretending to take Erynn doggy?){/i}"
    mc "{i}(This girl...){/i}"
    mc "{i}(Why is this turning me on too?){/i}"
    scene 11_1716 with Dissolve(1)
    mc "{i}(Haha.){/i}"
    mc "{i}(That face...){/i}"
    mc "{i}(Iris...){/i}"
    scene 11_1717 with Dissolve(1)
    ir "*Whispers* Oh no..."
    ir "*Whispers* I just drooled on her."
    mc "Haha. I saw that. So disgusting."
    scene 11_1718 with Dissolve(1)
    a "Okay. What's so funny back there?"
    ir "Oh... Lexi's bitties."
    scene 11_1719 with Dissolve(1)
    mc "..."
    er "Uh, Lex..."
    scene 11_1720 with Dissolve(1)
    a "What are you..."
    mc "Your..."
    a "Ah..."
    scene 11_1721 with Dissolve(1)
    a "I can't believe that just happened!"
    a "Now the whole beach saw me."
    mc "Haha. I don't think anyone saw it. I covered them up real quick!"
    a "Thanks for that."
    scene 11_1722 with Dissolve(1)
    a "You go lie down."
    a "I'll do your back instead."
    mc "Sure. Thanks."
    scene 11_1723 with Dissolve(1)
    mc "Oh, you're here too?"
    mc "Come here often?"
    er "Heh. Not as much as I'd like."
    mc "How's the service?"
    er "Excellent!"
    scene 11_1724 with Dissolve(1)
    mc "..."
    mc "{i}(Doesn't she realise I can see her boobs, too?){/i}"
    scene 11_1725 with Dissolve(1)
    da "Go long, Val!"
    va "What? Long?"
    va "I don't know what that means..."
    scene 11_1726 with Dissolve(1)
    va "..."
    scene 11_1727 with vpunch
    a "Ahhh!"
    scene 11_1728 with Dissolve(1)
    mc "Did something happen?"
    a "Just got a ball to my face."
    mc "What? Are you okay?"
    va "I'm so sorry, Alexis!"
    scene 11_1729 with Dissolve(1)
    va "We didn't mean to... I'm sorry."
    va "Are you okay?"
    a "Don't worry. I'll be fine."
    va "Can I get you an icepack or something?"
    a "No, it's okay. Thanks."
    scene 11_1730 with Dissolve(1)
    mc "Why did you even throw it here?"
    a "[mc]. It's fine."
    va "No, I..."
    mc "Of course. I know it was Darryl. I can see his smug face from here."
    scene 11_1731 with Dissolve(1)
    mc "What the fuck, Darryl!"
    da "Chill dude. It was an accident!"
    va "It was my fault. I couldn't catch it."
    menu:
        "Give Valeria the ball":
            scene 11_1732 with Dissolve(1)
            mc "Nah. Darryl is just a shitty thrower!"
            va "Heh."
            mc "Here."
            va "Thanks."
        "Throw the ball":
            scene 11_1734 with Dissolve(1)
            mc "Nah. Darryl is just a shitty thrower!"
            va "Uh..."
    scene 11_1733 with Dissolve(1)
    va "Sorry again, Alexis."
    a "It's okay."
    va "Bye."
    scene 11_1735 with Dissolve(1)
    mc "Let me have a look."
    mc "It's getting red already. You're probably gonna end up with a bruise tomorrow."
    mc "You sure you don't want an icepack?"
    a "Yeah, it's fine."
    menu:
        "Kiss Alexis[KoGa3AutoWTChange1]{size=-4}(Alexis BeachPoints+4, {i}Valeria LikeMC: Valeria Points-4{/i}) {/size} {/color}":
            $ Alexis_BeachPoints += 4
            # Alexis_Beach (10)
            scene 11_1736 with Dissolve(1)
            ""
            if Valeria_LikeMC == True:
                $ Valeria_Points -= 4
                scene 11_1737 with Dissolve(1)
                va "..."
            else:
                pass
        "Don't[KoGa3AutoWTChange1]{size=-4}(Alexis BeachPoints-2) {/size} {/color}":
            $ Alexis_BeachPoints -= 2
    scene 11_1738 with Dissolve(1)
    a "It's not the first time I've had a ball in my face."
    mc "..."
    ir "Good for you, [mc]!"
    a "What?"
    scene 11_1739 with Dissolve(1)
    a "No... NO! That's not what I meant."
    mc "Haha. I don't want to say it, but..."
    a "Yeah. Just say it! I deserve it."
    scene 11_1740 with Dissolve(1)
    mc "Phrasing!"
    a "*Shakes head*"
    mc "Now you're getting red for a whole nother reason."
    a "I know..."
    mc "Haha."
    scene 11_1741 with Dissolve(1)
    mc "Speaking of balls... Wanna go play volleyball now?"
    er "Yeah, we can do that."
    jump Week5_Wednesday_Beach_Volleyball

label Week5_Wednesday_Beach_Volleyball:
    scene black with Dissolve(1)
    pause 2
    scene 11_1742 with Dissolve(1)
    mc "So... How are we gonna do this?"
    er "Why don't we make this a little more interesting?"
    mc "What do you have in mind?"
    er "A bet or something?"
    mc "Sure. Sounds fun."
    scene 11_1743 with Dissolve(1)
    mc "Any idea what we're betting on?"
    er "Hmm..."
    a "How about the losing team has to do whatever the winning team says for a whole day?"
    ir "Anything? I'm in."
    mc "Let's do that."
    er "Okay. Teams then."
    scene 11_1744 with Dissolve(1)
    ir "I'll go with [mc]!"
    er "Alright. Lex and I versus you two."
    mc "What? No!"
    scene 11_1745 with Dissolve(1)
    ir "Why? Don't you want to play with me?"
    mc "It's not that. We're gonna get rekt!"
    mc "You know those two play volleyball, right?"
    ir "Oh..."
    mc "Yes... Oh!"
    scene 11_1746 with Dissolve(1)
    a "Too bad. No switching teams."
    mc "Look at you. You really want to win, huh?"
    a "Of course. A whole day of me telling you what to do."
    mc "That's no different than usual."
    a "Haha. This is gonna be so much fun!"
    scene 11_1747 with Dissolve(1)
    er "I'm gonna get us a ball."
    mc "Okay. Listen up."
    a "..."
    scene 11_1748 with Dissolve(1)
    mc "What are you doing? Eavesdropping?"
    a "Why would I do that?"
    mc "Because we're talking strategy here."
    a "Strategy?"
    mc "Yes! Go stand on your side."
    a "Haha. Okay, okay."
    scene 11_1749 with Dissolve(1)
    mc "If we want to win, we can't play fair."
    ir "So, we need to cheat?"
    mc "Uh-huh. Are you okay with that?"
    scene 11_1750 with Dissolve(1)
    ir "Yeah! I want to win! A whole day of Erynn doing what I want."
    ir "I'm starting to drool again."
    mc "Haha."
    scene 11_1751 with Dissolve(1)
    ir "What do you have in mind?"
    mc "I don't know yet. Since it's a non-contact sport, it makes it more difficult."
    mc "I think a distraction of some sort is our best bet."
    ir "Distraction? Leave that to me!"
    scene 11_1752 with Dissolve(1)
    er "What are they doing?"
    a "Talking strategy..."
    er "Heh, okay. Should we take it easy on them?"
    a "Yeah. I don't think Iris has played much volleyball before."
    scene 11_1753 with Dissolve(1)
    er "Here! You guys can start."
    er "Let's do beach volleyball rules. First to twenty-one wins."
    mc "Sure."
    scene 11_1754 with Dissolve(1)
    ir "Let me go first."
    mc "You know how to serve?"
    ir "Yes!"
    scene 11_1755 with Dissolve(1)
    mc "..."
    scene 11_1756 with Dissolve(1)
    ir "Ahh..."
    er "Are you okay, Iris?"
    ir "Yeah. I just hit the ball incorrectly. That one doesn't count! Let me go again."
    er "Sure. Go ahead."
    mc "Do the underhand serve and make a fist. That's easier."
    scene 11_1757 with Dissolve(1)
    mc "Yeah, like that."
    scene 11_1758 with Dissolve(1)
    mc "{i}(Oh boy...){/i}"
    mc "By the way. Those were just warm-up serves!"
    mc "We're starting now."
    a "Haha."
    scene 11_1759 with Dissolve(1)
    mc "That wasn't so bad. Just unlucky."
    mc "Want to try again?"
    ir "No. You go first, or else we'll never score a point."
    mc "Alright."
    scene 11_1760 with Dissolve(1)
    mc "{i}(I don't know who the better player is of the two.){/i}"
    mc "{i}(Let's serve it to Alexis first and see how she handles it.){/i}"
    scene 11_1761 with Dissolve(1)
    mc "{i}(FUCK!!!){/i}"
    a "..."
    scene 11_1762 with Dissolve(1)
    a "Is this still the warm-up, or...?"
    mc "Shut up and go serve."
    a "Haha. Someone's getting annoyed already."
    scene 11_1763 with Dissolve(1)
    a "Ready?"
    mc "Yes..."
    scene 11_1764 with Dissolve(1)
    mc "{i}(What the fuck...?){/i}"
    scene 11_1765 with vpunch
    ir "Aaah..."
    mc "{i}(Seriously?){/i}"
    scene 11_1766 with Dissolve(1)
    mc "What the hell was that, Alexis?"
    a "Alexis..."
    ir "That was so scary!"
    mc "Can you chill a little? Give us at least a chance."
    scene 11_1767 with Dissolve(1)
    a "What? I did. That was like an average serve."
    mc "Average? Are you kidding me? No more jump serves! They're banned!"
    a "Fine. I'll do only underhand serves from now on. Okay?"
    scene black with Dissolve(1)
    pause 2
    scene 11_1768 with Dissolve(1)
    mc "Be ready Iris."
    mc "Try to play it back to me."
    ir "Uhm... Okay?"
    scene 11_1769 with Dissolve(1)
    ir "Aaah..."
    ir "Sorry."
    mc "It's fine. It's over the net."
    scene 11_1770 with Dissolve(1)
    er "Lex!"
    a "I'm ready."
    scene 11_1771 with Dissolve(1)
    mc "{i}(Just fucking look at that.){/i}"
    mc "{i}(How is this even remotely fair?){/i}"
    scene 11_1772 with vpunch
    mc "..."
    scene 11_1773 with Dissolve(1)
    a "Nice. Good job, Erynn!"
    a "You've still got it!"
    er "Thank you!"
    scene 11_1774 with Dissolve(1)
    mc "Holy shit."
    ir "You okay?"
    mc "Yeah. That ball came so much quicker than I thought."
    mc "Where does she get that power from?"
    mc "We're in big trouble."
    scene 11_1775 with Dissolve(1)
    a "Two-nil!"
    mc "I know."
    a "We can stop this whenever you want, babe."
    mc "Just go serve! Babe..."
    a "Haha."
    scene black with Dissolve(1)
    pause 2
    scene 11_1776 with Dissolve(1)
    ""
    scene 11_1777 with Dissolve(1)
    ""
    scene 11_1778 with vpunch
    ""
    scene 11_1779 with vpunch
    ""
    scene 11_1780 with vpunch
    mc "..."
    a "Sorry!"
    scene 11_1781 with Dissolve(1)
    mc "Why are you only smashing towards me? There's someone else on my team..."
    a "Don't be so mad."
    mc "Someone wants to win so badly."
    mc "Volleyball is such a stupid sport!"
    a "Haha."
    scene 11_1782 with Dissolve(1)
    a "He's getting pretty annoyed."
    er "That's one of the things that hasn't changed. He hates losing."
    a "Shall we dial it back a little more?"
    er "Let's give them a chance to play the ball back at least."
    a "Okay. And what are they doing now? Talking strategy again?"
    scene 11_1783 with Dissolve(1)
    mc "The plan is starting to take effect."
    mc "I knew if you acted scared, they'll only smash the ball towards me."
    mc "They must be thinking I'm so angry."
    ir "You did well. For a moment you convinced me, too."
    mc "{i}(Because I kinda am!){/i}"
    scene 11_1784 with Dissolve(1)
    ir "What's next?"
    mc "I think they might take it easier on us now and let their guard down a bit."
    mc "Time for phase two. Distraction!"
    scene black with Dissolve(1)
    pause 2
    scene 11_1785 with Dissolve(1)
    a "I've got it."
    mc "Now, Iris!"
    scene 11_1786 with Dissolve(1)
    ir "Hey, Erynn!"
    er "..."
    er "Wha... Iris!"
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 11_1787 at moveup
    pause 3
    mc "{i}(Haha. Typical Iris.){/i}"
    mc "{i}(I think I'm more distracted than those two.){/i}"
    a "Erynn! The ball!"
    scene 11_1788 with Dissolve(1)
    er "Shit!"
    scene 11_1789 with vpunch
    ir "I did it! We got a point!"
    mc "Haha. Good job!"
    scene 11_1790 with Dissolve(1)
    mc "Uh..."
    scene 11_1791 with Dissolve(1)
    a "IRIS! GET OFF HIM!"
    ir "Can't we hug?"
    a "That's not the issue!"
    scene 11_1792 with Dissolve(1)
    ir "Oh this?"
    ir "Don't worry. He's seen them before."
    a "Iris!"
    scene 11_1793 with Dissolve(1)
    mc "Alright! Comeback, baby! Let's fucking go!"
    a "..."
    scene 11_1794 with Dissolve(1)
    a "So, this is how we're gonna play, huh?"
    a "We took it easy on you guys. But it's on, now!"
    mc "That was you taking it easy?"
    er "Haha."
    scene black with Dissolve(1)
    pause 2
    scene 11_1795 with Dissolve(1)
    er "I've got it!"
    show 11_1796
    mc "{i}(What is she...?){/i}"
    scene 11_1797 with Dissolve(1)
    mc "..."
    ir "..."
    scene 11_1798 with Dissolve(1)
    mc "What just happened?"
    ir "I don't know but I liked it... A lot!"
    if Erynn_LikeMC == True:
        mc "{i}(Damn, that was fucking hot!){/i}"
    else:
        pass
    scene 11_1799 with Dissolve(1)
    a "Erynn! I can't believe you scored like that."
    er "Haha. We can play their game too!"
    scene 11_1800 with Dissolve(1)
    mc "Is that even allowed?"
    er "Yeah, you can use any body part basically."
    mc "Really..."
    er "Uh-huh."
    scene 11_1801 with Dissolve(1)
    mc "I think I'm gonna watch female volleyball from now on."
    a "Didn't you say volleyball is a stupid sport, before?"
    mc "What? No! I never said that!"
    a "Haha. Let's continue."
    scene black with Dissolve(1)
    pause 2
    scene 11_1802 with Dissolve(1)
    ""
    scene 11_1803 with Dissolve(1)
    mc "{i}(Fuck...){/i}"
    scene 11_1804 with Dissolve(1)
    er "That's game!"
    er "Twenty-one to one!"
    mc "Yeah-yeah. Congrats!"
    mc "{i}(We scored one measly point... ONE!){/i}"
    mc "{i}(And we even had to cheat to get that one.){/i}"
    scene 11_1805 with Dissolve(1)
    mc "Damn, I've never been this humiliated before..."
    a "You did great though, babe."
    mc "Oh, shut up! This was a massacre."
    a "I still think you did great!"
    scene 11_1806 with Dissolve(1)
    a "Reward for second place."
    mc "{i}(Second place...){/i}"
    scene 11_1807 with Dissolve(1)
    mc "*Sigh* I thought I was better at volleyball."
    a "You're good at the things you need to be good at!"
    mc "Heh..."
    scene 11_1808 with Dissolve(1)
    ir "You have to thank me for that!"
    a "..."
    scene 11_1809 with Dissolve(1)
    mc "No, but seriously. You guys were amazing!"
    er "Thanks!"
    mc "It was very nice to look at how you play. For obvious reasons."
    ir "I second that."
    er "Haha. Thanks."
    scene 11_1810 with Dissolve(1)
    mc "I didn't know you were that good."
    mc "Now I wish I could've seen you play a game in high school."
    er "Lexi might have some videos."
    a "Yeah. We have a few at home."
    mc "Show them to me next time."
    scene 11_1811 with Dissolve(1)
    mc "You should sign up for those beach volleyball tournaments in the summer."
    mc "Do they still do those?"
    er "They do. Every weekend in August."
    mc "Go sign up, then. You might actually have a chance."
    mc "You guys haven't played in years and still had this kind of performance."
    scene 11_1812 with Dissolve(1)
    a "Yeah. Maybe."
    er "We'll think about it."
    mc "You'll have at least two supporters here already."
    scene 11_1813 with Dissolve(1)
    mc "How did you actually become friends?"
    a "Who? Iris and I?"
    mc "No, that I know. Probably because you're sharing a dorm."
    mc "You and Erynn."
    scene 11_1814 with Dissolve(1)
    er "It was the first day at elementary school."
    mc "First day? So, you saw each other and thought, hey, you're pretty, I'm pretty, let's be friends?"
    a "Haha."
    er "Haha, no."
    scene 11_1815 with Dissolve(1)
    er "The desks were arranged by name."
    er "And because of our names, Monroe and Orlandi, we were sat next to each other."
    mc "And then you said, you're pretty, I'm pretty, let's..."
    er "Haha. No... We just started talking and yeah, became friends, I guess."
    scene 11_1816 with Dissolve(1)
    mc "If I had been in your class, I would've been sitting between you two."
    er "You're right. Moreno... We'd be neighbours either way."
    mc "Heh, yeah."
    scene 11_1817 with Dissolve(1)
    er "I have a question. Maybe it's not the right time to ask you this, but..."
    mc "No. Go ahead."
    er "Okay, uhm... Do you still go by Moreno? Because of Andres... You know..."
    scene 11_1818 with Dissolve(1)
    mc "Hmm... I haven't thought about that yet. I should change it though."
    er "What does it say on your ID?"
    mc "I have both on my ID. Vicari-Moreno."
    mc "But I always went with Moreno since everyone I knew used their dad's last name."
    er "Except for me."
    mc "Haha. You're right. Except for you."
    scene 11_1819 with Dissolve(1)
    ir "So, your actual name is Vicari?"
    mc "It is."
    ir "After all this time, I still learn new things about you."
    scene 11_1820 with Dissolve(1)
    ir "What's your bio-dad's last name?"
    mc "I don't know. I never asked Mom about that."
    mc "Maybe I should change my name to his name. But only if it's something cool like Valentine... Or Montana."
    mc "Or an animal name like Fox, Raven or Wolf. I don't know."
    scene 11_1821 with Dissolve(1)
    er "Or just wait to change it until you're married and then take the name of your future wife."
    mc "That's also an option."
    mc "But she needs to have a cool name too."
    a "..."
    scene 11_1822 with Dissolve(1)
    mc "Why are you looking like that?"
    a "Like what? I'm just looking."
    mc "We're not gonna get married any time soon."
    a "Haha. I didn't say anything."
    scene 11_1823 with Dissolve(1)
    ir "Who did you pick again to marry when we played Kill-Fuck-Marry?"
    if KFM_Marry_Alexis == True:
        mc "Lexi."
        mc "So, I would be [mc] Monroe."
    else:
        if KFM_Marry_Erynn == True:
            mc "Erynn."
            mc "So, I would be [mc] Orlandi."
        else:
            mc "You!"
            mc "So, I would be [mc] Vančura."
    mc "Yeah... I can live with that."
    a "..."
    scene black with Dissolve(1)
    pause 2
    scene 11_1824 with Dissolve(1)
    mc "Nggh... I'm getting a little hungry."
    a "Shall we head home, then? We've been here for quite a few hours now."
    a "We need to get ready for the club, anyway."
    mc "Sounds good."
    scene 11_1825 with Dissolve(1)
    er "I won't be joining you guys though."
    ir "What? Erynn... No! You're not going to the club?"
    er "I have to work in the morning and need to wake up early."
    mc "{i}(Does she have another shoot or something?){/i}"
    ir "Not just for a little? Like an hour or two?"
    er "Next time. I promise."
    scene 11_1826 with Dissolve(1)
    a "We'll be right back."
    mc "Take your time. I'll wait here."
    if Erynn_LikeMC == True:
        scene 11_1827 with Dissolve(1)
        mc "{i}(This day went better than expected.){/i}"
        mc "{i}(But now I'm even more confused.){/i}"
        mc "*Sigh*"
        scene 11_1828 with Dissolve(1)
        mc "{i}(I love Lexi, but I still can't get Erynn out of my head.){/i}"
        if Iris_Points >= 1:
            mc "{i}(And now spending some time with Iris again, there's still so much there.){/i}"
            mc "{i}(It's just easy and so much fun. Or is this just familiarity?){/i}"
            if Valeria_LikeMC == True:
                mc "{i}(And then there's the biggest confusion.){/i}"
                scene 11_1829 with Dissolve(1)
                mc "{i}(Her...){/i}"
                scene 11_1830 with Dissolve(1)
                mc "{i}(Okay... This is weird.){/i}"
                mc "{i}(Why is she looking over here? It's as if she knows I'm thinking about her.){/i}"
                mc "..."
                mc "{i}(She's probably just looking in this direction and doesn't even know I'm standing here.){/i}"
            else:
                pass
            scene 11_1831 with Dissolve(1)
            mc "{i}(Waiting here and thinking about all this makes it worse...){/i}"
            mc "{i}(I should just...){/i}"
        else:
            if Valeria_LikeMC == True:
                mc "{i}(And then there's the biggest confusion.){/i}"
                scene 11_1829 with Dissolve(1)
                mc "{i}(Her...){/i}"
                scene 11_1830 with Dissolve(1)
                mc "{i}(Okay... This is weird.){/i}"
                mc "{i}(Why is she looking over here? It's as if she knows I'm thinking about her.){/i}"
                mc "..."
                mc "{i}(She's probably just looking in this direction and doesn't even know I'm standing here.){/i}"
            else:
                pass
            scene 11_1831 with Dissolve(1)
            mc "{i}(Waiting here and thinking about all this makes it worse...){/i}"
            mc "{i}(I should just...){/i}"
    else:
        if Iris_Points >= 1:
            mc "{i}(And now spending some time with Iris again, there's still so much there.){/i}"
            mc "{i}(It's just easy and so much fun. Or is this just familiarity?){/i}"
            if Valeria_LikeMC == True:
                mc "{i}(And then there's the biggest confusion.){/i}"
                scene 11_1829 with Dissolve(1)
                mc "{i}(Her...){/i}"
                scene 11_1830 with Dissolve(1)
                mc "{i}(Okay... This is weird.){/i}"
                mc "{i}(Why is she looking over here? It's as if she knows I'm thinking about her.){/i}"
                mc "..."
                mc "{i}(She's probably just looking in this direction and doesn't even know I'm standing here.){/i}"
            else:
                pass
            scene 11_1831 with Dissolve(1)
            mc "{i}(Waiting here and thinking about all this makes it worse...){/i}"
            mc "{i}(I should just...){/i}"
        else:
            if Valeria_LikeMC == True:
                mc "{i}(And then there's the biggest confusion.){/i}"
                scene 11_1829 with Dissolve(1)
                mc "{i}(Her...){/i}"
                scene 11_1830 with Dissolve(1)
                mc "{i}(Okay... This is weird.){/i}"
                mc "{i}(Why is she looking over here? It's as if she knows I'm thinking about her.){/i}"
                mc "..."
                mc "{i}(She's probably just looking in this direction and doesn't even know I'm standing here.){/i}"
            else:
                scene 11_1831 with Dissolve(1)
                mc "{i}(I hate waiting here on my own...){/i}"
                mc "{i}(I should just...){/i}"
    if Erynn_LikeMC == True:
        if Iris_Points >= 1:
            menu:
                "Join Alexis[KoGa3AutoWTChange1]{size=-4}(Alexis BeachPoints+2, Alexis Week5 Wednesday Beach Join) {/size} {/color}":
                    $ Alexis_BeachPoints += 2
                    # Alexis_Beach (12)
                    $ Alexis_Week5_Wednesday_Beach_Join = True
                    jump Week5_Wednesday_Beach_Join_Alexis
                "Join Erynn[KoGa3AutoWTChange1]{size=-4}(Erynn Week5 Wednesday Beach Join) {/size} {/color}":
                    $ Erynn_Week5_Wednesday_Beach_Join = True
                    jump Week5_Wednesday_Beach_Join_Erynn
                "Join Iris[KoGa3AutoWTChange1]{size=-4}(Iris Week5 Wednesday Beach Join) {/size} {/color}":
                    $ Iris_Week5_Wednesday_Beach_Join = True
                    jump Week5_Wednesday_Beach_Join_Iris
                "Wait here":
                    mc "{i}(Nah. It won't be too long. Right?){/i}"
                    jump Week5_Wednesday_Beach_End
        else:
            menu:
                "Join Alexis[KoGa3AutoWTChange1]{size=-4}(Alexis BeachPoints+2, Alexis Week5 Wednesday Beach Join) {/size} {/color}":
                    $ Alexis_BeachPoints += 2
                    # Alexis_Beach (12)
                    $ Alexis_Week5_Wednesday_Beach_Join = True
                    jump Week5_Wednesday_Beach_Join_Alexis
                "Join Erynn[KoGa3AutoWTChange1]{size=-4}(Erynn Week5 Wednesday Beach Join) {/size} {/color}":
                    $ Erynn_Week5_Wednesday_Beach_Join = True
                    jump Week5_Wednesday_Beach_Join_Erynn
                "Wait here":
                    mc "{i}(Nah. It won't be too long. Right?){/i}"
                    jump Week5_Wednesday_Beach_End
    else:
        if Iris_Points >= 1:
            menu:
                "Join Alexis[KoGa3AutoWTChange1]{size=-4}(Alexis BeachPoints+2, Alexis Week5 Wednesday Beach Join) {/size} {/color}":
                    $ Alexis_BeachPoints += 2
                    # Alexis_Beach (12)
                    $ Alexis_Week5_Wednesday_Beach_Join = True
                    jump Week5_Wednesday_Beach_Join_Alexis
                "Join Iris[KoGa3AutoWTChange1]{size=-4}(Iris Week5 Wednesday Beach Join) {/size} {/color}":
                    $ Iris_Week5_Wednesday_Beach_Join = True
                    jump Week5_Wednesday_Beach_Join_Iris
                "Wait here":
                    mc "{i}(Nah. It won't be too long. Right?){/i}"
                    jump Week5_Wednesday_Beach_End
        else:
            menu:
                "Join Alexis[KoGa3AutoWTChange1]{size=-4}(Alexis BeachPoints+2, Alexis Week5 Wednesday Beach Join) {/size} {/color}":
                    $ Alexis_BeachPoints += 2
                    # Alexis_Beach (12)
                    $ Alexis_Week5_Wednesday_Beach_Join = True
                    jump Week5_Wednesday_Beach_Join_Alexis
                "Wait here":
                    mc "{i}(Nah. It won't be too long. Right?){/i}"
                    jump Week5_Wednesday_Beach_End

label Week5_Wednesday_Beach_Join_Alexis:
    if _in_replay:
        $ Alexis_Intro_Join = True
        $ Alexis_Points = 40
        $ Alexis_BeachPoints = 12
    scene 11_1832 with Dissolve(1)
    n "*Knock-knock*"
    scene 11_1833 with Dissolve(1)
    a "Hey. What are you doing here? Need something?"
    mc "I was just lonely waiting here by myself."
    a "Heh..."
    a "Want to come inside?"
    mc "Uh-huh. Can I?"
    scene 11_1834 with Dissolve(1)
    mc "Hi..."
    a "Hey."
    if Alexis_Intro_Join == True:
        a "Do you know what this reminds me of?"
        mc "The aeroplane?"
        a "Haha, yes. This is a little more spacious, though."
    else:
        pass
    scene 11_1835 with Dissolve(1)
    ""
    scene 11_1836 with vpunch
    a "Aah-haha..."
    scene 11_1837 with Dissolve(1)
    er "Lex? Are you okay?"
    a "Uh..."
    a "Yeah... I just stumbled over my bag."
    er "Be careful!"
    scene 11_1838 with Dissolve(1)
    a "Let's leave this for later tonight."
    mc "*Sigh* I guess..."
    a "I'll change real quick."
    scene 11_1839 with Dissolve(1)
    mc "..."
    mc "{i}(I love watching girls undress.){/i}"
    scene 11_1840 with Dissolve(1)
    a "..."
    scene 11_1841 with Dissolve(1)
    mc "{i}(Okay... Enough is enough.){/i}"
    scene 11_1842 with Dissolve(1)
    a "Ahh..."
    mc "Now you're just doing this on purpose!"
    a "Haha. What? I'm just undressing."
    mc "Yeah fucking right!"
    scene 11_1843 with Dissolve(1)
    mc "I've had to watch you in a bikini the whole day."
    mc "Now I have to see this."
    mc "Later, you'll probably be dressed in some sexy clothes when we go to the club."
    mc "This is too much! I can't wait until later tonight!"
    scene 11_1844 with Dissolve(1)
    mc "When was the last time we had sex?"
    a "Hmm..."
    mc "See! Exactly! You even have to think about it. That means it's way too long ago!"
    a "Was it two days?"
    scene 11_1845 with Dissolve(1)
    mc "We should have sex at least four times a day!"
    a "Four times? Can you even go that often?"
    mc "Easy! I can go the whole day!"
    a "Haha. Okay. Let's test that theory next time, Mr All Day..."
    mc "Next time? We can start right now!"
    scene 11_1846 with Dissolve(1)
    a "Ah..."
    a "Hey!"
    scene 11_1847 with Dissolve(1)
    a "*Sigh* Fine..."
    mc "Quickie?"
    a "No."
    scene 11_1848 with Dissolve(1)
    a "Something else!"
    mc "Something else, huh?"
    scene 11_1849 with Dissolve(1)
    ""
    scene 11_1850 with Dissolve(1)
    ""
    scene 11_1851 with Dissolve(1)
    mc "{i}(Yes...){/i}"
    show 11_1852
    ""
    scene 11_1853 with Dissolve(1)
    mc "Fuck... Lexi..."
    scene 11_1854 with Dissolve(1)
    mc "You have no idea how much I needed this!"
    scene 11_1855 with Dissolve(1)
    mc "This feels so good!"
    show 11_1856
    ""
    scene 11_1857 with Dissolve(1)
    a "..."
    scene 11_1858 with Dissolve(1)
    a "Mmhh..."
    scene 11_1859 with Dissolve(1)
    mc "Just a little more!"
    scene 11_1860 with Dissolve(1)
    mc "{i}(Almost.){/i}"
    menu:
        "Cum in her mouth[KoGa3AutoWTChange1]{size=-4}(Alexis Week5 Wednesday Beach CumMouth) {/size} {/color}":
            $ Alexis_Week5_Wednesday_Beach_CumMouth = True
            scene 11_1861 with vpunch
            ""
            scene 11_1861 with vpunch
            mc "Fuck..."
            a "..."
            scene 11_1862 with Dissolve(1)
            mc "{i}(I don't know if she's mad or...){/i}"
            scene 11_1863 with Dissolve(1)
            mc "Did you just swallow it?"
            a "Yes... Did you want me to spit it in your mouth or something?"
            mc "Haha. No, thanks."
            scene 11_1864 with Dissolve(1)
            mc "For a second I thought you were angry. I didn't know if I could..."
            a "Anywhere is fine as long as it's not on my face."
            mc "Heh, okay."
            scene 11_1865 with Dissolve(1)
            mc "That was an amazing blowjob by the way. Thanks!"
            a "Did it help?"
            mc "Uh-huh."
        "Cum on her face[KoGa3AutoWTChange1]{size=-4}(Alexis BeachPoints-2, Alexis Week5 Wednesday Beach CumFace) {/size} {/color}":
            $ Alexis_BeachPoints -= 2
            $ Alexis_Week5_Wednesday_Beach_CumFace = True
            scene 11_1866 with vpunch
            ""
            scene 11_1866 with vpunch
            mc "Fuck..."
            a "..."
            scene 11_1867 with Dissolve(1)
            a "Really now?"
            a "How about a warning next time?"
            mc "Sorry. It just... I didn't know if I could cum in your mouth and..."
            a "Get me a towel, please."
            scene 11_1868 with Dissolve(1)
            mc "You okay?"
            a "I'm fine."
            mc "Did it get into your eyes?"
            a "No."
            scene 11_1863 with Dissolve(1)
            mc "No more cumming on your face then."
            a "Anywhere else is fine. Just not the face. I don't like it."
            mc "Sorry."
            scene 11_1864 with Dissolve(1)
            mc "The blowjob was amazing by the way."
            a "Did it help?"
            mc "Uh-huh."
            scene 11_1865 with Dissolve(1)
            mc "Thanks."
        "Cum on her tits[KoGa3AutoWTChange1]{size=-4}(Alexis Week5 Wednesday Beach CumTits) {/size} {/color}":
            $ Alexis_Week5_Wednesday_Beach_CumTits = True
            scene 11_1869 with vpunch
            ""
            scene 11_1869 with vpunch
            mc "Fuck..."
            a "Ahh..."
            scene 11_1870 with Dissolve(1)
            mc "Sorry, I..."
            a "Haha. No, it's fine."
            a "As long as it's not on my face, I'm okay with anywhere."
            mc "Heh. Good to know."
            a "Can you get me a towel, please?"
            scene 11_1871 with Dissolve(1)
            mc "All clean again?"
            a "No, but it's alright. I needed a shower anyway."
            scene 11_1864 with Dissolve(1)
            mc "The blowjob was amazing by the way."
            a "Did it help?"
            mc "Uh-huh."
            scene 11_1865 with Dissolve(1)
            mc "Thanks."
    $ renpy.end_replay()
    jump Week5_Wednesday_Beach_End

label Week5_Wednesday_Beach_Join_Erynn:
    scene 11_1832 with Dissolve(1)
    n "*Knock-knock*"
    scene 11_1872 with Dissolve(1)
    er "Hey..."
    mc "Hey."
    er "If you're looking for Lexi, she's in the cabin next to this one."
    mc "I know. I actually wanted to talk to you."
    scene 11_1873 with Dissolve(1)
    er "Oh..."
    er "Uhm. Want to come inside?"
    mc "Sure."
    scene 11_1874 with Dissolve(1)
    er "So, what's up?"
    mc "I..."
    mc "{i}(What am I doing here? Why did I come here instead of going to Alexis?){/i}"
    mc "I just wanted to ask if you're okay."
    er "I'm good. Thanks."
    scene 11_1875 with Dissolve(1)
    mc "..."
    mc "{i}(I want to see them again.){/i}"
    mc "{i}(After the photo shoot I just can't get them out of my mind.){/i}"
    scene 11_1876 with Dissolve(1)
    er "We can do more than just take pictures!"
    mc "..."
    scene 11_1877 with Dissolve(1)
    er "[mc]?"
    mc "Hmm?"
    er "Are you okay?"
    mc "Yeah, yeah, no worries. Just thinking."
    scene 11_1878 with Dissolve(1)
    mc "So you won't be joining us at the club?"
    er "Sadly no. I have to wake up early for a shoot."
    mc "Want me to come with you again?"
    er "Thanks, but it will be fine. There will be several girls this time."
    mc "Okay."
    scene 11_1879 with Dissolve(1)
    mc "Did you have fun today?"
    er "Uh-huh. I did. Lots of fun. You?"
    mc "Me too. I love spending time on the beach with pretty girls."
    er "Heh."
    scene 11_1880 with Dissolve(1)
    mc "And the more time I spend with you, the more I..."
    mc "..."
    mc "Never mind."
    er "..."
    scene 11_1881 with Dissolve(1)
    mc "{i}(Fuck. Did I just make this awkward?){/i}"
    mc "{i}(What is she thinking?){/i}"
    scene 11_1882 with Dissolve(1)
    mc "Now I wish I had that thing you have with Lexi."
    mc "The looking at each other and knowing what the other is thinking without actually saying it thing."
    mc "{i}(I really want to know what she's thinking right now.){/i}"
    scene 11_1883 with Dissolve(1)
    mc "Stop doing that!"
    er "Haha. I'm not doing anything."
    mc "Then say something!"
    er "I was hoping you could read my mind."
    scene 11_1884 with Dissolve(1)
    mc "You're so weird."
    er "You're weird!"
    scene 11_1885 with Dissolve(1)
    mc "..."
    er "..."
    scene 11_1886 with Dissolve(1)
    mc "I can't be in here with you any longer. I'll get out before I..."
    if Erynn_Week5_Tuesday_Room_Kiss == True:
        mc "{i}(... Kiss you again.){/i}"
    else:
        mc "{i}(... Kiss you.){/i}"
    mc "I'll let you change."
    er "Uh..."
    scene 11_1887 with Dissolve(1)
    mc "Erynn..."
    er "You told me I can hug you whenever I want."
    mc "{i}(I did say that.){/i}"
    mc "{i}(I can feel her hard nipples pressing up against my back.){/i}"
    scene 11_1888 with Dissolve(1)
    mc "{i}(I'm getting more confused the more time I spend with her.){/i}"
    mc "{i}(Was it too soon to start dating Alexis?){/i}"
    mc "{i}(If... Then maybe... Fuck...){/i}"
    jump Week5_Wednesday_Beach_End

label Week5_Wednesday_Beach_Join_Iris:
    scene 11_1832 with Dissolve(1)
    n "*Knock-knock*"
    scene 11_1889 with Dissolve(1)
    ir "Hey..."
    mc "Hi."
    ir "Did you pick the wrong door, or...?"
    mc "No, I..."
    scene 11_1890 with Dissolve(1)
    ir "Get in!"
    mc "Uh..."
    scene 11_1891 with Dissolve(1)
    ir "..."
    mc "*Sigh*"
    ir "You okay?"
    scene 11_1892 with Dissolve(1)
    mc "I'm just a little confused and have a bunch of questions on my mind right now."
    ir "You and me both. Wanna talk about it?"
    mc "I don't know. Maybe another time."
    ir "Okay. I'm here for you whenever."
    mc "I know."
    scene 11_1893 with Dissolve(1)
    mc "Did you have fun today?"
    ir "I did. Thanks again for doing the double date. Even though it didn't really progress much. Or rather at all."
    ir "But it was fun hanging out with all of you nevertheless. We should do this again."
    scene 11_1894 with Dissolve(1)
    mc "We'll have to anyway, since we lost the volleyball game and have to do whatever they want."
    ir "Right. I forgot about that. That will be fun."
    ir "Imagine if we won. The things I'd have Erynn do..."
    mc "Haha."
    scene 11_1895 with Dissolve(1)
    mc "Uh..."
    ir "What?"
    mc "Nothing... You... Never mind, it's nothing."
    mc "{i}(Why am I still surprised about this?){/i}"
    ir "..."
    scene 11_1896 with Dissolve(1)
    ir "They're pretty small compared to Erynn's and Alexis's, right?"
    mc "..."
    ir "What do you think?"
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 11_1897 at moveup
    pause 3
    mc "I've always thought they were incredible!"
    ir "Thanks."
    mc "{i}(If this was a few months ago, or even a few weeks, I'd be all over them.){/i}"
    mc "{i}(Even now, I have to hold myself back. Why do I put myself in these situations?){/i}"
    scene 11_1898 with Dissolve(1)
    mc "Iris..."
    ir "No one's stopping you from getting out."
    mc "I don't want to open the door while you're naked and..."
    ir "Like that's the issue."
    scene 11_1899 with Dissolve(1)
    mc "{i}(I don't want to leave!){/i}"
    ir "..."
    scene 11_1900 with vpunch
    mc "..."
    scene 11_1901 with Dissolve(1)
    ir "If you weren't with Alexis, we'd be having sex right now."
    mc "{i}(I can feel her pussy rubbing against my dick.){/i}"
    ir "But let's stop this here before we overstep even more boundaries."
    mc "{i}(Would I have stopped if she didn't?){/i}"
    scene 11_1902 with Dissolve(1)
    mc "{i}(I'm so confused...){/i}"
    scene 11_1903 with Dissolve(1)
    ir "Time for you to get out now."
    mc "I'm going, I'm going!"
    scene 11_1904 with Dissolve(1)
    ir "*Sigh*"
    ir "What am I doing?"
    ir "I almost ruined everything..."
    $ renpy.end_replay()
    jump Week5_Wednesday_Beach_End

label Week5_Wednesday_Beach_End:
    scene black with Dissolve(1)
    pause 2
    scene 11_1905 with Dissolve(1)
    mc "Everyone ready?"
    er "Yes!"
    mc "Let's go, then."
    scene 11_1906 with Dissolve(1)
    a "Do you want me to drop you off at home, or the dorm?"
    ir "I'll head home but you don't have to drive me. I'll take the bus."
    a "No, no. It's fine. It's much quicker too."
    ir "Thanks."
    scene 11_1907 with Dissolve(1)
    ir "But you don't have to come to pick me up later."
    ir "We can meet in the city."
    a "Okay. Just text me where."
    scene 11_1908 with Dissolve(1)
    stop music fadeout 1.0
    play music ("Music/LoFi Upbeat 1.mp3", "Music/LoFi Upbeat 2.mp3", "Music/LoFi Upbeat 3.mp3", "Music/LoFi Upbeat 4.mp3") volume 0.2
    ir "*Yawn* Nggh..."
    mc "Someone's tired."
    ir "A little."
    mc "Maybe you should skip the club today."
    scene 11_1909 with Dissolve(1)
    ir "No! I'm not skipping that!"
    ir "Just gonna have a little nap and I'm good to go."
    mc "A nap doesn't sound that bad."
    scene 11_1910 with Dissolve(1)
    ir "We can nap together?"
    a "No, you can't!"
    mc "Haha. You heard the boss."
    ir "You can come too, Alexis. As can Erynn. Let's just make it a slumber party."
    a "No!"
    scene 11_1911 with Dissolve(1)
    ir "I'm probably gonna be sore tomorrow. That volleyball game was the first physical activity I've had in months."
    mc "Most of the time you just stood there."
    ir "Who was it again who scored our point? Our ONLY point, might I add!"
    mc "Haha. Okay, okay."
    if Alexis_Week5_Wednesday_Beach_Join == True:
        scene 11_1912 with Dissolve(1)
        ir "*Whispers* But you seem to have had some reserves."
        mc "Huh?"
        ir "*Whispers* 'I stumbled...'"
        mc "*Whispers* What? I have no idea what you're talking about."
        ir "*Whispers* I heard you!"
        scene 11_1913 with Dissolve(1)
        ir "*Whispers* It sounded pretty hot. Did you have sex?"
        mc "*Shakes head*"
        ir "*Whispers* Blowjob?"
        mc "*Nods*"
        scene 11_1914 with Dissolve(1)
        ir "*Whispers* Do you know what I did?"
        mc "..."
        scene black with Dissolve(1)
        transform moveup:
            xalign 0.5 yalign 1.0
            linear 5.0 yalign 0.0
        show 11_1915 at moveup
        pause 3
        mc "{i}(I don't know if she's serious or not...){/i}"
        mc "{i}(But I can't stop imagining it now.){/i}"
        scene 11_1916 with Dissolve(1)
        mc "I call bullshit!"
        ir "Haha. I guess you'll never know."
    else:
        pass
    scene black with Dissolve(1)
    pause 2
    scene 11_1917 with Dissolve(1)
    ""
    scene 11_1918 with Dissolve(1)
    er "Today was really fun."
    er "Thanks for driving, Lex, and picking all of us up."
    a "No problem."
    scene 11_1919 with Dissolve(1)
    a "Call me tomorrow after your shoot."
    er "Will do."
    scene 11_1920 with Dissolve(1)
    er "Thanks for hanging out with us girls."
    mc "Anytime!"
    er "Then let's do it again soon. Very soon!"
    scene 11_1921 with Dissolve(1)
    mc "But we'll change teams next time."
    mc "I'm not letting you guys team up again."
    er "Haha. Sure."
    scene 11_1922 with Dissolve(1)
    er "Have fun at the club!"
    mc "We will. Bye, Erynn."
    er "Bye-bye."
    scene 11_1923 with Dissolve(1)
    er "Oh, and Lex. Let's think about what we want them to do for a whole day."
    a "I forgot about that. But I might have an idea."
    er "Let's talk about this later. I'm excited!"
    a "Me too. Bye!"
    mc "..."
    scene 11_1924 with Dissolve(1)
    mc "So, what's the idea?"
    a "You'll have to wait and see."
    mc "Tell me!"
    a "I'm not telling you!"
    scene 11_1925 with Dissolve(1)
    a "Aaah... [mc]!"
    mc "Tell me!"
    a "Nooo... Haha."
    scene 11_1926 with Dissolve(1)
    ""
    scene 11_1927 with Dissolve(1)
    mc "I'll get you to spill. One way or another."
    a "Mmm..."
    scene 11_1928 with Dissolve(1)
    a "..."
    a "[mc]! Stop!"
    mc "Then tell me!"
    a "No, uhm..."
    scene 11_1929 with Dissolve(1)
    mc "Mom!"
    m "I'm sorry. I didn't want to interrupt."
    a "Hi, Emily."
    m "Hey, Alexis. How are you?"
    scene 11_1930 with Dissolve(1)
    a "I'm good... How..."
    a "Oh my god. I'm parked in the middle of the driveway."
    a "I'm so sorry, I'll..."
    m "It's fine. Don't worry about it."
    scene 11_1931 with Dissolve(1)
    m "Are you guys leaving, or...?"
    mc "We just came back from the beach with Erynn and Iris."
    m "Fun! Wasn't it crowded?"
    mc "It was alright. We went to Minerva Shore."
    m "Good choice. I drove past Madison Beach and that was chaos."
    if Emily_Week1_Saturday_BeachInvite == True:
        $ Emily_Week5_Wednesday_BeachInvite_Adriana = True
        scene 11_1932 with Dissolve(1)
        m "When are we going to the beach? You invited me a few weeks ago, remember?"
        mc "I know. Just..."
        a "You can join us next time."
        scene 11_1933 with Dissolve(1)
        a "I can ask Mom if she wants to come, too."
        m "I'd love that! Thanks."
        mc "..."
    else:
        pass
    scene 11_1934 with Dissolve(1)
    m "Alexis. Do you have time? Want to come inside and have a coffee with me?"
    a "Uh..."
    mc "Yeah. Do you want to have coffee with my mom?"
    scene 11_1935 with Dissolve(1)
    a "..."
    if Alexis_Week5_Wednesday_Beach_Join == True:
        mc "You like to have coffee, right? We had coffee at the beach too. Sorta..."
    else:
        mc "You like to have coffee, right?"
    a "[mc]... Stop..."
    mc "Haha."
    scene 11_1936 with Dissolve(1)
    m "What's so funny about coffee?"
    mc "Nothing. It's just a little inside joke."
    m "Hmm..."
    scene 11_1937 with Dissolve(1)
    mc "But she can't. She has to leave and get ready for later."
    a "Next time, though."
    m "Alright."
    scene 11_1938 with Dissolve(1)
    m "Anyway. I'm heading inside."
    m "Nice to see you again, Alexis."
    a "You too, Emily. Bye."
    scene 11_1939 with vpunch
    mc "Hey!"
    a "Stop embarrassing me in front of your mom!"
    mc "Haha, I didn't. I just talked about coffee."
    a "Your mom isn't stupid. She knows something's up."
    mc "Haha."
    if Emily_Week5_Wednesday_BeachInvite_Adriana == True:
        scene 11_1940 with Dissolve(1)
        mc "Sorry, sorry."
        a "..."
        scene 11_1941 with Dissolve(1)
        mc "So... A beach date with our moms, huh?"
        mc "Kill-Fuck-Marry will be very awkward then."
        a "Oh my god... Haha."
        a "I hadn't thought about that."
        scene 11_1942 with Dissolve(1)
        a "I guess I'll have to fuck your mom then."
        mc "Alexis!"
        a "Haha."
        scene 11_1943 with Dissolve(1)
        mc "Seriously? What's with you girls liking my mom? First Erynn says that she has a nice ass."
        mc "Then Iris flirts with her."
        mc "Now you..."
        a "Well. Your mom is very pretty."
        mc "..."
        scene 11_1944 with Dissolve(1)
        mc "Okay. You know what?"
        mc "I'll fuck your mom then!"
        a "HEY!"
        scene 11_1945 with Dissolve(1)
        mc "What? You can fuck mine but I can't fuck yours?"
        mc "How is that fair?"
        a "..."
        scene 11_1946 with Dissolve(1)
        a "You slapped my mom's butt, remember? That should be plenty!"
        mc "Right. That happened."
        a "Like you needed a reminder. I can see it on your face!"
        scene 11_1947 with Dissolve(1)
        mc "You're right. I'll never forget the sensation..."
        mc "The nice peachy shape... The softness..."
        a "..."
        scene 11_1948 with Dissolve(1)
        a "And mine is this hard, bony..."
        mc "No. Yours is the same. That's why I confused it. It's a compliment really."
        a "The more I think about it, the less I believe it was an accident!"
        mc "Haha."
    else:
        pass
    scene 11_1949 with Dissolve(1)
    a "I'm leaving!"
    mc "But we're having so much fun..."
    mc "When are you picking me up?"
    a "Never!"
    mc "Haha."
    scene 11_1950 with Dissolve(1)
    a "Eight o'clock sharp!"
    a "And you better be ready and waiting here, or I'll leave without you!"
    mc "Yes, Mom!"
    scene 11_1951 with Dissolve(1)
    mc "You are so sexy when you're angry, or rather, pretending to be angry."
    a "Shut up!"
    a "..."
    a "I love you!"
    mc "Haha. Love you too. See you later."
    scene black with Dissolve(1)
    pause 2
    if Erynn_LikeMC == True:
        scene 11_1952 with Dissolve(1)
        mc "{i}(I'm so confused about Erynn and if I made the correct decision being with Lexi.){/i}"
        mc "{i}(But then this stuff happens and...){/i}"
        mc "Man..."
    else:
        pass
    scene 11_1953 with Dissolve(1)
    mc "..."
    mc "What's with that look again?"
    m "What look? I don't have a look. I'm just enjoying my coffee."
    mc "Uh-huh."
    scene 11_1954 with Dissolve(1)
    m "Come here for a second."
    mc "See! I knew you wanted something."
    scene 11_1955 with Dissolve(1)
    mc "What is it?"
    m "Is she your girlfriend?"
    mc "*Sigh* That again?"
    m "You never answered me."
    scene 11_1956 with Dissolve(1)
    mc "..."
    m "Tell me, please."
    mc "I'm not telling you."
    scene 11_1957 with Dissolve(1)
    mc "What are you doing? Stop!"
    m "Using your tactics against you."
    m "You're gonna tell me one way or another."
    mc "Mom!"
    scene 11_1958 with Dissolve(1)
    m "Mmm..."
    mc "Fine. Fine. FINE!"
    mc "I'll tell you!"
    scene 11_1959 with Dissolve(1)
    mc "Yes!"
    m "Yes as in...?"
    mc "Yes, she's my girlfriend."
    scene 11_1960 with Dissolve(1)
    m "I knew it!"
    mc "Then why did you even ask?"
    m "Because I wanted to hear it from you."
    scene 11_1961 with Dissolve(1)
    m "You look good together."
    m "I like her."
    scene 11_1962 with Dissolve(1)
    m "Who asked who?"
    mc "I did."
    m "Aw. How did you do it?"
    mc "*Sigh*"
    scene 11_1963 with Dissolve(1)
    m "Oh, come on. You can't stop now."
    m "I love this kinda stuff."
    mc "We played a game."
    m "A game?"
    scene 11_1964 with Dissolve(1)
    mc "Truth or dare."
    mc "She picked dare and I dared her to be my girlfriend."
    m "That's so cute!"
    mc "..."
    scene 11_1965 with Dissolve(1)
    m "You have a little romantic side."
    mc "I wouldn't call it romantic."
    mc "It was just on the street in the city."
    m "I think it's romantic. And I'm sure Alexis thought so too."
    scene 11_1966 with Dissolve(1)
    mc "But enough of this. I want to take a shower."
    mc "Can you get up?"
    m "No... Not yet! Give me five minutes."
    m "I need a little affection. I missed out on this for so long!"
    mc "Five minutes!"
    scene 11_1967 with Dissolve(1)
    m "Ten minutes!"
    mc "*Shakes head*"
    jump Week5_Wednesday_Club_Alexis

label Week5_Wednesday_Beach_Alexis_SP:
    scene black with Dissolve(1)
    pause 2
    stop music fadeout 1.0
    play music ("Music/LoFi Upbeat 1.mp3", "Music/LoFi Upbeat 2.mp3", "Music/LoFi Upbeat 3.mp3", "Music/LoFi Upbeat 4.mp3") volume 0.2
    scene 11_1423 with Dissolve(1)
    mc "Haha."
    mc "The dragon ate him..."
    mc "That's what you get!"
    play sound "Sounds/CarHonk.mp3" volume 0.1
    n "*Beep-beep*"
    scene 11_1424 with Dissolve(1)
    mc "{i}(That sounded close.){/i}"
    play sound "Sounds/CarHonk.mp3" volume 0.1
    n "*Beep-beep*"
    mc "{i}(Kay. What's going on?){/i}"
    scene 11_1425 with Dissolve(1)
    mc "{i}(Oh... It's them.){/i}"
    mc "{i}(I didn't think we'd be going this early.){/i}"
    scene 11_1426 with Dissolve(1)
    er "Are you coming?"
    ir "Get in, loser! We're going to the beach!"
    mc "..."
    mc "{i}(Damn... They're all wearing bikinis already!){/i}"
    scene 11_1968 with Dissolve(1)
    mc "Hey girls!"
    er "Hey."
    mc "Is that your car, Alexis?"
    a "No, It's my dad's. He let me borrow it for today."
    scene 11_1969 with Dissolve(1)
    mc "Man... It's a really nice car."
    mc "Maybe in twenty years, if I'm lucky. *Sigh* A man can dream."
    er "Dream or marry a rich woman."
    mc "That's also an option. Good thinking, Erynn."
    scene 11_1431 with Dissolve(1)
    mc "Hi!"
    er "Hey."
    scene 11_1432 with Dissolve(1)
    ir "..."
    ir "Where's mine?"
    mc "Hey, Iris."
    ir "I mean my kiss!"
    mc "You called me a loser, you don't get one!"
    scene 11_1433 with Dissolve(1)
    ir "I didn't. That was a scene from a movie."
    ir "We even watched it together some time ago."
    a "It's from Mean Girls."
    ir "See!"
    scene 11_1434 with Dissolve(1)
    mc "Fine!"
    ir "Thanks."
    scene 11_1435 with Dissolve(1)
    ir "*Whispers* Besides. I'd never call you a loser."
    ir "*Whispers* You should know that!"
    scene black with Dissolve(1)
    pause 2
    scene 11_1436 with Dissolve(1)
    ""
    stop music fadeout 1.0
    play music "Music/Mia Rodriguez - California Girls.mp3" volume 0.6
    scene 11_1970 with Dissolve(1)
    mc "Are you serious? This song?"
    mc "Did you girls plan this?"
    er "No. It's the radio."
    mc "..."
    scene 11_1438 with Dissolve(1)
    er "You want it louder?"
    mc "No! Please change the channel."
    er "Louder it is!"
    scene 11_1439 with Dissolve(1)
    n "*Singing* California Girls..."
    mc "{i}(Are you kidding me? What have I done?){/i}"
    mc "Nooo... Why did I come again?"
    er "Haha."
    scene 11_1440 with Dissolve(1)
    mc "{i}(I'm just gonna hide here for a bit.){/i}"
    ir "What are you doing?"
    mc "Nothing."
    scene 11_1441 with Dissolve(1)
    ir "You're sitting in a car with three extremely hot girls."
    ir "You should be lots of things, but embarrassed isn't one of them!"
    ir "Let's have some fun!"
    scene 11_1442 with Dissolve(1)
    ir "Come on!"
    mc "*Singing* California Girls..."
    er "Haha. Sounds great! Such talent."
    mc "Shut up..."
    scene 11_1445 with Dissolve(1)
    play sound "Sounds/CarHonk.mp3" volume 0.1
    n "*Beep-beep*"
    a "..."
    scene 11_1446 with Dissolve(1)
    x "Hey, Alexis. What's up? Sweet car you've got there."
    mc "{i}(I'm not the only one who likes the car.){/i}"
    x "Not working at the bar today?"
    a "As you can see!"
    x "Oh, I can see! Looking good in a bikini!"
    scene 11_1447 with Dissolve(1)
    x "Going to the beach? Why not hang out with us?"
    a "Not interested!"
    x "Don't be like that. It will be fun! Bring your friends."
    x "And your gay friend can come too!"
    scene 11_1448 with Dissolve(1)
    mc "{i}(Okay. That's enough.){/i}"
    ir "Don't!"
    scene 11_1449 with Dissolve(1)
    er "He..."
    ir "He wasn't gay when he fucked the three of us this morning."
    x "What?"
    ir "Exactly! What do you boys know about fucking a girl?"
    ir "Nothing! You're too busy jerking each other's small dicks off."
    scene 11_1450 with Dissolve(1)
    x "What did you say, slut?"
    ir "LOSERS!"
    scene 11_1451 with Dissolve(1)
    er "Oh my god, Iris..."
    mc "{i}(Yeah, that's Iris for you.){/i}"
    a "Haha. Thanks, Iris!"
    ir "Sure. They're just a bunch of idiots."
    scene 11_1452 with Dissolve(1)
    er "You know those guys, Lex?"
    a "Don't really know them. They come to the bar quite often."
    mc "{i}(Probably not the only guys who try to flirt with her.){/i}"
    scene 11_1453 with Dissolve(1)
    mc "Thanks for sticking up for me."
    ir "Always."
    mc "But you really need to be more careful. One day you won't get away with that."
    scene 11_1971 with Dissolve(1)
    ir "*Whispers* Thanks for still worrying about me!"
    scene black with Dissolve(1)
    pause 2
    scene 11_1972 with Dissolve(1)
    play music "Sounds/Ocean.mp3" volume 0.5
    ""
    scene 11_1973 with Dissolve(1)
    er "*Whispers* Hey. Can you do me a favour?"
    mc "*Whispers* Sure. What is it?"
    er "*Whispers* Can you carry Alexis's bag? There's also some of my stuff and Iris's in there and it's quite heavy."
    mc "*Whispers* Yeah. No problem."
    er "*Whispers* Thanks."
    scene 11_1974 with Dissolve(1)
    mc "Let me carry your bag."
    a "It's..."
    mc "No, just give it!"
    a "Thanks."
    scene 11_1975 with Dissolve(1)
    mc "Why are you looking like that all of a sudden?"
    mc "Your bag isn't nearly as big or heavy as Alexis's!"
    mc "And if you wanted me to carry yours, why not just say so?"
    scene 11_1461 with Dissolve(1)
    er "..."
    mc "{i}(Are you kidding me?){/i}"
    mc "Puppy dog eyes... Really?"
    er "..."
    mc "Fine... FINE!"
    scene 11_1976 with Dissolve(1)
    er "Hehe. Still works!"
    mc "It's so dumb. It's. So. Dumb!"
    scene 11_1977 with Dissolve(1)
    ir "And while you're at it. Here's mine!"
    mc "Really, Iris? I thought you were on my side?"
    ir "I am."
    mc "..."
    ir "Thank you!"
    scene 11_1464 with Dissolve(1)
    mc "Now I know why I was invited. To carry all your shit!"
    er "You offered!"
    mc "I offered to carry Alexis's. The rest of you weaselled your way to me carrying your bags."
    er "Weaselled... Haha."
    scene 11_1465 with Dissolve(1)
    er "He's cute when he's angry."
    ir "He is, isn't he?"
    ir "But you need to see him when he's really angry and not pretending. So cute!"
    mc "..."
    scene 11_1466 with Dissolve(1)
    mc "{i}(Heh...){/i}"
    mc "{i}(She isn't wasting any time, huh?){/i}"
    scene 11_1467 with Dissolve(1)
    ir "..."
    mc "*Shakes head*"
    scene black with Dissolve(1)
    pause 2
    scene 11_1468 with Dissolve(1)
    er "Shall we set up here? It's a little away from all the other people."
    a "Seems good to me."
    er "Or we can..."
    mc "Nope! This is the spot!"
    er "Haha. Sure. Thanks for carrying our stuff."
    scene 11_1978 with Dissolve(1)
    ""
    menu:
        "Watch Alexis[KoGa3AutoWTChange1]{size=-4}(Alexis SP+2) {/size} {/color}":
            $ Alexis_SP += 2
            # Alexis_SP (6)
            scene 11_1470 with Dissolve(1)
            mc "..."
            mc "{i}(I wouldn't mind seeing those again.){/i}"
            mc "{i}(But I think Layla's are bigger.){/i}"
            scene 11_1979 with Dissolve(1)
            a "..."
            scene 11_1473 with Dissolve(1)
            a "Do you need something?"
            mc "Hmm?"
            a "Sunscreen?"
            mc "Uhm, no. I'm good. Thanks."
        "Watch Erynn":
            scene 11_1471 with Dissolve(1)
            mc "..."
            mc "{i}(She has a good ass!){/i}"
        "Watch Iris":
            scene 11_1472 with Dissolve(1)
            mc "..."
            mc "{i}(How many times have I seen her undress?){/i}"
            mc "{i}(Never gets old.){/i}"
        "Do nothing":
            pass
    scene black with Dissolve(1)
    pause 2
    scene 11_1980 with Dissolve(1)
    ir "Is it weird for you that you're hanging out with only girls?"
    mc "Not really. I grew up hanging around Erynn all the time."
    mc "And nowadays, I think I have more girl friends than guy friends anyway."
    ir "So, nothing's changed!"
    mc "Heh..."
    scene 11_1981 with Dissolve(1)
    mc "By the way Alexis. I wanted to ask you earlier. Where did you get those sunglasses?"
    a "I think I got them at the mall. Don't know the name of the store. The one next to Delta Sport."
    mc "They look good on you. I like them."
    a "Thanks. Want to try them on?"
    mc "Can I? Sure."
    scene 11_1982 with Dissolve(1)
    a "Uhm..."
    a "I was about to hand them to you but... Yeah, just take them, I guess."
    mc "Thanks."
    a "Are you always this forward?"
    mc "What do you mean?"
    a "Never mind."
    scene 11_1482 with Dissolve(1)
    mc "What do you think?"
    a "Looks good. They suit you."
    mc "Yeah? Let me get my phone. I want to see for myself."
    scene 11_1983 with Dissolve(1)
    er "Let me take the picture for you."
    mc "Thanks."
    er "You get in the picture too, Lexi!"
    a "Uhm..."
    scene 11_1984 with Dissolve(1)
    a "..."
    scene 11_1484 with Dissolve(1)
    er "Alright."
    er "Big smiles!"
    scene 11_1985 with Dissolve(1)
    mc "*Whispers* This feels like deja vu."
    a "*Whispers* It does. I'm happy you're wearing shorts this time though!"
    mc "Haha. Yeah... Me too."
    scene 11_1485 with Dissolve(1)
    er "So cute, right?"
    ir "The cutest!"
    er "They would be so good together."
    ir "Mm-hmm..."
    scene 11_1986 with Dissolve(1)
    mc "Let's see!"
    mc "Damn, I'm so good-looking!"
    a "Haha. And not at all conceited."
    mc "Right? Where do you find guys like that?"
    a "*Shakes head*"
    menu:
        "Compliment Alexis[KoGa3AutoWTChange1]{size=-4}(Alexis SP+2) {/size} {/color}":
            $ Alexis_SP += 2
            # Alexis_SP (8)
            scene 11_1987 with Dissolve(1)
            mc "You look good, too!"
            a "Thanks..."
            mc "It's a nice picture."
        "Say nothing":
            pass
    scene 11_1488 with Dissolve(1)
    mc "You want me to take a picture of you guys?"
    ir "Yes! YES!"
    er "Sure."
    mc "Get a little closer then."
    scene 11_1489 with Dissolve(1)
    mc "{i}(A little closer...){/i}"
    mc "{i}(Seeing them together last time and now this...){/i}"
    mc "{i}(I can't unsee it.){/i}"
    scene 11_1490 with Dissolve(1)
    mc "When I saw you together last time, I thought this already."
    mc "You actually look so much alike. You two could be sisters."
    er "You think?"
    a "Yeah. Now that you mention it. I can see some similarities."
    ir "What? NO! Don't say that! We can't be sisters! Don't ruin our moment! Let's take another picture!"
    mc "Haha."
    scene 11_1491 with Dissolve(1)
    er "Iris! What are you doing?"
    ir "Proving we're not sisters!"
    er "Haha."
    scene 11_1492 with Dissolve(1)
    er "Since we're taking pictures, I have to show you one."
    er "I told you about this one before. Maybe you remember it."
    a "Let's see."
    mc "{i}(Is it Erynn dressed up? For a photo shoot maybe?){/i}"
    scene 11_1493 with Dissolve(1)
    a "Oh no... Erynn... What did you do?"
    a "The poor boy."
    mc "{i}(Boy?){/i}"
    ir "Well that explains a lot of things!"
    mc "{i}(What's going on?){/i}"
    scene 11_1494 with Dissolve(1)
    mc "What's so funny?"
    a "You don't want to see this."
    er "Just my old dress-up doll."
    mc "{i}(Dress-up doll...? No...){/i}"
    mc "Show me!"
    scene 11_1495 with Dissolve(1)
    mc "..."
    mc "Are you kidding me?"
    er "Remember this?"
    mc "I don't want to remember that! Why do you even have that?"
    er "I told you I have lots of pictures from when you were younger."
    scene 11_1496 with Dissolve(1)
    a "Let me see that one again."
    a "Did you put makeup on him?"
    er "He didn't mind the blush and the eyeliner."
    er "But he drew the line at lipstick. Said it was too girly."
    mc "..."
    scene 11_1988 with Dissolve(1)
    mc "Delete it!"
    er "Aaah... [mc]! Haha."
    mc "I said to delete it!"
    er "Never!"
    scene 11_1989 with Dissolve(1)
    er "[mc]!"
    er "Lexi, help me!"
    a "You took the picture, your mess. I'm not getting involved."
    er "Iris!"
    mc "Don't you dare, Iris."
    scene 11_1990 with Dissolve(1)
    er "Oh, hey Valeria."
    mc "I'm not falling for your cheap distraction tactics."
    va "Hey, Erynn."
    scene 11_1991 with Dissolve(1)
    mc "..."
    a "Hey!"
    va "Hey, Alexis, [mc]."
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 11_1504 at moveup
    pause 3
    mc "Hey..."
    scene 11_1506 with Dissolve(1)
    mc "{i}(Why does Darryl have a guitar?){/i}"
    mc "{i}(Trying to serenade Valeria?){/i}"
    mc "{i}(I bet he can't even play.){/i}"
    scene 11_1508 with Dissolve(1)
    da "Three girls this time..."
    da "Seriously. Who is this guy?"
    tj "No idea, man."
    da "You know them, Val?"
    scene 11_1509 with Dissolve(1)
    va "A little? The long-haired blonde is Erynn."
    da "Yeah, I know who Erynn is."
    va "The brunette is Alexis, Layla's sister."
    da "Layla? As in Layla from the track team? Didn't know she had a sister."
    va "I don't know who the other blonde is."
    if Tori_Week3_Saturday_TC_Sex == True:
        scene black with Dissolve(1)
        transform moveup:
            xalign 0.5 yalign 1.0
            linear 5.0 yalign 0.0
        show 11_1510 at moveup
        pause 3
        mc "{i}(Looking good, Tori!){/i}"
        mc "{i}(I get horny just from looking at her.){/i}"
    else:
        pass
    scene 11_1512 with Dissolve(1)
    mc "{i}(Look at his smug face.){/i}"
    mc "{i}(Like you have a chance with her...){/i}"
    scene 11_1513 with Dissolve(1)
    a "I didn't know you know Valeria."
    er "I met her when I drove [mc] to school right before the training camp. She's Zach's girlfriend."
    a "Zach's girlfriend? We're talking about the same Zach, right? [mc]'s friend?"
    mc "{i}(Friend...){/i}"
    mc "She isn't Zach's girlfriend!"
    scene 11_1514 with Dissolve(1)
    er "No? Hmm... I thought she was. She seemed very annoyed when Zach tried to flirt with me."
    a "Who isn't annoyed with Zach?"
    mc "Exactly."
    scene 11_1515 with Dissolve(1)
    er "Back to the pictures."
    er "Do you still have pictures of you and [mc]?"
    ir "I have some, yeah."
    er "Can we look at them?"
    scene 11_1517 with Dissolve(1)
    er "Iris! You had long hair?"
    er "I didn't know that."
    ir "I cut it when I moved here."
    scene 11_1518 with Dissolve(1)
    er "Any special reason for that?"
    ir "Not really. A new beginning, I guess."
    er "I like the long hair."
    ir "Yeah? I might grow it out again."
    mc "{i}(Don't try too hard, Iris!){/i}"
    scene 11_1519 with Dissolve(1)
    er "Look at his face! So cute."
    er "Can you send me that picture? I don't have any of [mc] from his time in Alvarado."
    ir "Sure."
    scene 11_1522 with Dissolve(1)
    er "Haha. That looks fun."
    a "Hmm... I think I've seen that guy before. He seems familiar. But I can't remember where from."
    ir "Nathan?"
    a "I don't know. I could be wrong though."
    scene 11_1523 with Dissolve(1)
    er "John teaching [mc] to ride a bike."
    a "That's your dad, Iris?"
    ir "Uh-huh."
    er "He's a hottie, right?"
    a "He is!"
    mc "..."
    scene 11_1524 with Dissolve(1)
    er "Oh..."
    ir "Ups!"
    scene 11_1525 with Dissolve(1)
    a "Uhm..."
    er "Iris!"
    ir "Haha. Sorry. Didn't mean to show that one."
    scene 11_1526 with Dissolve(1)
    mc "What picture are you talking about?"
    mc "Can I see for a sec?"
    er "No!"
    a "No, you can't!"
    scene 11_1527 with Dissolve(1)
    mc "Oh, come on!"
    mc "I've probably seen it before!"
    er "Another reason why you don't need to see it!"
    mc "..."
    scene 11_1529 with Dissolve(1)
    er "How did you guys actually meet? Did you go to school together?"
    ir "We met in a park."
    scene 11_1530 with Dissolve(1)
    ir "Funny enough. It started with a picture."
    mc "Not this again..."
    er "Let her tell the story!"
    mc "*Sigh*"
    scene 11_1531 with Dissolve(1)
    mc "..."
    scene 11_1532 with Dissolve(1)
    mc "{i}(What the hell? Are they actually dating?){/i}"
    mc "{i}(Can't be. Isn't he with Tori?){/i}"
    scene 11_1533 with Dissolve(1)
    mc "I'm going to the bar to get an iced coffee or something."
    mc "Anyone wants anything?"
    ir "Can you get me caramel macchiato? Thanks."
    er "Same for me."
    a "Make that three."
    scene 11_1534 with Dissolve(1)
    mc "Alright. Be right back."
    a "Thank you!"
    er "Thanks, [mc]."
    scene 11_1535 with Dissolve(1)
    ""
    if Tori_End == False:
        scene 11_1538 with Dissolve(1)
        mc "..."
        to "Guess who. And you'd better answer correctly!"
        scene 11_1539 with Dissolve(1)
        mc "Sup, Tori."
        mc "What do you want?"
        scene 11_1540 with Dissolve(1)
        to "I think you know what I want!"
        mc "Uh..."
        mc "I'm here with my friends."
        if Tori_Week3_Saturday_TC_Sex == True:
            to "What does that matter? I saw you looking at me!"
        else:
            to "What does that matter?"
            mc "{i}(I rejected her last time, but she keeps on trying.){/i}"
            menu:
                "Reject Tori[KoGa3AutoWTChange1]{size=-4}(Tori End) {/size} {/color}":
                    $ Tori_End = True
                    scene 11_1541 with Dissolve(1)
                    mc "How many times do I have to tell you that I'm not interested?"
                    mc "Leave already."
                    to "..."
                    scene 11_1543 with Dissolve(1)
                    to "*Sigh*"
                    to "*You're so fucking boring!"
                    mc "{i}(That girl has problems.){/i}"
                    scene 11_1536 with Dissolve(1)
                    bt "Hi."
                    mc "Hey."
                    bt "What can I get you?"
                    mc "Four caramel macchiato, please."
                    scene 11_1537 with Dissolve(1)
                    bt "Here you go!"
                    mc "Thanks."
                    scene 11_1586 with Dissolve(1)
                    er "That was quick."
                    mc "Yeah. Wasn't that busy."
                    jump Week5_Wednesday_Beach2_Alexis_SP
                "Go with Tori[KoGa3AutoWTChange1]{size=-4}(Tori Points+2, Tori Week5 Wednesday Beach Sex) {/size} {/color}":
                    $ Tori_Points += 2
                    $ Tori_Week5_Wednesday_Beach_Sex = True
                    jump Week5_Wednesday_Beach_Tori
        scene 11_1541 with Dissolve(1)
        mc "What about Darryl?"
        to "What about him?"
        mc "Aren't you here with him?"
        to "He's busy with Valeria. Besides. I have more fun with you!"
        scene 11_1542 with Dissolve(1)
        to "Can we go already?"
        to "I'm fucking horny!"
        menu:
            "Go with her[KoGa3AutoWTChange1]{size=-4}(Tori Points+2, Tori Week5 Wednesday Beach Sex) {/size} {/color}":
                $ Tori_Points += 2
                # Tori (18)
                $ Tori_Week5_Wednesday_Beach_Sex = True
                jump Week5_Wednesday_Beach_Tori
            "Stay[KoGa3AutoWTChange1]{size=-4}(Tori Points-2) {/size} {/color}":
                $ Tori_Points -= 2
                mc "I can't, Tori. I..."
                scene 11_1543 with Dissolve(1)
                to "*Sigh*"
                to "*Why is everyone so fucking boring?"
                mc "{i}(What the fuck is her problem again?){/i}"
                scene 11_1536 with Dissolve(1)
                bt "Hi."
                mc "Hey."
                bt "What can I get you?"
                mc "Four caramel macchiato, please."
                scene 11_1537 with Dissolve(1)
                bt "Here you go!"
                mc "Thanks."
                scene 11_1586 with Dissolve(1)
                er "That was quick."
                mc "Yeah. Wasn't that busy."
                jump Week5_Wednesday_Beach2_Alexis_SP
    else:
        scene 11_1536 with Dissolve(1)
        bt "Hi."
        mc "Hey."
        bt "What can I get you?"
        mc "Four caramel macchiato, please."
        scene 11_1537 with Dissolve(1)
        bt "Here you go!"
        mc "Thanks."
        scene 11_1586 with Dissolve(1)
        er "That was quick."
        mc "Yeah. Wasn't that busy."
        jump Week5_Wednesday_Beach2_Alexis_SP

label Week5_Wednesday_Beach2_Alexis_SP:
    scene 11_1587 with Dissolve(1)
    mc "Here you go. Everyone take one."
    er "Thank you."
    a "Thanks, [mc]."
    scene 11_1588 with Dissolve(1)
    er "Iris told us how you met. About that picture..."
    mc "*Sigh* I know, okay? It was a mistake and I was punished for it."
    ir "That's what I was? Punishment?"
    mc "Oh, come on... You know what I mean."
    scene 11_1589 with Dissolve(1)
    er "..."
    a "..."
    scene 11_1590 with Dissolve(1)
    er "..."
    mc "{i}(What the fuck are they doing?){/i}"
    scene 11_1591 with Dissolve(1)
    mc "Are you seriously having a conversation by just looking at each other?"
    mc "Girls are so weird."
    er "..."
    mc "Oh... I know what that look means! Run!"
    scene 11_1592 with Dissolve(1)
    mc "That reminds me of that one meme."
    mc "When that guy says run and then the music. Duuh-duh-duh-duh-duh. You know it?"
    er "And you say girls are weird..."
    mc "Haha."
    scene black with Dissolve(1)
    pause 2
    scene 11_1593 with Dissolve(1)
    ir "Let's play a game, [mc]."
    ir "Us three girls. Kill-Fuck-Marry. Go!"
    mc "Hell no!"
    ir "What? Why not?"
    mc "Because girls are emotional and someone will get their feelings hurt. And I'll be labelled as the bad guy."
    scene 11_1594 with Dissolve(1)
    ir "No... It's just for fun."
    ir "We'll play too, right?"
    er "Yeah, why not?"
    scene 11_1595 with Dissolve(1)
    mc "*Sigh* Fine... I guess..."
    ir "Cool. You start."
    mc "Alright. Let's see."
    mc "Kill... Hmm..."
    menu:
        "Alexis[KoGa3AutoWTChange1]{size=-4}(Alexis SP-2, KFM Kill Alexis) {/size} {/color}":
            $ Alexis_SP -= 2
            $ KFM_Kill_Alexis = True
            scene 11_1992 with Dissolve(1)
            mc "Sorry, Alexis. Just for the sole reason that I know you the least."
            a "Sure, it's fine."
            er "No, it's not. Don't kill Lexi!"
            mc "Would you rather have me kill you?"
            er "No..."
            scene 11_1607 with Dissolve(1)
            ir "Who do you fuck and marry?"
            mc "I still have to answer?"
            ir "Well yeah!"
            mc "Hmm... Okay. I'll..."
            menu:
                "Fuck Erynn[KoGa3AutoWTChange1]{size=-4}(KFM Fuck Erynn, KFM Marry Iris) {/size} {/color}":
                    $ KFM_Fuck_Erynn = True
                    $ KFM_Marry_Iris = True
                    scene 11_1608 with Dissolve(1)
                    mc "I'll fuck Erynn and marry Iris."
                    er "Uhm..."
                    ir "I was fine with either one. But sure. I'll marry you."
                "Fuck Iris[KoGa3AutoWTChange1]{size=-4}(KFM Fuck Iris, KFM Marry Erynn) {/size} {/color}":
                    $ KFM_Fuck_Iris = True
                    $ KFM_Marry_Erynn = True
                    scene 11_1609 with Dissolve(1)
                    mc "I'll fuck Iris and marry Erynn."
                    er "Oh... Thanks."
                    ir "I was fine with either one. So, sure. Let's fuck."
        "Erynn[KoGa3AutoWTChange1]{size=-4}(KFM Kill Erynn) {/size} {/color}":
            $ KFM_Kill_Erynn = True
            scene 11_1610 with Dissolve(1)
            mc "Sorry, Erynn. But I'll have to kill you."
            er "What? Why would you kill me? I'm always nice to you..."
            mc "I can't kill Alexis because of Layla. And if I kill Iris, John kills me."
            mc "And you've seen John. It won't be pretty!"
            ir "Haha. You're right about that."
            er "Still..."
            scene 11_1611 with Dissolve(1)
            mc "Sorry."
            mc "You can kill me when it's your turn."
            er "..."
            menu:
                "Fuck Alexis[KoGa3AutoWTChange1]{size=-4}(KFM Fuck Alexis, KFM Marry Iris, Alexis SP+2) {/size} {/color}":
                    $ KFM_Fuck_Alexis = True
                    $ KFM_Marry_Iris = True
                    $ Alexis_SP += 2
                    scene 11_1993 with Dissolve(1)
                    mc "Fuck and marry..."
                    mc "{i}(I've fucked Iris. I guess I'll give Alexis a go.){/i}"
                    mc "{i}(That sounded so bad.){/i}"
                    mc "I think I'll fuck Alexis."
                    a "Uh... O-kay..."
                    scene 11_1613 with Dissolve(1)
                    mc "And then marry Iris."
                    ir "Sure. I'd marry you!"
                "Fuck Iris[KoGa3AutoWTChange1]{size=-4}(KFM Fuck Iris, KFM Marry Alexis, Alexis SP+4) {/size} {/color}":
                    $ KFM_Fuck_Iris = True
                    $ KFM_Marry_Alexis = True
                    $ Alexis_SP += 4
                    # Alexis_SP (12)
                    scene 11_1613 with Dissolve(1)
                    mc "I guess I'll fuck Iris and marry Alexis."
                    a "..."
                    ir "I was okay with both choices. So yeah, let's fuck!"
        "Iris[KoGa3AutoWTChange1]{size=-4}(KFM Kill Iris) {/size} {/color}":
            $ KFM_Kill_Iris = True
            scene 11_1596 with Dissolve(1)
            mc "I'll kill you, Iris!"
            mc "Because you make us play this stupid game!"
            ir "Haha."
            ir "If that's the only reason, I'm fine with it."
            menu:
                "Fuck Alexis[KoGa3AutoWTChange1]{size=-4}(KFM Fuck Alexis, KFM Marry Erynn, Alexis SP+2) {/size} {/color}":
                    $ KFM_Fuck_Alexis = True
                    $ KFM_Marry_Erynn = True
                    $ Alexis_SP += 2
                    scene 11_1993 with Dissolve(1)
                    mc "Fuck and marry..."
                    mc "{i}(I see Erynn more as a sister. It would be weird to fuck her. I guess I'll give Alexis a go.){/i}"
                    mc "{i}(That sounded so bad.){/i}"
                    mc "I think I'll fuck Alexis."
                    a "Uh... O-kay..."
                    scene 11_1994 with Dissolve(1)
                    mc "And marry Erynn."
                    er "Sure. I don't mind."
                    mc "{i}(It's also weird to marry your sister.){/i}"
                    mc "{i}(I should have thought a little longer about this and not have killed Iris.){/i}"
                    mc "{i}(Oh well... I'd have a pretty wife, at least.){/i}"
                "Fuck Erynn[KoGa3AutoWTChange1]{size=-4}(KFM Fuck Erynn, KFM Marry Alexis, Alexis SP+4) {/size} {/color}":
                    $ KFM_Fuck_Erynn = True
                    $ KFM_Marry_Alexis = True
                    $ Alexis_SP += 4
                    # Alexis_SP (12)
                    scene 11_1600 with Dissolve(1)
                    mc "{i}(Even though we're just friends. I wouldn't mind fucking her at least once.){/i}"
                    mc "I guess I'll fuck Erynn and marry Alexis."
                    er "Oh..."
    scene 11_1614 with Dissolve(1)
    mc "Alright. That was actually tough..."
    mc "Now it's your turn."
    mc "Let's hear your choices, Iris."
    ir "Sure."
    scene 11_1615 with Dissolve(1)
    ir "I'll kill Alexis!"
    mc "Wow. Right off the bat."
    er "That's unexpected. Why Lex?"
    ir "That way I won't have to share the dorm room anymore."
    a "Heh... Good to know. But if I'm not there you'll probably get a new roommate. And who knows what she'd be like..."
    mc "{i}(Catfight incoming.){/i}"
    scene 11_1616 with Dissolve(1)
    ir "I'll fuck Erynn. And marry [mc]!"
    er "Uh..."
    mc "Wanna explain those choices?"
    ir "Because... Reasons."
    mc "{i}(Reasons...){/i}"
    scene 11_1617 with Dissolve(1)
    mc "Next. Let's go with Alexis now."
    a "Kill Iris! Because reasons!"
    mc "Haha."
    mc "{i}(Round two!){/i}"
    mc "{i}(I'm so happy I picked first. This is only getting worse.){/i}"
    scene 11_1618 with Dissolve(1)
    a "Fuck and marry..."
    a "Hmm... Normally I wouldn't have sex with another woman but if I had to, I'd pick Erynn."
    a "So, I'll fuck Erynn and marry [mc]."
    mc "{i}(Marry, huh? Why was I hoping she'd pick me to fuck?){/i}"
    if KFM_Fuck_Erynn == True:
        scene 11_1619 with Dissolve(1)
        mc "Everyone wants to have sex with Erynn it seems."
        er "..."
        mc "{i}(She's blushing.){/i}"
        mc "{i}(I don't know if she's uncomfortable with that, or happy.){/i}"
    else:
        pass
    scene 11_1620 with Dissolve(1)
    mc "I'm actually curious now."
    mc "Here's a question."
    mc "Have you two ever kissed each other?"
    scene 11_1621 with Dissolve(1)
    a "..."
    er "..."
    mc "Holy shit! You have!"
    scene 11_1622 with Dissolve(1)
    mc "Was it just a peck on the lips or a full make-out sesh?"
    mc "Or more like a dare or something?"
    a "We're not telling you!"
    mc "Oh, come on!"
    a "No!"
    mc "{i}(I really want to know, now.){/i}"
    scene 11_1623 with Dissolve(1)
    mc "{i}(Damn...){/i}"
    mc "{i}(Just imagining it makes me hard.){/i}"
    scene 11_1624 with Dissolve(1)
    a "I can see you're thinking about it."
    mc "Well yeah..."
    mc "I'll get you or Erynn drunk one day and have you tell me the full story."
    er "Haha."
    scene 11_1625 with Dissolve(1)
    mc "Okay, okay. So you would kill Iris, fuck Erynn and marry me."
    a "Mm-hmm."
    mc "Erynn. Your turn."
    scene 11_1626 with Dissolve(1)
    er "Hmm... This is difficult."
    mc "Just kill me."
    er "No! I could never kill you!"
    scene 11_1627 with Dissolve(1)
    er "I'm so sorry, Iris! But I'll have to pick you."
    er "Lex is like a sister to me and..."
    ir "Haha, it's fine. I understand."
    mc "{i}(That must sting! You're breaking her heart, Erynn.){/i}"
    scene 11_1628 with Dissolve(1)
    er "And then..."
    er "I think I'll fuck Lexi and marry [mc]."
    mc "{i}(All three want to marry me...){/i}"
    mc "{i}(Why did no one pick me to fuck?){/i}"
    scene 11_1629 with Dissolve(1)
    er "This game is pretty stressful."
    a "Isn't it? Maybe we should've drunk some cocktails before playing."
    mc "Yeah. Would also be nice to know if any answers would change if you're drunk."
    scene black with Dissolve(1)
    pause 2
    scene 11_1630 with Dissolve(1)
    er "Mmm... I'm going in the water for a bit."
    a "I'll join you."
    ir "I'll stay here and tan a bit more."
    ir "I'm so pale compared to you guys. I need to catch up."
    scene 11_1631 with Dissolve(1)
    er "Are you coming?"
    mc "I'll keep Iris company."
    mc "Maybe later."
    er "Alright."
    scene 11_1632 with Dissolve(1)
    mc "Heh..."
    mc "You run like a girl!"
    er "I am a girl!"
    scene 11_1633 with Dissolve(1)
    ir "Come lie down next to me."
    mc "Sure."
    scene 11_1995 with Dissolve(1)
    ir "You've probably realised this already. But Erynn is trying to set you up with Alexis."
    mc "I know. Not the first time."
    mc "But so did you, when you were talking about your roommate."
    ir "I can't remember."
    mc "Haha. Bullshit."
    scene 11_1635 with Dissolve(1)
    ir "Honestly. You would look good together."
    ir "And I think she likes you. The way she looks at you sometimes..."
    mc "I don't think so."
    mc "Besides. That would complicate things, since I'm kinda seeing her sister."
    scene 11_1996 with Dissolve(1)
    ir "You're dating Layla?"
    mc "You know her?"
    ir "I've met her a couple of times when she's visited Alexis at the dorm."
    ir "But you're right. That surely would be complicated."
    scene 11_1638 with Dissolve(1)
    a "What do you think they're talking about?"
    er "I don't know."
    er "They dated for a while. So could be anything."
    scene 11_1997 with Dissolve(1)
    ir "So, Layla is your girlfriend?"
    mc "No. We're hanging out and we flirt and stuff."
    ir "Heh. And stuff..."
    scene 11_1639 with Dissolve(1)
    ir "Good! Or else you'd be cheating on me."
    mc "On you? How would I be cheating on you? We broke up months ago."
    ir "Did we?"
    scene 11_1640 with Dissolve(1)
    mc "What?"
    ir "Did we break up?"
    mc "Now you're confusing me."
    ir "It's fine. I'm just messing with you."
    mc "No... You're not messing with me. I know when you are. Tell me!"
    scene 11_1641 with Dissolve(1)
    ir "Last summer. When I told you I was moving away."
    ir "We talked about breaking up because of the whole long-distance thing and stuff."
    ir "But we never did. We never really said 'Hey, let's break up now' or officially ended it."
    ir "Summer went by, I moved away and that's about it."
    mc "Yeah. Now that I think about it, I guess we didn't."
    scene 11_1642 with Dissolve(1)
    mc "In that case. I hate to tell you, but I've cheated on you a lot!"
    ir "Haha. Really?"
    ir "I don't even know why I'm laughing."
    ir "I should be FURIOUS!"
    mc "Haha."
    scene 11_1643 with Dissolve(1)
    ir "How many?"
    mc "A few..."
    mc "And every girl from your school back in Alvarado."
    ir "Haha. Liar."
    ir "Actually. It could be true. There were lots of hoes in my class."
    mc "Haha."
    scene 11_1644 with Dissolve(1)
    ir "Remember Tiffany? I almost fought her because she couldn't keep her hands off you."
    ir "You didn't sleep with her, right?"
    mc "No."
    ir "Good! Because I wouldn't forgive you if you did."
    scene 11_1645 with Dissolve(1)
    ir "But really. How many?"
    mc "A few..."
    ir "[mc]... What's a few? Like five, ten?"
    mc "Yeah. Around that number."
    scene 11_1646 with Dissolve(1)
    ir "All in Alvarado?"
    mc "Some of them, yes."
    ir "Okay... Let me guess. Hmm..."
    scene 11_1647 with Dissolve(1)
    ir "Aaliyah?"
    mc "No."
    ir "Lakeyn?"
    if Lakeyn_FB_Sex == True:
        scene 11_1648 with Dissolve(1)
        mc "Yes!"
        ir "You had sex with Lakeyn? How did you manage that? Did she also do the tattoos on you?"
        mc "She did."
        ir "I always thought she was into girls. Hmm..."
        ir "Good on you. She's hot!"
    else:
        mc "Nope."
        ir "Did Nate? I remember he fancied her."
        mc "He didn't either."
    scene 11_1649 with Dissolve(1)
    ir "Hmm..."
    ir "Mira?"
    mc "..."
    ir "I knew it! I so knew it!"
    ir "But I can't blame you there. She's a cutie. And she always had a thing for you!"
    scene 11_1650 with Dissolve(1)
    er "Hey! Come join us now!"
    mc "Yeah, yeah. We're coming."
    scene 11_1651 with Dissolve(1)
    mc "This girl..."
    mc "Are you coming?"
    ir "I'll stay here. Go have fun!"
    ir "Give me a hug though."
    scene 11_1654 with Dissolve(1)
    mc "You sure you don't want to join us and play with Erynn in the water?"
    ir "..."
    mc "You've gotta step up your flirting game. Your previous attempts were pretty pathetic."
    scene 11_1655 with Dissolve(1)
    mc "'Maybe I'll grow it out again.'"
    ir "Hey!"
    mc "Haha."
    scene 11_1656 with Dissolve(1)
    er "Aren't you coming, Iris?"
    ir "I'll stay here and guard our stuff."
    er "Oh... Okay. Thanks!"
    scene 11_1657 with Dissolve(1)
    mc "She actually can't swim and she's too embarrassed to say anything."
    er "I didn't know that."
    a "Don't listen to him! She can swim just fine. I've been to the beach with her before."
    scene 11_1658 with Dissolve(1)
    er "[mc]!"
    er "You always do that!"
    mc "Haha."
    if Iris_Points >= 1:
        scene 11_1659 with Dissolve(1)
        ir "*Sigh*"
        ir "{i}(Fuck...){/i}"
    else:
        pass
    scene 11_1998 with Dissolve(1)
    mc "So, what do you want to do now?"
    er "I don't know..."
    mc "You wanted to go in the water!"
    er "Just to cool off a bit."
    scene 11_1999 with Dissolve(1)
    mc "We should've brought a ball or something."
    er "We can play volleyball a little later."
    er "They have balls at the bar which you can rent."
    mc "Good idea. Let's do that."
    if Erynn_Week2_Tuesday_Fly == True:
        scene 11_2000 with Dissolve(1)
        mc "I have another idea for now, though."
        er "Yeah?"
        mc "You always wanted to do that Dirty Dancing flying scene, right?"
        er "Uh, yeah... How do you know that?"
        scene 11_2001 with Dissolve(1)
        mc "Melissa mentioned it before and showed me a picture where she picked you up."
        er "Oh..."
        mc "Up for it?"
        er "I want to try."
        scene 11_1665 with Dissolve(1)
        a "I can't believe you've watched Dirty Dancing."
        mc "I haven't. I had to google it."
        a "Haha, okay."
        scene 11_1666 with Dissolve(1)
        mc "Where are you going?"
        er "I need some space to run towards you and..."
        mc "Because we've done this so many times already, right?"
        mc "Let's start here in the water first so I can figure out how to pick you up."
        if Erynn_Week5_Tuesday_Photoshoot_Join == True:
            scene 11_1667 with Dissolve(1)
            mc "{i}(This reminds me of the photo shoot again.){/i}"
            mc "{i}(She has such great boobs!){/i}"
        else:
            pass
        scene 11_1668 with Dissolve(1)
        er "How are we doing this?"
        mc "Hmm... I think I have to hold you on your hips so you can turn and balance once in the air."
        mc "Just jump and... We'll see, I guess."
        scene 11_1671 with Dissolve(1)
        mc "Alright. Alexis, can you move back a little."
        mc "If I drop Erynn, I don't want her to fall on you."
        er "Then don't drop me!"
        mc "We're in the water. It's not gonna hurt."
        scene 11_1672 with Dissolve(1)
        mc "Ready?"
        er "Uh-huh."
        mc "Jump on three!"
        mc "One... two... three..."
        scene 11_1673 with Dissolve(1)
        mc "JUMP!"
        er "Aaah!"
        scene 11_1674 with Dissolve(1)
        mc "{i}(This is harder than I thought.){/i}"
        mc "{i}(She isn't nearly as high up as she needs to be.){/i}"
        mc "{i}(Shit!){/i}"
        scene 11_1675 with vpunch
        ""
        scene 11_1676 with Dissolve(1)
        er "Aaah!"
        a "Be careful!"
        scene 11_1677 with Dissolve(1)
        a "Are you guys alright?"
        er "Haha, yeah."
        mc "Well, that was a fail."
        scene 11_1678 with Dissolve(1)
        er "Did I do something wrong, or...?"
        mc "I don't know. It's really difficult."
        mc "Maybe try to jump a little higher and I'll get a bit lower and push more with my legs."
        er "Or maybe you're not as strong as Patrick Swayze?"
        mc "..."
        scene 11_1679 with Dissolve(1)
        mc "The girl in the movie was tiny!"
        mc "You guys are much bigger."
        er "Much bigger..."
        mc "Bigger as in... I mean taller, okay? Dios mío..."
        mc "Let's just go again!"
        scene 11_1680 with Dissolve(1)
        er "..."
        a "..."
        scene 11_1681 with Dissolve(1)
        mc "And stop that talking without talking bullshit!"
        a "We were just looking at each other."
        mc "Yeah right!"
        er "Haha."
        scene 11_1682 with Dissolve(1)
        mc "Are you ready?"
        er "Uh-huh."
        mc "Jump as high as you can!"
        mc "In three... two... one..."
        scene 11_1683 with Dissolve(1)
        er "Aah..."
        a "Yes! That's it!"
        mc "Is it?"
        scene 11_1684 with Dissolve(1)
        a "Try to straighten your legs, Erynn."
        mc "Give me a second. I need to balance her first."
        scene 11_1686 with Dissolve(1)
        er "Oh no..."
        mc "Don't lean so far forward!"
        a "Be careful!"
        scene 11_1687 with Dissolve(1)
        er "[mc]!"
        mc "Shit!"
        scene 11_1688 with Dissolve(1)
        da "What the fuck are they doing?"
        tj "No idea. Looks fun though."
        da "Fun?"
        tj "Our girls are just lying here, doing nothing. They seem to be having fun at least."
        scene 11_1690 with Dissolve(1)
        da "Mm-mm-mm..."
        scene 11_1691 with Dissolve(1)
        va "Darryl!"
        da "Come on, babygirl. Get up!"
        va "Get off me!"
        to "Leave her alone, Darryl!"
        da "Are you jealous I'm not on top of you?"
        scene 11_1692 with Dissolve(1)
        da "*Whispers* You're so fucking sexy! I want you!"
        va "Seriously, Darryl! Get off!"
        da "Then let's do something other than just lying here."
        va "Fine..."
        scene 11_1693 with Dissolve(1)
        a "Are you guys okay?"
        er "Haha, yeah."
        a "It looked good for a moment."
        mc "Not bad for a second try, right? Take that Swayze!"
        scene 11_2002 with Dissolve(1)
        er "Your turn Lex!"
        a "No, no, I'm good."
        mc "You sure? I don't mind."
        er "It's a lot of fun!"
        a "It's okay. Really."
        scene 11_2003 with Dissolve(1)
        mc "Shall we head back?"
        a "Maybe Erynn wants another go."
        er "It's fine. We can try again later."
        er "Iris has been alone for a while now."
    else:
        scene 11_2003 with Dissolve(1)
        er "Let's go back."
        er "I don't like that Iris is there alone."
        mc "Alright."
    menu:
        "Pick the girls up[KoGa3AutoWTChange1]{size=-4}(Alexis SP+2) {/size} {/color}":
            $ Alexis_SP += 2
            # Alexis_SP (14)
            scene 11_2004 with vpunch
            mc "Let's go then!"
            a "Aaah..."
            a "[mc]! What are you doing?"
            scene 11_1699 with vpunch
            mc "And you too!"
            er "Haha..."
            scene 11_1700 with Dissolve(1)
            mc "What are you guys giggling about back there?"
            mc "Are you making out?"
            er "Who knows?"
            mc "At least let me look!"
            a "Haha."
            scene 11_1705 with Dissolve(1)
            mc "Look, Iris. I found two bongos in the ocean!"
            a "Bongos?"
            ir "Oh, I always wanted to try those."
            scene 11_1706 with Dissolve(1)
            ir "These are some nice bongos!"
            er "Hey!"
            ir "They don't make much sound though."
            mc "Hit them harder!"
            er "No!"
            mc "Haha."
        "Head back":
            pass
    scene black with Dissolve(1)
    pause 2
    scene 11_1707 with Dissolve(1)
    ir "Let me do your back for you, Erynn."
    er "Thank you."
    scene 11_2005 with Dissolve(1)
    er "[mc], can you help Lexi with her back?"
    a "You don't have to. I can wait until Erynn is finished."
    menu:
        "Help Alexis[KoGa3AutoWTChange1]{size=-4}(Alexis SP+2) {/size} {/color}":
            $ Alexis_SP += 2
            # Alexis_SP (16)
            mc "I don't mind, if you're okay with it."
            a "Uhm... Sure then, I guess. Thanks."
            scene 11_2006 with Dissolve(1)
            mc "{i}(Should I also sit on top of her? It makes it easier, right?){/i}"
            mc "{i}(I'm just gonna do it.){/i}"
            mc "{i}(If she doesn't want me to, she can just say so.){/i}"
            scene 11_2007 with Dissolve(1)
            a "..."
            mc "{i}(A few weeks ago, I was in the exact same position with Layla.){/i}"
            mc "{i}(She has a nice ass too.){/i}"
            mc "{i}(And I'm getting hard... Seriously. It's so easy to get turned on with these girls.){/i}"
            scene 11_1709 with Dissolve(1)
            ir "Here. You'll need this."
            mc "Uh... Yeah. Thanks."
            scene 11_1710 with Dissolve(1)
            er "..."
            a "*Shakes head*"
            scene 11_1711 with Dissolve(1)
            ir "Erynn. Can I loosen your top?"
            er "I'll take it off for a moment."
            ir "That works too."
            a "You can loosen mine too if it makes things easier."
            mc "Sure."
            scene 11_1712 with Dissolve(1)
            ir "Is this alright?"
            er "Mm-hmm. Feels nice."
            scene 11_1713 with Dissolve(1)
            mc "*Whispers* I see what you're doing."
            ir "*Whispers* I'm not doing anything!"
            ir "You have very soft skin, Erynn."
            er "Thanks."
            mc "*Whispers* Not doing anything...?"
            scene 11_1715 with Dissolve(1)
            mc "{i}(What the fuck is she doing now?){/i}"
            mc "{i}(Is she pretending to take Erynn doggy?){/i}"
            mc "{i}(This girl...){/i}"
            mc "{i}(Why is this turning me on, too?){/i}"
            scene 11_1716 with Dissolve(1)
            mc "{i}(That face...){/i}"
            mc "{i}(Iris...){/i}"
            scene 11_1717 with Dissolve(1)
            ir "*Whispers* Oh no..."
            ir "*Whispers* I just drooled on her."
            mc "Haha. I saw that. So disgusting."
            ir "Haha. It was an accident!"
            scene 11_1718 with Dissolve(1)
            a "What happened?"
            ir "Oh... Lexi's bitties."
            scene 11_2008 with Dissolve(1)
            mc "..."
            mc "{i}(This is now the second time I've seen them. But not this up close.){/i}"
            er "Uh, Lex..."
            scene 11_1719 with Dissolve(1)
            a "Why are you..."
            mc "Your..."
            scene 11_2009 with Dissolve(1)
            a "Ah..."
            scene 11_1721 with Dissolve(1)
            a "No-no-no-no-no... I can't believe that just happened!"
            a "Oh my god... Nooo... This is so embarrassing!"
            a "Can you please get off me?"
            mc "Sure."
            scene 11_1740 with Dissolve(1)
            er "You're red."
            a "I know!"
            ir "It's nothing to be ashamed about. They look great!"
            a "Can we please talk about something else now?"
        "Don't help":
            mc "Alright."
    scene black with Dissolve(1)
    pause 2
    scene 11_1741 with Dissolve(1)
    mc "How about we go play some volleyball now?"
    er "Yeah, we can do that."
    scene black with Dissolve(1)
    pause 2
    scene 11_1742 with Dissolve(1)
    mc "So... How are we gonna do this?"
    mc "Do we play against each other or should we look for four more people?"
    er "Just two versus two, no?"
    mc "That's fine. Teams then."
    scene 11_2010 with Dissolve(1)
    er "I'll play with Iris. [mc], you're on Lexi's team."
    a "..."
    mc "Sounds good to me."
    er "First to twenty-one wins."
    scene 11_2011 with Dissolve(1)
    mc "I'll get us a ball."
    er "Thanks."
    ir "Wait! I'll come with you. I need to use the bathroom."
    scene 11_2012 with Dissolve(1)
    ir "Hey, [mc]."
    mc "Hmm?"
    ir "Do me a favour and don't go all out. Give us a little bit of a chance."
    mc "I should be asking you."
    ir "What?"
    scene 11_2013 with Dissolve(1)
    mc "Erynn played volleyball in high school."
    ir "She did?"
    ir "So, I'm going to win against you, then?"
    mc "I wouldn't go that far."
    scene 11_2014 with Dissolve(1)
    ir "Haha. We'll see. Feeling much better all of a sudden."
    mc "Heh..."
    if Iris_Points >= 1:
        ir "We should've made a bet."
        mc "And what would you want if you win?"
        ir "You!"
        mc "..."
    else:
        pass
    scene 11_2015 with Dissolve(1)
    er "This is going to be fun! You and [mc] on the same team."
    a "..."
    er "What's up with you?"
    er "Why are you looking at me like that?"
    scene 11_2016 with Dissolve(1)
    a "Can you stop?"
    er "Stop what?"
    a "You know what I'm talking about, Erynn."
    er "Aren't you interested in him?"
    scene 11_2017 with Dissolve(1)
    a "He's with Layla!"
    er "Aren't they just friends?"
    a "Erynn... They wouldn't have been in the hot tub together if they were just friends."
    er "Did Layla say anything?"
    a "She likes him. So, he's off limits."
    scene 11_2018 with Dissolve(1)
    if KFM_Fuck_Alexis == True:
        er "But he even picked to fuck you."
        a "It was just a game. He had to pick someone."
    else:
        if KFM_Marry_Alexis == True:
            er "But he even picked to marry you."
            a "It was just a game. He had to pick someone."
        else:
            pass
    er "You guys would be so good together though."
    a "*Sigh* Erynn..."
    scene 11_2019 with Dissolve(1)
    er "You're right. I'll stop."
    er "I'm sorry."
    er "If I knew he and Layla were that serious, I wouldn't have pushed this."
    a "It's fine."
    scene black with Dissolve(1)
    pause 2
    scene 11_2020 with Dissolve(1)
    mc "Here you go. You can start."
    ir "Thanks."
    er "Good luck!"
    mc "Yeah, you too."
    scene 11_2021 with Dissolve(1)
    mc "{i}(Is she upset about something?){/i}"
    mc "You alright?"
    a "Yeah, why?"
    mc "You didn't look happy when Erynn said I was on your team before."
    mc "If you want to team up with someone else, we can still switch. No worries."
    scene 11_2022 with Dissolve(1)
    a "No! It wasn't about that. I'm sorry."
    a "I'm fine playing with you."
    mc "{i}(I guess I was overthinking again.){/i}"
    scene 11_2023 with Dissolve(1)
    a "Let's go beat them!"
    mc "Hell yeah! I like your attitude."
    scene 11_2024 with Dissolve(1)
    er "Go, Iris!"
    mc "{i}(Wait...){/i}"
    mc "{i}(Is she seriously doing on overhead serve?){/i}"
    mc "{i}(Does she know how to play volleyball?){/i}"
    scene 11_2025 with Dissolve(1)
    ir "Ahh..."
    er "You okay? Are you hurt?"
    ir "I'm good, I'm good. I just, I don't know."
    mc "{i}(Okay. That's what I expected to happen.){/i}"
    scene 11_2026 with Dissolve(1)
    er "Let her go again!"
    ir "Yes! That one doesn't count! It was just a warm-up!"
    mc "Sure. Go ahead."
    scene 11_2027 with Dissolve(1)
    er "I'll help you."
    ir "..."
    scene 11_2028 with Dissolve(1)
    mc "Haha. That didn't change much!"
    ir "Stop laughing!"
    er "Don't listen to him. You did great."
    mc "Yeah. Really great! Keep doing exactly this, Iris."
    ir "Shut up!"
    scene 11_2029 with Dissolve(1)
    mc "One-zip!"
    ir "Yeah, yeah. Just serve already!"
    scene 11_1760 with Dissolve(1)
    mc "{i}(I'm just going to serve to Iris all the time.){/i}"
    mc "{i}(This game will be done in five minutes.){/i}"
    scene 11_2030 with Dissolve(1)
    mc "{i}(Fuck me! Of course this happens now.){/i}"
    ir "Haha. That's what you get! ONE-ONE!"
    ir "Maybe you should try the underhand serve next time!"
    mc "..."
    mc "{i}(That was actually funny.){/i}"
    scene 11_2031 with Dissolve(1)
    mc "{i}(She's looking serious!){/i}"
    scene 11_1772 with vpunch
    mc "{i}(What the fuck...){/i}"
    mc "{i}(How is this ball so fast?){/i}"
    scene 11_2032 with Dissolve(1)
    ir "That was amazing, Erynn!"
    er "Thanks."
    scene 11_2033 with Dissolve(1)
    ir "Two-one!"
    mc "We know..."
    mc "{i}(I was just caught off guard. Concentrate!){/i}"
    mc "{i}(That won't happen again.){/i}"
    scene 11_2034 with Dissolve(1)
    a "I've got it."
    mc "I've got this one."
    scene 11_2035 with vpunch
    a "Ahhh..."
    scene 11_2036 with Dissolve(1)
    mc "..."
    scene 11_2037 with Dissolve(1)
    er "Are you guys alright? That looked painful."
    mc "Sorry. Are you okay?"
    a "I am. We're good, Erynn."
    scene 11_2038 with Dissolve(1)
    mc "I'll help you up."
    a "Thanks."
    mc "{i}(Man... We are so fucked!){/i}"
    ir "Three-one."
    mc "Yeah... Thanks, Iris. Kick us when we're down. Literally!"
    scene 11_2039 with Dissolve(1)
    a "Let me take Erynn's serve."
    mc "You sure? It's really fast and..."
    a "I'm sure."
    mc "Okay. You can give it a go."
    mc "{i}(The only point we're gonna have is the failed serve from Iris. How embarrassing!){/i}"
    mc "{i}(And here I thought this game would be over quick. Well, it will be. But us losing instead of winning.){/i}"
    scene 11_2040 with Dissolve(1)
    er "Can we continue or do you need a minute?"
    a "Just serve!"
    er "Heh..."
    mc "{i}(Now she's getting pissed too.){/i}"
    mc "{i}(We're doomed.){/i}"
    scene 11_2041 with Dissolve(1)
    mc "Oh..."
    mc "Nice, Alexis!"
    mc "{i}(She actually did it.){/i}"
    scene 11_2042 with Dissolve(1)
    mc "Here you go!"
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 11_2043 at moveup
    pause 3
    mc "{i}(What...?){/i}"
    scene 11_2044 with Dissolve(1)
    mc "{i}(What's going on?){/i}"
    mc "{i}(Did she play volleyball too?){/i}"
    scene 11_2045 with Dissolve(1)
    ir "Aaah..."
    er "..."
    scene 11_2046 with Dissolve(1)
    a "I'm sorry, Iris."
    ir "I'm fine. I didn't expect the ball to come at me so fast! That was scary for a second!"
    er "Is that how we're gonna play?"
    a "What?"
    er "Let's bring it then. It's on!"
    mc "{i}(Ooh... The tension. I love me some competition. But I hope this won't turn into drama.){/i}"
    scene 11_2047 with Dissolve(1)
    mc "Where did that come from? Did you also play volleyball?"
    a "Yeah. I played together with Erynn in high school."
    mc "I didn't know that. That was impressive!"
    a "Thanks."
    mc "{i}(This also changes things. We might actually have a chance now.){/i}"
    scene black with Dissolve(1)
    pause 2
    scene 11_2048 with Dissolve(1)
    a "Play it to the net!"
    mc "Okay."
    scene 11_2049 with Dissolve(1)
    ir "Aaah!"
    scene 11_2050 with Dissolve(1)
    a "..."
    scene 11_2051 with Dissolve(1)
    er "Not this time..."
    scene 11_2052 with Dissolve(1)
    a "Good job!"
    mc "You too."
    scene black with Dissolve(1)
    pause 2
    scene 11_2053 with Dissolve(1)
    mc "Shit!"
    scene 11_2054 with Dissolve(1)
    er "..."
    scene 11_2055 with Dissolve(1)
    a "Fuck..."
    scene black with Dissolve(1)
    pause 2
    scene 11_2056 with Dissolve(1)
    mc "Twenty-fourteen!"
    mc "Alright, Alexis. Match point. Let's do this."
    scene 11_2057 with Dissolve(1)
    mc "{i}(She looks exhausted.){/i}"
    mc "{i}(Even though we smashed all the balls towards Iris to get easy points...){/i}"
    mc "{i}(I can't believe she managed to score fourteen against us. I had no idea she was this good.){/i}"
    mc "{i}(She really meant it when she said let's bring it.){/i}"
    scene 11_2058 with Dissolve(1)
    a "Not this time, Erynn!"
    er "..."
    scene 11_2059 with Dissolve(1)
    mc "That's game!"
    a "We did it!"
    scene 11_2060 with vpunch
    a "Aaah..."
    mc "Haha."
    if Alexis_SP >= 13:
        scene 11_2061 with Dissolve(1)
        mc "You were amazing, Alexis!"
        a "{i}('You guys would be so good together though.'){/i}"
        a "{i}(Dammit, Erynn...){/i}"
    else:
        mc "You were amazing, Alexis!"
    scene 11_2062 with Dissolve(1)
    ir "I'm so sorry, Erynn."
    ir "We lost because of me."
    er "Don't say that. You did great!"
    scene 11_2063 with Dissolve(1)
    er "Hey. Congrats guys!"
    a "Thanks."
    scene 11_2064 with Dissolve(1)
    mc "You were great too, Erynn!"
    a "I agree."
    er "Thank you."
    mc "I didn't know you were that good."
    ir "What about me?"
    scene 11_2065 with Dissolve(1)
    mc "Well... Hmm..."
    mc "You tried!"
    ir "..."
    mc "Haha. Don't look like that. I'm just being honest."
    er "No, you did well, Iris!"
    scene 11_2066 with Dissolve(1)
    mc "Now I wish I could've seen you play a game in high school. That must have been something."
    er "Lexi might have some videos."
    a "Yeah. We have a few at home."
    mc "You do? If we do this again. Please bring them if possible."
    a "Sure. Remind me of it then."
    scene 11_2067 with Dissolve(1)
    mc "You know what you two should do? Sign up for those beach volleyball tournaments in the summer."
    mc "Do they still do those?"
    er "They do. Every weekend in August."
    mc "Go sign up then. You might actually have a chance."
    scene 11_2068 with Dissolve(1)
    a "Yeah. Maybe."
    er "We'll think about it."
    mc "You'll have at least two supporters here already."
    scene 11_2069 with Dissolve(1)
    mc "How did you actually become friends?"
    a "Who? Iris and I? Or do you mean me and Erynn?"
    mc "Iris and you I know. Probably because you're sharing a dorm."
    mc "Yeah, I meant you and Erynn."
    scene 11_2070 with Dissolve(1)
    er "It was the first day at elementary school."
    mc "First day? So, you saw each other and thought, hey, you're pretty, I'm pretty, let's be friends?"
    a "Haha."
    er "Haha, no."
    scene 11_2071 with Dissolve(1)
    er "The desks were arranged by name."
    er "And because of our names, Monroe and Orlandi, we were sat next to each other."
    mc "And then you said, you're pretty, I'm pretty, let's..."
    er "Haha. No... We just started talking and yeah, became friends, I guess."
    scene 11_2072 with Dissolve(1)
    mc "If I had been in your class. I would've been sitting between you two."
    er "You're right. Moreno... We'd be neighbours either way."
    mc "Heh, yeah."
    scene 11_2073 with Dissolve(1)
    er "I have a question. Maybe it's not the right time to ask you this, but..."
    mc "No. Go ahead."
    er "Okay, uhm... Do you still go by Moreno? Because of Andres... You know..."
    scene 11_2074 with Dissolve(1)
    mc "Hmm... I haven't thought about that yet. I should change it though."
    er "What does it say on your ID?"
    mc "I have both on my ID. Vicari-Moreno."
    mc "But I always went with Moreno since everyone I knew used their dad's last name."
    er "Except for me."
    mc "Haha. You're right. Except for you."
    scene 11_2075 with Dissolve(1)
    ir "So, your actual name is Vicari?"
    mc "It is."
    ir "After all this time, I still learn new things about you."
    scene 11_2076 with Dissolve(1)
    ir "What's your bio-dad's last name?"
    mc "I don't know. I've never asked Mom about that."
    mc "Maybe I should change my name to his name. But only if it's something cool like Valentine... Or Montana."
    mc "Or an animal name like Fox, Raven or Wolf. I don't know."
    scene 11_2077 with Dissolve(1)
    er "Or just wait to change it until you're married and then take the name of your future wife."
    mc "That's also an option."
    mc "But she needs to have a cool name, too."
    scene 11_2078 with Dissolve(1)
    ir "Who did you pick again to marry when we played Kill-Fuck-Marry?"
    if KFM_Marry_Alexis == True:
        mc "Lexi."
        mc "So, I would be [mc] Monroe."
        mc "Yeah... I can live with that."
        a "..."
    else:
        if KFM_Marry_Erynn == True:
            mc "Erynn."
            mc "So, I would be [mc] Orlandi."
        else:
            mc "You."
            mc "So, I would be [mc] Vančura."
        mc "Yeah... I can live with that."
    scene black with Dissolve(1)
    pause 2
    scene 11_2079 with Dissolve(1)
    mc "Nggh... I'm getting a little hungry."
    a "Shall we head home then? We've been here for quite a few hours now."
    er "Yeah. I think it's been long enough."
    scene 11_2080 with Dissolve(1)
    er "We'll be right back."
    mc "Take your time. I'll wait here."
    scene 11_2081 with Dissolve(1)
    mc "{i}(This was a fun day!){/i}"
    if Iris_Points >= 1:
        scene 11_1828 with Dissolve(1)
        mc "{i}(Spending some time with Iris again, I feel there's still so much there.){/i}"
        mc "{i}(It's just easy and so much fun. Or is this just familiarity?){/i}"
        mc "{i}(Maybe I should...?){/i}"
        menu:
            "Join Iris[KoGa3AutoWTChange1]{size=-4}(Iris Week5 Wednesday Beach Sex) {/size} {/color}":
                $ Iris_Week5_Wednesday_Beach_Sex = True
                jump Week5_Wednesday_Beach_Sex_Iris
            "Wait here":
                mc "{i}(No... I shouldn't. I'll just wait here.){/i}"
                jump Week5_Wednesday_Beach_End_SP
    else:
        jump Week5_Wednesday_Beach_End_SP

label Week5_Wednesday_Beach_Sex_Iris:
    if _in_replay:
        $ SexCounter_Iris = 2
        $ MC_SexCounter = 2
    $ SexCounter_Iris += 1
    $ MC_SexCounter += 1
    scene 11_1832 with Dissolve(1)
    n "*Knock-knock*"
    scene 11_1889 with Dissolve(1)
    ir "Hey..."
    mc "Hi."
    ir "Did you need something, or...?"
    mc "No, I..."
    scene 11_1890 with Dissolve(1)
    ir "Get in!"
    mc "Uh..."
    scene 11_1891 with Dissolve(1)
    ir "..."
    mc "*Sigh*"
    ir "You okay?"
    mc "Mm-hmm."
    scene 11_2082 with Dissolve(1)
    ir "You know I didn't win, right?"
    mc "What?"
    ir "Volleyball..."
    mc "Yeah, and? Oh... You mean the bet."
    ir "*Nods*"
    scene 11_2083 with Dissolve(1)
    ir "..."
    mc "..."
    scene 11_2084 with Dissolve(1)
    ""
    scene 11_2085 with Dissolve(1)
    mc "{i}(This feels right!){/i}"
    scene 11_2086 with Dissolve(1)
    ir "..."
    scene 11_2087 with Dissolve(1)
    ir "Mmm..."
    ir "[mc]..."
    scene 11_2088 with Dissolve(1)
    ir "You sure you want to do this?"
    mc "*Nods*"
    mc "Do you?"
    ir "Do you even have to ask?"
    scene 11_2089 with Dissolve(1)
    mc "I remember these!"
    ir "I hope you remember what to do with them."
    mc "Trust me. I do!"
    scene 11_2090 with Dissolve(1)
    ir "Ahh..."
    scene 11_2091 with Dissolve(1)
    mc "{i}(How much I missed them!){/i}"
    mc "{i}(She has such great boobs!){/i}"
    scene 11_2092 with Dissolve(1)
    ""
    scene 11_2093 with Dissolve(1)
    mc "{i}(And not just great boobs.){/i}"
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 11_2094 at moveup
    pause 3
    mc "I thought I'd never see this again."
    ir "Any time you want!"
    mc "Fuck you are beautiful!"
    scene 11_2095 with vpunch
    mc "..."
    scene 11_2096 with Dissolve(1)
    mc "Do you have any idea how much you turn me on."
    ir "Let me help you then."
    scene 11_2097 with vpunch
    ir "Ah-haha..."
    ir "Look at you. Being so rough."
    mc "Sorry. Can't help it."
    scene 11_2098 with Dissolve(1)
    mc "..."
    scene 11_2099 with Dissolve(1)
    ""
    scene 11_2100 with Dissolve(1)
    ir "Still fits perfectly!"
    mc "Haha."
    show 11_2101
    ir "*Moaning*"
    show 11_2102
    ir "Ahh..."
    ir "[mc]..."
    show 11_2103
    ""
    scene 11_2104 with vpunch
    ir "Ahh..."
    mc "Sorry. Didn't mean to..."
    ir "Haha. No, it's fine. Just don't break the cabin."
    mc "I try my best."
    show 11_2105
    ""
    show 11_2106
    mc "{i}(This feels so good!){/i}"
    scene 11_2107 with Dissolve(1)
    mc "Why are you looking at me so intensely?"
    ir "I love watching you while you fuck me!"
    mc "Heh..."
    show 11_2108
    mc "I love fucking you!"
    scene 11_2109 with vpunch
    pause 2
    scene 11_2110 with vpunch
    ir "Ahhh..."
    scene 11_2111 with Dissolve(1)
    mc "*Heavy breathing*"
    ir "You learned some new things, huh?"
    ir "I'm a little jealous!"
    mc "Heh..."
    mc "This was amazing!"
    scene 11_2112 with Dissolve(1)
    ir "..."
    mc "..."
    scene 11_2113 with Dissolve(1)
    ir "[mc], I..."
    mc "What?"
    ir "Never mind."
    scene 11_2114 with Dissolve(1)
    ir "I'd better start changing now."
    mc "Yeah. I'll wait outside."
    ir "Don't tell anyone what we did. Especially Erynn."
    mc "..."
    mc "I won't."
    scene 11_2115 with Dissolve(1)
    ir "Thanks!"
    scene 11_2116 with Dissolve(1)
    mc "{i}(That just ended... on a weird note...){/i}"
    scene 11_2117 with Dissolve(1)
    ir "..."
    $ renpy.end_replay()
    jump Week5_Wednesday_Beach_End_SP

label Week5_Wednesday_Beach_End_SP:
    scene black with Dissolve(1)
    pause 2
    scene 11_2118 with Dissolve(1)
    mc "Everyone ready?"
    er "Yes!"
    mc "Let's go, then."
    scene 11_2119 with Dissolve(1)
    a "Do you want me to drop you off at home or the dorm?"
    ir "I'll head home but you don't have to drive me. I'll take the bus."
    a "No, no. It's fine. It's much quicker too."
    ir "Thanks."
    scene 11_1908 with Dissolve(1)
    ir "Nggh..."
    mc "Someone's tired."
    ir "A little."
    ir "Just gonna have a little nap."
    mc "A nap doesn't sound that bad."
    scene 11_1911 with Dissolve(1)
    if Iris_Week5_Wednesday_Beach_Sex == False:
        ir "I'm probably gonna be sore tomorrow. That volleyball game was the first physical activity I've had in months."
        mc "Most of the time you just stood there."
        ir "I tried!"
    else:
        ir "I'm probably gonna be sore tomorrow. That volleyball game was the first physical activity I've had in months."
        mc "Quickly followed by the second."
        ir "What?"
        scene 11_1912 with Dissolve(1)
        mc "*Whispers* You had a second physical activity!"
        ir "*Whispers* Oh yeah, that's right!"
    scene black with Dissolve(1)
    pause 2
    stop music fadeout 1.0
    play music ("Music/LoFi Indie 3.mp3", "Music/LoFi Indie 1.mp3", "Music/LoFi Indie 2.mp3") volume 0.2
    scene 11_2120 with Dissolve(1)
    ""
    scene 11_2121 with Dissolve(1)
    er "That was a fun day. We definitely should do this again."
    er "Thanks for driving, Lexi!"
    a "You're welcome."
    scene 11_2122 with Dissolve(1)
    mc "Yeah. Thanks for driving and picking me up, Alexis."
    a "No worries."
    mc "And thank you for helping me beat Erynn at volleyball."
    mc "Well... Not helping. You basically did everything."
    a "Haha. You did great too!"
    scene 11_2123 with Dissolve(1)
    er "But let's switch teams next time. Alexis and I versus you and..."
    mc "Versus me and Iris? Someone wants to win so badly!"
    mc "That game probably lasts five minutes and ends twenty-one to nil."
    mc "Maybe twenty-one to one. We'll probably find a way to score one point."
    er "Haha."
    scene 11_2124 with Dissolve(1)
    er "You can have an extra player."
    mc "And who will that be?"
    er "I don't know. You go to a sports school. You probably have at least one friend who is on the volleyball team."
    mc "..."
    mc "{i}(You totally overestimate how many friends I have.){/i}"
    scene 11_2125 with Dissolve(1)
    mc "Anyway. I'm heading home."
    mc "Thanks again for inviting me."
    er "You're welcome."
    scene 11_2126 with Dissolve(1)
    mc "See you later, Erynn."
    er "Bye, [mc]."
    menu:
        "Hug Alexis[KoGa3AutoWTChange1]{size=-4}(Alexis SP+2) {/size} {/color}":
            $ Alexis_SP += 2
            # Alexis_SP (18)
            scene 11_2127 with Dissolve(1)
            mc "Bye, Alexis. See you next time."
            a "Yeah. See ya."
            scene 11_2129 with Dissolve(1)
            mc "Bye, girls."
            er "Bye-bye."
        "Kiss Alexis[KoGa3AutoWTChange1]{size=-4}(Alexis SP+4) {/size} {/color}":
            $ Alexis_SP += 4
            # Alexis_SP (20)
            scene 11_2128 with Dissolve(1)
            mc "Bye, Alexis. See you next time."
            a "Yeah. See ya."
            scene 11_2129 with Dissolve(1)
            mc "Bye, girls."
            er "Bye-bye."
            scene 11_2129a with Dissolve(1)
            er "..."
            a "Stop."
            er "You look happy though."
        "Go home":
            scene 11_2129 with Dissolve(1)
            mc "Bye, Alexis. See you next time."
            a "Yeah. See ya."
    jump Week5_Wednesday_Layla_Date

label Week5_Wednesday_Club_Alexis:
    scene black with Dissolve(1)
    pause 2
    scene 11_2130 with Dissolve(1)
    mc "{i}(What time is it now?){/i}"
    mc "{i}(Five minutes before eight.){/i}"
    mc "{i}(I'd better wait outside or she'll be mad again...){/i}"
    scene 11_2131 with Dissolve(1)
    n "*Ding-dong*"
    mc "{i}(Wait... Is that her already?){/i}"
    mc "{i}(She's early. Can't be.){/i}"
    scene 11_2132 with Dissolve(1)
    mc "Uh..."
    a "Hey. Ready?"
    mc "I was going to wait outside, but you're early!"
    a "Hehe. It's fine."
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 11_2133 at moveup
    pause 3
    mc "{i}(Damn...){/i}"
    mc "{i}(I like the way she dresses when we go out.){/i}"
    scene 11_2134 with Dissolve(1)
    mc "You don't wear skirts often, but when you do..."
    mc "You look hot!"
    a "Thanks."
    scene 11_2135 with Dissolve(1)
    mc "And how high are those heels?"
    mc "You're just as tall as me, now."
    a "Too much?"
    mc "No, I like it."
    scene 11_2136 with Dissolve(1)
    ""
    scene 11_2137 with Dissolve(1)
    a "Hmm..."
    mc "What's with that disapproving look?"
    a "*Sigh* It's the hat."
    mc "What about it?"
    a "You kinda look like a douchebag."
    scene 11_2151 with Dissolve(1)
    mc "Haha. So, I'm a douchebag?"
    a "What? No!"
    a "I'm not saying you're a douchebag. The hat... *Sigh* I don't like the hat."
    scene black with Dissolve(1)
    pause 2
    scene 11_2147 with Dissolve(1)
    mc "{i}(It's not too bad, right?){/i}"
    mc "{i}(Or should I wear it normally?){/i}"
    scene 11_2148 with Dissolve(1)
    mc "Mom! Question."
    mc "What do you think about the hat?"
    m "If you like it, wear it."
    scene 11_2149 with Dissolve(1)
    mc "No, seriously. How do I look? And be honest!"
    m "..."
    m "A little douchebaggy? Is that a word? Sorry."
    m "But maybe that's because you're wearing it backwards?"
    scene 11_2150 with Dissolve(1)
    mc "Thanks a lot..."
    m "Oh, come on! You wanted an honest answer."
    mc "..."
    scene black with Dissolve(1)
    pause 2
    scene 11_2152 with Dissolve(1)
    mc "{i}(I guess Mom was right...){/i}"
    mc "Hey!"
    a "Can I please take it off?"
    mc "*Sigh* Fine..."
    scene 11_2153 with Dissolve(1)
    mc "Lexi!"
    a "Haha. I'm just fixing your hair."
    scene 11_2154 with Dissolve(1)
    a "Heh. So much better!"
    a "Look at this handsome boy!"
    mc "*Shakes head*"
    scene 11_2155 with Dissolve(1)
    mc "..."
    scene 11_2156 with Dissolve(1)
    a "Let's go."
    scene 11_2157 with Dissolve(1)
    mc "Nice of your dad to let you borrow his car for the whole day."
    a "He isn't here, so he doesn't need it today."
    mc "You did actually ask him, right?"
    a "Haha. Yes!"
    scene 11_2158 with Dissolve(1)
    mc "By the way. There are some holes in your fishnet thingies."
    a "Don't pull them. They're supposed to be there."
    mc "They're supposed to be torn?"
    a "Yeah..."
    mc "Why would you buy torn clothes?"
    scene 11_2159 with Dissolve(1)
    a "You've never seen those t-shirts with 'bullet holes' in them?"
    a "Or ripped jeans? You even have a pair."
    mc "Right. It just... Never mind."
    a "Haha."
    scene black with Dissolve(2)
    pause 2
    scene 11_2160 with Dissolve(1)
    a "There she is."
    mc "{i}(Of course, she's surrounded by guys.){/i}"
    mc "{i}(It was always that way when we went out.){/i}"
    scene 11_2161 with Dissolve(1)
    ir "Hey!"
    ir "Sorry, guys. Gotta go. My dates are here!"
    x "What?"
    scene 11_2162 with Dissolve(1)
    mc "Hi again, Iris."
    ir "Hey. You guys look amazing!"
    a "Thank you. So do you!"
    ir "Thanks."
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 11_2163 at moveup
    pause 3
    mc "..."
    mc "{i}(Wow... That just gave me a flashback.){/i}"
    scene 11_2164 with Dissolve(1)
    ir "I'm taking this side for today if you don't mind, Alexis."
    a "It's fine. But just for today."
    a "And within boundaries!"
    mc "{i}(Iris and boundaries. You should know better by now, Lexi.){/i}"
    scene black with Dissolve(1)
    pause 2
    scene 11_2165 with Dissolve(1)
    mc "Oh man..."
    mc "It's early and there's already a line? On a Wednesday?"
    a "Spring break..."
    scene 11_2166 with Dissolve(1)
    mc "Want to go somewhere else?"
    a "I really wanted to go to Heaven, but if you..."
    mc "No, it's fine. We'll just have to wait a bit then."
    ir "..."
    scene 11_2167 with Dissolve(1)
    mc "Where are you going?"
    ir "I'm not going to wait in line to get into a club."
    ir "Follow me!"
    mc "Uh..."
    scene 11_2168 with Dissolve(1)
    mc "{i}(There's no way!){/i}"
    scene 11_2169 with Dissolve(1)
    ir "Come on. We can go in."
    mc "{i}(How? Every freaking time!){/i}"
    a "What did she say to him?"
    mc "I have no idea, but somehow she always gets what she wants."
    scene 11_2170 with Dissolve(1)
    x "Seriously?? We've been waiting here for over thirty minutes..."
    x "It's always the same. The shorter the skirt the faster you'll get in!"
    x "ID please!"
    play music ("Music/Kyroflux - Circuit Breaker.mp3", "Music/Kyroflux - After Hours.mp3", "Music/Kyroflux - Drop the Night.mp3", "Music/Kyroflux - Starlight.mp3") volume 0.4
    # Copyright NyxVN
    scene 11_2171 with Dissolve(1)
    a "We even got a booth. If we had to wait in line, this surely would've been taken by the time we got in."
    a "Thanks for getting us in this quickly, Iris. What did you say to him?"
    ir "We just talked."
    mc "{i}(Just talked... Yeah fucking right!){/i}"
    a "Really?"
    scene 11_2172 with Dissolve(1)
    a "Come, sit down. Plenty of space."
    mc "I'll get us some drinks first."
    ir "Should we do cocktails?"
    mc "Why not."
    scene 11_2173 with Dissolve(1)
    mc "What do you want?"
    ir "I'll take a mojito."
    a "Just a water for me."
    mc "Water? Don't you want to drink?"
    scene 11_2174 with Dissolve(1)
    a "I want to, but I'm driving. So, no alcohol."
    mc "You can always do an alcohol-free cocktail or something."
    a "Yeah, I'll do that then. Just pick something for me."
    mc "Or... If you trust me with your dad's car. I'll drive and you can drink."
    a "Uhm..."
    scene 11_2175 with Dissolve(1)
    mc "I'm gonna go run tomorrow morning, so I wasn't planning on drinking anyway."
    mc "{i}(And I really want to drive that car!){/i}"
    a "You sure?"
    mc "Uh-huh."
    a "Okay. Make it two mojitos then."
    scene 11_2176 with Dissolve(1)
    mc "*Sigh*"
    mc "{i}(We skipped the line outside, but now I'm gonna be stuck in this one for a while...){/i}"
    scene 11_2177 with vpunch
    mc "{i}(For fuck's sake! Why is everyone pushing here?){/i}"
    mc "{i}(It won't be any faster!){/i}"
    scene 11_2178 with vpunch
    mc "..."
    x "Ahh..."
    mc "Hey! Stop pushing already!"
    if Gabi_End == True:
        scene 11_2179 with Dissolve(1)
        tr "Can you be a little more careful? People are sitting here!"
        mc "{i}(Oh... It's Gabi.){/i}"
        mc "Sorry. I got pushed."
        scene 11_2181 with Dissolve(1)
        mc "{i}(Kinda weird seeing your teacher in a club.){/i}"
        x "What can I get you?"
        mc "Two mojitos and an alcohol-free beer."
    else:
        scene 11_2180 with Dissolve(1)
        tr "Can you be a little more..."
        tr "[mc]..."
        mc "{i}(Gabi...){/i}"
        scene black with Dissolve(1)
        transform moveup:
            xalign 0.5 yalign 1.0
            linear 5.0 yalign 0.0
        show 11_2182 at moveup
        pause 3
        mc "Hola, Gabi."
        tr "Heh. Hola."
        mc "Sorry, I got pushed and..."
        tr "Está bien."
        scene 11_2183 with Dissolve(1)
        mc "{i}(Damn, she's looking so good again.){/i}"
        mc "{i}(I want to kiss her so bad.){/i}"
        menu:
            "Kiss her":
                scene 11_2184 with Dissolve(1)
                tr "What are you doing?"
                mc "I wanted to kiss your cheek."
                tr "Not gonna happen!"
                mc "{i}(Yeah, she's right. What was I thinking? If Alexis saw...){/i}"
                mc "{i}(Not just Alexis. Anyone who knows we're teacher and student.){/i}"
                scene 11_2185 with Dissolve(1)
                mc "Sorry."
                tr "..."
                mc "I like the dress. Estás hermosa!\n(You look beautiful!)"
                tr "Gracias."
            "Don't":
                mc "{i}(But I'd better not.){/i}"
                scene 11_2185 with Dissolve(1)
                mc "I like the dress. Estás hermosa!\n(You look beautiful!)"
                tr "Gracias."
        scene 11_2186 with Dissolve(1)
        mc "Are you here alone?"
        tr "Why would I be alone at a club?"
        mc "This is kinda how we met. Both drinking alone in a bar."
        tr "..."
        scene 11_2187 with Dissolve(1)
        tr "No, I'm here with a friend."
        mc "A friend?"
        mc "{i}(Why am I sounding so jealous? We aren't even...){/i}"
        mc "Where..."
        x "What can I get you?"
        scene 11_2188 with Dissolve(1)
        mc "Uh..."
        mc "{i}(Shit. What did they want again? Mojito?){/i}"
        mc "Two mojitos and an alcohol-free beer."
        scene 11_2189 with Dissolve(1)
        mc "Do you want something?"
        tr "..."
        tr "A cosmo."
        mc "And a cosmo, please."
        tr "Thank you!"
        scene 11_2190 with Dissolve(1)
        tr "Who are you here with?"
        mc "Friends!"
        tr "Hmm..."
        mc "{i}(Could it be that she's a little jealous too?){/i}"
        scene 11_2191 with Dissolve(1)
        mc "*Whispers* But I'd prefer to be spending time with you!"
        tr "..."
        mc "*Whispers* Why don't we ditch our friends and get out of here?"
        tr "*Whispers* That's not gonna happen!"
        scene 11_2192 with Dissolve(1)
        mc "*Whispers* Tengo muchas ganas de follarte!\n(I really want to fuck you!)"
        mc "*Whispers* Sabes cuánto me excitas?\n(Do you have any idea how much you turn me on?)"
        mc "*Whispers* Estás buenísima!\n(You are so hot!)"
        x "Two mojitos, a cosmopolitan and a beer. That's forty-two dollars, please."
        scene 11_2193 with Dissolve(1)
        mc "{i}(Forty-two dollars? For four drinks? Are you kidding me?){/i}"
        mc "{i}(Was it that expensive last time I was here with Layla and Elena?){/i}"
        mc "..."
        mc "{i}(Right... Zach paid for our drinks.){/i}"
        scene 11_2194 with Dissolve(1)
        mc "Here's your cosmo."
        tr "Thank you."
        scene 11_2195 with Dissolve(1)
        mc "I guess I'll see you the next time we bump into each other."
        tr "Heh, yes."
        mc "Adiós, chica."
        tr "Haha. Adiós, chico."
        scene 11_2196 with Dissolve(1)
        tr "..."
        scene 11_2197 with Dissolve(1)
        x "Who was that?"
        tr "Dios mío... You scared me!"
        x "So?"
        tr "Nobody. Just someone who ordered drinks."
        x "And that nobody just happened to order something for you too?"
        scene 11_2198 with Dissolve(1)
        x "Oh come on, Gabs. I've known you for over ten years."
        x "I saw your face."
        x "You know him. And you enjoy the attention he's giving you."
        scene 11_2199 with Dissolve(1)
        tr "I have no idea what you're talking about."
        x "Uh-huh..."
        x "He's handsome. A little young though, no?"
        x "Feels like I've seen him before."
        tr "..."
    scene 11_2200 with Dissolve(1)
    mc "Here you go. Two mojitos!"
    a "Thank you, babe."
    ir "Thanks."
    scene 11_2201 with Dissolve(1)
    mc "Cheers, everyone."
    ir "Cheers!"
    scene 11_2202 with Dissolve(1)
    ir "When did you guys actually start dating?"
    mc "Why are you looking at me? She asked us, not just me!"
    a "I want you to answer!"
    mc "..."
    mc "*Sigh* That is such a girl thing to say."
    scene 11_2203 with Dissolve(1)
    mc "It depends, I guess."
    mc "Some people count from the moment they met, others the first time they had sex, first date and so on..."
    mc "So could be the plane, the bar, the concert... I don't know. You pick one."
    a "We kinda broke up after..."
    mc "Oh yeah. Hmm..."
    scene 11_2204 with Dissolve(1)
    ir "You guys are so confusing!"
    ir "Just tell me the whole story!"
    scene black with Dissolve(1)
    pause 2
    scene 11_2205 with Dissolve(1)
    ir "You guys could've been a drama TV show..."
    a "..."
    mc "Haha."
    scene 11_2206 with Dissolve(1)
    a "I'm gonna get us some new drinks."
    mc "I can go."
    a "I need to use the bathroom too."
    scene 11_2207 with Dissolve(1)
    ir "Did I say something wrong?"
    mc "No. It's just that the thing between her and Erynn was pretty heavy and I think she doesn't want to be reminded."
    mc "It hasn't been that long."
    scene 11_2208 with Dissolve(1)
    ir "There's an easy way to make her forget."
    mc "Yeah?"
    ir "Get her drunk."
    mc "Haha."
    scene 11_2209 with Dissolve(1)
    mc "I've actually never seen her drunk."
    ir "No?"
    mc "Have you?"
    ir "A few times, at the dorm."
    scene 11_2210 with Dissolve(1)
    mc "What kind of drunk is she? The aggressive type, or...?"
    ir "No. Fun drunk. And she'll get more flirty."
    mc "Just like you then!"
    scene 11_2211 with Dissolve(1)
    ir "No, I'm more of the aggressive type."
    mc "Aggressive in another way."
    ir "Uh-huh..."
    if Iris_Points >= 1:
        scene 11_2212 with Dissolve(1)
        ir "..."
        mc "..."
    else:
        pass
    scene 11_2213 with Dissolve(1)
    a "Two mojitos and a beer."
    mc "Look at you. So professional. It seems like you've done this before."
    a "Idiot!"
    ir "Haha."
    scene 11_2214 with Dissolve(1)
    mc "Thanks!"
    a "You're welcome."
    scene 11_2215 with Dissolve(1)
    mc "Hmm...?"
    scene 11_2216 with Dissolve(1)
    a "Is it not good?"
    mc "It tastes different."
    a "Oh... I forgot to ask for alcohol-free..."
    scene 11_2217 with Dissolve(1)
    a "Sorry..."
    a "Drinking one beer should be fine, no?"
    mc "When I drive, I don't drink at all. That's a promise I made with Mom, and with John too, actually."
    ir "I remember that."
    mc "I guess you'll have to finish it for me!"
    scene 11_2218 with Dissolve(1)
    ir "Chug it!"
    a "I don't know if I can, I've never done that."
    ir "Just try it, it's easy."
    a "Then you do it!"
    ir "You made the mistake!"
    scene 11_2219 with Dissolve(1)
    a "Fine..."
    mc "{i}(She's actually doing it.){/i}"
    scene 11_2220 with Dissolve(1)
    mc "GO LEXI!"
    ir "Chug, chug, chug."
    a "..."
    scene 11_2221 with Dissolve(1)
    a "*Shrugs* Uh... That was actually terrible. Why do people do this?"
    mc "Haha. You did good though. Was that really your first time?"
    a "Yeah. And never again!"
    scene 11_2222 with Dissolve(1)
    mc "You didn't have to do something like that when you joined the sorority?"
    a "I'm not in a sorority."
    mc "You aren't? I thought you were."
    mc "So you never had to do the hazing stuff?"
    a "No."
    mc "Boring!"
    scene 11_2223 with Dissolve(1)
    a "Heh. Boring..."
    mc "They do have sororities and fraternities at MSU though, right?"
    a "They do."
    mc "Pfew..."
    scene 11_2224 with Dissolve(1)
    mc "Are you in one, Iris?"
    ir "I'm not either."
    mc "Why?"
    scene 11_2225 with Dissolve(1)
    a "Can you let me pass again, please?"
    mc "Haha... Bathroom again?"
    mc "I have the same issue. If I go the first time, I'll have to go every ten minutes."
    mc "That's why I try to hold it as long as I can."
    scene 11_2226 with Dissolve(1)
    a "No, I'm gonna get you a new beer. Alcohol-free this time."
    mc "I can get it."
    a "No, it's fine. I have to use the bathroom too."
    mc "Haha, I knew it!"
    a "Only because you mentioned it!"
    scene 11_2227 with Dissolve(1)
    ir "She's gonna be drunk so quickly."
    mc "I think so too. She's getting tipsy already."
    scene black with Dissolve(1)
    pause 2
    scene 11_2228 with Dissolve(1)
    ""
    scene 11_2229 with Dissolve(1)
    ""
    scene 11_2230 with Dissolve(1)
    ""
    scene black with Dissolve(1)
    pause 2
    scene 11_2231 with Dissolve(1)
    a "Come dance with me!"
    mc "Dance...? Uh..."
    a "We're not here only to drink."
    mc "Dance with Iris."
    a "She can come too!"
    scene 11_2232 with Dissolve(1)
    a "Come on! Just a little bit!"
    a "Please?"
    mc "Fine. One song!"
    a "Two! Maybe three or four!"
    mc "..."
    scene 11_2233 with Dissolve(1)
    mc "I feel like a little kid who gets dragged by his parents to do something he doesn't want to."
    ir "Haha."
    a "You don't like to dance?"
    ir "He doesn't."
    scene black with Dissolve(1)
    pause 2
    scene 11_2234 with Dissolve(1)
    ""
    scene 11_2235 with Dissolve(1)
    mc "I always feel stupid when I'm dancing. I probably look stupid, too!"
    a "Haha. No, you don't! And why would you feel stupid?"
    mc "I don't know..."
    scene 11_2236 with Dissolve(1)
    mc "{i}(It seems like every time I come here, I dance with two girls.){/i}"
    scene 11_2237 with Dissolve(1)
    ""
    scene 11_2238 with Dissolve(1)
    ir "..."
    scene 11_2239 with Dissolve(1)
    mc "Having fun?"
    a "*Nods*"
    scene 11_2240 with Dissolve(1)
    a "Aah-haha..."
    scene 11_2241 with Dissolve(1)
    ""
    scene 11_2242 with Dissolve(1)
    a "See! You have fun too!"
    mc "A little maybe."
    a "Haha. That's a start."
    a "Let's take a picture."
    scene 11_2243 with Dissolve(1)
    a "Smile!"
    scene 11_2244 with Dissolve(1)
    a "Let's take one with Iris, too."
    mc "Sure."
    scene 11_2245 with Dissolve(1)
    a "Iris, do you... Iris?"
    a "..."
    a "Where is she?"
    mc "I have no idea. She was next to me this whole time."
    x "*Cheer*"
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 11_2246 at moveup
    pause 3
    mc "{i}(Of course...){/i}"
    a "What is she doing...?"
    scene 11_2247 with Dissolve(1)
    n "*Cheering*"
    x "Yeah! You go girl!"
    scene 11_2248 with Dissolve(1)
    x "Can I have your number?"
    scene 11_2249 with Dissolve(1)
    n "*Cheering*"
    x "You're so fucking sexy!"
    mc "{i}(Thirsty much?){/i}"
    scene 11_2250 with Dissolve(1)
    ir "Hey!"
    x "Hey girl!"
    mc "..."
    scene 11_2251 with Dissolve(1)
    ir "Join me, Alexis!"
    a "No, I'm good."
    ir "Come on!"
    x "I'll join you!"
    ir "Please, Lex!"
    scene 11_2252 with Dissolve(1)
    a "*Sigh* Fine..."
    a "Just this one song!"
    ir "Of course."
    mc "{i}(I'd never would've guessed she would go up there as well.){/i}"
    mc "{i}(Well, she had plenty of liquid courage...){/i}"
    scene 11_2253 with Dissolve(1)
    a "Now that I'm up here, this is actually so scary... Why did I agree to this?"
    ir "You were dancing earlier. Now you're just dancing here."
    a "Yeah, but this is different. And everyone is watching us."
    ir "They were watching us earlier too and you didn't even realise. Just don't think about it. Ignore them and have fun! Follow my lead."
    a "..."
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 11_2254 at moveup
    pause 3
    mc "{i}(This is amazing! They're so sexy!){/i}"
    mc "{i}(Iris always has a way to loosen people up.){/i}"
    mc "{i}(I guess I'll get my phone out, too.){/i}"
    scene 11_2255 with Dissolve(1)
    x "*Cheering*"
    scene 11_2256 with Dissolve(1)
    ir "See! It's not that bad, right?"
    a "No. Because of all the lights here, I don't even see the other people."
    scene 11_2257 with Dissolve(1)
    x "Kiss! Kiss! Kiss!"
    scene 11_2258 with Dissolve(1)
    x "*Cheering*"
    scene 11_2259 with Dissolve(1)
    mc "*Cheering*"
    mc "{i}(What the fuck? Why am I cheering now, too?){/i}"
    scene 11_2260 with Dissolve(1)
    a "Haha."
    ir "That was great. Thanks for joining me!"
    scene 11_2261 with Dissolve(1)
    mc "I'll help you down."
    a "Thanks."
    scene 11_2262 with Dissolve(1)
    mc "You looked sexy!"
    a "Yeah?"
    mc "Uh-huh."
    scene 11_2263 with Dissolve(1)
    mc "I'll help you, too."
    ir "Thank you."
    scene 11_2264 with Dissolve(1)
    ir "Aaah... Hey!"
    ir "What's with the different handling?"
    mc "Want me to put you back up there?"
    ir "Haha. No!"
    scene 11_2265 with Dissolve(1)
    mc "That was great! You guys looked amazing up there!"
    a "Thanks."
    mc "Everyone seemed to enjoy your little show."
    scene 11_2266 with Dissolve(1)
    mc "You okay?"
    a "Just a little dizzy from the dancing and spinning around."
    mc "And in combination with all those cocktails."
    a "I could use one of them now."
    mc "Heh."
    scene black with Dissolve(1)
    pause 2
    scene 11_2267 with Dissolve(1)
    mc "{i}(How many has she drunk now?){/i}"
    mc "{i}(This is crazy...){/i}"
    scene 11_2268 with Dissolve(1)
    a "Mmm..."
    mc "Starting to get tired? Time to go home then?"
    a "Not yet. One more..."
    ir "I think you've had enough for today, Lex."
    scene 11_2269 with Dissolve(1)
    a "..."
    mc "What?"
    scene 11_2270 with Dissolve(1)
    a "You're so hot!"
    mc "You're drunk."
    a "No..."
    mc "Yes!"
    ir "Haha. I told you she's a fun-flirty drunk."
    scene 11_2271 with Dissolve(1)
    a "Just look at this face. So handsome. Isn't he handsome, Iris?"
    ir "He is!"
    a "The most handsomest!"
    mc "I'd say phrasing right now, but you'll probably wouldn't get it."
    a "What?"
    mc "Exactly."
    scene 11_2272 with Dissolve(1)
    mc "..."
    scene 11_2273 with Dissolve(1)
    mc "Uh..."
    scene 11_2274 with Dissolve(1)
    ""
    scene 11_2275 with Dissolve(1)
    mc "{i}(What is she doing?){/i}"
    scene 11_2276 with Dissolve(1)
    mc "Are you trying to win at kissing or something? This isn't a competition!"
    a "I'm not trying to win. You are!"
    mc "Uh-huh, I can feel it."
    a "I'm the better kisser, maybe that's what you feel."
    scene 11_2277 with Dissolve(1)
    mc "The better kisser?"
    a "Yeah!"
    mc "There's no way you're the better kisser."
    a "Wanna bet?"
    mc "How you wanna do that?"
    scene 11_2278 with Dissolve(1)
    ir "I might have an idea."
    mc "Yeah?"
    ir "I know how you kiss. If I kiss Alexis, I can compare the two of you."
    mc "I see what you're trying to do!"
    ir "Just trying to help!"
    mc "Uh-huh..."
    menu:
        "Don't do the bet":
            scene 11_2279 with Dissolve(1)
            mc "I'll just take the L on this one."
            a "So, I'm the better kisser?"
            mc "Sure. Whatever..."
            a "Hehe."
        "Let her kiss Alexis[KoGa3AutoWTChange1]{size=-4}(Alexis Week5 Wednesday Club KissIris) {/size} {/color}":
            $ Alexis_Week5_Wednesday_Club_KissIris = True
            scene 11_2280 with Dissolve(1)
            mc "It's up to you. Still wanna do the bet?"
            a "Sure. Let's find out who kisses better!"
            scene 11_2281 with Dissolve(1)
            a "This is a one-time thing, okay?"
            ir "Whatever you want."
            mc "{i}(I'm sure Iris has wanted to kiss her many times before.){/i}"
            scene 11_2282 with Dissolve(1)
            mc "{i}(I guess she's getting her wish.){/i}"
            mc "{i}(But I can't help being really excited myself.){/i}"
            scene 11_2283 with Dissolve(1)
            mc "{i}(Should I be filming this?){/i}"
            mc "{i}(Like... Holy shit!){/i}"
            scene 11_2284 with Dissolve(1)
            mc "{i}(She's really going for it now...){/i}"
            mc "{i}(Should I be jealous or something? Because I'm not...){/i}"
            mc "{i}(I wish I would've seen the kiss between Lexi and Erynn though...){/i}"
            mc "{i}(I need to find out if that really happened or if they were just joking.){/i}"
            scene 11_2285 with Dissolve(1)
            ir "That was a great kiss. You're a good kisser, Lex."
            a "Thanks. So are you!"
            ir "How do you want me to rate it? Out of ten, or...?"
            a "We just need to know who the better kisser is."
            scene 11_2286 with Dissolve(1)
            mc "Wait before you answer."
            mc "This is a little unfair. Lexi's kiss is now fresh on your mind. Our last kiss was months ago..."
            mc "It'd be only fair if I got to kiss you too!"
            mc "To have a proper judgement!"
            scene 11_2287 with Dissolve(1)
            a "..."
            mc "What? You made the bet!"
            a "One kiss. One kiss!"
            mc "{i}(If she wasn't drunk. She would've never agreed to this.){/i}"
            mc "{i}(She wouldn't have kissed Iris to begin with.){/i}"
            mc "{i}(Is it wrong to take advantage of this situation?){/i}"
            scene 11_2288 with Dissolve(1)
            ir "*Whispers* Why do you always have to be so competitive?"
            mc "*Whispers* Nothing to do with competition. Maybe I just want to kiss you!"
            ir "Heh..."
            mc "*Whispers* Besides. You taught me how to kiss. Your reputation is on the line too!"
            ir "*Whispers* You'd better not disappoint then!"
            scene 11_2289 with Dissolve(1)
            mc "{i}(I've wanted to do this the whole day.){/i}"
            scene 11_2290 with Dissolve(1)
            ir "..."
            scene 11_2291 with Dissolve(1)
            mc "{i}(She's such an amazing kisser.){/i}"
            mc "{i}(Let's see if she likes this.){/i}"
            scene 11_2292 with Dissolve(1)
            ir "..."
            scene 11_2293 with Dissolve(1)
            mc "{i}(I guess she does!){/i}"
            scene 11_2294 with Dissolve(1)
            a "Okay, that's enough!"
            a "I said one kiss, not a whole make-out session!"
            mc "Haha, sorry."
            scene 11_2295 with Dissolve(1)
            a "So, who's the better kisser, Iris?"
            ir "Hmm..."
            ir "You have very soft lips and the kiss was amazing, Lex."
            ir "But I have to go with [mc]."
            a "..."
            scene 11_2296 with Dissolve(1)
            mc "See! I told you!"
            a "Get away from me!"
            mc "Haha. Are you mad now?"
            scene 11_2297 with Dissolve(1)
            mc "You should be happy that your boyfriend is such a great kisser."
            mc "Show me those soft lips."
            a "Rather than a kiss, I want another cocktail!"
            mc "No, you don't!"
            a "Haha. [mc], stop!"
            if Iris_Points >= 1:
                scene 11_2298 with Dissolve(1)
                ir "..."
            else:
                pass
    scene black with Dissolve(1)
    pause 2
    scene 11_2299 with Dissolve(1)
    mc "What time is it now?"
    ir "Almost two."
    mc "Already? Time went by quickly."
    ir "Shall we leave?"
    mc "Yeah. Before this one here falls asleep."
    stop music fadeout 1.0
    play music "Sounds/Street_Traffic.mp3" volume 0.5
    scene 11_2300 with Dissolve(1)
    mc "{i}(First the beach. Now the club. Can you have a better day?){/i}"
    scene 11_2301 with Dissolve(1)
    ir "I'll head over this way."
    mc "What do you mean? We're parked over there."
    scene 11_2302 with Dissolve(1)
    ir "I'll take the train home."
    mc "You don't have to take the train. I can drive you."
    ir "I live on the other side of town. If you take me home first and then Alexis, you'll be driving for an hour."
    mc "That's no problem."
    scene 11_2303 with Dissolve(1)
    ir "It's fine. Just take Alexis home."
    a "I don't mind, either."
    ir "No, seriously."
    mc "Alright."
    scene 11_2304 with Dissolve(1)
    ir "This was fun. The beach, the club..."
    ir "Volleyball not so much."
    mc "Haha."
    ir "Thanks for inviting me!"
    a "Of course. I'll call you tomorrow, okay?"
    scene 11_2305 with Dissolve(1)
    ir "Bye, [mc]."
    mc "Bye, Iris. Message me once you get home."
    ir "Heh. I know!"
    scene 11_2306 with Dissolve(1)
    ir "Drive safe!"
    scene 11_2307 with Dissolve(1)
    mc "It's just the two of us, now."
    mc "Let's go home."
    a "Mm-hmm."
    if Iris_Points >= 1:
        scene 11_2308 with Dissolve(1)
        ir "..."
    else:
        pass
    scene 11_2309 with Dissolve(1)
    mc "Can I have the keys, please?"
    a "They're in my pocket."
    mc "Do skirts have pockets?"
    a "Some do. This one has an inside pocket."
    scene 11_2310 with Dissolve(1)
    mc "Can I have them?"
    a "..."
    mc "What? You want me to get them myself?"
    a "*Nods*"
    scene 11_2311 with Dissolve(1)
    mc "..."
    mc "{i}(If someone comes by now, what would they think we're doing?){/i}"
    mc "{i}(Don't worry, it's not what you think. I'm just looking for the car keys...){/i}"
    mc "{i}(They're in my girlfriend's vagina...){/i}"
    scene 11_2312 with Dissolve(1)
    a "Ahh..."
    a "Not that pocket!"
    mc "..."
    scene 11_2313 with Dissolve(1)
    a "That one is empty!"
    mc "For now!"
    a "Mmm..."
    scene 11_2314 with vpunch
    a "Aaah..."
    mc "Sorry... My finger slipped."
    mc "It's so wet down there!"
    scene 11_2315 with vpunch
    a "[mc]!"
    mc "Haha."
    mc "Let's get in the car. We can continue this at home!"
    scene 11_2316 with Dissolve(1)
    mc "{i}(I've always wanted to drive such a car.){/i}"
    mc "{i}(This is gonna be so cool!){/i}"
    scene 11_2317 with Dissolve(1)
    a "Did you know that this is the first time that you've been driving when we are in a car together?"
    mc "Really?"
    mc "I've driven you before, no?"
    if MC_Bike == True:
        a "On your bike, yes. But not in a car."
    else:
        a "No. Never."
    scene 11_2318 with Dissolve(1)
    a "You look sexy when you're driving!"
    mc "Haha. Thanks. But it's probably due to the car."
    a "No..."
    scene 11_2319 with Dissolve(1)
    a "[mc]?"
    mc "Hmm?"
    a "I'm horny!"
    mc "Heh... I know. I felt it. But don't worry. We'll take care of that once we're home!"
    a "Yeah?"
    mc "Oh yeah! The things we're about to do!"
    scene black with Dissolve(1)
    pause 2
    stop music fadeout 1.0
    play music ("Music/LoFi Upbeat 1.mp3", "Music/LoFi Upbeat 2.mp3", "Music/LoFi Upbeat 3.mp3", "Music/LoFi Upbeat 4.mp3") volume 0.2
    scene 11_2320 with Dissolve(1)
    mc "..."
    a "*Cough-cough*"
    mc "{i}(This isn't what I had in mind...){/i}"
    mc "Are you okay?"
    if Nikki_Girlfriend == True:
        scene 11_2321 with Dissolve(1)
        mc "{i}(First Nikki, now Alexis...){/i}"
        mc "{i}(Is it really the alcohol, or is there some kind of bug going around?){/i}"
    else:
        pass
    scene 11_2322 with Dissolve(1)
    a "[mc]... I don't want to anymore."
    mc "Let it all out. You'll feel better after."
    a "I..."
    a "*Puking*"
    scene black with Dissolve(1)
    pause 2
    scene 11_2323 with Dissolve(1)
    mc "Change your clothes first. You can't sleep in those."
    a "It's fine..."
    mc "They smell of alcohol and smoke. Come on. I'll help you. It won't take long."
    scene 11_2324 with Dissolve(1)
    mc "Arms up!"
    a "..."
    scene 11_2325 with Dissolve(1)
    mc "Where are the clothes you wear to bed?"
    a "Just pick something."
    scene 11_2326 with Dissolve(1)
    mc "There! Now go sleep!"
    a "Aren't you staying?"
    mc "No. I'll go home. But I'll call you tomorrow, okay?"
    a "Okay..."
    scene 11_2327 with Dissolve(1)
    mc "Good night, Lexi."
    a "Good night."
    scene 11_2328 with Dissolve(1)
    mc "{i}(I'll leave the car keys here on the kitchen counter.){/i}"
    mc "{i}(They'll probably find them.){/i}"
    scene 11_2329 with vpunch
    x "Hey there, burglar!"
    mc "..."
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 11_2330 at moveup
    pause 3
    mc "Adriana!"
    scene 11_2331 with Dissolve(1)
    mc "You scared the living shit out of me!"
    am "What do you think my first reaction was when I saw a man in my house at night who wasn't my husband?"
    am "What are you doing sneaking around?"
    mc "I was just dropping your husband's car keys on the counter here."
    scene 11_2332 with Dissolve(1)
    am "And why do you have his car keys?"
    mc "I was out with Alexis and she was drinking. So I drove her home afterwards."
    am "..."
    am "Thank you for being responsible."
    scene 11_2333 with Dissolve(1)
    am "Is Alexis upstairs?"
    mc "Yeah. I've put her to bed. She was... Uh..."
    am "Drunk?"
    mc "Hmmyeah..."
    mc "{i}(And puking...){/i}"
    scene 11_2334 with Dissolve(1)
    mc "Anyway. I was about to leave. Have a good night, Adriana."
    am "Wait a second. How are you going home?"
    mc "The bus?"
    am "There are no buses anymore at this hour."
    mc "Then I'll just walk."
    scene 11_2335 with Dissolve(1)
    am "I don't want you to walk home. Let me get my keys, I'll drive you."
    mc "Thanks, but it's fine. I won't get kidnapped or anything."
    am "I'm still not comfortable letting you walk alone at night. Especially after they..."
    mc "Found a body a few days back?"
    am "Exactly!"
    scene 11_2336 with Dissolve(1)
    mc "{i}(First I drove her dad's cabrio. Now I'll be in her mom's sports car.){/i}"
    mc "{i}(What a day.){/i}"
    mc "{i}(I've seen Lexi in another car also. How many cars do they have?){/i}"
    scene 11_2337 with Dissolve(1)
    mc "{i}(The more I look at her, the more of Alexis I see in her.){/i}"
    mc "{i}(It's crazy how much they look alike.){/i}"
    mc "{i}(No wonder I mixed them up last time.){/i}"
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 11_2338 at moveup
    pause 3
    mc "{i}(And now seeing her in this dress...){/i}"
    mc "{i}(She's so gorgeous!){/i}"
    mc "{i}(We were joking earlier about fucking each other's mom. I would!){/i}"
    scene 11_2339 with Dissolve(1)
    mc "Do you know where I live or do you want me to put my address in the GPS?"
    am "I know it. I've driven Alexis many times to Erynn."
    mc "Right."
    scene 11_2340 with Dissolve(1)
    am "What have you guys been up to today?"
    mc "We went to the beach with some friends."
    mc "Spend most of the day there. Played some volleyball."
    scene 11_2341 with Dissolve(1)
    am "Alexis played too?"
    mc "{i}(She looks so surprised.){/i}"
    mc "Yeah."
    am "Really? Hmm."
    scene 11_2342 with Dissolve(1)
    mc "She totally kicked my ass. I didn't know she was that good."
    am "I loved to see her play. It's already three years, I think, since she last played."
    mc "Because of her ankle."
    am "Oh? She told you?"
    if Emily_Week5_Wednesday_BeachInvite_Adriana == True:
        $ Adriana_Points += 2
        # Adriana (6)
        scene 11_2343 with Dissolve(1)
        mc "But you might get another chance."
        mc "She was planning to invite you the next time we go to the beach. Together with my mom."
        am "Emily too? I'd love that! Thank you!"
        mc "Don't tell her I said that though."
        am "I won't."
        scene 11_2344 with Dissolve(1)
        mc "{i}(She looks happy!){/i}"
    else:
        pass
    scene 11_2345 with Dissolve(1)
    mc "And where have you been today?"
    mc "Date night with hubby?"
    am "Haha. Hubby?"
    am "Don't ever say that to him."
    scene 11_2346 with Dissolve(1)
    mc "Don't worry. He'll kill me anyway once he finds out I slapped your ass."
    mc "{i}(Fuck! Why did I just say that?){/i}"
    am "I'm actually trying to forget that."
    mc "Me too..."
    mc "{i}(Not really.){/i}"
    scene 11_2347 with Dissolve(1)
    am "He knows already."
    mc "You told him?"
    am "Why do you think I got you out of the house so quickly?"
    mc "Shit!"
    am "Haha."
    scene 11_2348 with Dissolve(1)
    mc "Wait! Maybe you aren't driving me home but you're about to do the job yourself?"
    mc "This area looks pretty foresty to me."
    am "Haha. You saw right through me. I was just about to take this dirt road."
    mc "I knew it!"
    mc "{i}(She even has the same banter as Alexis. She must have been fun when she was my age!){/i}"
    scene 11_2349 with Dissolve(1)
    am "All jokes aside. We went to a party of an ex-colleague of his."
    mc "You look the part. The dress looks amazing on you!"
    mc "{i}(Okay... Stop flirting with your girlfriend's mom!){/i}"
    am "Thank you!"
    scene 11_2350 with Dissolve(1)
    am "I see why Alexis likes you."
    am "And you're a good influence on her."
    mc "I don't know about that."
    am "Trust me. She's changed a lot in the last few weeks."
    scene black with Dissolve(1)
    pause 2
    scene 11_2351 with Dissolve(1)
    ""
    scene 11_2352 with Dissolve(1)
    mc "Thank you very much for driving me home, Adriana."
    mc "This was way quicker than walking."
    am "You're welcome."
    mc "If not earlier, I'll see you next week at school."
    scene 11_2353 with Dissolve(1)
    am "Yes. Good night, [mc]."
    am "And say hi to your mom for me. I mean not now, but tomorrow, okay?"
    mc "Hehe. Will do. Good night!"
    menu:
        "Kiss[KoGa3AutoWTChange1]{size=-4}(Adriana Week5 Wednesday Kiss, Adriana Points+2) {/size} {/color}":
            $ Adriana_Week5_Wednesday_Kiss = True
            $ Adriana_Points += 2
            # Adriana (6)
            scene 11_2354 with Dissolve(1)
            am "..."
            scene 11_2355 with Dissolve(1)
            mc "{i}(Why did I kiss her cheek? I feel so awkward now.){/i}"
            mc "..."
            mc "{i}(Is it weird to kiss your girlfriend's mom?){/i}"
            mc "{i}(Well, she isn't just her mom. She's also my principal.){/i}"
            mc "{i}(Oh man...){/i}"
            scene 11_2356 with Dissolve(1)
            am "*Shakes head*"
        "Leave":
            pass
    scene 11_2357 with Dissolve(1)
    mc "{i}(I'm beat!){/i}"
    if Iris_Points >= 1:
        scene 11_2358 with Dissolve(1)
        ir "..."
        scene 11_2359 with Dissolve(1)
        n "I still love you!"
        scene 11_2360 with Dissolve(1)
        ir "*Sigh*"
        scene 11_2361 with Dissolve(1)
        n "I'm home!"
    else:
        pass
    scene black with Dissolve(2)
    pause 2
    n "Thursday, 09:17."
    scene 11_2362 with Dissolve(1)
    n "*Knock-knock*"
    a "Yeah?"
    x "Can I come in?"
    a "Yeah."
    scene 11_2363 with Dissolve(1)
    x "Oh... You're still in bed."
    a "Was a long night."
    x "Did I wake you?"
    a "No, no. I've been awake for a while. Didn't wanna get up yet."
    scene 11_2364 with Dissolve(1)
    a "What's up?"
    x "I wanted to ask if you want to go for a run."
    a "..."
    a "Sure!"
    scene 11_2365 with Dissolve(1)
    x "*Sigh* Fine..."
    x "I'll ask Layla."
    a "..."
    scene 11_2366 with Dissolve(1)
    x "Wait..."
    x "Did you say yes?"
    a "Yeah."
    scene 11_2367 with vpunch
    a "Haha, Dad!"
    a "You're squishing me!"
    scene 11_2368 with Dissolve(1)
    x "Uhm... I'll... I'll wait downstairs."
    a "I'll be ready in 10 minutes."
    scene 11_2369 with Dissolve(1)
    x "One more thing."
    x "I'm gonna kill your boyfriend!"
    a "What? Why?"
    x "You know why!"
    scene 11_2370 with Dissolve(1)
    a "It was an honest mistake!"
    x "No such thing!"
    a "Haha. Please don't. I really like him!"
    x "I'll make it quick."
    a "DAD!"
    scene 11_2371 with Dissolve(1)
    am "Aaah!"
    am "What's up with you?"
    x "It's a good day!"
    am "Hmm?"
    jump Week5_Wednesday_End

label Week5_Wednesday_Layla_Date:
    $ Layla_Week5_Wednesday_ClubDate = True
    scene black with Dissolve(1)
    pause 2
    stop music fadeout 1.0
    play music ("Music/LoFi Upbeat 1.mp3", "Music/LoFi Upbeat 2.mp3", "Music/LoFi Upbeat 3.mp3", "Music/LoFi Upbeat 4.mp3") volume 0.2
    scene 11_2372 with Dissolve(1)
    mc "Is there seriously nothing on TV right now?"
    if MC_Bike == True:
        mc "Maybe I should go ride somewhere on my bike for a bit?"
    else:
        pass
    play sound "Sounds/Phone_Vibrate.mp3"
    n "*Bzzzt. Bzzzt*"
    scene 11_2373 with Dissolve(1)
    mc "Hey, Layla."
    la "Hey."
    mc "How are you?"
    la "I'm good."
    scene 11_2374 with Dissolve(1)
    mc "No hangover?"
    la "A little this morning, but it's fine now. You?"
    mc "I felt fine. Then again, I didn't drink as much as you girls. Especially you. You went crazy."
    scene 11_2375 with Dissolve(1)
    la "Haha, noooo..."
    mc "Yeeeesss..."
    mc "It was so much fun!"
    la "Yeah."
    mc "Still thinking about it."
    la "Me too..."
    scene 11_2376 with Dissolve(1)
    mc "What have you been up to today until now?"
    la "Cleaning the hot tub."
    mc "Why didn't you call me? I would've come and helped you."
    la "Thanks. Elena helped me."
    scene 11_2377 with Dissolve(1)
    mc "Is she still there?"
    la "No, she left a half hour ago or so."
    mc "Happy she could make it though."
    la "Yes. She needed a little uh... time off?"
    scene 11_2378 with Dissolve(1)
    if Alexis_SecretPath == False:
        la "What did you do today?"
        mc "Nothing special. I ran a little and chilled for the rest of the day basically."
        la "Same as me then. I'm lying on a hammock right now."
        mc "Picture or it didn't happen!"
    else:
        la "What did you do today?"
        mc "I ran a little this morning and I just came back from the beach."
        la "Oh, you were at the beach again?"
        scene 11_2379 with Dissolve(1)
        mc "Erynn invited me. Your sister was also there."
        la "What? Why wasn't I invited?"
        mc "Sorry. I should have!"
        la "Everyone goes to the beach with you. First Elena, now Erynn and Lex..."
        scene 11_2380 with Dissolve(1)
        la "I want to go too. It's been weeks since we went!"
        mc "We can go together next time!"
        la "Promise?"
        mc "I promise."
        scene 11_2381 with Dissolve(1)
        mc "What are you doing now?"
        la "Just chilling on a hammock."
        mc "Picture or it didn't happen!"
        la "What?"
        mc "Send me a picture."
    scene 11_2382 with Dissolve(1)
    la "..."
    scene 11_2383 with Dissolve(1)
    la "Aaah..."
    mc "What happened?"
    scene 11_2384 with Dissolve(1)
    la "Aww. I fell."
    mc "Haha."
    la "It's not funny!"
    mc "Sorry. Are you alright?"
    la "Yeah..."
    scene 11_2385 with Dissolve(1)
    la "Did you get the picture?"
    mc "Let me check real quick."
    scene 11_2386 with Dissolve(1)
    mc "Heh..."
    mc "{i}(She's such a cutie.){/i}"
    scene 11_2387 with Dissolve(1)
    mc "You're so cute, Layla."
    la "Thanks. You like it?"
    mc "You in a bikini. What's not to like?"
    la "Haha."
    scene 11_2388 with Dissolve(1)
    la "Hey..."
    la "Yesterday, after the hot tub party, we... uhm..."
    la "Do you still wanna go out with me today?"
    scene 11_2389 with Dissolve(1)
    mc "Of course! Our date, right?"
    la "Yes!"
    mc "Whenever you're ready, I'll come pick you up."
    scene 11_2390 with Dissolve(1)
    la "Uh, okay..."
    la "I'll get ready right now!"
    mc "When do you want me to come over?"
    la "An hour?"
    mc "{i}(A girl who's ready within an hour. I knew it was possible!){/i}"
    scene 11_2391 with Dissolve(1)
    mc "Alright. See you in an hour, then."
    la "Kay. Bye, [mc]."
    mc "Later, Layla!"
    scene 11_2392 with Dissolve(1)
    la "YAY!"
    scene 11_2393 with vpunch
    la "Ouch!"
    scene black with Dissolve(2)
    pause 2
    if MC_Bike == True:
        scene 11_2394 with Dissolve(1)
        mc "{i}(Should I take the bike?){/i}"
        mc "{i}(Layla hasn't seen it yet.){/i}"
        mc "{i}(But if we go out, I won't be able to drink or I'll have to keep it at Layla's for a day...){/i}"
        mc "{i}(Next time.){/i}"
    else:
        pass
    scene 11_2395 with Dissolve(1)
    n "*Ding-dong*"
    scene 11_2396 with Dissolve(1)
    la "Hey."
    mc "..."
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 11_2397 at moveup
    pause 3
    mc "Holy shit!"
    mc "You look incredible, Layla!"
    la "Thank you!"
    scene 11_2398 with Dissolve(1)
    mc "Can you close the door and open it again?"
    la "What?"
    mc "I just want to see it again."
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 11_2399 at moveup
    pause 3
    mc "Oh my god... Layla..."
    la "..."
    mc "So fucking sexy!"
    scene 11_2400 with Dissolve(1)
    mc "Can you also do like a twirl, please?"
    la "Like this?"
    mc "Uh-huh."
    scene 11_2401 with Dissolve(1)
    mc "Okay, I'm touching you right now. You must be real!"
    mc "Please tell me you're real and I'm not dreaming right now."
    la "Haha. I am!"
    scene 11_2402 with Dissolve(1)
    mc "You've changed your makeup too!"
    la "*Nods*"
    mc "It's beautiful! Makes your eyes really pop."
    mc "I need to do one more thing to be sure you're real."
    scene 11_2403 with Dissolve(1)
    ""
    scene 11_2404 with Dissolve(1)
    la "Still think you're dreaming? Because now I think I am..."
    mc "Haha."
    mc "If there's anything I can do to help you with that, just tell me."
    scene 11_2405 with Dissolve(1)
    mc "Shall we leave? Are you ready to go?"
    la "Mm-hmm."
    scene 11_2406 with Dissolve(1)
    mc "I'm gonna walk like this so I can look at you this whole time."
    mc "Warn me if I'm about to run into a pole or something."
    la "Haha. I will."
    scene black with Dissolve(2)
    pause 2
    scene 11_2407 with Dissolve(1)
    la "Okay, you can stop now..."
    la "People are already looking."
    mc "Haha. They're not looking because of me!"
    la "..."
    mc "*Sigh* But fine..."
    scene 11_2408 with Dissolve(1)
    mc "Better this way?"
    la "Yes! I like this much more!"
    scene 11_2409 with Dissolve(1)
    mc "So, where do you wanna go?"
    la "Hmm..."
    la "I was actually thinking about Heaven. Because that was the first place we went to together."
    la "But if you don't wanna go there, we can also go to a bar, or..."
    scene 11_2410 with Dissolve(1)
    mc "I'm good with Heaven."
    mc "You, looking like this. I'll follow you wherever you wanna go!"
    la "..."
    scene 11_2411 with Dissolve(1)
    la "Maybe I should pick something really girly then!"
    mc "Girly, huh? Like what?"
    la "Hmm... Maybe a lingerie store?"
    scene 11_2412 with Dissolve(1)
    mc "Haha. You think I'd be embarrassed to go in there?"
    mc "Quite the opposite! You testing on different lingerie? Let's go!"
    la "Noooo... Let me think of something else then."
    scene 11_2413 with Dissolve(1)
    la "Let's see..."
    la "..."
    mc "Can't think of anything?"
    la "Give me a second."
    scene 11_2414 with vpunch
    mc "..."
    scene 11_2415 with Dissolve(1)
    la "Haha. That's what you get!"
    mc "Thanks for the warning!"
    la "Haha, sorry. I wasn't paying attention, either."
    scene 11_2416 with Dissolve(1)
    la "Does it hurt?"
    mc "Change of plans."
    mc "We need to go to the hospital. I think I broke my arm."
    la "What? Are you serious? Let me see..."
    scene 11_2417 with Dissolve(1)
    mc "Ahhh..."
    la "I'm sorry!"
    mc "{i}(She's so cute!){/i}"
    scene 11_2418 with Dissolve(1)
    la "Aaah!"
    mc "Haha, I'm kidding. There's nothing wrong with my arm!"
    la "[mc]!"
    scene 11_2419 with Dissolve(1)
    la "Don't do this to me!"
    la "Not today!"
    mc "{i}(Not today?){/i}"
    scene 11_2420 with Dissolve(1)
    mc "Sorry. No pranks today."
    la "..."
    scene 11_2421 with Dissolve(1)
    mc "Decided where to go?"
    la "Let's just do Heaven?"
    mc "Sure."
    scene black with Dissolve(1)
    pause 2
    scene 11_2422 with Dissolve(1)
    mc "..."
    mc "Wow... There's already a line this early? On a Wednesday?"
    mc "Is there some special event happening today?"
    scene 11_2423 with Dissolve(1)
    la "Most days it's like this."
    la "We were lucky the last time we came."
    la "And at spring break, it's always packed. Any day of the week."
    mc "Right."
    scene 11_2424 with Dissolve(1)
    mc "*Sigh*"
    mc "We've been standing here for fifteen minutes..."
    mc "Feels like this line isn't even moving. Can't be that they're at max capacity already."
    la "I don't know."
    scene 11_2425 with Dissolve(1)
    la "We can go somewhere else if you want."
    mc "No. Let's wait a bit more. Can't be that much longer."
    la "Okay."
    scene 11_2426 with Dissolve(1)
    mc "{i}(What's going on?){/i}"
    mc "{i}(Are they letting one person in every ten minutes?){/i}"
    la "..."
    scene 11_2427 with Dissolve(1)
    mc "{i}(And what's this guy's issue?){/i}"
    menu:
        "Say something[KoGa3AutoWTChange1]{size=-4}(Layla Points+2) {/size} {/color}":
            $ Layla_Points += 2
            # Layla (90)
            scene 11_2428 with Dissolve(1)
            mc "Hey!"
            mc "Need something?"
            x "No..."
            mc "Then eyes up front, buddy!"
            scene 11_2429 with Dissolve(1)
            mc "What?"
            la "Nothing."
        "Do nothing":
            mc "{i}(Whatever.){/i}"
    scene 11_2430 with Dissolve(1)
    n "Ten minutes later."
    la "Shall we go somewhere else?"
    mc "Hmm... I think I might have an idea. Do you trust me?"
    la "Yes."
    mc "When I say 'now', don't say anything, just follow me quickly."
    la "*Nods*"
    scene 11_2431 with Dissolve(1)
    mc "{i}(We just have to wait until the bouncer is busy.){/i}"
    mc "{i}(The other one still hasn't come back.){/i}"
    mc "{i}(I guess we won't get a better chance.){/i}"
    scene 11_2432 with Dissolve(1)
    mc "Now!"
    la "..."
    scene 11_2433 with Dissolve(1)
    mc "{i}(I hope this works.){/i}"
    mc "{i}(If not...){/i}"
    stop music fadeout 1.0
    play music ("Music/Kyroflux - Drop the Night.mp3", "Music/Kyroflux - Starlight.mp3", "Music/Kyroflux - Circuit Breaker.mp3", "Music/Kyroflux - After Hours.mp3") volume 0.4
    scene 11_2434 with Dissolve(1)
    la "What is this place?"
    mc "Side entrance, I guess. They probably use it for drinks and food deliveries."
    mc "And maybe even to sneak in celebrities. Who knows?"
    scene 11_2435 with Dissolve(1)
    la "Are we allowed to be here?"
    mc "Most likely not. So, let's not get caught."
    la "[mc]!"
    mc "Haha. Come on. Let's go before anyone sees us."
    scene 11_2436 with Dissolve(1)
    la "Elena was right about you!"
    mc "What did she say?"
    la "That you're trouble."
    mc "Haha. Typical Elena."
    scene 11_2437 with Dissolve(1)
    mc "Funny though. That's the first thing I thought about you when I first met you in the hallway at school. Trouble."
    la "What? That's the first thing? I'm not trouble!"
    mc "Nooo... Of course not..."
    la "..."
    la "You didn't think anything else?"
    scene 11_2438 with Dissolve(1)
    mc "And that you're really cute."
    la "Heh. You thought I was cute?"
    mc "I still do!"
    mc "And I thought you might be a teacher who was looking for me."
    scene 11_2439 with Dissolve(1)
    la "Haha. A teacher."
    la "A cute teacher!"
    mc "Haha. See! Trouble!"
    scene 11_2440 with Dissolve(1)
    mc "..."
    scene 11_2441 with Dissolve(1)
    mc "{i}(Oh shit!){/i}"
    la "..."
    scene 11_2442 with Dissolve(1)
    mc "{i}(Not the best hiding spot, but we don't really have options here){/i}"
    scene 11_2443 with Dissolve(1)
    mc "{i}(Don't turn your head. Nothing's going on here.){/i}"
    mc "{i}(Just keep moving.){/i}"
    mc "{i}(That was close...){/i}"
    scene 11_2444 with Dissolve(1)
    mc "Hey! Layla?"
    la "..."
    mc "He's gone. You can open your eyes again."
    scene 11_2445 with Dissolve(1)
    mc "Why did you close them anyway?"
    mc "It's not that if you can't see him, he can't see you. The thing they do with babies."
    la "That's not it! I closed them because I was scared!"
    la "Do you have any idea how fast my heart is beating right now?"
    menu:
        "Go to the club":
            scene 11_2446 with Dissolve(1)
            mc "Come on!"
            mc "Let's get inside the club before we actually get caught."
            la "*Nods*"
        "Kiss her[KoGa3AutoWTChange1]{size=-4}(Layla Points+2) {/size} {/color}":
            $ Layla_Points += 2
            # Layla (92)
            scene 11_2447 with Dissolve(1)
            mc "Is it?"
            mc "I bet I can make it beat even faster!"
            la "..."
            scene 11_2448 with Dissolve(1)
            ""
            scene 11_2449 with Dissolve(1)
            mc "{i}(Mine is beating faster, too.){/i}"
            scene 11_2450 with Dissolve(1)
            la "Ahh..."
            scene 11_2451 with Dissolve(1)
            ""
            scene 11_2452 with Dissolve(1)
            mc "And? Did it increase even more?"
            la "..."
            mc "Not telling me?"
            la "*Shakes head*"
            mc "Heh..."
            scene 11_2453 with Dissolve(1)
            mc "Come on!"
            mc "Let's get inside the club now before we actually get caught."
            la "Yeah."
    scene black with Dissolve(1)
    pause 2
    scene 11_2454 with Dissolve(1)
    la "*Sigh* We made it!"
    mc "And we didn't get caught!"
    mc "Wasn't that better than waiting for I don't know how long in line outside?"
    la "I don't know. That was so scary!"
    mc "Haha."
    scene 11_2455 with Dissolve(1)
    la "Why are they all looking at us?"
    mc "We came from the back entrance. They probably think we're celebrities."
    la "Oh..."
    scene 11_2456 with Dissolve(1)
    la "If you were a celebrity. Who would you be?"
    mc "Hmm... I don't know. Maybe an athlete? Are athletes celebrities?"
    la "I think so."
    mc "How about you?"
    scene 11_2457 with Dissolve(1)
    la "Well, I can't sing..."
    mc "And you can't act!"
    la "You don't know that!"
    mc "Haha. Can you?"
    la "I've never done it, so... I might be really good at it."
    scene 11_2458 with Dissolve(1)
    mc "A mattress actress maybe."
    la "What's that?"
    mc "Uh... An actress for a bed commercial?"
    mc "{i}(She'll never believe that, right?){/i}"
    la "Oh... So just lying happily on a bed and pretending you have the best sleep ever? I can do that."
    mc "{i}(There's no way. How can someone be flirty and so innocent at the same time? Protect this girl at all costs.){/i}"
    scene 11_2459 with Dissolve(1)
    la "[mc]. There's a free table. Should we go there?"
    mc "Perfect."
    scene 11_2460 with Dissolve(1)
    mc "Was this table worth the trouble?"
    mc "We would've never gotten it if we'd waited in line."
    la "I guess."
    mc "I'll get us something to drink. What do you want?"
    scene 11_2461 with Dissolve(1)
    la "Hmm... What will you get?"
    mc "Probably a beer."
    la "Can we do like a shot?"
    mc "Sure. Tequila?"
    la "Yes. And I'll take a Mai Tai cocktail."
    scene 11_2462 with Dissolve(1)
    mc "Alright. Will you stay here so we don't lose the table?"
    la "Uh-huh."
    mc "Kay. Don't go flirting with other boys though!"
    la "Haha. I won't."
    scene 11_2463 with Dissolve(1)
    mc "Be right back!"
    scene 11_2176 with Dissolve(1)
    mc "*Sigh*"
    mc "{i}(We skipped the line outside, but now I'm gonna be stuck in this one for a while...){/i}"
    scene 11_2177 with vpunch
    mc "{i}(For fuck's sake! Why is everyone pushing here?){/i}"
    mc "{i}(It won't be any faster!){/i}"
    scene 11_2178 with vpunch
    mc "..."
    x "Ahh..."
    mc "Hey! Stop pushing already!"
    if Gabi_End == True:
        scene 11_2179 with Dissolve(1)
        tr "Can you be a little more careful? People are sitting here!"
        mc "{i}(Oh... It's Gabi.){/i}"
        mc "Sorry. I got pushed."
        scene 11_2181 with Dissolve(1)
        mc "{i}(Kinda weird seeing your teacher in a club.){/i}"
        x "What can I get you?"
        mc "Two shots of tequila, a beer and a Mai Tai cocktail."
    else:
        scene 11_2180 with Dissolve(1)
        tr "Can you be a little more..."
        tr "[mc]..."
        mc "{i}(Gabi...){/i}"
        scene black with Dissolve(1)
        transform moveup:
            xalign 0.5 yalign 1.0
            linear 5.0 yalign 0.0
        show 11_2182 at moveup
        pause 3
        mc "Hola, Gabi."
        tr "Heh. Hola."
        mc "Sorry, I got pushed and..."
        tr "Está bien."
        scene 11_2183 with Dissolve(1)
        mc "{i}(Damn, she's looking so good again.){/i}"
        mc "{i}(I want to kiss her so bad.){/i}"
        menu:
            "Kiss her":
                scene 11_2184 with Dissolve(1)
                tr "What are you doing?"
                mc "I wanted to kiss your cheek."
                tr "Not gonna happen!"
                mc "{i}(Yeah, she's right. What was I thinking? If Layla saw...){/i}"
                mc "{i}(Not just Layla. Anyone who knows we're teacher and student.){/i}"
                scene 11_2185 with Dissolve(1)
                mc "Sorry."
                tr "..."
                mc "I like the dress. Estás hermosa!\n(You look beautiful!)"
                tr "Gracias."
            "Don't":
                mc "{i}(But I'd better not.){/i}"
                scene 11_2185 with Dissolve(1)
                mc "I like the dress. Estás hermosa!\n(You look beautiful!)"
                tr "Gracias."
        scene 11_2186 with Dissolve(1)
        mc "Are you here alone?"
        tr "Why would I be alone at a club?"
        mc "This is kinda how we met. Both drinking alone in a bar."
        tr "..."
        scene 11_2187 with Dissolve(1)
        tr "No, I'm here with a friend."
        mc "A friend?"
        mc "{i}(Why am I sounding so jealous? We aren't even...){/i}"
        mc "Where..."
        x "What can I get you?"
        scene 11_2188 with Dissolve(1)
        mc "Uh..."
        mc "{i}(Shit. What did she want again? Something with Thailand?){/i}"
        mc "Uhm... Two shots of tequila, a beer and a Thai..."
        x "Mai Tai?"
        mc "Yes!"
        scene 11_2189 with Dissolve(1)
        mc "Do you want something?"
        tr "..."
        tr "A cosmo."
        mc "And a cosmo, please."
        tr "Thank you!"
        scene 11_2190 with Dissolve(1)
        tr "Who are you here with?"
        mc "Friends!"
        tr "Hmm..."
        mc "{i}(Could it be that she's a little jealous too?){/i}"
        scene 11_2191 with Dissolve(1)
        mc "*Whispers* But I'd prefer to be spending time with you!"
        tr "..."
        mc "*Whispers* Why don't we ditch our friends and get out of here?"
        tr "*Whispers* That's not gonna happen!"
        scene 11_2192 with Dissolve(1)
        mc "*Whispers* Tengo muchas ganas de follarte!\n(I really want to fuck you!)"
        mc "*Whispers* Sabes cuánto me excitas?\n(Do you have any idea how much you turn me on?)"
        mc "*Whispers* Estás buenísima!\n(You are so hot!)"
        x "Two shots, a beer, a cosmopolitan and a Mai Tai. That's forty-four dollars, please."
        scene 11_2193 with Dissolve(1)
        mc "{i}(Forty-four dollars? For five drinks? Are you kidding me?){/i}"
        mc "{i}(Was it that expensive last time I was here, with Layla and Elena?){/i}"
        mc "..."
        mc "{i}(Right... Zach paid for our drinks.){/i}"
        scene 11_2464 with Dissolve(1)
        mc "Here's your cosmo."
        tr "Thank you."
        scene 11_2195 with Dissolve(1)
        mc "I guess I'll see you the next time we bump into each other."
        tr "Heh, yes."
        mc "Adiós, chica."
        tr "Haha. Adiós, chico."
        scene 11_2465 with Dissolve(1)
        tr "..."
        scene 11_2197 with Dissolve(1)
        x "Who was that?"
        tr "Dios mío... You scared me!"
        x "So?"
        tr "Nobody. Just someone who ordered drinks."
        x "And that nobody just happened to order something for you too?"
        scene 11_2198 with Dissolve(1)
        x "Oh come on, Gabs. I've known you for over ten years."
        x "I saw your face."
        x "You know him. And you enjoy the attention he's giving you."
        scene 11_2199 with Dissolve(1)
        tr "I have no idea what you're talking about."
        x "Uh-huh..."
        x "He's handsome. A little young though, no?"
        x "Feels like I've seen him before."
        tr "..."
    scene 11_2466 with Dissolve(1)
    mc "Here you go. You wanted a {i}Muay Thai{/i}, right?"
    la "Haha. Mai Tai, yes."
    mc "{i}(Mai Tai... Why do cocktails have such weird names?){/i}"
    mc "{i}(Even the word cocktail is weird...){/i}"
    scene 11_2467 with Dissolve(1)
    la "Cheers!"
    mc "Cheers."
    scene 11_2468 with Dissolve(1)
    la "Bleh..."
    mc "Haha."
    mc "{i}(Her face... Every time.){/i}"
    scene 11_2469 with Dissolve(1)
    mc "Do you even like tequila?"
    la "Not really."
    mc "Then why did you drink it?"
    la "Because I'm nervous."
    mc "Why would you be nervous?"
    la "*Shrugs*"
    scene 11_2470 with Dissolve(1)
    mc "You like the cocktail?"
    la "Mm-hmm. It's sweet."
    scene 11_2471 with Dissolve(1)
    la "Hey. Can I ask you a question?"
    mc "Sure."
    la "Back there you said the first time we met you thought I might be a teacher, right?"
    mc "Right."
    mc "{i}(I kinda have a feeling where this is going.){/i}"
    scene 11_2472 with Dissolve(1)
    la "If I really was a teacher, would you still think I'm cute?"
    mc "Haha. Layla..."
    mc "You being a teacher wouldn't change the fact that you're cute."
    la "Would you still go out with me?"
    scene 11_2473 with Dissolve(1)
    mc "Haha. Your mom is the principal. You'd get fired in no time."
    if Gabi_End == False:
        mc "{i}(I say that while doing the exact same thing with Gabi...){/i}"
    else:
        pass
    la "I know but just like pretend I was your teacher."
    la "What would you do?"
    scene 11_2474 with Dissolve(1)
    mc "What would I do? Uh... Be in your class, pay attention, take notes... I don't know."
    la "That's it?"
    mc "I don't know what you're imagining right now, but I can't just slap your ass or kiss you or anything. Especially while in class."
    scene 11_2475 with Dissolve(1)
    la "No, I mean... Would you like... Look at me?"
    la "In a certain way..."
    mc "Like this?"
    la "*Nods*"
    scene 11_2476 with Dissolve(1)
    mc "I would..."
    scene 11_2477 with Dissolve(1)
    ""
    scene 11_2478 with Dissolve(1)
    mc "And I would definitely wanna have sex with you!"
    la "..."
    mc "{i}(Why is she looking like that?){/i}"
    mc "{i}(Isn't that what she wanted to hear?){/i}"
    scene 11_2479 with Dissolve(1)
    la "I'm going to the bathroom."
    mc "Uhm... Okay."
    mc "{i}(Did I really say something wrong?){/i}"
    scene 11_2480 with Dissolve(1)
    mc "{i}(Normally I have a good sense of when I say something stupid.){/i}"
    mc "{i}(But this time... I have no idea.){/i}"
    scene black with Dissolve(1)
    pause 2
    scene 11_2481 with Dissolve(1)
    la "I've got us new drinks too."
    la "I didn't know what you wanted, so I got you another beer. Is that okay?"
    mc "That's fine, thanks."
    mc "{i}(Maybe I was just overthinking it and she really just needed to use the bathroom.){/i}"
    scene 11_2482 with Dissolve(1)
    mc "Two straws? Couldn't drink fast enough with one?"
    mc "{i}(I almost made a joke about that but...){/i}"
    la "Haha, no. If you didn't want a beer, I could share this with you."
    la "Want to try it?"
    mc "Yes."
    scene 11_2483 with Dissolve(1)
    mc "Mmm... It's good!"
    la "Hey!"
    la "Don't drink everything!"
    scene 11_2484 with Dissolve(1)
    la "..."
    mc "..."
    scene 11_2485 with Dissolve(1)
    mc "{i}(What is she thinking right now?){/i}"
    scene 11_2486 with Dissolve(1)
    la "..."
    scene 11_2487 with Dissolve(1)
    mc "..."
    la "[mc]! You sneaky thief!"
    la "You set me up!"
    scene 11_2488 with Dissolve(1)
    la "Look what you've done! You completely emptied it!"
    mc "Haha, sorry. I was lost in your eyes and just kept on drinking."
    scene 11_2489 with Dissolve(1)
    mc "Here. I'll share my beer with you."
    la "No, thanks."
    mc "I'll get you a new cocktail then."
    la "No, it's fine."
    scene 11_2490 with Dissolve(1)
    mc "You sure?"
    mc "The bar looks pretty empty at the moment. Will be quick."
    la "I didn't want to drink too much anyway today. I don't want to get as drunk as yesterday."
    scene 11_2491 with Dissolve(1)
    la "Oh, by the way. You'll never guess who I saw at the bar."
    mc "{i}(It's probably Gabi.){/i}"
    mc "Who?"
    scene 11_2492 with Dissolve(1)
    la "Ramirez!"
    mc "{i}(Haha. How her expression changed. She really doesn't like her.){/i}"
    if Gabi_End == False:
        mc "{i}(And if she knew what I'm doing with her, she'd hate me too. Even more so.){/i}"
    else:
        pass
    mc "Our Spanish teacher?"
    la "Yeah."
    scene 11_2493 with Dissolve(1)
    la "So weird to see a teacher in a club. Isn't she too old for that?"
    mc "I don't know. How old is she?"
    mc "{i}(I'm actually interested to know that.){/i}"
    la "I think it was twenty-seven or twenty-eight."
    mc "{i}(Younger than I thought.){/i}"
    mc "I'll still party when I'm that age. And there are lots of people here who are above thirty."
    scene 11_2494 with Dissolve(1)
    mc "It would've been more weird if you saw Mr Coleman here."
    la "Imagine..."
    mc "Would you go dance with him if he asked you?"
    la "Ew... No!"
    scene 11_2495 with Dissolve(1)
    la "But I'll dance with you!"
    mc "I should've never mentioned dancing..."
    la "Too late!"
    scene 11_2496 with Dissolve(1)
    la "Come on!"
    mc "Haha. Fine."
    scene 11_2497 with Dissolve(1)
    mc "{i}(She's acting differently to normal.){/i}"
    scene 11_2498 with Dissolve(1)
    mc "{i}(I don't know what it is exactly, but...){/i}"
    mc "{i}(Whatever. Let's just have fun.){/i}"
    scene 11_2499 with Dissolve(1)
    la "Haha."
    la "You're getting better at dancing."
    mc "You think?"
    scene 11_2500 with Dissolve(1)
    la "..."
    scene 11_2501 with Dissolve(1)
    mc "It's all because of you."
    mc "I'm just following your movements."
    scene 11_2502 with Dissolve(1)
    ""
    scene 11_2503 with Dissolve(1)
    mc "Uh..."
    scene 11_2504 with Dissolve(1)
    mc "{i}(Okay...){/i}"
    mc "{i}(Someone is wearing sexy lingerie.){/i}"
    scene 11_2505 with Dissolve(1)
    mc "You little tease!"
    la "Haha..."
    scene 11_2506 with Dissolve(1)
    mc "{i}(I think I love this girl!){/i}"
    scene 11_2507 with Dissolve(1)
    ""
    if Elena_LikeMC == True:
        scene 11_2508 with Dissolve(1)
        ""
        scene 11_2509 with Dissolve(1)
        mc "{i}(What the fuck?){/i}"
        mc "{i}(Why am I thinking about Elena right now?){/i}"
        scene 11_2510 with Dissolve(1)
        la "[mc]?"
        la "Are you okay? Looks like you saw a ghost or something."
        mc "{i}(Not a ghost...){/i}"
        mc "I'm good, I'm good."
    else:
        pass
    scene black with Dissolve(1)
    pause 2
    scene 11_2511 with Dissolve(1)
    mc "Normally I don't like dancing, but I'm really enjoying this today!"
    mc "Just for today. I'll dance with you for as long as you want!"
    scene 11_2512 with Dissolve(1)
    la "..."
    scene 11_2513 with Dissolve(1)
    la "[mc]..."
    mc "Hmm?"
    la "I wanna leave!"
    mc "Already? You sure?"
    la "*Nods*"
    scene 11_2514 with Dissolve(1)
    mc "{i}(We haven't even been here for an hour.){/i}"
    mc "Uhm... Okay. Let's leave."
    mc "{i}(She's really acting differently today.){/i}"
    scene 11_2515 with Dissolve(1)
    mc "Do you want to go somewhere else?"
    la "I want to go home."
    mc "..."
    mc "{i}(I don't get it.){/i}"

    scene black with Dissolve(1)
    pause 2
    stop music fadeout 1.0
    play music ("Music/LoFi Upbeat 1.mp3", "Music/LoFi Upbeat 2.mp3", "Music/LoFi Upbeat 3.mp3", "Music/LoFi Upbeat 4.mp3") volume 0.2
    scene 11_2516 with Dissolve(1)
    mc "{i}(She hasn't said a single thing since we left the club.){/i}"
    mc "{i}(I'm so confused...){/i}"
    mc "{i}(Did I do or say something wrong?){/i}"
    scene 11_2517 with Dissolve(1)
    la "..."
    mc "..."
    scene 11_2518 with Dissolve(1)
    mc "Uh..."
    mc "Are you okay, Layla?"
    la "*Nods*"
    la "*Shakes head*"
    mc "{i}(What?){/i}"
    scene 11_2519 with Dissolve(1)
    la "Do you want to come inside...?"
    la "..."
    la "To my room?"
    scene 11_2520 with Dissolve(1)
    mc "..."
    mc "{i}(Does she...?){/i}"
    mc "{i}(Now it all makes sense.){/i}"
    mc "{i}(Her behaviour... The nervousness...){/i}"
    if Elena_LikeMC == True:
        menu:
            "Go with Layla[KoGa3AutoWTChange1]{size=-4}(Layla Week5 Wednesday FirstTime, Layla Points+8, Layla Girlfriend) {/size} {/color}":
                $ Layla_Week5_Wednesday_FirstTime = True
                $ Layla_Points += 8
                $ Layla_Girlfriend = True
                # Layla (100)
                scene 11_2521 with Dissolve(1)
                mc "{i}(Is she really ready?){/i}"
                mc "You sure you want this?"
                la "*Nods*"
                scene 11_2522 with Dissolve(1)
                mc "{i}(Now I'm the one who's getting nervous.){/i}"
                mc "{i}(Layla's first time...){/i}"
                mc "..."
                mc "{i}(Get yourself together! Imagine how she must feel.){/i}"
                jump Week5_Wednesday_LaylaRoom
            "Elena[KoGa3AutoWTChange1]{size=-4}(Layla Week5 Wednesday LikeElenaKnow, Layla Week5 Wednesday BreakUp, Layla Points-30, Layla Friends, Layla DatingFalse) {/size} {/color}":
                $ Layla_Week5_Wednesday_LikeElenaKnow = True
                $ Layla_Week5_Wednesday_BreakUp = True
                $ Layla_Points -= 30
                $ Layla_Friends = True
                $ Layla_Dating = False
                stop music fadeout 1.0
                play music ("Music/Valeria - Emptiness.mp3", "Music/Slow4.mp3", "Music/Slow.mp3") volume 0.4
                scene 11_2523 with Dissolve(1)
                mc "{i}(Layla's amazing, she's beautiful, she's cute.){/i}"
                mc "{i}(I love spending time with her. The flirting, the kissing...){/i}"
                mc "{i}(But why can't I stop thinking about Elena now?){/i}"
                scene 11_2524 with Dissolve(1)
                la "..."
                mc "{i}(Fuck. If I'd figured out earlier what she had in mind, I wouldn't have...){/i}"
                mc "{i}(It's her first time. I like her too much to let her waste it on a guy who isn't one hundred per cent sure and is conflicted about someone else.){/i}"
                mc "{i}(That someone being her best friend...){/i}"
                mc "{i}(Her heart is beating so fast.){/i}"
                scene 11_2525 with Dissolve(1)
                mc "{i}(The way she's looking at me... She knows something's up.){/i}"
                mc "{i}(This is breaking my heart. And I'm about to break hers...){/i}"
                mc "{i}(I don't want to do this to her, but...){/i}"
                mc "Uhm..."
                scene 11_2526 with Dissolve(1)
                la "*Steps back*"
                mc "It's not that I don't like you or anything like that..."
                mc "I think you are absolutely amazing and..."
                mc "{i}(Am I making it worse by saying those things? Fuck...){/i}"
                scene 11_2527 with Dissolve(1)
                mc "There's someone else I like..."
                la "..."
                mc "{i}(Why isn't she saying anything?){/i}"
                mc "{i}(Probably because she's shocked about what she's hearing right now, you dumbass.){/i}"
                mc "{i}(Her supposed great day turned into a nightmare.){/i}"
                scene 11_2528 with Dissolve(1)
                mc "Layla, I'm sorry, I..."
                la "Who?"
                mc "Uhm..."
                la "Is it Valeria?"
                scene 11_2529 with Dissolve(1)
                mc "No. I like Elena."
                $ achievement.grant("ACHIEVEMENT_LAYLA_BREAKUP")
                $ achievement.sync()
                la "..."
                scene 11_2530 with Dissolve(1)
                mc "Layla, I..."
                la "Please, go home!"
                mc "Can..."
                la "Can you please go home?"
                mc "Yeah..."
                scene 11_2531 with Dissolve(1)
                mc "I'm so sorry, Layla. I never meant to hurt you."
                la "..."
                mc "I'm sorry."
                scene 11_2532 with Dissolve(1)
                mc "Fuck!"
                mc "Why do I always have to ruin the good things in my life?"
                scene black with Dissolve(1)
                pause 2
                scene 11_2533 with Dissolve(1)
                la "*Crying*"
                scene 11_2534 with Dissolve(1)
                a "Layla, are you..."
                la "*Crying*"
                a "Layla!"
                scene 11_2535 with Dissolve(1)
                la "Le... Lex... Lex..."
                la "*Crying*"
                scene 11_2536 with Dissolve(1)
                a "Come here!"
                a "What happened?"
                la "Is... Is there... something wrong... with... with me?"
                a "No! Of course not!"
                scene 11_2536a with Dissolve(1)
                la "*Crying*"
                a "I'm here."
                la "*Crying*"
                a "I'm here for you!"
                jump Week5_Wednesday_End
    else:
        $ Layla_Week5_Wednesday_FirstTime = True
        $ Layla_Girlfriend = True
        $ Layla_Points += 8
        # Layla (100)
        scene 11_2521 with Dissolve(1)
        mc "{i}(Is she really ready?){/i}"
        mc "You sure you want this?"
        la "*Nods*"
        scene 11_2522 with Dissolve(1)
        mc "{i}(Now I'm the one who's getting nervous.){/i}"
        mc "{i}(Layla's first time...){/i}"
        mc "..."
        mc "{i}(Get yourself together! Imagine how she must feel.){/i}"
        jump Week5_Wednesday_LaylaRoom

label Week5_Wednesday_LaylaRoom:
    if _in_replay:
        $ SexCounter_Layla = 0
        $ MC_SexCounter = 0
        $ Layla_Points = 100
    $ SexCounter_Layla += 1
    $ MC_SexCounter += 1
    scene black with Dissolve(1)
    pause 2
    scene 11_2537 with Dissolve(1)
    la "This is my room."
    mc "{i}(I've been to this house a few times already, but this is the first time I've been in her room.){/i}"
    mc "{i}(It's smaller than I expected. And...){/i}"
    scene 11_2538 with Dissolve(1)
    la "What do you think?"
    mc "Uhm..."
    mc "I expected it to be more... Hmm... Girly, I suppose?"
    la "Heh, yeah. It was. But when Alexis went to college, she redid her whole room."
    la "And I thought, why not do it now, too, since we're redecorating anyway."
    scene 11_2539 with Dissolve(1)
    mc "I really like that picture."
    mc "I'm looking for something to hang in my room since all my walls are pretty much empty."
    mc "Something like this would fit perfectly. Where did you get it?"
    la "I don't know. My dad bought it for me. I'll ask where he got it."
    mc "Thanks."
    scene 11_2540 with Dissolve(1)
    mc "What's in that room?"
    la "That's a closet."
    mc "Oh, like a walk-in closet?"
    la "Yes."
    scene 11_2541 with Dissolve(1)
    la "Well uhm... I'll be right back."
    la "You can have a look around if you want."
    mc "Will do."
    scene 11_2542 with Dissolve(1)
    mc "{i}(Let's have a quick look.){/i}"
    mc "{i}(It's a nice room.){/i}"
    mc "{i}(She even has her own TV.){/i}"
    scene 11_2543 with Dissolve(1)
    mc "..."
    mc "{i}(What's that? Pictures?){/i}"
    scene 11_2544 with Dissolve(1)
    mc "{i}(Heh... All kinds of pictures. Old and new.){/i}"
    mc "{i}(From training camp, even a few from the photo booth.){/i}"
    scene 11_2545 with Dissolve(1)
    mc "{i}(This must be from when Layla was on the cheerleading squad.){/i}"
    mc "{i}(Or maybe she just wore it for the picture? She said she still has the uniform.){/i}"
    mc "{i}(She should wear it more often. I hope she wears it for me again.){/i}"
    mc "{i}(Wait...){/i}"
    scene 11_2546 with Dissolve(1)
    mc "{i}(She had a dog?){/i}"
    mc "{i}(When was that? What kind of dog is that? A Dobermann?){/i}"
    mc "{i}(She looks so young here. Her hair was long too!){/i}"
    scene 11_2547 with Dissolve(1)
    mc "{i}(They had two dogs!){/i}"
    mc "{i}(They are huge.){/i}"
    mc "{i}(Adriana looking hot as always.){/i}"
    mc "{i}(But no chance of getting close to her with those bodyguards.){/i}"
    scene 11_2548 with Dissolve(1)
    mc "{i}(Young Layla and Elena.){/i}"
    mc "{i}(Layla has changed quite a bit, but Elena still looks the same. A little younger maybe?){/i}"
    mc "{i}(She must be a late bloomer... Or rather, an early bloomer.){/i}"
    mc "{i}(And she had a ponytail. It actually suits her.){/i}"
    mc "{i}(She also had that bitchy look already. Haha.){/i}"
    scene 11_2549 with Dissolve(1)
    la "..."
    scene 11_2550 with Dissolve(1)
    la "*Deep sigh*"
    scene black with Dissolve(1)
    pause 1
    scene 11_2551 with Dissolve(1)
    mc "{i}(Why is she standing there?){/i}"
    mc "{i}(Actually I don't mind. She looks so freakin' sexy.){/i}"
    mc "Come sit down here with me."
    la "..."
    scene 11_2552 with Dissolve(1)
    mc "{i}(She's so nervous.){/i}"
    mc "{i}(Which makes her that much cuter.){/i}"
    scene 11_2553 with Dissolve(1)
    mc "{i}(I can feel her whole body shivering.){/i}"
    mc "{i}(Does she really want to do this?){/i}"
    scene 11_2554 with Dissolve(1)
    mc "Don't force it, okay?"
    mc "We can stop at any time."
    scene 11_2555 with Dissolve(1)
    la "..."
    scene 11_2556 with Dissolve(1)
    mc "{i}(I'll try to slowly ease her into it.){/i}"
    scene 11_2557 with Dissolve(1)
    mc "{i}(As I say that...){/i}"
    mc "{i}(I'm already touching her boobs.){/i}"
    scene 11_2558 with Dissolve(1)
    ""
    scene 11_2559 with Dissolve(1)
    mc "{i}(This kiss feels different already.){/i}"
    mc "{i}(It's so weird that a kiss can change so much depending on the situation.){/i}"
    scene 11_2560 with Dissolve(1)
    mc "{i}(It's so much softer and more...){/i}"
    mc "{i}(Sensual...?){/i}"
    scene 11_2561 with Dissolve(1)
    la "..."
    scene 11_2562 with Dissolve(1)
    mc "{i}(She pulled away. Maybe this is going too fast for her?){/i}"
    mc "{i}(I'll slow down a bit more and get her more comfortable.){/i}"
    la "Should we put some music on?"
    mc "Whatever you prefer, Layla."
    la "Okay."
    scene 11_2563 with Dissolve(1)
    la "Let's see."
    la "I found something earlier."
    stop music fadeout 1.0
    play music "Sounds/Pornmusic.mp3" volume 0.4
    scene 11_2564 with Dissolve(1)
    la "What do you think of this one?"
    mc "{i}(She can't be serious?){/i}"
    mc "Haha."
    la "Why are you laughing?"
    scene 11_2565 with Dissolve(1)
    mc "You're actually serious?"
    mc "Where did you find that song?"
    mc "An eighties porn movie?"
    la "What no... I just googled songs when you are... going to... You know..."
    scene 11_2566 with Dissolve(1)
    mc "{i}(Your first time is not going to be to this song!){/i}"
    mc "Give me your phone. I'll look for something."
    la "Okay."
    stop music fadeout 1.0
    play music ("Music/Valeria - Peripheral.mp3", "Music/Valeria - The Last Train You Didn't Take.mp3") volume 0.4
    # Copyright NyxValeria
    scene 11_2567 with Dissolve(1)
    mc "How about this one?"
    la "I like it."
    mc "I'll just put up a playlist real quick."
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 11_2568 at moveup
    pause 3
    mc "{i}(She looks so perfect right now!){/i}"
    scene 11_2569 with Dissolve(1)
    mc "Have I told you already that you're looking so pretty today?"
    la "*Nods*"
    mc "Good! Just making sure."
    scene 11_2570 with Dissolve(1)
    ""
    scene 11_2571 with Dissolve(1)
    mc "Come here."
    scene 11_2572 with Dissolve(1)
    ""
    scene 11_2573 with Dissolve(1)
    ""
    scene 11_2574 with Dissolve(1)
    mc "{i}(She's taking the initiative now.){/i}"
    mc "{i}(I guess she's getting more comfortable.){/i}"
    scene 11_2575 with Dissolve(1)
    la "Mmm..."
    scene 11_2576 with Dissolve(1)
    la "..."
    scene 11_2577 with Dissolve(1)
    mc "{i}(Is it selfish of me that I never want anyone else to see those boobs?){/i}"
    scene 11_2578 with Dissolve(1)
    mc "{i}(They're mine now!){/i}"
    scene 11_2579 with Dissolve(1)
    ""
    scene 11_2580 with Dissolve(1)
    la "..."
    scene 11_2581 with Dissolve(1)
    mc "{i}(I hope she enjoys this as much as I do.){/i}"
    scene 11_2582 with Dissolve(1)
    la "Mmm..."
    la "[mc]..."
    scene black with Dissolve(1)
    pause 2
    scene 11_2583 with Dissolve(1)
    mc "Shall we take it off?"
    la "*Nods*"
    scene 11_2584 with Dissolve(1)
    la "Can you open the zipper for me?"
    mc "With pleasure!"
    la "Heh..."
    scene 11_2585 with Dissolve(1)
    mc "{i}(Damn...){/i}"
    scene 11_2586 with Dissolve(1)
    la "..."
    scene 11_2587 with Dissolve(1)
    mc "Teasing me again with that cute little ass of yours?"
    la "I'm not doing anything!"
    mc "Uh-huh."
    scene 11_2588 with Dissolve(1)
    la "Aaah..."
    mc "Come here, you!"
    la "Haha, [mc]!"
    scene 11_2589 with vpunch
    la "[mc]..."
    mc "Haha."
    scene 11_2590 with Dissolve(1)
    mc "Hey, pretty!"
    la "Hey..."
    scene 11_2591 with Dissolve(1)
    ""
    scene 11_2592 with Dissolve(1)
    la "Ahhh..."
    scene 11_2593 with Dissolve(1)
    mc "{i}(I can't stop playing with her boobs.){/i}"
    mc "{i}(And then those cute nipples of hers which are getting harder by the second...){/i}"
    scene 11_2594 with Dissolve(1)
    la "..."
    scene 11_2595 with Dissolve(1)
    mc "{i}(This is the second time she's stopping my hand now.){/i}"
    mc "{i}(But I think she's doing it subconsciously.){/i}"
    mc "{i}(Is her body telling her she's not ready yet?){/i}"
    scene 11_2596 with Dissolve(1)
    mc "{i}(Looks like she wants it, though.){/i}"
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 11_2597 at moveup
    pause 3
    mc "What an amazing view!"
    la "I think so too."
    scene 11_2598 with Dissolve(1)
    ""
    scene 11_2599 with Dissolve(1)
    ""
    scene 11_2600 with Dissolve(1)
    ""
    scene 11_2601 with vpunch
    la "Haha."
    mc "Do you think you can just keep on kissing me?"
    la "Yes!"
    mc "We'll see about that."
    scene 11_2602 with Dissolve(1)
    ""
    scene 11_2603 with Dissolve(1)
    la "..."
    scene 11_2604 with Dissolve(1)
    la "Mmm..."
    scene 11_2605 with Dissolve(1)
    la "Ahh... [mc]..."
    scene 11_2606 with Dissolve(1)
    la "*Moaning*"
    scene 11_2607 with Dissolve(1)
    mc "{i}(I'll slowly work myself downwards.){/i}"
    scene 11_2608 with Dissolve(1)
    mc "{i}(I can feel her tensing up again.){/i}"
    scene 11_2609 with Dissolve(1)
    ""
    scene 11_2610 with Dissolve(1)
    mc "Can I remove your panties?"
    la "..."
    la "*Nods*"
    scene 11_2611 with Dissolve(1)
    mc "{i}(She looks so embarrassed...){/i}"
    mc "{i}(She's even blushing.){/i}"
    mc "{i}(So cute! Why is she so cute?){/i}"
    scene 11_2612 with Dissolve(1)
    mc "If you're too uncomfortable, we can stop, okay?"
    la "..."
    mc "Do you wanna stop?"
    la "*Shakes head*"
    scene 11_2613 with Dissolve(1)
    mc "{i}(I'm getting more and more excited myself.){/i}"
    scene 11_2614 with Dissolve(1)
    mc "Can't I see?"
    la "No."
    mc "Why not?"
    la "It's embarrassing!"
    scene 11_2615 with Dissolve(1)
    mc "Why is it embarrassing?"
    la "I don't know."
    la "..."
    la "Just for a second, okay?"
    mc "Okay!"
    show 11_2616
    pause 5
    ""
    scene 11_2617 with Dissolve(1)
    mc "It's beautiful."
    la "Don't say that!"
    mc "It is though."
    la "..."
    scene 11_2618 with Dissolve(1)
    mc "You can watch too."
    la "I don't want to see!"
    mc "Haha."
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 11_2619 at moveup
    pause 3
    mc "{i}(Every time I look at her, she gets cuter...){/i}"
    mc "{i}(If she knew how much she's turning me on right now...){/i}"
    scene 11_2620 with Dissolve(1)
    la "*Shakes*"
    mc "Sorry. I didn't wanna scare you."
    mc "{i}(I might actually get as nervous as she is.){/i}"
    mc "{i}(I wanna taste her so bad.){/i}"
    scene 11_2621 with Dissolve(1)
    mc "{i}(Her legs, her thighs, her...){/i}"
    scene 11_2622 with Dissolve(1)
    la "..."
    la "[mc]! You are... My..."
    scene 11_2623 with Dissolve(1)
    la "Ahh..."
    mc "{i}(That cute little moan!){/i}"
    mc "{i}(I think she likes this.){/i}"
    scene 11_2624 with Dissolve(1)
    la "*Moaning*"
    scene 11_2625 with Dissolve(1)
    la "Ahhh... Mmm..."
    mc "{i}(Found the spot.){/i}"
    scene 11_2626 with Dissolve(1)
    la "[mc]... [mc]..."
    la "Haah..."
    scene 11_2627 with Dissolve(1)
    mc "{i}(She's even pushing her pussy into my face now.){/i}"
    scene 11_2628 with Dissolve(1)
    la "*Moaning*"
    mc "{i}(She just...){/i}"
    scene 11_2629 with Dissolve(1)
    la "*Breathing heavily*"
    mc "You okay? You're breathing fast."
    scene 11_2630 with Dissolve(1)
    la "..."
    mc "Why are you so happy?"
    la "Stop looking at me!"
    mc "Haha."
    scene 11_2631 with Dissolve(1)
    mc "Did you enjoy that?"
    la "*Nods*"
    la "Can you do that again?"
    mc "As many times as you want!"
    scene 11_2632 with Dissolve(1)
    ""
    scene 11_2633 with Dissolve(1)
    mc "How about this?"
    la "Mmm..."
    scene 11_2634 with Dissolve(1)
    la "Ahh..."
    scene 11_2635 with Dissolve(1)
    ""
    scene black with Dissolve(1)
    pause 2
    scene 11_2636 with Dissolve(1)
    mc "Are you ready?"
    la "*Nods*"
    mc "I'm gonna put it in then."
    la "..."
    scene 11_2637 with Dissolve(1)
    la "Wait! Is it gonna hurt?"
    mc "For some it does, for others, it doesn't."
    mc "I'll be going very slow, okay?"
    scene 11_2638 with Dissolve(1)
    mc "{i}(The moment...){/i}"
    scene 11_2639 with Dissolve(1)
    mc "{i}(I can't push it in further without pressing too hard.){/i}"
    mc "{i}(She's way too tense.){/i}"
    scene 11_2640 with Dissolve(1)
    mc "Layla, you'll need to relax a little. Or else I can't put it in."
    la "..."
    la "I'm trying but..."
    mc "Let's try something different then. Can you turn on your side? It might be easier that way."
    scene 11_2641 with Dissolve(1)
    mc "Are you comfortable lying like this?"
    la "*Nods*"
    show 11_2642
    pause 3
    la "..."
    show 11_2643
    pause 2
    ""
    scene 11_2644 with Dissolve(1)
    mc "..."
    mc "{i}(She's tearing up.){/i}"
    mc "I'm so sorry. Does it hurt much?"
    la "A little."
    mc "Sorry."
    scene 11_2645 with Dissolve(1)
    la "..."
    scene 11_2646 with Dissolve(1)
    mc "I'm gonna start uhm... moving, slowly."
    mc "It will be a little sore at first but it will feel better in a while."
    la "*Nods*"
    show 11_2647
    la "..."
    show 11_2648
    la "..."
    scene 11_2649 with Dissolve(1)
    mc "{i}(She still has pain written all over her face.){/i}"
    mc "{i}(I hope it will fade away soon.){/i}"
    mc "Is this okay?"
    la "*Nods*"
    scene 11_2650 with Dissolve(1)
    ""
    scene black with Dissolve(1)
    pause 2
    scene 11_2651 with Dissolve(1)
    mc "Let's try this again."
    mc "I want to see your pretty face."
    mc "{i}(I also had to switch positions because I was about to cum already. She's so tight, it's amazing.){/i}"
    scene 11_2652 with Dissolve(1)
    la "Aaah..."
    mc "Sorry."
    show 11_2653
    la "..."
    show 11_2654
    mc "{i}(Her expression is slowly changing.){/i}"
    mc "{i}(Seems like she's starting to enjoy it somewhat.){/i}"
    scene 11_2655 with Dissolve(1)
    mc "Is it starting to feel better for you?"
    la "*Nods*"
    show 11_2656
    la "*Moaning*"
    show 11_2657
    la "*Moaning*"
    mc "{i}(I can't hold it much longer...){/i}"
    scene 11_2658 with vpunch
    pause 2
    scene 11_2658 with vpunch
    mc "Ahh..."
    la "..."
    scene 11_2659 with Dissolve(1)
    la "*Heavy breathing*"
    mc "*Heavy breathing*"
    mc "Are you okay?"
    la "*Nods* Yeah. Did you...?"
    mc "Yeah."
    la "I could feel it... Inside me."
    scene 11_2660 with Dissolve(1)
    ""
    scene black with Dissolve(1)
    pause 2
    scene 11_2661 with Dissolve(1)
    mc "How are you feeling?"
    la "Happy."
    la "And a little sad."
    scene 11_2662 with Dissolve(1)
    mc "Sad? Why are you feeling sad?"
    la "I don't know."
    la "Maybe because... No, I don't know."
    menu:
        "Joke[KoGa3AutoWTChange1]{size=-4}(Layla Points-4) {/size} {/color}":
            $ Layla_Points -= 4
            scene 11_2663 with Dissolve(1)
            mc "Maybe you're sad because you've lost something."
            la "I didn't lose anything. What do you mean? Are you talking about my hoodie?"
            mc "No, your virginity!"
            la "..."
            mc "Sorry. Terrible joke."
        "Was it good?":
            pass
    scene 11_2664 with Dissolve(1)
    mc "But it was good for you, right?"
    la "I think."
    la "I have nothing to compare it to."
    mc "Haha. True."
    scene 11_2665 with Dissolve(1)
    la "I'm kidding."
    la "It was amazing!"
    la "I couldn't be happier!"
    mc "Me too."
    scene 11_2666 with Dissolve(1)
    la "Uhm... [mc]..."
    mc "Hmm?"
    la "Was... Was I good?"
    scene 11_2667 with Dissolve(1)
    mc "You were perfect!"
    mc "You're really good at sex! You know that?"
    la "Haha. Stop!"
    scene 11_2668 with Dissolve(1)
    la "But really?"
    mc "Yeah!"
    mc "Little cutie you!"
    la "..."
    scene 11_2669 with Dissolve(1)
    la "Are you staying here tonight?"
    mc "I want to, but I can't. I have to work tomorrow. Sorry."
    mc "But I'll stay until you fall asleep."
    la "Then I won't go to sleep for a while."
    mc "Heh..."
    scene 11_2670 with Dissolve(1)
    mc "{i}(This was really amazing!){/i}"
    mc "{i}(Can't wait to have sex with her regularly.){/i}"
    scene black with Dissolve(1)
    pause 2
    scene 11_2671 with Dissolve(1)
    mc "*Whispers* Layla?"
    mc "{i}(It didn't take that long.){/i}"
    scene 11_2672 with Dissolve(1)
    mc "{i}(I hope this day was everything you hoped for.){/i}"
    mc "*Whispers* Good night, cutie!"
    scene 11_2673 with Dissolve(1)
    mc "..."
    scene black with Dissolve(2)
    pause 2
    stop music fadeout 1.0
    play music ("Music/LoFi Upbeat 1.mp3", "Music/LoFi Upbeat 2.mp3", "Music/LoFi Upbeat 3.mp3", "Music/LoFi Upbeat 4.mp3") volume 0.2
    n "Thursday, 10:07."
    scene 11_2674 with Dissolve(1)
    la "*Yawn* Nggh..."
    scene 11_2675 with Dissolve(1)
    la "*Smiling*"
    scene 11_2676 with Dissolve(1)
    la "..."
    scene 11_2677 with Dissolve(1)
    la "..."
    scene 11_2678 with vpunch
    la "*Muffled* KYAAA!"
    scene 11_2679 with Dissolve(1)
    n "*Knock-knock*"
    a "Lays? Are you awake?"
    la "Yes."
    a "If you want to come with to the airport, you'll need to get ready!"
    la "Give me a few minutes."
    $ renpy.end_replay()
    scene black with Dissolve(1)
    pause 2
    scene 11_2680 with Dissolve(1)
    am "Layla?"
    la "I'm in the bathroom."
    am "I'm doing laundry. Do you have anything that needs to be washed?"
    la "Uh... My black dress."
    am "The one that's lying on the floor?"
    la "Uh-huh..."
    scene 11_2681 with Dissolve(1)
    am "*Sigh*"
    am "At least hang it over a chair or something!"
    am "Now it's all wrinkled up!"
    am "*Shakes head* This girl..."
    scene 11_2682 with Dissolve(1)
    am "How about your bedsheets?"
    am "Do they need to be washed?"
    la "Yes. You can take them too."
    scene 11_2683 with Dissolve(1)
    am "..."
    scene 11_2684 with Dissolve(1)
    am "What is this?"
    am "Blood?"
    am "{i}(She's on the same cycle as me... So...){/i}"
    scene 11_2685 with Dissolve(1)
    la "Oh..."
    la "You're still here. Did you need something else?"
    am "..."
    scene 11_2686 with Dissolve(1)
    la "Uh..."
    am "Are you okay?"
    la "What?"
    am "Are you okay, Layla?"
    scene 11_2687 with Dissolve(1)
    la "..."
    la "How do you even know?"
    am "I'm your mother!"
    scene 11_2688 with Dissolve(1)
    am "Are you okay? Are you hurting?"
    la "I'm good. Maybe a little sore."
    am "Was it your choice?"
    la "Yes. He..."
    scene 11_2689 with Dissolve(1)
    am "[mc]?"
    la "..."
    la "Yes."
    am "How was it?"
    scene 11_2690 with Dissolve(1)
    la "Mom... I can't tell you that."
    am "Why not?"
    la "Because..."
    scene 11_2691 with Dissolve(1)
    la "I need to get ready. Lexi's waiting for me."
    am "We'll talk later, then."
    la "..."
    scene 11_2692 with Dissolve(1)
    la "Mom?"
    am "Hmm?"
    la "Please don't tell Dad."
    scene black with Dissolve(1)
    pause 2
    scene 11_2693 with Dissolve(1)
    x "Why do you look so sad?"
    am "It's nothing. I was just thinking how fast those two grew up."
    x "They did, huh?"
    am "They were just little girls a while ago. And next year, Layla will be off to college, too..."
    am "*Sigh*"
    scene 11_2694 with Dissolve(1)
    x "You want another one?"
    am "What? Don't joke about that."
    x "Who says I'm joking?"
    x "We always talked about having three."
    am "..."
    jump Week5_Wednesday_End

label Week5_Wednesday_End:
    jump Episode_12_Start

# Max Points:

# Alexis (46)
# Melissa (18)
# Layla (100)
# Elena (48)
# Emily (22)
# Erynn (60)
# Tori (18)
# Cara (16)
# Nikki (20)
# Lakeyn (6)
# Brooke (6)
# Adriana (6)
# Naomi (2)
# Valeria (26)
# Zach (10)
# Darryl (4)
# ShaCarri (4)
# Iris (2)
# Sienna (4)

# MC_GoodStudent (14)

# Nikki_Weekend (10)
# Nikki_Visit (40)
# Cara_Weekend (6)
# Cara_Visit (44)
# Alexis_SP (20)
# Alexis_Jealous (16)
# Alexis_Beach (16)

# MC_Sex (35)
# Alexis_Sex (9)
# Tori_Sex (3)
# Lakeyn_Sex (1)
# Nikki_Sex (6)
# Cara_Sex (7)
# Julia_Sex (1)
# Rachel_Sex (1)
# Gabi_Sex (3)
# Iris_Sex (3)
# Layla_Sex (1)

#WTAdded
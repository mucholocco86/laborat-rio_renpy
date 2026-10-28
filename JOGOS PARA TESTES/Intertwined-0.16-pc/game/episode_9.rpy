label Episode_9_Start:

    #KoGa3 START#
    $ KoGa3GameProgress = "Ep9"
    #KoGa3 END#

    $ achievement.grant("ACHIEVEMENT_EPISODE_8")
    $ achievement.sync()
    $ Layla_End = False
    $ Elena_End = False
    $ Nikki_Solo = False
    $ Nikki_Visit = False
    $ Nikki_MeetEmily = False
    $ Cara_Solo = False
    $ Cara_Visit = False
    $ Cara_MeetEmily = False
    $ Cara_Week4_Wednesday_Visit_Breakup = False
    $ Nikki_Week4_Wednesday_Visit_Breakup = False
    $ Alexis_RiversideStory = False
    $ Iris_FB_Outfit_DontLike = False
    $ Nikki_Week4_Wednesday_Visit_Knows = False
    $ Cara_Week4_Wednesday_Visit_Knows = False
    $ MC_Week4_Wednesday_BedOccupied = False
    $ MC_Week4_Thursday_SleepInEmilyBed = False
    $ MC_Girlfriend_Riverside = False
    $ Layla_Week4_Thursday_Val_NakedRun = False
    $ Layla_Week4_Thursday_HoldPenis = False
    $ Tori_Week3_Thursday_School_HJ = False
    $ Layla_Week4_Thursday_Val_NakedRun = False
    $ Layla_Week4_Thursday_WingmanVal = False
    $ Tori_Week4_Thursday_SeeNikki = False
    $ Tori_Week4_Thursday_SeeCara = False
    $ Mike_Week4_Thursday_NikkiCaraDad = False
    $ Nikki_Week4_Thursday_Swimsuit_Option1_Like = False
    $ Nikki_Week4_Thursday_ArmwrestlingWin = False
    $ Nikki_Week4_Thursday_Lotion = False
    $ Nikki_Week4_Thursday_LotionMC = False
    $ Nikki_Week4_Thursday_Handstand_Help = False
    $ Naomi_Week4_Thursday_Watch = False
    $ Cara_Week4_Thursday_Dress_Like = False
    $ Cara_Week4_Thursday_Dress_Sex = False
    $ Valeria_Week4_Thursday_MeetNikki = False
    $ Valeria_Week4_Friday_Help = False

    if Andres_FB_Punch == True:
        jump Week4_Wednesday_Evening2
    else:
        if Nikki_Girlfriend == True:
            $ Nikki_Visit = True
            $ Nikki_MeetEmily = True
            $ MC_Week4_Wednesday_BedOccupied = True
            jump Week4_Wednesday_Nikki
        else:
            if Cara_Girlfriend == True:
                $ Cara_Visit = True
                $ Cara_MeetEmily = True
                $ MC_Week4_Wednesday_BedOccupied = True
                jump Week4_Wednesday_Cara
            else:
                jump Week4_Wednesday_Evening2

label Week4_Wednesday_Evening2:
    scene black with Dissolve(1)
    pause 2
    scene 09_058 with Dissolve(1)
    mc "Here's your package."
    m "Thank you."
    scene 09_059 with Dissolve(1)
    mc "What did you order?"
    m "Why are you so curious?"
    mc "I'm not..."
    m "It's not for you!"
    if Alexis_Dating == True:
        if Layla_Week3_Wednesday_TC_Alexis_DateBoth == True:
            $ Alexis_End = True
            $ Alexis_Friends = True
            $ Alexis_Dating = False
            $ Layla_End = True
            $ Layla_Friends = True
            $ Layla_Dating = False
            $ Elena_End = True
            $ Valeria_Friends = True
            $ Valeria_Points -= 6
            n "*Ding-dong*"
            scene 09_060 with Dissolve(1)
            stop music fadeout 1.0
            play music "Music/Valeria - Emptiness.mp3" volume 0.5
            mc "Another package?"
            m "Can you go check, please?"
            mc "You are so secretive... Who knows what this is."
            m "It's... No, you know what? I'm not telling you."
            scene 09_061 with Dissolve(1)
            mc "Pssh... Don't tell me, like I care. I'm not losing sleep over not knowing!"
            m "Haha."
            scene black with Dissolve(1)
            transform moveup:
                xalign 0.5 yalign 1.0
                linear 5.0 yalign 0.0
            show 09_036 at moveup
            pause 3
            mc "Lexi!"
            mc "Hey, what are you doing here?"
            scene 09_037 with Dissolve(1)
            a "..."
            mc "What's wrong? Why aren't you saying anything?"
            scene 09_038 with Dissolve(1)
            mc "{i}(Oh shit.){/i}"
            $ achievement.grant("ACHIEVEMENT_THINK_HAPPEN")
            $ achievement.sync()
            if Zach_Week3_Wednesday_TC_Girlshower == False:
                mc "{i}(I knew I should've said something during training camp. What did I expect?){/i}"
            else:
                mc "{i}(I guess Layla told her, after all.){/i}"
            scene 09_039 with Dissolve(1)
            la "You... You... I..."
            a "I'll take it from here."
            scene 09_040 with Dissolve(1)
            a "You are a disgusting piece of shit!"
            a "How long did you think you could keep this up for before we found out?"
            mc "I..."
            scene 09_041 with Dissolve(1)
            a "She's my sister!"
            mc "Let me explain, please."
            a "What is there to explain? You fool around with the both of us until you decide who does it better?"
            mc "No, I..."
            scene 09_042 with Dissolve(1)
            a "What, [mc]? What?"
            mc "..."
            a "Stay away, and don't you ever talk to us again."
            scene 09_043 with Dissolve(1)
            a "Come on, Layla. Let's go home. He isn't worth any more of our time."
            la "..."
            a "Fucking asshole!"
            scene black with Dissolve(1)
            pause 2
            scene 09_044 with Dissolve(1)
            mc "{i}(Fuck...){/i}"
            mc "{i}(It's because I like both of you and I didn't want to hurt anyone...){/i}"
            mc "{i}(Who am I kidding? I knew exactly how this would turn out.){/i}"
            jump Week4_Wednesday_Emily2
        else:
            play sound "Sounds/Phone_Vibrate.mp3"
            n "*Bzzzt. Bzzzt*"
            scene 09_060 with Dissolve(1)
            m "Go answer your phone instead."
            mc "You are so secretive... Who knows what this is."
            m "It's... No, you know what? I'm not telling you."
            scene 09_061 with Dissolve(1)
            mc "Pssh... Don't tell me, like I care. I'm not losing sleep over not knowing!"
            m "Haha."
            scene black with Dissolve(1)
            pause 2
            scene 09_046 with Dissolve(1)
            mc "Hi. How are you?"
            a "Hey. I'm good."
            scene 09_047 with Dissolve(1)
            a "How are you?"
            mc "Good, good."
            a "What are you doing?"
            mc "Nothing much. Was at a garage today, looking at cars."
            scene 09_049 with Dissolve(1)
            a "I heard. And you met Iris again."
            mc "..."
            mc "I did."
            scene 09_050 with Dissolve(1)
            a "What a coincidence! Her words."
            mc "Tell me about it."
            a "..."
            a "Hey! Want to come over?"
            scene 09_051 with Dissolve(1)
            mc "I want to, but it will take me some time to get there. And I won't be able to stay that long."
            a "I'm not at the dorm. I'm home."
            mc "Oh... Because of Iris? She said you guys made up."
            a "We did. I just wanted to be alone to think."
            scene 09_052 with Dissolve(1)
            a "So, is that a yes?"
            mc "It's a yes. But aren't your parents home?"
            a "They are."
            mc "Do they know... about us?"
            a "No, I haven't told them yet. But don't worry, I'll sneak you in."
            mc "Heh... Okay."
            scene 09_053 with Dissolve(1)
            mc "I'll be there in twenty to twenty-five minutes?"
            a "Perfect. Call me once you're here."
            mc "Alright. See you soon."
            jump Week4_Wednesday_Alexis
    else:
        scene 09_060 with Dissolve(1)
        mc "You are so secretive... Who knows what this is."
        m "It's... No, you know what? I'm not telling you."
        scene 09_061 with Dissolve(1)
        mc "Pssh... Don't tell me, like I care. I'm not losing sleep over not knowing!"
        m "Haha."
        jump Week4_Wednesday_Emily2

label Week4_Wednesday_Nikki:
    if Alexis_Dating == False:
        if Layla_Dating == False:
            $ Nikki_Solo = True
            $ MC_Girlfriend_Riverside = True
        else:
            $ Nikki_Solo = False
    else:
        $ Nikki_Solo = False
    scene 09_001 with Dissolve(1)
    mc "Nikki!"
    mc "Uhm... Wha... What are you doing here?"
    scene 09_002 with Dissolve(1)
    ni "..."
    ni "I..."
    m "You can bring it into the living room."
    scene 09_003 with Dissolve(1)
    mc "No, it's not the delivery."
    m "Who was it?"
    mc "Uh..."
    scene 09_004 with Dissolve(1)
    m "Hello."
    ni "Hi, Emily."
    mc "Mom. This is Nikki."
    m "Oh... Haley's Nikki? From Riverside?"
    mc "Yes."
    scene 09_005 with Dissolve(1)
    m "Don't just stand outside, sweetheart. Come on in."
    m "Invite her in next time, [mc]! And get her suitcase!"
    scene black with Dissolve(1)
    pause 2
    scene 09_006 with Dissolve(1)
    m "Let me have a good look at you."
    m "You are gorgeous, Nikki!"
    ni "Thank you."
    m "Please have a seat. Can I get you anything?"
    scene 09_007 with Dissolve(1)
    ni "Uhm..."
    m "Coffee, tea?"
    ni "A water, maybe?"
    m "Of course."
    ni "Thank you."
    scene 09_008 with Dissolve(1)
    mc "Hi."
    ni "Hey."
    scene 09_009 with Dissolve(1)
    mc "I'm sorry about... before... at the door."
    mc "I was expecting a delivery guy and then... Well, you were standing there."
    scene 09_010 with Dissolve(1)
    mc "Why did you come here?"
    ni "..."
    ni "I... I don't know. I thought..."
    m "Here you go."
    scene 09_011 with Dissolve(1)
    ni "Thank you, Emily."
    m "You're welcome."
    scene 09_012 with Dissolve(1)
    m "Can you scoot over a bit, [mc]?"
    mc "Uhm, yeah..."
    scene 09_013 with Dissolve(1)
    mc "..."
    ni "..."
    scene 09_014 with Dissolve(1)
    m "[mc] didn't tell me you were coming to visit."
    ni "He didn't know. It was... a spur of the moment thing."
    ni "I should've called beforehand. I'm sorry for the inconvenience."
    m "No-no-no, nothing like that. I'm glad you are here, I always wanted to meet you."
    scene 09_015 with Dissolve(1)
    m "Haley knows you're here?"
    ni "Yes, she does."
    if Alexis_Dating == True:
        if Layla_Week3_Wednesday_TC_Alexis_DateBoth == True:
            $ Alexis_End = True
            $ Alexis_Friends = True
            $ Alexis_Dating = False
            $ Layla_End = True
            $ Layla_Friends = True
            $ Layla_Dating = False
            $ Elena_End = True
            $ Valeria_Friends = True
            $ Valeria_Points -= 6
            n "*Ding-dong*"
            stop music fadeout 1.0
            play music "Music/Valeria - Emptiness.mp3" volume 0.5
            scene 09_016 with Dissolve(1)
            m "Oh, that must be the delivery."
            mc "I'll get it."
            scene 09_018 with Dissolve(1)
            m "..."
            scene black with Dissolve(1)
            pause 2
            scene black with Dissolve(1)
            transform moveup:
                xalign 0.5 yalign 1.0
                linear 5.0 yalign 0.0
            show 09_036 at moveup
            pause 3
            mc "Lexi!"
            mc "Hey, what are you doing here?"
            scene 09_037 with Dissolve(1)
            a "..."
            mc "What's wrong? Why aren't you saying anything?"
            scene 09_038 with Dissolve(1)
            mc "{i}(Oh shit.){/i}"
            $ achievement.grant("ACHIEVEMENT_THINK_HAPPEN")
            $ achievement.sync()
            mc "{i}(I knew I should've said something during training camp. What did I expect?){/i}"
            scene 09_039 with Dissolve(1)
            la "You... You... I..."
            a "I'll take it from here."
            scene 09_040 with Dissolve(1)
            a "You are a disgusting piece of shit!"
            a "How long did you think you could keep this up for before we found out?"
            mc "I..."
            scene 09_041 with Dissolve(1)
            a "She's my sister!"
            mc "Let me explain, please."
            a "What is there to explain? You fool around with the both of us until you decide who does it better?"
            mc "No, I..."
            scene 09_042 with Dissolve(1)
            a "What, [mc]? What?"
            mc "..."
            a "Stay away, and don't you ever talk to us again."
            scene 09_043 with Dissolve(1)
            a "Come on, Layla. Let's go home. He isn't worth any more of our time."
            la "..."
            a "Fucking asshole!"
            scene black with Dissolve(1)
            pause 2
            scene 09_044 with Dissolve(1)
            mc "{i}(Fuck...){/i}"
            mc "{i}(It's because I like both of you and I didn't want to hurt anyone...){/i}"
            mc "{i}(Who am I kidding? I knew exactly how this would turn out.){/i}"
            scene 09_045 with Dissolve(1)
            x "Good evening. I have a parcel for an Emily Vicari."
            mc "Yes, I'll take it."
            x "Can you sign here, please?"
            scene black with Dissolve(1)
            pause 2
            scene 09_054 with Dissolve(1)
            ni "*Crying*"
            mc "{i}(What happened here? Why is she crying?){/i}"
            mc "Uhm..."
            scene 09_055 with Dissolve(1)
            m "Give us a moment, [mc]."
            mc "Okay?"
            mc "I'll be in my room. I left the package in the kitchen."
            m "Thanks."
            mc "{i}(Seriously, what's going on?){/i}"
            scene black with Dissolve(1)
            pause 2
            scene 09_512 with Dissolve(1)
            mc "{i}(It's been an hour already. I guess I'll check up on them.){/i}"
            jump Week4_Wednesday_Nikki2
        else:
            play sound "Sounds/Phone_Vibrate.mp3"
            n "*Bzzzt. Bzzzt*"
            scene 09_017 with Dissolve(1)
            mc "Oh, give me a sec, I need to take this."
            mc "Be right back."
            scene 09_018 with Dissolve(1)
            m "..."
            scene black with Dissolve(1)
            pause 2
            scene 09_046 with Dissolve(1)
            mc "Hi. How are you?"
            a "Hey. I'm good."
            scene 09_047 with Dissolve(1)
            a "How are you?"
            mc "Good, good."
            a "What are you doing?"
            mc "Nothing much. Was at a garage today, looking at cars."
            scene 09_049 with Dissolve(1)
            a "I heard. And you met Iris again."
            mc "..."
            mc "I did."
            scene 09_050 with Dissolve(1)
            a "What a coincidence! Her words."
            mc "Tell me about it."
            a "..."
            a "Hey! Want to come over?"
            scene 09_051 with Dissolve(1)
            mc "I want to, but it will take me some time to get there. And I won't be able to stay that long."
            a "I'm not at the dorm. I'm home."
            mc "Oh... Because of Iris? She said you guys made up."
            a "We did. I just wanted to be alone to think."
            scene 09_052 with Dissolve(1)
            a "So, is that a yes?"
            mc "It's a yes. But aren't your parents home?"
            a "They are."
            mc "Do they know... about us?"
            a "No, I haven't told them yet. But don't worry, I'll sneak you in."
            mc "Heh... Okay."
            scene 09_053 with Dissolve(1)
            mc "I'll be there in twenty to twenty-five minutes?"
            a "Perfect. Call me once you're here."
            mc "Alright. See you soon."
            scene black with Dissolve(1)
            pause 2
            scene 09_054 with Dissolve(1)
            ni "*Crying*"
            mc "{i}(What happened here? Why's she crying?){/i}"
            mc "Uhm..."
            scene 09_055 with Dissolve(1)
            m "Give us a moment, [mc]."
            mc "Okay?"
            mc "I need to go somewhere. I'll be back a little later."
            m "Thanks."
            mc "{i}(Seriously, what's going on?){/i}"
            jump Week4_Wednesday_Alexis
    else:
        n "*Ding-dong*"
        scene 09_016 with Dissolve(1)
        m "Oh, that must be the delivery."
        mc "I'll get it."
        scene 09_018 with Dissolve(1)
        m "..."
        scene 08_2367 with Dissolve(1)
        x "Good evening, I have a parcel for an Emily Vicari."
        mc "Yes, I'll take it."
        scene black with Dissolve(1)
        pause 2
        scene 09_054 with Dissolve(1)
        ni "*Crying*"
        mc "{i}(What happened here? Why's she crying?){/i}"
        mc "Uhm..."
        scene 09_055 with Dissolve(1)
        m "Give us a moment, [mc]."
        mc "Okay?"
        mc "I'll be in my room. I left the package in the kitchen."
        m "Thanks."
        mc "{i}(Seriously, what's going on?){/i}"
        scene black with Dissolve(1)
        pause 2
        scene 09_512 with Dissolve(1)
        mc "{i}(It's been an hour already. I guess I'll check up on them.){/i}"
        jump Week4_Wednesday_Nikki2

label Week4_Wednesday_Cara:
    if Alexis_Dating == False:
        if Layla_Dating == False:
            $ Cara_Solo = True
            $ MC_Girlfriend_Riverside = True
        else:
            $ Cara_Solo = False
    else:
        $ Cara_Solo = False
    scene 09_019 with Dissolve(1)
    mc "Cara!"
    mc "Uhm... Wha... What are you doing here?"
    scene 09_020 with Dissolve(1)
    c "..."
    c "I..."
    m "You can bring it into the living room."
    scene 09_021 with Dissolve(1)
    mc "No, it's not the delivery."
    m "Who was it?"
    mc "Uh..."
    scene 09_022 with Dissolve(1)
    m "Hello."
    c "Hi, Emily."
    mc "Mom. This is Cara."
    m "Oh... Haley's Cara? From Riverside?"
    mc "Yes."
    scene 09_023 with Dissolve(1)
    m "Don't just stand outside, sweetheart. Come on in."
    m "Invite her in next time, [mc]! And get her suitcase!"
    scene black with Dissolve(1)
    pause 2
    scene 09_024 with Dissolve(1)
    m "Let me have a good look at you."
    m "You are so beautiful, Cara!"
    c "Thank you."
    m "Please have a seat. Can I get you anything?"
    scene 09_025 with Dissolve(1)
    c "Uhm..."
    m "Coffee, tea?"
    c "I'm good, thank you."
    scene 09_026 with Dissolve(1)
    mc "Hi."
    c "Hey."
    scene 09_027 with Dissolve(1)
    mc "I'm sorry about... before... at the door."
    mc "I was expecting a delivery guy and then... Well, you were standing there."
    scene 09_028 with Dissolve(1)
    mc "Why did you come here?"
    c "..."
    c "I... I don't know. I thought..."
    scene 09_029 with Dissolve(1)
    m "Can I join you?"
    mc "Sure..."
    scene 09_030 with Dissolve(1)
    m "Can you scoot over a bit, [mc]?"
    mc "Uhm, yeah."
    scene 09_031 with Dissolve(1)
    mc "..."
    c "..."
    scene 09_032 with Dissolve(1)
    m "[mc] didn't tell me you were coming to visit."
    c "He didn't know. It was... a spur of the moment thing."
    c "I should've called beforehand. I'm sorry for the inconvenience."
    m "No-no-no, nothing like that. I'm glad you're here, I always wanted to meet you."
    scene 09_033 with Dissolve(1)
    m "Haley knows you're here?"
    c "Yes, she does."
    if Alexis_Dating == True:
        if Layla_Week3_Wednesday_TC_Alexis_DateBoth == True:
            $ Alexis_End = True
            $ Alexis_Friends = True
            $ Alexis_Dating = False
            $ Layla_End = True
            $ Layla_Friends = True
            $ Layla_Dating = False
            $ Elena_End = True
            $ Valeria_Friends = True
            $ Valeria_Points -= 6
            n "*Ding-dong*"
            stop music fadeout 1.0
            play music "Music/Valeria - Emptiness.mp3" volume 0.5
            scene 09_016 with Dissolve(1)
            m "Oh, that must be the delivery."
            mc "I'll get it."
            scene 09_035 with Dissolve(1)
            m "..."
            scene black with Dissolve(1)
            pause 2
            scene black with Dissolve(1)
            transform moveup:
                xalign 0.5 yalign 1.0
                linear 5.0 yalign 0.0
            show 09_036 at moveup
            pause 3
            mc "Lexi!"
            mc "Hey, what are you doing here?"
            scene 09_037 with Dissolve(1)
            a "..."
            mc "What's wrong? Why aren't you saying anything?"
            scene 09_038 with Dissolve(1)
            mc "{i}(Oh shit.){/i}"
            $ achievement.grant("ACHIEVEMENT_THINK_HAPPEN")
            $ achievement.sync()
            mc "{i}(I knew I should've said something during training camp. What did I expect?){/i}"
            scene 09_039 with Dissolve(1)
            la "You... You... I..."
            a "I'll take it from here."
            scene 09_040 with Dissolve(1)
            a "You are a disgusting piece of shit!"
            a "How long did you think you could keep this up for before we found out?"
            mc "I..."
            scene 09_041 with Dissolve(1)
            a "She's my sister!"
            mc "Let me explain, please."
            a "What is there to explain? You fool around with the both of us until you decide who does it better?"
            mc "No, I..."
            scene 09_042 with Dissolve(1)
            a "What, [mc]? What?"
            mc "..."
            a "Stay away, and don't you ever talk to us again."
            scene 09_043 with Dissolve(1)
            a "Come on, Layla. Let's go home. He isn't worth any more of our time."
            la "..."
            a "Fucking asshole!"
            scene black with Dissolve(1)
            pause 2
            scene 09_044 with Dissolve(1)
            mc "{i}(Fuck...){/i}"
            mc "{i}(It's because I like both of you and I didn't want to hurt anyone...){/i}"
            mc "{i}(Who am I kidding? I knew exactly how this would turn out.){/i}"
            scene 09_045 with Dissolve(1)
            x "Good evening. I have a parcel for an Emily Vicari."
            mc "Yes, I'll take it."
            x "Can you sign here, please?"
            scene black with Dissolve(1)
            pause 2
            scene 09_056 with Dissolve(1)
            c "*Crying*"
            mc "{i}(What happened here? Why's she crying?){/i}"
            mc "Uhm..."
            scene 09_057 with Dissolve(1)
            m "Give us a moment, [mc]."
            mc "Okay?"
            mc "I'll be in my room. I left the package in the kitchen."
            m "Thanks."
            mc "{i}(Seriously, what's going on?){/i}"
            scene black with Dissolve(1)
            pause 2
            scene 09_512 with Dissolve(1)
            mc "{i}(It's been an hour already. I guess I'll check up on them.){/i}"
            jump Week4_Wednesday_Cara2
        else:
            $ Layla_End = False
            $ Elena_End = False
            play sound "Sounds/Phone_Vibrate.mp3"
            n "*Bzzzt. Bzzzt*"
            scene 09_034 with Dissolve(1)
            mc "Oh, give me a sec, I need to take this."
            mc "Be right back."
            scene 09_035 with Dissolve(1)
            m "..."
            scene black with Dissolve(1)
            pause 2
            scene 09_046 with Dissolve(1)
            mc "Hi. How are you?"
            a "Hey. I'm good."
            scene 09_047 with Dissolve(1)
            a "How are you?"
            mc "Good, good."
            a "What are you doing?"
            mc "Nothing much. Was at a garage today, looking at cars."
            scene 09_049 with Dissolve(1)
            a "I heard. And you met Iris again."
            mc "..."
            mc "I did."
            scene 09_050 with Dissolve(1)
            a "What a coincidence! Her words."
            mc "Tell me about it."
            a "..."
            a "Hey! Want to come over?"
            scene 09_051 with Dissolve(1)
            mc "I want to, but it will take me some time to get there. And I won't be able to stay that long."
            a "I'm not at the dorm. I'm home."
            mc "Oh... Because of Iris? She said you guys made up."
            a "We did. I just wanted to be alone to think."
            scene 09_052 with Dissolve(1)
            a "So, is that a yes?"
            mc "It's a yes. But aren't your parents home?"
            a "They are."
            mc "Do they know... about us?"
            a "No, I haven't told them yet. But don't worry, I'll sneak you in."
            mc "Heh... Okay."
            scene 09_053 with Dissolve(1)
            mc "I'll be there in twenty to twenty-five minutes?"
            a "Perfect. Call me once you're here."
            mc "Alright. See you soon."
            scene black with Dissolve(1)
            pause 2
            scene 09_056 with Dissolve(1)
            c "*Crying*"
            mc "{i}(What happened here? Why's she crying?){/i}"
            mc "Uhm..."
            scene 09_057 with Dissolve(1)
            m "Give us a moment, [mc]."
            mc "Okay?"
            mc "I need to go somewhere. I'll be back a little later."
            m "Thanks."
            mc "{i}(Seriously, what's going on?){/i}"
            jump Week4_Wednesday_Alexis
    else:
        n "*Ding-dong*"
        scene 09_016 with Dissolve(1)
        m "Oh, that must be the delivery."
        mc "I'll get it."
        scene 09_035 with Dissolve(1)
        m "..."
        scene 08_2367 with Dissolve(1)
        x "Good evening, I have a parcel for an Emily Vicari."
        mc "Yes, I'll take it."
        scene black with Dissolve(1)
        pause 2
        scene 09_056 with Dissolve(1)
        c "*Crying*"
        mc "{i}(What happened here? Why's she crying?){/i}"
        mc "Uhm..."
        scene 09_057 with Dissolve(1)
        m "Give us a moment, [mc]."
        mc "Okay?"
        mc "I'll be in my room. I left the package in the kitchen."
        m "Thanks."
        mc "{i}(Seriously, what's going on?){/i}"
        scene black with Dissolve(1)
        pause 2
        scene 09_512 with Dissolve(1)
        mc "{i}(It's been an hour already. I guess I'll check up on them.){/i}"
        jump Week4_Wednesday_Cara2

label Week4_Wednesday_Alexis:
    scene black with Dissolve(1)
    pause 2
    stop music fadeout 1.0
    play music ("Music/LoFi Upbeat 1.mp3", "Music/LoFi Upbeat 2.mp3", "Music/LoFi Upbeat 3.mp3", "Music/LoFi Upbeat 4.mp3") volume 0.2
    scene 09_062 with Dissolve(1)
    mc "{i}(I guess her dad is here, too.){/i}"
    mc "{i}(Haven't met him yet. Let's hope it won't be today, either.){/i}"
    scene 09_063 with Dissolve(1)
    mc "{i}(If he knew what Lexi and I did in his car...){/i}"
    n "*Ding-dong*"
    scene 09_064 with Dissolve(1)
    mc "{i}(Did I just?){/i}"
    mc "{i}(Fuck!){/i}"
    scene 09_065 with Dissolve(1)
    mc "{i}(Seriously... That was so stupid!){/i}"
    mc "{i}(And now I'm feeling even more stupid hiding here.){/i}"
    n "*Bzzzt. Bzzzt*"
    scene 09_066 with Dissolve(1)
    mc "Hey."
    a "Did you just ring the doorbell?"
    mc "About that..."
    mc "I kinda did... I was distracted and just pressed it out of habit. I'm so sorry."
    a "You had one job! One job!"
    mc "..."
    scene 09_067 with Dissolve(1)
    a "Where are you?"
    mc "Hiding behind your dad's car."
    a "Haha."
    a "Go to the door. I'll let you in."
    a "And don't press the doorbell!"
    scene black with Dissolve(1)
    pause 2
    scene 09_068 with Dissolve(1)
    mc "Hi."
    a "Hey."
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 09_069 at moveup
    pause 3
    mc "You look good."
    a "These are my pyjamas."
    mc "You look good in your pyjamas!"
    scene 09_070 with Dissolve(1)
    a "Thanks."
    scene 09_071 with Dissolve(1)
    a "Come on. I'll sneak you in."
    a "Let's be quick but quiet."
    mc "..."
    menu:
        "Go with her":
            pass
        "Press doorbell[KoGa3AutoWTChange1]{size=-4}(Alexis Points+2) {/size} {/color}":
            $ Alexis_Points += 2
            # Alexis (42)
            scene 09_072 with Dissolve(1)
            n "*Ding-dong!*"
            a "..."
            a "You didn't!"
            scene 09_073 with Dissolve(1)
            mc "Haha."
            a "That's not funny. Now we're both sitting here like idiots."
            scene 09_074 with Dissolve(1)
            a "..."
            x "Who is it?"
            scene 09_075 with Dissolve(1)
            am "Nobody. I think some kids are playing ding-dong-dash."
            a "Haha... Ding-dong-dash. Okay, it's a little funny."
            x "If they ring again, I'll check the cameras to see who they are."
            scene 09_076 with Dissolve(1)
            mc "You have cameras?"
            a "I forgot about those... We are so busted!"
            scene 09_077 with Dissolve(1)
            mc "Well, it was nice to know you."
            a "Haha."
            a "Let's go in now. And don't press it, please."
    scene black with Dissolve(1)
    pause 2
    scene 09_078 with Dissolve(1)
    ""
    scene 09_079 with Dissolve(1)
    a "Mmm..."
    n "*Knock-knock*"
    x "Lex?"
    scene 09_080 with Dissolve(1)
    a "Yes?"
    x "Can I come in?"
    mc "..."
    a "Uhm, give me a sec."
    scene 09_081 with Dissolve(1)
    a "*Whisper* Quick. Hide!"
    mc "*Whisper* You don't have to push me..."
    scene 09_082 with Dissolve(1)
    a "*Whisper* You can complain all you want after."
    mc "..."
    a "*Whisper* Now please go lie down behind the bed."
    scene 09_083 with Dissolve(1)
    a "Come on in."
    scene 09_084 with Dissolve(1)
    x "Hey."
    a "Hey, Dad. What's up?"
    scene 09_085 with Dissolve(1)
    x "Everything alright?"
    a "Uhm, yeah? Why shouldn't it be?"
    x "Never mind. Just curious why you were here."
    a "Oh... Uhm... Iris has company, so..."
    x "That's reason enough, I guess."
    a "Yeah."
    scene 09_086 with Dissolve(1)
    x "While you're here. Wanna go for a run?"
    a "Haha. Layla not home?"
    x "No, she left earlier... Just a few laps?"
    a "Pass. I'm running enough at the bar, already."
    x "*Sigh*"
    scene 09_087 with Dissolve(1)
    x "Speaking about the bar. I'll join you tomorrow."
    a "You mean drinking and watching the game!"
    x "Yeah, like I said. Join you."
    a "..."
    x "Haha."
    x "Come here. Give me a hug."
    scene 09_088 with Dissolve(1)
    x "You're my favourite, you know that?"
    a "Uh-huh. I heard you say the same to Layla."
    x "You're both my favourite."
    a "Seriously..."
    scene 09_089 with Dissolve(1)
    x "Good night."
    a "Night, Dad."
    scene 09_090 with Dissolve(1)
    mc "You're my favourite!"
    a "Haha. I'd better be!"
    scene 09_091 with Dissolve(1)
    a "Hey, I'm sorry I pushed you."
    mc "Heh, it's alright."
    a "You can come back up here."
    scene 09_092 with Dissolve(1)
    mc "That was scary for a moment. I thought he knew."
    a "I had the same feeling. But my record is still clean."
    mc "Heh? How many people have you snuck in your room before?"
    a "You're the second."
    mc "Oh..."
    scene 09_093 with Dissolve(1)
    a "I've never had a boy over, if that's what you're thinking."
    mc "..."
    a "It was years ago when I was grounded and snuck Erynn in here."
    scene black with Dissolve(1)
    pause 2
    scene 09_094 with Dissolve(1)
    mc "So, what are we doing now?"
    a "You continue with what you're doing right now."
    show 09_095
    mc "You like getting petted, huh?"
    a "Mmm-hmm."
    scene 09_096 with Dissolve(1)
    a "Tell me something I don't know."
    mc "About?"
    a "Yourself, or anything really."
    mc "Hmm..."
    if Andres_FB_Punch == True:
        scene 09_102 with Dissolve(1)
        mc "It's really difficult to think of anything if you ask me like that."
        a "Tell me about Iris."
        mc "Uh... You sure?"
        a "How did you meet her?"
    else:
        if Nikki_Girlfriend == False:
            if Cara_Girlfriend == False:
                scene 09_102 with Dissolve(1)
                mc "It's really difficult to think of anything if you ask me like that."
                a "Tell me about Iris."
                mc "Uh... You sure?"
                a "How did you meet her?"
            else:
                menu:
                    "Tell her about Cara[KoGa3AutoWTChange1]{size=-4}(Alexis RiversideStory, Alexis Points-4) {/size} {/color}":
                        $ Alexis_RiversideStory = True
                        $ Alexis_Points -= 4
                        scene 09_097 with Dissolve(1)
                        mc "My ex showed up at my house today."
                        a "What? Why would Iris come to your house?"
                        mc "Not Iris. My ex from Riverside, Cara."
                        a "..."
                        scene 09_098 with Dissolve(1)
                        mc "I haven't had a chance to talk to her yet. You called a few minutes after she arrived."
                        a "She's still there?"
                        mc "I guess. She was talking to Mom when I left."
                        a "Does she know about us?"
                        mc "No, I haven't talked to her since we broke up."
                        mc "I'll speak to her when I get back home."
                        scene 09_099 with Dissolve(1)
                        a "*Mumbles* I know why she's here..."
                        mc "Hmm?"
                        a "Nothing."
                        scene 09_100 with Dissolve(1)
                        a "*Sigh* First Iris, now Cara..."
                        mc "Sorry..."
                        a "Don't. It's just... Why are they all showing up now? Who's it going to be tomorrow?"
                        scene 09_101 with Dissolve(1)
                        if Valeria_Points >= 9:
                            mc "Probably Valeria."
                            a "Valeria? Who the fuck is Valeria?"
                            mc "Haha, I'm kidding."
                            mc "{i}(Why did I say Valeria? I could've used a random name...){/i}"
                        else:
                            mc "Probably Alice."
                            a "Alice? Who the fuck is Alice?"
                            mc "Haha, I'm kidding. There's no Alice."
                            a "..."
                        scene 09_102 with Dissolve(1)
                        a "How did you meet Iris?"
                        mc "Uh... You really want to know?"
                        a "Yes."
                    "Tell her a story":
                        scene 09_102 with Dissolve(1)
                        mc "It's really difficult to think of anything if you ask me like that."
                        a "Tell me about Iris."
                        mc "Uh... You sure?"
                        a "How did you meet her?"
        else:
            menu:
                "Tell her about Nikki[KoGa3AutoWTChange1]{size=-4}(Alexis RiversideStory, Alexis Points-4) {/size} {/color}":
                    $ Alexis_RiversideStory = True
                    $ Alexis_Points -= 4
                    scene 09_097 with Dissolve(1)
                    mc "My ex showed up at my house today."
                    a "What? Why would Iris come to your house?"
                    mc "Not Iris. My ex from Riverside, Nikki."
                    a "..."
                    scene 09_098 with Dissolve(1)
                    mc "I haven't had a chance to talk to her yet. You called a few minutes after she arrived."
                    a "She's still there?"
                    mc "I guess. She was talking to Mom when I left."
                    a "Does she know about us?"
                    mc "No, I haven't talked to her since we broke up."
                    mc "I'll speak to her when I get back home."
                    scene 09_099 with Dissolve(1)
                    a "Mumbles* I know why she's here..."
                    mc "Hmm?"
                    a "Nothing."
                    scene 09_100 with Dissolve(1)
                    a "*Sigh* First Iris, now Nikki..."
                    mc "Sorry..."
                    a "Don't. It's just... Why are they all showing up now? Who's it going to be tomorrow?"
                    scene 09_101 with Dissolve(1)
                    if Valeria_Points >= 9:
                        mc "Probably Valeria."
                        a "Valeria? Who the fuck is Valeria?"
                        mc "Haha, I'm kidding."
                        mc "{i}(Why did I say Valeria? I could've used a random name...){/i}"
                    else:
                        mc "Probably Alice."
                        a "Alice? Who the fuck is Alice?"
                        mc "Haha, I'm kidding."
                    scene 09_102 with Dissolve(1)
                    a "How did you meet Iris?"
                    mc "Uh... You really want to know?"
                    a "Yes."
                "Tell her a story":
                    scene 09_102 with Dissolve(1)
                    mc "It's really difficult to think of anything if you ask me like that."
                    a "Tell me about Iris."
                    mc "Uh... You sure?"
                    a "How did you meet her?"
    jump FB_Alvarado_Iris

label FB_Alvarado_Iris:
    scene black with Dissolve(2)
    pause 2
    stop music fadeout 1.0
    play music ("Music/LoFi Indie 3.mp3", "Music/LoFi Indie 1.mp3", "Music/LoFi Indie 2.mp3") volume 0.2
    n "Some time ago, in Alvarado."
    scene 09_103 with Dissolve(1)
    na "How about this one?"
    mc "Looks cool but that guitar is mostly for metal."
    scene 09_104 with Dissolve(1)
    mc "I was thinking about getting a strat."
    mc "The red one here."
    na "That's seven hundred bucks..."
    mc "I know."
    scene 09_105 with Dissolve(1)
    na "How much do you have?"
    mc "One-fifty cash and the two hundred Mom sent me for my eighteenth birthday."
    na "I can lend you another one-fifty, but you'd still be short."
    mc "Yeah, I'm not getting it today. Maybe next month. Thanks though."
    scene black with Dissolve(1)
    pause 2
    stop music fadeout 1.0
    play music "Sounds/Street_Traffic.mp3" volume 0.5
    scene 09_106 with Dissolve(1)
    mc "Oh by the way. How was the movie?"
    na "It sucked!"
    mc "Haha, yeah?"
    na "The first part was so good. But somehow they managed to screw this one up."
    scene 09_107 with Dissolve(1)
    na "I should've joined you and ran some laps instead."
    mc "You and running?"
    na "Haha, who am I kidding? That's not gonna happen."
    na "Maybe once I have a car, I'll drive next to you while you run. Go [mc]. Faster! FASTER!"
    mc "Haha."
    scene 09_108 with Dissolve(1)
    na "Hey, Lakeyn!"
    mc "..."
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 09_109 at moveup
    pause 3
    ln "Hey. Nate, was it?"
    na "Correct."
    scene 09_110 with Dissolve(1)
    na "This is my friend, [mc]."
    mc "{i}(Tattoos, coloured hair. She reminds me of Melissa.){/i}"
    na "This is Lakeyn. She's the new tattoo artist at Eclipse Ink."
    mc "Hey."
    ln "Hi."
    scene 09_111 with Dissolve(1)
    na "Lakeyn. I'll visit the shop next week to talk about a tattoo design I have in mind."
    ln "Sure. I work every day. Come by any time."
    na "Cool."
    scene 09_112 with Dissolve(1)
    na "What are you doing today?"
    ln "Oh, we're just going to hang out in the park. Listen to music. Drink. Draw up some tattoo ideas."
    na "Fun. I'll let you be then."
    ln "Alright. Have fun you both, and we'll see each other next week, then."
    scene 09_113 with Dissolve(1)
    ln "Bye Nate. Nice to meet you, [mc]."
    na "Later."
    mc "You too, Lakeyn. Good luck with the shop."
    ln "Thank you!"
    scene 09_114 with Dissolve(1)
    mc "She seems cool."
    mc "Unusual name though. Lakeyn..."
    na "Indeed. Don't ask me how to spell it."
    mc "Haha."
    scene 09_115 with Dissolve(1)
    na "Hey, I have a good idea."
    mc "You want to go to the park?"
    na "You know me well."
    mc "Let's grab some burgers first, though. I am hungry."
    na "Me too."
    jump FB_Alvarado_Iris_Park

label FB_Alvarado_Iris_Park:
    scene black with Dissolve(1)
    pause 2
    stop music fadeout 1.0
    play music "Sounds/Park.mp3" volume 0.5
    scene 09_116 with Dissolve(1)
    na "There's no one here."
    mc "Maybe we should've asked which park."
    na "Yeah..."
    scene 09_117 with Dissolve(1)
    na "Let's go sit there and chill a bit, I guess."
    mc "Mmm-hmm."
    scene 09_118 with Dissolve(1)
    mc "What kind of tattoo are you getting?"
    na "Let me show you some examples of what I'm thinking about."
    scene 09_119 with Dissolve(1)
    na "Something like this maybe."
    mc "Dog tags?"
    na "For my brother."
    mc "He'd like that."
    scene 09_120 with Dissolve(1)
    mc "Where are you gonna place it?"
    na "The inside of my forearm."
    mc "It would look good there."
    scene 09_121 with Dissolve(1)
    na "If you got a tattoo, what would you get?"
    mc "Hmm..."
    mc "Don't really know. Maybe something Día de Muertos inspired."
    mc "But that's a big maybe. I probably won't get any tattoos."
    scene 09_122 with Dissolve(1)
    na "..."
    mc "Is it really that shocking?"
    scene 09_123 with Dissolve(1)
    na "Don't move, and listen exactly to what I'm saying."
    mc "What?"
    na "Trust me."
    na "When I say now, slowly turn your head around. And by slowly, I mean fucking slow. Don't make it too obvious."
    mc "..."
    na "Now!"
    scene 09_124 with Dissolve(1)
    mc "..."
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 09_125 at moveup
    pause 3
    mc "Oh damn..."
    mc "How long has she been sitting there?"
    na "No idea. I saw her just now."
    scene 09_126 with Dissolve(1)
    mc "Why is she sunbathing here? Topless..."
    na "No beach. So this is the next best thing, I guess."
    mc "I'm not complaining. Just... Wow!"
    na "Yeah, I know what you mean."
    scene 09_127 with Dissolve(1)
    na "What are you doing?"
    mc "Taking a picture."
    na "If you get caught, it's on you. Just letting you know."
    mc "Her eyes are closed. She won't notice."
    scene 09_128 with vpunch
    mc "..."
    na "Are you kidding me? You didn't turn off the flash?"
    mc "I forgot. Fuck... Maybe she didn't notice?"
    scene 09_129 with Dissolve(1)
    mc "..."
    na "That doesn't look like a maybe."
    mc "Oh shit... We're in trouble."
    na "We? No! As I said earlier, this is on you. Leave me out of this."
    scene 09_130 with Dissolve(1)
    mc "..."
    ir "Phone!"
    scene 09_131 with Dissolve(1)
    mc "I'm so sorry."
    mc "{i}(Please don't break it. She's gonna smash it, right? Dad's gonna be so pissed.){/i}"
    mc "{i}(Guess I deserve this for being so stupid.){/i}"
    scene 09_132 with Dissolve(1)
    ir "..."
    scene 09_133 with Dissolve(1)
    ir "This is actually a really nice picture."
    ir "I look pretty!"
    mc "..."
    scene 09_134 with Dissolve(1)
    ir "Don't do that again!"
    mc "I won't, I'm sorry."
    scene 09_121 with Dissolve(1)
    na "I played this situation differently in my head."
    na "She let you off the hook very easy."
    mc "Yeah, I expected at least a slap and a smashed phone."
    mc "Let's leave before she changes her mind."
    $ renpy.end_replay()
    scene black with Dissolve(1)
    pause 2
    stop music fadeout 1.0
    play music ("Music/LoFi Indie 3.mp3", "Music/LoFi Indie 1.mp3", "Music/LoFi Indie 2.mp3") volume 0.2
    scene 09_135 with Dissolve(1)
    na "What shall we do tomorrow?"
    mc "Not going to that park, that's for sure."
    na "Haha. Let's stay away from there for a while."
    ni "We had to come all the way here for this?"
    scene 09_136 with Dissolve(1)
    c "They don't have an Ashley's in Riverside!"
    ni "We're splitting the gas money, just so you know!"
    scene black with Dissolve(1)
    pause 2
    scene 09_137 with Dissolve(1)
    mc "{i}(Why did I do such a stupid thing...){/i}"
    mc "{i}(That could've ended way differently.){/i}"
    scene 09_138 with Dissolve(1)
    mc "..."
    mc "{i}(Wait... She didn't delete the picture?){/i}"
    scene 09_139 with Dissolve(1)
    mc "{i}(She's really beautiful.){/i}"
    mc "{i}(I wish the girls at school were this pretty.){/i}"
    scene 09_140 with Dissolve(1)
    mc "..."
    scene 09_141 with Dissolve(1)
    mc "Dad?"
    mc "Dad, are you home?"
    mc "..."
    mc "{i}(Guess not.){/i}"
    scene black with Dissolve(2)
    pause 2
    n "The next day."
    scene 09_142 with Dissolve(1)
    play sound "Sounds/Phone_Vibrate.mp3"
    n "*Bzzzt. Bzzzt*"
    mc "..."
    play sound "Sounds/Phone_Vibrate.mp3"
    n "*Bzzzt. Bzzzt*"
    mc "{i}(Who's calling this early? It's freaking Saturday!){/i}"
    scene 09_143 with Dissolve(1)
    mc "Hello?"
    ir "About time. What took you so long?"
    mc "Who's this?"
    scene 09_144 with Dissolve(1)
    ir "Forgot about me already? I even let you keep the picture."
    mc "Oh... Park-girl."
    ir "Park-girl? Meet me there at ten o'clock. Don't be late!"
    scene 09_145 with Dissolve(1)
    mc "What?"
    mc "..."
    mc "Hello?"
    mc "{i}(I have a bad feeling about this. I knew she let me off too easy yesterday.){/i}"
    mc "{i}(Should I even go? Fuck...){/i}"
    scene black with Dissolve(2)
    pause 2
    stop music fadeout 1.0
    play music "Sounds/Park.mp3" volume 0.5
    scene 09_146 with Dissolve(1)
    mc "{i}(What am I doing here?){/i}"
    mc "{i}(It's been twenty minutes already. Of course she's not gonna come.){/i}"
    ir "You're here! Didn't expect you to show up."
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 09_147 at moveup
    pause 3
    mc "..."
    mc "{i}(She makes me so nervous.){/i}"
    scene 09_148 with Dissolve(1)
    ir "What's your name?"
    mc "Uhm... [mc]."
    ir "[mc]!"
    ir "Alright [mc]. You're going to come with me today and do whatever I ask of you."
    scene 09_149 with Dissolve(1)
    mc "Uhm."
    ir "Don't worry. It won't be anything illegal. See it as punishment."
    mc "{i}(What have I gotten myself into?){/i}"
    mc "Sure, I guess."
    mc "{i}(Let's just do this today and be done with it.){/i}"
    ir "I'm curious. Why did you take the picture?"
    scene 09_150 with Dissolve(1)
    mc "Well... Uhm... Because you looked pretty and uh... Topless..."
    ir "At least you're honest."
    ir "So you think I'm pretty?"
    mc "Uhm..."
    scene 09_151 with Dissolve(1)
    ir "Okay. Enough with the 'Uhms'. Be direct and answer confidently!"
    mc "..."
    mc "Yes, you're very pretty!"
    ir "Thank you."
    scene 09_152 with Dissolve(1)
    ir "How many times did you masturbate to my picture?"
    mc "..."
    mc "{i}(Fuck! How does she even know?){/i}"
    scene 09_153 with Dissolve(1)
    mc "Four times."
    ir "Four times? Wow. Four times to one picture!"
    ir "Hmm... You must really like it."
    scene 09_154 with Dissolve(1)
    ir "What do you think about my outfit today?"
    menu:
        "I like it":
            mc "I like it. You look really good."
            ir "Thank you."
            ir "Come on, let's leave."
        "I don't like it[KoGa3AutoWTChange1]{size=-4}(Iris FB Outfit DontLike) {/size} {/color}":
            $ Iris_FB_Outfit_DontLike = True
            mc "I liked the one from yesterday better."
            ir "Haha."
            scene 09_155 with Dissolve(1)
            ir "Maybe it'll help if I tell you that I'm not wearing panties today?"
            mc "..."
            ir "Come on. let's go."
    scene black with Dissolve(1)
    pause 2
    stop music fadeout 1.0
    play music "Sounds/Street_Traffic.mp3" volume 0.5
    scene 09_156 with Dissolve(1)
    x "Hey beautiful, wanna hang out with us?"
    mc "..."
    mc "{i}(That's like the third guy already in five minutes.){/i}"
    mc "{i}(Funny how she ignores every single one of them.){/i}"
    scene 09_157 with Dissolve(1)
    x "HEY! Are you kidding me? I'm right here..."
    mc "{i}(You sir, are in trouble. Just like I am.){/i}"
    mc "{i}(But I still don't know where we're going or what I'm supposed to do.){/i}"
    scene 09_158 with Dissolve(1)
    ir "This is our first stop."
    mc "Clothes shopping?"
    ir "I'm just picking up some stuff."
    scene black with Dissolve(1)
    pause 2
    scene 09_159 with Dissolve(1)
    mc "..."
    mc "{i}(Now I know why I had to tag along. She needed a pack mule...){/i}"
    scene 09_160 with Dissolve(1)
    ir "Hey [mc], I'm thirsty. Can you get me a coffee from here?"
    mc "..."
    mc "{i}(My hands are full. Can't she get it herself?){/i}"
    mc "{i}(Stop complaining. It's just for today. I won't see her again after anyway.){/i}"
    scene 09_161 with Dissolve(1)
    ir "What?"
    mc "What kind of coffee?"
    ir "Surprise me."
    scene 09_162 with Dissolve(1)
    mc "*Mumbles* Surprise me, surprise me..."
    mc "How should I know what you like?"
    mc "Let's see."
    scene 09_163 with Dissolve(1)
    ba "Hello."
    mc "Hi."
    ba "What can I get you?"
    mc "Hmm, two caramel macchiatos to go, please."
    ba "Sure. That'll be eight-thirty please."
    scene 09_164 with Dissolve(1)
    mc "{i}(Shit... I don't even have that much on me right now.){/i}"
    mc "Sorry, make that one please."
    ba "One caramel macchiato. Four-fifteen please."
    scene 09_165 with Dissolve(1)
    mc "Here you go."
    ir "Thank you. You didn't want anything?"
    mc "No, I'm good."
    ir "Hmm..."
    scene 09_166 with Dissolve(1)
    ir "..."
    ir "{i}(Caramel macchiato! Lucky guess?){/i}"
    scene 09_167 with Dissolve(1)
    ir "Good choice! My favourite."
    ir "Here, have a sip. You look thirsty."
    mc "..."
    ir "*Sigh* I'll help you."
    scene 09_168 with Dissolve(1)
    ir "Haha."
    mc "..."
    scene 09_169 with Dissolve(1)
    ir "Let's continue. A few more stops to go."
    mc "{i}(Even more? My arms are getting tired...){/i}"
    scene black with Dissolve(1)
    pause 2
    scene 09_170 with Dissolve(1)
    ir "This is me."
    mc "{i}(About time. How long have we been running around for?){/i}"
    scene 09_171 with Dissolve(1)
    ir "Thank you, [mc], for helping me."
    mc "{i}(Helping? You didn't carry anything...){/i}"
    mc "Sure."
    mc "{i}(It doesn't matter anymore. It's done. Lesson learned.){/i}"
    scene 09_172 with Dissolve(1)
    ir "I'll see you tomorrow, then."
    mc "What?"
    mc "{i}(She's joking, right? Right?){/i}"
    ir "I'll text you where to meet."
    mc "On Sunday?"
    ir "Uh-huh."
    mc "{i}(How long do I have to do this for?){/i}"
    mc "Okay... See you tomorrow..."
    ir "Bye-bye."
    scene 09_173 with Dissolve(1)
    ir "[mc]!"
    mc "*Sigh* Yes?"
    ir "I'm Iris!"
    mc "{i}(I liked you better as park-girl, Iris.){/i}"
    mc "..."
    scene black with Dissolve(2)
    pause 2
    stop music fadeout 1.0
    play music ("Music/LoFi Indie 3.mp3", "Music/LoFi Indie 1.mp3", "Music/LoFi Indie 2.mp3") volume 0.2
    scene 09_174 with Dissolve(1)
    d "Where have you been all day?"
    mc "All over town."
    d "Have you eaten? Are you hungry?"
    mc "No, not hungry."
    d "That's new..."
    scene 09_175 with Dissolve(1)
    mc "{i}(*Sigh* How many more days do I have to do this?){/i}"
    mc "{i}(One stupid picture...){/i}"
    mc "..."
    mc "{i}(Okay... It wasn't that bad walking around town with her.){/i}"
    mc "{i}(She looked really good, too.){/i}"
    show 09_176
    pause 2
    ir "Miss me already?"
    if Iris_FB_Outfit_DontLike == True:
        scene 09_155 with Dissolve(1)
        ir "I'm not wearing panties."
    else:
        pass
    scene 09_177 with Dissolve(1)
    mc "{i}(FUCK! Why can't I hate her?){/i}"
    mc "{i}(And why am I happy to see her tomorrow?){/i}"
    mc "AAAH!"
    d "Keep it down a bit!"
    scene black with Dissolve(2)
    pause 2
    scene 09_178 with Dissolve(1)
    play sound "Sounds/Phone_Message.mp3"
    n "*Bzzzt*"
    mc "{i}(Are you kidding me? It's the middle of the night...){/i}"
    scene 09_179 with Dissolve(1)
    mc "{i}(Of course it's her.){/i}"
    mc "{i}(She couldn't text me the address in the morning?){/i}"
    scene 09_180 with Dissolve(1)
    mc "..."
    scene 09_181 with Dissolve(1)
    mc "Fuck!"
    scene 09_182 with Dissolve(1)
    mc "{i}(Whatever. She's just teasing me again...){/i}"
    mc "{i}(It's not gonna work this time.){/i}"
    scene 09_183 with Dissolve(1)
    mc "..."
    scene 09_184 with Dissolve(1)
    mc "Iris... Iris..."
    mc "*Heavy breathing*"
    mc "Iris... Haa..."
    jump FB_Alvarado_Iris_Lake

label FB_Alvarado_Iris_Lake:
    scene black with Dissolve(2)
    pause 2
    stop music fadeout 1.0
    play music "Sounds/Park.mp3" volume 0.5
    scene 09_185 with Dissolve(1)
    mc "Hey Iris."
    ir "Hey there. Look at you. Actually using my name."
    mc "I didn't know it yesterday."
    ir "You never asked!"
    scene 09_186 with Dissolve(1)
    mc "Uh..."
    mc "{i}(This... is unexpected.){/i}"
    scene 09_187 with Dissolve(1)
    ir "Hmm... You have a different look about you today."
    ir "Are you actually happy to see me?"
    mc "{i}(It's your fault I can't stop thinking about you.){/i}"
    mc "Yeah right. I can't wait to carry all your bags again."
    ir "Haha. You didn't complain yesterday. At least not verbally."
    scene 09_188 with Dissolve(1)
    mc "Where's the first stop today?"
    ir "What's the rush? Let's sit down for a moment. We have all day."
    ir "Or do you have to be somewhere?"
    mc "No."
    scene 09_189 with Dissolve(1)
    ir "Did you enjoy the picture?"
    mc "I did..."
    ir "How many times?"
    mc "*Sigh* Not again..."
    scene 09_190 with Dissolve(1)
    ir "Tell me!"
    mc "..."
    mc "Twice!"
    scene 09_191 with Dissolve(1)
    ir "Only twice?"
    ir "Hmm. Do you think the first one was better?"
    mc "No. I really liked this one."
    ir "Good. But do you know what I didn't like?"
    mc "No?"
    scene 09_192 with Dissolve(1)
    ir "I never got a return picture. I had to use my imagination!"
    mc "What?"
    ir "Haha."
    mc "Stop joking around."
    scene 09_193 with Dissolve(1)
    ir "Who says I'm joking?"
    mc "..."
    scene 09_194 with Dissolve(1)
    ir "Why do you look so disappointed?"
    mc "No, it's..."
    ir "The pants? It's not a skirt day today, trust me. You'll see."
    ir "As a matter of fact. Let's go."
    scene black with Dissolve(1)
    pause 2
    scene 09_195 with Dissolve(1)
    ir "Here you go. You'll need this."
    mc "Wait... This is yours?"
    ir "Yes."
    mc "We're riding on that?"
    ir "Yes..."
    scene 09_196 with Dissolve(1)
    ir "I also brought you my dad's old jacket. I think it will fit you."
    mc "Uh, okay."
    mc "Where are we going?"
    ir "You'll see."
    scene 09_197 with Dissolve(1)
    ir "Let me see... Fits perfectly."
    ir "Good to go, I guess."
    scene 09_198 with Dissolve(1)
    ir "Hold on tight. Ready?"
    mc "Yes."
    ir "You call this tight? Lean against my back and put your arms around me. Can't have you fall off!"
    scene 09_199 with Dissolve(1)
    mc "You've done this before, right?"
    ir "Ride a motorcycle? Of course."
    mc "I mean with someone on the back."
    ir "No, first time."
    mc "..."
    stop music fadeout 1.0
    play music ("Music/LoFi Indie 3.mp3", "Music/LoFi Indie 1.mp3", "Music/LoFi Indie 2.mp3") volume 0.2
    scene 09_200 with Dissolve(1)
    mc "{i}(What is this feeling? I'm scared and turned on at the same time...){/i}"
    scene 09_201 with Dissolve(1)
    mc "{i}(She's going even faster now... That's insane.){/i}"
    mc "FUUUUCK!!!!"
    scene black with Dissolve(1)
    pause 2
    scene 09_202 with Dissolve(1)
    mc "Oh man..."
    ir "Are you alright?"
    scene 09_203 with Dissolve(1)
    mc "That was awesome!"
    mc "I should've known you were crazy when I first saw you sunbathing topless in a park."
    ir "Haha."
    scene 09_204 with Dissolve(1)
    mc "What are we doing here?"
    ir "I wanted to go swimming."
    scene black with Dissolve(1)
    pause 2
    scene 09_205 with Dissolve(1)
    ir "What are you waiting for?"
    mc "If you had told me we were going swimming, I would've brought my swimming trunks."
    ir "Where's the fun in that? Live a little!"
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 09_206 at moveup
    pause 3
    ir "Just go in your underwear, it's basically the same."
    ir "Or naked..."
    scene 09_207 with Dissolve(1)
    ir "Suit yourself. I'm going in."
    mc "..."
    scene 09_208 with Dissolve(1)
    mc "{i}(What am I doing here? What does she want from me?){/i}"
    mc "{i}(And why am I thinking about stupid questions when there is a pretty girl, swimming topless, right in front of me...){/i}"
    mc "{i}(Just go in there with her. Live a little!){/i}"
    scene 09_209 with Dissolve(1)
    ir "..."
    scene 09_210 with Dissolve(1)
    ir "Hey! What changed your mind?"
    mc "You..."
    ir "Me or me being topless?"
    scene 09_211 with Dissolve(1)
    mc "You and..."
    ir "You can look."
    mc "..."
    ir "Help me float!"
    scene 09_212 with Dissolve(1)
    ir "That's perfect. I like to come here and relax."
    mc "{i}(Does she come here often? With other... people?){/i}"
    mc "{i}(I don't even know if she does and I'm getting jealous already...){/i}"
    scene 09_213 with Dissolve(1)
    ir "Do you have a girlfriend?"
    mc "No."
    ir "No? Why not? You're very handsome. I bet all the girls at your school would love to date you."
    mc "I don't want to date them. I'm..."
    scene 09_214 with Dissolve(1)
    ir "Waiting for the perfect girl?"
    ir "She doesn't exist."
    mc "..."
    ir "Don't look at me like that. I'm not her either. I'm much worse than the girls at your school."
    mc "{i}(I don't think so.){/i}"
    scene 09_215 with Dissolve(1)
    mc "Do you have a boyfriend?"
    ir "Haha."
    mc "..."
    scene 09_216 with Dissolve(1)
    ir "What do you think?"
    mc "Uh... I don't know..."
    ir "Would I be doing this if I had one?"
    scene 09_217 with Dissolve(1)
    mc "..."
    mc "{i}(She's... She's...){/i}"
    ir "..."
    scene 09_218 with Dissolve(1)
    ir "Was that your first kiss?"
    mc "Yes..."
    ir "Oh. Are you a virgin?"
    scene 09_219 with Dissolve(1)
    mc "..."
    ir "Hey, that's nothing to be embarrassed about!"
    ir "And don't worry. I'll teach you."
    scene 09_220 with Dissolve(1)
    ir "I just felt your boner getting even harder."
    ir "I was talking about kissing. I'm not taking your virginity. I'll leave that for your future girlfriend."
    mc "..."
    ir "But we can take care of your hard-on right now..."
    scene 09_221 with Dissolve(1)
    mc "What?"
    ir "You can masturbate, and this time you don't have to look at a picture. You have the real me to look at."
    mc "{i}(Oh... I thought she would give me a handjob or a blowjob... Wishful thinking.){/i}"
    mc "{i}(Would she do it if I'd ask?){/i}"
    mc "{i}(Like I'm gonna ask her...){/i}"
    mc "I'm not masturbating in front of you!"
    ir "We're in the water, I won't see... much."
    mc "No!"
    scene 09_222 with Dissolve(1)
    ir "Okay, I'll close my eyes then."
    mc "..."
    show 09_223
    ir "..."
    ir "{i}(I expected him to make a move on me at least.){/i}"
    ir "{i}(I don't know if he's just shy or unsure. Maybe a bad experience?){/i}"
    ir "{i}(And why am I so comfortable around him?){/i}"
    scene 09_224 with Dissolve(1)
    ir "Hey, do you eat ice cream?"
    mc "Uh, yeah."
    ir "Good, because I want some."
    ir "Let's head back."
    $ renpy.end_replay()
    scene black with Dissolve(2)
    pause 2
    scene 09_225 with Dissolve(1)
    ""
    scene 09_226 with Dissolve(1)
    ir "Give me a minute. I'm gonna change real quick."
    ir "Do you need anything?"
    mc "I'm good."
    ir "Kay, be right back."
    scene 09_227 with Dissolve(1)
    mc "Iris! The jacket..."
    ir "Keep it. You look good in it."
    mc "You sure? I mean..."
    ir "Keep it."
    mc "Thanks."
    scene 09_228 with Dissolve(1)
    mc "{i}(Is this a date?){/i}"
    mc "{i}(I don't understand her at all. Yesterday I had to carry all her stuff. Today we went swimming and she kissed me...){/i}"
    mc "{i}(Now we're going to eat ice cream? Then there are the pictures she sent me...){/i}"
    mc "{i}(Does she like me? Or is all of this some weird scheme? I don't get it.){/i}"
    scene 09_229 with Dissolve(1)
    mc "{i}(Uh... Who's that?){/i}"
    mc "{i}(I saw that bike here yesterday, too.){/i}"
    scene 09_230 with Dissolve(1)
    jo "Who are you?"
    mc "I'm [mc], sir."
    jo "Iris here, too?"
    mc "Yes, she's inside."
    scene 09_231 with Dissolve(1)
    jo "What are your intentions with my daughter, [mc]?"
    mc "..."
    mc "Uh. Better question would be what are her intentions with me."
    mc "{i}(Fuck... Why did I say that?){/i}"
    scene 09_232 with Dissolve(1)
    jo "Haha. That's funny. But you're probably right."
    jo "Good to meet you, [mc]. And nice jacket!"
    scene 09_233 with Dissolve(1)
    mc "{i}(Wow, I played this conversation differently in my head...){/i}"
    mc "{i}(He seems like a really chill dad.){/i}"
    scene black with Dissolve(1)
    pause 2
    scene 09_234 with Dissolve(1)
    ir "Sorry, I had to talk to my dad."
    mc "No... worries..."
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 09_235 at moveup
    pause 3
    mc "{i}(She's gonna turn all the men's heads again in the city... Mine included.){/i}"
    ir "From now on it's a skirt day!"
    scene 09_236 with Dissolve(1)
    ir "What do you think?"
    ir "Can I be seen with you like this?"
    mc "Yes..."
    ir "Haha, yes?"
    ir "Compliment me!"
    scene 09_237 with Dissolve(1)
    mc "You look very cute."
    ir "Thank you. I like compliments, so give me lots."
    ir "Let's go get some ice cream!"
    jump FB_Alvarado_Iris_Ice

label FB_Alvarado_Iris_Ice:
    if _in_replay:
        $ Iris_FB_Outfit_DontLike = True
    scene black with Dissolve(1)
    pause 2
    scene 09_238 with Dissolve(1)
    mc "{i}(Do we look like a couple to other people? I wouldn't mind dating her. Is this considered a date?){/i}"
    mc "..."
    mc "{i}(I've known her for two days and I'm talking about dating her already.){/i}"
    mc "{i}(Actually, I don't even know her. Her name is Iris, that's about it.){/i}"
    mc "{i}(Who is she, really?){/i}"
    scene 09_239 with Dissolve(1)
    ir "You okay?"
    mc "Yeah, it's nothing. Was just thinking something."
    ir "Hmm..."
    scene 09_240 with Dissolve(1)
    mc "Shall we get the ice cream from here?"
    ir "Yes, this one is really good."
    mc "What do you want?"
    scene 09_241 with Dissolve(1)
    ir "No, no. It's on me. You paid for my coffee last time."
    ir "So, what can I get you?"
    mc "Surprise me!"
    ir "Haha. You'd better not regret it."
    scene 09_242 with Dissolve(1)
    x "Hello."
    ir "Hi."
    x "Have you decided yet?"
    ir "Yes. I'll have a cherry and a..."
    scene 09_243 with Dissolve(1)
    x "That'll be four dollars, please."
    ir "One second... Oh no! I forgot my purse. I'm sorry."
    x "Uh..."
    mc "{i}(Is she serious? Should I go and pay?){/i}"
    ir "Can you hold on to it for a moment? I'll quickly run home and get it."
    x "They'll probably have melted by then."
    ir "I'm so embarrassed now."
    scene 09_244 with Dissolve(1)
    x "You know what? Here, they're on me today."
    ir "No! Really? What's your name?"
    x "Adrian."
    ir "Adrian, you're an angel! Thank you very much."
    scene 09_245 with Dissolve(1)
    ir "Hehe!"
    mc "*Shakes head* Are you serious?"
    mc "You get away with everything, don't you?"
    scene 09_246 with Dissolve(1)
    mc "How many times have you done this?"
    ir "What? Never..."
    mc "..."
    ir "Okay. Maybe once or twice... This week."
    mc "Haha."
    scene 09_247 with Dissolve(1)
    ir "Here, this is yours."
    mc "Thank you. What is this?"
    ir "Mint chocolate chip. Surprise!"
    scene 09_248 with Dissolve(1)
    mc "Uh. Okay... Never had that before."
    ir "Let's go sit on the bench over there."
    scene 09_249 with Dissolve(1)
    mc "..."
    mc "{i}(Since when has eating ice cream looked so sexy?){/i}"
    scene 09_250 with Dissolve(1)
    ir "How's yours?"
    mc "Terrible."
    ir "Haha. Really? I'm sorry."
    ir "Can I try?"
    mc "Sure."
    scene 09_251 with Dissolve(1)
    ir "..."
    mc "What do you think?"
    scene 09_252 with Dissolve(1)
    mc "{i}(Her face says it all.){/i}"
    ir "It is terrible!"
    ir "Must be one of those flavours, you either love it or hate it. And I hate it!"
    mc "Same here."
    ir "It was a gamble. Just throw it away."
    scene 09_253 with Dissolve(1)
    ir "Want to try mine?"
    mc "I'm good."
    ir "Try it!"
    scene 09_254 with Dissolve(1)
    mc "{i}(She's gonna smear it on my face, right?){/i}"
    mc "{i}(Any second now...){/i}"
    scene 09_255 with Dissolve(1)
    mc "{i}(Maybe not.){/i}"
    ir "And? Better?"
    mc "It's good. Cherry?"
    ir "Uh-huh."
    scene 09_256 with Dissolve(1)
    mc "Uh..."
    ir "Let's share this one then."
    scene 09_257 with Dissolve(1)
    mc "..."
    ir "Don't just look. You should know by now that there's no need to be shy around me. You can touch."
    scene 09_258 with Dissolve(1)
    ir "{i}(His hands are really warm. Feels nice.){/i}"
    mc "{i}(My heart is pumping as if I've just finished running a marathon.){/i}"
    scene 09_259 with Dissolve(1)
    ir "Here, help me finish this ice cream before it melts."
    scene 09_260 with Dissolve(1)
    mc "{i}(The ice cream isn't bad, but now I wish it wasn't between us...){/i}"
    scene 09_261 with Dissolve(1)
    ir "Wanna try without the ice cream?"
    mc "{i}(How does she do that? It's like she's reading my mind...){/i}"
    mc "Uh..."
    show 09_262
    mc "..."
    scene 09_263 with Dissolve(1)
    ir "Mmm. I should've taken you instead of cherry."
    ir "Do you want to lick me?"
    mc "Iris..."
    ir "Anywhere you want!"
    scene 09_264 with Dissolve(1)
    ir "How about you start here and work your way down?"
    mc "..."
    ir "Or up..."
    scene 09_265 with Dissolve(1)
    ir "Hey, what's wrong?"
    ir "Too much? Too fast?"
    scene 09_266 with Dissolve(1)
    mc "No, it's not that. I'm just a little confused."
    mc "I know you planned something yesterday because I took the picture and you wanted to get even or something."
    mc "But then today..."
    scene 09_267 with Dissolve(1)
    ir "It's not that I wanted to get even. If it wasn't for the way you looked at me in the park, I would've deleted the picture and been done with it."
    ir "I wanted to find out more and play a little. I had something in mind, I'll admit that. But there's one thing that I didn't predict."
    mc "That is?"
    scene 09_268 with Dissolve(1)
    ir "That I'd enjoy spending time with you!"
    ir "So, this here isn't planned. This is me following my feelings."
    mc "..."
    mc "{i}(Does that mean she likes me?){/i}"
    ir "You must be thinking I'm some kinda weirdo."
    scene 09_269 with Dissolve(1)
    mc "No, I think you're kinda terrific!"
    ir "..."
    scene 09_270 with vpunch
    ir "Aaah!"
    ir "Hey!"
    mc "Haha."
    if Iris_FB_Outfit_DontLike == True:
        scene 09_271 with Dissolve(1)
        mc "{i}(She's wearing panties today!){/i}"
        mc "{i}(Maybe she was just teasing me yesterday.){/i}"
    else:
        pass
    scene 09_272 with Dissolve(1)
    mc "Did that get your heart pumping?"
    ir "You have no idea!"
    mc "Put your arms around me and hold on tight. Can't have you falling off! Your words."
    ir "Haha."
    mc "Now you know how I felt the whole day!"
    scene 09_273 with Dissolve(1)
    ir "You ran around with a hard-on this whole day?"
    mc "That's not what I meant!"
    ir "That's what I feel."
    scene 09_274 with Dissolve(1)
    ir "I told you to take care of it at the lake."
    mc "..."
    ir "Haha."
    scene 09_275 with Dissolve(1)
    ir "Want a second chance?"
    mc "IRIS!"
    scene 09_276 with Dissolve(1)
    ir "Haha."
    mc "You're crazy! What if someone sees?"
    ir "And takes a picture?"
    mc "Very funny!"
    mc "Please put your shirt back down!"
    scene 09_277 with Dissolve(1)
    mc "Sorry, I didn't..."
    ir "I don't mind."
    scene black with Dissolve(1)
    pause 2
    scene 09_278 with Dissolve(1)
    ir "*Sigh* The weekend is almost over... This one in particular went by way too quick!"
    ir "I don't want to go to school tomorrow. Can't they include Monday in the weekend?"
    mc "Haha, yeah. But isn't college fun?"
    scene 09_279 with Dissolve(1)
    ir "I don't know. I'm not in college yet."
    mc "What?"
    ir "I'm a senior."
    mc "Oh..."
    scene 09_280 with Dissolve(1)
    ir "And here you were thinking you're fooling around with a college student... What a letdown."
    mc "..."
    ir "Haha."
    scene 09_281 with Dissolve(1)
    mc "I really thought you were in college, since I haven't seen you before. You must be going to Canyon Valley?"
    ir "Indeed. You Alvarado High?"
    mc "Yes. We're basically rivals then."
    ir "Hmm..."
    scene 09_282 with Dissolve(1)
    ir "Our own little Romeo and Juliet story right here."
    mc "Yeah no, I'm way too young to die... This Romeo is out."
    ir "Haha."
    scene 09_283 with Dissolve(1)
    ir "You've changed a lot since yesterday. Yesterday you barely spoke five sentences."
    ir "Today we're actually having conversations. You aren't as shy as I first thought."
    mc "I was never really shy. You just make me nervous..."
    ir "Do I? That's good."
    scene 09_284 with Dissolve(1)
    ir "Let's go home."
    mc "Mmm-hmm."
    $ renpy.end_replay()
    scene black with Dissolve(2)
    pause 2
    scene 09_285 with Dissolve(1)
    ir "Thank you for walking me home."
    mc "You're welcome. Thank you for... today. It was lots of fun."
    ir "I had fun too."
    scene 09_286 with Dissolve(1)
    mc "Uhm, Iris..."
    ir "Yeah?"
    mc "No, nothing."
    ir "..."
    scene 09_287 with Dissolve(1)
    ir "Bye, [mc]."
    mc "Bye."
    scene 09_288 with Dissolve(1)
    ir "..."
    mc "..."
    scene 09_289 with Dissolve(1)
    ir "Bye."
    scene 09_290 with Dissolve(1)
    mc "{i}(Why was that so awkward, now?){/i}"
    mc "{i}(Should I have kissed her?){/i}"
    mc "{i}(It looked like she was waiting for it, right?){/i}"
    mc "..."
    mc "{i}(Fuck! Why didn't I kiss her?){/i}"
    scene 09_291 with Dissolve(1)
    mc "{i}(I wanted to kiss her the whole time we were sitting on that bench.){/i}"
    mc "{i}(And now when she gives me an obvious opening, I mess up...){/i}"
    mc "{i}(I'm a fucking idiot!){/i}"
    jump FB_Alvarado_Iris_Firsttime

label FB_Alvarado_Iris_Firsttime:
    if _in_replay:
        $ SexCounter_Iris = 0
        $ MC_SexCounter = 0
    $ SexCounter_Iris += 1
    $ MC_SexCounter += 1
    stop music fadeout 1.0
    play music ("Music/Slow3.mp3", "Music/Slow2.mp3") volume 0.2
    scene 09_292 with Dissolve(1)
    n "*Knock-knock*"
    mc "..."
    scene 09_293 with Dissolve(1)
    ir "Hey!"
    ir "What's..."
    scene 09_294 with Dissolve(1)
    ir "..."
    scene 09_295 with Dissolve(1)
    ""
    scene 09_296 with Dissolve(1)
    ""
    scene 09_297 with Dissolve(1)
    ir "Want to come inside?"
    mc "Didn't you say..."
    ir "I've changed my mind."
    scene black with Dissolve(1)
    pause 2
    scene 09_298 with Dissolve(1)
    ""
    scene 09_299 with Dissolve(1)
    ir "You sure you want to do this?"
    mc "I am."
    scene 09_300 with Dissolve(1)
    ir "Not stopping me this time, are you?"
    mc "No... I..."
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 09_301 at moveup
    pause 3
    ir "Don't be nervous, just follow my lead."
    scene 09_302 with Dissolve(1)
    ir "You can touch me, just like you did on the bench."
    mc "..."
    ir "Do whatever you're thinking about."
    scene 09_303 with Dissolve(1)
    mc "{i}(This!){/i}"
    scene 09_304 with Dissolve(1)
    ir "Mmm..."
    mc "{i}(So much better than ice cream.){/i}"
    scene 09_305 with Dissolve(1)
    ir "Let me take my clothes off."
    scene 09_306 with Dissolve(1)
    mc "{i}(I still can't believe I'm going to have sex with her...){/i}"
    mc "{i}(My first time, and with such a beautiful girl.){/i}"
    scene 09_307 with Dissolve(1)
    ir "I don't mind you staring. As a matter of fact, I really like it. But how about you get naked too?"
    mc "Uh, yeah."
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 09_308 at moveup
    pause 3
    ir "Satisfied?"
    mc "You are so pretty!"
    ir "Thank you."
    scene 09_309 with Dissolve(1)
    ir "You look nervous again."
    ir "We don't have to do this if you aren't ready."
    scene 09_310 with Dissolve(1)
    mc "I want to!"
    ir "Haha, I want it too!"
    scene 09_311 with Dissolve(1)
    mc "{i}(She's taking all the initiative. I'm just lying here like an idiot.){/i}"
    mc "{i}(Maybe I should...){/i}"
    scene 09_312 with vpunch
    ir "Haha, I didn't expect that."
    mc "Sorry, I just..."
    ir "Don't apologise!"
    scene 09_313 with Dissolve(1)
    ""
    scene 09_314 with Dissolve(1)
    mc "Can I?"
    ir "Don't ask either. Be confident and take control."
    ir "Touch me, pet me, kiss me, lick me, bite me. Whatever you like."
    mc "..."
    scene 09_315 with Dissolve(1)
    mc "{i}(I'm touching her pussy...){/i}"
    mc "How is this?"
    ir "Place your fingers a little higher."
    mc "..."
    scene 09_316 with Dissolve(1)
    ir "Yes, right there!"
    ir "Mmm..."
    scene 09_317 with Dissolve(1)
    ""
    scene 09_318 with Dissolve(1)
    mc "{i}(Should I?){/i}"
    mc "{i}(Well, she told me I can do whatever I like.){/i}"
    scene 09_319 with Dissolve(1)
    ir "..."
    scene 09_320 with Dissolve(1)
    ir "Stop for a moment."
    mc "Sorry, did I do something wrong?"
    ir "Not wrong, just... not right."
    ir "Kiss me. I'll show you what to do down there."
    scene 09_321 with Dissolve(1)
    mc "..."
    scene 09_322 with Dissolve(1)
    ir "Haha, what's with the face?"
    mc "Wow... Can you do that again?"
    ir "Haha. As many times as you want!"
    ir "I love kissing, so I'm going to make an amazing kisser out of you."
    scene 09_323 with Dissolve(1)
    mc "I'd better start practising then."
    ir "Mmm... Good!"
    scene 09_324 with Dissolve(1)
    ir "*Moaning*"
    scene black with Dissolve(1)
    pause 2
    scene 09_325 with Dissolve(1)
    mc "{i}(I'm getting really nervous now.){/i}"
    mc "{i}(This is it.){/i}"
    scene 09_326 with Dissolve(1)
    ir "[mc]. Look at me!"
    scene 09_327 with Dissolve(1)
    ir "Slowly, okay?"
    scene 09_328 with Dissolve(1)
    ""
    scene 09_329 with Dissolve(1)
    mc "{i}(I'm no longer a virgin!){/i}"
    scene 09_330 with Dissolve(1)
    ""
    scene 09_331 with Dissolve(1)
    ""
    scene 09_332 with Dissolve(1)
    mc "Is this okay? Do I have to go slower or faster?"
    ir "You're doing good. Just continue."
    scene 09_333 with Dissolve(1)
    ir "*Moaning*"
    scene black with Dissolve(1)
    pause 2
    scene 09_334 with Dissolve(1)
    mc "Uhm... Do I..."
    ir "You can cum inside me."
    scene 09_335 with vpunch
    pause 2
    scene 09_335 with vpunch
    mc "Thank you."
    ir "Haha, thank you? You're welcome. You did good!"
    scene black with Dissolve(2)
    pause 2
    scene 09_336 with Dissolve(1)
    ir "How do you feel?"
    mc "Amazing!"
    ir "Yeah?"
    mc "You are amazing!"
    ir "Heh..."
    scene 09_337 with Dissolve(1)
    ir "..."
    ir "Want to do it again?"
    scene 09_338 with Dissolve(1)
    mc "Yes!"
    scene 09_339 with Dissolve(1)
    ""
    scene 09_340 with vpunch
    mc "Hey! Don't steal my move!"
    ir "..."
    ir "Look at that. Lost his virginity and immediately thinks he has moves."
    scene 09_341 with Dissolve(1)
    ir "I'll show you moves! It's my turn now!"
    $ renpy.end_replay()
    scene black with Dissolve(1)
    pause 2
    stop music fadeout 1.0
    play music ("Music/LoFi Indie 3.mp3", "Music/LoFi Indie 1.mp3", "Music/LoFi Indie 2.mp3") volume 0.2
    scene 09_342 with Dissolve(1)
    mc "{i}(I can't believe that just happened. Three times!){/i}"
    mc "{i}(I won't be able to sleep tonight.){/i}"
    scene black with Dissolve(2)
    pause 2
    n "A few days later."
    scene 09_343 with Dissolve(1)
    na "He goes to his left."
    na "Crossover!"
    scene 09_344 with Dissolve(1)
    mc "..."
    na "Oooh... He got him! Nate 'Anklebreaker' Hayes does it again."
    scene 09_345 with Dissolve(1)
    na "And he finishes with an acrobatic lay-up."
    scene 09_346 with Dissolve(1)
    na "Eight-two! You'd better step up your game."
    scene 09_347 with Dissolve(1)
    mc "How do you like this fade-away?"
    scene 09_348 with Dissolve(1)
    na "..."
    scene 09_349 with Dissolve(1)
    na "What was that?"
    mc "Just not my day, I guess..."
    na "You've been down this whole week. What's going on? Did something happen?"
    mc "*Sigh*"
    na "Let's sit down."
    scene 09_350 with Dissolve(1)
    na "So, what happened?"
    mc "Do you remember the girl from the park?"
    na "The one you took the picture of?"
    mc "Yes."
    mc "Well..."
    scene black with Dissolve(2)
    pause 2
    scene 09_351 with Dissolve(1)
    na "Wait... What? Why are you only telling me this now?"
    na "If I didn't know you, I'd call bullshit, but... You had sex with her?"
    mc "Yeah..."
    na "Then why are you so mopy? That's awesome, no?"
    mc "It was..."
    na "But? What happened since?"
    scene 09_352 with Dissolve(1)
    mc "Nothing..."
    na "Nothing? You slept with her and nothing?"
    mc "I haven't heard from her since then."
    mc "I texted her a few times. Even called her, but she didn't pick up."
    scene 09_353 with Dissolve(1)
    na "That's weird."
    mc "We spent almost the whole weekend together. We had lots of fun."
    mc "It felt like she liked me. She even gave me her dad's old jacket to keep."
    mc "So, I don't know... Like you said. Weird."
    scene 09_354 with Dissolve(1)
    na "You said she has a motorcycle, maybe she was in an accident?"
    mc "What?"
    na "Just thinking of possibilities for why she didn't contact you or text back..."
    mc "And that's the first thing you came up with?"
    na "Sorry..."
    scene 09_355 with Dissolve(1)
    na "Maybe she's just busy?"
    mc "Too busy to text back?"
    x "Nate!"
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 09_356 at moveup
    pause 3
    mr "I've been looking for you. Hey, [mc]."
    mc "Hey, Mira."
    scene 09_357 with Dissolve(1)
    na "What's up, Mira?"
    mr "Wanna hang out with me?"
    na "Can't right now, I'm with my boy. Maybe later."
    scene 09_358 with Dissolve(1)
    mr "Come on... It'll be fun. [mc] can join us. Rylee will be there too."
    na "I told you we're busy, Miranda! I'll call you later."
    mr "*Sigh* Alriiiight. Don't forget!"
    scene 09_359 with Dissolve(1)
    ""
    scene 09_360 with Dissolve(1)
    mc "{i}(There's no way...){/i}"
    mc "{i}(Will she even make it to the rim?){/i}"
    scene 09_361 with Dissolve(1)
    mc "{i}(Yeah, okay...){/i}"
    scene 09_362 with Dissolve(1)
    mr "Three Points!"
    mr "Bye-bye."
    scene 09_363 with Dissolve(1)
    na "Uh..."
    mc "..."
    scene 09_364 with Dissolve(1)
    na "Haha."
    mc "Haha. Somehow I'm feeling a little better now."
    na "Somehow, huh?"
    scene 09_365 with Dissolve(1)
    na "Anyway. What are you going to do about park-girl?"
    mc "I don't know."
    na "Why don't you go to her house?"
    mc "Yeah?"
    na "Yeah! Ask her straight up what the deal is."
    mc "Hmm... You're right. I'll go later."
    scene 09_366 with Dissolve(1)
    na "Want to go for another round?"
    mc "Not really. I feel like I just got my ass kicked by a girl, and I didn't even play against her."
    na "Haha. She scored more points with one shot than you the whole game."
    mc "Oh, shut up."
    na "Haha."
    scene 09_367 with Dissolve(1)
    na "We can go hang out with Mira and Rylee?"
    mc "Why not. Let's do that."
    scene 09_368 with Dissolve(1)
    na "Hey Mira! Wait up!"
    scene 09_369 with Dissolve(1)
    mc "What are the plans for today?"
    mr "How about we get some ice cream? I really..."
    na "NOOOO!"
    scene 09_370 with Dissolve(1)
    mr "What no? Why not?"
    na "We hate ice cream!"
    mr "Heh? Since when?"
    na "Last week!"
    mc "Haha."
    scene black with Dissolve(2)
    pause 2
    n "The next day."
    scene 09_371 with Dissolve(1)
    mc "{i}(Her dad is here.){/i}"
    mc "{i}(Might as well ask him if she's here.){/i}"
    scene 09_372 with Dissolve(1)
    mc "Hello, sir."
    jo "Hey. [mc] was it?"
    mc "Yes."
    scene 09_373 with Dissolve(1)
    jo "Perfect timing, [mc]. Can you help me out for a minute?"
    mc "Uhm, sure."
    jo "Great."
    scene 09_374 with Dissolve(1)
    jo "Hold it right there."
    jo "I'm changing the suspension. It was way too stiff for all those bumpy roads here."
    jo "It was set up for track racing, but now I use it more as a daily driver."
    scene 09_375 with Dissolve(1)
    mc "You're a racing driver?"
    jo "Heh... Just a mechanic."
    jo "You've come to see Iris?"
    mc "Yes. Is she here?"
    jo "She's out. Can't say when she's coming back."
    scene 09_376 with Dissolve(1)
    mc "Oh..."
    jo "But since you're here. I could use a hand to finish this up."
    mc "Yeah, I'll help."
    jo "Thanks."
    scene black with Dissolve(1)
    pause 2
    scene 09_377 with Dissolve(1)
    jo "Hey, you're back."
    ir "Hey."
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 09_378 at moveup
    pause 3
    jo "Everything okay?"
    ir "Yes."
    mc "{i}(Is she crying?){/i}"
    scene 09_379 with Dissolve(1)
    mc "Hey."
    ir "Uh..."
    scene 09_380 with Dissolve(1)
    jo "I'll go check what happened."
    mc "I need to go home, too."
    jo "You don't want to wait and talk to her?"
    mc "I don't think it's a good time right now."
    scene 09_381 with Dissolve(1)
    jo "Alright. Thank you very much for helping me, [mc]."
    mc "My pleasure, sir. It was fun."
    jo "Call me John!"
    mc "John."
    scene 09_382 with Dissolve(1)
    mc "{i}(Why was she crying?){/i}"
    mc "{i}(I really want to know if something happened, but...){/i}"
    mc "*Sigh*"
    scene black with Dissolve(2)
    pause 2
    scene 09_383 with Dissolve(1)
    play sound "Sounds/Phone_Vibrate.mp3"
    n "*Bzzzt. Bzzzt*"
    mc "{i}(You've gotta be kidding me.){/i}"
    mc "{i}(I should turn my phone off at night.){/i}"
    scene 09_384 with Dissolve(1)
    mc "Hello?"
    ir "Hi."
    scene 09_385 with Dissolve(1)
    mc "Iris!"
    mc "Uhm..."
    scene 09_386 with Dissolve(1)
    ir "Can we talk?"
    mc "Uhm, yeah, sure. What's up?"
    scene 09_387 with Dissolve(1)
    ir "Can you come over?"
    mc "To your house?"
    ir "Yes."
    mc "Now? It's the middle of the night."
    ir "Please? I don't want to talk over the phone."
    scene 09_388 with Dissolve(1)
    mc "Okay. Give me like twenty minutes."
    ir "Thank you. See you soon."
    scene 09_389 with Dissolve(1)
    mc "{i}(Something so important she can't tell me over the phone?){/i}"
    mc "{i}(And why now? After almost a week without contact?){/i}"
    jump FB_Alvarado_Iris_Phone

label FB_Alvarado_Iris_Phone:
    scene black with Dissolve(1)
    pause 2
    scene 09_390 with Dissolve(1)
    mc "{i}(Why is she waiting outside? In that outfit?){/i}"
    mc "Hey!"
    scene 09_391 with Dissolve(1)
    ir "Thank you for coming."
    mc "Are you okay? Aren't you cold?"
    ir "That's why I'm hugging you, to warm up."
    mc "Only to warm up?"
    ir "No... Let's go inside."
    scene 09_392 with Dissolve(1)
    mc "{i}(She's undressing?){/i}"
    mc "{i}(I thought she wanted to talk.){/i}"
    scene 09_393 with Dissolve(1)
    ir "Come, join me."
    mc "What are we doing? Didn't you want to talk?"
    ir "It's more comfortable on the bed."
    scene 09_394 with Dissolve(1)
    ir "Can I snuggle up against you?"
    mc "Sure?"
    ir "Thank you."
    scene 09_395 with Dissolve(1)
    ir "You're warm! I like it."
    mc "I wasn't the one standing outside just wearing a robe..."
    ir "Put your arms around me."
    scene 09_396 with Dissolve(1)
    ir "This is much better. Thank you."
    mc "{i}(I haven't heard from her in a week. Then earlier she was crying and didn't say anything. And now she's... I don't get it.){/i}"
    scene 09_397 with Dissolve(1)
    mc "What happened? You..."
    ir "I'll tell you everything."
    scene 09_398 with Dissolve(1)
    ir "Two weeks before we met in the park, my girlfriend broke up with me."
    mc "Girlfriend?"
    ir "Yes. I'm bi. I like both men and women."
    mc "Oh..."
    scene 09_399 with Dissolve(1)
    ir "It took me by surprise, and the next few days after weren't my greatest."
    ir "I rarely came out of the house."
    ir "When things got better, I decided to go relax in the park. That was the day we met."
    scene 09_400 with Dissolve(1)
    ir "At first, I only saw you as an opportunity to get my mind off of her."
    ir "And it worked. I was enjoying myself. I felt happy."
    ir "It was supposed to be only for that day, but when you brought me home... I don't know. I wasn't thinking of her, I was thinking of wanting to see you again."
    ir "So that's why I said I'll see you tomorrow."
    scene 09_401 with Dissolve(1)
    ir "The day after we slept together, she called me and said she needed to see me."
    ir "I went to her place and we talked. She wanted to get back together."
    ir "I told her I needed some time."
    ir "Not because I was thinking about getting back together, that decision was already made. Just... I needed some time to myself."
    scene 09_402 with Dissolve(1)
    ir "When you saw me yesterday, I'd just come back from her."
    ir "I told her I can't be with her. I've met someone else..."
    ir "..."
    ir "I'm sorry. I should have..."
    scene 09_403 with Dissolve(1)
    mc "Hey, it's alright."
    mc "Thank you for telling me."
    scene black with Dissolve(2)
    pause 2
    scene 09_404 with Dissolve(1)
    mc "So, you like me, huh?"
    ir "Mmm-hmm."
    scene 09_405 with Dissolve(1)
    ir "Want to stay the night?"
    mc "Yeah, I don't want to walk home in the cold."
    ir "That's your reason? I might have a better one."
    scene 09_406 with Dissolve(1)
    ""
    scene 09_407 with Dissolve(1)
    ""
    scene 09_408 with Dissolve(1)
    ""
    scene black with Dissolve(2)
    pause 2
    scene 09_409 with Dissolve(1)
    play sound "Sounds/Phone_Vibrate.mp3"
    n "*Bzzzt. Bzzzt*"
    ir "Nggh... Who's calling so early? It's Sunday!"
    mc "Look who's talking. If I didn't know better, I'd say it was you!"
    scene 09_410 with Dissolve(1)
    play sound "Sounds/Phone_Vibrate.mp3"
    n "*Bzzzt. Bzzzt*"
    ir "Please pick up or I'll smash your phone!"
    scene 09_411 with Dissolve(1)
    mc "Hey, Dad."
    mc "..."
    mc "I left late last night."
    scene 09_412 with Dissolve(1)
    mc "*Whisper* Stop it!"
    mc "..."
    mc "What? No, nothing..."
    scene 09_413 with Dissolve(1)
    mc "Yeah, I'm at a friend's place."
    ir "Friend?"
    scene 09_414 with Dissolve(1)
    ir "*Bites*"
    mc "Aaaah!"
    scene 09_415 with Dissolve(1)
    mc "Dad, I've gotta go. I need to take care of something."
    ir "Mmm..."
    mc "See you later."
    scene 09_416 with vpunch
    ir "Haha."
    mc "Yeah, just laugh! Time for some punishment!"
    scene 09_417 with Dissolve(1)
    ir "If you think this is punishment, punish me!"
    mc "..."
    $ renpy.end_replay()
    jump FB_Alvarado_Iris_Bike

label FB_Alvarado_Iris_Bike:
    if _in_replay:
        $ SexCounter_Iris = 1
        $ MC_SexCounter = 1
    $ SexCounter_Iris += 2
    $ MC_SexCounter += 2
    scene black with Dissolve(2)
    pause 2
    n "Some weeks later."
    scene 09_418 with Dissolve(1)
    mc "Hey, aren't you going to open up? I've been standing here for a while."
    ir "I'm in the garage. Just come here."
    scene 09_419 with Dissolve(1)
    mc "{i}(Are we driving somewhere on the bike?){/i}"
    mc "{i}(Why is the light off?){/i}"
    scene 09_420 with Dissolve(1)
    ir "Surprise."
    mc "..."
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 09_421 at moveup
    pause 3
    mc "Fuck me..."
    ir "No! Fuck me!"
    mc "Damn, you look hot."
    ir "Thank you. Come here."
    scene 09_422 with Dissolve(1)
    ir "So, how about it?"
    mc "How about what?"
    ir "The 'fuck me' part."
    mc "On your dad's motorcycle?"
    ir "Uh-huh."
    scene 09_423 with Dissolve(1)
    mc "He's not here, right?"
    ir "Not yet. So let's stop wasting precious time."
    ir "I'm into lots of things, but my dad seeing me having sex isn't one of them."
    scene 09_424 with Dissolve(1)
    mc "Well then..."
    ir "Haha."
    scene 09_425 with Dissolve(1)
    ""
    scene 09_426 with Dissolve(1)
    ""
    scene 09_427 with Dissolve(1)
    ""
    scene black with Dissolve(1)
    pause 2
    scene 09_428 with Dissolve(1)
    mc "You really are in a rush..."
    mc "We can go to your room, you know."
    ir "No. I want to do it here!"
    scene 09_429 with Dissolve(1)
    ""
    scene 09_430 with Dissolve(1)
    ir "Hard already. Perfect."
    scene 09_431 with Dissolve(1)
    mc "Do you have any idea how much you turn me on when you look at me like that?"
    mc "You're so sexy, Iris."
    scene 09_432 with Dissolve(1)
    ""
    show 09_433
    ""
    scene 09_434 with Dissolve(1)
    mc "Oh, fuck..."
    scene 09_435 with Dissolve(1)
    ir "Heh, you liked that?"
    mc "Uh-huh..."
    scene 09_436 with vpunch
    ir "Aaah..."
    mc "My turn."
    scene 09_437 with Dissolve(1)
    ""
    scene 09_438 with Dissolve(1)
    ir "*Moaning*"
    scene 09_439 with Dissolve(1)
    ""
    scene 09_440 with Dissolve(1)
    ""
    scene 09_441 with Dissolve(1)
    ir "Ah... Keep going!"
    scene black with Dissolve(1)
    pause 2
    scene 09_442 with Dissolve(1)
    ""
    scene 09_443 with Dissolve(1)
    ""
    show 09_444
    ""
    scene 09_445 with Dissolve(1)
    mc "You feel so good, Iris."
    show 09_446
    ""
    scene 09_447 with Dissolve(1)
    ir "Look at you taking initiative!"
    mc "You okay with this?"
    ir "More than okay! I've told you many times. I'm yours."
    scene 09_448 with Dissolve(1)
    ir "Aaah..."
    show 09_449
    ""
    scene 09_450 with Dissolve(1)
    ir "Faster!"
    scene black with Dissolve(1)
    pause 2
    scene 09_451 with Dissolve(1)
    mc "You sure about this? If this falls..."
    ir "Then we run and we have no idea what happened here if Dad asks!"
    mc "*Shakes head* Iris..."
    scene 09_452 with Dissolve(1)
    mc "Well, your dad's gonna be thrilled once he sees all your juices on his seat."
    ir "Haha. And what about your juices?"
    mc "I was planning to cum inside of you or on your pretty tits. So I'm good."
    ir "Are you now? Then you'd better deliver!"
    scene 09_453 with Dissolve(1)
    ""
    show 09_454
    ""
    scene 09_455 with Dissolve(1)
    ir "Are you close? 'Cause I am."
    scene 09_456 with Dissolve(1)
    menu:
        "Cum inside her":
            scene 09_457 with vpunch
            pause 2
            scene 09_457 with vpunch
            ""
            scene 09_458 with Dissolve(1)
            mc "That was incredible!"
            ir "I've taught you well."
            scene 09_459 with Dissolve(1)
            mc "Iris!"
            ir "Hmm?"
            mc "I love you!"
            scene 09_460 with Dissolve(1)
            ir "I love you!"
        "Cum on her tits":
            scene 09_461 with vpunch
            pause 2
            scene 09_462 with vpunch
            ""
            scene 09_463 with Dissolve(1)
            mc "That was incredible!"
            ir "I've taught you well."
            mc "Iris, I love you!"
            ir "Heh. You couldn't pick a better moment than after cumming all over me to tell me?"
            mc "..."
            scene 09_464 with Dissolve(1)
            ir "I love you! Come here."
            mc "Ew... You're smearing all..."
            ir "Haha. Now you know how it feels!"
    $ renpy.end_replay()
    if Alexis_Dating == True:
        jump Week4_Wednesday_Alexis2
    else:
        jump Week4_Wednesday_Emily3

label Week4_Wednesday_Alexis2:
    scene black with Dissolve(2)
    pause 2
    stop music fadeout 1.0
    play music ("Music/LoFi Upbeat 1.mp3", "Music/LoFi Upbeat 2.mp3", "Music/LoFi Upbeat 3.mp3", "Music/LoFi Upbeat 4.mp3") volume 0.2
    scene 09_465 with Dissolve(1)
    a "You really took a picture of her when she was tanning in the park?"
    mc "Yeah, I don't know what I was thinking, but that's how we met."
    a "I would've been so mad if a random guy took such a picture of me."
    mc "Even if it was me?"
    scene 09_466 with Dissolve(1)
    a "..."
    a "That's difficult to answer."
    mc "See."
    a "No, it's because I know you and... I don't know. I'd probably be mad and a bit flattered?"
    mc "That's a weird combination."
    scene 09_467 with Dissolve(1)
    mc "We can try it now."
    a "Haha. You can take as many pictures as you want!"
    scene 09_468 with Dissolve(1)
    mc "Even those kinds of pictures?"
    a "Uh-huh."
    scene 09_469 with Dissolve(1)
    mc "You're turning me on so much right now."
    scene 09_470 with Dissolve(1)
    a "I'm gonna be honest. I'm a little jealous."
    mc "About?"
    a "You and Iris..."
    a "She was your first?"
    mc "Yeah. First girlfriend, first kiss..."
    scene 09_471 with Dissolve(1)
    a "No!"
    mc "What?"
    a "She wasn't your first kiss!"
    mc "Heh? What makes you say that?"
    a "..."
    scene 09_472 with Dissolve(1)
    a "Never mind."
    mc "Tell me!"
    a "No... If you don't know, I'm not telling you!"
    mc "..."
    scene 09_473 with Dissolve(1)
    mc "Where are you going?"
    a "Bathroom."
    mc "Are you mad at me?"
    scene 09_474 with Dissolve(1)
    mc "{i}(What's she talking about?){/i}"
    mc "{i}(Did I kiss someone else first? And how would Lexi know that?){/i}"
    mc "{i}(I definitely didn't kiss anyone before Iris in Alvarado...){/i}"
    mc "{i}(So...){/i}"
    scene 09_475 with Dissolve(1)
    mc "{i}(Erynn?){/i}"
    mc "{i}(No... I'd remember that.){/i}"
    mc "{i}(Who else does Lexi know that I know?){/i}"
    mc "..."
    scene 09_476 with Dissolve(1)
    mc "Oh..."
    scene black with Dissolve(2)
    pause 2
    scene 05_456a with Dissolve(1)
    a "Hey, are you okay?"
    mc "Go away. Just leave me alone!"
    a "Ethan is an idiot. I don't like him either."
    mc "..."
    scene 05_457a with Dissolve(1)
    a "I think what you did was really cute."
    a "Nobody ever gave me flowers."
    mc "It's just one flower."
    a "That doesn't matter. I'd love to get flowers from a boy one day."
    scene 05_458a with Dissolve(1)
    mc "{i}(Uh?){/i}"
    mc "Hey! What are you doing?"
    scene 05_459a with Dissolve(1)
    a "Happy Birthday, [mc]!"
    scene 09_477 with Dissolve(1)
    mc "..."
    scene 09_478 with Dissolve(1)
    mc "{i}(They're a little smaller than Erryn's.){/i}"
    scene 06_545 with Dissolve(1)
    a "..."
    scene 06_546 with Dissolve(1)
    a "{i}(Heh... I can't believe he just stole my first kiss...){/i}"
    scene 09_479 with Dissolve(1)
    mc "{i}(Girl's lips are so soft...){/i}"
    scene black with Dissolve(2)
    pause 2
    scene 09_480 with Dissolve(1)
    a "..."
    mc "{i}(She was actually my first kiss. What are the odds?){/i}"
    mc "{i}(She's looking so annoyed, but I can't stop smiling now.){/i}"
    scene 09_481 with Dissolve(1)
    a "[mc]!"
    mc "..."
    a "What are you doing?"
    scene 09_482 with vpunch
    a "Aah-haha-aaw!"
    scene 09_483 with Dissolve(1)
    mc "You were my first kiss, Lexi!"
    a "So you do remember!"
    mc "Yeah."
    scene 09_484 with Dissolve(1)
    a "That was also my first kiss!"
    mc "It was?"
    a "Uh-huh. You stole it!"
    scene 09_485 with Dissolve(1)
    mc "I'm sorry."
    a "I hated you for doing that back then, but now... I actually like it. It's somewhat special."
    scene 09_486 with Dissolve(1)
    mc "I remember thinking you had really soft lips after I kissed you."
    mc "Also, I was kinda checking you out. Looking at your boobs. You were wearing a tank top with a cat on it."
    a "First you don't remember, and now you even know what I was wearing..."
    a "I might still have that top somewhere. Let me check."
    scene black with Dissolve(1)
    pause 2
    scene 09_487 with Dissolve(1)
    a "This one, right?"
    mc "That's the one. I can't believe you still have it."
    a "Me neither."
    mc "Put it on."
    a "Yeah?"
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 09_488 at moveup
    pause 3
    mc "{i}(Or don't...){/i}"
    scene 09_489 with Dissolve(1)
    a "What do you think?"
    mc "Cute! Very cute!"
    a "Hehe."
    mc "Now that I look at it. Is it actually a cat?"
    a "Of course it is."
    scene 09_490 with Dissolve(1)
    mc "Is he looking at your boobs?"
    a "..."
    a "You're right. He is!"
    mc "Sneaky little pussy... cat."
    a "Haha."
    scene 09_491 with Dissolve(1)
    mc "Come here. I have an idea. Let's redo our first kiss."
    mc "But this time, the way a first kiss should be."
    scene 09_492 with Dissolve(1)
    ""
    scene 09_493 with Dissolve(1)
    a "..."
    scene 09_494 with Dissolve(1)
    ""
    scene 09_495 with Dissolve(1)
    la "..."
    scene 09_496 with Dissolve(1)
    a "I'm so horny right now!"
    la "Ew..."
    mc "What shall we do about that?"
    scene 09_498 with Dissolve(1)
    a "*Sigh...*"
    a "We can't today. Not when my parents are home."
    mc "Just cuddling then?"
    a "Sorry."
    scene 09_499 with Dissolve(1)
    mc "I don't mind. I still have all this."
    a "Haha."
    scene black with Dissolve(2)
    pause 2
    scene 09_500 with Dissolve(1)
    a "And we made it out safe!"
    mc "Want to push our luck?"
    a "Don't you dare ring the doorbell!"
    mc "Haha."
    scene 09_502 with Dissolve(1)
    mc "See you next time."
    a "Bye, [mc]. Thanks for coming."
    mc "Always. Good night, Lexi."
    a "Good night!"
    scene 09_501 with Dissolve(1)
    ""
    scene 09_503 with Dissolve(1)
    n "*Ding-dong*"
    mc "Haha. Good luck!"
    a "I hate you!"
    mc "No, you don't!"
    scene 09_504 with Dissolve(1)
    am "Did you see them?"
    a "What?"
    am "There are some kids playing ding-dong-dash. They were here before."
    a "Oh... Yeah, he ran away."
    scene 09_505 with Dissolve(1)
    am "Don't let him get away next time."
    a "Trust me, I won't."
    am "Hmm?"
    a "Nothing."
    scene 09_506 with Dissolve(1)
    la "Hey, Lex!"
    a "Hey."
    la "Can I come in?"
    a "Of course."
    scene 09_507 with Dissolve(1)
    la "What are you doing?"
    a "Reading."
    la "Since when do you read?"
    a "As in studying, Layla..."
    scene 09_508 with Dissolve(1)
    a "Bored?"
    la "No, not really."
    la "But you know what I am, Lexi?"
    a "Tell me."
    scene 09_509 with Dissolve(1)
    la "I'm so horny right now!"
    a "LAYLA!"
    scene 09_510 with Dissolve(1)
    a "You heard that?"
    la "Haha."
    a "Nooooo... Don't tell Mom and Dad!"
    scene 09_511 with Dissolve(1)
    la "They already know."
    a "What?"
    la "Well, Dad I'm not sure, but Mom knows you had [mc] over. Not [mc], but a boy."
    a "..."
    scene black with Dissolve(2)
    pause 2
    if Nikki_Girlfriend == False:
        if Cara_Girlfriend == False:
            jump Week4_Wednesday_Emily2
        else:
            jump Week4_Wednesday_Cara2
    else:
        jump Week4_Wednesday_Nikki2

label Week4_Wednesday_Nikki2:
    stop music fadeout 1.0
    play music ("Music/LoFi Indie 3.mp3", "Music/LoFi Indie 1.mp3", "Music/LoFi Indie 2.mp3") volume 0.2
    scene 09_513 with Dissolve(1)
    if Alexis_Dating == False:
        m "Hey, want a cup of tea, [mc]?"
        mc "I'm good. Are you okay?"
        ni "Yeah."
    else:
        m "Hey, where have you been?"
        mc "Sorry, was at a friend's house. Took a little longer than I expected. Are you okay?"
        ni "Yeah."
    scene 09_514 with Dissolve(1)
    mc "What have you been talking about?"
    m "All kinds of things."
    mc "Okay? Are you staying here, or...?"
    scene 09_515 with Dissolve(1)
    ni "Uhm, I kinda came here on a whim and haven't booked a hotel yet."
    ni "So I thought you might be able to recommend me one?"
    scene 09_516 with Dissolve(1)
    m "No-no-no, I'm not letting you stay at a hotel."
    m "They're all overpriced and you won't find a single room at this time. They'll have been booked-up for months."
    m "You can stay here."
    ni "Thank you, but..."
    m "[mc] lived at your place for months, you can stay here. Besides, I'd like that, too."
    ni "Thank you, Emily."
    scene 09_517 with Dissolve(1)
    m "I'll order a new bed for the guest room, in the meantime you can have [mc]'s room."
    mc "What?"
    ni "It's fine, I can..."
    m "You don't mind, right, [mc]?"
    mc "*Sigh* I guess..."
    scene 09_518 with Dissolve(1)
    mc "Where..."
    m "You can stay with me for a few days."
    mc "I'm not sleeping in the same bed as you."
    m "It's big enough, and it's not like we've never shared a bed."
    mc "I was like five years old or something, now it'd just be weird..."
    scene 09_519 with Dissolve(1)
    m "Twelve."
    mc "Huh?"
    m "You were twelve the last time..."
    mc "Whatever."
    m "There's also the couch?"
    mc "Couch it is!"
    scene 09_520 with Dissolve(1)
    m "Anyway, I'm going to search the internet for a bed."
    m "Can you show Nikki the room and carry her luggage upstairs?"
    mc "Sure."
    m "Thank you."
    scene black with Dissolve(2)
    pause 2
    scene 09_529 with Dissolve(1)
    mc "This is it."
    mc "I'll change the sheets later, you don't have..."
    scene 09_530 with Dissolve(1)
    mc "Uh... Nikki?"
    ni "I miss you!"
    ni "I didn't want you to leave."
    if Nikki_Solo == True:
        $ Nikki_Visit_Points += 4
        # Nikki_Visit (4)
        scene 09_531 with Dissolve(1)
        mc "I missed you too."
        mc "I'm sorry I've been so cold since you arrived. It's just... I didn't expect you to be here, and I didn't know what to say or how to react."
        ni "It's alright. This hug makes up for it."
        jump Week4_Wednesday_Nikki_Kiss
    else:
        menu:
            "Hug her[KoGa3AutoWTChange1]{size=-4}(Nikki Visit Points+2) {/size} {/color}":
                $ Nikki_Visit_Points += 2
                # Nikki_Visit (2)
                scene 09_531 with Dissolve(1)
                mc "I missed you too."
                mc "I'm sorry I've been so cold since you arrived. It's just... I didn't expect you to be here, and I didn't know what to say or how to react."
                ni "It's alright. This hug makes up for it."
            "No hug":
                mc "..."
        menu:
            "Seeing someone[KoGa3AutoWTChange1]{size=-4}(Nikki Week4 Wednesday Visit Knows) {/size} {/color}":
                $ Nikki_Week4_Wednesday_Visit_Knows = True
                scene 09_533 with Dissolve(1)
                mc "Nikki, we need to talk first."
                ni "Is something wrong?"
                mc "Let's sit down."
                scene 09_559 with Dissolve(1)
                mc "*Sigh* This is more difficult than I thought."
                mc "Sorry, uhm... It's not that I'm not happy to see you."
                scene 09_560 with Dissolve(1)
                mc "I'm seeing someone."
                ni "Oh..."
                mc "Yeah."
                mc "{i}(Fuck, this is so awkward.){/i}"
                scene 09_561 with Dissolve(1)
                ni "Sorry. I wouldn't have kissed you if..."
                mc "It's okay."
                ni "Me being here complicates things?"
                mc "..."
                mc "{i}(You have no idea.){/i}"
                scene 09_562 with Dissolve(1)
                ni "Do you want me to leave?"
                scene 09_563 with Dissolve(1)
                mc "No."
                mc "I don't want you to leave."
                mc "It's not that I don't have feelings for you anymore..."
                mc "It's just... complicated, like you said. I thought I'd never see you again, and..."
                scene 09_564 with Dissolve(1)
                ni "I understand."
                ni "Do you still like me?"
                mc "Of course I do."
                scene 09_565 with Dissolve(1)
                ni "Then I'm staying!"
                mc "Good."
                scene 09_566 with Dissolve(1)
                mc "{i}(This is going to be trouble...){/i}"
                mc "{i}(I'd better leave, or else I don't know what we'll end up doing.){/i}"
                scene 09_567 with Dissolve(1)
                mc "I'm gonna get you those fresh sheets."
                mc "Make yourself at home."
                ni "I will. And I'm sorry I'm taking your room."
                mc "It's fine."
                jump Week4_Wednesday_Emily2
            "We need to talk[KoGa3AutoWTChange1]{size=-4}(Nikki Week4 Wednesday Visit Breakup, Riverside Friends, Nikki GirlfriendFalse) {/size} {/color}":
                $ Nikki_Week4_Wednesday_Visit_Breakup = True
                $ Riverside_Friends = True
                $ Nikki_Girlfriend = False
                scene 09_533 with Dissolve(1)
                mc "Nikki, I think we need to talk."
                ni "Is something wrong?"
                mc "Let's sit down."
                scene 09_559 with Dissolve(1)
                mc "*Sigh* This is more difficult than I thought."
                mc "Sorry, uhm... It's not that I'm not happy you're here."
                scene 09_560 with Dissolve(1)
                mc "It's uh... I'm seeing someone."
                ni "Oh..."
                mc "Yeah."
                mc "{i}(Fuck, this is so awkward.){/i}"
                scene 09_561 with Dissolve(1)
                mc "Look, I thought we were over and we wouldn't see each other again."
                mc "I..."
                ni "No need to explain."
                ni "So, me being here complicates things?"
                mc "..."
                scene 09_562 with Dissolve(1)
                mc "Not complicate, but..."
                ni "I understand."
                ni "I should've called first. I'll leave."
                scene 09_568 with Dissolve(1)
                mc "Hey, I'm not kicking you out."
                mc "Stay. At least for today."
                ni "*Nods*"
                scene 09_569 with Dissolve(1)
                mc "I'm gonna get you some fresh sheets."
                ni "Thank you."
                mc "{i}(I hate to see her cry. But I think it was better to rip off the band-aid instead of having a drawn-out, considerate lead-up.){/i}"
                jump Week4_Wednesday_Emily2
            "Kiss her[KoGa3AutoWTChange1]{size=-4}(Nikki Visit Points+2) {/size} {/color}":
                $ Nikki_Visit_Points += 2
                # Nikki_Visit (4)
                jump Week4_Wednesday_Nikki_Kiss

label Week4_Wednesday_Nikki_Kiss:
    scene 09_534 with Dissolve(1)
    ""
    scene 09_535 with Dissolve(1)
    mc "Don't you think we need to talk first?"
    ni "Maybe we should, but..."
    scene 09_536 with vpunch
    mc "Hey, haha."
    scene 09_537 with Dissolve(1)
    mc "Nikki..."
    scene 09_538 with Dissolve(1)
    ni "Want me to stop?"
    mc "No..."
    scene 09_539 with Dissolve(1)
    ""
    scene 09_540 with Dissolve(1)
    mc "{i}(I missed that ass!){/i}"
    scene 09_541 with Dissolve(1)
    ni "Mmm..."
    scene 09_542 with Dissolve(1)
    ""
    scene 09_543 with Dissolve(1)
    ni "..."
    scene 09_544 with Dissolve(1)
    ni "[mc], wait a moment."
    mc "Sorry, too fast? Are you okay?"
    scene 09_545 with Dissolve(1)
    ni "I'm better than okay, actually."
    ni "But you were right. Maybe we should talk first."
    ni "But where to start?"
    scene 09_546 with Dissolve(1)
    mc "Maybe with why you're here?"
    ni "That's easy. Because of you!"
    ni "Are you happy I'm here?"
    mc "I am. I thought I'd never see you again."
    ni "Me too. But I hated that thought."
    scene 09_547 with Dissolve(1)
    mc "How long are you staying?"
    ni "Until Sunday, if that's okay?"
    mc "You can stay longer. It's spring break next week."
    ni "For you, yes. I have to go back to work on Monday."
    mc "..."
    scene 09_548 with Dissolve(1)
    ni "Uhm... Can we talk about our parent's almost-wedding?"
    mc "You mean your mom and my not-dad?"
    ni "Yeah... Sorry. Can you tell me about that?"
    mc "Sure."
    mc "*Sigh* Well, it was one crazy week. Finding out he wasn't my dad. Having a huge fight with Mom."
    ni "..."
    scene black with Dissolve(1)
    pause 2
    scene 09_549 with Dissolve(1)
    mc "So yeah, that's the... Why are you crying?"
    ni "Because now I finally understand how difficult it must have been for you to be put in that situation."
    ni "The way I reacted... I only thought..."
    mc "No. Your reaction was just fine, Nikki."
    ni "No, it wasn't! I should've considered your feelings, too."
    scene 09_550 with Dissolve(1)
    ni "I'm so sorry, [mc]!"
    mc "I'm sorry, too."
    scene 09_551 with Dissolve(1)
    ""
    scene black with Dissolve(1)
    pause 2
    scene 09_552 with Dissolve(1)
    ni "What now? What about us? What are we?"
    mc "Not brother and sister, that's for sure."
    ni "Haha."
    mc "What do you want us to be?"
    scene 09_553 with Dissolve(1)
    ni "I want to be your girlfriend!"
    scene 09_554 with vpunch
    ni "Hahaha..."
    mc "{i}(I'm getting turned on so much, lying on top of her.){/i}"
    scene 09_555 with Dissolve(1)
    n "*Slap*"
    ni "Is that a yes?"
    mc "Yes!"
    scene 09_556 with Dissolve(1)
    ""
    scene 09_557 with Dissolve(1)
    ni "Where are you going?"
    mc "Getting you new bedsheets and... To cool off a bit."
    ni "Cool off?"
    scene 09_558 with Dissolve(1)
    ni "We can... If you want."
    mc "I want to, but I think I should explain our hmm... situation... to my mom first."
    ni "That might be best."
    $ renpy.end_replay()
    jump Week4_Wednesday_Emily2

label Week4_Wednesday_Cara2:
    stop music fadeout 1.0
    play music ("Music/LoFi Indie 3.mp3", "Music/LoFi Indie 1.mp3", "Music/LoFi Indie 2.mp3") volume 0.2
    scene 09_521 with Dissolve(1)
    if Alexis_Dating == False:
        m "Hey, want a cup of tea, [mc]?"
        mc "I'm good. Are you okay?"
        c "Yeah."
    else:
        m "Hey, where have you been?"
        mc "Sorry, was at a friend's house. Took a little longer than I expected. Are you okay?"
        c "Yeah."
    scene 09_522 with Dissolve(1)
    mc "What have you been talking about?"
    m "All kinds of things."
    mc "Okay? Are you staying here, or...?"
    scene 09_523 with Dissolve(1)
    c "Uhm, I kinda came here on a whim and haven't booked a hotel yet."
    c "So I thought you might be able to recommend me one?"
    scene 09_524 with Dissolve(1)
    m "No-no-no, I'm not letting you stay at a hotel."
    m "They're all overpriced and you won't find a single room at this time. They'll have been booked-up for months."
    m "You can stay here."
    c "Thank you, but..."
    m "[mc] lived at your place for months, you can stay here. Besides, I'd like that too."
    c "Thank you, Emily."
    scene 09_525 with Dissolve(1)
    m "I'll order a new bed for the guest room, in the meantime you can have [mc]'s room."
    mc "What?"
    c "It's fine, I can..."
    m "You don't mind, right, [mc]?"
    mc "*Sigh* I guess..."
    scene 09_526 with Dissolve(1)
    mc "Where..."
    m "You can stay with me for a few days."
    mc "I'm not sleeping in the same bed as you."
    m "It's big enough, and it's not like we never shared a bed."
    mc "I was like five years old or something, now it'd just be weird..."
    scene 09_527 with Dissolve(1)
    m "Twelve."
    mc "Huh?"
    m "You were twelve the last time..."
    mc "Whatever."
    m "There's also the couch?"
    mc "Couch it is!"
    scene 09_528 with Dissolve(1)
    m "Anyway, I'm going to search the internet for a bed."
    m "Can you show Cara the room and carry her luggage upstairs?"
    mc "Sure."
    m "Thank you."
    scene black with Dissolve(1)
    pause 2
    scene 09_570 with Dissolve(1)
    mc "This is it."
    mc "I'll get you some fresh sheets later."
    scene 09_571 with Dissolve(1)
    mc "Cara?"
    mc "Are you okay?"
    if Cara_Solo == True:
        $ Cara_Visit_Points += 2
        # Cara _Visit (4)
        scene 09_572 with Dissolve(1)
        mc "Hey."
        mc "I'm sorry I've been so cold since you arrived. It's just... I didn't expect you to be here, and I didn't know what to say or how to react."
        c "I miss you."
        mc "I miss you too."
        jump Week4_Wednesday_Cara_Kiss
    else:
        menu:
            "Hug her[KoGa3AutoWTChange1]{size=-4}(Cara Visit Points+2) {/size} {/color}":
                $ Cara_Visit_Points += 2
                # Cara _Visit (2)
                scene 09_572 with Dissolve(1)
                mc "Hey."
                mc "I'm sorry I've been so cold since you arrived. It's just... I didn't expect you to be here, and I didn't know what to say or how to react."
                c "I miss you."
                mc "I miss you too."
            "Don't hug":
                mc "..."
        menu:
            "Seeing someone[KoGa3AutoWTChange1]{size=-4}(Cara Week4 Wednesday Visit Knows) {/size} {/color}":
                $ Cara_Week4_Wednesday_Visit_Knows = True
                scene 09_591 with Dissolve(1)
                mc "But there's something I need to talk to you about."
                mc "*Sigh* This is more difficult than I thought."
                mc "Sorry, uhm... It's not that I'm not happy to see you."
                scene 09_592 with Dissolve(1)
                mc "I'm seeing someone."
                c "Oh..."
                mc "Yeah."
                mc "{i}(Fuck, this is so awkward.){/i}"
                scene 09_593 with Dissolve(1)
                c "I thought of many reasons why I shouldn't come here, but that wasn't one of them."
                mc "..."
                c "Maybe I..."
                scene 09_594 with Dissolve(1)
                mc "Hey. I'm happy you're here."
                c "Don't you want me to leave?"
                mc "No, I don't want you to leave."
                mc "Cara. It's not that I don't have feelings for you anymore..."
                mc "It's just... a little complicated. I thought I'd never see you again, and..."
                scene 09_595 with Dissolve(1)
                c "Then, do you still like me?"
                mc "Of course I do."
                c "Okay. I'm staying!"
                scene 09_596 with Dissolve(1)
                mc "Good."
                scene 09_590 with Dissolve(1)
                mc "I'm gonna get you those fresh sheets."
                mc "Make yourself at home."
                c "I will. And I'm sorry I'm taking your room."
                mc "It's fine."
                jump Week4_Wednesday_Emily2
            "We need to talk[KoGa3AutoWTChange1]{size=-4}(Cara Week4 Wednesday Visit Breakup, Riverside Friends, Cara GirlfriendFalse) {/size} {/color}":
                $ Cara_Week4_Wednesday_Visit_Breakup = True
                $ Riverside_Friends = True
                $ Cara_Girlfriend = False
                scene 09_591 with Dissolve(1)
                mc "Cara, listen. I think we need to talk."
                mc "{i}(*Sigh* This is more difficult than I thought.){/i}"
                mc "Sorry, uhm... It's not that I'm not happy you're here."
                scene 09_592 with Dissolve(1)
                mc "It's uh... I'm seeing someone."
                c "Oh..."
                mc "Yeah."
                mc "{i}(Fuck, this is so awkward.){/i}"
                scene 09_593 with Dissolve(1)
                mc "We were over, and I thought we wouldn't see each other again."
                mc "So..."
                c "I had many reasons why I shouldn't come here, but that wasn't one of them."
                mc "Sorry."
                c "No, it's my fault for hoping that... Never mind."
                scene 09_597 with Dissolve(1)
                c "I don't know what to do, now."
                mc "Hey, I'm not kicking you out or anything."
                mc "We're still friends. You can stay and we can figure something out."
                c "*Nods*"
                scene 09_598 with Dissolve(1)
                mc "I'm gonna get you some fresh sheets."
                c "Thank you."
                mc "{i}(I hate to see her cry. But I think it was better to rip off the band-aid instead of having a drawn-out, considerate lead-up.){/i}"
                jump Week4_Wednesday_Emily2
            "Kiss her[KoGa3AutoWTChange1]{size=-4}(Cara Visit Points+2) {/size} {/color}":
                $ Cara_Visit_Points += 2
                # Cara_Visit (4)
                jump Week4_Wednesday_Cara_Kiss

label Week4_Wednesday_Cara_Kiss:
    scene 09_573 with Dissolve(1)
    c "Are you happy I'm here?"
    mc "I am. I thought I'd never see you again after what happened."
    scene 09_574 with Dissolve(1)
    ""
    scene 09_575 with Dissolve(1)
    mc "{i}(I've missed her more than I thought.){/i}"
    mc "{i}(This feels so right.){/i}"
    scene 09_576 with Dissolve(1)
    c "Mmm..."
    scene 09_577 with Dissolve(1)
    c "Ah..."
    scene 09_578 with Dissolve(1)
    c "..."
    scene 09_579 with Dissolve(1)
    c "[mc], wait a moment."
    mc "Sorry, too fast? Are you okay?"
    c "I'm better than okay, actually."
    c "But you were right. Maybe we should talk first."
    c "But where to start?"
    scene 09_580 with Dissolve(1)
    c "Uhm... Can we talk about our parent's almost-wedding?"
    mc "You mean your mom and my not-dad?"
    c "Yeah... Sorry. Can you tell me about that?"
    scene 09_581 with Dissolve(1)
    mc "Sure."
    mc "*Sigh* Well, it was one crazy week. Finding out he wasn't my dad. Having a huge fight with Mom."
    c "..."
    scene black with Dissolve(1)
    pause 2
    scene 09_582 with Dissolve(1)
    mc "That's the... Uh, Cara?"
    c "I'm so sorry. If I knew, I wouldn't have reacted the way I did, and..."
    mc "Cara, it's okay. You reacted just fine."
    scene 09_583 with Dissolve(1)
    c "But maybe then we..."
    mc "You're here now!"
    c "*Nods*"
    scene 09_584 with Dissolve(1)
    mc "Speaking of being here. How long are you staying?"
    c "Until Sunday, if that's okay with you?"
    mc "You can stay the whole of next week too. It's spring break."
    c "For you, yes. Mine is this week, so I'll have to be back before Monday."
    mc "I guess we'll have to make the best out of this week, then."
    c "Yeah."
    scene 09_585 with Dissolve(1)
    ""
    scene 09_586 with Dissolve(1)
    c "Heh..."
    mc "What are you smiling about?"
    c "Just thinking... Are we like... back together?"
    scene 09_587 with vpunch
    mc "Yes!"
    c "Haha."
    scene 09_588 with Dissolve(1)
    mc "{i}(Why is she so goddamn cute...?){/i}"
    mc "..."
    scene 09_589 with Dissolve(1)
    c "Where are you going?"
    mc "Getting you new bedsheets and... To cool off a bit."
    c "Cool off? What do you..."
    scene 09_590 with Dissolve(1)
    c "Oh..."
    mc "Yeah, that! And I think I should explain our hmm... situation... to my mom first."
    $ renpy.end_replay()
    jump Week4_Wednesday_Emily2

label Week4_Wednesday_Emily2:
    stop music fadeout 1.0
    play music ("Music/LoFi Indie 2.mp3", "Music/LoFi Indie 3.mp3", "Music/LoFi Indie 1.mp3") volume 0.2
    if Nikki_Girlfriend == True:
        scene black with Dissolve(1)
        pause 2
        scene 09_599 with Dissolve(1)
        mc "What are you watching?"
        m "A TV show. It's called Entanglement."
        if Alexis_Dating == False:
            mc "Hmm, okay."
        else:
            mc "Oh yeah. I've heard about that."
        m "Is Nikki upstairs? Have you talked?"
        mc "We have. And I think we need to talk, too."
        m "Come, sit down."
        scene 09_600 with Dissolve(1)
        mc "Nikki, she's..."
        m "The reason why you moved back here?"
        mc "Sort of, yeah. How..."
        m "I figured when I talked with her that there's more than just a friendship between you two."
        scene 09_602 with Dissolve(1)
        mc "Heh, yeah. It's still kinda weird she's here."
        m "Don't worry. You guys will figure it out."
        m "By the way. I've ordered a new bed. It will arrive on Friday though. Meaning you'll be spending two nights on this couch here."
        mc "One or two nights doesn't make much of a difference."
        m "My offer still stands!"
        mc "..."
        if Emily_Week3_Sunday_Surprise == False:
            jump Week4_Thursday_Nikki_Morning
        else:
            scene 09_601 with Dissolve(1)
            m "I'm meeting all your girlfriends today."
            if Alexis_Dating == False:
                m "First Iris, now Nikki. Anyone else?"
                mc "No..."
            else:
                m "First Iris, now Nikki. Anyone else showing up today?"
                m "Alexis, maybe?"
                mc "Very funny."
            scene 09_600 with Dissolve(1)
            m "How did you meet?"
            mc "Meet who?"
            m "Let's start with Iris today."
            mc "*Sigh*"
            scene 09_610 with Dissolve(1)
            m "Please? I know nothing about that time in your life."
            mc "Fine!"
            m "She was your first girlfriend?"
            mc "Yes."
            if Alexis_Dating == True:
                mc "Well..."
                jump Week4_Wednesday_Emily3
            else:
                jump FB_Alvarado_Iris
    else:
        if Cara_Girlfriend == True:
            scene black with Dissolve(1)
            pause 2
            scene 09_599 with Dissolve(1)
            mc "What are you watching?"
            m "A TV show. It's called Entanglement."
            if Alexis_Dating == False:
                mc "Hmm, okay."
            else:
                mc "Oh yeah. I've heard about that."
            m "Is Cara upstairs? Have you talked?"
            mc "We have. And I think we need to talk, too."
            m "Come, sit down."
            scene 09_600 with Dissolve(1)
            mc "Cara, she's..."
            m "The reason why you moved back here?"
            mc "Sort of, yeah. How..."
            m "I figured when I talked with her that there's more than just a friendship between you two."
            scene 09_602 with Dissolve(1)
            mc "Heh, yeah. It's still kinda weird she's here."
            m "Don't worry. You guys will figure it out."
            m "By the way. I've ordered a new bed. It will arrive on Friday though. Meaning you'll be spending two nights on this couch here."
            mc "One or two nights doesn't make much of a difference."
            m "My offer still stands!"
            mc "..."
            if Emily_Week3_Sunday_Surprise == False:
                jump Week4_Thursday_Cara_Morning
            else:
                scene 09_601 with Dissolve(1)
                m "I'm meeting all your girlfriends today."
                if Alexis_Dating == False:
                    m "First Iris, now Cara. Anyone else?"
                    mc "No..."
                else:
                    m "First Iris, now Cara. Anyone else showing up today?"
                    m "Alexis maybe?"
                    mc "Very funny."
                scene 09_600 with Dissolve(1)
                m "How did you meet?"
                mc "Meet who?"
                m "Let's start with Iris today."
                mc "*Sigh*"
                scene 09_610 with Dissolve(1)
                m "Please? I know nothing about that time in your life."
                mc "Fine!"
                m "She was your first girlfriend?"
                mc "Yes."
                if Alexis_Dating == True:
                    mc "Well..."
                    jump Week4_Wednesday_Emily3
                else:
                    jump FB_Alvarado_Iris
        else:
            if Nikki_Week4_Wednesday_Visit_Breakup == True:
                scene black with Dissolve(1)
                pause 2
                scene 09_599 with Dissolve(1)
                mc "What are you watching?"
                m "A TV show. It's called Entanglement."
                if Alexis_Dating == False:
                    mc "Hmm, okay."
                else:
                    mc "Oh yeah. I've heard about that."
                m "Is Nikki upstairs? Have you talked?"
                mc "We have. And I think we need to talk, too."
                m "Come, sit down."
                scene 09_600 with Dissolve(1)
                mc "Nikki, she's..."
                m "The reason why you moved back here?"
                mc "Sort of, yeah. How..."
                m "I figured when I talked with her that there's more than just a friendship between you two."
                scene 09_602 with Dissolve(1)
                mc "Heh, yeah. It's still kinda weird she's here. I thought we ended it, and well... I kinda moved on."
                m "Does she know that?"
                mc "Yeah, I told her earlier. I thought it was best to tell her immediately instead of drawing it out."
                mc "But now she's..."
                m "No, it was the right thing to do."
                scene 09_611 with Dissolve(1)
                m "Is she still staying here?"
                mc "I don't know. I asked her to stay at least for today, and said we'll see tomorrow."
                m "I'll talk to her later and see what she wants to do."
                mc "Thanks."
                if Emily_Week3_Sunday_Surprise == False:
                    jump Week4_Thursday_Nikki_Breakup
                else:
                    scene 09_600 with Dissolve(1)
                    m "What about Iris?"
                    mc "What about her?"
                    m "How did you meet her?"
                    mc "*Sigh* I should've seen that coming."
                    scene 09_601 with Dissolve(1)
                    m "Please? I know nothing about that time in your life."
                    mc "Fine!"
                    m "She was your first girlfriend?"
                    mc "Yes."
                    if Alexis_Dating == True:
                        mc "Well..."
                        jump Week4_Wednesday_Emily3
                    else:
                        jump FB_Alvarado_Iris
            else:
                if Cara_Week4_Wednesday_Visit_Breakup == True:
                    scene black with Dissolve(1)
                    pause 2
                    scene 09_599 with Dissolve(1)
                    mc "What are you watching?"
                    m "A TV show. It's called Entanglement."
                    if Alexis_Dating == False:
                        mc "Hmm, okay."
                    else:
                        mc "Oh yeah. I've heard about that."
                    m "Is Cara upstairs? Have you talked?"
                    mc "We have. And I think we need to talk, too."
                    m "Come, sit down."
                    scene 09_600 with Dissolve(1)
                    mc "Cara, she's..."
                    m "The reason why you moved back here?"
                    mc "Sort of, yeah. How..."
                    m "I figured when I talked with her that there's more than just a friendship between you two."
                    scene 09_602 with Dissolve(1)
                    mc "Heh, yeah. It's still kinda weird she's here. I thought we ended it, and well... I kinda moved on."
                    m "Does she know that?"
                    mc "Yeah, I told her earlier. I thought it was best to tell her immediately instead of drawing it out."
                    mc "But now she's..."
                    m "No, it was the right thing to do."
                    scene 09_611 with Dissolve(1)
                    m "Is she still staying here?"
                    mc "I don't know. I asked her to stay at least for today, and said we'll see tomorrow."
                    m "I'll talk to her later and see what she wants to do."
                    mc "Thanks."
                    if Emily_Week3_Sunday_Surprise == False:
                        jump Week4_Thursday_Cara_Breakup
                    else:
                        scene 09_600 with Dissolve(1)
                        m "What about Iris?"
                        mc "What about her?"
                        m "How did you meet her?"
                        mc "*Sigh* I should've seen that coming."
                        scene 09_601 with Dissolve(1)
                        m "Please? I know nothing about that time in your life."
                        mc "Fine!"
                        m "She was your first girlfriend?"
                        mc "Yes."
                        if Alexis_Dating == True:
                            mc "Well..."
                            jump Week4_Wednesday_Emily3
                        else:
                            jump FB_Alvarado_Iris
                else:
                    if Emily_Week3_Sunday_Surprise == False:
                        jump Week4_Thursday_School
                    else:
                        scene black with Dissolve(1)
                        pause 2
                        scene 09_599 with Dissolve(1)
                        mc "Anything good on TV?"
                        m "The usual. Want to see the game?"
                        mc "Nah, just keep watching your show."
                        m "Come sit down. Let's talk."
                        scene 09_600 with Dissolve(1)
                        mc "What do you want to talk about?"
                        m "Iris."
                        mc "*Sigh* I should've seen that coming."
                        scene 09_601 with Dissolve(1)
                        m "Please? I know nothing about that time in your life."
                        mc "Fine!"
                        m "She was your first girlfriend?"
                        mc "Yes."
                        m "How did you meet?"
                        if Alexis_Dating == True:
                            mc "Well..."
                            jump Week4_Wednesday_Emily3
                        else:
                            jump FB_Alvarado_Iris

label Week4_Wednesday_Emily3:
    scene black with Dissolve(2)
    pause 2
    scene 09_602 with Dissolve(1)
    m "Wow. It sounds like you were a really cute couple."
    m "I'm sad I missed all of that, though."
    m "She's the one who taught you how to ride a motorcycle?"
    mc "She started it, but it was mostly John who showed me how to ride properly."
    mc "We started with a dirt bike on an empty field."
    scene 09_603 with Dissolve(1)
    m "*Sigh* If you can promise me that you'll ride safely and not do anything reckless..."
    mc "{i}(Is she agreeing to buy me a motorcycle?){/i}"
    m "We also need to look for a helmet and..."
    scene 09_604 with Dissolve(1)
    mc "You're buying me a motorcycle?"
    m "I guess."
    mc "MOM!"
    scene 09_605 with vpunch
    m "..."
    mc "..."
    scene 09_606 with Dissolve(1)
    mc "Aaah, Mom!"
    m "Haha."
    mc "Why did you turn your head? I wanted to kiss your cheek!"
    m "Haha. I thought you were going in for a hug."
    mc "Stop laughing, this isn't funny."
    scene 09_607 with Dissolve(1)
    mc "I can't believe I kissed my mom on the lips!"
    m "Don't be so dramatic."
    mc "I could die of embarrassment right now."
    m "..."
    scene 09_608 with Dissolve(1)
    m "Let me help you with that then."
    mc "Mom! Haha."
    scene 09_609 with Dissolve(1)
    mc "Thanks, Mom."
    m "You're welcome, honey."
    if MC_Week4_Wednesday_BedOccupied == False:
        jump Week4_Thursday_School
    else:
        scene black with Dissolve(2)
        pause 2
        scene 09_612 with Dissolve(1)
        mc "{i}(I should've known I wouldn't be able to sleep on this couch...){/i}"
        mc "*Sigh*"
        menu:
            "Stay here":
                mc "{i}(It's only two nights...){/i}"
                scene black with Dissolve(2)
                pause 2
                scene 09_621 with Dissolve(1)
                mc "*Yawn*"
                if Nikki_Girlfriend == True:
                    jump Week4_Thursday_Nikki_Morning
                else:
                    if Cara_Girlfriend == True:
                        jump Week4_Thursday_Cara_Morning
                    else:
                        if Nikki_Week4_Wednesday_Visit_Breakup == True:
                            jump Week4_Thursday_Nikki_Breakup
                        else:
                            if Cara_Week4_Wednesday_Visit_Breakup == True:
                                jump Week4_Thursday_Cara_Breakup
                            else:
                                jump Week4_Thursday_School
            "Sleep in Emily's bed[KoGa3AutoWTChange1]{size=-4}(MC Week4 Thursday SleepInEmilyBed) {/size} {/color}":
                $ MC_Week4_Thursday_SleepInEmilyBed = True
                jump Week4_Thursday_Emily_Bed

label Week4_Thursday_Emily_Bed:
    scene 09_613 with Dissolve(1)
    mc "..."
    mc "{i}(We're just sleeping in the same bed, no big deal.){/i}"
    scene 09_614 with Dissolve(1)
    ""
    scene 09_615 with Dissolve(1)
    m "Oh, you're here."
    mc "Sorry, did I wake you?"
    m "No. Couldn't sleep on the couch?"
    mc "It's too short."
    scene 09_616 with Dissolve(1)
    m "Need some more blanket?"
    mc "It's fine."
    m "Okay. Good night."
    mc "Night, Mom."
    scene black with Dissolve(2)
    pause 2
    scene 09_617 with Dissolve(1)
    mc "..."
    scene 09_618 with Dissolve(1)
    mc "*Yawn*"
    mc "{i}(I don't want to wake up yet. Just a little more.){/i}"
    scene 09_619 with vpunch
    $ achievement.grant("ACHIEVEMENT_NOT_HAPPENING")
    $ achievement.sync()
    mc "{i}(Mom!){/i}"
    mc "{i}(Right... I totally forgot I'm in Mom's bed.){/i}"
    mc "{i}(Did I just touch... Nope, don't think about it. It never happened! Shower...){/i}"
    scene 09_677a with Dissolve(1)
    mc "{i}(Note to self. Don't sleep in Mom's bed again!){/i}"
    $ renpy.end_replay()
    if Nikki_Girlfriend == True:
        scene 09_678 with vpunch
        ni "[mc]!"
        scene black with Dissolve(1)
        transform moveup:
            xalign 0.5 yalign 1.0
            linear 5.0 yalign 0.0
        show 09_679 at moveup
        pause 3
        mc "..."
        scene 09_680a with Dissolve(1)
        mc "I'm so sorry, Nikki."
        mc "I didn't know you were in here."
        ni "It's okay. Nothing you haven't seen before."
        ni "You can come in."
        mc "Uh..."
        menu:
            "Wait outside":
                scene 09_681 with Dissolve(1)
                mc "I still have some time. I'll wait until you're ready."
                ni "Five minutes."
                mc "Sure."
                jump Week4_Thursday_Nikki_Morning2
            "Go in[KoGa3AutoWTChange1]{size=-4}(Nikki Visit Points+2) {/size} {/color}":
                $ Nikki_Visit_Points += 2
                jump Week4_Thursday_Nikki_Morning_Shower
    else:
        pass
    scene black with Dissolve(2)
    pause 2
    scene 09_723 with Dissolve(1)
    m "Hey, good morning."
    mc "Morning, Mom."
    m "Are all your clothes in the laundry?"
    mc "I forgot to get some clothes out of my room yesterday."
    scene 09_724 with Dissolve(1)
    m "Your teachers will be thrilled if they see you like this in their classroom."
    if Gabi_End == True:
        pass
    else:
        mc "{i}(Gabi would be, maybe...){/i}"
    mc "Very funny."
    if Zach_Week3_Wednesday_TC_Girlshower == True:
        pass
    else:
        if Zach_Week3_Saturday_TC_Swap == False:
            m "You still have those panties from your friend, too! I've washed them, if you..."
            mc "MOM!"
            m "Haha."
            mc "But good thing you reminded me. I still need to give them back."
        else:
            pass
    scene 09_725 with Dissolve(1)
    m "Coffee?"
    mc "Yes, please."
    scene 09_726 with Dissolve(1)
    if Nikki_Visit == True:
        m "Does Nikki drink coffee?"
        mc "She does."
        m "What about breakfast?"
        mc "Hmm... It depends. Sometimes just a banana, other times muesli or some other grain stuff..."
        scene 09_727 with Dissolve(1)
        m "Ask her if she needs anything and make a list and send it to me. I'll go shopping after work."
        mc "Will do."
    else:
        if Cara_Visit == True:
            m "Does Cara drink coffee?"
            mc "She does."
            m "What about breakfast?"
            mc "She never eats breakfast."
            scene 09_727 with Dissolve(1)
            m "Ask her if she needs anything and make a list and send it to me. I'll go shopping after work."
            mc "Will do."
        else:
            pass
    if Nikki_Girlfriend == True:
        jump Week4_Thursday_Nikki_Morning
    else:
        if Cara_Girlfriend == True:
            jump Week4_Thursday_Cara_Morning
        else:
            if Nikki_Week4_Wednesday_Visit_Breakup == True:
                jump Week4_Thursday_Nikki_Breakup
            else:
                if Cara_Week4_Wednesday_Visit_Breakup == True:
                    jump Week4_Thursday_Cara_Breakup
                else:
                    jump Week4_Thursday_School

label Week4_Thursday_Nikki_Breakup:
    scene black with Dissolve(2)
    pause 2
    scene 09_783 with Dissolve(1)
    mc "Hey, morning. You're up early."
    ni "Morning."
    mc "Your bag... You're leaving?"
    ni "I am. I think it's for the best."
    scene 09_784 with Dissolve(1)
    mc "Do you need a ride?"
    ni "Emily is driving me to the airport."
    mc "When are you..."
    scene 09_785 with Dissolve(1)
    m "Morning, [mc]."
    mc "Morning, Mom. And thank you for driving Nikki."
    m "Of course. Are you ready, Nikki?"
    ni "Yes."
    mc "Oh, you're leaving now..."
    scene 09_786 with Dissolve(1)
    mc "Again, I'm really sorry."
    ni "..."
    scene 09_787 with Dissolve(1)
    ni "Maybe we'll meet again someday."
    mc "Yeah..."
    scene 09_788 with Dissolve(1)
    mc "*Sigh*"
    mc "{i}(This was the right choice, right?){/i}"
    mc "{i}(I kinda miss her already. Even this bed smells like her...){/i}"
    scene black with Dissolve(2)
    pause 2
    scene 09_789 with Dissolve(1)
    mc "{i}(Fuck, I dozed off.){/i}"
    mc "{i}(I'm going to be late!){/i}"
    jump Week4_Thursday_School

label Week4_Thursday_Cara_Breakup:
    scene black with Dissolve(2)
    pause 2
    scene 09_778 with Dissolve(1)
    mc "Hey, morning. You're up early."
    c "Morning."
    mc "Your bag... You're leaving?"
    c "I am. I think it's for the best."
    scene 09_779 with Dissolve(1)
    mc "Do you need a ride?"
    c "Emily is driving me to the airport."
    mc "When are you..."
    scene 09_780 with Dissolve(1)
    m "Morning, [mc]."
    mc "Morning, Mom. And thank you for driving Cara."
    m "Of course. Are you ready, Cara?"
    c "Yes."
    mc "Oh, you're leaving now..."
    scene 09_781 with Dissolve(1)
    mc "Again, I'm really sorry."
    c "..."
    scene 09_782 with Dissolve(1)
    c "Maybe we'll meet again someday."
    mc "Yeah..."
    scene 09_788 with Dissolve(1)
    mc "*Sigh*"
    mc "{i}(This was the right choice, right?){/i}"
    mc "{i}(I kinda miss her already. Even this bed smells like her...){/i}"
    scene black with Dissolve(2)
    pause 2
    scene 09_789 with Dissolve(1)
    mc "{i}(Fuck, I dozed off.){/i}"
    mc "{i}(I'm going to be late!){/i}"
    jump Week4_Thursday_School

label Week4_Thursday_Nikki_Morning:
    if MC_Week4_Thursday_SleepInEmilyBed == True:
        jump Week4_Thursday_Nikki_Morning2
    else:
        $ Nikki_Visit_Points += 2
        # Nikki_Visit (6)
        $ Valeria_Week4_Thursday_MeetNikki = True
        scene black with Dissolve(2)
        pause 2
        scene 09_620 with Dissolve(1)
        ""
        scene 09_622 with Dissolve(1)
        ni "..."
        scene 09_623 with Dissolve(1)
        ni "Hey, wake up."
        mc "Nggh..."
        ni "Come on, wake up!"
        scene 09_624 with Dissolve(1)
        mc "Nikki!"
        ni "Morning, sunshine."
        mc "What are you doing here? What time is it?"
        ni "It's six o'clock! Time for our run."
        scene 09_625 with Dissolve(1)
        mc "Six? That's way too early, Nikki. Go back to bed."
        ni "No, it's time for our morning run."
        mc "Run? I have training at school, I'll be doing lots of running there."
        ni "Please, come with me. I don't know this area. You don't want me to get lost, or...?"
        menu:
            "Wake up":
                scene 09_626 with Dissolve(1)
                mc "*Yawn* Fine! Give me five minutes."
                ni "Three!"
                mc "..."
            "Grab her[KoGa3AutoWTChange1]{size=-4}(Nikki Visit Points+2) {/size} {/color}":
                $ Nikki_Visit_Points += 2
                # Nikki_Visit (8)
                scene 09_627 with vpunch
                ni "[mc]!"
                mc "Come here!"
                ni "Haha."
                scene 09_628 with Dissolve(1)
                mc "Isn't this much better than running?"
                mc "Let's sleep a bit longer!"
                ni "[mc], noooo!"
                scene 09_629 with Dissolve(1)
                ni "Please come jog with me."
                n "*Slap*"
                ni "Ah..."
                mc "Fine! Give me five minutes."
                scene 09_629a with Dissolve(1)
                ""
                scene 09_630 with Dissolve(1)
                ni "I'll give you three!"
                mc "Hey!"
                scene 09_631 with Dissolve(1)
                ni "..."
                mc "..."
                scene 09_632 with Dissolve(1)
                ni "Five minutes it is."
        scene black with Dissolve(2)
        pause 2
        stop music fadeout 1.0
        play music "Sounds/Park.mp3" volume 0.3
        scene 09_633 with Dissolve(1)
        ni "Haha."
        mc "You can stop laughing now!"
        mc "It's... the morning. It happens."
        scene 09_634 with Dissolve(1)
        mc "Obviously you've had hard nipples before!"
        ni "Obviously."
        mc "*Sigh*"
        scene 09_635 with Dissolve(1)
        mc "Did you sleep okay in my bed?"
        ni "Yes, it's very comfortable. Thanks again for letting me have it."
        mc "Of course."
        scene 09_636 with Dissolve(1)
        mc "What are your plans for today?"
        ni "Hmm... Probably check out the city, do some sightseeing."
        ni "Anywhere specific I should go?"
        mc "The beach of course. Back in Riverside, you said you can't wait to go there."
        scene 09_637 with Dissolve(1)
        ni "I'd rather go there with you."
        mc "Sure. We can go after school."
        ni "Today? Not at the weekend?"
        mc "It's gonna be swarmed in the weekend. Especially since spring break starts then."
        scene 09_638 with Dissolve(1)
        ni "Okay, today it is. I'll pick you up then."
        mc "I'll need to go home first to change, though."
        ni "I'll pick you up anyway. That way I can have a look at your school."
        scene 09_639 with Dissolve(1)
        ni "What are you smiling about all of a sudden?"
        mc "Just imagining your pretty butt in a bikini."
        ni "..."
        ni "That's why you like the beach so much, huh?"
        scene 09_640 with Dissolve(1)
        mc "I don't need the beach for that."
        mc "It looks just as amazing in those white pants!"
        scene 09_641 with Dissolve(1)
        ni "You know what. I'm gonna run like this from now on... No more butts for you!"
        mc "Ha. I don't mind either. You look good from both sides."
        scene 09_642 with Dissolve(1)
        mc "But just a little reminder of what happened last time you didn't pay attention when we jogged!"
        ni "Good thing you're here to save me!"
        scene 09_643 with Dissolve(1)
        mc "Uh-huh."
        ni "Besides. We're in a park. No cars here..."
        scene 09_644 with vpunch
        ni "Aaah..."
        va "..."
        scene 09_645 with Dissolve(1)
        mc "Nikki!"
        mc "Are you alright?"
        scene 09_646 with Dissolve(1)
        ni "Oh my god, I'm so sorry! Are you okay?"
        va "I'm sorry too, I..."
        ni "No-no-no. It's my fault. I shouldn't run backwards."
        va "I wasn't paying attention either."
        scene 09_647 with Dissolve(1)
        mc "You guys alright?"
        ni "Yeah, I think we're good."
        mc "Oh, hey Val!"
        va "Hey, [mc]."
        menu:
            "Help Nikki[KoGa3AutoWTChange1]{size=-4}(Nikki Visit Points+2) {/size} {/color}":
                $ Nikki_Visit_Points += 2
                # Nikki_Visit (10)
                scene 09_648 with Dissolve(1)
                mc "Let me help you up."
                ni "Hehe, thanks."
            "Help Valeria[KoGa3AutoWTChange1]{size=-4}(Valeria Points+2) {/size} {/color}":
                $ Valeria_Points += 2
                # Valeria (14)
                scene 09_649 with Dissolve(1)
                mc "Let me help you up."
                va "Thank you, [mc]."
        scene 09_650 with Dissolve(1)
        ni "Let me fix this for you."
        va "Thanks."
        ni "Again, I'm so sorry. You sure you're okay?"
        va "All good, don't worry."
        scene 09_651 with Dissolve(1)
        ni "So, you know each other?"
        mc "Yes. This is Valeria, we go to school together."
        mc "We're also on the same track-and-field team."
        scene 09_652 with Dissolve(1)
        mc "Not only at training camp but also now you wake up early and get some training in, huh?"
        va "Yes, I didn't like my second place. So I have to do some extra training to be able to catch up to Sha'Carri."
        va "It looks like you had the same idea?"
        mc "Oh no. Honestly, I'd still be sleeping if it wasn't for Nikki."
        scene 09_653 with Dissolve(1)
        ni "Is he lazy at training too?"
        mc "Hey!"
        va "Uh. Sometimes..."
        ni "Hmm, I knew it!"
        mc "I'm here running with you, aren't I?"
        scene 09_654 with Dissolve(1)
        mc "By the way, Val. Your fall earlier, that would've never happened if you didn't wear that hat."
        mc "I told you it makes you clumsy!"
        va "Haha."
        scene 09_655 with Dissolve(1)
        va "I'm starting to believe that. I guess we need to do some more theory crafting."
        mc "Haha, sure."
        scene 09_656 with Dissolve(1)
        va "Anyway, I'll do a few more laps before I have to go home and get ready for school."
        mc "We'll do the same. See you later then."
        va "Yeah. Nice to meet you, Nikki."
        ni "Nice to meet you."
        scene 09_657 with Dissolve(1)
        mc "Lazy, huh?"
        ni "Hmm?"
        scene 09_658 with Dissolve(1)
        ni "What was that about a training camp?"
        mc "Ah, we were at training camp last week and had a competition against three other schools at the weekend."
        ni "Oh... Did you compete?"
        mc "I did."
        ni "And..."
        if MC_Week3_Saturday_TC_Win == True:
            $ Nikki_Visit_Points += 2
            # Nikki_Visit (12)
            scene 09_659 with Dissolve(1)
            mc "Hehe!"
            ni "What? No way! You won?"
            mc "Uh-huh."
            ni "You're kidding! No?"
            scene 09_661 with Dissolve(1)
            ni "Congrats!"
            mc "Thank you."
            ni "I wish I could've seen that."
            scene 09_662 with Dissolve(1)
            ni "As a prize, you may carry me home."
            mc "Haha, shouldn't it be the other way around?"
            ni "No!"
            scene 09_663 with Dissolve(1)
            mc "You're right. You probably can't do it anyway."
            ni "I know what you are doing!"
            mc "..."
            ni "I hate you!"
            ni "I don't want to do it because of your poor reverse psychology attempt, but at the same time, I want to prove you wrong!"
            scene 09_664 with Dissolve(1)
            ni "Get on."
            mc "I was kidding, you don't..."
            ni "Get on!"
            scene 09_665 with Dissolve(1)
            mc "Jumping on now, ready?"
            ni "Go ahead."
            mc "{i}(Getting hard already...){/i}"
            scene 09_666 with Dissolve(1)
            mc "I didn't expect you to be able to do it."
            ni "And I didn't expect you to be this heavy!"
            mc "Haha."
            scene 09_667 with Dissolve(1)
            mc "Obviously all my muscles weigh a lot!"
            ni "Obviously..."
            mc "Alright, I'll get down. Point proven."
        else:
            scene 09_660 with Dissolve(1)
            mc "Not so good, made lots of mistakes and ended up fourth."
            ni "Fourth isn't that bad."
            mc "I should've at least ended up in the top three, though."
        scene black with Dissolve(2)
        pause 2
        stop music fadeout 1.0
        play music ("Music/LoFi Indie 3.mp3", "Music/LoFi Indie 1.mp3", "Music/LoFi Indie 2.mp3") volume 0.2
        scene 09_668 with Dissolve(1)
        ni "Can I shower first, or do you need to get ready for school?"
        mc "I still have time, you can go."
        ni "Thanks."
        scene 09_669 with Dissolve(1)
        ni "Do you have a towel for me? I didn't bring any."
        mc "They're in the bathroom. You'll find them."
        mc "Oh, I need to go to my room to get some clothes."
        ni "Sure, it's your room. You don't have to ask."
        scene 09_670 with Dissolve(1)
        m "Hey, good morning."
        mc "Morning, Mom."
        m "Have you been somewhere?"
        scene 09_671 with Dissolve(1)
        mc "I went for a jog with Nikki."
        m "This early?"
        mc "Yeah, she does this every other day, and when I lived at her house, she always dragged me along."
        m "Hmm, I like her already."
        scene 09_672 with Dissolve(1)
        m "Did you sleep okay on the couch?"
        mc "More or less. It's a little short, though."
        scene 09_673 with Dissolve(1)
        m "Have you had breakfast yet?"
        mc "No, I wanted to cool down a bit and shower first."
        m "Coffee?"
        mc "Yes, please."
        scene 09_674 with Dissolve(1)
        m "Does Nikki drink coffee?"
        mc "She does."
        m "What about breakfast?"
        mc "That depends if she's on some kind of fitness diet or not."
        scene 09_675 with Dissolve(1)
        mc "Mostly she eats a banana after a morning run."
        m "We have those. If she needs anything specific, make a list and send it to me. I'll go shopping after work."
        mc "Will do."
        scene black with Dissolve(2)
        pause 2
        scene 09_676 with Dissolve(1)
        mc "{i}(Was she always this messy?){/i}"
        mc "{i}(Looks like she just randomly packed stuff.){/i}"
        scene 09_677 with Dissolve(1)
        ""
        scene 09_678 with vpunch
        ni "[mc]!"
        scene black with Dissolve(1)
        transform moveup:
            xalign 0.5 yalign 1.0
            linear 5.0 yalign 0.0
        show 09_679 at moveup
        pause 3
        mc "..."
        scene 09_680 with Dissolve(1)
        mc "I'm so sorry, Nikki. I grabbed some clothes from my room and out of habit I went straight to the bathroom."
        mc "I totally forgot that you were in here."
        ni "It's okay. Nothing you haven't seen before."
        ni "You can come in."
        mc "Uh..."
        menu:
            "Wait outside":
                scene 09_681 with Dissolve(1)
                mc "I still have some time. I'll wait until you're ready."
                ni "Five minutes."
                mc "Sure."
                jump Week4_Thursday_Nikki_Morning2
            "Go in[KoGa3AutoWTChange1]{size=-4}(Nikki Visit Points+2) {/size} {/color}":
                $ Nikki_Visit_Points += 2
                # Nikki_Visit (14)
                jump Week4_Thursday_Nikki_Morning_Shower

label Week4_Thursday_Nikki_Morning_Shower:
    if _in_replay:
        $ MC_Week4_Thursday_SleepInEmilyBed = False
        $ Nikki_Week4_Wednesday_Visit_Knows = False
        $ SexCounter_Nikki = 3
        $ MC_SexCounter = 3
    $ SexCounter_Nikki += 1
    $ MC_SexCounter += 1
    if MC_Week4_Thursday_SleepInEmilyBed == True:
        scene 09_683 with Dissolve(1)
        mc "..."
        mc "{i}(I was kinda hoping she'd still be naked.){/i}"
        ni "I'll be ready in five minutes."
        mc "No rush, take your time."
    else:
        scene 09_682 with Dissolve(1)
        mc "..."
        mc "{i}(I was kinda hoping she'd still be naked.){/i}"
        ni "I'll be ready in five minutes."
        mc "No rush, take your time."
        scene 09_683 with Dissolve(1)
        ni "..."
    if Nikki_Week4_Wednesday_Visit_Knows == True:
        jump Week4_Thursday_Nikki_Morning2
    else:
        stop music fadeout 1.0
        play music "Sounds/Shower.mp3" volume 0.3
        scene 09_684 with Dissolve(1)
        ""
        scene 09_685 with Dissolve(1)
        mc "By the way Nikki, do..."
        mc "..."
        scene black with Dissolve(1)
        transform moveup:
            xalign 0.5 yalign 1.0
            linear 5.0 yalign 0.0
        show 09_686 at moveup
        pause 3
        mc "Damn you're beautiful."
        ni "Thank you, and yes, I want to join you!"
        scene 09_687 with Dissolve(1)
        mc "Not the question I had in mind, but I like your answer."
        ni "What was the question?"
        mc "I forgot."
        scene 09_688 with Dissolve(1)
        ""
        scene 09_689 with Dissolve(1)
        ni "Mmm."
        scene 09_690 with Dissolve(1)
        mc "Every time I see them, I... Damn, they are perfect!"
        ni "Heh, thanks."
        scene 09_691 with Dissolve(1)
        mc "I could eat them!"
        ni "Aah-haha..."
        scene 09_692 with Dissolve(1)
        ""
        scene 09_693 with Dissolve(1)
        ""
        scene 09_694 with Dissolve(1)
        ""
        scene 09_695 with Dissolve(1)
        ni "*Moaning* Aah..."
        scene 09_696 with Dissolve(1)
        mc "Fuck. Sorry but you make me so horny, I can't wait anymore."
        ni "Haha. That was my actual intent, to just have a quickie before you go to school."
        mc "Why didn't you say so?"
        ni "Because I'm enjoying what you're doing!"
        mc "Let's make that a to be continued then."
        scene 09_697 with Dissolve(1)
        ""
        show 09_698
        ""
        scene 09_699 with Dissolve(1)
        ""
        show 09_700
        ""
        scene 09_701 with Dissolve(1)
        ni "Hehe..."
        mc "What are grinning at?"
        ni "Just the way you look at my boobs."
        mc "Have you seen how they bounce? Mesmerising..."
        ni "Haha. Keep at it."
        show 09_702
        ""
        show 09_703
        ""
        scene 09_704 with Dissolve(1)
        ni "Moaning*"
        mc "I'm cumming..."
        scene 09_705 with vpunch
        pause 2
        scene 09_705 with vpunch
        ""
        scene 09_706 with Dissolve(1)
        if MC_Week4_Thursday_SleepInEmilyBed == True:
            ni "This was amazing, thank you."
            mc "I agree, but..."
        else:
            mc "Second workout of the day. I'm going to be useless at training today."
            ni "Or even more energized!"
            ni "This was amazing, thank you."
            mc "I agree, but..."
        scene 09_707 with Dissolve(1)
        mc "Despite how amazing this was, you need to go now. I have to shower."
        ni "Haha, you're kicking me out?"
        mc "Yes! It's this or I won't go to school."
        ni "I can soap you in?"
        mc "Don't make it more difficult for me. And the longer I think about it, the more enticing it gets..."
        scene 09_708 with Dissolve(1)
        ni "Fine! I don't want to mess up your perfect attendance!"
        mc "It is actually perfect, if you don't count the few times I was a bit late."
        ni "That's not what perfect attendance means..."
        mc "You're stalling..."
        ni "Haha, sorry. One more kiss? Time for that?"
        scene 09_709 with Dissolve(1)
        ""
        scene 09_710 with Dissolve(1)
        n "*Slap*"
        mc "Now go..."
        ni "Aah-haha. Biting me, slapping me... Is that how they do it here in Madison Springs?"
        mc "Stick around and find out!"
        ni "Mmm..."
        $ renpy.end_replay()
        jump Week4_Thursday_Nikki_Morning2

label Week4_Thursday_Nikki_Morning2:
    scene black with Dissolve(2)
    pause 2
    stop music fadeout 1.0
    play music ("Music/LoFi Indie 3.mp3", "Music/LoFi Indie 1.mp3", "Music/LoFi Indie 2.mp3") volume 0.2
    scene 09_712 with Dissolve(1)
    ni "Ready for school?"
    mc "*Sigh* Yeah... It's gonna be such a long day."
    mc "By the way. Where did you find that shirt? I've been looking for that for days."
    scene 09_713 with Dissolve(1)
    ni "Oh, this one? You kinda forgot it last time."
    mc "Hmm. Can I have it back?"
    ni "No! It's mine now."
    mc "..."
    scene 09_714 with Dissolve(1)
    mc "Before I forget something else..."
    mc "Mom asked me earlier what you mostly eat for breakfast."
    mc "I told her pancakes, so she's making some for you now."
    ni "No, you didn't! [mc], why did you say that? I feel so bad."
    scene 09_715 with Dissolve(1)
    mc "Better go downstairs and eat them before they get cold."
    ni "You're unbelievable!"
    scene black with Dissolve(1)
    pause 2
    scene 09_716 with Dissolve(1)
    ni "Pancakes?"
    mc "Haha."
    ni "Pancakes?"
    mc "That's what you get for stealing my shirt!"
    scene 09_717 with vpunch
    ni "I didn't steal it. You gave it to me!"
    mc "Hey! Haha. No violence in my room."
    scene 09_718 with Dissolve(1)
    ni "I've never been so embarrassed in my life. I could feel my cheeks burning."
    mc "Haha."
    ni "I don't get embarrassed easily, but this..."
    scene 09_719 with Dissolve(1)
    ni "I even asked her where the pancakes were because I didn't see them. Now she thinks I'm some spoiled girl whose mom makes pancakes for her."
    mc "Haha. I wish I'd seen that."
    ni "And then she offered to make some for me..."
    scene 09_720 with Dissolve(1)
    mc "She's probably making them right now. You'd better go check!"
    ni "[mc]!"
    mc "Haha."
    scene 09_721 with Dissolve(1)
    mc "Anyway, I have to go now."
    mc "See you later, I guess. Have fun in whatever you're going to do."
    ni "Planning my revenge!"
    if Nikki_FB_PureEvil == False:
        mc "Haha."
    else:
        mc "Haha. Pure evil!"
        ni "You know it!"
    scene 09_722 with Dissolve(1)
    ni "Have fun."
    mc "Bye, Nikki."
    jump Week4_Thursday_School

label Week4_Thursday_Cara_Morning:
    stop music fadeout 1.0
    play music ("Music/LoFi Indie 3.mp3", "Music/LoFi Indie 1.mp3", "Music/LoFi Indie 2.mp3") volume 0.2
    if MC_Week4_Thursday_SleepInEmilyBed == False:
        scene black with Dissolve(2)
        pause 2
        scene 09_723 with Dissolve(1)
        m "Hey, good morning."
        mc "Morning, Mom."
        m "Are all your clothes in the laundry?"
        mc "I forgot to get some clothes out of my room yesterday."
        scene 09_724 with Dissolve(1)
        m "Your teachers will be thrilled if they see you like this in their classroom."
        if Gabi_End == True:
            pass
        else:
            mc "{i}(Gabi would be, maybe...){/i}"
        mc "Very funny."
        if Zach_Week3_Wednesday_TC_Girlshower == True:
            pass
        else:
            if Zach_Week3_Saturday_TC_Swap == False:
                m "You still have those panties from your friend, too! I've washed them, if you..."
                mc "MOM!"
                m "Haha."
                mc "But good thing you reminded me. I still need to give them back."
            else:
                pass
        scene 09_725 with Dissolve(1)
        m "Coffee?"
        mc "Yes, please."
        scene 09_726 with Dissolve(1)
        m "Does Cara drink coffee?"
        mc "She does."
        m "What about breakfast?"
        mc "She never eats breakfast."
        scene 09_727 with Dissolve(1)
        m "Ask her if she needs anything and make a list and send it to me. I'll go shopping after work."
        mc "Will do."
    else:
        pass
    scene 09_728 with Dissolve(1)
    m "Do you want me to go into your room and get you some clothes?"
    mc "No, I'll go myself."
    m "Make sure to be quiet so you won't wake her."
    scene 09_729 with Dissolve(1)
    mc "{i}(Alright. Quietly!){/i}"
    scene 09_730 with Dissolve(1)
    mc "{i}(She's such a cutie.){/i}"
    scene 09_731 with Dissolve(1)
    mc "..."
    mc "{i}(Just as messy as back in Riverside, huh?){/i}"
    scene 09_732 with Dissolve(1)
    c "[mc]?"
    mc "Sorry, I didn't want to wake you."
    c "What are you doing here?"
    scene 09_733 with Dissolve(1)
    mc "I needed some clothes. I forgot to take them yesterday."
    c "What time is it?"
    mc "Ten to eight."
    scene 09_734 with Dissolve(1)
    c "You need to go to school now?"
    mc "Yes, I'll be leaving in a few minutes."
    c "Can I come with you?"
    scene 09_735 with Dissolve(1)
    mc "Uhm..."
    c "I'll be ready in five minutes."
    mc "Okay, sure."
    menu:
        "Leave the room":
            mc "I'll wait downstairs in the kitchen."
            jump Week4_Thursday_Cara_Morning2
        "Stay[KoGa3AutoWTChange1]{size=-4}(Cara Visit Points+2) {/size} {/color}":
            $ Cara_Visit_Points += 2
            # Cara_Visit (6)
            jump Week4_Thursday_Cara_Morning_Stay

label Week4_Thursday_Cara_Morning_Stay:
    if _in_replay:
        $ Cara_Visit_Points = 6
    scene 09_736 with Dissolve(1)
    mc "{i}(She's undressing here?){/i}"
    mc "{i}(She knows I'm still standing here, right?){/i}"
    scene 09_737 with Dissolve(1)
    mc "{i}(I guess not.){/i}"
    scene 09_738 with vpunch
    c "[mc]!"
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 09_739 at moveup
    pause 3
    c "What are... Why are..."
    scene 09_740 with Dissolve(1)
    mc "Sorry, Cara."
    c "Please, leave..."
    menu:
        "Leave the room":
            mc "Yeah, sorry."
            mc "I'll get my clothes real quick and wait downstairs."
            $ renpy.end_replay()
            jump Week4_Thursday_Cara_Morning2
        "Stay[KoGa3AutoWTChange1]{size=-4}(Cara Visit Points+2) {/size} {/color}":
            $ Cara_Visit_Points += 2
            # Cara_Visit (8)
    scene 09_741 with Dissolve(1)
    mc "Why are you shy all of a sudden?"
    c "I'm not..."
    c "..."
    c "Maybe a bit... Because... I don't know..."
    mc "You're beautiful, Cara!"
    c "Thank you."
    scene 09_742 with Dissolve(1)
    ""
    scene 09_743 with Dissolve(1)
    mc "I enjoyed your little striptease."
    c "That wasn't a striptease..."
    mc "No?"
    scene 09_744 with Dissolve(1)
    c "Don't we have to go?"
    mc "We still have a few minutes."
    scene 09_745 with Dissolve(1)
    mc "And I think you could do with a little longer too!"
    c "..."
    scene 09_746 with Dissolve(1)
    ""
    scene 09_747 with Dissolve(1)
    c "Ah..."
    scene 09_748 with Dissolve(1)
    mc "{i}(I knew she'd enjoy this.){/i}"
    scene 09_749 with Dissolve(1)
    c "Aah... [mc]..."
    show 09_750
    c "*Moaning*"
    scene 09_751 with Dissolve(1)
    ""
    scene 09_752 with Dissolve(1)
    c "Aaaah..."
    mc "{i}(There it is.){/i}"
    scene 09_753 with Dissolve(1)
    c "*Heavy breathing*"
    mc "You good?"
    c "Haah... Yeah..."
    scene 09_754 with Dissolve(1)
    mc "Well, I really need to go now."
    c "School! I forgot about that."
    c "Five minutes, okay? Please wait for me."
    mc "I'll wait downstairs in the kitchen."
    $ renpy.end_replay()
    jump Week4_Thursday_Cara_Morning2

label Week4_Thursday_Cara_Morning2:
    scene black with Dissolve(2)
    pause 2
    scene 09_755 with Dissolve(1)
    c "Kay, I'm ready."
    mc "Five minutes, huh?"
    c "Yes..."
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 09_756 at moveup
    pause 3
    mc "I forgot that your five minutes don't equal mine."
    c "..."
    mc "We need to hurry now."
    mc "{i}(She looks damn cute though, she's definitely going to turn some heads at school.){/i}"
    scene 09_757 with Dissolve(1)
    c "So, do you have a bike or something?"
    mc "No bike."
    c "Car?"
    mc "Nuh-uh. You're going to have to use your legs today."
    mc "I hope you can walk fast in those heels."
    scene black with Dissolve(1)
    pause 2
    scene 09_758 with Dissolve(1)
    c "Do you always walk to school?"
    mc "Yes, it isn't that far."
    c "How far is it?"
    mc "Twenty, twenty-five minutes or so."
    scene 09_759 with Dissolve(1)
    c "And it's an easy route?"
    mc "Heh, planning to pick me up after school?"
    c "Yes, if I remember the way."
    mc "It's pretty easy."
    scene 09_760 with Dissolve(1)
    mc "{i}(Not wearing a bra! Not that she needs one anyway.){/i}"
    mc "{i}(I love her perky boobs.){/i}"
    scene 09_761 with Dissolve(1)
    c "Hmm?"
    mc "Nothing. You just look very cute in that dress."
    c "Thanks."
    scene 09_762 with Dissolve(1)
    mc "So uhm, what are the plans for today?"
    c "I don't know yet. I don't want to walk around the city on my own. I'll probably just wait until you're done with school."
    c "Maybe read or watch a movie or something."
    scene 09_763 with Dissolve(1)
    mc "If you need my computer, you can use it. There's no password on it."
    c "Okay, thank you."
    mc "And maybe you can think of something we can do after school?"
    c "Hmm-mmm."
    mc "By the way, how is the driving going?"
    scene 09_764 with Dissolve(1)
    c "I haven't been able to drive since you taught me."
    c "Nikki works late hours and I don't want to drive in the dark, and Mom... You know, she..."
    mc "Had other stuff going on."
    c "Yeah..."
    scene 09_765 with Dissolve(1)
    mc "Well, if we find time and Mom doesn't need the car, we can..."
    c "Really? That'd be great!"
    mc "It won't be today though, since she goes grocery shopping after work."
    c "That's fine. Maybe tomorrow then."
    scene 09_766 with Dissolve(1)
    c "Haha, I'm really happy I came."
    mc "Uh, Cara..."
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 09_767 at moveup
    pause 3
    mc "{i}(She looks happy.){/i}"
    mc "{i}(Good thing she's wearing panties though.){/i}"
    scene 09_768 with Dissolve(1)
    c "Aaah..."
    mc "Haha."
    c "Stupid wind!"
    scene 09_769 with Dissolve(1)
    mc "Are you going to walk like this the whole way to school?"
    c "Yes!"
    mc "There's no one here, no one saw."
    c "Better safe than sorry."
    scene 09_770 with Dissolve(1)
    mc "If people see you like this, they'll think you had an 'accident'."
    c "[mc]!"
    mc "Haha. Wait, I'll help you."
    scene 09_771 with Dissolve(1)
    mc "Better like this, no?"
    c "..."
    scene black with Dissolve(2)
    pause 2
    scene 09_772 with Dissolve(1)
    mc "This is it. Welcome to my uh... school."
    c "Are you sure you aren't on spring break? No one's here."
    mc "Well, that's because I'm late."
    scene 09_773 with Dissolve(1)
    c "What? Didn't you say we still had some time?"
    mc "That might have been a stretch."
    c "I'm sorry. You should've told me and I..."
    mc "Hey, don't worry about it. It will be fine. It's not the first time I've been a little late."
    scene 09_774 with Dissolve(1)
    mc "I guess I'll see you after school again, or do you want to come with me to class?"
    c "Haha, no thanks. I've earned my break!"
    c "When will you be finished?"
    mc "I've got training this afternoon, so half past three."
    c "Alright, I'll be waiting here then. If I find the way."
    mc "Haha, okay."
    menu:
        "Kiss[KoGa3AutoWTChange1]{size=-4}(Cara Visit Points+4) {/size} {/color}":
            $ Cara_Visit_Points += 4
            # Cara_Visit (12)
            scene 09_777 with Dissolve(1)
            ""
        "Kiss on cheek[KoGa3AutoWTChange1]{size=-4}(Cara Visit Points+2) {/size} {/color}":
            $ Cara_Visit_Points += 2
            # Cara_Visit (10)
            scene 09_776 with Dissolve(1)
            mc "Later."
            c "Bye-bye."
        "Leave":
            scene 09_775 with Dissolve(1)
            mc "Later."
            c "Bye-bye."
    jump Week4_Thursday_School

label Week4_Thursday_School:
    scene black with Dissolve(2)
    pause 2
    stop music fadeout 1.0
    play music ("Music/LoFi Upbeat 1.mp3", "Music/LoFi Upbeat 2.mp3", "Music/LoFi Upbeat 3.mp3", "Music/LoFi Upbeat 4.mp3") volume 0.2
    scene 09_790 with Dissolve(1)
    if Emily_Week3_Sunday_Surprise == True:
        mc "{i}(I haven't seen this car here before.){/i}"
        mc "{i}(Maybe that's Coach's? I could see him in that car.){/i}"
        scene 09_791 with Dissolve(1)
        mc "{i}(No... That's Zach's car? Didn't expect him to get a charger.){/i}"
        mc "{i}(But why this license plate? Zach Attack? Really?){/i}"
    else:
        mc "{i}(Zach came with his new car already.){/i}"
        scene 09_791 with Dissolve(1)
        mc "{i}(No... He didn't! He put Zach Attack on his license plate!){/i}"
    scene 09_792 with Dissolve(1)
    tr "Are you kidding me? Whose car is this?"
    mc "{i}(You're going to be in trouble Zach. This is the teachers' parking.){/i}"
    if Week3_Monday_Spanish_Blackmail == True:
        pass
    else:
        scene 09_793 with Dissolve(1)
        tr "[mc]! Is that your car?"
        mc "No..."
        tr "Do you know whose car it is?"
        menu:
            "Tell her[KoGa3AutoWTChange1]{size=-4}(Zach Points-2) {/size} {/color}":
                $ Zach_Points -= 2
                mc "{i}(Sorry Zach.){/i}"
                mc "I think it's Zach's."
                scene 09_794 with Dissolve(1)
                tr "*Shakes head* Unbelievable!"
                tr "I'm gonna stay parked right here. He can wait until I'm finished for today."
                mc "{i}(Oh shit. Sorry again, Zach.){/i}"
            "You don't know":
                mc "{i}(I'm not going to tell you!){/i}"
                mc "I have no idea."
                tr "*Sigh*"
        if Gabi_End == True:
            pass
        else:
            scene 09_795 with Dissolve(1)
            mc "{i}(Just looking at her gets me hard again.){/i}"
            mc "{i}(Too bad I don't have any classes with her today.){/i}"
            scene black with Dissolve(1)
            transform moveup:
                xalign 0.5 yalign 1.0
                linear 5.0 yalign 0.0
            show 09_796 at moveup
            pause 3
            mc "You're looking pretty."
            tr "You're late!"
            mc "..."
    scene black with Dissolve(1)
    pause 2
    scene 09_797 with Dissolve(1)
    mc "Good morning, Mr Coleman... Sorry, but I..."
    tc "What are you doing here?"
    mc "Taking your class."
    scene 09_798 with Dissolve(1)
    tc "My class? When you're late? I don't think so."
    tc "You should know the rules by now."
    tc "You can wait outside until class is over!"
    mc "I can..."
    tc "Outside. Now!"
    scene 09_799 with Dissolve(1)
    mc "*Sigh* For fuck's sake..."
    mc "I should just drop this class! Who needs geography anyway?"
    if Layla_End == True:
        scene 09_800 with Dissolve(1)
        mc "Oh hey... Morning, Elena. You're also late, huh?"
        el "Don't talk to me!"
        mc "Uhm..."
        el "Despicable!"
        scene 09_801 with Dissolve(1)
        mc "{i}(What did I expect?){/i}"
        mc "{i}(I think there's no way I can fix this. School's gonna be much more boring from now on.){/i}"
        scene black with Dissolve(2)
        pause 2
        scene 09_835 with Dissolve(1)
        mc "..."
        mc "{i}(Layla's not here? Is she sick?){/i}"
        scene 09_836 with Dissolve(1)
        mc "Is Layla sick?"
        el "..."
        mc "Elena?"
        scene 09_837 with Dissolve(1)
        el "I told you not to talk to me!"
        mc "Listen, I..."
        el "NO! I don't want to hear it."
        scene 09_838 with Dissolve(1)
        t "Enough! All you guys do is talk and not pay attention in class."
        t "I've given you plenty of chances, but it just doesn't work."
        scene 09_839 with Dissolve(1)
        t "Jasmine, switch places with [mc]!"
        el "Thank you!"
        mc "..."
        scene 09_840 with Dissolve(1)
        to "Why am I the one being punished here?"
        t "Like you weren't disrupting class with all your chatter?"
        to "..."
        scene 09_841 with Dissolve(1)
        to "Great..."
        mc "I didn't ask for this either!"
        if Tori_Week3_Saturday_TC_Sex == False:
            to "Just be quiet, loser."
            mc "Look who's talking."
            scene 09_842 with Dissolve(1)
            mc "*Sigh*"
            mc "{i}(This is going to be such a long day.){/i}"
            jump Week4_Thursday_School_Hallway
        else:
            jump Week4_Thursday_School_Tori_HJ
    else:
        scene 09_802 with Dissolve(1)
        el "Hey there. Been kicked out?"
        mc "Morning, Elena. Yeah, I was late."
        el "And that's the best place you could choose to sit?"
        mc "Well..."
        scene 09_803 with Dissolve(1)
        el "Haha."
        mc "And why are you laughing? Seems like you're late too."
        el "I am."
        mc "There's a place right here next to me. See you soon."
        el "Uh-huh."
        scene 09_804 with Dissolve(1)
        mc "{i}(Isn't she coming back out?){/i}"
        mc "{i}(Don't tell me she can stay but I had to leave?){/i}"
        mc "{i}(Seriously...){/i}"
        scene black with Dissolve(2)
        pause 2
        scene 09_805 with Dissolve(1)
        la "Hey, [mc]."
        mc "Hi."
        el "Look at this little perrito. Still waiting for us, so cute."
        mc "*Sigh* Elena..."
        scene 09_806 with Dissolve(1)
        la "What's a perrito?"
        el "Puppy."
        la "He does look like a puppy sitting there."
        el "Haha."
        if Layla_Dating == False:
            pass
        else:
            scene 09_807 with Dissolve(1)
            la "*Whispers* My little perrito!"
            mc "Heh..."
            mc "How are you?"
            la "Good."
        if MC_Girlfriend_Riverside == True:
            scene 09_809 with Dissolve(1)
            la "Why were you late?"
            mc "My girlfriend is visiting."
            la "You have a girlfriend?"
            el "Yeah, that! Why is this the first time we're hearing about that?"
            mc "Because it's somewhat complicated and a long story."
            scene 09_810 with Dissolve(1)
            el "I'm even more curious now!"
            la "We have something to talk about during lunch."
            mc "Who says I'm..."
            el "What do you think she looks like?"
            mc "*Sigh*"
            la "No idea, but she must be cute, no?"
            el "I don't know."
        else:
            scene 09_808 with Dissolve(1)
            la "Why were you late?"
            mc "Overslept."
            el "I would've kicked you out for oversleeping, too."
            mc "What's your excuse then, Elena?"
            el "I had to take my brothers to school."
            mc "Hmm... Fair enough, I guess."
        if Layla_Dating == True:
            scene 09_811 with Dissolve(1)
            la "I really want to kiss you."
            el "Okaaay... That's my cue to leave. See you in chemistry."
            mc "Heh... Later, Elena."
            scene 09_812 with Dissolve(1)
            la "Good, she's gone."
            mc "Wait, what?"
            la "I said that because I needed her to leave. I have to show you something."
            mc "So, no kiss?"
            la "Sorry, not here. But..."
            scene black with Dissolve(1)
            pause 2
            scene 09_813 with Dissolve(1)
            ""
            scene 09_814 with Dissolve(1)
            mc "{i}(Toilets will do I guess.){/i}"
            scene 09_815 with Dissolve(1)
            mc "The girls' toilets. So romantic!"
            la "This was the best place I could think of where no one would see us."
            mc "I'm just teasing. I like kissing you, it doesn't matter where."
            scene 09_816 with Dissolve(1)
            la "Only kissing?"
            mc "Now you're teasing me?"
            la "Maybe..."
            mc "..."
            scene 09_817 with Dissolve(1)
            la "Anyway. I wanted to show you something."
            mc "Right. I forgot about that."
            scene 09_818 with Dissolve(1)
            la "Here, what do you think?"
            mc "Wait... Is that a..."
            la "Yeah. Next time we go, you can use this."
            mc "That's amazing! Where did you get it?"
            la "Bought it from a website. I'll bring it tomorrow."
            scene 09_819 with Dissolve(1)
            mc "This is going to be so much fun."
            la "Haha, she's gonna hate it."
            mc "Oh yeah! I love it. Can't wait."
            scene 09_820 with Dissolve(1)
            mc "Do you have one of yourself too?"
            la "No. I only ordered this one to test it."
            mc "Oh, too bad."
            la "You want one of me?"
            scene 09_821 with Dissolve(1)
            mc "Uh-huh."
            la "Hehe, okay. I'll order one."
            mc "How much is it?"
            la "It's fine. It's not expensive."
            mc "Alright. Thank you, Layla."
            la "I just need to pick out a..."
            n "*Peeing noises*"
            scene 09_822 with Dissolve(1)
            la "..."
            mc "Is that?"
            scene 09_823 with Dissolve(1)
            la "Don't listen!"
            mc "Haha."
            scene 09_824 with Dissolve(1)
            mc "I kinda need to go too, now."
            la "What? Now? Here?"
            mc "Uh... I want to go before the next class starts and this is a toilet! So..."
            scene 09_825 with Dissolve(1)
            la "I mean, I'm here and..."
            mc "I don't expect you to stay here, just wait outside."
            la "..."
            scene 09_826 with Dissolve(1)
            la "[mc]?"
            mc "Hmm?"
            la "Can I do it?"
            mc "Do what?"
            scene 09_827 with Dissolve(1)
            la "Hold it."
            mc "You mean..."
            la "Yeah."
            menu:
                "Yes[KoGa3AutoWTChange1]{size=-4}(Layla Week4 Thursday HoldPenis, Layla Points+2) {/size} {/color}":
                    $ Layla_Week4_Thursday_HoldPenis = True
                    $ Layla_Points += 2
                    # Layla (68)
                    scene 09_828 with Dissolve(1)
                    mc "Uhm... That's..."
                    la "It's fine, I..."
                    mc "Okay!"
                    la "Okay? I can?"
                    mc "Yeah."
                    scene black with Dissolve(1)
                    pause 2
                    scene 09_829 with Dissolve(1)
                    mc "{i}(This isn't weird, right?){/i}"
                    mc "{i}(Maybe a little...){/i}"
                    mc "{i}(Why is she holding it so tight?){/i}"
                    scene 09_830 with Dissolve(1)
                    mc "Hey, you don't have to hold it so tight. You're not giving me a handjob!"
                    la "[mc]!"
                    mc "What? You wanted to do this."
                    scene 09_831 with Dissolve(1)
                    la "Like this?"
                    mc "Yeah, just balance it on your hand I guess and uh... aim."
                    scene 09_832 with Dissolve(1)
                    la "Is it coming? Nothing's happening."
                    mc "..."
                    mc "I'm kinda having a hard time... Almost literally."
                    mc "{i}(Concentrate... Stop thinking about this...){/i}"
                    mc "Give me a second."
                    scene 09_833 with Dissolve(1)
                    la "Oh wow... I can actually feel it. This is so weird."
                    mc "That is weird? The fact you're holding my penis while I pee is weirder to me!"
                    scene 09_834 with Dissolve(1)
                    la "Haha."
                    mc "Watch where you are aiming. I'm not cleaning it if you hit the rim!"
                "No":
                    mc "I don't think I'll be able to do it when you're holding it."
                    la "..."
                    la "I'll wait outside."
            scene black with Dissolve(1)
            pause 2
            scene 09_856 with Dissolve(1)
            el "What's up with that smirk?"
            mc "Hehe."
            el "You and Layla planned something, right?"
            scene 09_857 with Dissolve(1)
            el "What did you talk about?"
            mc "Nothing."
            el "I don't believe you."
            mc "Oh well. Then I guess you'll just have to wait and see."
            el "..."
            scene 09_858 with Dissolve(1)
            el "Te odio!\n(I hate you!)"
            mc "Haha."
            scene 09_859 with Dissolve(1)
            mc "I like you though."
            mc "You're my favourite chemistry partner!"
            el "..."
            scene 09_860 with Dissolve(1)
            mc "And look, we even match today. Last time you were so jealous that Layla and I were both wearing shirts with skulls."
            el "So jealous..."
            scene 09_861 with Dissolve(1)
            el "You say we're matching, but where are your white pants?"
            mc "I don't have a white pair."
            mc "And aren't those Layla's pants? You wore them when we were at the club."
            el "Wow, you remember that."
            if Elena_Points >= 25:
                scene 09_862 with Dissolve(1)
                el "They're mine now. She gave them to me."
                el "She said they look really good on me."
                scene 09_863 with Dissolve(1)
                mc "She's right. Your ass looks great in them too."
                el "..."
                mc "{i}(Shit! Did I say that out loud?){/i}"
                scene 09_864 with Dissolve(1)
                el "Haha."
                mc "Sorry, I..."
                el "Don't worry, I'll take the compliment."
            else:
                scene 09_862 with Dissolve(1)
                el "They're mine now. She gave them to me."
                el "She said they look really good on me."
                mc "She's right. You look good in them."
                el "Haha. Thank you!"
        else:
            scene black with Dissolve(1)
            pause 2
            scene 09_856 with Dissolve(1)
            el "..."
            el "What are you looking at?"
            scene 09_857 with Dissolve(1)
            mc "I just noticed that we're matching. We're both wearing white."
            el "You should've worn white pants, though."
            mc "I don't have a white pair."
            mc "And aren't those Layla's pants? You wore them when we were at the club."
            el "Wow, you remember that."
            scene 09_862 with Dissolve(1)
            el "They're mine now. She gave them to me."
            el "She said they look really good on me."
            mc "She's right. They do."
            el "Haha, thank you."
        scene 09_838 with Dissolve(1)
        t "Enough! All you guys do is talk and not pay attention in class."
        t "I've given you plenty of chances, but it just doesn't work."
        t "Jasmine, switch places with [mc]!"
        mc "..."
        scene 09_840 with Dissolve(1)
        to "Why am I the one being punished here?"
        t "Like you weren't disrupting class with all your chatter?"
        to "..."
        scene 09_865 with Dissolve(1)
        el "Sorry, I shouldn't have laughed so loud."
        mc "It's not your fault."
        mc "This is going to be so boring now. Gonna miss you, partner."
        el "Me too."
        scene 09_841 with Dissolve(1)
        to "Great..."
        mc "I didn't ask for this either!"
        if Tori_Week3_Saturday_TC_Sex == False:
            to "Just be quiet, loser."
            mc "Look who's talking."
            scene 09_842 with Dissolve(1)
            mc "*Sigh*"
            mc "{i}(This is going to be such a long day.){/i}"
            jump Week4_Thursday_School_Hallway
        else:
            jump Week4_Thursday_School_Tori_HJ

label Week4_Thursday_School_Tori_HJ:
    $ Tori_Week3_Thursday_School_HJ = True
    scene 09_842 with Dissolve(1)
    mc "*Sigh*"
    mc "{i}(This is going to be such a long day.){/i}"
    scene 09_843 with Dissolve(1)
    mc "{i}(I thought that maybe after what happened at training camp we could...){/i}"
    mc "{i}(*Sigh* Never mind. It's Tori...){/i}"
    scene 09_844 with Dissolve(1)
    mc "..."
    mc "{i}(She looks damn fine, though.){/i}"
    scene 09_845 with Dissolve(1)
    to "What are you looking at? Just because we fucked, doesn't mean we're friends now."
    mc "Who says anything about being friends?"
    to "Heh, can't get enough of me then? You want to fuck me again?"
    mc "..."
    mc "{i}(I wouldn't mind, to be honest. She gets me hard so easily.){/i}"
    scene 09_846 with Dissolve(1)
    to "I guess it's your lucky day. How about a little fun?"
    mc "Here?"
    to "Yes!"
    scene 09_847 with Dissolve(1)
    to "Hard already. Do I make you this horny?"
    scene 09_848 with Dissolve(1)
    mc "{i}(This is so crazy.){/i}"
    mc "{i}(But it turns me on so much!){/i}"
    mc "{i}(If I could I'd fuck her on this desk right now.){/i}"
    t "Tori."
    scene 09_849 with Dissolve(1)
    mc "{i}(Shit!){/i}"
    to "Yes?"
    t "What do you get when you combine H2O with CO2?"
    scene 09_850 with Dissolve(1)
    mc "{i}(Wait... She's just continuing? Seriously, this girl...){/i}"
    to "H2CO3, carbonic acid."
    t "Correct."
    show 09_851
    mc "{i}(This is so good.){/i}"
    mc "{i}(The excitement of getting caught makes it even better.){/i}"
    scene 09_852 with Dissolve(1)
    mc "You need to stop soon, I'm close to..."
    to "Don't worry, I've got it."
    scene 09_853 with Dissolve(1)
    mc "Uh..."
    mc "{i}(I guess this works.){/i}"
    scene 09_854 with Dissolve(1)
    mc "{i}(I hope no one noticed.){/i}"
    scene 09_855 with Dissolve(1)
    mc "That was amazing!"
    to "Like I said at camp, we should've done this way earlier."
    to "Think of all the fun we could've had."
    mc "We still can."
    to "Then show me what you've got! And if I like it, I might have a surprise for you!"
    $ renpy.end_replay()
    jump Week4_Thursday_School_Hallway

label Week4_Thursday_School_Hallway:
    if Layla_End == True:
        scene black with Dissolve(2)
        pause 2
        scene 09_873 with Dissolve(1)
        z "Hey, man."
        mc "Hey."
        z "Where are the girls?"
        mc "No idea. We aren't really on speaking terms anymore."
        z "Are they on their period or something?"
        mc "Or something."
        if Emily_Week3_Sunday_Surprise == True:
            scene 09_871 with Dissolve(1)
            z "I need to show you something."
            mc "Talking about your car?"
            z "You saw it already?"
            scene 09_872 with Dissolve(1)
            mc "I did. Checked it out when I was late."
            mc "It's really cool."
            z "Right? I even have a name for it."
            mc "Let me guess. Zach Attack?"
            z "Haha, yeah. How did you... Oh, you probably saw my license plate. Isn't it the coolest name ever?"
            z "Zach Attack!"
        else:
            scene 09_871 with Dissolve(1)
            z "Damn. I wanted to show them something."
            mc "Talking about your car?"
            z "Hehe, yeah."
            scene 09_872 with Dissolve(1)
            mc "I saw your license plate this morning."
            z "Haha. Awesome, right?"
            z "Zach Attack!"
        scene 09_873 with Dissolve(1)
        z "By the way. Do you have plans for tomorrow? I've got something nice planned."
        mc "Uhm, I don't know yet."
        z "No, dude. You have to come. I'm not here during spring break, so we can't hang out then. And let me tell you, you don't want to miss this."
        mc "Alright... Sure I guess."
        z "Cool, I'll pick you up after school."
        scene 09_874 with Dissolve(1)
        z "Oh, and have you seen Valeria? I want to show her my car."
        mc "Haven't seen her yet."
        z "Hmm. Guess I'll go look for her. See you later."
        mc "Good luck."
        jump Week4_Thursday_Afterschool
    else:
        scene black with Dissolve(2)
        pause 2
        scene 09_866 with Dissolve(1)
        la "Hey, do we need to save a spot for you or are you eating with Tori?"
        mc "..."
        if Tori_Week3_Thursday_School_HJ == True:
            mc "{i}(For a moment I thought she knew about the handjob...){/i}"
        else:
            pass
        mc "You think you're so funny, don't you?"
        la "Haha, I am funny!"
        scene 09_867 with Dissolve(1)
        la "So?"
        mc "Let me put my stuff away and I'll join you."
        z "Ah, there you are!"
        scene 09_868 with Dissolve(1)
        z "Good, you're all together."
        la "Hey, Zach."
        mc "What's up?"
        z "You need to come with me. I need to show you something amazing! It's outside."
        scene 09_869 with Dissolve(1)
        el "Whatever it is, I'm not interested in the slightest."
        el "Go have fun."
        z "..."
        scene 09_870 with Dissolve(1)
        la "Yeah, sorry, Zach. We're going to eat first. Maybe later."
        z "Come on. It's really awesome!"
        z "*Sigh*"
        if Emily_Week3_Sunday_Surprise == True:
            scene 09_871 with Dissolve(1)
            z "Do you want to see it?"
            mc "Talking about your car?"
            z "You saw it already?"
            scene 09_872 with Dissolve(1)
            mc "I did. Checked it out when I was late."
            mc "It's cool."
            z "Right? I even have a name for it."
            mc "Let me guess. Zach Attack?"
            z "Haha, yeah. How did you... Oh, you probably saw my license plate. Isn't it the coolest name ever?"
            z "Zach Attack!"
        else:
            scene 09_871 with Dissolve(1)
            mc "Talking about your car?"
            z "Yeah..."
            scene 09_872 with Dissolve(1)
            mc "I saw your license plate this morning."
            z "Haha. Awesome, right?"
            z "Zach Attack!"
        scene 09_873 with Dissolve(1)
        z "By the way. Do you have plans for tomorrow? I've got something nice planned."
        mc "Uhm, I don't know yet."
        z "No, dude. You have to come. I'm not here during spring break, so we can't hang out then. And let me tell you, you don't want to miss this."
        mc "Alright... Sure I guess."
        z "Cool, I'll pick you up after school."
        scene 09_874 with Dissolve(1)
        z "Oh, and have you seen Valeria? I want to show her my car."
        mc "Haven't seen her yet."
        z "Hmm. Guess I'll go look for her. See you later."
        mc "Good luck."
        scene black with Dissolve(1)
        pause 2
        scene 09_875 with Dissolve(1)
        mc "Hey there."
        va "Hey, [mc]."
        scene black with Dissolve(1)
        transform moveup:
            xalign 0.5 yalign 1.0
            linear 5.0 yalign 0.0
        show 09_876 at moveup
        pause 3
        mc "No skirt today?"
        va "That was a once-in-a-while outfit."
        va "I'd rather wear this."
        scene 09_877 with Dissolve(1)
        va "Besides, this is much more comfortable."
        mc "And suits you better."
        mc "No, that's not true. Honestly, you looked good in a skirt, too."
        va "Haha, thanks."
        scene 09_878 with Dissolve(1)
        mc "Zach is looking for you."
        va "I know. He's been texting me non-stop since yesterday to the point of annoyance."
        va "He was very secretive about something he wants to show me."
        mc "Zach Attack..."
        va "Huh?"
        mc "Nothing."
        scene 09_879 with Dissolve(1)
        mc "You're heading to the cafeteria too?"
        va "No, I'll go for a short jog first."
        mc "Now? You really are crazy!"
        va "Haha."
        scene 09_880 with Dissolve(1)
        va "But cute, right?"
        mc "Heh..."
        scene 09_881 with Dissolve(1)
        va "Want to join me?"
        mc "You do know we have training in the afternoon?"
        va "That's why it'll only be a short jog."
        mc "Next time."
        va "I'll keep you to it."
        scene 09_882 with Dissolve(1)
        va "See you later then."
        mc "Later, Val."
        if Valeria_Points >= 9:
            scene 09_883 with Dissolve(1)
            mc "{i}(Man...){/i}"
            scene 09_884 with Dissolve(1)
            va "Why did you turn around?"
            mc "You wouldn't know that if you didn't turn around yourself!"
            va "Hmm..."
            scene 09_885 with Dissolve(1)
            mc "I was just looking at your pants."
            va "My pants, uh-huh..."
            mc "Yeah, they're cool. What's your excuse?"
            va "I don't have one! I just felt like looking!"
            scene 09_886 with Dissolve(1)
            mc "{i}(Haha, this girl.){/i}"
            scene 09_887 with Dissolve(1)
            va "I knew it!"
            mc "I was just checking if you..."
            va "Go eat!"
            mc "Go run!"
            scene 09_888 with Dissolve(1)
            mc "Haha."
            scene 09_889 with Dissolve(1)
            z "..."
        else:
            scene 09_889 with Dissolve(1)
            z "..."
        scene black with Dissolve(2)
        pause 2
        scene 09_890 with Dissolve(1)
        tm "I know this is our last training before spring break."
        tm "But that doesn't mean you can slack off for a whole week."
        tm "I expect everyone to keep up their conditioning."
        tm "And to make it easier for you, I've created a personal training schedule for everyone. Come pick yours up in my office later."
        scene 09_892 with Dissolve(1)
        la "Do you want water?"
        mc "I'm good, thanks."
        la "Banana?"
        mc "Haha, can't get rid of your bananas, huh?"
        la "No one wants them."
        scene 09_893 with Dissolve(1)
        la "Let's go running together during the break."
        mc "Yeah, I had the same idea. I most likely wasn't gonna do it on my own."
        mc "Having someone coming with surely helps."
        scene 09_894 with Dissolve(1)
        la "You're joining us too, Val?"
        va "I'd love to."
        if Layla_Week3_Friday_TC_Wager == False:
            jump Week4_Thursday_School_Track
        else:
            scene 09_895 with Dissolve(1)
            mc "Good. Then you girls can run that one lap, naked..."
            la "What?"
            mc "The bet, remember? I won!"
            la "I remember, I'd hoped you'd forget."
            scene 09_896 with Dissolve(1)
            la "Can we just forget about it? It was stupid anyway. Please?"
            mc "Haha. Now it's stupid? You were so confident before. If I had lost, I'm pretty sure you'd make me run."
            la "*Sigh*"
            menu:
                "Forget about it":
                    scene 09_897 with Dissolve(1)
                    mc "Fine... You don't have to do it."
                    la "Really?"
                    mc "But I'll get a pass too, if I lose a bet."
                    la "Sure."
                    scene 09_898 with Dissolve(1)
                    la "Thank you, [mc]."
                    jump Week4_Thursday_School_Track
                "Do the bet[KoGa3AutoWTChange1]{size=-4}(Layla Points+2, Valeria Points+2, Layla Week4 Thursday Val NakedRun) {/size} {/color}":
                    $ Layla_Points += 2
                    # Layla (70)
                    $ Valeria_Points += 2
                    # Valeria (16)
                    $ Layla_Week4_Thursday_Val_NakedRun = True
                    jump Week4_Thursday_School_NakedRun

label Week4_Thursday_School_NakedRun:
    if _in_replay:
        $ Alexis_Dating = True
        $ Layla_Points = 70
        $ Valeria_Points = 16
    scene 09_899 with Dissolve(1)
    mc "Here's an idea. You can do it now."
    la "Now? Here?"
    mc "Yeah, look! No one's here. Who knows who'll be at the park and will see you."
    mc "{i}(Lucas comes to mind...){/i}"
    la "..."
    la "Let me talk to Val first."
    scene 09_900 with Dissolve(1)
    la "Look, it was my bet, you don't have to do this."
    va "It's fine, I agreed to it."
    la "Okay, thanks. I'm feeling a bit more comfortable doing it with the two of us."
    la "So..."
    scene black with Dissolve(1)
    pause 2
    scene 09_901 with Dissolve(1)
    la "Okay, we're doing it now, but..."
    mc "But?"
    la "We're only going topless, not completely naked!"
    mc "Alright, that's fine."
    scene 09_902 with Dissolve(1)
    la "I'm so nervous."
    va "I don't get nervous often, but now..."
    la "Big breath. Let's get this over with."
    scene 09_903 with Dissolve(1)
    la "It's time for you to turn around."
    mc "I can't watch?"
    la "You can watch when we're running, now turn around."
    scene 09_904 with Dissolve(1)
    mc "Better?"
    la "Thank you. If you see someone, shout."
    mc "Will do."
    mc "{i}(I really want to look though...){/i}"
    menu:
        "Peek[KoGa3AutoWTChange1]{size=-4}(Layla Points-4, Valeria Points-4) {/size} {/color}":
            $ Layla_Points -= 4
            $ Valeria_Points -= 4
            scene 09_905 with Dissolve(1)
            mc "{i}(Just a bit more...){/i}"
        "Don't peek":
            pass
    scene 09_906 with Dissolve(1)
    la "One lap, right?"
    mc "You're going to run like that?"
    la "Like what?"
    mc "You know what I mean..."
    la "Haha."
    scene 09_907 with Dissolve(1)
    mc "Can I have a little peek at least? Please?"
    la "Haha."
    la "What do you think, Val?"
    va "Sure, I guess."
    la "Ready?"
    if Alexis_Dating == True:
        scene 09_907a with Dissolve(1)
        la "By the way. I'm telling Lexi you're looking at other girls. Naked girls!"
        mc "Please don't."
        va "Your sister?"
        la "Yes, they're dating."
        va "Oh, I didn't know that."
    else:
        pass
    scene 09_908 with Dissolve(1)
    la "Aaah..."
    mc "*Shakes head*"
    mc "{i}(Please turn around...){/i}"
    scene 09_909 with Dissolve(1)
    mc "{i}(What are they doing? Waving?){/i}"
    mc "{i}(It's too far away. I can't see anything.){/i}"
    mc "{i}(I don't know who's the bigger tease out of those two...){/i}"
    scene 09_910 with Dissolve(1)
    la "And we are done! Punishment completed!"
    mc "{i}(If this is punishment, I want to be punished every day!){/i}"
    scene 09_910a with Dissolve(1)
    mc "..."
    la "Look at that happy face."
    scene 09_910b with Dissolve(1)
    mc "Hehe. Congrats! I didn't think you would do it."
    mc "High five, girls!"
    va "Haha."
    la "Nice try. I almost fell for it. Now turn around again!"
    mc "..."
    scene black with Dissolve(1)
    pause 2
    scene 09_911 with Dissolve(1)
    la "I still can't believe we did that."
    va "I'm not joining your bets anymore, Layla."
    la "Haha, sorry!"
    scene 09_912 with Dissolve(1)
    la "Did you enjoy it, at least?"
    mc "I more than enjoyed it."
    va "..."
    mc "Okay, that sounded weird."
    la "Haha."
    mc "But honestly. It was pretty sexy!"
    $ renpy.end_replay()
    jump Week4_Thursday_School_Track

label Week4_Thursday_School_Track:
    scene 09_913 with Dissolve(1)
    va "I guess it's time for me to hit the showers and head home."
    mc "..."
    la "Lucky you. I have to wait until Mom's ready."
    la "By the way, Val. Where did you get those leggings? I really like them!"
    scene 09_914 with Dissolve(1)
    va "Thanks. I got them at the store you recommended, Delta Sport."
    la "Right, we wanted to go there sometime. Let's go next week, I need some stuff too."
    va "Sure."
    scene 09_915 with Dissolve(1)
    va "See you tomorrow."
    la "Bye-bye."
    mc "Later, Val."
    scene 09_916 with Dissolve(1)
    la "I saw you looking."
    mc "Oh, come on... It wasn't my fault. I turned around and... I didn't know she... Never mind."
    mc "I was looking at her pants, okay? Just like you!"
    la "Uh-huh, her pants."
    if Alexis_Dating == True:
        scene 09_919 with Dissolve(1)
        la "I'm telling Lexi!"
        mc "Is that your new go-to sentence every time I look or speak to another girl?"
        mc "A female teacher asks me a question and I answer and you go:"
        mc "*Girly voice* Lexi, I saw [mc] talking with another girl and..."
        la "Haha. I don't sound like that! I was just teasing you."
        scene 09_920 with Dissolve(1)
        la "How are things with Lexi and you?"
        mc "They're good."
        la "Have you made plans with her during spring break?"
        mc "No, not yet. Maybe drive somewhere. We'll see."
        scene 09_922 with Dissolve(1)
        mc "Anyway, I'll go shower too."
        la "Yeah, I'm slowly getting ready as well. It can't be too much longer for Mom to finish up."
        mc "I'll help you up."
        la "Thanks."
        jump Week4_Thursday_Afterschool
    else:
        if Layla_Dating == False:
            scene 09_921 with Dissolve(1)
            la "She has a nice butt though, right?"
            mc "I'm not gonna comment on that."
            if MC_Girlfriend_Riverside == False:
                $ Layla_Week4_Thursday_WingmanVal = True
                la "Why don't you ask her out?"
                mc "..."
            else:
                pass
            scene 09_922 with Dissolve(1)
            mc "Anyway, I'll go shower too."
            la "Yeah, I'm slowly getting ready as well. It can't be too much longer for Mom to finish up."
            mc "I'll help you up."
            la "Thanks."
            jump Week4_Thursday_Afterschool
        else:
            pass
    scene 09_917 with Dissolve(1)
    la "She has a nice butt though, right?"
    mc "I'm not gonna comment on that."
    la "Haha. Do I have a nice butt?"
    mc "Why do you think I joined the track team?"
    scene 09_918 with Dissolve(1)
    la "Good!"
    scene black with Dissolve(1)
    pause 2
    scene 09_923 with Dissolve(1)
    mc "Have you seen Zach's car already?"
    la "Zach has a car?"
    mc "Yeah, that's the thing he wanted to show you. He..."
    el "There you are!"
    scene 09_924 with vpunch
    la "Elena!"
    mc "Fuck, that scared me."
    el "What are you kids doing here?"
    el "I've been looking for you all over the school. Valeria finally told me where you were."
    scene 09_925 with Dissolve(1)
    el "What were you talking about? A car?"
    la "Yeah, seems like Zach has a car."
    el "Who's idea was it to let that guy on the road?"
    la "Haha, you're so mean, El."
    scene 09_926 with Dissolve(1)
    mc "You know, you can come to this side of the wall, this isn't..."
    el "Wow! Eres un idiota! You're a Latino as well, remember? Maybe you should come to this side."
    mc "Haha, maybe. Or maybe you're waiting for a spiderman kiss?"
    el "Huh?"
    scene 09_927 with Dissolve(1)
    el "Watch out!"
    mc "..."
    scene 09_928 with Dissolve(1)
    el "What's with that look?"
    mc "It's just... I don't know how to explain it. I know you're on the cheerleading squad. I've seen you jump, do flippy things, splits."
    mc "You're very athletic, but every time you do stuff like that, it impresses me and I can't get used to it for some reason."
    el "Thanks, I guess..."
    mc "It's definitely a compliment!"
    scene 09_929 with Dissolve(1)
    el "And what's a spiderman kiss?"
    mc "You don't know it? Never seen the movie?"
    el "My brothers watch it all the time, but I can't really remember any of it."
    mc "Well it's basically an upside-down kiss, I guess."
    scene 09_930 with Dissolve(1)
    mc "He was hanging upside-down from a building and kissed a girl standing on the street."
    la "Does that even work in real life? Kissing upside-down?"
    mc "It should, I think..."
    la "I want to try. Can we?"
    mc "Sure."
    scene 09_931 with Dissolve(1)
    la "So, I'm going to lean over the wall, as Elena did before?"
    mc "You want to do it like that? We can just do it while lying down."
    la "No, where's the fun in that? I want to be spiderman... girl. Spidergirl!"
    scene 09_932 with Dissolve(1)
    mc "Just be careful. Can't have you smashing your pretty face."
    el "I'll hold you up so you don't faceplant."
    la "Thanks."
    scene 09_933 with Dissolve(1)
    la "This is more difficult than I thought."
    mc "Tell me if I need to hold you."
    la "I've got it for now."
    scene 09_934 with Dissolve(1)
    el "All this hassle for a kiss?"
    la "You're so not romantic, Elena!"
    el "Yeah, because this looks so romantic..."
    scene 09_935 with Dissolve(1)
    mc "Hi!"
    la "Haha. Hi."
    mc "Ready?"
    la "Uh-huh."
    scene 09_936 with Dissolve(1)
    ""
    scene 09_937 with Dissolve(1)
    mc "{i}(This isn't bad at all, quite the opposite.){/i}"
    if Elena_Points >= 25:
        scene 09_938 with Dissolve(1)
        el "..."
    else:
        pass
    scene 09_939 with Dissolve(1)
    la "That was so much fun! You have to try this, Elena!"
    el "Very funny..."
    mc "*Slap* You can get up again now, or else we'll leave you hanging here."
    el "That's a good idea!"
    la "Nooo-haha..."
    scene 09_940 with Dissolve(1)
    la "You can't do this for too long though, all the blood rushes to your head."
    mc "I have the same issue."
    el "Dios mío..."
    la "Heh? You weren't even upside down."
    scene 09_941 with Dissolve(1)
    el "Not what he meant, Layla."
    la "..."
    mc "Haha, sorry, Elena."
    el "I'm used to it already..."
    scene 09_942 with Dissolve(1)
    mc "What are the plans for spring break?"
    la "Beach!"
    mc "Yes, at least two beach days, if not every day."
    la "Haha, yeah. Uh... Clubbing!"
    scene 09_943 with Dissolve(1)
    el "Babysitting!"
    la "What? Don't tell me you need to watch your brothers for the whole week like last year."
    el "Not the whole week, but most days."
    la "..."
    scene 09_944 with Dissolve(1)
    mc "So, party at Elena's then, I guess."
    el "Haha, no!"
    mc "Hot tub party at Layla's?"
    la "We can do that."
    scene 09_945 with Dissolve(1)
    la "*Whispers* But not the kind of hot tub party you're thinking of."
    mc "*Whispers* Maybe a little?"
    scene 09_946 with Dissolve(1)
    el "We can talk about this some more tomorrow, but now I have to go and pick up my brothers."
    la "You're going to shower first?"
    el "Yes."
    la "I'll come with you, then."
    scene 09_947 with Dissolve(1)
    mc "Let's all shower together!"
    el "Uh-huh..."
    if Elena_Points >= 25:
        mc "We already had a three-way kiss, we even compared..."
        el "What happened at training camp..."
        la "Haha."
    else:
        pass
    scene 09_948 with Dissolve(1)
    mc "But you're my partner, Elena. We have to do this together."
    el "Chemistry partner, not shower partner!"
    mc "Tomayto, tomahto..."
    el "And since today, not even chemistry partners anymore. That's Tori now. Ask her!"
    mc "You'll always be the chemistry partner in my heart."
    scene 09_949 with Dissolve(1)
    el "Besides. You showering with us won't help your condition."
    mc "What condition?"
    el "The blood rushing to your head."
    mc "Haha. That's so true."
    scene 09_950 with Dissolve(1)
    la "I still don't get that."
    mc "Don't ever lose your innocence, Layla."
    el "Haha, so pure."
    scene 09_951 with Dissolve(1)
    la "I don't know if you're complimenting or making fun of me."
    el "And this time we aren't even speaking Spanish!"
    la "Ugh... You both are assholes!"
    scene 09_952 with Dissolve(1)
    mc "You'd better take that back."
    la "Aah-haha!"
    jump Week4_Thursday_Afterschool

label Week4_Thursday_Afterschool:
    if Nikki_Girlfriend == True:
        jump Week4_Thursday_Nikki
    else:
        if Cara_Girlfriend == True:
            jump Week4_Thursday_Cara
        else:
            jump Week4_Friday_Afternoon

label Week4_Thursday_Nikki:
    $ Tori_Week4_Thursday_SeeNikki = True
    $ Mike_Week4_Thursday_NikkiCaraDad = True
    scene black with Dissolve(2)
    pause 2
    scene 09_955 with Dissolve(1)
    ""
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 09_956 at moveup
    pause 3
    mc "{i}(Nikki... She's picking me up.){/i}"
    mc "{i}(Looks like she's daydreaming. So cute.){/i}"
    scene 09_957 with Dissolve(1)
    mc "Hey there, miss. Can I help you? Are you looking for someone?"
    ni "Not anymore. Found what I came for."
    menu:
        "Kiss[KoGa3AutoWTChange1]{size=-4}(Nikki Visit Points+2) {/size} {/color}":
            $ Nikki_Visit_Points += 2
            # Nikki_Visit (16)
            scene 09_958 with Dissolve(1)
            ""
            to "College guys must be so lame that all those old women come here..."
        "Hug":
            scene 09_959 with Dissolve(1)
            mc "Thanks for picking me up. How are you?"
            ni "I'm good. Missed you!"
            to "Ooh, I missed you, ugh..."
    scene 09_960 with Dissolve(1)
    mc "Don't listen to her. She's lonely."
    ni "And last time you were in Riverside, you said girls in Madison Springs were nicer..."
    mc "Haha. I might have been wrong."
    to "..."
    mc "Let's go. Beach time!"
    scene 09_961 with Dissolve(1)
    mc "If I'd known you'd be picking me up, I'd have hurried a little bit more."
    ni "It's fine. I haven't been here long."
    mc "What were you daydreaming about earlier? I think I could've passed you without you even noticing."
    scene 09_962 with Dissolve(1)
    ni "Oh, I was thinking about my time in high school."
    mc "The good old times!"
    ni "Hey! I'm not old. We're only two years apart, not even! More like one and a half, if that!"
    scene 09_963 with Dissolve(1)
    mc "Would you have dated me if you were still in school?"
    ni "You mean together in the same school as you?"
    mc "Yeah. You a senior and me a sophomore or something like that."
    ni "Hmm... Probably not."
    mc "Haha. Then I'm happy we weren't."
    scene 09_964 with Dissolve(1)
    mc "Do you regret not going to college?"
    ni "No. And if I did, I could still go."
    mc "True. What made you decide not to go?"
    ni "After high school, I worked at the gym during summer break."
    ni "They offered me a full-time job as a receptionist but with the possibility of doing a personal trainer course."
    if Layla_End == True:
        pass
    else:
        scene 09_965 with Dissolve(1)
        am "What's the hold up? Can you get in the car?"
        la "One second."
    scene 09_966 with Dissolve(1)
    ni "So, the first six months I..."
    tm "[mc]!"
    scene 09_967 with Dissolve(1)
    if Mike_Name == True:
        mc "Hey, Mike."
    else:
        mc "Hey, Coach."
    tm "You forgot your..."
    scene 09_968 with Dissolve(1)
    ni "Dad!"
    tm "Nikki!"
    mc "{i}(Dad? Coach Morgan is Nikki's dad? Morgan... Of course. I knew it sounded familiar the first time I heard it. What are the odds?){/i}"
    scene 09_969 with Dissolve(1)
    tm "I'm so happy to see you!"
    ni "How... What are..."
    if Layla_End == True:
        pass
    else:
        scene 09_970 with Dissolve(1)
        am "What are you actually looking at?"
        am "Oh..."
        la "Do you know who that is?"
        am "That's probably Coach's daughter."
        la "Coach has a daughter?"
        am "Two!"
        scene 09_971 with Dissolve(1)
        la "{i}(How does [mc] know Coach's daughter? And why haven't I ever seen her?){/i}"
        am "Come on, get in now. I have stuff to do."
        la "{i}(She's very pretty! How old is she?){/i}"
        if MC_Girlfriend_Riverside == False:
            pass
        else:
            la "{i}(Could she be [mc]'s girlfriend?){/i}"
    scene 09_972 with Dissolve(1)
    tm "Why are you here? How do you know [mc]?"
    ni "That's a long story!"
    mc "I'll give you guys some time. I'll..."
    ni "No."
    scene 09_973 with Dissolve(1)
    ni "Dad, we already have plans today. Can we maybe meet up tomorrow?"
    tm "Of course."
    ni "I'll come pick you up after school, then?"
    tm "I'm done at noon. If you come then we can go eat together."
    ni "Sounds good."
    scene black with Dissolve(1)
    pause 2
    scene 09_974 with Dissolve(1)
    mc "Uhm... Yeah, that happened. You didn't know he teaches here? Well, you would've told me if you knew, so..."
    ni "Yeah, I didn't. He was an athletics trainer for a team with whom he travelled."
    ni "I'll ask him tomorrow what made him change to become a school coach and why he didn't tell us."
    ni "I'm a little shaken, to be honest. That took me completely by surprise."
    mc "Same."
    scene 09_975 with Dissolve(1)
    mc "Coach Mike is your dad... Wow."
    mc "{i}(Let's hope he doesn't find out all the stuff I did with his daughter.){/i}"
    ni "It's funny you call him Mike."
    mc "The first time I met him, he said to call him Mike or Coach. You want me to call him Dad now?"
    ni "Haha."
    if Nikki_Visit_Points >= 10:
        scene 09_976 with Dissolve(1)
        mc "By the way. You look freaking sexy in hot pants, Nikki!"
        ni "Thanks."
        mc "I guess I'll have to fight off lots of guys trying to steal you away."
        ni "I'll help you!"
        scene 09_977 with vpunch
        n "*slap*"
        ni "Ah..."
        mc "Yes, ah exactly. I think my hand hurts more than your butt. Been doing squats?"
        ni "A few."
    else:
        pass
    scene black with Dissolve(2)
    pause 2
    stop music fadeout 1.0
    play music ("Music/LoFi Indie 2.mp3", "Music/LoFi Indie 3.mp3", "Music/LoFi Indie 1.mp3") volume 0.2
    scene 09_996 with Dissolve(1)
    ni "Alright, you need to help me."
    mc "Okay?"
    ni "I've brought a one-piece and a bikini. You tell me which one you like best."
    scene 09_997 with Dissolve(1)
    mc "You're modelling them for me?"
    ni "Uh-huh, that's the best way to show them."
    mc "You're assolu... absolutely right!"
    ni "I know you're staring!"
    mc "I know you're bending over on purpose!"
    scene 09_998 with Dissolve(1)
    ni "Stop flirting or we won't make it to the beach!"
    mc "That's fine with me."
    ni "I want to go, though!"
    scene 09_999 with Dissolve(1)
    mc "Now you're just doing this on purpose."
    ni "Haha."
    mc "If you really want to go, you'd better change in the bathroom. This is not helping your case!"
    scene 09_1000 with Dissolve(1)
    ni "Fine! I'll be right back with option one."
    mc "I can't wait."
    scene black with Dissolve(1)
    pause 2
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 09_1001 at moveup
    pause 3
    ni "Alright, I started with the one-piece. What do you think?"
    menu:
        "Like[KoGa3AutoWTChange1]{size=-4}(Nikki Week4 Thursday Swimsuit Option1 Like) {/size} {/color}":
            $ Nikki_Week4_Thursday_Swimsuit_Option1_Like = True
            mc "I like it. It shows less skin, but I think that's somehow sexy."
            ni "Yeah? I think so too. Adds a little mystery, right?"
            mc "Exactly."
            mc "But you do know there's a hole it in?"
        "Don't like":
            mc "I'm not the biggest fan of one-pieces."
            ni "They cover too much?"
            mc "Heh, yes..."
            mc "Besides, you do know there's a hole in it?"
    scene 09_1002 with Dissolve(1)
    ni "What? Where?"
    mc "Right there. You can't miss it."
    ni "..."
    ni "It's the design! For a moment I thought you were serious, idiot!"
    mc "Haha."
    scene 09_1003 with Dissolve(1)
    ni "That is option one. Let me change into option two."
    mc "{i}(Her butt looks amazing in this one though.){/i}"
    scene black with Dissolve(1)
    pause 2
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 09_1004 at moveup
    pause 3
    ni "Based on your expression, I can see you've made a decision already."
    mc "Hehe, you look really good."
    ni "Thanks."
    scene 09_1005 with Dissolve(1)
    ni "So, it's this one?"
    mc "Definitely!"
    if Nikki_Week4_Thursday_Swimsuit_Option1_Like == True:
        mc "It's not that I didn't like option one. As I said, I think it's really sexy."
        mc "But you have that incredible body and... You know..."
        mc "Also, you'll get some weird tan lines in that one-piece, especially with that hole."
        ni "Haha. You're right, I hadn't even thought about that."
    else:
        mc "Also, you'll get some weird tan lines in that one-piece, especially with that hole."
        ni "Haha. You're right, I hadn't even thought about that."
    scene 09_1006 with Dissolve(1)
    ni "Alright, thanks. I guess I don't have to change again."
    mc "I'll change real quick, though."
    ni "..."
    ni "You could've changed when I did."
    mc "I had other stuff on my mind."
    scene black with Dissolve(1)
    pause 2
    scene 09_1007 with Dissolve(1)
    ni "You're wearing that?"
    mc "Uh yeah? Something wrong?"
    ni "I hate that t-shirt!"
    mc "It's just a t-shirt."
    scene 09_1008 with Dissolve(1)
    ni "Aiden has the same one."
    mc "Aiden? Oh... Man bun?"
    ni "Yeah."
    mc "... I'll change."
    scene 09_1009 with Dissolve(1)
    ni "Give me that."
    mc "..."
    scene 09_1010 with Dissolve(1)
    mc "What are you doing?"
    ni "Ripping it."
    mc "That was a present, Nikki..."
    ni "Well now it's a dusting cloth."
    scene 09_1011 with Dissolve(1)
    mc "Can I have my other shirt back, then?"
    ni "What? No! That's mine now!"
    mc "..."
    ni "But I'll let you borrow it for today."
    scene black with Dissolve(2)
    pause 2
    stop music fadeout 1.0
    play music "Sounds/Ocean.mp3" volume 0.5
    scene 09_1012 with Dissolve(1)
    ni "This is so beautiful. I can't believe you live just twenty-five minutes from the beach!"
    ni "No wonder you left Riverside that quickly."
    mc "..."
    scene 09_1013 with Dissolve(1)
    ni "Thank you for bringing me here."
    mc "You're welcome."
    scene 09_1014 with Dissolve(1)
    mc "Want to set up here, or...?"
    ni "Here's good!"
    scene 09_1015 with Dissolve(1)
    ni "It's been four years since last I was at a beach."
    mc "Four Years? That's a long time."
    mc "Actually... It was five for me before I moved back here..."
    scene 09_1016 with Dissolve(1)
    ni "Now you can come here every day."
    mc "And I probably will, during spring break."
    ni "I'm so jealous. Why are we living in Riverside when we can have all this..."
    mc "Hehe. You can always move."
    ni "Hmm..."
    scene 09_1017 with Dissolve(1)
    ni "No bathroom here!"
    mc "Haha, I didn't say anything."
    scene 09_1018 with Dissolve(1)
    ""
    scene 09_1019 with Dissolve(1)
    ni "..."
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 09_1020 at moveup
    pause 3
    ni "This is so beautiful! The warmth, the smell, the ocean view."
    mc "Yeah, absolutely gorgeous!"
    scene 09_1021 with Dissolve(1)
    ni "You were right about it not being so crowded today."
    mc "If we'd waited for tomorrow or the weekend, we'd have to fight for a spot."
    ni "What if I want to come here again on Saturday?"
    mc "Well, we'd either have to come very early, or take a wrestling starter course."
    ni "Haha. Good thing we wake up early."
    scene 09_1022 with Dissolve(1)
    mc "We? It's the weekend. You'd better not wake me at six again."
    ni "Then wrestling it is."
    ni "Are you prepared to also fight girls?"
    mc "Girls? Easy. I'll just pick them up and throw them in the water."
    ni "Really..."
    scene 09_1023 with Dissolve(1)
    ni "Okay, let's see how strong you are!"
    mc "Haha, arm wrestling?"
    ni "Come on, show me!"
    mc "Nikki..."
    ni "Come on!"
    scene 09_1024 with Dissolve(1)
    ni "Ready?"
    mc "You look cute when you're being serious!"
    ni "Distraction tactics already?"
    mc "No distraction, just the truth."
    ni "..."
    ni "Three... two... one..."
    scene 09_1025 with Dissolve(1)
    ni "Go!"
    mc "{i}(Oh shit... I know she's strong, but I actually have to put in more than I thought.){/i}"
    menu:
        "Let Nikki win":
            scene 09_1027 with vpunch
            ni "I did it!"
            scene 09_1028 with Dissolve(1)
            ni "Haha, that was fun. I've always wanted to arm wrestle you."
            mc "Congrats!"
            scene 09_1029 with Dissolve(1)
            ni "I know you let me win!"
            mc "Did I now?"
            ni "Uh-huh."
        "Win[KoGa3AutoWTChange1]{size=-4}(Nikki Week4 Thursday ArmwrestlingWin) {/size} {/color}":
            $ Nikki_Week4_Thursday_ArmwrestlingWin = True
            scene 09_1026 with vpunch
            ni "Aaah..."
            scene 09_1028 with Dissolve(1)
            ni "Haha, that was fun. I've always wanted to arm wrestle you."
            ni "I can't believe I thought I might have a chance."
            mc "You did well, though."
            scene 09_1029 with Dissolve(1)
            ni "Thanks."
    scene 09_1030 with Dissolve(1)
    ni "I'd better finish lotioning up. I can feel my skin burning already."
    mc "The sun hits different here, huh?"
    ni "It does, but I enjoy it. As long as I don't look like a lobster tomorrow."
    mc "Haha."
    menu:
        "Watch":
            scene 09_1031 with Dissolve(1)
            ni "Need some too?"
            mc "I'm good. I don't get burned that quickly."
            jump Week4_Thursday_Nikki_Beach
        "Offer to help[KoGa3AutoWTChange1]{size=-4}(Nikki Week4 Thursday Lotion, Nikki Visit Points+2) {/size} {/color}":
            $ Nikki_Week4_Thursday_Lotion = True
            $ Nikki_Visit_Points += 2
            # Nikki_Visit (18)
            jump Week4_Thursday_Nikki_Beach_Lotion

label Week4_Thursday_Nikki_Beach_Lotion:
    if _in_replay:
        $ Nikki_Visit_Points = 18
    scene 09_1032 with Dissolve(1)
    mc "Do you want me to do your back?"
    ni "Yes, please."
    scene 09_1033 with Dissolve(1)
    mc "{i}(Haven't even started yet and I'm so hard.){/i}"
    mc "{i}(Nikki's body is just insane!){/i}"
    ni "..."
    ni "I don't mind you staring at my ass..."
    scene 09_1034 with Dissolve(1)
    ni "But how about after you put the lotion on it?"
    mc "Your butt too?"
    ni "Since you're doing my back, you can do the rest, too."
    mc "Sure!"
    scene 09_1035 with Dissolve(1)
    ""
    scene 09_1036 with Dissolve(1)
    ""
    scene 09_1037 with Dissolve(0.5)
    ""
    scene 09_1038 with Dissolve(1)
    mc "{i}(Her butt is so firm.){/i}"
    mc "{i}(I could do this all day.){/i}"
    scene 09_1039 with Dissolve(1)
    ni "You've definitely done this before."
    mc "My friends always ask me to put lotion on their backs."
    ni "Your friends?"
    scene 09_1040 with Dissolve(1)
    mc "Only guys, obviously."
    ni "Obviously..."
    menu:
        "Kiss her shoulder":
            scene 09_1041 with Dissolve(1)
            ""
        "Kiss her cheek":
            scene 09_1042 with Dissolve(1)
            ""
    scene 09_1043 with Dissolve(1)
    mc "*Whisper* You turn me on so much, Nikki."
    mc "*Whisper* If we were alone, I'd take you right here like this."
    ni "*Whisper* You know I love this position. Why don't you ask the others to leave?"
    mc "*Whisper* You think they will if I ask them politely? What if they wanna watch?"
    ni "..."
    scene black with Dissolve(1)
    pause 2
    scene 09_1044 with Dissolve(1)
    n "*Slap*"
    mc "Anyway. We're finished. All lotioned up."
    ni "What do you mean finished? There's this whole other side to me."
    mc "Haha."
    scene 09_1045 with Dissolve(1)
    ni "Here you go!"
    menu:
        "Take lotion":
            scene 09_1046 with Dissolve(1)
            mc "Everything?"
            ni "Everything!"
        "Joke":
            mc "Everything?"
            ni "Everything!"
            scene 09_1047 with Dissolve(1)
            ni "Aaah... [mc]!"
            mc "Haha, sorry."
            scene 09_1048 with Dissolve(1)
            mc "You said everything."
            ni "..."
            mc "See it as a happy little accident."
            ni "You're not funny!"
    scene 09_1049 with Dissolve(1)
    ni "Here, you can start with my leg."
    mc "Yes, ma'am."
    scene 09_1050 with Dissolve(1)
    mc "{i}(I'll have to go in the water soon, or...){/i}"
    scene 09_1051 with Dissolve(1)
    mc "You're enjoying this, huh?"
    ni "I am. It's not every day I have a cute boy putting lotion all over me."
    ni "You seem to be enjoying it, too."
    mc "Totally. It's not every day I... No, that's not true..."
    scene 09_1052 with Dissolve(1)
    ni "Hey!"
    mc "Haha. I'm kidding."
    ni "Uh-huh. I saw the girls who attend your school when I was waiting for you."
    scene 09_1053 with Dissolve(1)
    mc "You of all people shouldn't be jealous. Look at you. You're a freakin' goddess!"
    ni "..."
    ni "You forgot a part!"
    mc "Hmm?"
    ni "I said everything!"
    mc "{i}(Her boobs?){/i}"
    scene 09_1054 with Dissolve(1)
    ni "Uhm, what are you doing?"
    mc "Taking your top off so I..."
    ni "No-no-no, I'm not taking my top off in public."
    mc "Then..."
    ni "Figure it out."
    scene 09_1055 with Dissolve(1)
    mc "{i}(I don't know what I enjoy more. Lotioning her butt or her massive boobs.){/i}"
    show 09_1056
    ""
    scene black with Dissolve(1)
    pause 2
    scene 09_1057 with Dissolve(1)
    mc "There you go."
    ni "Thank you very much, [mc]."
    scene 09_1058 with Dissolve(1)
    ""
    scene 09_1059 with Dissolve(1)
    ni "Do you want me to put some sunscreen on you?"
    menu:
        "No":
            mc "Thanks, but I'm good. I usually don't get sunburn."
            $ renpy.end_replay()
        "Yes[KoGa3AutoWTChange1]{size=-4}(Nikki Week4 Thursday LotionMC, Nikki Visit Points+2) {/size} {/color}":
            $ Nikki_Week4_Thursday_LotionMC = True
            $ Nikki_Visit_Points += 2
            # Nikki_Visit (20)
            mc "Yes, please."
            ni "Hehe, alright."
            scene 09_1060 with Dissolve(1)
            mc "Normally I don't use sunscreen, but..."
            ni "But you just want my hands all over you!"
            mc "Exactly!"
            ni "Haha."
            scene 09_1061 with Dissolve(1)
            ni "I can feel that your back muscles have become stronger. Are you still going to the gym?"
            mc "Besides the school gym, no. Mike... Well, your dad..."
            ni "Haha, that's something we have to get used to."
            mc "Indeed. He makes us do lots of back exercises."
            scene 09_1062 with Dissolve(1)
            ni "Do you like him?"
            mc "As a trainer?"
            ni "Mmm-hmm."
            mc "He's a good coach. You can see he cares about his students. He even made us individual training schedules for the break."
            mc "But maybe that will change now he knows that we..."
            ni "No, he's professional in that regard. But outside of training, maybe... I don't know."
            scene 09_1063 with Dissolve(1)
            ni "It's a good thing you like him though."
            mc "Not as much as my former personal trainer!"
            ni "Oh... You had a personal trainer?"
            mc "I did."
            ni "Tell me about him!"
            scene 09_1064 with Dissolve(1)
            mc "Her!"
            ni "A girl? Obviously..."
            mc "Well, I didn't have a choice. The gym appointed her to be my trainer."
            ni "Really? As far as I remember, you specifically asked for her, Roberto!"
            scene 09_1065 with Dissolve(1)
            mc "The name is [mc]!"
            ni "Sorry, I had you confused with someone else."
            ni "Please continue. So, a female personal trainer."
            mc "Yes. She was amazing!"
            ni "What was so amazing about her?"
            scene 09_1066 with Dissolve(1)
            mc "Her body for starters. Just... Wow! You had to see it to believe it."
            mc "I'll tell you a secret. I didn't go to the gym to train. I only went there to look at her."
            mc "Even though I knew how to do the exercises, I purposefully messed up so she would touch me to correct me or show me again."
            mc "I can't remember how many times I messed up squats."
            scene 09_1067 with Dissolve(1)
            ni "..."
            mc "Hey!"
            scene 09_1068 with vpunch
            n "*Slap*"
            mc "Aaah..."
            ni "I really thought you didn't know how to do them properly! And now you tell me this..."
            mc "Haha. Sorry, not sorry!"
            scene 09_1068 with vpunch
            n "*Slap*"
            mc "Aah-haha..."
            scene black with Dissolve(1)
            pause 2
            scene 09_1069 with Dissolve(1)
            mc "Oh, doing the front, too?"
            ni "Everything!"
            mc "Hehe."
            scene black with Dissolve(1)
            transform moveup:
                xalign 0.5 yalign 1.0
                linear 5.0 yalign 0.0
            show 09_1070 at moveup
            pause 3
            mc "{i}(Note to self. If you go to the beach with Nikki, bring multiple pairs of shorts...){/i}"
            mc "{i}(Damn, she's so hot!){/i}"
            ni "Tell me more about that female personal trainer."
            ni "You only talked about her body. What about her personality?"
            scene 09_1071 with Dissolve(1)
            mc "Oh yeah, her personality. She has these two big..."
            ni "Turn around, so I can slap your ass again!"
            mc "Haha, I'm kidding! Not really though."
            ni "..."
            scene 09_1072 with Dissolve(1)
            ni "How is this for personality!"
            mc "Mmmh..."
            scene 09_1073 with Dissolve(1)
            mc "Hey! No water sports on the beach! Keep them in the water!"
            ni "What?"
            mc "Motorboating..."
            ni "You are such an idiot."
            mc "Haha, it thought it was clever."
            scene 09_1074 with Dissolve(1)
            mc "But seriously, she has an incredible personality!"
            mc "She's fun and playful with a good sense of humour. She's passionate, also very loving and caring."
            mc "She's confident, but keeps it down to earth. And maybe the most important bit, she accepts my flaws."
            scene 09_1075 with Dissolve(1)
            ni "That's very sweet, thank you!"
            $ renpy.end_replay()
    jump Week4_Thursday_Nikki_Beach

label Week4_Thursday_Nikki_Beach:
    scene black with Dissolve(1)
    pause 2
    scene 09_1076 with Dissolve(1)
    ""
    scene 09_1077 with Dissolve(1)
    mc "I'm gonna get me something to drink. Do you want anything?"
    ni "Oh... Yes, please. A bottle of water."
    mc "Water? Okay. Be right back."
    ni "Thank you!"
    scene black with Dissolve(1)
    pause 2
    scene 09_1078 with Dissolve(1)
    mc "{i}(Oh... I almost missed this.){/i}"
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 09_1079 at moveup
    pause 3
    mc "{i}(Good form.){/i}"
    scene 09_1080 with Dissolve(1)
    mc "{i}(How long can she do this for?){/i}"
    mc "..."
    mc "{i}(She's actually trying to walk.){/i}"
    scene 09_1081 with vpunch
    mc "Ouch... Are you okay?"
    ni "Haha, yeah."
    mc "It looked good for a moment."
    ni "Until I tried to walk."
    scene 09_1082 with Dissolve(1)
    mc "Here's your water."
    ni "Thanks. What did you get?"
    mc "Caramel frappé."
    ni "Oh..."
    menu:
        "Give Nikki water":
            pass
        "Give Nikki frappé[KoGa3AutoWTChange1]{size=-4}(Nikki Visit Points+2) {/size} {/color}":
            $ Nikki_Visit_Points += 2
            # Nikki_Visit (22)
            scene 09_1083 with Dissolve(1)
            mc "Here!"
            ni "Really?"
            scene 09_1084 with Dissolve(1)
            ni "*Humming*"
            mc "Tasty?"
            ni "Mmm-hmm."
    scene 09_1085 with Dissolve(1)
    ni "Let's try this again."
    menu:
        "Just watch":
            mc "Good luck!"
            scene 09_1086 with vpunch
            ni "Aaah..."
            scene 09_1087 with Dissolve(1)
            mc "I see you were hungry, too. Why didn't you say so? I could've gotten you something better than sand."
            ni "..."
            mc "Haha."
            scene 09_1088 with Dissolve(1)
            mc "Instead of trying to break your neck, you want to go in the water?"
            ni "Sure..."
            scene black with Dissolve(1)
            pause 2
            scene 09_1101 with Dissolve(1)
            ni "This is so nice. Good call coming here today!"
            mc "So, you're enjoying yourself here?"
        "Offer help[KoGa3AutoWTChange1]{size=-4}(Nikki Week4 Thursday Handstand Help, Nikki Visit Points+2) {/size} {/color}":
            $ Nikki_Week4_Thursday_Handstand_Help = True
            $ Nikki_Visit_Points += 2
            # Nikki_Visit (24)
            mc "Need some help?"
            ni "Oh, if you don't mind."
            scene 09_1089 with Dissolve(1)
            mc "What I should I do?"
            ni "Stand in front of me and when you see me lose my balance and tilt towards you, support me."
            mc "Sure."
            scene 09_1090 with Dissolve(1)
            ni "Ooh..."
            mc "Don't worry, I gotcha. Keep on going."
            scene 09_1091 with Dissolve(1)
            mc "You're doing great! You look good doing it, too!"
            ni "Thanks. It's not that difficult if you're holding me."
            mc "I'm not. I'm just trying to keep you balanced."
            scene 09_1092 with vpunch
            ni "Aaah..."
            mc "Now I'm holding you up!"
            ni "[mc]!"
            scene 09_1093 with Dissolve(1)
            ni "What are you doing?"
            mc "Going for a walk."
            scene 09_1094 with Dissolve(1)
            ni "Where are... No! No-no-no... [mc]!"
            ni "Don't you dare do what I think you're about to do!"
            ni "I..."
            scene 09_1095 with Dissolve(1)
            mc "Haha."
            mc "{i}(She's gonna be so mad.){/i}"
            scene 09_1096 with Dissolve(1)
            ni "[mc]!"
            mc "Sorry, what were you saying? I couldn't understand because..."
            ni "You are so..."
            mc "Watch out! Another wave!"
            scene 09_1097 with Dissolve(1)
            ni "..."
            scene 09_1098 with Dissolve(1)
            ni "You are so dead!"
            mc "Haha, I'm sorry... The first wave was an accident."
            scene 09_1099 with vpunch
            ni "What about the second?"
            mc "I have no excuse for that one."
            scene black with Dissolve(1)
            pause 2
            scene 09_1100 with Dissolve(1)
            mc "Sorry again. I didn't mean to..."
            ni "No, don't be. I like it when you play with me."
            mc "So, you're enjoying yourself here?"
    scene 09_1102 with Dissolve(1)
    ni "It's only been two days, but I love this place already."
    mc "It's the beach, right?"
    ni "You might have a little something to do about it, too. No... You're right. It's the beach!"
    mc "Haha."
    menu:
        "Kiss[KoGa3AutoWTChange1]{size=-4}(Nikki Visit Points+2) {/size} {/color}":
            $ Nikki_Visit_Points += 2
            # Nikki_Visit (26)
            jump Week4_Thursday_Nikki_Beach_Kiss
        "Don't kiss":
            scene black with Dissolve(1)
            pause 2
            scene 09_1113 with Dissolve(1)
            ni "Let's get out of the water, dry up and go home?"
            mc "There's still plenty of sunlight. We can stay longer if you like."
            ni "I don't want to keep you here all evening on a school day!"
            mc "Haha, I don't mind."
            ni "A little longer then."
            jump Week4_Thursday_Nikki_Beach_End

label Week4_Thursday_Nikki_Beach_Kiss:
    if _in_replay:
        $ Nikki_Week4_Thursday_Handstand_Help = True
    scene 09_1103 with Dissolve(1)
    ""
    scene 09_1104 with Dissolve(1)
    mc "Hey, Nikki?"
    ni "Hmm?"
    mc "Does this still count as being in public?"
    ni "No..."
    scene 09_1105 with Dissolve(1)
    ""
    scene 09_1106 with Dissolve(1)
    ""
    scene 09_1107 with Dissolve(1)
    ""
    scene 09_1108 with Dissolve(1)
    ni "*Heavy breathing*"
    scene 09_1109 with Dissolve(1)
    ""
    scene 09_1110 with Dissolve(1)
    ni "Ah... [mc]! Keep going. I'm..."
    scene 09_1111 with Dissolve(1)
    ni "Mmm... Cumming."
    scene black with Dissolve(1)
    pause 2
    scene 09_1112 with Dissolve(1)
    ni "That was amazing!"
    mc "Yeah, did you enjoy it?"
    ni "Mmm-hmm!"
    if Nikki_Week4_Thursday_Handstand_Help == True:
        scene 09_1114 with Dissolve(1)
        mc "What?"
        ni "..."
        scene 09_1115 with Dissolve(1)
        mc "{i}(Is she going to give me a blowjob underwater?){/i}"
        mc "{i}(Let's see how long she can hold her breath for.){/i}"
        mc "{i}(This is going to be so good!){/i}"
        scene 09_1116 with Dissolve(1)
        mc "Nikki!"
        ni "Good luck out there!"
        mc "What are you doing? Give me my shorts! Please!"
        ni "This is what you get for holding me underwater."
        ni "If you want them, come and get them!"
        mc "..."
        scene 09_1117 with Dissolve(1)
        ni "What are you still doing there? Don't you want to come out?"
        mc "Ha-ha-ha, you're so funny!"
        ni "Haha."
        mc "Can I please have them back, Nikki?"
        scene black with Dissolve(1)
        pause 2
        scene 09_1118 with Dissolve(1)
        ni "Why do you look so annoyed now? It was only five minutes..."
        mc "..."
        scene 09_1119 with vpunch
        ni "Aaah..."
        mc "I'm not annoyed at you. I'm annoyed I was fooled so easily."
        ni "Haha, sorry?"
        scene 09_1120 with Dissolve(1)
        ni "Are we even, now?"
        mc "Far from it!"
        ni "Mmm..."
        scene 09_1121 with Dissolve(1)
        ""
        scene black with Dissolve(1)
        pause 2
        scene 09_1122 with Dissolve(1)
        ni "*Whispers* [mc], are you asleep?"
        mc "No, just a bit tired."
        ni "Let's go home then."
        scene 09_1123 with Dissolve(1)
        ni "*Stomach rumbling*"
        mc "Haha. Why didn't you say you were hungry?"
        ni "You were lying there so peacefully."
        mc "Let's leave."
    else:
        scene 09_1113 with Dissolve(1)
        ni "Let's get out of the water, dry up and go home?"
        mc "There's still plenty of sunlight. We can stay longer if you like."
        ni "I don't want to keep you here all evening on a school day!"
        mc "Haha, I don't mind."
        ni "A little longer then."
    $ renpy.end_replay()
    jump Week4_Thursday_Nikki_Beach_End

label Week4_Thursday_Nikki_Beach_End:
    scene black with Dissolve(2)
    pause 2
    scene 09_1124 with Dissolve(1)
    ni "Should we get some food along the way?"
    mc "I think Mom will be cooking. She said she was grocery shopping after work."
    mc "And if not, we can still order in. But since you're here, I'm pretty sure she'll make something."
    scene 09_1125 with Dissolve(1)
    ni "Hmm..."
    mc "What?"
    ni "The hat looks better on me."
    mc "Obviously! Everything looks better on you."
    scene 09_1126 with Dissolve(1)
    mc "Even if you aren't wearing anything, you look better than me!"
    ni "That's not true!"
    mc "Of course it's true. But if you want proof. Once we're home, we'll get naked and compare."
    ni "Haha."
    if Nikki_Visit_Points >= 18:
        scene 09_1127 with Dissolve(1)
        ni "Maybe..."
        mc "Maybe?"
        ni "Maybe!"
        ni "I still don't believe that I look better in everything!"
        scene 09_1128 with Dissolve(1)
        mc "Imagine me wearing your hotpants. I'd look ridiculous."
        ni "Now I really want to see that."
        mc "Not gonna happen!"
        ni "I'll give you your shirt back."
        mc "I guess you can keep it forever!"
        ni "Haha."
    else:
        ni "I still don't believe that I look better in everything!"
        scene 09_1129 with Dissolve(1)
        mc "Imagine me wearing your hotpants. I'd look ridiculous."
        ni "Now I really want to see that."
        mc "Not gonna happen!"
        ni "I'll give you your shirt back."
        mc "I guess you can keep it forever!"
        ni "Haha."
    scene black with Dissolve(2)
    pause 2
    stop music fadeout 1.0
    play music ("Music/LoFi Indie 3.mp3", "Music/LoFi Indie 1.mp3", "Music/LoFi Indie 2.mp3") volume 0.2
    scene 09_1130 with Dissolve(1)
    mc "Hey, Mom."
    m "Ah, you're back."
    ni "Smells amazing, Emily!"
    m "Thank you."
    scene 09_1131 with Dissolve(1)
    m "Where did you go?"
    mc "I showed Nikki the beach."
    m "Oh, nice. Good thing you went today. You'd be fighting for a spot at the weekend."
    mc "Haha, that's what I said."
    m "Did you have fun?"
    ni "Yeah, it's so beautiful here."
    scene 09_1132 with Dissolve(1)
    mc "I'm gonna shower and change real quick."
    m "Food will be ready in forty-five minutes."
    mc "Okay."
    ni "Do you need some help, Emily?"
    m "Sure, thank you."
    scene 09_1133 with Dissolve(1)
    ni "Do I cut them like this, or...?"
    m "Yes, that looks good."
    scene black with Dissolve(1)
    pause 2
    scene 09_1134 with Dissolve(1)
    ni "Weren't you going to shower and change?"
    mc "I'm about to. Was just reading some mail."
    mc "Weren't you going to help cooking?"
    ni "It's in the oven now."
    scene 09_1135 with Dissolve(1)
    mc "What?"
    ni "My shirt, please!"
    mc "..."
    mc "Can't I keep it? I don't have that many."
    scene 09_1136 with Dissolve(1)
    ni "If you want it, you know what to do..."
    mc "..."
    ni "What's it gonna be?"
    scene 09_1137 with Dissolve(1)
    mc "Keep it!"
    ni "Haha, thank you. You can borrow it again though, if you want."
    scene black with Dissolve(2)
    pause 2
    scene 09_1138 with Dissolve(1)
    ni "[mc]."
    mc "Nggh..."
    ni "[mc]?"
    scene 09_1139 with Dissolve(1)
    mc "Nikki... Don't tell me it's six already... I'm way too tired to go running."
    mc "Feels like I've only been sleeping thirty minutes."
    ni "It's half past twelve."
    mc "Then..."
    ni "I don't want to sleep alone."
    menu:
        "Stay here[KoGa3AutoWTChange1]{size=-4}(Nikki Visit Points-6) {/size} {/color}":
            $ Nikki_Visit_Points -= 6
            scene 09_1140 with Dissolve(1)
            mc "I don't think it's a good idea, Nikki."
            mc "Let's talk tomorrow, okay?"
            ni "..."
            ni "Okay. Good night, [mc]."
            mc "Good night!"
            scene black with Dissolve(2)
            pause 2
            scene 09_1160 with Dissolve(1)
            mc "Hey, here you are..."
            ni "Morning, [mc]."
            mc "Did you go for a run already?"
            ni "I did. I've let you off the hook for today."
            scene 09_1161 with Dissolve(1)
            ni "Well not really, I tried to wake you, but you didn't budge."
            mc "Hehe. Thanks, I guess..."
            mc "Mom not here?"
            ni "She left already. Had to be early at the café? I think she meant restaurant but..."
            scene 09_1163 with Dissolve(1)
            mc "No, no. She's actually opening up a café."
            ni "Oh?"
            mc "Yeah. It should've been open before spring break, but there were some setbacks."
            mc "{i}(Rachel...){/i}"
            scene 09_1164 with Dissolve(1)
            mc "Is that coffee?"
            ni "Mmm-hmm."
            mc "Can I have a sip?"
            ni "Sure."
            scene 09_1165 with Dissolve(1)
            mc "..."
            mc "I always forget you put milk in your coffee."
            scene 09_1166 with Dissolve(1)
            mc "So, you're gonna spend some time with your dad today, right?"
            ni "That's the plan. I probably won't be able to pick you up."
            mc "Don't worry. A friend asked me to hang out after school."
            scene 09_1168 with Dissolve(1)
            ni "Are you done in the bathroom, can I go shower?"
            mc "Go ahead. I need to leave now anyway, or I'll be late again."
            ni "See you tonight, then."
            mc "Yes. Have fun with your dad."
            ni "Thanks, you too."
            jump Week4_Friday_Afternoon
        "Go with Nikki[KoGa3AutoWTChange1]{size=-4}(Nikki Visit Points+2) {/size} {/color}":
            $ Nikki_Visit_Points += 2
            # Nikki_Visit (28)
            jump Week4_Thursday_Nikki_Night

label Week4_Thursday_Nikki_Night:
    if _in_replay:
        $ Nikki_Visit_Points = 28
        $ SexCounter_Nikki = 4
        $ MC_SexCounter = 4
    $ SexCounter_Nikki += 1
    $ MC_SexCounter += 1
    scene 09_1141 with Dissolve(1)
    mc "I can scoot over a bit."
    mc "But there's not much space here..."
    scene 09_1142 with Dissolve(1)
    ni "Hmm..."
    mc "Like I said, not much space. Maybe we can try this?"
    scene 09_1143 with Dissolve(1)
    mc "This works. And now the chances of you falling off are slim to none."
    ni "Haha. As much as I'm enjoying this, maybe we should go upstairs?"
    mc "If we go upstairs, we won't be doing much sleeping."
    ni "And you think it will be different here?"
    scene black with Dissolve(1)
    pause 2
    scene 09_1144 with Dissolve(1)
    ni "Good night!"
    mc "Uh... Good night..."
    mc "{i}(Is she really gonna sleep now?){/i}"
    scene 09_1145 with Dissolve(1)
    ni "Heh... We have all this space and you're still clinging on to me?"
    mc "First you lure me here and now you..."
    ni "Lure? I only said I don't want to sleep alone. Emphasis on sleep!"
    scene 09_1146 with Dissolve(1)
    ni "Didn't you say you were tired?"
    mc "Earlier, yes. I'm wide awake now!"
    ni "I see."
    mc "Can I take them off?"
    scene 09_1147 with Dissolve(1)
    mc "You're so beautiful, Nikki."
    mc "I'm happy you came."
    scene 09_1148 with Dissolve(1)
    ni "Me too!"
    scene 09_1149 with Dissolve(1)
    ""
    scene 09_1150 with Dissolve(1)
    mc "Yeah, right, you wanted to sleep. Your panties are dripping wet!"
    mc "Let's take them off. Don't want you to get sick."
    ni "*Giggles*"
    scene 09_1151 with Dissolve(1)
    mc "I've wanted to fuck you all day!"
    scene 09_1152 with Dissolve(1)
    ni "Ah..."
    scene 09_1153 with Dissolve(1)
    mc "You okay?"
    ni "Don't stop!"
    scene 09_1154 with Dissolve(1)
    ni "*Moaning*"
    scene 09_1155 with Dissolve(1)
    mc "{i}(Fuck... I'm cumming already. Has it even been a minute?){/i}"
    mc "Nikki... I can't..."
    scene 09_1156 with vpunch
    pause 2
    scene 09_1156 with vpunch
    mc "Aaah..."
    scene black with Dissolve(1)
    pause 2
    scene 09_1157 with Dissolve(1)
    mc "Look who's clinging to who now!"
    ni "I'm allowed after I let you fuck me!"
    mc "Is that how it works?"
    ni "Uh-huh..."
    if Nikki_Visit_Points >= 25:
        scene 09_1158 with Dissolve(1)
        ni "*Whisper* I love you!"
    else:
        pass
    scene black with Dissolve(2)
    pause 2
    scene 09_1159 with Dissolve(1)
    mc "..."
    scene 09_1160 with Dissolve(1)
    mc "Hey, here you are..."
    ni "Morning, [mc]."
    mc "Did you go for a run already?"
    ni "I did. I've let you off the hook for today."
    scene 09_1161 with Dissolve(1)
    ni "Well not really, I tried to wake you, but you didn't budge."
    mc "Hehe. Thanks, I guess..."
    scene 09_1162 with Dissolve(1)
    mc "Good morning!"
    ni "Haha... A good morning indeed."
    scene 09_1163 with Dissolve(1)
    mc "Mom not here?"
    ni "She left already. Had to be early at the cafe? I think she meant restaurant but..."
    mc "No, no. She's actually opening up a cafe."
    ni "Oh?"
    mc "Yeah. It should've been open before spring break, but there were some setbacks."
    mc "{i}(Rachel...){/i}"
    scene 09_1164 with Dissolve(1)
    mc "Is that coffee?"
    ni "Mmm-hmm."
    mc "Can I have a sip?"
    ni "Sure."
    scene 09_1165 with Dissolve(1)
    mc "..."
    mc "I always forget you put milk in your coffee."
    scene 09_1166 with Dissolve(1)
    mc "So, you're gonna spend some time with your dad today, right?"
    ni "That's the plan. I probably won't be able to pick you up."
    mc "Don't worry. A friend asked me to hang out after school."
    scene 09_1167 with Dissolve(1)
    ni "Oh, another date..."
    mc "I hope not. That'd be very awkward. I told you, I only have guy friends."
    ni "I still don't believe you!"
    mc "Haha."
    scene 09_1168 with Dissolve(1)
    ni "Are you done in the bathroom, can I go shower?"
    mc "Go ahead. I need to leave now anyway, or I'll be late again."
    ni "See you tonight, then."
    mc "Yes. Have fun with your dad."
    ni "Thanks, you too."
    scene 09_1169 with Dissolve(1)
    ni "I guess you won't be joining me?"
    mc "Don't do this to me now, Nikki!"
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 09_1170 at moveup
    pause 3
    ni "Last chance!"
    mc "Nikki!"
    menu:
        "Grab her":
            scene 09_1171 with vpunch
            mc "You really are evil!"
            ni "Pure evil!"
            mc "Obviously!"
            ni "Haha."
            scene 09_1177 with Dissolve(1)
            mc "Now I have to be in school the whole day and the only thing I'll be able to think about is this..."
            ni "Sorry, not sorry!"
            mc "..."
            scene 09_1178 with Dissolve(1)
            ""
            scene 09_1179 with Dissolve(1)
            ni "Now you can think about that."
            mc "You just made it worse!"
            ni "Haha."
        "Joke":
            scene 09_1172 with Dissolve(1)
            mc "Mom?"
            ni "..."
            scene 09_1173 with Dissolve(1)
            ni "Sorry, Emily, I..."
            mc "Haha."
            ni "Oh, you asshole!"
            scene 09_1174 with Dissolve(1)
            ni "You asshole! That's the second time you've done this to me!"
            mc "And you keep falling for it."
            ni "One day I'll get you back for this."
            scene 09_1175 with Dissolve(1)
            mc "Come here."
            ni "I thought I couldn't get more embarrassed than the pancake story, but this..."
            mc "Haha, sorry!"
            scene 09_1176 with Dissolve(1)
            ni "I'll go shower now. You'd better leave, or you'll be late."
            mc "No kiss goodbye?"
            ni "I guess you'll have to earn it again."
            mc "Haha, challenge accepted!"
    $ renpy.end_replay()
    jump Week4_Friday_Afternoon

label Week4_Thursday_Cara:
    $ Tori_Week4_Thursday_SeeCara = True
    $ Mike_Week4_Thursday_NikkiCaraDad = True
    scene black with Dissolve(2)
    pause 2
    scene 09_978 with Dissolve(1)
    mc "{i}(Cara... Seems like she didn't forget the way.){/i}"
    mc "{i}(Looks like she's daydreaming. So cute.){/i}"
    scene 09_979 with Dissolve(1)
    mc "Hey there, didn't get lost, huh?"
    c "Hehe, no."
    menu:
        "Kiss[KoGa3AutoWTChange1]{size=-4}(Cara Visit Points+2) {/size} {/color}":
            $ Cara_Visit_Points += 2
            # Cara_Visit (14)
            scene 09_980 with Dissolve(1)
            to "Grade school is on the other side of the street!"
        "Hug":
            scene 09_981 with Dissolve(1)
            mc "Thanks for picking me up. What did you do today?"
            c "Nothing much. I..."
            to "Grade school is on the other side of the street!"
    scene 09_982 with Dissolve(1)
    mc "Don't listen to her. She's lonely."
    to "..."
    mc "Let's go?"
    c "Yes."
    scene 09_983 with Dissolve(1)
    mc "What were you daydreaming about earlier? I think I could've passed you without you even noticing."
    c "I was deciding which sport I would pick if I went here."
    mc "What did you decide on?"
    c "Not going to this school."
    mc "Haha. That's also an option."
    scene 09_984 with Dissolve(1)
    c "Nikki would've loved this school, though."
    mc "She'd be on multiple teams, most likely."
    c "Haha, yeah."
    scene 09_985 with Dissolve(1)
    mc "Have you thought about what we can do today?"
    c "I have, but I just don't know..."
    mc "I can show you the city? Maybe we'll find something there."
    c "Yeah, let's do that."
    if Layla_End == True:
        pass
    else:
        scene 09_965 with Dissolve(1)
        am "What's the hold up? Can you get in the car?"
        la "One second."
    scene 09_986 with Dissolve(1)
    mc "Do you need anything from home, or can we..."
    tm "[mc]!"
    scene 09_987 with Dissolve(1)
    if Mike_Name == True:
        mc "Hey, Mike."
    else:
        mc "Hey, Coach."
    tm "You forgot your..."
    scene 09_988 with Dissolve(1)
    c "Dad..."
    tm "Cara!"
    mc "{i}(Dad? Coach Morgan is Cara's dad? Morgan... Of course. I knew it sounded familiar the first time I heard it. What are the odds?){/i}"
    scene 09_989 with Dissolve(1)
    tm "I'm so happy to see you! How are you? What are you doing here?"
    c "Vacation."
    tm "Is Nikki here too?"
    c "... No!"
    if Layla_End == True:
        pass
    else:
        scene 09_970 with Dissolve(1)
        am "What are you actually looking at?"
        am "Oh..."
        la "Do you know who that is?"
        am "That's probably Coach's daughter."
        la "Coach has a daughter?"
        am "Two!"
        scene 09_971 with Dissolve(1)
        la "{i}(How does [mc] know Coach's daughter? And why haven't I ever seen her?){/i}"
        am "Come on, get in now. I have stuff to do."
        la "{i}(She's very pretty! How old is she?){/i}"
        if MC_Girlfriend_Riverside == False:
            pass
        else:
            la "{i}(Could she be [mc]'s girlfriend?){/i}"
    scene 09_990 with Dissolve(1)
    tm "How do you know [mc]?"
    c "That's a long story!"
    mc "I'll give you guys some time. I'll..."
    c "No."
    c "We made plans, we have to leave now."
    scene 09_991 with Dissolve(1)
    tm "Can we maybe meet up tomorrow?"
    c "I don't know if I'll have time."
    tm "Please, Cara. I really want to talk to you."
    tm "How about noon tomorrow? We could go eat together?"
    c "Fine."
    tm "Thank you."
    scene 09_992 with Dissolve(1)
    mc "You okay? It looked like you didn't know he teaches here?"
    c "I'm fine. And no, I didn't know. As you may have noticed, we don't have the best relationship."
    c "When I was younger, he was the athletics coach for a sports team. Most days he was gone since he travelled with them."
    c "I was too young to understand why he was gone all the time, I thought he didn't want to be with us."
    scene 09_993 with Dissolve(1)
    c "We never really grew close, and since the divorce, we barely speak or see each other. Not like him and Nikki, they are much closer."
    mc "Does Nikki know that he lives here?"
    c "I don't think so. She surely would have mentioned it once she knew you were moving back to Madison Springs."
    mc "Hmm..."
    mc "{i}(Now I know why she never talks about her dad.){/i}"
    scene 09_994 with Dissolve(1)
    mc "I'm still a bit perplexed. Coach Mike is your dad... Wow."
    mc "{i}(Let's hope he doesn't find out all the stuff I did with his daughter.){/i}"
    c "It's funny you call him Mike."
    mc "The first time I met him, he said to call him Mike or Coach. You want me to call him Dad now?"
    c "Haha."
    scene 09_995 with Dissolve(1)
    mc "Let's go..."
    scene black with Dissolve(2)
    pause 2
    stop music fadeout 1.0
    play music "Sounds/Street_Traffic.mp3" volume 0.5
    scene 09_1180 with Dissolve(1)
    c "The city is so much bigger than I thought. So this is actually Madison Springs and not where you live?"
    mc "This is the main city, yes. We live in one of the three suburbs."
    c "Oh, okay."
    mc "There's also a big campus area, the beachfront and Old Town. That's where Mom's restaurant is located."
    scene 09_1181 with Dissolve(1)
    c "Is that close to here?"
    mc "The restaurant?"
    c "Yes."
    mc "Hmm... Fifteen minutes or so."
    c "So, we can go check it out later?"
    mc "Sure."
    scene 09_1182 with Dissolve(1)
    c "Oh..."
    mc "What?"
    c "You even have an Ashley's here!"
    mc "Uhm... Yeah..."
    scene 09_1183 with Dissolve(1)
    c "It's my favourite clothing store. Sadly we don't have one in Riverside."
    c "I always ask Nikki to drive me to Alvarado."
    mc "You've been to Alvarado?"
    c "A few times."
    mc "Heh..."
    scene 09_1184 with Dissolve(1)
    mc "Let's go in then."
    c "We don't have to. I can..."
    mc "We're here already, Cara. Maybe they'll have something you like. And it'll save Nikki a trip too!"
    c "You sure you don't mind? I know it can be very boring watching me try on clothes."
    scene 09_1185 with Dissolve(1)
    mc "I like spending time with you, and I can come up with lots of things much more boring than watching you undress..."
    c "*Shakes head*"
    scene black with Dissolve(1)
    pause 2
    stop music fadeout 1.0
    play music ("Sounds/Store2.mp3", "Sounds/Store1.mp3") volume 0.5
    scene 09_1186 with Dissolve(1)
    mc "{i}(She really likes shopping.){/i}"
    mc "{i}(I know in Riverside she could do this for hours, if not the whole day.){/i}"
    if Erynn_End == True:
        pass
    else:
        mc "{i}(I should introduce her to Erynn and they can do a shopping spree together.){/i}"
    scene 09_1187 with Dissolve(1)
    c "They also have a men's section on the other side."
    mc "Haha, I get it. I'll let you look in peace."
    c "It's not that, just..."
    mc "It's fine. Take your time."
    menu:
        "Kiss her on the cheek[KoGa3AutoWTChange1]{size=-4}(Cara Visit Points+2) {/size} {/color}":
            $ Cara_Visit_Points += 2
            # Cara_Visit (16)
            scene 09_1188 with Dissolve(1)
            ""
        "Go to men's section":
            pass
    scene black with Dissolve(1)
    pause 2
    scene 09_1189 with Dissolve(1)
    mc "{i}(Hmm... Not bad. But what about the colours? Too flashy?){/i}"
    mc "{i}(Maybe I should ask Cara what she thinks about it.){/i}"
    scene 09_1190 with Dissolve(1)
    mc "{i}(Not here?){/i}"
    mc "{i}(Is she already in a dressing room?){/i}"
    menu:
        "Check dressing rooms":
            jump Week4_Thursday_Cara_Davis
        "Wait for her":
            scene 09_1198 with Dissolve(1)
            c "[mc]?"
            mc "There you are! I was looking for you."
            c "What are you wearing?"
            mc "I tried on this shirt, what do you think?"
            jump Week4_Thursday_Cara_Clothes

label Week4_Thursday_Cara_Davis:
    if _in_replay:
        $ Cara_Visit_Points = 4
    scene 09_1191 with Dissolve(1)
    mc "..."
    mc "{i}(That's... my math teacher!){/i}"
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 09_1192 at moveup
    pause 3
    mc "{i}(Damn, that booty!){/i}"
    menu:
        "Continue[KoGa3AutoWTChange1]{size=-4}(Naomi Week4 Thursday Watch, Cara Visit Points-4) {/size} {/color}":
            $ Naomi_Week4_Thursday_Watch = True
            $ Cara_Visit_Points -= 4
            scene 09_1193 with Dissolve(1)
            mc "{i}(Yeah, looking good there Ms Davis! Mmm-mmm-mmm...){/i}"
            mc "{i}(I'm hard already.){/i}"
            scene 09_1194 with Dissolve(1)
            mc "{i}(Oh... She's taking off her bra?){/i}"
            mc "{i}(Let's watch a little more.){/i}"
            scene 09_1195 with Dissolve(1)
            mc "{i}(Look at those! I want to taste them so bad!){/i}"
            mc "{i}(Math class won't be the same from now on.){/i}"
            scene 09_1196 with vpunch
            c "[mc]?"
            mc "..."
            scene 09_1197 with Dissolve(1)
            c "What are you doing?"
            mc "{i}(Fuck!){/i}"
            mc "Uh... Looking for you. What do you think of this shirt?"
            c "..."
            $ renpy.end_replay()
        "Stop watching":
            scene 09_1198 with Dissolve(1)
            c "[mc]?"
            mc "There you are! I was looking for you."
            c "What are you wearing?"
            mc "I tried on this shirt, what do you think?"
            $ renpy.end_replay()
    jump Week4_Thursday_Cara_Clothes

label Week4_Thursday_Cara_Clothes:
    scene 09_1199 with Dissolve(1)
    c "I like the colours."
    mc "Yeah? That's the thing I wasn't sure of."
    c "But you shouldn't wear those pants with it. It doesn't match."
    mc "Haha, thanks."
    c "Want to see mine?"
    mc "Of course."
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 09_1200 at moveup
    pause 3
    mc "Where are you planning to go later?"
    c "Hehe."
    scene 09_1201 with Dissolve(1)
    c "Do you like it?"
    menu:
        "Not really":
            mc "Hmm, you look beautiful, but I don't really like the dress."
            mc "It looks more like one of those things you wear when you're cooking, you know?"
            scene 09_1202 with Dissolve(1)
            c "Haha, you mean an apron?"
            mc "Yes, an apron!"
            c "Seriously... Your mom owns a restaurant and you don't know the word for an apron?"
            c "Shows how much cooking you do! Haha."
            mc "Hey!"
            scene 09_1203 with Dissolve(1)
            c "Hmm..."
            mc "What?"
            scene 09_1204 with Dissolve(1)
            c "You're right! This does look like an apron. And now I can't unsee it."
            mc "Haha, sorry."
            c "I'm not taking this one, then. I'll try the other one. Can you close the door?"
            mc "Sure."
        "You look beautiful[KoGa3AutoWTChange1]{size=-4}(Cara Week4 Thursday Dress Like) {/size} {/color}":
            $ Cara_Week4_Thursday_Dress_Like = True
            mc "You look beautiful."
            c "Thank you."
            scene 09_1204 with Dissolve(1)
            c "Before I decide, I'll try the other one."
            c "Can you close the door?"
            mc "Sure."
    menu:
        "Wait outside":
            scene black with Dissolve(1)
            pause 2
            scene 09_1205 with Dissolve(1)
            c "What do you think?"
            mc "Pretty, very pretty!"
            jump Week4_Thursday_Cara_Home
        "Join her[KoGa3AutoWTChange1]{size=-4}(Cara Visit Points+2) {/size} {/color}":
            $ Cara_Visit_Points += 2
            # Cara_Visit (18)
            jump Week4_Thursday_Cara_Clothes_Sex

label Week4_Thursday_Cara_Clothes_Sex:
    if _in_replay:
        $ Cara_Visit_Points = 18
        $ Naomi_Week4_Thursday_Watch = False
        $ SexCounter_Cara = 3
        $ MC_SexCounter = 3
    scene 09_1206 with Dissolve(1)
    c "Uhm..."
    mc "I thought you might need some help?"
    c "Help with what?"
    mc "Undressing!"
    scene 09_1207 with Dissolve(1)
    mc "And maybe some other things, too."
    c "Here?"
    menu:
        "Have sex[KoGa3AutoWTChange1]{size=-4}(Cara Week4 Thursday Dress Sex, Cara Visit Points-2, SexCounter Cara+1, MC SexCounter+1) {/size} {/color}":
            $ Cara_Week4_Thursday_Dress_Sex = True
            $ Cara_Visit_Points -= 2
            $ SexCounter_Cara += 1
            $ MC_SexCounter += 1
            scene 09_1208 with Dissolve(1)
            ""
            scene 09_1213 with Dissolve(1)
            ""
            scene 09_1214 with Dissolve(1)
            if Naomi_Week4_Thursday_Watch == True:
                mc "{i}(I wish I could've tasted Ms Davis's tits, too!){/i}"
            else:
                ""
            scene 09_1215 with Dissolve(1)
            ""
            scene 09_1216 with Dissolve(1)
            mc "No Nikki this time to interrupt us."
            c "*Nods*"
            scene black with Dissolve(1)
            pause 2
            scene 09_1217 with Dissolve(1)
            c "*Moaning*"
            show 09_1218
            ""
            show 09_1219
            ""
            show 09_1220
            c "Haah... [mc]...! Ah..."
            c "I'm cumming!"
            scene 09_1221 with vpunch
            pause 2
            scene 09_1221 with vpunch
            ""
            scene black with Dissolve(1)
            pause 2
            scene 09_1222 with Dissolve(1)
            mc "That was great! Did you enjoy it?"
            c "Yes..."
            scene black with Dissolve(1)
            pause 2
            scene 09_1205 with Dissolve(1)
            c "What do you think?"
            mc "Pretty, very pretty!"
        "Kiss her":
            scene 09_1208 with Dissolve(1)
            ""
            scene 09_1209 with Dissolve(1)
            mc "I'll let you try on the other dress."
            c "Didn't you say you'd help me?"
            mc "If you count watching you undress as helping..."
            c "Haha."
            scene black with Dissolve(1)
            transform moveup:
                xalign 0.5 yalign 1.0
                linear 5.0 yalign 0.0
            show 09_1210 at moveup
            pause 3
            mc "{i}(I still remember the first time she was standing in front of me. She was so nervous.){/i}"
            mc "{i}(Now she undresses without a second thought. But still cute as ever.){/i}"
            c "Can you hand me the other dress."
            mc "Uh, sure."
            scene 09_1211 with Dissolve(1)
            mc "Here you go."
            c "Thanks."
            scene 09_1205 with Dissolve(1)
            c "What do you think?"
            mc "Pretty, very pretty!"
    $ renpy.end_replay()
    jump Week4_Thursday_Cara_Home

label Week4_Thursday_Cara_Home:
    scene black with Dissolve(1)
    pause 2
    stop music fadeout 1.0
    play music "Sounds/Street_Traffic.mp3" volume 0.5
    scene 09_1223 with Dissolve(1)
    c "Who would've thought you'd find something too."
    mc "Yeah. Not the usual clothing store I'd go to."
    x "Hey there."
    scene 09_1224 with Dissolve(1)
    mc "Oh hey, Mom."
    c "Hey, Emily."
    m "You also went shopping, I see."
    mc "Indeed. We both got some new clothes."
    scene 09_1225 with Dissolve(1)
    mc "Let me take that."
    m "Thank you."
    scene 09_1226 with Dissolve(1)
    mc "Where did you park?"
    m "Just around the corner here."
    m "What are the plans for the rest of the day?"
    mc "We were actually on our way to the restaurant. Are you done for today?"
    scene 09_1227 with Dissolve(1)
    m "Yes. I'm heading home. You wanted to eat there?"
    mc "Yeah. Cara wanted to try the risotto."
    m "Hmm..."
    mc "What? Do we need a reservation or something?"
    m "You won't get a reservation. We're fully booked for the next three weeks and I have already a waiting list if there is a cancellation."
    scene 09_1228 with Dissolve(1)
    mc "Oh wow. Busy."
    m "Very. I'll probably need your help for a few days next week."
    mc "No problem. So, no table at the restaurant?"
    m "You can sit and eat at the bar if you don't mind. If there's space, that is."
    scene 09_1229 with Dissolve(1)
    m "Or I can cook the risotto at home. I have everything I need for it."
    c "No, you don't have to, Emily. I'm already staying at your place and..."
    m "I don't mind at all."
    c "Only if I can help."
    m "I'd love that."
    if Cara_Week4_Thursday_Dress_Like == False:
        scene 09_1230 with Dissolve(1)
        mc "Maybe you should've gotten the apron dress since you're going to cook!"
        c "..."
        mc "Haha."
    else:
        pass
    scene black with Dissolve(2)
    pause 2
    stop music fadeout 1.0
    play music ("Music/LoFi Indie 3.mp3", "Music/LoFi Indie 1.mp3", "Music/LoFi Indie 2.mp3") volume 0.2
    scene 09_1231 with Dissolve(1)
    ""
    scene black with Dissolve(1)
    pause 2
    scene 09_1232 with Dissolve(1)
    mc "{i}(This movie is so boring...){/i}"
    mc "{i}(It's so cheesy... How can anyone enjoy this.){/i}"
    scene 09_1233 with Dissolve(1)
    mc "{i}(I could watch this for hours, though.){/i}"
    scene 09_1234 with Dissolve(1)
    mc "*Yawn*"
    c "Tired?"
    mc "Getting there."
    scene 09_1235 with Dissolve(1)
    c "Let's go sleep then. We can continue this tomorrow."
    mc "{i}(Nooo...){/i}"
    mc "Yeah."
    menu:
        "Sleep on the couch":
            scene 09_1236 with Dissolve(1)
            mc "Good night, Cara."
            c "Uh... Good night."
            mc "And if I don't see you tomorrow morning, have fun with your dad."
            c "I almost forgot about that."
            mc "Hehe. Good night!"
            jump Week4_Friday_Afternoon
        "Sleep in the bed[KoGa3AutoWTChange1]{size=-4}(Cara Visit Points+4) {/size} {/color}":
            $ Cara_Visit_Points += 4
            # Cara_Visit (22)
            jump Week4_Thursday_Cara_Home_Sex

label Week4_Thursday_Cara_Home_Sex:
    if _in_replay:
        $ Cara_Week4_Thursday_Dress_Sex = False
        $ SexCounter_Cara = 4
        $ MC_SexCounter = 4
    $ SexCounter_Cara += 1
    $ MC_SexCounter += 1
    scene 09_1237 with Dissolve(1)
    c "Uh... You're sleeping here?"
    mc "I was planning to. But if you don't want this, I can sleep on the couch again."
    c "No, it's fine."
    scene black with Dissolve(1)
    pause 2
    scene 09_1238 with Dissolve(1)
    mc "Good night."
    c "Night..."
    scene 09_1239 with Dissolve(1)
    ""
    scene 09_1240 with Dissolve(1)
    mc "..."
    scene 09_1241 with Dissolve(1)
    c "Haha."
    scene 09_1242 with Dissolve(1)
    c "Wanna do it?"
    mc "Mm-hmm!"
    scene 09_1243 with vpunch
    mc "Haha. That's a first."
    scene 09_1244 with Dissolve(1)
    ""
    if Cara_Week4_Thursday_Dress_Sex == False:
        scene 09_1245 with Dissolve(1)
        mc "Where are you going?"
        c "You'll see..."
        scene 09_1246 with Dissolve(1)
        mc "Handjob?"
        c "*Shakes head*"
        mc "Blowjob..."
        c "*Nods*"
        scene 09_1247 with Dissolve(1)
        mc "{i}(Cara making eye contact while giving a blowjob... Damn...){/i}"
        scene 09_1248 with Dissolve(1)
        mc "{i}(This feels so good.){/i}"
        show 09_1250
        ""
        scene 09_1249 with Dissolve(1)
        mc "Damn, Cara!"
        c "Hehe."
    else:
        pass
    scene black with Dissolve(1)
    pause 2
    scene 09_1251 with Dissolve(1)
    mc "Someone's horny today."
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 09_1252 at moveup
    pause 3
    mc "So pretty!"
    scene 09_1253 with Dissolve(1)
    c "Mmm..."
    scene 09_1254 with Dissolve(1)
    mc "{i}(She's actually making me cum already with her grinding.){/i}"
    show 09_1255
    ""
    scene 09_1256 with Dissolve(1)
    c "Aaah..."
    mc "You okay?"
    c "Start slowly, please."
    scene 09_1257 with Dissolve(1)
    c "*Moaning* Yes, like this..."
    show 09_1258
    mc "{i}(Fuck... I'm so close already...){/i}"
    scene 09_1259 with Dissolve(1)
    ""
    scene 09_1260 with vpunch
    pause 2
    scene 09_1260 with vpunch
    c "Haah..."
    mc "{i}(She just... too... I guess we both finished quickly.){/i}"
    scene 09_1261 with Dissolve(1)
    ""
    scene black with Dissolve(1)
    pause 2
    scene 09_1262 with Dissolve(1)
    mc "I'm gonna miss you tomorrow."
    c "I can call Dad and cancel. It's not that I really want to go."
    mc "No, I think you should talk. Besides, a friend asked me to go out with him."
    c "*Sigh* Okay..."
    scene 09_1263 with Dissolve(1)
    c "Wake me up before you leave tomorrow."
    mc "You sure? Don't be mad at me afterwards!"
    c "I won't be."
    scene black with Dissolve(2)
    pause 2
    scene 09_1264 with Dissolve(1)
    mc "Cara, I'm leaving now."
    c "Nggh... It's too early, [mc]."
    mc "Haha, I told you yesterday you'll be annoyed when I wake you."
    scene 09_1265 with Dissolve(1)
    mc "See you later. Have fun with your dad."
    c "Hmm-mmm."
    $ renpy.end_replay()
    jump Week4_Friday_Afternoon

label Week4_Friday_Afternoon:
    scene black with Dissolve(2)
    pause 2
    if Layla_End == True:
        stop music fadeout 1.0
        play music "Sounds/Street_Traffic.mp3" volume 0.5
        scene 09_1274 with Dissolve(1)
        mc "Can we make a quick stop at my house? I need to drop some stuff off."
        z "Sure thing, man."
    else:
        scene 09_1266 with Dissolve(1)
        la "[mc]!"
        if Layla_Dating == True:
            scene 09_1267 with Dissolve(1)
            la "Here, don't forget this."
            mc "Right. The Elena surprise. Thank you."
            mc "Can't wait to see her face once she sees this."
            la "Haha."
            scene 09_1268 with Dissolve(1)
            mc "When shall we go? Like Monday?"
            la "I'll ask Elena if she has time then. I'll let you know."
            mc "Cool."
        else:
            scene 09_1267 with Dissolve(1)
            mc "What's that?"
            la "Oh, this? It's a present for Elena."
            mc "Is it her birthday or something?"
            la "No, just something funny I've seen on the internet."
        if Nikki_Girlfriend == True:
            scene 09_1269 with Dissolve(1)
            la "By the way. How do you know Coach's daughter?"
            mc "Uh... You know her, too?"
            la "No. I saw her for the first time yesterday. I didn't even know Coach has a daughter."
            mc "Two, actually."
            la "Yeah, Mom told me."
            scene 09_1270 with Dissolve(1)
            la "So? How do you know her?"
            mc "Hehe. That's somewhat of a long story."
            la "Hmm... Suspicious! Tell me!"
            n "*Car honk*"
        else:
            if Cara_Girlfriend == True:
                scene 09_1269 with Dissolve(1)
                la "By the way. How do you know Coach's daughter?"
                mc "Uh... You know her, too?"
                la "No. I saw her for the first time yesterday. I didn't even know Coach has a daughter."
                mc "Two, actually."
                la "Yeah, Mom told me."
                scene 09_1270 with Dissolve(1)
                la "So? How do you know her?"
                mc "Hehe. That's somewhat of a long story."
                la "Hmm... Suspicious! Tell me!"
                n "*Car honk*"
            else:
                n "*Car honk*"
        if Layla_Dating == True:
            scene 09_1271 with Dissolve(1)
        else:
            scene 09_1271a with Dissolve(1)
        z "Are you coming? We can't be late."
        mc "Yeah, I'm ready."
        la "Is that your new car, Zach?"
        z "It sure is. Awesome right? It's called Zach Attack!"
        la "Don't call it that."
        z "Why not? It's the perfect name for this beast."
        la "..."
        scene 09_1272 with Dissolve(1)
        mc "You heard him. Gotta go."
        la "Where are you guys going?"
        mc "Zach hasn't told me yet, I don't know either."
        la "You just don't want to tell me..."
        mc "No, I really don't know. I'll tell you next time, okay?"
        if Layla_Dating == True:
            la "Fine... I'll call you once I've talked to Elena about the beach."
            scene 09_1273 with Dissolve(1)
            mc "Talk to you soon."
            la "Have fun."
        else:
            pass
        scene 09_1274 with Dissolve(1)
        stop music fadeout 1.0
        play music "Sounds/Street_Traffic.mp3" volume 0.5
        mc "Can we make a quick stop at my house? I need to drop some stuff off."
        z "Sure thing, man."
    scene black with Dissolve(1)
    pause 2
    scene 09_1275 with Dissolve(1)
    mc "So, are you telling me now where we're going?"
    z "A modelling show!"
    mc "A modelling show?"
    if Erynn_End == True:
        pass
    else:
        if Erynn_Week3_Monday_Blackmailhelp == False:
            pass
        else:
            mc "{i}(Didn't Erynn have her modelling gig today? Maybe it's that one.){/i}"
    z "Yeah. We'll be backstage. That way we can talk to the models and even watch them change clothes."
    mc "..."
    scene 09_1276 with Dissolve(1)
    mc "And how did you manage that?"
    z "I know a guy."
    mc "You know a guy?"
    z "He's a good friend of mine, you'll meet him there."
    scene black with Dissolve(1)
    pause 2
    scene 09_1277 with Dissolve(1)
    mc "When are you leaving on your family trip?"
    z "Tomorrow... For a whole freaking week."
    mc "Are you flying there, or...?"
    z "I wish we were. We're actually going by car. But it's easier with all the stuff we take with us."
    stop music fadeout 1.0
    play music ("Music/Battle_Rock.mp3", "Music/Battle_Rock3.mp3", "Music/Battle_Rock2.mp3") volume 0.6
    if Erynn_Week3_Monday_Help == False:
        scene 09_1278 with Dissolve(1)
        mc "Oh no..."
        z "What?"
        mc "Trouble ahead. What's he doing here?"
        scene 09_1279 with Dissolve(1)
        z "You mean Ethan?"
        mc "How do you know Ethan?"
        z "He's the friend I was talking about. He's got us the backstage access."
        et "Yo, Zach Attack, my man."
        scene 09_1280 with Dissolve(1)
        mc "You're friends with Ethan? Zach... He's not a good guy."
        z "Nah, you just don't know him as I do. Once you get to know him, you'll see what a cool guy he is."
        mc "..."
        scene 09_1281 with Dissolve(1)
        z "Hey Ethan, how are you? Thanks again for inviting me."
        et "Anything for a friend. I heard you've finally got your car."
        z "I did. I'll show you later. Oh, and I did call it Zach Attack."
        et "Haha, that's awesome!"
        mc "*Shakes head*"
        scene 09_1282 with Dissolve(1)
        z "Ethan, I hope you don't mind, but I've brought a friend. You might know each other. This is [mc]."
        et "We do know each other. And uh... This is difficult for me to say but I have to be honest with you, Zach."
        et "I'm not really comfortable having him here."
        z "Why not?"
        scene 09_1283 with Dissolve(1)
        et "Me and him, we have some history."
        et "When we were younger, he used to bully me."
        mc "Haha. Me bullying you? Is this a joke?"
        et "See, even now he can't admit it. For him, it was all just a game."
        mc "What the fuck are you talking about, Ethan."
        scene 09_1284 with Dissolve(1)
        et "I was always hanging around girls, just like now I guess."
        z "Hehe, you are a ladies' man, after all."
        et "And that's why we're friends, Zach. You understand me."
        et "Him on the other hand. Not so much."
        scene 09_1285 with Dissolve(1)
        et "He always got jealous when I was talking to girls, and he tried to break us apart."
        et "He was spreading rumours about me and badmouthing me to the girls. To the point of them resenting me."
        mc "Heh..."
        z "Why did you do that?"
        mc "Don't listen to this bullshit. He's a fucking liar!"
        scene 09_1286 with Dissolve(1)
        et "Me a liar? Zach, didn't you tell me something similar about a girl you liked, and now she barely talks to you? Layla, was it?"
        mc "Haha, where do you come up with this stuff?"
        z "Yeah... That's true."
        mc "What? You really believe this nonsense? Can't you see what he's doing?"
        scene 09_1287 with Dissolve(1)
        z "Ethan's right, though. How many times did you promise to help me with girls?"
        z "But you never did. Quite the opposite, actually."
        z "I told you I liked Layla when you came back. Now she's spending so much time with you and barely speaks to me anymore."
        z "She wasn't even interested when I wanted to show her my new car..."
        scene 09_1288 with Dissolve(1)
        mc "Where is this coming from, all of a sudden?"
        z "You can stop pretending now. I know what you're doing."
        mc "..."
        if Zach_Week3_Wednesday_TC_Girlshower == True:
            pass
        else:
            scene 09_1289 with Dissolve(1)
            z "What about when I told you about Elena at training camp?"
            z "You didn't even think for a second that it could've happened."
            mc "It didn't happen."
            z "But it could have."
            mc "{i}(No...){/i}"
            z "You didn't have to immediately dismiss it and laugh in my face..."
        scene 09_1290 with Dissolve(1)
        z "Then what about Valeria?"
        mc "What about her?"
        z "See! Pretending again. I know what you're doing with her."
        mc "I'm just talking to her."
        z "Talking... I've seen you 'talking' to her."
        scene 09_1291 with Dissolve(1)
        z "When she transferred to our school, she only talked to me."
        z "We had a really good thing going until I introduced her to you."
        z "Now, she barely speaks to me anymore. She even avoids me at times."
        scene 09_1292 with Dissolve(1)
        mc "And that's my fault?"
        z "Yes! Who knows what you've been saying to her behind my back."
        mc "Nothing... The only thing I told her was that you were a good guy!"
        z "Yeah right."
        scene 09_1293 with Dissolve(1)
        mc "Did it ever cross your mind that she doesn't want to be more than friends?"
        mc "You're way too pushy at times when talking to girls. How about you let them talk and actually listen to what they're saying?"
        et "See what he's doing? He's putting all the blame on you, Zach. Just like he tried with me. He's never at fault, it's always the others."
        mc "Shut up, Ethan!"
        scene 09_1294 with Dissolve(1)
        z "It's exactly as Ethan says. You always blame the others. You think you're Mr Perfect. Let me tell you, you're not!"
        mc "..."
        z "When you see a girl interested in someone else, you get jealous and can't handle it. You just want them to yourself."
        z "You weren't interested in Layla until I said I liked her. Now the same with Valeria, you..."
        mc "*Sigh* Don't be stupid, Zach!"
        scene 09_1295 with vpunch
        mc "What the fuck..."
        z "Don't call me stupid!"
        mc "I didn't. That's why I said you need to listen sometimes..."
        scene 09_1296 with vpunch
        mc "..."
        scene 09_1297 with Dissolve(1)
        mc "Are you kidding me, Zach?"
        et "Oh... Haha. That went better than expected."
        et "Zach Attack!"
        scene 09_1298 with Dissolve(1)
        et "As much as I'm enjoying this show, we have a better one to attend."
        et "Come on, Zach. Let's go. No need to waste any more of your time with this trash."
        et "I'll do what your supposed friend promised you. I'll introduce you to some hot girls! How about it?"
        z "I'd like that."
        scene 09_1299 with Dissolve(1)
        et "Do you box or anything?"
        z "No, I don't."
        et "Maybe you should. That punch was impressive. You should teach me sometime."
        z "Hehe, sure."
        mc "..."
        scene 09_1300 with Dissolve(1)
        et "[mc], one more thing."
        et "Erynn was a damn good lay, you missed out big time!"
        et "Now it's something you'll never experience."
        mc "Asshole!"
        et "Haha."
        scene 09_1301 with Dissolve(1)
        mc "{i}(Are you fucking serious?){/i}"
        mc "{i}(So much for being a friend... Good riddance!){/i}"
        jump Week4_Friday_Evening
    else:
        scene 09_1278 with Dissolve(1)
        mc "Oh no..."
        z "What?"
        mc "Trouble ahead. What's he doing here?"
        mc "{i}(Fuck. This can turn real bad, real quick.){/i}"
        scene 09_1279 with Dissolve(1)
        z "You mean Ethan?"
        mc "How do you know Ethan?"
        z "He's the friend I was talking about. He's got us the backstage access."
        mc "{i}(And it just became worse. If it was just Ethan... But no, he brought those other two clowns.){/i}"
        et "Yo, Zach Attack, my man."
        scene 09_1280 with Dissolve(1)
        mc "We should just leave, Zach. Ethan's not the guy you think he is."
        z "Nah, you just don't know him as I do. Once you get to know him, you'll see what a cool guy he is."
        mc "..."
        scene 09_1281 with Dissolve(1)
        z "Hey Ethan, how are you. Thanks again for inviting me."
        et "Anything for a friend. I heard you've finally got your car."
        z "I did. I'll show you later. Oh, and I did call it Zach Attack."
        et "Haha, that's awesome!"
        mc "*Shakes head*"
        scene 09_1282 with Dissolve(1)
        z "Ethan, I hope you don't mind, but I've brought a friend. You might know each other. This is [mc]."
        et "We do know each other. And uh... This is difficult for me to say, but I have to be honest with you, Zach."
        et "I'm not really comfortable having him here."
        z "Why not?"
        scene 09_1285 with Dissolve(1)
        et "Me and him, we have some history. Remember when I told you that I got jumped?"
        et "Well... It was him."
        z "What? [mc]? Why would you hit Ethan?"
        mc "He deserved it! He knows why!"
        et "I deserved it? I was only talking to a girl and..."
        mc "You call that talking?"
        scene 09_1284 with Dissolve(1)
        et "Okay, I'll admit it. I wasn't really talking to her. More like flirting, if you know what I mean."
        z "Hehe, you are a ladies' man after all."
        et "And that's why we're friends, Zach. You understand me."
        et "Him on the other hand. Not so much."
        scene 09_1283 with Dissolve(1)
        et "You saw her flirting with me, got jealous and sucker-punched me!"
        et "Just like years ago when you bullied me. Spreading rumours and badmouthing me to my friends. To the point of them resenting me."
        mc "Heh..."
        et "See, even now he can't admit it. For him, it was all just a game. He always got jealous when I was talking to girls, and he tried to break us apart."
        mc "Heh... You're a fucking liar!"
        scene 09_1286 with Dissolve(1)
        et "Me a liar? Zach, didn't you tell me something similar about a girl you liked and now she barely talks to you? Layla, was it?"
        mc "Haha, where do you come up with this bullshit?"
        z "Yeah... That's true."
        mc "What? You really believe this nonsense? Can't you see what he's doing?"
        scene 09_1287 with Dissolve(1)
        z "Ethan's right, though. How many times did you promise to help me with girls?"
        z "But you never did. Quite the opposite, actually."
        z "I told you I liked Layla when you came back. Now she's spending so much time with you and barely speaks to me anymore."
        z "She wasn't even interested when I wanted to show her my new car..."
        scene 09_1288 with Dissolve(1)
        mc "Where is this coming from, all of a sudden?"
        z "You can stop pretending now. I know what you're doing."
        mc "..."
        if Zach_Week3_Wednesday_TC_Girlshower == True:
            pass
        else:
            scene 09_1289 with Dissolve(1)
            z "What about when I told you about Elena at training camp?"
            z "You didn't even think for a second that it could've happened."
            mc "It didn't happen."
            z "But it could have."
            mc "{i}(No...){/i}"
            z "You didn't have to immediately dismiss it and laugh in my face..."
        scene 09_1290 with Dissolve(1)
        z "Then what about Valeria?"
        mc "What about her?"
        z "See! Pretending again. I know what you're doing with her."
        mc "I'm just talking to her."
        z "Talking... I've seen you 'talking' to her."
        scene 09_1291 with Dissolve(1)
        z "When she transferred to our school, she only talked to me."
        z "We had a really good thing going until I introduced her to you."
        z "Now, she barely speaks to me anymore. She even avoids me at times."
        scene 09_1292 with Dissolve(1)
        mc "And that's my fault?"
        z "Yes! Who knows what you've been saying to her behind my back."
        mc "Nothing... The only thing I told her was that you were a good guy!"
        z "Yeah right."
        scene 09_1293 with Dissolve(1)
        mc "Did it ever cross your mind that she doesn't want to be more than friends?"
        mc "You're way too pushy at times when talking to girls. How about you let them talk and actually listen to what they're saying?"
        et "See what he's doing? He's putting all the blame on you, Zach. Just like he tried with me. He's never at fault, it's always the others."
        mc "Shut up, Ethan!"
        scene 09_1294 with Dissolve(1)
        z "It's exactly as Ethan said. You always blame the others. You think you're Mr Perfect. Let me tell you, you're not!"
        mc "..."
        z "When you see a girl interested in someone else, you get jealous and can't handle it. You just want them to yourself."
        z "You weren't interested in Layla until I said I liked her. Now the same with Valeria, you..."
        mc "*Sigh* Don't be stupid, Zach!"
        scene 09_1295 with vpunch
        mc "What the fuck..."
        z "Don't call me stupid!"
        mc "I didn't. That's why I said you need to listen sometimes..."
        scene 09_1296 with vpunch
        mc "..."
        scene 09_1297 with Dissolve(1)
        mc "Are you kidding me, Zach?"
        et "Oh... Haha. That went better than expected."
        et "Zach Attack!"
        scene 09_1298 with Dissolve(1)
        et "As much as I'm enjoying this show, we have a better one to attend."
        et "Come on, no need to waste any more of your time with this trash."
        et "I'll do what your supposed friend promised you. I'll introduce you to some hot girls! How about it?"
        z "I'd like that."
        et "You go ahead and I'll meet you inside. I need to have a little chat with [mc] first. We have some... Unfinished business!"
        scene black with Dissolve(1)
        pause 2
        scene 09_1302 with Dissolve(1)
        et "How was that? Oscar-worthy, no?"
        et "Maybe I should try acting, what do you think?"
        x "Hehe, why not?"
        et "Well, enough playing around. Guys!"
        scene 09_1303 with vpunch
        mc "Hey!"
        et "So..."
        scene 09_1304 with Dissolve(1)
        et "Wohoho... Hold on there, Bruce Lee. I only wanted to talk."
        mc "Sure... Talk! That's why your two buffoons here are restraining me?"
        et "Yeah, you're right."
        scene 09_1305 with vpunch
        mc "*Cough*"
        et "Did you think there wouldn't be any consequences?"
        scene 09_1306 with Dissolve(1)
        et "You really should stay out of my business. You're costing me a lot of money."
        mc "What business is that? Blackmailing models?"
        et "I see. Erynn told you about the video, huh?"
        et "The precious deflowering. It's a work of art, really. Want to see it?"
        mc "You sick piece of shit!"
        et "I'll take that as a yes. Let's watch it together!"
        scene 09_1307 with Dissolve(1)
        et "Look at that amazing body. No wonder she's getting a lot of lingerie gigs."
        mc "..."
        et "Have you ever seen her naked? Don't look away!"
        scene 09_1308 with vpunch
        et "Come on now, don't make me force you. Enjoy it."
        et "I'll even put the sound on so you can hear the cutest moans you'll ever hear."
        scene 09_1309 with Dissolve(1)
        et "Oh, here comes my favourite part. Look at her expression and listen carefully."
        et "You can see the exact moment her hymen ruptures."
        mc "..."
        mc "{i}(I'm so sorry, Erynn.){/i}"
        if Erynn_LikeMC == True:
            et "So, what did... Are you crying? Aw... You're such a sweet guy."
            et "You really love her, huh?"
        else:
            et "What did you think? Want to rate it? Keep in mind it was her first time."
            mc "Motherfucker!"
            et "Don't be rude now. I just showed you my most precious possession."
        scene 09_1312 with Dissolve(1)
        mc "What do you want? Just leave her alone!"
        et "Hasn't Erynn told you what I want?"
        mc "You're a fucking bastard!"
        et "So you do know. It's just one time. What's the big deal? After that, I'll delete the video! I promise."
        mc "..."
        if Alexis_Dating == True:
            scene 09_1313 with Dissolve(1)
            et "I might have another idea. I've heard you're dating Alexis."
            mc "Shut up! Don't you dare involve her!"
            et "What are you getting so mad for, all of a sudden? You didn't even hear my proposition."
            scene 09_1314 with Dissolve(1)
            et "One blowjob from Alexis, that's it!"
            mc "I told you to shut up and leave her out of this!"
            et "Are you scared that she'll choose Erynn over you and actually do it?"
            et "Why don't you ask her? Hmm?"
            et "I've known her much longer than you, and if you ask me, I think she will. She would do anything to help Erynn, especially now since their relationship is... rocky, to say the least."
        else:
            pass
        scene 09_1315 with vpunch
        n "*Slap*"
        et "So, what's it gonna be? Help me, help Erynn."
        if Valeria_Points >= 13:
            $ Valeria_Week4_Friday_Help = True
            scene 09_1330 with vpunch
            et "..."
            scene 09_1331 with Dissolve(1)
            mc "Val?"
            scene 09_1335a with Dissolve(1)
            et "Fuck!"
            et "Grab her!"
            scene 09_1332 with vpunch
            x "You fucking bitch!"
            va "Aaah..."
            mc "Let go of her, fuckface!"
            scene 09_1319 with vpunch
            mc "..."
            scene 09_1333 with vpunch
            mc "I said let go of her!"
            scene 09_1334 with vpunch
            va "DON'T TOUCH ME..."
            mc "Val, it's me. Come on, we need to get out of here."
            scene 09_1335 with Dissolve(1)
            et "You're going to regret this! You know who'll pay for this!"
            et "You hear? This isn't over!"
            scene black with Dissolve(1)
            pause 2
            scene 09_1336 with vpunch
            mc "FUCK!"
            va "Are you alright?"
            scene 09_1337 with Dissolve(1)
            mc "WHY WERE YOU THERE? WHY DIDN'T YOU JUST LEAVE?"
            va "Why are you screaming at me? I just tried to help!"
            mc "BECAUSE I DIDN'T WANT YOU TO GET INVOLVED IN THIS MESS, VALERIA! FUCK!"
            scene 09_1338 with Dissolve(1)
            mc "*Sigh*"
            va "Sorry."
            mc "..."
            mc "I'm sorry I yelled at you. And thank you for helping me."
            scene 09_1339 with Dissolve(1)
            va "Are you hurt?"
            mc "*Nods*"
            va "Want me to call a doctor?"
            mc "I meant... Not physically."
            scene 09_1340 with Dissolve(1)
            va "It's gonna be alright."
            mc "I don't know, Val. It's bad."
            va "Can you tell me?"
            mc "I want to, but I can't. You can't get involved in this. That guy is dangerous."
            mc "Give me a second to calm down..."
            scene black with Dissolve(2)
            pause 2
            stop music fadeout 1.0
            play music ("Music/LoFi Upbeat 1.mp3", "Music/LoFi Upbeat 2.mp3", "Music/LoFi Upbeat 3.mp3", "Music/LoFi Upbeat 4.mp3") volume 0.2
            scene 09_1341 with Dissolve(1)
            mc "Sorry, with all the stuff on my mind right now, I didn't even ask how you are."
            va "I'm good."
            mc "Yeah? Not hurting? That guy almost ripped your hair out."
            va "He got a few."
            scene 09_1342 with Dissolve(1)
            va "I might have a new reason to wear my hat if I end up having a bald spot. So, no biggie."
            mc "Heh..."
            va "At least that made you smile."
            scene 09_1343 with Dissolve(1)
            mc "No, but seriously, let me have a look, just to be sure."
            va "Go ahead."
            mc "Can I remove the hairband?"
            va "Sure."
            scene 09_1344 with Dissolve(1)
            va "How does it look? Do I have to wear my beanie all day now?"
            mc "Haha, no. Plenty of hair left. Still pretty!"
            va "What a letdown."
            scene 09_1345 with Dissolve(1)
            mc "Hey, Val?"
            va "Hmm?"
            mc "Thanks again for what you did. I didn't expect to leave that scene without a bruise..."
            mc "But you're crazy for doing so, you know that?"
            va "Cute but crazy!"
            mc "Haha, exactly."
            menu:
                "Kiss her[KoGa3AutoWTChange1]{size=-4}(Valeria Points+2) {/size} {/color}":
                    $ Valeria_Points += 2
                    # Valeria (18)
                    scene 09_1346 with Dissolve(1)
                    n "*Bzzzt. Bzzzt*"
                    scene 09_1347 with Dissolve(1)
                    va "Sorry, it's probably my mom. I'm supposed to meet her."
                    mc "You'd better pick up then."
                "Do nothing":
                    n "*Bzzzt. Bzzzt*"
                    scene 09_1348 with Dissolve(1)
                    va "That's probably my mom. I'm supposed to meet her."
                    mc "You'd better pick up then."
            scene 09_1349 with Dissolve(1)
            va "Hi, mama."
            x "Hola, cariño."
            x "Where are you? I've been waiting here for ten minutes."
            va "Sorry, I got..."
            scene 09_1350 with Dissolve(1)
            va "... distracted!"
            va "I'm on my way though. I'll be there shortly."
            x "Okay, see you soon then. Chao-chao."
            scene 09_1351 with Dissolve(1)
            va "I guess that's my cue to leave."
            mc "Do you want me to go with you?"
            va "No need, it's not that far."
            scene 09_1352 with Dissolve(1)
            va "No fighting without me, okay?"
            mc "I can't promise you that."
            va "..."
            scene 09_1353 with Dissolve(1)
            va "Bye, [mc]."
            mc "Thank you for being here for me. Oh, and Val?"
            va "Hmm?"
            mc "Be careful!"
            scene 09_1354 with Dissolve(1)
            va "Don't worry about me. I'm gonna be fine..."
            va "Famous last words!"
            mc "Not funny!"
            va "Haha."
            scene 09_1355 with Dissolve(1)
            mc "*Sigh*"
            mc "{i}(What should I do now?){/i}"
            mc "{i}(Should I even tell Erynn about the video? I so hoped it wouldn't be real...){/i}"
            if Alexis_Dating == False:
                pass
            else:
                mc "{i}(And what about Lexi? If he touches her...){/i}"
            scene 09_1355a with Dissolve(1)
            mc "{i}(Hmm... She's not picking up.){/i}"
            jump Week4_Friday_Evening
        else:
            show 09_1316
            et "..."
            scene 09_1317 with Dissolve(1)
            mc "John!"
            x "Who's this motherfucker?"
            scene 09_1318 with Dissolve(1)
            x "You're messing with the wrong guy, old man!"
            jo "..."
            scene 09_1319 with vpunch
            mc "You can also let go of me now!"
            scene 09_1320 with vpunch
            jo "{i}(Old man?){/i}"
            scene 09_1321 with Dissolve(1)
            jo "We need to get out of here, [mc]."
            jo "[mc]?"
            jo "Come, get on."
            scene 09_1322 with Dissolve(1)
            mc "..."
            scene black with Dissolve(1)
            pause 2
            scene 09_1323 with vpunch
            mc "FUCK!"
            jo "..."
            jo "Want to talk about what happened?"
            scene 09_1324 with Dissolve(1)
            mc "The phone!"
            jo "What phone?"
            mc "I need to go back, I need that phone."
            jo "No, we can't go back there, police might have shown up already. Let's get off the street for now. Besides, I can use a drink. How about you?"
            mc "Sure... Let me make a quick call."
            scene 09_1324a with Dissolve(1)
            mc "..."
            mc "Hmm... Not picking up."
            scene 09_1325 with Dissolve(1)
            jo "Two beers, please."
            bt "Coming right up."
            scene 09_1326 with Dissolve(1)
            jo "So, what was that about?"
            mc "No offence, John. But I don't want to involve anyone in this mess."
            jo "Like it or not, I'm involved already."
            mc "*Sigh*"
            mc "It's about a friend. She's getting blackmailed by that guy..."
            scene black with Dissolve(1)
            pause 2
            stop music fadeout 1.0
            play music ("Music/LoFi Upbeat 1.mp3", "Music/LoFi Upbeat 2.mp3", "Music/LoFi Upbeat 3.mp3", "Music/LoFi Upbeat 4.mp3") volume 0.2
            scene 09_1327 with Dissolve(1)
            jo "*Shakes head* Despicable!"
            jo "Who's the guy anyway?"
            mc "He's her agent and the son of the CEO."
            jo "That's bad. Means he has lots of connections."
            scene 09_1328 with Dissolve(1)
            jo "Do you know what you're going to do?"
            if Erynn_Week3_Monday_Blackmailhelp == False:
                mc "I told her that I'm here if she needs me, but I can't help her with that. It's..."
                jo "I understand, but she's still your friend, no?"
                jo "If that happened to Iris, I'd kill that guy. No questions asked!"
                jo "Just think about it."
            else:
                mc "I don't. I know the video is real, so probably getting rid of that first."
                jo "You'll figure it out."
            scene 09_1329 with Dissolve(1)
            jo "And if you need my help, I've got your back, always."
            mc "Thanks, John."
            jump Week4_Friday_Evening

label Week4_Friday_Evening:
    scene black with Dissolve(2)
    pause 2
    if Nikki_Girlfriend == True:
        scene 09_1356 with Dissolve(1)
        m "[mc]! Can you come here for a minute?"
        mc "{i}(Oh, is Nikki back?){/i}"
        mc "Coming."
    else:
        if Cara_Girlfriend == True:
            scene 09_1356 with Dissolve(1)
            m "[mc]! Can you come here for a minute?"
            mc "{i}(Oh, is Cara back?){/i}"
            mc "Coming."
        else:
            scene 09_1356a with Dissolve(1)
            m "[mc]! Can you come here for a minute?"
            mc "Coming."
    scene 09_1357 with Dissolve(1)
    mc "Oh... Hey, Melissa."
    me "Hi."
    mc "If you're here for the backyard, I can do it tomorrow."
    me "Thanks, but it's actually about Erynn."
    scene 09_1358 with Dissolve(1)
    mc "Did something happen?"
    me "I don't know. That's why I came here to ask if you've talked to her today?"
    mc "Not today, no. Why?"
    if Erynn_End == True:
        mc "{i}(I'd probably be the last person she'd call.){/i}"
    else:
        pass
    me "We were supposed to meet up, but she never showed up. Normally when something comes up, she calls to let me know."
    scene 09_1359 with Dissolve(1)
    if Erynn_End == True:
        me "I tried calling her several times, but she didn't pick up. She isn't at her apartment either."
    else:
        if Erynn_Week3_Monday_Blackmailhelp == False:
            me "I tried calling her several times, but she didn't pick up. She isn't at her apartment either."
        else:
            mc "Doesn't she have a modelling gig today?"
            me "That was this morning. I tried calling her several times, but she didn't pick up. She isn't at her apartment either."
            mc "Hmm..."
    me "I thought that maybe you might have an idea where she is?"
    mc "Sorry, I don't."
    scene 09_1360 with Dissolve(1)
    m "Can you maybe check some clubs and bars and see if she's there?"
    mc "Yeah, sure."
    m "Thank you."
    scene black with Dissolve(2)
    pause 2
    stop music fadeout 1.0
    play music "Music/Suspense.mp3" volume 0.5
    scene 09_1361 with Dissolve(1)
    mc "{i}(Still nothing.){/i}"
    if Erynn_End == True:
        mc "{i}(If I was her, I probably wouldn't answer my calls either...){/i}"
    else:
        pass
    mc "{i}(I hope this doesn't have anything to do with Ethan...){/i}"
    if Alexis_Dating == True:
        mc "{i}(Maybe I should call Alexis? She might know where she usually hangs out.){/i}"
        scene black with Dissolve(1)
        pause 2
        scene 09_1362 with Dissolve(1)
        mc "Hey."
        a "Hey, how are you?"
        mc "Lexi, listen..."
        scene 09_1363 with Dissolve(1)
        a "You okay? Has something happened?"
        mc "I don't know. You have to do me a favour."
        a "You're scaring me!"
        mc "Can you try to call Erynn?"
        scene 09_1364 with Dissolve(1)
        a "Something happened to Erynn?"
        mc "As I said, I don't know. No one knows where she is and we can't reach her, either."
        a "Where are you? I'll..."
        mc "Just try to call her and..."
        scene 09_1365 with Dissolve(1)
        a "[mc]! Where are you right now?"
        mc "I'm heading to Heaven to see if she's there."
        a "What street?"
        mc "Uhm... Ocean Avenue."
        a "Stay there, don't move!"
        scene 09_1366 with Dissolve(1)
        la "What happened?"
        a "Sorry, not now, Layla."
        a "Tell Mom I'll be back later."
        la "Sure."
        scene black with Dissolve(2)
        pause 2
        scene 09_1367 with Dissolve(1)
        ""
        scene 09_1368 with Dissolve(1)
        a "Hey. Any news?"
        mc "No, nothing."
        a "This is so unlike her. Let's go."
        scene 09_1369 with Dissolve(1)
        mc "Come on... Just pick up!"
        a "..."
        mc "Erynn..."
        scene 09_1370 with Dissolve(1)
        mc "I have an eerie feeling about all of this."
        a "Me too."
        mc "*Sigh*"
        scene 09_1371 with Dissolve(1)
        play sound "Sounds/Phone_Vibrate.mp3"
        n "*Bzzzt. Bzzzt*"
    else:
        scene 09_1372 with Dissolve(1)
        mc "Come on... Just pick up!"
        mc "Erynn..."
        scene 09_1373 with Dissolve(1)
        mc "{i}(I have an eerie feeling about all of this.){/i}"
        mc "*Sigh*"
        scene 09_1371 with Dissolve(1)
        play sound "Sounds/Phone_Vibrate.mp3"
        n "*Bzzzt. Bzzzt*"
    jump Episode_10_Start

# Max Points:

# Alexis (42)
# Melissa (14)
# Layla (70)
# Elena (32)
# Emily (16)
# Erynn (40)
# Tori (16)
# Cara (16)
# Nikki (20)
# Lakeyn (6)
# Brooke (4)
# Adriana (4)
# Naomi (2)
# Valeria (18)
# Zach (10)
# Darryl (2)
# ShaCarri (4)
# Iris (2)

# MC_GoodStudent (14)

# Nikki_Weekend (10)
# Nikki_Visit (28)
# Cara_Weekend (6)
# Cara _Visit (22)
# Alexis_SP (2)
# Alexis_Jealous (2)

# MC_Sex (27)
# Alexis_Sex (8)
# Tori_Sex (2)
# Lakeyn_Sex (1)
# Nikki_Sex (5)
# Cara_Sex (5)
# Julia_Sex (1)
# Rachel_Sex (1)
# Gabi_Sex (2)
# Iris_Sex (2)

#WTAdded
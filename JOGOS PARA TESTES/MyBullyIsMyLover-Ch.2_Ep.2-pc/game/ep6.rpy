default freyacheckpanties = False
default naomitakecoffee = False
default freyaselfielike = False
default ainehelpbuildpc = False
#default gwenskyharem = False
default ainebreakfastheadpat = False
default lilytracksory = False

label ep6:
    scene ep5e
    with dissolve
    $ renpy.pause()
    scene ep6
    with dissolve
    $ renpy.pause()
    play music 'audio/HighLine.mp3' fadein 2
    image emmctbaep:
        "ep6_1.jpg"
        pause 3.0
        "ep6_2.jpg"
        pause .2
        repeat
    show emmctbaep
    with dissolve
    mc "Whoa~! What the... heck...?"
    mc "What's with the big smile so early in the morning?"
    e "......"
    e "It's not that early."
    mc "Well... yeah... but I never saw you smile at least once before. So what's with today?"
    e "...It's my birthday."
    mc "For real~?!"
    e "Please don't shout."
    mc "Wait, are you being serious?"
    e "I'm not joking in the very least."
    mc "Huh... But you never celebrated your birthday in high school."
    mc "Like... everyone would celebrate theirs. I thought yours was outside of the school year."
    scene ep6_3
    with dissolve
    e "No, I never celebrated my birthday after..."
    e "......"
    mc "Hm?"
    e "...Nevermind."
    menu:
        "Make her smile":
            scene ep6_4
            with dissolve
            mc "Well, don't be sad now! It's your birthday, isn't it?"
            mc "Just keep on smiling! Haha!"
            e "Mhf..."
            $ emmapoint += 1
            $ renpy.notify(emmanotif)
            e "O-okay..."
            mc "Good!"
            mc "I'm going to work, then. It's almost time for today's opening."
        "Don't bother":
            mc "Well... if you say so..."
            mc "I'm going to work, then. It's almost time for today's opening."

    image emmctbaep2:
        "ep6_5.jpg"
        pause 3.0
        "ep6_6.jpg"
        pause .2
        repeat
    show emmctbaep2
    with dissolve
    e "Where do you work?"
    mc "Where else? At the town's best burger shack, of course! Woody Burger! Hahaha!"
    e "{i}...He's still the same airhead even after so long, huh?"
    e "{i}...I guess that's why I liked him in the first place, he never gets boring."
    e "I'll come with you."
    mc "Uhh... Isn't your station far from here?"
    e "I never told you where I work, why would you think that it is?"
    mc "Well... There are two stations here so..."
    e "Mine is not that far from where you work, don't worry. I always just walk back and forth."
    mc "Hmm... If that's the case..."
    mc "Alright then, let's go!"

    scene black
    with dissolve
    with fade

    play sound 'audio/traffic.mp3' loop fadein 2
    scene ep6_7
    with dissolve
    e "I should be asking you. Why are you so happy today?"
    e "I know that you still don't trust me and Aine, so you don't come and talk to me very often."
    e "Unless... I'm the one who starts a conversation first."
    menu:
        "It's nothing like that":
            mc "It's not that I'm happy or anything. I mean, it's Sunday. I just want to start the new week with a bang, you know?"
        "Well...":
            mc "Well... It would be such a waste to start the new week negatively."

    mc "In fact, I'm always like this. You'll just have to get used to it. Haha."
    scene ep6_8
    with dissolve
    mc "And to tell you the truth..."
    mc "Yes, I still don't trust you and Aine. But what's the point of distancing myself from you two?"
    mc "Yeah, you gave me a hard time, mopped the floor with me, and all sorts of things that I don't even want to recall."
    mc "But I'm not an asshole, at the very least. I did let you come into my house, didn't I?"
    mc "Now that I know part of the truth, it at least gives me comfort that I somehow did not do the wrong thing."
    mc "Grudge? Revenge? Pff!"
    mc "Fuck that shit! What do I get from doing or having those? It would absolutely not bring me any benefit!"
    mc "I just want to be happy and set my life straight, you know?"
    mc "However, one wrong move, and I will confidently throw you out of the window. Ahaha!"
    e "I know that, don't worry."
    scene ep6_9
    with dissolve
    mc "Do you at least feel a bit of remorse for what you did to me back then?"
    e "Yes, I do..."
    mc "Then, that's enough reason for me to talk to you. Although, you still have to do something else if you really want me to totally forgive you."
    mc "No matter what reason you had for your actions, it's still you who did it. Your actions, your responsibility."
    mc "And I'm gonna leave that up to you, because I honestly don't know what it should be. HAHAHA!"
    e "You're crazy..."
    scene ep6_10
    with dissolve
    mc "Well, yeah! Call me cra-"
    image emmcotwwt:
        "ep6_11.jpg"
        pause 3.0
        "ep6_12.jpg"
        pause .2
        repeat
    show emmcotwwt
    with dissolve
    mc "......"
    mc "...Huh?"
    e "What?"
    mc "...Nothing, I just... felt something weird."
    e "{i}Did he remember something? I better change the topic. Besides, I'm really curious about something...{/i}"
    e "I'm actually curious about you back then... Why didn't you fight back? Was it really just because of your feelings for Aine?"
    mc "...Now that you mention it again... yeah, that was one of the reasons."
    mc "That's probably one of the worst decisions I made in the past."
    mc "Ugh! I was such a derp, that's for sure!"
    mc "Although... there's another reason why I tried to endure it."
    e "Hm?"
    mc "...I just had a gut feeling, an impression that I wasn't even sure of before, but... There were times when I caught her napping."
    mc "It was like she was in real pain, and she kept on mumbling about something I couldn't understand. I tried patting her head once, and for some reason, she was suddenly comforted."
    mc "Yeah, yeah... I know what you are going to say... I was foolish to do that for the girl who mistreated me, but I wanted to find out the real reason why she was doing that."
    mc "I confessed to her, alright..."
    mc "But that was too shallow a reason to do all those things to me, even for her."
    mc "In fact, before the school year started, we already..."
    mc "......"
    e "What is it?"
    mc "Ah, nothing. Nevermind that."
    mc "Anyway, my curiosity sure got me killed. And I regretted the fact that I did all those things for her."
    e "You could've just stayed away from us."
    mc "How could I? We were in the same class!"
    e "Transferred schools, then?"
    mc "I'm not a pussy to run away. But even if I wanted to, it wouldn't have been that easy — our high school was the only one in this city."
    mc "With Klara overseas, it would've been hard to do. It was still thanks to her that all this shit stopped, though."
    mc "But hey, nobody's perfect. And I changed, mentally and physically, I am not the same person I once was."
    e "Are you sure about that?"
    mc "Why not give me the benefit of the doubt? Ahahaha!"
    e "{i}I still wonder what Miss Klara did to make the school principal accept her request. I was certain the principal was one of Hera's lackeys."
    e "Did you know that the principal was one of Aine's mother's lackeys?"
    mc "Well, I'm not shocked to know that now. She gives me the impression that nothing is impossible for her."
    e "So what's your plan? Have you come up with anything yet?"
    mc "Yes. I wanted to talk to her personally and hear everything from her own mouth."
    mc "Don't get me wrong, I'm not doing this for you guys. I still think your plan was too stupid for a detective to come up with, you know?"
    mc "Especially since you know her very well."
    scene ep6_13
    with dissolve
    e "*sighs*..."
    mc "I'm doing this for my own peace of mind. Will I help you or not? That depends on her answers."
    image emmcotwwt2:
        "ep6_14.jpg"
        pause 3.0
        "ep6_15.jpg"
        pause .2
        repeat
    show emmcotwwt2
    with dissolve
    e "I see..."
    e "But how will you do it? It's not that easy to get even a minute of her time."
    mc "I know someone who's close to her. She managed to arrange a meeting with me and Hera in a cafe less than three weeks from now."
    e "Good luck with that, then. Let me know what you two speak about once it's done."
    mc "You really don't have a single clue about it?"
    e "I already told you what I know."
    e "{i}And probably what I can disclose..."
    mc "Well, that sucks... I'll see what I can do, then. I'm not afraid of her."
    e "You should be."
    mc "Meehh... She could've killed me already if she wanted to. But nothing has happened over all these years."
    e "I see your point."
    e "{i}And I wonder why she didn't do anything aside from making us bully [mc]. I don't know what her real plan or true intentions are, myself."
    scene ep6_16
    with dissolve
    mc "Well, I think this is where we part ways. I go this direction next."
    e "Alright..."
    scene ep6_17
    with dissolve
    mc "I'll see you later then. Bye!"
    e "Mhm..."
    scene ep6_18
    with dissolve
    e "......"
    scene ep6_19
    with dissolve
    mc "Oh, hey. I forgot."
    e "Hm?"
    menu:
        "Nevermind":
            mc "Oh, uhh... Nevermind."
            mc "I'll see you later."
            e "Mhm..."
        "Greet her":
            $ emmapoint += 1
            $ renpy.notify(emmanotif)
            mc "Happy birthday."
            e "Thanks."
            mc "I'll see you later."
            e "Mhm..."
            scene ep6_20
            with dissolve
            $ renpy.pause()
            scene ep6_21
            with dissolve
            e "...*blushes*"
            scene ep6_22
            with dissolve
            e "Mhrrmmnnn...!!!"
            scene ep6_23
            with dissolve
            $ renpy.pause()

    scene ep6_24
    with dissolve
    e "*sighs*..."
    e "Now that I remember everything..."
    scene ep5_446
    with flash
    $ renpy.pause()
    scene ep3_311
    with dissolve
    $ renpy.pause()
    scene ep6_24
    with dissolve
    e "That was Amber we met at the supermarket last time..."
    e "But why did she pretend that she doesn't know us? Did she forget?"
    e "No, I doubt that. She was acting strange at that time. Was she there by coincidence?"
    e "Just who is she? And why do I feel like she's been watching over us?"
    e "......"
    scene ep6_25
    with dissolve
    e "Ahh! Time to focus! I have to concentrate on my new case!"
    stop music fadeout 2
    stop sound fadeout 2

    scene black
    with dissolve
    with fade

    play music 'audio/BlackCat.mp3' fadein 2
    scene ep6_26
    with dissolve
    mc "Holy shit! I lost track of time talking to Emma! Now I'm five minutes late!"
    mc "I hope Lily is fine handling the opening on her..."
    scene ep6_27
    with dissolve
    "*muffled crowd noise*"
    scene ep6_28
    with dissolve
    mc "...own..."
    mc "WHAT IN THE WORLD IS THIS MAYHEM?!"
    mc "Why are there so many customers already?!"
    play sound 'audio/busyrestaurant.mp3' loop fadein 2
    scene ep6_29
    with dissolve
    yt "Wait... who's..."
    scene ep6_30
    with dissolve
    yt "Freya?!"
    scene ep6_31
    with dissolve
    om "Wahaha! The burgers here are excellent! How come I didn't know about this place until now?"
    scene ep6_32
    with dissolve
    om "You should try their menu, young man! I'm sure you won't regret it!"
    mc "Uhm... I actually work here, sir."
    om "Oh, you are? Then I must commend you guys for doing such a good job with your food. Especially bringing that girl out."
    om "She sure reminds me of my teenage years! I can die happy now if you like!"
    mc "No, you shouldn't!"
    om "Well, I guess I need to live a lot longer to experience more of this kind of food."
    om "Please tell your manager that I love him or her."
    mc "I beg your pardon?"
    scene ep6_31
    with dissolve
    om "Hahahaha!"
    mc "Uhh... please excuse me, sir. I'm gonna have a chat with my colleague."
    scene ep6_32
    with dissolve
    om "Don't mind me, young man. I'm just chilling."
    yt "Now that was weird..."
    scene ep6_33
    with dissolve
    mc "Excuse us for a minute, ma'am."
    scene ep6_34
    with dissolve
    mc "*whispers* Come with me!"
    image frecmct:
        "ep6_35.jpg"
        pause 3.0
        "ep6_36.jpg"
        pause .2
        repeat
    show frecmct
    with dissolve
    f "Hey, [mc]! What's up?"
    mc "No, you tell me 'what's up'! How come there're this many customers at this time and why are you dressed..."
    mc "In that..."
    mc "...sexy..."
    f "Heeh... You like it?"
    menu:
        "I like it":
            $ freyapoint += 1
            $ renpy.notify(freyanotif)
            mc "I mean, yeah... I like it. But isn't it too revealing for your age?!"
        "I guess so...":
            mc "I guess so? But it's too revealing for your age if you ask me!"

    scene ep6_37
    with dissolve
    f "For my age~? I'm legal, officer! What are you talking about?!"
    scene ep6_38
    with dissolve
    f "Teehee~!"
    mc "Don't 'teehee' me!"
    image frecmct2:
        "ep6_39.jpg"
        pause 3.0
        "ep6_40.jpg"
        pause .2
        repeat
    show frecmct2
    with dissolve
    f "And for the record, I got permission from Jess to do this! In fact, she was all over my idea!"
    mc "Is she for real?!"
    f "Yeppers! She even mentioned this the last time we had a meeting together!"
    #flash of that meeting
    mc "Now that you mention it, yeah, I remember now. But I didn't expect it to be something like this."
    f "Yeah! Jess wanted to surprise you and Lily with this, but I figured I should let Lily know in advance."
    mc "Well it worked, I'm not gonna lie! I still don't get the outfit choice though. Why that?"
    f "Haha! You can consider me our official mascot!"
    mc "I'm sorry?"
    f "I told you I'm a streamer, right?"
    mc "Yeah...? And what kind of stream do you do?"
    f "I stream games while wearing outfits like this! My fanbase likes them a lot!"
    mc "Alright, that's it! I'm calling the FBI!"
    scene ep6_41
    with dissolve
    f "I told you, I'm legal, you moron! And I'm a cosplayer, not a Twitch thot!"
    mc "Yeah, yeah... You're nineteen, alright..."
    mc "But that still doesn't convince me!"
    image frecmct3:
        "ep6_42.jpg"
        pause 3.0
        "ep6_43.jpg"
        pause .2
        repeat
    show frecmct3
    with dissolve
    f "Check my employee profile later if that's what it takes to convince you, but trust me, the burger shack will greatly benefit from this!"
    f "While working here, I'll take a lot of selfies and post them on my Twitter account {b}@flatoverfat{/b}. Check my profile if you have some time."
    mc "Flat what?"
    f "Flat over fat!"
    mc "Oh god..."
    f "You can talk to Jess about the details too, if you prefer."
    f "I got your phone number from her, so we can talk later. We don't have time to chit-chat right now."
    mc "Yeah, let's do that."
    f "Great! You should get to the counter as soon as possible, though! Lily might need life support already! Just leave things out here to me, just like what Jess planned."
    mc "Yeah, I'll just change into my uniform quickly. Tell Lily I'll be there soon."
    f "Got it!"
    scene ep6_44
    with dissolve
    f "Alright~! Let's gooooo~!"
    yt "This girl is leaving me speechless. Like... literally."
    menu:
        "Check her out":
            $ freyacheckpanties = True
            scene ep6_45
            with dissolve
            yt "Holy... shit...! Kitty cat panties, huh? That fits her in a lot of ways, I must say!"
            scene ep6_46
            with dissolve
            f "{i}Heeh... He's checking me out?"
            scene ep6_47
            with dissolve
            f "{i}That's a good sign. *giggles*"
        "Don't risk it":
            $ freyacheckpanties = False
            yt "Nahh... better not risk it and waste time. I've got to go to Lily now."
    stop sound fadeout 2

    scene black
    with dissolve
    with fadeq

    "After the shift..."

    scene black
    with dissolve
    with fadeq

    scene ep6_48
    with dissolve
    l "Ahhh~! Finally! We survived!"
    l "What in the world just happened?"
    scene ep6_49
    with dissolve
    mc "Here, take this. It's on me."
    l "Oh! Thanks, [mc]."
    scene ep6_50
    with dissolve
    mc "I should be the one to ask you that. What just happened? How the heck did Freya attract so many customers?"
    l "To be honest? I have no idea."
    scene ep6_51
    with dissolve
    l "I saw her take a selfie and start giggling after a minute of staring at her phone."
    scene ep6_52
    with dissolve
    l "Then she ran out with a poster for the shop in her hand."
    scene ep6_53
    with dissolve
    l "Before I knew it, she had a horde of people following her, and me dying trying to handle the onslaught of customers."
    l "And you were late!"
    mc "Sorry, I was talking to someone on my way here and lost track of time. I'll be early tomorrow, I promise."
    l "We handled the opening just fine by ourselves, though, so that's good. I just didn't expect it to be that chaotic."
    mc "I didn't either, it's just we weren't able to prepare for it. What was Miss Jess thinking to catch us off guard like that?"
    l "She might be testing us, who knows?"
    mc "Knowing her? That might be the case, yes."
    mc "But damn... We doubled our usual income today!"
    scene ep6_54
    with dissolve
    l "Wait, you're done with the inventory already?"
    mc "Of course! It's me you're talking about here! Hahaha!"
    image llmctabr:
        "ep6_55.jpg"
        pause 3.0
        "ep6_56.jpg"
        pause .2
        repeat
    show llmctabr
    with dissolve
    mc "And I can't let you do it since I know you're pretty tired after that."
    mc "I can already see Miss Jess being over the moon with the report I'll send her later."
    l "Experience really does speak for itself, huh?"
    mc "Yeah, you got that right. Even though you can't always be good with some things, if you just keep on pushing, you'll eventually be able to get the grasp of it."
    mc "And I can see that from you. You've improved a lot in the past few days."
    mc "A great man once said..."
    mc "'A jack of all trades is a master of none, but oftentimes better than a master of one.'"
    l "I think I can agree with you. I don't think I could've handled that many customers on my own if I was still panicking like I used to."
    mc "See? You're getting used to the pressure!"
    l "Your advice was really helpful, [mc]. Thank you."
    mc "Hey, no worries! I'm always happy to help!"
    scene ep6_57
    with dissolve
    l "I've been a little clumsy since I was a kid. Messing things up here and there."
    l "Even though this place isn't much to be proud of, I think I found another place where I belong. *giggles*"
    mc "Another place? You mean... there's another one?"
    l "Ahh... The good old high school days..."
    mc "High school days? Now I'm curious."
    scene ep6_58
    with dissolve
    l "Yep~! I was once a track and field athlete. I don't want to brag, but I was good at it."
    mc "I think you already did, just now, Lily."
    l "Well, a little is fine?"
    stop music fadeout 2
    mc "Haha! Go on. Don't mind me, I'm just pulling your leg."
    l "Jeez..."
    play music 'audio/HeadingNorth.mp3' fadein 2
    scene ep6_59
    with dissolve
    l "Well, I guess... that's what you'd call an innate talent."
    scene ep6_60
    with dissolve
    l "I joined the club for extra-curricular activity. I didn't intend to put all my focus on it. All I wanted was to get an extra grade, nothing more."
    scene ep6_61
    with dissolve
    l "But as soon as I set foot on the track, I felt something in me that I never felt before."
    l "It's weird to say, but my feet felt like they belonged there. That they're meant to be on the track."
    scene ep6_62
    with hpunch
    l "A place where competitors give their all to reach the finish line is where I found my passion."
    scene ep6_63
    with dissolve
    l "It's not flashy compared to the other sports, that's for sure."
    l "But the sound of people cheering for you, the immense pressure when you're at the starting line, the other runners' talents looming over you, and the joy of winning a race."
    l "It all captivated my heart."
    l "After a year, I was already the main runner in the one and two hundred meter dash."
    l "Don't get me wrong, it was tough to get to that position. There were times I almost puked my stomach out because of our coach's intense training."
    l "Even so, I climbed to the top faster than all my other teammates."
    mc "Really? Was it really that tough?"
    l "Yeah, some people see it as a simple sport because all we do is just... well... run. It's not as cool as basketball or soccer, and that's true."
    l "But, that's not all there is to it. The sport is simple, but the training is not."
    l "It's a sport where you have to constantly be better... Better than anyone else..."
    scene ep6_64
    with Dissolve(2.0)
    l "But... I guess that doesn't always happen. Things don't always go the way you wanted it to be."
    scene ep6_65
    with dissolve
    yt "It seems that there's really more to her than meets the eye. I never thought of her as an athlete before."
    yt "I'm curious what happened and why she stopped."
    scene ep6_66
    with dissolve
    mc "What happened though? Why did you stop running?"
    scene ep6_67
    with dissolve
    l "......"
    l "It's... not that I wanted to stop, but..."
    scene ep6_68
    with flash
    $ renpy.pause()
    scene ep6_69
    with dissolve
    $ renpy.pause()
    scene ep6_67
    with flash
    l "Uhm... I think we should just talk about that some other time. I still need to get to the academy as soon as possible."
    mc "Oh right! I forgot about that!"
    mc "Let's close up shop real quick so we can go!"
    scene ep6_71
    with dissolve
    l "Roger that!"
    mc "You're doing the salute wrong..."
    l "Ahaha!"
    mc "Where's Freya, by the way?"
    scene ep6_72
    with dissolve
    l "I think she's still in the restroom trying to change out of the costume she wore earlier."
    mc "Oh, jeez... Well, can you go check on her? She's been in there for quite a while now."
    l "Got it!"
    stop music fadeout 2

    scene black
    with dissolve
    with fade

    play music 'audio/DontShoot.mp3' fadein 2
    scene ep6_73
    with dissolve
    yt "Ahh... What a day that was! At least it's over now. I'll just have to arrive early and prepare myself for tomorrow."
    yt "I've gotta pay Mr. Scott a visit, like I promised Naomi."
    yt "...Oh, right! I have to tell Klara about his situation, too. I just hope he's actually fine."
    scene ep6_74
    with dissolve
    yt "I may get home a bit late than usual, so it might be a good idea to send my report to Miss Jess now."
    yt "It's hard to do it on my phone, but it's better than nothing."
    yt "I bet she'll be happy with the results as soon as she reads the report."
    scene ep6_75
    with wiperight
    j "Good, but that doesn't surprise me at all."
    mc "Eeehhhh......"
    j "Don't get depressed, now, I already expected that to happen. Consider that a trial, and it's good to know that you all survived it."
    mc "So you really did agree to Freya's idea?"
    j "Of course! Why would I reject such a brilliant idea?"
    j "She got a huge fan base, and Freya promoting the burger shack will make a huge impact on its numbers."
    j "So we made a deal that I will let her do her thing while she promotes the business. It's a win-win situation."
    scene ep6_76
    with dissolve
    mc "I see. I have no complaints about it as long as it benefits the shop. I'm pretty sure we'll get used to the amount of customers over time, too."
    j "That's good to hear."
    mc "I just can't believe she came up with that considering her age."
    j "I'd advise you to not take her so lightly, [mc]. She thinks differently from other girls her age."
    j "She's got a good sense for business — that's why I like her in the first place."
    mc "As long as you approved her idea, then I'm cool with it."
    j "By the way, I'm with Klara right now. She wants to talk to you."
    mc "Wait, really? How do you guys know each other?"
    j "It's a bit of a story, so I'll let her explain it to you."
    mc "Alright then."
    scene ep6_77
    with dissolve
    k "[mc]?"
    mc "Hey, Klara! What's going on? Why are you with Miss Jess?"
    k "It's a long story, [mc]. But I'll get to the main points."
    k "She's helping me along with her friend — Aurora — shaping up my company. Kana is with me too, by the way."
    k "Kana was the one who asked them for help."
    mc "So Kana knows her too? Damn... What a small world!"
    k "It looks like it, yes. *giggles*"
    mc "How's everything going, though? All good?"
    k "Things are looking good at the moment, we finished planning our business strategy and have several papers to take care of, so far."
    k "We decided to relax for a while and get back to it tomorrow."
    k "There is still a lot to do, but with their help, I believe we'll get things done faster than what I was expecting."
    mc "I see. That's great to hear. Looking forward to seeing you soon."
    k "Me too, [mc]."
    mc "By the way, I'm on my way to Mr. Scott's house right now. I'll call you once I have time and fill you in about his condition."
    k "Oh! I almost forgot about him!"
    k "Yes, please do, [mc]. And please give him my regards."
    mc "Will do."
    k "Alright, I won't hold you any further. Please, take care and get home early, okay?"
    mc "I might get home a bit late, but I won't stay there for too long."
    k "Great! Goodbye then, [mc]."
    mc "Bye for now."
    stop music fadeout 2
    scene ep6_78
    with dissolve
    k "Thanks."
    play music 'audio/Yearning.mp3' fadein 2
    j "I must say... He's a good man, Klara."
    scene ep6_79
    with dissolve
    k "Mmh... He's not perfect, that's what I certainly know. But he has the ability to have a positive effect on other people's lives."
    k "He may be unaware of it at the moment, but it's just a matter of time until he realizes it himself."
    k "I just hope... My decision to get the girls in there was right."
    j "So, all of that was part of your plan from the beginning?"
    k "Yes, but it was a huge risk for me. I know he'll blame me when he learns that I let the girls stay there on purpose."
    k "But I'll take it. It's for their own good..."
    scene ep6_80
    with dissolve
    k "...and... for Hera too."
    j "A huge sacrifice, huh?"
    j "*chuckles* It seems that I'm not the only person here that educates people. The only difference between us two... is that you sacrifice a lot."
    scene ep6_81
    with dissolve
    k "*giggles* Well, I guess you can say that. But there's no turning back now."
    scene ep6_82
    with dissolve
    j "So, will you fight her or not?"
    k "I will. That's why I came back home. I'm not doing this on a whim."
    k "I will bring Hera to her knees and slap her back to reality. But... everything is up to [mc]."
    j "You and [mc] have exactly the same mentality, you know that?"
    scene ep6_83
    with dissolve
    k "I know that very well. That's why I trust he'll make things right."
    j "You guys know you're against the current boss of the Mafia, right?"
    k "And here I am speaking with her younger sister like it's nothing."
    j "Ah, I don't want to be associated with them. I never stayed with them from the moment I could stand on my own feet anyways."
    k "I know this fight won't be easy, but I will fight with sticks and stones if I have to."
    k "Not just for the kids' sake — this is all for Hera, too."
    scene ep6_84
    with dissolve
    j "*chuckles* Nothing beats friendship at the end of the day."
    j "And that's why I'm here. She can't touch any of you as long as she knows that I'm on your side."
    k "I'm relieved to know that, Jess. Although... there's someone I'm really concerned about right now."
    j "Hm? And who might that be?"
    scene ep6_85
    with dissolve
    k "Nevermind her daughter — I'm more worried about the servant."
    j "Emy? Or should we call her Emma now?"
    k "So that's her real name?"
    j "Yes, every servant has to change their name and profile before they start working for the Mafia. That's to keep things confidential."
    j "They have to follow certain rules by heart, like keeping their emotions under wraps and staying true to their pledge."
    k "I see now..."
    k "I don't know what happened to her and [mc] in the past. But I feel like she's the one suffering the most from all of this."
    k "I want to end this as soon as possible. I can handle it, but I can't take any more of the kids' suffering."
    scene ep6_86
    with dissolve
    j "You have to be patient, Klara. Don't let your feelings get to you. Just focus on the matters at hand right now."
    j "Rushing this won't result in anything."
    scene ep6_87
    with dissolve
    j "......"
    j "And if my theory is correct... then Emma is our key to everything."
    k "What do you mean?"
    j "She's smart. That plan of hers that you told me about last night was perfect."
    k "You mean that she wants [mc] to marry Hera's daughter?"
    j "Yes."
    k "Honestly I was against that plan of hers. I'm just not sure if that will work."
    j "Trust me, it may sound stupid but, that's actually better than what I had in mind, and I think I know what she's planning to do."
    k "Tell me about it."
    j "It has something to do with our family's name."
    j "Considering that [mc] has no standing in society, he's the perfect choice for her plan."
    j "Let [mc] marry Hera's daughter, lay low and attack when the time comes."
    j "Hera leading the Mafia doesn't actually fit with its rules."
    j "Just remember that no woman... can ever lead the group. That's our first and foremost rule."
    j "She must have went through the group's history and found that information."
    k "*gasps* Don't tell me that she wants to..."
    j "Mhm... Break the group for real this time around."
    j "Although, I bet she can't tell him anything at the moment, I know my sister may be the one holding her back. But..."
    j "You'll see when the right time comes. Just leave that part to them."
    j "I will have to prepare a nice bottle of wine for myself when that happens."
    k "Keeping some things mysterious?"
    scene ep6_88
    with dissolve
    j "It's nothing like that. It's just a waste of time to explain it while it's still up in the air. But I have a good feeling that I'm right. We'll just have to watch it unfold."
    scene ep6_89
    with dissolve
    j "If that happens, then it will be a good opportunity for us to strike and do our part."
    j "And prepare yourself. You're making a big decision as [mc]'s guardian."
    k "No, that won't be my decision. It's all up to him, I can't tell him what to do anymore. All I can do is have faith in him."
    j "Well, that's still a theory, but we'll see if I'm actually right."
    k "Alright, then. I trust you, Jess."
    j "Haha! Save that trust for when we get results."
    j "For now, let's wait till Aurora comes back with the good news."
    k "Ah, that's right. Did you two find a good construction company?"
    j "We did. The problem is... how to convince him to join us."
    j "Let's take our time and relax. Tomorrow will be a busy one."
    k "Sure!"
    stop music fadeout 2

    scene black
    with dissolve
    with fade

    play music 'audio/WeekendGetaway.mp3' fadein 2
    scene ep6_90
    with dissolve
    sc "There ya go! Television's all good! What d'ya have next, love?"
    scene ep6_91
    with dissolve
    play sound 'audio/runningfootstepswood.mp3'
    "*running*"
    stop sound
    scene ep6_92
    with dissolve
    n "Huh? What did ya do?"
    sc "This?"
    scene ep6_93
    with dissolve
    n "Oh, come on! For the last time, dad, the doctor and I already told ya, ya have to get some rest!"
    sc "Naaah... Screw that bullshit! I am as fine as I was when I started this job, just look at me, and-"
    n "Nuh-uhh! The doctor may have told ya that yer back is all fine now. But it doesn't mean that ya can lift somethin' heavy already!"
    scene ep6_94
    with dissolve
    n "Ya need to take this seriously, dad! Go get some rest and just leave this to me."
    n "And don't worry about the business, I can handle it on my own, ya know that better than anyone."
    sc "Ya know some parts of it, yes. But ya still have a long way to go before reaching your old man's level, young lady."
    n "Bloody hell, ya know this is..."
    play sound 'audio/doorbell.mp3'
    scene ep6_95
    with dissolve
    "*doorbell rings*"
    n "Hm? Expecting someone today, dad?"
    sc "Nah, that must be your boyfriend, love. Don't be rude, go open the door, would ya?"
    scene ep6_96
    with dissolve
    n "*sighs* Don't go thinkin' this conversation is over, ya just got lucky here."
    scene ep6_97
    with dissolve
    sc "{i}I don't think I could win against her another time. Guess I'll just have to give it up and leave the rest to her. Haha."
    n "Oh! Hey, mate!"
    n "Right, right! I forgot ya mentioned that yah'd be coming here today."
    scene ep6_98
    with dissolve
    sc "Hrm?"
    n "Please, come in! Don't be shy!"
    mc "Thanks, Naomi."
    scene ep6_99
    with dissolve
    sc "Aye! Look who's here! If it ent my boy, [mc]!"
    sc "Please, sit down, lad!"
    scene ep6_100
    with dissolve
    mc "It's been a while, Mr. Scott!"
    sc "Look at how ya've grown!"
    mc "Haha! It's just months since we last saw each other. I haven't grown that much, really."
    mc "How are you doing? All fine now, I guess?"
    scene ep6_101
    with dissolve
    sc "......"
    scene ep6_102
    with dissolve
    n "Don't lie, dad."
    scene ep6_103
    with dissolve
    sc "Ah, well... I'm still recovering. I can at least stand up properly now, unlike a few weeks back where I couldn't even lift my back at all."
    mc "That's great to hear! Although, you should still get some more rest just to be sure."
    mc "Klara was worried about your condition when I told her about you."
    mc "And weeks of recovery isn't that much, to be honest."
    scene ep6_104
    with dissolve
    n "Yeah, tell him 'bout it."
    mc "Huh? Why? What's up?"
    n "Stubborn old man lifted that TV even though the doctor warned him about doin' any heavy work."
    scene ep6_105
    with dissolve
    mc "Come on, Mr. Scott... You should listen to the advice they give you. Nothing's more important than your own health, you know?"
    sc "There, there... Don't gang up on me now, young'uns."
    scene ep6_104
    with dissolve
    n "Why don't ya take a vacation to the countryside for now? Unwind and take yer mind off the business for a while, dad."
    mc "I agree with Naomi there, Mr. Scott. Give yourself some time to chill!"
    scene ep6_106
    with dissolve
    sc "Hmm... Yer right. I kind of miss yer mom already. I might as well do that."
    scene ep6_107
    with hpunch
    sc "*grabs* Now don't go thinkin' of hittin' on my little girl without me knowin', lad!"
    mc "Are you intentionally saying that so Naomi will hear it?"
    scene ep6_108
    with dissolve
    sc "*whispers* But I can't stop ya if ya really want to. I know yer a fine young man and she has been alone for years now. This is yer chance!"
    sc "*whispers* Why don't you show her around the city? She's never been here before I got myself injured."
    mc "Huh? But I thought you didn't want me to hit on her?"
    sc "*whispers* Shh... Keep it down, lad. Ya don't want her to hear us!"
    mc "*whispers* O...kay...? Although I bet she heard all of it, anyway."
    scene ep6_109
    with dissolve
    n "Hmn? What're ya boys talkin' about? Can I join in?"
    mc "No?"
    sc "No!"
    scene ep6_110
    with dissolve
    n "Come on, dad! Just go pack yer bags already!"
    sc "Not yet, love. I need to call yer mom first and let the kids know I'm coming."
    n "What're ya waitin' for then? Go, go! Tell mom I said Hi!"
    scene ep6_111
    with dissolve
    n "Besides... I wanna talk to [mc] for a while."
    scene ep6_112
    with dissolve
    sc "I got'cha, love... I'll be upstairs if you two need me."
    scene ep6_113
    with dissolve
    n "Coffee?"
    mc "Uhh... Sorry, but I have to say no to that for now. I have to wake up early tomorrow and I'm afraid that might keep me up all night."
    n "No worries. I'll be back in a minute."
    mc "Sure, take your time."

    scene black
    with dissolve
    with fade

    scene ep6_114
    with dissolve
    n "Lookin' into the distance, are we?"
    scene ep6_115
    with dissolve
    mc "Hm?"
    n "I'm back. Sorry I took a bit longer. I had to change my clothes from the sweat of workin' all day."
    mc "No prob-"
    mc "Hey, that smells nice!"
    scene ep6_116
    with dissolve
    n "Told ya, you should've taken a cup."
    mc "Nah... Thanks, but I don't want to risk it now that the burger shack is getting busy."
    scene ep6_117
    with dissolve
    n "How about you take some of our coffee beans so you can brew a cup later if you want. They come from mom's coffee plantation out in the countryside."
    mc "You guys have a coffee farm? That's pretty awesome!"
    n "It's not big, but yes, we do sell it there too."
    n "I have no idea if mom's plannin' to export them soon but I can assure ya the quality of it."
    mc "That's one way to advertise a product for sure. Haha!"
    menu:
        "I'll take it":
            $ naomitakecoffee = True
            mc "I'm  not that much of a coffee person, but I definitely know someone who likes it a lot, so I'll take it."
            stop music fadeout 2
            n "I got'cha. I'll get some for ya later then."
            n "Let me sit down so we can talk properly."
        "No, thank you":
            $ naomitakecoffee = False
            mc "I'm not much of a coffee person myself so... probably not right now. But thanks for the offer."
            stop music fadeout 2
            n "I got'cha."
            n "Let me sit down so we can talk properly."

    play music 'audio/TimeTraveling2.mp3' fadein 2
    scene ep6_118
    with dissolve
    n "......"
    yt "Why is she staring at me like..."
    scene ep6_119
    with dissolve
    yt "......"
    yt "Whoa~! I can see her panties! Is she trying to tease me?"
    yt "Nevertheless, she's friggin thicc!"
    scene ep6_120
    with dissolve
    n "Yer eyes sure travel a lot, huh?"
    n "Look up here, Casanova."
    mc "Oh, s-sorry. I didn't mean to look at them."
    n "Don't sweat it. I don't really mind stuff like that. I'm comfortable talkin' to ya like this."
    scene ep6_121
    with dissolve
    n "I just don't want ya to melt lookin' at them. *giggles*"
    scene ep6_120
    with dissolve
    mc "I see...  I thought you were trying to tease me and did that on purpose."
    n "I'm not that kind of person, mate. I can assure ya."
    mc "Ahaha! Got it, got it."
    mc "By the way, you have siblings?"
    n "Yes. There's seven of us in total. I have two older brothers and four younger ones."
    mc "Wait... You're the only girl out of all your siblings?"
    n "Aye, that's why dad can be over-protective sometimes. Although, I don't know what changed his mind so he started to push me to some guys, especially to ya."
    mc "W-what? Why would he do that? And why me?"
    scene ep6_122
    with dissolve
    n "*shrugs*"
    scene ep6_120
    with dissolve
    n "I have no idea. I'm not interested in havin' a commitment, anyways, so I don't pay him any mind."
    n "He says senseless stuff from time to time, please forgive him."
    mc "Oh, trust me. I'm pretty used to it already. He used to joke around with me and Sky a lot when he had something to fix around the house."
    mc "He's basically like a father to us already. It's pretty fun having him around."
    n "Yeah, that sounds like somethin' dad would do, alright."
    image nmhmct:
        "ep6_123.jpg"
        pause 3.0
        "ep6_124.jpg"
        pause .2
        repeat
    show nmhmct
    with dissolve
    n "With all that said... I'm still quite interested in ya."
    n "Let's just say... Ya piqued my interest."
    mc "Hm? Why is that?"
    n "I don't wanna pry too much into yer personal life, and I'm a very straightforward person. So tell me if it's too much."
    mc "Uhh... Sure!"
    n "I got curious ever since Aine and I got to talkin' in her room last time."
    yt "Oh... That's what she meant."
    mc "Aine? What about her?"
    n "She seems a bit troubled about ya and asked me if the two of us are dating."
    mc "Huh? Why would she ask you that?"
    n "D'ya get what she was tryin'a imply on what she said?"
    mc "......"
    mc "Does she... have feelings for me and got jealous?"
    n "Precisely. You can call it slight jealousy. Her attraction might be small or it might be big. Whatever it is, there's definitely something."
    n "Are ya aware about it?"
    mc "No, at least I haven't been."
    yt "...Or I have... She's been asking to give her comfort..."
    yt "But it's too shallow for me to notice anyway..."
    n "I thought so..."
    n "People'd normally never ask about that and just ignore it, especially with someone they just met."
    n "I found it strange that she asked me out of nowhere."
    n "And then, here's you... All in dark about it."
    n "Ya don't have to believe me though. Because who knows? I might be wrong."
    n "That's why I have to ask... What exactly are you two?"
    mc "......"
    mc "*sighs*..."
    mc "It's a long story that would probably take me the rest of the day to explain, but..."
    mc "She was... my bully when we were in high school..."
    scene ep6_125
    with dissolve
    n "Mmh... I see. That's really interesting."
    show nmhmct
    with dissolve
    n "Yer affecting a person's life without ya knowin'. That's why I was intrigued by you and Aine."
    n "I hate seeing a damsel in distress, so all I can say is..."
    n "Pay attention to what's happening around ya from now on, or you'll regret it later. That happened to me, so I know that very well."
    n "Ya honestly don't have to trust me, I'm nothin' but just a concerned fellow."
    yt "Why is everybody trying to make me curious?"
    yt "Although, she's right..."
    yt "I might have been too naive about what's happening around me. I was only thinking of what might benefit me in the long run and ignored all the rest."
    yt "......"
    yt "I never thought that this would come from someone I barely even know. And she managed to grasp all this with only one conversation with Aine?"
    yt "If Aine really does have feelings for me... Then, I honestly don't know what I should do about it."
    yt "I did have feelings for her before, but all of those are gone by now. I abandoned everything when I left high school."
    yt "But why would she fall for me? Because of the comfort I gave her? That's the only reason I can think of right now."
    yt "If that's the case, then she might be unaware of it herself."
    yt "Seeking my comfort is just too shallow of a reason for her to fall for me. I need to know the real reason behind it."
    yt "*sighs*... Another problem added to my list."
    yt "Urrgghhh!"
    scene ep6_126
    with dissolve
    n "*giggles* I'm sorry, mate. Did I give ya a lot to think on? You were in deep thought for a while there."
    mc "To be honest? Yes."
    mc "But you made me realize what was happening, so I don't hold it against you."
    scene ep6_127
    with dissolve
    n "I told ya I'm a straightforward kind of person."
    n "If I have problems with ya, I'll tell ya about it. If I have somethin' to tell ya I'll tell ya right away. I don't like keepin' secrets."
    scene ep6_128
    with dissolve
    n "Whatever you two are goin' through right now, and I don't know if she told you already, but she deeply regrets what she did to you before, mate."
    n "There was no stain of doubt on the way she said it to me."
    n "I'm not forcin' ya, but come on... You two are livin' under the same roof. Make things right before it's too late. Ya ain't kids any longer."
    n "Furthermore, she's quite the looker, don't ya think?"
    scene ep6_129
    with dissolve
    n "*winks*"
    mc "It seems that fixing mechanical things isn't your only expertise, huh?"
    scene ep6_130
    with dissolve
    n "Haha! I don't have it on my CV... yet."
    scene ep6_131
    with dissolve
    n "Although I won't mind ya telling me more about you two next time. I'd love to hear more about yer story."
    mc "*chuckles* We'll see about that."
    n "Lookin' forward to it then."
    if naomitakecoffee:
        n "Please wait here for a moment. I'll go and get some coffee for ya before I forget about it."
        mc "Alright. I have to go home now. It's getting pretty late."
        n "Got it, just give me a second."

        scene black
        with dissolve
        with fade

        scene ep6_132
        with dissolve
        n "Here you go, mate."
        image nmhmct2:
            "ep6_133.jpg"
            pause 3.0
            "ep6_134.jpg"
            pause .2
            repeat
        show nmhmct2
        with dissolve
        mc "Thanks, Naomi."
        n "No worries!"
        mc "Can you go get Mr. Scott for me? I want to say goodbye before I go."
        n "I'm afraid he's gone to sleep. It's weird, but he usually does it at this time of the day."
        n "Don't worry I'll tell him later that you already left."
        mc "Please do."
        mc "Alright, I'm off then. See you, Naomi."
        n "Oh, wait. Give me yer phone for a moment."
        mc "Uhh... sure, here!"
        scene ep6_135
        with dissolve
        n "......"
        show nmhmct2
        with dissolve
        n "There. I saved my phone number to yer contacts. Dad will probably go home tomorrow, so call me, instead, if ya need anythin'."
        mc "Oh, of course!"
        n "Catch'ya later, mate."
        mc "Sure!"
    else:
        n "Please stay here for a moment. I'll go and look in on dad. He's been upstairs for a while now."
        mc "Alright. I have to go home. It's getting pretty late."
        n "Got it, just give me a second."

        scene black
        with dissolve
        with fade

        image nmhmct2:
            "ep6_133.jpg"
            pause 3.0
            "ep6_134.jpg"
            pause .2
            repeat
        show nmhmct2
        with dissolve
        n "He's sleeping. Don't worry I'll tell him later that you left already."
        mc "Please do."
        mc "Alright, I'm off then. See you, Naomi."
        n "Oh, wait. Give me yer phone for moment."
        mc "Uhh... sure, here!"
        scene ep6_135
        with dissolve
        n "......"
        show nmhmct2
        with dissolve
        n "There. I saved my phone number to yer contacts. Dad will probably go home tomorrow, so call me instead if ya need anythin'."
        mc "Oh, of course!"
        n "Catch'ya later, mate."
        mc "Sure!"
    stop music fadeout 2

    scene black
    with Dissolve(2.0)
label naomipause2:
    if _in_replay:
        $ name = persistent.gallery_name
    scene naomipause2
    with dissolve
    $ renpy.pause()
    $ renpy.end_replay()
    play sound 'audio/gamepause.mp3'
    show title at move_slide
    with flash
    $ renpy.notify(imageunlock)
    $ renpy.pause()

    scene black
    with dissolve
    with fade

    play music 'audio/SultansSwing.mp3' fadein 2
    scene ep6_136
    with dissolve
    yt "That was a very short conversation, but damn... she blew me away..."
    yt "Although her sudden interest in me and Aine puts me off a little bit. Why was she so interested to know our story?"
    yt "But I like that she's soft-spoken and very easy to talk to."
    yt "That's probably what got me to tell her some information about us."
    yt "She has the most soothing voice I've ever heard — like it would put me to sleep."
    scene ep6_137
    with dissolve
    yt "She sounds like someone who would be doing audio books for a living, to be honest. Haha!"
    scene ep6_138
    with dissolve
    yt "......"
    yt "Hey, is that Emma?"
    yt "...Yeah, of course it's her. She has the weirdest detective outfit I've ever seen."
    yt "I wonder what she's doing..."
    scene ep6_139
    with dissolve
    mc "Yow, Sherlock! What's up?"
    e "Nothing. I'm just on my way home. And please don't call me Sherlock."
    mc "Bummer..."
    mc "What's that?"
    e "...It's about the case I'm currently assigned to. Why?"
    mc "Let me guess..."
    mc "Some creepy stuff?"
    e "Why, are you really into something creepy? You asked me that before too."
    scene ep6_140
    with dissolve
    e "The inside details are confidential but, yes. It's more than just something creepy."
    e "A guy reported that he found his wife murdered after he came home from his day job."
    mc "Uhm... Is that all?"
    scene ep6_141
    with dissolve
    e "No, it's not just any type of murder, his wife was so torn apart that he could barely even recognize her."
    mc "Oh, shit!"
    scene ep6_142
    with dissolve
    e "Mhm... The crime was so gruesome that police couldn't find a single piece of evidence or any leads, so the investigation was passed over to our department."
    e "I'm making a list of the evidence I found earlier and the details of the crime. I'm interrogating the suspect tomorrow."
    mc "Heeh... So, who's the suspect?"
    e "The man who reported the crime -- her husband..."
    scene ep6_143
    with dissolve
    mc "What the..."
    mc "How were you able to tell that it was him?"
    e "It was easy..."
    e "The way he spoke to me was already suspicious to begin with."
    e "He took time to think about his answers and kept repeating the same phrases while his eyes never looked straight at me."
    e "His fingers fidgeted whenever I asked him some questions related to the crime. That's  basic psychology to determine if a person is lying or not."
    yt "Holy shit! I should be careful of her from now on! She'll easily be able to tell whenever I lie!"
    e "Knowing that he was lying to me, I asked him to remove the gloves he was wearing."
    mc "Huh? I don't get the logic behind it. Why his gloves?"
    e "At least let me finish first..."
    mc "Okay... Miss Inspector..."
    e "I found a small cut in his lips so I was assuming that his wife tried to fight back somehow. When he removed his gloves, there was some bruising and small cuts on his hands."
    mc "So you were right to assume that they fought before he was actually able to kill her, then?"
    e "Mhm..."
    e "But that alone can't prove that he's guilty, so I'm going to make him tell me the truth tomorrow."
    mc "That sounds tough! What will you do if he denies it anyway?"
    e "I have my ways. That's what I'm trained to do."
    mc "I got it. Good luck with that then."
    e "Mhm..."
    image emcmtouts:
        "ep6_144.jpg"
        pause 3.0
        "ep6_145.jpg"
        pause .2
        repeat
    show emcmtouts
    with dissolve
    yt "She sure did talk a lot, didn't she? I could sense her passion and a bit of emotion when she was talking about it."
    yt "I would usually be shocked if she did something I don't expect, like her smiling earlier, but..."
    yt "...it's different this time. It makes me happy that I could almost... smile?"
    yt "I want to test something..."
    mc "By the way, don't you really want to celebrate your birthday? I mean... I practically don't do it anymore because I find myself too old for it."
    mc "But you're still young, you know? We can tell everybody about it-"
    e "I'm just two years younger than you, I'm not a kid any longer."
    yt "And there goes the usual argument..."
    yt "Yeah, we've argued a lot, but... there's something about it. Something I can't put my fingers on."
    yt "Ever since I saw her express some emotion when they first moved in the house, I felt a relief that I couldn't understand."
    yt "I know that I literally should've been angry back then, but I don't understand why I felt so calm. I couldn't take my mind off of it, that was the reason why I couldn't sleep."
    if naomitakecoffee:
        mc "*sighs*..."
        scene ep6_146
        with dissolve
        mc "Well... At least take this then."
        e "Hm? What is this?"
        mc "Coffee beans. I know you like coffee, since it was almost the only thing you drank during high school to the point that I don't know if you know what water or juice is."
        e "......"
        $ emmapoint += 1
        $ renpy.notify(emmanotif)
        scene ep6_147
        with dissolve
        e "Thanks... but I do drink water and juices, too."
        mc "*sighs*..."
        mc "Well... I won't force you if you really don't want to celebrate it."
        e "......"
        e "I thought that argument was already over?"
        mc "Ah, jeez... Just... Nevermind..."
    else:
        mc "*sighs*..."
        mc "Well... I won't force you if you really don't want to."
    stop music fadeout 2

    scene black
    with dissolve
    with fade

    play music 'audio/TryingToBeOkay.mp3' fadein 2
    scene ep6_148
    with dissolve
    mc "Ahh... Finally, home sweet home."
    scene ep6_149
    with dissolve
    mc "I wonder if everyone is busy at-"
    scene ep6_150
    with hpunch
    ev "HAPPY BIRTHDAY, EMMA~!!"
    mc "Whoa~! "
    e "Ah..."
    g "Wohooooo! Yeeaahh~!!"
    yt "How is she drunk already?"
    scene ep6_151
    with dissolve
    mc "Well? You don't have any choice now, do you?"
    e "......"
    scene ep6_152
    with dissolve
    g "Heheee~! You cheeky little girl, I almost forgot it's your birthday today, Em!"
    scene ep6_153
    with dissolve
    g "Come and give big sister a kiss, will you?"
    e "E-eek! You reek of alcohol, Gwen!"
    g "Oh, come on! Why does it matter?"
    scene ep6_154
    with dissolve
    g "We'll drink all night long, baby~! Wahahaha!"
    e "Awww~! Get away from me~!"
    mc "*thumps*"
    mc "......"
    yt "...What the heck was that just now?"
    scene ep6_155
    with dissolve
    s "You look so dumbfounded, [mc]. Don't tell me you got surprised too?"
    mc "To be honest? Yeah, I was surprised. I knew it was her birthday, but she told me she doesn't celebrate it. So I wasn't expecting this at all."
    scene ep6_156
    with dissolve
    s "It was all Aine's idea. She told me that Emma stopped celebrating her birthday after her mom died. So I just couldn't say no to it."
    scene ep6_157
    with dissolve
    yt "Her mom... died? So that's what she was about to tell me earlier..."
    scene ep6_158
    with dissolve
    s "I hope you're fine with it, [mc]."
    mc "Well, if you're chill with it, then I'm cool."
    scene ep6_159
    with dissolve
    mc "And besides..."
    s "Hm? What is it?"
    mc "......"
    scene ep6_160
    with dissolve
    mc "Ah... Don't mind me."
    image embskytmc:
        "ep6_161.jpg"
        pause 3.0
        "ep6_162.jpg"
        pause .2
        repeat
    show embskytmc
    with dissolve
    mc "By the way... Were you the one who made that cake?"
    s "No, Aine made it herself. I lent her some of Mom's recipe books and she baked it all by herself."
    s "I volunteered to decorate the kitchen though. *giggles*"
    mc "Heeh... So you guys are planning to go all out tonight, huh?"
    s "Why not? We never got to do parties inside the house before."
    s "Plus, it's quite a special day for Emma. We need to go all out. *giggles*"
    mc "*lightly chuckles* You have a point."
    scene ep6_163
    with dissolve
    a "Sorry to surprise you like this, Em."
    a "I figured now that we're here, we should start to celebrate your birthdays again from now on."
    scene ep6_164
    with dissolve
    e "Mhh-nhh... It's fine. I'm really happy that you made all this for me."
    scene ep6_165
    with dissolve
    e "So, thank you, Aine."
    scene ep6_166
    with hpunch
    e "*sniffs* Thank you... Thank you..."
    a "Aww... Please stand up, Em..."
    yt "Is this... really Emma I'm seeing right now? Call me an idiot for repeating it, but she just keeps on surprising me."
    scene ep6_167
    with dissolve
    mc "Hey, isn't it supposed to be a happy day for you? Come on, stand up and wipe those tears off."
    scene ep6_168
    with dissolve
    e "......"
    scene ep6_169
    with dissolve
    e "Mhm~!"
    e "I'm sorry for that."
    mc "*thumps*"
    yt "There it is again... Why the heck am I getting this feeling from her...?"
    yt "She just nodded, I know... But why does it resonate with me like this?"
    yt "She's... just a girl who thinks about nothing but Aine's welfare... right?"
    yt "Was she actually this fragile?"
    scene ep6_170
    with dissolve
    g "Sheeesh...! What are you getting all teary for? Make a wish and blow your candle now, Em!"
    e "Ah, right. I almost forgot."
    scene ep6_171
    with dissolve
    a "Take your time."
    scene ep6_172
    with dissolve
    e "{i}It's not bad to wish for it twice, right?"
    e "......"
    e ".........."
    scene ep6_173
    with dissolve
    e "*blows*..."
    scene ep6_174
    with dissolve
    $ renpy.pause()
    scene ep6_175
    with dissolve
    $ renpy.pause()
    scene ep6_176
    with dissolve
    g "Hahaaa! So what's your wish, Em?"
    e "It's a secret."
    scene ep6_177
    with dissolve
    g "Gaaah! You and [mc] are practically the same! You're both bummers!"
    mc "I'm totally not like her, you know?"
    scene ep6_178
    with dissolve
    s "Come, Emma. Let's go to the kitchen."
    e "Mhm..."

    scene black
    with dissolve
    with fadeq

    scene ep6_179
    with dissolve
    s "Tadaaaa~!"
    yt "Haha! She's so cute."
    scene ep6_180
    with dissolve
    s "Do you like it?"
    e "Yeah, I like it. It's simple but I can see a lot of effort went into setting this up. Did you do all of this?"
    s "Yup! Aine was busy baking your cake, so I was the one in charge of the decorations! "
    e "Thank you, Sky. I appreciate it."
    s "You're welcome! It's your birthday, after all!"
    scene ep6_181
    with dissolve
    a "Shall we eat?"
    mc "Yeah, I'm quite hungry. But I think I should change my clothes before eating. These are drenched in sweat."
    e "Me too."
    e "And you should stop Gwen from guzzling all the wine or we will run out of drinks later."
    scene ep6_182
    with dissolve
    a "Huh?"
    scene ep6_183
    with dissolve
    a "*gasps*!"
    a "Gwen, could you please stop drinking?! It's still too early for you to be drunk!"
    scene ep6_184
    with dissolve
    g "Gahaaahh~! But that's some good bottles of wine you bought, Aine. I'm sure they cost some pretty good penny?"
    a "They are! So, leave some for the others!"
    scene ep6_185
    with dissolve
    g "Meehh... We have some beers in the fridge too, they can just drink those."
    a "That's not how it works, you drunkard!"

    scene black
    with dissolve
    with fadeq

    scene ep6_186
    with dissolve
    $ renpy.pause()
    scene ep6_187
    with dissolve
    $ renpy.pause()
    scene ep6_188
    with dissolve
    $ renpy.pause()
    scene ep6_189
    with dissolve
    $ renpy.pause()

    scene black
    with dissolve
    with fadeq

    scene ep6_190
    with dissolve
    yt "*deeply sighs*..."
    yt "Well? They're all dead to the world... They really went all out."
    yt "It looks like I'm in charge of cleaning up this mess, huh?"
    scene ep6_191
    with dissolve
    yt "Hng..."
    scene ep6_192
    with dissolve
    yt "Ahh..."
    yt "Let's take the girls to their rooms first."

    scene black
    with dissolve
    with fadeq

    scene ep6_193
    with dissolve
    yt "Well? This is a first... She never got this drunk before."
    yt "We used to enjoy a couple of beers on our own, but not as much as this evening."
    yt "I guess she's just enjoying the moment now that there's people here besides us."
    yt "Luckily, I didn't drink much because I knew this was going to happen..."
    yt "*lightly chuckles*"

    scene black
    with dissolve
    with fadeq

    if skyroute:
        scene ep6_194
        with dissolve
        yt "There you go!"
        yt "Man... She's just the cutest thing! It's like she's too good for this world. Haha!"
        yt "I've gotta spend some time with her later. I haven't talked to her much since she got too busy with her work."
        yt "......"
        yt "Alright, onto the damsels in distress!"
    else:
        scene ep6_194
        with dissolve
        yt "There you go!"
        yt "......"
        yt "Alright, onto the damsels in distress!"

    scene black
    with dissolve
    with fade

    if gwenstartdate:
        scene ep6_195
        with dissolve
        yt "Let's get you in first, my lady."
        yt "Time for you to get some rest."

        scene black
        with dissolve
        with fadeq

        scene ep6_196
        with dissolve
        yt "......"
        yt "She's sleeping so soundly... This is actually the first time I've watched her sleep, isn't it?"
        yt "The contrast between her usual personality and how different she is while sleeping really brings a smile to my face."
        yt "I could never get bored being with her."
        menu:
            with dissolve
            "Kiss her":
                scene ep6_197
                with dissolve
                mc "*kisses*"
                mc "Good night, Gwen. I love you."
                scene ep6_198
                with dissolve
                g "Mnhh... [mc]... One more round, please..."
                yt "Jesus... This girl."
            "Let her be":
                mc "Good night, Gwen."
    else:
        scene ep6_195
        with dissolve
        yt "Let's get this drunkard up first."
        scene ep6_196
        with dissolve
        mc "Good night, Gwen."

    scene black
    with dissolve
    with fade

    scene ep6_199
    with dissolve
    yt "You're up next, Ice-Queen... Or maybe not anymore."
    yt "I can't believe that I would actually be carrying her."
    yt "Who would've thought that what happened in that past would lead to something like this?"

    scene black
    with dissolve
    with fadeq

    scene ep6_200
    with dissolve
    yt "Thinking about my conversation with Naomi now... I've got a lot of stuff to learn about her."
    yt "The reason why she has feelings for me is the main thing. Although I can't be sure that she really has something for me yet."
    yt "Maybe Naomi and I were just reading too much into it."
    yt "I gotta find a way to know what she's exactly got for me."
    scene ep6_201
    with dissolve
    mc "Alright. Sleep well, Aine."
    if ainepoint == 9:
        scene ep6_202
        with dissolve
        a "Mhhnnn~!"
        scene ep6_203
        with dissolve
        $ renpy.pause(0.5)
        scene ep6_204
        with dissolve
        yt "How in the world was she able to find my hand while sleeping?!"
        mc "Sorry, Aine. I can't stay here. I still need to get Emma up here."
        a "Mhhhnnnn~!"
        mc "Okay, okay! I'll give you a head pat tomorrow if you want, just let me go."
        mc "Although, I don't know if you can hear me or not..."

    scene black
    with dissolve
    with fade

    scene ep6_205
    with dissolve
    yt "Holy Mary, Mother of Christ! This girl is heavy as fuck!"
    yt "Where the heck is she getting all her weight from? Her boob size?!"
    scene ep6_206
    with dissolve
    yt "But I would never tell her that... She's a detective and she probably knows some fighting techniques. I'd be dead if that's the case."
    yt "Might as well avoid getting on her nerves."
    yt "How can someone just become another person's servant, though? They said it was a tradition, but where did she get the resolve to commit herself to that?"
    yt "I feel like she intentionally gave her own freedom away."
    yt "She's really weird..."
    yt "Oftentimes, she's all emotionless and talks like a robot. But there are times where her emotions burst out of her like what happened earlier."
    yt "Just which one is the real Emma? And why do I feel like melting when she's smiling, especially when that smile is directed at me."
    yt "Ahh! What did I get myself into?! All these things happening right before my eyes confuse me and stir up my shit!"
    yt "*sighs*..."
    yt "I'll just carry her to her bed so I can get some rest too."

    scene black
    with dissolve
    with fadeq

    scene ep6_207
    with dissolve
    yt "Jeez... I only carried the four of them up here and I'm already feeling my arms."
    yt "I should start doing basic workouts soon. I have been neglecting my body for quite some time now."
    yt "......"
    yt "She's been holding on to my shirt ever since we entered the room."
    yt "Oh well... Let's just put her down."
    scene ep6_208
    with dissolve
    mc "Hey, are you a crab or something? Let go of my-"
    scene ep6_209
    with dissolve
    "*kisses*"
    scene ep6_210
    with dissolve
    mc "...!!!"
    scene ep6_211
    with dissolve
    mc "......"
    yt "Her lips... are so..."
    scene ep6_212
    with dissolve
    mc "Mmp!"
    scene ep6_213
    with dissolve
    mc "*inhales deeply*"
    scene ep6_214
    with dissolve
    yt "No, no, no! Why does it feel good to have her kiss me?!"
    yt "She's just-"
    scene ep6_215
    with dissolve
    e "Mnh... [mc]... I miss... y..."
    yt "Huh?!"
    yt "What did she just... Was she about to say that she missed me?!"
    yt "But why?!"
    yt "She's asleep so she could be dreaming! There's no reason for her to miss me! Or..."
    yt "......."
    scene ep6_216
    with dissolve
    yt "Arrrgghh! I don't know what's happening anymore! I'm about to go crazy!"
    stop music fadeout 2

    scene black
    with dissolve
    with fadeq

    "After cleaning..."

    scene black
    with dissolve
    with fadeq

    play music 'audio/SultansSwing.mp3' fadein 2
    scene ep6_217
    with dissolve
    yt "Come on, man...! I already have so many problems and now Emma just added a whole ton of questions into my head!"
    yt "I need to get my mind off all of this shit! At least for now..."
    scene ep6_218
    with dissolve
    yt "What should I do then?"
    yt "Play games?"
    yt "Nahh... It's already past nine, I can't risk it."
    scene ep6_38
    with flash
    yt "......"
    scene ep6_219
    with flash
    yt "Oh, right! Freya!"
    yt "Maybe I should check her Twitter profile."
    yt "......"
    yt "Uhh.... What was her username again?"
    yt "{b}@flatoverfat{/b}, right?"
    yt "Damn, girl... Is that your life motto or what?"
    scene ep6_220
    with dissolve
    yt "......"
    yt "So her name's 'Freya-chan', huh? Isn't it kind of... ordinary for someone who streams games?"
    yt "I wonder how many followers she has... I bet it's not-"
    scene ep6_221
    with dissolve
    yt "Holy Jesus! Two hundred thousand?!"
    yt "That's friggin' a lot! How long has she been doing this?!"
    yt "This girl is basically famous!"
    scene ep6_222
    with dissolve
    yt "No wonder she attracted so many customers earlier. Most of them are probably her fans."
    yt "It's kind of a weird way to promote a burger shack, but it works, nonetheless."
    yt "And she thought of that idea, right? No wonder Miss Jess didn't hesitate to let her work there."
    yt "Well, I should stop doubting her, now that I saw her real potential."
    scene ep6_223
    with dissolve
    yt "......"
    yt "This might be the picture she took before she went out and called for customers."
    yt "......"
    yt "Huh...?"
    yt "Good lord! Now that I've taken a good look at her..."
    yt "She wasn't wearing a bra earlier!"
    yt "How can this girl be so daring?"
    yt "It speaks to her personality, but that sure surprised me! Does her sister know that she's doing this?"
    yt "One wrong move, and she'll accidentally expose her nipples!"
    if freyapoint == 5:
        scene ep6_224
        with dissolve
        yt "......"
        yt "...I couldn't help but think about it now..."
        yt "Well? I must say... Way to go, chopping board! AHAHAHA!"
        yt "She may not be blessed like Emma who's got earth-sized tits, but heck, that sure is sexy, even if it's just my imagination."
        scene ep6_223
        with dissolve

    yt "The costume still suits her quite well though! All hail Neko Paradise! Haha!"
    yt "Should I give it a Like?"
    menu:
        "Give it a Like":
            $ freyaselfielike = True
            yt "Yep! There you go!"
        "No, don't bother":
            $ freyaselfielike = False
            yt "Probably not right now..."

    scene ep6_225
    with dissolve
    yt "But fuck me... This selfie of her got more than a hundred thousand likes! That's basically half of her fanbase!"
    yt "This girl is a monster! She'll become a celebrity in no time if she keeps this up!"
    "*phone vibrates*"
    yt "Hm? A message from an unknown number?"
    f "(Howdy, [mc]! Good evening! This is Frey!)"
    f "(Are you still up? Can I call?)"
    yt "Oh, it's our very own burger shack mascot!"
    yt "You know what? Let me just call her instead."
    scene ep6_226
    with dissolve
    mc "............"
    mc "Hey, Freya. You're pretty late."
    f "Yeah, sorry about this. I just finished today's class with my teacher. I'm taking night classes since I'm working during the day."
    mc "Oh, I see... It's good that you know how to manage your time properly."
    f "Pff... I hate studying, but I got no choice. Things are about to get messy since the exams are coming."
    yt "Seems like everyone who still studies is getting busy, huh? Lily is a bit worried about her upcoming exam, too."
    scene ep6_227
    with dissolve
    mc "Studies first, of course. That's the most important thing for you to focus on right now."
    f "Come on! Don't you be like sis, too! She keeps on bugging me about it! Like... almost every day!"
    scene ep6_228
    with dissolve
    mc "Haha! She's your sister, what do you expect?"
    f "Speaking of sis, I was trying to call her just before I called you, she was not answering, and her phone just kept on ringing."
    f "She usually waits for my call before going to bed. What happened? Is she asleep now?"
    scene ep6_229
    with dissolve
    mc "More than just asleep, I think."
    f "Huh?"
    mc "Do you know it's Emma's birthday today?"
    f "Yep! I sent her a message early this morning. What about it?"
    mc "Well... They celebrated it here and everybody got drunk as fuck. Including her..."
    f "Heeh... So Emma-Chan celebrated her birthday again, huh? That's good to know!"
    mc "It was your sister's idea though, Emma didn't actually want to celebrate it at first."
    f "That's good, that's good! They could both be truly happy, at least for a day."
    mc "They really went all out, that's for sure."
    f "Yeah, don't believe them when they tell you they don't like alcohol. Gwenny influenced them real bad. Haha!"
    mc "I think that might be the case."
    f "How about you? You seem pretty fine to me!"
    mc "I'm a bit tipsy, but I'm still cool."
    mc "I figured they would be drunk later on, so I held back my glasses, and I wasn't wrong."
    f "A fine young gentleman, I see...! Don't go thinking of doing something to them now!"
    mc "Well? I'm a guy. But I'm not that kind of guy, at the very least. Haha!"
    f "Good, good!"
    f "I know you guys are not on very good terms, but please take care of them, [mc]."
    mc "Just like what your sister told me to do for you. Haha!"
    mc "You don't have to worry about them, to be honest. They know what they're doing as far as I can see."
    f "Well, just in case, you know?"
    scene ep6_230
    with dissolve
    mc "*lightly chuckles* We'll see, we'll see..."
    scene ep6_229
    with dissolve
    mc "Anyway, enough about us here. I just checked your Twitter profile and damn... I didn't know you're pretty famous!"
    mc "How long have you been doing it?"
    if freyaselfielike:
        f "Oh, yeah. I saw you liked the picture I took earlier, that's why I called."
    else:
        f "Oh yeah?"

    f "I think it's more than a year now."
    f "And I'm not really that famous locally. Eighty percent of my followers are international."
    f "I still have a lot of solid fans in the city though."
    mc "Jeez... Twenty percent is still big! Does your sister know about it? Or your mom?"
    f "Sis knows about it, but not mom. She's a boomer, I'm pretty sure she doesn't even have any social media accounts."
    mc "I see... What does Aine think about it, then?"
    f "Hmm... She wasn't into the idea at the start. But she eventually accepted it, thinking that she won't be able to stop me anyways. Haha!"
    f "She's pretty conservative to begin with, so I understand her."
    f "But dude... It's the 21st century! Things like cosplay and streaming are pretty common these days!"
    mc "Yeah, I know. As long as you're passionate and not doing it for the sake of popularity and money, then you'll be fine."
    f "We all need money, but yeah... I really love doing this."
    f "I actually need to learn how to sew my own costumes though. Mom's seamstress is retiring soon."
    mc "Huh... Can't you buy them instead?"
    f "Costumes are really expensive, especially those detailed ones. I can't spend my money on those just yet, I'm saving my income for college."
    mc "I guess you were not lying about being independent, after all."
    f "Yeah, I don't like asking for money from anybody. Especially mom, I gotta earn it by myself."
    menu:
        "I'm starting to like...":
            mc "Haha! I'm actually starting to like the way you think. You're really efficient and optimistic."
            $ freyapoint += 1
            $ renpy.notify(freyanotif)
        "It's good...":
            mc "Haha! It's good that you're thinking like that. You're pretty efficient and optimistic."

    f "Thanks! Although I'm not that confident when it comes to studying. I still hate it, but I got no choice but to do it."
    mc "Just stay positive, it will eventually come to an end. And hopefully, it'll be a good one."
    f "*giggles* It's good that you're not like sis or Emma-Chan, they're both always full of negativities!"
    mc "Can you blame them though?"
    f "That's the big question. Haha!"
    if freyapoint == 6:
        f "Anyway, I'm not going to stay up for long. I just wanted to check how sis was doing."
        f "But I want to ask your opinion about my new costume before I go."
        scene ep6_231
        with dissolve
        mc "You mean the one you used in the shop?"
        f "Yep! That one! I wanted to ask you earlier, but we were too busy."
        f "My fans are just a bunch of horn dogs, I just want a guy's honest opinion about it."
        f "And sis will just tell me it's good as usual anyways, so I won't bother asking her again."
        mc "Uhh... Okay..."
        f "Let me send you some selfies!"
        mc "Wait, you're already wearing it?"
        f "Yep, hold on!"
        yt "I already saw it earlier, why does she have to send me another selfie?"
        f "Okay, you ready? Turn on your phone speaker, by the way."
        mc "Sure..."
        scene ep6_232
        with dissolve
        mc "There, hit me with it!"
        f "Sending..."
        scene ep6_233
        with dissolve
        $ renpy.pause()
        mc "......"
        scene ep6_234
        with dissolve
        mc "Whoa~! What the heck is this?!"
        f "AHAHAHA! Good night, [mc]~! Have a nice sleep! Byeeeee~!"
        mc "Hey, hey, wait!"
        "*click*"
        mc "......"
        yt "What the heck was she thinking sending me that?!"
    else:
        f "Anyway, I'm not going to stay up for long. I just wanted to check how sis was doing."
        mc "Alright, have a good one then."
        f "You too! Good night!"
    stop music fadeout 2

    scene black
    with dissolve
    with fade

    play music 'audio/Boxes.mp3' fadein 1
    scene ep6_235
    with dissolve
    $ renpy.pause()
    scene ep6_236
    with dissolve
    m "Hm?"
    scene ep6_237
    with dissolve
    m "Hey, what are you doing outside in that outfit? Where to?"
    un "......"
    un "I'll be on duty for a while. You take care of the house."
    m "You don't have to tell me that. It's my headquarters after all."
    un "You know you're not in the military anymore, right? I still can't get why you're making simple things weird."
    m "Speak for yourself, old hag."
    un "I told you to not call me that. I'm just two years older than you."
    m "So...?"
    un "......"
    scene ep6_238
    with dissolve
    un "Here's some money for this month's bills. The rest is all yours."
    m "...Thanks, but there's a lot in here. What do you want me to do this time?"
    scene ep6_239
    with dissolve
    un "Not much. I need you to watch someone for me."
    m "You mean I gotta stick with him or her? I still have college, you know?"
    un "Just do it if you have time. Give me updates with his status and that's it. I might tell you to do something aside from that, just be ready."
    un "This is not me asking you, it's an order from my boss and I need your help."
    scene ep6_240
    with dissolve
    m "Yeah, I can do that. I assume you don't have the details yet?"
    un "Not yet, I'll call you once I get all the information. Be sure to un-silence your phone."
    m "No worries."
    un "Help uncle in his ramen shop in my place. I won't be coming back any time soon."
    un "Tell him I'll be away for a while too."
    m "Can't you just do that yourself?"
    un "He's busy with the customers right now, I can't disturb him."
    m "Well, alright... If that's what you want."
    un "How's college going? You're not squandering all the money I'm giving you for some useless trash, right?"
    scene ep6_241
    with dissolve
    m "It's fine, you saw my report card last time. And no, I still have half of what you gave me. I know how to value my cash, unlike you."
    un "Good."
    un "Don't follow in my footsteps if you can. Don't use what I taught you for something personal, you got that?"
    scene ep6_242
    with dissolve
    m "Birds of a feather may flock together, but I'm totally not like you. Don't worry about that."
    m "How about your family? Aren't you worried about them?"
    scene ep6_243
    with dissolve
    un "......"
    un "Such as they are to me. I'm not worthy of being one of them any longer."
    m "Aren't you still their leader or whatever?"
    scene ep6_244
    with dissolve
    un "I still am. But I'd rather not consider myself in that status now that I found the right path to take."
    m "And that's to work under your current boss? You sure like to think weird."
    stop music fadeout 2
    un "You're not supposed to tell me that when you're actually the same."
    play sound 'audio/jesscarroar.mp3'
    play music 'audio/Caution.mp3'
    scene ep6_245
    with dissolve
    $ renpy.pause()
    scene ep6_246
    with dissolve
    un "I need to go. Remember what I told you."
    m "Sure. Take care."
    scene ep6_247
    with dissolve
    play sound 'audio/cardoorclose.mp3'
    "*car door closes*"
    j "......"
    j "It's been a while, Owl."
    scene ep6_248
    with dissolve
    j "Or should I just call you... Claire?"
    scene ep6_249
    with dissolve
    $ renpy.pause()
    scene ep6_250
    with dissolve
    $ renpy.pause()
    scene ep6_251
    with dissolve
    cl "You're close to me, so call me by my name. I'm no longer worthy of that stupid nickname. It makes me so sick that I want to throw up."
    scene ep6_247
    with dissolve
    j "Still as ruthless as ever. Just like your friend."
    cl "*chuckles* I never considered her a friend to begin with."
    j "Well, you're fine as you are now though. Good job on the recovery."
    cl "Thanks."
    j "...Was Fang your sister, by the way? I don't recall you having a little sister."
    scene ep6_251
    with dissolve
    cl "She's not. Although, she's worthy to be called my sister at this point."
    cl "She found me when I had nowhere to go. Her uncle happily took me in, too. I owe my life to them."
    j "Is that the reason why you don't want to go back to your family?"
    scene ep6_252
    with dissolve
    cl "......"
    j "......"
    j "Alright, I'll just avoid that topic from now on."
    scene ep6_253
    with dissolve
    cl "Thank you."
    scene ep6_251
    with dissolve
    cl "So, where's our destination?"
    j "Her apartment."
    j "Well, I'm staying with her until Aurora comes back. So you'll be our bodyguard for now."
    cl "Why did you choose me instead of {b}my friend{/b}? She's way more efficient than me, and you know that."
    scene ep6_247
    with dissolve
    j "She rejected my offer. She's not the type to get involved with this kind of issue."
    j "And if we're talking about skill, it's a no-brainer to choose you. I'm fully aware of what you're capable of doing by now."
    j "We'll be careful of your triggers, so we'll lay low until the right time comes."
    j "And I don't think this will come down to spilling any blood down the road, but just to be sure, we need you by our side."
    scene ep6_253
    with dissolve
    cl "I can at least hold back now, unlike before. So don't worry."
    j "I'm relieved to hear that."
    scene ep6_251
    with dissolve
    cl "What's happening though? You haven't filled me in about the situation, yet."
    cl "Are you and your sister in a love quarrel or what?"
    j "It's not between us two, but I at least want to help someone who's not on good terms with her."
    cl "I see..."
    cl "What happened to them, then? Is your sister bearing a grudge against them?"
    j "You got that right. I'll tell you the full story as we travel."
    j "Fasten your seatbelt and hang on tight, will you?"
    scene ep6_253
    with dissolve
    cl "*chuckles* Who do you think I am? Go full speed if you want."
    j "You asked for it."
    stop music fadeout 2

    scene black
    with dissolve
    with fadeq

    "Monday morning..."

    scene black
    with dissolve
    with fadeq

    play music 'audio/Ocean.mp3'
    scene ep6_254
    with dissolve
    mc "95..."
    scene ep6_255
    with dissolve
    $ renpy.pause()
    scene ep6_254
    with dissolve
    mc "96..."
    scene ep6_255
    with dissolve
    $ renpy.pause()
    scene ep6_254
    with dissolve
    mc "97..."
    scene ep6_255
    with dissolve
    $ renpy.pause()
    scene ep6_254
    with dissolve
    mc "98..."
    scene ep6_255
    with dissolve
    $ renpy.pause()
    scene ep6_254
    with dissolve
    mc "99..."
    scene ep6_255
    with dissolve
    $ renpy.pause()
    scene ep6_254
    with dissolve
    mc "100......"
    scene ep6_256
    with dissolve
    mc "Phew~!"
    yt "Damn...! That took me a while to finish a single round! I should do this more from now on or I'll get out of shape."
    yt "Too bad I can't go out and run now that I have to go to work so early."
    if gwenstartdate:
        scene ep6_257
        with dissolve
        yt "I'll try and ask Gwen if she wants to go to the Gym later this weekend."
        yt "I remember her asking me if I wanted to go with her last time. I could use some good time on a treadmill."
        yt "That would be an opportunity to spend more time with her too..."
        yt "...Yeah, I should do that..."
        scene ep6_258
        with dissolve
        yt "A date at the Gym, huh?"
        yt "That doesn't sound so bad. Haha!"

    scene ep6_259
    with dissolve
    play sound 'audio/doorknock.mp3'
    "*knocks*..."
    mc "Hm?"
    mc "Yes? Who is it?"
    a "Oh, you're awake already? Thank god~!"
    a "It's me, Aine. Can I come in for a moment?"
    mc "Uhmm... Yeah, sure. But I have to put on a shirt..."
    scene ep6_260
    with dissolve
    play sound 'audio/opendoor.mp3'
    "*door opens*"
    scene ep6_261
    with dissolve
    a "*gasps*!"
    mc "...first..."
    scene ep6_262
    with dissolve
    a "Oh, uhm... I'm sorry. I should've just waited outside instead."
    mc "Well, you're in here now anyway. Just hold on, let me get a shirt."
    if ainepoint == 9:
        scene ep6_263
        with dissolve
        a "......"
        scene ep6_264
        with dissolve
        a "{i}Oh, wow... Now that I'm seeing his body, he's actually very fit!"
        a "{i}Just look at all those muscles..."
        a "{i}...in the right places."
        a "{i}I bet he's..."
        scene ep6_265
        with flash
        f "{i}Yeah, it's common knowledge that if a guy is ripped, his thing underneath is pretty jacked up too!"
        scene ep6_266
        with flash
        a "{i}If what Freya said last time was true, then... he's probably..."
        scene ep6_267
        with dissolve
        a "{i}*gulps*"
        scene ep6_268
        with dissolve
        a "{i}Wait! No, no, no! What am I thinking?! I shouldn't be having these kinds of thoughts!"
        a "{i}I should stop believing everything Freya tells me!"
        scene ep6_269
        with dissolve
        mc "Hm~?"
        a "......"
        scene ep6_270
        with dissolve
        mc "Hey..."
        scene ep6_271
        with dissolve
        a "Ah! No, no, I'm not thinking of anything perverted at all!"
        a "I'm sorry, I'm sorry, I'm sorry!"
        mc "Excuse me?"
        scene ep6_272
        with dissolve
        a "*gasps*"
        a "I-it's n-nothing!"
        mc "What's happening with you? You were in such a rush to enter my room and now you're thinking of perverted things while looking at my body."
        mc "Am I really that tasty?"
        a "No, you're not!"
        mc "Ehhhh......"
        a "H-how did you get so fit? I couldn't imagine you being like this compared to your old shape."
    else:
        scene ep6_272
        with dissolve
        a "Can I ask something?"
        a "H-how did you get so fit? I couldn't imagine you being like this compared to your old shape."

    scene ep6_273
    with dissolve
    mc "Heeh... So you want to know my secret?"
    a "Uhm... Is it really a secret? Like... a secret training?"
    mc "So, you really want to know?"
    a "Mhm..."
    stop music fadeout 2
    scene ep6_274
    with dissolve
    mc "Well, fine. Listen up."
    mc "First, what's important is, to make sure you stick to this intense training regimen."
    scene ep6_275
    with dissolve
    a "{i}So it's really training then? He didn't go to the Gym, but training?"
    a "{i}What training?"
    play music 'audio/Workout.mp3' fadein 3
    scene ep6_276
    with dissolve
    mc "Listen, Aine."
    scene ep6_277
    with dissolve
    mc "You just have to keep doing it..."
    scene ep6_278
    with dissolve
    mc "No matter how hard it gets..."
    scene ep6_279
    with dissolve
    mc "It took me three years to get in this shape."
    scene ep6_280
    mc "One-hundred push-ups!"
    mc "One-hundred sit-ups!"
    scene ep6_281
    mc "One-hundred squats!"
    a "{i}Ah..."
    scene ep6_282
    mc "Then a ten-kilometer run!"
    scene ep6_283
    mc "Every single day!"
    scene ep6_276
    mc "Hmp..."
    stop music
    scene ep6_284
    play sound 'audio/scratch.mp3'
    with hpunch
    a "Uhh... Are you being serious?"
    mc "No, I just went to the Gym."
    a "I thought so."
    mc "So, what were you in a hurry to talk about?"
    play music 'audio/DifLove.mp3'
    image aiamctfpc:
        "ep6_285.jpg"
        pause 3.0
        "ep6_286.jpg"
        pause .2
        repeat
    show aiamctfpc
    with dissolve
    a "Uhm... Well... I bought a new PC yesterday, you see? But, the thing is... I didn't get it assembled in order to save some money."
    mc "And you don't know how to put it all together by yourself, right?"
    a "Yeah, that's right. I was hoping to ask you a favor to assemble it for me."
    a "I think there's a manual for everything, but I'm too nervous that I might ruin it if I don't know what I'm doing."
    mc "You're right about that... Do you need it now? Or..."
    a "I still have my old PC, so I can just use that for later classes instead."
    menu:
        "Get ready for work":
            $ ainehelpbuildpc = False
            mc "Hmm... To tell you the truth, I have to go and get ready for work now. So we could just do it later."
            mc "Or, you can ask Sky since she knows how to build her own PC too."
            a "Oh... I see..."
            a "Alright, I think I might just ask Sky instead."
        "Help her now":
            $ ainehelpbuildpc = True
            mc "Hmm... Okay, I'll help you. It's still early, so I have a some time to work on it."
            mc "Where's your computer box?"
            a "It's in our room's storage. Come and take a look!"
            mc "Alright, let's go."

            scene black
            with dissolve
            with fadeq

            scene ep6_287
            with dissolve
            mc "Why did you buy a new PC, by the way? Is your old one not powerful enough to handle your work?"
            scene ep6_288
            with dissolve
            a "It was fine, but Freya recommended that I should buy a new PC so we could play some games together."
            a "I didn't want to agree at first since I'm not really a gamer like her, but half of the money for it came from her, so I couldn't say no."
            a "She sent me the money before I knew it."
            scene ep6_289
            with dissolve
            mc "Heeh... So what games are you guys planning to play? I play games in my free time, too!"
            a "I have no idea, to be honest. She basically just forced me to buy this new one."
            scene ep6_287
            with dissolve
            mc "So it wasn't a recommendation, but a coercion?"
            scene ep6_288
            with dissolve
            a "Well, it's Freya we're talking about here. I know she'd keep pushing me no matter how many times I said no."
            scene ep6_287
            with dissolve
            mc "A new PC doesn't sound too bad, if you ask me."
            mc "What did you buy though?"
            scene ep6_290
            with dissolve
            a "I'm not actually familiar with them..."
            a "...but here's a list of all the items I bought yesterday."
            scene ep6_291
            with dissolve
            mc "......"
            scene ep6_292
            with dissolve
            mc "Wait, so you just bought all these products not knowing what they are?"
            a "I'm not really that into technology, so... yes."
            mc "Pardon me, but man... you're so out of touch. You weren't born in the 70s, were you?"
            scene ep6_293
            with dissolve
            a "*sighs* That's what Freya said to me last time. Even Gwen and Emma complain about it. But, that's how I really am."
            scene ep6_294
            with dissolve
            a "Anyway, there it is!"
            mc "Oh, wow! That's pretty big, isn't it? Did you buy it in parts?"
            scene ep6_295
            with dissolve
            a "No, it was a package deal, and they were supposed to set it up for me and deliver it here the day after I bought it, which would have been today."
            a "But I thought I should save a bit and refused the setup fee."
            scene ep6_296
            with dissolve
            mc "......"
            mc "How much was it?"
            a "Ten dollars or so?"
            scene ep6_297
            with dissolve
            mc "......."
            a "Hm? Why are you looking at me like that?"
            scene ep6_298
            with dissolve
            mc "I didn't know that you were so hard up, Aine. I would've just paid for it if I were you."
            mc "Ten bucks is not that much compared to messing your computer up, you know?"
            scene ep6_299
            with dissolve
            a "I gotta save my money, [mc]! Ten is still a lot! It's at least a day of food for me!"
            mc "Are you serious?! What the heck are you eating, then?"
            scene ep6_300
            with dissolve
            e "Ahhh... Take your lover's quarrel outside, please. There's still a person sleeping here..."
            scene ep6_301
            with dissolve
            a "......"
            mc "......"
            scene ep6_302
            with dissolve
            mc "Yeah, let's just get this done."
            a "G-good idea."

            scene black
            with dissolve
            with fadeq

            "One hour later..."

            scene black
            with dissolve
            with fadeq

            scene ep6_303
            with dissolve
            mc "There you go! Looking nice and beautiful!"
            a "Wow! I didn't think it would look this beautiful!"
            mc "You bought a nice one, that's for sure."
            a "It's pretty expensive, so maybe that's why."
            mc "I won't ask you how much it was. I have a pretty good sense just from looking at the parts you bought."
            scene ep6_304
            with dissolve
            a "Hmm... Can you guess how much it was, then?"
            menu:
                "$1250":
                    mc "Uh... $1250?"
                    a "Oh! You're close! *giggles*"
                "$1500":
                    mc "Uh... $1500?"
                    a "Nope! You're too far. But it's somewhere around that park. *giggles*"
                "$1100":
                    mc "Uh... $1100?"
                    a "Nah-uhh... You're too short. *giggles*"

            mc "Heeh... How much was it?"
            a "$1300 to be exact. It was supposed to be $1350, but since I bought a package, I got it at a discount."
            mc "*chuckles* You really are a cheapskate, Aine. I gotta remember that from now on."
            a "I guess I should educate you on how to budget your money properly then."
            a "You need to be practical now that the prices of things are going up."
            mc "Haha. We'll see about that."
            mc "Anyway, I need to get ready now. I have to be at work early today."
            a "Alright, thank you for helping me, [mc]. I appreciate it."
            mc "No worries."
            $ ainepoint += 1
            $ renpy.notify(ainenotif)
            if ainepoint == 10:
                scene ep6_305
                with dissolve
                a "*kisses*"
                scene ep6_306
                with dissolve
                $ renpy.pause()
                image aiamctfpc2:
                    "ep6_307.jpg"
                    pause 3.0
                    "ep6_308.jpg"
                    pause .2
                    repeat
                show aiamctfpc2
                with dissolve
                a "My god... How can you be so tall?"
                mc "Uhh... What was that for?"
                a "A second 'thank you'. That's for bringing us up here last night. I know you're the one who did it. *giggles*"
                a "I don't know how to repay you for all the kindness you're showing towards us, really."
                mc "Hmm... Maybe surprise me with something then?"
                a "Okay! I'll think of that something. *giggles*"
                mc "Jeez... I'll go now, alright?"
                a "Yep... Have a nice day today, [mc]."
                mc "You too."
                scene ep6_309
                with dissolve
                play sound 'audio/closedoor.mp3'
                "*door closes*"
                mc "......"
                yt "I guess that's a way to start a day, huh?"
                scene ep6_310
                with dissolve
                yt "*lightly chuckles*"
                yt "Let's get this done, then!"
    stop music fadeout 2

    scene black
    with dissolve
    with fade

    play music 'audio/City.mp3' fadein 2
    scene ep6_311
    with dissolve
    $ renpy.pause()
    scene ep6_312
    with dissolve
    k "Mhhn..."
    scene ep6_313
    with dissolve
    $ renpy.pause()
    scene ep6_314
    with dissolve
    k "*yawns*..."
    scene ep6_315
    with dissolve
    $ renpy.pause()
    scene ep6_316
    with dissolve
    $ renpy.pause()
    scene ep6_317
    with dissolve
    cl "Finally waking up, huh, boss?"
    cl "You're waking up late for someone who has a big job to do today."
    scene ep6_318
    with dissolve
    k "Huh...?"
    k "I'm sorry. But... May I know who you are and why you are in my room?"
    cl "Right, how rude of me."
    scene ep6_319
    with dissolve
    cl "My name is Claire. I'll be your and Jess' bodyguard for the time being. It's a pleasure to meet you, Miss Klara."
    scene ep6_320
    with dissolve
    k "Oh, I see... You're that person Jess was talking about last night."
    k "The pleasure is mine, I'll be in your care for now."
    k "{i}I can sense rudeness with the way she speaks, and that she's forcing herself to be respectful towards me. I'm not sure if I can trust her or not."
    scene ep6_321
    with dissolve
    cl "It's okay if you don't trust me at the moment. I truly deserve that."
    k "{i}How did she know what I was thinking?!"
    cl "...But this is a way for me to atone for my past sins on a journey for me to find my own way of living. So please allow me to serve you."
    k "It's alright since I trust Jess with her decisions. But what do you mean by your 'past sins'?"
    scene ep6_322
    with dissolve
    cl "I bet you're familiar with me if you've lived in Golden City."
    cl "I was known by the name of 'Owl' for the past five years. If you do, then you might have an idea who I am."
    k "*gasps*!"
    k "Y-you mean, you're that 'Owl'?! The real one?!"
    cl "Yes. The real one."
    k "There had been some reports of people trying to impersonate you and had been doing mischievous things around the city."
    k "But according to the rumors, the 'Owl' has pitch-black hair and a pair of bright sky-blue eyes. Both of your arms also have the tattoos that people were talking about."
    k "Although... no one has actually ever seen you before."
    cl "That's how I work, Miss Klara. Hence, my nickname."
    k "I guess you're not lying then..."
    k "But how come you're still..."
    cl "Alive?"
    k "...Yes."
    scene ep6_323
    with dissolve
    cl "*chuckles* I may look as pale as a dead body, but I'm alive. Was I said to be dead?"
    k "Yes, not only that, but I heard you were given a death sentence! Was that all... just a cover-up?"
    cl "None of that ever happened. I've been living my life for the past two years trying to work my way back into reality."
    cl "And now, here I am."
    scene ep6_324
    with dissolve
    k "Was Jess the one who..."
    cl "No, it was another person. Although Jess helped me get back on my feet."
    scene ep6_325
    with dissolve
    k "I see... I have been admiring her for her knowledge and power, but I couldn't understand where she's getting it all from."
    scene ep6_326
    with dissolve
    cl "She's separating herself from her family's name, that's all I know as well."
    cl "Years of knowing her, she's still a mysterious person, even for me and her friends."
    cl "She may be fragile physically, but we should never underestimate what she can do."
    scene ep6_327
    with dissolve
    cl "Which I did, and eventually lost to her."
    k "You guys... are so full of mystery."
    cl "The past is past, Miss Klara. We should never bring it back now."
    cl "You wouldn't want to hear the full story, either."
    k "I'm very curious, but then... I should probably just leave it at that. I have my own business to take care of at the moment, and that's what I should focus on."
    cl "Yes, we all should."
    k "......"
    scene ep6_328
    with dissolve
    k "I never would've imagined that you're this pretty considering your status, Claire. But I guess you already know that, right?"
    scene ep6_329
    with dissolve
    cl "I never praised myself for it, but I'll take that as a compliment, Miss Klara. Thank you."
    k "Have you eaten your breakfast yet?"
    scene ep6_330
    with dissolve
    cl "Not yet, I'm afraid. I haven't eaten anything since last night, actually."
    k "Oh, jeez! Come with me, I'll cook us both some breakfast!"
    cl "Roger."
    cl "Should I wake Jess up too?"
    k "If you would, please, dear. You young ones should never skip your breakfasts!"
    cl "So you're becoming my mother instead of my boss, huh?"
    k "That's just the right thing to do right now, dear. *giggles*"
    scene ep6_331
    with dissolve
    cl "Thinking of my mother now..."
    scene ep6_332
    with dissolve
    cl "I... should probably never have done that..."
    scene ep6_333
    with dissolve
    cl "*chuckles* Life... What have you done to me?"
    stop music fadeout 2

    scene black
    with Dissolve(2.0)
label klarapause2:
    if _in_replay:
        $ name = persistent.gallery_name
    scene klarapause2
    with dissolve
    $ renpy.pause()
    $ renpy.end_replay()
    play sound 'audio/gamepause.mp3'
    show title at move_slide
    with flash
    $ renpy.notify(imageunlock)
    $ renpy.pause()

    scene black
    with dissolve
    with fade

    play music 'audio/BlackCat.mp3' fadein 2
    if freyapoint == 6:
        scene ep6_334
        with dissolve
        mc "Ahh... The good ol'... burger shack!"
        mc "*sniffs*..."
        mc "Ahh...!"
        scene ep6_335
        with dissolve
        mc "I might be stupid, but the air here seems to be fresher than outside. This is the only place where I can not think of my problems, even if it is just a temporary reprieve."
        mc "I should just live here instead!"
        scene ep6_336
        with dissolve
        mc "Hahaaa! Bring the customers on, here I come~!!"
        scene ep6_337
        with dissolve
        f "Hey!"
        scene ep6_338
        with dissolve
        mc "Hm?"
        "*poke*"#pokes mc's cheek
        f "Got'cha~!"
        mc "Oh, hey, Frey! You're early today!"
        scene ep6_339
        with dissolve
        f "Heeh... Calling me by my nickname. Why are you so energetic that it seems like you just had some pot?"
        mc "Never mind me, but what's with you sending me that picture last night?!"
        mc "Do you actually want me to go to jail, huh?!"
        f "Hello~? I'm nineteen, Mister~! Just perfectly legal!"
        scene ep6_340
        with dissolve
        f "Teeheee~!"
        mc "Again, don't just 'teehee' me!"
        mc "That caught me off guard and I didn't know what I would do after seeing that!"
        scene ep6_341
        with dissolve
        f "Uhh... probably wank on it?"
        mc "I admit it's good wanking material, but don't shock me like that, I almost had a heart attack!"
        image frmctbsd2:
            "ep6_342.jpg"
            pause 3.0
            "ep6_343.jpg"
            pause .2
            repeat
        show frmctbsd2
        with dissolve
        f "There's a saying that girls like spontaneous men, so I was thinking I should apply that in reverse!"
        f "I call it 'My #1 fan' service! I bet you liked it!"
        mc "But I'm not your #1 fan!"
        f "You will be, I just know it. Hahaha!"
        mc "So have you done that to anyone besides me?!"
        f "Nope! Never, until I found someone I could tease a bit."
        mc "And that's me?"
        f "Yeppers!"
        f "Hey, you're pretty fun to talk to, you can't blame me for teasing you! Hahaha!"
        mc "*sighs*..."
        mc "Now, I'm getting depressed..."
        f "Naah... I bet you want more of it."
        f "Don't worry, I'll do it every night from now on. Well, if you ask me to, that is. Wahahaaa!"
        yt "This girl is definitely testing me."
        f "Chin up now, we still got a lot to do. Lily is on her way here now too."
    else:
        scene ep6_334
        with dissolve
        mc "Ahh... The good ol'... burger shack!"
        mc "*sniffs*..."
        mc "Ahh...!"
        mc "I might be stupid, but the air here seems to be fresher than outside. This is the only place where I can not think of my problems even if it's a temporary reprieve."
        mc "I could just live here instead!"
        mc "Hahaaa! Bring the customers out, here I come~!!"

    scene black
    with dissolve
    with fadeq

    "After the shift...."

    scene black
    with dissolve
    with fadeq

    scene ep6_344
    with dissolve
    mc "See? I told you we'd be fine if we're prepared for it. We got almost the same number of customers, and yet we're not nearly as exhausted as yesterday."
    l "Haha! Yeah, I believe you now. We handled it just fine."
    l "Although, this will be our everyday situation now. So I can't help but feel terrified."
    mc "You'll get used to it, trust me."
    scene ep6_345
    with dissolve
    f "I'm sorry to leave you guys like this, but I have to get back home as soon as possible. My class schedule is early today."
    f "I'll make it up to you next time, I promise."
    mc "Hey, I told you 'studies first', right? Don't worry about it. Lily and I got this."
    scene ep6_346
    with dissolve
    f "Thanks! Talk to you later, [mc]!"
    scene ep6_347
    with dissolve
    f "*winks*"
    yt "Jeez..."

    if lilypoint == 6:
        $ lilytracksory = True
        scene ep6_348
        with dissolve
        mc "Anyway, how's it going on your side, Lily? You told me you're pretty busy with your studies too."
        scene ep6_349
        with dissolve
        l "I'm struggling a little bit, because I'm pretty much average when it comes to smarts. But I'll be fine since I got some help from my classmates during study sessions."
        l "I have no idea why I am always nervous about exams coming up. I'm passing them just fine, but I can't help it. *giggles*"
        mc "I think most of us are, especially during our final year. I was pretty much the same during my last year in college."
        mc "I didn't have a lot of confidence before. But I had to do what I had to do."
        mc "And... I graduated with honors, which I didn't actually expect. Hahaha!"
        image llmctbs:
            "ep6_350.jpg"
            pause 3.0
            "ep6_351.jpg"
            pause .2
            repeat
        show llmctbs
        with dissolve
        l "Oh, really~? You never told me you graduated with honors! That's quite impressive, [mc]!"
        mc "Aha haa... Thanks!"
        mc "Yeah, I may have been at the top of the class, but I'm still here, working in a burger shack."
        mc "Though, I've never felt degraded by working here. I really love this place enough that I don't want to leave even if somebody offers me another job."
        mc "I could probably live in here if Miss Jess allowed me to. Ahahaha!"
        l "Wait, you're not serious, right?"
        mc "Nah... I'm just kidding. Don't get to be as crazy as me though."
        l "Haha. Don't worry. I love being in my bed and pillows every night."
        mc "Don't be angry, but I first thought that you were a couch potato. I was a bit shocked to learn that you were actually an athlete."
        l "You got some good sense, I must say."
        mc "Wait, I was right to assume that?!"
        l "Yeah, you're not wrong. I used to be, but that changed weeks after I started training."
        l "I just love being on the track. I guess that's the same feeling when you told me that you want to live here. Haha!"
        mc "We both got something we relate to, huh?"
        mc "I really want to know about what happened now that you told me a little bit of it. I'm quite thrilled, to be honest."
        l "Mmh... It's... quite tragic, really. It was fun at first, but..."
        mc "...Was it that sad?"
        l "Not so much... But if you're that eager to know about it, then I don't mind sharing it."
        mc "Please do!"
        scene ep6_352
        with dissolve
        l "......."
        l "*sighs*..."
        l "Where should I even start?"
        l "......"
        l "I think there's nothing but that day... The day I was recruited to join the club."
        l "It's when I first met our captain... Also the time I met my best friend and my partner on the team, Anne."
        stop music fadeout 2

        scene ep6_353
        with flash
        play music 'audio/phonealarm.mp3'
        "*phone alarm rings*......"
        scene ep6_354
        with dissolve
        l "Urrhh..."
        scene ep6_355
        with dissolve
        l "Yeah... I know... First day of school... Time to get up..."
        stop music
        scene ep6_356
        with dissolve
        l "*yawns*..."
        scene ep6_357
        with dissolve
        l "*sighs*..."
        play music 'audio/EnergizedMorning.mp3' fadein 2
        scene ep6_358
        with dissolve
        $ renpy.pause()
        scene ep6_359
        with dissolve
        $ renpy.pause()
        scene ep6_360
        with dissolve
        $ renpy.pause()
        scene ep6_361
        with dissolve
        l"{i}Alright... Let's go."
        play sound 'audio/ridebike_righttoleft.mp3' loop
        scene ep6_362
        with dissolve
        scene black
        with Dissolve(3.0)
        stop sound

        scene black
        with dissolve
        with fade

        scene ep6_363
        with dissolve
        play sound 'audio/bikestop.mp3'
        $ renpy.pause()
        scene ep6_364
        with dissolve
        l "*deeply exhales*"
        scene ep6_365
        with dissolve
        l "{i}Drealerra Academy... The only school in this city that has both high school and college."
        l "......"
        l "How convenient..."
        scene ep6_367
        with dissolve
        un "Ahh...! How come nobody ever wants to join the team...?"
        un "I mean..."
        scene ep6_368
        play sound 'audio/woosh.mp3'
        un "Look at all those people trying to apply for the Volleyball club!"
        scene ep6_369
        with dissolve
        un "Well? You did join the team last year, didn't you?"
        un "Why don't you stand up and try to hand out the forms for real this time, Anne?"
        un "You're always so pumped up when it comes to training, but never bring that enthusiasm to other things like this."
        an "Ehh...? I'm always pumped up, Cathy!"
        scene ep6_370
        with dissolve
        ca "*sighs* You're obviously not..."
        ca "You need to learn while I'm still here."
        scene ep6_371
        with dissolve
        ca "Hey, there's a first-year over there. Go and give her a form."
        an "Hm? How did you know she's a first-year?"
        ca "I have been attending this academy longer than you, how do you think I was able to tell?"
        an "Ehh... You go and give her a form then..."
        play sound 'audio/punch.mp3'
        scene ep6_372
        with hpunch
        ca "*punch*"
        ca "Stand up, you slug! Nisha isn't here, so it's your responsibility this time!"
        an "Okay, okay!"
        scene ep6_373
        with dissolve
        l "{i}Wow...! Look at all those people! What is happening? Is it a club?"
        scene ep6_374
        with dissolve
        l "{i}I should look for a club to join as well. I wonder if there's a Manga club in this academy."
        l "{i}I don't particularly like it, but that's all I can think of joining right now. I'm not really good at sports, too..."
        play sound 'audio/woosh2.mp3'
        scene ep6_375
        with hpunch
        an "Hey, you, first-year girl! Want to join the Track and field club?"
        an "We give free tuition to those who join!"
        scene ep6_376
        with dissolve
        l "Wait, for real~?!"
        scene ep6_377
        with dissolve
        ca "No, we don't. Stop making up stuff just to get people to join, will you, Anne?"
        scene ep6_378
        with dissolve
        l "Track and field club, huh?"
        l "I'm not really good at sports, so I probably should say no."
        an "Heeh? Do you have a club to join in mind then?"
        l "Uhm... I'm thinking the Manga club?"
        an "No, we don't have a Manga club. And I'm being completely honest this time."
        scene ep6_379
        with dissolve
        an "Right, Cathy?"
        ca "Mhm..."
        scene ep6_380
        with dissolve
        l "Really? That's the only club I have in mind right now. I'm not confident about anything but studying."
        an "You're a smart ass, huh?"
        l "No, I'm not."
        an "Well then, have you ever seen a Track and Field competition before?"
        l "Just on TV... Like the Olympics you mean? Then yes."
        an "What do you think of it?"
        l "Uhm... It's boring?"
        an "Well, that must be because you suck at sports, indeed!"
        l "I told you already."
        scene ep6_381
        play sound 'audio/woosh.mp3'
        an "The adrenaline when the race is about to start..."
        show ep6_382
        play sound 'audio/woosh2.mp3'
        an "That feeling when you go {b}zoom{/b} to the finish line and win the race..."
        show annefinish
        with flash
        pause 3.5
        hide annefinish
        show ep6_384
        with flash
        an "Is just the best feeling ever!"
        scene ep6_383
        with dissolve
        ca "*chuckles* It must be nice to be simple-minded."
        ca "Don't go bragging now, Anne."
        an "I'm not! I'm just trying to convince her to give it a try!"
        scene ep6_385
        with dissolve
        an "Hey, what's your name?"
        l "Uhm... Lily. My name is Lily."
        scene ep6_386
        with dissolve
        an "Your last name?"
        l "Kim. Lily Kim."
        an "I got it!"
        scene ep6_387
        with dissolve
        an "*scribbles* Lily... Kim..."
        an "There!"
        scene ep6_388
        with dissolve
        an "Listen, I listed you down as an applicant, alright?"
        l "Huh? But I'm really not interested in joining your club."
        scene ep6_389
        with dissolve
        an "That's fine! Just think about it for now."
        scene ep6_390
        with dissolve
        an "Look, I'll wait for you right here after the class is done this afternoon. I'll take you to the stadium so you can see things for yourself."
        l "The stadium?"
        scene ep6_391
        with dissolve
        an "Yeah! We don't have a track here at the academy, so we use the city's stadium as our official training area."
        l "Wait, are you allowed to do that?"
        an "Yep! Hundred percent! The government happily provided it for us!"
        l "I see..."
        an "You don't have to join right away. But I want to show you something before you make your decision."
        an "Think about it, Lily."
        l "O-okay..."
        scene ep6_392
        with dissolve
        $ renpy.pause()

        scene black
        with dissolve
        with fade

        scene ep6_393
        with dissolve
        l "{i}Track and field, huh...?"#looking outside the window
        l "{i}I think there's a lot of types of events included, or whatever they call them..."
        l "{i}The idea of me being an athlete isn't really sinking in to me."
        l "{i}I don't have any health issues, in fact, I'm quite fit to do it. But the sport doesn't really pique my interest at all."
        l "{i}It's just a simple sport anyway... Why was she so enthusiastic about it?"
        l "{i}I bet anybody could do it. What else do they do aside from running?"
        l "{i}Well... I guess I can go with her later and check it out at least."
        l "{i}I won't lose anything by doing so. It's not like my parents are around to scold me anymore."
        l "{i}Sorry, mom and dad. I might have to go back home a bit late today..."
        scene ep6_394
        with dissolve
        g1 "Hey, you want to join the Volleyball club? I heard they have a lot of slots for tryouts this year!"
        g2 "Really?"
        g2 "What will we even do there? We are not cut out for that kind of sport. Volleyball is for tall players, dumbass."
        g1 "Come on! It will make us look cooler, I am telling you! Just imagine wearing the club's official jersey!"
        g2 "That's all you are aiming for by joining a club? Jeez..."
        g1 "Yeah, but it's not a bad idea to try, right?"
        g2 "Well... That ain't so bad... Is it?"
        l "{i}It seems like Volleyball is pretty popular here, huh? Everyone seems interested in joining their club."
        l "{i}Anyway, I should focus on today's classes before thinking about anything else."
        l "{i}That's what I came here for, first and foremost, not for these silly little clubs everyone is talking about right now."
        stop music fadeout 2

        scene black
        with dissolve
        with fade

        play music 'audio/MariachiWay.mp3' fadein 2
        scene ep6_395
        with dissolve
        an "Alright, now we wait."
        an "My convincing technique might be a little bit shallow, but... oh well..."
        an "I can wait for thirty minutes, if she doesn't show up, then I'll take it as a 'no' from her."
        scene ep6_396
        with dissolve
        an "*crack*"
        scene ep6_397
        an "*crack*"
        scene ep6_398
        an "*crack*"
        scene ep6_399
        an "*crack*"
        scene ep6_400
        with dissolve
        an "Hup!"
        scene ep6_401
        with dissolve
        an "Hup!"
        scene ep6_402
        with dissolve
        an "Hng...!"
        scene ep6_403
        with dissolve
        an "Hm?"
        scene ep6_404
        with dissolve
        an "Hey, hey, hey~! Look who's here!"
        scene ep6_405
        with dissolve
        an "Have you finally decided to join? Or..."
        l "Not yet. I just want to check it out for now."
        l "I mean... it wouldn't hurt to join. It's an extracurricular activity anyway, but it will be pointless if I'm not interested in it."
        an "You make a good point there. I won't force you to join after this. It's all up to you, but trust me, my teammates are all awesome people!"
        scene ep6_406
        with dissolve
        an "Anyway... Wear these!"
        l "Running shoes? What for?"
        an "It's testing time!"
        l "Huh? But I'm not-"
        an "Nope! Come on, just do it! The stadium is just a kilometer away."
        an "And besides, no school shoes are allowed inside the stadium."
        l "Eh? That's weird..."
        an "Yep, it is! It's just a team rule that we came up with. We gotta pay respect to the Gods of Track and Field! Ahaha!"
        l "*sighs*... I can see this is going downhill already."

        scene black
        with dissolve
        with fadeq

        scene ep6_407
        with dissolve
        l "{i}The shoes are a good fit for me. How did she..."
        scene ep6_408
        with dissolve
        l "How did you know my foot size?"
        an "Hm? I didn't. It's just a guess since we're pretty much the same height."
        scene ep6_409
        with dissolve
        an "If it didn't fit, then... well... I dunno..."
        l "{i}What an airhead..."
        scene ep6_410
        with dissolve
        an "But hey, you look pretty good in them! Look at you~!"
        l "Yeah, it's not that bad."
        scene ep6_411
        with dissolve
        an "The school uniform is still not that great though... I hate it. It's so tight that I can barely breathe!"
        scene ep6_412
        with dissolve
        an "Let's not do any more chatting. Time is gold! I mean it... Literally."
        l "......"
        l "I don't get it..."
        an "*giggles* I'll tell you about it next time. Time for a short warm-up now!"
        l "Okay..."

        scene black
        with dissolve
        with fadeq

        scene ep6_413
        with dissolve
        an "Alright, here we are!"
        scene ep6_414
        with dissolve
        an "......"
        an "Huh? Where is she?"
        an "Ahh! I must have left her behind!"
        scene ep6_415
        with dissolve
        l "*huff* *huff* *huff*"
        an "Oh, there you are! I thought I lost you or something. Did you have trouble keeping up?"
        scene ep6_416
        with dissolve
        l "Isn't it... obvious? I thought... we were just going for a jog? Why were you... running so fast?"
        l "*huff* *huff* *huff*"
        an "Ahaha! I'm sorry, I'm sorry! But really, I was just jogging!"
        l "You're lying!"
        l "*huff* *huff*"
        an "Nope! Trust me, my teammates jog a lot faster than me."
        l "For real?"
        an "Yeah! Isn't it exciting?"
        l "No, not really. It makes me nervous instead."
        an "Wahahaha~!"
        an "Come here, I'll show you the environment here."
        stop music fadeout 2
        scene ep6_417
        with dissolve
        an "Let me introduce to you our second home..."
        show ep6_418
        with dissolve
        an "The city's official stadium..."
        play music 'audio/TheArrival.mp3' fadein 2
        hide ep6_418
        show stadiumshow
        with dissolve
        pause 8.5
        hide stadiumshow
        show ep6_419
        with dissolve
        l "Wow... It's... It's really huge..."
        an "Right~?"
        an "How does this compare to the things you saw on televisions?"
        l "I-it's nothing like it. It looks very small compared to this..."
        an "To be honest with you, Olympic-sized stadiums are way bigger. It's just that the camera angles make them look smaller because they usually film things from up top."
        an "But once you're the one inside the stadium, you can actually see things for yourself."
        an "We are lucky that we have this as a training ground instead of an ordinary school track."
        an "This right here is our second home. The place where we shed blood, sweat, and tears in order to get to the top."
        l "*gulps*"
        an "Heh... Are you still nervous?"
        l "No, right now... I'm just in awe. I've never been in an actual stadium before. This is my first time."
        scene ep6_420
        with dissolve
        an "Well, I'm glad I could be the one to deflower you. Wahaha!"
        scene ep6_421
        with dissolve
        l "You could've said that with a bit more tact, you know?"
        an "Haha. Don't mind me, that's just the way I talk. Don't let it get to you."
        scene ep6_422
        with dissolve
        an "Come! Let's take a walk on the track. I'll introduce you to the team while we're at it."
        l "Are we allowed to do that?"
        an "Of course! Just because they are in the middle of training, doesn't mean we can't step inside."
        stop music fadeout 2
        l "Alright then."
        play music 'audio/Damage.mp3' fadein 2
        scene ep6_423
        with dissolve
        l "*steps*"
        l "......"
        l "That's weird..."
        an "Hm? How does the rubber feel?"
        l "Is the track made of rubber?"
        scene ep6_424
        with dissolve
        an "Yeah, a hundred percent synthetic rubber. It's composed of rubber particles so it makes the spike shoes grip to it a lot better."
        scene ep6_425
        with dissolve
        l "It's a bit springy... but it feels... quite comfortable?"
        an "Haha! I had almost the same reaction when I first stepped in here. That makes me happy in a way."
        an "But yeah, it's better than running on tracks made of dirt, rocks, and sand, that's for sure. You can feel every step you make on a rubber track."
        scene ep6_426
        with dissolve
        l "Now that you mention it, how long have you been running?"
        scene ep6_427
        with dissolve
        an "Ehm... Well... I got interested in it since I was in primary school. I saw a Track and Field competition on TV just like you."
        an "I got curious and started running during middle school. So it has been years, and I never stopped since then."
        scene ep6_428
        with dissolve
        l "Have you ever won?"
        an "You can't win every time, there's a lot of prodigies out there that are much better than you. But I did win quite a lot of events already."
        an "If we are talking about experience, I have loads of it! Haha!"
        an "Although, it has been eating away at my studies. All I can think about is training and running since I started."
        scene ep6_429
        with dissolve
        l "Uhm... I think you've got your priorities backwards..."
        an "That's the biggest drawback, being involved seriously in sports while studying isn't an easy task. You gotta manage your time properly."
        l "Do you?"
        an "No, I don't."
        l "I thought so..."
        scene ep6_430
        with dissolve
        un "Anne, you have thirty minutes. Finish it up and do your drills. Don't forget the usual five laps of jog."
        an "Yeah, yeah! I got it, Ed! But I already jogged on my way here."
        ed "No, add another five laps on top of that. We need to work on your stamina."
        an "Yes! Copy that, Ed!"
        scene ep6_431
        with dissolve
        ed "*sighs* If only the rest of this team was more like you."
        scene ep6_432
        with dissolve
        an "That's Ed, by the way. He is both our coach and our trainer."
        play sound 'audio/introslam.mp3'
        scene ep6_432_2
        an "He's been coaching the team for almost five years now. At least, that's what he says."
        an "He's considered one of the top trainers in the whole region. He is very strict, but pays excellent attention to your progress."
        an "When you have him as a coach, there is no doubt that you'll shed tears in no time."
        scene ep6_433
        with dissolve
        un "Yes, team captain wannabe. Do your drills or you will be the one who will shed tears in no time, airhead."
        an "Ugh! Mind your own business, you monster! Can't a woman slack for a bit?!"
        scene ep6_434
        with dissolve
        un "By the way, good job finding an applicant in my place. I will buy you a popsicle after today's training."
        an "Wait, really~?!"
        un "We'll talk about it later. Bye~!"
        scene ep6_435
        with dissolve
        $ renpy.pause()
        play sound 'audio/introslam.mp3'
        scene ep6_435_2
        an "The one I just talked to is Nisha."
        play sound 'audio/introslam.mp3'
        scene ep6_435_3
        an "The other one is her twin sister Natasha."
        an "Both are in their 3rd year."
        an "The two of them are our distance runners. They run all the longest races which are the 3000 and 5000 meters."
        an "They even run the 1500 meters race. They're real monsters in terms of stamina."
        an "Though, if you ask me who's stronger, I'd say Nisha. She started running way before her twin sister followed her."
        an "If you want some tips on improving your lungs, you should talk to them. Or you can always just ask for advice from Ed instead."
        an "But all that will depend on your strength and what event you're going to compete in."
        l "I see."
        an "Don't think about it for now. Once you finally decide to join, that's when we'll test you out and find what event coach will put you in."
        l "Alright."
        scene ep6_436
        with dissolve
        $ renpy.pause()
        scene ep6_437
        with dissolve
        an "Yoh, Lidia! Your jumps are flawless as always! Keep up the good work!"
        scene ep6_438
        with dissolve
        lid "Thanks, Second Captain. But I'm your senior, you should treat me like one."
        an "I always do!"
        lid "No, you obviously don't."
        scene ep6_439
        with dissolve
        un "Hey, Anne! Is she a new applicant? Is she joining?"
        scene ep6_440
        with dissolve
        an "Not yet, I guess? I'm just showing her around for now."
        un "Oh, I see..."
        scene ep6_441
        with dissolve
        un "I hope you actually will join the team, we are kinda one person short at the moment."
        l "I'll think about it."
        scene ep6_442
        with dissolve
        un "Awesome! Enjoy the tour~!"
        l "I will, thanks!"
        scene ep6_443
        with dissolve
        l "She's so jolly!"
        scene ep6_444
        with dissolve
        l "I like her! Haha!"
        play sound 'audio/introslam.mp3'
        scene ep6_444_2
        an "Yep, that's Miwa for you."
        play sound 'audio/introslam.mp3'
        scene ep6_444_3
        an "The other one is her cousin, Lidia. Also both in their 3rd year."
        an "The two of them compete in the hurdle events. Both 100 and 400 meters hurdles."
        an "Don't let their looks fool you, especially Miwa. She doesn't like to talk about it, but she's one heck of a hardcore when it comes to her events."
        an "She may be short, but she's always managed to win something in all her competitions so far. Every city in the region has eyes on her right now."
        an "I'm just glad that she's on our team or she'd be trouble."
        l "How about her cousin?"
        an "Lidia? She's good! Like... extremely good! I think she has the most perfect jumping form I've seen, by far!"
        an "So much so that the coach compliments her every time she jumps over a hurdle. Haha!"
        an "In terms of overall strength... both are pretty even."
        an "They even count each other's scores whenever they do a time trial!"
        an "Right now, it's 21-22 in favor of Lidia. I'm sure Miwa will tie that score again next time, so it's just a bother to try and think about it."
        scene ep6_445
        with dissolve
        l "I get it, but why does everyone like to call you second captain or something like that?"
        an "Eh, no... I'm not a captain, I'm not the type to shoulder responsibility for a team. I just like to compliment everyone for their hard work, that's all."
        l "I see..."
        scene ep6_446
        with dissolve
        ca "Hey, you're here. Clap for us real quick, Anne."
        an "Heeh... Doing your workouts already?"
        scene ep6_447
        with dissolve
        un "Yeah, coach gave us ten rounds of 300 meters this time."
        an "Just ten?! That's pretty light!"
        un "Well, ask coach. 'Cuz I have no idea why. But I love this workout, this is the only distance where I can beat Cap'n."
        ca "*chuckles* Tell me that once you actually do, Brook."
        an "Alright, enough chit-chat. Time to run ladies."
        scene ep6_448
        with dissolve
        br "I'm ready."
        scene ep6_449
        with dissolve
        an "......"
        scene ep6_450
        with dissolve
        an "Set!"
        play sound 'audio/clap.mp3'
        scene ep6_451
        an "*claps*!"
        l "Are they the middle distance runners?"
        an "Damn right! You catch on pretty quick, Lily!"
        play sound 'audio/introslam.mp3'
        scene ep6_451_2
        an "Brook..."
        an "We both tried out for the team last year and she used to be my partner, but coach recently discovered her stamina and moved her to be Cathy's partner instead."
        an "At the moment, she's still trying to get used to the workouts and has been trying to match Cathy's time."
        play sound 'audio/introslam.mp3'
        scene ep6_451_3
        an "Cathy..."
        an "Our one and only Captain, and the best in the whole universe!"
        an "She might look intimidating, but that's just her looks. She's good at inspiring and lifting everyone's mood whenever we are struggling. That's why I love her. Haha!"
        an "You'll discover her qualities as a captain when you get to know her more."
        l "So, what are the events the middle runners handle?"
        an "Right now, they are both running the 400 and 800 meters events. You can consider them sprinters in a way, but with much better endurance."
        l "I see..."
        scene ep6_452
        with dissolve
        an "And lastly, there's me."
        play sound 'audio/introslam.mp3'
        scene ep6_452_2
        an "Pardon the late introduction, but my name is Anne. Nice to meet you, Lily."
        l "Yeah, nice to meet you too."
        an "I handle the best of all the events! The sprints!"
        an "There's three events for sprinters, actually. 100, 200, and 400 meters dash. If you're running international, that is."
        an "High school competitions only consider 100 and 200 as sprinter's events."
        an "400 and 800 are middles."
        an "1500, 3000, and 5000 meters runs are the long-distance."
        an "In international competitions they classify 3000 meters as a middle distance, which is really absurd if you ask me. That's obviously a long run. Haha!"
        l "Yeah, that's a pretty long run to be considered middle distance."
        an "Right~?"
        scene ep6_453
        with dissolve
        an "So... Was that interesting enough to convince you to join the team?"
        l "......"
        scene ep6_454
        with dissolve
        l "...I am definitely intrigued... but..."
        an "But...?"
        l "......"
        scene ep6_455
        with dissolve
        l "...Huh?"
        scene ep6_456
        with dissolve
        l "Whaaa~!"
        l "W-w-why are you all here?!"
        scene ep6_457
        with dissolve
        ca "We're quite interested to hear what you're going to say, please don't mind us."
        scene ep6_458
        with dissolve
        miw "Come on... Join us! We can't compete for the upcoming winter tournaments if we lack one member..."
        scene ep6_459
        with dissolve
        ca "Actually, we can. But the team will be at a huge disadvantage."
        ca "You guys can still run your events, sure. You might all win, and that's great. But that's not all there is to Track and Field."
        ca "There is a point system that determines the team that wins a meet. Whether the whole team wins or loses the competition is decided by that system."
        ca "Every athlete who runs gets one point even if you lose. As long as you reach the finish line, that's all that matters."
        ca "And there's no better joy than to win as a team."
        an "Damn right, Captain~!"
        ca "But we are not forcing you, Lily. I'm just trying to tell you that we need another teammate who will aim for the Nationals this year."
        scene ep6_460
        with dissolve
        ca "And I'm not joking. Our team has been one of the top competitors in the region for almost ten years straight."
        ca "Drealerra Academy is a living legend when it comes to sports. And the Track and Field team always aims for the top."
        scene ep6_461
        with dissolve
        l "I get it, yeah... But, I don't even know if I can handle it."
        l "When I stepped on the track today, I felt something clicking with me. I can't really explain what it is, but I was terrified of that feeling."
        l "When Anne took me for a tour, I was glad to meet new people. But at the same time, I was intimidated."
        l "I'm... just not the kind of girl who's into sports."
        l "I didn't even think of playing any sports, even once in my life."
        scene ep6_462
        with dissolve
        ca "I can't disagree with you. We all went through the same thing and everyone here knows that kind of feeling."
        scene ep6_463
        with dissolve
        ca "It's just a sport. It's just a club."
        scene ep6_464
        with dissolve
        ca "But once you taste the joy of winning a race, that's when you'll realize that Track and Field is fun."
        scene ep6_465
        with dissolve
        an "Mhm! Mhm~!"
        scene ep6_466
        with dissolve
        ed "Hey, you guys! Get back to training!"
        ev "Yes, sir!"
        scene ep6_467
        with dissolve
        an "Don't push yourself, Lily. You're still welcome to join any time."
        an "However, I wouldn't advise you to take too long to come up with a decision, or you'll be late for the training schedule. It'll be hard for you to catch up."
        l "I respect you guys, so... I will think about it and decide tonight."
        l "I don't want to keep you in suspense over nothing."
        scene ep6_468
        with dissolve
        an "......"
        scene ep6_469
        with dissolve
        an "It's nice to know that you're a lot more mature than me."
        an "If you ever decide to join, please be my partner."
        scene ep6_470
        with dissolve
        an "Later, Lily. I have to warm up for my drills and workout."
        stop music fadeout 2

        scene black
        with dissolve
        with fade

        play music 'audio/Inspiring.mp3'
        scene ep6_471
        with dissolve
        l "......"
        scene ep6_472
        with dissolve
        l "*sighs*"
        scene ep6_473
        with dissolve
        l "{i}What should I do now?"
        l "{i}Joining a club is not half bad since an extracurricular activity is what I wanted. But a sports club?"
        l "{i}I know that if I'm not motivated enough, I won't be able to keep up with it. Especially considering what I saw earlier, it seems to be a pretty intense sport."
        l "{i}There's definitely more to it than what I expected it to be. I guess my opinion about it was clearly wrong."
        l "{i}From now on, I should never judge anything before knowing what it really is."
        scene ep6_474
        with dissolve
        l "{i}But what was that thing I felt when I first stepped onto the track?"
        l "{i}I had butterflies in my stomach, but at the same time, my feet never felt lighter than ever."
        l "{i}I felt like it was sucking me in. A feeling that strong, yet so unknown... It only makes me more nervous."
        scene ep6_419
        with flash
        an "This right here, is our second home. The place where we shed sweat, blood, and tears in order to get to the top."
        scene ep6_464
        with dissolve
        ca "But once you taste the joy of winning a race, that's when you'll realize that Track and Field is fun."
        scene ep6_474
        with flash
        $ renpy.pause()
        scene ep6_475
        with dissolve
        l "*sighs*..."
        l "{i}I'll just order out tonight... I'm too tired to cook right now."
        l "{i}All this thinking uses up all my strength."
        scene ep6_476
        with dissolve
        l "Hm?"
        l "{i}Ahh... I forgot to return Anne's shoes!"
        l "......"
        l "{i}Did she... do that on purpose?"
        scene ep6_477
        with dissolve
        l "......"
        scene ep6_478
        with dissolve
        $ renpy.pause()

        scene black
        with dissolve
        with fadeq

        "The next afternoon..."

        scene black
        with dissolve
        with fadeq

        scene ep6_479
        with dissolve
        an "Hey, Cath..."
        ca "Hm?"
        an "Do you think she'll come?"
        ca "I have no idea. We did what we could to convince her."
        ca "As for what I saw with her, based on the way she talks, she is clearly a timid person. There's a high probability that she won't join us."
        an "Aww... I gave her my extra pair of shoes too...!"
        scene ep6_480
        with dissolve
        br "Wait, you did what?!"
        br "Don't tell me you gave her my shoes!"
        an "Nah... They were mine. Yours are the one I'm using right now."
        scene ep6_481
        with dissolve
        ca "But..."
        an "Hm?"
        ca "I was exactly like her when I first joined the team."
        scene ep6_482
        with dissolve
        an "Really? You never told me that story before!"
        ca "Well... I don't often think about that time, because look where I am now."
        an "Yeah, yeah... You're currently the best middle runner in the region, I know... You don't have to brag about it."
        scene ep6_483
        with dissolve
        ca "I was not into it, because... it's just a club, it's just a silly little sport. Where would it take me even if I reached the top?"
        ca "Those were my thoughts before I joined."
        ca "But all it took me was the resolve to do it."
        stop music fadeout 2
        ca "It doesn't matter if you like it or not. There will always be something that will pull you towards that path."
        play music 'audio/HeadingNorth.mp3'
        scene ep6_484
        with dissolve
        "*steps*"
        scene ep6_485
        with dissolve
        br "And... I guess you guys don't have to worry about that."
        an "Hm? Why?"
        scene ep6_486
        with dissolve
        br "Look who's here."
        ca "*chuckles* I guess I was wrong about her."
        scene ep6_487
        with dissolve
        an "Whaaa...!"
        an "Lily~!"
        an "Go talk to coach Ed for now! We can't stop once we start warming up!"
        l "Alright!"
        scene ep6_488
        with dissolve
        ed "Well? Have you finally made up your mind? Anne and Cathy told me all about you yesterday."
        ed "I honestly thought you'd never come back."
        l "Yes, I want to try it out. Whether I can handle it or not, I won't know unless I try."
        scene ep6_489
        with dissolve
        ed "That's fine. As long as you have the resolve to do it, that's all that matters."
        ed "I will shape you into something you can be proud of, so prepare yourself."
        l "T-thank you for having me!"
        ed "I have good eyes for other people's personalities, and I saw you as a very timid person as soon as I saw you here."
        ed "Honestly, I wasn't interested in you."
        l "{i}Now that he mentions it... He never even talked to me yesterday."
        ed "But you changed my opinion. Even though you still reek of timidity, you at least have the courage to try this out. I must commend you for that."
        ed "However..."
        ed "Don't think you're fully accepted just yet. I still need to see what you can do."
        ed "If you're no good, then we'll just have to look for someone else."
        l "I understand."
        ed "Good."
        ed "Now, get ready and join the rest with their warm-up. Just follow your captain's orders for now."
        l "I got it, sir!"
        ed "Don't call me sir. Just coach or Ed is fine."
        l "S-sure!"
        scene ep6_490
        with dissolve
        ed "{i}I might be more strict than usual, but I have to do it in order to bring out what she can do."
        ed "{i}There's a lot of schools that will be a challenge to us. We need to work twice as hard this year."
        stop music fadeout 2

        scene black
        with dissolve
        with fadeq

        "Thirty minutes later..."

        scene black
        with dissolve
        with fadeq

        play music 'audio/Damage.mp3' fadein 2
        scene ep6_491
        with dissolve
        l "*huff* *huff* *huff*"
        scene ep6_492
        with dissolve
        ca "Stand up straight, Lily. It's easier for you to breathe that way."
        ca "Besides, you don't want coach to yell at you this early on. Haha."
        scene ep6_493
        with dissolve
        l "Oh, s-sorry!"
        ca "No need to apologize, just make sure to remember it all the time.."
        l "I got it."
        l "But why is it easier to breathe when standing straight? I often see people slouching when they're out of breath."
        scene ep6_494
        with dissolve
        ca "It's fine to slouch, but here in Track and Field, it's different. We use our lungs almost non-stop, which puts a huge stress on them."
        ca "When you stand up straight, the air passes into your lungs with less effort. The blood circulates better that way as well."
        ca "You might not notice it at the moment, but trust me, when you do your workouts."
        ca "You'll feel it."
        l "I see..."
        play sound 'audio/woosh.mp3'
        scene ep6_495
        l "I'll take note!"
        ca "Aha haa... You don't have to salute just because I'm the captain, you know?"
        scene ep6_496
        with dissolve
        l "I'm sorry, I'm sorry."
        ca "Jeez..."
        scene ep6_497
        with dissolve
        l "By the way, was that the usual jogging pace? It's very fast, I could barely keep up."
        ca "You mean the five-lap warm-up? No-"
        scene ep6_498
        with dissolve
        an "No it's not! We're lucky our captain is the one holding the pace. It gets way worse when the longest runners are in charge!"
        an "Those damn stamina monsters!"
        scene ep6_499
        with dissolve
        ni "Hey, I heard my name. Ahaha!"
        an "Yes! We're talking about you!"
        ni "There, there... I'll buy you popsicles later too, don't worry."
        scene ep6_500
        with dissolve
        an "Really~?"
        ca "Why the heck do you love popsicles that much?"
        scene ep6_501
        with dissolve
        an "I dunno? I just love them!"
        an "But hasn't coach given us lighter workouts in the past few days? What's up with him?"
        ca "You always ask for harder training, this is getting scary, you know that?"
        ca "But you guys better prepare yourselves. I know very well that something's up if coach is treating us like this."
        scene ep6_502
        with dissolve
        ed "Alright! Huddle up, everyone!"
        scene ep6_503
        with dissolve
        ed "How's the warm-up? You weren't slacking just because it was a warm-up, were you?"
        scene ep6_504
        with dissolve
        an "You're the one who's making us slack, Ed..."
        ca "Hey..."
        ed "Well, don't worry. I'll give you guys what you want tomorrow."
        ev "Hrm...!!"
        scene ep6_505
        with dissolve
        an "Eek! Why are you all looking at me like you want to kill me?!"
        scene ep6_506
        with dissolve
        ed "Relax, girls. That's what I'm intending to do. You might have noticed a slight drop in the difficulty of your workouts, and that was to not stiffen your body for the upcoming regimen."
        ca "See? I called it."
        ed "For the next five days, your training will slowly get harder and harder."
        an "Nice! Now we're talking!"
        ed "Don't expect it to be the same as before. The other schools are bringing out their big guns and have recruited overseas students."
        l "Wait, is that even allowed?"
        scene ep6_507
        with dissolve
        an "Actually, yes. It is quite normal, in fact."
        an "All schools have the freedom to do so. As long as those recruits are actually enrolled with the school they represent, nobody can complain."
        an "If you haven't noticed yet, Nisha and Natasha come from a different country as well."
        l "I see..."
        scene ep6_508
        with dissolve
        ed "Well said, Anne."
        scene ep6_509
        with dissolve
        ed "If only the rest of your teammates were the same as you... *sighs*"
        scene ep6_510
        with dissolve
        na "What's the difference? I mean... duh...! The only thing that sets her apart from the rest of us is that she's an airhead."
        scene ep6_511
        with dissolve
        an "Whaaat did you saaay?! You wanna go, hrrmmnn...?"
        l "Should you guys actually be fighting at this time?"
        an "You really get on my nerves as soon as you open your mouth, Natasha! Hrmmnn...!"
        na "What? Everyone calls you that too, but you don't get upset. Why me?"
        an "You're different because you really mean it!"
        na "Well... It's the truth."
        play sound 'audio/woosh.mp3'
        scene ep6_512
        an "See?!"
        ed "This is no time for chatter."
        ed "All of you proceed to the 50-meters mark and give me 5 rounds."
        scene ep6_513
        with dissolve
        an "Wait, that's all?"
        ed "That's all of it. Take your time for today, tomorrow will be another story."
        an "OK, we got it, Ed."
        scene ep6_514
        with dissolve
        ed "And Anne..."
        an "Hm? Yes, coach?"
        ed "I need your help with Lily later."
        scene ep6_515
        with dissolve
        an "Heeh... Are we doing it?"
        l "Uhm... Doing what?"
        an "*giggles* You'll see, you'll see!"
        scene ep6_516
        with dissolve
        miw "We didn't have the opportunity to talk much yesterday, so pardon my late introduction."
        miw "Your name is Lily, right? My name is Miwa, I'm in hurdles. Nice to meet you, Lily~!"
        l "No worries. Nice to meet you too, Miwa."
        scene ep6_517
        with dissolve
        miw "Everyone, You should formally introduce yourselves too~!"
        scene ep6_518
        with dissolve
        lid "Hey, there. The name's Lidia, I am also in hurdles alongside Miwa."
        lid "People always tell me that I smile all the time, but I'm actually not. That's just the shape of my lips. Nice to meet you."
        l "Uhm... That's weird."
        scene ep6_519
        with dissolve
        na "Yo, Natasha here. I'm a distance runner. Glad you could be with the team."
        na "Don't get my personality wrong, I'm just specially rude to Anne."
        an "Damn you!"
        scene ep6_520
        with dissolve
        ni "You probably already know me, but I'm Nisha. Like my sister Natasha, I'm running the longest events. Nice to meet you, Lily."
        scene ep6_521
        with dissolve
        br "Brook at your service, ma'am! I'm one of the best middle runners on the team! Glad to see you come back, Lily!"
        ca "There's only the two of us in middles, Brook."
        scene ep6_522
        with dissolve
        br "You don't have to make it obvious that you're better than me, cap'n!"
        scene ep6_523
        with dissolve
        ca "Anyway, you already know me, but my name is Cathy and I'm your captain. Sorry that I judged you right away. I was totally wrong."
        scene ep6_524
        with dissolve
        l "Mhm! Nice to meet you guys."
        l "But I have a quick question."
        ca "Just ask away, Lily. Don't hold back."
        l "Uhm... Aren't there supposed to be other events here? Like that thing where you throw a metal ball and also those jumping events I saw on TV."
        ca "Oh, the field events, you mean?"
        ca "We do have them too. But they're on a different team with a different coach."
        ca "They have their own training ground as well, so you won't see them until the competitions."
        l "Oh... I see now."
        scene ep6_525
        with dissolve
        an "Let's go first, Lily."
        l "Eh? First?"
        an "Yep! We usually do it in pairs so there's a challenge to it."
        an "Start us up, please, captain!"
        scene ep6_526
        with dissolve
        ca "Alright."
        ca "Are you ready, Lily?"
        l "Uhm... We're just running to the finish line, right?"
        ca "Yeah. Don't feel pressured, this is just a workout. There's no winning or losing here."
        l "Okay, then I'm ready."
        an "Do a starting pose, Lily. Since we don't use a starting block right now, find a pose that you're comfortable on your feet with."
        an "Any will do, actually."
        an "When you feel that pose grips well, then just say 'Set', and Cathy will shout the 'Go' signal."
        an "Also try to run right when she shouts. Not before, not after. You got it?"
        l "I understand."
        scene ep6_527
        with dissolve
        l "{i}A starting pose, huh... I think I saw one when I researched Track and Field last night..."
        scene ep6_528
        with dissolve
        l "......"
        l "{i}This feels good..."
        ca "{i}Ahh... The classic running pose. Good choice."
        scene ep6_529
        with dissolve
        l "Set!"
        scene ep6_530
        with dissolve
        ca "Go!"
        scene ep6_531
        with dissolve
        l "{i}Urk!"
        l "{i}She's... so fast!"
        scene ep6_532
        with dissolve
        an "Alright~!!"
        scene ep6_533
        with dissolve
        na "Hey, hey. What are you doing beating the newbie, huh, Anne?"
        ev "Yeah, yeah! What an absolute showoff!"
        scene ep6_534
        with dissolve
        ed "Aha haaa..."
        scene ep6_535
        with dissolve
        an "I'm a sprinter! What do you slugs expect?!"
        l "*huff* *huff*"
        scene ep6_536
        with dissolve
        an "Hey, Lily."
        scene ep6_537
        with dissolve
        l "Hm?"
        an "*tap* *tap*"
        scene ep6_538
        with dissolve
        l "Ah, right. No slouching."
        an "Good. Always raise your head up whenever you finish a run. Try to make it a habit from now on."
        ed "Come here for a moment, Lily."
        scene ep6_539
        with dissolve
        l "Yes, coach?"
        scene ep6_540
        with dissolve
        ed "Throw your hands up like this every time you run. What you did just now makes it harder for you to move forward."
        ed "Don't throw it high, just target it right below your chin or in front of your face."
        scene ep6_541
        with dissolve
        ed "And when sprinting, don't clench your fists. That makes your hands heavier to throw."
        ed "Just keep both of your hands relaxed and you'll see what I mean."
        l "Copy!"
        scene ep6_542
        with dissolve
        an "Alright, you monsters..."
        scene ep6_543
        an "Go!"
        scene ep6_544
        with dissolve
        $ renpy.pause()
        scene ep6_545
        an "Go!"
        scene ep6_546
        with dissolve
        $ renpy.pause()
        scene ep6_547
        an "Go!"
        scene ep6_548
        with dissolve
        an "Hey, Natasha! Put more effort in your sprints!"
        na "Huuuuh?!! Why don't you say that again in my face, you little bitch?!!"
        scene ep6_549
        with dissolve
        l "Are you two usually like that?"
        an "Well, yeah... Our personalities just always collide with each other's."
        an "But don't worry, we never get to a physical fight or anything like that. Haha!"
        l "That's good to know."
        scene ep6_550
        with dissolve
        an "Are you ready to go again?"
        l "Yeah, four more rounds, right?"
        an "Yep!"
        scene ep6_551
        with dissolve
        l "Alright, I'm ready."
        scene ep6_552
        with dissolve
        an "Your call, Lily."
        l "Set!"
        scene black
        an "Go~!"
        stop music fadeout 2

        scene black
        with dissolve
        with fadeq

        "Fifteen minutes later..."

        scene black
        with dissolve
        with fadeq

        play music 'audio/Faster.mp3'
        scene ep6_553
        with dissolve
        l "*huff* *huff* *huff*"
        an "All tired now?"
        l "Yeah, but I'm still fine."
        an "Heeeh... Not bad!"
        scene ep6_554
        with dissolve
        an "Ed~! It's time!"
        l "Huh?"
        ed "Lily, Cathy, and Anne, come to me. The rest of you, go ahead and start your cool down, that will be all for today."
        scene ep6_555
        with dissolve
        ed "It's time for your tryout. Get ready."
        l "Okay, but... What should I do this time?"
        ed "Since the only slot we have left is the sprints, I would like to see what you can do at that distance."
        ed "I'll let you run a single 100 meter dash and time it out."
        l "A-alright..."
        scene ep6_556
        with dissolve
        ed "Take her to the starting line, Anne. And take this."
        ed "It's already loaded with blank rounds."
        an "Leave it to me."
        scene ep6_557
        with dissolve
        ed "You time her out, Cathy. I would like to focus on her performance."
        ca "You're usually the one timing the applicants out, coach. What's the problem?"
        ed "Have you noticed the way she throws her legs after I told her to relax and open up her hands earlier?"
        ca "I don't think so. I wasn't paying that much attention to her."
        ed "It was perfect."
        ca "Really?"
        ed "Do you know anything about her history? Any physical activities or something like that?"
        ca "Uhm... Not that I know of, coach. All I know is that she has a mountain bike, so she might be using it every day for travel."
        scene ep6_558
        with dissolve
        ca "Wait..."
        ed "Yeah... Her legs are used to pedaling. So much so that she applies it with the way she runs."
        ed "She has so much leg power, but it's getting wasted due to her overall bad running form."
        ca "Interesting..."
        scene ep6_559
        with dissolve
        an "Oh yeah~! Let's go, Lily!"
        l "I'm... honestly not ready for this..."
        an "Are you nervous?"
        l "Yeah, my hands are actually shaking, yet my legs are calm. I'm feeling weird right now."
        an "That's quite normal. Even we get nervous for time trials."
        an "Just don't forget to breathe, okay?"
        scene ep6_560
        with dissolve
        l "I got it."
        scene ep6_561
        with dissolve
        an "Now then, for the real starting position..."
        an "Try and copy me."
        scene ep6_562
        with dissolve
        l "Like this?"
        an "Yeah, not bad at all! It's much more comfortable with a starting block, but... Oh well..."
        an "Let's just make do for now."
        an "Next is the 'Set' pose."
        scene ep6_563
        with dissolve
        an "It's easy. You'll basically just lift your butt up like this..."
        an "Then, put all your lower body's weight to your left leg to kick you off when the gun fires."
        l "Alright, I'll see what I can do."
        an "Stand up for now, Lily. You don't want to stay in that position for a long time. Ahahah!"
        l "Sure."
        scene ep6_564
        with dissolve
        an "One last tip."
        an "After I yell 'Set' and you lift your butt up, inhale as much as you can through your nose within that one second. Then let it all out through your mouth after the gun fires."
        l "So, basically exhale it at the same time when I go for the run, right?"
        an "Exactly! You really do learn fast, Lily!"
        l "But what about that one second you mentioned just now?"
        an "Ahh... that's the time interval between 'Set' and 'Go' right before you run."
        an "The first one is usually 'On your marks', that's when you do your starting position from standing up."
        an "Umpires will check your pose and make sure your hands don't go beyond the starting line."
        an "Then, there's the 'Set', I told you what it is already."
        an "Lastly, the 'Go', or the gun fires."
        an "Those two only have a one-second interval. When 'Ready' is shouted, there's no turning back. Everything will be up to you at that point."
        l "Alright, let's get this done, then."
        scene ep6_565
        with dissolve
        an "Hey, Ed! We're ready~!"
        scene ep6_566
        with dissolve
        an "That's our go signal."
        scene ep6_567
        with dissolve
        an "......"
        an "Lily?"
        scene ep6_568
        with dissolve
        l "Hm?"
        an "Breathe. You got me?"
        scene ep6_569
        with dissolve
        l "*smiles* Roger!"
        an "Good."
        an "Are you all set?"
        l "Yeah, let's do this!"
        scene ep6_570
        with dissolve
        an "Alright, Lily. Get ready..."
        an "On your mark!"
        scene ep6_571
        with dissolve
        $ renpy.pause()
        scene ep6_572
        with dissolve
        an "......"
        scene ep6_573
        with dissolve
        an "......"
        scene ep6_574
        with dissolve
        an "Set!"
        scene ep6_575
        with dissolve
        $ renpy.pause()
        scene ep6_576
        with dissolve
        l "*inhales deeply*"
        play sound 'audio/startinggun.mp3'
        scene ep6_577
        with hpunch
        "*gun fires*"
        scene ep6_578
        with dissolve
        an "Whoa~! Hey there, Miss fast starter!"
        an "Her overall form is still as bad, though... I'm sure coach noticed that already."
        scene ep6_579
        with dissolve
        br "Wohohooo~! Look at those legs throw! Let's go, baby!"
        lid "Is that the timid girl we met yesterday? That form tells me otherwise, though."
        scene ep6_580
        with dissolve
        miw "Unfortunately, it looks like she's taking it seriously to me!"
        scene ep6_581
        with dissolve
        ca "*click*"
        scene ep6_582
        with dissolve
        ca "......"
        scene ep6_583
        with dissolve
        ca "Exactly 16 seconds, coach!"
        scene ep6_584
        with dissolve
        l "*huff* *huff*"
        scene ep6_585
        with dissolve
        l "Is it... *huff*"
        l "...bad?"
        ca "Well..."
        scene ep6_586
        with dissolve
        ed "It is bad, yes."
        scene ep6_587
        with dissolve
        ed "But..."
        ca "Hm?"
        scene ep6_588
        with dissolve
        ed "Can you go for another round, young lady?"
        l "Yeah... Yeah, I think I still can... I'm just out of breath at the moment."
        scene ep6_589
        with dissolve
        ed "Hey, Brook!"
        scene ep6_590
        with dissolve
        br "Yes, coach?"
        ed "Can you let Lily borrow your spikes for a while? We'll do a re-try."
        br "Sure! Hold on..."
        scene ep6_591
        with dissolve
        br "Here!"
        br "Since Anne's shoes fit you, I'm pretty sure these will be a good fit too."
        br "We both have the same size feet despite me being taller. I have small feet. Haha!"
        l "Thanks, Brook."
        br "No worries. Give it your all this time around."
        l "Mhm!"

        scene black
        with dissolve
        with fadeq

        scene ep6_592
        with dissolve
        ed "How do they feel?"
        l "Ehmm... They feel weird..."
        br "Hahaha! How nostalgic this is!"
        br "I had almost the same reaction when I first wore my spikes! It feels weird at first, but they will help you a lot, trust me."
        br "Try taking a jog and see for yourself."
        scene ep6_593
        with dissolve
        l "......"
        l "They... grip through the rubber. It's not slippery anymore. Although my heels are falling flat, there's no bounce at all."
        scene ep6_594
        with dissolve
        ed "And that's the purpose of the spike shoes."
        ed "Sprinters never use their heels, only their toes."
        ed "On this re-try, I want you to try and run tiptoe. We'll still do the same and time you out."
        ed "Listen to the gunfire, do you understand?"
        l "I got it, coach."
        ed "Good. Now, go back to Anne."
        scene ep6_595
        with dissolve
        l "Roger!"
        ed "Is saluting a mannerism of yours, or something? You don't have to do that."
        scene ep6_596
        with dissolve
        l "Ahaha... Yeah, my father used to work in the military. I got it from him."
        ed "I see..."
        ed "This will be your last run, Lily. Give it your all."
        l "Understood!"
        scene ep6_597
        with dissolve
        ca "Why did you let her use spikes, coach? Won't her feet be in shock with the sudden change of bounce?"
        ca "I know how it felt when I first used spikes for a time trial."
        scene ep6_598
        with dissolve
        ed "We'll think about that later. For now..."
        ed "I really want to see her leg power. Something with the way she runs seems to be off."
        ed "We'll see how that changes now that she has a better grip."
        br "......"
        scene ep6_599
        with dissolve
        ed "Don't look at me like that, Brook. I know what you want to say."
        br "Yeah, you're one heck of a sadist, coach. You're scary..."
        scene ep6_600
        with dissolve
        an "Hey, look at that~! The runner's partner! The legendary spikes!"
        scene ep6_601
        with dissolve
        an "Ed, you bastard! Hahaha!"
        l "Hm? Why? What's wrong?"
        scene ep6_602
        with dissolve
        an "Well... Coach obviously wants to get a performance out of you. It's not ideal to suddenly use spikes for the first time, you know?"
        an "The sudden change of bounce on your feet by changing from your usual running shoes to spike shoes will probably cause a bit of stress to your feet after this."
        an "But it will improve your performance, that's for sure."
        l "If it will give me a better time, I won't complain."
        an "Heeh... Where's the 'you' from yesterday?"
        stop music fadeout 2

        scene black
        with dissolve
        with fadeq

        play music 'audio/Frustration.mp3'
        scene ep6_603
        with dissolve
        l "*exhales deeply*..."
        scene ep6_604
        with dissolve
        l "{i}My vision is clear..."
        l "{i}I can see the finish line from here..."
        l "{i}I can feel the pressure, but I'm not nervous anymore..."
        l "{i}I'm a bit tired, yet my body feels so light..."
        l "{i}I can even hear my heart beat..."
        l "{i}Is this because of the spike shoes?"
        an "Set!"
        scene ep6_605
        with dissolve
        l "{i}I don't know..."
        l "{i}At this moment... I just want to..."
        play sound 'audio/startinggun.mp3'
        scene ep6_606
        with hpunch
        "*gun fires*"
        l "{i}Run..."
        scene ep6_607
        with dissolve
        an "Holy Jesus!"
        scene ep6_608
        with dissolve
        an "Hold on, I need to know her time!"
        scene ep6_609
        with dissolve
        ni "Huh?"
        na "Well? I guess we have another sprinter, huh?"
        lid "Yeah, it looks like it."
        scene ep6_610
        with dissolve
        ed "That leg and arm throw, they're perfect. Her head wobbles a bit, but that can be fixed."
        ed "It looks like we found a diamond in the rough, huh?"
        scene ep6_611
        with dissolve
        ca "*click*"
        scene ep6_612
        with dissolve
        ca "Whoa~! It's..."
        ca "It's 14.2 seconds, coach!"
        br "Wait, hold on... That much?!"
        br "Are you sure you timed her right, Cap'n?"
        scene ep6_613
        with dissolve
        l "*huff* *huff* *huff*"
        l "Aaahh!"
        ca "Yeah... I timed her right when the gun fired and when she reached the finish line."
        ca "The stopwatch won't be lying either..."
        br "You cheeky little..."
        br "Is this really a girl who hasn't been on a track before?!"
        scene ep6_614
        with dissolve
        an "Hey, Cath~! How much is it?"
        l "I want to know too."
        scene ep6_615
        with dissolve
        ca "Look..."
        an "14.2~?!"
        an "How much was her first one?"
        ca "16 seconds flat."
        scene ep6_616
        with dissolve
        play sound 'audio/whistle.mp3'
        an "*whistles*"
        an "Almost two seconds away, huh? Friggin' hell, Lily!"
        an "Are you sure this is your first time running?"
        l "Yes, I'm sure of that. I told you, I never had any interest in sports before."
        scene ep6_617
        with dissolve
        ed "You should now. 14.2 seconds on your first time? It's called potential. There's is so much potential in you."
        l "Is it... good?"
        an "Huh?! You don't even need to ask that, you know?!"
        ed "Anne's current best is 12.3 seconds."
        ed "Each second is already a huge gap, every millisecond counts."
        ed "A millisecond of improvement requires rigorous training. That's how it is in sprints."
        ed "And you're pretty much just 2 seconds away from her."
        scene ep6_618
        with dissolve
        an "Well? It looks like we're going to be partners from now on~! *giggles*"
        scene ep6_619
        with dissolve
        ed "Let me officially welcome you to the Track and Field club, Lily."
        ed "Never give up and work with us on our way to the top."
        stop music fadeout 2

        scene black
        with dissolve
        with fadeq

        "A week later..."

        scene black
        with dissolve
        with fadeq

        play music 'audio/EnergizedMorning.mp3' fadein 2
        scene ep6_620
        with dissolve
        $ renpy.pause()
        scene ep6_621
        with dissolve
        $ renpy.pause()
        scene ep6_622
        with dissolve
        l"{i}Alright! Let's go!"
        play sound 'audio/ridebike_righttoleft.mp3'
        scene ep6_623
        with dissolve
        l "{i}To the track~!!"
        scene black
        with Dissolve(2.0)
        scene ep6_624
        with dissolve
        l "And that's how I was introduced to the Track and Field club."
        l "I changed so much after that day — all the timidity in me slowly faded away. So sports is basically half of what I am right now."
        l "It was really fun! Although, coach's training was still spartan as heck!"
        scene ep6_625
        with dissolve
        mc "That's for sure! I had so much fun listening to it that it makes me want to run too! Haha!"
        l "I'm glad you liked it."
        l "There's still more to it though. But..."
        l "We can talk about it some other time. The next few days will be a bit busy for me, by the way, so I may have to leave early."
        mc "Sure! I can do the closing by myself, you take care of your studies first, don't worry about me!"
        l "Thanks, [mc]."
        mc "I have a question though..."
        l "Yes? What is it?"
        mc "Where are your teammates now? Especially the one you mentioned the most."
        mc "Her name is Anne, was it? You told me she's your best friend."
        scene ep6_626
        with dissolve
        l "Well... She {b}was{/b} my best friend."
        mc "Huh? What do you mean?"
        l "A lot of things happened after that day."
        l "Life always has sorrow in exchange for the happiness it gives you, that's what I believe."
        scene ep6_625
        with dissolve
        l "But like I said, we can talk about it more next time. I have to hurry to the academy now, or I'll be late for my courses and reviews."
        mc "Ah, sure, Lily! We're done with all the cleaning anyways, let's close up shop."
        stop music fadeout 2

        scene black
        with Dissolve(2.0)
        label lilyannepause:
        if _in_replay:
            $ name = persistent.gallery_name
        scene lilyannepause
        with dissolve
        $ renpy.pause()
        $ renpy.end_replay()
        play sound 'audio/gamepause.mp3'
        show title at move_slide
        with flash
        $ renpy.notify(imageunlock)
        $ renpy.pause()

    scene black
    with dissolve
    with fadeq

    "Late at night..."

    scene black
    with dissolve
    with fadeq

    play music 'audio/MachineryOfWar.mp3'
    scene ep6_627
    with dissolve
    m "......"
    scene ep6_628
    with dissolve
    m "Owl, do you copy?"
    cl "I'm listening."
    m "The tangos have arrived. Your intel was right, they're in front of their house."
    cl "You know what to do."
    scene ep6_629
    with dissolve
    m "Execute them, right?"
    cl "No, don't kill them. We don't want unnecessary bloodshed. Make sure they don't notice you, how copy, over?"
    m "Affirmative, moving on targets, over."
    scene ep6_630
    with dissolve
    $ renpy.pause()
    scene ep6_631
    with Dissolve(0.2)
    play sound 'audio/kick_light.mp3'
    scene ep6_632
    with Dissolve(0.2)
    scene ep6_633
    with Dissolve(0.2)
    scene ep6_634
    with Dissolve(0.2)
    play sound 'audio/thud.mp3'
    scene ep6_635
    with dissolve
    play sound 'audio/woosh2.mp3'
    scene ep6_636
    with Dissolve(0.2)
    play sound 'audio/kick_heavy.mp3'
    scene ep6_637
    with dissolve
    scene ep6_638
    with dissolve
    play sound 'audio/thud.mp3'
    scene ep6_639
    with Dissolve(1.0)
    m "Good night..."
    scene ep6_640
    with dissolve
    m "......"
    m "Owl, this is Fang, targets neutralized, they are asleep."
    cl "Copy, good job. Use their vehicle and take them somewhere far away. Copy?"
    m "Copy that."
    m "...Who are these people, by the way?"
    cl "Spies, we don't want them all over the place."
    m "Pests, you mean?"
    cl "You don't have to make it sound weird, you know?"
    cl "Anyway, get out of there before anybody sees you, over."
    m "Wilco, over."
    cl "Roger, out."
    stop music fadeout 2

    scene black
    with dissolve
    with fade

    play music 'audio/Slowevening.mp3'
    scene ep6_641
    with dissolve
    yt "Ahh... Jeez... Here it goes again! I just can't sleep now that I'm thinking of all the problems I have!"
    yt "I'm wondering about actually staying at the burger shack at this point."
    yt "All this shit just haunts me like I'm in a horror movie or something."
    yt "*sighs*... That's a bad analogy..."
    yt "I wonder if we still have some cans of beer in the fridge. A couple cans might help me sleep."

    scene black
    with dissolve
    with fadeq

    scene ep6_642
    with dissolve
    yt "Oh, sweet! We still have some!"
    yt "Well, thinking back... We mostly drank wine and almost never touched these."
    yt "Gotta get classy, eh?"
    scene ep6_643
    with dissolve
    yt "...Let's go to the veranda."

    scene black
    with dissolve
    with fadeq

    scene ep6_644
    with dissolve
    mc "Hm?"
    mc "Emma?"
    yt "I couldn't forget about that kiss last night, that was really mind-boggling."
    yt "Let's just pretend that didn't happen... At least for now..."
    scene ep6_645
    with dissolve
    mc "It's pretty late, what are you still doing outside? Don't tell me you couldn't sleep?"
    e "Yes, I can't."
    scene ep6_646
    with dissolve
    mc "Hmm..."
    mc "......"
    scene ep6_647
    with dissolve
    mc "How was your case, by the way? Solved it yet?"
    e "That's the reason I couldn't sleep."
    scene ep6_648
    with dissolve
    mc "Huh?"
    e "I can't sleep when I have things left unfinished."
    mc "......"
    mc "Let me guess..."
    mc "The suspect won't admit the truth, right?"
    e "Yeah..."
    yt "She almost speaks like a normal person when it comes to her work."
    scene ep6_649
    with dissolve
    mc "That's usually how it works. People will tend to deny the bad things they've done."
    mc "No matter their age, from children to adults, that's just how a person's mind behaves."
    mc "Unless you're a devout worshiper of justice, then it might be a different story."
    mc "I myself am no exception to that."
    scene ep6_650
    with dissolve
    e "......"
    e "You have a point."
    mc "Well? What are you going to do now? Got some plans up your sleeve?"
    mc "You're pretty smart, you'll eventually solve it anyways."
    yt "I just couldn't understand why you came here just for me to marry your friend, though. It's just not a thing you would do."
    e "I'm not a genius, but I'm working on it."
    scene ep6_651
    with dissolve
    mc "And staying up this late won't really help you, anyway. A brain works better when you have enough sleep."
    mc "Considering you wake up early and get home late, it'll be only a matter of time till you burn yourself out."
    e "Mhm."
    scene ep6_652
    with dissolve
    mc "......"
    e "......"
    yt "Damn... This is getting awkward."
    scene ep6_653
    with dissolve
    mc "You do drink, right? Here's a can of beer if you want it."
    e "......"
    scene ep6_654
    with dissolve
    e "Thanks..."
    e "......"
    scene ep6_655
    with dissolve
    e "What did you mean... you were no exception?"
    mc "Hm?"
    scene ep6_656
    with dissolve
    mc "Well... The truth is... There are a lot of terrible things I've done in the past... I kept it quiet and denied it to myself."
    e "Like, when you confessed to Aine?"
    scene ep6_657
    with dissolve
    mc "Hmm... Yeah, I guess you could include that."
    mc "I sometimes close my eyes and all I can think about is how I could have done things differently, changed the outcomes, been a better man."
    mc "I forced myself to believe that the things I've done were right, but... then, I came to understand a lot of things there were about life..."
    scene ep6_658
    with dissolve
    mc "...I started to doubt myself. Then I realized that I'm just one hell of an asshole."
    mc "There comes a point where the faces of the people you wronged become too many to recognize them all in a dream..."
    mc "They merge and they change... No longer recognizable individuals, but always here as a reminder of what you did or didn't do."
    mc "A memento of past mistakes I guess? A burden to carry, like when I confessed to Aine as you mentioned."
    scene ep6_659
    with dissolve
    mc "Man... I think I'm going crazy. Aha haaa..."
    e "Yeah... Why did you do it if you had a bad feeling in the first place, then?"
    stop music fadeout 2
    scene ep6_660
    with dissolve
    mc "......"
    mc "I..."
    mc "Did that to escape from the past..."
    scene ep6_661
    with hpunch
    e "...!!!"
    play music 'audio/SoMuchForForever.mp3' fadein 2
    scene ep6_662
    with dissolve
    e "What..."
    scene ep6_663
    with dissolve
    e "...did you..."
    mc "I did like Aine, don't get me wrong."
    scene ep6_664
    with dissolve
    mc "But, you know..."
    mc "I met a girl when I was a kid..."
    mc "She was annoying at first, but when we got to know each other and wrote letters back and forth, I came to fall in love with her."
    mc "And I know that she loved me too..."
    mc "I didn't have friends back then, so I valued her more than anything... and eventually, she became the world to me at such a young age."
    mc "There's nothing certain in this world, I know... But I was certain that I would marry her when we grew up."
    mc "Although... I guess that was just the kid in me talking..."
    mc "But I made a promise... A promise that I was willing to live up to, because I loved her..."
    scene ep6_665
    with dissolve
    mc "......"
    mc "Those happy times didn't last long..."
    mc "Life took me away from her."
    mc "I made a promise that I would come back for her... But lived overseas for more than a decade."
    mc "I wanted to come back as soon as possible. But what could I have done? I was just a snotty little brat."
    mc "It was impossible for me to live independently from Klara at that age."
    mc "It felt like a huge part of me was missing the fact that I couldn't even see her at least one more time, even after all those years."
    mc "I thought it couldn't get any more painful..."
    mc "But as problems and responsibilities stacked onto my shoulders, it couldn't help but take my mind off of her... and my memories of that time slowly faded away over the years."
    scene ep6_666
    with dissolve
    mc "I..."
    mc "I tried my best to recall everything, to keep my memories of her."
    mc "I wanted her to touch my face one more time. I wanted to hug her, to be there for her. I wanted her by my side."
    mc "That comfortable feeling when I was on her lap, I missed everything. I missed her so much..."
    scene ep6_667
    with dissolve
    e "......"
    scene ep6_668
    with dissolve
    mc "We finally came back just a few months before I started my final year in high school..."
    mc "...And the first thing I did was to rush over to her house, thinking that she might still be there just waiting for me to return."
    mc "I was filled with excitement. I was so eager to see her again."
    mc "I wondered what she looked like after years without being able to see her. I wondered what her voice would sound like."
    mc "I wanted to fill those missing memories of her. And by seeing her once more, I would finally remember everything."
    mc "But that eagerness and excitement turned into misery when I found out that she was no longer there."
    mc "I felt my heart turn into stone. I couldn't feel anything and went down on my knees."
    mc "I wanted to cry my heart out, but nothing came out of my eyes. Not even a single tear... I was... fucking numb."
    mc "A lot of thoughts came to my mind."
    mc "Did she forget about me? Did she move on?"
    mc "I don't know... And I can't blame her."
    mc "All I know is that I couldn't keep my promise..."
    scene ep6_669
    with dissolve
    e "{i}He... did come back for me?"
    mc "Right now... All I have left are these vague memories of her..."
    e "{i}If only..."
    e "{i}If only... I waited a bit longer..."
    mc "Ahh..."
    mc "Damn it, I can't even remember what she exactly looks like. Let alone her name."
    scene ep6_670
    with dissolve
    e "{i}That's enough..."
    mc "I'm just... a piece of trash who couldn't keep his promise to the girl he loved."
    e "{i}That's enough... Please..."
    e "{i}It's... all my fault..."
    e "{i}So please, wipe those tears away..."
    scene ep6_671
    with dissolve
    mc "Argh! This is why I don't want to recall that time! I just get too emotional!"
    scene ep6_672
    with dissolve
    e "...Do you... still miss her?"
    scene ep6_673
    with dissolve
    mc "Yes... I still want to see her. I want to say sorry. I want to know if she's doing fine. I want to ask if she still remembers me."
    mc "There's so, so much that I want to say to her. I... still want to keep my promise..."
    mc "But..."
    mc "But I let her down and confessed to someone else so I could escape from all the pain."
    mc "I'm... such a coward..."
    mc "Now, I'm facing a lot of problems that I don't know what to do with... I probably deserve all this after what I've done."
    scene ep6_674
    with dissolve
    e "{i}I thought... he totally forgot about me..."
    e "{i}Now that he told me what happened... This is just... too painful..."
    e "{i}Because of that one wrong decision, our lives turned out like this..."
    e "{i}It's just... so unfair..."
    e "{i}But even so..."
    scene ep6_675
    with dissolve
    e "*clench*"
    e "{i}Even just this one time..."
    e "{i}With all the courage I have..."
    e "{i}I..."
    e "{i}...want to hug him..."
    scene ep6_676
    with dissolve
    mc "Aha haaa... Man... Why am I even telling you all-"
    scene ep6_677
    with dissolve
    mc "...!!!"
    scene ep6_678
    with dissolve
    e "{i}Don't ever blame yourself. Knowing that you came back for me is enough."
    e "{i}That's all I wanted to know..."
    e "{i}I deeply regret my decision to move on, but now that we're in this situation, there is no turning back time anymore."
    e "{i}If I can comfort you like this any time you are in distress, then I will never ask for more."
    e "{i}I'm here now... I'll be here for you."
    scene ep6_172
    with flash
    e "{i}It's not bad to wish for it twice, right?"
    e "{i}Then..."
    e "{i}Please let us fix our past mistakes and guide us to the right path this time."
    e "{i}That's all I could ever wish for."
    scene ep6_679
    with dissolve
    e "[mc]...? Can you face me, please?"
    yt "...That is... the first time she called me by my name on her own..."
    yt "Why the heck... am I feeling like I'm going to melt?"
    scene ep6_680
    with dissolve
    mc "Uhm... Why did you hu-"
    scene ep6_681
    with dissolve
    e "Shhh..."
    scene ep6_682
    with dissolve
    e "*touch*"
    mc "Ah..."
    yt "Her hands feel so warm..."
    scene ep6_683
    with dissolve
    e "Stop dwelling on the past anymore. What happened in the past will remain in the past."
    e "You never did anything wrong by confessing to Aine. If your feelings were true, then that's what's important."
    image emmctver:
        "ep6_684.jpg"
        pause 3.0
        "ep6_685.jpg"
        pause .2
        repeat
    show emmctver
    with dissolve
    e "Because the magic of love is that it can happen at any time, or with anyone that you know for a long time or just met for the first time."
    e "Don't ever say that you're an asshole because you were in love."
    e "We always have to move on and find a new beginning at some point. You did not do anything wrong by doing so."
    e "We're just humans, we feel pain. And pain will always tell us to stay away from it."
    e "We all make decisions, but what we make out of the outcomes is what truly matters."
    e "In the end, only then can you fully say if they were good or bad."
    e "So if you have a lot of things to do now, then focus on them."
    e "You said to me that you're not like you were back then, right? Then stand for it."
    e "Be the man that you wanted to be."
    e "As simple as a guy like you is, you can change a person's life."
    e "You may not be rich, you may not be cool like other guys out there. But you are a good person, [mc]. Always remember that."
    yt "Her voice... It's not too loud, but not too quiet either. But every word coming out of her mouth feels like it reaches deep straight to my heart."
    yt "The way she's talking right now is nothing like I've ever heard from her before..."
    yt "What's with me? Why am I feeling like this towards her?"
    e "Wherever that girl is, I'm sure she's all fine. I'm sure she's happy right now."
    e "Although, if there's one thing I'm really certain about... it's that you became a part of her and she will never forget about you."
    scene ep6_686
    with dissolve
    e "*giggles*"
    mc "*thumps*"
    yt "God fucking damn it..."
    scene ep6_687
    with dissolve
    e "I never actually sincerely said 'sorry' to you before."
    scene ep6_688
    with dissolve
    e "So with all the things I did in the past..."
    e "I'm deeply sorry, [mc]. Please forgive me."
    mc "Uhm... Please raise your head, you don't really need to bow, you know?"
    mc "And please stop talking to me so formally."
    scene ep6_689
    with dissolve
    e "I want to make it up to you, so please give me the chance to do so. But... I have no idea what to do right now, so please give me time to think about it."
    mc "No, you should focus on your case first! A job is a job. I'm just here, I won't go anywhere."
    mc "Solve it, and then we have a deal."
    scene ep6_690
    with dissolve
    e "I'll make that piece of shit talk tomorrow then, mark my words."
    mc "So you can swear, huh?"
    scene ep6_691
    with dissolve
    e "...!!!"
    scene ep6_692
    with dissolve
    e "Oh... I'm sorry."
    mc "Let me guess? Gwen's influence, right?"
    e "Mhm. I think so?"
    mc "*sighs* That girl's personality is contagious."
    mc "Anyway, we should go upstairs and sleep. It's getting late."
    e "Okay."
    scene ep6_693
    with dissolve
    mc "......"
    scene ep6_694
    with dissolve
    mc "Uhm... hold on."
    e "Hm?"
    mc "Can you talk to me like you just did from now on?"
    mc "I don't know which is the real you, but you talking like a robot really puts me off."
    scene ep6_695
    with dissolve
    e "......"
    scene ep6_696
    with dissolve
    e "When we're alone, it will be alright."
    mc "Fair enough."
    mc "Alright, let's go."
    scene ep6_697
    with dissolve
    e "Mhm!"
    scene ep6_698
    with dissolve
    yt "I don't know what it is with her, but she made me feel so calm after that emotional talk just now."
    yt "I just wonder why I even told her about it. I never really told anyone about that part of my past."
    yt "I... need to know who this girl is."
    stop music fadeout 2

    scene black
    with dissolve
    with fade

    play music 'audio/InfinityCycle.mp3'
    scene ep6_699
    with dissolve
    e "......"
    e "........."
    a "Uhm... Em? What's wrong? You didn't-"
    e "Did you ever meet that guy before we started all of this?"
    a "To be honest with you, yes. A month before the school year started. Mom told me to do something about him... and..."
    scene ep6_700
    with dissolve
    e "*runs*"
    a "*gasps* Ah, Em! Where are you going?!"

    scene black
    with dissolve
    with fadeq

    scene ep6_701
    with dissolve
    h "Hm? You're home early. Where's Aine?"
    e "......"
    scene ep6_702
    with dissolve
    e "HEERRAAAAAAA!!!!"
    h "Charging head-on towards me? You're making a big mistake, Emma."
    scene ep6_703
    with dissolve
    e "And your biggest mistake was..."
    h "!!!"
    scene ep6_704
    with hpunch
    $ renpy.pause()
    scene ep6_705
    with dissolve
    h "Urk!"
    scene ep6_706
    with dissolve
    e "You should've thought twice about teaching me how to fight!"
    scene ep6_707
    with dissolve
    h "Heh... Nice try."
    scene ep6_708
    with dissolve
    h "Using what we taught you against me? How insolent."
    h "Let me guess..."
    h "He's finally back, isn't he?"
    scene ep6_709
    with dissolve
    e "You knew..."
    e "You knew everything!"
    scene ep6_710
    with dissolve
    h "Oh, of course. I've known him since he was born. I know his family, I know everything about him."
    h "I told you, didn't I?"
    h "Don't ever blame me for what's coming next. Yet, you still chose to be with Aine."
    h "You're very fragile, and that's your biggest weakness. It leads you to the worst decisions."
    e "Fragile?"
    e "I..."
    scene ep6_709
    with dissolve
    e "I waited a whole lot of years for him, I did what I could!"
    e "You didn't want me to serve Aine, you thought I was useless! Then you accepted me so easily after you knew that he's coming back!"
    e "Just what are you planning?"
    e "You never told-"
    scene ep6_710
    with dissolve
    h "Told you about what? That I knew?"
    h "Why would I? What for?"
    h "It's my personal business, you have nothing to do about it. I'm just using you as a tool the way I use any other servants here."
    h "You decided that on your own, Emma. Don't throw your anger at me just because you made the wrong decision."
    h "And now, you're nothing but a caged bird. You did that to yourself."
    scene ep6_711
    with dissolve
    e "You're right... I made the wrong decision. I can't blame you..."
    scene ep6_712
    with dissolve
    e "But we are humans, Hera! We are not your toys to play with for fun!"
    e "You don't have the right to manipulate our feelings for your own personal {b}bullshit{/b}!!"
    e "Do anything that you want to me! Just leave [mc] and Aine out of your ploys!!"
    scene ep6_713
    with dissolve
    h "Oh...? I totally have the right to do anything I want~!"
    h"I own you now, Aine is my daughter, that boy has a debt to pay back to me. I can't find anything invalid about that."
    scene ep6_714
    with dissolve
    e "Y-You!"
    e "You're just...!"
    e "...I don't get why mom even dedicated her entire life for you! She just died for nothing!"
    e "You probably manipulated her like you're doing to us!"
    h "!!!"
    scene ep6_715
    with dissolve
    e "Don't worry... I'm going to tell him everything about this..."
    h "*chuckles* Yeah, do it."
    h "Do it, Emma. Tell them everything, I dare you. And let's see you lose your precious lover... even your beloved friend."
    scene ep6_716
    with dissolve
    e "*glare*"
    scene ep6_717
    with dissolve
    h "Don't give me that look. You know what I'm capable of doing."
    h "Don't get me wrong just because I told you that I still have compassion for you."
    h "If you are going to be a hindrance to my plans, then I won't hesitate to take you away from them..."
    h "Or even worse... kill them."
    h "You're well aware where you are right now, Emma."
    h "My own hands are stained with blood to the point that I can even kill my own daughter, so don't you dare to take us so lightly."
    h "It might just be the worst decision you could come up with."
    h "You're very intelligent, and yet so foolish."
    h "Next time, use your brain... and not your emotions."
    e "......"
    scene ep6_718
    with dissolve
    e "I might as well do that."
    h "*chuckles* Follow my orders, and I promise you... You'll see them both as long as you are alive."
    h "I'm always watching you. As soon as I know that something has changed... Prepare to apologize to yourself."
    h "I can let this slide for once. But next time, it will be my turn to land something on your face."
    h "Mind your manners, Emma. I'm your boss, and you're alive because of me."
    e "......"
    scene ep6_719
    with dissolve
    e "I'm going to stay at the house you {b}gave{/b} us tonight. No one is staying there, right? Tell Aine I'll be back tomorrow."
    h "Fine."
    scene ep6_720
    with dissolve
    h "......"
    h "Tch!"

    scene black
    with dissolve
    with fadeq

    scene ep6_721
    with dissolve
    $ renpy.pause()
    scene ep6_722
    with dissolve
    $ renpy.pause()
    scene ep6_723
    with dissolve
    e "*hics*"
    scene ep6_724
    with dissolve
    e "AAAAAAAAAHHHH~!!!!"
    scene ep6_725
    with dissolve
    e "......HAAAAAAHHHHHH~!!!!"
    e "......"
    scene ep6_726
    with dissolve
    e "{i}I'm... going to destroy you..."
    e "{i}I will take everything that you have and make you beg for mercy..."
    e "{i}Just wait until the time comes that I will do the same to you, Hera. I will make you regret my existence, mark my words..."
    e "{i}For now, I'm going to swallow my pride and pretend that didn't happen."
    scene ep6_727
    with dissolve
    e "{i}But... I can't tell them anything... What should I do now?"
    e "{i}......"
    e "{i}I'm sorry, Aine... [mc]..."
    e "{i}I... Don't want to lose the two of you..."
    e "{i}This is all my fault. It all started with me..."
    e "{i}I'm responsible for this mess... I'll definitely find a way for us to escape, I promise..."
    e "{i}Please... bear with me a little..."
    e "{i}Think, Emy... Think of something..."
    e "*hics*"
    stop music fadeout 2

    scene ep6_728
    with dissolve
    $ renpy.pause()
    scene ep6_729
    with dissolve
    $ renpy.pause()
    scene ep6_730
    with dissolve
    e "......"
    scene ep6_731
    with dissolve
    e "*sighs*..."
    e "{i}Learning the truth from him last night makes me even more hesitant to tell them everything."
    e "{i}Now that I know that he still remembers me, I'm sure he would abandon anything just to make it up to me."
    e "{i}My plan will never work if that happens."
    e "{i}And here I thought that everything would be fine..."
    e "{i}Aww... What do I do now...?"
    e "{i}I'm already cornered..."
    e "{i}If I tell them anything, I'm sure Hera will notice. I can't take her that lightly..."
    e "{i}And if I stay quiet, things won't move on..."
    e "{i}This is just too much for me, I don't know what I should do anymore!"
    e "{i}......"
    e "{i}But, I promised that I would do something for him, so that's probably what I should focus on for now."
    e "{i}What am I going to do though...?"
    e "{i}......"
    scene ep6_732
    with dissolve
    e "*smiles*"
    e "[mc]..."

    scene black
    with dissolve
    with fade

    if (gwenstartdate and skyroute):
        label gwenmorningsex:
        if _in_replay:
            $ name = persistent.gallery_name
        play music 'audio/SlowEvening.mp3'
        scene ep6_733
        with dissolve
        $ renpy.pause()
        scene ep6_734
        with dissolve
        mc "Hng..."
        scene ep6_735
        with dissolve
        mc "Aaahh......"
        scene ep6_736
        with dissolve
        mc "...Huh?"
        yt "Damn... Why is she here and why am I hugging her already?"
        scene ep6_737
        with dissolve
        yt "......"
        yt "*lightly chuckles*..."
        yt "She must have come here just before dawn."
        yt "...Like I'm going to complain anyway."
        scene ep6_738
        with dissolve
        mc "*kisses*"
        mc "Good morning, my lady..."
        scene ep6_739
        with dissolve
        g "Mnnhh~!"
        yt "Umph!"
        yt "Uh-oh... I didn't notice my flag pole down there. She's pretty sensitive reacting to that."
        yt "Uhh, well... she reacted back during high school, so..."
        scene ep6_740
        with dissolve
        g "Mmh?"
        scene ep6_741
        with dissolve
        g "Oh, good morning, [mc]. Sorry, I came in without you knowing."
        mc "All fine by me, and good-"
        scene ep6_742
        with dissolve
        g "Mmnh..."
        scene ep6_743
        with dissolve
        mc "Mmm..."
        scene ep6_744
        with dissolve
        g "*licks*"
        g "Haah~"
        scene ep6_745
        with dissolve
        g "Mnnhh~"
        scene ep6_746
        with dissolve
        g "Ahh..."
        scene ep6_747
        with dissolve
        g "Were you rubbing your meat stick on me, huh? You cheeky handsome guy? Miss me already?"
        menu:
            "I miss you":
                mc "Not really rubbing it — it happened when I kissed you earlier. Hahaaa."
                mc "But yeah, I miss you."
            "Not so much":
                mc "Not really rubbing it — it happened when I kissed you earlier. Hahaaa."
                mc "And naah... Not so much, we see each other almost every day, anyway."

        scene ep6_748
        with dissolve
        g "Jeez..."
        g "Well... rubbing it or not, you're still really hard. It's literally on my pussy right now, you know that?"
        mc "Hmm... I know what you're thinking already, ma'am."
        g "Wanna have a quickie?"
        mc "*chuckles* I knew it..."
        scene ep6_749
        with dissolve
        g "Well...?"
        yt "Oh, boy..."
        menu:
            "Thank you for the breakfast":
                $ gwenskyharem = True
                mc "I'll say thank you for breakfast then."
                mc "But let me play with you a bit first."
                scene ep6_750
                with dissolve
                g "Ahh!"
                scene ep6_751
                with dissolve
                g "Oh, god... I don't know why I like it so much when you do that to me."
                mc "You're pretty aggressive yourself, so why can't I do it to you, as well? Haha!"
                g "Well, you're hitting the right notes there, mister. Keep it up."
                mc "As you wish, my lady."
                scene ep6_752
                with dissolve
                g "MNNHHH~!!"
                g "Oh... shiiit..."
                yt "She's reacting really nicely here too. Smaller breasts are a lot more sensitive, aren't they?"
                scene ep6_753
                with dissolve
                g "[mc]... Take it out. Let me suck it."
                mc "Good idea."
                scene ep6_754
                with dissolve
                g "Mmp..."
                show gwen17
                with dissolve
                g "*sucks*"
                g "*slurps*"
                g "Mnnhh~!"
                g "Mmpp~!"
                mc "Damn, you're really getting into it, Gwen. It feels real good!"
                g "Mmn, hmmn mmp mmnn hrnmnn..."
                mc "Okay... I get it."
                $ renpy.pause()
                scene ep6_755
                with dissolve
                g "*cough* *cough*... *cough*"
                mc "Was that too much?"
                scene ep6_756
                with dissolve
                g "No, I'm just not used to it. But I will be, sooner or later. Haha!"
                g "Let's get to the main event, shall we?"
                scene ep6_757
                with dissolve
                g "Start slowly for now, or I'll smack your head."
                mc "Ahaha! Alright, alright..."
                g "Good!"
                mc "I'm putting it in..."
                scene ep6_758
                with dissolve
                g "Slow..."
                scene ep6_759
                with dissolve
                g "...ly-"
                scene ep6_760
                with dissolve
                g "Aahhh~!"
                scene ep6_761
                with dissolve
                g "F-fuck... have you gotten bigger? What happened to you?"
                mc "Huh? No, I didn't. We just did it the other day too, there's no way I could've gotten bigger. Ahaha!"
                scene ep6_762
                with dissolve
                g "Well? Make me cum, [mc]..."
                mc "It'll be my pleasure!"
                show gwen18
                with dissolve
                $ renpy.pause()
                g "Oof~! Yeah... You're hitting the right spot, [mc]. Keep going."
                mc "Of course."
                $ renpy.pause()
                scene ep6_763
                with dissolve
                s "*deeply exhales*..."
                s "......"
                scene ep6_764
                with dissolve
                s "{i}I should go and cook breakfast now."
                g "{size=-10}Mnnhh~! Ahhh~! Aahhh~!"
                scene ep6_765
                with dissolve
                g "{size=-10}Ohh, fuck~!"
                stop music fadeout 2
                s "{i}Hm? What was that... just now?"
                scene ep6_766
                with dissolve
                s "......"
                scene ep6_767
                with dissolve
                s "{i}Was that... Gwen? It sounded like her voice. But next to this bathroom is... [mc]'s room, right?"
                s "Are they..."
                g "Ahhh...! Aahhh~!!"
                g "Yes, [mc]~! HARDER! HARDER~!!"
                scene ep6_768
                with Dissolve(2.0)
                play music 'audio/Bridges.mp3'
                s "...!!!"
                scene ep6_769
                with hpunch
                s "......"
                s "..........."
                s "................"
                s "{i}When... When did they get so close... that they went all the way... up to this point...?"
                s "{i}I thought..."
                s "{i}I was... the only..."
                scene ep6_770
                with dissolve
                s "......"
                s ".........."
                s "So... this is what heartbreak feels like..."
                s "......"
                s "Oww..."
                s "It..."
                s "...really hurts..."
                s "....."
                s "*hics*"
                show gwen19
                with Dissolve(1.0)
                $ renpy.pause()
                g "Mnhh~!"
                g "Ooh... yeaahhh~!"
                g "Hnngg~! Ahhh~! Ahhh~!"
                $ renpy.pause()
                show gwen20
                with dissolve
                $ renpy.pause()
                mc "Here I come, Gwen!"
                g "I'm... I'm cumming too, [mc]!"
                menu:
                    with dissolve
                    "Cum inside":
                        scene ep6_771
                        with dissolve
                        mc "Urgh!"
                        g "AAAHHHH~!"
                        scene ep6_772
                        with dissolve
                    "Cum outside":
                        scene ep6_771
                        with dissolve
                        g "AAAHHHH~!"
                        scene ep6_773
                        with dissolve
                        mc "Urgh!"
                        scene ep6_774
                        with dissolve

                g "*giggles*"
                scene ep6_775
                with dissolve
                g "I love you, [mc]..."
                mc "I love you too, Gwen."
                mc "Come on, let's get up and eat breakfast now. I have to go to work as soon as possible."
                g "Won't you be late because of this?"
                mc "If I'm going to be late because of you, it's well worth it."
                g "Ahaha! Smooth..."
                g "Alright, let's clean up."
            "Let's eat breakfast":
                $ gwenskyharem = False
                mc "I know it's very tempting, but we should get up and eat breakfast now."
                mc "We'll do it next time."
                g "Hmmnn... Alright..."
        $ renpy.end_replay()
    else:
        scene ep6_776
        with dissolve
        yt "Well, another day... Another life..."
        scene ep6_777
        with dissolve
        yt "......"
        yt "Let's go to work!"
    stop music fadeout 2

    if freyapoint == 6:
        scene black
        with dissolve
        with fade

        play music 'audio/SultansSwing.mp3' fadein 2
        scene ep6_778
        with dissolve
        mc "*whistles*"
        mc "Hmmn hmmm mmnhh hnnn..."
        mc "*singing softly* With the lights out, it's less dangerous..."
        mc "*singing softly* Here we are now, entertain us..."
        mc "*singing softly* I feel-"
        scene ep6_779
        with dissolve
        "*phone vibrates*"
        scene ep6_780
        with dissolve
        yt "......"
        yt "A message from Freya?"
        scene ep6_781
        with dissolve
        yt "......"
        yt "Oh, boy... I hope it's not what I'm thinking it is..."
        scene ep6_782
        with dissolve
        yt "......"
        yt "And... it is..."
        yt "Oh..."
        yt "My..."
        yt "Jesus...!"
        yt "Now that's what I call a {b}taste of life{/b}, brother! This is what it means to live!"
        yt "Is she actually fine sending me this kind of photo?"
        yt "......"
        yt "Hold on... There's another one!"
        scene ep6_783
        with dissolve
        yt "......"
        yt "Oh, shiiiiii-"
        scene ep6_784
        with dissolve
        kid "Mom? That guy is watching porn just like you."
        scene ep6_785
        with dissolve
        yt "...!!!"
        mc "Wha-"
        scene ep6_786
        with dissolve
        wom "Ah, cover your eyes, honey! You should never see those things at your age!"
        scene ep6_787
        with dissolve
        wom "*glare*"
        mc "Aha haa... I'm sorry."
        scene ep6_788
        with dissolve
        mc "Damn it! These pictures will get me to trouble sooner or later!"
        scene ep6_789
        with dissolve
        "*phone vibrates*"
        f "(Yow, [mc]! Where are you right now?)"
        mc "(I'm almost at the burger shack, near the intersection, why?)"
        f "(Oh, nice! Please wait for me, I'm almost there!)"

        scene black
        with dissolve
        with fadeq

        "A few moments later..."

        scene black
        with dissolve
        with fadeq

        scene ep6_790
        with dissolve
        f "Howdy, partner!"
        mc "What are you, a cowboy?"
        scene ep6_791
        with dissolve
        f "A cowgirl! I heard it's a nice position!"
        mc "......"
        mc "You just set that trap for me, didn't you?"
        scene ep6_792
        with dissolve
        f "Maaaaybeeee...?"
        mc "*sighs*"
        menu:
            "Compliment her pictures":
                $ freyapoint += 1
                $ renpy.notify(freyanotif)
                scene ep6_793
                with dissolve
                mc "But, hey..."
                f "Yeah?"
                scene ep6_794
                with dissolve
                mc "Nice... photos..."
                f "Hey, don't say that with a creepy smirk!"
                mc "They just compromised my innocence, you little..."
                f "I'm sorry?"
                mc "A kid saw me viewing those photos and the mother glared like she wanted to beat the crap out of me..."
                f "Pfff!"
                scene ep6_795
                with dissolve
                f "Owahahahahaha! Ahahahahaha!"
                scene ep6_796
                with dissolve
                f ".........."
                scene ep6_797
                with dissolve
                f "Ahahahahaha!"
                f "Ow, ow... My stomach!"
                scene ep6_798
                with dissolve
                mc "*sighs*..."
                mc "Well, it's my fault for viewing it in public anyways, I should've known better. But I didn't ask for it, you know?"
                mc "You told me that you'll only send those if I ask for it."
                scene ep6_799
                with dissolve
                f "Ahaha! I'm sorry."
                f "I was waiting for you to ask last night, but you never messaged me or anything, so I got bored and took those as I waited."
                f "And I fell asleep, unfortunately. I was pretty tired with all that reviewing."
                f "It'd be a waste if you didn't see them, so I sent it this morning."
                yt "Jesus, why are we both fine with all of this?"
                scene ep6_800
                with dissolve
                mc "Well... I got caught up in something last night and instantly fell asleep after I hit the bed."
                mc "I never even got to check my phone."
                f "Heeh... What happened?"
                mc "...It's something very personal, so I can't tell you. At least for now."
                f "Hmmn... That sounds pretty serious from your tone of voice."
                f "Hey, there's no problem that can't be solved, so chin up, big guy!"
                mc "Ahh... I hope so..."
                yt "I'm just... too suspicious of Emma right now..."
                scene ep6_801
                with dissolve
                mc "Let's just get to the shop, it's almost time for opening."
                f "Oh yeah, we should! I didn't notice the time either!"
            "Don't mention it":
                scene ep6_801
                with dissolve
                mc "Let's just get to the shop, it's almost time for opening."
                f "Oh yeah, we should! I didn't notice the time either!"

    scene black
    with dissolve
    with fadeq

    "After the shift..."

    scene black
    with dissolve
    with fadeq

    scene ep6_802
    with dissolve
    l "Alright, we need to leave ahead of you, [mc]."
    f "We'll volunteer to do the closing on our own once the exams are done, we promise."
    mc "Hey, it's not a big deal. You two just do your priorities for now and we'll talk about it once it's all over."
    scene ep6_803
    with dissolve
    l "Sure! Thanks, [mc]."
    f "Bye, bye~!"
    mc "Bye! Give it your best!"
    scene ep6_804
    with dissolve
    mc "......"
    yt "And that's it for the inventory."
    yt "Let's clean up and close the shop."
    scene ep6_805
    with wipeleft
    mc "*whistles*"
    mc "Hmmn hmmm mmnhh hnnn..."
    e "......"
    scene ep6_806
    with dissolve
    e "*whispers* Hi..."
    scene ep6_807
    with dissolve
    mc "Eek!"
    yt "That creepy monotonous voice... Of course, there's no one on this earth but her."
    scene ep6_808
    with dissolve
    mc "God, friggin, damn!"
    mc "That sent chills down my spine! Can you please stop doing that already? You told me you would last night!"
    scene ep6_809
    with dissolve
    e "*giggles*"
    e "Sorry, I'm just messing with you. But that put a smile on my face after a stressful day, so thank you."
    mc "......"
    mc "That's how you work?"
    e "Probably?"
    mc "Jeez..."
    mc "Why are you here, by the way? I'm about to close up the shop."
    e "Then that's good."
    e "Will you come on a date with me?"
    mc "I beg your pardon?"
    mc "A what?"
    e "A date!"
    mc "Yeah, I heard... A date. But why date? You and I are not even that close."
    e "...What do you call eating outside with a guy then?"
    mc "Uhmm... Probably just eating outside?"
    e "Then it's a date!"
    scene ep6_810
    with dissolve
    mc "Ugh... I'm losing a lot of brain cells right now."
    mc "Oh, lord... What have you done to this world...?"
    e "......"
    scene ep6_809
    with dissolve
    e "I told you I'm going to make it up to you. I can't think of anything aside from this, so..."
    e "...Do you want to come with me or not?"
    scene ep6_811
    with dissolve
    mc "Well..."
    mc "I have to submit a report to my boss as soon as possible after I go home..."
    mc "But... I can probably just do it through my mobile phone again..."
    yt "And this is also a chance for me to learn something about her."
    scene ep6_812
    with dissolve
    mc "So, yeah. I'll go with you."
    mc "Just don't call it a date though. It's really just eating outside."
    scene ep6_813
    with dissolve
    e "It's a date."
    mc "No."
    e "It's a date."
    mc "No."
    e "It's a date."
    mc "No!"
    scene ep6_814
    with dissolve
    e "......"
    scene ep6_815
    with dissolve
    e "It's a date."
    scene ep6_816
    with dissolve
    mc "Arrhh! Alright, alright! It's a date! Just stop it!"
    scene ep6_817
    with dissolve
    mc "Just wait a bit, I'm almost done."
    e "Sure thing."
    scene ep6_818
    with dissolve
    e "......"
    scene ep6_819
    with dissolve
    e "*whispers* Yes!"
    yt "Hm?"
    stop music fadeout 2

    scene black
    with dissolve
    with fade

    play music 'audio/HighLine.mp3'
    scene ep6_820
    with dissolve
    mc "*typing*......"
    e "......"
    scene ep6_821
    with dissolve
    e "What are you doing?"
    mc "Hm? Submitting my report to my boss."
    e "That looks detailed. Do you do that daily?"
    mc "Yeah, it's a daily report about the income and my colleagues' progress."
    mc "Unlike me, they're still pretty new to the shop. So my boss wants me to report how they did daily."
    e "I see..."
    image emmmcdate:
        "ep6_822.jpg"
        pause 3.0
        "ep6_823.jpg"
        pause .2
        repeat
    show emmmcdate
    with dissolve
    mc "Did you meet Freya earlier? She works in the shop too."
    e "Yes, I met her on my way to your workplace. But I already knew she's working there."
    e "We talk through chats or calls almost every day and she tells me all kinds of stuff. She's fun to talk to."
    mc "Her personality says it all, so I can agree."
    e "......"
    e "...Your boss is Aine's mom's little sister, right?"
    mc "Huh? You mean... Miss Jess?"
    mc "Nahh... I don't think so, she told me they know each other but..."
    mc "......"
    mc "Wait... For real?"
    e "Mhm. That's her name."
    e "She's a very mysterious person in Aine's family. Even Aine herself never saw her before."
    e "I saw her once, but that's it. I wasn't able to talk to her since she never stays at their place."
    e "You can consider yourself very lucky that you work for her. I heard she's a very good person."
    mc "Yeah, she's a good boss. But I can't believe that she's Hera's sister. She never told me about it."
    e "I heard a lot of rumors about her. Including her opposing her sister."
    mc "Jeez..."
    mc "Then do you know that she and Klara are currently working together?"
    e "Really? For what?"
    mc "Uhmm... Klara told me that she's helping her shape up her company. That's all I know."
    e "......"
    e "So Miss Klara is finally back in the country?"
    mc "Yeah! I can't wait to see her. But she told me she's really busy at the moment so she can't come home for now."
    e "Building a company is no joke, there's a lot of paperwork that you have to complete."
    e "Taxes, architectural topics, and a whole lot of problems."
    mc "Heeh... I wonder if she would hire me to work for her someday..."
    e "Perhaps..."
    mc "That would be nice, but... I don't really want to leave the burger shack. I already came to love the place."
    mc "So much so that I could actually just live there! Haha!"
    mc "That's the only place where I can't think of my problems."
    e "You're busy working, of course. How can you think of your problems in that case."
    mc "Hey, that's the point!"
    mc "I'm busy, it makes me sweat, but I still love it!"
    mc "I'm meeting all kinds of people every day. Talking to them, serving them... It makes my charisma grow somehow."
    e "Are you planning to become the president at some point?"
    mc "No?"
    e "Hmm... Become a leader of something?"
    mc "Uhh... What do you mean?"
    e "......"
    e "Nothing."
    scene ep6_824
    with dissolve
    e "We're almost there, let's go and order."
    e "It's my treat. So don't bring your wallet out of your pocket, you got me?"
    mc "And if I do...?"
    scene ep6_825
    with dissolve
    e "That means death..."
    mc "......"
    e "......"
    scene ep6_826
    with dissolve
    e "Just kidding. *giggles*"
    scene ep6_827
    with dissolve
    mc "......"
    yt "I can never get used to the way she smiles at me."
    yt "I already thought this last time, but... there's something in it... something that I can't put a finger on..."
    yt "Every time she smiles, it resonates in me. Not because she used to hurt me in the past. But because it's a good feeling that I'm not used to getting from her."
    yt "......"
    scene ep6_828
    with dissolve
    e "Don't just stare at me! Come on, I'm so hungry!"
    yt "I guess this is the real her... right?"
    yt "I hope she continues to be like this..."

    scene black
    with dissolve
    with fadeq

    scene ep6_829
    with dissolve
    e "......"
    scene ep6_830
    with dissolve
    e "*munch* *munch*"
    scene ep6_829
    with dissolve
    e "......"
    scene ep6_830
    with dissolve
    e "*munch* *munch*"
    scene ep6_829
    with dissolve
    e "......"
    scene ep6_830
    with dissolve
    e "*munch* *munch*"
    mc "Ehh......"
    scene ep6_831
    with dissolve
    e "......"
    e "What?"
    e "I'm hungry..."
    mc "I haven't said anything yet..."
    scene ep6_832
    with dissolve
    yt "......"
    yt "Oh, man..."
    yt "This looks tasty as fuck, but..."
    yt "There's so many carbs in here, and I just started working out again too..."
    yt "...I will have to double or even triple my workouts now..."
    scene ep6_833
    with dissolve
    e "Hm? You don't like the food?"
    e "You told me to get you whatever I want, so I got you the same choices as mine."
    mc "No, I like it. It looks tasty, but..."
    e "...Too many calories?"
    mc "Yeah."
    scene ep6_834
    with dissolve
    e "......"
    mc "Don't judge me! I just started working out again!"
    e "......"
    mc "Ugh... Well, it's my fault, I should've told you about that earlier. Don't worry though, I still love this kind of food."
    image emmmcdate2:
        "ep6_835.jpg"
        pause 3.0
        "ep6_836.jpg"
        pause .2
        repeat
    show emmmcdate2
    with dissolve
    e "By the way, I finally solved my case."
    mc "Oh, that's awesome! Congrats! So you made the suspect tell it all, right?"
    e "Yes. It was not easy and was very stressful, but I'm glad that it all worked out."
    mc "Damn... Was he putting on a brave face the whole time?"
    e "Mhm..."
    e "He didn't really want to admit anything he did, but no matter what kind of person you are, there is still a conscience. So I used that against him."
    e "I figured that he still did love his wife because, with all the lies that he told, his emotions for his wife were real."
    e "Then I made him feel guilty about it."
    e "I made him recall all his past memories of them together."
    e "Fortunately for me, he still values them."
    e "I finally got to his soft side and he admitted that he's a psychopath, which I already presumed way before I even interrogated him."
    mc "Jesus... You're scary..."
    mc "Why did you presume that he's a psychopath though? I mean..."
    image emmmcdate3:
        "ep6_837.jpg"
        pause 3.0
        "ep6_838.jpg"
        pause .2
        repeat
    show emmmcdate3
    with dissolve
    e "We often say to not judge a book by its cover, and I agree with that. But there are times that your gut feeling is a lot stronger than just judging that person."
    e "So I grab hold of it until he says it himself, and I wasn't wrong."
    e "It all went down to jealousy. He told me that he caught his wife cheating on him and he wasn't able to hold back his emotions."
    mc "Heeh... Were you able to confirm if his wife really did cheat on him? If that's true then..."
    e "Confirmed or not, he still killed her and that's against the law."
    e "But I can't just stay put and assume, so I investigated further to confirm his allegations."
    e "I talked to his wife's friends, family, and even their neighbors."
    e "One of her friends told me the truth that she was indeed seeing someone else."
    mc "God damn... That's just too fucked up!"
    scene ep6_839
    with dissolve
    e "...We all have to understand that in this world that we treat as {b}peaceful{/b}, there are cases such as what I told you that's happening without our knowledge."
    e "This place we live in is a lot more twisted than what most people think it is..."
    scene ep6_840
    with dissolve
    e "......"
    mc "......"
    scene ep6_841
    with dissolve
    e "Hm?"
    e "Stop staring at me, your food will get cold."
    mc "Oh, sorry."
    stop music fadeout 2

    scene black
    with dissolve
    with fade

    scene ep6_842
    with dissolve
    mc "Thanks for the food, Emma."
    e "You're welcome."
    scene ep6_843
    with dissolve
    e "Now come with me."
    mc "W-whoa~! Where are we going?"
    e "Not that far! Just come!"
    mc "Alright..."

    show black
    with dissolve
    with fade

    play music 'audio/Rainbow.mp3'
    show sunsetshow
    with Dissolve(2.0)
    pause 7.0
    show ep6_844
    with dissolve
    e "See?"
    mc "......"
    scene ep6_845
    with dissolve
    mc "Whoa..."
    e "It's pretty, isn't it?"
    mc "Yeah... I've already been here before, but not exactly this part of the beach... I never thought there was such a beautiful view here."
    e "Hmm... I think it's just recently that they built this beach site. It wasn't really in this area before."
    mc "I see..."
    scene ep6_846
    with dissolve
    e "But I'm glad that they did..."
    e "I always come by here after my day's duty, that's why I'm always late coming home."
    scene ep6_847
    with dissolve
    e "......"
    mc "Hey, what are you doing?"
    e "I'm going to try the water."
    scene ep6_848
    with dissolve
    mc "Well, it's going to be..."
    scene ep6_849
    with dissolve
    e "Urrrhh...! It's cold!"
    mc "...Yep!"
    scene ep6_850
    with dissolve
    e "......"
    scene ep6_851
    with dissolve
    mc "You regret that, don't you?"
    e "*giggles* Yeah, I didn't expect the water to be that cold in the afternoon."
    scene ep6_852
    with dissolve
    mc "It's actually not that cold, it's probably pretty average, to be honest."
    mc "It's just that our bodies are hotter during the afternoon, hence the water seems a lot colder during that time of the day."
    e "Hmm... You're good at science?"
    mc "Not that much, I just know a lot about physics and chemistry."
    e "Then you're good at it."
    scene ep6_853
    with dissolve
    mc "*sighs* I won't argue with you about it..."
    scene ep6_854
    with dissolve
    mc "Let's just sit here for a while..."
    e "Are you sure you don't want to go home yet?"
    mc "Yeah, I want to stay a bit longer. You can go home first if you want to."
    scene ep6_855
    with dissolve
    e "If you're staying, then I'm staying too."
    mc "......"
    mc "Okay."
    scene ep6_856
    with dissolve
    e "......"
    scene ep6_857
    with dissolve
    e "......"
    mc "......"
    yt "If this had happened sometime before yesterday... I'm sure I would've pushed her away just now..."
    yt "But..."
    yt "But this feels so nostalgic that I don't want this to end."
    yt "This just feels..."
    yt "......"
    yt "...A lot like back then..."
    mc "......"
    scene ep6_858
    with dissolve
    mc "Hey..."
    e "Hm?"
    mc "Let's come back here again."
    scene ep6_859
    with dissolve
    e "......"
    e "Mhm!"
    scene ep6_860
    with Dissolve(2.0)
    $ renpy.pause()
    stop music fadeout 3

    scene black
    with Dissolve(2.0)
label emmapause3:
    if _in_replay:
        $ name = persistent.gallery_name
    scene emmapause3
    with dissolve
    $ renpy.pause()
    $ renpy.end_replay()
    play sound 'audio/gamepause.mp3'
    show title at move_slide
    with flash
    $ renpy.notify(imageunlock)
    $ renpy.pause()

    scene black
    with dissolve
    with fadeq

    "Late at night..."

    scene black
    with dissolve
    with fadeq

    play music 'audio/Nocturne.mp3'
    scene ep6_861
    with dissolve
    mc "......"
    scene ep6_862
    with dissolve
    mc "*sighs*..."
    yt "Even playing this game can't take my mind off of earlier..."
    yt "......"
    yt "The feeling of her touch..."
    yt "The moment when she leaned on my shoulder..."
    yt "The usual argument every time we talk to each other..."
    yt "Even the way she reacts..."
    yt "I'm always feeling something from them..."
    yt "......"
    yt "Am I... in love with her?"
    yt "......"
    yt "No, that's not it. I mean... How?"
    yt "I haven't done anything, she hadn't done anything until yesterday. And those things aren't really enough to make my feelings resonate with everything she does."
    yt "After what I witnessed during her birthday and after she kissed me that night... I started reacting this way..."
    yt "......"
    scene ep6_863
    with dissolve
    yt "No, I'm not in love with her..."
    yt "I know what it feels like to be in love, and this is way different from it."
    yt "If only I could use my brain for this, I would've solved it by now... But it's my heart that's trying to tell me something."
    yt "It's trying to tell me that something is off..."
    yt "Ever since she leaned on my shoulder, my heart started beating so fast. Even until now, it just won't stop..."
    yt "I wanted more of it. I wanted that moment to last longer..."
    yt "Because I know that I'm feeling something... A feeling that is so familiar to me..."
    yt "But why her? What is it with her? Just who is she?"
    scene ep6_864
    with dissolve
    yt "......"
    yt "She... couldn't be that girl I met in my childhood, right?"
    yt "......"
    yt "I mean... What are the chances...?"
    scene ep6_865
    with dissolve
    yt "Yeah... What are the chances, indeed..."
    scene ep6_866
    with dissolve
    yt "*sighs*..."
    yt "So much for discovering something about her..."
    yt "I expected that I won't sleep again because of this, but right now... I just want to lie down and close my eyes..."
    stop music fadeout 2

    scene black
    with dissolve
    with fade

    play music 'audio/RiverRunsDeep.mp3' fadein 2
    scene ep6_867
    with dissolve
    m "Hey, who are we waiting for? Let's just go inside."
    cl "Just shut up for a minute, will you?"
    play sound 'audio/jesscarroar.mp3'
    scene ep6_868
    with dissolve
    $ renpy.pause()
    scene ep6_869
    with dissolve
    $ renpy.pause()
    play sound 'audio/cardoorclose.mp3'
    scene ep6_870
    with dissolve
    play sound 'audio/cardoorclose.mp3'
    j "*chuckles* Sweet ride..."
    scene ep6_871
    with dissolve
    gl "Phew~!"
    gl "My goodness! What's with you girls having a meeting this late at night? And why in this place?"
    scene ep6_872
    with dissolve
    gl "Anyways, good evening to all of you!"
    cl "Good evening."
    m "'Sup."
    scene ep6_873
    with dissolve
    j "Good evening, Glenn. It's nice to meet you again."
    j "And we are sorry about the place. This is the only safe place we found that's accessible to everyone."
    j "We won't know when or where her guards and spies are lurking around, so it's better to keep our guard up all the time."
    gl "I understand, I have no complaints about it. Seems a pretty secluded place."
    scene ep6_874
    with dissolve
    m "You'll be away for a while, huh?"
    cl "Don't start."
    gl "By the way, who are those two? I've never seen them before."
    j "Those two are Moon and Claire, but they're known as Fang and Owl. I bet you've heard stories about them."
    gl "Hold up... You're not joking right now... right?"
    j "I'm serious. Those rumors around the city were real, Glenn. They exist."
    j "The two of them are on our side, just in case."
    gl "Yeah, I know what you mean, but... Jesus Christ... Where are you getting all these people from?"
    j "Let's just say... They have a connection to me. That's all I can tell you."
    gl "Still a very mysterious person, I see..."
    gl "But alright, I'll leave it at that."
    scene ep6_875
    with dissolve
    gl "I apologize if it took me so long to finally come."
    gl "I agreed to your plans when this lovely lady talked to me about it, but I have so many   business meetings that I couldn't cancel."
    scene ep6_876
    with dissolve
    j "You don't have to apologize. We all have matters to take care of, so we understand."
    j "Let's go inside, so we can talk properly."
    gl "After you, ladies."

    scene black
    with dissolve
    with fade

    scene ep6_877
    with dissolve
    $ renpy.pause()
    scene ep6_878
    with dissolve
    $ renpy.pause()
    scene ep6_879
    with dissolve
    $ renpy.pause()
    scene ep6_880
    with dissolve
    gl "So, you are the boss of this Anti-Hera party, huh?"
    gl "I'm glad to meet you, my name is Glenn."
    gl "Let's forget about the handshake for now. I don't tend to do it with unfinished business."
    k "No worries. Glad to meet you too, Glenn. My name is Klara."
    gl "Alright, let's talk about business, shall we?"
    gl "I heard you're building your own company, am I right?"
    scene ep6_881
    with dissolve
    k "Yes."
    gl "Got it. I will have to ask you a few questions regarding your plan."
    gl "Let's set aside the minor questions for now and get straight to the point. I want to know where you are planning to establish your company first."
    scene ep6_882
    with dissolve
    k "Setting it up here would be too much of a hassle if I want to live in Golden City, so I would really prefer it to be there."
    k "Although I have absolutely no idea if there are any vacant buildings or lots for sale there anymore."
    scene ep6_883
    with dissolve
    gl "That's a real concern — Golden City has become quite tight over the past few years."
    gl "If you prefer to set it up there, I would love to check my assets and properties to see if we have any available slots there to give you options."
    gl "That way, you would save yourself the trouble of looking for it yourself."
    gl "I will contact any of you guys as soon as possible."
    gl "You're a Sports Performance Analyst, am I correct?"
    gl "Aurora already told me what I need to know, but I want to confirm it directly with you."
    scene ep6_884
    with dissolve
    k "Yes, I am. I have a PhD in Sports and Exercise Science."
    k "I was a former professional swimmer as well."
    gl "I see now, no wonder you have such a beautiful physique."
    scene ep6_885
    with dissolve
    k "*giggles* Thank you."
    scene ep6_886
    with dissolve
    au "Ehem!"
    gl "Alright, alright! I don't want to get scolded by you twice!"
    scene ep6_887
    with dissolve
    m "...What are they talking about?"
    cl "Sure, ask me, like I know what it is."
    scene ep6_888
    with dissolve
    m "Pfff... Halfwit..."
    cl "One more time and I'll cut you open. Are you on your period, or what?"
    scene ep6_889
    with dissolve
    gl "Anyway, you want it to be a Performance Analytic Company, right?"
    k "Absolutely!"
    gl "Lovely! That's all I need to know for now."
    gl "If I find some available slots for you, I would like to arrange a visit. It's better if you're the one who gets to see them."
    gl "And if you're not satisfied with them, we can start with the rebuilding process."
    k "I got it. Thank you for coming all the way here at this time."
    gl "It's my pleasure!"
    gl "And besides, helping you will also help me get back at Hera in a way."
    gl "For someone like me who owns a big company, she's been a pain in the ass for quite some time now."
    scene ep6_890
    with dissolve
    k "I know..."
    k "Aside from her sister here, I know her better than anyone — she used to be my best friend."
    k "Words will never get through her. This is the only way I've found to make her shut up once and for all."
    gl "Well? I'd say good luck. You have a very long road ahead of you."
    scene ep6_891
    with dissolve
    j "With our help, it won't be as long."
    j "And besides, it won't be like any of your regular companies out there."
    gl "Huh... So, what's the plan?"
    gl "I still have some time left, why don't we discuss more about it in detail?"
    j "Of course, that's why we're all here."
    scene ep6_892
    with dissolve
    cl "I'll go get them something to drink."
    m "I'll get it, you stay here."
    cl "Thanks."
    stop music fadeout 2

    scene black
    with dissolve
    with fade

    play music 'audio/Ocean.mp3'
    scene ep6_893
    with dissolve
    a "[mc]...?"
    mc "......"
    a "*lightly taps*"
    a "Hey, [mc]! Wake up!"
    scene ep6_894
    with dissolve
    mc "Hmn?"
    mc "Aine?"
    a "Yes, it's me! Sky told me to wake you up! It's already 7:30!"
    mc "Wha-"
    mc "Really?!"
    a "Yeah!"
    a "What happened to you? Aren't you usually early to wake up?"
    scene ep6_895
    with dissolve
    mc "Oh, shit! Oh, shit! Oh, shit!"
    a "Hurry up or you'll be late!"
    mc "Yeah! Thanks for waking me up!"
    a "S-sure...!"
    scene ep6_896
    with dissolve
    a "......"
    scene ep6_897
    with dissolve
    a "Hmnnn..."
    stop music fadeout 2

    if gwenskyharem:
        scene ep6_898
        with dissolve
        mc "Hey, Sky! Good-"
        s "There's some rice balls on the table."
        play sound 'audio/closedoor.mp3'
        scene ep6_899
        with dissolve
        yt "...Huh?"
        yt "What the..."

        scene black
        with dissolve
        with fadeq

        play music 'audio/shower.mp3' fadein 2
        scene ep6_900
        with dissolve
        yt "Why did she close her door so suddenly? She's never been that way with me before. What's up with her today?"
        yt "Is she on her period...?"
        scene ep6_901
        with dissolve
        yt "Nah... Even if she is, she's not the type to act like that."
        yt "Am I the reason...?"
        yt "But what did I do to make her angry at me?"
        yt "......"
        yt ".........."
        yt "Wait... Don't tell me..."
        yt "......"
        scene ep6_902
        with dissolve
        yt "Oh... Shhhh......."
        stop music fadeout 2

    if ainepoint == 10:
        scene black
        with dissolve
        with fadeq

        play music 'audio/Ocean.mp3'
        scene ep6_903
        with dissolve
        yt "Alright, let's just hurry up and-"
        scene ep6_904
        with dissolve
        a "[mc], wait!"
        mc "Hm?"
        scene ep6_905
        with dissolve
        a "You forgot your breakfast!"
        mc "Oh, sorry. I'm in such a rush that I forgot about it. Thanks, Aine."
        a "You're welcome!"
        scene ep6_906
        with dissolve
        mc "Alright, I'll see you-"
        a "Uhm..."
        mc "Hm? What's up?"
        scene ep6_907
        with dissolve
        a "......"
        mc "Oh, right..."
        menu:
            "Give her a headpat":
                $ ainebreakfastheadpat = True
                $ ainepoint += 1
                $ renpy.notify(ainenotif)
                scene ep6_908
                with dissolve
                mc "*pats*"
                a "Mnhh..."
                yt "She sure likes it a lot. Maybe I should talk to her about it later, but for now... Time to run!"
                scene ep6_909
                with dissolve
                a "*giggles* Thanks."
                mc "No worries. I gotta run now."
                a "Alright, have a nice day."
                mc "You too."
            "Do it later":
                $ ainebreakfastheadpat = False
                mc "Sorry, Aine. But I'm running late now. I'll get to it later, okay?"
                scene ep6_910
                with dissolve
                a "Hmm..."
                a "......"
                a "*pouts* Okay..."
                mc "Sheesh..."
                mc "I gotta run now. I'll see you later."
                scene ep6_911
                with dissolve
                a "Alright, have a nice day."
                mc "You too."
        stop music fadeout 2

    scene black
    with dissolve
    with fade

    play music 'audio/BlackCat.mp3' fadein 2
    scene ep6_912
    with dissolve
    mc "*gasps*!"
    mc "*huff* *huff*"
    scene ep6_913
    with dissolve
    yt "Thank god I made it in time!"
    yt "It's still a bit early so I still have time to properly settle myself."
    scene ep6_914
    with dissolve
    l "Oh, good morning, [mc]!"
    f "Good morning, future manager!"
    mc "Heeh... You guys are early today! Nice!"
    f "Yep! We can't just leave everything to you, can we?"
    f "So we decided to be early even just for today. It's the least we can do to help you for now."
    mc "*chuckles* Thanks."
    yt "It's nice to know that they have my back even if I mess up. I'm blessed with such good co-workers. Haha!"
    mc "Alright, let me just get myself ready and we're good for opening."
    if freyapoint == 7:
        label freyapantstease:
        if _in_replay:
            $ name = persistent.gallery_name
        scene ep6_915
        with dissolve
        f "No, wait!"
        f "......"
        scene ep6_916
        with dissolve
        f "Geheheee...!"
        mc "Uhh... What now?"
        scene ep6_917
        with dissolve
        f "Let's take a picture!"
        f "You know? Like what I did last time? But it will be the three of us this time around."
        l "Oh, I'm in! Let's do it~!"
        mc "Well, alright. Let's be quick, though, we're five minutes away from opening."
        scene ep6_918
        with dissolve
        l "Okay, I'm ready."
        f "Get behind us, [mc]."
        mc "Sure!"
        scene ep6_919
        with dissolve
        f "Okay... good!"
        scene ep6_920
        with dissolve
        f "In 3..."
        yt "Mmp! Why the heck is she holding my dick?!"
        image freytmcd:
            "ep6_921.jpg" with dissolve
            pause 0.7
            "ep6_920.jpg" with dissolve
            pause 0.7
            repeat
        show freytmcd
        with dissolve
        f "2..."
        yt "Oof! Her petite fingers... feel incredible! Good... lord!"
        scene ep6_922
        with dissolve
        f "1..."
        yt "Ooh, shit!"
        with flash
        scene ep6_924
        with dissolve
        l "How is it, how is it?"
        f "Let's see..."
        scene ep6_923
        with dissolve
        l "Eh? What's with your face, [mc]? Were you about to sneeze or something?"
        mc "O-oh yeah... Aaha haaa..."
        mc "I-I tried to hold it back and got caught by the camera. Sorry... Aha haa..."
        scene ep6_925
        with dissolve
        f "{i}Heheee...!"
        yt "Why you little...!"
        yt "I'll get my payback later, just watch!"
        mc "A-anyways... Let's get ready."
        l "Of course!"
        $ renpy.end_replay()
    stop music fadeout 2

    scene black
    with dissolve
    with fadeq

    "After the day's shift..."

    scene black
    with dissolve
    with fadeq

    play music 'audio/SultansSwing.mp3' fadein 2
    scene ep6_926
    with dissolve
    mc "Hey, thanks for helping me with the closing, I appreciate it."
    f "No big deal! My review schedule is a bit later than previous days, so I gotta at least help you."
    f "I'm back to the usual hectic shit tomorrow though, and I'm not sure about Lily, so I think you will be on your own again."
    mc "Don't worry, I can manage."
    if freyapoint == 7:
        scene ep6_927
        with dissolve
        yt "Let's just pretend that didn't happen earlier and take her by surprise later, shall we...?"
        yt "GRAHAHAAAA...! The evil in me says, YES!"

    scene ep6_928
    with dissolve
    un "Hnn?"
    scene ep6_929
    with dissolve
    un "Yow, [mc]! You're finally out!"
    mc "Huh? That voice sounds awfully familiar!"
    scene ep6_930
    with dissolve
    mc "What the..."
    mc "Yow, Shu! What's up? Long time no see!"
    scene ep6_931
    with dissolve
    f "Hrmnn...??"
    f "Huh!"
    play sound 'audio/woosh.mp3'
    scene ep6_932
    f "A comrade! A fellow flat earther!"
    scene ep6_933
    with dissolve
    f "Huwaaaaa...!"
    mc "Uhh... Frey? I'm sorry to shatter your dreams, but... he is a guy..."
    scene ep6_934
    with dissolve
    f "Eh? I beg your pardon? Can you please repeat that?"
    mc "He's a guy, a male, a chad, a he, whatever you can think of that can describe a man, that's him."
    scene ep6_935
    with dissolve
    shu "Yep! I have three girlfriends too!"
    scene ep6_936
    with dissolve
    shu "My, my... Jumping at me as soon as you saw me... I must be too good-looking!"
    scene ep6_937
    with dissolve
    shu "Ahh... I'm just too good for this world!"
    yt "Right, right... I almost forgot his personality... He's one heck of a narcissist..."
    shu "You can call me the Alpha and the Omeg-"
    scene ep6_938
    with dissolve
    $ renpy.pause()
    play sound 'audio/slap.mp3'
    scene ep6_939
    with hpunch
    shu "Gaaa~!!"
    f "Get out of my face, you squirt! You're not a comrade, you're my worst enemy!"
    scene ep6_940
    with dissolve
    shu "Huuuuh?!!"
    shu "You're the one who jumped at me, you bitch! Now you just damaged my precious and exquisitely handsome face!"
    shu "What do you mean your worst enemy, huh?!"
    scene ep6_941
    with dissolve
    f "How dare you make me think that you're a girl, squirt!"
    shu "Don't call me that! And blame my creators who made me like this! It's not my fault if they made me so perfect!"
    scene ep6_942
    with dissolve
    mc "Aha ha ha ha..."
    play sound 'audio/punch.mp3'
    scene ep6_943
    with hpunch
    shu "Ow, ow, ow!"
    f "Ow, ow, ow!"
    mc "Now, now... Calm down or I'll lock you both inside the shop."
    shu "With this bitch? Hell no!"
    f "With this squirt? Over my dead body!"
    mc "No, I'm serious, I'll lock you up..."
    scene ep6_944
    with Dissolve(1.0)
    f "......"
    shu "......"
    mc "I see that I finally got your attention."
    scene ep6_945
    with dissolve
    mc "*sighs*"
    scene ep6_946
    with dissolve
    f "Anyway, who's this squirt?"
    shu "Hey, I told you to not call me that!"
    mc "Ah, well... He was a classmate during college, you can say that he was my best friend."
    mc "But after we graduated, he went overseas along with his family, which is why I wonder what the heck he is doing here."
    mc "I haven't heard any news from him for almost two months now."
    f "Ah. I see."
    scene ep6_947
    with dissolve
    shu "Come on...! That's harsh of you, [mc]! Didn't you miss me at all?"
    mc "Uh, no? Why would I?"
    shu "Isn't it obvious?"
    scene ep6_948
    with dissolve
    shu "It's because I'm your..."
    shu "Best..."
    scene ep6_949
    with dissolve
    shu "Friend!"
    mc "You {b}were{/b} my best friend. You left me hanging after you left the country, you twat."
    scene ep6_950
    with dissolve
    shu "Huun... I'm sorry, okay!"
    mc "Now, what are you doing here? I didn't expect to see you today, to be honest."
    mc "You're free to enter the shop, by the way. Don't just stand outside like a stalker or something."
    scene ep6_951
    with dissolve
    shu "Dude! You're cleaning! How can I just enter without permission? I still have my manners, you know?"
    shu "I'd rather stay outside than get berated by your manager!"
    mc "That's shocking to know that you have manners."
    mc "Well, we don't have that kind of rule here. So you're free to enter as long as it's open."
    shu "Eh, alright, next time then."
    scene ep6_952
    with dissolve
    shu "But now that I'm back, we should go out sometime, man!"
    shu "You know? Go somewhere with a lot of hot chicks like the old times?"
    mc "......"
    mc "No... I'm busy."
    scene ep6_953
    with dissolve
    shu "Harsh!"
    shu "You've gone cold, [mc]. What happened to you?"
    mc "It's not that I'm cold, I just decided to be a better guy, Shu. Set my life straight, you know?"
    yt "Besides, someone is looking at me in a bad way..."
    scene ep6_954
    with dissolve
    shu "Well, we're at the age where we should be looking for a living, so I get you."
    mc "*chuckles* You've matured quite a bit, and that's good to know. You usually just forced me to come with you."
    shu "A lot happened while I was outside the country that got my shit all messed up, so... yeah. I learned from my mistakes."
    scene ep6_955
    with dissolve
    shu "But still, I want to celebrate my comeback, so we need to go somewhere some other time."
    shu "And no, it won't be at any bar here. We're going somewhere that you're very familiar with."
    mc "Heeh... Now I'm interested. How's that place going? I thought they closed it a year ago."
    shu "They did! But they reopened it recently — that's why I decided to come back and invite you."
    shu "Coming back here just for that place is really worth the trouble."
    shu "Why don't you invite your friends? I'm sure they'd like the place!"
    mc "I'll think about it for now."
    shu "Sure, sure!"
    scene ep6_956
    with dissolve
    shu "Don't let this bitch come with us though."
    f "Say what now?!"
    f "I might just kill this squirt one day, [mc]. Trust me."
    mc "You guys just met and you're already enemies, what's wrong with you two?"
    mc "Though it's pretty funny to see two short stacks fight. It's like seeing kids brawl!"
    mc "Ahahahahaha..."
    scene ep6_957
    with dissolve
    mc "...haaa..."
    mc "*ehem* I'm just kidding..."
    mc "W-well, anyway. I'm going home now."
    scene ep6_958
    with dissolve
    f "Yeah, let's go!"
    shu "Hold on, do you still have my number?"
    mc "Hmm... Yeah? I think so? I haven't deleted any of my contacts for years. Why?"
    scene ep6_959
    with dissolve
    shu "Noice!"
    scene ep6_960
    with dissolve
    shu "My number is still the same, by the way. I'll talk to you later, man."
    mc "Oh, that's convenient, sure!"

    scene black
    with dissolve
    with fade

    scene ep6_961
    with dissolve
    mc "......"
    scene ep6_962
    with dissolve
    mc "Uhh... Excuse me, sir. Why are you still following me? We are just two blocks away from my house. Are you lost or something?"
    shu "Huh? No way, dude! You know I'm good with directions, I still know every nook and cranny of this city even after all these years, you know?"
    mc "Then why are you following me?"
    shu "I'm not! I'm heading to my house, buddy!"
    scene ep6_963
    with dissolve
    shu "It's that one!"
    scene ep6_964
    with dissolve
    mc "Wait... This one is just right across from ours, isn't it...?"
    scene ep6_965
    with dissolve
    mc "Then that means..."
    shu "......"
    scene ep6_966
    with hpunch
    tbot "HUUUUUUUUHH......??!!"
    shu "Dude, you never told me you live here!"
    scene ep6_967
    with dissolve
    mc "No, you stay away from me, you demon spawn! You're toxic in my life!"
    shu "Hey, don't be rude to your new neighbor! Now bow down to your master!"
    mc "What the heck are you talking about! You ain't my master, you shit!"
    scene ep6_968
    with dissolve
    mc "...Wait, did you just say 'new neighbor'?"
    image shumctoh:
        "ep6_969.jpg"
        pause 3.0
        "ep6_970.jpg"
        pause .2
        repeat
    show shumctoh
    with dissolve
    shu "Well, yeah! I recently bought the house for myself. I'm going to stay here from now on."
    mc "You rich bastard!"
    mc "But... All alone? You mentioned you have three girlfriends, right? Where are they? Don't tell me you were lying."
    shu "No, I wasn't lying. I left them in that country so I can have my absolute freedom here."
    mc "Jesus, dude... You never change when it comes to women!"
    shu "No, no! You got me all wrong!"
    shu "What I meant was... So that I can go anywhere I want. Traveling and all that, you know?"
    shu "They're my chains. They don't want me to go anywhere. I just told them that I have a business to take care of in this country so they'd let me go."
    shu "But despite that, I love my girls, dude. I'll never cheat on them."
    scene ep6_971
    with dissolve
    shu "Not anymore since I lost her..."
    mc "You mean... your girlfriend when we were in college?"
    shu "Yeah..."
    scene ep6_972
    with dissolve
    mc "*chuckles*"
    scene ep6_973
    with hpunch
    mc "Depressed Shu, away!"
    shu "Pfff!!"
    scene ep6_974
    with dissolve
    mc "Come on! Just get over it, Shu. We're on our new lives now."
    mc "Just like what a certain girl said to me -- 'Be the man that you wanted to be'."
    scene ep6_975
    with dissolve
    mc "I don't know why, but I felt a huge weight removed from my shoulders when she said that to me the other day..."
    shu "Well, damn... You're so lucky, dude. Nobody ever told me something like that. Looks like you found the girl of your dreams, huh?"
    mc "I'm not too sure about that..."
    mc "Right now... She's just too mysterious to me..."
    scene ep6_976
    with dissolve
    shu "Shit, now you're the one brooding over something."
    shu "You know what? I'll just go inside before this talk gets any deeper. I don't want to hear your cringe-y words when that happens."
    shu "And besides, I still have to unpack my bags. I just got here today."
    mc "Well, alright. I'll see you later then."
    scene ep6_977
    with dissolve
    shu "Yep! See you later, dude!"
    mc "Don't come near my house though..."
    shu "You know that you're actually just tempting me to do so if you say that."
    scene ep6_978
    with dissolve
    e "{i}Hm? Is that a girl he was talking to?"
    scene ep6_979
    with dissolve
    mc "......"
    mc "Hey, Emma. You're home early today."
    e "Yes, I don't have anything to do at the office since I just solved my case."
    scene ep6_980
    with dissolve
    e "By the way, was that a girl you were talking to? I don't remember anybody living in that house since we got here."
    mc "Eh? No, that was a guy. Like... a hundred percent kind of guy..."
    scene ep6_981
    with dissolve
    e "......"
    mc "*sighs* I knew this would happen if he's here."
    mc "Trust me, I'm not lying. I can introduce him to you tomorrow if you want."
    scene ep6_982
    with dissolve
    e "......"
    mc "Ugh..."
    mc "Well, let's go inside. Sky might be fixing dinner already."
    scene ep6_983
    with dissolve
    e "Hm? No, I'm the one cooking dinner for tonight. Sky asked me to do it earlier. She told me she's not feeling well."
    mc "Oh... Okay..."
    if gwenskyharem:
        scene ep6_984
        with dissolve
        yt "Damn it... I know I have to talk to her about it. But I just know her well..."
        yt "Talking to her when she's like this won't get us anywhere. I know she won't listen to anything that I say if I try to force it."
        yt "All I can do right now is wait until she calms down a little bit."
        scene ep6_985
        with dissolve
        yt "*sighs*..."
        yt "And now, that's another problem added to my list! I think I might just go crazy at this point!"
    stop music fadeout 2

    if ainepoint == 11:
        scene black
        with dissolve
        with fade

        scene ep6_986
        with dissolve
        mc "......"
        mc "*sighs*"
        play sound 'audio/doorknock.mp3'
        "*knocks*..."
        a "Uhm... [mc]? Are you in there?"
        scene ep6_987
        with dissolve
        mc "Hmm...? Yeah... I'm here... Why...?"
        a "Can I come in?"
        mc "Ah... well... yeah... go ahead..."
        play sound 'audio/closedoor.mp3'
        play music 'audio/TimeTraveling.mp3'
        scene ep6_988
        with dissolve
        a "Hey, are you okay?"
        mc "Uh... Yeah...? I think so..."
        scene ep6_989
        with dissolve
        a "You don't sound okay to me. The usual energy in your voice isn't here. What's the matter?"
        mc "Mhh... Nothing... Maybe I'm just too tired... It's been rather hectic at the burger shack recently..."
        a "Hmmm... Are you sure? The last time you came back home really tired but you were still fine..."
        mc "And well... Too many problems inside my head... I'm pretty much just forcing myself to sleep right now..."
        a "Yeah, I figured that much. Everyone may not have noticed during dinner, but I saw you seemed to be staring into the distance."
        mc "I see..."
        yt "She is quite observant to have noticed those details..."
        a "You can tell me your problems, [mc]. We can talk about it if you want them off your chest."
        mc "Thanks... I appreciate that... but... probably not right now... I just want to go to sleep..."
        mc "Although... all these things inside my head... won't let me..."
        if gwenskyharem:
            yt "This could be a perfect opportunity to talk to her, but... damn... I'm just not in the right state of mind to do it..."
            yt "I already have a lot to think about already... but Sky being angry at me is another thing."
            yt "We've been living together since we were kids and we usually don't come to this point where we aren't talking to each other..."
            yt "Knowing that we are not fine, is just hitting me hard..."
        scene ep6_990
        with dissolve
        a "Look, get up and come here."
        scene ep6_991
        with dissolve
        mc "Hm? But why?"
        a "Come. It's my turn to comfort you."
        a "I'm always selfishly asking you to comfort me, but I've never returned the favor. And I just think this is the right thing to do."
        mc "Okay... but, what do you want me to do...?"
        a "Just lean on my chest and close your eyes. Then, try and just think about me and me alone, not what's inside your head right now."
        mc "......"
        mc "Okay then..."
        scene ep6_992
        with dissolve
        a "There you go... *giggles*"
        a "How does that feel?"
        mc "......"
        scene ep6_993
        with dissolve
        mc "It's soft..."
        a "*giggles* Is it?"
        mc "You're not embarrassed about this? You usually react whenever I do something... well... not proper to you."
        scene ep6_994
        with dissolve
        a "Well, that's the thing. You already saw me naked, you already touched them. What more is there to be embarrassed about?"
        mc "Hmn... You're a lot more open-minded than I thought you would be."
        a "I might be a conservative old-school kind of woman, but I know where and when I should be like that."
        a "And I don't think this is the time."
        mc "That's good to know. I don't want to get slapped by you again. That hurts, you know?"
        scene ep6_995
        with dissolve
        a "You took the reward without any permission, what did you expect me to do? *giggles*"
        a "And I guess you did like that, didn't you?"
        mc "For a gobsmacking slap in return? It's not worth the trouble, really."
        scene ep6_996
        with dissolve
        a "My, my..."
        a "That's enough talk for now. Just go to sleep and hope that tomorrow, everything will be better."
        mc "Mhm..."
        a "Now wrap your arms around me."
        scene ep6_997
        with dissolve
        mc "......"
        mc "...Can you manage to get out of there though? I know I'm pretty heavy."
        a "Yeah, I think I can manage. I'll even put you down properly if you want. *giggles*"
        mc "*lightly chuckles* Thanks, Aine."
        a "You're very welcome."
        a "......"
        a "Good night, [mc]."
        mc "Mhm. Good night."
        stop music fadeout 2

        scene black
        with Dissolve(2.0)
        label ainepause5:
        if _in_replay:
            $ name = persistent.gallery_name
        scene ainepause5
        with dissolve
        $ renpy.pause()
        $ renpy.end_replay()
        play sound 'audio/gamepause.mp3'
        show title at move_slide
        with flash
        $ renpy.notify(imageunlock)
        $ renpy.pause()

    scene black
    with dissolve
    with fade

    scene ep6_998
    with dissolve
    mc "55..."
    scene ep6_999
    with dissolve
    $ renpy.pause()
    scene ep6_998
    with dissolve
    mc "56..."
    scene ep6_999
    with dissolve
    $ renpy.pause()
    scene ep6_998
    with dissolve
    mc "57..."
    scene ep6_999
    with dissolve
    $ renpy.pause()
    scene ep6_998
    with dissolve
    mc "58..."
    scene ep6_999
    with dissolve
    $ renpy.pause()
    scene ep6_998
    with dissolve
    mc "59..."
    scene ep6_999
    with dissolve
    $ renpy.pause()
    scene ep6_998
    with dissolve
    mc "60..."
    scene ep6_1000
    with dissolve
    yt "Ahh... That will be all for now."
    yt "I think I should consider waking up a bit earlier next time so I can go outside and jog at least a few kilometers."
    yt "All I've been doing are these basic workouts. I should think of my stamina for once."
    scene ep6_1001
    with dissolve
    yt "......"
    yt "Alright, another day of the week. Let's do this!"
    play music 'audio/DontShoot.mp3'
    scene ep6_1002
    with wipeleft
    mc "*hums* Hmmn hmm hmmmn hmmmmmm..."
    shu "*click* *click*"
    scene ep6_1003
    with dissolve
    mc "*hums* Hmmh hmmmm hm-"
    scene ep6_1004
    with dissolve
    mc "Eh..."
    scene ep6_1005
    with dissolve
    shu "*munch* *munch* *munch*"
    play sound 'audio/woosh.mp3'
    scene ep6_1006
    with hpunch
    mc "What the fuck are you doing inside my house, man?!!"
    shu "Ummog mmmog nnog!"
    mc "Haaaa?! What the heck are you saying?! I told you to not come near my house, didn't I?!"
    mc "Everybody will mistake you for my girlfriend, you idiot!"
    scene ep6_1007
    with dissolve
    $ renpy.pause()
    scene ep6_1008
    with dissolve
    shu "*gasps*"
    shu "Dude, Sky let me in and even gave me something to eat!"
    yt "Ah, right... I forgot that Sky knows him."
    shu "Have you forgotten that I don't know how to cook?! What more can I do in order to survive?!"
    mc "You have money, go to a restaurant! It's not our fault that you don't know how to cook for yourself!"
    shu "Come on, dude! Have mercy on me, will you!"
    mc "For you? There's nothing, zero, none!"
    stop music fadeout 2
    scene black
    with Dissolve(1.5)
    pause 1.5
    play sound 'audio/introslam.mp3'
    scene ep6_1009
    play music 'audio/Gnossienne.mp3' fadein 3
    $ renpy.pause()
    shu "So, this is what rejection feels like......"
    mc "Huh...?"
    shu "The feeling of being rejected by your own brother..."
    mc "Wait, how did I become your brother?"
    shu "The feeling of emptiness, gradually increasing as your heart shatters in a million pieces....."
    shu "There is nothing more painful than-"
    mc "Ah, shit! Alright, alright! You can stay, just stop this stupid emotional blather!"
    stop music
    scene ep6_1010
    play sound 'audio/scratch.mp3'
    shu "Really~?"
    mc "Yeah, but if you're going to eat here, you need to chip in on our weekly food budget, you got me?"
    scene ep6_1011
    with dissolve
    shu "Hmhmmmm... Who do you think I am?"
    shu "Of course I will! I'm not going to let you feed me for nothing, you know?"
    mc "That's good to hear."
    play music 'audio/dark1.ogg'
    scene ep6_1012
    with dissolve
    shu "By the way, dude. Have you heard about this company called Ulysses launching a virtual, hyper-reality MMORPG game soon?"
    mc "Uh... No?"
    show eternumfeature
    with Dissolve(1.0)
    shu "I heard that they will use a neural implant to recreate the player's five senses within the game!"
    mc "A neural implant, huh? That sounds expensive as fuck."
    mc "But when did our technology reach that far?"
    shu "I have no idea... Although it does sound promising, doesn't it?"
    shu "I think I might try it when it's open to the public."
    mc "Well? It fits for someone like you who has a lot of money."
    scene ep6_1014
    with dissolve
    mc "Anyway, I'm going to get ready and go to work. Don't wander around the house too much. There are girls living here besides Sky."
    shu "I got'cha, buddy! The TV is all I need!"
    mc "Good! I gotta go now."
    shu "Sure! Have a nice day ahead, [mc]!"
    mc "Mhm. You too."
    stop music fadeout 2

    scene black
    with dissolve
    with fade

    scene ep6_1015
    with dissolve
    mc "*hums* Hmmn hmm hmmmn hmmmmmm..."
    scene ep6_1016
    with dissolve
    mc "*hums* Hmmh hmmmm hm-"
    scene ep6_1017
    with dissolve
    e "*gasps*!"
    mc "Hm?"
    mc "Uh-oh..."
    play sound 'audio/punch.mp3'
    scene ep6_1018
    with hpunch
    e "HYAAAAAAA~!!!"
    scene ep6_1019
    with dissolve
    yt "Ah, yeah... What a nice way to start the day..."
    scene ep6_1020
    play sound 'audio/kick_light.mp3'
    with hpunch
    pause 0.2
    play sound 'audio/impacteerie.mp3'
    scene black

    scene black
    with Dissolve(1.0)
    with fade

    $ renpy.pause()
    yt "Ugh... My head hurts like hell..."
    yt "...Did I die? I know I hit my head on the floor, but..."
    yt "Something smells so nice..."
    yt "And something... feels so soft on the back of my head..."
    yt "......"
    yt "This warmth... This feeling..."
    yt "No, I can't be wrong... This feels exactly like..."
    yt "...What I used to feel when I was on her lap... back... then..."
    scene ep5_319
    with flash
    play music 'audio/BlanketOfStars.mp3'
    mc "{i}Hey, what's your name?"
    em "{i}Hm? Emy... My name is Emy."
    scene ep5_354
    with dissolve
    mc "{i}Yooow~! Emy~!"
    scene ep5_489
    with dissolve
    mc "{i}S-s-stop kissing me! You're getting weird now, Emy! No one kissed me before!"
    scene ep5_516
    with dissolve
    mc "{i}Hey, Emy?"
    em "{i}Hm? Yeah? What is it?"
    mc "{i}Can I... rest on your lap again?"
    scene ep5_547
    with dissolve
    mc "{i}Emy~! Again, I promise! I'll definitely come back for you!"
    mc "{i}And... I love you too!"
    scene ep5_456
    with dissolve
    mc "{i}Emy!"
    scene ep6_859
    with dissolve
    mc "{i}Emy~!"
    scene ep5_385
    with dissolve
    yt "Ahh... That's right..."
    yt "Her name... was Emy... wasn't it...?"
    scene black
    with Dissolve(1.0)
    $ renpy.pause()
    scene ep6_1021
    with Dissolve(2.0)
    yt "That was the reason... why everything about what she does... feels so familiar..."
    yt "That was the reason why those moments felt so dear to me..."
    scene ep6_1022
    with Dissolve(2.0)
    yt "Now I... understand..."
    yt "I did not... fall in love with her..."
    yt "It's not love..."
    yt "I was longing..."
    yt "...I was longing for those exact feelings... that happened a long time ago..."
    yt "...And she's... reminding me of them..."
    scene ep6_1023
    with Dissolve(2.0)
    e "Hey, you're finally awake. Why are you crying?"
    yt "Emma... You couldn't be..."
    stop music fadeout 2
    scene black
    with Dissolve(2.0)
    $ renpy.pause()
    show ep6end
    with dissolve
    $ renpy.pause()
    scene black
    with dissolve
    $ renpy.pause()

    scene ep6_1024
    with Dissolve(2.0)
    play music 'audio/InfinityCycle.mp3'
    mc "This... can't be..."
    mc "All this time she's..."
    mc "......"
    mc ".........."
    mc "God... what..."
    mc "...have I done?"
    stop music fadeout 3
    scene ep6_1025
    with Dissolve(3.0)
    pause 2.0
    play sound 'audio/cinematicimpact.mp3'
    scene black
    $ renpy.pause()

    jump ep7

label Episode_10_Start:

    #KoGa3 START#
    $ KoGa3GameProgress = "Ep10"
    #KoGa3 END#

    $ achievement.grant("ACHIEVEMENT_EPISODE_9")
    $ achievement.sync()
    $ Erynn_Week4_Friday_Slap = False
    $ Alexis_Week4_Friday_Blackmail_Involve = False
    $ Nikki_Week4_Friday_Oral = False
    $ Nikki_Week4_Friday_SleepBed = False
    $ Cara_Week4_Friday_Play = False
    $ Cara_Week4_Friday_LickAss = False
    $ Cara_Week4_Friday_SleepBed = False
    $ Erynn_Week4_Saturday_Jump_Cara = False
    $ Erynn_Week4_Saturday_Jump_Nikki = False
    $ Erynn_Week4_Saturday_Jump = False
    $ Erynn_Week4_Saturday_NikkiLie = False
    $ Erynn_Week4_Saturday_CaraLie = False
    $ Melissa_Week4_Saturday_Kiss = False
    $ Melissa_End = False
    $ Melissa_Week4_Saturday_Dream = False
    $ MC_NoFriends = False
    $ Darryl_SeeNikkiMC = False
    $ Nikki_Week4_Saturday_Icecubes = False
    $ Nikki_Week4_Saturday_Bed = False
    $ Nikki_Week4_Saturday_Sex_Inside = False
    $ Cara_Week4_Saturday_LickAss = False
    $ Alexis_Week4_Saturday_Cara_Phone = False
    $ Cara_Week4_Saturday_Bed = False
    $ Cara_Week4_Saturday_Anal_Suggestion = False
    $ Cara_Week4_Saturday_Sexgame = False
    $ Cara_Week4_Saturday_Game_Change = False
    $ Nikki_Week4_Wednesday_AlexisLaylaBreakUp = False
    $ Cara_Week4_Wednesday_AlexisLaylaBreakUp = False
    $ MC_Bike = False
    $ Emily_Week4_Sunday_Sexy = False
    $ Emily_Week4_Sunday_DateJohn = False
    $ Erynn_Week4_Sunday_OfferBikeRide = False
    $ Week5_Monday_Prettiest_Layla = False
    $ Week5_Monday_Prettiest_Valeria = False
    $ Week5_Monday_Prettiest_Tori = False
    $ Valeria_Week5_Monday_Picture = False
    $ Valeria_LikeMC = False
    $ Valeria_Week5_Monday_Photobooth = False
    $ Valeria_Week5_Monday_Kiss = False
    $ Alexis_Week5_Monday_Date_Cancel = False
    $ Alexis_Week5_Monday_Makeup = False
    $ Adriana_Week5_Monday_SlapAss = False
    $ Elena_Week5_Monday_Beach_Hero = False
    $ Elena_Week5_Monday_Beach = False


    if Alexis_Dating == True:
        jump Week4_Friday_Evening2_Alexis
    else:
        jump Week4_Friday_Evening2

label Week4_Friday_Evening2:
    scene black with Dissolve(1)
    pause 2
    scene 10_001 with Dissolve(1)
    mc "{i}(Seriously... Where is that girl?){/i}"
    play sound "Sounds/Phone_Vibrate.mp3"
    n "*Bzzzt. Bzzzt*"
    scene 10_002 with Dissolve(1)
    mc "Erynn?"
    me "It's me."
    mc "Mel... Any news?"
    scene 10_003 with Dissolve(1)
    stop music fadeout 1.0
    play music ("Music/LoFi Upbeat 1.mp3", "Music/LoFi Upbeat 2.mp3", "Music/LoFi Upbeat 3.mp3", "Music/LoFi Upbeat 4.mp3") volume 0.2
    me "She just called me."
    mc "*Sigh* What a relief. What happened?"
    me "They had some problems at the photo shoot and had to redo everything."
    mc "Problems?"
    scene 10_004 with Dissolve(1)
    if Erynn_End == True:
        me "Lighting issues and there was some drama with the photographer and..."
        mc "Where is she now?"
        me "She's on her way here."
        mc "Okay, I'm going back home too, then."
        me "Thank you, [mc]."
        mc "No problem."
        jump Week4_Friday_Evening3
    else:
        me "Lighting issues and there was some drama with the photographer and... She can tell you all about it."
        mc "Where is she now?"
        me "She's on her way here."
        mc "Okay, I'm coming back, then."
        scene black with Dissolve(2)
        pause 2
        scene 10_022 with Dissolve(1)
        mc "Hey, Mel."
        me "Hey."
        mc "Erynn not back yet?"
        me "No, but any minute now."
        scene 10_023 with Dissolve(1)
        me "Thank you, [mc]."
        mc "I didn't do anything."
        me "That's not true. You immediately went looking for her without question. So, thank you!"
        scene 10_024 with Dissolve(1)
        me "Don't have children, they'll just worry you for the smallest of things."
        me "Especially this one."
        mc "Oh, don't worry. I don't plan on having a child anytime soon."
        me "That's what I said when I was your age."
        mc "Haha. Mom too, I bet."
        scene 10_025 with Dissolve(1)
        mc "Didn't you ever want a second one?"
        me "I did. But... Hmm... It just wasn't in the cards, I guess."
        me "Besides, the one I have easily counts as two."
        mc "Haha."
        scene 10_026 with Dissolve(1)
        er "So that's what you think of me. Good to know!"
        scene black with Dissolve(1)
        transform moveup:
            xalign 0.5 yalign 1.0
            linear 5.0 yalign 0.0
        show 10_027 at moveup
        pause 3
        me "Erynn!"
        mc "Hey, Erynn."
        scene 10_028 with Dissolve(1)
        er "I'm not that bad."
        me "No, you're not!"
        scene 10_029 with Dissolve(1)
        er "Hey."
        mc "Hi. I can stand up, you know?"
        er "This works too."
        scene 10_030 with Dissolve(1)
        me "Come sit down with us and tell us what happened."
        mc "{i}(Doesn't look like she's seen Ethan today.){/i}"
        scene 10_031 with Dissolve(1)
        mc "Uh..."
        er "No need to make space. I can sit right here."
        mc "Sure... I guess."
        scene 10_032 with Dissolve(1)
        mc "*Whisper* Are you okay?"
        er "*Whisper* Yeah, why?"
        mc "*Whisper* I'll tell you later."
        if Erynn_LikeMC == True:
            scene 10_033 with Dissolve(1)
            er "*Whisper* Okay."
            me "So, why didn't you pick up when we called?"
        else:
            er "*Whisper* Okay."
            me "So, why didn't you pick up when we called?"
        scene 10_034 with Dissolve(1)
        er "I couldn't. The photo shoot should've been done at noon. But halfway in, our photographer decided that the lighting was wrong."
        er "And it's not that he didn't test it beforehand."
        er "It wasn't just a few spots that needed adjusting. Nooo... The whole setup needed to be rearranged."
        er "There were some huge props so it took a little over two hours before he was satisfied."
        scene 10_035 with Dissolve(1)
        er "In the meantime, we couldn't do much but wait."
        er "We were mostly just chatting and on our phones."
        er "Then the photographer came again and started to complain about us being noisy."
        er "'Oh my gosh, I can't work like this.'"
        mc "{i}(Haha. I hope he doesn't sound like that.){/i}"
        scene 10_036 with Dissolve(1)
        er "He started shouting at us and had the audacity to call us props and say that we should be quiet. Ridiculous, let me tell you."
        er "The girls got mad. More drama started. The director got involved. Phone calls were made."
        er "In the end, they decided we weren't allowed to use our phones until the shoot was done. Like that had anything to do with the lighting issues..."
        er "I asked if I could make a quick call to let you know. But with all that was going on, they didn't want to upset this diva of a photographer even more."
        er "To top it all off. Instead of four hours, the shoot took eight! And the pictures don't even look that great!"
        if Erynn_Week3_Monday_Blackmailhelp == False:
            scene 10_037 with Dissolve(1)
            mc "Weren't you in any of the pictures then?"
            er "Hehe. Sadly in lots of them."
            mc "Then they can't be that bad."
            er "Thanks."
            scene 10_051 with Dissolve(1)
            er "Let's go to my room."
            mc "What do you want to do in your room?"
            er "..."
            er "Talk!"
            scene black with Dissolve(1)
            pause 2
            scene 10_060 with Dissolve(1)
            er "It's been a while since last you were in my room."
            mc "No, not really. I slept in your bed a couple of weeks ago."
            er "You did?"
            mc "Yeah, after you kicked me out of your apartment."
            er "Oh... Sorry about that."
        else:
            menu:
                "Nice":
                    scene 10_037 with Dissolve(1)
                    mc "Weren't you in any of the pictures then?"
                    er "Hehe. Sadly in lots of them."
                    mc "Then they can't be that bad."
                    er "Thanks."
                    scene 10_051 with Dissolve(1)
                    er "Let's go to my room."
                    mc "What do you want to do in your room?"
                    er "..."
                    er "Talk!"
                    scene black with Dissolve(1)
                    pause 2
                    scene 10_060 with Dissolve(1)
                    er "It's been a while since last you were in my room."
                    mc "No, not really. I slept in your bed a couple of weeks ago."
                    er "You did?"
                    mc "Yeah, after you kicked me out of your apartment."
                    er "Oh... Sorry about that."
                "Joke":
                    scene 10_038 with Dissolve(1)
                    mc "Because you were in all of them?"
                    er "..."
                    er "Yeah! Not everyone can be as pretty as you."
                    mc "I know, right?"
                    me "Haha."
                    scene 10_039 with Dissolve(1)
                    er "Okay... Let's test it."
                    er "Mom, take a picture of us, please."
                    mc "You sure about that? I mean, I don't want to make you look bad."
                    er "Cocky..."
                    mc "Confident?"
                    scene 10_040 with Dissolve(1)
                    me "Are you guys ready?"
                    me "Three... two..."
                    menu:
                        "Take the picture":
                            scene 10_041 with Dissolve(1)
                            me "One!"
                            scene 10_042 with Dissolve(1)
                            er "Thanks, Mom."
                            mc "Okay... I'll admit. You look better. In the photo that is!"
                            er "Haha, thanks. You aren't looking so bad either, if you didn't smile so... Why are you smiling like that?"
                            mc "I was trying extra hard to look good."
                            er "Haha."
                            scene 10_051 with Dissolve(1)
                            er "Let's go to my room."
                            mc "What do you want to do in your room?"
                            er "..."
                            er "Talk!"
                            scene black with Dissolve(1)
                            pause 2
                            stop music fadeout 1.0
                            play music ("Music/Valeria - Emptiness.mp3", "Music/Slow4.mp3", "Music/Slow.mp3") volume 0.4
                            scene 10_060 with Dissolve(1)
                            er "It's been a while since last you were in my room."
                            mc "No, not really. I slept in your bed a couple of weeks ago."
                            er "You did?"
                            mc "Yeah, after you kicked me out of your apartment."
                            er "Oh... Sorry about that."
                        "Slap Erynn's butt[KoGa3AutoWTChange1]{size=-4}(Erynn Week4 Friday Slap, {i}Erynn LikeMC: Erynn Points+2{/i}, {i}else: Erynn Points-2{/i}) {/size} {/color}":
                            $ Erynn_Week4_Friday_Slap = True
                            if Erynn_LikeMC == True:
                                $ Erynn_Points += 2
                                # Erynn (42)
                            else:
                                $ Erynn_Points -= 2
                            scene 10_043 with vpunch
                            n "*Slap*"
                            er "..."
                            scene 10_044 with Dissolve(1)
                            er "Aaah..."
                            me "One!"
                            scene 10_045 with Dissolve(1)
                            er "Hey!"
                            mc "Haha, what?"
                            er "..."
                            scene 10_046 with Dissolve(1)
                            mc "Now I know why you said those pictures aren't that great. If they all look like this. Sheez..."
                            er "Very funny!"
                            mc "And I was right. See! I look so much better!"
                            er "Argh... That's because you... *Sigh* Can you ever take a serious picture?"
                            er "Mom, take another one, please! I'll delete this one."
                            mc "No! It's perfect!"
                            scene 10_047 with Dissolve(1)
                            er "..."
                            me "Ready?"
                            scene 10_048 with Dissolve(1)
                            mc "..."
                            mc "Talking about being serious..."
                            er "Haha. What do you mean? This one is perfect."
                            mc "*Shakes head*"
                            scene 10_043 with vpunch
                            n "*Slap*"
                            scene 10_049 with Dissolve(1)
                            er "Aaah! Mom! [mc] just slapped my ass for the second time!"
                            me "Language!"
                            er "What? There's nothing wrong with saying ass!"
                            scene 10_050 with Dissolve(1)
                            mc "I did no such thing, Melissa."
                            mc "Not without your permission, that is!"
                            me "You don't need my permission to slap her bum."
                            er "MOM!"
                            scene 10_051 with Dissolve(1)
                            mc "Well then..."
                            er "Haha, what are you doing?"
                            scene 10_052 with Dissolve(1)
                            er "Hey."
                            er "HEY!"
                            mc "This is for making us worry."
                            er "That wasn't my fault!"
                            scene 10_053 with vpunch
                            er "AAAH!"
                            er "Mom, do something!"
                            me "Haha."
                            er "Besides laughing!"
                            scene 10_054 with Dissolve(1)
                            er "I'll go to my room."
                            er "Go ahead and slap each other's ASSES for all I care. You've got my permission!"
                            me "Erynn..."
                            scene 10_055 with Dissolve(1)
                            me "You're going with her?"
                            mc "Yeah."
                            me "You know she's planning something, right?"
                            mc "I do. Like mother, like daughter."
                            me "Haha."
                            scene 10_056 with Dissolve(1)
                            me "Thank you, [mc]."
                            mc "Still don't know what I did..."
                            me "I love seeing Erynn this happy and playful, it's been so long. Thank you for being here."
                            if Melissa_Points >= 11:
                                menu:
                                    "Slap her ass":
                                        scene 10_057 with vpunch
                                        me "Hey!"
                                        mc "I got permission!"
                                        scene 10_058 with Dissolve(1)
                                        me "Oh, honey. You're on very thin ice now!"
                                        mc "Haha. As I said, Mel. Bring it on."
                                        me "You are not prepared!"
                                    "Go to Erynn":
                                        pass
                            else:
                                pass
                            scene black with Dissolve(1)
                            pause 2
                            stop music fadeout 1.0
                            play music ("Music/Valeria - Emptiness.mp3", "Music/Slow4.mp3", "Music/Slow.mp3") volume 0.4
                            scene 10_059 with Dissolve(1)
                            mc "{i}(Here she is.){/i}"
                            scene 10_060 with Dissolve(1)
                            mc "Hey."
                            er "Why is she always on your side? I understand when we were younger she helped you, but now..."
                            er "She should be on my side."
                            mc "Trust me, she is. She always has been."
                            er "..."
                            if Erynn_LikeMC == True:
                                scene 10_061 with Dissolve(1)
                                mc "Are you mad at me because I slapped your butt?"
                                er "No."
                                mc "Okay..."
                                scene 10_062 with vpunch
                                n "*Slap*"
                                er "Aaah... Hey! That wasn't an invitation to slap me again. I've got your handprint on one of my cheeks already."
                                mc "Really? Did you check? How does it look? Let me see!"
                                scene 10_063 with Dissolve(1)
                                er "Haha. [mc], no!"
                                er "[mc]!"
                                scene 10_064 with Dissolve(1)
                                er "..."
                                mc "{i}(Damn... I really need to talk to her before...){/i}"
                                mc "{i}(Fuck you, Ethan!){/i}"
                            else:
                                pass
        scene 10_065 with Dissolve(1)
        mc "Sorry... Uhm, I think we need to talk about something."
        er "You became serious all of a sudden."
        mc "Because it is serious, Erynn. *Sigh* It's serious."
        scene 10_066 with Dissolve(1)
        mc "Did you see Ethan today?"
        er "No. He had to be at another modelling show. Why?"
        mc "I met him earlier."
        scene 10_067 with Dissolve(1)
        er "What did he do? He didn't hurt you, or...?"
        mc "No, but uh..."
        er "[mc], what happened?"
        scene black with Dissolve(2)
        pause 2
        scene 10_068 with Dissolve(1)
        er "..."
        mc "Erynn?"
        er "..."
        scene 10_069 with Dissolve(1)
        er "You saw... the video? You saw me..."
        mc "..."
        mc "*Nods*"
        scene 10_070 with Dissolve(1)
        er "*Crying*"
        mc "I'm sorry, Erynn. I'm so sorry this is happening to you."
        er "I hate him... I hate him!"
        if Erynn_Week3_Monday_Blackmailhelp == False:
            scene 10_071 with Dissolve(1)
            er "I should never have dragged you into this."
            mc "I wish I could help you, but..."
            er "I know."
            mc "You need to talk to someone about this, Erynn. If not Melissa, maybe ask my mom or tell Alexis. Anyone who might be able to help you."
            mc "You can't keep doing this."
        else:
            scene 10_071 with Dissolve(1)
            er "I should never have dragged you into this."
            mc "I told you I'm here for you."
            mc "You can't keep doing this."
        scene 10_072 with Dissolve(1)
        er "Maybe I should just..."
        mc "NO! He's not going to delete it, Erynn!"
        er "But he's hurting you too, now."
        mc "I can take care of myself."
        mc "Come here."
        if Erynn_Week3_Monday_Blackmailhelp == False:
            scene 10_073 with Dissolve(1)
            mc "You're going to figure this out."
            mc "As I said. Talk to someone about it."
            er "*Nods*"
        else:
            scene 10_073 with Dissolve(1)
            mc "We're going to figure this out."
            er "*Nods*"
            scene 10_074 with Dissolve(1)
            ""
        scene 10_075 with Dissolve(1)
        er "Can you stay a bit longer?"
        mc "Of course."
        scene black with Dissolve(1)
        pause 2
        scene 10_076 with Dissolve(1)
        ""
        if Erynn_Week3_Monday_Blackmailhelp == False:
            scene 10_077 with Dissolve(1)
            mc "Erynn."
            mc "..."
            mc "Erynn?"
            mc "{i}(Must have fallen asleep.){/i}"
            scene 10_078 with Dissolve(1)
            mc "{i}(I guess I'll take these off for her.){/i}"
            mc "{i}(That should be a little bit more comfortable.){/i}"
            mc "..."
            mc "{i}(Maybe I should've helped her, but what can I do?){/i}"
            mc "*Sigh*"
            jump Week4_Friday_Evening3
        else:
            scene 10_077 with Dissolve(1)
            mc "Erynn."
            mc "..."
            mc "Erynn?"
            scene 10_079 with Dissolve(1)
            er "Hmm?"
            mc "Sorry, were you sleeping?"
            er "Just resting."
            scene 10_080 with Dissolve(1)
            mc "I've been thinking. You said that Ethan's dad is the CEO of the agency, right?"
            er "Yeah, he is."
            mc "Do you think he knows that Ethan is blackmailing you, and maybe even other models and using them as escorts?"
            scene 10_081 with Dissolve(1)
            er "I don't think so, no. If this came to light, it would be a huge scandal for the agency."
            mc "Exactly my thoughts. He wouldn't risk his business for his son's shenanigans."
            mc "So we need to prove to him what Ethan's been doing."
            er "And with prove, you mean the video?"
            scene 10_082 with Dissolve(1)
            mc "No, the video doesn't prove anything. He can simply just deny it or say that you sent it to him."
            er "I would never! I didn't even know he recorded it."
            mc "They don't know that. Same if you went to the police now. It's a 'he said, she said' case."
            mc "Also, the escorting could be masked as a modelling gig. That's how he probably does it."
            er "..."
            scene 10_083 with Dissolve(1)
            mc "The best thing would be that he sees with his own eyes what Ethan makes you do."
            mc "Does he know you work at his agency? Would he recognise you?"
            er "Yeah, he knows me."
            scene 10_084 with Dissolve(1)
            er "So, I have to go on one of those... arrangements and..."
            mc "I think that's the best way."
            er "*Sigh* I hate those men... They're always..."
            mc "Erynn, if you're not comfortable doing this, we..."
            er "No, I..."
            scene 10_085 with Dissolve(1)
            mc "How about this? We ask someone we know and trust who, uhm... hires you, I suppose?"
            mc "That way we have control over it."
            er "Do you know anyone who might help us with this?"
            if Valeria_Week4_Friday_Help == True:
                mc "We'll find someone, don't worry."
            else:
                scene 10_086 with Dissolve(1)
                mc "I have someone in mind. I'm pretty sure he can help in some way."
                mc "I'll talk to him about it."
                er "Do I know him?"
                mc "I don't think so. Do you want to meet him first, before..."
                er "I do."
                scene 10_087 with Dissolve(1)
                mc "I'll call him tomorrow and see when he's free to meet up."
                er "Thank you, [mc]!"
            scene 10_088 with Dissolve(1)
            er "But what about the video? We still need to get the phone."
            mc "That's another problem. Even if we get the phone, who says he doesn't have copies?"
            er "..."
            er "You think he made a copy?"
            mc "I don't know. He's a piece of shit, but he's not stupid."
            mc "{i}(Unlike someone else I know.){/i}"
            scene 10_089 with Dissolve(1)
            mc "But we'll figure this out, too. One step at a time."
            er "*Nods*"
            mc "I guess, for now, try to stay away from Ethan as much as you can."
            mc "Move back here for a while. Since it's spring break, you don't have to be at college anyway."
            scene 10_090 with Dissolve(1)
            er "I'll do that."
            mc "Do you have any more gigs coming up?"
            er "I have a photo shoot next week."
            mc "I'll join you then. If that's allowed."
            if Erynn_LikeMC == True:
                er "I'd love that!"
                scene 10_091 with Dissolve(1)
                er "..."
                mc "..."
            else:
                er "I'd like that."
            scene 10_092 with Dissolve(1)
            mc "I guess it's time for me to go home now."
            er "Uh... Yeah."
            mc "I'll speak to you tomorrow."
            scene 10_093 with Dissolve(1)
            er "[mc]?"
            mc "Hmm?"
            if Erynn_LikeMC == True:
                er "Thank you again. And... Uh... No, nothing."
                mc "Okay... Can you do me one favour though? I know it's scary, but please talk to Melissa. She worries so much about you, and she needs to know this, Erynn. Please!"
            else:
                er "Thank you again."
                mc "Can you do me one favour though? I know it's scary, but please talk to Melissa. She worries so much about you, and she needs to know this, Erynn. Please!"
            er "I will."
            scene 10_094 with Dissolve(1)
            mc "Thank you!"
            mc "Good night, Erynn."
            er "Bye, [mc]."
            jump Week4_Friday_Evening3

label Week4_Friday_Evening2_Alexis:
    scene black with Dissolve(1)
    pause 2
    scene 10_005 with Dissolve(1)
    mc "{i}(Seriously, where is that girl?){/i}"
    mc "Do you know of some other places she usually hangs out?"
    a "Yeah, let's go to..."
    play sound "Sounds/Phone_Vibrate.mp3"
    n "*Bzzzt. Bzzzt*"
    scene 10_006 with Dissolve(1)
    mc "Erynn?"
    a "..."
    me "It's me."
    mc "Mel. Any news?"
    scene 10_003 with Dissolve(1)
    me "She just called me."
    mc "*Sigh* What a relief. What happened?"
    me "They had some problems at the photo shoot and had to redo everything."
    mc "Problems?"
    scene 10_007 with Dissolve(1)
    me "Lighting issues and there was some drama with the photographer and... She can tell you all about it."
    mc "Where is she now?"
    me "She's on her way here."
    mc "Okay, we're coming back then."
    me "We?"
    mc "Yeah, Alexis is here with me."
    scene 10_008 with Dissolve(1)
    stop music fadeout 1.0
    play music ("Music/LoFi Upbeat 1.mp3", "Music/LoFi Upbeat 2.mp3", "Music/LoFi Upbeat 3.mp3", "Music/LoFi Upbeat 4.mp3") volume 0.2
    mc "That was Melissa. Erynn just called her."
    a "What happened? Is she alright?"
    mc "Yeah. Some problems at the photo shoot, it seems."
    scene 10_009 with Dissolve(1)
    a "Oh my god. I'm so happy she's okay."
    mc "Me too."
    a "Let's leave, I'll drive you home."
    scene black with Dissolve(2)
    pause 2
    scene 10_010 with Dissolve(1)
    mc "Thank you for driving me."
    a "You're welcome."
    mc "I hope you asked your dad this time before you took his car."
    scene 10_011 with Dissolve(1)
    a "I didn't have time to ask."
    mc "Lexi..."
    a "..."
    mc "You like doing chores, huh?"
    scene 10_012 with Dissolve(1)
    a "Haha, noooo..."
    a "I was in a hurry, so I just grabbed the keys and left."
    mc "*Sigh* Since I called you, I'll help you this time."
    scene 10_013 with Dissolve(1)
    a "Thank you, [mc]."
    scene 10_014 with Dissolve(1)
    a "Alright. Call me later or tomorrow and tell me what happened, okay?"
    mc "No, I'm not calling you. You're coming with me."
    a "I'm not. She doesn't want to see me."
    mc "I don't care what she wants. I gave her plenty of time."
    a "[mc]..."
    mc "You're coming!"
    scene black with Dissolve(1)
    pause 2
    scene 10_015 with Dissolve(1)
    mc "Hey, Mel."
    me "Hey. Haven't seen you for quite a while, Alexis."
    a "Good evening, Melissa."
    scene 10_016 with Dissolve(1)
    me "How are you?"
    a "I'm good, thanks. How are you?"
    me "Much better after Erynn finally called. And thank you for helping to look for her."
    a "Of course."
    scene 10_017 with Dissolve(1)
    me "Thank you, [mc]."
    mc "I didn't do anything."
    me "That's not true. You immediately went looking for her. So, thank you!"
    scene 10_018 with Dissolve(1)
    me "Why aren't you coming over anymore? It's been weeks."
    a "Uhm..."
    me "I asked Erynn before, and she said you were busy?"
    a "We..."
    mc "They're in a fight."
    scene 10_019 with Dissolve(1)
    a "..."
    me "What?"
    mc "They've been fighting for a few weeks now, and they're too stubborn to talk it out."
    me "Fighting about what?"
    mc "Something stupid."
    mc "{i}(I just called myself stupid...){/i}"
    scene 10_020 with Dissolve(1)
    me "Don't worry. You've been best friends since you were seven."
    me "Remember that guy in high school who tried to break you apart? Adam or something?"
    mc "{i}(Ethan...){/i}"
    me "He couldn't do it, so this something stupid won't either."
    mc "{i}(Thanks, Melissa...){/i}"
    a "Yeah."
    scene 10_021 with Dissolve(1)
    mc "Melissa. Can we maybe wait inside?"
    mc "I mean, if Erynn sees us all together, she might think this is some kind of intervention."
    me "Haha, you might be right."
    me "You can wait in her room, you both know where it is. I'll send her up once she's here."
    mc "Thank you."
    scene black with Dissolve(1)
    pause 2
    scene 10_095 with Dissolve(1)
    a "It's been a while since I was in this room."
    a "I'm actually nervous."
    mc "That's a good thing. It means you care."
    scene 10_096 with Dissolve(1)
    mc "Don't just stand there, come sit down."
    scene 10_097 with Dissolve(1)
    a "*Sigh*"
    mc "Don't worry. It'll be fine."
    a "What if she doesn't want to talk?"
    mc "As I said, I won't give her a choice."
    scene 10_098 with Dissolve(1)
    ""
    scene 10_099 with Dissolve(1)
    ""
    scene 10_100 with Dissolve(1)
    a "..."
    scene 10_101 with Dissolve(1)
    a "[mc], stop!"
    a "Not now! Not in this room!"
    scene 10_102 with Dissolve(1)
    a "It's going to be too much already for Erynn if she sees us both in her room."
    a "If she sees us making out on her bed, she's never gonna talk to us again."
    mc "You're right, I'm sorry."
    scene 10_103 with Dissolve(1)
    mc "So now you're just gonna stand there and wait until she comes?"
    a "Yes! And you stay where you are!"
    mc "..."
    scene 10_104 with Dissolve(1)
    mc "It's a good idea, actually."
    a "Hmm?"
    mc "I'll distract her when she walks through the door, and you grab her from behind. That way she can't escape."
    a "Nooo... Haha."
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 10_105 at moveup
    pause 3
    mc "You know, you look really hot just standing there."
    mc "Mmm-mmm-mmm..."
    a "Stop!"
    scene 10_106 with Dissolve(1)
    mc "What? I can't compliment you, either?"
    a "No!"
    mc "Okay... I'll be quiet from now on."
    a "Good."
    scene 10_107 with Dissolve(1)
    mc "Oh, by the way. What do..."
    a "Wow, that didn't even last two seconds."
    mc "..."
    mc "Never mind then."
    scene black with Dissolve(1)
    pause 2
    stop music fadeout 1.0
    play music ("Music/Valeria - Emptiness.mp3", "Music/Slow4.mp3", "Music/Slow.mp3") volume 0.4
    scene 10_108 with Dissolve(1)
    mc "She's here! I can hear her coming up the stairs."
    a "Yeah."
    scene 10_109 with Dissolve(1)
    mc "Hey, Erynn."
    er "Hey?"
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 10_110 at moveup
    pause 3
    er "What are you doing here?"
    mc "Checking up on you."
    er "Heh..."
    scene 10_111 with Dissolve(1)
    mc "Are you okay?"
    er "I am. Sorry for worrying you. Mom told me she'd sent you looking for me."
    scene 10_112 with Dissolve(1)
    a "Hey, Erynn."
    er "..."
    scene 10_113 with Dissolve(1)
    er "And what are you doing here, Alexis?"
    a "I was worried about you, I..."
    scene 10_114 with Dissolve(1)
    mc "I called her."
    mc "We couldn't reach you, so I called Alexis to ask if she knew some places you could be."
    mc "She offered... Demanded to help look for you."
    scene 10_115 with Dissolve(1)
    er "Thank you for worrying about me."
    er "But as you can see, I'm alright, so..."
    scene 10_116 with Dissolve(1)
    n "*Click*"
    a "..."
    er "Hey!"
    scene 10_117 with Dissolve(1)
    er "[mc]! What are you doing? Open the door!"
    mc "Not until you guys have talked. I've given you plenty of time."
    er "[mc]!"
    mc "[mc] me all you want. I'm not opening the door unless you talk it out."
    mc "And guess what? It's spring break, so I have plenty of time."
    scene 10_118 with Dissolve(1)
    er "..."
    er "FINE!"
    mc "And Erynn. Tell her!"
    er "Tell her what?"
    mc "You know what!"
    scene 10_119 with Dissolve(1)
    er "I can't."
    mc "Yes, you can. You need to talk about this. You need to talk to other people, so we can help you!"
    er "..."
    mc "Please, Erynn!"
    er "*Sigh*"
    scene 10_120 with Dissolve(1)
    mc "Call me if you need something to drink or anything."
    er "I need to go to the bathroom."
    mc "I'll get a bucket."
    er "[mc]!"
    mc "Kidding! I'm no sadist, I'll get two. One for each of you."
    scene 10_121 with Dissolve(1)
    er "..."
    er "He's such an idiot sometimes."
    a "I know."
    scene 10_122 with Dissolve(1)
    er "*Sigh*"
    er "Come, sit down. You don't have to stand there the whole time."
    a "Thank you."
    scene 10_123 with Dissolve(1)
    mc "Hey."
    me "Hey..."
    mc "Do you have a bucket, Mel?"
    me "Why do you need a bucket?"
    mc "Heh, never mind."
    scene 10_124 with Dissolve(1)
    me "The girls are still upstairs?"
    mc "Yeah, I locked them in Erynn's room until they've talked."
    mc "I'll check on them in thirty minutes or so. Or when we hear some screaming."
    me "Oh boy..."
    scene black with Dissolve(1)
    pause 2
    n "An hour or so later."
    scene 10_125 with Dissolve(1)
    mc "{i}(They're actually talking and smiling.){/i}"
    mc "{i}(I didn't expect that, to be honest.){/i}"
    scene 10_126 with Dissolve(1)
    a "Haha. He would do that!"
    mc "Heh..."
    scene 10_127 with Dissolve(1)
    er "You scared me, [mc]!"
    a "How long have you been standing there?"
    mc "I just came in. Don't worry. I didn't hear anything you guys talked about."
    scene 10_128 with Dissolve(1)
    mc "So, we're finally all friends again?"
    er "We've always been friends, we were just on a break."
    mc "Oh... A break. That makes so much sense..."
    er "Haha."
    menu:
        "Kiss Erynn[KoGa3AutoWTChange1]{size=-4}(Erynn Points+2) {/size} {/color}":
            $ Erynn_Points += 2
            # Erynn (42)
            scene 10_129 with Dissolve(1)
            ""
        "Kiss Alexis[KoGa3AutoWTChange1]{size=-4}(Alexis Points+2) {/size} {/color}":
            $ Alexis_Points += 2
            # Alexis (42)
            scene 10_130 with Dissolve(1)
            ""
        "Kiss both[KoGa3AutoWTChange1]{size=-4}(Alexis Points+2, Erynn Points+2) {/size} {/color}":
            $ Alexis_Points += 2
            # Alexis (42)
            $ Erynn_Points += 2
            # Erynn (42)
            scene 10_129 with Dissolve(1)
            ""
            scene 10_130 with Dissolve(1)
            ""
    scene 10_131 with Dissolve(1)
    mc "Did you tell Alexis?"
    er "No... I didn't. I can't..."
    mc "Erynn!"
    scene 10_132 with Dissolve(1)
    er "I don't want to involve her, [mc]."
    a "What are you talking about?"
    menu:
        "Alexis is already involved[KoGa3AutoWTChange1]{size=-4}(Alexis Week4 Friday Blackmail Involve) {/size} {/color}":
            $ Alexis_Week4_Friday_Blackmail_Involve = True
            mc "She's already involved, Erynn. Ethan involved her."
            er "What do you mean?"
        "You need to talk about this":
            mc "You need to talk to other people about this so they can help you."
            mc "Nothing's gonna change if you keep this to yourself."
    scene 10_133 with Dissolve(1)
    mc "Did you speak to Ethan today?"
    er "No, I didn't see him. He had to be at another modelling show. Why?"
    mc "Well, I met him."
    er "Did he do something to you?"
    mc "Well, he..."
    scene black with Dissolve(1)
    pause 2
    scene 10_134 with Dissolve(1)
    er "You... You saw the video?"
    mc "I'm sorry. I didn't have a choice."
    scene 10_135 with Dissolve(1)
    a "What video?"
    a "Can someone tell me what's going on?"
    mc "Erynn... Please, tell her."
    scene 10_136 with Dissolve(1)
    er "..."
    er "Remember prom? When I went with Ethan?"
    a "Yes..."
    scene black with Dissolve(2)
    pause 2
    scene 10_137 with Dissolve(1)
    a "I'm sorry this is happening to you, Erynn! I'm so sorry!"
    a "I understand why you don't want to involve me, but you should've told me."
    a "I'm here for you. Anytime you need me."
    scene 10_138 with Dissolve(1)
    a "We've gotten rid of Ethan before and we will again."
    a "He's never gonna win. He's never gonna get you!"
    a "We'll figure it out, okay?"
    er "*Nods*"
    scene 10_139 with Dissolve(1)
    a "When did you find out about this?"
    mc "Maybe two weeks ago?"
    a "Why didn't you tell me?"
    scene 10_140 with Dissolve(1)
    mc "I promised Erynn I wouldn't tell anyone. It was something she had to explain."
    mc "Also, the same reason you didn't tell me who you were at first, or tell Erynn about us. We're all scared of what the other will think."
    a "You're right. I sound like a hypocrite, I'm sorry."
    a "I know me not telling was wrong, and I still feel bad about it."
    scene 10_141 with Dissolve(1)
    er "Hey, don't fight because of me."
    a "We're not fighting. This was my fault to begin with, and I'm sorry about that again, Erynn."
    if Alexis_Week4_Friday_Blackmail_Involve == True:
        scene 10_142 with Dissolve(1)
        a "You said earlier that I was already involved, or rather Ethan involved me. What did you mean by that?"
        mc "It was just something he said. He knows we're dating and..."
        mc "*Sigh* He probably just said it to rile me up."
        scene 10_143 with Dissolve(1)
        a "What did he say, [mc]?"
        mc "..."
        a "[mc], please?"
        scene 10_144 with Dissolve(1)
        mc "*Sigh* He... He said he'll delete the video if you give him a blowjob."
        er "..."
        a "What? He..."
        scene 10_145 with Dissolve(1)
        a "That disgusting pig!"
        er "I'm sorry, Lexi."
        a "You have nothing to be sorry for. This is all Ethan's doing!"
    else:
        pass
    scene black with Dissolve(1)
    pause 2
    if Erynn_Week3_Monday_Blackmailhelp == False:
        $ Alexis_Points -= 10
        scene 10_146 with Dissolve(1)
        a "Do you have any idea what we can do?"
        mc "I've told Erynn before that I can't really help her and my involvement will make it even worse."
        a "..."
        a "So, you're not going to do anything?"
        mc "The best thing I can think of is that Erynn needs to talk to Melissa."
        scene 10_147 with Dissolve(1)
        a "With that I agree. You need to tell your mom, Erynn."
        er "I'm scared of what she'll think of me when..."
        a "She won't think less of you. Quite the opposite, actually."
        a "Let's go talk to her now. Don't drag this on any further."
        scene 10_148 with Dissolve(1)
        mc "I'll go home then, and let you guys talk in peace."
        mc "If you need me, just call me."
        mc "We'll talk tomorrow, okay?"
        er "*Nods*"
        scene 10_149 with Dissolve(1)
        mc "You're strong. You'll figure it out!"
        er "Thanks for being here for me today, [mc]."
        mc "Bye, Erynn."
        scene 10_150 with Dissolve(1)
        mc "Bye, Lexi."
        a "..."
        a "Bye."
        jump Week4_Friday_Evening3
    else:
        scene 10_151 with Dissolve(1)
        a "So now we need to find a way to get his phone?"
        mc "Even if we get the phone, who says he doesn't have copies?"
        er "..."
        a "You think he made a copy?"
        mc "I don't know. He's a piece of shit, but he's not stupid."
        mc "{i}(Unlike someone else I know.){/i}"
        scene 10_152 with Dissolve(1)
        mc "Erynn. Didn't you say that Ethan's dad is the CEO of the agency?"
        er "Yes, he is."
        mc "Do you think he knows that Ethan is blackmailing you, and maybe even other models, and using you as an escort?"
        scene 10_153 with Dissolve(1)
        er "I don't think so, no. If this came to light, it would be a huge scandal for the agency."
        mc "Exactly my thoughts. He wouldn't risk his business for his son's shenanigans."
        mc "So we need to prove to him what Ethan's been doing."
        er "And with prove, you mean the video?"
        scene 10_154 with Dissolve(1)
        mc "No, that doesn't prove anything. He can simply just deny it or say that you sent it to him."
        er "I would never! I didn't even know he recorded it."
        mc "They don't know that. Same if you went to the police now. It's a 'he said, she said' case."
        mc "Also, the escorting could be masked as a modelling gig. That's how he probably does it."
        er "..."
        scene 10_155 with Dissolve(1)
        a "The video may not prove anything, but it would probably make him aware or suspicious of what's going on, no?"
        mc "Hmm, true. But it would be best if he saw it with his own eyes. I mean the things Ethan is doing, the escorting."
        mc "Does he know you work at his agency? Would he recognise you?"
        er "Yeah, he knows me. He's the one who scouted me."
        scene 10_156 with Dissolve(1)
        er "So, you want me to go on one of those... arrangements and..."
        mc "I think that's the best way."
        er "..."
        er "*Sigh* I hate those men... They're always..."
        scene 10_157 with Dissolve(1)
        mc "Erynn, it was just an idea. If you're not comfortable doing this, we..."
        er "No, I..."
        scene 10_158 with Dissolve(1)
        mc "How about this? We ask someone we know and trust who, uhm... hires you, I suppose?"
        mc "That way we have control over it."
        er "Do you know anyone who might help us with this?"
        if Valeria_Week4_Friday_Help == True:
            mc "We'll find someone, don't worry."
            scene 10_159 with Dissolve(1)
            a "I can ask my dad. You know he likes you a lot. I'm sure he'll do this for you."
            er "Thank you, I like him too. But I don't want to involve him in this. And I think he's too famous, and it can ruin his reputation. Besides, I'm sure Ethan knows him too, and might suspect some kind of set-up."
            mc "{i}(Famous? Am I missing something?){/i}"
            mc "{i}(She probably just means that Ethan's seen him before.){/i}"
        else:
            scene 10_159 with Dissolve(1)
            a "I can ask my dad. You know he likes you a lot. I'm sure he'll do this for you."
            er "Thank you, I like him too. But I don't want to involve him in this. And I think he's too famous, and it can ruin his reputation. Besides, I'm sure Ethan knows him too, and might suspect some kind of set-up."
            mc "{i}(Famous? Am I missing something?){/i}"
            mc "{i}(She probably just means that Ethan's seen him before.){/i}"
            scene 10_160 with Dissolve(1)
            mc "I have someone in mind. I'm pretty sure he can help in some way."
            er "You do?"
            mc "I'll talk to him about it."
            er "Do we know him?"
            mc "I don't think so. Do you want to meet him first, before..."
            er "I do."
            scene 10_161 with Dissolve(1)
            mc "I'll call him tomorrow and see when he's free to meet up."
            er "Thank you, [mc]!"
            mc "I guess, for now, try to stay away from Ethan as much as you can."
            mc "Move back here for a while. Since it's spring break, you don't have to be at college anyway."
            er "I'll do that. I have stuff here from last week, anyway."
        scene 10_162 with Dissolve(1)
        mc "Do you have any more gigs coming up?"
        er "I have a photo shoot next week."
        mc "I'll join you then. If that's allowed."
        er "I'd like that."
        scene black with Dissolve(1)
        pause 2
        scene 10_163 with Dissolve(1)
        mc "I guess it's time for me to slowly head on home."
        er "Okay."
        mc "I'll speak to you tomorrow."
        scene 10_149 with Dissolve(1)
        er "Thank you for being here for me, [mc]."
        mc "Of course."
        scene 10_164 with Dissolve(1)
        mc "One more thing, Erynn. Please talk to Melissa."
        er "..."
        mc "I know it's scary, but she worries so much about you, and she needs to know this, Erynn. Please!"
        er "I will."
        scene 10_165 with Dissolve(1)
        mc "Are you coming with me, or...?"
        a "I'm staying a bit longer. I'll call you later or tomorrow, okay?"
        mc "Sure."
        scene 10_150 with Dissolve(1)
        ""
        scene 10_166 with Dissolve(1)
        mc "Bye, girls. And don't fight!"
        er "We won't."
        mc "Good! Or else I'll lock you up again. And don't talk about me!"
        a "We wo... No, we probably will."
        mc "..."
        scene 10_167 with Dissolve(1)
        er "Haha. Good night, [mc]."
        mc "Bye!"
        a "Good night!"
        jump Week4_Friday_Evening3

label Week4_Friday_Evening3:
    scene black with Dissolve(1)
    pause 2
    stop music fadeout 1.0
    play music ("Music/LoFi Indie 3.mp3", "Music/LoFi Indie 1.mp3", "Music/LoFi Indie 2.mp3") volume 0.2
    scene 10_168 with Dissolve(1)
    m "Hey. You're back."
    mc "*Sigh* Hey, Mom."
    scene 10_169 with Dissolve(1)
    m "Everything alright?"
    mc "I don't know. Just lots going on today."
    m "Sit down for a second."
    if Emily_Week3_Sunday_Surprise == False:
        scene 10_170 with Dissolve(1)
        m "Thank you for looking for Erynn. Melissa called me before and told me she's alright."
        mc "Some drama at the photo shoot."
        scene 10_171 with Dissolve(1)
        m "So, what happened to you?"
        mc "Nothing. I was wrong about someone, that's it."
        m "Hmm?"
        if Nikki_Girlfriend == True:
            scene 10_172 with Dissolve(1)
            m "Oh, the new bed arrived. I haven't been able to set it up yet, though."
            mc "I'll do it tomorrow. I'll just put the mattress down for tonight."
            mc "Is Nikki back already?"
            m "Yes, she's upstairs."
            scene 10_173 with Dissolve(1)
            mc "I'm gonna see what she's been up to all day."
            mc "Good night, Mom."
            m "Good night, honey."
            jump Week4_Friday_Evening_Nikki
        else:
            if Cara_Girlfriend == True:
                scene 10_172 with Dissolve(1)
                m "Oh, the new bed arrived. I haven't been able to set it up yet, though."
                mc "I'll do it tomorrow. I'll just put the mattress down for tonight."
                mc "Is Cara back already?"
                m "Yes, she's upstairs."
                scene 10_173 with Dissolve(1)
                mc "I'm gonna see what she's been up to all day."
                mc "Good night, Mom."
                m "Good night, honey."
                jump Week4_Friday_Evening_Cara
            else:
                scene 10_173 with Dissolve(1)
                mc "I guess I'm going to bed for today."
                m "You sure you're okay?"
                mc "Just tired. Good night, Mom."
                m "Good night, honey."
                jump Week4_Friday_Evening4
    else:
        scene 10_174 with Dissolve(1)
        m "Thank you for..."
        m "What's wrong?"
        mc "Are you going to hug me or kiss me again?"
        scene 10_175 with Dissolve(1)
        m "Both!"
        mc "Haha."
        scene 10_176 with Dissolve(1)
        m "As I was saying, thank you for looking for Erynn. Melissa called me before and told me she's alright."
        mc "Some drama at the photo shoot."
        scene 10_172 with Dissolve(1)
        m "And, what happened to you?"
        mc "Nothing... *Sigh* I was wrong about someone, that's it."
        m "Hmm?"
        scene 10_177 with Dissolve(1)
        m "Come..."
        mc "What?"
        m "Put your head down."
        scene 10_178 with Dissolve(1)
        mc "What are you smiling about?"
        m "Looking at this pretty boy I created."
        mc "Heh... You're so weird sometimes."
        scene 10_179 with Dissolve(1)
        m "I'm the weird one?"
        mc "I must have gotten it from someone."
        m "Haha."
        scene 10_180 with Dissolve(1)
        mc "Good thing that's not the only thing I got from you."
        m "*Shakes head* Thanks... You're just like your dad. Lots of compliments..."
        mc "Santiago?"
        m "Uh-huh. How does this feel?"
        mc "Great!"
        m "He also liked it when I ran my fingers through his hair."
        scene black with Dissolve(1)
        pause 2
        if Nikki_Girlfriend == True:
            scene 10_181 with Dissolve(1)
            mc "Is Nikki back already?"
            m "Yes, she was dropped off by her dad a few minutes after you went looking for Erynn. I think she's upstairs."
            m "I didn't know her dad lives here as well."
            mc "Neither did she. Did you talk to her?"
            m "We talked a bit, yes."
            scene 10_182 with Dissolve(1)
            mc "I guess I'll go check up on her."
            m "Yeah, do that. I'm going to bed."
            mc "Thanks for the head massage."
            m "You're welcome!"
            scene 10_183 with Dissolve(1)
            mc "Good night, Mom."
            m "Good night, honey."
            jump Week4_Friday_Evening_Nikki
        else:
            if Cara_Girlfriend == True:
                scene 10_181 with Dissolve(1)
                mc "Is Cara back already?"
                m "Yes, she was dropped off by her dad a few minutes after you went looking for Erynn. I think she's upstairs."
                m "I didn't know her dad lives here as well."
                mc "Neither did she. Did you talk to her?"
                m "We talked a bit, yes."
                scene 10_182 with Dissolve(1)
                mc "I guess I'll go check up on her."
                m "Yeah, do that. I'm going to bed."
                mc "Thanks for the head massage."
                m "You're welcome!"
                scene 10_183 with Dissolve(1)
                mc "Good night, Mom."
                m "Good night, honey."
                jump Week4_Friday_Evening_Cara
            else:
                scene 10_184 with Dissolve(1)
                m "[mc]..."
                m "[mc]?"
                mc "Hmm?"
                m "Let's go to bed."
                scene 10_182 with Dissolve(1)
                mc "Sorry, must have dozed off. I enjoyed those head scratches. Thank you."
                m "You're welcome."
                mc "Are you working tomorrow?"
                m "No, but Sunday I am."
                mc "Alright."
                scene 10_183 with Dissolve(1)
                mc "Good night, Mom."
                m "Good night, honey."
                jump Week4_Friday_Evening4

label Week4_Friday_Evening_Nikki:
    if _in_replay:
        $ Nikki_Visit_Points = 30
        $ Nikki_Week4_Wednesday_Visit_Knows = False
    scene black with Dissolve(1)
    pause 2
    scene 10_185 with Dissolve(1)
    ni "Oh hey, you're back!"
    mc "Hi."
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 10_186 at moveup
    pause 3
    mc "Do you always run around other people's homes like that?"
    ni "Always!"
    scene 10_187 with Dissolve(1)
    ni "How was your date?"
    mc "Heh... Date... If that was an actual date, it would've been terrible, to say the least."
    ni "Oh? Did something happen?"
    if Nikki_Week4_Wednesday_Visit_Knows == False:
        menu:
            "Grab her[KoGa3AutoWTChange1]{size=-4}(Nikki Week4 Friday Oral) {/size} {/color}":
                $ Nikki_Week4_Friday_Oral = True
                scene 10_188 with vpunch
                ni "Aah..."
                mc "Not worth talking about. I'd rather do this."
                ni "Haha."
                scene 10_189 with Dissolve(1)
                mc "I missed you today!"
                ni "Same here."
                scene 10_190 with Dissolve(1)
                ""
                scene 10_191 with Dissolve(1)
                mc "..."
                scene 10_192 with Dissolve(1)
                ni "Ah..."
                ni "[mc]!"
                scene 10_193 with Dissolve(1)
                ni "They're not edible, you know?"
                scene 10_194 with Dissolve(1)
                mc "It was worth a try. It tasted great though."
                ni "Heh..."
                mc "Let's take 'em off."
                scene 10_195 with Dissolve(1)
                ""
                scene 10_196 with Dissolve(1)
                ""
                scene 10_197 with Dissolve(1)
                ni "..."
                scene 10_198 with Dissolve(1)
                ""
                scene 10_199 with Dissolve(1)
                ""
                scene 10_200 with vpunch
                ni "Haha. Careful! We have plenty of time!"
                scene 10_201 with Dissolve(1)
                ""
                scene 10_202 with Dissolve(1)
                ""
                scene 10_203 with Dissolve(1)
                ni "*Moaning*"
                mc "{i}(Her moans are getting louder.){/i}"
                scene 10_204 with Dissolve(1)
                mc "{i}(And she's starting to ride my face){/i}"
                scene 10_205 with Dissolve(1)
                ""
                scene 10_206 with Dissolve(1)
                ni "F-Fuck!"
                mc "{i}(That's the first time I've heard her swear!){/i}"
                ni "[mc]... Keep going..."
                scene 10_207 with Dissolve(1)
                ni "*Heavy breathing*"
                ni "Haah... Mmm..."
                scene 10_208 with Dissolve(1)
                ni "[mc]... I'm..."
                ni "Ahhh..."
                ni "I'm..."
                scene 10_209 with Dissolve(1)
                ni "Nnnggh..."
                scene 10_210 with Dissolve(1)
                mc "..."
                mc "{i}(What the...){/i}"
                scene 10_211 with Dissolve(1)
                ni "..."
                ni "Sorry... I..."
                scene 10_212 with Dissolve(1)
                mc "Uh... Wow... Did you...?"
                ni "*Nods*"
                mc "I didn't know you can squirt."
                ni "Neither did I..."
                scene 10_213 with Dissolve(1)
                mc "Mmm."
                ni "Don't do that!"
                scene 10_214 with vpunch
                mc "You're the one who squirted on my face."
                ni "It wasn't on purpose. And it surely wasn't an invitation to taste it!"
                mc "It doesn't taste like anything. It's a little sweet though."
                ni "I don't want to know!"
                mc "Haha."
                scene 10_215 with Dissolve(1)
                mc "You're still shaking."
                ni "I know. Do you have any idea what you just did to me? Fuck!"
                mc "Haha."
                ni "You have a knack for embarrassing me."
                mc "Hey! This one's on you!"
                ni "Haha."
                scene 10_216 with Dissolve(1)
                ni "I'm gonna put some other clothes on."
                mc "Me too. This shirt is drenched."
                ni "Drenched... It wasn't that much."
                mc "I'm the one who got sprayed on, so I'll be the judge of that."
                ni "..."
                scene 10_217a with Dissolve(1)
                ni "Speaking of shirts."
                mc "Hmm?"
                scene 10_218 with Dissolve(1)
                ni "Here you go."
                mc "What's this?"
                ni "I bought you a new shirt, since I ripped the other one."
                mc "Oh, thank you."
            "Nothing worthwhile":
                mc "Nothing worth talking about."
                scene 10_217 with Dissolve(1)
                ni "Let me change real quick."
                ni "But first, before I forget. I got you something."
                mc "Hmm?"
                scene 10_218 with Dissolve(1)
                ni "Here you go."
                mc "What's this?"
                ni "I bought you a new shirt, since I ripped the other one."
                mc "Oh, thank you."
    else:
        mc "Nothing worth talking about."
        scene 10_217 with Dissolve(1)
        ni "Let me change real quick."
        ni "But first, before I forget. I got you something."
        mc "Hmm?"
        scene 10_218 with Dissolve(1)
        ni "Here you go."
        mc "What's this?"
        ni "I bought you a new shirt, since I ripped the other one."
        mc "Oh, thank you."
    scene 10_219 with Dissolve(1)
    ni "Try it on to see if it fits, or we can exchange it tomorrow."
    ni "I fitted it to my dad, and you're about the same size, I'd say."
    mc "The same size, huh...?"
    ni "Not that!"
    scene 10_220 with Dissolve(1)
    ni "Just try it on! Be right back."
    mc "Haha."
    $ renpy.end_replay()
    scene black with Dissolve(1)
    pause 2
    scene 10_221 with Dissolve(1)
    mc "What do you think?"
    ni "Heh... You didn't find any pants?"
    mc "There weren't any in the bag you gave me."
    ni "..."
    scene 10_222 with Dissolve(1)
    ni "It looks good though, right?"
    mc "Yeah, I like it. Thank you, Nikki!"
    ni "You're welcome."
    scene 10_223 with Dissolve(1)
    mc "Let me put it away for now. I don't want to dirty it."
    if Alexis_Dating == True:
        play sound "Sounds/Phone_Vibrate.mp3"
        n "*Bzzzt. Bzzzt*"
        scene 10_224 with Dissolve(1)
        ni "Who's Alexis?"
        mc "What?"
        ni "Alexis... She's calling you."
        mc "..."
        scene 10_225 with Dissolve(1)
        mc "Give me a second. This might be important."
        ni "..."
        scene black with Dissolve(1)
        pause 2
        scene 10_226 with Dissolve(1)
        mc "Hey."
        a "Hey. Sorry I'm calling so late."
        mc "It's not that late. How are you?"
        scene 10_227 with Dissolve(1)
        a "I'm good."
        mc "How about Erynn?"
        a "She talked to Melissa."
        mc "That's great. The more people who know, the more can help her."
        scene 10_228 with Dissolve(1)
        a "*Sigh*"
        mc "What?"
        a "I'm such a bad friend."
        mc "Lexi, you're not!"
        a "I am. This has been going on for months and I didn't even notice anything."
        scene 10_229 with Dissolve(1)
        mc "You couldn't have known. She hid it from everyone."
        a "Still, I..."
        mc "Lexi! This is not your fault! So stop thinking it's your fault!"
        a "..."
        mc "Did you get in trouble? Because you took the car?"
        scene 10_230 with Dissolve(1)
        a "No. I explained what happened to Dad, and he said it was fine. He's always had a soft spot for Erynn."
        mc "No extra chores?"
        a "Heh, no. Not this time, at least."
        mc "Nice. So I don't have to come over and help out."
        scene 10_231 with Dissolve(1)
        a "But you can come over for other things."
        mc "What other things are you talking about?"
        a "Hmm... Come over and find out!"
        if Nikki_Week4_Friday_Oral == True:
            mc "{i}(I want to, but I can't... Not after what I just did with Nikki...){/i}"
        else:
            mc "{i}(I want to, but I can't... Not with Nikki still here.){/i}"
        mc "How about I come tomorrow?"
        scene 10_232 with Dissolve(1)
        a "I can't tomorrow. I'm gonna spend the day with Erynn."
        mc "Sunday?"
        a "Can't Sunday either, sorry."
        scene 10_233 with Dissolve(1)
        mc "*Sigh* What a great start to spring break."
        a "Haha, sorry. You want to see me that bad?"
        mc "Well, yeah..."
        a "How about Monday then? I don't have to work, I'm free all day."
        scene 10_234 with Dissolve(1)
        mc "Monday it is, then. I'll pick you up in the afternoon, and we'll go somewhere for a change."
        a "Can't wait."
        mc "Okay, see you on Monday then. Good night, Alexis!"
        scene 10_235 with Dissolve(1)
        a "LEXI!"
        mc "Haha. That's what I meant!"
        a "..."
        a "Good night... Albert!"
        mc "Albert? Haha."
        scene 10_236 with Dissolve(1)
        mc "Oh, I get it. Einstein. From back when we met on the aeroplane."
        mc "Good one."
        mc "..."
        mc "{i}(She hung up already...){/i}"
        play sound "Sounds/Phone_Message.mp3"
        n "*Bzzzt*"
        scene 10_237 with Dissolve(1)
        mc "{i}(Haha, yep. Definitely Einstein!){/i}"
        mc "{i}(She looks as crazy as him. Haha, this is too funny.){/i}"
        if Valeria_Week4_Friday_Help == True:
            mc "{i}(Why do girls keep sticking out their tongues, though?){/i}"
            mc "{i}(Reminds me of Valeria. She did the same today.){/i}"
            mc "{i}(Maybe I should call her and ask how she's doing, after what happened.){/i}"
            menu:
                "Call Valeria[KoGa3AutoWTChange1]{size=-4}(Valeria Points+2) {/size} {/color}":
                    $ Valeria_Points += 2
                    # Valeria (20)
                    scene 10_238 with Dissolve(1)
                    mc "..."
                    mc "{i}(Not picking up. She might be asleep already.){/i}"
                    mc "..."
                    mc "{i}(Or... Don't tell me that...){/i}"
                    va "Hi!"
                    scene 10_239 with Dissolve(1)
                    mc "Hey. Sorry, did I wake you?"
                    va "No, you didn't. I had my phone on silent because I'm watching TV."
                    mc "Ah, okay."
                    scene 10_240 with Dissolve(1)
                    mc "How are you?"
                    x "Who's calling you so late?"
                    va "A friend from school."
                    x "I'm going to bed. Don't make it too late, okay?"
                    va "I won't."
                    scene 10_241 with Dissolve(1)
                    x "Buenas Noches, cariño."
                    va "Buenas Noches."
                    scene 10_242 with Dissolve(1)
                    va "Sorry. You were saying?"
                    mc "I asked how you are."
                    va "I'm fine. Are you okay? You weren't in another fight or anything, right?"
                    mc "Heh, no. I'm good."
                    scene 10_243 with Dissolve(1)
                    va "What's up?"
                    mc "Nothing much. I just called to see if you were alright."
                    va "So you were actually worried?"
                    mc "Well, yeah... Famous last words, remember?"
                    va "Haha. Thanks."
                    scene 10_244 with Dissolve(1)
                    mc "What are you doing?"
                    va "Eh..."
                    mc "Oh yeah, watching TV... You told me before."
                    mc "{i}(Fuck, I'm so stupid.){/i}"
                    scene 10_245 with Dissolve(1)
                    va "Why are you nervous talking to me all of a sudden?"
                    mc "I don't know. Maybe it's because we're talking over the phone."
                    va "Hmm... I'm not nervous."
                    mc "Yeah, I'm weird like that."
                    scene 10_246 with Dissolve(1)
                    va "Cute but weird?"
                    mc "Haha. Can a guy be cute?"
                    va "Of course."
                    scene 10_247 with Dissolve(1)
                    mc "At least I'm not crazy!"
                    va "Hey!"
                    scene 10_248 with Dissolve(1)
                    va "I'd rather be crazy than weird."
                    mc "And that is why you are crazy!"
                    va "Haha."
                    scene 10_249 with Dissolve(1)
                    mc "..."
                    va "..."
                    scene 10_250 with Dissolve(1)
                    mc "Anyway. I'm glad you're okay. And sorry again for calling so late."
                    va "It's fine."
                    mc "I'll let you finish watching TV."
                    scene 10_251 with Dissolve(1)
                    mc "Good night, Val."
                    va "Good night."
                    va "..."
                "Go upstairs":
                    mc "{i}(She might be asleep already. I'll ask her next time.){/i}"
        else:
            pass
        scene 10_252 with Dissolve(1)
        mc "Sorry, Nikki."
        mc "Took a little longer than I expected."
        scene 10_253 with Dissolve(1)
        if Nikki_Week4_Wednesday_Visit_Knows == True:
            ni "Who's Alexis? Is she the girl you told me you were seeing before?"
            mc "Yes, but this was about something else."
        else:
            $ Nikki_Visit_Points -= 4
            ni "Who is Alexis?"
            mc "Uhm... She's a friend."
            ni "..."
        scene 10_254 with Dissolve(1)
        mc "Melissa, that's our neighbour, couldn't get hold of Erynn, her daughter, and..."
        ni "Emily told me you were out looking for her."
        mc "Yeah."
        ni "Is she alright?"
        mc "She's fine. She was held up at a photo shoot and couldn't use her phone."
        scene 10_255 with Dissolve(1)
        mc "Anyway, we couldn't reach her at first. So, I called Alexis, who's her best friend, to ask if she might know where she is."
        mc "She then came along to look for her."
        mc "She just called me to say that everything is alright now. There was some other drama going on between them."
        ni "Hmm..."
    else:
        ni "What do you think of the colours? I wasn't too sure since you mostly wear black and white shirts."
        mc "They're cool."
        ni "Yeah? Good."
        scene 10_253 with Dissolve(1)
        ni "So, what happened earlier? Emily told me you were looking for a girl who was missing?"
        mc "Erynn, yes. Her mom couldn't reach her the whole day and asked if I could help look for her."
        ni "Is she alright?"
        mc "She's fine. She was held up at a photo shoot and couldn't use her phone."
        ni "That's a relief."
    scene 10_256 with Dissolve(1)
    mc "But tell me about your day. You were with your dad the whole time?"
    ni "Yes, it was good."
    ni "We talked a lot. He showed me his apartment, we went to a restaurant..."
    ni "Well, it wasn't really a restaurant. More of a bar which also serves food. Dad said they have the best steaks in town."
    scene 10_257 with Dissolve(1)
    mc "Oh, Dylan's bar?"
    ni "Could have been, I can't remember the name."
    mc "Big guy, long beard?"
    ni "I think the cook had a long beard yes, but we were served by a girl."
    if Alexis_Dating == True:
        mc "{i}(Heh... She actually met Alexis.){/i}"
    else:
        pass
    scene 10_258 with Dissolve(1)
    mc "Did you get the steak?"
    ni "I did. With fries."
    mc "And?"
    ni "It was good, great actually. But I liked the food your mom made yesterday better."
    mc "Hehe, she would love to hear that."
    scene 10_259 with Dissolve(1)
    mc "But I agree. She's an amazing cook."
    ni "I'm jealous you get to eat her cooking every day."
    mc "Oh, trust me. We don't eat that fancy every day."
    scene 10_260 with Dissolve(1)
    mc "Did you talk to your dad about... You know, uhm... Why he's here and stuff?"
    ni "Uh-huh."
    mc "You want to tell me or...?"
    ni "*Nods*"
    scene 10_261 with Dissolve(1)
    ni "I told you before that he was an athletics coach for a team, right?"
    ni "Three years ago, he was let go. He said he was so ashamed that he couldn't tell us."
    mc "People get fired all the time. It's nothing to be ashamed of."
    ni "For him, it was. He's very prideful in what he does. When he visited us, he always talked about the team. Who they'd beaten or lost against."
    scene 10_262 with Dissolve(1)
    mc "You never visited him?"
    ni "Since he was always on the road, he didn't have a place."
    ni "He stayed with us during breaks. My parents are divorced but they're still friends."
    ni "Maybe that was also a reason why he felt ashamed."
    scene 10_263 with Dissolve(1)
    mc "How did he end up here, being a coach at a sports school?"
    ni "Purely by luck."
    ni "He was let go when they were here in Madison Springs. He stayed a couple of days to get his head straight."
    ni "He was watching a game at the bar we ate at today when he met a sports agent. Na... Navarro or something?"
    scene 10_264 with Dissolve(1)
    mc "Heh, yes. Mr Navarro."
    ni "Oh, you know him?"
    mc "Wouldn't say know, per se, but I've met him. He was also at the competition last weekend to scout for talent."
    ni "Funny."
    scene 10_265 with Dissolve(1)
    ni "Well, they got to talking, and he told my dad that your school was looking for a new athletics coach."
    ni "Long story short. Navarro recommended him and a week later he got the job."
    ni "He's been there ever since."
    scene 10_266 with Dissolve(1)
    ni "Dad sounded so different once he told me. Like a huge weight had been lifted off his shoulders."
    ni "He's going to visit us next week, and he'll explain everything to Mom and Cara."
    mc "I'm happy it turned out okay."
    ni "Yeah, I was worried before."
    scene 10_267 with Dissolve(1)
    ni "The good thing though, is I can visit you more often, now."
    ni "I always have a place to stay and..."
    mc "You can stay here with us, as well. You know we have the space and Mom likes you too."
    scene 10_268 with Dissolve(1)
    ni "I hoped you'd say that. I don't really want to stay in Dad's small apartment."
    mc "Haha."
    if Nikki_Visit_Points >= 22:
        scene 10_269 with Dissolve(1)
        ""
    else:
        pass
    scene 10_270 with Dissolve(1)
    ni "*Yawn*"
    mc "Someone's tired."
    ni "Sorry, yeah. The whole day I felt exhausted for some reason. No running tomorrow. I think I'm gonna sleep in for once."
    mc "You should. That's a great idea."
    scene 10_271 with Dissolve(1)
    ni "Are you staying here, or are you gonna test out the new mattress?"
    menu:
        "Sleep here[KoGa3AutoWTChange1]{size=-4}(Nikki Week4 Friday SleepBed, Nikki Visit Points+2) {/size} {/color}":
            $ Nikki_Week4_Friday_SleepBed = True
            $ Nikki_Visit_Points += 2
            # Nikki Visit (30)
            mc "I'll stay here."
            scene 10_272 with Dissolve(1)
            mc "Besides, this is my favourite mattress, here."
            ni "If you just want this bed, we can also switch. I don't mind sleeping in the other room."
            scene 10_273 with Dissolve(1)
            mc "Obviously, I mean this one here."
            ni "Obviously."
            mc "It's so perfect. It's firm, but soft at the same time. And it bounces a little when you push on it."
            ni "Haha."
            scene 10_274 with Dissolve(1)
            mc "I'm gonna shower real quick."
            ni "Hurry!"
            mc "I will. Be right back."
            scene 10_275 with Dissolve(1)
            ""
        "Go to the other room":
            mc "I'll go to the other room and let you sleep."
            ni "Okay..."
            mc "Good night, Nikki."
            ni "Night."
    jump Week4_Saturday_Morning

label Week4_Friday_Evening_Cara:
    scene black with Dissolve(1)
    pause 2
    scene 10_277 with Dissolve(1)
    mc "{i}(Heh... She's so fixated on her movie, she didn't even notice me entering the room.){/i}"
    mc "{i}(What's she watching this time?){/i}"
    scene 10_278 with vpunch
    mc "Hey there."
    c "Aah... [mc]!"
    mc "Haha, sorry. I didn't want to scare you. What are you watching?"
    scene 10_279 with Dissolve(1)
    mc "Oh... Porn."
    c "It's not porn!"
    c "It's... It's just a sex scene in the movie."
    mc "Isn't that exactly what porn is?"
    c "NO!"
    menu:
        "Watch movie":
            scene 10_280 with Dissolve(1)
            mc "Can I watch with you?"
            c "Only if you want to see this movie. I want to see what happens."
            mc "Hey, there's porn in it, so..."
            c "It's not porn!"
            mc "Haha."
            scene 10_281 with Dissolve(1)
            mc "I'm gonna change real quick."
            mc "All those scenes make me hot."
            c "*Shakes head* ..."
            if Alexis_Dating == False:
                scene black with Dissolve(1)
                pause 2
                scene 10_314 with Dissolve(1)
                c "So, what happened earlier? Emily told me you were looking for a girl who was missing?"
                mc "Erynn, yes. Her mom couldn't reach her the whole day and asked if I could help look for her."
                c "Is she alright?"
                mc "She's fine. She was held up at a photo shoot and couldn't use her phone."
                c "That's a relief."
            else:
                n "*Bzzzt. Bzzzt*"
            jump Week4_Friday_Evening_Cara2
        "Play with her[KoGa3AutoWTChange1]{size=-4}(Cara Week4 Friday Play, Cara Visit Points+4) {/size} {/color}":
            $ Cara_Week4_Friday_Play = True
            $ Cara_Visit_Points += 4
            # Cara Visit (26)
            jump Week4_Friday_Evening_Cara_Play

label Week4_Friday_Evening_Cara_Play:
    if _in_replay:
        $ SexCounter_Cara = 5
        $ MC_SexCounter = 5
    $ SexCounter_Cara += 1
    $ MC_SexCounter += 1
    scene 10_284 with Dissolve(1)
    mc "I'll let you finish watching the movie."
    c "We can talk if you want. I can continue tomorrow."
    mc "It's fine. Just watch it."
    c "Okay."
    scene 10_285 with Dissolve(1)
    c "..."
    scene 10_286 with Dissolve(1)
    ""
    scene 10_287 with Dissolve(1)
    c "What are you doing?"
    mc "Nothing, just playing around a bit back here. Go watch your movie."
    c "I'm trying, but you're distracting me."
    mc "See it as a feature from the movie. If she's getting touched, so are you."
    c "..."
    scene 10_288 with Dissolve(1)
    mc "{i}(The woman in the movie is naked, you will be naked!){/i}"
    scene 10_289 with Dissolve(1)
    mc "{i}(I love her peachy ass.){/i}"
    scene 10_290 with Dissolve(1)
    c "Mmm..."
    scene 10_291 with Dissolve(1)
    ""
    menu:
        "Lick her ass[KoGa3AutoWTChange1]{size=-4}(Cara Week4 Friday LickAss) {/size} {/color}":
            $ Cara_Week4_Friday_LickAss = True
            scene 10_292 with vpunch
            c "Aaah..."
            scene 10_295 with Dissolve(1)
            c "[mc]! That's my..."
            mc "Ass? I couldn't help it, it looks so good! Did you enjoy that?"
            c "Uh... It just took me by surprise."
            mc "{i}(That's not a no.){/i}"
            scene 10_293 with Dissolve(1)
            mc "{i}(Why does this turn me on so much?){/i}"
            scene 10_294 with Dissolve(1)
            c "*Moaning*"
            mc "{i}(I think she's enjoying this too.){/i}"
            scene 10_296 with Dissolve(1)
            ""
        "Continue":
            scene 10_296 with Dissolve(1)
            ""
    scene 10_297 with Dissolve(1)
    mc "{i}(I'm so hard, I can't wait any longer.){/i}"
    scene 10_298 with Dissolve(1)
    mc "Why do you keep turning around? Watch your movie!"
    c "I'm curious what you're going to do."
    mc "You'll feel it."
    c "..."
    scene 10_299 with Dissolve(1)
    mc "{i}(Nice and wet!){/i}"
    scene 10_300 with Dissolve(1)
    c "Ahhh..."
    scene 10_301 with Dissolve(1)
    c "*Moaning*"
    scene 10_302 with Dissolve(1)
    c "Nggh... [mc]!"
    scene 10_303 with Dissolve(1)
    mc "{i}(Fuck, I'm cumming already.){/i}"
    mc "{i}(Fucking her from behind is so hot! Just a bit longer.){/i}"
    mc "{i}(No...){/i}"
    scene 10_304 with vpunch
    mc "Aah..."
    scene 10_305 with Dissolve(1)
    mc "Damn, that was a good movie!"
    c "Haha. It ended too soon though. Is this what they call a quickie?"
    mc "Sorry. You're just way too cute."
    scene 10_306 with Dissolve(1)
    ""
    scene 10_307 with Dissolve(1)
    mc "Do you know that you're wearing the headphones the wrong way?"
    c "What?"
    mc "This side is supposed to be on your right ear."
    scene 10_308 with Dissolve(1)
    c "Oh..."
    mc "Haha."
    c "I didn't realise."
    $ renpy.end_replay()
    if Alexis_Dating == False:
        scene black with Dissolve(1)
        pause 2
        scene 10_314 with Dissolve(1)
        c "So, what happened earlier? Emily told me you were looking for a girl who was missing?"
        mc "Erynn, yes. Her mom couldn't reach her the whole day and asked if I could help look for her."
        c "Is she alright?"
        mc "She's fine. She was held up at a photo shoot and couldn't use her phone."
        c "That's a relief."
    else:
        scene 10_309 with Dissolve(1)
        mc "I'm gonna get some water. Do you want anything from the kitchen?"
        c "I'm good, thanks."
        scene 10_310 with Dissolve(1)
        mc "Alright. Be right back."
        play sound "Sounds/Phone_Vibrate.mp3"
        n "*Bzzzt. Bzzzt*"
    jump Week4_Friday_Evening_Cara2

label Week4_Friday_Evening_Cara2:
    if Alexis_Dating == True:
        if Cara_Week4_Friday_Play == False:
            scene 10_282 with Dissolve(1)
            c "Who's Alexis?"
            mc "What?"
            c "Alexis... She's calling you."
            mc "..."
            scene 10_283 with Dissolve(1)
            mc "Give me a second. This might be important."
            c "..."
        else:
            scene 10_311 with Dissolve(1)
            c "Who's Alexis?"
            mc "What?"
            c "Alexis... She's calling you."
            mc "..."
            scene 10_312 with Dissolve(1)
            mc "Give me a second. This might be important."
            c "..."
        scene 10_226 with Dissolve(1)
        mc "Hey."
        a "Hey. Sorry I'm calling so late."
        mc "How are you?"
        scene 10_227 with Dissolve(1)
        a "I'm good."
        mc "How about Erynn?"
        a "She talked to Melissa."
        mc "That's great. The more people who know, the more can help her."
        scene 10_228 with Dissolve(1)
        a "*Sigh*"
        mc "What?"
        a "I'm such a bad friend."
        mc "Lexi, you're not!"
        a "I am. This has been going on for months and I didn't even notice anything."
        scene 10_229 with Dissolve(1)
        mc "You couldn't have known. She hid it from everyone."
        a "Still, I..."
        mc "Lexi! This is not your fault! So stop thinking it's your fault!"
        a "..."
        mc "Did you get in trouble? Because you took the car?"
        scene 10_230 with Dissolve(1)
        a "No. I explained what happened to Dad, and he said it fwas fine. He's always had a soft spot for Erynn."
        mc "No extra chores?"
        a "Heh, no. Not this time, at least."
        mc "Nice. So I don't have to come over and help out."
        scene 10_231 with Dissolve(1)
        a "But you can come over for other things."
        mc "What other things are you talking about?"
        a "Hmm... Come over and find out!"
        mc "How about I come tomorrow, then?"
        scene 10_232 with Dissolve(1)
        a "I can't tomorrow. I'm gonna spend the day with Erynn."
        mc "Sunday?"
        a "Can't Sunday either, sorry."
        scene 10_233 with Dissolve(1)
        mc "*Sigh* What a great start to spring break."
        a "Haha, sorry. You want to see me that bad?"
        mc "Well yeah..."
        a "How about Monday then? I don't have to work, I'm free all day."
        scene 10_234 with Dissolve(1)
        mc "Monday it is. I'll pick you up in the afternoon, and we'll go somewhere for a change."
        a "Can't wait."
        mc "Okay, see you on Monday, then. Good night, Alexis!"
        scene 10_235 with Dissolve(1)
        a "LEXI!"
        mc "Haha. That's what I meant!"
        a "..."
        a "Good night... Albert!"
        mc "Albert? Haha."
        scene 10_236 with Dissolve(1)
        mc "Oh, I get it. Einstein. From back when we met on the aeroplane."
        mc "Good one."
        mc "..."
        mc "{i}(She hung up already...){/i}"
        play sound "Sounds/Phone_Message.mp3"
        n "*Bzzzt*"
        scene 10_237 with Dissolve(1)
        mc "{i}(Haha, yep. Definitely Einstein!){/i}"
        mc "{i}(She looks as crazy as him. Haha, this is too funny.){/i}"
        if Valeria_Week4_Friday_Help == True:
            mc "{i}(Why do girls keep sticking out their tongues, though?){/i}"
            mc "{i}(Reminds me of Valeria. She did the same today.){/i}"
            mc "{i}(Maybe I should call her and ask how she's doing, after what happened.){/i}"
            menu:
                "Call Valeria[KoGa3AutoWTChange1]{size=-4}(Valeria Points+2) {/size} {/color}":
                    $ Valeria_Points += 2
                    # Valeria (20)
                    scene 10_238 with Dissolve(1)
                    mc "..."
                    mc "{i}(Not picking up. She might be asleep already.){/i}"
                    mc "..."
                    mc "{i}(Or... Don't tell me that...){/i}"
                    va "Hi!"
                    scene 10_239 with Dissolve(1)
                    mc "Hey. Sorry, did I wake you?"
                    va "No, you didn't. I had my phone on silent because I'm watching TV."
                    mc "Ah, okay."
                    scene 10_240 with Dissolve(1)
                    mc "How are you?"
                    x "Who's calling you so late?"
                    va "A friend from school."
                    x "I'm going to bed. Don't make it too late, okay?"
                    va "I won't."
                    scene 10_241 with Dissolve(1)
                    x "Buenas Noches, cariño."
                    va "Buenas Noches."
                    scene 10_242 with Dissolve(1)
                    va "Sorry. You were saying?"
                    mc "I asked how you are."
                    va "I'm fine. Are you okay? You weren't in another fight or anything, right?"
                    mc "Heh, no. I'm good."
                    scene 10_243 with Dissolve(1)
                    va "What's up?"
                    mc "Nothing much. I just called to see if you were alright."
                    va "So you were actually worried?"
                    mc "Well, yeah... Famous last words, remember?"
                    va "Haha. Thanks."
                    scene 10_244 with Dissolve(1)
                    mc "What are you doing?"
                    va "Eh..."
                    mc "Oh yeah, watching TV... You told me before."
                    mc "{i}(Fuck, I'm so stupid.){/i}"
                    scene 10_245 with Dissolve(1)
                    va "Why are you nervous talking to me all of a sudden?"
                    mc "I don't know. Maybe it's because we're talking over the phone."
                    va "Hmm... I'm not nervous."
                    mc "Yeah, I'm weird like that."
                    scene 10_246 with Dissolve(1)
                    va "Cute but weird?"
                    mc "Haha. Can a guy be cute?"
                    va "Of course."
                    scene 10_247 with Dissolve(1)
                    mc "At least I'm not crazy!"
                    va "Hey!"
                    scene 10_248 with Dissolve(1)
                    va "I'd rather be crazy than weird."
                    mc "And that is why you're crazy!"
                    va "Haha."
                    scene 10_249 with Dissolve(1)
                    mc "..."
                    va "..."
                    scene 10_250 with Dissolve(1)
                    mc "Anyway. I'm glad you're okay. And sorry again for calling so late."
                    va "It's fine."
                    mc "I'll let you finish watching TV."
                    scene 10_251 with Dissolve(1)
                    mc "Good night, Val."
                    va "Good night."
                    va "..."
                "Go upstairs":
                    mc "{i}(She might be asleep already. I'll ask her next time.){/i}"
        scene black with Dissolve(1)
        pause 2
        scene 10_313 with Dissolve(1)
        mc "Sorry, Cara."
        mc "Took a little longer than I expected."
        scene 10_314 with Dissolve(1)
        if Cara_Week4_Wednesday_Visit_Knows == True:
            c "Who's Alexis? Is she the girl you told me you were seeing?"
            mc "Yes, but this was about something else."
        else:
            $ Cara_Visit_Points -= 4
            c "Who's Alexis?"
            mc "Uhm... She's a friend."
        scene 10_315 with Dissolve(1)
        mc "Melissa, that's our neighbour, couldn't get a hold of Erynn, her daughter, and..."
        c "Emily told me you were out looking for her."
        mc "Yeah."
        c "Is she alright?"
        mc "She's fine. She was held up at a photo shoot and couldn't use her phone."
        scene 10_316 with Dissolve(1)
        mc "Anyway, we couldn't reach her at first. So, I called Alexis, who is her best friend, to ask if she might know where she is."
        mc "She then came along to look for her."
        mc "She just called me to say that everything is alright now. There was some other drama going on between them."
        c "Hmm..."
    else:
        pass
    scene 10_317 with Dissolve(1)
    mc "But tell me about your day. You were with your dad the whole time?"
    c "Yes, it was alright."
    c "We talked a lot. He showed me his apartment, we went to a restaurant... Nothing special."
    c "Well, Dad called it a restaurant. It was more of a sports bar which also serves snacks. Supposedly, they have the best steaks in town."
    scene 10_318 with Dissolve(1)
    mc "Oh, Dylan's Bar and BBQ?"
    c "I think so, not sure."
    mc "Big guy, long beard?"
    c "The cook had a long beard, yes, but we were served by a girl."
    if Alexis_Dating == True:
        mc "{i}(Heh... She actually met Alexis.){/i}"
    else:
        pass
    scene 10_319 with Dissolve(1)
    mc "Did you get the steak?"
    c "No, I only took fries."
    mc "What? The best steak in town and you didn't even try it?"
    c "I wasn't that hungry. It wouldn't have been better than the food your mom made yesterday, anyway."
    mc "Hehe, she would love to hear that."
    scene 10_320 with Dissolve(1)
    mc "But I agree. She's an amazing cook."
    c "Does she cook every day for you?"
    mc "No, not every day. Sometimes she brings some food from the restaurant with her, or we order out."
    c "After being at the restaurant the whole day, I wouldn't want to cook at home, either."
    mc "Exactly."
    scene 10_321 with Dissolve(1)
    mc "Did you talk to your dad about... You know, uhm... Why he's here and stuff?"
    c "I did."
    mc "You want to tell me, or...?"
    c "*Sigh* There's not much to tell, really..."
    scene 10_322 with Dissolve(1)
    c "I told you before that he was an athletics coach for a team, right?"
    c "Three years ago, he was let go. He said he was so ashamed that he couldn't tell us."
    mc "People get fired all the time. It's nothing to be ashamed of."
    c "I don't know either. Maybe he just didn't want to tell us."
    scene 10_323 with Dissolve(1)
    mc "You never visited him?"
    c "No, I never wanted to. I don't think he had a place, since he was always on the road, anyway."
    c "He stayed with us during breaks. My parents are divorced, but they're still friends."
    c "Maybe that was the reason why he felt ashamed."
    scene 10_324 with Dissolve(1)
    mc "How did he end up here, being a coach in a sports school?"
    c "Purely by luck."
    c "He was let go when they were here in Madison Springs. He stayed a couple of days to get his head straight."
    c "He was watching a game at the bar we ate at today when he met a sports agent. Na... Navarro or something?"
    scene 10_325 with Dissolve(1)
    mc "Yes, Mr Navarro."
    c "Oh, you know him?"
    mc "Wouldn't say know, per se, but I've met him. He was also at the competition last weekend to scout for talent."
    c "Heh..."
    scene 10_326 with Dissolve(1)
    c "Well, they got to talking, and he told my dad that your school was looking for a new athletics coach."
    c "Long story short. Navarro recommended him, and a week later he got the job."
    c "He's been there ever since."
    scene 10_327 with Dissolve(1)
    c "Felt like a huge weight had been lifted off his shoulders after he told me."
    c "He's going to visit us next week, and he'll explain everything to Mom and Nikki."
    mc "I'm happy it turned out okay."
    c "Yeah..."
    scene 10_328 with Dissolve(1)
    c "The good thing about Dad living here is that I can convince Mom to let me visit you more often, now."
    c "I always have a place to stay, and..."
    mc "You can stay here with us, as well. You know we have the space, and Mom likes you too."
    scene 10_329 with Dissolve(1)
    c "Good! I really didn't want to stay in Dad's small apartment. I like your place so much better!"
    mc "Haha."
    if Cara_Visit_Points >= 18:
        scene 10_330 with Dissolve(1)
        ""
    else:
        pass
    scene 10_331 with Dissolve(1)
    c "*Yawn*"
    mc "Someone is tired."
    c "No!"
    mc "Your yawning says different."
    scene 10_332 with Dissolve(1)
    c "Are you staying here or are you gonna sleep in the other room?"
    menu:
        "Sleep here[KoGa3AutoWTChange1]{size=-4}(Cara Week4 Friday SleepBed, Cara Visit Points+2) {/size} {/color}":
            $ Cara_Week4_Friday_SleepBed = True
            $ Cara_Visit_Points += 2
            # Cara Visit (28)
            mc "I'll stay here."
            scene 10_333 with Dissolve(1)
            mc "I don't have a cuddle partner in the other room!"
            c "Haha."
            scene 10_334 with Dissolve(1)
            mc "But first, I'll go shower."
            mc "You can finish your movie in the meantime."
            c "Finally!"
            mc "Haha."
            scene 10_335 with Dissolve(1)
            ""
        "Go to the other room":
            mc "I'll go to the other room and let you sleep."
            c "Okay..."
            mc "Good night, Cara."
            c "Night."
    jump Week4_Saturday_Morning

label Week4_Friday_Evening4:
    if Alexis_Dating == True:
        scene black with Dissolve(1)
        pause 2
        scene 10_276 with Dissolve(1)
        mc "{i}(What was I thinking going to bed at ten?){/i}"
        mc "{i}(Of course I can't fall asleep...){/i}"
        play sound "Sounds/Phone_Vibrate.mp3"
        n "*Bzzzt. Bzzzt*"
        mc "{i}(Is that my phone?){/i}"
        scene 10_226 with Dissolve(1)
        mc "Hey."
        a "Hey. Sorry I'm calling so late."
        mc "How are you?"
        scene 10_227 with Dissolve(1)
        a "I'm good."
        mc "How about Erynn?"
        a "She talked to Melissa."
        mc "That's great. The more people who know, the more can help her."
        scene 10_228 with Dissolve(1)
        a "*Sigh*"
        mc "What?"
        a "I'm such a bad friend."
        mc "Lexi, you're not!"
        a "I am. This has been going on for months and I didn't even notice anything."
        scene 10_229 with Dissolve(1)
        mc "You couldn't have known. She hid it from everyone."
        a "Still, I..."
        mc "Lexi! This is not your fault! So stop thinking it's your fault!"
        a "..."
        mc "Did you get in trouble? Because you took the car?"
        scene 10_230 with Dissolve(1)
        a "No. I explained what happened to Dad, and he said it was fine. He's always had a soft spot for Erynn."
        mc "No extra chores?"
        a "Heh, no. Not this time, at least."
        mc "Nice. So I don't have to come over and help out."
        scene 10_231 with Dissolve(1)
        a "But you can come over for other things."
        mc "What other things are you talking about?"
        a "Hmm... Come over and find out!"
        mc "How about I come tomorrow, then?"
        scene 10_232 with Dissolve(1)
        a "I can't tomorrow. I'm gonna spend the day with Erynn."
        mc "Sunday?"
        a "Can't Sunday either, sorry."
        scene 10_233 with Dissolve(1)
        mc "*Sigh* What a great start to spring break."
        a "Haha, sorry. You want to see me that bad?"
        mc "Well yeah..."
        a "How about Monday then? I don't have to work, I'm free all day."
        scene 10_234 with Dissolve(1)
        mc "Monday it is. I'll pick you up in the afternoon, and we'll go somewhere for a change."
        a "Can't wait."
        mc "Okay, see you on Monday, then. Good night, Alexis!"
        scene 10_235 with Dissolve(1)
        a "LEXI!"
        mc "Haha. That's what I meant!"
        a "..."
        a "Good night... Albert!"
        mc "Albert? Haha."
        scene 10_236 with Dissolve(1)
        mc "Oh, I get it. Einstein. From back when we met on the aeroplane."
        mc "Good one."
        mc "..."
        mc "{i}(She hung up already...){/i}"
        play sound "Sounds/Phone_Message.mp3"
        n "*Bzzzt*"
        scene 10_237 with Dissolve(1)
        mc "{i}(Haha, yep. Definitely Einstein!){/i}"
        mc "{i}(She looks as crazy as him. Haha, this is too funny.){/i}"
        if Valeria_Week4_Friday_Help == True:
            mc "{i}(Why do girls keep sticking out their tongues, though?){/i}"
            mc "{i}(Reminds me of Valeria. She did the same today.){/i}"
            mc "{i}(Maybe I should call her and ask how she's doing, after what happened.){/i}"
            menu:
                "Call Valeria[KoGa3AutoWTChange1]{size=-4}(Valeria Points+2) {/size} {/color}":
                    $ Valeria_Points += 2
                    # Valeria Points (20)
                    scene 10_238 with Dissolve(1)
                    mc "..."
                    mc "{i}(Not picking up. She might be asleep already.){/i}"
                    mc "..."
                    mc "{i}(Or... Don't tell me that...){/i}"
                    va "Hi!"
                    scene 10_239 with Dissolve(1)
                    mc "Hey. Sorry, did I wake you?"
                    va "No, you didn't. I had my phone on silent because I'm watching TV."
                    mc "Ah, okay."
                    scene 10_240 with Dissolve(1)
                    mc "How are you?"
                    x "Who's calling you so late?"
                    va "A friend from school."
                    x "I'm going to bed. Don't make it too late, okay?"
                    va "I won't."
                    scene 10_241 with Dissolve(1)
                    x "Buenas Noches, cariño."
                    va "Buenas Noches."
                    scene 10_242 with Dissolve(1)
                    va "Sorry. You were saying?"
                    mc "I asked how you are."
                    va "I'm fine. Are you okay? You weren't in another fight or anything, right?"
                    mc "Heh, no. I'm good."
                    scene 10_243 with Dissolve(1)
                    va "What's up?"
                    mc "Nothing much. I just called to see if you were alright."
                    va "So you were actually worried?"
                    mc "Well, yeah... Famous last words, remember?"
                    va "Haha. Thanks."
                    scene 10_244 with Dissolve(1)
                    mc "What are you doing?"
                    va "Eh..."
                    mc "Oh yeah, watching TV... You told me before."
                    mc "{i}(Fuck, I'm so stupid.){/i}"
                    scene 10_245 with Dissolve(1)
                    va "Why are you nervous talking to me all of a sudden?"
                    mc "I don't know. Maybe it's because we're talking over the phone."
                    va "Hmm... I'm not nervous."
                    mc "Yeah, I'm weird like that."
                    scene 10_246 with Dissolve(1)
                    va "Cute but weird?"
                    mc "Haha. Can a guy be cute?"
                    va "Of course."
                    scene 10_247 with Dissolve(1)
                    mc "At least I'm not crazy!"
                    va "Hey!"
                    scene 10_248 with Dissolve(1)
                    va "I'd rather be crazy than weird."
                    mc "And that is why you're crazy!"
                    va "Haha."
                    scene 10_249 with Dissolve(1)
                    mc "..."
                    va "..."
                    scene 10_250 with Dissolve(1)
                    mc "Anyway. I'm glad you're okay. And sorry again for calling so late."
                    va "It's fine."
                    mc "I'll let you finish watching TV."
                    scene 10_251 with Dissolve(1)
                    mc "Good night, Val."
                    va "Good night."
                    va "..."
                "Go upstairs":
                    mc "{i}(She might be asleep already. I'll ask her next time.){/i}"
        else:
            pass
    else:
        pass
    jump Week4_Saturday_Morning

label Week4_Saturday_Morning:
    scene black with Dissolve(2)
    pause 2
    n "Saturday morning, 08:42."
    scene 10_336 with Dissolve(1)
    er "Good morning, Emily."
    m "Hey, good morning, Erynn."
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 10_337 at moveup
    pause 3
    m "Look at you. So pretty again."
    er "Thank you."
    m "Come give me a hug."
    scene 10_338 with Dissolve(1)
    er "I came to apologise for..."
    m "You don't have to apologise, sweetheart."
    m "You know how we mothers are. Always worrying for nothing."
    er "..."
    scene 10_339 with Dissolve(1)
    er "Do you maybe have some time tomorrow? Mom and I need to talk to you about something."
    m "How about I come by in the morning?"
    er "Thank you."
    scene 10_340 with Dissolve(1)
    m "Have you had breakfast yet? Or do you want some coffee?"
    er "Thank you, but I'm going for brunch with a friend a little later."
    m "Mimosas?"
    er "Heh, yeah."
    if Erynn_End == True:
        scene 10_341 with Dissolve(1)
        m "[mc] is still sleeping, I think, if you wanted to talk to him."
        er "No, I just visited to quickly talk to you."
        scene 10_342 with Dissolve(1)
        m "Thank you for coming by, Erynn. We'll see each other tomorrow, then."
        er "Yes. Bye, Emily."
        m "Bye, sweetheart."
        if Nikki_Girlfriend == True:
            jump Week4_Saturday_Morning_Nikki
        else:
            if Cara_Girlfriend == True:
                jump Week4_Saturday_Morning_Cara
            else:
                jump Week4_Saturday_Morning2
    else:
        if Erynn_Week3_Monday_Blackmailhelp == False:
            scene 10_341 with Dissolve(1)
            m "[mc] is still sleeping, I think, if you wanted to talk to him."
            er "No, I just visited to quickly talk to you."
            scene 10_342 with Dissolve(1)
            m "Thank you for coming by, Erynn. We'll see each other tomorrow then."
            er "Yes. Bye, Emily."
            m "Bye, sweetheart."
            if Nikki_Girlfriend == True:
                jump Week4_Saturday_Morning_Nikki
            else:
                if Cara_Girlfriend == True:
                    jump Week4_Saturday_Morning_Cara
                else:
                    jump Week4_Saturday_Morning2
        else:
            scene 10_343 with Dissolve(1)
            m "[mc] is still sleeping, I think, if you wanted to talk to him."
            er "I guess it's time to wake him, then."
            er "I know it's spring break, but he shouldn't spend all day sleeping."
            m "I totally agree with you."
            if Nikki_Girlfriend == True:
                $ Erynn_Week4_Saturday_Jump_Nikki = True
                scene 10_344 with Dissolve(1)
                m "Oh, he's sleeping in the other room."
                er "Hmm? Okay."
                jump Week4_Saturday_Morning_ErynnNikki
            else:
                if Cara_Girlfriend == True:
                    $ Erynn_Week4_Saturday_Jump_Cara = True
                    scene 10_344 with Dissolve(1)
                    m "Oh, he's sleeping in the other room."
                    er "Hmm? Okay."
                    jump Week4_Saturday_Morning_ErynnCara
                else:
                    $ Erynn_Week4_Saturday_Jump = True
                    jump Week4_Saturday_Morning_Erynn

label Week4_Saturday_Morning_ErynnNikki:
    scene black with Dissolve(1)
    pause 2
    scene 10_345 with Dissolve(1)
    er "{i}(The other room? He's right here.){/i}"
    scene 10_346 with vpunch
    er "Good morning, sleepyhead!"
    er "Time to wake up!"
    scene 10_347 with Dissolve(1)
    ni "..."
    scene 10_348 with Dissolve(1)
    er "Uh..."
    er "Who..."
    scene 10_349 with vpunch
    er "Aah!"
    ni "Who are you?"
    scene 10_350 with Dissolve(1)
    ni "And what are you doing here?"
    er "Let me go, Nikki!"
    scene 10_351 with Dissolve(1)
    ni "How do you know my name?"
    mc "{i}(Oh, that was Erynn screaming...){/i}"
    mc "{i}(What are they doing?){/i}"
    mc "{i}(Two hot girls on top of each other. I want to keep watching, but...){/i}"
    scene 10_352 with Dissolve(1)
    mc "I'm enjoying the show, but what's going on?"
    ni "[mc]."
    er "[mc]! Help me! She..."
    scene 10_353 with Dissolve(1)
    mc "You can let her go, Nikki."
    mc "This is Erynn, my neighbour."
    ni "Oh... The girl you were looking for yesterday?"
    mc "Yes."
    scene 10_354 with Dissolve(1)
    ni "Why didn't you say so?"
    er "I would have, if you didn't tackle me and not let me explain."
    ni "I didn't tackle you! You jumped on me. Besides, I'm not covering your mouth..."
    er "I thought you were [mc]!"
    scene 10_355 with Dissolve(1)
    mc "And I thought it was spring break instead of school hallways."
    ni "..."
    er "..."
    mc "Haha. Kidding?"
    scene 10_356 with Dissolve(1)
    mc "Why did you come over?"
    er "I wanted to thank you again for yesterday, and I have to tell you something."
    mc "Alright. Want to go downstairs?"
    er "Yes."
    scene 10_357 with Dissolve(1)
    mc "Give me a minute. I'll be right down."
    er "I'll be in the living room."
    mc "Kay."
    scene 10_358 with Dissolve(1)
    mc "Did she wake you?"
    ni "She did."
    mc "It's just something she does. Been that way since we were little."
    scene 10_359 with Dissolve(1)
    mc "I can't believe you were still sleeping. It's almost nine o'clock, already."
    mc "You must have been really exhausted, like you said yesterday. Are you feeling better?"
    ni "I am, thanks. Sleeping in was a good idea."
    mc "Hehe, I know right? You should do it more often."
    menu:
        "Talk to Erynn":
            scene 10_360 with Dissolve(1)
            mc "Anyway, I'll go and see what Erynn wants."
            ni "I'll take a shower in the meantime."
            mc "If you're looking for me after, I'll probably be at the neighbours'. I have to do some lawnmowing and stuff."
            ni "Ah, okay."
            mc "See you in a bit."
            ni "Have fun."
        "Tackle Nikki[KoGa3AutoWTChange1]{size=-4}(Nikki Visit Points+2, Erynn Friends) {/size} {/color}":
            $ Nikki_Visit_Points += 2
            # Nikki Visit (32)
            scene 10_361 with Dissolve(1)
            mc "*Sigh*"
            ni "What?"
            mc "I wanted to be the one to wake you and get tackled."
            ni "I did not tackle her!"
            scene 10_362 with Dissolve(1)
            ni "Don't look at me like that."
            ni "I did not tackle her!"
            ni "I just..."
            scene 10_363 with vpunch
            ni "Aaah-ha-ha..."
            ni "Okay, I see your point. Maybe I tackled her a bit... Just a tiny bit!"
            scene 10_364 with Dissolve(1)
            mc "What were your plans after holding her like this?"
            ni "Nothing!"
            mc "Nothing?"
            ni "Maybe interrogate her? I don't know..."
            scene 10_365 with Dissolve(1)
            mc "Haha. Interrogate..."
            mc "Interrogate how?"
            scene 10_366 with Dissolve(1)
            mc "Maybe something like this?"
            ni "Haha. No!"
            scene 10_367 with Dissolve(1)
            mc "How about this?"
            ni "Definitely no!"
            scene 10_368 with Dissolve(1)
            ni "Hey, go speak to Erynn first before you continue interrogating me. She's waiting for you."
            mc "She can wait a bit longer."
            ni "And what if she comes back and sees us? Please, go talk to her first."
            mc "Fine..."
            scene 10_369 with Dissolve(1)
            ni "And put some pants on! She doesn't have to see your... interrogation stick."
            mc "Haha."
            ni "I'll go shower in the meantime."
            scene 10_370 with Dissolve(1)
            mc "By the way. I have to do some lawnmowing and stuff at my neighbours' after I've talked with Erynn."
            mc "So if you need me, I'll be there."
            ni "Alright."
            scene 10_371 with Dissolve(1)
            mc "See you later."
            ni "Bye, have fun."
    scene black with Dissolve(1)
    pause 2
    scene 10_372 with Dissolve(1)
    mc "Hey, sorry about that."
    mc "..."
    mc "Why are you looking like that?"
    scene 10_373 with Dissolve(1)
    er "Why is she here?"
    mc "She's visiting."
    er "Why didn't you tell me yesterday?"
    mc "Uh... Because we had other things on our minds..."
    if Alexis_Dating == False:
        er "Didn't you break up?"
        if Nikki_Visit_Points >= 19:
            $ Erynn_LikeMC = False
            $ Erynn_Friends = True
            mc "We did, but we're back together."
            er "Oh... Okay."
        else:
            menu:
                "We broke up[KoGa3AutoWTChange1]{size=-4}(Erynn Week4 Saturday NikkiLie) {/size} {/color}":
                    $ Erynn_Week4_Saturday_NikkiLie = True
                    mc "We did. We're still friends though."
                    er "Hmm..."
                "Back together[KoGa3AutoWTChange1]{size=-4}(Erynn LikeMCFalse, Erynn Friends) {/size} {/color}":
                    $ Erynn_LikeMC = False
                    $ Erynn_Friends = True
                    mc "We did, but we're back together."
                    er "Oh... Okay."
    else:
        scene 10_374 with Dissolve(1)
        er "Does Alexis know she's here?"
        if Alexis_RiversideStory == True:
            mc "Yes, I told her."
            er "And she's okay with that?"
            mc "I think so, yeah."
            er "..."
        else:
            mc "No, I didn't tell her."
            er "[mc]! I think she should know you have another girl sleeping in your bed."
            mc "..."
            er "I'm not going to tell her, but I hate that I have to keep something from her just after we've become friends again."
            mc "I'm sorry. *Sigh* I'll talk to her, okay?"
    scene 10_375 with Dissolve(1)
    er "She's so aggressive."
    mc "Who, Nikki? No, she's not. You woke her up by jumping on her. No wonder she reacted the way she did. She's really sweet, actually."
    er "I don't like her."
    mc "Erynn... You don't know her. You're just angry she's able to hold you down."
    er "..."
    scene 10_376 with Dissolve(1)
    er "And she's very pretty too..."
    mc "Haha. You have a very special gift in complimenting someone in a truculent way."
    mc "But she is very pretty."
    scene 10_377 with Dissolve(1)
    er "..."
    mc "What? Fishing for a compliment as well?"
    menu:
        "Compliment her[KoGa3AutoWTChange1]{size=-4}(Erynn Points+2) {/size} {/color}":
            $ Erynn_Points += 2
            # Erynn (44)
            mc "Yes, you are very beautiful!"
            scene 10_378 with Dissolve(1)
            er "Hehe."
            mc "I like your outfit too."
            er "Thank you!"
        "Don't":
            scene 10_379 with Dissolve(1)
            mc "Well, tough luck. Not gonna happen."
            mc "I'm immune to your puppy dog eyes."
            er "So mean."
            mc "Haha."
    scene 10_380 with Dissolve(1)
    mc "Anyway, why are you here this morning?"
    er "I came to thank you again for yesterday."
    mc "You're welcome."
    er "And... I've also talked to Mom about... that."
    scene 10_381 with Dissolve(1)
    mc "You did? That's great, Erynn! A big step."
    mc "That mustn't have been easy. I'm proud of you."
    er "Thank you."
    mc "What did she say?"
    scene 10_382 with Dissolve(1)
    er "Not much at first. Seemed like she was in a state of shock."
    er "Then a sudden rush of emotions. She hugged me and started crying. I've never seen Mom cry before. It broke my heart."
    er "She got... well, not angry but... I don't know. She felt terrible that I kept it to myself for so long and couldn't confide in her."
    scene 10_383 with Dissolve(1)
    mc "How do you feel now?"
    er "Much better. I should've talked to her earlier, but..."
    mc "You needed someone to push you."
    scene 10_384 with Dissolve(1)
    er "Yeah. So thank you, [mc]!"
    scene 10_385 with Dissolve(1)
    mc "Did she have any idea what we can do?"
    er "I didn't tell her about your suggestion, because I know she won't agree to that."
    er "But she asked me to talk to Emily first. She's coming by tomorrow."
    mc "That's good. She might be able to help, too."
    scene 10_386 with Dissolve(1)
    er "But enough of this. Today is a good day."
    mc "Yeah? What are the plans?"
    er "Spending the day with Lexi. Brunch, shopping, beach."
    if Alexis_Sex == False:
        mc "That sounds like fun."
    else:
        if Alexis_Dating == False:
            if Erynn_Week2_Tuesday_AlexisFight == False:
                mc "That sounds like fun."
                mc "{i}(I guess Alexis never told Erynn about our hookup. Maybe for the better.){/i}"
            else:
                if Alexis_Week2_Wednesday_Breakup == True:
                    mc "Oh, you're friends again?"
                    er "We talked it out a few days ago."
                    mc "About time!"
                    mc "{i}(I guess Alexis didn't say anything to Erynn about the breakup.){/i}"
                else:
                    if Alexis_Week3_Wednesday_TC_Breakup == True:
                        mc "Oh, you're friends again?"
                        er "We talked it out a few days ago."
                        mc "About time!"
                        mc "{i}(I guess Alexis didn't say anything to Erynn about the breakup.){/i}"
                    else:
                        if Layla_Week3_Wednesday_TC_Alexis_DateBoth == True:
                            mc "Oh, you're friends again?"
                            er "We talked it out a few days ago."
                            mc "About time!"
                            mc "{i}(I guess Alexis didn't say anything to Erynn about the breakup.){/i}"
                            mc "{i}(If she knew, we wouldn't be talking like this right now. I hope it stays that way.){/i}"
                        else:
                            mc "Oh, you're friends again?"
                            er "We talked it out a few days ago."
                            mc "About time!"
        else:
            mc "Right. She told me yesterday she's spending the day with you."
    scene 10_387 with Dissolve(1)
    er "You're going to hang out with Nikki?"
    mc "I am. It's her last day here."
    mc "But first I need to do some lawnmowing for Melissa."
    scene 10_388 with Dissolve(1)
    er "Let's go then. I need to get ready, too."
    mc "You're not ready? You look ready."
    er "Just a few touch-ups!"
    mc "Heh..."
    scene 10_389 with Dissolve(1)
    er "The pool needs some cleaning too. Lots of leaves in there."
    mc "Melissa has a big net in the garage. I'll get it for you."
    er "Heh... You think you're so clever, huh?"
    mc "I am. There's a reason why I take the advanced math class."
    scene 10_390 with Dissolve(1)
    er "A very good reason. Who was the one spending lots of her time teaching you math after school?"
    mc "Haha."
    er "Don't laugh, answer the question!"
    jump Week4_Saturday_Melissa

label Week4_Saturday_Morning_ErynnCara:
    scene black with Dissolve(1)
    pause 2
    scene 10_345 with Dissolve(1)
    er "{i}(The other room? He's right here.){/i}"
    scene 10_346 with vpunch
    er "Good morning, sleepyhead!"
    er "Time to wake up!"
    scene 10_391 with Dissolve(1)
    c "..."
    scene 10_348 with Dissolve(1)
    er "Uh..."
    er "Who..."
    scene 10_392 with Dissolve(1)
    c "Aaah!"
    c "Who... Wha-What are you doing here?"
    scene 10_393 with Dissolve(1)
    er "Sorry, I didn't want to scare you. I thought you were [mc]."
    er "I'm Erynn and you must be... Cara?"
    c "..."
    scene 10_394 with Dissolve(1)
    c "How..."
    er "[mc] showed me some pictures of you before."
    er "You look even cuter in person."
    c "Uh... Thank you."
    scene 10_395 with Dissolve(1)
    mc "{i}(Erynn?){/i}"
    mc "{i}(What's she doing here?){/i}"
    scene 10_396 with Dissolve(1)
    mc "Hey, good morning."
    c "[mc]!"
    er "There you are!"
    scene 10_397 with Dissolve(1)
    mc "Hey, Erynn. Why did you come over?"
    er "I wanted to thank you again for yesterday, and I have to tell you something."
    mc "Alright. Want to go downstairs?"
    er "Yes."
    scene 10_398 with Dissolve(1)
    er "Nice to meet you, Cara."
    er "And sorry again."
    c "Uhm... No problem."
    scene 10_399 with Dissolve(1)
    mc "Give me a minute. I'll be right down."
    er "I'll be in the living room."
    mc "Kay."
    scene 10_400 with Dissolve(1)
    mc "Hey, are you alright? Did she wake you?"
    c "She did."
    mc "It's just something she does. Been that way since we were little."
    scene 10_401 with Dissolve(1)
    c "Who is she?"
    mc "She's Erynn, my neighbour's daughter."
    c "Oh, the one you were looking for yesterday."
    mc "Exactly."
    scene 10_402 with Dissolve(1)
    c "When she jumped on me, I first thought it was you."
    c "Then I opened my eyes and this pretty girl was sitting on top of me..."
    menu:
        "Talk to Erynn":
            c "I was shocked for a moment, like what's going on? Who is this?"
            mc "Haha. I can believe that."
            scene 10_403 with Dissolve(1)
            mc "Anyway, I'll go and see what she wants."
            c "*Yawn* I'm gonna sleep a bit more."
            mc "Heh, you do that. If you wake up later and can't find me, I'll probably be at the neighbours'. I have to do some lawnmowing and stuff."
            c "Ah, okay."
            mc "See you in a bit."
            c "Have fun."
        "Jump on Cara[KoGa3AutoWTChange1]{size=-4}(Cara Visit Points+2) {/size} {/color}":
            $ Cara_Visit_Points += 2
            # Cara Visit (30)
            scene 10_404 with vpunch
            c "Aaah..."
            mc "Still confuse me with a girl?"
            c "Nooo-ha-ha... You are so much heavier!"
            mc "What did you say?"
            scene 10_405 with Dissolve(1)
            n "*Kiss-kiss-kiss*"
            c "Haha."
            scene 10_406 with Dissolve(1)
            c "Don't you have to go talk to Erynn?"
            mc "She can wait a little bit."
            mc "Punishment for waking my sleeping beauty."
            scene 10_407 with Dissolve(1)
            c "..."
            c "That was so cheesy!"
            mc "Cheesy or not. It's still true."
            scene 10_408 with Dissolve(1)
            ""
            scene 10_409 with Dissolve(1)
            c "There! Now go talk to her."
            mc "You really want to get rid of me, huh?"
            c "Yes, so I can sleep some more."
            mc "Haha, fine. I'll let you sleep, Princess Morgan!"
            c "Hey!"
            scene 10_410 with Dissolve(1)
            mc "By the way. I have to do some lawnmowing and stuff at my neighbours' after I've talked with Erynn."
            mc "So, if you need me, I'll be there."
            c "Alright. Bye."
            mc "..."
            scene 10_411 with vpunch
            n "*Slap*"
            c "Aaah-ha-ha..."
    scene black with Dissolve(1)
    pause 2
    scene 10_412 with Dissolve(1)
    mc "Hey. You look happy today."
    er "I am. It's a good day."
    scene 10_373 with Dissolve(1)
    er "Why is Cara here?"
    mc "She's visiting."
    er "Why didn't you tell me yesterday?"
    mc "Uh... Because we had other things on our minds..."
    if Alexis_Dating == False:
        er "Didn't you break up?"
        if Cara_Visit_Points >= 19:
            mc "We did, but we're back together."
            er "Oh... Okay."
        else:
            menu:
                "We broke up[KoGa3AutoWTChange1]{size=-4}(Erynn Week4 Saturday CaraLie) {/size} {/color}":
                    $ Erynn_Week4_Saturday_CaraLie = True
                    mc "We did. We're still friends though."
                    er "Hmm..."
                "Back together":
                    mc "We did, but we're back together."
                    er "Oh... Okay."
    else:
        scene 10_374 with Dissolve(1)
        er "Does Alexis know she's here?"
        if Alexis_RiversideStory == True:
            mc "Yes, I told her."
            er "And she's okay with that?"
            mc "I think so, yeah."
            er "..."
        else:
            mc "No, I didn't tell her."
            er "[mc]! I think she should know you have another girl sleeping in your bed."
            mc "..."
            er "I'm not going to tell her, but I hate that I have to keep something from her just after we've become friends again."
            mc "I'm sorry. *Sigh* I'll talk to her, okay?"
    scene 10_413 with Dissolve(1)
    er "She's so cute."
    mc "Cara?"
    er "I like her."
    mc "Heh, already? You don't even know her."
    er "It feels like we'd get along if we hung out. She's sixteen, right?"
    scene 10_414 with Dissolve(1)
    mc "No, she's eighteen."
    er "Oh... She looks so young. She's very pretty."
    mc "She is."
    scene 10_377 with Dissolve(1)
    er "..."
    mc "What? Fishing for a compliment as well?"
    menu:
        "Compliment her[KoGa3AutoWTChange1]{size=-4}(Erynn Points+2) {/size} {/color}":
            $ Erynn_Points += 2
            # Erynn (44)
            mc "Yes, you are very beautiful!"
            scene 10_378 with Dissolve(1)
            er "Hehe."
            mc "I like your outfit, too."
            er "Thank you!"
        "Don't":
            scene 10_379 with Dissolve(1)
            mc "Well, tough luck. Not gonna happen."
            mc "I'm immune to your puppy dog eyes."
            er "So mean."
            mc "Haha."
    scene 10_380 with Dissolve(1)
    mc "Anyway, why are you here this morning?"
    er "I came to thank you again for yesterday."
    mc "You're welcome."
    er "And... I've also talked to Mom about... that."
    scene 10_381 with Dissolve(1)
    mc "You did? That's great, Erynn! A big step."
    mc "That mustn't have been easy. I'm proud of you."
    er "Thank you."
    mc "What did she say?"
    scene 10_382 with Dissolve(1)
    er "Not much at first. Seemed like she was in a state of shock."
    er "Then a sudden rush of emotions. She hugged me and started crying. I've never seen Mom cry before. It broke my heart."
    er "She got... well, not angry but... I don't know. She felt terrible that I kept it to myself for so long and couldn't confide in her."
    scene 10_383 with Dissolve(1)
    mc "How do you feel now?"
    er "Much better. I should've talked to her earlier, but..."
    mc "You needed someone to push you."
    scene 10_384 with Dissolve(1)
    er "Yeah. So thank you, [mc]!"
    scene 10_385 with Dissolve(1)
    mc "Did she have any idea what we can do?"
    er "I didn't tell her about your suggestion, because I know she won't agree to that."
    er "But she asked me to talk to Emily first. She's coming by tomorrow."
    mc "That's good. She might be able to help, too."
    scene 10_386 with Dissolve(1)
    er "But enough of this. Today is a good day."
    mc "Yeah? What are the plans?"
    er "Spending the day with Lexi. Brunch, shopping, beach."
    if Alexis_Sex == False:
        mc "That sounds like fun."
    else:
        if Alexis_Dating == False:
            if Erynn_Week2_Tuesday_AlexisFight == False:
                mc "That sounds like fun."
                mc "{i}(I guess Alexis never told Erynn about our hookup. Maybe for the better.){/i}"
            else:
                if Alexis_Week2_Wednesday_Breakup == True:
                    mc "Oh, you're friends again?"
                    er "We talked it out a few days ago."
                    mc "About time!"
                    mc "{i}(I guess Alexis didn't say anything to Erynn about the breakup.){/i}"
                else:
                    if Alexis_Week3_Wednesday_TC_Breakup == True:
                        mc "Oh, you're friends again?"
                        er "We talked it out a few days ago."
                        mc "About time!"
                        mc "{i}(I guess Alexis didn't say anything to Erynn about the breakup.){/i}"
                    else:
                        if Layla_Week3_Wednesday_TC_Alexis_DateBoth == True:
                            mc "Oh, you're friends again?"
                            er "We talked it out a few days ago."
                            mc "About time!"
                            mc "{i}(I guess Alexis didn't say anything to Erynn about the breakup.){/i}"
                            mc "{i}(If she knew, we wouldn't be talking like this right now. I hope it stays that way.){/i}"
                        else:
                            mc "Oh, you're friends again?"
                            er "We talked it out a few days ago."
                            mc "About time!"
        else:
            mc "Right. She told me yesterday she's spending the day with you."
    scene 10_387 with Dissolve(1)
    er "You're going to hang out with Cara?"
    mc "I am. It's her last day here."
    mc "But first I need to do some lawnmowing for Melissa."
    scene 10_388 with Dissolve(1)
    er "Let's go, then. I need to get ready, too."
    mc "You're not ready? You look ready."
    er "Just a few touch-ups!"
    mc "Heh..."
    scene 10_389 with Dissolve(1)
    er "The pool needs some cleaning too. Lots of leaves in there."
    mc "Melissa has a big net in the garage. I'll get it for you."
    er "Heh... You think you're so clever, huh?"
    mc "I am. There's a reason why I take the advanced math class."
    scene 10_390 with Dissolve(1)
    er "A very good reason. Who was the one spending lots of her time teaching you math after school?"
    mc "Haha."
    er "Don't laugh, answer the question!"
    jump Week4_Saturday_Melissa

label Week4_Saturday_Morning_Nikki:
    scene black with Dissolve(2)
    pause 2
    n "Saturday morning, 8:51."
    scene 10_415 with Dissolve(1)
    mc "Morning, Mom."
    m "Good morning, honey."
    scene 10_416 with Dissolve(1)
    mc "Oh... You're making pancakes. Nice! Can I have some?"
    m "Of course."
    mc "Do we have maple syrup?"
    m "In the fridge."
    scene 10_417 with Dissolve(1)
    m "Nikki still sleeping?"
    mc "I think so, yes."
    m "She okay?"
    mc "Yeah, she was tired yesterday and said she'll sleep in for once."
    scene 10_418 with Dissolve(1)
    m "How is the new mattress? Comfortable?"
    if Nikki_Week4_Friday_SleepBed == False:
        mc "Yeah, I slept really well."
        mc "I'll set up the bed later today."
        scene black with Dissolve(1)
        pause 2
        scene 10_419 with Dissolve(1)
        mc "..."
        mc "{i}(Is she still sleeping?){/i}"
        scene 10_431 with Dissolve(1)
        mc "{i}(She is.){/i}"
        mc "{i}(She must have been really tired yesterday.){/i}"
        scene 10_432 with Dissolve(1)
        mc "Nikki?"
        ni "Hmm?"
        mc "Sorry to wake you."
        scene 10_433 with Dissolve(1)
        mc "I just wanted to tell you that I'm at the neighbours' to do some yard stuff."
        mc "If you need me, just come on over."
        ni "Alright."
        mc "Kay, sleep some more. See you later."
        jump Week4_Saturday_Melissa
    else:
        mc "Uh... Yeah... It's good."
        mc "I'll set up the bed later today."
        scene black with Dissolve(1)
        pause 2
        scene 10_419 with Dissolve(1)
        mc "..."
        mc "{i}(Is she still sleeping?){/i}"
        scene 10_420 with vpunch
        mc "Good morning, sunshine!"
        scene 10_347 with Dissolve(1)
        ni "..."
        mc "{i}(Oh... She looks mad.){/i}"
        mc "You were actually still sleeping?"
        scene 10_421 with vpunch
        ni "YOU!"
        mc "Haha... I'm sorry, Nikki."
        mc "I really thought you were awake."
        scene 10_422 with Dissolve(1)
        if Nikki_Week4_Thursday_ArmwrestlingWin == False:
            mc "You wanna fight again?"
            ni "You're not going to win this time!"
        else:
            mc "You wanna fight again?"
            ni "You wanna lose again?"
        scene 10_423 with Dissolve(1)
        mc "I don't mind losing if I end up in this situation."
        mc "I'll be the biggest loser ever!"
        ni "Something we agree on!"
        mc "Haha."
        scene 10_424 with Dissolve(1)
        mc "I know you're evil, but you can also be mean."
        ni "I can be a lot of things."
        mc "Mmm... Is it weird that turns me on?"
        scene 10_425 with vpunch
        ni "Aah-haha..."
        mc "I kinda hate losing though, to be honest."
        scene 10_364 with Dissolve(1)
        ni "You're winning every day."
        ni "You've got me!"
        scene 10_366 with Dissolve(1)
        mc "You're right about that."
        ni "Haha."
        scene 10_367 with Dissolve(1)
        ""
        scene 10_369 with Dissolve(1)
        mc "How are you feeling today? Still exhausted?"
        ni "No, I'm good now. Sleeping a bit longer did the trick."
        mc "Alright."
        scene 10_426 with Dissolve(1)
        mc "Oh, by the way. I'll be at the neighbours' in a bit to do some yard stuff."
        mc "So if you're looking for me, I'm there."
        ni "First you woke me and now you're leaving?"
        mc "Sorry..."
        scene 10_360 with Dissolve(1)
        ni "I guess I'll go shower then and eat some breakfast."
        mc "There's still coffee and pancakes in the kitchen."
        scene 10_427 with Dissolve(1)
        ni "Pancakes..."
        mc "Yeah, Mom made pancakes."
        ni "Pancakes?"
        mc "Don't look at me like that. I'm actually serious this time!"
        scene 10_428 with Dissolve(1)
        ni "There'd better be pancakes this time."
        ni "Because if not, you're going to make me some!"
        scene 10_429 with Dissolve(1)
        mc "One small problem. I don't know how to make pancakes."
        ni "You don't know how to make pancakes?"
        mc "No. I never had to..."
        ni "*Shakes head* You're so spoiled!"
        mc "Hey. It's not my fault people always make them for me."
        scene 10_430 with Dissolve(1)
        mc "Anyway, I'm heading next door."
        mc "If you need me, just come on over. Melissa won't mind."
        ni "Will do. Have fun."
        scene 10_371 with Dissolve(1)
        ""
        jump Week4_Saturday_Melissa

label Week4_Saturday_Morning_Cara:
    scene black with Dissolve(2)
    pause 2
    n "Saturday morning, 8:51."
    scene 10_415 with Dissolve(1)
    mc "Morning, Mom."
    m "Good morning, honey."
    scene 10_416 with Dissolve(1)
    mc "Oh... You're making pancakes. Nice! Can I have some?"
    m "Of course."
    mc "Do we have maple syrup?"
    m "In the fridge."
    scene 10_417 with Dissolve(1)
    m "Cara still sleeping?"
    mc "I think so, yes."
    m "She okay?"
    mc "Yeah, she was tired yesterday, and she's someone who can easily sleep till noon."
    m "Sounds just like you."
    mc "Heh..."
    scene 10_418 with Dissolve(1)
    m "How is the new mattress? Comfortable?"
    if Cara_Week4_Friday_SleepBed == False:
        mc "Yeah, I slept really well."
        mc "I'll set up the bed later today."
        scene black with Dissolve(1)
        pause 2
        scene 10_419a with Dissolve(1)
        mc "..."
        mc "{i}(Is she still sleeping?){/i}"
        scene 10_434 with Dissolve(1)
        mc "{i}(She is.){/i}"
        mc "{i}(She must have been really tired yesterday.){/i}"
        scene 10_435 with Dissolve(1)
        mc "Cara?"
        c "Hmm?"
        mc "Sorry to wake you."
        scene 10_436 with Dissolve(1)
        mc "Just wanted to tell you that I'm at the neighbours' to do some yard stuff."
        mc "If you need me, just come on over."
        c "Alright."
        mc "Kay, sleep some more. See you later."
        jump Week4_Saturday_Melissa
    else:
        mc "{i}(I wouldn't know.){/i}"
        mc "Uh... Yeah... It's good."
        mc "I'll set up the bed later today."
        scene black with Dissolve(1)
        pause 2
        scene 10_419a with Dissolve(1)
        mc "..."
        mc "{i}(Is she still sleeping?){/i}"
        scene 10_420 with vpunch
        mc "Good morning, cutie!"
        scene 10_437 with Dissolve(1)
        c "Nggh... [mc]..."
        mc "Haha, sorry."
        scene 10_438 with Dissolve(1)
        c "Haha, stop."
        c "Let me sleep a bit more."
        scene 10_439 with Dissolve(1)
        mc "Can I have a little cuddle?"
        c "Just a little!"
        scene 10_440 with Dissolve(1)
        mc "Maybe more than a little."
        c "Heh..."
        scene 10_441 with Dissolve(1)
        c "Okay, that's enough. You're way too hot."
        mc "Thank you!"
        c "No... I mean... Your body... No..."
        mc "Haha."
        scene 10_442 with Dissolve(1)
        mc "I thought you like it when I snuggle up against you."
        c "I do. But it's so warm in your room already."
        mc "It's on the south side, so the sun is hitting it the whole day, basically."
        mc "But I'll let you sleep a bit more. I need to go anyway."
        scene 10_443 with Dissolve(1)
        c "Where are you going?"
        mc "Next door. I need to do some yard stuff."
        c "Oh..."
        scene 10_444 with Dissolve(1)
        mc "Yeah, so if you need me, just come on over. Melissa won't mind."
        mc "There are also pancakes in the kitchen if you're hungry."
        c "Okay, thank you."
        scene 10_445 with Dissolve(1)
        mc "See you later, then."
        c "Bye."
        jump Week4_Saturday_Melissa

label Week4_Saturday_Morning_Erynn:
    scene black with Dissolve(2)
    pause 2
    scene 10_345 with Dissolve(1)
    er "{i}(Of course. Still sleeping...){/i}"
    scene 10_346 with vpunch
    er "Good morning, sleepyhead!"
    er "Time to wake up!"
    scene 10_446 with Dissolve(1)
    er "Uh..."
    scene 10_447 with Dissolve(1)
    er "What is this? Pillows?"
    mc "Haha."
    scene 10_448 with Dissolve(1)
    er "[mc]!"
    mc "Did you really think that would work a second time?"
    mc "I heard you talking to Mom downstairs."
    er "..."
    menu:
        "Jump on her[KoGa3AutoWTChange1]{size=-4}(Erynn Points+2) {/size} {/color}":
            $ Erynn_Points += 2
            # Erynn (44)
            scene 10_449 with Dissolve(1)
            mc "This is how you do it!"
            er "Aah-haha, [mc]!"
            scene 10_450 with Dissolve(1)
            mc "You look happy today."
            er "I am. Feeling much better."
            if Erynn_LikeMC == True:
                scene 10_451 with Dissolve(1)
                ""
            else:
                pass
        "Sit next to her":
            scene 10_452 with Dissolve(1)
            mc "Hey, how are you?"
            er "I'm good. Much better than yesterday."
    scene 10_453 with Dissolve(1)
    mc "Anyway, why are you here this morning?"
    er "I came to thank you again for yesterday."
    mc "You're welcome."
    er "And... I've also talked to Mom about... that."
    scene 10_454 with Dissolve(1)
    mc "You did? That's great, Erynn! A big step."
    mc "That mustn't have been easy. I'm proud of you."
    er "Thank you."
    mc "What did she say?"
    scene 10_455 with Dissolve(1)
    er "Not much at first. Seemed like she was in a state of shock."
    er "Then a sudden rush of emotions. She hugged me and started crying. I've never seen Mom cry before. It broke my heart."
    er "She got... well, not angry but... I don't know. She felt terrible that I kept it to myself for so long and couldn't confide in her."
    scene 10_456 with Dissolve(1)
    mc "How do you feel now?"
    er "Much better. I should've talked to her earlier but..."
    mc "You needed someone to push you."
    scene 10_457 with Dissolve(1)
    er "Yeah. So thank you, [mc]!"
    scene 10_458 with Dissolve(1)
    mc "Did she have any idea what we can do?"
    er "I didn't tell her about your suggestion, because I know she won't agree to that."
    er "But she asked me to talk to Emily first. She's coming by tomorrow."
    mc "That's good. She might be able to help, too."
    scene 10_459 with Dissolve(1)
    er "But enough of this. Today is a good day."
    mc "Yeah? What are the plans?"
    er "Spending the day with Lexi. Brunch, shopping, beach."
    if Alexis_Sex == False:
        mc "That sounds like fun."
    else:
        if Alexis_Dating == False:
            if Erynn_Week2_Tuesday_AlexisFight == False:
                mc "That sounds like fun."
                mc "{i}(I guess Alexis never told Erynn about our hookup. Maybe for the better.){/i}"
            else:
                if Alexis_Week2_Wednesday_Breakup == True:
                    mc "Oh, you're friends again?"
                    er "We talked it out a few days ago."
                    mc "About time!"
                    mc "{i}(I guess Alexis didn't say anything to Erynn about the breakup.){/i}"
                else:
                    if Alexis_Week3_Wednesday_TC_Breakup == True:
                        mc "Oh, you're friends again?"
                        er "We talked it out a few days ago."
                        mc "About time!"
                        mc "{i}(I guess Alexis didn't say anything to Erynn about the breakup.){/i}"
                    else:
                        if Layla_Week3_Wednesday_TC_Alexis_DateBoth == True:
                            mc "Oh, you're friends again?"
                            er "We talked it out a few days ago."
                            mc "About time!"
                            mc "{i}(I guess Alexis didn't say anything to Erynn about the breakup.){/i}"
                            mc "{i}(If she knew, we wouldn't be talking like this right now. I hope it stays that way.){/i}"
                        else:
                            mc "Oh, you're friends again?"
                            er "We talked it out a few days ago."
                            mc "About time!"
        else:
            mc "Right. She told me yesterday she's spending the day with you."
    scene 10_460 with Dissolve(1)
    er "What are your plans?"
    mc "I don't know yet."
    er "Want to come with us?"
    scene 10_461 with Dissolve(1)
    mc "Eh... Brunch? Shopping? If it was only beach, I'd come. But all that other stuff..."
    er "It's fun."
    mc "I don't know. I'd be the third wheel."
    mc "Besides. I have to do some lawnmowing for Melissa, anyway."
    er "Next time then."
    scene 10_462 with Dissolve(1)
    er "Alright, let's go, then. I need to get ready, too."
    mc "You're not ready? You look ready."
    er "Just a few touch-ups!"
    mc "Heh..."
    scene 10_463 with Dissolve(1)
    mc "I like your outfit by the way."
    er "Yeah?"
    mc "You look good."
    er "Thank you."
    scene 10_464 with Dissolve(1)
    if Alexis_Dating == True:
        er "Wait until you see Lex. You're probably going to change your mind immediately and come with us."
        mc "Haha, maybe."
    else:
        pass
    scene 10_465 with Dissolve(1)
    er "The pool needs some cleaning too. Lots of leaves in there."
    mc "Melissa has a big net in the garage. I'll get it for you."
    er "Heh... You think you're so clever, huh?"
    mc "I am. There's a reason why I take the advanced math class."
    scene 10_466 with Dissolve(1)
    er "A very good reason. Who was the one spending lots of her time teaching you math after school?"
    mc "Haha."
    er "Don't laugh, answer the question!"
    jump Week4_Saturday_Melissa

label Week4_Saturday_Morning2:
    scene black with Dissolve(2)
    pause 2
    n "Saturday morning, 8:51."
    scene 10_415 with Dissolve(1)
    mc "Morning, Mom."
    m "Good morning, honey."
    scene 10_416 with Dissolve(1)
    mc "Oh... You're making pancakes. Nice! Can I have some?"
    m "Of course."
    mc "Do we have maple syrup?"
    m "In the fridge."
    scene 10_417 with Dissolve(1)
    m "What's the plan for today?"
    mc "Don't know yet. I have to do some lawnmowing for Melissa first, anyway."
    scene 10_418 with Dissolve(1)
    m "I'm going shopping with her a little later."
    m "I don't know when I'll be back."
    jump Week4_Saturday_Melissa

label Week4_Saturday_Melissa:
    scene black with Dissolve(1)
    pause 2
    stop music fadeout 1.0
    play music ("Music/LoFi Upbeat 1.mp3", "Music/LoFi Upbeat 2.mp3", "Music/LoFi Upbeat 3.mp3", "Music/LoFi Upbeat 4.mp3") volume 0.2
    if Erynn_End == True:
        $ Melissa_Points -= 10
        $ Melissa_End = True
        scene 10_467 with Dissolve(1)
        mc "{i}(There she is.){/i}"
        menu:
            "Watch":
                scene 10_469 with Dissolve(1)
                mc "{i}(That body...){/i}"
            "Help her":
                scene 10_470 with Dissolve(1)
                mc "Let me help you."
                me "Oh, hey... Thank you, [mc]!"
        scene black with Dissolve(1)
        transform moveup:
            xalign 0.5 yalign 1.0
            linear 5.0 yalign 0.0
        show 10_472 at moveup
        pause 3
        mc "..."
        scene 10_474 with Dissolve(1)
        mc "You changed your hair."
        me "I styled a client yesterday and she wanted this colour. I really liked it on her and since I had some left over, I tried it on myself."
        me "I'm not too sure yet, though."
        menu:
            "Looks good":
                mc "I think it looks good."
                me "Thank you."
            "Not good":
                scene 10_475 with Dissolve(1)
                mc "Hmm, I don't know either. It's... different..."
                me "Haha. Different, huh? Is that your nice way of saying it's shit?"
                mc "Uh, no... I..."
                me "Haha. I appreciate your honesty!"
                scene 10_476 with Dissolve(1)
                me "What colour would you recommend?"
                mc "I've never seen you with your natural hair colour. So, maybe that?"
                me "It's been over twenty years since I was last blonde. Yeah, maybe."
        scene 10_496 with Dissolve(1)
        mc "Is there anything in particular you need to have done?"
        me "Hmm... Not really. The usual? Oh, but can you help me set up the beach umbrella?"
        mc "Sure."
    else:
        if Erynn_Week3_Monday_Blackmailhelp == True:
            $ Melissa_Points += 2
            # Melissa (16)
            scene 10_471 with Dissolve(1)
            er "Hey, Mom. Look! I've found the pool boy."
            mc "..."
            mc "Hi, Mel!"
            me "Hey there."
            scene black with Dissolve(1)
            transform moveup:
                xalign 0.5 yalign 1.0
                linear 5.0 yalign 0.0
            show 10_472 at moveup
            pause 3
            mc "..."
            scene 10_473 with Dissolve(1)
            mc "You changed your hair."
            me "I styled a client yesterday and she wanted this colour. I really liked it on her and since I had some left over, I tried it on myself."
            me "I'm not too sure yet, though."
            menu:
                "Looks good":
                    mc "I think it looks good."
                    me "Thank you."
                "Not good":
                    scene 10_475 with Dissolve(1)
                    mc "Hmm, I don't know either. It's... different..."
                    me "Haha. Different, huh? Is that your nice way of saying it's shit?"
                    er "Don't listen to him, Mom! What does..."
                    me "No, I appreciate his honesty!"
                    scene 10_476 with Dissolve(1)
                    me "What colour would you recommend?"
                    mc "I've never seen you with your natural hair colour. So, maybe that?"
                    me "It's been over twenty years since I was last blonde. Yeah, maybe."
            scene 10_477 with Dissolve(1)
            er "I'll let you guys talk hair. I need to get ready before Alexis arrives."
            er "See you later."
            scene black with Dissolve(1)
            pause 2
            scene 10_478 with vpunch
            me "Thank you!"
            mc "Uh..."
            scene 10_479 with Dissolve(1)
            mc "What are you hugging me for this time?"
            me "You know what! Erynn told me yesterday."
            me "Thank you, [mc]!"
            mc "..."
            mc "{i}(Why am I getting turned on by this situation?){/i}"
            scene 10_480 with Dissolve(1)
            me "I'm so happy you're here and helping her."
            me "She wouldn't have come to me if it wasn't for you telling her to."
            mc "{i}(Is she crying?){/i}"
            scene 10_481 with Dissolve(1)
            mc "I'm here for Erynn if she needs me. Same for you, Melissa!"
            mc "You were there for me countless times when I was younger. Even last time, with the Andres stuff."
            mc "If I can help in any way, I will."
            scene 10_482 with Dissolve(1)
            ""
            scene 10_483 with Dissolve(1)
            me "Promise me though, you won't do anything reckless."
            me "Let me take care of this, alright?"
            mc "{i}(I can't promise you that.){/i}"
            mc "Alright."
            me "And please don't tell Erynn I've been crying again."
            mc "I won't."
            if Melissa_Points >= 13:
                scene 10_484 with Dissolve(1)
                me "Hey, a little warning. I'm gonna hug you again, and this time for no reason other than I want to."
                mc "Haha, okay."
                scene 10_485 with Dissolve(1)
                mc "You're a good hugger! Not like those weak, barely touching... things."
                me "Heh..."
                menu:
                    "Grab her ass":
                        scene 10_486 with Dissolve(1)
                        me "Speaking about barely touching..."
                        mc "Uh, sorry. I got caught up in the moment."
                        me "Uh-huh... I'll let it slide this time, but next time..."
                    "Don't":
                        pass
                scene 10_487 with Dissolve(1)
                me "Aah... [mc]!"
                mc "Haha, I didn't know you had such a girly scream!"
                me "Haha..."
                scene 10_488 with Dissolve(1)
                er "Mom, do you know where..."
                er "..."
                scene 10_489 with Dissolve(1)
                er "What are you guys doing?"
                me "Haha. Hey, Erynn."
                menu:
                    "Playing":
                        mc "We're just playing around."
                        er "You are so weird..."
                        scene 10_495 with Dissolve(1)
                        me "Are you looking for something?"
                        er "No, never mind."
                    "Joke[KoGa3AutoWTChange1]{size=-4}(Melissa Week4 Saturday Kiss, Melissa Points+2) {/size} {/color}":
                        $ Melissa_Week4_Saturday_Kiss = True
                        $ Melissa_Points += 2
                        # Melissa (18)
                        mc "I think we've been found out."
                        er "What?"
                        scene 10_490 with Dissolve(1)
                        mc "I guess it's time we told her."
                        er "Told me what?"
                        mc "Melissa and I have been secretly dating."
                        er "..."
                        scene 10_491 with Dissolve(1)
                        er "Secretly? I've known this for years."
                        mc "{i}(Haha, she's playing along?){/i}"
                        mc "Oh... Really?"
                        mc "{i}(Let's see how she reacts to this.){/i}"
                        mc "I guess we don't have to hide this anymore, either."
                        scene 10_492 with Dissolve(1)
                        me "..."
                        er "Oh my god... I was kidding!"
                        er "That is just... Ew... Stop!"
                        scene 10_493 with Dissolve(1)
                        er "You do realise you just kissed my mom, yeah?"
                        mc "Haha."
                        er "That's not funny! That's weird! Ugh..."
                        scene 10_494 with Dissolve(1)
                        mc "Sorry, Melissa. I might have taken it a little too far. I didn't..."
                        me "Don't worry about it. But don't tease her too much."
                        mc "I won't."
                scene 10_496 with Dissolve(1)
                mc "Well, enough playing around."
                mc "Is there anything in particular you need to have done?"
                me "Hmm... Not really. The usual? Oh, but can you help me set up the beach umbrella?"
                mc "Sure."
            else:
                scene 10_496 with Dissolve(1)
                mc "Is there anything in particular you need to have done?"
                me "Hmm... Not really. The usual? Oh, but can you help me set up the beach umbrella?"
                mc "Sure."
        else:
            $ Melissa_Points -= 10
            $ Melissa_End = True
            scene 10_467 with Dissolve(1)
            mc "{i}(There she is.){/i}"
            menu:
                "Watch":
                    scene 10_469 with Dissolve(1)
                    mc "{i}(That body...){/i}"
                "Help her":
                    scene 10_470 with Dissolve(1)
                    mc "Let me help you."
                    me "Oh, hey... Thank you, [mc]!"
            scene black with Dissolve(1)
            transform moveup:
                xalign 0.5 yalign 1.0
                linear 5.0 yalign 0.0
            show 10_472 at moveup
            pause 3
            mc "..."
            scene 10_474 with Dissolve(1)
            mc "You changed your hair."
            me "I styled a client yesterday and she wanted this colour. I really liked it on her and since I had some left over, I tried it on myself."
            me "I'm not too sure yet, though."
            menu:
                "Looks good":
                    mc "I think it looks good."
                    me "Thank you."
                "Not good":
                    scene 10_475 with Dissolve(1)
                    mc "Hmm, I don't know either. It's... different..."
                    me "Haha. Different, huh? Is that your nice way of saying it's shit?"
                    mc "Uh, no... I..."
                    me "Haha. I appreciate your honesty!"
                    scene 10_476 with Dissolve(1)
                    me "What colour would you recommend?"
                    mc "I've never seen you with your natural hair colour. So, maybe that?"
                    me "It's been over twenty years since I was last blonde. Yeah, maybe."
            scene 10_496 with Dissolve(1)
            mc "Is there anything in particular you need to have done?"
            me "Hmm... Not really. The usual? Oh, but can you help me set up the beach umbrella?"
            mc "Sure."
    scene black with Dissolve(1)
    pause 2
    scene 10_497 with Dissolve(1)
    mc "Here? Or do you want it somewhere else?"
    me "That's perfect, thank you."
    scene 10_498 with Dissolve(1)
    me "I'll get us something to drink. Do you want anything in particular?"
    mc "It's a little early for a beer, so... just a soda, I guess."
    me "Alright."
    if Melissa_Week4_Saturday_Kiss == True:
        scene 10_499 with Dissolve(1)
        mc "{i}(I can't believe I kissed her...){/i}"
        mc "{i}(It was just a peck, but still...){/i}"
        mc "{i}(I never looked at her in that way before, but ever since I saw her lying here topless...){/i}"
        mc "{i}(Then the see-through bikini, I... Fuck! She's just so hot!){/i}"
    else:
        pass
    scene black with Dissolve(1)
    pause 2
    scene 10_500 with Dissolve(1)
    ""
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 10_501 at moveup
    pause 3
    mc "..."
    if Erynn_End == True:
        scene 10_502 with Dissolve(1)
        mc "{i}(I probably deserve those looks.){/i}"
    else:
        if Alexis_Dating == False:
            if Erynn_Week3_Monday_Blackmailhelp == True:
                if Alexis_Sex == True:
                    scene 10_503 with Dissolve(1)
                    mc "Have fun, you two."
                    er "Thanks, [mc]."
                    er "See you later."
                    mc "{i}(I hope Alexis won't talk about what happened between us.){/i}"
                else:
                    scene 10_503 with Dissolve(1)
                    mc "Have fun, you two."
                    er "Thanks, [mc]."
                    er "See you later."
            else:
                scene 10_503 with Dissolve(1)
                mc "Have fun, you two."
                er "Thanks."
        else:
            scene 10_504 with Dissolve(1)
            a "Hey there."
            a "Give me a second."
            er "Sure."
            scene 10_505 with Dissolve(1)
            mc "Hey, sexy."
            a "Hi."
            mc "You look pretty."
            a "Thank you."
            scene 10_506 with Dissolve(1)
            mc "How are you?"
            a "I'm good. And thank you for making me talk to Erynn."
            mc "Heh, everyone is hugging and thanking me today. I must be really good at it."
            a "..."
            if Melissa_Week4_Saturday_Kiss == True:
                scene 10_507 with Dissolve(1)
                a "There's something we're gonna talk about later, though!"
                mc "You mean..."
                if Alexis_RiversideStory == False:
                    if Nikki_Girlfriend == True:
                        mc "{i}(Nikki? Did Erynn tell her? She promised she wouldn't.){/i}"
                    else:
                        if Cara_Girlfriend == True:
                            mc "{i}(Cara? Did Erynn tell her? She promised she wouldn't){/i}"
                        else:
                            pass
                else:
                    pass
                a "The kiss!"
                mc "Oh... That! That was just a joke."
                a "Uh-huh..."
                scene 10_508 with Dissolve(1)
                a "Call me later, okay?"
                mc "I will. Have fun."
                if Erynn_LikeMC == True:
                    scene 10_509 with Dissolve(1)
                    er "..."
                else:
                    pass
                scene 10_511 with Dissolve(1)
                a "Bye, [mc]."
                mc "Uh... No kiss?"
                a "You've gotten one already!"
                mc "..."
                scene 10_512 with Dissolve(1)
                mc "Haha."
                mc "Have fun girls!"
            else:
                scene 10_508 with Dissolve(1)
                a "Call me later, okay?"
                mc "I will. Have fun."
                if Erynn_LikeMC == True:
                    scene 10_509 with Dissolve(1)
                    er "..."
                else:
                    pass
                scene 10_510 with Dissolve(1)
                a "Bye, [mc]."
                mc "See you!"
            scene 10_513 with Dissolve(1)
            er "You guys are so cute together."
            a "Thank you."
            er "A little jealous here."
            a "Hehe."
            scene 10_514 with Dissolve(1)
            er "What do you call him?"
            a "Uhm... [mc]?"
            er "No, I mean, don't you have couple names for each other? Like babe or something?"
            a "Not really. I asked him to call me Lexi and that's what he does. And I've always called him [mc]."
            scene 10_515 with Dissolve(1)
            a "You think I should?"
            er "That's up to you. If you don't like it, don't. But you can try, and see how he reacts."
            a "Hmm..."
            scene 10_516 with Dissolve(1)
            a "I'd probably stick to babe or baby. Maybe honey?"
            a "Never mind... That's what his mom calls him. That'd be weird."
            a "It isn't that easy if you have to think about it."
            er "Yeah, I believe it just comes naturally."
            scene 10_517 with Dissolve(1)
            a "Darling... Haha."
            er "Haha."
            scene 10_518 with Dissolve(1)
            a "BYE, DARLING!"
            er "Haha."
            mc "*Shakes head*"
    if Melissa_Week4_Saturday_Kiss == True:
        $ Melissa_Week4_Saturday_Dream = True
        jump Week4_Saturday_Melissa_Dream
    else:
        scene black with Dissolve(1)
        pause 2
        scene 10_519 with Dissolve(1)
        me "I've put your soda here in the shade."
        mc "Thank you, Melissa."
        jump Week4_Saturday_Melissa2

label Week4_Saturday_Melissa_Dream:
    scene black with Dissolve(1)
    pause 2
    scene 10_519 with Dissolve(1)
    me "I've put your soda here in the shade."
    mc "Thank you, beautiful."
    scene 10_520 with Dissolve(1)
    me "She isn't here anymore."
    mc "You're still beautiful, though."
    me "..."
    scene 10_521 with Dissolve(1)
    me "{i}(This boy... He reminds me so much of... *Sigh*){/i}"
    scene black with Dissolve(2)
    pause 2
    scene 10_522 with Dissolve(1)
    x "Hey, beautiful."
    me "..."
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 10_523 at moveup
    pause 3
    me "Hey."
    scene 10_524 with Dissolve(1)
    me "Couldn't make up your mind?"
    x "I didn't know what flavour you'd like, so I got one of each."
    me "Thank you."
    scene 10_525 with Dissolve(1)
    x "But it seems I've forgotten the sweetest one."
    me "Yeah? Which one is that?"
    scene 10_526 with Dissolve(1)
    x "This one right here!"
    me "..."
    scene 10_527 with Dissolve(1)
    ""
    scene 10_528 with Dissolve(1)
    x "Want to get out of here?"
    me "*Nods*"
    scene 10_529 with Dissolve(1)
    mc "You are so beautiful!"
    mc "Can I kiss you again?"
    scene 10_530 with vpunch
    me "Aaah!"
    me "Not again!"
    scene 10_531 with Dissolve(1)
    mc "Haha. What was that?"
    me "..."
    mc "Bad dream or something?"
    scene 10_532 with Dissolve(1)
    mc "You're all sweaty and feel hot. Are you alright?"
    mc "Maybe stay out of the sun for a while and drink something."
    mc "Melissa?"
    scene 10_533 with Dissolve(1)
    mc "..."
    scene 10_534 with Dissolve(1)
    ""
    scene 10_535 with vpunch
    me "[mc], stop!"
    me "Sorry... I..."
    me "I shouldn't have done this... I don't know why I..."
    scene 10_536 with vpunch
    me "..."
    scene 10_537 with Dissolve(1)
    me "[mc]! We can't."
    me "What about Erynn... And Emily... This..."
    mc "Erynn and I are friends. Always have been, always will be. And Mom will understand."
    me "[mc]..."
    scene 10_538 with Dissolve(1)
    mc "I want you, Melissa!"
    me "..."
    mc "And I know you want me, too!"
    scene 10_539 with Dissolve(1)
    ""
    scene 10_540 with Dissolve(1)
    me "..."
    scene 10_541 with Dissolve(1)
    ""
    scene 10_542 with Dissolve(1)
    ""
    scene 10_543 with Dissolve(1)
    me "Mmm..."
    scene 10_544 with Dissolve(1)
    ""
    scene 10_545 with Dissolve(1)
    ""
    scene 10_546 with Dissolve(1)
    ""
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 10_547 at moveup
    pause 3
    mc "You are so beautiful, Mel!"
    mc "Can't wait to finally taste you!"
    scene 10_548 with Dissolve(1)
    ""
    scene 10_549 with Dissolve(1)
    ""
    scene 10_550 with Dissolve(1)
    me "*Moaning*"
    scene 10_551 with Dissolve(1)
    ""
    scene 10_552 with Dissolve(1)
    ""
    scene 10_553 with Dissolve(1)
    ""
    scene 10_554 with Dissolve(1)
    ""
    scene 10_555 with Dissolve(1)
    me "Ah..."
    scene 10_556 with Dissolve(1)
    mc "You feel so good!"
    me "Fuck me, [mc]!"
    scene 10_557 with Dissolve(1)
    me "*Moaning*"
    scene 10_558 with Dissolve(1)
    ""
    show 10_559
    ""
    show 10_560
    ""
    scene 10_561 with Dissolve(1)
    ""
    scene 10_562 with Dissolve(1)
    ""
    scene 10_563 with Dissolve(1)
    ""
    scene 10_564 with Dissolve(1)
    ""
    show 10_565
    ""
    show 10_566
    ""
    scene 10_567 with Dissolve(1)
    me "[mc]..."
    me "I'm cumming..."
    scene 10_568 with Dissolve(1)
    mc "Melissa."
    me "*Moaning* I'm cumming... [mc]..."
    mc "Melissa?"
    mc "MELISSA?"
    scene 10_530 with vpunch
    me "Aaah..."
    mc "Are you alright, Mel?"
    scene 10_531 with Dissolve(1)
    mc "You were saying, [mc] come, come..."
    me "..."
    mc "I thought you were stung by a bee or something."
    scene 10_532 with Dissolve(1)
    mc "You're all sweaty and feel hot. Bad dream?"
    me "..."
    scene 10_569 with vpunch
    me "Nooo... This..."
    mc "Haha, no? Good dream?"
    mc "{i}(She looks so flustered.){/i}"
    scene 10_570 with Dissolve(1)
    me "No... It was just... I don't know..."
    me "I can't believe this happened."
    mc "What?"
    me "*Sigh* Never mind..."
    scene 10_571 with Dissolve(1)
    mc "Drink something, or jump in the pool to cool off a bit."
    mc "It's scorching today."
    me "That's a good idea."
    mc "{i}(Is she...){/i}"
    scene 10_572 with Dissolve(1)
    mc "{i}(Wet?){/i}"
    mc "{i}(Did she have a wet dream?){/i}"
    mc "{i}(Can girls actually have a wet dream? And who was she dreaming about?){/i}"
    mc "{i}(She was saying my name before... Or am I imagining things now, too? Wishful thinking, maybe? Guess the heat is getting to me as well.){/i}"
    $ renpy.end_replay()
    jump Week4_Saturday_Melissa2

label Week4_Saturday_Melissa2:
    if Cara_Girlfriend == True:
        scene black with Dissolve(1)
        pause 2
        scene 10_573 with Dissolve(1)
        me "Are you waiting for [mc]?"
        mc "{i}(Who is she talking to? Mom? Or maybe Cara?){/i}"
        scene 10_574 with Dissolve(1)
        mc "Hey. Finally awake?"
        c "Hehe, yeah."
        mc "Did you grow a few inches while sleeping?"
        c "Haha. I'm standing on a planter."
        scene 10_575 with Dissolve(1)
        mc "I'm almost finished."
        c "Don't worry, take your time. I'll wait."
        me "You can also come over and wait here if you like."
        c "Uhm... Okay."
        scene 10_576 with Dissolve(1)
        mc "Cara, Melissa. Melissa, Cara."
        me "Nice to meet you, Cara."
        c "You too, Melissa."
        scene 10_577 with Dissolve(1)
        mc "I'll go continue. You girls can chat, gossip, or whatever you do."
        me "Heh, don't worry. We will!"
        c "Have fun."
        scene 10_578 with Dissolve(1)
        c "It's really warm today."
        me "It is. Want to dip our feet in the pool?"
        c "I'd like that."
        scene 10_579 with Dissolve(1)
        c "This feels so nice."
        me "If it's getting too warm in the sun, we can also move the umbrella here."
        c "It's fine for now."
        me "Or you can jump in the pool."
        scene 10_580 with Dissolve(1)
        mc "And with jump, she means push. Melissa is notorious for 'helping' people get in pools. So beware!"
        if Melissa_Week1_Saturday_Payback == True:
            me "Hey! You slipped, as far as I remember. And weren't you the one who pulled me in?"
            mc "Never happened."
            me "Uh-huh. My revenge is still coming. You'd better beware."
            c "Haha."
        else:
            me "Hey! You slipped, as far as I remember."
            mc "Call it whatever you want!"
            c "Haha."
        scene 10_581 with Dissolve(1)
        me "Are you enjoying your vacation here so far?"
        c "I am. I wish we had this kind of weather at home."
        me "You're from Alvarado?"
        c "Riverside."
        me "Oh right, Riverside."
        c "We have some nice weeks during the summer, but not like this."
        scene 10_582 with Dissolve(1)
        me "I have to ask. I've been eyeing your hair since you came over. Is that your natural colour?"
        c "It is."
        me "It's really pretty. I'm so jealous."
        c "Thank you. I like your hair too. Especially the purple accents."
        me "Thanks. I changed it this morning, actually, as an experiment."
        scene 10_583 with Dissolve(1)
        c "I've been wanting to change mine for some time."
        me "The cut, the colour?"
        c "Both... I've had this hairstyle for a few years now."
        c "I've looked at some magazines, and I've found a few hairstyles I like, but I'm scared that if I change it, it won't look good on me."
        scene 10_584 with Dissolve(1)
        mc "Just an FYI. I like your hair how it is!"
        c "Heh, thanks."
        mc "But if you want advice, now's your chance. Melissa is a hairstylist."
        scene 10_585 with Dissolve(1)
        c "Oh, you are?"
        me "Yes, we can go look at some hairstyles if you'd like. I have plenty of magazines inside."
        c "Really? That'd be amazing."
        scene 10_586 with Dissolve(1)
        me "Alright. Wait here for a second. I'll get you a towel."
        c "Thank you."
        scene 10_587 with Dissolve(1)
        c "So, that's Erynn's mom?"
        mc "Uh-huh."
        c "She looks like a really cool mom."
        mc "Melissa is awesome, yeah."
        scene black with Dissolve(2)
        pause 2
        scene 10_588 with Dissolve(1)
        mc "{i}(*Sigh* How long can they talk about hair?){/i}"
        mc "{i}(It must be at least an hour already...){/i}"
        if Melissa_Week4_Saturday_Kiss == True:
            scene 10_589 with Dissolve(1)
            mc "{i}(Still can't get the image of Melissa out of my head, though.){/i}"
            mc "{i}(I'm really curious what she was dreaming about. It looked like she was enjoying it.){/i}"
            scene black with Dissolve(1)
            transform moveup:
                xalign 0.5 yalign 1.0
                linear 5.0 yalign 0.0
            show 10_590 at moveup
            pause 3
            ""
            scene 10_591 with Dissolve(1)
            me "..."
            scene 10_592 with vpunch
            me "Sleeping on the job?"
            mc "Aaah... Melissa!"
            me "Haha."
            scene 10_593 with Dissolve(1)
            mc "Damn, you scared me."
            me "This time you were the one dreaming, huh? Was it a good one at least?"
            mc "Uhm..."
            mc "{i}(Yes!){/i}"
            scene 10_594 with Dissolve(1)
            mc "Well, this makes us even again, at least."
            me "Even? Oh, honey. You can't be more wrong. As I said before. You are not prepared!"
            mc "..."
            scene 10_595 with Dissolve(1)
            me "Good luck!"
            mc "{i}(Kiss of death?){/i}"
            scene 10_596 with Dissolve(1)
            me "Anyway. Are you ready to see Cara's new hair?"
            mc "Wait... Did you give her a haircut? I thought you were only looking at some examples."
            me "She found one she liked pretty quickly, and I agreed that it would look good on her. So, I offered to style it for her."
            mc "Oh..."
        else:
            scene 10_596 with Dissolve(1)
            me "Hey!"
            mc "Hey... What were you doing for so long?"
            me "I gave Cara a new haircut."
            mc "Wait... You did? I thought you were only looking at some examples."
            me "She found one she liked pretty quickly, and I agreed that it would look good on her. So, I offered to style it for her."
            mc "Oh..."
        scene 10_597 with Dissolve(1)
        me "Can I call her?"
        mc "Uh, yeah."
        me "Cara! You can come out."
        scene 10_598 with Dissolve(1)
        mc "..."
        scene black with Dissolve(1)
        transform moveup:
            xalign 0.5 yalign 1.0
            linear 5.0 yalign 0.0
        show 10_599 at moveup
        pause 3
        ""
        scene 10_600 with Dissolve(1)
        mc "Look at you! Just wow!"
        mc "Very beautiful."
        c "Thank you."
        scene 10_601 with Dissolve(1)
        mc "What a difference a hairstyle can make. You look... not older, but..."
        me "More mature."
        mc "Yes, mature. That's the word."
        scene 10_602 with Dissolve(1)
        mc "Do you like it?"
        c "I love it!"
        scene 10_603 with Dissolve(1)
        c "Thank you so very much, Melissa."
        c "I really, really, really love it!"
        me "Haha. You're welcome."
        scene 10_604 with Dissolve(1)
        m "Hey. Weren't you coming over?"
        me "Oh... Sorry, Emily. I forgot about that."
        scene 10_605 with Dissolve(1)
        m "Cara! You've got a new haircut!"
        c "Yes, thanks to Melissa."
        scene 10_606 with Dissolve(1)
        m "You look so pretty! It suits you."
        c "Thank you!"
        scene 10_607 with Dissolve(1)
        m "Ah, sorry. I didn't want to ruin it."
        c "Haha, it's fine."
        mc "Good job, Mom... She's had this for two minutes before you..."
        m "..."
        scene 10_608 with Dissolve(1)
        m "It wasn't on purpose. I just like to touch pretty things!"
        m "But let's see if you did a good job here."
        mc "What? You're gonna measure if the grass has the correct length?"
        scene 10_609 with Dissolve(1)
        m "See! I knew it!"
        mc "Oh... Did I forget to cut one blade of grass or something?"
        m "No! Come check it."
        mc "..."
        scene 10_610 with Dissolve(1)
        mc "I don't see anything."
        m "..."
        mc "There's nothing wrong here..."
        scene 10_611 with vpunch
        mc "Hey!"
        scene 10_612 with Dissolve(1)
        mc "I knew it! The moment you walked to the pool, I suspected you would do this."
        m "Then why did you come?"
        mc "For that one per cent chance of you actually being serious!"
        scene 10_613 with Dissolve(1)
        m "Haha. I'm sorry, honey."
        mc "You girls are all the same!"
        me "Haha."
        scene 10_614 with Dissolve(1)
        m "Are you still coming over, or...?"
        me "I have a better idea."
        m "Hmm?"
        scene 10_615 with Dissolve(1)
        me "What do you think of mimosas?"
        m "Oh... I see where this is going."
        me "Let me get ready then."
        scene 10_616 with Dissolve(1)
        me "Do you want to come with us, Cara?"
        me "I don't know if you've met my daughter Erynn, already. She's gonna be there together with her friend Alexis."
        c "Uhm..."
        scene 10_617 with Dissolve(1)
        mc "If you want to go, go with them."
        mc "We can hang out this afternoon or whenever you're back."
        if Alexis_Sex == True:
            mc "{i}(Maybe that wasn't such a good idea!){/i}"
        else:
            pass
        scene 10_618 with Dissolve(1)
        c "I'd love to go, thanks."
        me "Alright."
        m "Let's all get ready and meet in ten minutes?"
        scene 10_619 with Dissolve(1)
        mc "See you later then. Have fun."
        m "Thank you, we will."
        c "Bye, [mc]."
        scene 10_620 with vpunch
        me "One more thing."
        mc "Wha..."
        if Melissa_Week1_Saturday_Payback == True:
            scene 10_621 with Dissolve(1)
            mc "MELISSA!"
            me "Now we're even."
            mc "Oh, hell no!"
            me "Haha."
        else:
            scene 10_621 with Dissolve(1)
            mc "MELISSA!"
            me "What? Did you slip again?"
            mc "..."
    else:
        scene black with Dissolve(1)
        pause 2
        scene 10_589 with Dissolve(1)
        mc "{i}(This is the best part of this job!){/i}"
        mc "{i}(Relaxing in the pool){/i}"
        if Melissa_Week4_Saturday_Kiss == True:
            mc "{i}(Still can't get the image of Melissa out of my head, though.){/i}"
            mc "{i}(I'm really curious what she was dreaming about. It looked like she was enjoying it.){/i}"
            scene black with Dissolve(1)
            transform moveup:
                xalign 0.5 yalign 1.0
                linear 5.0 yalign 0.0
            show 10_590 at moveup
            pause 3
            ""
            scene 10_591 with Dissolve(1)
            me "..."
            scene 10_592 with vpunch
            me "Sleeping on the job?"
            mc "Aaah... Melissa!"
            me "Haha."
            scene 10_593 with Dissolve(1)
            mc "Damn, you scared me."
            me "This time you were the one dreaming, huh? Was it a good one at least?"
            mc "Uhm..."
            mc "{i}(Yes!){/i}"
            scene 10_594 with Dissolve(1)
            mc "Well, this makes us even again, at least."
            me "Even? Oh, honey. You can't be more wrong. As I said before. You are not prepared!"
            mc "..."
            scene 10_595 with Dissolve(1)
            me "Good luck!"
            mc "{i}(Kiss of death?){/i}"
            scene 10_596 with Dissolve(1)
            me "I'm heading out with your mom. Stay as long as you want."
            mc "Will do, thanks."
            me "And thank you very much for the hard work."
            mc "You're welcome. Have fun."
        else:
            scene 10_596 with Dissolve(1)
            me "Sleeping on the job?"
            mc "Oh... You scared me, Melissa."
            me "Haha, sorry. Thanks for your hard work. I'm heading out with your mom, stay as long as you like."
            mc "Thanks. Have fun."
    scene black with Dissolve(2)
    pause 2
    if Nikki_Girlfriend == True:
        scene 10_622 with Dissolve(1)
        mc "{i}(Not here...){/i}"
        mc "Nikki?"
        ni "I'm in the bathroom. Be right there."
        mc "Take your time. Was just wondering where you were."
        scene 10_623 with Dissolve(1)
        m "Hey. I'm heading out with Melissa now."
        mc "Okay."
        m "Do you need anything?"
        mc "Not really, no."
        scene 10_624 with Dissolve(1)
        m "I won't be back before dinner, so..."
        mc "We'll find something to eat, don't worry."
        m "Okay. See you later."
        mc "Bye."
    else:
        if Cara_Girlfriend == True:
            pass
        else:
            scene 10_623 with Dissolve(1)
            m "Hey. I'm heading out with Melissa now."
            mc "Okay."
            m "Do you need anything?"
            mc "Not really, no."
            scene 10_624 with Dissolve(1)
            m "I won't be back before dinner, so..."
            mc "I'll find something to eat, don't worry."
            m "Okay. See you later."
            mc "Bye."
    jump Week4_Saturday_Layla

label Week4_Saturday_Layla:
    if Layla_End == False:
        scene black with Dissolve(1)
        pause 2
        scene 10_625 with Dissolve(1)
        play sound "Sounds/Phone_Vibrate.mp3"
        n "*Bzzzt. Bzzzt*"
        scene 10_626 with Dissolve(1)
        mc "Hey, Layla."
        la "Hey. How are you?"
        mc "I'm good, you?"
        la "Well, it's spring break. Feeling great!"
        scene 10_627 with Dissolve(1)
        mc "Whatcha doing?"
        la "I'm at Elena's at the moment. She needs to watch her brothers today. I came over to keep her company."
        el "Hey, give it back now. It's your brother's turn!"
        mc "Hehe, I can hear them."
        la "Haha, yeah. They can be very loud."
        scene 10_628 with Dissolve(1)
        la "By the way. Did you hear?"
        mc "Hear what?"
        la "Haven't watched the news yet?"
        mc "No..."
        scene 10_629 with Dissolve(1)
        la "They found a body."
        mc "What? A body? Like a dead person?"
        la "Yeah."
        mc "Where? Close by?"
        la "In the city."
        scene 10_630 with Dissolve(1)
        mc "Oh shit. Who is it?"
        la "A woman. That's all I know."
        la "They haven't disclosed who, or what happened, yet."
        mc "Hmm... I hope not someone we know."
        scene 10_631 with Dissolve(1)
        la "Aaah..."
        ma "Haha."
        el "Mateo!"
        scene 10_632 with Dissolve(1)
        el "You okay?"
        la "It was just water. It's fine."
        ma "Take this!"
        scene 10_633 with Dissolve(1)
        el "Hey!"
        ma "You have a wet butt. Haha."
        el "You little..."
        la "Haha."
        scene 10_634 with Dissolve(1)
        el "I've got him. Now's your chance Diego! Shoot him!"
        ma "Haha. Nooo!"
        scene 10_635 with Dissolve(1)
        el "..."
        scene 10_636 with Dissolve(1)
        el "Are you kidding me! I'm helping you."
        ma "Nice one, Diego!"
        di "Thanks."
        la "Haha."
        el "Dios mío."
        scene 10_637 with Dissolve(1)
        mc "Seems like you guys are having fun over there."
        la "Oh yeah, Elena's having a blast."
        la "What about you? Can you tell me now what you and Zach did yesterday?"
        scene 10_638 with Dissolve(1)
        mc "Nothing."
        la "Nothing?"
        mc "Well, we had a... *Sigh* Never mind. Zach's an idiot."
        la "That's nothing new."
        scene 10_639 with Dissolve(1)
        la "Do you have time on Monday?"
        if Alexis_Dating == True:
            mc "I've made plans with Alexis in the afternoon."
            la "Oh... But you're free in the morning?"
            mc "Hmm, yeah."
            la "Okay, good."
        else:
            mc "I think so, yes."
            la "Okay, good."
        scene 10_640 with Dissolve(1)
        la "I called Valeria before, and she also has time then. We can all go for a run together."
        mc "Thanks for reminding me. I forgot about that, already."
        la "Haha, no problem. So, you're coming?"
        mc "Sure."
        scene 10_641 with Dissolve(1)
        mc "What time?"
        la "I told Val eight thirty?"
        mc "That's fine with me. I'll be there."
        la "Cool."
        if Layla_Dating == True:
            scene 10_642 with Dissolve(1)
            la "And we can go to the beach in the afternoon. Elena has time too, then."
            mc "Awesome. I'll get the Elena surprise ready."
            la "Haha."
            if Elena_Week3_Monday_CheerTraining == True:
                scene 10_643 with Dissolve(1)
                el "Can I talk to him for a second?"
                la "Sure. Elena wants to talk to you. I'll hand her over."
                mc "Alright."
                scene 10_644 with Dissolve(1)
                el "Hey."
                mc "Hi, Elena. I heard you have a wet butt."
                el "*Sigh* Of course, you heard that."
                scene 10_645 with Dissolve(1)
                el "That's your fault, by the way."
                mc "How is it my fault?"
                el "Because you aren't here and they're targeting me!"
                mc "Haha. Probably deserved!"
                el "..."
                scene 10_646 with Dissolve(1)
                el "The boys have been asking for you."
                mc "They have?"
                el "Uh-huh. When is [mc] coming over again to play..."
                mc "Hehe."
                scene 10_647 with Dissolve(1)
                mc "You sure it's the boys asking and not you wanting me to come?"
                el "Trust me. I see you every day at school and that's reaching my limit, already."
                mc "Haha. You always have the nicest things to say to the people you like. I like you too, Elena!"
                el "*Shakes head* Dios mío."
                scene 10_648 with Dissolve(1)
                mc "But I can come by some day next week and spend some time with you... and the boys."
                el "Heh. Thank you! I'll let you know on Monday which days would work."
                mc "Alright."
                el "I'll hand you back to Layla. Bye, [mc]."
                mc "See you on Monday!"
            else:
                pass
        else:
            pass
        scene 10_649 with Dissolve(1)
        ma "Get them!"
        la "Aaah..."
        el "Hey!"
        ma "Haha."
        scene 10_650 with Dissolve(1)
        el "I've had enough. Layla, I need your help."
        la "Sorry, [mc]. We have to take care of something."
        mc "Hehe, I can hear that. Speak to you soon, then. Have fun."
        la "Thanks. Bye."
        if Nikki_Girlfriend == True:
            jump Week4_Saturday_Nikki
        else:
            if Cara_Girlfriend == True:
                jump Week4_Saturday_Cara
            else:
                scene black with Dissolve(2)
                pause 2
                scene 10_1132 with Dissolve(1)
                mc "Oh hey, you're back."
                m "And you're still here? Don't you want to go out with your friends?"
                mc "They were all busy."
                m "Hmm..."
                scene 10_1133 with Dissolve(1)
                m "Well, I've bought you something. Last time you said you couldn't find a certain t-shirt."
                m "So, I got you a new one."
                mc "Oh, thank you."
                m "Can you try it on and see if it fits? I can still exchange it, if not."
                scene 10_1134 with Dissolve(1)
                m "I wasn't too sure about the colours, either."
                mc "Why? You picked something flashy?"
                m "Somewhat, yes. Not what you would usually wear."
                scene 10_1135 with Dissolve(1)
                mc "I like it. Definitely more colourful than the stuff I usually wear."
                mc "Fits perfectly too. What do you think?"
                m "Yes, it looks good on you."
                scene 10_1136 with Dissolve(1)
                mc "Thank you very much, Mom."
                m "You're welcome. Now go play outside. You can't spend your whole break behind your pc."
                mc "Hehe. I'll go find my lego."
                jump Week4_Sunday_Morning
    else:
        $ Valeria_Friends = True
        if Nikki_Girlfriend == True:
            jump Week4_Saturday_Nikki
        else:
            if Cara_Girlfriend == True:
                jump Week4_Saturday_Cara
            else:
                if Erynn_End == True:
                    $ MC_NoFriends = True
                    scene 10_625 with Dissolve(1)
                    mc "{i}(It's finally spring break, but there's nothing to do...){/i}"
                    mc "{i}(Layla and Elena hate me. Zach is a fucking idiot. I screwed things up with Erynn...){/i}"
                    mc "{i}(My friend count is plummeting badly. Who else can I call?){/i}"
                    mc "{i}(Valeria!){/i}"
                    scene 10_626 with Dissolve(1)
                    mc "Hey, Val. How..."
                    va "Layla told me what you did!"
                    scene 10_629 with Dissolve(1)
                    mc "I can explain... I..."
                    mc "..."
                    mc "{i}(She hung up!){/i}"
                    scene 10_651 with Dissolve(1)
                    mc "{i}(That officially brings my friend count to zero...){/i}"
                    mc "{i}(What the fuck am I doing?){/i}"
                else:
                    pass
                scene black with Dissolve(2)
                pause 2
                scene 10_1132 with Dissolve(1)
                mc "Oh hey, you're back."
                m "And you're still here? Don't you want to go out with your friends?"
                mc "They were all busy."
                m "Hmm..."
                scene 10_1133 with Dissolve(1)
                m "Well, I've bought you something. Last time you said you couldn't find a certain t-shirt."
                m "So, I got you a new one."
                mc "Oh, thank you."
                m "Can you try it on and see if it fits? I can still exchange it, if not."
                scene 10_1134 with Dissolve(1)
                m "I wasn't too sure about the colours, either."
                mc "Why? You picked something flashy?"
                m "Somewhat, yes. Not what you would usually wear."
                scene 10_1135 with Dissolve(1)
                mc "I like it. Definitely more colourful than the stuff I usually wear."
                mc "Fits perfectly too. What do you think?"
                m "Yes, it looks good on you."
                scene 10_1136 with Dissolve(1)
                mc "Thank you very much, Mom."
                m "You're welcome. Now go play outside. You can't spend your whole break behind your pc."
                mc "Hehe. I'll go find my lego."
                jump Week4_Sunday_Morning

label Week4_Saturday_Nikki:
    scene black with Dissolve(1)
    pause 2
    stop music fadeout 1.0
    play music ("Music/LoFi Indie 3.mp3", "Music/LoFi Indie 1.mp3", "Music/LoFi Indie 2.mp3") volume 0.2
    scene 10_652 with Dissolve(1)
    ni "Hey. It's been a while since last I heard you play."
    mc "I haven't been playing that much, lately."
    ni "Why not?"
    mc "Because I'm not that good, for starters..."
    scene 10_653 with Dissolve(1)
    ni "You keep saying that, but it's not true. I think it sounds beautiful."
    mc "Heh... You're just being biased."
    ni "When am I biased? If it sucks, I'd tell you it sucks!"
    mc "Haha."
    scene 10_654 with Dissolve(1)
    ""
    scene 10_655 with Dissolve(1)
    mc "What do you want to do today?"
    ni "Let's change it up. Let's do something you want to do."
    mc "I have plenty of time to do stuff next week. It's your last day here, and..."
    ni "No, it's fine. I'm happy with just spending time with you."
    scene 10_656 with Dissolve(1)
    mc "Hmm... Alright."
    if Layla_Week2_Wednesday_Knows == False:
        mc "How about we go to the city and eat something first? I know a good Italian place."
    else:
        mc "There's this Italian place I want to check out."
    ni "Mm-hmm."
    mc "Then we can spend some time at the beach, since you wanted to go again, right?"
    scene 10_657 with Dissolve(1)
    ni "As I said. Pick something you want to do."
    mc "I want to go to the beach!"
    ni "Heh. Okay then."
    scene 10_658 with Dissolve(1)
    mc "And after that maybe go to a club?"
    ni "We can do that. But we can't stay too late. I have a very early flight."
    mc "Right. Okay, scratch the club idea."
    scene 10_659 with Dissolve(1)
    mc "Let's change it to a few cocktails at the beach bar instead?"
    ni "I like that."
    if Nikki_Visit_Points >= 26:
        mc "And once we're home. A little bit of cuddling, obviously."
        ni "Obviously."
        jump Week4_Saturday_Nikki_BJ
    else:
        jump Week4_Saturday_Nikki_Restaurant

label Week4_Saturday_Nikki_BJ:
    scene 10_660 with vpunch
    ni "Aah..."
    mc "But that depends."
    ni "On what?"
    mc "If you're nice Nikki or evil Nikki!"
    ni "Which one will lead to the cuddling?"
    scene 10_661 with Dissolve(1)
    mc "Hah... You'll see tonight!"
    ni "*Evil stare*"
    mc "I see you picked the dark side."
    scene 10_662 with Dissolve(1)
    ni "Haha..."
    scene 10_663 with Dissolve(1)
    mc "I'll get changed then."
    ni "Me too. Skirt or pants?"
    mc "Skirt!"
    ni "Hehe, okay."
    scene 10_664 with Dissolve(1)
    ""
    scene 10_665 with Dissolve(1)
    mc "Should I wear the shirt you got me?"
    ni "That's up to you. Won't it be too warm, since it's long-sleeved?"
    mc "Hmm... You're right."
    scene 10_666 with Dissolve(1)
    mc "..."
    ni "Haha, ew... What are you doing?"
    scene 10_667 with Dissolve(1)
    mc "Ew? When you do it, it's sexy. When I do it, it's ew?"
    ni "I never said it's sexy when I do it. That was you!"
    mc "..."
    scene 10_668 with Dissolve(1)
    ni "You're just gonna stand there now? Naked?"
    mc "Uh-huh. Do you have a problem with that, too?"
    ni "Not at all. I might just..."
    scene 10_669 with Dissolve(1)
    mc "Uh..."
    scene 10_670 with Dissolve(1)
    mc "{i}(This is so unexpected, but so hot!){/i}"
    scene 10_671 with Dissolve(1)
    ""
    scene 10_672 with Dissolve(1)
    ""
    scene 10_673 with Dissolve(1)
    mc "This feels so good, Nikki!"
    show 10_675
    mc "Oh... Fuck..."
    show 10_674
    ""
    scene 10_676 with Dissolve(1)
    mc "Nikki... I'm..."
    scene 10_677 with vpunch
    ""
    scene 10_677 with vpunch
    ""
    scene 10_678 with Dissolve(1)
    mc "Fuck, Nikki. That was amazing."
    scene 10_679 with Dissolve(1)
    mc "Every day has a new surprise, with you."
    ni "Did that count as nice Nikki or evil Nikki?"
    mc "Both!"
    ni "Good."
    scene 10_680 with Dissolve(1)
    mc "Let's get ready and head to the beach?"
    ni "Beach? Aren't we going to that Italian place first?"
    mc "I thought we can skip the restaurant and go straight to the beach, since you've eaten already."
    scene 10_681 with Dissolve(1)
    ni "..."
    mc "I'm kidding!"
    scene 10_682 with vpunch
    mc "Aah-haha... Nikki!"
    mc "It was a joke!"
    mc "Sorry!"
    scene 10_683 with Dissolve(1)
    ni "Aaah..."
    mc "Almost! But I won't make it that easy for you!"
    mc "Ready for a bodyslam?"
    ni "What?"
    scene 10_684 with vpunch
    ni "Haha."
    scene 10_685 with Dissolve(1)
    mc "Are you tapping out?"
    ni "Never!"
    scene 10_686 with Dissolve(1)
    mc "Hey..."
    ni "..."
    mc "{i}(Where did this come from?){/i}"
    scene 10_687 with Dissolve(1)
    mc "{i}(She's so strong. I actually can't get out.){/i}"
    mc "{i}(Fuck!){/i}"
    mc "I give..."
    ni "You tapping out?"
    mc "Yes!"
    scene 10_688 with Dissolve(1)
    ni "Hehe."
    mc "I'm not so sure anymore you were with your dad yesterday."
    mc "I think you secretly took that wrestling class!"
    ni "I just might have."
    scene 10_689 with Dissolve(1)
    ni "..."
    ni "Really? Is this situation...?"
    mc "Haha, sorry... It kinda turned me on. I couldn't help it."
    ni "*Shakes head*"
    ni "I'm not going to suck it again. We're leaving now!"
    scene black with Dissolve(2)
    pause 2
    stop music fadeout 1.0
    play music "Sounds/Street_Traffic.mp3" volume 0.5
    scene 10_690 with Dissolve(1)
    ni "Why are you walking so far away from me?"
    mc "This way I can have a better look at you."
    mc "It's not often you wear skirts, so I'm just enjoying the moment."
    ni "Heh..."
    scene 10_691 with Dissolve(1)
    mc "Better?"
    ni "Much better. Do you like skirts that much?"
    mc "Hmm, not just skirts. Anything that shows off your great body, really."
    ni "Haha."
    scene 10_692 with Dissolve(1)
    mc "You look very pretty!"
    ni "Thank you."
    scene 10_693 with Dissolve(1)
    mc "Is there a reason you normally don't wear skirts?"
    ni "I don't have that many, and I spend most of my day at the gym."
    ni "Ever seen someone in a skirt at the gym?"
    mc "Now that you mention it. No, I don't think I have. Good point."
    scene 10_694 with Dissolve(1)
    mc "Cara has lots of skirts, though. She could probably lend you some."
    ni "They wouldn't fit me. I have a much bigger butt."
    mc "You're right about that."
    scene 10_695 with Dissolve(1)
    ni "Hey!"
    mc "What? You said it. And it's not that it isn't true."
    ni "..."
    scene 10_696 with Dissolve(1)
    n "*Slap*"
    mc "It's a good thing!"
    scene 10_697 with Dissolve(1)
    ni "Are you a boob or a butt person?"
    mc "Uh..."
    menu:
        "Boob":
            scene 10_698 with Dissolve(1)
            mc "I think a boob person."
            mc "I just love to play with them."
            ni "Hmm..."
        "Butt":
            scene 10_698 with Dissolve(1)
            mc "Definitely a butt person!"
            mc "Can't really say why. But it's the first thing I look at."
            ni "Hmm..."
        "Both":
            scene 10_698 with Dissolve(1)
            mc "Honestly I don't know. I would say both, but it also depends on the girl."
            mc "I don't wanna sound mean, but some girls have an amazing butt, but lack in the boob area."
            mc "Others have nice boobs but no ass..."
            scene 10_699 with Dissolve(1)
            mc "And then there's you. You have those amazing boobs."
            mc "Every time I see them, I feel like, I must be a boob person."
            mc "But then I see your butt, and..."
            scene 10_700 with Dissolve(1)
            mc "I just can't decide. I want them both!"
            mc "Don't make me choose, Nikki!"
            ni "Haha. I won't."
    scene 10_701 with Dissolve(1)
    mc "What about you?"
    ni "Is there a female equivalent to the boob or butt person?"
    mc "Good question. No idea actually. Don't girls look at men's butts?"
    ni "We do sometimes. But not as excessively as you do."
    mc "Haha. Fair enough."
    scene 10_702 with Dissolve(1)
    mc "Let's find out, then."
    mc "What was the thing that attracted you to me when you first saw me?"
    mc "Besides me being this handsome, obviously."
    ni "Obviously."
    scene 10_703 with Dissolve(1)
    ni "The first time I saw you was when you came into my room with Cara."
    ni "I immediately noticed your shoulders. They're quite broad. I like that."
    mc "A shoulders-girl..."
    ni "I suppose."
    scene 10_704 with Dissolve(1)
    mc "Feel free to massage my shoulders any time you want. I don't mind at all."
    ni "I bet you don't."
    scene 10_705 with vpunch
    mc "Haha. That's not even close to being a massage!"
    ni "It isn't?"
    ni "Don't you feel what I'm doing?"
    scene 10_706 with Dissolve(1)
    mc "Pressing your boobs against my back is not a massage!"
    ni "In some massages it is! Don't you like it?"
    mc "I didn't say that."
    ni "Haha."
    ni "How about you show me how to massage, then?"
    mc "Uh-huh. Nice try."
    scene 10_707 with Dissolve(1)
    ni "Oh..."
    da "..."
    ni "I'm sorry!"
    scene 10_708 with Dissolve(1)
    $ Darryl_SeeNikkiMC = True
    da "Every time I see this guy, he's with another worldie..."
    tj "He knows how to choose 'em. You gotta give him that."
    da "Yeah, but this one is on a whole nother level. Fuck, she's hot!"
    da "Never seen her before. Know who she is?"
    scene 10_709 with Dissolve(1)
    tj "I think I saw her with Coach at school yesterday."
    da "Mike?"
    tj "Yeah. There were some rumours about him having a daughter. She might be her."
    da "Interesting."
    $ renpy.end_replay()
    jump Week4_Saturday_Nikki_Restaurant

label Week4_Saturday_Nikki_Restaurant:
    scene black with Dissolve(1)
    pause 2
    stop music fadeout 1.0
    play music ("Music/LoFi Italian 1.mp3", "Music/LoFi Italian 2.mp3", "Music/LoFi Italian 3.mp3") volume 0.2
    scene 10_710 with Dissolve(1)
    mc "This is it."
    ni "I would've never found this place by myself."
    if Layla_End == True:
        mc "Yeah, it's a little hidden away. I didn't know it until someone from school showed it to me."
    else:
        mc "Yeah, it's a little hidden away. I didn't know it until a friend from school showed it to me."
    scene 10_711 with Dissolve(1)
    ni "Mmm... I can smell it already. I love Italian food."
    mc "Same. Pasta, pizza, garlic bread, lasagna..."
    ab "Tiramisu!"
    ni "Haha."
    scene 10_712 with Dissolve(1)
    mc "The dessert will be an easy choice."
    ni "Haha. Indeed."
    scene 10_713 with Dissolve(1)
    x "Buongiorno. Here you go."
    ni "Hello. Thank you."
    mc "Hi."
    scene 10_714 with Dissolve(1)
    x "Can I start you off with something to drink?"
    mc "I'll have an iced tea, please."
    ni "A glass of wine, red, please."
    x "Thank you very much."
    scene 10_715 with Dissolve(1)
    if Cara_FB_BikeCity == False:
        mc "Why didn't we ever go to an Italian place? Don't they have one in Riverside?"
        ni "No, we have a few. Bella Ciao and Giovanni's."
        mc "Right, Giovanni's. We ordered pizza from there before."
    else:
        mc "We never went to an Italian place in Riverside, right? I did go with Cara a few times."
        ni "I know... After school, and you never invited me!"
        mc "Yeah. Sorry about that. Making up for it today!"
    scene black with Dissolve(1)
    pause 2
    scene 10_716 with Dissolve(1)
    mc "How's the wine?"
    ni "It's good. Want to try?"
    mc "I have nothing to compare it to. I've never had wine before."
    ni "Never?"
    mc "Not that I know of. Mom uses it for cooking some dishes, but that's the closest I've come to 'drinking' it."
    scene 10_717 with Dissolve(1)
    ni "Here, have a sip."
    mc "You're such a bad influence! Making me drink alcohol."
    ni "Haha. What are the plans again after the restaurant? Something with beach bar and cocktails?"
    scene 10_718 with Dissolve(1)
    mc "Alcohol-free, obviously."
    ni "Obviously."
    ni "Now taste!"
    mc "Si, principessa."
    scene 10_719 with Dissolve(1)
    er "Want to grab some dessert here?"
    a "You can but I don't want anything. I'm still full from brunch."
    scene 10_720 with Dissolve(1)
    mc "..."
    mc "*Cough!*"
    scene 10_721 with Dissolve(1)
    mc "*Cough! Cough!*"
    ni "Are you alright?"
    scene 10_722 with Dissolve(1)
    a "What? Erynn, if you want to..."
    er "No, I just thought I heard someone I know."
    er "That girl has amazing legs by the way."
    a "Says the one with amazing legs..."
    scene 10_723 with Dissolve(1)
    er "Cute couples everywhere."
    a "Yeah..."
    if Alexis_Dating == True:
        er "You can't yeah me. You're in a cute couple yourself!"
        a "Haha."
        scene 10_724 with Dissolve(1)
        er "Are you seeing him later?"
        a "No. We made plans for Monday."
        er "You won't see each other until Monday? Aw..."
        a "Haha, shut up!"
    else:
        pass
    scene 10_725 with Dissolve(1)
    ni "You okay?"
    mc "Yeah, thanks. Got it in the wrong pipe."
    ni "Sorry."
    mc "Wasn't your fault."
    scene black with Dissolve(1)
    pause 2
    scene 10_726 with Dissolve(1)
    ni "That was really good."
    mc "Ready for some dessert?"
    ni "Honestly, I'm so full. I don't think I..."
    mc "You're saying no to tiramisu?"
    scene 10_727 with Dissolve(1)
    ni "Sadly, yes..."
    mc "Alright. Let's get out of here, then."
    ni "Wait. You don't want any? No, just order one if you want one. Don't worry about me."
    if Nikki_Visit_Points >= 22:
        mc "Heh, okay."
        scene black with Dissolve(1)
        pause 2
        scene 10_728 with Dissolve(1)
        mc "Mmm..."
        ni "..."
        mc "So good!"
        scene 10_729 with Dissolve(1)
        ni "Don't do that!"
        mc "Do what? I'm just enjoying my tiramisu."
        mc "I bet you're regretting not getting any, huh?"
        menu:
            "Eat it yourself":
                mc "Well, tough luck. Maybe you'll make a better decision next time!"
                ni "*Shakes head*"
                scene black with Dissolve(1)
                pause 2
                scene 10_737 with Dissolve(1)
                mc "Ready to go?"
                ni "Mm-hmm."
                mc "Do you need to go home first to switch clothes?"
                ni "No, I'm wearing a bikini under my clothes, already."
                mc "Perfect."
            "Share[KoGa3AutoWTChange1]{size=-4}(Nikki Visit Points+2) {/size} {/color}":
                $ Nikki_Visit_Points += 2
                # Nikki Visit (34)
                scene 10_730 with Dissolve(1)
                mc "Want to try it?"
                ni "Yes, please. One scoop."
                ni "One big scoop!"
                mc "Haha."
                scene 10_731 with Dissolve(1)
                mc "Here you go. One big scoop."
                ni "Thank you."
                scene 10_732 with Dissolve(1)
                mc "Mmm... Just so good."
                ni "[mc]! That was my scoop!"
                mc "I like sharing things with you, but I draw the line at tiramisu!"
                ni "..."
                scene 10_733 with Dissolve(1)
                mc "Haha. Hey there. Fancy seeing you here."
                ni "Please? [mc]?"
                mc "Now you're nice Nikki all of a sudden?"
                scene 10_734 with Dissolve(1)
                ni "*Humming*"
                mc "{i}(She always hums when she likes something.){/i}"
                scene black with Dissolve(1)
                pause 2
                scene 10_735 with Dissolve(1)
                ni "Thank you!"
                mc "{i}(One scoop, she said...){/i}"
                mc "{i}(She ate the whole thing by herself.){/i}"
                mc "{i}(It's always the same. Next time, I'll order two to begin with.){/i}"
                scene 10_736 with Dissolve(1)
                mc "Ready to go?"
                ni "Mm-hmm."
                mc "Do you need to go home first to switch clothes?"
                ni "No, I'm wearing a bikini under my clothes, already."
                mc "Perfect."
    else:
        mc "Nah, it's fine."
        scene 10_737 with Dissolve(1)
        mc "Ready to go?"
        ni "Mm-hmm."
        mc "Do you need to go home first to switch clothes?"
        ni "No, I'm wearing a bikini under my clothes, already."
        mc "Perfect."
    scene black with Dissolve(2)
    pause 2
    stop music fadeout 1.0
    play music "Sounds/Ocean.mp3" volume 0.5
    scene 10_738 with Dissolve(1)
    ni "You were right about the beach being very busy today."
    mc "This is still doable. It will be worse next week."
    mc "You probably won't see any sand due to all the towels."
    ni "Really? That bad?"
    scene 10_739 with Dissolve(1)
    mc "And let's not talk about summer..."
    ni "One towel will be mine then."
    mc "Haha. Already made plans for the summer?"
    ni "Yes!"
    scene 10_740 with Dissolve(1)
    mc "Do you have a go-to?"
    ni "Go-to cocktail?"
    mc "Yeah."
    ni "Hmm... Mojito, I think. You?"
    scene 10_741 with Dissolve(1)
    mc "I haven't really tried that many yet. I usually stick to a Cuba libre or Long Island iced tea."
    ni "Are those the ones with cola?"
    mc "Yes."
    ni "I don't like those. Not a fan of cola."
    scene 10_742 with Dissolve(1)
    mc "Let's try a few different ones. Maybe we'll find something else we like."
    ni "Sounds good."
    mc "But before we drink too many. When was your flight again?"
    scene 10_743 with Dissolve(1)
    ni "At eight. So we need to be there around seven-ish."
    mc "Leave home at around six then."
    ni "Our usual time."
    mc "Your usual time! You'll probably need to wake me."
    ni "Haha. Will do."
    scene 10_744 with Dissolve(1)
    bt "Hello."
    mc "Hi."
    bt "What can I getcha?"
    mc "Uhm. Do you have one of those cocktail card menu thingies?"
    bt "Sure. I'll get you one."
    scene 10_745 with Dissolve(1)
    bt "Here you go. One cocktail card menu thingy."
    mc "... Thank you."
    ni "Haha."
    scene 10_746 with Dissolve(1)
    mc "Why are you laughing?"
    ni "No reason."
    mc "I didn't know what to call it."
    ni "I think you explained it perfectly. She got you what you asked for. A cocktail card menu thingy... Haha."
    mc "..."
    scene 10_747 with Dissolve(1)
    mc "Haha. Adios, Motherfucker... Why is that a cocktail? I could've used this one yesterday though."
    ni "Oh, because of that idiot you were talking about?"
    mc "Exactly."
    ni "Are you gonna try it?"
    mc "Yeah."
    scene black with Dissolve(1)
    pause 2
    scene 10_748 with Dissolve(1)
    mc "Cheers."
    ni "Cheers."
    scene 10_749 with Dissolve(1)
    x "Hey Evelyn. Can I have four beers, please?"
    bt "Four?"
    x "Yes. Bottle is fine."
    scene 10_750 with Dissolve(1)
    x "Hey."
    ni "Hi."
    mc "{i}(Seriously? I'm right here...){/i}"
    mc "{i}(Have I seen him before? He looks familiar, somehow...){/i}"
    scene 10_751 with Dissolve(1)
    x "Enjoying your cocktail?"
    ni "We are."
    x "You've gotta try the piña colada. Evelyn makes the best ones."
    ni "Thanks. We'll definitely try it, then."
    scene 10_752 with Dissolve(1)
    bt "Don't scare away my customers."
    x "I'm not. I'm praising your piña coladas."
    x "You know what? Next round is on me."
    mc "Uh, thanks."
    scene 10_753 with Dissolve(1)
    bt "How are the waves?"
    x "A little on the small side, but they're getting there. Next week should be good."
    x "You're always welcome to join us."
    bt "Thanks. I'll see if I can get away for a few hours."
    scene 10_754 with Dissolve(1)
    x "Anyway. Guys, enjoy your cocktails. Evelyn, see you later."
    ni "Thank you!"
    bt "Later."
    scene 10_755 with Dissolve(1)
    mc "..."
    mc "If you want him to turn around, you might try whistling."
    scene 10_756 with Dissolve(1)
    ni "Haha. Can't I look?"
    mc "Of course, you can. I can't fault you. Even I admit he's a good-looking guy."
    ni "..."
    ni "I was actually looking at the surfboards."
    mc "Oh..."
    if Nikki_Visit_Points >= 24:
        scene 10_757 with Dissolve(1)
        ""
    else:
        pass
    scene 10_758 with Dissolve(1)
    ni "Have you surfed before?"
    mc "No. Never."
    ni "How about we take some lessons next time I visit?"
    mc "..."
    scene 10_759 with Dissolve(1)
    ni "No... It's not because of surfer boy. See. I can do the naming thing, too!"
    mc "Haha."
    ni "It's actually something I've always wanted to try."
    mc "Let's do that then, next time you're here."
    ni "But don't cheat and take some lessons on your own."
    mc "I won't. We can fail together."
    scene 10_760 with Dissolve(1)
    mc "They're all looking over here. Probably talking about you."
    ni "Maybe they're looking at you."
    mc "No. I recognise those stares. I've seen them many times."
    if Nikki_Visit_Points >= 24:
        ni "Do you do that, too?"
        mc "When I see you, all the time!"
        scene 10_761 with Dissolve(1)
        ni "Don't ever stop doing that!"
        mc "It's impossible, anyway."
        scene 10_762 with Dissolve(1)
        ""
    else:
        pass
    scene black with Dissolve(1)
    pause 2
    scene 10_763 with Dissolve(1)
    bt "Another round?"
    ni "I'll try your piña colada."
    mc "Mojito, please."
    bt "Alright. I'll put it on their tab."
    ni "Heh, thanks."
    scene 10_764 with Dissolve(1)
    mc "I guess surfer boy was right. Seems like you're really enjoying that one."
    ni "I found my new favourite!"
    mc "Oh, it's that good?"
    ni "Mm-hmm!"
    scene 10_765 with Dissolve(1)
    ni "I'm sticking with this one for today. I don't think I'll find another one I like this much."
    mc "Not even this mojito?"
    ni "Here, have a try and see for yourself!"
    scene black with Dissolve(1)
    pause 2
    scene 10_766 with Dissolve(1)
    ni "Okay, what's her deal?"
    mc "Hmm?"
    ni "I thought I was imagining it at first, but that girl has been staring at you for a while now."
    mc "Who?"
    ni "Straight across from us."
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 10_767 at moveup
    pause 3
    mc "Oh..."
    ni "You know her?"
    scene 10_768 with Dissolve(1)
    mc "She was at training camp with us last week. Don't know from which school, though. She probably recognises me since she kicked a ball in my face."
    ni "She did what?"
    mc "Yeah, I don't know if it was on purpose or an accident. But whatever, it was just one of those beach balls."
    mc "Man... What was her name again? Sha... Sha-Sha..."
    scene 10_769 with Dissolve(1)
    ni "Chachacha? Like the dance?"
    mc "Haha, no. Sha'Carri...? Maybe? Or something like that. Anyway, she won the 100- and 200-meter races."
    ni "She must be really good, then."
    mc "Yeah. She annihilated the girls from my school. Wasn't close at all. Number one in the country."
    ni "Wow..."
    scene 10_770 with Dissolve(1)
    ni "She looks like the female version of you."
    mc "Heh? That's how you picture me as a girl?"
    ni "Sort of, yes. She's pretty. You both do track and field. The tattoos. She might be mixed too."
    mc "I would have bigger boobs though, if I was a girl."
    ni "Haha..."
    scene black with Dissolve(1)
    pause 2
    scene 10_771 with Dissolve(1)
    ni "It's hotter today than Thursday, right?"
    mc "A degree or two, maybe. But we've also just eaten and we're drinking alcohol."
    ni "That might be it. I think I'll slow down with the cocktails. It's only three o'clock, and I'm feeling a little tipsy already."
    mc "You can also jump in the ocean if you need to cool off."
    ni "Maybe later. I'm good for now."
    if Nikki_Visit_Points >= 22:
        menu:
            "Cool her off[KoGa3AutoWTChange1]{size=-4}(Nikki Week4 Saturday Icecubes, Nikki Visit Points+2) {/size} {/color}":
                $ Nikki_Week4_Saturday_Icecubes = True
                $ Nikki_Visit_Points += 2
                # Nikki Visit (36)
                if Nikki_Visit_Points >= 28:
                    jump Week4_Saturday_Nikki_CoolOff
                else:
                    scene 10_772 with Dissolve(1)
                    mc "I have another idea that will cool you down a bit."
                    ni "Do you?"
                    scene 10_773 with Dissolve(1)
                    ni "..."
                    scene 10_774 with Dissolve(1)
                    mc "Does it help?"
                    ni "Mmm... It feels really nice."
                    jump Week4_Saturday_Nikki_Cocktail
            "Don't":
                jump Week4_Saturday_Nikki_Cocktail
    else:
        jump Week4_Saturday_Nikki_Cocktail

label Week4_Saturday_Nikki_CoolOff:
    scene 10_772 with Dissolve(1)
    mc "I have another idea that will cool you down a bit."
    ni "Do you?"
    scene 10_773 with Dissolve(1)
    ni "..."
    scene 10_774 with Dissolve(1)
    mc "Does it help?"
    ni "Mmm... It feels really nice."
    scene 10_775 with Dissolve(1)
    ni "Keep going!"
    scene 10_776 with Dissolve(1)
    ni "..."
    scene 10_777 with Dissolve(1)
    ""
    scene 10_778 with Dissolve(1)
    mc "{i}(She's not pushing me away.){/i}"
    scene 10_779 with Dissolve(1)
    mc "{i}(Let's see if I can take it even further.){/i}"
    scene 10_780 with Dissolve(1)
    ni "..."
    scene 10_781 with Dissolve(1)
    mc "{i}(She's really enjoying this...){/i}"
    scene 10_782 with Dissolve(1)
    mc "I think that's enough for now. Can't have people getting suspicious."
    ni "*Nods*"
    scene 10_783 with Dissolve(1)
    ni "[mc]!"
    scene 10_784 with Dissolve(1)
    mc "I had to get rid of the evidence!"
    mc "Tastes great though. A Nikki colada!"
    ni "*Shakes head*"
    scene 10_785 with Dissolve(1)
    ""
    scene 10_786 with Dissolve(1)
    mc "Thief!"
    ni "Haha."
    scene 10_787 with Dissolve(1)
    mc "That's mine! Give it back!"
    ni "Make me!"
    scene 10_788 with Dissolve(1)
    mc "If you think this tree will save you, you're mistaken!"
    ni "I think it does its job perfectly."
    mc "And that is?"
    ni "Wasting precious time!"
    mc "..."
    scene 10_789 with Dissolve(1)
    mc "Gotcha!"
    ni "Haha. You're too late!"
    mc "What?"
    scene 10_790 with Dissolve(1)
    mc "Nooo!"
    scene 10_791 with Dissolve(1)
    ni "Sorry..."
    scene 10_792 with Dissolve(1)
    ni "We can always make a new one."
    if Nikki_FB_PureEvil == False:
        mc "I knew you liked it! You have a little kinky side..."
    else:
        mc "I knew you liked it! Evil Nikki has a little kinky side..."
    mc "Can I have a little taste from the source?"
    scene 10_793 with Dissolve(1)
    ni "..."
    ni "Let's go behind the tree."
    scene 10_794 with Dissolve(1)
    mc "Your nipples are so perfect!"
    ni "Go ahead and taste 'em then!"
    scene 10_795 with Dissolve(1)
    ni "Mmm..."
    scene 10_796 with Dissolve(1)
    ni "Ah..."
    ni "You're sucking really hard on them..."
    scene 10_797 with Dissolve(1)
    ""
    scene 10_798 with Dissolve(1)
    ni "*Whispers* [mc]! Stop-stop-stop!"
    mc "..."
    ni "*Whispers* Someone is coming."
    scene 10_799 with Dissolve(1)
    ni "Hello."
    x "Ah, young love... So beautiful."
    scene 10_800 with Dissolve(1)
    x "You have some nice titties, missy!"
    ni "Uh... Thank you."
    x "She's a keeper, son!"
    scene 10_801 with Dissolve(1)
    mc "..."
    ni "..."
    scene 10_802 with Dissolve(1)
    ni "Haha."
    mc "Haha."
    ni "That was so random."
    mc "He was right though. You have nice titties, missy!"
    ni "Haha, thanks."
    scene 10_803 with Dissolve(1)
    ni "I think I need another cocktail after this."
    mc "Or two. Back to the bar?"
    ni "Yes."
    scene 10_804 with Dissolve(1)
    mc "By the way. You having nice titties wasn't the only thing he was right about."
    ni "Hmm?"
    mc "Also, you being a keeper!"
    ni "..."
    scene 10_805 with vpunch
    mc "Haha. Careful!"
    scene 10_806 with Dissolve(1)
    ni "So are you!"
    scene 10_807 with Dissolve(1)
    mc "I guess you're going for another piña colada?"
    ni "Uh-huh. What will you take?"
    mc "Sex on the beach!"
    ni "Haha. Maybe it won't be just a cocktail next time."
    mc "{i}(Damn, I love this girl...){/i}"
    scene 10_808 with Dissolve(1)
    mc "Hey, can we get another piña colada and a sex on the beach, please."
    bt "Sure."
    mc "Oh, and some extra ice if possible."
    ni "Haha, idiot."
    $ renpy.end_replay()
    jump Week4_Saturday_Nikki_Cocktail

label Week4_Saturday_Nikki_Cocktail:
    scene black with Dissolve(1)
    pause 2
    scene 10_809 with Dissolve(1)
    mc "Drunk?"
    ni "I'm very close... No, scratch that. I think I actually am."
    ni "I didn't want to drink that much, but the cocktails tasted so good. Let's not do this on the last day, next time."
    mc "Haha."
    scene 10_810 with Dissolve(1)
    mc "I'll call an Uber, because I won't be able to carry you all the way home."
    ni "Thank you."
    scene black with Dissolve(2)
    pause 2
    stop music fadeout 1.0
    play music ("Music/LoFi Indie 3.mp3", "Music/LoFi Indie 1.mp3", "Music/LoFi Indie 2.mp3") volume 0.2
    scene 10_811 with vpunch
    ni "Haah... This is nice!"
    scene 10_812 with Dissolve(1)
    mc "Did you enjoy yourself today?"
    ni "It was perfect! Thank you, [mc]."
    ni "I couldn't have a better last day here."
    scene 10_813 with Dissolve(1)
    ni "Come! Join me!"
    if Nikki_Visit_Points >= 24:
        menu:
            "Go to bed[KoGa3AutoWTChange1]{size=-4}(Nikki Visit Points-8) {/size} {/color}":
                $ Nikki_Visit_Points -= 8
                scene 10_814 with Dissolve(1)
                mc "I think we should just go to bed."
                mc "We actually drank more than we wanted to, and we need..."
                scene 10_815 with Dissolve(1)
                ni "..."
                mc "Nikki?"
                ni "Bathroom!"
                scene 10_816 with Dissolve(1)
                ni "*Puking*"
                mc "Let it all out. You'll feel better afterwards."
                scene 10_817 with Dissolve(1)
                ni "I didn't even drink that much."
                mc "Maybe it's the combination of the wine, the cocktails, the heat..."
                scene 10_818 with Dissolve(1)
                ni "Do you have mouthwash or something?"
                mc "Mom has some. I'll get it for you."
                ni "Thank you."
                scene 10_819 with Dissolve(1)
                mc "Here you go."
                ni "Thanks."
                mc "Feeling better?"
                ni "I am."
                scene 10_820 with Dissolve(1)
                ni "I think I'm gonna take a shower, too. I'm feeling dirty."
                mc "Alright. If you need anything, you know where I am."
                ni "Thank you. And thank you for helping me."
                mc "Of course."
                scene 10_821 with Dissolve(1)
                ni "Good night, [mc]."
                mc "Night, Nikki. See you tomorrow."
                mc "Oh and wake me if I'm not up on time."
                ni "Will do."
                jump Week4_Sunday_Morning_Nikki
            "Join her[KoGa3AutoWTChange1]{size=-4}(Nikki Week4 Saturday Bed) {/size} {/color}":
                $ Nikki_Week4_Saturday_Bed = True
                jump Week4_Saturday_Nikki_Sex
    else:
        scene 10_814 with Dissolve(1)
        mc "I think we should just go to bed."
        mc "We actually drank more than we wanted to, and we need..."
        scene 10_815 with Dissolve(1)
        ni "..."
        mc "Nikki?"
        ni "Bathroom!"
        scene 10_816 with Dissolve(1)
        ni "*Puking*"
        mc "Let it all out. You'll feel better afterwards."
        scene 10_817 with Dissolve(1)
        ni "I didn't even drink that much."
        mc "I wasn't a little either. Maybe it's the combination of the wine, the cocktails, the heat..."
        scene 10_818 with Dissolve(1)
        ni "Do you have mouthwash or something?"
        mc "Mom has some. I'll get it for you."
        ni "Thank you."
        scene 10_819 with Dissolve(1)
        mc "Here you go."
        ni "Thanks."
        mc "Feeling better?"
        ni "I am."
        scene 10_820 with Dissolve(1)
        ni "I think I'm gonna take a shower, too. I'm feeling dirty."
        mc "Alright. If you need anything, you know where I am."
        ni "Thank you. And thank you for helping me."
        mc "Of course."
        scene 10_821 with Dissolve(1)
        ni "Good night, [mc]."
        mc "Night, Nikki. See you tomorrow."
        mc "Oh and wake me if I'm not up on time."
        ni "Will do."
        jump Week4_Sunday_Morning_Nikki

label Week4_Saturday_Nikki_Sex:
    if _in_replay:
        $ SexCounter_Nikki = 5
        $ MC_SexCounter = 5
    $ SexCounter_Nikki += 1
    $ MC_SexCounter += 1
    scene 10_822 with Dissolve(1)
    ni "*Sigh* Today went by so fast. All the days were fast, but this one especially. Can't believe I'm leaving tomorrow."
    mc "Maybe we shouldn't spend so much time together, then."
    ni "Haha. No!"
    mc "Well, the day isn't over yet. We still have some time."
    scene 10_823 with Dissolve(1)
    ni "Are you tired?"
    mc "Not really. You?"
    ni "A little. But I have a six-hour flight tomorrow where I can sleep."
    scene 10_824 with Dissolve(1)
    mc "I planned the first part of the day. How about you plan the rest?"
    ni "Hmm... Okay. I might have an idea."
    mc "That was quick! What should I do?"
    ni "Go stand over there."
    scene 10_825 with Dissolve(1)
    mc "Here?"
    ni "Uh-huh. Now turn around!"
    mc "What are you planning?"
    ni "Turn around!"
    scene black with Dissolve(1)
    pause 2
    scene 10_826 with Dissolve(1)
    ni "Hey!"
    mc "Hi. I remember this!"
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 10_827 at moveup
    pause 3
    mc "Damn you're gorgeous!"
    mc "But no panties this time, huh?"
    ni "No. We won't just cuddle this time either!"
    scene 10_828 with Dissolve(1)
    ni "How about we continue with what we started at the beach?"
    mc "I like that idea."
    scene 10_829 with Dissolve(1)
    ""
    scene 10_830 with Dissolve(1)
    ""
    scene 10_831 with Dissolve(1)
    mc "I don't have a tree in this room..."
    ni "Time to improvise!"
    scene 10_832 with vpunch
    ni "Aah-haha..."
    scene 10_833 with Dissolve(1)
    ni "I guess this works."
    scene 10_834 with Dissolve(1)
    ""
    scene 10_835 with Dissolve(1)
    ""
    scene 10_836 with Dissolve(1)
    ni "Ahh..."
    scene 10_837 with Dissolve(1)
    ni "Fuck me!"
    show 10_838
    ""
    show 10_839
    ""
    show 10_840
    ""
    scene 10_841 with vpunch
    ni "Aaah..."
    mc "Too rough?"
    ni "No, keep going!"
    scene 10_842 with Dissolve(1)
    mc "{i}(Her nipples are going to be so sore tomorrow.){/i}"
    show 10_843
    ""
    show 10_844
    ""
    show 10_845
    ""
    scene 10_846 with Dissolve(1)
    ni "[mc]! Are you..."
    ni "*Moaning*"
    ni "Because... I... Am..."
    menu:
        "Pull out":
            scene 10_847 with vpunch
            mc "Ahh..."
        "Cum inside her[KoGa3AutoWTChange1]{size=-4}(Nikki Week4 Saturday Sex Inside) {/size} {/color}":
            $ Nikki_Week4_Saturday_Sex_Inside = True
            scene 10_848 with vpunch
            pause 2
            scene 10_848 with vpunch
            ni "Nggh..."
    scene black with Dissolve(1)
    pause 2
    scene 10_849 with Dissolve(1)
    ni "*Heavy breathing*"
    ni "Haah... That... Was..."
    mc "Amazing!"
    ni "Yes! Perfect workout!"
    mc "Haha."
    scene 10_850 with Dissolve(1)
    ni "..."
    mc "Nikki? You okay?"
    ni "Bathroom!"
    scene 10_851 with Dissolve(1)
    ni "*Puking*"
    mc "Let it all out. You'll feel better afterwards."
    scene 10_852 with Dissolve(1)
    ni "I didn't even drink that much."
    mc "It wasn't a little either. Maybe it's the combination of the wine, the cocktails, and the heat..."
    scene 10_853 with Dissolve(1)
    ni "Do you have mouthwash or something?"
    mc "Mom has some. I'll get it for you."
    ni "Thank you."
    scene 10_854 with Dissolve(1)
    mc "Here you go."
    ni "Thanks."
    mc "Feeling better?"
    ni "I am."
    scene 10_855 with Dissolve(1)
    ni "I think I'm gonna take a shower."
    mc "That's a good idea."
    scene 10_856 with Dissolve(1)
    ni "Thank you for helping me, [mc]."
    mc "Of course. Can I..."
    mc "I'll be in my room..."
    ni "..."
    scene 10_857 with Dissolve(1)
    ni "Want to join me?"
    mc "Yes! I hoped you'd ask. I was scared to do it myself."
    ni "Haha. I know."
    $ renpy.end_replay()
    jump Week4_Sunday_Morning_Nikki

label Week4_Saturday_Cara:
    scene black with Dissolve(2)
    pause 2
    scene 10_858 with Dissolve(1)
    ""
    scene 10_859 with Dissolve(1)
    c "Hey."
    mc "... Oh hey. You're back. I had to look twice before I realised it was you."
    mc "I have to get used to the new hair."
    c "Hehe."
    if Erynn_End == True:
        $ Cara_Visit_Points -= 2
        scene 10_860 with Dissolve(1)
        mc "How was it? Did you have fun?"
        c "It was fun, but a little awkward. Don't you and Erynn get along?"
        mc "Hmm... Not anymore, no."
        c "Why didn't you tell me? I wouldn't have gone if I had known."
        mc "I'm sorry."
        c "It's fine."
    else:
        scene 10_861 with Dissolve(1)
        mc "How was it? Did you have fun?"
        c "It was really fun. Erynn is so cool."
        mc "Heh. She can be."
        c "Alexis too. They're both so pretty."
    scene 10_862 with Dissolve(1)
    mc "What did you guys do?"
    c "We had brunch first and talked a bit."
    c "Then we went to some clothing stores. They have really good boutiques in the city."
    mc "I wouldn't know. Did you get anything?"
    c "No. Mom would kill me if I spent even more. That dress was already over my limit."
    scene 10_863 with Dissolve(1)
    c "What did you do?"
    mc "Not much. Played some guitar and video games."
    c "The usual."
    mc "Exactly."
    scene 10_864 with Dissolve(1)
    mc "Do you still want to go out, or did you have enough for today?"
    c "No, we can go out. Have something in mind?"
    mc "I was thinking about getting Mom's car keys, so we can go for another practice drive, if you want to."
    scene 10_865 with Dissolve(1)
    c "YES!"
    mc "Haha, okay."
    c "Thank you, [mc]!"
    scene 10_866 with Dissolve(1)
    mc "Let's go then."
    c "Give me a minute. I want to change first."
    mc "Alright."
    scene black with Dissolve(1)
    pause 2
    scene 10_867 with Dissolve(1)
    mc "..."
    mc "{i}(How long does it take to change clothes? Typical Cara...){/i}"
    mc "{i}(Should I go check up on her?){/i}"
    menu:
        "Wait for her":
            scene 10_868 with Dissolve(1)
            mc "{i}(I'll wait a bit longer.){/i}"
            mc "{i}(She must be ready any second now, anyway.){/i}"
            mc "{i}(I hope...){/i}"
            scene 10_869 with Dissolve(1)
            c "I'm ready."
            mc "..."
            mc "Why did you change, anyway? You're basically wearing the same. Hot pants and a top."
            c "Hehe, sorry."
            scene black with Dissolve(1)
            transform moveup:
                xalign 0.5 yalign 1.0
                linear 5.0 yalign 0.0
            show 10_870 at moveup
            pause 3
            mc "You look cute though."
            c "Thank you."
            jump Week4_Saturday_Cara_Car
        "Check up on her[KoGa3AutoWTChange1]{size=-4}(Cara Visit Points+4) {/size} {/color}":
            $ Cara_Visit_Points += 4
            # Cara Visit (34)
            jump Week4_Saturday_Cara_Bathroom

label Week4_Saturday_Cara_Bathroom:
    if _in_replay:
        $ Cara_Visit_Points = 34
        $ Cara_Week4_Friday_LickAss = True
    scene 10_871 with Dissolve(1)
    mc "..."
    mc "{i}(She's not even close to being ready.){/i}"
    mc "{i}(What is she doing?){/i}"
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 10_872 at moveup
    pause 3
    mc "{i}(Cute...){/i}"
    mc "Are you checking yourself out?"
    scene 10_873 with vpunch
    c "[mc]!"
    mc "Haha, sorry."
    c "What are you doing here?"
    mc "Just seeing what was taking you so long."
    scene 10_874 with Dissolve(1)
    c "..."
    mc "So?"
    c "I wasn't checking myself out..."
    mc "No?"
    scene 10_875 with Dissolve(1)
    c "I was just looking at my hair."
    c "I didn't have time yet to properly look at it."
    mc "And what do you think?"
    c "I like it! A lot!"
    if Cara_Visit_Points >= 22:
        scene 10_876 with Dissolve(1)
        mc "Me too. You look sexy."
        mc "If I were you, I'd be checking myself out, too!"
        c "I wasn't!"
        scene 10_877 with Dissolve(1)
        mc "Very sexy!"
        c "..."
        scene 10_878 with Dissolve(1)
        ""
        scene 10_879 with Dissolve(1)
        c "What do you think you're doing?"
        mc "I'm helping you change!"
        scene 10_880 with Dissolve(1)
        c "I wasn't going to change my underwear!"
        mc "Now you are."
        scene 10_881 with Dissolve(1)
        mc "{i}(That peachy ass again...){/i}"
        mc "{i}(I just have to!){/i}"
        scene 10_882 with Dissolve(1)
        c "Ah... [mc]..."
        scene 10_883 with Dissolve(1)
        ""
        scene 10_884 with Dissolve(1)
        ""
        if Cara_Week4_Friday_LickAss == True:
            scene 10_885 with Dissolve(1)
            mc "{i}(Should I lick her ass again?){/i}"
            mc "{i}(I think she enjoyed it yesterday.){/i}"
            menu:
                "Lick her ass[KoGa3AutoWTChange1]{size=-4}(Cara Week4 Saturday LickAss) {/size} {/color}":
                    $ Cara_Week4_Saturday_LickAss = True
                    scene 10_886 with Dissolve(1)
                    c "..."
                    scene 10_887 with Dissolve(1)
                    c "*Moaning*"
                    scene 10_888 with Dissolve(1)
                    ""
                "Continue":
                    scene 10_886 with Dissolve(1)
                    c "..."
                    scene 10_887 with Dissolve(1)
                    c "*Moaning*"
        else:
            scene 10_886 with Dissolve(1)
            c "..."
            scene 10_887 with Dissolve(1)
            c "*Moaning*"
        scene 10_889 with Dissolve(1)
        ""
        scene black with Dissolve(1)
        pause 2
        scene 10_890 with Dissolve(1)
        mc "You're really enjoying that, huh?"
        c "*Nods*"
        mc "I'll let you finish changing now, or else we won't get anywhere today."
        c "Hehe."
        scene 10_891 with Dissolve(1)
        ""
    else:
        scene 10_876 with Dissolve(1)
        mc "Do you need much longer or...?"
        c "No. Give me five minutes."
        mc "Alright."
    scene black with Dissolve(1)
    pause 2
    scene 10_869 with Dissolve(1)
    c "I'm ready."
    mc "..."
    mc "Why did you change anyway? You're basically wearing the same. Hot pants and a top."
    c "Hehe, sorry."
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 10_870 at moveup
    pause 3
    mc "You look cute though."
    c "Thank you."
    $ renpy.end_replay()
    jump Week4_Saturday_Cara_Car

label Week4_Saturday_Cara_Car:
    scene 10_892 with Dissolve(1)
    mc "Let's go then."
    c "Do you know a place where there aren't any cars around?"
    mc "Since it's spring break. The parking lot at the MSU campus will be empty. Plenty of space."
    c "Oh, the university..."
    scene 10_893 with Dissolve(1)
    c "This car looks similar to Mom's."
    mc "It's the same car!"
    scene 10_894 with Dissolve(1)
    c "That will make it easier. But you still have to show me again what I have to do."
    mc "Don't worry, it's like riding a bike."
    scene 10_895 with Dissolve(1)
    c "Emily doesn't mind that I'll be driving her car?"
    mc "She doesn't know."
    c "[mc]!"
    mc "If you won't tell, I won't either. So, it's fine."
    c "..."
    scene 10_896 with Dissolve(1)
    c "But what if I hit something or scratch the car... She..."
    mc "You won't. Just like last time. It's an empty car lot. Nothing to hit or scratch."
    mc "Now put your seat belt on."
    scene black with Dissolve(1)
    pause 2
    stop music fadeout 1.0
    play music ("Music/LoFi Upbeat 1.mp3", "Music/LoFi Upbeat 2.mp3", "Music/LoFi Upbeat 3.mp3", "Music/LoFi Upbeat 4.mp3") volume 0.2
    scene 10_897 with Dissolve(1)
    mc "See! No one here."
    c "Will you be going to MSU next year?"
    mc "Most likely. But it will also depend if I get a scholarship."
    scene 10_898 with Dissolve(1)
    mc "Have you made a decision yet what you're going to do after this year?"
    c "I want to go to college, but where is the question."
    mc "You can always come here. Your dad lives here too, which helps."
    c "Hmm... Maybe. I guess I'll have to start looking at some campuses soon and see what they're offering."
    if Erynn_End == True:
        pass
    else:
        scene 10_899 with Dissolve(1)
        c "Erynn and Alexis go here too, right?"
        mc "They do, yes. Maybe they can show you around, next time you're visiting."
        c "That'd be cool."
    scene 10_900 with Dissolve(1)
    mc "Anyway. Let's talk about colleges later. Time to do some driving."
    c "Heh, okay."
    c "But show me the stick thingy first again."
    mc "Haha. The stick thingy."
    scene black with Dissolve(1)
    pause 2
    scene 10_901 with Dissolve(1)
    mc "You're getting the hang of it. Doing really good!"
    c "Thank you."
    scene 10_902 with Dissolve(1)
    mc "{i}(What's this idiot doing here?){/i}"
    c "Looks like we're not alone anymore. They must have had the same idea."
    mc "I don't think they're here for driving lessons..."
    mc "{i}(Just stay out of our way!){/i}"
    scene 10_903 with Dissolve(1)
    mc "{i}(A little close there, buddy...){/i}"
    mc "{i}(Seriously... This parking lot is big enough. No need to doughnut around us.){/i}"
    scene 10_904 with Dissolve(1)
    c "Aaah..."
    scene 10_905 with Dissolve(1)
    mc "What the fuck is he doing!"
    mc "Brake!"
    scene 10_906 with Dissolve(1)
    mc "Cara, BRAKE!"
    play sound "Sounds/CarBrake.mp3" volume 0.8
    scene 10_907 with vpunch
    mc "{i}(Fuck! That was close.){/i}"
    scene 10_908 with Dissolve(1)
    mc "Are you okay?"
    c "..."
    mc "Cara?"
    mc "Give me a second. Stay in the car."
    c "*Nods*"
    scene 10_909 with Dissolve(1)
    mc "What the fuck was that? There's plenty of space here. No need to frickin' drift around us."
    x "How about you tell your girlfriend to learn how to drive!"
    mc "What do you think we're doing here, dipshit!"
    mc "Get the fuck outta here if you want Daddy's car to keep looking like that."
    x "Heh... Whatever, dude."
    scene 10_910 with Dissolve(1)
    x "Fuck you, loser!"
    mc "..."
    mc "Yeah, fuck you, too!"
    scene 10_911 with Dissolve(1)
    mc "Sorry... Are you okay, Cara?"
    c "I... I panicked... I didn't know what to do..."
    c "I..."
    scene 10_912 with Dissolve(1)
    c "*Crying*"
    mc "This wasn't your fault. You did good! Sorry, I yelled at you."
    scene 10_913 with Dissolve(1)
    ""
    scene 10_914 with Dissolve(1)
    mc "Shall we leave?"
    c "Yeah. I don't want to drive anymore."
    scene 10_915 with Dissolve(1)
    mc "Want to go home, or...?"
    c "No. Let's just do something else."
    mc "Can I grab a snack somewhere quickly? I'm a little hungry."
    c "Haha, You're always hungry."
    scene black with Dissolve(1)
    pause 2
    stop music fadeout 1.0
    play music "Sounds/Park.mp3" volume 0.5
    scene 10_916 with Dissolve(1)
    mc "Want a bite?"
    c "*Shakes head*"
    mc "Haha. What's with that face? Don't you like hot dogs?"
    c "No."
    scene 10_917 with Dissolve(1)
    mc "No?"
    c "Well, I've never had one before."
    mc "Have a try. Maybe you'll like it."
    c "It looks so fatty. And just the smell and the mustard... No!"
    mc "Haha."
    scene 10_918 with Dissolve(1)
    c "..."
    mc "What now? Never seen anyone eat a hot dog either?"
    c "*Shakes head*"
    mc "You're so weird."
    scene 10_919 with Dissolve(1)
    c "No, it's not that."
    c "There's a girl... Lying there... Top... Topless..."
    mc "{i}(Topless? In a park?){/i}"
    mc "{i}(Don't tell me it's...){/i}"
    scene 10_920 with Dissolve(1)
    mc "{i}(Iris!){/i}"
    mc "{i}(She still does this, huh? And why a park? We have a beach here. Looking amazing though...){/i}"
    mc "{i}(We aren't together anymore, and I've moved on, but I still don't like that other people might see her like that...){/i}"
    scene 10_921 with Dissolve(1)
    c "Let's quickly leave before she notices us watching."
    mc "You don't want to watch? She probably wouldn't mind."
    c "[mc]! No!"
    scene 10_922 with Dissolve(1)
    c "Come on!"
    mc "I can't watch, either?"
    c "No!"
    scene 10_923 with Dissolve(1)
    c "Come!"
    mc "Haha."
    ir "..."
    scene black with Dissolve(1)
    pause 2
    scene 10_924 with Dissolve(1)
    c "Why would she lie here anyway? Isn't she scared she'll be seen?"
    mc "Maybe she's waiting for a guy to take a picture of her. So she then can use him to go shopping with her and carry all her bags."
    c "Haha. You have such a vivid imagination. You should write a story."
    mc "Maybe I will."
    scene 10_925 with Dissolve(1)
    c "She's brave, though. I would never dare to do that."
    mc "You sure? You're undressing already."
    c "..."
    c "I'm just taking off my jacket. It's really hot today."
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 10_926 at moveup
    pause 3
    mc "{i}(What a cutie...){/i}"
    scene 10_927 with Dissolve(1)
    c "Why are you staring like that?"
    mc "Just looking at your hair. Still getting used to it."
    mc "It's really pretty."
    c "Thank you."
    scene 10_928 with Dissolve(1)
    mc "I wonder what your mom and Nikki will say once they see it."
    c "They liked it."
    mc "Oh, they saw it already?"
    c "Yeah. I sent a picture earlier."
    scene 10_929 with Dissolve(1)
    mc "Did you also tell them about your dad? Him living here."
    c "No, not yet. I'll do that once I'm back. A short version."
    c "He said he'll visit us sometime next week."
    scene 10_930 with Dissolve(1)
    mc "A little family vacation."
    c "For him, yes. I have to be in school again on Monday."
    mc "Ah right. Your spring break was this week. So happy mine just started."
    c "Just rub it in..."
    mc "Haha."
    scene 10_931 with Dissolve(1)
    c "Look who's undressing now."
    mc "Haha, you were right. It is hot today!"
    scene 10_932 with Dissolve(1)
    mc "How are you feeling about earlier?"
    c "It was scary, but I'm good now."
    mc "I'm sorry. I hope this doesn't discourage you from wanting to drive."
    c "No. It made me realise, though, that I have to take more driving lessons."
    menu:
        "Kiss her[KoGa3AutoWTChange1]{size=-4}(Cara Visit Points+2) {/size} {/color}":
            $ Cara_Visit_Points += 2
            # Cara Visit (36)
            if Cara_Visit_Points >= 24:
                jump Week4_Saturday_Cara_Park_Kiss
            else:
                scene 10_933 with Dissolve(1)
                ""
                jump Week4_Saturday_Cara_Park
        "Don't":
            jump Week4_Saturday_Cara_Park

label Week4_Saturday_Cara_Park_Kiss:
    scene 10_934 with Dissolve(1)
    ""
    scene 10_935 with Dissolve(1)
    c "Do you think that girl is still there?"
    mc "I don't know. Maybe. Why? Do you want to have another look?"
    c "No..."
    scene 10_936 with Dissolve(1)
    mc "Do you want me to go look?"
    c "No!"
    mc "I don't mind. Really. I'll do it for you!"
    c "Haha. No, [mc]!"
    scene 10_937 with Dissolve(1)
    mc "Have I told you already that you look really pretty?"
    c "No."
    mc "Liar!"
    scene 10_938 with Dissolve(1)
    c "Aaah..."
    mc "That's what you get for lying!"
    c "Haha."
    scene 10_939 with Dissolve(1)
    ""
    scene 10_940 with Dissolve(1)
    c "[mc]..."
    mc "What?"
    c "Did you hear that?"
    mc "I didn't."
    scene 10_941 with Dissolve(1)
    mc "There's no one here."
    mc "Maybe it's the girl from earlier, and she's watching us now."
    c "..."
    c "Nooo... That's creepy!"
    mc "Haha."
    scene 10_942 with vpunch
    c "Aaah..."
    mc "Or maybe it's a hungry bear who sees this sweet honey here and..."
    c "Haha. That's so bad!"
    scene 10_943 with Dissolve(1)
    c "There are no bears here, right?"
    mc "Haha, Cara. No, there aren't."
    mc "But there are spiders though."
    scene 10_944 with Dissolve(1)
    c "Hmm?"
    scene 10_945 with Dissolve(1)
    c "Oh wow. This one is really pretty. Look!"
    mc "..."
    mc "That was not what I expected to happen..."
    scene 10_946 with Dissolve(1)
    c "You thought I would be afraid of spiders and scream?"
    mc "Sort of, yeah."
    mc "I'm a little disappointed now."
    c "..."
    scene 10_947 with vpunch
    c "AAAH!"
    mc "..."
    scene 10_948 with Dissolve(1)
    ir "..."
    scene 10_949 with Dissolve(1)
    mc "What the fuck! That was loud, Cara!"
    c "Haha."
    mc "Seriously, that was crazy... Now everyone who heard that will think I'm... I'm doing something inappropriate to you."
    c "IT WAS JUST A SPIDER, SORRY!"
    c "There... Better?"
    scene 10_950 with Dissolve(1)
    c "Maybe we can do something inappropriate later!"
    mc "Did that spider bite you? Who are you?"
    c "Hehe..."
    scene 10_951 with Dissolve(1)
    ""
    $ renpy.end_replay()
    jump Week4_Saturday_Cara_Park

label Week4_Saturday_Cara_Park:
    scene black with Dissolve(1)
    pause 2
    scene 10_952 with Dissolve(1)
    mc "What courses will you take in college?"
    c "I don't know yet. I still have some time to think about it."
    mc "Just a few months... That's not that long, anymore."
    c "Do you already know what courses you'll take?"
    mc "Most of 'em, yes. But as I said in the car, it also depends if I can get a scholarship or not."
    scene 10_953 with Dissolve(1)
    c "Hmm... Maybe the reason why I haven't really thought about it much is that Nikki didn't go to college, and I..."
    mc "But didn't she want to go to college?"
    c "She did. But after she got the job offer, she cancelled it."
    scene 10_954 with Dissolve(1)
    mc "You can always take some general courses your first semester and once you know what you want to do, you can switch or pick up those courses the next semester."
    c "I might do that. I'm gonna talk to Mom, too, about what she thinks is best."
    mc "And maybe you can convince Nikki to go, too, so you can go together."
    scene 10_955 with Dissolve(1)
    c "I never thought about that. But that would be nice."
    c "Maybe we'll have some courses together. I always wanted to know what she's like in class."
    mc "Maybe she's a total nerd."
    c "Haha, I doubt it, but who knows? Now that I think about it, she always had good marks in school."
    scene 10_956 with Dissolve(1)
    mc "Oh... So, she's smarter than you!"
    c "No, she isn't!"
    mc "Haha."
    mc "Smarter and prettier... Must be tough!"
    c "What?"
    scene 10_957 with Dissolve(1)
    c "So, she's smarter and prettier, huh?"
    mc "Haha. I was talking about you!"
    c "Who's the liar now."
    scene 10_958 with vpunch
    c "Aaah!"
    c "[mc]!"
    scene 10_959 with Dissolve(1)
    c "I'm gonna get you once you let me back down."
    mc "You weigh like nothing. I can do this for a loooong time!"
    scene 10_960 with Dissolve(1)
    c "Nggh..."
    mc "You can try as much as you want. It's not going to work."
    c "*Sigh* Fine..."
    c "Can you please let me down, [mc]?"
    scene 10_961 with vpunch
    c "Aah-ha-ha."
    mc "Haha. Sorry, a little too fast?"
    c "No, it was fun."
    scene 10_962 with Dissolve(1)
    mc "I'm all sweaty now. Maybe we should've gone to the beach instead, so we could cool off."
    c "Yeah, we can go next time. But we should've brought something to drink at least."
    mc "There was a vending machine back there. I'll get us something."
    scene 10_963 with Dissolve(1)
    mc "What do you want?"
    c "Something refreshing."
    mc "Heh, okay. Be right back."
    scene 10_964 with Dissolve(1)
    mc "{i}(Hmm... What should I get for her?){/i}"
    if Alexis_Dating == False:
        pass
    else:
        play sound "Sounds/Phone_Vibrate.mp3"
        n "*Bzzzt. Bzzzt*"
        scene 10_965 with Dissolve(1)
        mc "{i}(Alexis...){/i}"
        mc "{i}(I expected her to call, but...){/i}"
        menu:
            "Turn phone off[KoGa3AutoWTChange1]{size=-4}(Alexis Points-4) {/size} {/color}":
                $ Alexis_Points -= 4
                if Alexis_RiversideStory == True:
                    mc "{i}(Sorry, but I don't have time now.){/i}"
                else:
                    mc "{i}(Don't have time to explain it now. And especially not over the phone.){/i}"
                    mc "{i}(I should've just told her when I was at her place...){/i}"
            "Pick up[KoGa3AutoWTChange1]{size=-4}({i}Alexis RiversideStoryFalse: Alexis Week4 Saturday Cara Phone, Alexis Points-4{/i}) {/size} {/color}":
                if Alexis_RiversideStory == False:
                    $ Alexis_Week4_Saturday_Cara_Phone = True
                    $ Alexis_Points -= 4
                    scene 10_966 with Dissolve(1)
                    mc "Hey, Lexi."
                    a "Hey."
                    mc "How is the day with Erynn going?"
                    a "It's fine..."
                    scene 10_967 with Dissolve(1)
                    a "Why didn't you tell me Cara is staying at your place?"
                    mc "Uhm... I didn't know how to explain it. And I wasn't sure how you'd react if I told you."
                    a "Different to how I'm reacting now!"
                    scene 10_968 with Dissolve(1)
                    a "Now it feels like you're hiding something."
                    mc "I'm not. Cara and I are just friends. Her visit wasn't planned, or anything, and she'll be leaving tomorrow."
                    a "..."
                    a "You still should've told me that another girl is staying at your place!"
                    scene 10_969 with Dissolve(1)
                    mc "I'm sorry. Are you mad at me?"
                    a "Of course I am. How would you feel if I had a boy stay over and you found out? Even if he's just a friend."
                    mc "..."
                    mc "Yeah, I wouldn't want that. Sorry."
                else:
                    scene 10_970 with Dissolve(1)
                    a "So, I've met Cara."
                    mc "Yeah, I figured. Melissa invited her to... crash your brunch."
                    a "Your mom was there, too."
                    scene 10_971 with Dissolve(1)
                    mc "I know. Did you guys talk?"
                    a "We did. Your mom is fun!"
                    mc "She can be. But I meant Cara."
                    scene 10_972 with Dissolve(1)
                    a "Oh... Hmm, not much. She's nice, but I don't have to be friends with your ex."
                    mc "Heh, okay..."
                    if Cara_Visit_Points >= 20:
                        mc "{i}(If they'd talked, this would've been a whole different conversation.){/i}"
                        mc "{i}(And Cara would've mentioned something earlier.){/i}"
                        mc "{i}(I really need to decide before this blows up.){/i}"
                    else:
                        pass
                scene 10_973 with Dissolve(1)
                mc "You're still with Erynn?"
                a "Yes. We're at her apartment to pick some stuff up."
                mc "So she's staying longer at Melissa's. That's good."
                a "She'll be staying with me, too, for a few days next week."
                scene 10_974 with Dissolve(1)
                mc "At the dorm?"
                a "No, at the house."
                mc "We're still on for Monday, or...?"
                a "Yes!"
                if Alexis_RiversideStory == False:
                    scene 10_975 with Dissolve(1)
                    mc "..."
                    a "I can hear you smiling."
                    mc "It's because I'm happy. I hate when you're angry at me."
                    a "So don't give me a reason, next time!"
                else:
                    pass
                scene 10_976 with Dissolve(1)
                a "What are you doing?"
                mc "I was giving Cara a driving lesson earlier."
                a "Be careful, okay? Both of you!"
                mc "We are."
                scene 10_977 with Dissolve(1)
                a "Well, I'll leave you to it then. We'll see each other Monday."
                mc "Can't wait."
                a "Bye, [mc]."
                mc "Bye, darling!"
                a "Haha. Idiot."
    scene 10_978 with Dissolve(1)
    mc "{i}(Alright, let's see...){/i}"
    mc "{i}(Cola? Or maybe an orange juice?){/i}"
    scene 10_979 with vpunch
    ir "Boo!"
    mc "Aah... Iris!"
    ir "Hey, handsome."
    scene 10_980 with Dissolve(1)
    ir "How are you?"
    mc "I'm good, you?"
    ir "Same."
    scene 10_981 with Dissolve(1)
    mc "Coincidence, huh?"
    ir "Haha, is it? I'm starting to believe otherwise. Maybe we're just meant to be!"
    mc "Haha. Maybe..."
    ir "What are you doing here? And do you always walk around without a shirt? Not that I mind. I'd show off that body too!"
    scene 10_982 with Dissolve(1)
    mc "I was lying topless in the park, hoping for a girl to take a picture."
    ir "Any success?"
    mc "Sadly, no."
    ir "I'd have been your first customer if I'd seen you."
    mc "Heh, thanks."
    scene 10_983 with Dissolve(1)
    ir "But good thing you aren't the one taking the picture."
    mc "Trust me. I learned my lesson."
    ir "I think you learned so much more."
    scene 10_984 with Dissolve(1)
    ir "I'd love to stay and spend some time with you, but I have to be at the garage."
    ir "Come by again sometime, yes?"
    mc "Will do."
    scene 10_985 with Dissolve(1)
    ir "Bye, [mc]."
    mc "See ya, Iris."
    if Alexis_Dating == True:
        ir "And I'm still waiting for that double date!"
        mc "Haha."
    else:
        pass
    scene 10_986 with Dissolve(1)
    ir "[mc]!"
    mc "Uh... Iris..."
    ir "Now we're even."
    mc "We were even already."
    ir "Oh... Then I know what to ask for next time."
    scene black with Dissolve(1)
    pause 2
    scene 10_987 with Dissolve(1)
    mc "Here you go. I got you an orange juice."
    c "Thank you."
    scene 10_988 with Dissolve(1)
    mc "So what were we talking about earlier? I forgot."
    c "College and spiders."
    c "Oh, and me being prettier than Nikki."
    mc "Right. I remember now. Except for that last part."
    c "Hey!"
    scene 10_989 with Dissolve(1)
    mc "{i}(Now I keep staring at her boobs.){/i}"
    mc "{i}(Thanks a lot, Iris...){/i}"
    scene 10_990 with Dissolve(1)
    c "Want to taste?"
    mc "What...?"
    scene 10_991 with Dissolve(1)
    c "Want to taste? The orange juice."
    mc "Oh... Yeah... Thanks."
    scene 10_992 with Dissolve(1)
    mc "{i}(My mind is so fucked up...){/i}"
    mc "{i}(I can't even look at her without imagining things.){/i}"
    scene 10_993 with Dissolve(1)
    mc "Do you want to stay here longer, or shall we head home?"
    c "We can leave."
    mc "Alright. Let's go then."
    scene black with Dissolve(2)
    pause 2
    stop music fadeout 1.0
    play music ("Music/LoFi Indie 3.mp3", "Music/LoFi Indie 1.mp3", "Music/LoFi Indie 2.mp3") volume 0.2
    scene 10_994 with Dissolve(1)
    c "What do you want to watch?"
    mc "You pick. But nothing too soppy..."
    c "Hehe, okay. How about this one?"
    mc "That's fine."
    scene 10_995 with Dissolve(1)
    c "Oh, can I finish watching the movie from yesterday, first?"
    mc "The sex movie?"
    c "It's not a sex movie!"
    mc "Haha."
    c "It's just the last fifteen minutes."
    scene 10_996 with Dissolve(1)
    mc "{i}(That position is pretty hot!){/i}"
    mc "{i}(Definitely have to try that next time.){/i}"
    scene 10_997 with Dissolve(1)
    c "I know they're acting, but do you think they... get aroused or something?"
    mc "{i}(She has the weirdest questions sometimes.){/i}"
    mc "They must do! Maybe not everyone, though..."
    scene 10_998 with Dissolve(1)
    c "What do they do when that happens?"
    c "For girls, it isn't that much of an issue, but if the guy gets a boner..."
    mc "No idea. I don't think they'll continue."
    mc "They might take a little time-out until the situation has... cooled down."
    scene 10_999 with Dissolve(1)
    mc "If you were in a movie and had to film a sex scene, and the guy gets turned on. How would you react?"
    c "Uhm..."
    c "Depends on the actor I'm with. I'd be a little flattered, I guess..."
    mc "And what if that same actor sees you naked, and you film the scene and there's... nothing?"
    scene 10_1000 with Dissolve(1)
    c "Hmm... Yeah... I might question my looks..."
    c "Like, is there something wrong with me?"
    scene 10_1001 with Dissolve(1)
    c "What about you? Would you get a hard-on if you were filming such a scene?"
    mc "I'm having one right now just watching the movie. So, yes..."
    c "Haha. TMI!"
    scene 10_1002 with Dissolve(1)
    c "And what if it were with an old lady?"
    mc "Why do I get an old lady? I didn't say you had to have a scene with a grandpa..."
    c "Haha, okay, okay. Let's say around forty then. Or let's take Melissa as an example."
    scene 10_1003 with Dissolve(1)
    mc "Melissa?"
    c "Uh-huh."
    if Melissa_Points >= 13:
        mc "{i}(I've had so many boners just looking at Melissa...){/i}"
        mc "{i}(I've even masturbated thinking about her.){/i}"
    else:
        pass
    mc "Probably, yes."
    scene 10_1004 with Dissolve(1)
    c "Do you have a celebrity crush?"
    mc "Doesn't everyone? Don't you?"
    c "I do."
    mc "Who's yours?"
    c "I asked you first."
    scene 10_1005 with Dissolve(1)
    mc "Ana de Armas!"
    c "Who's that?"
    mc "She's an actress."
    scene 10_1006 with Dissolve(1)
    c "Let me look her up."
    mc "Who's yours?"
    c "I'll tell you after."
    mc "What? You're gonna change it depending on what mine looks like?"
    c "No... I'm just curious."
    scene 10_1007 with Dissolve(1)
    c "Ah... Her! I know her."
    c "She's very pretty. I approve."
    mc "Heh... You approve... Now tell me who's yours!"
    c "I'll show you a picture."
    scene 10_1008 with Dissolve(1)
    mc "Him? You're kidding, right?"
    c "No, I'm not."
    mc "You're not into sports, but your crush is Freakin' Zo?"
    scene 10_1009 with Dissolve(1)
    c "You know him?"
    mc "Of course, I know him. He played for the Marauders."
    mc "I even had posters of him in my room."
    scene 10_1010 with Dissolve(1)
    c "You did? That's funny."
    c "So I'm not the only one who has a crush on him..."
    mc "That's a different crush, okay!"
    c "Haha."
    scene 10_1011 with Dissolve(1)
    mc "That's really unexpected, though."
    mc "I thought it would be a younger guy from one of those boybands you listen to and not a forty-ish-year-old ex-basketball player."
    c "No... I don't know what it is. I just think he's very attractive."
    if Cara_Visit_Points >= 24:
        scene 10_1012 with Dissolve(1)
        c "Hey. Want to play a game?"
        mc "What game?"
        c "..."
        mc "What game, Cara?"
        c "A sex game..."
        menu:
            "Watch movie[KoGa3AutoWTChange1]{size=-4}(Cara Visit Points-2) {/size} {/color}":
                $ Cara_Visit_Points -= 2
                scene 10_1013 with Dissolve(1)
                mc "Uhm... Why don't we finish watching the movie?"
                mc "It's getting late, and we have to wake up early tomorrow."
                c "Right. Forget about that."
                c "Let's finish the movie, then."
                jump Week4_Sunday_Morning_Cara
            "Play game[KoGa3AutoWTChange1]{size=-4}(Cara Week4 Saturday Bed, Cara Week4 Saturday Sexgame, Cara Visit Points+4) {/size} {/color}":
                $ Cara_Week4_Saturday_Bed = True
                $ Cara_Week4_Saturday_Sexgame = True
                $ Cara_Visit_Points += 4
                # Cara Visit (40)
                jump Week4_Saturday_Cara_Sexgame
    else:
        scene 10_1013 with Dissolve(1)
        mc "Uhm... Why don't we finish watching the movie?"
        mc "It's getting late, and we have to wake up early tomorrow."
        c "Right. Forget about that."
        c "Let's finish the movie, then."
        jump Week4_Sunday_Morning_Cara

label Week4_Saturday_Cara_Sexgame:
    if _in_replay:
        $ Cara_Week4_Saturday_LickAss = True
        $ Cara_Week4_Saturday_Game_Change = True
        $ SexCounter_Cara = 6
        $ MC_SexCounter = 6
    $ SexCounter_Cara += 1
    $ MC_SexCounter += 1
    scene 10_1014 with Dissolve(1)
    mc "A sex game?"
    c "Mm-hmm."
    mc "Alright. What do you have in mind?"
    scene 10_1015 with Dissolve(1)
    c "There is this app where you need to fill in words on a wheel and spin it."
    c "And whatever the arrow lands on, you need to do to the other person."
    c "But we'll use two wheels. One with different body parts and another with what to do."
    c "For example. If I spin and the arrows point to kiss and arm, I have to kiss your arm."
    scene 10_1016 with Dissolve(1)
    c "What shall we take as actions?"
    mc "Kiss, lick, bite. Uhm... What else... Suck? Pet?"
    c "Okay. And body parts?"
    mc "I'll leave those to you. Pick whatever you want. But make it interesting."
    scene black with Dissolve(1)
    pause 2
    scene 10_1017 with Dissolve(1)
    c "Okay, I'm done. Let's play."
    mc "This will be fun."
    c "I'm a little nervous now. You can go first."
    scene 10_1018 with Dissolve(1)
    mc "Lick..."
    mc "Aaaand... Thighs. Nice start."
    scene 10_1019 with Dissolve(1)
    mc "Gimme them legs!"
    c "Aah-haha..."
    scene 10_1020 with Dissolve(1)
    ""
    scene 10_1021 with Dissolve(1)
    c "Haha, that's enough. I want to play too!"
    scene 10_1022 with Dissolve(1)
    c "Give me a good one, please..."
    c "Suck... Fingers..."
    mc "Uh, okay."
    scene 10_1023 with Dissolve(1)
    c "I've never done this, so..."
    scene 10_1024 with Dissolve(1)
    mc "{i}(I didn't think I would enjoy this as much as I am...){/i}"
    mc "{i}(Especially when she's looking at me like that.){/i}"
    scene 10_1025 with Dissolve(1)
    mc "That was better than expected!"
    c "Haha."
    scene 10_1026 with Dissolve(1)
    mc "I like this game! Next!"
    mc "Suck again... Lips."
    mc "That's basically a kiss?"
    scene 10_1027 with Dissolve(1)
    ""
    scene 10_1028 with Dissolve(1)
    mc "{i}(I wish I had this one.){/i}"
    scene 10_1029 with Dissolve(1)
    ""
    scene 10_1030 with Dissolve(1)
    ""
    scene 10_1031 with Dissolve(1)
    mc "Yes! Finally."
    c "Haha."
    mc "Time to remove that top!"
    scene 10_1032 with Dissolve(1)
    c "You were waiting for this one, huh?"
    mc "There are a few other options I can't wait to spin, too."
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 10_1033 at moveup
    pause 3
    mc "{i}(Every time I see her, she becomes sexier!){/i}"
    scene 10_1034 with Dissolve(1)
    mc "Now gimme that nipple!"
    c "Ah..."
    scene 10_1035 with Dissolve(1)
    ""
    scene black with Dissolve(1)
    pause 2
    scene 10_1036 with Dissolve(1)
    c "Nooo... Not that!"
    mc "Haha. You picked the words! I'd do it to you."
    c "It's different for you."
    mc "How is that different?"
    c "Can I change it to kiss at least, please?"
    menu:
        "Sure[KoGa3AutoWTChange1]{size=-4}(Cara Week4 Saturday Game Change) {/size} {/color}":
            $ Cara_Week4_Saturday_Game_Change = True
            mc "Sure."
            scene 10_1037 with Dissolve(1)
            mc "So. How you wanna do this?"
            c "Yeah, not like that! Just lie down."
            mc "Hehe, okay."
            scene 10_1038 with Dissolve(1)
            c "I can't believe I'm doing this."
            mc "You came up with the game and made the rules!"
            c "No word to anyone about this."
            scene 10_1039 with Dissolve(1)
            ""
        "No":
            mc "No!"
            mc "It's the rules."
            scene 10_1037 with Dissolve(1)
            mc "So. How you wanna do this?"
            c "Yeah, not like that! Just lie down."
            mc "Hehe, okay."
            scene 10_1038 with Dissolve(1)
            c "I can't believe I'm doing this."
            mc "You came up with the game and made the rules!"
            c "No word to anyone about this."
            scene 10_1040 with Dissolve(1)
            ""
    scene 10_1041 with vpunch
    c "*Slap* There!"
    mc "Hey! It didn't say slap!"
    c "That was for the laughing."
    mc "Haha, I wasn't laughing."
    c "You're laughing right now!"
    scene 10_1042 with Dissolve(1)
    c "Just wait until you get a weird option."
    mc "There's nothing I wouldn't do to you."
    c "..."
    scene 10_1043 with Dissolve(1)
    mc "Except that!"
    c "Haha."
    mc "No! Just no! I hate feet!"
    c "That's what you get!"
    scene 10_1044 with Dissolve(1)
    c "Here!"
    mc "I really don't want to do this, Cara!"
    if Cara_Week4_Saturday_Game_Change == True:
        c "Haha. Alright. Since you let me change, you can change too."
        scene 10_1046 with Dissolve(1)
        mc "I'll suck on this thumb instead!"
        c "Heh, okay."
        scene 10_1047 with Dissolve(1)
        ""
    else:
        c "Tough luck! You should've let me change when I asked!"
        mc "..."
        scene 10_1045 with Dissolve(1)
        mc "{i}(This is so disgusting!){/i}"
        mc "{i}(At least her feet are clean and don't smell.){/i}"
    scene 10_1048 with Dissolve(1)
    mc "Let's remove a few options. I don't want to get feet again."
    mc "This will also make it more interesting."
    mc "I'll start again, since we changed the wheels."
    scene 10_1049 with Dissolve(1)
    mc "What the fuck!"
    c "Haha. That's definitely more interesting!"
    mc "Why is this even an option for me? We should have separate wheels!"
    c "Haha, you changed them. Good luck!"
    scene 10_1050 with Dissolve(1)
    mc "Yeah, that's not gonna happen. And I'm quite sure it's close to impossible."
    c "You've never tried it?"
    mc "What kind of question is that? Of course not!"
    mc "Have you ever tried to lick your pussy?"
    c "Haha, no!"
    scene 10_1051 with Dissolve(1)
    mc "I'll spin again."
    c "No! Respins are against the rules!"
    mc "Cara..."
    c "I'll do that one!"
    mc "You? Okay..."
    scene 10_1052 with Dissolve(1)
    c "You owe me, though!"
    scene 10_1053 with Dissolve(1)
    ""
    scene 10_1054 with Dissolve(1)
    mc "{i}(Fuck!){/i}"
    scene 10_1055 with Dissolve(1)
    mc "{i}(This feels so amazing...){/i}"
    scene 10_1056 with Dissolve(1)
    ""
    scene 10_1057 with Dissolve(1)
    c "Hey. Instead of playing, want to continue this instead?"
    mc "Mm-hmm. I'd like that."
    mc "But how about you turn around then?"
    c "Turn around?"
    scene 10_1058 with Dissolve(1)
    c "You mean like this?"
    mc "Yes!"
    mc "Your pants need to go, though."
    scene 10_1059 with Dissolve(1)
    mc "{i}(Fuck! I'm so turned on right now.){/i}"
    mc "{i}(My whole body is shaking because of the excitement.){/i}"
    scene 10_1060 with Dissolve(1)
    c "Ah..."
    scene 10_1061 with Dissolve(1)
    ""
    scene 10_1062 with Dissolve(1)
    ""
    scene 10_1063 with Dissolve(1)
    ""
    scene 10_1064 with Dissolve(1)
    mc "{i}(I can't believe this is the first time I'm doing sixty-nine!){/i}"
    mc "{i}(This is awesome!){/i}"
    scene black with Dissolve(1)
    pause 2
    scene 10_1065 with Dissolve(1)
    ""
    scene 10_1066 with Dissolve(1)
    c "Slowly..."
    scene 10_1067 with vpunch
    c "Ahhh..."
    mc "Didn't you say slowly?"
    c "Fuck me, [mc]!"
    show 10_1068
    ""
    show 10_1069
    ""
    scene 10_1070 with Dissolve(1)
    mc "{i}(She keeps surprising me...){/i}"
    scene 10_1071 with Dissolve(1)
    mc "{i}(This position is so hot!){/i}"
    mc "{i}(Looking at her ass while she rides me!){/i}"
    show 10_1072
    ""
    scene 10_1073 with Dissolve(1)
    mc "Fuck... Cara!"
    if Cara_Week4_Saturday_LickAss == True:
        scene 10_1074 with Dissolve(1)
        c "Uh, [mc]..."
        mc "Everything alright?"
        c "Yeah, nothing like that. I have a question."
        mc "Now? Okay?"
        scene 10_1075 with Dissolve(1)
        c "Have you ever done... anal?"
        mc "No, I haven't."
        c "I was thinking about it last time when you... You know... licked it."
        scene 10_1076 with Dissolve(1)
        c "Do you maybe want to try?"
        mc "Don't get me wrong, I want to. It's something I was thinking about, too."
        mc "But we aren't really ready for it, I think. We should get some stuff first, like lube maybe and uh... practice somehow."
        scene 10_1077 with Dissolve(1)
        mc "Maybe we can do it next time?"
        c "*Nods*"
        mc "In the meantime, I can keep licking it, if you liked it."
        c "Mm-hmm..."
        mc "{i}(I don't know where it came from, but I like this kinky side of her.){/i}"
        scene 10_1078 with Dissolve(1)
        ""
        scene 10_1079 with Dissolve(1)
        mc "Wanna do some doggy instead?"
        c "Uh-huh."
        mc "Uh-huh?"
        c "Haha."
    else:
        pass
    scene 10_1080 with Dissolve(1)
    ""
    scene 10_1081 with Dissolve(1)
    ""
    scene 10_1082 with Dissolve(1)
    ""
    show 10_1083
    ""
    show 10_1084
    ""
    scene 10_1085 with Dissolve(1)
    c "*Moaning*"
    scene 10_1086 with vpunch
    pause 1
    scene 10_1086 with vpunch
    mc "Ahh..."
    c "Nggh..."
    scene 10_1087 with Dissolve(1)
    ""
    scene black with Dissolve(1)
    pause 2
    scene 10_1088 with Dissolve(1)
    mc "We surely ended your vacation here with a bang."
    c "Haha. Literally!"
    mc "Haha."
    scene 10_1089 with Dissolve(1)
    c "*Sigh* I don't wanna go to school on Monday. This week went way too quick."
    mc "Then don't. Call in sick and stay another week."
    c "I wish I could. Mom would come to get me personally. Drag me home and send me to school."
    mc "Hehe."
    scene 10_1090 with Dissolve(1)
    mc "Since your dad lives here, it's easier for you to come to visit again."
    mc "I will come visit you, too, and before we know it, it'll be summer."
    c "Hmm..."
    scene 10_1091 with Dissolve(1)
    ""
    $ renpy.end_replay()
    jump Week4_Sunday_Morning_Cara

label Week4_Sunday_Morning_Nikki:
    scene black with Dissolve(2)
    pause 2
    stop music fadeout 1.0
    play music ("Music/LoFi Indie 2.mp3", "Music/LoFi Indie 2.mp3", "Music/LoFi Indie 3.mp3") volume 0.2
    if Nikki_Week4_Saturday_Bed == True:
        scene 10_1104 with Dissolve(1)
        ni "[mc]. You need to wake up now."
        mc "Nggh..."
        ni "We have to leave in ten minutes."
        scene 10_1105 with vpunch
        ni "Aah..."
        mc "Maybe I want to keep you here!"
        ni "Haha. [mc]!"
        mc "Five minutes!"
        ni "[mc]!"
        scene 10_1106 with Dissolve(1)
        ni "..."
        mc "..."
        mc "{i}(I really don't want her to leave.){/i}"
        scene 10_1107 with Dissolve(1)
        ""
        scene 10_1108 with Dissolve(1)
        ""
        scene 10_1109 with Dissolve(1)
        mc "What?"
        ni "We don't have time for this now."
        ni "If you wanted to have sex with me before I leave, you should've woken up earlier!"
        scene 10_1110 with Dissolve(1)
        ni "Come on..."
        mc "{i}(She's so doing this on purpose.){/i}"
        mc "What about if I speed to the airport? We'll have a little more time then."
        ni "You had your chance..."
        scene 10_1111 with vpunch
        mc "*Slap* You're evil!"
        ni "Pure evil!"
        mc "I'll never sleep in again!"
        ni "Haha."
    else:
        scene 10_1092 with Dissolve(1)
        mc "Morning."
        ni "Hey, morning. I was just about to wake you."
        mc "Hehe. I guess I'm getting used to waking up early. All packed up?"
        ni "*Sigh* Yes..."
    scene 10_1093 with Dissolve(1)
    m "Oh, you're here already. I was just coming to get you."
    mc "..."
    mc "It's not that I sleep in all the time. If I need to wake up early, I can..."
    scene 10_1094 with Dissolve(1)
    m "I can't believe you're leaving already. It's only been a few days, but I'm going to miss you."
    m "It was lovely having you over."
    ni "Thank you, Emily. I'm gonna miss you too. And thank you for letting me stay here out of the blue."
    m "Come here, sweetheart!"
    scene 10_1095 with Dissolve(1)
    m "You're always welcome here. Out of the blue or not. We have plenty of space."
    ni "Thank you."
    scene 10_1096 with Dissolve(1)
    m "Hey, don't cry now, or you're gonna make me cry, too."
    ni "Haha, sorry."
    scene 10_1097 with Dissolve(1)
    ""
    scene 10_1098 with Dissolve(1)
    m "[mc], I'll be at Melissa's a little later. Erynn wanted to talk with me."
    m "Could you pick up some groceries on your way back?"
    mc "Is it even open? It's Sunday..."
    m "It's open. I'll text you a list."
    mc "Alright."
    scene 10_1099 with Dissolve(1)
    mc "I guess we'll be heading to the airport, then?"
    ni "Mm-hmm."
    mc "Do you have everything, or...?"
    ni "I think so, yes."
    scene 10_1100 with Dissolve(1)
    m "And if not, you'll just have to come to visit us again."
    ni "Haha, will do."
    m "Give me one more hug!"
    scene 10_1101 with Dissolve(1)
    m "Call us when you land, okay? And say hi to your family from me."
    ni "I will. Thank you for everything, Emily."
    m "Bye, sweetheart!"
    ni "Bye, Emily!"
    scene 10_1102 with Dissolve(1)
    mc "Ready to go?"
    ni "Not really..."
    ni "But I don't have a choice."
    scene 10_1103 with Dissolve(1)
    mc "I'll drive very slowly."
    ni "Haha. Good!"
    scene black with Dissolve(2)
    pause 2
    scene 10_1137 with Dissolve(1)
    mc "..."
    mc "{i}(She's been quiet for a while now.){/i}"
    mc "{i}(Is it just because she's leaving, or is something else bothering her?){/i}"
    scene 10_1138 with Dissolve(1)
    mc "Are you alright?"
    ni "Oh yeah, sorry. Just a little sad."
    ni "The last day went by so quick. I'd hoped to have a little more time."
    mc "It was quick, yeah."
    scene 10_1139 with Dissolve(1)
    mc "Well... We're here. This is as far as I can follow you."
    menu:
        "Leave":
            mc "Have a safe flight, and call me when you've arrived."
            mc "Bye, Nikki!"
            ni "..."
            scene 10_1140 with Dissolve(1)
            ni "Hey... What?"
            ni "[mc]?"
            mc "{i}(I feel so bad...){/i}"
            mc "{i}(Isn't she running after me?){/i}"
            scene 10_1141 with Dissolve(1)
            mc "Uh..."
            mc "{i}(Not what I expected.){/i}"
            scene 10_1142 with Dissolve(1)
            mc "Where do you think you're going? Did you really think I'd let you leave like this?"
            ni "Haha."
            scene 10_1143 with Dissolve(1)
            ""
            scene 10_1144 with Dissolve(1)
            ni "I can play that game too!"
            mc "Evil!"
            ni "You left first!"
            mc "Would you have come chasing after me if I hadn't?"
            ni "Maybe, maybe not. You'll never know."
        "Hug":
            pass
    scene 10_1145 with Dissolve(1)
    mc "I'm gonna miss you."
    ni "I'm going to miss you, too."
    scene 10_1146 with Dissolve(1)
    mc "Longest hug ever?"
    ni "Just a little longer."
    mc "It's not like we won't see each other again."
    ni "..."
    if Nikki_Week4_Saturday_Bed == True:
        scene 10_1147 with Dissolve(1)
        mc "Are you crying again? Are you okay?"
        ni "..."
        mc "Nikki."
        ni "Yeah, I don't know. I just got very emotional for some reason."
        scene 10_1148 with Dissolve(1)
        mc "Hey, it will be alright."
        scene 10_1149 with Dissolve(1)
        ni "*Sigh* I guess it's time to head to the terminal now."
        mc "Yeah. Call me when you've landed."
        ni "I will. What are you gonna do for the rest of the day?"
        mc "Pick up those groceries, and work at the restaurant in the afternoon."
        ni "You'll be busy then."
        if Nikki_Week4_Wednesday_Visit_Knows == True:
            $ Nikki_Week4_Wednesday_AlexisLaylaBreakUp = True
            scene 10_1150 with Dissolve(1)
            ni "There's one more thing."
            ni "About that girl you were seeing before I came here."
            mc "{i}(I thought she'd just brushed it off, but she's actually thought about it.){/i}"
            scene 10_1151 with Dissolve(1)
            ni "Now that I won't be here for a while, are you going to meet up with her again?"
            mc "No... Of course not. I want you, Nikki! Only you!"
            mc "{i}(Fuck. I can't keep doing this. I have to decide sooner or later.){/i}"
            ni "Good! Because I won't be this understanding next time!"
        else:
            pass
        scene 10_1152 with Dissolve(1)
        ""
        scene 10_1153 with Dissolve(1)
        ni "Bye, [mc]!"
        mc "Bye, Nikki. Have a safe flight."
        ni "Thank you."
        scene 10_1154 with Dissolve(1)
        ni "Bye."
        mc "Hehe, bye. See you soon."
        menu:
            "Leave":
                pass
            "Love you[KoGa3AutoWTChange1]{size=-4}(Nikki Visit Points+4) {/size} {/color}":
                $ Nikki_Visit_Points += 4
                # Nikki Visit (40)
                scene 10_1155 with Dissolve(1)
                mc "Nikki!"
                ni "Hmm?"
                mc "I love you!"
                scene 10_1156 with vpunch
                mc "Haha."
                ni "I love you, [mc]!"
                scene 10_1157 with Dissolve(1)
                ""
                scene 10_1158 with Dissolve(1)
                mc "*Slap* Now go, before you miss your flight."
                ni "Aah..."
                mc "Damn, I'm gonna miss this!"
                ni "Haha."
    else:
        if Nikki_Visit_Points >= 26:
            scene 10_1147 with Dissolve(1)
            mc "Are you crying again? Are you okay?"
            ni "..."
            mc "Nikki."
            ni "Yeah, I don't know. I just got very emotional for some reason."
            scene 10_1148 with Dissolve(1)
            mc "Hey, it will be alright."
            scene 10_1149 with Dissolve(1)
            ni "*Sigh* I guess it's time to head to the terminal now."
            mc "Yeah. Call me when you've landed."
            ni "I will. What are you gonna do for the rest of the day?"
            mc "Pick up those groceries, and work at the restaurant in the afternoon."
            ni "You'll be busy then."
            if Nikki_Week4_Wednesday_Visit_Knows == True:
                $ Nikki_Week4_Wednesday_AlexisLaylaBreakUp = True
                scene 10_1150 with Dissolve(1)
                ni "There's one more thing."
                ni "You told me that you were seeing someone before I came here."
                mc "{i}(I thought she'd just brushed it off, but she's actually thought about it.){/i}"
                scene 10_1151 with Dissolve(1)
                ni "Now that I won't be here for a while, are you going to meet up with her again?"
                mc "No... Of course not. I want you, Nikki! Only you!"
                mc "{i}(Fuck. I can't keep doing this. I have to decide sooner or later.){/i}"
                ni "Good! Because I won't be this understanding next time!"
            else:
                pass
            scene 10_1152 with Dissolve(1)
            ""
            scene 10_1153 with Dissolve(1)
            ni "Bye, [mc]!"
            mc "Bye, Nikki. Have a safe flight."
            ni "Thank you."
            scene 10_1154 with Dissolve(1)
            ni "Bye."
            mc "Hehe, bye. See you soon."
            menu:
                "Leave":
                    pass
                "Love you[KoGa3AutoWTChange1]{size=-4}(Nikki Visit Points+4) {/size} {/color}":
                    $ Nikki_Visit_Points += 4
                    # Nikki Visit (40)
                    scene 10_1155 with Dissolve(1)
                    mc "Nikki!"
                    ni "Hmm?"
                    mc "I love you!"
                    scene 10_1156 with vpunch
                    mc "Haha."
                    ni "I love you, [mc]!"
                    scene 10_1157 with Dissolve(1)
                    ""
                    scene 10_1158 with Dissolve(1)
                    mc "*Slap* Now go, before you miss your flight."
                    ni "Aah..."
                    mc "Damn, I'm gonna miss this!"
                    ni "Haha."
        else:
            $ Nikki_Girlfriend = False
            $ Riverside_Friends = True
            scene 10_1159 with Dissolve(1)
            ni "Let's end it here."
            mc "Uh, what? What do you mean?"
            ni "Us... Let's end... us. It's... It's not... I don't know. It's different."
            ni "It feels like your head is somewhere else, or with someone else."
            scene 10_1160 with Dissolve(1)
            mc "Nikki... No, I..."
            ni "I don't regret coming here. I had an amazing time, and you're an amazing guy."
            ni "It's just not our time."
            mc "Nikki..."
            ni "Let's not prolong this, [mc]. My decision is made."
            scene 10_1161 with Dissolve(1)
            mc "So, this is it then? Are we at least still friends?"
            ni "We'll always be more than just friends, [mc]."
            mc "Can I hug you one more time?"
            ni "Of course."
            scene 10_1162 with Dissolve(1)
            ni "..."
            scene 10_1163 with Dissolve(1)
            ni "Goodbye, [mc]!"
            mc "..."
            scene 10_1164 with Dissolve(1)
            mc "{i}(Goodbye, Nikki!){/i}"
            scene 10_1165 with Dissolve(1)
            ""
            scene 10_1166 with Dissolve(1)
            mc "{i}(Fuck...){/i}"
            mc "{i}(I never wanted to hurt her. She's amazing and deserves the world.){/i}"
            mc "{i}(But maybe this is for the best? Why am I so indecisive all the time?){/i}"
            mc "{i}(I'm still gonna miss her like crazy!){/i}"
    jump Week4_Sunday_Grocery

label Week4_Sunday_Morning_Cara:
    scene black with Dissolve(2)
    pause 2
    stop music fadeout 1.0
    play music ("Music/LoFi Indie 2.mp3", "Music/LoFi Indie 2.mp3", "Music/LoFi Indie 3.mp3") volume 0.2
    if Cara_Week4_Saturday_Bed == True:
        scene 10_1123 with Dissolve(1)
        mc "{i}(Of course she's still sleeping.){/i}"
        scene 10_1124 with Dissolve(1)
        ""
        scene 10_1125 with Dissolve(1)
        c "Nggh..."
        mc "It actually worked."
        mc "I really must be a prince."
        c "..."
        scene 10_1126 with Dissolve(1)
        c "What time is it?"
        mc "We'll have to leave in like twenty minutes."
        c "What? [mc]!"
        scene 10_1127 with Dissolve(1)
        mc "{i}(I wish we had a little more time.){/i}"
        mc "{i}(I'd love to see that ass bouncing on me again.){/i}"
        scene 10_1128 with Dissolve(1)
        c "What are you doing?"
        mc "Just looking and reminiscing."
        c "..."
        mc "Anyway. I'll let you get ready. I'll be waiting downstairs."
        c "Okay."
    else:
        scene 10_1112 with Dissolve(1)
        c "Hey, morning."
        mc "Hey. You're here already."
        c "Hehe. I can wake up early if I have to."
    scene 10_1113 with Dissolve(1)
    m "Oh, you're awake too. I was just coming to get you."
    mc "..."
    mc "It's not that I sleep in all the time."
    scene 10_1114 with Dissolve(1)
    m "I can't believe you're leaving already. It's only been a few days, but I'm going to miss you."
    m "It was lovely having you over."
    c "Thank you, Emily. I'm gonna miss you too. And thank you for letting me stay here out of the blue."
    m "Come here, sweetheart!"
    scene 10_1115 with Dissolve(1)
    m "You're always welcome here. Out of the blue or not. We have plenty of space."
    c "Thank you."
    scene 10_1116 with Dissolve(1)
    m "Hey, don't cry now, or you're gonna make me cry, too."
    c "Haha, sorry."
    scene 10_1117 with Dissolve(1)
    ""
    scene 10_1118 with Dissolve(1)
    m "[mc], I'll be at Melissa's a little later. Erynn wanted to talk with me."
    m "Could you pick up some groceries on your way back?"
    mc "Is it even open? It's Sunday..."
    m "It's open. I'll text you a list."
    mc "Alright."
    scene 10_1119 with Dissolve(1)
    mc "I guess we'll be heading to the airport, then?"
    c "Mm-hmm."
    mc "Do you have everything, or...?"
    c "I think so, yes."
    scene 10_1120 with Dissolve(1)
    m "And if not, you'll just have to come to visit us again."
    c "Haha, will do."
    m "Give me one more hug!"
    scene 10_1121 with Dissolve(1)
    m "Call us when you land, okay? And say hi to your family from me."
    c "I will. Thank you for everything, Emily."
    m "Bye, sweetheart!"
    c "Bye, Emily!"
    scene 10_1122 with Dissolve(1)
    mc "Ready to go?"
    c "Not really..."
    c "But I don't have a choice."
    scene black with Dissolve(2)
    pause 2
    scene 10_1167 with Dissolve(1)
    mc "..."
    mc "{i}(She's been quiet for a while now.){/i}"
    mc "{i}(Is it just because she's leaving, or is something else bothering her?){/i}"
    scene 10_1168 with Dissolve(1)
    mc "Are you alright?"
    c "Hmm? Oh, yeah. I just don't know what to say."
    c "The last day went by so quick. I'd hoped to have a little more time."
    mc "It was quick, yeah."
    scene 10_1169 with Dissolve(1)
    mc "Well... We're here. This is as far as I can follow you."
    scene 10_1170 with Dissolve(1)
    mc "I'm gonna miss you."
    c "I'm going to miss you too."
    if Cara_Week4_Saturday_Bed == True:
        scene 10_1171 with Dissolve(1)
        c "*Sigh* I guess it's time to head to the terminal now."
        mc "Yeah. Call me when you've landed."
        c "I will. What are you gonna do for the rest of the day?"
        mc "Pick up those groceries, and work at the restaurant in the afternoon."
        c "You'll be busy, then."
        if Cara_Week4_Wednesday_Visit_Knows == True:
            $ Cara_Week4_Wednesday_AlexisLaylaBreakUp = True
            scene 10_1172 with Dissolve(1)
            c "Uhm, [mc]. There's one more thing I wanted to ask."
            c "You told me that you were seeing someone before I came here."
            mc "{i}(I thought she'd just brushed it off, but she's actually thought about it.){/i}"
            scene 10_1173 with Dissolve(1)
            mc "Don't worry about that, Cara. I want you!"
            mc "{i}(Fuck. I can't keep doing this. I have to decide sooner or later.){/i}"
            c "I want you too."
        else:
            pass
        scene 10_1174 with Dissolve(1)
        ""
        scene 10_1175 with Dissolve(1)
        c "Bye, [mc]!"
        mc "Bye, Cara. Have a safe flight."
        c "Thank you."
        scene 10_1176 with Dissolve(1)
        c "Bye."
        mc "Hehe, bye. See you soon."
        menu:
            "Leave":
                pass
            "Love you[KoGa3AutoWTChange1]{size=-4}(Cara Visit Points+4) {/size} {/color}":
                $ Cara_Visit_Points += 4
                # Cara Visit (44)
                scene 10_1177 with Dissolve(1)
                mc "Cara!"
                c "Hmm?"
                mc "I love you!"
                scene 10_1178 with Dissolve(1)
                c "Stop... Not here. That is so embarrassing."
                mc "Haha. I do though."
                c "*Whispers* I love you, too."
                mc "What?"
                c "You heard me!"
    else:
        if Cara_Visit_Points >= 29:
            scene 10_1171 with Dissolve(1)
            c "*Sigh* I guess it's time to head to the terminal now."
            mc "Yeah. Call me when you've landed."
            c "I will. What are you gonna do for the rest of the day?"
            mc "Pick up those groceries, and work at the restaurant in the afternoon."
            c "You'll be busy, then."
            if Cara_Week4_Wednesday_Visit_Knows == True:
                $ Cara_Week4_Wednesday_AlexisLaylaBreakUp = True
                scene 10_1172 with Dissolve(1)
                c "Uhm, [mc]. There's one more thing I wanted to ask."
                c "You told me that you were seeing someone before I came here."
                mc "{i}(I thought she'd just brushed it off, but she's actually thought about it.){/i}"
                scene 10_1173 with Dissolve(1)
                mc "Don't worry about that, Cara. I want you!"
                mc "{i}(Fuck. I can't keep doing this. I have to decide sooner or later.){/i}"
                c "I want you, too."
            else:
                pass
            scene 10_1174 with Dissolve(1)
            ""
            scene 10_1175 with Dissolve(1)
            c "Bye, [mc]!"
            mc "Bye, Cara. Have a safe flight."
            c "Thank you."
            scene 10_1176 with Dissolve(1)
            c "Bye."
            mc "Hehe, bye. See you soon."
            menu:
                "Leave":
                    pass
                "Love you[KoGa3AutoWTChange1]{size=-4}(Cara Visit Points+4) {/size} {/color}":
                    $ Cara_Visit_Points += 4
                    # Cara Visit (44)
                    scene 10_1177 with Dissolve(1)
                    mc "Cara!"
                    c "Hmm?"
                    mc "I love you!"
                    scene 10_1178 with Dissolve(1)
                    c "Stop... Not here. That is so embarrassing."
                    mc "Haha. I do though."
                    c "*Whispers* I love you, too."
                    mc "What?"
                    c "You heard me!"
        else:
            $ Cara_Girlfriend = False
            $ Riverside_Friends = True
            $ Nikki_SP = False
            scene 10_1179 with Dissolve(1)
            c "Let's break up, [mc]."
            mc "Uh, what? What do you mean?"
            c "I don't think we should be together anymore."
            scene 10_1180 with Dissolve(1)
            mc "Cara... No, I..."
            c "I love you and I always will. But I can feel that your heart wasn't with me."
            c "It's not the same as it was before."
            mc "Cara..."
            scene 10_1181 with Dissolve(1)
            mc "So, this is it then? Are we at least still friends?"
            c "We'll always be more than just friends, [mc]."
            mc "Can I hug you one more time?"
            c "*Nods*"
            scene 10_1182 with Dissolve(1)
            mc "I'm so sorry that I made you feel this way, Cara."
            c "..."
            scene 10_1183 with Dissolve(1)
            mc "Goodbye, Cara."
            scene 10_1184 with Dissolve(1)
            c "..."
            scene 10_1166 with Dissolve(1)
            mc "{i}(Fuck...){/i}"
            mc "{i}(I never wanted to hurt her. She's amazing and deserves the world.){/i}"
            mc "{i}(But maybe this is for the best? Why am I so indecisive all the time?){/i}"
            mc "{i}(I'm still gonna miss her like crazy!){/i}"
    jump Week4_Sunday_Grocery

label Week4_Sunday_Morning:
    scene black with Dissolve(2)
    pause 2
    stop music fadeout 1.0
    play music ("Music/LoFi Indie 2.mp3", "Music/LoFi Indie 2.mp3", "Music/LoFi Indie 3.mp3") volume 0.2
    scene 10_1129 with Dissolve(1)
    mc "Morning, Mom."
    m "Good morning, honey."
    mc "Are you going somewhere?"
    scene 10_1130 with Dissolve(1)
    m "Yes, I'm heading next door. Erynn wanted to talk to me."
    mc "Oh, okay."
    m "I don't know how long it will take, and I still need some stuff for the restaurant."
    m "Can you do me a favour and head to the supermarket in the meantime?"
    scene 10_1131 with Dissolve(1)
    mc "Uh sure, but is it even open on a Sunday?"
    m "Thank you and yes, it's open."
    mc "What do you need?"
    m "I'll text you a list."
    jump Week4_Sunday_Grocery

label Week4_Sunday_Grocery:
    scene black with Dissolve(2)
    pause 2
    if Erynn_End == True:
        pass
    else:
        if Erynn_Week3_Monday_Blackmailhelp == True:
            scene 10_1185 with Dissolve(1)
            mc "{i}(Let's see... What does she need?){/i}"
            mc "{i}(Onions, paprika...){/i}"
            scene 10_1186 with Dissolve(1)
            mc "{i}(Heh... John?){/i}"
            mc "{i}(This family and coincidences.){/i}"
            scene 10_1187 with Dissolve(1)
            mc "Hey, John."
            jo "Hey, [mc]. What a coincidence."
            mc "Haha, tell me about it. Like father, like... daughter."
            jo "Hmm?"
            mc "Oh, nothing. Inside joke with Iris."
            scene 10_1188 with Dissolve(1)
            mc "Frozen pizza?"
            jo "You know... I've never been much of a cook."
            mc "I never complained."
            jo "You didn't. Someone else does."
            mc "Haha. Get her the Caprese, that's her favourite."
            jo "Thanks."
            if Valeria_Week4_Friday_Help == True:
                scene 10_1189 with Dissolve(1)
                mc "{i}(Hmm... Now that I think about it.){/i}"
                mc "{i}(John might be able to help me with Erynn.){/i}"
                mc "{i}(I should ask him, at least.){/i}"
                scene 10_1190 with Dissolve(1)
                mc "John, can I ask you a question?"
                jo "Sure, what's up?"
                mc "How best to explain this..."
                mc "Uhm... I have this friend, Erynn..."
                scene black with Dissolve(1)
                pause 2
                scene 10_1191 with Dissolve(1)
                jo "*Shakes head* Despicable!"
                jo "Who's the guy, anyway?"
                mc "He's her agent and the son of the CEO."
                jo "That's bad."
                scene 10_1192 with Dissolve(1)
                jo "Do you know what you're going to do?"
                mc "Well, we have this plan..."
                mc "I say plan, but it's actually just a stupid idea. I just don't know what else to do."
            else:
                scene 10_1193 with Dissolve(1)
                jo "How are you doing after what happened on Friday?"
                mc "I'm good. Thanks again for your help."
                jo "Anytime."
                scene 10_1194 with Dissolve(1)
                jo "What about the girl?"
                mc "Yeah... About that... I might have a favour to ask."
                mc "I want to help her, and we have this plan."
                mc "I say plan, but it's actually just a stupid idea. I just don't know what else to do."
            scene 10_1195 with Dissolve(1)
            jo "What do you have in mind?"
            mc "So, we were thinking..."
            scene black with Dissolve(1)
            pause 2
            scene 10_1196 with Dissolve(1)
            jo "And she's okay with that?"
            mc "I think she's gotten to the point that she might try anything to stop this."
            jo "If I can help in any way, I'm game, but she needs to be one hundred per cent sure she's willing to do this."
            jo "It won't be as easy as it sounds. How about we all meet up first and talk, and see from there?"
            scene 10_1197 with Dissolve(1)
            mc "Yeah, that's what she wants to do anyway. Are you free today?"
            jo "I'm at the garage the whole day. You can come by anytime you want."
            mc "I have to help Mom at the restaurant first, but how about in the evening?"
            jo "That's good for me."
            mc "Alright. I'll talk with Erynn, and if anything changes, I'll call you."
            scene 10_1198 with Dissolve(1)
            mc "Thanks, John. See you later, then."
            jo "Later, [mc]."
        else:
            pass
    scene black with Dissolve(2)
    pause 2
    scene 10_1199 with Dissolve(1)
    mc "{i}(Oh, Mom's back already.){/i}"
    mc "{i}(What is she doing? Didn't even hear me come in?){/i}"
    scene 10_1200 with Dissolve(1)
    mc "Hey, Mom."
    mc "You alright?"
    scene 10_1201 with Dissolve(1)
    m "Hey, honey. Yeah. You can put the bags on the table. Thank you."
    m "Did you find everything?"
    mc "Yes."
    if Erynn_End == True:
        pass
    else:
        if Erynn_Week3_Monday_Blackmailhelp == True:
            $ Emily_Points += 2
            # Emily (18)
            scene 10_1202 with Dissolve(1)
            mc "Did you talk with Erynn?"
            m "Mm-hmm. The poor girl. I feel so sorry for her."
            m "Can't imagine what she's been going through."
            scene 10_1203 with Dissolve(1)
            m "I wish she would've told us sooner, so..."
            mc "She didn't tell anyone. No one knew."
            m "I'm happy she told you though."
            mc "Because she had to. If I didn't see what happened, this would still be going on."
            m "*Sigh*"
            scene 10_1204 with Dissolve(1)
            mc "So what now? Are you going to help her?"
            m "Of course. I'll go see my lawyer tomorrow and ask for advice. That's all we can do for now."
            mc "{i}(I know I should just let our parents handle this, but who knows how long it will take...){/i}"
            m "And please continue to be there for her. She needs all of our support now."
            mc "I will."
        else:
            pass
    jump Week4_Sunday_Bike

label Week4_Sunday_Bike:
    if Emily_Week3_Sunday_Surprise == True:
        $ MC_Bike = True
        scene 10_1205 with Dissolve(1)
        m "Well, uhm... I've got a surprise for you."
        mc "Oh, you do?"
        m "Mm-hmm. It's outside. Follow me."
        scene 10_1206 with Dissolve(1)
        m "Don't look!"
        mc "I have my eyes closed."
        mc "{i}(What can it be? Maybe something in that package she was so secretive about?){/i}"
        m "Stop here!"
        m "I know it's been a few months, but..."
        scene 10_1207 with Dissolve(1)
        m "Happy belated birthday, honey!"
        mc "..."
        mc "Mom!"
        scene 10_1208 with Dissolve(1)
        mc "{i}(This is so amazing!){/i}"
        mc "I know we talked about it, and you agreed that I can have a bike..."
        mc "But you bought it already? This must have been so expensive."
        m "John gave us a really good offer."
        scene 10_1209 with vpunch
        m "Aaah!"
        mc "Thank you, thank you, thank you!"
        m "Haha. You're welcome."
        scene 10_1210 with Dissolve(1)
        m "Please don't make me regret this decision."
        m "Always drive safe, okay?"
        mc "I promise!"
        menu:
            "Kiss her lips":
                scene 10_1212 with Dissolve(1)
                mc "You're the best!"
                m "Uh..."
                scene 10_1213 with Dissolve(1)
                m "You kissed me on the lips... This is soooo embarrassing!"
                mc "..."
                mc "Really? I wasn't that dramatic!"
                scene 10_1214 with Dissolve(1)
                m "No?"
                m "*Imitating* I could die of embarrassment!"
                mc "Yeah, yeah. I get it."
                scene 10_1215 with Dissolve(1)
                mc "Anyway. Thank you very much."
                m "You're welcome."
            "Kiss her cheek":
                scene 10_1211 with Dissolve(1)
                mc "You're the best!"
                scene 10_1215 with Dissolve(1)
                mc "Thank you very much, Mom."
                m "You're welcome."
        scene 10_1216 with Dissolve(1)
        mc "Two helmets... You got one, too?"
        m "No. John put this one in for free."
        m "That way you'll always have a spare if a friend rides with you."
        mc "Sweet. I'll call him later to thank him."
        scene 10_1217 with Dissolve(1)
        mc "Have you ever driven a motorcycle?"
        m "No, never. Never even sat on one."
        scene 10_1218 with Dissolve(1)
        mc "Today is your lucky day, then."
        mc "Here you go!"
        m "No-no-no... That's not gonna happen."
        scene 10_1219 with Dissolve(1)
        mc "What? Are you scared?"
        m "Yes! I am!"
        mc "Why?"
        m "Because it's dangerous..."
        scene 10_1220 with Dissolve(1)
        mc "We don't have to drive, but at least sit on it."
        m "Okay. I can do that."
        m "It won't fall over, right?"
        mc "It won't."
        scene 10_1221 with Dissolve(1)
        mc "See! It's not that bad."
        m "As long as it's standing here, no."
        m "Can you take a picture of me? I want to show Melissa. She'll be so jealous."
        mc "Sure. If Melissa was here, she would go for a ride with me."
        m "I know she would."
        scene 10_1222 with Dissolve(1)
        m "How do I look?"
        menu:
            "Good":
                mc "You look good! Kinda suits you."
                m "Thanks."
            "Sexy[KoGa3AutoWTChange1]{size=-4}(Emily Week4 Sunday Sexy) {/size} {/color}":
                $ Emily_Week4_Sunday_Sexy = True
                mc "You look sexy!"
                mc "{i}(Wow... I can't believe I just called my mom sexy...){/i}"
                m "Haha, what? Sexy?"
                scene 10_1223 with Dissolve(1)
                m "I'll take sexy."
                mc "*Shakes head* Sometimes I wish I knew how you were when you were my age."
                m "Sexy!"
                mc "Haha, stop!"
        scene 10_1224 with Dissolve(1)
        m "Give me your phone. I'll take one of you."
        mc "Thanks."
        scene 10_1225 with Dissolve(1)
        m "Smile! Three... two... one..."
        mc "..."
        if Emily_Week4_Sunday_Sexy == True:
            m "So sexy!"
            mc "Okay, I get it!"
            m "Haha."
        else:
            pass
        scene 10_1226 with Dissolve(1)
        m "Let's take one more. I don't have that many pictures of you."
        m "Especially of us together."
        scene black with Dissolve(1)
        pause 2
        scene 10_1227 with Dissolve(1)
        m "[mc]. There's something else we need to talk about."
        mc "Okay..."
        m "Uhm... When John delivered the bike, he asked me out."
        scene 10_1228 with Dissolve(1)
        mc "You mean as in a date?"
        m "Mm-hmm."
        mc "What did you say?"
        m "Nothing yet. I wanted to talk to you first. You've known him for some time and are pretty close to him."
        m "So, I wanted to know what you think about this."
        menu:
            "Go for it[KoGa3AutoWTChange1]{size=-4}(Emily Week4 Sunday DateJohn, Emily Points+2) {/size} {/color}":
                $ Emily_Week4_Sunday_DateJohn = True
                $ Emily_Points += 2
                # Emily (20)
                scene 10_1229 with Dissolve(1)
                mc "I saw this coming at the garage already."
                m "Heh."
                mc "You don't really need my permission, Mom. If you want to go on a date with John and get to know him, I'm cool with it."
                m "Thank you."
            "Against it":
                scene 10_1230 with Dissolve(1)
                mc "I think... *Sigh* I don't know... It would feel kinda weird if you guys dated... He's also Iris's dad."
                mc "I mean..."
                m "Honey, it's fine. That's why I asked you. Don't worry about it."
                mc "Sorry."
        scene 10_1231 with Dissolve(1)
        m "Will you go for a test drive now?"
        mc "Yeah, but I'll give John a call first to thank him."
        m "That's a good idea."
        scene 10_1232 with Dissolve(1)
        mc "Thank you again, Mom. This is amazing!"
        m "You're welcome!"
        if Erynn_End == True:
            scene 10_1233 with Dissolve(1)
            mc "Hey, John."
            jo "Hey, [mc]. How are you?"
            mc "Really good! How about you?"
            jo "Heh, I'm good too!"
            scene 10_1234 with Dissolve(1)
            mc "Thank you very much for bringing the bike."
            jo "You're welcome. Happy with it?"
            mc "You have no idea."
            jo "Have you already driven it?"
            mc "Not yet, I came back just now, but I'm about to. I wanted to call you first and thank you."
            scene 10_1235 with Dissolve(1)
            mc "Sorry I wasn't here to thank you personally."
            jo "It's fine. This way it was a bigger surprise, no?"
            mc "Totally. And thank you for the second helmet. I'll come by later and we can have some beers or something."
            jo "Sounds good. I'll be at the garage the whole day."
            scene 10_1245 with Dissolve(1)
            mc "{i}(Let's test this baby out a bit.){/i}"
        else:
            if Erynn_Week3_Monday_Blackmailhelp == False:
                scene 10_1233 with Dissolve(1)
                mc "Hey, John."
                jo "Hey, [mc]. How are you?"
                mc "Really good! How about you?"
                jo "Heh, I'm good too!"
                scene 10_1234 with Dissolve(1)
                mc "Thank you very much for bringing the bike."
                jo "You're welcome. Happy with it?"
                mc "You have no idea."
                jo "Have you already driven it?"
                mc "Not yet, I came back just now, but I'm about to. I wanted to call you first and thank you."
                scene 10_1235 with Dissolve(1)
                mc "Sorry I wasn't here to thank you personally."
                jo "It's fine. This way it was a bigger surprise, no?"
                mc "Totally. And thank you for the second helmet. I'll come by later and we can have some beers or something."
                jo "Sounds good. I'll be at the garage the whole day."
                scene 10_1245 with Dissolve(1)
                mc "{i}(Let's test this baby out a bit.){/i}"
            else:
                scene black with Dissolve(1)
                pause 2
                scene 10_1245 with Dissolve(1)
                mc "{i}(Let's test this baby out a bit.){/i}"
                mc "{i}(I should also talk to Erynn before I head to the restaurant.){/i}"
                er "Hey!"
                scene black with Dissolve(1)
                transform moveup:
                    xalign 0.5 yalign 1.0
                    linear 5.0 yalign 0.0
                show 10_1246 at moveup
                pause 3
                mc "Speak of the devil!"
                er "The devil..."
                mc "Hehe. Hey, Erynn."
                scene 10_1247 with Dissolve(1)
                mc "How are you?"
                er "I'm good. You?"
                mc "Same. Did you have fun yesterday with Alexis?"
                er "We did."
                mc "{i}(Why does she always smell so good?){/i}"
                scene 10_1248 with Dissolve(1)
                er "So, what's with the motorcycle?"
                mc "It's mine."
                er "It is?"
                mc "Mm-hmm. Mom bought it for me as a belated birthday gift."
                scene 10_1249 with Dissolve(1)
                er "Oh... I haven't gotten you anything either..."
                mc "Heh, it's fine, Erynn. I..."
                er "No!"
                scene 10_1250 with Dissolve(1)
                er "Is there anything in particular you want?"
                if Erynn_LikeMC == True:
                    mc "{i}(There's one thing I've wanted for so long, but I can't ask you for that.){/i}"
                else:
                    pass
                mc "Hmm... Not really. I'll have to think about it."
                er "I'll find something."
                scene 10_1251 with Dissolve(1)
                er "This will have to do for now."
                mc "Haha, thanks."
                scene 10_1252 with Dissolve(1)
                er "Have you driven it yet?"
                mc "I was about to."
                menu:
                    "Talk about John":
                        mc "But since you're here now, there's something else I need to talk to you about."
                        er "Okay."
                        mc "Let's go inside."
                    "Offer a ride[KoGa3AutoWTChange1]{size=-4}(Erynn Week4 Sunday OfferBikeRide, Erynn Points+2) {/size} {/color}":
                        $ Erynn_Week4_Sunday_OfferBikeRide = True
                        $ Erynn_Points += 2
                        # Erynn (46)
                        mc "Have you ever been on a motorcycle before?"
                        er "Not yet, no."
                        scene 10_1253 with Dissolve(1)
                        mc "Well... Go ahead. Test it out."
                        er "You sure?"
                        mc "Yes!"
                        scene 10_1254 with Dissolve(1)
                        er "This is more comfortable than I thought it would be."
                        mc "That's not how you sit on a bike!"
                        er "No?"
                        mc "{i}(She actually reminds me of Iris.){/i}"
                        mc "Maybe if you're in a photo shoot for a bike magazine..."
                        scene 10_1255 with Dissolve(1)
                        er "*Whispers* I might have an idea for your birthday present."
                        mc "What?"
                        er "Nothing. I was just thinking out loud."
                        scene 10_1256 with Dissolve(1)
                        mc "Now go sit on it properly!"
                        er "Like this?"
                        mc "Yes."
                        scene 10_1257 with Dissolve(1)
                        er "How do you turn it on? Just like a car?"
                        mc "Why? You're going to steal my bike?"
                        er "Maybe... Haha, no. I have no idea how to drive this anyway. I just want to know what it feels like."
                        er "Can you show me?"
                        scene 10_1258 with Dissolve(1)
                        mc "You can turn the key..."
                        er "It won't just go when I turn it, right?"
                        mc "No, it won't. Don't worry."
                        er "Can you do it, please? I'm a little scared, actually."
                        scene 10_1259 with Dissolve(1)
                        mc "So, what you do is, you turn the key. And now you see this green light? That means it's in neutral. It won't start when it's in gear. There are several safety measures."
                        mc "The killswitch here needs to be down. You'll hold your clutch and push the ignition button here."
                        mc "Ready?"
                        scene 10_1260 with Dissolve(1)
                        mc "Erynn?"
                        er "What?"
                        mc "Ready to start the bike?"
                        er "Uh, yes... Ready..."
                        scene 10_1261 with Dissolve(1)
                        er "Aah..."
                        mc "Haha. What do you think?"
                        er "Uhm, I don't know. It's way different from what I expected. I thought it would vibrate more."
                        scene 10_1262 with Dissolve(1)
                        mc "There are other things for that."
                        er "*Shakes head* ..."
                        er "I didn't mean it like that!"
                        mc "Haha."
                        scene 10_1263 with Dissolve(1)
                        mc "Want to go for a ride?"
                        er "I can't drive this. And don't you need a special license?"
                        mc "I'll be the one driving. You'll be sitting on the back."
                        er "Oh..."
                        scene 10_1264 with Dissolve(1)
                        er "Then yes. I'd love to."
                        mc "Great."
                        er "You've done this before, right?"
                        mc "Having someone on the back? Yeah, many times."
                        scene 10_1265 with Dissolve(1)
                        er "Many times? With who?"
                        mc "Friends..."
                        er "Mm-hmm..."
                        scene 10_1266 with Dissolve(1)
                        mc "Here you go, you'll need this."
                        er "Thanks. Do I have to change clothes, too?"
                        mc "No, it'll be fine. We'll just drive up and down the street here."
                        scene 10_1267 with Dissolve(1)
                        er "Hmm..."
                        mc "What?"
                        er "The red doesn't really fit with my outfit..."
                        mc "*Shakes head* Really Erynn? That's what you're worried about? It's on your head. You won't even see it... Want the black one instead?"
                        er "Yes, please."
                        scene 10_1268 with Dissolve(1)
                        mc "I'll help you with the straps."
                        er "Thanks."
                        scene 10_1269 with Dissolve(1)
                        mc "Hold on tight, okay? Especially when I accelerate."
                        mc "Just lean onto my back."
                        er "Like this?"
                        mc "Even more."
                        mc "{i}(I'm enjoying this way too much.){/i}"
                        scene 10_1270 with Dissolve(1)
                        mc "Ready?"
                        er "[mc], I'm scared!"
                        mc "Scared or nervous?"
                        er "Both!"
                        mc "Do you trust me?"
                        er "I do."
                        scene 10_1271 with Dissolve(1)
                        mc "Open your eyes."
                        er "How do you even know they are closed?"
                        mc "I had a feeling."
                        mc "{i}(This bike is amazing...){/i}"
                        mc "{i}(I really want to drive a bit faster, but with Erynn on it...){/i}"
                        menu:
                            "Keep driving slow":
                                scene 10_1274 with Dissolve(1)
                                ""
                                scene black with Dissolve(1)
                                pause 2
                                scene 10_1275 with Dissolve(1)
                                mc "Haha. Your hair looks so messy now."
                                er "Haha. Doesn't matter."
                                mc "Did you enjoy it?"
                                er "Actually yes. More than I thought."
                            "Speed up":
                                scene 10_1272 with Dissolve(1)
                                mc "Hold on tight. I'll speed up!"
                                er "What? [mc]!"
                                scene 10_1273 with Dissolve(1)
                                er "AAAH!"
                                mc "{i}(She's gonna be so mad...){/i}"
                                scene 10_1274 with Dissolve(1)
                                ""
                                scene black with Dissolve(1)
                                pause 2
                                scene 10_1276 with Dissolve(1)
                                er "You promised not to drive so fast!"
                                mc "Haha. Sorry."
                                er "Why are you laughing? This isn't funny!"
                                scene 10_1277 with Dissolve(1)
                                mc "Your hair is so messy right now."
                                er "And whose fault is that?"
                                mc "Haha. I'm sorry, Erynn."
                                er "..."
                                menu:
                                    "Hug her[KoGa3AutoWTChange1]{size=-4}(Erynn Points+2) {/size} {/color}":
                                        $ Erynn_Points += 2
                                        # Erynn (48)
                                        scene 10_1278 with Dissolve(1)
                                        mc "I know, I'm the worst!"
                                        er "No, you're not."
                                        er "It was scary, but... I liked it. Only a little bit though!"
                                        scene 10_1279 with Dissolve(1)
                                        mc "Good!"
                                    "Talk about John":
                                        pass
                        scene 10_1280 with Dissolve(1)
                        mc "Since you're here now, there's something I need to talk to you about."
                        er "Okay?"
                        mc "Let's go inside."
                        er "I'll fix my hair real quick."
                scene black with Dissolve(1)
                pause 2
                scene 10_1286 with Dissolve(1)
                mc "I talked to a friend of mine, and he might be able to help us with uh... your situation."
                er "Oh, you did?"
                mc "His name is John..."
                er "John?"
                mc "Mm-hmm."
                scene 10_1287 with Dissolve(1)
                mc "I've known him for a couple of years. He's a good guy."
                mc "He also lived in Alvarado and coincidentally moved here."
                if MC_Bike == True:
                    mc "He owns a garage and that's where I met him again. He's the one who sold Mom the bike."
                else:
                    mc "He owns a garage and that's where I met him again."
                scene 10_1288 with Dissolve(1)
                er "Uh... Okay. I don't know what to say."
                er "Does he know... about..."
                mc "Yeah, I told him. Sorry. Maybe I should've talked to you first."
                er "No, it's fine."
                mc "It's because I trust him completely, Erynn. He's helped me many times with all kinds of stuff."
                scene 10_1289 with Dissolve(1)
                er "And he agreed to help me?"
                mc "I told him that I need to talk to you first to see if you are comfortable with it."
                mc "If you are, we can go meet with him, and you can talk and get to know him a little."
                mc "Then you can still decide what you want to do."
                scene 10_1290 with Dissolve(1)
                er "Okay."
                mc "Okay?"
                er "I'll meet with him."
                scene 10_1291 with Dissolve(1)
                mc "So, do you have plans for today?"
                er "We're doing this today?"
                mc "If you have time, yes."
                er "Like now?"
                mc "No, in the evening. I have to work at the restaurant first."
                scene 10_1292 with Dissolve(1)
                er "Uhm... Sure."
                er "I'm actually getting nervous now."
                mc "Haha, already?"
                scene 10_1293 with Dissolve(1)
                m "Hey, are you ready? We need to leave."
                mc "I'm good to go. Just have to switch to black pants."
                scene 10_1294 with Dissolve(1)
                er "How are we going to do this then? I'll pick you up at the restaurant once you're done, and we go from there?"
                mc "Sounds good."
                mc "I'll text you beforehand."
                er "Great."
                scene 10_1295 with Dissolve(1)
                er "Thank you so much."
                mc "You're welcome."
                er "I'll see you later, then."
    else:
        $ MC_Bike = False
        scene 10_1205 with Dissolve(1)
        m "Well, uhm... Thanks for getting the groceries."
        mc "No problem."
        m "Can you bring the bedsheets downstairs? I want to do some laundry before we have to go to the restaurant."
        m "And if you have any clothes that need to be washed, bring them, too."
        mc "Okay."
        if Erynn_End == True:
            pass
        else:
            if Erynn_Week3_Monday_Blackmailhelp == True:
                scene black with Dissolve(1)
                pause 2
                scene 10_1281 with Dissolve(1)
                mc "{i}(I hope she'll pick up this time.){/i}"
                mc "..."
                scene 10_1282 with Dissolve(1)
                er "Hey!"
                mc "Heh... Hi."
                er "I had a feeling you'd want to talk."
                scene 10_1283 with Dissolve(1)
                mc "Yeah right. Just hang up!"
                er "You hang up!"
                scene 10_1284 with Dissolve(1)
                er "What are you watching?"
                mc "It's called The Boyz."
                er "Ah, I heard about that. Superheroes, right?"
                mc "More or less, yes."
                scene 10_1285 with Dissolve(1)
                mc "Did you have fun yesterday with Alexis?"
                er "We did. Join us next time!"
                er "Why were you calling me?"
                mc "I need to talk to you about something. Let's sit on the bed."
                scene black with Dissolve(1)
                pause 2
                scene 10_1286 with Dissolve(1)
                mc "I talked to a friend of mine and he might be able to help us with uh... your situation."
                er "Oh, you did?"
                mc "His name is John..."
                er "John?"
                mc "Mm-hmm."
                scene 10_1287 with Dissolve(1)
                mc "I've known him for a couple of years. He's a good guy."
                mc "He also lived in Alvarado and coincidentally moved here."
                mc "He owns a garage and that's where I met him again."
                scene 10_1288 with Dissolve(1)
                er "Uh... Okay. I don't know what to say."
                er "Does he know... about..."
                mc "Yeah, I told him. Sorry. Maybe I should've talked to you first."
                er "No, it's fine."
                mc "It's because I trust him completely, Erynn. He's helped me many times with all kinds of stuff."
                scene 10_1289 with Dissolve(1)
                er "And he agreed to help me?"
                mc "I told him that I need to talk to you first to see if you are comfortable with it."
                mc "If you are, we can go meet with him, and you can talk and get to know him a little."
                mc "Then you can still decide what you want to do."
                scene 10_1290 with Dissolve(1)
                er "Okay."
                mc "Okay?"
                er "I'll meet with him."
                scene 10_1291 with Dissolve(1)
                mc "So, do you have plans for today?"
                er "We're doing this today?"
                mc "If you have time, yes."
                er "Like now?"
                mc "No, in the evening. I have to work at the restaurant first."
                scene 10_1292 with Dissolve(1)
                er "Uhm... Sure."
                er "I'm actually getting nervous now."
                mc "Haha, already?"
                scene 10_1293 with Dissolve(1)
                m "Hey, are you ready? We need to leave."
                mc "I'm good to go. Just have to switch to black pants."
                scene 10_1294 with Dissolve(1)
                er "How are we going to do this then? I'll pick you up at the restaurant once you're done, and we go from there?"
                mc "Sounds good."
                mc "I'll text you beforehand."
                er "Great."
                scene 10_1295 with Dissolve(1)
                er "Thank you so much."
                mc "You're welcome."
                er "I'll see you later, then."
            else:
                pass
    jump Week4_Sunday_Restaurant

label Week4_Sunday_Restaurant:
    scene black with Dissolve(1)
    pause 2
    stop music fadeout 1.0
    play music ("Sounds/Restaurant_Background2.mp3", "Sounds/Restaurant_Background3.mp3", "Sounds/Restaurant_Background.mp3") volume 0.3
    scene 10_1296 with Dissolve(1)
    mc "Where do you need me today?"
    mc "Or can I be behind the bar?"
    m "That's up to Brooke. She'll assign you wherever she needs the most help."
    scene 10_1297 with Dissolve(1)
    mc "Alright. I'm gonna change then."
    m "Thanks for helping out today."
    mc "No problem."
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 10_1299 at moveup
    pause 3
    mc "..."
    mc "Uh."
    scene 10_1298 with Dissolve(1)
    br "[mc]!"
    mc "Sorry, Brooke! I didn't know anyone was in here."
    mc "I'll let you change. Sorry again."
    scene 10_1300 with Dissolve(1)
    br "It's fine, you can stay. It's not as if I'm naked."
    br "You just surprised me."
    scene 10_1301 with Dissolve(1)
    br "How have you been? I haven't seen you in a while."
    mc "I'm good. Busy with school. We were at training camp for a few days."
    br "Training camp? Oh yeah, you're on the track and field team."
    menu:
        "Keep talking":
            br "Must have been fun."
            mc "It was."
            scene 10_1302 with Dissolve(1)
            br "What happens at camp, stays at camp?"
            mc "Haha, something like that."
        "Check her out[KoGa3AutoWTChange1]{size=-4}(Brooke Points-2) {/size} {/color}":
            $ Brooke_Points -= 2
            scene 10_1303 with Dissolve(1)
            br "Must have been fun."
            mc "It was... really nice."
            scene 10_1304 with Dissolve(1)
            br "What happens at camp, stays at camp?"
            mc "Haha, something like that."
    scene 10_1305 with Dissolve(1)
    mc "I hope no one else will stumble in here now and see us both half-naked."
    mc "They might get the wrong impression and another Rachel situation will happen."
    br "Haha, please no."
    scene 10_1306 with Dissolve(1)
    mc "Heard anything from her since?"
    br "No. She can be lying behind a dumpster for all I care..."
    br "She was a total bitch."
    mc "Haha."
    scene black with Dissolve(1)
    pause 2
    scene 10_1307 with Dissolve(1)
    br "You're on spring break now, right?"
    mc "I am."
    br "Lucky you. I miss all those school holidays."
    mc "Especially now. Must be a really busy period."
    br "Spring break is one of 'em, yes."
    scene 10_1308 with Dissolve(1)
    m "Hey, Brooke."
    br "Hey, Emily. How are you?"
    m "I'm good, thank you. How about you?"
    br "Also good, thanks."
    scene 10_1309 with Dissolve(1)
    m "I've told [mc] already that you'll assign him for today."
    br "Will do."
    m "Also, Monique just called and will be a few minutes late. So best start setting up already so we don't fall behind."
    scene 10_1310 with Dissolve(1)
    br "Don't worry. I have the perfect guy for the job."
    br "Right, [mc]."
    mc "Yes, boss!"
    m "Thank you."
    scene 10_1311 with Dissolve(1)
    m "Anyway. I'd better get ready and change too."
    mc "Are you going somewhere?"
    m "Kitchen."
    mc "Oh..."
    m "We're still short a chef, so I'll have to help out a bit more with preparation."
    scene 10_1312 with Dissolve(1)
    m "Have fun, sweethearts."
    br "Thanks, you too, Emily. Once [mc] is done setting up, I'll send him over to cut some vegetables."
    m "Haha, great! Thanks, Brooke!"
    scene 10_1313 with Dissolve(1)
    mc "{i}(Hmm?){/i}"
    scene 10_1314 with Dissolve(1)
    mc "You're enjoying this, huh?"
    br "Mm-hmm."
    mc "You do realise that I might be your boss one day, right?"
    scene 10_1315 with Dissolve(1)
    br "Haha. Hopes and dreams."
    mc "You're laughing now..."
    br "Come on. The tables won't set themselves. Chop-chop."
    mc "*Shakes head*"
    scene black with Dissolve(1)
    pause 2
    scene 10_1316 with Dissolve(1)
    mc "Here you go!"
    x "Thank you very much."
    mc "Enjoy!"
    scene black with Dissolve(1)
    pause 2
    scene 10_1317 with Dissolve(1)
    mc "Two more champagnes for the lovely ladies."
    x "Thank you!"
    scene 10_1318 with Dissolve(1)
    br "*Whisper* Someone is trying hard today for tips."
    mc "*Whisper* It's spring break. I could use some extra cash."
    br "*Whisper* Because of all the girls you'll need to take on dates?"
    mc "Haha."
    scene 10_1319 with Dissolve(1)
    mc "Which day would you prefer?"
    br "Nice..."
    mc "Nice? Is that a Wednesday?"
    br "*Shakes head* Haha."
    scene black with Dissolve(1)
    pause 2
    scene 10_1320 with vpunch
    mc "{i}(Oh no...){/i}"
    mc "{i}(Why here?){/i}"
    mc "{i}(Why today?){/i}"
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 10_1321 at moveup
    pause 3
    mc "..."
    scene 10_1322 with Dissolve(1)
    br "I have the same expression every time I see them."
    mc "What?"
    br "The Monroes. The prettiest family in Madison Springs."
    br "Gene pool jackpot right there."
    scene 10_1323 with Dissolve(1)
    br "They always remind me of the Cullens."
    mc "The Cullens?"
    br "The vampire family from Twilight."
    mc "Oh..."
    scene 10_1324 with Dissolve(1)
    br "Have you seen the movies?"
    mc "I'm ashamed to admit that I have."
    br "Haha. Big fan, huh?"
    mc "The biggest!"
    scene 10_1325 with Dissolve(1)
    mc "Do you think they might be vampires too?"
    br "I'm pretty sure of it, yeah."
    br "Well, I'm gonna seat them. Be right back."
    mc "Don't get bit."
    br "I wish. I wouldn't mind being part of that family!"
    menu:
        "Compliment Brooke[KoGa3AutoWTChange1]{size=-4}(Brooke Points+2) {/size} {/color}":
            $ Brooke_Points += 2
            # Brooke (6)
            scene 10_1326 with Dissolve(1)
            mc "You're already pretty, though."
            br "Haha, thanks."
            br "Immortality sounds pretty nice, though."
        "Say nothing":
            pass
    if Alexis_Dating == True:
        if Layla_Week3_Tuesday_Train == False:
            scene 07_928 with Dissolve(1)
            mc "{i}(Fuck!){/i}"
            mc "{i}(They actually might be.){/i}"
        else:
            pass
    else:
        pass
    scene 10_1327 with Dissolve(1)
    br "Good evening."
    am "Good evening. We have a reservation for Monroe."
    br "Four people?"
    am "Yes. Husband is a little delayed."
    br "If you could follow me, please."
    am "Thank you."
    if Layla_End == True:
        scene 10_1330 with Dissolve(1)
        mc "..."
    else:
        if Alexis_Dating == True:
            scene 10_1329 with Dissolve(1)
            la "Hey."
        else:
            scene 10_1328 with Dissolve(1)
            la "Hey."
    scene 10_1331 with Dissolve(1)
    br "A server will be with you shortly."
    am "Thank you very much."
    if Layla_End == True:
        scene 10_1332 with Dissolve(1)
        la "Can't we go eat somewhere else?"
        am "Why, all of a sudden? You knew we were coming here. Isn't this your favourite restaurant?"
        la "It is but... Just... Because..."
        am "No, we're staying. It's difficult enough to get a reservation here."
        la "Fine..."
    else:
        pass
    scene 10_1333 with Dissolve(1)
    br "You can have the Monroe table."
    mc "Uh..."
    br "Don't be scared. They're really nice and they tip a lot."
    mc "It's not that. I kinda have history with them."
    if Layla_End == True:
        scene 10_1334 with Dissolve(1)
        br "History? As in dating?"
        mc "Mm-hmm..."
        br "Who did you date?"
        mc "Both."
        br "Oh..."
        scene 10_1335 with Dissolve(1)
        br "Wait! Both...? You said both?"
        mc "I didn't know they were sisters, so..."
        br "Oh my... I'm really curious now. I'll take the table then. But you'll have to tell me the story!"
        mc "Thank you, Brooke."
    else:
        scene 10_1336 with Dissolve(1)
        br "Wait... You know them?"
        mc "Mm-hmm... Adriana is the principal of my school. Layla and I share some classes and we're on the track and field team together."
        br "Oh... Wow."
        br "You'll have to tell me the whole story later!"
        scene black with Dissolve(1)
        pause 2
        scene 10_1337 with Dissolve(1)
        mc "Good evening, everyone."
        am "Good evening, [mc]."
        la "Hey!"
        if Alexis_Sex == False:
            a "Hi."
        else:
            pass
        scene 10_1338 with Dissolve(1)
        mc "You all look beautiful today."
        am "Thank you."
        mc "Special occasion?"
        am "Just a day out with the family."
        if Layla_Dating == True:
            scene 10_1339 with Dissolve(1)
            mc "{i}(Damn...){/i}"
            mc "{i}(Are they getting bigger, or am I just imagining things?){/i}"
            scene 10_1340 with Dissolve(1)
            mc "{i}(She knows...){/i}"
        else:
            if Alexis_Dating == True:
                scene 10_1341 with Dissolve(1)
                mc "Here you go."
                mc "*Whisper* You look gorgeous!"
                a "Thanks!"
            else:
                pass
        scene 10_1342 with Dissolve(1)
        am "Part-time job?"
        mc "Hmm, not really. I help out when Mom needs me."
        am "That's sweet of you."
        scene 10_1343 with Dissolve(1)
        am "See, Layla. You could help me out, too, sometimes."
        la "I'm busy most of the time."
        am "Uh-huh. Busy... It's spring break. No school, as far as I know."
        la "Lexi is on spring break too! Why don't you ask her?"
        scene 10_1344 with Dissolve(1)
        a "I work!"
        la "And I have to do school stuff!"
        a "So do I!"
        am "Okay, I'll remind you of that! School stuff..."
        scene 10_1345 with Dissolve(1)
        am "Is Emily here, too?"
        mc "Yes. I can get her if..."
        am "No, no, it's fine. Surely she's busy."
        scene 10_1346 with Dissolve(1)
        mc "Can I start you off with something to drink?"
        am "Yes, please. I'll have a white wine."
        a "I'll take the same, thank you."
        la "Red for me."
        scene 10_1347 with Dissolve(1)
        n "*Bzzzt. Bzzzt*"
        la "Is that Dad?"
        am "Yes."
        la "He's probably calling because he can't make it."
        am "He'd better make it! It's difficult enough to get a reservation here."
        scene 10_1348 with Dissolve(1)
        am "Hey..."
        am "What do you mean you can't make it?"
        am "..."
        am "Of course I'm angry. I told you before you left that this will happen."
        scene 10_1349 with Dissolve(1)
        am "You'd better!"
        am "..."
        am "What? This isn't the kind of restaurant that does takeaway..."
        am "I'll ask. If not I'll text you and you can get a burger or something."
        am "Alright. See you later then. Love you. Bye."
        scene 10_1350 with Dissolve(1)
        la "Told you!"
        am "Well, it's just us girls, then. Girls talk?"
        if Layla_Dating == True:
            la "I'll be right back."
            am "Uhm... Alright."
            scene 10_1351 with Dissolve(1)
            la "Hey."
            mc "Hi, pretty. How are you?"
            la "Heh... Good, thanks. You?"
            mc "Busy, but good."
            la "Haha, yeah. I can see that."
            scene 10_1352 with Dissolve(1)
            la "Been here all day?"
            mc "More or less."
            la "Will you still be able to go running tomorrow?"
            mc "Hehe, I'll be there. But I'll admit. Standing on your feet the whole day is more exhausting than I thought."
            scene 10_1353 with Dissolve(1)
            la "You'll need good shoes for that."
            mc "Yep. I'm not wearing the most practical ones for this job."
            mc "And some of the girls here wear high heels... I don't know how they manage."
            scene 10_1354 with Dissolve(1)
            la "By the way. I saw you!"
            mc "You saw me?"
            la "Don't pretend you don't know what I'm talking about..."
            scene 10_1355 with Dissolve(1)
            la "..."
            scene 10_1356 with Dissolve(1)
            if Layla_Week2_Wednesday_Chichis == True:
                la "You were looking at my chichis..."
            else:
                la "You were looking at my boobs..."
            mc "..."
            scene 10_1357 with Dissolve(1)
            la "See! You're doing it again!"
            mc "You're showing them to me! Of course I'm looking..."
            la "So unprofessional!"
            m "Who's unprofessional?"
            scene 10_1358 with Dissolve(1)
            la "Uh..."
            mc "Hey, Mom."
            la "..."
            scene 10_1359 with Dissolve(1)
            m "What did he do? Do I need to fire him?"
            mc "I didn't do anything..."
            la "No, no... I was just joking..."
            if Emily_Week3_Sunday_DareTell == True:
                scene 10_1360 with Dissolve(1)
                mc "Mom, this is Layla."
                mc "The same Layla who complained about the risotto."
                la "[mc]!"
                scene 10_1363 with Dissolve(1)
                m "Oh yeah, I remember. Kayla, right?"
                la "..."
                la "I'm so sorry, [mc]'s mom! It was a dare and I felt so bad after."
                la "I..."
                scene 10_1364 with Dissolve(1)
                m "Hey, don't worry about it. You were really sweet."
                la "I actually really like the risotto here."
                m "Haha, thank you."
                m "And you can call me Emily."
                scene 10_1365 with Dissolve(1)
                m "I'm gonna say hello to your mom and sister, too."
                m "It's nice to meet you, Layla!"
                la "Nice to meet you too, Emily."
                scene 10_1366 with Dissolve(1)
                la "You have such a nice mom, but you are so mean!"
                mc "Haha, sorry. Couldn't help it."
                la "I was so embarrassed."
                mc "I saw that."
                scene 10_1367 with Dissolve(1)
                mc "I'd better get back to work now and get you those wines."
                la "I expect a very full glass as compensation!"
                mc "Haha. I'll take care of it."
                scene black with Dissolve(1)
                transform moveup:
                    xalign 0.5 yalign 1.0
                    linear 5.0 yalign 0.0
                show 10_1368 at moveup
                pause 3
                mc "Oh, and Layla!"
                la "Hmm?"
                mc "You look really cute!"
            else:
                scene 10_1361 with Dissolve(1)
                mc "Mom, this is Layla. She's also on the track team."
                m "We've seen each other before. But nice to meet you, Layla! I'm Emily."
                la "Nice to meet you too, Emily."
                scene 10_1362 with Dissolve(1)
                m "I'll let you guys talk and I'll say hello to your mom. Don't forget about their drinks though."
                mc "I was just about to get them."
                la "I'll let you work, then."
        scene 10_1369 with Dissolve(1)
        m "Hey, gorgeous!"
        am "Emily! Right back at you."
        scene 10_1370 with Dissolve(1)
        am "It's been a while. How are you?"
        m "I'm good. How are you?"
        am "Good!"
        scene 10_1371 with Dissolve(1)
        m "Let me have a look at you."
        m "Ana! That dress! You look amazing!"
        am "Thank you. But you act like you can't pull this off..."
        am "Come have a seat. You have a little time, yes?"
        scene 10_1372 with Dissolve(1)
        mc "And here's the wine for the ladies."
        am "Thank you very much."
        a "Thank you!"
        scene 10_1373 with Dissolve(1)
        mc "I've got you one too."
        m "Oh, thank you, honey."
        am "Look at that service!"
        m "Make sure to put it on Adriana's tab."
        am "Haha, I heard that!"
        scene 10_1374 with Dissolve(1)
        mc "Have you decided already on the food?"
        am "Since we have the chef here, what do you recommend, Emily?"
        m "The salmon. It's a grilled cajun parmesan salmon with a sun-dried tomato cream sauce and..."
        am "Say no more. Sounds delicious. That's what I'm having."
        scene black with Dissolve(1)
        pause 2
        scene 10_1375 with Dissolve(1)
        m "Anyway, I'd better go check up on the kitchen. Thanks for having me."
        am "Emily, before I forget. Husband couldn't make it and he really enjoys the food here, so he asked if you do takeaway?"
        m "I'm sure we have some containers we can put the food in."
        am "Oh, thank you very much. You're an angel."
        scene 10_1376 with Dissolve(1)
        am "Oh and Emily. How about you come by sometime next week for a coffee?"
        m "Yeah, I'd love that."
        am "I'll give you a call."
        m "Okay. Well, enjoy the rest of your evening. It was lovely to meet you all."
        scene 10_1377 with Dissolve(1)
        a "Ana?"
        am "Haha, yeah. That's what she used to call me back in college. It's a funny story."
        la "Tell us."
        am "Another time."
        la "Oh, come on... Please?"
        am "Fine... Emily was somewhat of a wild child back in the day. A real party girl."
        scene 10_1378 with Dissolve(1)
        am "One night she came to the dorm, drunk... Hammered actually. I still have no idea how she was able to walk or even remember where she needed to go."
        am "She was so confused when she saw me. She kept asking who I was. I said 'I'm your roommate Adriana.'"
        am "'Ana?' 'No, Adriana.' 'That's what I said. Ana...' She passed out soon after."
        am "The next day she couldn't remember any of it but she kept calling me Ana. And it stuck from that point on."
        scene 10_1379 with Dissolve(1)
        la "Can't imagine Emily being a party girl."
        am "Yeah, if you know her now, you wouldn't believe it."
        a "Did you spend lots of time together?"
        am "No. I wasn't that often at the dorm. Maybe that's why she was confused that I was there that night."
        am "I was there if I had to study for exams or if some event was going on. Else I was with grandpa and grandma, taking care of you, Lexi."
    scene black with Dissolve(1)
    pause 2
    scene 10_1380 with Dissolve(1)
    br "Hey. How are you holding up."
    mc "I thought it would slow down after the dinner rush, but no."
    br "That was just the first rush. Mostly there are two. One at six, another at eight."
    mc "Oh man..."
    scene 10_1381 with Dissolve(1)
    br "You'll be fine."
    br "You're doing really good. Proud of you."
    mc "You sound like my mom. But thanks."
    br "Haha."
    if Alexis_Dating == True:
        scene 10_1382 with Dissolve(1)
        a "..."
    else:
        pass
    scene black with Dissolve(1)
    pause 2
    scene 10_1383 with Dissolve(1)
    x "Hey, Pink Nation. It's ya girl Vanessa. And I'm with Kelly today."
    x "Hey guys."
    x "We were hungry, and guess where we are again. Yep. Rue Madison!"
    x "Goat-cheese balls! So excited!"
    scene 10_1384 with Dissolve(1)
    x "And there's something else we're excited about!"
    x "They have a new bartender! Can you see him?"
    x "What do you think, Pink Nation? Hot or Not? Let me know in the comments!"
    scene 10_1385 with Dissolve(1)
    a "*Shakes head*"
    scene 10_1386 with Dissolve(1)
    mc "Good evening."
    x "Hi. Are you new here?"
    mc "Hmm. Sorta? What can I get you?"
    x "We'll have the goat-cheese balls. Two times!"
    mc "Something to drink?"
    x "Surprise us."
    scene 10_1387 with Dissolve(1)
    x "Hey, do you mind being in my vlog?"
    mc "Uh, sure. What's it for?"
    x "I have a YouTube channel where I post stuff."
    x "One more question. Can you take a picture with us? I need one for the thumbnail."
    scene 10_1388 with Dissolve(1)
    ""
    if Alexis_Dating == True:
        scene 10_1389 with Dissolve(1)
        a "..."
        a "Excuse me for a minute."
        scene 10_1390 with Dissolve(1)
        mc "{i}(Ah shit...){/i}"
        mc "{i}(Maybe it wasn't the smartest idea to take a picture with two random girls in front of her.){/i}"
        scene 10_1391 with Dissolve(1)
        mc "Hey. Come here for a second."
        a "Uh..."
        scene 10_1392 with Dissolve(1)
        mc "Are you okay?"
        a "Yeah."
        mc "You looked angry when I took that picture..."
        a "[mc]..."
        mc "Lexi, I'm sorry if..."
        scene 10_1393 with Dissolve(1)
        a "[mc], I'm not angry at you. You didn't do anything wrong."
        a "I was annoyed at myself for getting jealous over a harmless picture."
        scene 10_1394 with Dissolve(1)
        mc "You must like me a whole lot, huh?"
        a "You know the answer to that."
        mc "I like you, too. A whole lot!"
        scene 10_1395 with vpunch
        a "Aaah-ha-ha..."
        mc "You know how difficult it was to stay away from you while you were sitting there."
        a "Haha, sorry. I can give you a reason to come over, then."
        mc "Dropping your knife?"
        a "Haha. For example."
        scene 10_1396 with Dissolve(1)
        ""
        scene 10_1397 with Dissolve(1)
        mc "We keep running into each other."
        mc "I thought I wouldn't see you until tomorrow, but then we met yesterday. Again today. You really are a stalker."
        a "Haha. It's not my fault you show up wherever I go."
        mc "Wanna test it? Let's cancel tomorrow's plans and see if we meet anyway, somehow."
        a "No! We're not cancelling anything. I've been looking forward to tomorrow, so you'd better show up!"
        scene black with Dissolve(1)
        transform moveup:
            xalign 0.5 yalign 1.0
            linear 5.0 yalign 0.0
        show 10_1398 at moveup
        pause 3
        mc "I can't stay away, anyway if you keep looking like this. You look really nice by the way."
        a "Thank you!"
        mc "Haven't seen those clothes on you yet. Are they new?"
        a "Yes. I bought them yesterday while shopping with Erynn."
        scene 10_1399 with Dissolve(1)
        mc "Did you have fun?"
        a "We did. I think we both needed a day like that."
        mc "How is she?"
        scene 10_1400 with Dissolve(1)
        a "She's trying not to show how scared she is by acting like everything is okay. But now that I know what's going on, I can see the difference in her behaviour."
        a "She isn't the fun and lively Erynn she used to be. Well, she's pretending, but... *Sigh* I still can't believe I didn't notice this."
        a "Now she double-checks everything. Is unsure about stuff. Lots of small things she didn't do before."
        a "*Sigh* I hope this will all be over very soon. I can't wait for you to meet the real Erynn again."
        scene 10_1401 with Dissolve(1)
        mc "{i}(The real Erynn...){/i}"
        mc "{i}(I haven't seen that smile in a long time.){/i}"
        mc "{i}(Now that I think about it, her smiles do look forced at times.){/i}"
        mc "{i}(Don't know if she can come back from all that has happened.){/i}"
        if Erynn_Week3_Monday_Blackmailhelp == True:
            scene 10_1402 with Dissolve(1)
            mc "Erynn and I are going to meet a friend of mine who might be able to help us."
            a "Oh, that's great. When are you..."
            mc "Later today."
            a "Give me a call later and tell me how it went."
        else:
            mc "It's a good thing you're friends again. She really needs that."
            a "So do I."
        scene 10_1403 with Dissolve(1)
        a "I'd better go back now, before they start asking questions."
        mc "Yeah, and your food is getting cold."
        a "That too!"
        scene 10_1404 with Dissolve(1)
        ""
        scene 10_1405 with Dissolve(1)
        m "*Shakes head*"
        scene black with Dissolve(1)
        pause 2
        scene 10_1406 with Dissolve(1)
        am "Compliments to the chef, and this is for you."
        mc "Thank you very much."
        mc "I wish you all a lovely evening."
        am "Thank you, [mc]."
        scene 10_1408 with Dissolve(1)
        ""
    else:
        if Layla_End == True:
            pass
        else:
            scene black with Dissolve(1)
            pause 2
            scene 10_1406 with Dissolve(1)
            am "Compliments to the chef, and this is for you."
            mc "Thank you very much."
            mc "I wish you all a lovely evening."
            am "Thank you, [mc]."
            scene 10_1407 with Dissolve(1)
            ""
    scene black with Dissolve(1)
    pause 2
    scene 10_1409 with Dissolve(1)
    br "Hey, you're still here?"
    if Erynn_Week3_Monday_Blackmailhelp == True:
        mc "Waiting for a friend to pick me up."
    else:
        mc "Waiting till Mom's ready."
    mc "You're done for today, too?"
    br "Yep!"
    scene 10_1410 with Dissolve(1)
    mc "I'll let you change. I'll go wait at the bar."
    br "You don't have to leave for me."
    br "You saw me change before, and guess what? Nothing's changed. I still look the same."
    mc "Heh..."
    menu:
        "Go to the bar":
            scene 10_1411 with Dissolve(1)
            mc "Thanks but as I said earlier. I don't want people to get the wrong impression."
            br "Alright. Will you be here tomorrow?"
            mc "Tomorrow, no. Nor on Tuesday. But I think Wednesday. And Thursday for sure."
            br "Okay. See you then. Bye, [mc]."
            mc "Bye, Brooke."
        "Stay":
            mc "{i}(I guess I'll stay then.){/i}"
            scene black with Dissolve(1)
            transform moveup:
                xalign 0.5 yalign 1.0
                linear 5.0 yalign 0.0
            show 10_1412 at moveup
            pause 3
            ""
            scene 10_1413 with Dissolve(1)
            br "Will you be here tomorrow?"
            mc "Tomorrow, no. Nor on Tuesday. But I think Wednesday. And Thursday for sure."
            br "Alright. But Emily will be here?"
            mc "I think so, yes."
            if Brooke_Week2_Saturday_TurnDown == True:
                scene 10_1414 with Dissolve(1)
                mc "What are you doing later? Wanna hang out maybe?"
                br "Sorry. I have another morning shift tomorrow. So I'm gonna go to bed pretty early."
                mc "{i}(Hmm... I thought she might be interested in me, because she doesn't mind me watching her change.){/i}"
                mc "{i}(It's the second time now she's turned me down.){/i}"
                mc "{i}(Maybe she's just tired. Working here all day is exhausting, to be fair.){/i}"
                if Brooke_Points >= 3:
                    scene 10_1415 with Dissolve(1)
                    mc "Another time, then."
                    br "Hmm, sure..."
                else:
                    pass
            else:
                scene 10_1414 with Dissolve(1)
                mc "Got plans for the rest of your evening?"
                br "No. Gonna pack me some food from the kitchen and head home."
                br "I have another morning shift tomorrow. So I'm gonna go to bed pretty early."
                mc "I understand. Working here is exhausting. I'm pretty tired myself."
            scene 10_1416 with Dissolve(1)
            br "Well, I'll see you on Thursday then, or maybe Wednesday."
            mc "Yeah. Bye, Brooke."
            br "Bye [mc]."
    scene black with Dissolve(1)
    pause 2
    if Erynn_End == True:
        scene 10_1417 with Dissolve(1)
        m "Hey."
        mc "Finally finished for today?"
        m "Yeah. Sorry, it took a little while. Ready to leave?"
        mc "Yes!"
        scene 10_1420 with Dissolve(1)
        m "Thanks a lot for today. You were a big help."
        mc "You're welcome."
        m "Want to go grab something to eat?"
        mc "We're at a restaurant!"
        scene 10_1418 with Dissolve(1)
        m "Not here. I'm in the mood for some fries."
        mc "Heh, fries... Yeah, sounds good."
        m "Let's go then."
        jump Week5_Monday_Morning
    else:
        if Erynn_Week3_Monday_Blackmailhelp == False:
            scene 10_1417 with Dissolve(1)
            m "Hey."
            mc "Finally finished for today?"
            m "Yeah. Sorry, it took a little while. Ready to leave?"
            mc "Yes!"
            scene 10_1420 with Dissolve(1)
            m "Thanks a lot for today. You were a big help."
            mc "You're welcome."
            m "Want to go grab something to eat?"
            mc "We're at a restaurant!"
            scene 10_1418 with Dissolve(1)
            m "Not here. I'm in the mood for some fries."
            mc "Heh, fries... Yeah, sounds good."
            m "Let's go then."
            if Alexis_Dating == True:
                scene 10_1419 with Dissolve(1)
                m "So, about Alexis..."
                mc "Nope!"
                m "What? I didn't even ask anything yet."
                mc "Not doing the girlfriend talk."
                m "Oh, so she IS your girlfriend?"
                mc "..."
            else:
                pass
            jump Week5_Monday_Morning
        else:
            scene 10_1417 with Dissolve(1)
            m "Hey."
            mc "Finally ready for today?"
            m "Yeah. Sorry, it took a little while. Ready to leave?"
            mc "You can go. I'm actually waiting for Erynn."
            scene 10_1420 with Dissolve(1)
            m "Oh, she's coming to pick you up?"
            mc "Yeah, we're going to hang out."
            m "That's nice."
            m "I guess I'll see you later, then."
            scene 10_1421 with Dissolve(1)
            m "Bye, honey. And thanks for today."
            mc "You're welcome. Bye, Mom."
            scene black with Dissolve(1)
            pause 2
            scene 10_1422 with Dissolve(1)
            ja "Yo, what's up. Haven't seen you in a while."
            mc "Hey, man. Yeah, busy with school. How are you?"
            ja "Not bad, not bad."
            scene 10_1423 with Dissolve(1)
            ja "Do you like it here so much that you stay even after your shift?"
            mc "No. I'm just waiting for a friend to pick me up."
            ja "Well, if you're waiting for the girl who just showed up, I'll salute you!"
            mc "Hmm?"
            scene black with Dissolve(1)
            transform moveup:
                xalign 0.5 yalign 1.0
                linear 5.0 yalign 0.0
            show 10_1424 at moveup
            pause 3
            mc "{i}(Holy...){/i}"
            scene 10_1425 with Dissolve(1)
            er "Hey!"
            mc "Hey, Erynn."
            scene 10_1426 with Dissolve(1)
            ja "..."
            mc "Haha. Idiot."
            er "What?"
            mc "No, it's nothing."
            scene 10_1427 with Dissolve(1)
            mc "You look nice!"
            er "Yeah, you think? Thank you."
            mc "Come, sit down."
            scene 10_1428 with Dissolve(1)
            mc "Even though you look really good, I don't think it was the right choice to wear white."
            er "Uhm... Where are we going?"
            mc "To a garage. Lots of grease, oil and stuff."
            er "I didn't know that."
            scene 10_1429 with Dissolve(1)
            mc "You'll be fine as long as you don't crouch under the cars."
            er "Haha. Not happening."
            scene 10_1430 with Dissolve(1)
            mc "How are you feeling?"
            er "Good until now. The nervousness is slowly creeping in."
            mc "Hehe. Why don't you have a drink?"
            er "Can't. I have to drive."
            mc "I can drive. So just take a shot or two to calm the nerves. And just an FYI, you have nothing to be nervous about."
            scene 10_1431 with Dissolve(1)
            er "One shot of tequila, please."
            ja "Sure. Can I get you anything, [mc]?"
            mc "I'm good. Just the shot for her."
            scene 10_1432 with Dissolve(1)
            er "*Sigh* Okay... Here we go."
            mc "Haha. What was that?"
            er "I need to concentrate!"
            mc "To take a shot? Haha."
            scene 10_1433 with Dissolve(1)
            mc "{i}(That face she makes...){/i}"
            scene 10_1434 with Dissolve(1)
            er "*Shakes* Aah..."
            mc "You're cracking me up, Erynn..."
            er "What now?"
            mc "Nothing. Ready to leave?"
            er "Mm-hmm."
            jump Week4_Sunday_Erynn_John

label Week4_Sunday_Erynn_John:
    scene black with Dissolve(1)
    pause 2
    stop music fadeout 1.0
    play music "Sounds/Street_Traffic.mp3" volume 0.5
    scene 10_1435 with Dissolve(1)
    mc "You know. If you become a teacher, you..."
    er "When!"
    mc "Huh?"
    er "Not if, when I become a teacher..."
    scene 10_1436 with Dissolve(1)
    mc "WHEN you become a teacher! You won't be able to wear clothes like that, anymore."
    er "Why not? What's wrong with them?"
    mc "You seriously gonna ask me that?"
    scene 10_1437 with Dissolve(1)
    mc "Because no one would be paying attention and they'd all be hoping you'll drop the chalk."
    er "Not everyone's like that."
    mc "The majority is, trust me!"
    mc "{i}(Gabi comes to mind. No one pays attention in her class. It won't be any different when Erynn teaches. Probably even worse.){/i}"
    scene 10_1438 with Dissolve(1)
    er "Would you pay attention if I was teaching your class?"
    mc "I'd pay attention alright."
    er "..."
    er "To the class or me?"
    menu:
        "The class":
            scene 10_1439 with Dissolve(1)
            mc "The class, obviously..."
            er "Mm-hmm..."
            if Nikki_Girlfriend == True:
                mc "{i}(Why did I think she'd say 'obviously' in a snarky way?){/i}"
                mc "{i}(Damn you, Nikki...){/i}"
            else:
                pass
            mc "I told you before. I'm a good student."
        "Both[KoGa3AutoWTChange1]{size=-4}(Erynn Points+2) {/size} {/color}":
            $ Erynn_Points += 2
            # Erynn (50)
            scene 10_1439 with Dissolve(1)
            mc "The class, obviously..."
            er "Mm-hmm..."
            if Nikki_Girlfriend == True:
                mc "{i}(Why did I think she'd say 'obviously' in a snarky way?){/i}"
                mc "{i}(Damn you, Nikki...){/i}"
            else:
                pass
            scene 10_1440 with Dissolve(1)
            mc "But mostly to you."
            er "..."
            mc "Especially WHEN you wear stuff like that!"
            mc "You look really sexy!"
            scene 10_1441 with Dissolve(1)
            er "Thanks!"
    scene 10_1442 with Dissolve(1)
    er "Do you know why I want to become a teacher?"
    mc "Because you enjoyed teaching me back in the day?"
    er "Uhm... Yeah, actually. I had lots of fun."
    scene 10_1443 with Dissolve(1)
    mc "You do realise, as a teacher, you'll have to teach multiple students and not just one, yes?"
    er "Oh really?"
    mc "Uh-huh. I should know since I'm a student, after all. And not every student will be as sweet or good-looking as I am."
    er "..."
    mc "In fact..."
    scene 10_1444 with vpunch
    mc "Hey!"
    scene 10_1445 with Dissolve(1)
    mc "See! That, you can't do as a teacher!"
    mc "Hitting your precious student."
    er "Precious my ass!"
    mc "That I agree on. It is precious!"
    scene 10_1446 with vpunch
    mc "Hey... Really?"
    mc "Not only do you hit students, but also people who compliment your preci..."
    er "[mc]!"
    mc "Haha."
    scene 10_1447 with Dissolve(1)
    mc "Did that drop out of your bag?"
    er "It did. I should've closed it before swinging it."
    mc "Sorry, I didn't see."
    er "It's fine. I've got it."
    menu:
        "Check her out":
            scene 10_1448 with Dissolve(1)
            mc "{i}(Pink...){/i}"
            scene 10_1449 with Dissolve(1)
            er "..."
            mc "What's with that look? Was this some kind of test?"
            mc "Of course, I'm gonna fail and look at your butt if you bend over right in front of me."
            mc "I'm not the one per cent!"
            scene 10_1450 with vpunch
            n "*Slap*"
            er "Aaah..."
            scene 10_1451 with Dissolve(1)
            er "[mc]!"
            mc "I was just fixing your skirt! Your panties were showing!"
            er "You slapped my ass!"
            mc "Haha. Sorry?"
            mc "{i}(She can actually run in those heels and clothes? Damn... I'd better slow down before she falls, though.){/i}"
            scene 10_1452 with Dissolve(1)
            er "Gotcha!"
            er "I thought you were on the track team!"
            mc "Haha."
            scene 10_1453 with Dissolve(1)
            mc "That was impressive, you running in that outfit."
            er "Thanks."
            if Erynn_LikeMC == True:
                scene 10_1454 with Dissolve(1)
                ""
            else:
                pass
            scene 10_1455 with Dissolve(1)
            mc "Alright. Enough playing around."
            mc "Where did you park your car?"
            er "We actually just passed it."
            mc "Heh..."
        "Help her up":
            scene 10_1456 with Dissolve(1)
            mc "I'll help you up."
            er "Thanks."
    scene 10_1457 with Dissolve(1)
    mc "Keys, please."
    er "Don't worry. I can still drive."
    mc "Not gonna happen."
    scene 10_1458 with Dissolve(1)
    er "Here you go."
    mc "Thanks."
    scene 10_1459 with Dissolve(1)
    er "Nggh..."
    mc "What's with you all of a sudden?"
    er "For a moment I forgot about everything, but now I'm getting nervous again."
    scene 10_1460 with Dissolve(1)
    mc "I'm here for you!"
    mc "You'll be okay."
    scene black with Dissolve(1)
    pause 2
    stop music fadeout 1.0
    play music "Sounds/Traffic.mp3" volume 0.5
    scene 10_1461 with Dissolve(1)
    er "So, this John guy. He works at a garage?"
    mc "He owns it, but he's also a mechanic."
    er "For cars?"
    mc "And motorcycles."
    scene 10_1462 with Dissolve(1)
    er "You told me you guys know each other from Alvarado. How did you meet?"
    mc "Uhm..."
    mc "I uh... I dated his daughter."
    scene 10_1463 with Dissolve(1)
    er "Oh..."
    mc "Yeah..."
    mc "{i}(Not sure if I should tell her right now that his daughter is Iris.){/i}"
    mc "{i}(I think we should talk to John first.){/i}"
    scene black with Dissolve(1)
    pause 2
    stop music fadeout 1.0
    play music ("Music/LoFi Upbeat 1.mp3", "Music/LoFi Upbeat 2.mp3", "Music/LoFi Upbeat 3.mp3", "Music/LoFi Upbeat 4.mp3") volume 0.2
    scene 10_1464 with Dissolve(1)
    mc "We're here."
    er "That was quick."
    scene 10_1465 with Dissolve(1)
    mc "How are you feeling?"
    er "Crazy nervous! My heart is beating so fast."
    mc "Maybe you should've taken two shots..."
    er "I don't know if that would've helped."
    menu:
        "Take her hand[KoGa3AutoWTChange1]{size=-4}(Erynn Points+2) {/size} {/color}":
            $ Erynn_Points += 2
            # Erynn (52)
            scene 10_1466 with Dissolve(1)
            mc "Come on. You're creating some weird scenarios in your head."
            mc "Once you've met John, I'm sure you'll relax a bit."
        "Go inside":
            pass
    scene 10_1467 with Dissolve(1)
    ir "Erynn!"
    er "Uh... Iris... Hi."
    ir "You look so pretty!"
    er "Thanks."
    mc "{i}(Maybe I should've said something in the car... But I didn't expect her to be here today.){/i}"
    scene 10_1468 with Dissolve(1)
    ir "I haven't seen you for a while. How are you?"
    er "I'm good. How are you?"
    ir "Really good right now!"
    scene 10_1469 with Dissolve(1)
    er "You work here?"
    ir "Yes. Doing the books."
    er "Oh..."
    scene 10_1470 with Dissolve(1)
    mc "{i}(Heh... The first time I saw Iris, she reminded me of Erynn.){/i}"
    mc "{i}(Now that I see them together, I can see the similarities.){/i}"
    mc "{i}(The high cheekbones and the strong jawline.){/i}"
    scene 10_1471 with Dissolve(1)
    er "I'm so sorry. This is..."
    ir "Hey, handsome!"
    mc "Hi, Iris."
    scene 10_1472 with Dissolve(1)
    er "..."
    scene 10_1473 with Dissolve(1)
    ir "*Whispers* I can't believe you actually brought her here. Thank you!"
    mc "Uh..."
    ir "*Whispers* I'm getting so nervous around her. It's crazy."
    mc "*Whispers* You and nervous? That is crazy!"
    ir "*Whispers* I owe you. Anything you want. Anything!"
    scene 10_1474 with Dissolve(1)
    er "You know each other?"
    er "Wait... She is..."
    ir "Yes, we dated! You didn't tell her?"
    mc "Not yet, because..."
    scene 10_1475 with Dissolve(1)
    er "That means that you're John's daughter?"
    ir "You know my dad?"
    er "Not really."
    scene 10_1476 with Dissolve(1)
    jo "Iris. Can you get me the documents for the 660, please?"
    ir "Yes, getting them now!"
    scene 10_1477 with Dissolve(1)
    ir "Alright, be right back."
    ir "Don't go anywhere, please."
    mc "Hehe, we won't. Go get the documents."
    ir "Be right back!"
    scene 10_1478 with Dissolve(1)
    er "Iris? You dated Iris?"
    mc "Back in Alvarado, yes."
    if Alexis_Dating == True:
        er "Does Alexis know?"
        mc "Yes, I told her."
    else:
        pass
    er "Why didn't you tell me?"
    scene 10_1479 with Dissolve(1)
    mc "Well, it didn't come up until now. I didn't know she lived here until recently."
    mc "And secondly, if I told you beforehand that Iris was John's daughter, you wouldn't have agreed to come here."
    er "Of course not. I can't involve..."
    scene 10_1480 with Dissolve(1)
    mc "Erynn... It's not that we're spoiled for choices here."
    mc "He..."
    er "Let's leave!"
    mc "Erynn..."
    scene 10_1481 with Dissolve(1)
    mc "You know what? Fine!"
    mc "Nothing will change if you keep running away!"
    mc "Let Ethan control you for the rest of your life!"
    mc "I tried..."
    scene 10_1482 with Dissolve(1)
    er "..."
    scene 10_1483 with Dissolve(1)
    er "Don't go!"
    er "I'm sorry. Please don't be angry with me."
    er "I'm sorry, [mc]!"
    scene 10_1484 with Dissolve(1)
    er "I'm scared! I don't like involving others in my mess. Especially, people I'm close with."
    mc "You need to start thinking about yourself, Erynn. Put yourself first for once!"
    mc "Others have a choice if they want to get involved or not."
    mc "So, if they're willing to help. Accept it!"
    scene 10_1485 with Dissolve(1)
    mc "So, please, Erynn!"
    er "..."
    mc "Let's go talk with John, yes?"
    er "Yes."
    er "But give me a moment to collect myself."
    scene black with Dissolve(1)
    pause 2
    scene 10_1486 with Dissolve(1)
    mc "Shall we head inside?"
    er "*Nods*"
    scene 10_1487 with Dissolve(1)
    er "*Whisper* Is that him?"
    mc "Mm-hmm."
    mc "Hey, John!"
    scene 10_1488 with Dissolve(1)
    jo "Hey, [mc]."
    scene 10_1489 with Dissolve(1)
    er "*Whisper* Uh... He looks..."
    mc "*Whisper* What?"
    er "*Whisper* Never mind... It was a stupid thought."
    scene 10_1490 with Dissolve(1)
    jo "Hi. You must be Erynn. I'm John."
    er "Nice to meet you, John."
    jo "Nice to meet you, too."
    scene 10_1491 with Dissolve(1)
    jo "For a second I thought you were someone else."
    jo "You look so much like somebody I used to know a long time ago."
    mc "She must've been really pretty."
    jo "Haha. She was."
    scene 10_1492 with Dissolve(1)
    jo "Hey, how are you?"
    mc "I'm good."
    if MC_Bike == True:
        mc "Thanks again for bringing the bike. It was a huge surprise."
        jo "You're welcome. Just be careful with it."
    else:
        pass
    scene 10_1493 with Dissolve(1)
    jo "Can I get you guys anything to drink?"
    mc "I'm good."
    er "Thank you."
    jo "Nothing? Water, soda, beer..."
    scene 10_1494 with Dissolve(1)
    er "Actually. Sorry... Can I maybe have a beer?"
    jo "Of course."
    jo "I don't have a seating area here, but make yourself comfortable. I'll get the beer."
    scene 10_1495 with Dissolve(1)
    mc "Some more liquid courage?"
    er "Mm-hmm."
    mc "So, first impressions? What do you think of John?"
    er "He's tall... And handsome..."
    scene 10_1496 with Dissolve(1)
    mc "Heh, tall and handsome? I didn't mean his physical appearance."
    er "Oh... Yeah, uhm..."
    mc "{i}(Is she blushing?){/i}"
    er "I mean, he seems like a cool guy. And knowing that Iris is his daughter helps too. He's not just someone random."
    scene 10_1497 with Dissolve(1)
    ir "Here you are! What are you talking about?"
    mc "Someone tall and handsome."
    er "[mc]! No!"
    mc "Haha."
    scene 10_1498 with Dissolve(1)
    ir "You should come to the dorm again so we can hang out. I haven't seen you there in weeks."
    er "Yeah, sorry. I was uh... busy. But after spring break, I'll show up more often."
    ir "Awesome!"
    if Alexis_Dating == True:
        scene 10_1499 with Dissolve(1)
        ir "Speaking of spring break. How about we all spend a day together sometime next week? We could go to the beach or something?"
        ir "[mc] can invite Alexis."
        mc "{i}(The double date... But going to the beach with three hotties... Yes!){/i}"
        mc "{i}(The girl I had a crush on, the girl I dated, and the girl I'm currently dating. What could go wrong?){/i}"
        er "We can do that."
    else:
        scene 10_1499 with Dissolve(1)
        ir "Speaking of spring break. How about we spend a day together sometime next week? We could go to the beach or something?"
        ir "We can invite Alexis, maybe someone else?"
        er "We can do that."
    scene 10_1500 with Dissolve(1)
    ir "Awesome. But first I have to go bikini shopping. I need a new one."
    ir "Can you maybe come with me and help me pick? You have such good taste in clothes."
    er "Sure."
    scene 10_1501 with Dissolve(1)
    ir "You're the best!"
    mc "{i}(Does Erynn realise that Iris is flirting with her?){/i}"
    scene 10_1502 with Dissolve(1)
    jo "I didn't know what you'd like so I picked several choices."
    er "Heh, thank you. I'll take that one."
    jo "Here you go. You sure you don't want one?"
    mc "I'm good. I'm also driving."
    ir "I'll take his then."
    scene 10_1503 with Dissolve(1)
    jo "Are you done with the books?"
    ir "Yes!"
    jo "Then you're done for today and can go home or wherever."
    ir "I'll stay here then and hang with you guys."
    scene 10_1504 with Dissolve(1)
    jo "No. I have to talk to Erynn and [mc]."
    ir "About what?"
    jo "It's a private matter."
    ir "*Sigh*"
    scene 10_1505 with Dissolve(1)
    ir "Alright, alright. I'll leave."
    jo "If you're hungry, I bought pizza. Caprese! Your favourite, right?"
    ir "I'm not hungry! See you later, then."
    jo "Later."
    scene 10_1506 with Dissolve(1)
    ir "Oh and Erynn. I'll call you for our beach date!"
    er "Date...? Uh, okay."
    ir "Bye, guys."
    mc "Later, Iris."
    scene 10_1507 with Dissolve(1)
    jo "I've sent her away because that's the only condition I have."
    jo "She can't get involved."
    er "I don't want her to get involved either."
    mc "She won't."
    jo "Thank you!"
    scene 10_1508 with Dissolve(1)
    jo "[mc] told me the gist of it, but would you mind telling me the whole story?"
    jo "So I'll have a better idea of what's going on."
    er "Yes, of course."
    er "This guy Ethan..."
    scene black with Dissolve(2)
    pause 2
    scene 10_1509 with Dissolve(1)
    ""
    scene black with Dissolve(2)
    pause 2
    scene 10_1510 with Dissolve(1)
    mc "What do you think?"
    jo "Hmm..."
    jo "First I would need a way to meet him without it looking like a set-up."
    mc "Like in a bar or something?"
    scene 10_1511 with Dissolve(1)
    er "There are some places he frequents and I can find out when he's going to be there."
    jo "That would help."
    jo "Let me meet him and see what he's all about and we'll go from there."
    scene 10_1512 with Dissolve(1)
    jo "Are you comfortable with all this? It won't be easy for you. Also with me helping?"
    jo "[mc] knows me, but I'm a total stranger to you and..."
    er "So am I to you. I'm a stranger, and you're still willing to help me."
    er "I trust [mc], and he trusts you."
    jo "Then I'm happy to help however I can."
    scene 10_1513 with Dissolve(1)
    er "Thank you so very much, John!"
    jo "You're welcome!"
    scene 10_1514 with Dissolve(1)
    jo "[mc], can I have a quick word with you?"
    jo "There's something I meant to ask you."
    mc "Sure."
    er "I'll go wait outside."
    scene black with Dissolve(1)
    pause 2
    scene 10_1515 with Dissolve(1)
    mc "Thank you so much, John, for doing this."
    mc "You think this is going to work?"
    jo "This is what I wanted to talk to you about, and I didn't want to say this in front of her and crush all her hopes."
    scene 10_1516 with Dissolve(1)
    jo "To put it bluntly. It's a shit plan."
    mc "Uh... What? I thought..."
    jo "It's not going to have the results you're hoping for."
    scene 10_1517 with Dissolve(1)
    ir "..."
    scene 10_1518 with Dissolve(1)
    jo "I see what you are trying to accomplish, but you don't know how the CEO will react."
    jo "It's a big company, they probably have a good legal department because the fashion industry has always been dodgy."
    jo "It can backfire very easily."
    mc "But what can we do then?"
    scene 10_1519 with Dissolve(1)
    jo "Look. Best case scenario. We can have her stop going on those escort jobs."
    mc "That's something at least."
    jo "It is. But as long as he has that video, he keeps her shackled in some way."
    scene 10_1520 with Dissolve(1)
    jo "I still want to meet the guy and see what he's all about. I'm gonna make some calls, too."
    jo "I know someone who has a better understanding of all these things, and there might be a simpler solution."
    jo "If you can give me a few days..."
    mc "Sure."
    scene 10_1521 with Dissolve(1)
    jo "In the meantime, take care of her."
    mc "I will."
    mc "Thanks, John."
    scene black with Dissolve(1)
    pause 2
    scene 10_1522 with Dissolve(1)
    mc "Alright, we're back."
    er "Hey."
    jo "Sorry about that."
    er "It's fine."
    scene 10_1523 with Dissolve(1)
    jo "It was nice to meet you, Erynn. Even though it wasn't the best of circumstances."
    er "Nice to meet you, John."
    jo "I say take a few days and think about the things we've discussed."
    er "I will. Thank you."
    jo "[mc] and I will stay in contact."
    scene 10_1524 with Dissolve(1)
    mc "You did great! I'm proud of you, Erynn."
    er "Thank you, [mc]. I couldn't have done this without you."
    scene 10_1525 with Dissolve(1)
    ""
    scene 10_1526 with Dissolve(1)
    er "I felt comfortable talking to him for some reason."
    mc "That's good."
    er "Maybe it's because he's similar to you. I can see that you've spent a lot of time around him."
    mc "Heh, yeah."
    er "First I thought he would be your typical tough guy, with all his tattoos..."
    scene 10_1527 with Dissolve(1)
    mc "And now you think he's tall and handsome..."
    er "Well... He is."
    mc "Someone has a crush!"
    er "[mc]!"
    mc "Haha."
    scene black with Dissolve(2)
    pause 2
    stop music fadeout 1.0
    play music ("Music/LoFi Indie 3.mp3", "Music/LoFi Indie 1.mp3", "Music/LoFi Indie 2.mp3") volume 0.2
    scene 10_1528 with vpunch
    mc "Aah... Finally home!"
    mc "This was such a long day..."
    scene 10_1529 with vpunch
    er "*Sigh* Such a long day!"
    mc "..."
    scene 10_1530 with Dissolve(1)
    mc "Yeah? What have you done all day?"
    er "Lots of stuff!"
    mc "Like what?"
    er "Just... Stuff..."
    scene 10_1531 with Dissolve(1)
    mc "Uh-huh... Stuff."
    er "Okay... I'm allowed to have a relaxing day once in a while where I do nothing!"
    mc "Haha. Of course, you are. Nothing wrong or be ashamed about."
    scene 10_1532 with Dissolve(1)
    er "Do you have plans for spring break?"
    if Layla_End == True:
        mc "Nothing specific yet."
    else:
        mc "I'm going running with Layla tomorrow."
        if Alexis_Dating == False:
            er "Like a date?"
            mc "No. We got a training schedule from Coach which we'll need to do."
            er "Oh..."
        else:
            mc "We got a training schedule from Coach which we'll need to do."
            er "Oh..."
            mc "I'm also going on a date with Alexis."
            scene 10_1533 with Dissolve(1)
            er "Oh, what are you doing?"
            mc "Not telling you."
            er "What? Why not?"
            mc "Because you'll tell her."
            er "I wouldn't!"
            scene 10_1534 with Dissolve(1)
            mc "Uh-huh..."
            er "You know what I think? I think you still haven't figured out what to do or where to go. And that's why you aren't telling me!"
            mc "Haha. You got me! I have no idea. I'm probably just gonna wing it."
            er "She's easy-going. So she'll be happy just spending time with you. You'll be fine."
    scene 10_1535 with Dissolve(1)
    mc "Tuesday, you have your photo shoot, right?"
    er "I do. It's for a perfume campaign."
    mc "I'll be watching you, then."
    er "Oh, you're coming?"
    mc "I promised I would!"
    scene 10_1536 with Dissolve(1)
    er "Thank you!"
    scene 10_1537 with Dissolve(1)
    er "Have you ever been to a photo shoot?"
    mc "If school pictures count, yes."
    er "Haha, no school pictures."
    mc "Then no. I can't wait to see you in your element."
    er "Hehe."
    scene 10_1538 with Dissolve(1)
    mc "A perfume campaign... So, it's mostly like this?"
    mc "Holding a small bottle and pretending it smells amazing?"
    er "Haha. Something like that, yes."
    scene 10_1539 with Dissolve(1)
    er "Wait. Let me take a picture of you. I can use that as inspiration on Tuesday."
    mc "Haha. Sure."
    er "Can you do that same pose again, please?"
    scene 10_1540 with Dissolve(1)
    er "Haha..."
    mc "Why are you laughing?"
    er "Haha, I can't..."
    mc "Give me that!"
    scene 10_1541 with Dissolve(1)
    mc "What the fuck!"
    mc "Who is this?"
    er "Haha."
    mc "You're a terrible photographer!"
    er "Now it's the photographer's fault?"
    scene 10_1542 with Dissolve(1)
    mc "This can never be seen! I'll delete it."
    er "No! Please, [mc]..."
    er "Please, please, please... I won't show anyone. Please, don't delete it."
    mc "Fine!"
    scene 10_1543 with Dissolve(1)
    if Alexis_Dating == False:
        er "Haha. I can't get enough of this."
        mc "..."
    else:
        er "Wait till Lexi sees this."
        mc "Hey!"
        er "I'm kidding."
    mc "{i}(She has such a contagious laugh.){/i}"
    mc "How about you show me how it's done then, Miss Model?"
    er "Alright."
    scene 10_1544 with Dissolve(1)
    mc "Can you stop budging around already..."
    er "My boots are uncomfortable sitting like this."
    mc "Now it's the boots' fault... I thought you were a professional!"
    er "Let me take 'em off first."
    menu:
        "Let her do it":
            pass
        "Help her[KoGa3AutoWTChange1]{size=-4}(Erynn Points+2) {/size} {/color}":
            $ Erynn_Points += 2
            # Erynn (54)
            scene 10_1545 with vpunch
            er "Aah..."
            mc "I'll help you."
            menu:
                "Look closer[KoGa3AutoWTChange1]{size=-4}(Erynn Points-4) {/size} {/color}":
                    $ Erynn_Points -= 4
                    scene 10_1546 with Dissolve(1)
                    mc "..."
                "Don't":
                    scene 10_1547 with Dissolve(1)
                    mc "{i}(She really has pretty legs!){/i}"
            scene 10_1548 with Dissolve(1)
            mc "There!"
            er "Thanks..."
    scene 10_1549 with Dissolve(1)
    mc "All good now, or...?"
    er "No, I'm good."
    mc "Actually. That skirt looks pretty uncomfortable as well. Maybe even your shirt. You should..."
    er "Uh-huh. Nice try!"
    mc "Haha. Alright. Gimme your best model expression."
    scene 10_1550 with Dissolve(1)
    mc "{i}(It's so effortless for her.){/i}"
    mc "{i}(Pretty...){/i}"
    mc "..."
    mc "{i}(But let's see how you look after this.){/i}"
    mc "AAAH!"
    scene 10_1551 with vpunch
    er "Aaah..."
    mc "I think we've got a winner."
    scene 10_1552 with Dissolve(1)
    er "[mc]! That's not fair!"
    mc "Haha."
    er "I want to see it!"
    scene 10_1553 with Dissolve(1)
    er "Oh, it's not that bad, actually."
    mc "Now that is not fair! How do you still look cute like this?"
    er "Heh... Do you want to see a funny picture?"
    mc "Yes!"
    scene 10_1554 with Dissolve(1)
    mc "..."
    mc "Why do you have this?"
    er "Haha."
    mc "Where did you get it? Did Mom give it to you?"
    scene 10_1555 with Dissolve(1)
    er "..."
    mc "Where do you think you're going?"
    er "Hehe. Nowhere. Just... The bathroom?"
    mc "Not with that picture you're not!"
    scene 10_1556 with Dissolve(1)
    mc "Give it here!"
    er "No! It's mine!"
    mc "Give me your phone, Erynn!"
    er "EMILY! Help!"
    scene 10_1557 with Dissolve(1)
    mc "Almost... A little more..."
    er "Nooo! [mc]!"
    scene 10_1558 with Dissolve(1)
    mc "Got... It..."
    er "..."
    scene 10_1559 with Dissolve(1)
    mc "..."
    m "Uh..."
    scene 10_1560 with Dissolve(1)
    mc "Mom..."
    m "Sorry, I thought you called me."
    m "Uhm... Carry on?"
    mc "This..."
    scene 10_1561 with Dissolve(1)
    mc "Well... This will be the topic for the next few tea parties."
    er "Haha. Yes!"
    scene 10_1562 with Dissolve(1)
    mc "Here, I'll help you up."
    er "Thanks."
    scene black with Dissolve(1)
    pause 2
    scene 10_1563 with Dissolve(1)
    mc "So... What are we gonna do now?"
    er "Let's continue with our thousand questions game."
    mc "We haven't finished that yet?"
    er "We're at question thirty-seven."
    scene 10_1564 with Dissolve(1)
    mc "What? Only thirty-seven? There's no way... And why are you counting?"
    er "I'm not..."
    mc "Fine. Go ahead."
    scene 10_1565 with Dissolve(1)
    er "So, you and Iris dated?"
    mc "*Sigh* I knew you were gonna ask about that!"
    mc "Yes, we dated!"
    er "For how long? And how did you meet?"
    scene 10_1566 with Dissolve(1)
    mc "Nuh-uh... One question, remember? My turn."
    er "That's so stupid! Let's change the rules."
    mc "Now it's stupid and you want to change it... No!"
    scene black with Dissolve(1)
    pause 2
    scene 10_1567 with Dissolve(1)
    mc "..."
    mc "{i}(She fell asleep again?){/i}"
    scene 10_1568 with Dissolve(1)
    mc "Erynn?"
    er "Hmm?"
    mc "Tired, or am I so boring that you fall asleep every time you're with me?"
    er "You're not boring!"
    scene 10_1569 with Dissolve(1)
    er "What time is it?"
    mc "Half past ten."
    if Nikki_Girlfriend == False:
        if Layla_Dating == False:
            if Erynn_Points >= 39:
                $ Erynn_LikeMC = True
            else:
                pass
        else:
            pass
    else:
        pass
    if Erynn_LikeMC == True:
        jump Week4_Sunday_Erynn_Sleepover
    else:
        er "That late already? Maybe I should go home, then."
        scene 10_1570 with Dissolve(1)
        er "Thank you again for today, [mc]!"
        mc "You're welcome."
        scene 10_1571 with Dissolve(1)
        mc "When do I have to come over on Tuesday?"
        er "I'll come to pick you up. Around ten in the morning."
        mc "Alright. See you then."
        scene 10_1572 with Dissolve(1)
        er "Good night!"
        mc "Night, Erynn."
        jump Week5_Monday_Morning

label Week4_Sunday_Erynn_Sleepover:
    if _in_replay:
        $ Alexis_Dating = False
        $ Nikki_Girlfriend = False
        $ Layla_End = False
    er "That late already?"
    scene 10_1573 with Dissolve(1)
    er "Uhm... [mc]?"
    mc "Hmm?"
    er "Can I sleep here tonight?"
    mc "..."
    scene 10_1574 with Dissolve(1)
    mc "Sure... I guess."
    er "Thanks! Now I don't have to move."
    mc "Well, you'll need to move a little. I'm not going to sleep in these clothes."
    scene 10_1575 with Dissolve(1)
    er "You have something for me?"
    mc "Clothes to sleep in? What do you need? T-shirt and some joggers?"
    er "Just a t-shirt is fine."
    mc "They're in my drawer. Just pick one."
    scene 10_1576 with Dissolve(1)
    er "This drawer here?"
    mc "Yes, the one on the left."
    er "Do you need one too?"
    mc "No, I'm good."
    scene 10_1576a with Dissolve(1)
    mc "..."
    scene 10_1577 with Dissolve(1)
    er "I think you've seen enough for today!"
    mc "Today?"
    er "..."
    er "You can turn around now!"
    scene 10_1578 with Dissolve(1)
    mc "You know we have a bathroom, right? In fact, we have two!"
    er "I know."
    mc "..."
    menu:
        "Wait until she's ready":
            pass
        "Peek":
            scene black with Dissolve(1)
            transform moveup:
                xalign 0.5 yalign 1.0
                linear 5.0 yalign 0.0
            show 10_1579 at moveup
            pause 3
            mc "{i}(What an incredible body...){/i}"
            mc "{i}(She's so beautiful.){/i}"
    scene black with Dissolve(1)
    pause 2
    scene 10_1580 with Dissolve(1)
    er "I'm ready. You can turn around again."
    mc "Oh, you picked that one."
    mc "{i}(Why do girls always look so cute in guys' clothes?){/i}"
    scene 10_1581 with Dissolve(1)
    if Nikki_Girlfriend == False:
        er "The fabric is thin and soft. Feels nice."
        mc "Yeah, it's one of my favourites."
        mc "{i}(Now even more so.){/i}"
    else:
        er "I was looking for the one I got you before, but didn't see it."
        mc "{i}(That's because Nikki ripped it. But I can't tell her that.){/i}"
        mc "It's probably in the laundry basket."
    scene 10_1582 with Dissolve(1)
    er "What side do you prefer?"
    mc "Doesn't matter to me. I move around so much when I sleep, who knows where I'll end up."
    er "I remember that. I'll take the window side then."
    scene 10_1583 with Dissolve(1)
    mc "When was the last time you slept in my room?"
    er "Hmm... Six, maybe seven years ago I think."
    er "It was a few days after you got this bed."
    mc "You even remember that, huh?"
    scene 10_1584 with Dissolve(1)
    er "How can I forget? That was the night you..."
    mc "I what?"
    er "Never mind."
    mc "No, tell me."
    scene 10_1585 with Dissolve(1)
    er "You asked me if you could touch my boobs."
    mc "I asked that?"
    er "Uh-huh. You wanted to know what they felt like."
    mc "And did I?"
    er "Both of 'em."
    scene 10_1586 with Dissolve(1)
    mc "I'm so sorry I did that."
    er "It's fine."
    mc "No, I..."
    scene 10_1587 with Dissolve(1)
    er "You were curious. Besides. It's not like you just grabbed them."
    er "You asked me and I agreed. I could've said no."
    mc "Why didn't you?"
    er "I'd never had a boy touch me before. So I was a little curious myself."
    scene 10_1588 with Dissolve(1)
    mc "I can't believe I did that. What a little perv I was."
    er "Was?"
    mc "Haha. I'm trying, okay?"
    scene 10_1589 with Dissolve(1)
    er "..."
    if Alexis_Dating == True:
        $ Alexis_JealousyPoints += 2
        # Alexis_Jealous (4)
        scene 10_1590 with Dissolve(1)
        er "Good night!"
        mc "Uh... Good night?"
        mc "{i}(That was weird... Did I say something wrong?){/i}"
    else:
        scene 10_1591 with Dissolve(1)
        er "[mc]?"
        mc "Hmm?"
        er "Can I move closer to you?"
        mc "Uh... Sure."
        scene 10_1592 with Dissolve(1)
        er "Thanks."
        mc "No problem."
        scene 10_1593 with Dissolve(1)
        mc "..."
        scene 10_1594 with Dissolve(1)
        mc "If I asked you right now if I could touch your boobs. Would you let me?"
        er "*Nods*"
        scene 10_1595 with Dissolve(1)
        ""
        scene 10_1596 with Dissolve(1)
        ""
        scene 10_1597 with Dissolve(1)
        ""
        scene 10_1598 with Dissolve(1)
        ""
        scene 10_1599 with Dissolve(1)
        mc "They are really soft."
        er "You said the exact same thing back then."
        mc "I was talking about your lips... But your boobs too!"
        er "..."
        mc "{i}(I want to go so much further with her. But... I don't think we're ready yet...){/i}"
        scene 10_1600 with Dissolve(1)
        ""
    scene black with Dissolve(2)
    pause 2
    scene 10_1601 with Dissolve(1)
    ""
    scene 10_1602 with Dissolve(1)
    er "..."
    scene 10_1603 with vpunch
    n "*Slap*"
    mc "Aaah..."
    if Layla_End == True:
        mc "What was that for?"
        er "No reason. I just wanted to!"
    else:
        er "Didn't you have to wake up early to go running?"
        scene 10_1604 with Dissolve(1)
        mc "Oh, shit..."
        mc "Thanks!"
        er "Hehe, you're welcome."
    scene 10_1605 with Dissolve(1)
    er "Good morning, by the way."
    mc "Good morning."
    scene 10_1606 with Dissolve(1)
    mc "Did you sleep?"
    er "Really well actually. Maybe I'll sleep here more often."
    if Alexis_Dating == True:
        mc "Fine by me. If Alexis doesn't mind."
        er "She can come, too!"
        mc "Haha."
    else:
        pass
    if Layla_End == False:
        scene 10_1607 with Dissolve(1)
        mc "Anyway. I'm gonna get ready."
    else:
        er "I think I'll go home now, before Mom starts worrying again."
    mc "What are you going to do today?"
    er "Probably some school assignments, since I don't have much time during the week."
    mc "Yeah, always a good idea to get them done early so you don't have to worry about it for the rest of the vacation."
    er "Exactly."
    scene 10_1608 with Dissolve(1)
    mc "I'll see you Tuesday, then?"
    er "Mm-hmm. I'll come to pick you up. Around ten."
    mc "I'll be ready."
    $ renpy.end_replay()
    jump Week5_Monday_Morning

label Week5_Monday_Morning:
    if Layla_End == True:
        scene black with Dissolve(2)
        pause 2
        scene 10_1816 with Dissolve(1)
        mc "Hmm..."
        mc "{i}(Nothing in the fridge either... What should I eat?){/i}"
        mc "{i}(I can go eat at Dylan's? Or maybe just grab some fast food?){/i}"
        mc "{i}(I guess I'll head to the city and make up my mind there.){/i}"
        if Gabi_End == True:
            jump Week5_Monday_End
        else:
            jump Week5_Monday_Gabi
    else:
        jump Week5_Monday_Layla_Run

label Week5_Monday_Layla_Run:
    scene black with Dissolve(2)
    pause 2
    n "Monday morning, 08:24."
    stop music fadeout 1.0
    play music ("Music/LoFi Upbeat 1.mp3", "Music/LoFi Upbeat 2.mp3", "Music/LoFi Upbeat 3.mp3", "Music/LoFi Upbeat 4.mp3") volume 0.2
    scene 10_1609 with Dissolve(1)
    mc "{i}(Heh... Of course, she's here already.){/i}"
    va "Hey!"
    mc "Hi. Good morning."
    scene 10_1610 with Dissolve(1)
    mc "Now this is funny. We kinda match."
    va "Haha, we do."
    mc "We look like two athletes from the same team."
    va "Well... We are on the same team!"
    mc "True."
    scene 10_1611 with Dissolve(1)
    mc "Have you been waiting here for long?"
    va "No, I actually just arrived myself. I was about to ring the doorbell when I saw you coming around the corner."
    mc "Let's hope Layla is awake! Or else we'll be waiting for a while."
    scene 10_1612 with Dissolve(1)
    mc "Not wearing your beanie today?"
    va "No..."
    mc "Your hair's not moi..."
    va "Don't say it. I'll kick your ass!"
    if Valeria_Week4_Friday_Help == True:
        scene 10_1613 with Dissolve(1)
        mc "Haha. I actually believe you would."
        mc "I saw your kick first hand and it looked painful."
        va "..."
        mc "{i}(How can someone look scary and cute at the same time?){/i}"
    else:
        pass
    if Alexis_Dating == True:
        scene 10_1614 with Dissolve(1)
        a "Hey!"
        mc "Hi..."
        scene 10_1615 with Dissolve(1)
        va "..."
        scene 10_1616 with Dissolve(1)
        a "What are you doing here? I thought we said the afternoon?"
        mc "We're actually waiting for Layla."
        a "We?"
        scene 10_1617 with Dissolve(1)
        va "Hi."
        mc "This is Valeria. She's also on the track team."
        a "Valeria?"
        scene 10_1618 with Dissolve(1)
        a "Oh, hey. It's nice to finally meet you. I've heard so much about you."
        a "I'm Alexis."
        va "Nice to meet you, Alexis."
        scene 10_1619 with Dissolve(1)
        a "You should come over sometime, so we can all hang out together."
        mc "..."
        scene 10_1620 with Dissolve(1)
        a "What's with that disapproving face?"
        mc "You know. If you keep opening the door wearing stuff like this..."
        mc "One day, there will be a creep waiting and..."
        a "Oh, that's no different to today then!"
        scene 10_1621 with Dissolve(1)
        mc "Wow... That's so mean, Lexi..."
        mc "You've only just met her. Valeria is not a creep!"
        a "I'm talking about you, you idiot!"
        va "Haha."
        scene 10_1622 with Dissolve(1)
        la "Sorry, sorry. I'm here now!"
        mc "Hey, Layla."
        va "Good morning, Layla."
        scene 10_1623 with Dissolve(1)
        la "Shall we go to the park, or...?"
        a "What are you doing?"
        la "We're all going running together."
        a "Can I come with you?"
        scene 10_1624 with Dissolve(1)
        la "No, you can't. You'd just slow us down."
        a "Heh..."
        a "I'm pretty sure I've run the same time you have."
        la "Maybe three years ago before you... Never mind. Sorry."
        mc "{i}(Three years ago? Did something happen?){/i}"
        scene 10_1625 with Dissolve(1)
        a "Fine..."
        la "I'm sorry, Lex. I didn't mean it like that."
        a "I know. Have fun! See you later, [mc]."
        mc "Lexi, wait!"
        la "Give me a second. I'll be right back. Lex, I'm sorry!"
        scene 10_1626 with Dissolve(1)
        mc "When I was younger, I always wanted to have a little brother or sister."
        mc "But every time I see siblings fight, I think maybe it's not that bad being an only child."
        va "Heh. But you also miss out on all the good parts of having a sibling."
        mc "True."
        scene 10_1627 with Dissolve(1)
        mc "Did you ever want to have a brother or sister?"
        va "No."
        mc "No? Well, why have two kids if you can have one who is both cute and crazy."
        va "Haha. See, you understand."
        mc "Haha."
        scene 10_1628 with Dissolve(1)
        mc "I'm gonna text Lexi real quick."
        va "Sure. How long have you been together?"
        mc "Not long. A few weeks."
        va "Oh, it's still pretty new, then."
        mc "Yeah."
        scene 10_1629 with Dissolve(1)
        la "Kay, I'm back."
        mc "Everything alright?"
        la "Yeah. I shouldn't have said that. That was so mean."
        mc "Did something happen?"
        la "What? No... It's nothing. Forget it."
    else:
        scene 10_1630 with Dissolve(1)
        la "Heeey..."
        mc "Morning, Layla."
        scene 10_1631 with Dissolve(1)
        mc "How are you?"
        la "I'm good. Still a little tired. Val not here yet?"
        mc "No. So annoying that she always makes us wait, right?"
        la "Maybe she just got held up."
        va "Very funny..."
        scene 10_1632 with Dissolve(1)
        la "Oh hey, Val! Did you just arrive?"
        va "Yeah..."
        la "Perfect timing!"
        mc "Haha."
        va "*Shakes head*"
        if Valeria_Week4_Friday_Help == True:
            mc "{i}(That look! She's gonna kick my ass for sure, now!){/i}"
        else:
            pass
    scene 10_1633 with Dissolve(1)
    mc "Shall we go?"
    la "Hmm..."
    mc "What?"
    scene 10_1634 with Dissolve(1)
    la "Why are you matching? Were we supposed to match?"
    mc "No, it's just a coincidence."
    la "I want to match, too."
    scene 10_1635 with Dissolve(1)
    mc "Well, it doesn't really matter."
    la "No, I'll stick out like a sore thumb. Or look like the enemy."
    mc "What? The enemy...?"
    la "Let me change real quick. Be right back."
    mc "Layla..."
    scene 10_1636 with Dissolve(1)
    mc "Yeah, I'm not even gonna try to understand."
    mc "The enemy...?"
    va "Haha."
    scene black with Dissolve(1)
    pause 2
    scene 10_1637 with Dissolve(1)
    la "This is the only one I found that comes close to those colours."
    la "It's actually Lexi's old jogging gear."
    mc "I think it works. It also has some green in it."
    scene 10_1638 with Dissolve(1)
    la "Val. How about we go shopping after our run?"
    la "We wanted to go to Delta Sport this week anyway, right?"
    va "We can do that."
    la "Cool."
    scene black with Dissolve(2)
    pause 2
    stop music fadeout 1.0
    play music "Sounds/Park.mp3" volume 0.5
    scene 10_1639 with Dissolve(1)
    la "What do you normally do as a warm-up?"
    la "Do you run laps, or do you have a specific routine?"
    va "That depends. Mostly I..."
    scene 10_1640 with Dissolve(1)
    mc "{i}(What a beautiful day...){/i}"
    mc "{i}(We definitely should do this more often.){/i}"
    la "[mc]!"
    scene 10_1641 with Dissolve(1)
    mc "Sorry, what?"
    la "Why are you running back there? Should we slow down a bit?"
    mc "No, it's good. I was just... daydreaming."
    la "Mm-hmm..."
    scene 10_1642 with Dissolve(1)
    la "*Whispers*"
    mc "Hey! What are you whispering about?"
    la "Maybe if you keep up with us, you could hear!"
    menu:
        "Grab Layla[KoGa3AutoWTChange1]{size=-4}(Layla Points+2) {/size} {/color}":
            $ Layla_Points += 2
            # Layla (72)
            scene 10_1643 with vpunch
            la "Aaah..."
            mc "How's this for keeping up?"
            scene 10_1644 with Dissolve(1)
            la "Yay! Let's go!"
            la "Faster, [mc]!"
            mc "{i}(Faster? Are you kidding me?){/i}"
            la "Come on, Val."
            scene 10_1645 with Dissolve(1)
            mc "Oh, man..."
            la "Wait... That's it?"
            mc "Sorry. I didn't expect this to be so difficult."
            if Layla_Dating == True:
                scene 10_1646 with Dissolve(1)
                la "Thanks."
                la "It was only a few seconds, but it was fun while it lasted."
                mc "{i}(Layla... Please never change!){/i}"
            else:
                pass
            scene 10_1650 with Dissolve(1)
            va "Are you alright?"
            mc "Hmm? Yeah. Just a little out of breath."
            va "At least you're all warmed up now."
            mc "For sure."
        "Grab Valeria[KoGa3AutoWTChange1]{size=-4}({i}Valeria Points > 15: Valeria Points+2, Valeria Points-2{/i}, {i}Layla Dating: Layla Points-2{/i}) {/size} {/color}":
            if Valeria_Points >= 15:
                $ Valeria_Points += 2
                # Valeria (22)
            else:
                $ Valeria_Points -= 2
            if Layla_Dating == True:
                $ Layla_Points -= 2
            else:
                pass
            scene 10_1647 with vpunch
            va "Aaah..."
            mc "How's this for keeping up?"
            scene 10_1648 with Dissolve(1)
            va "..."
            la "Faster, [mc]!"
            mc "{i}(Faster? Are you kidding me? I'm the one carrying her...){/i}"
            scene 10_1649 with Dissolve(1)
            mc "Oh shit, sorry... I forgot that you don't like being picked up."
            va "It's fine. It was fun."
            la "You're stopping already?"
            scene 10_1650 with Dissolve(1)
            va "Are you alright?"
            mc "Hmm? Yeah. Just a little out of breath."
            va "At least you're all warmed up now."
            mc "For sure."
        "Keep running":
            pass
    scene black with Dissolve(1)
    pause 2
    scene 10_1651 with Dissolve(1)
    ""
    scene 10_1652 with Dissolve(1)
    ""
    scene 10_1653 with Dissolve(1)
    ""
    scene black with Dissolve(1)
    pause 2
    scene 10_1654 with Dissolve(1)
    mc "{i}(Man... I really should work more on my endurance.){/i}"
    mc "{i}(I can barely keep up with the girls.){/i}"
    scene 10_1655 with Dissolve(1)
    la "*Sigh* It's so unfair!"
    mc "Hmm?"
    la "You improve way too fast, Val..."
    va "You're doing great too though."
    scene 10_1656 with Dissolve(1)
    la "I hate being third fastest on our team. I can live with second, but third..."
    la "That's bronze... And no one likes bronze..."
    mc "Aren't you second?"
    la "No... Tori is faster. She's beaten me more times than I have her."
    if Alexis_Dating == True:
        scene 10_1657 with Dissolve(1)
        la "Dammit... I should've let Lexi join us."
        la "That way I could've beaten her in a race and felt better about myself."
        mc "Haha. Sister of the year right here."
    else:
        pass
    scene 10_1658 with Dissolve(1)
    mc "At least you're second prettiest on the team!"
    la "Second? Who's first? And don't you dare say Tori!"
    menu:
        "Me":
            scene 10_1659 with Dissolve(1)
            mc "Me, obviously..."
            la "What? No!"
            la "I'm prettier than you. Val is way prettier than you."
            mc "Haha. Guess I'm third then. I'm good with third! Still a medal."
            la "An ugly bronze one!"
        "Layla[KoGa3AutoWTChange1]{size=-4}(Week5 Monday Prettiest Layla, Layla Points+2) {/size} {/color}":
            $ Week5_Monday_Prettiest_Layla = True
            $ Layla_Points += 2
            # Layla (74)
            scene 10_1660 with Dissolve(1)
            mc "I'm kidding. Of course, you're gold!"
            la "Thanks... I feel a little better now."
            if Layla_Dating == True:
                scene 10_1661 with Dissolve(1)
                mc "Maybe this will help, too!"
                la "..."
            else:
                pass
        "Valeria[KoGa3AutoWTChange1]{size=-4}(Week5 Monday Prettiest Valeria, Valeria Points+2) {/size} {/color}":
            $ Week5_Monday_Prettiest_Valeria = True
            $ Valeria_Points += 2
            # Valeria (24)
            scene 10_1662 with Dissolve(1)
            mc "Uhm... Val is first."
            va "..."
            la "Yeah, Val is very pretty. I agree with that."
        "Tori[KoGa3AutoWTChange1]{size=-4}(Week5 Monday Prettiest Tori) {/size} {/color}":
            $ Week5_Monday_Prettiest_Tori = True
            scene 10_1663 with Dissolve(1)
            mc "Well... It's Tori."
            la "What? I told you..."
            scene 10_1664 with vpunch
            la "Aaah!"
            mc "Haha. Hey!"
            mc "If you used all this energy during your races, you'd probably be second fastest!"
            la "What did you say? Val, help me kick his ass!"
            mc "Haha. Let her do her stretches!"
    scene 10_1665 with Dissolve(1)
    la "Val, let's go run again tomorrow!"
    va "Uh, sure."
    scene 10_1666 with Dissolve(1)
    la "You're coming too?"
    la "..."
    la "[mc]?"
    scene 10_1667 with Dissolve(1)
    mc "Sorry. What?"
    la "*Whisper* I've caught you again! And don't tell me you were looking at her pants."
    mc "*Whisper* What do you want me to do? Turn around and look away?"
    if Valeria_Points >= 19:
        if Layla_Week4_Thursday_WingmanVal == True:
            la "*Whisper* You should ask her out already!"
            scene 10_1668 with Dissolve(1)
            la "I'll help you."
            mc "I don't need your help."
            la "You'll thank me later!"
        else:
            pass
    else:
        pass
    scene 10_1669 with Dissolve(1)
    va "Okay, I'm done. Sorry, it took so long."
    mc "Don't apologise for that. Do your thing. We have plenty of time."
    mc "Besides, we should've followed your example by doing some stretches instead of lazing on this bench."
    va "Lazing on the bench doesn't sound too bad, either."
    scene 10_1670 with Dissolve(1)
    mc "In that case. Join us in being lazy!"
    va "Haha."
    scene 10_1671 with Dissolve(1)
    mc "So, you guys are going shopping now?"
    la "Aren't you coming with us?"
    mc "Uhm... Sure, I'll join you."
    la "Ready to go?"
    scene 10_1672 with Dissolve(1)
    mc "What are you doing? Are you looking for something?"
    la "Yeah, my hoodie. I can't find it."
    mc "Where did you put it?"
    la "Right here, together with all of our other stuff."
    mc "We'll help you look."
    scene black with Dissolve(1)
    pause 2
    scene 10_1673 with Dissolve(1)
    va "Sorry, Layla. No luck."
    mc "Me neither. Maybe someone stole it?"
    la "I didn't see anyone here. And we were here this whole time."
    mc "We were running some laps, maybe then?"
    scene 10_1674 with Dissolve(1)
    la "But why only take my hoodie? None of the other stuff was taken..."
    mc "Yeah... Weird. Did you have some money in there or something?"
    la "No, nothing..."
    la "I wanted to buy a new one anyway, but still... This sucks!"
    scene 10_1675 with Dissolve(1)
    mc "Here, wear mine in the meantime."
    la "Thank you, [mc]."
    scene 10_1676 with Dissolve(1)
    mc "Let's go shopping and find you a new hoodie, or whatever else you like."
    la "You seem very eager to go shopping with us..."
    mc "What? No..."
    la "Uh-huh. I know what you're thinking about."
    scene black with Dissolve(2)
    pause 2
    stop music fadeout 1.0
    play music ("Sounds/Store1.mp3", "Sounds/Store2.mp3") volume 0.3
    scene 10_1677 with Dissolve(1)
    ""
    scene 10_1678 with Dissolve(1)
    la "I'm gonna have a look around for hoodies."
    la "You can have yours back. Thanks for letting me wear it."
    mc "No problem."
    scene 10_1679 with Dissolve(1)
    va "I'll also look around a bit. Maybe I'll find a bikini I like for when I go to the beach."
    mc "You still haven't gone?"
    va "Not yet. I didn't have time, but I will now during spring break."
    if Layla_Dating == True:
        scene 10_1680 with Dissolve(1)
        la "Elena, [mc], and I are going to the beach this afternoon. You can come too, if you want."
        va "I'd like to but I can't. It's my mom's birthday today, so..."
        la "Oh. Tell her Happy Birthday!"
        va "Thanks. I will."
    else:
        pass
    scene 10_1681 with Dissolve(1)
    la "Val, can you also show me where the leggings you always wear are?"
    va "Yeah, they're back here."
    la "We'll be right back, [mc]."
    mc "No worries. Take your time."
    scene black with Dissolve(1)
    pause 2
    scene 10_1682 with Dissolve(1)
    ""
    if Layla_Dating == True:
        scene 10_1683 with vpunch
        la "Hey!"
        mc "Hey. Found something?"
        la "Uh-huh."
        mc "Show me."
        scene black with Dissolve(1)
        transform moveup:
            xalign 0.5 yalign 1.0
            linear 5.0 yalign 0.0
        show 10_1684 at moveup
        pause 3
        la "What do you think?"
        mc "{i}(Is it weird that I think she looks sexy in a tracksuit?){/i}"
        mc "It looks really good on you, Layla!"
        scene 10_1685 with Dissolve(1)
        mc "Can you turn around? Just to be sure."
        la "Turn around?"
        mc "I need to see if your butt looks good in those pants."
        la "..."
        mc "What? It's important!"
        scene 10_1686 with Dissolve(1)
        la "You want me to bend over, too?"
        mc "Uhm... Sure."
        la "No!"
        mc "Haha, you suggested it. I'm happy with you just turning around."
        scene 10_1687 with Dissolve(1)
        la "So?"
        mc "Uh-huh... I approve. You should definitely buy them."
        scene 10_1688 with Dissolve(1)
        ""
        scene 10_1689 with Dissolve(1)
        la "Now I also match with you."
        mc "Haha. That really bothered you, huh?"
        scene 10_1690 with Dissolve(1)
        la "Well... When I saw you standing next to Val, you looked like this cute couple in matching outfits..."
        mc "It was just a coincidence."
        la "Still..."
        mc "The things you worry about sometimes."
        scene 10_1691 with Dissolve(1)
        mc "But that also makes you cute!"
        la "Haha..."
        scene 10_1692 with Dissolve(1)
        va "That looks so good on you, Layla."
        la "Thank you."
        la "Didn't you find anything?"
        va "Not really, no."
        scene 10_1693 with Dissolve(1)
        la "What about the blue swimsuit you tried on?"
        va "I wasn't too sure about it."
        la "I think it really suited you."
        scene 10_1694 with Dissolve(1)
        mc "What swimsuit? If you need a second opinion, I..."
        la "..."
        mc "Never mind. I trust Layla. If she says it looked great, I'm sure it did."
    else:
        scene 10_1695 with Dissolve(1)
        la "Hey, [mc]. I found this."
        la "Can you take a look and tell me what you think?"
        mc "Sure."
        scene black with Dissolve(1)
        transform moveup:
            xalign 0.5 yalign 1.0
            linear 5.0 yalign 0.0
        show 10_1684 at moveup
        pause 3
        mc "It looks really good on you, Layla!"
        la "Yeah? Thanks."
        mc "Now we somewhat match too."
        la "Hehe. That was the point. I think I'll get this one, then."
        scene 10_1692 with Dissolve(1)
        va "That looks so good on you, Layla."
        la "Thank you."
        la "Didn't you find anything?"
        va "Not really, no."
        scene 10_1693 with Dissolve(1)
        la "What about the blue swimsuit you tried on?"
        va "I wasn't too sure about it."
        la "I think it really suited you. You looked so sexy!"
        mc "..."
        mc "{i}(I wish I could've seen it.){/i}"
        scene 10_1696 with Dissolve(1)
        la "What's with that face?"
        mc "What face?"
        la "Uh-huh. I know what you're thinking. You're even blushing."
        mc "I'm not!"
        va "Haha."
    scene 10_1697 with Dissolve(1)
    la "Hey, I have an idea. Since we match now. Why don't we all get the same shoes?"
    mc "Uh..."
    la "No?"
    va "I don't mind."
    mc "Well... I could use some new running shoes. So, yeah why not."
    scene 10_1698 with Dissolve(1)
    la "Cool. Let's see if we can find a pair that we all like."
    if Layla_Dating == False:
        if Valeria_Points >= 19:
            if Tori_Week3_Saturday_TC_Sex == True:
                pass
            else:
                if Gabi_End == False:
                    pass
                else:
                    $ Valeria_LikeMC = True
                    $ Valeria_Week5_Monday_Picture = True
                    play sound "Sounds/Phone_Message.mp3"
                    n "*Bzzzt*"
                    scene 10_1699 with Dissolve(1)
                    mc "..."
                    scene 10_1700 with Dissolve(1)
                    mc "{i}(Fuck me!){/i}"
                    scene 10_1701 with Dissolve(1)
                    mc "{i}(Did she mean to send this to me, or...?){/i}"
                    la "I like this pair here."
                    mc "{i}(Yeah, she did...){/i}"
        else:
            pass
    else:
        pass
    scene 10_1702 with Dissolve(1)
    la "What do you guys think about them?"
    mc "Pink? Uh... I don't know."
    la "How about everyone picks the colour they like most and we pick one from them?"
    va "That's fair."
    scene 10_1703 with Dissolve(1)
    mc "Let's see..."
    mc "Do you have one in mind?"
    va "I'm deciding between two."
    scene 10_1704 with Dissolve(1)
    mc "This one!"
    va "Uh..."
    mc "Haha."
    la "I kinda had a feeling you guys would pick the same one."
    scene 10_1705 with Dissolve(1)
    mc "What was the other one you had in mind? The orange one?"
    va "Yeah. How did you know?"
    mc "The beanie you wear is orange, so I thought you might like orange."
    va "Heh, I do."
    scene 10_1706 with Dissolve(1)
    la "I guess we've picked already."
    mc "If you don't like it, we can..."
    la "No, I like it. I have some clothes in that colour too."
    scene black with Dissolve(1)
    pause 2
    scene 10_1707 with Dissolve(1)
    la "So stupid they didn't have the shoes in all our sizes..."
    mc "Maybe next time. At least you've found a nice hoodie."
    la "Mm-hmm."
    scene 10_1708 with Dissolve(1)
    la "Since when do they have a photo booth here in the mall?"
    va "I don't know. But I've seen it every time I've been here."
    la "Hmm... I've never noticed."
    va "They moved it, though. It was in another corridor before."
    scene 10_1709 with Dissolve(1)
    la "Want to take some pictures? I haven't been in a photo booth in years."
    mc "Let's take a few."
    la "Yay!"
    scene 10_1710 with Dissolve(1)
    la "Come on, Val. You too!"
    va "Is there enough space for three people?"
    la "There's plenty."
    scene 10_1711 with Dissolve(1)
    mc "Plenty, huh?"
    la "Haha. Maybe plenty was... We can make it work!"
    va "I can wait outside."
    la "No! We both just have to sit on your lap, [mc]."
    mc "Sure, that's fine."
    if Valeria_Week5_Monday_Picture == True:
        scene 10_1712 with Dissolve(1)
        mc "..."
    else:
        pass
    scene 10_1713 with Dissolve(1)
    la "Let's see. We have a few options here."
    la "We can have one big picture or four smaller ones. And if we take the smaller ones, we can have four different pictures."
    mc "Easy choice. Take the smaller ones."
    la "Alright. Okay, and what does this do?"
    scene 10_1714 with Dissolve(1)
    la "Aah..."
    va "Haha."
    mc "Turn the lights off, it seems. Good job, Layla. I thought you'd done this before?"
    la "It was a long time ago!"
    scene 10_1715 with Dissolve(1)
    la "Okay... Now it should work."
    la "We have a five-second interval between the pictures."
    la "So, what kind of pictures should we take? A normal one, a funny one, what else?"
    mc "Doesn't matter. Spur of the moment."
    scene 10_1716 with Dissolve(1)
    ""
    scene 10_1717 with Dissolve(1)
    ""
    scene 10_1718 with Dissolve(1)
    la "What now?"
    mc "Uh..."
    la "Fast! We only have three more seconds!"
    mc "Kiss!"
    va "What?"
    scene 10_1719 with Dissolve(1)
    va "..."
    la "..."
    scene 10_1720 with Dissolve(1)
    mc "Haha."
    la "[mc]!"
    mc "Spur of the moment!"
    scene 10_1721 with Dissolve(1)
    la "Here they are."
    mc "That was pretty fast."
    scene 10_1722 with Dissolve(1)
    la "They look great!"
    la "Haha. I look like I'm high or something."
    la "Shall we split them up?"
    scene 10_1723 with Dissolve(1)
    la "Which one do you want, Val?"
    va "It doesn't matter, I..."
    mc "Can I have that one?"
    scene 10_1724 with Dissolve(1)
    la "No! You don't get one. You ruined two pictures."
    mc "What do you mean ruined? The last two are the best ones!"
    mc "And if you don't like 'em, I'll gladly take 'em."
    la "No, I'll keep them."
    if Layla_Dating == True:
        scene 10_1725 with Dissolve(1)
        la "Anyway. This was fun. What shall we do next?"
        va "Sorry, but I need to go home."
        la "Right. Your mom's birthday."
        la "Do you mind if I take all the pictures with me first, so I can cut them at home? I don't want to accidentally rip them. I'll bring them next time."
        va "Sure, that's fine."
        scene 10_1726 with Dissolve(1)
        va "Thanks for inviting me."
        la "Val... Of course. Running together is much more fun than solo, no?"
        va "It is."
        la "I'll call you later, okay?"
        scene 10_1727 with Dissolve(1)
        va "Bye, [mc]!"
        mc "..."
        scene 10_1728 with Dissolve(1)
        la "Hey! Why did he get a kiss and I didn't?"
        mc "Uh? How about you check those 'ruined' pictures again? I think you got the better one!"
        la "Oh, yeah. That's right. Hehe."
        mc "Now you 'hehe'...?"
        va "Haha."
        scene 10_1729 with Dissolve(1)
        va "Bye, guys."
        mc "Bye, Val. See you next time."
        la "Bye-bye."
        scene 10_1730 with Dissolve(1)
        mc "I guess we'll leave too, then."
        la "Mm-hmm."
        menu:
            "Go home":
                scene 10_1731 with Dissolve(1)
                mc "I guess we'll leave too then."
                la "Okay..."
                scene black with Dissolve(2)
                pause 2
                scene 10_1751 with Dissolve(1)
                ""
                scene 10_1752 with Dissolve(1)
                la "Thanks for walking me home."
                mc "You're welcome. I guess I'll see you later, at the beach?"
                la "Same place as last time. I'll text you if anything changes."
                mc "Cool."
                scene 10_1753 with Dissolve(1)
                ""
                jump Week5_Monday_Beach
            "Take more pictures[KoGa3AutoWTChange1]{size=-4}(Layla Week5 Monday Pictures, Layla Points+2) {/size} {/color}":
                $ Layla_Week5_Monday_Pictures = True
                $ Layla_Points += 2
                # Layla (76)
                jump Week5_Monday_Layla_Pictures
    else:
        if Valeria_Week5_Monday_Picture == True:
            scene 10_1725 with Dissolve(1)
            la "Anyway. This was fun. What shall we do next?"
            n "*Bzzzt. Bzzzt*"
            la "Oh, that's me."
            scene 10_1757 with Dissolve(1)
            la "Hey, Mom."
            la "I'm at the mall."
            la "We did train but someone stole my hoodie. That's why we went to the mall to buy a new one."
            scene 10_1758 with Dissolve(1)
            la "I don't know... If I knew, it wouldn't be stolen..."
            la "*Sigh* I'm not. I was just saying that..."
            la "Yes..."
            la "Yeah. Bye!"
            scene 10_1759 with Dissolve(1)
            la "Sorry, I've gotta go."
            la "Val. Do you mind if I take all the pictures with me first, so I can cut them at home? I don't want to accidentally rip them. I'll bring them next time."
            va "Sure, that's fine."
            scene 10_1726 with Dissolve(1)
            la "Bye, Val."
            va "Bye, Layla. See you next time."
            la "I'll call you."
            if Layla_Week4_Thursday_WingmanVal == True:
                scene 10_1760 with Dissolve(1)
                la "Bye, [mc]!"
                la "*Whisper* Go take some more pictures with Val!"
                mc "Heh... Bye, Layla."
            else:
                la "Bye, [mc]."
                mc "Bye!"
            menu:
                "Go home[KoGa3AutoWTChange1]{size=-4}(Valeria LikeMCFalse, Valeria Friends, Valeria Points-6) {/size} {/color}":
                    $ Valeria_LikeMC = False
                    $ Valeria_Friends = True
                    $ Valeria_Points -= 6
                    scene 10_1761 with Dissolve(1)
                    mc "I guess we should go home, too?"
                    mc "You said it's your mom's birthday, right?"
                    va "It is."
                    mc "Well, I don't know if there's a party or something, but have fun."
                    va "Thanks. I'm sure we will."
                    scene 10_1727 with Dissolve(1)
                    va "Bye, [mc]. See you next time, I guess."
                    mc "Yeah. Later, Val."
                    if Alexis_Dating == True:
                        jump Week5_Monday_Alexis
                    else:
                        jump Week5_Monday_End
                "Pictures with Valeria[KoGa3AutoWTChange1]{size=-4}(Valeria Week5 Monday Kiss, Valeria Week5 Monday Photobooth, Valeria Points+2) {/size} {/color}":
                    $ Valeria_Week5_Monday_Kiss = True
                    $ Valeria_Week5_Monday_Photobooth = True
                    $ Valeria_Points += 2
                    # Valeria (26)
                    jump Week5_Monday_Valeria_Photobooth
        else:
            scene 10_1725 with Dissolve(1)
            la "Anyway. This was fun. What shall we do next?"
            n "*Bzzzt. Bzzzt*"
            la "Oh, that's me."
            scene 10_1757 with Dissolve(1)
            la "Hey, Mom."
            la "I'm at the mall."
            la "We did train but someone stole my hoodie. That's why we went to the mall to buy a new one."
            scene 10_1758 with Dissolve(1)
            la "I don't know... If I knew, it wouldn't be stolen..."
            la "*Sigh* I'm not. I was just saying that..."
            la "Yes..."
            la "Yeah. Bye!"
            scene 10_1759 with Dissolve(1)
            la "Sorry, I've gotta go."
            la "Val. Do you mind if I take all the pictures with me first, so I can cut them at home? I don't want to accidentally rip them. I'll bring them next time."
            va "Sure, that's fine."
            scene 10_1726 with Dissolve(1)
            la "Bye, Val."
            va "Bye, Layla. See you next time."
            la "I'll call you."
            scene 10_1761 with Dissolve(1)
            mc "I guess we should go home too?"
            mc "You said it's your mom's birthday, right?"
            va "It is."
            mc "Well, I don't know if there's a party or something, but have fun."
            va "Thanks. I'm sure we will."
            scene 10_1727 with Dissolve(1)
            va "Bye, [mc]. See you next time."
            mc "Yeah. Later, Val."
            if Gabi_End == False:
                scene black with Dissolve(2)
                pause 2
                scene 10_1816 with Dissolve(1)
                mc "Hmm..."
                mc "{i}(Nothing in the fridge either... What should I eat?){/i}"
                mc "{i}(I can go eat at Dylan's? Or maybe just grab some fast food?){/i}"
                mc "{i}(I guess I'll head to the city and make up my mind there.){/i}"
                jump Week5_Monday_Gabi
            else:
                if Alexis_Dating == True:
                    jump Week5_Monday_Alexis
                else:
                    jump Week5_Monday_End

label Week5_Monday_Valeria_Photobooth:
    if _in_replay:
        $ Alexis_Dating = True
    scene 10_1762 with Dissolve(1)
    mc "Now it's just us."
    va "Uh-huh..."
    mc "Hey, since we're here anyway, do you maybe want to take a few more pictures?"
    scene 10_1763 with Dissolve(1)
    va "That's your line? Since we're here..."
    mc "Well... Did it work?"
    va "Sure..."
    mc "Haha."
    scene 10_1764 with Dissolve(1)
    mc "{i}(Heh... She went straight to sitting on my lap again.){/i}"
    mc "{i}(And I'm getting hard... Again...){/i}"
    va "So, what kind of picture were you thinking of?"
    scene 10_1765 with Dissolve(1)
    mc "I liked the picture you sent me earlier."
    mc "You look really good in that swimsuit."
    va "Thank you."
    mc "Why did you send it to me?"
    va "I wanted to see your reaction."
    scene 10_1766 with Dissolve(1)
    mc "I wish I could've seen you wear it. I mean in the store."
    va "You should've come to the dressers then."
    mc "{i}(I don't know if she's joking or being serious.){/i}"
    scene 10_1767 with Dissolve(1)
    mc "Did you take more pictures?"
    va "I've got one more."
    mc "Can I see it?"
    va "*Nods*"
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 10_1768 at moveup
    pause 3
    mc "{i}(Damn...){/i}"
    mc "{i}(If I wasn't hard already, I would be right now!){/i}"
    mc "Val! You're hot!"
    va "Haha, thanks."
    mc "{i}(Didn't mean to say that out loud, but I think she took it as a compliment.){/i}"
    scene 10_1769 with Dissolve(1)
    mc "You should be in that one magazine... What was it called again? The one with the swimsuit edition."
    va "I know which one you mean."
    mc "Seriously, you look so good in it. Covergirl right there."
    va "Haha. Now you're overreacting."
    mc "I'm not!"
    scene 10_1770 with Dissolve(1)
    mc "Why didn't you buy it? You should've bought it..."
    mc "If you don't get it, I will."
    va "..."
    mc "Not for myself, I'm not gonna wear that. But for you."
    scene 10_1771 with Dissolve(1)
    va "I'm sure I can make you wear it."
    mc "I know you can..."
    scene 10_1772 with Dissolve(1)
    ""
    scene 10_1773 with Dissolve(1)
    mc "{i}(I want to kiss her.){/i}"
    mc "{i}(Should I kiss her? Does she want to kiss me?){/i}"
    mc "{i}(Fuck it. I want to!){/i}"
    scene 10_1774 with Dissolve(1)
    mc "..."
    scene 10_1775 with Dissolve(1)
    mc "{i}(She uses lots of tongue... I like it!){/i}"
    scene 10_1776 with Dissolve(1)
    mc "{i}(And then having this amazing ass in my hands...){/i}"
    scene 10_1777 with Dissolve(1)
    mc "..."
    scene 10_1778 with Dissolve(1)
    mc "You really enjoy licking people, huh?"
    va "At training camp was the first time actually. I kinda liked it."
    va "So I thought, why not give it another go."
    va "Don't you like it?"
    scene 10_1779 with Dissolve(1)
    va "Haha, okay..."
    scene 10_1780 with Dissolve(1)
    mc "What are you doing later?"
    va "It's my mom's birthday."
    mc "Oh yeah, right. You said that. Tell her Happy Birthday."
    va "Thanks, I will."
    scene 10_1781 with Dissolve(1)
    mc "What about tomorrow?"
    va "Tomorrow, I don't know yet."
    mc "Wanna hang out then?"
    va "Maybe. I'll call you."
    mc "{i}(Maybe...? I guess I'll take a maybe.){/i}"
    scene 10_1782 with Dissolve(1)
    mc "{i}(Damn, she's so pretty!){/i}"
    mc "I want to kiss you again."
    va "Then stop talking and do it!"
    scene 10_1783 with Dissolve(1)
    ""
    scene black with Dissolve(1)
    pause 2
    scene 10_1784 with Dissolve(1)
    va "We took lots of beautiful pictures..."
    mc "Oh, you still want to take a picture?"
    va "Isn't that why we're in here? Or was this just a tactic to kiss me?"
    mc "Tactic? I'm not the one who sent that sexy swimsuit photo..."
    scene 10_1785 with vpunch
    va "Aaah..."
    va "You keep picking me up..."
    mc "I know. And this time, I'm not sorry!"
    scene 10_1786 with Dissolve(1)
    va "You're not? You do know where my knee is, right?"
    mc "Uh-huh... I can feel it. I'll take my chances."
    va "Brave Sir [mc]..."
    mc "Haha."
    scene 10_1787 with vpunch
    va "[mc]!"
    mc "I needed my other hand free to push the buttons."
    va "You could've put me down first!"
    mc "I could have. I like this more..."
    va "..."
    scene 10_1788 with Dissolve(1)
    mc "One big picture or four small ones?"
    va "You're only getting one!"
    mc "Hehe, okay..."
    scene 10_1789 with Dissolve(1)
    mc "Five seconds... Smile!"
    va "Wait! You're not letting me down first?"
    mc "I only get one picture and I want your butt in it, so no!"
    va "..."
    mc "Two seconds!"
    scene 10_1790 with Dissolve(1)
    mc "Hey!"
    scene 10_1791 with Dissolve(1)
    mc "..."
    va "Haha. It looks great!"
    mc "As compensation, I want your other swimsuit picture!"
    va "I'll think about it."
    scene 10_1792 with Dissolve(1)
    va "Let's do one more before I have to leave."
    mc "One more what? Kiss?"
    va "Picture. Maybe a kiss."
    mc "{i}(That maybe again.){/i}"
    scene black with Dissolve(2)
    pause 2
    stop music fadeout 1.0
    play music ("Music/LoFi Spanish 1.mp3", "Music/LoFi Spanish 2.mp3", "Music/LoFi Spanish 3.mp3") volume 0.2
    scene 10_1794 with Dissolve(1)
    ""
    scene 10_1795 with Dissolve(1)
    x "Hola, cariño."
    va "Hey, mama."
    x "What are you looking at?"
    scene 10_1796 with Dissolve(1)
    x "Oh... Who's this? He's handsome. Boyfriend?"
    va "No. He's a friend."
    x "That's Zach? I pictured him differently when you told me about him."
    va "This is [mc]!"
    scene 10_1797 with Dissolve(1)
    x "Oh, the friend of the friend. Now I get it."
    va "It's not like that!"
    x "Hmm... You look cute together. Do you like him?"
    if Alexis_Dating == True:
        scene 10_1798 with Dissolve(1)
        va "He has a girlfriend."
        x "Some girl's heart will be broken soon."
        va "Mama!"
        x "What? The way he looks at you, he likes you. You must like him too. At least a little?"
        scene 10_1799 with Dissolve(1)
        va "I'm having fun spending time with him, and I'm getting to know him still."
        va "So, I don't know yet."
        va "He's a good kisser though."
        x "You..."
        x "You kissed him while he has a girlfriend? Valeria! *Sigh*"
        scene 10_1800 with Dissolve(1)
        x "Okay, we're cancelling the birthday dinner. I wanna hear all about this."
        va "What? No! It was so difficult to get a reservation."
        va "We can eat and talk there."
        $ renpy.end_replay()
        scene black with Dissolve(2)
        pause 2
        stop music fadeout 1.0
        play music ("Music/LoFi Indie 3.mp3", "Music/LoFi Indie 1.mp3", "Music/LoFi Indie 2.mp3") volume 0.2
        scene 10_1801 with Dissolve(1)
        mc "{i}(I can't believe we kissed...){/i}"
        mc "{i}(That kiss was incredible! I should've asked her out a week ago...){/i}"
        mc "{i}(I need to go do something, or I probably won't stop thinking about this the whole day, now.){/i}"
        scene 10_1802 with Dissolve(1)
        mc "{i}(Oh fuck!){/i}"
        mc "{i}(Alexis...){/i}"
        scene 10_1803 with Dissolve(1)
        mc "{i}(Fuuuuuuck...){/i}"
        mc "{i}(I was so in the moment, I completely forgot about her...){/i}"
        mc "{i}(What have I done?){/i}"
        mc "{i}(We never talked about exclusivity... But she's my girlfriend... Does that mean we're exclusive?){/i}"
        if Nikki_Girlfriend == True:
            mc "{i}(I'm dating Nikki too... I guess not exclusive. If they ever find out... Fuck, I'm screwed){/i}"
        else:
            if Cara_Girlfriend == True:
                mc "{i}(I'm dating Cara too... I guess not exclusive. If they ever find out... Fuck, I'm screwed){/i}"
            else:
                mc "{i}(It does, right? Dating is so confusing...){/i}"
        scene 10_1804 with Dissolve(1)
        mc "{i}(Maybe the thing with Val was just a moment of weakness?){/i}"
        mc "{i}(The talks, the flirting. We just had to get rid of the tension?){/i}"
        mc "{i}(But why do I want to do it again?){/i}"
        mc "{i}(Maybe it's best to cancel the date with Alexis until I sort my feelings out? But she was so happy about today...){/i}"
        menu:
            "Cancel[KoGa3AutoWTChange1]{size=-4}(Alexis Week5 Monday Date Cancel, Alexis Points-10) {/size} {/color}":
                $ Alexis_Week5_Monday_Date_Cancel = True
                $ Alexis_Points -= 10
                mc "{i}(I think it's best to cancel.){/i}"
                mc "{i}(There's just too much stuff going through my mind right now.){/i}"
                scene 10_1805 with Dissolve(1)
                mc "{i}(What do I even say to her?){/i}"
                mc "{i}(I feel so bad about this...){/i}"
                scene 10_1806 with Dissolve(1)
                a "Hey."
                mc "Hi, Lexi."
                a "We'll see each other in like two hours, but you..."
                mc "About that."
                scene 10_1807 with Dissolve(1)
                mc "Something came up and I can't make it today."
                a "Oh..."
                mc "Yeah, I'm sorry."
                a "No, it's fine. We can go another time, I guess."
                scene 10_1808 with Dissolve(1)
                mc "Hmm... That's it actually. I just wanted to let you know..."
                a "Are you okay? Did something happen? You sound a little off."
                mc "No, no... Everything's alright. Don't worry."
                a "Okay... Uhm, can I call you later?"
                mc "Of course."
                scene 10_1809 with Dissolve(1)
                a "Speak to you later, then."
                a "Bye, [mc]."
                mc "Bye, Lexi. And sorry again."
                scene 10_1810 with Dissolve(1)
                la "Hey, Lex."
                a "Oh hey, Layla."
                a "Come here for a second."
                scene 10_1811 with Dissolve(1)
                la "What's up?"
                a "Did something happen? I mean with [mc]."
                la "Today? No. Why?"
                a "He just called and cancelled our date. He sounded a bit off and said that something came up."
                scene 10_1812 with Dissolve(1)
                la "Hmm... Maybe he has to help out at the restaurant. You saw yesterday how busy it was."
                a "Yeah, that makes sense. That's maybe also why he didn't sound too happy."
                a "Is that new by the way?"
                la "Uh-huh. I bought it today because... Wait... Something did happen at the park. Someone stole my hoodie!"
                scene 10_1813 with Dissolve(1)
                a "What?"
                la "Yeah... We were done with our training, about to leave, and poof... Hoodie gone. Who the fuck steals a hoodie, right?"
                la "That's why we went to the mall and I bought this one."
                la "What do you think?"
                a "It looks cute."
                scene 10_1814 with Dissolve(1)
                la "We also took some pictures at a photo booth."
                la "Here take a look at this one here."
                a "Heh..."
                scene 10_1815 with Dissolve(1)
                mc "{i}(That was the right thing to do, right?){/i}"
                mc "*Sigh*"
                mc "{i}(Let's go shower and reset my thoughts, I guess...){/i}"
                jump Week5_Monday_End
            "Go on the date":
                mc "{i}(No... Going out with Alexis might give me the answer I'm looking for.){/i}"
                mc "{i}(Let's go shower and reset my thoughts.){/i}"
                jump Week5_Monday_Alexis
    else:
        scene 10_1799 with Dissolve(1)
        va "I'm having fun spending time with him, and I'm getting to know him still."
        va "So, I don't know yet."
        va "He's a good kisser though."
        x "You..."
        scene 10_1800 with Dissolve(1)
        x "Okay, we're cancelling the birthday dinner. I wanna hear all about this."
        va "What? No! It was so difficult to get a reservation."
        va "We can eat and talk there."
        $ renpy.end_replay()
        jump Week5_Monday_End

label Week5_Monday_Layla_Pictures:
    scene 10_1732 with Dissolve(1)
    mc "How about we take some more pictures?"
    mc "Just the two of us?"
    la "*Nods* Mm-hmm..."
    scene 10_1733 with Dissolve(1)
    la "So, what pictures should we take this time?"
    mc "I have a few ideas."
    scene 10_1734 with Dissolve(1)
    la "Yeah? What's the first one?"
    mc "Spur of the moment!"
    la "I knew you'd say that."
    scene 10_1735 with Dissolve(1)
    ""
    scene 10_1736 with Dissolve(1)
    la "Haha..."
    scene 10_1737 with Dissolve(1)
    ""
    scene 10_1738 with Dissolve(1)
    la "[mc]!"
    mc "Don't forget to smile!"
    scene 10_1739 with Dissolve(1)
    ""
    scene black with Dissolve(1)
    pause 2
    scene 10_1740 with Dissolve(1)
    mc "They turned out great!"
    la "Heh, yeah."
    mc "We look good together!"
    scene 10_1741 with Dissolve(1)
    la "Wait... What is this one?"
    mc "Haha. Best one yet!"
    scene 10_1742 with Dissolve(1)
    mc "I'll keep that one!"
    la "Sure... You can't even recognise who that is."
    mc "I'd recognise this cute butt anywhere."
    la "Hey!"
    scene 10_1743 with Dissolve(1)
    la "I want to take one more picture. The bigger size this time."
    mc "Okay, sure."
    scene 10_1744 with Dissolve(1)
    la "But just me!"
    mc "Oh, you want to go in alone?"
    la "Uh-huh. You have to wait outside. It's a surprise."
    mc "I like surprises."
    la "And no peeking!"
    scene 10_1745 with Dissolve(1)
    la "Seriously, [mc]. Please, no peeking."
    mc "I won't. I promise."
    scene 10_1746 with Dissolve(1)
    mc "{i}(Why do I have to be so curious? I really want to look...){/i}"
    mc "*Sigh*"
    mc "{i}(She's taking her time though. Can't wait to see it.){/i}"
    scene 10_1747 with Dissolve(1)
    mc "Hey. You look all smiley."
    la "Hehe."
    mc "What did you do?"
    la "Not telling you. You'll see it later... Maybe..."
    scene 10_1748 with Dissolve(1)
    mc "Can I have a little sneak peek?"
    la "No."
    mc "The tiniest of peeks?"
    la "Haha. No!"
    mc "..."
    scene 10_1749 with Dissolve(1)
    mc "Shall we go home?"
    la "Mm-hmm."
    mc "So, what kind of picture did you take?"
    la "Not telling you."
    scene 10_1750 with Dissolve(1)
    mc "A sexy picture?"
    la "I'm not saying anything!"
    mc "A really sexy picture?"
    la "Haha."
    scene black with Dissolve(1)
    pause 2
    scene 10_1751 with Dissolve(1)
    ""
    scene 10_1752 with Dissolve(1)
    la "Thanks for walking me home."
    mc "You're welcome. I guess I'll see you later, at the beach?"
    la "Same place as last time. I'll text you if anything changes."
    mc "Cool."
    scene 10_1753 with Dissolve(1)
    ""
    scene 10_1754 with Dissolve(1)
    la "Here. This is for you."
    mc "Uh. Thanks."
    la "See you later, [mc]."
    scene 10_1755 with Dissolve(1)
    mc "..."
    scene 10_1756 with Dissolve(1)
    mc "THANK YOU!"
    la "Haha. Don't show anyone!"
    mc "I won't."
    $ renpy.end_replay()
    jump Week5_Monday_Beach

label Week5_Monday_Gabi:
    scene black with Dissolve(1)
    pause 2
    stop music fadeout 1.0
    play music "Sounds/Street_Traffic.mp3" volume 0.5
    scene 10_1817 with Dissolve(1)
    mc "{i}(What can I get?){/i}"
    mc "{i}(Hamburgers? Pizza? Honey-glazed chicken wings, maybe?){/i}"
    mc "{i}(No. They're too messy to eat... What else?){/i}"
    mc "{i}(Oh... Kebab...){/i}"
    scene 10_1818 with Dissolve(1)
    mc "{i}(Yeah... I haven't eaten kebab in a long time.){/i}"
    mc "{i}(There must be a place somewhere around here that sells kebabs, right?){/i}"
    mc "{i}(Let's see...){/i}"
    scene 10_1819 with vpunch
    mc "..."
    scene 10_1820 with Dissolve(1)
    tr "Can't you watch where..."
    tr "..."
    mc "Gabi..."
    scene 10_1821 with Dissolve(1)
    mc "I'm sorry. That was my fault. I should've been paying attention."
    mc "Are you okay?"
    mc "Let me get those for you."
    scene 10_1822 with Dissolve(1)
    mc "Big shopping spree?"
    tr "Something like that."
    scene 10_1823 with Dissolve(1)
    mc "{i}(Why does she always look so... Sad?){/i}"
    menu:
        "Hand her the bags[KoGa3AutoWTChange1]{size=-4}(Gabi End) {/size} {/color}":
            $ Gabi_End = True
            scene 10_1824 with Dissolve(1)
            mc "Here are your bags."
            tr "Thank you."
            mc "Well, I guess I'll see you again next week. Enjoy spring break, Gabi."
            tr "You too. Bye, [mc]."
            scene 10_1825 with Dissolve(1)
            tr "..."
            if Alexis_Dating == True:
                if Alexis_Week5_Monday_Date_Cancel == False:
                    jump Week5_Monday_Alexis
                else:
                    jump Week5_Monday_End
            else:
                jump Week5_Monday_End
        "Carry the bags for Gabi":
            scene 10_1826 with Dissolve(1)
            mc "I'll help you carry them."
            tr "Thanks."
            mc "Are you here by car, or...?"
            tr "Yes, it's parked a little further up."
            scene 10_1827 with Dissolve(1)
            mc "How is your spring break going so far? Not planning to go somewhere?"
            tr "For you, it might be spring break. For me, it's time to catch up on all the work."
            mc "Heh..."
            tr "Yeah. Enjoy your student life as long as you can!"
            mc "I intend to do so."
            scene 10_1828 with Dissolve(1)
            tr "How about you? Not going anywhere?"
            mc "I've been gone for years. Madison Springs is a vacation for me. Beaches, good clubs, lots of bars... We've got everything here."
            tr "True."
            mc "Are you originally from here?"
            tr "No. Palm City."
            scene 10_1829 with Dissolve(1)
            mc "Ew..."
            tr "What do you mean ew...?"
            mc "You're like the enemy."
            if Layla_Dating == True:
                mc "{i}(Haha. I sound just like Layla. Now I know what she meant before...){/i}"
            else:
                pass
            scene 10_1830 with Dissolve(1)
            tr "Enemy..."
            mc "As in rivals. Basketball. We've been kicking your ass for years now."
            tr "Basketball... Right. We've still got the better beaches though."
            mc "Mierda! Only if you like to hang around all those old people... Or those weirdos with metal detectors."
            scene 10_1831 with Dissolve(1)
            tr "Haha."
            mc "{i}(Wow... This is the first time I've seen her laugh.){/i}"
            mc "{i}(And the actual first time I'm having a conversation with her.){/i}"
            mc "{i}(It's very easy to talk to her, too.){/i}"
            scene 10_1832 with Dissolve(1)
            tr "Were you heading to the beach just now?"
            mc "No. Was looking for some food. Thinking about getting a kebab."
            tr "A kebab?"
            mc "Ya. You don't know what a kebab is? It's this..."
            tr "Of course I know what a kebab is. I like to eat them after a good night out at a club or..."
            scene 10_1833 with Dissolve(1)
            mc "Wait... You're still going to clubs and stuff?"
            tr "Yes! How old do you think I am?"
            mc "Uhm..."
            tr "Don't answer that!"
            scene 10_1834 with Dissolve(1)
            mc "{i}(I don't care how old you are. I think you're freakin' stunning.){/i}"
            mc "{i}(And I can't forget what happened at training camp.){/i}"
            mc "{i}(Does she think about it, or was it just...?){/i}"
            tr "What?"
            mc "Nothing... I was just... No, it's nothing."
            scene 10_1835 with Dissolve(1)
            mc "{i}(Maybe it's for the better.){/i}"
            mc "*Sigh*"
            tr "..."
            scene 10_1836 with Dissolve(1)
            tr "You can put the bags here, in the trunk."
            mc "Sure."
            scene 10_1837 with Dissolve(1)
            tr "Thank you very much, [mc]!"
            mc "You're welcome."
            mc "Well, I guess I'll see you again next week. Enjoy spring break, Gabi."
            tr "You too. Bye, [mc]."
            menu:
                "Leave[KoGa3AutoWTChange1]{size=-4}(Gabi End) {/size} {/color}":
                    $ Gabi_End = True
                    scene 10_1838 with Dissolve(1)
                    tr "..."
                    if Alexis_Dating == True:
                        if Alexis_Week5_Monday_Date_Cancel == False:
                            jump Week5_Monday_Alexis
                        else:
                            jump Week5_Monday_End
                    else:
                        jump Week5_Monday_End
                "Kiss":
                    jump Week5_Monday_Gabi_Home

label Week5_Monday_Gabi_Home:
    if _in_replay:
        $ Layla_Week2_Wednesday_Knows = False
        $ Layla_End = False
        $ Layla_Dating = False
        $ Alexis_Dating = False
        $ MC_SexCounter = 2
        $ SexCounter_Gabi = 2
    $ MC_SexCounter += 1
    $ SexCounter_Gabi += 1
    scene 10_1839 with Dissolve(1)
    tr "..."
    scene 10_1840 with Dissolve(1)
    mc "{i}(Fuck! Why did I do that?){/i}"
    mc "Sorry... I..."
    mc "Uhm... Bye."
    scene black with Dissolve(1)
    pause 2
    scene 10_1841 with Dissolve(1)
    tr "..."
    scene 10_1842 with Dissolve(1)
    tr "*Sigh*"
    scene 10_1843 with Dissolve(1)
    n "*Beep-beep*"
    mc "{i}(Was that for me?){/i}"
    mc "{i}(Did she forget something?){/i}"
    scene 10_1844 with Dissolve(1)
    mc "Hey. Did you for..."
    tr "Get in!"
    mc "You mean...? Okay..."
    scene 10_1845 with Dissolve(1)
    stop music fadeout 1.0
    play music "Sounds/Traffic.mp3" volume 0.5
    mc "..."
    scene 10_1846 with Dissolve(1)
    mc "{i}(Where are we going?){/i}"
    mc "{i}(She looks... not nervous, but...){/i}"
    scene black with Dissolve(1)
    pause 2
    scene 10_1847 with Dissolve(1)
    mc "{i}(She hasn't said a single thing since I got in the car.){/i}"
    mc "{i}(Should I even be in here... With her?){/i}"
    scene 10_1848 with Dissolve(1)
    mc "{i}(This looks like her apartment.){/i}"
    mc "{i}(Are we...?){/i}"
    scene black with Dissolve(1)
    pause 2
    stop music fadeout 1.0
    play music ("Music/LoFi Spanish 1.mp3", "Music/LoFi Spanish 2.mp3", "Music/LoFi Spanish 3.mp3") volume 0.2
    scene 10_1849 with Dissolve(1)
    mc "{i}(I guess I'll just follow her up to carry her bags.){/i}"
    mc "{i}(She still hasn't said anything since I got into her car.){/i}"
    scene 10_1850 with Dissolve(1)
    mc "Uhm, Gabi? Where do you want me to put the bags?"
    tr "Just put them on the small table there."
    tr "Make yourself comfortable. I'll be right back."
    scene 10_1851 with Dissolve(1)
    mc "{i}(Is this the moment when Gabi and her husband show up and...){/i}"
    mc "..."
    mc "{i}(Why did I get in her car?){/i}"
    scene black with Dissolve(1)
    pause 2
    scene 10_1852 with Dissolve(1)
    mc "Oh..."
    mc "{i}(No way...){/i}"
    mc "{i}(That's why I got into her car!){/i}"
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 10_1853 at moveup
    pause 3
    tr "Hey!"
    scene 10_1854 with Dissolve(1)
    mc "{i}(Her body is insane... Fuck...){/i}"
    mc "Bonita."
    scene 10_1855 with Dissolve(1)
    mc "Estás súper guapa, Gabriela!\n(You look super beautiful, Gabriela!)"
    scene 10_1856 with Dissolve(1)
    tr "Gracias!"
    mc "Ay wey!\n(Whoa!)"
    scene 10_1857 with vpunch
    mc "..."
    scene 10_1858 with Dissolve(1)
    tr "Me gusta cuando hablas en español.\n(I like it when you speak in Spanish.)"
    scene 10_1859 with Dissolve(1)
    ""
    scene 10_1860 with Dissolve(1)
    ""
    scene 10_1861 with Dissolve(1)
    tr "..."
    scene 10_1862 with Dissolve(1)
    tr "Ven!"
    mc "{i}(We're going to do it again?){/i}"
    mc "{i}(Fuck, yes!){/i}"
    scene 10_1863 with Dissolve(1)
    mc "Gabi, yo pensaba que ese campamento de entrenamiento era...\n(Gabi, I thought that training camp was...)"
    tr "No hables más!"
    scene 10_1864 with Dissolve(1)
    mc "{i}(No more talking doesn't mean I'm going to stop touching your whole body!){/i}"
    scene 10_1865 with Dissolve(1)
    mc "{i}(I want this so bad!){/i}"
    scene 10_1866 with Dissolve(1)
    mc "..."
    mc "{i}(This feels different than last time.){/i}"
    mc "{i}(Better! So much better!){/i}"
    scene 10_1867 with vpunch
    mc "{i}(Heh.){/i}"
    scene 10_1868 with Dissolve(1)
    mc "{i}(Even though we've had sex twice before.){/i}"
    mc "{i}(This still feels like something forbidden?){/i}"
    mc "{i}(Probably because it actually is, but that makes this even better!){/i}"
    scene 10_1869 with Dissolve(1)
    mc "{i}(This is definitely different!){/i}"
    scene 10_1870 with Dissolve(1)
    ""
    scene 10_1871 with Dissolve(1)
    ""
    scene 10_1872 with Dissolve(1)
    mc "{i}(Maybe a little handjob this time?){/i}"
    mc "{i}(Or is she going to give me a blowjob?){/i}"
    scene 10_1873 with Dissolve(1)
    mc "{i}(I'm going crazy just thinking about it.){/i}"
    mc "{i}(My dick is so hard, it actually hurts...){/i}"
    mc "{i}(Please, Gabi. Put it in your mouth!){/i}"
    scene 10_1874 with Dissolve(1)
    mc "{i}(Fuck!){/i}"
    mc "{i}(Gabi is actually licking my dick... This feels so good!){/i}"
    mc "{i}(And the way she looks at me. Fuck... I'm going crazy...){/i}"
    scene 10_1875 with Dissolve(1)
    mc "..."
    show 10_1876
    ""
    scene 10_1877 with Dissolve(1)
    mc "{i}(This is so amazing.){/i}"
    mc "{i}(Please don't be a dream, and if it is, don't wake up!){/i}"
    scene 10_1878 with Dissolve(1)
    mc "{i}(Yes, show me those amazing tits again.){/i}"
    scene 10_1879 with Dissolve(1)
    mc "{i}(Still amazed how big they are.){/i}"
    scene 10_1880 with Dissolve(1)
    mc "{i}(More than a handful.){/i}"
    scene 10_1881 with Dissolve(1)
    mc "{i}(They feel amazing. Soft but firm.){/i}"
    mc "{i}(I could play with them all day.){/i}"
    mc "{i}(But first...){/i}"
    scene 10_1882 with Dissolve(1)
    tr "Ahh..."
    scene 10_1883 with Dissolve(1)
    mc "{i}(I can feel her nipples stiffen in my mouth!){/i}"
    mc "{i}(So tasty!){/i}"
    scene 10_1884 with Dissolve(1)
    ""
    scene 10_1885 with vpunch
    mc "Hola, chica!"
    tr "Haha. Hola, chico."
    mc "Me toca!\n(My turn!)"
    scene 10_1886 with Dissolve(1)
    ""
    scene 10_1887 with Dissolve(1)
    mc "{i}(I could kiss and lick this body from top to bottom.){/i}"
    mc "{i}(Her juicy ass...){/i}"
    scene black with Dissolve(1)
    pause 2
    scene 10_1888 with Dissolve(1)
    ""
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 10_1889 at moveup
    pause 3
    mc "{i}(Seriously... She's so perfect.){/i}"
    mc "{i}(Her fit body, her big boobs, a thicc ass.){/i}"
    mc "{i}(And this sweet pink pussy!){/i}"
    scene 10_1890 with Dissolve(1)
    mc "{i}(She's so wet already. Feels so warm inside.){/i}"
    mc "{i}(She wants this too. She's just as excited as I am.){/i}"
    scene 10_1891 with Dissolve(1)
    tr "*Moaning*"
    mc "{i}(I don't know if she's holding back, but she has the cutest moans.){/i}"
    mc "{i}(I love this sound.){/i}"
    scene 10_1892 with Dissolve(1)
    ""
    scene 10_1893 with Dissolve(1)
    mc "{i}(She tastes so sweet!){/i}"
    scene black with Dissolve(1)
    pause 2
    scene 10_1894 with Dissolve(1)
    mc "{i}(How will I ever be able to concentrate in her class again after this?){/i}"
    scene 10_1895 with Dissolve(1)
    tr "Aah... Mmm..."
    scene 10_1896 with Dissolve(1)
    mc "{i}(Her pussy feels so good!){/i}"
    show 10_1897
    ""
    show 10_1898
    ""
    scene 10_1899 with Dissolve(1)
    n "*Ding-dong*"
    mc "Are you expecting someone?"
    tr "No... He'll probably leave when no one answers."
    tr "Continue!"
    scene 10_1900 with Dissolve(1)
    ""
    show 10_1901
    n "*Ding-dong*"
    tr "..."
    n "*Ding-dong*"
    scene 10_1902 with Dissolve(1)
    n "*Knock. Knock*"
    tr "Estás bromeando!\n(You've got to be kidding me!)"
    tr "Perdona, voy a ver quién es.\n(I'm sorry. Let me go see who it is.)"
    scene 10_1903 with Dissolve(1)
    tr "Ahora vuelvo.\n(Be right back.)"
    mc "Vuelve rápido, eh!\n(You'd better get back fast!)"
    tr "Heh..."
    mc "{i}(I hope she doesn't open the door like that.){/i}"
    scene black with Dissolve(1)
    pause 2
    scene 10_1904 with vpunch
    tr "Layla?"
    la "Hello."
    mc "{i}(Layla? What's she doing here?){/i}"
    scene 10_1905 with Dissolve(1)
    tr "I forgot we have the tutoring today. I'm so sorry."
    if Layla_Week2_Wednesday_Knows == True:
        mc "{i}(Maybe if I'd tutored her, she wouldn't be here now. That's karma.){/i}"
    else:
        mc "{i}(What? Tutoring? She did great on the last test...){/i}"
    tr "Come on in."
    mc "{i}(What do you mean, come on in? I'm still here! Fuck! Should I go hide?){/i}"
    scene 10_1906 with Dissolve(1)
    tr "Uh... Sorry for my get-up. I was just about to go shower. Give me a minute, I'll change real quick."
    tr "You can sit on the sofa there."
    la "Thanks."
    scene 10_1907 with Dissolve(1)
    mc "What..."
    tr "Shhh!"
    scene 10_1908 with Dissolve(1)
    tr "*Sigh*"
    tr "*Whispers* I completely forgot about this."
    tr "*Whispers* Layla's mom called me yesterday and asked if I can give her some private lessons once or twice during spring break."
    scene 10_1909 with Dissolve(1)
    mc "*Whispers* I guess I'll leave then."
    tr "*Whispers* No! You can't leave while Layla is here. She'll see you when you go downstairs."
    mc "*Whispers* What do you want me to do, then? Stay up here and be quiet until she's gone?"
    tr "*Whispers* Well... Yes!"
    scene 10_1910 with Dissolve(1)
    mc "*Whispers* Seriously?"
    tr "*Whispers* It's better than the risk of getting caught. You know what'll happens if..."
    mc "*Whispers* Can't you distract her for a while and..."
    tr "..."
    mc "*Whispers* No, you're right. *Sigh* How long will she be here?"
    tr "*Whispers* Uhm... One, maybe one and a half hours."
    scene 10_1911 with Dissolve(1)
    mc "*Whispers* Fine..."
    tr "*Whispers* I'll get you something to drink."
    mc "*Whispers* Do you maybe have some food too? I'm kinda hungry."
    tr "*Whispers* I don't have a kebab, but I can bring you an apple?"
    mc "*Whispers* Heh... Thanks."
    scene 10_1912 with Dissolve(1)
    tr "Perdón."
    if Layla_End == True:
        mc "{i}(One, maybe one and a half hours... What am I going to do here this whole time?){/i}"
        mc "..."
    else:
        if Layla_Dating == True:
            scene 10_1913 with Dissolve(1)
            mc "{i}(So this is why Layla couldn't come to the beach...){/i}"
            mc "{i}(The girl I'm sorta dating and the woman I'm fucking, in the same room!){/i}"
            mc "{i}(Actually it's no different to when we're in class...){/i}"
        else:
            pass
        mc "{i}(One, maybe one and a half hours... What am I going to do here this whole time?){/i}"
        mc "..."
    if Alexis_Dating == True:
        scene 10_1914 with Dissolve(1)
        mc "{i}(Alexis! Fuck! I forgot about her. Now I'm gonna be late, since I'm stuck here!){/i}"
        mc "{i}(Why am I here in the first place when I have a girlfriend?){/i}"
        mc "{i}(Fuck... What am I doing?){/i}"
        menu:
            "Cancel date[KoGa3AutoWTChange1]{size=-4}(Alexis Week5 Monday Date Cancel, Alexis Points-10) {/size} {/color}":
                $ Alexis_Week5_Monday_Date_Cancel = True
                $ Alexis_Points -= 10
                mc "{i}(I'm not really in the mood anymore to go on a date with her today.){/i}"
                mc "{i}(I guess I'll text her, since I can't really call her right now...){/i}"
                scene 10_1915 with Dissolve(1)
                mc "{i}(Hey... Sorry, something came up and I can't make it. I'll call you later. [mc]){/i}"
                mc "{i}(That will do...){/i}"
                mc "{i}(Should I just break up with her? And date Gabi?){/i}"
                mc "{i}(What the fuck am I thinking... This is just a hookup for her.){/i}"
                mc "{i}(And I like Alexis! But then why did I cheat on her?){/i}"
                mc "{i}(Because it's fucking Gabi!!!){/i}"
            "Go on date":
                mc "{i}(I still want to go on a date with her. I like Alexis...){/i}"
                mc "{i}(But then why did I cheat on her? Because it's fucking Gabi!!!){/i}"
                mc "*Sigh*"
                mc "{i}(I guess I'll text her, since I can't really call her right now...){/i}"
                scene 10_1915 with Dissolve(1)
                mc "{i}(Hey... Sorry, something came up, and I'm gonna be late. [mc]){/i}"
                mc "{i}(Yeah, that will do...){/i}"
                mc "*Sigh*"
    else:
        pass
    scene black with Dissolve(1)
    pause 2
    scene 10_1916 with Dissolve(1)
    mc "{i}(Wasn't there a picture of her and her husband hanging before?){/i}"
    mc "{i}(She must have switched it out.){/i}"
    mc "{i}(Maybe they're getting a divorce? Or just a break or something? Is she even married? I never asked.){/i}"
    scene 10_1917 with Dissolve(1)
    mc "{i}(I hope she doesn't mind me snooping around.){/i}"
    mc "{i}(But I'm bored...){/i}"
    mc "{i}(Let's see what's in here.){/i}"
    scene 10_1918 with Dissolve(1)
    mc "{i}(Pictures...){/i}"
    scene 10_1919 with Dissolve(1)
    mc "{i}(Damn... She's so pretty. And she knows it too.){/i}"
    mc "{i}(Just a little bit more wind next time...){/i}"
    scene 10_1920 with Dissolve(1)
    mc "{i}(Oh, wow... That's hot!){/i}"
    mc "{i}(Young Gabi... How old is she here? Around my age, I guess?){/i}"
    scene 10_1921 with Dissolve(1)
    mc "{i}(With a friend? She looks so happy. Or drunk? Haha, yeah maybe.){/i}"
    mc "{i}(She even had a sixpack!){/i}"
    mc "{i}(If she was a student now... Just... Man...){/i}"
    scene 10_1922 with Dissolve(1)
    mc "{i}(Wait... What?){/i}"
    mc "{i}(She was on a track team? What...? I had no idea...){/i}"
    mc "{i}(That explains her incredible body too.){/i}"
    mc "{i}(What team is that? I recognise the colours. Must be Palm City High.){/i}"
    scene 10_1923 with Dissolve(1)
    mc "{i}(That... That's Navarro! Also looking younger. Hehe. One surprise after another.){/i}"
    mc "{i}(Was he her agent? She must have been really good, then. Like Sha'Carri good? Maybe better?){/i}"
    mc "{i}(Why did she quit though and become a teacher?){/i}"
    mc "{i}(Does anyone know about this?){/i}"
    scene black with Dissolve(1)
    pause 2
    scene 10_1924 with Dissolve(1)
    la "Thank you, Ms Ramirez."
    mc "{i}(Is she finally leaving?){/i}"
    tr "You're welcome. We'll see each other Thursday then."
    la "Okay. Bye."
    tr "Bye, Layla."
    scene 10_1925 with Dissolve(1)
    tr "I'm sorry. It took a little longer than I expected."
    mc "It's fine. I dozed off anyway."
    scene 10_1926 with Dissolve(1)
    tr "I was on my way home to prepare for Layla coming."
    tr "But then we bumped into each other and I forgot."
    mc "Don't worry, I space out too, every time I see you."
    tr "Heh..."
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 10_1927 at moveup
    pause 3
    mc "..."
    scene 10_1928 with Dissolve(1)
    tr "What?"
    mc "{i}(I'll ask her next time.){/i}"
    mc "Nothing. I told you I space out when I see you."
    scene 10_1929 with Dissolve(1)
    tr "Idiota!"
    scene 10_1930 with Dissolve(1)
    tr "[mc]..."
    tr "If we want to continue... this. We need to be more careful."
    tr "I know this was my fault but I think we need to set some rules."
    mc "Uhm... Rules... Like... Uh, sure, I guess. What do you have in mind?"
    scene 10_1931 with Dissolve(1)
    tr "Well, this one is pretty obvious. You can't tell anyone about this. Not even your best friend. No one can know."
    mc "{i}(Even though I know that Nate would keep this to the grave.){/i}"
    tr "No phone calls, messages, emails or anything of that sort."
    tr "No personal questions!"
    mc "I can't ask you if..."
    tr "You know what questions I mean!"
    scene 10_1932 with Dissolve(1)
    tr "At school, I'm Ms Ramirez. Not Gabi, not Gabriela. I'm a teacher and you're a student. Nothing more, nothing less."
    tr "We can have conversations there, as long as it's about school."
    tr "We can't just meet outside, I also think it's best not to meet here anymore. It's just too risky. I don't know yet where we..."
    mc "You can come to my place."
    scene 10_1933 with Dissolve(1)
    tr "Your parents' home..."
    mc "Yeah. We'll say you come over to give me some tutoring."
    tr "Because you need tutoring in Spanish... Very believable!"
    mc "Yeah, that was a stupid idea."
    mc "{i}(I have a lot of those lately.){/i}"
    scene 10_1934 with Dissolve(1)
    tr "I'll figure something out."
    tr "Hmm... I think that's it? Unless you have something?"
    mc "Not that I can think of. This is new to me, too."
    scene 10_1935 with Dissolve(1)
    tr "*Sigh* Dios mío! What am I doing?"
    mc "{i}(That sounded just like Elena.){/i}"
    mc "Gabi! If you don't want to..."
    scene 10_1936 with Dissolve(1)
    tr "That's the thing I don't understand... I want to!"
    mc "So do I!"
    tr "..."
    scene 10_1937 with Dissolve(1)
    mc "{i}(You have no idea how much I want this!){/i}"
    scene 10_1938 with Dissolve(1)
    tr "Wait!"
    mc "Hmm?"
    tr "There is one more thing."
    tr "Don't fall in love with me."
    mc "Don't fall in love with you?"
    scene 10_1939 with Dissolve(1)
    tr "Yes. If you do, this ends."
    mc "Okay. Not falling in love with you it is."
    tr "..."
    tr "I mean it! This is complicated enough already."
    scene 10_1940 with Dissolve(1)
    ""
    scene black with Dissolve(1)
    pause 2
    scene 10_1941 with Dissolve(1)
    mc "I want to stay longer, but I'd better get going now."
    mc "Before anyone else shows up here."
    tr "Heh, yeah."
    scene 10_1942 with Dissolve(1)
    mc "One more thing. How do we contact each other?"
    mc "You said before, no calls, no messages and so on..."
    tr "We'll meet at school."
    scene 10_1943 with Dissolve(1)
    mc "That's still a week from now."
    tr "Just a week. And I'm busy anyway."
    mc "..."
    scene 10_1944 with Dissolve(1)
    mc "*Sigh* See you in a week, then."
    tr "Haha. Enjoy your spring break!"
    mc "You too."
    scene 10_1945 with Dissolve(1)
    ""
    menu:
        "Bye":
            scene 10_1946 with Dissolve(1)
            mc "Adiós, Gabi!"
            tr "Adiós!"
        "Love you":
            scene 10_1946 with Dissolve(1)
            mc "Adiós, chica!"
            tr "Heh... Adiós, chico!"
            scene 10_1947 with Dissolve(1)
            mc "Te amo!"
            tr "..."
            mc "Haha... Es broma!\n(Kidding!)"
    scene 10_1948 with Dissolve(1)
    tr "*Shakes head*"
    $ renpy.end_replay()
    if Alexis_Dating == True:
        if Alexis_Week5_Monday_Date_Cancel == True:
            jump Week5_Monday_End
        else:
            jump Week5_Monday_Alexis
    else:
        jump Week5_Monday_End

label Week5_Monday_Alexis:
    $ Alexis_Week5_Monday_Makeup = True
    scene black with Dissolve(1)
    pause 2
    stop music fadeout 1.0
    play music ("Music/LoFi Upbeat 1.mp3", "Music/LoFi Upbeat 2.mp3", "Music/LoFi Upbeat 3.mp3", "Music/LoFi Upbeat 4.mp3") volume 0.2
    n "Later that afternoon."
    if MC_Bike == True:
        scene 10_1949 with Dissolve(1)
        ""
    else:
        scene 10_1950 with Dissolve(1)
        ""
    scene 10_1951 with Dissolve(1)
    mc "Hey! Uh..."
    a "Hey. Sorry, I'm not ready yet. I was just about to do my makeup..."
    mc "You haven't even changed yet. You're still wearing the same thing as this morning..."
    mc "You even had more time, since I'm late..."
    a "I know!"
    scene 10_1952 with Dissolve(1)
    ""
    scene 10_1953 with Dissolve(1)
    a "Come on in."
    a "Give me like ten minutes. Twenty... twenty minutes!"
    mc "Heh..."
    scene 10_1954 with Dissolve(1)
    mc "I think this is the first time I've seen you without makeup."
    a "Ugly, right?"
    menu:
        "Don't answer":
            scene 10_1955 with Dissolve(1)
            mc "I'm not answering stupid questions!"
            a "Sorry... I didn't..."
            a "..."
        "Joke":
            scene 10_1956 with Dissolve(1)
            mc "Uh... Well..."
            a "I knew it!"
            mc "I'm kidding."
            mc "Besides. Not everyone can be as pretty as I am."
            a "..."
            scene 10_1957 with Dissolve(1)
            mc "Haha. I'm still kidding."
            a "How about you wait outside!"
            mc "See! You can joke too!"
            a "I'm not."
            scene 10_1958 with vpunch
            mc "What?"
            a "Haha. I wasn't joking..."
            mc "Really... Then why are you laughing?"
            a "[mc]!"
        "No":
            mc "No! You're just as pretty with or without makeup."
            mc "Stop being so insecure about yourself. You're gorgeous, Lexi! Okay?"
            a "Thanks."
    scene black with Dissolve(1)
    pause 2
    if Erynn_Week3_Monday_Blackmailhelp == True:
        scene 10_1959 with Dissolve(1)
        a "How did it go with Erynn yesterday."
        mc "Good, I think. We still have stuff to figure out, though."
        mc "But let's not talk about that today."
        a "Sure."
        if Erynn_LikeMC == True:
            mc "I need to tell you something, though."
            scene 10_1960 with Dissolve(1)
            a "That Erynn slept in your bed?"
            mc "Oh, you know."
            a "Mm-hmm. She told me. Thanks for telling me too."
            a "And don't worry. It's fine."
        else:
            pass
    else:
        pass
    scene 10_1961 with Dissolve(1)
    a "Be right back. I'll do my makeup real quick."
    mc "Lexi?"
    a "Hmm?"
    mc "Can I do it?"
    a "Do what? My makeup?"
    scene 10_1962 with Dissolve(1)
    mc "Yeah."
    a "Really? Have you ever done it?"
    mc "No, but I want to try it."
    a "Heh... Weird request, but sure. Let me get my stuff, then."
    scene black with Dissolve(1)
    pause 2
    scene 10_1963 with Dissolve(1)
    mc "Alright. Ready?"
    a "I'm gonna be honest. I'm a little scared."
    a "Please be gentle and don't poke my eyes out!"
    mc "I promise to be gentle, but I can't guarantee not to poke your eyes out."
    a "[mc]..."
    scene 10_1964 with Dissolve(1)
    mc "Do you need to moisturise first?"
    a "No, I did that already."
    mc "Kay, then we'll start with the foundation."
    a "How do you know all this?"
    mc "..."
    scene 10_1965 with Dissolve(1)
    a "Oh, never mind... I actually know. Erynn..."
    mc "We're not talking about that! Ever!"
    a "Haha. I wish I'd seen it though."
    scene black with Dissolve(1)
    pause 2
    scene 10_1966 with Dissolve(1)
    ""
    scene 10_1967 with Dissolve(1)
    a "You are really concentrating. You look so serious."
    mc "Don't move!"
    a "I'm sorry."
    mc "Now do the thingy with your lips!"
    scene 10_1968 with Dissolve(1)
    mc "Let's see... Yeah, I think it's finished. Stunning!"
    a "Haha. Happy with the result?"
    mc "I am. Especially for my first time."
    a "Someone found a new career path."
    mc "Haha."
    scene 10_1969 with Dissolve(1)
    a "I don't know how it looks yet, but I weirdly feel like you did a really good job."
    a "I feel pretty."
    mc "You are!"
    scene 10_1970 with Dissolve(1)
    a "Before I look, I have a question."
    a "If you saw me at a bar tonight, and I was having a cocktail or something, and you were behind me and I just..."
    a "Looked over my shoulder and like... giggled."
    a "What would you do? What would you honestly do?"
    scene 10_1971 with Dissolve(1)
    mc "Hmm... I would think..."
    mc "Wow! That girl must have had a rough night. But she looks like a good time!"
    a "Haha. I don't know if that's a compliment or not..."
    a "I'm ready to see it. Hand me the mirror, please."
    scene 10_1972 with Dissolve(1)
    a "..."
    scene 10_1973 with Dissolve(1)
    a "Haha."
    a "It's not bad. It's not... that bad!"
    mc "Yeah, I think it's pretty good."
    a "'She had a rough night'. Haha. Definitely!"
    scene 10_1974 with Dissolve(1)
    a "This was fun. Thank you for doing my makeup."
    mc "Anytime."
    scene 10_1975 with Dissolve(1)
    a "Let me change real quick and then we can leave."
    mc "Wait... You're going like this?"
    a "Yeah. Didn't you say I look pretty?"
    mc "Uhm..."
    scene 10_1976 with Dissolve(1)
    a "Haha. I knew it! Your face says it all!"
    mc "..."
    a "Don't worry. I won't leave the house like this."
    a "Give me thirty minutes."
    scene 10_1977 with Dissolve(1)
    mc "Thirty? What happened to twenty?"
    a "Now I need to remove this first and then reapply. I'll hurry."
    mc "It's fine. Take your time. Make yourself pretty... Prettier? You know what I mean."
    a "Haha."
    scene 10_1978 with Dissolve(1)
    la "Haha. What is this? What have you done?"
    a "I was just trying something."
    la "Well, you failed!"
    a "It's not that bad..."
    la "Not that bad? Lex! You look like a clown!"
    scene 10_1979 with Dissolve(1)
    a "What are you doing?"
    la "I need to take a picture of that."
    a "Layla, don't! Go away!"
    a "LAYLA! DELETE THAT!"
    la "Haha."
    scene black with Dissolve(1)
    pause 2
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 10_1980 at moveup
    pause 3
    a "Good to go!"
    mc "You look good! You look better than good!"
    a "Thanks."
    mc "That's the Lexi I know and love."
    scene 10_1981 with Dissolve(1)
    a "..."
    mc "What?"
    a "That counts!"
    mc "What counts?"
    scene 10_1982 with Dissolve(1)
    a "You said you love me!"
    mc "I said..."
    a "You love me!"
    mc "I..."
    a "Nuh-uh. It counts!"
    mc "Fine. You said it first, though."
    scene 10_1983 with Dissolve(1)
    a "No, I didn't."
    mc "You did! When I was at training camp, and we were on the phone, you..."
    a "That doesn't count!"
    mc "Oh... That doesn't count... But mine does?"
    scene 10_1984 with Dissolve(1)
    a "Uh-huh... I don't make the rules."
    mc "Are you sure about that? Because that..."
    scene 10_1985 with Dissolve(1)
    mc "..."
    scene 10_1986 with Dissolve(1)
    mc "Okay, I think you're right."
    a "Haha."
    scene 10_1987 with Dissolve(1)
    a "Come on. Let's head out."
    mc "You did your nails, too."
    a "Yeah, going all black today."
    scene 10_1988 with Dissolve(1)
    a "So, where are we going?"
    mc "I had something in mind but after doing your makeup, I've got another idea."
    mc "What do you think of a costume shop and trying on different outfits?"
    a "That sounds fun."
    scene black with Dissolve(1)
    pause 2
    if MC_Bike == True:
        scene 10_1989 with Dissolve(1)
        a "..."
        a "Who parked his motorcycle on our driveway?"
        menu:
            "That's mine":
                mc "That was me!"
                scene 10_1990 with Dissolve(1)
                a "That's your motorcycle?"
                mc "Yeah!"
                a "No! When did you get a motorcycle?"
                mc "Yesterday."
                scene 10_1991 with Dissolve(1)
                a "Are you actually serious?"
                mc "I am!"
                a "And are we gonna ride it?"
                mc "That was the plan."
                scene 10_1992 with Dissolve(1)
                a "I've always wanted to ride a motorcycle!"
                mc "Today's the day then."
                mc "Go sit on it."
                scene 10_1993 with Dissolve(1)
                mc "What do you think?"
                a "This is amazing!"
                mc "It really suits you, too. You look like a sexy biker girl."
                a "Haha, thanks."
                mc "Move a little."
            "Sit on it":
                scene 10_1994 with Dissolve(1)
                mc "This is nice!"
                a "[mc]! What are you doing? What if the owner shows up? Get off!"
                mc "It's fine. I don't see anyone."
                scene 10_1995 with Dissolve(1)
                mc "Want to give it a go?"
                a "No!"
                mc "Come on. I'm sure he wouldn't mind having a hot girl sitting on his bike!"
                mc "Just try it. I can see you want to."
                a "Just real quick. Stay on the lookout, okay?"
                scene 10_1993 with Dissolve(1)
                mc "What do you think?"
                a "This is amazing!"
                mc "It really suits you too. You look like a sexy biker girl."
                a "Haha, thanks."
                scene 10_1996 with Dissolve(1)
                mc "Oh shit! Someone's coming! Good luck!"
                a "[mc]!"
                a "Wait! Are you kidding me! Help me get off!"
                a "[mc]!"
                scene 10_1997 with Dissolve(1)
                mc "Haha. Your face when you panic is the best!"
                a "..."
                mc "I'm sorry! No one's here."
                scene 10_1998 with Dissolve(1)
                a "Now help me get off before he actually shows up!"
                mc "He's been here the whole time. It's my bike!"
                a "What?"
                mc "It's mine. I got it yesterday."
                scene 10_1999 with Dissolve(1)
                a "Are you actually serious?"
                mc "I am!"
                a "And are we gonna ride it?"
                mc "That was the plan. Move a little."
        scene 10_2000 with Dissolve(1)
        a "Oh... You want me to ride?"
        mc "Sure."
        a "Haha, I wish I knew how. You'll have to teach me one day."
        mc "We can do that. But maybe on a smaller bike."
        scene 10_2001 with Dissolve(1)
        ""
        scene 10_2002 with Dissolve(1)
        a "I'm starting to feel like Stephanie Zinone."
        mc "Who's that?"
        a "You've never seen Grease? Well, Grease 2?"
        mc "No..."
        a "Never heard of..."
        scene 10_2003 with Dissolve(1)
        a "*Sings* Cool rider..."
        mc "{i}(I love it when she sings. So sexy!){/i}"
        scene 10_2004 with Dissolve(1)
        mc "That sounded great!"
        a "Thanks."
        mc "I guess that's from the movie?"
        a "Uh-huh. One of my favourites. Let's watch it once we're back."
        scene 10_2005 with Dissolve(1)
        ""
        scene 10_2006 with Dissolve(1)
        ""
        scene 10_2007 with Dissolve(1)
        ""
        scene black with Dissolve(2)
        pause 2
        scene 10_2008 with Dissolve(1)
        a "That was such a rush!"
        mc "You liked it?"
        a "I loved it!"
        scene 10_2009 with Dissolve(1)
        a "Let's drive somewhere farther away next time."
        mc "We can do that."
    else:
        scene black with Dissolve(2)
        pause 2
    scene 10_2010 with Dissolve(1)
    a "How was your run this morning with Layla and Valeria?"
    mc "It was good. We had fun."
    a "Did you race her?"
    if Layla_Week3_Tuesday_Train == True:
        scene 10_2011 with Dissolve(1)
        mc "Not this time, no. I raced her a few weeks ago though."
        a "I remember. The day you turned me down."
        mc "Heh. Sorry..."
        a "It's fine. You can make up for it today."
        scene 10_2012 with Dissolve(1)
        mc "She raced a few times against Val, though."
        a "Did she win?"
        mc "No."
        a "She should've let me join. She might have won against me. Maybe!"
        mc "Haha. She said the exact same thing."
    else:
        scene 10_2012 with Dissolve(1)
        mc "No, I didn't. She raced a few times against Val though."
        a "Did she win?"
        mc "No."
        a "She should've let me join. She might have won against me. Maybe!"
        mc "Haha. She said the exact same thing."
    scene 10_2013 with Dissolve(1)
    mc "If you want to come with us next time, you can."
    a "No, Layla was right. I'll just slow you guys down."
    mc "By the way. What did she mean when she said three years ago, before you...?"
    a "Oh... You heard that?"
    mc "Did something happen?"
    scene 10_2014 with Dissolve(1)
    a "In high school, I was on the volleyball team together with Erynn."
    a "Back then my dad, Layla, and I went running together once or twice a week."
    a "He still asks me every week if I want to jog with him, but I haven't gone in three years."
    a "It's not that I don't want to... But... I'm scared..."
    scene 10_2015 with Dissolve(1)
    a "We had a game against a school from Palm City. Together with a teammate, I went to block a spike from the other team."
    a "While coming down, I stepped on my teammate's foot and twisted my ankle. Later we found out that I actually broke it."
    a "I didn't need surgery, but it took over two months to fully heal and another to be able to play again."
    a "At my first training after I got back, I don't really know what happened exactly, but I was hesitant due to the injury and I think I misstepped or something..."
    a "And yeah... I twisted it again."
    scene 10_2016 with Dissolve(1)
    a "It took a long time again to heal, but that time, I didn't rejoin the team. I just quit."
    a "I was too scared to injure my ankle again and maybe suffer permanent damage."
    a "I haven't done any sport since. It also changed my plans for college."
    mc "{i}(Is that what Erynn meant when she said 'Lexi is more fragile than you think'?){/i}"
    mc "I'm sorry. Is your foot okay now, or do you still...?"
    scene 10_2017 with Dissolve(1)
    a "No, it's totally fine."
    a "Otherwise, I wouldn't be wearing high heels as often or working in a bar where I have to be on my feet the whole time."
    mc "Thanks for telling me. I like it when I get to know more things about you."
    a "You can ask me anything."
    scene black with Dissolve(1)
    pause 2
    stop music fadeout 1.0
    play music ("Sounds/Store2.mp3", "Sounds/Store2.mp3") volume 0.3
    scene 10_2018 with Dissolve(1)
    a "They sell a lot of normal clothes, too."
    mc "It can't be Halloween every day. That's probably how they keep afloat."
    a "Hmm... True."
    a "We should've asked Erynn to come. She loves this stuff."
    scene 10_2019 with Dissolve(1)
    mc "No, I'd rather spend some time with you alone."
    a "Heh..."
    mc "We can ask her out next time. Maybe."
    a "Haha."
    scene 10_2020 with Dissolve(1)
    a "I have an idea."
    a "How about we each pick something to dress up in and only show it once we're in costume?"
    mc "Okay, sure. Pick something sexy though!"
    a "Haha. Same goes for you!"
    scene 10_2021 with Dissolve(1)
    mc "{i}(Let's see what we've got here...){/i}"
    mc "{i}(This is too small.){/i}"
    mc "{i}(I definitely won't wear something like this...){/i}"
    scene 10_2022 with vpunch
    a "AAAH!"
    mc "Fuck...!"
    scene 10_2023 with Dissolve(1)
    a "Haha, you scare so easily."
    mc "..."
    if Layla_Week3_Tuesday_Train == False:
        scene 10_2024 with Dissolve(1)
        mc "See! I knew you were a vampire! Even Brooke thinks so."
        a "Who's Brooke?"
        mc "She works at the restaurant. She says your whole family are vampires!"
        a "She might be right."
        scene 10_2025 with Dissolve(1)
        mc "Don't you dare bite me again!"
        a "Your neck looks so tasty though!"
    else:
        scene 10_2024 with Dissolve(1)
        mc "Brooke was right. You are a vampire!"
        a "Who's Brooke?"
        mc "She works at the restaurant. She says your whole family are vampires!"
        a "She might be right."
        scene 10_2025 with Dissolve(1)
        mc "Don't you dare bite me!"
        a "Your neck looks so tasty though!"
    scene 10_2026 with Dissolve(1)
    a "So, what do you think?"
    mc "I have to admit. You look sexy with fangs. But that can be your vampire charm making me feel attracted to you."
    a "Hmm... You seem to know a lot about vampires..."
    mc "Haha. Where did you get them?"
    a "They were lying on the table there."
    scene 10_2027 with Dissolve(1)
    mc "And you just put them in your mouth? Who knows who else used them before you!"
    a "Ew..."
    mc "Exactly!"
    a "Why did you tell me this?"
    mc "Why did you put them in your mouth?"
    scene 10_2028 with Dissolve(1)
    mc "Maybe you'll find a toothbrush lying somewhere, so you can brush your teeth."
    a "*Mumbling* Shut up!"
    mc "Haha."
    scene black with Dissolve(1)
    pause 2
    scene 10_2029 with Dissolve(1)
    a "Are you ready?"
    mc "I am."
    a "Alright. Let's come out at the same time."
    a "Three... two... one..."
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 10_2030 at moveup
    pause 3
    mc "Hello there, Miss Wonder Woman!"
    mc "You look hot, Lexi!"
    a "Thanks."
    scene 10_2031 with Dissolve(1)
    a "Looks like we had the same idea."
    mc "Too bad we aren't in the same universe, though."
    a "What?"
    mc "Never mind."
    scene 10_2032 with Dissolve(1)
    mc "You look really good in that, Lexi."
    mc "If that woman who plays Wonder Woman ever stops or if they need a younger version, they should contact you!"
    a "Haha, thanks. My acting is terrible, though."
    mc "Can you give me a spin?"
    scene 10_2033 with Dissolve(1)
    mc "Seriously... This is so sexy! Good choice!"
    a "I guess I know what to get during Halloween."
    mc "I have to remove the mask. It's getting hard to breathe."
    scene 10_2034 with Dissolve(1)
    a "That's not the only thing that's hard."
    a "Your suit was tight already, but it's getting very tight down there."
    mc "Uh..."
    scene 10_2035 with Dissolve(1)
    a "Your ass looks good too. You should wear spandex more often."
    mc "Okay. That's enough!"
    a "What? Can't I compliment you?"
    scene 10_2035 with vpunch
    n "*Slap*"
    mc "Hey!"
    scene 10_2036 with Dissolve(1)
    a "*Whisper* I'm not really into cosplay. But I have to admit, it kinda turns me on!"
    mc "..."
    a "*Whisper* Let's try some more costumes?"
    mc "*Nods*"
    scene black with Dissolve(1)
    pause 2
    scene 10_2037 with Dissolve(1)
    mc "I'm ready. How about you?"
    a "One second!"
    mc "{i}(Can't wait to see what she picked this time. It can't be better than the Wonder Woman outfit, right?){/i}"
    a "Kay, good to go."
    if Team_Yennefer == True:
        scene black with Dissolve(1)
        transform moveup:
            xalign 0.5 yalign 1.0
            linear 5.0 yalign 0.0
        show 10_2038 at moveup
        pause 3
        mc "{i}(HOLY SHIT!){/i}"
        mc "{i}(She didn't...){/i}"
        scene 10_2039 with Dissolve(1)
        a "Oh... You're a warrior this time?"
        a "What do you think of mine?"
        mc "..."
        scene 10_2040 with Dissolve(1)
        a "Why aren't you saying anything? Don't you like it?"
        mc "..."
        a "[mc]?"
        scene 10_2041 with Dissolve(1)
        mc "Dreams really do come true!"
        a "What?"
        mc "You have no idea what you're doing to me right now."
        scene 10_2042 with Dissolve(1)
        a "[mc]!"
        a "Haha."
        scene 10_2043 with Dissolve(1)
        mc "I know you said you aren't into cosplay, but can you be my Yennefer one time? For me?"
        a "Yennefer? I have no idea what you're talking about."
        mc "Trust me. It's better I don't explain."
        a "Heh... Sure, I guess."
        scene 10_2044 with Dissolve(1)
        mc "Great. Now I only need to find a unicorn."
        a "A unicorn? Okay... What's going on? Maybe I agreed too quickly."
        mc "Haha."
    else:
        scene black with Dissolve(1)
        transform moveup:
            xalign 0.5 yalign 1.0
            linear 5.0 yalign 0.0
        show 10_2038 at moveup
        pause 3
        mc "{i}(So close, yet so far.){/i}"
        mc "{i}(She looks good though.){/i}"
        scene 10_2039 with Dissolve(1)
        a "Oh... You're a warrior this time?"
        a "What do you think of mine?"
        mc "..."
        scene 10_2045 with Dissolve(1)
        mc "You're Yennefer. It looks really good on you."
        mc "You should've picked Triss though, just saying."
        a "Yennefer, Triss? Uh... What's going on?"
        mc "Haha. I'll tell you later. You look nice."
        a "Thanks."
    scene black with Dissolve(1)
    pause 2
    scene 10_2046 with Dissolve(1)
    a "They have a lot of nice wigs, too. Want to try some out?"
    mc "Sure."
    a "Let's pick one for each other."
    scene 10_2047 with Dissolve(1)
    a "Haha."
    mc "I knew you'd pick this one."
    a "It's not that bad."
    mc "I know what your 'it's not that bad' means..."
    mc "I look like someone who plays video games for a living. Ridiculous..."
    scene 10_2048 with Dissolve(1)
    mc "My turn!"
    mc "I'm not gonna pick a funny one. I'll pick one I think you might look good in."
    a "Hmm... Go for it."
    scene 10_2049 with Dissolve(1)
    a "I quite like this one. Good choice."
    mc "It actually suits you. Fits nicely with your outfit too!"
    a "Well, you have better taste in wigs than makeup."
    mc "Haha. I tried, okay."
    scene 10_2050 with Dissolve(1)
    a "Let's do another one."
    mc "Pick a normal one for me this time though. One I might look good in."
    a "Can I take a long-haired one? I'm curious how you'd look with long hair."
    mc "Yeah. I'm a little curious myself."
    scene 10_2051 with Dissolve(1)
    a "Haha. What have I done?"
    mc "Why are you laughing? This is great! I look like a rockstar!"
    a "Uh-huh. Total rockstar. Haha."
    mc "We should start a band now. You sing, I'll play guitar."
    scene 10_2052 with Dissolve(1)
    mc "I even have a name for our band."
    a "Yeah?"
    mc "Wow!"
    a "Wow?"
    mc "Wearers of Wigs!"
    scene 10_2053 with Dissolve(1)
    a "Haha..."
    mc "Look at all those tears of joy. Don't ruin your makeup though. I don't have time to redo it!"
    a "[mc]... Haha... Please, stop... Haha... I can't... Please take it off..."
    mc "Haha."
    scene 10_2054 with Dissolve(1)
    mc "You alright?"
    a "Yeah... That was funny! How do you come up with those stupid names?"
    mc "Stupid? It's still better than Yellow Snow!"
    a "Haha."
    mc "I'll get you a tissue."
    scene 10_2055 with Dissolve(1)
    ""
    scene 10_2056 with Dissolve(1)
    a "Okay... Deep breath! Last one. I don't think I can handle more."
    mc "I'll pick a good one. Close your eyes. it will be a surprise."
    scene black with Dissolve(1)
    pause 2
    mc "Holy shit!"
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 10_2057 at moveup
    pause 3
    mc "I think we've found a winner!"
    mc "That is so hot, Lexi! You've gotta see this."
    mc "Let's go to the dressing rooms. There's a big mirror."
    scene 10_2058 with Dissolve(1)
    a "Oh..."
    mc "Amazing, right? So sexy!"
    scene 10_2059 with Dissolve(1)
    mc "You look so much like your mom."
    a "Is that a good thing?"
    mc "It is. Because if you look like her when you're her age. Man..."
    a "..."
    scene 10_2060 with Dissolve(1)
    a "Do you have a crush on my mom?"
    mc "Haha..."
    a "Don't laugh. Answer me!"
    mc "A little, maybe?"
    a "That's so wrong."
    scene 10_2061 with Dissolve(1)
    mc "Why is that wrong? She's attractive. And I meant it more as a compliment than anything else."
    mc "Just like I think my mom is attractive, too."
    a "Emily is very pretty."
    mc "See!"
    scene 10_2062 with Dissolve(1)
    a "It's still a bit weird though."
    mc "Didn't you ever have a crush on someone older?"
    a "I wanted to marry my dad when I was younger."
    mc "Well... You can marry your dad, I'll marry your mom and..."
    scene 10_2063 with vpunch
    a "..."
    mc "Haha. I'm kidding!"
    scene 10_2064 with Dissolve(1)
    a "Aah..."
    mc "I wasn't kidding when I said you look amazing though."
    mc "It really suits you."
    a "Thanks."
    scene 10_2065 with Dissolve(1)
    mc "What do you think? Hottest couple in Madison Springs?"
    a "At least top three!"
    a "Should I get it?"
    mc "It's up to you."
    scene 10_2066 with Dissolve(1)
    a "I think I will."
    mc "Shall we head out then, or do you want to look some more?"
    if MC_Bike == True:
        a "I'm good. Let's go home and watch Grease!"
        mc "Two!"
        a "Yes, Grease 2."
    else:
        a "I'm good. Let's go home and watch a movie or something."
    scene 10_2067 with Dissolve(1)
    a "Thanks for buying it for me."
    mc "You're welcome."
    jump Week5_Monday_Alexis_TV

label Week5_Monday_Alexis_TV:
    if _in_replay:
        $ MC_Bike = True
    $ Adriana_Week5_Monday_SlapAss = True
    scene black with Dissolve(2)
    pause 2
    stop music fadeout 1.0
    play music ("Music/LoFi Upbeat 1.mp3", "Music/LoFi Upbeat 2.mp3", "Music/LoFi Upbeat 3.mp3", "Music/LoFi Upbeat 4.mp3") volume 0.2
    if MC_Bike == True:
        scene 10_2068 with Dissolve(1)
        a "Alright. Let's watch Grease 2 then."
        mc "Don't I have to watch the first one, first?"
        a "No. They're basically the same movie. The first one is with cars, the second with motorcycles."
        mc "Hmm, okay..."
        scene 10_2069 with Dissolve(1)
        a "Just a heads up. It's also part-musical."
        mc "Eh..."
        a "The songs are good though."
        mc "The one you sang earlier?"
        a "That one too, yes."
    else:
        scene 10_2068 with Dissolve(1)
        a "What do you want to watch?"
        mc "Whatever you want to see."
        a "Hmm... For some reason, I want to watch Grease 2!"
        mc "What's it about?"
        a "High school and motorcycles."
        scene 10_2069 with Dissolve(1)
        mc "Don't we have to watch the first one, first?"
        a "No. They're basically the same movie. Instead of motorcycles, the first one has cars."
        mc "Hmm, okay..."
        a "Oh, and just a heads up. It's also part-musical."
        mc "Eh..."
    scene 10_2070 with Dissolve(1)
    mc "Will your parents be home soon?"
    a "In about an hour or so."
    mc "Do they know... About us?"
    a "Not yet. I was going to tell them today. If you don't mind?"
    mc "No, it's fine."
    scene 10_2071 with Dissolve(1)
    a "Are you nervous now?"
    mc "A little maybe. But just because I haven't met your dad yet."
    a "You haven't? Hmm... I thought you had already."
    a "You have nothing to worry about. He's not scary."
    scene 10_2072 with Dissolve(1)
    mc "Not scary until his daughter brings a boy home!"
    a "Haha."
    a "You're actually the first boy I'll introduce to my parents. It's new for me too."
    a "So yeah. Maybe he is scary!"
    mc "..."
    scene 10_2073 with Dissolve(1)
    a "I'll protect you!"
    a "And if nothing works, just start talking about basketball."
    mc "Basketball? I can do that."
    scene 10_2074 with Dissolve(1)
    ""
    scene 10_2075 with Dissolve(1)
    a "Does your mom know?"
    mc "I haven't told her, but she knows."
    a "Heh..."
    scene 10_2076 with Dissolve(1)
    a "Let's watch the movie now!"
    a "This is perfect!"
    mc "You know what would make this even more perfect?"
    a "No, what?"
    scene 10_2077 with Dissolve(1)
    mc "Starts with PO, ends with RN."
    a "..."
    a "You're such a guy... Way to ruin a moment."
    scene 10_2078 with Dissolve(1)
    mc "Popcorn!"
    a "Oh..."
    mc "What did you think?"
    a "Nothing. I didn't think anything. I was... thinkless..."
    scene 10_2079 with Dissolve(1)
    mc "Thinkless? You mean thoughtless?"
    a "Yeah, I meant thoughtless!"
    mc "Your parents must be so proud. That communications major really is paying off."
    a "Oh shut up! I just misspoke!"
    mc "Uh-huh..."
    scene black with Dissolve(1)
    pause 2
    scene 10_2080 with Dissolve(1)
    ""
    scene 10_2081 with Dissolve(1)
    mc "..."
    scene 10_2082 with Dissolve(1)
    mc "Seriously Lexi... Are you always this annoying when watching a movie? Can't you sit still for like two minutes?"
    a "I'm bored. I've seen this movie a million times."
    mc "Then why did you pick it?"
    a "I wanted to show it to you. But let's do something else now."
    scene 10_2083 with Dissolve(1)
    a "Wanna have sex?"
    mc "..."
    a "Hmm?"
    mc "You know what? No! I want to finish this movie!"
    scene 10_2084 with Dissolve(1)
    a "You sure?"
    mc "..."
    mc "{i}(Stay strong! Stay strong!){/i}"
    mc "{i}(But she looks so good...){/i}"
    scene 10_2085 with Dissolve(1)
    mc "{i}(Stay stro... Why is this so difficult?){/i}"
    scene 10_2086 with Dissolve(1)
    a "You can do whatever you want..."
    mc "..."
    scene 10_2087 with Dissolve(1)
    ""
    scene 10_2088 with vpunch
    a "Aah-haha..."
    mc "No! It's not gonna work this time!"
    a "Heh... I know you were close to breaking."
    mc "Can we finish the movie first, please?"
    a "Fine!"
    scene black with Dissolve(1)
    pause 2
    scene 10_2089 with Dissolve(1)
    ""
    scene 10_2090 with Dissolve(1)
    a "Are you thirsty? I'm gonna get us something to drink."
    mc "Thanks. I'll have the same as you."
    a "Kay. I'll also change real quick. These pants are getting uncomfortable."
    a "Be right..."
    play sound "Sounds/Phone_Vibrate.mp3"
    n "*Bzzzt. Bzzzt*"
    scene 10_2091 with Dissolve(1)
    a "Hey! How are you?"
    a "I'm good."
    a "One second."
    scene 10_2092 with Dissolve(1)
    a "I'll be right back, okay?"
    mc "I'll pause the movie."
    a "No, it's fine. Just keep on watching. I know what happens."
    scene 10_2093 with Dissolve(1)
    mc "{i}(Now I can watch this in peace for a while.){/i}"
    mc "{i}(Can't believe I'm actually enjoying this.){/i}"
    scene black with Dissolve(2)
    pause 2
    scene 10_2094 with Dissolve(1)
    mc "{i}(She's been gone for a while now.){/i}"
    mc "{i}(Who's she on the phone with, anyway?){/i}"
    mc "{i}(I guess I'll get my own drink.){/i}"
    scene 10_2095 with Dissolve(1)
    mc "{i}(Oh... There she is!){/i}"
    mc "{i}(Is she still on the phone?){/i}"
    mc "{i}(Her ass looks good in those white leggings.){/i}"
    scene 10_2096 with vpunch
    n "*Slap*"
    scene 10_2097 with Dissolve(1)
    am "Mmm..."
    am "You're home early!"
    scene 10_2098 with Dissolve(1)
    mc "Uh..."
    mc "{i}(Oh no... This is...){/i}"
    am "..."
    a "What are you doing!"
    mc "{i}(I'm dead. I'm so dead!){/i}"
    scene 10_2099 with Dissolve(1)
    am "[mc]!"
    mc "I'm so sorry Princi... Adriana! I didn't mean to... I thought you were Alexis..."
    am "You thought I was Alexis?"
    scene 10_2100 with Dissolve(1)
    mc "Yeah. Lexi..."
    a "Mom, we..."
    am "Is this some kind of joke? Why do you look like me? Did you colour your hair?"
    a "No, this is a wig. I'll take it off."
    scene 10_2101 with Dissolve(1)
    am "What's going on here?"
    a "It's nothing. [mc] and I were at a costume shop and..."
    am "You and [mc]? On a date?"
    a "Yes! I wanted to tell you today that we're together. Not like this, of course."
    scene 10_2102 with Dissolve(1)
    am "I thought you and Layla were dating."
    mc "Uhm, no. We're just friends."
    mc "Again, I'm really sorry."
    scene 10_2103 with Dissolve(1)
    mc "If there's..."
    a "Okay... That's enough. You apologised. It was an honest mistake."
    a "Can you wait in my room? I need to talk to Mom."
    mc "I think I should maybe leave for today?"
    a "What? No! Please, wait in my room."
    scene 10_2104 with Dissolve(1)
    a "Why are you looking like that?"
    am "How am I looking?"
    a "Like you're judging me!"
    am "I'm not. I'm actually pleased to finally meet the reason why you're so happy lately!"
    scene 10_2105 with Dissolve(1)
    am "[mc], huh? Let's go talk."
    a "*Nods*"
    am "And by the way. You looked really pretty with the red hair."
    a "Thanks."
    $ renpy.end_replay()
    jump Week5_Monday_Alexis_Room

label Week5_Monday_Alexis_Room:
    if _in_replay:
        $ SexCounter_Alexis = 8
        $ MC_SexCounter = 8
    $ SexCounter_Alexis += 1
    $ MC_SexCounter += 1
    scene 10_2106 with Dissolve(1)
    mc "{i}(Fuck-fuck-fuck...){/i}"
    mc "{i}(This is going to be so awkward now every time I see her.){/i}"
    scene black with Dissolve(1)
    pause 2
    scene 10_2107 with Dissolve(1)
    a "..."
    scene 10_2108 with Dissolve(1)
    a "Hey. Are you okay?"
    mc "No..."
    mc "I slapped your mom's ass, Lexi. The principal's ass..."
    scene 10_2109 with Dissolve(1)
    a "You did more than just slap her ass! You kissed her neck and even squeezed her boobs!"
    mc "Thanks... I know..."
    a "Heh."
    scene 10_2110 with Dissolve(1)
    mc "Are you angry at me?"
    a "I want to be angry at you, but I can't. It's too funny."
    a "But if it was anyone other than my mom. I probably would've killed you just now!"
    mc "Why doesn't it sound like you're kidding?"
    a "Haha."
    scene 10_2111 with Dissolve(1)
    mc "How about her? Is she angry?"
    a "No. She was laughing too when we talked about it."
    a "Just between us, I think she enjoyed it at first."
    mc "Yeah, at first. Until she found out that it wasn't her husband."
    a "Haha, exactly."
    scene 10_2112 with Dissolve(1)
    mc "Hey. Can we postpone telling your dad we're dating?"
    mc "Now I'm not only fooling around with his daughter, but I also did with his wife."
    mc "He's actually going to kill me."
    a "Haha, he definitely will."
    scene 10_2113 with Dissolve(1)
    mc "But you said you'll protect me, right?"
    a "Haha. I can't protect you from this. You'd better start shovelling!"
    mc "Alexis!"
    scene 10_2114 with vpunch
    a "And don't call me Alexis, or I'll do it myself!"
    mc "I'm sorry, Ms Monroe!"
    a "..."
    mc "You can be so scary sometimes!"
    scene 10_2115 with Dissolve(1)
    a "One more thing!"
    a "If you want to slap an ass or squeeze some boobs or kiss someone's neck..."
    a "It's these here!"
    mc "{i}(This girl.){/i}"
    scene 10_2116 with Dissolve(1)
    mc "I love you!"
    a "..."
    a "That definitely counts!"
    mc "Yes! That counts."
    scene 10_2117 with Dissolve(1)
    a "I love you, [mc]!"
    scene 10_2118 with Dissolve(1)
    ""
    scene 10_2119 with Dissolve(1)
    a "Oh, sorry. I almost took my shirt off. What was I thinking?"
    a "You probably want to finish the movie, right?"
    mc "..."
    mc "You'd better continue taking that off!"
    a "Haha."
    scene 10_2120 with Dissolve(1)
    ""
    show 10_2121
    ""
    scene 10_2122 with Dissolve(1)
    mc "Come here, you tease!"
    a "Haha."
    scene 10_2123 with Dissolve(1)
    ""
    scene 10_2124 with Dissolve(1)
    a "Mmm..."
    scene 10_2125 with Dissolve(1)
    mc "{i}(I love sucking on boobs!){/i}"
    scene 10_2126 with Dissolve(1)
    ""
    scene 10_2127 with Dissolve(1)
    ""
    scene 10_2128 with Dissolve(1)
    ""
    scene 10_2129 with Dissolve(1)
    ""
    scene 10_2130 with Dissolve(1)
    mc "{i}(That's new...){/i}"
    scene 10_2131 with Dissolve(1)
    mc "..."
    scene 10_2132 with Dissolve(1)
    mc "{i}(She's really sucking on it today...){/i}"
    scene 10_2133 with Dissolve(1)
    mc "Fuck, Lexi... This is so good!"
    scene black with Dissolve(1)
    pause 2
    scene 10_2134 with Dissolve(1)
    mc "{i}(Is she so horny she can't wait any longer?){/i}"
    scene 10_2135 with Dissolve(1)
    a "Make me feel good!"
    mc "You don't have to tell me twice!"
    scene 10_2136 with Dissolve(1)
    ""
    scene 10_2137 with Dissolve(1)
    a "*Moaning*"
    a "Keep going!"
    scene 10_2138 with Dissolve(1)
    mc "{i}(She looks so pretty when she moans.){/i}"
    mc "You like that?"
    a "*Nods*"
    scene black with Dissolve(1)
    pause 2
    scene 10_2139 with Dissolve(1)
    ""
    scene 10_2140 with Dissolve(1)
    ""
    show 10_2141
    ""
    show 10_2142
    ""
    scene 10_2143 with Dissolve(1)
    a "Mmm..."
    show 10_2144
    ""
    scene 10_2145 with Dissolve(1)
    a "[mc]... I'm... Cum... ming..."
    a "*High-pitched moan* Aaah-haah..."
    mc "..."
    scene 10_2146 with Dissolve(1)
    a "Oh shit!"
    mc "Oh shit is right!"
    a "Do you think they heard?"
    scene 10_2147 with Dissolve(1)
    mc "Of course, they heard! Do you know how loud that was?"
    mc "You really want me dead, huh?"
    a "Haha, sorry! Love you?"
    scene 10_2148 with Dissolve(1)
    ""
    scene black with Dissolve(1)
    pause 2
    scene 10_2149 with Dissolve(1)
    a "Want to stay the night?"
    mc "Uh... I touched your mom, we had sex, and now you want me to have breakfast with your dad?"
    scene 10_2150 with Dissolve(1)
    a "Haha. I see your point. But next time?"
    mc "If I'm still allowed in the house."
    scene 10_2151 with Dissolve(1)
    a "Haha. I'll make sure of it, otherwise I'll sneak you in again."
    mc "Because that worked so great last time."
    a "Whose fault was that?"
    mc "Heh..."
    a "Let's cuddle for a little bit."
    scene 10_2152 with vpunch
    n "*Slap*"
    a "Aah-haha..."
    a "I said cuddle!"
    scene 10_2153 with Dissolve(1)
    mc "Well, I kissed your neck and squeezed your boobs, so the only thing left was..."
    a "To slap my butt."
    mc "Exactly!"
    scene 10_2154 with Dissolve(1)
    mc "That will be my new greeting."
    mc "Every time I see you, I kiss your neck, squeeze your boob, and slap your ass."
    a "Haha, oh please, no."
    scene 10_2155 with Dissolve(1)
    a "I'm fine with the neck kissing though."
    a "Maybe the ass slapping too. I kinda like it."
    mc "..."
    scene 10_2156 with Dissolve(1)
    a "Seems like someone wants another round."
    mc "How about you?"
    a "*Nods*"
    n "*Knock-knock*"
    scene 10_2157 with Dissolve(1)
    la "Lex?"
    a "..."
    la "Can I come in, or are you still having sex?"
    a "Uh... What...? One second, Layla."
    scene 10_2158 with Dissolve(1)
    a "That girl has the worst timing!"
    mc "At least she knocked."
    a "This time!"
    mc "This time?"
    scene black with Dissolve(1)
    pause 2
    scene 10_2159 with Dissolve(1)
    la "Hey. Hey, [mc]."
    mc "Hi, Layla."
    a "What do you want?"
    scene 10_2160 with Dissolve(1)
    la "Mom wanted me to ask [mc] if he is staying for dinner."
    mc "Uh... Not this time, but thanks."
    la "Okay. I'll tell her."
    a "..."
    scene 10_2161 with Dissolve(1)
    a "Is that all you wanted to ask?"
    la "Pretty much, yes."
    a "Really, Layla? You could've just asked us while standing outside..."
    la "If you didn't want me to come inside so you could finish... what you were doing, you could have said so."
    scene 10_2162 with Dissolve(1)
    a "Knowing you, you would just wait there and listen."
    la "I don't need to stand outside your room to listen. We could hear you in the whole house."
    a "LAYLA!"
    la "What? It's true..."
    scene 10_2163 with Dissolve(1)
    mc "Haha."
    a "That's not funny!"
    scene 10_2164 with Dissolve(1)
    mc "Oh yeah, Layla."
    la "Hmm?"
    mc "Since you're here, I need to do three things..."
    scene 10_2165 with vpunch
    a "No, you don't!"
    mc "Haha. You don't even know what I was about to say."
    a "Oh, I know!"
    la "What is it? I want to know too!"
    scene 10_2166 with Dissolve(1)
    mc "Hey! Why are you teaming up against me now?"
    la "I don't know but it looks fun!"
    la "Tickle attack!"
    mc "Too bad but I'm not ticklish at all."
    a "We'll see about that."
    scene 10_2167 with Dissolve(1)
    mc "Haha..."
    mc "Okay... Haha... You win!"
    mc "Haha, please..."
    scene 10_2168 with Dissolve(1)
    am "..."
    $ renpy.end_replay()
    jump Week5_Monday_End

label Week5_Monday_Beach:
    scene black with Dissolve(1)
    pause 2
    stop music fadeout 1.0
    play music "Sounds/Ocean.mp3" volume 0.5
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 10_2169 at moveup
    pause 3
    mc "Hola, Elena!"
    el "Hey, puppy."
    mc "{i}(Papi? What? Okay, I guess...){/i}"
    mc "Sup, mama."
    scene 10_2170 with Dissolve(1)
    el "..."
    el "Puppy... As in perrito!"
    mc "Oh... Haha. I thought you meant papi. Like... Hey, daddy."
    scene 10_2171 with Dissolve(1)
    el "Dios mío! Like I would call you daddy..."
    mc "Haha, yeah. I thought it was weird."
    el "*Shakes head*"
    scene 10_2172 with Dissolve(1)
    mc "Layla not here yet?"
    el "As you can see."
    mc "It's the same as last time..."
    scene 10_2173 with Dissolve(1)
    mc "But knowing her, she's probably hiding and ready to jump on me again."
    el "That's always a possibility."
    mc "You didn't come together?"
    n "*Bzzzt. Bzzzt*"
    scene 10_2174 with Dissolve(1)
    el "That might be her actually."
    el "One sec."
    scene 10_2175 with Dissolve(1)
    el "Hey, Layla."
    el "What? You're not coming?"
    el "Oh... That sucks."
    el "I don't know if I'll have time tomorrow. I'll let you know later."
    scene 10_2176 with Dissolve(1)
    el "Yeah, he's here already."
    el "Eh... You want him to be there too? You sure?"
    el "Kay, I'll ask him."
    el "I'll call you later then. Have fun."
    el "Bye, Lay."
    scene 10_2177 with Dissolve(1)
    el "Well, she's not coming."
    mc "Did something happen?"
    el "Her mom told her to study, something about some school stuff..."
    mc "School stuff?"
    mc "{i}(Her big mouth in the restaurant yesterday...){/i}"
    scene 10_2178 with Dissolve(1)
    el "She wants to have a hot tub party tomorrow, though."
    mc "A hot tub party? At her place?"
    el "Yeah. She'll call you later about it. She also said that you can invite Zach."
    mc "{i}(That's not gonna happen.){/i}"
    scene 10_2179 with Dissolve(1)
    mc "He's on a family vacation."
    el "Oh, so he's not here? That's great!"
    mc "Haha. You really like that guy, huh?"
    scene 10_2180 with Dissolve(1)
    el "I can't stand him. He gives me the ick."
    el "He even believed we had sex at training camp... In what world would I ever have sex with him?"
    el "How dumb can you be!"
    scene 10_2181 with Dissolve(1)
    mc "Tell me about it."
    mc "He's the kind of guy who would sleep with a ruler just to see how long he sleeps."
    el "What? Haha..."
    el "That's so funny and probably true."
    mc "Haha."
    scene 10_2182 with Dissolve(1)
    mc "Anyway. Since Layla isn't coming. Are you staying here, or...?"
    el "I'm here now, so I'm going to enjoy the sun for a couple of hours."
    el "If you want to go, just go. Don't feel obliged to stay and keep me company."
    if Elena_Points >= 27:
        scene 10_2183 with Dissolve(1)
        mc "It's not that I only came for Layla. I like you too."
        el "Liar!"
        mc "Haha, I'm not. You're actually fun to be around."
        mc "I'll stay a while. I even brought a big towel this time."
        el "Look at you."
    else:
        mc "I'll stay a while. I even brought a big towel this time."
        el "Look at you."
    scene 10_2184 with Dissolve(1)
    mc "What do you think?"
    el "What is that? Where did you get it?"
    mc "Haha. Layla gave it to me. She ordered it online."
    scene 10_2185 with Dissolve(1)
    el "..."
    el "The surprise you guys were laughing about at school..."
    mc "Exactly."
    scene 10_2186 with Dissolve(1)
    el "Now I know why she wanted to take those pictures..."
    el "But did she have to use the worst one?"
    mc "If this is the worst, I want to see the other pictures."
    mc "I think you look great!"
    el "..."
    if Elena_Points >= 27:
        scene 10_2187 with Dissolve(1)
        mc "My very own Magdalena."
        el "Magdalena...?"
        mc "She's perfect. Well, almost. The only thing that's missing is your snarky comments."
        el "How about you find another spot on the beach to lie down? Far away from me!"
        scene 10_2188 with Dissolve(1)
        mc "My beautiful Magdalena!"
        el "[mc]!"
        scene 10_2189 with vpunch
        mc "Hey! Haha."
        mc "Magdalena... Help!"
        el "I guess she's missing more than just my snarky comments!"
        scene 10_2190 with Dissolve(1)
        mc "You're right!"
        mc "No one beats the OG Elena."
        el "..."
        mc "{i}(Is she blushing? That's new...){/i}"
    else:
        scene 10_2187 with Dissolve(1)
        mc "My very own Elena."
        el "If you keep doing that, you can find another spot on the beach."
        el "Far away from me!"
        mc "Haha."
    scene 10_2191 with Dissolve(1)
    el "By the way. I'm taking that towel with me, later."
    el "I don't trust what you do with it at home."
    mc "I only sleep with it."
    el "Exactly!"
    scene black with Dissolve(1)
    pause 2
    if Elena_Points >= 27:
        scene 10_2192 with Dissolve(1)
        mc "..."
        scene 10_2193 with Dissolve(1)
        el "What?"
        mc "Oh, nothing. I was just looking at your bikini."
        el "What of it?"
        mc "I just haven't seen you wear it before."
        scene 10_2194 with Dissolve(1)
        mc "Is it new?"
    else:
        scene 10_2194 with Dissolve(1)
        mc "Is that a new bikini?"
    el "No. It's actually another Layla hand-me-down."
    mc "You're wearing a lot of Layla's old clothes, huh?"
    scene 10_2195 with Dissolve(1)
    el "..."
    el "Yeah..."
    mc "I mean. Not that there's anything wrong with it. You look good in them."
    if Elena_Points >= 27:
        mc "Especially those white pants."
        el "Heh. Thanks."
    else:
        pass
    scene 10_2196 with Dissolve(1)
    mc "Seems like Layla has a good idea what does look good on the both of you."
    el "She..."
    x "There she is!"
    el "..."
    if Elena_Week3_Monday_CheerTraining == True:
        scene 10_2197 with Dissolve(1)
        el "Mom!"
        ma "See! I told you Elena has a boyfriend."
        di "Elena has a boyfriend. Elena has a boyfriend."
        x "..."
    else:
        scene 10_2197 with Dissolve(1)
        el "Mom!"
        ma "Elena is with a boy, Mom."
        x "..."
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 10_2198 at moveup
    pause 3
    mc "{i}(That's Elena's mom?){/i}"
    mc "{i}(She doesn't look too pleased seeing me. Probably expected Layla to be here.){/i}"
    scene 10_2199 with Dissolve(1)
    el "Qué haces aquí?\n(What are you doing here?)"
    x "Ven aquí un segundo!\n(Come here for a second!)"
    if Elena_Week3_Monday_CheerTraining == True:
        scene 10_2200 with Dissolve(1)
        ma "Hey, [mc]."
        mc "Hey, guys. How are you?"
    else:
        scene 10_2201 with Dissolve(1)
        ma "Who are you?"
        mc "Hey, guys. I'm [mc]."
        ma "Are you Elena's boyfriend?"
        mc "Heh, no. I go to school with Elena."
    scene 10_2202 with Dissolve(1)
    di "Mom, look! There's another Elena."
    mc "{i}(Oh shit!){/i}"
    x "..."
    di "Haha."
    scene 10_2203 with Dissolve(1)
    el "La toalla es solo una broma de Layla.\n(The towel was just a joke from Layla.)"
    x "Dónde está Layla?"
    el "Hoy no pudo venir.\n(She couldn't make it today.)"
    x "Y quién es él?\n(And who is he?)"
    el "Un amigo de la escuela.\n(A friend from school.)"
    if Elena_Week3_Monday_CheerTraining == True:
        scene 10_2204 with Dissolve(1)
        x "Parece que los chicos lo conocen.\n(The boys seem to know him.)"
        el "Se pasó una vez para ayudarme a practicar.\n(He came over once to help me practice.)"
        x "A nuestra casa vino?\n(To our house?)"
        el "Sí, fue antes del campamento.\n(Yes. It was before training camp.)"
        el "Tuvimos unos entrenamientos extra, pero no pude ir porque me quedé en casa con los chicos.\n(We had some extra trainings but I couldn't go because I had to stay at home for the boys.)"
        el "Le pregunté a [mc] si podía pasarse a ayudarme a practicar.\n(I asked [mc] if he could come over to help me practice.)"
    else:
        pass
    scene 10_2205 with Dissolve(1)
    el "[mc], esta es mi mamá. Ava!\n([mc], this is my mom. Ava!)"
    mc "Hola. Encantado de conocerte, Ava.\n(Hello. Nice to meet you, Ava.)"
    av "Igualmente.\n(Nice to meet you too.)"
    scene 10_2206 with Dissolve(1)
    el "Entonces, qué haces aquí? No me digas que yo...\n(So, why are you here? Don't tell me I...)"
    av "Tienes que cuidar a los chicos.\n(You have to take care of the boys.)"
    el "Mamá... me habías dicho que hoy podía.\n(Mom... You told me I can have today.)"
    av "Eso fue antes de que una compañera se pusiera enferma y yo le cubriera los turnos.\n(That was before a colleague got sick and I took her shifts.)"
    scene 10_2207 with Dissolve(1)
    el "Solo pedí un día... no puede alguien más cubrir el turno de hoy?\n(I only asked for one day. Can't someone else take the shift for today?)"
    av "Sabes que tengo que tomar todos los turnos que pueda. Necesitamos... *Sigh*.\n(You know I have to take all the shifts I can get. We need the... *Sigh*.)"
    av "Elena, por favor!"
    el "*Nods*"
    scene 10_2208 with Dissolve(1)
    av "Gracias, mija."
    av "Perdón. Sé que es vacaciones de primavera y ojalá hubiera otra forma, pero...\n(I'm sorry. I know it's spring break, and I wish there was another way, but...)"
    el "No, te entiendo.\n(No, I understand.)"
    av "Mañana llamo a la abuela y le pregunto si puede venir unos días, vale?\n(I'll call grandma tomorrow and ask if she can make time to come for a few days, okay?)"
    el "*Nods*"
    scene 10_2209 with Dissolve(1)
    av "He preparado algunas cosas para ellos por si quieren quedarse en la playa.\n(I packed some stuff for them if you want to stay at the beach.)"
    av "También hay sobras de ayer en la nevera. Solo recaliéntalas para esta noche.\n(There are also some leftovers in the fridge from yesterday. Just reheat them for tonight.)"
    el "Gracias."
    scene 10_2210 with Dissolve(1)
    av "Hoy tengo doble turno, así que vuelvo mañana como al mediodía. Hablamos entonces.\n(I have a double shift today, so I'll be back tomorrow around noon. Let's talk then.)"
    el "Bien."
    av "Gracias, mi amor."
    scene 10_2211 with Dissolve(1)
    av "You boys behave, and listen to your big sister, alright?"
    di "Yes, mama."
    av "I'll see you tomorrow."
    scene 10_2212 with Dissolve(1)
    mc "Elena... Are you alright?"
    el "Yeah. Just give me a minute."
    di "Are you crying, Elena?"
    scene 10_2213 with Dissolve(1)
    el "No, no. Don't worry."
    el "I just got some sand in my eyes."
    di "That really hurts, right?"
    el "It does."
    menu:
        "Hug her[KoGa3AutoWTChange1]{size=-4}(Elena Points+2) {/size} {/color}":
            $ Elena_Points += 2
            # Elena (34)
            scene 10_2214 with Dissolve(1)
            el "Uh..."
            mc "You're an amazing sister!"
            mc "Take your time. I'll watch the boys."
            el "Thanks."
            scene 10_2215 with Dissolve(1)
            av "..."
        "Don't":
            mc "Take your time. I'll watch the boys."
            el "Thanks."
    if Elena_Points >= 29:
        scene black with Dissolve(1)
        pause 2
        scene 10_2217 with Dissolve(1)
        ma "Haha. This is so much fun!"
        di "That's long enough! Now it's my turn again!"
        mc "But that will be the last time, okay?"
        scene 10_2218 with Dissolve(1)
        di "Faster, [mc]! Faster!"
        mc "I'm doing my best here."
        di "Elena! Look! I'm flying!"
        scene 10_2219 with Dissolve(1)
        di "Elena! Are you looking?"
        el "Yes! I'm looking. You're doing great!"
        mc "What about me, Elena? Am I doing great too?"
        el "*Shakes head*"
        scene black with Dissolve(1)
        pause 2
        scene 10_2220 with Dissolve(1)
        mc "*Deep breath* That was exhausting!"
        el "Haha. They can be pretty exhausting sometimes, yes."
        el "But don't worry. I'll let them go in the water once, and then we'll be leaving."
        menu:
            "Leave":
                scene 10_2221 with Dissolve(1)
                mc "I'll stay a few minutes longer and watch them with you. I don't have anything else planned anyway."
                el "Thanks."
                scene black with Dissolve(2)
                pause 2
                scene 10_2286 with Dissolve(1)
                el "Sorry that..."
                mc "Don't be sorry. It's not your fault. Layla couldn't come either. We can come another day."
                mc "Are you taking the bus?"
                el "Yeah, you?"
                mc "I'll stay here and grab something to eat."
                scene 10_2292 with Dissolve(1)
                el "Maybe we'll see each other tomorrow at Layla's hot tub party..."
                mc "If she can make it."
                el "Haha. It's at her house. She'd better make it."
                scene 10_2289 with Dissolve(1)
                el "Anyway. Bye, [mc]."
                mc "Later, Elena."
                if Gabi_End == False:
                    jump Week5_Monday_Gabi
                else:
                    jump Week5_Monday_End
            "Stay[KoGa3AutoWTChange1]{size=-4}(Elena Week5 Monday Beach, Elena Points+4) {/size} {/color}":
                $ Elena_Week5_Monday_Beach = True
                $ Elena_Points += 4
                # Elena (38)
                jump Week5_Monday_Beach_Elena
    else:
        scene 10_2216 with Dissolve(1)
        el "So much for our beach day."
        mc "Oh, well... It happens I guess."
        el "Look, you don't have to stay. I just let them jump in the water a few times and head home too."
        mc "I'll stay a few minutes and watch them with you. Don't have anything else planned anyway."
        el "Thanks."
        scene black with Dissolve(2)
        pause 2
        scene 10_2286 with Dissolve(1)
        el "Sorry that..."
        mc "Don't be sorry. It's not your fault. Layla couldn't come either. We can go another day."
        mc "Are you taking the bus?"
        el "Yeah, you?"
        mc "I'll stay here and grab something to eat."
        scene 10_2292 with Dissolve(1)
        el "Maybe we'll see each other tomorrow at Layla's hot tub party..."
        mc "If she can make it."
        el "Haha. It's at her house. She better make it."
        el "Anyway. Bye, [mc]."
        mc "Later, Elena."
        if Gabi_End == False:
            jump Week5_Monday_Gabi
        else:
            jump Week5_Monday_End

label Week5_Monday_Beach_Elena:
    if _in_replay:
        $ Elena_Points = 38
    scene 10_2221 with Dissolve(1)
    mc "Already? You don't want to stay a bit longer?"
    el "I want to, but now I have to look after my brothers and..."
    mc "You can do that here! I'll help you out. And I think they'd like to stay longer too, and play a bit."
    el "You're sure you don't mind?"
    mc "I don't."
    scene 10_2222 with Dissolve(1)
    mc "And spending time with you isn't the worst either."
    el "Not the worst, but the second worst?"
    mc "Second is not the worst!"
    el "Haha. Idiota!"
    el "Thank you."
    scene 10_2223 with Dissolve(1)
    ma "Come, [mc]. Let's go play in the water."
    mc "Uh..."
    di "Come on!"
    el "Hey, you said you wanted to stay and help out!"
    mc "I did say that."
    scene 10_2224 with Dissolve(1)
    mc "AAAAH!"
    di "Haha..."
    ma "You can't catch us!"
    scene 10_2225 with Dissolve(1)
    mc "Up you go!"
    di "Aaah..."
    scene 10_2226 with Dissolve(1)
    ma "Hahaha."
    scene 10_2227 with Dissolve(1)
    el "..."
    scene 10_2228 with Dissolve(1)
    mc "Uh..."
    mc "Hello."
    scene 10_2229 with Dissolve(1)
    el "Haha."
    scene 10_2230 with Dissolve(1)
    x "I'm so sorry. She saw you throwing the boys and wanted to try it too."
    mc "Uhm, well... If you're okay with me throwing her in the water, I..."
    x "Yeah? Thank you!"
    scene 10_2231 with Dissolve(1)
    mc "You want to go high or not so high?"
    x "Not so high."
    mc "Okay."
    scene black with Dissolve(1)
    pause 2
    scene 10_2232 with Dissolve(1)
    mc "They just don't tire, huh?"
    el "They don't."
    mc "Why do kids have such high endurance? There's no need for that!"
    mc "I train every day and I can't keep up."
    el "Haha."
    scene 10_2233 with Dissolve(1)
    mc "Did you see?"
    el "See what?"
    mc "You weren't even looking?"
    scene 10_2234 with Dissolve(1)
    mc "Well... While throwing your brothers in the water, like at least fifty times, might I add."
    el "Wow. Fifty times!"
    mc "Each! Along came this mom with her little daughter who also wanted to be thrown."
    mc "And instead of throwing them one by one, I just thought, I'll throw them all together to save time, you know."
    el "Uh-huh..."
    scene 10_2235 with Dissolve(1)
    mc "So, I had those four kids on my shoulders."
    el "Four..."
    mc "And with one big swing, I threw those five kids..."
    el "Five... Right..."
    scene 10_2236 with Dissolve(1)
    mc "So, and then..."
    mc "..."
    mc "Why are you smiling like that?"
    scene 10_2237 with Dissolve(1)
    el "Haha."
    el "You're such an idiot."
    scene 10_2238 with Dissolve(1)
    ma "Did you rest enough? Can we play again?"
    mc "Let me lie down a little more."
    el "If [mc] wants to lie down, why don't you bury him in the sand?"
    di "Yes! Let's do that!"
    mc "Uhm... Sure."
    scene 10_2239 with Dissolve(1)
    mc "{i}(This isn't too bad.){/i}"
    scene 10_2240 with Dissolve(1)
    mc "{i}(And I have a really nice view too.){/i}"
    scene 10_2241 with Dissolve(1)
    di "Can you help us, Elena?"
    el "Just keep at it. You're doing great!"
    di "But it will be faster with three!"
    di "Please?"
    scene 10_2242 with Dissolve(1)
    mc "Yes, Elena! It will be faster with three!"
    el "..."
    mc "Pretty please..."
    el "Dios mío. Fine! I'll help!"
    scene 10_2243 with vpunch
    mc "Hey! Maybe a little gentler when throwing sand in that particular area."
    el "You wanted me to help, so stop complaining!"
    mc "..."
    scene 10_2244 with vpunch
    mc "Elena, you..."
    el "Say it!"
    mc "..."
    mc "You're so lucky your brothers are here, and I'm half buried in the sand!"
    scene black with Dissolve(1)
    pause 2
    scene 10_2245 with Dissolve(1)
    ma "The Ortiz boys saved the world again!"
    ma "They defeated the monster and buried him deep within the sand."
    mc "{i}(Monster? Defeated? Really? This easily?){/i}"
    scene 10_2246 with Dissolve(1)
    mc "*Evil laugh* Hahaha."
    di "No! Mateo! He's still alive!"
    mc "Did you really think this was over?"
    mc "Did you really think I could be defeated this easily?"
    scene 10_2247 with Dissolve(1)
    mc "AAAH!"
    ma "Nooo! We didn't bury him deep enough!"
    mc "Behold, the terrible vengeance of... Sand... Sandman!"
    mc "{i}(Wow [mc]... So original. Is that really the best I could come up with? Sandman?){/i}"
    scene 10_2248 with Dissolve(1)
    el "Man? Sandboy, maybe!"
    mc "Are you mocking me, human?"
    el "You're doing a pretty good job yourself, Sandboy!"
    mc "Once I'm finished with the Ortiz boys, I'm coming after you!"
    scene 10_2249 with Dissolve(1)
    ma "We need to use our special attack!"
    di "But it's too dangerous to use."
    ma "We have no choice! This is the only way to stop him!"
    ma "Are you ready?"
    scene 10_2250 with Dissolve(1)
    ma "Power up!"
    di "Aaaah!"
    mc "Power up all you want. That won't help you!"
    scene 10_2251 with Dissolve(1)
    di "Super-Mega-Lightning-Hyper-Dragon-Claw!"
    mc "{i}(Super-Mega what? Haha.){/i}"
    scene 10_2252 with Dissolve(1)
    mc "*Evil laugh* Hahaha."
    mc "Is that it? Is that all you've got? Your dragon claw is as weak as..."
    di "Omae wa mou shindeiru!"
    scene 10_2253 with Dissolve(1)
    el "Nani..."
    mc "NANI?"
    scene 10_2254 with Dissolve(1)
    mc "Aaah... What's happening?"
    mc "Elena... Elena, help... me..."
    el "Haha, get away from me, Sandboy."
    scene 10_2255 with vpunch
    el "Aah-haha... Nooo..."
    scene 10_2256 with Dissolve(1)
    mc "Not a bad way to die!"
    el "You're supposed to be dead! You can't talk."
    mc "That's just the nerves."
    el "Uh-huh... I can feel another nerve too!"
    mc "{i}(... I can't help it.){/i}"
    scene 10_2257 with Dissolve(1)
    ma "We did it! We defeated Sandman once and for all!"
    di "But he fell on Elena and crushed her!"
    ma "It was a worthy sacrifice to save humanity!"
    scene 10_2258 with Dissolve(1)
    el "What? Are you kidding me? Why did I have to die too?"
    mc "Haha. RIP!"
    el "Quiet you!"
    el "You're supposed to save the pretty girl!"
    scene 10_2259 with Dissolve(1)
    ma "But you're not pretty..."
    mc "{i}(Oh no, they didn't...){/i}"
    el "..."
    ma "Haha. Diego, run!"
    menu:
        "Laugh":
            scene 10_2260 with Dissolve(1)
            mc "Haha."
            el "..."
            el "Of course, you find this funny!"
            el "How about you get off me now, Sandboy!"
        "Hero[KoGa3AutoWTChange1]{size=-4}(Elena Week5 Monday Beach Hero, Elena Points+2) {/size} {/color}":
            $ Elena_Week5_Monday_Beach_Hero = True
            $ Elena_Points += 2
            # Elena (40)
            scene 10_2261 with Dissolve(1)
            mc "Just an FYI."
            mc "I think you're pretty!"
            el "..."
            mc "{i}(Very pretty in fact. Seeing her this up close...){/i}"
            mc "And if I was the hero, I would've saved you!"
            scene 10_2262 with Dissolve(1)
            mc "Hell... I even would've sacrificed myself to..."
            el "Okay, okay, I get it!"
            el "How about you get off me now, Sandboy!"
            scene 10_2263 with Dissolve(1)
            mc "But this is so nice!"
            el "If you want to lie on top of me so bad, use Magdalena!"
            mc "She's not as good as you!"
            el "..."
    scene black with Dissolve(1)
    pause 2
    scene 10_2264 with Dissolve(1)
    mc "Uh, Elena?"
    el "Hmm?"
    mc "Sorry about before... You know..."
    el "Oh, the blood rushing to your head?"
    mc "Heh? Yeah... That..."
    scene 10_2265 with Dissolve(1)
    el "It's fine. I know boys can't help it sometimes. Not the first time it's happened, either."
    mc "What?"
    el "Remember back at school. When you fell on me."
    mc "Hmm?"
    scene 10_2266 with Dissolve(1)
    mc "Oh! That time... On the grass."
    mc "Shit! Did you feel that? I'm sorry."
    mc "{i}(I didn't think she would be this chill about that.){/i}"
    mc "{i}(The more time I spend with her, the more...){/i}"
    mc "*Sigh*"
    scene 10_2267 with Dissolve(1)
    mc "Can I ask you a question?"
    el "Do I have a choice?"
    mc "Yeah, that's why I asked."
    el "Then no."
    mc "Haha, okay."
    scene 10_2268 with Dissolve(1)
    el "Can I ask you a question?"
    menu:
        "Yes":
            mc "*Sigh* Sure, I guess..."
        "No":
            mc "No..."
            el "Well tough luck. I'll ask anyway."
            mc "Heh... Where's my choice?"
            el "You don't get one!"
    scene 10_2269 with Dissolve(1)
    el "What's the question you wanted to ask me?"
    mc "Why don't you have a boyfriend?"
    el "Hmm, okay."
    mc "Okay? That's your answer?"
    scene 10_2270 with Dissolve(1)
    el "No. Your 'why don't you have a boyfriend' was the answer to my question, not a question itself, technically."
    mc "ELENA!"
    el "Haha."
    scene 10_2271 with Dissolve(1)
    mc "No, but seriously. Why don't you have a boyfriend?"
    mc "You're beautiful, funny, caring. Very direct, but that's also part of the charm, right?"
    el "..."
    scene 10_2272 with Dissolve(1)
    el "Because I'm into girls!"
    mc "Wait... What? You are? Really? Wow... Could've fooled me."
    mc "But that explains why you kissed Layla on the train."
    el "I was just drunk. I kissed you too!"
    mc "Right... This is getting confusing now. I had no idea you like girls though..."
    scene 10_2273 with Dissolve(1)
    el "..."
    mc "..."
    scene 10_2274 with Dissolve(1)
    mc "You asshole! I knew it! I almost believed you!"
    el "Haha. Took you long enough."
    mc "..."
    scene black with Dissolve(1)
    pause 2
    scene 10_2275 with Dissolve(1)
    mc "What's your type?"
    el "I don't know. I don't really have a type."
    el "I don't like pretty boys, though."
    scene 10_2276 with Dissolve(1)
    mc "What a coincidence. Me neither."
    el "Haha."
    mc "Pretty boys are the worst!"
    scene 10_2277 with Dissolve(1)
    el "So, pretty boys are the worst. Spending time with me is second worst."
    el "I'm learning so much about you today."
    mc "Right? Isn't it great?"
    el "Eh..."
    scene 10_2278 with Dissolve(1)
    mc "So you don't have a type... Hmm... Maybe... someone you're interested in?"
    el "Maybe."
    mc "Maybe?"
    el "There's this one guy..."
    mc "Yeah? There's a guy? Miguel?"
    scene 10_2279 with Dissolve(1)
    el "What? No! Not Miguel! Are you kidding me?"
    mc "He's interested in you."
    el "I know that. He makes it quite obvious. Still, no reason for me to be interested in him!"
    mc "Why aren't you together with that mystery guy?"
    scene 10_2280 with Dissolve(1)
    el "Because he's in a relationship."
    mc "He took another girl instead of you?"
    mc "Haha. What an idiot."
    mc "You call me an idiot all the time. But that guy is on a whole nother level."
    scene 10_2281 with Dissolve(1)
    mc "Anyway. Him having a girlfriend doesn't matter. Look at you, you're a catch. So much better than that other girl."
    mc "He'll realise that one day."
    el "..."
    scene 10_2282 with Dissolve(1)
    el "She's actually pretty awesome."
    mc "Pssh. She might be, the guy is still an idiot though."
    el "He is. Sometimes... But he has his moments."
    scene 10_2283 with Dissolve(1)
    mc "I meant everything I said, though. You're amazing, Elena!"
    el "Thanks."
    mc "Sometimes even cute..."
    scene 10_2284 with Dissolve(1)
    mc "Especially when you roll your eyes, you know that?"
    el "Dios mío..."
    mc "Yes! Exactly like that!"
    el "..."
    scene black with Dissolve(2)
    pause 2
    scene 10_2285 with Dissolve(1)
    ""
    scene 10_2286 with Dissolve(1)
    el "You're pretty good with kids, you know?"
    mc "Yeah? Maybe because I'm still a kid myself."
    el "Haha. You said it. But that's probably the reason."
    mc "Haha."
    scene 10_2287 with Dissolve(1)
    el "And you're not the worst to spend time with, either, pretty boy."
    mc "Nooo... I'm a pretty boy? You're breaking my heart, Elena!"
    el "Heh. Anyway. Thank you for playing with them."
    scene 10_2288 with Dissolve(1)
    mc "You're welcome. I had fun too."
    scene 10_2289 with Dissolve(1)
    mc "Oh... A second one..."
    scene 10_2290 with Dissolve(1)
    el "That one was for me!"
    ma "Kiss! Kiss! Kiss!"
    el "..."
    di "Kiss. Kiss."
    scene 10_2291 with Dissolve(1)
    el "That's enough you two. Get on the bus!"
    ma "Elena has a boyfriend. Elena has a boyfriend!"
    el "*Sigh*"
    scene 10_2292 with Dissolve(1)
    mc "Maybe we'll see each other tomorrow at Layla's hot tub party."
    el "I'll try."
    mc "Bye, mama."
    scene 10_2293 with Dissolve(1)
    el "Haha. Please, don't ever call me that again."
    mc "No promises!"
    $ renpy.end_replay()
    if Gabi_End == False:
        jump Week5_Monday_Gabi
    else:
        jump Week5_Monday_End

label Week5_Monday_End:
    jump Episode_11_Start

# Max Points:

# Alexis (44)
# Melissa (18)
# Layla (76)
# Elena (40)
# Emily (20)
# Erynn (54)
# Tori (16)
# Cara (16)
# Nikki (20)
# Lakeyn (6)
# Brooke (6)
# Adriana (2)
# Naomi (2)
# Valeria (26)
# Zach (10)
# Darryl (2)
# ShaCarri (4)
# Iris (2)

# MC_GoodStudent (14)

# Nikki_Weekend (10)
# Nikki_Visit (40)
# Cara_Weekend (6)
# Cara_Visit (44)
# Alexis_SP (2)
# Alexis_Jealous (4)

# MC_Sex (32)
# Alexis_Sex (9)
# Tori_Sex (2)
# Lakeyn_Sex (1)
# Nikki_Sex (6)
# Cara_Sex (7)
# Julia_Sex (1)
# Rachel_Sex (1)
# Gabi_Sex (3)
# Iris_Sex (2)

#WTAdded
label Episode_8_Start:

    #KoGa3 START#
    $ KoGa3GameProgress = "Ep8"
    #KoGa3 END#

    $ achievement.grant("ACHIEVEMENT_EPISODE_7")
    $ achievement.sync()
    $ Erynn_Week3_Wednesday_Lying = False
    $ Zach_Week3_Wednesday_Seats = False
    $ Valeria_Week3_Wednesday_Pictures = False
    $ Layla_Week3_Wednesday_TC_Kiss = False
    $ Layla_Week3_Wednesday_TC_TrainingPartner = False
    $ Tori_Week3_Wednesday_TC_Fun = False
    $ Layla_Week3_Wednesday_TC_AlexisTalk = False
    $ Zach_Week3_Wednesday_TC_Girlshower = False
    $ Iris_Week3_Sunday_Meet = False
    $ Alexis_Week3_Wednesday_TC_Breakup = False
    $ Layla_Week3_Wednesday_TC_Alexis_DateBoth = False
    $ Layla_LikeMC = False
    $ Layla_Dating = False
    $ Alexis_Dating = False
    $ Valeria_Week3_Thursday_TC_Massage = False
    $ Alexis_Week3_Wednesday_TC_FriendsButKissedLayla = True
    $ Zach_Week3_Thursday_TC_Box = False
    $ Layla_Week3_Friday_TC_Wager = False
    $ TC_Pool_Layla = False
    $ TC_Pool_Elena = False
    $ TC_Pool_Sienna = False
    $ TC_Pool_Valeria = False
    $ Tori_Week3_Friday_TC_Step = False
    $ Gabi_Week3_Friday_TC_Picture = False
    $ Week3_Friday_TC_Kickball = False
    $ ShaCarri_End = False
    $ MC_Week3_Saturday_TC_Win = False
    $ Tori_End = False
    $ Tori_LickAss = False
    $ Tori_Week3_Saturday_TC_Sex = False
    $ Tori_Week3_Saturday_TC_LickAss = False
    $ MC_Week3_Saturday_TC_Cheer_Late = False
    $ Gabi_Week3_Saturday_TC_Sex = False
    $ Gabi_Week3_Saturday_TC_CumInside = False
    $ Valeria_Week3_Saturday_Tea = False
    $ Adriana_Week3_Saturday_TC_Pick = False
    $ Elena_Week3_Saturday_TC_Threewaykiss = False
    $ Valeria_Week3_Saturday_TC_Swap = False
    $ Zach_Week3_Saturday_TC_Swap = False
    $ Layla_Week3_Saturday_TC_Swap = False
    $ Valeria_Week3_Saturday_TC_Peek = False
    $ Emily_Week3_Sunday_DareTell = False
    $ Emily_Week3_Sunday_Surprise = False
    $ Alexis_Week3_Sunday_BubbleIce = False
    $ Alexis_Week3_Sunday_Meet = False
    $ Erynn_LikeMC = False
    $ Iris_Week3_Sunday_Meet = False
    $ Alexis_Girlfriend = False
    $ Alexis_Week4_Monday_Meet = False
    $ Alexis_Week3_Sunday_PizzaJoke = False
    $ Alexis_Week3_Sunday_Dorm_StripteaseCute = False
    $ Layla_Week4_Monday_FailTest = False
    $ Alexis_SecretPath = False
    $ Layla_Week4_Monday_Hottub = False
    $ Layla_Week4_Monday_Hottub_BJ = False
    $ Alexis_Week3_Sunday_NewBartender = False

    if Alexis_Week3_Tuesday_Date == True:
        jump Week3_Wednesday_Alexis
    else:
        if Erynn_Week3_Monday_Blackmailhelp == False:
            jump Week3_Wednesday_School
        else:
            jump Week3_Wednesday_Erynn

label Week3_Wednesday_Alexis:
    if _in_replay:
        $ SexCounter_Alexis = 6
        $ MC_SexCounter = 6
        $ Alexis_Points = 36
    $ SexCounter_Alexis += 1
    $ MC_SexCounter += 1
    scene black with Dissolve(2)
    n "Wednesday, 07:42."
    stop music fadeout 1.0
    play music ("Music/LoFi Indie 3.mp3", "Music/LoFi Indie 1.mp3", "Music/LoFi Indie 2.mp3") volume 0.2
    pause 2
    scene 08_001 with Dissolve(1)
    mc "Hey, can you come back in?"
    a "I want to, but I don't have much time."
    mc "..."
    a "I need to leave soon or I'll be late for class."
    scene 08_002 with Dissolve(1)
    mc "Five minutes?"
    a "I'm sorry."
    mc "{i}(Last time she got into trouble when she stayed. I'd better let her leave on time.){/i}"
    scene 08_003 with Dissolve(1)
    mc "I guess I'll come to you then."
    a "Hehe..."
    mc "I'm happy you were lying next to me when I woke up. You look really cute when you sleep."
    scene 08_004 with Dissolve(1)
    a "Only when I sleep?"
    mc "No! You're always cute!"
    a "Uh-huh... I know what you're doing."
    mc "Giving you a compliment?"
    a "I can feel your compliment!"
    scene 08_005 with Dissolve(1)
    a "Seriously. Again?"
    mc "Haha. Can you blame me?"
    a "..."
    mc "Just look in the mirror. You can see what I have to look at all the time."
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 08_006 at moveup
    pause 3
    a "..."
    mc "Gorgeous, isn't she?"
    mc "I love ... touching and kissing her."
    mc "{i}(Fuck, I'm becoming horny again.){/i}"
    scene 08_007 with Dissolve(1)
    a "Idiot..."
    a "{i}(For a moment I thought he'd say...){/i}"
    scene 08_008 with Dissolve(1)
    mc "You smell just like me."
    a "Maybe because I used your shower gel."
    mc "I'll buy some shower gel and shampoo for you next time, so you'll have them here when you stay over."
    a "Thank you."
    menu:
        "Raspberry[KoGa3AutoWTChange1]{size=-4}(Alexis Points+2) {/size} {/color}":
            $ Alexis_Points += 2
            # Alexis (38)
            scene 08_009 with Dissolve(1)
            mc "Something fruity, raspberry, was it?"
            a "Haha, yes."
            a "{i}(Why does that make me so happy?){/i}"
        "Strawberry":
            mc "Something fruity, strawberry maybe?"
            a "Yeah, strawberry is fine."
    scene black with Dissolve(1)
    pause 2
    scene 08_010 with Dissolve(1)
    mc "*Sigh*"
    a "What?"
    mc "I can't wait for Sunday. I'm going to miss you."
    a "I'll miss you too."
    scene 08_011 with Dissolve(1)
    a "..."
    a "{i}(I guess I have a few minutes...){/i}"
    scene 08_012 with Dissolve(1)
    a "How fast can you be?"
    mc "{i}(Does she mean?){/i}"
    mc "Uhm... I'm so horny right now, I'd be surprised if I lasted longer than a minute."
    a "Heh. A minute?"
    scene 08_013 with Dissolve(1)
    a "..."
    scene 08_014 with Dissolve(1)
    a "Time is ticking. If you keep kissing me, there won't..."
    mc "Don't worry about that. I lied about that minute. It's more like twenty seconds."
    a "Haha."
    scene 08_015 with Dissolve(1)
    mc "{i}(She's just as horny as I am. She's so wet already...){/i}"
    scene 08_016 with Dissolve(1)
    mc "{i}(Seeing myself in the mirror while having sex is so weird.){/i}"
    mc "{i}(Do I always make those weird faces?){/i}"
    scene 08_017 with Dissolve(1)
    a "*Moaning*"
    mc "{i}(But the good thing is I can see so much more of Lexi.){/i}"
    scene 08_018 with Dissolve(1)
    a "{i}(Is he watching himself in the mirror?){/i}"
    a "{i}(That's so funny, but hot at the same time, seeing him fuck me.){/i}"
    scene 08_019 with Dissolve(1)
    a "*Moaning* Mmm, keep going."
    show 08_020
    mc "{i}(Fuck, this feels so good.){/i}"
    scene 08_021 with Dissolve(1)
    mc "{i}(I slipped out...){/i}"
    scene 08_022 with Dissolve(1)
    ""
    show 08_023
    a "AAAH!"
    a "That is my..."
    mc "Shit... Sorry!"
    scene black with Dissolve(1)
    pause 2
    scene 08_024 with Dissolve(1)
    a "Ouch..."
    mc "Are you alright?"
    a "That hurt!"
    mc "I'm so sorry."
    scene 08_025 with Dissolve(1)
    m "Everything alright?"
    mc "{i}(Oh shit!){/i}"
    mc "Uhm... Yeah. There was... a spider."
    m "Since when are you scared of spiders?"
    mc "Uh, I'm not but it came out of nowhere and surprised me!"
    scene 08_026 with Dissolve(1)
    mc "See what I did there? Came out of..."
    a "Not funny, [mc]!"
    mc "Want me to kiss it to make it feel better?"
    a "[mc]!"
    mc "It's a little funny."
    a "For you maybe."
    scene black with Dissolve(1)
    pause 2
    scene 08_027 with Dissolve(1)
    mc "{i}(Looks like she's in real pain...){/i}"
    mc "{i}(I kinda feel like an asshole now.){/i}"
    mc "{i}(Heh, asshole.){/i}"
    mc "{i}(Wow, now I'm even laughing about my own jokes...){/i}"
    menu:
        "Ask her to continue[KoGa3AutoWTChange1]{size=-4}(Alexis Points-2) {/size} {/color}":
            $ Alexis_Points -= 2
            scene 08_028 with Dissolve(1)
            mc "Are you okay to continue, or...?"
            a "Fuck you!"
            mc "{i}(That's a no.){/i}"
            mc "Sorry."
        "Caress her[KoGa3AutoWTChange1]{size=-4}(Alexis Points-2, Erynn End, Erynn Friends, Erynn Week3 Monday BlackmailhelpFalse) {/size} {/color}":
            scene 08_029 with Dissolve(1)
            mc "Does it still hurt?"
            a "Yes..."
            scene 08_030 with Dissolve(1)
            mc "I'm so sorry."
    scene black with Dissolve(2)
    pause 2
    scene 08_031 with Dissolve(1)
    a "Have you seen my top? Did I leave it in your room?"
    mc "I only saw you grab your panties before, so probably."
    scene 08_032 with Dissolve(1)
    mc "Just run to the room, it isn't far."
    a "Can you give me a towel to cover up, please."
    mc "Just go like this."
    a "Uh-huh... What if your mom sees me? Does she even know I'm here?"
    mc "Be quick!"
    a "*Sigh* ..."
    scene 08_033 with Dissolve(1)
    a "{i}(I don't see anyone. Emily must be downstairs.){/i}"
    mc "*Whispers* Go!"
    scene black with Dissolve(1)
    pause 2
    scene 08_034 with Dissolve(1)
    a "*Heart pounding*"
    a "Haha..."
    a "{i}(I can't believe I just did that.){/i}"
    a "{i}(Why did I even agree to this?){/i}"
    $ renpy.end_replay()
    if Erynn_Week3_Monday_Blackmailhelp == False:
        scene black with Dissolve(1)
        pause 2
        scene 08_103 with Dissolve(1)
        mc "Oh... You're clothed already."
        a "Because I have to leave now."
        a "And why aren't you naked? I had to sneak in here, you should've at least done the same."
        mc "I am not as brave as you."
        a  "..."
        scene 08_104 with Dissolve(1)
        mc "I don't want to go to training camp. I'd rather stay here with you."
        a "It's only a few days. You'll be having lots of fun, so time will fly by."
        mc "*Sigh*"
        scene 08_105 with Dissolve(1)
        a "Okay, enough hugging. I have to go now."
        mc "Can you wait a minute? I'll get ready and take you to the bus stop."
        a "I'm late as it is. I can't miss the next bus."
        a "And you still need to pack for your trip since you didn't do it yesterday."
        a "But there's one thing I still have time for!"
        scene 08_106 with Dissolve(1)
        ""
        scene 08_107 with Dissolve(1)
        a "Don't forget to call me!"
        mc "I won't."
        a "Bye-bye."
        scene 08_108 with Dissolve(1)
        mc "Bye Lexi."
        a "Awww..."
        scene 08_109 with Dissolve(1)
        mc "I'm so sorry. I forgot."
        a "..."
        mc "I really forgot!"
        jump Week3_Wednesday_School
    else:
        scene 08_035 with vpunch
        a "..."
        if Erynn_Week3_Monday_Alexis_Mention == False:
            $ Erynn_Points -= 4
            $ Alexis_Points -= 2
        else:
            pass
        scene 08_036a with Dissolve(1)
        a "Erynn!"
        scene 08_037 with Dissolve(1)
        a "What... Uhm... I..."
        a "I'm sorry. I'm so sorry, Erynn."
        scene 08_038 with Dissolve(1)
        a "I want us to be friends again. I miss you. I miss us."
        a "Can you forgive me, Erynn?"
        a "Please say something."
        scene 08_039 with Dissolve(1)
        er "Can you put some clothes on..."
        a "Sorry."
        scene black with Dissolve(1)
        pause 2
        scene 08_040 with Dissolve(1)
        a "I didn't want this to happen."
        er "..."
        a "It's all my fault."
        scene 08_041 with Dissolve(1)
        mc "Did you make it withou..."
        scene 08_042 with vpunch
        mc "{i}(Oh shit...){/i}"
        mc "Erynn!"
        er "..."
        mc "Uh... Sorry, give me a sec."
        scene black with Dissolve(1)
        pause 2
        if Erynn_Week3_Monday_Makeout == True:
            $ Erynn_Points -= 8
            $ Erynn_End = True
            $ Erynn_Friends = True
            $ Erynn_Week3_Monday_Blackmailhelp = False
            scene 08_043 with Dissolve(1)
            mc "What are you doing here, Erynn?"
            er "The better question would be, what is she doing here?"
            a "Uhm..."
            scene 08_044 with Dissolve(1)
            er "Because we didn't have sex, you called Alexis to finish the job?"
            a "What?"
            mc "..."
            scene 08_045 with Dissolve(1)
            er "He didn't tell you? Feels good being lied to, right?"
            a "..."
            scene 08_046 with Dissolve(1)
            a "Is that true?"
            mc "..."
            menu:
                "Erynn is lying[KoGa3AutoWTChange1]{size=-4}(Erynn Week3 Wednesday Lying) {/size} {/color}":
                    $ Erynn_Week3_Wednesday_Lying = True
                    mc "Of course not. She's lying. It's her way of getting revenge."
                    scene 08_047 with vpunch
                    n "*Slap*"
                    scene 08_048 with Dissolve(1)
                    er "I can't believe you just said that."
                    er "Were you just pretending to like me this whole time just so you can..."
                    er "After all that's happened? I can't believe that you... That you... Never mind."
                    er "I don't want to waste any more time with you! You're just as bad as him."
                    er "Seems like you guys are perfect for each other."
                    scene 08_049 with Dissolve(1)
                    mc "..."
                    a "Erynn, please wait."
                    scene 08_050 with Dissolve(1)
                    a "I'll go after her. We'll talk about this later."
                    a "Can you give me my jacket?"
                    mc "Yeah."
                    scene black with Dissolve(1)
                    pause 2
                    scene 08_051 with Dissolve(1)
                    er "Bye, Emily."
                    m "Uh... Bye Erynn. You're leaving already?"
                    m "{i}(She didn't stay long.){/i}"
                    scene 08_052 with Dissolve(1)
                    a "Bye, Emily."
                    m "Alexis? You were here?"
                    m "{i}(Oh no...){/i}"
                    a "Yeah. I stayed the night."
                    m "Do you want breakfast, coffee?"
                    a "I'm good. Sorry, but I have to go. Bye."
                    m "Okay. Bye..."
                    scene 08_053 with Dissolve(1)
                    m "{i}(What have I done?){/i}"
                "It's true[KoGa3AutoWTChange1]{size=-4}(Alexis Friends, Alexis End) {/size} {/color}":
                    $ Alexis_Friends = True
                    $ Alexis_End = True
                    mc "I'm sorry, Lexi..."
                    scene 08_054 with vpunch
                    n "*Slap*"
                    scene 08_055 with Dissolve(1)
                    a "One day? It took you one day to cheat on me?"
                    mc "..."
                    a "Really? You have nothing to say about that?"
                    a "We are done! We are so done!"
                    a "I'm so sorry, Erynn."
                    scene 08_056 with Dissolve(1)
                    mc "..."
                    er "Lexi. Wait!"
                    scene 08_057 with Dissolve(1)
                    er "We're done too!"
                    er "I don't want to waste any more time with you! You're just as bad as..."
                    scene black with Dissolve(1)
                    pause 2
                    scene 08_052a with Dissolve(1)
                    m "Alexis? You were here?"
                    m "{i}(Oh no...){/i}"
                    a "Yeah. I stayed the night."
                    m "Do you want breakfast, coffee?"
                    a "Sorry, but I have to go. Bye."
                    m "Okay. Bye..."
                    scene 08_051a with Dissolve(1)
                    er "Bye, Emily."
                    m "Uh... Bye, Erynn..."
                    scene 08_053 with Dissolve(1)
                    m "{i}(What have I done?){/i}"
            scene black with Dissolve(1)
            pause 2
            scene 08_058 with Dissolve(1)
            m "Hey. Are you alright?"
            mc "No..."
            m "I'm so sorry. I sent Erynn up. I didn't know Alexis was here."
            menu:
                "Blame her[KoGa3AutoWTChange1]{size=-4}(Emily Points-4) {/size} {/color}":
                    $ Emily_Points -= 4
                    scene 08_059 with Dissolve(1)
                    mc "Why would you even send her up here?"
                    mc "At least let me know she's here first!"
                    m "I'm sorry. Next time..."
                    mc "There won't be a next time!"
                    m "..."
                    m "I'm so sorry, [mc]."
                "My fault":
                    scene 08_059a with Dissolve(1)
                    mc "Don't worry. It wasn't about that. It was my fault."
                    m "Do you want to talk about it?"
                    mc "No, not really..."
            jump Week3_Wednesday_School
        else:
            scene 08_043a with Dissolve(1)
            mc "What are you doing here?"
            er "I wanted to see you because you'll be gone till Sunday."
            a "..."
            er "And I came over to drive you to school."
            mc "Oh... Thank you."
            scene 08_060 with Dissolve(1)
            er "But it seems like you already have a ride..."
            a "Uhm, no... I was just... I have to leave anyway."
            scene 08_061 with Dissolve(1)
            mc "*Sigh* Can't you guys just talk it out already?"
            er "..."
            a "..."
            mc "Seriously?"
            scene 08_062 with Dissolve(1)
            a "I'd better go now or I won't make it in time."
            a "Have fun at training camp and good luck with the competition."
            mc "Thanks."
            a "I'll see you when you're back?"
            mc "Yeah. And I'll call you as promised."
            menu:
                "Kiss lips[KoGa3AutoWTChange1]{size=-4}(Erynn Points-2) {/size} {/color}":
                    $ Erynn_Points -= 2
                    scene 08_064 with Dissolve(1)
                    er "..."
                "Kiss cheek":
                    scene 08_063 with Dissolve(1)
                    ""
            scene 08_065 with Dissolve(1)
            a "Erynn, can we meet up sometime this week, please?"
            a "I'll call you later, okay?"
            er "..."
            scene 08_066 with Dissolve(1)
            a "Bye-bye."
            mc "Wait, I'll see you out."
            a "It's fine. Stay here with Erynn."
            mc "Alright. Bye, Lexi."
            scene black with Dissolve(1)
            pause 2
            scene 08_052 with Dissolve(1)
            a "Bye, Emily."
            m "Alexis? You were here?"
            m "{i}(Oh no...){/i}"
            a "Yeah. I stayed the night."
            m "Do you want breakfast, coffee?"
            a "I'm sorry, I really can't stay this time, but thank you."
            m "Okay. Uhm... Bye."
            a "Bye-bye."
            scene 08_053 with Dissolve(1)
            m "{i}(What have I done?){/i}"
            scene black with Dissolve(1)
            pause 2
            if Erynn_Week3_Monday_Alexis_Mention == False:
                $ Erynn_Week3_Monday_Alexis_Mention = True
                scene 08_067 with Dissolve(1)
                mc "Sorry about that."
                er "..."
                er "Why didn't you tell me you're dating Alexis?"
                er "Is everyone keeping stuff from me now?"
                scene 08_068 with Dissolve(1)
                mc "I'm sorry. You're right. I should've told you when I was at your place, but you had so much on your mind that day already."
                mc "I didn't know how serious it was until we went on a date yesterday."
                scene 08_069 with Dissolve(1)
                mc "I'm really sorry, Erynn."
                er "It's fine. But please, let's agree to talk about stuff. I don't want another misunderstanding happening like years ago..."
                mc "Me neither, trust me."
                mc "Are you okay with me dating her?"
                if Erynn_Friends == False:
                    er "..."
                    er "{i}(I don't know, because I...){/i}"
                    er "Yes."
                else:
                    er "..."
                    er "Yes. But I would've liked to find out another way, though. Not seeing you both naked in your room..."
            else:
                scene 08_070 with Dissolve(1)
                mc "Sorry about that, Erynn."
                er "..."
                er "When you told me you were seeing each other, I didn't think you guys would be that serious already."
                mc "Me neither, to be honest."
            scene black with Dissolve(1)
            pause 2
            scene 08_071 with Dissolve(1)
            er "She really likes you, you know? I can see the way she looks at you."
            er "Keep being nice to her, and please don't hurt her. She's more fragile than you might think."
            mc "{i}(What does she mean by that?){/i}"
            scene 08_072 with Dissolve(1)
            mc "I won't."
            mc "Is that why she doesn't know about the whole Ethan situation?"
            er "Yeah. I don't want to involve her. I'm scared that Ethan will do something to her, too."
            mc "{i}(I bet she would do anything to help you out though. Especially now.){/i}"
            scene 08_073 with Dissolve(1)
            mc "You clearly care a lot about Alexis. Why don't you make up already? You're both miserable without each other."
            mc "Besides, you're in the same boat. She kept something from you because she didn't want to hurt you. You did the same."
            er "..."
            mc "Do me a favour. When she calls you later or tomorrow, please pick up."
            er "*Nods*"
            scene 08_074 with Dissolve(1)
            mc "Thank you."
            scene 08_075 with Dissolve(1)
            mc "Me dating Alexis won't change our relationship, okay?"
            mc "We're friends. We can still hang out like we did the last few weeks."
            mc "{i}(Hmm... Feels like I've said that before...){/i}"
            mc "I'm here for you."
            er "Thank you, [mc]."
            jump Week3_Wednesday_Erynn2

label Week3_Wednesday_Erynn:
    scene black with Dissolve(2)
    pause 2
    stop music fadeout 1.0
    play music ("Music/LoFi Indie 3.mp3", "Music/LoFi Indie 1.mp3", "Music/LoFi Indie 2.mp3") volume 0.2
    scene 08_076 with Dissolve(1)
    mc "{i}(Training camp, huh? I'm so stoked. Will be lots of fun for sure.){/i}"
    mc "{i}(Can't wait for the competition, either.){/i}"
    n "*Guitar sounds*"
    mc "{i}(Hmm... What's that?){/i}"
    scene black with Dissolve(1)
    pause 2
    scene 08_077 with Dissolve(1)
    mc "{i}(Oh... It's Erynn. Didn't know she was here.){/i}"
    mc "{i}(What is she doing? That sounds awful...){/i}"
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 08_078 at moveup
    pause 3
    mc "{i}(Cute...){/i}"
    scene 08_079 with Dissolve(1)
    mc "Hey, Erynn."
    er "Good morning, [mc]."
    mc "What are you doing?"
    scene 08_080 with Dissolve(1)
    er "..."
    er "What are YOU doing?"
    mc "{i}(Oh shit...){/i}"
    scene 08_081 with Dissolve(1)
    mc "Why are you even staring?"
    er "You would stare too if I was naked in front of you."
    mc "Well... Yes, but that's different."
    er "How is that different? That's such a double standard!"
    mc "..."
    mc "Never mind. Be right back."
    scene black with Dissolve(1)
    pause 2
    scene 08_082 with Dissolve(1)
    er "That just answered a few of the thousand questions I had."
    mc "Very funny."
    er "Haha."
    scene 08_083 with Dissolve(1)
    er "So, what did you think of my guitar performance? Sounded good, right?"
    mc "Eh... Good isn't the word I would've used."
    er "Haha."
    mc "You looked sexy doing it, though."
    er "I'll take that!"
    scene 08_084 with Dissolve(1)
    er "But, you're right. It couldn't compare with your 'performance' just now."
    mc "You just keep on going, huh?"
    er "Haha. Sorry, sorry. I'll stop."
    scene 08_085 with Dissolve(1)
    mc "So, what brings you here today?"
    er "I wanted to drive you to school."
    mc "Oh, thank you. That'd be great. Meaning I have a bit more time."
    if Erynn_Friends == True:
        jump Week3_Wednesday_Erynn2
    else:
        scene 08_088 with Dissolve(1)
        er "Uh..."
        mc "{i}(This feels so nice!){/i}"
        scene 08_090 with Dissolve(1)
        er "That's a long hug."
        mc "Just a little longer."
        er "Haha, that's my sentence."
        jump Week3_Wednesday_Erynn2

label Week3_Wednesday_Erynn2:
    scene black with Dissolve(1)
    pause 2
    scene 08_091 with Dissolve(1)
    mc "So, you're staying at Melissa's?"
    er "Yeah. At least for a week."
    mc "Good. Heard anything about Ethan?"
    er "No, nothing, and I hope it stays that way."
    mc "You and me both."
    mc "{i}(Still have an uneasy feeling about all this.){/i}"
    scene 08_092 with Dissolve(1)
    mc "By the way. I remember that top."
    er "Haha, you do?"
    if Erynn_Week2_Tuesday_Shirt == True:
        er "Want to wear it again?"
        mc "No, you look so much better in it than I do."
        er "Haha."
    else:
        er "Want to wear it this time?"
        mc "No, I'm pretty sure you look better in it than I will."
        er "Haha."
    scene 08_093 with Dissolve(1)
    er "You sure? Last chance..."
    mc "{i}(I wouldn't mind you taking off your clothes.){/i}"
    er "I can see you're thinking about it."
    mc "{i}(Snap out of it, [mc]. Stop imagining things...){/i}"
    scene 08_094 with Dissolve(1)
    mc "And what's with you trying to make me wear your clothes?"
    mc "Don't you have a doll to play dress up with?"
    er "I had one, some time ago. A really cute one."
    mc "I know you're talking about me..."
    er "Haha. Am I?"
    mc "..."
    scene 08_095 with Dissolve(1)
    er "I wore this to high school. It's cute, right?"
    mc "{i}(She really likes modelling.){/i}"
    mc "You still wear the clothes you had in high school? So weird."
    er "Hey! It hasn't been that long, okay."
    mc "And yeah, it's cute. I like skirts. On girls..."
    er "Thank you."
    scene 08_096 with Dissolve(1)
    m "You're still not ready? You know you'll have to leave in five minutes?"
    mc "I have a bit more time. Erynn is driving me."
    m "Where's your bag? Have you packed already?"
    mc "I was about to start."
    m "*Sigh*"
    scene 08_097 with Dissolve(1)
    m "I've put some snacks on the kitchen table for the trip."
    mc "Thank you."
    m "Well, I have to go now. Have fun, and good luck with the competition. Call me, okay?"
    mc "Thanks. Bye, Mom."
    scene 08_098 with Dissolve(1)
    m "Oh and Erynn. I'm jealous, so I've decided that the day will come that I'll steal your legs."
    er "Haha. Just let me keep them for a few more years."
    m "Eh... We'll see. They're gorgeous."
    er "Thank you, Emily!"
    scene 08_099 with Dissolve(1)
    mc "{i}(They are gorgeous!){/i}"
    m "Bye, sweethearts."
    er "Bye-bye."
    scene black with Dissolve(1)
    pause 2
    scene 08_100 with Dissolve(1)
    er "I love your mom."
    mc "She loves your legs. Now you know why she's always nice to you."
    er "Haha."
    scene 08_101 with Dissolve(1)
    er "Come on. Let's start packing. I can't believe you didn't do that yesterday."
    mc "I was busy."
    if Alexis_Week3_Tuesday_Date == True:
        er "Right... Alexis..."
    else:
        er "Playing video games was more important?"
    mc "..."
    if Erynn_Points >= 23:
        scene 08_102 with Dissolve(1)
        mc "*Mumbling* You have more than just beautiful legs!"
        er "What?"
        mc "Nothing..."
    else:
        pass
    jump Week3_Wednesday_School_Erynn

label Week3_Wednesday_School_Erynn:
    scene black with Dissolve(1)
    pause 2
    stop music fadeout 1.0
    play music ("Music/LoFi Upbeat 1.mp3", "Music/LoFi Upbeat 2.mp3", "Music/LoFi Upbeat 3.mp3", "Music/LoFi Upbeat 4.mp3") volume 0.2
    scene 08_110 with Dissolve(1)
    er "Lucky! My parking spot was still open."
    mc "Yes, 'your' parking spot."
    er "Hehe."
    scene 08_111 with Dissolve(1)
    er "Maybe I should've brought a backpack so I could sneak onto the bus and join you at training camp."
    mc "That's why you wore one of your high school outfits. I'm connecting the dots now."
    er "Haha."
    x "Uhm... Excuse me, miss."
    scene 08_112 with Dissolve(1)
    tr "This parking is reserved for teachers."
    er "Oh? I'm so sorry. I didn't know."
    er "I'll just drop my friend off and I'll be gone."
    scene 08_113 with Dissolve(1)
    tr "Can't you move it now?"
    er "I'll be very quick."
    tr "..."
    scene 08_114 with Dissolve(1)
    er "Come on... Before she starts complaining again."
    if Gabi_End == False:
            scene black with Dissolve(1)
            transform moveup:
                xalign 0.5 yalign 1.0
                linear 5.0 yalign 0.0
            show 08_115 at moveup
            pause 3
            mc "Looking good today, Ms Ramirez. Real sporty..."
            tr "Uh... Thanks, [mc]."
            tr "..."
            scene 08_116 with Dissolve(1)
            er "You know her?"
    else:
        scene 08_116 with Dissolve(1)
        er "You know her?"
    mc "Yeah, that's my Spanish teacher."
    er "You take Spanish?"
    mc "Easy credits."
    er "That's practically cheating."
    mc "Hehe."
    scene 08_117 with Dissolve(1)
    mc "Anyway, still want to join training camp and deal with all the drama?"
    er "Sure. I would love a do-over at this school."
    er "{i}(Especially one without...){/i}"
    mc "Yeah? What team would you join then?"
    er "I played volleyball, so probably that."
    scene 08_118 with Dissolve(1)
    er "Or maybe the cheerleading squad and do some cheers in those cute uniforms."
    mc "Haha. Could've guessed that."
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 08_119 at moveup
    pause 3
    er "Something like this, right?"
    if Erynn_Friends == False:
        mc "Yeah, looks pretty good!"
        er "Thanks."
    else:
        mc "I wouldn't know."
    scene 08_120 with Dissolve(1)
    z "Oh my goddess... Is this what love feels like?"
    scene 08_121 with Dissolve(1)
    z "Hi... Uh... Erynn."
    mc "{i}(Oh no...){/i}"
    z "You probably don't know me but I'm a big fan."
    z "You're even prettier in person."
    scene 08_122 with Dissolve(1)
    er "Haha, thank you."
    er "You're Zach, right?"
    z "..."
    z "{i}(She knows who I am.){/i}"
    scene 08_123 with Dissolve(1)
    z "Can I take a picture with you?"
    er "Uhm... Sure."
    z "Yeah?"
    scene 08_124 with Dissolve(1)
    z "{i}(This is the best day of my life!){/i}"
    scene 08_125 with Dissolve(1)
    va "Hey. Good morning."
    mc "Morning, Valeria."
    er "Hello."
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 08_126 at moveup
    pause 3
    mc "{i}(Cute but crazy. I know a few more of those.){/i}"
    scene 08_127 with Dissolve(1)
    va "Morning, Zach."
    z "Can we take another one?"
    er "Yeah, go ahead."
    scene 08_128 with Dissolve(1)
    er "Uh..."
    mc "{i}(That idiot!){/i}"
    scene 08_129 with Dissolve(1)
    z "This is the best picture ever. You look so amazing, Erynn."
    z "New background and screensaver."
    z "Prettiest girl I've ever seen. No girl in this school compares to you."
    va "..."
    er "Sorry."
    scene 08_130 with Dissolve(1)
    er "*Whispers* Was that his girlfriend?"
    mc "*Whispers* No, he would've told me if that was the case."
    er "*Whispers* I feel really bad though."
    mc "*Whispers* You didn't do anything wrong. That's just Zach... If he has something on his mind, he becomes oblivious to everything else."
    scene 08_131 with Dissolve(1)
    er "*Whispers* Still. I'm gonna go look for her and apologise."
    er "I have to leave anyway."
    mc "Yeah, before your car gets towed."
    er "That too!"
    scene 08_132 with Dissolve(1)
    z "What? You have to go already?"
    er "Yeah."
    z "Don't you want to come with us to training camp?"
    er "Haha. I would if I could."
    scene 08_133 with Dissolve(1)
    z "That can be arranged. I'll just empty my bag. I don't need those clothes and we can stash the booze in [mc]'s bag."
    z "Do you think you can fit?"
    er "Probably not. Thanks for offering?"
    scene 08_134 with Dissolve(1)
    la "Hey guys. Hi, Erynn."
    er "Good morning."
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 08_135 at moveup
    pause 3
    mc "Hey, Layla, Elena."
    el "Hi."
    scene 08_136 with Dissolve(1)
    la "Are you joining us at training camp, Erynn?"
    z "Yes, she is!"
    er "Haha. No, I just dropped [mc] off. I'm about to leave, actually."
    scene 08_137 with Dissolve(1)
    la "Too bad. You haven't been over to the house in a while. Even Dad asked about you."
    la "You should come by again some time."
    er "..."
    er "Sorry, I've been really busy lately."
    scene 08_138 with Dissolve(1)
    er "Well, I'm leaving now."
    z "Come on, just stay!"
    er "Enjoy training camp. Have lots of fun."
    la "Thank you. We will."
    scene 08_139 with Dissolve(1)
    er "I'll see you once you're back on Sunday, then?"
    mc "Maybe. If not, on Monday."
    er "Call me and tell me how it's going, alright?"
    mc "Sure, will do."
    er "*Whisper* And try to win!"
    mc "Hehe. I'll do my best."
    if Erynn_Friends == True:
        mc "Bye, Erynn."
        er "Bye-bye."
    else:
        scene 08_140 with Dissolve(1)
        mc "Bye, Erynn."
        er "Bye-bye."
        if Layla_Friends == True:
            pass
        else:
            scene 08_137 with Dissolve(1)
            la "You and Erynn seem to be good friends again."
            mc "We are."
            la "Just friends?"
            menu:
                "Friends[KoGa3AutoWTChange1]{size=-4}(Erynn Friends, Erynn Points-4) {/size} {/color}":
                    $ Erynn_Friends = True
                    $ Erynn_Points -= 4
                    mc "Yes. Just friends."
                    er "..."
                "More than friends[KoGa3AutoWTChange1]{size=-4}(Layla Friends, Layla Points-4) {/size} {/color}":
                    $ Layla_Friends = True
                    $ Layla_Points -= 4
                    scene 08_141 with Dissolve(1)
                    mc "..."
                    if Alexis_Friends == True:
                        mc "I don't know. Maybe a little more than friends."
                    else:
                        mc "I don't know, to be honest."
                    la "Hmm..."
    jump Week3_Wednesday_Busride

label Week3_Wednesday_School:
    scene black with Dissolve(2)
    pause 2
    stop music fadeout 1.0
    play music ("Music/LoFi Upbeat 1.mp3", "Music/LoFi Upbeat 2.mp3", "Music/LoFi Upbeat 3.mp3", "Music/LoFi Upbeat 4.mp3") volume 0.2
    n "Wednesday, 08:13. School."
    scene 08_142 with Dissolve(1)
    mc "Hey, Zach."
    z "Yo. What's up."
    scene 08_143 with Dissolve(1)
    z "Let me tell you. I'm so stoked for training camp."
    z "I have a feeling good things will happen."
    mc "I'm up for some good things."
    scene 08_144 with Dissolve(1)
    z "Look, I brought lots of stuff."
    mc "Haha, you're crazy. Let's hope the teachers don't check our bags."
    z "They aren't allowed to go through our stuff."
    scene 08_145 with Dissolve(1)
    z "We just need to sneak out of our room and join up with the girls to have some fun."
    z "Or invite them to our room. Whatever's easiest."
    mc "Yeah, I'll talk to Layla and Elena about it."
    z "Cool."
    scene 08_146 with Dissolve(1)
    z "Oh shit! Look at that car."
    z "How can teachers afford such a car with their salary?"
    z "Who is that anyway?"
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 08_147 at moveup
    pause 3
    z "It's Gabi. I didn't know she drives such a car."
    z "She just increased her ranking on my list."
    mc "..."
    scene 08_148 with Dissolve(1)
    mc "What's with that huge suitcase though."
    z "Maybe she brought lots of booze too?"
    mc "Haha. I don't think so."
    z "Well then, maybe some sexy lingerie and dresses."
    mc "Why would she bring that?"
    z "I don't know. Wishful thinking."
    if Gabi_End == False:
        scene 08_149 with Dissolve(1)
        z "Good morning, Gabi, uh... Ms Ramirez."
        tr "Good morning."
        z "Looking good today. Very sporty!"
        tr "Thank you."
        scene 08_149a with Dissolve(1)
        z "Do you need any help with your suitcase?"
        tr "I'm good. Thank you, Zach."
        scene 08_150 with Dissolve(1)
        z "Just look at her."
        z "Have you ever seen a hotter teacher?"
    else:
        scene 08_150 with Dissolve(1)
        z "Just look at her."
        z "Have you ever seen a hotter teacher?"
    scene 08_151 with Dissolve(1)
    va "Good morning."
    mc "Hey, Valeria."
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 08_126 at moveup
    pause 3
    mc "{i}(Cute but crazy. I know a few more of those.){/i}"
    scene 08_152 with Dissolve(1)
    va "Morning, Zach."
    z "That juicy ass..."
    z "Not a single girl in this school compares to Gabi."
    mc "{i}(Just shut up, Zach!){/i}"
    scene 08_153 with Dissolve(1)
    z "I would do anything to fuck her."
    va "..."
    mc "Uhm, Zach."
    z "Wouldn't you?"
    mc "{i}(Zach, stop!){/i}"
    scene 08_154 with Dissolve(1)
    va "See you later!"
    z "Squeeze her big tits, suck on her nipples..."
    mc "Uh, yeah... Later, Val."
    z "What later? NOW!"
    mc "{i}(You're always digging your own grave.){/i}"
    scene 08_155 with Dissolve(1)
    z "Oh hey, Val. Good morning."
    va "..."
    z "Good morning, Valeria!"
    scene 08_156 with Dissolve(1)
    z "Didn't she hear me?"
    mc "{i}(She heard you. More than you think.){/i}"
    z "Probably listening to music again. She could at least say good morning..."
    scene 08_157 with Dissolve(1)
    z "Anyway. I'm planning something for her at training camp."
    z "She won't be able to resist me after that."
    mc "{i}(That ship might have sailed just now.){/i}"
    mc "Yeah? What's that?"
    z "I don't know yet, but what I know is that she's going to lose something."
    mc "{i}(You have no idea how hard I'm facepalming myself in my mind.){/i}"
    scene 08_158 with Dissolve(1)
    el "Who's going to lose something?"
    z "Uh... What? No one... Haha."
    el "Sus!"
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 08_135 at moveup
    pause 3
    mc "Hey, Layla, Elena."
    la "Hey, [mc]."
    jump Week3_Wednesday_Busride

label Week3_Wednesday_Busride:
    scene black with Dissolve(1)
    pause 2
    scene 08_159 with Dissolve(1)
    la "The buses are here already."
    el "Let's go wait there then. I don't want to sit at the front again like last year."
    la "Indeed."
    scene 08_160 with Dissolve(1)
    la "If you want a good seat, you'd better do the same."
    mc "Yeah, I'm gonna go to the bathroom real quick, though."
    la "Better hurry, they fill up quick!"
    scene black with Dissolve(1)
    pause 2
    scene 08_161 with Dissolve(1)
    el "Really? There are plenty of seats. You had to sit behind us?"
    z "Yeah, we can play some games or something. It will be fun."
    el "*Sigh* So much fun!"
    el "At least sit behind me, so I don't have to see your face every time I turn around."
    z "Don't turn around then..."
    scene 08_162 with Dissolve(1)
    mg "Zachy! Thanks for the seat."
    z "Uh... This was actually for Valeria."
    scene 08_163 with Dissolve(1)
    mg "*Whisper* Oh come on, man. You know I have a thing for Elena. Let me sit here so I can chat with her a bit."
    z "*Whisper* I had plans too, you know."
    mg "*Whisper* Just this once."
    z "*Sigh* Sure. But on the way back, this is Valeria's seat."
    mg "Hey, I owe you. Big time."
    scene 08_164 with Dissolve(1)
    mg "Hola, Elena."
    el "Hey, Miki. Qué tal?"
    mg "Cómo estás?"
    scene black with Dissolve(1)
    pause 2
    scene 08_165 with Dissolve(1)
    mc "I thought you wanted to sit in the back."
    la "The guys from the football team are sitting there and they are always loud."
    la "So, we'd rather sit here."
    if Layla_Week3_Tuesday_Train == True:
        scene 08_166 with Dissolve(1)
        la "Don't fall asleep!"
        mc "Haha, I won't."
    else:
        pass
    scene 08_167 with Dissolve(1)
    la "Not feeling lonely sitting there on your own?"
    mc "I don't mind. I have all this space for myself!"
    if Layla_Friends == True:
        la "True. I should've thought about that..."
        el "You can sit somewhere else, you know..."
    else:
        la "True. But I might switch during the ride and claim that spot."
        mc "Sure. Be my guest."
    scene black with Dissolve(1)
    pause 2
    scene 08_168 with Dissolve(1)
    z "Hey, Val! Sorry. I had this seat for you but Miguel wanted to sit here and..."
    mg "Okay, okay, I get it. I'll go sit somewhere else."
    z "Thanks, man."
    scene 08_169 with Dissolve(1)
    va "No-no, just stay. I don't want to sit there anyway."
    z "What? Why?"
    if Layla_Points >= 43:
        scene 08_170 with Dissolve(1)
        va "Hey, [mc]. Is this seat taken or can I sit there?"
        mc "Uh... Yeah sure. Want the window or this one?"
        va "The window seat if you don't mind."
        mc "Let me get up."
        va "Don't worry. I can get through."
        scene 08_171 with Dissolve(1)
        mc "..."
    else:
        scene 08_170_01 with Dissolve(1)
        va "Hey, [mc], is this seat taken or can I sit there?"
        mc "Uh... Yeah sure. Want the window or this one?"
        va "The window seat if you don't mind."
        mc "Let me get up."
        va "Don't worry. I can get through."
        scene 08_171_01 with Dissolve(1)
        mc "..."
    scene 08_172 with Dissolve(1)
    va "Uh..."
    mc "Yeah, that was my foot."
    va "Haha. I'm sorry. Maybe this wasn't the smartest idea."
    mc "{i}(Seeing her this close up, she's prettier than I thought.){/i}"
    scene 08_172a with Dissolve(1)
    va "Let me step here."
    mc "My other foot."
    va "Sorry! I'll try to..."
    scene 08_173 with vpunch
    va "Aaah..."
    mc "Haha. Be careful."
    if Layla_Points >= 43:
        scene 08_174 with Dissolve(1)
        la "..."
        la "{i}(Is she doing that on purpose?){/i}"
        scene 08_175 with Dissolve(1)
    else:
        scene 08_175 with Dissolve(1)
    va "Ouch..."
    mc "Are you alright?"
    va "Yeah. Thank you."
    scene 08_176 with Dissolve(1)
    z "Are you alright, Val? Did you hurt yourself?"
    va "..."
    va "I'm good!"
    scene 08_177 with Dissolve(1)
    mc "Now I know why you're wearing that hat. To hide all the bumps from falling and tripping."
    va "Haha. And here I was hoping no one would find out my secret."
    scene 08_178 with Dissolve(1)
    mc "No, but seriously. Why are you wearing the hat? Some fashion statement?"
    va "Haha, not really, no."
    va "My hair was still wet this morning."
    va "I was running late and didn't have time to blow-dry it. Hence the hat."
    scene 08_179 with Dissolve(1)
    va "Don't you like it?"
    menu:
        "No":
            mc "Honest answer?"
            va "Please."
            mc "No, not really."
            va "Haha."
            mc "Isn't it damp or moist?"
        "It's fine":
            mc "It's fine. I was just thinking that it would be hot with it on."
            mc "Or at least damp or moist."
    scene 08_180 with Dissolve(1)
    va "Ew... Don't say that word. I hate it."
    mc "Moist?"
    va "Yes, that one."
    mc "Haha."
    va "I'll take it off."
    scene black with Dissolve(1)
    pause 2
    scene 08_181 with Dissolve(1)
    va "There... Better?"
    mc "Uh-huh."
    scene 08_182 with Dissolve(1)
    mc "How does it feel? Still moist?"
    va "No..."
    mc "What's wrong with moist?"
    scene 08_183 with Dissolve(1)
    va "Please, [mc]. Stop."
    mc "Haha, sorry."
    mc "{i}(She really hates that word. That's so funny.){/i}"
    scene 08_184 with Dissolve(1)
    mc "Now I understand the crazy part."
    va "What?"
    mc "The text on your top. Cute but crazy."
    va "Oh... Haha. Yeah, maybe a little."
    scene 08_185 with Dissolve(1)
    mc "A little what? Cute or crazy?"
    va "I'll let you decide."
    mc "{i}(I took her as a shy girl at first, but it seems I was mistaken.){/i}"
    mc "{i}(Good luck, Zach! Well, you'll need more than just luck, after what you pulled today.){/i}"
    scene 08_186 with Dissolve(1)
    mc "I have a theory."
    va "Let's hear it."
    mc "I think it's the hat."
    va "Hmm. The hat... I don't follow. Explain."
    scene 08_187 with Dissolve(1)
    mc "Okay, listen to this. When you were wearing the hat, you were this cute, shy-ish girl who trips and falls."
    mc "But once you took it off, your personality and demeanour changed. That's the crazy part."
    mc "Cute and crazy, right?"
    scene 08_188 with Dissolve(1)
    va "You might be on to something here."
    va "Are you brave enough to test your theory?"
    scene 08_189 with Dissolve(1)
    mc "They don't call me brave Sir [mc] for nothing."
    va "Oh, brave Sir [mc], the bravest of the brave. Good, so you won't gallantly chicken out then?"
    mc "No way... You saw the tale of Sir Robin?"
    va "Yeah, a friend sent me the clip. So funny."
    va "But I'm curious about one thing though. What happened to his penis?"
    mc "Haha... My thoughts exactly. I think everyone wants to know."
    scene 08_190 with Dissolve(1)
    la "{i}(Penis? What are they talking about?){/i}"
    la "..."
    z "{i}(What the fuck?){/i}"
    scene 08_191 with Dissolve(1)
    mc "I think we should be able to come up with some possibilities."
    va "Haha."
    scene black with Dissolve(1)
    pause 2
    scene 08_192 with Dissolve(1)
    va "Well, back to the theory."
    mc "Right. The hat."
    va "Here you go."
    mc "Thanks."
    scene black with Dissolve(1)
    pause 2
    scene 08_193 with Dissolve(1)
    mc "Hmm... Nope. Maybe I was wrong. I feel no different."
    va "[mc]! Haha."
    mc "What's so funny?"
    va "Haha. Please take it off. My stomach is already hurting from all the laughing."
    if Layla_Points >= 43:
        scene 08_194 with Dissolve(1)
        la "They're having fun there... Why is she sitting next to him anyway?"
        el "You sound jealous."
        la "..."
        la "I want to have fun too. I should've sat next to him."
        scene 08_195 with Dissolve(1)
        el "Wow... Thanks a lot."
        la "I didn't mean it like that."
        el "Uh-huh. And they say I'm the mean one."
        la "Sorry, El!"
        scene 08_196 with Dissolve(1)
        el "And why are you mad at her for? She's just talking to him. She doesn't know you like [mc]."
        la "..."
        la "You're right..."
        el "If you want to talk to him, Layla, talk to him. He's sitting right there. You're basically sitting next to him."
        scene 08_197 with Dissolve(1)
        va "Haha."
        la "*Sigh*"
    else:
        pass
    scene black with Dissolve(1)
    pause 2
    scene 08_198 with Dissolve(1)
    tr "Okay everyone. Listen up. This is the schedule for today."
    tr "Depending on traffic, the bus ride will take approximately three and a half hours. Expect an arrival around noon."
    tr "We will have lunch. Info about the rest of the week will be explained then."
    tr "After lunch you'll have an hour to get your stuff to your rooms."
    tr "First training starts at two. Don't be late!"
    scene 08_199 with Dissolve(1)
    tr "Any questions?"
    x "Yes. Will we have some free time?"
    tr "It's normal school hours. So from 08:30 to 16:00. After that, you're free to use the facilities as you like."
    tr "Friday will be half a day and also on Saturday, after the competition, you'll have the rest of the day off."
    tr "Any other questions?"
    scene 08_200 with Dissolve(1)
    x "What competition will you be in?"
    tr "Haha. No competition for me. It's all about you."
    x "There should be a competition between the teachers though."
    z "Yeah!"
    scene 08_201 with Dissolve(1)
    x "A competition for the sexiest teacher."
    z "Haha. Yes! You'll win for sure."
    x "GO GABI!"
    tr "*Sigh*"
    tr "I guess there's no more questions..."
    scene 08_202 with Dissolve(1)
    z "Gabi's so hot!"
    mg "Yeah, she's pretty, but I only have eyes for one Latina."
    scene 08_203 with Dissolve(1)
    mg "Right, Elena?"
    el "Sorry, what?"
    mg "No, nothing..."
    scene 08_204 with Dissolve(1)
    z "You're kidding, right?"
    z "You're choosing Elena over Gabi?"
    mg "Of course. She's hella cute and she's got moves..."
    scene 08_205 with Dissolve(1)
    la "Oooh... Someone has a crush on you!"
    el "Stop."
    la "You cutie, you."
    scene 08_206 with Dissolve(1)
    mg "What about your other Latina?"
    z "Who?"
    mg "The one who seems to be angry at you."
    z "Still don't know who you're talking about."
    mg "Dude... Valeria!"
    z "What? She's a Latina?"
    mg "Are you serious?"
    z "And she's mad at me? Why? I didn't do anything to her."
    z "I don't understand women sometimes..."
    scene 08_207 with Dissolve(1)
    mg "Here's a tough decision for you. Gabi or Valeria?"
    z "Man... That's like choosing between pizza and burgers..."
    mg "You are so weird."
    z "Gabi has always been a dream of mine. Bang the hot teacher, you know?"
    z "But I see that more as a one-time thing. Unless she's a crazy nympho chick or something and can't get enough of me."
    mg "..."
    z "If I really had to choose. I think I'd rather pop Valeria's cherry."
    scene 08_208 with Dissolve(1)
    mg "She's a virgin?"
    z "I don't know, actually. I think she is... She seems very inexperienced."
    mg "Says the virgin."
    z "That will change this week!"
    scene black with Dissolve(1)
    pause 2
    scene 08_209 with Dissolve(1)
    va "How do you feel about the competition?"
    mc "Feeling confident."
    va "Yeah? Hmm... I've been watching you during training and..."
    scene 08_210 with Dissolve(1)
    mc "Ooh... You're checking me out, huh?"
    va "Hey now. Don't twist my words."
    scene 08_211 with Dissolve(1)
    va "I meant that Darryl beat you in every race."
    mc "You're right about that. I haven't taken it seriously lately, but I've been training outside of school since I heard about the competition."
    mc "You'll see a different me over the next few days."
    mc "How about you?"
    va "A little nervous maybe? We have some fast girls on the team and I don't know about the other schools. I've heard they're pretty good."
    scene 08_212 with Dissolve(1)
    mc "Speaking of teams, that reminds me. Who are you bunking with? Did you find a group, or were you placed in one?"
    va "I'm with Tori and her friends."
    mc "Wow."
    va "Yeah... It's fine though. I'm only going to be there to sleep, anyway."
    scene 08_213 with Dissolve(1)
    mc "You're always welcome to hang out in our room."
    va "Thanks, as long as Zach isn't there..."
    mc "Oh yeah, Zach. Sorry about before. That's just who he is. He does stupid things and talks a lot. Most of the time it's nonsense, but he's a good guy."
    va "Yeah he's a good guy, but he can be annoying."
    mc "Haha true. Don't tell him that I said that."
    mc "{i}(You have a lot of work to do, Zach!){/i}"
    scene 08_214 with Dissolve(1)
    la "What are you guys talking about?"
    mc "Val is grouped up with Tori and her posse."
    la "Oh joy..."
    la "You can always come hang out in our room."
    scene 08_215 with Dissolve(1)
    va "Thank you, Layla."
    mc "Now you have two options already. At this rate, you'll be invited by everyone before we arrive."
    va "Haha, yes."
    scene black with Dissolve(1)
    pause 2
    scene 08_216 with Dissolve(1)
    va "Where did you move from?"
    mc "Riverside, but I only lived there for about two months."
    va "Heh?"
    mc "Yeah... Long story. Before that, Alvarado."
    mc "But I was actually born and raised here in Madison Springs."
    va "Same. Born here, moved, and now moved back."
    scene 08_217 with Dissolve(1)
    va "Do you like it here?"
    mc "I love it. I didn't know how much I missed this place until I was back. Especially the beach."
    mc "How about you?"
    va "Can't remember much from before since we moved when I was four, but it's slowly growing on me."
    va "I haven't visited the beach yet."
    mc "You have to!"
    scene 08_218 with Dissolve(1)
    va "It's on my agenda during spring break."
    mc "Oh yeah, that's in two weeks already. I'll most likely be there every day."
    va "We might run into each other then."
    mc "It will be packed with tourists, though."
    mc "We'll probably plan something with a few people from school. If you're interested, I'll let you know."
    va "That'd be nice, thank you."
    scene 08_219 with Dissolve(1)
    mc "How long have you been doing track?"
    va "I started with gymnastics when I was seven."
    mc "That early?"
    va "Uh-huh. And I've been on the track team since I was eleven."
    va "Started with middle-distance running until I was fourteen. Switched to pole vault until last year."
    scene 08_220 with Dissolve(1)
    mc "Hold on. Wait a minute. You pole-vaulted?"
    va "Yes."
    mc "No way."
    va "No, really."
    mc "I don't believe you."
    va "Haha, I'll show you then."
    scene black with Dissolve(1)
    pause 2
    scene 08_221 with Dissolve(1)
    va "Here you go."
    mc "Oh damn, Val!"
    scene 08_221a with Dissolve(1)
    z "{i}(What are they looking at? Pictures?){/i}"
    z "{i}(I want to see, too...){/i}"
    scene 08_222 with Dissolve(1)
    mc "You are buff!"
    va "Heh, yeah... That was just before Nationals."
    mc "Nationals? How good were you? I take everything back. I'm so impressed right now."
    scene 08_223 with Dissolve(1)
    mc "Look at those abs... I'm somewhat jealous."
    va "Haha."
    mc "{i}(The only other girl I know who looks this fit is Nikki. She surely has some competition here.){/i}"
    scene 08_224 with Dissolve(1)
    mc "Wow. This is an amazing shot. Seems like you had some room to spare."
    va "Yeah, this was a warm-up jump."
    mc "Still impressive."
    mc "{i}(She's a serious athlete already.){/i}"
    scene 08_225 with Dissolve(1)
    mc "Oh. Also an amazing shot!"
    va "Aaah..."
    scene 08_226 with Dissolve(1)
    va "T-That's... That wasn't pole vaulting..."
    mc "Haha. Definitely not."
    menu:
        "Compliment[KoGa3AutoWTChange1]{size=-4}(Valeria Points+2) {/size} {/color}":
            $ Valeria_Points += 2
            # Valeria (2)
            scene 08_227 with Dissolve(1)
            mc "It's a beautiful picture, you're beautiful."
            va "Thank you."
            mc "{i}(Why is she so embarrassed? It's her in a bikini and she looks amazing...){/i}"
        "Don't say anything":
            pass
    scene black with Dissolve(1)
    pause 2
    scene 08_228 with Dissolve(1)
    mc "Why did you quit pole vaulting?"
    va "Lost interest in it, I guess. Besides I wasn't that good, I'm a better sprinter."
    mc "{i}(Lost interest?){/i}"
    mc "You were at Nationals, meaning you must have been really good."
    va "..."
    scene 08_229 with Dissolve(1)
    x "We've got the heart! We've got the fight!"
    x "We're gonna win the game tonight!"
    mc "There isn't even a game tonight... They should change up the lyrics."
    va "Haha."
    x "We've got the talent! We bring the heat!"
    x "Falcons just can't be beat!"
    scene 08_230 with Dissolve(1)
    mc "Hey Elena. If you need some more cheerleaders, you'll find them in the football team."
    el "Haha."
    z "This isn't cheering. It's called a chant."
    mc "Riiight... And why aren't you with your team and... chanting?"
    z "To keep you guys company, of course."
    scene 08_231 with Dissolve(1)
    x "We've got the heart! We've got..."
    la "Here we go again. I hope they won't be doing this the whole ride."
    scene 08_232 with Dissolve(1)
    la "[mc], don't you know a song we can sing? So we don't have to listen to them?"
    mc "Elena is on the squad, she should know a few."
    el "I'm not doing some cheers like those guys back there."
    z "It's not a cheer! It's a chant, okay!"
    if Elena_Week3_Monday_CheerTraining == True:
        scene 08_233 with Dissolve(1)
        la "So... No song?"
        mc "Well... I kinda know one. But it's very catchy. It will get stuck in your head for the whole ride."
        la "Doesn't matter. Anything is better than that ridiculous cheer."
        z "IT'S A CHANT!"
        mc "Okay, here we go."
        scene 08_234 with Dissolve(1)
        mc "*Sings* Elena has a boyfriend! Elena has a boyfriend!"
        el "You didn't!"
        mc "Haha..."
        el "Thanks for that!"
        mc "It has been stuck in my head for a while now."
        scene 08_235 with Dissolve(1)
        mg "What? You have a boyfriend, Elena?"
        la "Yeah. What he said."
        scene 08_236 with Dissolve(1)
        el "Haha. No, I don't."
        mg "Good!"
        scene 08_237 with Dissolve(1)
        el "It was something my brother was singing when [mc] came over."
        la "[mc] was at your place?"
        el "Yeah, I asked him if he could help me practice my balance. Didn't I tell you?"
        mg "Why didn't you ask me?"
        la "No, you didn't. When was that?"
        el "Monday. Sorry, I thought I'd mentioned it."
        la "What did you do?"
    else:
        scene 08_233 with Dissolve(1)
        la "So, no song?"
        mc "I know a few but I'm surely not singing here on the bus."
        la "Hehe, okay."
    scene 08_238 with Dissolve(1)
    tr "We'll be having a ten-minute pit stop."
    tr "Use this time to use the bathroom or stretch your legs."
    scene black with Dissolve(1)
    pause 2
    scene 08_239 with Dissolve(1)
    z "What have you and Valeria been talking about?"
    mc "All kinds of stuff, really."
    z "Did she talk about me?"
    mc "No."
    z "Is she mad at me or something? Miguel told me."
    mc "Uh... She might be..."
    scene 08_240 with Dissolve(1)
    z "What the fuck? She's the one who ignored me this morning..."
    mc "{i}(Not without reason.){/i}"
    scene 08_241 with Dissolve(1)
    z "Man. Can you do me a favour? Can we switch seats so I can talk to her?"
    menu:
        "Switch seats[KoGa3AutoWTChange1]{size=-4}(Zach Points+2, Zach Week3 Wednesday Seats) {/size} {/color}":
            $ Zach_Points += 2
            $ Zach_Week3_Wednesday_Seats = True
            # Zach (2)
            mc "Yeah, of course, man. No problem."
            z "Thanks."
        "Let Valeria decide":
            mc "I think it's better to let her choose."
            z "Don't worry, it will be fine."
            mc "Ask her at least."
    scene 08_242 with Dissolve(1)
    z "I'll go sit in your seat and wait for her. You take my spot."
    z "If you hear some weird noises later, don't mind them. We are probably cuddling and making out."
    mc "..."
    scene black with Dissolve(1)
    pause 2
    scene 08_243 with Dissolve(1)
    la "What are you doing there?"
    z "I switched seats with [mc] so I can sit next to Valeria."
    la "Did you ask her if you can sit there?"
    z "No..."
    scene 08_244 with Dissolve(1)
    la "That's not how you approach a girl, Zach. She won't like that."
    z "I know her better than you do."
    la "Heh... Okay."
    scene black with Dissolve(1)
    pause 2
    scene 08_245 with Dissolve(1)
    if Zach_Week3_Wednesday_Seats == False:
        $ Valeria_Points += 2
        # Valeria (4)
        la "You should've asked Val if she was okay with it."
        mc "Yeah, that's what I told Zach, but..."
        la "*Sigh*"
        mc "I'll go look for her."
    else:
        $ Valeria_Points -= 2
        $ Layla_Points -= 2
        mc "Zach really wanted to sit next to her, so he can chat with her."
        la "But maybe she doesn't want to? Did you think of that?"
        mc "You're right. We probably should've asked."
        mc "I'll go look for her."
    scene 08_246 with Dissolve(1)
    va "Why are you sitting there?"
    mc "{i}(Too late...){/i}"
    z "I switched seats with [mc] so we can sit next to each other."
    va "I told you already I don't want to sit next to you."
    scene 08_247 with Dissolve(1)
    z "Why are you mad at me?"
    va "Because you never listen when I talk..."
    z "I always listen. You ignored me this morning."
    va "..."
    scene 08_248 with Dissolve(1)
    mc "{i}(Don't look at me like that. I feel terrible as it is already...){/i}"
    mc "Come on. You can sit here."
    scene black with Dissolve(1)
    pause 2
    scene 08_249 with Dissolve(1)
    mc "Sorry. It was my fault."
    va "No, it wasn't. I'm sure it was his idea."
    mc "He wanted to sit next to you and chat."
    va "And he could've asked me. But never does. He only talks and never listens."
    scene 08_250 with Dissolve(1)
    va "I'm really happy that he approached me on my first day and introduced me to others."
    va "He's my first friend since moving here, and he always helps me out. I can't thank him enough for that."
    va "But there are times that he's just too much to handle and I need some space."
    va "Today is such a day."
    va "I will talk to him again later, when I'm ready."
    scene 08_251 with Dissolve(1)
    mc "I'm sorry."
    va "Don't apologise."
    mc "It's also my fault though. I could've asked you as well if you were okay with it. I'm as much to blame as Zach."
    va "See. That's the difference between you and Zach. You feel remorse."
    scene 08_252 with Dissolve(1)
    va "Besides. I like sitting next to you. You let me talk and actually listen to what I say."
    va "It's refreshing."
    va "And you're somewhat funny, too..."
    mc "Somewhat funny. Thanks."
    menu:
        "Hug her[KoGa3AutoWTChange1]{size=-4}(Valeria Points+2) {/size} {/color}":
            $ Valeria_Points += 2
            # Valeria (6)
            mc "I feel like giving you a hug right now."
            va "I'd like that."
            scene 08_253 with Dissolve(1)
            mc "If you ever need someone to vent to, I'm here, okay?"
            va "Thank you!"
            mc "Now that we're friends again. We are friends, right?"
            va "Yes!"
        "Don't hug her":
            mc "If you ever need someone to vent to, I'm here, okay?"
            va "Thank you!"
            mc "Now that we're friends again. We are friends, right?"
            va "Yes!"
    scene 08_254 with Dissolve(1)
    mc "Okay. Can you show me that one picture again?"
    va "Haha. No!"
    mc "Worth a try..."
    scene 08_255 with Dissolve(1)
    va "But we can take a picture together, maybe?"
    mc "Sure."
    scene black with Dissolve(1)
    pause 2
    scene 08_256 with Dissolve(1)
    mc "..."
    scene 08_257 with Dissolve(1)
    la "Hey, no fair! I want to be in the picture too."
    mc "Get in here then."
    scene 08_258 with Dissolve(1)
    el "Me too, me too!"
    scene 08_259 with Dissolve(1)
    ""
    scene 08_260 with Dissolve(1)
    la "I'm really in the mood to take lots of pictures now."
    la "Let's take a few more, Elena."
    el "Thinking what I'm thinking?"
    la "Training camp scrapbook!"
    scene 08_261 with Dissolve(1)
    mc "Can I look at the pictures?"
    va "Sure, here."
    scene 08_262 with Dissolve(1)
    la "Hey Val, get in the picture already."
    va "Oh, me too?"
    la "Of course you too."
    scene 08_263 with Dissolve(1)
    la "Can you send me the picture we just took, later?"
    va "Yeah."
    la "Oh, I also need your number."
    scene black with Dissolve(1)
    pause 2
    scene 08_264a with Dissolve(1)
    mc "{i}(Haha, I look horrible.){/i}"
    mc "{i}(She looks very cute though.){/i}"
    scene 08_264b with Dissolve(1)
    mc "{i}(All of them are so beautiful.){/i}"
    menu:
        "Look at other pictures[KoGa3AutoWTChange1]{size=-4}(Valeria Week3 Wednesday Pictures, Valeria Points-2) {/size} {/color}":
            $ Valeria_Week3_Wednesday_Pictures = True
            $ Valeria_Points -= 2
            mc "{i}(Let's see what other pictures she has.){/i}"
            scene 08_264 with Dissolve(1)
            mc "{i}(That's the one from earlier.){/i}"
            mc "{i}(Seriously, why was she embarrassed about this?){/i}"
            mc "{i}(What a body!){/i}"
            scene 08_264c with Dissolve(1)
            mc "{i}(Oh shit. That's hot...){/i}"
            mc "{i}(Why do girls take that kind of selfie though?){/i}"
            scene 08_264d with Dissolve(1)
            mc "{i}(Another one. No bra.){/i}"
            mc "{i}(Maybe she had a boyfriend and sent it to him? Or maybe she still has a boyfriend? Shouldn't Zach know?){/i}"
            mc "{i}(Well she mentioned he never listens and he surely doesn't want to hear about a boyfriend. So probably not.){/i}"
            mc "{i}(Why do I even care if she has a boyfriend or not?){/i}"
            scene 08_264e with Dissolve(1)
            mc "{i}(Boyfriend or not, I'm kinda getting turned on now.){/i}"
            va "HEY!"
            scene 08_265 with vpunch
            mc "{i}(Shit, that scared me.){/i}"
            va "What are you doing?"
            mc "Uhm... I asked you if I could look at your pictures."
            va "I thought you meant the ones we just took."
            mc "Oh... Sorry."
        "Don't look":
            pass
    scene black with Dissolve(1)
    pause 2
    scene 08_266 with Dissolve(1)
    mc "The pictures are nice."
    va "Yeah?"
    va "Let me see."
    scene 08_267 with Dissolve(1)
    va "Haha, this one is cute."
    mc "You look cute, I look ridiculous."
    va "No, you don't. It's perfect."
    scene black with Dissolve(1)
    pause 2
    scene 08_268 with Dissolve(1)
    la "Hey, you guys want to play a game?"
    mc "What game?"
    la "Some road trip games."
    mc "Hmm sure."
    la "You in, Val?"
    va "Yes."
    la "Cool."
    scene 08_269 with Dissolve(1)
    la "Let's play the alphabet game first."
    mc "What's that?"
    la "We choose a topic and for each letter, you need to name something."
    la "For example famous people, first letter A, we have Abraham Lincoln."
    mc "Okay, got it."
    la "How about we start with animals?"
    mc "Sounds good."
    la "[mc], you start."
    scene 08_270 with Dissolve(1)
    mc "Alligator."
    va "Bear."
    scene 08_271 with Dissolve(1)
    el "C... Hmm. Haha. Why don't I know an animal with a C..."
    mc "Wow Elena. You're gonna be out already."
    el "Aaah... Give me a second."
    el "Crocodile... Pfew."
    scene 08_272 with Dissolve(1)
    z "Crocodile is with a K."
    el "No, it's not! And you shut up. You aren't playing with us!"
    z "Whatever... I'm sure it's with a K."
    scene 08_273 with Dissolve(1)
    va "Cat was another one."
    el "Oh my god... Cat... So obvious."
    scene 08_274 with Dissolve(1)
    el "Layla, your turn."
    la "Donkey."
    el "..."
    el "Why do I feel attacked all of a sudden? Are you calling me a donkey because I took so long with crocodile?"
    la "What? Nooo... Just an animal with a D."
    el "You could've said dog or dolphin..."
    la "Donkey was the first thing that came to mind though, funnily enough."
    el "Uh-huh..."
    scene 08_275 with Dissolve(1)
    mc "Haha."
    el "Why are you laughing now."
    mc "Just thought it was funny how easy arguments start because of nothing really..."
    el "Yeah, yeah, just continue. E!"
    scene 08_276 with Dissolve(1)
    mc "Elena."
    la "Haha."
    el "I'm not an animal, okay? I would hit you if I could reach."
    mc "So wild. Just like..."
    el "[mc]!"
    mc "Sorry, sorry."
    scene black with Dissolve(2)
    pause 2
    scene 08_277 with Dissolve(1)
    mc "Animal starting with E. Hmm..."
    mc "Wait a minute. Are there animals starting with E?"
    el "Haha. That's what you get. Karma at its finest right there."
    mc "Let me think. We gave you time too."
    mc "E..."
    mc "Shit. This is harder than I thought."
    scene 08_278 with Dissolve(1)
    z "That's what she said."
    la "Really, Zach?"
    scene 08_279 with Dissolve(1)
    mc "E... EEE... Emu! Oh yeah."
    el "Lucky you."
    va "Frog."
    el "Giraffe."
    la "Horse."
    scene 08_280 with Dissolve(1)
    mc "I... I... Why do I have all the difficult letters? Seems like this was pre-planned."
    mc "Oh... Eagle was another one with E. Elephant too. How come I know them now..."
    el "Good job, but you need one with I."
    mc "I know, I know."
    mc "Iguana."
    scene 08_281 with Dissolve(1)
    va "Jaguar."
    el "Kangaroo."
    la "Lion."
    mc "Monkey."
    scene 08_282 with Dissolve(1)
    va "Hmm... N..."
    mc "N is also a difficult one. I can't come up with anything either."
    va "Nightingale."
    la "Nice, Val!"
    scene 08_283 with Dissolve(1)
    el "Octopus."
    la "Peacock."
    z "Haha... Pussy and cock."
    scene 08_284 with Dissolve(1)
    aa "SHUT UP, ZACH!"
    z "What? You guys said it!"
    scene black with Dissolve(1)
    pause 2
    scene 08_285 with Dissolve(1)
    mc "Why are you smiling like that?"
    la "No reason."
    mc "Is it because the next letter is Q? I told you it's a set-up..."
    la "Good luck!"
    scene 08_286 with Dissolve(1)
    mc "Quetzalcoatlus. Joke's on you."
    la "What is that? You just made that up."
    mc "No... It's one of those flying dinosaurs. Well, they weren't dinosaurs, but you know what I mean."
    la "That doesn't count."
    mc "Why not?"
    scene 08_287 with Dissolve(1)
    la "Because they are extinct."
    mc "So? When you gave your example about famous people, you said Abraham Lincoln. As far as I know, he's dead too..."
    la "*Sigh* Fair enough."
    el "Val, you're up."
    scene 08_281 with Dissolve(1)
    va "Rabbit."
    el "Snake."
    la "Tiger."
    scene 08_288 with Dissolve(1)
    mc "Hmm... Something with U."
    mc "..."
    scene black with Dissolve(1)
    pause 2
    scene 08_288 with Dissolve(1)
    mc "I have no idea."
    la "What? No dinosaur with a U?"
    mc "Actually..."
    mc "No, I don't know."
    if Gabi_End == False:
        scene 08_238 with Dissolve(1)
        tr "Urchin!"
        mc "Oh yeah. Urchin, there you go."
        scene 08_288a with Dissolve(1)
        mc "Thank you, Ms Ramirez!"
        la "No, that one doesn't count."
        mc "..."
        scene 08_289 with Dissolve(1)
        la "If you don't know any, you're out."
        mc "I'm out, I guess."
    else:
        scene 08_289 with Dissolve(1)
        la "If you don't know any, you're out."
        mc "I'm out, I guess."
    scene 08_290 with Dissolve(1)
    la "Yay, we won! 1-0!"
    mc "What do you mean you won? There are still three players."
    el "It was boys versus girls."
    mc "Heh? Since when?"
    la "It's always been that way."
    mc "That's fair..."
    la "Next topic."
    scene 08_291 with Dissolve(1)
    mc "Hell no! Not playing three against one again..."
    el "Ask Zach to join, then. Not that it will change the outcome."
    mc "{i}(He might be able to help when we pick movies as a topic.){/i}"
    scene 08_292 with Dissolve(1)
    mc "Zach, I need you!"
    z "*Snoring*"
    mg "He's busy... Getting his makeup done."
    mc "Is he sleeping?"
    z "*Snoring*"
    mg "As you can hear."
    mc "{i}(He was right about the weird noises he talked about earlier. Why is he snoring like that?){/i}"
    mc "{i}(He better not snore in our room.){/i}"
    scene black with Dissolve(1)
    pause 2
    scene 08_293 with Dissolve(1)
    mg "Haha, let's see how long he walks around like that for."
    mg "Quick, take a picture."
    la "Why do guys always draw penises on each other?"
    mg "Because it's funny..."
    if Alexis_Week1_Concert == True: 
        scene black with Dissolve(1)
        pause 2
        scene 08_294 with Dissolve(1)
        va "*Sings* You needed a shoulder, I gave you my own..."
        mc "{i}(Is she singing? It's cute. She should create a band with Lexi.){/i}"
        va "*Sings* But now that I'm gone, you're feeling alone..."
        scene 08_295 with Dissolve(1)
        mc "{i}(What is she listening to, anyway?){/i}"
        mc "{i}(Oh... I know this one.){/i}"
        scene 08_296 with vpunch
        mc "*Sings* I won't be there to catch you, when you fall..."
        va "Uh? Was I singing out loud?"
        mc "More like humming, but yeah."
        va "{i}(So embarrassing...){/i}"
        scene 08_297 with Dissolve(1)
        va "You know this song?"
        mc "Yeah. When You Fall, by Yellow Snow."
        scene 08_298 with Dissolve(1)
        mc "I saw them like a week ago in Palm City."
        va "Really? I was there too."
        mc "Heh, what a coincidence."
        va "Did you like the concert?"
        mc "The music was good, yes. Don't like the guitarist though."
        va "Matt or Cruz?"
        mc "{i}(Why does everyone know their names? Are they that famous?){/i}"
        mc "Matt."
        if Alexis_Week1_Sunday_Concert_Sing == True:
            scene 08_299 with Dissolve(1)
            va "You must have seen the girl they asked to sing Embers and The Queen in Black, then?"
            mc "I did."
            va "She was so amazing. Even better than the original."
            if Alexis_Friends == False:
                mc "{i}(That's my Lexi!){/i}"
                va "I wish I recorded it, so I can listen to it again. It was so beautiful."
                mc "{i}(I have it, but I don't know if it's a good idea to show her.){/i}"
            else:
                va "I wish I recorded it, so I can listen to it again. It was so beautiful."  
            scene 08_300 with Dissolve(1)
            va "She actually lives in Madison Springs, so maybe I'll meet her someday."
            mc "{i}(Those chances are higher than you think.){/i}"
            va "Hmm, what was her name again?"
            mc "Alexis."
            scene 08_301 with Dissolve(1)
            va "Yes. Alexis! She must have left quite the impression on you too, that you remember her name."
            if Alexis_Friends == False:
                mc "She did. I'm her number one fan. But I also know her."
            else:
                mc "She did. But I also know her."
            va "Haha. Yes..."
            mc "I really do, actually."
            va "You're not fooling me today, Brave Sir [mc]!"
            mc "{i}(Shit, that name's gonna stick.){/i}"
            scene 08_302 with Dissolve(1)
            mc "She's Layla's sister."
            va "Okay, now I know you're just joking."
            mc "I'm serious."
            if Alexis_Friends == False:
                mc "{i}(I could show her the picture of us, but I need to talk to Layla first.){/i}"
            else:
                pass
            mc "Layla?"
            scene 08_303 with Dissolve(1)
            la "Yes?"
            mc "You have a sister, right?"
            la "Uhm... You know I do, you've met her!"
            mc "What was her name again?"
            la "..."
            la "Alexis."
            scene 08_304 with Dissolve(1)
            va "That can be pure coincidence."
            mc "Do you have a picture of her?"
            la "I do."
            mc "Please show it to Valeria."
            va "Wait... She really is her sister?"
            mc "You'll see for yourself."
            scene 08_305 with Dissolve(1)
            la "Here's one."
            la "Take a look."
            scene 08_306 with Dissolve(1)
            va "It is her!"
            mc "Told you."
            la "You know my sister?"
            va "No, not really. Just saw her once."
            la "Ah, okay."
            scene 08_307 with Dissolve(1)
            va "She's so pretty. You both are so pretty!"
            va "And wearing those dresses. I'm so jealous!"
            la "Thank you."
            scene 08_308 with Dissolve(1)
            la "Do you have siblings, Valeria?"
            va "Sadly, I don't."
            va "How about you, [mc]?"
            scene 08_309 with Dissolve(1)
            mc "An only child, just like you."
            mc "Well, I almost had two sisters."
            va "Almost?"
            mc "Yeah, but that's a story for another time."
        else:
            pass
    else:
        scene black with Dissolve(2)
        pause 2
        scene 08_294 with Dissolve(1)
        va "*Sings* You needed a shoulder, I gave you my own..."
        mc "{i}(Is she singing? It's cute.){/i}"
        va "*Sings* But now that I'm gone, you're feeling alone..."
        scene 08_295 with Dissolve(1)
        mc "{i}(What is she listening too, anyway?){/i}"
        mc "{i}(Hmm... Never heard of them. Sounds good though.){/i}"
        scene 08_296 with vpunch
        va "Aaah..."
        mc "Sorry, I didn't want to scare you."
        va "Uh? Was I singing out loud?"
        mc "More like humming, but yeah."
        va "{i}(So embarrassing...){/i}"
    scene 08_297 with Dissolve(1)
    mc "What other music do you like?"
    va "Want to listen to my playlist?"
    mc "Can I? Sure."
    scene black with Dissolve(1)
    pause 2
    scene 08_310 with Dissolve(1)
    mc "Oh... This is The No Tomorrows. They're great."
    mc "We have the same taste in music."
    scene black with Dissolve(2)
    pause 2
    scene 08_311 with Dissolve(1)
    tr "Everyone, we've arrived. You can step off the bus, and don't forget to grab your bags."
    tr "If you have any trash, please take it with you and throw it in a bin outside."
    scene black with Dissolve(1)
    pause 2
    scene 08_312 with Dissolve(1)
    la "Look who just stepped off that bus. What's she doing here?"
    mc "Who are you talking about."
    la "That girl back there."
    scene 08_313 with Dissolve(1)
    mc "Who is she?"
    la "That's Sha'Carri. She won the 100m and 200m sprints last year."
    scene 08_314 with Dissolve(1)
    la "I thought she would be in college. No idea why she's here."
    menu:
        "Joke":
            scene 08_314a with Dissolve(1)
            mc "Well, maybe they rejected her application because her Spanish is terrible."
            la "Very funny!"
            mc "Haha."
        "Don't":
            mc "Well, maybe they rejected her application and she's doing another year in the academy."
            la "Possible."
    scene 08_315 with Dissolve(1)
    mc "So, she's fast, I assume?"
    la "Yeah, she is. She had no competition at all."
    la "Maybe she's even faster now..."
    scene 08_316 with Dissolve(1)
    to "Ugh... What's she doing here?"
    la "We had the same question."
    scene 08_317 with Dissolve(1)
    la "There go our chances of winning."
    to "Speak for yourself. I'm beating her this time."
    scene 08_318 with Dissolve(1)
    z "Hey Val, let me take your bag for you."
    va "Thanks, it's fine."
    z "No really, I insist!"
    scene 08_319 with Dissolve(1)
    to "Darryl, can you get my bag for me?"
    da "Bitch, you have two hands. Get it yourself..."
    to "..."
    scene black with Dissolve(1)
    pause 2
    scene 08_320 with Dissolve(1)
    z "I spoke to Valeria just now. All is good again."
    mc "Nice to hear."
    mc "{i}(She didn't tell him about the penis?){/i}"
    mg "So mission 'pop the cherry' is a go?"
    mc "..."
    z "You know it."
    mc "{i}(What have they been talking about the whole ride...){/i}"
    scene 08_321 with Dissolve(1)
    mg "How's your sandwich?"
    z "Pretty good."
    mg "You got something here."
    z "Oh, thanks."
    scene 08_322 with Dissolve(1)
    mg "Haha..."
    z "Is it gone?"
    mg "No."
    scene 08_323 with Dissolve(1)
    mg "Keep going. Haha..."
    z "Why are you laughing? It's not that funny."
    mg "Trust me, it is!"
    z "Whatever man."
    scene 08_324 with Dissolve(1)
    tr "Can one person from each group come to get the keys for their room."
    tr "We have two keys per room. So you'll have to share."
    z "I'll get them."
    scene black with Dissolve(1)
    pause 2
    scene 08_325 with Dissolve(1)
    tr "Next. Name, and who's in your group?"
    z "Zach Gallagher. BDC."
    tr "BDC?"
    z "Big..."
    tr "*Sigh* Okay, okay..."
    scene 08_326 with Dissolve(1)
    tr "Here are your... keys. You'll be in room twelve."
    z "Thank you."
    tr "Can you please sign here to validate that you've received the keys."
    z "Anything for you."
    tr "..."
    scene 08_327 with Dissolve(1)
    tr "Uhm, Zach..."
    tr "You've got something on your face."
    z "What? I thought they were kidding."
    scene 08_328 with Dissolve(1)
    z "Maybe if I rub it harder..."
    tr "{i}(Why am I laughing at that. This is ridiculous.){/i}"
    z "{i}(Why is she laughing?){/i}"
    scene 08_329 with Dissolve(1)
    z "WHAT THE FUCK! WHO DID THIS?"
    tr "Language, Zach!"
    z "MIGUEL!"
    scene black with Dissolve(1)
    pause 2
    scene 08_330 with Dissolve(1)
    z "What is this? This room is tiny. Oh man..."
    z "[mc], mind if I take the top bed?"
    mc "Sure, go ahead."
    scene 08_331 with Dissolve(1)
    z "You'd better keep an eye open at night, Miguel!"
    mg "Haha. Don't worry, I'll have both my eyes open because I plan to be in Elena's bed instead of here."
    mc "..."
    mc "{i}(Please don't be another Zach... One is enough!){/i}"
    scene 08_332 with Dissolve(1)
    z "Well, then we'll be staying in the same room anyway, since I'm sleeping with Valeria!"
    mc "She's with Tori's group."
    z "Oh yeah, I forgot. For a second I thought she was with Layla's group."
    z "Damn... I don't want to be in the same room as Tori."
    scene 08_333 with Dissolve(1)
    z "Seems like she'll be sharing this bed right here then."
    z "You still fine with the bottom bed? I mean, it can get rocky."
    mc "Uh-huh..."
    scene 08_334 with Dissolve(1)
    z "Oh here. We only got two keys for the room."
    z "You take one, we'll share the other since we're on the same team anyway."
    mc "Thanks."
    jump Week3_Wednesday_Training

label Week3_Wednesday_Training:
    scene black with Dissolve(1)
    pause 2
    stop music fadeout 1.0
    play music ("Music/Indie-Electro 1.mp3", "Music/Indie-Electro 2.mp3", "Music/Indie-Electro 3.mp3", "Music/Indie-Electro 4.mp3") volume 0.2
    scene 08_335 with Dissolve(1)
    mc "{i}(Val is already here.){/i}"
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 08_335a at moveup
    pause 3
    ""
    scene 08_336 with Dissolve(1)
    mc "Hey, Val."
    va "Hi. First ones here, huh?"
    mc "Yeah, we're early. Well, we're at the correct place, right?"
    scene 08_337 with Dissolve(1)
    va "Now that you mention it, and we are the only ones here, I'm not that sure anymore."
    mc "Haha."
    mc "We'll know if no one shows up in the next five minutes."
    scene 08_338 with Dissolve(1)
    mc "How's your room?"
    va "It's fine."
    mc "What bed did you choose? Top or bottom. Or maybe you didn't have a choice due to Tori?"
    va "What do you mean? I just took a free bed."
    mc "You don't have bunk beds?"
    va "No, four singles."
    mc "Oh..."
    scene 08_339 with Dissolve(1)
    mc "We have a small room with two bunk beds, that's it. Not even a table or a chair."
    va "Which bed did you take?"
    mc "Bottom. Zach wanted to be on top."
    scene 08_340 with Dissolve(1)
    mc "..."
    mc "Okay, that sounded weird for a second."
    va "Haha. You made it weird..."
    scene 08_341 with Dissolve(1)
    mc "Did you at least get a key?"
    va "No. We only got two. Tori took one and gave the other to Jasmine because she's on a different team."
    va "So if I can't get into my room I might take up your offer and hang out in yours in the meantime."
    mc "Anytime."
    va "Thanks."
    scene 08_342 with Dissolve(1)
    va "Anyway. Since you're the only one here. Can you help me stretch a bit?"
    mc "Sure, no problem."
    scene black with Dissolve(1)
    pause 2
    scene 08_343 with Dissolve(1)
    mc "Tell me if I'm pushing too hard."
    va "You're good."
    mc "I wish I was this flexible."
    va "You're not that far off. Just stretch every day and you'll be here in no time."
    scene 08_344 with Dissolve(1)
    mc "{i}(Zach would do anything to be in my shoes now.){/i}"
    scene 08_345 with Dissolve(1)
    mc "{i}(But I don't mind at all... Is she getting prettier every time I see her, or am I just imagining things?){/i}"
    mc "{i}(It might be the 'if you get to know a person, she either gets prettier or less attractive' phenomenon.){/i}"
    mc "{i}(Does she like Zach? She said he's her first friend since moving back here, but could there be more?){/i}"
    scene 08_346 with Dissolve(1)
    mc "{i}(Zach would've told me, right?){/i}"
    if Alexis_Friends == False:
        mc "{i}(Why does it matter anyway? I'm dating Alexis...){/i}"
        mc "..."
    else:
        mc "..."
    mc "{i}(But I still want to know, for some reason.){/i}"
    scene 08_347 with Dissolve(1)
    va "Earth to [mc]. Still here?"
    mc "Uh... Sorry."
    va "Daydreaming?"
    menu:
        "Daydreaming[KoGa3AutoWTChange1]{size=-4}({i}Valeria Points6: Valeria Points+2{/i}) {/size} {/color}":
            scene 08_348 with Dissolve(1)
            mc "Uh yeah, was just thinking about something."
            va "Something specific?"
            if Valeria_Points == 6:
                $ Valeria_Points += 2
                # Valeria (8)
                scene 08_349 with Dissolve(1)
                mc "Maybe, maybe not."
                va "So vague..."
            else:
                mc "No, random things."
        "Nose ring[KoGa3AutoWTChange1]{size=-4}(Valeria Points+2) {/size} {/color}":
            $ Valeria_Points += 2
            # Valeria (8)
            scene 08_348 with Dissolve(1)
            mc "Uh... I was looking at your nose ring. Are you allowed to wear that at competitions?"
            va "At the pole vault competition, no... I had to take it off."
            va "Sprinting, I'm not sure actually. I'll have to ask Coach later. I don't see the problem with keeping it in though."
            scene 08_349 with Dissolve(1)
            va "What do you think about it?"
            mc "Yeah, I think it shouldn't be a problem keeping it in."
            va "Haha no, I meant does it suit me."
            menu:
                "No":
                    mc "It's not my thing."
                    va "Haha, I appreciate your honesty."
                "Yes":
                    mc "Yeah, it looks good on you. I like it."
                    va "Thanks."
        "Pretty[KoGa3AutoWTChange1]{size=-4}(Valeria Points-2) {/size} {/color}":
            scene 08_348 with Dissolve(1)
            $ Valeria_Points -= 2
            mc "Looking at you. You're very pretty!"
            va "Uh, thank you..."
    scene 08_350 with Dissolve(1)
    va "Can you lean in and stretch my leg all the way down?"
    mc "Putting my weight on it?"
    va "Uh-huh."
    scene 08_351 with Dissolve(1)
    mc "Tell me if I'm hurting you, okay?"
    va "It's fine."
    scene 08_352 with Dissolve(1)
    va "Push a bit more."
    mc "{i}(In some way, lots of stretching positions could also be sex positions.){/i}"
    va "Yeah, keep it there."
    mc "..."
    mc "{i}(And now I'm getting turned on.){/i}"
    scene 08_353 with Dissolve(1)
    va "Keep it right there."
    if Layla_Points >= 43:
        scene 08_354 with Dissolve(1)
        la "..."
        la "{i}(What are they doing?){/i}"
    else:
        $ Layla_Friends = True
    scene 08_355 with Dissolve(1)
    la "Hey. You guys are early!"
    mc "Hey, Layla."
    va "Hi."
    scene 08_356 with Dissolve(1)
    mc "Yeah, we thought we were on the wrong track at first."
    mc "But since more people are coming, this must be it."
    scene 08_357 with Dissolve(1)
    la "Warming up already?"
    va "Just some stretching. Since [mc] was the first one here, I asked him if he could help me."
    la "How long have you been here?"
    va "Not that long. Five minutes or so?"
    scene 08_358 with Dissolve(1)
    to "Why don't you ever wait?"
    da "Because you take ages to get ready..."
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 08_358a at moveup
    pause 3
    mc "{i}(I bet lots of guys would wait for her though.){/i}"
    mc "{i}(She isn't bad to look at. If only her personality and choices were... Different.){/i}"
    scene 08_359 with Dissolve(1)
    la "Here we go. Argument number one of training camp."
    mc "No-no-no, it's at least number two."
    scene 08_360 with Dissolve(1)
    mc "This could be a good drinking game. Every time they argue, we drink."
    la "Haha. We'll be drunk in no time."
    scene 08_361 with Dissolve(1)
    to "Valeria!"
    va "What's up?"
    to "Follow me! Official room business."
    va "..."
    scene 08_362 with Dissolve(1)
    mc "Oh, official room business. Maybe you'll get a key."
    va "Would be nice, but I don't think so."
    va "See you later. Thanks for helping me stretch."
    mc "You're welcome."
    scene 08_363 with Dissolve(1)
    mc "Want to do some stretches too?"
    la "Didn't you stretch already?"
    mc "No, I only helped Val stretch."
    scene 08_364 with Dissolve(1)
    mc "Come on."
    la "Thanks."
    if Layla_Friends == True:
        scene 08_365a with Dissolve(1)
        mc "..."
        scene 08_366a with Dissolve(1)
        la "You like her."
        mc "Who? Tori?"
        la "No, Valeria."
        scene 08_367a with Dissolve(1)
        mc "We've just got to know each other a little. She seems fun. We're friends, that's about it."
        mc "Besides. Zach likes her."
        la "..."
        la "But maybe she doesn't like Zach."
        if Valeria_Points == 8:
            scene 08_368a with Dissolve(1)
            la "Want me to do some digging and find out?"
            mc "Haha, no thanks."
            la "Hmm... Okay."
        else:
            pass
    else:
        if Layla_Points >= 43:
            scene 08_365 with Dissolve(1)
            la "..."
            scene 08_366 with Dissolve(1)
            mc "Hey! What's wrong?"
            la "Nothing."
            mc "Layla..."
            la "Do you like her?"
            mc "Who?"
            la "Valeria."
            scene 08_367 with Dissolve(1)
            mc "We've just got to know each other a little. She seems fun. We're friends, that's about it. Don't worry about it."
            scene 08_368 with Dissolve(1)
            mc "What? Not a good enough answer?"
            la "She's beautiful and cute."
            mc "So are you!"
            la "She has an amazing body. Big chichis too..."
            mc "Again, so do you!"
            la "..."
            la "You've known her for a day or so, and you were already lying on top of her."
            mc "Oh... There we go. It's about that. I was just helping her stretch, Layla."
            scene 08_369 with Dissolve(1)
            la "I know that. Still, it looked very... *Mumbles*"
            mc "What?"
            la "Nothing..."
            mc "You sound a bit jealous."
            scene 08_370 with Dissolve(1)
            la "Of course I'm jealous!"
            mc "{i}(Trying to look angry. It's not working, Layla. You look pretty cute.){/i}"
            la "I wish I was lying there."
            menu:
                "Do nothing":
                    scene 08_371 with Dissolve(1)
                    mc "Haha, you're funny."
                    la "For the remainder of training camp, I'll be your stretch partner!"
                    mc "Heh, okay. Are there any benefits to being your stretch partner?"
                    la "Yes! But it's for you to find out what they are."
                    scene 08_372 with Dissolve(1)
                    mc "Then I'm in."
                    la "You had no choice, anyway."
                    scene 08_373 with vpunch
                    n "*SLAP*"
                    la "Aaah... Not again!"
                    scene 08_374 with Dissolve(1)
                    tm "Technically we aren't in school, but keep the PDA to a minimum, or at least after the training."
                    mc "{i}(Oh shit!){/i}"
                    scene 08_380 with Dissolve(1)
                    mc "Heh, hey, Coach. That was just a well-done slap. Like a high five, you know?"
                    tm "A high five? Come on over here then. I'll high five you too."
                    mc "I'm good, I'm good. No need, Coach!"
                    la "Haha."
                "Push her down[KoGa3AutoWTChange1]{size=-4}(Layla Week3 Wednesday TC Kiss, Layla Points+2) {/size} {/color}":
                    $ Layla_Week3_Wednesday_TC_Kiss = True
                    $ Layla_Points += 2
                    # Layla (62)
                    scene 08_375 with vpunch
                    la "Haha..."
                    mc "Now I'm lying on top of you. Happy now?"
                    la "Yes!"
                    scene 08_376 with Dissolve(1)
                    to "What are they doing..."
                    va "Playing around and having fun, I assume."
                    to "You call lying on the floor having fun?"
                    to "She should concentrate on training, instead."
                    scene 08_377 with Dissolve(1)
                    la "For the remainder of training camp, I'll be your stretch partner!"
                    mc "Heh, okay. Are there any benefits to being your stretch partner?"
                    la "Yes! Here's one."
                    scene 08_378 with Dissolve(1)
                    mc "{i}(She's getting more confident.){/i}"
                    mc "{i}(Or maybe it's because we aren't at school?){/i}"
                    tm "Technically we aren't in school, but keep the PDA to a minimum, or at least after the training."
                    scene 08_379 with Dissolve(1)
                    mc "{i}(Oh shit!){/i}"
                    scene 08_380 with Dissolve(1)
                    mc "Heh, hey, Coach. That was just a greeting. Like hey, how are you, you know?"
                    tm "A greeting? Come on over here then. I'll greet you, too."
                    mc "I'm good, I'm good. No need, Coach!"
                    la "Haha."
        else:
            $ Layla_Friends = True
    scene black with Dissolve(1)
    pause 2
    scene 08_381 with Dissolve(1)
    tm "Alright, everyone. Gather around."
    tm "I see you're all here already. How come this never happens at school?"
    scene 08_382 with Dissolve(1)
    tm "Let's start with some warm-up laps."
    tm "A little warning though..."
    tm "Today and tomorrow, I'll push you guys to your limits."
    scene 08_383 with Dissolve(1)
    to "Push me to my limits, huh? I like the sound of that."
    to "The first thing I'll do once I graduate is fuck Coach's brains out."
    va "What?"
    to "You heard me. I think he has a huge dick. Just look at that bulge in his pants."
    va "Uhm..."
    to "Mmm. Getting horny just thinking about it."
    scene 08_384 with Dissolve(1)
    to "Wouldn't you?"
    va "No..."
    to "Why not? He's good looking for his age. He probably has lots of experience, and he's a coach."
    to "Meaning he has lots of stamina."
    to "Screw graduation. I'll do him right here during training camp if I have the chance..."
    va "You're crazy."
    to "I've heard worse."
    scene 08_385 with Dissolve(1)
    to "Okay then. Which of the guys on this team would you fuck?"
    va "..."
    va "Uhm. I don't know."
    to "Oh come on. Don't worry, I won't tell your boyfriend."
    scene 08_386 with Dissolve(1)
    va "I don't have a boyfriend."
    to "Then why are you hanging around with that weirdo all the time?"
    va "You mean Zach?"
    to "I don't know his name."
    va "He's my friend."
    scene 08_387 with Dissolve(1)
    to "Forget about him."
    to "All the guys in the school would wait in line to have a go with you."
    to "So, take your pick."
    scene 08_388 with Dissolve(1)
    va "*Sigh* Maybe Darryl."
    to "Oh, Darryl... Interesting!"
    to "Who else?"
    scene 08_389 with Dissolve(1)
    if Valeria_Points == 8:
        va "No one."
        to "No one else? Well, I can give you a few names who know what they're doing."
    else:
        va "[mc]?"
        if Tori_Week1_Interested == True:
            to "Been there, done that."
            to "But good choices. The two guys with the biggest dicks."
        else:
            to "He's also on my list. Good choices."
    va "..."
    scene 08_390 with Dissolve(1)
    tm "Tori, Valeria!"
    tm "Are you paying attention?"
    to "You know I am, Mike."
    tm "..."
    tm "Let's get started then."
    scene 08_391 with Dissolve(1)
    to "Look at that. You're running with us for once."
    tm "I have to stay in shape too."
    to "Mmm-hmm. Will you be able to keep up with us?"
    tm "The question is, can you keep up with me?"
    to "Mr Morgan!"
    to "Let's find out together."
    scene 08_392 with Dissolve(1)
    la "..."
    la "If she keeps this up, we'll have another argument pretty soon."
    la "She flirts with him every day. Isn't he getting tired of it?"
    mc "Maybe he likes it? It's probably flattering."
    if Layla_Week3_Tuesday_Train == False:
        scene 08_393 with Dissolve(1)
        mc "By the way, I'm sorry about yesterday. Something came up and..."
        la "It's fine. No worries."
        mc "Did you do some running?"
        la "At first I wasn't going, but my dad joined and trained with me. It was really fun."
        mc "Oh cool."
    else:
        pass
    scene black with Dissolve(1)
    pause 2
    scene 08_394 with Dissolve(1)
    tm "Okay, everyone. We'll keep on running but we'll switch to an Indian relay."
    tm "I want you to create a single file line. The person in the front decides the pace. The person at the back sprints to the front."
    tm "We'll do this until everyone has sprinted ten times."
    scene 08_395 with Dissolve(1)
    tm "And since I know you guys, I'll join you once more so you don't drop the pace to a walk!"
    tm "Also, the person who keeps the front position for the longest will get some extra credit."
    scene black with Dissolve(1)
    pause 2
    scene 08_396 with Dissolve(1)
    tm "Good job, keep up the pace."
    scene 08_397 with Dissolve(1)
    mc "{i}(Oh... She's already caught up.){/i}"
    menu:
        "Let her pass":
            scene black with Dissolve(1)
            pause 2
            scene 08_402 with Dissolve(1)
            n "*Heavy breathing*"
            mc "{i}(Man... This isn't easy at all.){/i}"
            mc "Are you okay, Layla?"
            la "Yeah, just give me a minute..."
        "Start sprinting[KoGa3AutoWTChange1]{size=-4}(Layla Points-2, Valeria Points+2) {/size} {/color}":
            $ Layla_Points -= 2
            $ Valeria_Points += 2
            # Valeria (10)
            mc "{i}(I never saw her go all out.){/i}"
            mc "{i}(Let's see what she can do.){/i}"
            scene 08_398 with Dissolve(1)
            va "Hey! What are you doing?"
            va "..."
            scene 08_399 with Dissolve(1)
            la "Seriously?"
            tm "Yes! That's what I want to see. Don't make it easy for each other."
            tm "Come on, Layla. Let's keep up."
            la "*Sigh*"
            scene 08_400 with Dissolve(1)
            mc "Look at you. Didn't expect you to be able to keep up."
            va "Didn't expect you can be an asshole and not let me pass..."
            mc "Haha. Touché!"
            scene 08_401 with Dissolve(1)
            mc "It's not you. I just want that extra credit."
            va "Oh... Is that what this is?"
            mc "Of course!"
            va "Uh-huh."
            scene black with Dissolve(1)
            pause 2
            scene 08_402 with Dissolve(1)
            n "*Heavy breathing*"
            mc "{i}(Maybe that was a bit too much...){/i}"
            mc "Are you okay, Layla?"
            la "I'm feeling sick..."
            mc "I'm so sorry."
            la "You'd better be!"
            scene 08_403 with Dissolve(1)
            da "Thanks a lot! We could've been done in two, three laps. But noooo..."
            da "All this because you want to impress the new girl?"
            da "You do realise, we have four more hours of training?"
            scene 08_404 with Dissolve(1)
            mc "What's the issue? Just having a little fun."
            da "Having fun..."
            va "They don't like each other, huh?"
            la "No. Since the first day when [mc] beat Darryl at training, there's been tension between them."
            la "Maybe because both of them are competitive and want to win."
            scene 08_405 with Dissolve(1)
            va "By the way. I love your shorts. They're so cute."
            la "Yeah? Thanks."
            la "I got them at Delta Sport."
            scene 08_406 with Dissolve(1)
            va "Oh, where's that?"
            la "At the mall in the city."
            la "We can go there together sometime next week if you like?"
            va "Totally. Thank you."
    scene 08_407 with Dissolve(1)
    tm "That's what I call a warm-up!"
    tm "What's with the faces? Don't tell me you're tired already."
    tm "Come on. Partner up."
    if Layla_Points >= 45:
        $ Layla_Week3_Wednesday_TC_TrainingPartner = True
        scene 08_408 with Dissolve(1)
        la "I told you before, you're gonna be my training partner for this trip."
        mc "I'm fine with that."
        la "Good!"
        scene 08_409 with Dissolve(1)
        la "Sorry, Val. I..."
        va "No, no. Don't worry about it. I'll find someone."
    else:
        scene 08_410 with Dissolve(1)
        la "Val, want to partner up with me?"
        va "Yes."
        la "Great!"
        mc "{i}(Guess I'll look for someone, too... Would've loved to partner up with one of them, though.){/i}"
    scene 08_411 with Dissolve(1)
    da "Come on, babe."
    to "Now you babe me? Earlier, when I asked you to wait you called me another name with a B..."
    to "So... Fuck off!"
    scene 08_412 with Dissolve(1)
    da "Bitch..."
    to "Oh, look at that. You can actually remember something."
    da "..."
    if Layla_Week3_Wednesday_TC_TrainingPartner == True:
        scene 08_413 with Dissolve(1)
        to "Val, you're with me!"
        va "Uh, okay."
        jump Week3_Wednesday_Training_Layla
    else:
        scene 08_414 with Dissolve(1)
        to "You're with me!"
        mc "Uh, okay?"
        jump Week3_Wednesday_Training_Tori

label Week3_Wednesday_Training_Layla:
    scene black with Dissolve(1)
    pause 2
    scene 08_415 with Dissolve(1)
    la "Seven."
    scene 08_416 with Dissolve(1)
    mc "Having fun?"
    la "Eight. I am. I wish school was like this every day."
    mc "Yeah, this beats sitting in a classroom by a large margin."
    scene black with Dissolve(1)
    pause 2
    scene 08_417 with Dissolve(1)
    la "This is a bit..."
    mc "Haha. Regretting picking me as your training partner?"
    la "No... Just..."
    scene 08_418 with Dissolve(1)
    mc "Oh, and remember, we have to switch positions after this."
    la "What?"
    mc "Haha."
    scene 08_419 with Dissolve(1)
    mc "{i}(But she's right. This is very hot...){/i}"
    la "Where are you looking?"
    scene black with Dissolve(1)
    pause 2
    scene 08_420 with Dissolve(1)
    mc "What are you doing?"
    la "Not looking!"
    mc "Haha. I'm wearing clothes. You won't see anything."
    la "No... I'm not risking it."
    mc "{i}(She's so cute when she's embarrassed.){/i}"
    tm "Sit-ups next!"
    la "Finally..."
    scene black with Dissolve(1)
    pause 2
    scene 08_421 with Dissolve(1)
    mc "Oh, you want me to start?"
    la "Yeah. Show me what you've got."
    scene 08_421a with Dissolve(1)
    la "Twelve..."
    la "Thirteen..."
    if Layla_Week3_Wednesday_TC_Kiss == True:
        scene 08_422 with Dissolve(1)
        mc "And... Twenty!"
        la "That's it? Come on, I expect at least a hundred more!"
        mc "You're my training partner. Encourage me then!"
        la "Well, okay. For every five sit-ups, you'll get a benefit."
        mc "Ah, the benefits... Let's see what they are!"
        scene black with Dissolve(1)
        pause 2
        scene 08_423 with Dissolve(1)
        la "Four!"
        mc "{i}(Why am I getting nervous?){/i}"
        scene 08_424 with Dissolve(1)
        mc "..."
        scene 08_425 with Dissolve(1)
        mc "I'm starting to like those benefits."
        la "Haha."
        mc "Any more of this?"
        la "Who knows..."
        scene black with Dissolve(1)
        pause 2
        scene 08_426 with Dissolve(1)
        mc "Your turn."
        la "Do I have to? I hate doing sit-ups."
        mc "They aren't that bad."
        mc "Especially the ones I just did."
        la "..."
        scene 08_427 with Dissolve(1)
        mc "You're doing good, keep going."
        scene 08_428 with Dissolve(1)
        la "{i}(Five...){/i}"
        scene 08_428a with Dissolve(1)
        la "..."
        scene 08_429 with Dissolve(1)
        la "Hey! Where's my kiss?"
        mc "What do you mean? I'm the one who gets benefits. There was no talk about you getting any..."
        la "That's not fair."
        mc "You failed to specify certain conditions."
        la "..."
        scene 08_430 with Dissolve(1)
        mc "This is all you're getting."
        la "Thank you."
        mc "Now do your push-ups."
        la "Sit-ups!"
        mc "Yeah, that's what I mean."
    else:
        scene 08_422 with Dissolve(1)
        mc "And... Twenty!"
        la "That's it? Come on, I expect at least a hundred more!"
        mc "Twenty is enough for now."
        scene 08_426 with Dissolve(1)
        mc "Your turn."
        la "Do I have to? I hate doing sit-ups."
        mc "They aren't that bad."
        scene 08_427 with Dissolve(1)
        mc "You're doing good, keep going."
    jump Week3_Wednesday_Training_End

label Week3_Wednesday_Training_Tori:
    if _in_replay:
        $ Tori_Points = 2
        $ Tori_Week1_Interested = True
    scene 08_431 with Dissolve(1)
    mc "You sure you got the right person? Darryl is right there."
    to "Who?"
    mc "..."
    scene black with Dissolve(1)
    pause 2
    scene 08_432 with Dissolve(1)
    mc "How is this? Higher, lower?"
    to "Hmm... Depends. How does my butt look in this position?"
    scene 08_433 with Dissolve(1)
    mc "..."
    to "Tell me!"
    to "Need a closer look, maybe?"
    scene 08_434 with Dissolve(1)
    mc "{i}(Honestly, she has a nice ass...){/i}"
    scene black with Dissolve(1)
    pause 2
    scene 08_435 with Dissolve(1)
    if Tori_Week1_Interested == True:
        to "I wouldn't mind fucking you again, to be honest."
        mc "Do you need someone you can ignore again?"
        scene 08_436 with Dissolve(1)
        mc "Aaah... Hey, chill a bit."
        to "Rather than chill, let's fuck!"
        mc "..."
    else:
        to "Why haven't we fucked yet?"
        mc "Heh. Because I told you I'm not interested."
        scene 08_436 with Dissolve(1)
        mc "Aaah... Hey, chill a bit."
        to "You deserved that."
    scene black with Dissolve(1)
    pause 2
    scene 08_437 with Dissolve(1)
    da "For fuck's sake! With him? Is she trying to make me jealous? I'll get you back for that, Tori..."
    tj "Why are you still with her? You know what she's like."
    da "Shut up!"
    scene 08_438 with Dissolve(1)
    to "See, Mike wants us to fuck too. He even shows us sex positions..."
    to "If that isn't a sign."
    to "Want to test it out after? Or maybe right now?"
    scene 08_439 with Dissolve(1)
    to "..."
    to "{i}(Stop ignoring me!){/i}"
    scene 08_440 with Dissolve(1)
    mc "{i}(She's right though. It does look very hot.){/i}"
    to "Why are you looking at them? You have a gorgeous girl spreading her legs right in front of you. Literally!"
    mc "What?"
    to "..."
    to "{i}(Let's see how you like this.){/i}"
    show 08_441
    mc "..."
    scene 08_441 with Dissolve(1)
    mc "Hey!"
    mc "{i}(What is she doing? That was close... She's very flexible though.){/i}"
    scene 08_442 with Dissolve(1)
    mc "Sorry?"
    to "Don't apologise. Enjoy it!"
    scene 08_443 with vpunch
    to "Caught you. Now you're mine!"
    mc "Let go, Tori."
    mc "{i}(This girl is crazy...){/i}"
    scene 08_444 with Dissolve(1)
    to "If you want me to let go, you need to pay the price."
    mc "And what's that?"
    to "I think you can figure it out."
    mc "{i}(Does she do MMA after school? This is a serious headlock.){/i}"
    scene 08_445 with Dissolve(1)
    mc "{i}(What should I do?){/i}"
    menu:
        "Kiss[KoGa3AutoWTChange1]{size=-4}(Tori Week3 Wednesday TC Fun, Tori Points+2) {/size} {/color}":
            $ Tori_Week3_Wednesday_TC_Fun = True
            $ Tori_Points += 2
            # Tori (4)
            scene 08_449 with Dissolve(1)
            mc "{i}(She's wet... Could be sweat though.){/i}"
            to "Oh... I didn't think you had it in you. You're more fun than I'd expected."
            to "Payment accepted."
            scene 08_451 with Dissolve(1)
            tj "What are they doing?"
            da "Haha, she's choking him out. Just what he deserves..."
            scene 08_453 with Dissolve(1)
            to "That was fun!"
            if Tori_Week1_Interested == False:
                to "Maybe your friend down here will get to play, too."
            else:
                to "You just might change my mind about my rule."
        "Lick[KoGa3AutoWTChange1]{size=-4}(Tori Week3 Wednesday TC Fun, Tori Points+4) {/size} {/color}":
            $ Tori_Week3_Wednesday_TC_Fun = True
            $ Tori_Points += 4
            # Tori (6)
            scene 08_446 with Dissolve(1)
            mc "{i}(She's wet... Could be sweat though.){/i}"
            mc "{i}(She's actually managed to turn me on. I hope no one sees this.){/i}"
            scene 08_447 with Dissolve(1)
            to "Ah..."
            to "Payment accepted!"
            scene 08_451 with Dissolve(1)
            tj "What are they doing?"
            da "Haha, she's choking him out. Just what he deserves..."
            scene 08_453 with Dissolve(1)
            to "That was fun!"
            if Tori_Week1_Interested == False:
                to "Maybe your friend down here will get to play, too."
            else:
                to "You just might change my mind about my rule."
        "Push her away":
            scene 08_450 with vpunch
            to "Aaah... That hurt! I was just playing around."
            mc "I'm not."
            to "I thought you were fun..."
            scene 08_452 with Dissolve(1)
            to "You need to chill sometimes and have some fun."
            if Tori_Week1_Interested == False:
                mc "I can have fun, I just don't want to be another name on your list!"
            else:
                mc "I'm on your list already, once is enough!"
            to "Whatever..."
    $ renpy.end_replay()
    jump Week3_Wednesday_Training_End

label Week3_Wednesday_Training_End:
    scene black with Dissolve(1)
    pause 2
    scene 08_454 with Dissolve(1)
    tm "Let's do a little bit of sprinting before you start with your individual training."
    tm "We'll start with the boys today."
    da "It's about time."
    scene 08_455 with Dissolve(1)
    da "Ready to get your ass whooped again?"
    mc "What's your problem, Darryl? Still butthurt I beat you on my first run?"
    da "That was a fluke, you didn't even come close to beating me after that."
    mc "Because every time you're about to lose, you fake an injury..."
    tm "Are you ready, guys?"
    scene 08_456 with Dissolve(1)
    la "Ready!"
    la "Set!"
    scene 08_457 with Dissolve(1)
    la "GO!"
    scene 08_458 with Dissolve(1)
    mc "..."
    scene 08_459 with Dissolve(1)
    mc "{i}(What's he doing? Why is he so close?){/i}"
    scene 08_460 with vpunch
    mc "Shit!"
    scene 08_461 with vpunch
    da "What the fuck was that?"
    da "Stay in yo lane!"
    menu:
        "Walk away":
            scene 08_462 with Dissolve(1)
            mc "If you say so."
            da "Yeah, just walk away, pussy!"
            da "If this happens at the competition, I'll kick your ass!"
        "Confront him[KoGa3AutoWTChange1]{size=-4}(Darryl Points+2) {/size} {/color}":
            $ Darryl_Points += 2
            # Darryl (2)
            scene 08_463 with vpunch
            mc "Get off me, man!"
            mc "How about you stay in yours!"
            scene 08_465 with Dissolve(1)
            va "Are they going to fight?"
            to "That could be interesting."
            to "Let's do this, boys. Winner gets me!"
            la "Really, Tori?"
            scene 08_464 with Dissolve(1)
            da "You wanna go?"
            mc "Try me!"
            da "Come on! Show me what you've got."
            scene 08_466 with Dissolve(1)
            tm "HEY, HEY, HEY!"
            tm "I like the energy, but keep it for Saturday!"
            tm "We are a team here. If someone gets an ass-kicking, it's the other schools."
            tm "Both of you, take a break and cool off!"
            tm "Girls, you're up!"
    scene black with Dissolve(1)
    pause 2
    scene 08_467 with Dissolve(1)
    mc "Damn... And this was only the first day."
    la "Half a day. Tomorrow will be worse."
    mc "Yeah, I think so, too."
    scene 08_468 with Dissolve(1)
    mc "What are your plans for the rest of the day?"
    la "I'm exhausted. Probably just going to shower, eat something and lie down a bit."
    if Alexis_Sex == False:
        mc "Doesn't sound bad at all. I might just do the same."
    else:
        if Layla_Week2_Wednesday_Knows == True:
            mc "Doesn't sound bad at all. I might just do the same."
        else:
            $ Layla_Week3_Wednesday_TC_AlexisTalk = True
            mc "Doesn't sound bad at all. I might just do the same."
            mc "{i}(I probably should talk to her about Alexis. I can't drag it out for much longer.){/i}"
            scene 08_469 with Dissolve(1)
            mc "Will you have time after your nap? I need to talk to you."
            la "Uh, yeah, sure. What about?"
            mc "I'll tell you then."
            la "You're making me nervous now."
            mc "Haha. It isn't bad."
            mc "{i}(I think...){/i}"
            scene 08_470 with Dissolve(1)
            la "Where do you want to meet?"
            mc "Pick me up in my room once you're ready? We can go from there."
            la "What's your room number?"
            mc "Twelve."
    if Layla_Week3_Wednesday_TC_Kiss == True:
        scene 08_471 with Dissolve(1)
        mc "Come on, let's go back and take a shower."
        la "We're not showering together!"
        mc "What, why not? We're friends. Friends shower together. You and Elena must have showered together already."
        la "..."
        scene 08_472 with Dissolve(1)
        mc "What?"
        la "That's different."
        mc "How is that different? You're so sexist."
        la "Nothing to do with sexism."
        mc "Oh... It's like that. I'm just a B-list friend and you shower only with A-listers, huh?"
        mc "Good to know."
        scene 08_473 with Dissolve(1)
        la "I wouldn't kiss a B-lister!"
        va "Haha. That happened?"
    else:
        scene 08_474 with Dissolve(1)
        mc "Come on, let's go back."
        va "Haha. That happened?"
    scene 08_475 with Dissolve(1)
    mc "Hmm... What are they talking about?"
    la "Who? Valeria and Darryl?"
    scene 08_476 with Dissolve(1)
    mc "Yeah, since when is he funny?"
    la "I don't know. I actually can't remember the last time I talked with him."
    la "Maybe two years ago or so."
    mc "Really? I wish he would stop talking to me for at least two years..."
    scene 08_477 with Dissolve(1)
    la "Well, you don't talk, you mostly fight."
    la "I should start calling you Tori! Haha..."
    mc "You think you're so funny, don't you?"
    la "Uh-huh."
    if Valeria_Points == 10:
        scene 08_478a with Dissolve(1)
        va "..."
    else:
        scene 08_478 with Dissolve(1)
        va "..."
    jump Week3_Wednesday_Alexis_Call

label Week3_Wednesday_Alexis_Call:
    scene black with Dissolve(1)
    pause 2
    stop music fadeout 1.0
    play music ("Music/LoFi Upbeat 1.mp3", "Music/LoFi Upbeat 2.mp3", "Music/LoFi Upbeat 3.mp3", "Music/LoFi Upbeat 4.mp3") volume 0.2
    scene 08_479 with Dissolve(1)
    mc "{i}(*Sigh* And this was only the first day. I thought we would be able to have some fun, but after those exercises, everyone just wants to rest...){/i}"
    mc "{i}(Happy Zach and the others aren't back yet. I could use a little quiet.){/i}"
    if Alexis_Friends == True:
        scene black with Dissolve(1)
        pause 2
        scene 08_481 with vpunch
        mc "Do you have a death wish or something?"
        z "Oh shit!"
        z "I thought you were sleeping."
        mc "There'd better not be any marker on my face!"
        scene 08_482 with Dissolve(1)
        z "What have you been doing?"
        mc "I was trying to rest a bit. Training was a bitch."
        z "Yours too? Coach is drilling our asses."
        mc "..."
        mc "You seriously need to think before you speak sometimes."
        z "What do you mean?"
        mc "Nothing..."
        scene 08_483 with Dissolve(1)
        z "I really wanted to do some fun stuff after training, but damn, I'm so exhausted and not really in the mood today."
        mc "Hehe, I had the same thought. Tomorrow will be even worse."
        z "Yeah. Friday will be chill though, especially since we have the competition on Saturday."
        z "What are the girls doing?"
        scene 08_484 with Dissolve(1)
        mc "Elena, I don't know. Layla was going to shower, eat and then rest too."
        z "And Valeria?"
        mc "The last I saw her, she was talking to Darryl."
        z "What? Why would she be talking to Darryl? What were they talking about?"
        mc "No idea."
        scene 08_485 with Dissolve(1)
        z "I'll go look for her and see what she's up to."
        z "Want to come with me?"
        mc "No, I'll rest a bit more."
        z "Alright. If we plan something, I'll let you know."
        mc "Cool."
        scene black with Dissolve(2)
        pause 2
        scene 08_551 with Dissolve(1)
        z "You're still sleeping? Come on, man. I need your help."
        scene 08_545 with Dissolve(1)
        mc "What do you want?"
        z "I need a lookout."
        mc "What are you planning?"
        z "Hehe. You'll see for yourself."
        mc "Let me change real quick."
        jump Week3_Wednesday_Zach_Shower
    else:
        scene 08_480 with Dissolve(1)
        mc "{i}(Should I call Lexi now? I promised to call her every day.){/i}"
        menu:
            "Call her[KoGa3AutoWTChange1]{size=-4}({i}Layla Week3 Tuesday Train: Alexis Points+2{/i}) {/size} {/color}":
                if Layla_Week3_Tuesday_Train == True:
                    $ Alexis_Points += 2
                    # Alexis (40)
                    scene 08_488 with Dissolve(1)
                    mc "Hi!"
                    a "Hey, [mc]. Look at you. Keeping your promise."
                    mc "Yeah, I told you I'd call you every day."
                    a "Thanks."
                else:
                    if Erynn_Week3_Wednesday_Lying == True:
                        $ Alexis_Points -= 10
                        $ Alexis_End = True
                        $ Alexis_Friends = True
                        scene 08_488 with Dissolve(1)
                        mc "Hey, Lexi. How are you?"
                        a "Terrible!"
                        mc "How come? Are you still hurting because... You know?"
                        scene 08_489 with Dissolve(1)
                        a "You lied to me!"
                        mc "What?"
                        a "About Erynn. You lied to me!"
                        mc "{i}(Shit.){/i}"
                        scene 08_490 with Dissolve(1)
                        a "I trusted you!"
                        mc "Listen, I..."
                        a "No, I don't want to hear your excuses."
                        mc "Lexi, let me explain."
                        a "We are done!"
                        mc "Lexi..."
                        a "Asshole!"
                        scene 08_491 with Dissolve(1)
                        mc "Alexis?"
                        mc "*Sigh*"
                        mc "{i}(What should I have done?){/i}"
                        mc "{i}(Let's try again. Please just hear me out.){/i}"
                        scene 08_492 with Dissolve(1)
                        n "You've reached the voicemail..."
                        mc "{i}(She blocked me.){/i}"
                        mc "Fuck!"
                        scene 08_493 with Dissolve(1)
                        mc "*Muffled scream*"
                        scene 08_494 with Dissolve(1)
                        er "Are you okay?"
                        a "I'm sorry, Erynn. I'm so sorry."
                        er "I'm sorry, too!"
                        scene black with Dissolve(2)
                        pause 2
                        scene 08_551 with Dissolve(1)
                        z "You're still sleeping? Come on, man. I need your help."
                        scene 08_545 with Dissolve(1)
                        mc "What do you want?"
                        z "I need a lookout."
                        mc "What are you planning?"
                        z "Hehe. You'll see for yourself."
                        mc "Let me change real quick."
                        jump Week3_Wednesday_Zach_Shower
                    else:
                        $ Alexis_Points += 2
                        # Alexis (40)
                        scene 08_488 with Dissolve(1)
                        mc "Hi!"
                        a "Hey, [mc]. Look at you. Keeping your promise, huh?"
                        mc "Yeah, I told you I'd call you every day."
                        a "Thanks."
                        scene 08_495 with Dissolve(1)
                        mc "How is your... you know?"
                        a "It's better now. It did hurt for quite a while though."
                        mc "Sorry..."
                        a "I can hear you laughing."
                        mc "It was somewhat funny though. Maybe a little karma because of your strap-on joke yesterday."
                        scene 08_496 with Dissolve(1)
                        a "..."
                        a "Here's some karma for you. No more sex until you let me use a strap-on on you! That way you know how it feels."
                        mc "Uh, what? No..."
                        a "Yes!"
                        mc "Lexi..."
                        scene 08_497 with Dissolve(1)
                        mc "..."
                        mc "Lexi?"
                        mc "She hung up..."
                        mc "It wasn't that bad, was it? Should I call her back?"
                        scene 08_498 with Dissolve(1)
                        n "*Bzzzt. Bzzzt*"
                        mc "Oh, she's calling back."
                        scene 08_499 with Dissolve(1)
                        mc "Hi again."
                        a "Hey."
                        scene 08_500 with Dissolve(1)
                        mc "Sorry."
                        a "You're still laughing."
                        mc "I'm sorry, okay? I can't help it."
                        a "You're an idiot."
                scene 08_501 with Dissolve(1)
                a "How's camp?"
                mc "Exhausting, to say the least. Coach is pushing us to our limits."
                a "You'll be prepared for the competition, then."
                mc "Or so exhausted that I won't be able to participate."
                mc "But it's fun so far."
                scene 08_502 with Dissolve(1)
                a "What are the plans for the rest of the day?"
                mc "Relaxing! So I can withstand tomorrow's torture."
                a "Haha. It can't be that bad."
                mc "You have no idea. If I knew, I would've trained much more after school before coming here."
                scene 08_503 with Dissolve(1)
                mc "What are you doing?"
                a "I'm at the bar for my shift. We open in a few minutes."
                mc "I'm not calling at a bad time?"
                a "It's fine. Preparations are done already. I have some time."
                scene 08_504 with Dissolve(1)
                a "I called Erynn earlier."
                mc "You did? How did that go?"
                a "She picked up, but didn't say anything though. I didn't know what to say either. So, it was just silence for a few minutes before she hung up."
                mc "It's a start, maybe?"
                a "Yeah. I'm happy she picked up, at least. She could've simply ignored my call."
                if Erynn_Week3_Monday_Blackmailhelp == False:
                    scene 08_505 with Dissolve(1)
                    mc "I was at her place on Monday. I told her about us."
                    a "Oh? What did she say?"
                    scene 08_506 with Dissolve(1)
                    mc "She said she's fine with us dating. She's angry because..."
                    a "Because I lied to her. *Sigh* I should've just told her."
                    a "I miss her so much."
                    mc "She misses you too. She doesn't want to admit it. Just give her some time."
                    a "Yeah. Thanks for talking to her."
                    scene 08_507 with Dissolve(1)
                    mc "I'm going to talk to Layla today."
                    a "I'm so nervous about that."
                    mc "You and me both."
                    a "I hope it will be fine and she won't hate me."
                    mc "She won't, don't worry."
                else:
                    if Layla_Week3_Tuesday_Train == True:
                        if Erynn_Week3_Monday_Alexis_Mention == True:
                            scene 08_505 with Dissolve(1)
                            mc "I was at her place on Monday. I told her about us."
                            a "Oh? What did she say?"
                            scene 08_506 with Dissolve(1)
                            mc "She said she's fine with us dating. She's angry because..."
                            a "Because I lied to her. *Sigh* I should've just told her."
                            a "I miss her so much."
                            mc "She misses you too. She doesn't want to admit it. Just give her some time."
                            a "Yeah. Thanks for talking to her."
                            scene 08_507 with Dissolve(1)
                            mc "I'm going to talk to Layla today."
                            a "I'm so nervous about that."
                            mc "You and me both."
                            a "I hope it will be fine and she won't hate me."
                            mc "She won't, don't worry."
                        else:
                            scene 08_507 with Dissolve(1)
                            mc "I'm going to talk to Layla today."
                            a "I'm so nervous about that."
                            mc "You and me both."
                            a "I hope it will be fine and she won't hate me."
                            mc "She won't, don't worry."
                    else:
                        scene 08_507 with Dissolve(1)
                        mc "I'm going to talk to Layla today."
                        a "I'm so nervous about that."
                        mc "You and me both."
                        a "I hope it will be fine and she won't hate me."
                        mc "She won't, don't worry."
                scene 08_508 with Dissolve(1)
                mc "By the way. Can you send me a new picture?"
                a "Why do you want a picture?"
                mc "No special reason..."
                a "Uh-huh."
                scene 08_509 with Dissolve(1)
                a "I can't take such a picture right now. I'm at work, remember?"
                mc "I meant a normal picture."
                if Alexis_Week1_Saturday_Picture == True:
                    a "A normal picture?"
                    a "The last time we took a normal picture, you were disappointed."
                    scene 08_510 with Dissolve(1)
                    mc "Hey, hey, hey!"
                    mc "I thought you were talking about a different picture back then."
                    mc "And let's get one thing straight."
                    mc "I'm never disappointed in a picture when you're in it!"
                    scene 08_511 with Dissolve(1)
                    a "Heh..."
                    mc "What?"
                    a "That was sweet. Thank you."
                else:
                    a "Oh... Sure, I guess."
                scene 08_512 with Dissolve(1)
                a "{i}(I'm so bad at this.){/i}"
                a "{i}(I hope this one looks cute.){/i}"
                scene 08_513 with Dissolve(1)
                bd "What are you doing? Don't tell me you became one of those instant grammar girls."
                a "Instant? What?"
                bd "You know. The ones who take selfies all the time and make those weird faces."
                a "I'm just taking a picture for someone."
                scene 08_514 with Dissolve(1)
                bd "Oh my gosh! This picture is so cute. Just look at me."
                a "Haha. Shut up, Dylan!"
                scene 08_515 with Dissolve(1)
                bd "You know, if you take that kind of selfie for a guy, you need to push up your boobs with your other arm."
                a "What? No! How do you even know that?"
                bd "Uhm... I..."
                bd "I own a bar. I see things, okay?"
                a "Uh-huh."
                scene 08_516 with Dissolve(1)
                a "Sorry about that."
                a "Did you get it?"
                mc "Yes, I got it."
                a "Happy with it?"
                scene 08_517 with Dissolve(1)
                if Valeria_Week3_Wednesday_Pictures == True:
                    mc "{i}(Haha, she's so cute. She needs to work on her selfie skills though.){/i}"
                    mc "{i}(Maybe Valeria can give her some lessons. Her selfies were hot!){/i}"
                else:
                    mc "{i}(Haha, she's so cute. She needs to work on her selfie skills though.){/i}"
                mc "Really cute. First time I've seen you in a ponytail."
                a "Yeah, as you know, I didn't have time to wash it this morning."
                a "It looked pretty greasy, so I've bound it."
                a "Do you like it?"
                menu:
                    "Yes":
                        scene 08_518 with Dissolve(1)
                        mc "I do. You look so different, but really cute!"
                        a "Thank you."
                    "No":
                        scene 08_518 with Dissolve(1)
                        mc "I like the loose hair better."
                        a "Hehe, noted."
                        mc "Sorry."
                        a "No. I appreciate your honesty."
                scene 08_519 with Dissolve(1)
                a "Can you send me one of you now?"
                mc "Why do you want my picture?"
                a "Haha. Not telling you."
                mc "Then you don't get one."
                scene 08_520 with Dissolve(1)
                a "*Sigh*"
                a "Because I want one? Please?"
                mc "Oh well. Good enough, I guess. One second."
                menu:
                    "Selfie":
                        scene 08_521 with Dissolve(1)
                        mc "{i}(This should look close to what she sent.){/i}"
                        scene 08_522 with Dissolve(1)
                        mc "Did you get it?"
                        a "Yes, opening it now."
                        scene 08_523 with Dissolve(1)
                        a "You're so good looking, you know that?"
                        mc "You talk as if you aren't..."
                        mc "I'm the one who's punching here."
                        bd "What's going on?"
                        a "Here, have a look."
                        scene 08_527 with Dissolve(1)
                        a "Is he punching, or am I?"
                        bd "Definitely you! He's a handsome fella!"
                        scene 08_526 with Dissolve(1)
                        a "Go wash some dishes or something!"
                        bd "Haha. You asked me..."
                        scene 08_528 with Dissolve(1)
                        a "Dylan also really likes your picture."
                        a "Should I send it to him?"
                        mc "NO!"
                    "Dick pic":
                        scene 08_524 with Dissolve(1)
                        mc "{i}(I hope she won't be mad about this.){/i}"
                        mc "{i}(Maybe she'll even enjoy it?){/i}"
                        scene 08_525 with Dissolve(1)
                        a "Are you kidding me?"
                        a "Why would you send me this?"
                        bd "What's going on?"
                        scene 08_526 with Dissolve(1)
                        a "Nothing. Just... Never mind."
                        bd "..."
                scene 08_529 with Dissolve(1)
                z "Here you are. I've been looking for you."
                mc "One second."
                z "You need to come with me."
                mc "Kinda busy right now, I'm on the phone."
                scene 08_530 with Dissolve(1)
                z "That can wait. Give me that."
                mc "Hey!"
                scene 08_531 with Dissolve(1)
                z "Hi. This is Zach."
                z "I need [mc] right now, he'll call you back later."
                scene 08_532 with Dissolve(1)
                a "Hi, Zach."
                a "Did something happen?"
                scene 08_533 with Dissolve(1)
                z "Oh? You're a girl!"
                a "Uhm, yes..."
                z "Never mind then. I'll give the phone back."
                z "I'm so sorry."
                scene 08_534 with Dissolve(1)
                z "Sorry, sorry."
                mc "It's cool."
                z "I'll give you guys some one-on-one time."
                mc "Uh, thanks?"
                scene 08_535 with Dissolve(1)
                z "You're missing out."
                mc "What?"
                z "I'll tell you later!"
                scene 08_536 with Dissolve(1)
                mc "Sorry about that."
                mc "You know Zach. He's..."
                a "Haha, yeah."
                scene 08_537 with Dissolve(1)
                a "But don't let me stop you, if your friend needs you, go with him."
                mc "I'd rather talk to you though."
                a "Haha, thanks. I need to open the bar now anyway."
                a "And you'll only be at camp once, so go have fun."
                scene 08_538 with Dissolve(1)
                mc "You're awesome, you know that?"
                a "I try."
                mc "I'll call you again tomorrow then. Any specific time?"
                a "No, call me whenever you have time. Oh, and tell me how it went with Layla."
                mc "Oh yeah. I almost forgot about that. Now I'm getting nervous again."
                a "Sorry..."
                scene 08_539 with Dissolve(1)
                a "Thank you for calling."
                mc "You're welcome. Speak to you tomorrow."
                a "Can't wait."
                mc "Bye, Lexi."
                scene 08_540 with Dissolve(1)
                a "Goodnight, [mc]."
                a "Love you!"
                mc "What?"
                show 08_541
                a "..."
                scene 08_542 with Dissolve(1)
                mc "Hello?"
                mc "Lexi?"
                mc "She hung up."
                mc "Did she just say... It was just a figure of speech, right?"
                scene 08_543 with Dissolve(1)
                a "Oh no... No-no-no..."
                a "Why did I say that?"
                scene 08_544 with Dissolve(1)
                a "AAAH!"
                bd "{i}(She's so weird sometimes.){/i}"
                bd "Can you open up, Lex?"
                scene 08_545 with Dissolve(1)
                mc "Zach, wait up!"
                scene 08_546 with Dissolve(1)
                z "Don't worry, still here. I was waiting outside."
                mc "So much for one-on-one time."
                z "I can't go alone. I need a lookout."
                mc "What are you planning?"
                z "Hehe. You'll see for yourself."
                mc "Let me change real quick."
                if Layla_Week3_Tuesday_Train == False:
                    scene black with Dissolve(1)
                    pause 2
                    scene 08_547 with Dissolve(1)
                    mc "Zach question."
                    mc "Would you let a girl fuck you with a strap-on?"
                    z "Fuck yeah!"
                    mc "..."
                    mc "You didn't even think about that answer..."
                    z "I don't have to. A hot girl can do anything to me."
                    mc "{i}(Why did I even bother asking him?){/i}"
                    scene 08_548 with Dissolve(1)
                    z "Does the girl who was on the phone want to fuck you with a strap-on?"
                    mc "No... Just a random thought."
                    z "You have some weird thoughts... Who was that anyway? She sounded familiar."
                    scene 08_549 with Dissolve(1)
                    mc "Alexis."
                else:
                    scene 08_549 with Dissolve(1)
                    z "Who was the girl? She sounded familiar."
                    mc "Alexis."
                z "Alexis? Hot bartender Alexis?"
                mc "Yes."
                z "Wait... You're still in contact with her?"
                scene 08_550 with Dissolve(1)
                z "I know she asked for your number a while back, but damn. Lucky you."
                z "I hope you're tapping that ass."
                mc "..."
                jump Week3_Wednesday_Zach_Shower
            "Take a rest":
                mc "{i}(I'll call her later.){/i}"
                scene black with Dissolve(1)
                pause 2
                scene 08_481 with vpunch
                mc "Do you have a death wish or something?"
                z "Oh shit!"
                z "I thought you were sleeping."
                mc "There'd better not be any marker on my face!"
                scene 08_482 with Dissolve(1)
                z "What have you been doing?"
                mc "I was trying to rest a bit. Training was a bitch."
                z "Yours too? Coach is drilling our asses."
                mc "..."
                mc "You seriously need to think before you speak sometimes."
                z "What do you mean?"
                mc "Nothing..."
                scene 08_483 with Dissolve(1)
                z "I really wanted to do some fun stuff after training, but damn, I'm so exhausted and not really in the mood today."
                mc "Hehe, I had the same thought. Tomorrow will be even worse."
                z "Yeah. Friday will be chill though, especially since we have the competition on Saturday."
                z "What are the girls doing?"
                scene 08_484 with Dissolve(1)
                mc "Elena, I don't know. Layla was going to shower, eat and then rest too."
                z "And Valeria?"
                mc "The last I saw her, she was talking with Darryl."
                z "What? Why would she be talking to Darryl? What were they talking about?"
                mc "No idea."
                scene 08_485 with Dissolve(1)
                z "I'll go look for her and see what she's up to."
                z "Want to come with me?"
                mc "No, I'll rest a bit more."
                z "Alright. If we plan something, I'll let you know."
                mc "Cool."
                if Layla_Week3_Tuesday_Train == True:
                    scene black with Dissolve(1)
                    pause 2
                    scene 08_551 with Dissolve(1)
                    z "You're still sleeping? Come on, man. I need your help."
                    scene 08_545 with Dissolve(1)
                    mc "What do you want?"
                    z "I need a lookout."
                    mc "What are you planning?"
                    z "Hehe. You'll see for yourself."
                    mc "Let me change real quick."
                    jump Week3_Wednesday_Zach_Shower
                else:
                    if Erynn_Week3_Wednesday_Lying == True:
                        $ Alexis_End = True
                        $ Alexis_Friends = True
                        $ Alexis_Points -= 10
                        scene black with Dissolve(1)
                        pause 2
                        scene 08_486 with Dissolve(1)
                        n "*Bzzzt. Bzzzt*"
                        mc "Nggh..."
                        mc "Who's this now?"
                        scene 08_487 with Dissolve(1)
                        mc "Hello?"
                        a "Hi."
                        scene 08_488 with Dissolve(1)
                        mc "Oh hey, Lexi. How are you?"
                        a "Terrible!"
                        mc "How come? Are you still hurting because... You know?"
                        scene 08_489 with Dissolve(1)
                        a "You lied to me!"
                        mc "What?"
                        a "About Erynn. You lied to me!"
                        mc "{i}(Shit.){/i}"
                        scene 08_490 with Dissolve(1)
                        a "I trusted you!"
                        mc "Listen, I..."
                        a "No, I don't want to hear your excuses."
                        mc "Lexi, let me explain."
                        a "We are done!"
                        mc "Lexi..."
                        a "Asshole!"
                        scene 08_491 with Dissolve(1)
                        mc "Alexis?"
                        mc "*Sigh*"
                        mc "{i}(What should I have done?){/i}"
                        mc "{i}(Let's try again. Please just hear me out.){/i}"
                        scene 08_492 with Dissolve(1)
                        n "You've reached the voicemail..."
                        mc "{i}(She blocked me.){/i}"
                        mc "Fuck!"
                        scene 08_493 with Dissolve(1)
                        mc "*Muffled scream*"
                        scene 08_494 with Dissolve(1)
                        er "Are you okay?"
                        a "I'm sorry, Erynn. I'm so sorry."
                        er "I'm sorry too!"
                        scene black with Dissolve(2)
                        pause 2
                        scene 08_551 with Dissolve(1)
                        z "You're still sleeping? Come on, man. I need your help."
                        scene 08_545 with Dissolve(1)
                        mc "What do you want?"
                        z "I need a lookout."
                        mc "What are you planning?"
                        z "Hehe. You'll see for yourself."
                        mc "Let me change real quick."
                        jump Week3_Wednesday_Zach_Shower
                    else:
                        scene black with Dissolve(1)
                        pause 2
                        scene 08_551 with Dissolve(1)
                        z "You're still sleeping? Come on, man. I need your help."
                        scene 08_545 with Dissolve(1)
                        mc "What do you want?"
                        z "I need a lookout."
                        mc "What are you planning?"
                        z "Hehe. You'll see for yourself."
                        mc "Let me change real quick."
                        jump Week3_Wednesday_Zach_Shower

label Week3_Wednesday_Zach_Shower:
    scene black with Dissolve(1)
    pause 2
    scene 08_552 with Dissolve(1)
    mc "So, where are we going, what are we doing?"
    z "Patience, [mc]. Patience..."
    mc "{i}(Here we go again.){/i}"
    mc "{i}(We'll probably get in trouble for this.){/i}"
    scene 08_553 with Dissolve(1)
    mc "Wait... Isn't this the girls' shower?"
    z "*Whisper* Yes, this is the back entrance. Let's be quiet!"
    mc "*Whisper* This isn't a good idea, Zach."
    mc "*Whisper* If we get caught, we won't just get sent home, we'll get expelled!"
    z "*Whisper* That's why you're here, as a lookout."
    menu:
        "Go back[KoGa3AutoWTChange1]{size=-4}(Zach Points-2) {/size} {/color}":
            $ Zach_Points -= 2
            scene 08_554 with Dissolve(1)
            mc "*Whisper* This isn't worth the trouble, Zach."
            z "*Whisper* What? Come on, just a few minutes?"
            mc "*Whisper* Nah. Sorry, but I'm out."
            scene 08_555 with Dissolve(1)
            mc "*Whisper* Are you staying?"
            z "*Whisper* I'm just going to have a quick look. I'll be sneaky, don't worry."
            mc "*Whisper* You're crazy."
            z "*Whisper* No risk, no fun."
            mc "*Sigh* ..."
            jump Week3_Wednesday_Laylatalk
        "Help Zach[KoGa3AutoWTChange1]{size=-4}(Zach Points+2, Zach Week3 Wednesday TC Girlshower) {/size} {/color}":
            $ Zach_Points += 2
            # Zach (4)
            $ Zach_Week3_Wednesday_TC_Girlshower = True
            jump Week3_Wednesday_Zach_Shower_Help

label Week3_Wednesday_Zach_Shower_Help:
    if _in_replay:
        $ Layla_Week3_Wednesday_TC_AlexisTalk = False
    scene 08_556 with Dissolve(1)
    mc "*Whisper* Okay, but be quick. We can't stay too long."
    z "*Whisper* Hehe, I knew I could count on you!"
    scene 08_557 with Dissolve(1)
    mc "*Whisper* See anything?"
    z "*Whisper* It's the cheerleading team."
    mc "*Whisper* From our school?"
    z "*Whisper* Yes."
    scene 08_558 with Dissolve(1)
    mc "*Whisper* Anyone we know?"
    z "*Whisper* I know everyone here, but if you mean Elena, no, I don't see her."
    z "*Whisper* Which is a good thing. She's the last person I want to see..."
    mc "..."
    z "*Whisper* But why are they just standing there and talking?"
    scene 08_559 with Dissolve(1)
    z "*Whisper* Damn, what a failure."
    mc "*Whisper* Your turn."
    scene 08_560 with Dissolve(1)
    mc "{i}(I wouldn't call this a failure. Maybe he should've watched a little longer.){/i}"
    mc "{i}(I'm not gonna complain about this.){/i}"
    scene 08_561 with Dissolve(1)
    mc "{i}(Oh, that's Jasmine, Tori's BFF. I think she's in my geography and chemistry class. Never talked to her though.){/i}"
    mc "{i}(Maybe I should change that. Her tits are huge! When she cheers, they must be bouncing all over the place...){/i}"
    mc "{i}(Don't know the other girl.){/i}"
    scene 08_562 with Dissolve(1)
    z "*Whisper* Anything interesting?"
    mc "{i}(Sorry Zach, I'm quite enjoying this.){/i}"
    mc "*Whisper* There are still just talking."
    mc "{i}(Naked!){/i}"
    scene 08_563 with Dissolve(1)
    mc "*Whisper* Oh... There's Elena."
    mc "*Whisper* Do you want to switch again?"
    z "*Whisper* Elena? No thanks. I don't even want to look when she's naked."
    scene 08_564 with Dissolve(1)
    mc "*Whisper* I don't understand your animosity towards her."
    z "*Whisper* I just don't like her. That simple."
    z "*Whisper* You must have people you don't like."
    mc "*Whisper* True that."
    scene 08_565 with Dissolve(1)
    mc "{i}(Oh wow...){/i}"
    mc "{i}(You're missing out, Zach.){/i}"
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 08_566 at moveup
    pause 3
    mc "{i}(I'm so hard right now...){/i}"
    mc "{i}(First Jasmine, and now this!){/i}"
    scene 08_567 with Dissolve(1)
    mc "{i}(There are so many pretty girls in our school...){/i}"
    mc "{i}(I wish I could hear what they're talking about, though.){/i}"
    scene 08_568 with Dissolve(1)
    mc "{i}(Oh shit...){/i}"
    mc "{i}(Did she see?){/i}"
    scene 08_569 with Dissolve(1)
    el "{i}(Is someone there?){/i}"
    el "{i}(Hmm... Thought I saw something.){/i}"
    scene 08_570 with Dissolve(1)
    mc "*Whisper* We need to go, Zach. Like now!"
    z "*Whisper* What, why? Did they see you?"
    mc "*Whisper* I'm not sure, but let's not find out."
    scene black with Dissolve(1)
    pause 2
    scene 08_571 with Dissolve(1)
    mc "Haha, my heart's beating so fast..."
    z "Because of the running or what you saw?"
    mc "A little of both. Maybe one more than the other."
    z "Haha."
    scene 08_572 with Dissolve(1)
    $ achievement.grant("ACHIEVEMENT_TRUST_BRO")
    $ achievement.sync()
    z "Who did you see?"
    mc "Elena and Sienna just came out of the shower and Jasmine was undressing."
    z "Nice. I wish I saw Jasmine... Her boobs are massive. We'll try again later, or tomorrow, alright?"
    z "Maybe check out the girls from the other schools."
    scene 08_573 with Dissolve(1)
    z "I'm kinda hungry now."
    z "Want to go grab something to eat?"
    if Layla_Week3_Wednesday_TC_AlexisTalk == False:
        mc "Yeah, I could eat something."
    else:
        mc "I'll grab something later. I made plans with Layla earlier. She should be here soon, I think."
        z "A date?"
        mc "No, I need to talk to her about something."
        z "Hmm. Have fun, and I'll see you later."
    $ renpy.end_replay()
    jump Week3_Wednesday_Laylatalk

label Week3_Wednesday_Laylatalk:
    if Layla_Week3_Wednesday_TC_AlexisTalk == False:
        if Layla_Friends == True:
            jump Week3_Thursday
        else:
            if Layla_Points >= 45:
                jump Week3_Wednesday_Laylatalk_Solo
            else:
                jump Week3_Thursday
    else:
        jump Week3_Wednesday_Laylatalk_Alexis

label Week3_Wednesday_Laylatalk_Solo:
    if _in_replay:
        $ Layla_Week2_Wednesday_Knows = False
        $ Layla_Week2_Wednesday_Chichis = True
    $ Layla_Dating = True
    scene 08_574 with Dissolve(1)
    n "*Knock-knock*"
    mc "Come on in."
    scene 08_575 with Dissolve(1)
    la "Hey."
    mc "Hi. What are you doing here?"
    la "Just wanted to see you."
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 08_576 at moveup
    pause 3
    mc "You look cute."
    la "Thanks."
    mc "Sit down."
    scene 08_577 with Dissolve(1)
    la "This room is tiny."
    mc "I know."
    la "Ours is at least triple the size and we don't have bunk beds."
    scene 08_578 with Dissolve(1)
    mc "Really? How is that fair..."
    mc "Must have been a woman who made the room arrangements! Feminism at its finest."
    la "Haha."
    scene 08_579 with Dissolve(1)
    mc "So you only came here to see me?"
    la "Maybe..."
    mc "Heh."
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 08_580a at moveup
    pause 3
    mc "{i}(Damn. She looks so fucking sexy.){/i}"
    mc "{i}(Especially since her shirt is a little see-through.){/i}"
    scene 08_611 with Dissolve(1)
    mc "Sorry. You look just too cute."
    mc "I have to."
    la "..."
    scene 08_612 with Dissolve(1)
    ""
    scene 08_613 with Dissolve(1)
    la "..."
    scene 08_614 with Dissolve(1)
    ""
    scene 08_615 with Dissolve(1)
    ""
    scene 08_616 with Dissolve(1)
    mc "They look amazing."
    la "What?"
    if Layla_Week2_Wednesday_Chichis == True:
        mc "Your chichis."
    else:
        mc "Your boobs."
    la "Haha. You really like them, huh?"
    scene 08_617 with Dissolve(1)
    mc "I'm crazy about them."
    mc "Can I?"
    la "Your hands are already there."
    scene 08_618 with Dissolve(1)
    mc "{i}(They feel so great.){/i}"
    mc "{i}(Can't wait to suck them.){/i}"
    scene 08_619 with Dissolve(1)
    mc "{i}(Maybe later...){/i}"
    mc "{i}(I guess she wants to kiss some more.){/i}"
    scene 08_620 with Dissolve(1)
    mc "{i}(I like her cute and shy self, but when she's comfortable, she's so different.){/i}"
    scene 08_621 with vpunch
    n "*Slap*"
    la "Ah..."
    scene 08_622 with Dissolve(1)
    la "Seems like you found another body part to grab."
    mc "I can't help it. Everything feels so nice."
    la "Haha."
    scene 08_623 with Dissolve(1)
    mc "If you don't like it, tell me, okay?"
    la "If I didn't like it, I wouldn't let you touch me to begin with."
    scene 08_620 with Dissolve(1)
    z "Oh yeah [mc], stick your finger in my ass!"
    scene 08_624 with Dissolve(1)
    la "ZACH!"
    mc "What the fuck, Zach!"
    scene 08_625 with Dissolve(1)
    z "Haha, you should see your faces."
    la "Not funny! How long have you been here?"
    z "I saw [mc] slapping your ass."
    scene 08_626 with Dissolve(1)
    la "You're disgusting!"
    z "What? I was just joking..."
    la "See you tomorrow, [mc]."
    mc "Uh yeah. Bye, Layla."
    $ renpy.end_replay()
    scene 08_627 with Dissolve(1)
    z "Sorry, man."
    z "Maybe it was a little too much."
    menu:
        "Angry":
            scene 08_628 with Dissolve(1)
            mc "Seriously, Zach! Just shut up sometimes."
            mc "The least you could've done is announce that you were there instead of making that comment."
            mc "To us guys, this might be funny. But girls react differently to that, as you saw."
            scene 08_629 with Dissolve(1)
            z "Sorry, you're right."
            mc "No need to apologise to me. But you'd better apologise to Layla."
            z "I will."
        "Friendly[KoGa3AutoWTChange1]{size=-4}(Zach Points+2) {/size} {/color}":
            $ Zach_Points += 2
            # Zach (6)
            scene 08_628a with Dissolve(1)
            mc "Even though it wasn't the right time. It was kinda funny."
            mc "I had to do my best not to laugh in front of Layla."
            scene 08_629a with Dissolve(1)
            z "Yeah, she looked mad."
            mc "I think you'd better apologise to her though."
            z "Yeah, I will."
    scene 08_630 with Dissolve(1)
    z "Anyway, how about a beer?"
    mc "Did you bring beer as well? Aren't they warm?"
    z "A little, maybe."
    mc "Pass. I'll wait till after the competition before I drink."
    mc "I don't have teammates who pick up my slack."
    z "Ha-ha. Very funny..."
    jump Week3_Thursday

label Week3_Wednesday_Laylatalk_Alexis:
    scene black with Dissolve(1)
    pause 2
    scene 08_574 with Dissolve(1)
    n "*Knock-knock*"
    mc "Come on in."
    scene 08_575 with Dissolve(1)
    la "Hey."
    mc "Hi. All rested up?"
    la "Yeah. I needed that nap."
    if Layla_Friends == False:
        scene black with Dissolve(1)
        transform moveup:
            xalign 0.5 yalign 1.0
            linear 5.0 yalign 0.0
        show 08_576 at moveup
        pause 3
        mc "You look cute."
        la "Thanks."
        mc "Sit down."
        scene 08_577 with Dissolve(1)
        la "This room is tiny."
        mc "I know."
        la "Ours is at least triple the size and we don't have bunk beds."
    else:
        scene 08_577 with Dissolve(1)
        la "This room is tiny."
        mc "I know."
        la "Ours is at least triple the size and we don't have bunk beds."
    scene 08_578 with Dissolve(1)
    mc "Really? How is that fair..."
    mc "Must have been a woman who made the room arrangements! Feminism at its finest."
    la "Haha."
    scene 08_579 with Dissolve(1)
    la "So, you wanted to talk?"
    mc "Yeah. Want to go somewhere or stay here?"
    la "I don't mind staying here. It's quiet compared to outside. Lots of commotion going on."
    mc "Yeah, until the others are back."
    la "We can still go when they show up."
    scene 08_580 with Dissolve(1)
    la "I'm quite nervous since I have no idea what you want to talk about."
    mc "Hehe. I'm more nervous about how you're going to react."
    la "You're making it worse..."
    mc "Sorry, sorry."
    if Layla_Friends == False:
        scene black with Dissolve(1)
        transform moveup:
            xalign 0.5 yalign 1.0
            linear 5.0 yalign 0.0
        show 08_580a at moveup
        pause 3
        mc "{i}(Just sitting there, she turns me on...){/i}"
        scene 08_581 with Dissolve(1)
        mc "*Sigh* Where to start."
        mc "So... It's about your... Your sister."
    else:
        scene 08_581 with Dissolve(1)
        mc "*Sigh* Where to start."
        mc "So... It's about your... Your sister."
    scene 08_582 with Dissolve(1)
    la "Lexi?"
    mc "Yes."
    la "Okay. What about her?"
    if Layla_Friends == False:
        if Alexis_Friends == True:
            $ Layla_Dating = True
            scene 08_583 with Dissolve(1)
            mc "Alexis and I knew each other already before you introduced us at the pizzeria."
            la "Oh? So you met before? Why didn't you just tell me?"
            la "I thought you didn't like each other at first and that's why she didn't stay to eat, it felt so awkward."
            mc "Yeah, a lot happened before that day."
            la "What do you mean?"
            scene 08_584 with Dissolve(1)
            mc "I'll start from the beginning."
            mc "We met on the plane when I moved back to Madison Springs."
            mc "Well actually, we used to know each other way back because she's friends with Erynn."
            mc "But I didn't know that at that time. I didn't recognise her."
            mc "Anyway. A few days later we met again by chance and we've kept in contact since."
            scene 08_585 with Dissolve(1)
            la "So you met a few times?"
            mc "Well, we didn't just meet."
            scene 08_586 with Dissolve(1)
            mc "We... *Sigh* We hooked up..."
            la "What?"
            la "You hooked up with my sister?"
            scene 08_587 with Dissolve(1)
            mc "Yeah."
            mc "Back then, I didn't know she was your sister. I found out at the pizzeria."
            mc "That's why it was so awkward."
            la "I can't believe this."
            mc "I'm sorry, Layla."
            scene 08_588 with Dissolve(1)
            la "Why didn't you tell me then?"
            mc "I didn't think it was the right time to tell you then and there."
            mc "I wanted to be alone with you so I could explain it properly."
            scene 08_589 with Dissolve(1)
            mc "Hey, I'm so sorry."
            mc "Please say something, Layla."
            la "..."
            scene 08_590 with Dissolve(1)
            mc "Layla?"
            la "Give me a minute..."
            scene black with Dissolve(1)
            pause 2
            scene 08_591 with Dissolve(1)
            la "Do you like her?"
            mc "No, not like that. It was a hookup."
            scene 08_606 with Dissolve(1)
            mc "I'm sorry, Layla."
            mc "If I knew she was your sister, I..."
            scene 08_607 with Dissolve(1)
            la "What about me?"
            la "How do you feel about me?"
            scene 08_608 with Dissolve(1)
            mc "I like you. I like you a lot!"
            la "..."
            mc "Please stop crying."
            scene 08_609 with Dissolve(1)
            mc "..."
            la "I like you too. A lot!"
            scene 08_610 with Dissolve(1)
            mc "Really? That came out of nowhere."
            la "Idiot..."
            mc "Haha. Laughing suits you so much better."
            scene 08_611 with Dissolve(1)
            mc "You're so pretty."
            la "..."
            scene 08_612 with Dissolve(1)
            ""
            scene 08_613 with Dissolve(1)
            la "..."
            scene 08_614 with Dissolve(1)
            ""
            scene 08_615 with Dissolve(1)
            ""
            scene 08_616 with Dissolve(1)
            mc "They look amazing."
            la "What?"
            if Layla_Week2_Wednesday_Chichis == True:
                mc "Your chichis."
            else:
                mc "Your boobs."
            la "Haha. You really like them, huh?"
            scene 08_617 with Dissolve(1)
            mc "I'm crazy about them."
            mc "Can I?"
            la "Your hands are already there."
            scene 08_618 with Dissolve(1)
            mc "{i}(They feel so great.){/i}"
            mc "{i}(Can't wait to suck on them.){/i}"
            scene 08_619 with Dissolve(1)
            mc "{i}(Maybe later...){/i}"
            mc "{i}(I guess she wants to kiss some more.){/i}"
            scene 08_620 with Dissolve(1)
            mc "{i}(I like her cute and shy self, but when she's comfortable, she's so different.){/i}"
            scene 08_621 with vpunch
            n "*Slap*"
            la "Ah..."
            scene 08_622 with Dissolve(1)
            la "Seems like you found another body part to grab."
            mc "I can't help it. Everything feels so nice."
            la "Haha."
            scene 08_623 with Dissolve(1)
            mc "If you don't like it, tell me, okay?"
            la "If I didn't like it, I wouldn't let you touch me to begin with."
            scene 08_620 with Dissolve(1)
            z "Oh yeah [mc], stick your finger in my ass!"
            scene 08_624 with Dissolve(1)
            la "ZACH!"
            mc "What the fuck, Zach!"
            scene 08_625 with Dissolve(1)
            z "Haha, you should see your faces."
            la "Not funny! How long have you been here?"
            z "I saw [mc] slapping your ass."
            scene 08_626 with Dissolve(1)
            la "You're disgusting!"
            z "What? I was just joking..."
            la "See you tomorrow, [mc]."
            mc "Uh yeah. Bye, Layla."
            scene 08_627 with Dissolve(1)
            z "Sorry, man."
            z "Maybe it was a little too much."
            menu:
                "Angry":
                    scene 08_628 with Dissolve(1)
                    mc "Seriously, Zach! Just shut up sometimes."
                    mc "The least you could've done is announce that you were there instead of making that comment."
                    mc "To us guys, this might be funny. But girls react differently to that, as you saw."
                    scene 08_629 with Dissolve(1)
                    z "Sorry, you're right."
                    mc "No need to apologise to me. But you'd better apologise to Layla."
                    z "I will."
                "Friendly[KoGa3AutoWTChange1]{size=-4}(Zach Points+2) {/size} {/color}":
                    $ Zach_Points += 2
                    # Zach (6)
                    scene 08_628a with Dissolve(1)
                    mc "Even though it wasn't the right time. It was kinda funny."
                    mc "I had to do my best not to laugh in front of Layla."
                    scene 08_629a with Dissolve(1)
                    z "Yeah, she looked mad."
                    mc "I think you'd better apologise to her, though."
                    z "Yeah, I will."
            scene 08_630 with Dissolve(1)
            z "Anyway, how about a beer?"
            mc "Did you bring beer? Aren't they warm?"
            z "A little, maybe."
            mc "Pass. I'll wait till after the competition before I drink."
            mc "I don't have teammates who pick up my slack."
            z "Ha-ha. Very funny..."
            jump Week3_Thursday
        else:
            menu:
                "Tell her everything":
                    scene 08_583 with Dissolve(1)
                    mc "Alexis and I knew each other already before you introduced us at the pizzeria."
                    la "Oh? So you met before? Why didn't you just tell me?"
                    la "I thought you didn't like each other at first and that's why she didn't stay to eat, it felt so awkward."
                    mc "Yeah, a lot happened before that day."
                    la "What do you mean?"
                    scene 08_584 with Dissolve(1)
                    mc "I'll start from the beginning."
                    mc "We met on the plane when I moved back to Madison Springs."
                    mc "Well actually, we used to know each other way back because she's friends with Erynn."
                    mc "But I didn't know that at that time. I didn't recognise her."
                    mc "Anyway. A few days later we met again by chance and we've kept in contact since."
                    scene 08_585 with Dissolve(1)
                    la "So you met a few times?"
                    mc "Well, we didn't just meet."
                    scene 08_586 with Dissolve(1)
                    mc "We... *Sigh* We hooked up..."
                    la "What?"
                    la "You hooked up with my sister?"
                    scene 08_587 with Dissolve(1)
                    mc "Yeah."
                    mc "Back then, I didn't know she was your sister. I found out at the pizzeria."
                    mc "That's why it was so awkward."
                    la "I can't believe this."
                    mc "I'm sorry, Layla."
                    scene 08_588 with Dissolve(1)
                    la "Why didn't you tell me then?"
                    mc "I didn't think it was the right time to tell you then and there."
                    mc "I wanted to be alone with you so I could explain it properly."
                    scene 08_589 with Dissolve(1)
                    mc "Hey, I'm so sorry."
                    mc "Please say something, Layla."
                    la "..."
                    scene 08_590 with Dissolve(1)
                    mc "Layla?"
                    la "Give me a minute..."
                    scene black with Dissolve(1)
                    pause 2
                    scene 08_591 with Dissolve(1)
                    la "Do you like her?"
                    mc "Yeah, I do like her, but..."
                    scene 08_607 with Dissolve(1)
                    la "What about me?"
                    la "How do you feel about me?"
                    menu:
                        "Friends[KoGa3AutoWTChange1]{size=-4}(Layla Friends, {i}Layla Week3 Wednesday TC Kiss: Alexis Week3 Wednesday TC FriendsButKissedLayla, Layla Points-10{/i}, {i}else: Layla LikeMC{/i}) {/size} {/color}":
                            $ Layla_Friends = True
                            scene 08_590 with Dissolve(1)
                            if Layla_Week3_Wednesday_TC_Kiss == True:
                                $ Alexis_Week3_Wednesday_TC_FriendsButKissedLayla = True
                                $ Layla_Points -= 10
                                mc "I like you, Layla. But it's more like friends."
                                la "Why did you kiss me then, today?"
                                mc "I don't know."
                                la "That's not fair towards Alexis or me."
                                mc "You're right."
                                scene 08_591 with Dissolve(1)
                                la "I'm sorry, but I need to be alone for a while."
                                mc "I understand."
                                la "We'll talk tomorrow, okay?"
                                mc "I'm here whenever."
                                jump Week3_Wednesday_Night
                            else:
                                $ Layla_LikeMC = True
                                mc "I like you, Layla. But it's more like friends."
                                la "..."
                                mc "Layla?"
                                scene 08_591 with Dissolve(1)
                                la "I'm sorry, but I need to be alone for a while."
                                mc "I understand."
                                la "We'll talk tomorrow, okay?"
                                mc "I'm here whenever."
                                jump Week3_Wednesday_Night
                        "Break up with Alexis[KoGa3AutoWTChange1]{size=-4}(Layla Dating, Alexis Week3 Wednesday TC Breakup) {/size} {/color}":
                            $ Layla_Dating = True
                            $ Alexis_Week3_Wednesday_TC_Breakup = True
                            scene 08_608 with Dissolve(1)
                            mc "Alexis and I hooked up and I like her, but it's not the same way I like you."
                            mc "I'm crazy about you, Layla! I like you a lot!"
                            la "..."
                            mc "Please stop crying."
                            scene 08_590 with Dissolve(1)
                            mc "Layla?"
                            la "I'm sorry, but I need to be alone for a while."
                            mc "I understand."
                            la "We'll talk tomorrow, okay?"
                            mc "I'm here whenever."
                            jump Week3_Wednesday_Night
                "Leave out some details[KoGa3AutoWTChange1]{size=-4}(Layla Week3 Wednesday TC Alexis DateBoth, Layla Dating) {/size} {/color}":
                    $ Layla_Week3_Wednesday_TC_Alexis_DateBoth = True
                    $ Layla_Dating = True
                    scene 08_583 with Dissolve(1)
                    mc "Alexis and I knew each other already before you introduced us at the pizzeria."
                    la "Oh? So you met before? Why didn't you just tell me?"
                    la "I thought you didn't like each other at first and that's why she didn't stay to eat, it felt so awkward."
                    mc "Yeah, a lot happened before that day."
                    la "What do you mean?"
                    scene 08_584 with Dissolve(1)
                    mc "I'll start from the beginning."
                    mc "We met on the plane when I moved back to Madison Springs."
                    mc "Well actually, we used to know each other way back because she's friends with Erynn."
                    mc "But I didn't know that at that time. I didn't recognise her."
                    mc "Anyway. A few days later we met again by chance and we've kept in contact since."
                    scene 08_585 with Dissolve(1)
                    la "So you met a few times?"
                    mc "Well, we didn't just meet."
                    scene 08_586 with Dissolve(1)
                    mc "We... *Sigh* We hooked up..."
                    la "What?"
                    la "You hooked up with my sister?"
                    scene 08_587 with Dissolve(1)
                    mc "Yeah."
                    mc "Back then, I didn't know she was your sister. I found out at the pizzeria."
                    mc "That's why it was so awkward."
                    la "I can't believe this."
                    mc "I'm sorry, Layla."
                    scene 08_588 with Dissolve(1)
                    la "Why didn't you tell me then?"
                    mc "I didn't think it was the right time to tell you then and there."
                    mc "I wanted to be alone with you so I could explain it properly."
                    scene 08_589 with Dissolve(1)
                    mc "Hey, I'm so sorry."
                    mc "Please say something, Layla."
                    la "..."
                    scene 08_590 with Dissolve(1)
                    mc "Layla?"
                    la "Give me a minute..."
                    scene black with Dissolve(1)
                    pause 2
                    scene 08_591 with Dissolve(1)
                    la "Do you like her?"
                    mc "We just hooked up."
                    scene 08_606 with Dissolve(1)
                    mc "I'm sorry, Layla."
                    mc "If I knew she was your sister, I..."
                    scene 08_607 with Dissolve(1)
                    la "What about me?"
                    la "How do you feel about me?"
                    scene 08_608 with Dissolve(1)
                    mc "I like you. I like you a lot!"
                    la "..."
                    mc "Please stop crying."
                    scene 08_609 with Dissolve(1)
                    mc "..."
                    la "I like you too. A lot!"
                    scene 08_610 with Dissolve(1)
                    mc "Really? That came out of nowhere."
                    la "Idiot..."
                    mc "Haha. Laughing suits you so much better."
                    scene 08_611 with Dissolve(1)
                    mc "You're so pretty."
                    la "..."
                    scene 08_612 with Dissolve(1)
                    ""
                    scene 08_613 with Dissolve(1)
                    la "..."
                    scene 08_614 with Dissolve(1)
                    ""
                    scene 08_615 with Dissolve(1)
                    ""
                    scene 08_616 with Dissolve(1)
                    mc "They look amazing."
                    la "What?"
                    if Layla_Week2_Wednesday_Chichis == True:
                        mc "Your chichis."
                    else:
                        mc "Your boobs."
                    la "Haha. You really like them, huh?"
                    scene 08_617 with Dissolve(1)
                    mc "I'm crazy about them."
                    mc "Can I?"
                    la "Your hands are already there."
                    scene 08_618 with Dissolve(1)
                    mc "{i}(They feel so great.){/i}"
                    mc "{i}(Can't wait to suck them.){/i}"
                    scene 08_619 with Dissolve(1)
                    mc "{i}(Maybe later...){/i}"
                    mc "{i}(I guess she wants to kiss some more.){/i}"
                    scene 08_620 with Dissolve(1)
                    mc "{i}(I like her cute and shy self, but when she's comfortable, she's so different.){/i}"
                    scene 08_621 with vpunch
                    n "*Slap*"
                    la "Ah..."
                    scene 08_622 with Dissolve(1)
                    la "Seems like you found another body part to grab."
                    mc "I can't help it. Everything feels so nice."
                    la "Haha."
                    scene 08_623 with Dissolve(1)
                    mc "If you don't like it, tell me, okay?"
                    la "If I didn't like it, I wouldn't let you touch me to begin with."
                    scene 08_620 with Dissolve(1)
                    z "Oh yeah [mc], stick your finger in my ass!"
                    scene 08_624 with Dissolve(1)
                    la "ZACH!"
                    mc "What the fuck, Zach!"
                    scene 08_625 with Dissolve(1)
                    z "Haha, you should see your faces."
                    la "Not funny! How long have you been here?"
                    z "I saw [mc] slapping your ass."
                    scene 08_626 with Dissolve(1)
                    la "You're disgusting!"
                    z "What? I was just joking..."
                    la "See you tomorrow, [mc]."
                    mc "Uh yeah. Bye, Layla."
                    scene 08_627 with Dissolve(1)
                    z "Sorry, man."
                    z "Maybe it was a little too much."
                    menu:
                        "Angry":
                            scene 08_628 with Dissolve(1)
                            mc "Seriously, Zach! Just shut up sometimes."
                            mc "The least you could've done is announce that you were there instead of making that comment."
                            mc "To us guys, this might be funny. But girls react differently to that, as you saw."
                            scene 08_629 with Dissolve(1)
                            z "Sorry, you're right."
                            mc "No need to apologise to me. But you'd better apologise to Layla."
                            z "I will."
                        "Friendly[KoGa3AutoWTChange1]{size=-4}(Zach Points+2) {/size} {/color}":
                            $ Zach_Points += 2
                            # Zach (6)
                            scene 08_628a with Dissolve(1)
                            mc "Even though it wasn't the right time. It was kinda funny."
                            mc "I had to do my best not to laugh in front of Layla."
                            scene 08_629a with Dissolve(1)
                            z "Yeah, she looked mad."
                            mc "I think you'd better apologise to her, though."
                            z "Yeah, I will."
                    scene 08_630 with Dissolve(1)
                    z "Anyway, how about a beer?"
                    mc "Did you bring beer as well? Aren't they warm?"
                    z "A little maybe."
                    mc "Pass. I'll wait till after the competition before I drink."
                    mc "I don't have teammates who pick up my slack."
                    z "Ha-ha. Very funny..."
                    jump Week3_Wednesday_Night
    else:
        scene 08_583 with Dissolve(1)
        mc "As you know. Alexis and I knew each other already before you introduced us at the pizzeria."
        la "Oh? So you met before? Why didn't you just tell me?"
        la "I thought you didn't like each other at first and that's why she didn't stay to eat, it felt so awkward."
        mc "Yeah, a lot happened before that day."
        la "What do you mean?"
        scene 08_584 with Dissolve(1)
        mc "I'll start from the beginning."
        mc "We met on the plane when I moved back to Madison Springs."
        mc "Well actually, we used to know each other way back because she's friends with Erynn."
        mc "But I didn't know that at that time. I didn't recognise her."
        mc "Anyway. A few days later we met again by chance and we've kept in contact since."
        scene 08_585 with Dissolve(1)
        la "So you met a few times?"
        mc "Well, we didn't just meet."
        scene 08_586 with Dissolve(1)
        mc "We... *Sigh* We hooked up..."
        la "What?"
        la "You hooked up with my sister?"
        scene 08_587 with Dissolve(1)
        mc "Yeah."
        mc "Back then, I didn't know she was your sister. I found out at the pizzeria."
        mc "That's why it was so awkward."
        la "I can't believe this."
        mc "I'm sorry, Layla."
        scene 08_588 with Dissolve(1)
        la "Why didn't you tell me then?"
        mc "I didn't think it was the right time to tell you then and there."
        mc "I wanted to be alone with you so I could explain it properly."
        scene 08_589 with Dissolve(1)
        mc "Hey, I'm so sorry."
        mc "Please say something, Layla."
        la "..."
        scene 08_590 with Dissolve(1)
        mc "Layla?"
        la "Give me a minute..."
        scene black with Dissolve(1)
        pause 2
        if Alexis_Friends == True:
            scene 08_591 with Dissolve(1)
            la "Do you like her?"
            mc "Uhm... We aren't together or anything. We won't be either."
            mc "It was just a hookup and that's it."
            la "So you knew each other, hooked up, and that's it?"
            mc "Yeah. We thought you should know because we're friends."
            scene 08_583 with Dissolve(1)
            la "If that is all, I'm fine with it."
            la "Just wish I'd known earlier."
            la "I only hope it won't be awkward when we're all together."
            mc "Maybe a bit?"
            scene 08_600 with Dissolve(1)
            z "What will be awkward?"
            la "Nothing, Zach!"
            z "Just FYI, I can see your panties."
            la "Really, Zach?"
        else:
            scene 08_591 with Dissolve(1)
            la "Do you like her?"
            mc "Yeah, I like her."
            scene 08_592 with Dissolve(1)
            la "Then I approve."
            mc "What?"
            la "I approve!"
            mc "You got me there for a second."
            la "Hehe."
            scene 08_593 with Dissolve(1)
            la "We haven't known each other that long, but you're already one of my best friends."
            la "Also, I haven't seen Lexi this happy in a long time. But I think it has something to do with you."
            la "Now it all makes sense. The dancing, the singing..."
            scene 08_594 with Dissolve(1)
            la "Now I want to know everything."
            mc "Everything?"
            la "What? No, not... everything. But how you guys met. Have you been on dates?"
            scene black with Dissolve(1)
            pause 2
            scene 08_595 with Dissolve(1)
            la "That's so cute. I want that too. She's so lucky..."
            la "I'm gonna call her later. Maybe prank her a bit."
            scene 08_596 with Dissolve(1)
            mc "Don't be too mean to her, please."
            la "You're taking her side already, huh?"
            la "Good. And don't worry. I won't. I'm just gonna make her squirm a bit for not telling me."
            mc "That's on me. She wanted to tell you, but I asked her if I could do it."
            la "Oh... I'll still call her though and have a bit of fun."
            scene 08_597 with Dissolve(1)
            la "You'd better be nice to her, or you're going to have problems with me!"
            la "And with the school principal."
            mc "Haha. That's right. I hadn't even thought about that."
            scene 08_598 with Dissolve(1)
            la "I'm happy it's you."
            mc "Lexi has an amazing sister."
            la "Hehe, thank you."
            scene 08_599 with Dissolve(1)
            la "And you're calling her Lexi? She doesn't let just anyone call her that."
            mc "Yeah, she asked... Well, told me to call her Lexi."
            la "She must really like you."
            scene 08_600 with Dissolve(1)
            z "Who likes who?"
            la "No one."
            z "Just FYI, I can see your panties."
            la "Really, Zach?"
        scene 08_601 with Dissolve(1)
        z "Yes really. That's why I said it."
        la "*Sigh* Oh my god..."
        scene 08_602 with Dissolve(1)
        la "I'm going back to my room now."
        mc "Alright. Thanks for listening."
        la "If you ever need to talk, I'm here for you."
        mc "Thanks, Layla."
        la "See you tomorrow, then."
        scene 08_603 with Dissolve(1)
        z "Good night, Layla. Sleep tight."
        la "Night, Zach!"
        scene 08_604 with Dissolve(1)
        z "Did I interrupt something?"
        mc "No, we only talked."
        z "What a shame. She looked so sexy though."
        mc "As you said, she looks good in anything she wears."
        z "Right?"
        scene 08_605 with Dissolve(1)
        z "Anyway, how about a beer?"
        mc "Did you bring beer as well? Aren't they warm?"
        z "A little maybe."
        mc "Pass. I'll wait till after the competition before I drink."
        if Alexis_Friends == False:
            jump Week3_Wednesday_Night
        else:
            jump Week3_Thursday

label Week3_Wednesday_Night:
    scene black with Dissolve(1)
    pause 2
    scene 08_631 with Dissolve(1)
    play sound "Sounds/Phone_Vibrate.mp3"
    n "*Bzzzt. Bzzzt*"
    mc "{i}(This happens way too often in the middle of the night.){/i}"
    mc "{i}(Who is it this time?){/i}"
    scene 08_632 with Dissolve(1)
    mc "{i}(Heh, Lexi again. Should've known.){/i}"
    mc "{i}(She's probably finished her shift at the bar.){/i}"
    mc "{i}(Let's see... Oh, it's a video.){/i}"
    show 08_634
    a "Hey!"
    pause 4
    play sound "Sounds/Good_Night.mp3" volume 2.0
    a "Good night!"
    $ renpy.end_replay()
    if Layla_Week3_Wednesday_TC_Alexis_DateBoth == True:
        scene 08_635 with Dissolve(1)
        mc "{i}(That was hot!){/i}"
        mc "{i}(How will I be able to sleep now, Lexi?){/i}"
        scene 08_636 with Dissolve(1)
        mc "{i}(Fuck... What am I doing?){/i}"
        mc "{i}(I'm dating Lexi, but told Layla I like her...){/i}"
        mc "{i}(Can I date both? But they're sisters... This won't end well.){/i}"
        mc "{i}(I have to make a decision sooner or later or they'll find out.){/i}"
        mc "*Sigh*"
    else:
        if Alexis_Week3_Wednesday_TC_Breakup == True:
            scene 08_636 with Dissolve(1)
            mc "{i}(Fuck...){/i}"
            mc "{i}(She sends me this and I'm breaking up with her tomorrow...){/i}"
            mc "{i}(I feel really bad now.){/i}"
        else:
            scene 08_635 with Dissolve(1)
            mc "{i}(That was hot!){/i}"
            mc "{i}(How will I be able to sleep now, Lexi?){/i}"
    jump Week3_Thursday

label Week3_Thursday:
    scene black with Dissolve(2)
    pause 2
    stop music fadeout 1.0
    play music ("Music/LoFi Upbeat 1.mp3", "Music/LoFi Upbeat 2.mp3", "Music/LoFi Upbeat 3.mp3", "Music/LoFi Upbeat 4.mp3") volume 0.2
    n "Thursday morning. Second day of training camp."
    scene 08_637 with Dissolve(1)
    mg "Shit, what happened to you? You look terrible."
    mc "I feel worse. I couldn't sleep."
    mg "Muscle aches?"
    mc "Something like that."
    scene 08_638 with Dissolve(1)
    mc "Zach's gone already?"
    mg "Oh, he had to go somewhere. Something important. He took Jay with him."
    mc "Heh. I can guess where he went..."
    scene 08_639 with Dissolve(1)
    mc "Where were you yesterday? You came back late."
    mg "I was supporting our cheer squad."
    mc "Supporting? That's what they call it now?"
    mg "Haha. You got me. I was watching Elena. She looks so damn cute in her uniform."
    mc "{i}(She sure does.){/i}"
    mg "Anyway, you'd better get ready if you want to be on time."
    mc "Is it that late already?"
    scene black with Dissolve(1)
    pause 2
    scene 08_640 with Dissolve(1)
    mc "{i}(Heh, she's here already.){/i}"
    mc "{i}(And no one else. Damn Miguel... I still had some time.){/i}"
    mc "Good morning, Val."
    scene 08_641 with Dissolve(1)
    va "Oh, hey. Good morning, [mc]."
    mc "First ones here again?"
    va "Haha, yeah."
    scene 08_642 with Dissolve(1)
    va "I've been here for forty minutes already."
    mc "What? Forty minutes? Why?"
    va "I did some training on my own."
    mc "Girl, you're crazy. How do you even have the energy after yesterday?"
    scene 08_643 with Dissolve(1)
    va "I like early mornings."
    mc "I like them too, as long as I'm in my bed!"
    va "Haha."
    scene 08_644 with Dissolve(1)
    mc "You remind me of another girl. She woke me up at six in the morning to go jogging with her."
    va "Layla?"
    mc "No, it was before I moved back to Madison Springs."
    scene 08_645 with Dissolve(1)
    mc "*Sigh* Aaah..."
    va "What was that? You sound like you're a hundred years old."
    va "You haven't even run yet. Still exhausted from yesterday?"
    scene 08_646 with Dissolve(1)
    mc "No, my back aches. I didn't get much sleep. I can never sleep in another bed the first night."
    mc "I don't know why, it's weird but, yeah..."
    va "It's not weird. You just don't feel comfortable in another bed."
    scene 08_647 with Dissolve(1)
    va "I can give you a massage if you'd like?"
    menu:
        "No thanks":
            mc "It's fine, thanks though. It will be over soon."
            mc "How about I do some warm-up laps with you?"
            va "Sure."
            jump Week3_Thursday_Warmup
        "That'd be great[KoGa3AutoWTChange1]{size=-4}(Valeria Week3 Thursday TC Massage) {/size} {/color}":
            $ Valeria_Week3_Thursday_TC_Massage = True
            mc "Yeah? That'd be great, thank you."
            scene 08_648 with Dissolve(1)
            va "Where does it hurt the most?"
            mc "My left side, right there."
            va "Tell me if I'm too rough, okay?"
            scene 08_649 with Dissolve(1)
            mc "Hehe..."
            va "Why are you laughing?"
            mc "Nothing..."
            va "Tell me!"
            mc "Just your too rough comment."
            scene 08_650 with Dissolve(1)
            va "..."
            scene 08_651 with Dissolve(1)
            mc "Aaah... I get it, I get it..."
            va "What?"
            mc "Too rough! Too rough!"
            scene black with Dissolve(1)
            pause 2
            scene 08_652 with Dissolve(1)
            mc "This feels nice. You've done this before, huh?"
            va "A few times."
            mc "What a lucky guy!"
            va "..."
            mc "What do I owe you?"
            va "Nothing. You helped me stretch yesterday, so we're even."
            scene 08_653 with Dissolve(1)
            mc "What if I want another one?"
            va "Hmm..."
            mc "What do they usually charge for a massage?"
            if Layla_Dating == True:
                jump Week3_Thursday_Layla_Massage
            else:
                if Tori_Week3_Wednesday_TC_Fun == True:
                    jump Week3_Thursday_Tori_Massage
                else:
                    va "I have no idea."
                    mc "How about I do some warm-up laps with you?"
                    va "Sure."
                    jump Week3_Thursday_Warmup

label Week3_Thursday_Layla_Massage:
    scene 08_654 with Dissolve(1)
    va "I have no idea."
    la "..."
    scene 08_655 with Dissolve(1)
    mc "Mostly I get them for free."
    va "Haha. You do?"
    mc "Layla gave me one when we were at the beach. It was really good."
    va "You really like her, huh?"
    scene 08_656 with Dissolve(1)
    mc "Yeah, I do."
    scene 08_657 with Dissolve(1)
    mc "How do you get along with her?"
    la "*Whisper* Shhh. Let's switch."
    scene 08_658 with Dissolve(1)
    va "We haven't talked much, but she seems fun."
    mc "Let's plan something for tomorrow. We only have half a day."
    va "Uhm..."
    la "*Whisper* Swimming pool."
    va "Maybe we can check out the swimming pool?"
    mc "Relaxing by the pool. Perfect!"
    scene 08_659 with Dissolve(1)
    mc "By the way. What did you do yesterday after training?"
    va "I hung out with Tori and Darryl."
    mc "What's that like?"
    va "Argumentative."
    mc "Haha."
    scene 08_660 with Dissolve(1)
    mc "As I said, you're welcome to hang out with us."
    mc "Or go to Elena and Layla's room. I'm pretty sure they won't mind."
    va "Yeah, I'll do that. Thanks."
    scene 08_661 with Dissolve(1)
    la "*Whisper* ..."
    va "*Whisper* Really?"
    scene 08_662 with Dissolve(1)
    va "So, who gives the best massage?"
    mc "Hmm, they're both great but if I have to choose."
    menu:
        "Layla":
            mc "This might be a little biased, but Layla..."
            scene 08_663 with Dissolve(1)
            la "Good answer."
            mc "Uhm... Layla?"
            scene 08_664 with Dissolve(1)
            mc "..."
            la "Yes!"
        "Valeria":
            mc "I think yours slightly edges it."
            scene 08_665 with Dissolve(1)
            va "Uh... Thank you?"
            mc "But please don't tell Layla I said that."
            va "I won't..."
            scene 08_666 with Dissolve(1)
            mc "Val? What are you doing?"
            la "..."
            scene 08_667 with Dissolve(1)
            mc "Hey!"
            mc "Stop!"
            scene 08_668 with Dissolve(1)
            mc "Layla!"
            la "Haha."
    scene 08_669 with Dissolve(1)
    va "Sorry, sorry."
    mc "Haha. When did you switch? I didn't even realise."
    va "A minute ago or so."
    mc "That's funny. Really, I had no idea."
    scene 08_670 with Dissolve(1)
    la "So, your back was hurting?"
    mc "I didn't sleep much."
    la "How does it feel now? Better already?"
    mc "Much better. Thanks to both of you. Think I'm ready for some warm-up laps. Anyone up for it?"
    la "I'll go stretch first."
    va "I can join you."
    jump Week3_Thursday_Warmup

label Week3_Thursday_Tori_Massage:
    scene 08_671 with Dissolve(1)
    va "I have no idea."
    mc "But we can exchange massages for me helping you stretch?"
    va "Maybe. I'll think about it."
    scene 08_672 with Dissolve(1)
    to "{i}(This can be interesting.){/i}"
    mc "Not a good deal?"
    va "I like to barter."
    mc "Haha. Okay."
    scene 08_673 with Dissolve(1)
    to "*Whisper* Shhh. Move, let me do it."
    va "..."
    scene 08_674 with Dissolve(1)
    mc "Uhm... Okay?"
    mc "Is this part of the barter? I think I got the better deal..."
    scene 08_675 with Dissolve(1)
    mc "Val?"
    mc "This is... Wait..."
    scene 08_676 with vpunch
    mc "What the fuck, Tori."
    to "Hey there."
    mc "Get off!"
    to "I thought you enjoyed yesterday?"
    va "..."
    scene 08_677 with Dissolve(1)
    to "Don't worry, Val. It was just a little touching..."
    to "No harm, no foul. Right?"
    va "Uhm, sure..."
    scene 08_678 with Dissolve(1)
    mc "{i}(Just a little touching...){/i}"
    menu:
        "Leave":
            mc "{i}(I think I'll do some warm-up laps. Not going to play her games...){/i}"
            jump Week3_Thursday_Warmup
        "Slap her ass[KoGa3AutoWTChange1]{size=-4}(Tori Points+2) {/size} {/color}":
            $ Tori_Points += 2
            # Tori (8)
            scene 08_679 with vpunch
            n "*Slap*"
            to "Aaah..."
            mc "No harm, no foul!"
            scene 08_680 with Dissolve(1)
            to "I wouldn't say no harm, but definitely no foul."
            to "I guess it's your turn now, Val."
            va "What?"
            scene 08_681 with Dissolve(1)
            to "Come here. let me spank that ass."
            va "Tori..."
            scene 08_682 with vpunch
            va "Ouch..."
            da "Hey."
            scene 08_683 with Dissolve(1)
            va "Oh... I'm sorry, Darryl."
            da "Nah, it's alright, baby girl."
            mc "{i}(Baby girl?){/i}"
            scene 08_684 with Dissolve(1)
            to "What are you doing?"
            to "She needs to get spanked."
            da "You've been naughty, Val?"
            da "I can help with that!"
            scene 08_685 with vpunch
            va "Aaah..."
            scene 08_686 with Dissolve(1)
            va "..."
            da "Damn, baby girl. That's a nice ass you have there!"
            da "How about we skip today's training and play with it some more?"
            scene 08_687 with vpunch
            va "Get off me!"
            da "What? Yesterday you were all over me!"
            va "You wish!"
            scene black with Dissolve(1)
            pause 2
            scene 08_688 with Dissolve(1)
            mc "Are you okay?"
            va "No..."
            scene 08_689 with Dissolve(1)
            va "Why do they always have to touch me like that?"
            va "First Zach, then Joshua and Aaron..."
            mc "{i}(Joshua? Aaron? She's really popular.){/i}"
            va "Now Darryl..."
            mc "I'd agree with you, but I'd be a hypocrite since I did the same."
            scene 08_690 with Dissolve(1)
            va "I asked you to help me stretch, that's different."
            mc "I meant with Tori before."
            va "..."
            scene 08_691 with Dissolve(1)
            mc "Want me to beat up Darryl?"
            va "Haha, no..."
            mc "How about some warm-up laps then? Maybe it'll help you think of something else?"
            va "I'd like that."
            mc "Well, warm-up laps for me, for you it's just more running, since you were here so early."
            va "Haha, true."
            jump Week3_Thursday_Warmup

label Week3_Thursday_Warmup:
    scene black with Dissolve(1)
    pause 2
    scene 08_692 with Dissolve(1)
    mc "{i}(She hasn't said anything since we started...){/i}"
    mc "{i}(Maybe she doesn't talk while running?){/i}"
    mc "{i}(This might cheer her up a bit.){/i}"
    scene 08_693 with Dissolve(1)
    mc "When I was around five, I always wanted a pet, but my parents never got me one."
    mc "I knew that chickens sat on eggs to hatch little chicks."
    mc "So I used to steal eggs out of the fridge and hide them in warm places all over the house."
    scene 08_694 with Dissolve(1)
    mc "Like under the radiator or inside my parents' shoes."
    mc "After a while, I just forgot about them."
    mc "Weeks or even months later, my... My dad screamed all of a sudden."
    scene 08_695 with Dissolve(1)
    mc "He stepped on an egg when putting his shoes on."
    mc "A smelly surprise, let me tell you."
    va "Haha."
    mc "They found eight more eggs that day."
    va "Eight? Haha..."
    jump Week3_Thursday_Afternoon

label Week3_Thursday_Afternoon:
    scene black with Dissolve(2)
    pause 2
    n "Late afternoon, after another tiresome training session."
    if Alexis_Friends == False:
        if Layla_Dating == False:
            if Layla_Week3_Wednesday_TC_Kiss == True:
                $ Alexis_End = True
                $ Alexis_Friends = True
                $ Alexis_Points -= 10
                stop music fadeout 1.0
                play music "Music/Slow4.mp3" volume 0.5
                scene 08_696 with Dissolve(1)
                mc "Hi."
                a "Hey."
                mc "How are you?"
                a "..."
                mc "Lexi?"
                scene 08_722 with Dissolve(1)
                a "Layla called me yesterday."
                mc "She did? I told her about us."
                a "I know. But you didn't tell me about you and her!"
                if Alexis_Week2_Sunday_Honest == True:
                    scene 08_699 with Dissolve(1)
                    mc "I did. When I was at your place. I even told you we kissed."
                    a "Yes, past tense. You didn't tell me yesterday you are still..."
                else:
                    scene 08_699 with Dissolve(1)
                    mc "We're friends."
                    a "Friends? I'm not making out with my friends."
                scene 08_723 with Dissolve(1)
                a "I know we haven't talked about or defined our relationship."
                a "But this..."
                a "I still consider this cheating!"
                a "And it's not just with anyone..."
                a "She's my sister, [mc]!"
                a "Even if she didn't call me. How long do you think you could keep this up before we found out?"
                scene 08_724 with Dissolve(1)
                mc "I wasn't hiding it. I like you both."
                mc "I just wasn't sure what to do or who to choose."
                a "..."
                scene 08_725 with Dissolve(1)
                a "I can help you with that!"
                a "We are over!"
                mc "Lexi..."
                a "Don't Lexi me!"
                scene 08_726 with Dissolve(1)
                mc "Lex... Alexis?"
                mc "..."
                scene 08_727 with Dissolve(1)
                mc "*Sigh*"
                scene black with Dissolve(2)
                pause 2
                scene 08_736 with Dissolve(1)
                la "There you are."
                la "I've been looking for you..."
                la "What are you doing here?"
                scene 08_737 with Dissolve(1)
                la "Is this seat taken?"
                mc "No, go ahead."
                scene 08_738 with Dissolve(1)
                la "..."
                mc "..."
                scene 08_739 with Dissolve(1)
                la "I talked to Alexis yesterday after our talk."
                mc "Yeah, I know. I talked with her just now."
                la "..."
                la "I'm sorry about..."
                scene 08_740 with Dissolve(1)
                mc "No, no. You have nothing to be sorry for."
                mc "I'm the one who's sorry."
                mc "I should've said something way sooner. Especially once I knew you were sisters."
                mc "So much has been happening lately and it was never the right time..."
                mc "*Sigh* These are all just bad excuses... I'm sorry."
                scene 08_739 with Dissolve(1)
                la "You really like her, huh?"
                mc "I do, but it doesn't matter anymore. She broke it off."
                la "..."
                la "I'm sorry."
                mc "It's my fault."
                scene black with Dissolve(1)
                pause 2
                scene 08_743 with Dissolve(1)
                la "So what should we do now?"
                mc "You've been my best friend since I moved back and I hope we can stay that way."
                mc "I want to hang out with you and have fun, but..."
                la "No more making out."
                mc "Heh, yes. You could put it that way."
                scene 08_744 with Dissolve(1)
                la "You're also one of my best friends. And I'd rather be friends than..."
                mc "Yeah."
                la "Hehe."
                la "Hugging is still allowed, right?"
                mc "Yes, it is."
                scene 08_745 with Dissolve(1)
                la "How about we start over? Strictly as friends?"
                mc "Perfect."
                scene 08_746 with Dissolve(1)
                mc "Hi. I'm [mc]."
                la "Hey. Layla. Haha..."
                el "YOU!"
                scene 08_747 with Dissolve(1)
                mc "Aaah..."
                el "HOW COULD YOU!"
                scene 08_748 with Dissolve(1)
                mc "Elena!"
                scene 08_749 with Dissolve(1)
                mc "What are you..."
                el "I SHOULD BEAT..."
                scene 08_750 with Dissolve(1)
                la "ELENA STOP!"
                el "..."
                el "You're not crying?"
                la "What? No..."
                el "..."
                la "I'll explain."
                scene black with Dissolve(1)
                pause 2
                scene 08_751 with Dissolve(1)
                el "Dios mío... You two are something else. So confusing!"
                el "And since it seems that I have no idea about... any of what has been going on lately. You'd better tell me everything from the very beginning."
                scene 08_752 with Dissolve(1)
                mc "Alright. I'll tell you."
                mc "I met Alexis during..."
                scene black with Dissolve(1)
                pause 2
                scene 08_754 with Dissolve(1)
                el "Who would've expected that?"
                la "Yeah, you tell me."
                scene 08_755 with Dissolve(1)
                el "I'm sorry, [mc]. For tackling you and almost slapping you."
                mc "It's all good, Elena. You're being a good friend and protecting Layla."
                el "Can I hug you as an apology at least?"
                mc "That's so unlike you, but sure."
                scene 08_756 with Dissolve(1)
                el "You're so sticky and you smell. You need a shower."
                mc "Haha, that's the Elena I know."
                el "Haha, I'm sorry."
                mc "No, you're right. I need a shower and that's what I'll be going to do now."
                scene 08_757 with Dissolve(1)
                mc "See you tomorrow, then?"
                la "Yes. Bye, [mc]."
                mc "Later. And thank you, Layla!"
                el "Bye."
                jump Week3_Thursday_Evening
            else:
                $ Alexis_Dating = True
                scene 08_696 with Dissolve(1)
                mc "Hi."
                a "Hey. How are you?"
                mc "Exhausted again. These exercises are so hard."
                a "Are you done for today?"
                mc "Yes. And very happy about that."
                a "Haha."
                scene 08_697 with Dissolve(1)
                mc "What are you doing?"
                a "I'm actually home. Had to do some chores."
                mc "Right, the punishment chores. I'm so sorry."
                a "It's fine. Worth it."
                mc "Haha."
                scene 08_698 with Dissolve(1)
                mc "How long do you have to do them for?"
                a "This week and next."
                a "Mom is very strict about these things."
                mc "Yeah, Layla told me that too, once."
                scene 08_699 with Dissolve(1)
                a "Speaking about Layla. She called me yesterday."
                mc "She did? Well, she told me yesterday she might call you. But since she hasn't mentioned anything today, I thought she hadn't yet."
                mc "How was it? What did she say?"
                scene 08_700 with Dissolve(1)
                a "She was so mad!"
                mc "Huh? What? Really?"
                mc "{i}(She said she would joke with her, but since she didn't say anything today, maybe she's upset after all?){/i}"
                scene 08_701 with Dissolve(1)
                a "She was like: 'How can you do that?', 'Why him?', 'I can't believe you did that...'"
                mc "{i}(Oh shit...){/i}"
                scene 08_702 with Dissolve(1)
                a "But she couldn't keep her act up for long. I heard her giggling in between."
                a "So the jig was up."
                mc "{i}(She got me there for a second, too...){/i}"
                scene 08_703 with Dissolve(1)
                a "She told me what you told her, and I didn't expect her reaction after that."
                a "She was happy for us. And excited."
                scene 08_704 with Dissolve(1)
                a "I always thought she liked you. So her reaction surprised me even more."
                mc "We're good friends and have fun hanging out. We might come across as flirty sometimes, but that's about it."
                a "Thank you [mc], for telling her."
                mc "Of course. Maybe I waited a little too long, but it went way better than expected."
                scene 08_705 with Dissolve(1)
                a "I agree."
                a "I was scared that another Erynn situation would happen."
                mc "I had the same feeling."
                scene 08_706 with Dissolve(1)
                mc "Anything new with Erynn?"
                a "I haven't spoken to her. She wasn't at school today."
                mc "Hmm, okay..."
                mc "{i}(Maybe I should call her.){/i}"
                scene black with Dissolve(1)
                pause 2
                scene 08_707 with Dissolve(1)
                mc "What are your plans for the rest of the day? Do you have to work?"
                a "No, I'm off today. I'm going to relax a bit and then start working on an assignment for school."
                mc "Sounds like fun. The relaxing part, not the assignment."
                a "Haha."
                a "How about you?"
                scene 08_708 with Dissolve(1)
                mc "First, I need a shower. Badly."
                a "We have a shower!"
                mc "Haha, I'm not running to your house this time."
                a "Aw... Too bad. And after your shower?"
                mc "Grab something to eat. And if I still have some energy left, I'll see what the others are up to and join them in whatever, I guess."
                am "Why aren't the dishes done?"
                scene 08_709 with Dissolve(1)
                a "Sorry, give me one second."
                mc "Sure."
                scene 08_710 with Dissolve(1)
                a "Hey, Mom. What did you say?"
                am "The dishes... Why aren't they done yet?"
                a "I got a call. I was about to do them..."
                scene 08_711 with Dissolve(1)
                am "Come on. I'll help you. You can call your boyfriend later."
                a "What? My boy... No... I mean... How do..."
                scene 08_712 with Dissolve(1)
                am "Mother's intuition."
                a "..."
                am "You've been my daughter for twenty years. I know when something's up."
                am "Invite him over next time."
                a "Uhm..."
                am "Come on now."
                scene 08_713 with Dissolve(1)
                a "Sorry, I have to go."
                mc "No worries."
                a "Speak to you tomorrow?"
                mc "Yeah, I'll call you."
                scene 08_714 with Dissolve(1)
                a "Okay, thank you for calling today. Bye, [mc]."
                mc "Didn't you forget something?"
                a "Hmm?"
                scene 08_715 with Dissolve(1)
                a "Nooo... You heard that?"
                a "That was just... You know... Aah... I hoped you'd forget."
                mc "That ended quickly."
                scene 08_716 with Dissolve(1)
                a "No, it's not that I don't..."
                a "..."
                a "What am I saying?"
                a "Uhm... Bye."
                scene 08_717 with Dissolve(1)
                mc "{i}(Haha, she hung up.){/i}"
                mc "{i}(Why is she so easily flustered? Normally, she's so confident.){/i}"
                mc "{i}(I'll send her a heart.){/i}"
                scene 08_718 with Dissolve(1)
                a "..."
                scene 08_719 with Dissolve(1)
                a "{i}(Idiot!){/i}"
                scene black with Dissolve(1)
                pause 2
                scene 08_720 with Dissolve(1)
                am "I like this happy you."
                a "Heh..."
                am "So, who is the guy? Is he cute?"
                a "Mom... We're not doing that!"
                am "What's his name?"
                a "You'll know soon enough..."
                scene 08_721 with Dissolve(1)
                am "Come on. Tell me! Let's talk boys!"
                a "MOM!"
                a "Haha..."
                scene black with Dissolve(2)
                pause 2
                if Layla_LikeMC == True:
                    scene 08_736 with Dissolve(1)
                    la "There you are."
                    la "I've been looking for you..."
                    la "What are you doing here?"
                    scene 08_737 with Dissolve(1)
                    la "Is this seat taken?"
                    mc "No, go ahead."
                    scene 08_738 with Dissolve(1)
                    la "..."
                    mc "..."
                    scene 08_739 with Dissolve(1)
                    la "I talked to Alexis yesterday after our talk."
                    mc "Yeah, I know. I talked with her just now."
                    la "..."
                    la "I'm sorry about..."
                    scene 08_740 with Dissolve(1)
                    mc "No-no-no. You have nothing to be sorry for."
                    mc "I'm the one who's sorry."
                    mc "I should've said something way sooner. Especially once I knew you were sisters."
                    mc "So much has been happening lately and it never was the right time..."
                    mc "*Sigh* These are all just bad excuses... I'm sorry."
                    scene 08_741 with Dissolve(1)
                    la "You really like her, huh?"
                    mc "Yes, I do."
                    la "..."
                    la "I'm actually not mad about you two seeing each other. It just took me by surprise."
                    la "I would've never guessed."
                    la "But now I finally understand why she has been so happy lately. And thanks to that, we even grew closer the past couple of weeks."
                    scene 08_742 with Dissolve(1)
                    la "There's one more thing I need to say though. I'd regret it if I didn't."
                    la "Since you were honest, I'll be honest too."
                    la "I've never said it out loud, but I like you."
                    mc "I like you too."
                    la "But only as friends, right? So what should we do now?"
                    scene 08_743 with Dissolve(1)
                    mc "You've been my best friend since I moved back, and I hope we can stay that way."
                    mc "I want to hang out with you and have fun, but..."
                    la "No more making out."
                    mc "Heh, yes. You could put it that way."
                    mc "I won't do that to Lexi, anyway."
                    scene 08_744 with Dissolve(1)
                    la "You're also one of my best friends. And I'd rather be friends than..."
                    mc "Yeah."
                    la "Hehe."
                    la "Hugging is still allowed, right?"
                    mc "Yes, it is."
                    scene 08_745 with Dissolve(1)
                    la "How about we start over? Strictly as friends?"
                    mc "Perfect."
                    scene 08_746 with Dissolve(1)
                    mc "Hi. I'm [mc]."
                    la "Hey. Layla. Haha..."
                    el "YOU!"
                    scene 08_747 with Dissolve(1)
                    mc "Aaah..."
                    el "HOW COULD YOU!"
                    scene 08_748 with Dissolve(1)
                    mc "Elena!"
                    scene 08_749 with Dissolve(1)
                    mc "What are you..."
                    el "I SHOULD BEAT..."
                    scene 08_750 with Dissolve(1)
                    la "ELENA STOP!"
                    el "..."
                    el "You're not crying?"
                    la "What? No..."
                    el "..."
                    la "I'll explain."
                    scene black with Dissolve(1)
                    pause 2
                    scene 08_751 with Dissolve(1)
                    el "Dios mío... You two are something else. So confusing!"
                    el "And since it seems that I have no idea about... any of what's been going on lately. You'd better tell me everything from the very beginning."
                    scene 08_752 with Dissolve(1)
                    mc "Alright. I'll tell you."
                    mc "I met Alexis during..."
                    scene black with Dissolve(1)
                    pause 2
                    scene 08_753 with Dissolve(1)
                    el "Wow, that was a lot."
                    el "So you're Alexis's boyfriend?"
                    mc "Eh... We aren't really boyfriend-girlfriend..."
                    el "But you're dating?"
                    mc "Yes."
                    scene 08_754 with Dissolve(1)
                    el "Who would've expected that?"
                    la "Yeah, you tell me."
                    scene 08_755 with Dissolve(1)
                    el "I'm sorry, [mc]. For tackling you and almost slapping you."
                    mc "It's all good, Elena. You're being a good friend and protecting Layla."
                    el "Can I hug you as an apology at least?"
                    mc "That's so unlike you, but sure."
                    scene 08_756 with Dissolve(1)
                    el "You're so sticky and you smell. You need a shower."
                    mc "Haha, that's the Elena I know."
                    el "Haha, I'm sorry."
                    mc "No, you're right. I need a shower and that's what I'll be going to do now."
                    scene 08_757 with Dissolve(1)
                    mc "See you tomorrow, then?"
                    la "Yes. Bye, [mc]."
                    mc "Later. And thank you, Layla!"
                    el "Bye."
                    scene 08_758 with Dissolve(1)
                    el "That was some..."
                    el "Hey, what's wrong?"
                    el "Layla?"
                    el "Come here!"
                    scene 08_759 with Dissolve(1)
                    el "You really liked him, huh?"
                    la "*Nods*"
                    el "It will be alright. And who knows what will happen in the future. Maybe they'll break up."
                    scene 08_760 with Dissolve(1)
                    la "Elena!"
                    el "What? Everything's allowed in love and war."
                    la "Haha..."
                    jump Week3_Thursday_Evening
                else:
                    scene 08_736 with Dissolve(1)
                    la "There you are."
                    la "I've been looking for you..."
                    la "What are you doing here?"
                    scene 08_737 with Dissolve(1)
                    la "Is this seat taken?"
                    mc "No, go ahead."
                    scene 08_738 with Dissolve(1)
                    la "..."
                    mc "..."
                    scene 08_739 with Dissolve(1)
                    la "Is something wrong?"
                    mc "No, don't worry. Just a little tired."
                    scene 08_742 with Dissolve(1)
                    la "I talked to Lexi yesterday."
                    mc "Yeah, I was on the phone with her just now. She told me."
                    mc "You can be really mean."
                    scene 08_746 with Dissolve(1)
                    la "Haha."
                    la "I warned you I'd prank her."
                    la "But it didn't really work, she caught on quickly."
                    scene 08_745 with Dissolve(1)
                    la "Thank you for being so nice to her."
                    la "She sounded so happy."
                    mc "I'm happy too."
                    scene 08_744 with Dissolve(1)
                    if Tori_Week1_Interested == False:
                        la "So from now on. No more flirting. No more fake-boyfriend-kissing."
                        mc "Haha, that's right, that happened."
                    else:
                        la "So from now on. No more flirting."
                    la "Strictly friends!"
                    mc "Agreed."
                    la "Well, maybe a little bit of flirting, because it's fun."
                    mc "Haha."
                    jump Week3_Thursday_Evening
        else:
            if Alexis_Week3_Wednesday_TC_Breakup == True:
                $ Alexis_End = True
                $ Alexis_Friends = True
                $ Alexis_Points -= 4
                stop music fadeout 1.0
                play music "Music/Slow4.mp3" volume 0.5
                scene 08_728 with Dissolve(1)
                mc "Hi."
                a "Hey. How are you?"
                mc "*Sigh*"
                scene 08_729 with Dissolve(1)
                a "What's wrong? Are you okay? Did something happen?"
                mc "..."
                a "[mc]?"
                mc "We need to talk, Alexis."
                a "{i}(Alexis?){/i}"
                a "Uhm. Okay?"
                scene 08_701 with Dissolve(1)
                a "Let's talk."
                mc "I think it would be best to do this face-to-face instead of over the phone."
                a "..."
                a "If you're breaking up with me, I'd rather you do it now and don't let me wait and guess until Sunday!"
                scene 08_726 with Dissolve(1)
                mc "I'm sorry."
                a "..."
                scene 08_723 with Dissolve(1)
                a "I don't understand. Did something happen? What changed since... Since yesterday?"
                mc "It's Layla."
                a "Did you talk to her?"
                a "Did she say something, or..."
                mc "No. I like her."
                if Alexis_Week2_Sunday_Honest == True:
                    scene 08_716 with Dissolve(1)
                    a "..."
                    a "I know you told me that you flirted and kissed before, but... I thought it was in the past."
                    a "So your feelings changed?"
                    mc "No, I still like you, but..."
                    a "But you like Layla more."
                    mc "I'm so sorry, Alexis."
                else:
                    scene 08_722 with Dissolve(1)
                    a "..."
                    a "You like her?"
                    a "I asked you if there was something between Layla and you, and you told me no!"
                    mc "I didn't know at that time."
                    a "That was four days ago..."
                    a "You could've told me the truth about how you feel about Layla instead of suggesting to give us a shot."
                scene 08_730 with Dissolve(1)
                a "Does Layla know about us?"
                mc "Yes, I told her."
                scene 08_731 with Dissolve(1)
                a "..."
                mc "..."
                scene 08_706 with Dissolve(1)
                mc "I don't know what else to say other than sorry..."
                a "..."
                mc "Maybe the words you said to me before. I hope we can be friends?"
                a "..."
                mc "I'll also try to help you fix your relationship with Erynn. So whenever you need me, you can count on me."
                if Alexis_Week2_Sunday_Honest == True:
                    a "..."
                else:
                    a "No... I'll do it myself."
                scene 08_732 with Dissolve(1)
                mc "..."
                a "..."
                scene 08_700 with Dissolve(1)
                mc "Uhm... Goodbye, Alexis."
                a "..."
                scene 08_727 with Dissolve(1)
                mc "{i}(Fuck!){/i}"
                mc "{i}(I'm sorry...){/i}"
                scene 08_733 with Dissolve(1)
                a "*Crying*"
                scene 08_734 with Dissolve(1)
                am "Hey. Everything alright?"
                a "..."
                scene 08_735 with Dissolve(1)
                am "Come here."
                am "Anything I can do?"
                a "No..."
                scene black with Dissolve(1)
                pause 2
                scene 08_736 with Dissolve(1)
                la "There you are."
                la "I've been looking for you..."
                la "What are you doing here?"
                scene 08_737 with Dissolve(1)
                la "Is this seat taken?"
                mc "No, go ahead."
                scene 08_761 with Dissolve(1)
                la "What's wrong? Are you okay?"
                mc "Yeah, I just had to think about some stuff."
                la "About us?"
                mc "In a way."
                scene 08_739 with Dissolve(1)
                mc "I called Alexis earlier and told her that I like you."
                la "What did she say?"
                mc "Not much."
                la "Hmm..."
                scene 08_741 with Dissolve(1)
                mc "..."
                mc "How are you feeling about... everything?"
                la "I'm good. I just needed some time yesterday to think."
                mc "Are we good?"
                scene 08_742 with Dissolve(1)
                la "I need to tell you something."
                la "I've never said it out loud, but I think it's time."
                la "I like you. I really like you, [mc]!"
                scene 08_765 with Dissolve(1)
                mc "I like you too, Layla! A lot!"
                la "I know. You told me yesterday."
                mc "Haha."
                scene 08_763 with Dissolve(1)
                mc "So... Where should we go from here?"
                scene 08_764 with Dissolve(1)
                la "I have an idea."
                scene 08_766 with Dissolve(1)
                ""
                scene 08_769 with Dissolve(1)
                mc "{i}(Oh, a little French...){/i}"
                scene 08_770 with Dissolve(1)
                el "YOU!"
                scene 08_771 with Dissolve(1)
                la "Elena!"
                el "Yes, Elena..."
                scene 08_772 with Dissolve(1)
                el "You asked me to help you look for [mc]."
                el "I've been running around all over the place and here you are... Making out with him."
                el "At least text me that you found him!"
                scene 08_773 with Dissolve(1)
                la "I'm sorry, Elena!"
                la "It completely slipped my mind. I'm really sorry."
                el "Uh-huh. Seems like that wasn't the only thing that slipped."
                scene 08_774 with Dissolve(1)
                la "What? No! We weren't having sex!"
                mc "{i}(Haha, what is she saying...){/i}"
                el "..."
                el "I meant his tongue."
                la "Oh. Haha."
                scene 08_775 with Dissolve(1)
                mc "Hey. Let me intervene real quick."
                mc "She used much more tongue than I did."
                la "..."
                scene 08_776 with Dissolve(1)
                la "I did? Too much? I never..."
                mc "No, it was really good. I liked it."
                scene 08_777 with Dissolve(1)
                el "Dios mío. You guys are something else."
                la "Haha."
                scene black with Dissolve(1)
                pause 2
                scene 08_778 with Dissolve(1)
                mc "Well, I'll leave you girls for a while. I actually need to get out of these clothes and take a shower."
                el "You sure do. I don't understand how you can make out with him, Layla. All sweaty and sticky..."
                if Elena_Points >= 17:
                    scene 08_779 with Dissolve(1)
                    mc "Someone's jealous..."
                    el "Jealous of having a sweaty guy attached to me? I don't think so."
                    scene 08_780 with Dissolve(1)
                    mc "Here, have all my sweaty goodness over you."
                    el "Ew... That isn't just disgusting, it even sounds disgusting!"
                    scene 08_781 with Dissolve(1)
                    el "[mc]!"
                    el "Haha... Stop! Layla, help me!"
                    scene 08_782 with Dissolve(1)
                    el "EW! I hope this washes off!"
                    mc "Haha."
                else:
                    scene 08_779 with Dissolve(1)
                    mc "Someone's jealous..."
                    el "Jealous of having a sweaty guy attached to me? I don't think so."
                scene 08_783 with Dissolve(1)
                mc "Bye, girls."
                el "Yeah. Please leave!"
                mc "Haha."
                la "Bye, [mc]."
                jump Week3_Thursday_Evening
            else:
                $ Alexis_Dating = True
                scene 08_696 with Dissolve(1)
                mc "Hi."
                a "Hey. How are you?"
                mc "Exhausted again. These exercises are so hard."
                a "Are you done for today?"
                mc "Yes. And very happy about that."
                a "Haha."
                scene 08_697 with Dissolve(1)
                mc "What are you doing?"
                a "I'm actually home. Had to do some chores."
                mc "Right, the punishment chores. I'm so sorry."
                a "It's fine. Worth it."
                mc "Haha."
                scene 08_698 with Dissolve(1)
                mc "How long do you have to do them for?"
                a "This week and next."
                a "Mom is very strict about these things."
                mc "Yeah, Layla told me that too, once."
                scene 08_706 with Dissolve(1)
                mc "Anything new with Erynn?"
                a "I haven't spoken to her. She wasn't at school today."
                mc "Hmm, okay..."
                mc "{i}(Maybe I should call her.){/i}"
                scene black with Dissolve(1)
                pause 2
                scene 08_707 with Dissolve(1)
                mc "What are your plans for the rest of the day? Do you have to work?"
                a "No, I'm off today. I'm going to relax a bit and then start working on an assignment for school."
                mc "Sounds like fun. The relaxing part, not the assignment."
                a "Haha."
                a "How about you?"
                scene 08_708 with Dissolve(1)
                mc "First, I need a shower. Badly."
                a "We have a shower!"
                mc "Haha, I'm not running to your house this time."
                a "Aw... And after your shower?"
                mc "Grab something to eat. And if I still have some energy left, I'll see what the others are up to and join them in whatever, I guess."
                am "Why aren't the dishes done?"
                scene 08_709 with Dissolve(1)
                a "Sorry, give me one second."
                mc "Sure."
                scene 08_710 with Dissolve(1)
                a "Hey, Mom. What did you say?"
                am "The dishes... Why aren't they done yet?"
                a "I got a call. I was about to do them..."
                scene 08_711 with Dissolve(1)
                am "Come on. I'll help you. You can call your boyfriend later."
                a "What? My boy... No... I mean... How do..."
                scene 08_712 with Dissolve(1)
                am "Mother's intuition."
                a "..."
                am "You've been my daughter for twenty years. I know when something's up."
                am "Invite him over next time."
                a "Uhm..."
                am "Come on now."
                scene 08_713 with Dissolve(1)
                a "Sorry, I have to go."
                mc "No worries."
                a "Speak to you tomorrow?"
                mc "Yeah, I'll call you."
                scene 08_714 with Dissolve(1)
                a "Okay, thank you for calling today. Bye, [mc]."
                mc "Didn't you forget something?"
                a "Hmm?"
                scene 08_715 with Dissolve(1)
                a "Nooo... You heard that?"
                a "That was just... You know... Aah... I hoped you'd forget."
                mc "That ended quickly."
                scene 08_716 with Dissolve(1)
                a "No, it's not that I don't..."
                a "..."
                a "What am I saying?"
                a "Uhm... Bye."
                scene 08_717 with Dissolve(1)
                mc "{i}(Haha, she hung up.){/i}"
                mc "{i}(Why is she so easily flustered? Normally, she's so confident.){/i}"
                mc "{i}(I'll send her a heart.){/i}"
                scene 08_718 with Dissolve(1)
                a "..."
                scene 08_719 with Dissolve(1)
                a "{i}(Idiot!){/i}"
                scene black with Dissolve(1)
                pause 2
                scene 08_720 with Dissolve(1)
                am "I like this happy you."
                a "Heh..."
                am "So, who is the guy? Is he cute?"
                a "Mom... We're not doing that!"
                am "What's his name?"
                a "You'll know soon enough..."
                scene 08_721 with Dissolve(1)
                am "Come on. Tell me! Let's talk boys!"
                a "MOM!"
                a "Haha..."
                scene black with Dissolve(2)
                pause 2
                scene 08_736 with Dissolve(1)
                la "There you are."
                la "I've been looking for you..."
                la "What are you doing here?"
                scene 08_737 with Dissolve(1)
                la "Is this seat taken?"
                mc "No, go ahead."
                scene 08_761 with Dissolve(1)
                la "What's wrong? Are you okay?"
                mc "Yeah, I just had to think about some stuff."
                la "About us?"
                scene 08_763 with Dissolve(1)
                mc "No, no, we're good."
                mc "I'm happy you're here."
                scene 08_766 with Dissolve(1)
                ""
                scene 08_767 with Dissolve(1)
                mc "What are you doing?"
                la "Continuing where we left off yesterday!"
                mc "Oh... I like that idea."
                scene 08_768 with Dissolve(1)
                ""
                scene 08_769 with Dissolve(1)
                mc "{i}(Oh, a little French...){/i}"
                scene 08_770 with Dissolve(1)
                el "YOU!"
                scene 08_771 with Dissolve(1)
                la "Elena!"
                el "Yes, Elena..."
                scene 08_772 with Dissolve(1)
                el "You asked me to help you look for [mc]."
                el "I've been running around all over the place and here you are... Making out with him."
                el "At least text me that you found him!"
                scene 08_773 with Dissolve(1)
                la "I'm sorry, Elena!"
                la "It completely slipped my mind. I'm really sorry."
                el "Uh-huh. Seems like that wasn't the only thing that slipped."
                scene 08_774 with Dissolve(1)
                la "What? No! We weren't having sex!"
                mc "{i}(Haha, what is she saying...){/i}"
                el "..."
                el "I meant his tongue."
                la "Oh. Haha."
                scene 08_775 with Dissolve(1)
                mc "Hey. Let me intervene real quick."
                mc "She used much more tongue than I did."
                la "..."
                scene 08_776 with Dissolve(1)
                la "I did? Too much? I never..."
                mc "No, it was really good. I liked it."
                scene 08_777 with Dissolve(1)
                el "Dios mío. You guys are something else."
                la "Haha."
                scene black with Dissolve(2)
                pause 2
                scene 08_778 with Dissolve(1)
                mc "Well, I'll leave you girls for a while. I actually need to get out of these clothes and take a shower."
                el "You sure do. I don't understand how you can make out with him, Layla. All sweaty and sticky..."
                if Elena_Points >= 17:
                    scene 08_779 with Dissolve(1)
                    mc "Someone's jealous..."
                    el "Jealous of having a sweaty guy attached to me? I don't think so."
                    scene 08_780 with Dissolve(1)
                    mc "Here, have all my sweaty goodness over you."
                    el "Ew... That isn't just disgusting, it even sounds disgusting!"
                    scene 08_781 with Dissolve(1)
                    el "[mc]!"
                    el "Haha... Stop! Layla, help me!"
                    scene 08_782 with Dissolve(1)
                    el "EW! I hope this washes off!"
                    mc "Haha."
                else:
                    scene 08_779 with Dissolve(1)
                    mc "Someone's jealous..."
                    el "Jealous of having a sweaty guy attached to me? I don't think so."
                scene 08_783 with Dissolve(1)
                mc "Bye, girls."
                el "Yeah. Please leave!"
                mc "Haha."
                la "Bye, [mc]."
                jump Week3_Thursday_Evening
    else:
        if Layla_Dating == True:
            scene black with Dissolve(1)
            pause 2
            scene 08_736 with Dissolve(1)
            la "There you are."
            la "I've been looking for you..."
            la "What are you doing here?"
            scene 08_737 with Dissolve(1)
            la "Is this seat taken?"
            mc "No, go ahead."
            scene 08_761a with Dissolve(1)
            la "What's wrong?"
            mc "Nothing really. Just a little exhausted and wanted to be alone for a while."
            la "Oh. Want me to leave?"
            mc "No. I like that you're here!"
            scene 08_762 with Dissolve(1)
            la "Then I'm staying!"
            la "We're good, right?"
            scene 08_763 with Dissolve(1)
            mc "I'm happy you're here."
            scene 08_764 with Dissolve(1)
            la "I need to tell you something."
            la "I've never said it out loud, but I think it's time."
            la "I like you. I really like you, [mc]!"
            scene 08_765 with Dissolve(1)
            mc "I like you too, Layla! A lot!"
            la "I know."
            mc "Haha."
            scene 08_766 with Dissolve(1)
            ""
            scene 08_769 with Dissolve(1)
            mc "{i}(Oh, a little French...){/i}"
            scene 08_770 with Dissolve(1)
            el "YOU!"
            scene 08_771 with Dissolve(1)
            la "Elena!"
            el "Yes, Elena..."
            scene 08_772 with Dissolve(1)
            el "You asked me to help you look for [mc]."
            el "I've been running around all over the place and here you are... Making out with him."
            el "At least text me that you found him!"
            scene 08_773 with Dissolve(1)
            la "I'm sorry, Elena!"
            la "It completely slipped my mind. I'm really sorry."
            el "Uh-huh. Seems like that wasn't the only thing that slipped."
            scene 08_774 with Dissolve(1)
            la "What? No! We weren't having sex!"
            mc "{i}(Haha, what is she saying...){/i}"
            el "..."
            el "I meant his tongue."
            la "Oh. Haha."
            scene 08_775 with Dissolve(1)
            mc "Hey. Let me intervene real quick."
            mc "She used much more tongue than I did."
            la "..."
            scene 08_776 with Dissolve(1)
            la "I did? Too much? I never..."
            mc "No, it was really good. I liked it."
            scene 08_777 with Dissolve(1)
            el "Dios mío. You guys are something else."
            la "Haha."
            scene black with Dissolve(2)
            pause 2
            scene 08_778 with Dissolve(1)
            mc "Well, I'll leave you girls for a while. I actually need to get out of these clothes and take a shower."
            el "You sure do. I don't understand how you can make out with him, Layla. All sweaty and sticky..."
            if Elena_Points >= 17:
                scene 08_779 with Dissolve(1)
                mc "Someone's jealous..."
                el "Jealous of having a sweaty guy attached to me? I don't think so."
                scene 08_780 with Dissolve(1)
                mc "Here, have all my sweaty goodness over you."
                el "Ew... That isn't just disgusting, it even sounds disgusting!"
                scene 08_781 with Dissolve(1)
                el "[mc]!"
                el "Haha... Stop! Layla, help me!"
                scene 08_782 with Dissolve(1)
                el "EW! I hope this washes off!"
                mc "Haha."
            else:
                scene 08_779 with Dissolve(1)
                mc "Someone's jealous..."
                el "Jealous of having a sweaty guy attached to me? I don't think so."
            scene 08_783 with Dissolve(1)
            mc "Bye, girls."
            el "Yeah. Please leave!"
            mc "Haha."
            la "Bye, [mc]."
        else:
            jump Week3_Thursday_Evening

label Week3_Thursday_Evening:
    scene black with Dissolve(1)
    pause
    stop music fadeout 1.0
    play music ("Music/LoFi Indie 3.mp3", "Music/LoFi Indie 1.mp3", "Music/LoFi Indie 2.mp3") volume 0.2
    scene 08_784 with Dissolve(1)
    z "I can't believe you missed all those chances."
    mg "Look who's talking. You missed a penalty."
    z "It was three-nil already by then, it wouldn't have changed anything."
    mg "We still had fifteen minutes. You never know..."
    z "Dude..."
    scene 08_785 with Dissolve(1)
    mc "Hey! What's going on here?"
    z "We lost, that's what's going on..."
    mc "So you lost a training match, big fucking deal."
    z "No, it was the qualification for Saturday's finale!"
    scene 08_786 with Dissolve(1)
    mc "What?"
    z "Yeah!"
    mc "Why didn't you tell me? I would've watched!"
    z "We lost, nothing much to see."
    mc "Three-nil?"
    z "Four-nil actually..."
    scene 08_787 with Dissolve(1)
    mc "That sucks."
    mc "So, no more competition for you guys?"
    z "We still have the game for third place on Saturday."
    mc "That's something at least, right?"
    z "I guess... Still sucks though."
    scene 08_788 with Dissolve(1)
    z "I'm so discouraged now."
    z "I was hyped up coming here, but now..."
    z "Just because of that stupid game."
    mc "Did you play bad, or was the other team just better?"
    z "They outplayed us."
    scene 08_789 with Dissolve(1)
    z "I want to punch something. Release some anger."
    mc "You can go to the gym and use the punching bag, or punch Darryl, either are good options."
    z "That's a good idea."
    scene 08_790 with Dissolve(1)
    mc "Punching Darryl? Alright, let's go."
    z "What? No! Are you crazy? That dude is huge. I meant the punching bag."
    z "Want to join me?"
    if Valeria_Points >= 7:
        menu:
            "Yes[KoGa3AutoWTChange1]{size=-4}(Zach Week3 Thursday TC Box, Zach Points+2) {/size} {/color}":
                $ Zach_Week3_Thursday_TC_Box = True
                $ Zach_Points += 2
                # Zach (8)
                scene 08_791 with Dissolve(1)
                mc "Yeah, I could also release some aggression."
                z "Awesome."
                jump Week3_Thursday_Zach_Box
            "No":
                scene 08_791a with Dissolve(1)
                mc "I just showered. I'm done for today."
                mc "But don't let me stop you."
                z "No worries. Miguel, you're coming with me, right?"
                mg "Uh... Sure. I'm up for some boxing."
                jump Week3_Thursday_Val
    else:
        $ Zach_Week3_Thursday_TC_Box = True
        $ Zach_Points += 2
        # Zach (8)
        scene 08_791 with Dissolve(1)
        mc "Yeah, I could also release some aggression."
        z "Awesome."
        jump Week3_Thursday_Zach_Box

label Week3_Thursday_Val:
    scene black with Dissolve(1)
    pause
    scene 08_792 with Dissolve(1)
    mc "You did? That's great."
    n "*Knock-knock*"
    mc "Someone's at the door."
    mc "Yeah, come on in."
    scene 08_793 with Dissolve(1)
    va "Oh, I'm sorry, I didn't..."
    mc "It's okay, stay. One second though."
    scene 08_794 with Dissolve(1)
    mc "Yeah, a friend."
    m "I'll leave you to it then. I'm glad you're having fun."
    m "Thanks for calling. I'll see you Sunday, and good luck with the competition."
    mc "Thank you."
    scene 08_795 with Dissolve(1)
    m "Bye, honey. Love you."
    mc "Love you too, bye."
    scene 08_796 with Dissolve(1)
    va "Girlfriend?"
    mc "No. That was my mom."
    va "Oh... Haha. Sorry."
    scene 08_797 with Dissolve(1)
    mc "So, what brings you to my humble... Very humble abode?"
    va "Yeah, this room is really sad. Ours is at least two to three times the size."
    if Layla_Week3_Wednesday_TC_AlexisTalk == False:
        mc "Really? Who made those room assignments again?"
        va "Haha."
    else:
        mc "Layla said the same about their room."
        mc "Who made those room assignments again?"
        va "Haha."
    scene 08_798 with Dissolve(1)
    va "Well, actually no. This one is better than mine, since I can't even get into mine."
    mc "They won't let you in?"
    va "No-no, no one is there and... No key."
    va "I tried Layla's room but they aren't there either."
    scene 08_799 with Dissolve(1)
    va "So I came here."
    va "You said that I could come here and hang out, but... Maybe you just said it to be nice and..."
    mc "No, I meant it. Of course you can hang out here."
    va "Thank you."
    scene 08_800 with Dissolve(1)
    mc "Let me put a t-shirt on real quick."
    va "You don't have to because of me. Well, if you're embarrassed or uncomfortable, go ahead. Otherwise, stay as you are."
    mc "Embarrassed? Do I come across like that?"
    scene 08_801 with Dissolve(1)
    va "No, not really. Seems like you feel pretty good in your skin."
    va "And you're not bad to look at."
    mc "That a compliment?"
    va "Hmm... Sure. Or just an observation."
    mc "Haha."
    scene 08_802 with Dissolve(1)
    mc "You're not bad to look at, either."
    va "Thanks!"
    scene 08_803 with Dissolve(1)
    va "Where are the others?"
    mc "Don't know about Jay, but Zach and Miguel are relieving some anger and stress in the gym."
    va "Oh?"
    mc "They had a qualifying game today for Saturday's finale."
    mc "But they lost pretty bad."
    scene 08_804 with Dissolve(1)
    va "Zach didn't tell me that. I would've liked to watch a game."
    mc "I didn't know either. Most likely Zach didn't either until the game started."
    va "Haha. True."
    scene 08_805 with Dissolve(1)
    mc "How are things between you and Zach? Better?"
    va "Yeah, we talked. I talked!"
    mc "Haha. Good!"
    mc "He did listen though, right?"
    va "He did."
    mc "Just checking."
    scene black with Dissolve(1)
    pause
    scene 08_806 with Dissolve(1)
    va "Want to listen to some music?"
    mc "Yeah, I'd like to know what else you have on your playlist."
    scene 08_807 with Dissolve(1)
    va "Let's see."
    va "Hmm, I think you might like this one. Or maybe this one?"
    if Alexis_Dating == True:
        scene 08_808 with Dissolve(1)
        mc "{i}(This smell...){/i}"
        va "What do you think of Falling Into Jupiter?"
        mc "You smell good."
        scene 08_809 with Dissolve(1)
        va "What? Oh... Haha. I just came out of the shower."
        mc "Raspberry shampoo?"
        va "Uh..."
        va "Yeah, my favourite."
        mc "{i}(Must be popular.){/i}"
        scene 08_810 with Dissolve(1)
        mc "..."
        va "..."
        scene 08_811 with Dissolve(1)
        va "So... What do you think of them?"
        mc "Who?"
        va "Falling Into Jupiter."
        mc "Never heard of them."
        va "No? Same singer from Yellow Snow."
        mc "Really?"
    else:
        scene 08_811 with Dissolve(1)
        va "What do you think of Falling Into Jupiter?"
        mc "Never heard of them."
        va "No?"
    mc "Maybe I know some songs. But the name doesn't ring a bell."
    va "Uh..."
    va "Let's see if you know this song."
    scene 08_812 with Dissolve(1)
    stop music fadeout 1.0
    play music "Music/Falling Into Jupiter - When the Beasts Wake Below.mp3" volume 0.5
    mc "..."
    mc "Yeah. I've heard that one before."
    mc "*Sings* They rise from the dark beneath..."
    va "*Sings* And none who stand will walk back home!"
    scene 08_813 with Dissolve(1)
    mc "Haha..."
    va "Haha."
    if Elena_Week3_Monday_CheerTraining == True:
        va "So you actually know more songs than the 'Elena has a boyfriend' song!"
        mc "Haha. Stuck in your head too?"
        va "Totally! Thanks for that by the way."
        mc "I said it's catchy."
    else:
        va "You're pretty good. You should've sung on the bus when Layla asked you."
        mc "I wasn't going to sing there in front of everyone."
    scene black with Dissolve(1)
    pause 2
    stop music fadeout 1.0
    play music ("Music/LoFi Indie 3.mp3", "Music/LoFi Indie 1.mp3", "Music/LoFi Indie 2.mp3") volume 0.2
    scene 08_814 with Dissolve(1)
    mc "Heh... Tired?"
    va "Sorry. A bit."
    mc "That happens when you wake up at six to do some extra training before the actual training!"
    va "Hehe."
    mc "Just lie down."
    scene 08_815 with Dissolve(1)
    va "You don't mind? I'm already invading your space, I don't want to take it all."
    mc "Well then, in exchange. Can I keep listening to your music?"
    if Valeria_Week3_Wednesday_Pictures == True:
        va "Uhm..."
        mc "I won't look at your pictures. I promise."
        va "Okay then."
    else:
        va "Deal."
    scene 08_816 with Dissolve(1)
    mc "Mind if I use your headphones as well?"
    va "No, no. Let me get them for you. One sec."
    scene 08_817 with Dissolve(1)
    mc "Thank you."
    va "I'm just going to rest a bit. If I fall asleep, please wake me up later."
    mc "Will do."
    scene 08_818 with Dissolve(1)
    ""
    scene 08_819 with Dissolve(1)
    ""
    scene black with Dissolve(1)
    pause 2
    scene 08_820 with Dissolve(1)
    mc "{i}(It hasn't even been five minutes and she's asleep.){/i}"
    mc "{i}(I couldn't sleep at all the first night and she's out like nothing.){/i}"
    mc "{i}(I wish I could do that.){/i}"
    scene 08_821 with Dissolve(1)
    mc "{i}(Cutie...){/i}"
    scene black with Dissolve(2)
    pause 2
    scene 08_822 with Dissolve(1)
    z "That was so good. You should've joined me."
    mc "Shhh!"
    z "What?"
    scene 08_823 with Dissolve(1)
    z "Oh... Who's that?"
    z "..."
    z "Valeria? What is she doing here?"
    scene 08_824 with Dissolve(1)
    mc "She couldn't get into her room, so she asked if she could stay here."
    z "She's going to sleep here?"
    mc "No. She's just waiting a while until Tori is back."
    scene 08_825 with Dissolve(1)
    z "How long has she been sleeping here?"
    mc "Close to an hour now, I think. I'm gonna wake her soon, so she can go back."
    z "Just let her stay here and switch beds with me!"
    mc "She can get in trouble for that. But you can always ask her."
    scene 08_826 with Dissolve(1)
    z "Give me a sec before you wake her."
    z "Just look at that ass..."
    mc "Don't be a creep!"
    z "You need to help me with her."
    mc "..."
    scene 08_827 with Dissolve(1)
    mc "We're all going to the pool tomorrow afternoon. Spend some time with her there."
    mc "Have fun, get to know her and maybe have some one-on-one later."
    z "Valeria in a bikini... Just thinking about it... Fuck..."
    z "But yes, that's what I'm going to do. Thanks."
    scene black with Dissolve(2)
    pause 2
    scene 08_828 with Dissolve(1)
    mc "Hey, Val. Val?"
    mc "You need to wake up now."
    scene 08_829 with Dissolve(1)
    va "*Yawn*"
    mc "Good morning, sunshine!"
    scene 08_830 with Dissolve(1)
    va "What? Morning?"
    va "Did I sleep here the whole night?"
    mc "Haha. No, I'm kidding."
    scene 08_831 with Dissolve(1)
    va "[mc]!"
    mc "Sorry, sorry. I just had to. Haha."
    scene 08_831a with Dissolve(1)
    va "You scared me for a second."
    va "Feel how fast my heart is beating."
    mc "Uh..."
    mc "{i}(I think mine is beating faster...){/i}"
    scene 08_831b with Dissolve(1)
    va "So what time is it, actually?"
    mc "Quarter past nine."
    va "Oh wow. I slept for over two hours..."
    mc "Yeah."
    scene 08_832 with Dissolve(1)
    mc "I'm kinda jealous you can fall asleep that easily."
    va "Normally I can't, but somehow I felt comfortable around you."
    mc "..."
    scene 08_833 with Dissolve(1)
    va "The others still not back?"
    mc "They were here some time ago. All sitting around you and watching you sleep."
    scene 08_834 with Dissolve(1)
    va "That's creepy!"
    mc "Haha."
    va "..."
    va "You're joking, right?"
    mc "I am."
    mc "{i}(Except for Zach...){/i}"
    scene 08_835 with Dissolve(1)
    mc "I've put your phone and headphones in your bag."
    mc "Your phone needs to be charged though, it's like twelve percent."
    va "Thank you. And thank you for letting me wait here."
    mc "You're welcome."
    scene 08_836 with Dissolve(1)
    va "I'd better head back before Tori files a missing persons report."
    mc "You think she would do that?"
    va "Hmm... Unlikely."
    mc "Haha."
    scene 08_837 with Dissolve(1)
    va "Thank you, [mc]!"
    mc "Uh..."
    scene 08_837a with Dissolve(1)
    va "See you tomorrow."
    mc "Bye, Val."
    jump Week3_Friday

label Week3_Thursday_Zach_Box:
    scene black with Dissolve(1)
    pause 2
    stop music fadeout 1.0
    play music ("Music/LoFi Indie 3.mp3", "Music/LoFi Indie 1.mp3", "Music/LoFi Indie 2.mp3") volume 0.2
    scene 08_838 with Dissolve(1)
    z "Fuck!"
    z "I hate that we lost. I thought we might do better than last year, but again, we had no chance against them."
    z "We'll get them next year, for sure!"
    mc "..."
    scene 08_839 with Dissolve(1)
    mc "So, you're planning not to go to college?"
    z "You're right. This was my last chance!"
    z "Damn, that pisses me off even more."
    scene 08_840 with Dissolve(1)
    mc "Make sure you win on Saturday, though."
    z "Oh, we will. We won't let those fuckers from Palm City beat us. After today, everyone is fired up."
    mc "What time is the game?"
    z "Kick-off is at ten."
    mc "Hmm... That sucks. My race is at ten thirty, so I can't watch. Again."
    scene 08_841 with Dissolve(1)
    z "Man. I can't watch yours either, then. This schedule is stupid."
    z "Why couldn't they put basketball or volleyball or something else at those times..."
    z "*Sigh*"
    z "When do the girls race?"
    mc "Nine thirty."
    z "At least we can watch them."
    scene 08_842 with Dissolve(1)
    mc "Yeah. I'm excited to see them."
    z "You and me both."
    z "How's your training going?"
    mc "Pretty good so far. But I have no idea about the competition yet."
    mc "So for now, I only have to worry about Darryl."
    scene 08_843 with Dissolve(1)
    z "Can you beat him?"
    mc "I don't know, to be honest. He's fast."
    mc "I beat him the first time we raced, but since then he's had my number."
    mc "It will be close though, that's for sure."
    z "Let's switch."
    scene 08_844 with Dissolve(1)
    z "Man... I want to watch that race just to see Darryl's face when he loses."
    z "Is there something we can do to mess with him?"
    mc "No, I'm not gonna do that. I want to race him fairly."
    mc "If he's faster, so be it."
    scene 08_845 with Dissolve(1)
    z "By the way. I've been looking at some cars the past week."
    mc "You're getting a car?"
    z "Yeah. I've saved up enough and I want to get it before spring break."
    mc "That's awesome."
    scene 08_846 with Dissolve(1)
    mc "Found something interesting yet?"
    z "Yeah, there's this charger that caught my eye. I'm gonna go look at it again next week and decide then."
    z "If you have time, you can join me."
    mc "Sure thing, just let me know when."
    scene 08_847 with Dissolve(1)
    z "I will. Maybe you'll find something too."
    mc "I might, but I can't afford it at this point. I need to work some extra shifts at the restaurant first."
    mc "And by 'some extra shifts', I mean a lot. I don't have anything saved up at this point."
    z "Haha."
    scene 08_848 with Dissolve(1)
    z "Where are you spending your money then?"
    mc "Well, the last big purchase I made was on my tattoos. They weren't cheap."
    z "Heard they could be expensive. Especially big ones like you have."
    mc "I got a really good price, but they were still expensive."
    scene 08_849 with Dissolve(1)
    z "I was thinking about getting a tattoo, but I'm not sure."
    z "What do you think?"
    mc "It's totally up to you. I can't help you with that."
    mc "But in my opinion, if you aren't sure, you shouldn't get one."
    mc "Give it some more thought, first. What would you get? Placement, colours, size and so on."
    mc "And don't forget. Once you get one, you'll most likely have it for the rest of your life."
    scene 08_850 with Dissolve(1)
    z "I'll think about it some more, then."
    z "Thanks."
    mc "Any time."
    scene black with Dissolve(1)
    pause 2
    scene 08_851 with Dissolve(1)
    z "That was very tiring, but exactly what I needed."
    mc "Same. I'm feeling pretty good right now."
    scene 08_852 with Dissolve(1)
    z "Except for my knuckles. They hurt!"
    mc "Haha. Maybe we should've used the gloves."
    z "Definitely."
    scene 08_853 with Dissolve(1)
    mc "Do you have plans already for spring break?"
    z "We're going on a skiing trip to the mountains with the whole family, like every year."
    mc "That'll be fun."
    z "It's alright, but when you do it every year, it's... Well, not that special anymore."
    scene 08_854 with Dissolve(1)
    mc "So, you won't be here at all?"
    z "Only the last weekend. We'll need to do something then with everyone."
    mc "Especially since you'll have your car."
    z "Exactly!"
    scene 08_855 with Dissolve(1)
    z "What about you?"
    mc "I'll probably go to the beach with a few people from school. Nothing else planned at this point though."
    mc "Maybe help Mom out at the restaurant. Will be busy enough with all the tourists."
    z "Not going to visit your dad?"
    mc "Eh... No. That's not going to happen."
    z "..."
    mc "Long story. I'll tell you another time."
    jump Week3_Friday

label Week3_Friday:
    scene black with Dissolve(2)
    pause 2
    stop music fadeout 1.0
    play music ("Music/LoFi Upbeat 1.mp3", "Music/LoFi Upbeat 2.mp3", "Music/LoFi Upbeat 3.mp3", "Music/LoFi Upbeat 4.mp3") volume 0.2
    scene 08_856 with Dissolve(1)
    tm "That was our last training session before tomorrow's competition."
    tm "Thank you all very much for your hard work these last few days. You all trained very hard with... Well, close to no complaints."
    n "Haha."
    scene 08_857 with Dissolve(1)
    tm "I'm very happy with the progress we made all year and I'm sure it will show tomorrow."
    tm "A little heads-up."
    tm "There will be spectators. Don't let it distract you."
    scene 08_858 with Dissolve(1)
    tm "Anyway, I'll see you all tomorrow morning at eight for warm-ups. Keep in mind, that will be at the main track, not this one."
    tm "That's it from me for today. Enjoy your free afternoon. Have fun, relax, but try to keep it in check."
    tm "Darryl, [mc]. Please stay for a minute."
    scene 08_859 with Dissolve(1)
    tm "Listen. You guys need to get it together. You're my best runners and have the best chance of winning tomorrow."
    tm "So instead of the constant bickering like an old married couple..."
    mc "..."
    tm "Work together, help each other out! You'll only benefit from it."
    tm "Okay? Now, get out of here."
    scene black with Dissolve(1)
    pause 2
    scene 08_860 with Dissolve(1)
    la "Hey there, bad boy."
    mc "Yeah... That sounds so much like me..."
    scene 08_861 with Dissolve(1)
    la "No, what was his name again?"
    va "Brave Sir [mc]?"
    la "Right. Brave Sir [mc]. Haha."
    scene 08_862 with Dissolve(1)
    mc "I should've never said that."
    va "I'm so sorry. It was just so funny."
    la "Haha."
    scene 08_863 with Dissolve(1)
    la "What did Coach want from you guys?"
    mc "He said since we have such a shitty girls' team that all hope lies on Darryl and me."
    la "Ha-ha... Shitty girls' team?"
    scene 08_864 with Dissolve(1)
    la "How about a little wager then?"
    mc "Sure. What do you have in mind?"
    la "One second."
    scene 08_865 with Dissolve(1)
    mc "..."
    mc "{i}(Layla whispering in Val's ear is actually pretty hot...){/i}"
    scene 08_866 with Dissolve(1)
    la "Are you okay with that?"
    va "Mmm-hmm."
    scene 08_867 with Dissolve(1)
    la "Best average placement of the top three girls versus boys from our school."
    la "Loser has to run a lap, completely naked!"
    mc "Oh... Naked?"
    la "Uh-huh."
    scene 08_868 with Dissolve(1)
    mc "If the boys win, you're both running? Naked?"
    la "Yes!"
    mc "You must be confident."
    mc "{i}(Why are they so confident? Am I missing something?){/i}"
    mc "{i}(They wouldn't do this if they weren't sure of winning...){/i}"
    scene 08_869 with Dissolve(1)
    la "Are you in, or not?"
    mc "Hmm..."
    menu:
        "Yes[KoGa3AutoWTChange1]{size=-4}(Layla Week3 Friday TC Wager) {/size} {/color}":
            $ Layla_Week3_Friday_TC_Wager = True
            scene 08_870 with Dissolve(1)
            mc "Yeah, let's do it."
            la "Great. Good luck!"
            mc "{i}(Why do I have a bad feeling about this?){/i}"
        "No":
            scene 08_870 with Dissolve(1)
            mc "No, something's fishy. It's probably all planned already."
            la "Haha. Are you scared, brave Sir [mc]?"
            mc "*Sigh* ..."
    scene 08_871 with Dissolve(1)
    la "Come on, Val. Let's go eat something."
    la "*Sings* Brave Sir [mc] ran away."
    va "*Sings* Bravely ran away, away."
    mc "{i}(That's funny...){/i}"
    mc "{i}(And since when did they become such good friends?){/i}"
    scene 08_872 with Dissolve(1)
    mc "{i}(Can't wait to see them in bikini's later.){/i}"
    mc "{i}(Oh yeah...){/i}"
    mc "Hey, we're still going to the pool, right?"
    la "Yes, we are."
    scene 08_873 with Dissolve(1)
    la "Meet there at two?"
    mc "Perfect."
    jump Week3_Friday_Pool

label Week3_Friday_Pool:
    scene black with Dissolve(1)
    pause 2
    scene 08_874 with Dissolve(1)
    z "Seems like others had the same idea."
    mc "It's a nice day. I think everyone just wants to relax after exercising for two days straight."
    mc "Let's take these chairs right here."
    scene 08_875 with Dissolve(1)
    mc "This is what school should be like every day."
    z "Haha. Agreed. The only thing missing is a cold beer or a cocktail."
    mc "I wouldn't risk that. I saw some teachers patrolling already. They might suspect that."
    z "True."
    scene 08_876 with Dissolve(1)
    z "When did the girls say they'd come?"
    mc "Around two. So, any minute now."
    z "Do you know who's coming?"
    mc "Hmm... Layla and Valeria for sure. Don't know about others."
    z "Can't wait to see them in their bikinis. This is going to be so great!"
    scene black with Dissolve(1)
    pause 2
    scene 08_877 with Dissolve(1)
    la "Hey there."
    mc "Hi."
    z "..."
    la "Can we join you guys?"
    mc "Of course."
    scene 08_878 with Dissolve(1)
    mc "This looks like a scene from that one show..."
    z "Baywatch!"
    mc "Yes! If only they would walk in slow motion."
    z "You're reading my thoughts... Fuck they are hot. I'll probably have to spend most of the time in the pool."
    menu:
        "Layla[KoGa3AutoWTChange1]{size=-4}(TC Pool Layla) {/size} {/color}":
            $ TC_Pool_Layla = True
            scene black with Dissolve(1)
            transform moveup:
                xalign 0.5 yalign 1.0
                linear 5.0 yalign 0.0
            show 08_879_layla at moveup
            pause 3
            "..."
        "Elena[KoGa3AutoWTChange1]{size=-4}(TC Pool Elena) {/size} {/color}":
            $ TC_Pool_Elena = True
            scene black with Dissolve(1)
            transform moveup:
                xalign 0.5 yalign 1.0
                linear 5.0 yalign 0.0
            show 08_879_elena at moveup
            pause 3
            "..."
        "Sienna[KoGa3AutoWTChange1]{size=-4}(TC Pool Sienna) {/size} {/color}":
            $ TC_Pool_Sienna = True
            scene black with Dissolve(1)
            transform moveup:
                xalign 0.5 yalign 1.0
                linear 5.0 yalign 0.0
            show 08_879_sienna at moveup
            pause 3
            "..."
        "Valeria[KoGa3AutoWTChange1]{size=-4}(TC Pool Valeria) {/size} {/color}":
            $ TC_Pool_Valeria = True
            scene black with Dissolve(1)
            transform moveup:
                xalign 0.5 yalign 1.0
                linear 5.0 yalign 0.0
            show 08_879_val at moveup
            pause 3
            "..."
    scene 08_880 with Dissolve(1)
    mc "We didn't know how many of you were coming. We only got three chairs. The rest were reserved for some reason."
    la "It's fine, we can share one. I also brought a blanket. Besides, if it stays this hot, we'll spend more time in the pool than sitting here."
    scene 08_881 with Dissolve(1)
    mc "Here. Take this chair, Layla."
    la "Don't worry."
    mc "No, no, just take it."
    la "Okay then. Thank you, [mc]."
    la "Want the blanket?"
    mc "Sure, I'll take that."
    scene 08_882 with Dissolve(1)
    la "There you go."
    mc "Thanks."
    mc "Look at all this space... Just for me. This is great. Best trade ever."
    la "Haha."
    if Layla_Dating == True:
        scene 08_883 with Dissolve(1)
        la "Maybe I should just lie here, too."
        mc "What are you doing?"
        la "This is much more comfortable!"
        scene 08_884 with Dissolve(1)
        mc "Nuh-uh. This is private property now, missy!"
        mc "Shoo, shoo."
        la "Uh... So mean."
    else:
        scene 08_883a with Dissolve(1)
        la "Maybe I should just lie here, too."
        mc "What are you doing?"
        mc "Nuh-uh. This is private property now, missy!"
        mc "Shoo, shoo."
        la "So mean..."
    scene 08_885 with Dissolve(1)
    z "Hey Layla, can you switch places with Valeria?"
    la "..."
    la "Am I allowed to sit anywhere?"
    z "No, I..."
    scene 08_886 with Dissolve(1)
    la "No? Wow... You hear that?"
    z "That's not what I meant!"
    la "Remember what I told you on the bus?"
    z "..."
    z "Oh!"
    scene 08_887 with Dissolve(1)
    z "Valeria, would you like to switch places with Layla?"
    mc "{i}(Look at that. He's learning.){/i}"
    va "Uhm, I don't mind, if you're okay with it, Layla."
    la "Let's switch."
    z "Thank you, Layla."
    la "Uh-huh."
    scene 08_888 with Dissolve(1)
    el "Take this seat. I'll scoot over."
    la "Hehe."
    scene 08_889 with Dissolve(1)
    mc "Are we done switching now? This is more stressful than the training..."
    el "Sienna wants to, maybe?"
    la "Haha."
    si "No, no, I'm good."
    scene black with Dissolve(1)
    pause 2
    scene 08_890 with Dissolve(1)
    mc "Elena, how are you and the squad doing?"
    el "I'm good. The squad is doing fine. But you would've known that if you came to watch us as you said you would."
    mc "Can't really leave my training to go check you guys out, though."
    scene 08_891 with Dissolve(1)
    el "You could've come after training."
    mc "Have you seen our training? It was exhausting."
    el "Excuses, excuses... Miguel came to watch us!"
    mc "{i}(He came for a different reason.){/i}"
    el "You'd better come to watch us at the competition, or I'll be mad."
    mc "I'll make sure of it."
    scene 08_892 with Dissolve(1)
    la "*Sigh*"
    la "And here I was hoping we could spend half a day without her being around..."
    la "There's so much to do. Why does she have to pick the pool?"
    mc "Who?"
    la "There, have a look!"
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 08_893 at moveup
    pause 3
    "..."
    scene 08_894 with Dissolve(1)
    to "Do you have to lie in the middle of everything?"
    mc "What? There's plenty of space."
    scene 08_895 with Dissolve(1)
    to "Move!"
    mc "Ask nicely!"
    to "MOVE!"
    menu:
        "Move":
            scene 08_896 with Dissolve(1)
            mc "There you go, princess..."
            to "About time, peasant."
            z "What a bitch!"
        "Stay[KoGa3AutoWTChange1]{size=-4}(Tori Week3 Friday TC Step, Tori Points+2) {/size} {/color}":
            $ Tori_Week3_Friday_TC_Step = True
            $ Tori_Points += 2
            # Tori (10)
            mc "Not moving. Just go around, Tori..."
            to "..."
            scene 08_898 with Dissolve(1)
            mc "{i}(What is she...){/i}"
            scene 08_897 with Dissolve(1)
            mc "Really now?"
            z "What a bitch!"
    scene 08_899 with Dissolve(1)
    to "You said something, ginger?"
    z "..."
    to "That's what I thought."
    to "See what I mean, Val?"
    to "If you're getting bored. Come hang out with us. You're better than these..."
    scene 08_900 with Dissolve(1)
    el "That's enough, Victoria!"
    to "It's Tori!"
    el "Jazz, please?"
    jz "Yeah. Come on, Tori. Let's find us some chairs."
    scene 08_901 with Dissolve(1)
    el "..."
    to "..."
    menu:
        "Check them out[KoGa3AutoWTChange1]{size=-4}(Elena Points-2, Tori Points+2) {/size} {/color}":
            $ Elena_Points -= 2
            $ Tori_Points += 2
            # Tori (12)
            scene 08_902 with Dissolve(1)
            mc "{i}(Shame those don't reflect personality. They look great!){/i}"
        "High-five":
            scene 08_903 with Dissolve(1)
            mc "You are badass, Elena!"
            el "Thanks."
    scene 08_904 with Dissolve(1)
    mc "Victoria, huh? Didn't know that."
    la "Neither did I."
    el "Not many do. She absolutely hates it."
    scene 08_905 with Dissolve(1)
    mc "Is Elena short for something?"
    el "..."
    el "Yes! It's short for 'eres un idiota'."
    la "Haha."
    scene 08_906 with Dissolve(1)
    mc "Por qué te ríes?\n(Why are you laughing?)"
    la "Qué?"
    mc "Exactamente!"
    scene 08_907 with Dissolve(1)
    la "Hey! There will be a day when I speak perfect Spanish and I'll understand everything you guys say."
    la "No more making fun of me then!"
    mc "Sí... Claro!"
    la "Ugh..."
    el "Haha."
    scene 08_908 with Dissolve(1)
    la "Besides. I'm not the only one here who doesn't speak Spanish."
    la "Zach can't speak it either!"
    scene 08_909 with Dissolve(1)
    z "Of course I speak Spanish."
    z "Dónde está la biblioteca?"
    va "Haha."
    la "What? How? You didn't take Spanish."
    mc "{i}(Layla, you're so cute...){/i}"
    scene 08_910 with Dissolve(1)
    la "*Sigh* It's so unfair."
    mc "Want me to teach you some more?"
    la "Maybe... Does your mom speak Spanish?"
    scene 08_911 with Dissolve(1)
    mc "She does. French too."
    la "Oh wow. She learned French at school?"
    mc "She took some French courses when she attended culinary school."
    scene 08_912 with Dissolve(1)
    z "You look nice, Val!"
    va "Thank you."
    z "The bikini is very cute."
    va "Thanks."
    scene 08_913 with Dissolve(1)
    z "How has training been?"
    va "Fun and exciting. Can't wait for tomorrow's competition."
    z "Good. I'll be watching and cheering for you!"
    scene 08_912a with Dissolve(1)
    la "Don't you dare! I know what you want to do!"
    mc "I'm not scared of you."
    scene 08_914 with Dissolve(1)
    z "Will you come to watch me?"
    va "Uh... It's at the same time as the 100m race for the boys, right?"
    z "Yeah, sucks. But I'm pretty sure we'll win if you come to watch!"
    scene 08_915 with Dissolve(1)
    la "Haha, stop. Stop! I'm falling."
    va "..."
    scene 08_916 with Dissolve(1)
    la "[mc]... [mc]!"
    la "Aaah... Elena, help!"
    if Layla_Dating == True:
        scene 08_916a with Dissolve(1)
        mc "{i}(Oh... Her nipple.){/i}"
        scene 08_917 with Dissolve(1)
        va "I want to support my team, but I'll rush to your game once the race is over."
        z "That's okay. You can watch the second half."
        z "I'll score a goal for you. Maybe even two."
        scene 08_918 with Dissolve(1)
        la "Did you see?"
        mc "No... What are you talking about?"
        scene 08_919 with Dissolve(1)
        la "You did!"
        mc "Haha."
    else:
        scene 08_917 with Dissolve(1)
        va "I want to support my team, but I'll rush to your game once the race is over."
        z "That's okay. You can watch the second half."
        z "I'll score a goal for you. Maybe even two."
    scene 08_920 with Dissolve(1)
    ""
    scene 08_921 with Dissolve(1)
    ""
    scene 08_922 with Dissolve(1)
    ""
    scene 08_923 with Dissolve(1)
    z "{i}(Fuck!){/i}"
    z "{i}(What should I do?){/i}"
    scene 08_924 with Dissolve(1)
    z "CANNONBAAAAALL!"
    la "Haha, what is he doing?"
    mc "No idea. Probably stung by something."
    scene black with Dissolve(1)
    pause 2
    scene 08_925 with Dissolve(1)
    z "This is so refreshing."
    z "[mc]. Get in here!"
    scene 08_926 with Dissolve(1)
    mc "I'm good for now."
    z "Come on! I feel stupid being in here on my own."
    mc "You can always come out again."
    z "Dude..."
    mc "What?"
    z "Dude!"
    scene 08_927 with Dissolve(1)
    mc "Oh... Haha. Okay, okay."
    la "I don't get it. What's going on?"
    mc "Nothing."
    la "Tell me!"
    mc "Later."
    z "No! Don't!"
    scene black with Dissolve(1)
    pause 2
    scene 08_928 with Dissolve(1)
    mc "Cooling off alright?"
    z "Haha, you have no idea."
    z "I was looking at her while she was readjusting her bikini top and... Fuck man..."
    z "She's so hot."
    scene 08_929 with Dissolve(1)
    z "Look at her, being all seductive."
    mc "{i}(She's just sunbathing...){/i}"
    z "Amazing, right?"
    scene 08_930 with Dissolve(1)
    z "*Sigh*"
    mc "What now?"
    z "I have a question."
    mc "Okay. Shoot."
    scene 08_931 with Dissolve(1)
    z "Promise me you'll answer honestly."
    mc "Of course. Always."
    z "What are my chances with Valeria?"
    menu:
        "Friend-zone":
            scene 08_932 with Dissolve(1)
            mc "Hmm... I think she only sees you as a friend."
            z "Meaning I'm friend-zoned?"
            mc "Yeah, more or less."
            z "Should I just give up, or do you think I can get out of there?"
            mc "There's always a possibility. Feelings change, right?"
        "Good chances":
            scene 08_933 with Dissolve(1)
            mc "She wouldn't spend so much time with you if she didn't like you."
            mc "So, I think your chances are pretty good."
            z "Yeah?"
    scene 08_934 with Dissolve(1)
    z "Does she know that I like her?"
    mc "She knows."
    z "You sure? Hmm... Maybe I should kiss her and go from there? See how she reacts?"
    mc "Not out of nowhere though. Don't just go towards her and start kissing her."
    z "I'll wait for the perfect moment."
    mc "No. There's no such thing. I can't really explain it. You... You just know. You feel it."
    z "In other words, the perfect moment!"
    mc "..."
    scene 08_935 with Dissolve(1)
    mc "Just make sure your lip ring doesn't get stuck in her nose ring. Like, aaah..."
    z "Haha. That would look very weird."
    mc "Haha."
    scene 08_936 with Dissolve(1)
    la "What's so funny?"
    mc "Layla! That scared me!"
    la "Oh... Something inappropriate then."
    mc "Are you filming us?"
    la "No! Maybe... Yes. Haha."
    scene 08_937 with Dissolve(1)
    mc "What's up?"
    la "Can you take some pictures of us?"
    mc "Sure, are you coming in the pool, or?"
    la "I meant of us girls."
    mc "Oh, okay..."
    la "Thanks. I'll get them."
    scene 08_938 with Dissolve(1)
    z "This is the perfect opportunity."
    mc "For what?"
    z "Rate them. Up for it?"
    mc "Rate the girls? Go ahead."
    scene 08_939 with Dissolve(1)
    z "Are they discussing something?"
    mc "Probably how to pose."
    mc "Come on girls. We can take multiple pictures..."
    scene 08_940 with Dissolve(1)
    z "You go first. Best boobs."
    mc "Best boobs?"
    z "Yup."
    scene 08_941 with Dissolve(1)
    mc "They're all great for starters."
    if Zach_Week3_Wednesday_TC_Girlshower == True:
        if Tori_Week3_Wednesday_TC_Fun == True:
            scene 08_942 with Dissolve(1)
            mc "{i}(They are amazing too.){/i}"
            mc "I pick..."
            menu:
                "Layla":
                    scene 08_943_layla with Dissolve(1)
                    mc "Layla, no competition. Hers are just... Yum."
                    z "Yum? That's a good word for it."
                    z "Mine is a toss-up between Layla and Valeria."
                    z "But I think Layla edges slightly ahead. So, I agree with you on Layla. Yum!"
                "Elena":
                    scene 08_943_elena with Dissolve(1)
                    mc "Elena."
                    mc "They're just the perfect size for her body."
                    z "Hmm. They aren't bad but I think the others look better."
                    z "Mine is a toss-up between Layla and Valeria."
                    z "But I think Layla edges slightly ahead."
                "Valeria":
                    scene 08_943_val with Dissolve(1)
                    mc "Don't get mad at me, but it's Valeria."
                    mc "Before today I would've said Layla, but seeing Val in her bikini... Sorry, Zach."
                    z "Haha, no worries. They look amazing."
                    z "For me, it's the other way around. It is a toss-up between Layla and Valeria."
                    z "But Layla edges slightly ahead."
                "Sienna":
                    scene 08_943_sienna with Dissolve(1)
                    mc "Sienna."
                    z "Really?"
                    mc "Yeah. I prefer smaller boobs. Along with her pale skin... So pretty."
                    z "They look nice, but mine is a toss-up between Layla and Valeria."
                    z "But I think Layla edges slightly ahead."
                "Tori":
                    scene 08_943_tori with Dissolve(1)
                    mc "Uh... Well... It's Tori."
                    z "What?"
                    mc "Yeah."
                    z "Tori? What the hell... She isn't bad looking, I'll give you that. But just her reputation alone..."
                    if Tori_Week3_Friday_TC_Step == True:
                        mc "I know, but somehow, I don't know what exactly it is, she turns me on."
                        mc "Even when she was stepping on me before. I thought it was hot."
                        z "There is something majorly wrong with you, dude!"
                        mc "Haha."
                    else:
                        mc "I know, but somehow, I don't know what exactly it is, she turns me on."
                        z "There is something majorly wrong with you, dude!"
                        mc "Haha."
                "Jasmine":
                    scene 08_943_jasmine with Dissolve(1)
                    mc "Actually, it's Jasmine's."
                    z "Would've never guessed that."
                    mc "I saw hers when we were at the girl's showers, and then earlier in her bikini... Just damn."
                    z "They are huge, right? Do you think they're natural?"
                    mc "I don't know. I'd need to touch them first. Maybe a little taste too."
                    z "Haha."
                    mc "But if they are... She's won the lottery."
                    z "True. My pick is Layla."
        else:
            scene 08_942 with Dissolve(1)
            mc "{i}(They're amazing too.){/i}"
            mc "I pick..."
            menu:
                "Layla":
                    scene 08_943_layla with Dissolve(1)
                    mc "Layla, no competition. Hers are just... Yum."
                    z "Yum? That's a good word for it."
                    z "Mine is a toss-up between Layla and Valeria."
                    z "But I think Layla edges slightly ahead. So, I agree with you on Layla. Yum!"
                "Elena":
                    scene 08_943_elena with Dissolve(1)
                    mc "Elena."
                    mc "They're just the perfect size for her body."
                    z "Hmm. They aren't bad but I think the others look better."
                    z "Mine is a toss-up between Layla and Valeria."
                    z "But I think Layla edges slightly ahead."
                "Valeria":
                    scene 08_943_val with Dissolve(1)
                    mc "Don't get mad at me, but it's Valeria."
                    mc "Before today I would've said Layla, but seeing Val in her bikini... Sorry, Zach."
                    z "Haha, no worries. They look amazing."
                    z "For me, it's the other way around. It is a toss-up between Layla and Valeria."
                    z "But Layla edges slightly ahead."
                "Sienna":
                    scene 08_943_sienna with Dissolve(1)
                    mc "Sienna."
                    z "Really?"
                    mc "Yeah. I prefer smaller boobs. Along with her pale skin... So pretty."
                    z "They look nice, but mine is a toss-up between Layla and Valeria."
                    z "But I think Layla edges slightly ahead."
                "Jasmine":
                    scene 08_943_jasmine with Dissolve(1)
                    mc "Actually, it's Jasmine's."
                    z "Would've never guessed that."
                    mc "I saw hers when we were at the girl's showers and then earlier in her bikini... Just damn."
                    z "They are huge, right? Do you think they're natural?"
                    mc "I don't know. I'd need to touch them first. Maybe a little taste too."
                    z "Haha."
                    mc "But if they are... She's won the lottery."
                    z "True. My pick is Layla."
    else:
        if Tori_Week3_Wednesday_TC_Fun == True:
            scene 08_942 with Dissolve(1)
            mc "{i}(They're amazing too.){/i}"
            mc "I pick..."
            menu:
                "Layla":
                    scene 08_943_layla with Dissolve(1)
                    mc "Layla, no competition. Hers are just... Yum."
                    z "Yum? That's a good word for it."
                    z "Mine is a toss-up between Layla and Valeria."
                    z "But I think Layla edges slightly ahead. So, I agree with you on Layla. Yum!"
                "Elena":
                    scene 08_943_elena with Dissolve(1)
                    mc "Elena."
                    mc "They're just the perfect size for her body."
                    z "Hmm. They aren't bad but I think the others look better."
                    z "Mine is a toss-up between Layla and Valeria."
                    z "But I think Layla edges slightly ahead."
                "Valeria":
                    scene 08_943_val with Dissolve(1)
                    mc "Don't get mad at me, but it's Valeria."
                    mc "Before today I would've said Layla, but seeing Val in her bikini... Sorry, Zach."
                    z "Haha, no worries. They look amazing."
                    z "For me, it's the other way around. It is a toss-up between Layla and Valeria."
                    z "But Layla edges slightly ahead."
                "Sienna":
                    scene 08_943_sienna with Dissolve(1)
                    mc "Sienna."
                    z "Really?"
                    mc "Yeah. I prefer smaller boobs. Along with her pale skin... So pretty."
                    z "They look nice, but mine is a toss-up between Layla and Valeria."
                    z "But I think Layla edges slightly ahead."
                "Tori":
                    scene 08_943_tori with Dissolve(1)
                    mc "Uh... Well... It's Tori."
                    z "What?"
                    mc "Yeah."
                    z "Tori? What the hell... She isn't bad looking, I'll give you that. But just her reputation alone..."
                    if Tori_Week3_Friday_TC_Step == True:
                        mc "I know, but somehow, I don't know what exactly it is, she turns me on."
                        mc "Even when she was stepping on me before. I thought it was hot."
                        z "There is something majorly wrong with you, dude!"
                        mc "Haha."
                    else:
                        mc "I know, but somehow, I don't know what exactly it is, she turns me on."
                        z "There is something majorly wrong with you, dude!"
                        mc "Haha."
        else:
            mc "I pick..."
            menu:
                "Layla":
                    scene 08_943_layla with Dissolve(1)
                    mc "Layla, no competition. Hers are just... Yum."
                    z "Yum? That's a good word for it."
                    z "Mine is a toss-up between Layla and Valeria."
                    z "But I think Layla edges slightly ahead. So, I agree with you on Layla. Yum!"
                "Elena":
                    scene 08_943_elena with Dissolve(1)
                    mc "Elena."
                    mc "They're just the perfect size for her body."
                    z "Hmm. They aren't bad but I think the others look better."
                    z "Mine is a toss-up between Layla and Valeria."
                    z "But I think Layla edges slightly ahead."
                "Valeria":
                    scene 08_943_val with Dissolve(1)
                    mc "Don't get mad at me, but it's Valeria."
                    mc "Before today I would've said Layla, but seeing Val in her bikini... Sorry, Zach."
                    z "Haha, no worries. They look amazing."
                    z "For me, it's the other way around. It is a toss-up between Layla and Valeria."
                    z "But Layla edges slightly ahead."
                "Sienna":
                    scene 08_943_sienna with Dissolve(1)
                    mc "Sienna."
                    z "Really?"
                    mc "Yeah. I prefer smaller boobs. Along with her pale skin... So pretty."
                    z "They look nice, but mine is a toss-up between Layla and Valeria."
                    z "But I think Layla edges slightly ahead."
    scene 08_944 with Dissolve(1)
    mc "Hot damn..."
    z "They're doing that on purpose, right?"
    mc "Yes. They know exactly what they're doing."
    z "Make us drool!"
    mc "I think I'll stay a little bit longer in the pool with you."
    z "Haha."
    scene 08_945 with Dissolve(1)
    to "Look at them with their ridiculous poses."
    to "They think they're all so pretty."
    jz "I thought you liked Valeria."
    to "I do. But I don't like that she's hanging around with them... She's in our group, they didn't want her."
    scene 08_946 with Dissolve(1)
    z "Best butt next."
    z "Take your pick."
    mc "You go first this time."
    z "Alright."
    scene 08_947 with Dissolve(1)
    z "Now this will come very unexpected from me, but it's Elena's."
    mc "Really? That is unexpected. Not Valeria, huh?"
    z "Yeah. She's skinny but she has that nice Latina ass."
    mc "Valeria is a Latina."
    z "That's right! I keep forgetting that. I don't know why. Valeria has a really sweet ass, but it's more muscular, athletic. Elena's is more round and juicy, you know what I mean?"
    z "Don't ever tell Elena I said that though."
    mc "I won't."
    z "Who's your number one?"
    if Zach_Week3_Wednesday_TC_Girlshower == True:
        if Tori_Week3_Wednesday_TC_Fun == True:
            menu:
                "Layla":
                    scene 08_948_layla with Dissolve(1)
                    mc "Layla. It's so feminine. Perfect curves."
                    z "Yeah, she would've been my second pick."
                "Elena":
                    scene 08_948_elena with Dissolve(1)
                    mc "This time I agree with you. It's Elena."
                    mc "Just let me use it as a pillow, Elena."
                    z "Haha."
                "Valeria":
                    scene 08_948_val with Dissolve(1)
                    mc "It's Valeria's. I actually like her athletic bum. It looks so firm and has a nice shape to it. So slappable."
                    z "Hey! If anyone's allowed to slap that, it's me!"
                    mc "Haha."
                "Sienna":
                    scene 08_948_sienna with Dissolve(1)
                    mc "Sienna. I like small butts."
                    z "Hmm... Not enough curve for me. It just doesn't do it for me."
                "Tori":
                    scene 08_902 with Dissolve(1)
                    mc "I don't know why, but it's Tori's..."
                    z "What? Seriously?"
                    mc "I think she's put a spell on me or something. I can't get her out of my head."
                    z "There's clearly something wrong up there."
                    mc "Haha."
                "Jasmine":
                    scene 08_902 with Dissolve(1)
                    mc "Jasmine... You had to see her at the showers."
                    mc "She was bending over and..."
                    z "Now I wish I'd looked a bit longer."
                    z "But she has a really nice bum. When she was walking by earlier... If not for Elena, I might agree."
        else:
            menu:
                "Layla":
                    scene 08_948_layla with Dissolve(1)
                    mc "Layla. It's so feminine. Perfect curves."
                    z "Yeah, she would've been my second pick."
                "Elena":
                    scene 08_948_elena with Dissolve(1)
                    mc "This time I agree with you. It's Elena."
                    mc "Just let me use it as a pillow, Elena."
                    z "Haha."
                "Valeria":
                    scene 08_948_val with Dissolve(1)
                    mc "It's Valeria's. I actually like her athletic bum. It looks so firm and has a nice shape to it. So slappable."
                    z "Hey! If anyone's allowed to slap that, it's me!"
                    mc "Haha."
                "Sienna":
                    scene 08_948_sienna with Dissolve(1)
                    mc "Sienna. I like small butts."
                    z "Hmm... Not enough curve for me. It just doesn't do it for me."
                "Jasmine":
                    scene 08_902 with Dissolve(1)
                    mc "Jasmine... You had to see her at the showers."
                    mc "She was bending over and..."
                    z "Now I wish I'd looked a bit longer."
                    z "But she has a really nice bum. When she was walking by earlier... If not for Elena, I might agree."
    else:
        if Tori_Week3_Wednesday_TC_Fun == True:
            menu:
                "Layla":
                    scene 08_948_layla with Dissolve(1)
                    mc "Layla. It's so feminine. Perfect curves."
                    z "Yeah, she would've been my second pick."
                "Elena":
                    scene 08_948_elena with Dissolve(1)
                    mc "This time I agree with you. It's Elena."
                    mc "Just let me use it as a pillow, Elena."
                    z "Haha."
                "Valeria":
                    scene 08_948_val with Dissolve(1)
                    mc "It's Valeria's. I actually like her athletic bum. It looks so firm and has a nice shape to it. So slappable."
                    z "Hey! If anyone's allowed to slap that, it's me!"
                    mc "Haha."
                "Sienna":
                    scene 08_948_sienna with Dissolve(1)
                    mc "Sienna. I like small butts."
                    z "Hmm... Not enough curve for me. It just doesn't do it for me."
                "Tori":
                    scene 08_902 with Dissolve(1)
                    mc "I don't know why, but it's Tori's..."
                    z "What? Seriously?"
                    mc "I think she's put a spell on me or something. I can't get her out of my head."
                    z "There's clearly something wrong up there."
                    mc "Haha."
        else:
            menu:
                "Layla":
                    scene 08_948_layla with Dissolve(1)
                    mc "Layla. It's so feminine. Perfect curves."
                    z "Yeah, she would've been my second pick."
                "Elena":
                    scene 08_948_elena with Dissolve(1)
                    mc "This time I agree with you. It's Elena."
                    mc "Just let me use it as a pillow, Elena."
                    z "Haha."
                "Valeria":
                    scene 08_948_val with Dissolve(1)
                    mc "It's Valeria's. I actually like her athletic bum. It looks so firm and has a nice shape to it. So slappable."
                    z "Hey! If anyone's allowed to slap that, it's me!"
                    mc "Haha."
                "Sienna":
                    scene 08_948_sienna with Dissolve(1)
                    mc "Sienna. I like small butts."
                    z "Hmm... Not enough curve for me. It just doesn't do it for me."
    scene black with Dissolve(1)
    pause 2
    scene 08_949 with Dissolve(1)
    mc "The pictures are looking really good!"
    el "Just the pictures?"
    mc "Only because you girls are so pretty!"
    la "Good save."
    mc "Let's do one more. Show me your best pose."
    la "Are you a professional photographer now?"
    mc "I just might be."
    scene 08_950 with Dissolve(1)
    mc "Gorgeous, Sienna. Yes, Elena, that's what I want to see!"
    la "Haha."
    mc "Take it seriously, Layla! Stop wasting our time!"
    la "Haha. Sorry, sorry."
    z "Now. Best girl overall."
    if Alexis_Dating == True:
        mc "Easy. Alexis!"
        mc "Who's yours?"
    else:
        if TC_Pool_Layla == True:
            mc "Easy. Layla!"
            mc "Who's yours?"
        else:
            if TC_Pool_Elena == True:
                mc "Easy. Elena!"
                mc "Who's yours?"
            else:
                if TC_Pool_Sienna == True:
                    mc "Easy. Sienna!"
                    mc "Who's yours?"
                else:
                    mc "Easy. Valeria!"
                    mc "Who's yours?"
    scene 08_951 with Dissolve(1)
    mc "..."
    mc "Who's yours?"
    mc "Zach?"
    z "Forget everything I said."
    z "She has the perfect boobs, the perfect ass, the perfect everything!"
    mc "What?"
    z "Look there!"
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 08_952 at moveup
    pause 3
    mc "Gabi?"
    z "Uh-huh."
    scene 08_953 with Dissolve(1)
    z "Take a picture of her."
    mc "Are you crazy?"
    z "Please, I need it!"
    mc "This isn't even my phone. It's Layla's..."
    z "Just ask her to send me that picture later. After that, she can delete it."
    menu:
        "Take picture[KoGa3AutoWTChange1]{size=-4}(Gabi Week3 Friday TC Picture, Zach Points+2) {/size} {/color}":
            $ Gabi_Week3_Friday_TC_Picture = True
            $ Zach_Points += 2
            # Zach (10)
            mc "Alright, alright."
            z "My man."
            mc "I hope she doesn't notice."
            scene 08_954 with Dissolve(1)
            mc "{i}(Oh shit... Did she see?){/i}"
            mc "{i}(Just keep on walking.){/i}"
        "Don't do it":
            mc "Sorry, but I'm not doing that."
            z "..."
    scene black with Dissolve(1)
    pause 2
    scene 08_939 with Dissolve(1)
    z "Here we go again."
    z "What are they discussing this time?"
    scene 08_955 with Dissolve(1)
    la "[mc], come here for a second."
    la "We have a little surprise as a thank you for taking the pictures."
    mc "No need. I had fun taking them."
    la "No, no, sit down here. You'll love it."
    scene 08_956 with Dissolve(1)
    la "Can you take the next picture for us, Zach?"
    z "Sure."
    la "Thank you."
    scene 08_957 with Dissolve(1)
    z "{i}(Holy shit... She's sitting right here, basically next to me.){/i}"
    z "{i}(This must be a sign.){/i}"
    if Gabi_Week3_Friday_TC_Picture == True:
        z "{i}(Nothing wrong with a second picture, right?){/i}"
    else:
        z "{i}(I need this picture!){/i}"
    scene 08_958 with Dissolve(1)
    z "{i}(She's so hot! Are teachers allowed to be this sexy?){/i}"
    z "{i}(Why didn't I take Spanish...){/i}"
    scene 08_959 with Dissolve(1)
    mc "{i}(Oh, my own little harem right here.){/i}"
    mc "You were right. I kinda love this."
    la "Haha. We knew it."
    z "Hey! I also want one of those pictures..."
    scene black with Dissolve(1)
    pause 2
    scene 08_960 with Dissolve(1)
    z "Ready everyone?"
    z "Three... two... one..."
    scene 08_961 with Dissolve(1)
    tr "..."
    scene 08_962 with Dissolve(1)
    z "Okay, my turn!"
    z "This is so awesome."
    z "Come on girls, join me, don't be shy."
    scene 08_963 with Dissolve(1)
    el "I'm not going to be in that picture."
    z "I didn't even want you in it, anyway..."
    el "Good!"
    scene 08_964 with Dissolve(1)
    mc "And... Done!"
    mc "Thanks, girls."
    la "Thank you, too."
    scene black with Dissolve(1)
    pause 2
    scene 08_965 with Dissolve(1)
    la "We're going to get some coffee. Do you want anything?"
    mc "I'm good, thank you."
    la "How about you, Zach?"
    z "Nothing, thanks."
    la "Can you keep an eye on our stuff?"
    mc "Uh-huh."
    la "Thanks, see you later."
    scene black with Dissolve(1)
    pause 2
    scene 08_966 with Dissolve(1)
    z "That was fun. Next time we rate all the girls in our school."
    mc "Haha."
    z "By the way, have you heard the rumour yet?"
    mc "No, what rumour?"
    z "Well, this info comes from one of the other schools, so who knows..."
    z "Supposedly, a big shot agent is coming to watch the competition tomorrow."
    mc "Oh?"
    scene 08_967 with Dissolve(1)
    mc "Is he or she coming for someone specific or just to scout some up-and-coming talent?"
    z "No idea. It's definitely not for me though, haha."
    mc "Don't sell yourself short."
    z "Thanks, but I know my limits. My only focus is to impress a scout from a university."
    mc "For a scholarship?"
    z "Exactly."
    scene 08_968 with Dissolve(1)
    z "What are your plans after this year?"
    mc "Most likely MSU."
    z "MSU would be a dream destination. But without a scholarship, that's a no for me."
    z "They'll never accept me with my scores."
    mc "It's never too late..."
    z "Nah, that ship sailed a long time ago."
    scene 08_969 with Dissolve(1)
    z "Any specific reason why MSU?"
    mc "Their athletics department is top-notch for starters."
    z "So you're continuing with track?"
    mc "Yeah. I enjoy it and might give it a serious shot."
    z "You should."
    mc "It's close to home. Which is a plus."
    if Alexis_Dating == True:
        scene 08_970 with Dissolve(1)
        mc "And Alexis is at MSU. Would be cool to attend the same college."
        z "Right. Our cute bartender Alexis. Things seem to be getting serious, huh?"
        mc "It's going really good."
        z "I'm happy for you, man."
        mc "Thanks."
        scene 08_971 with Dissolve(1)
        mc "Erynn is also at MSU."
        z "Really? Damn... New top priority. Getting a scholarship to MSU."
        mc "Haha."
        z "Maybe she can give us a tour of the campus?"
        mc "I'll ask her."
        z "Awesome."
        scene 08_972 with Dissolve(1)
        z "Do you know what the girls will do after this year?"
        mc "No idea. Haven't talked about that with any of 'em."
        mc "But I think they'll all go to college first."
        mc "Layla will most likely go to MSU as well, to join her sister."
        scene 08_973 with Dissolve(1)
        z "Wait, wait, wait. Layla has a sister?"
        z "How do you know?"
        mc "Are you serious? You've known Layla for how many years? How could you not know? Besides, she told us before."
        mc "{i}(Actually, I only found out myself a few days ago who it is.){/i}"
        z "Hmm... Can't recall at all."
        mc "And we just spoke about her."
        z "Hmm... Have you met her? Is she cute? How old is she?"
        scene 08_974 with Dissolve(1)
        mc "I've met her, multiple times. She's very cute. Twenty years old. Oh, and you've met her, too."
        z "What, really? Who..."
        mc "Alexis!"
        z "..."
        z "Your Alexis? Bartender Alexis?"
        mc "Yeah!"
    else:
        scene 08_972 with Dissolve(1)
        z "Do you know what the girls will do after this year?"
        mc "No idea. Haven't talked about that with any of em."
        mc "But I think they'll all go to college first."
        mc "Layla will most likely go to MSU as well, to join her sister."
        scene 08_973 with Dissolve(1)
        z "Wait, wait, wait. Layla has a sister?"
        z "How do you know?"
        mc "Are you serious now? How come you don't know? You've known Layla for how many years? Besides, she told us before."
        mc "{i}(Actually, I only found out myself a few days ago who it is.){/i}"
        z "Hmm... Can't recall at all."
        z "Have you met her? Is she cute? How old is she?"
        if Alexis_Sex == False:
            scene 08_974a with Dissolve(1)
            mc "I've met her, multiple times. She's pretty. You've met her, too."
            z "What, really? Who..."
            mc "Alexis!"
            z "..."
            z "Bartender Alexis?"
            mc "Yeah!"
            scene 08_975 with Dissolve(1)
            z "She's Layla's sister?"
            mc "Uh-huh."
        else:
            scene 08_974a with Dissolve(1)
            mc "I've met her, multiple times. She's pretty. Actually hooked up with her. You've met her, too."
            z "What, really? Who..."
            mc "Alexis!"
            z "..."
            z "Bartender Alexis? You hooked up with her?"
            mc "Yeah!"
            scene 08_975 with Dissolve(1)
            z "And she's Layla's sister?"
            mc "Uh-huh."
    z "Wow... I'm kinda mind blown right now."
    z "I even have a buzzing sound in my head, it's affected me that much."
    mc "Haha."
    scene 08_976 with Dissolve(1)
    z "No, but seriously, what is that sound?"
    mc "What sound?"
    z "Listen."
    mc "..."
    play sound "Sounds/Phone_Vibrate.mp3"
    n "*Bzzzt. Bzzzt*"
    scene 08_977 with Dissolve(1)
    mc "That's my phone!"
    play sound "Sounds/Phone_Vibrate.mp3"
    n "*Bzzzt. Bzzzt*"
    if Erynn_End == True:
        jump Week3_Friday_Pool_Phone
    else:
        if Erynn_Week3_Monday_Blackmailhelp == False:
            jump Week3_Friday_Pool_Phone
        else:
            jump Week3_Friday_Pool_Phone_Erynn

label Week3_Friday_Pool_Phone:
    scene 08_978 with Dissolve(1)
    z "Who is it?"
    mc "Unknown number."
    scene 08_986 with Dissolve(1)
    mc "Hello?"
    x "Hello, sir. I'm reaching out to you concerning your car's extended warranty!"
    mc "Fuck off!"
    scene 08_998 with Dissolve(1)
    z "Haha, who was that?"
    mc "Telemarketer."
    mc "I hate tho..."
    scene 08_999 with vpunch
    mc "Aaah..."
    x "SORRY!"
    scene 08_1001 with Dissolve(1)
    x "I'm so sorry. It was an accident."
    mc "{i}(Was it though?){/i}"
    menu:
        "Kick the ball away[KoGa3AutoWTChange1]{size=-4}(Week3 Friday TC Kickball, ShaCarri End, Tori Points+2) {/size} {/color}":
            $ Week3_Friday_TC_Kickball = True
            $ ShaCarri_End = True
            $ Tori_Points += 2
            # Tori (14)
            scene 08_1004 with Dissolve(1)
            mc "..."
            z "Haha."
            z "I told you you should've joined the football team instead of track!"
            scene 08_1005 with Dissolve(1)
            x "What the fuck, dude. It was an accident."
            mc "The expression on your friend's face says otherwise."
            x "Whatever..."
            scene 08_1008 with Dissolve(1)
            to "Ups..."
            x "Really, Tori?"
            scene 08_1009 with Dissolve(1)
            x "Haven't changed much from last year, huh? Still a bitch, it seems."
            to "Haha. The only thing that will change is who crosses the finish line first tomorrow."
            x "Uh-huh."
            to "Now go fetch!"
            x "..."
        "Throw the ball back[KoGa3AutoWTChange1]{size=-4}(ShaCarri Points+2) {/size} {/color}":
            $ ShaCarri_Points += 2
            # ShaCarri (2)
            scene 08_1002 with Dissolve(1)
            mc "It's fine."
            mc "Here you go."
            scene 08_1003 with Dissolve(1)
            x "Thanks."
            menu:
                "Check her out[KoGa3AutoWTChange1]{size=-4}(ShaCarri Points+2) {/size} {/color}":
                    $ ShaCarri_Points += 2
                    # ShaCarri (4)
                    scene black with Dissolve(1)
                    transform moveup:
                        xalign 0.5 yalign 1.0
                        linear 5.0 yalign 0.0
                    show 08_1006 at moveup
                    pause 3
                    mc "{i}(I like her tattoos.){/i}"
                    scene 08_1007 with Dissolve(1)
                    x "See, I told you he's cute."
                    x "Yeah, not bad. He wasn't here last year, right? What school is he from?"
                    x "No idea."
                "Don't":
                    scene 08_1007 with Dissolve(1)
                    x "See, I told you he's cute."
                    x "He wasn't here last year, right? What school is he from?"
                    x "No idea."
    scene 08_1010 with Dissolve(1)
    z "You know who that was?"
    mc "I have no idea. Do you?"
    z "Sha'Carri Evans. The winner of the 100m race last year."
    mc "Which one?"
    z "The mixed girl with the tats and coloured hair."
    z "I almost didn't recognise her. She had blue hair before."
    mc "It amazes me how you know every girl."
    jump Week3_Friday_Pool_Play

label Week3_Friday_Pool_Phone_Erynn:
    if _in_replay:
        $ Erynn_Friends = False
        $ Erynn_Points = 32
        $ Erynn_Week1_Saturday_Pool = True
        $ Tori_Points = 12
        $ ShaCarri_Points = 0
    scene 08_978 with Dissolve(1)
    mc "Oh, it's actually..."
    z "The devil?"
    mc "She can be a devil sometimes. Erynn."
    z "Sorry. I meant to say angel!"
    mc "Haha. Give me a second."
    scene 08_979 with Dissolve(1)
    z "Tell her hi from me."
    z "I'll do some sightseeing in the meantime."
    mc "Hehe, sure."
    scene 08_980 with Dissolve(1)
    mc "Hey, Erynn."
    mc "How are you?"
    scene 08_981 with Dissolve(1)
    er "Hi!"
    er "I'm good. How are you?"
    mc "Good also."
    mc "You sound happy."
    er "Because I am."
    scene 08_982 with Dissolve(1)
    mc "Anything good happen?"
    er "Nothing special. Just enjoying being at home I guess."
    mc "{i}(Seems like Ethan hasn't shown up yet. I'm happy about that, but also uneasy. He must be up to something, right?){/i}"
    mc "{i}(Better not bring that up now. She seems to be in a really good mood.){/i}"
    scene 08_983 with Dissolve(1)
    er "How has training been? Are you having fun?"
    mc "Amazing. And yes, we're having lots of fun here."
    er "You are? Maybe I should've taken Zach's offer and joined you."
    mc "Haha."
    er "I'm regretting it a little bit."
    scene 08_984 with Dissolve(1)
    er "Do you miss me, at least?"
    mc "Do you want an honest answer?"
    er "Oh wow..."
    mc "What? I didn't say I'm not!"
    er "..."
    scene 08_985 with Dissolve(1)
    er "So do you?"
    mc "Do you want an honest answer?"
    er "Haha, you asshole!"
    mc "Haha."
    scene 08_986 with Dissolve(1)
    er "Are you done training for today?"
    mc "We only had half a day so we can relax a bit before tomorrow's competition."
    mc "So at the moment I'm enjoying the sun and lying by the pool."
    er "I'm doing the exact same thing!"
    if Erynn_Friends == True:
        er "Hey, can we Facetime maybe?"
        mc "Sure."
        scene 08_988 with Dissolve(1)
        mc "Hi!"
        er "Hey."
        mc "You're wearing your hair loose again. Very pretty!"
        er "Thank you."
    else:
        menu:
            "Flirt[KoGa3AutoWTChange1]{size=-4}(Erynn Points+2) {/size} {/color}":
                $ Erynn_Points += 2
                # Erynn (36)
                if Erynn_Week1_Saturday_Pool == True:
                    scene 08_987 with Dissolve(1)
                    mc "Are you wearing your mom's bikini again?"
                    er "Haha. You'd like that, huh?"
                    er "No. I've brought my own. Want to see?"
                    mc "Yes!"
                    er "Let's Facetime. I want to see you too!"
                else:
                    scene 08_987 with Dissolve(1)
                    mc "What are you wearing?"
                    er "A red bikini. Want to see?"
                    mc "Yes!"
                    er "Let's Facetime. I want to see you too!"
                scene black with Dissolve(1)
                pause 2
                scene 08_988 with Dissolve(1)
                mc "Hi!"
                er "Hey."
                mc "You're wearing your hair loose again. Very pretty!"
                er "Thank you."
                scene 08_989 with Dissolve(1)
                er "As promised!"
                mc "Oh my..."
                er "You like it?"
                mc "I do. Really sexy, Erynn!"
                scene 08_990 with Dissolve(1)
                er "Thank you."
                mc "Can you send me that as a picture too?"
                er "Haha. I'll think about it."
            "Don't":
                er "Hey, can we Facetime maybe?"
                mc "Sure."
                scene 08_988 with Dissolve(1)
                mc "Hi!"
                er "Hey."
                mc "You're wearing your hair loose again. Very pretty!"
                er "Thank you."
    scene 08_991 with Dissolve(1)
    er "You look good too! A little red, maybe?"
    er "How long have you been in the sun already?"
    mc "A few hours, I think."
    er "Ask your friends to put some sunscreen on you, you'll burn if you stay much longer."
    mc "I'll be fine."
    me "Who are you talking to?"
    scene 08_992 with Dissolve(1)
    er "[mc]."
    er "He's at training camp right now."
    er "Here, you can say hi to him."
    scene 08_993 with Dissolve(1)
    me "Hey, [mc]. How are you? Having fun?"
    mc "Uh... Hi, Melissa."
    mc "..."
    mc "Yeah... Fun..."
    scene 08_994 with Dissolve(1)
    me "Why is he looking so surprised in that picture?"
    er "Huh?"
    me "..."
    me "Wait... Is your camera on?!"
    er "Yeah, it's Facetime."
    scene 08_995 with Dissolve(1)
    me "Erynn!"
    er "Haha. So deserved!"
    mc "Like mother, like daughter."
    scene 08_996 with Dissolve(1)
    me "Oh, Rinny! Big mistake!"
    er "Haha."
    me "And you better be prepared too, once you're back, [mc]!"
    mc "I didn't do anything!"
    scene 08_997 with Dissolve(1)
    mc "Hey, don't involve me in your schemes!"
    mc "Now I have to watch my back, too."
    er "Haha. Sorry, sorry!"
    scene black with Dissolve(1)
    pause 2
    scene 08_998 with Dissolve(1)
    er "Have you had a chance to scope out the competition yet?"
    mc "No. Training was so exhausting, I was happy to stay in bed for the rest of the time."
    mc "But I've heard there are some really fast people here. Especially from Miramar Bay Academy."
    er "I have faith you'll do well."
    mc "Thanks."
    mc "What are yo..."
    scene 08_999 with vpunch
    mc "Aaah..."
    x "SORRY!"
    scene 08_1000 with Dissolve(1)
    er "[mc]!"
    er "Are you okay? What happened?"
    mc "Are you kidding me?"
    scene 08_1001 with Dissolve(1)
    x "I'm so sorry. It was an accident."
    mc "{i}(Was it though?){/i}"
    menu:
        "Kick the ball away[KoGa3AutoWTChange1]{size=-4}(Week3 Friday TC Kickball, ShaCarri End, Tori Points+2) {/size} {/color}":
            $ Week3_Friday_TC_Kickball = True
            $ ShaCarri_End = True
            $ Tori_Points += 2
            # Tori (14)
            scene 08_1004 with Dissolve(1)
            mc "..."
            z "Haha."
            z "I told you you should've joined the football team instead of track!"
            scene 08_1005 with Dissolve(1)
            x "What the fuck, dude. It was an accident."
            mc "The expression on your friend's face says otherwise."
            x "Whatever..."
            scene 08_1008 with Dissolve(1)
            to "Ups..."
            x "Really, Tori?"
            scene 08_1009 with Dissolve(1)
            x "Haven't changed much from last year, huh? Still a bitch, it seems."
            to "Haha. The only thing that will change is who crosses the finish line first tomorrow."
            x "Uh-huh."
            to "Now go fetch!"
            x "..."
        "Throw the ball back[KoGa3AutoWTChange1]{size=-4}(ShaCarri Points+2) {/size} {/color}":
            $ ShaCarri_Points += 2
            # ShaCarri (2)
            scene 08_1002 with Dissolve(1)
            mc "It's fine."
            mc "Here you go."
            scene 08_1003 with Dissolve(1)
            x "Thanks."
            menu:
                "Check her out[KoGa3AutoWTChange1]{size=-4}(ShaCarri Points+2) {/size} {/color}":
                    $ ShaCarri_Points += 2
                    # ShaCarri (4)
                    scene black with Dissolve(1)
                    transform moveup:
                        xalign 0.5 yalign 1.0
                        linear 5.0 yalign 0.0
                    show 08_1006 at moveup
                    pause 3
                    mc "{i}(I like her tattoos.){/i}"
                    scene 08_1007 with Dissolve(1)
                    x "See, I told you he's cute."
                    x "Yeah, not bad. He wasn't here last year, right? What school is he from?"
                    x "No idea."
                "Don't":
                    scene 08_1007 with Dissolve(1)
                    x "See, I told you he's cute."
                    x "He wasn't here last year, right? What school is he from?"
                    x "No idea."
    scene 08_1010 with Dissolve(1)
    z "You know who that was?"
    mc "I have no idea. You do?"
    z "Sha'Carri Evans. The winner of the 100m race last year."
    mc "Which one?"
    z "The mixed girl with the tats and coloured hair."
    z "I almost didn't recognise her. She had blue hair before."
    mc "It amazes me how you know every girl."
    scene black with Dissolve(1)
    pause 2
    scene 08_1011 with Dissolve(1)
    mc "I'm back. Sorry."
    er "Hey. What happened?"
    mc "Got hit in the face by a ball."
    scene 08_1012 with Dissolve(1)
    er "Are you okay? Are you hurt?"
    mc "I'm okay. And no, it didn't hurt. It was just a beach ball. More air than anything else."
    scene 08_1013 with Dissolve(1)
    me "Did something happen?"
    er "No, no. He's fine. He got hit in the face by a ball."
    me "Ouch..."
    scene 08_1014 with Dissolve(1)
    if Erynn_Friends == True:
        mc "What are you doing at the weekend?"
        er "Working on some assignments that need to be done before the break."
        er "Then some relaxing and tanning, like I'm doing now."
    else:
        mc "What are you doing at the weekend?"
        er "Working on some assignments that need to be done before the break."
        er "Then some relaxing and tanning, like I'm doing now."
        scene 08_1015 with Dissolve(1)
        er "Maybe topless."
        mc "..."
        mc "You know I'll need proof of that!"
        er "Haha. Not happening!"
    scene black with Dissolve(1)
    pause 2
    scene 08_1016 with Dissolve(1)
    er "Anyway. I'll stop bothering you and let you relax some more."
    mc "You're not bothering me, Erynn!"
    er "I just wanted to know if you're okay and having fun."
    scene 08_1017 with Dissolve(1)
    er "We'll talk when you're back?"
    mc "Of course."
    er "Oh and don't forget to let me know how the competition went."
    mc "Will do."
    if Erynn_Points >= 31:
        scene 08_1018 with Dissolve(1)
        er "Bye, [mc]."
        mc "Later, Erynn. And bye, Mel."
        scene black with Dissolve(1)
        pause 2
        scene 08_1019 with Dissolve(1)
        me "Now you're taking it off?"
        er "I'm not going to be topless while facetiming with [mc]."
        scene 08_1020 with Dissolve(1)
        er "Like you did!"
        me "Very funny..."
        scene 08_1021 with Dissolve(1)
        me "You should stop teasing the poor boy."
        me "At least send him a picture now."
        er "I'm not sending him a picture!"
        er "..."
        er "{i}(Yet.){/i}"
    else:
        scene 08_1018 with Dissolve(1)
        er "Bye, [mc]."
        mc "Later, Erynn. And bye, Mel."
    $ renpy.end_replay()
    jump Week3_Friday_Pool_Play

label Week3_Friday_Pool_Play:
    scene black with Dissolve(1)
    pause 2
    scene 08_1022 with Dissolve(1)
    mc "{i}(The girls have been gone for quite some time, now.){/i}"
    scene black with Dissolve(1)
    pause 2
    scene 08_1023 with vpunch
    mc "Aaaah..."
    scene 08_1024 with Dissolve(1)
    mc "Layla!"
    la "Haha."
    la "It looked like you needed a little refreshing!"
    mc "..."
    mc "You just wait!"
    scene 08_1025 with Dissolve(1)
    la "Haha..."
    mc "I guess you still haven't learned your lesson yet."
    mc "For every action, there is a reaction!"
    scene 08_1026 with Dissolve(1)
    la "What are you going to do, brave Sir [mc]?"
    mc "..."
    mc "Let's see how brave you are, Miss Layla!"
    scene 08_1027 with Dissolve(1)
    mc "Zach. Grab her feet!"
    la "What... No!"
    scene 08_1028 with Dissolve(1)
    la "Listen, Zach. Together we can..."
    z "Nice try. But bros before ho... Girls! Always!"
    la "..."
    scene black with Dissolve(1)
    pause 2
    scene 08_1029 with Dissolve(1)
    la "Guys. Can we talk about this?"
    la "I think we can come to an agreement."
    la "..."
    la "Please!"
    scene 08_1030 with Dissolve(1)
    la "I will do anything if you let me go, Zach."
    z "Anything?"
    la "Anything!"
    scene 08_1031 with Dissolve(1)
    mc "Don't listen to her."
    mc "She's trying to manipulate you."
    la "You shush. I'm talking to Zach."
    mc "You are in no position to make demands! Literally!"
    scene 08_1032 with Dissolve(1)
    la "What do you want?"
    z "..."
    z "I want to throw you in the pool!"
    show 08_1032_Swing
    la "NOOO!"
    mc "Haha."
    la "Please!"
    mc "One!"
    la "No-no-no..."
    mc "Two!"
    la "I'm so sorry, [mc]!"
    scene 08_1033 with Dissolve(1)
    tr "Guys, be careful!"
    show 08_1032_Swing2
    pause 2
    la "AAAH!"
    pause 2
    scene 08_1034 with Dissolve(1)
    mc "It looked like you needed a little refreshing too!"
    la "Ha-ha-ha. Two against one... So not fair!"
    mc "It's boys against girls. Your words, remember?"
    la "..."
    scene 08_1035 with vpunch
    va "I remember."
    mc "Hey!"
    scene 08_1036 with Dissolve(1)
    la "Haha. That's what you get."
    mc "Hehe. This isn't over yet."
    la "Your hair's all ruffled up, now."
    mc "So is yours!"
    scene 08_1037 with Dissolve(1)
    va "I'm so sorry. It wasn't on purpose or anything."
    mc "Of course not."
    va "The ground was wet and I slipped."
    mc "Uh-huh..."
    scene 08_1038 with Dissolve(1)
    la "Thank you, Val!"
    va "You're welcome."
    scene 08_1039 with Dissolve(1)
    z "{i}(Hmm...){/i}"
    z "{i}(Maybe I should've put her in first place instead of Elena.){/i}"
    scene 08_1040 with Dissolve(1)
    z "{i}(Your pretty butt won't help you this time.){/i}"
    la "Val, watch out!"
    scene 08_1041 with Dissolve(1)
    z "Don't let your guard down."
    va "Uh..."
    la "ZACH!"
    scene 08_1042 with Dissolve(1)
    z "Haha."
    z "[mc], watch out! Incoming!"
    scene 08_1043 with vpunch
    ""
    scene 08_1044 with Dissolve(1)
    mc "{i}(Soft...){/i}"
    scene 08_1045 with Dissolve(1)
    va "*Deep breath*"
    va "*Cough. Cough*"
    scene 08_1046 with Dissolve(1)
    la "Val! Are you alright?"
    va "Yeah, I think I swallowed some water, though."
    scene 08_1047 with Dissolve(1)
    la "Zach! Why did you push her so hard?"
    z "It was just a normal push... I'm sorry, Val."
    va "It's fine. Nothing happened."
    scene 08_1048 with Dissolve(1)
    tr "Is everyone alright?"
    z "We are."
    tr "I told you guys to be careful!"
    tr "What if you get injured a day before the competition?"
    scene 08_1049 with Dissolve(1)
    z "We're just playing, Gabi..."
    tr "..."
    z "I mean Ms Ram..."
    scene 08_1050 with vpunch
    tr "I'm just playing too."
    z "Hey!"
    scene 08_1051 with Dissolve(1)
    mc "Haha. That just happened."
    mc "Who would've thought she'd push him."
    scene 08_1055 with Dissolve(1)
    tr "..."
    scene 08_1052 with Dissolve(1)
    va "..."
    va "Uhm... Thank you, but you can let go now."
    scene 08_1053 with Dissolve(1)
    mc "Oh, sorry!"
    scene 08_1054 with Dissolve(1)
    la "Haha. You deserved that."
    z "Funnily enough. I didn't even mind."
    la "You're so weird."
    scene black with Dissolve(1)
    pause 2
    scene 08_1056 with Dissolve(1)
    z "Since we're all in the pool now. How about a little game?"
    mc "I'm up for it. What do you have in mind?"
    z "The girls sitting on our shoulders and trying to push each other off."
    z "First to fall loses."
    scene 08_1057 with Dissolve(1)
    z "What do you girls think?"
    la "Sure, I'm in."
    va "Yeah, why not."
    scene 08_1058 with Dissolve(1)
    z "But no scratching, clawing, hair-pulling or anything like that."
    la "Who do you think we are?"
    z "I've seen girls fight."
    va "..."
    la "You sure you weren't punching a mirror?"
    scene 08_1059 with Dissolve(1)
    z "Ha-ha. Very funny..."
    mc "Haha. I thought it was good."
    mc "I can even picture it."
    z "Yeah, yeah. Just make fun of me."
    scene 08_1060 with Dissolve(1)
    z "Teams."
    z "How about Valeria and I versus you and Layla?"
    mc "Fine with me."
    z "Great. Let's do this."
    scene black with Dissolve(1)
    pause 2
    scene 08_1061 with Dissolve(1)
    la "Okay, change of plans."
    mc "You don't want to do this?"
    if Layla_Week1_Saturday_Beach_Ocean == True:
        la "I think this is something for Elena. She'll be much better at this than me."
        la "Remember the time at the beach? Besides, I want to tan a bit too, before we leave."
    else:
        la "I think this is something for Elena. She'll be much better at this than me."
        la "Besides, I want to tan a bit too, before we leave."
    mc "I don't mind, but maybe she doesn't want to get in the water."
    scene 08_1062 with Dissolve(1)
    la "She was laughing when you guys threw me in here and didn't even try to help me."
    la "I think you can figure something out to get her in the pool."
    mc "You're the mean one, but I'm the one who'll get the blame."
    la "She'll forgive you."
    mc "..."
    scene 08_1063 with Dissolve(1)
    z "Hey! Where are you going?"
    z "Giving up already?"
    mc "No, no. I'll be right back. Getting my secret weapon."
    z "Pssh... Secret weapon... No cheating though!"
    scene 08_1064 with Dissolve(1)
    z "Don't worry. Whatever they're planning won't matter."
    z "We'll win for sure."
    scene 08_1065 with Dissolve(1)
    mc "Hey Elena."
    el "Hey."
    mc "Where's Sienna?"
    el "Somewhere on the phone with her boyfriend."
    mc "Why don't you join us in the pool? Can't have you sitting here alone."
    el "Thanks, but I'm good. Just do your thing."
    scene 08_1066 with Dissolve(1)
    mc "Can't I convince you? We're playing a game that would be perfect for you."
    el "Not really in the mood to get in the water today."
    mc "{i}(Shit. I hate to do this. Thanks, Layla!){/i}"
    scene 08_1067 with Dissolve(1)
    mc "I'm so sorry, but you could have done this the easy way."
    el "[mc]! What are you doing?"
    scene 08_1068 with Dissolve(1)
    el "Aah..."
    el "[mc]!"
    la "Good luck, Elena!"
    el "I know this is your doing..."
    scene 08_1069 with Dissolve(1)
    el "Don't you dare, [mc]. I'm so going to beat you up!"
    el "Do you remember when I said you aren't that bad? I take that back."
    el "I hate you!"
    mc "Haha."
    el "[mc]!"
    scene 08_1070 with Dissolve(1)
    el "NOOOO!"
    la "Haha."
    scene 08_1071 with Dissolve(1)
    tr "Seriously? What did I say earlier... Am I talking to a wall?"
    tr "*Sigh*"
    scene black with Dissolve(1)
    pause 2
    scene 08_1072 with Dissolve(1)
    mc "Since you're in the pool already, how about you help me out?"
    el "..."
    mc "What's with the mean face?"
    scene 08_1073 with Dissolve(1)
    mc "Hey, haha."
    el "I told you I'd beat you up!"
    scene 08_1074 with Dissolve(1)
    z "They're fighting each other already. The secret weapon backfired completely."
    z "This will be even easier than I thought."
    scene 08_1075 with Dissolve(1)
    mc "They're right, let's stop fighting each other."
    mc "There isn't going to be a winner here."
    mc "Can't we just..."
    scene 08_1076 with Dissolve(1)
    mc "..."
    scene 08_1077 with Dissolve(1)
    mc "Never mind. I give up. You win!"
    el "Don't mess with me!"
    if Elena_Points >= 17:
        mc "Lesson learned!"
        mc "{i}(Is it weird that I enjoyed her grabbing my balls?){/i}"
    else:
        mc "Lesson learned!"
    scene 08_1078 with Dissolve(1)
    el "Go underwater for a second, so I can get on your shoulders."
    mc "Oh, you're joining us?"
    el "Like you said, since I'm in the pool already..."
    mc "Thanks, Elena!"
    scene black with Dissolve(1)
    pause 2
    scene 08_1079 with Dissolve(1)
    mc "All good?"
    el "Yes, let's kick some butt. Preferably not ours."
    mc "Haha, yes."
    scene 08_1080 with Dissolve(1)
    z "Finally!"
    z "You know you have us at a big disadvantage? I've had Valeria on my shoulders for a couple of minutes already!"
    mc "Boo-freaking-hoo. Here come the excuses."
    z "It's not an excuse!"
    mc "I carried Elena on my shoulders and even jumped into the pool with her. I think we're even."
    scene 08_1081 with Dissolve(1)
    z "Get ready girls!"
    z "Val, you know what to do."
    z "Three... two... one..."
    z "GO!"
    scene black with Dissolve(1)
    pause 2
    scene 08_1082 with Dissolve(1)
    va "Haha."
    z "Stop laughing and push her down!"
    el "Don't tell her what to do. We're doing the hard work here!"
    scene 08_1083 with Dissolve(1)
    z "I want to see aggression. Where is the shit-talking? Anything..."
    va "I don't want to do that. I like her."
    z "And you can like her again after we beat them."
    scene 08_1084 with Dissolve(1)
    mc "You're doing great, Elena! Keep pushing!"
    va "See, why can't you be more supportive like [mc] is?"
    z "I am. PUSH!"
    scene 08_1085 with Dissolve(1)
    el "Aaah..."
    mc "C'mon El. We can come back."
    el "I don't know about that. She's way stronger than I thought."
    if Elena_Week3_Monday_CheerTraining == False:
        mc "Show me your fighting spirit from earlier."
    else:
        mc "We've trained for this, remember?"
    scene 08_1086 with Dissolve(1)
    el "How are you so strong?"
    z "Yes, Val! That's what I mean."
    z "She's leaning back already. Just a little more. No mercy!"
    scene 08_1087 with Dissolve(1)
    mc "{i}(This view isn't so bad. Did she realise I basically motorboated her before?){/i}"
    el "Hey, what are you doing? Help me out here."
    scene 08_1088 with Dissolve(1)
    el "[mc]!"
    mc "{i}(Oh shit!){/i}"
    z "Nice, Val!"
    scene black with Dissolve(1)
    pause 2
    scene 08_1089 with Dissolve(1)
    mc "Sorry, that was my fault. Are you alright?"
    el "Yeah. Didn't think we would lose though. She's so strong!"
    mc "{i}(Her boob is out...){/i}"
    if Elena_Points >= 17:
        menu:
            "Tell her[KoGa3AutoWTChange1]{size=-4}(Elena Points+2) {/size} {/color}":
                $ Elena_Points += 2
                # Elena (22)
                mc "{i}(Better tell her before other people see.){/i}"
                scene 08_1091 with Dissolve(1)
                mc "Uhm. Your boob is out, Elena."
                el "Oh... Thank you!"
            "Pretend you didn't see":
                mc "{i}(I'll just pretend I didn't see.){/i}"
                scene 08_1090 with Dissolve(1)
                el "..."
                mc "Good job, guys."
            "Grab her[KoGa3AutoWTChange1]{size=-4}(Elena Points+4) {/size} {/color}":
                $ Elena_Points += 4
                # Elena (24)
                scene 08_1092 with vpunch
                el "What are you doing?"
                mc "Uhm. Your boob is out, Elena."
                el "What?"
                scene 08_1093 with Dissolve(1)
                el "Oh..."
                scene 08_1094 with Dissolve(1)
                el "You could've just told me without pressing up against me."
                mc "Sorry, I didn't want to make you uncomfortable."
                mc "I just reacted as quick as I could. I didn't want Zach to see and make a stupid comment."
                el "..."
                el "Thank you."
    else:
        mc "{i}(I'll just pretend I didn't see.){/i}"
        scene 08_1090 with Dissolve(1)
        el "..."
        mc "Good job, guys."
    scene 08_1095 with Dissolve(1)
    el "That was fun. Congratulations!"
    z "Thank you, thank you."
    scene 08_1096 with Dissolve(1)
    z "Hahaha. Good job, Val!"
    z "I knew we'd beat them easily."
    scene 08_1097 with Dissolve(1)
    z "We are the perfect couple!"
    va "..."
    z "No one can beat us!"
    scene 08_1098 with Dissolve(1)
    va "Uhm... Zach?"
    scene 08_1099 with Dissolve(1)
    z "{i}(This is it! The moment [mc] was talking about!){/i}"
    z "You're so beautiful, and I need to tell you something."
    z "I like you, Val."
    if Valeria_Points >= 7:
        scene 08_1100 with Dissolve(1)
        va "..."
        scene 08_1101 with Dissolve(1)
        va "..."
    else:
        scene 08_1100 with Dissolve(1)
        va "..."
    if Elena_Points >= 19:
        scene 08_1102 with Dissolve(1)
        el "It was really difficult, actually."
        mc "You did great but you do this daily. Minus the pushing part of course."
        mc "I expected a little..."
        el "Why don't you try it then?"
        scene 08_1103 with Dissolve(1)
        el "Hey! What are you doing?"
        mc "Trying it. Help me up here!"
        el "Haha, [mc]. Stop."
        scene 08_1104 with Dissolve(1)
        ""
        scene 08_1105 with Dissolve(1)
        el "I didn't see that coming. At all..."
        mc "Same."
        if Valeria_Points >= 7:
            mc "{i}(Good for him.){/i}"
            mc "{i}(Why do I feel jealous, though?){/i}"
        else:
            mc "{i}(Good for him.){/i}"
    else:
        mc "You did great anyway."
        el "Thanks."
        scene 08_1104 with Dissolve(1)
        el "I didn't see that coming. At all..."
        mc "Same."
        if Valeria_Points >= 7:
            mc "{i}(Good for him.){/i}"
            mc "{i}(Why do I feel jealous, though?){/i}"
        else:
            mc "{i}(Good for him.){/i}"
    scene black with Dissolve(1)
    pause 2
    scene 08_1106 with Dissolve(1)
    la "Hey."
    el "Hey. Sienna still not back?"
    la "No..."
    scene 08_1107 with Dissolve(1)
    la "Ew, you're wet!"
    el "Whose fault is that, huh?"
    la "Haha."
    scene 08_1108 with Dissolve(1)
    la "Did you have fun?"
    if Elena_Points >= 19:
        el "I did. I feel comfortable around [mc]. It's like we've known him a long time."
        la "I could see that."
        el "Sorry."
        la "Don't be. I'm happy you get along so great. A little jealous though."
        el "Haha. That's your fault. You gave me your spot."
        la "I know..."
    else:
        el "I did, thanks."
    scene 08_1109 with Dissolve(1)
    el "By the way. Did you see earlier?"
    la "Valeria and Zach?"
    el "Yeah!"
    la "Yeah. What was that?"
    el "Right? I didn't think she would..."
    scene 08_1110 with Dissolve(1)
    la "Congrats, Val!"
    va "What?"
    la "For winning. You did great. This one here had no chance!"
    el "Hey!"
    va "Thanks."
    scene 08_1111 with Dissolve(1)
    mc "I think you need to talk."
    z "Hehe, it's nothing, man."
    mc "It didn't look like nothing."
    scene 08_1112 with Dissolve(1)
    z "I told her I like her."
    mc "You did? What did she say?"
    z "Nothing yet. I think she was a bit embarrassed. Too many people here."
    z "I'll talk to her tomorrow after the competition, when we're alone."
    mc "Good."
    scene 08_1113 with Dissolve(1)
    mc "I've had enough of the pool. Let's get out of here."
    z "Yeah."
    mc "I'm happy for you!"
    scene 08_1114 with Dissolve(1)
    mc "If only there were some empty chairs so you didn't all have to share one."
    la "Haha. We're just gossiping and it's easier this way."
    scene 08_1115 with Dissolve(1)
    mc "I'll join you."
    el "Hey!"
    mc "I love me some gossip this time of year."
    la "Haha."
    scene 08_1116 with Dissolve(1)
    mc "Are you guys staying much longer, or...?"
    la "You're getting hungry?"
    mc "You know me well."
    la "Hehe."
    el "We're just going to dry up in the sun and then we can leave."
    mc "Sounds good."
    jump Week3_Friday_Evening

label Week3_Friday_Evening:
    scene black with Dissolve(1)
    pause 2
    scene 08_1117 with Dissolve(1)
    n "*Washing face*"
    scene 08_1118 with Dissolve(1)
    mc "{i}(It's been a while since I've been clean-shaven.){/i}"
    mc "{i}(Feels weird. I look so much younger.){/i}"
    mc "{i}(Maybe I'll keep it for a few weeks...){/i}"
    scene 08_1119 with Dissolve(1)
    play sound "Sounds/Phone_Vibrate.mp3"
    n "*Bzzzt. Bzzzt*"
    if Alexis_Dating == True:
        scene 08_1120 with Dissolve(1)
        mc "Hello?"
        a "Hi!"
        mc "Oh shit, Alexis!"
        scene 08_1121 with Dissolve(1)
        a "Oh shit, Alexis? Exactly what I wanted to hear..."
        mc "No-no-no. It was more like, shit, I totally forgot to call Alexis."
        a "Uh-huh."
        mc "I didn't mean..."
        mc "Sorry!"
        scene 08_1122 with Dissolve(1)
        mc "Hi, Lexi!"
        a "Heh... Hey."
        scene 08_1123 with Dissolve(1)
        a "Did I call you at an inappropriate time?"
        mc "No. Well... Not an inappropriate time, but maybe inappropriate in a different way."
        a "How so?"
        mc "Just showered. Sitting naked in the locker room."
        a "Mmm..."
        scene 08_1124 with Dissolve(1)
        mc "What's that 'mmm' for?"
        a "Two more days."
        mc "Haha. Counting the days already, huh? Miss me that much?"
        a "I'm not going to answer that."
        scene 08_1125 with Dissolve(1)
        mc "I will though."
        mc "I miss you. A lot!"
        scene 08_1126 with Dissolve(1)
        mc "It's loud there."
        a "It's Friday, and the game is on. So, lots of people are here."
        mc "Oh yeah, Marauders are playing today. What's the score?"
        a "..."
        scene 08_1127 with Dissolve(1)
        a "27-23."
        mc "To us, yes?"
        a "Yes. To... Us."
        scene 08_1128 with Dissolve(1)
        a "How was training? Last one before tomorrow's competition, right?"
        mc "Yeah. Training was good. We only had half a day. So we could relax in the afternoon."
        a "What did you do?"
        mc "Went to the pool with some friends."
        a "Fun!"
        scene 08_1129 with Dissolve(1)
        mc "Are you working the whole night?"
        a "I am. Dylan hired someone new who I have to show the ropes to."
        scene 08_1130 with Dissolve(1)
        mc "Is she cute?"
        a "..."
        mc "{i}(Why did I just ask that? Stupid, stupid question. I should stop hanging out with Zach so much.){/i}"
        a "Why does that even matter?"
        mc "{i}(Shit...){/i}"
        mc "Heh. Uhm... For the tips, maybe? If you're good looking, you'll probably get higher tips, no?"
        mc "{i}(I'm digging my own grave here. Just stop.){/i}"
        scene 08_1131 with Dissolve(1)
        a "Does that mean I'm not good looking? You never tipped me!"
        mc "..."
        mc "Because you paid for me."
        a "Oh, did I? Would you look at that."
        mc "..."
        scene 08_1132 with Dissolve(1)
        a "And to answer your question."
        a "Yes, he's handsome!"
        mc "He?"
        a "Yes! He!"
        mc "..."
        scene 08_1133 with Dissolve(1)
        mc "Sorry. I'm being stupid. Maybe too much sun today, I don't know. And to answer your question..."
        mc "You aren't just good looking. You're freakin' gorgeous, Lexi!"
        a "Haha, thanks."
        scene black with Dissolve(1)
        pause 2
        scene 08_1126 with Dissolve(1)
        a "Are you nervous about tomorrow?"
        mc "No, not yet. It will probably hit me once I'm in bed or when I wake up."
        mc "I'm trying not to think about it too much."
        scene 08_1134 with Dissolve(1)
        a "How about Lays? How is she?"
        mc "She's doing good. She didn't come across as nervous or anything."
        a "Can you watch her race or..."
        mc "Yeah, it's thirty minutes before mine. I'll be cheering for her."
        scene 08_1135 with Dissolve(1)
        a "That's sweet. Is it possible to maybe video the race?"
        a "I haven't seen her run in a long time and really want to see it."
        mc "Sure, I can record it."
        a "Thank you."
        scene 08_1136 with Dissolve(1)
        bt "Hey, sorry, Alexis."
        a "Yes?"
        bt "I think I typed something wrong in the register. Can you take a look?"
        a "Of course. Give me one sec."
        bt "Thanks."
        scene 08_1137 with Dissolve(1)
        mc "Was that the new guy?"
        a "Yes."
        mc "He even sounds handsome. Such a deep voice."
        a "He has a deep voice, yes."
        mc "Is he really good-looking?"
        scene 08_1138 with Dissolve(1)
        a "Haha."
        mc "What?"
        a "This is the first time you've seemed a little jealous."
        mc "..."
        a "I'm somewhat happy about it."
        scene 08_1139 with Dissolve(1)
        a "Anyway, I need to go."
        mc "Sorry that I forgot to call you."
        a "It's fine. You can make it up to me by calling tomorrow and telling me how your race went."
        mc "Will do."
        a "Bye, [mc]."
        mc "Bye, Lexi. And don't spend too much time with the new guy!"
        a "Haha. I won't. Bye."
    else:
        scene 08_1130 with Dissolve(1)
        mc "Hello?"
        x "Hello, sir. I'm reaching out to you concerning your car's extended warranty!"
        mc "Are you kidding me? Stop calling this number! I don't even own a car!"
        mc "{i}(I'll block this idiot.){/i}"
    jump Week3_Saturday

label Week3_Saturday:
    scene black with Dissolve(2)
    pause 2
    stop music fadeout 1.0
    play music ("Music/Indie-Electro 1.mp3", "Music/Indie-Electro 2.mp3", "Music/Indie-Electro 3.mp3", "Music/Indie-Electro 4.mp3") volume 0.2
    n "Saturday, 08:13. Competition day."
    scene 08_1140 with Dissolve(1)
    tm "I'm impressed with the progress you guys have made during the last few days of training."
    tm "I didn't make it easy for you, but you pushed through. Thank you for that."
    tm "I explained already that the results are very important, not only for your scores but also for your future. Read: Scholarship!"
    tm "There will be scouts from several colleges attending. If you want to impress someone. Today is the day."
    scene 08_1141 with Dissolve(1)
    tm "I have some more good news."
    tm "Because of our good times at training, we can have four boys and three girls run this year."
    tm "That will increase our chances of winning significantally!"
    scene black with Dissolve(1)
    pause 2
    scene 08_1142 with Dissolve(1)
    tm "Girls. You can start your warm-up routines to get ready for your race. That will be in exactly forty-six minutes."
    tm "Boys, you can relax a bit more or start preparing already for your race, which will be thirty minutes later."
    tm "I wish you all good luck. And I hope you will support each other!"
    tm "Come on. Let's do this!"
    scene 08_1143 with Dissolve(1)
    mc "I guess you need to get ready. How are you feeling?"
    la "*Sigh* Good. Nervous."
    mc "But excited?"
    la "Oh yeah."
    mc "How about you, Val?"
    scene 08_1144 with Dissolve(1)
    va "Same. Not really nervous though."
    la "You aren't? I wish I could be that calm."
    scene 08_1145 with Dissolve(1)
    la "Oh..."
    mc "What?"
    la "I don't know why I only just realised, but you shaved!"
    mc "Haha, I did, yeah."
    scene 08_1146 with Dissolve(1)
    mc "What do you think?"
    la "I don't know yet, you look so different. It's smooth though."
    la "Funny how a little hair can change your look so much."
    mc "{i}(A little hair...){/i}"
    la "Any specific reason?"
    scene 08_1147 with Dissolve(1)
    mc "{i}(I messed up while trimming...){/i}"
    mc "It's uh less weight. And as you said, it's smooth."
    mc "So it's much more aerodynamic, meaning I can run faster..."
    mc "{i}(That was the stupidest thing I've ever said.){/i}"
    scene 08_1148 with Dissolve(1)
    va "..."
    la "..."
    scene 08_1149 with Dissolve(1)
    va "Haha."
    la "Haha. He probably believes it too..."
    mc "Hey now. It was a joke!"
    scene 08_1150 with Dissolve(1)
    mc "Anyway. I'll leave you guys to it."
    mc "I'm gonna look for Elena and Sienna and we'll be cheering for you guys."
    menu:
        "Hug Layla[KoGa3AutoWTChange1]{size=-4}(Layla Points+2) {/size} {/color}":
            $ Layla_Points += 2
            # Layla (64)
            if Layla_Dating == True:
                scene 08_1151 with Dissolve(1)
                mc "Good luck, Layla! I know you'll do well."
                la "Thank you, [mc]. I'll do my best."
                scene 08_1152 with Dissolve(1)
                va "..."
            else:
                scene 08_1151 with Dissolve(1)
                mc "Good luck, Layla! I know you'll do well."
                la "Thank you, [mc]. I'll do my best."
            scene 08_1154 with Dissolve(1)
            mc "See you later."
            la "We'll be cheering for you when it's your turn."
            mc "Hehe, thanks."
            la "See you."
            va "Bye."
        "Hug Valeria[KoGa3AutoWTChange1]{size=-4}(Valeria Points+2, {i}Layla Dating: Layla Points-4{/i}) {/size} {/color}":
            $ Valeria_Points += 2
            # Valeria (10)
            if Layla_Dating == True:
                $ Layla_Points -= 4
            else:
                pass
            scene 08_1153 with Dissolve(1)
            mc "Good luck to you, Valeria!"
            va "Thank you!"
            scene 08_1154a with Dissolve(1)
            mc "See you later."
            la "See you."
            va "Bye."
            scene 08_1155 with Dissolve(1)
            la "What was that?"
            la "Why didn't I get a hug?"
        "Hug Both[KoGa3AutoWTChange1]{size=-4}(Valeria Points+2, Layla Points+2) {/size} {/color}":
            $ Valeria_Points += 2
            $ Layla_Points += 2
            # Layla (64)
            # Valeria (10)
            if Layla_Dating == True:
                scene 08_1151 with Dissolve(1)
                mc "Good luck, Layla! I know you'll do well."
                la "Thank you, [mc]. I'll do my best."
                scene 08_1152 with Dissolve(1)
                va "..."
            else:
                scene 08_1151 with Dissolve(1)
                mc "Good luck, Layla! I know you'll do well."
                la "Thank you, [mc]. I'll do my best."
            scene 08_1153 with Dissolve(1)
            mc "Good luck to you, too, Valeria!"
            va "Thank you!"
            scene 08_1154 with Dissolve(1)
            mc "See you later."
            la "We'll be cheering for you when it's your turn."
            mc "Hehe, thanks."
            la "See you."
            va "Bye."
        "Leave[KoGa3AutoWTChange1]{size=-4}({i}Layla Dating: Layla Points-2{/i}) {/size} {/color}":
            if Layla_Dating == True:
                $ Layla_Points -= 2
            else:
                pass
            scene 08_1154 with Dissolve(1)
            mc "Good luck both of you. See you later."
            la "We'll be cheering for you when it's your turn."
            mc "Hehe, thanks."
            la "See you."
            va "Bye."
    scene black with Dissolve(1)
    pause 2
    scene 08_1156 with Dissolve(1)
    mc "Finally! What took you so long?"
    el "Sorry, sorry. We had to make some preparations first."
    menu:
        "Check her out[KoGa3AutoWTChange1]{size=-4}({i}Elena Points > 19: Elena Points-2{/i}) {/size} {/color}":
            if Elena_Points >= 19:
                scene black with Dissolve(1)
                transform moveup:
                    xalign 0.5 yalign 1.0
                    linear 5.0 yalign 0.0
                show 08_1157 at moveup
                pause 3
                el "What?"
                mc "It's the cheerleader outfit."
                el "What about it?"
                mc "Nothing. Just... You look cute in it."
                el "Thanks?"
                scene 08_1158 with Dissolve(1)
                mc "Where are your pompoms?"
                el "Sorry, I forgot to bring them."
                mc "And here I was hoping we could do some sort of cheer routine for Layla. Dammit..."
                el "Uh-huh. You and cheering..."
            else:
                $ Elena_Points -= 2
                scene black with Dissolve(1)
                transform moveup:
                    xalign 0.5 yalign 1.0
                    linear 5.0 yalign 0.0
                show 08_1157 at moveup
                pause 3
                el "What?"
                mc "It's the cheerleader outfit."
                el "Really?"
            menu:
                "Cheer[KoGa3AutoWTChange1]{size=-4}(Elena Points+2) {/size} {/color}":
                    $ Elena_Points += 2
                    # Elena (26)
                    scene 08_1159 with Dissolve(1)
                    mc "Yeah. Something like. L A Y L A. GOOOO LAYLA!"
                    el "Dios mío. Don't ever do that again!"
                    mc "Haha."
                    scene 08_1160 with Dissolve(1)
                    si "I think you did great, [mc]."
                    el "Don't encourage him."
                    mc "Thank you, Sienna! At least someone appreciates my cheers."
                    el "It's not a cheer..."
                    scene 08_1161 with Dissolve(1)
                    mc "It's a chant? Haha. That was so bad."
                    el "Indeed. Hopefully, we don't have to listen to that on the way back."
                    mc "Unlikely. They aren't even playing the finale."
                    scene 08_1162 with Dissolve(1)
                    el "Where is he anyway?"
                    mc "I have no idea. I thought he'd be the first to arrive."
                    tj "Hey, isn't that that famous agent?"
                "Sit down":
                    scene 08_1162 with Dissolve(1)
                    el "Where's Zach. Didn't he say he'd support Valeria?"
                    mc "I have no idea. I thought he'd be the first to arrive."
                    tj "Hey, isn't that that famous agent?"
        "Sit down":
            scene 08_1162 with Dissolve(1)
            el "Where's Zach. Didn't he say he'd support Valeria?"
            mc "I have no idea. I thought he'd be the first to arrive."
            tj "Hey, isn't that that famous agent?"
    scene 08_1163 with Dissolve(1)
    da "Where?"
    tj "Over there. Talking to Coach."
    scene 08_1164 with Dissolve(1)
    da "Oh damn! It is."
    tj "Why would he be here at this event?"
    da "To scout and sign me, of course!"
    mc "..."
    da "This pumps me up even more."
    scene black with Dissolve(1)
    pause 2
    scene 08_1165 with Dissolve(1)
    mc "Oh, there they are."
    el "She doesn't look as nervous as last year."
    scene 08_1166 with Dissolve(1)
    el "GO LAYLA! You can do it!"
    scene 08_1167 with Dissolve(1)
    mc "Finally!"
    z "I'm still on time? They didn't run yet, right?"
    mc "No, they didn't, but they're about to start."
    scene 08_1168 with Dissolve(1)
    mc "What took you so long?"
    z "Warm-up, and Coach kept on talking."
    z "I had to practically beg him to come here for five minutes."
    z "So I can't stay. I'll just watch and then I'll have to go back."
    scene 08_1169 with Dissolve(1)
    z "VAL! Go beat those bitches!"
    mc "Dude..."
    scene 08_1170 with Dissolve(1)
    la "Did he just call us bitches?"
    va "..."
    scene 08_1171 with Dissolve(1)
    to "Would you look at that. They gave me lane number one."
    to "Seems like they already know who's going to win."
    sc "..."
    scene 08_1172 with Dissolve(1)
    to "What are you doing here anyway?"
    to "Failed to get into college?"
    sc "If you must know, I..."
    to "No... Don't really care. It won't change the outcome anyway."
    scene 08_1173 with Dissolve(1)
    el "Who do you think will win?"
    el "Does Layla have a chance?"
    mc "I have no idea, to be honest. She's beaten Tori at training a few times. But a competition is always different. Lots of nerves and adrenaline involved."
    mc "And I don't know how good the girls from the other schools are."
    if Layla_Week3_Tuesday_Train == True:
        scene 08_1174 with Dissolve(1)
        z "Haha."
        z "What's Layla doing? Is she dancing?"
        scene 08_1175 with Dissolve(1)
        mc "That's her new warm-up routine."
        z "That's a warm-up? Damn! It's pretty sexy..."
        mc "Right?"
    else:
        pass
    scene black with Dissolve(1)
    pause 2
    if Alexis_Dating == True:
        scene 08_1176 with Dissolve(1)
        z "Oooh, they're getting ready."
        z "I'm probably more nervous than they are."
        mc "Haha. That might be true."
        scene 08_1176a with Dissolve(1)
        mc "Before I forget, let me video this."
        z "Oh, that's a good idea."
        z "Can you film Val too?"
        mc "Sure, she's running next to Layla. So, she'll be in it anyway."
        z "Cool."
    else:
        scene 08_1176 with Dissolve(1)
        z "Oooh, they're getting ready."
        z "I'm probably more nervous than they are."
        mc "Haha. That might be true."
    scene 08_1177 with Dissolve(1)
    an "READY!"
    scene 08_1178 with Dissolve(1)
    an "SET!"
    mc "{i}(She's the winner from last year. Let's see what she's got.){/i}"
    scene 08_1179 with Dissolve(1)
    n "*BANG*"
    scene 08_1180 with Dissolve(1)
    el "Go, Layla!"
    z "Faster, Valeria! Faster!"
    scene 08_1181 with Dissolve(1)
    mc "..."
    z "What the fuck?"
    scene 08_1182 with Dissolve(1)
    mc "She's on a whole different level..."
    z "Yeah... So fast!"
    scene 08_1183 with Dissolve(1)
    z "Wait... Wait!"
    z "Val is catching up!"
    scene 08_1184 with Dissolve(1)
    z "GO, VAL!"
    z "She can do it. This is going to be so close."
    scene 08_1185 with Dissolve(1)
    mc "..."
    scene 08_1186 with Dissolve(1)
    z "Who won? Who freakin' won?"
    mc "Val might have just caught her at the finish."
    scene 08_1187 with Dissolve(1)
    an "Lane two. Sha'Carri Evans."
    z "Oh, come on. That must be a mistake."
    scene 08_1188 with Dissolve(1)
    va "Congratulations!"
    sc "You did great, girl!"
    va "Thanks. If you didn't slow down the last twenty meters, it wouldn't have been close at all, though."
    to "..."
    scene black with Dissolve(2)
    pause 2
    if Layla_Dating == False:
        scene 08_1189 with Dissolve(1)
        la "Haha."
        el "Hey."
        mc "Congrats, Layla!"
        la "Thank you, thank you!"
        z "Why are you so happy? You didn't even win!"
    else:
        scene 08_1190 with Dissolve(1)
        la "Haha."
        mc "Hey."
        el "Congrats, Layla!"
        la "Thank you, thank you!"
        z "Why are you so happy? You didn't even win!"
    scene 08_1191 with Dissolve(1)
    la "Last year I was sixth, this year I'm fourth. That's a win for me."
    z "Hmm, fair enough."
    scene 08_1192 with Dissolve(1)
    z "I'm going to congratulate Valeria, and after that, I have to run to get to my game."
    z "Good luck, [mc]! And if you still have time after your race, come watch us."
    mc "Thank you. Will do."
    z "And congrats, Layla."
    la "Thanks, Zach."
    scene 08_1193 with Dissolve(1)
    z "Congratulations, Valeria!"
    va "Thanks."
    z "You were amazing and I actually think you won that."
    z "They surely made a mistake. Shall we ask to see the video?"
    va "She won, Zach. And can you put me down, please!"
    scene 08_1194 with Dissolve(1)
    z "No. I like having you in my arms."
    va "Zach! I asked you to put me down!"
    scene 08_1195 with Dissolve(1)
    z "What are you mad at me for now?"
    z "You don't have to take it out on me just because you lost."
    va "..."
    sn "Are you alright?"
    va "Yes!"
    scene black with Dissolve(1)
    pause 2
    scene 08_1196 with Dissolve(1)
    la "I guess it's your turn now."
    mc "Indeed. Going to do my last warm-up and it's go-time."
    la "Are you nervous?"
    mc "Actually no. Which is a little weird."
    la "Haha. I was the complete opposite."
    if Layla_Dating == False:
        scene 08_1197 with Dissolve(1)
        mc "Anyway, see you guys later."
        el "We'll be here, cheering for you."
        mc "Thank you!"
    else:
        scene 08_1197 with Dissolve(1)
        mc "Anyway, see you guys later."
        el "We'll be here, cheering for you."
        mc "Thank you!"
        if Elena_Points >= 21:
            scene 08_1198 with Dissolve(1)
            la "And here's a little something for luck!"
            mc "Thanks."
            scene 08_1199 with Dissolve(1)
            el "Here's some more luck if you want a better placement than fourth."
            la "Hey! That's so mean."
            mc "Haha. Thanks, Elena!"
        else:
            scene 08_1198 with Dissolve(1)
            la "And here's a little something for luck!"
            mc "Thanks."
    scene black with Dissolve(1)
    pause 2
    scene 08_1200 with Dissolve(1)
    la "Hey. Congratulations. Second place!"
    va "Thank you. You did great too."
    la "Thanks."
    el "I had no idea you were that fast."
    scene 08_1201 with Dissolve(1)
    la "It was so close. Just a little more and you had her."
    va "No. She slowed down at the end to conserve some energy. She told me she'll also be running the 200m later on."
    va "If she'd gone all out, it wouldn't have been close at all."
    scene 08_1202 with Dissolve(1)
    la "*Sigh* Now I don't feel that great anymore about my fourth place. I thought I was catching up to her compared to last year."
    la "That's the number one in the nation for you, I guess..."
    el "You all did great though. Second to fourth place all came from our school. That's really good!"
    scene black with Dissolve(1)
    pause 2
    scene 08_1203 with Dissolve(1)
    mc "..."
    scene 08_1204 with Dissolve(1)
    to "Hey Darryl!"
    to "Win or lose. You know you've got me."
    scene 08_1205 with Dissolve(1)
    to "But if you win today, you get her too!"
    da "If I win?"
    da "Look at these chumps. It's not a question of if, but of how much."
    to "You'd better show us then. We'll be waiting!"
    scene 08_1206 with Dissolve(1)
    da "Not that I needed more motivation."
    da "We'll have a good time later!"
    da "And Jasmine. Keep wearing that outfit. You look damn fine!"
    scene 08_1207 with Dissolve(1)
    x "Look it's the guy from the pool. He's on Madison Springs' track team."
    if Week3_Friday_TC_Kickball == True:
        sc "The one who kicked our ball away?"
        x "Yeah, I saw him earlier here in the stands."
        x "He was looking at you."
        sc "Don't care."
    else:
        sc "The one you have a crush on?"
        x "Yeah, I saw him earlier here in the stands."
        x "He was looking at you, though."
        sc "Was he?"
        x "Uh-huh."
        scene 08_1208 with Dissolve(1)
        sc "Hmm..."
        sc "Let's see what he's got."
    scene 08_1209 with Dissolve(1)
    mc "{i}(He's still here. So, he's watching our race too.){/i}"
    mc "..."
    mc "{i}(Why am I getting nervous all of a sudden?){/i}"
    scene black with Dissolve(1)
    pause 2
    stop music fadeout 1.0
    play music "Music/Race.mp3" volume 0.5
    scene 08_1210 with Dissolve(1)
    mc "{i}(I can do this.){/i}"
    mc "{i}(I can do this!){/i}"
    scene 08_1211 with Dissolve(1)
    la "I'm more nervous than I was for my own race."
    el "It's the first time I've really gotten to watch him run. Well, except for a race against Darryl at school."
    el "Can he win?"
    la "I hope so..."
    scene 08_1212 with Dissolve(1)
    an "Ready!"
    an "Set!"
    if Layla_Week3_Tuesday_Train == False:
        $ Tori_End = True
        $ ShaCarri_End = True
        scene 08_1213 with Dissolve(1)
        n "*BANG*"
        scene 08_1215 with Dissolve(1)
        la "Oh no..."
        la "He had a bad start."
        scene 08_1217 with Dissolve(1)
        la "Come on, [mc]. You can still catch up!"
        la "Go, go!"
        scene 08_1218 with Dissolve(1)
        mc "{i}(Fuck, what a terrible start...){/i}"
        scene 08_1220 with Dissolve(1)
        mc "{i}(Is he faster than at training? I'm not getting closer at all.){/i}"
        mc "{i}(Even seems like he's pulling away more.){/i}"
        scene 08_1222 with Dissolve(1)
        if Week3_Friday_TC_Kickball == True:
            sc "How disappointing."
            sc "Used up all his energy when he kicked the ball away, huh?"
        else:
            sc "How disappointing."
        scene 08_1223 with Dissolve(1)
        mc "..."
        scene 08_1225 with Dissolve(1)
        da "Easiest win of my life!"
        an "Lane four. Darryl Bridges."
        mc "{i}(*Sigh*){/i}"
        mc "{i}(Now he'll be even more annoying. Fuck...){/i}"
        stop music fadeout 1.0
        play music ("Music/Indie-Electro 3.mp3", "Music/Indie-Electro 4.mp3", "Music/Indie-Electro 1.mp3", "Music/Indie-Electro 2.mp3") volume 0.2
        scene 08_1227 with Dissolve(1)
        el "That wasn't good, right?"
        la "No..."
        el "What place did he finish?"
        la "Third or fourth, I think."
        va "Fourth."
        scene 08_1239 with Dissolve(1)
        to "I knew you could do it, babe."
        da "Like I said earlier. It was never a question of if."
        scene 08_1240 with Dissolve(1)
        to "What are you looking at?"
        to "Move along, loser!"
        mc "..."
        menu:
            "Comment":
                scene 08_1241 with Dissolve(1)
                mc "Like you won your race, Victoria!"
                to "It's Tori!"
                da "You heard her. Use your legs for once!"
                scene 08_1242 with Dissolve(1)
                x "That was an impressive run, Darryl!"
                da "Thank you."
                x "Let me introduce myself."
                to "I'll let you talk to this handsome gentleman!"
            "Walk away":
                scene 08_1242 with Dissolve(1)
                x "That was an impressive run, Darryl!"
                da "Thank you."
                x "Let me introduce myself."
                to "I'll let you talk to this handsome gentleman!"
        scene 08_1243 with Dissolve(1)
        to "Come find us later."
        to "Your little surprise will be waiting."
        scene 08_1244 with Dissolve(1)
        sn "You need to work on your start. Lengthen your first three steps and you'll do fine."
        mc "Uh... Thanks."
        scene black with Dissolve(1)
        pause 2
        scene 08_1250 with Dissolve(1)
        la "Are you okay?"
        mc "Yeah. Just not that happy with the result."
        mc "I messed up the start again."
        scene 08_1251 with Dissolve(1)
        mc "Seriously... How many times can you make the same mistake before you learn?"
        mc "*Sigh*"
        mc "Fourth place... What a joke!"
        scene 08_1252 with Dissolve(1)
        la "Hey! I also ended fourth!"
        mc "Yeah, but your fourth place is good since there were lots of good runners."
        mc "In my case, there was only Darryl. I should've beaten TJ and that other dude at least."
        if Layla_Week1_Monday_Payattention == True:
            scene 08_1253 with Dissolve(1)
            el "Hey, cheer up. At least you guys can create the fourth-place-club now."
            la "Haha. True!"
        else:
            scene 08_1253 with Dissolve(1)
            el "Hey, cheer up. At least you guys can create the fourth-place-club now."
            la "Haha. True!"
            scene 08_1254 with Dissolve(1)
            mc "Yeah... And what's up with that number four? If follows me wherever I go."
            mc "You jinxed me!"
            la "Haha. I did no such thing."
        scene 08_1255 with Dissolve(1)
        la "Well, we should get going to your competition, right?"
        el "Yeah, we need to start our warm-up."
        si "I'll go get Jasmine."
        el "Thanks."
        scene 08_1256 with Dissolve(1)
        el "Are you coming with us, Val?"
        va "I'd love to, but I promised Zach I'd watch his game, so I'm going there first."
        el "All good."
        va "But if there's still time, I'll come to join you."
        el "Cool."
        scene 08_1257 with Dissolve(1)
        el "How about you, [mc]?"
        mc "I'll come."
        el "Good, because you promised to cheer for us!"
        mc "Haha. I hoped you'd forget that."
        el "Never!"
        scene 08_1258 with Dissolve(1)
        mc "But I'll come a bit later. I need to talk to Coach first."
        el "Alright. See you later, then."
        scene black with Dissolve(1)
        pause 2
        scene 08_1259 with Dissolve(1)
        mc "{i}(Seems I'm not the only one who needs to talk to Coach.){/i}"
        mc "{i}(Guess I'll do it later.){/i}"
        jump Week3_Saturday_Gabi
    else:
        $ MC_Week3_Saturday_TC_Win = True
        if Week3_Friday_TC_Kickball == True:
            $ ShaCarri_End = True
        else:
            pass
        scene 08_1214 with Dissolve(1)
        n "*BANG*"
        scene 08_1216 with Dissolve(1)
        la "He had a really good start."
        scene 08_1217 with Dissolve(1)
        la "Come on, [mc]. You can win this!"
        la "Go, go!"
        scene 08_1219 with Dissolve(1)
        mc "{i}(Alright. Good start. Let's finish this.){/i}"
        scene 08_1221 with Dissolve(1)
        mc "{i}(We're still head-to-head.){/i}"
        mc "{i}(Why can't I seem to pull ahead?){/i}"
        mc "{i}(Was he holding back at training? He's faster than before.){/i}"
        scene 08_1222 with Dissolve(1)
        sc "Hmm... Finally some competition for Darryl."
        scene 08_1224 with Dissolve(1)
        ""
        scene 08_1226 with Dissolve(1)
        x "Now that was much more interesting than I'd expected."
        x "Lane three wasn't here last year, right?"
        sn "He wasn't."
        x "Guess I'll be talking to three people today."
        scene 08_1228 with Dissolve(1)
        la "Did he win? He won, right?"
        el "I think so."
        an "Lane three. [mc] Moreno."
        scene 08_1229 with Dissolve(1)
        stop music fadeout 1.0
        play music ("Music/Indie-Electro 2.mp3", "Music/Indie-Electro 4.mp3", "Music/Indie-Electro 1.mp3", "Music/Indie-Electro 3.mp3") volume 0.2
        la "Yay! He did it."
        el "Hey, watch out. Haha."
        scene 08_1230 with Dissolve(1)
        la "I'm going to go congratulate him."
        el "I'm sure he'll join us, but go ahead, we'll wait here."
        if Layla_Dating == False:
            scene 08_1231 with Dissolve(1)
            la "You did it!"
            mc "Haha. I did it!"
            da "..."
            scene 08_1232 with Dissolve(1)
            la "Congratulations! You were amazing!"
            mc "Thank you, thank you."
            scene 08_1233 with Dissolve(1)
            la "How does it feel to win?"
            mc "Incredible. I didn't think I had a chance but my smooth-face theory worked."
            la "Haha. Of course, that's the reason."
            mc "Or it's because I trained with you."
            la "That's more likely."
            scene 08_1245 with Dissolve(1)
            da "Hey Tori. Where are you going? Are we still on for later?"
            to "You didn't win... Get lost, loser!"
            da "Bitch!"
            scene 08_1246 with Dissolve(1)
            x "Excuse me. Do you mind if I talk to your boyfriend for a minute?"
            la "My boy... Uh... He... I mean. Yeah, sorry."
            x "Thank you."
        else:
            scene 08_1234 with Dissolve(1)
            la "Congratulations!"
            mc "Be careful!"
            scene 08_1235 with vpunch
            mc "..."
            scene 08_1236 with Dissolve(1)
            mc "You alright?"
            la "Haha, yeah. Sorry."
            mc "By the way. You just ran that hundred meters faster than your actual race!"
            la "Very funny!"
            scene 08_1237 with Dissolve(1)
            la "Anyway. Congratulations!"
            mc "Thank you, thank you."
            la "How does it feel to win?"
            mc "Incredible. I didn't think I had a chance, but my smooth-face theory worked."
            scene 08_1238 with Dissolve(1)
            la "Haha. Of course that's the reason."
            mc "Or it's because I trained with you."
            la "That's more likely."
            scene 08_1245 with Dissolve(1)
            da "Hey Tori. Where are you going? Are we still on for later?"
            to "You didn't win... Get lost, loser!"
            da "Bitch!"
            scene 08_1247 with Dissolve(1)
            x "Excuse me. I'm sorry for interrupting."
            x "Do you mind if I talk to your boyfriend for a minute?"
            la "My boy... Uh... He... I mean. Yeah, sorry."
            x "Thank you."
        scene 08_1248 with Dissolve(1)
        la "I'll leave you two then."
        la "We're heading towards the field where Elena and Sienna's cheerleading competition will be."
        mc "Which one is that?"
        la "The one we used for our training."
        mc "Ah okay, I'll join you guys later."
        la "Alright."
        scene 08_1249 with Dissolve(1)
        la "*Whisper* Good luck!"
        mc "Thank you."
        scene black with Dissolve(1)
        pause 2
        scene 08_1260 with Dissolve(1)
        to "Hey there."
        mc "Heh... What do you want, Tori?"
        to "What? Can't I congratulate you?"
        mc "..."
        scene 08_1261 with Dissolve(1)
        to "So, congratulations! You did great!"
        menu:
            "Stop":
                scene 08_1262 with Dissolve(1)
                mc "Just stop, Tori."
                mc "I know what you're doing, and it's not going to work."
                to "No one needs to know."
                mc "Uh-huh. Everyone knows... You even keep a list. Just leave me alone."
                scene 08_1263 with Dissolve(1)
                to "You think you're so much better than me?"
                mc "Trust me. I'm not. Just not interested."
                mc "How about you go console Darryl instead?"
                to "Funny..."
                jump Week3_Saturday_Gabi
            "Thank her":
                mc "Thank you."
                to "You even got the attention of the MSU scout."
                mc "How do you know he was from MSU?"
                to "I have my connections..."
                scene 08_1264 with Dissolve(1)
                mc "What are you doing? Don't you have to console Darryl or something?"
                to "Haha. Funny, but I have a much better idea."
                to "So... Much... Better!"
                menu:
                    "No thanks":
                        scene 08_1262 with Dissolve(1)
                        mc "Not interested, Tori."
                        mc "I know what you're doing, and it's not going to work."
                        to "No one needs to know."
                        mc "Uh-huh. Everyone knows... You even keep a list. Just leave me alone."
                        scene 08_1263 with Dissolve(1)
                        to "You think you're so much better than me?"
                        mc "Trust me. I'm not."
                        to "..."
                        jump Week3_Saturday_Gabi
                    "Go with her":
                        jump Week3_Saturday_Tori

label Week3_Saturday_Tori:
    if _in_replay:
        $ Tori_Week3_Wednesday_TC_Fun = True
        $ Tori_Points = 14
        $ Valeria_Points = 6
        $ SexCounter_Tori = 1
        $ MC_SexCounter = 1
    $ Tori_Sex = True
    $ MC_Week3_Saturday_TC_Cheer_Late = True
    $ Tori_Week3_Saturday_TC_Sex = True
    $ SexCounter_Tori += 1
    $ MC_SexCounter += 1
    $ Tori_Points += 2
    # Tori (16)
    stop music fadeout 1.0
    play music ("Music/LoFi Upbeat 1.mp3", "Music/LoFi Upbeat 2.mp3", "Music/LoFi Upbeat 3.mp3", "Music/LoFi Upbeat 4.mp3") volume 0.2
    scene 08_1265 with Dissolve(1)
    mc "Oh... I like that!"
    mc "What do you have in mind?"
    to "Follow me and find out."
    scene 08_1266 with Dissolve(1)
    mc "Do I get the same prize you offered to Darryl?"
    to "Haha. You're not ready for that!"
    mc "..."
    scene black with Dissolve(1)
    pause 2
    scene 08_1267 with Dissolve(1)
    to "Look at that. No one here."
    mc "As if that would've stopped us."
    to "Mmm-mmm. I'm starting to like you."
    scene 08_1268 with Dissolve(1)
    if Tori_Week3_Wednesday_TC_Fun == False:
        to "Show me what you've got."
        scene 08_1269 with Dissolve(1)
        to "Good start."
    else:
        to "How about you continue with what you started during training?"
        scene 08_1269 with Dissolve(1)
        mc "You liked that, huh?"
    scene 08_1270 with Dissolve(1)
    mc "{i}(I hope they taste as good as they look.){/i}"
    scene 08_1271 with Dissolve(1)
    ""
    scene 08_1272 with Dissolve(1)
    ""
    scene 08_1273 with Dissolve(1)
    to "..."
    scene 08_1274 with Dissolve(1)
    to "Okay, okay. I'll stop you there. What do you think you're doing?"
    mc "Kissing you. I don't know, what does it feel like?"
    to "No-no-no... We're not doing that."
    to "You're here to eat my pussy and fuck me! That's it!"
    mc "Heh. Sure..."
    scene 08_1275 with Dissolve(1)
    mc "Eating pussy and fucking?"
    mc "Let's get rid of these then."
    scene 08_1276 with Dissolve(1)
    ""
    scene 08_1277 with vpunch
    to "Aaah..."
    mc "What? You wanted me to eat your pussy."
    scene 08_1278 with Dissolve(1)
    to "I've misjudged you."
    to "I told you we should've done this earlier!"
    to "Continue!"
    scene 08_1279 with Dissolve(1)
    mc "{i}(I don't know what turns me on more...){/i}"
    mc "{i}(Tori, or this position...){/i}"
    scene 08_1280 with Dissolve(1)
    mc "{i}(I'm so hard.){/i}"
    menu:
        "Lick her ass[KoGa3AutoWTChange1]{size=-4}(Tori Week3 Saturday TC LickAss, Tori LickAss) {/size} {/color}":
            $ Tori_Week3_Saturday_TC_LickAss = True
            $ Tori_LickAss = True
            mc "{i}(Let's see how she likes this...){/i}"
            scene 08_1283 with Dissolve(1)
            to "That's not my..."
            to "Never mind, keep going!"
            scene 08_1284 with Dissolve(1)
            ""
        "Eat her pussy":
            scene 08_1281 with Dissolve(1)
            to "*Moaning*"
            scene 08_1282 with Dissolve(1)
            to "Oh yeah..."
    scene 08_1285 with Dissolve(1)
    to "FUCK!"
    mc "{i}(I think she's cumming the way she's choking me.){/i}"
    mc "{i}(Damn, she has strong legs...){/i}"
    scene black with Dissolve(1)
    pause 2
    scene 08_1286 with Dissolve(1)
    to "I thought you were only good at track, but damn... You've got some other skills too."
    mc "There are lots of things you don't know about me."
    to "Yeah. Let's keep it that way! I'm not interested in your life story!"
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 08_1287 at moveup
    pause 3
    mc "{i}(She's so hot. If only she wasn't such a bitch all the freakin' time...){/i}"
    scene 08_1288 with Dissolve(1)
    to "What are you waiting for?"
    to "Take your pants off and come get your prize!"
    scene 08_1289 with Dissolve(1)
    to "Put it in already and fuck me!"
    scene 08_1290 with Dissolve(1)
    ""
    scene 08_1291 with Dissolve(1)
    ""
    scene 08_1293 with Dissolve(1)
    $ achievement.grant("ACHIEVEMENT_VICTORI")
    $ achievement.sync()
    to "I'm not some porcelain doll. Hit it like you mean it!"
    scene 08_1292 with Dissolve(1)
    to "Ah..."
    mc "You asked for it!"
    show 08_1294
    to "Yes! Harder!"
    to "Harder!"
    show 08_1294a
    to "Mmm... Fuck!"
    scene 08_1295 with Dissolve(1)
    to "*Moaning*"
    scene black with Dissolve(1)
    pause 2
    scene 08_1296 with Dissolve(1)
    ""
    scene 08_1297 with Dissolve(1)
    ""
    scene 08_1298 with Dissolve(1)
    ""
    scene 08_1299 with Dissolve(1)
    to "Aaah..."
    scene 08_1300 with Dissolve(1)
    to "*Heavy breathing*"
    to "Keep going..."
    scene 08_1302 with Dissolve(1)
    ""
    scene 08_1303 with Dissolve(1)
    ""
    show 08_1304
    ""
    scene 08_1305 with Dissolve(1)
    to "Tell me when you're close. I'll finish you off myself!"
    mc "Someone wants a taste of victory!"
    to "Heh... He's got jokes too."
    scene black with Dissolve(1)
    pause 2
    scene 08_1306 with Dissolve(1)
    mc "What are you doing?"
    to "Don't worry, you'll stay hard even without me having my tits out."
    mc "I don't care. Get them back out!"
    scene 08_1307 with Dissolve(1)
    to "So demanding!"
    scene 08_1308 with Dissolve(1)
    to "Just remember. I'm holding your cock now, I'm in charge!"
    scene 08_1309 with Dissolve(1)
    ""
    scene 08_1310 with Dissolve(1)
    ""
    scene 08_1312 with Dissolve(1)
    mc "{i}(This feels so good!){/i}"
    scene 08_1313 with Dissolve(1)
    mc "{i}(I can't hold it much longer...){/i}"
    mc "{i}(She wants a taste, so...){/i}"
    scene 08_1314 with Dissolve(1)
    mc "Ahhh..."
    to "..."
    scene 08_1315 with Dissolve(1)
    mc "You got a little bit of..."
    scene 08_1316 with Dissolve(1)
    to "Mmm..."
    mc "{i}(She's crazy! But also a very good fuck!){/i}"
    scene black with Dissolve(1)
    pause 2
    scene 08_1317 with Dissolve(1)
    to "Well, that wasn't too bad."
    to "Top ten."
    mc "What? Only top ten? Guess I'll have to show you something different next time."
    scene 08_1318 with Dissolve(1)
    to "Heh... Who says there'll be a next time?"
    mc "Don't act like you didn't like it!"
    to "I had fun. Bye now."
    mc "..."
    mc "Yeah. Bye!"
    mc "{i}(I'd better hurry now to watch the cheer competition.){/i}"
    mc "{i}(But a quick bathroom break first.){/i}"
    $ renpy.end_replay()
    jump Week3_Saturday_Gabi

label Week3_Saturday_Gabi:
    scene black with Dissolve(2)
    pause 2
    stop music fadeout 1.0
    play music ("Music/LoFi Upbeat 1.mp3", "Music/LoFi Upbeat 2.mp3", "Music/LoFi Upbeat 3.mp3", "Music/LoFi Upbeat 4.mp3") volume 0.2
    if MC_Week3_Saturday_TC_Win == False:
        scene 08_1319 with Dissolve(1)
        mc "{i}(Damn... Fourth place... This is so bad.){/i}"
        mc "{i}(I hoped I'd be top three at least.){/i}"
        if Alexis_Dating == True:
            mc "{i}(Now I'm ashamed to call Mom. Or Alexis, even...){/i}"
        else:
            mc "{i}(Now I'm even ashamed to call Mom...){/i}"
        scene 08_1320 with Dissolve(1)
        mc "{i}(Shit! It's that late already? How long have I been sitting here?){/i}"
        mc "{i}(Time to stop my self-pity and head to the field.){/i}"
        scene 08_1321 with Dissolve(1)
        x "ARE YOU KIDDING ME?"
        mc "{i}(Who was that?){/i}"
    else:
        scene 08_1322 with Dissolve(1)
        mc "{i}(Shit! It's that late already?){/i}"
        mc "{i}(I'd better hurry, or I'll miss the whole cheer competition.){/i}"
        scene 08_1323 with Dissolve(1)
        x "ARE YOU KIDDING ME?"
        mc "{i}(Who was that?){/i}"
    menu:
        "Go to the field[KoGa3AutoWTChange1]{size=-4}(Gabi End) {/size} {/color}":
            $ Gabi_End = True
            mc "{i}(I don't have time for this.){/i}"
            jump Week3_Saturday_Cheer
        "Check it out":
            scene 08_1324 with Dissolve(1)
            tr "And you've left already?"
            if Gabi_End == True:
                mc "{i}(Oh... It's just Gabi. Whatever.){/i}"
                mc "{i}(It's not really my business, anyway.){/i}"
                jump Week3_Saturday_Cheer
            else:
                mc "{i}(Oh... It's Gabi.){/i}"
                mc "{i}(Who is she talking to?){/i}"
                scene 08_1325 with Dissolve(1)
                tr "Why didn't you tell me you were coming?"
                tr "..."
                tr "You knew that before..."
                scene 08_1326 with Dissolve(1)
                tr "And then you just leave without saying anything?"
                tr "..."
                tr "You could've surprised me, or at the very least come say hello."
                scene 08_1327 with Dissolve(1)
                tr "No time? NO TIME?"
                tr "You couldn't spare two minutes?"
                tr "..."
                tr "Do you even care about me?"
                scene 08_1328 with Dissolve(1)
                tr "ANSWER ME!"
                mc "{i}(Shit, this sounds serious.){/i}"
                scene 08_1329 with Dissolve(1)
                mc "{i}(Glad this doesn't have anything to do with me this time!){/i}"
                mc "{i}(I feel kinda bad for her, though.){/i}"
                menu:
                    "Go to the field":
                        mc "{i}(But I don't have time. Let's hurry now.){/i}"
                        jump Week3_Saturday_Cheer
                    "Check up on her":
                        jump Week3_Saturday_Gabi_Sex

label Week3_Saturday_Gabi_Sex:
    if _in_replay:
        $ SexCounter_Gabi = 1
        $ MC_SexCounter = 1
    scene 08_1330 with Dissolve(1)
    mc "Ms Ramirez?"
    mc "..."
    scene 08_1331 with Dissolve(1)
    mc "Gabi?"
    mc "Are you okay?"
    tr "..."
    scene 08_1332 with Dissolve(1)
    tr "Did you hear?"
    mc "Uhm..."
    mc "{i}(I'd better not tell her I was eavesdropping.){/i}"
    mc "No. I just came past and saw you sitting here."
    scene 08_1333 with Dissolve(1)
    tr "*Sigh* I'm fine."
    mc "Okay..."
    mc "{i}(I really don't know what to say.){/i}"
    mc "{i}(Why did I even come here? I think I should just leave.){/i}"
    scene 08_1334 with Dissolve(1)
    mc "I'll be leaving, then."
    mc "Bye, Ms Ramirez."
    tr "..."
    scene 08_1335 with Dissolve(1)
    tr "If you don't care, I don't care anymore, either!"
    mc "{i}(Is she talking about me, or the person on the phone?){/i}"
    scene 08_1336 with Dissolve(1)
    mc "{i}(What the...){/i}"
    menu:
        "Push her away[KoGa3AutoWTChange1]{size=-4}(Gabi End) {/size} {/color}":
            $ Gabi_End = True
            scene 08_1337 with Dissolve(1)
            mc "I'm sorry. This isn't a good idea."
            mc "We shouldn't do this again."
            scene 08_1338 with Dissolve(1)
            tr "You're right. I'm sorry, I..."
            tr "*Sigh*"
            mc "Will you be okay?"
            tr "I just need to think. Please forget about what just happened."
            mc "No worries."
            tr "Thank you, [mc]."
            scene 08_1339 with Dissolve(1)
            mc "{i}(It's the right thing, to leave, right?){/i}"
            mc "{i}(I think she's just confused.){/i}"
            $ renpy.end_replay()
            jump Week3_Saturday_Cheer
        "Kiss her back[KoGa3AutoWTChange1]{size=-4}(SexCounter Gabi+1, MC SexCounter+1, Gabi Week3 Saturday TC Sex, MC Week3 Saturday TC Cheer Late) {/size} {/color}":
            $ SexCounter_Gabi += 1
            $ MC_SexCounter += 1
            $ Gabi_Week3_Saturday_TC_Sex = True
            $ MC_Week3_Saturday_TC_Cheer_Late = True
            scene 08_1340 with Dissolve(1)
            ""
            scene 08_1341 with Dissolve(1)
            mc "{i}(I know this is wrong in so many ways, but...){/i}"
            scene 08_1342 with Dissolve(1)
            tr "Stop."
            mc "Sorry, I thought..."
            mc "{i}(What did I expect? That we would have sex again? She's my teacher...){/i}"
            tr "Not here."
            scene 08_1343 with Dissolve(1)
            tr "Come with me."
            mc "{i}(Maybe we are? Is this a good idea?){/i}"
            scene black with Dissolve(1)
            pause 2
            scene 08_1344 with Dissolve(1)
            tr "Come on in and lock the door."
            mc "{i}(Why didn't we students get such a room? What a difference to what we've got.){/i}"
            mc "{i}(And why am I thinking about our room when this hot teacher is standing in front of me?){/i}"
            mc "{i}(Just stop being in your head and say something, you idiot!){/i}"
            scene black with Dissolve(1)
            transform moveup:
                xalign 0.5 yalign 1.0
                linear 5.0 yalign 0.0
            show 08_1345 at moveup
            pause 3
            mc "You look really pretty."
            tr "Thank you. It's nice being complimented once in a while."
            scene 08_1346 with Dissolve(1)
            mc "Also yesterday at the pool!"
            mc "I had a hard time keeping my eyes off you."
            tr "..."
            scene 08_1347 with Dissolve(1)
            tr "Make me feel good again!"
            scene 08_1348 with Dissolve(1)
            mc "{i}(This feels so much different already than last time.){/i}"
            scene 08_1349 with vpunch
            tr "Aaah..."
            mc "Hehe."
            scene 08_1350 with Dissolve(1)
            tr "Let's go to the bed."
            scene 08_1351 with vpunch
            tr "Haha."
            mc "{i}(Good! She's finally laughing.){/i}"
            scene 08_1352 with Dissolve(1)
            mc "{i}(Look at her. She's gorgeous.){/i}"
            mc "{i}(If I was her husband, we wouldn't leave the bedroom. Ever. What an idiot.){/i}"
            mc "{i}(I'm not even feeling bad about this.){/i}"
            scene 08_1353 with Dissolve(1)
            ""
            scene black with Dissolve(1)
            pause 2
            scene 08_1354 with Dissolve(1)
            ""
            scene 08_1355 with Dissolve(1)
            mc "{i}(They're so huge!){/i}"
            scene black with Dissolve(1)
            transform moveup:
                xalign 0.5 yalign 1.0
                linear 5.0 yalign 0.0
            show 08_1356 at moveup
            pause 3
            tr "Do whatever you want! I'm all yours!"
            $ achievement.grant("ACHIEVEMENT_EXTRA_CREDIT")
            $ achievement.sync()
            scene 08_1357 with Dissolve(1)
            tr "Ah..."
            mc "{i}(I always wanted to taste them.){/i}"
            scene 08_1358 with Dissolve(1)
            mc "{i}(We just had drunken sex last time.){/i}"
            mc "{i}(But now. Touching her, feeling her. This is so...){/i}"
            mc "{i}(What I don't understand is, why would she risk her career for this?){/i}"
            mc "{i}(Why am I thinking again...? Just stop and enjoy this.){/i}"
            scene black with Dissolve(1)
            pause 2
            scene 08_1359 with Dissolve(1)
            ""
            scene 08_1360 with Dissolve(1)
            mc "You're sure about this, right?"
            mc "Because last time when we..."
            scene 08_1361 with vpunch
            mc "{i}(I'll take that as a yes.){/i}"
            scene 08_1362 with Dissolve(1)
            tr "*Moaning quietly*"
            scene 08_1363 with Dissolve(1)
            mc "{i}(She even moans sexily.){/i}"
            scene black with Dissolve(1)
            pause 2
            scene 08_1364 with Dissolve(1)
            mc "{i}(I'm actually getting nervous.){/i}"
            scene 08_1365 with Dissolve(1)
            mc "{i}(Just with her holding my cock I'm about to explode...){/i}"
            mc "{i}(Is she going to suck it?){/i}"
            scene 08_1366 with Dissolve(1)
            mc "{i}(Maybe not... Well, she said to make her feel good.){/i}"
            mc "{i}(Next time maybe? Will there be a next time?){/i}"
            scene 08_1367 with Dissolve(1)
            ""
            scene 08_1368 with Dissolve(1)
            mc "You feel so good!"
            scene 08_1369 with Dissolve(1)
            tr "*Moaning quietly*"
            mc "{i}(Again those moans...){/i}"
            scene 08_1370 with Dissolve(1)
            mc "{i}(Everything she does is a turn-on...){/i}"
            scene 08_1371 with Dissolve(1)
            ""
            scene 08_1372 with Dissolve(1)
            mc "{i}(This feels so incredible!){/i}"
            mc "{i}(So much that I'm cumming already...){/i}"
            mc "{i}(Think of something so I'll last a big longer. I don't want this to end yet.){/i}"
            scene 08_1373 with Dissolve(1)
            tr "Oh..."
            scene 08_1374 with Dissolve(1)
            mc "{i}(This doesn't really help much.){/i}"
            mc "{i}(Quite the opposite...){/i}"
            mc "{i}(Let's change position so I can control the speed.){/i}"
            scene black with Dissolve(1)
            pause 2
            scene 08_1376 with Dissolve(1)
            ""
            show 08_1377
            tr "Ah-ah-ah..."
            scene 08_1378 with Dissolve(1)
            mc "{i}(Now I can't hold it any longer...){/i}"
            menu:
                "Cum inside[KoGa3AutoWTChange1]{size=-4}(Gabi Week3 Saturday TC CumInside) {/size} {/color}":
                    $ Gabi_Week3_Saturday_TC_CumInside = True
                    scene 08_1380 with vpunch
                    scene 08_1380 with vpunch
                    mc "*Breathing heavily*"
                    mc "{i}(Fuck that was good!){/i}"
                "Pull out":
                    scene 08_1379 with vpunch
                    mc "*Breathing heavily*"
                    mc "{i}(Fuck that was good!){/i}"
            scene 08_1381 with Dissolve(1)
            ""
            scene black with Dissolve(1)
            pause 2
            scene 08_1382 with Dissolve(1)
            tr "Can you stay for a bit? I don't want..."
            mc "Of course."
            scene 08_1383 with Dissolve(1)
            mc "Was that okay?"
            tr "*Nods*"
            scene 08_1384 with Dissolve(1)
            mc "{i}(Can't believe I had sex with a teacher. Again.){/i}"
            mc "{i}(And this time, knowing who she is...){/i}"
            scene 08_1385 with Dissolve(1)
            mc "{i}(I always thought she had fake boobs, since they're so big.){/i}"
            mc "{i}(But after I touched and... Heh. Damn, they're great!){/i}"
            mc "{i}(I'm getting horny again just thinking about it.){/i}"
            tr "I can feel you staring!"
            scene 08_1386 with Dissolve(1)
            mc "What?"
            tr "I said I can feel you staring."
            scene 08_1387 with Dissolve(1)
            mc "Sorry. But I can't help it. You're gorgeous."
            tr "Thank you, [mc]."
            mc "I won't be able to concentrate in Spanish class anymore after this."
            scene 08_1388 with Dissolve(1)
            tr "Haha. Like you need to concentrate to ace that class."
            scene 08_1389 with Dissolve(1)
            mc "..."
            mc "{i}(You have no idea what you're doing to me.){/i}"
            scene black with Dissolve(2)
            pause 2
            scene 08_1390 with Dissolve(1)
            mc "{i}(Shit! I must have dozed off.){/i}"
            mc "{i}(I'm gonna be so late for Elena's competition. Fuck!){/i}"
            mc "{i}(Is she sleeping? I don't want to wake her.){/i}"
            mc "{i}(I'll just leave, before I lose even more time thinking about what I should do...){/i}"
            scene 08_1391 with Dissolve(1)
            ""
            $ renpy.end_replay()
            jump Week3_Saturday_Cheer_Late

label Week3_Saturday_Cheer_Late:
    $ Elena_Points -= 4
    $ Layla_Points -= 4
    scene black with Dissolve(1)
    pause 2
    scene 08_1392 with Dissolve(1)
    mc "Uh... What are you doing here?"
    la "Right back at you."
    mc "I'm on my way to you guys to watch the cheerleading competition."
    la "Uh-huh."
    scene 08_1393 with Dissolve(1)
    mc "Are you mad at me?"
    el "You promised!"
    mc "What?"
    el "..."
    mc "Where are you going? Don't you have to head to the competition?"
    el "That was twenty minutes ago."
    scene 08_1394 with Dissolve(1)
    mc "Shit... I didn't know it was that late already."
    mc "I'm so sorry, Elena. I was held up and forgot about the time."
    mc "Sorry! Really!"
    scene 08_1395 with Dissolve(1)
    mc "How can I make it up to you? I'll do anything?"
    el "..."
    mc "Elena, please!"
    el "I'll think about it."
    mc "So, you'll forgive me?"
    el "Maybe."
    scene 08_1396 with Dissolve(1)
    mc "By the way. Did you win?"
    if Elena_Week3_Monday_CheerTraining == True:
        el "Yes!"
        mc "Of course, you did. Congratulations!"
    else:
        el "No. Second place."
        mc "That's still good, right?"
    scene 08_1397 with Dissolve(1)
    el "*Sigh* It's so hard staying mad at you, you know?"
    la "I have the same problem."
    mc "It's part of my charm."
    el "Dios mío."
    la "Haha, riiight..."
    scene 08_1417 with Dissolve(1)
    mc "So what are the plans for the rest of the day?"
    la "Uhm... We can all meet up in our room and play some games?"
    mc "What games?"
    la "I don't know. We'll figure it out."
    scene 08_1418 with Dissolve(1)
    mc "Sounds good, but can we go eat first?"
    la "Haha. Somehow I knew you were gonna say that."
    el "Haha."
    jump Week3_Saturday_Evening

label Week3_Saturday_Cheer:
    $ Elena_Points += 2
    # Elena (28)
    scene black with Dissolve(1)
    pause 2
    stop music fadeout 1.0
    play music ("Music/LoFi Spanish 1.mp3", "Music/LoFi Spanish 2.mp3", "Music/LoFi Spanish 3.mp3") volume 0.2
    scene 08_1398 with Dissolve(1)
    ""
    scene 08_1399 with Dissolve(1)
    ""
    if Elena_Points >= 23:
        scene black with Dissolve(1)
        transform moveup:
            xalign 0.5 yalign 1.0
            linear 5.0 yalign 0.0
        show 08_1400 at moveup
        pause 3
        mc "{i}(I can't get enough of Elena in her cheer outfit!){/i}"
        scene 08_1401 with Dissolve(1)
        n "GO FALCONS!"
    else:
        scene 08_1401 with Dissolve(1)
        n "GO FALCONS!"
    scene 08_1402 with Dissolve(1)
    mc "Elena is actually incredible."
    la "Yeah, she is."
    mc "She must be the best in the squad. Everything is centred around her."
    la "She's head cheerleader. She's the one who comes up with the routines, together with the coach."
    scene 08_1403 with Dissolve(1)
    mc "Really?"
    la "Uh-huh."
    mc "Wow. I didn't know that."
    scene 08_1404 with Dissolve(1)
    mc "I totally underestimated what cheering was."
    mc "I never watched it because I thought it was just 'cheering'."
    mc "But this is actually more gymnastics."
    if Layla_Dating == False:
        scene 08_1405 with Dissolve(1)
        mc "If they had a few more guys, they could do even more aerial... uh... flippy things... I don't know what they're called."
    else:
        scene 08_1405a with Dissolve(1)
        mc "If they had a few more guys, they could do even more aerial... uh... flippy things... I don't know what they're called."
    la "Haha. Why do you think Elena kept asking you to join."
    mc "I thought she was kidding and teasing me."
    la "No. Well, she was, but not entirely. They actually would love to have more boys."
    scene black with Dissolve(1)
    pause 2
    scene 08_1406 with Dissolve(1)
    la "You were amazing, Elena!"
    el "Thank you."
    scene 08_1407 with Dissolve(1)
    la "This should be an easy victory, right?"
    el "Haha, I don't know. Miramar was pretty good."
    scene 08_1408 with Dissolve(1)
    mc "I agree with Layla. You did great!"
    el "Thanks, [mc]!"
    el "And thank you for coming to watch us."
    mc "My pleasure."
    scene 08_1409 with Dissolve(1)
    el "Now we only have to wait for the final scores."
    scene black with Dissolve(1)
    pause 2
    scene 08_1410 with Dissolve(1)
    an "We counted the scorecards and the results are in!"
    if Elena_Week3_Monday_CheerTraining == True:
        an "First place. Madison Springs Athletics!"
        scene 08_1411 with Dissolve(1)
        la "I knew it!"
        el "Haha."
        mc "Congrats, Elena!"
        scene 08_1413 with Dissolve(1)
        el "Thank you, [mc], for training with me. It helped me a lot!"
        mc "Anytime. I had fun too!"
        la "[mc] was so impressed that he's thinking about joining."
        el "What? Really? That would be so..."
        scene 08_1414 with Dissolve(1)
        el "You're joking, right?"
        la "Haha."
        el "Not funny!"
        scene 08_1415 with Dissolve(1)
        mc "I was impressed though. I had fun watching you... Uh... The team."
    else:
        an "First place. Miramar Bay Academy."
        x "*Cheer*"
        an "Second place. Madison Springs Athletics."
        scene 08_1412 with Dissolve(1)
        la "Second place! Congrats, Elena."
        mc "Congratulations!"
        el "Thank you, both of you."
    scene 08_1416 with Dissolve(1)
    el "I'll be right back. I'll go congratulate the squad."
    la "Go ahead. We'll wait here for you."
    scene black with Dissolve(1)
    pause 2
    scene 08_1417 with Dissolve(1)
    mc "So what are the plans for the rest of the day?"
    la "Uhm... We can all meet up in our room and play some games?"
    mc "What games?"
    la "I don't know. We'll figure it out."
    scene 08_1418 with Dissolve(1)
    mc "Sounds good, but can we go eat first?"
    la "Haha. Somehow I knew you were gonna say that."
    el "Haha."
    jump Week3_Saturday_Evening

label Week3_Saturday_Evening:
    scene black with Dissolve(1)
    pause 2
    play music ("Music/LoFi Upbeat 3.mp3", "Music/LoFi Upbeat 4.mp3", "Music/LoFi Upbeat 1.mp3", "Music/LoFi Upbeat 2.mp3") volume 0.2
    scene 08_1419 with Dissolve(1)
    la "Welcome to our room."
    mc "Damn... Why is this room so much nicer and bigger than ours?"
    el "Is it really that bad?"
    mc "Haha, yeah. It's pretty bad compared to this one."
    scene 08_1420 with Dissolve(1)
    la "You guys haven't really met yet, right?"
    la "This is MacKenzie. Kens, this is [mc]."
    mc "Hi, nice to meet you."
    mk "Hey, [mc]. You too."
    if Elena_Week3_Monday_CheerTraining == True:
        mc "And congrats on first place."
    else:
        mc "And congrats on second place."
    mk "Thank you!"
    scene 08_1421 with Dissolve(1)
    la "You're leaving?"
    mk "Yeah."
    la "We were about to play some games. Don't you want to join?"
    mk "Maybe later. I want to check out the pool, since I couldn't yesterday."
    la "Alright. See you then. Have fun."
    scene 08_1422 with Dissolve(1)
    mc "So, who's joining?"
    la "It's us four, and Zach's asking Valeria to come too."
    la "Anyone else in mind?"
    mc "No, seems fine to me."
    if Layla_Dating == True:
        scene 08_1423 with Dissolve(1)
        mc "Do you know when they're coming?"
        la "No idea."
        mc "We might have a little time then."
        la "Hmm? Time for what?"
        scene 08_1424 with Dissolve(1)
        mc "You'll see."
        la "Hey, [mc]!"
        scene 08_1425 with vpunch
        la "Haha."
        scene 08_1426 with Dissolve(1)
        el "Seriously, those two."
        si "Are they actually dating?"
        el "Not yet. Won't be long though, I think."
        scene 08_1427 with Dissolve(1)
        la "Is that it?"
        la "I expected something..."
        scene 08_1428 with Dissolve(1)
        la "more..."
        scene 08_1429 with Dissolve(1)
        ""
        if Elena_Points >= 23:
            scene 08_1430 with Dissolve(1)
            el "..."
        else:
            scene 08_1430a with Dissolve(1)
            el "We're still here, you know!"
        scene 08_1431 with Dissolve(1)
        la "Haha, sorry, sorry."
        scene 08_1432 with Dissolve(1)
        mc "By the way. Should I get us some snacks?"
        la "Zach said he's bringing some."
        mc "Ah, cool."
    else:
        scene 08_1432 with Dissolve(1)
        mc "By the way. Should I get us some snacks?"
        la "Zach said he's bringing some."
        mc "Ah, cool."
    scene 08_1433 with Dissolve(1)
    va "Hey."
    z "Yo, yo, yo."
    mc "Speak of the devil."
    z "The man of the hour is here!"
    scene 08_1434 with Dissolve(1)
    z "I was stopped by a teacher on my way here. He asked where I was going with my bag. I thought he'd ask what's in it."
    mc "What did you say?"
    z "That I spilled some stuff on my clothes and was going to the showers to clean them."
    mc "Seems like it worked. You made it here safely."
    z "Yeah, so scary though. I panicked a little."
    scene 08_1435 with Dissolve(1)
    la "Did you bring the snacks?"
    z "Of course! Why do you think I panicked earlier with the teacher?"
    la "Huh?"
    scene 08_1436 with Dissolve(1)
    z "I have beers."
    z "I have vodka."
    scene 08_1437 with Dissolve(1)
    z "And I have... You're gonna like this!"
    z "Tequila!"
    scene 08_1438 with Dissolve(1)
    la "Snacks! I meant chips, crackers, stuff like that..."
    z "Oh... I thought snacks was a code word for alcohol."
    la "*Sigh*"
    z "So, you don't want to drink?"
    scene 08_1439 with Dissolve(1)
    la "I didn't say that. We can play some drinking games now."
    z "See! That's exactly why I brought them."
    z "This is going to be so much fun."
    scene 08_1440 with Dissolve(1)
    el "But no passing out in our room! We're not going to carry you back to yours!"
    z "Hey. If I remember correctly... You were the one passed out at the club, and I carried you!"
    el "..."
    scene 08_1441 with Dissolve(1)
    mc "You guys figure out what games we can play."
    mc "In the meantime, I'll go get us some snacks."
    va "I'll come with you."
    la "Thank you, [mc]."
    scene black with Dissolve(1)
    pause 2
    scene 08_1442 with Dissolve(1)
    mc "I just wanted to get out of there."
    mc "I felt another argument coming up."
    va "Haha, I had the same feeling."
    scene 08_1443 with Dissolve(1)
    va "Do they hate each other that much? Elena and Zach. Well, not hate, but..."
    mc "I know what you mean."
    mc "I don't know. I think they're just different people."
    mc "Just like there are people you get along with, others you don't."
    va "Hmm..."
    scene 08_1444 with Dissolve(1)
    mc "By the way. How was the game? You watched the second half, right?"
    va "It was good."
    mc "Yeah?"
    scene 08_1445 with Dissolve(1)
    va "No! I was bored. I like to watch sports but I'm just not a football person."
    mc "Haha."
    va "Zach got a red card ten minutes into the second half, so he wasn't even on the field."
    mc "And you still watched the whole game, huh?"
    va "I couldn't just leave."
    scene 08_1446 with Dissolve(1)
    mc "Oh, poor you!"
    va "Haha, stop."
    scene black with Dissolve(1)
    pause 2
    scene 08_1447 with Dissolve(1)
    va "Should we get some soda too?"
    mc "Yeah, good idea. I don't think any of us drinks vodka straight up."
    scene 08_1448 with Dissolve(1)
    mc "Except for maybe Zach."
    va "Haha, true. What's your favourite?"
    mc "Soda?"
    va "Uh-huh."
    menu:
        "Cola":
            mc "I'm just an average cola person I suppose."
            va "Cola? I don't like it at all."
            mc "Too moist?"
            va "Ew, haha. Just the thought of it now..."
        "Iced tea[KoGa3AutoWTChange1]{size=-4}(Valeria Week3 Saturday Tea) {/size} {/color}":
            $ Valeria_Week3_Saturday_Tea = True
            mc "I don't really have a favourite, per se."
            mc "But I mostly order iced tea when I'm at a bar or restaurant."
            va "Ever tried bubble milk tea?"
            mc "Never heard of that."
            va "It's good. You have to try it when you get the chance."
            mc "I will."
        "Ginger ale":
            mc "I actually really like ginger ale."
            va "Never had that. What does it taste like?"
            mc "Hmm... It has a citrusy ginger flavour, I suppose."
    scene black with Dissolve(1)
    pause 2
    scene 08_1449 with Dissolve(1)
    mc "How many did you buy?"
    va "Six."
    mc "That many?"
    va "One for each."
    scene 08_1450 with Dissolve(1)
    mc "Haha, need some help?"
    va "I've got it, thanks."
    mc "You sure? That looks really... Unstable."
    va "..."
    mc "Just don't trip like you did on the bus."
    if Valeria_Points >= 7:
        va "Let me concentrate, or I will actually trip."
        scene 08_1451 with Dissolve(1)
        mc "Don't worry. I'll catch you again if you do."
        va "..."
    else:
        va "Let me concentrate, or I will actually trip."
    scene 08_1452 with Dissolve(1)
    va "Do you have everything?"
    mc "Yeah, two packs of chips. One spicy, the other green onion and sour cream."
    mc "A pack of salted crackers and a few candy bars."
    va "Let's go then."
    if Alexis_Dating == True:
        scene 08_1453 with Dissolve(1)
        mc "You can go ahead. I need to make a quick phone call."
        va "Alright."
        mc "One more thing."
        va "Don't trip, I know!"
        mc "Haha, how did you even..."
        va "I've started to figure you out."
        mc "That's scary!"
        if Valeria_Points >= 7:
            va "Haha."
            scene black with Dissolve(1)
            transform moveup:
                xalign 0.5 yalign 1.0
                linear 5.0 yalign 0.0
            show 08_1454 at moveup
            pause 3
            mc "{i}(Fuck... I know I should be happy for Zach.){/i}"
            mc "{i}(But somehow I don't like that they've kissed...){/i}"
        else:
            va "Haha."
        scene black with Dissolve(1)
        pause 2
        scene 08_1455 with Dissolve(1)
        mc "Let's see if she picks up."
        mc "..."
        scene 08_1456 with Dissolve(1)
        a "Hi!"
        mc "Hey there. How are you?"
        scene 08_1457 with Dissolve(1)
        a "I'm good, how about you?"
        mc "Also good."
        scene 08_1458 with Dissolve(1)
        ir "Boyfriend?"
        a "..."
        ir "Haha. I'll be quiet."
        scene 08_1459 with Dissolve(1)
        mc "Not a good time?"
        a "I'm out with my roomie, but I have time for you. Always."
        mc "Aw... So sweet."
        a "Haha."
        scene 08_1460 with Dissolve(1)
        mc "What are you up to?"
        a "We're going to a club with a few friends."
        mc "Wish I could tag along."
        scene 08_1461 with Dissolve(1)
        a "With a bunch of girls?"
        mc "Sure, why not?"
        a "Haha. Next time then! How was the competition?"
        if MC_Week3_Saturday_TC_Win == True:
            scene 08_1462 with Dissolve(1)
            mc "Lots of fun."
            mc "And I actually won!"
            a "Congratulations, [mc]! I'm so happy for you!"
            mc "Thanks."
        else:
            scene 08_1462a with Dissolve(1)
            mc "Hmm... It was okay. I didn't do as good as I hoped."
            mc "Fourth place!"
            a "That's still good, though. It's your first competition."
            mc "Yeah..."
        mc "I also recorded Layla's run, we can watch it when I'm back."
        a "Thank you!"
        a "*Sigh* Uhm..."
        scene 08_1463 with Dissolve(1)
        a "[mc]!"
        mc "Lexi!"
        a "There's something I have to come clean about."
        mc "Okay?"
        a "I feel so bad about it."
        mc "..."
        a "I cheated!"
        scene 08_1464 with Dissolve(1)
        mc "WHAT? You chea..."
        mc "What the fuck, Alexis! The new bartender, right?"
        scene 08_1465 with Dissolve(1)
        a "No-no-no. That's not what I meant. I would never..."
        mc "..."
        a "I knew the result of the competition already. I called Layla earlier to ask how she did."
        a "And well, I was curious and I sneakily asked how you did, too... Sorry."
        scene 08_1466 with Dissolve(1)
        mc "FUCK! LEXI! Do you have any idea how fast my heart was pumping just now... I was about to punch someone."
        a "Haha. Sorry again. Poor choice of words."
        mc "..."
        a "Don't say it!"
        mc "What?"
        scene 08_1467 with Dissolve(1)
        a "You know what!"
        mc "Phrasing?"
        a "SEE!"
        mc "Haha."
        scene 08_1468 with Dissolve(1)
        a "Any plans for the last night?"
        mc "Hanging out with friends, drinking a little and playing some games."
        a "Don't get caught drinking, though."
        mc "We'll be careful."
        scene black with Dissolve(1)
        pause 2
        scene 08_1469 with Dissolve(1)
        a "Anyway, I'll leave you be for today. We'll talk more tomorrow. And not over the phone!"
        mc "Yeah, talk... Can't wait."
        mc "Bye, Lexi."
        a "Bye, [mc]. Have fun!"
        mc "You too."
        scene 08_1470 with Dissolve(1)
        ir "Ew, it's so disgusting how much in love you are with that boy."
        a "Do I hear jealousy?"
        ir "Totally!"
        ir "*Sigh* Maybe I'll find someone at the club."
        scene 08_1471 with Dissolve(1)
        ir "Or we can make out?"
        a "Not happening!"
        ir "Just once? How else would you know if you're into girls or not?"
        a "Who said I've never kissed a girl?"
        ir "You did? Who? Lexiiii, tell me!"
        a "..."
    else:
        if Valeria_Points >= 7:
            scene 08_1453 with Dissolve(1)
            mc "Go ahead, I'll be right behind."
            scene black with Dissolve(1)
            transform moveup:
                xalign 0.5 yalign 1.0
                linear 5.0 yalign 0.0
            show 08_1454 at moveup
            pause 3
            mc "{i}(Fuck... I know I should be happy for Zach.){/i}"
            mc "{i}(But somehow I don't like that they've kissed...){/i}"
        else:
            scene 08_1453 with Dissolve(1)
            mc "Go ahead, I'll be right behind."
    scene black with Dissolve(1)
    pause 2
    scene 08_1472 with Dissolve(1)
    n "Cheers!"
    scene black with Dissolve(1)
    pause 2
    scene 08_1473 with Dissolve(1)
    la "Haha... That's funny."
    el "Did that really happen?"
    mc "It did."
    scene 08_1474 with Dissolve(1)
    la "Next question. Who's turn is it?"
    z "Mine. I have a really good one."
    z "Who is the hottest teacher?"
    el "Really, Zach?"
    z "What? It's a good question. [mc], you go first."
    scene 08_1475 with Dissolve(1)
    mc "Hmm. Hottest teacher."
    mc "Let's see..."
    if Zach_Week2_Monday_Sister == True:
        menu:
            "Gabi":
                scene 08_1476 with Dissolve(1)
                mc "Gabi!"
                z "Haha, right? No one's even getting close. She's just... perfection."
                z "Very hot, big boobs, big ass..."
                la "*Sigh*"
                la "Is that all you see when looking at girls?"
                z "Well yeah. Is there anything else? I can't look at personality!"
                el "..."
            "Ms Davis":
                scene 08_1476 with Dissolve(1)
                mc "I think I'll go with Ms Davis."
                z "Really? Naomi, huh? I thought you'd pick Gabi. But not a bad choice."
                z "She has really big boobs, too."
                la "*Sigh*"
                la "Is that all you think about? Boobs?"
                z "Not all, but it's a big part... Haha, see what I did there. Big... Haha."
                el "..."
            "Principal Moore[KoGa3AutoWTChange1]{size=-4}(Adriana Week3 Saturday TC Pick) {/size} {/color}":
                $ Adriana_Week3_Saturday_TC_Pick = True
                scene 08_1478 with Dissolve(1)
                mc "Technically not a teacher, but she works at our school."
                mc "Principal Moore."
                la "HEY!"
                mc "Haha sorry. But she's the prettiest. Want me to lie?"
                z "I thought you'd pick Gabi, but honestly, Principal Moore is a total milf!"
                scene 08_1479 with Dissolve(1)
                z "She has a nice body too. I'd totally do her."
                mc "{i}(Zach. No!){/i}"
                la "Oh my god!"
                el "Uhm... Guys? That's Layla's mom."
                z "What? Are you serious? Principal Moore is your mom, Layla?"
                scene 08_1480 with Dissolve(1)
                la "Yeah, she is!"
                z "I didn't know that. Why didn't..."
                la "I don't want to talk about that now. Can we continue, please?"
                z "Sure..."
    else:
        menu:
            "Gabi":
                scene 08_1476 with Dissolve(1)
                mc "Gabi!"
                z "Haha, right? No one's even getting close. She's just... perfection."
                z "Very hot, big boobs, big ass..."
                la "*Sigh*"
                la "Is that all you see when looking at girls?"
                z "Well yeah. Is there anything else? I can't look at personality!"
                el "..."
            "Ms Davis":
                scene 08_1476 with Dissolve(1)
                mc "I think I'll go with Ms Davis."
                z "Really? Naomi, huh? I thought you'd pick Gabi. But not a bad choice."
                z "She has really big boobs, too."
                la "*Sigh*"
                la "Is that all you think about? Boobs?"
                z "Not all, but it's a big part... Haha, see what I did there. Big... Haha."
                el "..."
            "Receptionist":
                scene 08_1477 with Dissolve(1)
                mc "Technically not a teacher, but she works at our school. I'll go with the red-haired receptionist."
                z "What? You know that's my sister, right?"
                la "You have a sister?"
                mc "Wait. That's Natasha?"
                z "Yeah..."
                mc "Shit. I didn't recognise her. It's been a long time since I last saw her."
                z "Enough talk about my sister. Let's move on."
            "Principal Moore[KoGa3AutoWTChange1]{size=-4}(Adriana Week3 Saturday TC Pick) {/size} {/color}":
                $ Adriana_Week3_Saturday_TC_Pick = True
                scene 08_1478 with Dissolve(1)
                mc "Technically not a teacher, but she works at our school."
                mc "Principal Moore."
                la "HEY!"
                mc "Haha sorry. But she's the prettiest. Want me to lie?"
                z "I thought you'd pick Gabi, but honestly, Principal Moore is a total milf!"
                scene 08_1479 with Dissolve(1)
                z "She has a nice body too. I'd totally do her."
                mc "{i}(Zach. No!){/i}"
                la "Oh my god!"
                el "Uhm... Guys? That's Layla's mom."
                z "What? Are you serious? Principal Moore is your mom, Layla?"
                scene 08_1480 with Dissolve(1)
                la "Yeah, she is!"
                z "I didn't know that. Why didn't..."
                la "I don't want to talk about that now. Can we continue, please?"
                z "Sure..."
    if Adriana_Week3_Saturday_TC_Pick == True:
        scene 08_1481 with Dissolve(1)
        z "Elena, you're next!"
        el "Hmm... Since we don't have to pick an actual teacher."
        el "I'll take Principal Moore too."
        la "Are you kidding me? You too, now?"
        el "I have to agree with [mc]. She's the prettiest."
        la "Seriously..."
        scene 08_1482 with Dissolve(1)
        z "Are you a lesbian?"
        el "No. What gave you that idea?"
        z "Then why..."
        el "Your question was who is the hottest teacher. Teacher not being gender specific. She is. That's it."
        z "Hmm. Okay, fair enough."
        el "How about you, Layla?"
        scene 08_1483 with Dissolve(1)
        la "I'm not picking my mom..."
        z "Haha."
        la "Uhm... I think Mr Donovan."
        el "Oh, he's a cutie."
    else:
        scene 08_1484 with Dissolve(1)
        z "Elena, you're next!"
        el "I'll go with Mr Donovan."
        la "I agree, he's a cutie."
    scene 08_1485 with Dissolve(1)
    z "Who's that?"
    la "He teaches English literature."
    z "I don't take that class. Never heard of him."
    si "He's my pick, too."
    scene 08_1486 with Dissolve(1)
    z "How about you, Val?"
    va "Mr Donovan."
    z "What the fuck? Who is this guy? Some kind of Greek god?"
    scene 08_1474 with Dissolve(1)
    z "Well, mine is..."
    la "Ms Ramirez, we know!"
    z "Haha. Correct."
    z "Okay then. I have another great question."
    z "What's your 'number'?"
    scene 08_1487 with Dissolve(1)
    la "Favourite number?"
    z "No... The number of people you've had sex with."
    la "Not going to answer that."
    el "That's more of a truth or dare question..."
    z "Let's play truth or dare, then!"
    scene 08_1488 with Dissolve(1)
    mc "Fine with me, but I'll go use the bathroom first."
    z "I need to go, too."
    scene black with Dissolve(1)
    pause 2
    scene 08_1489 with Dissolve(1)
    z "Truth or dare. Now this will get interesting."
    mc "Seems like you're prepared already?"
    z "Yeah, I've got lots of questions and some nice dares."
    scene 08_1490 with Dissolve(1)
    z "You've gotta help me out though, bro. With Valeria."
    mc "{i}(You guys kissed, you're doing fine, but I guess...){/i}"
    mc "Sure thing."
    z "But don't make it too obvious."
    mc "Don't worry."
    scene black with Dissolve(1)
    pause 2
    scene 08_1491 with Dissolve(1)
    el "[mc], truth or dare?"
    mc "What? Why do I have to go first?"
    la "We girls decided when you were in the bathroom."
    mc "No-no-no. Not the boys against girls bullshit again. Let's spin a bottle to make it fair."
    el "Alright. We can do that."
    la "I'll spin it."
    scene 08_1492 with Dissolve(1)
    mc "Oh, come on..."
    la "Sorry, [mc]."
    el "Haha. See! Even fate wanted it to be you."
    mc "{i}(Fate... Fate can kiss my ass!){/i}"
    scene 08_1493 with Dissolve(1)
    el "Truth or dare?"
    mc "Truth!"
    el "You sure?"
    mc "I'm not drunk enough to do your dare."
    el "Haha. You're scared already, huh? Let's make a rule though. You can only use truth three times before you have to do a dare. Or else no one will pick dare."
    mc "Hmm. Sounds good."
    scene 08_1494 with Dissolve(1)
    el "I've always wanted to know this!"
    mc "Go ahead."
    el "Did you cheat on the geography test?"
    mc "Haha."
    scene 08_1482 with Dissolve(1)
    z "What kind of question is that? We're not six years old..."
    el "I can ask whatever I want. When it's your turn, you can ask your stupid questions."
    z "They're not stupid!"
    el "..."
    scene 08_1495 with Dissolve(1)
    el "So?"
    mc "*Sigh* Okay... The truth. Listen, I needed a good score..."
    el "I knew it! I so knew it! Tramposo!\n(Cheater!)"
    mc "I had a feeling we'd get a test, so I studied the day before."
    scene 08_1496 with Dissolve(1)
    el "What?"
    mc "I didn't cheat, Elena!"
    la "Haha."
    el "No way! I was so sure... *Sigh*"
    z "Next spin."
    scene 08_1492 with Dissolve(1)
    mc "..."
    mc "You've gotta be kidding me!"
    el "Haha. I like this game."
    mc "I'm so glad you're enjoying this, Elena!"
    scene 08_1497 with Dissolve(1)
    mc "*Sigh* Truth!"
    z "Same question as before. What's your number?"
    mc "Really, Zach? You could've asked me a simple question. Help me out here!"
    z "No one gets simple questions when it's my turn."
    mc "Fine..."
    scene 08_1498 with Dissolve(1)
    mc "Well... I actually don't know. I never counted."
    el "More than five?"
    mc "Uh... Yeah."
    z "More than ten?"
    la "What?"
    mc "Give me a sec."
    scene 08_1488 with Dissolve(1)
    mc "No, it's between five and ten. Let's keep it at that."
    z "Dude! Seriously? I'm kinda jealous."
    la "..."
    scene 08_1492 with Dissolve(1)
    el "Haha."
    mc "..."
    scene 08_1499 with Dissolve(1)
    mc "Seriously? No! Just no! This can't be right. Is this some kind of set-up?"
    el "Haha, I can't stop laughing!"
    mc "We're going to switch bottles after this and I'm going to spin!"
    mc "Truth!"
    el "The one after has to be a dare."
    mc "I know!"
    scene black with Dissolve(1)
    pause 2
    n "Sometime later."
    scene 08_1500 with Dissolve(1)
    la "I guess I have to pick dare now."
    la "So yeah. Dare."
    mc "You look scared."
    la "Cause I am..."
    scene 08_1501 with Dissolve(1)
    mc "This one isn't that bad."
    mc "Dress up as a cheerleader and do a cheer."
    la "Really?"
    mc "Yeah! I'm sure you'll do great!"
    la "I don't have a uniform though..."
    mc "If only we were in a room with cheerleaders. I'm pretty sure you can borrow Sienna's or Elena's."
    el "You can wear mine."
    scene 08_1502 with Dissolve(1)
    la "*Sigh* Be right back."
    el "Do the one we used to do in your backyard."
    la "No!"
    scene black with Dissolve(1)
    pause 2
    if Layla_Dating == True:
        scene 08_1503 with Dissolve(1)
        la "This is so embarrassing!"
        va "You look so pretty, Layla!"
        scene black with Dissolve(1)
        transform moveup:
            xalign 0.5 yalign 1.0
            linear 5.0 yalign 0.0
        show 08_1504 at moveup
        pause 3
        mc "{i}(She looks really cute.){/i}"
        la "Happy?"
        mc "Almost. Only the cheer left."
    else:
        scene 08_1503a with Dissolve(1)
        la "This is so embarrassing!"
        va "You look so pretty, Layla!"
        scene black with Dissolve(1)
        transform moveup:
            xalign 0.5 yalign 1.0
            linear 5.0 yalign 0.0
        show 08_1504 at moveup
        pause 3
        la "Happy?"
        mc "Almost. Only the cheer left."
    scene 08_1505 with Dissolve(1)
    la "Isn't this enough?"
    mc "Nuh-uh. Just a quick little cheer."
    la "*Sigh* Fine..."
    scene 08_1506 with Dissolve(1)
    la "H... A... T... E..."
    la "I hate this, yes, yes, I hate this!"
    z "Aren't cheers supposed to be joyful?"
    scene 08_1507 with Dissolve(1)
    la "S... H... U... T..."
    la "Shut up, Zach, yes, yes, shut up, Zach!"
    mc "Haha. This is gold! I should've recorded it!"
    la "NO!"
    scene 08_1508 with Dissolve(1)
    la "And... Done! That's all you're getting."
    n "*Cheering*"
    if Layla_Dating == True:
        el "Go, Layla. Go, Layla!"
        scene 08_1509 with Dissolve(1)
        mc "*Whisper* That was hot!"
        mc "*Whisper* You look cute in that uniform."
        la "*Whisper* Thank you."
    else:
        el "Go, Layla. Go, Layla!"
    scene black with Dissolve(1)
    pause 2
    scene 08_1510 with Dissolve(1)
    si "Your turn, Valeria."
    va "I'll take truth."
    scene 08_1511 with Dissolve(1)
    el "Oh, I have a good one."
    el "Is Zach a good kisser?"
    z "HEY!"
    scene 08_1512 with Dissolve(1)
    va "Uhm..."
    va "I don't know."
    el "What do you mean?"
    la "Oh... Maybe he's your first kiss and you have no one to compare it to?"
    va "No, we..."
    scene 08_1513 with Dissolve(1)
    z "We haven't kissed."
    el "What?"
    el "We saw you. At the pool."
    z "No."
    scene black with Dissolve(1)
    pause 2
    scene 08_1099 with Dissolve(1)
    z "{i}(This is it! The moment!){/i}"
    z "You are so beautiful and I need to tell you something."
    z "I like you, Val."
    scene 08_1100 with Dissolve(1)
    ""
    scene 08_1104 with Dissolve(1)
    ""
    scene 08_1514 with Dissolve(1)
    va "..."
    scene 08_1515 with Dissolve(1)
    va "*Whisper* Sorry, I can't."
    z "*Whisper* It's okay."
    va "*Whisper* Can you let me go?"
    z "*Whisper* Uh, sure."
    scene black with Dissolve(1)
    pause 2
    scene 08_1516 with Dissolve(1)
    if Valeria_Points >= 7:
        el "Oh..."
        mc "{i}(Somehow I'm happy they didn't kiss.){/i}"
    else:
        el "Oh..."
        mc "{i}(Why didn't Zach tell me?){/i}"
    el "So, you're still waiting for your first kiss?"
    z "It wouldn't be my first kiss!"
    el "Really... I might have a truth question for you later!"
    z "..."
    scene 08_1517 with Dissolve(1)
    mc "Here, looks like you need another one."
    va "I do. Thanks."
    scene black with Dissolve(1)
    pause 2
    scene 08_1518 with Dissolve(1)
    la "That's you, Sienna!"
    si "Dare!"
    el "Hmm... A dare."
    z "Give someone a lap dance."
    si "My choice?"
    z "Sure, you can pick anyone. But pick me, please."
    scene 08_1519 with Dissolve(1)
    si "Would you like to have a lap dance, Layla?"
    la "I'd love one. My very first!"
    z "Dammit!"
    el "We need a good song though."
    va "I might have something. Give me a second."
    scene 08_1520 with Dissolve(1)
    va "How about this?"
    mc "Yeah, that's perfect."
    z "Why do you have that song on your phone?"
    va "Uhm..."
    mc "We might have chosen the wrong person to give a lap dance."
    scene 08_1521 with Dissolve(1)
    z "Do you have experience giving lap dances?"
    va "What? No!"
    z "She's blushing."
    la "Stop teasing her, guys!"
    scene black with Dissolve(1)
    pause 2
    scene 08_1522 with Dissolve(1)
    la "Be gentle."
    z "Haha."
    scene 08_1523 with Dissolve(1)
    ""
    scene 08_1524 with Dissolve(1)
    n "*slap*"
    la "Haha."
    z "Hey! No touching the dancer! Don't you know the rules?"
    scene 08_1525 with Dissolve(1)
    z "Damn... I wish I had that lap dance."
    va "..."
    z "Seems like it isn't her first time, either."
    el "Go, Sienna!"
    scene 08_1526 with Dissolve(1)
    la "Haha, that was great! And really sexy!"
    si "Thank you!"
    scene black with Dissolve(1)
    pause 2
    scene 08_1527 with Dissolve(1)
    z "YES! Finally! Dare! I pick dare!"
    z "Come on, [mc]. Give me a good one."
    la "No, it's my turn to choose a dare."
    z "*Sigh* Alright."
    scene 08_1528 with Dissolve(1)
    la "I dare you to make out with..."
    z "Yes! YES!"
    la "Your hand!"
    scene 08_1529 with Dissolve(1)
    el "Haha."
    z "What?"
    la "Make out with your hand."
    z "That's stupid!"
    la "You picked dare."
    z "..."
    scene 08_1530 with Dissolve(1)
    si "Haha."
    el "I think he's enjoying it. He even closed his eyes."
    la "That's so funny."
    scene 08_1531 with Dissolve(1)
    z "Shut up, Elena."
    z "I'd rather kiss my hand than you any day."
    el "And I'm grateful for that."
    la "Shush the both of you, and let's continue."
    scene 08_1532 with Dissolve(1)
    la "*Sigh* And that's what I get for shushing people..."
    z "Haha."
    la "I'll take another dare. They're more fun."
    scene 08_1533 with Dissolve(1)
    z "Time for my revenge, Layla."
    la "Whatchu got?"
    scene 08_1534 with Dissolve(1)
    z "Call [mc]'s mom at the restaurant and make a complaint about the food."
    la "That's just mean..."
    el "Pick another dare, Zach."
    z "No. Layla said dares are more fun!"
    el "*Sigh*"
    scene 08_1535 with Dissolve(1)
    la "Can you give me the number, [mc]?"
    mc "Sure."
    scene 08_1536 with Dissolve(1)
    la "It's ringing. I'm so nervous. I've never done a prank call before."
    mc "You haven't?"
    la "I've always hung up before someone picked up 'cause I was too scared."
    mc "Don't hang up now though. I actually want to know how she'll react. I have no clue."
    scene 08_1537 with Dissolve(1)
    br "Good evening. Rue Madison restaurant. What can I do for you?"
    la "Uhm..."
    la "Good evening."
    scene 08_1538 with Dissolve(1)
    la "I would like to talk to the manager, please."
    br "May I ask what this is about? Maybe I can help you."
    la "I'd rather talk to the manager directly."
    z "Savage!"
    scene 08_1539 with Dissolve(1)
    br "No problem, miss."
    br "Please hold for a moment."
    la "Of course."
    scene 08_1540 with Dissolve(1)
    z "What's happening?"
    la "She put me on hold. This is so nerve-wracking."
    mc "Do you know who it was?"
    la "A woman. She sounded young though."
    mc "That was probably Brooke."
    la "You know her?"
    mc "Yeah, I've worked together with her."
    scene 08_1541 with Dissolve(1)
    br "Hey Emily. I have a woman on the phone who wants to speak to you."
    m "What's it about?"
    br "I don't know, I asked but she wouldn't say. Only said she needed to talk to the manager."
    m "Okay, thank you, Brooke."
    scene 08_1542 with Dissolve(1)
    m "Good evening. This is Emily."
    la "Good evening, Emily. This is Lay... Uh, Kayla."
    mc "{i}(Kayla? Are you serious? Is that the best she came up with? Haha.){/i}"
    m "Hello, Kayla. How can I help you?"
    scene 08_1543 with Dissolve(1)
    la "I was at your restaurant yesterday and I had the risotto."
    la "But it was undercooked, the rice was very crunchy."
    la "I'd heard only good things before about the restaurant, so I was a little disappointed."
    m "I'm sorry you had a bad experience, Kayla."
    scene 08_1544 with Dissolve(1)
    m "Why didn't you mention it yesterday? We would've remade the dish for you."
    la "I was embarrassed, to be honest. I didn't want to make a big deal out of it."
    m "You don't have to be embarrassed. If the dish isn't made to standard, you'll get a new one."
    scene 08_1545 with Dissolve(1)
    m "How about you visit us again when you have time and I will personally take care of the dish? Free of charge, of course."
    la "There's no need, thank you for offering. I just wanted to get it off my chest."
    m "I understand. I'm so sorry again."
    scene 08_1546 with Dissolve(1)
    la "It's fine. Anyway, thank you for listening."
    m "Thank you very much for calling. I appreciate the feedback."
    la "Bye-bye."
    m "Bye, Kayla."
    scene 08_1547 with Dissolve(1)
    z "Haha. That was great, Layla. So believable. What did she say?"
    la "No, it wasn't. I feel really bad. She was so sweet about it. I didn't know what to say because I didn't want to be mean."
    la "I'm so sorry, [mc]."
    mc "It was a dare. Don't be sorry. You were really respectful."
    scene 08_1548 with Dissolve(1)
    la "I need a drink now."
    mc "What do you want?"
    la "Can you hand me the tequila?"
    mc "Sure."
    scene 08_1549 with Dissolve(1)
    el "Layla!"
    z "Haha. That's what I'm talking about."
    mc "Slow down a bit."
    scene 08_1550 with Dissolve(1)
    la "Bleh... That wasn't a good idea."
    z "Haha."
    el "I could've told you that before."
    scene black with Dissolve(1)
    pause 2
    n "Thirty minutes later."
    scene 08_1551 with Dissolve(1)
    el "Let's up the stakes a little."
    la "What do you have in mind?"
    el "If you're not doing the dare, instead of drinking, you need to take off a piece of clothing?"
    z "Hell yeah!"
    el "Is everyone cool with that?"
    mc "Sure..."
    scene 08_1552 with Dissolve(1)
    z "Here's one for you, Elena. Let's see if you dare to do this."
    z "Have a three-way kiss."
    el "That's it? Easy! Not taking off my shirt for this."
    if Layla_Dating == False:
        scene 08_1553 with Dissolve(1)
        el "Then I'll pick my two girls here."
        z "All girls? You sure you aren't a lesbian?"
        el "I'm not picking you, that's for sure!"
        scene 08_1554 with Dissolve(1)
        la "How does this even work?"
        si "I have no idea. I've never done it before, either."
        scene 08_1555 with Dissolve(1)
        mc "..."
        scene 08_1556 with Dissolve(1)
        z "Okay... That's kinda hot."
        z "I want to do that too! [mc], remember what we spoke about?"
        mc "..."
        scene 08_1557 with Dissolve(1)
        n "Haha."
    else:
        if Elena_Points >= 23:
            scene 08_1558 with Dissolve(1)
            el "*Whisper* Is it okay if..."
            z "Hey, what are you whispering about?"
            la "*Whisper* It's fine. It's just a game."
            scene 08_1559 with Dissolve(1)
            el "I'll take Layla and [mc] then."
            mc "{i}(That was unexpected. I'm a little excited, though. But...){/i}"
            menu:
                "Three-way-kiss[KoGa3AutoWTChange1]{size=-4}(Elena Week3 Saturday TC Threewaykiss, Elena Points+2) {/size} {/color}":
                    $ Elena_Week3_Saturday_TC_Threewaykiss = True
                    $ Elena_Points += 2
                    # Elena (30)
                    scene 08_1561 with Dissolve(1)
                    la "How does this even work?"
                    mc "I have no idea. Never done it before."
                    mc "Let's just try it."
                    scene 08_1562 with Dissolve(1)
                    ""
                    menu:
                        "Focus on Elena[KoGa3AutoWTChange1]{size=-4}(Layla Points-2, Elena Points+2) {/size} {/color}":
                            $ Layla_Points -= 2
                            $ Elena_Points += 2
                            # Elena (32)
                            scene 08_1563 with Dissolve(1)
                            la "..."
                            scene 08_1565 with Dissolve(1)
                            n "Haha."
                            la "That felt more like a third wheel than three-way..."
                            el "Haha, sorry."
                        "Focus on Layla[KoGa3AutoWTChange1]{size=-4}(Layla Points+2) {/size} {/color}":
                            $ Layla_Points += 2
                            # Layla (66)
                            scene 08_1564 with Dissolve(1)
                            el "..."
                            scene 08_1565 with Dissolve(1)
                            n "Haha."
                            el "That felt more like a third wheel than three-way..."
                            la "Haha, sorry."
                        "Stop kissing":
                            scene 08_1565 with Dissolve(1)
                            n "Haha."
                            mc "{i}(That was really nice. I hope we can do this again.){/i}"
                "Don't do it[KoGa3AutoWTChange1]{size=-4}(Elena Points-6) {/size} {/color}":
                    $ Elena_Points -= 6
                    scene 08_1560 with Dissolve(1)
                    mc "I'd rather not do it, sorry Elena."
                    el "..."
                    el "It's fine."
                    scene 08_1553 with Dissolve(1)
                    el "Then I'll pick my two girls here."
                    z "All girls? You sure you aren't a lesbian?"
                    el "I'm not picking you, that's for sure!"
                    scene 08_1554 with Dissolve(1)
                    la "How does this even work?"
                    si "I have no idea. I've never done it before, either."
                    scene 08_1555 with Dissolve(1)
                    mc "..."
                    scene 08_1556 with Dissolve(1)
                    z "Okay... That's kinda hot."
                    z "I want to do that too! [mc], remember what we spoke about?"
                    mc "..."
                    scene 08_1557 with Dissolve(1)
                    n "Haha."
        else:
            scene 08_1553 with Dissolve(1)
            el "Then I'll pick my two girls here."
            z "All girls? You sure you aren't a lesbian?"
            el "I'm not picking you, that's for sure!"
            scene 08_1554 with Dissolve(1)
            la "How does this even work?"
            si "I have no idea. I've never done it before, either."
            scene 08_1555 with Dissolve(1)
            mc "..."
            scene 08_1556 with Dissolve(1)
            z "Okay... That's kinda hot."
            z "I want to do that too! [mc], remember what we spoke about?"
            mc "..."
            scene 08_1557 with Dissolve(1)
            n "Haha."
    scene black with Dissolve(1)
    pause 2
    scene 08_1566 with Dissolve(1)
    mc "*Sigh* Of course. Me again."
    mc "I'm not letting you spin anymore, Layla."
    la "Haha, it's not on purpose."
    scene 08_1567 with Dissolve(1)
    el "Truth or dare?"
    mc "Dare!"
    el "Then I've got something for you."
    mc "Bring it."
    scene 08_1568 with Dissolve(1)
    el "Exchange the underwear you're wearing with someone else."
    mc "Eh? Are you serious?"
    el "Uh-huh."
    mc "..."
    scene 08_1569 with Dissolve(1)
    mc "I see where this is heading."
    el "You do?"
    mc "First, you change the rules to losing a piece of clothing if you don't do the dare."
    mc "Now you want me to wear girls' panties so if I..."
    el "I never said you have to exchange them with a girl. Turn to your left."
    scene 08_1570 with Dissolve(1)
    z "Yeah, it's an easy dare. Just pick me."
    z "We can exchange them real quick."
    mc "Uhm..."
    scene black with Dissolve(1)
    pause 2
    scene 06_383 with Dissolve(1)
    mc "I stayed the night at... Someone else's place. Didn't have a change."
    z "Right, the good day. Now I get it. My man!"
    z "But, why not wear the ones you wore yesterday then? Nothing wrong with that."
    z "When they're not dirty, why change? I sometimes wear mine for a week."
    mc "{i}(I'm so not picking Zach.){/i}"
    scene black with Dissolve(1)
    pause 2
    if Zach_Week3_Wednesday_TC_Girlshower == True:
        $ Layla_Friends = True
        $ Layla_Dating = False
        $ Layla_Points -= 4
        $ Elena_Points -= 10
        $ Valeria_Points -= 8
        scene 08_1571 with Dissolve(1)
        el "Don't look at me. I'm not doing it."
        z "Like he would pick you. He's seen everything there is to see already, anyway."
        mc "ZACH!"
        scene 08_1572 with Dissolve(1)
        el "What do you mean?"
        z "Forget I said anything."
        el "What do you mean, Zach!"
        scene 08_1573 with Dissolve(1)
        el "[mc]?"
        mc "Sorry, Elena! We were just snooping around and..."
        el "The showers?"
        mc "*Nods*"
        el "I knew I saw something. That was you?"
        mc "Yeah."
        scene 08_1574 with Dissolve(1)
        la "We're done with this game! Get out!"
        mc "Sorry, Elena! It wasn't on purpose."
        z "It was my fault!"
        la "Get out!"
        scene black with Dissolve(1)
        pause 2
        scene 08_1575 with Dissolve(1)
        z "Fuck man. That's on me."
        mc "..."
        z "[mc], I'm really sorry."
        menu:
            "Angry[KoGa3AutoWTChange1]{size=-4}(Zach Points-2) {/size} {/color}":
                $ Zach_Points -= 2
                scene 08_1576 with Dissolve(1)
                mc "Learn to shut your mouth once in a while, Zach!"
                z "Sorry. When I'm drinking I..."
                mc "Don't blame it on the alcohol now!"
                scene 08_1577 with Dissolve(1)
                z "Sorry, I..."
                mc "Just leave me alone."
                jump Week3_Saturday_TC_End_Bad
            "Calm[KoGa3AutoWTChange1]{size=-4}({i}Tori Week3 Saturday TC Sex: Valeria Friends, Valeria Points-4{/i}) {/size} {/color}":
                scene 08_1576a with Dissolve(1)
                mc "Why did you even say that? You should've known how they'd react to something like that."
                z "I don't know, bro. Maybe it's the alcohol."
                mc "..."
                z "I just wanted to stir Elena up a bit. Who knew she saw something when we were there."
                z "Sorry!"
                scene 08_1578 with Dissolve(1)
                z "What shall we do now?"
                mc "I'm going to sleep."
                jump Week3_Saturday_TC_End_Bad
    else:
        scene 08_1571 with Dissolve(1)
        el "Don't look at me. I'm not doing it."
        if Layla_Dating == False:
            scene 08_1579 with Dissolve(1)
            la "Even though I'm going to change, I'm not doing it, either."
            if Valeria_Points >= 7:
                if Tori_Week3_Saturday_TC_Sex == True:
                    $ Valeria_Friends = True
                    $ Valeria_Points -= 4
                    va "*Shakes head*"
                    mc "{i}(Val shaking her head. I thought she might be up for it.){/i}"
                    mc "I guess there's only one option..."
                    scene 08_1582 with Dissolve(1)
                    z "Come on. This will be quick."
                    mc "*Sigh* Yeah, okay..."
                    jump Week3_Saturday_TC_Swap_Zach
                else:
                    if Gabi_Week3_Saturday_TC_Sex == True:
                        $ Valeria_Friends = True
                        $ Valeria_Points -= 4
                        va "*Shakes head*"
                        mc "{i}(Val shaking her head. I thought she might be up for it.){/i}"
                        mc "I guess there's only one option..."
                        scene 08_1582 with Dissolve(1)
                        z "Come on. This will be quick."
                        mc "*Sigh* Yeah, okay..."
                        jump Week3_Saturday_TC_Swap_Zach
                    else:
                        scene 08_1581 with Dissolve(1)
                        va "I can do it. I don't mind."
                        mc "Uh... Really?"
                        z "What?"
                        scene 08_1590 with Dissolve(1)
                        mc "You sure?"
                        va "Uh-huh. It's just for fun."
                        menu:
                            "Valeria[KoGa3AutoWTChange1]{size=-4}(Valeria Points+2, Zach Points-4) {/size} {/color}":
                                $ Valeria_Points += 2
                                # Valeria (12)
                                $ Zach_Points -= 4
                                mc "Okay, thanks. Where should we change? My room?"
                                va "I have no key to mine, so yeah."
                                mc "That's right... Tori didn't give you a key."
                                mc "Let's go, then."
                                scene 08_1591 with Dissolve(1)
                                z "..."
                                z "Dude?"
                                jump Week3_Saturday_TC_Swap_Valeria
                            "Zach":
                                mc "Thank you, Val. But I think I'll go with Zach."
                                va "That's okay."
                                jump Week3_Saturday_TC_Swap_Zach
            else:
                mc "I guess there's only one option..."
                scene 08_1582 with Dissolve(1)
                z "Come on. This will be quick."
                mc "*Sigh* Yeah, okay..."
                jump Week3_Saturday_TC_Swap_Zach
        else:
            if Valeria_Points >= 9:
                if Tori_Week3_Saturday_TC_Sex == True:
                    $ Valeria_Friends = True
                    $ Valeria_Points -= 4
                    scene 08_1615 with Dissolve(1)
                    la "I'll do it!"
                    mc "Really?"
                    el "Yeah, really? You know you have to wear his underwear too, right?"
                    la "I don't mind. Besides I need to change, anyway."
                    el "Hmm..."
                    menu:
                        "Layla":
                            scene 08_1509 with Dissolve(1)
                            mc "I'll go with Layla!"
                            mc "You sure you don't mind?"
                            la "I don't."
                            mc "Thanks."
                            jump Week3_Saturday_TC_Swap_Layla
                        "Zach":
                            mc "Thank you, Layla. But I think I'll go with Zach."
                            la "That's okay."
                            jump Week3_Saturday_TC_Swap_Zach
                else:
                    if Gabi_Week3_Saturday_TC_Sex == True:
                        $ Valeria_Friends = True
                        $ Valeria_Points -= 4
                        scene 08_1615 with Dissolve(1)
                        la "I'll do it!"
                        mc "Really?"
                        el "Yeah, really? You know you have to wear his underwear too, right?"
                        la "I don't mind. Besides I need to change, anyway."
                        el "Hmm..."
                        menu:
                            "Layla":
                                scene 08_1509 with Dissolve(1)
                                mc "I'll go with Layla!"
                                mc "You sure you don't mind?"
                                la "I don't."
                                mc "Thanks."
                                jump Week3_Saturday_TC_Swap_Layla
                            "Zach":
                                mc "Thank you, Layla. But I think I'll go with Zach."
                                la "That's okay."
                                jump Week3_Saturday_TC_Swap_Zach
                    else:
                        scene 08_1615 with Dissolve(1)
                        la "I'll do it!"
                        mc "Really?"
                        el "Yeah, really? You know you have to wear his underwear too, right?"
                        la "I don't mind. Besides I need to change, anyway."
                        el "Hmm..."
                        scene 08_1581 with Dissolve(1)
                        va "I can do it too. I don't mind."
                        mc "Uh..."
                        z "What?"
                        menu:
                            "Layla":
                                scene 08_1509 with Dissolve(1)
                                mc "I'll go with Layla!"
                                mc "You sure you don't mind?"
                                la "I don't."
                                mc "Thanks."
                                jump Week3_Saturday_TC_Swap_Layla
                            "Valeria[KoGa3AutoWTChange1]{size=-4}(Layla Points-8, Valeria Points+2, Zach Points-4) {/size} {/color}":
                                $ Layla_Points -= 8
                                $ Valeria_Points += 2
                                # Valeria (12)
                                $ Zach_Points -= 4
                                scene 08_1590 with Dissolve(1)
                                mc "You sure?"
                                va "Uh-huh. It's just for fun."
                                mc "Okay, thanks. Where should we change? My room?"
                                va "I have no key to mine, so yeah."
                                mc "That's right... Tori didn't give you a key."
                                mc "Let's go, then."
                                scene 08_1591 with Dissolve(1)
                                z "..."
                                z "Dude?"
                                jump Week3_Saturday_TC_Swap_Valeria
                            "Zach":
                                mc "Thank you, girls. But I think I'll go with Zach."
                                la "That's okay."
                                jump Week3_Saturday_TC_Swap_Zach
            else:
                scene 08_1615 with Dissolve(1)
                la "I'll do it!"
                mc "Really?"
                el "Yeah, really? You know you have to wear his underwear too, right?"
                la "I don't mind. Besides I need to change, anyway."
                el "Hmm..."
                menu:
                    "Layla":
                        scene 08_1509 with Dissolve(1)
                        mc "You sure you don't mind?"
                        la "I don't."
                        mc "Thanks."
                        jump Week3_Saturday_TC_Swap_Layla
                    "Zach":
                        mc "Thank you, Layla. But I think I'll go with Zach."
                        la "That's okay."
                        jump Week3_Saturday_TC_Swap_Zach

label Week3_Saturday_TC_Swap_Layla:
    $ Layla_Week3_Saturday_TC_Swap = True
    scene black with Dissolve(1)
    pause 2
    scene 08_1616 with Dissolve(1)
    mc "You didn't have to do this, but thank you so very much!"
    mc "I really don't want to wear Zach's underwear."
    la "Any specific reason?"
    mc "Trust me. You don't want to know."
    la "I'll take your word for it."
    scene 08_1617 with Dissolve(1)
    la "And you're welcome!"
    mc "..."
    scene 08_1618 with Dissolve(1)
    mc "That wasn't part of the dare, but I liked it."
    la "Hehe, good."
    la "But now it's time for you to turn around and throw me your underwear."
    la "And no peeking!"
    mc "I'll try."
    la "Uh-huh..."
    scene 08_1595 with Dissolve(1)
    mc "{i}(I'm trying, Layla but I have to look.){/i}"
    scene 08_1619 with Dissolve(1)
    mc "..."
    mc "{i}(This will be the first time I've worn pink underwear...){/i}"
    mc "{i}(They look good on her.){/i}"
    scene 08_1620 with Dissolve(1)
    mc "{i}(Watching her undress is so hot.){/i}"
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 08_1621 at moveup
    pause 3
    mc "{i}(I wish you'd turn around now.){/i}"
    mc "{i}(I don't even care if you catch me peeking.){/i}"
    mc "{i}(This girl is so pretty.){/i}"
    mc "{i}(Okay, enough. Let's start undressing too.){/i}"
    scene 08_1622 with Dissolve(1)
    la "When you're ready, can you throw me yours?"
    mc "Will do."
    la "Mine is already lying at your feet."
    mc "I can see that. Nice colour."
    la "Haha, right? They'll look good on you."
    scene 08_1623 with Dissolve(1)
    mc "Here you go."
    la "Thanks. They're soft. Didn't expect that."
    scene 08_1624 with Dissolve(1)
    mc "{i}(What is she doing?){/i}"
    mc "{i}(Wait... Is she...){/i}"
    scene 08_1625 with Dissolve(1)
    mc "Are you smelling my underwear?"
    la "What? NO!"
    mc "Haha, you so are."
    mc "I didn't know you were that weird."
    scene 08_1626 with Dissolve(1)
    la "I wasn't doing that!"
    mc "Uh..."
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 08_1627 at moveup
    pause 3
    mc "{i}(Thank you! Thank you! Thank you!){/i}"
    la "What?"
    scene 08_1628 with vpunch
    la "Aaah... Nooo..."
    mc "..."
    scene 08_1629 with vpunch
    la "Aaah!"
    la "Turn around!"
    mc "Haha."
    scene 08_1630 with Dissolve(1)
    la "Don't laugh!"
    la "Did you see?"
    mc "Well... I did."
    la "Everything?"
    mc "Hmm, yeah. Want to see mine to make it even?"
    la "Nooo..."
    mc "Haha."
    scene 08_1631 with Dissolve(1)
    la "I was just curious, okay?"
    la "Please don't tell anyone."
    mc "I won't. But the thing I will do is smell yours!"
    scene 08_1632 with Dissolve(1)
    la "Don't you dare!"
    mc "{i}(She's hugging me. Completely naked...){/i}"
    scene 08_1633 with Dissolve(1)
    la "Come on, let's get ready or the others will start asking why we took so long."
    mc "Uhm... Give me a minute. Your panties won't fit at the moment."
    la "Huh? What do you mean? They stretch."
    scene 08_1634 with Dissolve(1)
    mc "..."
    mc "Not enough."
    la "And don't turn around!"
    mc "Trust me, I won't."
    scene black with Dissolve(1)
    pause 2
    scene 08_1635 with Dissolve(1)
    la "I'm ready. Turn around, have a look."
    mc "I don't know if I want to turn around. This looks ridiculous."
    la "It looks good from the back. Like a pink speedo."
    mc "Funny..."
    scene 08_1636 with Dissolve(1)
    la "Haha."
    mc "Okay, you can stop laughing now."
    la "Haha, sorry. I pictured it differently in my mind."
    mc "This stays between us!"
    la "The others know though."
    mc "But they won't see."
    la "You're not going to show them?"
    mc "Hell no!"
    scene 08_1637 with Dissolve(1)
    la "So, what do you think of mine?"
    mc "Hmm... Not bad, but I prefer you in them."
    la "Haha."
    scene 08_1638 with Dissolve(1)
    la "These are comfortable. I might just keep them."
    mc "Sure. You look better in them than I do."
    la "Hehe."
    scene 08_1639 with Dissolve(1)
    la "When we're back, please don't tell them..."
    mc "That you sniffed my underwear?"
    la "I didn't do that!"
    la "But yes."
    mc "Haha, don't worry."
    la "Thanks, [mc]."
    $ renpy.end_replay()
    scene black with Dissolve(1)
    pause 2
    scene 08_1640 with Dissolve(1)
    el "Oh, they're back. Took you long enough!"
    la "Hey."
    el "Show us! Show us!"
    mc "*Sigh* I am so not showing you."
    scene 08_1641 with Dissolve(1)
    el "But how do we know you are wearing Layla's underwear?"
    el "We need some proof."
    mc "Not going to happen!"
    la "You can trust me. He's wearing my underwear."
    scene 08_1642 with Dissolve(1)
    el "How was it?"
    la "I did something embarrassing."
    el "You did? Tell me later."
    scene 08_1643 with Dissolve(1)
    va "How does it feel to wear a girl's underwear?"
    mc "Heh. It's alright, I guess. Just a little tighter than I'd like."
    jump Week3_Saturday_Evening2

label Week3_Saturday_TC_Swap_Valeria:
    if _in_replay:
        $ Valeria_Points = 4
        $ Valeria_Week3_Saturday_TC_Peek = False
    $ Valeria_Week3_Saturday_TC_Swap = True
    scene black with Dissolve(1)
    pause 2
    scene 08_1592 with Dissolve(1)
    mc "You didn't have to do this, but thank you so very much!"
    mc "I really don't want to wear Zach's underwear."
    va "Any specific reason?"
    mc "Trust me. You don't want to know."
    va "Haha. That bad?"
    scene 08_1593 with Dissolve(1)
    mc "By the way. You're not wearing any weird laced underwear or anything like that, right?"
    va "Weird?"
    mc "I don't mean weird..."
    va "Maybe I'm not wearing any and you'll have to go commando."
    mc "What? I don't know if you're joking or not."
    va "I guess you'll find out soon enough."
    mc "..."
    scene 08_1594 with Dissolve(1)
    va "You can turn around now."
    mc "Oh yeah, sorry."
    scene 08_1595 with Dissolve(1)
    mc "So... You didn't kiss Zach, huh? At the pool."
    va "No."
    mc "Would you kiss him if someone dared you?"
    va "..."
    menu:
        "Peek[KoGa3AutoWTChange1]{size=-4}(Valeria Week3 Saturday TC Peek, Valeria Points-6, Valeria Friends) {/size} {/color}":
            $ Valeria_Week3_Saturday_TC_Peek = True
            $ Valeria_Points -= 6
            $ Valeria_Friends = True
            scene 08_1596 with Dissolve(1)
            mc "{i}(She's wearing underwear...){/i}"
            scene 08_1597 with Dissolve(1)
            mc "{i}(I can't stop watching...){/i}"
            scene black with Dissolve(1)
            transform moveup:
                xalign 0.5 yalign 1.0
                linear 5.0 yalign 0.0
            show 08_1598 at moveup
            pause 3
            mc "{i}(That's so hot...){/i}"
            mc "{i}(I wish she would take her top off too.){/i}"
            scene 08_1599 with vpunch
            va "Hey! Why are you looking?"
            mc "You wouldn't know that I was looking if you didn't turn around yourself."
            scene 08_1600 with Dissolve(1)
            va "*Sigh*"
            va "Can you give me your underwear?"
            mc "Sure."
        "Don't":
            scene 08_1600 with Dissolve(1)
            va "Uhm. Can you throw me your underwear?"
            mc "Sure."
    scene black with Dissolve(1)
    pause 2
    scene 08_1601 with Dissolve(1)
    mc "Oh shit... I don't know if I should laugh or cry. What am I doing..."
    mc "Please don't tell anyone."
    va "I don't have to. Four other people know already."
    mc "*Sigh*"
    va "Are you ready?"
    mc "Yeah, you?"
    scene 08_1602 with Dissolve(1)
    va "Haha, they look good on you. It accentuates your butt!"
    mc "Very funny."
    va "Can you turn around?"
    mc "No. This looks ridiculous."
    va "Please! I'll show you mine if you show me yours?"
    mc "*Sigh*"
    scene 08_1603 with Dissolve(1)
    va "Haha."
    mc "..."
    scene 08_1604 with Dissolve(1)
    va "You were right! Haha."
    mc "I'm so glad you're enjoying this so much."
    va "It's very brave..."
    mc "Oh, not that again. You know, one of these days I'll come up with a name for you, and you're not gonna like it."
    va "Haha."
    mc "You're laughing now..."
    va "Haha."
    scene 08_1605 with Dissolve(1)
    mc "Still laughing, huh?"
    va "Aah, [mc]!"
    scene 08_1606 with vpunch
    va "..."
    mc "..."
    scene 08_1607 with Dissolve(1)
    mc "{i}(Damn, she's pretty!){/i}"
    mc "{i}(Don't look at me like that or I won't be able to stop myself from kissing you.){/i}"
    mc "..."
    scene 08_1608 with Dissolve(1)
    mc "Sorry. You've told me before that others just grab you and you don't like it. And now I'm doing the same..."
    va "No, it's ... okay."
    mc "Anyway, ready to go back?"
    va "Yes, but before that..."
    scene 08_1609 with Dissolve(1)
    va "What do you think of this look?"
    mc "Not bad, but I would've preferred seeing you in the ones I'm wearing now."
    if Valeria_Week3_Saturday_TC_Peek == True:
        va "Hmm... I'm pretty sure you did!"
        mc "..."
    else:
        va "Hmm..."
    scene 08_1610 with Dissolve(1)
    va "These are very comfortable. I might just keep them."
    va "Want to trade?"
    mc "Uhm..."
    va "I'm kidding... Maybe..."
    $ renpy.end_replay()
    scene black with Dissolve(1)
    pause 2
    scene 08_1611 with Dissolve(1)
    la "Oh, they're back."
    va "Hey."
    el "Show us! Show us!"
    mc "*Sigh* I am so not showing you."
    scene 08_1612 with Dissolve(1)
    el "But how do we know you're wearing Val's underwear?"
    el "We need some proof."
    mc "Not going to happen!"
    scene 08_1613 with Dissolve(1)
    va "You can trust me. He's wearing my underwear."
    va "And as you can see, I'm wearing his."
    z "Val, what are you doing?"
    scene 08_1614 with Dissolve(1)
    mc "Thank you."
    va "You're welcome. It was fun."
    jump Week3_Saturday_Evening2

label Week3_Saturday_TC_Swap_Zach:
    $ Zach_Week3_Saturday_TC_Swap = True
    scene 08_1580 with Dissolve(1)
    mc "Let's get this over with, Zach."
    z "Right here?"
    mc "No... We'll go to our room. Be right back, girls."
    scene 08_1583 with Dissolve(1)
    el "And we need proof!"
    mc "Yeah, yeah, don't worry."
    la "I'm going to change too, in the meantime."
    scene black with Dissolve(1)
    pause 2
    scene 08_1584 with Dissolve(1)
    z "The game will get really interesting now."
    z "We need to come up with some dares that the girls won't do, so they'll lose their clothes."
    z "It shouldn't be that hard, right?"
    mc "Who knows. They've surprised me already."
    scene 08_1585 with Dissolve(1)
    mc "What even are those?"
    z "What do you mean? These are my original BlueFoxes."
    z "And they are the limited 'lovable' edition. Very comfortable."
    z "Just feel how soft they are."
    mc "I'm just going to put them on and be done with this."
    scene 08_1586 with Dissolve(1)
    z "What do you think? Looks good on me, huh!"
    mc "..."
    mc "Please, don't ever do that again."
    scene black with Dissolve(1)
    pause 2
    scene 08_1587 with Dissolve(1)
    el "Oh, they're back."
    la "Show us! Show us!"
    mc "*Sigh*"
    scene 08_1588 with Dissolve(1)
    mc "There! Happy?"
    $ achievement.grant("ACHIEVEMENT_LOVABLE_EDITION")
    $ achievement.sync()
    el "Haha. You look so cute in those hearts!"
    mc "Funny!"
    scene 08_1589 with Dissolve(1)
    el "But how do we know those are Zach's and not yours?"
    mc "Just look at them... Do you really think I'd wear something like this?"
    z "Hey! That's my most precious pair. They're original limited-edition Blue..."
    mc "Foxes. I know."
    jump Week3_Saturday_Evening2

label Week3_Saturday_Evening2:
    scene black with Dissolve(1)
    pause 2
    scene 08_1644 with Dissolve(1)
    z "Woohoo!"
    z "About time it's my turn again."
    z "I'll pick dare, of course!"
    scene 08_1645 with Dissolve(1)
    el "Then I want you to sing..."
    z "What? No!"
    el "You don't even know what I want you to sing."
    z "I don't care. Why do I only get stupid dares? Sienna had to lap dance, you got a three-way kiss, [mc] had..."
    z "I'm not doing it!"
    el "That's fine with me. Lose a piece of clothing and we'll continue."
    scene 08_1646 with Dissolve(1)
    z "There! Happy?"
    el "On second thoughts, put your shirt back on."
    z "Heh. Getting turned on?"
    el "Dios mío..."
    scene 08_1647 with Dissolve(1)
    z "[mc], can you hand me the vodka. I need a few drinks..."
    mc "Sure."
    scene black with Dissolve(1)
    pause 2
    scene 08_1648 with Dissolve(1)
    mc "Finally you again, Val. That's only your second time, right?"
    va "Yep. Got lucky so far. Or unlucky? Depends on how you see it, I guess."
    mc "Haha. Anyway. Truth or dare?"
    va "Dare!"
    scene 08_1649 with Dissolve(1)
    z "Oh! Nice!"
    mc "{i}(Let's try to help him out a bit. But I can't just dare her to kiss Zach, it'd be too obvious.){/i}"
    mc "{i}(Do I even want her to kiss him? Hmm... But I promised I'd help him.){/i}"
    scene 08_1650 with Dissolve(1)
    mc "I dare you to lick someone's face."
    va "Lick?"
    mc "Yes, all the way from the bottom to the top."
    mc "Or lose a piece of clothing."
    va "No, I'll do it."
    mc "{i}(I did my part. Now she only has to choose Zach.){/i}"
    scene 08_1660 with Dissolve(1)
    va "..."
    scene 08_1651 with Dissolve(1)
    mc "{i}(Wait...){/i}"
    mc "{i}(She isn't going to pick me, or...?){/i}"
    if Valeria_Points >= 9:
        scene 08_1652 with Dissolve(1)
        mc "You're picking me?"
        va "Yes, do you mind?"
        mc "{i}(Not what I had in mind, but...){/i}"
        mc "Uhm... No, I don't."
        scene 08_1653 with Dissolve(1)
        mc "{i}(I'm actually excited for this.){/i}"
        mc "{i}(Reminds me of someone who did the same.){/i}"
        show 08_1654
        ""
        scene 08_1661 with Dissolve(1)
        n "Haha."
    else:
        if Tori_Week3_Saturday_TC_Sex == True:
            scene 08_1652 with Dissolve(1)
            mc "Are you?"
            va "No..."
            va "*Whispers* I know what you did before!"
            mc "{i}(What? Does she know I did this for Zach? Or is she talking about something else?){/i}"
        else:
            if Gabi_Week3_Saturday_TC_Sex == True:
                scene 08_1652 with Dissolve(1)
                mc "Are you?"
                va "No..."
                va "*Whispers* I know what you did before!"
                mc "{i}(What? Does she know I did this for Zach? Or is she talking about something else?){/i}"
            else:
                scene 08_1652 with Dissolve(1)
                mc "Are you?"
                va "No..."
                mc "{i}(Too bad...){/i}"
        scene 08_1655 with Dissolve(1)
        va "Do you mind if I pick you, Layla?"
        la "Not at all."
        scene 08_1656 with Dissolve(1)
        mc "{i}(I'm kinda jealous.){/i}"
        mc "{i}(Reminds me of someone who did the same.){/i}"
        show 08_1657
        ""
        scene 08_1662 with Dissolve(1)
        n "Haha."
    scene 08_1658 with Dissolve(1)
    z "..."
    scene 08_1659 with Dissolve(1)
    z "..."
    scene black with Dissolve(1)
    pause 2
    n "Sometime later, after more dares and alcohol."
    scene 08_1663 with Dissolve(1)
    mc "Oh, this is great!"
    el "Layla, what have you done?"
    la "How is this my fault? I just spun the bottle..."
    scene 08_1664 with Dissolve(1)
    el "Can't you go in my place? You're still wearing pants."
    la "If you didn't reject all those dares, you'd still be wearing your clothes too."
    el "..."
    scene 08_1665 with Dissolve(1)
    el "[mc]!"
    mc "Nuh-uh... Don't even try. This is payback for the underwear swap."
    el "*Sigh* Fine! What do I have to do?"
    scene 08_1666 with Dissolve(1)
    mc "{i}(Hmm. I need something she won't do.){/i}"
    mc "..."
    mc "{i}(Got it!){/i}"
    mc "I dare you to kiss Zach!"
    z "No!"
    scene 08_1667 with Dissolve(1)
    el "Sure."
    mc "Heh? You didn't even think about it."
    el "I'm not stripping down for a kiss."
    scene 08_1668 with Dissolve(1)
    el "Come here, Zach!"
    z "Do I have a say in this?"
    scene 08_1669 with Dissolve(1)
    mc "I didn't expect her to do it."
    la "You want her to be naked that badly?"
    mc "You're trying to do the same with me with your dares..."
    la "Hehe. The night's still young!"
    scene 08_1670 with Dissolve(1)
    mc "..."
    scene 08_1671 with Dissolve(1)
    mc "What the hell was that?"
    el "You said kiss. I kissed him on the cheek. That's still a kiss in my book."
    el "You should've been more specific."
    if Elena_Points >= 25:
        mc "{i}(I'm actually happy she didn't.){/i}"
    else:
        mc "..."
    scene 08_1672 with Dissolve(1)
    mc "Would you have kissed... Made out with him if I'd specified better?"
    el "Who knows..."
    mc "Elena!"
    el "Haha."
    scene black with Dissolve(1)
    pause 2
    scene 08_1673 with Dissolve(1)
    va "Uh..."
    mc "What did you do, Elena? Is your kiss poisonous or something?"
    if Elena_Week3_Saturday_TC_Threewaykiss == True:
        scene 08_1672 with Dissolve(1)
        el "You're still alive."
        mc "Maybe I'm immune."
        el "Want to kiss me again and find out?"
        mc "..."
        el "Haha."
        scene 08_1673 with Dissolve(1)
    else:
        el "Haha."
    la "Is he passed out?"
    va "I think so. He drank a lot."
    el "Push him off before he starts drooling on your leg."
    mc "I'd better carry him to our room. Call it a night?"
    scene 08_1674 with Dissolve(1)
    la "What, no!"
    la "It just started to get interesting. And it's still early."
    mc "Haha. You want to keep playing until everyone is naked or something?"
    la "Maybe..."
    el "Just put him in one of the beds here for now."
    scene 08_1675 with Dissolve(1)
    mc "You're heavy, you know that?"
    el "Of course, you chose my bed."
    mc "Haha, I didn't know it was yours."
    el "Layla, we're switching beds!"
    mc "Enjoy Elena's bed, Zach! Might be a once in a lifetime experience!"
    if Elena_Points >= 25:
        jump Week3_Saturday_TC_End_Elena
    else:
        scene black with Dissolve(1)
        pause 2
        scene 08_1676 with Dissolve(1)
        n "The game continued until late into the night."
        scene 08_1677 with Dissolve(1)
        ""
        scene 08_1678 with Dissolve(1)
        ""
        scene 08_1679 with Dissolve(1)
        ""
        scene 08_1680 with Dissolve(1)
        ""
        if Valeria_Week3_Saturday_TC_Swap == False:
            scene 08_1681 with Dissolve(1)
            ""
        else:
            scene 08_1681a with Dissolve(1)
            ""
        scene 08_1682 with Dissolve(1)
        ""
        scene black with Dissolve(2)
        pause 2
        jump Week3_Sunday_TC_End

label Week3_Saturday_TC_End_Elena:
    if _in_replay:
        $ Valeria_Week3_Saturday_TC_Swap = True
    scene black with Dissolve(1)
    pause 2
    scene 08_1676 with Dissolve(1)
    n "The game continued until late in the night."
    scene 08_1677 with Dissolve(1)
    ""
    scene 08_1678 with Dissolve(1)
    ""
    scene 08_1679 with Dissolve(1)
    ""
    scene 08_1680 with Dissolve(1)
    ""
    if Valeria_Week3_Saturday_TC_Swap == False:
        scene 08_1681 with Dissolve(1)
        ""
    else:
        scene 08_1681a with Dissolve(1)
        ""
    scene 08_1682 with Dissolve(1)
    ""
    scene 08_1683 with Dissolve(1)
    ""
    scene 08_1684 with Dissolve(1)
    ""
    scene black with Dissolve(4)
    pause 2
    $ renpy.end_replay()
    jump Week3_Sunday_TC_End

label Week3_Sunday_TC_End:
    scene black with Dissolve(2)
    pause 2
    scene 08_1685 with Dissolve(1)
    z "Nggh."
    z "{i}(What time is it?){/i}"
    scene 08_1686 with Dissolve(1)
    z "{i}(Oh... Is that?){/i}"
    z "..."
    z "{i}(Haha, I finally did it!){/i}"
    z "{i}(I knew she liked me. I love you too, Va...){/i}"
    scene 08_1687 with vpunch
    z "{i}(No... No... Noooo!){/i}"
    z "{i}(Am I still dreaming? This...){/i}"
    z "{i}(Not Elena! No!){/i}"
    z "{i}(This can't be happening!){/i}"
    z "{i}(What is she doing here?){/i}"
    scene 08_1688 with Dissolve(1)
    z "{i}(No-no-no...){/i}"
    z "{i}(My first time was with Elena?){/i}"
    z "{i}(Fuck! What have I done...){/i}"
    z "{i}([mc]! Where is [mc]?){/i}"
    scene 08_1689 with Dissolve(1)
    z "{i}(She... With him?){/i}"
    z "{i}(Can this day get any worse?){/i}"
    if Valeria_Week3_Saturday_TC_Swap == False:
        scene 08_1690 with Dissolve(1)
        z "*Whisper* [mc]!"
        z "*Whisper* Hey, [mc]!"
    else:
        scene 08_1690a with Dissolve(1)
        z "*Whisper* [mc]!"
        z "*Whisper* Hey, [mc]!"
    scene 08_1691 with Dissolve(1)
    mc "*Whisper* Zach... It's still early! What do you want?"
    z "*Whisper* I need to talk to you."
    mc "*Whisper* This isn't what you think."
    z "*Whisper* No, it's... Let's get back to our room."
    mc "..."
    if Valeria_Points >= 9:
        mc "*Whisper* Give me a second."
        scene 08_1692 with Dissolve(1)
        va "[mc]?"
        mc "*Whisper* It's still early, you can sleep some more."
        mc "*Whisper* I'll go back before a teacher finds out."
    else:
        mc "*Whisper* Give me a second."
    scene black with Dissolve(1)
    pause 2
    scene 08_1693 with Dissolve(1)
    mc "My head still hurts."
    mc "How aren't you hungover after what you drank last night."
    z "It wasn't that much."
    mc "Heh... You know you passed out, right?"
    mc "So, what do you want?"
    scene 08_1694 with Dissolve(1)
    z "Did you have sex with Valeria?"
    mc "No, I didn't."
    z "Layla?"
    mc "No."
    z "With anyone?"
    mc "What's up with these questions?"
    scene 08_1695 with Dissolve(1)
    z "I had sex!"
    mc "What? Had a good dream or something?"
    z "No, man. Real sex."
    mc "{i}(Real sex?){/i}"
    mc "What are you talking about? With who?"
    scene 08_1696 with Dissolve(1)
    z "Elena!"
    mc "Elena? Haha. Now I know for sure you were dreaming."
    z "No, I swear. Why would I make this up?"
    mc "Elena?"
    z "Yeah!"
    mc "You don't like her."
    z "I know."
    mc "..."
    scene 08_1697 with Dissolve(1)
    mc "Do you actually remember anything from yesterday?"
    z "No, but I feel different, you know what I mean?"
    mc "Not really, no. I'm still confused."
    scene 08_1698 with Dissolve(1)
    z "Did you take off my pants?"
    mc "No, I just put you on the bed when you were passed out."
    z "Then explain why I was naked when I woke up."
    mc "I have no idea. Maybe you took them off during the night?"
    z "I've never done that before. Like I said. I had sex with Elena."
    scene 08_1699 with Dissolve(1)
    mc "..."
    z "Fuck!"
    z "Don't tell anyone. No one can know I lost my virginity to Elena. That's so embarrassing!"
    mc "{i}(Embarrassing? I think you can call yourself lucky!){/i}"
    mc "Uhm... Sure."
    z "Especially not Miguel!"
    z "I need a shower! Wash this filth of me."
    mc "*Shakes head*"
    scene black with Dissolve(1)
    pause 2
    n "Sunday, 08:23. The drive back to Madison Springs."
    scene 08_1702 with Dissolve(1)
    mc "{i}(Hehe, they're all still tired...){/i}"
    z "Hey, [mc]. Come sit here."
    scene 08_1703 with Dissolve(1)
    mc "Why are you sitting so far from the girls?"
    z "You know why. I can't deal with Elena now."
    scene black with Dissolve(2)
    pause 2
    scene 08_1704 with Dissolve(1)
    mc "They should've given us at least one more day off."
    el "Totally agree with you."
    la "It's only a week until spring break, though. We'll have a week of vacation then."
    mc "True. Can't wait. Let's come up with some ideas for what we can do during our time off."
    scene 08_1705 with Dissolve(1)
    el "Who says we want to hang out with you?"
    el "Maybe we need a vacation from you, too!"
    la "Haha."
    if Elena_Points >= 25:
        mc "Ah, there she is. Good old Elena. I missed her!"
        scene 08_1706 with Dissolve(1)
        el "Hey!"
        mc "You sure you don't want to hang out with me?"
        el "I'm getting more sure every second."
        mc "Haha."
    else:
        mc "Ah, there she is. Good old Elena. I missed her!"
    scene 08_1707 with Dissolve(1)
    mc "Anyway, I'm heading home. I guess I'll see you again tomorrow."
    el "Bye."
    la "Bye, [mc]."
    va "Bye-bye."
    jump Week3_Sunday

label Week3_Saturday_TC_End_Bad:
    scene black with Dissolve(2)
    pause 2
    n "Sunday, 08:23. The drive back to Madison Springs."
    scene 08_1700 with Dissolve(1)
    mc "{i}(I think I'll look for another place to sit.){/i}"
    scene 08_1701 with Dissolve(1)
    mc "{i}(Damn...){/i}"
    mc "{i}(How do I get out of this mess? A simple sorry probably won't do.){/i}"
    jump Week3_Sunday

label Week3_Sunday:
    scene black with Dissolve(2)
    pause 2
    stop music fadeout 1.0
    play music ("Music/LoFi Indie 3.mp3", "Music/LoFi Indie 1.mp3", "Music/LoFi Indie 2.mp3") volume 0.2
    scene 08_1708 with Dissolve(1)
    m "Hey, [mc]!"
    mc "{i}(Oh... Mom's picking me up.){/i}"
    scene 08_1709 with Dissolve(1)
    mc "Hey, Mom."
    mc "Thanks for picking me up. How did you know when we'd arrive?"
    m "I called the school on Friday to ask."
    if Zach_Week3_Wednesday_TC_Girlshower == False:
        scene 08_1710 with Dissolve(1)
        m "I see you've made a few friends already."
        mc "I have."
        m "All girls, huh?"
        mc "Uhm..."
        scene 08_1711 with Dissolve(1)
        m "They're all pretty."
        m "Any of them your girlfriend?"
        mc "Mom!"
        if Alexis_Dating == True:
            scene 08_1712 with Dissolve(1)
            m "I know Alexis is your girlfriend."
            mc "What? No, she isn't either."
            m "Uh-huh."
        else:
            scene 08_1712 with Dissolve(1)
            mc "None of them is my girlfriend."
            m "None of them? Is there someone else?"
            mc "No!"
        m "Come on, get in. You can tell me all about..."
        mc "I'm not talking about girlfriends with you!"
        m "I meant training camp."
        scene 08_1713 with Dissolve(1)
        m "So, how was it?"
    else:
        scene 08_1713 with Dissolve(1)
        m "So, how was it?"
    mc "Really good actually. Training was tough, but we had lots of fun."
    m "And the competition?"
    if MC_Week3_Saturday_TC_Win == True:
        scene 08_1714 with Dissolve(1)
        mc "First place!"
        m "[mc]! Congratulations! Now I wish I could've come to watch."
        mc "No worries, there's always a next time."
        scene 08_1715 with Dissolve(1)
        mc "There was a scout from MSU who wanted a chat with me."
        m "What did he say?"
        mc "He was impressed by my performance and will keep following my progress over the next few months."
        mc "I might be able to get a full scholarship, even."
        m "That's amazing, [mc]! I'm so proud of you."
    else:
        scene 08_1714a with Dissolve(1)
        mc "Not that great. Fourth place..."
        m "Fourth place is still good."
        mc "Should've done better. I messed up my start."
    scene black with Dissolve(1)
    pause 2
    scene 08_1716 with Dissolve(1)
    mc "How was your week?"
    m "The usual. Nothing special. The restaurant is getting very busy."
    m "Oh... Except..."
    mc "What?"
    scene 08_1717 with Dissolve(1)
    m "When was it? Yesterday? Yes, yesterday."
    m "I got my first complaint."
    mc "Complaint?"
    m "Yes, about the food in the restaurant."
    mc "You've never had a bad review before?"
    scene 08_1718 with Dissolve(1)
    m "No, no, we've had those."
    m "There're always some trolls on the internet who try to bring you down by leaving bad reviews or writing other nonsense."
    mc "Haha, trolls."
    m "That's what they're called, no?"
    mc "You're right, trolls is the word. It's just funny to hear you say it."
    m "Why? We already had internet when I was your age. I'm not that old."
    scene 08_1719 with Dissolve(1)
    m "Anyway..."
    m "I had this woman call the restaurant and ask to speak to the manager."
    m "She had the risotto but said she was disappointed with the cooking."
    mc "{i}(Oh no... That was Layla.){/i}"
    m "She was friendly about it but it still shook me a bit. I didn't know how to react to it."
    mc "{i}(You reacted just fine. Layla felt really bad about it.){/i}"
    mc "{i}(Should I tell her?){/i}"
    menu:
        "Yes[KoGa3AutoWTChange1]{size=-4}(Emily Week3 Sunday DareTell, Emily Points+2) {/size} {/color}":
            $ Emily_Week3_Sunday_DareTell = True
            $ Emily_Points += 2
            # Emily (16)
            scene 08_1720 with Dissolve(1)
            mc "Uhm, Mom. I have to tell you something."
            mc "It was a joke."
            m "What was a joke?"
            mc "That complaint. We played truth or dare and one of the dares was to call you and complain about the food."
            scene 08_1721 with Dissolve(1)
            m "Are you serious?"
            mc "Yeah, I'm sorry. Layla, the girl who had to call, felt really bad, too."
            m "Layla? I called her Kayla the whole time."
            mc "{i}(She even remembers the name.){/i}"
            m "What a relief. Now I don't have to fire our chef."
            mc "What? You were going to..."
            scene 08_1722 with Dissolve(1)
            m "Kidding. Haha."
            mc "Mom!"
            m "You're not the only one who has jokes."
            mc "*Shakes head*"
            m "Next time you see Layla, tell her it's fine. She was really sweet."
            if Zach_Week3_Wednesday_TC_Girlshower == False:
                mc "Hell no. I'll tell her you fired the chef."
                m "..."
            else:
                mc "{i}(She probably doesn't want to talk to me.){/i}"
        "No":
            mc "{i}(It wasn't that bad. I'll leave it be.){/i}"
    if Emily_Points >= 11:
        $ Emily_Week3_Sunday_Surprise = True
        scene 08_1723 with Dissolve(1)
        m "Are you free Wednesday after school?"
        mc "Hmm, I think so."
        m "Good. I took the afternoon off. We need to go somewhere."
        mc "And where is somewhere?"
        m "It's a surprise."
    else:
        pass
    if Erynn_End == True:
        jump Week4_Monday
    else:
        if Erynn_Week3_Monday_Blackmailhelp == False:
            if Alexis_Dating == True:
                jump Week3_Sunday_Alexis
            else:
                jump Week4_Monday
        else:
            jump Week3_Sunday_Erynn

label Week3_Sunday_Erynn:
    scene black with Dissolve(2)
    pause 2
    scene 08_1724 with Dissolve(1)
    mc "And contract completed."
    mc "Oh yeah, pay up!"
    mc "*Sings* Toss a coin to your..."
    scene 08_1725 with Dissolve(1)
    er "Who are you tossing a coin to?"
    mc "Oh... Hey, Erynn."
    scene 08_1726 with Dissolve(1)
    er "Hey. How are you?"
    mc "I'm good. How have you been?"
    er "Good also. Staying with Mom was a great idea."
    mc "Glad to hear that."
    scene 08_1727 with Dissolve(1)
    er "How was training camp? And the competition?"
    mc "It was fun and exhausting. But we had a really good time."
    if MC_Week3_Saturday_TC_Win == True:
        mc "I got first place!"
        scene 08_1728 with Dissolve(1)
        er "No? Really? Congratulations."
        mc "Thank you."
        er "I wish I could've seen it. Next competition I'll be there, okay?"
        mc "I'll hold you to that."
    else:
        mc "Only fourth place though."
        er "That's really good for your first race. Once you get more experience and practice, it will be an easy first!"
        mc "Hehe, maybe."
    scene 08_1729 with Dissolve(1)
    er "What are you doing?"
    mc "Uhm, just playing a video game."
    scene 08_1730 with Dissolve(1)
    er "You're that old guy?"
    mc "Heh... Yeah."
    scene 08_1731 with Dissolve(1)
    er "What are you doing later?"
    if Alexis_Dating == True:
        if Erynn_Week3_Monday_Alexis_Mention == True:
            $ Alexis_Week3_Sunday_BubbleIce = True
            mc "I was planning to go see..."
            er "Alexis?"
            mc "Yes."
            scene 08_1732 with Dissolve(1)
            er "Okay..."
            mc "You guys still haven't talked?"
            er "..."
            mc "Erynn. This has gone for long enough, already."
            scene 08_1733 with Dissolve(1)
            er "I don't know what to say."
            mc "Ask her how her day was. Talk about the weather. Clothes... Anything really."
            mc "Ask her if she likes... Uhm... Bubblegum ice cream."
            er "She doesn't."
            mc "No?"
            er "No."
            scene 08_1734 with Dissolve(1)
            mc "What about Ethan? Did you talk to him?"
            er "No. I haven't heard nor seen him since."
        else:
            $ Alexis_Week3_Sunday_BubbleIce = True
            $ Erynn_Points -= 4
            mc "{i}(Shit! I still haven't told her that I'm seeing Alexis... I guess I'll do it now.){/i}"
            mc "I was planning to go see Alexis."
            if Erynn_Week3_Monday_Makeout == True:
                $ Erynn_Points -= 4
                er "Alexis? You're still seeing each other? Then why did you..."
                mc "What?"
                er "Never mind..."
            else:
                er "Alexis? You're still seeing each other?"
                mc "Yes."
            er "Why didn't you tell me?"
            mc "I just didn't find the right moment to tell you, because of all that has been going on lately."
            scene 08_1732 with Dissolve(1)
            er "..."
            mc "You guys still haven't talked?"
            er "..."
            mc "Erynn. This has gone for long enough, already."
            scene 08_1733 with Dissolve(1)
            er "I don't know what to say."
            mc "Ask her how her day was. Talk about the weather. Clothes... Anything really."
            mc "Ask her if she likes... Uhm... Bubblegum ice cream."
            er "She doesn't."
            mc "No?"
            er "No."
            scene 08_1734 with Dissolve(1)
            mc "What about Ethan? Did you talk to him?"
            er "No. I haven't heard nor seen him since."
    else:
        mc "I have nothing planned for today."
        scene 08_1732 with Dissolve(1)
        mc "By the way, has Ethan shown up yet?"
        scene 08_1734 with Dissolve(1)
        er "No. I haven't heard nor seen him since."
    mc "Nothing?"
    er "I'm a little worried that..."
    scene 08_1735 with Dissolve(1)
    mc "You're still staying at Melissa's though, right?"
    er "I am, but I was planning to go back to the apartment tomorrow."
    mc "You think it's a good idea?"
    er "All my stuff is there and I have a photo shoot coming up next Friday."
    scene 08_1736 with Dissolve(1)
    mc "You're going to do that?"
    er "I'm under contract."
    er "Besides, there will be multiple girls from our agency. We all go together. It will be fine."
    mc "Okay."
    scene 08_1737 with Dissolve(1)
    m "[mc]. Do you have laundry that needs to be washed?"
    m "I'm about to fill up the washing machine."
    mc "Oh yeah. It's still in my bag. Let me..."
    m "It's alright, I'll get it."
    scene 08_1738 with Dissolve(1)
    m "This one here."
    mc "Yes, thank you."
    if Zach_Week3_Wednesday_TC_Girlshower == True:
        scene 08_1739 with Dissolve(1)
        er "Your mom has a nice ass."
        mc "What? Where did that come from?"
        er "Just saying."
        er "And you were looking too!"
        mc "..."
        mc "She was asking about the bag, I was looking... Whatever. Stop being weird!"
        er "Haha."
    else:
        if Zach_Week3_Saturday_TC_Swap == True:
            scene 08_1739 with Dissolve(1)
            er "Your mom has a nice ass."
            mc "What? Where did that come from?"
            er "Just saying."
            er "And you were looking too!"
            mc "..."
            mc "She was asking about the bag, I was looking... Whatever. Stop being weird!"
            er "Haha."
        else:
            if Valeria_Week3_Saturday_TC_Swap == True:
                scene 08_1747a with Dissolve(1)
                m "I didn't know you wear this kind of underwear."
                mc "AAAH!"
                mc "{i}(Shit! I forgot to give them back...){/i}"
            else:
                scene 08_1747 with Dissolve(1)
                m "I didn't know you wear this kind of underwear."
                mc "AAAH!"
                mc "{i}(Shit! I forgot to give them back...){/i}"
            scene 08_1748 with Dissolve(1)
            mc "Uh... Those aren't mine!"
            m "No? Then why are they in your bag?"
            scene 08_1749 with Dissolve(1)
            mc "*Sigh* It was a dare. We played truth or dare at camp."
            m "You had to steal a pair of panties?"
            mc "Hmm, yeah... Something like that... I don't want to talk about it now."
            scene 08_1750 with Dissolve(1)
            m "What do you want me to do with them? Do you want to keep them?"
            mc "No! I don't want to keep them!"
            m "Throw them away then?"
            mc "No! Can you wash them together with the other clothes? I'll give them back tomorrow."
            m "Sure."
            mc "Thanks."
            scene 08_1751 with Dissolve(1)
            er "Haha."
            mc "What are you laughing about?"
            er "If you wanted a pair of panties, you just had to ask me."
            mc "Ha-ha-ha."
            scene 08_1752 with Dissolve(1)
            er "So... What's the real story behind the dare?"
            mc "I told you already."
            er "Stealing? Uh-huh..."
            scene 08_1753 with Dissolve(1)
            er "Tell me! Please?"
            mc "No..."
            er "Please? I'll show you my panties!"
            mc "No! Your puppy dog eyes won't work, either."
            scene 08_1739 with Dissolve(1)
            er "Haha, fine. By the way, your mom has a nice ass."
            mc "What? Where did that come from?"
            er "Just saying."
            er "And you were looking too!"
            mc "..."
            mc "She was asking about the bag, I was looking... Whatever. Stop being weird!"
            er "Haha."
    scene 08_1740 with Dissolve(1)
    er "What about me? Do I have a nice ass?"
    mc "..."
    menu:
        "Yes[KoGa3AutoWTChange1]{size=-4}(Erynn Points+2) {/size} {/color}":
            $ Erynn_Points += 2
            # Erynn (38)
            if Erynn_Friends == False:
                scene 08_1741 with Dissolve(1)
                mc "Yes, a very nice one."
                er "Haha, thanks."
                scene 08_1742 with vpunch
                n "*Slap*"
                er "Aaah! Hey!"
                mc "You totally asked for that."
                er "I did not!"
            else:
                scene 08_1741 with Dissolve(1)
                mc "Yes, a very nice one."
                er "Haha, thanks."
        "No":
            scene 08_1743 with Dissolve(1)
            mc "No, not really. A little too skinny for my taste."
            er "Skinny? It isn't skinny at all..."
        "Joke[KoGa3AutoWTChange1]{size=-4}(Erynn Points+2) {/size} {/color}":
            $ Erynn_Points += 2
            # Erynn (38)
            scene 08_1744 with Dissolve(1)
            mc "I like my mom's better!"
            er "Very funny. But I can't argue with that."
    scene 08_1745 with Dissolve(1)
    mc "You know who else has a nice ass?"
    er "Who?"
    mc "Melissa!"
    scene 08_1746 with Dissolve(1)
    er "..."
    mc "What now? Why are you looking like that?"
    mc "You started talking about my mom's ass all of a sudden. Now I'm the weird one?"
    if Alexis_Dating == True:
        mc "Anyway, I have to go now."
        scene 08_1753 with Dissolve(1)
        er "Really? Can't you stay? I want to hear everything about training camp."
        er "Pretty please? With cherries on top?"
        menu:
            "Meet Alexis":
                mc "Next time, okay?"
                scene 08_1754 with Dissolve(1)
                mc "Want to come with me? You guys can talk, then."
                er "No..."
                mc "I'll give you one more week!"
                er "..."
                scene 08_1755 with Dissolve(1)
                er "We'll see each other next week then?"
                mc "For sure."
                er "Alright. Have fun on your date."
                mc "Thanks!"
                if Erynn_Friends == False:
                    scene 08_1756 with Dissolve(1)
                    er "Actually, I take that back. Don't have fun."
                    mc "Heh, Erynn..."
                    scene 08_1757 with Dissolve(1)
                    er "Bye."
                    mc "See you later."
                else:
                    scene 08_1757 with Dissolve(1)
                    er "Bye."
                    mc "See you later."
                jump Week3_Sunday_Alexis
            "Stay with Erynn[KoGa3AutoWTChange1]{size=-4}(Alexis JealousyPoints+2) {/size} {/color}":
                $ Alexis_JealousyPoints += 2
                # Alexis_Jealous (2)
                jump Week3_Sunday_Erynn_Stay
    else:
        jump Week3_Sunday_Erynn_Stay

label Week3_Sunday_Erynn_Stay:
    $ Erynn_Points += 2
    # Erynn (40)
    if Layla_Dating == False:
        if Erynn_Points >= 31:
            $ Erynn_LikeMC = True
        else:
            $ Erynn_Friends = True
    else:
        $ Erynn_Friends = True
    if Alexis_Dating == True:
        scene 08_1758 with Dissolve(1)
        mc "Fine, I'll stay. I'll go see her a little later."
        er "Hehe."
        scene 08_1759 with Dissolve(1)
        mc "But there's a price to pay!"
        er "What?"
    else:
        scene 08_1758 with Dissolve(1)
        er "You've always been the weird one."
        er "Kidding!"
        scene 08_1759 with Dissolve(1)
        mc "Big mistake, Erynn!"
        er "What?"
    scene 08_1760 with vpunch
    er "Aaah!"
    er "Haha. What are you doing?"
    mc "All those years of torture..."
    er "What are you talking about?"
    mc "You'll see. Well, rather feel..."
    scene 08_1761 with Dissolve(1)
    er "Haha. [mc]!"
    er "No... Haha."
    er "Stop, I can't."
    er "[mc]!"
    scene 08_1762 with Dissolve(1)
    mc "Where do you think you're going? We're not done yet."
    er "Haha. This, this..."
    mc "Not so fun when the roles are reversed, huh?"
    er "[mc]! Haha."
    er "I get it. Please, haha."
    scene black with Dissolve(1)
    pause 2
    scene 08_1763 with Dissolve(1)
    er "*Heavy breathing*"
    mc "I didn't know you were this ticklish."
    er "Haha. Neither did I."
    scene 08_1764 with Dissolve(1)
    mc "This feels like back then, right?"
    er "..."
    scene 08_1765 with vpunch
    er "Ha! You let your guard down. Did you think I wouldn't retaliate?"
    mc "No... I was waiting for it."
    if Erynn_LikeMC == True:
        mc "{i}(It's funny she still thinks she can pin me down like this.){/i}"
        mc "{i}(But I'm rather enjoying it.){/i}"
    else:
        mc "{i}(It's funny she still thinks she can pin me down like this.){/i}"
    er "Let's see how ticklish you are!"
    scene 08_1766 with Dissolve(1)
    er "Take this!"
    mc "..."
    er "Why aren't you laughing and squirming around?"
    scene 08_1767 with Dissolve(1)
    er "Doesn't that tickle you?"
    mc "You tickled me so much when we were younger."
    mc "It's lost its effect."
    scene 08_1768 with Dissolve(1)
    if Erynn_LikeMC == True:
        er "Nothing at all?"
        mc "{i}(If you knew what other effect you're having on me right now, you wouldn't be on top of me.){/i}"
        mc "{i}(I'm so hard right now. She's basically riding me.){/i}"
        if Alexis_Dating == False:
            mc "{i}(Good thing she hasn't realised yet. That'd be very awkward.){/i}"
            scene 08_1769 with Dissolve(1)
            er "How about this?"
            mc "..."
            scene 08_1770 with Dissolve(1)
            mc "Uhm..."
            er "Sorry. I shouldn't have done that."
            mc "It's alright."
        else:
            mc "{i}(Good thing she hasn't realised yet. That'd be very awkward.){/i}"
    else:
        er "Nothing at all?"
        er "Sorry..."
    scene black with Dissolve(1)
    pause 2
    scene 08_1771 with Dissolve(1)
    er "Hey, can I maybe try the game you played earlier?"
    mc "You play video games?"
    er "Yeah, why not?"
    mc "Go ahead."
    er "Can you show me? I have no idea how to even start."
    scene 08_1772 with Dissolve(1)
    mc "I'll just show you the basics real quick."
    er "Okay."
    mc "You use these keys to move, E is to interact with characters, doors and so on."
    mc "And the mouse here to look around and fight if you click the left button. Very simple, really."
    er "Hmm..."
    scene 08_1773 with Dissolve(1)
    mc "I'll go to an easy area and then you can give it a try."
    er "Alright."
    scene 08_1774 with Dissolve(1)
    mc "You can take the seat and..."
    er "No-no, just stay there. I'll probably need your help."
    mc "Are you just going to stand there? It's much easier if..."
    scene 08_1775 with Dissolve(1)
    mc "{i}(That answers my question.){/i}"
    er "I'm really curious about this. I've never played a computer game before."
    mc "Not even solitaire?"
    er "Never heard of it. Is it similar to this one?"
    if Erynn_LikeMC == True:
        mc "Eh... This one also has a card game, I guess..."
        scene 08_1776 with Dissolve(1)
        er "Hmm..."
        mc "{i}(I'm getting hard again.){/i}"
        scene 08_1778 with Dissolve(1)
        mc "{i}(Why does she always smell so good?){/i}"
        mc "{i}(I don't know if it's nostalgia or something else, but...){/i}"
        scene 08_1779 with Dissolve(1)
        er "Hey! What are you doing?"
        er "No sleeping back there, I need your help."
        mc "Sorry. Just a bit tired."
        er "Do you want me to leave so you can sleep?"
        mc "It's fine."
    else:
        mc "Eh... This one also has a card game, I guess..."
    if Alexis_Dating == True:
        scene 08_1777 with Dissolve(1)
        er "Oh... Didn't you have to go? Plans with Alexis?"
        mc "I decided to stay here. I'll call her later to say something came up."
        mc "I'll go see her tomorrow."
    else:
        pass
    scene black with Dissolve(1)
    pause 2
    scene 08_1780 with Dissolve(1)
    mc "Now follow the trail."
    er "This one here?"
    mc "Yes. It will bring you straight to them."
    scene 08_1781 with Dissolve(1)
    er "Aaah!"
    mc "What are you doing? Stop running away..."
    er "They're shooting me."
    mc "No shit. They're not just going to let you kill them."
    mc "RINNY!"
    scene 08_1782 with Dissolve(1)
    mc "..."
    er "What's this screen? What do I have to do now?"
    mc "Just read it. You're dead. Game over."
    er "How?"
    scene 08_1783 with Dissolve(1)
    mc "Seriously? You didn't see all those arrows flying towards you?"
    er "They hit me like once! In the knee."
    mc "Haha."
    er "Why are you laughing?"
    mc "You wouldn't understand."
    scene 08_1784 with Dissolve(1)
    er "This was my first time playing. I wasn't that bad!"
    mc "As long as you aren't thinking about going pro, no, not that bad."
    er "Besides, this game is way too difficult."
    mc "Want to try a different one?"
    scene 08_1785 with Dissolve(1)
    er "No, you can play. I'll watch."
    mc "You sure? It will probably bore you though."
    er "Then it's up to you to make it interesting."
    mc "Hehe, alright. I'll get you a chair."
    if Erynn_LikeMC == True:
        scene 08_1786 with Dissolve(1)
        er "No need, I'm quite comfy here."
        mc "{i}(You are, maybe. I've had a hard-on for some time now...){/i}"
    else:
        er "No need, I'm quite comfy here."
    scene black with Dissolve(1)
    pause 2
    scene 08_1787 with Dissolve(1)
    er "You make it look so easy."
    mc "This isn't my first time playing. Also, I'm a little over-levelled for this area."
    er "I don't know what that means."
    mc "Haha."
    er "You rarely played computer games when you were younger, right?"
    if Erynn_LikeMC == True:
        scene 08_1788 with Dissolve(1)
        mc "Because I had other people to play with."
        mc "Especially that cute neighbour girl."
    else:
        scene 08_1788a with Dissolve(1)
        mc "Because I had other people to play with."
        mc "Especially that annoying neighbour girl."
        er "HEY!"
        mc "Haha."
    scene black with Dissolve(1)
    pause 2
    scene 08_1789 with Dissolve(1)
    er "Is that... What kind of club is this?"
    mc "I think you know exactly what club this is."
    er "A brothel?"
    mc "Uh-huh."
    er "They have those in games?"
    mc "In some, yes."
    er "Hmm..."
    scene 08_1790 with Dissolve(1)
    er "Can you also..."
    mc "Hire one of the girls?"
    er "Yes."
    mc "You can."
    er "Really?"
    if Alexis_Dating == True:
        scene 08_1791 with Dissolve(1)
        mc "Want to see?"
        er "No!"
        mc "Haha, okay."
        scene 08_1812 with Dissolve(1)
        m "ERYNN?"
        er "Yes?"
        m "Are you staying for dinner?"
        er "I'd love to."
        scene 08_1813 with Dissolve(1)
        er "I think I'll help your mom with dinner."
        mc "I told you this will bore you."
        er "It's not that. We can continue next time."
        mc "Alright."
        jump Week4_Monday
    else:
        if Erynn_LikeMC == True:
            jump Week3_Sunday_Erynn_Game
        else:
            scene 08_1791 with Dissolve(1)
            mc "Want to see?"
            er "No!"
            mc "Haha, okay."
            scene 08_1812 with Dissolve(1)
            m "ERYNN?"
            er "YES, EMILY?"
            m "Are you staying for dinner?"
            er "I'd love to."
            scene 08_1813 with Dissolve(1)
            er "I think I'll help your mom with dinner."
            mc "I told you this will bore you."
            er "It's not that. We can continue next time."
            mc "Alright."
            jump Week4_Monday

label Week3_Sunday_Erynn_Game:
    if _in_replay:
        $ Team_Yennefer = True
    scene 08_1792 with Dissolve(1)
    er "Can we try?"
    mc "You really want to see?"
    er "Mmm... Yeah."
    if Team_Yennefer == True:
        mc "You'll make me cheat on Yennefer though."
    else:
        mc "You'll make me cheat on Triss though."
    er "Who is she?"
    mc "Sort of the character's love interest."
    scene 08_1793 with Dissolve(1)
    er "Oh, okay. Then don't, I guess."
    mc "No, it's fine. I'll save and reload after."
    mc "{i}(If only real life had this function.){/i}"
    mc "Let's talk to all the girls first, then you can pick your favourite."
    scene black with Dissolve(1)
    pause 2
    scene 08_1794 with Dissolve(1)
    er "Let's take her."
    mc "Haha. I knew you were going to pick her."
    er "Why's that?"
    mc "Blonde... Also, she's an elf, by the way."
    er "Does that change anything?"
    menu:
        "Joke":
            scene 08_1791a with Dissolve(1)
            mc "Well yeah. She has a penis!"
            er "What?"
            mc "Haha, no. I'm kidding. The only thing that is pointy are her ears."
            er "..."
            scene 08_1791 with Dissolve(1)
            er "Let's pick someone else."
            mc "Haha."
        "Answer":
            mc "No, just pointy ears."
    scene 08_1795 with Dissolve(1)
    er "They're naked... And you can see..."
    er "Is this even allowed in games?"
    mc "It's PEGI 18."
    scene 08_1796 with Dissolve(1)
    mc "{i}(I expected it to be awkward watching this with her, but it seems she's rather enjoying it...){/i}"
    mc "{i}(But this situation surely doesn't help my other situation.){/i}"
    scene 08_1797 with Dissolve(1)
    mc "{i}(Hmm...){/i}"
    mc "{i}(I didn't even realise I was caressing her leg.){/i}"
    scene 08_1798 with Dissolve(1)
    mc "{i}(Will it be okay if I kiss her?){/i}"
    mc "{i}(She kissed me before, so...){/i}"
    mc "{i}(Stop thinking and just do it!){/i}"
    scene 08_1799 with Dissolve(1)
    ""
    scene 08_1800 with Dissolve(1)
    mc "{i}(Do you have any idea how much I want you right now?){/i}"
    scene 08_1801 with Dissolve(1)
    mc "{i}(She's taking her top off...){/i}"
    mc "{i}(I'm not dreaming this time, right?){/i}"
    scene 08_1802 with Dissolve(1)
    mc "..."
    scene 08_1803 with Dissolve(1)
    er "Kiss me again!"
    scene 08_1804 with Dissolve(1)
    mc "Erynn..."
    scene 08_1805 with Dissolve(1)
    er "Mmm."
    scene 08_1806 with Dissolve(1)
    mc "{i}(Let's take these off.){/i}"
    scene 08_1807 with vpunch
    m "ERYNN?"
    er "That scared me..."
    scene 08_1808 with Dissolve(1)
    er "YES, EMILY?"
    m "Are you staying for dinner?"
    er "I'd love to."
    scene 08_1809 with Dissolve(1)
    er "*Sigh*"
    mc "Back to reality?"
    er "Yeah."
    er "I think I'll help your mom with dinner."
    mc "Okay."
    scene black with Dissolve(1)
    pause 2
    scene 08_1810 with Dissolve(1)
    er "[mc]?"
    mc "Hmm?"
    er "It's not that I don't want to."
    mc "I know."
    scene 08_1811 with Dissolve(1)
    mc "*Sigh*"
    $ renpy.end_replay()
    jump Week4_Monday

label Week3_Sunday_Alexis:
    $ Alexis_Week3_Sunday_Meet = True
    $ Alexis_Week3_Sunday_NewBartender = True
    scene black with Dissolve(1)
    pause 2
    stop music fadeout 1.0
    play music "Sounds/Bar_Background.mp3" volume 0.3
    scene 08_1814 with Dissolve(1)
    mc "{i}(That must be the new guy.){/i}"
    mc "{i}(Hmm... I don't see Alexis. Is she not working today?){/i}"
    mc "{i}(Maybe I should've called her, but that wouldn't be much of a surprise.){/i}"
    scene 08_1815 with Dissolve(1)
    bt "Hey."
    mc "Hi."
    bt "What can I get you?"
    mc "Is Alexis working today?"
    bt "Yes, she's in the back doing inventory."
    scene 08_1816 with Dissolve(1)
    bt "Anything I can help you with?"
    mc "Can you tell her [mc] is here?"
    bt "Uh... Sure. Anything to drink?"
    mc "I'm good, thanks."
    scene black with Dissolve(1)
    pause 2
    scene 08_1817 with Dissolve(1)
    bt "Alexis?"
    a "Yes?"
    bt "Some guy is asking for you."
    scene 08_1818 with Dissolve(1)
    a "Some guy?"
    bt "Yeah, felt kinda weird. Do you want me to get rid of him?"
    a "No. Just tell him I'm busy."
    a "I want to finish this before my shift ends anyway."
    bt "Will do."
    a "Thanks."
    scene black with Dissolve(1)
    pause 2
    scene 08_1819 with Dissolve(1)
    bt "I'm sorry but she's busy at the moment."
    mc "Hmm... Okay."
    mc "{i}(Not even time for a hello?){/i}"
    mc "{i}(Guess I'll wait a while.){/i}"
    mc "Can I get an iced tea, please?"
    bt "Of course."
    scene black with Dissolve(1)
    pause 2
    n "An hour later."
    scene 08_1820 with Dissolve(1)
    a "*Sigh* Finally finished..."
    bt "Good job!"
    a "I hate doing inventory."
    bt "No one likes to do inventory."
    a "Yeah. That's why Dylan lets me do it."
    bt "Hehe. Have you seen the whiskey bottles by any chance?"
    scene 08_1821 with Dissolve(1)
    a "Yeah, they're right here. I'll get them for you."
    bt "Thanks."
    bt "That guy from before is still here, by the way."
    a "Okay. This is getting weird. You know who he is?"
    bt "He told me his name. What was it again? [mc]?"
    scene 08_1822 with Dissolve(1)
    a "[mc]?"
    bt "Think so. Or something like that?"
    a "Oh my god..."
    scene black with Dissolve(1)
    pause 2
    scene 08_1823 with Dissolve(1)
    a "I'm so sorry, [mc]."
    mc "Hey, there you are. Busy?"
    a "I didn't know it was you, or else I would've come earlier. Sorry."
    mc "It's fine. I could've called before, but wanted to surprise you."
    scene 08_1824 with Dissolve(1)
    bt "Oh, he's your boyfriend?"
    a "Uhm..."
    bt "I'm so sorry, I didn't know, or else I..."
    mc "It's all good, man."
    bt "Drinks are on me to make up for it, alright?"
    scene 08_1825 with Dissolve(1)
    a "You don't have to pay for him. He never pays here anyway."
    mc "I offered. It's not my fault others pay for me."
    scene 08_1826 with Dissolve(1)
    mc "You know what? When we go to a restaurant next time. It's on me, okay?"
    a "We'll probably go to Rue Madison and most likely you won't have to pay there either."
    mc "Haha, you got me. I feel like such a cheapskate... Free drinks, free food."
    scene 08_1827 with Dissolve(1)
    a "Cheapskate or not, I still like you!"
    mc "Thanks?"
    scene 08_1828 with Dissolve(1)
    a "Hmm?"
    mc "What?"
    a "You shaved!"
    mc "Yeah. Like it?"
    scene 08_1829 with Dissolve(1)
    a "No!"
    mc "Haha, ouch."
    a "I liked the stubble look better."
    mc "Give it a couple of days and it will be back."
    scene 08_1830 with Dissolve(1)
    a "Alright, see you in a couple of days then."
    mc "Hey!"
    scene 08_1831 with Dissolve(1)
    mc "Where do you think you're going?"
    a "Haha."
    scene 08_1833 with Dissolve(1)
    if Layla_Week3_Tuesday_Train == False:
        a "No biting, okay?"
        mc "Look who's talking."
        a "At least not in public!"
    else:
        a "That tickles!"
    scene 08_1832 with Dissolve(1)
    a "Missed you!"
    mc "Missed you too."
    a "And thank you for calling me every day."
    mc "All but one."
    a "Right. The 'Oh shit Alexis' day."
    mc "Haha, sorry!"
    a "You're forgiven."
    if Erynn_Week3_Monday_Blackmailhelp == False:
        scene 08_1834 with Dissolve(1)
        mc "When does your shift end?"
        a "Just now."
        mc "Perfect. Let's head out then."
    else:
        scene 08_1843 with Dissolve(1)
        a "Were you with Erynn earlier?"
        mc "Yeah. She came by to ask about training camp. How do you even know that?"
        a "I smell her perfume on you."
        mc "I've told you before, but I'll say it again. You have a really good nose."
        a "Hehe."
        scene 08_1834 with Dissolve(1)
        mc "When does your shift end?"
        a "Just now."
        mc "Perfect. Let's head out then."
    scene black with Dissolve(1)
    pause 2
    stop music fadeout 1.0
    play music ("Music/LoFi Upbeat 1.mp3", "Music/LoFi Upbeat 2.mp3", "Music/LoFi Upbeat 3.mp3", "Music/LoFi Upbeat 4.mp3") volume 0.2
    if Zach_Week3_Wednesday_TC_Girlshower == True:
        $ Alexis_Points -= 4
        scene 08_1835 with Dissolve(1)
        mc "What do you want to do today?"
        a "How about we play truth or dare."
        mc "..."
        mc "{i}(Fuck! She knows. Of course she knows, they're sisters.){/i}"
        if Layla_Week3_Wednesday_TC_Alexis_DateBoth == False:
            mc "Layla told you?"
            a "She said to talk to you about it."
        else:
            mc "{i}(But seems that's the only thing Layla told her. If she told Alexis we hooked up at training camp, I wouldn't be talking to her right now.){/i}"
            mc "Layla told you about that?"
            a "She did..."
        scene 08_1836 with Dissolve(1)
        mc "*Sigh*"
        mc "Zach asked me to help him with something. Before I knew it, we were in the girls' changing room."
        mc "He wanted to peek a bit at girls from the other schools and have me stand on lookout."
        mc "He didn't see anything and asked me if I wanted a quick peek."
        scene 08_1837 with Dissolve(1)
        mc "I should've said no and just left."
        a "You should've left the moment you knew where you were and not helped him with such despicable behaviour."
        mc "You're right. I'm sorry."
        a "What happened next?"
        scene 08_1838 with Dissolve(1)
        mc "The moment I looked, Elena came out of the showers."
        a "Elena? Layla's friend?"
        mc "Yeah. I told Zach we should leave before he could see her."
        a "Look at you. Such a hero."
        mc "Okay. You don't have to put salt in the wound now."
        a "Your wound? I think Elena is the victim here!"
        scene 08_1839 with Dissolve(1)
        mc "I know that. But if Zach didn't blurt it out during the game, she would've never known..."
        a "So now it's all Zach's fault?"
        mc "No. I'm as much to blame as him."
        a "At least you're right about that. But it doesn't make it any better. What you did is wrong!"
        mc "I know! Don't you ever make mistakes?"
        a "..."
        a "You of all people should know I make mistakes..."
        scene 08_1840 with Dissolve(1)
        a "I think I'm going home for today."
        mc "Lexi?"
        a "..."
        mc "I'm really sorry!"
        a "Fix it! I can't have my sister not liking you."
        scene 08_1841 with Dissolve(1)
        a "I'll call you. Bye."
        mc "Bye..."
        scene 08_1842 with Dissolve(1)
        mc "{i}(Fuck! What am I doing?){/i}"
        mc "{i}(I should stop behaving like a little kid! Grow up already. Fucking idiot!){/i}"
        jump Week4_Monday
    else:
        $ Alexis_Girlfriend = True
        scene 08_1844 with Dissolve(1)
        mc "What do you want to do today?"
        a "Hmm... How about we play truth or dare?"
        mc "Heh, okay. What has Layla told you?"
        scene 08_1845 with Dissolve(1)
        a "Nothing..."
        a "Only that you guys had lots of fun."
        a "And that you like wearing other people's underwear."
        scene 08_1846 with Dissolve(1)
        mc "I knew it! That little..."
        a "Haha."
        mc "I bet the whole school knows already."
        mc "Now I'll have to switch schools again. Third time this year."
        scene 08_1847 with Dissolve(1)
        a "You can come to my school."
        mc "I probably will next year."
        a "Yeah? I'd love that. Maybe we'll have some classes together, then."
        scene 08_1848 with Dissolve(1)
        mc "Who knows. But I hope not."
        a "Why not?"
        mc "Because I won't be able to concentrate..."
        scene 08_1849 with Dissolve(1)
        a "Don't worry. I'll tutor you after class."
        mc "What class would that be?"
        a "Advanced Chemistry."
        mc "Haha, I see what you did there. Nice."
        mc "How about some biology?"
        a "That will be today's lesson."
        mc "Oh..."
        scene 08_1850 with Dissolve(1)
        mc "By the way. Truth or dare?"
        a "What?"
        mc "You said you wanted to play. So pick!"
        a "Dare."
        mc "Right off the bat?"
        a "Uh-huh."
        mc "No wonder I like you. So brave."
        scene 08_1851 with Dissolve(1)
        a "Haha."
        mc "..."
        mc "Did she tell you that too? Come on."
        a "You go by many names. New guy, brave Sir [mc], underwear boy..."
        scene 08_1852 with Dissolve(1)
        mc "Underwear boy?"
        mc "You just made that up."
        a "Haha."
        mc "{i}(I'll get you back for that.){/i}"
        scene 08_1853 with Dissolve(1)
        mc "So dare, huh?"
        mc "Here's a nice one to start with..."
        if Alexis_Week3_Sunday_BubbleIce == False:
            scene 08_1854 with Dissolve(1)
            mc "I dare you to sing your favourite song. Right here, right now."
            a "What? Here? No!"
            a "No-no-no..."
            scene 08_1855 with Dissolve(1)
            a "Please pick another dare, [mc]!"
            a "I can't do that one."
            a "Please?"
            scene 08_1857 with Dissolve(1)
            mc "Why not? You're a really good singer, Lexi."
            a "No... Just give me another dare. This one doesn't count."
            mc "Alright."
        else:
            scene 08_1854 with Dissolve(1)
            mc "I dare you to eat bubblegum ice cream!"
            a "What? No!"
            a "No-no-no..."
            scene 08_1855 with Dissolve(1)
            a "Please pick another dare, [mc]!"
            a "I can't do that one."
            a "Please?"
            scene 08_1856 with Dissolve(1)
            mc "Haha. What's your deal with bubblegum ice cream?"
            a "Have you tasted it?"
            mc "No."
            a "Well, it does NOT work in ice cream. What are you supposed to do with the pieces of bubble gum? Chew them while your ice cream melts?"
            a "Swallow them or spit them out? It's all wrong. Just no!"
            scene 08_1857 with Dissolve(1)
            mc "Fine, you'll get your punishment later."
            a "No... Just give me another dare. This one doesn't count."
            mc "Alright."
        scene 08_1858 with Dissolve(1)
        mc "You're going to hate this one even more!"
        mc "I dare you to be my girlfriend!"
        a "..."
        mc "What? Not doing this one either?"
        scene 08_1859 with Dissolve(1)
        mc "It's no fun playing with you."
        a "..."
        scene 08_1860 with Dissolve(1)
        a "Wait! [mc]!"
        a "I'll do the dare."
        scene 08_1861 with Dissolve(1)
        a "I will do the dare!"
        mc "Good."
        scene 08_1862 with vpunch
        mc "Hey! Careful."
        a "My turn. I dare you to ask me again!"
        mc "Who says I'll pick dare? Maybe I'll go for truth?"
        a "Please pick dare."
        mc "Hehe."
        scene 08_1863 with Dissolve(1)
        a "Ask me again!"
        mc "Alexis Monroe. Do you want to be my girlfriend?"
        a "Yes! I want to be your girlfriend!"
        scene 08_1864 with Dissolve(1)
        ""
        scene 08_1865 with Dissolve(1)
        x "Get a room!"
        x "Not everyone wants to see your PDA!"
        scene 08_1866 with Dissolve(1)
        mc "What's her problem?"
        a "Maybe no one dared her to be someone's girlfriend?"
        mc "Haha. That must be it."
        scene 08_1867 with Dissolve(1)
        a "But she's right though."
        a "We should get a room. How about my place?"
        if Layla_Week3_Tuesday_Train == True:
            mc "Sure."
        else:
            scene 08_1868 with Dissolve(1)
            mc "Did you clean your room this time? Uhm, I mean, your roommate isn't there today?"
            a "I really have a roommate, okay? She was there last time. Naked! That's why I didn't let you in."
            scene 08_1869 with Dissolve(1)
            mc "I wouldn't have minded."
            a "..."
            mc "Kidding?"
            a "Uh-huh..."

label Week3_Sunday_Alexis_Dorm:
    if _in_replay:
        $ SexCounter_Alexis = 7
        $ MC_SexCounter = 7
        $ Alexis_Week3_Sunday_PizzaJoke = True
    $ SexCounter_Alexis += 1
    $ MC_SexCounter += 1
    $ Iris_Week3_Sunday_Meet = True
    scene black with Dissolve(1)
    pause 2
    scene 08_1870 with Dissolve(1)
    mc "..."
    a "Don't say a word!"
    mc "I wasn't..."
    scene 08_1871 with Dissolve(1)
    a "Why does she always do this?"
    a "It isn't that difficult to put everything in the basket."
    scene 08_1872 with Dissolve(1)
    a "Anyway, welcome to my not-so-clean room."
    mc "Hehe, thanks."
    a "You can have a look around if you'd like."
    a "I'm going to clean up this mess real quick."
    scene black with Dissolve(1)
    pause 2
    scene 08_1873 with Dissolve(1)
    mc "{i}(I've seen this before.){/i}"
    scene 08_1874 with Dissolve(1)
    mc "{i}(It's the same one Erynn has.){/i}"
    mc "{i}(I'll get you guys talking again. One way or another.){/i}"
    scene 08_1875 with Dissolve(1)
    a "Screw it. I'll just put everything on her bed."
    mc "That's what I would've done too."
    a "Hmm, what's this?"
    scene 08_1876 with Dissolve(1)
    a "Are you serious?"
    a "Can't even put that away?"
    scene 08_1877 with Dissolve(1)
    a "Ew, why am I even touching that?"
    mc "Touching what?"
    a "Nothing..."
    a "I'm going to wash my hands real quick."
    scene black with Dissolve(1)
    pause 2
    scene 08_1878 with Dissolve(1)
    a "What are you looking at?"
    mc "This picture here. Erynn has the same one on her nightstand."
    a "She does?"
    mc "Yeah, in her old room."
    a "At Melissa's? I haven't been there in a long time."
    scene 08_1879 with Dissolve(1)
    mc "You'll be friends again."
    a "You think?"
    mc "Yeah."
    mc "I'll make sure of it."
    scene 08_1880 with Dissolve(1)
    a "Thank you!"
    scene black with Dissolve(1)
    pause 2
    scene 08_1881 with Dissolve(1)
    a "I can read your mind. I know exactly what you're thinking right now."
    mc "I'll do you one better. I know that you're thinking the same thing!"
    a "What shall we do about that?"
    menu:
        "Kiss her":
            scene 08_1884 with Dissolve(1)
            ""
        "Joke[KoGa3AutoWTChange1]{size=-4}(Alexis Week3 Sunday PizzaJoke) {/size} {/color}":
            $ Alexis_Week3_Sunday_PizzaJoke = True
            scene 08_1882 with Dissolve(1)
            mc "Order a large pepperoni pizza, of course."
            a "What?"
            mc "Pepperoni pizza. Or do you want other toppings?"
            scene 08_1883 with Dissolve(1)
            a "Seriously?"
            mc "Haha, I'm joking. Come here."
            scene 08_1884 with Dissolve(1)
            ""
    scene 08_1885 with Dissolve(1)
    ""
    scene 08_1886 with Dissolve(1)
    mc "{i}(Hi! I missed you guys!){/i}"
    scene 08_1887 with Dissolve(1)
    ""
    scene 08_1888 with Dissolve(1)
    a "Mmm..."
    scene 08_1889 with vpunch
    a "Aaah, [mc]!"
    mc "Haha, don't worry. I've got you."
    scene 08_1890 with Dissolve(1)
    mc "I won't let you drop!"
    a "Haha, that tickles!"
    scene black with Dissolve(1)
    pause 2
    scene 08_1891 with Dissolve(1)
    a "My turn!"
    if Alexis_Week3_Sunday_PizzaJoke == True:
        scene 08_1892 with Dissolve(1)
        a "Who's underwear are you wearing right now?"
        mc "..."
        mc "What pizza did you want again?"
        a "Haha."
    else:
        scene 08_1892 with Dissolve(1)
        a "Let me spoil you a bit today, boyfriend!"
        mc "Hehe. I like that."
    scene 08_1893 with Dissolve(1)
    ""
    scene 08_1894 with Dissolve(1)
    mc "Oh... Fuck..."
    scene 08_1895 with Dissolve(1)
    mc "{i}(Damn, Lexi...){/i}"
    mc "{i}(Don't do that, or this night will be over very quick!){/i}"
    scene 08_1896 with Dissolve(1)
    mc "{i}(This is so good!){/i}"
    scene 08_1897 with Dissolve(1)
    ""
    scene black with Dissolve(1)
    pause 2
    scene 08_1898 with Dissolve(1)
    mc "I can stare at you undressing all day."
    a "But if it takes all day. There won't be much time for doing anything else."
    mc "I don't mind."
    a "Haha."
    scene 08_1899 with Dissolve(1)
    mc "Hold on a second."
    a "Hmm?"
    mc "Can you do a little striptease?"
    a "A striptease?"
    mc "Ya! See it as punishment for the first dare you didn't do."
    a "Sure... I can try. Don't expect too much though."
    show 08_1900
    ""
    scene 08_1901 with Dissolve(1)
    a "Haha. That was so bad. I'm sorry."
    a "I don't know how to do this. That was so embarrassing!"
    menu:
        "Agree":
            scene 08_1902 with Dissolve(1)
            mc "Yeah, it was pretty shit."
            a "I know... I'm sorry!"
            mc "A for effort though!"
        "Cute[KoGa3AutoWTChange1]{size=-4}(Alexis Week3 Sunday Dorm StripteaseCute) {/size} {/color}":
            $ Alexis_Week3_Sunday_Dorm_StripteaseCute = True
            scene 08_1903 with Dissolve(1)
            mc "I liked it. It was cute actually. A little sexy, too."
            a "Yeah? Thanks."
    scene 08_1904 with Dissolve(1)
    a "Next time it's your turn."
    mc "Fine with me. You're the one who has to watch it."
    a "You can start today by taking your t-shirt off."
    scene 08_1908 with Dissolve(1)
    ""
    scene 08_1905 with Dissolve(1)
    ""
    scene 08_1906 with Dissolve(1)
    a "Aah..."
    scene 08_1907 with Dissolve(1)
    mc "{i}(I love the face she makes when she moans.){/i}"
    scene 08_1909 with Dissolve(1)
    mc "{i}(And I love having sex with her!){/i}"
    show 08_1910
    ""
    scene 08_1911 with Dissolve(1)
    ""
    scene black with Dissolve(1)
    pause 2
    scene 08_1912 with Dissolve(1)
    mc "{i}(Reverse cowgirl. We haven't done this before.){/i}"
    scene 08_1913 with Dissolve(1)
    ""
    scene 08_1914 with Dissolve(1)
    mc "{i}(Watching her ride me is so hot...){/i}"
    show 08_1915
    ""
    scene black with Dissolve(1)
    pause 2
    scene 08_1916 with Dissolve(1)
    x "That's so hot!"
    scene 08_1917 with Dissolve(1)
    mc "Sorry, what did you say?"
    a "I didn't say anything."
    scene 08_1918 with Dissolve(1)
    a "..."
    scene 08_1919 with Dissolve(1)
    a "IRIS!"
    mc "{i}(Iris? Is someone here?){/i}"
    scene 08_1920 with Dissolve(1)
    ir "Hey there."
    ir "That was so hot. I'm wet just watching you guys!"
    a "ARE YOU KIDDING ME?"
    scene 08_1921 with Dissolve(1)
    a "WHAT ARE YOU DOING HERE? GET OUT!"
    mc "Iris..."
    $ renpy.end_replay()
    if Andres_FB_Punch == False:
        scene black with Dissolve(2)
        pause 2
        n "A week ago."
        stop music fadeout 1.0
        play music "Sounds/Aeroplane_Onboard.mp3" volume 0.3
        scene 06_920 with Dissolve(1)
        mc "..."
        ir "Oh my god... [mc]!"
        mc "Hey. What are you doing here?"
        scene black with Dissolve(1)
        transform moveup:
            xalign 0.5 yalign 1.0
            linear 5.0 yalign 0.0
        show 08_1922 at moveup
        pause 3
        ir "What are you doing here? That's how you greet me?"
        scene 08_1923 with Dissolve(1)
        mc "Haha, I'm sorry, Iris."
        mc "It's nice to see you. How are you?"
        ir "Really good. How about you?"
        mc "So-so."
        ir "Hmm..."
        scene 08_1924 with Dissolve(1)
        mc "Wow, haha... I'm kinda speechless. You of all people."
        mc "I never thought we'd see each other again."
        ir "You and me both."
        scene 08_1925 with Dissolve(1)
        mc "And this is your seat?"
        ir "Uh-huh."
        mc "What a coincidence."
        ir "Tell me about it."
        scene 08_1926 with Dissolve(1)
        mc "I almost didn't recognise you. You've cut your hair."
        mc "And not just a little. It's really short now."
        ir "It was time for something new. Makes me look cute though, right?"
        menu:
            "No":
                scene 08_1927 with Dissolve(1)
                mc "Eh..."
                ir "Just say yes to make me happy! It was a big decision."
                mc "Haha."
            "Yes[KoGa3AutoWTChange1]{size=-4}(Iris Points+2) {/size} {/color}":
                $ Iris_Points += 2
                # Iris (2)
                scene 08_1928 with Dissolve(1)
                mc "It suits you. I like it."
                ir "Thanks."
        x "Uhm, excuse me miss. I think you're sitting in my seat."
        scene 08_1929 with Dissolve(1)
        ir "I know. I'm so sorry."
        ir "Look. The plane was almost completely booked when we got our tickets and there wasn't a row left with two empty seats."
        ir "And I really need to sit next to my boyfriend here because I'm terrified of flying."
        ir "Could we maybe swap seats? You would do me a huge favour!"
        scene 08_1930 with Dissolve(1)
        x "Uhm... I don't..."
        ir "Please..."
        x "*Sigh*"
        scene 08_1931 with Dissolve(1)
        ir "Thank you so much. I knew there were still gentlemen in this world."
        ir "My seat is C12. Bye."
        scene 08_1932 with Dissolve(1)
        mc "Coincidence..."
        ir "Haha."
        mc "Can't believe you get away with stuff like that. Every time..."
        ir "I'm charming."
        mc "Uh-huh. I actually think you didn't like the person you had to sit next to, so you were looking for another seat and here we are."
        scene 08_1933 with Dissolve(1)
        ir "Haha. You caught me!"
        mc "Yep. I know you."
        ir "You sure do."
        scene 08_1934 with Dissolve(1)
        ir "But if I didn't do that, we probably wouldn't have met again."
        mc "Also true."
        ir "And you'd probably rather sit next to me anyway."
        mc "Yeah, you're much nicer to look at."
        scene 08_1935 with Dissolve(1)
        if Alexis_Dating == False:
            ir "By the way, looking at you. You've changed too. More muscles and... tattoos!"
        else:
            ir "By the way, looking at you. You've changed too. More muscles and... tattoos!"
            mc "{i}(This feels a bit like deja-vu.){/i}"
        ir "Are you copying Dad?"
        mc "Haha. Maybe he influenced me a bit."
        ir "As you know, I've always been a daddy's girl. Looks good on you."
        scene 08_1936 with Dissolve(1)
        mc "How is John?"
        ir "He's good. I think he misses you sometimes."
        mc "Me?"
        ir "Yeah. You were my first boyfriend he actually liked."
        mc "Heh."
        scene 08_1937 with Dissolve(1)
        ir "He owns a garage now in Madison Springs."
        mc "Madison Springs?"
        ir "Yeah."
        mc "Weren't you moving to Novasota?"
        ir "We did. We'd been there a week when Dad got the offer. And I'm so glad for that."
        ir "Novasota is a shit hole. Madison Springs has beaches, a university, a big shopping district, good clubs. Heavenly."
        scene 08_1938 with Dissolve(1)
        mc "Haha."
        ir "What's so funny?"
        mc "I live in Madison Springs too."
        ir "What? No! Really? You guys moved there as well?"
        mc "Only me. I'm living with my mom again."
        scene 08_1939 with Dissolve(1)
        ir "What about your dad?"
        mc "Which one?"
        ir "Okay, tell me..."
        scene black with Dissolve(1)
        pause 2
        scene 08_1940 with Dissolve(1)
        ir "Now I'm speechless... And that never happens. Holy shit!"
        mc "Exactly."
        ir "I'm so sorry."
        scene 08_1941 with Dissolve(1)
        ir "But you're okay, right?"
        mc "Yeah, don't worry."
        ir "What else happened? I want to know everything now!"
        mc "Well..."
        scene black with Dissolve(1)
        pause 2
        n "A few hours later."
        scene 08_1933 with Dissolve(1)
        ir "Haha, that's so typical."
        mc "You would've done the same thing."
        ir "Probably."
        scene 08_1942 with Dissolve(1)
        ir "Hey [mc]?"
        mc "Hmm?"
        ir "Are you dating anyone?"
        if Alexis_Dating == False:
            scene 08_1943 with Dissolve(1)
            mc "Sort of..."
            ir "Sort of? What kind of answer is that? Tell me!"
            mc "..."
            mc "I'm still figuring it out myself."
            ir "Heh. I'll find out sooner or later."
        else:
            scene 08_1943 with Dissolve(1)
            mc "Sort of..."
            ir "Sort of? What kind of answer is that?"
            ir "Is she pretty?"
            mc "Very pretty."
            ir "Hmm..."
        scene 08_1944 with Dissolve(1)
        mc "How about you then? Are you seeing someone?"
        ir "There's someone I'm interested in."
        mc "Oh... Boy or girl?"
        ir "..."
        scene 08_1945 with Dissolve(1)
        mc "Girl?"
        ir "Yeah. She's best friends with my roommate."
        ir "Absolutely gorgeous. You'd probably like her too."
        mc "Call me intrigued."
        scene 08_1946 with Dissolve(1)
        ir "When I first met her, I felt this... like... immediate bond, I can't explain it. Do you know what I mean?"
        mc "Can't say for sure, but I'm a little jealous now."
        ir "Don't be. I felt the same with you, which makes this even more weird."
        scene 08_1947 with Dissolve(1)
        mc "You're dating her, or...?"
        ir "*Sigh* No. I've only talked to her a few times. I don't even know if she's into girls or not."
        mc "That's very easy to figure out."
        ir "Yeah? How?"
        scene 08_1948 with Dissolve(1)
        mc "Ask her!"
        ir "..."
        mc "Haha."
        scene 08_1949 with Dissolve(1)
        ir "How about you ask her for me?"
        ir "We should exchange numbers anyway and hang out again."
        ir "I'll introduce you to my roommate, so we can go on a double date."
        if Alexis_Dating == False:
            mc "Your roommate?"
            ir "She's very beautiful, too."
        else:
            mc "I told you I'm dating..."
            ir "Doesn't matter. I'm sure my roommate is prettier!"
            mc "..."
            mc "{i}(Prettier than Alexis? I don't think so.){/i}"
        scene black with Dissolve(1)
        pause 2
        scene 08_1950 with Dissolve(1)
        play sound "Sounds/Aeroplane_Beep.wav" volume 0.3
        pi "Please fasten your seatbelts..."
        ir "We're here already? Wasn't this a six-hour flight?"
        mc "It was."
        ir "Wow. I forgot how fast time passes when we hang out."
        ir "I have so much more to tell and ask."
        scene black with Dissolve(1)
        pause 2
        stop music fadeout 1.0
        play music ("Music/LoFi Upbeat 1.mp3", "Music/LoFi Upbeat 2.mp3", "Music/LoFi Upbeat 3.mp3", "Music/LoFi Upbeat 4.mp3") volume 0.2
        scene 08_1951 with Dissolve(1)
        ir "I'm really happy we met again. I didn't know I missed you this much."
        mc "Heh, same."
        ir "I've got your number now, so we'll stay in contact. Maybe we can do something during spring break?"
        mc "Sounds good."
        ir "Great! Double date incoming!"
        scene 08_1952 with Dissolve(1)
        ir "Kay, gotta go. I'll call you."
        mc "But please not at two in the morning, like you used to."
        ir "Haha, that's because I missed you when you weren't in my bed."
        mc "..."
        scene 08_1953 with Dissolve(1)
        ir "Bye, [mc]."
        mc "Bye..."
        scene 08_1954 with Dissolve(1)
        ir "Haha, sorry. Old habit."
        ir "Bye-bye."
        scene 08_1955 with Dissolve(1)
        ir "..."
        scene black with Dissolve(2)
        pause 2
        scene 08_1956 with Dissolve(1)
        ir "Hi again, [mc]."
        ir "Looks like I taught you well."
    else:
        scene 08_1956 with Dissolve(1)
        ir "Hi [mc]. Didn't think I'd ever see you again."
        ir "Looks like I taught you well, though."
    scene 08_1957 with Dissolve(1)
    a "What is she talking about? You know each other?"
    mc "We do..."
    ir "Do you want to tell her, or should I?"
    a "Tell me what?"
    scene 08_1958 with Dissolve(1)
    mc "Iris is my ex."
    a "..."
    a "Your..."
    a "That... doesn't matter now. We'll talk about that later."
    scene 08_1959 with Dissolve(1)
    a "Why are you here, Iris? Watching us... Don't you have any respect for my privacy?"
    ir "I have, and I'm sorry. I was waiting outside for a while. But I got curious and I wanted to know who the guy was."
    ir "It started with a quick peek but it turned me on so much that... Well..."
    a "..."
    scene 08_1960 with Dissolve(1)
    a "I'm sorry, but can you leave for today?"
    a "Iris and I need to have a serious conversation."
    mc "Yeah, I understand."
    scene 08_1961 with Dissolve(1)
    mc "Are you alright?"
    a "Mmm..."
    mc "Are you mad at me?"
    scene 08_1962 with Dissolve(1)
    a "What? No! You didn't do anything wrong."
    a "I'm just a little annoyed."
    a "I'll call you later, okay?"
    mc "Uhm, Lex."
    a "Yeah?"
    scene 08_1963 with Dissolve(1)
    mc "You look cute in it but can I have my t-shirt back?"
    mc "I don't really want to run around campus like this."
    a "Oh..."
    scene black with Dissolve(1)
    pause 2
    scene 08_1964 with Dissolve(1)
    mc "Good night."
    a "Night."
    scene 08_1965 with Dissolve(1)
    mc "Bye, Iris."
    ir "Bye, and sorry, [mc]."
    scene 08_1966 with Dissolve(1)
    a "Hey!"
    mc "Yeah?"
    scene 08_1967 with Dissolve(1)
    ""
    scene 08_1968 with Dissolve(1)
    a "This is a to be continued, okay?"
    mc "Haha. Of course."
    scene 08_1969 with Dissolve(1)
    mc "{i}(I hope this doesn't turn into another Erynn-Alexis fiasco.){/i}"
    if Alexis_Week4_Monday_Meet == False:
        jump Week4_Monday
    else:
        jump Week4_Wednesday

label Week4_Monday:
    scene black with Dissolve(2)
    pause 2
    stop music fadeout 1.0
    play music ("Music/LoFi Upbeat 3.mp3", "Music/LoFi Upbeat 4.mp3", "Music/LoFi Upbeat 2.mp3", "Music/LoFi Upbeat 1.mp3") volume 0.2
    n "Monday, 08:16. School."
    if Zach_Week3_Wednesday_TC_Girlshower == True:
        scene 08_1970 with Dissolve(1)
        mc "{i}(They're all here already?){/i}"
        mc "{i}(Should I even say anything? Why am I so nervous?){/i}"
        scene 08_1971 with Dissolve(1)
        mc "Morning."
        la "..."
        mc "{i}(Yeah... Exactly what I thought.){/i}"
        jump Week4_Monday_Spanish
    else:
        scene 08_1972 with Dissolve(1)
        mc "Morning, Zach."
        z "Hey man. How are you feeling? Have you recovered from training camp?"
        scene 08_1973 with Dissolve(1)
        mc "Could've used a few more days."
        z "Agreed. But it's almost spring break, anyway."
        z "Just too bad I'll be gone for most of it."
        if Zach_Week3_Thursday_TC_Box == True:
            mc "Too bad? You're going skiing. Doesn't sound bad to me."
            z "Well... Yeah..."
        else:
            mc "Going somewhere?"
            z "Skiing with my family."
            mc "That doesn't sound bad to me!"
            z "Well... Yeah..."
        la "Morning guys."
        scene black with Dissolve(1)
        transform moveup:
            xalign 0.5 yalign 1.0
            linear 5.0 yalign 0.0
        show 08_1974 at moveup
        pause 3
        if Layla_Dating == False:
            mc "Hey, morning Layla."
        else:
            mc "Hey there good-lookin'"
        z "Hi."
        scene 08_1975 with Dissolve(1)
        mc "Skirt day today?"
        la "Yeah and tights. Seems like you didn't get the memo again."
        mc "Haha. I mixed up the days."
        scene 08_1976 with Dissolve(1)
        am "Good morning."
        mc "Morning, Principal Moore."
        am "Layla! Can you come with me for a second?"
        la "Uhm, sure Mom..."
        if Adriana_Week3_Saturday_TC_Pick == False:
            scene 08_1977a with Dissolve(1)
            z "Mom?"
            la "*Sigh* Yeah, she's my mom. Keep this to yourself, please."
            z "..."
            mc "{i}(That's right. He didn't know that yet.){/i}"
            scene 08_1978 with Dissolve(1)
            z "I'm baffled right now. Did you know?"
            mc "She told me a few days ago."
            z "Now I know where she got her good looks from. Can't wait to see how Layla looks in a few years."
        else:
            scene 08_1977 with Dissolve(1)
            z "Ooh... Someone's in trouble."
            la "*Sigh* I'm not!"
            la "See you in class, [mc]."
            mc "Uh-huh. Later."
            scene 08_1978 with Dissolve(1)
            z "I'm still shocked she's Layla's mother."
            mc "Same."
            z "But you were right. She's so hot. Can't wait to see how Layla looks in a few years."
        mc "Like Alexis maybe? With shorter hair?"
        z "Oh yeah. They're sisters!"
        scene 08_1979 with Dissolve(1)
        z "Man... That family. What a gene pool."
        z "I wish I was born into that family!"
        mc "{i}(Are you sure about that?){/i}"
        scene 08_1980 with Dissolve(1)
        el "No family except yours wants you. Trust me."
        z "WHAT DID YOU..."
        scene black with Dissolve(1)
        transform moveup:
            xalign 0.5 yalign 1.0
            linear 5.0 yalign 0.0
        show 08_1981 at moveup
        pause 3
        z "..."
        mc "{i}(You've gotta love skirt and tights day...){/i}"
        scene 08_1982 with Dissolve(1)
        z "Oh hi, Elena. How are you? You look really pretty today."
        el "What's up with you? You're being weird."
        scene 08_1983 with Dissolve(1)
        el "Hi, [mc]."
        mc "Morning, Elena."
        el "Layla not here yet?"
        mc "She's with her mom."
        el "Oh, okay."
        scene 08_1984 with Dissolve(1)
        el "I'll go look for her."
        if Elena_Points >= 25:
            el "See you in chemistry."
            mc "Can't wait."
            mc "{i}(Can't wait? What?){/i}"
        else:
            el "See you in chemistry."
            mc "Later."
        scene 08_1985 with Dissolve(1)
        z "Damn... Was Elena always this cute or did she become more beautiful lately?"
        if Elena_Cute == True:
            mc "I told you at the club, she's always been cute."
        else:
            mc "Are you okay?"
            z "What? Yeah..."
        scene 08_1986 with Dissolve(1)
        mc "Is this about what happened at training camp?"
        z "I don't know. Ever since I had sex with Elena, I can't forget about her."
        mc "..."
        z "Do you think she secretly likes me too? Maybe that's why we're always fighting?"
        scene 08_1987 with Dissolve(1)
        mc "How about you talk to her and ask her?"
        z "*Sigh* Now?"
        mc "Whenever you feel like it."
        mc "Of course now!"
        mc "If you don't do it now, you never will."
        z "Okay, okay..."
        jump Week4_Monday_School_Chemistry

label Week4_Monday_School_Chemistry:
    scene black with Dissolve(1)
    pause 2
    scene 08_1988 with Dissolve(1)
    t "You can shake or stir, but the fluids won't mix."
    t "But if we heat them, you can see they're combining as the viscosity changes."
    scene 08_1989 with Dissolve(1)
    if Elena_Points >= 25:
        mc "{i}(Did she really have sex with Zach? She wouldn't, right?){/i}"
        mc "{i}(Why am I even questioning it myself, now?){/i}"
        mc "{i}(And why am I pissed off about it. Shouldn't I be happy for him?){/i}"
    else:
        mc "{i}(Did she really have sex with Zach?){/i}"
        mc "{i}(Why am I even questioning it myself, now?){/i}"
    scene 08_1990 with Dissolve(1)
    el "What?"
    mc "Uh... Nothing."
    scene 08_1991 with Dissolve(1)
    el "Then pay attention. I don't want to start over like last time, due to your mistakes."
    mc "My mistakes? Okay..."
    el "That's how I remember it. And I have the better memory!"
    mc "Haha."
    if Elena_Points >= 25:
        scene 08_1992 with Dissolve(1)
        mc "..."
        mc "{i}(Sexy!){/i}"
        scene 08_1993 with Dissolve(1)
        el "Okay, what?"
        el "You've been staring at me this whole time."
        mc "You look cute today."
        el "Thanks. But don't try to deflect my question by complimenting me!"
        el "Tell me what's going on!"
        scene 08_1994 with Dissolve(1)
        mc "Has Zach talked to you?"
    else:
        scene 08_1994 with Dissolve(1)
        mc "By the way. Has Zach talked to you yet?"
    el "No... Why would he talk to me?"
    mc "{i}(I knew it.){/i}"
    scene 08_1995 with Dissolve(1)
    mc "*Sigh* He believes..."
    mc "Well, he's actually pretty sure about it."
    el "[mc]!"
    scene 08_1996 with Dissolve(1)
    mc "He told me you guys had sex at camp."
    el "Haha. Totally. It was amazing!"
    mc "..."
    mc "So it's true?"
    scene 08_1997 with Dissolve(1)
    el "Wait, are you serious? I thought you were joking."
    mc "No. He strongly believes you guys slept together."
    el "What? Of course we didn't!"
    el "Dios mío... How obvious do I have to make it that I don't like that cabron..."
    scene 08_1994 with Dissolve(1)
    mc "Then you'd better go talk to him asap and tell him what happened, before he tells other people."
    el "Who else knows?"
    mc "Only me I think, but I'm not sure."
    scene 08_1998 with Dissolve(1)
    el "I'll go look for him immediately after class or this will be another Lucas-Layla fiasco, but this time it'll be Zach instead of Tori who's spreading the rumour."
    mc "{i}(So that's what happened between Layla and Tori.){/i}"
    mc "Tori told everyone Layla slept with Lucas?"
    el "Yes."
    el "She didn't FYI!"
    mc "I know."
    scene 08_1999 with vpunch
    t "ELENA!"
    el "Uh... Yes?"
    t "That's enough talking now. How about you answer the question?"
    el "Uhm..."
    if Layla_Week1_Monday_Payattention == True:
        scene 08_2001 with Dissolve(1)
        el "Sorry, I don't know."
        t "How about you pay attention then?"
        el "Yes, sorry."
    else:
        scene 08_2000 with Dissolve(1)
        mc "*Whisper* The answer is four!"
        el "*Whisper* Nice try. I'm not going to fall for that. Layla told me the story."
        scene 08_2001 with Dissolve(1)
        el "Sorry, I don't know."
        t "How about you pay attention then?"
        el "Yes, sorry."
        scene 08_2002 with Dissolve(1)
        t "It's four. Four ml."
        el "..."
        if Elena_Points >= 25:
            el "Just don't! And stop smirking!"
            scene 08_2002a with Dissolve(1)
            el "..."
        else:
            el "Just don't! And stop smirking!"
    jump Week4_Monday_Spanish

label Week4_Monday_Spanish:
    scene black with Dissolve(1)
    pause 2
    if Zach_Week3_Wednesday_TC_Girlshower == True:
        scene 08_2003 with Dissolve(1)
        if Week3_Monday_Spanish_Steal == True:
            mc "{i}(Still hasn't said a single word to me today.){/i}"
        else:
            if Week3_Monday_Spanish_Blackmail == True:
                mc "{i}(At least she'll get a B on her test. Maybe that will soften her mood a bit.){/i}"
            else:
                mc "{i}(I hope she did well on the test though.){/i}"
    else:
        scene 08_2003a with Dissolve(1)
        mc "You look nervous."
        la "I am. I need a good score on this test."
        if Week3_Monday_Spanish_Steal == True:
            mc "You'll be fine. Don't worry."
        else:
            if Week3_Monday_Spanish_Blackmail == True:
                mc "You'll be fine. Don't worry."
            else:
                if Layla_Week2_Wednesday_Knows == True:
                    mc "{i}(I should've helped her study...){/i}"
                else:
                    mc "You'll be fine. Don't worry."
    scene 08_2004 with Dissolve(1)
    tr "Good morning, everyone."
    if Week3_Monday_Spanish_Steal == True:
        tr "First of all, let me apologise. It seems like I've misplaced the tests from last week. I can't find them."
        if Gabi_End == True:
            n "Woohoo."
        else:
            n "Woohoo."
            scene black with Dissolve(1)
            transform moveup:
                xalign 0.5 yalign 1.0
                linear 5.0 yalign 0.0
            show 08_2007 at moveup
            pause 3
            mc "{i}(Damn, she looks good again...){/i}"
            mc "{i}(Can't believe I fucked her again. This time we can't blame the alcohol.){/i}"
            mc "{i}(I'm getting horny just thinking about it.){/i}"
        scene 08_2005 with Dissolve(1)
        tr "Meaning everyone will have to retake the test."
        la "What? Are you kidding me?"
        x "It's your fault you can't find the tests!"
        x "Yeah, this is so unfair."
        scene 08_2006 with Dissolve(1)
        tr "I'm sorry about that. But the test is important for your final grade."
        tr "It won't be today and it won't be the week after spring break, so you'll have some time."
        tr "We'll also be revising what's going to be on the test today."
        scene 08_2008 with Dissolve(1)
        la "*Sigh* Now I have to study again..."
        mc "I can help you if you want."
        la "Like you did last time?"
        if Zach_Week3_Wednesday_TC_Girlshower == True:
            mc "..."
        else:
            mc "..."
            scene 08_2009 with Dissolve(1)
            la "Sorry, I didn't mean it like that."
            mc "It's fine."
    else:
        tr "I've graded your tests from last week. I'll be handing them out and we'll look over every question together."
        if Week3_Monday_Spanish_Blackmail == True:
            scene 08_2010 with Dissolve(1)
            tr "..."
            scene 08_2012 with Dissolve(1)
            la "What? How?"
            mc "{i}(Looks like she got the grade she needed.){/i}"
            scene 08_2013 with Dissolve(1)
            la "I did it!"
            la "[mc], look! I did it!"
            mc "Congratulations!"
            la "I don't even know how. I was so sure I would fail."
            if Zach_Week3_Wednesday_TC_Girlshower == True:
                mc "{i}(I had to blackmail the teacher for this...){/i}"
                scene 08_2014 with Dissolve(1)
                la "I'm still mad at you, though."
                mc "Hehe, okay."
                mc "{i}(At least she talked to me.){/i}"
            else:
                mc "{i}(I had to blackmail the teacher for this...){/i}"
        else:
            if Layla_Week2_Wednesday_Knows == True:
                $ Layla_Week4_Monday_FailTest = True
                scene 08_2010 with Dissolve(1)
                tr "Let's talk after class, okay?"
                la "..."
                scene 08_2011 with Dissolve(1)
                la "*Sigh*"
                mc "{i}(Looks like she failed.){/i}"
                scene 08_2008 with Dissolve(1)
                mc "I can help you study if you want?"
                la "Like you did last time?"
                if Zach_Week3_Wednesday_TC_Girlshower == True:
                    mc "..."
                else:
                    mc "..."
                    scene 08_2009 with Dissolve(1)
                    la "Sorry, I didn't mean it like that."
                    mc "It's fine."
            else:
                scene 08_2010 with Dissolve(1)
                tr "Very nice, Layla!"
                la "..."
                scene 08_2012 with Dissolve(1)
                la "What?"
                la "No way!"
                scene 08_2013 with Dissolve(1)
                la "I did it!"
                la "[mc], look! I did it!"
                mc "Congratulations!"
                la "Thank you so very much for tutoring me."
                if Zach_Week3_Wednesday_TC_Girlshower == True:
                    mc "My pleasure."
                    scene 08_2014 with Dissolve(1)
                    la "I'm still mad at you, though."
                    mc "Hehe, okay."
                    mc "{i}(At least she talked to me.){/i}"
                else:
                    mc "My pleasure."
            scene 08_2015 with Dissolve(1)
            if Week3_Monday_Spanish_Blackmail == True:
                tr "..."
            else:
                tr "Bien hecho!"
                mc "Gracias."
    if Gabi_End == True:
        if Week3_Monday_Spanish_Steal == False:
            scene 08_2017 with Dissolve(1)
            tr "Empecemos con las preguntas de gramática.\n(Let's start with the grammar questions first.)"
        else:
            pass
        if Zach_Week3_Wednesday_TC_Girlshower == True:
            jump Week4_Monday_Cafeteria
        else:
            jump Week4_Monday_Hallway
    else:
        jump Week4_Monday_Spanish_Gabi

label Week4_Monday_Spanish_Gabi:
    scene 08_2016 with Dissolve(1)
    mc "{i}(What was that?){/i}"
    mc "{i}(Did she just smile at me?){/i}"
    scene 08_2017 with Dissolve(1)
    tr "Empecemos con las preguntas de gramática.\n(Let's start with the grammar questions first.)"
    mc "{i}(She should wear those jeans more often. Her ass looks so good in them...){/i}"
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 08_2018 at moveup
    pause 3
    mc "{i}(Seriously, how can anyone concentrate with this in front of them.){/i}"
    mc "{i}(No wonder so many flunked the test.){/i}"
    scene black with Dissolve(2)
    pause 2
    scene 08_2019 with Dissolve(1)
    tr "[mc], are you paying attention?"
    mc "Uhm... Yes."
    tr "Really? It seemed to me like you were staring at my butt."
    mc "{i}(What the fuck? Is she serious?){/i}"
    mc "I wasn't."
    scene 08_2020 with Dissolve(1)
    tr "Are you sure? Maybe you need a better look?"
    tr "How is this? Do you like that?"
    mc "Gabi... Ms Ramirez, what are you doing? You know we're in class, right?"
    mc "{i}(Doesn't she care about her job anymore?){/i}"
    tr "What? Too many clothes? We can change that."
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 08_2021 at moveup
    pause 3
    tr "Better?"
    mc "..."
    scene 08_2022 with Dissolve(1)
    mc "Ms Ramirez... I..."
    tr "Yes. I can't forget about you either."
    tr "I want you to fuck me, [mc]! Right here. In front of everyone."
    scene 08_2023 with Dissolve(1)
    tr "Oh yeah, [mc]!"
    tr "[mc]!"
    scene 08_2024 with vpunch
    tr "[mc]!"
    mc "..."
    scene 08_2025 with Dissolve(1)
    tr "I know you aced the test, but is this lesson really so boring that you fell asleep?"
    x "Haha, that idiot."
    mc "Uhm... No."
    tr "How about you stay a bit longer after class to make up for the lost time?"
    mc "..."
    scene 08_2026 with Dissolve(1)
    tr "Can I continue, or do you need some time?"
    x "Haha. You go, Ms Ramirez."
    mc "No, you can continue."
    tr "Bueno."
    mc "{i}(Fuck... That was so hot!){/i}"
    scene black with Dissolve(1)
    pause 2
    scene 08_2027 with Dissolve(1)
    mc "{i}(It's been ten minutes already. How long do I have to sit here for?){/i}"
    mc "{i}(She hasn't said a single word yet. Is she thinking about how to punish me?){/i}"
    scene 08_2028 with Dissolve(1)
    tr "[mc], you can leave now."
    mc "{i}(Finally! Not that I don't like being alone with her. But this was just awkward.){/i}"
    mc "Thanks."
    mc "{i}(I'd better apologise though.){/i}"
    scene 08_2029 with Dissolve(1)
    mc "Sorry, it's not that your lessons are boring."
    mc "I just..."
    scene 08_2030 with vpunch
    mc "..."
    scene black with Dissolve(1)
    pause 2
    scene 08_2031 with Dissolve(1)
    mc "*Heavy breathing*"
    mc "{i}(What the hell was that? That wasn't a dream, right?){/i}"
    $ renpy.end_replay()
    if Zach_Week3_Wednesday_TC_Girlshower == True:
        jump Week4_Monday_Cafeteria
    else:
        jump Week4_Monday_Hallway

label Week4_Monday_Cafeteria:
    scene black with Dissolve(1)
    pause 2
    scene 08_2032 with Dissolve(1)
    mc "*Sigh*"
    mc "{i}(This day is the worst...){/i}"
    mc "{i}(How can I fix this?){/i}"
    scene 08_2033 with Dissolve(1)
    el "Hey..."
    mc "Hey, Elena."
    el "..."
    mc "..."
    scene 08_2034 with Dissolve(1)
    mc "I'm sorry."
    mc "I didn't..."
    el "I know. Zach told me everything."
    mc "It still doesn't change the fact that I went along with it."
    scene 08_2035 with Dissolve(1)
    el "..."
    mc "..."
    scene 08_2036 with Dissolve(1)
    el "Can I have a sip?"
    mc "Of course."
    scene 08_2037 with Dissolve(1)
    el "Ew... This isn't coffee!"
    el "What is this?"
    mc "It's hot cocoa."
    el "You drink this?"
    mc "Sometimes..."
    scene 08_2038 with Dissolve(1)
    el "Actually, it isn't that bad. It threw me off because I expected it to taste like coffee."
    el "I'll keep this."
    mc "..."
    mc "{i}(Thank you, Elena!){/i}"
    if Layla_Week4_Monday_FailTest == True:
        scene 08_2039 with Dissolve(1)
        la "ELENA!"
        el "What's wrong with you?"
        la "I failed the Spanish test."
        el "You're kidding me?"
        la "No..."
        scene 08_2040 with Dissolve(1)
        el "I told you to study!"
        la "I did."
        el "*Sigh* What now? You have to retake the class?"
        la "I don't have to. I have enough credits already to graduate, but Mom's gonna be pissed."
        scene 08_2041 with Dissolve(1)
        la "I talked to Ms Ramirez. She'll let me retake the test if I agree to some tutoring during spring break."
        el "You've accepted, right?"
        la "I told her I'd think about it."
        el "No! You've done enough 'thinking'. Go to her now and tell her you're doing the tutoring."
        la "But..."
        el "NOW!"
        scene 08_2042 with Dissolve(1)
        la "Before I go. You guys talked?"
        el "Yes and I stole his drink, we're good."
        la "Great. We can't be fighting just before spring break."
        la "There's way too much fun to have."
        el "Now go talk to Ms Ramirez!"
        la "Fine..."
        scene 08_2054 with Dissolve(1)
        el "I'd better go with her. Moral support or something."
        mc "Heh, yeah."
        el "See you later, [mc]. And I'm keeping the hot cocoa!"
        mc "All yours. And thank you, Elena."
    else:
        if Week3_Monday_Spanish_Steal == True:
            scene 08_2039 with Dissolve(1)
            la "ELENA!"
            el "What's wrong with you?"
            la "I have to retake the Spanish test."
            el "You're kidding me? You failed?"
            la "No..."
            scene 08_2040 with Dissolve(1)
            la "Ms Ramirez lost the tests. She can't find them."
            el "What? How do you lose a bunch of tests..."
            la "I have no idea. But now I have to study again."
            el "Well, that's better than failing."
            scene 08_2042 with Dissolve(1)
            la "By the way. You guys talked?"
            el "Yes and I stole his drink, we're good."
            la "Great. We can't be fighting just before spring break."
            la "There's way too much fun to have."
        else:
            scene 08_2043 with Dissolve(1)
            la "ELENA!"
            el "What's wrong with you?"
            la "I passed!"
            el "What did you pass?"
            la "The Spanish test!"
            scene 08_2044 with Dissolve(1)
            el "Oh, congratulations!"
            la "Thank you."
            la "Now if I don't fail the final, I'm good."
            scene 08_2045 with Dissolve(1)
            el "That's a big if, though."
            la "Hey!"
            el "Haha."
            scene 08_2042 with Dissolve(1)
            la "I see you smiling again. Does that mean you guys talked?"
            el "Yes, and I stole his drink, we're good."
            la "Great. We can't be fighting just before spring break."
            la "There's way too much fun to have."
        scene 08_2054 with Dissolve(1)
        el "I'll take off. Cheer meeting."
        mc "Alright."
        el "See you later, [mc]. And I'm keeping the hot cocoa!"
        mc "All yours. And thank you, Elena."
    scene black with Dissolve(1)
    pause 2
    scene 08_2055 with Dissolve(1)
    z "Hey, man."
    mc "Hey."
    z "Uhm... I saw you talking to Elena."
    mc "Yeah, she told me you talked to her."
    scene 08_2056 with Dissolve(1)
    z "Look, I'm sorry. I really didn't want to spill anything."
    mc "Just take a seat, you don't have to stand there."
    scene 08_2057 with Dissolve(1)
    z "I don't even know why I did it. I think I was a bit frustrated."
    z "And as you know, Elena and I always butt heads."
    mc "It's all been cleared up, so let's just forget about it. No need to keep dragging this on."
    z "Thanks. I'm glad you're so forgiving."
    mc "Tell that to Elena. She's way too good of a friend for the likes of us."
    if Zach_Week3_Thursday_TC_Box == True:
        scene 08_2058 with Dissolve(1)
        mc "So, one more day, huh?"
        z "One more day?"
        mc "Aren't you going to buy that car tomorrow?"
        z "I am, I am. So stoked about it."
        if Emily_Week3_Sunday_Surprise == False:
            scene 08_2059 with Dissolve(1)
            z "You're still joining me?"
            mc "Of course. I can't wait to see it."
            z "It's so awesome."
            jump Week4_Monday_Afternoon
        else:
            scene 08_2059a with Dissolve(1)
            mc "Sorry, but I can't. My mom asked me to go somewhere."
            z "No worries. You'll see it when I drive to school with it."
            mc "Can't wait to see it."
            jump Week4_Monday_Afternoon
    else:
        jump Week4_Monday_Afternoon

label Week4_Monday_Hallway:
    scene black with Dissolve(1)
    pause 2
    if Layla_Week4_Monday_FailTest == True:
        scene 08_2046 with Dissolve(1)
        mc "{i}(Not here either.){/i}"
        mc "{i}(Where did she go?){/i}"
        scene black with Dissolve(1)
        pause 2
        scene 08_2047 with Dissolve(1)
        mc "{i}(This is the only place I haven't checked yet.){/i}"
        mc "{i}(Let's see.){/i}"
        scene 08_2048 with Dissolve(1)
        x "This is the girls' bathroom!"
        mc "Sorry. I need to talk to Layla."
        x "..."
        scene 08_2049 with Dissolve(1)
        mc "Layla?"
        mc "..."
        mc "I'm opening the door, okay?"
        scene 08_2050 with Dissolve(1)
        mc "Hey."
        la "I got an F."
        mc "I'm sorry."
        scene 08_2051 with Dissolve(1)
        mc "What now? You have to retake the class?"
        la "I don't have to. I have enough credits already to graduate, but Mom's gonna be pissed."
        mc "Isn't there anything else you can do? Didn't you talk to Ms Ramirez?"
        scene 08_2052 with Dissolve(1)
        la "I did. She'll let me retake the test if I agree to some tutoring during spring break."
        mc "You've accepted, right?"
        la "I told her I'd think about it."
        mc "What? No! Go to her now and tell her you're doing the tutoring. Seriously... I don't even understand why you have to think about this."
        la "But it's spring break..."
        mc "Now!"
        scene 08_2053 with Dissolve(1)
        la "*Sigh* Fine."
        la "Can you come with me?"
        mc "Sure."
        jump Week4_Monday_Afternoon
    else:
        if Layla_Dating == True:
            scene 08_2060 with Dissolve(1)
            la "Thank you, thank you, thank you!"
            mc "Haha, you're welcome."
            scene 08_2061 with Dissolve(1)
            la "I got a B! I still can't believe it."
            mc "I knew you could do it."
            scene 08_2062 with Dissolve(1)
            la "Now I only need to pass the final and I'm good."
            la "So we'll need to arrange another study session for that."
            scene 08_2063 with Dissolve(1)
            mc "Well, the word will get out that I helped you get a B."
            mc "I'll be very busy with all the students who want to get tutored by me now."
            mc "I don't know if I'll have time for you. I should also increase my price."
            la "..."
            scene 08_2064 with Dissolve(1)
            la "Your business only exists because of me!"
            la "I should get priority and a big discount!"
            mc "Hmm... Is that so? What else can you offer me?"
            scene 08_2065 with vpunch
            if Gabi_End == True:
                la "Here's something extra you won't get from anyone else."
                scene 08_2066 with Dissolve(1)
                mc "{i}(This is the first time she's kissed me like this in school.){/i}"
            else:
                la "Here's something extra you won't get from anyone else."
                mc "{i}(Didn't this just happen?){/i}"
                scene 08_2066 with Dissolve(1)
                mc "{i}(This is the first time she's kissed me like this in school.){/i}"
                scene 08_2067 with Dissolve(1)
                tr "..."
            scene 08_2068 with Dissolve(1)
            la "Hey!"
            mc "What?"
            la "Your hand!"
            mc "Isn't that the something extra?"
            la "I don't mind, but not here. What if my mom sees us?"
            scene 08_2069 with vpunch
            n "*Slap*"
            la "HEY! I just said..."
            mc "That wasn't me!"
            scene 08_2070 with Dissolve(1)
            el "It was him. I saw it!"
            mc "The culprit tries to blame someone else. Shocker..."
            la "I knew it."
            scene 08_2071 with Dissolve(1)
            el "Haha."
            mc "Seriously? You believe her without a second thought?"
            mc "She was standing behind you. Just look at her. She can't even keep her laughter in."
        else:
            if Week3_Monday_Spanish_Steal == True:
                scene 08_2061 with Dissolve(1)
                la "Hey! Here you are. What are you doing?"
                mc "Nothing. Was on my way to the cafeteria to get a coffee before the next class."
                scene 08_2062 with Dissolve(1)
                la "So we all have to retake the test..."
                mc "Uh-huh."
                la "We'll need to arrange a study session for that."
                scene 08_2063 with Dissolve(1)
                mc "Who says I'll help you?"
                mc "What's in it for me?"
            else:
                scene 08_2060 with Dissolve(1)
                la "Thank you, thank you, thank you!"
                mc "Haha, you're welcome."
                scene 08_2061 with Dissolve(1)
                la "I got a B! I still can't believe it."
                mc "I knew you could do it."
                scene 08_2062 with Dissolve(1)
                la "Now I only need to pass the exam and I'm good."
                la "So we'll need to arrange another study session for that."
                scene 08_2063 with Dissolve(1)
                mc "Well, the word will get out that I helped you get a B."
                mc "I'll be very busy with all the students who want to get tutored by me now."
                mc "I don't know if I'll have time for you, then. I should also increase my price."
                la "..."
                scene 08_2064 with Dissolve(1)
                la "Your business only exists because of me!"
                la "I should get priority and a big discount!"
                mc "Hmm... Is that so? What else can you offer me?"
            if Alexis_Dating == True:
                scene 08_2076 with Dissolve(1)
                la "How about I tell Alexis what a great guy you are?"
                mc "She knows that already."
                la "Psssh... Look at that confidence."
            else:
                la "How about I help you get a girlfriend?"
                mc "I don't need help with that."
                la "Psssh... Look at that confidence."
            la "Well, then there's only one more solution!"
            scene 08_2077 with vpunch
            la "Violence!"
            mc "Haha, violence. You're a funny girl."
            scene 08_2069 with vpunch
            n "*Slap*"
            la "Hey!"
            mc "That wasn't me!"
            scene 08_2070 with Dissolve(1)
            el "It was him. I saw it!"
            mc "The culprit tries to blame someone else. Shocker..."
            la "I knew it."
            scene 08_2071 with Dissolve(1)
            el "Haha."
            mc "Seriously? You believe her without a second thought?"
            mc "She was standing behind you. Just look at her. She can't even keep her laughter in."
        scene black with Dissolve(1)
        pause 2
        scene 08_2072 with Dissolve(1)
        el "Shall we go?"
        la "Yes. What class do you have next, [mc]?"
        mc "Math."
        la "Oh yeah, you're in the advanced class."
        mc "Yup."
        scene 08_2073 with Dissolve(1)
        la "See you later then."
        el "Have fun, nerd."
        mc "Haha, nerd? You're more of a nerd than me, chemistry girl!"
        el "Haha."
        scene 08_2074 with Dissolve(1)
        mc "Oh, and Elena?"
        el "Hmm?"
        mc "Did you talk..."
        el "I did!"
        scene 08_2075 with Dissolve(1)
        mc "I hope you let him down nicely."
        el "Haha... Hope as much as you want."
        la "What are you talking about?"
        el "Zach. I'll tell you in class."
    scene black with Dissolve(1)
    pause 2
    scene 08_2078 with Dissolve(1)
    mc "{i}(Here he is.){/i}"
    mc "{i}(Elena! What have you done to this guy?){/i}"
    scene 08_2079 with Dissolve(1)
    mc "Hey, man. What's up?"
    z "*Sigh* You were right."
    scene 08_2080 with Dissolve(1)
    z "I didn't have sex with Elena."
    mc "You talked to her?"
    z "Heh... She talked to me!"
    scene 08_2081 with Dissolve(1)
    mc "But isn't that what you wanted? You don't like Elena anyway, or...?"
    z "..."
    z "I'm still a fucking virgin though."
    mc "Look at the bright side. Now you can still choose who you want your first time to be with."
    scene 08_2082 with Dissolve(1)
    z "Do me a favour and don't tell anyone about this, okay?"
    mc "Sure."
    z "I hope Elena won't say anything either."
    mc "{i}(Elena is probably the last person who'd want that rumour to spread.){/i}"
    scene 08_2083 with Dissolve(1)
    va "Good morning, guys."
    z "..."
    mc "Oh no, you didn't..."
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 08_2084 at moveup
    pause 3
    va "What?"
    mc "Don't tell me you joined their 'let's all wear skirts tomorrow' day."
    scene 08_2085 with Dissolve(1)
    va "Haha, no. Maybe just this once."
    va "Normally I don't wear stuff like this. I just wanted to try it."
    scene 08_2086 with Dissolve(1)
    mc "Uh-huh, just once... And tomorrow it's tanktop day, specifically pink ones."
    va "Haha. You know that already?"
    mc "I'm kidding. I have no idea."
    scene 08_2087 with Dissolve(1)
    va "Well, I'm heading to my next class."
    mc "Which is?"
    va "English literature."
    mc "Oh, together with Layla and Elena?"
    va "Yes. And Sienna."
    z "And Mr Donovan..."
    scene 08_2088 with Dissolve(1)
    mc "Have fun."
    va "See you later, at lunch?"
    mc "Same time, same place."
    va "Hehe. Bye-bye."
    mc "Later, Val."
    if Valeria_Points >= 9:
        scene 08_2089 with Dissolve(1)
        mc "Oh and Val."
        va "Hmm?"
        mc "It looks good on you."
        va "Thank you!"
        scene 08_2079 with Dissolve(1)
        z "How do you do that?"
        mc "Do what?"
        z "You talk so casually to her and she smiles and laughs the whole time."
        z "She never laughs like that when I talk to her."
        mc "Uhm, I don't know. I'm just having a normal conversation with her."
        z "..."
        scene 08_2090 with Dissolve(1)
        z "But you were right though."
        z "She looked really good. Did you see those legs? She should wear that more often. Damn..."
        z "Think I should go talk to her and try once more? Since the Elena situation didn't happen, I might still have a chance, right?"
        mc "{i}(... You're going to anyway.){/i}"
        mc "Go ahead."
        z "Normal conversation. Normal... Aaah. Feeling so much better already. Later, [mc]."
        mc "Later."
    else:
        scene 08_2079 with Dissolve(1)
        z "How do you do that?"
        mc "Do what?"
        z "You talk so casually to her and she smiles and laughs the whole time."
        z "She never laughs like that when I talk to her."
        mc "Uhm, I don't know. I'm just having a normal conversation with her."
        z "..."
        scene 08_2090 with Dissolve(1)
        z "She looked really good though, right? Did you see those legs? She should wear that more often. Damn..."
        z "Think I should go talk to her and try once more? Since the Elena situation didn't happen, I might still have a chance, right?"
        mc "{i}(... You're going to anyway.){/i}"
        mc "Go ahead."
        z "Normal conversation. Normal... Aaah. Feeling so much better already. Later, [mc]."
        mc "Later."
    scene 08_2091 with Dissolve(1)
    mc "*Sigh*"
    mc "{i}(If he spent all his energy on one girl instead of chasing a new girl every day, he would have a girlfriend by now.){/i}"
    mc "..."
    mc "{i}(Unlikely, but maybe...){/i}"
    jump Week4_Monday_Afternoon

label Week4_Monday_Afternoon:
    stop music fadeout 1.0
    play music ("Music/LoFi Indie 1.mp3", "Music/LoFi Indie 2.mp3", "Music/LoFi Indie 3.mp3") volume 0.2
    if Layla_Dating == True:
        scene black with Dissolve(2)
        pause 2
        n "Monday, 16:57."
        scene 08_2092 with Dissolve(1)
        mc "*Sings* Don't you know that you're toxic?"
        play sound "Sounds/Phone_Vibrate.mp3"
        n "*Bzzzt. Bzzzt*"
        menu:
            "Answer":
                scene 08_2093 with Dissolve(1)
                mc "Hey Layla."
                la "Hey. What are you doing?"
                scene 08_2094 with Dissolve(1)
                mc "Nothing special. I was just playing a song on my guitar."
                la "Oh... I didn't know you played the guitar. What were you playing?"
                mc "Toxic."
                la "Haha, Britney?"
                mc "Yeah. For some reason it got stuck in my head, and before I knew it, I was playing it."
                la "It's catchy, I'll give you that."
                mc "It is. What's up?"
            "Joke":
                scene 08_2093 with Dissolve(1)
                mc "It's Britney, bitch."
                la "Haha, what?"
                mc "Hey Layla."
                la "Hey. What's with Britney?"
                scene 08_2094 with Dissolve(1)
                mc "Haha, nothing. I was just playing a song on my guitar."
                la "Oh... I didn't know you played the guitar. A Britney song?"
                mc "Yeah. Toxic. For some reason it got stuck in my head, and before I knew it, I was playing it."
                la "It's catchy, I'll give you that."
                mc "It is. What's up?"
        scene 08_2095 with Dissolve(1)
        la "Remember when you were tutoring me last time, we were talking about having a hot tub party?"
        mc "I remember."
        la "Well, I'm having one today to celebrate me not flunking the Spanish test."
        scene 08_2096 with Dissolve(1)
        mc "That seems like a perfect reason to have a party..."
        la "Right? I thought so, too."
        mc "{i}(Haha, this girl.){/i}"
        mc "I was being sarcastic."
        scene 08_2097 with Dissolve(1)
        la "..."
        la "So, you're not coming?"
        if Layla_Week3_Wednesday_TC_Alexis_DateBoth == False:
            $ Layla_Week4_Monday_Hottub = True
            jump Week4_Monday_Layla_Hottub
        else:
            if Alexis_Week3_Sunday_Meet == True:
                $ Layla_Week4_Monday_Hottub = True
                jump Week4_Monday_Layla_Hottub
            else:
                mc "{i}(I actually wanted to go see Alexis today, since I didn't yesterday.){/i}"
                mc "{i}(But I also want to go to the hot tub party...){/i}"
                menu:
                    "Meet Alexis[KoGa3AutoWTChange1]{size=-4}(Layla Points-4) {/size} {/color}":
                        $ Layla_Points -= 4
                        scene 08_2098 with Dissolve(1)
                        mc "I'm sorry, Layla. I can't today. I have plans already."
                        mc "Rain check?"
                        la "Sure. See you tomorrow then. Bye."
                        mc "Bye, Layla."
                        jump Week4_Monday_Alexis_Meet
                    "Hot tub party[KoGa3AutoWTChange1]{size=-4}(Layla Week4 Monday Hottub, Alexis Points-6) {/size} {/color}":
                        $ Layla_Week4_Monday_Hottub = True
                        $ Alexis_Points -= 6
                        jump Week4_Monday_Layla_Hottub
    else:
        if Alexis_Dating == True:
            if Alexis_Week3_Sunday_Meet == False:
                jump Week4_Monday_Alexis_Meet
            else:
                jump Week4_Wednesday
        else:
            jump Week4_Wednesday

label Week4_Monday_Layla_Hottub:
    $ Layla_Week4_Monday_Hottub_BJ = True
    scene 08_2099 with Dissolve(1)
    mc "What no, of course, I'm coming. I'm not turning down a hot tub party."
    la "Hehe, cool."
    mc "Do I need to bring anything? Snacks, drinks? Or call someone?"
    la "No, I've got it all covered. Only a bathing suit."
    scene 08_2100 with Dissolve(1)
    mc "Alright. Around what time?"
    la "Seven o'clock!"
    mc "Seven? Okay. See you then."
    la "Later, [mc]."
    scene 08_2101 with Dissolve(1)
    la "..."
    scene black with Dissolve(1)
    pause 2
    scene 08_2102 with Dissolve(1)
    la "Hey, there."
    mc "Hi."
    mc "I see you're in uniform already."
    la "Haha yeah."
    scene 08_2103 with Dissolve(1)
    mc "I'm so ready for this hot tub party."
    la "Hehe."
    la "Come on, get in before the neighbours see me standing here like this."
    scene 08_2104 with Dissolve(1)
    mc "{i}(Yeah, can't have them seeing this view.){/i}"
    scene black with Dissolve(1)
    pause 2
    scene 08_2105 with Dissolve(1)
    mc "Oh. I'm the first one here?"
    la "Uhm... Yeah."
    scene 08_2106 with Dissolve(1)
    la "You can go in. I'm gonna get us some drinks."
    la "I'll also get you a towel, since you didn't bring one."
    mc "Hey, I asked if I had to bring anything. You said no!"
    la "I thought that was a given, since we'll be in a hot tub."
    scene 08_2107 with Dissolve(1)
    mc "{i}(This is my first time in a hot tub.){/i}"
    mc "{i}(Feels nice.){/i}"
    scene black with Dissolve(1)
    pause 2
    scene 08_2108 with Dissolve(1)
    la "I'm back."
    la "I don't know what my dad would do if he found out some beers were missing, so I got us soda instead."
    mc "Soda is fine, thanks."
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 08_2109 at moveup
    pause 3
    mc "{i}(She's such a cutie.){/i}"
    la "How's the water for you?"
    mc "It's good."
    mc "{i}(Even better now you're in here.){/i}"
    scene 08_2110a with Dissolve(1)
    mc "This feels so nice. Can I come over every day so I can use your hot tub?"
    la "Haha, sure. I don't mind."
    scene 08_2110 with Dissolve(1)
    mc "Who else is coming? Elena probably?"
    la "Uhm... No one. I only invited you."
    mc "Oh?"
    scene 08_2111 with Dissolve(1)
    la "I wanted to be alone with you."
    la "I'm sorry..."
    mc "Don't be. I don't mind at all. I'd rather be alone with you, anyway."
    scene 08_2112 with Dissolve(1)
    mc "Now we have this all to ourselves."
    la "Mmm-hmm."
    scene 08_2113 with Dissolve(1)
    mc "Is this a new one?"
    la "The bikini? No, it's an older one. My others are still in the laundry."
    mc "They still look nice."
    scene 08_2114 with Dissolve(1)
    la "Are you talking about the bikini or something else?"
    mc "Haha."
    scene 08_2115 with Dissolve(1)
    mc "Both!"
    la "..."
    scene 08_2116 with Dissolve(1)
    ""
    scene 08_2117 with Dissolve(1)
    mc "Hey cutie."
    la "Hey."
    scene 08_2118 with Dissolve(1)
    mc "{i}(She keeps on taking more initiative. So different compared to her shyness at first.){/i}"
    mc "{i}(Is this maybe her real personality? Before the Lucas situation?){/i}"
    scene 08_2119 with Dissolve(1)
    ""
    scene 08_2120 with Dissolve(1)
    la "[mc], wait..."
    mc "{i}(Maybe still a little shy.){/i}"
    scene 08_2121 with Dissolve(1)
    la "Let me take it off."
    mc "{i}(Maybe not.){/i}"
    mc "Can I?"
    la "Sure."
    scene 08_2122 with Dissolve(1)
    mc "{i}(I can never get enough of them.){/i}"
    scene 08_2123 with Dissolve(1)
    mc "{i}(I can't wait to finally taste them...){/i}"
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 08_2124 at moveup
    pause 3
    la "Why are you smiling like that? You look like a kid in a candy store."
    mc "Because I am!"
    la "Haha."
    mc "You look incredible, Layla."
    la "Thank you."
    scene 08_2125 with Dissolve(1)
    mc "Where are you going?"
    la "Come here!"
    mc "..."
    scene 08_2126 with Dissolve(1)
    mc "You're half-naked already and now you're playing hard to get and making me chase you?"
    la "If someone's hard to get, it's you!"
    la "I've been flirting with you for weeks."
    scene 08_2127 with Dissolve(1)
    mc "Oh, that's what that was."
    la "Ha-ha-ha!"
    scene 08_2128 with Dissolve(1)
    la "Is my flirting that bad?"
    mc "I wouldn't be here if it was. You're really cute."
    scene 08_2129 with Dissolve(1)
    mc "Besides, you have no idea how you make me feel."
    la "Hmm, I think I have a pretty good idea, because of something else I'm feeling!"
    mc "..."
    scene 08_2130 with Dissolve(1)
    mc "Come here you little tease."
    la "Haha."
    scene black with Dissolve(1)
    pause 2
    scene 08_2131 with Dissolve(1)
    mc "You are so beautiful, Layla!"
    scene 08_2132 with Dissolve(1)
    ""
    scene 08_2133 with Dissolve(1)
    la "Aah..."
    scene 08_2134 with Dissolve(1)
    la "Mmm."
    scene 08_2135 with Dissolve(1)
    mc "{i}(Even her moans are cute.){/i}"
    scene black with Dissolve(1)
    pause 2
    scene 08_2136 with Dissolve(1)
    ""
    scene 08_2137 with Dissolve(1)
    ""
    scene 08_2138 with Dissolve(1)
    mc "{i}(She's pulling my pants down?){/i}"
    mc "{i}(Seems we're going further than I thought.){/i}"
    mc "{i}(Just thinking about it gets me harder. If that's even possible. It was throbbing like crazy already.){/i}"
    scene 08_2139 with Dissolve(1)
    mc "{i}(Fuck...){/i}"
    scene 08_2140 with Dissolve(1)
    la "Hehe."
    mc "What are you giggling about?"
    la "It's the first time I'm holding a..."
    mc "Holding what?"
    la "You know what! Your..."
    scene 08_2141 with Dissolve(1)
    mc "I have no idea what you mean."
    la "..."
    mc "Say it!"
    la "A penis!"
    scene 08_2142 with Dissolve(1)
    mc "Haha. Someone paid attention in biology."
    mc "So formal."
    la "..."
    la "Dick, cock, johnson, weenie..."
    mc "Haha."
    scene 08_2143 with Dissolve(1)
    mc "You're cute!"
    la "..."
    scene black with Dissolve(1)
    pause 2
    scene 08_2144 with Dissolve(1)
    mc "{i}(For it being her first time, she's good at it.){/i}"
    mc "{i}(She must watch porn.){/i}"
    scene 08_2145 with Dissolve(1)
    la "Is this good, or am I doing it wrong?"
    mc "No, it's amazing, Layla!"
    show 08_2146
    mc "{i}(She definitely watches porn.){/i}"
    mc "{i}(This feels so good.){/i}"
    scene black with Dissolve(1)
    pause 2
    scene 08_2147 with Dissolve(1)
    la "..."
    scene 08_2148 with Dissolve(1)
    mc "{i}(Oh... Is she?){/i}"
    scene 08_2149 with Dissolve(1)
    mc "{i}(She's actually giving me a blowjob.){/i}"
    scene 08_2150 with Dissolve(1)
    mc "{i}(Fuck, this is amazing.){/i}"
    mc "Damn... Layla!"
    show 08_2151
    ""
    scene black with Dissolve(1)
    pause 2
    scene 08_2152 with Dissolve(1)
    mc "Layla... I'm cumming..."
    mc "Layla!"
    scene 08_2153 with Dissolve(1)
    la "..."
    scene 08_2154 with Dissolve(1)
    la "Mmm-mmm..."
    mc "Haha. Just spit it out."
    la "Mmm..."
    mc "I don't know. Anywhere."
    scene 08_2155 with Dissolve(1)
    mc "{i}(Is she swallowing it?){/i}"
    mc "{i}(This girl...){/i}"
    scene 08_2156 with Dissolve(1)
    la "Bleh!"
    mc "Haha. Why did you swallow? You could've just spat it out somewhere."
    la "I didn't want to be rude."
    mc "..."
    la "It reminded me of the kiss we had in the ocean..."
    mc "Haha. Layla..."
    scene 08_2157 with Dissolve(1)
    mc "You okay?"
    la "Yeah, I'll be right back. Gonna brush my teeth real quick."
    mc "Heh, okay."
    $ renpy.end_replay()
    scene 08_2158 with Dissolve(1)
    mc "{i}(She surprised me today. That blowjob was amazing.){/i}"
    mc "{i}(What a day...){/i}"
    if Alexis_Intro_Ignore == True:
        if Erynn_End == True:
            jump Week4_Monday_Layla_Hottub_Adriana
        else:
            if Erynn_LikeMC == True:
                jump Week4_Monday_Layla_Hottub_Adriana
            else:
                if Erynn_Week3_Monday_Blackmailhelp == False:
                    jump Week4_Monday_Layla_Hottub_Adriana
                else:
                    jump Week4_Monday_Layla_Hottub_AlexisErynn
    else:
        jump Week4_Monday_Layla_Hottub_Adriana

label Week4_Monday_Layla_Hottub_Adriana:
    if _in_replay:
        $ Adriana_Points = 4
        $ MC_Week3_Saturday_TC_Win = True
        $ Alexis_Dating = True
    scene black with Dissolve(2)
    pause 2
    scene 08_2159 with vpunch
    am "Looks like you're enjoying yourself."
    mc "..."
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 08_2160 at moveup
    pause 3
    mc "{i}(Holy shit!){/i}"
    mc "Principal Moore!"
    mc "{i}(And I'm hard again...){/i}"
    if Adriana_Points == 4:
        am "I've told you before. Here, I'm Adriana."
        mc "Sorry."
    else:
        am "Hey [mc]."
        am "And it's Adriana here."
    scene 08_2161 with Dissolve(1)
    am "Layla invited you over?"
    mc "Uhm, yeah."
    mc "{i}(Fuck, is she getting in here? What if she came just a few minutes earlier...){/i}"
    mc "{i}(Where are my shorts?){/i}"
    scene 08_2162 with Dissolve(1)
    if MC_Week3_Saturday_TC_Win == True:
        am "I heard you won the 100-meter race. Congratulations!"
        mc "Thank you."
        am "How was training camp?"
        mc "Really good. I enjoyed it. Training was tough, though."
    else:
        am "How was training camp?"
        mc "Really good. I enjoyed it. Training was tough, though."
    scene 08_2163 with Dissolve(1)
    am "Haha. Did Coach Morgan make you run laps?"
    mc "He did. Every day!"
    mc "{i}(She must do pilates or something to stay in shape like this.){/i}"
    mc "{i}(Maybe she and Melissa do yoga together?){/i}"
    scene 08_2164 with Dissolve(1)
    am "Aaah, this is great after a long day."
    mc "{i}(I'm sitting in a hot tub with my principal, who's also Layla's mom...){/i}"
    if Adriana_Points == 4:
        mc "{i}(Why isn't this awkward? It should be awkward, no?){/i}"
        mc "{i}(When's Layla coming back?){/i}"
    else:
        mc "{i}(When's Layla coming back?){/i}"
    scene 08_2165 with Dissolve(1)
    am "How's your mom?"
    mc "She's good. Very busy."
    am "I believe that. We tried to get a table today, but the restaurant was fully booked."
    mc "Oh. Do you want me to call her? I can maybe..."
    am "No-no, no need. Thank you for the offer. We've already made reservations for Sunday."
    scene 08_2166 with Dissolve(1)
    la "MOM!"
    la "What are you doing here? Weren't you going out with Dad?"
    am "We had a change of plans. He went to the bar instead."
    la "..."
    scene 08_2167 with Dissolve(1)
    la "But why are you in the hot tub with [mc]?"
    la "This is just weird. First of all, you're my mom, and second you're also the principal."
    am "At school, I'm the principal. This is my home and I want to enjoy the hot tub. That simple."
    la "But..."
    scene 08_2168 with Dissolve(1)
    la "Would you have gone in if one of Dad's friends was in here?"
    am "No, that's different."
    la "What? How is that different?"
    la "*Sigh*"
    scene 08_2169 with Dissolve(1)
    la "Come on, [mc], let's watch some TV or something..."
    la "Let my mom 'enjoy' the hot tub."
    am "Don't get snippy with me now!"
    scene 08_2170 with Dissolve(1)
    mc "Uhm..."
    mc "*Shakes head*"
    mc "{i}(I'm not wearing anything...){/i}"
    scene 08_2171 with Dissolve(1)
    la "Oh..."
    la "Mom! We need to talk."
    am "Now?"
    la "It's urgent. Please?"
    scene 08_2172 with Dissolve(1)
    am "Slow down a bit, will you?"
    scene 08_2173 with Dissolve(1)
    am "What is it you want to talk about that is so urgent?"
    la "Uhm... Not here. Let's just go inside for a minute."
    scene 08_2174 with Dissolve(1)
    mc "{i}(Come on... They must be here somewhere...){/i}"
    mc "{i}(Good thing Adriana didn't find them. That would've been something to explain.){/i}"
    mc "{i}(Oh, I've got them.){/i}"
    scene 08_2175 with Dissolve(1)
    mc "{i}(Nope... Not doing this again!){/i}"
    scene black with Dissolve(1)
    pause 2
    scene 08_2176 with Dissolve(1)
    la "Ah good, you found them."
    mc "Yeah, also got your top. I put it next to the towel."
    la "Thanks."
    scene 08_2177 with Dissolve(1)
    la "*Sigh* I'm sorry. My parents were supposed to be gone for two more hours."
    mc "It's fine. We had fun anyway, right?"
    la "Yeah."
    scene 08_2178 with Dissolve(1)
    mc "Does your mom know that..."
    if Adriana_Points == 4:
        la "Maybe? She knows we didn't just sit in the hot tub and talk. I don't think she minds though, because she likes you."
        scene 08_2179 with Dissolve(1)
        mc "She does?"
        la "Uh-huh."
        mc "That's good I guess."
        mc "{i}(I hope I can keep it that way.){/i}"
        mc "I was so nervous that she would find my shorts while she was getting in."
        la "Good thing Dad went to the bar. Or else this would've gone a whole different way..."
    else:
        la "Maybe? She knows we didn't just sit in the hot tub and talk."
        scene 08_2179 with Dissolve(1)
        mc "I was so nervous that she would find my shorts while she was getting in."
        la "Good thing Dad went to the bar. Or else this would've gone a whole different way..."
    scene 08_2180 with Dissolve(1)
    la "Actually, I don't know. I've never had a boy over, except last time, when you helped me study. So I have no idea how he would react."
    mc "How did he react when Alexis brought someone over?"
    if Alexis_Dating == True:
        la "She never has."
        mc "{i}(Well...){/i}"
    else:
        la "She never has."
        mc "Oh..."
    scene 08_2181 with Dissolve(1)
    mc "So, I'm like an experiment?"
    la "Haha, you could say that."
    scene 08_2182 with Dissolve(1)
    mc "*Sigh* Anyway, I think I'd better leave for today."
    la "You don't have to. We can still watch some TV."
    mc "We'll find plenty of time during spring break to hang out."
    la "*Nods*"
    scene 08_2183 with Dissolve(1)
    la "I'll show you out, then."
    mc "Thanks."
    scene 08_2184 with Dissolve(1)
    am "You're leaving already?"
    mc "Yeah, school night."
    am "Haha. Good answer!"
    scene 08_2185 with Dissolve(1)
    la "I thought you weren't the principal here?"
    am "*Sigh* I hope she's nicer to you..."
    mc "Hehe, bye Adriana."
    am "Bye, [mc]."
    scene black with Dissolve(1)
    pause 2
    scene 08_2186 with Dissolve(1)
    mc "Thank you for today. It was amazing."
    la "Hehe, you're welcome."
    la "See you tomorrow at school?"
    mc "Definitely."
    scene 08_2187 with Dissolve(1)
    ""
    scene 08_2188 with Dissolve(1)
    mc "Bye, Layla."
    la "Bye-bye."
    la "One more thing."
    mc "Yeah?"
    scene 08_2189 with Dissolve(1)
    mc "..."
    mc "What are you doing to me?"
    la "Haha."
    scene black with Dissolve(1)
    pause 2
    scene 08_2190 with Dissolve(1)
    am "LAYLA!"
    la "Yes?"
    am "Come here for a second!"
    scene 08_2191 with Dissolve(1)
    la "What?"
    am "Join me."
    scene 08_2192 with Dissolve(1)
    la "Okay, what is it?"
    am "Do we need to talk?"
    la "Oh, we're so not doing this!"
    scene 08_2193 with Dissolve(1)
    am "Listen, please. You know I was pregnant with Lexi when I was eighteen and I..."
    la "Mom!"
    am "Layla, I just want you to be safe."
    am "Are you being safe?"
    la "..."
    am "Layla?"
    scene 08_2194 with Dissolve(1)
    la "We're not having sex, okay?"
    am "Okay."
    scene 08_2195 with Dissolve(1)
    am "Take your time."
    la "I am."
    am "I love you."
    la "Love you too, Mom."
    $ renpy.end_replay()
    jump Week4_Wednesday

label Week4_Monday_Layla_Hottub_AlexisErynn:
    if _in_replay:
        $ Alexis_SP = 0
    scene black with Dissolve(2)
    pause 2
    scene 08_2159 with vpunch
    a "Haha, here?"
    x "Yes!"
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 08_2196 at moveup
    pause 3
    mc "{i}(Alexis...){/i}"
    x "Okay, now stop and pose!"
    mc "..."
    scene 08_2197 with Dissolve(1)
    er "That was perfect, Lex. Take a look!"
    mc "{i}(And Erynn... What are they doing here?){/i}"
    mc "{i}(Shit... Where are my shorts? Please just leave without noticing me.){/i}"
    scene 08_2198 with Dissolve(1)
    a "I don't know. It looks kinda off."
    er "What are you talking about? You're gorgeous!"
    er "Let's take one together, now."
    scene 08_2199 with Dissolve(1)
    a "Erynn, look! We have a spectator."
    mc "{i}(I should've dove underwater...){/i}"
    er "Hmm? Oh... [mc]!"
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 08_2200 at moveup
    pause 3
    mc "Hey Erynn."
    er "Hey. Such a surprise! What are you doing here?"
    mc "Uhm... Layla invited me... To celebrate passing her Spanish test?"
    er "Where is she?"
    mc "{i}(Brushing her teeth after she gave me a blowjob...){/i}"
    mc "Uhm... Bathroom."
    scene 08_2201 with Dissolve(1)
    er "You remember Alexis? She's Layla's sister."
    mc "Yeah, we've met."
    a "A few times already, actually."
    er "Really? Hmm... Interesting."
    scene 08_2202 with Dissolve(1)
    mc "{i}(They're getting in?){/i}"
    er "What did you think of Lexi's posing just now?"
    a "Erynn... Don't ask him."
    er "No, it's good to have someone else's opinion."
    er "So?"
    menu:
        "Pretty[KoGa3AutoWTChange1]{size=-4}(Alexis SecretPath, Alexis SP+2) {/size} {/color}":
            $ Alexis_SecretPath = True
            $ Alexis_SP += 2
            # Alexis_SP (2)
            scene 08_2203 with Dissolve(1)
            $ achievement.grant("ACHIEVEMENT_STEAL_BOY")
            $ achievement.sync()
            mc "I thought you looked pretty!"
            a "Thanks."
            er "See, I told you!"
        "Not so good":
            scene 08_2204 with Dissolve(1)
            mc "Hmm. It looked a little stiff to me."
            a "I told you!"
            er "Don't listen to him. What does he know about posing?"
            mc "Hey, you asked me..."
    scene 08_2205 with Dissolve(1)
    er "Aaaanyway. Let's take some more pictures. Since we have a photographer now."
    mc "Me?"
    er "Yeah, you!"
    mc "Sure, I guess."
    scene black with Dissolve(1)
    pause 2
    scene 08_2206 with Dissolve(1)
    ""
    scene 08_2207 with Dissolve(1)
    ""
    scene 08_2208 with Dissolve(1)
    ""
    scene black with Dissolve(1)
    pause 2
    scene 08_2209 with Dissolve(1)
    mc "{i}(Wait... Are they going to kiss?){/i}"
    scene 08_2210 with Dissolve(1)
    n "Haha."
    scene 08_2211 with Dissolve(1)
    mc "{i}(Okay... They're just teasing me.){/i}"
    mc "{i}(*Shakes head* Girls...){/i}"
    scene 08_2212 with Dissolve(1)
    er "What's with that look?"
    mc "What look?"
    er "Are you judging us?"
    mc "No..."
    er "Uh-huh."
    scene 08_2213 with Dissolve(1)
    er "Let's do a topless one next."
    mc "..."
    scene 08_2214 with Dissolve(1)
    er "See how fast his face turned from judgement to excitement?"
    mc "..."
    er "To disappointment, now."
    a "Haha."
    scene 08_2215 with Dissolve(1)
    er "We're kidding!"
    mc "I figured..."
    scene 08_2216 with Dissolve(1)
    er "Or are we?"
    a "Haha. Erynn, stop!"
    er "Just a little?"
    a "Haha. Do it yourself..."
    scene black with Dissolve(1)
    pause 2
    scene 08_2217 with Dissolve(1)
    a "Thanks for taking the pictures, [mc]."
    er "Thank you."
    mc "You're welcome."
    er "Let's take a look."
    a "Oh wow. They're good."
    er "Look at this one. Haha."
    scene 08_2218 with Dissolve(1)
    er "Okay, you're hired!"
    mc "Hired? For what?"
    er "Every time we need some pictures taken. We're going to call you."
    mc "Uh..."
    er "Alright, deal!"
    mc "But..."
    mc "{i}(Stop pretending. I don't mind at all. Maybe Layla can join, too?){/i}"
    scene 08_2219 with Dissolve(1)
    er "*Whisper*"
    a "*Nods*"
    mc "{i}(What are they cooking up now?){/i}"
    scene 08_2220 with Dissolve(1)
    er "As a thank you, we'll also take a picture with you."
    mc "Uhm. Thanks?"
    scene 08_2221 with Dissolve(1)
    er "Ready!"
    er "Three! Two! One!"
    scene 08_2222 with Dissolve(1)
    mc "..."
    scene 08_2223 with Dissolve(1)
    er "Haha. That was fun."
    er "Lexi, can you take one of [mc] and me?"
    mc "{i}(I'm starting to feel like a prop.){/i}"
    mc "{i}(Please save me, Layla! How long can you brush your teeth for?){/i}"
    a "Sure."
    scene 08_2224 with Dissolve(1)
    er "Come on, get up. Let's recreate our picture where I carry you on my back. But this time, you carry me!"
    mc "Uhm..."
    mc "{i}(I can't get out of the water...){/i}"
    mc "Let's take one in the water for now. We can recreate that one when we're at Melissa's. At the same place."
    er "Oh yeah. Good idea."
    scene 08_2225 with Dissolve(1)
    mc "..."
    mc "{i}(I can feel her boobs pressing up against my back.){/i}"
    scene 08_2226 with Dissolve(1)
    er "Oh, this is cute. You have a nice smile."
    mc "Thanks. Yours isn't too shabby, either."
    er "Haha. Alright. Now you guys."
    a "We're good, right?"
    er "Come on. Just one."
    scene 08_2227 with Dissolve(1)
    er "By the way, [mc]. You're totally Lexi's type."
    a "Erynn!"
    er "What? When you described your type, you basically described [mc]."
    a "..."
    scene 08_2228 with Dissolve(1)
    a "Let's get this over with, or else she won't stop."
    a "And please forget what she just said."
    mc "{i}(That I'm your type?){/i}"
    scene 08_2229 with Dissolve(1)
    er "Act cuter."
    er "Here's an idea. Pretend you're in love with each other."
    mc "{i}(Is she playing cupid? Seems like she's trying to couple us up.){/i}"
    a "Erynn... Just take the picture."
    er "But that way, you can use the picture when you're getting hit on again in the bar by those idiots."
    er "You can say you have a boyfriend and show this as proof."
    a "*Sigh* Fine!"
    scene 08_2230 with vpunch
    a "..."
    mc "{i}(Oh fuck! She's touching my...){/i}"
    scene 08_2231 with Dissolve(1)
    a "*Whisper* Was that your... Are you naked?"
    mc "*Whisper* Uhm... Yeah? Sorry."
    a "*Whisper* That explains why I found Layla's bikini top earlier. Did you... Never mind. This never happened!"
    er "What are you guys whispering about?"
    a "*Whisper* Just don't hurt her!"
    mc "*Whisper* I won't."
    scene 08_2232 with Dissolve(1)
    er "That's perfect!"
    la "WHAT ARE YOU DOING?"
    scene 08_2233 with Dissolve(1)
    la "And why are you here?"
    a "We're taking pictures. I told you yesterday that Erynn will be coming over."
    la "..."
    la "I forgot."
    scene 08_2234 with Dissolve(1)
    er "Hey, Layla."
    la "Hey, Erynn."
    er "Why don't you join us?"
    la "Uhm... I..."
    scene 08_2235 with Dissolve(1)
    a "Looking for this?"
    la "ALEXIS!"
    scene black with Dissolve(1)
    pause 2
    scene 08_2236 with Dissolve(1)
    a "You and [mc]... Are you..."
    la "Not now! Hold the towel up, please."
    a "I am."
    scene 08_2237 with Dissolve(1)
    a "Just take your time. Don't rush into things just because..."
    la "I know, Lex."
    scene 08_2238 with Dissolve(1)
    la "Thanks."
    a "You're welcome. But why did you need the towel anyway?"
    a "You were topless before."
    la "..."
    la "If you want him to see boobs so badly..."
    scene 08_2239 with Dissolve(1)
    la "Why don't you show him yours?"
    a "Aaah!"
    mc "{i}(Hot damn...){/i}"
    scene 08_2240 with Dissolve(1)
    a "LAYLA!"
    la "Haha. That's what you get."
    scene black with Dissolve(1)
    pause 2
    scene 08_2241 with Dissolve(1)
    mc "Are they okay?"
    er "Oh yeah, don't worry."
    er "But just to be sure, I'll go check up on them."
    er "It'll also give you some time to look for your shorts!"
    mc "..."
    mc "{i}(How does she know?){/i}"
    scene 08_2174 with Dissolve(1)
    mc "{i}(Come on... They must be here somewhere...){/i}"
    mc "{i}(And since when did Erynn know? Did she see?){/i}"
    scene black with Dissolve(1)
    pause 2
    scene 08_2242 with Dissolve(1)
    la "I forgot that Erynn and Lexi would be here today."
    mc "It's okay."
    scene 08_2243 with Dissolve(1)
    la "Also, I'm sorry that I ruined our evening. But when I saw her with you, I got jealous and..."
    mc "No, I should've said no. I'm sorry."
    la "You guys were just taking pictures and having fun... I feel bad what I did to her though. I shouldn't have done that."
    mc "..."
    la "I'm happy you and Lexi get along, though."
    scene 08_2244 with Dissolve(1)
    la "You had fun today, right?"
    mc "It was great. You're great!"
    la "Thanks."
    mc "And we can be happy it was your sister and not your dad, for example, who was here."
    la "True, this would've gone a whole different way..."
    scene 08_2245 with Dissolve(1)
    la "Actually, I don't know. I've never had a boy over except last time, when you helped me study. So I have no idea how he'd react."
    mc "How did he react when Alexis brought someone over?"
    la "She never has."
    mc "Oh..."
    scene 08_2246 with Dissolve(1)
    mc "So, this would have been sort of an experiment?"
    la "Haha, you could say that."
    scene 08_2247 with Dissolve(1)
    mc "*Sigh* Anyway, I think I'd better leave. Let your sister and Erynn have the hot tub for today."
    la "You don't have to leave. We can still watch some TV."
    mc "We'll find plenty of time during spring break to hang out."
    la "*Nods*"
    scene 08_2248 with Dissolve(1)
    la "I'll show you out, then."
    mc "Thanks."
    scene black with Dissolve(1)
    pause 2
    scene 08_2249 with Dissolve(1)
    mc "Thank you for today. It was amazing."
    la "Hehe, you're welcome."
    la "See you tomorrow at school?"
    mc "Definitely."
    scene 08_2250 with Dissolve(1)
    ""
    scene 08_2251 with Dissolve(1)
    mc "Bye, Layla."
    la "Bye-bye."
    scene 08_2252 with Dissolve(1)
    er "You guys look really good together."
    a "*Sigh* Erynn..."
    a "I know what you are doing. He's with Layla."
    er "I know. Doesn't change the fact that you guys look cute. And that he's your type. Oh, and he was your first kiss!"
    a "..."
    scene 08_2253 with Dissolve(1)
    a "Can you send me the pictures we took today?"
    er "Of course."
    a "But not this one. Please delete it."
    er "You sure?"
    if Alexis_SP == 2:
        a "Yes!"
        scene black with Dissolve(2)
        pause 2
        scene 08_2254 with Dissolve(1)
        a "..."
        a "She's right."
        scene 08_2255 with Dissolve(1)
        a "Dammit, Erynn!"
    else:
        a "Yes!"
    $ renpy.end_replay()
    jump Week4_Wednesday

label Week4_Monday_Alexis_Meet:
    $ Alexis_Week4_Monday_Meet = True
    $ Alexis_Week3_Sunday_Meet = True
    $ Alexis_Week3_Sunday_NewBartender = True
    $ Iris_Week3_Sunday_Meet = True
    $ Alexis_Girlfriend = True
    scene black with Dissolve(1)
    pause 2
    stop music fadeout 1.0
    play music "Sounds/Bar_Background.mp3" volume 0.3
    scene 08_1814 with Dissolve(1)
    mc "{i}(That must be the new guy.){/i}"
    mc "{i}(Hmm... I don't see Alexis. Isn't she working today? Maybe I should've come yesterday.){/i}"
    scene 08_1815 with Dissolve(1)
    bt "Hey."
    mc "Hi."
    bt "What can I get you?"
    mc "Is Alexis working today?"
    bt "Yes, she's in the back doing inventory."
    scene 08_1816 with Dissolve(1)
    bt "Anything I can help you with?"
    mc "Can you tell her [mc] is here?"
    bt "Uh... Sure. Anything to drink?"
    mc "I'm good, thanks."
    scene black with Dissolve(1)
    pause 2
    scene 08_1817 with Dissolve(1)
    bt "Alexis?"
    a "Yes?"
    bt "Some guy's asking for you."
    scene 08_1818 with Dissolve(1)
    a "Some guy?"
    bt "Yeah, felt kinda weird. Do you want me to get rid of him?"
    a "No. Just tell him I'm busy."
    a "I want to finish this before my shift ends, anyway."
    bt "Will do."
    a "Thanks."
    scene black with Dissolve(1)
    pause 2
    scene 08_1819 with Dissolve(1)
    bt "I'm sorry, but she's busy at the moment."
    mc "Hmm... Okay."
    mc "{i}(Not even time for a hello?){/i}"
    mc "{i}(Guess I'll wait a while.){/i}"
    mc "Can I get an iced tea, please?"
    bt "Of course."
    scene black with Dissolve(1)
    pause 2
    n "An hour later."
    scene 08_1820 with Dissolve(1)
    a "*Sigh* Finally finished..."
    bt "Good job!"
    a "I hate doing inventory."
    bt "No one likes to do inventory."
    a "Yeah. That's why Dylan lets me do it."
    bt "Hehe. Have you seen the whiskey bottles, by any chance?"
    scene 08_1821 with Dissolve(1)
    a "Yeah, they're right here. I'll get them for you."
    bt "Thanks."
    bt "That guy from before is still here, by the way."
    a "Okay. This is getting weird. You know who he is?"
    bt "He told me his name. What was it again? [mc]?"
    scene 08_1822 with Dissolve(1)
    a "[mc]?"
    bt "Think so. Or something like that?"
    a "Oh my god..."
    scene black with Dissolve(1)
    pause 2
    scene 08_1823 with Dissolve(1)
    a "I'm so sorry, [mc]."
    mc "Hey, there you are. Busy?"
    a "I didn't know it was you, or else I would've come earlier. Sorry."
    mc "It's fine. I could've called before, but wanted to surprise you."
    mc "And I'm sorry I couldn't come yesterday!"
    a "You're here now. So it's all good."
    scene 08_1824 with Dissolve(1)
    bt "Oh, he's your boyfriend?"
    a "Uhm..."
    bt "I'm so sorry, I didn't know, or else I..."
    mc "It's all good, man."
    bt "Drinks are on me to make up for it, alright?"
    scene 08_1825 with Dissolve(1)
    a "You don't have to pay for him. He never pays here anyway."
    mc "I offered. It's not my fault others pay for me."
    scene 08_1826 with Dissolve(1)
    mc "You know what? When we go to a restaurant next time. It's on me, okay?"
    a "We'll probably go to Rue Madison and most likely you won't have to pay there either."
    mc "Haha, you got me. I feel like such a cheapskate... Free drinks, free food."
    scene 08_1827 with Dissolve(1)
    a "Cheapskate or not, I still like you!"
    mc "Thanks?"
    scene 08_1828 with Dissolve(1)
    a "Hmm?"
    mc "What?"
    a "You shaved!"
    mc "Yeah. Like it?"
    scene 08_1829 with Dissolve(1)
    a "No!"
    mc "Haha, ouch."
    a "I liked the stubble look better."
    mc "Give it a couple of days and it will be back."
    scene 08_1830 with Dissolve(1)
    a "Alright, see you in a couple of days, then."
    mc "Hey!"
    scene 08_1831 with Dissolve(1)
    mc "Where do you think you're going?"
    a "Haha."
    scene 08_1833 with Dissolve(1)
    if Layla_Week3_Tuesday_Train == False:
        a "No biting, okay?"
        mc "Look who's talking."
        a "At least not in public!"
    else:
        a "That tickles!"
    scene 08_1832 with Dissolve(1)
    a "Missed you!"
    mc "Missed you, too."
    a "And thank you for calling me every day."
    mc "All but one."
    a "Right. The 'Oh shit Alexis' day."
    mc "Haha, sorry!"
    a "You're forgiven."
    scene 08_1834 with Dissolve(1)
    mc "When does your shift end?"
    a "Just now."
    mc "Perfect. Let's head out, then."
    scene black with Dissolve(1)
    pause 2
    stop music fadeout 1.0
    play music ("Music/LoFi Upbeat 1.mp3", "Music/LoFi Upbeat 2.mp3", "Music/LoFi Upbeat 3.mp3", "Music/LoFi Upbeat 4.mp3") volume 0.2
    if Zach_Week3_Wednesday_TC_Girlshower == True:
        $ Alexis_Points -= 4
        scene 08_1835 with Dissolve(1)
        mc "What do you want to do today?"
        a "How about we play truth or dare."
        mc "..."
        mc "{i}(Fuck! She knows. Of course she knows, they're sisters.){/i}"
        if Layla_Week3_Wednesday_TC_Alexis_DateBoth == False:
            mc "Layla told you?"
            a "She did, but she also said you guys made up already."
        else:
            mc "{i}(But it seems that's the only thing Layla told her. If she told Alexis we hooked up at training camp, I wouldn't be talking to her right now.){/i}"
            mc "Layla told you about that?"
            a "She did..."
        scene 08_1835 with Dissolve(1)
        a "I'll forgive you too, but don't you ever do that again!"
        mc "I won't. I've learned my lesson. Sorry, Lexi."
        scene 08_1849 with Dissolve(1)
        a "Let's forget about all of that and have fun today."
        mc "{i}(I'm so happy all of them are so forgiving. This could've easily been the end of our relationships.){/i}"
        mc "Thank you."
        scene 08_1850 with Dissolve(1)
        mc "Alright. Truth or dare?"
        a "What?"
        mc "You said you wanted to play. So pick!"
        a "Dare."
        mc "Right off the bat?"
        a "Uh-huh."
        mc "No wonder I like you. So brave."
    else:
        scene 08_1844 with Dissolve(1)
        mc "What do you want to do today?"
        a "Hmm... How about we play truth or dare?"
        mc "Heh, okay. What's Layla told you?"
        scene 08_1845 with Dissolve(1)
        a "Nothing..."
        a "Only that you guys had lots of fun."
        a "And that you like wearing other people's underwear."
        scene 08_1846 with Dissolve(1)
        mc "I knew it! That little..."
        a "Haha."
        mc "I bet the whole school knows already."
        mc "Now I'll have to switch schools again. Third time this year."
        scene 08_1847 with Dissolve(1)
        a "You can come to my school."
        mc "I probably will next year."
        a "Yeah? I'd love that. Maybe we'll have some classes together, then."
        scene 08_1848 with Dissolve(1)
        mc "Who knows. But I hope not."
        a "Why not?"
        mc "Because I won't be able to concentrate..."
        scene 08_1849 with Dissolve(1)
        a "Don't worry. I'll tutor you after class."
        mc "What class would that be?"
        a "Advanced Chemistry."
        mc "Haha, I see what you did there. Nice."
        mc "How about some biology?"
        a "That will be today's lesson."
        mc "Oh..."
        scene 08_1850 with Dissolve(1)
        mc "By the way. Truth or dare?"
        a "What?"
        mc "You said you wanted to play. So pick!"
        a "Dare."
        mc "Right off the bat?"
        a "Uh-huh."
        mc "No wonder I like you. So brave."
    scene 08_1851 with Dissolve(1)
    a "Haha."
    mc "..."
    mc "Did she tell you that too? Come on."
    scene black with Dissolve(2)
    pause 2
    scene 08_1853 with Dissolve(1)
    mc "So dare, huh?"
    mc "Here's a nice one to start with..."
    if Alexis_Week3_Sunday_BubbleIce == False:
        scene 08_1854 with Dissolve(1)
        mc "I dare you to sing your favourite song. Right here, right now."
        a "What? Here? No!"
        a "No-no-no..."
        scene 08_1855 with Dissolve(1)
        a "Please pick another dare, [mc]!"
        a "I can't do that one."
        a "Please?"
        scene 08_1857 with Dissolve(1)
        mc "Why not? You're a really good singer, Lexi."
        a "No... Just give me another dare. This one doesn't count."
        mc "Alright."
    else:
        scene 08_1854 with Dissolve(1)
        mc "I dare you to eat bubblegum ice cream!"
        a "What? No!"
        a "No-no-no..."
        scene 08_1855 with Dissolve(1)
        a "Please pick another dare, [mc]!"
        a "I can't do that one."
        a "Please?"
        scene 08_1856 with Dissolve(1)
        mc "Haha. What's your deal with bubblegum ice cream?"
        a "Have you tasted it?"
        mc "No."
        a "Well, it does NOT work in ice cream. What are you supposed to do with the pieces of bubble gum? Chew them while your ice cream melts?"
        a "Swallow them or spit them out? It's all wrong. Just no!"
        scene 08_1857 with Dissolve(1)
        mc "Fine, you'll get your punishment later."
        a "No... Just give me another dare. This one doesn't count."
        mc "Alright."
    scene 08_1858 with Dissolve(1)
    mc "You're going to hate this one even more!"
    mc "I dare you to be my girlfriend!"
    a "..."
    mc "What? Not doing this one either?"
    scene 08_1859 with Dissolve(1)
    mc "It's no fun playing with you."
    a "..."
    scene 08_1860 with Dissolve(1)
    a "Wait! [mc]!"
    a "I'll do the dare."
    scene 08_1861 with Dissolve(1)
    a "I will do the dare!"
    mc "Good."
    scene 08_1862 with vpunch
    mc "Hey! Careful."
    a "My turn. I dare you to ask me again!"
    mc "Who says I'll pick dare? Maybe I'll go for truth?"
    a "Please pick dare."
    mc "Hehe."
    scene 08_1863 with Dissolve(1)
    a "Ask me again!"
    mc "Alexis Monroe. Do you want to be my girlfriend?"
    a "Yes! I want to be your girlfriend!"
    scene 08_1864 with Dissolve(1)
    ""
    scene 08_1865 with Dissolve(1)
    x "Get a room!"
    x "Not everyone wants to see your PDA!"
    scene 08_1866 with Dissolve(1)
    mc "What's her problem?"
    a "Maybe no one dared her to be someone's girlfriend?"
    mc "Haha. That must be it."
    scene 08_1867 with Dissolve(1)
    a "But she's right though."
    a "We should get a room. How about my place?"
    if Layla_Week3_Tuesday_Train == True:
        mc "Uh-huh."
    else:
        scene 08_1868 with Dissolve(1)
        mc "Did you clean your room this time? Uhm, I mean, your roommate isn't there today?"
        a "I really have a roommate, okay? She was there last time. Naked! That's why I didn't let you in."
        scene 08_1869 with Dissolve(1)
        mc "I wouldn't have minded."
        a "..."
        mc "Kidding?"
        a "Uh-huh..."
    jump Week3_Sunday_Alexis_Dorm

label Week4_Wednesday:
    scene black with Dissolve(2)
    pause 2
    stop music fadeout 1.0
    play music ("Music/LoFi Indie 3.mp3", "Music/LoFi Indie 1.mp3", "Music/LoFi Indie 2.mp3") volume 0.2
    n "Wednesday, 17:26."
    if Emily_Week3_Sunday_Surprise == True:
        scene 08_2256 with Dissolve(1)
        mc "Can you tell me now where we're going?"
        m "No! It's a surprise."
        mc "A hint then?"
        m "It's in the city."
        scene 08_2257 with Dissolve(1)
        mc "*Sigh*"
        m "What?"
        mc "Nothing."
        m "Since when are you so impatient? Let me surprise you for once!"
        scene black with Dissolve(1)
        pause 2
        scene 08_2258 with Dissolve(1)
        mc "{i}(A garage. A lot with cars...){/i}"
        mc "{i}(Wait... Is she buying me a car?){/i}"
        scene 08_2259 with Dissolve(1)
        mc "MOM!"
        m "What's up with you all of a sudden?"
        mc "Is this the surprise? Are you buying me a car?"
        scene 08_2260 with Dissolve(1)
        m "Hmm? What makes you think I'd buy you a car?"
        mc "Well, the..."
        mc "Never mind."
        scene 08_2261 with Dissolve(1)
        m "Come on."
        mc "{i}(Why did we park here then?){/i}"
        mc "That's just mean, you know?"
        scene 08_2262 with Dissolve(1)
        m "Haha. I'm kidding. Let's have a look around."
        mc "Are you being serious?"
        m "Yes!"
        scene 08_2263 with Dissolve(1)
        m "This will be your birthday present."
        mc "Thank you, thank you, thank you!"
        scene black with Dissolve(1)
        pause 2
        scene 08_2264 with Dissolve(1)
        m "How about this one here? It looks sporty, no?"
        mc "That's not bad. Yeah, maybe. Nikki has the same one."
        m "Nikki from Riverside?"
        mc "Yes."
        scene 08_2265 with Dissolve(1)
        m "How is she? Have you spoken to her or Cara lately?"
        mc "No. We aren't really in contact."
        m "Why not?"
        mc "I don't know... That's just how things go sometimes."
        m "Shame."
        scene 08_2266 with Dissolve(1)
        mc "Oh... I really like this one. It'd be perfect for the summer."
        m "Uh-huh. Keep on moving."
        mc "Haha. A bit over budget, maybe."
        m "A bit..."
        scene 08_2267 with Dissolve(1)
        mc "Wouldn't that be something for you?"
        m "Not really. I can get so much more stuff in my car."
        scene 08_2268 with Dissolve(1)
        mc "How about this one then? The new ranger?"
        m "Hmm, I like it, but we're here for you, not me."
        mc "But if you buy a new one, I'll just take the old."
        n "*Bzzzt. Bzzzt*"
        m "One second."
        scene 08_2269 with Dissolve(1)
        m "*Sigh* Yes, Connor?"
        m "..."
        m "No, I can't come to the restaurant now. What's the matter?"
        m "..."
        scene 08_2270 with Dissolve(1)
        m "I'm sorry, honey. Can you give me a minute?"
        mc "Sure. I'll look around some more."
        m "Thank you."
    else:
        scene 08_2271 with Dissolve(1)
        z "This is the place."
        z "They have a lot more cars on the other side of the garage."
        z "You'll probably find something you like, too."
        scene 08_2272 with Dissolve(1)
        z "And this is her! What do you think? Isn't she a beaut?"
        mc "Yeah, it's one hell of a machine."
        mc "Didn't expect you to be into muscle cars."
        scene 08_2273 with Dissolve(1)
        z "What do you mean? Just look at me."
        z "If I was a car. This would literally be me."
        mc "Maybe yeah. At least the colour's correct."
        z "Huh?"
        mc "Never mind."
        scene 08_2274 with Dissolve(1)
        z "Man, I can't wait. It's gonna be so AWESOME!"
        z "I even have a name."
        z "The ZACH-ATTACK! Girls are gonna love this!"
        mc "{i}(Don't facepalm. Don't say anything. Let him do his thing...){/i}"
        mc "{i}(No one saw or heard this, right?){/i}"
        scene 08_2275 with Dissolve(1)
        z "Should I put a decal on the hood with Zach-Attack surrounded by flames and stuff?"
        mc "{i}(NO!){/i}"
        mc "Sure... Go for it."
        z "Such a good idea, right? Just imagine it. Zach-Attack!"
        scene 08_2276 with Dissolve(1)
        mc "How does she drive?"
        z "I don't know."
        mc "You haven't test-driven it yet?"
        z "No, not yet. I was about to do that today."
        mc "Alright. You go get someone and test drive it. I'll have a look around."
        z "Sounds good."
    scene black with Dissolve(1)
    pause 2
    scene 08_2277 with Dissolve(1)
    mc "{i}(That's also sweet looking.){/i}"
    mc "{i}(Nathan would love this car.){/i}"
    x "Hey John, can you hand me the wrench?"
    mc "{i}(No John around.){/i}"
    scene 08_2278 with Dissolve(1)
    mc "Here you go!"
    x "Thanks."
    x "..."
    if Alexis_Week3_Sunday_NewBartender == True:
        scene 08_2279 with Dissolve(1)
        bt "Hey. Can I help you?"
        mc "Hi. I was just looking at some cars here."
        bt "Oh. If you need anything, let me know."
        mc "Thanks."
        scene 08_2280 with Dissolve(1)
        mc "Aren't you the new bartender at Dylan's?"
        bt "And you're Alexis's boyfriend."
        mc "You work here, too?"
        bt "Yeah, this is my main job. I only work part-time at the bar."
        scene 08_2281 with Dissolve(1)
        bt "Let me apologise again for last time. I was being a dick."
        mc "It's cool."
        bt "I was just trying to look out for Alexis."
        mc "Did something happen?"
        scene 08_2282 with Dissolve(1)
        bt "Some idiots kept hitting on her. It really pissed her off and..."
        mc "When was that?"
        bt "Friday night."
        mc "Hmm."
        mc "{i}(She hasn't said anything about that.){/i}"
        scene 08_2283 with Dissolve(1)
        mc "Does that happen a lot?"
        bt "I just started a few days ago. But she gets lots of attention, yes."
        bt "She's a pretty girl."
        mc "Yeah, she is. And thanks."
        bt "Sure."
        scene 08_2284 with Dissolve(1)
        mc "By the way. Nice car."
        bt "Thanks. It was at some point. At the moment, it's just scrap."
        bt "Will take me a few weeks to get it running again."
        scene 08_2285 with Dissolve(1)
        mc "Then I'll leave you to it. I'll go look at some more cars."
        bt "If you need some help, you know where to find me."
        mc "Thanks."
    else:
        scene 08_2279 with Dissolve(1)
        x "Hey. Can I help you?"
        mc "Hi. I was just looking at some cars here."
        x "Oh. If you need anything, let me know."
        mc "Thanks."
    scene black with Dissolve(1)
    pause 2
    scene 08_2286 with Dissolve(1)
    mc "{i}(Guess I'll take a look at the bikes too.){/i}"
    mc "{i}(Would Mom agree to get me a bike instead of a car? Probably not!){/i}"
    scene 08_2287 with Dissolve(1)
    mc "{i}(Oh man...){/i}"
    mc "{i}(This is it!){/i}"
    if Andres_FB_Punch == True:
        jump Week4_Wednesday_Garage_Iris1
    else:
        if Iris_Week3_Sunday_Meet == True:
            jump Week4_Wednesday_Garage_Iris2
        else:
            jump Week4_Wednesday_Garage_Iris3

label Week4_Wednesday_Garage_Iris1:
    if Iris_Week3_Sunday_Meet == True:
        scene 08_2288 with Dissolve(1)
        x "Still into bikes, huh?"
        mc "..."
        scene black with Dissolve(1)
        transform moveup:
            xalign 0.5 yalign 1.0
            linear 5.0 yalign 0.0
        show 08_2289 at moveup
        pause 3
        mc "Iris!"
        ir "Hey, [mc]. We meet again."
        mc "What are you doing here?"
        ir "What are you doing here? That's how you greet me?"
        ir "Don't just stand there. Hug me!"
        scene 08_2340 with Dissolve(1)
        mc "Haha, I'm sorry, Iris."
        mc "It's nice to see you. How are you?"
        ir "Really good. How about you?"
        mc "I'm good."
        scene 08_2296 with Dissolve(1)
        mc "Wow, I couldn't believe my eyes when I saw you at Lexi's. You of all people."
        mc "I never thought we'd see each other again."
        ir "You and me both."
        scene 08_2290 with Dissolve(1)
        ir "Let me apologise for that, first. I didn't want to ruin your night with Alexis."
        mc "It's okay. It was a little weird though. You sitting there and watching us..."
        ir "I'm a weirdo, you know that."
        mc "Haha."
        scene 08_2291 with Dissolve(1)
        ir "I knew she was dating someone, but she wouldn't tell me anything."
        ir "When I came home and heard you guys, I got very curious."
        ir "I only wanted a quick peek, but once I saw that it was you... I don't know... I stayed."
        scene 08_2292 with Dissolve(1)
        ir "It was really hot! Got a little jealous, too. I was this close to joining you."
        mc "Haha."
        mc "I think we wouldn't be talking now if you had."
        ir "Haha. If looks could kill, I'd be buried already. She was so mad when you left."
        scene 08_2293 with Dissolve(1)
        mc "Is she still mad at you?"
        ir "No. We hashed it out. We're roommates. It would be very awkward if we fought for a longer period."
        mc "{i}(Tell that to Erynn and Alexis!){/i}"
        scene 08_2341 with Dissolve(1)
        mc "Anyway. You've cut your hair."
        mc "And not just a little. It's really short now."
        ir "It was time for something new. Makes me look cute though, right?"
        menu:
            "No":
                scene 08_2342 with Dissolve(1)
                mc "Eh..."
                ir "Just say yes to make me happy! It was a big decision."
                mc "Haha."
            "Yes[KoGa3AutoWTChange1]{size=-4}(Iris Points+2) {/size} {/color}":
                $ Iris_Points += 2
                # Iris (2)
                scene 08_2343 with Dissolve(1)
                mc "It suits you. I like it."
                ir "Thanks."
        scene 08_2344 with Dissolve(1)
        ir "By the way, I'm looking at you, and you've changed too. More muscles and... tattoos!"
        ir "Are you copying Dad?"
        mc "Haha. Maybe he influenced me a bit."
        ir "As you know, I've always been a daddy's girl. Looks good on you."
        scene 08_2345 with Dissolve(1)
        mc "How is John?"
        ir "He's good. I think he misses you sometimes."
        mc "Me?"
        ir "Yeah. You were my first boyfriend he actually liked."
        mc "Heh."
        scene 08_2346 with Dissolve(1)
        ir "You'll probably see him later. He's out giving someone a test drive. This is his garage."
        mc "Really? That explains why you're in Madison Springs, then."
        mc "Weren't you moving to Novasota?"
        ir "We did. We were there a week before Dad got the offer to buy this garage."
        scene 08_2347 with Dissolve(1)
        mc "Haha."
        ir "What's so funny?"
        mc "It's just that we're living in the same city again."
        ir "When you did guys move here?"
        mc "About a month ago, almost. But only me. I'm living with my mom again."
        scene 08_2348 with Dissolve(1)
        ir "What about your dad?"
        mc "Which one?"
        ir "What do you mean? Okay, tell me..."
        scene black with Dissolve(1)
        pause 2
        scene 08_2349 with Dissolve(1)
        ir "Now I'm speechless... And that never happens. Holy shit!"
        mc "Exactly."
        ir "I'm so sorry."
        scene 08_2350 with Dissolve(1)
        ir "But you're okay, right?"
        mc "Yeah, don't worry."
        ir "Good."
        scene 08_2345 with Dissolve(1)
        ir "Well, tell me more. I want to know everything, now."
        ir "Let's start with you dating Alexis. How's that going?"
        mc "Really good. I like her a lot."
        ir "She likes you too. Heaps. I can tell."
        scene 08_2353 with Dissolve(1)
        mc "How about you? Are you seeing someone?"
        ir "There's someone I'm interested in."
        mc "Oh... Boy or girl?"
        ir "..."
        scene 08_2354 with Dissolve(1)
        mc "So, girl!"
        ir "Yeah. She's best friends with Alexis."
        ir "Absolutely gorgeous. You'd probably like her, too."
        mc "{i}(Alexis's best friend? Does she mean Erynn?){/i}"
        scene 08_2355 with Dissolve(1)
        ir "When I first met her, I felt this... like... immediate bond, I can't explain it. Do you know what I mean?"
        mc "Can't say for sure, but I'm a little jealous, now."
        ir "Don't be. I felt the same with you, which makes this even more weird."
        scene 08_2356 with Dissolve(1)
        mc "You're dating her, or...?"
        ir "*Sigh* No. I've only talked to her a few times. I don't even know if she's into girls or not."
        mc "That's very easy to figure out."
        ir "Yeah? How?"
        scene 08_2357 with Dissolve(1)
        mc "Ask her!"
        ir "..."
        scene 08_2295 with Dissolve(1)
        mc "By the way. Could it be you're talking about Erynn?"
        ir "Uhm, yeah... How do you know Erynn? Oh, maybe because of Alexis?"
        scene 08_2296 with Dissolve(1)
        ir "You need to tell me all about her. What does she like? Is she into girls?"
        mc "Uhm..."
        ir "No wait, I have a better idea."
        ir "Double date!"
        scene 08_2297 with Dissolve(1)
        mc "That'd be a little complicated."
        ir "How so?"
        mc "I don't know if I should tell you this, but Alexis and Erynn aren't on speaking terms at the moment."
        ir "What? Why?"
        mc "{i}(Well...){/i}"
        ir "But that explains why she hasn't come over in a while. I thought she was busy..."
        ir "They need to talk and make up already! I want this double date!"
        mc "Agreed. On the making up part. Not the double date."
        ir "No, no. It's already in the works."
        if Emily_Week3_Sunday_Surprise == True:
            jump Week4_Wednesday_Garage_Emily
        else:
            jump Week4_Wednesday_Garage_Zach
    else:
        scene 08_2288 with Dissolve(1)
        x "Still into bikes, huh?"
        mc "..."
        scene black with Dissolve(1)
        transform moveup:
            xalign 0.5 yalign 1.0
            linear 5.0 yalign 0.0
        show 08_2289 at moveup
        pause 3
        mc "Iris!"
        mc "What are you doing here?"
        ir "What are you doing here? That's how you greet me?"
        ir "Don't just stand there. Hug me!"
        scene 08_2340 with Dissolve(1)
        mc "Haha, I'm sorry, Iris."
        mc "It's nice to see you. How are you?"
        ir "Really good. How about you?"
        mc "I'm good."
        scene 08_2296 with Dissolve(1)
        mc "Wow, haha... I'm kinda speechless. You of all people."
        mc "I never thought we'd see each other again."
        ir "You and me both."
        scene 08_2341 with Dissolve(1)
        mc "You've cut your hair."
        mc "And not just a little. It's really short now."
        ir "It was time for something new. Makes me look cute though, right?"
        menu:
            "No":
                scene 08_2342 with Dissolve(1)
                mc "Eh..."
                ir "Just say yes to make me happy! It was a big decision."
                mc "Haha."
            "Yes[KoGa3AutoWTChange1]{size=-4}(Iris Points+2) {/size} {/color}":
                $ Iris_Points += 2
                # Iris (2)
                scene 08_2343 with Dissolve(1)
                mc "It suits you. I like it."
                ir "Thanks."
        scene 08_2344 with Dissolve(1)
        ir "By the way, I'm looking at you, and you've changed too. More muscles and... tattoos!"
        ir "Are you copying Dad?"
        mc "Haha. Maybe he influenced me a bit."
        ir "As you know, I've always been a daddy's girl. Looks good on you."
        scene 08_2345 with Dissolve(1)
        mc "How is John?"
        ir "He's good. I think he misses you sometimes."
        mc "Me?"
        ir "Yeah. You were my first boyfriend he actually liked."
        mc "Heh."
        scene 08_2346 with Dissolve(1)
        ir "You'll probably see him later. He's out giving someone a test drive. This is his garage."
        mc "Really? That explains why you're in Madison Springs, then."
        mc "Weren't you moving to Novasota?"
        ir "We did. We were there a week before Dad got the offer to buy this garage."
        scene 08_2347 with Dissolve(1)
        mc "Haha."
        ir "What's so funny?"
        mc "I live in Madison Springs, too. We're living in the same city again."
        ir "What? No! Really? You guys moved here as well?"
        mc "About a month ago, almost. But only me. I'm living with my mom again."
        scene 08_2348 with Dissolve(1)
        ir "What about your dad?"
        mc "Which one?"
        ir "What do you mean? Okay, tell me..."
        scene black with Dissolve(1)
        pause 2
        scene 08_2349 with Dissolve(1)
        ir "Now I'm speechless... And that never happens. Holy shit!"
        mc "Exactly."
        ir "I'm so sorry."
        scene 08_2350 with Dissolve(1)
        ir "But you're okay, right?"
        mc "Yeah, don't worry."
        ir "Good."
        scene 08_2345 with Dissolve(1)
        ir "Well, tell me more. I want to know everything now."
        ir "Are you dating anyone?"
        if Alexis_Dating == False:
            scene 08_2351 with Dissolve(1)
            mc "Sort of..."
            ir "Sort of? What kind of answer is that? Tell me!"
            mc "..."
            mc "I'm still figuring it out myself."
            ir "Heh. I'll find out sooner or later."
        else:
            scene 08_2351a with Dissolve(1)
            mc "I'm dating this girl, Alexis."
            ir "Alexis? My roommate's name is also Alexis."
            mc "Monroe?"
            ir "No way! You're dating my roommate! Now I know why she's been so happy lately."
            ir "Small world..."
            scene 08_2352 with Dissolve(1)
            ir "How's that going?"
            mc "Good. I like her a lot."
            ir "She likes you too. Heaps. I can tell."
        scene 08_2353 with Dissolve(1)
        mc "How about you? Are you seeing someone?"
        ir "There's someone I'm interested in."
        mc "Oh... Boy or girl?"
        ir "..."
        if Alexis_Dating == True:
            scene 08_2354 with Dissolve(1)
            mc "So, girl!"
            ir "Yeah. She's actually best friends with Alexis."
            ir "Absolutely gorgeous. You'd probably like her, too."
            mc "{i}(Alexis's best friend? Does she mean Erynn?){/i}"
        else:
            scene 08_2354 with Dissolve(1)
            mc "So, girl!"
            ir "Yeah. She's best friends with my roommate, Alexis."
            mc "{i}(Alexis...){/i}"
            ir "Absolutely gorgeous. You'd probably like her too."
            mc "{i}(Alexis's best friend? Does she mean Erynn?){/i}"
        scene 08_2355 with Dissolve(1)
        ir "When I first met her, I felt this... like... immediate bond, I can't explain it. Do you know what I mean?"
        mc "Can't say for sure, but I'm a little jealous, now."
        ir "Don't be. I felt the same with you, which makes this even more weird."
        scene 08_2356 with Dissolve(1)
        mc "You're dating her, or...?"
        ir "*Sigh* No. I've only talked to her a few times. I don't even know if she's into girls or not."
        mc "That's very easy to figure out."
        ir "Yeah? How?"
        scene 08_2357 with Dissolve(1)
        mc "Ask her!"
        ir "..."
        if Alexis_Dating == True:
            scene 08_2295 with Dissolve(1)
            mc "By the way. Could it be you're talking about Erynn?"
            ir "Uhm, yeah... How do you know Erynn? Oh, maybe because of Alexis?"
            scene 08_2296 with Dissolve(1)
            ir "You need to tell me all about her. What does she like? Is she into girls?"
            mc "Uhm..."
            ir "No wait, I have a better idea."
            ir "Double date!"
            scene 08_2297 with Dissolve(1)
            mc "That'd be a little complicated."
            ir "How so?"
            mc "I don't know if I should tell you this, but Alexis and Erynn aren't on speaking terms at the moment."
            ir "What? Why?"
            mc "{i}(Well...){/i}"
            ir "But that explains why she hasn't come over in a while. I thought she was busy..."
            ir "They need to talk and make up already! I want this double date!"
            mc "Agreed. On the making up part. Not the double date."
            ir "No, no. It's already in the works."
        else:
            scene 08_2295 with Dissolve(1)
            mc "By the way. Could it be you're talking about Erynn?"
            ir "Uhm, yeah... How do you know Erynn?"
            if Erynn_End == True:
                mc "I know her from back in the day. But we aren't really friends."
                ir "Too bad. You could've told me everything about her."
            else:
                mc "We've been friends since we were little."
                scene 08_2296 with Dissolve(1)
                ir "Really? You need to tell me all about her, then. What does she like? Is she into girls?"
                mc "Uhm..."
                ir "No wait, I have a better idea."
                ir "Double date!"
                mc "Heh."
        if Emily_Week3_Sunday_Surprise == True:
            jump Week4_Wednesday_Garage_Emily
        else:
            jump Week4_Wednesday_Garage_Zach

label Week4_Wednesday_Garage_Iris2:
    scene 08_2288 with Dissolve(1)
    x "Still into bikes, huh?"
    mc "..."
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 08_2289 at moveup
    pause 3
    mc "Iris!"
    ir "Hey, [mc]. Third time in a week. You still want to talk about coincidences? It feels like we're still dating."
    mc "Hi. It's starting to feel like that. Uhm... What are you doing here?"
    ir "I told you Dad owns a garage."
    scene 08_2290 with Dissolve(1)
    ir "But first, let me apologise. I didn't want to ruin your night with Alexis."
    mc "It's okay. It was a little weird though. You sitting there and watching us..."
    ir "I'm a weirdo, you know that."
    mc "Haha."
    scene 08_2291 with Dissolve(1)
    ir "I knew she was dating someone, but she wouldn't tell me anything."
    ir "When I came home and heard you guys, I got very curious."
    ir "I only wanted a quick peek, but once I saw that it was you... I don't know... I stayed."
    scene 08_2292 with Dissolve(1)
    ir "It was really hot! Got a little jealous too. I was this close to joining you."
    mc "Haha."
    mc "I think we wouldn't be talking now if you had."
    ir "Haha. If looks could kill, I'd be buried already. She was so mad when you left."
    scene 08_2293 with Dissolve(1)
    mc "Is she still mad at you?"
    ir "No. We hashed it out. We're roommates. It would be very awkward if we fought for a longer period."
    mc "{i}(Tell that to Erynn and Alexis!){/i}"
    mc "{i}(Speaking about Erynn...){/i}"
    scene 08_2294 with Dissolve(1)
    mc "Hey, on the plane, you told me you have a crush on Alexis's best friend, right?"
    ir "Correct."
    mc "That best friend, could it be Erynn?"
    scene 08_2295 with Dissolve(1)
    ir "You know Erynn?"
    mc "She's a friend of mine."
    ir "No way!"
    scene 08_2296 with Dissolve(1)
    ir "Okay, you need to tell me all about her. What does she like? Is she into girls?"
    mc "Uhm..."
    ir "No wait, I have a better idea."
    ir "The double date I mentioned!"
    scene 08_2297 with Dissolve(1)
    mc "That'd be a little complicated."
    ir "How so?"
    mc "I don't know if I should tell you this, but Alexis and Erynn aren't on speaking terms at the moment."
    ir "What? Why?"
    mc "{i}(Well...){/i}"
    ir "But that explains why she hasn't come over in a while. I thought she was busy..."
    ir "They need to talk and make up already! I want this double date!"
    mc "Agreed. On the making up part. Not the double date."
    ir "No, no. It's already in the works."
    if Emily_Week3_Sunday_Surprise == True:
        jump Week4_Wednesday_Garage_Emily
    else:
        jump Week4_Wednesday_Garage_Zach

label Week4_Wednesday_Garage_Iris3:
    scene 08_2288 with Dissolve(1)
    x "Still into bikes, huh?"
    mc "..."
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 08_2289 at moveup
    pause 3
    mc "Iris!"
    ir "Hey [mc]. We meet again."
    scene black with Dissolve(2)
    pause 2
    stop music fadeout 1.0
    play music "Sounds/Aeroplane_Onboard.mp3" volume 0.3
    n "A week ago."
    scene 06_920 with Dissolve(1)
    mc "..."
    ir "Oh my god... [mc]!"
    mc "Hey. What are you doing here?"
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 08_1922 at moveup
    pause 3
    ir "What are you doing here? That's how you greet me?"
    scene 08_1923 with Dissolve(1)
    mc "Haha, I'm sorry, Iris."
    mc "It's nice to see you. How are you?"
    ir "Really good. How about you?"
    mc "So-so."
    ir "Hmm..."
    scene 08_1924 with Dissolve(1)
    mc "Wow, haha... I'm kinda speechless. You of all people."
    mc "I never thought we'd see each other again."
    ir "You and me both."
    scene 08_1925 with Dissolve(1)
    mc "And this is your seat?"
    ir "Uh-huh."
    mc "What a coincidence."
    ir "Tell me about it."
    scene 08_1926 with Dissolve(1)
    mc "I almost didn't recognise you. You've cut your hair."
    mc "And not just a little. It's really short now."
    ir "It was time for something new. Makes me look cute though, right?"
    menu:
        "No":
            scene 08_1927 with Dissolve(1)
            mc "Eh..."
            ir "Just say yes to make me happy! It was a big decision."
            mc "Haha."
        "Yes[KoGa3AutoWTChange1]{size=-4}(Iris Points+2) {/size} {/color}":
            $ Iris_Points += 2
            # Iris (2)
            scene 08_1928 with Dissolve(1)
            mc "It suits you. I like it."
            ir "Thanks."
    x "Uhm, excuse me miss. I think you're sitting in my seat."
    scene 08_1929 with Dissolve(1)
    ir "I know. I'm so sorry."
    ir "Look. The plane was almost completely booked when we got our tickets and there wasn't a row left with two empty seats."
    ir "And I really need to sit next to my boyfriend here because I'm terrified of flying."
    ir "Could we maybe swap seats? You would be doing me a huge favour!"
    scene 08_1930 with Dissolve(1)
    x "Uhm... I don't..."
    ir "Please..."
    x "*Sigh*"
    scene 08_1931 with Dissolve(1)
    ir "Thank you so much. I knew there were still gentlemen in this world."
    ir "My seat is C12. Bye."
    scene 08_1932 with Dissolve(1)
    mc "Coincidence..."
    ir "Haha."
    mc "Can't believe you get away with stuff like that. Every time..."
    ir "I'm charming."
    mc "Uh-huh. I actually think you didn't like the person you had to sit next to, so you were looking for another seat and here we are."
    scene 08_1933 with Dissolve(1)
    ir "Haha. You caught me!"
    mc "Yep. I know you."
    ir "You sure do."
    scene 08_1934 with Dissolve(1)
    ir "But if I didn't do that, we probably wouldn't have met again."
    mc "Also true."
    ir "And you'd probably rather sit next to me anyway."
    mc "Yeah, you're much nicer to look at."
    scene 08_1935 with Dissolve(1)
    if Alexis_Dating == False:
        ir "And look at you, though! You've changed too. More muscles... And tattoos!"
    else:
        ir "And look at you, though! You've changed too. More muscles... And tattoos!"
        mc "{i}(This feels a bit like deja-vu.){/i}"
    ir "Are you copying my dad?"
    mc "Haha. Maybe he influenced me a bit."
    ir "As you know, I've always been a daddy's girl. Looks good on you."
    scene 08_1936 with Dissolve(1)
    mc "How is John?"
    ir "He's good. I think he misses you sometimes."
    mc "Me?"
    ir "Yeah. You were my first boyfriend he actually liked."
    mc "Heh."
    scene 08_1937 with Dissolve(1)
    ir "He owns a garage now in Madison Springs."
    mc "Madison Springs?"
    ir "Yeah."
    mc "Weren't you moving to Novasota?"
    ir "We did. We were there a week before Dad got the offer. And I'm so glad for that."
    ir "Novasota is a shit hole. Madison Springs has beaches, a university, a big shopping district, good clubs. Heavenly."
    scene 08_1938 with Dissolve(1)
    mc "Haha."
    ir "What's so funny?"
    mc "I live in Madison Springs, too."
    ir "What? No! Really? You guys moved there as well?"
    mc "Only me. I'm living with my mom again."
    scene 08_1939 with Dissolve(1)
    ir "What about your dad?"
    mc "Which one?"
    ir "Okay, tell me..."
    scene black with Dissolve(1)
    pause 2
    scene 08_1940 with Dissolve(1)
    ir "Wow... I'm speechless... And that never happens. Holy shit!"
    mc "Exactly."
    ir "I'm so sorry."
    scene 08_1941 with Dissolve(1)
    ir "But you're okay, right?"
    mc "Yeah, don't worry."
    ir "What else happened? I want to know everything now!"
    mc "Well..."
    scene black with Dissolve(2)
    pause 2
    n "A few hours later."
    scene 08_1933 with Dissolve(1)
    ir "Haha, that's so typical."
    mc "You would've done the same thing."
    ir "Probably."
    scene 08_1942 with Dissolve(1)
    ir "Hey, [mc]?"
    mc "Hmm?"
    ir "Are you dating anyone?"
    if Alexis_Dating == False:
        scene 08_1943 with Dissolve(1)
        mc "Sort of..."
        ir "Sort of? What kind of answer is that? Tell me!"
        mc "..."
        mc "I'm still figuring it out myself."
        ir "Heh. I'll find out sooner or later."
    else:
        scene 08_1943 with Dissolve(1)
        mc "Sort of..."
        ir "Sort of? What kind of answer is that?"
        ir "Is she pretty?"
        mc "Very pretty."
        ir "Hmm..."
    scene 08_1944 with Dissolve(1)
    mc "How about you then? Are you seeing someone?"
    ir "There's someone I'm interested in."
    mc "Oh... Boy or girl?"
    ir "..."
    scene 08_1945 with Dissolve(1)
    mc "Girl?"
    ir "Yeah. She's best friends with my roommate Alexis."
    if Alexis_Dating == False:
        mc "{i}(Could it be the Alexis I know?){/i}"
    else:
        mc "{i}(Could it be my Alexis?){/i}"
    ir "Absolutely gorgeous. You'd probably like her, too."
    mc "Consider me intrigued."
    scene 08_1946 with Dissolve(1)
    ir "When I first met her, I felt this... like... immediate bond, I can't explain it. Do you know what I mean?"
    mc "Can't say for sure, but I'm a little jealous, now."
    ir "Don't be. I felt the same with you, which makes this even more weird."
    scene 08_1947 with Dissolve(1)
    mc "You're dating her, or...?"
    ir "*Sigh* No. I've only talked to her a few times. I don't even know if she's into girls or not."
    mc "That's very easy to figure out."
    ir "Yeah? How?"
    scene 08_1948 with Dissolve(1)
    mc "Ask her!"
    ir "..."
    mc "Haha."
    scene 08_1949 with Dissolve(1)
    ir "How about you ask her for me?"
    ir "We should exchange numbers anyway and hang out again."
    ir "I'll introduce you to my roommate, so we can go on a double date."
    if Alexis_Dating == False:
        mc "Your roommate?"
        ir "She's very beautiful, too."
    else:
        mc "I told you I'm dating..."
        ir "Doesn't matter. I'm sure my roommate is prettier!"
        mc "..."
        mc "{i}(Prettier than Alexis? I don't think so.){/i}"
    scene black with Dissolve(1)
    pause 2
    scene 08_1950 with Dissolve(1)
    play sound "Sounds/Aeroplane_Beep.wav" volume 0.3
    pi "Please fasten your seatbelts..."
    ir "We're here already? Wasn't this a six-hour flight?"
    mc "It was."
    ir "Wow. I forgot how fast time passes when we hang out."
    ir "I have so much more to tell and ask."
    scene black with Dissolve(1)
    pause 2
    stop music fadeout 1.0
    play music ("Music/LoFi Indie 3.mp3", "Music/LoFi Indie 1.mp3", "Music/LoFi Indie 2.mp3") volume 0.2
    scene 08_1951 with Dissolve(1)
    ir "I'm really happy we met again. I didn't know I missed you this much."
    mc "Heh, same."
    ir "I've got your number now, so we'll stay in contact. Maybe we can do something during spring break?"
    mc "Sounds good."
    ir "Great! Double date incoming!"
    scene 08_1952 with Dissolve(1)
    ir "Kay, gotta go. I'll call you."
    mc "But please not at two in the morning, like you used to."
    ir "Haha, that's because I missed you when you weren't in my bed."
    mc "..."
    scene 08_1953 with Dissolve(1)
    ir "Bye, [mc]."
    mc "Bye..."
    scene 08_1954 with Dissolve(1)
    ir "Haha, sorry. Old habit."
    ir "Bye-bye."
    scene 08_1955 with Dissolve(1)
    ir "..."
    scene black with Dissolve(2)
    pause 2
    scene 08_2352 with Dissolve(1)
    mc "What brings you to this garage?"
    ir "I told you my dad owns one. This is it!"
    mc "Oh wow..."
    ir "Still think this is all planned and not a coincidence?"
    mc "You're starting to convince me."
    scene 08_2294 with Dissolve(1)
    mc "By the way, something's been on my mind since we met on the plane."
    ir "Okay?"
    if Alexis_Dating == False:
        mc "You told me you have a crush on your roommates' best friend, right?"
        ir "Correct."
        mc "And your roommate's name is Alexis?"
        ir "Uh-huh."
        mc "That best friend, could it be Erynn?"
        scene 08_2295 with Dissolve(1)
        ir "You know Erynn?"
        if Erynn_End == True:
            mc "I know her from back in the day. But we aren't really friends."
            ir "Too bad. You could've told me everything about her."
            if Emily_Week3_Sunday_Surprise == True:
                jump Week4_Wednesday_Garage_Emily
            else:
                jump Week4_Wednesday_Garage_Zach
        else:
            mc "We've been friends since we were little."
            scene 08_2296 with Dissolve(1)
            ir "Really? You need to tell me all about her, then. What does she like? Is she into girls?"
            mc "Uhm..."
            ir "No wait, I have a better idea."
            ir "Double date!"
            mc "Heh."
            if Emily_Week3_Sunday_Surprise == True:
                jump Week4_Wednesday_Garage_Emily
            else:
                jump Week4_Wednesday_Garage_Zach
    else:
        mc "Your roommate's name is Alexis, right?"
        ir "Correct."
        mc "Last name Monroe?"
        scene 08_2295 with Dissolve(1)
        ir "Yeah... You know her?"
        mc "I'm dating her."
        ir "What? No way... You're the boy she's dating? Now I know why she's been on cloud nine lately."
        ir "These coincidences are getting scary now!"
        mc "Tell me about it. But there's more. Your crush, Alexis's best friend, Erynn?"
        ir "You know Erynn too?"
        mc "She's a friend of mine."
        ir "My head's starting to spin..."
        scene 08_2296 with Dissolve(1)
        ir "Okay, you need to tell me all about her. What does she like? Is she into girls?"
        mc "Uhm..."
        ir "No wait, I have a better idea."
        ir "The double date I mentioned!"
        scene 08_2297 with Dissolve(1)
        mc "That'd be a little complicated."
        ir "How so?"
        mc "I don't know if I should tell you this, but Alexis and Erynn aren't on speaking terms at the moment."
        ir "What? Why?"
        mc "{i}(Well...){/i}"
        ir "But that explains why she hasn't come over in a while. I thought she was busy..."
        ir "They need to talk and make up already! I want this double date!"
        mc "Agreed. On the making up part. Not the double date."
        ir "No, no. It's already in the works."
        if Emily_Week3_Sunday_Surprise == True:
            jump Week4_Wednesday_Garage_Emily
        else:
            jump Week4_Wednesday_Garage_Zach

label Week4_Wednesday_Garage_Emily:
    scene 08_2298 with Dissolve(1)
    ir "But enough talk about girls and relationships for today. Why are you here? Buying a motorcycle?"
    mc "We came here to look for a car. But then I saw the bikes and... Well..."
    ir "Especially this one, huh?"
    mc "Yeah. I don't know why, but once I saw it, it somehow drew me in."
    ir "I might have an idea why. I'll show you."
    scene 08_2299 with Dissolve(1)
    ir "Does this trigger your memory?"
    mc "..."
    mc "Oh my god... You, me and your dad's bike..."
    ir "Uh-huh. I knew you'd remember. This is the actual bike!"
    scene 08_2300 with Dissolve(1)
    ir "If you ever want to recreate that night. I'm up for it."
    mc "I..."
    scene 08_2301 with Dissolve(1)
    ir "Haha. I'm just playing."
    if Alexis_Dating == True:
        mc "..."
        ir "Alexis might enjoy that though! She's a little rocker chick."
    else:
        mc "..."
    scene 08_2302 with Dissolve(1)
    ir "Anyway. You're becoming more like my dad every day. First the tattoos, something of a beard? Now a bike."
    mc "He's a cool guy, what can I say?"
    ir "Haha. He has his moments."
    scene 08_2303 with Dissolve(1)
    ir "Oh... Give me a second."
    ir "Who's that?"
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 08_2304 at moveup
    pause 3
    mc "That's my mom."
    ir "That's Emily? She's gorgeous. Is she single?"
    mc "She's my mom, Iris!"
    ir "You said that already."
    mc "*Sigh*"
    scene 08_2305 with Dissolve(1)
    ir "Hello, Emily. It's so nice to finally meet you."
    m "Uhm... Hello..."
    ir "I'm Iris. [mc]'s ex-girlfriend."
    m "Oh..."
    scene 08_2306 with Dissolve(1)
    m "Nice to meet you, Iris."
    m "Ex-girlfriend?"
    ir "Oh yeah. That was back in Alvarado."
    ir "We broke up because my dad and I had to move, but it seems we're in the same city again."
    scene 08_2307 with Dissolve(1)
    ir "Excuse me for a second. I think my dad's back."
    ir "I'll be right back."
    scene 08_2308 with Dissolve(1)
    m "You never told me you had a girlfriend."
    mc "I know, sorry. We didn't really talk back then."
    m "How long were you together?"
    mc "Uh... A while."
    scene 08_2309 with Dissolve(1)
    m "A while? It must have been quite a serious relationship."
    mc "It was."
    m "She was your first girlfriend?"
    mc "Yes."
    m "I would've loved to get to know her."
    mc "You still can. We're friends."
    scene black with Dissolve(1)
    pause 2
    scene 08_2310 with Dissolve(1)
    m "Did you find anything?"
    mc "Besides the one outside, no."
    mc "But I've been looking at the bikes here."
    scene 08_2311 with Dissolve(1)
    m "A motorcycle? Do you even know how to ride one?"
    mc "Yeah, and think about it. It's cheaper, less fuel..."
    m "More dangerous!"
    mc "True, but..."
    m "What about when it rains?"
    mc "*Sigh*"
    scene 08_2312 with Dissolve(1)
    m "What's the price tag on one of those anyway?"
    scene 08_2313 with Dissolve(1)
    x "This one here is half price!"
    mc "John!"
    scene 08_2314 with Dissolve(1)
    jo "Hey. How are you, [mc]."
    mc "I'm good."
    scene 08_2315 with Dissolve(1)
    mc "John, this is my mom, Emily."
    mc "This is John, Iris's dad."
    m "Nice to meet you, John."
    jo "The pleasure is all mine, Emily."
    scene 08_2316 with Dissolve(1)
    jo "So you're finally visiting your mom? About time."
    mc "I actually moved back here."
    jo "I didn't know you were from Madison Springs. But good choice. This is a much nicer place than Alvarado."
    jo "Andres is here too?"
    ir "Dad!"
    scene 08_2317 with Dissolve(1)
    jo "What?"
    ir "We don't talk about him."
    jo "Did something happen?"
    mc "Long story. I'll tell you another time."
    jo "Alright."
    scene 08_2318 with Dissolve(1)
    jo "Oh, Iris. There's a guy who's buying the charger outside."
    jo "Can you start with the paperwork?"
    jo "I'll have a quick chat here and I'll finish it up after."
    ir "Sure."
    jo "Thanks."
    scene black with Dissolve(1)
    pause 2
    scene 08_2319 with Dissolve(1)
    jo "What can I help you guys with?"
    m "Well, we were looking for a car for him. But he might be more interested in this motorcycle here."
    jo "I might be at fault for that. I was the one who introduced him to bikes."
    scene 08_2320 with Dissolve(1)
    m "Can I ask you a question? Parent to parent."
    jo "Of course."
    m "Would you buy a nineteen-year-old a motorcycle?"
    jo "Honestly, if I didn't know him, no. Especially a machine with this much power. At least I wouldn't recommend it."
    jo "But I've known him for a while. He basically lived at my place. He's responsible, and he knows how to ride."
    scene 08_2321 with Dissolve(1)
    m "Hmm..."
    jo "You don't have to make a decision now. Sleep on it, take a few days to think about it."
    m "Thank you."
    scene 08_2322 with Dissolve(1)
    jo "And you too!"
    jo "This will sound strange coming from me, but a motorcycle isn't always practical."
    jo "A car has its advantages."
    ir "Dad! The papers need your signature."
    scene 08_2323 with Dissolve(1)
    jo "I'd better take care of the customer now. Can't make him wait for too long."
    jo "If you have any questions or need some information, come by, email me, or Iris can help you too."
    m "Thank you."
    jo "Emily, so nice to meet you."
    m "Nice to meet you too, John!"
    scene 08_2324 with Dissolve(1)
    jo "[mc], come by any time. You're always welcome here."
    mc "Will do. Thanks."
    jo "Next time I'll take some time and we'll have a proper chat and some beers."
    scene 08_2325 with Dissolve(1)
    jo "Oh, he's allowed to drink beer, right?"
    m "Haha yeah, but..."
    jo "In moderation."
    scene 08_2326 with Dissolve(1)
    jo "And that goes for you too, Emily. If you ever want to chat, feel free to come by."
    jo "I have some nice stories to tell about those two."
    m "Oh, I'd love to hear those."
    jo "I don't know if you are a beer gal, but I'll make sure to have some wine too."
    m "Beer is fine."
    jo "Gotcha."
    scene black with Dissolve(1)
    pause 2
    scene 08_2327 with Dissolve(1)
    mc "..."
    m "What?"
    mc "You didn't have to flirt with him."
    m "He flirted with me!"
    scene 08_2328 with Dissolve(1)
    mc "'Beer is fine'."
    m "Haha. Okay, maybe a bit. I'm sorry."
    scene 08_2329 with Dissolve(1)
    mc "Thanks for not just saying no."
    m "Of course. Let's talk about it and we'll make a decision together, deal?"
    mc "Perfect!"
    scene 08_2330 with Dissolve(1)
    ir "Oh, you're leaving?"
    mc "For today, yes. We'll be back once a decision is made."
    ir "Great."
    scene 08_2331 with Dissolve(1)
    ir "It was so nice to meet you, Emily."
    m "..."
    m "Very nice to meet you too, Iris."
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 08_2332 at moveup
    pause 3
    m "Uh..."
    ir "Sorry, I'm a hugger."
    mc "*Shakes head*"
    mc "{i}(Seriously, this girl...){/i}"
    if Erynn_Week3_Monday_Blackmailhelp == True:
        scene 08_2333 with Dissolve(1)
        ir "Bye, [mc]. And don't be a stranger now."
        mc "I won't. Bye, Iris."
        scene 08_2334 with Dissolve(1)
        ir "*Whisper* By the way, your mom has an amazing ass!"
        mc "*Whisper* By the way, Erynn said the same thing!"
        ir "*Whisper* She did? So Erynn is into girls?"
        mc "*Whisper* Find out for yourself!"
        ir "*Whisper* You're so mean!"
        scene 08_2335 with Dissolve(1)
        ir "*Whisper* And still freakin' handsome!"
        mc "Heh. Bye, Iris!"
    else:
        scene 08_2335 with Dissolve(1)
        ir "Bye, [mc]. And don't be a stranger now."
        mc "I won't. Bye, Iris."
    scene black with Dissolve(1)
    pause 2
    scene 08_2336 with Dissolve(1)
    m "So uhm... Iris... She's very..."
    mc "Friendly? Yeah, I saw that. That's just how she is."
    m "Well, that was a first for me."
    scene 08_2337 with Dissolve(1)
    mc "You sure? Melissa told me a different story!"
    m "WHAT?"
    m "What did she tell you?"
    mc "Haha, nothing!"
    mc "*Mumbles* Just some college fun..."
    scene 08_2338 with Dissolve(1)
    m "I heard that!"
    m "I can't believe she told you."
    m "How fast is that motorcycle again?"
    mc "Haha, why? Are you in a hurry?"
    m "I have some urgent business with a certain Ms Orlandi."
    scene 08_2339 with Dissolve(1)
    mc "Ooh... 'Business'."
    m "NOT THAT!"
    mc "Haha."
    jump Week4_Wednesday_Evening

label Week4_Wednesday_Garage_Zach:
    scene 08_2298 with Dissolve(1)
    ir "But enough talk about girls and relationships for today. Why are you here? Buying a motorcycle?"
    mc "We came here to look for a car. But then I saw the bikes and... Well..."
    ir "Especially this one, huh?"
    mc "Yeah. I don't know why, but once I saw it, it somehow drew me in."
    ir "I might have an idea why. I'll show you."
    scene 08_2299 with Dissolve(1)
    ir "Does this trigger your memory?"
    mc "..."
    mc "Oh my god... You, me and your dad's bike..."
    ir "Uh-huh. I knew you'd remember. This is the actual bike!"
    scene 08_2300 with Dissolve(1)
    ir "If you ever want to recreate that night. I'm up for it."
    mc "I..."
    scene 08_2301 with Dissolve(1)
    ir "Haha. I'm just playing."
    if Alexis_Dating == True:
        mc "..."
        ir "Alexis might enjoy that though! She's a little rocker chick."
    else:
        mc "..."
    scene 08_2302 with Dissolve(1)
    ir "Anyway. You're becoming more like Dad every day. First the tattoos, something of a beard? Now a bike."
    mc "He's a cool guy, what can I say? Is he here?"
    ir "He's here, but at the moment, he's giving someone a test drive. I'll get him once he's back. Shouldn't be too long."
    mc "{i}(Must be with Zach.){/i}"
    scene 08_2358 with Dissolve(1)
    mc "What's the price for this one?"
    ir "Hmm, let's see."
    x "That one's half price."
    scene 08_2359 with Dissolve(1)
    ir "Oh, you're back."
    x "I'd never thought I'd see you two together again."
    mc "John!"
    scene 08_2360 with Dissolve(1)
    jo "Hey. How are you, [mc]."
    mc "I'm good."
    scene 08_2316 with Dissolve(1)
    jo "You're looking good."
    jo "Finally filling out that frame of yours, huh?"
    scene 08_2361 with Dissolve(1)
    jo "Are you here on vacation or something?"
    mc "I actually moved back here."
    jo "Right. You told me you're from Madison Springs originally."
    jo "Andres is here too?"
    ir "Dad!"
    scene 08_2362 with Dissolve(1)
    jo "What?"
    ir "We don't talk about him."
    jo "Did something happen?"
    mc "Long story. I'll tell you another time."
    scene 08_2363 with Dissolve(1)
    jo "I'd love to stay and chat but I have a customer I need to take care of."
    ir "He bought the charger?"
    jo "He's about to, yes."
    scene 08_2364 with Dissolve(1)
    jo "[mc], come by any time. You're always welcome here."
    mc "Will do. Thanks."
    jo "Next time I'll take some time and we'll have a proper chat and some beers."
    mc "Sounds great."
    scene 08_2333 with Dissolve(1)
    ir "I need to start doing some work too, now."
    ir "Don't be a stranger, and come see me once in a while."
    ir "Well, more than once in a while, we have lots to talk about."
    mc "Hehe, alright."
    scene 08_2335 with Dissolve(1)
    ir "Bye, handsome!"
    mc "Bye, Iris."
    scene black with Dissolve(1)
    pause 2
    scene 08_2365 with Dissolve(1)
    mc "Alright, Zach. Let's see what this can do."
    z "Oh yeah. I've been waiting for this!"
    z "Hold on tight!"
    jump Week4_Wednesday_Evening

label Week4_Wednesday_Evening:
    scene black with Dissolve(2)
    pause 2
    scene 08_2366 with Dissolve(1)
    n "*Ding-dong*"
    m "[mc], can you get the door please. I'm in the bathroom."
    mc "Are you expecting someone?"
    m "A delivery."
    if Andres_FB_Punch == True:
        scene 08_2367 with Dissolve(1)
        x "Good evening, I have a parcel for an Emily Vicari."
        mc "Yes, I'll take it."
    else:
        if Nikki_Girlfriend == True:
            scene black with Dissolve(1)
            transform moveup:
                xalign 0.5 yalign 1.0
                linear 5.0 yalign 0.0
            show 08_2368 at moveup
            pause 3
            ni "Hi."
        else:
            if Cara_Girlfriend == True:
                scene black with Dissolve(1)
                transform moveup:
                    xalign 0.5 yalign 1.0
                    linear 5.0 yalign 0.0
                show 08_2369 at moveup
                pause 3
                c "Hi."
            else:
                scene 08_2367 with Dissolve(1)
                x "Good evening, I have a parcel for an Emily Vicari."
                mc "Yes, I'll take it."
    jump Episode_9_Start

# Max Points:

# Alexis (40)
# Melissa (14)
# Layla (66)
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
# Valeria (12)
# Zach (10)
# Darryl (2)
# ShaCarri (4)
# Iris (2)

# MC_GoodStudent (14)

# Nikki_Weekend (10)
# Cara_Weekend (6)
# Alexis_SP (2)
# Alexis_Jealous (2)

# MC_Sex (21)
# Alexis_Sex (8)
# Tori_Sex (2)
# Lakeyn_Sex (1)
# Nikki_Sex (3)
# Cara_Sex (3)
# Julia_Sex (1)
# Rachel_Sex (1)
# Gabi_Sex (2)

#WTAdded
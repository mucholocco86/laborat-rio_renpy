default gwenoutsidetalk = False
default aineinvitebreakfast = False
default aineteachhelp = False
default turnwateroff = False
default naomiride = False
default noamiaboutjob = False
default noamiaboutself = False
default gwenbuywine = False
default gwenroomaccess = False
#default gwenroute = False

label ep3:
    k "Could you please stop mentioning his name? The man was already long gone."
    k "Can't you just... move on with your life, huh? Hera?"
    k "Playing with our lives isn't enough for you? What else do you want?"
    h "Let's just say..."
    h "...I want nothing but entertainment."
    h "Is that reason good enough for you?"
    scene ep3_1
    with dissolve
    k "Entertainment?"
    k "Entertainment, you say?"
    k "My husband died because of you!"
    k "You used your own daughter to make [mc] suffer because you couldn't move on with what happened to us in the past..."
    k "...and now, you're telling me that you just want entertainment?!"
    k "How can you stomach all the devious things you've done to us?"
    h "That's who I am, Klara. You are fully aware of who I am and what I am capable of."
    h "You should've thought about it more carefully when you stole Jovian from me."
    scene ep3_2
    with dissolve
    k "Stole? Stole you say?"
    k "He chose me instead of you. I did nothing to take his attention away from you, Hera."
    k "Enough is enough."
    k "One more move from you, and this won't stay between just you and me anymore."
    scene ep3_3
    with dissolve
    h "Hmp... What can you do? Report me to the authorities?"
    h "I can control the law, Klara."
    h "And I know what you've been doing all this time. I know for a fact that my daughter is staying with him right now."
    h "I know what you are planning. You're just as dirty as I am. *chuckles*"
    k "I have no idea about what you're saying, but if you think I am doing something like you do, then you're mistaken."
    k "I may not have told him about it, and that's selfish of me, I know."
    k "But all I want is for them to understand and forgive each other."
    k "Whether they want to do that or not, is totally up to them."
    k "You may have been my best friend long ago, but don't put me into the same box as you are, Hera."
    k "If you want something, come to me. Don't drag the kids into our issues."
    scene ep3_4
    with dissolve
    k "Now, if you'll excuse me, I don't want to waste my time talking nonsense with you."
    h "*chuckles* Well then, good luck with your endeavour. Tell him I said 'Hi', will you?"
    k "Hmp..."

    scene black
    with dissolve
    with fade

    scene ep3_5
    with dissolve
    k "{i}*sighs* A problem as soon as I set foot on the country...{/i}"
    scene ep3_6
    with dissolve
    k "{i}Anyway... I wonder what are those two doing right now.{/i}"
    k "{i}I haven't been able to contact them since I was overseas.{/i}"
    k "{i}In any case, I should call to inform them that I'll be coming home soon. I just have to finish some business in this city first.{/i}"
    k "{i}I bet they'll be ecstatic to know that I'm back in the country again. *giggles*{/i}"
    k "{i}Oh, right. I should fix something for dinner first.{/i}"
    play sound 'audio/doorbell.mp3'
    "*doorbell rings*"
    scene ep3_7
    with dissolve
    k "Hmn?"

    scene black
    with dissolve
    with fade

    play sound 'audio/closedoor.mp3'
    scene ep3_8
    with dissolve
    k "Why if it isn't my dear Kana!"
    ka "Good evening, aunt Klara!"
    scene ep3_9
    with dissolve
    k "Oh, my... you look more like a real woman now!"
    k "Taking a good look at you, you really look like my sister. *giggles*"
    ka "Like mother, like daughter, right?"
    scene ep3_10
    with dissolve
    ka "By the way, here are the documents that you asked me to bring."
    scene ep3_11
    with dissolve
    k "Oh, gosh! Right! I told you to bring these to me here, didn't I? Thank you, dear!"
    k "...My~ I really am getting old, indeed!"
    scene ep3_12
    with dissolve
    ka "Don't be too hard on yourself, Auntie. And if you ask me, you don't look old at all!"
    k "Aw... you're such a sweetheart, aren't you? Flattering me won't make me cook your favorite food, you know? *giggles*"
    k "But since you did me great favor... Alright, I'll reconsider."
    ka "Oh, yes~! I haven't tasted your food in years, Auntie!"
    k "Come and sit down on the sofa first, dear. I'll cook our dinner real quick."
    k "You're not in a hurry, are you?"
    ka "No, just take your time, Auntie. *giggles*"
    stop music fadeout 2

    if ainepoint == 3:
        scene black
        with Dissolve(2.0)
        label thunderchan:
        if _in_replay:
            $ name = persistent.gallery_name
        scene thunderchan
        with dissolve
        $ renpy.pause()
        $ renpy.end_replay()
        play sound 'audio/gamepause.mp3'
        show title at move_slide
        with flash
        $ renpy.notify(imageunlock)
        $ renpy.pause()
    else:
        scene black
        with Dissolve(2.0)
        label klaraherapause:
        if _in_replay:
            $ name = persistent.gallery_name
        scene klaraherapause
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

    "Meanwhile..."

    scene black
    with dissolve
    with fadeq

    play music 'audio/marshmallow.mp3'
    scene ep3_13
    with dissolve
    mc "Uhm... why are you so shocked to see me? You're not doing anything fishy, are you?"
    e "F-fishy? No. I'm just cooking for dinner... and..."
    e "{i}W-w-why does he have to come down here all of a sudden? Now of all times when I'm wearing this outfit!{/i}"
    e "{i}I thought Sky was the one coming in here since she's the one usually cooking and all.{/i}"
    scene ep3_14
    with dissolve
    e "{i}I-I have to compose myself.{/i}"
    yt "Here she is acting all strange again..."
    yt "...I really don't get her."
    e "*ahem*..."
    yt "She cleared her throat?"
    scene ep3_15
    with dissolve
    e "*sighs*..."
    yt "A sigh?"
    scene ep3_16
    with dissolve
    e "No, I'm just cooking for dinner. I won't poison you, so don't worry."
    scene ep3_17
    with dissolve
    mc "Are you sure about that...?"
    e "Yes."
    scene ep3_18
    with dissolve
    mc "Hmm... But why are you wearing a maid outfit? This isn't a mansion, you know?"
    mc "We're just in a regular house on an ordinary city street."
    image emckb:
        "ep3_19.jpg"
        pause 3.0
        "ep3_20.jpg"
        pause .2
        repeat
    show emckb
    with dissolve
    e "I got used to it when we were still in the mansion and wore it out of habit."
    e "I wear this all morning and at night. It's like my uniform."
    mc "...I can see why you got used to it."
    menu:
        "Compliment":
            mc "I must say, you look pretty good in it, Emma."
            mc "Although I still don't get why you were shocked to see me earlier."
            $ emmapoint += 1
            $ renpy.notify(emmanotif)
        "Don't mind it":
            mc "Although I still don't get why you were shocked to see me earlier."

    e "Because Aine and Freya are the only ones who've seen me wearing it. I'm not used to anybody but them seeing me in this outfit."
    mc "Not even Gwen?"
    e "Not even Gwen."
    mc "Jeez..."
    mc "I still don't trust you cooking our dinner, though."
    mc "You put laxatives on my lunch back in school, don't you remember?"
    mc "That sent me to the bathroom countless times that whole day, you psycho woman!"
    e "I was just..."
    scene ep3_21
    with dissolve
    e "{i}No... Even though Aine said she'll take all the blame... Still, my own actions are my own responsibility.{/i}"
    e "{i}I can't just let her shoulder everything.{/i}"
    image emckb2:
        "ep3_22.jpg"
        pause 3.0
        "ep3_23.jpg"
        pause .2
        repeat
    show emckb2
    with dissolve
    e "Hey, uhm... I..."
    mc "Hm?"
    e "I'm sorry... for... hurting you before. Aine told me you guys had talked. And..."
    mc "Oh, boy..."
    mc "*sighs* You know that I don't need that, right?"
    mc "Just like what I said to Aine, I don't need an apology. All I want is for you to show your sincerity through your actions."
    mc "......"
    mc ".........."
    mc "You know what, Emma?"
    show emckb
    with dissolve
    e "Hmn?"
    mc "......"
    mc "No, never mind. Something just caught my mind for a moment."
    menu:
        "Ask about Aine":
            mc "I must ask you though. Why didn't you tell me that Aine was being mistreated by her mother?"
            mc "Like, we had a pretty long conversation last time, but you never mentioned anything about it. Why is that?"
            e "The reason is simple."
            e "...We are forbidden to talk to outsiders about Aine's mother, even if it's someone as important as a government official asking us to do so."
            e "I'm not even allowed to say her name."
            mc "Jesus Christ! Who does she think she is? The president of the country?"
            mc "Ever since I learned these things about you and Aine's family, all I can do whenever I try to think about it is to either shake my head or facepalm myself!"
            mc "There's not a single word I can think of to describe how messed up you guys are!"
            e "Sorry..."
            mc "Now you turned into an apologetic mushroom? *sighs*"
            mc "Never mind... Let's just finish the dinner before everyone comes down."
            e "Oh... sure."
        "End the conversation":
            mc "We should finish cooking those now before everybody comes down here."
            e "Oh... sure."

    scene black
    with dissolve
    with fadeq

    "After your dinner..."

    scene black
    with dissolve
    with fadeq

    scene ep3_24
    with dissolve
    "*phone vibrates*"
    scene ep3_25
    with dissolve
    s "Hm?"
    s "Who's calling me this late at night?"
    s "......"
    scene ep3_26
    with dissolve
    s "*gasps* It's Mom!"
    scene ep3_27
    with dissolve
    s "[mc]~! Mom is calling!"
    mc "Oh! Hold on! I'm coming!"
    scene ep3_28
    with dissolve
    mc "Can you manage the dishes?"
    a "Of course. Just go and talk to her. Don't worry about me."
    menu:
        "Just go":
            mc "Alright, I'll leave it to you."
        "Thank her{#ep3}":
            $ ainepoint += 1
            $ renpy.notify(ainenotif)
            mc "Thanks, Aine. I'll leave it to you then."

    scene ep3_29
    with dissolve
    a "Hmn??"
    a "Why is the water draining so slowly?"

    scene black
    with dissolve
    with fade

    scene ep3_30
    with dissolve
    s "Oh, here he is! I'm putting it on speaker so we can both hear you."
    scene ep3_31
    with dissolve
    mc "Hey, Klara! It's been a while since the last time you called. How are you? You're doing fine, right?"
    k "I'm doing really fine, dear. Thanks for asking."
    k "How about you two? I haven't checked on you for a while. It's been hectic with work lately."
    mc "Don't worry about us too much. We're both doing fine!"
    mc "Right, Sky?"
    scene ep3_32
    with dissolve
    s "Yep! All good and healthy! *giggles*"
    k "Well, I'm relieved to hear that."
    k "Oh, by the way, I have a small surprise for the two of you."
    s "Huh?"
    k "Let me switch this call to a video. Just give me a moment."
    k "*whispers * Here, take it."
    scene ep3_33
    with dissolve
    ka "[mc]~! Sky~! How are you guys? Heheee~!"
    mc "Who in the..."
    s "Kana?! Wait... is that you now? You look so different than the last time we saw you~! Wow~!"
    s "I know I'm older than you, but you look really mature now! What happened to you over the past two years?"
    mc "Seriously?! Is that really you now, Kana?!"
    mc "For real, we're both not exaggerating! You look... more like a woman now!"
    mc "Back then you look more of a kid than a certain someone beside me. But now..."
    s "Hey~!"
    mc "What happened to you?"
    ka "I don't know. I guess puberty wasn't over for me yet."
    ka "And I did not really change that much, if you ask me."
    ka "Anyway, I'm hoping we can meet up soon! How about we go camping somewhere? Sounds exciting, right?"
    s "Of course! We should take Mom with us too!"
    mc "Wait, wait, wait. Hold up... Something is not right here..."
    s "Huh? What are you talking about?"
    scene ep3_34
    with dissolve
    k "*chuckles*"
    mc "Kana was Klara's former assistant, right? But then, Kana stopped working with her when Klara went abroad."
    s "So...?"
    mc "So... why are they together?"
    s "*gasps*"
    s "Don't tell me she's..."
    mc "Back home?!!"
    s "Back hooome?!!"
    scene ep3_35
    with dissolve
    ka "So you guys just noticed, huh?"
    ka "I sure had my fair share of stupidity before, but I wasn't expecting you guys to be so dense. Ahaha!"
    s "Hey, hey! You're a year younger than me, you know? Don't speak like you have all the wisdom in the universe!"
    k "Alright, alright... you guys should calm down before it gets out of hand."
    k "Nothing has changed whenever you guys talk or meet each other."
    k "You're all so hyper!"
    k "Anyway, to answer your questions..."
    k "Yes, I'm back in the country. But I won't be home just yet."
    k "I still have something to take care of in this city for a couple of weeks."
    k "But rest assured that I will definitely come home once I'm done with my remaining work here."
    s "Awww... I was so excited to finally have you back here again too!"
    k "Don't worry, dear. I will be home in no time."
    mc "But, how long will you stay here once you arrive home? I know you still have to go back abroad, right?"
    k "That is also the reason why I had Kana come over to my apartment."
    s "Hm?"
    k "I'm not planning to go abroad anymore. I will establish my own company here. And Kana will be helping me all throughout the process."
    scene ep3_36
    with dissolve
    ka "Yep!"
    s "F-for real?!"
    scene ep3_37
    with dissolve
    k "Yes, my dear! However, we need to process some papers here first."
    k "That is why I couldn't come home just yet. But I will, once all matters have been taken care of."
    menu:
        "That's great news":
            mc "That's incredible news! I'm glad that you will have your own company soon."
            $ klarapoint += 1
            $ renpy.notify(klaranotif)
            mc "And with Kana's help, I'm pretty sure that it will lead to nothing but success. No one's smarter than her, after all. Hahaha!"
            k "I agree that she is. *giggles*"
            scene ep3_38
            with dissolve
            ka "You guys give me too much credit. I haven't done anything yet, you know?"
            k "Yet, that is. But with you as my partner, I agree with [mc] that everything will lead to success."
            k "That's why I chose you, and I'm glad that you accepted my request."
            scene ep3_39
            with dissolve
            ka "I can't really turn you down, Auntie. You helped me stand on my own feet back then, so I owe you a lot. *giggles*"
        "Don't say anything":
            mc "And with Kana's help, I'm pretty sure that it will lead to nothing but success. No one's smarter than her, after all. Hahaha!"
            k "I agree that she is. *giggles*"
            scene ep3_38
            with dissolve
            ka "You guys give me too much credit. I haven't done anything yet, you know?"
            k "Yet, that is. But with you as my partner, I agree with [mc] that everything will lead to success."
            k "That's why I chose you, and I'm glad that you accepted my request."
            scene ep3_39
            with dissolve
            ka "I can't really turn you down, Auntie. You helped me stand on my own feet back then, so I owe you a lot. *giggles*"

    scene ep3_40
    with dissolve
    ka "Anyway, I think I should be going home now. It's getting pretty late."
    k "Alright, dear. Take care on your way home."
    ka "I will. Thanks, Aunt Klara!"
    ka "Goodbye for now, [mc], Sky! We'll talk again some other time, okay?"
    mc "Sure, Kana. And take care!"
    s "Bye, Kana! Talk to you again soon!"

    scene black
    with dissolve
    with fadeq

    scene ep3_41
    with dissolve
    k "I should be getting some sleep soon, too. I'm still quite tired from all the travel."
    s "No worries, Mom. You should go get some rest now."
    mc "Have a good night's sleep. We'll talk to you again soon?"
    k "Of course, dear! You two have a good night as well."

    if skyroute:
        scene ep3_42
        with dissolve
        s "......"
        mc "Hm? What are you thinking, Sky?"
        scene ep3_43
        with dissolve
        s "I should be happy that Mom will come home soon... But..."
        s "I'm worried about how she'll take it when she learns about our relationship."
        scene ep3_44
        with dissolve
        yt "Now that I think about it, she's right. There's no way Klara will accept our relationship just like that..."
        yt "But we chose this. It will be our responsibility to tell her about it sooner or later."
        yt "For now, I should..."
        menu:
            "Reassure her":
                scene ep3_45
                with dissolve
                mc "Don't worry about it for now, Sky."
                mc "It will be a challenge for both of us since we chose this, but I think she will understand us."
                mc "What's important is that we love each other. And we'll fight for it no matter what happens."
                $ skypoint += 1
                $ renpy.notify(skynotif)
                scene ep3_46
                with dissolve
                s "Thanks for saying that, [mc]."
            "Act nervous":
                scene ep3_47
                with dissolve
                mc "Yeah, I'm quite nervous about how she'll react, too."
                mc "But we chose this, and I'm sure she will understand us."
                mc "What's important is that we love each other. And we'll fight for it no matter what happens."
                s "Yeah... you're right..."

        mc "We both should get some rest now, too. We still have work tomorrow."
        s "Yep! Hehe! Let's go."
    else:
        scene ep3_47
        with dissolve
        mc "We both should get some rest now too. We still have work tomorrow."
        s "Yep! Hehe! Let's go."
    stop music fadeout 2

    scene black
    with dissolve
    with fade

    scene ep3_48
    with dissolve
    yt "Is that Gwen? Where is she going at this hour?"
    yt "...Well, I guess she's just going outside. Should I talk to her?"
    menu:
        "Talk to her":
            $ gwenoutsidetalk = True
            scene ep3_49
            with dissolve
            mc "You can go on ahead, Sky. I want to talk with Gwen for a bit."
            s "Oh, sure. Goodnight, [mc]."
            mc "Have a good night, too, Sky."

            scene black
            with dissolve
            with fade

            play music 'audio/JourneyHome.mp3'
            scene ep3_50
            with dissolve
            mc "Hey..."
            g "[mc]?"
            mc "What's up? You look a bit gloomy."
            mc "Well... it's not like you're always smiling anyway, but..."
            scene ep3_51
            with dissolve
            mc "Just like last time we talked in the kitchen, you seem really upset."
            mc "I know you don't want to talk about it, but... are you still worried about your company?"
            scene ep3_52
            with dissolve
            g "......"
            scene ep3_53
            with dissolve
            g "........."
            scene ep3_54
            with dissolve
            $ renpy.pause()
            scene ep3_55
            with dissolve
            mc "I see you still smoke. It's not good for you, you know?"
            g "......"
            mc "......"
            scene ep3_56
            with dissolve
            g "...Remember when I told you that I regret what happened to us back then?"
            mc "Oh... yeah. I actually have been wondering about the reason behind what you said."
            mc "You can tell me anything, Gwen. But if you're uncomfortable, you don't have to."
            mc "I'm also responsible for what happened anyway, so... I'm all ears if you want to... well... let it out."
            scene ep3_57
            with dissolve
            g "*sighs*"
            g "...On the second thought, I think I should keep this to myself for now, [mc]. I'm sorry."
            mc "You don't have to be sorry. It's alright."
            yt "I wonder what her reason really is..."
            scene ep3_58
            with dissolve
            g "Thanks for coming here though. I at least have someone to talk to."
            mc "I was just curious why you were still going outside this late at night. Plus, it's cold out here and you're just in your sleepwear."
            mc "You'll catch cold if you stay out here for too long."
            scene ep3_59
            with dissolve
            g "Ah... I don't care about that. Like I have any risk of it affecting anything when I'm sick anyway. I don't even have a job."
            mc "So, you're basically telling me that you don't care about your well-being at all?"
            mc "...Well, I don't wanna push you into something."
            mc "But I'd rather have you drink till you pass out. Way better than cutting your potential years of living with cigarettes."
            scene ep3_60
            with dissolve
            g "Drinking causes liver problems too, you silly."
            mc "Well, at least you'll live longer, right? Hahaha!"
            mc "Or you can just stop all your bad habits instead. They may fix your cravings now, but you'll suffer from it in the future."
            mc "That's something I know for certain."
            scene ep3_61
            with dissolve
            g "You know, [mc]..."
            g "That's what I like about you. You're soft-hearted, kind, and somehow care about me even though we weren't {b}that{/b} close before."
            g "Well, I didn't really do anything to you before aside from making you buy wine for me..."
            g "But still, sorry for being such a bitch..."
            scene ep3_62
            with dissolve
            g "Oh, oh~!"
            g "Remember the time when I let you taste alcohol for the first time?"
            g "If only you could've seen your face back then! Hahaha!"
            mc "Well, that was the first time I tasted it. And it tasted gross! Haha!"
            mc "I was also curious how it tasted anyway."
            scene ep3_63
            with dissolve
            g "Aah... the good old days..."
            mc "Good to you, but not for me. It was a hell of a high school!"
            scene ep3_64
            with dissolve
            g "Yeah, about that..."
            g "Don't you think you're way too forgiving? You know what I mean, right?"
            g "I don't really think it's a bad thing, but you welcomed us just like that."
            g "You knew that it was us the moment you opened that door. You had the opportunity to turn us away, especially those two, but you didn't."
            g "You know what I mean?"
            scene ep3_65
            with dissolve
            mc "*sighs*"
            scene ep3_66
            with dissolve
            mc "Yeah... I was meaning to ask Emma earlier, but I don't think she's the right person to ask about it."
            g "Haha! What can Emma help you with anyway. She even has her own problems with communicating."
            mc "Yeah... so, like... after we graduated from high school I swore to myself that I would definitely get my revenge to Aine."
            mc "But as time passed, I felt that it wasn't worth it anymore. Then, I moved on from everything."
            mc "And set my own life on a better path instead."
            mc "Now, when you guys arrived, I thought that letting you in wasn't the right thing to do."
            scene ep3_67
            with dissolve
            g "However, you welcomed us instead."
            mc "Weird, I know... Most people would still cling to their anger or hatred, but... not me... I didn't do so..."
            mc "I'm actually conflicted between my heart and my brain."
            mc "Like, I know that forgiving those who sinned against you is a good thing, but sometimes, I can't help to think that what I'm doing is probably too much..."
            g "It doesn't feel right that you're telling me all this. But, one thing I can say..."
            g "...Is that it's alright to follow your heart, because that's what's great about you. You're a good person, [mc]."
            g "You never resort to any form of violence. That just means that you're mature enough to think of what's right and what's wrong."
            g "Don't let it go to your head too much or it'll only make you stupid."
            scene ep3_68
            with dissolve
            g "But what's even stupid is to have that coming from me who couldn't even set her own life straight."
            mc "Huh? What do you mean by that? Could you not be so mysterious, please?"
            g "You shouldn't worry about me."
            image gomctb:
                "ep3_69.jpg"
                pause 3.0
                "ep3_70.jpg"
                pause .2
                repeat
            show gomctb
            with dissolve
            g "Come here and let big sister give you a hug instead."
            mc "Ugh! I don't know how to feel about that..."
            g "Jeez! I'm two years older than you, so it's fine! Hahaha! Come on, what are you waiting for?"
            menu:
                "Hug her":
                    mc "*sighs* Okay, okay!"
                    play sound 'audio/cloth.mp3'
                    scene ep3_71
                    with dissolve
                    g "Mhhnn..."
                    $ gwenpoint += 1
                    $ renpy.notify(gwennotif)
                    image gomctb2:
                        "ep3_72.jpg"
                        pause 3.0
                        "ep3_73.jpg"
                        pause .2
                        repeat
                    show gomctb2
                    with dissolve
                    g "Hmmm... You've become quite buff, haven't you?"
                    g "I remember you being so squishy back then. Ahahaha!"
                    g "Are you on some kind of a diet right now?"
                    mc "Not really a diet, I just tend to avoid too much fat in my food, that's all."
                    g "You also go to the gym, right? Why don't we go together sometime soon? It will be fun!"
                    mc "I don't have much time to work out anymore, but... we'll see on the weekend, I guess?"
                    mc "I'll see if I can free up some time, but I can't promise."
                    g "That's all fine."
                    mc "Then, let's go get some rest now. I still have work tomorrow."
                    scene black
                    with dissolve
                    g "Oh, shoot! I forgot about that! Alright, let's go!"
                    g "Ah, wait, wait! My cigarette!"
                    mc "Jeez! Throw it away properly, please."
                    g "Got it, Mr. Landlord! Hahaha!"
                "Refuse":
                    mc "This is no time for hugs! We both should get inside now or else-"
                    g "Yeah, yeah! You bummer!"
                    g "Alright, let's go get some rest."
                    scene black
                    with dissolve
                    g "Ah, wait, wait! My cigarette!"
                    mc "Jeez! Throw it away properly, please."
                    g "Got it, Mr. Landlord! Hahaha!"
        "Go to sleep":
            $ gwenoutsidetalk = False
            mc "Nahh... I still have work for tomorrow, let's just go to sleep."
    stop music fadeout 2

    scene black
    with dissolve
    with fade

    scene ep3_74
    with dissolve
    $ renpy.pause()
    scene ep3_75
    with dissolve
    yt "Huh..."
    yt "That's weird..."
    yt "I woke up pretty early today. Still quite dark outside..."
    yt "I wonder what time it is..."
    scene ep3_76
    with dissolve
    yt "......"
    yt "4 am, huh?"
    yt "Damn... that's so unusual."
    yt "Well? I guess I don't have any choice. Let's just go downstairs and see what I can make for breakfast."

    scene black
    with dissolve
    with fade

    play music 'audio/DifLove.mp3'
    scene ep3_77
    with dissolve
    yt "Hmm... Aine?"
    yt "Does she usually wake up this early?"
    menu:
        "Invite her to breakfast":
            $ aineinvitebreakfast = True
            $ ainepoint += 1
            $ renpy.notify(ainenotif)
            scene ep3_78
            with dissolve
            mc "Morning, Aine."
            scene ep3_79
            with dissolve
            a "Oh, good morning, [mc]."
            mc "I'll go and make something for breakfast. Do you want to join me?"
            a "Hmm... alright, sure! Let's go."
        "Let her be":
            $ aineinvitebreakfast = False
            yt "Not that I really care about it anyway. I'll just let her be for now."

    scene black
    with dissolve
    with fade

    if aineinvitebreakfast:
        scene ep3_80
        with dissolve
        yt "All we have are eggs and some vegetables... Hm..."
        yt "I'll probably have to go to the supermarket to buy some stuff later..."
        yt "I guess the usual rice omelet, then."
        yt "I should make some for the others too."
        scene ep3_81
        with dissolve
        yt "Alright, let's get cooking!"

        scene black
        with dissolve
        with fadeq

        scene ep3_82
        with dissolve
        a "By the way, [mc]."
        scene ep3_83
        with dissolve
        mc "Hm? What is it?"
        a "Do you usually wake up this early in the morning?"
        mc "I wanted to ask you the same question to be honest, but no..."
        mc "I tend to wake up at exactly 6 am. Somewhere around 7 am in cases where I'm really tired from the previous day's work."
        a "I see... no wonder I haven't seen you come down this early before."
        mc "Oh, so you do always wake up this early?"
        scene ep3_84
        with dissolve
        a "Yep! You know what they say -- 'The early bird gets the worm.' *giggles*"
        menu:
            "Agree":
                scene ep3_85
                with dissolve
                mc "Well, I agree with that quote. But I'd rather have proper food than a worm, thank you."
                a "Of course! You wouldn't really eat a worm, would you? Hehe!"
            "However":
                scene ep3_85
                with dissolve
                mc "However, 'The early worm gets eaten.', right?"
                a "Hmm... If I'm the bird, and you're the worm... then, do I get to eat you? *giggles*"
                scene ep3_86
                with dissolve
                mc "Uhmm..."
                yt "How the heck am I going to respond to that?"
                yt "As far as I know her, she's a pretty conservative girl. And that coming from her is just... well... weird!"
                yt "Or it's just me over-thinking it. She probably didn't mean it some other way..."
                yt "Better to change the topic now before things get awkward."

        scene ep3_87
        with dissolve
        mc "Anyway, I'll just finish cooking so we can eat."
        a "Oh, right!"
        a "I'll make some coffee."
        a "Do you want me to make a cup for you too?"
        mc "Coffee? Sure."

        scene black
        with dissolve
        with fade

        scene ep3_88
        with dissolve
        yt "It's been fifteen minutes since we started eating, and she's been totally silent since."
        yt "I'm guessing she's in deep thought about something."
        scene ep3_89
        with dissolve
        yt "Should I talk to her?"
        menu:
            "Talk to her":
                $ aineteachhelp = True
                mc "Hey, what's up? You've been silent since we started eating."
                scene ep3_90
                with dissolve
                a "Hmn?"
                a "Oh, sorry. I was just thinking about the lesson plan for today."
                mc "Lesson plan?"
                mc "...Oh, of course. You're working with Sky now, right?"
                mc "How is it so far?"
                image akmceb:
                    "ep3_91.jpg"
                    pause 3.0
                    "ep3_92.jpg"
                    pause .2
                    repeat
                show akmceb
                with dissolve
                a "So far so good! Some of the kids that are having trouble learning the language though."
                a "The exams are close and I don't want anyone in my class to fail."
                a "That is why I'm thinking of revising my lesson plan to make it easier for those who are having trouble."
                a "I may have a little experience, but it wasn't really much. So I'm still kind of... in a learning phase myself."
                a "Plus, I started in the middle of the school year."
                mc "Is that what you were checking in the living room earlier?"
                a "Yeah. I'm much more comfortable writing my lesson plans by hand, so..."
                mc "Can I check it for a moment?"
                a "Hm? Why?"
                mc "I'm good with some technical stuff, so I may know how to improve it if I could see your current plan."
                a "Oh, really?"
                scene ep3_93
                with dissolve
                a "Here it is then."
                mc "Alright, give me a minute."
                scene ep3_94
                with dissolve
                a "Sure!"

                scene black
                with dissolve
                with fadeq

                "A few moments later..."

                scene black
                with dissolve
                with fadeq

                scene ep3_95
                with dissolve
                mc "Alright, I think I see what you are having trouble with."
                mc "I'm not an online teacher like you and Sky, but I can give you a few pointers that I think will be able to help you improve."
                mc "If you're interested in hearing, that is."
                a "......"
                scene ep3_96
                with dissolve
                mc "Hey, what do you th-"
                show ep3_97
                with hpunch
                mc "Eekk!"
                mc "W-why are you staring at me like that?!"
                a "Huh?"
                a "Oh, sorry. I was just so amused at how you're really focusing on reading my notes that I can't help but stare at you."
                mc "Jeez! You almost gave me a heart attack! Can you not do that again, please?"
                scene ep3_98
                with dissolve
                a "*giggles* I'll try."
                mc "*sighs* Anyway, do you want to hear my pointers?"
                a "Of course! If it's a way to improve my teaching, then why not?"
                image akmceb2:
                    "ep3_99.jpg"
                    pause 3.0
                    "ep3_100.jpg"
                    pause .2
                    repeat
                show akmceb2
                with dissolve
                mc "Alright. Your lesson plan is already good as it is right now, so I think you don't have to worry about it."
                mc "And I can see that you're prioritizing efficiency which is good."
                mc "I came to a conclusion that the problem isn't from your plan. But on the way you teach your students instead."
                mc "I'm not sure if you're already doing these things, but I'll share it to you anyway."
                a "Uh-huh? I'm listening."
                mc "Well? First things first..."
                mc "'Reflect on your lessons'"
                mc "If you're thinking that your lessons didn't go as expected, of course, you will probably know that your lessons could be improved..."
                mc "...which is what you're trying to do right now."
                mc "So, next time that you teach, which will probably be later, reflect on the lesson afterwards."
                mc "Ask yourself something like..."
                mc "'Did the students enjoy the lesson?'"
                mc "'Did I achieve my personal aims at the end of the class? Why or why not?'"
                mc "'Were all students engaged?'"
                mc "Lastly... 'Was I interesting?'"
                mc "Those questions will certainly help you reflect and improve the way you teach your students."
                a "I see... Those are things that I never considered before. I'll be sure to remember that."
                image akmceb3:
                    "ep3_101.jpg"
                    pause 3.0
                    "ep3_102.jpg"
                    pause .2
                    repeat
                show akmceb3
                with dissolve
                mc "Also, if you're having problems reflecting your lessons, or you wish to study your lessons in more detail..."
                mc "...consider recording your own lesson to analyze it afterwards."
                mc "You will be able to see your own habits..."
                mc "...become more aware of what you were doing as well as seeing your own instruction or pick up any things that could be lost during the process of teaching."
                mc "I learned all this when I tried helping Sky with her teaching when she was having a hard time before."
                a "......"
                mc "One last thing that I would really recommend is to observe Sky while she's teaching her students."
                mc "Observing her will help you pick up new ideas for teaching and find yourself more confident after."
                mc "However, I don't know how you can make that work, since you both start and end your shifts at the same time, right?"
                mc "You might be able to talk about this with Sky later and see what she can do about it."
                mc "And I know that she will also do some observations while you're working since she's your team leader after all."
                mc "Did you get all that?"
                a "......"
                mc "Hey, are you even..."
                mc "*sighs*"
                image akmceb4:
                    "ep3_103.jpg"
                    pause 3.0
                    "ep3_104.jpg"
                    pause .2
                    repeat
                show akmceb4
                with dissolve
                a "Oh, sorry! Yes, I did get all that!"
                mc "...Really? Are you sure?"
                a "Absolutely!"
                mc "I don't trust you... Can you then repeat what I said?"
                a "Of course!"
                image akmceb5:
                    "ep3_105.jpg"
                    pause 3.0
                    "ep3_106.jpg"
                    pause .2
                    repeat
                show akmceb5
                with dissolve
                a "One... I should reflect on my lessons."
                a "Two... Record my lessons so I can analyze them later."
                a "And lastly... I should observe Sky."
                a "*giggles*"
                mc "*sighs* At least, you were listening."
                mc "We should finish eating now."
                a "Alright. I'll take care of the dishes later."
                mc "Sure."
                stop music fadeout 2

                scene black
                with Dissolve(2.0)
                if emmapoint == 0:
                    label thunderchan3:
                    if _in_replay:
                        $ name = persistent.gallery_name
                    scene thunderchan3
                    with dissolve
                    $ renpy.pause()
                    $ renpy.end_replay()
                    play sound 'audio/gamepause.mp3'
                    show title at move_slide
                    with flash
                    $ renpy.notify(imageunlock)
                    $ renpy.pause()
                else:
                    label ainepause3:
                    if _in_replay:
                        $ name = persistent.gallery_name
                    scene ainepause3
                    with dissolve
                    $ renpy.pause()
                    $ renpy.end_replay()
                    play sound 'audio/gamepause.mp3'
                    show title at move_slide
                    with flash
                    $ renpy.notify(imageunlock)
                    $ renpy.pause()
            "Continue eating":
                $ aineteachhelp = False
                yt "Nahh... Let's continue eating and just let her be."
    else:
        scene ep3_80
        with dissolve
        yt "All we have are eggs and some vegetables... Hm..."
        yt "I'll probably have to go to the supermarket to buy some stuff later..."
        yt "I guess the usual rice omelet, then."
        yt "I should make some for the others too."
        scene ep3_81
        with dissolve
        yt "Alright, let's get cooking!"
    stop music fadeout 2

    scene black
    with dissolve
    with fade

    play music 'audio/LovelySwindler.mp3'
    scene ep3_107
    with dissolve
    yt "Alright, my stomach is satisfied!"
    scene ep3_108
    with dissolve
    yt "It's still pretty early though. I'll probably just watch TV for now to kill some time."
    scene ep3_109
    with dissolve
    yt "Hmm... I wonder if there's a movie on air at this time?"
    scene ep3_110
    with dissolve
    yt "..."
    yt "...meehh..."
    scene ep3_111
    with dissolve
    yt "TV advertising shows... ugh!"
    yt "Oh... Let's check some anime on Netflix!"
    yt "Hmmn... I wonder if there's anything new..."
    yt "......"
    yt "..."
    yt "......"
    scene ep3_112
    with dissolve
    yt "'Japan Sinks', huh? A disaster anime? I've never seen this here before..."
    scene ep3_113
    with dissolve
    yt "Based on the banner, the art isn't that good, but the story might be worth it..."
    yt "Okay, let's give it a try."

    scene black
    with dissolve
    with fadeq

    "An hour later..."

    scene black
    with dissolve
    with fadeq

    scene ep3_114
    with dissolve
    $ renpy.pause()
    scene ep3_115
    with dissolve
    mc "*crying*..."
    yt "Damn it... I shouldn't have watched this!"
    scene ep3_116
    with dissolve
    s "Good morning, [mc]~!"
    g "Yow!"
    e "Morning..."
    mc "M-morning guys..."
    scene ep3_117
    with dissolve
    s "Wait, were you crying?"
    scene ep3_118
    with dissolve
    mc "What? No? Pff... why would I cry?"
    scene ep3_119
    with dissolve
    e "Hm?"
    e "I've watched that anime... It's an emotional anime where a family has to survive when a calamitous earthquake strikes the entire Japanese archipelago..."
    scene ep3_120
    with dissolve
    e "They struggle not only to stay alive, but also to learn the difficulty of coping with loss... It's a very emotional anime..."
    mc "You watch anime too?!"
    e "I don't see why not?"
    if skyroute:
        scene ep3_121
        with dissolve
        s "So was that why you were crying? Who's crying like a sissy now? *giggles*"
    else:
        scene ep3_121
        with dissolve
        s "So was that why you were crying?"
    menu:
        "Admit it":
            mc "*sighs* There's a lot of emotion in the show, alright? I couldn't help it!"
            g "There's nothing wrong with that, you know? Boys can cry too. *giggles*"
        "Deny it":
            mc "No, I didn't cry, I promise! Hahaha!"
            g "There's nothing wrong with that, you know? Boys can cry too. *giggles*"
    scene ep3_122
    with dissolve
    s "By the way, where's Aine?"
    e "She's in our room getting ready."
    s "Did she already have her breakfast?"
    e "She told me yes."
    s "I see, then let's go eat! Hihi!"
    scene ep3_123
    with dissolve
    mc "Don't bother cooking, Sky. I already made your portions for breakfast. You can just heat it up if you want."
    s "Alright! Thanks, [mc]."
    mc "No worries."

    scene black
    with dissolve
    with fadeq

    "A few moments later..."

    scene black
    with dissolve
    with fadeq

    scene ep3_124
    with dissolve
    a "[mc]?"
    scene ep3_125
    mc "Whoa! Why the hell are you down here in your bath towel?"
    image alrmctb:
        "ep3_126.jpg"
        pause 3.0
        "ep3_127.jpg"
        pause .2
        repeat
    show alrmctb
    with dissolve
    a "Ehmm... I was about to take a bath, but the tub faucet doesn't work."
    mc "Can you please elaborate on that? What do you mean, it doesn't work?"
    a "When I turn the knob, no water comes out, I'm pretty sure the water system is working since all the other faucets are functioning just fine."
    mc "Huh... well that's weird. We had all the faucets checked by a repairman before you moved in here."
    mc "But, which one isn't working?"
    a "The one in our room. I swear it was working fine yesterday. And I also noticed the kitchen sink is taking a long time to drain."
    mc "Alright, I got it. But why didn't you use the bathroom in the hallway instead?"
    a "Well... uhm..."
    mc "Ahh... don't worry, I won't accidentally barge in on you this time. Plus, I still need to call the repairman to fix this immediately."
    a "Okay then, I'll use the one in the hallway for now."

    scene black
    with dissolve
    with fadeq

    scene ep3_128
    with dissolve
    yt "Let's call that old man. I just hope that he's not on a vacation again."
    yt "Something unexpected always happens when he is."
    "......"
    ".........."
    "..............."
    un "Mornin', lad! How's it goin'?"
    scene ep3_129
    with dissolve
    mc "Good morning, Mr. Scott! I'm doing really fine, thanks for asking."
    mc "Sorry to bother you this early in the morning..."
    mc "But one of our bathtub faucets seems to be busted, and the kitchen sink drain is also partially clogged."
    mc "I would like to know if you can come here this early to fix them up?"
    sc "Normally, I certainly could. But this old-ager had an accident a few weeks ago."
    scene ep3_130
    with dissolve
    mc "Huh?! What happened to you, Mr. Scott? Are you alright?"
    sc "There, there..."
    sc "I would love to say — 'I'm fine, lad', however, my body doesn't work how it used to."
    sc "As simple a thing as fallin' down the stairs broke a few of the bones in me."
    mc "Jesus! How can you call falling down stairs a simple thing?"
    sc "Stairs are nothin' compared to roofs and water tanks, lad. Hahahahaha!"
    mc "Holy mackerel... How did you even survive all that?"
    sc "A strong will to survive, I guess? Hahaha!"
    sc "But, cheer up! I'll send someone over there in my place."
    mc "Huh? I thought you were the only repairman around these parts?"
    sc "I am, indeed. But I think it's time to pass the baton over."
    sc "Even if I do heal up, I don't think I can manage the hard work of being a repairman anymore."
    scene ep3_131
    with dissolve
    mc "Alright, Mr. Scott. I'll be sure to pay you a visit when I have some time."
    sc "And I will gladly open my door to you, lad. Now it's time for me to go back and rest."
    mc "Rest well, Mr. Scott. And please get well soon."
    scene ep3_132
    with dissolve
    yt "I feel sorry for the old man..."
    yt "I hope he recovers soon..."
    stop music fadeout 2

    scene black
    with dissolve
    with fadeq

    "20 minutes later..."

    scene black
    with dissolve
    with fadeq

    play sound 'audio/doorbell.mp3'
    play music 'audio/AtTheBar.mp3'
    scene ep3_133
    with dissolve
    "*doorbell rings*"
    yt "That's already him, I guess."

    scene black
    with dissolve
    with fade

    play sound 'audio/opendoor.mp3'
    image notmcb:
        "ep3_134.jpg"
        pause 3.0
        "ep3_135.jpg"
        pause .2
        repeat
    show notmcb
    with dissolve
    "*door opens*"
    un "Good mornin', mister!"
    yt "Whoa! Wait..."
    yt "Who the heck is this?"
    un "Dad told me ya have somethin' for me to fix here?"
    yt "Oh, she's the one Mr. Scott sent."
    yt "...I was expecting a guy who's as big as Mr. Scott, but..."
    yt "...Hold up, did she just say 'dad'? So she's Mr. Scott's daughter?"
    mc "Uhm... good morning, miss. I know your dad, so no need to be formal."
    mc "But, yes. There's a couple of things that need to be fixed."
    un "Alright, mate. Just leave it to me."
    mc "Please come inside. I'll show them to you."
    un "Sure thing!"

    scene black
    with dissolve
    with fade

    play sound 'audio/closedoor.mp3'
    scene ep3_136
    with dissolve
    n "By the way, I forgot to introduce myself. I'm Naomi. Pleased to meet ya."
    yt "Naomi, huh?"
    yt "If I remember it correctly, Naomi means 'pleasant', and that name fits her to a tee. She's so pretty and so pleasant to look at."
    menu:
        "Give her a handshake":
            $ naomipoint += 1
            $ renpy.notify(naominotif)
            scene ep3_137
            with dissolve
            mc "Nice to meet you, Naomi. I'm [mc]."
            n "That's such a lovely name!"
            mc "Haha! Thanks!"
        "Don't do it{#ep3,1}":
            mc "Nice to meet you, Naomi. I'm [mc]."
            n "That's such a lovely name!"
            mc "Haha! Thanks!"

    scene ep3_138
    with dissolve
    play sound 'audio/closedoor.mp3'
    $ renpy.pause()
    scene ep3_139
    with dissolve
    a "Hmn?"
    scene ep3_140
    with dissolve
    mc "Oh... Hey, Aine. Perfect timing. Can you take Naomi to your room and show her what she needs to fix?"
    mc "I think you can explain it better to her than me."
    scene ep3_139
    with dissolve
    a "{i}W-wow! Who is she...? She looks... so pretty...{/i}"
    a "{i}Is she [mc]'s girlfriend?{/i}"
    scene ep3_141
    with dissolve
    n "Oh, so it's in her room?"
    mc "Yeah, she told me her bathtub faucet won't work, but I think she can explain it better."
    n "I gotcha."
    scene ep3_142
    with dissolve
    a "{i}They look so good together... I wonder how long they've been dating...{/i}"
    mc "Aine?"
    a "{i}Wait... why did I just assume that, anyway?{/i}"
    mc "Hey, Aine!"
    scene ep3_143
    with dissolve
    a "Huh? Oh, sorry. What were you saying?"
    mc "Are you okay? You're just standing there staring the whole time."
    a "I-I'm fine. Something just caught my mind for a moment there."
    mc "*sighs* Then would you take Naomi to your room now? Show her what she needs to fix."
    scene ep3_144
    with dissolve
    a "Sure! But, aren't you coming with us?"
    mc "Sorry, but I have to get ready now. It's almost 7 am and I still have to go to work."
    scene ep3_145
    with dissolve
    n "No worries, [mc]. We got this. Just leave it to us."
    mc "Thanks, Naomi."

    scene black
    with dissolve
    with fade

    play sound 'audio/chair.mp3'
    scene ep3_146
    with dissolve
    yt "Alright, everything I need is packed. Now, let's take a shower."
    scene ep3_147
    with dissolve
    yt "......"
    yt "Hold on..."
    yt "I feel like I'm missing something here..."
    yt "Hmmmm..........."
    yt "I think all I need later are just my uniform and some extra clothes just in case..."
    yt "I don't think I'm missing anything but..."
    menu:
        "Think harder":
            $ turnwateroff = True
            scene ep3_148
            with dissolve
            yt "Hmmnnnnn........."
            yt "........"
            yt "............."
            yt "!!!!"
            yt "Oh, right! The main water valve!"
            yt "Naomi must have forgotten about it too. And only Sky and I have the key to the basement anyway."
            yt "I need to turn the valve off quick. It's dangerous if the water suddenly bursts out. Who knows what might happen."

            scene black
            with dissolve
            with fade

            scene ep3_149
            with dissolve
            yt "Alright, let's turn that valve off now."
            yt "Luckily, the bathroom in the hallway has a reserve water tank. I don't need to wait until Naomi is done."
        "Let it be":
            $ turnwateroff = False
            yt "Nahh... I'm just overthinking it. I'll just take my shower now."

    scene black
    with dissolve
    with fade

    play sound 'audio/opendoor.mp3'
    scene ep3_150
    with dissolve
    a "Here's our bathroom."
    scene ep3_151
    with dissolve
    a "I don't really know what happened, because it was working just fine yesterday."
    a "So I was a bit perplexed when I tried to use it earlier and it was not working."
    a "I also noticed that our kitchen sink is taking a long time to drain."
    scene ep3_152
    with dissolve
    n "I see..."
    n "Hmm... I have the right tools to fix the faucet right now."
    n "However, dad didn't inform me of the second issue, so I haven't brought the tools for the sink."
    scene ep3_153
    with dissolve
    n "Sorry, mate. But, I will have to return for it tomorrow."
    n "I still have somethin' to take care of right after this, so I won't be able to come back here today."
    a "Oh, I have no problem with it, but I think you should tell [mc] about it instead of me. I have no authority in this house to be honest."
    scene ep3_154
    with dissolve
    n "Got it."
    a "By the way, my name is Aine. Nice to meet you, Naomi."
    n "Hehe. Nice to meet you too!"
    n "Now let's get the faucet fixed shall we?"
    a "Sure! I'll help you however I can."
    n "Cheers, mate!"
    a "{i}*giggles* She's so nice!{/i}"

    scene black
    with dissolve
    with fadeq

    scene ep3_155
    with dissolve
    n "Before I start, can you please make sure the main water valve is closed off first? It's usually in the basement if you guys have one."
    a "Hmm... I think [mc] is busy right now, so I'll go get Sky instead."
    a "I'll be back in a jiffy!"
    n "Thanks! And just take your time, no need to rush."

    scene black
    with dissolve
    with fadeq

    "A few moments later..."

    scene black
    with dissolve
    with fadeq

    if turnwateroff:
        scene ep3_156
        with dissolve
        a "I'm back!"
        n "All good?"
        a "Yeah! Sky said it was already turned off when she went down the basement. It must have been [mc] who turned it off for you."
        n "I see. I will have to thank him later, then."
        $ naomipoint += 1
        $ renpy.notify(naominotif)
    else:
        scene ep3_156
        with dissolve
        a "I'm back!"
        n "All good?"
        a "Yeah! Sky turned it off for you."
        n "Please give her my thanks later, will you?"
        a "Oh, sure! I will!"

    n "Now let's get this done."

    scene black
    with dissolve
    with fade

    scene ep3_157
    with dissolve
    n "*hums* Hmm... hm hmm.. hmmm..."
    a "{i}She's really pretty no matter how you look at her... I'm sure she's a foreigner with her complexion and the way she speaks.{/i}"
    scene ep3_158
    with dissolve
    n "Hand me the wrench, please, Aine."
    a "Oh..."
    scene ep3_159
    with dissolve
    a "Here!"
    n "Cheers!"
    scene ep3_160
    with dissolve
    n "*hums* Hmm... hm hmm.. hmmm..."
    a "......"
    a ".........."
    scene ep3_161
    with dissolve
    a "By the way, Naomi... Can I ask you something?"
    n "Sure thing, ask away! It would be nice to talk while I'm workin'."
    a "...Then, how old are you?"
    a "{i}She's probably not older than [mc] and I, right?{/i}"
    n "That's easy. I'm 24, how 'bout you?"
    scene ep3_162
    with dissolve
    a "Really?!"
    a "You're a year older than me! I'm 23, but I'm turning 24 this year though."
    n "*giggle* What's with that reaction? Do I look older than my age?"
    scene ep3_163
    with dissolve
    a "Oh, no, no! I didn't mean it like that. To be honest, it's the opposite. You look so young and pretty!"
    n "Why, thanks! You're quite a looker yourself. Hehe."
    a "Ehh... not really..."
    scene ep3_164
    with dissolve
    n "Not so confident, are we?"
    n "That's what we always say when someone tells us that we are pretty."
    n "We may never look at ourselves like that, but to some people, we actually are."
    n "So chin up, 'cuz you're one hell of a neck turner. Hahaha!"
    scene ep3_165
    with dissolve
    a "Well... hehe. Thanks, I guess. *giggles*"
    scene ep3_166
    with dissolve
    a "Do you live around here?"
    n "I do now, but I used to live in the countryside. I spent a lot of years there."
    n "I came to move here recently when dad had an accident and I had to take care of him."
    scene ep3_167
    with dissolve
    a "Oh my... I'm sorry to hear that. What happened? Is he doing fine now?"
    n "Heh... the silly old man fell down the stairs and broke a few bones, but he's alright now."
    n "He's actually your usual repairman here. But I'm takin' over now since he's too old for the job, and the accident he had made it worse."
    a "I see..."
    scene ep3_168
    with dissolve
    n "If you have more questions, don't hesitate to ask, I'd be more than happy to answer them for you."
    a "Yes, I have one last question..."
    a "Uhm..."
    scene ep3_169
    with dissolve
    a "Are you and [mc]..."
    a "I mean... are you guys dating?"
    n "Hmn? What makes ya say that?"
    a "Hmm... I was just looking at you two earlier, and I somehow felt something... but, I don't know..."
    n "D'ya like him?"
    scene ep3_170
    with dissolve
    a "Huh? No, no, no! It's nothing like that!"
    scene ep3_171
    with dissolve
    n "Relax... we're not datin' or anythin'. In fact, we never met each other until just earlier, so rest easy. *giggles*"
    a "Oh, I'm really sorry. I just assumed that out of nowhere."
    a "You two look great together though."
    n "Havin' a commitment, is the last thing I need right now."
    n "I'm not sayin' this in general, but most guys just want the same thing. They approach and date you for that reason."
    n "But once they get what they want and get sick and tired of it, they'll all leave you in the end."
    n "At least, that's what I have seen and heard in most cases. But like I said, I'm not sayin' all guys are like that."
    n "I admit that there are sincere gentlemen out there."
    n "Let's say that [mc] is one of them, but that doesn't mean that he's stayin' like that forever, wouldn't you say?"
    a "You make a fair point..."
    scene ep3_172
    with dissolve
    a "...But, with all the things I've done in the past... I don't know... if I still deserve any attention from anyone."
    n "Hmn? What do you mean by that?"
    scene ep3_173
    with dissolve
    a "Oh... uhh... never mind that. I was just speaking my mind for a moment."
    n "......"
    n "...Let me ask you a question then."
    a "Sure! It's not fair that I'm just asking you, is it? Hehe."
    n "...I don't know what you did in the past. And I don't wanna dig into the life of someone I just met..."
    n "But, do you regret what you've done? You don't have to answer my question if you don't want to."
    scene ep3_174
    with dissolve
    a "......"
    a "...Yes, I deeply regret everything..."
    n "Then that's all that matters, mate."
    n "Imbeciles may say you don't deserve any forgiveness, that you deserved to be punished or you belong in hell."
    n "Don't listen to those folks, everyone deserves a chance to be forgiven. Even criminals are given a second chance."
    scene ep3_175
    with dissolve
    n "The past stays in the past, Aine. Move on, and strive to be a better individual, then do good things from now on."
    a "Thanks for saying that, Naomi. That makes me feel a bit better."
    scene ep3_176
    with dissolve
    n "No worries. Now, the faucet should be workin' properly."
    n "I found out the filter was just clogged up by accumulated dirt, so it wasn't that hard to fix."
    a "You're amazing, Naomi! Do you fix other things too?"
    n "Not everythin', but almost. If ya have problems with anything, just call me and I'll try to get it done for ya."
    n "Just don't call me if 'tis your heart that's broken. 'Cuz I can't help ya with anything in that regard. Haha!"
    a "*giggles* You silly! But hey, that was a pretty good statement earlier, so you might know a lot of things."
    n "I know a thing or two, but I'm not that experienced when it comes to relationships."
    n "Now I will go, or I'll be late for my next stop."
    a "Oh, alright then, let me walk you out."
    n "Cheers!"

    scene black
    with dissolve
    with fade

    scene ep3_177
    with dissolve
    n "It's goodbye for now. But, I'll be back here early tomorrow mornin'."
    scene ep3_178
    with dissolve
    a "Sure thing! I'm looking forward to talking to you again. You've been really nice! Hehe!"
    play sound 'audio/opendoor.mp3'
    "*door opens*"
    scene ep3_179
    with dissolve
    play sound 'audio/closedoor.mp3'
    "*door closed*"
    scene ep3_180
    with dissolve
    a "Hey there, [mc]."
    mc "Oh, are you guys done? Sorry I couldn't check on you guys earlier."
    n "It's all good, no worries. The faucet's all fixed. However, I still have to come back here tomorrow mornin' for the kitchen sink."
    n "I haven't brought the right tools for it. Silly dad for not informin' me about the whole issue."
    n "I just hope your sink can hold on till then. Haha!"
    mc "Well then, I guess we'll have to use the bathroom sink for now. Hahaha!"
    n "I wouldn't do that if I were you. *giggles*"
    mc "Nah... I'm just kidding."
    if turnwateroff:
        n "Thanks for turnin' off the water valve for me, by the way."
        mc "Oh, hehe. You're welcome!"
    n "Are ya goin' to work now?"
    mc "Yep! Why do you ask?"
    n "Why don't ya just come with me? I'll drop ya off, instead."
    menu:
        "Reject":
            $ naomiride = False
            mc "Nah... I really don't want to impose. Plus, the place where I work is just walking distance from here."
            n "Are ya sure?"
            mc "Yeah! Don't worry about me."
            n "Alright then, I'm gonna head out now. I'll see you both tomorrow."
            mc "Take care, Naomi."
            n "Cheers! Ya do the same."
            scene ep3_181
            with dissolve
            mc "I'm going now too, Aine. I'll see you later."
            scene ep3_183
            with dissolve
            a "Ah..."
            scene ep3_184
            with dissolve
            a "Mmn......"
        "Accept":
            $ naomiride = True
            mc "Hehe. Sure, thanks for having me."
            n "Alright then, let's go?"
            mc "Okay!"
            scene ep3_182
            with dissolve
            mc "We're going now, Aine. I'll see you later."
            scene ep3_183
            with dissolve
            a "Ah..."
            scene ep3_184
            with dissolve
            a "Mmn......"

    scene black
    with dissolve
    with fade

    if naomiride:
        scene ep3_185
        with dissolve
        mc "Holy... crap, Naomi!"
        mc "Is this yours?!"
        n "Haha! Not a single part of it."
        n "It's dad's. I just borrowed it so I could get to yer house as fast as I could."
        scene ep3_186
        with dissolve
        mc "Damn! Mr. Scott rocks on this one!"
        mc "Though I must say..."
        menu:
            "It suits you...":
                mc "...it really suits your style somehow."
                n "Haha! Dad told me the same. He wanted to give it to me when I got my driver's license, but he changed his mind."
                n "I guess he doesn't want to let go of his partner just yet."
                n "Silly old man. Hahaha!"
            "You'd look better...":
                mc "...you'd look way better in a smaller car."
                mc "It's just my opinion though, I'm not really judging."
                n "Ya think so?"
                mc "Yeah!"
                n "Dad actually told me that it suits me really well. He wanted to give it to me when I got my driver's license, but he changed his mind."
                n "I guess he doesn't wanna let go of his partner just yet."
                n "Silly old man. Hahaha!"

        scene ep3_185
        with dissolve
        mc "Now that we talked about him..."
        mc "He told me he fell down the stairs and... *sighs*"
        mc "...broke a few bones..."
        mc "Is he going to be alright? I mean... he told me that he's fine. But I know that he just told me that to make me feel better."
        image nmcrtw:
            "ep3_187.jpg"
            pause 3.0
            "ep3_188.jpg"
            pause .2
            repeat
        show nmcrtw
        with dissolve
        n "I heard ya guys talk over the phone. If he tells ya that he's fine, he'll be fine. He'll never lie 'bout things such as his health condition."
        n "He's a man of his word, so just trust him."
        mc "Yeah, I guess so..."
        mc "In any case, I told him that I'll visit him. So I will, once I have time. Is it fine if I come over on the weekend?"
        n "Of course! I don't see why not? It'll be our pleasure to have ya around. Dad seems to really like ya after all."
        mc "Thanks, Naomi."
        n "Hey, no worries!"
        image nmcrtw2:
            "ep3_189.jpg"
            pause 3.0
            "ep3_190.jpg"
            pause .2
            repeat
        show nmcrtw2
        with dissolve
        n "...Oh, by the way, I have been driving for a while, but I don't know where to drop ya off."
        mc "Right, I almost forgot! Please drop me off at 'Woody Burger'. It's near the central plaza."
        n "I gotcha!"
        menu:
            "Ask questions":
                mc "Uhm... is it alright if I ask you some questions?"
                mc "But it's alright if you don't want me to, I don't want to bother you that much since you're driving."
                n "Sure, just ask away! I don't see it as a problem, really."
                mc "Okay. Then..."
                label naomiquestions:
                menu:
                    "About her job":
                        $ noamiaboutjob = True
                        mc "Is this your regular everyday job? I mean, it's not really a typical job a woman would take, you know?"
                        n "Yes it is! To be really honest with ya, I don't just fix things inside the house like what I did earlier. It could be anythin'."
                        n "Electronics, automotive, house maintenance and a lot o' things! However, I do specialize in automobiles."
                        mc "Whoa! That's a lot! So you're basically a Handyman? Or should I say, a Handywoman? Hahaha!"
                        n "Yep! That's me! Haha."
                        mc "That's really impressive if I really think about it! Did you learn all of it from Mr. Scott?"
                        n "Yes, I did. However, there are some things that I learned on my own. Like mobile phones and computers for example."
                        n "Dad is an electrician, but he doesn't have any knowledge about gadgets and stuff."
                        n "And I may specialize in automotive which I picked up from dad, but I majored in Electronics when I was in college."
                        mc "That explains it, yes. But did you really want this job from the beginning?"
                        n "It's not that great of a job, but I would say... it was my dream."
                        n "I watched dad do things here and there when I was little, and I said to myself, 'that's how I wanna be!'. *giggles*"
                        mc "What do you mean 'not that great'? Are you kidding me? That's a lot of things to master, you know?"
                        mc "I would have a hard time doing so if I was in your place."
                        n "Well, we all have our own field of specialization, and I assume that ya do, am I right?"
                        mc "Aside from customer service and cooking burgers? Yes I do. Haha!"
                        mc "I took up Information Technology and specialized as a Systems Analyst. So I'm kinda good with some technical stuff."
                        n "Ooh... that's quite a complicated career path you got there. I'm not shamin' ya, but how come ya work in a burger shack though?"
                        mc "They say the job is pretty in demand, but I don't think so."
                        mc "I ended up working in a burger shack instead because I had trouble finding job vacancies."
                        mc "There may have been some, but they're looking for some experience from you, which I don't have since I was a fresh grad."
                        n "Then how 'bout now? There might be some companies that are willing to accept inexperienced applicants, ya know?"
                        mc "I don't know to be honest... I grew pretty close to the burger shack now. I can't resign just like that."
                        n "Any more particular reasons?"
                        mc "That would be a lot to explain. I'll tell you some other time."
                        n "No worries."
                        jump naomiquestions
                    "About herself":
                        $ noamiaboutself = True
                        mc "Have you been living with Mr. Scott all along? I didn't see you around the last time I visited him."
                        n "No, just moved in a few weeks ago when dad had his accident, and I had to take care of him."
                        n "I used to live with my mom in the countryside, which is a very long way from here."
                        mc "I see... that explains it."
                        mc "Uhh... How old are you though? If you don't mind me asking."
                        n "Hmm... let me guess..."
                        n "You're also 23 years old, right?"
                        mc "Also?"
                        n "Aine and I talked earlier and we shared things about each other."
                        mc "I see. Then, yes. I'm currently 23."
                        n "Hehe. Then I'm a year older than ya."
                        mc "You're older than me?!"
                        mc "Jeez... you look so young too!"
                        n "*giggles* I'll take that as a compliment."
                        jump naomiquestions
                    "End":
                        if (noamiaboutjob and noamiaboutself):
                            $ naomipoint += 1
                            $ renpy.notify(naominotif)
                            mc "That's all for now, and we're getting near midtown, too. We can just continue talking tomorrow."
                            n "Sure! Lookin' forward to it."
                        else:
                            mc "Uhm... I changed my mind. Let's just talk again tomorrow."
                            n "Sure! Lookin' forward to it."
                stop music fadeout 2

                scene black
                with Dissolve(2.0)
                if lilypoint == 2:
                    label thunderchan2:
                    if _in_replay:
                        $ name = persistent.gallery_name
                    scene thunderchan2
                    with dissolve
                    $ renpy.pause()
                    $ renpy.end_replay()
                    play sound 'audio/gamepause.mp3'
                    show title at move_slide
                    with flash
                    $ renpy.notify(imageunlock)
                    $ renpy.pause()
                else:
                    label naomipause:
                    if _in_replay:
                        $ name = persistent.gallery_name
                    scene naomipause
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

            "End the conversation":
                scene black
                with dissolve
                with fade

        play music 'audio/AtTheBar.mp3'
        play sound 'audio/traffic.mp3' loop
        scene ep3_191
        with dissolve
        mc "Thanks for the ride, Naomi."
        n "Anytime, [mc]. I'll see ya again tomorrow."
        mc "Of course! You take care."
        n "Cheers!"

        scene black
        with dissolve
        with fade

        scene ep3_192
        with dissolve
        "*phone vibrates*"
        scene ep3_193
        with dissolve
        mc "......"
        scene ep3_194
        with dissolve
        mc "Good morning, Miss Jess. You called again today, is something up?"
        scene ep3_195
        with dissolve
        j "*huff* Good morning... [mc]. *huff*"
        mc "Hm? Why do you sound like you're out of breath? Are you being chased or something?"
        scene ep3_196
        with dissolve
        j "Phew~!"
        scene ep3_197
        with dissolve
        j "Oh, no. I'm at the central park right now taking a quick jog."
        mc "I see why you sound like you're out of breath."
        j "You know I got to keep up with my health, [mc]. Haha."
        mc "Yeah, I remember what you told me."
        j "Anyway, are you on the way to work right now?"
        mc "Actually, I'm right outside the burger shack. Why do you ask?"
        scene ep3_198
        with dissolve
        j "Oh, jeez... Alright, do you see Lily and Freya inside?"
        mc "Now that you mentioned it, yes, I do."
        scene ep3_199
        with dissolve
        j "Perfect! Just hold on, I'm on my way. Tell them that I want to have a quick meeting with you guys."
        mc "Will do, Miss Jess."
    else:
        play sound 'audio/traffic.mp3' loop
        scene ep3_192
        with dissolve
        "*phone vibrates*"
        scene ep3_193
        with dissolve
        mc "......"
        scene ep3_194
        with dissolve
        mc "Good morning, Miss Jess. You called again today, is something up?"
        scene ep3_195
        with dissolve
        j "*huff* Good morning... [mc]. *huff*"
        mc "Hm? Why do you sound like you're out of breath? Are you being chased or something?"
        scene ep3_196
        with dissolve
        j "Phew~!"
        scene ep3_197
        with dissolve
        j "Oh, no. I'm at central park right now taking a quick jog."
        mc "I see why you sound like you're out of breath."
        j "You know I got to keep up with my health, [mc]. Haha."
        mc "Yeah, I remember what you told me."
        j "Anyway, are you on the way to work right now?"
        mc "Actually, I'm already outside the burger shack. Why do you ask?"
        scene ep3_198
        with dissolve
        j "Oh, jeez... Alright, can you see Lily and Freya inside?"
        mc "Now that you mentioned it, yes, I do."
        scene ep3_199
        with dissolve
        j "Perfect! Just hold on, I'm on my way. Tell them that I want to have a quick meeting with you guys."
        mc "Will do, Miss Jess."
    stop music fadeout 2
    stop sound fadeout 2

    scene black
    with dissolve
    with fade

    play music 'audio/BlackCat.mp3'
    scene ep3_200
    with dissolve
    f "Did you say health problems? Is she sick or something? I didn't know about that, she never told me."
    mc "I should say... 'was'. And it's not something that she hides, really. She told Lily about it too."
    l "Yep! She did when I first applied here."
    scene ep3_201
    with dissolve
    j "Hey~! Good morning to you three!"
    l "Good morning, Miss Jess!"
    f "Morning, Jess!"
    scene ep3_202
    with dissolve
    j "Hmm... you three look up and ready today, which is good! You'll really need it. *giggles*"
    yt "Uh-oh..."
    mc "By the way, Miss Jess. Didn't you say Freya will only be filling in just until Lily gets back to work?"
    scene ep3_203
    with dissolve
    j "Yes, I did! However, I had a change of plans. And that's what I'm about to tell you."
    j "You see, we had an evaluation here yesterday and I saw a great potential in Freya that would improve the business."
    scene ep3_204
    with dissolve
    yt "Huh? Why is she blushing?"
    j "Not only will it ease the workload, but will also improve the workflow significantly."
    l "Really?"
    scene ep3_205
    with dissolve
    j "Yes. So this is what my plan is..."
    j "While Lily and [mc] work as cashiers, Freya will attend to some customers that are in line, to get their orders."
    j "She'll write down the customers' orders, so they can just hand the list to Lily and [mc] when it's their turn to order."
    j "It's not a new workflow that I just came up with, some burger shacks and even restaurants are doing this already."
    j "Which is really efficient if there are a lot of customers waiting to get their food."
    j "She'll also attend to customers wanting to get an extra order. So, she'll be a focus of customer service."
    j "She'll be like the waitress if you compare it to restaurants. We both already talked about this and she agreed to do it."
    l "Wow~! You're really something, Freya."
    l "But, are you sure that you really want to do it? It's a pretty big task!"
    f "Of course! I wanted a real work experience, and this is what I'm looking for. So, I'm really up to the task."
    j "We also have another plan that she volunteered to do herself, but we won't talk about it until she's fully ready."
    scene ep3_206
    with dissolve
    yt "Heeh... I wonder what that is..."
    l "*giggles* I think I know what that is. Right, Freya?"
    scene ep3_207
    with dissolve
    f "Heh!"
    mc "Hmm... I'm already suspicious about you two."
    l "It's our secret, [mc]. You'll find out about it later, so don't worry. *giggles*"
    scene ep3_208
    with dissolve
    mc "Still very suspicious... Hmm......"
    scene ep3_209
    with dissolve
    j "You guys don't have to worry about it for now. We'll start implementing it on Sunday since it's your day off tomorrow."
    j "Now... This is where you'll need most of your energy for today. *giggles*"
    yt "I knew it! Another evaluation!"
    j "We're going to have another evaluation..."
    yt "Yep, I called it!"
    j "...but this time, it's going to be a little bit different."
    l "Eh?"
    mc "How so?"
    j "[mc] will be the one who will observe you two, not me."
    mc "Wait, why me, Miss Jess?"
    j "I told you that I plan to promote you to a manager, but you will have to work for it."
    j "However, I already know that you can do everything in here."
    j "So, we'll start with something that you don't have experience doing, and that is taking my role as the boss here."
    mc "I totally didn't expect that, to be honest."
    scene ep3_210
    with dissolve
    l "You can do it, [mc]. I know that you can. *giggles*"
    l "And to be honest, I'd feel more comfortable if you were the one observing me. Hehe."
    mc "Thanks for saying that, Lily."
    scene ep3_209
    with dissolve
    j "But, don't get me wrong. I'm not promoting you just yet. I just want to see how well you do in taking on my role."
    j "After the evaluation for today, you'll fill me in once you get home with reports through email."
    j "You think you can do it?"
    menu:
        "Positive reply":
            mc "You know me, Miss Jess. I will never back down on a challenge."
            mc "I know how much trust you have in me, and I'll see it through."
            j "Good! That's what I like about you, [mc]. You're always determined to do something once you put your mind to it."
            mc "I'll do my best, Miss Jess."
        "Negative reply":
            mc "I'm not sure how well I'll do, but I will give it a go, Miss Jess."
            j "Don't worry, it's a very easy task compared to what your real job will be once you're promoted to manager."
            j "But I believe that you can do it."
            mc "I'll see what I can do, Miss Jess."
    j "Now I shall take my leave. You guys already know what to do."
    j "And don't forget to send me reports before sundown, alright?"
    mc "Copy!"

    scene black
    with dissolve
    with fadeq

    "A few moments later..."

    scene black
    with dissolve
    with fadeq

    scene ep3_211
    with dissolve
    l "Alright, we're done with the hygiene check, [mc]. We're all set too."
    mc "Good! Now we'll start with the first customer to come in."
    mc "Don't pay any attention to me and just do your thing."
    f "Roger!"
    yt "I think I should remind them of the things I told them last time."
    yt "Should I do it?"
    menu:
        "Let them focus":
            yt "I think I should just let them focus for now. I'm pretty sure they already know what to do."
        "Remind them":
            mc "Remember what I taught you before, Lily?"
            l "Yes, sir! I got this!"
            $ lilypoint += 1
            $ renpy.notify(lilynotif)
            mc "How about you, Freya?"
            f "Eh he he... I'll try to hold it back, but I can't promise."
            $ freyapoint += 1
            $ renpy.notify(freyanotif)
            mc "*sighs* Well, alright. Let's get started."

    scene black
    with dissolve
    with fadeq

    "A few hours later..."

    scene black
    with dissolve
    with fadeq

    scene ep3_212
    with dissolve
    yt "Jeez... What a surprise for me today. I didn't expect this to happen, really."
    yt "I wanted to hide my excitement, but damn... my inner self wants to burst with bliss right now. Hahaha!"
    scene ep3_213
    with dissolve
    yt "Well, today isn't about me, it's about them. So let's focus on them for now."
    scene ep3_214
    with dissolve
    yt "Lily seems to be helping Freya..."
    yt "There's not many customers right now, which is a good opportunity for her to do so."
    scene ep3_215
    with dissolve
    yt "It's only been a few weeks since she started working here, but she's learning at a fast pace which is quite remarkable."
    yt "That is something that I couldn't do myself before."
    yt "Thinking back to when she started her first day here now... it was such a mess. Haha!"
    stop music fadeout 2
    scene ep3_216
    with flash
    mc "*hums* Hmm hmm... hmn hmmm... hm..."
    scene ep3_217
    with dissolve
    mc "Hmn?"
    play music 'audio/Boogie.mp3'
    scene ep3_218
    with dissolve
    l "*sighs* That's the last one on the list..."
    l "None of them want to accept me just because I had a bad record..."
    scene ep3_219
    with dissolve
    l "Aww... I'm now running out of options! What should I do?!"
    yt "Is she just talking to herself?"
    l "....."
    scene ep3_220
    with dissolve
    l "No, Lily! You can do this! Believe in yourself!"
    l "Fight!"
    scene ep3_218
    with dissolve
    l "*sighs* But, I still can't help but feel dejected..."
    scene ep3_219
    with dissolve
    l "Well... Back to searching for job vacancies, I guess..."
    yt "Wait, is she looking for a job?"
    scene ep3_221
    with dissolve
    mc "Hold on, miss!"
    l "Huh?"
    image lmcfbt:
        "ep3_222.jpg"
        pause 3.0
        "ep3_223.jpg"
        pause .2
        repeat
    show lmcfbt
    with dissolve
    l "Oh, can I help you, sir?"
    mc "Uhh... No, not really, but I think I can help you instead."
    mc "I heard you talking just now. You're looking for a job, right?"
    l "Uhm... yes, I am. But I've failed every single job interview so far. And... well... I'm already running out of options."
    mc "That's very unfortunate for you. I'm sorry to hear that."
    mc "But, we're actually looking for someone who can start as soon as possible. I don't know if you will be interested in the job though..."
    mc "Do you want to hear about it?"
    image lmcfbt2:
        "ep3_224.jpg"
        pause 3.0
        "ep3_225.jpg"
        pause .2
        repeat
    show lmcfbt2
    with dissolve
    l "Erm... this isn't another strip club offer, is it?"
    l "There have been guys I met who offered me to work for them in a strip club. I know I'm desperate for a job, but I won't go as far as that."
    mc "Do I look like someone who owns a strip club?"
    l "Uh-huh..."
    mc "Hmm... A strip club would really make a lot of money. But no, don't own nor work in one. Haha!"
    mc "I'm working in a burger shack just a couple of blocks from here, I'm actually on my way there right now. It's called 'Woody Burger'."
    l "Oh, yes. I think I heard of it before."
    mc "Of course, you have. It's the best burger place in town, you know? Hahaha!"
    mc "My senior who has been working for quite some time now, resigned a week ago, and I'm working alone at the moment."
    mc "My boss wants to hire someone as soon as possible because the lack of workforce is affecting the business now."
    show lmcfbt
    with dissolve
    l "But, I didn't see that you guys were hiring when I checked for job vacancies online."
    mc "That's because my boss just decided to list it yesterday when she noticed that a lot of customers are complaining about the slow service."
    mc "And she's not actually in there all the time to begin with."
    mc "I can keep going for a day working alone, but it's a different story if it's a week. Hahaha!"
    mc "So, what do you think? Do you want to give it a go?"
    mc "My boss isn't that strict..."
    mc "Uhh... no, I take it back. She can be quite strict sometimes. But I'm positive you'll pass the interview."
    l "What makes you say that?"
    mc "Absolutely nothing! Hahaha! I just have a feeling that you will."
    l "Well... I'm all out of alternatives, so I guess I'll try and see."
    mc "Great! Let me call my boss now. Let's walk there while I do."
    l "Okay..."

    scene black
    with dissolve
    with fadeq

    scene ep3_226
    with dissolve
    "......"
    ".........."
    mc "Yes, boss. We're on the way to the shop right now."
    "......"
    mc "Alright, we'll wait for you there."
    ".........."
    mc "Copy!"
    "......"
    mc "Thanks, boss! You take care on your way as well."
    scene ep3_227
    with dissolve
    mc "Alright, she's on her way. We'll just have to wait till she gets there."
    l "I'm... getting a bit nervous..."
    mc "Hey, relax! She doesn't bite or anything like that. Haha! I'm pretty sure you'll be fine!"
    l "I'll try..."
    mc "Jeez..."
    mc "Oh, right! By the way, I'm [mc]. Nice to meet you... Uhm..."
    l "Lily. My name is Lily."
    mc "Nice to meet you, Lily!"
    yt "She looks really nervous, I think I should lift her mood somehow."
    mc "I'm glad you trusted and came with me though, not all people will trust somebody they just met."
    mc "Especially in the middle of nowhere like we did. Haha!"
    scene ep3_228
    with dissolve
    l "Well, I can protect myself just in case you do something to me."
    l "I always bring a stun gun with me, you know?"
    scene ep3_229
    with dissolve
    l "But you look like someone I can trust even though you look like a strip club owner, so I guess I won't have to use it today. Haha!"
    mc "I'm not a bad person, I promise."
    yt "A bit shallow, but that made her smile at the very least."
    scene ep3_230
    with dissolve
    mc "I'm very curious tho, are you still studying? Based on your clothes, it's a uniform from a academy near here, right?"
    l "Yes, I'm still finishing up my degree. Though, I'm only taking up a couple of courses at night since I will be working during the day."
    mc "Heeh... That's quite something..."
    mc "I'm guessing that you live alone? Where are your parents? Don't you miss them?"
    scene ep3_231
    with dissolve
    l "...I'm an orphan... both my parents died in a car accident and I'm the only one who survived."
    scene ep3_232
    with dissolve
    mc "Oh sh...! I'm so sorry, I ran off my mouth there. I'm sorry to hear that, Lily. I shouldn't have asked."
    scene ep3_233
    with dissolve
    l "That's alright, it's a truth that I have to face and accept if I want to survive. So I'll just have to keep on moving forward."
    yt "Ahh... jeez... I made her all gloomy again."
    scene ep3_234
    with dissolve
    mc "Hey, Lily."
    l "Hm?"
    mc "What do you call a pig that does karate?"
    l "Uhh... I don't know?"
    scene ep3_235
    with dissolve
    mc "A pork chop!"
    scene ep3_236
    with dissolve
    l "......"
    mc ".........."
    scene ep3_237
    with dissolve
    l "*walks faster*"
    scene ep3_238
    with dissolve
    mc "Hey, wait up~!"
    scene ep3_239
    with dissolve
    l "Pfff!"

    scene black
    with dissolve
    with fade

    scene ep3_240
    with dissolve
    mc "We're here. The boss should be arriving any moment now."
    l "I have never been here before. I usually eat my burgers on the other side of the town."
    mc "Well, damn. You missed some good burgers in your life then."
    mc "I may not eat them all the time, but I still do the quality check, you know? Hahaha!"
    scene ep3_241
    with dissolve
    l "Why not?"
    mc "It's a pretty long story. Haha."
    scene ep3_242
    with dissolve
    j "Hey, [mc]. Good morning!"
    mc "Good morning, boss!"
    scene ep3_243
    with dissolve
    j "I told you to stop calling me boss, didn't I?"
    mc "Eh he hee... Sorry, I'm still not used to it. But I'll try..."
    j "*sighs*"
    scene ep3_244
    with dissolve
    j "Anyway... is she the one?"
    l "G-good morning..."
    mc "Yep! She's the one, indeed."
    scene ep3_245
    with dissolve
    j "Well, alright then. Please come with me."
    j "[mc]. You stay here outside."
    mc "Huh? Why?"
    j "Don't worry about the hygiene check, you can do it later. This will be a girl-to-girl talk. No boys allowed."
    mc "O-okay... if you say so, boss."
    scene ep3_246
    with dissolve
    j "......"
    mc "M-Miss Jess, boss!"
    scene ep3_247
    with dissolve
    j "*sighs*... you're hopeless..."
    scene ep3_248
    with dissolve
    mc "Pssst!"
    scene ep3_249
    with dissolve
    l "Hm?"
    scene ep3_250
    with dissolve
    mc "*whispers* You can do it!"
    l "*nods*"
    scene ep3_251
    with dissolve
    $ renpy.pause()

    scene black
    with dissolve
    with fadeq

    "30 minutes later..."

    scene black
    with dissolve
    with fadeq

    scene ep3_252
    with dissolve
    mc "Oh..."
    mc "Hey, Lily! How did it go?"
    image lmcfbt3:
        "ep3_253.jpg"
        pause 3.0
        "ep3_254.jpg"
        pause .2
        repeat
    show lmcfbt3
    with dissolve
    l "*giggles* I'm hired at last! Finally!"
    mc "Well, congrats, Lily! I'm glad that you made it!"
    l "It was so nerve-wracking at first, but Miss Jess was so kind to me. She helped me to relax and all that."
    mc "Told you so..."
    image lmcfbt4:
        "ep3_255.jpg"
        pause 3.0
        "ep3_256.jpg"
        pause .2
        repeat
    show lmcfbt4
    with dissolve
    l "It's also thanks to you that I finally have a job. Thank you, [mc]."
    mc "Nahh... all I did was to bring you here, you did all the talking yourself. So you shouldn't give me any credit."
    l "If not for you, I wouldn't be here in the first place. So it's still thanks to you."
    mc "You got a point. Haha."
    mc "Well? Chin up now. We're going to work together from now on."
    mc "When do you start?"
    l "Miss Jess wanted me to start as soon as possible so it's going to be tomorrow."
    l "I don't have any experience with this job, so I'm quite nervous about it."
    mc "Hey, that's my job as your senior now. I'll try to guide you however I can."
    l "Thanks, [mc]. I owe you for this."
    mc "No worries! I'm just glad that I could help."
    mc "Are you off to somewhere now?"
    l "Ah, yes! I'm going to the academy to fix my course schedules."
    mc "I see... You take care then, Lily. I'll see you tomorrow?"
    l "Of course! See you tomorrow."
    scene ep3_257
    with dissolve
    j "Quite a lovely and determined girl... I like her."
    scene ep3_258
    with dissolve
    mc "Hm?"
    mc "Oh! Hey boss!"
    j "......"
    mc "...I mean... Miss Jess."
    scene ep3_259
    with dissolve
    j "You're a remarkable employee, [mc]."
    j "Yet, the thing that's as simple as calling me by my name, is the thing that you're having trouble with."
    j "You can still manage by yourself today, right? I wanted to give her some time to at least prepare herself."
    mc "No worries, boss! I-I mean, Miss Jess! Just leave it to me."
    j "That's good to hear."
    j "Alright then, I'm heading off too. You can go and prepare for opening now."
    scene ep3_260
    with dissolve
    mc "Will do, Miss Jess!"
    j "*sighs* Finally."
    mc "Eh he hee..."

    scene black
    with dissolve
    with fadeq

    "Tomorrow morning..."

    scene black
    with dissolve
    with fadeq

    scene ep3_261
    with dissolve
    l "Good morning, [mc]!"
    mc "Good morning! You're quite early, Lily."
    l "I wouldn't want to be late on my first day, would I?"
    mc "That's a fair point."
    mc "And.... hm... you're hair is quite different too."
    l "Oh, because I let it hang down."
    l "Do I look horrible? Haha!"
    mc "Uhh... not really. You look good actually."
    scene ep3_262
    with dissolve
    mc "Anyway, here's an extra key so you don't have to wait for me the next time you get here first."
    l "Thanks!"
    mc "Do you have your uniform already?"
    l "Yep! Miss Jess already gave me some yesterday."
    mc "Good!"
    mc "Shall we go inside then?"
    l "Sure!"

    scene black
    with dissolve
    with fade

    scene ep3_263
    with dissolve
    l "Alright, so what do we do first?"
    mc "There's only one thing we do on every opening, and that's the hygiene check."
    mc "We have to clean the place like wiping all the tables, chairs and mopping the floor."
    mc "But the most important would be making sure everything in the kitchen is nice and tidy, and of course, all clean so the cook won't have a hard time later on."
    l "Got it!"
    l "How about counting the stocks and stuff?"
    mc "Don't worry about that for now, we do that every closing of the place."
    l "I see..."
    mc "For now, you'll do the tables and chairs, I'll mop the floor while you're at it. Then after that, we'll both do the kitchen."
    scene ep3_264
    with dissolve
    l "Roger, boss!"
    scene ep3_265
    with dissolve
    $ renpy.pause()
    scene ep3_266
    with dissolve
    $ renpy.pause()

    scene black
    with dissolve
    with fadeq

    "After cleaning the whole place..."

    scene black
    with dissolve
    with fadeq

    scene ep3_267
    with dissolve
    l "[mc]...? Here's the first batch of burgers ready."
    mc "Good! Just put them in the..."
    mc "Hey, hey! That's a lot! Watch where you're stepping, the floor is still slip-"
    scene ep3_268
    with dissolve
    l "*slips* Whaaa~!"
    menu:
        "Catch her":
            scene ep3_269
            with dissolve
            with hpunch
            mc "Oof! I got you now, don't worry."
            scene ep3_270
            with dissolve
            l "Ehhm... Thanks, [mc]."
            scene ep3_271
            with dissolve
            mc "I told you to watch out, didn't I?"
            l "I'm sorry, I tend to be very clumsy sometimes."
            mc "Did you hurt your foot? Can you stand by yourself?"
            l "I can stand, I'm not hurt or anything, thanks to you."
            mc "Be very cautious next time, alright?"
            l "I will."
        "Don't do it{#ep3,2}":
            scene black
            "*THUD*" with hpunch
            scene ep3_272
            with dissolve
            l "Aww... How clumsy of me..."
            scene ep3_273
            with dissolve
            yt "H-holy mother of panties! I can see them as clear as day!"
            scene ep3_274
            with dissolve
            l "Hmn?"
            scene ep3_275
            with dissolve
            l "Wha-"
            l "D-don't look!"
            mc "I-I didn't see anything!"

    scene black
    with dissolve
    with fadeq

    scene ep3_276
    with dissolve
    l "Aww~! Now I wasted all the burgers! *sighs*"
    l "It's just my first day and I already made such a mess~!"
    mc "Well..."
    mc "I guess, we'll have this cut to your first pay..."
    l "*sighs*"
    scene ep3_277
    with flash
    yt "Yep... it was a mess indeed."
    scene ep3_278
    with dissolve
    yt "But her improving day by day is all I wish for her, really."
    yt "Ahh... I'm getting sidetracked. Let's just focus on observing for now."
    stop music fadeout 2

    scene black
    with Dissolve(2.0)
label lilypause2:
    if _in_replay:
        $ name = persistent.gallery_name
    scene lilypause2
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

    "After the shift..."

    scene black
    with dissolve
    with fadeq

    play music 'audio/AtTheBar.mp3'
    scene ep3_279
    with dissolve
    f "Phew~!"
    l "There weren't many customers today, but it was still pretty hectic."
    f "I couldn't agree more!"
    l "How did we both do, [mc]?"
    mc "Well, I think you guys should clean up first. You're all covered with sweat."
    mc "I'll wait for you two here."
    l "Okay~!"
    l "Let's go, Freya!"
    f "Sure!"

    scene black
    with dissolve
    with fade

    scene ep3_280
    with dissolve
    l "We're back~!"
    mc "You guys sit down first, I won't really take much time since I have to go to the supermarket after this."
    mc "And I still have to submit a report to Miss Jess before sundown."
    image lfmcrt:
        "ep3_281.jpg"
        pause 3.0
        "ep3_282.jpg"
        pause .2
        repeat
    show lfmcrt
    with dissolve
    mc "Well, it's really unfortunate that there wasn't a single irate customer today."
    mc "I really wanted to see how either of you guys handle them now."
    mc "But I saw how you both help each other when you need to."
    mc "And you time it right where you don't have customers on your line, which is good."
    mc "It's not a big deal, but still worth the praise nonetheless."
    mc "Now, let's go with individual performances. There's not much to say, but I think I'll start with Freya."
    menu:
        "Good job":
            $ freyapoint += 1
            $ renpy.notify(freyanotif)
            mc "I think you're a natural at this, Freya."
            mc "There are still some things that you don't know, that's for sure."
            mc "However, the way you handle the customers comes out naturally."
            mc "Just try to hold back your temper when you handle irate customers, and try to learn as much as you can especially if Lily shows you something, alright?"
            f "Of course! I'll try my best!"
            f "But I still can't promise anything about my temper."
            f "That's how I really am. But let's see what I can do about it."
            mc "Good!"
        "Needs improvement":
            mc "You still have a lot to improve, Freya."
            mc "There are a lot of things that you don't know yet, which is understandable since you only worked here for a couple of days."
            mc "But try to learn as much as you can especially if Lily teaches you a thing or two, alright?"
            f "Of course! I'll try my best!"
            f "But I still can't promise anything about my temper. That's how I really am. But let's see what I can about it."
            mc "Good!"

    mc "Now onto Lily's performance..."
    menu:
        "Good job":
            $ lilypoint += 1
            $ renpy.notify(lilynotif)
            mc "Even though I didn't see you handle irate customers like what we practiced last time, you did a good job. Especially when you helped Freya."
            mc "It feels like yesterday that I was helping you when you were in trouble."
            mc "But now, you're the one giving a helping hand."
            mc "It's really important that we help each other. We're workmates after all."
            mc "Just continue on what you've been doing and you'll get there in no time — I can see that you're improving at a fast pace."
            l "Thanks, [mc]! I'm glad I'm living up to your expectations."
        "Needs improvement":
            mc "There's still room for improvement, Lily."
            mc "We need to see how you handle irate customers just like what we practiced last time."
            mc "Things may be a bit hard for you guys right now, but I trust that you guys will improve in no time."
            l "I'll do my best to live up to your expectations, [mc]."
            mc "No pressure, Lily. Just take your time to improve."

    mc "I think I gave you guys pretty short comments. Haha!"
    mc "I also have a lot that I need to improve in order to live up to Miss Jess' expectations."
    mc "So I hope that we keep helping each other."
    l "Of course! I'm lucky enough to have this job, and I won't let it slip through my hands anymore."
    mc "Alright then! That's it for today guys! Should we go now?"
    f "Yeah! Let's!"

    scene black
    with dissolve
    with fade

    scene ep3_283
    with dissolve
    mc "So, where are you guys heading off to?"
    f "I'll be going home today."
    f "I'm a bit sad that I can't see Aine personally this time, but I can just give her a call later."
    yt "So she turned her communication back on again, huh?"
    l "And I will be heading off to the academy as usual. Hehe!"
    l "Lectures are getting complicated now that the exams are close. I need to stay focused."
    mc "Alright, you two take care. I'll be heading to the supermarket now."
    l "It'll be our day off tomorrow, so... see you on Sunday, [mc]!"
    f "Bye~!"
    stop music fadeout 2

    scene black
    with dissolve
    with fade

    play music 'audio/JazzInParis.mp3'
    scene ep3_284
    with dissolve
    un "Good afternoon, sir! Welcome!"
    mc "Good afternoon to you too."
    yt "Hmmm?"
    yt "Yellow hair, yellow eyes... even a yellow tattoo on her face?"
    yt "Wait... is that even allowed?"
    scene ep3_285
    with dissolve
    un "*smiles*"
    yt "I don't know but... I'm getting some kind of... weird vibe from her? Hmm..."
    un "Please leave your backpack here first."
    mc "Oh, right! Sorry."

    scene black
    with dissolve
    with fadeq

    scene ep3_286
    with dissolve
    un "All good, you may enter now, sir."
    mc "Thanks..."
    scene ep3_287
    with dissolve
    yt "I'm definitely getting a feeling that this isn't the first time we've talked to each other..."
    yt "Weird... Because this is the first time I saw her."
    yt "Well, never mind... Must be my mind playing with me."
    scene ep3_288
    with dissolve
    yt "Now what do we need... Hmm... Good thing I wrote a list."
    scene ep3_289
    with dissolve
    yt "Since I'm here, let's go with some drinks first."
    scene ep3_290
    with dissolve
    mc "Ahh... Jeez... It's empty."
    scene ep3_291
    with dissolve
    e "They must have forgotten to fill it up..."
    scene ep3_292
    with dissolve
    mc "Hmm??"
    mc "Emma? What are you doing here?"
    scene ep3_293
    with dissolve
    mc "...And again... what's with the outfit?"
    image emcmsb:
        "ep3_294.jpg"
        pause 3.0
        "ep3_295.jpg"
        pause .2
        repeat
    show emcmsb
    with dissolve
    e "...This is a supermarket, so of course, I'm buying something before I go home."
    mc "Makes sense..."
    e "And Aine made this for me as my uniform..."
    e "Do I look stupid?"
    menu:
        "You look good":
            $ emmapoint += 1
            $ renpy.notify(emmanotif)
            mc "Well, I'd be lying if I say that you do. You're a private investigator, right?"
            mc "You really look the part with that uniform."
        "Yes{#ep3}":
            mc "Well, yes. You definitely look weird, especially with that hat. It makes you look like a pokemon trainer instead of a private investigator."

    e "I see..."
    e "I'm no longer just a private investigator. I recently applied and got accepted in the police division in the city."
    mc "Police division, huh... So... you must be a detective now given that you were a private investigator before?"
    e "Yes."
    mc "Well, I admit, that sounds pretty cool."
    mc "Got any interesting cases lately?"
    e "I handled two cases before, but none at the moment... The city is peaceful as it is right now."
    mc "No strange events whatsoever?"
    mc "Like people disappearing and being kidnapped by some kind of dark entity like in the movies?"
    e "I was a private investigator, not a paranormal expert."
    mc "Heeehh..."
    e "But what would be strange, is us standing in front of this empty cooler for a long period of time..."
    mc "R-Right! I'm going now then, I still have a lot of thing to buy on my list."
    if gwenoutsidetalk:
        scene ep3_296
        with dissolve
        yt "Ooh... Wines, huh? They have a pretty great selection here. I'm sure Gwen will like one of these."
        yt "Should I buy one for her?"
        menu:
            "Buy":
                $ gwenbuywine = True
                scene ep3_297
                with dissolve
                yt "It's pretty expensive! Damn fancy girl!"
                yt "But, yeah! One bottle won't hurt my pocket too much, I guess. Haha!"
                yt "I'm pretty sure this will help lift her mood. She's been kind of depressed every time I've talked to her."
                yt "I still kind of wonder about why she has some regrets about what happened to us though..."
                yt "I just can't get it off my mind..."
            "Don't buy":
                $ gwenbuywine = False
                scene ep3_297
                with dissolve
                yt "Naahh... Probably next time. These are quite expensive. I'll probably bust my pocket with just one of these. Haha!"
                yt "Though... I still kind of wonder about why she has some regrets about what happened to us though..."
                yt "I just can't get it off my mind..."

    scene black
    with dissolve
    with fadeq

    scene ep3_298
    with dissolve
    $ renpy.pause()
    scene ep3_299
    with dissolve
    $ renpy.pause()
    scene ep3_300
    with dissolve
    $ renpy.pause()
    scene ep3_301
    with dissolve
    mc "Hm?"
    scene ep3_302
    with dissolve
    mc "Why do you seem to be following me around?"
    e "I'm not. I'm buying some stuff Aine and I will need later."
    e "I'm looking for something, but I can't seem to find it. I don't know if they have it here."
    mc "What are you looking for then? I'll just help you look for it. You should've just told me earlier."
    scene ep3_303
    with dissolve
    e "Uhm... it's a biscuit called 'Candi'."
    mc "Candi?"
    mc "Yeah, I know where that is. They have it here all the time."
    mc "It should be on the other side. Follow me."
    e "Okay..."
    stop music fadeout 2

    scene black
    with dissolve
    with fade

    scene ep3_304
    with Dissolve(1.0)
    mc "Ahh, yes! That! Haha! I used to eat that all the time as a kid!"
    mc "Kind of brings back some memories... Hmm..."
    scene ep3_305
    with dissolve
    mc "Do you eat that all the time too?"
    scene ep3_306
    with dissolve
    $ renpy.pause()
    scene ep3_307
    with dissolve
    $ renpy.pause()
    scene ep3_308
    with flash
    play music 'audio/BlanketOfStars.mp3'
    e "*sniffs* *sniffs*"
    mc "Here, I got one for you! Stop crying now, okay~?"
    e "O-okay..."
    scene ep3_309
    with flash
    e "......"
    e "...Yes."
    mc "They sure are pretty tasty, right? Haha!"
    e "...Yes. They are..."
    mc "Well then, do you already have what you need?"
    mc "Let's go pay at the cashier so we can go home, I still have a report to submit to my boss before sundown."
    e "Alright..."
    stop music fadeout 2

    scene black
    with dissolve
    with fade

    play music 'audio/JazzInParis.mp3'
    scene ep3_310
    with dissolve
    un "Hello there, sir!"
    mc "W-whoa!"
    mc "You're the cashier too?!"
    un "*giggles* Yes, I am!"
    mc "Are you new here? I never saw you here before. It's also kind of strange that you're working here alone."
    un "Yes, but I'll only be here for tonight's shift."
    un "And as you can see there aren't many customers entering this place at this time. So I'll be fine on my own."
    yt "She kind of reminds me of myself at some point in the past..."
    mc "By the way... have we met... somewhere? I kind of have a feeling that we somehow did."
    un "Hmm... not that I'm sure of myself. Maybe? *giggles*"
    yt "Hrmn... she's kind of suspicious... I don't know why."
    un "Anyway, is this all? Or do you have anything to add?"
    mc "No, I think this is all I need for now."
    un "Okie dokie! Let's get this all sorted out, and please don't forget to retrieve your backpack before you leave."
    mc "No worries."

    scene black
    with dissolve
    with fadeq

    scene ep3_311
    with dissolve
    un "Thank you, sir! Please come again!"
    mc "Will do!"
    scene ep3_312
    with dissolve
    mc "Hey, did that girl looked familiar to you?"
    e "No. That's the first time I saw her. Why?"
    mc "Not that it really matters, but I was getting a feeling that I already met her before."
    mc "Which is... kind of strange..."
    e "It's probably just your imagination."
    mc "Yeah... probably..."
    e "Let's hurry home, the sky is getting darker."
    mc "Well, I hope the rain won't pour down on us soon."
    stop music fadeout 2

    if skypoint == 0:
        scene black
        with Dissolve(2.0)
        label thunderchan4:
        if _in_replay:
            $ name = persistent.gallery_name
        scene thunderchan4
        with dissolve
        $ renpy.pause()
        $ renpy.end_replay()
        play sound 'audio/gamepause.mp3'
        show title at move_slide
        with flash
        $ renpy.notify(imageunlock)
        $ renpy.pause()
    else:
        scene black
        with Dissolve(2.0)
        label emmapause2:
        if _in_replay:
            $ name = persistent.gallery_name
        scene emmapause2
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

    play music 'audio/MBBSax.mp3'
    if gwenbuywine:
        scene ep3_313
        with dissolve
        $ renpy.pause()
        scene ep3_314
        with dissolve
        mc "We're home!"
        mc "Hm? No one's here?"
        g "Oh hey, you're back!"
        scene ep3_315
        with dissolve
        g "Heeh..."
        g "This is the first time I saw you guys together. Are you two dating now or something?"
        scene ep3_316
        play sound 'audio/woosh.mp3'
        mc "Her?"
        scene ep3_317
        mc "Hell no!"
        e "No."
        mc "Why would you just assume that we're dating anyway?!"
        e "What makes you say that?"
        scene ep3_318
        play sound 'audio/woosh.mp3'
        mc "Why are you just paraphrasing what I say?"
        e "I don't know. I'm just talking to Gwen."
        scene ep3_319
        with dissolve
        g "Hey, hey! Relax, I'm just teasing you two. Haha!"
        g "Look, come here!"
        scene ep3_320
        with dissolve
        e "Oh..."
        scene ep3_321
        with dissolve
        mc "Uhmm... what was that for?"
        g "What? Can't I hug my housemates?"
        mc "Well... there's nothing wrong with it, but it was out of nowhere."
        g "Uhh... you're really such a bummer, you know that?"
        e "Uh, I'm going to go change my clothes now. These are really hot."
        g "Sure, go ahead Emma!"
        image gbamcb:
            "ep3_322.jpg"
            pause 3.0
            "ep3_323.jpg"
            pause .2
            repeat
        show gbamcb
        with dissolve
        g "Hey, wanna play billiards with me?"
        mc "I don't think I have time for that, I still have a report to submit to my boss before sundown."
        g "Living up to your boss' expectations, eh?"
        g "Sure, go ahead now."
        mc " Alright, but before I go..."
        scene ep3_324
        with dissolve
        mc "Here."
        g "Heeh~! Isn't this quite an expensive brand? You bought this for me?"
        mc "Well... Aha haaa... Yes."
        image gbamcb2:
            "ep3_325.jpg"
            pause 3.0
            "ep3_326.jpg"
            pause .2
            repeat
        show gbamcb2
        with dissolve
        g "......"
        mc "What?"
        g "Are you trying to hit on me?"
        g "Well, you already did something way more than that, but... really?"
        mc "To be honest, I just bought it on a whim. I saw them in the market and thought that you'd like it, so..."
        g "So, it's not really intentional?"
        mc "Hmm... Not really."
        g "Ohh..."
        image gbamcb3:
            "ep3_327.jpg"
            pause 3.0
            "ep3_328.jpg"
            pause .2
            repeat
        show gbamcb3
        with dissolve
        g "I like it though, so I guess it's fine. Haha!"
        g "If you're planning to hit on me, just tell me, you know? You have nothing to lose anyway. Hahaha!"
        mc "What makes you say that?"
        g "Jeez... You already took my first time, so what's there to hesitate about, right? Hahaha!"
        mc "Uhh... this conversation is getting awkward now..."
        g "Haha, silly! I'm just teasing! Go on now, then. You still have something to do, right?"
        mc "Yeah."
        g "Go get 'em, [mc]."
        scene ep3_329
        with dissolve
        mc "......"
        scene ep3_330
        with dissolve
        mc "Alright. I'll see you later then."
        g "See you later."
        scene ep3_331
        with dissolve
        g "{i}Jeez... Just man up, will you?{/i}"

        scene black
        with dissolve
        with fade

    if aineteachhelp:
        scene ep3_332
        with dissolve
        a "Phew~!"
        s "Excellent, Aine! Good job today! So it was [mc] who told you all that?"
        scene ep3_333
        with dissolve
        a "Yeah, he told me to record my classes and all that. You observing me is still nerve wracking though. Hehe..."
        s "I don't bite, so don't worry about me. Just stay focused on your class next time we do it."
        s "It will probably be next week, so prepare yourself for it."
        a "Yes, ma'am!"
        $ ainepoint += 1
        $ renpy.notify(ainenotif)
        s "Alrighty then. That's all for today. I'll see you later on at dinner?"
        a "Of course! See you later, Sky!"
    else:
        scene ep3_332
        with dissolve
        a "Phew~!"
        s "Excellent, Aine! Good job today."
        scene ep3_333
        with dissolve
        a "You observing me is still nerve wracking though. Hehe... Good thing I managed to relax mid-way."
        s "I don't bite, so don't worry about me. Just stay focused on your class next time we do it."
        s "It will probably next week, so prepare yourself for it."
        a "Yes, ma'am!"
        s "Alrighty then. That's all for today. I'll see you later on dinner?"
        a "Of course! See you later, Sky!"

    scene ep3_334
    with dissolve
    "*phone vibrates*"
    a "{i}Oh, It's Freya.{/i}"
    scene ep3_335
    with dissolve
    a "Hey, Frey! What's up?"
    f "Heya, sis! Oh, wait up. Let me just put the phone on my setup so you can see me better."
    f "There!"
    scene ep3_336
    with dissolve
    f "Hihi! What do you think?"
    a "Oh, wow~! You look so cute, Frey~! I want to hug you so badly~! *giggle*"
    a "Did you made those cat paws yourself?"
    scene ep3_337
    with dissolve
    f "I sewed the poncho myself, but I had someone make the cat paws."
    a "Hmn... you didn't bother mother's seamstress again, did you?"
    f "Errmm... Kind of... Hehe! She was fine with it, so there's nothing to worry about."
    a "Are you sure...? I can see your nose getting longer from here, you know?"
    scene ep3_338
    with dissolve
    f "Oh, come on, sis. I promise. *giggles*"
    a "Well, alright then. As long as she's fine with it."
    a "So how's the house? Anything changed?"
    scene ep3_339
    with dissolve
    f "You know how things are here, sis. It's the same gloomy shithole as usual. Nothing has changed."
    a "Language, Frey!"
    scene ep3_340
    with dissolve
    f "Oops! Sorry..."
    scene ep3_341
    with dissolve
    f "Mom was away for two days now though. That's why I had the opportunity to call you."
    a "Do you have any idea where she went?"
    f "Not a single clue. She doesn't let anyone here know where she's going lately. Not the guards, not Miss Taylor and not even the nanny."
    f "She's probably just with her business partners as usual. Not that I really care."
    scene ep3_342
    with dissolve
    f "Ugh! I want to get out of this place so badly!"
    f "It's always like this! I'm eating alone all the time and there's no one to talk to except for the nanny. But I can't bother her all the time!"
    a "*sighs*... I'm sorry, Frey... I shouldn't have left you alone..."
    scene ep3_343
    with dissolve
    f "Oh, no, no, no! You made the right choice of getting out of here! I couldn't stand what mom was doing to you!"
    scene ep3_342
    with dissolve
    f "Urrgghh! I want to say it! I want to say it so badly! But..."
    a "Ahh... stop it, Frey. I know what you want to say. She's still our mother no matter what she did."
    a "If you want to get out of there, you'll have to finish your studies first, then find a decent job, like what I did."
    a "For sure mother will allow you to."
    scene ep3_344
    with dissolve
    f "Yeah... I know I have to finish my studies first... *sighs*"
    f "After this, I still have college to do. Ugh!"
    a "Whining won't do anything, Frey. I know you can do it. You just have to do your best on your studies."
    a "Promise me that you will."
    scene ep3_345
    with dissolve
    f "Hehe! Alright, I promise to do my best at my studies. Cross my heart!"
    a "Good~!"
    if ainepoint == 8:
        scene ep3_346
        with dissolve
        a "......"
        a "Uhh..."
        a "Hey, Frey?"
        f "Yeah?"
        scene ep3_347
        with dissolve
        a "How do you know if you like someone?"
        f "Hmmnnnn...? *giggles*"
        a "What?"
        f "Heeh... I knew it! You're in love with [mc], aren't you?"
        scene ep3_348
        with dissolve
        a "What?! No, I'm not!"
        f "Sheesh~! I saw you sleeping on his lap looking all comfy, you know?"
        f "I actually never saw you looking so comfortable before, not even once."
        a "Huh?! When did that happen?!"
        f "Uhh... When you guys talked to each other last time?"
        scene ep3_349
        with dissolve
        a "*blushes* I... I... I did that?"
        f "Yepers! I saw it as clear as daylight!"
        f "From the moment he took his hand off your head, and you returned it like a suckling baby finding the nipples. Wahahaha!"
        a "Wait... I did what?!"
        f "You heard me, sis! *giggles*"
        scene ep3_350
        with dissolve
        a "Hrrmmmnnnn...!! But why would you describe it like that?!"
        f "Well, that's how babies normally respond! And you did it like it's a very normal thing to do!"
        a "Ahh! Why did I do that?! That's so embarrassing~!"
        f "*giggles* I like seeing you all flustered, sis. But, I'm actually happy for you."
        scene ep3_351
        with dissolve
        a "Huh? For what?"
        f "'Cuz you finally found love! Wahahaha!"
        scene ep3_352
        with dissolve
        a "Come on~! How many times do I have to tell you that I'm not in love, Frey?!"
        scene ep3_353
        with dissolve
        a "It's just that... I feel so comfortable every time he pats my head..."
        a "It's ridiculous but... I don't know..."
        a "Why would I feel comfortable with someone I mistreated? It's... really weird..."
        f "I have nooo idea. It's hard to put myself into your place, so I can't really say anything."
        scene ep3_354
        with dissolve
        a "...Have you ever wondered how things would be right now if we'd had a different life?"
        a "Like... if we were born into a different family or something like that?"
        f "Hmmm... I haven't, but... I think you and [mc] would already be married by now if that was the case. Ahahaha!"
        scene ep3_355
        with dissolve
        a "*sighs* There you go again with the marrying and stuff. Can we not talk about it for now, please?"
        f "Oops! Sorry. Hehe! I just like teasing you, sis."
        a "*sighs*"
        f "But, if you really want advice from me, then..."
        f "...Why don't you guys have sex?"
        a "Oh... that's..."
        show ep3_356
        with hpunch
        a "Wait, what did you just say?!"
        f "Sex! You know? Like what they do in porn videos and stuff?"
        a "P-porn videos?!"
        scene ep3_357
        with dissolve
        a "Ugh! I'm speechless, Frey! Where did you get that stupid idea, anyway?!"
        f "A professional told me that it's a very effective way to determine your feelings for a person!"
        f "It's apparently a tested and proven method! *giggles*"
        scene ep3_358
        with dissolve
        a "And who's this professional you're speaking of? I'm going to kill that person right this second!"
        f "Wahaha! Relax, sis! I'm just kidding! That's just what most people do nowadays, you know?"
        scene ep3_359
        with dissolve
        a "Most people?"
        f "And like you're capable of killing a person anyway. Hahaha!"
        scene ep3_360
        with dissolve
        a "Oh god... You literally just blew my mind, Frey. I don't know what to say..."
        f "Well? Suit yourself~! I'm not an expert, so that's all I can say. Wahahaha!"
        a "*sighs* You're always up to no good..."
        f "Hey, I'm just trying to help!"
        f "Plus, he already saw you naked and squeezed your jugs! So what are you hesitating for?"
        play sound 'audio/woosh.mp3'
        show ep3_361
        a "That's not how it works! You're supposed to get married first before doing something like that!"
        f "Gaaah! Were you born in the 1940s or what? We're in the 21st century, sis!"
        f "Things like getting married before having sex don't exist anymore!"
        a "No! I'm not going to do it! That's a ridiculous idea just to confirm what I feel!"
        f "......"
        f "Hmmmnnn?"
        f "Wahahahahahaha!"
        scene ep3_362
        with dissolve
        a "What? What are you laughing so hard for?"
        f "I gotcha, sis~! You definitely have something for him no matter how little!"
        scene ep3_363
        with dissolve
        a "*gasps*"
        a "Wha..."
        scene ep3_364
        with dissolve
        a "W-w-what did I just..."
        f "Wahahahaha! I'm off to my stream then, sis! Byieee~!"
        scene ep3_365
        with dissolve
        a "Wha... no, no, no! Don't just leave me like that!"
        f "Byeeee~!"
        show ep3_366
        with hpunch
        a "Freyaaaaa~!!"
        "*click*"
        scene ep3_367
        with dissolve
        a "Awww... *sniffs*"
        play sound 'audio/opendoor.mp3'
        scene ep3_368
        with dissolve
        mc "Hey, why are you shouting your sister's name like she's about to die or something?! What happened?!"
        a "!!!!"
        mc "We're already cooking for dinner, you should..."
        scene ep3_369
        with dissolve
        mc "Wait... are you crying?!"
        scene ep3_370
        with dissolve
        a "N-n-no! I-I'm fine!"
        mc "Huh??"

        scene black
        with dissolve
        with fade
    else:
        f "Gonna go now then, sis! I just called to show you my new costume."
        f "It's a good opportunity for me to stream today since mom is away, no one's going to bother me. Hehe!"
        a "You're still streaming games? Well, alright then. Have fun, Frey."
        f "Bye~!"

        scene black
        with dissolve
        with fade

    "After dinner..."

    scene black
    with dissolve
    with fadeq

    play sound 'audio/closedoor.mp3'
    scene ep3_371
    with dissolve
    mc "*yawns*..."
    g "Sleepy already, eh?"
    mc "Yeah... the report I submitted to my boss took a lot out of me."
    g "Well, sleeping right after eating is bad for your health. Why don't we watch a movie first before heading to bed?"
    scene ep3_372
    with dissolve
    mc "A movie? Well... yeah, sure. Why not?"
    scene ep3_373
    with dissolve
    g "How about you guys? Want to join us for a movie?"
    scene ep3_374
    with dissolve
    s "Hmm... sure! Just one movie though. I'm pretty tired after today's work."
    a "Me too."
    e "Same..."
    g "Ehh... I'm the only one out of the loop here. Well, no matter. Let's go~!"

    scene black
    with dissolve
    with fade

    scene ep3_375
    with dissolve
    mc "So, what are we watching? It won't be a romantic movie like what you're always watching, right?"
    g "Considering most of us here like anime, why don't we watch an anime movie?"
    mc "Heeh... You didn't watch anime before."
    g "I don't, but I don't hate them. I found this movie called 'Hello World', and the trailer seems interesting."
    g "So, I kind of want to check it out."
    mc "Let me guess... a romantic genre?"
    g "Bingo! Haha!"
    scene ep3_376
    with dissolve
    g "What do you guys think?"
    mc "Well, as long as it's an anime, it should be fine to me."
    s "Yeah, let's watch it!"
    g "How about you two?"
    a "Sure!"
    e "Mhm."
    g "Alright, here goes nothing!"

    scene black
    with dissolve
    with fadeq

    "An hour later..."

    scene black
    with dissolve
    with fadeq

    if gwenbuywine:
        scene ep3_377
        with dissolve
        g "Well..."
        g "They all dropped off one by one. Hahaha!"
        g "Everyone seemed really tired today, huh?"
        g "As the owner of a company, it's nice to see you guys doing your best in your jobs."
        g "Just make sure you don't overdo yourselves, alright?"
        mc "......"
        scene ep3_378
        with dissolve
        g "Hmn?"
        scene ep3_379
        with dissolve
        g "*sighs*..."
        scene ep3_380
        with dissolve
        g "Hey..."
        mc "Mmnn..."
        g "Hey, wake up!"
        scene ep3_381
        with dissolve
        mc "Hm?"
        scene ep3_382
        with dissolve
        mc "Oh, did I fall asleep?"
        g "You obviously did, you silly."
        mc "Is the movie done already?"
        g "No, not yet. I think we're still halfway through it."
        g "Was it boring or something?"
        mc "I don't know, I slept 30 minutes through the movie."
        mc "Did the others go to bed already?"
        g "Yeah, Emma just went ahead not too long ago."
        mc "I see..."
        g "Hmmnn..."
        scene ep3_383
        with dissolve
        g "Oh, hey! Wanna come to my room? I want to show you something."
        mc "To your room? What do you want to show me, though?"
        g "It's a surprise! Haha! So, what do you think?"
        menu:
            "Agree":
                $ gwenroomaccess = True
                mc "Uhm... Alright. But don't blame me if I fall asleep in your room."
                g "Jeez! That's not a problem at all! You can sleep there as much as you want, you know?"
                mc "What?"
                g "Hahaha! Never mind."
                g "Come on! Let's go before you fall asleep again."
            "Go to sleep":
                $ gwenroomaccess = False
                mc "Uhm... I think I'll go to sleep for now. I'm sleepy as fuck, I don't want to sleep in your room, you know?"
                g "Jeez! You're really such a bummer!"
                g "Well, alright then. I'll stay here until I'm done with the movie."
                mc "Be sure to turn off the TV when you're done."
                g "Will do! Good night, [mc]."
                mc "Good night."
    else:
        scene ep3_377
        with dissolve
        g "Well..."
        g "They all dropped off one by one. Hahaha!"
        g "Everyone seemed really tired today, huh?"
        g "As the owner of a company, it's nice to see you guys doing your best in your jobs."
        g "Just make sure you don't overdo yourselves, alright?"
        mc "......"
        scene ep3_378
        with dissolve
        g "Hmn?"
        scene ep3_379
        with dissolve
        g "*sighs*..."
        scene ep3_380
        with dissolve
        g "Hey..."
        mc "Mmnn..."
        g "Hey, wake up!"
        scene ep3_381
        with dissolve
        mc "Hm?"
        scene ep3_382
        with dissolve
        mc "Oh, did I fall asleep?"
        g "You obviously did, you silly."
        mc "Is the movie done already?"
        g "No, not yet. I think we're still halfway through it."
        g "Don't mind me, just go sleep already if you're that sleepy."
        mc "Will you be fine here alone?"
        g "Of course! I don't really mind."
        mc "Alright then. I'll go upstairs now. Be sure to turn off the TV when you're done."
        g "Will do! Good night, [mc]."
        mc "Good night."

    scene black
    with dissolve
    with fade

    if gwenroomaccess:
        play sound 'audio/closedoor.mp3'
        scene ep3_384
        with dissolve
        g "Everything is still a little bit messy, but here we are!"
        g "Welcome! Haha!"
        mc "......"
        scene ep3_385
        with dissolve
        mc "...Whoa~! Holy cow!"
        scene ep3_386
        with dissolve
        mc "A piano and three guitars?! Are they yours?! When did you move these in here?"
        g "That's a silly question after seeing them in my room. Haha!"
        g "But, yeah. They're mine. I had them since high school, you know?"
        g "You were at work when the moving company delivered them here."
        mc "For real? They look like brand new!"
        g "Yep, for real! I take care of them like my own babies."
        mc "But I never saw you bring a guitar or play any of them before!"
        g "Well, I can play them, but I'm not that good. So I'm not really proud to show it off. Haha."
        mc "Ehh... why did you show me then?"
        g "Nothing! Haha! Maybe to surprise you in hopes of waking you up?"
        mc "Well, it worked. So I'll give you that. Haha."
        scene ep3_387
        with dissolve
        mc "This grand piano though..."
        g "Hmn? What about it?"
        mc "......"
        mc "It brings back some memories..."
        g "Heeh~ Can you play it?"
        mc "A little bit, yes. Pretty much just the basics of it. We used to have one and Klara used to play it."
        mc "And I have a bit of preference for classical music, so..."
        g "Well? Give it a try!"
        mc "Naah... Maybe next time. I'm too tired to focus right now. Haha."
        g "That's unfortunate. It's supposed to be your chance to show off to me. Now you just lost it. Hahaha!"
        scene ep3_388
        with dissolve
        mc "Uhh......"
        g "Jeez! Relax! I'm just messing with you! I just like seeing your stupid face every time I do! Hahaha!"
        mc "*sighs* Your personality hasn't changed at all."
        mc "You can be serious and playful any time you wanted to."
        scene ep3_389
        with dissolve
        g "So you're saying that you really know me well, then?"
        image grmcts:
            "ep3_390.jpg"
            pause 3.0
            "ep3_391.jpg"
            pause .2
            repeat
        show grmcts
        with dissolve
        mc "Considering what I just discovered?"
        mc "Nope. I don't know what more secrets you have up your sleeve, to be honest."
        mc "I never saw you as a person who plays instruments, let alone like them."
        mc "I just perceived you as a drunkard and... well... someone who smokes."
        mc "I was even surprised to know that you own a company."
        mc "I never in my life thought that you would be this successful in life, you know?"
        g "I 'was' successful, but now, I'm nothing but a regular jobless person. Hahaha!"
        mc "I like that you just laugh through your problems. You were all gloomy the last times we talked, so what happened?"
        g "Well, brooding about it won't really help me."
        g"The problem is already a problem, so instead of thinking about the problem, I'll just think about the solution."
        mc "Got anything so far, then?"
        g "Absolutely nothing! Hahaha!"
        mc "You're crazy..."
        g "Let's not talk about that, shall we?"
        g "All I want for now is to relax and take my mind off of all the stress it caused me before going out there again for another journey."
        mc "Heeh... that's a bit poetic right there. You're not the type Gwen, so stop it. Haha."
        g "Sheesh! Alright~"
        mc "If you want to relax, then why don't you play the guitar for us? I bet you know some relaxing songs, yeah?"
        g "Oh, sure! Why not? Let me just get it down."
        stop music fadeout 2

        scene black
        with dissolve
        with fade

        scene ep3_392
        with dissolve
        g "I'll play this one. I don't want to wake everyone with the electric guitars. Haha!"
        mc "Acoustic guitars are more suitable for relaxing songs, so..."
        g "I have a couple of songs in mind though. I don't know which one to play."
        mc "Just play whichever you think is best."
        g "Okay then, are you ready?"
        mc "Go on..."
        play music 'audio/MaySong.mp3'
        scene ep3_393
        with dissolve
        g "......"
        mc "Oh, nice..."
        g "You like that tune?"
        mc "Yeah..."
        scene ep3_394
        with dissolve
        g "......"
        g "I have... a lot of memories with this song..."
        mc "Hmmm..."
        g "You know, when I was a kid, this is a song Dad used to play a lot..."
        g "...Me lying on mom's lap... while she brushed my hair until I fell asleep..."
        g "...We were all living in bliss, like one happy family would... until..."
        mc "Until...?"
        g "......"
        g "...Never mind. I don't want to break the mood. Haha."
        mc "That's fine."

        scene black
        with dissolve
        with fadeq

        "A few moments later..."

        scene black
        with dissolve
        with fadeq
        label gwenhandjob:
        if _in_replay:
            $ name = persistent.gallery_name
        scene ep3_395
        with dissolve
        g "And that's it."
        g "Next time you could at least play the pia-"
        scene ep3_396
        with dissolve
        mc "......"
        mc "*snore*..."
        g "Jeez... what a kid."
        scene ep3_397
        with dissolve
        g "Come here, will you?"
        scene ep3_398
        with dissolve
        g "......"
        mc "......"
        g "......"
        g ".........."
        g ".............."
        g "*sighs*"
        g "...You know... I was kind of wondering why you didn't pursue me after what happened to us back then..."
        g "...I know we just shrugged it off like nothing happened... but... you're the guy, you know?"
        g "...Like... I knew that you had something for me after that, even up to now..."
        g "...I know you didn't buy that wine for me just on a whim, you stupid..."
        g "......"
        g "...or..."
        g "Do you... still like Aine?"
        g "......"
        scene ep3_399
        with dissolve
        g "I..."
        g "Have been waiting for you to man up for me..."
        scene ep3_400
        with dissolve
        g "...you idiot..."
        scene ep3_401
        with dissolve
        g "*kisses*"
        g "{i}Ahh... I knew this would happen if I brought you here...{/i}"
        g "...Mnnhh..."
        mc "......"
        scene ep3_402
        with dissolve
        mc "...Mmm?"
        scene ep3_403
        with dissolve
        mc "!!!!"
        yt "Gwen?!"
        yt "W-why is she... kissing me?"
        yt "I fell asleep... I don't know what happened!"
        scene ep3_404
        with dissolve
        mc "Gwen... what are we..."
        g "*breathes heavily*"
        g "......"
        g "*giggles*"
        g "Do you... want me to continue?"
        mc "I don't know Gwen... I..."
        g "Remember what I told you last night?"
        g "I told you that it's alright to follow your heart, right?"
        yt "Shit... what do I even do here?"
        menu:
            "Let her continue":
                $ gwenroute = True
                mc "Mhm!"
                g "*giggles* I remember you had the exact same response when I asked you back then."
                g "Well then..."
                scene ep3_405
                g "*kisses*"
                g "Mnnhh~ [mc]..."
                scene ep3_406
                with dissolve
                mc "......"
                g "{i}Yeah... you do have something for me... Even after all these years...{/i}"
                yt "...this feeling..."
                yt "...is so familiar..."
                scene i210
                with flash
                $ renpy.pause()
                scene ep3_406
                with flash
                yt "Why do I get a feeling... that I... have been missing this?"
                yt "I... don't understand..."
                scene ep3_407
                with dissolve
                g "Mnnhhhh~! Haahh~"
                g "*licks*"
                mc "*slurps*"
                g "......"
                scene ep3_408
                with dissolve
                g "{i}He's already so hard..."
                g"{i}Ahh... I want to go further.{/i}"
                stop music fadeout 1

                scene black
                with dissolve
                with fadeq

                play music 'audio/Woho.mp3'
                scene ep3_409
                with dissolve
                g "[mc], I want to try this."
                mc "Have you tried doing it before?"
                g "Of course not, you silly. You're the only man who ever touched me before. That's why I said I'll 'try' it, right?"
                mc "I see... Alright then."
                show gwen4
                with dissolve
                $ renpy.pause()
                mc "Ahh..."
                g "How's that?"
                mc "It feels good! K-keep going."
                g "Alright~"
                $ renpy.pause()
                show gwen5
                with dissolve
                $ renpy.pause()
                g "Cumming soon?"
                mc "Not yet, I think you have to put more effort in it."
                g "Sheesh! You sure make it hard, eh? Alright then."
                $ renpy.pause()
                show gwen6
                with dissolve
                $ renpy.pause()
                mc "Yeah, that's it, Gwen."
                g "You like that?"
                mc "Y-yeah!"
                g "You're throbbing real hard now. Are you about to cum?"
                mc "Ahh... Almost there!"
                g "*giggles*"
                $ renpy.pause()
                show ep3_410
                with hpunch
                mc "Arrrgghh!"
                mc "Wait, why did you..."
                scene ep3_411
                with dissolve
                g "Ahh..."
                scene ep3_412
                with dissolve
                g "*swallows*"
                scene ep3_413
                with dissolve
                g "Hmm... it doesn't taste half bad."
                g "I like it, to be honest."
                mc "You're one daring girl, I'll give you that."
                g "Well, thanks!"
                scene ep3_414
                with dissolve
                g "Now... let's continue, shall we?"
                g "You can still go for another round, right?"
                mc "Uhm... yeah?"
                g "Okay, let me just..."
                scene ep3_415
                with dissolve
                $ renpy.pause()
                scene ep3_416
                with dissolve
                $ renpy.pause()
                scene ep3_417
                with dissolve
                $ renpy.pause()
                scene ep3_418
                with dissolve
                $ renpy.pause()
                scene ep3_419
                with dissolve
                $ renpy.pause()
                scene ep3_420
                with dissolve
                g "Let's do it again, [mc]. I'm so horny now."
                mc "But didn't you said that you regretted doing it with me before?"
                scene ep3_421
                with dissolve
                g "Hey, focus on the task at hand, mister!"
                mc "Oh, eeh... okay..."
                scene ep3_422
                with dissolve
                g "Now, let's put it-"
                stop music
                play sound 'audio/doorknock.mp3'
                "*knocks*" with hpunch
                e "Gwen, are you still up?"
                scene ep3_421
                with dissolve
                g "*gasps*!"
                g "*whispers* I forgot to lock the door!"
                mc "*whisper* Oh, shit!"
                g "*whispers* Quick! Hide in the closet!"
                mc "*whispers* Ehh? I can just-"
                g "*whispers* Just hide, you idiot!"
                mc "*whispers* A-alright."

                scene black
                with dissolve
                with fadeq

                play sound 'audio/opendoor.mp3'
                scene ep3_423
                with dissolve
                g "Hey, Em! What's up?"
                e "Do you still have the towels we were using back in our previous apartment?"
                e "Aine said you have them."
                g "Oh, the old towels? Yes, I have them. Just wait a sec."

                scene black
                with dissolve
                with fadeq

                scene ep3_424
                with dissolve
                g "Here."
                e "Thanks."
                g "Goodnight, Em!"
                e "Good night."
                play sound 'audio/closedoor.mp3'
                scene ep3_425
                with dissolve
                "*door closed*"
                g "Phew~!"
                scene ep3_426
                with dissolve
                g "You can come out now."
                scene ep3_427
                with dissolve
                mc "Is she gone?"
                g "Yeah..."
                mc "Jeez..."
                scene ep3_428
                with dissolve
                g "*sighs* Why does she have to be such a cock blocker~"
                mc "Well, nothing we can do about it now."
                scene ep3_429
                with dissolve
                g "Let's just continue where we left next time, alright?"
                mc "Next time?"
                scene ep3_430
                with dissolve
                g "......"
                mc "......"
                g "......"
                mc "Alright, alright... I know what you mean."
                scene ep3_431
                with dissolve
                g "*sighs* Let's just go to sleep, shall we?"
                mc "Okay, see you tomorrow."
                g "Good night, [mc]. You rest well."
                mc "Good night."
            "Stop it":
                $ gwenroute = False
                mc "I... I think we should stop this now, Gwen."
                g "Ohh..."
                mc "I'm sorry. I..."
                g "Shhh... No need to explain. I don't really mind if that's what you really want."
                g "I can't really force you to something you don't want, can I?"
                g "Let's just forget this happened and just go to sleep."
                mc "Yeah, you're right."
        $ renpy.end_replay()
    stop music fadeout 2

    scene black
    with dissolve
    with fade

    play music 'audio/JourneyHome.mp3'
    scene ep3_432
    with dissolve
    g "*hum* Hmm hmn... hm... hmmmm..."
    "*class murmuring*..."
    scene ep3_433
    with dissolve
    st1 "Hey, hey... Did [mc] just confess to Aine?"
    st1 "Damn! I like his guts bro! Not everyone has the courage to even approach her!"
    st2 "Well, he got dumped like the others and got the worst outcome possible."
    st1 "I think you have a good chance bro, why don't you confess to her next? You have the money and the looks!"
    st2 "Jesus Christ, no! Have you forgotten all those big shot students who confessed to her?"
    st1 "Uhh... they all got dumped?"
    st2 "Yeah, you stupid! Even those guys got dumped, so what's even the point of me trying?"
    st1 "Well, who knows... she might find you different from the others and accept you, you know?"
    st2 "And what's the difference between me and them?"
    st1 "What else? Your failing marks, of course! Hahaha!"
    st2 "Well fuck you, dude!"
    g "{i}Hmn? What's happening here?{/i}"
    scene ep3_434
    with dissolve
    a "Ugh! You disgusting creature! Who do you think you are, you glutton!"
    a "From now on your name shall be Fatso! Sounds very fitting for someone like you!"
    mc "*sniffs* W-why would you do that to me...?"
    a "Listen to me, everyone! From now-"
    scene ep3_435
    g "No! Stop it, Aine... That's going way too far."

    jump ep4

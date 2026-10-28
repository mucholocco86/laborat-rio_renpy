default lilyhug = False
default skywear = False
#default skyroute = False

label ep2:
    stop music fadeout 2
    scene eoep1
    with dissolve
    $ renpy.pause()
    scene ep2
    with dissolve
    $ renpy.pause()

    play music 'audio/Tryout.mp3'
    scene i312
    with dissolve
    yt "Fuuuck... it still hurts like hell!"
    yt "Why does she have to slap me like that?!"
    yt "It's not like I actually wanted to do that. I was half asleep!"
    yt "*sighs*... Well, at least she's not angry..."
    scene i313
    with dissolve
    yt "...My hands... on Aine's..."
    yt "Damn... Now that's what I call {b}experience{/b}!"
    yt "......"
    scene i314
    with dissolve
    yt "Oh, well... back into the game."
    scene i315
    with dissolve
    yt "So, 'My Real Desire' by Lyk4n, huh?"
    yt "It's not all the time that I play this kind of game, but this seems pretty good!"
    yt "I really like this character named Krystal..."
    scene i316
    with dissolve
    yt "What a tragic past she has. Compared to her, my experience of being bullied is nothing."
    yt "I can't imagine myself being in her place at all! If I was, I would probably just kill myself rather than experience things like she did."
    scene i317
    with dissolve
    yt "The main character did a really good job of getting her out of her shell too!"
    yt "Not only that. The main story is also pretty interesting. I hope this guy gets what he really desires."
    yt "......"
    scene i318
    with dissolve
    yt "Now that I think about it..."
    yt "...Do I even have a real desire?"
    yt "Probably get my dream job of working in a company?"
    yt "I would probably be happy if I did, but... I feel something is still lacking."
    yt "I just can't put my finger on what it is."
    yt "Oh, well... I already finished the latest update. I can't wait to play the upcoming one."
    yt "I should go to sleep now."

    scene black
    with dissolve
    with fade

    scene i319
    with dissolve
    $ renpy.pause()
    scene i320
    with dissolve
    yt "Hm? Sky's not here to wake me up?"
    yt "......"
    if skyroute:
        yt "Oh, damn... I already got used to her coming here every morning."
        yt "I really have been longing for her care. It's like I'm falling in love with her or something. *sighs*"
    else:
        yt "Oh, damn... I've gotten used to her coming here every morning. Even though I rejected her that time. I still couldn't help it."

    yt "What is she doing, though? This is the first time that she didn't come here to wake me up."

    scene black
    with dissolve
    with fade

    scene i321
    with dissolve
    play sound 'audio/doorknock.mp3'
    mc "*knocks*"
    mc "Sky? I'm going to work!"
    "......"
    yt "She's not answering."
    scene i322
    with dissolve
    yt "Her door seems open, though. Should I enter to check on her?"
    menu:
        "Enter{#ep2}":
            play sound 'audio/closedoor.mp3'
            scene i323
            with dissolve
            mc "Sky?"
            yt "Oh, she's still sleeping..."
            yt "She might have been really busy last night."
            if skycelebrate:
                yt "I have to take her somewhere she can relax on our 'date'..."
                yt "......"
                yt "Well, she wanted to call it a date, so be it. Haha!"
            scene i324
            with dissolve
            mc "Sky... I'm going to work now."
            scene i325
            with dissolve
            mc "*kisses*"
            $ skypoint += 1
            $ renpy.notify(skynotif)
            scene i324
            with dissolve
            yt "I'll just let her sleep for now. Let's go to work."
            scene i326
            with dissolve
            $ renpy.pause()
            scene i327
            with dissolve
            s "*thump*"
            scene i328
            with dissolve
            s "......"
            scene i329
            with dissolve
            s "{i}It's... getting really hard to hold back now...{/i}"
        "Just go to work":
            yt "She's probably still asleep. She might have been really busy last night."
            yt "I'll just let her rest and go to work instead."
    stop music fadeout 2

    scene black
    with dissolve
    with fade

    play music 'audio/Twenties.mp3'
    play sound 'audio/traffic.mp3' fadein 2 loop
    scene i330
    with dissolve
    $ renpy.pause()
    scene i331
    with dissolve
    "*phone vibrates*"
    scene i332
    with dissolve
    yt "Miss Jess? It's pretty rare for her to call me. Something is definitely up..."
    scene i333
    with dissolve
    mc "Good morning, Miss Jess."
    j "Good morning, [mc]. I'm sorry, but I have bad news for you."
    yt "Yep, there it is..."
    mc "Bad news? What happened?"
    j "Lily won't be able to come to work today. She called me earlier to inform me and I told her to take an emergency leave."
    j "She has a fever right now. I just went to her house to check on her and it seems not that bad. Still, I won't risk my employee's health."
    j "Sorry, [mc]... but can you please help the person filling in for her?"
    mc "No worries, Miss Jess. Just leave it to me!"
    scene i334
    with dissolve
    mc "Wait... someone's filling in for her shift?"
    j "Yes."
    j "I know that you can handle a full shift on your own. But, I won't risk having you overheating on me too."
    mc "I see, that's understandable. So, who's this new guy?"
    j "A woman, [mc]. But, be careful with her. She's young and inexperienced with the job."
    j "She begged me to let her fill in for Lily since she doesn't rely on her family for financial support, so I couldn't say no."
    mc "...Do you guys know each other?"
    j "Yes, we know each other."
    j "She did a lot of odd jobs before, but with this kind of job... Her experience is way less than Lily."
    j "I must warn you, she's really quick to blow a fuse."
    yt "Uh-oh... Looks like this could be a very long day~"
    j "And one more thing..."
    j "I'm not sure how long till Lily recovers. So, until she can manage, Freya will be filling up for her."
    mc "So her name is Freya, huh?"
    j "Yes. She's probably there now. You should go and meet her."
    mc "Alright. Just leave everything to me."
    j "Thank you, [mc]. I knew I could depend on you. Maybe one day, you'll earn yourself a promotion."
    j "I make no promises though. You have to sweat for it."
    yt "A promotion?! Miss Jess really knows how to lift her employee's spirits! Haha!"
    mc "And that I will do, Miss Jess."
    j "Good! I have to go now. I still have to meet someone."
    mc "Alright. Please take care!"
    scene i335
    with dissolve
    yt "I hope Lily is okay..."
    yt "Well, knowing her, she'll definitely be fine."
    yt "But, I'm still worried about her. Should I go and give her a quick visit later?"
    menu:
        "Pay her a visit":
            $ lilyvisit =  True
            yt "Yeah, I should! But I need to tell her first before I go there."
            yt "Let's send her a message right now."
        "Give her time to rest":
            $ lilyvisit =  False
            yt "Hmm..."
            yt "I'll just give her some time to rest for now."
    stop music fadeout 2
    stop sound fadeout 2

    scene black
    with dissolve
    with fade

    play music 'audio/BlackCat.mp3'
    scene i336
    with dissolve
    f "Heeeey~ Good morning, partner!"
    yt "Partner?"
    menu:
        "Greet her back":
            $ freyapoint += 1
            $ renpy.notify(freyanotif)
            scene i337
            with dissolve
            mc "Good morning, you must be Freya. Nice to meet you."
            f "Nice to meet you too... Uhm..."
            mc "[mc]. My name is [mc]."
            f "Hehe~ Nice to meet you too, [mc]!"
        "Give her a hand shake":
            $ freyapoint += 1
            $ renpy.notify(freyanotif)
            scene i338
            with dissolve
            mc "You must be Freya. Nice to meet you."
            f "Nice to meet you too... Uhm..."
            mc "[mc]. My name is [mc]."
            yt "Damn, I did not expect her to be this... well..."
            yt "...small..."
            f "Hehe~ Nice to meet you too, [mc]!"
        "Don't do anything":
            scene i337
            with dissolve
            f "You must be the co-worker that Jess told me about, right?"
            mc "Yeah, my name is [mc]. You must be Freya."
            f "Yep! The one and only! Hehe~"

    yt "She looks like someone I'm very familiar with."
    yt "Pink eyes, with black hair but shorter... Is she Aine's sister by any chance?"
    yt "I'll ask her later. We should get ready now."
    yt "Plus, we still haven't done a hygiene check yet, since Lily is usually the one doing it during opening."
    mc "Alright! Let's go and prepare for opening now. I assume you don't have your uniform yet, am I right?"
    f "No, not yet I'm afraid."
    mc "Then let's get you one in the storage room."
    f "Okaay~! Hehe!"
    yt "She's a one cheerful girl, isn't she?"

    scene black
    with dissolve
    with fadeq

    "A few moments later..."

    scene black
    with dissolve
    with fadeq

    play sound 'audio/cloth.mp3'
    scene i339
    with dissolve
    mc "There! It looks good on you!"
    f "Really? This is my first time wearing a work uniform. So, I'm not really sure..."
    image fbb:
        "i340.jpg"
        pause 3.0
        "i341.jpg"
        pause .2
        repeat
    show fbb
    with dissolve
    mc "I heard from Miss Jess that you've done some odd jobs before, but you don't have much experience with this kind of job."
    f "She's right. But I know what I have to do, so you don't have to worry."
    mc "That's good to hear!"
    mc "Speaking of odd jobs, what kind of jobs did you have? Considering how you look, I'm guessing that you're still in high school, right?"
    f "Yeah! I'm a high school student. But, I'm being home schooled by my parents."
    f "I sometimes stream games online and I'm currently developing a game..."
    mc "Whoa... That's quite something."
    mc "I can't believe a high school student can make games."
    image fbb2:
        "i342.jpg"
        pause 3.0
        "i343.jpg"
        pause .2
        repeat
    show fbb2
    with dissolve
    f "Hah! It's nothing, really."
    f "I am not allowed to do them, to be honest. So I'm keeping it a secret, at least from my mom."
    f "I really hate her, so I don't want to rely on her financially."
    f "Fortunately, she allowed me to take a proper job even though it is temporary, so here I am."
    yt "Now I really have a strong feeling that she's Aine's sister."
    mc "Uhm... If you don't mind, can I ask how old are you?"
    f "Not a problem! I'm already 19 years old! Hehe~!"
    yt "She's still young, and yet she's thinking like she's older than me."
    yt "If she's really Aine's sister, considering how her mom treats her, she'll probably end up like Aine someday."
    yt "Should I ask her?"
    yt "......"
    yt "I think it's okay to ask. Let's give it a try."
    mc "Are you... Aine's little sister by any chance?"
    f "Oh yes! How do you know Aine?"
    mc "Well... She was my classmate back in high school."
    yt "And the one who gave me a hard time throughout it. *chuckles*"
    image fbb3:
        "i344.jpg"
        pause 3.0
        "i345.jpg"
        pause .2
        repeat
    show fbb3
    with dissolve
    f "Really?! Do you know where she is?!"
    yt "Huh?! What did she mean by that? She doesn't know Aine's whereabouts?!"
    f "I have been looking for her for days now."
    f "She wasn't in her previous apartment when I went there and I can't contact her through her phone number!"
    f "I... I already miss her so much! She's been away from home for years, and now, I can't even find her..."
    yt "Jeez... What is Aine even thinking?"
    yt "Should I tell her that Aine is living in our house? She seems to really care about her sister."
    yt "I really want to avoid putting myself into their problems as much as possible, since I'm still not sure what to do."
    yt "But, I think I should at least tell Freya's sister where she is. I could probably get some clues about Aine this way too."
    mc "Well... to tell you the truth, Freya..."
    mc "Your sister is... actually living in our house."
    show i346
    with hpunch
    f "EXCUSE MEEE~?!!"
    mc "Ouch! My ears!"
    show fbb3
    with dissolve
    f "Oh, sorry. I didn't mean to shout like that. But, why is she living with you?! Are you her boyfriend or something?!"
    yt "Oh, man... she has no idea that someone is plotting for me and her sister to get married. *chuckles*"
    yt "But I'll keep that information to myself for now."
    mc "No! We're not together. We're not even that close."
    mc "They told us that they lost their jobs. So they looked for a cheaper place to stay."
    f "'They'?"
    mc "Yeah, she came with Emma and Gwen."
    show fbb2
    with dissolve
    f "Oh, Emma-chan~! I really miss her too!"
    yt "'Emma-chan'? Is she an otaku or something?"
    show fbb
    with dissolve
    f "...But, why can't I contact Aine?"
    mc "That is something I don't know. Aren't you in contact with Emma?"
    f "No... I'm not."
    yt "Hmm... A good idea comes to mind!"
    yt "Having them meet might give me some more leads about Aine."
    mc "Do you want to come with me later, so you could meet her?"
    scene i342
    with dissolve
    f "Whaa~ I can~?"
    yt "She's cute. Haha!"
    mc "Yeah, sure! Why not?"
    f "Hehe~! Thank you, [mc]!"
    if lilyvisit:
        mc "But, I still have to go pay Lily a quick visit before I go home. Is that okay with you?"
        f "Miss Lily? Sure, no problem."
        f "I will go and meet with my teacher too, so we could probably meet somewhere before going to your place."
        mc "Sure! How about the central park? I think that's the best place we could meet up."
        f "Okaay~!"
    scene i347
    with dissolve
    "*door opens*"
    mc "There's our first customer. Let's talk later, Freya."
    f "Alright! Just leave it to me."

    scene black
    with dissolve
    with fadeq

    "A few hours later..."

    scene black
    with dissolve
    with fadeq

    play sound 'audio/busyrestaurant.mp3' fadein 2 loop
    scene i348
    with dissolve
    mc "Next please!"
    scene i349
    with dissolve
    ass "I told you, you little bitch! I literally found a cockroach in my burger!"
    yt "Wait... this guy is back here again?!"
    yt "Doesn't he have anything to do with his life but to try his luck in getting food for free?!"
    mc "I should-"
    show i350
    with hpunch
    f "What did you just say to me?!"
    f "Speak for yourself, you old fag!"
    yt "What the..."
    ass "W-what?!"
    f "This place has the best burgers in the entire universe!"
    f "There is no way in hell a dirty little pest such as yourself could get into our food!"
    f "If you don't have any money to pay for your grub, then scram, you peasant!"
    f "We don't want to see your ugly fucked-up face in here ever again!"
    scene i351
    with dissolve
    ass "*crying* F-fuck this place! I'm going to tell my mom about this!"
    ass "*crying* MOMMYYYYYYY~!!"
    f "That's right~! Go tell mommy!"
    yt "...heck..."
    "*Everyone applauses*"
    b1 "Whooohooo~! Way to go girl!"
    b2 "Fuck! I want to marry her! Can you please be my girlfriend?"
    scene i352
    with dissolve
    f "Heh!"
    mc "W-well... t-that's good, I guess?"
    stop music fadeout 2
    stop sound fadeout 2

    scene black
    with Dissolve(2.0)
label freyapause:
    if _in_replay:
        $ name = persistent.gallery_name
    scene freyapause
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

    "After your shift..."

    scene black
    with dissolve
    with fadeq

    play music 'audio/Tryout.mp3'
    scene i353
    with dissolve
    mc "Jesus, Freya. I didn't know you could talk like that!"
    f "I usually don't, but hey, that guy deserved it anyway. Plus, I know he's planning something."
    f "I won't let things like that slide."
    mc "I guess Miss Jess was right about you being quick to blow a fuse. Haha!"
    f "Yeah, I won't deny it. Ahaha!"
    mc "Still, you should try to be more patient next time, alright?"
    f "At the end of the day, it still worked, so I make no promises."
    mc "*sighs*"
    if lilyvisit:
        mc "Alright, I'm going to visit Lily now. I'll see you later at central park."
        f "Okay, take care~! Send Miss Lily my regards."
        mc "I will!"

        scene black
        with dissolve
        with fade

        scene i354
        with dissolve
        yt "I guess this is her place? Let me double check the address..."
        scene i355
        with dissolve
        yt "......"
        scene i354
        with dissolve
        yt "Yep! This is it."
        scene i356
        with dissolve
        yt "And wow~! Look at that! Not insulting her or something, but this place is not what I expected."
        yt "I think it was left to her when her parents passed away."
        scene i357
        with dissolve
        yt  "She told me to talk through the doorbell's microphone, so... here goes."
        mc "Lily? I'm here now."
        l "[mc]?"
        l "Oh... hold on. I'll open the gate for you."
        "*clank*!"
        l "There, now you can open the gate from outside. Just come in, I'll open the front door for you too."
        mc "Okay."

        scene black
        with dissolve
        with fade

        scene i358
        with dissolve
        l "Thanks for coming all the way here, [mc]. I really appreciate the concern."
        mc "Hey, no big deal! As your senior co-worker, it's also my responsibility to take care of you."
        l "Uhm... You already helped me with improving my service skill and now you're here paying me a visit."
        l "I'm afraid that I might just be a burden to you..."
        mc "Don't worry about it. It's not just because it's my responsibility. But, you're a friend too!"
        l "Haha! Alright, if you say so."
        mc "Why don't you lie or sit down and rest? You shouldn't be moving around too much, you know?"
        l "I live alone, so I don't really have any choice."

        scene black
        with dissolve
        with fadeq

        scene i359
        with dissolve
        mc "Have you eaten anything yet?"
        l "Not so much for lunch. I don't really have the appetite. I feel like the food won't go down to my stomach at all."
        scene i360
        with dissolve
        mc "That's alright, at least you still tried."
        mc "Look, I brought you meds for fever, and fruits that you can eat."
        mc "I'll cook you dinner right now, which you can just heat up in the microwave later."
        mc "Maybe something that will go down smoothly..."
        scene i361
        with dissolve
        mc "Hm... let me think of something..."
        scene i362
        with dissolve
        l "{i}Miss Jess was right...{/i}"
        scene i363
        with flash
        j "Your fever isn't that bad, so I don't really have to worry about you."
        j "And I know [mc] will come here to take care of you later too."
        l "Huh? How could you be so sure, Miss Jess? I mean, I'm just his co-worker after all."
        j "I will call him right after I leave."
        j "I won't tell him to come and visit you, but I know that he will come in his own free will."
        j "I've known him for some time now, and I know that he'll definitely come here."
        j "What's more, he reminds me of someone I know."
        l "Are you... talking about your boyfriend?"
        j "Yes. They have different personalities, but the kindness in their hearts aren't that much different."
        j "They both take care of someone they really care about."
        j "And [mc] is a really soft-hearted guy, unlike my boyfriend."
        scene i362
        with dissolve
        l "{i}But... this is all because of his kindness towards me, right?{/i}"
        l "{i}If only I had someone like him to take care of me every single day... I wonder how that would feel?{/i}"
        scene i364
        with dissolve
        mc "Ah! I know just what to cook! Just stay right there, I'll be back."
        l "Sure!"

        scene black
        with dissolve
        with fadeq

        "30 minutes later..."

        scene black
        with dissolve
        with fadeq

        scene i365
        with dissolve
        yt "There you go... There should be enough food portions until tomorrow."
        yt "All she has to do is to heat it up in the microwave and it's ready for serving."
        yt "Let's go back to Lily."

        scene black
        with dissolve
        with fadeq

        scene i366
        with dissolve
        $ renpy.pause()
        scene i367
        with dissolve
        mc "Lily? Are you sleeping?"
        scene black
        with dissolve
        scene i368
        with dissolve
        l "Oh... no. I was just lying down for a bit. Are you done already?"
        image lhb:
            "i369.jpg"
            pause 3.0
            "i370.jpg"
            pause .2
            repeat
        show lhb
        with dissolve
        mc "Yeah."
        mc "So, I made four portions of food for you that will last for quite a while."
        mc "Just put them in the microwave and you are good."
        mc "And of course, don't forget to take your medicine, alright?"
        l "I got it."
        mc "Good!"
        mc "I won't stay long now, Lily. I should give you time to rest, it's already getting late. I still have to go home, myself."
        scene i371
        with dissolve
        l "Oh, right... Uhmm... but before you go..."
        scene i372
        l "*hugs*"
        scene i373
        with dissolve
        yt "Oh... I didn't expect that..."
        yt "Well, I guess she's just appreciative of me doing things for her."
        yt "Should I hug her back?"
        menu:
            "Don't do it{#ep2}":
                $ lilyhug = False
                show lhb
                with dissolve
                mc "Don't worry, Lily. I'm always here for you."
                l "Oh... Uhm... Thanks! Haha..."
                mc "I'll go now, alright?"
                l "{i}I want him to stay for a bit longer, but...{/i}"
                l "Alright, please take care on your way home."
                mc "I will. Goodbye for now, Lily. And be sure to rest properly."
                l "Aye aye, boss!"
            "Hug her back":
                $ lilyhug = True
                $ lilypoint += 1
                $ renpy.notify(lilynotif)
                scene i374
                with dissolve
                l "Mmhh..."
                show lhb
                with dissolve
                mc "Don't worry, Lily. I'm always here for you."
                l "Oh... hehehe. Uhm... Thanks! *giggles*"
                mc "I'll go ahead now, alright?"
                l "{i}I want him to stay for a bit longer, but...{/i}"
                l "Okay, please take care on your way home."
                mc "I will. Goodbye for now, Lily. And take your time to rest."
                l "Aye aye, boss!"

        stop music fadeout 2

        scene black
        with dissolve
        with fade

        play music 'audio/Elevate.mp3'
        scene i375
        with dissolve
        $ renpy.pause()
        scene i376
        with dissolve
        yt "This is the central park, huh?"
        yt "I heard they renovated this place just recently. It looks way nicer than last time."
        scene i377
        with dissolve
        yt "Now where is Freya...?"
        scene i378
        with dissolve
        yt "Oh, there she is!"
        scene i379
        with dissolve
        f "No, mom! I told you, I'm not going home today! I will be staying at my friend's house! Please allow me, just this once!"
        "......"
        f "Alright, alright! I will be home early tomorrow morning!"
        "......"
        f "Okay. Goodbye."
        scene i380
        with dissolve
        f "*sighs*"
        scene i381
        with dissolve
        mc "Hey there, Freya! How long have you been waiting here for me?"
        image fpb:
            "i382.jpg"
            pause 3.0
            "i383.jpg"
            pause .2
            repeat
        show fpb
        with dissolve
        f "Not too long! Probably for about five minutes. My mom called me too, so no worries!"
        mc "Yeah, I couldn't help but overhear a bit of your conversation, sorry."
        f "Don't worry. It's not like it's a private conversation anyway."
        mc "So, you plan to stay overnight with your sister?"
        f "Of course! We haven't seen each other for a while. I'm sure that she misses me too!"
        f "I won't let my parents stop me from doing that!"
        f "But... is it okay for me to stay in your house for the night?"
        mc "Sure! I don't have a problem with it."
        f "Thanks, [mc]~!"
        f "My first impression of you is really good. You're really a nice guy!"
        f "At least, I can breathe, now that I know that my sister is in safe hands."
        yt "{b}Hands{/b}, huh? Jeez..."
        mc "Well, thanks. Haha."
        mc "Should we go now? The sky is getting dark, it's going to rain soon."
        f "Yep! Lets~!"
    else:
        mc "Alright, should we go? The sky is getting dark, it's going to rain soon."
        f "Yeah! Let's go~! I can't wait to see my sister! Hehe~!"
    stop music fadeout 2

    scene black
    with dissolve
    with fade

    play music 'audio/JazzInParis.mp3'
    scene i383b
    with dissolve
    f "Oh, woooow~!"
    f "I didn't expect it to be all white walls."
    scene i384
    with dissolve
    mc "Hm? Do you have a thing with white walls?"
    f "Yeah, they're very pleasant to look at!"
    f "Even though my room is full of anime posters and stuff like that, I still like seeing this kind of design."
    mc "Are you really a 19 year old? Because the way you talk and think doesn't match your physical appearance at all."
    mc "It just doesn't convince me."
    f "I can't blame you, and that's what most people think about me as well."
    f "Don't jump to conclusions though... I can still be a kid sometimes."
    scene i385
    with dissolve
    s "[mc]~! You're home!"
    scene i386
    with dissolve
    mc "Yeah! Did you put that picture up there? I didn't see that before."
    s "Yep! I redecorated the kitchen too!"
    s "It's better to liven up the house since we have people living here besides us now."
    mc "That's a good idea!"
    mc "But you should take it easy, Sky..."
    mc "You've been so busy with your work lately. Don't burn yourself out now!"
    scene i387
    with dissolve
    s "Don't worry, I got Aine and Gwen's help with it, so it did not take that much effort."
    yt "Well, it's good to know that they're helping out."
    scene i388
    with dissolve
    s "By the way, who's this?"
    mc "Oh, our visitor. She's Aine's little sister. She came to visit her and probably will stay for the night."
    mc "She filled in for Lily's shift at the burger place since she was out sick today."
    s "I see..."
    scene i389
    with dissolve
    s "Hm......"
    scene i390
    with dissolve
    f "Eh? What are you doing?"
    scene i391
    s "*gasps*! Someone shorter than me!"
    scene i392
    f "Hey~! What do you mean shorter? You're only an inch taller than me!"
    f "I'm just 19, and I'm still growing, you know?!"
    scene i393
    with dissolve
    f "But... how did you..."
    scene i394
    with dissolve
    f "...those... big..."
    scene i395
    with dissolve
    f "...and... so much... curves..."
    show i396
    play sound 'audio/woosh.mp3'
    f "*gasps*! Of course, an enemy!"
    scene i397
    with dissolve
    s "Huh? What do you mean 'an enemy'?"
    f "You're short, but you got those big oppais and lots of curves! You're definitely an enemy!"
    scene i398
    with dissolve
    s "Oh, I see what it is now..."
    s "Sorry to tell you, but {b}the bigger, the better{/b}!"
    show i399
    play sound 'audio/woosh.mp3'
    f "No, you're wrong! {b}Flat is justice{/b}!"
    scene i400
    with dissolve
    s "No! The bigger they are, the better!"
    scene i399
    with dissolve
    f "Flat over fat!"
    scene i401
    with dissolve
    s "Hrrrmmnnnn....."
    scene i402
    with dissolve
    f "Hrrrmmnnnn....."
    scene i403
    with dissolve
    yt "Uh-oh... I have a feeling this won't stop until a man states his opinion."
    yt "I have to say something."
    menu:
        "Take Sky's side":
            $ skypoint += 1
            $ renpy.notify(skynotif)
            scene i404
            with dissolve
            mc "You girls need to calm down!"
            mc "I'm sorry, Freya. I'm on Sky's side."
            f "Eh? Still! Flat is justice!"
            s "No! The bigger, the better!"
        "Take Freya's side":
            $ freyapoint += 1
            $ renpy.notify(freyanotif)
            scene i405
            with dissolve
            mc "You girls need to calm down!"
            mc "I'm sorry, Sky. But, I'm on Freya's side this time."
            f "See?!"
            s "No! The bigger they are, the better!"
        "Agree with both":
            $ skypoint += 1
            $ freyapoint += 1
            $ renpy.notify("Sky and Freya +1 point!")
            scene i406
            with dissolve
            mc "You girls need to calm down!"
            mc "If I can say my opinion, then I like them both! Hehe!"
            f "Eh? Still! Flat is justice!"
            s "No! The bigger they are, the better!"
    scene i407
    with dissolve
    s "Hrrrmmnnnn....."
    scene i408
    with dissolve
    f "Hrrrmmnnnn....."
    "......"
    scene i409
    with dissolve
    $ renpy.pause()
    scene i410
    with dissolve
    "*both giggle*"
    scene i411
    with dissolve
    s "Sorry, that was rude of me. I'm Sky, nice to meet you."
    f "That's alright. I'm Freya, Aine's little sister. Nice to meet you, Sky."
    yt "I... I don't know what to say..."
    f "By the way, is Aine home right now?"
    s "Yes, she is! She's upstairs in her room setting up her computer for work tomorrow."
    f "I see. Thanks, Sky! I'll go and meet her right now."
    s "Sure, I'll go back to my room too."
    stop music fadeout 2

    scene black
    with dissolve
    with fade

    play music 'audio/Ocean.mp3'
    scene i412
    with dissolve
    f "Shhh..."
    mc "Mhm."
    yt "She probably wants to surprise Aine. I know that I should give them some privacy... but..."
    yt "...I really want to know what's happening with their family."
    play sound 'audio/doorknock.mp3'
    scene i413
    with dissolve
    f "*knocks*"
    a "Who is it?"
    play sound 'audio/doorknock.mp3'
    f "*knocks* *knocks*"
    a "Ahh... Hold on! I'm coming!"
    play sound 'audio/opendoor.mp3'
    scene i414
    with dissolve
    "*door opens*"
    scene i415
    a "F-Freya?!"
    scene i416
    with dissolve
    f "*sniffs*"
    scene i417
    with hpunch
    f "*crying* Sis~!"
    f "*sobs*"
    scene i418
    with dissolve
    a "How did you know that I'm here?"
    scene i419
    with dissolve
    mc "I brought her."
    mc "She apprently knows my boss and begged her to fill in for my co-worker who's not feeling well."
    mc "She looks a lot like you, so I asked her and confirmed that you two are related."
    mc "She's been looking for you, so I let her tag along. I hope that's okay."
    scene i420
    with dissolve
    a "No, I should thank you. We haven't seen each other for quite a while now."
    a "I had to temporarily cut off my connection to my mother."
    a "And that affected my connection to Freya as well."
    a "Thank you for bringing her here, [mc]. I appreciate it, really..."
    menu:
        "You're welcome":
            $ ainepoint += 1
            $ renpy.notify(ainenotif)
            mc "You're welcome."
        "Keep quiet":
            mc "......"
    mc "I'll leave you guys for now."
    scene black
    with dissolve
    scene i421
    with dissolve
    play sound 'audio/closedoor.mp3'
    "*door closed*"
    yt "It's rude to eavesdrop with someone else's conversation, but... I can't help it."
    scene i422
    with dissolve
    f "When will you come back home sis? It's getting really lonely there!"
    a "I told you that I can't, right?"
    a "I can't let myself be mother's puppet anymore, Freya. What she did to me back then was more than enough."
    yt "Her mother is mistreating her?"
    yt "Emma mentioned that she doesn't have any freedom, but... why is she out here like it's nothing, then?"
    yt "The same goes to Freya."
    a "And now that I'm finally outside of that hell, she's still won't let me go by setting me up in an arranged marriage."
    scene i423
    with dissolve
    f "Wait, what?! I never never knew about it!"
    scene i422
    with dissolve
    a "How can you not know? It was broadcast on the news."
    f "I don't watch the news, so... don't blame me."
    a "Jeez..."
    f "So, who's the guy? He needs to be at least handsome enough for you!"
    a "*sighs* Who else? That old guy who is mother's business partner, of course."
    scene i424
    f "WHAT?! That guy is like more than 50 years old!"
    f "How can she plan to marry you with that old fag?! I don't get it!"
    yt "50 year old?! Jesus Christ!"
    a "I'm against it, Freya. That is why I cut my connection to her, including you."
    a "I know she can just get my phone number from you and track me that way."
    f "...Then, what's your plan?"
    f "That guy is nasty, rude and cocky as fuck! I won't let you marry that motherfucker!"
    a "Hey, watch your language, Freya!"
    f "I can't help it! He may have a deep pocket, but he's the worst guy you could marry!"
    a "I know that! Still, you shouldn't say things like that all of a sudden."
    f "Alright, alright, I'm sorry..."
    scene i425
    with dissolve
    f "Then why don't you find someone you could marry instead? Like [mc] for example!"
    f "I can't vouch for him, but he seems to be a nice gentleman. Hahaha!"
    yt "Pardon?"
    scene i426
    a "Where did that come from?! Marrying someone else will not solve my problem!"
    a "Why... would I..."
    scene i427
    with dissolve
    pause
    scene i231
    pause 0.2
    scene i309
    pause 0.2
    scene i427
    with dissolve
    $ renpy.pause()
    scene i428
    with dissolve
    a "*blushes*"
    show i429
    with hpunch
    a "Errmmnnn....!"
    f "Why is your face like a tomato, hmm?"
    f "Heeeh~"
    f "I get it, now. Something already happened between you two, am I right?"
    f "Tell me, tell me! Did you guys already kiss?"
    f "He told me you guys are not together, so why you are acting like this?"
    f "Something must have happened!"
    a "N-no~! It's nothing like that!"
    f "Then tell me! *giggles*"
    scene i430
    with dissolve
    a "*whispers*......"
    show i431
    with hpunch
    f "WHAAAAT?!!"
    scene i432
    a "Shhhhh....! Keep your voice down! What if he hears us?"
    yt "Uhm... I actually do hear you..."
    scene i433
    with dissolve
    f "Do you like him?"
    scene i434
    with dissolve
    a "No, I don't! Our previous interactions are just embarrassing!"
    yt "Well... I have to agree. Those were pretty embarrassing."
    a "I know they were just accidents, but..."
    scene i435
    with dissolve
    f "Heeeh~ My big sister is finally in love~!"
    a "I am not, Freya! And I don't deserve anyone's love..."
    a "I'm just a horrible girl who did terrible things in the past... and nothing I could do will be able to absolve what I did."
    yt "At least she's aware of it."
    scene i436
    with dissolve
    f "Come on! Stop thinking about that already... Mom turned you into that monster!"
    yt "Her mother?!! What did her mother have to do with her bullying me back then?!"
    scene i437
    with dissolve
    a "Even if you tell me that, it won't change the fact that I hurt somebody back then. I'm still responsible for my own actions."
    a "......"
    a "I wonder where he is now? I don't even remember his name. I'm really an idiot!"
    a "I know it's not enough, but I still want to apologize for the things that I did to him."
    a "I'm ready to face all the consequences just to fix everything with him..."
    a "I... I want to tell him everything..."
    yt "......"
    scene i438
    with dissolve
    yt "Ugh! Enough of this spying shit!"
    stop music fadeout 2
    scene i439
    play sound 'audio/opendoor.mp3'
    "*door opens*"
    mc "Then, tell me... Aine."
    mc "...Tell me why did you make my high school a hell on earth."
    stop music fadeout 2
    play music 'audio/TheEnd.mp3'
    mc "You said you wanted to tell me everything, right?"
    mc "So here I am..."
    scene i440
    with dissolve
    f "Uhm...... Uhh......"
    f "I think... I should leave you guys for now."

    scene black
    with dissolve
    with fadeq

    scene i441
    with dissolve
    a "W-what do you mean, [mc]? I... don't understand..."
    scene i442
    with dissolve
    mc "Oh, right. You already {b}forgot{/b} about me."
    mc "Well, let me introduce myself properly this time."
    scene i443
    with dissolve
    mc "My name is [mc]. I'm the one you {b}bullied{/b} back in high school. Nice to meet you again, Aine."
    scene i444
    with dissolve
    $ renpy.pause()
    scene i445
    with dissolve
    a "Y...you're..."
    mc "Oh, jesus! Why do you always-"
    show i446
    with hpunch
    a "*hugs*"
    a "I know that you want to push me away right now."
    a "But... P-please... just let me do this for a while..."
    scene i447
    with dissolve
    yt "I don't get her. A hug is not what I expected from her after all this time."
    a "I know crying is pointless, so I will hold back my emotion. My apology means nothing after what I did to you, but still..."
    a "With all my heart, I am sorry, [mc]... I'm really sorry for giving you a hard time before."
    a "I'm ready for whatever judgment and consequences you have for me. But at least... let's just stay like this for a while."
    scene i448
    with dissolve
    mc "You deserve to be, but no, I don't want to get my hands dirty just for that, Aine. I'm not that kind of person."
    mc "Right now, all I need is at least an explanation."
    scene i449
    with dissolve
    a "I know... And I will give it to you."
    a "But... w-would you please pat my head one more time? I want to confirm something."
    yt "What should I do?"
    menu:
        "Reject her request":
            mc "No, I won't. I need you to explain everything to me now."
            a "Oh... Uhm... Okay..."
        "Pat her head":
            scene i450
            with dissolve
            a "Mnnhh..."
            a "{i}His hand... really feels so comfortable...{/i}"
            scene i451
            with dissolve
            a "I was wondering why I feel so comfortable everytime you do that to me."
            a "So it was you all along. The one patting my head when I was asleep back then."
            mc "*sighs* Yes, pretty much every time I saw you having a nightmare."
            a "I see... But why? Why did you do that despite what I was doing to you?"
            mc "I don't know, Aine. My brain told me not to do it, but my heart told me to go ahead."
            mc "That is something that I don't get myself."
            mc "You did all those things to me. But, I was an idiot for not fighting back, and letting my feelings overtake my anger."
            mc "I was so stupid and naive."
            mc "I know I should've tormented you for what you did. I even pushed to change myself for that reason."
            mc "But, as I got older and had more control over decisions, I realized that any time I spent getting back at you would just be a waste..."
            mc "...And so I focused on my own life instead."
            mc "I already threw everything away, Aine... That includes my feelings for you."
            a "{i}He... really is a good guy... I feel... so terrible.{/i}"
            a "I'm... really sorry, [mc]."
            mc "Instead of apologizing, why don't you start telling me everything?"
            a "Okay..."

    scene black
    with dissolve
    with fadeq

    play sound 'audio/chair.mp3'
    image arrb:
        "i452.jpg"
        pause 3.0
        "i453.jpg"
        pause .2
        repeat
    show arrb
    with dissolve
    a "*sighs* Where do I even start?"
    mc "Start with the reason why you were doing those things to me back then."
    a "Alright, I'll get straight to the point, then. There's no reason to lie and hide it now..."
    mc "I'm listening."
    a "...Mom was controlling me to do those horrible things to you."
    yt "I already guessed as much after hearing what she said earlier. But the question is... why me? What does it have to do with me?"
    a "I was young and powerless against her, I couldn't do anything but follow her orders, because if I didn't, she'd mistreat and hurt me until I said yes."
    a "It didn't have anything to do with you confessing to me before."
    a "Even if you hadn't, she still would have pushed me to do it."
    mc "My... god! Just... what kind of family do you have, Aine?!"
    mc "But I can't understand..."
    mc "Why me? What does it have to do with me?"
    a "She didn't tell me why. Every time I tried to refuse her, she'd threaten to hurt me and take Emma away from me."
    a "She could hurt me all she wanted, but I couldn't let her take away Emma. She's my best friend, we grew up together..."
    a "I... I didn't have any choice..."
    a "But even though I was forced, I know that what I did was still wrong."
    a "And there's nothing that I can do to absolve myself and reverse all the bad things that I did."
    a "So, I won't ask for your forgiveness."
    a "It's too selfish of me to ask, but all I want is your understanding."
    mc "As I said, the past doesn't matter to me anymore, Aine. All I want is to clear things up."
    mc "I understand that you were forced by your stupid fucking mother."
    scene i454
    with dissolve
    a "Language, [mc]."
    mc "Oops... sorry..."
    image arrb2:
        "i455.jpg"
        pause 3.0
        "i456.jpg"
        pause .2
        repeat
    show arrb2
    with dissolve
    mc "However, I won't be able to understand everything while we don't know the reason your mom did that to you."
    a "I really don't know, [mc]. She doesn't tell me anything, except giving me orders."
    a "'You do this and do that' and threatens me if I try to refuse her."
    yt "But, why didn't Emma tell me all this? All she told me is that Aine doesn't have a say in her own future."
    yt "Not just Emma, but Aine is being controlled by them too! Just what kind of family is that?!"
    yt "My blood is boiling just listening to her right now!"
    yt "They're supposed to treat each other well! That's what family is supposed to be!"
    yt "I want to do something to uncover all this. I have a feeling that this isn't just between me and Aine."
    yt "I want to hear everything from her mother herself. But... how the heck am I going to do that?!"
    yt "......"
    yt ".........."
    yt "Wait a minute..."
    yt "Didn't Freya tell me that she knows Miss Jess?"
    yt "Hm..."
    yt "Maybe Miss Jess would be able to help me. She might know the family too..."
    yt "But I can't be sure just yet. Maybe I can try and contact her later."
    yt "So much for leads and clues, huh?"
    yt "now, it led me to another mystery..."
    mc "I have a question..."
    mc "How did you manage to move out of your house if that's the case?"
    image arrb3:
        "i457.jpg"
        pause 3.0
        "i458.jpg"
        pause .2
        repeat
    show arrb3
    with dissolve
    a "My family has a strong work ethic, especially my mother. So me, her daughter, having that kind of mindset worked in my favor."
    a "It was easy to convince her by telling her I was looking for a proper job."
    yt "No, that's too shallow considering what her family is like. There's gonna be something behind it."
    a "I was so happy thinking that I would finally have my freedom, but I was wrong."
    a "Even though I'm outside, I still don't have much freedom."
    a "Now, she even set me up to marry her business partner."
    mc "Yes, I already know that."
    a "Wait... did you hear our conversation earlier?"
    mc "Yeah, I heard everything."
    a "It's not good to eavesdrop on someone's conversation, you know?"
    mc "I know. But what choice did I have? I wanted to know everything."
    a "......"
    a "You could've turned us away the moment we arrived here, but you didn't."
    a "You had the chance to take revenge for everything that we did, but you moved on from it instead."
    a "I feel like a shameless little bitch facing you right now because of what I did..."
    mc "Hey, didn't you tell me to watch my language?"
    a "I'm sorry, but I have been holding back my feelings. I want to cry my heart out, I want to scream out all the pent-up feelings inside me."
    a "But... I can't."
    scene i459
    with dissolve
    a "Pain, regret, sorrow, guilt. I want them all out... I want to breathe freely away from all of it..."
    a "But I don't know what to do..."
    mc "......"
    mc "*sighs* Come here."
    scene i460
    with dissolve
    yt "Well... Fuck this! As usual, I'm doing what my heart dictates."
    mc "It's okay to cry."
    mc "At least... that's what you can do right now. Don't worry about anything for now, and just cry it out."
    scene i461
    with dissolve
    a "Mnnh..."
    a "......"
    scene i462
    with dissolve
    a "*sniffs*"
    a "*sobs*"
    a "Mm...!"
    a "*crying* Mhhmmn..."
    a "*hiccups* Mhhmmn...!"

    scene black
    with dissolve
    with fadeq

    "A few moments later..."

    scene black
    with dissolve
    with fadeq

    scene i463
    with dissolve
    yt "*sighs* She fell asleep..."
    scene i464
    with dissolve
    yt "I should probably move her to-"
    scene i465
    with dissolve
    a "Mmmn!"
    scene i466
    with Dissolve(1.0)
    scene i467
    with Dissolve(1.0)
    yt "Jeez..."
    yt "...I even forgot to ask some of the questions I have for her... But, that can wait."
    yt "I now have one bigger question that needs an answer."
    play sound 'audio/opendoor.mp3'
    scene i468
    with dissolve
    f "She looks really comfortable. *giggles*"
    scene i469
    with dissolve
    mc "Where did you go?"
    f "I was talking to Sky in her room."
    mc "I see."
    scene black
    with dissolve
    scene i470
    with dissolve
    f "So, are you two on good terms now?"
    mc "I'm not too sure about that."
    f "I can guarantee that she will do something about it, trust me."
    f "But, you know? I was really shocked when you entered the room. I didn't know it was you!"
    f "I'm really wondering how she ended up in your house, to be honest."
    mc "Well, that's a long story..."
    yt "I guess it's alright to tell her, she's Aine's sister after all."

    scene black
    with dissolve
    with fadeq

    "You tell Freya about Emma's plan..."

    scene black
    with dissolve
    with fadeq

    scene i471
    with dissolve
    f "I see... So that's why they're here, huh?"
    image frrb:
        "i472.jpg"
        pause 3.0
        "i473.jpg"
        pause .2
        repeat
    show frrb
    with dissolve
    mc "You seem pretty nonchalant about it."
    f "I know Emma-chan. She will do everything for my sister's sake. Even if it costs her everything, so I'm not really surprised."
    f "She may be Aine's servant, but that's not all there is to it."
    f "They're best friends, and they've really cared about each other since they were little."
    image frrb2:
        "i474.jpg"
        pause 3.0
        "i475.jpg"
        pause .2
        repeat
    show frrb2
    with dissolve
    f "They're both under mom's control and I really hate that fact!"
    f "I, myself will eventually fall under mom's control..."
    f "Well, to be honest I already am. But I am not going to be like my sister! Not over my dead body!"
    f "I already had enough after seeing them both suffer! But, there's nothing that I could do for them."
    f "Like my sister, I'm powerless against mom."
    f "Now that they're here, it might be just you who can help them."
    f "But I am not saying you have to."
    f "That is still up to you."
    f "They did something to you that you should have a grudge over, after all."
    f "Although, I'm guessing you already got over it, no?"
    mc "Mhm."
    image frrb3:
        "i476.jpg"
        pause 3.0
        "i477.jpg"
        pause .2
        repeat
    show frrb3
    with dissolve
    f "I only met you today, but I already know that you have a good heart."
    f "Enough to forgive those who have sinned against you..."
    mc "Are you really 19 years old? Because I feel like you are way older than that."
    f "Of course I am! But, I'm not the type of girl who's been pampered by her parents. I can even live on my own if they would let me!"
    f "I avoid relying on them as much as possible, so at this age, I already know things that other 19 year old brats out there don't."
    mc "That makes sense."
    f "So... what's your plan, [mc]? Are you going to marry my sister? Ahaha!"
    mc "No, I won't. That will not solve anything, Freya. Even if I decided to do it, we can't say for sure that your mother will let her go for good."
    mc "And I'm thinking of Aine's side too."
    mc "Let's say that we both agree to it, and then what? Hide from her parents forever? For sure she doesn't want that."
    f "You have a point there..."
    mc "I'm not really sure yet, but I want to talk to your mother."
    image frrb4:
        "i478.jpg"
        pause 3.0
        "i479.jpg"
        pause .2
        repeat
    show frrb4
    f "Wait, what?! Talk to my mom? Are you for real?!"
    f "You can't just do that, you know? How do you even plan to do that?"
    f "Us, her daughters, can probably talk to her without any security and identity check."
    f "But you, I'm not really sure, [mc]. Also I couldn't take you in there just like that!"
    mc "I'm not planning to do it anytime soon. But, I will definitely come up with a plan for it. I want to hear it from her own mouth."
    mc "For sure, Miss Jess can help me out with that. She knows you, so I'm thinking that she knows your family too."
    f "Yes, she knows my mom... but, are you really sure about that? Like a hundred percent sure?!"
    mc "I've made up my mind. That's the only way for me to learn the truth."
    f "Well, alright then. I'll support you anyway I can if you really want to do it."
    mc "Thanks, Freya."
    f "Hey, no problemo~!"
    mc "I'll set Aine properly on her bed, then I'll have to get Sky so we can prepare dinner."
    f "Sure!"
    stop music fadeout 2

    scene black
    with Dissolve(2.0)
label ainepause2:
    if _in_replay:
        $ name = persistent.gallery_name
    scene ainepause2
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

    "After eating dinner..."

    scene black
    with dissolve
    with fadeq

    play music 'audio/Sorrow.mp3'
    play sound 'audio/closedoor.mp3'
    scene i480
    with dissolve
    yt "Okay, time to call Miss Jess. I just hope she's not busy right now..."
    scene i481
    with dissolve
    ".........."
    scene i482
    with dissolve
    j "[mc], what's the matter? You, calling me at this time of the day... is there a problem?"
    mc "I'm sorry to call you so suddenly. But, I have something to ask."
    j "Hm? Sure, just ask away."
    mc "You said that you and Freya know each other, and she told me that you know her mother too."
    mc "Can I have your confirmation on that?"
    j "Oh, Hera?"
    j "Yes, of course, we know each other. Why do you ask?"
    mc "I told you a little bit about my past before when I applied for the job."
    mc "I just learned something that can answer the questions that I have had in my head for some time now."
    mc "She's the only one who can answer those questions, so I'm planning to meet her."
    mc "I figured that you might be able to help me with that, Miss Jess."
    scene i483
    with dissolve
    j "Hold on, let me just park the car..."

    scene black
    with dissolve
    with fadeq

    scene i484
    with dissolve
    j "Hm... meeting Hera, huh?"
    j "I'm not looking down on you, [mc]. But a normal person like you meeting Hera is like a beggar asking to meet the President."
    j "Considering what I know, it's like you jumping from a plane without any parachute."
    j "You're not a suicidal person as far as I can remember."
    mc "But... it's not totally impossible, right? And I know you can make it happen too."
    scene i485
    j "Well, well... What do you know?"
    j "I like your mindset, [mc]. You've impressed me once more."
    mc "If we're talking about power, then there's no one else I can ask but you."
    j "You're really playing with fire here, [mc], you know that?"
    mc "I know..."
    mc "But, I have a gut feeling that there are more people involved in this."
    mc "All I want are answers to settle the questions I have in my mind once and for all."
    j "*chuckles* Alright then. If you're really willing to go that far, then I shall help you."
    j "However, you will have to wait for a while. I can't suddenly tell her to meet up with you just like that, as I want to stay on good terms with her."
    scene i486
    with dissolve
    j "......"
    j "In a month..."
    j "I have an appointment with her next month. I will let you use that chance to talk to her."
    j "I will tell you the details at a later time. I still have to make preparations."
    mc "Thanks, Miss Jess!"
    scene i487
    with dissolve
    j "There's no turning back on this now, [mc]. This is the first and last chance that I can give you. Nothing more, do you understand?"
    mc "I understand."
    j "Good! Now please excuse me. I still have to go somewhere."
    mc "Thanks again, Miss Jess. And take care."
    j "I will. Goodbye for now."
    scene i488
    with dissolve
    y "Your boy is meeting your sister, huh? I just hope he doesn't mess it up. You're really putting your name on the line for him."
    j "Well, what can I say? I'm quite fond of the way he thinks."
    j "And... this might be the moment I've been waiting for. I can't let this slip my fingers."
    y "If you say so."
    scene i489
    with dissolve
    j "Alright. Let's go?"
    y "Okay."
    scene i490
    with dissolve
    yt "Now that's settled. I'll just have to prepare myself for it."
    yt "So, their mother's name is Hera, huh? What's with all the goddesses' names?"
    yt "Aine, Freya, and Hera are all names of goddesses, right?"
    yt "I wouldn't be shocked if their father's name turned out to be Zeus or Poseidon."
    scene i492
    with dissolve
    yt "Despite that fact, their family is just too messed up for those names. Jeez..."
    yt "I have a very strong feeling that there is more to this than what I really expect..."
    yt "......"
    yt "Well... That's enough thinking for today. Let's just head to bed."

    scene black
    with dissolve
    with fade

    scene i493
    with dissolve
    h "......"
    h ".........."
    h "Not just my daughters... but my sister too, huh?"
    h "I don't know if I should thank you for that, Jess."
    scene i494
    with dissolve
    h "*chuckles*"
    h "Regardless, I'm looking forward to meeting you soon..."
    h "...my boy."
    h "...Be in haste."
    h ".........."
    h "Hmp..."
    stop music fadeout 2

    scene black
    with Dissolve(2.0)
label jessherapause:
    if _in_replay:
        $ name = persistent.gallery_name
    scene jessherapause
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

label mytruefeelings:
    if _in_replay:
        $ name = persistent.gallery_name
    play music 'audio/LeafBeach.mp3'
    scene i495
    with dissolve
    mc "......"
    un "Hmmnnn..."
    yt "Who's...?"
    scene i496
    with dissolve
    s "*giggles*"
    scene i497
    with dissolve
    mc "Sky?! What are you doing here?"
    mc "And why are you—"
    show sky6
    with dissolve
    s "Shhhh... just relax. I know you want this, [mc]."
    s "It's been a while since we let ourselves feel this way."
    if skyroute:
        show sky7
        with dissolve
        mc "Ahh—f-fuck, Sky! That feels amazing!"
        s "There's no turning back now, [mc]... No more second-guessing, no more hiding what we feel! Mmhmm~"
        yt "Is this... what we've become? Is something real happening between us?"
        yt "Part of me's still hesitant... but the rest? The rest wants this more than anything."
        yt "Do I really love her... as more than just the girl I grew up with?"
        yt "We crossed that line already... but where do we go from here?"
        scene i497
        with dissolve
        s "All you need to do now is wake up, [mc]."
        mc "Huh?"
        s "Get up or you'll be late for work!"
    else:
        show sky7
        with dissolve
        mc "Sky... I told you we can't keep doing this."
        s "It's too late, [mc]. This thing between us is already alive. You feel it, don't you?"
        yt "We said we'd stop... but my heart keeps rewriting the rules."
        yt "What even are we now? Two people who got too close?"
        yt "Every time I try to pull away, she pulls me right back in."
        yt "I don't know what this is anymore—but I know I can't ignore it."
        scene i497
        with dissolve
        s "All you need to do now is wake up, [mc]."
        mc "What...?"
        s "Come on, or you're going to be late!"
    stop music fadeout 2
    scene i498
    with dissolve
    $ renpy.pause()
    scene i499
    with dissolve
    $ renpy.pause()
    scene i500
    with dissolve
    yt "Shit... just a dream."
    yt "......"
    scene i501
    with dissolve
    yt "Only a dream... right?"
    yt "......"
    yt "They say dreams reflect the things we bury during the day..."
    yt "So does that mean... deep down, I actually want this?"
    yt "A relationship with Sky... after everything?"
    yt "But we live together. Blurring that line could change everything..."
    scene i502
    with dissolve
    yt "*sighs* Sky..."
    $ renpy.end_replay()

    scene black
    with dissolve
    with fade

    play music 'audio/Typhoon.mp3'
    play sound 'audio/closedoor.mp3'
    scene i503
    with dissolve
    mc "Hm?"
    scene i504
    with dissolve
    yt "Holy... shit..."
    scene i505
    with dissolve
    yt "Why the heck are they both wearing cat ears?"
    s "There! You look really pretty in them, Aine!"
    scene i506
    with dissolve
    a "Uhm... Do I really need to wear this, Sky? I'm getting butterflies in my stomach for some reason."
    scene i507
    with dissolve
    mc "Good morning, girls! What's with the cat ears? Is it some kind of a prop?"
    scene i508
    with dissolve
    s "Yeah! Today is a special day for our team since this is Aine's first day of work with us."
    s "So this is to celebrate it, and I'm pretty sure the kids will love them too! *giggles*"
    mc "I see..."
    menu:
        "Compliment Sky":
            $ skypoint += 1
            $ renpy.notify(skynotif)
            scene i509
            with dissolve
            mc "You look so cute in them, Sky! You should wear them all the time."
            s "Really?! Oh, thanks [mc]!"
            s "This is only to celebrate Aine's first day. But I'll consider it. *giggles*"
        "Compliment Aine":
            $ ainepoint += 1
            $ renpy.notify(ainenotif)
            scene i510
            with dissolve
            mc "I agree with Sky, you look very pretty in it, Aine. You should consider wearing them often."
            yt "I said it like I didn't confess to her in the past. That could've made things awkward. Haha!"
            yt "Oh, well... That feeling is long gone. And she doesn't seem to have any issues with it either."
            yt "I would rather not make things awkward."
            yt "However, I still shouldn't be too soft to her even after learning what's going on with her family."
            yt "She said she's ready to do everything to make things up with me. So I would like to see how she does that first."
            s "Right? Told you so!"
            a "Uhmm... Thanks. I'll think about it."
            yt "So this is what a shy Aine looks like..."
            yt "*chuckles*"
        "Compliment them both":
            $ skypoint += 1
            $ ainepoint += 1
            $ renpy.notify("Sky and Aine +1 point!")
            scene i511
            with dissolve
            mc "You look so cute in them, Sky! You should wear them all the time."
            s "Really?! Oh, thanks [mc]!"
            s "This is only to celebrate Aine's first day. But I'll consider it. *giggles*"
            mc "And I agree with Sky, you look very pretty in them, Aine."
            yt "I said it like I didn't confess to her in the past. That could've made things awkward. Haha!"
            yt "Oh, well... That feeling is long gone. And she doesn't seem to have any issues with it either."
            yt "I would rather not make things awkward."
            yt "However, I still shouldn't be too soft to her even after learning what's going on with her family."
            yt "She said she's ready to do everything to make things up with me. So I would like to see how she does that first."
            s "Right? Told you so!"
            a "Uhmm... Thanks. I'll think about it."
            yt "So this is what a shy Aine looks like..."
            yt "*chuckles*"

    if skycelebrate:
        yt "Thinking about Sky now... I still haven't got a single clue of where to take her yet."
        yt "I don't really know a place, to be honest."
        yt "I could probably ask someone... Someone who might know a nice place to relax."
        yt "It doesn't need to be fancy at all!"
        yt "...Fancy,... Places... Hmm..."
        yt "Gwen comes to mind. I'll try to ask her later."
    scene i512
    with dissolve
    mc "By the way, did Freya go home already?"
    a "Yeah, she went home pretty early. She told me she still has to go to work."
    a "She can be mature enough to think about what she needs to do, but she's still young. Please take care of her, [mc]."
    menu:
        "I will":
            mc "Don't worry, it falls under my responsibility as her senior even if it's temporary."
            a "Thanks, [mc]."
            mc "You're welcome!"
            $ ainepoint += 1
            $ renpy.notify(ainenotif)
        "I can't promise":
            mc "I can't promise anything, Aine. But I will try. That's all I can say."
            a "Alright..."

    mc "Anyway, I have to go to work now. I'll see you guys later."
    s "Take care, [mc]."
    mc "I will!"
    mc "I'll be on my way now. Good luck with you guys' work!"
    scene i513
    with dissolve
    "*phone vibrates*"
    yt "An incoming call..."
    scene i514
    with dissolve
    yt "Lily?"
    scene i515
    with dissolve
    mc "Hello, Lily? What's up? How's your fever?"
    l "Haha! That is the reason why I'm calling you! I feel all fine now."
    scene i516
    with dissolve
    if lilyvisit:
        l "Thank you for visiting me yesterday, [mc]."
        l "Your food tasted really great, by the way. That helped a lot in my recovery."
        mc "No worries, Lily. I'm glad to help."
    l "I called Miss Jess and asked if I could return to work today. And she agreed."
    mc "Wait... don't you think you should rest for at least another day just to make sure?"
    l "Hmm... Miss Jess said the same thing. But, I'm all good now. I know my body better than anyone else."
    l "If I felt like I still needed more rest, then I would."
    l "But I'm sure I can go back to work now. So don't worry. In fact, I already timed in for today."
    mc "Heeh... Alright, if you say so..."
    mc "Just hold on, I'm on my way there now."
    l "Oh, about that!"
    l "Miss Jess told me that..."
    scene i517
    with dissolve
    l "*imitating Jess' voice* Tell [mc] to take a two day rest. I'll let you and Freya handle things on those days. We will do an evaluation of you guys on the first day too."
    mc "Yikes..."
    scene i518
    with dissolve
    l "I'm not sure if I can survive the first day without you, [mc]! What if I mess up?"
    menu:
        "Be positive":
            mc "Nahh... That's what we trained you for, right? We both know that you can do it. Just be positive and believe in yourself, Lily."
            $ lilypoint += 1
            $ renpy.notify(lilynotif)
        "Be negative":
            mc "Yeah, I agree. I'm not sure if you're quite ready yet."
    mc "But, hey! Miss Jess won't fire anyone just because they mess up. She just wants to see how much we improve, that's all."
    mc "Just think of it as our normal day to day shift and not an evaluation. That will help remove some of your feeling of pressure on you."
    scene i519
    with dissolve
    l "You really know how to lift my spirits, [mc]. I don't know what I can do to repay all the help you've given me."
    mc "You don't have to do anything for me, Lily. I'm always happy to help. Hehe!"
    l "Alrighty then, I'll remember what you said."
    mc "But, do I really have to take 2 days off? I can still do things in the kitchen, you know?"
    l "Yep! Miss Jess told me to not allow you to say no. *giggles*"
    mc "*sighs* Alright. I can't really go against her decisions."
    l "She said that you deserve it. I may be afraid of not having you around during work, but I agree, you deserve some rest, [mc]."
    l "What's more, she also told me that she'll send you the 'details' later so you can take your time to think about it."
    l "You're probably having a promotion soon, [mc]!"
    yt "Well, damn... I would be ecstatic if that's the case!"
    yt "However, this is way more important than a promotion to me."
    yt "I don't want to drag Lily into this, so I'll just go along with it."
    mc "Yeah, probably. Ehe he he..."
    mc "I'll rest a couple days then."
    l "Good! Just leave this to me and Freya. We may only meet today, but I can feel that she's a good workmate."
    scene i520
    with dissolve
    l "Oh! She's here!"
    l "Alright, [mc]. We'll have to prepare for the opening now. Bye~!"
    mc "Good bye for now, Lily. And good luck!"
    l "Yup! Wish me luck!"
    scene i521
    with dissolve
    $ renpy.pause()
    scene i522
    with dissolve
    s "Well, well, well... Look who's got a day off..."
    a "Not just one, but two days off! How lucky for you, [mc]!"
    a "Your boss must be really nice~!"
    mc "Well, yeah... Miss Jess is an extremely nice person. But she can be quite strict when she needs it."
    mc "I only saw her get angry once before, and she's quite intimidating!"
    s "*giggles* You must be really proud that you are her employee if you're talking about her that much!"
    mc "She has helped me in a lot of ways, so yeah! I'm proud to work under her. Haha."
    scene i523
    with dissolve
    a "Hmmm....."
    s "Aine?"
    a "I'm not really sure... but... that name sounds familiar."
    yt "Well... that's probably because she knows your mother?"
    a "It's like I've met her somewhere before? I think during my childhood?"
    a "However, I can't remember her at all."
    yt "Hm... Seems like Miss Jess has a deeper relationship with their mother. I guess I will find out once I talk to her."
    yt "I'll just have to make sure to ask her everything."
    yt "Also, I think it's best not to tell Aine anything about it."
    yt "At least, for now... since I don't know how she'll react."
    mc "That's weird..."
    a "Yeah..."
    scene i524
    with dissolve
    mc "Well... I'll leave you guys for now. I have to unpack my things and change my clothes."
    s "Sure! We'll see you later at lunch time!"
    mc "Oh yeah! Now that it's my rest day, I'll take care of our lunch this time."
    s "Ooh... nice! Thanks, [mc]."
    mc "No problem! Just focus on your job for now, Sky. You're already working too much to begin with."
    s "Got it."
    stop music fadeout 2

    scene black
    with dissolve
    with fade

    play music 'audio/SultansSwing.mp3'
    scene i525
    with dissolve
    mc "I told myself to not spend money on this gacha called 'Wish', but this new character makes my mouth water!"
    mc "Aahhh! I already spent 5 wishes but the game still won't give him to me! Damn RNG!"
    mc "...Alright, alright! Two more! Last two rolls!"
    scene i526
    mc "...C'mon, c'mon, c'mon.........."
    scene i527
    with dissolve
    mc "......"
    show i528
    with hpunch
    mc "Noooooooo~! Why can't you just give the character to me~?!"
    scene i525
    with dissolve
    mc "Graaaaahhh! One last time!"
    scene i526
    mc "Come on, please, please, please, please, please~!"
    mc "Pleeeeaaaaasssseee~!"
    scene i527
    with dissolve
    mc "......"
    scene i529
    with dissolve
    mc "WHAA~!"
    scene i530
    with hpunch
    mc "YESAAAAAAAAAAAH~!!!"
    show i531
    play sound 'audio/woosh.mp3'
    mc "WAHAHAHAHA~!! WOOOOOOOO~!!"
    show i532
    play sound 'audio/woosh.mp3'
    $ renpy.pause()
    scene i533
    play sound 'audio/woosh.mp3'
    pause
    scene i534
    play sound 'audio/woosh.mp3'
    mc "I got him. I got him. I got him."
    mc "Woot, woooot~!"
    play sound 'audio/opendoor.mp3'
    show i535
    g "Hey, [mc]! Why are you so noi..."
    scene i536
    with dissolve
    g "...sy..."
    g "*gulp*"
    g "Oh, uhm... sorry. I didn't mean to..."
    g "Y-you were just so loud that... I..."
    g "{i}Gosh~! Why am I...{/i}"
    scene i537
    with dissolve
    mc "Gwen?"
    mc "Sorry, were you sleeping? Did I wake you up?"
    scene i538
    with dissolve
    g "N-no! Nevermind!"
    if skycelebrate:
        scene i539
        mc "Wait! Hold on, Gwen!"
        mc "Do you have a minute? I want to ask you about something."
        image gmcn:
            "i540.jpg"
            pause 3.0
            "i541.jpg"
            pause .2
            repeat
        show gmcn
        with dissolve
        g "Oh? Sure... What is it?"
        mc "I remember that you know a lot of places since you loved wandering around the town and cut classes."
        g "Ouch, that hits..."
        mc "Ah, sorry, did I overstepped my-"
        g "Naah, it's true anyways."
        g "Well, you're asking the right person. What kind of place you're looking for?"
        mc "I want to take Sky somewhere she can relax — maybe tomorrow since my boss gave me 2 days off."
        mc "She's been working a lot and not thinking about herself lately. So, I can at least help her relax even just for a day."
        scene i542
        with dissolve
        g "Dude, are you taking her on a date or something?"
        mc "No, not really. But... that's how she wants to think of it. Aha haaa..."
        show gmcn
        with dissolve
        g "Hey, there's nothing wrong with that, you know? Just some good old bonding time!"
        mc "Well, you have a point."
        scene i543
        with dissolve
        g "A place to relax, huh?"
        g "Hmm..."
        show gmcn
        g "Ahh! I have a private beach that I own not that far from here..."
        mc "Hold up... you already own a place like that?!"
        g "Well, yes! I may have been at the bottom of the class during high school, but I worked my butt off during college, you know?"
        mc "Yeah, I know! You even inherited your father's company. I'm just a little bit shocked, that's all. Haha!"
        scene i544
        with dissolve
        g "*sighs* Let's not talk about that right now."
        mc "Oh, sorry."
        g "That's alright."
        show gmcn
        with dissolve
        g "Now about the beach... I can give you guys access to it. But be sure to not litter around the place, alright?"
        g "I'm quite OCD when it comes to things like that. I want to keep everything nice and tidy."
        mc "No worries about that, but... really? That's so unlike you."
        g "Hah! Yeah, I got that with all the work ethics pounded into me by my father before he handed over the company to me."
        g "You're not the only one who can change, you know?"
        mc "Yeah, I know..."
        scene i545
        with dissolve
        g "Here, give me your phone number so I can message you the place's address, and a guide to the location as it's in a quite hidden area."
        show gmcn
        with dissolve
        mc "Sure!"
        mc "......"
        mc "Here you go."
        scene i546
        with dissolve
        g "Let's see..."
        g "......"
        scene i547
        with dissolve
        g "And... sent!"
        mc "Oh, you're right it's not that far from here."
        show gmcn
        with dissolve
        g "And take your time checking out the guide. I don't want you guys getting lost in there. Hahaha!"
        menu:
            "Thanks for the heads up":
                mc "Thanks for the heads up, Gwen!"
                g "No worries. Just spend some time with Sky and we'll take care of the house during that time."
                mc "Great! And thank you for letting us use your place."
                g "Don't sweat it. Just remember to keep the place clean, alright?"
                mc "Sure!"
                $ gwenpoint += 1
                $ renpy.notify(gwennotif)
            "Don't worry":
                mc "Don't worry, Gwen. We won't get lost."
                g "Hmm... Okay. Just spend some time with Sky and we'll take care of the house during that time."
                mc "Great! And thank you for letting us use your place."
                g "Don't sweat it. Just remember to keep the place clean, alright?"
                mc "Sure!"
        g "Alright... I'll go back in my room for now."
        mc "Okay!"
        play sound 'audio/closedoor.mp3'
        scene i548
        with dissolve
        yt "Was she looking at my body?"
        yt "Do I really look that juicy now? Hahahaha!"
    else:
        play sound 'audio/closedoor.mp3'
        scene i548
        with dissolve
        yt "Was she looking at my body?"
        yt "Do I really look that juicy now? Hahahaha!"

    scene i549
    with dissolve
    "*phone vibrates*"
    scene i550
    with dissolve
    mc "......"
    yt "A message from Miss Jess..."
    j "(Please check your e-mail. I sent all the details that you need to know.)"
    yt "Okay, let's check it out."

    scene black
    with dissolve
    with fade

    scene i551
    with dissolve
    yt "Hmmm..."
    yt "The date is really convenient. It's on my day off. And it's exactly 3 weeks from today."
    yt "......"
    yt "In a cafe, huh? Well, that's not what I expected."
    yt "Now I'm pretty sure that Miss Jess is in a close relationship with her for them to meet in a place like a cafe."
    yt "......"
    yt "I should wear nice clothes too?"
    yt "Okay, that's not a problem."
    yt "...There's a note at the very end of the email..."
    yt "......"
    yt "'Speak formally with her, and keep your composure no matter what she tells you. And good luck!'"
    yt "'Remember, this is the only chance I can give you.'"
    yt "I'll keep that in mind. Thanks, Miss Jess. I owe you one."
    scene i552
    with dissolve
    yt "Let's go and prepare lunch now."
    stop music fadeout 2

    scene black
    with Dissolve(2.0)
label gwenpause2:
    if _in_replay:
        $ name = persistent.gallery_name
    scene gwenpause2
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

    play music 'audio/LovelySwindler.mp3'
    scene i553
    with dissolve
    yt "Hmm... what should we have for lunch...?"
    yt "Maybe a low-fat Japanese menu will do."
    yt "Hah! Here I go again with my low-fat diet. I hope they'll like it though."

    scene black
    with dissolve
    with fade

    scene i554
    with dissolve
    mc "*hums* Hmm.. hm... hm hmm..."
    scene i555
    with dissolve
    $ renpy.pause()
    scene i556
    with dissolve
    $ renpy.pause()
    scene i557
    s "*hugs*"
    scene i558
    with dissolve
    s "{i}Ah...{/i}"
    scene i559
    with dissolve
    mc "Oh... hey, Sky! Are you done with your work?"
    s "Not yet, but it's already my lunch break, I still have to go back at 1pm though."
    mc "How's Aine doing? She's not causing you any problems, is she?"
    s "Nope! She's working flawlessly to be honest. She had an experience, so it's not surprising."
    mc "That's good to hear!"
    if skycelebrate:
        image smckh:
            "i560.jpg"
            pause 3.0
            "i561.jpg"
            pause .2
            repeat
        show smckh
        with dissolve
        mc "Oh, by the way... Are you free tomorrow? Since I don't have to go to work, I was thinking of taking you to a private beach so you could relax."
        s "Ehh... A private beach? Isn't that expensive, since it's not being offered to the public?"
        mc "Normally it would be. But Gwen was kind enough to let us use her place."
        mc "We have to keep the place clean in exchange though."
        s "Whoa~! So, she owns the beach we're going into?!"
        mc "Yeah, I was a bit shocked too. But yes, she owns the place."
        image smckh2:
            "i562.jpg"
            pause 3.0
            "i563.jpg"
            pause .2
            repeat
        show smckh2
        with dissolve
        s "Then, I should thank her later. And of course, I told you that I can free up my schedule for our date, right?"
        s "I'm pretty excited already, if you ask me!"
        mc "Alright then. We'll go early in the morning tomorrow. You should pack your things later."
        s "Roger! Hehe!"
        s "But we have to stop by a clothing store first."
        s "We haven't been able to go to a beach for years, the only bikini I have might not fit anymore."
        if skyroute:
            yt "Oh, sweet baby Jesus..."
            yt "Sky... in a bikini?"
            yt "Tomorrow's already looking like a perfect day. Hahaha!"
            yt "Oops. There I go again..."
            yt "...Thinking dirty thoughts about Sky."
            scene i564
            with dissolve
            s "I'm guessing you're already picturing me in a bikini... aren't you?"
            mc "What the—are you psychic now?"
            s "So I was right, huh?"
            s "You're such a perv~!"
            yt "Yep... she's definitely messing with me."
    image smckh3:
        "i565.jpg"
        pause 3.0
        "i566.jpg"
        pause .2
        repeat
    show smckh3
    with dissolve
    s "But this is not a time to chit chat. Everyone's going to come down soon. Let me help you finish cooking."
    mc "Oh, yeah... Okay... it will be faster that way."
    s "Four hands are better than two, right? Hehe!"
    mc "'Four hands'... that reminds me of Rachmaninov's piano arrangement. Hahahaha!"
    s "I didn't know you have a preference for classical music..."
    mc "A little bit, yeah. I picked it up from Klara, I guess."
    mc "I stumbled upon it while listening to some music before."
    s "What's the title called?"
    mc "Hm... I think it's called 'Sleeping Beauty Waltz for Piano 4 Hands'. That was why I was reminded of it when you said 4 hands."
    s "Ehh... I can't really relate to it. I don't like classical music."
    mc "I can't blame you. Only a few people in our generation can really appreciate classical music."
    s "That's true..."
    mc "You watch animes, right? I think they played it in a musical anime too!"
    s "Really?!"
    mc "But, I don't want to tell you the title of the anime. Hahaha!"
    image smckh4:
        "i567.jpg"
        pause 3.0
        "i568.jpg"
        pause .2
        repeat
    show smckh4
    with dissolve
    s "Ehhhh? Why? I want to watch it!"
    mc "I don't want you to cry like a sissy and blame me later that I let you watch it. Hahaha!"
    s "Oh, come on..."
    mc "It happened several times before so... nope!"
    s "Ehh...?"
    mc "Come on, let's finish this before everyone comes down."
    show smckh3
    with dissolve
    s "Okay... But you tell me the title of that anime later, alright?"
    mc "Alright, alright. But promise me you're not going to cry. Hahaha!"
    s "If it's a sad anime, then I won't make any promises."
    mc "*sighs*"
    stop music fadeout 2

    if skycelebrate:
        scene black
        with dissolve
        with fadeq

        "Time passes by..."

        scene black
        with dissolve
        with fadeq

        "In the morning..."

        scene black
        with dissolve
        with fadeq

        play music 'audio/MBBSax.mp3'
        scene i569
        with dissolve
        yt "Ahh... The morning breeze and the sun shines upon me!"
        yt "I haven't had this feeling for a while. It feels good to get out of the house from time to time."
        yt "Well... I go outside almost everyday for work, but it feels different when I'm not thinking about it."
        yt "It's not just Sky who can relax, but me as well. Haha!"
        yt "I will have to thank Miss Jess when she visits the burger shack next time."
        scene i570
        with dissolve
        s "Hey~! I'm ready!"
        mc "Alright, should we go?"
        s "Okie dokie! Let's stop by the clothing store first."
        mc "No problem!"

        scene black
        with dissolve
        with fade

        scene i571
        with dissolve
        s "Here we are!"
        scene i572
        with dissolve
        s "Just stay here, [mc]. I will ask the cashier for help."
        mc "Oh, sure! Take your time!"
        scene i573
        with dissolve
        li "Good morning, miss. How may I help you?"
        scene i574
        with dissolve
        s "Uhm... I'm looking for swimwear. Do you guys have any?"
        scene i573
        with dissolve
        li "Of course, we have a huge selection here."
        li "Please come this way."

        scene black
        with dissolve
        with fadeq

        "A few moments later..."

        scene black
        with dissolve
        with fadeq

        scene i575
        with dissolve
        yt "These look pretty high quality!"
        scene i576
        with dissolve
        li "Good morning, sir. Are you looking for something?"
        mc "Oh, nah..."
        mc "I was only looking at these. They look pretty well made, I must say."
        li "Right? That's one of my partner's favorite shirts."
        li "I'm sure your girlfriend will like you wearing it too!"
        scene i577
        with dissolve
        mc "Uhm... not really. She's my-"
        scene i578
        s "[mc]~! Can you come here, please?"
        scene i577
        with dissolve
        mc "Oops, sorry. She's calling for me."
        li "No worries, sir. You guys take your time."
        scene black
        with dissolve
        scene i579
        with dissolve
        mc "Yes, Sky? Do you need some help?"
        s "Uhm... The cashier helped me find some suits, and I picked two of them."
        s "But, I'm not really sure which one I should choose, they both look so pretty~!"
        s "Can you help me pick one, please?"
        s "I'm wearing the first one right now. I'll open the door so you can see it."
        mc "Alright, let me see..."
        scene black
        play sound 'audio/opendoor.mp3'
        with dissolve
        scene i580
        with dissolve
        s "Here it is..."
        yt "Oh, Christ..."
        yt "She looks awesome in it! But I should give her my honest opinion."
        image sbw1:
            "i581.jpg"
            pause 3.0
            "i582.jpg"
            pause .2
            repeat
        show sbw1
        with dissolve
        menu:
            "It looks good on you":
                mc "To be honest, it's fairly simple. But at the same time, it looks good on you."
                mc "You don't really have to wear anything flashy to look beautiful, Sky."
                s "Really? Hehe! Thanks!"
                $ skypoint += 1
                $ renpy.notify(skynotif)
            "Too plain":
                mc "To be honest, you look good, Sky! But it looks too plain on you. Let's see how the second one looks."
                s "Hmmn... Okay~! Hihi!"

        scene black
        play sound 'audio/opendoor.mp3'
        with dissolve
        scene i583
        with dissolve
        s "Then, how about this one?"
        yt "Holy mother of-"
        if skyroute:
            yt "Damn... she looks insanely hot right now."
            yt "She's straight-up fire."
            yt "I can't even pretend she's not completely captivating me."
        else:
            yt "Uh-oh... here we go again. I really need to get a grip..."
            yt "*sighs* I keep telling myself to chill, but... she's just straight-up fire."
        image sbw2:
            "i584.jpg"
            pause 3.0
            "i585.jpg"
            pause .2
            repeat
        show sbw2
        with dissolve
        s "Hey~! Don't just stare at me! *giggle*"
        mc "Oh... sorry."
        s "So, how do I look?"
        yt "What should I tell her?"
        menu:
            "It looks alright":
                mc "It looks alright, I guess..."
                s "Ehh...?"
            "You look hot":
                mc "I'm not gonna lie, Sky. You look really hot in it."
                mc "If we were going to a public beach, I bet other people would be turning their heads towards you."
                s "Hmmn... You're not saying that just to make me happy, right?"
                mc "No, I'm being completely honest. Hahaha!"
                mc "And why would I lie? There's nothing you wear that can make you look ugly, Sky."
                s "Hehe! Thank you!"
                $ skypoint += 1
                $ renpy.notify(skynotif)
        s "So... which one should I wear later, then?"
        mc "Are you sure you want me to decide which one you'll wear?"
        s "Of course! You're the only one who will be able to see it anyway, so I'm leaving it up to you. *giggles*"
        yt "Hmmm... This is a hard one. Both look good on her to be honest."
        yt "But, if I really have to choose..."
        menu:
            "The first one":
                $ skywear = True
                mc "Then, I'll pick the first one!"
                s "Alright~! I'll use that one later, then!"
            "This one":
                $ skywear = False
                mc "Then, I'll pick this one!"
                s "Alright~! I'll use this one later, then!"

        s "But, to be honest, either choice looks good, so I'm going to buy them both."
        mc "Are you sure? You shouldn't spend too much money on these things, you know?"
        s "You're talking like Mom, [mc]!"
        s "Don't worry, it's not like I took the money from my savings anyway."
        s "What's more, I can continue to use them in the future."
        mc "Hm... Alright, I won't argue about it since this is your day."
        s "*giggles*"
        s "I'll change into my clothes and pay the cashier so we can go."
        mc "Okay!"

        scene black
        with dissolve
        with fade

        scene i573
        with dissolve
        li "Thank you for coming to our store, please have a great day!"
        s "Thanks! You do the same."
        scene i586
        with dissolve
        mc "All done?"
        s "Yep! Let's go! I can't wait to see what the beach looks like!"
        mc "Me too! And don't worry, we have until afternoon to enjoy it."

        scene black
        with dissolve
        with fadeq

        "A few hours later..."

        scene black
        with dissolve
        with fadeq

        scene i587
        with dissolve
        yt "Looking at the address..."
        yt "Yeah, there's no mistaking it, we're here."
        yt "It looks like a private beach indeed! This place is very well hidden and seems like a great place to relax."
        scene i588
        with dissolve
        yt "This feeling..."
        yt "The refreshing ocean breeze..."
        scene i589
        with dissolve
        yt "The gentle waves of the sea..."
        scene i590
        with dissolve
        yt "And a beautiful... blue... Sky..."
        scene i591
        with dissolve
        "*thump*"
        scene i592
        with dissolve
        yt "Ahh... and it looks like I'm... really..."
        scene i593
        with dissolve
        s "Hehehe~! The beach~!"
        s "Look, [mc]~! It's the beach!"
        yt "... in love with Sky..."
        yt "We've been holding it back all this time..."
        yt "Telling ourselves that it is something that we shouldn't do..."
        yt "Our love is forbidden... and yet, why...?"
        yt "Why does fate seem to really bring our hearts together no matter how much we hold back?"
        scene i594
        with dissolve
        s "C'mon, [mc]! What are you standing there for? It's time to plunge in! Hehehe!"
        mc "W-wait! Hold on! We should change into our swimwear first! I only have one set of clothes with me!"
        s "Oh, right... I only have one set with me too..."
        mc "Jeez..."
        yt "If only... the circumstances were different..."
        s "Hey! Let's go~!"
        mc "I know, just calm down, Sky."

        scene black
        with dissolve
        with fadeq

        "A few moments later..."

        scene black
        with dissolve
        with fadeq

        if skywear:
            label skycelebratewear1:
            if _in_replay:
                $ name = persistent.gallery_name
            scene i595
            with dissolve
            s "Oh wow~! You look pretty awesome, [mc]!"
            s "It's been a while since you went to the gym, hasn't it?"
            mc "That's thanks to you helping with my diet."
            mc "But, don't mind me. You look friggin awesome yourself!"
            s "Hehe. Thanks!"
            scene i597
            with dissolve
            s "Although, sometimes I wish I could be a little bit taller, you know?"
            menu:
                "Your height doesn't matter":
                    mc "To be honest, your height doesn't really matter. You already look beautiful as you are right now."
                "You look cute":
                    mc "You look cute as you are right now, Sky. You don't need any more height. Haha!"
            scene i599
            with dissolve
            s "*blushes*"
            s "{i}Yep... and there goes our 'holding back'. *sighs*{/i}"
            scene i601
            with dissolve
            mc "Come on! You wanted to 'plunge in' right? Haha!"
            s "Ahh! Wait, what are you..."
            scene i603
            with dissolve
            mc "Canon ball~!!!"
            s "*screams* AAAHHH~!!"
            show black
            with hpunch
            play sound 'audio/watersplash.mp3'
            "*SPLASH*!!"
            scene i605
            with dissolve
            s "Fuwaaah~!"
            scene i607
            with dissolve
            mc "Ahahahahahahaha~!!"
            mc "If only you could've seen your face just now! Ahahahaha!"
            mc "Ouch! My... stomach! Ahahaha!"
            scene i609
            with dissolve
            s "Hrrmmmnnnn~! So you find it funny, huh?!"
            scene i611
            with dissolve
            $ renpy.pause()
            scene i613
            with hpunch
            s "Here, take... this!"
            scene i615
            with dissolve
            mc "Aw!!"
            scene i616
            with dissolve
            mc "What the heck?!"
            mc "Come here, you little..."
            scene i617
            with dissolve
            mc "*tickles*"
            s "WAHAHAHA!! AHA! AHAHAHA!!"
            s "S-stop!"
            scene i619
            with dissolve
            s "EHEHE HEHE EHEHE!! I said stop~! AHAHA HAHA!"
            mc "Nope! Not stopping! Ahahaha! My face still hurts because of that ball you threw at me, and you're gonna pay the price! Haha!"
            scene i621
            with dissolve
            s "{i}*gasps* His hands are almost...{/i}"
            s "{i}...reaching my...{/i}"
            scene i623
            with dissolve
            s "*moans* M-mmnnhh~!!"
            yt "Oh, shit! My hands reached Sky's breast without me noticing!"
            stop music fadeout 2
            scene i625
            with dissolve
            mc "Shit! I'm sorry, Sky. I didn't notice my-"
            play music 'audio/MakeMeFeel.mp3'
            s "N-no! P-please don't... stop, [mc]..."
            mc "Huh? Don't you want me to stop tickling you?"
            s "No, I mean..."
            scene i627
            with dissolve
            s "Please, don't stop..."
            if skyroute:
                scene i629
                with dissolve
                mc "A-are you sure? Are we really... going to do it... again?"
                s "Yeah... what is there to even think of? We already crossed the line before."
                s "I..."
                s "I want you again... [mc]..."
                yt "Aw shit! This look... is what got me before! And now, it's turning me on again!"
            else:
                scene i629
                with dissolve
                mc "A-are you sure? We shouldn't be doing this, Sky. I just accidentally touched your... uhm..."
                s "What is there to even think of? We already crossed the line before."
                s "I..."
                s "I want you again... [mc]..."
                yt "Aw shit! This look... is what got me before! And now, it's turning me on again!"

            scene i631
            with dissolve
            mc "Why the heck do you have to look so cute at such a crucial moment, Sky?"
            s "*giggles* I don't know... All I know... is that I want you... to make love with me."
            s "Am I... turning you on?"
            mc "Of course! You are a woman. And... a beautiful one..."
            mc "A woman who takes care of me."
            mc "And... a woman who loves me more than anyone else..."
            yt "Aw jeez... I'm just speaking what my heart tells me..."
            s "I can hear your heartbeat getting louder and louder, you know?"
            mc "Sky..."
            show sky8
            with dissolve
            $ renpy.pause()
            s "*moans* Mmmnnhh~! Ahhh~!"
            mc "Your nipples are getting harder, Sky..."
            s "That's because... I'm turned on right now. Mmnnhh~!"
            s "It... feels so good, [mc]."
            $ renpy.pause()
            show sky10
            with dissolve
            $ renpy.pause()
            s "*moans* Hnng! Mnnhh! Haaaah~!"
            s "My pussy is getting really wet, [mc]~! I... I want more!"
            $ renpy.pause()
            mc "Then, I want to taste you, Sky..."
            s "Let's get out of the water."
            mc "Alright."

            scene black
            with dissolve
            with fade

            scene i633
            with dissolve
            mc "Let's do it here."
            s "You don't have to tell me, [mc]."
            s "You can do what you want to me. *giggles*"
            mc "If that's the case... then..."
            show sky12
            with dissolve
            $ renpy.pause()
            s "Ohhh~! [mc]~! That feels really good~!"
            s "*moans* Mnnhhh~! Yes that's it! Lick my pussy harder!"
            $renpy.pause()
            show sky13
            with dissolve
            $ renpy.pause()
            s "*moans* Haah~! Yes, Yes! Do me more!"
            mc "You taste really good, Sky!"
            mc "I haven't told you before, but you taste like strawberries to me."
            s "Really? Then, you must really like it."
            mc "Yes, I do like it. Hehe."
            $ renpy.pause()
            scene i633
            with dissolve
            s "That's enough, [mc]... It's my turn now."
            mc "Are you sure?"
            s "Yeah!"
            mc "Alright then..."

            scene black
            with dissolve
            with fadeq

            scene i634
            with dissolve
            s "I really wanted to do this before, but you stopped me right away after I took it out. *giggles*"
            mc "That's because I was so shocked. It's not something that you do often, you know?"
            s "Well... It doesn't matter now."
            scene i635
            with dissolve
            s "Mmphh~ It's... so big~!"
            mc "Sky, you don't have to do it, really..."
            s "No, I want to."
            show sky14
            with dissolve
            $ renpy.pause()
            s "Mnh..."
            s "*slurps*"
            mc "Aw... s-shit, Sky! That feels so good~!"
            s "*giggles* I'm glad you like it."
            $ renpy.pause()
            show sky15
            with dissolve
            $ renpy.pause()
            mc "Fuck! Not too fast, Sky... or I'll..."
            $ renpy.pause()
            scene i634
            with dissolve
            s "No, not yet."
            s "Put it inside me, [mc]. I want you now!"
            mc "O-okay..."
            scene i636
            with dissolve
            mc "Let's do it this way..."
            scene i637
            with dissolve
            s "My pussy is really wet right now..."
            s "I'm sure it will..."
            scene i638
            with dissolve
            s "...go..."
            scene i639
            with dissolve
            s "...right..."
            scene i640
            with dissolve
            s "...IN~!!!"
            s "Haaaah~ [mc]... You're so big~! It's reaching even deeper than last time!"
            mc "I'm going to move now, Sky!"
            scene i641
            with dissolve
            s "Go on~ You don't have to hold back."
            show sky16
            with dissolve
            $ renpy.pause()
            s "*moans* Aahhh~! Haaah~! Hnnng~!"
            mc "You're just as tight as I remember, Sky!"
            s "Harder, [mc]~! Do it harder~!"
            $ renpy.pause()
            show sky17
            with dissolve
            $ renpy.pause()
            s "*moans* Haah~! Ahh~! Aahh~! Aahh~!"
            $ renpy.pause()
            show sky18
            with dissolve
            $ renpy.pause()
            s "[mc]... I'm almost there!"
            mc "Shit! I can't hold it any longer too, Sky!"
            s "Cum inside me, [mc]!"
            s "Let's cum together~!"
            mc "A-alright!"
            $ renpy.pause()
            scene i642
            with dissolve
            s "HAAAAAAAHHHHHHH~!!!"
            mc "Arrggh~!!"
            with hpunch
            $ renpy.pause()
            with hpunch
            $ renpy.pause()
            with hpunch
            $ renpy.pause()
            scene i643
            with dissolve
            s "*huff* I can... *huff* feel it inside me... it's... so hot..."

            scene black
            with dissolve
            with fade

            scene i644
            with dissolve
            s "Tell me, [mc]..."
            s "Do you... really love me?"
            s "Not just as your childhood friend, but as something more than that."
            s "Because I really love you, [mc]."
            s "I was trying to hold back my feelings for you after we talked about what happened before."
            s "We both told each other that it was just an accident and just a spur of the moment."
            s "We said that we shouldn't have done that... but... I can't, [mc]."
            s "I can't hold it back any longer..."
            s "I'm not seeing you as my childhood friend anymore, [mc]. Even way before we made love for the first time."
            s "I know that my feelings for you are forbidden, it's not right."
            s "But... I don't care where this will take me. I don't care what will happen to us."
            s "I can never be your girlfriend... but, at least treat me like one. That's all I want."
            s "But if you tell me that you don't love me... then... I will just have to kill my feelings for you and pretend that everything never happened."
            yt "I already know that she's madly in love with me..."
            yt "And us holding our feelings back never helped take it away. Even I admit that..."
            yt "Yes, I am in love with her... I tried to deny it. But, my heart is still longing for her."
            yt "However, I should make the right choice here."
            yt "Do I pursue my feelings for Sky?"
            yt "Or should I deny her and end this once and for all?"
            menu:
                "Pursue your feelings":
                    $ skyroute = True
                    scene i645
                    with dissolve
                    mc "I'll be honest with you, Sky..."
                    mc "Yeah... I love you. And it's not just as a childhood friend."
                    mc "I've tried to ignore it. Tried to push it down and convince myself it wasn't real..."
                    mc "But the truth is, I find myself longing for you, even when I shouldn't."
                    mc "That morning you didn't wake me up? It threw my whole day off. I missed you beside me."
                    mc "And no matter how hard I try to look away, my eyes always find their way back to you."
                    mc "We live under the same roof, we've been through so much together..."
                    mc "And maybe that's why it's terrifying to feel this way. But I do."
                    mc "I won't hide it anymore, Sky."
                    mc "Let people talk—I don't care. I love you."
                    scene i646
                    with dissolve
                    s "*blushes* My heart... it's racing so fast right now, [mc]."
                    s "I... I think I'm gonna cry..."
                    s "*sniffs*"
                    s "I love you too, [mc]. So much more than I ever let myself say out loud."
                    mc "But... don't you think this all happened kind of fast?"
                    s "Maybe... but we've been holding it in for years. I think it's about time we stopped pretending."
                    mc "...You're right."
                    s "Hehe~!"
                    scene i648
                    with dissolve
                    mc "Come here..."
                    mc "You've been working yourself to the bone. Let me take care of you for once."
                    s "Hehe. I know... And thank you for bringing me here."
                    mc "Anything for you, Sky."
                    mc "Now rest."
                    s "{i}This might be where we are now... but I'm not settling for 'just for now'... *giggles*{/i}"
                    scene i650
                    with dissolve
                    mc "*sighs*"
                    yt "......"
                    yt "..........."
                    yt "The sand may brush off..."
                    yt "The salt may wash away..."
                    yt "The tans might fade..."
                    yt "But these memories—"
                    yt "... these ones will last forever."
                "Deny her":
                    $ skyroute = False
                    scene i647
                    with dissolve
                    mc "*sighs* I'll be honest with you, Sky."
                    mc "Yes, I love you. And yeah, I've felt more than just... whatever this thing between us is."
                    mc "But I still think we're crossing a line we might not come back from."
                    mc "I know this hurts. Believe me—it hurts me too."
                    mc "But I think we need to stop this now... before it changes everything between us."
                    s "*sighs* I figured you'd say that."
                    s "And honestly? I agree. Maybe it's better this way."
                    mc "I'm glad you understand."
                    s "I'll be okay. I just need a little time to move forward."
                    scene i649
                    with dissolve
                    mc "Come here..."
                    mc "You've been working hard. You deserve a moment of peace."
                    s "I know... And thank you for bringing me here."
                    mc "Anytime, Sky."
                    mc "Now rest."
            $ renpy.end_replay()
            stop music fadeout 2
        else:
            label skycelebratewear2:
            if _in_replay:
                $ name = persistent.gallery_name
            scene i596
            with dissolve
            s "Oh wow~! You look pretty awesome, [mc]!"
            s "It's been a while since you went to the gym, hasn't it?"
            mc "That's thanks to you helping with my diet."
            mc "But, don't mind me. You look friggin awesome yourself!"
            s "Hehe. Thanks!"
            scene i598
            with dissolve
            s "Although, sometimes I wish I could be a little bit taller, you know?"
            menu:
                "Your height doesn't matter":
                    mc "To be honest, your height doesn't really matter. You already look beautiful as you are right now."
                "You look cute":
                    mc "You look cute as you are right now, Sky. You don't need any more height. Haha!"
            scene i600
            with dissolve
            s "*blushes*"
            s "{i}Yep... and there goes our 'holding back'. *sighs*{/i}"
            scene i602
            with dissolve
            mc "Come on! You wanted to 'plunge in' right? Haha!"
            s "Ahh! Wait, what are you..."
            scene i604
            with dissolve
            mc "Canon ball~!!!"
            s "*screams* AAAHHH~!!"
            show black
            with hpunch
            play sound 'audio/watersplash.mp3'
            "*SPLASH*!!" with hpunch
            scene i606
            with dissolve
            s "Fuwaaah~!"
            scene i608
            with dissolve
            mc "Ahahahahahahaha~!!"
            mc "If only you could've seen your face just now! Ahahahaha!"
            mc "Ouch! My... stomach! Ahahaha!"
            scene i610
            with dissolve
            s "Hrrmmmnnnn~! So you find it funny, huh?!"
            scene i612
            with dissolve
            $ renpy.pause()
            scene i614
            with hpunch
            s "Here, take... this!"
            scene i615
            with dissolve
            mc "Aw!!"
            scene i616
            with dissolve
            mc "What the heck?!"
            mc "Come here, you little..."
            scene i618
            with dissolve
            mc "*tickles*"
            s "WAHAHAHA!! AHA! AHAHAHA!!"
            s "S-stop!"
            scene i620
            with dissolve
            s "EHEHE HEHE EHEHE!! I said stop~! AHAHA HAHA!"
            mc "Nope! Not stopping! Ahahaha! My face still hurts because of that ball you threw at me, and you're gonna pay the price! Haha!"
            scene i622
            with dissolve
            s "{i}*gasps* His hands are almost...{/i}"
            s "{i}...reaching my...{/i}"
            scene i624
            with dissolve
            s "*moans* M-mmnnhh~!!"
            yt "Oh, shit! My hands reached Sky's breasts without me noticing!"
            stop music fadeout 2
            scene i626
            with dissolve
            mc "Shit! I'm sorry, Sky. I didn't notice my-"
            play music 'audio/MakeMeFeel.mp3'
            s "N-no! P-please don't... stop, [mc]..."
            mc "Huh? You don't want me to stop tickling you?"
            s "No, I mean..."
            scene i628
            with dissolve
            s "Please, don't stop..."
            if skyroute:
                scene i630
                with dissolve
                mc "A-are you sure? Are we really... going to do it... again?"
                s "Yeah... what is there to even think of? We already crossed the line before."
                s "I..."
                s "I want you again... [mc]..."
                yt "Aw shit! This look... is what got me before! And now, it's turning me on again!"
            else:
                scene i630
                with dissolve
                mc "A-are you sure? We shouldn't be doing this, Sky. I just accidentally touched your... uhm..."
                s "What is there to even think of? We already crossed the line before."
                s "I..."
                s "I want you again... [mc]..."
                yt "Aw shit! This look... is what got me before! And now, it's turning me on again!"

            scene i632
            with dissolve
            mc "Why the heck do you have to look so cute at such a crucial moment, Sky?"
            s "*giggles* I don't know... All I know... is that I want you... to make love with me."
            s "Am I... turning you on?"
            mc "Of course! You're a woman. And... a beautiful one..."
            mc "A woman who takes care of me."
            mc "And... a woman who loves me more than anyone else..."
            yt "Aw jeez... I'm just saying what my heart tells me..."
            s "I can hear your heartbeat getting louder and louder, you know?"
            mc "Sky..."
            show sky9
            with dissolve
            $ renpy.pause()
            s "*moans* Mmmnnhh~! Ahhh~!"
            mc "Your nipples are getting harder, Sky..."
            s "That's because... I'm turned on right now. Mmnnhh~!"
            s "It... feels so good, [mc]."
            $ renpy.pause()
            show sky11
            with dissolve
            $ renpy.pause()
            s "*moans* Hnng! Mnnhh! Haaaah~!"
            s "My pussy is getting really wet, [mc]~! I... I want more!"
            $ renpy.pause()
            mc "Then, I want to taste you, Sky..."
            s "Let's get out of the water."
            mc "Alright."

            scene black
            with dissolve
            with fade

            scene i633
            with dissolve
            mc "Let's do it here."
            s "You don't have to tell me, [mc]."
            s "You can do what you want to me. *giggles*"
            mc "If that's the case... then..."
            show sky12
            with dissolve
            $ renpy.pause()
            s "Ohhh~! [mc]~! That feels really good~!"
            s "*moans* Mnnhhh~! Yes that's it! Lick my pussy harder!"
            $ renpy.pause()
            show sky13
            with dissolve
            $ renpy.pause()
            s "*moans* Haah~! Yes, Yes! Do me more!"
            mc "You taste really good, Sky!"
            mc "I haven't told you before, but you taste like strawberries to me."
            s "Really? Then, you must really like it."
            mc "Yes, I do like it. Hehe."
            $ renpy.pause()
            scene i633
            with dissolve
            s "That's enough, [mc]... It's my turn now."
            mc "Are you sure?"
            s "Yeah!"
            mc "Alright then..."

            scene black
            with dissolve
            with fadeq

            scene i634
            with dissolve
            s "I really wanted to do this before, but you stopped me right away after I took it out. *giggles*"
            mc "That's because I was so shocked. It's not something that you do often, you know?"
            s "Well... It doesn't matter now."
            scene i635
            with dissolve
            s "Mmphh~ It's... so big~!"
            mc "Sky, you don't have to do it, really..."
            s "No, I want to."
            show sky14
            with dissolve
            $ renpy.pause()
            s "Mnh..."
            s "*slurps*"
            mc "Aw... s-shit, Sky! That feels so good~!"
            s "*giggles* I'm glad you like it."
            $ renpy.pause()
            show sky15
            with dissolve
            $ renpy.pause()
            mc "Fuck! Not too fast, Sky... or I'll..."
            $ renpy.pause()
            scene i634
            with dissolve
            s "No, not yet."
            s "Put it inside me, [mc]. I want you now!"
            mc "O-okay..."
            scene i636
            with dissolve
            mc "Let's do it this way..."
            scene i637
            with dissolve
            s "My pussy is really wet right now..."
            s "I'm sure it will..."
            scene i638
            with dissolve
            s "...go..."
            scene i639
            with dissolve
            s "...right..."
            scene i640
            with dissolve
            s "...IN~!!!"
            s "Haaaah~ [mc]... You're so big~! It's reaching even deeper than last time!"
            mc "I'm going to move now, Sky!"
            scene i641
            with dissolve
            s "Go on~ You don't have to hold back."
            show sky16
            with dissolve
            $ renpy.pause()
            s "*moans* Aahhh~! Haaah~! Hnnng~!"
            mc "You're just as tight as I can remember, Sky!"
            s "Harder, [mc]~! Do it harder~!"
            $ renpy.pause()
            show sky17
            with dissolve
            $ renpy.pause()
            s "*moans* Haah~! Ahh~! Aahh~! Aahh~!"
            $ renpy.pause()
            show sky18
            with dissolve
            $ renpy.pause()
            s "[mc]... I'm almost there!"
            mc "Shit! I can't hold it any longer too, Sky!"
            s "Cum inside me, [mc]!"
            s "Let's cum together~!"
            mc "A-alright!"
            $ renpy.pause()
            scene i642
            with dissolve
            s "HAAAAAAAHHHHHHH~!!!"
            mc "Arrggh~!!"
            with hpunch
            $ renpy.pause()
            with hpunch
            $ renpy.pause()
            with hpunch
            $ renpy.pause()
            scene i643
            with dissolve
            s "*huff* I can... *huff* feel it inside me... it's... so hot..."

            scene black
            with dissolve
            with fade

            scene i644
            with dissolve
            s "Tell me, [mc]..."
            s "Do you... really love me?"
            s "Not just as your childhood friend, but as something more than that."
            s "Because I really love you, [mc]."
            s "I was trying to hold back my feelings for you after we talked about what happened before."
            s "We both told each other that it was just an accident and just a spur of the moment."
            s "We said that we shouldn't have done that... but... I can't, [mc]."
            s "I can't hold it back any longer..."
            s "I'm not seeing you as my childhood friend anymore, [mc]. Even way before we made love for the first time."
            s "I know that my feelings for you are forbidden, it's not right."
            s "But... I don't care where this will take me. I don't care what will happen to us."
            s "I can never be your girlfriend... but, at least treat me like one. That's all I want."
            s "But if you tell me that you don't love me... then... I will just have to kill my feelings for you and pretend that everything never happened."
            yt "I already know that she's madly in love with me..."
            yt "And us holding our feelings back never helped take it away. Even I admit that..."
            yt "Yes, I am in love with her... I tried to deny it. But, my heart is still longing for her."
            yt "However, I should make the right choice here."
            yt "Do I pursue my feelings for Sky?"
            yt "Or should I deny her and end this once and for all?"
            menu:
                "Pursue your feelings":
                    $ skyroute = True
                    scene i645
                    with dissolve
                    mc "I'll be honest with you, Sky..."
                    mc "Yeah... I love you. And it's not just as a childhood friend."
                    mc "I've tried to ignore it. Tried to push it down and convince myself it wasn't real..."
                    mc "But the truth is, I find myself longing for you, even when I shouldn't."
                    mc "That morning you didn't wake me up? It threw my whole day off. I missed you beside me."
                    mc "And no matter how hard I try to look away, my eyes always find their way back to you."
                    mc "We live under the same roof, we've been through so much together..."
                    mc "And maybe that's why it's terrifying to feel this way. But I do."
                    mc "I won't hide it anymore, Sky."
                    mc "Let people talk—I don't care. I love you."
                    scene i646
                    with dissolve
                    s "*blushes* My heart... it's racing so fast right now, [mc]."
                    s "I... I think I'm gonna cry..."
                    s "*sniffs*"
                    s "I love you too, [mc]. So much more than I ever let myself say out loud."
                    mc "But... don't you think this all happened kind of fast?"
                    s "Maybe... but we've been holding it in for years. I think it's about time we stopped pretending."
                    mc "...You're right."
                    s "Hehe~!"
                    scene i648
                    with dissolve
                    mc "Come here..."
                    mc "You've been working yourself to the bone. Let me take care of you for once."
                    s "Hehe. I know... And thank you for bringing me here."
                    mc "Anything for you, Sky."
                    mc "Now rest."
                    s "{i}This might be where we are now... but I'm not settling for 'just for now'... *giggles*{/i}"
                    scene i650
                    with dissolve
                    mc "*sighs*"
                    yt "......"
                    yt "..........."
                    yt "The sand may brush off..."
                    yt "The salt may wash away..."
                    yt "The tans might fade..."
                    yt "But these memories—"
                    yt "... these ones will last forever."
                "Deny her":
                    scene i647
                    with dissolve
                    mc "*sighs* I'll be honest with you, Sky."
                    mc "Yes, I love you. And yeah, I've felt more than just... whatever this thing between us is."
                    mc "But I still think we're crossing a line we might not come back from."
                    mc "I know this hurts. Believe me—it hurts me too."
                    mc "But I think we need to stop this now... before it changes everything between us."
                    s "*sighs* I figured you'd say that."
                    s "And honestly? I agree. Maybe it's better this way."
                    mc "I'm glad you understand."
                    s "I'll be okay. I just need a little time to move forward."
                    scene i649
                    with dissolve
                    mc "Come here..."
                    mc "You've been working hard. You deserve a moment of peace."
                    s "I know... And thank you for bringing me here."
                    mc "Anytime, Sky."
                    mc "Now rest."
            $ renpy.end_replay()
            stop music fadeout 2
        scene black
        with dissolve
        with fadeq

        "You spend time relaxing with Sky until the afternoon and go straight back home..."

        scene black
        with dissolve
        with fadeq

        "Later at dinner time..."

        scene black
        with dissolve
        with fadeq

        scene i651
        with dissolve
        yt "Haha! She went straight to bed."
        yt "It's almost time for dinner, but I think I should let her rest some more. She deserves it."
        yt "I'll go prepare dinner. I'll just wake her up when it's ready."
        stop music fadeout 2

        scene black
        with dissolve
        with fade
    else:
        stop music fadeout 2

        scene black
        with dissolve
        with fadeq

        "The day passed by without anything noteworthy..."

        scene black
        with dissolve
        with fadeq

        "The next day at dinner time..."

        scene black
        with dissolve
        with fadeq

    play music 'audio/Meander.mp3'
    scene i652
    with dissolve
    a "Ah... [mc]."
    mc "Hey there, Aine."
    a "Where are you going? Are you heading out?"
    mc "Uh, no... I'm actually heading to the kitchen to prepare dinner."
    a "Oh, you don't have to! Emma is taking care of it right now."
    mc "Wait... What? Emma? Cooking?"
    a "Why are you so shocked?"
    a "Of course, Emma can cook!"
    yt "Well? What can I say? She just blew my mind right now!"
    yt "I should still check on her. I still don't trust her at all."
    mc "Alright. I'll go downstairs to check on her. I'll call you guys later when dinner is ready."
    a "Oh, sure! Thanks, [mc]!"

    scene black
    with dissolve
    with fade

    scene i653
    with dissolve
    $ renpy.pause()
    scene i654
    with dissolve
    yt "Holy... Jesus and Mary...!"
    yt "Why the hell is she wearing a maid outfit?!"
    scene i655
    with dissolve
    mc "Hey, Emma."
    show i656
    with dissolve
    e "Hmn?"
    scene i657
    with hpunch
    e "!!!!!!"
    stop music fadeout 2
    scene ep2e
    with dissolve
    $ renpy.pause()
    scene ep3
    with dissolve
    $ renpy.pause()

    scene black
    with dissolve
    with fade

    play music 'audio/Fear.mp3'
    scene i658
    with dissolve
    h "Finally done hiding, huh?"
    k "Hmp... you really know where to find me."
    h "Have you forgot who I am?"
    k "Not that I care about you, anyway."
    h "*chuckles* Welcome back, then..."
    h "...Jovian's wife."

    jump ep3

label ch1ep3:
    scene ch1ep2e
    with dissolve
    pause
    scene ch1ep3s
    with dissolve
    pause
    show screen day_monday with dissolve
    play music 'audio/EveryoneRainfalls.mp3'
    scene ch1ep3_1
    with dissolve
    f "{i}Ah, yeah..."
    f "{i}It's always been like this, no matter where I go..."
    f "{i}No matter where I am..."
    scene ch1ep3_2
    with Dissolve(1.0)
    f "{i}I was born into a world that already had its shining sun..."
    f "{i}Aine is the sun, loved by everyone who gazes upon her..."
    f "{i}And me?"
    play sound lightsoff
    show ch1ep3_3
    f "{i}I'm the shadow. I exist, yet I'm overlooked, invisible."
    scene ch1ep3_4
    with dissolve
    f "{i}Every smile, every praise, it's always for her... always about her..."
    f "{i}Always has been... always will be..."
    f "{i}And the worst part?"
    f "{i}I can't help but adore her too..."
    f "{i}She's my sister, after all. I understand that she's been through a lot..."
    f "{i}But at the same time, I can't help but envy her."
    f "{i}Because she has... everything I've ever wanted..."
    play sound cityalley loop
    show ch1ep3_5
    mc "Hey, Frey! You ready?"
    show ch1ep3_6
    f "!!!"
    scene ch1ep3_7
    with dissolve
    f "{i}Ah, fuck...!"
    f "{i}I'm aware..."
    f "{i}I'm fully aware..."
    f "{i}I'm aware that when I think this way, I've already lost..."
    play sound2 slap
    show ch1ep3_8
    with hpunch
    f "Hrrmn~!!"
    scene ch1ep3_9
    with dissolve
    f "Hooo..."
    f "{i}On your feet, Freya. Get it together."
    scene ch1ep3_10
    with dissolve
    mc "Uhh... you good?"
    f "Yeah! I just needed to wake myself up. I had an extremely long night."
    mc "Well, whatever that was, you know you can always talk to me-{w=2.0}{nw}"
    show ch1ep3_11
    f "It was nothing! Let's go, let's go!"
    yt "... This again."
    stop music fadeout 4
    scene ch1ep3_12
    with dissolve
    mc "By the way, did Jess call you too?"
    f "Me? No, why?"
    scene ch1ep3_13
    with dissolve
    mc "Well..."
    f "Blah, blah, blah... I'm going to transfer you three. Here's the address."
    scene ch1ep3_14
    with dissolve
    f "..."
    play sound2 woosh
    show ch1ep3_15
    with hpunch
    f "{i}Excuse{/i} me?! Care to elaborate?!"
    mc "She was in a rush and didn't give me further details, so I have no idea."
    mc "Only one way to find out, I guess..."
    stop sound fadeout 2

    scene black
    with dissolve
    with fade

    play sound traffic loop
    scene ch1ep3_16
    with dissolve
    mc "..."
    yt "Ugh... I hate this awkward silence between us."
    yt "It started after our beach island vacation and has become more frequent ever since."
    yt "I know she's struggling emotionally when she gets like this."
    yt "I've tried to coerce it out of her several times, but she always has found clever ways to dodge the subject."
    scene ch1ep3_17
    with dissolve
    f "..."
    stop sound fadeout 2
    play music 'audio/DontWakEmUp.mp3'
    scene ch1ep3_18
    with flash
    f "Thankie~! I'll return it in one piece, I promise!"
    k "Noooo~! Cecilia~!!!"
    scene ch1ep3_19
    with dissolve
    mc "Cecilia? You named your skateboard Cecilia?"
    mc "Heck, I'm surprised it still exists..."
    play sound skateboardland
    scene ch1ep3_20
    f "Wohoooooo~!"
    mc "Hey, Frey, slow down!"
    k "Not my Cecilia..."
    scene black
    with dissolve
    pause 0.5
    play sound smallbell
    show ch1ep3_21
    f "Ahhhh~!!" 
    mc "What did I tell you?"
    stop music fadeout 4
    play music2 'audio/HoldMeCloser.mp3' fadein 4 loop
    scene ch1ep3_22
    with dissolve
    f "I just wanted to-{w=0.5}{nw}"
    show ch1ep3_23
    mc "Play, I know. But that doesn't mean getting yourself hurt in the process is okay."
    f "Are you becoming my mother?"
    mc "Well, if there's nobody to look after you, then what will you do next time something like this happens?"
    scene ch1ep3_24
    with dissolve
    f "..."
    scene ch1ep3_25
    with dissolve
    f "{size=-10}Sorry..."
    mc "I can't hear you."
    scene ch1ep3_26
    with dissolve
    f "I'm sorry..."
    show ch1ep3_27
    mc "Good!"
    scene ch1ep3_28
    with dissolve
    pause
    scene ch1ep3_29
    with dissolve
    mc "Can you stand? Don't force yourself if you can't. Lily and I can take care of today's shift if you need."
    f "I think I can manage."
    mc "Let's go, then. We're almost late."
    scene ch1ep3_30
    with dissolve
    f "Hey, [mc]."
    mc "Hm?"
    f "Is it hard to notice me?"
    f "Just tell me \"yes\" or \"no\", and why."
    menu:
        "Yes{#ch1ep3}":
            $ freyaroute = False
            scene ch1ep3_31
            with dissolve
            mc "Well, I don't exactly know what you mean by that."
            mc "But if you're asking if it's hard for me to notice you as a woman, then..."
            mc "Kind of...?"
            mc "I mean you-{w=0.5}{nw}"
            show ch1ep3_32
            f "That's all I wanted to know."
            mc "Wait, what about the \"why\"?"
            f "It's fine. You can keep it."
            mc "Huh?"
        "No{#ch1ep3}":
            $ freyaroute = True
            scene ch1ep3_31
            with dissolve
            mc "Well, I don't exactly know what you mean by that."
            mc "But if you're asking if it's hard for me to notice you as a woman, then no."
            mc "Do you want to know what I like most about you?"
            scene ch1ep3_33
            with dissolve
            f "What?"
            play sound cloth
            scene ch1ep3_34
            with dissolve
            mc "The fact that you don't need a hero in your life."
            scene ch1ep3_35
            with dissolve
            mc "I'm quite jealous of that about you, and I'm certain I'm not the only one."
            f "Huh?"
    
    stop music2 fadeout 4
    play sound traffic loop
    scene ch1ep3_36
    with flash
    f "..."
    scene ch1ep3_37
    with dissolve
    f "...."
    play sound2 fistbump
    show ch1ep3_38
    with hpunch
    f "Oof!"
    scene ch1ep3_39
    with dissolve
    f "Hey, what..."
    scene ch1ep3_40
    with dissolve
    f "Hm?"
    play sound2 fingersnap
    play music 'audio/ErrorsExpected.mp3'
    show ch1ep3_41
    pause 0.2
    show ch1ep3_42
    pause 0.5
    show ch1ep3_43
    pause 0.5
    show ch1ep3_44
    pause 0.8
    scene ch1ep3_45
    with dissolve
    shu "Well, hello there my slaves!"
    shu "Time to bow down to your master as you feast your eyes upon the pinnacle of modern gastronomy!"
    scene ch1ep3_46
    with dissolve
    shu "Welcome to Shu's \"Best Burger\"!"
    scene ch1ep3_47
    with Dissolve(1.0)
    shu "Behold the palace where the humble burger ascends to divine gourmet, where every bite transports you to a paradise of taste!"
    shu "Who else could transform the simple burger into a symphony of flavor but I, the great maestro of the kitchen?"
    shu "My culinary wizardry will stun your senses, leaving you begging for more!"
    scene ch1ep3_48
    with dissolve
    shu "But let's not forget the real secret sauce of this establishment - the indomitable, irresistible charm of yours truly, the master and commander of this gourmet vessel."
    shu "Yes, my friends, the heart and soul of this culinary wonderland is none other than..."
    play sound2 introslam
    show ch1ep3_49
    shu "Me!"
    stop music
    show ch1ep3_50
    mc "You don't even know how to cook for yourself."
    show ch1ep3_51
    shu "Ah."
    scene ch1ep3_52
    with dissolve
    f "\"Best Burger\"? That's lame. Who named this?"
    play sound2 bonebreak
    show ch1ep3_53
    shu "*audible heartbreak*"
    play sound smallbell
    play music 'audio/ErrorsExpected.mp3'
    show ch1ep3_54
    pause
    mc "So this is what you meant by transferring us?"
    j "Yes. It's a partnership between me, Klara, and Shu."
    scene ch1ep3_55
    with dissolve
    j "He couldn't wait for the rest of the preparations. So, I decided to have you three work here instead."
    scene ch1ep3_56
    with dissolve
    l "Uhm..."
    j "You don't need to raise your hand, Lily."
    l "Sorry, but to my knowledge of business best practices, shouldn't we have done a pre-opening instead of an official opening right away?"
    mc "Exactly what I was thinking."
    j "I'm confident in your skills, so in my opinion, we don't need one."
    j "However, business is still business, so today will be our pre-opening."
    j "I've only invited a certain number of customers who will come here under reservations."
    j "I will task your manager to report to me by the end of the day."
    scene ch1ep3_57
    with dissolve
    f "Huh? Who's the manager?"
    j "*chuckles* Who else?"
    scene ch1ep3_58
    with dissolve
    l "Oh, jeez... Congrats, [mc]!"
    mc "*sighs* I don't know if I should feel happy since this was such short notice."
    f "You wanted this, right?"
    mc "... To be honest, I don't know anymore."
    mc "Too much has happened for me to comprehend how I feel right now."
    scene ch1ep3_59
    with dissolve
    j "You got this, [mc]."
    mc "Adapt and conquer, right?"
    j "Adapt and conquer."
    j "Take care of this business. It will serve you well in the long run."
    j "Places like this can be something you can always return to."
    scene ch1ep3_60
    with dissolve
    yt "..."
    scene ch1ep3_61
    with dissolve
    mc "Got it."
    scene ch1ep3_62
    with dissolve
    j "And Freya?"
    f "Yeah?"
    j "I'd like you to remove that hair extension of yours while on duty."
    j "I prefer your usual hair style. It makes you presentable."
    scene ch1ep3_63
    with dissolve
    f "Ah, right. I've been using them in my stream lately... I got carried away."
    scene ch1ep3_64
    with dissolve
    j "Alright, then. Shall we begin?"
    stop music fadeout 2

    if freyaroute:
        scene black
        with dissolve
        with fade
        label freyasucknosuck:
        if _in_replay:
            $ name = persistent.gallery_name
        $ renpy.sound.set_volume(0.3, 1.0)
        play sound traffic loop
        scene ch1ep3_65
        with dissolve
        f "Urrh... Still not done...? It's almost 6 pm..."
        mc "I'm double-checking the inventory. I can't mess this up."
        mc "You can change up and go home first, you know?"
        play sound2 woosh
        show ch1ep3_66
        f "Hey, you said you'd look after me! We're going home together!"
        mc "Right..."
        scene ch1ep3_67
        with dissolve
        f "..."
        scene ch1ep3_68
        with dissolve
        f "Ugh... It's infuriating how you can ignore everything when you get too focused on something."
        f "The worst part is you do this to everybody nowadays..."
        scene ch1ep3_69
        with dissolve
        mc "..."
        f "..."
        scene ch1ep3_70
        with dissolve
        f "You know, nobody will notice if you pocket some \"tip money\" for yourself?"
        mc "As your manager, I'll do you a favor and pretend I didn't hear that."
        scene ch1ep3_71
        with dissolve
        f "{i}Ugh! What a killjoy!"
        mc "..."
        f "..."
        play sound2 woosh
        show ch1ep3_72
        f "OH SHIT! SOMETHING'S BURNING!"
        mc "Huh?! Where?!"
        play sound2 cloth
        stop sound fadeout 2
        $ renpy.sound.set_volume(1.0, 1.0)
        scene ch1ep3_73
        with dissolve
        play music 'audio/RealClass.mp3'
        f "Ah, sorry, it's just me. I feel {i}so{/i} goddamn hot right now."
        mc "What are you-{w=0.5}{nw}"
        play sound closedoor2
        scene ch1ep3_74
        with dissolve
        pause 0.8
        play sound thud3
        show ch1ep3_75
        with hpunch
        f "*gasps*"
        yt "What the-{w=0.5}{nw}"
        scene ch1ep3_76
        with dissolve
        mc "*whispers* Hey, what are you doing?!"
        f "*whispers* I-I don't know! I panicked, okay?!"
        mc "*whispers* Just pretend you were grabbing something and get up before..."
        f "*whispers* Before...?"
        scene ch1ep3_77
        with dissolve
        mc "H-hello! Welcome to Best Burger!"
        f "{i}Well, shit... Too late now, I guess."
        scene ch1ep3_78
        with dissolve
        cu "Hi, can I get two Super burgers..."
        mc "Actually we-{w=0.5}{nw}"
        cu "A medium fry, four Ultra burger meals..."
        mc "Excuse me, ma'am-{w=0.5}{nw}"
        cu "A large milkshake, four colas..."
        scene ch1ep3_79
        with dissolve
        f "{i}Damn, is she still going? I wonder what this girl looks like..."
        mc "If I could just-{w=0.5}{nw}"
        f "{i}She has to be ordering for a group, right? No way she's eating all that herself... right...?"
        cu "Hmm... three kid's meals, and another Super burger..."
        f "{i}Well, we're closed anyways, so it doesn't matter. Tough luck, lady."
        mc "Ma'am, please-{w=0.5}{nw}"
        cu "Two hot dogs, and actually, not a medium fry. Make that a large fry..."
        scene ch1ep3_80
        with dissolve
        f "{i}Ugh, can she shut up already so we can all go home? It's getting boring down here."
        scene ch1ep3_81
        with dissolve
        pause
        scene ch1ep3_82
        with dissolve
        f "{i}Actually, maybe we can make things more stimulating..."
        scene ch1ep3_83
        with dissolve
        cu "On second thought, can you add two more milkshakes to the order? One large, one small."
        mc "MA'AM! WE ARE C-{w=0.5}{nw}"
        play sound cloth
        scene ch1ep3_84
        with Dissolve(1.0)
        pause 0.5
        mc "WHAT. THE. FUUUU...?"
        show ch1ep3_85
        cu "What was that? By the way, are you writing this down?"
        cu "I don't want to repeat myself, so you better be getting all of this."
        scene ch1ep3_86
        with dissolve
        mc "*whispers* Frey, what the hell are you doing?!"
        scene ch1ep3_87
        with dissolve
        f "*whispers* Shhh... Shouldn't you be focused on the customer right now?"
        f "*whispers* Let me have some fun with the other {i}member{/i} of our team."
        yt "Dammit... this is totally inappropriate, especially at work."
        yt "If Jess finds out about this, getting fired will be the least of my problems..."
        yt "I don't want to know what she's like in protective aunt mode..."
        yt "But at the same time... this is kinda hot."
        yt "Freya jacking me off while this lady has no clue what's happening right in front of her..."
        yt "Should I let her keep going?"
        menu:
            "Stop her":
                $ freyaroute = False
                yt "No, that's way too much."
                stop music fadeout 2
                scene ch1ep3_88
                with dissolve
                "You discreetly but firmly push Freya's hand away."
                mc "*whispers* Not here, Freya."
                f "*whispers* Huh...?"
                scene ch1ep3_89
                with dissolve
                mc "I'm sorry, ma'am, but we closed about an hour ago."
                cu "What do you mean, you're closed?"
                mc "Closed, as in {b}closed{/b}. All the kitchen equipment is stored away and won't be operating again until tomorrow morning."
                mc "I apologize for the inconvenience, but you are welcome to return here at 8 am tomorrow once we reopen."
                scene ch1ep3_90
                with dissolve
                "The customer walks away, muttering under her breath."
                cu "What kind of useless restaurant closes right at dinner time..."
                "With that taken care of, you turn your attention to Freya."
                scene ch1ep3_91
                with dissolve
                mc "She's gone. You can come out now."
                "You offer a hand to help her, but Freya gets up on her own."
                scene ch1ep3_92
                with dissolve
                f "I'm sorry, [mc]. I shouldn't have."
                mc "It's fine, I-{w=0.5}{nw}"
                scene ch1ep3_93
                with dissolve
                f "Is it really?"
                "Her expression tells you it clearly isn't fine for her."
                f "... I think we should stop before things go too far."
                mc "What do you mean?"
                scene ch1ep3_94
                with dissolve
                f "From now on, please keep your distance from me, [mc]."
                f "Being around you always makes me want to do crazy stuff, but it's getting out of control."
                f "I mean, you're my sister's fiancé."
                if aineroute == False:
                    f "Even if you're just engaged for show, this still isn't right."
                f "What if anyone found out about what I tried to do just now?"
                mc "Frey, wait-{w=0.5}{nw}"
                f "No, it's best if you stay away. It's not worth the risk."
                f "... I'm not worth the risk..."
                #Freya starts walking towards the door
                mc "Frey, can we-{w=0.5}{nw}"
                f "Please, don't. Let's stay coworkers and let it be."
                f "I think... I'll be able to breathe better this way."
                yt "What the hell did I just do?!"
            "Let her keep going":
                $ freyaroute = True
                yt "Ah, well. Fortune favors the bold... or something like that."
                scene ch1ep3_95
                with dissolve
                "Still keeping your eye on the customer, you give Freya a thumbs up to tell her to keep going."
                f "{i}That's what I thought."
                show freya4
                with dissolve
                pause
                "Freya begins by stroking up and down your dick."
                "Her small fingers are barely able to wrap around your girth, but her soft palm massages pleasure along your entire length, the softness of the skin contrasting the firmness of your cock."
                yt "Shit! She's really good at this..."
                cu "Did you hear what I just said?"
                mc "I'm s... sorry, could you repeat that?"
                cu "Ugh, sure. Just the last part or the whole order?"
                mc "Uhh... th... thuhhh..."
                "Encouraged by your inability to speak like a normal human, Freya begins moving her hand faster."
                yt "Fuck! I almost forgot how skilled her hands were."
                yt "I guess all that gaming is good for one thing, at least."
                hide freya4
                show ch1ep3_96
                with dissolve
                "You sneak a glance down at her."
                "She gives you a knowing smirk, gesturing you to turn your attention back to the customer."
                f "*whispers* Well? She's waiting..."
                scene ch1ep3_97
                with dissolve
                cu "Um, are you feeling okay?"
                mc "Nhhh... never better. Sorry, it's just been a lo-ooohh-ng day."
                cu "I see. Anyways, like I was saying..."
                play sound cloth
                scene ch1ep3_98
                with dissolve
                "You're forced to turn your attention away from the customer again due to a new sensation emanating from your nether region."
                show freya5
                with dissolve
                "You quickly glance down again, seeing that Freya has now started to massage your butt while continuing to rub your cock."
                "Somehow, she also has managed to remove her shirt with just one hand."
                "Those gamer girls are built differently, that's for sure."
                f "*whispers* Sorry, boss. I hope you don't mind the dress code violation."
                f "*whispers* I just didn't want to ruin my uniform with any unexpected spills."
                f "*whispers* Maybe not exactly unexpected, heh..."
                cu "Hey! Hello? I'm still talking to you!"
                "You snap back to reality thanks to the customer's annoyed shouts."
                yt "Ugh, fuck off, Karen. I'm a little preoccupied at the moment."
                mc "My sincere apologies, ma'am. However, I... uhhhh..."
                "Freya's hands just won't let up. You can feel the pleasure building, amplified by the fact that you could be caught at any moment."
                cu "You what? Spit it out already!"
                hide freya5
                show ch1ep3_97
                with dissolve
                mc "I regret to inform you that we're cl-{w=0.8}{nw}"
                show ch1ep3_99
                with hpunch
                "You pause suddenly, caught off-guard as Freya tries to take your entire cock into her mouth."
                f "Ack! *cough* *cough*"
                "Freya quickly discovers that she was overzealous, as she starts choking on you almost as quickly as she tried to swallow you whole."
                scene ch1ep3_100
                with dissolve
                mc "Um... ma'am, I'll have to ask you to {i}slow down{/i}, please."
                cu "Slow down? Slow down what? My words?"
                mc "Sure. We wouldn't want you to choke by going too fast, would we?"
                cu "If you say so... {size=-10}weirdo..."
                show freya6
                with dissolve
                "Despite having your cock in her mouth, you can feel Freya give an amused smile."
                "She got your message. Freya slows her movements down, letting her mouth adjust to your length before taking in more."
                hide freya6
                show ch1ep3_101
                with dissolve
                cu "Also, was that coughing just now? Is someone else here?"
                mc "No!"
                mc "I mean, no, that was probably just the building settling a little. Everything is new construction."
                cu "I see. Anyways, I'll take three Super burgers..."
                show freya6
                with dissolve
                "Having adjusted to your size rather quickly, Freya begins moving her head back and forth."
                "Her small mouth stretches to its limit to accommodate your manhood. It probably isn't comfortable, but her face shows no indications of unease."
                "Her lips hug your dick with just the right amount of pressure as she glides along its length."
                mc "Ghhh..."
                hide freya6
                show ch1ep3_102
                with dissolve
                "Freya speeds up, simultaneously sneaking one hand under her panties to pleasure herself."
                show freya7
                with dissolve
                cu "Are you still listening?"
                mc "Yhh... yes... keep... going..."
                cu "Okay, so I also asked for..."
                "Even though she is only able to take half of your dick into her mouth, her speed is just right to send shivers down your entire lower half."
                "Combined with the feeling of your dick hitting the back of her throat with every motion, you feel the pleasing sensations building higher, reaching close to your peak."
                mc "Actu... actually, ma'am, I need-{w=0.7}{nw}"
                "Suddenly, Freya speeds up."
                mc "To-hooohh!!! ... To tell you something..."
                cu "Hmph. What? I wasn't finished yet."
                "And neither are you, but Freya is doing everything she can to change that."
                "She was already making it hard to talk, but now Freya's fast pace is making it nearly impossible to get any words out."
                mc "We ahhh... I am... we are..."
                "Freya shows no signs of letting up. In fact, you can actually feel her moans, suppressed only by the footlong (give or take a few) gag in her mouth."
                f "Nghhh... hmmm..."
                yt "Fuck... I'm about to bust any second now."
                yt "I better find a way to warn her. And fast."
                mc "CLOSE!!! I mean, we're closed."
                "It's taking all your willpower just to ignore the throbbing in your dick while trying to keep a straight face in front of the customer."
                "The fact that you can still speak in sentences is nothing short of a miracle."
                hide freya7
                show ch1ep3_103
                cu "You're {i}what{/i}?"
                mc "We're {i}closed{/i}. Pl... please {i}come{/i} back {i}soon{/i}."
                cu "What do you mean, you're closed?"
                show freya7
                with dissolve
                mc "I-I mean, thank you... for {i}coming{/i}! But we stopped... serving food an hooooour ago..."
                mc "{i}So close{/i}, yet so far..."
                "You hope Freya got the message because, by now, you've exhausted almost all your resistance."
                "Any second now, Freya will have a surprise order of cream in her mouth unless she pulls back."
                cu "Closed?! You serious?!"
                mc "M... mhm."
                cu "What kind of useless restaurant closes at dinnertime?!"
                cu "Which dumbass decided that?"
                hide freya7
                play sound woodhit
                show ch1ep3_104
                with hpunch
                shu "Hnng!"
                shu "I sense a disturbance in the force... Someone insulted my magnificence..."
                scene ch1ep3_105
                with dissolve
                mc "Apologies for the inconvenience!"
                cu "Yeah, yeah. Whatever."
                show freya7
                with dissolve
                mc "Have a... NICE DAY!!!"
                "As soon as the door closes, the gates desperately holding back your pleasure swing wide open."
                play sound woodhit
                show ch1ep3_106
                with hpunch
                f "Mmmh!!"
                "Bracing yourself against the counter, you pump wave after wave of hot cum down Freya's throat, filling her entire mouth."
                "Her eyes go wide in shock but flutter closed again as she succumbs to her own pleasure."
                play sound thud3
                show ch1ep3_107
                with hpunch
                f "Ghhiiiihhh!!!"
                "Freya involuntarily releases her hold on your dick, squealing as her entire body contracts in orgasm."
                "The cum that was in her mouth spills out onto her cheeks and the floor, forming a small pool beside her face as she lays breathless on the tiles."
                yt "Holy shit... that was {i}so{/i} hot..."
                scene ch1ep3_108
                with dissolve
                "You give your coworker a few seconds to regain her composure before you break the silence."
                mc "... Yeah, you're cleaning that up."
                scene ch1ep3_109
                with dissolve
                f "Hahhh... jerk..."
                mc "You caused it; you clean it. It's only fair, Frey."
                f "Fine... just... a minute... still... catching breath..."
                mc "Take your time. I still have to finish counting."
                scene ch1ep3_110
                with dissolve
                f "You know... we..."
                mc "We what?"
                f "You don't have to go back to that right away..."
                mc "If we want to get out of here anytime soon, I should."
                f "No, I mean... we could... um..."
                f "..."
                mc "Since when did you get so bashful?"
                scene ch1ep3_111
                with dissolve
                f "Shut up!"
                mc "You were saying?"
                scene ch1ep3_112
                with dissolve
                f "Instead of going back to inventory, we could... you know..."
                f "Do it... maybe?"
                mc "Do... it...?"
                f "Yeah..."
                mc "What do you... oh. {i}OH.{/i}"
                mc "Well, I-{w=0.5}{nw}"
                stop music
                play sound phonevibrate loop
                show ch1ep3_113
                mc "Sorry, hold on."
                scene ch1ep3_114
                with dissolve
                yt "Aine?"
                scene ch1ep3_115
                with dissolve
                mc "Ah shoot, I have to take this. One second."
                f "... Sure."
                f "... {size=-10}Of all times, of course that would happen now..."
                play sound phoneclick
                scene ch1ep3_116
                with dissolve
                mc "Greetings, dear fiancée! How may I be of service to your elegance today?"
                a "Um... hello, [mc]...?"
                mc "Sorry, you caught me in a good mood. What's up?"
                a "Could you please bring back some leftover food for Sky and me?"
                a "We won't have time for dinner with everyone else since we're teaching an evening class."
                mc "Sure, I think we have a few burgers left over from today."
                a "Thank you! You're the best."
                mc "Anything for m'lady. Is there anything else you wanted to talk about?"
                a "No, that was all. How is Freya?"
                scene ch1ep3_117
                with dissolve
                mc "Well... we had more fun than usual at work today."
                a "Really? I'm happy to hear that!"
                mc "Heh... yeah..."
                mc "Anyways, we're almost ready to close up and go home. I'll have the burgers ready for you then."
                a "Okay, thanks again! Take care and get home safe!"
                mc "Bye, Aine."
                play sound phoneclick
                scene ch1ep3_118
                with dissolve
                mc "Sorry about that, Frey. It was your sister ca..."
                mc "... Freya?"
                scene ch1ep3_119
                with dissolve
                mc "... Hey? Frey?"
                scene ch1ep3_120
                with dissolve
                f "I'm ready. Let's go!"
                mc "But what about-{w=0.5}{nw}"
                f "Come on, hurry up, [mc]! I have a stream tonight, and I need to get ready!"
                mc "But-{w=0.5}{nw}"
                scene ch1ep3_121
                with dissolve
                f "I know you're the manager and all, but do you really want to stay here all night?"
                mc "Okay... just let me grab a few burgers for-{w=1.0}{nw}"
                play sound closedoor2
                scene ch1ep3_122
                with dissolve
                yt "Aaaaaaand she's gone."
                yt "Welp, better hurry up so I'm not left behind, I guess..."
        $ renpy.end_replay()

        scene black
        with dissolve
        with fade

        play sound dawnambient loop
        play music 'audio/HoldMeCloserINST.mp3'
        scene ch1ep3_123
        with dissolve
        f "..."
        yt "Ah, here we go again."
        scene ch1ep3_124
        with dissolve
        mc "Hey, what's wrong?"
        f "... Nothing."
        mc "Come on, Frey, let's talk. I know something's bothering you..."
        f "There's nothing to talk about. I'm fine."
        scene ch1ep3_125
        with dissolve
        mc "..."
        yt "I should try asking the usual questions."
        mc "Well then... How's your streaming going?"
        f "Fine."
        mc "... How's the business with Shu?"
        f "It's okay."
        yt "Those aren't the answers you usually give, Freya."
        yt "There's definitely something bugging you that you're not telling me."
        mc "I see..."
        scene ch1ep3_126
        with dissolve
        pause
        scene ch1ep3_127
        with dissolve
        mc "I'll see you tomorrow?"
        f "Sure."
        play sound2 closedoor
        scene ch1ep3_128
        with dissolve
        yt "Tsk!"
        yt "Patience, [mc], patience! Now's not the time to start a fight!"
        stop sound fadeout 2
        scene black
        with dissolve
        pause 0.5
        play sound2 closedoor
        scene ch1ep3_129
        with dissolve
        a "Hey, [mc]! Do you have the-{w=0.8}{nw}"
        scene ch1ep3_130
        with dissolve
        a "Hm?"
        mc "..."
        image aimctabfafedor:
            "ch1ep3_131.jpg"
            pause 3.0
            "ch1ep3_132.jpg"
            pause .2
            repeat
        show aimctabfafedor
        with dissolve
        a "What's the matter? Did something bad occur just now?"
        mc "... Has Freya said anything unusual to you lately?"
        a "Uhm... Nothing notable, really. She seems like her usual self to me."
        a "You mentioned you guys were having fun too. What happened?"
        mc "That's the thing: one minute, she was just her usual self. Then, all of a sudden, she's brushing off everything I say."
        mc "Something is bothering her, Aine. And I don't know what it is."
        mc "I've tried to talk to her, but she keeps dodging the conversation."
        mc "Or well, more like she just doesn't answer me at all."
        mc "If only I could read minds..."
        scene ch1ep3_133
        with dissolve
        a "..."
        scene ch1ep3_134
        with dissolve
        a "I'll talk to her, don't worry."
        mc "Yeah, please do."
        scene ch1ep3_135
        with dissolve
        mc "Oh, and here are your burgers."
        mc "Tell Sky I put extra cheese on hers."
        scene ch1ep3_136
        with dissolve
        a "Thanks!"
        mc "Are you two sure you don't want to have dinner?"
        scene ch1ep3_137
        with dissolve
        a "Our schedules are pretty hectic as it's almost time for our students' final exams, so we'll skip dinner tonight."
        a "We promise we'll make it up next time."
        scene ch1ep3_138
        with dissolve
        mc "*chuckles* Just don't make it a habit."
        scene black
        with dissolve
        pause 0.5
        play sound closedoor
        scene ch1ep3_139
        with dissolve
        pause
        play sound cloth
        scene ch1ep3_140
        with dissolve
        pause
        play sound chair
        show ch1ep3_141
        with hpunch
        pause
        f "{i}... I hate this."
        f "{i}Ignoring him and being unable to say anything."
        f "{i}I know I'm hurting him, and that pains me more than anything."
        scene ch1ep3_142
        with dissolve
        f "..."
        f "{i}Tch!" 
        f "{i}Get up. Stand up."
        f "{i}Don't lose to your thoughts now, Freya."
        play sound chair
        scene ch1ep3_143
        with dissolve
        pause
        scene ch1ep3_144
        with dissolve
        f "{i}Yeah, that's right. Time for your grand escape from reality..."
        f "{i}One more time..."
        f "{i}Just like always..."
        scene ch1ep3_145
        with dissolve
        f "Oh, that's right. I wonder what I should wear for today's stream?"
        f "Hmm..."
        f "..."
        scene ch1ep3_146
        with dissolve
        f "Ah, maybe that one~!"
        f "Big bucks, here I come!"
        f "Or rather, you'll come to me!"
    stop music fadeout 2

    scene black
    with dissolve
    with fade

    scene ch1ep3_147
    with dissolve
    pause
    play sound step
    show ch1ep3_148
    with hpunch
    pause
    scene ch1ep3_149
    with dissolve
    j "Hm?"
    scene ch1ep3_150
    with dissolve
    j "Oh..."
    j "I completely forgot about that."
    j "I hope it's not too late..."
    play sound dialtone loop
    scene ch1ep3_151
    with dissolve
    "..."
    "...."
    "....."
    stop sound fadeout 2
    scene ch1ep3_152
    with dissolve
    pause
    play sound2 phonevibrate loop
    scene ch1ep3_153
    with dissolve
    pause
    play sound2 phoneclick
    scene ch1ep3_154
    with dissolve
    mc "Jess?"
    j "Are you busy?"
    mc "Actually... I was just about to send you the report."
    j "Good! Send it. Then, come meet me at Soja Spot as soon as possible."
    scene ch1ep3_155
    with dissolve
    mc "Soja Spot? I've never heard of it."
    j "Ouch...?"
    mc "Huh? Why?"
    j "It's one of my team's businesses, you know?"
    mc "Oh... Sorry."
    j "Enough talk. Get moving."
    mc "Roger."

    scene black
    with dissolve
    with fade

    play sound coffeeshopambience fadein 2 loop
    play music 'audio/NightCharms.mp3'
    scene ch1ep3_156
    with dissolve
    yt "Soja Spot..."
    yt "So, it's a coffee shop. Seems like it's doing well."
    yt "I was being honest, though. I've never heard of this place before."
    yt "Looks like a good place where I could chill."
    scene ch1ep3_157
    with dissolve
    mc "..."
    yt "Isn't that... that crazy woman...?"
    scene ch1ep3_158
    with dissolve
    mc "Hey, it's been a while!"
    cl "It has. I'm glad to see you're still in one piece."
    yt "In one piece?"
    mc "L-likewise?"
    cl "Jess is waiting for you upstairs."
    yt "Of course, she's already here. I hope I haven't kept her waiting for too long."
    scene black
    with dissolve
    scene ch1ep3_159
    with dissolve
    j "[mc]."
    scene ch1ep3_160
    with dissolve
    yt "Aw, that's cute. It's the first time I've seen her wear something like that."
    scene ch1ep3_161
    with dissolve
    mc "What's the occasion?"
    j "You mean this?"
    j "I like to show off a new look once in a while."
    mc "I see."
    scene ch1ep3_162
    with dissolve
    j "Take a seat."
    play sound2 platedown
    scene ch1ep3_163
    with dissolve
    cl "Here."
    mc "Thanks."
    play sound2 cloth
    scene ch1ep3_164
    with dissolve
    mc "Did you get my report?"
    j "Yes. It's detailed yet impressively concise, as per your usual standards."
    mc "I'm glad to hear that."
    mc "So, why here?"
    mc "You're always welcome at our place, you know."
    j "I prefer to keep myself away from there as much as possible."
    scene ch1ep3_165
    with dissolve
    mc "Why is that?"
    j "Ah, that village is..."
    j "Well, it holds certain memories."
    mc "Nothing bad, I hope?"
    scene ch1ep3_166
    with dissolve
    j "The opposite, in fact. Those memories only belong to that place and that place alone."
    mc "Nostalgia, huh? How nice."
    j "*chuckles* Let's get down to business, shall we?"
    mc "Right. The reason why you made me come all the way to... Soja Spot."
    scene ch1ep3_167
    with dissolve
    j "Here."
    scene ch1ep3_168
    with dissolve
    mc "What's this?"
    j "Nothing that pertains to you, but it's still something you should be mindful about."
    j "Inside that box are clothes that Hera bought for Freya."
    j "I wanted to ask Aine, but considering her circumstances, I can't put her in that position. So this task fell on you."
    scene ch1ep3_169
    with dissolve
    mc "Christmas wrapping, sure..."
    j "Is that weird?"
    mc "Well..."
    mc "You could've just called Freya, you know?"
    j "As much as I'd like to, I want this to come from someone special to her."
    mc "But you're her aunt."
    scene ch1ep3_170
    with dissolve
    j "Just her aunt. Besides our familial ties, we don't share a powerful bond."
    j "If it comes from you, this gift might have a different effect on her."
    mc "That's your reason?"
    j "One of two reasons."
    j "The other is that I don't like giving gifts personally."
    scene ch1ep3_171
    with dissolve
    mc "And I find that odd about you, by the way. It's the one thing that doesn't align with who you are."
    scene ch1ep3_172
    with dissolve
    j "Yeah, yeah, whatever..."
    mc "See what I mean?"
    scene ch1ep3_173
    with dissolve
    j "Anyway, what happened to Freya? Something's off about her today."
    mc "Changing the subject now, are we?"
    scene ch1ep3_174
    with dissolve
    j "*sighs*"
    scene ch1ep3_173
    with dissolve
    mc "Well... that's what I'm trying to figure out."
    mc "Actually, it's more like I've been trying to figure that out since... our beach island vacation."
    mc "She didn't tell me anything, so I'm kind of in the dark here."
    j "It was the right decision to call you about this box, then. Use it to your advantage."
    mc "Hm, might as well."
    j "If you want a piece of genuine advice, just throw her a curveball question. Force her to answer from the heart."
    mc "Force her to answer from the heart?"
    mc "What makes you certain that will make her confess her problems to me?"
    scene ch1ep3_175
    with dissolve
    j "Because it worked on me before?"
    mc "How-{w=0.5}{nw}"
    mc "Wait, no. Don't answer that. I don't wanna know about your personal life."
    j "How rude..."
    mc "*chuckles* Just testing my privileges as your nephew-in-law."
    scene ch1ep3_176
    with dissolve
    j "We're not there yet, [mc]."
    mc "Hah, right..."
    stop music fadeout 4
    scene ch1ep3_177
    with dissolve
    mc "..."
    mc "Something is bothering me, though..."
    j "Hm?"
    scene ch1ep3_178
    with dissolve
    mc "Clothes? She bought something for her daughter?"
    j "Ah, it's unthinkable for Hera to do that, isn't it?"
    mc "Knowing her? Absolutely."
    play music 'audio/InTheDark.mp3' loop fadein 4
    scene ch1ep3_179
    with dissolve
    j "I'm not trying to paint her in a positive light, but she's simply... broken."
    j "Blinded by what she has lost, she sought retribution to no avail."
    j "When she called to me get these clothes..."
    scene ch1ep3_179a
    with flash
    j "You know, you shouldn't squander the little affection you have for me."
    j "Your daughters need you. When will you realize that?"
    scene ch1ep3_179b
    with dissolve
    h "I'm letting you mind your business, so let me mind mine."
    h "Are we clear?"
    j "Well, whatever...{w} Just don't come crying to me one day, sis."
    h "If it happens, I'll be glad to kneel before you and say I was wrong."
    scene ch1ep3_180
    with Dissolve(3.0)
    pause
    scene ch1ep3_181
    with Dissolve(2.0)
    pause
    play sound2 woodhit
    show ch1ep3_182
    with hpunch
    mc "What the hell does that mean?!"
    scene ch1ep3_183
    with dissolve
    j "I don't know what's her end goal in all this. However, one thing is for certain..."
    j "Hera... was never your enemy."
    j "That said, she probably won't admit that to anybody."
    scene ch1ep3_184
    with dissolve
    mc "..."
    scene ch1ep3_185
    with dissolve
    mc "... What do you know about the Mentzelopoutous family?"
    j "Tell me what happened."
    mc "Sure, but first, I want you to relay a message to Hera for me."

    scene black
    with dissolve
    with fade

    scene ch1ep3_186
    with dissolve
    j "I see..."
    scene ch1ep3_187
    with dissolve
    j "It seems like we've missed one of our marks..."
    j "I'll have a member of my team investigate them."
    play sound2 cloth
    scene ch1ep3_188
    with dissolve
    mc "Don't bother. I have my people."
    scene ch1ep3_189
    with dissolve
    j "Do you even know what you want to do?"
    mc "Yes."
    j "And that is?"
    mc "Live our blissful lives until we're nothing but ash."
    j "Good."
    mc "I'll be in touch."
    j "Of course."
    scene ch1ep3_190
    with dissolve
    cl "..."
    scene ch1ep3_191
    with dissolve
    cl "Can I have him?"
    j "No."
    scene ch1ep3_192
    with dissolve
    cl "Tch..."
    j "Stop pouting. It's not like you, and it's annoying me."
    stop music fadeout 2
    stop sound fadeout 2

    scene black
    with Dissolve(2.0)
label clairepause:
    if _in_replay:
        $ name = persistent.gallery_name
    scene clairepause
    with dissolve
    $ renpy.pause()
    $ renpy.end_replay()
    play sound 'audio/gamepause.mp3'
    show title at move_slide
    with flash
    $ renpy.notify(imageunlock)
    $ renpy.pause()

    if (freyaroute and freyapoint == 10):
        scene black
        with dissolve
        with fade

        scene ch1ep3_193
        with dissolve
        mc "Hmnn!"
        scene ch1ep3_194
        with dissolve
        mc "Ahh..."
        scene ch1ep3_195
        with dissolve
        yt "Now then... How the heck am I going to give this to her?"
        scene ch1ep3_196
        with dissolve
        mc "..."
        yt "Wait, she should be live right now!"
        yt "Should I check it out?"
        menu:
            "Watch Freya's stream":
                $ freyaroute = True
                jump freyafirstarccontinue
            "Go to sleep":
                $ freyaroute = False
                yt "Nah, I think I'll go to sleep."
                yt "I'll just find a way to give it to her some other time."
                $ renpy.music.set_volume(1.0, 1.0)
                jump freyafirstarcend

        label freyafirstarccontinue:
        $ renpy.music.set_volume(1.0, 1.0)
        play music 'audio/GoodEveningMadam.mp3'
        play sound chair2
        scene ch1ep3_197
        with dissolve
        yt "Now that I think about it..."
        yt "I see her almost every day, but this is my first time watching her stream!"
        scene ch1ep3_198
        with dissolve
        yt "And well... This is my first time on \"Stitch\" too. I need to create an account."
        yt "Should I use my name as my username?"
        mc "..."
        yt "Nah, I'll make something up. I don't want her to know that I'm watching."
        yt "At least for now..."
        $ ftname = renpy.input("Create your \"Stitch\" username (Default: FreyaLover6969)") 
        $ ftname = ftname.strip()
        if ftname == "":
            $ ftname = "FreyaLover6969"
        $ persistent.ftname = ftname
        scene ch1ep3_199
        with dissolve
        yt "[fmc] it is!"
        yt "Alright, onto her profile."
        mc "..."
        yt "Yeah, she's already been live for two hours and has over 10,000 current viewers too!"
        yt "GOD. DAYUM!"
        yt "She does cosplay in each of her streams, right?"
        yt "I wonder what she's rocking tonight..."
        scene ch1ep3_200
        with Dissolve(2.0)
        pause
        $ renpy.music.set_volume(0.1, 0.1)
        play sound guyslamtable
        show ch1ep3_201
        mc "Damn, what is that, bro-oh...{w=1.0}{nw}"
        show ch1ep3_202
        pause 0.5
        show ch1ep3_203
        pause 0.5
        show ch1ep3_204
        pause 0.8
        show ch1ep3_205
        pause 0.1
        hide ch1ep3_205
        show ch1ep3_206
        pause 0.2
        hide ch1ep3_206
        show ch1ep3_205
        pause 0.1
        show ch1ep3_206
        pause 0.2
        show ch1ep3_207
        pause 1.0
        hide ch1ep3_204
        hide ch1ep3_205
        hide ch1ep3_206
        hide ch1ep3_207
        hide ch1ep3_208
        show ch1ep3_205
        pause 0.1
        hide ch1ep3_205
        show ch1ep3_206
        pause 0.1
        hide ch1ep3_206
        show ch1ep3_205
        pause 0.1
        hide ch1ep3_205
        show ch1ep3_206
        pause 0.1
        hide ch1ep3_206
        show ch1ep3_205
        pause 0.1
        hide ch1ep3_205
        show ch1ep3_206
        pause 0.1
        hide ch1ep3_206
        show ch1ep3_205
        pause 0.1
        show ch1ep3_206
        pause 0.1
        show ch1ep3_207
        pause 1.0
        $ renpy.music.set_volume(1.0, 1.0)
        play sound2 chair2
        show ch1ep3_208
        yt "Oh boy, she's really pulling off that... witch costume? A sexy witch costume?!"
        yt "This is unexpected. But holy pixels, she is rocking it!"
        scene ch1ep3_200
        with dissolve
        yt "Those knee-high socks, though. That is some next-level witchery right there!"
        yt "If that's what witches looked like, I wouldn't mind being cursed!"
        play sound chair2
        scene ch1ep3_209
        with dissolve
        yt "Now, if only she could do that... thing... you know... Ehe he hee..."
        play sound woosh
        show ch1ep3_210
        with hpunch
        yt "Ah, shit, she's making me lose it!"
        yt "I need to donate! It's a must!"
        scene ch1ep3_211
        with dissolve
        mc "..."
        scene ch1ep3_212
        with dissolve
        mc "\"To contribute to FlatOverFat's channel, you must first become an active subscriber to her live stream.\""
        play sound woosh
        show ch1ep3_213
        with hpunch
        mc "BULLSHIT!"
        play sound woodhit
        show ch1ep3_214
        with hpunch
        mc "I need to sub to her to donate?! This woman is the epitome of capitalism!"
        mc "I demand the highest tier this instant!"
        scene ch1ep3_198
        with dissolve
        mc "..."
        yt "I don't know why I'm asking her this, but... I'll follow Jess' advice."
        play sound twitchbits
        scene ch1ep3_215
        with Dissolve(0.2)
        f "..." #donation sfx
        scene ch1ep3_216
        with Dissolve(0.3)
        f "Wha..."
        play sound step
        show ch1ep3_217
        f "Ohmygosh~! Big love going out to [fmc] for subscribing to Flat Earthers $100 tier~!"
        f "And donating fifty bucks~?!"
        f "Seriously, thank you from the bottom of my heart for your super-generous donation!"
        scene ch1ep3_218
        with dissolve
        f "Every single one of you in the \"FlatOverFat Family\" is incredibly special to me, but it's donations like these that help keep this magical stream alive!"
        f "Huge virtual hugs to you, [fmc]! You are totally slaying it!"
        scene ch1ep3_219
        with dissolve
        f "Keep sprinkling that awesome sauce everywhere you go!"
        scene ch1ep3_220
        with dissolve
        yt "*chuckles* She really is different when she's in her element."
        yt "Well, looks like she's busy playing."
        yt "Let's wait and see how she responds to my question attached to that donation."
        scene ch1ep3_221
        with dissolve
        "Freya's eyes dart across the screen as her fingers dance over the controls."
        f "Alright, team! We're breaching the enemy's castle now! Archers, you know what to do!"
        "Her face morphs into a determined grin as the on-screen battle rages."
        scene ch1ep3_222
        with dissolve
        f "Whoa! That was a close one. Good thing I've got my trusty shield of Aegis! Remember, folks, always be prepared!"
        scene ch1ep3_223
        with dissolve
        "Giggling, she shoots a playful glance at the camera."
        f "Oops! Looks like I almost walked into that trap. Not today, sneaky mechanics, not today!"
        scene ch1ep3_224
        with dissolve
        "In the final moments of her on-screen conquest, Freya leans forward, the atmosphere is electric."
        f "And here comes the War God's ultimate skill..."
        play sound chair2
        show ch1ep3_225
        with hpunch
        f "BOOM!"
        f "Victory is ours, team! GG everyone, G freaking G!"
        "She throws herself backwards, a satisfied grin plastered across her face."
        play sound chair2
        scene ch1ep3_226
        with Dissolve(0.2)
        f "Phew! That was an epic raid, wasn't it?"
        f "A gigantic thank you to all the brave souls who joined me in the fight. You were all amazing!"
        f "Seriously, I could not have done it without you all. I hope you had as much fun as I did!"
        scene ch1ep3_227
        with dissolve
        f "Now, who's up for another round? The battlefield awaits, people!"
        f "Don't be shy. Everyone's welcome in the \"FlatOverFat Family\"."
        f "In the meantime, I'll put the lobby in a queue while I answer some of the donations."
        f "If you think you have what it takes, join us in the next raid!"
        stop music fadeout 5
        play music2 'audio/HoldMeCloserINST.mp3' fadein 5 loop
        scene ch1ep3_228
        with Dissolve(2.0)
        yt "She looks happy: even more than usual."
        "You watch as Freya confidently commands her audience's attention, her laughter echoing from the computer speakers."
        yt "It's like... she's shining."
        scene ch1ep3_229
        with dissolve
        yt "What is this feeling?"
        yt "This sudden jolt in my chest... It's different."
        yt "Am I... attracted to her?"
        yt "No, that can't be. We're just friends right? Besides, she's Aine's sister."
        mc "..."
        play sound chair2
        show ch1ep3_230
        yt "Wait, hold the phone!"
        yt "Is she..."
        yt "And she's Aine's... sister."
        scene ch1ep3_231
        with dissolve
        yt "Damn it! Is that the reason why she's-"
        scene ch1ep3_232
        with dissolve
        f "And finally, from [fmc]!"
        play sound woodhit
        show ch1ep3_233
        with hpunch
        mc "No, wait! That's... Don't read it, Frey!"
        scene ch1ep3_234
        with dissolve
        f "Have you ever been..."
        play sound step
        show ch1ep3_235
        with hpunch
        f "What do you mean \"Have I ever been in love before\"?!"
        play sound woodhit
        show ch1ep3_236
        with hpunch
        f "Yes, I've loved before! Still am, in fact!" #angrily slams her hands on her table/standing up
        f "It's not something that goes away so easily!"
        "Irritated, she lets out a huff."
        f "The person I love? Well, they're not someone you would expect!"
        scene ch1ep3_237
        with dissolve
        "She hesitates for a moment, a fond smile appearing on her face."
        f "They're kind. The type to help someone, even if it means going out of their way..."
        f "One time, they even carried me when I couldn't get up. Helped me when I twisted my ankle."
        f "And that was... despite me clearly being an inconvenience..."
        scene ch1ep3_238
        with dissolve
        f "Hah! You know what? They're hardworking, too!"
        f "The type who never backs down, always giving their best in everything they do!"
        f "You can always rely on them to be there, no matter what!"
        play sound chair2
        scene ch1ep3_239
        with dissolve
        f "But..."
        "The smile on her face fades away as she slowly returns to her chair, wrapping her arms around her legs, her gaze far away."
        f "But the worst part?"
        f "They don't even know I exist..."
        f "Not in the way I want to be, at least..."
        f "I'm always in the shadows, always... the second choice."
        scene ch1ep3_240
        with dissolve
        f "So yeah, I'm in love..."
        f "But it's a love bound to be unrequited..."
        "Her last sorrowful comment leaves a poignant silence in the room."
        scene ch1ep3_241
        with dissolve
        "She gazes towards her screen, seeing her chat turn silent."
        "After a few moments, some chime in with shocked responses."
        "Only then does she realize the words that she uttered subconsciously."
        scene ch1ep3_242
        with dissolve
        f "What... what have I..."
        f "..."
        scene ch1ep3_243
        with dissolve
        f "*hics*"
        show ch1ep3_244
        "In one quick movement, Freya abruptly closes the stream as tears flood her eyes."
        scene ch1ep3_245
        with dissolve
        mc "Frey, why didn't you..."
        stop music2 fadeout 3
        play music 'audio/LightStorm.mp3' fadein 20
        play sound heartbeatslow loop
        scene ch1ep3_246
        with flash
        pause
        scene ch1ep3_247
        with dissolve
        pause
        scene ch1ep3_248
        with dissolve
        pause
        scene ch1ep3_249
        with dissolve
        pause
        scene ch1ep3_250
        with dissolve
        pause
        scene ch1ep3_251
        with dissolve
        pause
        if aineroute:
            scene ch1ep3_252
            with dissolve
            pause
            scene ch1ep3_253
            with dissolve
            pause
        scene ch1ep3_254
        with flash
        scene ch1ep3_255
        with flash
        scene ch1ep3_256
        with flash
        pause 1.0
        play sound thud3
        play sound2 running loop
        show ch1ep3_257
        with hpunch
        mc "Tsk!"
        play sound closedoor
        scene ch1ep3_258
        with Dissolve(0.1)
        a "[mc]?"
        mc "Sorry, Aine, I'll talk to you later!"
        stop sound2 fadeout 2
        scene ch1ep3_259
        with dissolve
        pause
        play sound closedoor
        scene ch1ep3_260
        with dissolve
        pause
        scene ch1ep3_261
        with dissolve
        f "*sniffs*"
        scene ch1ep3_262
        with dissolve
        f "H-hey, [mc]. What's up?"
        scene ch1ep3_263
        with dissolve
        mc "I saw."
        f "H-huh? What..."
        scene ch1ep3_264
        with dissolve
        mc "I know you'll deny it, but that doesn't matter."
        mc "I saw your stream and heard everything you said."
        mc "All I want right now is for you to talk to me face to face."
        f "W-what... H-hold on, I..."
        scene ch1ep3_265
        with dissolve
        mc "Frey... Do you like-{w=0.8}{nw}"
        mc "No."
        mc "Do you love me?"
        scene ch1ep3_266
        with dissolve
        "As the question pierces her soul, the composure that she has so painstakingly kept to that point simply splinters."
        "And the tears she has been valiantly holding back start to flow freely."
        scene ch1ep3_267
        with dissolve
        f "*hics* N-no, I don't~!"
        mc "Alright. Pardon me for what I'm about to do."
        scene ch1ep3_268
        with dissolve
        f "What-{w=0.5}{nw}"
        play sound chair2
        show ch1ep3_269
        with hpunch
        pause
        "With a firm yet gentle hold on her arm and waist, you pick her up from her seat."
        "And in a moment of breathless anticipation, you claim her first kiss."
        "As your lips meet, you feel Freya tense up for a brief moment, caught off-guard by your actions."
        scene ch1ep3_270
        with dissolve
        "But she just as quickly melts into your arms, pulling you in closer as she presses her lips into yours."
        "Finally, you break away."
        scene ch1ep3_271
        with dissolve
        mc "Sorry about that."
        "You give her a sly grin."
        mc "But not really."
        f "My first kiss..."
        mc "Was it worth the wait?"
        f "..."
        "She pauses, at a loss for words."
        mc "*laughs* Should we try again to make sure?"
        "She gives a quick nod."
        mc "Good choice."
        scene ch1ep3_270
        with dissolve
        "You bring her towards you, closing the distance between your lips."
        "Her eyes flutter closed as she wraps her delicate arms around your neck."
        "You hold the kiss for what seems like a lifetime, until Freya breaks away."
        scene ch1ep3_271
        with dissolve
        mc "So? How about now?"
        "Sheepishly, she speaks so quietly you can barely hear her."
        f "{size=-10}Wow..."
        mc "What was that?"
        f "I said, wow..."
        mc "Yeah, that's how I feel too."
        f "R-really?"
        mc "Yeah. You think that I'd just feel the same after kissing a pretty girl?"
        f "Pretty... me...?"
        mc "I said what I said."
        scene ch1ep3_272
        with dissolve
        f "Thank you, [mc]... you don't know how happy you've just made me." #smiles
        f "Hell, right now it feels like I'll be happy for the rest of my life, knowing that I caught your eye."
        mc "Well, how could I say no to such an amazing costume?"
        label freyastitchcosplay:
        if _in_replay:
            $ name = persistent.gallery_name
        stop music fadeout 4
        scene ch1ep3_273
        with dissolve
        f "Oh... so it's just the costume that you like?"
        "Freya's expression falls, seemingly dejected by your words."
        "But you can just make out a smile tugging on the corner of her lips as she speaks."
        yt "Getting playful again, are we, Freya?"
        yt "Just like last time, two can play at that game."
        play music 'audio/LikeThat.mp3' fadein 4
        scene ch1ep3_274
        with dissolve
        mc "Yeah, it's totally the costume. Not like I meant it when I called you a pretty girl just now."
        f "Is that right?"
        mc "Mhm. I just have a thing for witches and the spells they cast on me..."
        f "And the witches like your lame puns?"
        mc "You'd be surprised. Then again, if you were a real witch, wouldn't you already know?"
        f "Don't make me use my magic to shut you up."
        mc "And how exactly do you plan to do that?"
        scene ch1ep3_275
        with dissolve
        "She leans in, resting her hands on your chest."
        "Her next words tell you everything you need to know about her intentions."
        f "Why don't you come closer and find out?"
        mc "My pleasure."
        scene ch1ep3_276
        with dissolve
        "You lean in to kiss her again."
        "She brings her lips towards yours..."
        show ch1ep3_277
        "... but at the last second, she pulls away and shoves you back."
        play sound thud2
        show ch1ep3_278
        with hpunch
        "Though she didn't use that much force, the unexpected move causes you to stumble backwards and trip on the carpet."
        "You fall, landing with a loud \"thud\" on your butt."
        scene ch1ep3_279
        with dissolve
        m "Hm? Did Freya throw her chair for her video again?"
        show ch1ep3_280
        f "Oh my god! I'm so sorry, [mc]!"
        "Freya runs towards you, clearly concerned."
        scene ch1ep3_281
        with dissolve
        f "Are you ok?"
        mc "Don't worry: the only thing hurt is my pride."
        f "I'm sorry, that was a terrible idea. I'll stop to-"
        mc "No, let's keep going."
        f "Are you sure?"
        mc "I'm still wondering how exactly you'll bewitch me into being... {i}quiet{i}."
        scene ch1ep3_282
        with dissolve
        f "Oh... oh!"
        f "In that case..."
        scene ch1ep3_283
        with dissolve
        f "Pants. Off. Now."
        "She points her finger at you, waving it in a circular motion as she casts the \"spell\"."
        "Even though it's the first time she's doing anything like this, she's getting into the roleplay even more than when she was streaming."
        "You can't help but chuckle at her naivety and enthusiasm."
        mc "Yes, Madam Witch."
        play sound cloth
        scene ch1ep3_284
        with dissolve
        "You take off your pants, leaving your underwear as the only barrier between Freya's eyes and your manhood."
        scene ch1ep3_285
        with dissolve
        f "..."
        "Freya pauses, as if unsure where to go from here."
        mc "What's wrong, Frey?"
        scene ch1ep3_286
        with dissolve
        f "Am I doing too much, [mc]?"
        f "It's my... first time doing something like this..."
        mc "What do you mean? You weren't like this after work earlier."
        f "I know, it's just..."
        f "I don't want to go too far..."
        "She trails off again."
        "Even though she doesn't finish her thought, you can still understand what she wants to say."
        mc "Hey, let's just go with the flow, okay?"
        mc "Just do what you feel like you want to. Don't worry about anything else right now."
        mc "If something doesn't feel right, we can stop. Otherwise, let's just enjoy ourselves, yeah?"
        scene ch1ep3_287
        with dissolve
        f "Yeah... yeah, that sounds good."
        mc "Perfect. Now, what are you going to do next, Madam Witch?"
        scene ch1ep3_288
        with dissolve
        "She smiles, getting back into character."
        scene ch1ep3_289
        with dissolve
        f "Now that you're under my spell, let's test if it's really just the costume that turns you on."
        f "I wonder, what will your reaction be if I get rid of it?"
        play sound cloth
        scene ch1ep3_290
        with Dissolve(2.0)
        "She strips off her blouse, using her arms to cover her breasts."
        f "If you can remain {i}unaroused{/i} when you see me without my dress, then I'll release you from my spell and give you a nice reward."
        f "If you fail this challenge, then you'll see what punishment I have in store..."
        mc "Interesting..."
        "Right on cue, you feel mini-[mc] beginning to wake up."
        yt "Yeah, there's no way I win this challenge. Let's see what \"punishment\" she has in mind."
        scene ch1ep3_291
        with dissolve
        "Freya also seems to notice a disturbance in the force and looks down at your crotch."
        "She smirks, continuing her monologue."
        scene ch1ep3_292
        with dissolve
        f "I see your willpower is failing you already, human."
        f "Perhaps I should ease your burden a little?"
        scene ch1ep3_293
        with Dissolve(1.0)
        "With that said, she moves her arms to the side, exposing her soft tits."
        f "But then again, where's the fun in that?"
        "What Freya's tits lack in size, they make up for in excitement and personality-just like their owner."
        scene ch1ep3_294
        with dissolve
        "Mini-[mc] is begging to join the fun at this point, and your underwear can no longer hide the bulge between your legs."
        f "Well, would you look at that? It seems like you don't just have a thing for witch costumes."
        "Now that your manhood has betrayed you, Freya seizes the opportunity to take more control."
        scene ch1ep3_295
        with dissolve
        f "You're just a nasty pervert who will go for any girl that shows you her boobs, aren't you?"
        "She looks down at you, feigning disgust."
        mc "No... it's not like that..."
        f "Stop lying. Do you know what witches do to liars?"
        "You hold your tongue, curious to see where Freya will take things."
        mc "..."
        scene ch1ep3_296
        with dissolve
        pause
        "She struts towards you, resting her foot mere inches from your throbbing cock." #resting on the ground
        f "They {i}crush{/i} them beneath their feet like the scum that liars are."
        mc "No... please, don't..."
        "You play along, pretending to be scared."
        scene ch1ep3_297
        with dissolve
        "Freya continues staring down at you, then speaks."
        f "But you, human, are lucky. For some reason, I think I've taken a liking to you."
        f "And for that reason, I will not crush you."
        f "However, you still deserve to be punished. And I know just the thing to do."
        mc "What are you going to do...?"
        scene ch1ep3_298
        with dissolve
        f "If you admit that you're a dirty pervert, I'll give you an easier punishment: I'll {i}release{/i} you, but I won't use my hands to touch your filthy human skin."
        mc "So that means..."
        f "... I shall use my feet, and only my feet."
        f "Or, you could stubbornly deny the truth and-"
        mc "I'm a dirty pervert, one hundred percent!"
        scene ch1ep3_299
        with dissolve
        f "Well, that was easy..."
        mc "Honestly, things are starting to get a little painful down there, so..."
        scene ch1ep3_300
        with dissolve
        f "*giggles* Really? The tent in your boxers isn't making that obvious at all."
        "She briefly breaks character to offer some sarcasm and extend your suffering for a few more seconds, then resumes her witch duties."
        scene ch1ep3_301
        with dissolve
        f "I mean, who said you could speak, human?"
        f "Just for that, I order you to take off what remains of your garments."
        f "You will now be completely exposed for your punishment."
        mc "Yes, Madam..."
        play sound cloth
        scene ch1ep3_302
        with dissolve
        "You eagerly take off your remaining clothing, leaving yourself bare in front of Freya."
        "Grinning, she picks her foot up and moves it until it rests just above your cock."
        f "Good. Now, we can begin."
        f "Remember, do not speak unless spoken to. Understand?"
        mc "Loud and clear."
        show freya8
        with dissolve
        "The moment those words leave your mouth, Freya begins rubbing her sole on the underside of your dick."
        "The soft skin of her foot combined with the subtle friction from the stocking massages your manhood with a sensation you've never felt before."
        yt "Damn! I'm not normally a foot guy, but I could get used to this..."
        "Despite being a complete novice, Freya uses her whole foot to stimulate your member like a seasoned pro."
        "Up and down her foot goes, gliding from the top of your head down to the base of your scrotum."
        "She starts slowly, but gradually increases the pace as she gets used to the movement."
        yt "Fuck... that's {i}gooooood{/i}..."
        "Your already-pulsating cock rages even faster as the blood rushes south in response to her movements."
        "Freya interjects with a playful question."
        f "So, pervert, are you sorry for what you did?"
        mc "Fuuuuuck..."
        f "That's not a valid response."
        mc "Y-yes, I am Madam."
        f "Much better. I think you've had enough punishment..."
        yt "No, please don't say that..."
        f "Unless you want more?"
        yt "YES."
        mc "M-more..."
        f "More? You are strange, human. But I approve your request."
        show freya9
        with dissolve
        hide freya8
        "She changes tactics, using her toes to rub across and around the tip of your dick."
        "Her small toes wrap around your firm head, massaging ecstasy into your body with every movement."
        yt "Shiiit... between her stream tonight and all the teasing just now, this is getting too good..."
        yt "I don't want to ruin a good costume, but I might not be able to hold back for much longer..."
        mc "Mgh..."
        "A rogue moan escapes, your mouth unable to contain the pleasure."
        f "Did I not say only to speak when spoken to, human?"
        mc "I'm sorry, Madam Witch..."
        f "Nope, sorry won't cut it this time. Your punishment will now become even {i}harder{/i}."
        "With that, Freya speeds up even faster."
        "She massages the entire length of your cock again, but this time adds some additional pressure once she reaches the tip."
        "It's as if she's stepping on your manhood ever so slightly: not enough to cause pain, but enough to send your brain into overdrive trying to process all the different stimuli."
        yt "Shit! Shit! Shit! She's just too good at this!"
        "You can feel the tension building in your dick, your manhood begging for release."
        "Your breathing becomes more ragged as you approach your peak."
        show freya10
        with dissolve
        hide freya9
        "With the last threads of your self-control holding back your load, you look up to check Freya's expression."
        "Her gaze is focused on your cock, intent on having you submit to her desire and cum."
        "Beads of sweat grow on her brow as she continues to move her foot vigorously, reflecting the effort that she's pouring into her actions."
        "Her boobs rise and fall with each breath, glistening in the light as the sweat starts runing down her skin."
        "This sight is enough to break the last holds of your resistance."
        show ch1ep3_303
        with hpunch
        hide freya10
        mc "Rrgh!!"
        "Without warning, you unload your hot cum all over Freya's foot."
        "Your dick pumps out stream after stream, showering her foot in thanks for the \"punishment\" it gave."
        scene ch1ep3_304
        with dissolve
        "Finally, you release your last load."
        "You sit breathless, attempting to regain your composure."
        scene ch1ep3_305
        with dissolve
        "Freya reaches down and tilts your chin up to meet her gaze."
        f "Your punishment has been fulfilled. You may leave now, human."
        mc "Now?"
        f "Uh, yeah, [mc]? I gotta clean up this mess somehow." #raises her foot
        mc "Hah, sorry about that."
        scene ch1ep3_306
        with dissolve
        f "No, this is perfect!"
        f "I mean, I may never be able to wear these stockings again, but everything about this was even better than I imagined."
        mc "Really? But you didn't have the chance to cum yet?"
        f "It's fine, really! I'm just glad I could reward you for the happiness you've given me tonight."
        mc "All I did was speak from my heart..."
        f "And I'm so glad you did, [mc]. Thank you."
        scene ch1ep3_307
        with dissolve
        "Freya starts to shuffle towards the door."
        f "But really, I need to clean this off before it sets and ruins a good pair of-"
        play sound thud3
        show black
        with hpunch
        f "AAAHHH!"
        scene ch1ep3_308
        with Dissolve(1.0)
        "Freya trips over your foot and falls flat on her face."
        mc "Freya!"
        scene ch1ep3_309
        with dissolve
        f "Ugh... I'm fine, no worries."
        f "That was embarrassing..."
        scene ch1ep3_310
        with Dissolve(2.0)
        "Slowly, she starts to push herself up."
        "As she does, you notice her bare backside fully exposed, practically staring at you..."
        yt "Hmm... maybe I can give her a little surprise too..."
        yt "Well... When life gives you peaches!"
        play sound cloth2
        show ch1ep3_311
        "Quickly, you get up and grab Freya's arms from behind, preventing her from moving."
        f "Hey! What are you doing, [mc]?"
        mc "Now that I'm no longer under your spell, it's time for me to get my revenge."
        mc "That's what happens once you break free from an enemy spell, wouldn't you agree?"
        scene ch1ep3_312
        with dissolve
        f "W-well... I can't say I hate the idea..."
        mc "Good, because I'm not waiting any longer."
        mc "Stay put, or else you'll have to see the punishment that {i}I{/i} have for {i}you{/i}."
        f "Mmm... what if I want to be punished?"
        mc "Then I'd say save it for later."
        mc "Right now, I'm in control."
        f "Then stop talking..."
        f "And start controlling..."
        "She doesn't have to tell you twice: Little [mc] is already ready for round two."
        play sound cloth
        scene ch1ep3_313
        with dissolve
        "You pull off her panties, exposing her completely."
        "Using your hands to spread her cheeks slightly, you slide your cock into the narrow cleft."
        show freya11
        with dissolve
        "You start to move your hips back and forth, grinding your dick in between her glutes."
        "The tenderness of her butt sandwiches your sausage, squeezing you with the perfect amount of force."
        "Your thighs slap against hers, forming a steady rhythm as you find the perfect pace."
        "Sensing your cock twitching in excitement, Freya begins to move her butt up and down, intensifying the pleasure."
        "Suddenly, Freya speaks."
        f "So... do you like my butt?"
        mc "Urh! Do I really need to answer that?"
        f "Fine, I guess I'll stop moving..."
        yt "Don't you fucking dare, you little witch."
        mc "Fine, you asked for it! No, I don't like it."
        f "R-really?"
        mc "Yeah... I'm totally obsessed with it! Can't you tell?"
        f "You rascal..."
        mc "Hey, look who's talking! You're the one that's interrupting a good time."
        f "Sorry... I wanted to check if I was doing the right thing."
        mc "No need to be sorry. You're perfect-"
        mc "I mean, you're doing perfect."
        f "Heeh, okay!"
        f "Faster?"
        mc "Please!"
        show freya12
        with dissolve
        hide freya11
        "You ramp up the intensity, using your hands to drive her hips towards you as you grind against her even faster."
        "Freya also moves quicker, using her entire body to move her cheeks against your dick."
        "The pleasure builds throughout your groin as your body gives into the heavenly sensation."
        "Note to self: after this, tell Freya to keep doing whatever butt workout she's doing. Or say a prayer thanking the gods of genetics."
        f "Mmhhh... hahh... hahh..."
        "Amid her efforts to keep pace with you, Freya lets out a subtle moan."
        "Seems like you're not the only one enjoying this."
        yt "Sensitive ass, too? Damn, the things I could do to this girl..."
        "You try to think of the possibilities, but those thoughts are drowned out by the swells of euphoria coming from your lower half."
        mc "Huh... urhh!"
        yt "Shit... it's getting harder to keep this up!"
        yt "The movements, that is."
        yt "I better finish soon, otherwise I'll probably just collapse from all the sensations!"
        f "Hahh... nnhhh... mmhh..."
        yt "And it sounds like Freya might not be that far away either."
        yt "I wonder if-no, stop it [mc]. Focus before you-"
        mc "Rgaah! Ah..."
        show ch1ep3_314
        hide freya12
        mc "Hahh?"
        show ch1ep3_315
        f "Ha-eep!"
        "Your concentration breaks for just one moment, but that was enough to cause you to slip."
        "Sensing something warm and wet on your dick, you look down."
        scene ch1ep3_316
        with Dissolve(1.0)
        yt "Oh. Shit."
        "The head of your cock is now nestled inside Freya's pussy."
        scene ch1ep3_317
        with dissolve
        mc "Oh fuck! Sorry, Frey!"
        "Your face turns red in shock, and you begin to remove yourself from her."
        show ch1ep3_318
        f "Wait, no! Keep going!"
        mc "Keep going?"
        f "Yeah!"
        mc "Are you sure? This is your first time doing anything like this, so-"
        show ch1ep3_319
        with hpunch
        f "JUST DO IT!"
        f "JUST DO ME!"
        scene ch1ep3_320
        with dissolve
        mc "Well, alrighty then!"
        "To whichever being gave this girl her personality, thank you a thousand times."
        mc "But let's take it slowly for now."
        f "Hell no. You feel how wet I am already?"
        mc "Perhaps..."
        f "I can handle it, believe me."
        mc "You're really sure about that?"
        f "[mc], are you going to keep playing 20 questions, or are you actually going to do what we both really want you to do?"
        mc "Good point. You stay right there."
        mc "Sending Delta team in to breach, starting now."
        scene ch1ep3_321
        with dissolve
        "You push yourself deep into her, still somewhat slowly, in case she feels any pain."
        "To your surprise, she doesn't give any indication of discomfort at all."
        scene ch1ep3_322
        with dissolve
        f "*gasp* Ahhhh yesss...."
        "Instead, she expresses pure satisfaction and pleasure."
        "Seeing this, you begin moving again."
        show freya13
        with dissolve
        "You start slowly at first. However, Freya senses that you're holding back, so she takes the initiative to move herself quicker."
        "You mirror her movements, and soon both of you resume a steady rhythm, skin clapping against each other's."
        "Despite this being her first time, you feel almost no resistance when you move inside her."
        "Instead, her tight inner walls hug your dick like a glove, squeezing you with each thrust."
        f "Ahhh! Mhhh!"
        f "Y-yeah... that's more like it!"
        "For a first-timer, Freya certainly isn't acting like one. Her movements and words would make even porn stars jealous."
        "This girl is one of a kind, that's for sure. All those tips are well-deserved."
        mc "Urh! Damn! You're a n-natural, Frey!"
        f "Mhh! Thanks! I think..."
        show freya14
        with dissolve
        hide freya13
        "You continue pounding her with everything you have, but Freya doesn't flinch."
        "In fact, it seems like the more you move, the tighter she holds you."
        "Maybe it's because you're already tired, or because she's unbelievably multi-talented, or because your cock is extra sensitive from all the attention earlier."
        "Either way, you find yourself once again having to hold back before you reach the point of no return."
        f "Nghh!! Mmhh!!!"
        "And it seems like Freya isn't far off either."
        mc "Frey! I'm gonna cum!"
        f "Nhahh! Not inside!"
        f "P-pull out!"
        "The pressure comes to a head again, threatening to blow over."
        show ch1ep3_323
        with hpunch
        hide freya14
        mc "Grahhg!"
        f "Nghhh!!!!" with hpunch
        "At the last second, you pull back and release your cock from its hold."
        "Not a second later, your cock releases stream after stream, adorning Freya's back with white stripes."
        play sound thud3
        show ch1ep3_324
        with hpunch
        "You collapse next to Freya, unable to hold yourself up anymore."
        mc "Ahh, shit... that was..."
        f "Wow..."
        mc "Yeah, exactly."
        scene ch1ep3_325
        with dissolve
        f "I... actually meant... wow... my dry cleaner is... going to kill me..."
        mc "Sorry. Was either the carpet or your back, and I chose the latter."
        f "Haha... understandable..."
        play sound cloth
        scene ch1ep3_326
        with dissolve
        f "Anyway, I better get changed..."
        f "... Maybe after I can feel my legs again..."
        $ renpy.end_replay()
        mc "Heh... you know-{w=0.6}{nw}"
        stop music
        play sound closedoor
        show ch1ep3_327
        a "Frey?"
        scene ch1ep3_328
        with dissolve
        mc "Oh... Fuck..."
        play music 'audio/HoldMeCloser.mp3'
        play sound gasp
        show ch1ep3_329
        a "*gasps*"
        "Though her hands cover her mouth, Aine's disgust is clearly visible through her glare."
        play sound closedoor
        show ch1ep3_330
        pause
        scene ch1ep3_331
        with dissolve
        f "What's with that..."
        show ch1ep3_332
        with hpunch
        f "... FUCKING GLARE!!"
        mc "Hey, Frey, wait!"
        play sound closedoor
        show ch1ep3_333
        f "AINEEEEEEE!!!"
        play sound cloth2
        show ch1ep3_334
        with hpunch
        a "Urk!"
        a "L-let go..."
        play sound thud3
        show ch1ep3_335
        with hpunch
        a "OF ME!!"
        show ch1ep3_336
        pause 0.5
        play sound punch
        show ch1ep3_337
        with hpunch
        f "AAAAAGGHHH!!!"
        play sound thud3
        show ch1ep3_338
        with hpunch
        pause
        play sound closedoor
        scene ch1ep3_339
        with dissolve
        mc "Shit, shit, shit!"
        m "What's going on?"
        scene ch1ep3_340
        with dissolve
        mc "Go get Gwen, quick!"
        m "Roger."
        scene ch1ep3_341
        with dissolve
        f "Giiiiaaagghhh!"
        a "L...Let go, Freya!!"
        scene ch1ep3_342
        f "Why did you even come in here, huh?! To judge me again?! To show your disgust?!"
        a "Urk! I came to... talk! But I wasn't expecting to... find THIS!"
        f "So what if you did? It's none of your fucking business!"
        scene ch1ep3_343
        a "It... is my business because you are my sister! Do you have any idea how this looks?!"
        f "Oh, spare me your sanctimony! I'm tired of living in your perfect little shadow!!"
        f "Maybe, for once, I wanted to choose for myself!!"
        a "Is this how you rebel?! By jumping into bed with the first guy you see?!"
        scene ch1ep3_344
        with dissolve
        mc "That's not fair. We care about each other. This isn't just some fling, Aine."
        scene ch1ep3_345
        f "You wouldn't understand, Aine!"
        f "Your life was always set out for you, a perfect path laid out by Hera!"
        f "Meanwhile, I was left to fend for myself!"
        scene ch1ep3_346
        a "H-huh?! Do you think I enjoyed that?! Being paraded around, controlled, used?!"
        a "At least you had the freedom to make your own choices!!"
        scene ch1ep3_347
        f "Choices?! What fucking choices?!"
        f "While you had everything handed to you, I constantly fought for goddamn scraps!"
        scene ch1ep3_348
        mc "Frey, calm down!"
        yt "I can't... pull her off!"
        yt "Shit, how can she be so strong?! Is it the adrenaline?!"
        scene ch1ep3_349
        f "No, she has to hear it!"
        f "Every achievement, every compliment, every opportunity was handed to her!"
        scene ch1ep3_350
        with dissolve
        f "While I... I had to fight for even an ounce of recognition!"
        scene ch1ep3_351
        a "Because of choices like this, Freya!"
        a "It's always been this way! You, seeking attention in all the wrong places!"
        f "Maybe if I had a fraction of the attention you had, I wouldn't have to!"
        play sound closedoor
        show ch1ep3_352
        g "That's enough!"
        play sound cloth2
        show ch1ep3_353
        with hpunch
        pause
        play sound cloth2
        show ch1ep3_354
        with hpunch
        pause
        scene ch1ep3_355
        a "Look! Look at what you've done, Freya! Look at the chaos you've caused!"
        scene ch1ep3_356
        f "Me?! This isn't about me! This is about you never standing up for me, never being there when I needed you!"
        scene ch1ep3_357
        g "This isn't the place to hash this out, you two! Calm the fuck down!"
        scene ch1ep3_358
        with dissolve
        a "She's right. We're done here..."
        f "For once, I agree!"
        play sound fistbump
        show ch1ep3_359
        with hpunch
        a "Let me go, Gwen."
        g "You sure? If you guys start again, I might break a bone or two."
        a "None of your damn business."
        g "Yeah? I'll do it anyway, so try me."
        a "Whatever."
        if aineroute:
            scene ch1ep3_360
            with dissolve
            a "As for you, [mc], what were you thinking? My sister, really?"
            a "Out of everyone you could have landed yourself with, you decided to go for MY SISTER?"
            mc "Aine, it just happened, and..."
            a "And what? You think that makes it all right?"
            mc "It wasn't my intention. I just..."
            scene ch1ep3_361
            a "Oh, for f..."
            scene ch1ep3_362
            with dissolve
            a "*deeply inhales*"
            scene ch1ep3_360
            with dissolve
            a "Words cannot and will not express how disappointed I am right now."
            a "But trust me, we will have a word later, [mc]. You should have known better."
            scene ch1ep3_363
            with dissolve
            mc "This isn't just on me, Aine, you know that. Both of you had issues that you kept from each other."
            a "..."
        else:
            scene ch1ep3_360
            with dissolve
            a "And [mc], I'll speak with you later. You should've known better."
            scene ch1ep3_363
            with dissolve
            mc "This isn't just on me, Aine, you know that. Both of you had issues that you kept from each other."
            a "..."
        scene ch1ep3_364
        f "Leave him out of this, Aine! This is between you and me!"
        g "Jesus, go grab a beer to calm both of you guys' tits down, will you?"
        scene ch1ep3_365
        with dissolve
        a "Just so you know..."
        a "Those words cut deeper than you realize, Freya..."
        play sound closedoor
        scene ch1ep3_366
        with dissolve
        pause
        scene ch1ep3_367
        with dissolve
        f "*hics*"
        play sound doorslam
        show ch1ep3_368
        with hpunch
        pause
        stop music fadeout 20
        scene ch1ep3_369
        with dissolve
        g "*sighs*"
        if gwenroute:
            scene ch1ep3_370
            with dissolve
            g "So, what now?"
            mc "Let me take care of this."
            scene ch1ep3_371
            with dissolve
            g "..."
            mc "\"No real fights between the girls\". Yes, I know. I'm sorry."
            image gwmctabhcon:
                "ch1ep3_372.jpg"
                pause 3.0
                "ch1ep3_373.jpg"
                pause .2
                repeat
            show gwmctabhcon
            with dissolve
            g "I've said this a couple of times and will repeat it..."
            g "You have my full support on this \"harem\" thing."
            g "I will, and always will be on your side no matter what."
            g "But if this kind of physical fight between the girls happens again, I'll have to call the plan off. Do you understand?"
            mc "Mhm."
            mc "Wait, so you're not against the... you know?"
            g "You hitting on Aine's sister?"
            g "Uhh... No? Why would I be? I like it, even. It's quite hot."
            mc "I guess you're degenerate enough to like this kind of thing."
            scene ch1ep3_374
            with dissolve
            g "And what about her?"
            scene ch1ep3_375
            with dissolve
            mc "What about-huh?"
            play sound woosh2
            show ch1ep3_376
            with hpunch
            mc "Holy sh-"
            mc "How long have you been listening?!"
            m "Since Gwen got here."
            scene ch1ep3_377
            with dissolve
            mc "Oh no..."
            m "Don't mind me. I don't really care whatever that was."
            m "You have other places to be, don't you? Go."
        else:
            scene ch1ep3_370
            with dissolve
            g "So, what now?"
            mc "Let me take care of this."
            scene ch1ep3_374
            with dissolve
            g "What about her?"
            scene ch1ep3_375
            with dissolve
            mc "What about-huh?"
            play sound woosh2
            show ch1ep3_376
            with hpunch
            mc "Holy sh-"
            mc "How long have you been listening?!"
            m "Since Gwen got here."
            scene ch1ep3_377
            with dissolve
            mc "Oh no..."
            m "Don't mind me. I don't really care."
            m "You have other places to be, don't you? Go."

        scene black
        with dissolve
        with fadeq

        scene ch1ep3_378
        with dissolve
        yt "Damn it. I didn't expect that. Especially Freya's perspective on Aine."
        yt "While Aine handled it well and did not explode like Freya... as expected, Freya went below the belt in that fight."
        scene ch1ep3_379
        with dissolve
        yt "I so wanna talk to Aine, but I think I should prioritize the lady in tears now."

        scene black
        with dissolve
        with fade

        play music 'audio/Sentient.mp3' fadein 2
        play sound doorknock
        scene ch1ep3_380
        with dissolve
        mc "Frey? You in here?"
        f "... Yeah. Come in."
        play sound closedoor
        scene ch1ep3_381
        with dissolve
        f "Did you speak to her?"
        mc "No, not yet. I wanted to see how you were first."
        f "Thanks. It means a lot."
        mc "How're you holding up?"
        f "I... I let my emotions get the best of me."
        f "*sniffs* I don't know why I said what I said. I... I never meant to hurt her. Not like that."
        mc "It's okay, just breathe, Frey."
        image mcfretafrainf:
            "ch1ep3_382.jpg"
            pause 3.0
            "ch1ep3_383.jpg"
            pause .2
            repeat
        show mcfretafrainf
        with dissolve
        f "*hics* It's just... all these emotions and memories came flooding back, and I couldn't control myself."
        yt "Yeah, Jess did mention she was hard to handle once she explodes."
        mc "I saw the pain in both your eyes. You both have your scars from the past."
        mc "But you need to remember that words, especially in the heat of the moment, can leave the deepest wounds."
        f "I know. I was... just so angry and hurt after seeing her glaring at us like that."
        f "For years, I felt overshadowed. And when she saw us together, I felt like I was being judged all over again."
        mc "Do you really believe that Aine looks down on you? Or is it the weight of your insecurities pushing you to feel that way?"
        f "... Maybe both. I've always felt like the backup, the second choice."
        f "And when I finally find something for myself, I end up ruining it by losing control."
        mc "Nothing's ruined, Frey. But it would be best if you confronted these feelings head-on. Not just for Aine's sake, but for your own."
        scene ch1ep3_384
        with dissolve
        hide mcfretafrainf
        f "Ugh... How do I even begin to apologize? She must hate me now." 
        mc "Well, it's never easy to admit we're wrong. But if you genuinely feel remorse, it'll show."
        image mcfretafrainf2:
            "ch1ep3_385.jpg"
            pause 3.0
            "ch1ep3_386.jpg"
            pause .2
            repeat
        show mcfretafrainf2
        with dissolve
        f "I'm just... I'm so scared now, [mc]."
        f "What if she never forgives me? What if our relationship is damaged forever?"
        mc "Frey, the bond between siblings is complex and strong. It might take time, but you both will find a way to mend things."
        mc "But it starts with you reaching out first."
        mc "Knowing Aine, she might even forgive you once you admit you were wrong."
        scene ch1ep3_387
        with dissolve
        hide mcfretafrainf2
        f "*sobs* I shouldn't have done that."
        f "It's just... it's always been like this, like I didn't matter. All because Aine was... well, Aine."
        mc "What do you mean?"
        show mcfretafrainf2
        with dissolve
        f "She was the golden child, [mc]. Mom saw something in her, something she could use – her beauty, her charm, her intellect."
        f "She was the key to all of Mom's plans. And then there was me, just... Freya. The one in the background."
        mc "She didn't want that. And I know you wouldn't want to be in her place, either."
        mc "Trust me, that doesn't define your worth, Frey."
        f "Yeah, I know. I know that, but..."
        f "... But somehow it feels like it does!"
        f "Especially when mom spent so much time with Aine, leaving me behind because I was too young and couldn't match Aine's charm and beauty."
        scene ch1ep3_388
        with dissolve
        hide mcfretafrainf2
        f "Or... maybe I was just not useful to Mom at all..."
        f "That's why I turned to gaming. It was my refuge."
        f "A place where I mattered. Where I could connect with others and be seen for my skills."
        f "And then one day, I found streaming..."
        f "Then, thousands saw me and acknowledged me. For once, I wasn't just Aine's shadow."
        mc "You found your own light, your own path."
        f "Yes, but... it wasn't enough. The validation from viewers, the fleeting attention... it was temporary."
        f "Deep down, I craved to be seen in the real world. Not as Aine's little sister, but as Freya. Just... Freya."
        mc "And you thought I was that person who would see the real you?"
        f "I did. Because you never treated me as Aine's little sister."
        f "Well, it started with us teasing each other, playing with one another."
        f "But you saw the best part in me. And the more time we spent together, the more I fell for you."
        f "However, irony is cruel. Once again, I felt like I was competing with Aine, for your affection this time."
        f "It tore me apart. The one person who made me feel special, and he's my sister's..."
        if aineroute == False:
            f "Even if it's just for show, your relationship status doesn't deny that you have a responsibility towards each other."
        scene ch1ep3_389
        with dissolve
        mc "I understand, Frey. However, like I said, You don't need a hero in your life."
        image mcfretafrainf3:
            "ch1ep3_390.jpg"
            pause 3.0
            "ch1ep3_391.jpg"
            pause .2
            repeat
        show mcfretafrainf3
        with dissolve
        f "I still don't know what you mean by that."
        mc "Just think about it."
        f "Thinking is all I've been doing, [mc]. Going over every moment, every word. Trying to understand."
        mc "That's the problem, Frey. Sometimes, overthinking can cloud our judgment."
        mc "What I mean is, you've been your own hero, pulling yourself up from the shadows every time you fall."
        mc "That's how you came this far, and I am so, so jealous of you. I could never do that on my own."
        mc "And yet, you're still seeking validation and salvation in others."
        f "But isn't it natural to want to be acknowledged? To be seen and loved for who we are?"
        mc "Absolutely. But seeking acknowledgment should start from within."
        mc "You've come a long way, Freya. Don't let this setback pull you back into your past insecurities."
        scene ch1ep3_392
        with dissolve
        hide mcfretafrainf3
        f "..."
        scene ch1ep3_393
        with dissolve
        f "You're right. But this situation with Aine... It's more than just a setback."
        mc "Look, Aine loves you, even with how complex your relationship is. And I know you love her too."
        mc "This moment, it's a bump in the road. It may be a painful one, but it's also a chance to grow for both of you."
        f "It's just hard... Accepting that I hurt her so deeply."
        mc "Pain has a way of bringing out the worst in us."
        mc "But remember, it also has the power to foster understanding and change. It's up to us to choose which path we tread."
        f "I want to make it right, [mc]. I just don't know how."
        show mcfretafrainf3
        with dissolve
        mc "Alright, let me be your teacher just this once."
        f "Uh-huh...?"
        mc "Start by acknowledging it. Apologies are the first step, but understanding and self-reflection follow closely."
        mc "You'll have to face Aine, and maybe, just maybe, she feels as scared and hurt as you do right now."
        f "*sighs* I hope she can forgive me."
        mc "And I hope you can forgive yourself too. This is as much about self-forgiveness as it is about seeking Aine's understanding."
        scene ch1ep3_394
        with dissolve
        hide mcfretafrainf3
        f "Thank you, [mc]. For being here for me."
        mc "Always, Frey."
        mc "Remember, you don't need to be the golden child to shine."
        mc "You have your own unique light. Don't dim it for anyone, yeah?"
        f "I'll try to remember that."
        mc "Good. Now, I think it's time I talked to Aine. Wish me luck?"
        scene ch1ep3_395
        with dissolve
        f "*chuckles* Yeah, good luck."
        scene ch1ep3_396
        with dissolve
        mc "There you go, there's that chuckle of maturity that I want."
        mc "See you later, Frey."
        f "See you later..."
        scene ch1ep3_397
        with dissolve
        f "Oh, just to be clear, I will never regret that moment between us earlier."
        f "It was fun, and I'm already wondering what I will do next."
        f "Maybe we can explore something... deeper next time."
        scene ch1ep3_398
        with dissolve
        pause
        mc "Oh boy..."
        scene ch1ep3_399
        with dissolve
        f "AHAHAHAHA!"
        scene ch1ep3_400
        with dissolve
        f "Come here for a moment."
        mc "Hm?"
        play sound chair
        scene ch1ep3_401
        with dissolve
        pause
        scene ch1ep3_402
        with dissolve
        f "A bit of a good luck charm."
        mc "*chuckles* Thanks, how sweet of you."
        f "Hah! I don't usually do cringe things like that, but you earned it."
        f "Now go get that woman!"
        mc "I will."
        yt "Though I can still see some pain in that smile, that conversation helped her regain her footing, at the very least."
        yt "She's not as strong as Gwen when it comes to mental fortitude, but she's getting there, slowly but surely."
        stop music fadeout 2

        scene black
        with dissolve
        with fade

        scene ch1ep3_403
        with dissolve
        pause
        yt "Knocking. Knocking again..."
        yt "What's next? A slap? A cold stare? A kick in the ass? Maybe she'll toss the nearest vase at me for fucking her sister?"
        yt "Well... deep breaths. Let's face this head-on."
        play sound doorknock
        scene ch1ep3_404
        with dissolve
        pause
        mc "..."
        mc "Uhh... Aine?"
        "..."
        play sound opendoorcreak
        scene ch1ep3_405
        with dissolve
        mc "Pardon my..."
        play music 'audio/GoodEveningMadam.mp3'
        play sound woosh
        show ch1ep3_406
        a "HRMMMMMNNN~!!"
        yt "That's... surprisingly adorable! Not what I expected at all!"
        yt "Where did all that earlier bravado go, though...?"
        play sound closedoor
        scene ch1ep3_407
        with dissolve
        mc "Aine? You okay?"
        a "What do you think, [mc]?"
        mc "Seems like you're in a battle between being mad and... something else?"
        a "Ugh! I want to be mad, but also... I just... Argh!"
        if aineroute:
            menu:
                "Compliment her":
                    scene ch1ep3_408
                    with dissolve
                    mc "Your anger is too cute. Just like that pout."
                    play sound woosh
                    show ch1ep3_409
                    a "Huh!"
                    play sound fistbump
                    show ch1ep3_410
                    with hpunch
                    a "Knock it off~!"
                    $ ainepoint += 1
                    $ renpy.notify(ainenotif)
                    mc "You handled that well..."
                    stop music fadeout 3
                    scene ch1ep3_411
                    with dissolve
                    a "I wanted to talk, yes, but this... today was overwhelming. It's not what I had in mind!"
                "Let her be{#ch1ep3}":
                    stop music fadeout 3
                    scene ch1ep3_411
                    with dissolve
                    a "I wanted to talk, yes, but this... today was overwhelming. It's not what I had in mind!"
        else:
            stop music fadeout 3
            scene ch1ep3_411
            with dissolve
            a "I wanted to talk, yes, but this... today was overwhelming. It's not what I had in mind!"

        mc "I get it. And I'm genuinely sorry. I never meant for things to escalate this way."
        a "Did you know that was the first time Freya and I fought? Not just a sibling squabble, but truly fought?"
        mc "I didn't... and I can't help but feel like it's partly my fault."
        mc "Look, let's sit down."
        mc "Before you continue talking, collect yourself first."
        mc "Our conversations always go strange places whenever you're flustered or confused."
        play music2 'audio/Sentient.mp3' fadein 3 loop
        play sound cloth
        scene ch1ep3_412
        with Dissolve(1.0)
        a "*takes a deep breath*"
        scene ch1ep3_413
        with dissolve
        a "What exactly is Freya to you? How did I miss all the signs?"
        mc "Aine, Freya has become someone special to me. It wasn't planned; it just... evolved over time."
        mc "Our bond grew as we worked together. We spent so much time side by side, understanding each other's quirks, ideas, dreams..."
        mc "As days turned into weeks, I began to see her in a new light and admired her spirit and determination."
        mc "I never imagined she'd feel the same about me."
        mc "Remember our trip to the beach island? That's when I first sensed something amiss."
        mc "In my ignorance, I, myself, missed the signs – her lingering glances, the way she seemed to pull away."
        mc "She kept so much bottled up. Never breathed a word about how she felt."
        mc "After we returned home, the distance only grew. Every attempt I made to approach her was dodged, and I didn't understand why."
        mc "It was as if an invisible wall stood between us. Until I realized... it was because of you."
        mc "Every moment of hesitation, every unspoken word: you were the underlying reason."
        mc "It all became clear. So, I confronted her. And the rest... well, you were there."
        scene ch1ep3_414
        with dissolve
        a "*sighs* There's so much that's been buried under the surface."
        a "I've always been painted as the privileged one, but it's a privilege I never asked for."
        a "Being mother's pawn was a double-edged sword."
        mc "But Freya feels like she's always been in your shadow."
        scene ch1ep3_415
        with dissolve
        a "And I wish she'd realize that it was my way of protecting her."
        a "Being under the radar gave her a freedom that I've never known."
        a "Every step I took, every decision I made... it's never just mine."
        a "There's always an ulterior motive, an expectation. Do you know how suffocating that feels?"
        mc "I can only imagine. But Freya just sees the attention and the affection, even if it's all a façade."
        a "And that's the irony. She envies what she perceives as my 'privileges' while I envy her freedom and ability to make her own choices, to pave her own path."
        mc "Why didn't you ever tell her this?"
        scene ch1ep3_413
        with dissolve
        a "I tried, in subtle ways. But admitting all this means acknowledging my vulnerabilities and my resentments against mother."
        a "I always thought Freya was better off not being a part of mother's plans. It was my way of looking out for her."
        mc "But do you think Hera genuinely cares for Freya?"
        scene ch1ep3_414
        with dissolve
        a "Hera has a convoluted way of showing love. But in her heart, I believe she does love Freya."
        a "Not involving Freya in her schemes might have been her twisted way of keeping Freya safe."
        a "Letting her have a life outside the web of politics and power."
        scene ch1ep3_415
        with dissolve
        yt "The gift Hera bought for Freya was a subtle gesture, yet it says so much."
        yt "But when did she purchase it, though? After Freya left her?"
        yt "Was it always meant to be seen as just a gift?"
        yt "If not, then... it's fucking painful to even think about it."
        yt "However, sympathy for Hera isn't what I should be focusing on right now."
        scene ch1ep3_417
        with dissolve
        mc "*chuckles* Are you always this good at figuring people out? Even Hera."
        a "Not really. It's just that she's my mother, and I know her very well."
        scene ch1ep3_413
        with dissolve
        mc "That makes sense. And... I'm really sorry about earlier. I didn't mean to spring all that on you."
        a "No, you were right. It's not just on you, [mc]. We're all entangled in this messy web."
        mc "Yeah, but I could've been more upfront and given you a heads-up or something."
        mc "Freya is still... well, your sister, after all."
        scene ch1ep3_414
        with dissolve
        a "Everyone has their reasons for keeping things under wraps. It doesn't make it easy, but I get it."
        mc "Life's weird like that. Just when you think you've got a grip, it throws you a curveball."
        a "Tell me about it."
        scene ch1ep3_415
        with dissolve
        mc "Look, I feel like you could use a breather after all this. I can head out and let you process things."
        a "Yes, that might be a good idea. Just... let's not let today's drama keep us on different pages, okay?"
        a "I wouldn't want that, especially since we should be helping each other at a time like this."
        a "I know I should be furious, but... it won't help us if I am."
        mc "Deal."
        play sound cloth
        scene ch1ep3_418
        with dissolve
        pause
        scene ch1ep3_419
        with dissolve
        pause
        scene ch1ep3_420
        with dissolve
        a "See you later, [mc]." #Aine gives a small smile
        mc "Remember, chin up!"
        a "Yeah..."
        play sound closedoor
        scene ch1ep3_421
        with dissolve
        pause
        if aineroute:
            scene ch1ep3_422
            with dissolve
            pause
            play sound chair
            scene ch1ep3_423
            with dissolve
            a "Why do I seem to be okay about all this?"
            a "That was not the conversation I wanted..."
            a "Why couldn't I say anything to him?"
            scene ch1ep3_424
            with dissolve
            a "... Is this the reason why it hurts so much?"
            a "Because you're... meant to be mine..."
        stop music2 fadeout 2
        
        scene black
        with dissolve
        with fade

        play music 'audio/LilacSnowINST.mp3'
        scene ch1ep3_440
        with dissolve
        f "Hm~?"
        scene ch1ep3_441
        with dissolve
        f "Hmmm~?"
        f "Looks good~! Looks good~!"
        scene ch1ep3_442
        with dissolve
        f "..."
        f "*sighs*"
        f "Alright, let's do this, Freya."
        play sound chair2
        scene ch1ep3_443
        with dissolve
        pause
        scene ch1ep3_444
        with dissolve
        f "Hey, everyone! Good evening, good evening! Thank you for joining the stream despite the short notice!"
        f "I'm sorry for this impromptu stream, but I needed to apologize for that sudden exit earlier."
        f "It's not like me to leave so suddenly, and I hope I didn't worry anyone too much."
        f "It might've looked like I just vanished, or something happened out of the blue. But I promise, I'm still here, and I'm more than okay!"
        play sound twitchbits
        scene ch1ep3_445
        with dissolve
        pause
        f "@Kainan, your words mean more than you know. And @Pezzo, seeing that kind of support... it's heartwarming. I really appreciate it."
        scene ch1ep3_446
        with dissolve
        f "..."
        scene ch1ep3_447
        with dissolve
        f "I know I should be more professional and not let personal matters affect the stream. But sometimes... it's hard, you know?"
        f "Earlier today, before I started streaming, I received some news."
        f "It's something personal that I'm still trying to come to terms with."
        f "I'm sorry, I can't share it with you guys, but that's the gist of it."
        play sound twitchbits
        scene ch1ep3_448
        with dissolve
        f "@Corky, \"Thought you got whisked away to a different dimension or something\"."
        f "Hah! If only. That might've been easier than facing this real-life stuff."
        play sound twitchbits
        f "And @KageAfJörmungandr, \"We got your back, Freya\"."
        f "Aww, thank you! Messages like that keep me going on tough days."
        f "Moments like this make me realize how important this community is to me. How you all have become an extended family that I can lean on."
        f "So... on a more reflective note, have you ever felt a sudden change in your emotions, just when you thought everything was going well?"
        f "It's annoying. One moment, you're on top of the world, and the next, you're grappling with something that feels so heavy."
        f "But, oh well... that's life, I guess."
        f "Sometimes, stuff just happens, and there's nothing you can do but to face it."
        f "And so, I have a question for you guys."
        f "If you ever had to make amends or apologize for something that truly weighed on your heart, how did you do it?"
        f "Words just don't feel enough to me. I feel like I should do something to show my sincerity."
        play sound twitchbits
        scene ch1ep3_449
        with dissolve
        f "..."
        scene ch1ep3_450
        with dissolve
        f "@Dwenn, yeah... I might be quite good at gaming, but I'm a noob regarding stuff like this."
        play sound twitchbits
        pause
        f "@Foxhound7231..."
        f "Yes, exactly. Everyone has their strengths and weaknesses."
        f "Your thoughts and experiences mean a lot to me. So, please share."
        f "And remember, no matter how light or deep, all comments are welcome here."
        play sound twitchbits
        scene ch1ep3_449
        with dissolve
        pause
        scene ch1ep3_450
        with dissolve
        f "@OEJ... In my perspective, what do I think is the best course of action?"
        f "Hmm, well..."
        scene ch1ep3_451
        with dissolve
        f "..."
        stop music fadeout 2

        call hide_days from _call_hide_days_5
        with dissolve
        scene black
        with dissolve
        with fade
        show screen day_tuesday with dissolve
        
        scene ch1ep3_452
        with dissolve
        pause
        scene ch1ep3_453
        with dissolve
        pause
        scene ch1ep3_454
        with dissolve
        pause
        scene ch1ep3_455
        with dissolve
        a "..."
        a "\"I'm sorry\"? That must be from Freya. How did she even reach that high up?"
        play sound step
        scene ch1ep3_456
        with dissolve
        a "..."
        scene ch1ep3_457
        with dissolve
        a "\"I'm sorry. Put a password on your PC, please\"."
        a "On my PC, too?!"
        scene ch1ep3_458
        with Dissolve(1.0)
        a "..."
        a "Are these... rose petals?! How did she manage all this?"

        scene black
        with dissolve
        with fade

        play music 'audio/Sincerity.mp3' fadein 2
        play sound closedoor
        scene ch1ep3_459
        with dissolve
        pause
        scene ch1ep3_460
        with dissolve
        pause
        scene ch1ep3_461
        with dissolve
        a "..."
        f "..."
        scene ch1ep3_462
        with dissolve
        pause
        scene ch1ep3_463
        with dissolve
        pause
        scene ch1ep3_464
        with dissolve
        pause
        scene ch1ep3_465
        with dissolve
        pause
        scene ch1ep3_466
        with dissolve
        pause
        scene ch1ep3_467
        with dissolve
        pause
        scene ch1ep3_468
        with dissolve
        pause
        scene ch1ep3_469
        with dissolve
        pause
        scene ch1ep3_470
        with dissolve
        f "*sobs* Sis... please, I can't stand this cold treatment. Please, say something... anything..."
        scene ch1ep3_471
        with Dissolve(0.3)
        a "Uhn..."
        scene ch1ep3_472
        with dissolve
        a "Come here."
        scene ch1ep3_473
        with dissolve
        f "*crying* I'm sorry~! I'm so sorry~!"
        show ch1ep3_474
        a "I saw what you tried to do. It's just..."
        scene ch1ep3_475
        with dissolve
        a "..."
        a "Let's find somewhere private to talk, okay?"
        f "Alright..."
        scene black
        with dissolve
        pause 0.5
        scene ch1ep3_476
        with dissolve
        a "I've seen your apologies, Frey. Well... everywhere. And I appreciate the effort."
        a "But it's not just about feeling sorry, because the words you said hurt me more than you know."
        a "So I need to understand. Why did you do what you did?"
        scene ch1ep3_477
        with dissolve
        f "*takes a deep breath* I did it because I felt I was always stuck on the sidelines."
        f "It's been building up for a while."
        f "Whenever you dismissed my thoughts or feelings, it felt like you were pushing me away."
        f "I felt lonely, sis. Even with you right beside me."
        f "Still, I managed to get myself this far even with that weight over my shoulders."
        f "Then, I found the person who accepted me for what I am. But it didn't make things easier for me."
        f "Because... You know what I mean..."
        a "Because I'm [mc]'s fiancée?"
        f "Yeah..."
        a "I never realized you felt that way..."
        scene ch1ep3_478
        with dissolve
        f "But I should've communicated better instead of acting out. I regret what I did, and I'm genuinely sorry."
        scene ch1ep3_479
        with dissolve
        a "I know you feel sorry for what happened, but don't blame yourself. It was my ignorance that caused our fight."
        a "Like you said, it was about me never standing up for you."
        a "I was never there when you needed me, and that is true. I'm not going to deny that."
        a "As siblings, there are a lot of opportunities we missed with each other. We could've done so much more together."
        a "Instead, all I was thinking was how I could escape from mother's shackles."
        scene ch1ep3_480
        with Dissolve(1.0)
        a "But now that we both have this precious freedom away from her, let's use this chance to build what we couldn't back then, okay?"
        f "*sniffs* Mhm, let's~!"
        a "Thank you for being brave enough to express your feelings. And I wish..."
        a "... I could be the same way."
        scene ch1ep3_481
        with dissolve
        f "What do you mean?"
        a "You are strong enough to be your own hero, Frey. I hope you realize that."
        scene ch1ep3_34
        with flash
        mc "The fact that you don't need a hero in your life."
        scene ch1ep3_35
        with dissolve
        mc "I'm quite jealous of that about you, and I'm sure I'm not the only one."
        scene ch1ep3_482
        with flash
        f "Ah..."
        scene ch1ep3_483
        with dissolve
        yt "*chuckles* I guess I don't need butt in. Now that she has realized it herself, there are no further words needed."
        yt "That's all I wanted for her."
        if (aineroute and freyaroute and emmaroute and moonroute and gwenroute and skyroute and gwenskyharem):
            $ allornothingroute = True
        else:
            stop music fadeout 2
            $ allornothingroute = False
            jump freyafirstarcend

    if allornothingroute:
        scene ch1ep3_484
        with dissolve
        a "..."
        stop music
        show ch1ep3_485
        a "Where do you think you're going?"
        play music 'audio/FlyingPillows.mp3'
        scene ch1ep3_486
        with Dissolve(0.2)
        mc "Uh-oh..."
        a "What do you mean \"Uh-oh\"? Get back here, [mc]! We're not done yet!"
        mc "Aine, I didn't mean to..."
        scene ch1ep3_487
        with dissolve
        a "You crossed the line both with me and my sister. How do I know you haven't done the same with the other girls?"
        a "Who else is involved in this, [mc]?"
        mc "I-it's not what you think..."
        play sound woodhit
        show ch1ep3_488
        with hpunch
        a "Call them down here!"
        mc "C-come again?"
        a "Call. Them. DOWN. HERE!"
        a "I want answers, and I want them now!"
        mc "Eek!"
        scene black
        with dissolve
        pause 0.8
        play sound smallbell
        show ch1ep3_489
        pause
        g "AHAHAHAHAAAAAA! Well hello, ladies!"
        scene ch1ep3_490
        with dissolve
        a "Oh... my... god..."
        a "So, all of you know about this, and yet you haven't mentioned anything to me?!"
        scene ch1ep3_491
        with dissolve
        e "Can we get this over with, please...? I still have to report to duty in an hour..."
        play sound woosh
        show ch1ep3_492
        with hpunch
        a "No! It's still six, and your shift starts at eight!"
        a "I can tell time without looking at it! So sit down, Emma!"
        e "O-okay..."
        e "I forgot about that strange ability of yours..."
        play sound chair
        scene ch1ep3_493
        with dissolve
        f "*whispers* Aine not calling you by your nickname means she's furious, right?"
        e "*whispers* I guess so?"
        f "*whispers* You're best friends, but you don't know that about her?!"
        scene ch1ep3_494
        with dissolve
        s "*whispers* I'd say you don't know your sister too well either, since you're asking that, Frey..."
        f "*whispers* Oh, shut up! I'm angry at you for not telling me that [mc] is doing this!"
        scene ch1ep3_495
        with dissolve
        s "*whispers* I guess you two did it, huh? So what about our bet?"
        f "*whispers* Well, still on, but..."
        s "*whispers* How about we change it to something waaaay more interesting~?"
        e "*whispers* What are you two talking about?"
        f "*whispers* Change it? Again?"
        s "*whispers* Yeah! Let's see who can make [mc] cum first!"
        scene ch1ep3_496
        with dissolve
        e "You want to make [mc] whaaat?!"
        play sound woodhit
        show ch1ep3_497
        with hpunch
        e "No! I will not tolerate this kind of behavior towards [mc]!"
        play sound woosh
        show ch1ep3_498
        g "Hmmnnnn? Is this self-defiance I'm hearing from you?"
        g "You know you want in on this, too, Em. Stop lying to yourself."
        play sound woosh
        show ch1ep3_499
        e "Huh?! Engaging in such unseemly, audacious, and utterly egregious behavior is beyond my comprehension! My very honor and repute hang in the balance!"
        g "This is the first time I've seen you flustered, which is surprising, but where the hell did that come from...?"
        scene ch1ep3_500
        with dissolve
        yt "Didn't know Emma could make that kind of expression..."
        yt "Looks like I'm seeing sides I've never seen from these girls before. But did Sky just say that?! What the hell, Sky?!"
        yt "And the fact that she nonchalantly said it with innocence in her eyes! What did Gwen do to her?!"
        yt "Well, I'm in the hot seat at the moment. I better stay quiet and wait for my cue."
        play sound woodhit
        show ch1ep3_501
        with hpunch
        a "LISTEN TO AINE!"
        g "Oh... you were saying?"
        scene ch1ep3_502
        with dissolve
        a "I... I don't get it! I was expecting others, but not the whole lot of you!"
        a "When on earth did this start?!"
        scene ch1ep3_503
        with dissolve
        g "Since high school. Basically stole him from you."
        scene ch1ep3_504
        with dissolve
        e "Since pre-school. I was the first to fall for him, I guess..."
        play sound woosh
        show ch1ep3_505
        s "Since the big bang~!"
        scene ch1ep3_506
        with dissolve
        f "Since..."
        f "When was it again?"
        play sound woosh
        show ch1ep3_507
        a "How about you?!"
        m "Hm? I don't have any idea why I'm even here."
        play sound woosh2
        show ch1ep3_508
        a "We are here because all of us somehow..."
        play sound woosh
        show ch1ep3_509
        a "Uhm... got laid..."
        play sound woodhit
        show ch1ep3_510
        with hpunch
        a "With this man!"
        show ch1ep3_511
        g "Heh, you actually know that word?"
        scene ch1ep3_512
        with dissolve
        m "Oh... and? I don't care at all."
        m "As long as I can stay beside him, that's all that matters to me."
        a "You two met only recently, right? How can you be attracted to a man you met just a few weeks ago?!"
        m "I don't know. I'm attracted to him by default. What's wrong with that?"
        m "What's even the point of this discussion? I don't find it necessary at all."
        scene ch1ep3_513
        with dissolve
        a "Well, the point is that this isn't right! This is not supposed to happen!"
        a "All of us are into the same man! Do you all not realize that?!"
        scene ch1ep3_514
        with dissolve
        g "You don't find that hot? What's wrong with you?"
        a "No, what is {b}wrong{/b} with {b}you{/b}?!" with hpunch
        show ch1ep3_515
        a "How about you, Sky? Don't just stay silent! You guys grew up together: what is your say in this?!"
        s "Uhm... well..."
        scene ch1ep3_516
        with dissolve
        a "Wait... you're... you..."
        s "Yeah..."
        s "It was hard initially, but we both accepted it one day."
        play sound woosh
        show ch1ep3_517
        a "Ohhh~!"
        play music 'audio/EventualBloom.mp3'
        play sound thud2
        show ch1ep3_518
        with hpunch
        f "Whoa! Sis?!"
        a "What is going on...? I can't see anything..."
        scene ch1ep3_519
        with dissolve
        a "Wait, I can see someone... Daddy, is that you?"
        mc "Hey, Aine! Snap out of it!"
        play sound glasscrack
        show ch1ep3_520
        a "*dead inside*"
        f "No, don't leave us..."
        scene ch1ep3_521
        with dissolve
        f "AINEEEEEEEE~!!"
        play music 'audio/FlyingPillows.mp3'
        play sound woosh
        show ch1ep3_522
        a "Huh!"
        a "That's enough!"
        f "We didn't do anything to you..."
        mc "I'll... I'll just return to my chair..."
        scene ch1ep3_523
        with dissolve
        g "Stop being so dramatic, will you? Just calm down!"
        g "Look, this started with my idea, okay?"
        g "[mc] initially had it going with Sky, Emma, and me. He then confessed it to me, and I initiated the plan and supported his actions."
        scene ch1ep3_524
        with dissolve
        a "But why?! Explain it to me because I don't understand why we should compete for his attention!"
        a "I mean... [mc]'s just one man!"
        g "There you go! You said the point."
        g "A competition is where it's at, babe! One girl sounds waaaay too boring for me."
        scene ch1ep3_525
        with dissolve
        e "If you don't like the idea, that's alright. You don't have to join in on this, Aine."
        e "However, Gwen and Sky are the main supporters of this... polygamy thing. I don't think there's anything that's going to stop them."
        show ch1ep3_526
        s "Nope!"
        g "Nah-uhh!"
        a "*sighs*"
        scene ch1ep3_527
        with dissolve
        e "I don't want to do this either. I waited for [mc] for almost two decades, and I want him all to myself."
        scene ch1ep3_528
        with dissolve
        e "But I don't want to lose to these... rapscallions..."
        play sound woodhit
        show ch1ep3_529
        with hpunch
        f "Hey, I know what that means! You take that back!"
        g "Oh, here we go!"
        show ch1ep3_530
        e "No."
        e "I met [mc] when I was six. Considering the pain I've endured to be with him again, he should rightfully be mine..."
        e "I'm the only one with a legitimate and realistic reason out of all you... rapscallions..."
        f "Stop saying that word! It's annoying me~!"
        e "No. I said what I said..."
        e "And I'll keep saying it..."
        scene ch1ep3_531
        with dissolve
        yt "Damn! Emma and her emotionless robotic voice can be absolutely savage!"
        yt "Hahaha! Boy, this is fun!"
        yt "I was nervous to have to face these girls all in one room, but this situation has some positives too."
        yt "Now I know why Gwen is so into this."
        scene ch1ep3_532
        with dissolve
        s "What do you mean, \"you're the only one with a legit reason\"?"
        s "Have you forgotten that I'm the one that's always been with [mc]? You guys can't hold a candle to me!"
        s "And don't forget what you did to him in high school! I was the one who had to wipe his tears and comfort his ass!"
        yt "You didn't have to include my ass there, Sky..."
        e "Be that as it may, I was the one who shared the first kiss with [mc], so he likes me more..."
        scene ch1ep3_533
        with dissolve
        s "No! Based on the way he was playing with my tits on the boat at the beach island, and the way I passionately sucked his meat stick, I'm pretty sure he likes me more!"
        s "What more could he ask from me~? Oooh... I wish he'd put a leash on me next time~!"
        yt "You want me to... whaaat?!"
        e "[mc] played with my... breasts too..."
        e "I felt awkward, but... it feels nice, yes..."
        g "He tasted mine, twice. The first time was for breakfast, and I'm sure that was the best breakfast he ever had."
        play sound woosh
        show ch1ep3_534
        s "You broke my heart because of that!"
        scene ch1ep3_535
        with dissolve
        f "He played with mine back during our vacation as well..."
        s "I knew it! I had a feeling you guys did something after I left!"
        scene ch1ep3_536
        with dissolve
        m "Uhm... I sucked his balls. Does that count?"
        s "Whaaaaaaaaaat?!"
        g "Wait, when did this happen?!"
        scene ch1ep3_537
        with dissolve
        yt "Is that all you guys have to say about me...?"
        stop music fadeout 4
        scene ch1ep3_538
        with dissolve
        a "..."
        yt "What are you going to do, Aine? Will you choose defeat? Or are you going to fight back?"
        yt "Only three people in this room know you're not a shy, innocent mafia princess. And those people are you, Emma... and me."
        yt "Come on! Let me see that side again! The one you've been suppressing for too goddamn long!"
        play music 'audio/MissingArchetecture.mp3'
        scene ch1ep3_539
        with dissolve
        a "*chuckles* Pathetic. I've been standing here, wasting my precious time, listening to you all bicker like children over nothing."
        a "Do you honestly believe that some fleeting, {i}insignificant{/i} moments can define what [mc] and I share?"
        s "I-insignificant moments?!"
        scene ch1ep3_540
        with dissolve
        a "Sky. Always acting the martyr, the eternal sobbing pillow."
        a "Ever thought, just for once, that maybe [mc] needs someone more than a sad, clingy babysitter?"
        a "Where were your brave stances when he was mine to command? Did you even dare to intervene?"
        a "Of course not. Typical. So shut it."
        scene ch1ep3_541
        with dissolve
        pause
        yt "And... there she is. A side of you even the depths of hell would be scared to entertain."
        scene ch1ep3_542
        with dissolve
        a "Gwen, introducing a petty game to lure him in? Truly desperate."
        a "What if [mc] is seeking genuine feelings? Not your cheap theatrics? Did his wishes even cross your mind?"
        a "For someone who claims to be \"mature\", you're quite the laughable fool."
        scene ch1ep3_543
        with dissolve
        a "Emma, memories might be golden, but they also fade."
        a "Grasping them won't ensure he stays with you."
        a "Ever thought if [mc] still remembers the \"Emma\" from before? Or if he's tired of her now?"
        a "Ponder on that, if you can."
        yt "Even your closest friend isn't safe from your venom, huh, Aine?"
        scene ch1ep3_544
        with dissolve
        a "Ah, the newbie."
        a "Your shallow attraction to [mc], is it anything more than a passing fancy?"
        a "Such shallow feelings are easily swept away, like dust in the wind."
        scene ch1ep3_545
        with dissolve
        pause
        play sound cloth2
        show ch1ep3_546
        mc "*softly speaking* Don't. Not right now."
        mc "*softly speaking* Aine isn't a perfect human being. She knows she's not in the position to talk like that, but let her control the situation."
        m "..."
        scene ch1ep3_547
        with dissolve
        m "If you say so."
        scene ch1ep3_548
        with dissolve
        a "And if you all need evidence of my superiority?"
        scene ch1ep3_549
        with dissolve
        a "Here."
        a "This gift, from him to me, is more than any of you will ever have."
        a "Even if it's just a formality, it holds weight and meaning."
        a "While you're all lost in your delusions, remember..."
        a "No matter how much you wish, dream, or hope..."
        a "Whatever happened in the past years, months, weeks, or days..."
        a "{b}I am{/b} the queen here. {b}I am{/b} his chosen."
        a "So, you want a battle?"
        a "Bring it on. I relish a challenge."
        a "I was born to conquer, to dominate. And rest assured..."
        a "Defeat isn't in my dictionary."
        a "If this is what you desire..."
        a "Step up. Give it everything. Because facing me will be your worst nightmare."
        stop music fadeout 4
        scene ch1ep3_550
        with dissolve
        pause
        scene ch1ep3_551
        with dissolve
        yt "This is her. This is Aine Agnor."
        yt "No one can utter a single word... Not even Gwen herself."
        yt "But boy... She does know how and when to flip her switches."
        yt "While I'm impressed with her dominance over the other girls, I can't let this silence linger any longer."
        play sound cloth
        play music 'audio/NightingalesJourney.mp3'
        scene ch1ep3_552
        with dissolve
        mc "Ahem. I should've spoken much earlier. But everyone, please, take a moment and listen to me."
        scene ch1ep3_553
        with dissolve
        mc "I... never anticipated things would escalate to this point."
        mc "Let me be honest. This didn't start with Gwen's idea. This started with me."
        mc "It took me great courage to tell Emma and Gwen about the situation. In the end, they both accepted it."
        mc "But Gwen didn't settle for less, and she thought of an idea. An idea of me dating multiple girls all at once."
        mc "Don't get me wrong: part of me thought it was a bad idea. But another part of me thought it might be fun to feel loved and cared for by multiple lovely young ladies."
        mc "But as days went by, I began to see and cherish the bond I shared with each and every one of you."
        scene ch1ep3_554
        with dissolve
        mc "Sky... The way you've always stood by me, always been so protective and caring, means the world to me. I don't know where I'd be right now without you."
        scene ch1ep3_555
        with dissolve
        mc "Em, you were the first to make my heart skip a beat."
        mc "My bond with you that started during our childhood is something I will hold dear every single day."
        scene ch1ep3_556
        with dissolve
        mc "Moon, our recent encounter has shown me a different kind of love and affection. I'm happy that we found each other."
        mc "I don't know what this feeling is that ties us together so much, but I will never question it, and I'm happy to accept it."
        scene ch1ep3_557
        with dissolve
        mc "Frey... you already know, right?"
        f "Mhm~! No need for further explanation, [mc]."
        mc "Good. That's my Freya."
        scene ch1ep3_558
        with dissolve
        f "*giggles*"
        scene ch1ep3_559
        with dissolve
        mc "And Aine, what you said was right. The commitment we share is real. I will never consider it in any other way."
        scene ch1ep3_560
        with dissolve
        mc "What I'm trying to say is that all of you are equally important to me. I genuinely care about every one of you."
        mc "I don't see this as a true competition, and it pains me to see you fight over... well, me."
        scene ch1ep3_561
        with dissolve
        a "*sighs* But how does this work? Are you telling us to... just share you? Is that it?"
        a "If so, how can you expect us not to fight over your attention?"
        scene ch1ep3_562
        with dissolve
        g "Okay, let me clarify this to all of you."
        g "While I love the idea of a competition, like what happened between Aine and Freya yesterday, I don't want any real fights to happen between us girls."
        scene ch1ep3_563
        with dissolve
        g "I will fight for that ring to be on my finger, but I will not physically hurt somebody just because I want it so badly."
        g "So no matter what Aine says, I will stand by my principles."
        scene ch1ep3_564
        with dissolve
        s "You sisters fought?! What happened?!"
        f "Well... it's complicated, and I don't want to explain it again."
        play sound woosh
        stop music fadeout 2
        play music2 'audio/FlyingPillows.mp3' loop
        show ch1ep3_565
        a "So, a friendly competition is what you're suggesting."
        a "Fine by me!"
        g "God, I'd love to have a slap at that face."
        g "Makes me remember that your feistiness is the thing I hate the most about you."
        a "So what? You wanna go, Buttermilk?"
        g "Are you trying to insult my hair color?"
        a "Glad to know you're quick on the uptake, Sun-bleached."
        play sound fistbump
        show ch1ep3_566
        with hpunch
        g "Just so you know, I'm already [mc]'s girlfriend. Do something about it, babe."
        a "Just so you know, I'm [mc]'s fiancée, do something about it... {i}babe{/i}!"
        g "Virgin princess!"
        a "High school whore!"
        scene ch1ep3_567
        with dissolve
        yt "*sighs* I guess I can't stop this competition thing..."
        yt "Well, as long as they don't hurt each other, it'll be fine."
        scene ch1ep3_568
        with dissolve
        mc "..."
        scene ch1ep3_569
        with dissolve
        yt "Man, this is unreal. All of them... actually competing for me?"
        yt "Who died and made me king?"
        scene ch1ep3_570
        with dissolve
        yt "Still... Aine's fire is something else."
        yt "Seeing her all riled up just for me is insane."
        scene ch1ep3_571
        with dissolve
        yt "And Gwen... will always be my queen. Full of life, full of surprises."
        yt "Just when I think I've figured her out, she flips the script again."
        yt "She gave up everything to be part of this—how could I not respect that?"
        scene ch1ep3_572
        with dissolve
        yt "..."
        yt "God... the look on their faces..."
        scene ch1ep3_573
        with dissolve
        yt "Emma and I go way back. So many memories."
        yt "Seeing her open up like this is like watching someone you love finally step into the light."
        yt "*chuckles* That's it, Em. You belong here. Let them see who you really are."
        scene ch1ep3_574
        with dissolve
        yt "And then there's Sky..."
        yt "She's always been my anchor. The one person I could count on when everything else fell apart."
        yt "Now she's out there, standing her ground—fighting for what she wants. So... her."
        scene ch1ep3_575
        with dissolve
        yt "Freya—the sharp one. The one who always seems five steps ahead."
        yt "She sees the world differently. And now? Now she's laying it all out there like she's been saving it for the perfect moment."
        yt "*chuckles* Guess this was the moment she was waiting for."
        scene ch1ep3_576
        with dissolve
        yt "And then..."
        yt "There's this one girl."
        yt "We haven't known each other long, but there's something about her... something strange. Like a thread pulling us together."
        yt "When she's not around, something in me feels... off. Like I'm missing a part I didn't know I had."
        yt "I'm not talking about love or attraction. It's deeper than that. Like... an odd connection. I wonder if she can feel it too."
        yt "Even after learning about her past... it only left me with more questions."
        yt "Moon... who are you, really?"
        scene ch1ep3_577
        with dissolve
        m "Hm? Yes, Commander?"
        mc "I-it's nothing."
        scene ch1ep3_569
        with dissolve
        mc "..."
        yt "I still can't believe they're all doing this—for me."
        yt "It's overwhelming. Honestly? I'm flattered. But it's... a lot."
        yt "What I *do* know is that each of them holds a place in my heart."
        yt "Never thought I'd find myself in a moment like this."
        yt "Life really doesn't stop throwing curveballs, huh?"
        scene ch1ep3_578
        with dissolve
        a "Say what you want, but someone has to dictate the rules of this... whatever you call it!"
        scene ch1ep3_579
        with dissolve
        g "Oh, now that you mention it... yeah, I agree. But who?"
        play sound woosh
        show ch1ep3_580
        s "I vote for Gwen! She's the one who initiated everything, anyway. I believe she's a capable leader, considering her previous job!"
        s "And she's a good singer!"
        g "Stop simping for my voice, Sky."
        scene ch1ep3_581
        with dissolve
        m "... I second Sky's opinion. Seeing Gwen stop Aine and Freya's fight yesterday proves she can handle things when they get out of hand."
        m "I think she's the one."
        scene ch1ep3_582
        with dissolve
        mc "You should include yourself too, you know?"
        scene ch1ep3_583
        with dissolve
        m "It's true that I was forged in the fires of war, molded to take command, to lead legions into the chaos of battle."
        m "But each order I gave, every directive I issued, was a whisper in the reaper's ear, beckoning him closer to those under my command."
        m "The weight of their lives, the chorus of their final cries, haunts me to this very day."
        scene ch1ep3_584
        with dissolve
        m "I refuse to be the puppet master of death any longer, to string along souls to their untimely end."
        mc "Uhm... what? Where did you get that from?"
        scene ch1ep3_577
        with dissolve
        m "From a short recital I prepared for my homework."
        mc "Aren't you taking your homework too seriously?"
        m "Shu helped me make it."
        mc "... I should've guessed."
        scene ch1ep3_585
        with dissolve
        f "Legions?! Forged?! Puppet master of death?! That's freakin' cool!"
        f "You know, I should vote for y-{w=0.9}{nw}"
        m "I'm also the one who will break your neck if you vote for me, Freya."
        f "Okay, that's a no, then."
        m "Yes, keep it that way."
        scene ch1ep3_586
        with dissolve
        e "I vote for me..."
        e "I stand by what I said earlier. I want to make it so I can have [mc] all for myself..."
        scene ch1ep3_587
        with dissolve
        m "I'm afraid I cannot allow that. If that happens, I must kill you first, childhood friend."
        scene ch1ep3_588
        with dissolve
        e "... Do you want to do this again, cannon fodder?"
        scene ch1ep3_589
        with dissolve
        m "Come at me. I will not hold back this time, kid crush."
        play sound woosh
        show ch1ep3_590
        g "Fifty bucks on Emma."
        f "Eighty bucks on Moon!"
        scene ch1ep3_591
        with dissolve
        a "That's enough, both of you! You heard what Gwen said, right?"
        scene ch1ep3_592
        with dissolve
        a "Stop breaking the rule you made yourself!"
        g "Haha! Yeah, sorry, sorry. I couldn't help it."
        scene ch1ep3_593
        with dissolve
        mc "Let's keep it calm, everyone. This won't end if you guys fight on every single topic, you know?"
        scene ch1ep3_594
        with dissolve
        mc "Gwen, what do you think?"
        g "What do I think? Well, I can definitely keep these motherchuckers at bay, and, indeed, I was once a leader. But..."
        g "... What we need is more than just a leader to keep these nut cases in their place."
        scene ch1ep3_595
        with dissolve
        g "What we need is a tyrant, a ruler, a dictator. The one who can suppress anybody no matter who they are."
        g "Everyone here is a witness, so everyone knows who it is."
        scene ch1ep3_596
        with dissolve
        mc "*chuckles*"
        scene ch1ep3_597
        with dissolve
        e "If it's going to be her, then I will not oppose it."
        scene ch1ep3_598
        with dissolve
        s "Yeah, there can only be one!"
        scene ch1ep3_599
        with dissolve
        g "She may not look like it, and she doesn't tend to show it. She doesn't believe it, either."
        g "But that's who you are no matter how you try to hide your true personality."
        play sound bodyhit
        show ch1ep3_600
        with hpunch
        a "Wha..."
        scene ch1ep3_601
        with dissolve
        g "*clears her throat*"
        scene ch1ep3_602
        with dissolve
        g "Aine Agnor, I hereby declare you as the Ruler of this harem!"
        g "With this title, you are vested with the power to reign, the authority to decide, and the command to lead!"
        scene ch1ep3_603
        with dissolve
        g "In our chaotic realm, where many voices clamor and few are heard, you stand above all as the singular, decisive force!"
        a "A-are you sure you want to give this to me? We both know you're the best suited for this kind of role."
        g "True leadership is not always sought. Sometimes, it is thrust upon those who are worthy, whether they desire it or not."
        g "It's not about what you want, Aine, but what we need. And we need you."
        scene ch1ep3_604
        with dissolve
        mc "Hear, hear!"
        scene ch1ep3_605
        with dissolve
        e "Your oppressive side has always been your silent strength, Aine. It's been evident to those who have witnessed it."
        e "Just that you weren't given the right purpose for it, which is a shame."
        e "[mc], Gwen, me, and everyone here today saw how you closed our mouths, so... I guess you still got it?"
        scene ch1ep3_606
        with dissolve
        a "But... aren't you angry about anything I said?"
        s "*giggles* We are not angry. Just hold back on the words next time. I'm still your boss, you know?"
        e "Mhm."
        a "Sorry..."
        s "Now, the crown rests upon the rightful head. As it should be, Your Majesty."
        a "I...I'm overwhelmed. I know I wanted this from the start, but now... I don't know what to say."
        scene ch1ep3_607
        with dissolve
        a "But I guess... for all of you, I will strive to be the leader you believe I am."
        a "And I'm sorry for dragging all of you down here. I'll make it up to you guys."
label freyafirstarcend:
    stop music2 fadeout 2
    call hide_days from _call_hide_days_6
    scene black
    with dissolve
    with fade
    show screen day_tuesday with dissolve

    $ renpy.music.set_volume(0.5, 1.0)
    play music 'audio/CryForHelp.mp3'
    play sound firewood loop
    scene ch1ep3_425
    with dissolve
    pause
    scene ch1ep3_426
    with dissolve
    un "Ah, you've finally graced me with your presence. Have you completed the simple task I gave you?"
    fr "..."
    scene ch1ep3_427
    with dissolve
    fr "I haven't yet, but-"
    un "Ah, \"but\"; the same word your weak-willed sister was so fond of using."
    un "I detest that word, Francis. All I asked was for you to locate and bring Aine to me. A task apparently too monumental for you."
    scene ch1ep3_428
    with dissolve
    fr "I'm not entirely convinced that she's at the reported location, Father."
    un "Are you trying to question my power?"
    fr "No, father..."
    un "Did I raise a son who can't even ascertain a simple fact?"
    fr "No... father..."
    un "You are trying my patience, Francis."
    un "Do you want your sister back? Or would you prefer dawdling?"
    un "If you can't manage this simple task, tell me now. I have no qualms about handling it myself."
    scene ch1ep3_429
    with dissolve
    fr "No! Just..."
    fr "Just give me a bit more time! I have a strategy in mind and won't disappoint you!"
    un "... This is your final chance. And remember, I have no use for failures."
    scene ch1ep3_430
    with dissolve
    fr "..."
    un "Repeat it back, so I know it's sunk in."
    scene ch1ep3_431
    with dissolve
    fr "You dispose of useless people, just like you did with my sister..."
    un "Precisely. Keep that in mind, lest you wish to be erased from this lineage."
    scene ch1ep3_432
    with dissolve
    fr "{i}Tsk!"
    scene ch1ep3_433
    with dissolve
    fr "One question, which is what I came here for."
    un "What is it?"
    fr "What's the endgame once I find her? You've slated us for marriage, but to what end?"
    un "Always with the curiosity, I see."
    un "The motive? Merely to elevate our family's legacy. That's all you need to concern yourself with."
    fr "..."
    fr "Ensure you keep your end of the bargain. Return my sister to me."
    un "She will be returned if, and only if, you deliver on your part."
    scene ch1ep3_434
    with dissolve
    un "Time is of the essence, Francis. Do whatever it takes. Use force if necessary."
    un "Achieve this for Olivia's sake."
    scene ch1ep3_435
    with dissolve
    fr "Understood..."
    scene ch1ep3_436
    with Dissolve(2.0)
    un "..."
    scene ch1ep3_437
    with dissolve
    un "That boy..."
    un "Be careful of him."
    fr "You know him? Who is he?"
    un "Someone who's in debt to me. Or rather... the person who took him was."
    un "Take him out first, then getting Aine should be easy enough for you."
    un "You can do it, right?"
    fr "O-of course."
    un "Then you should take your leave. You are only wasting time."
    scene ch1ep3_438
    with dissolve
    fr "{i}Every moment I was there, I was humiliated..."
    fr "{i}I will set things right this time."
    fr "{i}Just hold on a little longer, Vi."
    scene ch1ep3_439
    with Dissolve(2.0)
    un "*chuckles* Looks like your plan is just as blinded as you are, Hera."
    un "Perhaps I should thank you for making my world smaller."
    $ renpy.music.set_volume(1.0, 2.0)
    play sound cinematicimpact
    stop music fadeout 4
    scene black
    pause
    call hide_days from _call_hide_days_7
    show ch1ep3end
    with dissolve
    pause 157.5
    scene black
    with dissolve
    pause

    jump ep3part2
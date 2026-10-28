label Episode_1_Start:

    #KoGa3 START#
    $ KoGa3GameProgress = "Ep1"
    #KoGa3 END#

    $ Alexis_Friends = False
    $ Alexis_Sex = False
    $ Alexis_Intro_Ignore = False
    $ Alexis_Intro_Join = False
    $ Rachel_Intro_CheckOut = False
    $ Rachel_Intro_BJ = False
    $ Rachel_End = False
    $ Melissa_Intro_Hug = False
    $ Melissa_Intro_Sunbath = False
    $ MC_Week1_Monday_Skip = False

    jump Intro_Aeroplane

label Intro_Aeroplane:
    play sound "Sounds/Aeroplane_Beep.wav" volume 0.3
    play music "Sounds/Aeroplane_Onboard.mp3" volume 0.5
    pi "Ladies and gentlemen, good morning."
    scene 01_001 with Dissolve(1)
    pi "Skye Airlines would like to welcome you on board this Boeing 737, bound for Madison Springs."
    pi "The flight time today will be six hours and twenty minutes."
    scene 01_002 with Dissolve(1)
    mc "{i}(*Sigh* Six long hours...){/i}"
    pi "We would like to draw your attention to the fact that this is a non-smoking flight. Smoking is prohibited throughout the entire aircraft, including in the lavatories."
    pi "Due to our imminent take-off, we kindly ask you to fasten your seatbelt, return your seat to its upright position, and stow the table in front of you."
    pi "We also ask that you switch off all electronic devices and open the window blinds. Please pay attention in a few moments for the safety briefing."
    pi "On behalf of the entire crew, we wish you a pleasant flight."
    scene 01_003 with Dissolve(1)
    n "I never liked flying."
    n "The cramped spaces, never enough room to stretch your legs."
    n "Not knowing who's going to sit next to you..."
    n "I can't read a book or play on my phone either to kill time. Always get a headache from it. Really annoying."
    n "So basically, the only option is to close my eyes and try to get some sleep. Mostly without success, though."
    scene black with Dissolve(2)
    pause 2
    scene 01_004 with Dissolve(1)
    x "..."
    scene 01_005 with Dissolve(1)
    x "Uhm... Excuse me?"
    mc "{i}(*Sigh* Really?){/i}"
    mc "{i}(Of course... Someone had to sit next to me. Can't I be lucky just once and have a row to myself?){/i}"
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 01_006 at moveup
    pause 3
    x "Hi."
    mc "{i}(Oh...){/i}"
    scene 01_007 with Dissolve(1)
    x "I'm so sorry I had to wake you, but I've got the seat next to you..."
    menu:
        "Let her pass[KoGa3AutoWTChange1]{size=-4}(Alexis Points+2) {/size} {/color}":
            $ Alexis_Points += 2
            # Alexis (2)
            jump Intro_Flashback_Alexis
        "Ignore her[KoGa3AutoWTChange1]{size=-4}(Alexis Intro Ignore, Alexis Friends) {/size} {/color}":
            $ Alexis_Intro_Ignore = True
            $ Alexis_Friends = True
            scene 01_008 with Dissolve(1)
            mc "{i}(I can't be bothered. It's way too early for this.){/i}"
            x "..."
            x "Seriously? You're not even going to move a little?"
            scene 01_010 with Dissolve(1)
            x "{i}(Pretending to sleep again... Unbelievable!){/i}"
            scene 01_011 with Dissolve(1)
            x "{i}(Great. Now he's staring at my butt. Can this get any worse?){/i}"
            x "{i}(Fucking creep!){/i}"
            scene 01_012 with Dissolve(1)
            mc "{i}(Hmm... Not bad actually. Reminds me of someone.){/i}"
            scene 01_013 with Dissolve(1)
            x "Asshole!"
            mc "{i}(Whatever... As if I'm ever seeing you again...){/i}"
            scene 01_014 with Dissolve(1)
            ""
            scene black with Dissolve(2)
            pause 2
            scene 01_015 with vpunch
            pause 2
            scene 01_015 with vpunch
            play sound "Sounds/Aeroplane_Beep.wav" volume 0.3
            pi "Ladies and gentlemen, the captain has turned on the fasten seatbelt sign. We are now crossing a zone of turbulence."
            pi "Please return to your seats and keep your seatbelts fastened. Thank you."
            scene 01_015 with vpunch
            pi "Cabin crew, please be seated."
            scene 01_016 with Dissolve(1)
            mc "{i}(Turbulence, huh?){/i}"
            mc "{i}(As if my life hasn't been turbulent enough these past few years.){/i}"
            scene black with Dissolve(2)
            jump Intro_Flashback

label Intro_Flashback_Alexis:
    scene 01_009 with Dissolve(1)
    mc "{i}(She sounds a little nervous... Maybe she doesn't like flying either?){/i}"
    mc "{i}(Great. Now I feel bad for being annoyed.){/i}"
    mc "Oh, yeah... Sorry about that. Give me a second."
    scene 01_017 with Dissolve(1)
    x "No worries. I need to put my stuff in the overhead bin first anyway."
    scene 01_018 with Dissolve(1)
    mc "Need a hand with that?"
    x "I've got it, thanks."
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 01_019 at moveup
    pause 3
    mc "{i}(Hmm... Have I met her somewhere? Feels like I've seen her before.){/i}"
    scene 01_020 with Dissolve(1)
    x "All done..."
    mc "Well, go ahead."
    x "Thank you!"
    scene 01_021 with Dissolve(1)
    mc "{i}(She's kinda cute. This could've been much worse.){/i}"
    mc "{i}(Should I talk to her? Might make this flight a little more bearable.){/i}"
    mc "{i}(Then again... Maybe she's one of those people glued to their phone the whole time. Boring!){/i}"
    mc "..."
    mc "{i}(But seriously... Where have I seen her before? Maybe she just reminds me of someone?){/i}"
    scene 01_022 with Dissolve(1)
    mc "{i}(This is gonna bug me the whole flight! Why am I so bad at remembering faces?){/i}"
    mc "{i}(*Sigh*){/i}"
    mc "{i}(Oh well... Might as well try to sleep again. Can't wait to finally get there.){/i}"
    scene 01_023 with Dissolve(1)
    x "Uh, do you..."
    x "Oh..."
    scene 01_024 with Dissolve(1)
    x "{i}(He's sleeping again?){/i}"
    x "{i}(Hmm... He's cute!){/i}"
    x "{i}(*Sigh* Too bad. Would've liked someone to talk to.){/i}"
    scene black with Dissolve(2)
    pause 2
    scene 01_025 with vpunch
    x "Aaah!"
    scene 01_025 with vpunch
    mc "{i}(Huh?){/i}"
    mc "{i}(What's going on? Turbulence?){/i}"
    scene 01_026 with Dissolve(1)
    x "Uhm..."
    mc "Hey, don't worry. It's just some turbulence. It will pass soon."
    play sound "Sounds/Aeroplane_Beep.wav" volume 0.3
    pi "Ladies and gentlemen, the captain has turned on the fasten seatbelt sign. We are now crossing a zone of turbulence."
    pi "Please return to your seats and keep your seatbelts fastened. Thank you."
    scene 01_026 with vpunch
    pi "Cabin crew, please be seated."
    scene black with Dissolve(2)
    pause 2
    scene 01_026 with Dissolve(1)
    mc "See... And we're through it already."
    scene 01_027 with Dissolve(1)
    x "Thanks! And sorry for grabbing onto you like that."
    mc "It's fine."
    x "It's just... I don't like flying to begin with. Then the turbulence... It... It really freaks me out."
    mc "I get it. I don't like it either. Having no control over the situation feels so weird."
    x "Right?"
    x "..."
    scene 01_028 with Dissolve(1)
    x "Uhm... Do you mind if we keep talking? It helps me keep my mind off being on a plane."
    x "It's fine if you don't. You can just go back to sleep. I..."
    mc "I don't mind at all. To be honest, I can't sleep anyway. I try every time, but no dice."
    x "Thanks. I have the same problem. I can never get comfortable on a plane."
    scene 01_029 with Dissolve(1)
    a "Oh... I'm Alexis, by the way."
    mc "I'm [mc]. Nice to meet you, Alexis."
    a "You too, [mc]."
    scene 01_030 with Dissolve(1)
    mc "So... Where are you headed? Going on vacation or back home?"
    mc "Maybe business... Or..."
    mc "Pleasure?"
    scene 01_031 with Dissolve(1)
    a "Hah! My vacation was very... pleasant! Sadly, I'm heading back home."
    mc "Where's home?"
    a "Madison Springs..."
    mc "Madison Springs isn't so bad. Especially the beaches..."
    a "Yeah, don't get me wrong. I like living there. Actually, I love it! But what I'm not looking forward to is being back at college and work on Monday."
    mc "Oh... You're a teacher?"
    scene 01_032 with Dissolve(1)
    a "No-no... I'm a student, sophomore. I work part-time as a bartender."
    a "Maybe I should've phrased that better..."
    scene 01_033 with Dissolve(1)
    mc "Cool! What are you majoring in?"
    a "Communications."
    mc "Communications, huh?"
    a "What?"
    mc "So, about that phrasing earlier..."
    scene 01_034 with Dissolve(1)
    a "Oh, shut up! Haha..."
    a "Just for the record, I'm a straight-A student, alright."
    mc "Sure... And the Earth is flat."
    a "Hey now! Haha."
    mc "Haha."
    a "Okay, Einstein... What about you? Where are you headed? Business? Pleasure...?"
    scene 01_035 with Dissolve(1)
    mc "Hmm... Neither."
    mc "Same as you. Home, I guess?"
    a "You guess?"
    mc "Well... It's a long story."
    a "If only we were on a six-hour flight with nowhere to go."
    mc "Touché!"
    scene 01_036 with Dissolve(1)
    mc "I hope I won't bore you to death."
    a "Hey! I'd rather listen to anything than spend six hours staring out the window of a plane. So, try me!"
    mc "Wow... Thank you. It's such an honour sitting next to you."
    a "Haha. Right?"
    scene 01_127 with Dissolve(1)
    mc "Everything started out pretty normal..."
    mc "Caring parents, lots of friends, a good childhood altogether."
    scene 01_128 with Dissolve(1)
    mc "That changed very quickly though, once Dad decided to leave and divorce Mom. Or did Mom divorce Dad? Hmm..."
    mc "Anyway, it happened out of nowhere. I had no idea what was going on."
    scene 01_129 with Dissolve(1)
    mc "Mom, especially, had a really hard time."
    mc "She couldn't cope with it whatsoever and was a total mess afterward."
    mc "Countless nights of drinking and crying..."
    mc "I didn't know what to do. And honestly, I wasn't the easiest kid to take care of either."
    scene 01_130 with Dissolve(1)
    mc "Luckily, she often got help from Melissa, her best friend since forever and our next-door neighbour."
    mc "Melissa always knew what to do and say to lift Mom's spirits."
    mc "She came by almost every day with her daughter, Erynn."
    scene 01_131 with Dissolve(1)
    mc "Ever since I can remember, Erynn and I were inseparable."
    mc "Always playing and chasing each other around, even though she's three years older than me."
    scene 01_132 with Dissolve(1)
    mc "As we grew older, our interests started to drift apart."
    mc "I still liked playing with her..."
    mc "But Erynn began hanging out more with her school friends."
    mc "She was really popular and got a lot of attention from other boys."
    mc "Especially that idiot Ethan, who stuck to her like glue and even gave her bike rides to school."
    mc "I wasn't happy about it at all. I grew more jealous every day."
    scene 01_133 with Dissolve(1)
    mc "I was about eleven or twelve when I came up with, in my opinion, the only way to spend more time with Erynn again."
    mc "Confessing..."
    mc "Telling her I liked her."
    scene 01_037 with Dissolve(1)
    a "How did you confess?"
    mc "I gave her a flower and basically just said that I liked her..."
    a "Oh... You gave her flowers? That's cute..."
    mc "Not flowers! A single flower!"
    mc "One... Which I took from a vase in the kitchen."
    scene 01_038 with Dissolve(1)
    a "Flower, flowers... It's the gesture that matters."
    a "No one's ever given me flowers. I think it's cute. And charming."
    a "But continue."
    scene 01_134 with Dissolve(1)
    mc "I still remember the laughter like it happened yesterday."
    mc "She took it as a joke..."
    mc "Or rather, she made me the joke. Even her friends were laughing at me."
    mc "I hated her for it."
    mc "... And my jealousy slowly turned into anger."
    scene 01_135 with Dissolve(1)
    mc "It didn't stop there."
    mc "That anger didn't just stay bottled up. It started affecting everything. My grades dropped, my attitude at school and home got worse."
    mc "Mom kept getting calls from teachers, one complaint after another. Detention became part of my daily routine."
    mc "And honestly? I couldn't have cared less."
    mc "After a few weeks of dealing with me, Mom finally had enough, and she sent me to stay with Dad during spring break."
    mc "That one week turned into years. Honestly, I've lost track of how long it's been now."
    scene 01_039 with Dissolve(1)
    mc "When my dad decided to remarry, we moved in with his fiancée and her two kids. The house got really crowded. Stuff happened and... Yeah..."
    mc "So, I decided to move back to Mom's place and finish my last year of school there."
    scene 01_040 with Dissolve(1)
    a "Your mom must be really happy that you're coming back."
    mc "I hope so. I haven't seen her for a while."
    a "How come?"
    mc "I was so angry that she sent me away. I didn’t even get to hang out with my friends during spring break."
    mc "But that changed pretty quickly once I made new friends in Alvarado."
    scene 01_041 with Dissolve(1)
    mc "In fact, I liked it there so much that I didn't want to go back."
    mc "My dad told my mom it might be better if I stayed longer and finished the school year in Alvarado."
    mc "Mom wanted to visit me so many times. But every time, I pretended I was still angry. That I didn’t want to see her. I used her as my scapegoat."
    mc "And I kept it up, even after the school year ended, because deep down... I just didn’t want to go back to Madison Springs."
    scene 01_042 with Dissolve(1)
    mc "We only talked a few times over the phone, and my dad sent her pictures now and then. But that was it. Not exactly 'Son of the Year' behaviour."
    a "That doesn't matter now. Trust me... She's your mom! I'm sure she'll be over the moon to have you back."
    mc "Hmm..."
    a "But what about the girl... Erynn? What happened with her?"
    scene 01_039 with Dissolve(1)
    mc "I don't know, to be honest."
    mc "Things were already strained after the so-called confession."
    mc "When I moved away, we lost all contact. I haven't spoken to her since..."
    mc "She wrote me a few letters in the first couple of months, but I never read them. Just tore them up and threw them away."
    mc "I regret that now... but back then, I didn’t want to hear from her."
    scene 01_042 with Dissolve(1)
    a "That reunion's going to be... interesting, to say the least."
    mc "If it ever happens."
    a "You don't want to see her?"
    mc "I do. I think I do... I'm just not sure. I mean, I might run into her at some point. But who's to say she even wants to see me?"
    a "..."
    mc "Anyway... What about you? How's college life treating you? Lots of partying and drinking?"
    scene 01_043 with Dissolve(1)
    a "{i}(Changing the topic... Even after all those years, maybe there are still some lingering feelings.){/i}"
    a "I wish... We have the occasional party, but not as wild as you might expect."
    mc "What? No crazy nights with people dancing naked on tables, playing absurd games, and jumping into pools fully clothed?"
    a "Haha. I think you've watched one too many college romcoms."
    mc "Damn... There go all my hopes and dreams."
    a "Not saying those kinds of parties never happen... I just don't have time for most of them."
    mc "Pfew... Don't scare me like that, Alexis!"
    scene black with Dissolve(2)
    pause 2
    n "We continue to talk for hours..."
    scene black with Dissolve(2)
    pause 2
    scene 01_044 with Dissolve(1)
    a "Hey... Can I see your tattoos?"
    mc "Sure."
    scene 01_045 with Dissolve(1)
    a "They look pretty new."
    mc "Yeah, I got them a few weeks ago. Birthday gift from my dad."
    a "Went straight for the full sleeve, huh? They're really nice. Must've taken a while?"
    mc "Four sessions. Each around six hours. So yeah, it took some time."
    a "That's a lot of sitting still while a needle repeatedly stabs your skin..."
    mc "Tell me about it."
    scene 01_046 with Dissolve(1)
    a "Oh... What's this one?"
    mc "Hmm? Which one do you mean?"
    scene 01_047 with Dissolve(1)
    mc "This one here?"
    a "..."
    scene 01_048 with Dissolve(1)
    mc "What? Why are you smiling?"
    mc "Is it the butterfly?"
    a "..."
    mc "Hey! Guys can have butterfly tattoos!"
    scene 01_049 with Dissolve(1)
    mc "Do you have any tattoos?"
    a "Nope. I've thought about it, but... I wouldn't even know what to get, or where."
    a "And just getting a tattoo for the heck of it isn't really my thing. It has to mean something, you know?"
    mc "Fair enough."
    a "Did it hurt? I've heard some spots can be brutal."
    mc "It wasn't too bad. Some places were more sensitive than others."
    mc "But my second one... That was a whole different story."
    scene 01_050 with Dissolve(1)
    a "Oh, you have another one?"
    mc "Yeah. It's on my ribs."
    a "So basically, at this rate, you'll be fully covered by next year."
    mc "Haha, no way... That's it for me."
    mc "Well... Maybe the name of my future wife."
    scene 01_051 with Dissolve(1)
    a "Oh no! You wouldn't, [mc]..."
    mc "And in a few years, I'll probably have a list of names crossed out on the other arm."
    scene 01_052 with Dissolve(1)
    a "Hahaha... That's so ridiculous."
    mc "Haha..."
    a "The sad part is... I can totally picture you doing it."
    mc "Haha."
    scene 01_053 with Dissolve(1)
    mc "So if you want your name on me, better act fast. I've still got a few blank spots left."
    a "Heh... Intriguing offer. I'll keep that in mind."
    mc "Hehe..."
    menu:
        "Check her out[KoGa3AutoWTChange1]{size=-4}(Alexis Points+2) {/size} {/color}":
            $ Alexis_Points += 2
            # Alexis (4)
            scene 01_054 with Dissolve(1)
            mc "{i}(Not wearing a bra...){/i}"
            scene 01_055 with Dissolve(1)
            mc "{i}(Shit... Did she catch me looking?){/i}"
            mc "{i}(Hard not to notice though. She's gorgeous! And I've been so caught up in the conversation, I barely took it all in.){/i}"
            mc "{i}(And those eyes... Hazel, right? Damn.){/i}"
        "Don't":
            pass
    scene 01_056 with Dissolve(1)
    a "Uhm [mc]... Could you let me pass for a second?"
    a "I need to use the bathroom."
    mc "Yeah, sure. Let me get up."
    scene 01_057 with Dissolve(1)
    a "Thanks."
    a "And uhm..."
    a "Join me in a couple of minutes."
    mc "Wait, what?"
    scene 01_058 with Dissolve(1)
    mc "{i}(Did she just...? No way...){/i}"
    mc "{i}(She can't be serious... Or is she?){/i}"
    menu:
        "Join her[KoGa3AutoWTChange1]{size=-4}(MC SexCounter+1, SexCounter Alexis+1, Alexis Intro Join, Alexis Sex, Alexis Points+2, Rachel End) {/size} {/color}":
            $ MC_SexCounter += 1
            # MC_Sex (1)
            $ SexCounter_Alexis += 1
            # Alexis_Sex (1)
            $ Alexis_Intro_Join = True
            $ Alexis_Sex = True
            $ Alexis_Points += 2
            # Alexis (6)
            $ Rachel_End = True
            jump Intro_Plane_Alexis
        "Stay":
            scene black with Dissolve(2)
            pause 2
            scene 01_031 with Dissolve(1)
            mc "Uhm... Sorry about that, I..."
            a "Don't worry about it. I don't know what I was thinking."
            mc "{i}(I hope this doesn't make things awkward now.){/i}"
            scene black with Dissolve(2)
            pause 2
            scene 01_092 with Dissolve(1)
            fa "Hello! Can I get you anything?"
            scene 01_101 with Dissolve(1)
            fa "Something to drink, or a snack, perhaps?"
            scene 01_094 with Dissolve(1)
            mc "I'm good, thank you."
            a "Nothing for me, thanks."
            fa "Alright."
            menu:
                "Check her out[KoGa3AutoWTChange1]{size=-4}(Rachel Intro CheckOut) {/size} {/color}":
                    $ Rachel_Intro_CheckOut = True
                    scene black with Dissolve(1)
                    transform moveup:
                        xalign 0.5 yalign 1.0
                        linear 5.0 yalign 0.0
                    show 01_102 at moveup
                    pause 3
                    ""
                    scene 01_103 with Dissolve(1)
                    mc "..."
                    scene 01_104 with Dissolve(1)
                    mc "{i}(Ugh... I really shouldn't have had so much to drink before boarding.){/i}"
                    mc "{i}(No point in holding it till we land, though.){/i}"
                    jump Intro_Stewardess
                "Don't[KoGa3AutoWTChange1]{size=-4}(Rachel End) {/size} {/color}":
                    $ Rachel_End = True
                    jump Intro_Plane_End

label Intro_Plane_Alexis:
    scene black with Dissolve(2)
    pause 2
    scene 01_059 with Dissolve(1)
    n "*Knock-knock!*"
    scene 01_060 with Dissolve(1)
    mc "Hi..."
    a "Hey!"
    scene 01_061 with Dissolve(1)
    a "..."
    scene 01_062 with Dissolve(1)
    a "{i}(Hmm... Coast looks clear.){/i}"
    a "No one's watching!"
    scene 01_063 with Dissolve(1)
    a "Quick! Get in!"
    scene 01_064 with Dissolve(1)
    mc "Hi!"
    a "Hi..."
    scene 01_065 with Dissolve(1)
    a "..."
    mc "{i}(Are we really gonna do this?){/i}"
    mc "{i}(Fuck! I'm so nervous!){/i}"
    scene 01_066 with Dissolve(1)
    a "What are you looking at so intensely? Second thoughts?"
    mc "Uhm no..."
    mc "Are you sure about this?"
    a "{i}(No...){/i}"
    a "Yes! Come here and kiss me already."
    scene 01_067 with Dissolve(1)
    mc "{i}(Soft lips.){/i}"
    a "{i}(Oh... A little lip nibble, huh? He knows what he's doing. I like it.){/i}"
    scene 01_068 with Dissolve(1)
    mc "{i}(Wow. She's really going for it now.){/i}"
    mc "{i}(Still can't believe this is happening!){/i}"
    mc "{i}(I'm not dreaming, right?){/i}"
    scene 01_069 with Dissolve(1)
    mc "{i}(Mmm... She smells amazing too.){/i}"
    scene 01_070 with Dissolve(1)
    a "Hey..."
    scene 01_071 with Dissolve(1)
    mc "Hmm?"
    a "Don't get me wrong... I really enjoy the foreplay. But we kinda have limited time. People could be needing to use the bathroom any minute."
    mc "Yeah. You're right. Straight to business it is! Or pleasure?"
    a "Heh..."
    scene 01_072 with Dissolve(1)
    a "Wait... You did lock the door, right?"
    mc "I did, I double-checked earlier."
    mc "{i}(Not making that mistake again.){/i}"
    scene 01_073 with Dissolve(1)
    a "{i}(I'm getting nervous now. But this is so exciting.){/i}"
    scene 01_074 with Dissolve(1)
    mc "You sure about this?"
    a "{i}(Still no, but I want this...){/i}"
    a "I am!"
    scene 01_075 with Dissolve(1)
    a "Ahh."
    mc "Sorry..."
    a "Just a little slower."
    scene 01_076 with Dissolve(1)
    mc "{i}(This feels so nice.){/i}"
    a "*Moaning*"
    mc "{i}(Holy shit! I'm fucking this cute girl... On a plane!){/i}"
    show 01_077
    ""
    show 01_078
    ""
    scene 01_079 with Dissolve(1)
    mc "{i}(Her boobs feel amazing too!){/i}"
    mc "{i}(If we weren't in the cramped space, I'd suck on those nipples...){/i}"
    show 01_080
    mc "{i}(I'm about to cum...){/i}"
    a "[mc]. I... I'm..."
    mc "{i}(I guess she is, too!){/i}"
    scene 01_081 with vpunch
    pause 2
    scene 01_081 with vpunch
    mc "{i}(Fuck!!!){/i}"
    a "Mmm!"
    scene 01_082 with Dissolve(1)
    mc "Wow. That was..."
    a "*Nods*"
    scene 01_083 with Dissolve(1)
    mc "{i}(One more squeeze!){/i}"
    scene 01_084 with Dissolve(1)
    a "As much as I'd love a second round, we better head back."
    mc "Yeah, we've pushed our luck enough."
    a "Hehe. You go first. I need a minute to freshen up."
    mc "I'll save you a spot."
    a "Thanks. What a gentleman!"
    scene 01_086 with Dissolve(1)
    mc "{i}(Oh shit!){/i}"
    mc "{i}(Does she...){/i}"
    scene 01_087 with Dissolve(1)
    mc "Uhm... Excuse me."
    fa "..."
    scene 01_085 with Dissolve(1)
    a "{i}(Shit...!){/i}"
    a "{i}(What have I done?){/i}"
    $ renpy.end_replay()
    scene black with Dissolve(2)
    pause 2
    scene 01_043 with Dissolve(1)
    a "I can't believe we just did that."
    mc "Yeah... Me neither."
    mc "It was amazing."
    a "Exhilarating!"
    scene 01_040 with Dissolve(1)
    a "Do you think... like... people noticed?"
    mc "Well... You weren't exactly quiet in there."
    scene 01_088 with Dissolve(1)
    a "Hey! I wasn't that loud. I don't think...?"
    mc "Haha. Didn't you see their faces when you walked back to your seat?"
    mc "We're lucky they can't just kick us off the plane."
    scene 01_089 with Dissolve(1)
    a "Oh no... I feel so embarrassed now. Hahaha."
    mc "Haha."
    scene 01_090 with Dissolve(1)
    mc "I guess we've officially joined the Mile High Club."
    a "Oh... Yeah! I guess we did."
    a "Something I can finally tick off my bucket list."
    mc "So that's how it goes, huh?"
    scene 01_091 with Dissolve(1)
    a "Guilty as charged..."
    mc "I feel so used now."
    mc "A good used."
    a "Haha..."
    scene 01_092 with Dissolve(1)
    fa "Hello. Can I get you anything?"
    scene 01_093 with Dissolve(1)
    fa "Something to drink, or a snack?"
    fa "A tissue, perhaps?"
    scene 01_094 with Dissolve(1)
    mc "{i}(Well shit. She knows.){/i}"
    mc "Uhm... I'm good. Do you want anything, Alexis?"
    a "No, thanks."
    scene 01_095 with Dissolve(1)
    a "Who spit in her cereal? I know people can have a bad day but... Such attitude!"
    mc "I think we did."
    a "What?"
    scene 01_096 with Dissolve(1)
    mc "She kinda saw me leaving the bathroom earlier..."
    a "That explains the tissue question. Haha."
    a "Oh well..."
    scene black with Dissolve(2)
    pause 2
    scene 01_097 with Dissolve(1)
    n "We continue to chitchat for a while until we both fall asleep."
    scene black with Dissolve(2)
    pause 2
    scene 01_098 with Dissolve(1)
    fa "Uhm... Excuse me, sir?"
    fa "Sir?"
    scene 01_099 with Dissolve(1)
    mc "Hmm?"
    fa "We landed ten minutes ago. You can grab your stuff and exit the plane now."
    fa "Do you need any assistance deplaning?"
    mc "Oh... Sorry about that. No, I'm good. I just fell asleep. I'll be on my way, thanks."
    scene 01_100 with Dissolve(1)
    mc "{i}(Hmm... Alexis left already?){/i}"
    mc "{i}(Shit. I should've asked for her number.){/i}"
    mc "{i}(Maybe not... This was probably a one-time thing. It's not like we'll see each other again.){/i}"
    stop music fadeout 1.0
    jump Intro_City_Bus

label Intro_Flashback:
    scene 01_127 with Dissolve(1)
    n "Everything started out pretty normal..."
    n "Caring parents, lots of friends, a good childhood altogether."
    scene 01_128 with Dissolve(1)
    n "That changed very quickly though, once Dad decided to leave and divorce Mom. Or did Mom divorce Dad? Hmm..."
    n "Anyway, it happened out of nowhere. I had no idea what was going on."
    scene 01_129 with Dissolve(1)
    n "Mom, especially, had a really hard time."
    n "She couldn't cope with it whatsoever and was a total mess afterward."
    n "Countless nights of drinking and crying..."
    n "I didn't know what to do. And honestly, I wasn't the easiest kid to take care of either."
    scene 01_130 with Dissolve(1)
    n "Luckily, she often got help from Melissa, her best friend since forever and our next-door neighbour."
    n "Melissa always knew what to do and say to lift Mom's spirits."
    n "She came by almost every day with her daughter, Erynn."
    scene 01_131 with Dissolve(1)
    n "Ever since I can remember, Erynn and I were inseparable."
    n "Always playing and chasing each other around, even though she's three years older than me."
    scene 01_132 with Dissolve(1)
    n "As we grew older, though, our interests started to drift apart."
    n "I still liked playing with her..."
    n "But Erynn began hanging out more with her school friends."
    n "She was really popular and got a lot of attention from other boys."
    n "Especially that idiot Ethan, who stuck to her like glue and even gave her bike rides to school."
    n "I wasn't happy about it at all. I grew more jealous every day."
    scene 01_133 with Dissolve(1)
    n "I was about eleven or twelve when I came up with, in my opinion, the only way to spend more time with Erynn again."
    n "Confessing..."
    n "Telling her I liked her."
    scene 01_134 with Dissolve(1)
    n "I still remember the laughter like it happened yesterday."
    n "She took it as a joke..."
    n "Or rather, she made me the joke. Even her friends were laughing at me."
    n "I hated her for it."
    n "... And my jealousy slowly turned into anger."
    scene 01_135 with Dissolve(1)
    n "It didn't stop there."
    n "That anger didn't just stay bottled up. It started affecting everything. My grades dropped, my attitude at school and home got worse."
    n "Mom kept getting calls from teachers, one complaint after another. Detention became part of my daily routine."
    n "And honestly? I couldn't have cared less."
    n "After a few weeks of dealing with me, Mom finally had enough, and she sent me to stay with Dad during spring break."
    n "That one week turned into years. Honestly, I've lost track of how long it's been now."
    scene 01_016 with Dissolve(1)
    n "When my dad decided to remarry, we moved in with his fiancée and her two kids. The house got really crowded. Stuff happened and... Yeah..."
    n "So, I decided to move back to Mom's place and finish my last year of school there."
    scene black with Dissolve(2)
    pause 2
    n "..."
    scene 01_105 with Dissolve(2)
    fa "Hello! Can I get you anything?"
    scene 01_101 with Dissolve(1)
    fa "Something to drink, or a snack perhaps?"
    mc "I'm good, thank you."
    fa "Sure."
    menu:
        "Check her out[KoGa3AutoWTChange1]{size=-4}(Rachel Intro CheckOut) {/size} {/color}":
            $ Rachel_Intro_CheckOut = True
            scene black with Dissolve(1)
            transform moveup:
                xalign 0.5 yalign 1.0
                linear 5.0 yalign 0.0
            show 01_102 at moveup
            pause 3
            ""
            scene 01_106 with Dissolve(1)
            mc "{i}(The only good thing about flying: Flight attendants! As long as they're female.){/i}"
            scene 01_107 with Dissolve(1)
            mc "{i}(Ugh... I really shouldn't have had so much to drink before boarding.){/i}"
            mc "{i}(No point in holding it till we land, though.){/i}"
            jump Intro_Stewardess
        "Don't[KoGa3AutoWTChange1]{size=-4}(Rachel End) {/size} {/color}":
            $ Rachel_End = True
            jump Intro_Plane_End

label Intro_Stewardess:
    scene black with Dissolve(2)
    pause 2
    scene 01_108 with Dissolve(1)
    ""
    scene 01_109 with hpunch
    mc "..."
    mc "{i}(What the fuck?){/i}"
    scene 01_110 with Dissolve(1)
    fa "Do you really think I didn't notice this whole time?"
    mc "What are you even talking about?"
    scene 01_111 with Dissolve(1)
    fa "You've been staring at me nonstop. It creeps me out."
    fa "Could you please stop?"
    mc "{i}(What is she even on about? I looked like once...){/i}"
    mc "{i}(Okay. Maybe twice.){/i}"
    mc "{i}(Everyone does that... No?){/i}"
    menu:
        "Apologise[KoGa3AutoWTChange1]{size=-4}(Rachel End) {/size} {/color}":
            $ Rachel_End = True
            scene 01_112 with Dissolve(1)
            mc "{i}(*Sigh* I guess I'll just apologise and be done with this.){/i}"
            mc "Sorry about that. Won't happen again."
            mc "If you'll excuse me now, I need to use the bathroom."
            $ renpy.end_replay()
        "Don't apologise[KoGa3AutoWTChange1]{size=-4}(Rachel Intro BJ) {/size} {/color}":
            $ Rachel_Intro_BJ = True
            mc "What's wrong with looking at someone?"
            scene 01_113 with Dissolve(1)
            mc "I'm pretty sure I'm not the only one."
            mc "And if that upsets you, maybe you're in the wrong business..."
            fa "..."
            fa "I'm not here for your entertainment!"
            mc "And I'm not here to apologise for looking at someone!"
            scene 01_114 with hpunch
            mc "..."
            scene 01_115 with Dissolve(1)
            fa "Good!"
            fa "Because I like a bad boy!"
            fa "Get in!"
            scene 01_116 with Dissolve(1)
            mc "Hey... What are you doing?"
            fa "Entertainment!"
            scene 01_117 with Dissolve(1)
            fa "And to be honest... I liked the way you looked at me. Kinda turned me on!"
            fa "So, how about we have a little bit of fun?"
            fa "Let's see what you're hiding under here."
            scene 01_118 with Dissolve(1)
            fa "Oh... Not bad!"
            fa "I can work with this!"
            scene 01_119 with Dissolve(1)
            mc "{i}(Fuck...){/i}"
            scene 01_120 with Dissolve(1)
            fa "So... How is this for entertainment?"
            mc "No complaints here. This airline just jumped into my top five."
            fa "Top five? We can't have that. We always strive to be number one!"
            fa "I guess I'll show you some more 'top-notch' service!"
            show 01_121
            mc "{i}(Damn, this is great!){/i}"
            scene 01_122 with Dissolve(1)
            pi "Ladies and gentlemen, as we start our descent, please be seated, make sure your seat and tray tables are in their full upright position."
            pi "Make sure your seatbelt is securely fastened, and all carry-on luggage is stowed underneath the seat in front of you or in the overhead bins."
            fa "Oh shit...!"
            scene 01_123 with Dissolve(1)
            fa "Well this was... fun."
            fa "Make sure you pull up your pants before returning to your seat."
            scene 01_124 with Dissolve(1)
            mc "Wait...!"
            mc "Are you fucking kidding me?"
            mc "*Sigh*"
            $ renpy.end_replay()
    jump Intro_Plane_End

label Intro_Plane_End:
    scene black with Dissolve(2)
    pause 2
    if Alexis_Intro_Ignore == False:
        scene 01_125 with Dissolve(1)
    else:
        scene 01_126 with Dissolve(1)
    play sound "Sounds/Aeroplane_Beep.wav" volume 0.3
    pi "Ladies and gentlemen, welcome to Madison Airport. Local time is 10:05 and the temperature is twenty-two degrees Celsius."
    pi "For your safety and comfort, please remain seated with your seatbelt fastened until the captain turns off the fasten seatbelt sign."
    pi "This will indicate that we have parked at the gate and that it is safe for you to move about."
    pi "Please check around your seat for any personal belongings you may have brought on board with you."
    pi "And please use caution when opening the overhead bins, as heavy items may have shifted around during the flight."
    pi "If you require deplaning assistance, please remain in your seat until all other passengers have deplaned. One of our crew members will then be happy to assist you."
    pi "On behalf of Skye Airlines and the entire crew, I’d like to thank you for joining us on this flight and we are looking forward to seeing you onboard again in the near future. Have a nice day!"
    stop music fadeout 1.0
    jump Intro_City_Bus

label Intro_City_Bus:
    scene black with Dissolve(2)
    pause 2
    play music "Sounds/Street_Traffic.mp3" volume 0.6
    scene 01_136 with Dissolve(1)
    n "A bus ride and forty minutes later."
    scene 01_137 with Dissolve(1)
    mc "{i}(Alright, let's see... Which bus do I need, and when does it arrive?){/i}"
    mc "..."
    mc "{i}(Two hours! Are you kidding me?){/i}"
    mc "{i}(One of the downsides of living on the outskirts of the city, I guess.){/i}"
    scene 01_138 with Dissolve(1)
    mc "{i}(I'm not in the mood to waste another two hours wandering around the city.){/i}"
    mc "{i}(My only options are to head to the train station or call Mom and hope she can pick me up.){/i}"
    scene 01_139 with Dissolve(1)
    mc "{i}(Let's try Mom first.){/i}"
    mc "..."
    mc "{i}(Come on... Please, pick up!){/i}"
    scene 01_140 with Dissolve(1)
    m "Hello?"
    mc "Hey, Mom. It's me."
    m "Hey, honey! How are you?"
    mc "I'm good."
    m "Did you just land?"
    scene 01_141 with Dissolve(1)
    mc "About an hour ago. I took the bus and I'm in the city now."
    m "Oh? Why didn't you call me earlier? I could've picked you up at the airport."
    mc "I wanted to surprise you, but now I'm kinda stuck... That's why I'm calling..."
    m "What happened?"
    mc "Don't worry. There won't be a bus home for another two hours. If possible, could you come pick me up?"
    scene 01_142 with Dissolve(1)
    m "Of course, honey! Where are you?"
    mc "At the bus stop at Sunrise Avenue."
    m "That's not far. I'll be there in ten to fifteen minutes."
    mc "Alright. Thanks, Mom."
    m "I'll hurry. Bye, [mc]."
    mc "Bye."
    scene 01_143 with Dissolve(1)
    mc "{i}(Well... Let's wait here I guess.){/i}"
    scene black with Dissolve(2)
    pause 2
    scene 01_144 with Dissolve(1)
    mc "{i}(Nice car!){/i}"
    mc "{i}(Wait... Isn't that...?){/i}"
    scene 01_145 with Dissolve(1)
    n "*Heavy braking*"
    mc "{i}(Haha. I think it is!){/i}"
    scene 01_146 with Dissolve(1)
    m "Hey, honey!"
    mc "Hey, Mom."
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 01_147 at moveup
    pause 3
    mc "{i}(She's cut her hair.){/i}"
    mc "{i}(Looks nice.){/i}"
    scene 01_148 with Dissolve(1)
    mc "How are you, Mom?"
    m "Really happy!"
    scene 01_149 with Dissolve(1)
    m "I still can't believe my baby is finally back!"
    mc "Heh..."
    scene 01_150 with Dissolve(1)
    m "I missed you so much!"
    mc "I missed you too, Mom. And I'm sorry for..."
    m "No, that's all behind us now. I'm just so glad you're here."
    scene 01_151 with Dissolve(1)
    m "Let me get a good look at you."
    m "You've changed so much."
    mc "It's been a long time since we last saw each other."
    m "Yeah... Honestly, I almost drove right past you."
    mc "Almost? You actually did and had to slam on the brakes!"
    scene 01_152 with Dissolve(1)
    m "Haha, sorry. I didn't recognise you at first."
    m "Especially with those tattoos on your arm."
    m "Can't believe Andres agreed to all of them."
    mc "{i}(He only agreed to one tattoo. Not a whole sleeve.){/i}"
    mc "He even paid for it."
    scene 01_153 with Dissolve(1)
    m "*Sigh*"
    m "Somehow, that doesn't surprise me at all."
    m "You look good, though. Really handsome!"
    mc "Thanks. You look great, too."
    mc "I like your new hairstyle."
    scene 01_154 with Dissolve(1)
    m "Really? Thanks! Melissa talked me into it."
    mc "Oh... She still cuts hair?"
    m "Mm-hmm, she does."
    scene 01_155 with Dissolve(1)
    m "Well, let's head home, and you can tell me everything I missed these past few years."
    mc "Sounds good."
    m "Come on, let's go."
    scene 01_156 with Dissolve(1)
    mc "I see you've bought a new car."
    m "Uh-huh. What do you think?"
    mc "It's an amazing car. I really like it. Must have been expensive, no?"
    m "It wasn't cheap!"
    scene 01_157 with Dissolve(1)
    m "Here!"
    mc "Oh, I can drive?"
    m "You've got your licence, right?"
    mc "I do."
    m "Then yes!"
    scene 01_158 with Dissolve(1)
    stop music
    play music "Sounds/Traffic.mp3" volume 0.5
    mc "Sports seats, sunroof, a huge media display... You went all out, huh?"
    mc "I'll definitely be borrowing this car a few times!"
    scene 01_159 with Dissolve(1)
    ""
    scene black with Dissolve(2)
    pause 2
    scene 01_160 with Dissolve(1)
    m "So... How have you been since we last spoke?"
    mc "All good. Nothing much."
    mc "Just happy to finally be back."
    m "I'm glad you decided to come back and live with me."
    scene 01_161 with Dissolve(1)
    mc "It wasn't a hard decision. Once Dad decided we'd move in with Haley, the house got really crowded."
    m "Oh? Did something happen with Andres?"
    mc "{i}(Sorry, Mom... Don't really want to talk about that.){/i}"
    mc "No... All good."
    scene 01_162 with Dissolve(1)
    m "Okay. How is he, anyway?"
    mc "He's doing alright, I suppose."
    m "And Haley? Was she nice to you? She has two daughters, right?"
    mc "Yes. Nikki and Cara."
    scene 01_163 with Dissolve(1)
    m "That must have been quite the change. From being an only child to suddenly having two sisters."
    mc "Yeah. You could say that..."
    m "Did you get on with them?"
    mc "More or less... We had our ups and downs, like any siblings."
    scene 01_164 with Dissolve(1)
    m "You can take a left here."
    mc "Shortcut?"
    m "Yes. They paved this road last year. Now we don't have to go all the way around Brighton Park."
    jump Intro_Home

label Intro_Home:
    scene black with Dissolve(2)
    pause 2
    stop music
    play music ("Music/LoFi Indie 3.mp3", "Music/LoFi Indie 1.mp3", "Music/LoFi Indie 2.mp3") volume 0.2
    # Copyright NyxValeria
    scene 01_165 with Dissolve(1)
    n "After a quick drive, we arrive home."
    scene 01_166 with Dissolve(1)
    m "Do you still remember this place?"
    mc "It's only been five... six... years? Of course I do."
    scene 01_167 with Dissolve(1)
    m "Well then... Welcome home!"
    mc "Thank you."
    scene black with Dissolve(1)
    pause 2
    scene 01_168 with Dissolve(1)
    m "Did you eat before your flight?"
    mc "I didn't, no. It was such an early flight, I didn't have time."
    mc "I was just glad I woke up on time."
    m "Haha. You still love your sleep, huh?"
    mc "Oh, definitely."
    scene 01_169 with Dissolve(1)
    m "Uhm, I can whip up some quick pancakes if you're hungry."
    m "Or would you prefer something else?"
    mc "No, pancakes sound perfect."
    m "Alright then."
    scene 01_170 with Dissolve(1)
    m "Crispy edges and fluffy inside?"
    mc "{i}(I can't wait to taste them again... It's been so long.){/i}"
    mc "Yes, please."
    scene black with Dissolve(1)
    pause 2
    scene 01_171 with Dissolve(1)
    m "Here you go, honey."
    mc "They smell amazing! Thanks, Mom!"
    m "You're welcome."
    scene 01_172 with Dissolve(1)
    mc "Mmm... So good!"
    mc "Still the best pancakes!"
    scene 01_173 with Dissolve(1)
    m "Thanks. They're on the menu at the restaurant now, too."
    mc "As they should be. How's the restaurant doing, anyway?"
    scene 01_174 with Dissolve(1)
    m "Really well, actually."
    m "I haven't told you yet, but I'm expanding in a few months."
    mc "Oh? You're opening a second restaurant?"
    m "No, not a restaurant. A café."
    scene 01_175 with Dissolve(1)
    mc "A café? That's great, Mom."
    mc "Also in the city?"
    m "Yes, on Madison Square."
    mc "That's a good location."
    mc "Especially once the tourist season kicks off."
    scene 01_176 with Dissolve(1)
    m "So... If you have time after school or at the weekends..."
    mc "You want me to help out?"
    m "I could really use your help. Like doing the dishes, bussing tables... I know they aren't the most exciting jobs, so only if you want to."
    mc "Yeah, of course, Mom. I don't mind, and some extra cash is always good."
    m "Thanks. But focus on school first. Once you're settled in, we'll talk about a few shifts a week."
    scene 01_177 with Dissolve(1)
    n "*Ding-dong*"
    mc "Expecting someone?"
    m "Not that I remember. One sec, I'll go check."
    scene black with Dissolve(1)
    pause 2
    scene 01_178 with Dissolve(1)
    m "Oh hey, Melissa."
    me "Hey. I heard the car. Is he back?"
    me "Never mind. Your big smile says it all."
    me "How does he look?"
    scene 01_179 with Dissolve(1)
    m "Well, why don't you come in and see for yourself?"
    me "Uh, you just got him back. I don't want to interrupt your mother-son time."
    m "Mel... You know better than that. Just come inside."
    me "Alright."
    scene 01_180 with Dissolve(1)
    m "[mc], do you remember Melissa?"
    me "Hey there."
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 01_181 at moveup
    pause 3
    mc "Of course I do..."
    mc "{i}(She hasn't aged a day...){/i}"
    menu:
        "Give her a hug[KoGa3AutoWTChange1]{size=-4}(Melissa Points+2, Melissa Intro Hug) {/size} {/color}":
            $ Melissa_Points += 2
            # Melissa (2)
            $ Melissa_Intro_Hug = True
            scene 01_182 with Dissolve(1)
            mc "How are you, Melissa?"
            me "I'm good, thanks. How about you?"
            mc "I'm good, too."
        "Give her a handshake":
            scene 01_183 with Dissolve(1)
            mc "How are you?"
            me "I'm good, thanks. How about you?"
            mc "Same."
    scene 01_184 with Dissolve(1)
    me "Wow, just look at you. You've turned out really well."
    me "Tall, dark, and handsome!"
    mc "Heh..."
    if Melissa_Intro_Hug == True:
        scene 01_185 with Dissolve(1)
        mc "You're looking good too, Melissa!"
        me "Thanks!"
    else:
        pass
    scene 01_186 with Dissolve(1)
    me "Erynn will be so happy you're back. Every time she visits, she asks about you."
    mc "..."
    mc "About that... Can you do me a favour and not tell her yet?"
    mc "I want to surprise her myself."
    me "Of course."
    scene 01_187 with Dissolve(1)
    me "Anyway, let me have a look at those tattoos."
    me "You finally turned to the dark side and got a whole sleeve, huh?"
    mc "I guess so, yeah."
    m "Can you believe that Andres even paid for it?"
    scene 01_188 with Dissolve(1)
    me "Oh, he did? They're really well done. Very clean, no scarring, no blowouts..."
    me "Must be a good tattoo artist, then?"
    mc "Yeah. Very talented."
    me "Indeed. Is that your only tattoo?"
    scene 01_189 with Dissolve(1)
    mc "Uh, no... I've got another one on my ribs."
    m "What? You've got more?"
    m "*Sigh*"
    scene 01_190 with Dissolve(1)
    m "He's starting to look more like he's your son than mine."
    me "Haha, right?"
    me "I'll adopt him right away."
    m "Sure. Want to trade him for Erynn?"
    scene 01_191 with Dissolve(1)
    mc "Hey! I'm standing right here, you know? I've been home thirty minutes, and you want to get rid of me already?"
    me "You sure about that? I might be the one who got the better deal..."
    mc "Thanks."
    scene 01_192 with Dissolve(1)
    m "I'm kidding! You're not going anywhere. You're stuck with me forever!"
    mc "Forever?"
    mc "I accept the trade!"
    scene 01_193 with Dissolve(1)
    mc "Come on, Mel. Let's go home!"
    m "..."
    m "Hope you enjoyed those pancakes! Mel's pancakes are shit!"
    me "Haha. Can't argue with that."
    scene black with Dissolve(1)
    pause 2
    scene 01_194 with Dissolve(1)
    me "All set to start school tomorrow?"
    mc "I'd hoped I'd have a few days to settle in, but I couldn't get an earlier flight."
    mc "It is what it is. Just need to unpack some stuff and I guess I'll be good to go."
    me "Nervous?"
    mc "Not really. It's not the first time I've switched schools. Second time this school year alone."
    scene 01_195 with Dissolve(1)
    me "The only thing missing then is a haircut, huh?"
    mc "I could do with one, yeah. It's been two months since my last cut."
    me "How about you come over later this afternoon and I'll cut it for you?"
    mc "If you've got time, that'd be great. Thanks."
    me "Sure."
    scene 01_196 with Dissolve(1)
    mc "It was nice catching up, but I think it's time I started unpacking some of my stuff."
    m "If you need any help, just come and get me."
    mc "Thanks, Mom. And Melissa, I'll see you later then?"
    me "Yes, see you then."
    scene 01_197 with Dissolve(1)
    mc "{i}(Oh damn... Did I have this much stuff?){/i}"
    mc "{i}(I hope Mom didn't carry all those boxes upstairs on her own.){/i}"
    mc "{i}(Feels like I never left. All my toys are still here. The comics... Even my skateboard and the posters.){/i}"
    mc "{i}(Guess I'll have to do more than just unpack. Can't have girls over with all this mess in my room.){/i}"
    mc "{i}(*Sigh* Let's get started...){/i}"
    scene 01_198 with Dissolve(1)
    mc "{i}(Freakin' Zo... Heh. Now I wish I'd caught one of his last games.){/i}"
    mc "{i}(When did he retire? Three or four years ago?){/i}"
    mc "{i}(Sorry, Zo! But you've got to go, too.){/i}"
    scene black with Dissolve(2)
    pause 2
    scene 01_199 with Dissolve(1)
    mc "{i}(Pfew... Finally done.){/i}"
    mc "{i}(The room looks so empty now. I need something to put on the walls to liven it up a bit. Maybe a plant or two, if I can keep them alive...){/i}"
    mc "{i}(But that's for later or tomorrow. I should head over to Melissa's first.){/i}"
    stop music fadeout 1.0
    jump Intro_Melissa

label Intro_Melissa:
    scene black with Dissolve(1)
    play music ("Music/LoFi Upbeat 1.mp3", "Music/LoFi Upbeat 2.mp3", "Music/LoFi Upbeat 3.mp3", "Music/LoFi Upbeat 4.mp3") volume 0.2
    # Copyright NyxValeria
    pause 2
    scene 01_200 with Dissolve(1)
    mc "{i}(So Erynn's moved out, then?){/i}"
    mc "{i}(Maybe she's in the city now, or living in a dorm at MSU.){/i}"
    mc "{i}(Does she even go to college?){/i}"
    mc "{i}(Doesn't really matter, I suppose.){/i}"
    scene 01_201 with Dissolve(1)
    n "*Knock-knock!*"
    mc "{i}(She must've heard that... right?){/i}"
    n "*Knock-knock!*"
    menu:
        "Call for Melissa":
            scene 01_202 with Dissolve(1)
            mc "MELISSA?"
            me "Sorry, [mc]. I'm in the backyard."
            me "Use the gate and come round. I'll grab my stuff."
            scene 01_203 with Dissolve(1)
            mc "{i}(Right... Melissa's got a pool here.){/i}"
            mc "{i}(Hope I still get to use it now and then.){/i}"
            jump Intro_Melissa_Haircut
        "Go to the backyard":
            jump Intro_Melissa_Sunbath

label Intro_Melissa_Sunbath:
    if _in_replay:
        $ Melissa_Points = 2
    $ Melissa_Intro_Sunbath = True
    scene 01_203 with Dissolve(1)
    mc "{i}(Right... Melissa's got a pool here.){/i}"
    mc "{i}(Hope I still get to use it now and then.){/i}"
    scene 01_204 with Dissolve(1)
    mc "Melis...sa."
    mc "{i}(Oh my... Is she...?){/i}"
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 01_205 at moveup
    pause 3
    mc "..."
    mc "{i}(She looks amazing!){/i}"
    mc "{i}(Is she asleep?){/i}"
    scene 01_206 with Dissolve(1)
    mc "*Whispers* Melissa?"
    mc "..."
    mc "{i}(Looks like she is.){/i}"
    mc "{i}(Should I wake her? Please don't slap me...!){/i}"
    mc "M-Melissa?"
    scene 01_207 with Dissolve(1)
    me "Hmm?"
    mc "Uh..."
    scene 01_208 with vpunch
    me "Aaah...! [mc]!"
    me "What are you doing here?"
    scene 01_209 with Dissolve(1)
    mc "Sorry, Mel... I didn't mean to... Uh..."
    mc "I knocked a few times, but I guess you didn't hear me."
    mc "So, I thought maybe you were in the backyard..."
    mc "I'm sorry. If I'd known you were..."
    scene 01_210 with Dissolve(1)
    me "It's alright, don't worry. Not your fault."
    me "I must've dozed off. Happens if you drink appletinis before noon..."
    mc "Heh..."
    me "Let me grab my stuff."
    mc "Sure."
    scene 01_211 with Dissolve(1)
    mc "{i}(She's definitely going to shave my head for this.){/i}"
    menu:
        "Check her out":
            mc "{i}(She really keeps in shape, though.){/i}"
            scene 01_213 with Dissolve(1)
            mc "{i}(What an ass!){/i}"
            mc "{i}(She must be doing squats...){/i}"
        "Apologise again[KoGa3AutoWTChange1]{size=-4}(Melissa Points+2) {/size} {/color}":
            $ Melissa_Points += 2
            # Melissa (4)
            mc "I'm sorry, Mel..."
            scene 01_212 with Dissolve(1)
            me "As I said, don't worry about it."
            me "Besides... Nothing you haven't seen before, right?"
            mc "Uh..."
            mc "{i}(Is she talking about me seeing her naked... or just in general?){/i}"
    scene 01_214 with Dissolve(1)
    mc "{i}(Fuck!){/i}"
    mc "{i}(Was she always this hot?){/i}"
    stop music fadeout 1.0
    $ renpy.end_replay()
    jump Intro_Melissa_Haircut

label Intro_Melissa_Haircut:
    scene black with Dissolve(1)
    play music ("Music/LoFi Upbeat 4.mp3", "Music/LoFi Upbeat 2.mp3", "Music/LoFi Upbeat 1.mp3", "Music/LoFi Upbeat 3.mp3") volume 0.2
    # Copyright NyxValeria
    pause 2
    scene 01_215 with Dissolve(1)
    me "Alright... Ready to get some work done?"
    mc "Yes!"
    me "Can you grab a chair from around the corner and bring it over here?"
    mc "Sure thing."
    scene 01_216 with Dissolve(1)
    me "Any preference? A particular style?"
    mc "Just a trim for now. Keep the top a little longer."
    me "Got it."
    scene 01_217 with Dissolve(1)
    me "So, got a girlfriend?"
    mc "No, not anymore..."
    me "Not anymore? Good to know."
    me "I might know someone else who's single."
    menu:
        "Flirt[KoGa3AutoWTChange1]{size=-4}(Melissa Points+2) {/size} {/color}":
            $ Melissa_Points += 2
            # Melissa (6)
            scene 01_218 with Dissolve(1)
            mc "Oh? Are you looking for a boyfriend, Melissa?"
            me "Depends... You interested?"
            mc "Uh... Wait... Are you actually single?"
            me "Haha, cheeky! I am, but I wasn't talking about me."
            mc "Heh, alright then."
            mc "{i}(Hard to believe she's still single. Just look at her. She's stunning.){/i}"
            scene 01_219 with Dissolve(1)
            mc "So, is she cute? I mean the girl you were talking about. We are talking about a girl, right?"
            me "Haha. Yes, we are. And yep, she's very cute!"
        "Is she cute?":
            scene 01_219 with Dissolve(1)
            mc "Oh? Is she cute?"
            me "Very!"
    scene black with Dissolve(2)
    pause 2
    scene 01_220 with Dissolve(1)
    me "All done."
    mc "Thanks, Mel!"
    me "Let me grab a mirror so you can check it out."
    mc "It's fine, I trust you. I'm sure it looks great."
    me "Only thing missing now is a splash of colour."
    scene 01_221 with Dissolve(1)
    mc "If you want Mom to kill us both, be my guest."
    me "Haha. True. I think she was shocked enough with your tattoos."
    mc "Yeah, though to be fair, she took it better than I expected."
    me "She did."
    scene 01_222 with Dissolve(1)
    me "Honestly, she doesn't care what you look like. She's just happy to have you home."
    me "She really missed you."
    mc "I know. I missed her too."
    scene 01_223 with Dissolve(1)
    mc "How much do I owe you?"
    me "Oh, come on... You know I'm not taking your money."
    mc "That was back then. Things are different now."
    scene 01_224 with Dissolve(1)
    me "Still no. But how about this. Help me out in the backyard sometime. Mow the lawn, clean the pool, stuff like that?"
    mc "Yeah, I can do that."
    me "Deal! Haircuts in exchange for yard work."
    mc "Sounds fair to me!"
    mc "Well... I should head back and get ready for school tomorrow."
    scene 01_225 with Dissolve(1)
    mc "Thanks again, Melissa. And give me a call when you need help with anything."
    me "Give you a call? I'll just come over and drag you outside!"
    mc "Haha. That works too. Bye, Mel."
    me "Bye, [mc]."
    if Melissa_Points == 6:
        scene 01_226 with Dissolve(1)
        mc "Hey, Melissa! I missed you too, by the way!"
        me "Heh... Same here. Happy you're back."
    else:
        pass
    scene black with Dissolve(1)
    pause 2
    scene 01_227 with Dissolve(1)
    er "Hey, Mom!"
    me "Oh... Hey, honey."
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 01_228 at moveup
    pause 3
    me "What are you doing here?"
    me "I thought you said you were coming next weekend?"
    scene 01_229 with Dissolve(1)
    er "Yeah, I was... But I need a book for school. Pretty sure I left it here last time I visited."
    me "Gotcha. How’ve you been?"
    er "I'm good. Who was that just now? I heard you talking to someone."
    me "Oh? Just someone I hired to help out with the backyard and pool stuff."
    er "Hmm... Okay."
    scene 01_230 with Dissolve(1)
    me "How's school going?"
    er "*Sigh*"
    me "Uh-oh... Come on, sit down and tell me."
    er "Let me get these boots off first."
    scene 01_231 with Dissolve(1)
    er "Ugh, my feet are killing me."
    me "I don't know how you walk in those, let alone drive..."
    er "Heh, yeah... Perks of the job, I guess."
    scene 01_232 with Dissolve(1)
    me "So, what happened?"
    er "Nothing happened."
    er "It's just... Everything's piling up. College, modelling, all these photo shoots..."
    er "It's getting overwhelming, and it's stressing me out."
    scene 01_233 with Dissolve(1)
    me "You don't have to do everything now. Focus on school first."
    me "Finish your degree. Work will still be there after."
    scene 01_234 with Dissolve(1)
    er "{i}(If only it were that simple.){/i}"
    er "Yeah, but I need the money... For rent, bills, everything. The apartment doesn't pay for itself."
    scene 01_235 with Dissolve(1)
    me "Look, I just want you to be happy. This time in your life... It should be something you enjoy, not just something you do to survive."
    me "You know you can always move back here if it gets too much. There's room for you, and I'd love having you around more."
    er "Thanks, Mom. I'll think about it."
    me "Good."
    scene 01_236 with Dissolve(1)
    er "So?"
    me "Hmm?"
    er "Is he cute?"
    me "Is who cute?"
    er "The pool boy!"
    scene 01_237 with Dissolve(1)
    me "Haha..."
    er "Stop laughing! Come on, tell me!"
    me "..."
    er "Mom!"
    me "Alright, alright... Yes, he is."
    scene 01_238 with Dissolve(1)
    er "Yeah? How old is he? Do you like him?"
    if Melissa_Points == 6:
        me "*Shakes head* Erynn..."
        me "I do like him, yeah."
        er "Oh wow. That's new."
        me "He's not exactly my age, though. He's closer to yours. Honestly, I think he might even be your type."
    else:
        me "He's around your age, and honestly, he seems more like your type than mine."
    scene 01_239 with Dissolve(1)
    er "Really?"
    er "Maybe I should move back home."
    er "Just imagine it... Lying out here, sunbathing..."
    scene 01_240 with Dissolve(1)
    er "Topless..."
    me "Topless, huh?"
    er "Uh-huh... While he's out here, cleaning the pool... Sneaking little glances..."
    if Melissa_Intro_Sunbath == True:
        me "Déjà vu... Haha."
        scene 01_241 with Dissolve(1)
        er "What? Déjà vu? What do you mean?"
        me "Oh, nothing, hon. I might just join you..."
        er "Haha, Mom... Okay, who is this boy?"
        me "You'll find out soon enough."
        er "You're being super sus right now..."
    else:
        scene 01_241 with Dissolve(1)
        me "I might just join you..."
        er "Haha, Mom..."
    stop music fadeout 1.0
    jump Week1_Monday_Morning

label Week1_Monday_Morning:
    play music ("Music/LoFi Indie 3.mp3", "Music/LoFi Indie 1.mp3", "Music/LoFi Indie 2.mp3") volume 0.2
    # Copyright NyxValeria
    scene black with Dissolve(2)
    pause 2
    n "Monday, 07:30."
    scene 01_242 with Dissolve(1)
    n "*Beep! Beep! Beep! Beep!*"
    mc "Nggh..."
    mc "{i}(Ugh... Already? That alarm is so annoying.){/i}"
    mc "{i}(Why does school have to start this early? Who decided that was a good idea?){/i}"
    scene 01_243 with Dissolve(1)
    m "[mc]?"
    mc "*Yawn*"
    mc "Yeah, I'm up..."
    scene 01_244 with Dissolve(1)
    mc "{i}(Alright, what to wear... I doubt there's a dress code.){/i}"
    mc "{i}(Maybe I should've actually read the student handbook. Oh well... Too late now.){/i}"
    scene black with Dissolve(1)
    pause 2
    scene 01_245 with Dissolve(1)
    m "Good morning, honey."
    mc "Morning, Mom."
    scene 01_246 with Dissolve(1)
    m "Did you get any sleep?"
    mc "Yeah, a little bit."
    m "Good. I made you some breakfast, and there's coffee in the pot. I've got to run. Early shift at the restaurant."
    mc "Thanks, Mom."
    m "Come here, give me a hug before I go."
    scene 01_247 with Dissolve(1)
    m "Even in heels, I still have to stretch to hug you."
    mc "Heh..."
    m "Alright. Have a great first day, and I'll see you tonight. Probably late, though."
    mc "No worries. See you later."
    scene 01_248 with Dissolve(1)
    m "Bye, [mc]."
    scene 01_249 with Dissolve(1)
    m "And try to make a few friends, okay?"
    mc "Seriously, Mom?"
    m "What?"
    mc "*Shakes head* Nothing... See ya."
    m "Bye."
    jump Week1_Monday_School

label Week1_Monday_School:
    stop music fadeout 1.0
    scene black with Dissolve(2)
    play music ("Music/LoFi Upbeat 3.mp3", "Music/LoFi Upbeat 2.mp3", "Music/LoFi Upbeat 1.mp3", "Music/LoFi Upbeat 4.mp3") volume 0.2
    pause 2
    n "Monday 08:42. School."
    scene 01_250 with Dissolve(1)
    mc "{i}(Finally made it. Can’t believe I went to my old school first and now I'm fucking late! Typical.){/i}"
    mc "{i}(Maybe I should've just stayed there. It's way closer.){/i}"
    mc "{i}(But they probably wouldn't take me back, especially if they keep records.){/i}"
    mc "{i}(Oh well... Go Bulldogs? Wait, what's the mascot here anyway?){/i}"
    scene 01_251 with Dissolve(1)
    mc "{i}(This has to be the reception office.){/i}"
    mc "{i}(They'll know where I'm supposed to go.){/i}"
    scene 01_252 with Dissolve(1)
    mc "Morning."
    re "Good morning."
    mc "I'm supposed to start here today."
    scene 01_253 with Dissolve(1)
    re "Let's see... [mc] Moreno?"
    mc "Yes."
    re "You're late!"
    mc "I know, I'm sorry. Took a wrong turn and..."
    scene 01_254 with Dissolve(1)
    re "You were supposed to be here at eight. It's 8:43 now! That's quite a wrong turn."
    mc "Doesn't school start at 8:30?"
    re "It does. But as a transfer student, we expect you here at eight for paperwork. Didn't you read the transfer papers?"
    mc "{i}(Oh, shit! Another thing I should've read...){/i}"
    mc "Sorry..."
    scene 01_255 with Dissolve(1)
    x "Good morning, Mrs Roberts."
    re "Good morning..."
    scene black with Dissolve(1)
    transform moveup:
        xalign 0.5 yalign 1.0
        linear 5.0 yalign 0.0
    show 01_256 at moveup
    pause 3
    mc "{i}(Looks like I'm not the only one running late.){/i}"
    scene 01_257 with Dissolve(1)
    re "This is the third time in two weeks, Miss Ortiz."
    mc "{i}(Uh-oh... You are in trouble, missy.){/i}"
    x "Sorry, sorry..."
    re "Don't let it happen again!"
    scene 01_258 with Dissolve(1)
    x "I won't."
    mc "{i}(Yeah, sure...){/i}"
    re "Now hurry to class."
    x "Thanks, Mrs Roberts. Bye!"
    scene 01_259 with Dissolve(1)
    re "Here's your student handbook and schedule. I suggest you give it a read."
    mc "Thanks. So, where do I have..."
    re "You're in class 3A. The handbook has a school map."
    re "Today, you'll need to share textbooks with a classmate. After classes, come by to get your own books and locker key."
    mc "Got it."
    scene black with Dissolve(1)
    pause 2
    scene 01_260 with Dissolve(1)
    mc "{i}(Hmm... This looks like the right hallway.){/i}"
    mc "{i}(Class was... 3A, right?){/i}"
    mc "{i}(Let me check the timetable and see what's first.){/i}"
    scene 01_261 with Dissolve(1)
    mc "{i}(Ugh, geography first period...){/i}"
    mc "{i}(Not really feeling it today.){/i}"
    menu:
        "Go to class[KoGa3AutoWTChange1]{size=-4}(MC GoodStudent+2) {/size} {/color}":
            $ MC_GoodStudent += 2
            # MC_GoodStudent (2)
            mc "{i}(Guess I can’t skip on my first day.){/i}"
            mc "*Sigh*"
            scene 01_262 with Dissolve(1)
            mc "{i}(Here we go... 3A!){/i}"
            n "*Knock-knock!*"
            jump Episode_2_Start
        "Skip class[KoGa3AutoWTChange1]{size=-4}(MC Week1 Monday Skip, Layla Points+2) {/size} {/color}":
            $ MC_Week1_Monday_Skip = True
            $ Layla_Points += 2
            # Layla (2)
            scene 01_263 with Dissolve(1)
            mc "{i}(Screw it! I'm late anyway.){/i}"
            mc "{i}(Skipping half an hour won't kill anyone...){/i}"
            scene 01_264 with Dissolve(1)
            mc "{i}(Are those footsteps?){/i}"
            mc "{i}(They're getting closer... Gotta move faster.){/i}"
            scene 01_265 with hpunch
            x "HEY!"
            mc "{i}(Crap...){/i}"
            scene 01_266 with Dissolve(1)
            x "Shouldn't you be in class?"
            mc "{i}(Okay, what excuse do I even use now?){/i}"
            scene black with Dissolve(1)
            transform moveup:
                xalign 0.5 yalign 1.0
                linear 5.0 yalign 0.0
            show 01_267 at moveup
            pause 3
            mc "{i}(Hmm... Is she a student or maybe a teacher?){/i}"
            mc "{i}(She looks too young to be a teacher. Unless she's some kind of substitute or interim?){/i}"
            mc "{i}(Wait, could she be the geography teacher looking for me?){/i}"
            mc "{i}(But teachers don't usually wear mini-skirts, right?){/i}"
            scene 01_268 with Dissolve(1)
            mc "{i}(She's cute though!){/i}"
            x "Are you the transfer student or..."
            x "Maybe the new school janitor?"
            mc "Funny..."
            mc "{i}(She's got jokes, huh?){/i}"
            scene 01_269 with Dissolve(1)
            x "Can I see your papers, please?"
            mc "{i}(Better hand them over. Don't need to make this worse.){/i}"
            mc "Sure, here you go."
            x "Thanks."
            scene 01_270 with Dissolve(1)
            x "Hmm... [mc] Moreno."
            x "Transferred from Riverside High."
            x "Class 3A."
            scene 01_271 with Dissolve(1)
            x "Looks like you really are the transfer student."
            x "Would've guessed wrong otherwise."
            mc "*Shakes head*"
            scene 01_272 with Dissolve(1)
            x "Come on, follow me. Class 3A is this way."
            mc "Alright."
            x "By the way, there's a school map in your student handbook."
            x "Finding your way around is pretty easy."
            mc "Right..."
            scene 01_273 with Dissolve(1)
            mc "{i}(So much for free time...){/i}"
            mc "{i}(Hope I'm not in too much trouble. Mom's gonna be pissed.){/i}"
            mc "{i}(Why didn't I just go to class in the first place?){/i}"
            scene 01_274 with Dissolve(1)
            x "{i}(Was he really planning to skip on his first day?){/i}"
            x "{i}(Guess this day won't be boring.){/i}"
            scene 01_275 with Dissolve(1)
            x "Here's class 3A."
            x "I'll let your teacher know you've arrived. Just wait here a moment."
            mc "Okay."
            mc "{i}(My teacher? Not ours? So... She isn't a student?){/i}"
            mc "{i}(I'm totally screwed!){/i}"
            scene 01_276 with Dissolve(1)
            x "He's here."
            x "Thanks, Layla. You can head back to your seat."
            mc "{i}(Still don't know if she's a student or teacher... This is confusing.){/i}"
            jump Episode_2_Start

# Max Points:

# Alexis (6)
# Melissa (6)
# Layla (2)

# MC_GoodStudent (2)

# MC_Sex (1)
# MC_BJ (1)
# Alexis_Sex (1)

#WTAdded
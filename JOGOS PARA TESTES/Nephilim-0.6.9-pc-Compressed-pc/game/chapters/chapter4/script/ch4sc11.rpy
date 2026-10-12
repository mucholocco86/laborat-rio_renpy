label ch4sc11:

    window hide dissolve
    play music explore_1 fadein 1.0
    scene black with Dissolve (1.0)
    scene ch4sc11_001 with Dissolve(2.0)
    $ renpy.pause(1)
    "You and Kira proceed to row into Looter's Bay, Kira hasn't looked at you once."
    mc "Kira, I don’t know what you hope to achieve by doing this."
    mc "I just need you to drop me off at Inmortui as we agreed."
    scene ch4sc11_002 with dissolve
    "Kira still isn't able to look at you, she clearly feels somewhat guilty of her decision to bring you here."
    ki "..."
    scene ch4sc11_003 with dissolve
    ki "Look, you’re clearly going after something valuable."
    ki "Nobody just 'goes to Inmortui.' Even the most seasoned sailors avoid that place like the plague."
    scene ch4sc11_002 with dissolve
    ki "..."
    kit "He just needs to tell father what he's after and we can all get out of here, nobody gets hurt."
    mc "Kira, do you really think betraying me and taking me to your father will make me tell you anything of value?"
    scene ch4sc11_003 with dissolve
    ki "He’s not- I never told you that!"
    scene ch4sc11_002 with dissolve
    mc "It wasn’t that hard to figure out."
    scene ch4sc11_003 with dissolve
    ki "It doesn’t matter! Nothing I can say or do will be able to protect you from him."
    ki "So just tell him everything you know! Otherwise he's going to hurt you, I-I don't want that! So just tell him."
    scene ch4sc11_002 with dissolve
    mc "Congratulations, Kira."
    scene ch4sc11_004 with dissolve
    mc "You just broke my trust in you."
    "Kira stiffens up, clearly she's surprised by your words."
    mc "That might not seem like much to you. But is that how you repay my saving Kelly?"
    mc "Over the past week, I thought we'd developed a rapport. Not a friendship, as such."
    mc "But we had an understanding of each other, at least. A mutual respect."
    mc "Hell, had it been another week, we'd have become friends I dare say."
    scene ch4sc11_005 with dissolve
    kit "We did... we do! We are friends!"
    kit "Fuck, Kira. Nicely done!"
    kit "But there’s no going back now that we’re here... this is protocol, he doesn't get it..."
    kit "Nobody breaks fathers rules and remains unhurt, even us!"
    scene ch4sc11_012 with dissolve
    ki "[mc]... I do respect you-"
    scene ch4sc11_004 with dissolve
    with vpunch
    mc "{b}Shut it, Kira!{/b}"
    mc "{b}Look at me!{/b} Do you think I’m messing around?"
    mc "You want to know so badly what I’m after on Inmortui? Fine."
    scene ch4sc11_006 with dissolve
    mc "I’m looking for an artifact... an ancient relic in the shape of a chalice."
    mc "Supposedly, it was blessed or created by one of the seven divines called {b}Lucid{/b}."
    mc "I need to use it to heal someone close to me who has been hurt badly."
    scene ch4sc11_007 with dissolve
    mc "So, let me be very clear about this."
    scene ch4sc11_008 with dissolve
    mc "If you, your father, or anyone else gets in my way..."
    mc "I will kill them, and everyone else here."
    mc "I will burn Looter’s Bay to the ground and erase it from existence."
    scene ch4sc11_009 with dissolve
    ki "*Stuttering* Wha-What are y-you!?"
    ki "Your eyes!"
    scene ch4sc11_008 with dissolve
    mc "Do we understand each other?"
    scene ch4sc11_009 with dissolve
    ki "Y-Yes! We understand each other."
    scene ch4sc11_010 with dissolve
    ki "Its not like I want this either! But he- 'She stops herself'"
    ki "Arghh... it doesn’t matter."
    scene ch4sc11_011 with dissolve
    mc "You want his approval."
    mc "Since Pearl usually acts so carefree and spoiled, I'm guessing that she must be the favorite."
    scene ch4sc11_010 with dissolve
    ki "{b}NO!{/b} I... how did you?"
    scene ch4sc11_011 with dissolve
    ki "..."
    scene ch4sc11_012 with dissolve
    ki "*Sigh* Just once, you know... just once, I'd like him to notice me and my achievements."
    ki "I’m always busting my ass and managing the crew."
    ki "Keeping that scumbag, Louie, in line... ensuring that we have marks to plunder..."
    scene ch4sc11_010 with dissolve
    ki "And do I ever get a pat on the back in return?"
    ki "Even a ‘Well done, Kira. I’m proud of you’ would suffice."
    scene ch4sc11_012 with dissolve
    ki "By the sea! Listen to me whining like a little girl. Sorry."
    ki "Let’s just get this over with."
    scene ch4sc11_011 with dissolve
    mc "I get it…"
    mct "Maybe it could be worth showing her some good faith? She does seem regretful of her actions."
    ###Choice###
    menu:
        "Open up to her about your past.":
            scene ch4sc11_006 with dissolve
            mc "When I was ten summers old… My parents were murdered."
            scene ch4sc11_007 with dissolve
            mc "I... I was the one who found them."
            scene ch4sc11_004 with dissolve
            $ renpy.pause (1.5)
            mc "Their bodies were cold to the touch..."
            mc "There was blood all over them. Lots of wounds and deep cuts."
            mc "I was lucky a man appeared in the dark of night and took me with him."
            mc "He became something of a father figure to me, over the years."
            scene ch4sc11_005 with dissolve
            mc "But he wasn’t one to give praise freely, either."
            mc "So, yeah. I know what it’s like, Kira. That constant battle for approval."
            scene ch4sc11_003 with dissolve
            ki "[mc]... I-"
            ki "Thank you…"
            scene ch4sc11_002 with dissolve
            kit "Fuck. Experiencing that at the age of ten??"
            kit "I... I just want to hug him!"
            "Kira is surprised that you trusted her with your past, her trust increased by {size=+3}{b}{color=#2bff8b}2{/color}{/b}{/size}."
            $ kira_trust += 2
            kit "*Sigh* You really messed up this time, Kira."
            kit "The first man I ever befriend and I go behind his back... fuck! I hate this!"
            scene black with Dissolve(2)

        "Don’t trust her.":
            scene black with Dissolve(2)
            "You keep your past to yourself and soon arrive at the docks."

    scene ch4sc11_013 with Dissolve(2)
    $ renpy.pause (1)
    ki "What the hell are you doing?"
    mc "What does it look like I’m doing? I'm helping you up."
    scene ch4sc11_014 with dissolve
    ki "*Raises voice* I don’t need your help!"
    ki "I’m more than capable of handling myself."
    mc "Go on then."
    scene ch4sc11_015 with dissolve
    ki "You really think I can’t do it?"
    ki "Typical man! Always underestimating women!"
    scene ch4sc11_016 with dissolve
    kit "Hah! Does he really think I can’t climb a silly dock?"
    kit "He'll be eating barnacles for a week!"
    scene ch4sc11_017 with dissolve
    $ renpy.pause (1)
    kit "I’ve done this a thousand times…"
    scene ch4sc11_018 with dissolve
    ki "Aha! Told you it was easy!"
    ki "And you thought I needed help! Pffft!"
    "Amidst her boasting, her foot slips."
    scene ch4sc11_019 with dissolve
    ki "Huh?? {b}Oouuhhoh!{/b}"
    scene ch4sc11_020 with dissolve
    $ renpy.pause (0.2)
    with vpunch
    ki "{b}*Screams* Aaiiiiihh!{/b}"
    menu:
        "Catch her. ({color=#ff8cdd}Romance{/color})":
            scene ch4sc11_020 with dissolve
            $ kira_kiss = True
            scene ch4sc11_023 with dissolve
            with vpunch
            mc "Don’t worry, I’ve got you."
            ki "Don’t let go!"
            scene ch4sc11_024 with dissolve
            $ kira_path = True
            mc "Say it."
            scene ch4sc11_025 with dissolve
            ki "{b}*Shouting* S-Say what?!{/b}"
            ki "Just pull me up already!"
            scene ch4sc11_024 with dissolve
            mc "Aren’t you going to say please?"
            scene ch4sc11_025 with dissolve
            ki "What?! You fucker!"
            ki "I’m going to kill you!!"
            scene ch4sc11_026 with dissolve
            "You loosen your grip."
            with vpunch
            ki "{b}AaaiiHhh!!{/b}"
            ki "F-Fuck! Please!"
            ki "Please pull me up!"
            "In one swift motion, you pull her up effortlessly, as if she weighed nothing."
            scene ch4sc11_027 with dissolve
            "But she clings too tightly in her desperation, and you both tumble to the dock."
            ki "{b}Wuaah! Watch out!{/b}"
            scene ch4sc11_028 with dissolve
            with vpunch
            ki "I told you to watch out!"
            scene ch4sc11_029 with dissolve
            mc "It’s not my fault you weigh-"
            scene ch4sc11_030 with dissolve
            ki "Pick your next words very carefully."
            scene ch4sc11_031 with dissolve
            mc "Nothing! It felt like you weighed nothing at all."
            scene ch4sc11_032 with dissolve
            stop music fadeout 2
            $ renpy.pause (1.5)
            ki "..."
            kit "We're... so close!"
            ki "..."
            play music relax_2 fadein 1.0
            scene ch4sc11_033 with dissolve
            $ renpy.pause (1.5)
            "To your surprise, she swiftly leans down and presses her lips to yours."
            scene ch4sc11_033 with dissolve
            ki "Mnnhhh…"
            scene ch4sc11_034 with dissolve
            ki "NnhhHh…"
            "Her blade touches your throat as her soft lips keep engaging yours."
            scene ch4sc11_035 with dissolve
            $ renpy.pause (1.5)
            ki "*Moans softly* MnHnhh! Mhhhhh…"
            scene ch4sc11_036 with dissolve
            ######ANIMATION#####
            show kira_kiss1 with fade
            $ renpy.pause(2, hard=True)
            $ renpy.pause ()
            "Every time you think she's about to pull back, she surprises you by renewing the kiss more hungrily."
            ki "*Sensual moans* MhhnHhHh…"
            "You can feel her breathing quicken more with each kiss, and her grip tightening on your shoulder..."
            "And the warmth of her thighs as she straddles your hips and holds you down."
            ki "*Moans* Nnngghh... NhmmM!"
            "Her blade gently moves back and forth against your throat as your kisses become more intense."
            scene ch4sc11_031 with dissolve
            "Suddenly she breaks away."
            scene ch4sc11_030 with dissolve
            ki "A word of this to anyone, and I'll slit your throat in your sleep."
            scene ch4sc11_031 with dissolve
            mc "Sure."
            mc "You taste great, by the way."
            scene ch4sc11_030 with dissolve
            ki "I what?? Y-You really think you can charm me with honeyed words?"
            scene ch4sc11_031 with dissolve
            mc "I think you’ve already been charmed."
            mc "Considering that you’ve been straddling me for the last five minutes."
            scene ch4sc11_030 with dissolve
            ki "What? No- I... that’s not-"
            scene ch4sc11_031 with dissolve
            mc "Put your dagger away."

            if leadership >=3:
                scene ch4sc11_030 with dissolve
                ki "You don’t command me!"
                scene ch4sc11_031 with dissolve
                mc "Kiss me."
                scene ch4sc11_030 with dissolve
                ki "W-What!? Have you lost your mind-"
                scene ch4sc11_031 with dissolve
                mc "I said kiss me woman."
                scene ch4sc11_035 with dissolve
                "In disbelief of your bossiness, Kira leans down and merges her lips with yours once more."
                ki "*Kisses softly* Mmh-nnhh..."
                $ kira_trust += 1
                "Kira likes the back and forth between the two of you, her trust has increased by {size=+3}{b}{color=#2bff8b}1{/color}{/b}{/size}."
                scene ch4sc11_030 with dissolve
                ki "I-... I-"
                scene ch4sc11_031 with dissolve
                $ leadership += 1
                mc "Now, put away your blade, or you'll never get to kiss me again."
                scene ch4sc11_030 with dissolve
                ki "Ugh! Fine! But don't think I'm doing it because you ordered it..."
                ki "And don't even think for a second I did it because I want to kiss you again, that was a one time thing!"
                "You successfully managed to get Kira to fall in line, {b}{color=#ffee54}Leadership{/color}{/b} has increased by {size=+3}{b}{color=#2bff8b}1{/color}{/b}{/size}."

            else:
                scene ch4sc11_030 with dissolve
                "You didn't have enough Leadership experience to pass the check."
                ki "I should cut your throat for kissing me like that... let alone for barking orders at me."
                scene ch4sc11_031 with dissolve
                mc "*Chuckles* I kissed you? Sure..."
                mc "Let me put it this way, if you accidentially cut my throat, a kiss like that won't happen again."


            scene ch4sc11_030 with dissolve
            "'Hesitantly, she finally removes the dagger from your throat.'"
            scene ch4sc11_028 with dissolve
            ki "Happy?"
            mc "Almost, just need to adjust something."
            scene ch4sc11_027b with dissolve
            with vpunch
            "You effortlessly lifts her up into the air as if she weighs nothing."
            ki "{b}*Squeals* AiiyhHh!{/b}"
            ki "{b}*Laughs* S-Stop!{/b} It tickles!"
            scene ch4sc11_027c with dissolve
            "After a few more pokes at her sides you put her down."
            mc "Now, would you look at that! You actually can laugh!"
            scene ch4sc11_027d with dissolve
            ki "*Mutters* Jackass."
            "Kira enjoyed being able to relax and laugh with you, her trust has increased by {size=+3}{b}{color=#2bff8b}2{/color}{/b}{/size}."
            scene ch4sc11_027e with dissolve
            mc "C’mon. Let’s go talk to this father of yours."
            scene ch4sc11_027c with dissolve
            ki "..."
            $ kira_trust += 2
            pl "Kira! There you are. You guys went ashore fast!"
            scene ch4sc11_027f with dissolve
            with vpunch
            ki "{b}*Shouts* N-Nothing happened!!{/b}"
            pl "Was that [mc]? And were you laughing-"
            ki "Shut up and let’s go! I need some of Father’s rum."
            scene black with Dissolve(1.5)

        "Let her fall.":
            scene ch4sc11_021 with dissolve
            ki "Owh! Owwwh!"
            scene ch4sc11_022 with dissolve
            ki "Not a word! If you ever speak about this to anyone... I’ll-"
            mc "You’ll feed me to the sharks. Yeah, yeah. I get it."
            scene black with Dissolve(1.5)


    scene ss1 with Dissolve(1.5)
    stop music fadeout 2
    $ renpy.pause ()
    scene ch4sc11_037 with Dissolve(1.5)
    play music summon_3 fadein 1.0
    el "Stupid rock!"
    scene ch4sc11_038 with dissolve
    el "Why won’t you work… Just light up already!"
    el "I want to talk to him!"
    scene ch4sc11_039 with dissolve
    br "Eliza? Ye in there?"
    el "..."
    scene ch4sc11_040 with dissolve
    el "Go away Borri."
    scene ch4sc11_039 with dissolve
    br "C’mon, lass. I’m heading over te the guild."
    br "Sylph won’t stop nagging me te bring yer bum over there."
    br "Even Dalen has asked te speak with ye."
    scene ch4sc11_040 with dissolve
    el "I don’t want to see anyone right now."
    scene ch4sc11_039 with dissolve
    with vpunch
    br "Blasted!"
    scene ch4sc11_041 with dissolve
    br "Yer coming with me, lass!"
    br "It’s been a week already. Sylph said she has something that'll cheer ye right up!"
    scene ch4sc11_040 with dissolve
    el "Has she heard anything about [mc]?"
    scene ch4sc11_039 with dissolve
    br "Naye. I’m afraid that's not what she was talking about."
    scene ch4sc11_040 with dissolve
    el "Then I’m not interested…"
    scene ch4sc11_041 with dissolve
    br "Lass, are ye really going te sit here and wallow in self-pity?"
    br "[mc] is out there right now..."
    br "For ye. For both of ye. So that ye can achieve y'goals, together."
    scene ch4sc11_039 with dissolve
    br "Shouldn’t ye be doing the same here?"
    br "Working towards something that'll benefit ye both when he returns?"
    scene ch4sc11_042 with dissolve
    elt "He’s right."
    elt "I should be doing something useful while he’s away... something that'll benefit us both."
    elt "But what? Hnnnhhmm…"
    stop music fadeout 2
    scene ch4sc11_043 with dissolve
    elt "I know! I'll see what work Sylph has for me!"
    play music tavern_2 fadein 1.0
    elt "That way, I can earn coin towards getting us our own place to call home."
    scene ch4sc11_044 with dissolve
    elt "Maybe I can even earn enough to buy him a gift as well!"
    elt "*Giggles* I’m sure he'll complain about it at first..."
    elt "But deep down, I know he'll appreciate it."
    scene ch4sc11_041 with dissolve
    br "Ahh! There’s that cheerful expression I've been lookin fer!"
    br "I take it yer ready te go see Sylph?"
    scene ch4sc11_044 with dissolve
    $ renpy.pause (1)
    scene ch4sc11_045 with dissolve
    el "OK! Let’s go!"
    scene black with Dissolve(2)
    $ renpy.pause (1)
    scene ch4sc11_046 with Dissolve(2)
    el "So, did Sylph mention what she needed me for?"
    scene ch4sc11_047 with dissolve
    br "Not te me…"
    br "That little pixie is sure te have something of interest t'ye, though."
    scene ch4sc11_046 with dissolve
    el "What makes you think that?"
    scene ch4sc11_047b with dissolve
    uk "He will return! Don’t sit idly by, prepare for his return!"
    uk "Come one, come all, to the Church of Embers and receive his blessing!"
    scene ch4sc11_047 with dissolve
    br "Ugh…. Those damned fanatics are getting worse."
    scene ch4sc11_046 with dissolve
    el "C’mon, Borri! Don’t change the subject. Tell me already!"
    scene ch4sc11_047 with dissolve
    br "Sorry, lass. Ye'll have to wait and see."
    br "All I know is... she were adamant about bringing ye by as soon as possible."
    br "Heh. Wouldn’t stop pestering me about it all morning!"
    scene ch4sc11_046 with dissolve
    el "She can be a little excitable."
    br "Aye... like a certain someone me knows..."
    el "Alright, alright..."
    el "Borri. Onwards to glory!"
    scene black with Dissolve(2)
    $ renpy.pause (1)
    scene ch4sc11_048 with Dissolve(2)
    with vpunch
    el "{b}*High pitched* Aiiih! Borri! Don’t drop me!{/b}"
    br "By Malpheon’s hammer! Quit yer wiggling!"
    with vpunch
    br "Yer acting like a fish outta water!"
    scene ch4sc11_049 with dissolve
    el "As if! I happen to be good at sitting on shoulders! The best even!"
    scene ch4sc11_048 with dissolve
    br "Hah! Ye been sitting on lots of shoulders, have ye?"
    scene ch4sc11_049 with dissolve
    el "No. Only [mc]’s!"
    scene ch4sc11_050 with dissolve
    elt "I really want to sit on his shoulders again."
    elt "Or have him call me a monkey when I cling to his back."
    scene ch4sc11_051 with dissolve
    $ renpy.pause ()
    scene ch4sc11_052 with dissolve
    br "Hey. None of that! We have work to do, remember?"
    scene ch3sc20_018 with dissolve
    sy "We’re closed for the day! You can come back tomo-"
    scene ch3sc20_020 with dissolve
    sy "Eliza!! You’re here!"
    scene ch4sc11_053 with dissolve
    el "*Sniff* ..."
    scene ch3sc20_031 with dissolve
    sy "Borri, please be so kind as to put her on the desk."
    scene ch4sc11_052 with dissolve
    br "Yes ma’am."
    scene ch4sc11_054 with dissolve
    br "I’ll leave yer to it, then. I’ll be checking that contract ye handed me this morning."
    scene ch4sc11_055 with dissolve
    $ renpy.pause ()
    scene ch4sc11_056 with dissolve
    el "So, what do you have for me, Sylph?"
    el "Borri said it was urgent?"
    scene ch4sc11_057 with dissolve
    sy "Urgent? Oh, gosh! Nothing of the sort."
    scene ch4sc11_058 with dissolve
    sy "Heheheh. I suppose I might have embellished a little!"
    sy "But only to make sure Borri would hurry up! You know how dwarves can be."
    scene ch4sc11_057 with dissolve
    sy "I have a surprise for you!"
    scene ch4sc11_056 with dissolve
    el "A surprise?"
    scene ch4sc11_057 with dissolve
    sy "Yuuup! You’re going to love it! And best of all, it’s low risk!"
    sy "There’s only a teeny-tiny, itsy-bitsy chance that you might spontaneously combust!"
    scene ch4sc11_056 with dissolve
    el "Spontaneously combust? What the-"
    scene ch4sc11_057 with dissolve
    sy "Relax, you worry-bug!"
    sy "Don’t you know worrying promotes wrinkles!"
    scene ch4sc11_059 with dissolve
    elt "Wrinkles?"
    sy "Weren’t you listening to me?"
    elt "It’s only a tiny, tiny, pretty-much nonexistent chance!"
    scene ch4sc11_060 with dissolve
    sy "And you'll be able to move again!"
    elt "M-Move again?!"
    scene ch4sc11_061 with dissolve
    el "Do it!"
    el "I don’t care about the risk! As long as I can move again."
    scene ch4sc11_057 with dissolve
    sy "Great! Just close your eyes and be patient."
    scene ch4sc11_062 with dissolve
    el "O-Okay. Go on, surprise me."
    scene ch4sc11_063 with dissolve
    sy "Sit tight! Heheheh."
    stop music fadeout 2
    scene ch4sc11_064 with dissolve
    play music feels_3 fadein 1.0
    $ renpy.pause (1.3)
    scene ch4sc11_065 with dissolve
    $ renpy.pause ()
    scene ch4sc11_066 with dissolve
    $ renpy.pause ()
    scene ch4sc11_067 with dissolve
    sy "Okay, here we go…"
    scene ch4sc11_068 with dissolve
    syt "Please, Earth-mother. Let this work. She deserves a win."
    syt "She needs this."
    scene ch4sc11_069 with dissolve
    "Sylph focuses intently trying to manifest some of her magic."
    scene ch4sc11_070 with dissolve
    "Squishing the magical essence with her hands, Sylph carefully shapes it into a sphere."
    scene ch4sc11_071 with dissolve
    "Then casts it towards Eliza..."
    scene ch4sc11_072 with dissolve
    $ renpy.pause (1.3)
    scene ch4sc11_073 with dissolve
    $ renpy.pause (1.3)
    scene ch4sc11_074 with dissolve
    "As the magical sphere reaches Eliza, it suddenly lights up and engulfs her."
    scene ch4sc11_075 with dissolve
    "Eliza suddenly begins to levitate as she is infused with Sylphs magic."
    stop music fadeout 2
    scene ch4sc11_076 with dissolve
    el "S-Sylph! What’s happening!?"
    el "A-Am I spontaneously combusting?!"
    play music relax_2 fadein 1.0
    scene ch4sc11_077 with dissolve
    sy "*Laughs* Hahhah! Goodness, that’s not even a thing! At least not with nature magic."
    sy "I'd never put you in danger. Besides, if you haven’t noticed..."
    scene ch4sc11_078 with dissolve
    sy "I’m totally awesome at magic!"
    sy "Now, fly!"
    scene ch4sc11_076 with dissolve
    el "F-Fly?!"
    scene ch4sc11_079 with dissolve
    el "What do you mean? I don’t know how to fly, Sylph!"
    scene ch4sc11_078 with dissolve
    sy "Sure you do! I cast a levitation spell on you. As long as I’m nearby, my magic will help you fly!"
    sy "Just think of it like you're swimming!"
    scene ch4sc11_079 with dissolve
    el "I suppose it does feel a little like I’m floating in water..."
    scene ch4sc11_080 with dissolve
    el "So I just move around like this?"
    "Eliza begins twisting her torso and moving her arms."
    scene ch4sc11_081 with dissolve
    $ renpy.pause (1.5)
    scene ch4sc11_082 with dissolve
    el "Sylph! I’m moving! I-I’m actually moving!!"
    scene ch4sc11_083 with dissolve
    sy "Yuuuup! I told you! Now try to make some larger movements, don’t be afraid to lose balance."
    scene ch4sc11_084 with dissolve
    sy "Yes! Just like that! You’ll be a flying champion before long!"
    scene ch4sc11_085 with dissolve
    sy "That’s it! Be free!"
    scene ch4sc11_086 with dissolve
    $ renpy.pause ()
    scene ch4sc11_087 with dissolve
    el "I’m doing it, Sylph! I’m actually flying!"
    scene ch4sc11_088 with dissolve
    el "Hey, Sylph? Wanna race?"
    scene ch4sc11_089 with dissolve
    sy "*Giggles* Someone's feeling mighty invincible, huh?"
    sy "How about you just spend today getting used to the feeling of being airborne!"
    sy "Once we know you can handle yourself without crashing into everything, then we can have a race! Yuup!"
    scene ch4sc11_090 with dissolve
    el "This is so much fun! I could do this every day!"
    el "Hey, Sylph? Do you think [mc] is capable of flying?"
    scene ch4sc11_091 with dissolve
    sy "Hmhh. I haven't really thought about it before."
    sy "He has an incredible amount of magic flowing through his veins."
    sy "Far more than I’ve felt in anyone else. More than the high mages of the conclave..."
    sy "And more than the elder council of the elves in the riverlands. None of them have that kind of magic."
    scene ch4sc11_092 with dissolve
    el "He’s special!"
    scene ch4sc11_093 with dissolve
    sy "Yeah. He is. But what kind of special? He can’t be human."
    sy "But he looks like a human."
    sy "Maybe he's disguised himself using an illusion spell."
    scene ch4sc11_094 with dissolve
    el "Oh. I thought Dalen would have told you by now."
    el "[mc] is a Nephilim."
    syt "N-Nephilim?! H-He’s half angel-"
    scene ch4sc11_092 with dissolve
    el "A Nephilim is a child of an angel and human."
    el "Pretty amazing, right?"
    scene ch4sc11_094 with dissolve
    sy "..."
    scene ch4sc11_095 with dissolve
    sy "Eliza... Angels aren’t kind or good."
    sy "They aren’t like the books describe, okay?"
    scene ch4sc11_094 with dissolve
    el "What are you talking about?"
    scene ch4sc11_095 with dissolve
    sy "Angels... they're beings of order."
    scene ch4sc11_096 with dissolve
    sy "They've been battling creatures of chaos for as long as Midomir has existed. Probably longer."
    sy "They're ruthless warriors. And they don’t come to answer the prayers of the innocent..."
    sy "They only appear when there are beings of chaos for them to eradicate."
    scene ch4sc11_094 with dissolve
    el "Sylph... [mc] isn't like that."
    syt "I want to believe her... He has been kind to me. But a half-angel?"
    syt "Earth-mother, what do I do?"
    scene ch4sc11_096 with dissolve
    sy "I’ve crossed paths with an angel once before. He came to our home in the riverlands ..."
    scene ch4sc11_095 with dissolve
    sy "M-My sister had gotten into some bad magic..."
    sy "But instead of helping her, or at least capturing her..."
    scene ch4sc11_096 with dissolve
    sy "He... he obliterated our entire enclave of fae."
    sy "I only survived because I was out looking for ingredients at the time."
    scene ch4sc11_097 with dissolve
    $ renpy.pause ()
    scene ch4sc11_098 with dissolve
    el "Sylph..."
    el "I had no idea. I’m so sorry that happened to you."
    scene ch4sc11_097 with dissolve
    $ renpy.pause ()
    scene ch4sc11_098 with dissolve
    el "But you know [mc]! You have to know he is nothing like that. He protects the ones he cares about!"
    scene ch4sc11_099 with dissolve
    el "You can’t judge him just because he was born to be what he is."
    el "No one can control that."
    scene ch4sc11_098 with dissolve
    el "You can only judge him by his actions."
    scene ch4sc11_093 with dissolve
    sy "*Sigh* It’s not that simple, Eliza. I can’t just forget what happened to my people."
    sy "I'll be keeping an eye on him once he gets back. No, both eyes!"
    scene ch4sc11_094 with dissolve
    el "Great! You'll see that all your worries are for nothing."
    scene ch4sc11_093 with dissolve
    sy "I hope you’re right. I really do."
    "Eliza flies off."
    scene ch4sc11_090 with dissolve
    el "So, what are we doing today?"
    scene black with Dissolve(2)
    scene ss22 with Dissolve(2)
    $ renpy.pause ()
    scene ch4sc11_100 with Dissolve(2)
    $ renpy.pause (1.5)
    al_t "I’ve been attending the Academy for about a week now, and these buildings still amaze me."
    al_t "We don’t have anything as fancy as them back in Riverside…"
    scene ch4sc11_101 with dissolve
    al_t "[mc]... I wish you were here."
    al_t "*Sigh* Focus up! I need to find a way to help Eliza."
    scene ch4sc11_102 with dissolve
    with vpunch
    uk "{b}*Shouting* Watch out!!{/b}"
    al "*Startled* Wha-"
    scene ch4sc11_103 with dissolve
    $ renpy.pause (1.5)
    scene ch4sc11_104 with dissolve
    $ renpy.pause (1.5)
    scene ch4sc11_105 with dissolve
    uk "OuuwHhAaaa!"
    scene ch4sc11_106 with dissolve
    $ renpy.pause (1.5)
    scene ch4sc11_107 with dissolve
    with vpunch
    uk "Owwhh..."
    scene ch4sc11_108 with dissolve
    al "*Groans* Urrgh..."
    uk "Huurhhh…"
    scene ch4sc11_109 with dissolve
    uk "Oh my god! Are you alright? I totally squished you!"
    uk "So sorry! I'm in a terrible rush!"
    scene ch4sc11_110 with dissolve
    uk "Master always tells me not to race around."
    uk "But I have to talk to professor Venetos as soon as possible!"
    scene ch4sc11_111 with dissolve
    uk "Speaking of... gotta go! Hope to see you around!"
    scene ch4sc11_112 with dissolve
    al_t "*Grunts* Ughh. What in the five hells?"
    al_t "Great way to start the day... getting trampled by a witch! Can't she just fly a broom?"
    al_t "Who was she anyway? I feel like I’ve seen her around in class."
    scene ch4sc11_113 with dissolve
    al_t "She mentioned Professor Venetos."
    al_t "I’m supposed to attend an alchemy class today with her. Perhaps she’ll be there?"
    al_t "I suppose I’ll find out later. Better get going before I end up late myself."
    scene black with Dissolve(2)
    $ renpy.pause (1)
    scene ch4sc10_011 with Dissolve(2)
    $ renpy.pause ()
    scene ch4sc11_114 with dissolve
    al_t "Yeah, that’s definitely her!"
    al_t "I wonder why she was in such a rush this morning?"
    scene ch4sc11_115 with dissolve
    pv "Do you find my class boring, Alice?"
    scene ch4sc11_116 with dissolve
    al "Hmm? No! Not at all!"
    al "I-I was just-"
    scene ch4sc11_117 with dissolve
    pv "No excuses, Alice."
    pv "Pay attention, going forward. If you don’t know which ingredients to mix in the future, you could kill someone."
    scene ch4sc11_118 with dissolve
    al "Y-Yes Professor…"
    scene black with Dissolve(2)
    scene ss2 with dissolve
    $ renpy.pause ()
    scene ch4sc11_119 with Dissolve(2)
    al "*Sighs heavily* Hrraahh. How am I ever going to remember all these plant species?!"
    al "[mc]... I need you."
    al "You always knew what to say to cheer me up."
    scene ch4sc11_120 with dissolve
    uk "Who are you talking to?"
    scene ch4sc11_121 with dissolve
    al "Huh?? No one."
    al "Hey, aren’t you the-"
    scene ch4sc11_122 with dissolve
    uk "The girl who so rudely trampled you this morning?"
    uk "That would be me. I’m terribly sorry about that."
    scene ch4sc11_123 with dissolve
    $ renpy.pause (1)
    scene ch4sc11_122 with dissolve
    lu "I’m Luna by the way."
    lu "I hope we can be friends."
    scene ch4sc11_117 with dissolve
    pv "Luna, please wait in my office."
    pv "I just need a little chat with Alice before we continue our project."
    scene ch4sc11_122 with dissolve
    lu "Bye bye, Alice."
    scene ch4sc11_124 with dissolve
    pv "Alice..."
    pv "You’ve been here for a week now. And I’ve yet to see you really dive into the subjects we are learning."
    scene ch4sc11_125 with dissolve
    pv "Would you care to explain why you’re not properly focused on your studies?"
    scene ch4sc11_126 with dissolve
    al "I..."
    al "I know I’ve been absent-minded since I started, Professor."
    al "It’s just... learning to mix elixirs of giant growth, or Jinglejuice potions... they're not why I came here."
    al "I-"
    scene ch4sc11_127 with dissolve
    "Alice pauses for a brief moment before continuing."
    scene ch4sc11_126 with dissolve
    al "I came here because I want to help a friend."
    al "She was severely injured recently, and I want to help her get better."
    scene ch4sc11_128 with dissolve
    pv "I see. Alice, unfortunately, healing potions can only be used to treat fresh wounds."
    pv "They need to be applied as soon as the wound is inflicted."
    pv "I’ve studied alchemy and herbology for my entire life, and let me tell you something."
    pv "Even if there isn't a potion that can solve your friend's problem right now..."
    scene ch4sc11_129 with dissolve
    pv "You can still learn recipes for hundreds of different potions and elixirs for all kinds of purposes."
    pv "They all have their uses. If you put your mind to it and learn to craft them, then you'll have a valuable skill that few possess."
    pv "And I have a feeling you'll have many occasions where you'll be able to help your friends in the future."
    scene ch4sc11_126 with dissolve
    al "I see..."
    scene ch4sc11_129 with dissolve
    pv "You should take the rest of the day off and think about what you really want to do."
    pv "Come back tomorrow with a clear mind. And I promise, you'll be able to make a difference in many lives."
    scene ch4sc11_126 with dissolve
    al "Thank you, Professor. I apologize for not paying attention."
    scene ch4sc11_128 with dissolve
    pv "Don’t worry about it, Alice. We all get a little lost sometimes."
    pv "As a Professor and a mentor, I try to set my students on a path that will serve them well in life."
    pv "And honestly, I think I see a little of myself in you."
    scene ch4sc11_130 with dissolve
    pv "You're free to go. I have to work on a project with Luna."
    scene black with Dissolve(2)
    $ renpy.pause(1)
    scene ch4sc11_131 with Dissolve(2)
    al_t "..."
    al_t "I don’t know what I was expecting…"
    scene ch4sc11_132 with dissolve
    al_t "Did I really think it would be that easy to help her?"
    al_t "That I could just waltz right in to the Academy, and learn to cure serious injuries in only a week?"
    scene ch4sc11_133 with dissolve
    al_t "Professor Venetos was right, though. Even if I can't help this time, learning alchemy would be useful later."
    al_t "Being able to support [mc] on his quests with a wide array of elixirs would definitely be worthwhile."
    al_t "Maybe he'd even take me along on a quest!"
    scene ch4sc11_132 with dissolve
    al_t "Speaking of... I wonder what he’s doing?"
    stop music fadeout 2
    scene black with Dissolve(2)
    jump ch4sc12

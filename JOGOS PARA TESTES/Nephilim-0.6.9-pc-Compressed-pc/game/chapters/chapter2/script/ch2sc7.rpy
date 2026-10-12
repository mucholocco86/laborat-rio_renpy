#Start Chaper
label ch2sc7:

    #play music morning_1

    # start scene 2
        window hide dissolve
        play music explore_1 fadein 2.0
        scene black with Dissolve (2.0)
        scene ch2sc7_01 with Dissolve(2.0)
        $ renpy.pause()
        window show dissolve
        scene ch2sc7_01 with dissolve
        mc "..."
        scene ch2sc7_02 with dissolve
        mct "What’s taking her so long?"
        scene ch2sc7_03 with dissolve
        mct "Thinking she can defeat me..."
        mct "*Chuckles* She’s very headstrong, I’ll give her that."
        scene ch2sc7_04 with dissolve
        mct "Then again, she did manage to put that creep Rammus on his ass."
        scene ch2sc7_03 with dissolve
        mct "His face was priceless when he realized it was a girl who had put him down."
        scene ch2sc7_04 with dissolve
        mct "Where we’re going, she will need that feistiness of hers."
        mct "But I have to remember that she’s untrained, no matter how eager she is. I shouldn’t go too hard on her..."
        scene ch2sc7_04_5 with dissolve
        mct "Speaking of the little vixen..."
        scene ch2sc7_05 with dissolve
        $ renpy.pause(1)
        el "[mc]? Ah..."
        scene ch2sc7_06 with dissolve
        el "There you are!"
        el "You ready to be defeated by a girl?"
        scene ch2sc7_07 with dissolve
        mc "Hey... you good?"
        scene ch2sc7_08 with dissolve
        $ renpy.pause(1)
        scene ch2sc7_09 with dissolve
        $ renpy.pause(1)
        scene ch2sc7_08 with dissolve
        $ renpy.pause(1)
        "Eliza nods with a soft giggle"
        scene ch2sc7_10 with dissolve
        mc "Okay. Come on, I know a place."
        scene ch2sc7_11 with dissolve
        el "Lead the way mas-"
        scene ch2sc7_12 with dissolve
        $ renpy.pause(1)
        el "*Bites lip* Nhh!"
        scene ch2sc7_13 with dissolve
        mc "You almost said it again."
        scene ch2sc7_14 with dissolve
        el "No! I DID NOT!"
        el "I-I was going to say..."
        scene ch2sc7_15 with dissolve
        $ renpy.pause()
        scene ch2sc7_16 with dissolve
        el "Hrrrh."
        scene ch2sc7_17 with dissolve
        mc "Try to keep up."
        ####Choice###
        menu:
            "Be playful. ({color=#87e1fa}Charisma{/color})":
                mc "Usually you’re as slow as a turtle on dry land."
                scene ch2sc7_14 with dissolve
                el "T-Turtle!?"
                scene ch2sc7_16 with dissolve
                mc "A slow one at that... Move your butt!"
                $ charisma += 1
                "You ruffled Eliza's feathers, your {b}{color=#87e1fa}Charisma{/color}{/b} has increased by {size=+3}{b}{color=#2bff8b}1{/color}{/b}{/size}."
                elt "{b}Jerk!{/b}"
                elt "..."
                elt "Hnngh, I'm going to kick his butt and then he can be the turtle! No- Tortoise! Mh!"


            "Inspire her. ({color=#ffee54}Leadership{/color})":
                mc "C'mon, don't you want a chance to 'kick my ass'?"
                scene ch2sc7_16 with dissolve
                elt "Hmhp! I do want to whoop his butt indeed!"
                mc "C'mon, I'm excited to see what you've got."
                mc "If you do well, I'll buy you dinner."
                scene ch2sc7_14 with dissolve
                el "D-Did you say dinner!? L-Like a date!?"
                scene ch2sc7_17 with dissolve
                mc "Who knows? Do well and find out."
                $ leadership += 1
                "You managed to inspire Eliza to do her best, your {b}{color=#ffee54}Leadership{/color}{/b} has increased by {size=+3}{b}{color=#2bff8b}1{/color}{/b}{/size}."


        scene ch2sc7_18 with dissolve
        el "H-Hey wait up!"
        stop music fadeout 2.0
        scene black with Dissolve(3)
        "A short walk away from Riverside, you reach a secluded area fit for practicing."
        scene ch2sc7_19 with dissolve
        play music outdoors_1 fadein 2.0
        mc "This is the spot."
        scene ch2sc7_20 with dissolve
        el "Great! So... what are you teaching me today?"
        scene ch2sc7_21 with dissolve
        mc "We’ll start with some hand-to-hand combat."
        scene ch2sc7_22 with dissolve
        mc "You won’t always have a weapon nearby. Being able to defend yourself without a weapon is valuable."
        scene ch2sc7_23 with dissolve
        el "Makes sense."
        scene ch2sc7_24 with dissolve
        el "Okay. Turn me into a deadly weapon that our enemies will fear!"

        if eliza_relationship == True:
            scene ch2sc7_25 with dissolve
            mc "Easy, kitten."
            mc "Why don’t you try to attack me first?"
            scene ch2sc7_26 with dissolve
            elt ".."
            elt "....."
            elt "........."
            elt "Kitten?"
            elt "He... he's given me a nickname? I-..."
            scene ch2sc7_27 with dissolve
            with vpunch
            stop music fadeout 2.0
            elt "No! {size=+5}{b}FOCUS!{/b}{/size} This is not the time to let him get under your skin."
            scene black with Dissolve(1.5)

        else:
            scene ch2sc7_25 with dissolve
            stop music fadeout 2.0
            mc "Why don’t you try to attack me first? Then we can judge how much of a *deadly weapon* you are."
            scene black with Dissolve(1.5)

        scene ch2sc7_28 with dissolve
        el "Alright, here I come!"
        scene ch2sc7_29 with dissolve
        play music action_1 fadein 2.0
        "She makes a fast dash towards you."
        scene ch2sc7_30 with dissolve
        "Just before she reaches you, she leaps into the air."
        scene ch2sc7_31 with dissolve
        mct "Heh. Too obvious."
        scene ch2sc7_32 with dissolve
        "You steady yourself, preparing for impact."
        scene ch2sc7_33 with dissolve
        with vpunch
        "You manage to catch her, which clearly surprises her."
        scene ch2sc7_34 with dissolve
        "In one quick move, you toss her into a bunch of leaves to soften her landing."
        stop music fadeout 2.0
        scene ch2sc7_35 with dissolve
        elt "Uurrrhh... I didn’t think he'd be able to catch me mid-air like that."
        play music explore_2 fadein 2.0
        scene ch2sc7_36 with dissolve
        mc "You good?"
        scene ch2sc7_37 with dissolve
        el "Y-Yeah. You just got lucky!"
        el "Wipe that smirk! I'm just warming up!"
        stop music fadeout 2.0
        scene ch2sc7_36 with dissolve
        mc "*Chuckles* Sure."
        mc "Now get up."
        scene ch2sc7_38 with dissolve
        with vpunch
        play music action_1 fadein 2.0
        el "Let’s go again!"
        scene ch2sc7_39 with dissolve
        $ renpy.pause()
        scene ch2sc7_40 with dissolve
        $ renpy.pause()
        scene ch2sc7_41 with dissolve
        $ renpy.pause()
        scene ch2sc7_42 with dissolve
        $ renpy.pause()
        scene ch2sc7_43 with dissolve
        $ renpy.pause()
        scene ch2sc7_44 with dissolve
        $ renpy.pause()
        scene ch2sc7_45 with dissolve
        $ renpy.pause()
        scene ch2sc7_46 with dissolve
        $ renpy.pause()
        scene ch2sc7_47 with dissolve
        $ renpy.pause()
        stop music fadeout 2.0
        scene ch2sc7_48 with dissolve
        mc "..."
        play music outdoors_1 fadein 2.0
        scene ch2sc7_49 with dissolve
        mc "Are you serious?"
        scene ch2sc7_50 with dissolve
        el "Do you surrender?"
        scene ch2sc7_51 with dissolve
        mc "Why would I do that?"
        scene ch2sc7_52 with dissolve
        el "Because I’ve got you in my special death grip!"
        el "The only way out is surrendering!"
        scene ch2sc7_51 with dissolve
        mc "How about you climb down and we call it a day?"
        scene ch2sc7_50 with dissolve
        el "Great!"
        el "I knew you wouldn’t be able to resist my death grip for long."
        scene ch2sc7_48 with dissolve
        mct "She was able to grab me mid-air as I was vaulting her?"
        mct "She's nimble, I’ll give her that."
        scene ch2sc7_53 with dissolve
        mc "Okay..."
        mc "Let’s rest over there."
        scene ch2sc7_54 with dissolve
        elt "*Snickers* This is my chance to get him!"
        scene ch2sc7_55 with dissolve
        $ renpy.pause()
        scene ch2sc7_56 with dissolve
        with vpunch
        $ renpy.pause()
        scene ch2sc7_57 with dissolve
        el "No way! H-How?"
        scene ch2sc7_58 with dissolve
        elt "How could he catch my punch like that! Without even seeing me?"
        scene ch2sc7_56 with dissolve
        mc "I sensed you."
        scene ch2sc7_59 with dissolve
        el "Huh..?"
        el "What do you mean 'you sensed me'?"
        scene ch2sc7_60 with dissolve
        mc "It’s just a feeling I get when something is about to happen."
        scene ch2sc7_61 with dissolve
        el "Mmh... that’s pretty odd."
        el "Have you always been able to 'sense' like that?"
        scene ch2sc7_60 with dissolve
        mc "No, it started happening in my early teen years."
        scene ch2sc7_62 with dissolve
        mc "At first I didn't pay any attention to it."
        mc "But as training with my mentor got more intense..."
        scene ch2sc7_60 with dissolve
        mc "... it started to happen more frequently."
        stop music fadeout 2.0
        scene ch2sc7_59 with dissolve
        el "Do you think it’s related to what happened to you during the encounter with Rammus and Irene?"
        scene ch2sc7_60 with dissolve
        mc "At this point, I wouldn’t be surprised."
        play music explore_2 fadein 2.0
        scene ch2sc7_63 with dissolve
        el "So... you’ve got some sort of power or ability?"
        el "And you were born with it?"
        scene ch2sc7_60 with dissolve
        mc "As far as I have been able to figure out, yeah."
        mc "I honestly don't know too much..."
        scene ch2sc7_62 with dissolve
        mc "Nothing ever happened before... my parents."
        mc "But after that night... I've gradually been able to do... certain things."
        scene ch2sc7_64 with dissolve
        el "Hmm... your parent's deaths must've activated something within you."
        el "If you were a mage, you'd have known as early as being able to walk."
        scene ch2sc7_68 with dissolve
        mc "Does it bother you? Knowing that I'm... different."
        scene ch2sc7_65 with dissolve
        el "..."
        el "No."
        scene ch2sc7_70 with dissolve
        mc "You think I’m a freak, right?"
        mc "You wouldn’t be the first to feel that way."
        scene ch2sc7_65 with dissolve
        $ renpy.pause(1)
        scene ch2sc7_66 with dissolve
        el "You’re wrong."
        scene ch2sc7_70 with dissolve
        mc "Yes, you-"
        scene ch2sc7_67 with dissolve
        with vpunch
        el "{b}[mc]!{/b} I swear by the divines! If you don’t shut up, {b}I-I’m really going to punch you.{/b}"
        scene ch2sc7_68 with dissolve
        mc "Okay, okay."
        mc "So my abilities or whatever they are, they don’t bother you?"
        scene ch2sc7_69 with dissolve
        el "No, they don't bother me. Do you really think so little of me?"
        scene ch2sc7_71 with dissolve
        mc "No, Eliza. It’s ... it's just not something I've shared with anyone before."
        mct "Rin is the only person who knows and has accepted me..."
        mc "I'm not sure how people will react to hearing about it."
        scene ch2sc7_72 with dissolve
        mc "I suspect that most would see me as a freak of nature, maybe start shouting 'devil spawn' and try to drag me off to the gallows."
        scene ch2sc7_66 with dissolve
        el "You're not... you're not any of those things."
        scene ch2sc7_59 with dissolve
        el "You'd better not believe it if someone says anything like that."
        scene ch2sc7_72 with dissolve
        mc "Eliza..."
        mc "Even I don't fully understand what I am."
        mc "What does being a Nephilim really mean?"
        scene ch2sc7_73 with dissolve
        el "I can't claim to know anything about being a Nephilim, either."
        el "I've never even heard that word?"
        el "But I do know you, and you're definitely not a 'devil spawn'."
        scene ch2sc7_74 with dissolve
        mc "You don’t know..."
        scene ch2sc7_75 with dissolve
        el "I do! I do know. In my eyes, you’re just [mc]... My friend."
        el "My... savior."
        stop music fadeout 2.0
        scene ch2sc7_76 with dissolve
        el "You might be a jerk sometimes. And clearly thickheaded!"
        el "But I trust you completely, if it isn’t obvious by now."
        scene ch2sc7_77 with dissolve
        mc "I trust you too, Eliza."
        play music outdoors_1 fadein 2.0
        mc "Thank you for the vote of confidence."
        scene ch2sc7_78 with dissolve
        el "Anytime. 'Cause I’m not going anywhere."
        scene ch2sc7_79 with dissolve
        $ renpy.pause(1)
        mct "*Chuckles* She... really does accept me as I am."
        scene ch2sc7_80 with dissolve
        $ renpy.pause(1)
        elt "Stop looking at me like that..."
        scene ch2sc7_81 with dissolve
        el "Uhh... we'd better get back to it."
        scene ch2sc7_82 with dissolve
        mc "I say we’re done for today."
        scene ch2sc7_83 with dissolve
        el "R-Really?"
        scene ch2sc7_82 with dissolve
        mc "Yeah, you impressed me with how fast you picked up the basics. I think we deserve a break."
        scene ch2sc7_84 with dissolve
        el "I second that! I’m a big fan of breaks!"
        scene ch2sc7_85 with dissolve
        el "Let’s sit over there, by the tree."
        scene ch2sc7_86 with dissolve
        $ renpy.pause()
        scene ch2sc7_87 with dissolve
        $ renpy.pause()
        scene ch2sc7_88 with dissolve
        $ renpy.pause()
        scene ch2sc7_89 with dissolve
        $ renpy.pause(0.5)
        el "Look daisies! *Giggles* Just like back home at Whitehills."
        scene ch2sc7_90 with dissolve
        $ renpy.pause(0.5)
        mc "Yeah, we have daisies near Riverside as well, just not as abundant as Whitehills."
        el "*Giggling joyously* Mh-hm!"
        scene ch2sc7_91 with dissolve
        $ renpy.pause()
        stop music fadeout 2.0
        scene ch2sc7_92 with dissolve
        "You both lean back, enjoying the rays of sun penetrating the canopy of trees above you."
        play music warm_1 fadein 2.0
        scene ch2sc7_93 with dissolve
        mc "..."
        scene ch2sc7_94 with dissolve
        el "..."
        scene ch2sc7_95 with dissolve
        el "What are you thinking about?"
        scene ch2sc7_96 with dissolve
        mc "Just this place. Brings back memories..."
        scene ch2sc7_97 with dissolve
        el "You used to come here before?"
        scene ch2sc7_98 with dissolve
        mc "Multiple times a week, with my best friend, Alice... and my cousin, Flynn."
        mc "These apple orchards were our hangout spot away from the village. We'd spend hours here messing around."
        scene ch2sc7_99 with dissolve
        mc "Just kids being kids."
        scene ch2sc7_100 with dissolve
        el "Sounds like some great memories were made here."
        scene ch2sc7_101 with dissolve
        $ renpy.pause(1)
        scene ch2sc7_102 with dissolve
        $ renpy.pause(1)
        stop music fadeout 2.0
        scene ch2sc7_103 with dissolve
        $ renpy.pause(1)
        scene ch2sc7_104 with dissolve
        $ renpy.pause(1)
        play music happy_1 fadein 2.0
        scene whiteflash with Dissolve (2.0)
        $ renpy.pause(1.5)
        #scene black with Dissolve(3)
        scene ch2sc7_105 with Dissolve (2.0)
        $ renpy.pause(0.5)
        fy "Up high, [mc]!"
        mc "Hah! She won’t find us here."
        scene ch2sc7_106 with dissolve
        al "There you are! What are you up to?"
        scene ch2sc7_107 with dissolve
        $ renpy.pause()
        scene ch2sc7_108 with dissolve
        fy "Alice! W-What a surprise!"
        fy "We weren’t hiding from you or anything..."
        mc "Hi Alice. What brings you out here?"
        scene ch2sc7_109 with dissolve
        al "Okaay... cut the crap, you two! I know you’re up to something!"
        scene ch2sc7_110 with dissolve
        fy "First, you have to promise you won’t tell our parents."
        scene ch2sc7_109 with dissolve
        al "Done! Now tell me!"
        scene ch2sc7_111 with dissolve
        fy "So, you’ll never believe the idea I came up with, Alice."
        fy "We’re going to build a boat!"
        scene ch2sc7_112 with dissolve
        al "... A boat?"
        scene ch2sc7_113 with dissolve
        with vpunch
        al "Have you gone mad?! Your parents will kill you, if you don’t drown first!"
        scene ch2sc7_114 with dissolve
        el "Sounds like you and your cousin were up to no good!"
        scene ch2sc7_115 with dissolve
        mc "That was usually the case."
        mc "Most of it was him coming up with silly ideas."
        scene ch2sc7_116 with dissolve
        el "Let me guess, Alice was the voice of reason in your group?"
        scene ch2sc7_115 with dissolve
        mc "I suppose she was."
        mc "At the time, it just seemed like she wanted to bust our balls."
        scene ch2sc7_117 with dissolve
        mc "She never told on us, though."
        mc "She somehow always ended up helping us."
        scene ch2sc7_118 with dissolve
        el "Even though your ideas were silly, I’m sure she just wanted to be with you guys."
        scene ch2sc7_115 with dissolve
        mc "You might be right."
        mc "Anyway, let’s head back and get some long overdue breakfast."
        scene ch2sc7_119 with dissolve
        el "Music to my ears! I’m famished!"
        scene ch2sc7_120 with dissolve
        mc "Don’t be so dramatic."
        mc "You've only gone a few hours without breakfast."
        scene ch2sc7_116 with dissolve
        el "And I'll remember it for the rest of my days!"
        scene ch2sc7_19 with dissolve
        mc "Come on, we'd better get some food in you before you have a meltdown."
        scene ch2sc7_20 with dissolve
        el "Finally, you're starting to see reason!"
        el "I'll be ordering double!"
        el "That's what you get for making me workout before breakfast!"
        scene black with Dissolve(2)
        stop music fadeout 2.0
        "You head back towards Riverside."
        jump ch2sc8

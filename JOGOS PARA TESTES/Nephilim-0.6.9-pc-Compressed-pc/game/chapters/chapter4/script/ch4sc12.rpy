label ch4sc12:

    window hide dissolve
    play music tavern_3 fadein 1.0
    scene ss29 with Dissolve (1.0)
    $ renpy.pause()
    scene ch4sc12_001 with Dissolve(2.0)
    $ renpy.pause()
    scene ch4sc12_002 with dissolve
    ki "Okay, we’re here. ‘Creed’s Chunky Chicken’..."
    scene ch4sc12_003 with dissolve
    mc "'Chunky Chicken'?"
    mc "Do I even want to know?"
    scene ch4sc12_004 with dissolve
    ki "Probably not."
    ki "But if you're curious... over there."
    scene ch4sc12_005 with dissolve
    $ renpy.pause()
    mc "Damn. I see your point."
    ki "Creed won’t tell anyone why he always keeps a fat chick here. But every time they grow up ..."
    scene ch4sc12_006 with dissolve
    ki "He gets a new one and wastes no time fattening it up."
    scene ch4sc12_005 with dissolve
    ki "Personally, I think he eats them."
    scene ch4sc12_007 with dissolve
    with vpunch
    cc "Squueeek!"
    scene ch4sc12_008 with dissolve
    cr "Hey! Stop scaring the poor fella!"
    cr "You might be the boss’s daughter, but I’ll still toss you out on your ass, Kira!"
    scene ch4sc12_009 with dissolve
    ki "Yeah, yeah, Creed... you’re lucky I’m in a good mood today."
    ki "Otherwise I’d use you as sharkbait."
    scene ch4sc12_010 with dissolve
    ki "Come."
    ki "We shouldn’t keep father waiting. He isn’t known for his patience."
    scene ch4sc12_011 with dissolve
    ki "Remember, let me do the talking. You’ll just say something stupid and get yourself killed…"
    mc "Concerned for my safety?"
    scene ch4sc12_012 with dissolve
    ki "Wha- No!"
    ki "I-I don’t care what happens to you! I mean, I do-"
    ki "Ugh! Just keep quiet and do as I say for once!"
    scene ch4sc12_013 with dissolve
    ki "I’m trying to help you here, in case you didn’t notice."
    mc "So you do care."
    mct "*Chuckles* She gets flustered so easily when I put her on the spot."
    scene ch4sc12_014 with dissolve
    $ renpy.pause(1.5)
    "Kira remains silent as she enters the back room."
    stop music fadeout 2
    scene ch4sc12_015 with dissolve
    ######ANIMATION#####
    show bh_intro with fade
    play music dark_1 fadein 1.0
    $ renpy.pause(2, hard=True)
    $ renpy.pause(12)
    scene ch4sc12_015 with dissolve
    $ renpy.pause(1.5)
    scene ch4sc12_016 with dissolve
    $ renpy.pause(1.5)
    scene ch4sc12_018 with dissolve
    stop music fadeout 1
    cb "Kira. What took you so long?"
    play music explore_1 fadein 1.0
    scene ch4sc12_017 with dissolve
    ki "Hi... Daddy."
    scene ch4sc12_018 with dissolve
    cb "Don’t ‘daddy’ me."
    cb "Your sister already stopped by to give me her full report."
    cb "While you were fooling around with the ‘cargo’... Pearl came to see me straightaway, as she should."
    scene ch4sc12_020 with dissolve
    ki "Daddy! I-"
    scene ch4sc12_021 with dissolve
    with vpunch
    cb "Enough!"
    cb "Go find your sister and get something to eat. You’ll anchor in the bay tonight and leave at first light."
    scene ch4sc12_022 with dissolve
    cb "I wish to have a chat with your friend here."
    scene ch4sc12_023 with dissolve
    "As Kira turns to leave, she puts her hand on your arm."
    "You can feel her arm trembling, she's clearly upset about her fathers reaction."
    scene ch4sc12_024 with dissolve
    $ renpy.pause(1)
    kit "I'm... never good enough."
    scene ch4sc12_025 with dissolve
    ki "*Whispers* {size=-10}{b}Come find me later… I’ll be at the docks.{/b}{/size}"
    ki "*Whispers* {size=-10}{b}There’s something I want to show you.{/b}{/size}"
    scene ch4sc12_026 with dissolve
    ki "*Whispers* {size=-10}{b}Make sure you aren’t followed.{/b}{/size}"
    scene ch4sc12_027 with dissolve
    "Blackheart turns his gaze towards you."
    scene ch4sc12_028 with dissolve
    cb "You."
    cb "Care to tell me why both my daughters have lost their heads over you?"
    scene ch4sc12_029 with dissolve
    cb "First, Pearl rushes to see me, telling me how great you are and that I shouldn’t kill you."
    scene ch4sc12_028 with dissolve
    cb "And now Kira finally delivers you, but not in chains as expected."
    scene ch4sc12_029 with dissolve
    cb "Neither of them have shown much interest in boys before."
    cb "And yet, here they are. Both acting out of character because of you."
    scene ch4sc12_028 with dissolve
    cb "What is a father supposed to make of that?"
    scene ch4sc12_030 with dissolve
    cb "Am I to embrace you as your potential father-in-law?"
    cb "Or... should I hang you for daring to lay eyes on my daughters?"
    stop music fadeout 1
    ###Choice###
    menu:
        "Attempt to Intimidate Blackheart. ({color=#fc584c}Intimidation{/color})":
            scene ch4sc12_031 with dissolve
            play music darknight_4 fadein 1.0
            mc "How about we skip these little games?"
            mc "They're boring, and I couldn't care less about your opinion of me."
            scene ch4sc12_032 with dissolve
            mc "I’m only interested in reaching Inmortui. If anyone gets in my way... even you, 'King of pirates' ..."
            mc "Then I will tear that person apart while your daughters watch."
            mc "And then I'll burn this cozy little settlement to the ground."
            $ intimidation += 2
            "You managed to intimidate Blackheart enough to gain his respect, {b}{color=#fc584c}Intimidation{/color}{/b} increased by {size=+3}{b}{color=#2bff8b}2{/color}{/b}{/size}."
            scene black with Dissolve(2)

        "Attempt to Persuade Blackheart. ({color=#2bff8b}Persuasion{/color})":
            scene ch4sc12_031 with dissolve
            play music home_2 fadein 1.0
            mc "How about a third option? I need to reach Inmortui."
            mc "The sooner we leave, the sooner I’ll be out of your hair."
            scene ch4sc12_032 with dissolve
            mc "In return for safe passage, I'll make sure to retrieve valuables from Inmortui."
            mc "Worst case scenario: I die, and you’re rid of me."
            scene ch4sc12_031 with dissolve
            mc "Best case, I return with some ancient loot for you."
            mc "Either way, it's a good deal for you."
            $ persuasion += 2
            "You managed to persuade Blackheart successfully! {b}{color=#2bff8b}Persuasion{/color}{/b} increased by {size=+3}{b}{color=#2bff8b}2{/color}{/b}{/size}."
            scene black with Dissolve(2)

        "Attempt to Lead Blackheart's decision. ({color=#ffee54}Leadership{/color})":
            scene ch4sc12_031 with dissolve
            play music home_2 fadein 1.0
            mc "Blackheart, you're a leader."
            mc "Which means I know you'll recognize my efforts."
            scene ch4sc12_032 with dissolve
            mc "Earlier you said Pearl has filled you in about everything, which means you know about the trouble in Luxenford."
            mc "That I was the one who secured our crew and ensured the wellbeing of them."
            scene ch4sc12_031 with dissolve
            $ leadership += 2
            mc "Now, you may or may not care about your daughters crew, I don't know you well enough to make that observation."
            mc "But you should know enough about me now that'll make you want to have me on your daughters manifest."
            mc "Am I right?"
            "You managed to take control of the discussion and lead Blackheart's opinion successfully! {b}{color=#ffee54}Leadership{/color}{/b} increased by {size=+3}{b}{color=#2bff8b}2{/color}{/b}{/size}."
            scene black with Dissolve(2)

        "Attempt to appeal to Blackheart's greed. ({color=#87e1fa}Charisma{/color})":
            scene ch4sc12_031 with dissolve
            play music home_2 fadein 1.0
            mc "Blackheart, you're a renowned Captain, and a undisputed leader of your pirates."
            mc "I've known you for less than an hour and yet I can clearly tell what you're after."
            scene ch4sc12_032 with dissolve
            mc "You want a future for your pirates where you're not fighting for scraps."
            mc "You want prosperity and recognition as an official independant state."
            cb "*Scoffs* Hmm."
            scene ch4sc12_031 with dissolve
            $ charisma += 2
            mc "Well guess what?"
            mc "Allowing me to undertake this journey with your daughters will be a step towards that future."
            mc "We're going to an infamous island that no sailors or any of your pirates dare step foot on..."
            mc "Imagine the treasures we might come across... your chambers filled with gold and gems..."
            "You managed to sway Blackheart's opinion due to his lust for power and riches, {b}{color=#87e1fa}Charisma{/color}{/b} increased by {size=+3}{b}{color=#2bff8b}2{/color}{/b}{/size}."
            scene black with Dissolve(2)



    scene ch4sc12_033 with dissolve
    stop music fadeout 1
    cb "..."
    play music summon_3 fadein 1.0
    cb "Heh! The balls on you, kid."
    cb "Hhmm..."
    scene ch4sc12_030 with dissolve
    cb "Alright. I’ve decided!"
    cb "I'll authorize your passage to Inmortui."
    cb "Pearl & Kira will supervise you. They'll have instructions to 'handle' you if you step out of line."
    cb "Now, leave. Before I run out of goodwill."
    scene ch4sc12_031 with dissolve
    mc "One last thing before I leave."
    scene ch4sc12_032 with dissolve
    mc "That’s quite an interesting ring you’re wearing."
    scene ch4sc12_033 with dissolve
    cb "Hmm."
    cb "This tacky old thing? Not all that interesting, I’m afraid. Just an old family heirloom…"
    scene ch4sc12_030 with dissolve
    cb "Now, was that all?"
    scene ch4sc12_034 with dissolve
    mct "He’s lying. That ring has the same magical aura that Borri’s ring does."
    mct "Only... darker."
    scene ch4sc12_035 with dissolve
    mct "I'll have to investigate another time. For now, I better go find Kira."
    scene ch4sc12_034 with dissolve
    stop music fadeout 1
    $ renpy.pause(1.5)
    scene ch4sc12_036 with dissolve
    play music dark_1 fadein 1.0
    $ renpy.pause(1.5)
    scene ch4sc12_037 with dissolve
    $ renpy.pause(1.5)
    wh "*Hissing* Sssaaahh He Ssshh He knows! Saaah…"
    scene ch4sc12_036 with dissolve
    wh "*Hissing* Ssaaah Kill! Yes… Kill! Saaahhh…"
    cb "He doesn’t know anything."
    scene ch4sc12_037 with dissolve
    wh "*Hissing* Saah! He knows… Kill him. Saahhh…"
    scene ch4sc12_038 with dissolve
    wh "*Hissing* Shhaa… He wants Saah… your throne... Your Sahhss… daughters!"
    scene ch4sc12_036 with dissolve
    cb "He did take an interest in you... And both my girls seem to be smitten already."
    scene ch4sc12_037 with dissolve
    wh "*Hissing* SAH! Yess... He wants to... Saaahh... Kill you! Kill him! Ssah."
    cb "Kill... yes... it's the only way."
    scene ch4sc12_038 with dissolve
    wh "*Hissing* SAH! Yess. Kill him... Shaahh... Kill! Kill him! Ssah."
    scene black with Dissolve(2)
    stop music fadeout 1
    scene ss3 with dissolve
    $ renpy.pause()
    scene ch4sc12_039 with Dissolve(2)
    play music chill_5 fadein 1.0
    $ renpy.pause(1)
    ######ANIMATION#####
    show ki_ani1 with fade
    $ renpy.pause(2, hard=True)
    kit "*Washing* Mnnh… I needed this."
    kit "Being surrounded by the crew all the time doesn't leave much room for privacy."
    kit "But this... the humid air of Looter’s bay caressing my skin..."
    kit "The distant cries of seagulls under the moonlit sky."
    kit "..."
    kit "Once again, Pearl got praised while I got ordered away... "
    kit "*Sigh* I hope [mc] can hold his own against father."
    kit "..."
    kit "[mc]..."
    "Kira starts squeezing her supple breasts, her touch eliciting quiet but still noticeable moans of pleasure."
    kit "Mnnhh... [mc]. Yes!"
    kit "Nnhhg! Touch me! Your rough hands on my soft skin..."
    scene black with Dissolve(2)
    $ renpy.pause(1.5)
    scene ch4sc12_039 with Dissolve(2)
    mc "Hey..."
    scene ch4sc12_040 with dissolve
    with vpunch
    $ renpy.pause()
    kit "F-Fuck! No, no, no, no!"
    scene ch4sc12_041 with dissolve
    ki "[mc]? W-What are you doing here?"
    mc "You asked me to meet you at the docks."
    scene ch4sc12_042 with dissolve
    ki "Oh, right! I remember... I asked you to meet me here, I didn't expect you to be done already?"
    ki "Why are you staring at me?"
    scene ch4sc12_043 with dissolve
    $ renpy.pause(1.3)
    ki "..."
    scene ch4sc12_044 with dissolve
    ki "{b}*Angrily* I-I’m going to kill you!!{/b}"
    ki "{b}*Shouts* You’re a pervert!{/b}"
    ki "{b}*Shouts* I swear you'll die by my sword!{/b}"
    scene ch4sc12_042 with dissolve
    ki "Huh?? Why are you laughing?!"
    ####Choice####
    menu:
        "Flirt. ({color=#ff8cdd}Romance{/color})":
            scene ch4sc12_045 with dissolve
            mc "*Laughs*"
            mc "I’m not looking at you because I’m perverted."
            scene ch4sc12_046 with dissolve
            mc "I’m looking at you because you’re beautiful."
            scene ch4sc12_047 with dissolve
            "Her angry frown quickly turns to a smile."
            scene ch4sc12_048 with dissolve
            kit "He thinks I’m beautiful?"
            kit "His eyes... they’re so blue!"
            $ kira_path = True
            kit "I can’t even stay mad at this jerk when he looks at me."
            "Despite Kira's outburst, she clearly enjoys being seen by you, her trust has increased by {size=+3}{b}{color=#2bff8b}2{/color}{/b}{/size}."
            $ kira_trust += 2
            scene ch4sc12_049 with dissolve
            $ renpy.pause()
            scene ch4sc12_046 with dissolve
            mc "Now you’re the one who’s staring."
            scene ch4sc12_048 with dissolve
            $ renpy.pause(1)
            ######ANIMATION#####
            show ki_ani2 with fade
            $ renpy.pause(2, hard=True)
            kit "I’ve killed men for looking at me, even when I've been dressed."
            kit "Yet here I am... letting [mc] see me like this."
            kit "I’ve never felt so excited to have a man’s gaze upon me."
            kit "[mc]..."
            mc "Kira?"
            scene ch4sc12_048 with dissolve
            ki "Huh??"
            scene ch4sc12_050 with dissolve
            ki "Avert your eyes, pervert!"
            ki "Turn around, and let me get dressed!"
            scene black with Dissolve(2)
            $ renpy.pause(1.5)

        "Dismiss. (Neutral)":
            scene ch4sc12_045 with dissolve
            mc "*Laughs*"
            scene ch4sc12_046 with dissolve
            mc "Don’t jump to conclusions. I’m not interested."
            mc "You wanted to meet, so here I am."
            ki "Hnrhh... jerk!"
            scene black with Dissolve(2)
            $ renpy.pause(1.5)

    scene ch4sc12_051 with Dissolve(2)
    stop music fadeout 1
    $ renpy.pause(1.5)
    scene ch4sc12_052 with dissolve
    play music darknight_4 fadein 1.0
    $ renpy.pause(1.5)
    "You feel something poking your back..."
    scene ch4sc12_053 with dissolve
    ki "*Whispers* {size=-10}{b}I could kill you right now and be done with you.{/b}{/size}"
    ki "*Whispers* {size=-10}{b}Perving on me while I'm naked... I really should punish you.{/b}{/size}"
    mct "It’s cute how she keeps making her little threats, as if she could actually hurt me."
    ki "What’s wrong? Cat got your tongue?"
    scene ch4sc12_054 with dissolve
    mc "Is that what you want? To be done with me?"
    scene ch4sc12_053 with dissolve
    ki "Yes..."
    stop music fadeout 1
    scene ch4sc12_055 with dissolve
    ki "I... no."
    "You feel Kira pull back her dagger."
    play music relax_2 fadein 1.0
    ki "*Whispers* {size=-10}{b}I don’t want that at all.{/b}{/size}"
    scene ch4sc12_054 with dissolve
    mc "Then what do you want, Kira?"
    scene ch4sc12_056 with dissolve
    kit "What do I want? Why did I invite him along tonight?"
    kit "I’ve never shared this place with anyone, not even Pearl."
    kit "But he makes me feel like I can let my guard down..."
    kit "And I wanted to make amends for bringing him here... I want to-"
    scene ch4sc12_057 with dissolve
    ki "Urgh!"
    ki "You’re so annoying! Just... come with me!"
    scene ch4sc12_058 with dissolve
    ki "I want to show you something…"
    "You follow Kira in silence."
    scene ch4sc12_059 with dissolve
    $ renpy.pause(1.5)
    scene ch4sc12_060 with dissolve
    $ renpy.pause(1.5)
    scene ch4sc12_061 with dissolve
    $ renpy.pause(1.5)
    scene ch4sc12_062 with dissolve
    $ renpy.pause(1.5)
    scene ch4sc12_063 with dissolve
    ki "Here."
    ki "Let’s sit over there."
    scene ch4sc12_064 with dissolve
    "The two of you climb onto a large rock, overlooking the bay."
    ki "I like it here."
    scene ch4sc12_065 with dissolve
    mc "What is this place?"
    scene ch4sc12_064 with dissolve
    ki "My favorite place in Looter’s Bay."
    ki "The only place where I can be alone."
    ki "Be... myself."
    scene ch4sc12_065 with dissolve
    mc "It’s nice…"
    scene ch4sc12_066 with dissolve
    ki "It’s nice? That’s the best you've got?"
    ki "I’m sharing my secret spot with you, and that’s all you give me?"
    ki "*Scoffs* Men!"
    scene ch4sc12_067 with dissolve
    mc "*Chuckles* What?"
    mc "You expect me to go on a poetic rant about how tranquil it is, or how soothing the waves are?"
    mc "Maybe rave about the refreshing feel of the cool evening breeze on my skin?"
    mc "Or should I swoon because of the mesmerizing moonlight?"
    "Kira remains silent for a moment before you see something new... she's actually laughing!"
    scene ch4sc12_068 with dissolve
    ki "*Light-hearted laughter* Hah-hah-ha! No, I suppose I shouldn’t expect that! Hah-ahah!"
    ki "*Laughs* Hahah! Sorry, sorry! Just the idea of you being a poet is so funny to me!"
    ####Choice####
    menu:
        "Show her some real poetry. ({color=#ff8cdd}Romance{/color})":
            scene ch4sc12_071 with dissolve
            mc "How’s this for poetry."
            $ kira_kiss = True
            scene ch4sc12_072 with dissolve
            $ renpy.pause(1.5)
            kit "He’s going to kiss me!"
            kit "By the sea! I didn’t prepare! I don't even know how to prepare!"
            kit "What if I'm horrible at it? What if he doesn't like it?"
            $ kira_path = True
            "Nonetheless, Kira leans towards you, her pulse quickening with anticipation."
            scene ch4sc12_073 with dissolve
            $ renpy.pause(1.5)
            scene ch4sc12_074 with dissolve
            $ renpy.pause(1.5)
            scene ch4sc12_073 with dissolve
            $ renpy.pause(1.5)
            scene ch4sc12_074 with dissolve
            $ renpy.pause(1.5)
            mct "Damn. Her lips are delightful."
            mct "I didn’t expect her to be this... appetizing."
            scene ch4sc12_073 with dissolve
            $ renpy.pause(1)
            scene ch4sc12_074 with dissolve
            kit "*Moans* Mnhhh!"
            kit "He’s kissing me! Please like it..."
            kit "She presses closer as you continue to engage each other, kiss after kiss."
            scene ch4sc12_075 with dissolve
            $ renpy.pause(1.5)
            ######ANIMATION#####
            show kira_kiss2 with fade
            $ renpy.pause(2, hard=True)
            $ renpy.pause ()
            mct "Her hair smells like freshly picked roses... and her lips taste slightly fruity."
            mct "She might be a pain in the ass at times but... I want her."
            kit "Mnhhhh! Mnnnnn... he’s so gentle with me! I... I can’t stop myself."
            kit "[mc]! Nngghh! The way he caresses my cheek as we kiss..."
            kit "Nnnhhhhh… Maybe it would be... Mnnhh... okay to let him touch..."
            scene ch4sc12_075 with dissolve
            kit "Yes, I want him to."
            "With her hand atop yours, she guides it downward as she deepens the intimacy of her kiss."
            scene ch4sc12_076 with dissolve
            $ renpy.pause (1.5)
            "She moans softly into your mouth as your hand finally cups her warm, perky breast."
            ki "*Moans* MHH! Mnnhh..."
            scene ch4sc12_077 with dissolve
            kit "I can’t believe I’m letting a man touch me."
            kit "But it feels right with him. Incredibly right, Mhhh!"
            scene ch4sc12_076 with dissolve
            $ renpy.pause (1.5)
            scene ch4sc12_077 with dissolve
            $ renpy.pause (1.5)
            scene ch4sc12_076 with dissolve
            mct "Her heart is beating so fast... she really isn’t faking it."
            mct "This is her being genuine... she's allowing herself to finally be... honest."
            scene ch4sc12_077 with dissolve
            mct "I can even feel her pulse through her breast... and her moans... fuck."
            scene ch4sc12_078 with dissolve
            ki "Mmnnhhh... [mc]... *Kiss*"
            scene ch4sc12_079 with dissolve
            ki "Nnggh… I- *Kiss* Mmhhh…"
            "Kira's lips part from yours reluctantly, but she doesn’t move away."
            scene ch4sc12_080 with dissolve
            ki "Pheew... What the hell was that?"
            mc "I’m not sure. But it felt right."
            scene ch4sc12_081 with dissolve
            ki "Yeah... Incredibly so."
            ki "Was it... Uhm... good?"
            scene ch4sc12_080 with dissolve
            mc "Yeah... I enjoyed every second of it."
            scene ch4sc12_081 with dissolve
            ki "Good! Good. Me too."
            mc "Am I the only guy you've kissed?"
            scene ch4sc12_080 with dissolve
            ki "Wha- Shut up! No..."
            ki "..."
            ki "Maybe."
            ki "So what if you are!? You already said you enjoyed kissing me! Doesn't matter if you were my first!"
            mct "*Chuckles* Cute, she thinks that me being her first kiss was something I'd frown upon?"
            scene ch4sc12_081 with dissolve
            mc "Now that I know I am the only one you've kissed, I like it even more."
            ki "You’re an idiot."
            mc "Yeah?"
            ki "Yeah... but I'm glad you were my first kiss."
            scene ch4sc12_080 with dissolve
            ki "*Sighs* You shouldn’t have done that."
            ki "You do realize my dad will kill you for this? Putting your hands and lips on his daughter."
            if leadership >=3:
                scene ch4sc12_081 with dissolve
                mc "Let me handle your father."
                $ kira_trust += 1
                mc "I know men like him, I fully expect him to have something up his sleeve."
                mc "He's likely going to betray us one way or another."
                scene ch4sc12_080 with dissolve
                ki "Yeah... that is something he likely will attempt."
                ki "[mc]- I... I want you to know-"
                ki "I won't betray you again, I... I promise."
                scene ch4sc12_081 with dissolve
                mc "You haven't betrayed me this far... yes, bringing me here was an inconvenience."
                mc "But you didn't owe me anything at that point, yes we were becoming friends..."
                mc "But we weren't as we are now, you bringing me here has oddly enough brought us closer."
                scene ch4sc12_080 with dissolve
                ki "I-... I feel the same."
                mc "Don't worry Kira, your father might believe he's the one in charge, but he's not."
                "Kira believes you, she finds your ability to take lead attractive, her trust has increased by {size=+3}{b}{color=#2bff8b}1{/color}{/b}{/size}."
                ki "Please... could you... kiss me again?"
                scene ch4sc12_078 with dissolve
                ki "*Moans softly* Mmmh-nnhh... your lips make me feel safe."
                scene ch4sc12_079 with dissolve
                mc "Then I better keep them on you."
                ki "Mmmh... yes... you better... mmhh..."
                scene ch4sc12_078 with dissolve
                ki "You're a real leader... mmhh... a real man, thank you..."
                "She slowly stops the kiss."

            else:
                ki "*Sighs* ..."


            scene ch4sc12_081 with dissolve
            ki "Make some room."
            scene ch4sc12_082 with dissolve
            "Before you can react, she climbs on you and puts herself between your legs."
            ki "Mnhh... This is nice."
            mc "Heh, nice? Some poet you are."
            ki "*Laughs* I suppose we’re a match in that regard."
            scene ch4sc12_083 with dissolve
            "Having fully cuddled herself into your arms, she lets out a sigh of relief."
            kit "I shouldn’t be sitting here like this with him."
            kit "*Sigh* Is it really so wrong to want this? To be happy for once?"
            scene ch4sc12_084 with dissolve
            kit "I’ve killed hundreds of men in battle... I’ve sailed the worst parts of the Cerulean Seas."
            kit "I’ve fought off drunkards, pillagers, sharks... and yet here I am, feeling like a mushy little girl in his arms."
            scene ch4sc12_085 with dissolve
            ki "Nobody can know."
            scene ch4sc12_086 with dissolve
            mc "Okay."
            scene ch4sc12_085 with dissolve
            ki "I’m serious."
            ki "Nobody. Not even your half-wit of a cousin."
            scene ch4sc12_086 with dissolve
            mc "Relax. I won’t tell anyone."
            scene ch4sc12_087 with dissolve
            ki "Good... I trust you."
            scene ch4sc12_088 with dissolve
            ki "Hey, [mc]? Promise me something."
            ki "Don’t let my father kill you."
            scene ch4sc12_087 with dissolve
            ki "It'd be a shame if a fine man, such as yourself, died a horrific death."
            scene ch4sc12_086 with dissolve
            mc "Oh? Is that a hint of worry I detect?"
            scene ch4sc12_087 with dissolve
            ki "*Giggles* You don’t detect shit, Jellyray!"
            ki "Certainly not worry! I couldn't even worry about a landlubber like you if I tried!"
            scene ch4sc12_086 with dissolve
            mc "Don’t worry, Kira. I won’t let your father come between us."
            mc "And I certainly don’t intend to die by his hands. Or anyone else's, for that matter."
            "Despite her denial from a moment ago, you clearly feel her heartbeat, returning to a calm state upon hearing your promise."
            scene ch4sc12_089 with dissolve
            kit "Ugh! What’s wrong with me?!"
            kit "Why do I care so much about him! I’ve only known him just over a week..."
            kit "And here I am, resting in his arms after kissing him... worrying that something bad might happen to him."
            kit "And now... I can't imagine having never met him? I don't want to... lose him."
            scene ch4sc12_090 with dissolve
            kit "He'd better keep his promise... or I'll kill him myself!"
            kit "*Sigh* I shouldn’t be this close with him. Someone will notice."
            scene ch4sc12_091 with dissolve
            ki "Scoot over."
            ki "I’ve had enough romance for one night."
            scene black with Dissolve(2)

        "Laugh it off. (Neutral)":
            scene ch4sc12_069 with dissolve
            mc "*Chuckles* Yeah, yeah. I suppose I won’t be applying for the bard’s college anytime soon."
            scene black with Dissolve(2)

    scene ch4sc12_070 with Dissolve(2)
    kit "..."
    scene ch4sc12_070b with dissolve
    mc "Thank you."
    ki "Hmh? What for?"
    mc "For sharing this place with me."
    scene ch4sc12_070 with dissolve
    ki "..."
    ki "You’re welcome."
    ki "I’ve never wanted to share it with anyone before. I can’t really explain it... it just felt right with you."
    scene ch4sc12_070b with dissolve
    mc "I’m glad you did. I won’t tell anyone about this place."
    scene ch4sc12_070 with dissolve
    ki "If you do..."
    mc "You’ll turn me to shark-bait. I know, I know."
    ki "*Scoffs* Good! You’re aware of the risk you’re taking."
    scene ch4sc12_070b with dissolve
    mc "When I first stepped onboard your ship-"
    ki "The Bloody Banshee."
    mc "Huh?"
    ki "That’s her name."
    ki "You're part of her crew now, you should address her as such."
    scene ch4sc12_070 with dissolve
    mc "Right."
    mc "When I first stepped aboard ‘The Bloody Banshee’."
    scene ch4sc12_070b with dissolve
    mc "I never imagined the two of us would be sitting here... together."
    ki "Obviously. You didn’t even know Looter’s Bay existed."
    mc "You know what I mean."
    scene ch4sc12_070 with dissolve
    ki "I- Yeah. I do."
    ki "I’m quite surprised at myself, to be fair."
    ki "I’ve been so patient with you..."
    scene ch4sc12_070b with dissolve
    mc "Hmh. Is that what you call it? I'd call it-"
    ki "Don’t make me regret bringing you here!"
    scene ch4sc12_070 with dissolve
    mc "*Chuckles* Alright, alright. I’m just pulling your leg... sorta."
    ki "*Smirks* Ass."
    scene ch4sc12_070b with dissolve
    ki "It’s getting late. We should head back and get some rest. We’re leaving at first light."
    mc "Hmm, actually..."
    mc "If you don’t mind, I'll stay here a little while longer."
    scene ch4sc12_070 with dissolve
    ki "Sure. I’ll see you tomorrow."
    scene black with Dissolve(1)
    scene ch4sc12_092 with Dissolve(1)
    $ renpy.pause (1.5)
    ######ANIMATION#####
    show mc_ani1 with fade
    $ renpy.pause(2, hard=True)
    mct "Kira’s very different from who I thought she was when we first met."
    mct "She's worried about me. I never expected that."
    mct "I’m not sure what to think of her father, though. She seems convinced he's going to make a move against me."
    mct "Not that it would be surprising, though. No 'king' of pirates is likely to be very friendly."
    mct "Then there's that ring of his... If it really is an enchanted ring, then it won't do any good in his hands."
    mct "If I could bring it back to Dalen and Sylph, maybe they could see if it's connected to Borri's ring."
    mct "Hmmh."
    mct "Kira seemed vulnerable tonight?"
    mct "Sharing her special spot with me... maybe she longs to connect with someone."
    mct "And for some reason, she's comfortable enough with me that she thinks I could be that someone."
    mct "*Sigh* Do I really need to add someone else to the list of people I care about?"
    mct "Guess it's too late, I already do care about her and Pearl, even Kelly has been a breath of fresh air."
    mct "However... it'll only put them in danger."
    mct "Taron... he’s made it clear that anyone I'm close with is a target."
    mct "Kira is no pushover, though. She and Pearl have lived amongst danger their entire lives…"
    mct "As soon as Eliza is back on her feet. I’m going straight for that bastard…"
    mct "Whatever twisted plans he seems to have for me, I don’t intend to sit around and wait for his next move."
    scene ch4sc12_092 with dissolve
    mct "Eliza... I miss you."
    scene black with Dissolve(2)
    scene ch4sc12_093 with Dissolve(2)
    $ renpy.pause (1.5)
    scene ch4sc12_094 with dissolve
    $ renpy.pause (1.5)
    "As the Arc-stone lights up, a faint humming echoes throughout the room"
    scene ch4sc12_095 with dissolve
    elt "Urrhh... what’s going on?"
    elt "Huh?"
    scene ch4sc12_096 with dissolve
    with vpunch
    elt "{b}OH! OHH!!{/b}"
    scene ch4sc12_097 with dissolve
    $ renpy.pause (1.5)
    elt "*Grunts* Hhnnnh!"
    scene ch4sc12_098 with dissolve
    $ renpy.pause (1.5)
    elt "{b}[mc]!{/b} It has to be [mc]!"
    scene ch4sc12_099 with dissolve
    $ renpy.pause (1.5)
    elt "Got it!"
    scene ch4sc12_100 with dissolve
    $ renpy.pause (1.5)
    el "[mc]? Is- Is it really you? Can you hear me?"
    mc "Hey, little one…"
    mc "How are you holding up?"
    el "I’m... good."
    scene ch4sc12_101 with dissolve
    el "Much better, now that I’m hearing your voice."
    el "How does this work? It’s like we’re talking but it’s inside my head."
    el "Am I dreaming?"
    scene ch4sc12_100 with dissolve
    mc "Not quite. The Arc-stone binds our minds when it's activated, letting us communicate telepathically."
    el "Woah... Wai-Wait! Does that mean you can read my thoughts?!"
    scene ch4sc12_092b with dissolve
    mc "Hah, no. Not exactly."
    mc "Why? Is there anything you don’t want me to know?"
    ######ANIMATION#####
    show mc_el_1 with fade
    $ renpy.pause(2, hard=True)
    el "Oh definitely! There’s so much I’m keeping from you! If only you knew! *Giggles*"
    mc "It’s good to hear you laugh again."
    mc "Eliza... I’m-"
    el "I know."
    el "You don’t have to say it. I know you had to leave…"
    el "At first, I was so upset with you. But that was just me lashing out... sorry."
    mc "You’re the last person in all of Midomir that should be sorry."
    mc "You had every right to react like you did. You must have felt so helpless in that moment."
    el "You- You understand?"
    mc "Yeah. Oren walked away from you. Your mother walked away. And now I-"
    el "You haven’t walked away. You’re out there for me. And, you’re here with me now."
    el "I hate not being able to hug you."
    mc "Yeah... it sucks."
    mc "How about everytime you feel like giving me a hug, you save it in your treasury?"
    el "*Giggles* What? Like a stash of hugs?"
    mc "*Chuckles* Heh… Yeah, something like that. And once we see each other again..."
    mc "You can cash in all of your stored hugs."
    el "{b}!!!!!!!!!!!!{/b}"
    with vpunch
    el "That’s so cute!"
    mc "It’s not..."
    el "{b}CUTE!{/b} Oh! OHH! I’m going to store a lot more than just hugs! *Giggles*"
    mc "Great. What did I just get myself into?"
    el "*Giggles* You’ll see! And don’t act like you’re against it."
    el "We both know you suck at playing tough with me!"
    mc "Damn you... Fine! I look forward to you cashing in too."
    el "That’s more like it! Now you better sit down, 'cause I have so much to tell you!"
    mc "Sitting as we speak."
    el "Okay, so... I’ll start with Alice."
    el "She’s joined the Academy of Learning. She’s been going every day since you left."
    el "She must really be into that alchemy and herbology stuff. Or maybe she has a hot teacher?"
    mc "Probably both."
    el "*Giggles* Right! And-and Borri! He’s been lugging me around in his trader’s cart."
    el "He pretends it’s hard on him, but I’ve caught him smiling every time I ask to go somewhere."
    el "I think he's just enjoying having me out and about."
    el "He’s also busting his ass at the guild. He's saving up all the coin he can, but he still refuses to tell me what it’s for."
    mc "Heh. He is stubborn, but I’ve never met anyone that can match your stubbornness."
    el "Heh-Heh! It’s only a matter of time before he folds and reveals what he has planned."
    mc "Now, tell me about you. What have you been up to?"
    el "I’ve mostly spent the days reading in our room. Can’t exactly move around except for when Borri is here."
    el "But that changed today!"
    with vpunch
    mc "Wai-Wait what?! You can walk again?"
    el "No... not quite. But Sylph surprised me today!"
    el "She cast a spell on me. And now whenever I’m near her, I can {b}FLY!!{/b}"
    el "You should see me in action! Even Sylph fears to race me!"
    mc "Woah... fly? That’s incredible. I know Sylph flies around all the time but..."
    mc "I never thought she would be able to make anyone else fly."
    el "It’s like an aura or something, she called it. It only works near her."
    mc "Yeah that would make sense. But that’s amazing, Eliza."
    mc "It sounds like it'll make things easier going forward."
    el "Yeah... I’m going to be spending most of my time at the guild until you return."
    el "Like Borri, I have something I want to save up for."
    mc "Do tell."
    el "Nuh-Uh! It’s going to be a surprise for you- Us!"
    mc "If you’re trying to ignite my curiosity so that I return faster, it’s working."
    el "Yay! Then that’s exactly what I’m doing!"
    el "Speaking of curiosity..."
    el "Would you like to know what I’m wearing right now?"
    scene ch4sc12_101 with dissolve
    ####Choice####
    menu:
        "Do you even need to ask? ({color=#ff8cdd}Romance{/color})":

            $ eliza_trust += 3
            scene ch4sc12_092b with dissolve
            $ eliza_path = True
            mc "You'd better tell me. In vivid detail."
            "Eliza likes that you're interested, her trust has increased by {size=+3}{b}{color=#2bff8b}3{/color}{/b}{/size}."
            scene ch4sc12_100 with dissolve
            el "I’m wearing... nothing."
            el "All that’s covering me is our blanket. It still has some of your scent."
            scene ch4sc12_102 with dissolve
            mc "I’ve got nothing here with your scent on it, but I remember it as if you were here."
            scene ch4sc12_100 with dissolve
            el "Oh yeah? Does my scent entice you?"
            mc "You’ve got no idea. The smell of your soft, raven-colored hair... Dreamveil & Sunroot."
            el "I love how you always remember my scent, it's so... primal and yet... incredibly romantic."
            mc "I also remember the taste of your luscious lips... the feeling of your smooth, naked skin against mine."
            scene ch4sc12_101 with dissolve
            el "*Breath quickens* Heavens... I miss your touch!"
            el "[mc]... my breasts crave your attention…"
            scene ch4sc12_103 with dissolve
            el "*Whimpers* {b}NnHhh!{/b}"
            scene ch4sc12_104 with dissolve
            $ renpy.pause (1.5)
            scene ch4sc12_103 with dissolve
            $ renpy.pause (1.5)
            scene ch4sc12_104 with dissolve
            $ renpy.pause (1.5)
            mc "Are you touching your breasts?"
            scene ch4sc12_103 with dissolve
            el "Y-Yes. They’re really soft and warm."
            scene ch4sc12_104 with dissolve
            el "{b}Mnnhh!!{/b} [mc]. I really want you to touch them."
            el "I need you..."
            el "*Moans* I’m squeezing them for you. Nnhh! Yes…"
            scene ch4sc12_103 with dissolve
            mc "You’ve got no idea how badly I want to be with you right now."
            scene ch4sc12_104 with dissolve
            $ renpy.pause (1.5)
            scene ch4sc12_103 with dissolve
            $ renpy.pause (1.5)
            scene ch4sc12_101 with dissolve
            $ renpy.pause (1.5)
            el "I’m going to store this in the treasury!"
            scene ch4sc12_100 with dissolve
            el "You'd better have plenty of stamina when you return. I intend to use every ounce you have."
            scene ch4sc12_092b with dissolve
            mc "I’m already looking forward to our date."
            scene ch4sc12_100 with dissolve
            el "I’ve thought about it every day since we talked about it."
            el "I’ve never been as excited about anything before. I feel like I’m going to burst!"
            scene ch4sc12_092b with dissolve
            mc "*Chuckles* I know what you mean..."
            mc "I’ve never been on a date before, you know?"
            scene ch4sc12_101 with dissolve
            el "Oh? I’m your first?"
            el "Same goes for me... but it will be magical anyway! I have a feeling our date will include several... 'first times' for me."
            mc "Yeah... I have a feeling it will, as long as you're ready for it."
            el "I... I am, all that matters to me, is that we get to spend time together."
            el "I wouldn’t even mind if you took me fishing."
            scene ch4sc12_100 with dissolve
            mc "*Chuckles* Is that so?"
            el "I take it back! No fishing please!"
            el "Please don’t make me go fishing..."
            scene ch4sc12_092b with dissolve
            mc "I thought kittens liked fish?"
            scene ch4sc12_101 with dissolve
            el "For eating! You dummy..."
            el "*Giggles*"
            scene ch4sc12_102 with dissolve
            mc "*Chuckles*"
            scene ch4sc12_092b with dissolve
            mc "I have to get going now. We’re setting sail early in the morning."
            scene ch4sc12_101 with dissolve
            el "Awwh... I wish we could keep talking all night."
            el "Please be careful out there. And come back to me... soon."
            scene ch4sc12_100 with dissolve
            mc "I will. Goodnight my kitten."
            el "Goodnight... my lion."
            scene ch4sc12_099 with dissolve
            $ renpy.pause (1.5)
            scene ch4sc12_098 with dissolve
            $ renpy.pause (1.5)
            scene black with Dissolve(2)

        "Tempting but I’ve got to get some rest. (Neutral)":
            scene ch4sc12_092b with dissolve
            mc "Tempting, but I’ve got to head back to the ship. We’re setting sail early in the morning…"
            scene ch4sc12_100 with dissolve
            el "Awwh... alright. Thank you for reaching out... I needed this."
            scene ch4sc12_092b with dissolve
            mc "We both did. I'll check in you again soon."
            scene ch4sc12_100 with dissolve
            el "Goodnight!"

    scene black with Dissolve(2)
    scene ch4sc12_092 with dissolve
    mct "*Sigh* Everything seems to be going well back in the capital."
    mct "I was slightly worried how she would cope with being immobilized."
    mct "It's good Borri and Sylph are watching out for her, they're definitely keeping her busy."
    mct "My life really has undergone quite the change since I met Eliza."
    mct "At least that's what started it, but now..."
    mct "Now I'm making more friends than I know what to do with."
    mct "Oren always preached the importance of allies you can count on."
    scene black with Dissolve(2)
    scene ch4sc12_092c with Dissolve(2)
    mct "Eliza... I would do anything for her. I trust her blindly and she has my back."
    mct "She hasn't wavered from my side since I met her."
    mct "She's one of the most amazing people I've ever met, headstrong and stubborn, cute and funny."
    scene ch4sc12_092d with Dissolve(2)
    mct "Kira... I can't believe I'm saying it but... we're friends... or something."
    mct "She's definitely a bit of a hothead, a fireball. But she cares."
    mct "Tonight made it clear, going forward I can rely on her..."
    scene ch4sc12_092e with Dissolve(2)
    mct "Pearl... Easy-going, relaxed, enjoying every moment presented to her. For a pair of twins they couldn't be more different."
    mct "I would definitely consider Pearl a friend. She's been kind and understanding towards me."
    mct "And our late night talks has really helped take my mind off all that's been going on."
    scene ch4sc12_092f with Dissolve(2)
    mct "Then there's Kelly."
    mct "Sweet young girl... she has the world awaiting her and she is eager to explore it."
    mct "She's the daughter of Luxenford nobles, Lady Maggie and Lord Edward, yet she's spent her life at sea as a... Sea-born."
    mct "She is sweet to Flynn and seems to enjoy his stupid jokes... *Chuckles* Even when they're slightly inappropriate."
    mct "That says a lot about her character."
    scene ch4sc12_092g with Dissolve(2)
    mct "Alice... we haven't had a moment to ourselves to properly talk."
    mct "I can't imagine it was easy for her coming all the way to the capital and then have me running off."
    mct "She has feelings for me, I'm not oblivious to that... but am I able to return her feelings?"
    mct "It's something I'll have to be cautious about, she means a lot to me and I don't want to hurt her."
    scene ch4sc12_092i with Dissolve(2)
    mct "Rin..."
    mct "We've not been able to reach out to one another... despite her giving me an Arcstone."
    mct "I've tried a couple of times over the years... *Exhales* She likely hates me for leaving."
    mct "I can't blame her... we were at the height of our relationship and I just... up and left."
    mct "I hope I get a chance to reconnect with her some day..."
    scene ch4sc12_092h with Dissolve(2)
    mct "*Sigh* And then there's Sylph... that little fae is something else."
    mct "Cheerful, excitable, reliable. Those are just a few terms I'd use to describe her."
    mct "I don't know how long she has been teamed up with Dalen, they're running the guild together which means he trusts her."
    mct "Before I left, she sensed my magic, but it also allowed me to sense hers... she's genuine to the core."
    scene black with Dissolve(2)
    scene ch4sc12_092 with Dissolve(2)
    mct "And now, Sylph's looking out for Eliza? Giving her something to be excited about? I appreciate that."
    mct "*Heavy sigh* ..."
    mct "What am I doing with all of them? They clearly have grown fond of me... And I of them."
    mct "I care for all of them in their own way. The last thing I want is for any of them to get hurt."
    mct "But do I even know how I feel? I've never imagined to be in such a situation..."
    mct "The goal has always been clear. Kill the man who murdered my parents."
    mct "Now it's all muddied... Friends... Allies... Companions... Lovers."
    mct "I can't make a decision right now. I can't be distracted by... Feelings."
    mct "Once Taron is dealt with. Then I can figure out what it is I really feel. And for whom."
    scene black with Dissolve(2)
    stop music fadeout 1.5
    scene ch4sc12_107 with dissolve
    play music forest_1 fadein 1.0
    $ renpy.pause (1.5)
    kl "*Humming* Hmmh, Hnnhhm, Mnnhh, Hmm, Hhh."
    scene ch4sc12_108 with dissolve
    kl "*Humming* Nnhh, Mnh, Mnnhh, Hahhn, Hmmmh."
    scene ch4sc12_109 with dissolve
    $ renpy.pause (1.5)
    "*Twig snaps*"
    stop music fadeout 1.5
    scene ch4sc12_110 with dissolve
    kl "Anyone there?!"
    play music dark_1 fadein 1.0
    kl "Hello?!"
    scene ch4sc12_111 with dissolve
    kl "L-Louie??"
    kl "Wha-What are you doing here? Did you follow me?"
    scene ch4sc12_112 with dissolve
    lll "Oi, hey there, Kelly…"
    lll "Following you? Nay, don’t be a silly girl. Just out for a stroll and wanted to check out the water."
    scene ch4sc12_111 with dissolve
    kl "Oh... O-okay."
    kl "Does it have to be right here, though? I'm kind of bathing..."
    scene ch4sc12_112 with dissolve
    lll "*Grunts* Hnnrrrh. Bathing, yes."
    scene ch4sc12_113 with dissolve
    lll "The ocean is so inviting tonight... wouldn’t you agree?"
    scene ch4sc12_111 with dissolve
    kl "I can’t deny that."
    scene ch4sc12_114 with dissolve
    kl "B-But Louie? Could you give me some privacy? I’m trying to wash up before we set sail."
    kl "It's hard to get privacy for bathing when we're at sea."
    scene ch4sc12_113 with dissolve
    lll "Silly little girl. We’re crewmates! I’ve seen you naked often... very often."
    scene ch4sc12_114 with dissolve
    kl "W-What?"
    kl "Y-You've watched me? You've seen me naked?!"
    stop music fadeout 1.5
    scene ch4sc12_115 with dissolve
    kl "L-Louie! Back off! I-I don't like this!"
    lll "Don’t be shy with me... Hrrh... I know you like showing off for me. You're a good little tease!"
    play music darknight_4 fadein 1.0
    kl "Wha-what?! No! I-I... I didn't even know you'd seen me naked!"
    kl "Louie. Please leave, right now! You're making me uncomfortable."
    scene ch4sc12_116 with dissolve
    with vpunch
    lll "{b}*Angrily* You tease! You wanted me here tonight! Admit me!{/b}"
    kl "{b}*Squeals* Eeeek! Ouwhh Louie!! You’re hurting me!{/b}"
    kl "Let go of me!"
    scene ch4sc12_117 with dissolve
    with vpunch
    lll "{b}Shut up, whore!{/b}"
    lll "I know you get off on this, don't you?!"
    lll "We both know you’re only good for one thing!"
    kl "{b}OWWH!{/b} Let me go!"
    lll "From now on you’re going to do exactly as I say! You'll be taking care of my every hnnrrrh ... need."
    lll "You'll be on your knees just like now, begging for me to satisfy you!"
    scene ch4sc12_118 with dissolve
    kl "*Crying*{b} N-No!{/b} Let me go, you creep!"
    kl "*Crying* {b}You’re sick! I don’t want you!{/b}"
    with vpunch
    lll "*Grip tightens* You'll play a different tune once I’ve filled every hole of yours!"
    scene ch4sc12_119 with dissolve
    lll "I bet you’re a tight fit. Such a young slender body. Hnnhhrrh... you’re mine, Kelly."
    with vpunch
    lll "{b}*Grunts* Stop struggling, you slut!{/b}"
    scene ch4sc12_118 with dissolve
    kl "{b}*Screams* Let me go! HELP!!{/b}"
    scene ch4sc12_119 with dissolve
    lll "{b}Whore!{/b} I’ll teach you some manners!"
    kl "*{b}Crying* Owwh! No! Stop!!{/b}"
    scene ch4sc12_120 with dissolve
    $ renpy.pause (1.5)
    scene ch4sc12_121 with dissolve
    with vpunch
    $ renpy.pause ()
    scene ch4sc12_122 with dissolve
    lll "*Grunts* Hnnrrh! You'll learn to obey me! You think you can tease me for years and not follow up?"
    with vpunch
    lll "{b}*Shouts* You are nothing! Hnnrr! You hear me?? NOTHING!!{/b}"
    scene ch4sc12_122 with dissolve
    $ renpy.pause (1)
    scene ch4sc12_123 with dissolve
    $ renpy.pause (1)
    scene ch4sc12_122 with dissolve
    $ renpy.pause (1)
    scene ch4sc12_123 with dissolve
    $ renpy.pause (1)
    scene ch4sc12_122 with dissolve
    $ renpy.pause (1)
    scene ch4sc12_123 with dissolve
    $ renpy.pause (1)
    lll "You think you can flirt with me for years and then turn all of your attention on the new guy?!"
    with vpunch
    lll "You belong to me! {b}ME!!{/b}"
    scene ch4sc12_121 with dissolve
    $ renpy.pause (1)
    scene ch4sc12_124 with dissolve
    $ renpy.pause (1)
    scene ch4sc12_121 with dissolve
    $ renpy.pause (1)
    scene ch4sc12_124 with dissolve
    $ renpy.pause (1)
    scene ch4sc12_105 with dissolve
    $ renpy.pause (1.5)
    scene ch4sc12_106 with dissolve
    mct "Huh? What’s that fat bastard doing out here?"
    scene ch4sc12_125 with dissolve
    with vpunch
    mct "Wait- What the fuck! {b}KELLY!{/b}"
    "You sprint towards Louie. Not wasting any time!"
    scene ch4sc12_126 with dissolve
    with vpunch
    "Your uppercut sends him flying, unconscious before he even lands."
    lll "*Grunts* {b}Hrrrraaarr!{/b}"
    scene ch4sc12_127 with dissolve
    with vpunch
    $ renpy.pause (1.5)
    scene ch4sc12_128 with dissolve
    mc "{b}Kelly! Hang on!{/b}"
    "You pull the unmoving body of the girl out of the water and lay her on the beach."
    stop music fadeout 1.5
    scene ch4sc12_129 with dissolve
    mc "C’mon, Kelly! {b}You’re tougher than this!{/b}"
    play music feels_3 fadein 1.0
    mc "You’re too damn young to die! Your life has barely begun!"
    scene ch4sc12_130 with dissolve
    mc "{b}Kelly! {size=+10}Wake up!{/b}{/size}"
    mct "Her heart is still beating, but just barely... she isn't breathing."
    mct "I need to get the water out of her lungs!"
    scene ch4sc12_131 with dissolve
    mc "*Whispers* You'd better wake up."
    scene ch4sc12_132 with dissolve
    $ renpy.pause (1.5)
    scene ch4sc12_133 with dissolve
    $ renpy.pause (1.5)
    scene ch4sc12_132 with dissolve
    $ renpy.pause (1.5)
    scene ch4sc12_133 with dissolve
    $ renpy.pause (1.5)
    scene ch4sc12_132 with dissolve
    $ renpy.pause (1.5)
    scene ch4sc12_133 with dissolve
    mc "Come on, Kelly! I didn’t go to the trouble of saving you from your father, just to have you die like this."
    scene ch4sc12_132 with dissolve
    $ renpy.pause (1.5)
    scene ch4sc12_133 with dissolve
    $ renpy.pause (1.5)
    scene ch4sc12_132 with dissolve
    $ renpy.pause (1.5)
    scene ch4sc12_134 with dissolve
    mct "Fuck... It isn’t working."
    mct "Did I get to her too late?"
    "..."
    scene ch4sc12_135 with dissolve
    with vpunch
    kl "*Shaky Cough* Hrrrh! Hrrr!"
    with vpunch
    kl "Hrrrh! HnnRrHh!"
    scene ch4sc12_136 with dissolve
    kl "[mc]? Are you really here?"
    kl "Last thing I remember... I was bathing and- and Louie, he-"
    kl "-Am I dead?"
    scene ch4sc12_137 with dissolve
    kl "Please tell me I didn't die!"
    scene ch4sc12_138 with dissolve
    mc "No, Kelly. You aren’t dead."
    mc "But you would’ve been if I hadn’t stopped Louie."
    mc "His fixation on you has clearly become a full blown obsession."
    scene ch4sc12_137 with dissolve
    kl "Louie... I've never liked the way he looks at me. I've always tried to steer clear of him."
    kl "I even tried to talk to Kira and Pearl about him. But they said there is nothing they can do to get rid of him."
    scene ch4sc12_138 with dissolve
    mc "Why not? I know for a fact Kira doesn’t like him."
    scene ch4sc12_137 with dissolve
    kl "Because of their father, Blackheart. He put Louie on their crew."
    kl "I don't know why he'd want him on the ship? surely he knows what a creep he is?"
    scene ch4sc12_138 with dissolve
    mc "Hmm. I don't think Blackheart is someone who acts blindly or without a purpose."
    mc "But we’re leaving Louie behind in Looter’s Bay."
    mc "I won’t allow him anywhere near you again."
    mc "If he does show his ugly face again, I'll make him regret it... I promise."
    stop music fadeout 1.5
    scene ch4sc12_136 with dissolve
    kl "[mc] ... I-"
    play music relax_2 fadein 1.0
    kl "Thank you so-"
    scene ch4sc12_135 with dissolve
    with vpunch
    kl "{b}*Coughing* Hhrrhrh! HHhr!{/b}"
    scene ch4sc12_136 with dissolve
    kl "Will you take me back to the ship?"
    scene ch4sc12_138 with dissolve
    mc "Sure thing, little one."
    scene ch4sc12_139 with dissolve
    mc "Let’s get you back to your bed, safe and sound."
    kl "Music to my ears! I'm getting a little cold ..."
    scene ch4sc12_140 with dissolve
    kl "*Mwaah*"
    "As you pull her up off the ground, she leans towards you and kisses your cheek."
    scene ch4sc12_141 with dissolve
    kl "Mnnhh… *Mhwaah*"
    "Her soft lips lingers on your cheek, she’s clearly not in a rush to pull away from you."
    ####Choice####
    menu:
        "Kiss her. ({color=#ff8cdd}Romance{/color})":
            scene ch4sc12_141 with dissolve
            $ kelly_kiss = True
            mct "The way she presses herself against me... who am I to deny the affections of a sweet girl like her?"
            scene ch4sc12_142 with dissolve
            $ kelly_path = True
            "You turn your head slightly, and her expectant lips find yours eagerly."
            scene ch4sc12_143 with dissolve
            $ kelly_bj = True
            "*Mwah MhaHhh* She responds to your kiss with multiple kisses of her own."
            scene ch4sc12_142 with dissolve
            $ renpy.pause (1.5)
            scene ch4sc12_143 with dissolve
            $ renpy.pause (1.5)
            scene ch4sc12_142 with dissolve
            mct "Heh, she’s so cute. It’s easy to tell she has no experience kissing."
            scene ch4sc12_143 with dissolve
            mct "But her eagerness and soft lips more than make up for it."
            scene ch4sc12_142 with dissolve
            kl "*Muffled moan* Mnnhhh... *Kiss* Nghhh. *Suck* Mhh..."
            mct "Let’s see how she reacts..."
            scene ch4sc12_144 with dissolve
            $ renpy.pause (1.5)
            scene ch4sc12_145 with dissolve
            $ renpy.pause (1.5)
            kl "*Moans* Mhhhh! Mnnnhhhh…"
            $ kelly_trust += 5
            "You rescuing Kelly and giving her much needed affection has solidified her trust in you, her trust increased by {size=+3}{b}{color=#2bff8b}5{/color}{/b}{/size}."
            scene ch4sc12_146 with dissolve
            mct "What a firm little plump ass she has. To think she’s only eighteen years of age..."
            scene ch4sc12_145 with dissolve
            mct "There’s so much for her still to experience. And by the looks of it, she wants me to be her guide."
            scene ch4sc12_146 with dissolve
            mct "I’ll take good care of you, Kelly. Don’t worry."
            scene ch4sc12_143 with dissolve
            kl "*Moans* Mnnhhh… *Mwah*  *Mhwaah*"
            scene ch4sc12_147 with dissolve
            kl "*Whispers* {size=-10}{b}My savior... rescuing me time and again.{/b}{/size}"
            kl "*Whispers* {size=-10}{b}I know just how to thank you.{/b}{/size}"
            kl "*Whispers* {size=-10}{b}Take me to bed... please. I want to taste you again- Mmmh.{/b}{/size}"
            stop music fadeout 1.5
            scene black with Dissolve(2)
            scene ch4sc9_0120 with Dissolve(2)
            play music lewd_1 fadein 1.0
            kl "*Whispers* {size=-10}{b}Mnnh... I can’t wait to have you in my mouth.{/b}{/size}"
            kl "*Whispers* {size=-10}{b}We'd better be quiet, though. We don’t want to wake up your cousin.{/b}{/size}"
            scene ch4sc9_0122 with dissolve
            $ renpy.pause (1.5)
            scene ch4sc9_0123 with dissolve
            "She blows a little bit of air on your tip, before planting her lips softly around it."
            scene ch4sc9_0124 with dissolve
            kl "*Soft moan* Nnnghh… *Sucks* MmHhh…"
            ######ANIMATION#####
            show kelly_bj1 with fade
            $ renpy.pause(2, hard=True)
            $ renpy.pause ()
            mct "F-Fuck… She’s really good at that. Aahh… It's as if her soft lips were made for this."
            mc "*Moans* Ahhmm... Kelly. Mhh..."
            kl "*Suck* *Suck* Nnnghhh… MmMhh!"
            mc "I should- Hhmmhh... I should rescue you more often."
            kl "*Sucks harder*"
            mc "F-Fuck! Mhhh! You’re amazing, Kelly."
            "She keeps increasing the suction even as she begins to swirl her wet tongue around your tip."
            "It’s clear she has one goal in mind: to satisfy you completely with her little, warm mouth."
            mc "Kelly! MMhh! I’m going to-"
            kl "*Suck* *Suck*"
            with vpunch
            mc "Aaahh!"
            with vpunch
            scene ch4sc9_0124 with dissolve
            "She keeps her lips closed around your tip, continuously sucking gently to get all of your cum."
            "The feel of her gentle sucking keeps you at the edge and, abrubtly, you give her another taste."
            scene ch4sc12_148 with dissolve
            with vpunch
            kl "*Muffled moan* MnnHhH! *Lick* MhhH! Nnnhhh…"
            "Surprised by your second load of cum, she can't contain it all in her mouth-"
            scene ch4sc12_149 with dissolve
            "-But instead of pulling away, she sets to work licking you thoroughly clean."
            kl "*Lick* Mnnhh... *Lick* Mnhh..."
            scene black with Dissolve(1)
            scene ch4sc9_0126 with Dissolve(1)
            kl "Wauhh. I can’t believe you came twice!"
            scene ch4sc9_0127 with dissolve
            mc "Yeah... surprised me as well, to be honest."
            scene ch4sc9_0126 with dissolve
            kl "*Giggles* I just wanted to thank you... really badly."
            kl "And- and you’re delicious!"
            scene ch4sc9_0127 with dissolve
            mc "*Chuckles* Glad you enjoyed it. You were amazing…"
            scene ch4sc9_0126 with dissolve
            kl "You have to say that... I just made you cum... {b}TWICE!{/b}"
            scene ch4sc9_0127 with dissolve
            mc "*Chuckles* Your eagerness certainly makes up for any lack of experience."
            scene ch4sc9_0126 with dissolve
            kl "Would you... like me to do it again sometime?"
            kl "I know I've been tasting you every night since we left Luxenford... but..."
            kl "I'd like your approval to continue?"
            scene ch4sc9_0127 with dissolve
            mc "Kelly... we’ll be traveling together for some time."
            mc "I'd hate it if this was the last time you have your sexy little mouth wrapped around my cock."
            scene ch4sc9_0126 with dissolve
            kl "*Giggles* Good! I was hoping you would say that."
            kl "In that case, I'd better make sure my mouth finds its way to your cock tomorrow."
            kl "And the day after that, and the day after that..."
            scene ch4sc9_0127 with dissolve
            mc "*Chuckles* I’m going to have my hands full with you, aren’t I?"
            scene ch4sc9_0126 with dissolve
            kl "You have no idea."
            kl "Goodnight, my hero."
            scene ch4sc9_0127 with dissolve
            mc "Goodnight, little one."
            stop music fadeout 1.5
            scene black with Dissolve(2)

        "Do nothing. (Neutral)":
            scene ch4sc12_147 with dissolve
            kl "My savior ... rescuing me from my lunatic father, and now Louie."
            kl "You’re the reason I’m alive. I won’t forget that."
            scene ch4sc12_141 with dissolve
            kl "*Mwah*"
            stop music fadeout 1.5
            scene black with Dissolve(2)

    scene black with dissolve
    ######ANIMATION#####
    show el_happy1 with fade
    play music chill_5 fadein 1.0
    $ renpy.pause(2, hard=True)
    $ renpy.pause ()
    elt "It felt amazing to hear his voice again!"
    elt "I was starting to think this little crystal thingy was broken."
    elt "But nuh-uh! He really is out there, looking for a way to help me."
    elt "He’s been gone a little over a week at this point, and... I miss him."
    elt "I miss him so much! I just want him to return safely. The sooner the better!"
    elt "If- no. When. When he finds a way to heal me, I'm going to ask him if we can speed up my training."
    elt "I don’t want to hold him back. Or worse... be a burden."
    elt "This isn’t likely to be our last meeting with that man. Or our last dangerous encounter."
    elt "I need to be able to hold my own, so that he doesn’t have to worry about me."
    elt "He was proud of me when I took out that goblin."
    elt "*Giggles* That was a thrill. Not the nasty goblin part but... him being proud of me."
    elt "The thought still warms me to my core."
    elt "[mc]... I want to be in your arms again."
    elt "You promised me a date when you get back. My first date! Our first date!"
    elt "*Inhales deeply* Deep breaths, Eliza. I'd better not get too excited."
    elt "*Giggles* But how can I not? {b}IT IS EXCITING!!{/b}"
    stop music fadeout 1.5
    scene black with Dissolve(2)
    scene ch4sc12_015b with Dissolve(2)
    play music dark_1 fadein 1.0
    uk "{b}*Angrily* You let them go?!{/b}"
    uk "We had a deal! You were to keep them here til I arrived!"
    scene ch4sc12_022 with dissolve
    cb "*Annoyed* You forget your place, Edward."
    cb "You might have all the lords back at Luxenford eating out of your palm..."
    scene ch4sc12_022b with dissolve
    with vpunch
    cb "But out here... {b}I AM THE KING!{/b}"
    cb "You would do well to remember that."
    scene ch4sc12_015b with dissolve
    ed "*Grunts* F-Fine! I'll just have to go after them myself then."
    stop music fadeout 1.5
    scene black with dissolve

    ######ANIMATION#####
    show 032_endani with fade
    play music explore_1 fadein 1.0
    $ renpy.pause(4, hard=True)
    $ renpy.pause ()
    scene black with dissolve
    $ renpy.pause(1)
    stop music fadeout 1.0
    jump ch4sc13

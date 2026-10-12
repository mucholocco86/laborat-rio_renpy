label ch3sc17:

    window hide dissolve
    play music home_2 fadein 1.0
    scene black with Dissolve (1.0)
    $ renpy.pause(1)
    scene ch3sc17_intro with Dissolve(2.0)
    $ renpy.pause()
    scene ch3sc17_001 with Dissolve(2.0)
    $ renpy.pause()
    scene ch3sc17_002 with dissolve
    $ renpy.pause()
    scene ch3sc17_003 with dissolve
    $ renpy.pause()
    scene ch3sc17_004 with dissolve
    $ renpy.pause()
    scene ch3sc17_005 with dissolve
    $ renpy.pause()
    scene ch3sc17_006 with dissolve
    mct "This is the tavern that'll be our home for the next while... 'The Drunken Rooster'"
    scene ch3sc17_007 with dissolve
    mct "Where do they come up with these tavern names? Rusty Spoon... Drunken Rooster..."
    scene ch3sc17_008 with dissolve
    sl "This is the place, my favorite tavern in Luxenford."
    sl "Aren't we meeting Eliza? I don't see her?"
    scene ch3sc17_009 with dissolve
    mc "I appreciate you recommending us this place, I even suggested it to my acquaintance, Borri."
    mc "He said he'd meet us here for ales."
    mc "As for Eliza, she's probably inside already."
    scene ch3sc17_010 with dissolve
    sl "Great! before we head in, though..."
    scene ch3sc17_011 with dissolve
    sl "I’ve been meaning to do this."
    scene ch3sc17_012 with dissolve
    "Before you have a chance to react, Selena leans in and plants her lips halfway between your lips and your cheek."
    scene ch3sc17_013 with dissolve
    "Her lips feel warm and soft, her scent surrounds you... Earthroot and Marigolds."
    "Instead of pulling back, her lips linger... awaiting your response."
    ####Choice####
    menu:
        "Kiss her. ({color=#ff8cdd}Romance{/color})":
            scene ch3sc17_014 with dissolve
            $ selena_kiss = True
            "You turn towards her, merging your lips."
            "Selena immediately responds with a soft moan of excitement as your lips connect."
            $ selena_path = True
            "She runs her fingers through your hair tenderly grabbing it while your kiss becomes more passionate."
            scene ch3sc17_015 with dissolve
            $ renpy.pause(1)
            scene ch3sc17_016 with dissolve
            $ renpy.pause(1)
            scene ch3sc17_015 with dissolve
            $ renpy.pause(1)
            scene ch3sc17_016 with dissolve
            $ renpy.pause(1)
            scene ch3sc17_017 with dissolve
            "Her tender, exotic lips keep pushing against yours with a heated passion."
            "Her lips have a sweetness to them, almost caramel flavored."
            "There’s nothing quite like the intoxicating scent of a woman who desires you."
            scene ch3sc17_018 with dissolve
            "You lean into her and she arches her back with your hands as support."
            sl "Mmhm! MmMmhh!"
            "She presses her tight little body against you, signaling that she won’t deny your hands on her body."
            $ selena_trust += 2
            "Selena is fully into the kiss between the two of you, her trust has increased by {size=+3}{b}{color=#2bff8b}2{/color}{/b}{/size}."
            scene ch3sc17_019 with dissolve
            with vpunch
            uk "{b}*Shouts* Ugh! Get a room you two!{/b}"
            uk "{b}*Shouts* Youthful indecency knows no bounds!{/b}"
            scene ch3sc17_020 with dissolve
            with vpunch
            sl "{b}*Shouts*{/b} How about you mind your own business! {b}You old hag!{/b}"
            sl "{b}*Shouts*{/b} If you can't handle seeing two young lovers having a moment, {b}then shut your eyes!{/b}"
            scene ch3sc17_021 with dissolve
            sl "Ughhh! Some people just have to ruin a good moment..."
            scene ch3sc17_022 with dissolve
            mc "Tell me about it."
            mc "That was a tasty kiss..."
            scene ch3sc17_011 with dissolve
            sl "Mmh... I agree, you're a good kisser."

            if harem_path == True:
                sl "I imagine you've kissed quite a few women..."
                sl "Maybe you've even got a harem? You definitely have the looks and personality for it."
                scene ch3sc17_009 with dissolve
                mc "*Sighs* I don't have a harem... but if I did, I'd definitely invite you."
                mc "You're gorgeous and a great kisser."
                scene ch3sc17_010 with dissolve
                sl "If that kiss was anything to go by... I'd happily accept."
                $ selena_trust += 2
                "Selena enjoys the thought of being in your harem, her trust has increased by {size=+3}{b}{color=#2bff8b}2{/color}{/b}{/size}."

            else:
                pass

            if eliza_path == True:
                sl "I imagine you've been practicing with Eliza?"
                sl "She's head over heels for you, the way she looked at you at the stables..."
                sl "The way she talked about you when she tried to calm me, she has feelings for you."
                scene ch3sc17_009 with dissolve
                mc "I'm well aware..."
                mc "She was talking about me?"
                scene ch3sc17_010 with dissolve
                sl "Mh-hm, she sang your praises."
                sl "A woman does not compliment a guy to another woman unless she is fully smitten."
                scene ch3sc17_011 with dissolve
                sl "And that is the single best indicator a man is of good character."
                sl "Which is why I feel the need to do this..."
                scene ch3sc17_012 with dissolve
                sl "*Mwaah* Mmmhhhh..."
                scene ch3sc17_011 with dissolve

            else:
                pass


            sl "We should probably head inside before they come looking for us..."
            scene ch3sc17_023 with dissolve
            $ renpy.pause(1.5)
            scene ch3sc17_024 with dissolve
            $ renpy.pause(1.5)
            scene ch3sc17_025 with dissolve
            $ renpy.pause(1.5)
            scene ch3sc17_026 with dissolve
            sl "To be continued. *Snickers*"
            mc "You bet..."
            scene black with Dissolve(1.5)

        "Break the kiss. ({color=#2bff8b}Friendship{/color})":
            scene ch3sc17_027 with dissolve
            mc "What’s that for?"
            scene ch3sc17_028 with dissolve
            sl "Just a little thank you for saving me twice."
            scene ch3sc17_027 with dissolve
            mc "Heh... alright, let’s head inside."
            mc "They’re probably waiting for us already."
            scene black with Dissolve(1.5)

    scene black
    stop music fadeout 2.0
    scene ch3sc17_029 with Dissolve(1.5)
    play music tavern_1 fadein 1.0
    "As you open the doors to the tavern you’re hit with the bustling sound of cheers and crowds talking."
    mc "Seems busy tonight..."
    sl "It usually is, the rooms and ales here is relatively cheap compared to the quality."
    sl "Which makes it one of the more popular taverns for the common people."
    scene ch3sc17_030 with dissolve
    sl "Hey... I’ll let you catch up with your friends."
    sl "There’s something I’ve gotta take care of... order whatever you feel like on my tab, okay?"
    scene ch3sc17_031 with dissolve
    mc "Sure, see you later."
    scene ch3sc17_030 with dissolve
    sl "I’ll come join you later, shouldn't take me more than an hour or so."
    sl "Oh and don't order their Firebrand wine, it'll leave you with a burning throat for hours."
    scene ch3sc17_032 with dissolve
    mc "Don't order the Firebrand wine, got it. *Chuckles*"
    $ renpy.pause()
    ###Choice###
    menu:
        "Grab her ass.":
            scene ch3sc17_032
            $ renpy.pause(1)
            scene ch3sc17_033 with dissolve
            $ renpy.pause(1)
            scene ch3sc17_034 with dissolve
            $ renpy.pause(0.3)
            with vpunch
            sl "{b}*Gasps* OH!!{/b}"
            sl "[mc]... this is so... so... indecent."
            scene ch3sc17_035 with dissolve
            mc "Oh is it? *Squeezes firmly*"
            with vpunch
            sl "Oh... Mhh... Grabbing my ass right here in public? *Bites lip* Nnnhh..."
            scene ch3sc17_036 with dissolve
            sl "*Soft moan* Mhaaahh... you’re being naughty."
            scene ch3sc17_037 with dissolve
            mc "*Whisper* {size=-10}{b}See you later, Selena.{/b}{/size}"
            sl "*Whimpers softly* Uh-huuhh... mmh... S-See you later."
            scene ch3sc17_038 with dissolve
            $ selena_trust += 1
            slt "This boy is trouble... but so am I."
            slt "He's definitely going to make things interesting."
            "Selena is intrigued by you, her trust has increased by {size=+3}{b}{color=#2bff8b}1{/color}{/b}{/size}."
            scene ch3sc17_039 with dissolve
            "You and Selena split off and you notice a familiar face sitting at one of the tables."

        "Don't risk it.":
            scene ch3sc17_032
            $ renpy.pause(1)
            "You and Selena split off and you notice a familiar face sitting at one of the tables."
            scene ch3sc17_039 with dissolve

    scene ch3sc17_039
    mct "Oh, Borri is already here."
    scene ch3sc17_040 with dissolve
    br "Oii [mc]! Finally, yer here!"
    br "Come on over. I saved yer a seat!"
    scene ch3sc17_041 with dissolve
    with vpunch
    br "Oi! Innkeep! Two ales!"
    scene ch3sc17_042 with dissolve
    mc "Hey Borri. Have you seen Eliza around?"
    scene ch3sc17_043 with dissolve
    br "Ahh, Eliza. That lass is a beauty, let me tell ye."
    br "Such a sweetheart too! If only she were a dwarf..."
    br "Naye... not even then, me wife is plenty o' trouble fer me! *Chuckles*"
    scene ch3sc17_044 with dissolve
    br "She greeted me earlier but the lass rushed off."
    br "She mumbled something about trying something on, I assume the outfit you mentioned her wanting earlier?"
    scene ch3sc17_045 with dissolve
    br "Said she’d be in yer room until ye came back."
    scene ch3sc17_046 with dissolve
    mc "Thanks Borri, I’ll go check on her."
    mc "Protect my ale until I get back."
    scene ch3sc17_047 with dissolve
    br "Aye! I’ll guard it with me life! *Chuckles*"
    br "But if ye take te long, I can't promise the ale's safety from me thirst! Hah!"
    scene black with Dissolve(1.5)
    stop music fadeout 2.0
    $ renpy.pause(1.5)
    scene ch3sc17_048 with Dissolve(1.5)
    play music home_2 fadein 1.0
    $ renpy.pause(0.5)
    mct "There she is."
    mct "*Chuckles* Of course she's napping... I guess she has been running around all day."
    scene ch3sc17_049 with dissolve
    mct "She sure looks comfortable."
    scene ch3sc17_050 with dissolve
    $ renpy.pause()
    el "Mmmh-mmh..."
    scene ch3sc17_051 with dissolve
    $ renpy.pause()
    el "Nnhh... [mc]... d-don't leave me..."
    scene ch3sc17_052 with dissolve
    $ renpy.pause()
    mct "I wonder what she's dreaming about?"
    scene ch3sc17_053 with dissolve
    $ renpy.pause()
    el "*Whimpers* Nnh-mhh..."
    scene ch3sc17_054 with dissolve
    "You gently stroke her smooth cheek."
    scene ch3sc17_055 with dissolve
    el "*Soft purrs* Hnnh... Mrrrmm..."
    scene ch3sc17_054 with dissolve
    $ renpy.pause(1)
    scene ch3sc17_055 with dissolve
    $ renpy.pause(1)
    scene ch3sc17_054 with dissolve
    $ renpy.pause(1)
    scene ch3sc17_055 with dissolve
    $ renpy.pause(1)
    scene ch3sc17_056 with dissolve
    $ renpy.pause(1)
    el "Nnhh?"
    scene ch3sc17_057 with dissolve
    el "Mmhm... [mc]?"
    scene ch3sc17_058 with dissolve
    mc "Hey... good dreams?"
    scene ch3sc17_057 with dissolve
    el "The best!"
    scene ch3sc17_059 with dissolve
    "She places her little hand in yours."
    el "Your hand is warm. This is nice... Mmh."
    scene ch3sc17_060 with dissolve
    el "Moments like these... I-I..."
    "She stops herself mid-sentence and begins rustling around underneath the sheets."
    scene ch3sc17_061 with dissolve
    $ renpy.pause(1)
    el "Hnngh... one moment!"
    scene ch3sc17_062 with dissolve
    $ renpy.pause(1)
    mc "*Chuckles* What are you up to?"
    scene ch3sc17_063 with dissolve
    $ renpy.pause(1)
    el "Juuuust getting comfy!"
    scene ch3sc17_064 with dissolve
    $ renpy.pause(1)
    el "..."
    scene ch3sc17_065 with dissolve
    $ renpy.pause()
    scene ch3sc17_066 with dissolve
    $ renpy.pause()
    scene ch3sc17_067 with dissolve
    el "I-I missed you."
    scene ch3sc17_066 with dissolve
    $ renpy.pause()
    ###Choice###
    menu:
        "Tell her you missed her. ({color=#ff8cdd}Romance{/color})":
            $ eliza_relationship = True
            scene ch3sc17_068 with dissolve
            mc "I've missed you too, I left Borri hanging with the ales, I wanted to come see you."
            scene ch3sc17_065 with dissolve
            elt "H-He missed me too?"
            elt "I thought I was just being silly for missing him so soon."
            scene ch3sc17_066 with dissolve
            $ renpy.pause()

            if selena_path == True:
                mc "Hey... so, I have to tell you something."
                el "Hmm?"
                scene ch3sc17_068_b with dissolve
                mc "Something happened outside the tavern just now, with Selena."
                mc "We... kissed."
                el "Hmmfh..."
                scene ch3sc17_067_b with dissolve
                el "*Sighs* I had a feeling that was going to happen."
                el "When we were at the stables... she was obviously very attracted to you."
                el "I knew she would try to seduce you... hnnnghh..."
                scene ch3sc17_068_b with dissolve
                mc "I didn't want to make you feel bad, but we promised we'd be honest, always."
                mc "Did I hurt you?"
                el "*Shakes head* ..."
                scene ch3sc17_066 with dissolve
                el "*Scoffs* ..."
                scene ch3sc17_065 with dissolve
                el "......"
                scene ch3sc17_067 with dissolve
                el "I'm glad you told me, it means a lot."
                el "And know, I'm not hurt, as I said I expected it."
                el "I'll always be your number one, right?"
                scene ch3sc17_068 with dissolve
                mc "Always, Eliza."
                scene ch3sc17_067 with dissolve
                el "Then there's nothing to worry about, do I like the idea of her kissing you?"
                el "Obviously not, but as long as you respect me enough not to do it in front of me..."
                el "I'll be okay, and I'd prefer not to be told about what happens with other women."
                scene ch3sc17_066 with dissolve
                mc "Deal, I won't bring up other women unless you ask about them yourself."
                el "*Nods in agreement* Mh-hm!"

            else:
                pass

            scene ch3sc17_067 with dissolve
            el "Hold me for a while?"
            scene ch3sc17_066 with dissolve
            mc "You know I can’t refuse you..."
            mc "Especially when you're asking like the cutest little kitten."
            scene ch3sc17_067 with dissolve
            el "*Giggling* That's me... your cute kitten."
            el "Now make some room!"
            $ eliza_path = True
            scene ch3sc17_069 with dissolve
            $ renpy.pause()
            scene ch3sc17_070 with dissolve
            $ renpy.pause()
            scene ch3sc17_071 with dissolve
            el "So. Missed me, huh?"
            scene ch3sc17_072 with dissolve
            mc "Yes... You’re enjoying this a bit too much."
            "She gently pushes your hand lower."
            scene ch3sc17_073 with dissolve
            el "I don’t know what you’re talking about..."
            scene ch3sc17_074 with dissolve
            $ renpy.pause()
            el "*Soft moan* Mhffmhm..."
            elt "Heavens! I can't stop myself when we're alone... I love feeling his touch."
            elt "Mmh... he's caressing my breast... mmh... they belong to him."
            scene ch3sc17_075 with dissolve
            $ renpy.pause()
            "Eliza’s breathing increases as the tip of your finger makes contact with her soft little nipple."
            scene ch3sc17_076 with dissolve
            $ renpy.pause()
            "You continue rubbing her nipple then releasing it, allowing her soft moans to guide you."
            "Each time you release the tension from her nipple, it bounces back to it’s perky position and she moans softly."
            scene ch3sc17_074 with dissolve
            $ renpy.pause(1)
            scene ch3sc17_075 with dissolve
            $ renpy.pause(1)
            scene ch3sc17_076 with dissolve
            $ renpy.pause(1)
            scene ch3sc17_074 with dissolve
            $ renpy.pause(1)
            scene ch3sc17_075 with dissolve
            $ renpy.pause(1)
            scene ch3sc17_076 with dissolve
            $ renpy.pause(1)
            el "Mhhh! [mc]! Gently... They're really Mhhhm... sensitive, you know."
            scene ch3sc17_077 with dissolve
            "She completely surrenders herself to you, to the feelings you're bringing out in her."
            scene ch3sc17_078 with dissolve
            el "I love being in your arms like this. Feeling your hands on me. Grabbing me. Squeezing me. Touching me."
            scene ch3sc17_079 with dissolve
            el "I would never let anyone see me like this or explore me like this. Just you. Only you."
            el "I never would've imagined how sensitive my breasts are..."
            el "It feels good when I touch them myself..."
            el "But when your hands explore them, it's like... a whole different sensation."
            el "It's like they're eager for your affection... for your touch."
            scene ch3sc17_080 with dissolve
            mc "I will never deny you the affection you desire."
            scene ch3sc17_081 with dissolve
            mc "Or the attention that your perfect breasts crave."
            scene ch3sc17_079 with dissolve
            el "Perfect? You really think so? I know they aren’t the biggest..."
            scene ch3sc17_080 with dissolve
            mc "They’re exactly as I like them. Squishy and soft, yet firm and perky."
            scene ch3sc17_081 with dissolve
            mc "Exploring your beautiful body is something I want to do every time I look at you."
            scene ch3sc17_082 with dissolve
            with vpunch
            $ renpy.pause()
            "Before you have a chance to speak any more honeyed words, Eliza leans up and catches your lips with hers."
            "Soft and tender, her lips embrace yours in a longing kiss."
            "And her hand holds the back of your neck, ensuring you can’t move away."
            scene ch3sc17_083 with dissolve
            "Her naked body presses back against you, rubbing her scent all over you as the gentle kiss continues."
            scene ch3sc17_084 with dissolve
            "She pauses the kiss for a few heartbeats, her mouth still close to your own and her warm breath lingering on your lips."
            scene ch3sc17_085 with dissolve
            "Then you feel her sweet kiss once more, this time more urgent with passion. More... raw lust."
            show mc_el_kiss3 with fade
            $ renpy.pause(2, hard=True)
            "She playfully teases your tongue with hers, sharing her saliva with you as she twines her tongue against yours."
            "Despite you being the first guy she’s ever kissed, she’s learning rapidly just by listening to her own desires."
            scene ch3sc17_087 with dissolve
            "As she continues playing with your tongue, your hands begin playing with her body in turn."
            "She whimpers into your mouth as you tenderly caress her mesmerizing breasts."
            scene ch3sc17_086 with dissolve
            el "Mhpfff! Mhhmm! Hmmhhm..."
            "Her left breast fits perfectly into your hand as you squeeze it firmly."
            el "*Moans* Aahhmmh! Y-Your hand... Feels so... Mmh! Amazing!"
            scene ch3sc17_087 with dissolve
            el "*Whispers* I need... Mmhm."
            scene ch3sc17_088 with dissolve
            el "I need you in my mouth right now!"
            el "Please? Can I... taste you again?"
            mc "*Nods* Mhmn-hm."
            scene ch3sc17_089 with dissolve
            with vpunch
            "Heavy doorknocks."
            with vpunch
            scene ch3sc17_090 with dissolve
            mct "Are you fucking kidding me?"
            scene ch3sc17_091 with dissolve
            elt "Seriously! Just as I was about to enjoy his... cock."
            elt "I really wanted to taste him..."
            scene ch3sc17_092 with dissolve
            with vpunch
            br "*Knocking* [mc], Eliza. Ye in there?"
            br "Just checking if everything is alright? Ye have been gone a while."
            scene ch3sc17_093 with dissolve
            mc "Everything is fine, Borri. We’ll be out in a few."
            scene ch3sc17_092 with dissolve
            br "Alright, sounds good! I’ll leave yer to it then."
            scene ch3sc17_094 with dissolve
            el "*Sigh* Talk about bad timing, huh?"
            el "I was going to show you what I was dreaming about when you woke me."
            scene ch3sc17_095 with dissolve
            mc "Tell me about it... you got me really excited there."
            scene ch3sc17_094 with dissolve
            el "I could tell. *Giggling* You've been poking my back vigorously!"
            el "I suppose we did get a little carried away."
            el "You'll just have to fill my mouth another time."
            scene ch3sc17_095 with dissolve
            mc "Already looking forward to it."
            scene ch3sc17_096 with dissolve
            el "*Giggles* You and me both."
            el "I better get dressed, though."
            scene ch3sc17_097 with dissolve
            $ renpy.pause()
            scene ch3sc17_098 with dissolve
            $ renpy.pause()
            scene ch3sc17_099 with dissolve
            $ renpy.pause()
            scene ch3sc17_100 with dissolve
            elt "I love how he can’t take his eyes off me."
            elt "He really does make me feel wanted. Desired. Loved."
            scene ch3sc17_101 with dissolve
            el "See something you like back there?"
            scene ch3sc17_102 with dissolve
            mc "'Something I like' would be the understatement of the century."
            scene ch3sc17_103 with dissolve
            el "As much as I enjoy teasing you, I can’t wait to show you my new outfit!"
            el "So I'll have to get dressed."
            scene ch3sc17_104 with dissolve
            el "Prepare to be amazed!"
            el "I managed to find something that really fits!"
            scene ch3sc17_105 with dissolve
            el "Hnnnghh!"
            scene ch3sc17_106 with dissolve
            el "*Moans* Hrrhhr!"
            scene ch3sc17_105 with dissolve
            el "I put it down here so you wouldn’t notice it... Hrrrmmh!"
            scene ch3sc17_106 with dissolve
            el "Nnhhh! Just a little further!"
            scene ch3sc17_107 with dissolve
            mct "By all that is Divine... grant me strength."
            scene ch3sc17_108 with dissolve
            mct "The things I'd do to that perky little ass..."
            scene ch3sc17_106 with dissolve
            $ renpy.pause(1.5)
            scene ch3sc17_108 with dissolve
            $ renpy.pause(1.5)
            scene ch3sc17_106 with dissolve
            $ renpy.pause(1.5)
            scene ch3sc17_108 with dissolve
            el "Hrraaaa... Almost got it!"
            ####CHOICE####
            menu:
                "Spank her.":
                    scene black with dissolve
                    "You carefully sneak up behind her while she's searching for her clothes."
                    scene ch3sc17_109 with dissolve
                    with vpunch
                    el "*Surprised moan* {b}Yhiiiiihh!{/b}"
                    scene ch3sc17_110 with dissolve
                    with vpunch
                    "You spank her tight ass once more. Firmly."
                    el "{size=+3}{b}*Squeals* AIIIHH!{/b}{/size}"
                    scene ch3sc17_111 with dissolve
                    "She loses her balance in surprise."
                    el "Uwwaahh!"
                    scene ch3sc17_112 with dissolve
                    $ renpy.pause(1.5)
                    scene ch3sc17_113 with dissolve
                    with vpunch
                    el "Owwhh!"
                    el "What in the five hells, [mc]?!"
                    scene ch3sc17_114 with dissolve
                    mc "That’s what you get for teasing me."
                    mc "You really thought I was going to let you flaunt that perky ass of yours without getting a feel?"
                    scene ch3sc17_115 with dissolve
                    el "*Growls* Hhrrrh."
                    scene ch3sc17_116 with dissolve
                    $ eliza_trust += 2
                    elt "I definitely won’t tell him how good it felt when he slapped my ass."
                    "Eliza likes that you took the chance to spank her, her trust has increased by {size=+3}{b}{color=#2bff8b}2{/color}{/b}{/size}."
                    scene ch3sc17_117 with dissolve
                    el "Are you done harassing my poor ass?"
                    scene ch3sc17_114 with dissolve
                    mc "For now."
                    scene ch3sc17_118 with dissolve
                    el "Good! Then sit back and let me show you the outfit."
                    el "You're going to love it. Just wait!"
                    el "Remember, I want your unfiltered opinion..."

                "Don’t risk it.":
                    scene ch3sc17_108 with dissolve
                    el "Found it! Just sit back and be amazed!"
                    scene ch3sc17_118 with dissolve
                    el "Promise you will give me your honest opinion?"
                    scene ch3sc17_114 with dissolve
                    mc "Cross my heart."

            scene ch3sc17_119 with dissolve
            mct "I love how confident and comfortable she's become when she's naked in front of me."
            mct "She has come a long way from the shy girl I found in the woods."
            mct "She’s a lot stronger now, she constantly pushes herself to the edge and beyond for me."
            scene ch3sc17_120 with dissolve
            "She begins dressing in front of you. One piece at a time."
            scene ch3sc17_121 with dissolve
            $ renpy.pause()
            el "The outfit comes with these sleeve-gloves."
            scene ch3sc17_122 with dissolve
            $ renpy.pause()
            el "Pretty cool, huh?"
            scene ch3sc17_123 with dissolve
            $ renpy.pause()
            mc "Mh-hm, I'm liking what I see."
            scene ch3sc17_124 with dissolve
            $ renpy.pause()
            el "*Giggling* ..."
            scene ch3sc17_125 with dissolve
            el "You look like you’re ready to devour me."
            scene ch3sc17_126 with dissolve
            mc "I definitely feel my appetite growing rapidly..."
            mc "Keep getting dressed like this and I might just have to skip dinner in favor of dessert."
            scene ch3sc17_125 with dissolve
            el "Pace yourself."
            el "If you're lucky, I may let you have a taste later."
            scene ch3sc17_127 with dissolve
            elt "Heavens! When he looks at me like that with those red eyes..."
            elt "Knowing that I'm the reason they turned red... from his desire for... me, I like having this effect on him."
            scene ch3sc17_128 with dissolve
            elt "I already feel myself dripping."
            elt "If it wasn't for these panties, he'd see my... excitement... running down my thighs."
            scene ch3sc17_129 with dissolve
            elt "I never imagined I'd meet someone like him... someone who could make me feel like this."
            elt "I'd better get dressed before I jump him!"
            scene ch3sc17_126 with dissolve
            mc "Eliza..."
            mc "You're pushing my limits here."
            scene ch3sc17_125 with dissolve
            el "Right! My bad! Back to it."
            scene ch3sc17_130 with dissolve
            $ renpy.pause()
            scene ch3sc17_131 with dissolve
            $ renpy.pause()
            scene ch3sc17_132 with dissolve
            $ renpy.pause()
            scene ch3sc17_133 with dissolve
            $ renpy.pause()
            scene ch3sc17_134 with dissolve
            $ renpy.pause()
            scene ch3sc17_135 with dissolve
            $ renpy.pause()
            scene ch3sc17_136 with dissolve
            $ renpy.pause()
            scene ch3sc17_137 with dissolve
            $ renpy.pause()
            scene ch3sc17_138 with dissolve
            $ renpy.pause()
            scene ch3sc17_139 with dissolve
            el "So... What do you think?"
            scene ch3sc17_140 with dissolve
            el "Coin well spent?"
            scene ch3sc17_141 with dissolve
            mc "..."
            mc "From now on you can be in charge of our coin whenever."
            scene ch3sc17_140 with dissolve
            el "*Giggles* That good, huh?"
            scene ch3sc17_141 with dissolve
            mc "You look like a..."
            #### CHOICE ####
            menu:
                "Radiant Rogue.":
                    scene ch3sc17_142 with dissolve
                    el "Oh yeah?"
                    scene ch3sc17_143 with dissolve
                    el "I suppose I can be a bit of a Rogue!"
                    el "Watch out or I might just steal your heart!"
                    $ eliza_trust += 1
                    "Eliza’s trust has increased by {size=+3}{b}{color=#2bff8b}1{/color}{/b}{/size}."
                "Seductive Swashbuckler.":
                    scene ch3sc17_142 with dissolve
                    el "Seductive eh? I’ll take it!"
                    scene ch3sc17_144 with dissolve
                    el "I can tell my seduction is having its intended effect."
                    $ eliza_trust += 1
                    "Eliza’s trust has increased by {size=+3}{b}{color=#2bff8b}1{/color}{/b}{/size}."
                "Tantalizing Temptress.":
                    scene ch3sc17_142 with dissolve
                    el "Temptress, huh? Makes sense. I do very much enjoy tempting you."
                    scene ch3sc17_145 with dissolve
                    el "And judging from that bulge in your pants, you're definitely enjoying it too!"
                    $ eliza_trust += 1
                    "Eliza’s trust has increased by {size=+3}{b}{color=#2bff8b}1{/color}{/b}{/size}."

            scene ch3sc17_146 with dissolve
            mc "Yeah, yeah..."
            el "*Giggling* What? Was it something I said hmm?"
            mc "*Chuckles* Let’s go before Borri comes back."
            scene ch3sc17_147 with dissolve
            mc "Speaking of... he's probably emptied our mugs by now."
            scene ch3sc17_148 with dissolve
            $ renpy.pause()
            scene ch3sc17_149 with dissolve
            el "He was in a very celebratory mood when he told me that you suggested he join us at the Adventurers Guild."
            el "I don't think I've seen him that excited before."
            scene ch3sc17_150 with dissolve
            mc "Mh. You think it’s a bad idea?"
            scene ch3sc17_149 with dissolve
            el "No, I was just surprised that you had suggested it! But it makes total sense."
            scene ch3sc17_151 with dissolve
            el "Borri seems to be capable of taking care of himself. I’m sure he’s strong as an ox!"
            scene ch3sc17_150 with dissolve
            mc "An Ox, huh? What about me?"
            mc "Which animal would I be?"
            scene ch3sc17_152 with dissolve
            el "Hmmm... HHmmm!"
            scene ch3sc17_153 with dissolve
            el "*Mumbles* You would be... HMhh..."
            scene ch3sc17_154 with dissolve
            mc "..."
            scene ch3sc17_155 with dissolve
            mc "I’ll head to the bar before Borri drinks my ale. Let me know when you come to a conclusion."
            scene ch3sc17_156 with dissolve
            $ renpy.pause(1.5)
            "As you reach the door you feel something pulling the back of your shirt."
            scene ch3sc17_157 with dissolve
            el "Don’t."
            el "Don’t go."
            scene ch3sc17_158 with dissolve
            "She tenderly grabs your arm as she moves in closer behind you."
            scene ch3sc17_159 with dissolve
            "You feel the warmth of her nimble body pressing against your back as she wraps her arms around your waist."
            scene ch3sc17_160 with dissolve
            $ renpy.pause()
            scene ch3sc17_161 with dissolve
            el "*Soft Whisper* {size=-7}{b}You’re much more than an Ox.{/b}{/size}"
            scene ch3sc17_162 with dissolve
            el "*Sensual whisper* {size=-7}{b}You’re an...{/b}{/size}"
            scene ch3sc17_163 with dissolve
            el "*Sensual whisper* {size=-7}{b}Arazalian Lion.{/b}{/size}"
            el "*Sensual whisper* {size=-7}{b}My lion.{/b}{/size}"
            el "*Sensual whisper* {size=-7}{b}A kitten and her lion, mmmh.{/b}{/size}"
            scene ch3sc17_164 with dissolve
            $ renpy.pause(1)
            "She gently nibbles the back of your ear with her soft wet lips"
            scene ch3sc17_165 with dissolve
            "She continues nibbling while she softly moans, sending small vibrations into your ear."
            #### ANIMATION# ###
            show mc_el_nibble1 with fade
            $ renpy.pause(2, hard=True)
            mct "This girl... she has an effect on me unlike anything I’ve ever felt before."
            mct "She... She makes me forget."
            mct "All the pain, the guilt, the loneliness... it all disappears when I’m with her."
            scene ch3sc17_165 with dissolve
            $ renpy.pause(1.5)
            scene ch3sc17_166 with dissolve
            mc "Lion, huh? I guess it beats being an Ox... Heh."
            scene ch3sc17_165 with dissolve
            el "*Sucks gently* Nnh-hmm... I much prefer my lion."
            scene ch3sc17_166 with dissolve
            mc "*Chuckles* 'Your' lion, huh? You're claiming me?"
            scene ch3sc17_165 with dissolve
            el "*Sucks gently* As your kitten, it's my responsiblity to imprint on you... mmh..."
            scene ch3sc17_167 with dissolve
            $ renpy.pause(0.5)
            "You turn around and hold her closely."
            scene ch3sc17_168 with dissolve
            el "A beautiful girl in your arms just imprinted on you..."
            scene ch3sc17_169 with dissolve
            el "Question is, what are you going to do about that?"
            scene ch3sc17_170 with dissolve
            mc "I can think of a few things..."
            scene ch3sc17_168 with dissolve
            el "Oh? You'd better hurry up and do it then-"
            scene ch3sc17_171 with dissolve
            with vpunch
            el "*Muffled moan* Mhh! Mhhnn! Mhmmm..."
            mct "Her lips are so soft. Every time our lips connect, a warm sizzling feeling builds inside me."
            scene ch3sc17_172 with dissolve
            el "Mmhm! *Soft moans* Aahhnn... Mhm..."
            elt "I love when he kisses me! Nnhhh..."
            #### ANIMATION# ###
            show mc_el_kiss4 with fade
            $ renpy.pause(2, hard=True)
            elt "Mhahh! He's kissing me so tenderly."
            elt "The way he's holding onto me as we kiss..."
            elt "I can feel how Mhmmh... precious I am to him."
            elt "I will never hurt you, [mc]. You are the one for me."
            scene ch3sc17_172 with dissolve
            $ renpy.pause()
            scene ch3sc17_173 with dissolve
            "Her wet lips have a suction-like effect as you slowly pull away."
            scene ch3sc17_174 with dissolve
            el "*Moan* Nhh! ... Nmmhh..."
            "She keeps pulling you back in for more kisses"
            scene ch3sc17_173 with dissolve
            $ renpy.pause(1)
            scene ch3sc17_174 with dissolve
            $ renpy.pause(1)
            scene ch3sc17_173 with dissolve
            $ renpy.pause(1)
            scene ch3sc17_174 with dissolve
            $ renpy.pause(1)
            "Her lips reluctantly release yours."
            scene ch3sc17_176 with dissolve
            elt "Hnngh..."
            scene ch3sc17_168 with dissolve
            el "I... I needed that."
            scene ch3sc17_177 with dissolve
            mc "Your lips... they taste like..."
            mc "Like how I imagine fruit from the highest heavens would taste."
            scene ch3sc17_178 with dissolve
            elt "..."
            elt "He's so romantic! I'm going to melt... Nyahh!"
            scene ch3sc17_179 with dissolve
            el "You’re going to make me blush!"
            el "What is a girl to do with you and your honeyed words?"
            stop music fadeout 1.0
            scene ch3sc17_180 with dissolve
            play music lewd_1 fadein 1.0
            el "Nevermind that question..."
            el "I know what to do with you."
            "She teasingly trace her finger down your chest while her other hand reaches her mark."
            scene ch3sc17_181 with dissolve
            "She curiously keeps her gaze fixed upon you as her hand slides into your pants."
            scene ch3sc17_182 with dissolve
            el "Mhh! There he is... Just as big and warm as I remember him."
            el "I believe I was about to taste you when Borri so rudely interrupted us earlier..."
            scene ch3sc17_183 with dissolve
            el "Let’s get you out of these."
            scene ch3sc17_184 with dissolve
            $ renpy.pause(1)
            el "Your body really turns me on... the way your muscles catches the light..."
            el "The feel of your scars as my fingers glide over them..."
            el "The way your beautiful cock hardens at my touch..."
            scene ch3sc17_185 with dissolve
            mc "Eliza... we don't have time-"
            scene ch3sc17_186 with dissolve
            el "Shhh."
            el "Let me take care of you, like only your kitten can."
            scene ch3sc17_187 with dissolve
            el "*Sensual tone* {b}My lion.{/b}"
            scene ch3sc17_188 with dissolve
            $ renpy.pause(1.5)
            scene ch3sc17_189 with dissolve
            $ renpy.pause(1.5)
            scene ch3sc17_190 with dissolve
            el "Seems like something needs my full, undivided attention."
            scene ch3sc17_186 with dissolve
            mc "You don’t hav-"
            scene ch3sc17_191 with dissolve
            el "Ahh-ah! You’re hard... really hard. Because of me..."
            el "I'd be a bad kitten if I didn’t take care of you."
            scene ch3sc17_192 with dissolve
            $ renpy.pause()
            el "A good kitten takes care of her lion. Whenever he needs it."
            el "He looks so delicious!"
            scene ch3sc17_193 with dissolve
            "She looks up to you with a hungry smile."
            mct "The sight of her kneeling in front of me is so hot!"
            scene ch3sc17_194 with dissolve
            el "I won’t stop until your cum fills the back of my throat."
            scene ch3sc17_195 with dissolve
            mc "You're the devil incarnate."
            scene ch3sc17_196 with dissolve
            elt "Just the thought of having his beautiful cock fill out my little mouth..."
            elt "How I'll keep sucking and licking until he gives me his seed."
            scene ch3sc17_197 with dissolve
            elt "It's so warm and rock hard in my hand... it pulses with life. My panties are soaked just looking at it!"
            "Eliza begins stroking you with a firm grip, she’s no longer shy about touching you."
            scene ch3sc17_196 with dissolve
            $ renpy.pause(1)
            scene ch3sc17_197 with dissolve
            $ renpy.pause(1)
            scene ch3sc17_196 with dissolve
            $ renpy.pause(1)
            scene ch3sc17_196 with dissolve
            $ renpy.pause(1)
            scene ch3sc17_197 with dissolve
            $ renpy.pause(1)
            scene ch3sc17_196 with dissolve
            $ renpy.pause(1)
            scene ch3sc17_194 with dissolve
            el "Remember, I won't stop until you fill my mouth with all your cum."
            el "Every. Last. Drop."
            scene ch3sc17_195 with dissolve
            mc "Fuck... go on."
            scene ch3sc17_198 with dissolve
            "As her bottom lip softly makes contact with your tip, she pauses to let her hot breath surround you."
            "She teasingly blows air onto your tip, grazing it with her lips each time."
            scene ch3sc17_199 with dissolve
            $ renpy.pause(1)
            scene ch3sc17_198 with dissolve
            $ renpy.pause(1)
            scene ch3sc17_199 with dissolve
            $ renpy.pause(1)
            scene ch3sc17_200 with dissolve
            $ renpy.pause(1)
            scene ch3sc17_201 with dissolve
            $ renpy.pause(1)
            #### ANIMATION ####
            show el_bj_ani2 with fade
            $ renpy.pause(2, hard=True)
            "With soft moans, she licks the tip of your cock slowly and inquisitively at first."
            "But soon her tongue eagerly massages and lubricates your tip with her saliva."
            "Her wet tongue caresses you intimately. Each of her gentle licks across your tip sends shivers through your cock."
            scene ch3sc17_202 with dissolve
            $ eliza_bj = True
            "After thoroughly massaging your cock with her tongue, she prepares you for entry."
            #### ANIMATION ####
            show el_bj_ani3 with fade
            $ renpy.pause(2, hard=True)
            $ renpy.pause()
            el "*Moans* Mhh! ... HMmhhh!"
            "She can’t seem to fit all of you inside her little mouth, but she keeps sucking eagerly while getting used to your size."
            el "Mmhm... Hhrrhh! MaHh!"
            "As her cheeks and jaw gets more comfortable with your cock she pushes you further inside."
            scene ch3sc17_203 with dissolve
            "You can feel the soft wet sides of her cheeks surrounding your tip."
            "She pauses for a few moments getting used to breathing through her nose."
            "Then you feel her wet tongue resume rubbing your cock, coating it with more saliva as her soft moaning begins to fill the room once more."
            #### ANIMATION ####
            show el_bj_ani4 with fade
            $ renpy.pause(2, hard=True)
            $ renpy.pause()
            el "*Muffled moans* Mhhawhh... MMmmh! Mhhnnnn! Hhhnn!"
            mc "Fuck! Eliza... Ahhh! You’re... amazing."
            "Her moans grow even louder as she responds to hearing how much pleasure she is giving you."
            "Every time she pushes you all the way she twists her head back and forth while pushing her tongue against your tip."
            "Her muffled moans vibrate into your cock sending you close to the edge."
            el "MmMhh!! Mhhhh... Mhhrhhm!"
            mc "I’m... I’m close, Eliza. Fuck, your mouth feels amazing..."
            "Hearing your words, she increases her suction by tightening her soft lips around your hard cock-"
            "- her tongue continuing to rub your tip eagerly."
            with vpunch
            mc "I'm... I'm cumming!"
            with vpunch
            $ renpy.pause(1)
            with vpunch
            scene ch3sc17_204 with dissolve
            "She grabs onto your thigh firmly as you fill her throat with your warm cum."
            with vpunch
            "You shoot one final load while she keeps squeezing your cock with her mouth."
            scene ch3sc17_205 with dissolve
            $ renpy.pause(1)
            "Eliza sits still for a few seconds, her mouth filled with your seed..."
            scene ch3sc17_206 with dissolve
            $ renpy.pause(1)
            el "*Gulps* Mmmh... *Gulp* Nnnhh..."
            scene ch3sc17_207 with dissolve
            "After swallowing all your hot cum, she proudly presents her clean tongue to you."
            $ renpy.pause(0.5)
            mc "Well done, Kitten, you really drained me with that sexy little mouth of yours."
            scene ch3sc17_208 with dissolve
            el "Thank you. That was delicious!"
            scene ch3sc17_209 with dissolve
            mc "I should be the one thanking you... That was incredible, Eliza."
            mc "I've never felt pleasure like that. Never."
            scene ch3sc17_210 with dissolve
            elt "He enjoyed it! I love pleasing him..."
            elt "He tasted so good! Like... so good!"
            $ eliza_trust += 3
            "Eliza is happy that she was able to satisfy you, her trust has increased by {size=+3}{b}{color=#2bff8b}3{/color}{/b}{/size}."
            scene ch3sc17_211 with dissolve
            el "It was incredible for me too, [mc]. I love tasting you."
            scene ch3sc17_210 with dissolve
            $ renpy.pause()
            scene ch3sc17_211 with dissolve
            el "If we didn't have somewhere to be... I'd already be sucking you again."
            scene ch3sc17_212 with dissolve
            el "But now you better go meet Borri. I’ll just be a second."
            scene ch3sc17_213 with dissolve
            mc "Hey..."
            mc "Don’t be embarrassed with me, Eliza."
            scene ch3sc17_214 with dissolve
            el "I'm not... I need to change my panties."
            el "They’re completely soaked after sucking your cock!"
            scene ch3sc17_215 with dissolve
            with vpunch
            el "Now get out of here you big buffoon!"
            el "Let a girl change her wet panties in peace! *Snickers*"
            scene ch3sc17_216 with dissolve
            mc "It’s kinda hot when you’re being forceful."
            scene ch3sc17_217 with dissolve
            el "*Laughs* You’re impossible!"
            scene ch3sc17_216 with dissolve
            mc "One of my many charms."
            scene ch3sc17_215 with dissolve
            el "Uh-huh, I see."
            el "Then go put them to use on Borri!"
            $ eliza_trust += 1
            "Eliza enjoys bantering with you, her trust has increased by {size=+3}{b}{color=#2bff8b}1{/color}{/b}{/size}."
            scene black with Dissolve(2)
            stop music fadeout 1.0
            $ renpy.pause(1)
            jump ch3sc18

        "Tell her it’s been a long day. ({color=#2bff8b}Friendship{/color})":
            scene ch3sc17_068 with dissolve
            mc "It’s been busy today."
            mc "I met Borri earlier, and he had money troubles so I suggested he could join our guild."
            scene ch3sc17_067 with dissolve
            el "Oh, that’s certainly unexpected. But I think he'd make a great fit!"
            scene ch3sc17_068 with dissolve
            $ eliza_relationship = False
            mc "Mh. I agree. He’s strong and hardworking."
            mc "I also met Selena on the way. She was having some troubles with a thug harassing her."
            scene ch3sc17_067_b with dissolve
            el "Did he hurt her?"
            scene ch3sc17_068_b with dissolve
            mc "He was about to, but I stepped in before it got out of hand."
            mc "They seemed to know each other and she told me a bit about him and their past."
            scene ch3sc17_067_b with dissolve
            $ eliza_path = False
            el "Jealous ex?"
            scene ch3sc17_068_b with dissolve
            mc "Nah, she was in a bad spot when she first arrived in Luxenford."
            mc "Long story short, she turned to thievery to survive."
            scene ch3sc17_067_b with dissolve
            el "And this man was from that stage of her life?"
            scene ch3sc17_068_b with dissolve
            mc "Pretty much. She’s fine now, though. She’s here at the tavern to hang out with us tonight"
            scene ch3sc17_067 with dissolve
            el "Ahh, good! I like her. It’s just nice to have another girl around sometimes."
            scene ch3sc17_068 with dissolve
            mc "Sure, I get that. You good to head downstairs? I have a feeling Borri will be drinking my ale if I take too long."
            scene ch3sc17_067 with dissolve
            el "Sure! Let’s go... Uh, I’ll just put my new outfit on real quick! I’ll meet you at the table."
            scene black with Dissolve(2)
            $ renpy.pause(1)
            stop music fadeout 2.0
            jump ch3sc18

    scene black dissolve

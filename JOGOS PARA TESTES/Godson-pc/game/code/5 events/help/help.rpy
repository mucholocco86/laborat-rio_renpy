label dad1:

    scene black
    with slowfade

    pause 1.0

    play music my_audio["dungeon ambience"] fadein 2.0 loop

    scene i84
    with slowfade

    voice my_audio["212"]
    nar "The warmth of feeling your cock inside Marnie's warm slimy dripping wet body fades faster than it should. You try to hold on, but something is....off."
    voice my_audio["213"]
    nar "It’s the silence that wakes you first, not peace, but a silence that feels thick, unnatural, like the air is holding its breath."

    scene i85
    with medium_dissolve

    voice my_audio["214"]
    nar "When your eyes open, you're no longer in your room. Stone walls surround you. Cold. Damp. Ancient. You're sitting upright on a slab of rock, arms limp, skin bare, and everything feels wrong."
    voice my_audio["215"]
    nar "Your ears catch something before your brain does, footsteps, maybe? No. A breath. Someone else is here."
    voice my_audio["216"]
    nar "Your instincts scream, but your body remains still."
    voice my_audio["217"]
    nar "Your eyes lock forward. There, across from you....sits a man. Silent. Waiting. Watching."

    scene i86
    with medium_dissolve

    voice my_audio["218"]
    nar "He’s seated on a narrow wooden bench, elbows resting between his knees, holding a worn black fedora loosely in both hands like it carries the weight of something sacred."
    voice my_audio["219"]
    nar "The lines on his face speak of time. Hard time. A life lived sharply and not without scars. His clothes are elegant but weathered, like something expensive worn for far too long in the wrong place."
    voice my_audio["220"]
    nar "He stares at you with a calm intensity that sends a chill down your spine... and something in your chest starts to tighten, as if your soul recognizes him before your mind catches up."

    play sound2 my_audio["bang sound 1"] noloop
    scene i87
    with hpunch

    voice my_audio["221"]
    nar "That face...that posture....."
    voice my_audio["222"]
    nar "It’s your father!"

    scene i88
    with medium_dissolve

    mc "........."
    mc ".............."

    $ freedfather = True

    menu:
        ".....dad?":



            pass
        "It can't be....":

            pass
        "What.....what the hell is going on?":

            pass
        "Dad, is that you?":

            pass

    scene black
    with slowfade

    scene i89
    with medium_dissolve
    pause

    scene i90
    with medium_dissolve

    menu:
        "Dad, what the hell is this? Am I dreaming?":



            pass
        "What is this? Are you alive? What's going on, or better yet, where the hell are we?":

            pass
        "The fuck is going on here, dad!?":

            pass

    stop music fadeout 2.0

    scene i91
    with medium_dissolve
    pause

    scene i92
    with medium_dissolve

    syl "Have I ever told you the story of the Queen Beyond the Winter Sea?"

    menu:
        mc ""
        "What?":


            syl "An entirely reasonable response. Most worthwhile stories begin with confusion."
            pass
        "The fuck are you talking about?":


            syl "There it is. That delicate curiosity of yours. Your mother must be very proud."
            pass
        "Huh?":


            mc "Huh?"
            syl "Exactly. Consider that the sound of your mind preparing to be disappointed."
            pass
        "No, but please explain.":


            syl "Polite, attentive, and trapped in a dungeon with nowhere else to go. The perfect audience."
            pass

    play sound my_audio["evilsneaky3"] loop
    scene i93
    with medium_dissolve

    syl "Years ago, I discovered a place that was never meant to be found. Not on any respectable map, anyway."
    syl "It lay beyond a sea that seemed to stretch forever, hidden behind storms violent enough to tear steel from a ship and courage from a man."
    syl "But beyond those storms was an island unlike anything I'd ever seen. White cliffs, golden towers, forests untouched by axes, and women carrying swords as naturally as other people carry handbags."
    syl "They were warriors, every one of them. Disciplined, powerful, and deeply suspicious of men. Under normal circumstances, they would've thrown me back into the sea before my shoes had finished drying."

    scene i94
    with medium_dissolve

    syl "Hah! But these were not normal circumstances!"
    syl "They had been waiting for someone. Not me, precisely... but something they believed I carried."
    syl "The women watched me as though I were a locked box and each of them possessed a different theory about what might be inside."
    syl "Then their queen arrived. Tall, magnificent, and beautiful in the sort of way that makes intelligent men temporarily misplace their intelligence."
    syl "She smiled at me, oh she did! Then she took my hand, and welcomed me as an honoured guest. And against every instinct I'd spent a lifetime sharpening... I believed her."

    scene i95
    with medium_dissolve

    syl "They dressed me in silk, filled my glass with wine, and prepared a feast large enough to bankrupt a small nation."
    syl "The queen sat beside me all evening. She asked about my world, my family, my work... although I suspect she already knew far more than she admitted."
    syl "She spoke of destiny. Of an ancient position left vacant. Of a man who had vanished from their world and a power that had crossed somewhere it did not belong."
    syl "At the time, I assumed she was speaking in riddles to appear mysterious. Powerful people adore riddles. It allows them to say nothing while making everyone else feel foolish for not understanding."

    scene i96
    with medium_dissolve

    syl "Near the end of the evening, she offered me a small silver cup."
    syl "The drink inside tasted of cinnamon, winter air, and something bitter hiding beneath the sweetness."
    syl "She raised her own cup and told me it was a toast to new beginnings, to old spirits, and to the future of her people."
    syl "I drank. Naturally."
    syl "I mean, if a beautiful queen offers you enchanted wine on a secret island, you drink it. There are moments when caution becomes terribly inconvenient."

    scene i97
    with medium_dissolve

    syl "But then, the next morning I woke in my own bed, back in our world."
    syl "No ship. No island. No sword-wielding women. For a while, I wondered if the entire thing had been some elaborate dream brought on by bad whiskey and worse judgment."
    syl "Then the headaches began."
    syl "At first, they were small. A sharp pain behind the eyes. A strange ringing in my ears. Moments where the room seemed to stretch farther away than it should."
    syl "Then I started dreaming of this place.....stone walls, iron chains, endless tunnels. Every night, the same dungeon. Every night, the same locked door."

    scene i98
    with medium_dissolve

    syl "You know, this reminds me of a book."
    syl "An island. A ruler who controls everyone around them. Spirits forced to serve. A guest who believes he's free, only to discover the entire performance was arranged long before he arrived."
    syl "Wonderful book. British, of course. The English have always understood that hospitality and imprisonment are separated by little more than who holds the key."

    label dadchoice1:

    menu:
        mc ""

        "Was it... The Odyssey?" if not choicemyy1:

            syl "Homer. Excellent storms, excellent monsters, far too much sailing."
            syl "No. Odysseus knew he was lost. I, unfortunately, believed I knew exactly where I was going."
            $ choicemyy1 = True
            $ chat_hovered = False
            jump dadchoice1

        "Sounds like The Count of Monte Cristo." if not choicemyy4:

            syl "A magnificent choice. Betrayal, imprisonment, revenge, buried wealth. Practically a business manual."
            syl "But no. Dantès escaped his prison with patience and a dead man's burial sack. My circumstances were considerably stranger."
            $ choicemyy4 = True
            $ chat_hovered = False
            jump dadchoice1

        "Maybe Heart of Darkness?" if not choicemyy3:

            syl "Conrad? No. This wasn't a journey into savagery."
            syl "The women on that island were frighteningly civilised. Civilisation, when properly organised, can be far more dangerous than madness."
            $ choicemyy3 = True
            $ chat_hovered = False
            jump dadchoice1

        "The Tempest?" if not choicemyy2:

            pass

    scene i99
    with medium_dissolve

    syl "The Tempest! That's it!"
    syl "A remote island ruled by someone who controls the board while everyone else mistakes themselves for players."
    syl "Prospero had spirits, storms, and an inconvenient obsession with arranging other people's futures."
    syl "My queen had warriors, an ancient secret, and a complete inability to accept that fate might choose someone without first requesting her permission."
    syl "Different wardrobe. Same arrogance."

    scene i100
    with medium_dissolve

    syl "But alas, the headaches grew worse."
    syl "I started losing time. Ten minutes here, an hour there. I'd be sitting at my desk, then suddenly find myself standing somewhere else with no memory of walking there."
    syl "And every time I slept, I returned to this dungeon."
    syl "Eventually, the dream became more real than the waking world. I could feel the cold stone. Smell the rust. Hear water dripping somewhere in the dark."
    syl "Then, one evening, I closed my eyes in our world... and never opened them again."

    scene i103
    with medium_dissolve

    syl "You know, the doctors called it a coma, isn't that something?"
    syl "A simple word for a remarkably complicated prison."
    syl "My body remained there breathing, aging, being poked by well-meaning people in white coats while my mind was dragged here and locked behind these walls."
    syl "The queen couldn't kill me. That much I understood. Whatever she believed was inside me was too valuable to destroy."
    syl "So she did what frightened rulers have always done with things they cannot control."
    syl "She buried me where no one would think to look."

    scene i104
    with medium_dissolve

    syl "But curses are rather like contracts. The person paying for them always wants certainty, while the person writing them prefers loopholes."
    syl "The old wizard who built this prison disliked the queen almost as much as she disliked men."
    syl "So he left a weakness in the spell. A path that could only open for someone bound to me by blood... someone carrying what the queen had actually been searching for."
    syl "She thought that condition was impossible. Then you arrived."
    syl "So, there you have it. A hidden island, a suspicious queen, a poisoned toast, and three years spent living inside an exceptionally unpleasant metaphor."
    syl "God, I missed storytelling."
    syl "Any questions?"

    scene i102
    with medium_dissolve

    voice my_audio["223"]
    nar "Ok....... So, if we've understood this story correctly. Your father, somehow, crossed into another reality, where he then crossed a murderous sea, discovered a secret island full of warrior women, and accepted a silver cup from their suspiciously beautiful queen. Naturally."
    voice my_audio["224"]
    nar "The silver cup had wine in it. Then (like the horny alcoholic he is), he drank the wine. Unbeknownst to him however, the wine was cursed. Because apparently the bitter taste, alternate reality, and surrounding army of armed women weren't sufficiently concerning."
    voice my_audio["225"]
    nar "Then, after drinking it, he woke in his own bed, developed headaches, started losing pieces of his day, and visited this dungeon every night while he slept. Until one night after he fell asleep, his mind finally moved in permanently without the common courtesy of informing his body."
    voice my_audio["226"]
    nar "The doctors called it a coma. The queen presumably called it 'problem solved.' Fortunately, the old wizard who designed the curse for the queen was a deeply petty professional and slipped an escape clause into it purely because he despised her hatred of men."
    voice my_audio["227"]
    nar "Said escape clause requires a blood relative carrying the same mysterious (something). Which brings us to you. Naked, confused, and apparently serving as the magical equivalent of a spare key. Yes, we have questions. Several of them are simply 'What the fuck?'."

    menu:
        "So basically, you found some magical place full of only women, then met their queen, got drunk there, came back home and started having nightmares for years, then eventually after some time passed you fell into a coma....which was actually a mental prison?":


            scene i105
            with medium_dissolve

            syl "When you say it like that, I sound like the village idiot who wandered into a fairy tale with a bottle in his hand."
            syl "But... yes. That's more or less the shape of it. I found a place nobody was ever supposed to find, met a queen nobody was ever supposed to meet, and trusted someone who had already decided exactly how our story would end."

            scene i106
            with medium_dissolve

            syl "The coma wasn't the punishment, my boy. That was merely the symptom."
            syl "This place... *this* is the prison. Every nightmare, every strange dream, every moment where I felt like something was pulling at the back of my mind... it was all leading here."
            syl "By the time I realized I'd been cursed, there wasn't a damned thing I could do to stop it."

            scene i107
            with medium_dissolve

            syl "Life has a curious habit of punishing confidence. You spend decades believing you're the cleverest man in every room... then one gracious smile and a silver goblet remind you that arrogance is a remarkably expensive luxury."
            syl "Still... if I'd been given the chance to do it all again..."
            syl "I'd probably still have taken the damned drink."
            pass
        "This doesn't make any sense. How and when did you leave the note in the hospital?":



            scene i105
            with medium_dissolve

            syl "Ah... the note. Now *that* is the interesting part."
            syl "You see, this prison was never perfect. Every now and then, tiny cracks would appear between this world and ours. Not long enough for me to escape... but just long enough for a whisper to slip through."

            scene i106
            with medium_dissolve

            syl "I could hear voices around my hospital bed from time to time. Doctors. Nurses. Machines. Occasionally... yours."
            syl "Moving so much as a finger felt like trying to lift a mountain, but eventually I managed it. Just enough to leave you a name... an address... and the faint hope that you'd follow it."
            syl "I couldn't explain everything. There wasn't time, and even if there had been... I wasn't entirely sure anyone would've believed me."

            scene i107
            with medium_dissolve

            syl "Fortunately, curiosity appears to be one trait you inherited from me."
            syl "You followed the trail instead of dismissing it as the ramblings of a man wasting away in a hospital bed."
            syl "And because of that... somewhere, someone who believed this prison would hold forever is about to have a very unpleasant surprise."
            pass


    scene i108
    with medium_dissolve

    syl ".........."
    syl ".............."
    syl "...................."

    scene i109
    with medium_dissolve

    syl ".........."
    syl ".............."
    syl "Uh....son, I have a question..."

    scene i110
    with medium_dissolve

    syl "What exactly were you doing before you appeared in this infernal prison?"
    syl "I'd imagine what you just did was the very thing that was needed to lift the curse."

    voice my_audio["416"]
    nar "Right. What exactly were we doing before being dragged naked into a magical prison? Let us carefully retrace this exceptionally respectable chain of events."
    voice my_audio["417"]
    nar "You invited Marnie upstairs, brought her into your room, and rather bluntly announced that you wanted to have sex with her. She responded by shouting that she was absolutely not going to fuck you."
    voice my_audio["418"]
    nar "The argument became heated. Marnie struck you repeatedly, and when she attempted to hit you again, you caught her arm and pulled her close before she could finish the swing."
    voice my_audio["419"]
    nar "Then, against every reasonable expectation, she willingly kissed you back. The shouting became making out, the anger became mutual desire, and the confrontation rapidly turned into some truly insane sex."
    voice my_audio["420"]
    nar "And not merely a brief encounter, either. You came inside that cum dumpster whore of a wife, three separate times. Three. Apparently magical curses keep extraordinarily detailed records of adultery."
    voice my_audio["421"]
    nar "Then, without warning, you vanished. One moment you were inside some stupid bitch; the next, you were naked inside this cold dungeon with your supposedly comatose father."
    voice my_audio["422"]
    nar "Whether that cum toilet Marnie actually watched you disappear, we have absolutely no idea. For all we know, something equally impossible may have happened to her the moment you vanished."
    voice my_audio["423"]
    nar "If we escape, that will make for a fascinating conversation. Still, if your father is correct, it appears three spectacularly huge cum blasts inside Marnie somehow counted as the official curse-breaking ritual."

    menu:
        "Oh uh, well I was sorta....banging Marnie. Even uh, came inside her....a few times. Three times, to be exact.":




            pass
        "I was.....fucking Marnie. Came inside her three times too.":

            pass
        "Well, I was fucking the shit out of Marnie. Came in her three times, too.":

            pass

    play sound my_audio["bang sound 1"] noloop
    scene i111
    with hpunch

    syl "You.....you what...?"
    syl "..........."
    syl ".................."

    play sound my_audio["bang sound 2"] noloop
    scene i112
    with hpunch
    play music my_audio["evilsneaky3"] loop

    syl "AHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHA!"

    scene i113
    with medium_dissolve

    syl "AHAHAHAHAHAHA!!! I SEE!! IT ALL MAKES SENSE NOW!!! HAHAHAHAHAHAHAHAHAHAHAHAA!!!!!"

    scene i114
    with medium_dissolve

    syl "Marnie...because she's a....of course...OF COURSE!!"
    syl "That old bastard wizard really thought of the most impossible situation! Hah!"
    syl "This explains everything! The dinner! The curse! The wizard! The fine wine!"

    scene i115
    with medium_dissolve

    syl "You know... I always knew there was something extraordinary about that island."
    syl "Not because of the palaces or the warriors. It was the way they looked at certain people... as though they were waiting for history itself to arrive."
    syl "And like the spectacular fool I was, I mistook ancient purpose for simple hospitality."

    scene i116
    with medium_dissolve

    syl "Now it finally fits."
    syl "The queen wasn't interested in me because of who I was. She was interested because of what I was carrying."
    syl "The curse was never designed to keep *me* imprisoned forever... it was designed to delay the inevitable."
    syl "That old wizard... clever bastard. He hid the key inside a condition so absurd that nobody believed it could ever happen."

    scene i117
    with medium_dissolve

    syl "And yet... somehow... against every law of probability..."
    syl "You stumbled into the one circumstance capable of fulfilling it."
    syl "Not because you understood the curse... not because you knew the prophecy... simply because you're young and horny!"

    scene i118
    with medium_dissolve

    syl "Do you understand what this means!?"
    syl "The curse wasn't broken by strength, or magic, or some glorious battle!"
    syl "It was broken because the final condition was fulfilled... the very condition the queen believed could never come to pass!"
    syl "She built the perfect prison... and the wizard quietly built the perfect escape!"
    syl "It's all just FUCKING MADNESS!"

    menu:
        "Hey, calm down. You're starting to lose it.":




            pass
        "Okay, well... that's a lot to take in.":

            pass
        "It's not that deep, man.":

            pass
        "I mean, yeah, she's hott. I just went with the moment...":

            pass


    scene i119
    with medium_dissolve
    pause

    scene i120
    with medium_dissolve
    pause

    scene i121
    with medium_dissolve

    syl "You know what, kid...."
    syl "I’m proud of you."
    syl "Not because you broke some curse, or because you're a horny kid, or because you pulled me out of the literal bowels of magical imprisonment... though, granted, those are all impressive."

    scene i122
    with medium_dissolve

    syl "I'm proud because you're still standing. Because after everything, you still came here, intentionally or not, and faced this madness head-on."
    syl "Five years ago, you were just a highschooler with a slingshot and a bad haircut."
    syl "Now you're a man with fire in his blood and chaos in his wake. Like father, like son."

    scene i123
    with medium_dissolve

    syl "I never wanted this life for you. But Gods help me, I’m glad you found your way here."
    syl "You remind me of who I used to be, before the chains, before the tricks, before the ancient grudges."
    syl "Maybe we should stay down here forever. Bit of father-son bonding, rotten food, whispered nightmares, what do you say?"

    play sound my_audio["bang sound 1"] noloop
    scene i124
    with hpunch

    syl "HAH! Just kidding!"
    syl "Come on, let's get the HELL out of here before the torchlight starts whispering again."

    scene i125
    with medium_dissolve

    syl "Ah, I always knew this day would come... well, not like this. I figured you’d show up in a leather jacket with a crossbow, not stark naked and confused, shit."
    syl "Still. I’ll take what I can get."
    syl "And you....look at you. Didn’t even cry once. Your mother would've loved that."

    scene i126
    with medium_dissolve

    menu:
        "Wait, isn't that door locked?":




            pass
        "So… what’s the plan? Sit here and look smug until the door magically opens?":

            pass
        "Not to kill the mood, but we’re still trapped.":

            pass


    play sound2 my_audio["dooropen"] noloop
    scene i127
    with medium_dissolve
    pause

    scene i128
    with medium_dissolve

    syl "Well, what do you know... looks like the universe finally RSVP’d to our little reunion!"
    syl "Come along, son. It’s rude to keep an open door waiting."

    scene i129
    with medium_dissolve

    syl "Let's see now, what time is it...?"
    syl "Hmm. According to this, it’s sometime between 'eternal despair' and 'half-past screwed.'"
    syl "Note to self...magical prisons are hell on quartz movement."

    scene i130
    with medium_dissolve

    syl "Tell me, by any cosmic miracle would you happen to have a toothpick, a pair of socks, or perhaps a flask of aged whiskey tucked away in your...birthday suit?"
    syl "No? Of course not. You’re as bare as truth in a confession booth. What am I saying?"
    syl "And by the way, do me a favor. Don't tell Marnie about any of this, alright?"

    scene i131
    with medium_dissolve

    unk "It... it can't be! Doctor! Come quick! Mr. [playerLastName] is waking up!"
    unk "Doctor!!!"

    scene i132
    with medium_dissolve

    syl "Well! Would you listen to that!?"
    syl "Sounds like the orchestra just struck up the overture to our grand return!"
    syl "Guess that’s our cue, kid! Time to take this little father-son act back to the real world!"

    scene i133
    with medium_dissolve

    syl "Funny, isn’t it? One minute you’re chained in magical purgatory, the next you’re getting summoned by a panicked intern and the smell of antiseptic."
    syl "I suppose this means my coma’s clock just ran out."
    syl "Let’s not keep destiny waiting, shall we!? ONWARD!"

    scene i134
    with medium_dissolve

    menu:
        "Wait! Hang on!":



            pass
        "Hold up! I need a second!":

            pass
        "Whoa, we’re just going through the door!?":

            pass
        "Hey! Don’t leave me behind!":

            pass


    jump marnie2nd
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

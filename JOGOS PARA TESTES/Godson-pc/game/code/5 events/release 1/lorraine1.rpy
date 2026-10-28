label lor1:

    stop music fadeout 2.0
    stop sound fadeout 2.0

    scene black
    with slowfade

    play music my_audio["apartment4"] loop fadein 3.0

    pause 2.0

    scene g1
    with slowfade

    voice my_audio["528"]
    nar "At last, you are alone. No arguments, no suspicious husbands, and no beautiful woman presenting you with yet another opportunity to complicate your life."

    if freedfather:
        voice my_audio["529"]
        nar "You came here because of your father's note. Since then, you forced your way into Henry's home, seduced Marnie beneath her husband's roof, and slept with her loudly enough to make discretion file for divorce."
        voice my_audio["530"]
        nar "Then you vanished into a freezing dungeon and found your supposedly comatose father waiting inside. His coma was a magical prison, and somehow your night with Marnie broke the curse holding him there."
        voice my_audio["531"]
        nar "You freed him, returned to this house, and carried on with the day as though adultery leading to supernatural prison reform were merely an unusual start to the morning."
    elif sexwithmarnie or fooledaroundwithmarnie:
        voice my_audio["532"]
        nar "You came here searching for the meaning behind your father's note. Instead, you became entangled with Marnie, crossed a line with Henry's wife, and woke today no closer to understanding why your father sent you."
        voice my_audio["533"]
        nar "Whatever happened between you and Marnie was real enough to leave consequences behind, yet it explained absolutely nothing about the secret hanging over this family."
    elif triedtogetmarnieupstairs:
        voice my_audio["534"]
        nar "You came here searching for answers, then spent part of your first night trying to persuade Marnie to join you upstairs. You pushed too hard, she refused, and the mystery survived your little campaign entirely untouched."
        voice my_audio["535"]
        nar "A failed seduction should have simplified matters. Somehow, it merely gave you one more strained relationship to place beside the unanswered questions concerning your father."
    elif evil:
        voice my_audio["536"]
        nar "You began this visit by forcing your way past Henry, ignoring nearly every boundary placed in front of you, and treating the people in this house as though their patience were an unlimited resource."
        voice my_audio["537"]
        nar "For all that confidence, however, you remain the least informed person here. Every reckless choice has changed how these people see you without revealing why your father sent you among them."
    else:
        voice my_audio["538"]
        nar "You followed your father's note to this house and, despite every strange temptation placed in your path, tried to treat Henry, Marnie, and their family with decency."
        voice my_audio["539"]
        nar "You have earned a little trust and avoided several obvious disasters. Unfortunately, good manners have brought you no closer to learning why your father sent you here."

    if metjennifer and deniedjennifer:
        voice my_audio["540"]
        nar "There was also Jennifer: the beautiful woman who drew you into her room, slapped you for asking a reasonable question, and demanded that you call her Mommy. You refused and left, although the encounter remains filed under things a sensible man should never need to process twice."

    scene g2
    with medium_dissolve

    if metlorrainebad:
        voice my_audio["541"]
        nar "This morning brought Lorraine. You entered while she searched the bathroom, but your restraint afterward kept a disastrous first meeting from becoming completely unsalvageable. Even so, she spoke and looked at you as though something important sat just beyond the words."
    elif metlorrainegood:
        voice my_audio["542"]
        nar "This morning brought Lorraine. You invaded her privacy, ignored her anger, and ensured that her first clear memory of you would involve a locked bathroom door and an urgent desire to be anywhere else."
    else:
        voice my_audio["543"]
        nar "Even the people you have barely spoken to seem to carry pieces of a story nobody intends to explain. In this house, a glance can feel like half a confession."

    if yuni_video_completed:
        voice my_audio["544"]
        nar "Then you helped Yuni film Martha and successfully turned a very strange family favour into a finished production. Yuni now knows you can be useful, while you know this family's definition of an ordinary afternoon is deeply untrustworthy."
    elif yuni_video_failed:
        voice my_audio["545"]
        nar "Then you agreed to help Yuni film Martha, failed her little music test, and were dismissed before the production properly began. Apparently, one poor song choice is enough to become professionally useless in your own guest room."
    elif yuni_video_refused:
        voice my_audio["546"]
        nar "Then you refused Yuni's request to help film Martha and walked away. It may have disappointed her, but it also spared you from adding amateur camera operator to today's growing list of questionable responsibilities."
    else:
        voice my_audio["547"]
        nar "Yuni and Martha supplied their own share of oddness, reinforcing the impression that everyone in this family is connected to something you still cannot see."

    scene g3
    with medium_dissolve

    if marnie_interview_watched:
        voice my_audio["548"]
        nar "Henry asked you to check on Marnie's interview. You stayed behind the door and watched his boss turn it into something no Human Resources department would dare describe in writing."
        if marnie_aftermath_gave_in:
            voice my_audio["549"]
            nar "When the damage surfaced, you abandoned explanations and gave in to Marnie yourself. Henry's trust, Marnie's marriage, and the original purpose of the interview all became secondary to another impulse."
        else:
            voice my_audio["550"]
            nar "When the damage surfaced, you admitted that remaining there had been a choice. Marnie asked for silence and space, leaving you with the unpleasant knowledge that observation can become its own kind of betrayal."
    elif marnie_interview_stopped:
        if marnie_boss_attacked:
            voice my_audio["551"]
            nar "Henry asked you to check on Marnie's interview. You responded by barging into the room, confronting his boss, and physically dragging the situation to an end."
        else:
            voice my_audio["552"]
            nar "Henry asked you to check on Marnie's interview. You barged into the room and stopped his boss from taking the situation any further, even as the man's threats placed Henry's job directly in the line of fire."

        if marnie_aftermath_gave_in:
            voice my_audio["553"]
            nar "Then, after protecting Marnie from one man's intentions, you gave in to your own. Heroism has rarely surrendered the moral high ground with such impressive speed."
        elif good:
            voice my_audio["554"]
            nar "Your intentions were decent, even if the result left Henry furious and Marnie scrambling to hold her marriage together. Doing the right thing has produced a remarkably ugly collection of consequences."
        else:
            voice my_audio["555"]
            nar "You explained yourself rather than making the wreckage worse. A measured response, particularly from someone whose earlier decisions have not always shown much affection for restraint."
    else:
        voice my_audio["556"]
        nar "Henry's request ended badly enough to leave the house strained and quiet, adding another set of consequences to a mystery that still refuses to explain itself."

    if evil:
        if memory_nina_is_boyfriend:
            voice my_audio["557"]
            nar "And then there was Nina. You manipulated a married woman more than twice your age into your room, gave her the most overwhelming sex of her life, heard her confess love, and told her you loved her too. You arrived seeking answers and somehow acquired a girlfriend instead."
        elif memory_nina_wait_response:
            voice my_audio["558"]
            nar "And then there was Nina. You manipulated her upstairs, fucked sense and caution out of the afternoon, and received a declaration of love in return. You asked for time, leaving a married woman more than twice your age waiting to learn what she now means to you."
        elif memory_nina_hates_you:
            voice my_audio["559"]
            nar "And then there was Nina. You manipulated her upstairs, fucked her senseless, and confirmed her worst suspicion by admitting that sex was all you ever wanted. She ran from the room with a final 'Fuck you,' now convinced that every vulnerable word had merely been part of your plan."
        elif memory_nina_crossed_line:
            voice my_audio["560"]
            nar "And then there was Nina. You tried to turn her fear and your unanswered questions into enough guilt to keep her here, but pushed too far. She walked away knowing you had nearly earned what you wanted before entitlement ruined it."
        elif nina_left_for_appointment:
            voice my_audio["561"]
            nar "And then there was Nina. She looked at you as though your existence should have been impossible, promised answers when she returned, and left for her appointment. For once, you allowed a woman to walk away without turning desire into a crisis."
        elif nina_guilt_success:
            voice my_audio["562"]
            nar "And then there was Nina. You somehow persuaded her to cancel her appointment, follow you upstairs, and cross a line neither of you can pretend was accidental. Whatever followed, the woman who recognised you now knows you far more intimately than before."
        else:
            voice my_audio["563"]
            nar "And then there was Nina, staring at you as though the dead had walked through the front door. She clearly knew something, yet the encounter ended without giving you the explanation she promised."

    if freedfather:
        voice my_audio["564"]
        nar "Even after finding your father and learning how his curse was broken, the larger picture remains hidden. The island, the enchanted wine, this family, and the impossible way people recognise you still refuse to form a complete answer."
    else:
        voice my_audio["565"]
        nar "Your father's note remains at the centre of it all. It brought you to a family filled with careful smiles, sudden silences, and people who seem to recognise something in you that you cannot recognise in yourself."

    voice my_audio["566"]
    nar "Different choices, different consequences, yet every path returns to the same question: what exactly did your father send you into?"
    voice my_audio["567"]
    nar "You stare at the wall and force your tired mind to arrange every look, warning, confession, and impossible coincidence into something that makes sense."
    voice my_audio["568"]
    nar "Then something inside your head pushes back."

    stop music
    play sound my_audio["bang sound 1"] noloop

    scene g5
    with hpunch

    play music my_audio["wizard1"] loop fadein 1.0

    voice my_audio["569"]
    nar "Pain explodes behind your eyes."
    voice my_audio["570"]
    nar "Your breath catches. Your balance disappears, and for one sickening moment, you can no longer tell which thoughts belong to you."
    voice my_audio["571"]
    nar "Voices tear through your mind all at once. Frightened, irritated, distracted. Too many people speaking without making a sound."

    scene g6
    with medium_dissolve

    voice my_audio["572"]
    nar "You try to shut them out. It has exactly the opposite effect. The harder you resist, the clearer they become."
    voice my_audio["573"]
    nar "A passing worry. A buried resentment. Someone downstairs wondering whether they remembered to lock a door."
    voice my_audio["574"]
    nar "These are not voices coming through the walls. They are thoughts, and none of them belong to you."

    scene g7
    with medium_dissolve

    voice my_audio["575"]
    nar "You clutch your head as another wave passes through you."
    voice my_audio["576"]
    nar "This time, beneath the pain, you feel a pattern. The voices are no longer one deafening mass. You can sense the distance between them, where one mind ends and another begins."
    voice my_audio["577"]
    nar "With effort, you reach for a single voice. The instant you hold it, the others recede into a distant murmur."

    scene g8
    with medium_dissolve

    voice my_audio["578"]
    nar "The pressure finally eases."
    voice my_audio["579"]
    nar "You bend forward, dragging air back into your lungs while the room slowly steadies around you."
    voice my_audio["580"]
    nar "The pain is fading. What caused it, however, remains."

    scene g9
    with medium_dissolve

    voice my_audio["581"]
    nar "Somewhere downstairs, someone decides to leave. You hear the decision form a heartbeat before a distant door opens and closes."
    voice my_audio["582"]
    nar "There can be no mistaking it now. Somehow, you can hear the thoughts of the people around you."
    voice my_audio["583"]
    nar "Not every thought. Not yet, and not without effort. But the door is open, and somehow you already know how to reach through it."
    voice my_audio["584"]
    nar "It is an answer, but not to any question you were asking."
    voice my_audio["585"]
    nar "For now, one far more troubling question takes its place: what are you going to do with this?"
    jump lor3

label lor3:

    play sound my_audio["knockm"] noloop
    pause 2.5

    scene g10
    with medium_dissolve

    lor "Hello? You in there?"
    lor "It's Lorraine. I wanted to ask you something."
    lor "Can I come in for a minute?"

    scene g11
    with medium_dissolve

    menu:
        "Can this wait? I got something going on here.":




            lor "It'll just take a few minutes, I promise."
            lor "I've got an idea for something we could do together. Nothing complicated. I just thought it might help both of us unwind."
            lor "And I'd prefer to explain it to your face instead of standing out here talking to a door."
            lor "..."
            lor "Are you seriously not going to answer me?"
            lor "Oh, come on. I'm coming in."
        "What do you want?":


            lor "Okay, straight to the point. I can work with that."
            lor "I wanted to see if you'd be interested in doing something with me. It's great for clearing your head, and after everything that's happened, I think we could both use it."
            lor "It'll make more sense once I show you."
            lor "..."
            lor "Are you really gonna make me have this entire conversation from the hallway?"
            lor "Okay. I'm coming in."
        "Yeah... just... give me a sec.":


            lor "Sure. Take your time."
            lor "I just wanted to suggest something we could do together. A little exercise, a chance to clear our heads, nothing too intense."
            lor "I think you might actually enjoy it."
            lor "..."
            lor "Wait. Is a second longer where you're from?"
            lor "All right, ready or not, I'm coming in."
        "You're not upset about the... loud noise you heard from this room?":


            lor "The noise? Henry already told me what happened."
            lor "He said Nina got sick, knocked over some furniture, and you stayed with her until she calmed down."
            lor "It sounded pretty alarming from downstairs, but if Nina's okay, I don't see any reason to make a big deal out of it."
            lor "Anyway, that's not why I'm here."
            lor "So, are you going to open the door, or are we gonna keep yelling through it?"
            lor "Actually, forget it. I'm coming in."

    stop music fadeout 3.0

    scene black
    with slowfade

    pause 2.0

    play music my_audio["think2"] loop fadein 3.0

    scene g12
    with medium_dissolve

    lor "There you are. Hey again, [playerName]."

    if metlorrainebad:

        menu:
            "Honestly, I thought you'd still be mad at me for barging in on you in the bathroom earlier.":


                lor "I was mad. You walked into a locked bathroom while I was changing, so I had every right to be."
                lor "But you left when I told you to, and I'm not interested in dragging one awful first impression through the rest of the day."
                lor "Consider this a chance for us to start over. Just don't make me regret giving it to you."

    lor "Okay, this might sound a little random, but I was thinking we could do some yoga together."
    lor "I do it whenever I need to stretch, clear my head, or keep myself from losing it after a particularly rough day."
    lor "It's good for you, it doesn't take much space, and it's a lot less boring when somebody does it with you."

    scene g14
    with medium_dissolve

    lor "Don't worry, I'm not about to lecture you about finding your inner peace."
    lor "It helps with your posture, your breathing, and all those muscles you don't realize are tight until you finally move them."
    lor "You've got enough room in here, and I already know a simple routine we can start with."
    lor "So, what do you think? Wanna give it a shot?"

    scene g15
    with medium_dissolve

    $ pe = "{image=evil} Hell yeah! I've always wanted to do some naked yoga!"

    menu:
        "Yoga, huh? I'm down. I've done it before.":




            scene g16
            with medium_dissolve

            lor "Oh, great. That makes this easier."
            lor "I won't have to walk you through every little move, and we can try something more interesting than the beginner stuff."
            lor "We're still warming up first, though. I'm not taking the blame if you pull something trying to show off."
        "Sure, but I've never done it before, so I might be trash at it.":


            scene g16
            with medium_dissolve

            lor "You'll be fine. Everybody's bad the first time."
            lor "I'll walk you through it, and if something hurts, you stop. There's no prize for throwing your back out."
            lor "Just follow my lead and try not to fall on top of me."

        "[pe]" if evil:

            scene g16
            with medium_dissolve

            lor "Oh, knock it off. You know damn well that isn't what I meant."
            lor "And yes, before you ask, naked yoga is a real thing. No, that is not what we're doing today."
            lor "We're keeping our clothes on and focusing on the stretching."
            lor "Try to hide your disappointment."
        "Shouldn't we be getting ready for Jennifer's party tonight?":


            scene g16
            with medium_dissolve

            lor "We've got plenty of time. Jennifer's party isn't starting right now."
            lor "Besides, moving around a little will wake us up and put us in a better mood before we spend the whole evening surrounded by people."
            lor "I'm taking that as a yes. Come on, let's get started."

    scene g17
    with medium_dissolve

    lor "We'll start with a few easy stretches. Nothing crazy."
    lor "A short Sun Salutation should warm everything up without wearing us out before the party."
    lor "Take it slow, pay attention to your breathing, and don't force anything that hurts."
    lor "Once you're warmed up, we can try a few poses that require a little more balance."

    scene g18
    with medium_dissolve

    lor "After that, we'll do something for your back and shoulders. Cobra and Cat-Cow should loosen everything up."
    lor "We'll throw in a couple of balance poses too, maybe Tree, or Warrior if you're feeling confident."
    lor "And before you make another joke, no, none of those involve taking your clothes off."
    lor "Anything bothering you physically? Bad back, tight legs, bad knee? Tell me now so I don't accidentally make it worse."
    mc "........."

    scene g19
    with medium_dissolve

    voice my_audio["586"]
    nar "As Lorraine talks you through the routine, you have to admit that yoga doesn't sound half bad. A chance to stretch, clear your head, and forget about this house for a while might be exactly what you need."
    voice my_audio["587"]
    nar "But the questions are still there, sitting quietly beneath your interest."
    voice my_audio["588"]
    nar "Lorraine acts as though she knows you. So does nearly everyone else here. Yet whenever you get close to finding out why, the conversation changes."
    voice my_audio["589"]
    nar "Part of you is ready to enjoy the session. The rest is tired of being the only person in the house who doesn't know what is really going on."
    jump part8

label part8:

    scene g19_1
    with medium_dissolve

    voice my_audio["590"]
    nar "Then you remember the new ability waiting at the back of your mind. You don't have to keep guessing what everyone is hiding. You can simply listen."
    voice my_audio["591"]
    nar "Lorraine is right in front of you. One look inside her thoughts might tell you why she knows you, what she is keeping from you, and what your connection to this house really is."
    voice my_audio["592"]
    nar "Of course, those thoughts belong to her. She hasn't given you permission to hear them, and she may never trust you again if she finds out."
    voice my_audio["593"]
    nar "The answer could be only a thought away. Now you must decide whether getting it is worth crossing that line."
    stop music fadeout 3.0
    voice my_audio["594-1"]
    nar "Only you can make that decision."
    jump part6

label part6:



    $ godson_text = "{image=evil} *Look into Lorraine's mind for the truth.*"

    scene g20
    with medium_dissolve

    menu:
        "Sounds good. Let's do some yoga.":

            jump lorraine_respects_privacy
        "I'm down for a little yoga. Let's do it.":

            jump lorraine_respects_privacy

        "[godson_text]" if evil:

            if sexwithmarnie or fooledaroundwithmarnie:
                voice my_audio["594-12"]
                nar "There it is. You crossed a rather significant line with Marnie, and now Lorraine's private thoughts are merely the next locked door standing between you and what you want. Go on, then."
            elif marnie_interview_watched:
                voice my_audio["594-13"]
                nar "Of course. After hiding outside a bedroom to watch Marnie's private interview, stepping uninvited into Lorraine's mind is less a change of direction and more a natural escalation."
            elif memory_nina_crossed_line or nina_guilt_success or memory_nina_is_boyfriend or memory_nina_wait_response or memory_nina_hates_you:
                voice my_audio["594-14"]
                nar "After pressing Nina until her resistance gave way, respecting Lorraine's boundaries now would have been a surprising change of character. Take the answer you came here for."
            else:
                voice my_audio["594-15"]
                nar "So much for restraint. Lorraine offered you trust, and you have decided to repay her by walking straight into the one place she cannot lock. Very well. Find the truth."

            $ earlytruth = True
            $ memory_lorraine_secret_uncovered = True
            $ show_tooltip(n=16)
            play sound2 my_audio["bell"] noloop

            play sound my_audio["mindread"] noloop fadeout 2.0

            scene g20_1
            with slow_dissolve

            play music my_audio["icecave"] loop fadein 1.0

            voice my_audio["595"]
            nar "You reach into Lorraine's mind."
            voice my_audio["596"]
            nar "At first, you find only the room around you: her plans for the yoga session, concern over your strange behavior, and the quiet hope that getting you moving might help."
            voice my_audio["597"]
            nar "Useful, perhaps. But hardly the truth everyone has worked so hard to keep from you. You push deeper."
            voice my_audio["598"]
            nar "The bedroom drops away."
            voice my_audio["599"]
            nar "Heat settles across your skin. Sunlight pours from a cloudless sky, bright enough to make you squint."
            voice my_audio["600"]
            nar "An island rises around you, surrounded by water so blue it scarcely looks real."
            voice my_audio["601"]
            nar "White stone homes climb the green hills. Flowering vines spill across their walls, and broad paths wind between courtyards open to the sea."
            voice my_audio["602"]
            nar "Long tables sag beneath fresh bread, roasted meat, bowls of fruit, and enough wine to make restraint seem like a local superstition."
            voice my_audio["603"]
            nar "Laughter carries through the warm air. For one brief moment, the place feels almost peaceful."
            voice my_audio["604"]
            nar "Then you notice there are women everywhere... and only women."
            voice my_audio["605"]
            nar "Some share food beneath the trees. Others shape metal, tend gardens, study maps, or move through the streets with the easy confidence of people who have never had to ask whether they belong."
            voice my_audio["606"]
            nar "Beyond them, entire groups train with swords, shields, bows, and spears. Every strike is controlled. Every formation moves as one."
            voice my_audio["607"]
            nar "This is no performance for visitors. Whatever this place is, its women have been raised to fight."
            voice my_audio["608"]
            nar "You spot Lorraine among them, younger but unmistakable, wearing fitted armor with a shield resting against her leg."
            voice my_audio["609"]
            nar "She isn't visiting. She isn't dreaming. This was home."
            voice my_audio["610"]
            nar "The memory shifts before you can study her any longer."
            voice my_audio["611"]
            nar "Now Lorraine stands inside a vast circular hall, surrounded by rows of armed women."
            voice my_audio["612"]
            nar "At the far end, a woman watches from a raised stone seat. You do not know her name, but you know what she is the moment every head in the chamber lowers."
            voice my_audio["613"]
            nar "A queen. She needs no crown and offers no smile. Authority follows her every glance."
            voice my_audio["614"]
            nar "Women approach her one by one, kneeling to deliver reports before being sent away with quiet orders."
            voice my_audio["615"]
            nar "Lorraine eventually takes her place before the throne. She kneels, speaks, and waits."
            voice my_audio["616"]
            nar "You strain to hear the exchange, but the words smear together whenever they draw close to anything useful."
            voice my_audio["617"]
            nar "The queen finally gives a small nod. Lorraine rises with something hidden in her hand and a purpose you can feel, but cannot name."
            voice my_audio["618"]
            nar "Whatever passed between them mattered. Lorraine carried its weight long after she left the chamber."
            voice my_audio["619"]
            nar "The memory shifts again."
            voice my_audio["620"]
            nar "A stone arch stands near the island's shore, its center filled not with open air, but with pale light moving like water."
            voice my_audio["621"]
            nar "Lorraine walks into it without hesitation."
            voice my_audio["622"]
            nar "One step later, she emerges beneath electric lights, surrounded by paved streets, passing cars, and the familiar noise of your world."
            voice my_audio["623"]
            nar "More memories race past. Different clothes. Different years. The same impossible crossing."
            voice my_audio["624"]
            nar "Again and again, Lorraine moves between the island and this world."
            voice my_audio["625"]
            nar "Sometimes she carries sealed letters or unfamiliar objects. Sometimes she returns exhausted. Once, you catch the flash of blood beneath her sleeve before the memory slips away."
            voice my_audio["626"]
            nar "This is not a hidden island reached by boat or plane. It exists somewhere else entirely, with that doorway joining the two worlds."
            voice my_audio["627"]
            nar "You search for the island's name, the queen's identity, anything that might explain what Lorraine was sent here to do."
            voice my_audio["628"]
            nar "For one brief moment, an answer begins to take shape."
            voice my_audio["629"]
            nar "Then something closes around the thought."

            play sound my_audio["bang sound 1"] noloop

            scene g22
            with hpunch

            voice my_audio["630"]
            nar "The memory tears itself apart."
            voice my_audio["631"]
            nar "The island vanishes. The queen's hall fractures into darkness, and the glowing doorway snaps shut."
            voice my_audio["632"]
            nar "You are thrown out of Lorraine's mind with only three certainties left behind: an island of warrior women, a queen they all obey, and a passage connecting their world to yours."

            menu:
                "What the hell was that!?":



                    pass
                "An island full of warrior women?":

                    pass
                "Who was that woman on the throne?":

                    pass
                "How were you moving between that island and this world?":

                    pass

            lor "...What?"
            lor "[playerName], are you all right?"
            lor "You've gone completely pale. Sit down before you fall over."
            lor "Here, let me have a look at you."

            scene black
            with slowfade

            scene g23
            with ffade

            lor "Come here. Let me check your temperature."

            menu:
                "S-Stay back!":




                    lor "Stay back? What's got into you?"
                    lor "You looked perfectly fine a moment ago, and now you're staring at me as if I've pulled a knife."
                    lor "Tell me what just happened."
                "What was that island?":


                    lor "...What island?"
                    lor "I never mentioned an island."
                    lor "Where did you hear that?"
                "Who was that queen?":


                    lor "What did you just say?"
                    lor "I never said anything about a queen."
                    lor "How could you possibly know she exists?"
                "I saw you walk through some kind of doorway into this world.":


                    lor "No. That isn't something you could've guessed."
                    lor "A moment ago, we were talking about yoga. Now you're describing something I've never told you."
                    lor "Tell me exactly what you saw."

            scene g24
            with medium_dissolve

            lor "..."
            lor "You aren't guessing, are you?"
            lor "Something happened just now. I saw it in your face."

            scene g25
            with medium_dissolve

            lor "You saw something."
            lor "Something you were never supposed to see."
            lor "Tell me exactly what it was."

            menu:
                "I saw your home. The island, the women, and the warriors.":




                    lor "..."
                    lor "You couldn't have seen that."
                    lor "Those aren't stories I've shared with anyone outside my family."
                    lor "You need to tell me how you saw it."
                "I saw you kneeling in front of a queen.":


                    lor "Keep your voice down."
                    lor "You don't understand what you saw or how dangerous that information could be."
                    lor "Now tell me how you found it."
                "I watched you cross from that island into this world.":


                    lor "That's impossible."
                    lor "No one in this house has ever described that crossing to you."
                    lor "You need to tell me how you saw it."
                "I saw enough to know you've all been lying to me!":


                    lor "We have kept things from you. That is not the same as lying about everything."
                    lor "There are reasons you haven't been told, even if you don't like them."
                    lor "But first, I need to know how you got inside that memory."

            scene g27
            with medium_dissolve

            menu:
                "I read your mind. Whatever happened to me earlier gave me the ability to hear people's thoughts.":




                    $ readmind = True
                    $ memory_lorraine_honesty = True
                    $ show_tooltip(n=35)


                    lor "You read my mind?"
                    lor "Holy shit... so it really has started."
                    lor "I knew there was something different about you, but I didn't expect your ability to surface this quickly."
                    lor "And for the record, going through someone's memories without permission is a serious violation."
                "Does it matter? I know now, so start explaining.":


                    $ readmind = False

                    lor "Yes, it matters. You pulled something out of my head that I have spent years protecting."
                    lor "You don't get to demand complete honesty while refusing to give me any in return."
                    lor "Still, pretending you saw nothing would be pointless now."
                "None of your business. Tell me what that place was.":


                    $ readmind = False

                    lor "You invade my privacy and then tell me your methods are none of my business?"
                    lor "You have some nerve, I'll give you that."
                    lor "Fine. I'll tell you what I can, but you are not getting everything."

            scene g28
            with medium_dissolve

            lor "The island you saw is real, but it isn't hidden somewhere on any map in this world."
            lor "I wasn't born there. However, I spent most of my early life among those women, and yes, every one of them is trained to protect the island and each other."
            lor "They are governed by the queen you saw. Her word carries more weight there than any law you've ever known here."
            lor "If you tried to find the island's name or the queen's identity inside my mind, you probably noticed that you couldn't. That was deliberate."

            scene g29
            with medium_dissolve

            lor "The doorway is real too. It allows certain people to move between the island and this world."
            lor "I left through it years ago and built a life here, although there have been times when I had to return."
            lor "The queen had her reasons for allowing me to leave, just as she had reasons for calling me back."
            lor "Those reasons are tied to things I am not free to explain to you. Not yet."

            menu:
                "What are you, Lorraine?":




                    scene g30
                    with medium_dissolve

                    lor "I am the same woman who walked into this room a few minutes ago."
                    lor "Being born somewhere impossible doesn't erase the life I've lived here."
                    lor "As for what my people call themselves, you're not ready to hear it, and I'm not allowed to tell you."
                "Does Marnie come from that island too?":


                    scene g30
                    with medium_dissolve

                    lor "That is Marnie's story to tell, not mine."
                    lor "I won't drag her secrets into this simply because you found your way into one of mine."
                    lor "If she wants you to know where she comes from, she will tell you herself."
                "Do Jennifer and Yuni know about this?":


                    scene g30
                    with medium_dissolve

                    lor "Jennifer and Yuni know a great deal, I'm afraid."
                    lor "That doesn't mean they know everything."
                    lor "Leave them out of this until we understand what is happening to you."
                    lor "They may be my family, but something tells me they're up to something."
                "Why do you keep going back there?":


                    scene g30
                    with medium_dissolve

                    lor "Sometimes I was summoned. Sometimes someone needed help. Once or twice, going back was the only way to protect the people I love here."
                    lor "I know that sounds like another carefully incomplete answer. It is."
                    lor "But I won't expose everyone connected to that place simply because you forced open one memory."

            scene g31
            with medium_dissolve

            lor "Listen to me. You have seen pieces of something much larger, but pieces can be more misleading than complete ignorance."
            lor "The island has rules. So does the passage between our worlds."
            lor "Breaking those rules could put people on both sides of that doorway in danger."
            lor "That is why we kept this from you. Not because I wanted to make a fool of you."

            scene g32
            with medium_dissolve

            lor "Your ability is another problem entirely."
            lor "If you can enter someone's memories without meaning to, you need to learn how to control it before you stumble into the wrong mind."
            lor "Some people will feel you searching. Others may have defences far less polite than mine."
            lor "I can try to help you understand what is happening, but only if you stop treating every unanswered question as permission to force your way inside."

            scene g33
            with medium_dissolve

            lor "For now, you know more than you did ten minutes ago."
            lor "The island is real. The warrior women are real. The queen is real, and the doorway you saw connects their home to this world."
            lor "You still don't know what they call themselves, why my family is connected to them, or why certain people here seem to know you."
            lor "I know that's frustrating, but giving you every answer before I understand what is happening to you could make things much worse."
            lor "Take a breath. Put the questions aside for a moment, and let's get through this yoga session without either of us invading the other's mind."

            menu:
                "This is FUCKING crazy, Lorraine! An island of warrior women in another world? Who the hell are you people!?":



                    pass
                "You keep giving me that 'you're not ready' bullshit. Do you realize how cliché that sounds?":

                    pass
                "Who is that queen, and why do you keep crossing between worlds?":

                    pass


            lor "......."
            lor "..........."
            lor ".............."

            scene g35
            with medium_dissolve
            stop music fadeout 2.0

            lor "Oh, fuck it."

            jump wishes2

label wishes2:

    scene lorrainestrip
    with ffast_dissolve
    if not persistent.seen_lorrainestrip:


        $ config.allow_skipping = False
        $ renpy.pause(15, hard=True)
        $ config.allow_skipping = True


        $ persistent.seen_lorrainestrip = True
        $ renpy.save_persistent()
    else:



        pause 15

    scene g39
    play music my_audio["think2evil"] loop
    with medium_dissolve

    lor "T-There..."
    lor "Will you calm down now?"

    menu:
        "What....in the world.....are you doing?":



            pass
        "Uh......":

            pass
        "Wow.":

            pass
        "..........":

            pass

    scene g40
    with medium_dissolve

    lor "It was the only way to get you to listen to me and calm down."
    lor "You're a man after all, and this is the only way I know to get a man to listen to you when he's out of control."
    lor "......."
    lor "Y-You're... also the first man in years to see me like this, okay?"
    lor "And I-I am not a whore or a slut. I'm a woman, and even standing here naked, I expect you to treat me with respect. Got it?"

    scene g42
    with medium_dissolve

    lor "....."
    lor ".........."
    lor "............."
    mc "..............."

    scene g45
    with medium_dissolve

    voice my_audio["633"]
    nar "There's... something strange here."
    voice my_audio["634"]
    nar "Lorraine took off her clothes because she wanted to get you to listen. But, she's just standing there naked, not saying a word."
    voice my_audio["635"]
    nar "You're starting to get the feeling that she has something else on her mind."
    voice my_audio["636"]
    nar "And you know exactly what it is."

    menu:
        "So....you wanna fuck?":




            lor "......."
            lor ".........."
            lor "............."

            scene g46
            with medium_dissolve
            lor "Is it that obvious?"
            lor "Don't get too full of yourself though..."
            lor "I'm just horny, and you're hot."
            lor "Now get on the bed before I change my mind."

            menu:
                "Oh! Commanding and sexy! I like it!":



                    pass
                "Sure, I'll have you screaming in no time.":

                    pass
                "I was wondering what your pussy felt like. Glad I get to finally experience it.":

                    pass

            lor "Don't be a jerk!"
            lor "Just get on the bed!"

            jump lorrainesexscene
        "I'm going to assume that you want to fuck me.":


            lor "......."
            lor ".........."
            lor "............."

            scene g46
            with medium_dissolve
            lor "Is it that obvious?"
            lor "Don't get too full of yourself..."
            lor "I'm just horny, and you're hot."
            lor "Now get on the bed before I change my mind."

            menu:
                "Oh! Commanding and sexy! I like it!":



                    pass
                "Sure, I'll have you screaming in no time.":

                    pass
                "I was wondering what your pussy felt like. Glad I get to finally experience it.":

                    pass

            lor "Don't be a jerk!"
            lor "Just get on the bed!"

            jump lorrainesexscene
        "How long.....has it been since you had sex, Lorraine? 5 years? 10 years?":


            scene g46
            with medium_dissolve

            lor "Is it that obvious? Yes, I haven't been with anyone in a long time!"
            lor "It's not my fault, men just can't handle my personality is all, and I doubt you can either!"
            lor "So how about we just....get on with this so it can be over."
            lor "Just get on the bed before I change my mind."

            jump lorrainesexscene

label lorrainesexscene:
    stop music fadeout 2.0

    scene black
    with slowfade
    play music my_audio["apartment4"] loop fadein 2.0

    pause 2.0

    scene lorrainesex1
    with ffast_dissolve
    call godson_locked_cutscene ("gui/lorrainesex1.webm", 61.0, "seen_lorrainesex1") from _call_godson_locked_cutscene_3

    $ unlock_gallery_scene("lorraine")

    voice my_audio["637"]
    nar "WHAT IN THE BLOODY HELL WAS THAT!?"
    voice my_audio["638"]
    nar "For one promising minute, Lorraine appeared to be keeping pace. Then she made one sound, went completely rigid, and collapsed across your chest apologizing for finishing before you had properly begun."
    voice my_audio["639"]
    nar "This woman CLEARLY hasn't had sex in years, and apparently her body treated your first few thrusts like this was some sort to race to the finish line."
    voice my_audio["640"]
    nar "So here you are! Arms spread, your cock presumably filing a formal complaint, and you laying there wondering whether to comfort her, congratulate yourself, or to simply say, what the fuck?"

    scene black

    voice my_audio["641"]
    nar "Oh, and did I forget the best part? Lorraine simply got up... and left."
    voice my_audio["642"]
    nar "Not a word. No awkward explanation, no promise of a rematch, not even the common courtesy of pretending that whatever just happened qualified as sex."
    voice my_audio["643"]
    nar "Well, that was certainly an experience. How about we continue with the story and agree to dig this little tragedy back up another time, shall we?"

    jump nina1alt

label lorraine_respects_privacy:

    if evil:
        if sexwithmarnie or fooledaroundwithmarnie:
            voice my_audio["594-2"]
            nar "Really? Restraint? You sure as hell didn't find any when Marnie was in front of you, but apparently Lorraine's private thoughts are where you have finally decided to draw a line."
        elif marnie_interview_watched:
            voice my_audio["594-3"]
            nar "Well, this is unexpected. You were willing to watch Marnie's private interview from behind a door, yet walking into Lorraine's thoughts is somehow a step too far. A strangely specific conscience, but a conscience nonetheless."
        elif memory_nina_crossed_line or nina_guilt_success or memory_nina_is_boyfriend or memory_nina_wait_response or memory_nina_hates_you:
            voice my_audio["594-4"]
            nar "You pushed Nina until her boundaries nearly disappeared, and now you are choosing not to invade Lorraine's mind? Really? Perhaps restraint has finally arrived, unfashionably late but technically present."
        elif triedtogetmarnieupstairs:
            voice my_audio["594-5"]
            nar "You spent part of last night trying to push Marnie upstairs, yet today you are respecting Lorraine's privacy. I would call that growth, although one decent decision may be a little early for a parade."
        else:
            voice my_audio["594-6"]
            nar "Really? After everything you have done since entering this house, Lorraine's thoughts are where you choose to show restraint? Unexpected, certainly, but perhaps not entirely unwelcome."
    elif sexaddict:
        if sexwithmarnie or fooledaroundwithmarnie:
            voice my_audio["594-7"]
            nar "Interesting. You showed precious little physical restraint with Marnie, yet you are unwilling to violate Lorraine's mind for an answer. Apparently even your appetite has boundaries."
        elif triedtogetmarnieupstairs:
            voice my_audio["594-8"]
            nar "You tried rather enthusiastically to get Marnie upstairs last night, but you are leaving Lorraine's thoughts alone. An oddly selective display of restraint, though I suppose we should take our victories where we find them."
        else:
            voice my_audio["594-9"]
            nar "So your lack of restraint does have limits. Lorraine may interest you in several very obvious ways, but her private thoughts are staying private. That is almost respectable."
    elif good:
        if marnie_interview_stopped:
            voice my_audio["594-10"]
            nar "You stepped in when Marnie's privacy and safety were threatened, and now you are extending Lorraine the same consideration. At least your principles remain intact when nobody is watching."
        elif deniedjennifer:
            voice my_audio["594-11"]
            nar "You resisted Jennifer when she tried to pull you across a line, and now you are refusing to cross one with Lorraine. Frustrating as this mystery may be, you are remaining consistent."
        else:
            voice my_audio["594-16"]
            nar "You could take the answer without permission, but you choose to let Lorraine keep what belongs to her. The mystery remains, although so does your decency."
    else:
        voice my_audio["594-17"]
        nar "You leave Lorraine's thoughts untouched. Whatever answers she carries will have to be earned another way."

    jump yoga1

label yoga1:

    play music my_audio["think"] loop fadein 2.0

    scene black
    with slowfade

    pause 2.0

    scene galt2
    with slowfade

    lor "Okay, just like that. Keep me steady."
    lor "I can really feel the stretch. It's been too long since I've done this properly."
    lor "Thanks for helping me maintain the pose."

    scene galt3
    with medium_dissolve

    lor "Make sure my back stays straight. It's easy to forget form when you're focusing on stretching."
    lor "This position always reminds me how important it is to stay flexible."
    lor "And not just physically. Being flexible in life matters just as much, don't you think?"
    lor "Anyway, let's not get too philosophical during yoga. Focus on the stretch."

    menu:
        "You're doing great. Feel okay to hold it a bit longer?":




            lor "Yeah, I think I can manage a little longer. Every second counts, right?"
            lor "But let's not overdo it. I don't want to turn into a pretzel."
            lor "Okay, that should be enough. Let's move on to the next position."
            pass
        "Remember to breathe. It helps with the stretch.":


            lor "Right, breathing is key. In and out, nice and steady."
            lor "It's easy to forget to breathe properly when you're focusing on not falling over."
            lor "Thanks for the reminder. That should be enough for now. What's the next position?"
            pass
        "Your form looks perfect from here.":


            lor "I'm glad to hear that. It feels like I'm getting the hang of it again."
            lor "Having you here to guide and support me makes a big difference."
            lor "Anyway, I think that should be enough stretching for now. Ready to try something new?"
            pass
        "Keep that ass up!":


            lor "I believe my butt is up, isn't it?"
            lor "But anyway, let's not overdo it. I don't want to turn into a pretzel."
            lor "That should be enough. Let's move on to the next position."
            pass

    scene black
    with slowfade

    pause 1.0

    scene galt4
    with ffade

    $ pe1777 = "{image=good} *Suck on Lorraine's toes when she moves her legs.*"

    lor "This next pose requires a bit more balance. Are you ready to assist?"
    lor "You need to stay focused here, or we might both end up on the floor."
    lor "Understand?"
    lor "......"
    lor "........."
    lor "Hello? Are you listening?"

    scene galt5
    with medium_dissolve

    menu:
        "Yeah yeah, I'm listening. Don't let you fall, got it.":

            jump lisen1
        "What? Y-Yeah, I got it.":

            jump lisen2
        "I'm listening.":

            jump lisen1

        "[pe1777]" if supergood_restraint_ready():
            $ supergood_devotion_started = True
            $ lorraine_makeout_attempts = 0
            voice my_audio["688"]
            nar "Wait, what!? Suck on Lorraine's toes? No, no, that is not a good deed! That's giving in to temptation with several deeply questionable extra steps!"
            voice my_audio["689"]
            nar "You've shown restraint at every opportunity. You kept your hands to yourself, ignored every temptation, and now Lorraine raises two feet and this is where your discipline finally dies?"
            voice my_audio["690"]
            nar "Although... this doesn't feel like ordinary lust. You're looking at her less like a temptation and more like someone to worship. Still, I suppose I don't get a vote. You've already decided what you're doing, so apparently we're doing this."
            scene lorrainefloortoessuck
            with ffast_dissolve
            if not persistent.seen_lorrainefloor1:


                $ config.allow_skipping = False
                $ renpy.pause(14, hard=True)
                $ config.allow_skipping = True


                $ persistent.seen_lorrainefloor1 = True
                $ renpy.save_persistent()
            else:

                pause 14
            jump listen3

label listen3:

    lor "......"
    lor "........."
    lor "L-Let's......just forget that happened and move on..."
    jump pose3

label lisen2:

    lor "Good to hear. I'm going to stretch my legs now. Steady me, please."
    lor "This requires a lot of trust, you know. I'm counting on you."
    lor "There, I'm stretching... Make sure I don't tip over."

    scene galt6
    with medium_dissolve

    lor "This is some pose, isn't it? What do you think?"
    lor "Honestly, it's a little embarrassing being this exposed."
    lor "But I trust you. And I can already feel the improvement."
    lor "Alright, that should be enough for now. Let's switch positions."

    scene galt7
    with medium_dissolve

    menu:
        "You're doing amazing. Your form is perfect.":




            lor "Thank you. It's reassuring to have your support."
            lor "I didn't realize how much I needed this... the stretching, the focus."
            lor "It's actually been pretty therapeutic, in more ways than one."
            lor "Well then, let's move on. What's next?"
            jump pose3
        "I'm impressed by your flexibility.":


            lor "Am I? Well, I guess all those years of yoga finally paid off."
            lor "It's different, doing this with someone. I feel more... motivated."
            lor "Thank you for being here, for doing this with me."
            lor "I think I'm ready for the next challenge. Lead the way."
            jump pose3
        "Your dedication is truly inspiring.":


            lor "Is it? I just... want to feel my best, you know?"
            lor "Having you here, it's made a significant difference. Thank you."
            lor "This has been a good session. I feel... lighter, somehow."
            lor "Ready for the next pose. I'm all in."
            jump pose3
        "Incredible! Perfect form!":


            lor "Is it? I just... want to feel my best, you know?"
            lor "Having you here, it's made a significant difference. Thank you."
            lor "This has been a good session. I feel... lighter, somehow."
            lor "Ready for the next pose. I'm all in."
            jump pose3


label lisen1:

    lor "Alright then, I'm going to stretch my legs now."
    lor "Keep a steady grip, and remember, it's all about balance."
    lor "Focus on my breathing... Inhale... Exhale..."

    scene galt6
    with medium_dissolve

    lor "How does my form look from there?"
    lor "It feels surprisingly freeing to stretch this way."
    lor "I haven't been able to do this properly in years."
    lor "What do you think? Am I doing alright?"

    scene galt7
    with medium_dissolve

    menu:
        "You're doing great. Your form is top-notch!":




            lor "That's reassuring to hear. Thank you."
            lor "Yoga is not just physical for me; it's a mental exercise as well."
            lor "Each pose teaches me something new about my limits and capabilities."
            lor "I believe that's enough for this pose. Time for the next position."
            jump pose3
        "Your flexibility is impressive. Keep it up.":


            lor "Thank you. I've been practicing for many years."
            lor "It's moments like these that remind me why I started yoga in the first place."
            lor "It's a journey of self-discovery, isn't it?"
            lor "Okay, I think that's enough for now. Let's move on to the next position."
            jump pose3
        "Absolutely. Your dedication is showing.":


            lor "Much appreciated. It's been a challenge to maintain discipline."
            lor "But with support like yours, it feels a bit easier."
            lor "Yoga is a path to balance, both in body and mind."
            lor "Alright, that should be enough. Ready for the next position?"
            jump pose3
        "Incredible! Perfect form!":


            lor "Is it? I just... want to feel my best, you know?"
            lor "Having you here, it's made a significant difference. Thank you."
            lor "This has been a good session. I feel... lighter, somehow."
            lor "Ready for the next pose. I'm all in."
            jump pose3


label pose3:

    scene black
    with slowfade

    scene galt8
    with ffade

    lor "This... this is the last pose for today."
    lor "I honestly haven't felt this relaxed in years. Having your help made a real difference."
    lor "It's fascinating, how much trust we've built in just one session, don't you think?"
    lor "......."
    lor ".........."
    lor "............"

    scene galt9
    with medium_dissolve

    lor "......well, speaking of trust, I do have a favor to ask."
    lor "......."
    lor ".........."
    lor "Can you....slap me?"
    $ pe17779 = "{image=good} *Make out with her instead.*"
    $ pe177789 = "{image=supergood} *Make out with her instead.*"
    lor "Just.....I don't know. Give me a good hard slap across the face."
    jump lorrainechoice1

label lorrainechoice1:

    menu:
        "What? Hell no.":

            pass
        "Absolutely not.":

            pass
        "Yeah, I ain't doing that.":

            pass

        "[pe17779]" if supergood_devotion_started:

            $ lorraine_makeout_attempts += 1

            if lorraine_makeout_attempts == 1:

                voice my_audio["691"]
                nar "No, no, no! What are you doing? She asked you to slap her, and somehow your answer is to start making out with her? That is not one of the available moral interpretations!"
                voice my_audio["692"]
                nar "You have spent this entire day practicing restraint. Sucking her toes was already a baffling detour, but perhaps we could have buried that beneath the yoga mat and moved forward."
                voice my_audio["693"]
                nar "Let us return and select the sensible answer. No, Lorraine, we are not slapping you. No improvising, no kissing, and preferably no further contact with her feet."

                jump lorrainechoice1

            elif lorraine_makeout_attempts == 2:

                voice my_audio["694"]
                nar "Again!? We have just discussed this! Rejecting violence does not automatically authorize you to replace it with your mouth!"
                voice my_audio["695"]
                nar "She asked for a slap. We say no, preserve our dignity, and continue behaving like the remarkably disciplined man you have pretended to be until now."
                voice my_audio["696"]
                nar "One more time. Go back, choose a refusal, and leave the woman's lips entirely out of this decision."

                jump lorrainechoice1
            else:


                voice my_audio["697"]
                nar "You are seriously choosing it again? I told you... Wait."
                stop music
                voice my_audio["698"]
                nar "This is not a momentary lapse, is it? You resisted every other woman, yet with Lorraine you keep returning, lowering yourself before her, refusing to hurt her, and choosing affection instead."
                voice my_audio["699"]
                nar "I see. You do not merely desire this woman. You have decided she is someone to cherish... perhaps even worship. Very well. If Lorraine is the one woman you have chosen above all others, then stop pretending this is an accident and kiss.....our queen."
                $ good = False
                $ supergood = True
                $ default_mouse = "supergood"

                menu:
                    "[pe177789]":

                        pass
                    "[pe177789]":

                        pass
                    "[pe177789]":

                        pass
                    "[pe177789]":

                        pass

                scene lorrainemakeout
                with ffast_dissolve
                if not persistent.seen_lorrainemakeout:


                    $ config.allow_skipping = False
                    $ renpy.pause(14, hard=True)
                    $ config.allow_skipping = True


                    $ persistent.seen_lorrainemakeout = True
                    $ renpy.save_persistent()
                else:

                    pause 14
                jump outro



    scene galt10
    with medium_dissolve

    lor "Then I guess we have nothing else to talk about."
    lor "I thought you, of all people, might understand. It's disappointing, truly."
    lor "I'll be on my way then."

    scene galt11
    with medium_dissolve

    menu:
        "Wait a sec. You're seriously about to walk out because I didn't want to slap you? How's that fair?":




            lor "It's not just about what you didn't want to do. It's about understanding and respect."
            lor "And clearly, we're not on the same page about either."
            lor "So yes, I think it's best I leave."
            pass
        "I'm sorry, I'm not doing it.":


            lor "I wasn't asking for an apology, but for an open mind."
            lor "I see now that I was mistaken to expect that from you."
            lor "Goodbye."
            pass
        "Not gonna happen Lorraine, sorry.":


            lor "Sorry doesn't really cover it, but okay."
            lor "I've made my peace with it. I'll see myself out."
            pass


    scene galt12
    with medium_dissolve

    lor "I shouldn't linger over this. There's nothing more to be said."
    lor "I should probably start getting ready for Jennifer's birthday party tonight."
    lor "It was... enlightening, to see this side of you. But I'm done here."
    lor "Goodbye, then. Take care."
    $ didntslaplorraine = True

    scene galt13
    with medium_dissolve
    pause

    scene galt14
    with medium_dissolve
    pause

    scene galt15
    with medium_dissolve
    pause

    scene galt16
    with medium_dissolve
    pause

    jump nina1alt
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

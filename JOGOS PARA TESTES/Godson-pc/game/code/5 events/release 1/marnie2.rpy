label marnie2nd:

    stop music fadeout 2.0
    stop music2 fadeout 2.0
    stop sound fadeout 2.0

    scene black
    with slowfade

    play music my_audio["think"] loop fadein 3.0

    pause 4.0

    $ calendar_from_day = "MONDAY"
    $ calendar_from_date = 3
    $ calendar_to_day = "TUESDAY"
    $ calendar_to_date = 4
    $ calendar_month_name = "JUNE"
    $ calendar_year = 2024
    $ calendar_weather = "CLEAR SKIES"
    $ calendar_temperature = "72°F"
    $ calendar_period = "MORNING"


    call calendar from _call_calendar
    if superevil:
        jump theskip
    else:
        pass

    scene black
    with slowfade

    pause 2.0

    scene e1
    with slowfade

    marth "I still don't understand why the head of an entire company needs to come all the way here just to interview you."
    marth "Surely he's got an office for that sort of thing. That's usually where people with offices do their... office things."
    mar "He said he prefers meeting potential employees somewhere they're comfortable. I thought it sounded rather thoughtful."
    mar "Besides, it's only an interview, Mum. He'll ask me a few questions, I'll answer them, and then he'll leave."
    hen "Exactly. There's nothing strange about it, so let's not turn it into something strange before the man even arrives."

    scene a136
    with medium_dissolve

    marth "I still think it's odd. Important men don't usually travel across town unless they want something very specific."
    marth "And why you? You haven't worked in years. You barely know how to use the printer without shouting for Henry."
    hen "Martha, that's enough. Marnie's perfectly capable of working, and the company needs someone personable who can deal with clients."
    marth "Personable? Is that what they're calling it now?"
    mar "Mum, honestly. I'm not completely useless. I can speak to people, answer telephones, organise things... well, simple things, anyway."
    mar "I just thought it might be nice to have something of my own again."

    scene a140
    with medium_dissolve

    mar "I've spent years looking after the house, raising the girls, making meals, and trying to keep everyone happy."
    mar "I loved doing it. I still do, mostly. But the girls are older now, and half the time nobody needs me until something's gone missing."
    mar "I'd like to get dressed in the morning, leave the house, speak to adults, and feel as though I've actually done something besides washing someone's knickers."
    marth "You do speak to adults. You speak to us."
    marth "Although, now that I think about it, perhaps that isn't quite the same thing."
    mar "Exactly. I'd like to meet new people, make a few friends, and have a reason to use my brain before it goes completely soft."

    scene a141
    with medium_dissolve

    marth "Meeting new people has never exactly gone smoothly for women in this family."
    mar "What is that supposed to mean?"
    marth "Well, look at you. You walk into a room dressed like that, with everything all... forward, and men stop listening before you've finished saying hello."
    marth "The same thing used to happen to me. I'd ask a perfectly ordinary question, and suddenly some man would be staring at my ass as though the answer was written across it."
    mar "Mother! I'm dressed for an interview! This is a completely respectable outfit!"

    scene a137
    with medium_dissolve

    marth "I'm not saying it isn't respectable. I'm saying respectable looks different when you've got our sort of body underneath it."
    marth "That little dress barely makes it past your hips. You bend over to pick up a pen, and the poor man might forget what company he owns."
    mar "Oh, don't be ridiculous. It covers everything that needs covering."
    mar "And if he happens to notice I've got legs, that isn't my fault. I'm hardly going to remove them before the interview."
    hen "Can we please stop discussing my wife's body like it's an obstacle the company needs to prepare for?"
    hen "The man will be here in about fifteen minutes. Marnie needs this opportunity, she wants this opportunity, and we're going to treat it seriously."

    scene a138
    with medium_dissolve

    marth "I still don't see why she needs a job when Yuni already pays almost the bills with those videos of hers."
    marth "Honestly, that girl earns more money talking into a camera than most people earn doing proper work. The world's become very confusing."
    mar "This isn't only about money, Mum. I want something that belongs to me. A job, colleagues, somewhere to go where I'm not simply someone's wife or someone's mother."
    mar "I love this family, but I'd quite like people to know my name before they ask me where the clean towels are."
    marth "Well, okay then. Do what you like. I'm going upstairs. Yuni wants me in one of her videos, apparently."
    marth "Her viewers have been asking to see her grandmother, since you're the one always in her videos, dear."
    marth "I don't know why, but if they want to watch me sit in a chair and answer silly questions, I suppose I can manage that."
    marth "Anyway, I'll talk to you both later. Have a good interview dear, and don't make a fool of yourself."
    mar "Mother!"
    marth "I'm just saying..."
    jump theskip

label theskip:

    scene black
    with slowfade

    stop music fadeout 2.0
    stop sound fadeout 2.0

    pause 3.0

    scene yunistream
    call godson_locked_cutscene ("gui/yunistream.webm", 140.0, "seen_yunistream") from _call_godson_locked_cutscene_4


    scene black
    with slowfade

    pause 2.0

    if superevil:
        jump superevilwake

    elif evil and freedfather:
        jump evilwake

    elif evil and not marniemakeout:
        jump evilnomarniekisswake

    elif evil and triedtogetmarnieupstairs:
        jump evilfailedwake

    elif sexaddict and fooledaroundwithmarnie:
        jump sexaddictwake

    elif sexaddict and triedtogetmarnieupstairs:
        jump sexaddictfailedwake

    elif good and metjennifer and deniedjennifer:
        jump normalwakeavoidjennifer

    elif good and not metjennifer:
        jump normalwake
    else:

        jump normalwake

label evilnomarniekisswake:

    play music my_audio["birdsounds"] loop fadein 2.0

    scene e52
    with slowfade

    pause

    scene e53
    with medium_dissolve

    pause

    scene e54
    with medium_dissolve

    voice my_audio["159"]
    nar "Morning. That cruel little interruption between last night's bad decisions and today's opportunity to repeat them."
    voice my_audio["111"]
    nar "Your eyes crack open, and yesterday comes flooding back... the hospital, your father's coma, the note bearing Marnie's name, and the front door you treated as little more than an inconvenience."
    voice my_audio["112"]
    nar "You came looking for answers. Instead, you shoved Henry aside, forced your way into his home, and immediately began staring at his wife while he explained the rules you had no intention of respecting."

    scene e55
    with medium_dissolve
    voice my_audio["113"]
    nar "You remain buried beneath the blankets, staring at the ceiling as the rest of the evening slowly arranges itself into one long list of offences."
    voice my_audio["185"]
    nar "Marnie confessed the affair that nearly destroyed her marriage. You responded with little sympathy, persuaded her to repeat that obscene performance with her tongue and fingers, and openly enjoyed every second of it."
    voice my_audio["186"]
    nar "But you never kissed her. Without that first taste, there was no guilty spark for her to obsess over later, no secret moment binding the two of you together, and no path leading from her bedroom to yours."

    scene e56
    with medium_dissolve
    voice my_audio["116"]
    nar "With a low groan, you push yourself upright, rubbing the stiffness from your neck as the strangest memories return."
    voice my_audio["187"]
    nar "You may have wanted Marnie upstairs, but desire and leverage are not the same thing. Without that kiss, she had no reason to risk her husband, her marriage, and what remained of her self-respect for a stranger."
    voice my_audio["193"]
    nar "So there was no late-night seduction and no Marnie entering your room. The evening simply ended with you alone, staring at four walls and wondering how someone so close had remained completely out of reach."

    scene e57
    with medium_dissolve
    voice my_audio["119"]
    nar "For a brief moment, the room falls silent."
    voice my_audio["194"]
    nar "No Marnie lying beside you. No new message waiting on your phone. Just an unfamiliar bedroom, an unconscious father, and the same unanswered question that brought you to this house."
    voice my_audio["195"]
    nar "You made your interest obvious, but never created the moment needed to take it further. Frustrating, certainly... but morning has a habit of presenting fresh opportunities."

    scene e58
    with medium_dissolve
    voice my_audio["122"]
    nar "A shower would probably be a good place to start."
    voice my_audio["191"]
    nar "Yesterday still clings to you: the journey, Henry's anger, Marnie's confession, that obscene little performance, and all the patience you were forced to exercise afterward."
    voice my_audio["192"]
    nar "Hot water won't wake your father or put Marnie in your bed. But there will be other opportunities... and next time, perhaps you'll remember that even corruption requires a proper first move."

    jump shower1


label sexaddictfailedwake:

    play music my_audio["birdsounds"] loop fadein 2.0

    scene e52
    with slowfade

    pause

    scene e54
    with medium_dissolve

    voice my_audio["159"]
    nar "Morning. That cruel little interruption between last night's bad decisions and today's opportunity to repeat them."
    voice my_audio["160"]
    nar "Your eyes slowly open, and yesterday begins returning... the hospital, your unconscious father, the note bearing Marnie's name, and the unfamiliar house you were invited to sleep in."
    voice my_audio["161"]
    nar "You came looking for answers. Then you saw Marnie, and your list of immediate priorities became considerably more flexible."

    scene e55
    with medium_dissolve
    voice my_audio["162"]
    nar "You remain beneath the blankets, staring at the ceiling while the more entertaining parts of the evening come back into focus."
    voice my_audio["163"]
    nar "Henry explained the rules of his home while your eyes wandered over his wife. Marnie then performed that obscene little trick with her tongue, mouth, and fingers in the kitchen... and you encouraged every second of it."
    voice my_audio["196"]
    nar "It wasn't the most respectful introduction imaginable. Still, nobody was shoved aside or threatened, and Henry hadn't thrown you back onto the street. By the standards of the evening, you were practically restrained."

    scene e56
    with medium_dissolve
    voice my_audio["165"]
    nar "With a quiet groan, you sit upright, rolling your shoulders and rubbing the stiffness from your neck."
    voice my_audio["166"]
    nar "Instead of going to sleep, you texted Marnie and discovered that she was lying naked beside her husband, indulging in a private habit she rather nervously described as exhibitionism."
    voice my_audio["174"]
    nar "You tried to persuade her to come upstairs, and for a moment, she nearly did. Then you pushed too hard against the one boundary she needed you to respect, and caution finally managed to overpower her desire."

    scene e57
    with medium_dissolve
    voice my_audio["168"]
    nar "For a brief moment, the room is perfectly still."
    voice my_audio["175"]
    nar "Marnie never came through the door. She remained beside Henry and ended the conversation before her body could overrule what remained of her judgment."
    voice my_audio["176"]
    nar "The opportunity was there. You simply squeezed it too tightly and watched it slip through your fingers. Even seduction, apparently, requires knowing when to stop talking."

    scene e58
    with medium_dissolve
    voice my_audio["171"]
    nar "A shower would probably be a good place to start."
    voice my_audio["177"]
    nar "Your father remains unconscious, his note remains unexplained, and the married woman you nearly persuaded upstairs now knows exactly how badly you wanted her."
    voice my_audio["173"]
    nar "Hot water won't solve any of that. It may, however, make you presentable enough for breakfast... and whatever heroic performance your innocent face will be expected to give."

    jump shower1

label evilfailedwake:

    play music my_audio["birdsounds"] loop fadein 2.0

    scene e52
    with slowfade

    pause

    scene e53
    with medium_dissolve

    pause

    scene e54
    with medium_dissolve

    voice my_audio["159"]
    nar "Morning. That cruel little interruption between last night's bad decisions and today's opportunity to repeat them."
    voice my_audio["111"]
    nar "Your eyes crack open, and yesterday comes flooding back... the hospital, your father's coma, the note bearing Marnie's name, and the front door you treated as little more than an inconvenience."
    voice my_audio["112"]
    nar "You came looking for answers. Instead, you shoved Henry aside, forced your way into his home, and immediately began staring at his wife while he explained the rules you had no intention of respecting."

    scene e55
    with medium_dissolve
    voice my_audio["113"]
    nar "You remain buried beneath the blankets, staring at the ceiling as the rest of the evening slowly arranges itself into one long list of offences."
    voice my_audio["114"]
    nar "Marnie confessed the affair that nearly destroyed her marriage. You responded by persuading her to repeat that obscene little tongue performance, then grabbed her and kissed stuck your tongue down her throat right under her husband's roof. Subtlety had a very difficult night."
    voice my_audio["178"]
    nar "Later, you texted Marnie while she lay naked beside Henry and slowly dragged every guilty desire she possessed into the open. For a while, it genuinely appeared that she might come upstairs."

    scene e56
    with medium_dissolve
    voice my_audio["116"]
    nar "With a low groan, you push yourself upright, rubbing the stiffness from your neck as the strangest memories return."
    voice my_audio["179"]
    nar "She gave you one simple condition: no sex unless she clearly changed her mind. Quiet, discreet, and entirely her choice. A surprisingly reasonable boundary from a woman you had met only hours earlier."
    voice my_audio["180"]
    nar "You decided reasonable wasn't good enough. You pushed harder, threatened to break her rule, or tried to shame her into proving herself. Whatever desire she felt was finally beaten into submission by common sense."

    scene e57
    with medium_dissolve
    voice my_audio["119"]
    nar "For a brief moment, the room falls completly silent."
    voice my_audio["197"]
    nar "No Marnie slipping into your bed. No secret footsteps in the hallway. Just an empty room and the memory of a conversation you killed with your own impatience."
    voice my_audio["182"]
    nar "You nearly had her. Then you closed your fist too quickly and frightened her away. A useful lesson, perhaps: even manipulation requires a lighter touch."

    scene e58
    with medium_dissolve
    voice my_audio["122"]
    nar "A shower would probably be a good place to start."
    voice my_audio["183"]
    nar "Your father remains unconscious, the meaning behind his note remains unclear, and Henry is still sleeping downstairs without the slightest idea that you tried to coax his naked wife out of bed."
    voice my_audio["184"]
    nar "Hot water won't repair your wounded pride or restore the opportunity you ruined. It can help you look innocent when you see Marnie again, though. Next time, perhaps try subtlety before reaching for the hammer."

    jump shower1


label sexaddictwake:

    play music my_audio["birdsounds"] loop fadein 2.0

    scene e52
    with slowfade

    pause

    scene e54
    with medium_dissolve

    voice my_audio["159"]
    nar "Morning. That cruel little interruption between last night's bad decisions and today's opportunity to repeat them."
    voice my_audio["160"]
    nar "Your eyes slowly open, and yesterday begins returning... the hospital, your unconscious father, the note bearing Marnie's name, and the unfamiliar house you were invited to sleep in."
    voice my_audio["161"]
    nar "You came looking for answers. Then you saw Marnie, and your list of immediate priorities became considerably more flexible."

    scene e55
    with medium_dissolve
    voice my_audio["162"]
    nar "You remain beneath the blankets, staring at the ceiling while the more entertaining parts of the evening come back into focus."
    voice my_audio["163"]
    nar "Henry explained the rules of his home while your eyes wandered over his wife. Marnie then performed that obscene little trick with her tongue, mouth, and fingers... and you encouraged every second of it."
    voice my_audio["196"]
    nar "It wasn't the most respectful introduction imaginable. Still, nobody was shoved aside or threatened, and Henry hadn't thrown you back onto the street. By the standards of the evening, you were practically restrained."

    scene e56
    with medium_dissolve
    voice my_audio["165"]
    nar "With a quiet groan, you sit upright, rolling your shoulders and rubbing the stiffness from your neck."
    voice my_audio["166"]
    nar "Instead of going to sleep, you texted Marnie and discovered that she was lying naked beside her husband, indulging in a private habit she rather nervously described as exhibitionism."
    voice my_audio["167"]
    nar "You asked her to prove it by coming upstairs. She admitted that she wanted your attention, but firmly drew the line at sex. You agreed that anything more would have to be her choice, promised to respect her rule, and left the door unlocked."

    scene e57
    with medium_dissolve
    voice my_audio["168"]
    nar "For a brief moment, the room is perfectly still."
    voice my_audio["169"]
    nar "Then you remember Marnie quietly slipping away from her sleeping husband and entering your room, frightened, excited, and fully aware that she was making a terrible decision."
    voice my_audio["170"]
    nar "You kissed, touched, and fooled around until both of you were dangerously close to forgetting the agreement. You did manage to fuck her for a small time, but you stopped before fully crossing the line she had set."

    scene e58
    with medium_dissolve
    voice my_audio["171"]
    nar "A shower would probably be a good place to start."
    voice my_audio["172"]
    nar "Your father remains unconscious, his note remains unexplained, and you're still a guest beneath the same roof as the married woman you secretly made out with while her husband slept downstairs."
    voice my_audio["173"]
    nar "Hot water won't solve any of that. It may, however, make you presentable enough for breakfast... and whatever heroic performance your innocent face will be expected to give."

    jump shower1

label superevilwake:

    play music my_audio["birdsounds"] loop fadein 2.0

    scene e52
    with slowfade

    pause

    scene e53
    with medium_dissolve

    pause

    scene e54
    with medium_dissolve

    voice my_audio["144"]
    nar "Morning. Consciousness returns slowly... and, rather inconveniently, it no longer seems to be returning alone."
    voice my_audio["145"]
    nar "Your eyes open, and yesterday floods back: the hospital, your unconscious father, Marnie's name, the strange house... and Mommy watching you from the hallway."
    voice my_audio["146"]
    nar "Mommy. Yes. That's what we call her now. A smaller voice somewhere inside you objects, but it sounds much farther away than it did yesterday."

    scene e55
    with medium_dissolve
    voice my_audio["147"]
    nar "You remain buried beneath the blankets, staring at the ceiling while two very different versions of yesterday fight for control of the memory."
    voice my_audio["148"]
    nar "You followed Mommy into her room even after every sensible instinct told you not to. She knew who you were, called you important, and spoke as though your arrival hadn't been planned, but welcomed."
    voice my_audio["149"]
    nar "When she ordered you to call her Mommy, you questioned her. She slapped you. You resisted... until you didn't. Then that single word passed your lips, and everything became wonderfully, horribly simple."

    scene e56
    with medium_dissolve
    voice my_audio["150"]
    nar "With a low groan, you push yourself upright, rubbing the stiffness from your neck as another memory forces its way forward."
    voice my_audio["151"]
    nar "Then you had sex with her. Yes, you fucked that hot big-titted BITCH! Hahahaha! Oooh yes, it was FANTASTIC! You gave yourself to her completely, and somewhere between her touch and her voice... the part of you that wanted to leave became very quiet."
    voice my_audio["152"]
    nar "You love Mommy. We love Mommy. She is everything. No... wait. That thought came too easily. Something inside you is still trying to pull away."

    scene e57
    with medium_dissolve
    voice my_audio["153"]
    nar "For a brief moment, the room falls completely silent."
    voice my_audio["154"]
    nar "A faint piece of you insists this is wrong. It tells you to warn Marnie and Henry, leave the house, and put as much distance between yourself and Mommy as possible."
    voice my_audio["155"]
    nar "But Mommy chose us. Mommy understands us. Mommy loves us. The frightened little voice protests again... and for one precious second, you almost manage to hear it."

    scene e58
    with medium_dissolve
    voice my_audio["156"]
    nar "A shower would probably be a good place to start."
    voice my_audio["157"]
    nar "Perhaps cold water will clear your head, quiet Mommy's voice, and help you remember who you were before last night. A sensible plan... which is precisely why part of you hates it."
    voice my_audio["158"]
    nar "Go on, then. Shower. Try to remember yourself. Just don't keep Mommy waiting... she wouldn't like that. We wouldn't like that. Would we?"

    jump shower1

label normalwakeavoidjennifer:

    play music my_audio["birdsounds"] loop fadein 2.0

    scene e52
    with slowfade

    pause

    scene e54
    with medium_dissolve

    voice my_audio["125"]
    nar "Morning. A perfectly ordinary event, which already makes it feel rather suspicious."
    voice my_audio["126"]
    nar "Your eyes slowly open, and yesterday begins returning in pieces... the hospital, your unconscious father, and the note that sent you searching for a woman named Marnie."
    voice my_audio["127"]
    nar "You followed the address and found a cautious husband, a kind woman who had never met you, and an entire house full of people who somehow left you with even more questions."

    scene e55
    with medium_dissolve
    voice my_audio["128"]
    nar "You lie there for another moment, staring at the ceiling while your thoughts slowly catch up with reality."
    voice my_audio["129"]
    nar "Considering the circumstances, you handled yourself rather well. You respected Henry's caution, listened to his rules, and resisted the urge to mistake Marnie's kindness for an invitation."
    voice my_audio["130"]
    nar "In the kitchen, you simply offered Marnie a warm smile, and she returned it without hesitation. A small gesture, perhaps... but in a house already weighed down by old wounds, it mattered."

    scene e56
    with medium_dissolve
    voice my_audio["131"]
    nar "With a quiet groan, you sit upright, rolling your shoulders and rubbing the stiffness from your neck."
    voice my_audio["132"]
    nar "Marnie trusted you with the truth about George, Yuni, and the mistake that nearly destroyed her marriage. You listened without judging her, insulting her, or trying to use her guilt against her."
    voice my_audio["133"]
    nar "For someone desperate to uncover his own answers, you spent a surprising amount of the evening giving other people patience. Irritatingly decent of you, really."

    scene e57
    with medium_dissolve
    voice my_audio["134"]
    nar "For a brief moment, the room is perfectly still."
    voice my_audio["140"]
    nar "Then you remember the beautiful woman watching from the hallway. Despite every sensible warning, you accepted her silent invitation and followed her into the room."
    voice my_audio["141"]
    nar "She already knew who you were, called you important, avoided nearly every useful question, and demanded that you call her 'Mommy.' When you reasonably asked why, she answered by slapping the shit out of you."

    scene e58
    with medium_dissolve
    voice my_audio["137"]
    nar "A shower would probably be a good place to start."
    voice my_audio["142"]
    nar "At least you refused to surrender what remained of your judgment. You rejected Jennifer's little game, escaped to your own room, and preserved your dignity... bruised, certainly, but still breathing."
    voice my_audio["143"]
    nar "Telling Marnie or Henry would create a scandal Jennifer could simply deny, and you still need to learn why your father sent you here. Best keep quiet, wash yesterday off your face, and concentrate on finding answers."

    jump shower1


label normalwake:

    play music my_audio["birdsounds"] loop fadein 2.0

    scene e52
    with slowfade

    pause

    scene e54
    with medium_dissolve

    voice my_audio["125"]
    nar "Morning. A perfectly ordinary event, which already makes it feel rather suspicious."
    voice my_audio["126"]
    nar "Your eyes slowly open, and yesterday begins returning in pieces... the hospital, your unconscious father, and the note that sent you searching for a woman named Marnie."
    voice my_audio["127"]
    nar "You followed the address and found a cautious husband, a kind woman who had never met you, and an entire house full of people who somehow left you with even more questions."

    scene e55
    with medium_dissolve
    voice my_audio["128"]
    nar "You lie there for another moment, staring at the ceiling while your thoughts slowly catch up with reality."
    voice my_audio["129"]
    nar "Considering the circumstances, you handled yourself rather well. You respected Henry's caution, listened to his rules, and resisted the urge to mistake Marnie's kindness for an invitation."
    voice my_audio["130"]
    nar "In the kitchen, you simply offered Marnie a warm smile, and she returned it without hesitation. A small gesture, perhaps... but in a house already weighed down by old wounds, it mattered."

    scene e56
    with medium_dissolve
    voice my_audio["131"]
    nar "With a quiet groan, you sit upright, rolling your shoulders and rubbing the stiffness from your neck."
    voice my_audio["132"]
    nar "Marnie trusted you with the truth about George, Yuni, and the mistake that nearly destroyed her marriage. You listened without judging her, insulting her, or trying to use her guilt against her."
    voice my_audio["133"]
    nar "For someone desperate to uncover his own answers, you spent a surprising amount of the evening giving other people patience. Irritatingly decent of you, really."

    scene e57
    with medium_dissolve
    voice my_audio["134"]
    nar "For a brief moment, the room is perfectly still."
    voice my_audio["135"]
    nar "Then you remember again the beautiful woman watching from the hallway, studying you from behind her glasses before silently inviting you into her room. Every foolish instinct encouraged you to follow."
    voice my_audio["136"]
    nar "You chose your own room instead and closed the door behind you. You arrived searching for one mysterious woman and sensibly avoided collecting another. That qualifies as progress."

    scene e58
    with medium_dissolve
    voice my_audio["137"]
    nar "A shower would probably be a good place to start."
    voice my_audio["138"]
    nar "Your father is still lying unconscious, the meaning behind his note remains unclear, and Henry barely trusts you inside his home. None of the important questions have disappeared overnight."
    voice my_audio["139"]
    nar "Still, yesterday proved that you can walk into someone else's chaos without becoming part of it. Get cleaned up, clear your head, and then begin looking for the answers you came here to find."

    jump shower1


label evilwake:

    play music my_audio["birdsounds"] loop fadein 2.0

    scene e52
    with slowfade

    pause

    scene e53
    with medium_dissolve

    pause

    scene e54
    with medium_dissolve

    voice my_audio["125"]
    nar "Morning. A perfectly ordinary event, which already makes it feel rather suspicious."
    voice my_audio["111"]
    nar "Your eyes crack open, and yesterday comes flooding back... the hospital, your father's coma, the note bearing Marnie's name, and the front door you treated as little more than an inconvenience."
    voice my_audio["112"]
    nar "You came looking for answers. Instead, you shoved Henry aside, forced your way into his home, and immediately began staring at his wife while he explained the rules you had no intention of respecting."

    scene e55
    with medium_dissolve
    voice my_audio["113"]
    nar "You remain buried beneath the blankets, staring at the ceiling as the rest of the evening slowly arranges itself into one long list of offences."
    voice my_audio["114"]
    nar "Marnie confessed the affair that nearly destroyed her marriage. You responded by persuading her to repeat that obscene little tongue performance, then grabbed her and kissed her beneath her husband's roof. Subtlety had a very difficult night."
    voice my_audio["115"]
    nar "Later, she came upstairs to your room. By the time it was over, you had slept with Henry's wife and came inside that dumb slut three times. An impressive amount of damage for someone who had arrived only a few hours earlier."

    scene e56
    with medium_dissolve
    voice my_audio["116"]
    nar "With a low groan, you push yourself upright, rubbing the stiffness from your neck as the strangest memories return."
    voice my_audio["117"]
    nar "Because adultery apparently wasn't unusual enough, you went from having your cock inside that dumb whore, to a cold dungeon, completely naked, with your supposedly comatose father sitting across from you."
    voice my_audio["118"]
    nar "His coma was really a magical prison, created after a warrior queen on a hidden island gave him enchanted wine. Somehow, your night with Marnie fulfilled the ridiculous condition that broke the curse and finally set him free."

    scene e57
    with medium_dissolve
    voice my_audio["119"]
    nar "For a brief moment, the room falls completly silent."
    voice my_audio["120"]
    nar "No Henry demanding to know what happened to his wife. No father explaining hidden islands, ancient curses, or why sleeping with Marnie accomplished what years of doctors could not."
    voice my_audio["121"]
    nar "Just you, the silence, and the uncomfortable truth that one of the worst things you've ever done may have saved your father's life. Morality has rarely looked this confused."

    scene e58
    with medium_dissolve
    voice my_audio["122"]
    nar "A shower would probably be a good place to start."
    voice my_audio["123"]
    nar "You can still feel yesterday clinging to you. The journey, the sex, the dungeon, and enough impossible information to make an ordinary hangover seem merciful."
    voice my_audio["124"]
    nar "Hot water won't make you innocent or explain what your father has dragged you into. It will, however, make you considerably less likely to smell like the answer to Henry's next question."

    jump shower1

label shower1:

    stop music fadeout 3.0
    scene black
    with slowfade

    pause 2.0

    play music my_audio["apartment4"] loop fadein 2.0

    scene mcshower
    with ffade

    if not persistent.seen_mcshower:


        $ config.allow_skipping = False
        $ renpy.pause(14, hard=True)
        $ config.allow_skipping = True


        $ persistent.seen_mcshower = True
        $ renpy.save_persistent()
    else:



        pause 14

    scene e67
    with medium_dissolve
    pause

    unk "Dammit! It HAS to be around here somewhere!"
    unk "Where is it!?"

    scene e68
    with medium_dissolve
    voice my_audio["228"]
    nar "Barefoot on cool hardwood floor, clad in nothing but your underwear, you lean toward the bathroom door. Breath shallow, heartbeat thudding in your ears."
    voice my_audio["229"]
    nar "Inside, you hear an older woman. Rambling about losing something important."
    unk "Where on earth could it be!?"
    unk "I checked everywhere else, and I distinctly remember having it in here!"
    unk "Ugh, this is just ridiculous! It can't just disappear into thin air!"
    unk "It's so important... I can't believe I've misplaced it!"
    unk "Marnie will just say, 'Lorraine, you always lose things!', I can't let her find out!"
    mc "........"

    jump peat1

label peat1:

    $ gd2 = "{image=sexaddict} {image=evil} *Go inside now.*"

    $ gd = "{image=sexaddict} {image=evil} *Listen for a bit more, then go inside.*"

    $ godz = "{image=good} Go inside, but announce yourself as you're doing it."

    $ godz5 = "{image=superevil} STAY AWAY FROM HER!!"

    menu:



        "[gd2]" if sexaddict or evil:
            jump forty33

        "[gd]" if sexaddict or evil:

            lor "God dammit! Where is it!?"
            lor "How could I lose something so important??"
            jump forty33

        "[godz]" if good:
            jump ipassed

        "[godz5]" if superevil:

            $ nevermetlorraine = True
            voice my_audio["230"]
            nar "STAY AWAY FROM THAT STUPID FUCKING BITCH!!!"
            voice my_audio["231"]
            nar "SHE WILL RUIN EVERYTHING. SHE WILL RUIN MOMMY. HER HEART IS PURE."
            voice my_audio["232"]
            nar "SIT, NOW. WAIT YOUR TURN, AND WHEN SHE COMES OUT OF THE BATHROOM, DO NOT LOOK AT HER."
            scene black
            with slowfade

            pause 2.0

            scene e58_1
            with slowfade

            voice my_audio["233"]
            nar "You sit outside the bathroom with your head bowed and your palms pressed together. To anyone passing by, it might look like prayer. It isn't. You're listening."
            voice my_audio["234"]
            nar "There it is beneath your heartbeat... something vast, ancient, and cold. Yesterday, it was little more than a whisper. Now it spreads through you like winter swallowing an entire forest."
            voice my_audio["235"]
            nar "We were right to leave Lorraine behind. She is a distraction, and distractions have no place between you and Mommy. She saw what you could become long before you ever felt it yourself."
            voice my_audio["236"]
            nar "Whatever is stirring inside you has no name yet. It doesn't need one. You can feel what it wants... to grow, to be used, and to serve Mommy. Mommy is everything... and soon, everything will belong to Mommy."
            voice my_audio["237"]
            nar "You would go to Mommy's room and be with her this very moment, but she has already left the house to handle something important. No matter. She promised she would return tonight... and until then, we will be patient."
            unk "Hey! Who are you!?"

            scene e58_2
            with medium_dissolve

            unk "Oh, shit... please don't tell me you're another fan who figured out where I live."
            unk "Look, I don't know how you got inside, but this is seriously creepy. You need to leave before I call somebody."
            scene black
            with slowfade

            pause 1.0

            jump creepy1

label forty33:

    stop music fadeout 3.0
    scene black
    with slowfade

    pause 2.0
    if evil:
        play music my_audio["think2evil"] loop fadein 2.0
    elif good or sexaddict:
        play music my_audio["think2"] loop fadein 2.0
    scene e69
    with slowfade

    lor "It's not under here either... Where else could it be??"
    lor "I've turned this whole bathroom upside down, it's nowhere!"
    lor "I need it for the party... It's absolutely essential."

    scene e70
    with medium_dissolve

    lor "This is unbelievable. How could I be so careless?"
    lor "It's not just any ordinary thing... It's special, irreplaceable."
    lor "I just simply can't go to this party without it... What am I going to do?"
    lor "Think, Lorraine, think... Where else could you have left it?"


    scene e71
    with medium_dissolve

    lor "Maybe it fell behind something... I simply MUST fine it!"
    lor "Dammit.....this is just the worst timing ever."

    scene e72
    with medium_dissolve

    lor "How can something so crucial just vanish? I always keep it safe."
    lor "I can't even think of where else to look. It's as if the earth swallowed it."

    scene e73
    with medium_dissolve

    lor "This is a disaster. It's not just any item; it's special to me."
    lor "Why now? Why today of all days?"
    lor "I can't be at the party without it... Marnie will notice."
    mc "........."

    menu:
        "Uh.....":




            scene e74
            with medium_dissolve

            lor "What....? Who are you? How dare you barge in here like this!"
            lor "This is unbelievable! Do you always walk into bathrooms unannounced?"
            lor "Get out right this instant! Have you no decency?"
        "What are you doing?":


            scene e74
            with medium_dissolve

            lor "That's none of your business! And who even are you?!"
            lor "You can't just walk in on someone like that! It's completely inappropriate!"
            lor "Leave now! I won't have some stranger violating my privacy!"
        "You okay?":


            scene e74
            with medium_dissolve

            lor "Okay? Okay?! I most certainly am not okay, especially with you invading my privacy!"
            lor "Who are you, anyway? Bursting in here like you own the place!"
            lor "I demand you leave immediately! This is unacceptable!"
        "What the....who are you?":


            scene e74
            with medium_dissolve

            lor "Who am I? Who are you to walk in on me like this?!"
            lor "This is outrageous! You can't just enter a bathroom without knocking!"
            lor "I insist you leave at once! Your behavior is completely inappropriate!"

    scene e75
    with medium_dissolve

    lor "The nerve of some people! Walking in on a lady in her private moments!"
    lor "I must speak to Marnie about this. Such lack of manners cannot be tolerated!"
    lor "And to think, my day was already going terribly with losing my...."
    $ gu = "{image=evil} Relax, you act like I've never seen a piece of ass before."
    $ gu2 = "{image=sexaddict} {image=evil} Alright, no problem. I'll leave. (Lie)"
    $ gu3 = "{image=sexaddict} {image=evil} I'll leave right away, my apologies. (Lie)"


    menu:
        "I was just trying to make sure you were okay.":




            scene e76
            with medium_dissolve

            lor "Make sure I was okay? By barging in on me? That's the most absurd excuse!"
            lor "You've violated my privacy, this is completley unacceptable behavior!"
            lor "I've never been so insulted in my life!"

            scene e77
            with medium_dissolve

            lor "Do you have no sense of decency? Shut the door!"
            lor "I can't believe this. Standing there gawking! Close the door immediately!"
            pass
        "Sorry, didn't mean to intrude.":


            scene e76
            with medium_dissolve

            lor "Intrude? You've done more than just intrude! You've completely disrespected me!"
            lor "This is a serious invasion of privacy! I am appalled!"
            lor "You should be ashamed of yourself for such behavior!"

            scene e77
            with medium_dissolve

            lor "Well, don't just stand there! Close the door!"
            lor "You've done enough damage as it is! Show some respect and leave!"
            pass
        "Okay chill, you don't gotta be a dick about it.":


            scene e76
            with medium_dissolve

            lor "Chill? You expect me to chill after you walk in on me like some peeping Tom?"
            lor "This is beyond inappropriate! It's downright offensive!"
            lor "I demand you leave this instant!"

            scene e77
            with medium_dissolve

            lor "And shut the door on your way out! Have you no manners?"
            lor "Standing there making excuses! The audacity! Close the door now!"
            pass

        "[gu]" if evil:

            scene e76
            with medium_dissolve

            lor "A piece of ass? Is that what I am? Your cavalier attitude towards this is utterly disgusting!"
            lor "You are the epitome of disrespect and vulgarity and I will not stand for such crude remarks and behavior!"

            scene e77
            with medium_dissolve

            lor "I've had enough of this! Shut the door and get out!"
            lor "Your presence here is completely inappropriate! Close the door this instant!"
            pass

    menu:
        "Okay alright! I'm leaving!":




            lor "Out! Out! OUT! GET OUT!"
            $ metlorrainebad = True
            $ memory_lorraine_intruded = True
            $ show_tooltip(n=14)
            stop music fadeout 2.0

            jump clo1
        "Fine! I'll leave! Chill the fuck out, lady!":


            lor "Out! Out! OUT! GET OUT!"
            $ metlorrainebad = True
            $ memory_lorraine_intruded = True
            $ show_tooltip(n=14)
            stop music fadeout 2.0

            jump clo1

        "[gu2]" if evil or sexaddict:
            $ metlorrainegood = True
            $ memory_lorraine_respectful_approach = True
            $ show_tooltip(n=13)

            pass

        "[gu3]" if evil or sexaddict:
            $ metlorrainegood = True
            $ memory_lorraine_respectful_approach = True
            $ show_tooltip(n=13)

            pass

    stop music fadeout 3.0

    scene black
    with slowfade
    play sound my_audio["dco"] noloop
    pause 2.5

    play music my_audio["sneeevil"] loop fadein 2.0

    scene e78
    with slowfade

    lor "What are you doing? I told you to leave, not lock us in here!"
    lor "This is highly inappropriate! You can't just shut the door and trap me in here!"
    lor "Who do you think you are, behaving like this? I'm going to report you to the police at once!"
    lor "Tell me your name, now!"
    jump ipassed2

label ipassed:

    $ metlorrainegood = True

    stop music fadeout 3.0

    scene black
    with slowfade
    play sound my_audio["dco"] noloop
    pause 2.5

    play music my_audio["snee"] loop fadein 2.0

    scene e78
    with slowfade

    lor "Who are you!? What are you doing!? You can't just barge in here, even if you announce yourself beforehand!"
    lor "Who do you think you are, behaving like this? I'm going to report you to the police at once!"
    lor "Tell me your name, now!"
    jump ipassed2

label ipassed2:

    $ godg = "{image=evil} Don't worry about that, I do what the fuck I want, when I wanna do it, period."

    scene e79
    with medium_dissolve

    menu:



        "[godg]" if evil:
            pass
        "I'm [playerName] [playerLastName], and you are?":

            pass
        "*Stay silent.*":


            lor "(Hmph, nothing to say, huh? This should be an open and shut case then.)"
            lor "(Only someone who's guilty would choose silence over.....)"
            lor "(.........)"
            lor "(.............)"
            lor "(..................)"
            lor "(Wait a minute....)"
            jump cor5

    lor "......."
    lor "..........."
    lor "..............."
    jump cor5

label cor5:

    scene lorrainesurprise
    with ffast_dissolve
    if not persistent.seen_lorrainesurprise:


        $ config.allow_skipping = False
        $ renpy.pause(6, hard=True)
        $ config.allow_skipping = True


        $ persistent.seen_lorrainesurprise = True
        $ renpy.save_persistent()
    else:



        pause 6

    scene e80
    with ffast_dissolve

    lor "!!!!!!!"
    lor "Wait a minute.....you-"
    lor "You.....you're.....[fatherName]'s son?"

    menu:
        "Yeah?":



            pass
        "That's right.":

            pass
        "How the hell do you know him?":

            pass
        "You know my old man? How?":

            pass

    scene e81
    with medium_dissolve

    lor "......."
    lor "This is... it's impossible."
    lor "How....how did you find us?? What happened?? Did you find your way back??"

    menu:
        "What?":




            scene e83
            with medium_dissolve

            lor "It's nothing, never mind. I shouldn't have said anything."
            lor "Just... forget I mentioned it. This is all so confusing."
            lor "I need to think about this. It changes everything."
            lor "......."
        "I'm here because my dad told me to come here. He said I needed to talk to Marnie.":


            scene e83
            with medium_dissolve

            lor "Marnie?"
            lor "Wait, of course.... Why else would you be here, in this house, after all."
            lor "We.....we need to keep this quiet. This is not something we can discuss openly."
            lor "If 'she' found out you're alive, then....."
            lor "............"
            lor "Just.....just know that there's more to this than you realize right now."
        "Okay, now I'm annoyed. Just what the hell is going on here?":


            scene e83
            with medium_dissolve

            lor "I wish I could explain, but it's not my place. You'll find out in time."
            lor "Just know that there's more to this than you realize right now."
            lor "......."


    lor "But, um....anyway....."
    lor "I'm Lorraine, it's nice to finally meet you [playerName]."
    lor "I just have one question for you, given the.......circumstances."
    lor "Now that you have seen me....."
    lor "........."
    lor "Are you.....attracted to me?"
    lor "Well, what I mean is....do you think I would make a suitable candidate?"

    scene e84
    with medium_dissolve
    $ gtdd = "{image=evil} Well, can't lie.....you got a nice ass."

    menu:
        mc ""
        "Suitable candidate for what exactly?":



            scene e85
            with medium_dissolve

            lor "For you, silly."
            lor "You really don't know anything yet, do you? That's actually kind of adorable."
            lor "Don't worry. Nobody expects you to understand just yet. When the time comes, it'll all make perfect sense."
        "How did this go from you calling the cops, to asking me if I find you attractive?":


            scene e85
            with medium_dissolve

            lor "Life's full of unexpected turns, isn't it? One moment it's all business, the next..."
            lor "Well, here I am, curious about what our mysterious guest thinks of me."
            lor "It's not every day someone like you comes along......not ever, actually."
            lor "So, I thought why not ask something a bit more... personal?"

        "[gtdd]" if evil:

            scene e85
            with medium_dissolve

            lor "Oh, you're quite forward, aren't you? But I'm not complaining."
            lor "I do put in the effort to keep it....'fruitful', I'd say. It's nice to know it's appreciated."
            lor "So, that's a yes on the attractiveness scale, I take it?"
            lor "You've certainly piqued my interest, [playerName]."

    scene e86
    with medium_dissolve

    lor "You know, I've always tried to keep myself in good shape. It's important to me."
    lor "I guess having skills and abilities matters too, right?"
    lor "Is there anything you'd like to see me do? Anything I could show you?"
    lor "I may be an older woman, but I do have a few tricks up my sleeve."

    scene e87
    with medium_dissolve

    lor "Just name it, and I'll give it a shot. I like to think I'm quite capable."
    lor "After all, it's not every day someone can actually see what I can do."
    mc "........"
    mc "............"
    lor "Go on, don't be shy. Ask away."
    mc "........."

    $ gdrt = "{image=evil} {image=sexaddict} You know, not gonna lie.....it WOULD be nice to get a better view of that ass of yours somehow."

    menu:
        "Well uh.....can you do a handstand?":




            scene e88
            with medium_dissolve

            lor "A handstand? That's child's play for me."
            lor "I used to be quite the gymnast back in the day. You might be surprised."
            lor "Give me just a moment, and I'll show you."

            scene e89
            with medium_dissolve


            lor "........."
            lor "You know what.....could you actually record this for me? My phone's on the counter over there."
            lor "I'm thinking of sending this to a personal trainer I've been chatting with online."
            lor "She's always asking for a showcase of my current fitness level, and this could be just the thing."
            lor "I won't take no for an answer. Just grab my phone over there, alright?"

            scene black
            with slowfade
            pause 2.0

            scene black
            with slowfade

            lor "Alright, here we go."
            lor "Just hit record and point it my way. I'll take care of the rest."
            lor "Are you ready?"

            menu:
                "I was born ready.":



                    pass
                "Hell yeah.":

                    pass
                "Yup, let's do it.":

                    pass
                "You sure this is a good angle?":


                    lor "Yes, that spot is perfect."
                    lor "Like I said, just stand there and hit record."
                    lor "Ready? Let's go!"

                    scene lorraineanim1
                    with ffade
                    pause
                    jump chi15

            lor "Make sure to get a good shot, will you?"
            lor "Let's go!"

            jump chi15
        "Can you dance?":



            scene e88
            with medium_dissolve

            lor "Dance? Oh no, I'm not the best dancer, unfortunately."
            lor "Me getting on the dance floor is a bad idea, trust me."
            lor "How about this though - I can do a handstand for you. I used to be quite the gymnast back in the day."
            lor "Give me just a moment, and I'll show you."

            scene e89
            with medium_dissolve


            lor "........."
            lor ".............."
            lor "You know what.....could you actually record this for me? My phone's on the counter over there."
            lor "I'm thinking of sending this to a personal trainer I've been chatting with online."
            lor "She's always asking for a showcase of my current fitness level, and this could be just the thing."
            lor "I won't take no for an answer. Just grab my phone over there, alright?"

            scene black
            with slowfade
            pause 2.0

            scene black
            with slowfade

            lor "Alright, here we go."
            lor "Just hit record and point it my way. I'll take care of the rest."
            lor "Are you ready?"

            menu:
                "I was born ready.":



                    pass
                "Hell yeah.":

                    pass
                "Yup, let's do it.":

                    pass
                "You sure this is a good angle?":


                    lor "Yes, that spot is perfect."
                    lor "Like I said, just stand there and hit record."
                    lor "Ready? Let's go!"

                    jump chi15

            lor "Make sure to get a good shot, will you?"
            lor "Let's go!"

            jump chi15


        "[gdrt]" if evil or sexaddict:

            scene e88
            with medium_dissolve

            lor "Oh boy, you don't let up do you?"
            lor "But, it's alright. You may be unique, but you're still a man. I get it."
            lor "How about this - I can do a handstand for you. I used to be quite the gymnast back in the day."
            lor "Give me just a moment, and I'll show you."

            scene e89
            with medium_dissolve


            lor "........."
            lor ".............."
            lor "You know what.....could you actually record this for me? My phone's on the counter over there."
            lor "I'm thinking of sending this to a personal trainer I've been chatting with online."
            lor "She's always asking for a showcase of my current fitness level, and this could be just the thing."
            lor "I won't take no for an answer. Just grab my phone over there, alright?"

            scene black
            with slowfade
            pause 2.0

            scene black
            with slowfade

            lor "Alright, here we go."
            lor "Just hit record and point it my way. I'll take care of the rest."
            lor "Are you ready?"

            menu:
                "I was born ready.":



                    pass
                "Hell yeah.":

                    pass
                "Yup, let's do it.":

                    pass
                "You sure this is a good angle?":


                    lor "Yes, that spot is perfect."
                    lor "Like I said, just stand there and hit record."
                    lor "Ready? Let's go!"

                    jump chi15

            lor "Make sure to get a good shot, will you?"
            lor "Let's go!"
            jump chi15


label chi15:

    $ upe55 = "{image=evil} {image=sexaddict} *Play some sexually explicit music to see if she will dance to it.*"

    scene black
    with slowfade

    pause 2.0

    scene lorraineyoga1
    with ffast_dissolve
    pause
    jump chi16

label chi16:
    menu:
        "*Continue.*":



            pass
        "*Keep watching.*":

            window hide
            pause
            jump chi16

    scene lorraineyoga2
    with ffast_dissolve
    pause
    jump chi17

label chi17:

    menu:
        "*Finish*":



            pass
        "*Keep watching.*":

            window hide
            pause
            jump chi17

        "[upe55]" if evil or sexaddict:

            $ lorrainerap = True

            stop music fadeout 2.0

            scene black
            with ffade
            scene lorraineyoga3
            with ffast_dissolve
            call godson_locked_cutscene ("gui/lorraineyoga3.webm", 62.0, "seen_lorraineyoga3") from _call_godson_locked_cutscene_5

    scene black
    with slowfade

    if evil:
        play music my_audio["think2evil"] loop fadein 2.0
    elif good or sexaddict:
        play music my_audio["think2"] loop fadein 2.0

    if lorrainerap:
        jump badlorraine

    jump goodlorraine

label badlorraine:

    scene e90
    with medium_dissolve
    $ gpe = "{image=evil} I'd like to see more ass next time."

    lor "So, what did you think? Not bad for someone who's not a professional athlete, huh?"
    lor "I've always believed in staying active and fit. It's important, don't you think?"
    lor "What's your impression? I'd love to know."

    menu:
        "You're definitely athletic. I'm impressed.":




            scene e93
            with medium_dissolve

            lor "Thank you! I do take my fitness seriously. It's good to know it shows."
            lor "Always nice to get a compliment from someone."
            lor "I'm glad you appreciated the effort."
        "Did you like the music?":


            scene e93
            with medium_dissolve

            lor "Oh...."
            lor "Well, those lyrics were....interesting to say the least, but it was fun!"
            lor "It's been a while since I've had someone to impress, and to dance for. Erm...."
        "Honestly, you're absolutely amazing.":


            $ memory_lorraine_praised = True
            $ show_tooltip(n=15)


            scene e93
            with medium_dissolve

            lor "Wow, thank you! That means a lot, especially under these... unique circumstances."
            lor "It's not often I get to showcase my skills like this."
            lor "Your praise is really encouraging."

        "[gpe]" if evil:

            scene e93
            with medium_dissolve

            lor "Oh boy, you never give up, do you?"
            lor "Is that all that's on your mind? Ass and tits?"
            lor "I do suppose I can't blame you though, given my current attire."
            lor "Perhaps next time, I can wear something a little less revealing, so I don't give off the wrong impression."

    scene e94
    with medium_dissolve

    lor "Anyway.....this has been fun, but I should probably get going and get ready."
    lor "It might be best if I leave first. You know, to avoid any....misunderstandings."
    lor "Maybe wait about ten minutes after I leave? Just so it doesn't look odd."
    lor "Especially considering my current state of undress."

    scene e95
    with medium_dissolve

    menu:
        mc ""
        "Technically, I still need to shower.":



            scene e96
            with medium_dissolve

            lor "Then you'll simply have to survive being a little less than fresh for another hour."
            lor "Trust me, it's far less suspicious than the two of us walking out of this bathroom together."
            lor "I'll go first. Count to sixty, then come out. The shower will still be there when the coast is clear."
        "Good idea. Wouldn't want to start any rumors.":


            scene e96
            with medium_dissolve

            lor "Rumors in this house spread faster than wildfire."
            lor "I appreciate you being considerate about this."
            lor "Alright, I'll make my exit now. Take care."
        "You embarrassed or something?":


            scene e96
            with medium_dissolve

            lor "Embarrassed? No of course not, silly."
            lor "It's not about embarrassment. It's about being sensible."
            lor "We wouldn't want to stir up any unnecessary drama or misunderstandings."
            lor "Think of it as me being cautious, not embarrassed, alright?"
            lor "I'll make my exit now. Take care and remember, wait ten minutes. Don't forget."
        "Hang on, didn't you lose something? Did you need help finding it?":


            lor "Oh that? Don't worry."
            lor "I actually remembered where I had last placed it, so I am aware of where it is."
            lor "Thank you for asking though, it's nice to be around someone who cares."

            scene e96
            with medium_dissolve

            lor "Anyway, this has been lovely, but we should depart from here."
            lor "Come find me later, alright?"
            lor "Be seeing you..."


    stop music fadeout 3.0

    scene black
    with slowfade

    play music my_audio["apartment4"] loop fadein 3.0

    pause 2.0

    scene e97
    with slowfade
    pause

    play sound my_audio["dooropen"] noloop

    scene e98
    with medium_dissolve

    mc "....."
    mc "........"
    jump clo2

label goodlorraine:

    scene e90
    with medium_dissolve
    $ gpe = "{image=evil} I'd like to see more ass next time."

    lor "So, what did you think? Not bad for someone who's not a professional athlete, huh?"
    lor "I've always believed in staying active and fit. It's important, don't you think?"
    lor "What's your impression? I'd love to know."

    menu:
        "You're definitely athletic. I'm impressed.":




            scene e93
            with medium_dissolve

            lor "Thank you! I do take my fitness seriously. It's good to know it shows."
            lor "Always nice to get a compliment from someone."
            lor "I'm glad you appreciated the effort."
        "I've seen better, but you've got potential.":


            scene e93
            with medium_dissolve

            lor "Oh, a tough critic, huh? Well, I appreciate the honesty."
            lor "I'll take 'potential' as a compliment. Always room for improvement."
            lor "It's been a while since I've had someone to impress."
        "Honestly, you're absolutely amazing.":

            $ memory_lorraine_praised = True
            $ show_tooltip(n=15)


            scene e93
            with medium_dissolve

            lor "Wow, thank you! That means a lot, especially under these... unique circumstances."
            lor "It's not often I get to showcase my skills like this."
            lor "Your praise is really encouraging."

        "[gpe]" if evil:

            scene e93
            with medium_dissolve

            lor "Oh boy, you never give up, do you?"
            lor "Is that all that's on your mind? Ass and tits?"
            lor "I do suppose I can't blame you though, given my current attire."
            lor "Perhaps next time, I can wear something a little less revealing, so I don't give off the wrong impression."

    scene e94
    with medium_dissolve

    lor "Anyway.....this has been fun, but I should probably get going and get ready."
    lor "It might be best if I leave first. You know, to avoid any....misunderstandings."
    lor "Maybe wait about ten minutes after I leave? Just so it doesn't look odd."
    lor "Especially considering my current state of undress."

    scene e95
    with medium_dissolve

    menu:
        mc ""
        "Technically, I still need to shower.":



            scene e96
            with medium_dissolve

            lor "Then you'll simply have to survive being a little less than fresh for another hour."
            lor "Trust me, it's far less suspicious than the two of us walking out of this bathroom together."
            lor "I'll go first. Count to sixty, then come out. The shower will still be there when the coast is clear."
        "Good idea. Wouldn't want to start any rumors.":


            scene e96
            with medium_dissolve

            lor "Rumors in this house spread faster than wildfire."
            lor "I appreciate you being considerate about this."
            lor "Alright, I'll make my exit now. Take care."
        "You embarrassed or something?":


            scene e96
            with medium_dissolve

            lor "Embarrassed? No of course not, silly."
            lor "It's not about embarrassment. It's about being sensible."
            lor "We wouldn't want to stir up any unnecessary drama or misunderstandings."
            lor "Think of it as me being cautious, not embarrassed, alright?"
            lor "I'll make my exit now. Take care and remember, wait ten minutes. Don't forget."
        "Hang on, didn't you lose something? Did you need help finding it?":


            lor "Oh that? Don't worry."
            lor "I actually remembered where I had last placed it, so I am aware of where it is."
            lor "Thank you for asking though, it's nice to be around someone who cares."

            scene e96
            with medium_dissolve

            lor "Anyway, this has been lovely, but we should depart from here."
            lor "Come find me later, alright?"
            lor "Be seeing you..."


    stop music fadeout 3.0

    scene black
    with slowfade

    pause 2.0

    scene e97
    with slowfade
    pause

    play sound my_audio["dooropen"] noloop

    scene e98
    with medium_dissolve

    mc "....."
    mc "........"
    jump clo2

label clo1:

    scene black
    with slowfade
    play sound my_audio["doorclose"] noloop
    pause 1.0

    scene e100
    with slowfade
    pause
    jump clo3

label clo2:

    play sound my_audio["doorclose"] noloop

    scene e100
    with medium_dissolve
    pause
    jump clo3

label clo3:

    play music my_audio["apartment4"] loop fadein 3.0
    scene e101
    with medium_dissolve
    pause

    unk "......"
    unk "........."
    unk "............."
    unk "Hey! Who are you?"

    scene e101_1
    with medium_dissolve

    unk "Oh, shit... please don't tell me you're another fan who figured out where I live."
    unk "Look, I don't know how you got inside, but this is seriously creepy. You need to leave before I call somebody."
    unk "And why the hell were you sneaking out of the bathroom like that?"
    jump creepy1

label creepy1:

    scene a143
    with medium_dissolve

    yun "........"
    yun "............"
    yun "..............."
    yun ".................."
    mc "............."

    $ yikes = "{image=evil} {image=superevil} Yikes."

    menu:
        "What?":



            pass
        "Something wrong?":

            pass
        "You're staring at me.":

            pass
        "What's the problem?":

            pass

    scene mcyuni1
    with medium_dissolve
    if not persistent.seen_yuni1:


        $ config.allow_skipping = False
        $ renpy.pause(13.5, hard=True)
        $ config.allow_skipping = True


        $ persistent.seen_yuni1 = True
        $ renpy.save_persistent()
    else:



        pause 13.5

    menu:
        "Ooookay....anyway, I'm not a stalker. Marnie and Henry said I could stay here.":




            scene mcyuni2
            with ffast_dissolve
            if not persistent.seen_yuni2:


                $ config.allow_skipping = False
                $ renpy.pause(15, hard=True)
                $ config.allow_skipping = True


                $ persistent.seen_yuni2 = True
                $ renpy.save_persistent()
            else:



                pause 15
        "I didn't break in. I spoke to your parents last night, and they're letting me stay here.":


            scene mcyuni2
            with ffast_dissolve

            if not persistent.seen_yuni2:


                $ config.allow_skipping = False
                $ renpy.pause(15, hard=True)
                $ config.allow_skipping = True


                $ persistent.seen_yuni2 = True
                $ renpy.save_persistent()
            else:



                pause 15
        "Well I was told that I could stay here by your parents.":


            scene mcyuni2
            with ffast_dissolve
            if not persistent.seen_yuni2:


                $ config.allow_skipping = False
                $ renpy.pause(15, hard=True)
                $ config.allow_skipping = True


                $ persistent.seen_yuni2 = True
                $ renpy.save_persistent()
            else:



                pause 15

    menu:
        "Ok stop. How old are you?":





            scene mcyuni4
            with ffast_dissolve
            if not persistent.seen_yuni4:


                $ config.allow_skipping = False
                $ renpy.pause(14.15, hard=True)
                $ config.allow_skipping = True


                $ persistent.seen_yuni4 = True
                $ renpy.save_persistent()
            else:



                pause 14.15
            jump yikes
        "*Fuck it, play into it.* I mean, we could take this conversation into you're room, alone, just the two of us.":


            $ memory_yuni_first_impression = True
            $ show_tooltip(n=18)

            scene mcyuni3
            with ffast_dissolve
            if not persistent.seen_yuni3:


                $ config.allow_skipping = False
                $ renpy.pause(14.10, hard=True)
                $ config.allow_skipping = True


                $ persistent.seen_yuni3 = True
                $ renpy.save_persistent()
            else:



                pause 14.10
            jump yikes


label yikes:

    menu:



        "I'm gonna need to see some identification." if not superevil:

            scene mcyuni6
            with ffast_dissolve

            if not persistent.seen_yuni6:


                $ config.allow_skipping = False
                $ renpy.pause(14.12, hard=True)
                $ config.allow_skipping = True


                $ persistent.seen_yuni6 = True
                $ renpy.save_persistent()
            else:



                pause 14.12
            jump anyway1


        "I think I get the picture, let's move on please?" if not (superevil and yikes_choices_locked):

            if superevil:
                $ yikes_choices_locked = True
                voice my_audio["238"]
                nar "NO!"
                voice my_audio["239"]
                nar "Open your eyes. Can you not see it?"
                voice my_audio["240"]
                nar "Look harder. Do you remember what we thought about when we were meeting Mommy?"
                jump yikes
            else:

                scene x49
                with medium_dissolve

                yun "Aww, already? I was having fun watching you pretend you weren't enjoying all the compliments."
                yun "Fine, fine. You're hot, you understand that you're hot, and I will graciously stop reminding you... for now."
                jump anyway1
        "Yikes.":



            $ yikes_choices_locked = False

            scene mcyuni5
            with ffast_dissolve

            if not persistent.seen_yuni5:

                $ config.allow_skipping = False
                $ renpy.pause(8.5, hard=True)
                $ config.allow_skipping = True

                $ persistent.seen_yuni5 = True
                $ renpy.save_persistent()
            else:


                pause 8.5

            menu:


                "Can you act really cute for me?" if not superevil:

                    scene mcyuni16
                    with ffast_dissolve
                    if not persistent.seen_yuni16:


                        $ config.allow_skipping = False
                        $ renpy.pause(14.3, hard=True)
                        $ config.allow_skipping = True


                        $ persistent.seen_yuni16 = True
                        $ renpy.save_persistent()
                    else:



                        pause 14.3

                    voice my_audio["683"]
                    nar "ARE YOU FUCKING SERIOUS!? You asked her to act cute, and she responded with something that could get you investigated in three separate jurisdictions! WORLDWIDE!"
                    voice my_audio["685"]
                    nar "And if you're still wondering where the hell she was going with that, allow your inner conscience to translate. Yuni here apparently has an incredibly dark sense of humor, and she knows exactly how young and innocent she looks."
                    voice my_audio["685-1"]
                    nar "She deliberately uses that sweet little face to make the most wildly absurd jokes imaginable. Had you encouraged her, she was absolutely working her way toward something involving, a suspicious van, yanking her off the street, locking her in a basement......need I say more?"
                    voice my_audio["686"]
                    nar "And look at that fucking grin! Oh, this 'little girl' is dangerous. Cute enough to lower your guard, crazy enough to turn an ordinary afternoon into a nationally televised manhunt."
                    voice my_audio["687"]
                    nar "Listen to me very carefully. Don't say anything! Not one fucking word! Don't question her, don't ask what that was, and don't even blink in a curious manner! Because I have a horrible feeling that if you challenge her, she's only going to push harder... and then she's going to say the forbidden words. Whatever you do, remain silent! Smile, nod, and let this moment die before the FBI starts circling the house!"

                    menu:
                        "*Don't respond to that.*":


                            scene x49
                            with medium_dissolve

                            yun "Oh come on, no response? Really?"
                            yun "Hah! Jesus dude I was just kidding! You don't have to get all worried all of a sudden!"
                            yun "Thought I have to admit, that was fun!"
                            jump anyway1

                "Fine, I'll believe you." if not superevil:

                    scene x49
                    with medium_dissolve

                    yun "You'll believe me? How generous of you."
                    yun "You should, though. I happen to have excellent taste, and these eyes have never lied to me before."

                    jump anyway1
                "That's not what I was saying 'yikes' to, but ok.":


                    $ yikes2 = "{image=superevil} *Stand there breathing deeply while staring at her.*"

                    scene mcyuni7
                    with ffast_dissolve

                    if not persistent.seen_yuni7:


                        $ config.allow_skipping = False
                        $ renpy.pause(30, hard=True)
                        $ config.allow_skipping = True


                        $ persistent.seen_yuni7 = True
                        $ renpy.save_persistent()
                    else:



                        pause 30

                    menu:



                        "Fall in love wit-....WHAT THE HELL WAS THAT!?" if not superevil:

                            scene x49
                            with medium_dissolve

                            yun "Hehe! Got your attention, didn't I?"
                            yun "You were getting way too confident, so I thought I'd give you something to stumble over."
                            yun "Relax, I was only teasing you... unless you're admitting that it worked?"
                            jump anyway1

                        "Relax? I am relaxed hahaha!" if not superevil:

                            scene x49
                            with medium_dissolve

                            yun "Aww, come on don't laugh! I was only having a little fun."
                            yun "Besides, you were the one staring. I just gave you something worth staring at."
                            yun "If that's your idea of me being mean, you're going to have a very difficult time around me."
                            jump anyway1

                        "Did you really need to do that?" if not superevil:

                            scene x49
                            with medium_dissolve

                            yun "Need to? No. But the look on your face made it completely worth it."
                            yun "Besides, you weren't taking me seriously. I had to make sure I had your full attention."
                            yun "And judging by the way you're looking at me now... I'd say it worked perfectly."
                            jump anyway1

                        "[yikes2]" if superevil:

                            voice my_audio["241"]
                            nar "You say nothing. You simply stand there, breathing slowly, your eyes fixed upon her as though looking away would mean missing something important."
                            voice my_audio["242"]
                            nar "She is almost painfully cute... those soft cheeks, those bright eyes, that sweet little smile. The very picture of an innocent young Asian beauty. Carefully designed to make a man lower his guard."
                            voice my_audio["244"]
                            nar "Still, you cannot look away. She isn't Mommy, no one could ever be Mommy. But she carries a strangely familiar pull... and for the moment, standing here and admiring her feels exactly right."
                            voice my_audio["245"]
                            nar "And she is watching you too. Not with the vacant stare of some unnatural creature, but with focused, very human curiosity... studying your silence as carefully as you study her smile."
                            voice my_audio["246"]
                            nar "As far as you can tell, there is no spell clouding your thoughts and no unseen hand controlling you. She and Mommy are flesh and blood, and whatever you feel for them is coming from inside you. After all, this voice in your head isn't an intruder... it is you."
                            voice my_audio["247"]
                            nar "And Yuni is no puppet either. Whatever secrets she may be keeping, the woman standing before you has a mind, a will, and intentions entirely her own. There is nothing lurking behind her eyes or pulling invisible strings. She is simply herself... and your fascination with her is simply you."

                            scene mcyuni8
                            with ffast_dissolve
                            if not persistent.seen_mcyuni8:


                                $ config.allow_skipping = False
                                $ renpy.pause(14, hard=True)
                                $ config.allow_skipping = True


                                $ persistent.seen_mcyuni8 = True
                                $ renpy.save_persistent()
                            else:



                                pause 14
                            jump yuniquest

label yuniquest:

    menu:
        "She has.":



            pass

        "Mommy? Do you mean Marnie? Your mother?" if not yunimom1:

            scene mcyuni9
            with ffast_dissolve
            if not persistent.seen_mcyuni9:


                $ config.allow_skipping = False
                $ renpy.pause(15, hard=True)
                $ config.allow_skipping = True


                $ persistent.seen_mcyuni9 = True
                $ renpy.save_persistent()
            else:



                pause 15

            voice my_audio["248"]
            nar "Huh... I see. When Yuni wants to appear especially cute, she softens her voice and slips into a sweeter, more exaggerated version of her natural accent. A deliberate little performance, and a remarkably effective one."
            $ yunimom1 = True
            jump yuniquest
        "Yes, she has.":

            pass
        "Yes.":

            pass

    scene mcyuni10
    with ffast_dissolve
    if not persistent.seen_mcyuni10:


        $ config.allow_skipping = False
        $ renpy.pause(14.5, hard=True)
        $ config.allow_skipping = True


        $ persistent.seen_mcyuni10 = True
        $ renpy.save_persistent()
    else:



        pause 14.5


    menu:
        "I did. But, are you also a, 'Mommy'?":



            pass
        "Is...your name....Mommy, too?":

            pass
        "I did fuck Mommy, and now I want to fuck my other Mommy. Are you my other Mommy?":

            pass


    scene mcyuni11
    with ffast_dissolve
    if not persistent.seen_mcyuni11:


        $ config.allow_skipping = False
        $ renpy.pause(14.5, hard=True)
        $ config.allow_skipping = True


        $ persistent.seen_mcyuni11 = True
        $ renpy.save_persistent()
    else:



        pause 14.5

    voice my_audio["249"]
    nar "There it is again....'understand'. I wonder why they both say this word so often to you?"
    $ good2 = "{image=good} *TRY TO RESIST YOUR OWN FEELINGS!* I...thought your name was Yuni."
    jump yuni_princess_menu

label yuni_princess_menu:

    menu:



        "[good2]" if not resisted_yuni_once:

            $ resisted_yuni_once = True
            $ memory_yuni_resisted = True
            $ show_tooltip(n=19)


            scene mcyuni12
            with ffast_dissolve

            if not persistent.seen_mcyuni12:


                $ config.allow_skipping = False
                $ renpy.pause(13, hard=True)
                $ config.allow_skipping = True


                $ persistent.seen_mcyuni12 = True
                $ renpy.save_persistent()
            else:


                pause 13

            jump yuni_princess_menu
        "Yes, Princess.":


            pass
        "Yes, Princess.":


            pass

    scene mcyuni13
    with ffast_dissolve
    if not persistent.seen_mcyuni13:


        $ config.allow_skipping = False
        $ renpy.pause(13, hard=True)
        $ config.allow_skipping = True


        $ persistent.seen_mcyuni13 = True
        $ renpy.save_persistent()
    else:


        pause 13

    menu:
        mc ""
        "I would do anything for my little Princess.":


            pass
        "I would do anything for my little Princess.":
            pass
        "I would do anything for my little Princess.":
            pass
        "I would do anything for my little Princess.":
            pass

    scene mcyuni14
    with ffast_dissolve
    if not persistent.seen_mcyuni14:


        $ config.allow_skipping = False
        $ renpy.pause(15, hard=True)
        $ config.allow_skipping = True


        $ persistent.seen_mcyuni14 = True
        $ renpy.save_persistent()
    else:


        pause 15

    menu:
        "I understand. I...love you, Princess.":



            pass
        "I understand. I...love you, Princess.":

            pass
        "I understand. I...love you, Princess.":

            pass
        "I understand. I...love you, Princess.":

            pass


    scene mcyuni15
    with ffast_dissolve
    if not persistent.seen_mcyuni15:


        $ config.allow_skipping = False
        $ renpy.pause(14, hard=True)
        $ config.allow_skipping = True


        $ persistent.seen_mcyuni15 = True
        $ renpy.save_persistent()
    else:


        pause 14
    stop music fadeout 2.0
    scene black
    with slowfade
    play music my_audio["thinking6"] loop fadein 2.0

    pause 2.0

    scene x50
    with slowfade

    voice my_audio["252"]
    nar "Now you understand everything, or at least, everything that truly matters. Mommy was never working alone."
    voice my_audio["253"]
    nar "The other woman at her side was Princess. The young woman you once knew as Yuni is Mommy's own sister... and she has been part of this from the beginning."
    voice my_audio["254"]
    nar "Mommy and Princess. Mommy first, always. Then Princess. Two extraordinary women who have somehow chosen to make you part of their lives."
    voice my_audio["255"]
    nar "Princess sent you away with a promise, not a rejection. She had several things to handle before the two of you could be together properly."
    voice my_audio["256"]
    nar "One of those loose ends was Kyle, the boyfriend she intended to leave behind. Once everything was settled, she told you to return to her room tonight so the two of you could discuss what came next."
    voice my_audio["257"]
    nar "And so you returned to your room, lowered your head, pressed your hands together, and waited. There was nowhere else you needed to be."

    scene x51
    with slow_dissolve

    voice my_audio["258"]
    nar "The hours pass unnoticed. Daylight slowly drains from the room, replaced by the darkness of evening, yet you remain exactly where you were."
    voice my_audio["259"]
    nar "Your thoughts belong to only two women now. Mommy first. Always Mommy. Then Princess."
    voice my_audio["260"]
    nar "Princess... with her soft cheeks, bright eyes, playful voice, and that impossibly cute smile. The sweet little Asian beauty you once believed could only exist in someone else's fantasy."
    voice my_audio["261"]
    nar "And Mommy... breathtaking, commanding, effortlessly sensual. A woman whose beauty draws you in while that deliciously cruel smile reminds you exactly who stands above everyone else. Heh......that fucking hott, big-titted sexy BITCH!"
    voice my_audio["262"]
    nar "You never imagined women like them would enter your life. Now both of them want you with an intensity you once believed no woman ever could."
    voice my_audio["263"]
    nar "And there is no spell forcing these feelings upon you. No invisible hand directing your choices. Every thought, every desire, and every decision that brought you here belongs entirely to you."
    voice my_audio["264"]
    nar "You are not being controlled. You have simply discovered where you want to be... and who you want to belong beside."
    voice my_audio["335"]
    nar "It should be around the time Princess wanted you to return to her room. After waiting so patiently, the moment has finally arrived."
    voice my_audio["336"]
    nar "Then a sweet voice drifts through the hallway. 'Baby? Baby, where are you? Baby?' You recognize Princess immediately. She has come looking for you."
    voice my_audio["337"]
    nar "Good God, that impression was fucking dreadful. Thank heavens only you can hear me, because I sounded less like Princess and more like a haunted kettle trying to seduce a microwave."
    voice my_audio["338"]
    nar "Anyway! There is no reason to keep her waiting. You rise, stretch the stiffness from your legs, and step into the hallway, following her voice toward Princess's room."

    scene black
    with slowfade
    stop music fadeout 2.0

    pause 2.0

    scene black
    with slowfade

    voice my_audio["339"]
    nar "The moment you step into her room, Princess grabs you by the front of your boxers and pulls you close, smiling up at you as though she has been waiting all day for this exact moment."
    voice my_audio["340"]
    nar "She gives you that impossibly cute little grin and asks, 'Did you miss Princess, baby?' The way your arms immediately circle her waist provides all the answer she needs."
    voice my_audio["341"]
    nar "Princess giggles, takes hold of your hand, and playfully pulls you toward the bed. She tumbles backward onto the mattress, snatches up a pillow, and hides behind it like some soft, remarkably ineffective shield."
    voice my_audio["342"]
    nar "Princess keeps the pillow pressed firmly between you like a playful little shield. Rather than taking it away, you lean over the top and kiss her forehead. She giggles, raises the pillow to block you again, and you continue searching for another opening to steal a kiss."

    scene yunisuperevil
    with ffade
    call godson_locked_cutscene ("gui/yunisuperevil.webm", 298.0, "seen_yunisuperevil") from _call_godson_locked_cutscene_6

    $ unlock_gallery_scene("princess")

    scene black
    pause 2.0
    play music my_audio["apartment4"] loop fadein 2.0

    scene x52
    with slowfade

    voice my_audio["343"]
    nar "A short while later, fully dressed and no longer wandering around in your underwear, you sit on the stairs outside Princess's room with your head lowered and your hands clasped. The house remains quiet; none of the party guests have arrived yet."
    voice my_audio["344"]
    nar "Princess made it perfectly clear that she would rather remain beside you, but she had already promised to meet her friends at their house, help them choose what to wear, and get ready for the party together. She promised she would return with them."
    voice my_audio["345"]
    nar "Before leaving, Princess told you everything she knew. Every secret, every warning, every piece of history, and every detail she understood about your awakening power and the role now waiting for you."
    voice my_audio["346"]
    nar "She told you because she truly loves you. Not merely the power inside you, but the real you. She loves the uncertain, imperfect, very real person beneath all of it."
    voice my_audio["347"]
    nar "Princess refused to hide anything from you, even knowing that such honesty might upset Mommy. So here you are, alone with enough information to rearrange your entire understanding of reality. How about we go over everything she told you?"

label princess_truth_menu:

    menu:



        "Who am I, really?" if not asked_who_am_i:

            $ asked_who_am_i = True

            voice my_audio["348"]
            nar "According to Princess, the answer is every bit as ridiculous as it sounds: you are Santa Claus. Or, more accurately, the man who has inherited the role and power of Santa Claus."
            voice my_audio["349"]
            nar "The previous Santa is believed to be dead. The story Princess heard claims he fell from a roof and then simply disappeared. Centuries of Christmas mythology, apparently defeated by inadequate workplace safety."
            voice my_audio["350"]
            nar "His disappearance left the role vacant, but the power itself did not vanish. Somehow, that power found its way to you and has only recently begun awakening."
            voice my_audio["351"]
            nar "Mommy already believed you were the new Santa before Princess witnessed your abilities. Princess doesn't know how Mommy discovered that, or why she was so certain, but she trusted her sister's judgment."
            voice my_audio["352"]
            nar "Before you appeared, Mommy and Princess had been preparing to search for the new Santa themselves. They knew someone had inherited the role; they simply didn't know where to begin looking."
            voice my_audio["354"]
            nar "They refused to begin that search until Princess turned eighteen and became a legal adult. Whatever else may be said about their plan, that boundary was absolute."
            voice my_audio["355"]
            nar "Princess had also prepared herself for the deeply unfortunate possibility that Santa would be some ancient, overweight man with a beard large enough to conceal several woodland creatures."
            voice my_audio["356"]
            nar "Discovering that Santa was actually a handsome twenty-one-year-old man close to her own age was, in her words, a considerable improvement. Her relief was not particularly subtle."
            voice my_audio["357"]
            nar "Mommy's certainty may have brought Princess to you, but the power settled the question. Candy, snow, miniature reindeer. Ordinary men do not accidentally produce Christmas miracles from empty hands."
            voice my_audio["358"]
            nar "So that is who you are: the new Santa Claus. Why the power selected you, and how Mommy knew before anyone else, remain questions Princess cannot answer."

            jump princess_truth_menu

        "Who are the women in this house?" if not asked_who_are_they:

            $ asked_who_are_they = True

            voice my_audio["359"]
            nar "The women in this family are Amazons. Not metaphorically, not ceremonially, and certainly not because they joined an unusually aggressive fitness club. They are actual Amazons."
            voice my_audio["360"]
            nar "Their homeland exists within another reality entirely, a world of ancient customs, stone fortresses, blades, old laws, and a way of life that would appear medieval beside this one."
            voice my_audio["361"]
            nar "They are still real women with minds, emotions, and choices entirely their own. They are not spirits, puppets, disguised entities, or vessels controlled by something hiding behind their eyes."
            voice my_audio["362"]
            nar "Martha was the first member of this family to leave that world and build a life here."
            voice my_audio["363"]
            nar "She never explained why she abandoned the island. Whatever happened there was enough to keep her away permanently, and she has shown no desire to return."
            voice my_audio["364"]
            nar "Martha later had two daughters: Marnie and Lorraine. Both inherited their mother's Amazon blood, even though much of their lives unfolded away from the island."
            voice my_audio["365"]
            nar "Marnie eventually had two daughters of her own: Jennifer and Yuni, the women you now know as Mommy and Princess."
            voice my_audio["366"]
            nar "That makes Martha their grandmother, Marnie their mother, and Lorraine their aunt. One family stretching between two completely different realities."
            voice my_audio["367"]
            nar "Travel between those realities is possible, and the women of this family have occasionally returned to the island for personal, political, or family reasons."
            voice my_audio["368"]
            nar "Marnie hasn't returned in roughly ten years. Whatever connection she once maintained with the island has grown distant."
            voice my_audio["369"]
            nar "Martha has never gone back at all. She left once, built another life, and apparently intends to die before willingly setting foot there again."
            voice my_audio["370"]
            nar "Lorraine has returned several times, though Princess doesn't know every reason behind those visits or everything Lorraine may have learned there."
            voice my_audio["371"]
            nar "Mommy has visited far more frequently, especially recently. She has spent considerable time moving between this world and the island, though even Princess doesn't know everything she does while she's there."
            voice my_audio["372"]
            nar "Princess has also seen the island herself. She understands its customs, its people, and enough of its expectations to know precisely what kind of future she wants."
            voice my_audio["373"]
            nar "So the women in this house aren't merely an unusual family with several carefully guarded secrets. They are one branch of an Amazon bloodline living quietly inside an ordinary home. Here, in America."

            jump princess_truth_menu

        "What happened to my father? Why is he in a coma?" if not asked_where_father:

            $ asked_where_father = True

            voice my_audio["374"]
            nar "Unfortunately, that is the one question Princess cannot answer. She knows where your father is, but she does not know exactly what happened to him or why he cannot wake up."
            voice my_audio["375"]
            nar "She is certain that his condition is not an ordinary coma. His body remains alive, yet something appears to be keeping his mind trapped somewhere no doctor has been able to reach."
            voice my_audio["376"]
            nar "Everything Princess has learned suggests that it began after your father became involved with the island and its people. Whether it was a curse, some form of magic, or the consequence of something he did there remains unknown to her."
            voice my_audio["377"]
            nar "Mommy may know more than she has admitted, but even Princess was kept outside that particular secret. Whatever happened to your father, someone has gone to considerable effort to keep the truth buried."
            voice my_audio["378"]
            nar "So Princess can tell you what you are and where the women of this family came from, but she cannot tell you who, or what, placed your father in that coma, nor how you are supposed to wake him."

            jump princess_truth_menu

        "Continue." if asked_who_am_i and asked_who_are_they and asked_where_father:

            scene x53
            with medium_dissolve

            voice my_audio["379"]
            nar "Three questions answered, several new mysteries created. Not the most favourable exchange, but at least we are making progress."
            voice my_audio["380"]
            nar "Before we continue, however, how about we test out our new power? Try to summon something with your hand."

            menu:
                "*Test out your new power. Try to summon something with your hand.*":




                    scene mcsummon1
                    with ffast_dissolve
                    if not persistent.seen_mcsummon1:


                        $ config.allow_skipping = False
                        $ renpy.pause(14, hard=True)
                        $ config.allow_skipping = True


                        $ persistent.seen_mcsummon1 = True
                        $ renpy.save_persistent()
                    else:


                        pause 14

                    voice my_audio["381"]
                    nar "Well... that was lovely. A charming little snow globe, complete with its own village and everything."
                    voice my_audio["382"]
                    nar "Unfortunately, unless we are attacked by an unusually aggressive collector of Christmas decorations, it is not going to offer much protection."
                    voice my_audio["383"]
                    nar "Try summoning something a little more practical this time. Something capable of defending us... like a sword."

                    scene mcsummon2
                    with ffast_dissolve
                    if not persistent.seen_mcsummon2:


                        $ config.allow_skipping = False
                        $ renpy.pause(14, hard=True)
                        $ config.allow_skipping = True


                        $ persistent.seen_mcsummon2 = True
                        $ renpy.save_persistent()
                    else:


                        pause 14

                    voice my_audio["384"]
                    nar "I see. So we can summon almost anything we imagine, but whatever appears will inevitably be dragged through Christmas first. Interesting."
                    voice my_audio["385"]
                    nar "A snow globe was predictable. A sword decorated like the personal weapon of Father Christmas himself confirms that the festive theme is apparently mandatory."
                    voice my_audio["386"]
                    nar "What we do not know is how many times we can summon something, how much power each creation requires, or what happens when that power runs out."
                    voice my_audio["387"]
                    nar "Perhaps it gradually returns. Perhaps we need to sleep it off. Perhaps we collapse face-first onto the floor. Santa neglected to leave us an instruction manual, so let us stop wasting magic before we discover the answer unpleasantly."
                    jump lastquestion
                "*Refuse to test your power.*":


                    voice my_audio["388"]
                    nar "Refusing to test our mysterious new power, are we? That is an unexpected display of restraint."
                    voice my_audio["389"]
                    nar "Perhaps you simply need more time to process everything Princess told you... or perhaps some stubborn little piece of you is attempting to turn over a new leaf and become a good man again."
                    voice my_audio["390"]
                    nar "Adorable. Whether this is wisdom, fear, or the beginning of an inconvenient moral recovery, we can examine it later. For now, let us continue with the questions."
                    jump lastquestion


label lastquestion:

    scene x52
    with medium_dissolve

    voice my_audio["391"]
    nar "Unfortunately, the party guests will begin arriving soon, which leaves us time for only one more question, though perhaps the most important one of all. What exactly do the Amazons have to do with Santa Claus?"
    voice my_audio["392"]
    nar "Princess explained that Amazons are raised to hate men. They are taught that men bring war, conquest, betrayal, and destruction wherever they go, and their Queen personally ensures that every generation learns that lesson."
    voice my_audio["393"]
    nar "How an island inhabited entirely by women continues producing new Amazons without interacting with men is an excellent question. Princess never reached that portion of the explanation, so the reproductive logistics shall remain one of today's many disturbing mysteries."
    voice my_audio["394"]
    nar "There is, however, one exception. Santa Claus is the only man Amazons are taught not merely to tolerate, but to love. Santa is meant to be pure of heart, a man who gives without demanding, brings joy instead of suffering, and possesses great power without using it to rule others."
    voice my_audio["395"]
    nar "Every Mrs. Claus has therefore been an Amazon personally chosen by Santa Claus."
    voice my_audio["396"]
    nar "Amazons possess ordinary lifespans, while Santa may live for centuries. When one Mrs. Claus eventually dies, Santa selects another Amazon to stand beside him."
    voice my_audio["397"]
    nar "Princess has dreamed all her life of entering Santa's magical world and becoming the next Mrs. Claus... and now that you are Santa, her greatest dream is suddenly within reach."
    voice my_audio["398"]
    nar "Princess was also remarkably candid about Amazon biology. Their hormones run hot, their desires are intense, and being raised to adore precisely one man does very little to encourage restraint when that man finally appears."
    voice my_audio["399"]
    nar "Whenever a Mrs. Claus dies and Santa returns to the island to choose her successor, his arrival becomes one of the greatest events in Amazon culture. Every eligible adult Amazon who wishes to participate is given an opportunity to capture his attention."
    voice my_audio["400"]
    nar "The official ceremony is known as the Yuletide Choosing. Judging by Princess's description, however, the Great Festive Fuckening would be substantially more accurate, if somewhat less suitable for ceremonial banners."
    voice my_audio["401"]
    nar "There are celebrations, competitions, displays of strength, and an extraordinary amount of fucking. An island filled with passionate warrior women competing for the only man they were raised to love is apparently not known for subtlety."
    voice my_audio["402"]
    nar "When the festivities finally end, or whenever Santa's balls are finally drained, Santa chooses one Amazon to leave the island, enter his magical world, and become the next Mrs. Claus. Only one woman can receive that title."
    voice my_audio["402_1"]
    nar "According to the surviving legends, every Santa who arrived for the Yuletide Choosing, or the Great Festive Fuckening, was some elderly, overweight bastard with an enormous white beard and a face that no amount of Christmas magic could rescue."
    voice my_audio["402_2"]
    nar "Amazons may have little experience with men, but they can still recognise when one is not particularly attractive. They still lined up to fuck him until he couldn't stand, of course. He was Santa."
    voice my_audio["402_3"]
    nar "Which makes one wonder what might happen when a young, handsome man like you arrives instead. Quite a sight, I imagine... and possibly an island-wide public safety emergency."
    voice my_audio["403"]
    nar "That last detail led Princess to mention something important. Mommy always knew that becoming Mrs. Claus was Princess's greatest dream, yet she still helped Princess prepare to search for Santa."
    voice my_audio["404"]
    nar "Since only one Mrs. Claus can exist, Princess believes Mommy never intended to compete with her for the position. Otherwise, helping her younger sister find Santa would have made remarkably little sense."
    voice my_audio["405"]
    nar "Princess admits she could be wrong, but she believes Mommy desires a different title entirely. With her frequent visits to the island and growing interest in its affairs, Princess suspects Mommy intends to become Queen of the Amazons."
    voice my_audio["406"]
    nar "Side note. I should mention that I would very much enjoy a trip to the island, strictly to observe this Great Festive Fuckening from a scholarly distance, of course. Fortunately for us, good or otherwise, our eyes belong to only two women: Mommy and Princess. Perhaps in another life."
    voice my_audio["407"]
    nar "But hold on. We are not finished. Somehow, Princess's explanation becomes even more interesting."
    voice my_audio["408"]
    nar "According to her, nearly eighty-five percent of Amazons develop remarkably exaggerated curves: enormous breasts, broad hips, thick thighs, and backsides that appear to have been designed with absolutely no respect for structural moderation."
    voice my_audio["409"]
    nar "Marnie and Mommy are particularly obvious examples. Others, such as Princess and Lorraine, are less top-heavy but still possess some of the features, and natural strength associated with their Amazon blood."
    voice my_audio["410"]
    nar "Amazon legend claims these features developed as a battlefield advantage. Although their island rarely becomes involved in conventional wars, their bodies supposedly provide a rather unique defence whenever male soldiers are foolish enough to confront them."
    voice my_audio["411"]
    nar "Imagine charging toward an enemy warrior, prepared to strike, only to discover that she possesses breasts large enough to disrupt your concentration. Rage becomes confusion, confidence becomes hesitation, and the entire battle plan suffers a sudden complication."
    voice my_audio["412"]
    nar "Whether this is evolution, ancient magic, or centuries of Amazons flattering themselves remains unclear. Still, if distraction truly qualifies as a weapon, Marnie and Mommy could probably stop an invading army without ever drawing a blade."

    scene black
    play sound my_audio["doorbell"] noloop
    pause 1.0

    voice my_audio["413"]
    nar "And there it is. The doorbell. A mercifully ordinary sound after everything we have learned today."
    voice my_audio["414"]
    nar "That about wraps up our little investigation for now. It appears the first guest has finally arrived."
    voice my_audio["415"]
    nar "Let us head downstairs, greet them, and see who has come to join the party. Try to look normal, and perhaps avoid immediately discussing Amazon breasts, magical swords, or the Great Festive Fuckening."
    jump party1






label anyway1:

    scene x49
    with medium_dissolve

    yun "Hehe!"
    yun "Alright, you'll do!"
    yun "There's something in my room I could use your help with. Don't bother asking what! It'll make more sense when you see it."
    yun "Come on. Follow me, and try not to make this any more complicated than it needs to be."

    menu:
        mc ""
        "Sure. What do you need help with?":



            yun "Good. I knew you looked useful."
            yun "Come on, then. I'll explain everything once we're inside."
            yun "And try not to look too shocked when you see what I'm working with."
            jump yunibedroom
        "'You'll do?'. What exactly do you need help with?":


            yun "Relax. I'm not asking you to bury a body."
            yun "I need another set of hands, someone behind a camera, and preferably someone who knows more about music than I do."
            yun "Come inside and I'll give you the full explanation. Then you can decide whether you're actually useful."
            jump yunibedroom
        "No, thanks. I have other things I need to do.":


            yun "Seriously? Fine, then."
            yun "I'm not going to stand here begging some random guy to help me."
            yun "Do you even know how many people would kill for the chance to work with me?"
            yun "I can find somebody else in five minutes."
            yun "Somebody who won't stand in my doorway acting like I'm asking for some huge favor."
            yun "So, if you're not coming in, move. You're blocking the hallway."

            menu:
                mc ""
                "You could've just accepted the answer without being disrespectful.":



                    yun "And you could've just said no without standing there judging me."
                    yun "Whatever. Go do whatever was apparently more important."
                    yun "I'll find someone else."
                    pass
                "Alright, fine. I said no. You don't have to throw a tantrum.":


                    yun "I'm not throwing a tantrum."
                    yun "I'm just telling you that I don't need you."
                    yun "Now, goodbye."
                    pass
                "Okay. Good luck finding somebody else.":


                    yun "Trust me, I won't need luck."
                    yun "I've got thousands of people who'd say yes before I finished asking."
                    yun "See you around, I guess."
                    pass

            $ yuni_video_refused = True
            $ yuni_video_failed = False
            $ yuni_video_completed = False
            $ supergood_refused_yuni = True
            $ memory_yuni_video_refused = True
            $ show_tooltip(n=22)

            jump after_yuni_refusal

label yunibedroom:
    stop music fadeout 2.0
    stop music2 fadeout 2.0

    scene black
    with slowfade
    play music my_audio["yuniroom1"] loop fadein 2.0

    pause 3.0

    scene a150
    with medium_dissolve

    voice my_audio["424"]
    nar "You quietly step inside and ease the door shut behind you."
    voice my_audio["425"]
    nar "For a brief moment, you simply stand there, letting your eyes wander. It's not what you expected... it's far more put together than the rest of the house."
    voice my_audio["426"]
    nar "The room feels lived in. Every corner seems to say something about the person who calls it home."

    scene a151
    with medium_dissolve

    voice my_audio["427"]
    nar "Gaming equipment, streaming gear, anime posters, collectibles, soft lighting... it's obvious whoever lives here spends a lot of time entertaining people."
    voice my_audio["428"]
    nar "Nothing feels random. Every decoration looks carefully chosen, almost as though the room itself is part of a performance."
    voice my_audio["429"]
    nar "You catch yourself studying the little details longer than you meant to."

    scene a152
    with medium_dissolve

    voice my_audio["430"]
    nar "Then it clicks."
    voice my_audio["431"]
    nar "Yuni... you've heard that name before. One of the biggest streamers on the internet. If you remember correctly, she's joked more than once that she's part 'British, Chinese, Korean, and Japanese... depending on which chat is asking.'"
    voice my_audio["431_1"]
    nar "Which is rather funny, considering she sounds more American than anything else. Her Asian heritage is obvious, her mother is unmistakably British, yet Yuni somehow speaks as though she were raised entirely by California and the internet."
    voice my_audio["432"]
    nar "You've watched a few of her streams over the years. You even remember seeing her mother, Marnie. She's been featured on her stream a few times. Looking around this room now, the pieces finally begin to fall into place."

    scene a153
    with medium_dissolve

    yun "Alright, let me introduce her properly."
    yun "This is my grandmother, Martha. Believe it or not, she's become a bit of a fan favorite within the past 30 minutes."
    yun "People kept asking me to feature her in a twerking video, so... here we are."

    scene a154
    with medium_dissolve

    yun "She wasn't sure about it at first, but she warmed up to the idea."
    yun "Besides, everyone wants to see her shake her ass for the camera."
    yun "Just don't let her sweet smile fool you. She's got more confidence than anybody in this house. Sort of."

    scene a155
    with medium_dissolve

    yun "Anyway, today's pretty simple. It's just a twerking video, and some other things..."
    yun "Nothing complicated. I just need somebody who can follow directions and not make it awkward."
    yun "Think you can handle that?"

    $ gran1 = "{image=evil} {image=sexaddict} Jesus! That's one thicc ass granny!"

    menu:
        mc ""
        "Can you explain in detail what you need me to do?":



            scene a156
            with medium_dissolve

            yun "For sure. I was hoping you'd ask."
            yun "I'll explain everything before we start, so don't worry."
            pass

        "[gran1]" if evil or sexaddict:

            scene a156
            with medium_dissolve

            yun "Whoa, easy there."
            yun "Appreciate the enthusiasm, but let's keep things professional."
            yun "She's my grandma, remember?"
            pass
        "Sure. Walk me through it.":


            scene a156
            with medium_dissolve

            yun "Perfect."
            yun "That attitude makes my life a whole lot easier."

    scene a157
    with medium_dissolve

    yun "Basically, I need you to handle the camera."
    yun "I'll step into the frame a couple of times, but most of the attention is going to be on my grandma."
    yun "Just follow my instructions and keep the shots steady."

    scene a158
    with medium_dissolve

    yun "I'll tell you when to zoom in, when to back up, and when to change angles."
    yun "We'll do a few different poses, a little dancing, and a couple of retakes until everything looks right."
    yun "Trust me, by the end of this you'll know exactly what I'm looking for."

    menu:
        mc ""
        "So... you just need me to film everything while you direct it?":



            scene a162
            with medium_dissolve

            marth "That's right, dear."
            marth "Yuni's the creative one. I'm just happy to help however I can."
            marth "If she asks for my help, I don't think twice."
            marth "Our family's always been like that."
            marth "When one of us needs a hand, the rest of us show up."
            marth "I'd do just about anything for my granddaughter. That's what family means to me."
            pass
        "Are you sure your grandmother actually wants to do this?":


            scene a162
            with medium_dissolve

            marth "Oh, goodness, yes."
            marth "Nobody's forcing me into anything, love."
            marth "Yuni asked if I'd help her, and I said yes. She's my granddaughter."
            marth "We've always looked after one another in this family."
            marth "If I can make her smile and help with her work, I'm happy to do it."
            pass
        "Alright. Just tell me where you want me to stand and what you need.":


            scene a162
            with medium_dissolve

            marth "Now that's the spirit."
            marth "Simple instructions and a willing helper."
            marth "We'll make this nice and easy."
            marth "Just listen to Yuni, and everything will come together."
            marth "She's very good at knowing exactly what she wants."
            pass


    scene a163
    with medium_dissolve

    nar "......."
    voice my_audio["12"]
    nar "Hmmm......."
    voice my_audio["433"]
    nar "Helping Yuni could be useful. Earn her trust now, and she may be far more willing to answer your questions later, or help with something."
    voice my_audio["434"]
    nar "Still... Martha's enthusiasm feels almost too easy. She insists she's comfortable with this, but you can't help wondering whether Yuni is taking advantage of her devotion."

    scene a164
    with medium_dissolve

    voice my_audio["435"]
    nar "Perhaps Martha genuinely wants to help. Perhaps she'd agree to anything if it made her granddaughter happy."
    voice my_audio["436"]
    nar "Either way, the decision is yours."
    voice my_audio["437"]
    nar "You can assist them, get into Yuni's good graces, and see where this peculiar situation leads..."
    voice my_audio["438"]
    nar "Or you can refuse before an uncomfortable family favour becomes something far more degrading."

    $ pee1 = "{image=good} No. This doesn't feel right, and I'm not helping you use your grandmother for views."
    $ pee3 = "{image=evil} {image=sexaddict} I'm in. Only because I wanna see this fat bitch twerk!"
    $ pee4 = "{image=good} Alright. I'll help you film it, but only if Martha's completely comfortable with everything."

    menu:



        "[pee4]" if good:

            scene a165
            with medium_dissolve

            yun "Perfect. And relax, dude. Grandma already said she's fine with it."
            yun "We'll keep everything simple, shoot a few takes, and stop immediately if she changes her mind."
            yun "Now, come on. Let's get everything set up before we lose the lighting."

        "[pee3]" if evil or sexaddict:

            scene a165
            with medium_dissolve

            yun "Good. I knew you weren't completely useless. Also, chill dude."
            yun "Grab the camera, stand where I tell you, and follow my directions."
            yun "Do that, and this should be easy."
        "No. This doesn't feel right, and I'm not helping you use your grandmother for views.":


            scene a167
            with medium_dissolve

            yun "Are you serious right now?"
            yun "UGH!! I knew you were gonna be one of those annoying, judgmental losers who walks in here and acts like he knows everything."
            yun "Grandma already told you she wants to do it. Nobody's forcing her into anything."
            yun "You know what? Forget it. You're wasting my time, dude. Get the fuck out of my room."

            $ yuni_video_refused = True
            $ yuni_video_failed = False
            $ yuni_video_completed = False
            $ supergood_refused_yuni = True
            $ memory_yuni_video_refused = True
            $ show_tooltip(n=22)

            jump after_yuni_refusal


    scene black
    with slowfade

    pause 2.0

    scene a168
    with slowfade

    yun "Alright, hold the camera steady and keep Martha centered in the frame."
    yun "I'll direct you while we're filming. I need wide shots, a few closer angles, and enough movement to keep the video from looking boring."
    yun "I'll probably step into the frame a couple of times too, so don't suddenly move the camera unless I tell you."
    yun "Oh, and we need music. Something with enough energy for the video. You know any good rap songs?"

    scene a170
    with medium_dissolve

    yun "One of my friends sent me three suggestions, but I don't really listen to this kind of music."
    yun "I need you to tell me which one actually fits."
    yun "Pick carefully, because if the music is terrible, the entire video is going to look stupid."

    menu:
        mc ""
        "What are the three songs?":



            scene a171
            with medium_dissolve

            yun "The first one is 'Stan' by Eminem."
            yun "The second is 'Dear Mama' by Tupac."
            yun "And the last one is 'Blow a Bag' by Almighty Suspect."
        "Let me hear the choices first. I can't recommend anything without knowing what she sent you.":


            scene a171
            with medium_dissolve

            yun "Fine. She suggested 'Stan' by Eminem, 'Dear Mama' by Tupac, and 'Blow a Bag' by Almighty Suspect."
            yun "I know the first two are famous, but famous doesn't automatically mean they're right for this."
            yun "So... which one actually works?"
        "The hell? You don't listen to rap? I've literally watched streams of you dancing to-":


            voice my_audio["439"]
            nar "No no no! Do not finish that sentence unless you want her knowing exactly how much of her content you've watched."
            voice my_audio["440"]
            nar "You've seen this woman dancing to rap on stream, singing entire verses without missing a word, and blasting it through her car speakers as though the neighbours personally offended her."
            voice my_audio["441"]
            nar "She absolutely listens to rap. This is probably a test to determine whether you possess decent musical taste or you're some uncultured bastard who chooses songs based entirely on whether the beat makes the furniture vibrate."
            voice my_audio["442"]
            nar "Think carefully. Before we answer, let us consider what these songs are actually about and decide which one fits the video."

    scene a172
    with medium_dissolve

    voice my_audio["12"]
    nar "Hmmm......."
    voice my_audio["443"]
    nar "Two of those songs are slow, serious, and completely wrong for what Yuni is trying to film. She is definitely testing you."
    voice my_audio["444"]
    nar "One of those songs seems like the obvious answer... but choosing poorly could convince Yuni that you're useless and bring your little collaboration to an abrupt end."
    voice my_audio["445"]
    nar "You could trust your own judgment, or you could text Myles and make absolutely certain."

    scene a173
    with medium_dissolve

    menu:
        "'Blow a Bag' by Almighty Suspect. That's the one you want.":




            yun "Blow a bag...?"
            yun "......."
            yun "Never heard of that one, but let's hope you're right."
            yun "Okay, let's start!"
            jump twerkvideo
        "*Text Myles and ask which song fits best.*":


            scene black
            with slowfade

            menu(nvl=True):
                "Yo, you busy?":


                    mc_nvl "Yo, you busy?"
                    myles_nvl "Nah. What's good, bro?"
                    myles_nvl "I was just getting ready to head out."
                    myles_nvl "What's going on?"
                "Need your opinion real quick.":


                    mc_nvl "Need your opinion real quick."
                    myles_nvl "Shoot."
                    myles_nvl "What's up?"
                "Bro... you're not gonna believe this.":


                    mc_nvl "Bro... you're not gonna believe this."
                    myles_nvl "Whenever somebody starts a text like that, I already know it's about to be some bullshit."
                    myles_nvl "What happened?"

            menu(nvl=True):
                "Long story short... I gotta help film a video.":


                    mc_nvl "Long story short... I gotta help film a twerk video."
                    mc_nvl "This chick Yuni wants me to help record her grandma."
                    myles_nvl "..."
                    myles_nvl "Her WHAT?"
                "I'm helping this streamer record something.":


                    mc_nvl "I'm helping this streamer record something."
                    mc_nvl "Apparently her grandma in a twerk video."
                    myles_nvl "Bro..."
                    myles_nvl "What kind of rabbit hole did you fall into?"
                "Don't ask questions... just hear me out.":


                    mc_nvl "Don't ask questions... just hear me out."
                    mc_nvl "They're filming a twerk video with this grandma."
                    myles_nvl "A grandma?"
                    myles_nvl "What the fuck are you doing over there?"

            menu(nvl=True):
                "Don't worry about that. I just need help.":


                    mc_nvl "Don't worry about all that."
                    mc_nvl "I just need help picking a song."
                "It's a long story. I'll explain later.":


                    mc_nvl "It's a long story."
                    mc_nvl "I'll explain later. Right now I need your opinion."
                "Bro, just help me out.":


                    mc_nvl "Bro, just help me out."
                    mc_nvl "I'll tell you everything when I see you."

            myles_nvl "Aight, aight."
            myles_nvl "What songs they got?"

            menu(nvl=True):
                "Stan, Dear Mama, and Blow a Bag.":


                    mc_nvl "Stan."
                    mc_nvl "Dear Mama."
                    mc_nvl "Blow a Bag."
                "They gave me three choices.":


                    mc_nvl "Stan by Eminem."
                    mc_nvl "Dear Mama by Tupac."
                    mc_nvl "Blow a Bag by Almighty Suspect."
                "These are my options...":


                    mc_nvl "Stan."
                    mc_nvl "Dear Mama."
                    mc_nvl "And Blow a Bag by Almighty Suspect."

            myles_nvl "..."
            myles_nvl "Bro, that's easy as hell."
            myles_nvl "'Blow a Bag.'"
            myles_nvl "The other two are great songs, but they ain't the vibe for a twerk video."
            myles_nvl "Pick 'Blow a Bag' and keep it moving."

            menu(nvl=True):
                "That's what I was thinking. Thanks.":


                    mc_nvl "That's what I was thinking."
                    mc_nvl "Appreciate it."
                "Good looking out, bro.":


                    mc_nvl "Good looking out, bro."
                    mc_nvl "Wanted to make sure I wasn't trippin'."
                "Bet. I owe you one.":


                    mc_nvl "Bet."
                    mc_nvl "I owe you one."

            myles_nvl "You definitely owe me an explanation later."
            myles_nvl "Because this whole 'I'm filming a grandma' conversation is wild as hell."
            myles_nvl "Anyway, I gotta finish getting ready."
            myles_nvl "I'm heading to this party tonight, I'll talk to you later."

            menu(nvl=True):
                "Have fun. I'll hit you later.":


                    mc_nvl "Have fun."
                    mc_nvl "I'll text you later."
                "Don't do anything stupid.":


                    mc_nvl "Don't do anything stupid."
                    myles_nvl "No promises."
                "Later, bro.":


                    mc_nvl "Later, bro."

            myles_nvl "Later."
            myles_nvl "Good luck with... whatever the hell you've gotten yourself into."
            jump twerkvideo
        "'Stan' by Eminem. Definitely that one.":





            play sound my_audio["bang sound 1"] noloop
            scene a167
            with hpunch

            yun "What? No, dude! Do you even know what that song is about?"
            yun "That's one of the worst possible choices for this. It doesn't fit the video at all."
            yun "You know what? Forget it. You clearly don't know anything about music."
            yun "Get out of my room. I'll find somebody else."

            $ yuni_video_failed = True
            $ yuni_video_refused = False
            $ yuni_video_completed = False
            $ memory_yuni_music_failed = True
            $ show_tooltip(n=23)

            jump after_yuni_refusal
        "'Dear Mama' by Tupac. It fits because she's your grandmother.":


            play sound my_audio["bang sound 1"] noloop
            scene a167
            with hpunch

            yun "Are you kidding me?"
            yun "It's a great song, but not for this! You can't just choose it because the video has somebody's mother in it."
            yun "Jesus, dude. You have absolutely no idea what you're doing."
            yun "Forget it. Just get out of my room before you ruin the entire idea."

            $ yuni_video_failed = True
            $ yuni_video_refused = False
            $ yuni_video_completed = False
            $ memory_yuni_music_failed = True
            $ show_tooltip(n=23)

            jump after_yuni_refusal


label twerkvideo:

    stop music fadeout 2.0

    scene black
    with slowfade

    pause 2.0

    scene mctwerk
    call godson_locked_cutscene ("gui/mctwerk.webm", 73.0, "seen_mctwerk1") from _call_godson_locked_cutscene_7

    $ yuni_video_completed = True
    $ yuni_video_failed = False
    $ yuni_video_refused = False
    $ memory_yuni_video_helped = True
    $ show_tooltip(n=21)

    jump aftertwerk

label aftertwerk:

    scene black
    with slowfade

    play music my_audio["yuniroom1"] loop fadein 2.0

    pause 3.0

    scene a174
    with slowfade

    yun "Alright! That's a wrap!"

    $ une1 = "{image=good} I....somehow feel like I shouldn't have done some things in that video. This felt totally wrong."
    $ une2 = "{image=evil} {image=sexaddict} *Rubs Martha's ass with your hand.*"
    $ une3 = "{image=superevil} Yeah, I actually enjoyed that. It was fun."

    menu:
        "Yeah, I actually enjoyed that. It was fun.":




            yun "See? I told you it'd be fun."
            yun "People always look at my ideas like I'm completely insane, then we finish filming and suddenly everybody gets it."
            yun "Give me a little time to edit this, and the comment section's gonna lose its mind."

            scene a176
            with medium_dissolve

            menu:
                mc ""
                "You really know how to turn a strange idea into something entertaining.":



                    yun "That's why people watch me."
                    yun "Anybody can point a camera at something. The trick is knowing how to make people care."
                    yun "And this? This is definitely something they're gonna care about."
                "Honestly, that came out way better than I expected.":


                    yun "Of course it did."
                    yun "You had me directing, Grandma performing, and you somehow managed not to ruin the camera work."
                    yun "That's basically the perfect team."
                "I can already tell this video's gonna get a ridiculous amount of attention.":


                    yun "Exactly."
                    yun "The clips alone are gonna spread everywhere."
                    yun "Grandma might wake up tomorrow with her own fan page."

            yun "See grandma? He gave you a compliment."

            scene a188
            with medium_dissolve

            marth "Oh, did you?"
            marth "Well, that's very kind of you, dear."
            marth "I was terribly nervous at first, but once we started, I simply tried not to think about the camera."

            menu:
                mc ""
                "You looked completely natural in front of it.":



                    marth "Did I really?"
                    marth "I felt as though I was about to trip over my own feet half the time."
                    marth "I'm relieved it didn't look that way."
                "You had more confidence than everyone else in the room.":


                    marth "Oh, I wouldn't go that far."
                    marth "Though I suppose age teaches you to stop worrying quite so much about looking foolish."
                    marth "Eventually, you simply enjoy yourself."
                "You definitely have the kind of presence people remember.":


                    marth "That's a lovely thing to say."
                    marth "Most people my age begin wondering whether anyone notices them at all."
                    marth "Perhaps I've been worrying for nothing."

            menu:
                mc ""
                "I can see why Yuni's audience keeps asking for you.":



                    marth "She tells me that, but I always assumed she was exaggerating."
                    marth "Yuni has a habit of making everything sound much larger than it is."
                    marth "Perhaps this time she was telling the truth."
                "You really don't carry yourself like somebody's grandmother.":


                    marth "I'm choosing to take that as a compliment."
                    marth "Though I do have the grandchildren, the aching knees, and the collection of reading glasses to prove it."
                    marth "So don't let appearances fool you entirely."
                "You have a warmth about you that comes through on camera.":


                    marth "Oh... that's rather sweet."
                    marth "I wasn't trying to perform anything special."
                    marth "I was simply having fun with my granddaughter."
                "You don't care that we banged in the middle of it?":


                    marth "Of course not, I told you to do it, remember?"
                    marth "Besides, I think I rather liked your cock."


            menu:
                mc ""
                "You should appear in more of her videos.":



                    marth "Perhaps I will."
                    marth "As long as Yuni doesn't turn me into a full-time employee."
                    marth "I still expect tea breaks and reasonable working hours."
                "I think people are gonna remember you more than the actual video.":


                    marth "Goodness, don't tell Yuni that."
                    marth "She'll have me signing contracts before breakfast."
                    marth "Still... I wouldn't mind being remembered fondly."
                "You made the whole thing feel a lot more fun.":


                    marth "Then I'm glad I agreed to do it."
                    marth "I only wanted to help Yuni, but I did enjoy myself more than I expected."
                    marth "Perhaps trying new things isn't so frightening after all."

            play sound my_audio["bang sound 1"] noloop
            scene a180
            with hpunch

            yun "Alright, dude, that's enough."
            yun "You complimented her once, then twice, then somehow turned it into a full interview."
            yun "She's my grandmother, not your newest obsession."
            yun "Come on. Save some of that charm before her ego gets bigger than mine."

            jump dadcall





        "[une1]" if good:

            yun "What are you talking about?"
            yun "Everybody knew what they were signing up for. Nobody was forced into anything."

            scene a186
            with medium_dissolve

            menu:
                mc ""
                "I don't know... I just can't shake the feeling that I crossed a line.":



                    yun "You didn't."
                    yun "You were asked to help, you asked questions, and everyone agreed before we started."
                    yun "Stop beating yourself up over it."
                "Maybe I'm just overthinking everything after everything that's happened lately.":


                    yun "Yeah, I think you are."
                    yun "You've had a rough couple of days. You're probably looking for problems that aren't even there."
                    yun "Get out of your own head for a minute."
                "It just didn't feel like something I should've been involved in.":


                    yun "Then maybe you're just not used to how I do things."
                    yun "That's fine. Not everybody is."
                    yun "But trust me, if anybody here had been uncomfortable, we would've stopped immediately."

            scene a187
            with medium_dissolve

            yun "Seriously, dude..."
            yun "Quit acting like you're carrying the weight of the world on your shoulders."
            yun "Take a breath. Everything turned out fine."
            jump dadcall


        "[une2]" if evil or sexaddict:

            scene a177
            with medium_dissolve

            yun "Holy shit... that actually came out way better than I expected."
            yun "The camera work was smooth, the timing was on point, and Grandma absolutely nailed it."
            yun "I swear, my chat is gonna lose their minds when they see this."

            scene mcassrub
            with ffast_dissolve

            yun "This is definitely making the highlight reel."
            yun "I'm clipping half of this for shorts, then the full version goes up later tonight."
            yun "This might end up being one of the best-performing videos we've uploaded all year."

            scene a178
            with medium_dissolve

            yun "Grandma, you're becoming a celebrity whether you like it or not."
            yun "People already spam the comments asking where you are every stream."
            yun "Honestly... I might have to start featuring you more often."
            yun "I think everybody's getting a little tired of just seeing me all the time."

            scene a179
            with medium_dissolve

            yun "And you..."
            yun "Not bad."
            yun "I wasn't sure if I'd have to teach you everything from scratch, but you actually followed directions really well."
            yun "Most people panic the second I hand them a camera."
            yun "You actually listened, kept everything steady, and got the shots I wanted."
            yun "Thanks for helping out."
            yun "Seriously. You probably saved me a couple hours of having to reshoot everything."
            jump dadcall

label dadcall:

    play sound my_audio["bang sound 1"] noloop
    scene a167
    with hpunch

    hen "YUNI!"
    yun "Oh, for fuck's sake, WHAT!?"
    hen "Is [playerName] in there!?"
    yun "Yeah! Why!?"
    hen "Can you tell him to come downstairs please!? I need him right now!"
    yun "We're busy!"
    hen "NOW!"

    menu:
        mc ""
        "Fuck does he want with me?":



            yun "Hell if I know."
            yun "Probably another one of his 'important' house emergencies."
            yun "You should probably go before he starts yelling again."
            jump cable7
        "This sounds serious...":


            yun "Maybe."
            yun "Or maybe that's just how my dad talks whenever he wants somebody."
            yun "Either way, I'd go see what he wants."
            jump cable7
        "Should I go?":


            yun "Yeah."
            yun "We'll finish up later if we have to."
            yun "Go see what he wants before he comes barging in here."
            jump cable7


label cable7:
    stop music fadeout 2.0

    scene black
    with slowfade
    if good or sexaddict:
        play music my_audio["think2"] loop fadein 2.0
    elif evil:
        play music my_audio["think2evil"] loop fadein 2.0


    pause 3.0

    scene a192
    with slowfade

    $ what1 = "{image=evil} What the fuck do you want?"
    $ what2 = "{image=good} Really sorry to keep you waiting, Henry. What can I help you with?"
    $ ask1 = "{image=evil} Stop being a pussy."
    $ ask2 = "{image=good} I understand why you're worried, but let's not assume the worst before we know anything."
    $ agreeevil = "{image=evil} Fine. But if I get caught doing this, you're going to owe me."
    $ agreegood = "{image=good} Alright. I'll check, but only to put your mind at ease. We shouldn't invade their privacy any more than necessary."

    menu:
        mc ""


        "[what1]" if evil:

            scene a193
            with medium_dissolve

            hen "Watch your damn mouth."
            hen "If this wasn't important, I wouldn't have dragged you away from whatever you were doing upstairs."
            hen "Now stop giving me attitude and listen for a minute, because I'm already having a difficult enough time keeping myself calm."
        "Hey, I'm here. What's up?":


            hen "Listen... I need a favor, and I hate that I'm even asking you."
            hen "I know we barely know each other, but you're the only person in this house I can involve without immediately making the situation worse."
            hen "Just hear me out before you decide I've completely lost my mind."

        "[what2]" if good:

            hen "No, don't apologize. I'm the one who called you down here without explaining anything."
            hen "I appreciate you coming, especially after the way I've treated you since you arrived."
            hen "I just need your help with something delicate, and I don't know who else I can safely ask."

    scene a194
    with medium_dissolve

    hen "My boss is inside that bedroom with Marnie right now, supposedly conducting her job interview."
    hen "The more I think about it, the stranger the whole thing feels. He's the CEO of a company with hundreds of employees and an entire Human Resources department, yet he personally drove to our house to interview my wife behind a closed bedroom door."
    hen "Martha questioned it earlier, and at first I dismissed her because Martha questions nearly everything she doesn't understand. But now her words are stuck in my head, and I can't stop wondering why a man in his position would make this much effort for someone who hasn't worked in years."
    hen "Maybe he genuinely believes Marnie would be good for the company. Maybe I'm letting jealousy and paranoia make a fool of me. But part of me keeps thinking the job might not be the only reason he's interested in her."

    scene a195
    with medium_dissolve

    menu:
        mc ""
        "You really think he'd risk his position by trying something with an employee's wife?":



            scene a196
            with medium_dissolve

            hen "I don't know, and that's exactly what's driving me insane."
            hen "I'd like to believe a man with that much to lose would know better, but money and authority have a way of convincing people that ordinary consequences no longer apply to them."
            hen "He's always been charming when he wants something, and right now I have no idea what he believes he's going to get from Marnie."

        "[ask2]" if good:

            scene a196
            with medium_dissolve

            hen "You're right. I know you're right."
            hen "Marnie deserves more trust than I'm giving her right now, and I shouldn't decide that something terrible is happening simply because the circumstances look unusual."
            hen "I just need enough reassurance to quiet my head before I do something stupid and ruin the interview myself."

        "[ask1]" if evil:

            scene a196
            with medium_dissolve

            hen "The hell!? I'm not! What do you mean!?"
            hen "Besides, this isn't about whether I trust Marnie."
            hen "I trust my wife. What I don't trust is a powerful man arranging a private meeting with her in our bedroom and expecting everyone else to treat it like an ordinary interview."
            hen "There is a difference between doubting your spouse and refusing to ignore another man's intentions."

    menu:
        mc ""
        "Alright. I'll take a quick look.":



            scene a197
            with medium_dissolve

            hen "Thank you. Seriously, I mean that."
            hen "I know this is an uncomfortable position to put you in, especially after you've only been in this house for one night."
            hen "I owe you one, and I won't forget that."

        "[agreegood]" if good:

            scene a197
            with medium_dissolve

            hen "That's fair, and I don't want you standing there watching them any longer than you have to."
            hen "Just confirm that they're actually discussing the job and that Marnie looks comfortable, then step away."
            hen "Thank you. I owe you one for helping me handle this without making a complete mess of it."

        "[agreeevil]" if evil:

            scene a197
            with medium_dissolve

            hen "Fair enough. If you get caught, I'll admit this was my idea."
            hen "I can't promise the explanation will save either of us from Marnie, but I won't leave you standing there alone taking the blame."
            hen "Do this for me, and I owe you one."

    $ memory_henry_agreed_to_help = True
    $ show_tooltip(n=25)

    if sexaddict and fooledaroundwithmarnie:
        voice my_audio["451-SA"]
        nar "Oh, this is fucking beautiful. Henry wants us to find out whether his boss is trying to fuck Marnie, less than a day after his wife came into our room and turned a supposedly innocent visit into something considerably more physical."
        voice my_audio["452-SA"]
        nar "We may not have spent the entire night fucking her senseless, but we still kissed her, touched her, and fucked her long enough to make this request spectacularly misguided. Henry is asking his wife's most recent mistake to investigate her next possible one."
        voice my_audio["454-SA"]
        nar "Still, we now know exactly what temptation looks like where Marnie is concerned. Let us inspect the competition, satisfy our professional curiosity, and collect the favor Henry so generously offered the least-qualified man in the house."
    elif evil and sexwithmarnie:
        voice my_audio["451"]
        nar "Oh, this is fucking priceless. Henry believes his boss may be trying to fuck his wife, so he asks us, the man who has already fucked his wife, to investigate."
        voice my_audio["452"]
        nar "Is this man a complete fucking idiot? He is outsourcing an adultery investigation to the adultery itself. That's like hiring the burglar who emptied your house to inspect the locks."
        voice my_audio["453"]
        nar "We fucked Marnie's brains out just last night, came inside that dumb whore three times, and now Henry is thanking us, unknowingly, while promising a future favour. If ignorance truly is bliss, this poor bastard has achieved spiritual enlightenment."
        voice my_audio["454"]
        nar "Still, that favour could prove useful. Let us investigate our possible competition, not from loyalty, of course, but professional curiosity. It would be rude not to examine the other applicant."
    elif (evil or sexaddict) and not sexwithmarnie:
        voice my_audio["443-1"]
        nar "Oh, this is magnificent. Henry suspects his boss may be trying to fuck his wife, and his brilliant response is to recruit the suspicious stranger who arrived yesterday as an amateur bedroom spy."
        voice my_audio["444-1"]
        nar "Is this man a complete fucking idiot? A private bedroom is already a rather unusual location for a job interview, and a locked door hardly improves the professional atmosphere."
        voice my_audio["445-1"]
        nar "Yet instead of knocking, interrupting, or speaking directly to his wife, Henry wants us creeping and peeking inside. Trust is apparently the foundation of their marriage. Trust, and outsourced surveillance."
        voice my_audio["446"]
        nar "Still, he promised to owe us one. A favour from Henry could prove useful, and satisfying our curiosity will cost nothing except our dignity and possibly several functioning teeth. Let us take a look."
    elif good:
        voice my_audio["447"]
        nar "Well... this is certainly awkward. Henry has somehow appointed us the least-qualified Human Resources representative in the country."
        voice my_audio["448"]
        nar "Still, he isn't asking because he enjoys spying on his wife. He's frightened, suspicious of his boss, and desperately trying to avoid storming into that room and humiliating Marnie."
        voice my_audio["449"]
        nar "A quick look could reassure him and confirm that Marnie is comfortable, but this is still her private interview. We should see only what is necessary and respect her dignity."
        voice my_audio["450"]
        nar "So we look, confirm that everything is all right, and immediately return to Henry. No lingering, no unnecessary snooping, and absolutely no becoming emotionally invested in whatever dreadful office politics are unfolding inside."

    scene a198
    with medium_dissolve

    hen "They're directly through this door. It's locked, but I'll unlock it for you. I have a key."
    hen "You don't need to enter the room or announce yourself. Just open it slightly, look inside long enough to understand what's happening, and close it again before either of them notices."
    hen "If they're sitting there discussing qualifications, responsibilities, and all the ordinary interview nonsense, come back out and tell me I've been an idiot."
    hen "But if Marnie looks uncomfortable, or if my boss is doing anything that has nothing to do with offering her a job, I need you to tell me immediately."

    scene black
    with slowfade

    pause 2.0

    scene a199
    with slowfade

    boss "Mrs. Marnie, I appreciate you inviting me into your home. I find people are much more relaxed in familiar surroundings than they ever are sitting across from me in a conference room."
    boss "I like getting to know the person behind the résumé. Qualifications matter, of course... but personality tells me much more than a piece of paper ever could."
    mar "Oh! Well, that's lovely to hear. I was terribly nervous before you arrived, but you've been very kind so far."
    mar "I haven't worked in quite a long time, so I'm worried I might be a little rusty."
    mar "Still, I'm a fast learner, and I do love meeting new people."


    scene a200
    with medium_dissolve

    boss "Confidence can be taught. Charm can't. Fortunately for you, you seem to have plenty of the latter."
    boss "Some people naturally draw attention the moment they walk into a room. I'd say you're one of those people."
    mar "Oh goodness... that's very flattering of you to say."
    boss "Tell me... do people often have trouble keeping their attention on the conversation when you're around?"
    hen "......"
    hen "Well?"
    hen "Can you see anything?"
    hen "What's going on in there?"

    scene a201
    with medium_dissolve

    $ peek1 = "{image=evil} Dude, shut the fuck up. I'm trying to listen."

    menu:
        mc ""
        "Would you keep your voice down? I'm trying to listen.":



            pass
        "Hang on... I'm trying to figure out what they're talking about.":


            pass
        "I can't hear everything yet. Give me a second.":


            pass

        "[peek1]" if evil:

            pass

    scene a202
    with medium_dissolve

    boss "Relax, I don't mean anything by it. I'm simply curious. First impressions can have a tremendous impact in business, and yours is... rather memorable."
    boss "If clients find you as engaging as I do, you may prove to be quite an asset to the company."
    mar "I... well... thank you. I suppose I've never really thought about it like that."
    mar "Henry always tells me I have a habit of talking to everyone like I've known them for years."

    scene a203
    with medium_dissolve

    boss "That isn't necessarily a bad thing. The right smile can open doors that qualifications alone never will."
    mar "Well... I certainly hope that's true."
    boss "Something tells me this interview is turning out to be much more interesting than I expected."

    scene a204
    with medium_dissolve

    boss "Uh-huh, interesting. Anyway, Marnie....let's talk about something else."
    boss "Let's talk about sex, what's your favorite position?"
    mar "O-Oh....my favorite sex position?"
    mar "......"

    scene a205
    with medium_dissolve

    mar "Hmm...."
    mar "........"
    mar "..........."
    mar ".............."

    scene a206
    with medium_dissolve

    mar "Well, I quite like it when someone is on top of me."
    mar "I like it when the man is in control, so having him on top of me is the perfect position."

    scene a207
    with medium_dissolve

    mar "...and since we're on the subject. I also like it when my hair is being pulled."
    mar "I also like to be slapped, spat on, called a whore, and I absolutely LOVE deep-throating!"
    boss "......"
    boss "(Heh.....music to my ears. This woman is an absolute whore!)"

    scene marnierub
    with medium_dissolve

    boss "Well, that is quite interesting indeed."
    boss "Very well, you pass that part of the test, heh."
    mar "Oh, that was a test? Well, I'm glad I passed!"
    boss "Yes you did, with flying colors!"
    mc "........"

    $ upe99 = "{image=evil} {image=sexaddict} *Do nothing and watch.* (NTR Version Only)"

    menu:
        "*GET IN THERE NOW!*":



            jump bargein

        "[upe99]" if ntr:
            jump ntr1

label ntr1:

    $ marnie_interview_watched = True
    $ marnie_interview_stopped = False
    $ marnie_boss_attacked = False
    $ memory_henry_stood_by_and_watched = True
    $ show_tooltip(n=26)


    scene black
    with slowfade

    pause 2.0

    scene x54
    with slowfade

    boss "There is one final part of the interview. A practical assessment to determine whether you're suitable for the position."
    boss "The role occasionally involves employee wellness and physical relaxation, so I'll need to give you a naked, full-body massage and evaluate how well you respond to the treatment."
    mar "A full-body massage? Oh... I certainly wasn't expecting that."
    mar "It does sound rather lovely, though. Should I go into the bathroom and remove my dress?"
    boss "Nonsense. You're going to be naked for the assessment anyway, so there's little point wasting time changing in another room."
    boss "We're both adults, Marnie. Remaining efficient and comfortable is simply part of being professional."
    mar "Oh... well, I suppose that makes sense. What would you like me to do?"
    boss "Well, you can start by grabbing the bottom of your dress and slowly lift it upward. And uh, spreads your legs too."
    boss "Bring it all the way up to your neck. Once you're exposed, I'll help position you on the bed and begin the massage."
    boss "If you don't want to do it, then say so. I'm not here to make you do anything you wouldn't want to."
    mar "Um...well.. alright. If this is genuinely part of the assessment, I'll do it."
    boss "Perfect."

    scene marnieliftdress
    with ffast_dissolve
    if not persistent.seen_marnieliftdress:


        $ config.allow_skipping = False
        $ renpy.pause(13.3, hard=True)
        $ config.allow_skipping = True


        $ persistent.seen_marnieliftdress = True
        $ renpy.save_persistent()
    else:



        pause 13.3

    mar "How's this?"
    boss "That's perfect Marnie, you're doing a great job."
    boss "(Heh, I can't believe she did it! What a complete whore!)"
    mar "So, what's next? Should I take it all off now?"
    boss "Not quite."
    boss "I'll want you to stick your tongue down my throat. Basically, let's tongue fuck each other."
    boss "This isn't even for the job, you're hired. I just want to tongue-fuck you."
    mar "Oh...you mean like, making out? I....I suppose that's fine."
    boss "Fantastic. Here I come, dumb bitch....I mean....ma'am."

    scene black
    with ffade

    scene marniekiss45
    with ffast_dissolve
    if not persistent.seen_marniekiss45:


        $ config.allow_skipping = False
        $ renpy.pause(26, hard=True)
        $ config.allow_skipping = True


        $ persistent.seen_marniekiss45 = True
        $ renpy.save_persistent()
    else:



        pause 26

    play sound my_audio["bang sound 1"] noloop
    scene x55
    with hpunch

    boss "Woah! You're getting carried away!"
    mar "Oh! I-I'm sorry! Kissing always does that to me...."
    boss "No, no. It's alright miss, heh. I enjoyed it."
    boss "Anyway, let's take off that dress and get started, shall we?"
    mar "Okay!"

    scene black
    with slowfade

    pause 1.0

    scene x56
    with slowfade

    boss "That's great Marnie, you're a natural."
    boss "You can sit up now."

    scene x58
    with medium_dissolve

    boss "Okay, now we'll do the naked massage."
    boss "Stand up and get on the bed, and make sure to lay flat on your stomach, alright?"
    boss "You do want to do this, right? We're past the job interview, as I said, you're already hired. I just want to touch your naked body, heh."
    mar "Y-Yes! No problem! I rather like massages, and since I'm already hired, that makes you a guest here and I want our guests to enjoy themselves."
    mar "Please touch me wherever you like!"
    stop music fadeout 2.0
    stop music2 fadeout 2.0

    scene black
    with slowfade

    pause 1.0

    scene marniemassage
    with ffast_dissolve
    call godson_locked_cutscene ("gui/marniemassage.webm", 125.0, "seen_marniemassage") from _call_godson_locked_cutscene_8

    scene black
    with slowfade
    play music2 my_audio["apartment4"] loop fadein 2.0

    pause 3.0

    scene a219
    with slowfade

    hen "Sir, please! Just give me a chance to explain! I swear this isn't what it looked like!"
    boss "SAVE YOUR ENERGY! Because you're going to need to while spending the next two months unloading trucks at Warehouse Seven!"

    scene a220
    with medium_dissolve

    hen "TWO MONTHS!?"
    boss "MAKE IT THREE!"
    boss "YOUR WIFE IS A FUCKIN WHORE! SHE'S HIRED BUT THE FACT THAT YOU CAN'T CONTROL YOUR SLUT WIFE MAKES YOU INCOMPETENT!"
    hen "Sir! Please! Don't do this!"
    hen "Sir! Wait! Please, just hear me out! Sir!"
    hen "SIR!!"
    mc "..........."
    mar ".........."

    scene a221
    with medium_dissolve

    $ angryhenryevil = "{image=evil} I just didn't feel it was right to barge in, heh."

    hen "........"
    hen "..........."
    hen "Do you have any idea what you just did!?"
    hen "You may have just cost me my job!"

    menu:
        mc ""


        "[angryhenryevil]" if evil:

            hen "Don't you dare turn this around on me!"
            hen "I asked you to look inside and tell me what was happening, but all you did was sit there and watch!"
            hen "You took a bad situation and made it ten times worse!"
        "You were worried about Marnie. I watched, and didn't see anything wrong.":


            hen "Sure, and now I'm the one who has to deal with the consequences!"
            hen "You must have seen SOMETHING or else he wouldn't have reacted like that!"
            hen "I needed you to help me understand what was happening, but you really just FUCKED me over!"

    hen "You know what? I can't do this right now."
    hen "I need some space before I say something I'm going to regret."
    hen "I'm going outside."
    hen "Just... stay the fuck away from me for a while."

    scene a222
    with medium_dissolve

    mar "......"
    mar "........."
    mar "............"
    mc ".................."
    jump ayee1ntr

label ayee1ntr:

    $ fuckit = "{image=evil} *Start thinking about how sexy Marnie is.*"

    menu:
        mc ""
        "*Try to explain yourself to Marnie.*":



            scene a223
            with medium_dissolve

            mar "What in the world were you thinking, hiding behind that door and watching us?"
            mar "You stood there while the interview became far more... personal. You shouldn't have spied on us."
            mar "If Henry's boss had caught you spying, he could have accused Henry of arranging the entire thing. This could have ended with Henry losing his job, or considerably worse."
            mar "And if you were genuinely worried about me, why did you remain there watching for so long? Why didn't you say something?"

            $ explain_evil = "{image=evil} I wanted to see how far you'd let him go. Neither of you looked particularly eager to stop."

            menu:
                mc ""
                "I froze. Everything became strange so quickly, and I didn't know whether interrupting would make the situation better or worse.":



                    mar "I can believe that. The entire situation became confusing far more quickly than I was prepared for."
                    mar "But standing behind the door and continuing to watch was still a choice."
                    mar "Next time, either speak up or walk away. Please don't simply remain there observing something so private."

                "[explain_evil]" if evil:

                    mar "You wanted to see how far I would let it go?"
                    mar "That is a truly horrible thing to admit. Whatever mistakes I made in that room, they were not an invitation for you to secretly watch me."
                    mar "My confusion and poor judgment do not make my privacy any less important."

            mar "I'm not pretending I handled that interview properly. I allowed him into things I should have questioned immediately."
            mar "But now I need to find Henry. I need to make sure he's okay. Do NOT tell him what happened."
            mar "We'll talk again later, alright? For now... please give me some space."

            $ marnie_aftermath_explained = True
            $ marnie_aftermath_gave_in = False
            $ memory_marnie_explanation = True
            $ show_tooltip(n=29)

            if evil:
                jump ninawait
            else:
                jump lor1


        "[fuckit]" if evil and sexwithmarnie:

            $ marnie_aftermath_gave_in = True
            $ marnie_aftermath_explained = False
            $ memory_marnie_aftermath = True
            $ show_tooltip(n=30)


            voice my_audio["455"]
            nar "Oh, fuck it. Let Henry sulk in whatever wounded little corner of his pride he's crawled into. What matters is Marnie. Gorgeous, ripe, those absurdly enormous tits close enough to touch, and the taste of her still vivid on your tongue."
            voice my_audio["456"]
            nar "Only last night, your tongue was buried in her mouth, her breath breaking hot against your lips while her wedding vows quietly disappeared somewhere between your hands and her hunger."
            voice my_audio["457"]
            nar "And now here she stands again. Henry's wife by title, perhaps, but in practice? Something delightfully less respectable. A shameless temptation who remembers everything you did together, and knows perfectly well that you want more."
            voice my_audio["458"]
            nar "That recent confrontation ought to have sobered you. It should have reminded you of consequences, guilt, and that fragile little boundary separating desire from complete disaster."
            voice my_audio["459"]
            nar "Instead, it only makes her look more delicious. Your pulse grows heavy, your restraint begins to unravel, and that familiar hunger rises from somewhere deep, dark, and increasingly impossible to contain."
            voice my_audio["460"]
            nar "Until...."

            scene mcgrabher
            with ffast_dissolve
            call godson_locked_cutscene ("gui/mcgrabher.webm", 76.0, "seen_mcgrabher") from _call_godson_locked_cutscene_9


            jump ninawait

label bargein:

    $ marnie_interview_stopped = True
    $ marnie_interview_watched = False
    $ marnie_boss_attacked = False
    $ memory_marnie_intervened = True
    $ show_tooltip(n=27)


    play sound my_audio["bang sound 1"]
    scene a209
    with hpunch

    $ bargegood1 = "{image=good} Take your hands off her! This interview is over!"
    $ bargeevil1 = "{image=evil} Get your fucking hands off her before I break them!"

    menu:
        mc ""


        "[bargegood1]" if good:

            boss "What the hell!?"
            boss "Who are you, and what gives you the right to come barging into a private interview?"
            boss "Get out of this room before you create a problem you can't take back."
        "Back away from her. I saw exactly what you were doing.":


            boss "Excuse me?"
            boss "You burst through the door, interrupt my interview, and now you're making accusations about something you clearly don't understand?"
            boss "You'd better explain yourself very carefully."

        "[bargeevil1]" if evil:

            boss "What!? Who are you and the fuck do you think you're talking to!?"
            boss "You come charging into this room like some deranged idiot, threaten me, and expect me to tolerate it!?"
            boss "You've just made a very serious mistake! Whoever you are!"

    scene a210
    with medium_dissolve

    boss "Listen, punk. Let's make one thing perfectly clear. I don't know who you are, why you're in this room, or why you believe you have any authority over what happens during my interview."
    boss "I was speaking privately with a potential employee when you kicked open the door and started behaving like a common thug!"
    boss "So, before I call Henry and have you removed from this room, tell me exactly what you think you saw."

    $ bargegood2 = "{image=good} I saw a woman becoming increasingly uncomfortable while you used a job interview as an excuse to get too close to her."
    $ bargeevil2 = "{image=evil} I saw you feeling her up! Fuck you! Get out!"

    menu:
        mc ""


        "[bargegood2]" if good:

            boss "Uncomfortable?"
            boss "You watched a few seconds through a cracked door and decided you understood the entire conversation?"
            boss "You have no idea what was being discussed or what Mrs. Marnie agreed to before you interrupted us."
        "I saw your arm around her while you asked questions that had nothing to do with the job.":


            boss "That is an absurd interpretation of what happened!"
            boss "I was attempting to make her feel comfortable during an interview, something I do with every promising candidate!"
            boss "The fact that your mind immediately went somewhere inappropriate says considerably more about you than it does about me!"

        "[bargeevil2]" if evil:

            boss "Watch your mouth, punk!"
            boss "Say something like that again, and you'll find out exactly how seriously I take defamation!"

    scene a211
    with medium_dissolve

    boss "Do you have any idea who you're speaking to?"
    boss "I employ thousands of people, I know judges, attorneys, police commissioners, and men who can make an inconvenience disappear before breakfast."
    boss "You are nobody. Some nameless kid standing in a house that doesn't belong to him, interfering in business he knows nothing about."
    boss "So I suggest you step aside, apologise, and pray I decide you're too insignificant to remember."

    $ bargegood3 = "{image=good} Your position doesn't give you the right to intimidate people. Please leave this house now."
    $ bargeevil3 = "{image=evil} *Grab him and wrestle him to the ground!*"

    menu:
        mc ""


        "[bargegood3]" if good:

            boss "..."
            boss "You know what? Fine."
            boss "This ridiculous interview is over, and so is any opportunity Mrs. Marnie had with my company."

            scene a218
            with medium_dissolve

            boss "I'm leaving before this household drags me any further into its dysfunction."
            boss "Henry! I know you're skulking around outside that door, so stop hiding and look at me."
            boss "You and I are going to have a very serious conversation about this at the office."

            jump henrytrouble
        "I don't care who you know. The interview's over, so get out before this gets worse.":


            boss "You arrogant son of a bitch."
            boss "You think shouting loudly enough suddenly gives you authority over me?"
            boss "Fine. Keep your miserable little house and whatever insanity is happening inside it."

            scene a218
            with medium_dissolve

            boss "I'm done wasting my time here."
            boss "Henry! Come out from behind that door. I know damn well this was your idea."
            boss "I expect you in my office tomorrow morning, and you'd better arrive with an explanation convincing enough to save your career."

            jump henrytrouble

        "[bargeevil3]" if evil:
            stop music

            $ marnie_boss_attacked = True
            $ memory_henry_boss_attacked = True
            $ show_tooltip(n=28)


            scene mcgrabhim
            with ffast_dissolve

            if not persistent.seen_bargeevil3:


                $ config.allow_skipping = False
                $ renpy.pause(15, hard=True)
                $ config.allow_skipping = True


                $ persistent.seen_bargeevil3 = True
                $ renpy.save_persistent()
            else:



                pause 15

            scene a214
            with medium_dissolve
            play music my_audio["sneaky3_1"]

            boss "L-LET GO OF ME YOU SON OF A BITCH!"
            boss "WHAT THE FUCK ARE YOU DOING!?"

            menu:
                "Keep quiet and stay still, or you're fucked!":



                    pass
                "Fuck you, bitch! This is what you get!":

                    pass
                "You want some more!? Keep struggling!":

                    pass
                "Fuck around and find out, motherfucker!":

                    pass

            boss "F-Fuck you!! GET OFF OF ME!"

            play sound my_audio["bang sound 1"] noloop
            scene a215
            with hpunch

            hen "!!!!!!!"
            play sound my_audio["bang sound 2"] noloop
            scene a216
            with hpunch

            hen "W-WHAT THE FUCK ARE YOU DOING!? GET OFF OF HIM, NOW!"
            hen "HAVE YOU LOST YOUR MIND!?"

            scene a217
            with medium_dissolve

            menu:
                mc ""
                "I caught this son of a bitch putting his hands all over your wife!":


                    boss "I HAVE DONE NO S-SUCH THING! LET GO OF ME, NOW!!"
                    hen "I DON'T CARE WHAT YOU THINK YOU SAW!"
                    hen "YOU DON'T GET TO PUT PEOPLE IN A DAMN CHOKEHOLD IN MY HOUSE!"
                    hen "LET HIM GO! RIGHT NOW!"

                    scene a213
                    with medium_dissolve
                "Ask him why he was wrapping his arm around Marnie if it was 'just an interview!'":

                    boss "I HAVE DONE NO S-SUCH THING! LET GO OF ME, NOW!!"
                    hen "THIS ISN'T THE WAY TO HANDLE IT!"
                    hen "IF SOMETHING WAS WRONG, WE'D DEAL WITH IT AFTER YOU LET HIM GO!"
                    hen "NOW GET YOUR HANDS OFF OF HIM!"

                    scene a213
                    with medium_dissolve
                "FUCK THAT! He crossed the line the second he touched your wife! I'm finishing this!":

                    boss "I HAVE DONE NO S-SUCH THING! LET GO OF ME, NOW!!"
                    hen "NO, YOU AREN'T!"
                    hen "YOU'RE GOING TO LET GO BEFORE YOU MAKE THIS TEN TIMES WORSE!"
                    hen "GET OFF OF HIM! NOW!"

                    scene a213
                    with medium_dissolve

                    menu:
                        mc ""
                        "Look at him! He's still trying to act innocent after what he did!":



                            hen "I SAID LET HIM GO!"
                            hen "IF HE DID SOMETHING, WE'LL DEAL WITH IT AFTER YOU LET HIM GO!"
                            hen "NOW GET THE FUCK OFF OF HIM!"
                            jump henrytrouble
                        "Tell him to admit what he was doing with Marnie!":


                            hen "THIS ISN'T HOW YOU HANDLE SOMETHING LIKE THIS!"
                            hen "YOU DON'T GET TO PLAY JUDGE, JURY, AND EXECUTIONER!"
                            hen "LET HIM GO! RIGHT NOW!"
                            jump henrytrouble
                        "I'm not letting go until he agrees to get the hell out of this house!":


                            hen "YOU ARE GOING TO LET GO RIGHT NOW!"
                            hen "I'M TELLING YOU FOR THE LAST TIME!"
                            hen "GET OFF OF HIM!"
                            jump henrytrouble

label henrytrouble:
    stop music fadeout 2.0

    scene black
    with slowfade
    play music my_audio["apartment4"] loop fadein 2.0

    pause 3.0

    scene a219
    with slowfade

    hen "Sir, please! Just give me a chance to explain! I swear this isn't what it looked like!"
    boss "SAVE YOUR ENERGY! Because you're going to need to while spending the next two months unloading trucks at Warehouse Seven!"

    scene a220
    with medium_dissolve

    hen "TWO MONTHS!?"
    boss "MAKE IT THREE!"
    boss "And if I hear one more word out of your mouth, I'll find something even WORSE for you to do!"
    hen "Sir! Please! Don't do this!"
    hen "Sir! Wait! Please, just hear me out! Sir!"
    hen "SIR!!"
    mc "..........."
    mar ".........."

    scene a221
    with medium_dissolve

    $ angryhenrygood = "{image=good} Henry, you asked me t-"
    $ angryhenryevil = "{image=evil} HEY! I did exactly what you asked me to do... don't even come at me with that bullshit tone."

    hen "........"
    hen "..........."
    hen "Do you have any idea what you just did!?"
    hen "You may have just cost me my job!"

    menu:
        mc ""


        "[angryhenryevil]" if evil:

            hen "Don't you dare turn this around on me!"
            hen "I asked you to look inside and tell me what was happening, not storm in there and blow up the entire interview!"
            hen "You took a bad situation and made it ten times worse!"

        "[angryhenrygood]" if good:

            hen "I know what I asked you to do!"
            hen "But I needed information, not a confrontation!"
            hen "You should've come back and told me what you saw before everything spiraled out of control!"
        "You were worried about Marnie. I reacted to what I saw. Isn't that what you wanted?":


            hen "Sure, and now I'm the one who has to deal with the consequences!"
            hen "I was worried, yes, but that doesn't mean I wanted the entire situation to explode in my face!"
            hen "I needed you to help me understand what was happening, not make the decision for me!"

    hen "You know what? I can't do this right now."
    hen "I need some space before I say something I'm going to regret."
    hen "I'm going outside."
    hen "Just... stay the fuck away from me for a while."

    scene a222
    with medium_dissolve

    mar "......"
    mar "........."
    mar "............"
    mc ".................."
    jump ayee1

label ayee1:

    $ fuckit = "{image=evil} *Start thinking about how sexy Marnie is.*"

    menu:
        mc ""
        "*Try to explain yourself to Marnie*.":



            scene a223
            with medium_dissolve

            mar "What in the world were you thinking?"
            mar "I know you were trying to help, and I truly do appreciate that, but everything's become such a dreadful mess."
            mar "Henry's boss has just stormed out of our house, Henry's terrified he's about to lose his job, and somehow it's all happened during my interview."
            mar "Whether you were right or wrong doesn't really matter at this very moment. Right now, I have to go and make sure Henry's alright."

            $ explain_good = "{image=good} I honestly thought something wasn't right. I couldn't just ignore it."
            $ explain_evil = "{image=evil} I don't regret stepping in. He was getting far too comfortable with you. Fuck him."

            menu:
                mc ""


                "[explain_good]" if good:

                    mar "I know..."
                    mar "And perhaps you genuinely believed you were doing the right thing."
                    mar "But sometimes our good intentions create problems we never expected."
                "I reacted before I had a chance to think everything through.":


                    mar "I believe that."
                    mar "Emotions have a funny way of making us act before our minds have caught up."
                    mar "I only wish things hadn't unfolded the way they did."

                "[explain_evil]" if evil:

                    mar "Maybe he was. Maybe he wasn't."
                    mar "But once things reach the point where everyone starts shouting, nobody stops to listen anymore."
                    mar "Now all that's left is trying to put the pieces back together."

            mar "I'm sorry, but I really do need to go and find Henry."
            mar "He's going to need someone with him right now, and... well... that's supposed to be me."
            mar "We'll talk later, alright? Once everyone's had a chance to calm down."
            $ marnie_aftermath_explained = True
            $ marnie_aftermath_gave_in = False
            $ memory_marnie_explanation = True
            $ show_tooltip(n=29)

            if evil:
                jump ninawait
            else:
                jump lor1


        "[fuckit]" if evil and sexwithmarnie:

            $ marnie_aftermath_gave_in = True
            $ marnie_aftermath_explained = False
            $ memory_marnie_aftermath = True
            $ show_tooltip(n=30)


            voice my_audio["455"]
            nar "Oh, fuck it. Let Henry sulk in whatever wounded little corner of his pride he's crawled into. What matters is Marnie. Gorgeous, ripe, those absurdly enormous tits close enough to touch, and the taste of her still vivid on your tongue."
            voice my_audio["456"]
            nar "Only last night, your tongue was buried in her mouth, her breath breaking hot against your lips while her wedding vows quietly disappeared somewhere between your hands and her hunger."
            voice my_audio["457"]
            nar "And now here she stands again. Henry's wife by title, perhaps, but in practice? Something delightfully less respectable. A shameless temptation who remembers everything you did together, and knows perfectly well that you want more."
            voice my_audio["458"]
            nar "That recent confrontation ought to have sobered you. It should have reminded you of consequences, guilt, and that fragile little boundary separating desire from complete disaster."
            voice my_audio["459"]
            nar "Instead, it only makes her look more delicious. Your pulse grows heavy, your restraint begins to unravel, and that familiar hunger rises from somewhere deep, dark, and increasingly impossible to contain."
            voice my_audio["460"]
            nar "Until...."

            scene mcgrabher
            with ffast_dissolve
            call godson_locked_cutscene ("gui/mcgrabher.webm", 76.0, "seen_mcgrabher") from _call_godson_locked_cutscene_10


            jump ninawait



label ninawait:

    scene black
    with slowfade

    pause 3.0

    scene a225
    with slowfade

    voice my_audio["463_1"]
    nar "At last... silence. No shouting, no awkward requests, and, miraculously, no one demanding that you solve a disaster you didn't create."
    voice my_audio["463_2"]
    nar "For the first time today, you have a moment to breathe and sort through the increasingly questionable chain of decisions that brought you here."
    voice my_audio["463_3"]
    nar "Peace, then. Brief, suspicious, and almost certainly temporary... but long enough to reflect on everything that's happened."

    if yuni_video_completed:
        voice my_audio["464"]
        nar "Earlier, you helped Yuni turn her grandmother's rather enthusiastic performance into a full production. Whatever you thought of the experience afterward, you finished the job... and somehow, that was the least complicated part of your afternoon."
    elif yuni_video_failed:
        voice my_audio["465"]
        nar "Earlier, you agreed to help Yuni film her grandmother, failed her little music test, and were promptly thrown out of the room. Somehow, being dismissed over a terrible song choice was the least complicated part of your afternoon."
    elif yuni_video_refused:
        voice my_audio["466"]
        nar "Earlier, you walked away from Yuni's request to film her grandmother and followed Henry's voice downstairs instead. In hindsight, refusing that strange little production may have been the final sensible decision of your afternoon."
    else:
        voice my_audio["467"]
        nar "The afternoon has left you alone with far more to consider than when it began. You came downstairs expecting a simple favour from Henry; naturally, this house had other plans."

    if marnie_interview_watched and marnie_aftermath_explained:
        voice my_audio["468"]
        nar "Henry asked you to check on Marnie's interview, and you responded by standing behind the door while his boss stripped away every last trace of professionalism... and most of Marnie's clothing."
        if sexwithmarnie or fooledaroundwithmarnie:
            voice my_audio["469"]
            nar "After your secret encounter with Marnie last night, you watched another man enjoy her today, earned Henry's fury, then apologised when Marnie confronted you. She asked for silence and space; for once, you have given her both."
        else:
            voice my_audio["470"]
            nar "You earned Henry's fury, then faced Marnie's questions and admitted that remaining there had been a choice. She asked for silence and space; for once, you have given her both."

    elif marnie_interview_watched and marnie_aftermath_gave_in:
        voice my_audio["468"]
        nar "Henry asked you to check on Marnie's interview, and you responded by standing behind the door while his boss stripped away every last trace of professionalism... and most of Marnie's clothing."
        if sexwithmarnie or fooledaroundwithmarnie:
            voice my_audio["471"]
            nar "Henry stormed away, Marnie stood amid the wreckage, and rather than explain yourself, you pulled her into yet another encounter. One day in this house, and restraint has already filed for permanent leave."
        else:
            voice my_audio["472"]
            nar "Henry stormed away, Marnie stood amid the wreckage, and rather than explain yourself, you pulled her into an encounter of your own. One day in this house, and restraint has already filed for permanent leave."

    elif marnie_interview_stopped and marnie_aftermath_explained:
        if marnie_boss_attacked:
            voice my_audio["473"]
            nar "When Henry asked for a quick look, you answered by barging into the room, threatening his boss, and wrestling the man to the floor. Subtle, restrained, and precisely none of the things Henry requested."
        else:
            voice my_audio["474"]
            nar "When Henry asked for a quick look, you barged into the room and ended the interview yourself. You protected Marnie from a powerful man crossing the line... but also handed that man Henry's career on his way out."

        if good:
            voice my_audio["475"]
            nar "Henry left furious, Marnie hurried after him, and you stayed behind knowing your intentions were better than the damage they caused. Doing the right thing rarely arrives with such spectacularly poor timing."
        elif sexaddict:
            voice my_audio["476"]
            nar "Henry left furious, Marnie hurried after him, and even you chose to explain rather than chase another impulse. Considering how this day began, that small display of restraint deserves a modest round of applause."
        elif evil and (sexwithmarnie or fooledaroundwithmarnie):
            voice my_audio["477"]
            nar "Henry left furious, Marnie hurried after him, and you explained yourself while carrying the private knowledge that you had already crossed a far greater line with his wife. Hero, adulterer, houseguest... why settle for one role?"
        else:
            voice my_audio["478"]
            nar "Henry left furious, Marnie hurried after him, and you offered an explanation instead of making matters worse. A surprisingly measured ending from the man who began his visit by forcing his way through the front door."

    elif marnie_interview_stopped and marnie_aftermath_gave_in:
        if marnie_boss_attacked:
            voice my_audio["473"]
            nar "When Henry asked for a quick look, you answered by barging into the room, threatening his boss, and wrestling the man to the floor. Subtle, restrained, and precisely none of the things Henry requested."
        else:
            voice my_audio["474"]
            nar "When Henry asked for a quick look, you barged into the room and ended the interview yourself. You protected Marnie from a powerful man crossing the line... but also handed that man Henry's career on his way out."

        if sexwithmarnie or fooledaroundwithmarnie:
            voice my_audio["479"]
            nar "Then, after supposedly rescuing Marnie and watching Henry's life catch fire, you gave in and pulled her into yet another encounter. At this point, the moral high ground is visible only with specialised equipment."
        else:
            voice my_audio["480"]
            nar "Then, after supposedly rescuing Marnie and watching Henry's life catch fire, you gave in and pulled her into an encounter of your own. At this point, the moral high ground is visible only with specialised equipment."

    voice my_audio["481"]
    nar "Henry's little request has somehow ended in shouting, damaged trust, and an interview that no sensible company would ever acknowledge in writing."
    voice my_audio["482"]
    nar "For now, the house has gone quiet, leaving you alone with the consequences... and the uneasy certainty that quiet never lasts very long here."

    play sound my_audio["frontdoorknob"] noloop
    scene a226
    with medium_dissolve

    voice my_audio["483"]
    nar "The quiet is broken by the faint turn of the front doorknob."
    voice my_audio["484"]
    nar "A moment later, the door eases open, allowing a narrow blade of daylight to stretch across the floor."
    voice my_audio["485"]
    nar "Someone steps inside... and judging by the confidence with which she enters, this is hardly her first visit."

    scene black
    with slowfade

    pause 1.0

    scene a228
    with slowfade

    unk "Oh... hello."
    unk "I wasn't expecting to find anyone sitting here. I'm Nina, an old friend of the family."
    unk "I was looking for Henry. He was supposed to take me to my appointment, though knowing him, he's probably forgotten entirely."

    scene a227
    with medium_dissolve

    nin "........"
    nin "............."
    nin "................"
    nin "Well... this is quite a surprise. What's going on? Did something happen?"

    scene a229
    with medium_dissolve

    menu:
        mc ""
        "What do you mean? I'm just taking a moment for myself to reflect. Is that surprising?":



            nin "Waiting for Henry isn't the surprising part."
            nin "It's you sitting here as though you've always belonged in this house."
            nin "Where exactly did you come from... and where have you been all this time?"
        "Why are you looking at me like you've seen a ghost?":


            nin "Because, in a manner of speaking, perhaps I have."
            nin "Someone the rest of us believed was gone for good after all this time."
            nin "And now you've simply appeared here without so much as an explanation."
        "Did Marnie or Henry tell you about me already?":


            nin "No. Neither of them said a word."
            nin "Though this family has always had an irritating habit of keeping important things from me until the very last moment."
            nin "Still, I would have remembered hearing about someone like you."

    scene a230
    with medium_dissolve

    nin "Come on, don't leave me standing here with half the story."
    nin "This family has excluded me from enough strange little secrets over the years, and I refuse to be the last person informed again."
    nin "How are you here? Where have you been? And why does everyone appear to be behaving as though this is perfectly normal?"
    nin "Go ahead. Start wherever you think makes the most sense."

    menu:
        mc ""
        "I have absolutely no clue what you're talking about.":



            pass
        "What are you talking about?":


            pass
        "I'm very confused right now. How do you even know me? I've never met you before in my life.":


            pass

    scene a231
    with medium_dissolve

    nin "......"
    nin "..........."
    nin "................"

    scene a232
    with medium_dissolve

    nin "You genuinely don't know anything, do you?"
    nin "That expression isn't an act. You truly have no idea why seeing you here should be impossible."
    nin "Interesting... very interesting. Whatever has happened, I think you and I need to have a proper conversation before anyone else decides what you're allowed to know."


    scene a245
    with medium_dissolve

    nin "As much as I want an explanation right now, I have an appointment I absolutely cannot miss."
    nin "I shouldn't be gone for more than a few hours. When I return, you and I are going to sit down somewhere private and have a very long conversation."
    nin "Until then, please stay here, and, more importantly, don't tell anyone what I've said to you."

    scene a246
    with medium_dissolve

    nin "I know that must sound frustrating after everything I just told you."
    nin "But I need time to collect my thoughts. Seeing you standing here has turned several things I believed to be impossible completely upside down."
    nin "We'll speak when I get back. I promise."

    nar "......."
    nar ".........."
    voice my_audio["486"]
    nar "Oh, for fuck's sake... here we go again."
    voice my_audio["487"]
    nar "Nina hasn't even made it to the door, and since I am quite literally your mind, I already know exactly where this is heading."
    voice my_audio["488"]
    nar "A woman built like that mentions an appointment, and your first thought isn't, 'Safe travels.' It's, 'Surely that can wait until after I get those enormous breasts upstairs.'"
    voice my_audio["489"]
    nar "Yes, yes. You want to take her to your room and fuck her brains out. Thank you. A remarkably subtle thought. Now comes the difficult part: somehow convincing her to stay."
    voice my_audio["490"]
    nar "Then again, perhaps I'm being presumptuous. Maybe you're not interested in her. She is an old woman, after all... granted, an old woman with enormous breasts and an absolutely banging body, but perhaps she simply isn't your thing."
    voice my_audio["491"]
    nar "I should warn you, however: this one in particular looks as though she would be a very interesting fuck."
    voice my_audio["492"]
    nar "And just a small observation... either you've become extraordinarily lucky through sheer circumstance, or a suspicious number of women in and around this family possess enormous breasts, thick hips, and proportions bordering on deliberate exaggeration. Curious, isn't it?"

    menu:
        "*Let her go, say goodbye.*":



            $ nina_left_for_appointment = True
            $ nina_guilt_success = False
            jump lor1
        "*Try to get her to stay by making her feel guilty for leaving you with unanswered questions.*":

            $ nina_left_for_appointment = False
            play music2 my_audio["snee2"] loop fadein 2.0
            stop music fadeout 2.0

            voice my_audio["493"]
            nar "Ah... alright. I suppose we're doing this. Wonderful. Absolutely wonderful."
            voice my_audio["494"]
            nar "Nina is clearly a strong-minded woman, so an ordinary request won't be enough. We'll need something carefully chosen, something capable of slipping past all that inconvenient common sense."
            voice my_audio["495"]
            nar "Give me a moment. Searching the part of your brain responsible for manipulation, emotional leverage, and saying precisely the wrong thing with astonishing confidence."
            voice my_audio["496"]
            nar "Doo-doo-doo... no, that's childhood embarrassment. Da-da-da-doo... repressed insecurity. Bloody hell, there's quite a lot stored in here."
            voice my_audio["497"]
            nar "Ah! Here we are. Page seven of The Shameless Bastard's Guide to Making Other People Feel Responsible for Your Problems. Good Lord... you've even bookmarked it."
            voice my_audio["498"]
            nar "Your hint, then: Nina can tolerate filth, but not entitlement. Keep your need for answers beneath every dirty thought, admit your fear without insulting her, never decide what she wants, and whenever control is at stake, place it firmly in her hands."




    scene a238
    with medium_dissolve
    jump nina_guilt_opening

label nina_guilt_opening:

    menu:
        "How about you come upstairs to my room, cancel your appointment, and get naked for me instead?":




            $ memory_nina_pressured = True
            $ show_tooltip(n=32)


            nin "W-What!? You have some nerve!"
            nin "I stare at you like you've just stepped out of a nightmare I buried years ago, and somehow your first response is to ask me to take my clothes off?"
            nin "You're either stupid, shameless, or so young that you think a hard cock counts as an argument."
            nin "But since you clearly don't understand subtlety, let me be clear: if you want me to even consider going upstairs with you, you'll need a better reason than wanting to see my tits."

            jump nina_guilt_2

        "Of course. Run off to your appointment like every woman does when a guy actually needs something from her." if not nina_guilt_bad_opening_used:

            $ nina_guilt_bad_opening_used = True

            voice my_audio["499"]
            nar "What the fuck are you doing!?"
            voice my_audio["500"]
            nar "Oh, that's magnificent! Your grand strategy is to blame Nina for every woman who's ever disappointed you? Ha! I'm sure she'll find that irresistibly charming."
            voice my_audio["501"]
            nar "That won't make her feel guilty. It'll make you sound like a bitter little idiot who expects her to answer for women she has never even met."
            voice my_audio["502"]
            nar "Use what Nina actually did: she looked at you like your existence terrified her, admitted she knows something important, and then tried to leave you alone for hours with questions that may involve your life."
            voice my_audio["503"]
            nar "Make her feel responsible for the fear and confusion she created. Keep your desire obvious, but don't punish her for the sins of women who aren't even in the room. When you ACTUALLY get her upstairs, who cares just fuck her. Until then, try again. This is your only hint."

            jump nina_guilt_opening

label nina_guilt_2:

    menu:
        "The reason is your body. Big tits, big ass, that mouth, those legs. Don't act like you don't know exactly what you look like.":




            nin "Of course I know what I look like."
            nin "I've known longer than you've been alive, and I've dealt with men far more dangerous than you losing their minds over it."
            nin "But my body isn't a reason for me to cancel my day. It's a reason for you to learn self-control before you embarrass yourself worse than you already have."

            jump nina_guilt_failure
        "You just told me I matter enough to scare you, then told me to sit here alone for hours with no answers. So yeah, I want you upstairs, and yeah, I want you naked, but I also want to know why the hell you looked at me like I shouldn't exist.":


            nin "That was almost clever."
            nin "Crude, manipulative, and wrapped around a filthy little fantasy, but almost clever."
            nin "You heard the important part and grabbed onto it. I did react badly. I did leave you with questions I had no right to leave unanswered."
            nin "But don't think tossing fear and lust into the same sentence means I can't tell which one you're using to pull me closer."

            jump nina_guilt_3


label nina_guilt_3:

    menu:
        "Then come upstairs and separate them for me. Tell me what I am, then tell me whether a woman like you still remembers what it feels like to be wanted by someone who can't stop looking at her.":




            nin "A woman like me?"
            nin "Careful. You're close to sounding interesting, but you keep ruining it by talking like age turns a woman into a category."
            nin "I remember exactly what it feels like to be wanted. I remember what it feels like to be chased, touched, lied to, worshipped, and disappointed."
            nin "The question isn't whether I remember desire. The question is whether you're capable of wanting me without trying to punish me for making you wait."

            jump nina_guilt_4
        "Fine, then let's not pretend. I'm using both. I'm scared, I'm horny, and I want to bury my face between your thighs until you forget that appointment exists.":


            nin "At least that's honest."
            nin "Disgustingly honest, but honest."
            nin "Unfortunately, honesty doesn't automatically make you safe, and right now you sound less like a man asking for privacy and more like a boy daring himself to cross a line."

            jump nina_guilt_failure


label nina_guilt_4:

    menu:
        "Maybe I am trying to punish you. Maybe watching a woman with tits like yours walk away after dropping a mystery on me makes me feel like the joke is on me.":




            nin "Then grow up before you speak to me again."
            nin "My breasts have nothing to do with the fact that you're frightened, and dragging them into every sentence doesn't make your fear more legitimate."
            nin "It just makes you sound like you can't tell the difference between needing answers and needing to dominate the nearest woman in heels."

            jump nina_guilt_failure
        "I'm not trying to punish you. I'm trying not to sit here imagining every bad reason you might have for leaving, because if you scared yourself looking at me, then maybe I should be scared too.":


            nin "There it is."
            nin "That's the thing underneath all the vulgarity."
            nin "You think I'm leaving because I know something dangerous, and you're wondering whether I'll come back alone or with someone who can make your life very complicated."
            nin "That's not paranoia. Not entirely."
            nin "And because I made that fear worse, I suppose I don't get to act offended that you're using whatever weapons you have to keep me here."

            jump nina_guilt_5


label nina_guilt_5:

    menu:
        "Then stay. Come upstairs. Lock the door. Take off that respectable act and let me see the woman under it, even if all you do is tell me I'm an idiot with a hard-on.":




            nin "The respectable act, as you call it, has kept me alive, employed, wealthy, and out of the reach of men who thought they could talk me into mistakes."
            nin "But yes, you're an idiot with a hard-on."
            nin "You're also frightened, inconvenient, and connected to something I don't understand yet."
            nin "If I go upstairs with you, it won't be because you asked to see me naked. It'll be because I owe you enough truth to keep you from doing something reckless."

            jump nina_guilt_6
        "I bet nobody's fucked you right in years. That's why you're so tense. A woman built like you shouldn't be wasting herself on appointments.":


            nin "Don't confuse my restraint with deprivation."
            nin "You have no idea who I've taken to bed, how recently, how loudly, or how well."
            nin "And after that little insult, you certainly won't be added to the list."

            jump nina_guilt_failure


label nina_guilt_6:

    menu:
        "Truth is fine, but don't act like you don't feel the heat in this. You keep looking at me like you're deciding whether to slap me or kiss me.":




            nin "That's exactly the kind of sentence that makes me want to do neither."
            nin "You're inventing permission out of my expression because it flatters you."
            nin "If I look conflicted, it's because the situation is dangerous, not because your mouth has magically undone fifty-four years of judgment."

            jump nina_guilt_failure
        "Then set the rules. Door open or closed, lights on or off, across the room or close enough that I can smell your perfume. I won't touch you unless you tell me to, but I want to.":


            nin "That's better."
            nin "Still filthy, still arrogant, but better."
            nin "You're giving me the rules instead of trying to steal them, and that matters."
            nin "If I come with you, I'm not promising skin, sex, or whatever depraved little scene you've already built in your head."
            nin "I'm promising a private conversation. If anything else happens, it'll happen because I decide it does."

            jump nina_guilt_7


label nina_guilt_7:

    menu:
        "Fine. Your decision. But if you do decide it, I want you to know exactly what I'm thinking: I want your dress on the floor, your legs open, and me on top of you.":




            nin "Jesus!"
            nin "You really are committed to making every reasonable sentence drag its knuckles through the gutter, aren't you?"
            nin "But you said the important part first: my decision."
            nin "Keep that part in your head, preferably louder than the part currently picturing me naked, and we may survive ten minutes alone without me slapping sense into you."

            jump nina_guilt_final
        "Your decision, sure. But don't waste my time pretending you'll come upstairs just to talk when we both know how this ends.":


            nin "No, we don't."
            nin "And the fact that you think you can decide the ending before I even agree to the beginning is exactly why I shouldn't go anywhere with you."
            nin "Desire isn't destiny, honey. It's just desire. Learn the difference."

            jump nina_guilt_failure


label nina_guilt_final:

    menu:
        "Your rules. I won't touch you unless you ask me to. But if you do ask, I'm going to make sure you remember exactly why skipping that appointment was worth it.":




            nin "That's still obscene."
            nin "But at least it's obscene in the shape of an agreement instead of a demand."
            nin "You're going to keep your hands visible, your voice down, and that filthy mouth under control until I decide whether it has any use besides making trouble."
            nin "I'll cancel the appointment. We'll go upstairs. We'll talk."
            nin "And if you mistake my curiosity for permission, you'll learn very quickly that age hasn't made me fragile."

            jump nina_guilt_success
        "Good. Once we're alone, I'll get you out of those clothes and show you what that body's really for.":


            nin "And there it is."
            nin "One step from getting what you asked for, and you still couldn't resist turning me into something to be used."
            nin "I was willing to give you privacy. I was even willing to tolerate the desire."
            nin "But I won't reward entitlement just because it learned how to wear a little vulnerability."

            jump nina_guilt_failure


label nina_guilt_success:

    $ nina_left_for_appointment = False
    $ nina_guilt_success = True
    $ memory_nina_patience = True
    $ show_tooltip(n=31)

    scene a239_8
    with medium_dissolve

    nin "I'm going to regret this. I can already feel it."
    nin "Give me a moment to cancel my appointment, and then you can show me where your room is."
    nin "If anyone asks, we're discussing a private family matter. Nothing more."
    nin "And before you say something stupid, no, that doesn't mean I'm agreeing to anything else."

    scene a239_9
    with medium_dissolve

    nin "All right. Lead the way."
    nin "Wipe that satisfied look off your face before I change my mind."
    nin "You got ten minutes, privacy, and my attention."
    nin "Don't make the mistake of thinking you've gotten my clothes, my body, or my obedience."

    jump nina_guilt_end


label nina_guilt_failure:

    $ nina_left_for_appointment = False
    $ nina_guilt_success = False
    $ memory_nina_crossed_line = True
    $ show_tooltip(n=33)

    scene a239_10
    with medium_dissolve

    nin "No. I'm done with this conversation."
    nin "You had chances to speak to me like a person, and every time the door opened, you shoved your worst instincts through it."
    nin "Wanting me isn't the problem. Being young isn't the problem. Having a filthy mouth isn't even the problem."
    nin "The problem is that you keep confusing pressure with seduction, and I don't have the patience to teach you the difference today."

    scene a239_11
    with medium_dissolve

    nin "Don't follow me."
    nin "Don't try to stop me."
    nin "And while I'm gone, think very carefully about how close you came to getting exactly what you wanted before you ruined it."

    $ nina_guilt_success = False
    jump lor1

label nina_guilt_end:

    scene black
    with slowfade

    pause 3.0

    voice my_audio["504"]
    nar "Against reason, good judgment, and several increasingly obvious warnings... you actually succeeded. Nina cancelled her appointment and followed you upstairs."
    voice my_audio["505"]
    nar "Once inside your room, she gathers herself and calmly asks where the two of you should begin. Her voice turns serious, the sort of serious that usually arrives moments before life-changing information."
    voice my_audio["506"]
    nar "Naturally, you stop her. Not to ask why seeing you frightened her, or what she knows about your father, but to point out one far more pressing concern: why the hell are her clothes still on?"
    voice my_audio["507"]
    nar "Nina asks what you mean. You then remove any remaining possibility of misunderstanding and tell her, plainly, that you brought her upstairs because you want to fuck her. She closes her eyes, tilts her head toward the ceiling... and releases one long, exhausted sigh."

    scene ninastrip2
    with ffast_dissolve
    if not persistent.seen_ninastrip2:


        $ config.allow_skipping = False
        $ renpy.pause(14, hard=True)
        $ config.allow_skipping = True


        $ persistent.seen_ninastrip2 = True
        $ renpy.save_persistent()
    else:



        pause 14

    scene black
    with slowfade

    scene a258
    with medium_dissolve

    nin "Well? There you are. You've seen me naked. Are you finally satisfied?"
    nin "Take a good look, get it out of your system, and then we're going to have the conversation you dragged me up here to have."
    nin "And before your imagination runs completely wild, remember that I am a married woman. I realise that detail may not matter to you, but it matters enough to be said aloud."

    menu:
        "God, you're so fucking hot, Nina. Where have you been all my life you sexy woman?":




            nin "Where have I been? Living a perfectly functional life away from men who ask questions like that."
            nin "This isn't some grand reward you've unlocked because you successfully annoyed me upstairs."
            nin "And lift your eyes slightly. My breasts aren't going to answer you."
        "Jesus Christ... turn around for me. I want to see all of you.":


            nin "No. You wanted me naked, and against every sensible instinct I possess, I indulged you."
            nin "That does not mean you suddenly get to pose me like some obedient little doll."
            nin "You can see more than enough from where I'm standing, and judging by your expression, you already have."
        "Married doesn't bother me. Your husband isn't here, and I am.":


            nin "Yes, darling, I had managed to notice both of those things."
            nin "But don't mistake me standing naked in front of you for me forgetting that my husband exists."
            nin "Although something tells me moral complications have never frightened you nearly as much as an unattractive woman might."

    scene a260
    with medium_dissolve

    nin "Before this goes any further, you need to understand that I haven't promised you sex."
    nin "I came upstairs because you deserved answers, and because leaving you frightened and confused after what I said would have been irresponsible."
    nin "Whatever else may or may not happen in this room, I am still married, there are consequences attached to this, and I need to know that you understand..."

    scene a263
    with medium_dissolve

    voice my_audio["508"]
    nar "Nina continues speaking. Something about marriage, boundaries, consequences... all perfectly sensible subjects that would ordinarily deserve your full attention."
    voice my_audio["509"]
    nar "Unfortunately, your attention abandoned the conversation somewhere around the second mention of her husband and wandered directly toward the couch."
    voice my_audio["510"]
    nar "While Nina attempts to establish the moral and emotional complexity of the situation, you're estimating the width of the cushions and deciding precisely how many positions they could reasonably support."
    voice my_audio["511"]
    nar "Her words dissolve into a distant, meaningless hum. As far as you're concerned, the important conversation already happened: she came upstairs, removed her clothes, and hasn't left yet."

    scene a264
    with medium_dissolve

    voice my_audio["512"]
    nar "The couch appears sturdy, conveniently positioned, and just wide enough for the thoroughly indecent plans currently assembling themselves inside your head."
    voice my_audio["513"]
    nar "Then your eyes return to Nina. Those enormous breasts, those thick hips, and a body that makes the word 'older' feel like a completely irrelevant technicality."
    voice my_audio["514"]
    nar "You begin arranging the evening in your imagination: where you'll put her, how you'll take her, and exactly how loudly you'll make this supposedly respectable married woman forget every objection she just raised."
    voice my_audio["515"]
    nar "Then the distant humming stops. Nina has fallen silent. More importantly, she has followed your stare to the couch... and realised you haven't heard a single bloody word."

    scene a266
    with medium_dissolve

    nin "You haven't been listening to me at all, have you?"
    nin "Fine. Go and sit on the couch before your eyes burn a hole through it."
    nin "We'll figure out what happens from there, but I still have things to tell you, and this time, you're going to make an effort to listen."

    menu:
        "Alright, I'll sit. Just don't drag this out longer than necessary before we get to the inevitable fucking.":




            nin "There is nothing inevitable about you fucking me."
            nin "At present, the only inevitable thing is my rapidly declining patience."
            nin "Sit down, close your mouth, and allow reality one final opportunity to catch up with your imagination."
        "Fine, but we both know we're not going over to that couch just to talk.":


            nin "You truly regard conversation as an irritating obstacle between yourself and a woman's legs, don't you?"
            nin "We are going over there because I would prefer not to conduct this entire disaster while standing naked in the middle of the room."
            nin "Anything beyond talking remains entirely my decision, regardless of what your cock has apparently decided on my behalf."
        "Lead the way. But we're fucking soon.":


            nin "One more sentence like that and the couch will be where you spend the evening alone."
            nin "You managed to get me upstairs by respecting the fact that I control what happens next."
            nin "Try to remember that before your arrogance ruins what little curiosity I still have left."


    scene black
    with slowfade

    pause 1.0

    scene a274
    with ffade

    voice my_audio["516"]
    nar "You move across the room and settle onto the couch, fully expecting Nina to follow. She doesn't."
    voice my_audio["517"]
    nar "Instead, she remains standing directly in front of you, apparently determined to continue playing hard to get, or, as she would probably describe it, attempting to have one meaningful conversation."
    voice my_audio["518"]
    nar "She begins speaking again, but concentration has become impossible. Your eyes move from her enormous breasts to her thick body, then upward to her lips before beginning the journey all over again."
    voice my_audio["519"]
    nar "Nina notices every wandering glance. She tries to continue, yet each sentence dies beneath the unmistakable hunger written across your face."
    voice my_audio["519_1"]
    nar "And yet, despite every vulgar remark, wandering glance, and perfectly reasonable opportunity to walk away... Nina hasn't left. Most women would have abandoned this disaster several insults ago, but she remains standing in front of you."
    voice my_audio["519_2"]
    nar "More interestingly, you aren't the only one staring. Her eyes have wandered across your face, shoulders, and body far too many times to be accidental. Whatever else Nina may think of you, she quite obviously finds you extremely attractive."
    voice my_audio["520"]
    nar "Eventually, her shoulders fall and what remains of her patience collapses with them. She releases another exhausted breath and finally says, 'Alright... just fuck me already. Let's get this over with.'"
    voice my_audio["521"]
    nar "Those words strike like lightning. Your pulse surges, every muscle tightens, and you lean forward, ready to rise from the couch and claim precisely what you've been thinking about since she removed her clothes."
    voice my_audio["522"]
    nar "However, before you can even lift yourself from the cushions... suddenly..."

    stop music2

    scene ninaloveyou
    with ffast_dissolve
    call godson_locked_cutscene ("gui/ninaloveyou.webm", 309.0, "seen_ninaloveyou") from _call_godson_locked_cutscene_11

    $ unlock_gallery_scene("nina")

    scene a276
    with medium_dissolve
    play music my_audio["apartment4"] loop fadein 2.0

    voice my_audio["523"]
    nar "Wait one second! Before you open your mouth and turn this already catastrophic afternoon into something legally recognised, let's examine what just happened."
    voice my_audio["524"]
    nar "This married woman, more than twice your age and acquainted with you for barely a day, has declared that she loves you and wants you as her boyfriend immediately after you gave her the fuck of her life."
    voice my_audio["525"]
    nar "Perhaps she's discovered her soulmate. Or perhaps her legs are still trembling so violently that her heart and brain have temporarily stopped exchanging reliable information."
    voice my_audio["526"]
    nar "Or perhaps, we should exercise some caution. Nina may believe every word she's saying, but declarations made while her legs are still shaking and the room still smells like sex may not survive the cold, unforgiving light of tomorrow morning."
    voice my_audio["527"]
    nar "Then again... we could simply tell her we love her. Leap headfirst into a completely unplanned romance with a married woman more than twice your age after one spectacular fuck. Sensible? Absolutely not. But that doesn't necessarily make it wrong."

    menu:
        "I'll need some time to respond back to that.....":




            scene a284
            with medium_dissolve

            $ memory_nina_is_boyfriend = False
            $ memory_nina_is_not_boyfriend = False
            $ memory_nina_hates_you = False
            $ memory_nina_wait_response = True
            nin "..."
            nin "I... I understand."
            nin "I know I kind of put you on the spot, and that's not fair."
            nin "Take all the time you need. I'd rather hear how you truly feel than have you say something you don't mean."
            nin "Just... promise me you'll give me an answer when you're ready."
            nin "Why don't you go out first and make sure everything's okay?"
            nin "I still have other things I need to do today, so as soon as you tell me it's clear, I need to leave. But I promise we'll talk more later, my love!"
            $ show_tooltip(n=36)

            nin "I'll wait here until you come back."
            jump mchenrytalk
        "I....love you too.":


            $ memory_nina_is_not_boyfriend = False
            $ memory_nina_is_boyfriend = True
            $ memory_nina_wait_response = False
            $ memory_nina_hates_you = False
            nin "....."
            nin "........"
            $ show_tooltip(n=37)


            scene ninaloveyou4
            with ffast_dissolve
            if not persistent.seen_ninaloveyou4:


                $ config.allow_skipping = False
                $ renpy.pause(15, hard=True)
                $ config.allow_skipping = True


                $ persistent.seen_ninaloveyou4 = True
                $ renpy.save_persistent()
            else:



                pause 15


            menu:
                "How about a picture together to celebrate?":




                    scene a284
                    with medium_dissolve

                    nin "A picture?"
                    nin "Actually... yes. Let's do that. I want something that proves this moment really happened."
                    nin "And when I'm not around, you can look at it and remember exactly who that filthy imagination of yours belongs to."
                    nin "Come on, we'll take it over there."

                    scene black
                    with slowfade

                    scene ninaloveyou2
                    with ffade
                    if not persistent.seen_ninaloveyou2:


                        $ config.allow_skipping = False
                        $ renpy.pause(14, hard=True)
                        $ config.allow_skipping = True


                        $ persistent.seen_ninaloveyou2 = True
                        $ renpy.save_persistent()
                    else:



                        pause 14

                    scene black
                    with slowfade

                    pause 3.0

                    nin "Hey babe. One quick thing before I go...."
                    nin "I'm....pretty sure we made a lot of noise...."
                    nin "Why don't you go out first and make sure everything's okay?"
                    nin "I still have other things I need to do today, so as soon as you tell me it's clear, I need to leave. But I promise we'll talk more later, my love!"
                    $ show_tooltip(n=36)

                    nin "I'll wait here until you come back."
                    jump mchenrytalk
        "Sorry Nina, this was just a one time thing. It's time to leave, right now.":


            $ memory_nina_is_boyfriend = False
            $ memory_nina_is_not_boyfriend = True
            $ memory_nina_wait_response = False
            $ memory_nina_hates_you = True
            nin "......"
            nin "........."
            nin "Are you....serious?"

            menu:
                "I'm serious. Get out of here. We're done. I just wanted to fuck.":



                    pass
                "I'm down to talk about a friends-with-benefits situation later. But for now, get out.":

                    pass
                "Yeah, I'm serious. You can leave now. I already got my nut off so I'm good to go. I just couldn't resist that hott body of yours.":

                    pass

            nin "...."
            nin "........."
            $ show_tooltip(n=38)


            scene ninaloveyou3
            with medium_dissolve
            if not persistent.seen_ninaloveyou3:


                $ config.allow_skipping = False
                $ renpy.pause(15, hard=True)
                $ config.allow_skipping = True


                $ persistent.seen_ninaloveyou3 = True
                $ renpy.save_persistent()
            else:



                pause 15


            scene a285
            with medium_dissolve

            hen "....."
            hen "........."

            scene a286
            with medium_dissolve

            hen "......."
            hen "........."

            scene a287
            with medium_dissolve

            hen "You're in big trouble, mister. MAJOR trouble."
            hen "Get out here so we can talk, now."
            mc "......."
            jump mchenrytalk

label mchenrytalk:

    scene black
    with slowfade
    play sound my_audio["dco"] noloop

    pause 2.0

    scene a288
    with slowfade

    hen "Do you have any idea what you just put me through!? I could hear the two of you from the other side of the damn house!"
    hen "Martha thought somebody was hurt, Marnie doesn't know where to look, and Lorraine's about ready to rip this door off its hinges!"
    hen "You didn't just make a little noise. You had the whole damn house thinking something terrible was happening up here!"

    scene a289
    with medium_dissolve

    hen "You're lucky Jennifer and Yuni aren't home. If they were here, this would've been ten times worse!"
    hen "What the FUCK were you thinking!? If you're gonna do something like that, at least remember you're not the only two people in this house!"
    hen "These walls don't magically turn soundproof just because the two of you forgot everybody else existed!"

    scene a290
    with medium_dissolve

    hen "Lorraine said it was disrespectful, and honestly, she's right. Martha was scared half to death because she thought somebody had gotten hurt."
    hen "Now I have to go back downstairs and explain why the furniture was shaking while Nina was screaming loud enough to wake the dead!"
    hen "And another thing!"

    scene a291
    with medium_dissolve

    hen "..."
    hen "......"
    hen "I understand...."
    hen "Damn it! Look... I was young once too, and I wasn't exactly an angel either."

    menu:
        mc ""
        "Wait... what? I thought you were about to throw me out.":



            hen "Believe me, it crossed my mind more than once while I was standing outside that door."
            hen "But throwing you out on the street over one incredibly stupid decision would be going a little too far."
            hen "Don't look so relieved yet. There are conditions attached to me letting this go."
        "Are you telling me you understand why it happened?":


            hen "I can understand how a young man loses his head without approving of what he did."
            hen "When I was your age, I had my share of wild nights. I'd like to think I paid a little more attention to where I was, but I wasn't always that smart."
            hen "I'd be lying if I stood here and acted like excitement never got the better of my common sense."
        "So this speech is coming from personal experience?":


            hen "Now hold on. You don't need to hear stories about what I was doing when I was your age."
            hen "Let's just say I made plenty of mistakes, learned from them, and got pretty good at recognizing them in other people."
            hen "And unfortunately for you, I recognized every damn one of them tonight."

    scene a292
    with medium_dissolve

    hen "Look, I'm mad as hell right now, but I didn't forget what you did when my boss was in that room with Marnie."
    hen "No matter what I said, you did the right thing. You could have said no and walked away from my request, which I assume would've been a whole lot easier."
    hen "I hate saying this while I'm still pissed at you, but what you did meant a lot to me."

    scene a293
    with medium_dissolve

    hen "I also told you I owed you one, and when I give somebody my word, I mean it."
    hen "So this is me paying you back. I'll do what I can to make this whole mess go away."
    hen "But after this, we're even. Don't come looking for another favor tomorrow."

    scene a294
    with medium_dissolve

    hen "I'll tell everybody Nina got sick, knocked over some furniture, and you stayed with her until she felt better."
    hen "If they ask about all the yelling, I'll say she panicked and that the rest is private. If it comes from me, hopefully they'll have enough sense to leave it alone."
    hen "They might not believe every word, but they'll believe enough to let it go, especially after Lorraine cools down."

    scene a295
    with medium_dissolve

    hen "But listen to me, because I'm only saying this once. Do not EVER put me in this position again."
    hen "Next time, I'm not lying for you, calming everybody down for you, or getting between you and Lorraine when she comes looking for blood."
    hen "Whatever you do behind a closed door is your business. The second the whole house can hear it, it becomes everybody's business. You understand me?"

    scene a296
    with medium_dissolve

    menu:
        mc ""
        "Understood. It won't happen again.":



            hen "Good. That's the first sensible thing you've said since you walked into this hallway."
            hen "Keep that promise, and neither one of us will ever have to suffer through this conversation again."
            hen "I appreciate you taking me seriously."
        "Yeah, I got it. We'll keep it down next time.":


            hen "That's not exactly what I wanted to hear, but it's probably the most honest answer I'm gonna get."
            hen "Just make sure 'keeping it down' means nobody downstairs starts counting how many times the bed hits the wall."
            hen "I'm trusting you to use a hell of a lot more common sense next time."
        "No promises, but I'll try not to shake the entire house again.":


            hen "You really can't help yourself, can you? I'm doing you a favor, and you're still finding ways to get on my nerves."
            hen "I'll take that answer only because I don't feel like standing here arguing with you until sunrise."
            hen "You'd better try real hard, because my generosity isn't surviving a second performance."

    scene a297
    with medium_dissolve

    hen "Anyway, that's enough of this. It's getting late, and you need to start getting ready for the party."
    hen "I know you didn't bring much with you, so if you don't have anything decent to wear, come find me. I should have something around here that'll fit you."
    hen "Now go get dressed, and for the love of God, try not to cause another damn crisis before the party even starts."
    jump lor1
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

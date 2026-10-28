label ch2ep2:
    show screen day_saturday with dissolve
    play music ["<from 41 to 141>audio/AHeartbeatApart.mp3"] fadein 2
    show ch2ep2intro
    with dissolve
    pause 56
    scene white
    with dissolve
    pause 1.0
    stop music fadeout 10
    scene black
    with Dissolve(3.0)
    with fade
    $ renpy.sound.set_volume(0.2, 1.0)
    play sound traffic fadein 3 loop
    $ phone_time_add(hours=2)
    scene ch2ep2_1
    with dissolve
    pause
    scene ch2ep2_2
    with dissolve
    f "You guys better pick up the pace. I'm about to close up."
    scene ch2ep2_3
    with dissolve
    mc "You're not tagging along?"
    f "Nah... meeting up with sis. We're grabbing dinner."
    mc "Gotcha."
    scene ch2ep2_4
    with dissolve
    e "..."
    scene ch2ep2_5
    with dissolve
    f "..."
    scene ch2ep2_6
    with dissolve
    f "Where'd you two run off to, anyway?"
    scene ch2ep2_7
    with dissolve
    mc "... *shrugs*"
    scene ch2ep2_8
    with dissolve
    e "That old freight depot. Harlow Street."
    f "The one that's supposed to be abandoned?"
    e "Supposed to be. Yeah."
    f "And?"
    e "And we found nothing."
    f "Ain't that the usual, though?"
    e "Trucks were there, alright. But by the time we showed up? Nothing. Only tire marks and some fuel stains."
    f "So they cleared out?"
    e "Couldn't tell you. Either way, that's a few hours of my life I'm not getting back."
    scene ch2ep2_9
    with dissolve
    mc "..."
    f "That's... uhh... rough."
    e "... Wasn't even a solid lead. Went to check it out anyway..."
    f "You think someone tipped them off or something?"
    e "I don't know. Or maybe [mc]'s right and we're just chasing ghosts at this point."
    f "Hey, at least you went. Better than sitting around wondering what if, right?"
    mc "..."
    scene ch2ep2_10
    with dissolve
    e "Yeah... I guess..."
    f "Well? What do I even say? I don't know jack about detective stuff..."
    f "But just... don't brood all night, okay? You reek of diesel and disappointment right now."
    e "I—"
    play sound2 cloth2
    play sound3 chairdrag
    scene ch2ep2_11
    pause
    scene ch2ep2_12
    with dissolve
    pause
    scene ch2ep2_13
    with dissolve
    e "Really?"
    mc "You heard the lady. Quit brooding."
    scene ch2ep2_14
    with dissolve
    mc "Oh. Tell your girl she's getting a pay cut."
    f "Huh? What for?"
    mc "Bailing on you once, forgivable. Twice? That's not gonna fly. If she pulls it again, cut her loose."
    f "Fine, fine... You got it, boss."
    mc "Good."
    scene ch2ep2_15
    with dissolve
    mc "Alright, we're heading out."
    f "Yeah, take care."
    scene ch2ep2_16
    with dissolve
    e "You guys have coffee?"
    f "Bro... quit drinking coffee like it's some kind of anti-anxiety med. We got colas, though."
    e "Mm... I'm good."
    $ renpy.sound.set_volume(1.0, 1.0)
    scene ch2ep2_17
    with dissolve
    e "Hey, wasn't that a little harsh? Maybe the girl's going through something."
    scene ch2ep2_18
    with dissolve
    mc "Easy. Since when do you question the call if it's by the book?"
    scene ch2ep2_19
    with dissolve
    mc "Besides, it's not about the girl. It's about Freya."
    if emmaroute:
        e "Why? What about her?"
        mc "Just... trying to teach her not to be me."
        e "Which part?"
        scene ch2ep2_20
        with dissolve
        pause
        e "Is that supposed to help me guess?"
        scene ch2ep2_21
        with dissolve
        mc "*shaking his head* You're even cuter when you're this clueless, Em."
        scene ch2ep2_22
        with dissolve
        pause
        play sound2 cardooropen
        scene ch2ep2_23
        with dissolve
        mc "Ma'am?"
        e "Thanks. I'll let you off the hook for good behavior this time."
        mc "Why, I appreciate it, detective."
    stop sound fadeout 2

    scene black
    with dissolve
    with fade

    play sound2 nightambience loop fadein 2
    play sound cooking loop fadein 2
    scene ch2ep2_24
    with dissolve
    mc "..."
    scene ch2ep2_25
    with dissolve
    mc "Where the hell is everyone?"
    k "Sky's upstairs. The rest? Not the faintest clue."
    k "You two eat yet?"
    stop sound fadeout 1
    play sound3 plating
    scene ch2ep2_26
    with dissolve
    mc "We grabbed some snacks, but I'll take a plate."
    e "I'll eat."
    scene ch2ep2_27
    with dissolve
    k "Alright, come get your food."
    scene ch2ep2_28
    with dissolve
    k "Sky? Dinner's ready!"
    play sound stairsrundown
    scene ch2ep2_29
    with dissolve
    s "Whoops! Sorry, coming!"
    play sound3 running_flipflops loop
    scene ch2ep2_30
    with dissolve
    pause
    scene ch2ep2_31
    with dissolve
    pause
    play sound3 chairdrag
    scene ch2ep2_32
    with Dissolve(0.2)
    mc "Whoa!"
    e "What happened to you?"
    play sound3 chair3
    scene ch2ep2_33
    with dissolve
    mc "All-nighter?"
    s "All-nighter."
    scene ch2ep2_34
    with dissolve
    s "Haven't slept at all, unfortunately. I had to cover Aine's to-dos. She's tied up with something else."
    scene ch2ep2_35
    with dissolve
    yt "Is she still working on my tasks?"
    if allornothingroutev2:
        scene ch2ep2_36
        with dissolve
        pause
        scene ch2ep2_37
        with dissolve
        pause
    scene ch2ep2_38
    with Dissolve(0.1)
    k "So..."
    if allornothingroutev2:
        scene ch2ep2_39
        pause
    scene ch2ep2_40
    with dissolve
    mc "Yeah?"
    k "How did it go?"
    mc "Uh... how did what go?"
    k "*soft laugh* Whatever's got you two smelling like diesel."
    mc "That obvious?"
    scene ch2ep2_41
    with dissolve
    s "Oh yeah. I thought something was off when I came down."
    k "Mm-hm. You came in looking like you spent the day crawling through a scrapyard."
    mc "*chuckles* Close enough."
    scene ch2ep2_42
    with dissolve
    e "We were following up on something. Wasn't a solid lead, and sure enough, it didn't pan out."
    k "Work?"
    e "Yeah. Work."
    k "Mm."
    k "Well, eat up. Whatever you went through, you look like you need it."
    e "... Thanks."
    scene ch2ep2_43
    with dissolve
    s "W-Was it dangerous?"
    e "*sighs* No. Just... a waste of time..."
    mc "What did Freya tell you again?"
    e "Not to brood over it, I know..."
    scene ch2ep2_44
    with dissolve
    mc "You sound curious, Sky."
    s "Oh! No, no. Not really. It's just..."
    s "Well... I was more interested in the thrill of it. You know..."
    s "I've never really..."
    s "Never mind. Probably just the sleep deprivation talking."
    mc "Make sure you get some proper rest tonight."
    s "*laughs* I hope so."
    scene ch2ep2_45
    with dissolve
    k "..."
    scene ch2ep2_46
    with dissolve
    e "Mm! This is so good. I need to stop eating before dinner."
    k "Glad you like it. Want some wine with that?"
    e "I'm good."
    k "Suit yourself."
    stop sound2 fadeout 4
    play sound cardriveinterior fadein 4 loop
    scene black
    with dissolve
    scene ch2ep2_47
    with dissolve
    pause
    scene ch2ep2_48
    with dissolve
    m "You okay?"
    scene ch2ep2_49
    with dissolve
    g "No. I'd be lying if I said I was."
    m "Want me to drive?"
    g "I'm fine."
    stop sound fadeout 1
    play sound2 traffic2 loop
    play sound4 jesscarroar
    scene ch2ep2_50
    with dissolve
    play sound3 car_idle loop
    pause
    stop sound3 fadeout 1
    stop sound2 fadeout 1
    play sound cardriveinterior fadein 1 loop
    scene ch2ep2_51
    with dissolve
    m "You haven't blinked in a while."
    g "I AM blinking, Moon! Just quit asking if I'm fine!" with hpunch
    m "... Okay."
    stop sound fadeout 1
    play sound2 traffic2 fadein 1 loop
    play sound3 car_idle fadein 1 loop
    scene ch2ep2_52
    with dissolve
    g "Sorry."
    stop sound3 fadeout 1
    stop sound2 fadeout 1
    play sound cardriveinterior fadein 1 loop
    scene ch2ep2_53
    with dissolve
    g "Claire didn't even sugarcoat it."
    m "She never does. Doesn't see the point."
    g "And she said there's no treatment."
    m "She said there's no fix."
    g "You know that's the same thing, right?"
    m "No, it's... worse..."
    play sound4 clench
    scene ch2ep2_54
    with dissolve
    pause
    scene ch2ep2_55
    with dissolve
    m "I don't know how long I can keep this up, Gwen."
    m "This isn't... I don't know what I'm supposed to do..."
    g "Maybe you should tell him to stop using it?"
    m "No, I told you, it doesn't matter because that's not the problem."
    scene ch2ep2_56
    with dissolve
    g "..."
    g "I'm sorry I couldn't find anyone. I just burned nine months away from him. I should've stayed."
    m "It wasn't a waste. You tried."
    g "Yeah, but at what cost?"
    stop sound fadeout 1
    play sound2 traffic2 fadein 1 loop
    play sound3 car_idle fadein 1 loop
    scene ch2ep2_57
    with dissolve
    g "You think he knows?"
    m "I think he knows something. But not how far it goes."
    scene ch2ep2_58
    with dissolve
    pause
    stop sound3 fadeout 1
    play sound4 carmoving loop
    scene ch2ep2_59
    with dissolve
    m "We should just tell him, Gwen."
    g "And watch him turn it into a schedule?"
    m "..."
    g "He'd start planning around it. Us. Work. The future. Like it's... another fucking deadline."
    g "You know him. He won't stop there."
    m "And if we don't tell him, he'll keep pretending there's time."
    g "Is there?"
    m "I don't know."
    scene ch2ep2_60
    with dissolve
    pause
    m "*exhales* What are you going to do?"
    g "Be with him."
    g "... So should you."
    stop sound4 fadeout 1
    stop sound2 fadeout 1
    play sound cardriveinterior fadein 1 loop
    scene ch2ep2_61
    with dissolve
    g "Hey, Moon."
    m "Yeah?"
    g "If this gets worse—"
    m "—I'll be there."
    stop sound fadeout 2

    scene black
    with dissolve
    with fade

    play sound camcorder_movement
    scene ch2ep2_62
    with dissolve
    pause
    play sound2 camcorder_fastforward loop
    scene ch2ep2_63
    with dissolve
    k "(Really? You actually went and got it?)"
    jov "(Hey, don't give me a hard time. You know I've been wanting one.)"
    k "(Ah, [mc]! Don't do that!)"
    play sound camcorder_glitch
    scene ch2ep2_64
    with dissolve
    jov "(It's been a while since I last touched this thing. Life's been... well, a bit of a whirlwind—work and everything else.)"
    jov "(Oh, right! Klara finally gave birth to Sky.)"
    jov "(She's been with us for a year now, and she's always trailing behind [mc]. Those two are practically inseparable. It's the sweetest thing.)"
    k "(Can you put the camera down for a bit? You've been staring at that thing all day!)"
    k "(Sky needs you, and I need help in the kitchen, too!)"
    jov "(Okay, okay, just a sec!)"
    play sound camcorder_glitch
    scene ch2ep2_65
    with dissolve
    k "(Awww! Aren't they adorable?)"
    jov "(Here we are, [mc] trying to teach Sky to walk. He's barely got it down himself, but he's so eager to help her.)"
    jov "(Their laughter, their games are full of love.)"
    jov "(Watching [mc] help Sky, and her looking up to him like he's a superhero—it's perfect.)"
    jov "(Capturing these moments feels like I'm keeping something precious forever.)"
    jov "(I just hope we can keep these good times going...)"
    play sound camcorder_glitch
    scene ch2ep2_66
    with dissolve
    jov "(This entry's hard... [mc]'s been feeling sick... a lot...)"
    jov "(The coughing doesn't stop, and it's not just a regular cold...)"
    jov "(He's also been clumsy, tripping over nothing, which isn't like him...)"
    jov "(And he looks pale, even though we've been outside a lot. It's got to be something more...)"
    jov "(You can tell, he's not his usual self...)"
    jov "(It's hard seeing him try to keep up with Sky but get tired so quickly...)"
    jov "(He's frustrated because he can't keep going like she does...)"
    jov "(The nights are tougher. His coughing keeps us all up...)"
    jov "(I stay with him, holding his hand, until he falls asleep...)"
    jov "(Even in his sleep, he's restless...)"
    jov "(I keep hoping it'll get better, but deep down, I'm worried...)"
    jov "(We've got doctor appointments lined up. I'm trying to be strong for Klara and Sky, but I'm scared. What if...)"
    jov "(*sighs* I need to stop here...)"
    play sound nightambience2 fadein 2 loop
    play sound2 camcorder_movement
    scene ch2ep2_67
    with dissolve
    pause
    play sound3 casepickup2
    scene ch2ep2_68
    with dissolve
    pause
    if allornothingroutev2:
        play sound2 cloth
        scene ch2ep2_69
        with dissolve
        pause
        play sound3 phonemessage
        scene ch2ep2_70
        with dissolve
        pause
        play sound2 chair
        scene ch2ep2_71
        with dissolve
        pause 0.3
        $ phone_start()
        $ switch_channel_view("sky_dm")
        show screen phone_ui
        $ quick_menu = False
        $ hide_all_phone_channels("sky_dm")
        $ lock_phone_screen()
        $ phone_stamp_rel("sky_dm")
        $ send_phone_message("Sky", "[mc]!", "sky_dm")
        $ send_phone_message(phone_config["phone_player_name"], "???", "sky_dm")
        $ send_phone_message(phone_config["phone_player_name"], "The hell?", "sky_dm")
        $ send_phone_message(phone_config["phone_player_name"], "Since when do you text?", "sky_dm")
        $ phone_pause(0.5)
        $ send_phone_message("Sky", "ik ik", "sky_dm")
        $ phone_pause(1.0)
        $ send_phone_message("Sky", "but had 2 say smth", "sky_dm")
        $ send_phone_message(phone_config["phone_player_name"], "About?", "sky_dm")
        $ phone_pause(0.5)
        $ send_phone_message("Sky", "dinner!!", "sky_dm")
        $ phone_pause(1.0)
        $ send_phone_message("Sky", "when mom asked how it went", "sky_dm")
        $ phone_pause(1.0)
        $ send_phone_message("Sky", "thought she meant US", "sky_dm")
        $ send_phone_message(phone_config["phone_player_name"], "Wait, what?", "sky_dm")
        $ phone_pause(0.5)
        $ send_phone_message("Sky", "was SWEATING", "sky_dm")
        $ phone_pause(0.5)
        $ send_phone_message("Sky", "full panic mode", "sky_dm")
        $ phone_pause(0.5)
        $ send_phone_message("Sky", "u didnt notice???", "sky_dm")
        $ send_phone_message(phone_config["phone_player_name"], "I thought you were just tired.", "sky_dm")
        $ phone_pause(0.2)
        $ send_phone_message("Sky", "was", "sky_dm")
        $ phone_pause(1.0)
        $ send_phone_message("Sky", "but also dying inside", "sky_dm")
        $ phone_pause(1.0)
        $ send_phone_message("Sky", "she kept looking @ me", "sky_dm")
        $ phone_pause(0.5)
        $ send_phone_message("Sky", "then @ u", "sky_dm")
        $ phone_pause(0.5)
        $ send_phone_message("Sky", "then back @ me", "sky_dm")
        $ send_phone_message(phone_config["phone_player_name"], "You're overthinking it, Sky.", "sky_dm")
        $ phone_pause(0.3)
        $ send_phone_message("Sky", "AM I THO", "sky_dm")
        $ phone_pause(0.5)
        $ send_phone_message("Sky", "felt like she KNEW", "sky_dm")
        $ send_phone_message(phone_config["phone_player_name"], "She was probably just wondering why you looked half dead.", "sky_dm")
        $ phone_pause(0.2)
        $ send_phone_message("Sky", "maybe...", "sky_dm")
        $ phone_pause(1.0)
        $ send_phone_message("Sky", "but i'm telling u", "sky_dm")
        $ phone_pause(1.0)
        $ send_phone_message("Sky", "that look she gave me?", "sky_dm")
        $ phone_pause(1.0)
        $ send_phone_message("Sky", "soul left my body 💀", "sky_dm")
        $ send_phone_message(phone_config["phone_player_name"], "Dramatic much?", "sky_dm")
        $ phone_pause(1.5)
        $ send_phone_message("Sky", "U WERENT THE ONE GETTING STARED DOWN", "sky_dm")
        $ phone_pause(0.2)
        $ send_phone_message("Sky", "anyway", "sky_dm")
        $ phone_pause(1.0)
        $ send_phone_message("Sky", "just... b careful around her ok?", "sky_dm")
        $ phone_pause(0.5)
        $ send_phone_message("Sky", "idk what she knows but", "sky_dm")
        $ phone_pause(0.5)
        $ send_phone_message("Sky", "she DEF suspects smth", "sky_dm")
        $ send_phone_message(phone_config["phone_player_name"], "Noted.", "sky_dm")
        $ send_phone_message(phone_config["phone_player_name"], "Now get some sleep.", "sky_dm")
        $ phone_pause(0.2)
        $ send_phone_message("Sky", "cant", "sky_dm")
        $ phone_pause(1.0)
        $ send_phone_message("Sky", "still too wired from dinner", "sky_dm")
        $ send_phone_message(phone_config["phone_player_name"], "Sky...", "sky_dm")
        $ phone_pause(0.2)
        $ send_phone_message("Sky", "FINE", "sky_dm")
        $ phone_pause(0.2)
        $ send_phone_message("Sky", "going 2 bed", "sky_dm")
        $ phone_pause(0.2)
        $ send_phone_message("Sky", "night", "sky_dm")
        $ present_phone_choices([("I love you", "I love you.", Jump("sktabdinwik")), ("Good night", "Good night.", Jump("sktabdinwik2"))], "sky_dm")
        label sktabdinwik:
            $ lock_phone_screen()
            pause
            $ send_phone_message(phone_config["phone_player_name"], "Good night, Sky.", "sky_dm")
            $ skypoint += 1
            $ renpy.notify(skynotif)
            $ phone_pause(1.0)
            $ send_phone_message("Sky", "i luv u 2 😚", "sky_dm")
            $ send_phone_message(phone_config["phone_player_name"], "When we're ready.", "sky_dm")
            $ phone_pause(0.2)
            $ send_phone_message("Sky", "when ready", "sky_dm")
            $ phone_pause(0.2)
            $ send_phone_message("Sky", "oh w8", "sky_dm")
            $ send_phone_message("Sky", "images/ch2ep2_72.jpg", "sky_dm", 2)
            $ phone_pause(0.5)
            $ send_phone_message("Sky", "sorry messy hair", "sky_dm")
            $ send_phone_message(phone_config["phone_player_name"], "Not something new to my eyes, but I like that on you.", "sky_dm")
            $ phone_pause(0.2)
            $ send_phone_message("Sky", "geez", "sky_dm")
            $ phone_pause(0.5)
            $ send_phone_message("Sky", "sleep well [mc]", "sky_dm")
            $ show_all_phone_channels()
            $ unlock_phone_screen()
            show screen phone_blocker
            show screen phone_close_button
            $ send_phone_message(phone_config["phone_player_name"], "Sleep well, Sky.", "sky_dm")
            jump sktabdinwikcont
        label sktabdinwik2:
            $ lock_phone_screen()

            $ show_all_phone_channels()
            $ unlock_phone_screen()
            show screen phone_blocker
            show screen phone_close_button
            jump sktabdinwikcont
    label sktabdinwikcont:
    stop sound fadeout 2
    call hide_days
    with dissolve
    
    scene black
    with dissolve
    with fade

    $ phone_time_add(hours=19)
    show screen day_sunday with dissolve
    play music 'audio/DriftBetweenSignals.mp3'
    show emmaletterponder
    with dissolve
    pause
    scene ch2ep2_73
    with dissolve
    hide emmaletterponder
    pause
    scene ch2ep2_74
    with dissolve
    pause
    if emmaroute:
        scene ch2ep2_75
        with flash
        play sound closedoor
        mc "Wait. Em."
        scene ch2ep2_76
        with dissolve
        mc "Here. This is for you."
        scene ch2ep2_77
        with dissolve
        e "What—"
        e "When?"
        scene ch2ep2_78
        with dissolve
        mc "Back when we raided Hera's place. She told me it was on me to get it to you."
        mc "Look... I have no idea what it says, but I don't think it's my call to decide when you should read it."
        scene ch2ep2_79
        with dissolve
        mc "I'm not gonna stop you if you've made up your mind, and I'm not banking on it changing anything."
        mc "But I hope it helps you figure out where to go from here."
        mc "You're free, Em. Make it count."
        scene ch2ep2_74
        with flash
        pause
    play music 'audio/WrongDoorRightDisaster.mp3'
    play sound doorslam2
    show ch2ep2_80 at blur_slide_right
    un "*catching her breath*"
    e "What's going on?"
    scene ch2ep2_81
    with dissolve
    hide ch2ep2_80
    un "Sec..."
    un "Need to... catch my breath..."
    un "Stairs..."
    un "Suck..."
    e "..."
    play sound woosh
    scene ch2ep2_82
    ela "Oh, hey! Elaine Harrison. Nice to meet you."
    mc "We've met."
    e "Damn it."
    scene ch2ep2_83
    with hpunch
    e "Elaine!"
    ela "Yeah?"
    e "Work!"
    stop music fadeout 3
    play music2 'audio/SolvingAMystery.mp3' fadein 3
    play sound rummage_paper
    scene ch2ep2_84
    with dissolve
    ela "Right. Got something. Maybe."
    play sound2 casepickup2
    scene ch2ep2_85
    with Dissolve(0.2)
    ela "Here."
    ela "Pulled this off a guy I picked up last week. Solicitation charge, but his call log's... interesting."
    scene ch2ep2_86
    with dissolve
    e "Club Ashen. Three calls in two days."
    scene ch2ep2_87
    with dissolve
    ela "Yeah. And get this—"
    ela "My contact sent this over an hour ago. Says she saw two guys walking a kid through the side entrance last night."
    scene ch2ep2_88
    with dissolve
    mc "She get a look at the kid?"
    ela "Yeah. Female. Red jacket. Maybe ten, eleven. Some weird muted copper-auburn hair."
    mc "Kids dye their hair now?"
    ela "Hence the \"weird.\" Pretty uncommon, if you ask me."
    play sound papermovement2
    scene ch2ep2_89
    with dissolve
    e "Doesn't match anyone on our list."
    mc "Which means she's unreported."
    e "Or she hasn't been reported yet."
    ela "Either way, a kid walking into a club at night? That alone is enough to check it out."
    scene ch2ep2_90
    with dissolve
    e "Checking it out isn't the problem, Ela. What happens after we check it out is the problem."
    e "Say we go in. Say the kid's there. Say it's exactly what it looks like."
    e "We'd still be walking into a club without a warrant, based on a tip from someone who had been drinking."
    scene ch2ep2_91
    with dissolve
    ela "We're not raiding the place. We're responding to a potential child endangerment sighting."
    e "And the second we pull out a gun or flash a badge, it becomes a raid."
    e "Any halfway decent lawyer is going to pick apart how we got there. Who told us. What state they were in when they told us."
    ela "She wasn't wasted, Em. She'd had a few—"
    e "A few is enough. You know that."
    scene ch2ep2_92
    with dissolve
    mc "So the intel's real, but the source is the weak link."
    e "The source is always the weak link. That's how these things fall apart in court."
    e "We go in, we find something, we make arrests."
    e "Six months later it gets thrown out because the tip came from a woman on her third drink at a bar."
    scene ch2ep2_93
    with dissolve
    ela "So what, we just let it go?"
    e "I didn't say that."
    e "I'm saying the freight depot cost me. Bad intel, rushed entry, nothing to show for it."
    e "The captain made it clear. One more mess and I'm done."
    ela "Wait. He actually said that?"
    e "He didn't have to spell it out. \"You're on thin ice, Meyer\" covers it."
    ela "Shit... how bad was it?"
    e "Bad enough that I'm having this conversation instead of already being in the car."
    scene ch2ep2_94
    with dissolve
    pause
    scene ch2ep2_95
    with dissolve
    mc "Em."
    e "What?"
    mc "This isn't the depot. The depot was dead. No movement, no bodies, nothing."
    mc "This has a kid walking through a door. That's not a maybe."
    e "It's not a maybe that she saw something. It's a maybe that what she saw is what we think it is."
    mc "A ten-year-old in a nightclub. What else could it be?"
    e "..."
    scene ch2ep2_96
    with dissolve
    ela "He's right, Em. Even if the tip doesn't hold up in court, we've got enough for exigent circumstances."
    scene ch2ep2_97
    with dissolve
    mc "Exigent circumstances?"
    ela "Immediate threat to life. Bypasses the warrant."
    e "Only if we can articulate the threat on the spot. \"Someone told us a kid went in there\" doesn't cut it unless we see something ourselves."
    scene ch2ep2_98
    with dissolve
    ela "Then we go see something ourselves."
    e "And if the kid's already gone? If they moved her the second they spotted heat?"
    ela "Then we've burned the location for nothing. I know."
    e "Not just the location. The whole lead. They scatter, they relocate, and we're back to square one."
    scene ch2ep2_99
    with dissolve
    ela "..."
    scene ch2ep2_100
    with dissolve
    ela "So what's the play?"
    scene ch2ep2_101
    with dissolve
    pause
    e "..."
    scene ch2ep2_102
    with dissolve
    mc "You already know what you want to do."
    e "..."
    play sound chairdrag
    scene ch2ep2_103
    with dissolve
    e "How fast can we get there?"
    ela "Fifteen, maybe twenty if traffic's ugly. And I mean... you've got yourself a solid driver."
    scene ch2ep2_104
    with dissolve
    mc "She's not wrong."
    scene ch2ep2_105
    with dissolve
    e "If we go, we go quiet. No badges, no weapons visible. We blend in, we observe."
    e "If we see the kid, we call it in and claim exigent circumstances on the spot."
    e "If we don't see anything, we leave. Clean. No trail."
    e "I'll go get dressed for the... occasion. We leave in ten."
    play sound closedoor2
    scene ch2ep2_106
    with dissolve
    pause 0.5
    mc "She always like this?"
    ela "Pretty much."
    ela "One second she's weighing every angle, the next she's out the door."
    mc "Thing is, she's nothing like this outside of all of this."
    ela "Huh... Guess I don't know her as well as I thought"

    stop music2 fadeout 2

    scene black
    with dissolve
    with fade

    $ phone_time_add(hours=4)
    play music 'audio/StringsOfImmersion1.mp3' fadein 2
    scene ch2ep2_107
    with dissolve
    mc "Em... how sure are we?"
    e "We're not."
    mc "That's the most reassuring thing you've ever said."
    e "Your idea, remember?"
    mc "My idea was \"check it out.\" You're the one who turned it into an operation."
    scene ch2ep2_108
    with dissolve
    pause
    scene ch2ep2_109
    with dissolve
    e "If there's really a kid in there, I'm not walking out without her."
    e "If not, we grab a drink and pretend we were never here."
    scene ch2ep2_110
    with dissolve
    mc "Your partner's contact—how reliable is she?"
    e "Drunk. Pissed at her ex. Probably seeing things."
    mc "There's a \"but\" coming, right?"
    scene ch2ep2_111
    with dissolve
    e "But she's tipped us off before. And she's never been wrong."
    mc "Then let's bet on that."
    play sound gun_magazine
    scene ch2ep2_112
    with Dissolve(0.3)
    pause
    play sound gun_magazine2
    scene ch2ep2_113
    with Dissolve(0.3)
    e "Take the service alley around back. I'll blend in through the front."
    mc "I got you."
    e "Let's move."
    play sound cardoorclose
    scene ch2ep2_114
    with dissolve
    mc "Alright. See you inside."
    e "*nods*"

    scene black
    with dissolve
    with fadeq

    play sound crowd_club loop
    scene ch2ep2_115
    with dissolve
    pause
    scene ch2ep2_116
    with dissolve
    e "This place used to be a textile factory. Now it's \"culture.\""
    mc "*scoffs through comms* Culture doesn't usually need this many exit points."
    e "Already inside?"
    if emmaroute:
        mc "*comms* Yeah, it's tight, and approaching climax."
        e "[mc]..."
    else:
        mc "*comms* Yeah, just got in."
    scene ch2ep2_117
    with dissolve
    wom "Looking for a good time tonight, babe?"
    e "I'll pass."
    scene ch2ep2_118
    with dissolve
    mc "*comms* Multiple exit points near the back. No idea where they lead, but they're there." #
    mc "*comms* No security on my end."
    e "Well, they've got at least one out here."
    mc "*comms* Shit. Need a distraction?"
    e "I can handle it."
    scene ch2ep2_119
    with dissolve
    pause
    scene ch2ep2_120
    with dissolve
    pause
    scene ch2ep2_121
    with dissolve
    pause
    scene ch2ep2_122
    with dissolve
    pause
    scene ch2ep2_123
    with dissolve
    pause
    scene ch2ep2_124
    with dissolve
    pause
    scene ch2ep2_125
    with dissolve
    e "Give me thirty seconds."
    mc "What are you—? Em...?"
    play sound2 punch_wall
    scene ch2ep2_126
    with hpunch
    pause 0.5
    scene ch2ep2_127
    guy1 "Hey, watch it—"
    scene ch2ep2_128
    guy2 "What the fuck, man?!"
    guy1 "Wasn't me! Some chick just—"
    scene ch2ep2_129
    with Dissolve(0.2)
    guy2 "I don't give a shit, you just ruined my fucking shirt!"
    play sound2 glassbreak
    scene ch2ep2_130
    with hpunch
    guy1 "Back off, I said it wasn't my fault—"
    guy2 "Yeah? Then whose is it?!" with hpunch
    scene ch2ep2_131
    with Dissolve(0.2)
    pause
    scene ch2ep2_132
    with Dissolve(0.2)
    pause
    scene ch2ep2_133
    with Dissolve(0.2)
    bounce "Hey! HEY! Break it up!"
    stop music fadeout 2
    $ renpy.music.set_volume(1.0, 1.0, "music2")
    play music2 ["<from 60 to 408>audio/BasementGravity.mp3"] fadein 2
    queue music2 'audio/BasementGravity.mp3'
    play sound2 closedoor2
    scene ch2ep2_134
    with dissolve
    e "I'm in."
    mc "*comms* Thirty seconds. Damn."
    mc "*comms* Multiple guards and cameras. Watch yourself."
    scene ch2ep2_135
    with dissolve
    pause
    scene ch2ep2_136
    with dissolve
    e "I see them."
    scene ch2ep2_137
    with dissolve
    mc "*comms* Visual on you."
    scene ch2ep2_138
    with dissolve
    e "Keep moving. Just keep comms tight."
    mc "*comms* I got you."
    play sound2 chair3
    scene ch2ep2_139
    with dissolve
    pause
    scene ch2ep2_140
    with dissolve
    bart "What can I get you?"
    e "Whiskey. Neat."
    bart "Coming right up."
    play sound2 drink_pour
    scene ch2ep2_141 # He pours SFX
    with dissolve
    mc "*comms* Oh? Didn't know you were a whiskey girl. Or is that an act?"
    scene ch2ep2_142
    with dissolve
    pause
    scene ch2ep2_143
    with dissolve
    bart "First time here?"
    e "Yeah. Friend recommended it."
    bart "Yeah? What friend?"
    e "Does it matter?"
    scene ch2ep2_144
    with dissolve
    bart "Just making conversation."
    e "I'm not really here for that."
    scene ch2ep2_145
    with dissolve
    bart "Fair enough. Shame, though. You're a cute one."
    mc "*comms* I'll shoot him later."
    scene ch2ep2_146
    with dissolve
    pause
    scene ch2ep2_147
    with dissolve
    mc "*comms* You good?"
    e "*whispers* I'm fine. Busy texting a... friend."
    mc "*comms* Passing through a utility corridor."
    scene ch2ep2_148
    with dissolve
    e "*whispers* See anything?"
    mc "*comms* Nothing yet. Just a bunch of drunk patrons trying to find their way out."
    mc "*comms* Smells like a shithole back here."
    scene ch2ep2_149
    with dissolve
    e "*whispers* Hold. I got something."
    mc "*comms* So do I."
    scene ch2ep2_150
    with dissolve
    e "*whispers* Kid-sized footprint. Near the bar. Right of the dance floor."
    mc "*comms* Lines up with what the contact said. Two guards on a side door, basement level."
    e "*whispers* Basement access?"
    mc "*comms* Keycard lock. No signage. That's not storage."
    mc "*comms* What the hell are they keeping down there? Can't force my way in without making a scene."
    mc "*comms* Sit tight. I'll loop through the back."
    e "*whispers* I'll find a better vantage point."
    play sound2 papermovement
    scene ch2ep2_151
    with dissolve
    pause
    scene ch2ep2_152
    with dissolve
    pause
    scene ch2ep2_153
    with dissolve
    pause
    scene ch2ep2_154
    with dissolve
    pause
    scene ch2ep2_155
    with dissolve
    pause
    stop sound fadeout 2
    $ renpy.music.set_volume(0.2, 1.0, "music2")
    scene ch2ep2_156
    with dissolve
    mc "I'm in the maintenance area. Barely any light down here."
    play sound running loop
    scene ch2ep2_157
    with Dissolve(0.2)
    pause
    scene ch2ep2_158
    with Dissolve(0.2)
    pause
    stop sound
    scene ch2ep2_159
    with Dissolve(0.2)
    mc "Got a door. Lights on inside."
    e "*comms* Can you get it open?"
    play sound opendoor2
    scene ch2ep2_160
    with dissolve
    pause
    scene ch2ep2_161
    with dissolve
    mc "A bed. Cheap mattress. Stuffed animals, and a jar of candies."
    mc "This is where they kept her, Em. But she's not here now."
    e "*comms* Keep looking."
    play sound metal_open
    scene ch2ep2_162
    gu "Хватит валять дурака и готовьте всё!"
    play sound2 running_metal loop
    scene ch2ep2_163
    with Dissolve(0.2)
    mc "..."
    scene ch2ep2_164
    with Dissolve(0.2)
    mc "They're moving. Three, maybe four."
    e "*comms* The kid?"
    mc "Negative—guards. They're packing something up."
    play sound crowd_club loop fadein 1
    $ renpy.music.set_volume(1.0, 0.5, "music2")
    stop sound2 fadeout 1
    scene ch2ep2_165
    with dissolve
    pause
    scene ch2ep2_166
    with Dissolve(0.1)
    e "They've got her. Heading for the side exit."
    mc "*comms* On my way."
    scene ch2ep2_167
    with dissolve
    pause 0.5
    e "I've got company. Must've been the bartender."
    e "Be careful. They're on to us."
    scene ch2ep2_168
    with Dissolve(0.2)
    mc "Em, where—"
    play sound2 handgunmovement
    scene ch2ep2_169
    with Dissolve(0.1)
    mc "Shit."
    scene ch2ep2_170
    stop music2
    play sound crowd_chaos loop
    play music 'audio/StringsOfImmersion2.mp3'
    play sound2 p226
    pause 0.2
    play sound3 p226
    pause 0.2
    play sound4 p226
    pause 0.5
    play sound5 bodyfall2
    scene ch2ep2_171
    with hpunch
    pause
    scene ch2ep2_172
    play sound2 g17
    pause 0.2
    play sound2 g17
    pause
    stop sound fadeout 30
    play sound2 clubshootout loop
    play sound3 bodyfall
    scene ch2ep2_173
    with hpunch
    pause
    play sound4 cloth
    show ch2ep2_174
    pause 0.7
    play sound5 thud3
    scene ch2ep2_175
    pause
    play sound3 handgunmovement
    scene ch2ep2_176
    pause 0.5
    bart "Whoa, whoa! Easy, man. I just work here. I don't know anything."
    scene ch2ep2_177
    with dissolve
    bart "..."
    play sound3 casepickup2
    scene ch2ep2_178
    pause 0.5
    scene ch2ep2_179
    play sound4 g17
    pause 0.9
    play sound3 bodyfall2
    scene ch2ep2_180
    with hpunch
    bart "AAAGH! MOTHERFUCKER!"
    mc "Should've shut up when the lady told you to."
    scene ch2ep2_181
    with Dissolve(0.1)
    pause
    scene ch2ep2_182
    with Dissolve(0.1)
    e "Conserve your bullets."
    mc "*comms* How? It's a storm down here."
    play sound3 gun_magazine
    scene ch2ep2_183
    with Dissolve(0.1)
    pause 0.7
    play sound4 running loop
    scene ch2ep2_184
    pause
    play sound4 woosh4
    scene ch2ep2_185
    pause 0.7
    play sound5 clench
    scene ch2ep2_186
    with Dissolve(0.1)
    pause
    scene ch2ep2_187
    with Dissolve(0.1)
    pause
    scene ch2ep2_188
    with Dissolve(0.1)
    pause
    scene ch2ep2_189
    play sound4 g17
    pause 0.2
    play sound5 g17
    pause 0.7
    play sound3 neck_break
    scene ch2ep2_190
    with hpunch
    pause
    play sound4 bodyfall2
    scene ch2ep2_191
    with Dissolve(0.1)
    pause
    play sound3 running loop
    scene ch2ep2_192
    with Dissolve(0.1)
    pause
    stop sound3 fadeout 1
    scene ch2ep2_193
    pause
    scene ch2ep2_194
    with Dissolve(0.1)
    e "[mc]!"
    mc "Get her out. I'll keep them busy."
    scene ch2ep2_195
    play sound4 g17
    pause 0.2
    play sound5 g17
    pause 0.2
    play sound5 g17
    pause 0.5
    scene ch2ep2_196
    pause
    play sound3 running loop
    scene ch2ep2_197
    pause
    stop sound2
    scene ch2ep2_198
    play sound4 g17
    pause 0.2
    play sound5 g17
    pause 0.7
    stop sound3
    play sound2 chair
    scene ch2ep2_199
    pause 0.7
    play sound woosh2
    with Dissolve(0.1)
    scene ch2ep2_200
    pause
    scene ch2ep2_201
    play sound4 g17
    pause 0.2
    play sound5 g17
    pause 0.2
    play sound5 g17
    pause
    play sound bodyfall
    scene ch2ep2_202
    pause
    scene ch2ep2_203
    with Dissolve(0.2)
    pause
    scene ch2ep2_204
    with Dissolve(0.2)
    e "Hey, hey—look at me."
    scene ch2ep2_205
    with dissolve
    e "We're getting you out of here, okay?"
    un "*nods*"
    scene ch2ep2_206
    with dissolve
    e "What's your name?"
    le "L-Leah..."
    play sound clubshootout loop
    scene ch2ep2_207
    mc "Em! More coming!"
    e "Cover us!"
    scene ch2ep2_208
    with Dissolve(0.2)
    pause
    stop sound fadeout 2
    stop music fadeout 3
    play music2 'audio/StringsOfImmersion1.mp3' fadein 3

    scene black
    with dissolve
    with fadeq

    scene ch2ep2_209
    with dissolve
    pause
    scene ch2ep2_210
    with dissolve
    e "Your arm."
    mc "I'm fine. Nothing vital. Just a graze."
    scene ch2ep2_211
    with dissolve
    e "*sighs in relief*"
    e "Toss me the radio, please."
    scene ch2ep2_212
    with Dissolve(0.2)
    mc "Yeah, here."
    play sound radiostatic
    scene ch2ep2_213
    with Dissolve(0.2)
    e "10-13! 10-13! This is Detective Meyer, badge 4-7-2-9. Code 3, requesting immediate backup."
    play sound radiostatic
    dis "Copy, 4-7-2-9. What's your 20?"
    play sound radiostatic
    e "Club Ashen, industrial district off Harlow. We have a 10-34S, shots fired at officer, multiple suspects still inside."
    play sound radiostatic
    dis "10-4. Nature of the incident?"
    play sound radiostatic
    e "Suspected abduction of a tender age victim in progress. One juvenile recovered, currently in our custody."
    e "We have a multiple armed suspects shooting at officer on scene, approximately four to six individuals. Requesting units for a 10-34, Code 3."
    play sound radiostatic
    scene ch2ep2_214
    with Dissolve(0.2)
    dis "Copy that. Units en route. ETA three minutes. Do you need medical?"
    play sound radiostatic
    e "Affirmative. We're transporting the victim to HC General now. Juvenile female, approximately ten years old, no visible injuries but needs evaluation."
    play sound radiostatic
    dis "10-4. I'll notify the hospital. Do you need an escort?"
    play sound radiostatic
    e "Negative. We're clear of the scene, en route now."
    play sound radiostatic
    dis "Copy. Be advised, SWAT is rolling for building sweep. They'll secure the location."
    play sound radiostatic
    e "Roger. Suspects are all armed. VIP section, basement level."
    play sound radiostatic
    dis "Confirmed. All available units, Code 3 to Club Ashen, industrial district. 10-34 in progress, suspects on scene are to be considered armed and dangerous."
    scene ch2ep2_215
    with dissolve
    mc "Hospital's twenty minutes out."
    e "Let's move fast."
    play sound police_siren
    scene ch2ep2_216
    with dissolve
    pause 0.5
    mc "You hear that? Help's coming. But we're getting you checked out first, okay?"
    stop music2 fadeout 2
    stop sound fadeout 2

    scene black
    with dissolve
    with fadeq

    play sound cardriveinterior loop fadein 2
    scene ch2ep2_217
    with dissolve
    e "We got her."
    ela "Yeah, we caught the broadcast. Nice work, Em. You guys good?"
    e "We're all fine. Captain say anything?"
    play sound2 policestation_ambience loop fadein 1
    stop sound fadeout 1
    scene ch2ep2_218
    with dissolve
    ela "Pfft. Not a word. But his mood's a little less murderous, so there's that."
    ela "What are you gonna do after this?"
    scene ch2ep2_219
    with dissolve
    e "Not sure yet. Still got a few things to sort out."
    ela "Alright. Take it easy."
    stop sound2 fadeout 1
    play sound cardriveinterior loop fadein 1
    play sound3 phoneclick
    scene ch2ep2_220
    with dissolve
    pause
    scene ch2ep2_221
    with dissolve
    pause
    scene ch2ep2_222
    with dissolve
    mc "So what happens next?"
    e "..."
    scene ch2ep2_223
    with dissolve
    e "Medical check. Standard intake protocol."
    e "Someone from CPS will talk—"
    play music 'audio/LeahsLullaby.mp3'
    scene ch2ep2_224
    with dissolve
    e "..."
    scene ch2ep2_225
    with dissolve
    pause 0.5
    le "Am I going to be okay?"
    scene ch2ep2_226
    with dissolve
    e "You're..."
    scene ch2ep2_227
    with Dissolve(0.1)
    mc "You're going to be fine. We won't let anyone else hurt you."
    le "*nods*"
    scene ch2ep2_228
    with Dissolve(1.0)
    pause
    play sound2 cloth
    scene ch2ep2_229
    with dissolve
    e "Ah—"
    scene ch2ep2_230
    with Dissolve(2.0)
    pause
    scene ch2ep2_231
    with dissolve
    pause
    stop sound fadeout 2

    scene black
    with dissolve
    with fade

    play sound hospitalambience2 loop fadein 2
    scene ch2ep2_232
    with dissolve
    nur "Detective Meyer?"
    e "Yeah."
    scene ch2ep2_233
    with dissolve
    nur "What do we have?"
    e "Juvenile female, approximately ten years old. Possible trafficking victim. No visible injuries, but she needs a full workup."
    scene ch2ep2_234
    with dissolve
    nur "Alright, let's get her to Exam Room 3."
    scene ch2ep2_235
    with dissolve
    cara "Hey, sweetie. I'm Cara. We're gonna take a look at you, okay? Make sure everything's alright."
    play sound2 cloth
    scene ch2ep2_236
    pause
    scene ch2ep2_237
    with dissolve
    e "Hey, I'll be right here. I'm not going anywhere."
    le "Okay..."
    scene ch2ep2_238
    with dissolve
    pause
    scene ch2ep2_239
    with dissolve
    pause
    scene ch2ep2_240
    with dissolve
    pause
    scene ch2ep2_241
    with dissolve
    pause
    scene ch2ep2_242
    with flash
    pause
    scene ch2ep2_241
    with flash
    pause
    scene ch2ep2_243
    with dissolve
    pause
    scene ch2ep2_244
    with dissolve
    mc "*exhales*"
    scene ch2ep2_245
    with dissolve
    e "You shouldn't have told her that."
    mc "Em...?"
    scene ch2ep2_246
    with Dissolve(0.2)
    e "In the car. You told her she'd be fine."
    scene ch2ep2_247
    with Dissolve(0.2)
    mc "What was I supposed to do? Tell her she's not?"
    e "You don't lie to a kid who just crawled out of hell, [mc]. That's—"
    mc "What? I didn't lie."
    scene ch2ep2_248
    with Dissolve(0.1)
    e "You promised her something we can't guarantee."
    mc "I promised her we'd try."
    e "And when trying isn't enough? What then?"
    mc "Then at least she knows someone gave a damn about her."
    scene ch2ep2_249
    with dissolve
    e "[mc], that's... that's not how this works."
    mc "Then how does it work, Em? Walk me through it."
    e "..."
    mc "Because from where I'm standing, you wanted me to tell a kid who just \"crawled out of hell\" that she's safe tonight, but tomorrow brings another hell of its own."
    mc "Paperwork, interviews, therapy, maybe a foster home she'll probably age out of."
    mc "Is that what you had in mind?"
    e "I just wanted you to be honest with her."
    mc "I was."
    e "You told her she'd be fine."
    mc "Yeah. And maybe she will be."
    scene ch2ep2_250
    with dissolve
    e "You don't know that. WE don't know that."
    mc "So we just say nothing? Let her sit there wondering if she's about to get thrown back into the same nightmare?"
    e "We tell her what's real. That's the job."
    scene ch2ep2_251
    with dissolve
    mc "Then I must've missed the memo, because for all I know, the JOB is to protect her."
    mc "And right now, that means not dumping the full weight of the system on her shoulders while she's still shaking."
    e "She deserves to know what's coming."
    mc "No. More than anything, she deserves to feel safe first."
    e "And tomorrow? When reality hits?"
    mc "Tomorrow she's stronger. Tomorrow she'll have had one night where she knew there were people in her corner, looking out for her."
    mc "That matters."
    scene ch2ep2_252
    with dissolve
    e "Until it doesn't. Until she's sitting in some intake office realizing we fed her the same line everyone else did."
    mc "Or—hear me out, Em—she remembers that two people pulled her out of that place and didn't treat her like a case number."
    e "She IS a case number, [mc]! The second CPS gets involved, that's exactly what she becomes!"
    mc "To them, maybe. Not to me. What about you?"
    e "I don't know. Because we're not different. We're part of the same machine."
    scene ch2ep2_253
    with Dissolve(0.2)
    mc "Well fuck the machine then!"
    scene ch2ep2_254
    with Dissolve(0.2)
    pause
    scene ch2ep2_255
    with dissolve
    e "In this line of work, we don't get to choose what they need. We only—ONLY—tell them what's real."
    scene ch2ep2_256
    with dissolve
    mc "And that's exactly why they stop trusting cops."
    scene ch2ep2_257
    with dissolve
    e "..."
    mc "You think I don't know how this ends? I know the numbers. I know most of these kids don't get happy endings."
    mc "But she didn't need to hear that tonight."
    scene ch2ep2_258
    with dissolve
    e "So we lie? That's where we're at?"
    mc "We give her hope, Em. Even if only a sliver."
    e "Hope without a foundation is just another word for false comfort."
    e "You run a charity. You of all people know that."
    scene ch2ep2_259
    with dissolve
    e "..."
    e "They told me she'd be fine."
    mc "Who?"
    e "My mom. The doctors. All of them."
    e "And I just... sat there. Believing it like an idiot."
    mc "Em..."
    e "She wasn't fine."
    scene ch2ep2_260
    with Dissolve(0.2)
    e "What happens when she figures out we couldn't keep that promise?"
    mc "..."
    scene ch2ep2_261
    with dissolve
    e "*shaking* Why am I like this?"
    e "Maybe I... shouldn't have taken this case, after all."
    menu:
        "Hold her shoulder":
            scene ch2ep2_262
            with dissolve
            mc "Alright... that's enough."
            mc "Listen to me."
            mc "You're not your mom. And Leah's not you."
            mc "What happened to your mom—that wasn't about hope. That was about something nobody could control."
            mc "This? This is different."
            e "..."
        "Hug her":
            $ emmapoint += 1
            $ renpy.notify(emmanotif)
            play sound2 cloth
            scene ch2ep2_263
            with dissolve
            mc "Alright... that's enough."
            mc "Listen to me."
            mc "You're not your mom. And Leah's not you."
            mc "What happened to your mom—that wasn't about hope. That was something nobody could control."
            mc "This? This is different."
            e "..."
    scene ch2ep2_264
    with dissolve
    doc "Detective Meyer?"
    scene ch2ep2_265
    with dissolve
    e "Here."
    scene ch2ep2_266
    with dissolve
    doc "She's stable. No critical injuries, but we'll keep her overnight for observation."
    mc "*exhales*"
    scene ch2ep2_267
    with dissolve
    doc "You can see her in a few hours, once the intake paperwork's done."
    e "Thanks."
    scene ch2ep2_268
    with dissolve
    pause
    scene ch2ep2_269
    with dissolve
    doc "Oh, and uhh..."
    scene ch2ep2_270
    with dissolve
    doc "She's asking for your name, Detective."
    scene ch2ep2_271
    with dissolve
    pause
    scene ch2ep2_272
    with dissolve
    mc "*shrugs*"
    scene ch2ep2_273
    with dissolve
    e "..."
    stop sound fadeout 2
    stop music fadeout 2

    scene black
    with dissolve
    with fade

    play sound nightambience2 loop
    play sound2 cardoorclose
    scene ch2ep2_274
    with dissolve
    pause
    scene ch2ep2_275
    with dissolve
    pause
    scene ch2ep2_276
    with dissolve
    mc "How long you been out here?"
    m "Since I couldn't sit still."
    mc "Oh boy..."
    play sound2 cloth2
    scene ch2ep2_277
    mc "Look, I'm fine. It's just a—"
    scene ch2ep2_278
    with dissolve
    pause
    play sound2 cloth
    scene ch2ep2_279
    with Dissolve(1.0)
    pause
    scene ch2ep2_280
    with dissolve
    mc "Something wrong?"
    m "Nothing. Just taking a sniff."
    mc "Huh... didn't know Sky was that contagious."
    m "..."
    play sound2 cloth
    scene ch2ep2_281
    with Dissolve(0.2)
    mc "Hey. Come here for a sec. Got something to ask you."
    m "Hm?"
    scene ch2ep2_282
    with dissolve
    mc "I'm not asking you, specifically. I'm asking the Sora inside you."
    m "Oh? What's it about?"
    play sound2 chairdrag
    scene ch2ep2_283
    with dissolve
    mc "There's a kid. Her name's Leah. We pulled her out of a trafficking ring tonight."
    m "What—"
    m "Is she okay?"
    play sound2 chair3
    scene ch2ep2_284
    with dissolve
    mc "For now. Hospital, CPS intake, the whole nine."
    mc "But after that? I don't know."
    mc "Foster care, maybe. Group home. Bouncing around the system until she ages out or gets lucky."
    m "That's... not great."
    mc "No. It's not."
    play sound2 chair2
    $ renpy.music.set_volume(1.0, 1.0)
    play music 'audio/ChemTrails.mp3' fadein 2
    scene ch2ep2_285
    with dissolve
    pause
    scene ch2ep2_286
    with dissolve
    m "So what are you asking me?"
    scene ch2ep2_287
    with dissolve
    mc "If you were in my shoes—if Sora was—what would she do?"
    m "Hmm... you mean if Kaito brought home a child who needed protection?"
    mc "Yeah. Something like that."
    scene ch2ep2_288
    with dissolve
    m "..."
    scene ch2ep2_289
    with dissolve
    m "Sora wouldn't have asked permission."
    m "She would've just done what needed to be done. Quietly. Without waiting for anyone's say-so."
    mc "Even if it broke the rules?"
    m "Especially then."
    mc "That's... not exactly helpful advice, Moon."
    m "I mean... you didn't ask for helpful. You asked what she'd do."
    mc "Fair enough."
    mc "And what about you? What would Moon do?"
    m "..."
    scene ch2ep2_290
    with dissolve
    m "I'd ask myself one thing first."
    mc "Which is?"
    m "Can you live with yourself if you don't try?"
    mc "..."
    m "Because if the answer's no—if you know you'll regret sitting on your hands—then the rules don't matter."
    m "You'll find a way. Or you'll break trying."
    m "And even if it doesn't work out, at least you'd know you tried."
    mc "You sound like Emma."
    m "Do I?"
    m "Pretty sure you sound the same. I know you two went at it over this. I can see it in your face. That frown."
    mc "Yeah. Except she gave me every reason why it's a bad idea first."
    scene ch2ep2_291
    with dissolve
    m "*laughs* It {i}is{/i} a bad idea."
    mc "Then why are you telling me to do it?"
    m "I'm not. I'm telling you what I would've done."
    m "What you do is on you."
    scene ch2ep2_292
    with dissolve
    mc "..."
    mc "If I do this—if I push for it—it's gonna get really messy."
    m "Probably."
    mc "Emma's already on my case about it."
    m "Can you blame her?"
    pause
    mc "But if I don't try..."
    m "Then you'll spend the rest of your life wondering if you could've made a difference."
    mc "..."
    mc "Yeah."
    mc "Yeah, you're right."
    play sound2 chairdrag
    scene ch2ep2_293
    with dissolve
    mc "Thanks, Moon."
    m "For what?"
    mc "For telling me what I wanted to hear."
    scene ch2ep2_294
    with dissolve
    m "..."
    scene ch2ep2_295
    with dissolve
    m "[mc]."
    mc "Yeah?"
    m "Be careful."
    mc "I will."
    m "I'm serious. You're healing faster, but that doesn't mean you're bulletproof."
    mc "I know."
    scene ch2ep2_296
    with dissolve
    mc "You coming in?"
    m "In a bit. I need to make a call."
    mc "To who?"
    m "Emma."
    mc "Why?"
    scene ch2ep2_297
    with dissolve
    m "*laughs* Because someone's gotta warn her you're about to do something stupid."
    mc "Moon—"
    m "I'm kidding."
    scene ch2ep2_298
    with dissolve
    m "Also... I was going to bring it up, but I figured you already knew."
    mc "Huh?"
    m "You've got a friend at DFCS. Best friend, actually."
    scene ch2ep2_299
    with dissolve
    pause
    scene ch2ep2_300
    with dissolve
    pause
    scene ch2ep2_301
    with dissolve
    mc "Moon... you're a genius."
    stop music fadeout 2
    stop sound fadeout 2

    scene black
    with dissolve
    with fade

    play sound traffic2 fadein 2 loop
    play sound2 atm_machine
    scene ch2ep2_302
    with dissolve
    pause
    play sound2 cardswipe
    scene ch2ep2_303
    with dissolve
    yt "*sighs* Still not enough."
    scene ch2ep2_304
    with dissolve
    ju "You didn't drag me out here to watch your bank account cry, right?"
    scene ch2ep2_305
    with dissolve
    mc "Actually... got something to ask you."
    ju "Whoa! Hold on, chief. No opening insult? No trash talk? You feeling alright?"
    scene ch2ep2_306
    with dissolve
    mc "I need you to take this one seriously."
    ju "..."
    ju "Sure."
    mc "Emma and I pulled a kid out of a trafficking ring earlier."
    scene ch2ep2_307
    with dissolve
    ju "Holy fucking christ, [mc]! Are you okay? How's Emma? And the kid?"
    mc "We're both fine, but the kid..."
    scene ch2ep2_308
    with dissolve
    ju "Hospital, I'm guessing? Child Protective Services handling intake?"
    mc "Yeah. Emma's still there seeing it through."
    ju "Ahh... so that's why I'm here."
    scene ch2ep2_309
    with dissolve
    mc "Can my charity take her?"
    scene ch2ep2_310
    with dissolve
    ju "..."
    scene ch2ep2_311
    with dissolve
    ju "[mc]..."
    mc "I know it's complicated. Just hear me out."
    mc "The case involves trafficking. There's a credible ongoing threat—these guys don't just let kids walk."
    mc "Normal foster placement might not cut it. Not right away."
    ju "So you think your charity's a better fit?"
    mc "Yeah. We've got temporary housing. Security. Resources built for at-risk kids."
    mc "It's not permanent. Just until things cool down and CPS finds a proper placement."
    ju "You know CPS can't just hand a kid over to you, right?"
    mc "There goes all my hope..."
    ju "..."
    ju "You're allowed to submit a request. But I can't promise you anything."
    mc "But it's possible?"
    ju "Possible? Sure. Likely? That's a different story."
    mc "Why?"
    play sound2 chair2
    scene ch2ep2_312
    with Dissolve(0.2)
    pause 0.5
    play sound2 cloth
    scene ch2ep2_313
    with Dissolve(0.1)
    ju "Because you were part of the extraction."
    mc "So?"
    ju "So that complicates things, dumbass."
    scene ch2ep2_314
    with dissolve
    ju "You think I can't see what you're doing? I get it—you've got a soft spot for kids. You pulled her out, now you feel responsible."
    ju "But from CPS's end, that's a conflict of interest."
    mc "How is keeping her safe a conflict?"
    ju "Because we have protocols, [mc]. Background checks. Conflict-of-interest reviews. Psych evals."
    ju "Even if your charity checks every box, someone's gonna ask, \"Why does this guy want custody of a kid he just pulled out of a raid?\""
    mc "Because nobody else is stepping up."
    scene ch2ep2_315
    with dissolve
    ju "That's not how the system sees it."
    ju "They'll see a guy who got emotionally involved and is trying to skip the line."
    mc "I'm not skipping anything. I'm following the process."
    ju "You hearing yourself right now? You're asking me for special treatment."
    mc "..."
    mc "So I shouldn't try?"
    scene ch2ep2_316
    with dissolve
    ju "I'm not saying that. But you need to understand what you're getting into."
    ju "You submit this request, there will be scrutiny. A lot of it."
    ju "They'll dig into your finances, your background, your mental health history."
    ju "They'll talk to people who know you. They'll pick apart your motives."
    ju "And even after all that? They might still say no."
    mc "If I don't submit?"
    ju "Then the kid goes into the system like every other kid."
    mc "..."
    scene ch2ep2_317
    with dissolve
    mc "I can live with the scrutiny. What I can't live with is watching on the sideline."
    ju "..."
    scene ch2ep2_318
    with dissolve
    ju "*scratches her neck* Alright. Here's what I can do."
    ju "Submit the request through official channels. Don't try to fast-track it. Don't pull strings."
    ju "I'll make sure it gets a fair review. That's the best I can offer."
    mc "That's all I'm asking."
    scene ch2ep2_319
    with dissolve
    ju "But [mc]..."
    mc "Yeah?"
    ju "You need to brace yourself in case this doesn't pan out."
    ju "Even if your charity's spotless. Even if you pass every check. The optics alone could sink it."
    mc "Because I was there when we pulled her out?"
    ju "Yeah."
    ju "Good intentions don't cancel out bad optics. And right now?"
    scene ch2ep2_320
    with dissolve
    ju "*shrugs* Just the fact that you were involved tips the scales against you."
    mc "*sighs* Noted."
    scene ch2ep2_321
    with Dissolve(0.2)
    ju "One more thing."
    mc "What?"
    ju "Emma know you're doing this?"
    mc "*shakes his head*"
    ju "That's what I thought."
    ju "You might want to bring her in on this before it blows up in your face."
    ju "Because if CPS flags this as inappropriate involvement, it doesn't just burn you."
    ju "It burns her case too."
    mc "Shit."
    ju "Yeah. Shit."
    scene ch2ep2_322
    with dissolve
    ju "So talk to her. Make sure you're on the same page before you pull the trigger. Don't be like your friend, alright?"
    mc "Yeah, yeah. I will."
    ju "Good."
    ju "Anything else?"
    mc "Yeah."
    mc "Can you take over Leah's case?"
    scene ch2ep2_323
    with dissolve
    ju "So that's her name..."
    mc "Please. I don't trust anyone else with this."
    ju "..."
    scene ch2ep2_324
    with dissolve
    ju "You know I'm putting my own neck on the line here, right? Because you and I know each other."
    ju "So whatever happens next—I will not, and will never, give either of you special treatment."
    mc "Understood."
    scene ch2ep2_325
    with dissolve
    ju "For what it's worth? I hope it works out."
    ju "Wanna grab a bite?"
    mc "You're buying? Hell yeah."
    ju "Alright."
    stop sound fadeout 2
    call hide_days
    with dissolve

    scene black
    with dissolve
    with fade

    $ phone_time_add(hours=13)
    show screen day_monday with dissolve
    play sound hospitalambience2 loop
    scene ch2ep2_326
    with dissolve
    pause
    stop sound fadeout 1
    play sound2 closedoor2
    scene ch2ep2_327
    with dissolve
    e "..."
    scene ch2ep2_328
    with dissolve
    e "... One of you shouldn't be in here."
    ela "I'm curious. Just let it slide this once, okay?"
    e "Not okay."
    ela "..."
    e "*sighs* Fine."
    scene ch2ep2_329
    with dissolve
    e "Where are we?"
    mc "Haven't started yet. About to."
    play music 'audio/FracturedInnocence_var.mp3'
    scene ch2ep2_330
    with dissolve
    mc "How is she, by the way? The doc's eval."
    e "Clean."
    mc "Just clean?"
    e "No physical injuries. No signs of sexual assault. No bruising, no defensive wounds."
    e "Blood work came back normal. She's healthy."
    ela "Hey, that sounds good."
    e "Mm. It's good."
    mc "Please don't tell me there's more."
    e "..."
    scene ch2ep2_331
    with dissolve
    e "No signs of trauma either."
    mc "Why do you say that like it's a bad thing?"
    scene ch2ep2_332
    with dissolve
    e "Because she should be showing something. But she's not. She's calm. Cooperative. Almost... normal."
    ela "Maybe she's just holding it together?"
    e "Maybe. Or she's been conditioned not to react."
    mc "You think they trained her?"
    e "I don't know. But kids don't just walk out of trafficking rings acting like nothing happened."
    e "They flinch. They freeze. They won't look you in the eye."
    e "Something's off."
    e "Either she's repressing it—buried so deep she doesn't even know it's there yet..."
    e "... or whoever had her knew exactly how to keep her compliant without leaving marks."
    ela "Shit."
    scene ch2ep2_333
    with dissolve
    mc "How long was she with them?"
    e "We don't know yet. That's what we're about to find out."
    mc "What if..."
    e "What if she doesn't remember?"
    mc "Yeah."
    e "She should have some sense of it, at least. If she doesn't, we've got a bigger problem than we thought."
    e "Psych eval's scheduled for tomorrow. We'll know more then."
    scene ch2ep2_334
    with dissolve
    ela "Uhh... this is also a psych eval and an interview rolled into one."
    e "What? That's way too fast. She's not ready—"
    play sound opendoor2
    scene ch2ep2_335
    with dissolve
    un "Detective Meyer, we're starting now. Standard protocol for trafficking cases—early evaluation helps establish a baseline trauma response."
    e "..."
    scene ch2ep2_336
    with dissolve
    e "Fine. But keep it gentle."
    scene ch2ep2_337
    with dissolve
    un "Always."
    play sound closedoor2
    scene ch2ep2_338
    with dissolve
    pause
    scene ch2ep2_339
    with dissolve
    drp "Hi, Leah. My name's Dr. Park. You can call me Sol if that's easier."
    le "Okay."
    drp "I just want to talk for a little bit. Nothing scary, I promise. Sound alright?"
    le "Mm-hm."
    play sound chair3
    scene ch2ep2_340
    with dissolve
    drp "Great. You can play with any of these while we chat. Whatever makes you comfortable."
    play sound papermovement2
    scene ch2ep2_341
    with dissolve
    pause
    scene ch2ep2_342
    with dissolve
    drp "So, Leah... do you remember how you got to the hospital?"
    le "The police brought me."
    drp "That's right. Do you remember their names?"
    scene ch2ep2_343
    with dissolve
    le "Em. I heard the other police officer call her that. She hasn't told me her real name yet."
    le "And... I don't know his name."
    scene ch2ep2_344
    with Dissolve(0.1)
    ela "Pfft!"
    mc "There's a sharp pain... right here."
    scene ch2ep2_345
    with dissolve
    e "..."
    scene ch2ep2_346
    with dissolve
    drp "Can you tell me what you remember before that? Before Em and her partner found you?"
    le "..."
    le "There were men. A lot of them."
    drp "Okay. Do you remember where you were?"
    le "A place with music. Really loud music."
    drp "What else do you remember?"
    le "The smell."
    drp "What kind of smell?"
    le "Old perfume. Like... the kind that makes your nose hurt."
    scene ch2ep2_347
    with dissolve
    mc "Club Ashen. VIP section. She's corroborating the location."
    drp "That's very helpful, Leah. You're doing great."
    drp "Do you remember how long you were there? At that place with the music?"
    le "Not long."
    le "That wasn't... the first place."
    drp "There were others?"
    le "Mm."
    drp "Do you remember how many?"
    le "..."
    le "No."
    drp "That's okay. You don't have to know everything."
    mc "Phew... she's okay."
    scene ch2ep2_348
    with dissolve
    drp "Leah, can I ask you something a little harder?"
    le "Okay."
    drp "Do you remember how you ended up there? At that place with the music?"
    le "..."
    scene ch2ep2_349
    with dissolve
    le "My mom."
    scene ch2ep2_350
    with dissolve
    pause
    scene ch2ep2_351
    with dissolve
    mc "What?"
    scene ch2ep2_352
    with dissolve
    drp "Your mom brought you there?"
    le "No. She sold me."
    scene ch2ep2_353
    with dissolve
    drp "..."
    drp "Leah, when you say she sold you—"
    scene ch2ep2_354
    with dissolve
    le "She needed money. So she sold me to them."
    le "She said they'd take care of me."
    scene ch2ep2_355
    with dissolve
    pause
    ela "Jesus Christ..."
    mc "She's... she's not even flinching."
    e "We need to find her, Ela."
    ela "Leave that one to me."
    scene ch2ep2_356
    with dissolve
    drp "Leah, I'm really sorry that happened to you."
    le "It's okay."
    drp "It's not okay. But I'm glad you're safe now."
    le "..."
    le "Am I safe?"
    drp "Yes, you are."
    scene ch2ep2_357
    with dissolve
    le "The lady said that too."
    drp "Which lady?"
    le "The one with the brown hair. Em."
    le "She told me I'd be okay."
    scene ch2ep2_358
    with dissolve
    pause
    scene ch2ep2_359
    with dissolve
    e "But I didn't say that."
    mc "You didn't have to."
    e "..."
    scene ch2ep2_360
    with dissolve
    drp "And do you believe her? That you're okay now?"
    le "..."
    scene ch2ep2_361
    with dissolve
    le "I think so."
    drp "Good. That's really good, Leah."
    scene ch2ep2_362
    with dissolve
    drp "Alright, we're almost done. Just a few more questions, okay?"
    le "Okay."
    drp "Do you remember anyone else from that place? Anyone who talked to you or spent time with you?"
    le "There was a man. He was nice."
    scene ch2ep2_363
    with dissolve
    pause
    scene ch2ep2_364
    with dissolve
    drp "What did he look like?"
    le "I don't know. I never really saw his face."
    drp "But he talked to you?"
    le "Yeah. He said I reminded him of someone."
    drp "Did he say who?"
    le "His sister."
    scene ch2ep2_365
    mc "That's him." (multiple=2)
    e "That's him." (multiple=2)
    ela "You sure?"
    e "Positive."
    scene ch2ep2_366
    with dissolve
    drp "Okay, Leah. You did really well today. I'm proud of you."
    le "Can I go now?"
    drp "In just a minute. Is there anything you want to tell me? Anything at all?"
    scene ch2ep2_367
    with dissolve
    le "..."
    scene ch2ep2_368
    with dissolve
    le "Can I see Em?"
    drp "I think we can arrange that."
    play sound cloth
    scene ch2ep2_369
    with dissolve
    drp "I'll be right back, okay?"
    le "Okay."
    play sound closedoor2
    scene ch2ep2_370
    with dissolve
    pause
    scene ch2ep2_371
    with dissolve
    drp "She's stable. No immediate psychological breaks. But Detective Meyer..."
    scene ch2ep2_372
    with dissolve
    drp "She's repressing. Hard."
    scene ch2ep2_373
    with dissolve
    e "How long before it surfaces?"
    drp "Unfortunately, in her case, there's no way to know."
    scene ch2ep2_374
    with dissolve
    e "..."
    drp "You should grant her request, but briefly. Keep it light. She's more fragile than she looks right now."
    e "Understood."
    play sound closedoor2
    stop music fadeout 4
    scene ch2ep2_375
    with dissolve
    pause
    play music2 'audio/TheRhythmOfTheirHearts.mp3'
    scene ch2ep2_376
    with dissolve
    pause
    scene ch2ep2_377
    with dissolve
    le "Hi."
    e "Hey."
    e "I heard you did really well."
    le "I just answered questions."
    e "That's all we needed."
    play sound cloth
    scene ch2ep2_378
    with Dissolve(1.0)
    pause
    scene ch2ep2_379
    with dissolve
    e "I wanted to say thank you. For being so brave."
    le "I wasn't brave."
    e "Yeah, you were."
    scene ch2ep2_380
    with dissolve
    pause
    scene ch2ep2_381
    with dissolve
    pause
    scene ch2ep2_382
    with dissolve
    ela "I'm guessing she wasn't always like this either."
    mc "No... she really wasn't."
    scene ch2ep2_383
    with dissolve
    le "I made this. For you."
    play sound papermovement2
    scene ch2ep2_384
    with dissolve
    pause
    le "That's when you told me I'd be okay."
    scene ch2ep2_385
    with Dissolve(1.0)
    e "..."
    e "Thank you, Leah..."
    le "You're welcome."
    play sound papermovement
    scene ch2ep2_386
    with dissolve
    e "I'll keep this safe."
    le "Promise?"
    e "Promise."
    scene ch2ep2_387
    with dissolve
    le "What's your name?"
    e "... Emma."
    le "Emma what?"
    e "Meyer. Emma Meyer."
    le "That's pretty."
    e "Thanks."
    le "Can I call you Emma? Or do I have to say Detective Meyer?"
    e "... Emma's fine."
    le "Okay."
    scene ch2ep2_388
    with dissolve
    le "Will I see you again?"
    e "..."
    e "I don't know yet."
    scene ch2ep2_389
    with dissolve
    le "Oh..."
    scene ch2ep2_390
    with dissolve
    pause
    scene ch2ep2_391
    with dissolve
    e "... You're gonna be alright, Leah."
    le "You said that before."
    e "..."
    le "Do you really mean it?"
    scene ch2ep2_392
    with dissolve
    e "..."
    scene ch2ep2_393
    with dissolve
    e "Yeah... I mean it."
    scene ch2ep2_394
    with Dissolve(1.0)
    pause
    e "Yes?"
    scene ch2ep2_395
    with dissolve
    pause
    scene ch2ep2_396
    with dissolve
    scene ch2ep2_397
    with dissolve
    e "Leah?"
    scene ch2ep2_398
    with dissolve
    le "I'm not dreaming..."
    e "What do you mean?"
    le "*softly shakes her head*"
    scene ch2ep2_399
    with dissolve
    drp "*through the speaker* Detective Meyer?"
    e "I know."
    scene ch2ep2_400
    with dissolve
    e "I have to go now."
    le "Mm-hm."
    play sound closedoor2
    scene ch2ep2_401
    with dissolve
    pause
    stop music2 fadeout 2

    scene black
    with dissolve
    with fade

    $ renpy.sound.set_volume(0.1, 0.0)
    play sound2 ceilingfan_low loop
    play sound dialtone2 loop 
    scene ch2ep2_402
    with dissolve
    pause
    scene ch2ep2_403
    with dissolve
    un "She was perfect this time." 
    un "You would've liked her. I'm certain."
    un "Her eyes... they were almost right."
    un "Almost."
    scene ch2ep2_404
    with dissolve
    un "*fingers trembling* Just a little more time. That's all I needed."
    un "Just a little more... and she would've remembered."
    play sound2 closedoor2
    scene ch2ep2_405
    with Dissolve(0.1)
    un "*out of breath* Boss..."
    scene ch2ep2_406
    with dissolve
    fr "..."
    frs "Boss, we got a problem."
    fr "Mm."
    frs "The girl—she's gone."
    $ renpy.sound.set_volume(0.3, 1.0)
    scene ch2ep2_407
    with dissolve
    pause
    scene ch2ep2_408
    with Dissolve(0.1)
    frs "Cops got her. Two of them. Pulled her right out of Ashen."
    fr "..."
    fr "*soft laugh*"
    frs "Boss?"
    fr "No, no. You're wrong."
    play sound2 chair2
    scene ch2ep2_409
    with dissolve
    fr "She's not gone."
    fr "She just ran away again. Like before."
    frs "Boss, I saw it myself. They had her in—"
    fr "She'll come back once she remembers me."
    scene ch2ep2_410
    with dissolve
    fr "She always comes back."
    frs "I don't think—"
    $ renpy.sound.set_volume(0.4, 1.0)
    play sound2 woodhit
    scene ch2ep2_411
    with hpunch
    fr "SHE ALWAYS COMES BACK!"
    scene ch2ep2_412
    with Dissolve(0.2)
    frs "B-Boss, we tried to—"
    scene ch2ep2_413
    with Dissolve(0.1)
    fr "Every time. Every single time, she runs. But then she remembers. And she comes home."
    scene ch2ep2_414
    with Dissolve(0.1)
    fr "Because she knows. She knows I'm the only one who understands her."
    scene ch2ep2_415
    with Dissolve(0.2)
    pause
    scene ch2ep2_416
    with dissolve
    fr "You see, sis?"
    fr "I'm trying. I'm really trying this time."
    fr "I know I messed up before. I know."
    fr "But I'm fixing it. Big brother's fixing it, okay?"
    scene ch2ep2_417
    with dissolve
    fr "They just keep breaking before I can finish..."
    scene ch2ep2_418
    with dissolve
    frs "..."
    scene ch2ep2_419
    with dissolve
    frs "What do you want me to do?"
    fr "..."
    fr "Find me another one."
    frs "Another—?"
    scene ch2ep2_420
    with dissolve
    fr "With eyes like hers."
    frs "Boss, the heat's on us. Cops know about Ashen—"
    fr "Then don't use Ashen."
    fr "Use the other depot. The one on Carver."
    frs "That place is—"
    fr "I don't care. Just do it."
    frs "And... what about the girl? The one they took?"
    scene ch2ep2_421
    with dissolve
    fr "..."
    fr "Leave her to me."
    frs "Boss?"
    fr "I said leave her to me."
    fr "She's not lost. I'll bring her home when she's ready."
    frs "..."
    scene ch2ep2_422
    with dissolve
    frs "Yeah. Okay."
    frs "I'll... I'll handle it."
    play sound2 closedoor2
    scene ch2ep2_423
    with dissolve
    pause
    play sound3 chair2
    play sound4 francis_humming
    scene ch2ep2_424
    with Dissolve(5.0)
    pause
    scene ch2ep2_425
    with Dissolve(2.0)
    pause
    $ renpy.sound.set_volume(1.0, 2.0)
    scene ch2ep2_426
    with Dissolve(2.0)
    pause 1.0

    stop sound4
    play sound2 hospitalambience2 fadein 2 loop
    play sound vendingmachine_click
    scene ch2ep2_427
    pause
    scene ch2ep2_428
    with dissolve
    pause
    scene ch2ep2_429
    with dissolve
    e "*sigh* ... You're kidding me."
    play sound vendingmachine_hit
    scene ch2ep2_430
    with hpunch
    pause
    play sound3 vendingmachine_drop
    scene ch2ep2_431
    with Dissolve(0.2)
    e "..."
    scene ch2ep2_432
    with dissolve
    fio "They get stuck sometimes. Knock it loose."
    e "... Thanks."
    fio "Mm."
    scene ch2ep2_433
    with dissolve
    e "..."
    scene ch2ep2_434
    with dissolve
    fio "..."
    scene ch2ep2_435
    with dissolve
    e "You from around here?"
    fio "I'm next. Do you mind?"
    scene ch2ep2_436
    with dissolve
    e "Right. Sorry."
    scene ch2ep2_437
    with dissolve
    pause
    scene ch2ep2_438
    with dissolve
    e "Coffee?"
    mc "Oh god... no, Em... It's barely past noon."
    e "Suit yourself."
    scene ch2ep2_439
    with dissolve
    pause
    scene ch2ep2_440
    with dissolve
    e "*exhales*"
    play sound chair2
    scene ch2ep2_441
    with dissolve
    mc "So? The captain."
    e "What about him?"
    mc "You still got a desk, or...?"
    e "For now."
    e "He wanted to know why I didn't radio for backup the second I confirmed the kid was there."
    mc "What'd you tell him?"
    scene ch2ep2_442
    with dissolve
    e "That they were moving her. That I had seconds, not a minute to spare."
    mc "You're not wrong. But you're still on the case?"
    scene ch2ep2_443
    with dissolve
    e "He said the rescue bought me some rope. Then told me not to hang myself with it next time."
    e "Anyway. It's done. Moving on."
    mc "What about Francis?"
    mc "Leah just put him in a room with her."
    e "I'll write it up. File it. Drop it on the captain's desk with everything else we've got and let him call the next play."
    mc "I see..."
    scene ch2ep2_444
    with dissolve
    pause
    scene ch2ep2_445
    with dissolve
    mc "Hey."
    e "Hm?"
    scene ch2ep2_446
    with dissolve
    mc "I talked to June."
    e "June? About what?"
    mc "About Leah. Whether my charity could take her in. Temporary placement, protective custody."
    scene ch2ep2_447
    with Dissolve(0.2)
    e "You what?"
    mc "Before you start—"
    e "When?"
    mc "Last night. After we got back."
    e "So while I was still at the hospital, you went behind my back and—"
    mc "I went to someone I trust and asked a question."
    e "This involves MY case, [mc]."
    mc "I know."
    e "The second CPS finds out a Sicae operative from the extraction is trying to pull the kid into his own program—"
    mc "June said the same thing."
    scene ch2ep2_448
    with dissolve
    e "..."
    mc "She flagged it. Said it's a conflict of interest."
    mc "She also said I'm allowed to submit a request. That's it. No promises, no shortcuts."
    scene ch2ep2_449
    with dissolve
    e "Did you submit it?"
    mc "No. Not yet."
    mc "I wasn't gonna do that without telling you first."
    scene ch2ep2_450
    with dissolve
    e "..."
    scene ch2ep2_451
    with dissolve
    e "What did June actually say? About the odds."
    mc "That it's possible. Not likely. Something about optics."
    e "Optics."
    mc "Her word, not mine."
    e "She's right. That's exactly what this is."
    e "Sicae or not, you were on site when we pulled her out. That's a red flag the size of a billboard."
    mc "*dry chuckle* On paper, everything's a red flag."
    scene ch2ep2_452
    with dissolve
    e "What else."
    mc "What?"
    scene ch2ep2_453
    with dissolve
    e "..."
    scene ch2ep2_454
    with dissolve
    mc "I asked June to take over Leah's case."
    e "You asked her to—"
    mc "I don't trust anyone else with it. And neither should you."
    scene ch2ep2_455
    with dissolve
    ju "Emma."
    scene ch2ep2_456
    with dissolve
    ju "[mc]."
    mc "Speak of the devil."
    scene ch2ep2_457
    with dissolve
    e "You could've mentioned she was coming."
    mc "I didn't know she was."
    scene ch2ep2_458
    with dissolve
    ju "Am I interrupting?"
    e "No. You're fine."
    mc "Perfect timing, actually. I was just about to get my head taken off."
    play sound cloth2
    scene ch2ep2_459
    e "You still might."
    ju "Can't say [mc] doesn't deserve it."
    scene ch2ep2_460
    with dissolve
    ju "Emma."
    scene ch2ep2_461
    with dissolve
    e "June."
    ju "I'll be handling Leah's case from here on out."
    ju "Before anything else—thank you. Both of you."
    e "Just doing the job."
    ju "Most people in your position would've waited for the warrant."
    scene ch2ep2_462
    with Dissolve(0.2)
    mc "..." (multiple=2)
    e "..." (multiple=2)
    ju "That wasn't a dig."
    scene ch2ep2_463
    with dissolve
    ju "Alright. Where we stand: temporary protective custody, seventy-two hours from intake before we need a formal hearing to extend it."
    ju "Given the circumstances—trafficking, ongoing threat, no identified guardian—I don't see a judge pushing back."
    mc "What happens after that?"
    scene ch2ep2_464
    with dissolve
    ju "We find placement. I won't sugarcoat it—trafficking cases are harder to place. Foster families hear the word and more than half of them bail."
    ju "Most aren't built for what comes with it. Nightmares, regression, attachment issues. That's the reality."
    mc "What about her family? Grandparents, cousins?"
    ju "First thing we checked."
    ju "Nadine, Leah's mother, was an only child. Her mother died when she was nineteen. No father on her birth certificate."
    ju "On Leah's side, the father's listed as unknown. We pulled what we could from the hospital records where she was born. Nobody ever signed."
    ju "There's no one to call. She's it."
    e "..."
    ju "That's part of why this is moving the way it is. If she had a grandmother in another state, this would be a completely different conversation."
    ju "She doesn't."
    e "Timeline?"
    ju "Weeks. Sometimes months. Depends on availability and how her psych eval shakes out."
    ju "If there's no match, she goes into a group facility until one opens up."
    mc "Months."
    ju "I know—"
    scene ch2ep2_465
    with Dissolve(0.2)
    pause
    scene ch2ep2_466
    with dissolve
    ju "Look. I need you both to hear this clearly."
    ju "Getting her out was the hard part. Keeping her safe is the long game. And that doesn't always look the way you think it should."
    scene ch2ep2_467
    with dissolve
    ju "It means process. Patience. Trusting the people handling it."
    scene ch2ep2_468
    with dissolve
    e "*nods* Understood."
    scene ch2ep2_469
    with dissolve
    mc "..."
    scene ch2ep2_466
    with dissolve
    ju "Good. Emma, I may need you for follow-up interviews later."
    e "Whatever you need."
    scene ch2ep2_467
    with dissolve
    ju "[mc]."
    mc "Yeah?"
    ju "Behave."
    mc "Always do."
    ju "Mm-hm."
    scene ch2ep2_470
    with dissolve
    pause
    e "I need to go get some sleep..."
    stop sound2 fadeout 2
    call hide_days
    with dissolve

    scene black
    with dissolve
    with fade

    $ phone_time_add(hours=23)
    play sound cityalley loop
    show screen day_tuesday with dissolve
    scene ch2ep2_471
    with dissolve
    pause
    scene ch2ep2_472
    with dissolve
    pause
    play sound2 cloth2
    scene ch2ep2_473
    with Dissolve(0.1)
    a "Hmm... cute."
    e "Shouldn't you be at the office right now?"
    scene ch2ep2_474
    with Dissolve(0.2)
    a "Wow! Good morning to you too."
    e "Sorry, I..."
    e "Good morning."
    scene ch2ep2_475
    with dissolve
    mc "Coffee?"
    scene ch2ep2_476
    with dissolve
    a "I'm good for now."
    scene ch2ep2_477
    with dissolve
    mc "Staying home today?"
    a "Yeah. Helping Sky. I've already asked way too much of her."
    scene ch2ep2_478
    with Dissolve(0.1)
    a "Anyway..."
    e "..." (multiple=2)
    mc "..." (multiple=2)
    a "What did you two numbskulls do, hm?"
    scene ch2ep2_479
    with dissolve
    mc "Word travels fast. Did Moon tell you?"
    a "No. Got it from Sicae."
    mc "They know?"
    a "Mm-hm. That charity of yours still has ties to them, after all."
    e "We were just doing our job."
    a "Right..."
    mc "Klara say anything?"
    a "She said she's reminded you enough. Next time, she'll be the one putting the bullet in your head."
    mc "Ouch..."
    play sound2 phonemessage
    scene ch2ep2_480
    with Dissolve(0.2)
    pause
    scene ch2ep2_481
    with dissolve
    pause 0.3
    $ phone_start()
    $ switch_channel_view("june_dm")
    show screen phone_ui
    $ quick_menu = False
    $ hide_all_phone_channels("june_dm")
    $ lock_phone_screen()
    $ phone_stamp_rel("june_dm")
    $ send_phone_message("June", "hey got a situation", "june_dm")
    $ send_phone_message(phone_config["phone_player_name"], "What's up?", "june_dm")
    $ phone_pause(0.5)
    $ send_phone_message("June", "leah won't talk", "june_dm")
    $ phone_pause(0.5)
    $ send_phone_message("June", "not to me not to dr. park", "june_dm")
    $ phone_pause(0.5)
    $ send_phone_message("June", "not to staff", "june_dm")
    $ phone_pause(0.5)
    $ send_phone_message("June", "she just sits in her room", "june_dm")
    $ send_phone_message(phone_config["phone_player_name"], "Since when?", "june_dm")
    $ phone_pause(0.5)
    $ send_phone_message("June", "since this morning", "june_dm")
    $ phone_pause(0.5)
    $ send_phone_message("June", "hasn't said a word to anyone", "june_dm")
    $ phone_pause(1.0)
    $ send_phone_message("June", "she keeps asking for emma", "june_dm")
    $ send_phone_message(phone_config["phone_player_name"], "Keeps asking? Thought she wasn't talking.", "june_dm")
    $ phone_pause(0.5)
    $ send_phone_message("June", "she wrote it down", "june_dm")
    $ send_phone_message(phone_config["phone_player_name"], "...", "june_dm")
    $ phone_pause(1.0)
    $ send_phone_message("June", "i need emma here, [mc]", "june_dm")
    $ show_all_phone_channels()
    $ unlock_phone_screen()
    show screen phone_blocker
    show screen phone_close_button
    $ send_phone_message(phone_config["phone_player_name"], "I'll tell her.", "june_dm")
    scene ch2ep2_482
    with dissolve
    mc "That was June."
    e "What did she say?"
    mc "... Leah's not talking to anyone. She keeps asking for you."
    scene ch2ep2_483
    with dissolve
    e "..."
    stop sound fadeout 2
    
    scene black
    with dissolve
    with fade

    play sound hospitalambience2 loop
    scene ch2ep2_484
    with dissolve
    mc "Where is she?"
    scene ch2ep2_485
    with dissolve
    ju "In her room."
    e "What do they need from her?"
    scene ch2ep2_486
    with dissolve
    ju "Dr. Park wants a follow-up. See where she's at after the first night."
    ju "But she won't engage. Not with Park, not with the nurses, not with me."
    mc "She talked fine yesterday."
    ju "I know. But somehow, yesterday she knew Emma was in the room."
    e "..."
    ju "Look, I'm not asking you to fix anything. Just... be in there. See if she opens up."
    ju "Then we let Dr. Park know she's ready for the follow-up. That's it."
    scene ch2ep2_487
    with dissolve
    e "Alright."
    play sound2 doorknock
    scene ch2ep2_488
    with dissolve
    pause
    stop sound fadeout 2
    scene ch2ep2_489
    with dissolve
    pause
    play sound2 closedoor2
    scene ch2ep2_490
    with dissolve
    pause
    $ renpy.music.set_volume(1.0, 1.0)
    play music 'audio/CarefreeHearts.mp3'
    scene ch2ep2_491
    with dissolve
    e "Hey."
    scene ch2ep2_492
    with dissolve
    le "Hi."
    e "How'd you sleep?"
    le "Okay. The bed is weird, though."
    e "Too soft?"
    le "Mm-hm. It feels like I'm sinking."
    e "Yeah, hospital beds are like that."
    play sound chair3
    scene ch2ep2_493
    with dissolve
    le "Is he here too?"
    e "[mc]? Yeah, he's right outside."
    le "Oh. That's his name?"
    e "That's his name."
    le "I didn't know. He never told me."
    e "... He can be like that."
    scene ch2ep2_494
    with dissolve
    le "Emma?"
    e "Hm?"
    le "Did you eat breakfast?"
    e "... Coffee counts, right?"
    le "No."
    e "Then no."
    le "That's bad."
    e "I know."
    scene ch2ep2_495
    with dissolve
    le "The nurse brought me toast. It had jelly on it. The grape kind."
    e "Was it good?"
    le "It was okay. The bread was a little cold."
    e "That's hospitals for you."
    scene ch2ep2_496
    with dissolve
    le "Do you like penguins?"
    e "..."
    e "I... don't mind them."
    le "This one doesn't have a name yet."
    e "No?"
    le "I was waiting."
    e "For?"
    le "I don't know. For it to tell me, I guess."
    scene ch2ep2_497
    with dissolve
    pause
    e "That's... a good way to pick a name."
    scene ch2ep2_498
    with dissolve
    le "My mom said names find you. You don't find them."
    e "..."
    scene ch2ep2_499
    with dissolve
    le "What's wrong?"
    e "Nothing. Just listening."
    scene ch2ep2_500
    with dissolve
    pause
    scene ch2ep2_501
    with dissolve
    le "Are you okay?"
    e "Me?"
    le "Mm-hm. The other night."
    e "Oh. I'm okay."
    le "And him? His arm was bleeding."
    e "He's fine. Already healed up."
    le "Okay."
    scene ch2ep2_502
    with dissolve
    pause
    play sound carwindowclose
    scene ch2ep2_503
    with dissolve
    le "There."
    e "Looks like a lineup."
    scene ch2ep2_504
    with dissolve
    le "A what?"
    e "Never mind. It's a work thing."
    scene ch2ep2_505
    with dissolve
    pause
    play sound chair
    scene ch2ep2_506
    with dissolve
    e "Leah."
    le "Yeah?"
    e "The people here... June, Dr. Park... they're trying to help. You know that, right?"
    le "..."
    scene ch2ep2_507
    with dissolve
    e "I know it doesn't feel that way. New faces, new questions, all the time."
    e "But they're on your side. Same as me."
    le "They ask a lot of things."
    e "I know. That's kind of their job."
    le "Your job too?"
    e "... Yeah. Mine too."
    le "But you're different."
    e "I'm really not."
    le "You don't write things down when I talk."
    scene ch2ep2_508
    with dissolve
    e "..."
    scene ch2ep2_509
    with dissolve
    e "They write things down so they can remember. So they can help you better."
    le "Mm."
    e "You don't have to say everything. Just... don't shut them out, okay? They're good people."
    le "..."
    le "Do I have to?"
    e "No. You don't have to do anything."
    e "But it'd help. And I think you'd like Dr. Park if you gave her a chance."
    le "She smells like hand sanitizer."
    e "... Everyone here smells like hand sanitizer."
    le "But you don't."
    le "You smell like coffee."
    scene ch2ep2_510
    with dissolve
    e "Well... that's accurate."
    scene ch2ep2_511
    with dissolve
    pause
    scene ch2ep2_512
    with dissolve
    le "Okay."
    e "Okay?"
    le "I'll try. But only if you're here."
    e "Leah, I can't always—"
    le "Not always. Just... right now."
    e "..."
    e "Yeah. I'm here right now."
    scene ch2ep2_513
    with dissolve
    le "Hold this for me?"
    e "... Sure."
    scene ch2ep2_514
    with dissolve
    pause
    scene ch2ep2_515
    with dissolve
    le "*nods*"
    scene ch2ep2_512
    with dissolve
    le "I think I'll name him later."
    e "Take your time."
    scene ch2ep2_516
    with dissolve
    pause
    stop music
    play sound doorslam3
    scene ch2ep2_517
    with hpunch
    nur "*from the hall* I NEED THAT CART MOVED NOW, PLEASE!"
    play sound3 cloth
    scene ch2ep2_518
    with Dissolve(0.2)
    pause
    scene ch2ep2_519
    with dissolve
    e "Leah?"
    pause
    scene ch2ep2_520
    with dissolve
    e "Leah, hey. It's just a door. Someone in the hall."
    scene ch2ep2_521
    with dissolve
    play music 'audio/AFracturedHeart.mp3'
    pause 0.5
    e "Leah...?" with Dissolve(2.0)
    e "..."
    play sound cloth
    scene ch2ep2_522
    with Dissolve(1.0)
    e "[mc]?"
    e "..."
    play sound running
    scene ch2ep2_523
    with Dissolve(0.2)
    pause 0.5
    play sound closedoor2
    scene ch2ep2_524
    with Dissolve(0.1)
    e "[mc]! Something's wrong with Leah—she won't move!"
    scene ch2ep2_525
    with Dissolve(0.2)
    mc "What? What do you mean?"
    e "I don't know, we were just talking and then—"
    play sound running
    scene ch2ep2_526
    pause 0.5
    play sound closedoor2
    scene ch2ep2_527
    with Dissolve(0.2)
    mc "Leah?"
    scene ch2ep2_528
    with Dissolve(0.2)
    mc "Em. What happened right before this?"
    e "A loud noise in the hall... and she just shut down."
    mc "Damn it."
    scene ch2ep2_529
    with Dissolve(0.1)
    e "[mc], I—what do I do?!"
    mc "Get Dr. Park. Now."
    play sound closedoor2
    scene ch2ep2_530
    with Dissolve(0.2)
    pause
    play sound cloth
    scene ch2ep2_531
    with Dissolve(1.0)
    mc "..."
    scene ch2ep2_532
    with dissolve
    mc "You know... I never told you my name."
    pause
    scene ch2ep2_533
    with dissolve
    mc "Didn't really get the chance."
    pause
    mc "It's [mc]. Just [mc]. Nothing fancy."
    scene ch2ep2_534
    with dissolve
    mc "Nice collection. Got a favorite?"
    pause
    scene ch2ep2_535
    with dissolve
    mc "I'm gonna guess the penguin. Emma used to have one when she was little. Her favorite."
    pause
    mc "Don't tell her I said that, though."
    mc "..."
    scene ch2ep2_536
    with dissolve
    mc "She didn't eat breakfast this morning. Just coffee. Again."
    mc "I tried telling her that's not a meal. She wouldn't hear it."
    mc "She never does."
    scene ch2ep2_537
    with dissolve
    pause
    mc "..."
    mc "Funny thing is... I get it."
    mc "Not wanting people to worry about you."
    scene ch2ep2_538
    with Dissolve(1.0)
    mc "..."
    scene ch2ep2_539
    with dissolve
    pause
    scene ch2ep2_540
    with dissolve
    mc "You don't have to talk. You don't have to do anything."
    mc "I'm just gonna sit here for a bit. That okay?"
    pause
    scene ch2ep2_541
    with dissolve
    pause
    scene ch2ep2_542
    with Dissolve(0.1)
    scene ch2ep2_543
    with Dissolve(0.1)
    scene ch2ep2_542
    with Dissolve(0.1)
    mc "..."
    scene ch2ep2_544
    with dissolve
    scene ch2ep2_545
    with dissolve
    pause 0.5
    scene ch2ep2_546
    with Dissolve(1.0)
    le "..."
    scene ch2ep2_547
    with dissolve
    le "Where's Emma?"
    mc "Getting someone. She'll be right back."
    scene ch2ep2_548
    with dissolve
    le "..."
    le "I couldn't hear anything."
    mc "I know."
    le "It was like... the sound went away. And then everything went away."
    mc "That happens sometimes. It's not your fault."
    le "..."
    le "Is it gonna happen again?"
    mc "Maybe. I don't know."
    mc "But if it does, someone'll be here. Same as right now."
    scene ch2ep2_549
    with dissolve
    le "..."
    scene ch2ep2_550
    with dissolve
    le "Emma has my penguin."
    mc "Yeah. She's holding it for you."
    le "... Can she come back?"
    mc "She's on her way."
    play sound closedoor2
    scene ch2ep2_551
    with dissolve
    pause
    scene ch2ep2_552
    with dissolve
    pause
    scene ch2ep2_553
    with dissolve
    e "*exhales*"
    scene ch2ep2_554
    with dissolve
    drp "Leah? I'm Dr. Park. We talked yesterday, remember?"
    le "Mm-hm."
    drp "I heard you had a rough moment. Mind if I sit with you for a bit?"
    scene ch2ep2_555
    with dissolve
    pause
    scene ch2ep2_556
    with dissolve
    e "I'll be right outside."
    le "... Okay."
    play sound hospitalambience2 fadein 1 loop
    play sound2 closedoor2
    scene ch2ep2_557
    with dissolve
    pause
    play sound2 chair2
    scene ch2ep2_558
    with dissolve
    e "How did you do that?"
    mc "I didn't do anything. I just sat there."
    e "She was gone, [mc]. I touched her and she didn't even—"
    mc "I know."
    e "I should've called a nurse."
    e "That was the first thing I should've done and I just..."
    e "... I went blank."
    scene ch2ep2_559
    with dissolve
    mc "Em—"
    e "I know the protocol for every scenario in that room. Every single one."
    mc "Knowing what it is and knowing what to do about it... aren't the same thing."
    mc "She talked yesterday because of you. She asked for you today. You came."
    mc "This isn't your fault."
    e "I didn't say it was."
    mc "You were about to."
    e "..."
    scene ch2ep2_560
    with dissolve
    e "She said I smell like coffee."
    mc "*chuckles* I mean... you do."
    scene ch2ep2_561
    with dissolve
    mc "..."
    scene ch2ep2_562
    with dissolve
    mc "*taps her leg* You should eat something."
    e "In a bit."
    mc "Leah would disagree."
    e "... Fine."
    stop music fadeout 2
    stop sound fadeout 2

    scene black
    with dissolve
    with fadeq

    "A few hours later..."

    scene black
    with dissolve
    with fadeq

    play sound hospitalambience2 fadein 2 loop
    scene ch2ep2_563
    with dissolve
    pause
    scene ch2ep2_564
    with dissolve
    pause
    stop sound fadeout 1
    play sound2 closedoor2
    scene ch2ep2_565
    with dissolve
    pause
    play music 'audio/TheRhythmOfTheirHearts.mp3'
    scene ch2ep2_566
    with Dissolve(2.0)
    pause
    scene ch2ep2_567
    with Dissolve(2.0)
    pause
    show emmaleahcuddle
    with Dissolve(2.0)
    pause 4.6
    scene ch2ep2_568
    with dissolve
    hide emmaleahcuddle
    mc "..."
    play sound closedoor2
    scene ch2ep2_569
    with dissolve
    pause
    play sound hospitalambience2 fadein 1 loop
    scene ch2ep2_570
    with dissolve
    pause
    play sound2 dialtone loop
    scene ch2ep2_571
    with dissolve
    pause
    play sound2 phoneclick
    scene ch2ep2_572
    with dissolve
    pause 0.5
    ju "Yeah?"
    mc "June."
    ju "What's up?"
    mc "I'm submitting the request."
    ju "..."
    ju "You sure about that?"
    mc "Yeah."
    ju "What changed?"
    scene ch2ep2_573
    with dissolve
    mc "Nothing changed. I just stopped talking myself out of it."
    ju "..."
    ju "Alright. I'll send the forms tonight. Fill them out, don't skip anything, don't embellish. We clear?"
    mc "Clear."
    ju "Park told me what happened. Thanks for being there with her."
    mc "I didn't really do anything."
    ju "That's exactly how you handle it. I appreciate that you know how."
    ju "But it doesn't change what I told you. You know the odds."
    mc "Yeah."
    ju "Okay. I'll be in touch."
    stop sound fadeout 2
    scene ch2ep2_574
    with Dissolve(2.0)
    pause
    scene ch2ep2_575
    with Dissolve(1.0)
    pause
    stop music fadeout 2
    call hide_days
    with dissolve

    scene black
    with dissolve
    with fade

    $ phone_time_add(hours=24)
    show screen day_wednesday with dissolve
    play music 'audio/KlarasSonata2.mp3'
    play sound morningambience loop
    scene ch2ep2_576a
    with dissolve
    pause
    scene ch2ep2_576
    with dissolve
    pause
    scene ch2ep2_577
    with dissolve
    s "Good morning."
    mc "Morning. You seen Emma?"
    s "She left early. Again."
    scene ch2ep2_578
    with dissolve
    mc "Did she say where? It's supposed to be her day off."
    s "Hospital. That's all she said."
    mc "What?"
    scene ch2ep2_579
    with dissolve
    s "Why, what's the big deal?"
    mc "Nothing. It's just..."
    mc "Give me a sec."
    s "... Okay?"
    scene ch2ep2_580
    with dissolve
    $ phone_start() 
    $ switch_channel_view("emma_dm")
    show screen phone_ui
    $ quick_menu = False
    $ hide_all_phone_channels("emma_dm")
    $ lock_phone_screen()
    $ phone_stamp_rel("emma_dm")
    $ send_phone_message(phone_config["phone_player_name"], "Em?", "emma_dm")
    $ phone_pause(0.5)
    $ send_phone_message("Emma", "Yes? Call me if it's an emergency.", "emma_dm")
    $ send_phone_message(phone_config["phone_player_name"], "No, nothing like that.", "emma_dm")
    $ send_phone_message(phone_config["phone_player_name"], "Are you at the hospital?", "emma_dm")
    $ phone_pause(0.5)
    $ send_phone_message("Emma", "That was the plan.", "emma_dm")
    $ phone_pause(1.0)
    $ send_phone_message("Emma", "But Elaine just called. They picked up Leah's mother.", "emma_dm")
    $ send_phone_message(phone_config["phone_player_name"], "Oh...", "emma_dm")
    $ send_phone_message(phone_config["phone_player_name"], "They talking to her?", "emma_dm")
    $ phone_pause(0.8)
    $ send_phone_message("Emma", "Yeah. Elaine's running the interview.", "emma_dm")
    $ send_phone_message(phone_config["phone_player_name"], "Got it. I'm handling some paperwork at the office.", "emma_dm")
    $ send_phone_message(phone_config["phone_player_name"], "I'll swing by the hospital later if you're still around.", "emma_dm")
    $ show_all_phone_channels()
    $ unlock_phone_screen()
    show screen phone_blocker
    show screen phone_close_button
    $ phone_pause(0.2)
    $ send_phone_message("Emma", "Sure.", "emma_dm")
    scene ch2ep2_581
    with dissolve
    s "I heard there was a kid."
    mc "Yeah, but it's... complicated. For now."
    s "I can only imagine."
    scene ch2ep2_582
    with dissolve
    mc "You'd like her, you know."
    s "My hands are full as it is. But thanks."
    stop music fadeout 2
    stop sound fadeout 2
    scene ch2ep2_583
    with dissolve
    pause
    scene ch2ep2_584
    with dissolve
    pause
    e "... She's younger than I expected."
    play music2 'audio/DriftBetweenSignals.mp3'
    scene ch2ep2_585
    with dissolve
    ela "Nadine. You understand why you're here?"
    nad "..."
    scene ch2ep2_586
    with dissolve
    nad "Yeah."
    ela "Okay. Let's keep it simple. How long was Leah with them?"
    nad "Four months. Maybe a little more."
    ela "And before that, she was with you? Just the two of you?"
    nad "Yeah."
    ela "What changed?"
    scene ch2ep2_587
    with dissolve
    nad "Everything."
    ela "That's not an answer to my question."
    nad "... I lost my job. Couldn't make rent. Couldn't keep the lights on. I had nothing left."
    ela "So you handed her off."
    nad "They said they'd take care of her. Better than I could."
    ela "Who told you that?"
    nad "The man who came to me. I don't know his name. He just showed up. Said he knew people, said she'd be fed, looked after. Said it was temporary."
    scene ch2ep2_588
    with dissolve
    pause
    scene ch2ep2_589
    with dissolve
    ela "Did you believe him?"
    nad "I wanted to."
    ela "You wanted to, but...?"
    nad "..."
    ela "Regardless, you took the money."
    nad "Yes... Yes, I did."
    scene ch2ep2_590
    with dissolve
    pause
    scene ch2ep2_591
    with dissolve
    ela "Did you look for her after?"
    nad "I tried the number he gave me. Disconnected after the first week. I also went to the address, but it was empty. I didn't know what to do."
    ela "You could've gone to the police."
    nad "I know."
    scene ch2ep2_592
    with dissolve
    pause
    scene ch2ep2_593
    with dissolve
    ela "Anything else about the man who approached you?"
    nad "He was quiet. Soft-spoken. He didn't look like what he was."
    ela "They almost never do."
    scene ch2ep2_594
    with dissolve
    nad "Is she okay?"
    scene ch2ep2_595
    with dissolve
    pause
    scene ch2ep2_596
    with dissolve
    pause
    scene ch2ep2_597
    with dissolve
    ela "She's safe."
    scene ch2ep2_598
    with dissolve
    nad "That's not what I asked, Officer."
    ela "..."
    scene ch2ep2_599
    with dissolve
    nad "She used to get nightmares when she was little. I'd sing to her—same song every time. She'd calm down before I even got through the first verse."
    nad "..."
    nad "Does she still get them?"
    scene ch2ep2_600
    with Dissolve(0.2)
    pause
    scene ch2ep2_601
    with dissolve
    ela "We'll leave it here for now. Someone else will be in shortly to go over next steps."
    nad "Okay."
    play sound closedoor2
    scene ch2ep2_602
    with dissolve
    pause
    scene ch2ep2_603
    with dissolve
    pause
    scene ch2ep2_604
    with dissolve
    ela "You good?"
    e "Yeah."
    ela "..."
    ela "She asked if Leah was okay."
    e "I heard her."
    scene ch2ep2_605
    with dissolve
    ela "What are you going to do with that?"
    e "... Nothing."
    scene ch2ep2_606
    with dissolve
    pause
    e "I'm going to see Leah."
    scene ch2ep2_607
    with dissolve
    pause
    scene ch2ep2_608
    with dissolve
    ela "Hey! Can I come?"
    e "No. Do your job."
    scene ch2ep2_609
    with dissolve
    ela "Damn it."
    stop music2 fadeout 2

    scene black
    with dissolve
    with fade

    play sound hospitalambience2 fadein 1 loop
    play sound2 doorknock
    scene ch2ep2_610
    with dissolve
    pause
    stop sound fadeout 1
    play sound2 closedoor2
    scene ch2ep2_611
    with dissolve
    pause
    play music 'audio/Carefreehearts.mp3'
    scene ch2ep2_612
    with dissolve
    pause
    scene ch2ep2_613
    with dissolve
    le "Hi."
    e "What are you working on?"
    play sound bookclose
    scene ch2ep2_614
    with Dissolve(0.1)
    le "Nothing."
    play sound2 cloth
    scene ch2ep2_615
    with dissolve
    le "You smell like coffee again. You should try smelling like something else for a change."
    e "Like...?"
    le "I don't know. Flowers? Or like... a bakery. So when you walk in, it smells like something good is about to happen."
    e "That's a high standard. I could step outside and buy some bread."
    le "I'm full."
    play sound chair
    scene ch2ep2_616
    with dissolve
    pause
    le "Did you come straight here?"
    e "Pretty much."
    le "I thought it was your day off."
    scene ch2ep2_617
    with dissolve
    e "How do you know that?"
    le "Aunt June mentioned it."
    e "Oh... She's your aunt now?"
    scene ch2ep2_618
    with dissolve
    le "No, but she could pass for my aunt if my aunt went through a phase in her teenage years."
    e "..."
    le "She said you weren't supposed to be here today."
    e "*sighs* Why does she have to say everything?"
    le "She said the same thing about herself, actually. Especially when she's around her best friends."
    e "Really...?"
    play sound chair
    scene ch2ep2_619
    with Dissolve(0.2)
    le "*clicking her pen*"
    scene ch2ep2_620
    with dissolve
    le "So why did you come?"
    e "I'm... just checking in."
    le "It's your day off though."
    e "Leah."
    le "I'm just saying. You could've done something fun."
    e "This is fine. I can't even remember the last time I did anything fun. Like... actually went outside."
    le "So sitting in a hospital room is fine?"
    e "Sitting in {i}this{/i} hospital room."
    scene ch2ep2_621
    with dissolve
    le "..."
    play sound bookopen
    scene ch2ep2_622
    with dissolve
    pause
    scene ch2ep2_623
    with dissolve
    e "New additions."
    le "Oh... That pretty nurse brought them. She left them on the table when she came to check my blood pressure. I think she felt bad about the needle."
    scene ch2ep2_624
    with dissolve
    e "Did it hurt?"
    le "A little. But I didn't cry."
    scene ch2ep2_625
    with dissolve
    e "You named them yet?"
    le "The green blob is Gerald. He looks like a Gerald. Very serious face. Very dependable."
    e "You can tell all that from a stuffed toy?"
    play sound woosh
    scene ch2ep2_626
    le "I can tell a lot from faces, actually."
    le "Like right now, you look like you didn't finish your lunch."
    scene ch2ep2_627
    with dissolve
    e "I finished most of it."
    le "How much is most?"
    e "More than... half?"
    le "... More than half isn't most. That's half."
    scene ch2ep2_628
    with dissolve
    e "It was a really big sandwich."
    le "Then you should've eaten the whole thing."
    e "..."
    scene ch2ep2_629
    with dissolve
    e "You're starting to sound like [mc]."
    le "Huh?"
    e "I eat often. Just not a lot. And... I usually skip breakfast."
    scene ch2ep2_630
    with dissolve
    le "*shaking her head* Tsk, tsk, tsk..."
    scene ch2ep2_631
    with dissolve
    pause
    scene ch2ep2_632
    with dissolve
    pause
    scene ch2ep2_633
    with dissolve
    e "What about the cat loaf?"
    le "Doesn't have one yet. He's not ready to tell me. Gerald knew right away."
    e "... You really have an odd way of naming things."
    le "Mm-hm. My friends used to say I'm a genius."
    play sound woosh
    scene ch2ep2_634
    pause
    scene ch2ep2_635
    with dissolve
    le "What do you think? For the cat bread."
    e "I'm not good at names."
    le "Try anyway."
    e "I really named my first plant \"Mr. Plant.\""
    le "Yeah, you told me yesterday after the nap. And that it died. I think the name had something to do with it."
    e "Plants don't really know their names."
    le "How would you know?"
    e "I don't... I guess."
    le "Exactly. So try."
    scene ch2ep2_636
    with dissolve
    e "What color is he?"
    le "Brown. Obviously."
    e "Does he look like anyone?"
    scene ch2ep2_637
    with dissolve
    le "..."
    le "He kind of looks like Dr. Park."
    e "I'm telling."
    le "Wait, no!" with hpunch
    e "Kidding. Then maybe something in her lane. Something soft."
    le "..."
    scene ch2ep2_638
    with dissolve
    le "Hm..."
    play sound bookopen
    scene ch2ep2_639
    with dissolve
    le "I'll think about it."
    e "Take your time."
    le "Like Dr. Park?"
    e "*chuckles* Like Dr. Park."
    le "*giggles* She walks so slow. How come?"
    e "She had a leg injury when she was young."
    le "Ah..."
    scene ch2ep2_640
    with dissolve
    e "What is that, anyway?"
    play sound papermovement2
    scene ch2ep2_641
    with dissolve
    le "My diary."
    play sound chairdrag
    scene ch2ep2_642
    with dissolve
    le "I've had it for a while. Since before."
    e "Before the hospital?"
    le "Before mom changed..."
    le "She gave it to me when I was little. She said if something is too big to say out loud, write it down first."
    le "Words find their way out whether you want them to or not, so it's better to give them somewhere to go."
    scene ch2ep2_643
    with dissolve
    e "..."
    scene ch2ep2_644
    with dissolve
    le "Did someone ever teach you that?"
    e "... My mom. Not with a diary, though. Just through letters. She said more or less the same thing."
    le "Did it help?"
    scene ch2ep2_645
    with dissolve
    e "I... kept writing them long after I had anyone left to send them to. So I think it must have."
    le "... Yeah. I think so too."
    scene ch2ep2_646
    with dissolve
    pause
    scene ch2ep2_647
    with dissolve
    e "That's actually a pretty good drawing, by the way."
    le "Is it?"
    e "Yeah."
    le "The other one I gave you was rougher—I didn't have much time."
    e "Wait—is that me?"
    le "The coffee gave it away."
    e "What's the star above the vending machine?"
    le "It gave me grape juice when I hit the peach button. I didn't even want grape juice, but it was still nice. Like a surprise."
    e "Why does the vending machine get a star for that?"
    le "Uhm... because."
    scene ch2ep2_648
    with dissolve
    e "... Okay. Then how many starts do I get?"
    scene ch2ep2_649
    with dissolve
    le "Four and a half."
    e "Out of...?"
    le "Out of five."
    e "What am I losing half a star for?"
    le "The sandwich."
    e "..."
    e "Fair."
    scene ch2ep2_650
    with dissolve
    le "Four and a half is generous, by the way."
    scene ch2ep2_918
    with dissolve
    le "..."
    le "Emma? How long have I been in here?"
    e "Just a few days."
    le "It feels longer. I haven't been outside once."
    le "Everything here smells the same. Sounds the same. Even the light is the same all day."
    e "Leah, I can't really take you out of the building. That's not something I'm allowed to do."
    le "... I see."
    scene ch2ep2_919
    with dissolve
    e "You have a TV. Are you not watching anything?"
    le "I don't like watching TV. And cartoons are so boring."
    scene ch2ep2_920
    with dissolve
    e "... We can walk around if you want."
    le "Like... right now?"
    e "Mm-hm. Right now."
    le "Where, though?"
    e "Downstairs. There's a lobby."
    le "Is it big?"
    e "Not that big, but... bigger than this room, for sure."
    play sound cloth
    scene ch2ep2_921
    with dissolve
    le "Okay!"
    e "Let's get your shoes on first."

    scene black
    with dissolve
    with fade

    play sound hospitalambience2 loop
    play sound2 elevatorclose
    scene ch2ep2_922
    with dissolve
    le "Whoa..."
    e "It's just a lobby, Leah."
    le "It has windows."
    e "I mean... It's a must."
    le "Big ones. With outside in them."
    scene ch2ep2_923
    with Dissolve(0.2)
    e "Hey, hey. Slow down."
    scene ch2ep2_924
    with dissolve
    pause
    le "There's a guy out there walking a really tiny dog. It's wearing a sweater."
    e "The guy?"
    le "The dog."
    le "I think it looks angry about the sweater. I'd hate it."
    e "You don't like sweaters?"
    le "They're okay. I guess it depends on the color."
    scene ch2ep2_925
    with dissolve
    le "Is that the front desk?"
    e "Yeah."
    le "Like a hotel?"
    scene ch2ep2_926
    with dissolve
    e "... Sort of. Don't bother the—"
    play sound2 woosh
    scene ch2ep2_927
    le "Hi!"
    nur "Oh! Hello, sweetheart. Are you lost?"
    scene ch2ep2_928
    with dissolve
    le "No. I'm with her."
    nur "Oh, is that your mom?"
    scene ch2ep2_929
    with dissolve
    le "..."
    le "She's..."
    e "I'm her—"
    scene ch2ep2_930
    with Dissolve(0.1)
    le "She's my Emma."
    nur "Aw... that's sweet."
    e "..."
    scene ch2ep2_931
    with dissolve
    e "Sorry. We're just walking around."
    nur "No worries. Enjoy the tour."
    scene ch2ep2_932
    with Dissolve(0.2)
    le "Do you like working here?"
    nur "Hm? Oh... Most days, yeah. Why do you ask?"
    le "The chairs look comfortable."
    nur "*laughs* They're alright. The ones in the rooms upstairs are worse."
    le "I know. I've been sitting in them."
    scene ch2ep2_933
    with dissolve
    e "..."
    scene ch2ep2_934
    with dissolve
    le "What's your name?"
    nur "Maria."
    le "That's a good name. Did it find you or did someone pick it?"
    nur "I... my parents picked it."
    le "Oh. That works too."
    scene ch2ep2_935
    with Dissolve(0.2)
    e "Alright, come on. Leave Maria alone."
    le "I wasn't bothering her."
    nur "She really wasn't."
    e "..."
    scene ch2ep2_936
    with dissolve
    le "See you later, Maria."
    nur "See you."
    scene ch2ep2_937
    with dissolve
    pause
    scene ch2ep2_938
    with Dissolve(0.2)
    le "These are all flowers."
    e "Mm-hm."
    le "They're in order."
    scene ch2ep2_939
    with dissolve
    e "..."
    e "Are they?"
    le "By color. See? Yellow, something that looks like peach, and then pink. Someone arranged them."
    scene ch2ep2_940
    with dissolve
    e "How's that in order? I think that's just decoration, Leah."
    le "Decoration still has a reason. Someone definitely chose this order."
    e "... I'm confused."
    le "Which one do you like?"
    scene ch2ep2_941
    with dissolve
    e "I don't really have opinions about flowers."
    le "There you go again. You're really no fun."
    scene ch2ep2_942
    with Dissolve(1.0)
    e "..."
    e "Then I'll pick the white one. Second row."
    le "Can you tell me why?"
    scene ch2ep2_943
    with dissolve
    e "It looks simple enough. It's not trying too hard to be a flower..."
    e "... Which is ironic."
    le "Ironic? Why?"
    e "It's nothing... Let's just move somewhere else."
    le "Okay."
    scene ch2ep2_944
    with dissolve
    pause
    le "Oh..."
    e "Your old friend."
    scene ch2ep2_945
    with dissolve
    le "It owes me a correct drink."
    e "Right..."
    le "The one from school gave me grape juice when I pressed peach."
    scene ch2ep2_946
    with dissolve
    e "Maybe you pressed the wrong button?"
    le "I pressed the right one. The machine had its own ideas."
    scene ch2ep2_947
    with dissolve
    e "Go on."
    play sound2 vendingmachine_click
    scene ch2ep2_948
    with Dissolve(0.2)
    pause
    play sound3 vendingmachine_drop
    scene ch2ep2_949
    with Dissolve(0.1)
    pause 0.5
    le "..."
    scene ch2ep2_950
    with dissolve
    le "Orange."
    e "..."
    le "I pressed peach one."
    e "Mm."
    le "It gave me orange."
    e "..."
    le "Don't do that."
    e "I'm not doing anything."
    le "Your face is doing something."
    play sound2 woosh
    scene ch2ep2_951
    e "..."
    le "I saw that."
    e "Saw what? I'm looking at the wall."
    play sound2 woosh
    scene ch2ep2_952
    le "You're laughing."
    e "I'm not laughing."
    le "Your shoulders are moving."
    e "..."
    scene ch2ep2_953
    with dissolve
    le "..."
    e "... It's a little funny."
    scene ch2ep2_954
    with dissolve
    le "It's not funny. It's a pattern. Vending machines doesn't respect me."
    e "Maybe it's just giving you what you need instead of what you want."
    le "..."
    le "That's what Dr. Park says."
    e "I mean... she's not wrong."
    le "Don't take her side."
    scene ch2ep2_955
    with dissolve
    le "... Orange isn't bad, though."
    e "Yeah. It's good for you."
    play sound2 chair
    scene ch2ep2_956
    with hpunch
    pause 0.5
    le "These are definitely better."
    e "Than the ones in your room?"
    le "Uh-huh. It's way better. Whoever picked these actually sat in one first."
    e "..."
    scene ch2ep2_957
    with dissolve
    le "Emma?"
    e "Yeah?"
    le "What did you want to be when you were little?"
    e "... A vet."
    le "Really?"
    e "Only for about two weeks. Then I realized you have to touch the animals when they're sick, and some of them bite."
    le "So you quit?"
    e "I was five. It wasn't quitting. It was a career change."
    le "*giggles* A career change."
    le "What happened after the vet thing?"
    scene ch2ep2_958
    with dissolve
    e "I wanted to be a detective, actually. My teachers gave me the idea. Said I was good at problem solving."
    le "Wait, you actually became one, though."
    e "Not right away. Somewhere in between, I wanted to be one of those people who travel everywhere with a suitcase and a notebook."
    le "What do they call it? A journalist?"
    e "I didn't really know what it was. But something along that line."
    e "I just wanted to knock on doors in places I'd never been and ask people if they'd seen someone."
    le "Seen who?"
    scene ch2ep2_959
    with dissolve
    e "It's a secret."
    le "... Alright then. Keep your secrets."
    le "So you went back to detective?"
    e "Eventually. Turns out knocking on doors and asking questions is most of the job anyway."
    le "..."
    le "So you got both."
    e "I guess I did."
    e "What about you? When you were little."
    le "I'm still little."
    e "Littler, then."
    play sound2 woosh
    scene ch2ep2_960
    le "Oh, I wanted to draw maps."
    e "Maps? The world map kind of maps?"
    le "Not real maps. Made-up ones. Like... places that don't exist but feel like they should."
    le "I'd name the rivers and the mountains and the towns. Then every town had a mayor with a story."
    e "... Do you still draw them?"
    le "No... Not anymore."
    le "My diary used to have some in the back. But the pages got ruined when we moved houses once."
    le "I kept the names, though. In my head."
    e "Tell me one."
    scene ch2ep2_961
    with dissolve
    le "There was one called Fenhollow. It was next to a lake that looked different to everyone who saw it."
    e "Your imagination really surprises me."
    le "Then the mayor's name was Constance. Then she had one rule: no one was allowed to lie on Tuesdays."
    e "Just Tuesdays? Like a rest day?"
    le "Yeah. Lying is tiring. You need to rest from it sometimes."
    scene ch2ep2_962
    with dissolve
    e "..."
    scene ch2ep2_963
    with dissolve
    le "You're doing the face again."
    e "What face?"
    le "The one where you're trying not to like something too much."
    e "... I don't have that face."
    le "You had it when I gave you the drawing. And when I told you about the penguin. And just now, with Fenhollow."
    e "You... You noticed all that?"
    le "Uh-huh?"
    e "That's a little unsettling."
    scene ch2ep2_964
    with dissolve
    le "Can I tell you something though?"
    e "Yeah. What is it?"
    le "This is the first time I've been somewhere in this building that isn't my room or the exam room."
    le "It's the same building, but it doesn't feel the same."
    e "Let me guess, because of the chairs?"
    le "Because of you."
    e "..."
    le "My room has you in it sometimes. But it also has the nurses, and the questions, and the door that opens for people I don't know."
    le "Down here, it's just us. I like that better."
    scene ch2ep2_965
    with dissolve
    le "Am I weird?"
    e "No. No, you're not."
    le "You sure?"
    e "Of course. You just surprise me sometimes, that's all."
    le "... Some people say I am."
    e "Trust me, you're not."
    le "... Alright. I believe you."
    scene ch2ep2_966
    with dissolve
    e "Actually, we should head back up. June doesn't know we're down here."
    le "Five more minutes?"
    scene ch2ep2_967
    with dissolve
    e "Leah..."
    le "Three."
    e "... Alright. Three."
    play sound2 woosh
    scene ch2ep2_968
    le "Hey, what's that?"
    scene ch2ep2_969
    with Dissolve(0.2)
    e "Hm?"
    scene ch2ep2_970
    with Dissolve(1.0)
    pause
    scene ch2ep2_971
    with dissolve
    e "Uhm... What was that for?"
    scene ch2ep2_972
    with dissolve
    le "A thank you kiss."
    scene ch2ep2_973
    with dissolve
    pause
    stop music fadeout 2
    stop sound fadeout 2

    scene black
    with dissolve
    with fade

    play sound hospitalambience2 fadein 1 loop
    scene ch2ep2_651
    with dissolve
    e "Yeah, heading out now. Give me two minutes."
    mc "How's she holding up?"
    scene ch2ep2_652
    with dissolve
    e "She's doing good. I'll explain when I get there."
    e "Anyway, I'm on—"
    play sound2 cloth2
    scene ch2ep2_653
    with hpunch
    ju "Oh—"
    e "Sorry."
    ju "No, that was me."
    scene ch2ep2_654
    with dissolve
    pause
    scene ch2ep2_655
    with dissolve
    pause
    scene ch2ep2_656
    with dissolve
    ju "Everything alright?"
    e "Yeah. Just stopped by."
    ju "Mm."
    scene ch2ep2_657
    with dissolve
    pause
    scene ch2ep2_658
    with dissolve
    ju "*nods* Get home safe."
    play sound2 closedoor2
    scene ch2ep2_659
    with dissolve
    pause
    scene ch2ep2_660
    with dissolve
    pause
    scene ch2ep2_661
    with dissolve
    e "... Yeah. I'm on my way."
    scene ch2ep2_662
    with dissolve
    pause
    scene ch2ep2_663
    with dissolve
    pause
    scene ch2ep2_664
    with dissolve
    pause
    stop sound fadeout 2

    scene black
    with dissolve
    with fade

    play sound ceilingfan_low loop fadein 2
    scene ch2ep2_665
    with dissolve
    frs "Boss. I got something."
    fr "Talk."
    scene ch2ep2_666
    with dissolve
    frs "She talked. Full interview—cooperated the whole way through."
    frs "Locations, what the place smelled like, how many times she was moved. She spilled almost everything."
    fr "And the rest?"
    frs "She described you. Said there was a man. That he was nice to her. That he reminded her of someone."
    frs "His sister."
    fr "..."
    fr "*exhales slowly* She remembered."
    fr "She remembered..."
    play sound2 chair2
    scene ch2ep2_667
    with dissolve
    fr "Do you know how many there were before her?"
    scene ch2ep2_668
    with dissolve
    frs "..."
    fr "The one before Leah stopped speaking by the third week. Gutted out from the inside—took everything with it. I had to let her go."
    frs "..."
    fr "The one before that lasted longer."
    fr "She remembered the hair. The way Vi used to hum when she was nervous."
    fr "For a while I was certain she was the one. But she started to fight—and fighting ruins everything."
    fr "Not one of them ever described me the way Leah did. \"The man who was nice.\" She's not afraid of me. Not even after everything."
    fr "That means everything I built with her is still there."
    scene ch2ep2_669
    with dissolve
    frs "She's in protective custody. CPS has a caseworker on her. If we move now—"
    fr "I'm not going to rip her out of there. She has to want to come home."
    frs "There's one more thing. The caseworker—she has a connection to both officers from Ashen."
    fr "Tell our contact to keep watching."
    frs "Copy that, boss."
    play sound2 closedoor2
    scene ch2ep2_670
    with dissolve
    pause
    fr "No more breaking, Vi. I just have to be patient this time."
    stop sound fadeout 2
    
    scene black
    with dissolve
    with fadeq

    play sound cityalley fadein 2 loop
    play sound2 cardoorclose
    scene ch2ep2_671
    with dissolve
    pause
    mc "Em?"
    scene ch2ep2_672
    with dissolve
    e "Hm?"
    mc "..."
    scene ch2ep2_673
    with dissolve
    e "What?"
    mc "Nothing. You good?"
    e "Yeah."
    scene ch2ep2_674
    with dissolve
    pause
    stop sound fadeout 2
    call hide_days
    with dissolve

    scene black
    with dissolve
    with fade

    $ phone_time_add(hours=24)
    show screen day_thursday with dissolve
    play sound policestation_ambience fadein 2 loop
    scene ch2ep2_675
    with dissolve
    ela "Tell me we have some creamer left in here."
    e "We don't."
    ela "We always have creamer."
    scene ch2ep2_676
    with dissolve
    e "Chen finished it yesterday."
    ela "Of course he did."
    scene ch2ep2_677
    with dissolve
    ela "Ugh... This tastes like a parking garage."
    e "It's the same coffee we always have."
    ela "Yeah, and I've always hated it. The creamer was doing a lot of the heavy lifting."
    scene ch2ep2_678
    with dissolve
    pause
    scene ch2ep2_679
    with dissolve
    ela "Nadine's lawyer called this morning."
    e "Already?"
    ela "Public defender. Just making contact."
    e "What's there even to defend?"
    ela "She handed her kid over to a trafficking ring, but she didn't know what it was. Or claims she didn't."
    e "Does it matter?"
    ela "To a jury? *scoffs* Maybe. To Leah? Probably not."
    scene ch2ep2_680
    with dissolve
    ela "*exhales* Nothing to it yet, really. Just establishing the line."
    e "Mm."
    scene ch2ep2_681
    with dissolve
    ela "Oh. The Captain wants the Ashen report finalized by Friday. Everything we have on Francis."
    e "I'll have it done by tomorrow, don't worry."
    ela "Yeah... I told him that. Still looked skeptical."
    e "What else is new? His face is made from skepticism."
    ela "Pfft... Look who's talking."
    scene ch2ep2_682
    with dissolve
    pause
    scene ch2ep2_683
    with dissolve
    ela "How many times have you been back to the hospital?"
    e "It's part of the case."
    ela "Emma..."
    scene ch2ep2_684
    with dissolve
    e "What?"
    ela "You went yesterday. I almost forgot, but seriously, on your day off?"
    e "..."
    ela "I'm not going to write it up or make it a thing. I just want to know if you know what you're doing."
    scene ch2ep2_685
    with dissolve
    pause
    scene ch2ep2_686
    with dissolve
    ela "Okay."
    scene ch2ep2_687
    with dissolve
    pause
    scene ch2ep2_688
    with dissolve
    ela "She's a good kid, Em. But that's not the problem, is it?"
    scene ch2ep2_689
    with dissolve
    pause
    stop sound fadeout 2

    scene black
    with dissolve
    with fade

    $ phone_time_add(hours=16)
    play sound nightambience2 fadeout 2 loop
    play sound2 doorknock
    scene ch2ep2_690
    with dissolve
    e "[mc]? You still up?"
    pause
    play sound2 opendoor
    scene ch2ep2_691
    with dissolve
    mc "... Well, I am now."
    e "Sorry, I couldn't sleep."
    e "Can I borrow your truck? I won't be long."
    mc "Huh? Where to?"
    e "..."
    e "The hospital."
    mc "Em, it's almost midnight."
    scene ch2ep2_692
    with dissolve
    e "I know."
    mc "Visiting hours—"
    e "I know..."
    scene ch2ep2_693
    with dissolve
    mc "..."
    scene ch2ep2_694
    with dissolve
    pause
    scene ch2ep2_695
    with dissolve
    pause
    scene ch2ep2_696
    with dissolve
    pause
    scene ch2ep2_697
    with dissolve
    mc "You couldn't sleep."
    e "No."
    mc "..."
    scene ch2ep2_698
    with dissolve
    pause
    scene ch2ep2_699
    with dissolve
    menu:
        "I'll take you":
            mc "I'll take you."
            $ emmapoint += 1
            $ renpy.notify(emmanotif)
            e "I appreciate it, but I'll be fine. I'd... rather go alone this time."
            mc "Yeah. I figured."
            scene ch2ep2_700
            with dissolve
            mc "The tank's full. Don't speed."
        "Here":
            scene ch2ep2_700
            with dissolve
            mc "Here."
            mc "The tank's full. Don't speed."
    e "... Thanks."
    scene ch2ep2_701
    with dissolve
    pause
    scene ch2ep2_702
    with Dissolve(0.2)
    mc "Emma."
    scene ch2ep2_703
    with Dissolve(0.1)
    pause
    scene ch2ep2_704
    with dissolve
    pause
    stop sound fadeout 2

    scene black
    with dissolve
    with fade

    scene ch2ep2_705
    with dissolve
    pause
    scene ch2ep2_706
    with dissolve
    cara "Detective Meyer?"
    e "Hey, uh..."
    cara "Visiting hours ended at eight."
    scene ch2ep2_707
    with dissolve
    e "I won't be long. I just... I want to check on her."
    cara "..."
    scene ch2ep2_708
    with dissolve
    pause
    scene ch2ep2_709
    with dissolve
    cara "... She had a rough night, Detective."
    e "Please..."
    scene ch2ep2_710
    with dissolve
    pause
    scene ch2ep2_711
    with dissolve
    pause
    scene ch2ep2_712
    with dissolve
    pause
    play sound closedoor2
    scene ch2ep2_713
    with dissolve
    pause
    play music 'audio/TheRhythmOfTheirHearts_var.mp3'
    scene ch2ep2_714
    with Dissolve(1.0)
    pause
    scene ch2ep2_715
    with Dissolve(1.0)
    pause
    scene ch2ep2_716
    with dissolve
    e "Bad dream?"
    le "Mm..."
    e "Want to talk about it?"
    le "No..."
    e "Okay."
    scene ch2ep2_717
    with dissolve
    le "You came from home?"
    e "Yeah."
    le "It's late."
    scene ch2ep2_718
    with dissolve
    le "Couldn't sleep either?"
    e "*nods* ... Something like that."
    scene ch2ep2_719
    with Dissolve(0.2)
    play sound chair_tap
    pause
    play sound2 chair
    scene ch2ep2_720
    with dissolve
    pause
    play sound3 cloth
    scene ch2ep2_721
    with dissolve
    pause
    scene ch2ep2_722
    with dissolve
    le "Those letters you wrote. Did you ever go back and read them?"
    e "Some of them."
    le "Were they hard to read?"
    e "The older ones."
    le "How come?"
    e "You write differently when you're young. You say things you'd never say out loud."
    le "Like what?"
    scene ch2ep2_723
    with dissolve
    e "..."
    e "... Some honest things."
    scene ch2ep2_724
    with dissolve
    pause
    scene ch2ep2_725
    with dissolve
    le "My mom used to say honesty is just bravery with bad timing."
    e "She said that to you?"
    le "Yep. When I told her I didn't like her cooking."
    scene ch2ep2_726
    with dissolve
    pause
    scene ch2ep2_727
    with dissolve
    le "What was yours like?"
    e "My mom?"
    le "Mm."
    e "..."
    scene ch2ep2_728
    with dissolve
    e "Practical... Warm... The kind of person who showed up before you could even ask."
    e "She used to iron my uniform the night before school. Even when I told her I didn't care what I looked like."
    e "She cared..."
    e "... too much."
    le "..."
    scene ch2ep2_729
    with dissolve
    le "Do you miss her?"
    e "Every day."
    e "..."
    e "It's... a specific kind of lonely, and it doesn't matter who's in the room with you."
    e "I've got [mc]... My friends... People who would drop everything if I called."
    e "But there's a part of you that only a mother knows how to reach."
    e "And when she's gone... that part stays quiet."
    le "Does it get smaller? The missing?"
    e "..."
    e "It gets a little easier. That's the best I can tell you."
    scene ch2ep2_730
    with dissolve
    le "*slowly nods*"
    play sound cloth
    scene ch2ep2_731
    with dissolve
    le "Emma?"
    e "Hm?"
    le "Will you stay until I fall asleep?"
    e "Leah, I shouldn't—"
    scene ch2ep2_732
    with dissolve
    le "..."
    scene ch2ep2_733
    with Dissolve(1.0)
    pause
    e "Yeah... Yeah, I'll stay."
    scene ch2ep2_734
    with Dissolve(1.0)
    pause
    scene ch2ep2_735
    with Dissolve(1.0)
    pause
    scene ch2ep2_736
    with Dissolve(1.0)
    pause
    scene ch2ep2_737
    with Dissolve(1.0)
    pause
    scene ch2ep2_738
    with Dissolve(2.0)
    pause
    stop music fadeout 2
    call hide_days
    with dissolve

    scene black
    with dissolve
    with fade

    $ phone_time_add(hours=8)
    show screen day_friday with dissolve
    play sound morningambience loop
    scene ch2ep2_739
    with dissolve
    k "[mc]."
    scene ch2ep2_740
    with dissolve
    k "Your key."
    scene ch2ep2_741
    with dissolve
    mc "The one who gave you this—she still around?"
    scene ch2ep2_742
    with dissolve
    k "There's no body in the driveway, so presumably."
    mc "What time did she get in?"
    k "Almost six in the morning. Should I be concerned?"
    scene ch2ep2_743
    with dissolve
    mc "... It's the kid."
    k "..."
    k "Maybe she's just worried about her?"
    mc "No. That's not it."
    scene ch2ep2_744
    with dissolve
    k "*exhales* Anyway, go grab Moon. I need you two today."
    mc "Groceries?"
    k "That, and decorations. It's almost Christmas and we're already behind."
    k "And you're forgetting something, aren't you?"
    mc "Oh, nah... How could I forget? It's that time of the year."
    play sound2 doorbell
    scene ch2ep2_745
    with dissolve
    pause
    play sound3 opendoor
    scene ch2ep2_746
    with dissolve
    ju "Morning."
    mc "You could've called."
    ju "I could've. But you would've asked questions I didn't want to answer over the phone."
    scene ch2ep2_747
    with dissolve
    ju "Your request was rejected."
    mc "..."
    ju "Conflict of interest. Optics. The same things I told you when you asked."
    mc "That's... fast."
    ju "I couldn't slow it down even if I wanted to."
    scene ch2ep2_748
    with dissolve
    ju "I warned you."
    mc "Yeah..."
    ju "I need to know you heard me then, and that you're hearing me now."
    mc "I heard you."
    ju "That's good. Because what comes next is out of my hands, [mc]."
    scene ch2ep2_749
    with dissolve
    pause
    scene ch2ep2_750
    with dissolve
    ju "*nods*"
    scene ch2ep2_751
    with dissolve
    ju "The placement hearing's scheduled tomorrow."
    mc "How solid is the placement?"
    ju "Solid enough. Family out of the north side. Clean record, prior experience with trauma cases."
    ju "On paper, it's the right call."
    mc "..."
    ju "I know what you're thinking. You're thinking paper doesn't know Leah."
    ju "You're not wrong. But that's not how this works, and you know it."
    scene ch2ep2_752
    with dissolve
    pause
    scene ch2ep2_753
    with dissolve
    ju "Talk to Emma before the hearing. She needs to know."
    mc "I will."
    ju "Today, [mc]. Not tomorrow."
    mc "Yeah, yeah, I got it."
    ju "*nods*"
    scene ch2ep2_754
    with dissolve
    pause
    scene ch2ep2_755
    with dissolve
    ju "[mc]... I really tried looking for a reason you'd get past the optics."
    mc "Thanks."
    ju "*shaking her head* But you're just at the wrong time... and the wrong place."
    scene ch2ep2_756
    with dissolve
    pause
    play sound2 cardriveaway
    scene ch2ep2_757
    with dissolve
    k "..."
    scene ch2ep2_758
    with dissolve
    k "Tomorrow, huh?"
    mc "Yeah..."
    scene ch2ep2_759
    with dissolve
    k "You tried. That's good enough."
    stop sound fadeout 2

    scene black
    with dissolve
    with fade

    play sound policestation_ambience fadeout 2 loop
    play sound2 closedoor2
    scene ch2ep2_760
    with dissolve
    cap "Meyer."
    e "Sir."
    cap "Ashen report. I've read it."
    scene ch2ep2_761
    with dissolve
    cap "Francis Mentzelopoutous. No confirmed address. Tied to Ashen's operations for at least the past month."
    cap "And if your boy's file is anything to go by, the man's been at this considerably longer than that."
    e "Correct."
    cap "SWAT swept the building. Nothing on Francis."
    scene ch2ep2_762
    with dissolve
    e "He wasn't there. Leah never placed him at Ashen directly."
    cap "Which means he's still walking about freely with absolutely no heat on him."
    e "Yes."
    cap "Marvellous."
    play sound2 papermovement2
    scene ch2ep2_763
    with dissolve
    cap "The girl. Leah Warren."
    e "Protective custody. Cooperating with DFCS since Monday."
    cap "Right. That's the tidy bit."
    cap "The rest is considerably less so."
    cap "No warrant."
    e "Exigent circumstances. The report covers—"
    play sound2 bookdrop
    scene ch2ep2_764
    cap "I've read the report, Meyer. Twice, in fact. Didn't get more enjoyable the second time around."
    play sound2 chair2
    scene ch2ep2_765
    with dissolve
    cap "I'm not disputing the call. The child's out—that still counts. Quite a lot, actually."
    cap "What I am saying is that \"exigent circumstances\" is a phrase that only holds water if no one goes poking at it."
    cap "And someone will go poking at it."
    scene ch2ep2_766
    with dissolve
    e "..."
    cap "The rescue stands. I'll back it. But Francis is still out there, Ashen is still a live crime scene, and your name is on the whole bloody lot of it."
    cap "So let's be sensible about what comes next."
    play music 'audio/AFracturedHeart.mp3' fadein 2
    cap "The placement, the hearings, whatever becomes of the girl afterward—that's not your department. Literally and otherwise."
    cap "The kindest thing you can do for that child right now is to tie up this loose end cleanly and let the right people sort the rest."
    cap "Closure, Meyer. For her sake as much as yours."
    play sound2 chair2
    scene ch2ep2_767
    with dissolve
    cap "In my experience, the cases that follow detectives home aren't the ones that went sideways."
    cap "They're the ones that went right."
    cap "You pull someone out of something like that and your brain starts writing a story that isn't yours to finish."
    cap "Your job ended at the loading dock."
    cap "Find Francis. That's where your head ought to be."
    scene ch2ep2_768
    with dissolve
    pause
    cap "Meyer."
    scene ch2ep2_769
    with dissolve
    e "Sir?"
    cap "Good work on Ashen. Don't make me say it again."
    e "*nods*"
    play sound2 closedoor2
    scene ch2ep2_770
    with dissolve
    pause
    scene ch2ep2_771
    with dissolve
    pause
    scene ch2ep2_772
    with dissolve
    pause
    scene ep5_5
    with flash
    em "But I don't need one! Mom should be my prince instead!"
    em "You love me and are always here for me. You always take care of me when I'm sick. And your food is always yummy."
    em "And... hhm..."
    scene ep5_6
    with dissolve
    d "My... my... You're such a sweet little girl. Of course, mom will always be here for you."
    d "Even on the day you marry your prince, mom and Emy will still be together."
    em "Forever...?"
    d "Yes, Emy... Forever."
    scene ch2ep2_772
    with flash
    pause
    scene ch2ep2_773
    with Dissolve(1.0)
    pause
    stop sound fadeout 2
    
    scene black
    with dissolve
    with fade

    scene ch2ep2_774
    with Dissolve(1.0)
    pause
    scene ch2ep2_775
    with Dissolve(1.0)
    pause
    scene ch2ep2_776
    with Dissolve(1.0)
    pause
    scene ch2ep2_777
    with dissolve
    pause
    scene ch2ep2_778
    with Dissolve(0.1)
    pause
    scene ch2ep2_779
    with Dissolve(1.0)
    pause
    scene ch2ep2_780
    with Dissolve(1.0)
    pause
    scene ch2ep2_781
    with Dissolve(1.0)
    pause
    call hide_days
    with dissolve

    scene black
    with dissolve
    with fade

    show screen day_saturday with dissolve
    play sound nightambience2 fadein 2 loop
    scene ch2ep2_782
    with Dissolve(1.0)
    pause
    scene ch2ep2_783
    with Dissolve(1.0)
    pause
    scene ch2ep2_784
    with Dissolve(0.1)
    mc "Em."
    scene ch2ep2_785
    pause
    scene ch2ep2_786
    with Dissolve(0.1)
    pause
    scene ch2ep2_787
    with dissolve
    pause
    scene ch2ep2_788
    with dissolve
    mc "Funny. Moon was standing right here after we got Leah out."
    e "..."
    mc "I called June. She said you weren't at the hospital. It's past midnight. Where have you been?"
    e "I don't know..."
    mc "You walked here?"
    e "..."
    scene ch2ep2_789
    with dissolve
    mc "Em. That's forty minutes on foot."
    e "I needed air."
    mc "Forty minutes' worth?"
    e "..."
    scene ch2ep2_790
    with dissolve
    mc "June also told me Leah was waiting for you."
    e "..."
    mc "She left the door open."
    e "..."
    mc "Apparently keeps it cracked open so she can hear the hall."
    e "Don't..."
    mc "She's not asking for you. She's not writing it down, not making a fuss."
    mc "Simply left the door open."
    e "[mc]—"
    scene ch2ep2_791
    with Dissolve(0.1)
    mc "Because you always show up eventually."
    e "..."
    mc "Wasn't she supposed to be just a case number?"
    e "..."
    mc "Your words."
    e "That's not fair."
    mc "For Leah? No. It really isn't."
    scene ch2ep2_792
    with dissolve
    pause
    scene ch2ep2_793
    with dissolve
    mc "I wanted you to look after her, Em. But not like this."
    e "..."
    mc "So what's the play?"
    e "I don't know."
    mc "That's not gonna cut it anymore."
    play sound2 cloth2
    scene ch2ep2_794
    with hpunch
    e "I said I don't know!"
    scene ch2ep2_795
    with dissolve
    mc "Hearing's later. You know what comes after."
    e "..."
    mc "Six months from now, she's in some foster home still wondering why you didn't show up today. Can you sit with that?"
    e "... What I feel doesn't factor into this."
    mc "It factors into a ten-year-old sitting in the dark with her door cracked open waiting for someone who didn't come."
    scene ch2ep2_796
    with Dissolve(0.1)
    pause
    mc "Don't look away from me right now, Emma!"
    scene ch2ep2_797
    with hpunch
    e "I don't know how to do this, [mc]! I don't even know when it stopped being just a case!"
    mc "..."
    scene ch2ep2_798
    with dissolve
    mc "Come inside. Get your head straight before the hearing."
    play sound2 closedoor
    scene ch2ep2_799
    with dissolve
    pause
    scene ch2ep2_800
    with dissolve
    pause
    scene ch2ep2_801
    with Dissolve(1.0)
    pause
    stop sound fadeout 2
    stop music fadeout 2

    scene black
    with dissolve
    with fade

    $ phone_time_add(hours=27)
    play sound hospitalambience2 fadein 2 loop
    scene ch2ep2_802
    with dissolve
    pause
    scene ch2ep2_803
    with dissolve
    ju "Did you tell her?"
    mc "I did what you told me to."
    scene ch2ep2_804
    with dissolve
    ju "What the hell does that mean?"
    mc "*exhales*"
    ju "Is she inside?"
    mc "Yeah."
    ju "Did they talk?"
    mc "Don't know. Doubt it."
    scene ch2ep2_805
    with dissolve
    pause
    stop sound fadeout 1
    play sound2 closedoor2
    scene ch2ep2_806
    with dissolve
    pause
    scene ch2ep2_807
    with dissolve
    ju "Leah."
    le "Hm?"
    ju "I need to talk to you about something. Is that okay?"
    le "Okay."
    play sound chair3
    scene ch2ep2_808
    with dissolve
    ju "So... I've got some news."
    ju "Good news, actually."
    le "..."
    scene ch2ep2_809
    with dissolve
    play music 'audio/AFracturedHeart.mp3'
    ju "You know how we've been looking for a place for you to stay, right? Somewhere a little more... long-term than here."
    le "Mm."
    ju "Well, we found one. A family. They live up on the north side—really nice neighborhood."
    ju "I've met them myself. They're really good people, Leah."
    ju "They've had kids stay with them before. Kids who've been through a lot, same as you."
    ju "And they're... really excited to meet you."
    ju "You'd have your own room. You can bring everything with you—Gerald, your diary, all of them."
    ju "It's not forever. Just... for now, until we find the right permanent fit."
    ju "Think of it like... the next step."
    le "..."
    scene ch2ep2_810
    with dissolve
    le "When?"
    ju "It's tomorrow."
    le "..."
    scene ch2ep2_811
    with dissolve
    pause
    scene ch2ep2_812
    with dissolve
    pause
    scene ch2ep2_813
    with dissolve
    ju "Do you have any questions? You can ask me anything, Leah."
    le "... Can you leave us?"
    ju "..."
    play sound chair2
    scene ch2ep2_814
    with dissolve
    pause
    scene ch2ep2_815
    with dissolve
    pause
    scene ch2ep2_816
    with dissolve
    pause
    scene ch2ep2_817
    with dissolve
    ju "I'll be right outside."
    le "Okay."
    play sound closedoor2
    scene ch2ep2_818
    with dissolve
    pause
    scene ch2ep2_819
    with dissolve
    le "You said I'd be okay."
    e "..."
    scene ch2ep2_820
    with dissolve
    le "Did you lie?"
    e "Leah?"
    le "Did you lie to me?"
    e "The placement is temporary. June vetted the family personally—"
    le "I don't care about the family."
    e "They have experience with kids who've been through—"
    le "I don't care."
    e "It's a safe environment. You'll have your own room, your things—"
    le "Emma... I don't care about the room."
    scene ch2ep2_821
    with dissolve
    e "..."
    scene ch2ep2_822
    with dissolve
    pause
    scene ch2ep2_823
    with dissolve
    le "Why are they moving me so fast?"
    e "It's standard procedure for—"
    le "Stop."
    e "What?"
    le "Stop talking like that."
    e "Leah, I'm trying to—"
    scene ch2ep2_824
    with Dissolve(0.1)
    le "Stop talking like I'm work!"
    scene ch2ep2_825
    with dissolve
    e "Leah, I want you to understand that this decision was made with your best interests—"
    le "You promised."
    e "I didn't promise—"
    le "You said I'd be okay!"
    e "And you will be. The placement is—"
    play sound thud3
    scene ch2ep2_826
    with hpunch
    le "STOP SAYING THAT!"
    le "You keep saying the same things over and over and none of it is what I'm asking!"
    le "I'm asking why you're letting them take me!"
    scene ch2ep2_827
    with Dissolve(0.2)
    e "It's not my call to make. That's not how this works—"
    le "Then whose call is it?!"
    e "June's. The system's. There are people whose job it is to—"
    scene ch2ep2_828
    with Dissolve(0.1)
    le "You're a person!"
    e "..."
    le "You're right there and you keep saying it's somebody else's job!"
    scene ch2ep2_829
    with dissolve
    pause
    scene ch2ep2_830
    with dissolve
    e "I know this is hard—"
    scene ch2ep2_831
    le "Then do something!"
    e "Leah, there's nothing I can—"
    le "YES THERE IS~!"
    e "..."
    le "You can tell them no!"
    le "You can do SOMETHING instead of just standing there talking about procedures and families and ROOMS!"
    le "I don't even know what half of that means!"
    scene ch2ep2_832
    with dissolve
    pause
    scene ch2ep2_833
    with Dissolve(0.1)
    e "What do you want from me, Leah?! I said there's nothing—!"
    scene ch2ep2_834
    le "I want you to fight for me!"
    e "..."
    le "You already did once! You ran into that place and got me out!"
    le "So why can't you do it again?!"
    le "Why won't you, huh...?! WHY WON'T YOU~?!"
    scene ch2ep2_835
    with dissolve
    pause
    scene ch2ep2_836
    with dissolve
    e "That's the thing..."
    e "I wish I never took this case..."
    scene ch2ep2_837
    with dissolve
    le "..."
    e "I wish I never pulled you out of that place..."
    e "Because then none of this—"
    scene ch2ep2_838
    with Dissolve(0.1)
    pause
    scene ch2ep2_839
    with Dissolve(1.0)
    le "..."
    scene ch2ep2_840
    with dissolve
    le "You wish you never saved me?"
    scene ch2ep2_841
    with dissolve
    e "That's not what I—"
    le "That's what you said..."
    e "Leah, listen to me—"
    le "You said you wished you never saved me..."
    e "I meant that I wish I wasn't the one who—"
    scene ch2ep2_842
    with dissolve
    le "How come?"
    le "How come you wish that?"
    scene ch2ep2_843
    with Dissolve(1.0)
    pause
    e "... Because one day I won't be there anymore. And you'll be the one left behind."
    scene ch2ep2_844
    with Dissolve(1.0)
    pause
    scene ch2ep2_845
    with dissolve
    le "I already know people leave..."
    le "My mom left..."
    le "My friends didn't want me around just because I'm a little different..."
    le "But that's not why you're leaving... You're not leaving because you want to, right?"
    e "..."
    e "Why, Leah?"
    e "Why me?"
    scene ch2ep2_846
    with dissolve
    le "Because you feel like you're hurting too."
    scene ch2ep2_847
    with Dissolve(0.1)
    pause
    scene ch2ep2_846
    with dissolve
    le "It was the first time I felt like someone actually got it... actually got {i}me{/i}..."
    le "I just wanted that feeling to stay."
    play sound running
    scene ch2ep2_848
    with Dissolve(0.1)
    pause 0.5
    play sound closedoor2
    scene ch2ep2_849
    with Dissolve(0.1)
    pause
    play sound2 hospitalambience2 fadein 1 loop
    scene ch2ep2_850
    with Dissolve(0.2)
    ju "Leah?"
    scene ch2ep2_851
    with Dissolve(0.2)
    ju "Leah, wait!"
    scene ch2ep2_852
    with Dissolve(0.1)
    ju "You stay here."
    mc "Are you telling me to just—"
    ju "Yes. Let me do my job."
    stop sound2 fadeout 1
    scene ch2ep2_853
    with Dissolve(1.0)
    pause
    play sound cloth
    scene ch2ep2_854
    with Dissolve(1.0)
    pause
    play sound closedoor
    scene ch2ep2_855
    with dissolve
    mc "Em? What happened—"
    scene ch2ep2_856
    with Dissolve(1.0)
    pause
    play sound closedoor
    scene ch2ep2_857
    with dissolve
    pause
    scene ch2ep2_858
    with Dissolve(1.0)
    pause
    scene ch2ep2_642
    with flash
    le "If something is too big to say out loud, write it down first."
    le "Words find their way out whether you want them to or not, so it's better to give them somewhere to go."
    scene ep5_47
    with flash
    d "Listen, Emy... Someday, if you can't express what you want to say through words, write a letter just like this."
    d "You can say anything you want in a letter. Express your feelings, tell it your problems, anything you want. It's like your friend!"
    stop music fadeout 5
    scene ch2ep2_859
    with flash
    pause

    transform emma_reading_recede:
        subpixel True
        ease 3.0 matrixcolor BrightnessMatrix(-.2) * SaturationMatrix(.7) blur 10

    transform diary_page_flip_out:
        subpixel True
        align (.5, .5)
        xzoom 1.0
        rotate 0
        easein_quart .8 xzoom 0.05 rotate -5 alpha 0.0

    transform diary_page_flip_in:
        subpixel True
        align (.5, .5)
        xzoom 0.05
        rotate 5
        alpha 0.0
        easein_quart 1.0 xzoom 1.0 rotate 0 alpha 1.0

    play sound2 bookopen
    scene ch2ep2_860
    with Dissolve(0.8)
    scene ch2ep2_860 at emma_reading_recede
    with Dissolve(0.2)

    play sound papermovement2
    show ch2ep2_861 at diary_page_flip_in
    play music2 'audio/LeahsHeart_loop.mp3'
    pause
    play sound papermovement
    show ch2ep2_861 at diary_page_flip_out
    pause 0.7
    hide ch2ep2_861
    pause 0.1

    play sound papermovement2
    show ch2ep2_863 at diary_page_flip_in
    pause
    play sound papermovement
    show ch2ep2_863 at diary_page_flip_out
    pause 0.7
    hide ch2ep2_863
    pause 0.1

    play sound papermovement2
    show ch2ep2_864 at diary_page_flip_in
    pause
    play sound papermovement
    show ch2ep2_864 at diary_page_flip_out
    pause 0.7
    hide ch2ep2_864
    pause 0.1

    play sound papermovement2
    show ch2ep2_865 at diary_page_flip_in
    pause
    play sound papermovement
    show ch2ep2_865 at diary_page_flip_out
    pause 0.7
    hide ch2ep2_865
    pause 0.1

    play sound papermovement2
    show ch2ep2_866 at diary_page_flip_in
    pause
    play sound papermovement
    show ch2ep2_866 at diary_page_flip_out
    pause 0.7
    hide ch2ep2_866
    pause 0.1

    if emmaroute:
        play sound papermovement2
        show ch2ep2_868 at diary_page_flip_in
        pause
        play sound papermovement
        show ch2ep2_868 at diary_page_flip_out
        pause 0.7
        hide ch2ep2_868
        pause 0.1
    else:
        play sound papermovement2
        show ch2ep2_867 at diary_page_flip_in
        pause
        play sound papermovement
        show ch2ep2_867 at diary_page_flip_out
        pause 0.7
        hide ch2ep2_867
        pause 0.1

    play sound papermovement2
    show ch2ep2_869 at diary_page_flip_in
    pause
    play sound papermovement
    show ch2ep2_869 at diary_page_flip_out
    pause 0.7
    hide ch2ep2_869
    pause 0.1

    play sound papermovement2
    show ch2ep2_870 at diary_page_flip_in
    pause
    play sound papermovement
    show ch2ep2_870 at diary_page_flip_out
    pause 0.7
    hide ch2ep2_870
    pause 0.1

    play sound papermovement2
    show ch2ep2_871 at diary_page_flip_in
    pause
    play sound papermovement
    show ch2ep2_871 at diary_page_flip_out
    pause 0.7
    hide ch2ep2_871
    pause 0.1

    play sound papermovement2
    show ch2ep2_862 at diary_page_flip_in
    pause
    play sound papermovement
    show ch2ep2_862 at diary_page_flip_out
    pause 0.7
    hide ch2ep2_862
    pause 0.1

    scene ch2ep2_860
    with dissolve
    pause
    play sound bookclose
    scene ch2ep2_872
    with dissolve
    pause
    scene ch2ep2_873
    with dissolve
    pause
    play sound2 closedoor2
    scene ch2ep2_874
    with Dissolve(0.2)
    ju "Emma—"
    scene ch2ep2_875
    with dissolve
    pause
    scene ch2ep2_876
    with dissolve
    ju "*sighs*"
    e "... Am I the reason this got pushed?"
    ju "Partly."
    ju "It was already happening before I could get ahead of it. I saw it and waited too long. That's on me."
    ju "But you're a trained professional, Emma. You knew what this was, but you kept coming back anyway."
    e "..."
    scene ch2ep2_877
    with dissolve
    ju "I'm pulling you off Leah's case. Effective immediately."
    ju "I should've done it sooner."
    scene ch2ep2_878
    with dissolve
    e "... I should've left sooner."
    scene ch2ep2_879
    with dissolve
    ju "..."
    scene ch2ep2_880
    with dissolve
    pause
    scene ch2ep2_881
    with dissolve
    ju "This isn't your first trafficking case, right? So what's different?"
    e "... I don't know."
    ju "*exhales*"
    ju "Go home, Emma."
    scene ch2ep2_882
    with dissolve
    e "Can I talk to her one last time?"
    ju "No."
    ju "And even if I could sign off on it... she doesn't want to see you right now."
    scene ch2ep2_883
    with dissolve
    pause
    play sound bookopen
    play sound2 cloth
    scene ch2ep2_884
    with Dissolve(1.0)
    pause
    e "(I don't know if I'm saying this the right way...)"
    e "(I don't even know if there is a right way.)"
    e "(I just... I need you to understand what I meant.)"
    e "(When I said I wished I never saved you...)"
    e "(I saw your face when I said that, and I...)"
    e "(That's not what I meant.)"
    e "(I don't wish you were still there.)"
    e "(I don't wish any of that ever happened to you.)"
    e "(I just...)"
    scene ch2ep2_885
    with Dissolve(2.0)
    e "(I wish it wasn't me.)"
    e "(I wish it had been someone else who got you out of that place.)"
    e "(Someone who could've done it cleanly without everything I come with.)"
    e "(Because if it was someone else...)"
    e "(I could've stayed.)"
    e "(Not as someone with a file on you, and as someone who has to pretend there are lines she won't cross.)"
    e "(But as someone who gets to sit next to you.)"
    e "(Someone who gets to be there when you're scared.)"
    e "(Someone who doesn't have to leave when the time calls for it.)"
    e "(That's all I wanted.)"
    e "(And I ruined it before I even understood why.)"
    e "(I'm sorry, Leah.)"
    e "(Also, you chose a very good name.)"
    e "(Don't let anyone tell you otherwise.)"
    scene ch2ep2_886
    with Dissolve(1.0)
    e "(Love,)" with Dissolve(1.0)
    e "(Emma)" with Dissolve(1.0)
    scene ch2ep2_887
    with dissolve
    pause
    le "*whispers* Goodbye, Emma..." with Dissolve(2.0)

    scene black
    with dissolve
    with fade

    play sound keyboardtype_fast fadein 1 loop
    scene ch2ep2_888
    with dissolve
    pause
    stop sound
    scene ch2ep2_889
    with dissolve
    pause
    scene ch2ep2_890
    with dissolve
    pause
    scene ch2ep2_891
    with dissolve
    pause
    play sound cloth
    scene ch2ep2_892
    with dissolve
    pause
    scene ch2ep2_893
    with dissolve
    pause
    scene ch2ep2_894
    with dissolve
    g "Everything okay?"
    e "Just a little tired..."
    g "Take all the time you need."
    e "... I'd rather not. You smell like alcohol."
    g "*scoffs* Says the woman who smells like coffee."
    e "She said that..."
    g "... I see."
    g "You'll be okay, Em."
    scene ch2ep2_895
    with dissolve
    pause
    stop music2 fadeout 2

    scene black
    with dissolve
    with fade

    play sound keyboardtype loop fadein 2
    scene ch2ep2_896
    with dissolve
    pause
    play sound2 closedoor2
    scene ch2ep2_897
    with dissolve
    mar "Boss."
    mc "Mark."
    scene ch2ep2_898
    with dissolve
    mar "Food drive went well. Turnout was better than last month."
    mc "Yeah, I saw the numbers. That's why I'm doing the report now."
    mar "Could've waited until tomorrow."
    mc "Nah... It's not that long. I'd rather get it out of my head tonight."
    mar "Fair enough."
    scene ch2ep2_899
    with dissolve
    mar "The kids were asking about you, by the way. Told them you were tied up."
    mc "How'd they take it?"
    mar "The usual. Woozie tried to guilt trip me about it for a solid ten minutes."
    mc "*chuckles* Yeah, that tracks."
    mar "He's getting good at it, too. Honestly kind of scary."
    mar "Oh, and Maple asked Aine to marry him again. Kid never learns."
    mc "*laughs* What'd she say this time?"
    mar "Decided to put him out of his misery. Showed him the engagement ring. He cried for the rest of the day."
    mc "I'll make it up to them next time."
    mar "Holding you to that."
    scene ch2ep2_900
    with dissolve
    mar "..."
    mar "You sleeping at all lately?"
    mc "Some. Better than last week."
    mar "Good. You were looking rough for a while there."
    mc "Yeah, well..."
    mar "Need anything else from me tonight?"
    mc "No. You can go home, Mark."
    mar "Alright. Have a good one, boss."
    mc "*nods*"
    play sound2 closedoor2
    scene ch2ep2_901
    with dissolve
    pause
    scene ch2ep2_902
    with dissolve
    mc "You know, I would understand Moon..."
    play sound woosh
    scene ch2ep2_903
    play music 'audio/WrongDoorRightDisaster.mp3'
    mc "But what are you two doing here?"
    scene ch2ep2_904
    with dissolve
    f "Streaming."
    mc "Here?"
    f "Better lighting."
    mc "You're not streaming."
    scene ch2ep2_905
    with dissolve
    f "..."
    scene ch2ep2_906
    with dissolve
    f "Better lighting."
    play sound woosh
    scene ch2ep2_907
    s "Go left! LEFT! Why do you keep going right?!"
    f "Because I want to go right, Sky! I'm a professional gamer, stop backseating me!"
    s "There's nothing on the right! I've been telling you for twenty minutes—"
    f "And I've been ignoring you for twenty minutes! You'd think you'd take the hint!"
    s "Just give me that—"
    play sound fistbump
    scene ch2ep2_908
    f "Touch it and you lose a hand."
    scene ch2ep2_909
    with dissolve
    s "*groans*"
    mc "..."
    scene ch2ep2_910
    with dissolve
    mc "Sky, didn't you say your class has a field trip tomorrow?"
    s "Hm? That was last month."
    mc "... I've had it on my calendar for two weeks."
    s "... Did you write down the wrong date?"
    mc "..."
    f "*snorts*"
    scene ch2ep2_911
    with Dissolve(0.2)
    s "Oh my god, you did."
    mc "..."
    scene ch2ep2_912
    with Dissolve(0.1)
    f "WAHAHAHAHA!"
    s "Oh my god..."
    mc "Go back to your game."
    f "He thought— WAHAHA—"
    scene ch2ep2_913
    with dissolve
    mc "Freya."
    f "Sorry, sorry... *snickers*"
    s "Are you okay? Do you need to sit down?"
    mc "I am sitting down. Go away."
    s "The field trip was November fourteenth, [mc]... It's December."
    mc "Both of you. Out."
    f "Okay, okay..."
    s "You want me to start sending you reminders, or—"
    mc "Goodnight, Sky."
    s "Goodnight."
    stop music fadeout 2
    scene ch2ep2_914
    with Dissolve(1.0)
    f "Come on, let's get dinner."
    s "..."
    scene ch2ep2_915
    with dissolve
    f "Sky."
    s "Yeah... Coming."
    play sound closedoor2
    scene ch2ep2_916
    with dissolve
    m "..."
    scene ch2ep2_917
    with dissolve
    m "The letter's been on the fridge since October."
    mc "Moon."
    m "Hm?"
    mc "Not a word."
    m "I didn't say anything."
    call hide_days
    with dissolve

    scene black
    with dissolve
    with fade

    $ phone_time_add(hours=21)
    show screen day_sunday with dissolve
    play sound restaurantambience loop
    scene ch2ep2_974
    with dissolve
    pause
    scene ch2ep2_975
    with dissolve
    pause
    play sound2 papermovement2
    scene ch2ep2_976
    with dissolve
    pause
    play sound2 doorchime2
    play sound3 closedoor2
    scene ch2ep2_977
    with dissolve
    pause
    play sound4 bookclose
    play sound5 papermovement2
    scene ch2ep2_978
    with dissolve
    un "Temporary placement. Seems like that didn't pan out your way."
    play music 'audio/SolvingAMystery.mp3' fadein 3
    play sound2 chair
    scene ch2ep2_979
    with dissolve
    fr "You look tired."
    mc "Francis."
    fr "Glad you didn't run."
    mc "I don't. Never had the tail and legs for it like you did."
    scene ch2ep2_980
    with dissolve
    pause
    scene ch2ep2_981
    with dissolve
    fr "There's a man outside. Blue sedan, second from the corner."
    fr "If I don't walk out of here in the next five minutes, he makes a call."
    fr "Not to the police."
    scene ch2ep2_982
    with dissolve
    pause
    scene ch2ep2_983
    with dissolve
    mc "Nobody asked."
    fr "A year later and you're still just as annoying."
    scene ch2ep2_984
    with dissolve
    fr "I'm not saying it as a threat."
    fr "I'm saying it so you know exactly why you're going to sit there and hear me out."
    scene ch2ep2_985
    with dissolve
    pause
    play sound2 cloth
    scene ch2ep2_986
    with dissolve
    mc "Sure. Just try not to breathe too hard. I can smell the money from here."
    scene ch2ep2_987
    with dissolve
    pause
    scene ch2ep2_988
    with dissolve
    fr "You followed the rules."
    mc "..."
    fr "Submitted the request. Went through the proper channels."
    fr "And yet... there it is."
    fr "The rules told you no."
    mc "The rules exist for a reason."
    fr "They exist to protect the system, not the child."
    mc "That's not—"
    fr "You filled out forms, [mc]."
    fr "While she was sitting in a hospital room waiting for someone to decide what happens to her next."
    fr "You filled out forms."
    mc "..."
    scene ch2ep2_989
    with dissolve
    fr "I don't fill out forms."
    mc "Of course not. Paperwork's beneath you. You've got children to collect."
    fr "I find them. I take them somewhere safe."
    fr "I don't wait for a system to tell me whether I'm allowed to care."
    mc "Keep telling yourself that, Francis."
    fr "I intend to."
    if aoifelives:
        scene ch2ep2_990
        with dissolve
        pause
    else:
        scene ch2ep2_991
        with dissolve
        pause
    fr "I heard about Club Ashen."
    fr "... She cried when I first brought her in, you know."
    fr "She gets overwhelmed by kindness. Most of them do, at first."
    play sound2 papermovement
    scene ch2ep2_992
    with dissolve
    pause
    scene ch2ep2_993
    with dissolve
    fr "She is not yours."
    mc "Nor is she yours."
    fr "That's where you're wrong."
    fr "I spent four months with her."
    fr "Four months of her learning to trust a place. Learning to trust a voice."
    fr "You had her for a few days."
    mc "A few days were enough to see what four months looked like on her."
    scene ch2ep2_994
    with dissolve
    fr "She reminds me of my sister."
    scene ch2ep2_995
    with dissolve
    pause
    fr "She used to follow me everywhere. Wanted to do everything I did."
    fr "I told her to wait inside once. I told her I'd be right back."
    scene ch2ep2_996
    with dissolve
    wait "Can I get you anything?"
    fr "Coffee. Black, please."
    wait "Sure thing."
    scene ch2ep2_997
    with dissolve
    wait "Refill for you, hon?"
    mc "I'm good."
    wait "Be right back."
    scene ch2ep2_998
    with dissolve
    pause
    scene ch2ep2_999
    with dissolve
    mc "What do you really want?"
    fr "..."
    fr "I want you to understand something."
    mc "You went above and beyond to find me just to tell me \"something\"?"
    fr "I'm not hurting them."
    mc "A ten-year-old girl, basement, candy jar. Yeah, real homey setup you had going."
    scene ch2ep2_1000
    with dissolve
    fr "I gave her somewhere safe and quiet. I took care of her."
    mc "Right. Because nothing says \"taken care of\" like a cheap mattress in an isolated room."
    fr "Until I could find what was missing."
    scene ch2ep2_1001
    with dissolve
    yt "He's different."
    yt "Not the same guy who stood over me and made speeches like he was reading from a script."
    yt "That Francis wanted a reaction. This one doesn't. What the hell happened to him?"
    play sound2 mugdown
    scene ch2ep2_1002
    with dissolve
    wait "Here you go."
    fr "Thank you."
    scene ch2ep2_1003
    with dissolve
    mc "Those children are not a missing piece, Francis. Leah's just a kid."
    fr "I know what she is. I also know what she carries, whether she knows it or not."
    mc "Yeah? She carries what happens when the person who was supposed to protect her puts a price tag on her instead."
    mc "That's her whole load right there. Nothing else."
    scene ch2ep2_1004
    with dissolve
    fr "..."
    scene ch2ep2_1005
    with dissolve
    fr "Father used to tell me that there's more to this world than what it lets on."
    fr "That some people are born carrying things they didn't choose."
    fr "Old debts, names, even memories. He said most of them never even figure it out."
    fr "You strike me as one of those people."
    play sound2 mugdown
    scene ch2ep2_1006
    with dissolve
    pause
    play sound3 cloth
    scene ch2ep2_1007
    with dissolve
    fr "You know what the difference is between you and me?"
    mc "..."
    fr "When the rules said no..."
    fr "You stopped."
    scene ch2ep2_1008
    with dissolve
    pause
    play sound2 doorchime2
    play sound3 closedoor2
    scene ch2ep2_1009
    with dissolve
    pause
    scene ch2ep2_1010
    with dissolve
    mc "*scoffs*"
    if aoifelives:
        stop music fadeout 4
        play music2 'audio/TheMeaningThatComesWithYou.mp3' fadein 4 
        scene ch2ep2_1011
        with dissolve
        mc "Didn't know you could hide your serum signature like that. You really are dangerous, like Moon said."
        ao "..."
        scene ch2ep2_1012
        with dissolve
        mc "You work here?"
        ao "Part-time..."
        mc "Right. Part-time."
        scene ch2ep2_1013
        with dissolve
        ao "Relax... Jess asked me to keep an eye out on this side of the city... You just happen to be in it..."
        play sound2 cloth
        scene ch2ep2_1014
        with dissolve
        mc "Hm, convenient."
        ao "Very..."
        ao "I'm telling you... I actually do work here... You can keep your guard down..."
        scene ch2ep2_1015
        with dissolve
        mc "How much of that did you hear?"
        ao "Just enough to know he walked out on his own legs... That was generous..."
        mc "He had men outside. Can't really risk the customers here."
        scene ch2ep2_1016
        with dissolve
        ao "..."
        ao "So you filed through DFCS... got rejected... and now you're sitting here with a cold coffee and a crease in your forehead..."
        mc "That... about covers it, yeah."
        ao "I take it you're here because you want to file an appeal...?"
        mc "After that one? \"Wanted\"."
        scene ch2ep2_1017
        with dissolve
        ao "You know... we don't go through those channels..."
        mc "I don't really want to tell a kid that I got her through questionable means."
        mc "In that case, I'd be no different from Francis."
        ao "You know what they say back in the military...? Clean is a nice word for slow..."
        scene ch2ep2_1018
        with dissolve
        mc "... Like the way you talk?"
        ao "..."
        scene ch2ep2_1019
        with dissolve
        ao "Not my intention to tell you what to do... Sorry..."
        mc "Nah... You're good. Just yanking your chain."
        mc "Besides, I already know who I'm calling."
        scene ch2ep2_1020
        with dissolve
        ao "Then drink your coffee... I brewed it for you... It's been cold for ten minutes..."
        mc "I take you're here just to tell me to drink my coffee? You hate it when people reject your food, huh?"
        scene ch2ep2_1021
        with dissolve
        ao "Try me..."
        mc "*scoffs* I'll take that as a yes."
        play sound2 cloth
        scene ch2ep2_1022
        with dissolve
        ao "Anyway... good luck..."
        scene ch2ep2_1023
        with dissolve
        mc "What you said about the whiskey. Does that still stand?"
        scene ch2ep2_1024
        with dissolve
        ao "Once you figure it out... anytime..."
        scene ch2ep2_1025
        with dissolve
        pause
        stop music2 fadeout 4
        play music 'audio/SolvingAMystery.mp3' fadein 4
        play sound2 dialtone loop
        scene ch2ep2_1026
        with dissolve
        pause
        play sound2 phoneclick
        scene ch2ep2_1027
        with dissolve
        j "[mc]."
        mc "I need Eliza again."
        j "What's going on?"
        mc "Our unfinished business."
        j "Ours... or yours?"
        mc "Francis."
        j "..."
        j "I'll get her down. Come when you're ready."
    else:
        play sound2 dialtone loop
        scene ch2ep2_1026
        with dissolve
        pause
        play sound2 phoneclick
        scene ch2ep2_1027
        with dissolve
        j "[mc]."
        mc "I need Eliza again."
        j "What's going on?"
        mc "Our unfinished business."
        j "Ours... or yours?"
        mc "Francis."
        j "..."
        j "I'll get her down. Come when you're ready."
    stop sound fadeout 2

    scene black
    with dissolve
    with fade

    play sound elevatorclose
    scene ch2ep2_1028
    with dissolve
    pause
    scene ch2ep2_1029
    with Dissolve(0.2)
    el "[mc]."
    scene ch2ep2_1030
    with Dissolve(0.2)
    el "Here."
    scene ch2ep2_1031
    with dissolve
    el "A message from Jess."
    mc "What'd she say?"
    el "\"Don't go thinking there's always an easy way through.\""
    scene ch2ep2_1032
    with dissolve
    mc "..."
    mc "Believe me. I tried to do it the right way this time."
    mc "Besides... I've always been the side character. Always have been."
    el "Glad to hear that. Good enough for me."
    mc "The President going to have a problem with this?"
    el "He'll ask questions. But Francis has been on our radar long before yours. This was always ours to close."
    play sound closedoor2
    scene ch2ep2_1033
    with dissolve
    pause
    play sound2 cloth
    scene ch2ep2_1034
    with dissolve
    e "You've been cooperative so far."
    tim "Don't see a reason in not being at this point."
    e "Smart."
    scene ch2ep2_1035
    with Dissolve(0.2)
    tim "... The kid. She okay?"
    e "Why do you ask?"
    tim "I just wanna know. I was the one feeding her. Making sure she had what she needed."
    tim "Wasn't much, but... I made sure she ate."
    e "..."
    tim "She used to save half her food."
    e "What for?"
    tim "Don't know. She just always did. Maybe she just doesn't like the food."
    e "..."
    tim "She okay or not?"
    e "She's safe."
    tim "Detective... I need to know. Please."
    scene ch2ep2_1036
    with dissolve
    e "..."
    scene ch2ep2_1037
    with dissolve
    e "She's okay."
    tim "*exhales* Good. Good..."
    scene ch2ep2_1038
    with dissolve
    tim "... She's a smart kid. Weird, but smart."
    e "Weird how?"
    tim "The way she talked. It's like she was always thinking three things at once."
    tim "Asked me once why I was doing this job."
    e "What did you tell her?"
    scene ch2ep2_1039
    with dissolve
    tim "The truth. Money."
    tim "She thought about it for a second and said, \"that makes sense, I guess.\""
    tim "*soft laugh* Ten years old. Just... \"that makes sense.\""
    scene ch2ep2_1040
    with dissolve
    e "..."
    play sound closedoor2
    scene ch2ep2_1041
    with dissolve
    pause
    play sound2 keyboardpress
    scene ch2ep2_1042
    with Dissolve(0.1)
    pause
    play sound3 poweron
    scene ch2ep2_1043
    play music 'audio/StringsOfImmersion1.mp3'
    pause
    play sound chair2
    scene ch2ep2_1044
    with dissolve
    el "Okay. Talk to me."
    mc "Hospital database. HC General."
    play sound keyboardtype loop
    el "Patient records?"
    mc "All of it. Access logs, file movement, copy requests."
    el "Copy requests specifically?"
    mc "Someone inside that hospital is feeding information out. I need to know who."
    el "You got a name? Ward? Department?"
    mc "Pediatric recovery. Let's go with last two weeks."
    el "Patient?"
    mc "Leah Warren. Trafficking case, protective custody."
    play sound2 computer_prompt
    scene ch2ep2_1045
    with Dissolve(0.2)
    el "..."
    el "Sensitive file. That's going to have extra encryption layers on top of the standard hospital network."
    el "HC General runs Medicore V4 on their backend. Government-adjacent, not government-grade."
    mc "Meaning?"
    el "Meaning I can get in. Just won't be in the next thirty seconds."
    mc "How long?"
    el "Depends on whether they patched their north node since we last had reason to look at them."
    el "If they didn't, five to ten minutes. If they did, longer."
    mc "Get started."
    play sound knuckle_crack
    scene ch2ep2_1046
    with Dissolve(0.1)
    pause
    play sound keyboardtype_fast2 loop
    scene ch2ep2_1047
    with Dissolve(0.2)
    el "Going in through the auxiliary network first. Less traffic, easier to bury the entry point."
    el "Once I'm past the outer firewall I can pull the access logs directly."
    el "You're looking for anomalous access patterns. Someone pulling a file they have no clinical reason to pull."
    mc "And copying it."
    el "Copying is a different flag entirely."
    el "If someone copied that file, there'll be a shadow log. Hospitals keep those for liability."
    el "Most people don't know that."
    mc "Does Francis?"
    el "Doesn't matter if he does. His possible contact inside won't. People get sloppy when they think they're invisible."
    scene ch2ep2_1048
    with Dissolve(0.2)
    el "I'm past the outer layer. Routing through a blind relay so the trace dies at the node."
    el "Give me a few minutes on the inner partition."
    mc "..."
    scene ch2ep2_1049
    with dissolve
    pause
    stop sound fadeout 1
    scene ch2ep2_1050
    with dissolve
    e "Francis Mentzelopoutous."
    tim "That's right."
    e "How long have you worked for him?"
    tim "Eight months. Almost nine."
    e "How did you get recruited?"
    tim "Same way everyone does. Someone knows someone. Money's good. You don't ask questions."
    e "Did you know what the operation was before you signed on?"
    tim "... I had a pretty good idea."
    e "And you still took the job."
    scene ch2ep2_1051
    with dissolve
    tim "Do you have kids, Detective?"
    e "... No."
    tim "Well, I've got two and a landlord who doesn't give a shit about either of them."
    tim "So yeah. I took the job."
    e "..."
    scene ch2ep2_1052
    with dissolve
    e "What can you tell me about him?"
    tim "What do you want to know?"
    e "Everything."
    scene ch2ep2_1053
    with dissolve
    tim "..."
    tim "He's... not right."
    e "Elaborate."
    scene ch2ep2_1054
    with Dissolve(0.2)
    tim "In the head. He's not right in the head."
    scene ch2ep2_1055
    with dissolve
    tim "You see, most guys running an operation like this, they're businessmen. Cold, yeah, but businessmen."
    tim "Francis isn't running a business. It's something personal."
    tim "He doesn't care about the money. Barely touches it."
    tim "The whole thing—the network, the locations, all of it—it's just infrastructure for whatever he's actually after."
    e "Which is?"
    tim "Looking for someone."
    e "Who?"
    scene ch2ep2_1056
    with dissolve
    tim "His sister."
    e "..."
    tim "She's dead. Has been for a long time, from what I gathered."
    tim "Fire. He was a kid. Got out. She didn't."
    tim "He never got over it."
    e "And the children? What's he really after?"
    tim "He's trying to put her back together."
    scene ch2ep2_1057
    with dissolve
    e "..."
    tim "That's the best way I can describe it."
    tim "Every kid that came through, he'd sit with them. Talk to them. Real quiet, real patient."
    tim "Looking for something specific. The way she moved. Something she said. The way she laughed. Like he was collecting pieces."
    e "Pieces?"
    tim "One had the right voice. One had the right eyes. One remembered something she shouldn't have."
    tim "None of them were ever... enough."
    tim "And when they weren't..."
    e "He lost interest."
    tim "Yeah."
    scene ch2ep2_1058
    with dissolve
    e "And then what happened to them?"
    tim "..."
    tim "Moved on. That's all I know."
    e "Moved on where?"
    tim "I didn't ask. You learn real fast not to ask."
    e "..."
    e "The sister. Did she actually exist?"
    scene ch2ep2_1059
    with dissolve
    tim "..."
    play sound keyboardtype_fast2 loop fadein 1
    scene ch2ep2_1060
    with dissolve
    el "I'm in the access logs."
    el "Pulling pediatric recovery. Last fourteen days."
    play sound2 computer_prompt
    el "..."
    el "Okay. I've got twenty-three unique access events on the file you're looking for."
    el "Seventeen are clinical. Doctors, nurses, attending staff. All timestamped within standard shift hours."
    el "The other six..."
    mc "What about them?"
    el "Off-hours. Three between midnight and 4 AM. Two during shift change—lowest surveillance window in any hospital."
    el "One this morning. About two hours ago."
    mc "..."
    stop sound
    play sound2 computer_prompt
    scene ch2ep2_1061
    with Dissolve(0.2)
    el "And there's your copy flag."
    el "Someone used a local terminal on the pediatric floor to export the file. Not to an external drive, but to an encrypted relay address."
    el "Whoever set this up knew what they were doing."
    el "But they used the same terminal every time."
    mc "Can you get a name from the terminal ID?"
    el "Already running it."
    play sound2 computer_prompt
    scene ch2ep2_1062
    with Dissolve(0.1)
    el "..."
    el "Staff login tied to that terminal."
    play sound2 computer_prompt
    scene ch2ep2_1063
    with Dissolve(0.1)
    el "..."
    el "Cara Voss. Registered nurse. Pediatric recovery."
    mc "She's been in the room with Leah since the first night."
    el "You want me to pull her full profile?"
    mc "Everything you can get."
    el "Give me a minute."
    scene ch2ep2_1064
    with dissolve
    tim "I don't know."
    tim "Eight months working for this man and I've never seen a photo. Never heard a last name. Never heard anyone else mention her."
    tim "Just him. Talking to himself about her like she's standing right there."
    tim "I think..."
    scene ch2ep2_1065
    with dissolve
    tim "I think she might just be something he built in his head to survive whatever happened to him."
    tim "But good luck telling him that."
    e "..."
    scene ch2ep2_1066
    with dissolve
    tim "The creepy part isn't that he's looking for her. The creepy part is he genuinely believes he's close."
    tim "Every single time. Always thinks he's close."
    e "And Leah?"
    tim "Closest he's ever gotten, far as I could tell."
    e "..."
    e "He spent more time with her than the others?"
    tim "Yeah."
    e "Why?"
    scene ch2ep2_1067
    with dissolve
    tim "Don't know. But he was different with her."
    tim "He was calmer. Like he thought she was it—or whatever it is that's going on in that head of his."
    tim "But the thing is... he's never really talked to her in person. Always just talked or watched her in front of a camera."
    tim "Like getting up close and personal would taint her or something. Really weird."
    e "..."
    e "The men who stayed. Why?"
    scene ch2ep2_1068
    with dissolve
    tim "Same reason I did. He pays well and on time."
    tim "Nobody's really loyal to him. He just keeps the money flowing and people keep showing up."
    tim "Pull the money out and the whole thing falls apart overnight."
    tim "But him? He'd keep going with nothing. I genuinely believe that."
    e "..."
    play sound bookclose
    scene ch2ep2_1069
    pause
    scene ch2ep2_1070
    with dissolve
    e "Where is he?"
    tim "... You're going to find him anyway."
    e "Faster with your help."
    tim "..."
    tim "Funny thing is, he's close to Ashen. Near the train station. He's got an office there."
    tim "31 Veyne Plaza, East End, Golden City."
    tim "He moves around but he keeps coming back. It's where he feels safe, I think."
    e "How many men?"
    tim "Skeleton crew by now. After Ashen, most of them probably scattered."
    tim "Maybe seven. Maybe less."
    play sound cloth
    scene ch2ep2_1071
    with dissolve
    e "Thank you."
    scene ch2ep2_1072
    with Dissolve(0.1)
    tim "Detective."
    e "Yeah?"
    tim "Thank you for getting her out of there."
    e "..."
    e "She saved herself. We just opened the door."
    play sound closedoor2
    scene ch2ep2_1073
    with dissolve
    pause
    scene ch2ep2_1074
    with dissolve
    pause
    scene ch2ep2_1075
    with dissolve
    pause
    play sound2 computer_prompt
    scene ch2ep2_1076
    with Dissolve(0.1)
    el "Okay. Cara Voss. Licensed RN, seven years. She's got a clean record, no flags."
    el "Hired at HC General fourteen months ago."
    el "Previous employer—private medical contractor. Dissolution Medical Services."
    el "Which is interesting, because Dissolution Medical Services doesn't exist anymore."
    el "Dissolved—right there in the name—eighteen months ago."
    el "But here's the thing... The registered address for Dissolution Medical Services?"
    scene ch2ep2_1077
    with dissolve
    el "Few miles from Club Ashen."
    mc "..."
    mc "He planted her before Leah even got there."
    el "Looks that way."
    el "I'd say she wasn't placed for Leah specifically. She was already there. Waiting for whoever came through."
    mc "..."
    el "You want us to act on this? Just say the word. I'll roll everyone in."
    mc "Give me a minute."
    play sound cloth
    scene ch2ep2_1078
    with dissolve
    pause
    play sound2 dialtone loop
    scene ch2ep2_1079
    with dissolve
    pause
    stop sound2 fadeout 1
    play sound3 phonevibrate loop fadein 1
    scene ch2ep2_1080
    with dissolve
    pause
    scene ch2ep2_1081
    with dissolve
    pause
    play sound3 phoneclick
    scene ch2ep2_1082
    with dissolve
    e "[mc]."
    mc "Where are you?"
    e "At the precinct. Just wrapped up an interrogation. I've got Francis's location—"
    scene ch2ep2_1083
    with Dissolve(0.2)
    mc "Em. Hold on."
    e "What?"
    scene ch2ep2_1084
    with dissolve
    mc "The nurse. Cara Voss."
    mc "She's Francis's contact. Has been since before Leah even got there."
    mc "She's been copying Leah's file. Placement details. Visitor logs. Everything."
    scene ch2ep2_1085
    with dissolve
    e "..."
    e "Where are you right now?"
    mc "Sicae HQ."
    e "[mc], I told you—"
    mc "Let me explain—Francis found me earlier. We talked, but he rambled {b}{i}too much{/i}{/b}."
    e "He what?"
    mc "He had men outside. It wasn't a conversation I chose. I didn't have a clean option, Em. This was the fastest way to confirm what he already knew."
    e "..."
    e "The foster family... They're moving Leah right now."
    mc "Yeah, but let us—"
    e "He knows where they're taking her."
    mc "..."
    mc "Em, I know what you're thinking—"
    scene ch2ep2_1086
    with Dissolve(0.2)
    e "Francis is a few miles east of Ashen. Office near the train station. 31 Veyne Plaza, East End, Golden City."
    e "File that report along with the information you got. Make sure the evidence is airtight. Do it now."
    mc "To who?"
    scene ch2ep2_1087
    with Dissolve(0.2)
    e "Hale. Go straight to Hale. He won't sit on it if Sicae's backing it."
    mc "Emma—"
    e "[mc]. Please."
    scene ch2ep2_1088
    with dissolve
    mc "..."
    e "File it. I'll buy you time."
    scene ch2ep2_1089
    with dissolve
    mc "Em, if you go there now—"
    e "I know what it'll cost..."
    mc "Let us handle this."
    e "You already are..."
    scene ch2ep2_1090
    with dissolve
    el "So?"
    mc "Yeah. Do it."
    stop music fadeout 2

    scene black
    with dissolve
    with fade

    play sound hospitalambience2 loop
    scene ch2ep2_1091
    with dissolve
    pause
    play sound2 shoesqueak_double
    scene ch2ep2_1092
    with Dissolve(0.1)
    pause
    scene ch2ep2_1093
    with Dissolve(0.1)
    ju "Emma—"
    play sound2 cloth
    scene ch2ep2_1094
    with Dissolve(0.1)
    pause
    stop sound fadeout 10
    play music 'audio/EmmasVow.mp3'
    scene ch2ep2_1095
    with dissolve
    ju "What are you doing?"
    e "Buying time."
    ju "You were removed from this case, Emma."
    e "Yeah. I know."
    scene ch2ep2_1096
    with dissolve
    le "Emma."
    e "Hm?"
    le "I read your letter."
    scene ch2ep2_1097
    with dissolve
    e "..."
    scene ch2ep2_1098
    with dissolve
    ju "Emma. Step aside. Right now."
    e "There's a report being filed with Hale as we speak."
    ju "That doesn't give you the authority to—"
    scene ch2ep2_1099
    with Dissolve(0.2)
    e "Cara Voss."
    ju "..."
    e "She's Francis's contact. She's been copying Leah's file."
    e "Visitor logs. Transfer schedule... and the placement details. He knows where you're taking her, June."
    scene ch2ep2_1098
    with Dissolve(0.2)
    lo "What? June, is this—"
    ju "Lois. Give me a moment, please."
    scene ch2ep2_1099
    with dissolve
    ju "Where is this coming from?"
    e "[mc]. He's the one filing the report with Hale."
    ju "Then let the report do its job. Step aside and give me ten minutes. I'll make the call myself."
    e "She doesn't have ten minutes. You can't guarantee she will, since we don't know what Francis might do. But I will make sure to give her that time."
    ju "I am trying to work with you here. But I can't halt a federal transfer on the word of an officer who was pulled from this case for emotional compromise."
    ju "That is exactly the reason you were removed. You know why I can't act on this. Not from you."
    e "I know."
    scene ch2ep2_1100
    with dissolve
    ju "Emma. I'm going to make the call. But you need to step aside while I do."
    e "You can make the call, but I am not stepping aside until Hale confirms the report."
    ju "Emma... please. I am trying to protect you. Why do you have to do this?"
    scene ch2ep2_1101
    with dissolve
    e "... Because I'm not about to make the same mistake I did before."
    e "I have a friend. She would've walked into that club herself."
    e "No badge. No backup. Not even a sliver of hesitation."
    e "Because that's just who she is."
    e "She's stronger than me. Faster. Better equipped for all of it."
    e "And I used to tell myself that was fine."
    e "That there were people better suited. That I'd done what I could."
    scene ch2ep2_1102
    with dissolve
    e "I told myself that when [mc] got taken."
    e "I knew something was wrong and convinced myself it wasn't my place."
    e "That the right people were handling it."
    e "He got out. Everything was fine. But I should've been there."
    scene ch2ep2_1103
    with dissolve
    e "It should've been me."
    ju "Emma..."
    e "I'm not like her, June."
    e "I can't move faster than a bullet or take a hit that would put anyone else in the ground."
    e "All I have is this job."
    e "And if I can't use it to protect one child..."
    e "Then what am I even doing here?"
    e "What was any of it for?"
    ju "..."
    ju "Look, I get you. But that still doesn't mean you have to risk your—"
    scene ch2ep2_1104
    with dissolve
    e "I fell in love with her, June." with Dissolve(2.0)
    scene ch2ep2_1105
    with dissolve
    mc "..."
    el "You should tell her she left the call on."
    scene ch2ep2_1104
    with dissolve
    e "I didn't plan it. I didn't even see it coming. But by the time I did... I didn't want to stop it."
    e "You asked me what's different with Leah. That's your answer. That's why I'm standing here."
    scene ch2ep2_1106
    with dissolve
    pause
    scene ch2ep2_1107
    with dissolve
    ph "June... if what she's saying is true, we can't risk the transfer now."
    ju "I know, Phillip. I know."
    scene ch2ep2_1108
    with dissolve
    e "By the time it clears the right desks, she could already be back in his hands."
    e "I'm not taking that chance. Not with Leah."
    stop music fadeout 5
    play sound hospitalambience2 loop fadein 3
    play sound2 phonevibrate loop
    scene ch2ep2_1109
    with dissolve
    pause
    scene ch2ep2_1110
    with dissolve
    pause
    scene ch2ep2_1111
    with dissolve
    pause
    play sound2 phoneclick
    scene ch2ep2_1112
    with dissolve
    "........"
    ju "Yeah. She's here."
    scene ch2ep2_1113
    with dissolve
    ".............."
    ju "You're certain, sir?"
    "..."
    ju "Okay."
    play sound2 phoneclick
    play sound3 elevatorclose
    scene ch2ep2_1114
    with dissolve
    pause
    scene ch2ep2_1115
    with dissolve
    pause
    scene ch2ep2_1116
    with dissolve
    pause
    scene ch2ep2_1117
    with dissolve
    y "Cara Voss."
    cara "... Yes?"
    y "Sicae. You're coming with us."
    play sound2 cloth2
    scene ch2ep2_1118
    with Dissolve(0.1)
    cara "I— what? Why?"
    li "Oh, please... don't make things harder for yourself."
    scene ch2ep2_1119
    with dissolve
    cara "What— I don't— what is this?! I haven't done anything!"
    y "*sighs* Why do they always lead with that...?"
    li "Beats me."
    cara "I want a lawyer!"
    li "That's not really how we work, hon."
    scene ch2ep2_1120
    with dissolve
    drp "What's— Cara?"
    cara "Dr. Park, help me! I don't know what's happening!"
    drp "What did she do?!"
    y "Above your pay grade, Doctor."
    scene ch2ep2_1121
    with dissolve
    li "Have a good one."
    cara "Wait— where are you taking me?!"
    scene ch2ep2_1122
    with dissolve
    pause
    scene ch2ep2_1123
    with dissolve
    pause
    scene ch2ep2_1124
    with dissolve
    ju "I'm sorry for the disruption."
    ju "Phillip. Lois. Please wait for me in the lobby."
    scene ch2ep2_1125
    with dissolve
    ph "*nods*"
    scene ch2ep2_1126
    with dissolve
    e "Whatever you're going to say... don't pity me. I chose this."
    scene ch2ep2_1127
    with dissolve
    ju "Hale forced me to file a report. About the placement... and what you did. You know this goes on record."
    e "... I already know that, June."
    ju "... And you'd do it again."
    scene ch2ep2_1128
    with dissolve
    e "Yeah..."
    scene ch2ep2_1129
    with dissolve
    pause
    scene ch2ep2_1130
    with dissolve
    ju "Stay away from her, Emma. Until this is sorted. Stay away."
    e "..."
    ju "I mean it."
    play music 'audio/EmmasVow.mp3' fadein 2
    scene ch2ep2_1131
    with dissolve
    e "Leah... I need you to go with Aunt June for now."
    le "Are you in trouble?"
    e "*softly nods*"
    le "Because of me?"
    play sound2 cloth
    scene ch2ep2_1132
    with Dissolve(1.0)
    e "Because of {i}me{/i}."
    scene ch2ep2_1133
    with Dissolve(1.0)
    le "... I'm sorry." with Dissolve(1.0)
    e "No, no... Don't be. It's my fault."
    le "Will I see you again?"
    e "..."
    scene ch2ep2_1134
    with dissolve
    e "Yeah."
    le "Promise?"
    e "..."
    e "Yeah. I promise."
    le "*nods* Okay..." 
    scene ch2ep2_1135
    with Dissolve(1.0)
    pause
    scene ch2ep2_1136
    with Dissolve(1.0)
    pause
    scene ch2ep2_1137
    with Dissolve(1.0)
    pause
    scene ch2ep2_1138
    with Dissolve(2.0)
    pause
    stop sound fadeout 2

    scene black
    with dissolve
    with fade

    play sound ceilingfan_low loop
    scene ch2ep2_1139
    with Dissolve(2.0)
    pause
    scene ch2ep2_1140
    with Dissolve(1.0)
    pause
    play sound2 doorknock3
    pause 1.5
    play sound2 closedoor2
    scene ch2ep2_1141
    with dissolve
    cap "Meyer."
    e "Sir."
    scene ch2ep2_1142
    with dissolve
    pause
    scene ch2ep2_1143
    with dissolve
    pause
    scene ch2ep2_1144
    with dissolve
    cap "Badge. Weapon. ID."
    e "..."
    play sound2 chair2
    scene ch2ep2_1145
    with dissolve
    pause
    play sound2 papermovement
    scene ch2ep2_1146
    with dissolve
    pause
    play sound2 cloth
    scene ch2ep2_1147
    with dissolve
    pause
    scene ch2ep2_1148
    with dissolve
    pause
    play sound2 gun_magazine2
    scene ch2ep2_1149
    with dissolve
    pause
    play sound2 casepickup2
    scene ch2ep2_1150
    with dissolve
    pause
    play sound2 gun_slider
    scene ch2ep2_1151
    pause 0.7
    play sound3 bodyhit
    scene ch2ep2_1152
    pause
    play sound2 casedown
    scene ch2ep2_1153
    with dissolve
    pause
    scene ch2ep2_1154
    with dissolve
    pause
    scene ch2ep2_1155
    with dissolve
    pause
    scene ch2ep2_1156
    with Dissolve(1.0)
    pause
    scene ch2ep2_1157
    with Dissolve(2.0)
    pause
    play sound2 cloth
    scene ch2ep2_1158
    with dissolve
    cap "As of this moment, you are terminated from the department."
    cap "Grounds: insubordination, obstruction of an official DFCS proceeding, and conduct unbecoming of a sworn officer."
    cap "Your record will reflect all three."
    e "..."
    cap "Any future application to law enforcement—any department, any jurisdiction—will require a full disclosure review."
    cap "You'll likely never hold a badge again."
    scene ch2ep2_1159
    with dissolve
    cap "..."
    cap "Is that the Francis location?"
    e "Yes."
    play sound2 bookopen
    scene ch2ep2_1160
    with dissolve
    cap "Good work."
    cap "For what it's worth."
    e "..."
    play sound2 bookclose
    scene ch2ep2_1161
    with dissolve
    cap "The Francis case will be handed to Sicae."
    cap "Should've been theirs from the off, if I'm being honest."
    cap "The trafficking network, the sister, whatever he's actually after—"
    cap "That's not our standard jurisdiction. That's their world. We were always just on the fringes."
    cap "They'll see it through."
    e "..."
    scene ch2ep2_1162
    with dissolve
    pause
    scene ch2ep2_1163
    with dissolve
    cap "I've got four kids, Meyer."
    cap "Four."
    cap "And I'd like to think I'd have done exactly what you did."
    pause 0.5
    scene ch2ep2_1164
    with dissolve
    cap "But I wouldn't have."
    cap "Because I know what this job demands. And so did you. That's what makes this particularly hard to stomach."
    scene ch2ep2_1165
    with dissolve
    pause
    scene ch2ep2_1166
    with dissolve
    cap "I came up under a detective named Garcia. Twenty-two years on the force. Best I've ever seen."
    cap "Lost his badge over a case not entirely unlike this one."
    cap "I watched him hand it over."
    cap "Told myself I'd never be the one on the other side of that desk."
    scene ch2ep2_1167
    with dissolve
    cap "But here we are."
    e "..."
    scene ch2ep2_1168
    with dissolve
    cap "Whatever happens with the child, that's no longer your concern. Professionally."
    cap "I trust you understand the distinction."
    e "Yes, sir."
    scene ch2ep2_1169
    with Dissolve(1.0)
    pause
    cap "You were one of the best I had, Meyer. Don't make me regret saying that."
    play sound2 closedoor2
    scene ch2ep2_1170
    with dissolve
    pause
    scene ch2ep2_1171
    with Dissolve(2.0)
    e "..."
    stop music fadeout 2
    stop sound fadeout 2
    
    scene black
    with dissolve
    with fade

    play music 'audio/YellowTapeDrift.mp3'
    play sound police_distant loop
    scene ch2ep2_1172
    with Dissolve(2.0)
    pause
    scene ch2ep2_1173
    with dissolve
    nic "Lycoris. Do you copy?"
    la "*comms* Go ahead."
    nic "He's not here."
    nic "Most of his men stood down. One didn't. He's been handled. The rest are with the police."
    mc "*comms* What about the location?"
    scene ch2ep2_1174
    with dissolve
    nic "..."
    nic "You're going to want to see this yourself."
    mc "*comms* Talk to me, Nicky."
    nic "... Photos. Mostly children. Every face scratched out except one."
    nic "The center photo. No scratch marks."
    mc "*comms* Leah?"
    nic "Yeah."
    scene ch2ep2_1175
    with dissolve
    nic "There's a mirror too. Cracked. Empty polaroid film tucked into the frame."
    nic "No photo. Just the film."
    nic "What the hell is going on in this guy's head?"
    scene ch2ep2_1176
    with dissolve
    nic "And there's books."
    nic "Human Anatomy. Medical Practices. An Analysis of Healthcare. The Human Mind."
    scene ch2ep2_1177
    with Dissolve(0.1)
    nic "Ooh, can I—"
    y " *comms* Not the time for shopping, Princess."
    nic "Damn it."
    la "*comms* Bag everything. Don't touch anything else."
    nic "Copy."
    stop sound fadeout 2
    scene ch2ep2_1178
    with dissolve
    la "If he's not there, then..."
    mc "His composure's gotten better. His thinking hasn't. He always figures he's the smartest guy in the room."
    mc "He'll be here."
    scene ch2ep2_1179
    with dissolve
    pause
    play sound2 carmoving loop
    scene ch2ep2_1180
    with dissolve
    pause
    stop sound2 fadeout 2
    play sound3 jesscarroar
    scene ch2ep2_1181
    with dissolve
    mc "And... there he is."
    la "*chuckles*"
    play sound2 cardoorclose
    scene ch2ep2_1182
    with dissolve
    fr "I was wondering why the street was empty."
    mc "You should've stayed in your cave."
    scene ch2ep2_1183
    with dissolve
    fr "And miss this?"
    scene ch2ep2_1184
    with dissolve
    pause
    scene ch2ep2_1185
    with dissolve
    pause
    scene ch2ep2_1186
    with dissolve
    pause
    scene ch2ep2_1187
    with Dissolve(2.0)
    pause
    scene ch2ep2_1188
    with dissolve
    fr "You found the location through her, didn't you? The detective."
    fr "She's something. You should hold onto her."
    mc "Maybe. Could've also used men who don't roll over the second someone flashes a badge."
    fr "..."
    mc "Take him in."
    scene ch2ep2_1189
    with dissolve
    fr "I'll find another one, you know."
    fr "I always do."
    mc "Good luck with that. Hope your \"sister\" finally gets some rest."
    stop music
    play sound cloth2
    scene ch2ep2_1190
    cl "Shall we see how long that bravado lasts, boy?"
    scene black
    play sound waterphone4
    pause
    
    scene black
    with dissolve
    with fade

    play sound nightambience2 loop fadein 2
    play sound2 cardriveaway
    scene ch2ep2_1191
    with dissolve
    pause
    scene ch2ep2_1192
    with dissolve
    pause
    play sound2 cloth
    scene ch2ep2_1193
    with dissolve
    pause
    scene ch2ep2_1194
    with dissolve
    pause
    play sound2 cloth
    scene ch2ep2_1195
    with dissolve
    ju "I'm sorry, Emma."
    e "... You did what you had to do."
    ju "So did you."
    e "..."
    scene ch2ep2_1196
    with dissolve
    ju "*exhales*"
    ju "I shouldn't be telling you this, but the placement is void."
    e "Cara."
    ju "Yeah. Family's been sent home. Case is flagged for reassessment."
    ju "Leah's back at the hospital for now. Same room."
    ju "We added some extra security measures, but it's not like we can just lock her in there."
    e "..."
    scene ch2ep2_1197
    with dissolve
    ju "She asked about you while we were sorting things out."
    e "What did she say?"
    ju "Asked if you were going to be okay."
    ju "Just that."
    ju "... I didn't have an answer for her."
    scene ch2ep2_1198
    with dissolve
    pause
    scene ch2ep2_1199
    with dissolve
    ju "Get some sleep. Both of you."
    scene ch2ep2_1200
    with dissolve
    pause
    scene ch2ep2_1201
    with dissolve
    mc "Come on. You need to eat."
    e "I'm not really hungry."
    mc "When's the last time you ate?"
    e "I... don't remember."
    mc "Em..."
    e "..."
    scene ch2ep2_1202
    with dissolve
    mc "Come on."
    stop sound fadeout 2

    scene black
    with dissolve
    with fade

    $ phone_time_add(hours=15)
    play sound firewood loop fadein 2
    play sound2 nightambience2 loop fadein 2
    scene ch2ep2_1203
    with dissolve
    pause
    scene ch2ep2_1204
    with dissolve
    pause
    scene ch2ep2_1205
    with dissolve
    pause
    scene ch2ep2_1206
    with dissolve
    pause
    scene ch2ep2_1207
    with dissolve
    mc "Talk to me."
    e "About what?"
    mc "About whatever's been eating you alive since you walked out of that hospital."
    scene ch2ep2_1208
    with dissolve
    e "..."
    e "There's nothing to talk about. The placement fell through. June will find another family. That's it."
    mc "Is that what you want?"
    e "What I want doesn't factor into this."
    mc "You said that last time too. Cut it out, Em."
    e "... Because it's true."
    mc "You blocked a DFCS transfer. Told June you fell in love with Leah in front of her supposed foster family."
    mc "If what you want doesn't factor in, you've got a real strange way of showing it."
    scene ch2ep2_1209
    with dissolve
    e "What do you want me to say, [mc]?"
    mc "Whatever you've been choking on."
    e "..."
    scene ch2ep2_1210
    with dissolve
    e "The truth is, I lost my badge, my career, and probably my credibility in one afternoon."
    e "The truth is, June pulled me off the case and I still showed up."
    e "The truth is, I can't stop thinking about a ten-year-old we pulled out of a trafficking ring."
    mc "I'm not asking about those. I'm asking what's underneath all of it."
    scene ch2ep2_1211
    with dissolve
    e "..."
    e "If I say it out loud, I can't take it back."
    mc "Em... What am I to you? Don't you trust me?"
    e "*softly nods*"
    mc "Then say it."
    play sound3 cloth
    scene ch2ep2_1212
    with Dissolve(1.0)
    pause
    scene ch2ep2_1213
    with dissolve
    e "I want to adopt her."
    mc "Oh. Okay."
    e "Not okay."
    mc "Why?"
    scene ch2ep2_1214
    with dissolve
    pause
    scene ch2ep2_1215
    with dissolve
    e "Because I'll have to feed her. Take her to school. Help with homework. Deal with the tantrums, the questions, the nights she can't sleep."
    scene ch2ep2_1216
    with dissolve
    mc "By the gods... you've already thought it through."
    e "[mc]... I'm being serious."
    mc "What? So am I."
    e "It's not that. It's just..."
    e "... I've never done any of that. I don't know how."
    mc "Nobody does the first time."
    scene ch2ep2_1217
    with dissolve
    e "So you know how?"
    mc "..."
    mc "No."
    scene ch2ep2_1218
    with dissolve
    e "And my record. That follows me everywhere now."
    e "CPS will see it. The judge will see it. Any lawyer worth half their salt will use it against me."
    e "June said the reassessment opens a door, but it's probably one I'll get turned away from."
    mc "So you'd rather not try?"
    e "I didn't say that."
    mc "Em. The paperwork, the record, the logistics—you'd grind through all of it. I've seen you do harder things on less sleep."
    mc "That's not what's stopping you."
    e "..."
    scene ch2ep2_1219
    with dissolve
    e "You know what I told you at the hospital. About my mom. About the promise."
    mc "Yeah."
    e "That was about Leah getting hurt. This is totally different."
    e "If I adopt her, I'm choosing it. On purpose."
    e "I'm walking into a room and saying, \"Depend on me. Build your life around me. I'll be the person you come home to.\""
    e "And then one day, I won't be there."
    mc "..."
    e "My mom didn't choose it either."
    e "But this would be worse. I'd be looking at a kid who's already been abandoned and saying, \"Trust me,\" knowing full well what I am."
    mc "What you are?"
    e "Temporary. I know everyone is."
    e "But do I really want to do that to a child who's already learned that lesson the hard way?"
    scene ch2ep2_1220
    with dissolve
    mc "..."
    e "She's already afraid that people will leave her, [mc]."
    e "Her mom sold her. The system shuffled her around. Every adult in her life has been a revolving door."
    e "And I'm supposed to walk through it and tell her this time is different?"
    e "What makes me different? Because I care? My mom cared. Caring didn't keep her alive."
    scene ch2ep2_1221
    with dissolve
    mc "... You're right."
    mc "You will leave her."
    scene ch2ep2_1222
    with dissolve
    pause 0.5
    mc "One day, for whatever reason, you won't be there. Could be years. Could be decades. Doesn't matter."
    mc "You'll leave. Everyone does."
    mc "Your mom left. Jovian left. The world doesn't hand out exceptions for the people who love the hardest."
    e "Then why would I put her through that?"
    scene ch2ep2_1223
    with dissolve
    mc "Because your mom had the greatest time of her life with you anyway."
    mc "I never got to meet her, but I know she wouldn't have traded a single day."
    e "..."
    mc "She knew she was dying. She knew she couldn't keep that promise. Yet she still made it."
    mc "She gave you something to hold onto when she couldn't hold you anymore."
    mc "It's been seventeen years since and you still carry it. You carried it into that club. You carried it into Leah's hospital room."
    mc "From what I see, that promise didn't break you, Em. It kept you standing."
    e "..."
    mc "You can't give Leah forever. Nobody gets to do that."
    mc "But you can be there until you can't. And that's what she'll carry."
    mc "You hear me?"
    play sound3 cloth
    scene ch2ep2_1224
    with dissolve
    pause
    play sound4 papermovement2
    scene ch2ep2_1225
    with dissolve
    pause
    scene ch2ep2_1226
    with Dissolve(1.0)
    pause
    e "I need to talk to June."
    mc "Uhh... It's almost past midnight."
    e "Then I'll be at her door first thing in the morning."
    menu:
        "I'm with you":
            $ emmapoint += 1
            $ renpy.notify(emmanotif)
            play sound3 cloth
            scene ch2ep2_1227
            with Dissolve(1.0)
            mc "Whatever happens, I'm with you."
            e "Thanks."
        "Stay quiet":
            play sound3 cloth
            scene ch2ep2_1228
            with Dissolve(1.0)
            pause
    scene ch2ep2_1229
    with Dissolve(2.0)
    pause
    stop sound fadeout 2
    stop sound2 fadeout 2
    call hide_days
    with dissolve

    scene black
    with dissolve
    with fade

    $ phone_time_add(hours=6)
    show screen day_monday with dissolve
    play sound dawnambient loop fadein 2
    scene ch2ep2_1230
    with dissolve
    pause
    play sound2 doorbell
    pause
    play sound3 doorbell
    pause 0.6
    play sound4 doorbell
    pause 0.6
    play sound5 doorbell
    pause 0.5
    play sound2 lightswitch
    scene ch2ep2_1231
    pause
    play sound3 opendoor
    scene ch2ep2_1232
    with dissolve
    ju "Jesus, Emma... It's four in the morning."
    e "Sorry. I couldn't sleep."
    ju "..."
    ju "This better be worth it."
    scene ch2ep2_1233
    with dissolve
    e "I want to submit an adoption application for Leah."
    scene ch2ep2_1234
    with dissolve
    pause
    play sound2 doorcreak2
    scene ch2ep2_1235
    with dissolve
    pause
    scene ch2ep2_1236
    with dissolve
    ju "... I'm listening."
    e "The placement is void. The review's still open."
    e "My record says what it says. I'm not here to argue that."
    e "I've got [mc]'s charity behind me. Whatever the board needs to see."
    ju "Knowing her isn't a legal qualification."
    scene ch2ep2_1237
    with dissolve
    e "No. But it's the only thing that's actually worked."
    e "She eats because she thinks I'll ask about it. She stays up late so she can be next to me a little longer."
    e "That doesn't happen for the system, June. It happens because of me."
    ju "..."
    scene ch2ep2_1238
    with dissolve
    e "I don't have a badge anymore. I can't pull rank or call in favors."
    e "All I've got is a disqualifying record and a kid who drew me holding a coffee cup before she even knew my name."
    e "If that's not enough, tell me now and I'll go home."
    scene ch2ep2_1239
    with dissolve
    ju "Adoption is a longer road than placement. You understand that."
    e "I do."
    scene ch2ep2_1240
    with dissolve
    ju "Background checks. Home evaluation. Psych review. Financial assessment."
    ju "Your termination record gets scrutinized at every stage."
    ju "And after all of that, it still goes before a judge."
    scene ch2ep2_1241
    with dissolve
    e "Okay."
    ju "..."
    ju "Submit through proper channels."
    ju "Don't knock on my door about it. Don't fish for updates."
    ju "Let. The process. Run."
    ju "God... I sound like a broken record and this point."
    scene ch2ep2_1242
    with dissolve
    ju "I'm saying this because there's a Sicae operative—or whatever they call themselves—who might be listening right there."
    e "Okay."
    scene ch2ep2_1243
    with dissolve
    ju "Same review as anyone else. No exceptions."
    e "Understood."
    ju "... And don't do this to me again at this hour. Please..."
    e "Sorry..."
    ju "Anything else?"
    e "No. That's all."
    scene ch2ep2_1244
    with dissolve
    ju "*yawns* Good night, Emma..."
    e "Good... morning...?"
    play sound2 closedoor
    scene ch2ep2_1245
    with dissolve
    pause
    scene ch2ep2_1246
    with dissolve
    pause
    scene ch2ep2_1247
    with dissolve
    mc "Well?"
    e "She didn't say no."
    scene ch2ep2_1248
    with dissolve
    e "I promised her I'd see her again."
    e "I'm going to keep that."
    stop sound fadeout 2

    scene black
    with dissolve
    with fade

    $ phone_time_add(hours=3)
    play music 'audio/AHeartbeatApart.mp3'
    scene ch2ep2_1262
    with Dissolve(2.0)
    pause
    scene ch2ep2_1263
    with Dissolve(2.0)
    pause
    scene ch2ep2_1264
    with Dissolve(2.0)
    pause
    scene ch2ep2_1265
    with Dissolve(2.0)
    pause
    call hide_days
    with dissolve
    scene ch2ep2_1266
    with Dissolve(2.0)
    $ phone_time_add(hours=24)
    show screen day_tuesday with dissolve
    pause
    scene ch2ep2_1267
    with Dissolve(2.0)
    pause
    scene ch2ep2_1268
    with Dissolve(2.0)
    pause
    scene ch2ep2_1269
    with Dissolve(2.0)
    pause
    call hide_days
    with dissolve
    scene ch2ep2_1270
    with Dissolve(2.0)
    $ phone_time_add(hours=24)
    show screen day_wednesday with dissolve
    pause
    scene ch2ep2_1271
    with Dissolve(2.0)
    pause
    scene ch2ep2_1272
    with Dissolve(2.0)
    pause
    scene ch2ep2_1273
    with Dissolve(2.0)
    pause
    scene ch2ep2_1274
    with Dissolve(2.0)
    pause
    scene ch2ep2_1275
    with Dissolve(2.0)
    pause
    call hide_days
    with dissolve
    scene ch2ep2_1276
    with Dissolve(2.0)
    $ phone_time_add(hours=39)
    show screen day_thursday with dissolve
    pause
    scene ch2ep2_1277
    with Dissolve(2.0)
    pause
    scene ch2ep2_1278
    with Dissolve(2.0)
    pause
    scene ch2ep2_1279
    with Dissolve(2.0)
    pause
    scene ch2ep2_1280
    with Dissolve(2.0)
    pause
    call hide_days
    with dissolve
    scene ch2ep2_1281
    with Dissolve(2.0)
    $ phone_time_add(hours=11)
    show screen day_friday with dissolve
    pause
    scene ch2ep2_1282
    with Dissolve(2.0)
    pause
    scene ch2ep2_1283
    with Dissolve(2.0)
    pause
    scene ch2ep2_1284
    with Dissolve(2.0)
    pause
    scene ch2ep2_1285
    with Dissolve(2.0)
    pause
    scene ch2ep2_1286
    with Dissolve(2.0)
    pause
    call hide_days
    with dissolve
    scene ch2ep2_1287
    with Dissolve(2.0)
    $ phone_time_add(hours=22)
    show screen day_saturday with dissolve
    pause
    scene ch2ep2_1288
    with Dissolve(2.0)
    pause
    scene ch2ep2_1289
    with Dissolve(2.0)
    pause
    scene ch2ep2_1290
    with Dissolve(2.0)
    pause
    scene ch2ep2_1291
    with Dissolve(2.0)
    pause
    scene ch2ep2_1292
    with Dissolve(2.0)
    pause
    scene ch2ep2_1293
    with Dissolve(2.0)
    pause
    scene ch2ep2_1294
    with Dissolve(2.0)
    pause
    scene ch2ep2_1295
    with Dissolve(2.0)
    pause
    call hide_days
    with dissolve
    scene ch2ep2_1296
    with Dissolve(2.0)
    $ phone_time_add(hours=25)
    show screen day_sunday with dissolve
    pause
    play sound lightswitch
    scene ch2ep2_1297
    pause
    stop music fadeout 3

    scene black
    with Dissolve(2.0)
    with fade

    play sound jesscarroar
    scene ch2ep2_1298
    with dissolve
    pause
    play music 'audio/WrongDoorRightDisaster.mp3'
    play sound2 cardoorclose
    scene ch2ep2_1299
    shu "EEEEY! MERRY FUCKING CHRISTMAS!"
    shu "Did the party start without the main event, or were y'all just standing around waiting for me to grace this street with my presence?"
    shu "The name's Shu, but today you can call me Santa—because I have arrived bearing the single greatest gift this miserable neighborhood has ever had the privilege of witnessing!"
    play sound woosh
    scene ch2ep2_1300
    shu "Behold! Feast your peasant eyes upon perfection!"
    shu "Flew halfway across the planet for this beauty."
    play sound woosh
    scene ch2ep2_1301
    shu "Half. Way. Across. The. Planet."
    shu "And before any of you ask—no, you cannot get this pretty thing in Quinara."
    shu "They told me, \"Sir, it's not available here.\""
    shu "I said, \"Then clearly your country lacks vision.\""
    shu "Three weeks to process, two layovers, one very confused customs officer, and here we are."
    shu "Style doesn't wait for availability, people. Write that down."
    scene ch2ep2_1302
    with dissolve
    mc "Who the hell are you talking to?"
    scene ch2ep2_1303
    with dissolve
    mc "Where the hell have you been? I've been trying to reach you."
    shu "Ah. Busy."
    mc "For two weeks?"
    shu "Greatness takes time, [mc]."
    scene ch2ep2_1304
    with dissolve
    shu "Also the signal in Solvern was terrible."
    shu "And Mashiro."
    shu "And wherever else I ended up."
    mc "You went to Solvern AND Mashiro."
    shu "The car had to clear two separate ports. Not my fault the world isn't more efficient."
    play sound woosh
    scene ch2ep2_1305
    shu "Anyway..."
    shu "Is that Klara's cooking? Because if it is, my timing is immaculate."
    shu "Just like me. But you already knew that."
    mc "..."
    scene ch2ep2_1306
    with dissolve
    mc "Merry Christmas, Shu."
    play sound woosh
    scene ch2ep2_1307
    shu "There's my guy!"
    shu "Happy birthday, buddy. Don't make it weird."
    play sound closedoor
    scene ch2ep2_1308
    with dissolve
    mc "*exhales*"
    stop music fadeout 4
    play music2 'audio/WhereOurHeartsFindWarmth.mp3' fadein 4
    scene ch2ep2_1309
    with dissolve
    shu "Oh, man... Smells like Christmas in here!"
    scene ch2ep2_1310
    with dissolve
    f "Look what the cat dragged in."
    shu "Ouch."
    s "Hey, welcome back!"
    shu "Sky! Looking radiant as always."
    scene ch2ep2_1311
    with dissolve
    pause
    scene ch2ep2_1312
    with dissolve
    shu "*whispers* Hey."
    mc "*whispers* Hm?"
    shu "*whispers* What's going on with her?"
    scene ch2ep2_1313
    with dissolve
    mc "*whispers* It's... a long story. There was a kid."
    shu "*whispers* A what?"
    scene ch2ep2_1314
    with dissolve
    g "Nobody breathe too hard. I almost dropped this twice already."
    g "Come on, gather up. Let's get this done before the wax goes everywhere."
    scene ch2ep2_1315
    with dissolve
    mc "Oh boy... I'm not used to this."
    g "What do you mean? We did the same thing last year."
    mc "..."
    scene ch2ep2_1316
    with dissolve
    g "Okay. On three."
    g "One."
    g "Two..."
    scene ch2ep2_1317
    with dissolve
    ev "Happy birthday to you~"
    scene ch2ep2_1318
    with dissolve
    ev "Happy birthday to you~"
    scene ch2ep2_1319
    with dissolve
    ev "Happy birthday dear [mc]~"
    scene ch2ep2_1320
    with dissolve
    ev "Happy birthday to youuuu~!"
    f "AND MANY MOOORE~!"
    mc "... And many more."
    scene ch2ep2_1321
    with dissolve
    pause
    scene ch2ep2_1322
    with dissolve
    mc "*takes a breath*"
    $ renpy.sound.set_volume(0.3, 0.0)
    play sound jesscarroar
    pause 0.5
    scene ch2ep2_1323
    with dissolve
    s "Who's that?"
    k "Anyone expecting someone?"
    $ renpy.sound.set_volume(1.0, 0.0)
    scene ch2ep2_1324
    with dissolve
    pause
    a "Em..."
    scene ch2ep2_1325
    with Dissolve(0.2)
    a "Em!"
    scene ch2ep2_1326
    with Dissolve(0.1)
    pause
    play sound running loop
    scene ch2ep2_1327
    with dissolve
    pause
    play sound closedoor
    scene ch2ep2_1328
    with dissolve
    pause
    stop music2 fadeout 5
    scene ch2ep2_1329
    with dissolve
    pause
    scene ch2ep2_1330
    with dissolve
    pause
    scene ch2ep2_1331
    with dissolve
    pause
    $ renpy.music.set_volume(1.0, 1.0)
    play music ["<from 70 to 141>audio/TheRhythmOfTheirHearts_var.mp3"] fadein 2
    queue music 'audio/TheRhythmOfTheirHearts_var.mp3' loop
    scene ch2ep2_1332
    with Dissolve(2.0)
    pause
    show emmaexpressionwork
    with dissolve
    pause 5.8
    scene ch2ep2_1333
    with dissolve
    le "Aunt June said my name is Leah Meyer now."
    scene ch2ep2_1334
    with dissolve
    pause
    scene ch2ep2_1335
    with dissolve
    ju "*slowly nods*"
    scene ch2ep2_1336
    with Dissolve(2.0)
    pause
    scene ch2ep2_1337
    with dissolve
    pause
    play sound cloth
    scene ch2ep2_1338
    with dissolve
    pause 0.5
    e "*softly* Leah..."
    scene ch2ep2_1339
    with Dissolve(2.0)
    le "*wails*"
    e "It's okay... it's okay... I'm here now."
    scene ch2ep2_1340
    with dissolve
    pause
    play sound closedoor
    scene ch2ep2_1341
    with dissolve
    pause
    scene ch2ep2_1342
    with Dissolve(2.0)
    pause
    scene ch2ep2_1343
    with dissolve
    pause
    scene ch2ep2_1344
    with dissolve
    pause
    scene ch2ep2_1345
    with dissolve
    ju "Your application went through the standard review, and your termination record flagged at every stage like I told you it would."
    ju "But then the testimonies came in and... that changed things."
    ju "Especially Park's."
    scene ch2ep2_1346
    with dissolve
    e "Dr. Park?"
    ju "*nods* Mm."
    ju "Said she'd never seen a child respond to someone the way Leah responded to you."
    ju "She believed it wasn't attachment damage, but... purely an attachment."
    ju "Elaine submitted one too. Unsolicited."
    ju "She said, and I'm quoting directly, \"If you don't give that kid to Meyer I will personally make sure you have hell to pay.\""
    e "*laughs softly*"
    ju "She also included three pages of supporting documentation, so... very thorough of her."
    ju "[mc] submitted his the same day you filed."
    scene ch2ep2_1347
    with dissolve
    ju "You broke protocol as an officer."
    ju "As a civilian?"
    ju "You did everything right."
    scene ch2ep2_1348
    with Dissolve(2.0)
    e "..."
    ju "There's still a hearing. But that's just red tape at this point."
    ju "Merry Christmas, Emma."
    e "... Merry Christmas, June..."
    play sound cloth
    scene ch2ep2_1349
    with dissolve
    ju "Alright. Let's go inside before I actually start crying out here."
    le "*sniffles* You're already crying, Aunt June."
    scene ch2ep2_1350
    with dissolve
    ju "..."
    ju "Inside. Now."
    scene ch2ep2_1351
    with dissolve
    e "Where are your other toys?"
    le "I said goodbye to them. I told the nurse to give them to the other kids."
    scene ch2ep2_1352
    with Dissolve(1.0)
    le "But I kept Mr. Penguin."
    e "..."
    scene ch2ep2_1353
    with dissolve
    pause
    scene ch2ep2_1354
    with dissolve
    mc "*nods*"
    stop music fadeout 2

    scene black
    with dissolve
    with fade

    play music 'audio/WhereOurHeartsFindWarmth.mp3'
    scene ch2ep2_1355
    with Dissolve(2.0)
    pause
    scene ch2ep2_1356
    with Dissolve(2.0)
    pause
    scene ch2ep2_1357
    with dissolve
    mc "I'll open them after dinner."
    f "You said that last year, then you fell asleep."
    if gwenroute:
        scene ch2ep2_1358
        with dissolve
        pause 0.5
        mc "There was... a situation last year."
    else:
        scene ch2ep2_1359
        with dissolve
        mc "No, I didn't."
    scene ch2ep2_1360
    with dissolve
    pause 0.5
    mc "Sora—I mean Moon."
    scene ch2ep2_1361
    with dissolve
    m "Gwen's gift from last year is still wrapped in your office drawer."
    scene ch2ep2_1362
    with dissolve
    g "It's fine. I returned it."
    mc "You returned it?! When were you in my drawer?"
    g "You said you'd open it later."
    mc "Yeah. I meant later. Not never—"
    g "It's fine."
    mc "Gwen—"
    g "Open your gifts, [mc]."
    mc "*sighs*"
    play sound woosh
    scene ch2ep2_1363
    f "Okay, mine first! Mine first!"
    mc "Why yours first?"
    f "Because I said so. Duh..."
    play sound rummage_paper2
    scene ch2ep2_1364
    with dissolve
    mc "..."
    mc "This is a gift card."
    f "A very generous gift card."
    mc "To sincerely yours' streaming merch store."
    mc "You have a merch store? How did I not know about this?"
    f "How do you think I survive?"
    mc "Fair enough... Thanks, Frey."
    play sound woosh
    scene ch2ep2_1365
    shu "Alright. Mine next."
    mc "I don't trust you..."
    play sound rummage_paper2
    scene ch2ep2_1366
    with dissolve
    pause
    shu "Had it custom made. You're welcome in advance."
    scene ch2ep2_1367
    with dissolve
    mc "..."
    mc "Bro... This is a portrait."
    shu "Of me, yes."
    mc "You got me a portrait of yourself. What am I supposed to do with this?"
    shu "Hang it somewhere prominent. So you never forget what peak male performance looks like."
    mc "..."
    scene ch2ep2_1368
    with Dissolve(0.2)
    f "Pfft— *laughs*"
    scene black
    with dissolve
    scene ch2ep2_1369
    with Dissolve(2.0)
    pause
    scene ch2ep2_1370
    with dissolve
    pause
    scene black
    with dissolve
    scene ch2ep2_1371
    with Dissolve(2.0)
    pause
    scene black
    with dissolve
    scene ch2ep2_1372
    with Dissolve(2.0)
    pause
    scene black
    with dissolve
    scene ch2ep2_1373
    with Dissolve(2.0)
    pause
    scene black
    with dissolve
    scene ch2ep2_1374
    with Dissolve(2.0)
    pause
    scene ch2ep2_1375
    with dissolve
    pause
    scene ch2ep2_1376
    with dissolve
    pause
    if not emmaroute:
        scene black
        with dissolve
        scene ch2ep2_1377
        with Dissolve(2.0)
        pause
        scene ch2ep2_1378
        with dissolve
        pause
    scene black
    with dissolve
    scene ch2ep2_1379
    with Dissolve(2.0)
    pause 0.5
    k "Oh? Looks like there's one more."
    scene ch2ep2_1380
    with dissolve
    e "*whispers* Go on."
    le "*whispers* What if he doesn't like it?"
    e "*whispers* He's going to love it."
    le "*whispers* How do you know?"
    e "*whispers* Because if he doesn't, I'm going to kick his butt."
    scene ch2ep2_1381
    with dissolve
    mc "Leah?"
    le "..."
    mc "Come on. Don't be shy."
    scene ch2ep2_1382
    with Dissolve(1.0)
    pause
    scene ch2ep2_1383
    with dissolve
    g "Hey. Pay attention."
    scene ch2ep2_1384
    with dissolve
    le "I made this for you."
    le "Aunt June got me the frame."
    scene ch2ep2_1385
    with dissolve
    mc "..."
    le "I got the necklace wrong the first time. The key was too big, so I started over."
    le "And your hair is hard to draw. It goes everywhere. I almost gave up on it."
    scene ch2ep2_1386
    with dissolve
    mc "Leah."
    le "Mm?"
    mc "When did you draw this?"
    le "After the \"episode.\" That's what Dr. Park called it. When you sat with me."
    scene ch2ep2_1387
    with dissolve
    le "I couldn't draw it that day because my hands were still shaky. So I did it from memory the next morning."
    mc "..."
    scene ch2ep2_1388
    with dissolve
    mc "This is really good. I didn't know you could draw like this."
    le "Thank you."
    scene ch2ep2_1389
    with dissolve
    mc "Did you know?"
    e "Mm-hm."
    scene ch2ep2_1390
    with dissolve
    mc "You gave me Emma's coffee."
    le "You steal each other's coffee. I saw you do it three times that afternoon."
    le "You always pretend you don't want it. Then you make that exact face."
    scene ch2ep2_1391
    with dissolve
    e "..."
    mc "*chuckles* Yep. That's me alright."
    mc "Thanks, Leah. I love it. This is going on my desk."
    scene ch2ep2_1392
    with Dissolve(0.2)
    pause 0.5
    e "See? Told you."
    scene ch2ep2_1393
    with Dissolve(1.0)
    k "Alright. The turkey's done in twenty minutes."
    f "FINALLY!"
    k "Sky. Help Aine with the table, please."
    s "Aye aye!"
    shu "Someone tell me Klara made her thing."
    g "She did."
    shu "Nice!"
    ju "I should probably head home."
    k "Eat first, at least."
    mc "You're already here. Least we can do is feed you."
    ju "..."
    ju "Fine."
    mc "Besides, you don't have anyone waiting anyway."
    ju "I have a cat, you know?"
    mc "The cat will survive."
    ju "*sighs* Fine. Alright..."
    mc "I'm gonna take these upstairs real quick. Be right back in a minute."
    if (emmaroute and emmapoint == 9):
        scene ch2ep2_1394
        with dissolve
        e "..."
        scene ch2ep2_1395
        with dissolve
        le "..."
        scene ch2ep2_1396
        with dissolve
        le "Why did Emma follow him?"
        ju "... Adult things, Leah."
        le "Oh..."
        le "..."
        le "Like taxes?"
        ju "... Sure. Like taxes."
        stop music fadeout 2

        scene black
        with dissolve
        with fade

        label insubordinatepussy:
        if _in_replay:
            $ name = persistent.gallery_name
        scene ch2ep2_1458
        with dissolve
        pause
        play sound closedoor
        scene ch2ep2_1459
        with dissolve
        mc "She's rather observant, huh?"
        e "Yeah."
        e "... How long did it take you to know me back then?"
        mc "*chuckles* I can't even remember anymore. Quite some time, for sure."
        e "Just a few days and she can already read me like a book."
        mc "Well? I'm sure she'll pick up more pointers from you."
        e "..."
        scene ch2ep2_1460
        with dissolve
        mc "Alright, let's head back down before Klara sends a search party."
        play sound doorlock
        pause 0.5
        "The lock clicks behind you."
        play music 'audio/UndercoverChristmas.mp3'
        scene ch2ep2_1461
        with dissolve
        mc "... Em?"
        "You know better than to believe that was an accident. Every move from Emma, Detective Meyer, is calculated and planned."
        "She leans against the door with her hands behind her back, chin lowered, watching you the way a cat leers at a bird that hasn't yet figured out it's trapped."
        "You've seen every version of her. The detective. The wreck. The woman who cried on your floor once."
        "But this one? This one's new."
        e "You know what I realized today?"
        mc "That we have a house full of people waiting on a turkey right now?"
        e "I've been breaking the rules for weeks."
        mc "..."
        scene ch2ep2_1462
        with dissolve
        e "Obstructed federal proceedings."
        e "Defied a direct order."
        e "Interfered with an active case I was explicitly removed from."
        mc "Em, where is this—"
        e "Insubordination. Conduct unbecoming. Hale read me the whole list."
        mc "... You already told me about those."
        e "Mm... I did."
        play sound handcuff_movement
        scene ch2ep2_1463
        with dissolve
        "She brings her hand forward. A pair of handcuffs hang from one finger, swaying and catching the lamplight."
        "Your brain does the math."
        mc "Are those yours?"
        e "Hale took my badge and my gun. He forgot these."
        mc "Somehow, I doubt he forgot."
        scene ch2ep2_1464
        with dissolve
        "She pushes off the door and crosses the room in four steps. Each one lands with the kind of purpose that makes you very aware of how small this room is." #
        e "I've been a real delinquent, [mc]. Broken just about every rule there is."
        mc "Not really every rule, but..."
        e "Someone should probably do something about that."
        scene ch2ep2_1465
        with dissolve
        "She holds them out to you. Cold steel, warm fingers."
        "You're thinking about Klara's turkey. You're thinking about the people downstairs."
        "About the painting of Shu."
        "About literally anything other than what your body wants to do right now."
        scene ch2ep2_1466
        with dissolve
        mc "..."
        e "You didn't think I forgot about your gift, did you?"
        mc "I thought the drawing was my gift."
        e "That was Leah's. This one's mine."
        scene ch2ep2_1467
        with dissolve
        "She takes your hand and sets the cuffs into your palm. Then, one by one, she folds your fingers closed around the metal, never looking away from your eyes the whole time." #
        e "I've been out of line, so go ahead."
        mc "Go ahead and what?"
        e "Apprehend me."
        scene ch2ep2_1468
        with dissolve
        mc "Em, everyone's downstairs."
        e "Then you'd better be quick."
        mc "Klara will—"
        e "Klara said the turkey's twenty minutes. That's plenty."
        mc "Plenty for what, exactly?"
        e "For you to do your job, officer."
        scene ch2ep2_1469
        with dissolve
        "She turns around. Puts her wrists together behind her back."
        "Looks at you over her shoulder with an expression that has no business being on the face of a woman who was looking lost in your living room."
        "Downstairs, someone laughs. Plates clink. None of that matters right now."
        e "Well? I'm resisting arrest."
        mc "*chuckles* No, you're not."
        e "Then make me."
        play sound bodyhit
        scene ch2ep2_1470
        with hpunch
        "So, you do."
        "Your hand finds the back of her neck. Your fingers close around it: firm, but not too tight."
        scene ch2ep2_1471
        with dissolve
        "You walk her forward until her chest meets the door."
        "The wood shudders. Downstairs, someone laughs at something Freya said."
        "Emma's breath catches."
        mc "Hands stay where they are."
        e "Yes, sir."
        mc "That's officer to you."
        play sound handcuff_lock
        scene ch2ep2_1472
        "You take the cuffs from your other hand. Her wrists are already together behind her back, waiting. She did half the work for you."
        "The first bracelet clicks shut around her left wrist. She flinches, and you feel it travel through her spine into your palm."
        play sound handcuff_lock
        scene ch2ep2_1473
        "The second one closes. The sound is obscene in a room this quiet."
        mc "Emma Meyer. You're under arrest for being a colossal pain in my ass for the past year."
        e "Only a year?"
        mc "We'll add the other charges as they come."
        e "Mm... Thorough..."
        scene ch2ep2_1474
        with dissolve
        "You press yourself against her from behind. Your stiffening cock settles against the curve of her ass."
        "She pushes back into you like she has you right where she wants you, despite the fact that she's the one restrained."
        "Your mouth finds the spot behind her ear where her perfume once was, but now all that's left is her."
        "She tilts her head to give you room. Very cooperative."
        mc "You have the right to remain silent."
        e "I won't be."
        mc "Didn't think you were gonna."
        play sound cloth
        scene ch2ep2_1475
        with dissolve
        "Your hand tugs at the button of her jeans. One pop."
        "The zipper follows. You drag the denim down past her hips."
        "The warmth radiating off her bare thighs hits your knuckles before you even touch her."
        play sound cloth
        scene ch2ep2_1476
        with dissolve
        "You reach around. Your fingers find the front of her blouse and pull it up. Her bra follows."
        show emma20
        with dissolve
        "You slowly roll your hips into her. She feels you thicken, and her breath stutters."
        e "Mmnhh..."
        mc "Hold still, criminal."
        e "You're really enjoying this."
        mc "It's my birthday. I'm allowed to."
        "Her forehead presses against the door. You grind your swollen length into the cleft of her ass, straining against your pants."
        "The friction drags a low sound out of her throat."
        "She pushes back against you, testing how much slack she has. The cuffs bite into her wrists and she stops."
        e "Just taking inventory? Or are you going to do something?"
        mc "Patience, detective."
        e "Former detective."
        mc "Even worse. No badge, no authority. Which means you don't get to give orders."
        e "... That shouldn't work as well as it does."
        mc "Yet, here you are. Wet and cuffed against my bedroom door."
        e "..."
        scene ch2ep2_1477
        with dissolve
        hide emma20
        "Your hand slides down her back. She sucks in a breath when your fingers dip between her thighs and find the damp elastic of her underwear."
        mc "Filed under: additional evidence."
        e "[mc]..."
        mc "Shhh..."
        show emma21
        with dissolve
        "You tug the fabric aside. Your finger meet her flushed, swollen folds."
        "She bites her lips when you drag along the length of her dripping slit, parting her slowly. The sound that leaks out of her is more air than voice."
        e "Hhnn... how long are you going to keep doing that?"
        mc "Depends. How long do you want to keep pretending you're in charge?"
        e "I never said I was in charge."
        mc "Your mouth says one thing. This soaking pussy says another."
        "She's rocking against your hand now. Your finger slide between, circling her swollen clit and teasing her tight entrance. Small, involuntary motions that she'd deny if pointed out."
        "You let her have it for a while."
        show emma22
        with dissolve
        hide emma21
        "Now, you sink both fingers into her needy cunt, knuckle-deep."
        "Her velvet walls grip you as if they've been starving."
        e "Ahh... [mc]..."
        mc "You're dripping on my floor, Em."
        e "Hngg...! Your fault."
        "You curl your fingers inside her. Her knees almost give."
        scene ch2ep2_1478
        with dissolve
        hide emma22
        "Then, abruptly, you pull your hand away. Her arousal strings between your glistening fingers."
        e "Why did you—"
        mc "Because I can."
        e "..."
        e "I hate you."
        mc "I don't think you do."
        play sound belt
        scene ch2ep2_1479
        with dissolve
        "Your zipper comes down. The teeth separate one by one, loud in the closed room, and she goes still."
        mc "That's what I thought."
        mc "I know troublemakers like you. All it takes is a firm hand and you shut up right away."
        mc "Or in this case, a firm {i}man{/I}."
        "You can feel Emma roll her eyes, but she doesn't retort. She knows what's next, and not even the worst of your one-liners will get in the way of her need."
        "The aching cock that's been straining against your pants since she clicked that lock finally comes free. Thick, flushed, and the relief is immediate."
        scene ch2ep2_1480
        with dissolve
        "You lean forward until your lips are against her ear. Your cock brushes against her bare ass."
        mc "Last chance to lawyer up."
        e "Shut up and fuck me."
        mc "Oof... Not even trying to deny our crimes? Foolish, but brazen."
        scene ch2ep2_1481
        with dissolve
        "You press your head against her entrance, dragging it through the wet mess between her thighs."
        "She whimpers."
        "Emma Meyer, the detective, who faced down armed traffickers without flinching, whimpering because you won't put it in."
        e "[mc], if you don't—"
        mc "Ask nicely."
        scene ch2ep2_1482
        with dissolve
        e "... Please."
        mc "Please what?"
        e "Please fuck me, officer."
        mc "See? Cooperation gets you everywhere."
        show emma23
        with dissolve
        "You slide your thick, rigid length into her slick, insubordinate pussy in one slow stroke."
        "Engorged and aroused from the teasing, Emma takes all of you with her teeth clenched and her cuffed hands balling into fists."
        "The door absorbs the sound. Barely."
        e "God...!"
        mc "Wrong name."
        e "Don't push it."
        mc "I already am."
        "You set a measured rhythm. Each thrust pins her chest against the door, creaking it just enough that it would cause a big problem if anyone were to walk through the hallway."
        "Emma doesn't care. Her cheek is flat against the wood, eyes half-shut and mouth hanging open."
        "Her bare breasts squeeze against the cold surface of the door with each stroke."
        e "Harder."
        mc "Again with the rudeness. What's the magic word?"
        e "..."
        e "Please..."
        e "Please, officer. Harder."
        e "I—nnh... need it harder."
        mc "That's better."
        "You grab her shoulder, tugging her back into the next stroke."
        "The angle changes and your cock hits something deeper. Her whole body curls."
        e "Hnhh... right there. Right fucking there."
        mc "Here?"
        e "You know where."
        mc "I want to hear you say it."
        e "... You really are the worst."
        mc "Same day as last year. Happy birthday to me."
        "The pace stays deliberate. You're not in a hurry—she is. And that gap between your patience and her need is doing more work than your dick-scipline is."
        "Emma's breathing goes ragged. Her shoulders strain against the cuffs."
        "You can feel her greedy womanhood clenching around you with every thrust, trying to pull you in deeper."
        e "[mc], I can't— with my hands like this—"
        mc "You brought the handcuffs, Em."
        e "I'm well aware of that."
        mc "So deal with it."
        "She laughs. A breathless, defeated laugh that turns into something else when you bottom out and hold. Your cock buries itself to the hilt, pressed flush against her deepest wall."
        e "Oh, fuck..."
        mc "Language. I'll add profanity to your charges."
        e "My charges are already longer than your—"
        mc "Finish that sentence. I dare you."
        e "..."
        e "Hhng... point taken."
        mc "That's what I thought."
        show emma24
        with dissolve
        hide emma23
        "You pick up the pace. Her back arches away from the door, pressing into your chest. The cuffs dig into your stomach."
        "Each stroke is wetter than the last. The filthy, slapping sound of you plunging into her drenched cunt fills the room."
        "It's a small miracle nobody's come upstairs yet."
        "Downstairs, Klara calls something out. Neither of you process a single word."
        e "Haaanh~! Unggh~! [mc]— someone's going to hear."
        mc "Then be quieter."
        e "That's— hhn— easy for you to say when you're balls deep."
        mc "Excuses."
        show emma25
        with dissolve
        hide emma24
        "Your hand moves from her hip to her mouth. Two fingers, pressed lightly against her lips."
        "Emma opens, takes them in and sucks, cutting the sound of her defiance."
        "Her eyes close. The tension in her shoulders melts. Your fingers taste like her and she knows it."
        "She trusts you, even like this: wrists locked behind her back, blouse hanging open, jeans around her thighs..."
        "... Your cock stretching her pussy open against a door in a house full of people who are going to wonder where the birthday boy went."
        "She trusts you completely."
        mc "You're shaking."
        e "Mm—"
        mc "Close?"
        e "Mm-hm."
        mc "No. Not yet."
        "You slow down. She makes a sound behind your fingers that vibrates through your knuckles."
        mc "Not until I say so."
        e "..."
        mc "Nod if you understand."
        "She nods."
        mc "Good girl."
        scene ch2ep2_1483
        with dissolve
        hide emma25
        "You pull out. Your slick cock leaves her with an obscene, wet pop and she gasps."
        "The sudden emptiness buckles her knees. You catch her by the waist."
        "Her thighs are glazed. A thin, glistening trail runs down her legs."
        play sound cloth
        scene ch2ep2_1484
        with dissolve
        "You take her jeans off. She steps out of them without complaint."
        "You slip her out of her panties next, leaving her bottomless."
        mc "To the desk."
        e "What?"
        mc "Move, criminal."
        play sound cloth
        scene ch2ep2_1485
        with dissolve
        "You take off your shirt. She hears the fabric hit the floor and turns her head."
        e "Oh, now you undress."
        mc "My room. My rules."
        e "You couldn't have done that five minutes ago?"
        mc "You were busy."
        scene ch2ep2_1486
        with dissolve
        "She looks you over. Takes her time with it. Her eyes drop... and stay there."
        e "..."
        mc "Something to say?"
        e "No. Just appreciating the... evidence."
        scene ch2ep2_1487
        with dissolve
        "You bend Emma forward over the desk, her hands still cuffed."
        "Her cheek presses against the wood. The desk lamp is still on, casting her shadow up the wall."
        "Her breathing fogs the surface. Her bare, plump ass is up, the open blouse hanging off her breasts like an afterthought."
        "From this angle, you can see almost everything. How flushed and puffy her lips are."
        "How her neglected cock socket glistens under the lights, twitching, clenching around nothing."
        "Craving to be filled."
        scene ch2ep2_1488
        with dissolve
        e "This is your workspace."
        mc "And you're disrupting it."
        e "Charge me."
        mc "Don't worry. I intend to."
        show emma26
        with dissolve
        "You press your swollen head against her entrance and push."
        e "Ahhhh~! Oh god...!"
        "The angle helps her swallow you whole, deeper than before, and her taut walls grip you so tight your vision narrows."
        "Her fingers curl. The cuffs clink against each other."
        mc "Different from the door?"
        e "Mm-hm... So much deeper."
        "The desk creaks under her. Your hand rests on her lower back, pinning her down. Her velvety sugar walls flutter around your buried cock, adjusting, stretching to take you in."
        "The room reeks of musk, her shampoo, and the fading cologne you put on hours ago."
        e "You're going slow on purpose."
        mc "Observant."
        e "I'm going to kill you."
        mc "That means I can add attempted murder to your charges."
        e "Do something about it before I break out of these cuffs and act on my threat."
        mc "Always with the attitude."
        "You push her back even more. Your cock shifts inside her and she moans into the wood."
        mc "You spent the entire week breaking every rule in the book."
        e "Mm-hm..."
        mc "Obstructed proceedings. Defied your captain. Got yourself fired."
        e "You're— hhng— really reciting my charges while your cock is inside me?"
        mc "I'm multitasking."
        "You thrust deeper. She gasps against the desk."
        mc "Blocked a federal transfer."
        "Thrust."
        e "[mc]—"
        mc "Told a room full of people you fell in love with a ten-year-old."
        "Thrust."
        e "Nnhh~!"
        mc "Knocked on June's door at four in the morning."
        "THRUST." with hpunch
        e "Ghh~! That one was your fault."
        mc "How?"
        e "You made me brave enough to do it."
        mc "..."
        mc "Say that again."
        e "You heard me—"
        show emma27
        with dissolve
        hide emma26
        "You speed up, forcing her to swallow whatever she was about to say."
        "Your cock drives into her fast enough that her body lurches forward with each stroke."
        "Each thrust pushes her hips into the edge of the desk. The lamp shudders. The pens in the holder rattle."
        "Your palm cracks against her bare ass. Sharp. Clean. The sound fills the room and she yelps into the wood."
        e "Ahhhh—!"
        mc "That's for knocking on June's door at four AM."
        e "I just said— hhh— that was your fault—"
        mc "Is it?"
        "Another slap. The reddening skin blooms pink under your hand. She bites her lip hard enough to leave a mark."
        e "Nnh...!"
        mc "That one's for consuming nothing but coffee for three days straight."
        e "I ate a sandwich—"
        mc "Half a sandwich."
        e "More than half."
        mc "Leah disagrees."
        "Your hand comes down again. Her whole body jolts forward, cuffed hands jerking."
        "She squeezes your length so hard you almost lose your rhythm."
        e "Hnhh—! God... [mc]!"
        mc "That's for making a ten-year-old worry about your eating habits."
        "She's trembling under you. Her voice has gone thin at the edges, fraying with each breath."
        e "[mc]... please..."
        mc "Please what?"
        e "Please don't stop."
        mc "Don't stop what?"
        e "Please don't stop pounding me! Punish me!"
        show emma28
        with dissolve
        hide emma27
        "You give her what she's asking for. The desk protests. You hold her steady while you ram into her."
        "The wet, rhythmic slap of skin on skin fills the room, your engorged member slamming into her battered, grateful pussy."
        "Emma's sounds are shattering whatever plausible deniability the two of you have left, should anyone walk past the door right now."
        mc "Shh... Keep it down, criminal."
        e "I'm trying—"
        mc "You need to try harder."
        e "Then stop hitting that spot—"
        e "It makes me— hhnn— makes me want to scream your name in a house full of people!"
        "Your hand slaps her ass one more time. Lighter. Almost affectionate, if that word applies to a handprint."
        mc "Damn. You've got quite the lovely mark down here."
        e "Whose fault is that?"
        mc "Yours. You brought the handcuffs."
        e "I'm starting to regret that."
        mc "Are you? Doesn't seem like it to me."
        "Her ravaged walls pulse around you, greedy, trying to milk something out that you're not ready to give yet."
        "Her toes curl. The lighting casts your shadows on the wall, merged into one shape."
        e "[mc]..."
        mc "Mm?"
        e "I'm close."
        mc "I know. I can feel you strangling me."
        e "Are you going to stop me again?"
        mc "Depends on how nicely you ask."
        "She turns her head. Her cheeks are flushed, eyes glassy, lips swollen. She looks at you over her shoulder the same way she did when she handed you the cuffs."
        e "Please let me come."
        mc "..."
        mc "That wasn't bad."
        e "I will actually murder you."
        mc "Hold it."
        e "[mc]—"
        mc "Hold. It."
        "She grits her teeth. Every muscle in her body is fighting the instruction. Her knuckles are white behind the cuffs. Her desperate pussy is clenching around you in waves, begging for release even though her mouth is following orders."
        "You keep the pace torturously slow. Each stroke drags the full length of your dick against the raw, swollen spot that makes her fall apart, and you know exactly where it is."
        e "I can't— I'm going to—"
        mc "Not here. Come on."
        scene ch2ep2_1489
        with dissolve
        hide emma28
        "You slide out, and she makes a sound like you ripped her heart out of her chest."
        e "[mc]..."
        play sound handcuff_movement
        scene ch2ep2_1490
        with dissolve
        "You uncuff both wrists. The metal falls away and she flexes her fingers, working the blood back in."
        play sound cloth
        scene ch2ep2_1491
        with dissolve
        "You slide the blouse off her shoulders. It drops. The bra follows."
        "She's naked. Completely."
        "And you stop."
        "You've seen her before. Plenty of times. But something about the lamp catching the soft curve of her stomach, the weight of her hips, the way her thighs press together when she's standing still."
        if allornothingroutev2:
            "She's not toned like Moon. She's not angular like Klara."
            "She's Emma."
        scene ch2ep2_1492
        with dissolve
        "A little soft where others are sharp. Fuller in places she never draws attention to."
        "But right now, she's completely uncovered. And the things running through your head would make her slap you if she heard them, then ask you to do every single one."
        mc "..."
        e "... What?"
        scene ch2ep2_1493
        with dissolve
        "You don't answer. You cross the distance between you and kiss her."
        "Not like the door. Not like the desk. This one is slow, unhurried."
        "She doesn't move at first. Then her fingers find your chest, like she's checking if you're real."
        "The twenty-minute clock, the turkey, the house full of people—gone. All of it, gone."
        scene ch2ep2_1494
        with dissolve
        "When you pull back, her eyes are still closed."
        e "... That was different."
        mc "Good different?"
        scene ch2ep2_1495
        with dissolve
        "She opens her eyes, yet doesn't answer. Just looks at you with something you haven't seen from her all night."
        "Not the roleplay. Not the defiance. Something underneath all of it that she's been holding back since she locked that door."
        scene ch2ep2_1496
        with dissolve
        "Her hand slides from your chest to the back of your neck and pulls you in again."
        "This one lasts longer."
        "You scoop her up. Her bare legs wrap around your waist. Her slick skin presses against yours, warm and damp, and you can feel every soft part of her against every hard part of you."
        "She keeps her lips pressed against yours the whole way."
        play sound chair
        scene ch2ep2_1497
        with dissolve
        "You lean back on the bed, propping yourself up on your hands. She climbs into your lap, facing forward."
        "Your palms press into the mattress behind you, taking your weight."
        "Emma's breathing is slower now. The urgency burned off somewhere between the kiss and the carry."
        e "No cuffs this time?"
        mc "You've served your sentence."
        e "Already? I thought the charges were extensive."
        mc "Good behavior. Time off."
        e "Mm... Lenient judge. I like that."
        "She reaches between her trembling legs and wraps her fingers around your shaft, guiding you to her entrance as she sinks down."
        show emma29
        with dissolve
        "The sound she makes when you fill her again is quiet, private, meant for a room smaller than this one."
        "A low, shuddering exhale as her body opens around you, inch by aching inch, until she's sitting flush in your lap with every last bit of you buried in her."
        e "Ahh... you're pressing against everything."
        mc "Too deep?"
        e "No. Don't you dare move back."
        "The pace is slow. Her hips do all the work, rolling against you."
        "Your dick shifts inside her with each rotation, pressed against her tender front wall, and every small movement pulls a sound out of her."
        "From this angle, leaned back beneath her, you can see the muscles in her back tense and release with every roll of her hips."
        "You want to touch her. Your fingers dig into the sheets instead."
        e "You're just going to sit there?"
        mc "Enjoying the view."
        e "Hands on the bed like a good boy?"
        mc "You're doing all the work. Don't want to get in the way."
        e "Liar. You're just watching me fall apart."
        mc "That too."
        "She doesn't have a comeback for that. Her head tilts and she lets out a breath she's been holding since the door."
        e "[mc]..."
        mc "Right there. Keep going."
        "Her hips pick up speed as she braces her hands tighter on your knees."
        "The rhythm shifts—deliberate drops that drive you deeper each time she comes back down."
        "The sounds coming out of her are half-formed words that dissolve before they land."
        e "Right there— right there, don't—"
        mc "I'm not going anywhere."
        e "Promise?"
        "Something in the way she says it has nothing to do with sex."
        mc "Yeah, Em. I promise."
        show emma30
        with dissolve
        hide emma29
        "Her pace turns desperate. Frantic. She's slamming herself down onto you, using your knees as leverage, chasing the edge with everything she has."
        "Your hips snap up to meet every drop. Arms locked, hands buried in the sheets, driving upward so hard the bed frame groans beneath you both."
        "Her thighs are shaking. Every thrust hits the same bruised spot inside her, and every impact tears another sound out of her that she can't swallow fast enough."
        e "[mc]— [mc], I—"
        mc "Em— ease up— I'm not gonna last the night if you keep doing that."
        e "I can't— help— it's too much—"
        mc "Em!"
        play sound chair
        scene ch2ep2_1498
        with hpunch
        hide emma30
        e "HHNNNNNNG~!"
        "Her whole body locks up. Her thighs clamp shut. Her wrecked hole seizes around your cock so hard it almost hurts."
        "The sound Emma makes is buried in her hand as she covers her mouth, muffled, desperate, raw."
        "The orgasm rips through her in waves. Each one ripples through her quaking thighs."
        "She's trembling. Still moving against you, riding it out."
        "Her hips roll in stuttering circles, her soaked, convulsing walls drawing every last second out of it."
        scene ch2ep2_1499
        with dissolve
        "You catch her as she slumps forward. Her back heaves with each ragged breath."
        mc "Breathe for me."
        e "Hahh... hahh..."
        mc "There you go."
        "You're still inside her. Still rock hard. Her pussy is still twitching around you in weak, fluttering aftershocks."
        scene ch2ep2_1500
        with dissolve
        "She gives you a knowing look over her shoulder, not to leave any job undone."
        e "Your turn."
        scene ch2ep2_1501
        with dissolve
        "She lifts off you. You pulse against the open air, slick and aching, and the loss of her warmth hits like a punishment."
        "But she doesn't go far."
        "She pauses. Looks back at you with something softer than lust."
        e "Not inside tonight. I want to give Leah a little more of me before we give her a sibling."
        "No guilt. No apology. Just a woman who knows what she wants and when she wants it."
        scene ch2ep2_1502
        with dissolve
        e "... Not \"yet\"."
        mc "Yet. Noted."
        e "Don't say it like you're filing a report."
        mc "Too late. It's on record."
        scene ch2ep2_1503
        with dissolve
        "She slides off the bed and drops to her knees between yours. Her hand wraps around your slick, pulsing shaft—still coated in her—and she looks up at you."
        e "Happy birthday, [mc]."
        show emma31
        with dissolve
        "Her lips close around your already leaking cock as she starts sucking you in."
        "Her tongue drags along the underside. She tastes herself on you and doesn't flinch. Her cheeks hollow. Her eyes stay locked on yours."
        mc "Em— fuck—"
        "She pulls back to the tip, swirls her tongue, then takes you deep again."
        "Your thighs tense. Your fingers tighten in her hair. She feels it and picks up the pace, her palm working the base of your shaft while her mouth handles the rest."
        "She can feel you swelling against her tongue, pulsing in her grip."
        e "Mm-hm."
        "That hum vibrates through your entire being and your vision whites out."
        scene ch2ep2_1504
        with hpunch
        mc "Emma!"
        "You unleash your load in her mouth, hips bucking forward."
        "Emma takes it, swallowing around you, throat working in steady pulses while her hand squeezes the last of it out of you."
        "Your head falls back. Your breath comes out wrecked."
        scene ch2ep2_1505
        with dissolve
        "She pulls off with a soft, wet pop, then wipes the corner of her mouth with her thumb."
        "She looks up at you with a devilish expression that belongs in a jail cell."
        mc "Shit..."
        mc "That was one hell of a gift."
        mc "Where did you learn that?"
        e "Practice..."
        mc "With what?"
        e "... Klara's veggies."
        mc "What the—"
        e "Just say thank you."
        mc "... Thank you."
        e "You're welcome."
        scene ch2ep2_1506
        with dissolve
        "The room settles. Your breathing evens out, in sync with hers."
        "Somewhere downstairs, a timer goes off. The turkey."
        e "... That's twenty minutes."
        mc "Yeah. Give or take."
        scene ch2ep2_1507
        with dissolve
        "She looks at the cuffs on the floor, then at her wrists."
        e "I'm keeping those."
        mc "They're department property."
        e "I'm unemployed. What are they going to do, fire me?"
        scene ch2ep2_1508
        with dissolve
        "You laugh. She leans against your shoulder, and for a second, neither of you moves."
        "Downstairs, Aine shouts something about plates. Sky yells something back. Klara's voice cuts through both of them."
        "And in the middle of all that noise, a ten-year-old girl is probably sitting at the table with a stuffed penguin named Mr. Penguin, waiting for the two of you to come back down."
        mc "We should go."
        e "Yeah."
        e "..."
        e "Five more seconds."
        "She counts them in her head."
        scene ch2ep2_1509
        with dissolve
        "Somewhere around three, her soft lips find your cheek. It's the kind of kiss that has nothing to prove."
        e "Okay."
        mc "Okay."
        stop music fadeout 20
        scene ch2ep2_1510
        with dissolve
        "She finds her clothes on the floor and puts herself back together."
        "You stare at her, trying to remembering the things you went through to get here, the things you said, the things you did."
        "{s}But nothing is coming to you.{/s} Everything comes back like it's yesterday."
        scene ch2ep2_1511
        with dissolve
        e "How do I look?"
        mc "*chuckles* Like you just committed a felony."
        e "Perfect..."
        play sound opendoor2
        scene ch2ep2_1512
        with dissolve
        "She unlocks the door. The hallway is empty."
        scene ch2ep2_1513
        with dissolve
        e "[mc]."
        mc "Hm?"
        e "I love you."
        mc "I love you too, Em. As always."
        e "Then don't just sit there. Come on. Let's go clean ourselves first."
        mc "I'll be right with you."
        scene ch2ep2_1514
        with dissolve
        "She walks out. You look at the handcuffs on the floor. Then at the drawing on the desk."
        mc "Phew! Hell of a birthday."
        stop music fadeout 2
        $ renpy.end_replay()

        scene black
        with dissolve
        with fade

        play music 'audio/OhHolyNight.mp3' fadein 2
    else:
        scene black
        with dissolve
        with fade

    scene ch2ep2_1397
    with Dissolve(2.0)
    pause
    scene ch2ep2_1398
    with Dissolve(2.0)
    pause
    scene ch2ep2_1399
    with Dissolve(2.0)
    pause
    scene ch2ep2_1400
    with Dissolve(2.0)
    pause
    scene ch2ep2_1401
    with Dissolve(2.0)
    pause
    scene ch2ep2_1402
    with Dissolve(2.0)
    pause
    scene ch2ep2_1403
    with Dissolve(2.0)
    pause
    scene ch2ep2_1404
    with Dissolve(2.0)
    pause
    scene ch2ep2_1405
    with Dissolve(2.0)
    pause
    scene black
    with dissolve
    scene ch2ep2_1406
    with Dissolve(2.0)
    pause
    scene ch2ep2_1407
    with Dissolve(2.0)
    pause
    scene ch2ep2_1408
    with Dissolve(2.0)
    pause
    scene black
    with dissolve
    scene ch2ep2_1409
    with Dissolve(2.0)
    pause
    scene ch2ep2_1410
    with Dissolve(2.0)
    pause
    scene ch2ep2_1411
    with Dissolve(2.0)
    pause
    scene ch2ep2_1412
    with Dissolve(2.0)
    pause
    scene ch2ep2_1413
    with Dissolve(2.0)
    pause
    scene black
    with dissolve
    scene ch2ep2_1414
    with Dissolve(2.0)
    pause
    scene ch2ep2_1415
    with Dissolve(2.0)
    pause
    scene black
    with dissolve
    scene ch2ep2_1416
    with Dissolve(2.0)
    pause

    scene black
    with dissolve
    with fadeq

    scene ch2ep2_1417
    with Dissolve(2.0)
    pause
    scene ch2ep2_1418
    with Dissolve(2.0)
    pause
    scene black
    with dissolve
    scene ch2ep2_1419
    with Dissolve(2.0)
    pause
    scene ch2ep2_1420
    with Dissolve(2.0)
    pause
    scene ch2ep2_1421
    with Dissolve(2.0)
    pause
    scene black
    with dissolve
    scene ch2ep2_1422
    with Dissolve(2.0)
    pause
    scene ch2ep2_1423
    with Dissolve(2.0)
    pause
    scene ch2ep2_1424
    with Dissolve(2.0)
    pause
    scene ch2ep2_1425
    with Dissolve(5.0)
    pause
    stop music fadeout 2

    scene black
    with dissolve
    with fade
    
    play sound nightambience2 loop fadein 2
    play sound2 cloth
    scene ch2ep2_1426
    with dissolve
    e "Careful with her head."
    mc "I've done this before, Em."
    e "I know. I'm just..."
    mc "Being a mom."
    e "..."
    play sound2 cloth
    scene ch2ep2_1427
    with dissolve
    e "Thanks, [mc]."
    mc "Don't worry about it."
    if emmaroute:
        scene ch2ep2_1428
        with dissolve
        mc "You know, if you ever need help with her. Anything at all."
        mc "You know who to come to first."
        e "Klara?"
        mc "... Yeah. Klara."
        e "But we both know it's going to be you."
        mc "Probably."
        e "Definitely."
        mc "Get some sleep, Em."
        e "In a bit. I'm going to sit with her for a while."
        mc "..."
        mc "Yeah. I figured."
    e "Goodnight, [mc]."
    mc "Goodnight, Emma."
    scene ch2ep2_1429
    with dissolve
    e "Wait, [mc]."
    scene ch2ep2_1430
    with dissolve
    mc "Yeah?"
    e "..."
    e "Really, thank you. For everything."
    mc "..."
    scene ch2ep2_1431
    with dissolve
    e "Not just tonight. All of it."
    e "The club. The hospital. June's porch at four in the morning."
    e "The floor."
    mc "..."
    e "I wouldn't be here without you."
    mc "You would've gotten here without me, Em."
    e "Maybe..."
    e "But you were the one who stayed with me."
    mc "... I try."
    scene ch2ep2_1432
    with dissolve
    pause
    scene ch2ep2_1433
    with dissolve
    pause
    scene ch2ep2_1434
    with dissolve
    mc "Goodnight, mom."
    play sound2 closedoor2
    scene ch2ep2_1435
    with dissolve
    pause
    scene ch2ep2_1436
    with dissolve
    pause
    play sound2 cloth
    scene ch2ep2_1437
    with Dissolve(1.0)
    pause
    scene ch2ep2_1438
    with dissolve
    pause
    scene ch2ep2_1439
    with Dissolve(2.0)
    pause
    scene ch2ep2_1440
    with dissolve
    pause
    play sound2 papermovement
    scene ch2ep2_1441
    with dissolve
    pause
    play sound3 papermovement2
    scene ch2ep2_1442
    with dissolve
    pause
    scene ch2ep2_1443
    with dissolve
    $ renpy.music.set_volume(1.0, 0.0)
    play music 'audio/FoldedLetter.mp3'
    d "(Dear Emy...)"
    d "(I used to think the hardest part of being a mother was learning how to hold you.)"
    d "(But I was wrong.)"
    stop sound fadeout 2
    scene ch2ep2_1444
    with Dissolve(1.0)
    d "(By the time you read this, I won't be there to guide you.)"
    d "(I won't be there to steady your hands when they shake.)"
    d "(I won't be there to tell you if you're doing the right thing.)"
    d "(And I know that scares you.)"
    d "(You've always been brave, Emy.)"
    d "(But bravery doesn't mean you don't feel afraid.)"
    d "(It means you choose to stay, even when fear is louder than your confidence.)"
    d "(There will come a time when the world asks you to choose.)"
    d "(Between what is right, and what is safe.)"
    d "(Between what you're told to do, and what your heart refuses to abandon.)"
    d "(And when that moment comes, you'll worry that choosing one means losing the other.)"
    scene ch2ep2_1445
    with Dissolve(1.0)
    d "(But listen to me, sweetheart.)"
    d "(Being a mother is not about having the answers.)"
    d "(It's about staying when walking away would hurt less.)"
    d "(You don't become a mother by being perfect.)"
    d "(You become one by loving imperfectly, and choosing to keep loving anyway.)"
    d "(You will sacrifice things.)"
    d "(Sometimes, things you worked your whole life to protect.)"
    d "(And you will wonder if it was worth it.)"
    d "(It was.)"
    d "(Because one day, someone will look at you the way you once looked at me.)"
    d "(And you'll realize it was never because you took care of them.)"
    d "(It was because you stayed.)"
    d "(And if you ever doubt yourself, if you ever feel lost under a sky that feels too big and too quiet, remember this.)"
    scene ch2ep2_1446
    with Dissolve(2.0)
    d "(A mother doesn't always have the words—)" with Dissolve(1.0)
    d "(so she wraps her daughter in a blanket of stars,)" with Dissolve(1.0)
    d "(and lets the sky say I love you.)" with Dissolve(3.0)
    play sound nightambience2 fadein 2 loop
    scene ch2ep2_1447
    with Dissolve(1.0)
    pause
    scene ch2ep2_1448
    with Dissolve(1.0)
    pause
    scene ch2ep2_1449
    with Dissolve(1.0)
    pause
    play sound2 papermovement2
    scene ch2ep2_1450
    with Dissolve(1.0)
    pause
    stop sound fadeout 2
    play sound2 chime_bell
    scene ch2ep2_1451
    with Dissolve(2.0)
    pause
    scene ch2ep2_1452
    with Dissolve(2.0)
    pause
    scene ch2ep2_1453
    with Dissolve(4.0)
    pause
    play sound nightambience2 loop fadein 2 
    scene ch2ep2_1454
    with Dissolve(1.0)
    pause
    play sound2 chair
    scene ch2ep2_1455
    with Dissolve(0.2)
    pause
    play sound3 cloth
    scene ch2ep2_1456
    with Dissolve(3.0)
    pause
    scene ch2ep2_1457
    with Dissolve(3.0)
    pause
    call hide_days
    with dissolve
    stop music fadeout 2
    stop sound fadeout 2

    scene black
    with Dissolve(3.0)
    show ch2ep2end
    with Dissolve(1.0)
    pause 169
    scene black
    pause

    stop music fadeout 2

    play sound ceilingfan_low fadein 2 loop
    play sound2 closedoor2
    scene ch2ep2_1249
    with dissolve
    mc "..."
    mc "Damn it... Last week...?"
    play sound2 dialtone loop
    scene ch2ep2_1250
    with dissolve
    pause
    play sound2 phoneclick
    scene ch2ep2_1251
    with dissolve
    lev "This is Dr. Levenhart."
    mc "Doc. It's me."
    lev "..."
    lev "Well. This is a surprise."
    play sound2 chair
    scene ch2ep2_1252
    with dissolve
    mc "Yeah, I know. I owe you an apology. Again..."
    mc "Last week completely slipped my mind. Things got... hectic."
    lev "Hectic?"
    scene ch2ep2_1253
    with dissolve
    if emmaroute:
        mc "Long story. Girlfriend of mine went through something."
    else:
        mc "Long story. A friend of mine went through something."
    mc "By the time I looked at my calendar, your appointment was a week gone."
    lev "I see."
    mc "I should've called sooner, doc. I'm really sorry."
    lev "You're calling now. That's more than I expected, frankly."
    mc "..."
    lev "How are you feeling?"
    mc "Good, actually. Really good."
    mc "Honestly, doc... I think it's run its course."
    lev "..."
    mc "I'm sleeping fine. Working fine. My thoughts seem to be on the right track. Whatever it was, I think my body sorted it out."
    lev "Mm..."
    mc "You don't sound convinced."
    lev "I'm listening. That's my job."
    lev "... Well, I'm glad you're feeling better. Genuinely. But if anything changes, call me. Not a week later. Call me right away."
    mc "Yeah. I will."
    lev "Take care of yourself, [mc]."
    mc "Thanks, doc."
    play sound2 phoneclick
    scene ch2ep2_1254
    with dissolve
    pause
    play sound2 casepickup2
    scene ch2ep2_1255
    with Dissolve(0.2)
    pause
    play sound2 chair2
    scene ch2ep2_1256
    with dissolve
    mc "*exhales*"
    stop sound fadeout 2
    play sound2 footstep_e1
    pause 0.2
    scene ch2ep2_1257
    with Dissolve(2.0)
    pause
    play sound2 footstep_e2
    scene ch2ep2_1258
    with Dissolve(1.0)
    pause
    play sound2 footstep_e3
    scene ch2ep2_1259
    with Dissolve(1.0)
    pause
    play sound2 footstep_e4
    scene ch2ep2_1260
    with Dissolve(1.0)
    transform mc_e_zoom_center:
        subpixel True
        align (.5, .1)
        zoom 1.0
        ease 5.0 zoom 1.02
    play sound ghost_riser
    scene ch2ep2_1260 at mc_e_zoom_center
    $ renpy.pause(4.0, hard=True)
    scene ch2ep2_1261
    if (emmaroute and emmapoint == 9):
        eee "I counted three. You counted none."
    else:
        eee "I counted two. You counted none."
    play sound ghostlybreath
    scene black
    pause 0.4
    play music 'audio/Unwanted.mp3'
    pause
    scene continued
    with Dissolve(5.0)
    pause
    stop music fadeout 2
    scene black
    with Dissolve(3.0)
    pause

    


    return
label ch2ep1:
    $ renpy.music.set_volume(0.0, 0.0)
    play music wallclock_rev fadein 3
    play sound wallclock fadein 3 loop
    scene ch2ep1_1
    with Dissolve(2.0)
    lev "Most people give the books or the couch a once-over. But you... you went straight for the busted clock."
    mc "Just wanted to see if it still ticks."
    lev "Some folks take it apart to figure out how it works. Others... they're scared of what might happen if it ever starts ticking again."
    scene black
    with Dissolve(0.2)
    scene ch2ep1_2
    with Dissolve(0.2)
    pause
    scene black
    with dissolve
    scene ch2ep1_3
    with dissolve
    mc "Lately... it feels like my head's a TV stuck between channels."
    mc "I'm going through the motions, but it's all just static. Nothing clicks. Nothing fits."
    lev "Static is {i}still{/i} a signal. Means something's in there—still trying to break through."
    scene black
    with Dissolve(0.2)
    scene ch2ep1_4
    with Dissolve(0.2)
    pause
    scene black
    with dissolve
    scene ch2ep1_5
    with dissolve
    lev "Okay. No need to dig. We'll just circle the hole a bit. Glance in every now and then. No shovels."
    scene ch2ep1_6
    with Dissolve(1.0)
    yt "I'd... rather not."
    scene ch2ep1_7
    with Dissolve(1.0)
    yt "Some things... are better off..."
    scene black
    with Dissolve(1.0)
    yt "... staying buried..."
    $ renpy.music.set_volume(1.0, 2.0)
    $ renpy.sound.set_volume(0.0, 2.0)
    scene ch2ep1_8
    with Dissolve(2.0)
    pause
    mc "This... This room again..."
    play sound2 chime_bell
    scene ch2ep1_9
    with Dissolve(0.1)
    pause
    scene black
    with dissolve
    scene ch2ep1_10
    with dissolve
    pause
    scene black
    with dissolve
    scene ch2ep1_11
    with dissolve
    pause
    scene black
    with dissolve
    scene ch2ep1_12
    with dissolve
    pause
    scene black
    with dissolve
    scene ch2ep1_13
    with dissolve
    pause
    scene black
    with Dissolve(1.0)
    scene ch2ep1_14
    with Dissolve(2.0)
    pause
    stop sound
    stop music fadeout 3
    $ renpy.music.set_volume(1.0, 2.0)
    $ renpy.sound.set_volume(1.0, 0.0)
    scene black
    with Dissolve(3.0)
    pause
    un "{size=-10}[mc]."
    lev "[mc]."
    play music 'audio/Meme.mp3'
    play sound gasp_male
    show keidreamwake
    pause 0.5
    scene black
    pause 2.0
    scene ch2ep1_15
    with dissolve
    lev "You with me?"
    scene ch2ep1_16
    with dissolve
    mc "..."
    lev "You alright there, [mc]?"
    play sound cloth
    scene ch2ep1_17
    with dissolve
    
    $ reset_phone_data()
    $ phone_start()
    $ switch_channel_view("aine_dm")
    show screen phone_ui
    $ quick_menu = False
    $ hide_all_phone_channels("aine_dm")
    $ lock_phone_screen()
    $ phone_stamp_rel("aine_dm")
    $ send_phone_message("Aine", "About that...", "aine_dm", do_pause=False)
    $ phone_pause(2.0)
    $ send_phone_message("Aine", "Sorry, we're not home right now. Sky and I are tied up in a work meeting.", "aine_dm")
    $ phone_pause(2.5)
    $ send_phone_message("Aine", "But like... what else is she supposed to be doing? Honestly, I doubt anything's changed.", "aine_dm")
    $ phone_pause(2.0)
    $ send_phone_message("Aine", "It's been—what, how long now? A year? And she's still locked up in her room...", "aine_dm")
    $ phone_pause(2.0)
    $ send_phone_message("Aine", "And hey, again, I'm really sorry. I shouldn't have brought it up back then.", "aine_dm")
    $ present_phone_choices([("Yeah", "Yeah.", Jump("notjustifyaine")), ("Let's stop pointing fingers", "Aine... how long are you gonna keep beating yourself up over this?", Jump("justifyaine"))], "aine_dm")
    label notjustifyaine:
    $ lock_phone_screen()
    pause
    $ send_phone_message(phone_config["phone_player_name"], "To be fair, none of us saw it coming. Not even me.", "aine_dm")
    $ send_phone_message(phone_config["phone_player_name"], "You were trying to help. That's more than most would've done. So let's not dwell on it, alright?", "aine_dm")
    $ phone_pause(1.0)
    $ send_phone_message("Aine", "Alright.", "aine_dm")
    jump ch2ep1cont
    label justifyaine:
    $ lock_phone_screen()
    pause
    $ send_phone_message(phone_config["phone_player_name"], "You saw she was down, and you tried to be there for her. That's not a mistake.", "aine_dm")
    $ send_phone_message(phone_config["phone_player_name"], "None of us could've predicted how she'd react. I certainly didn't.", "aine_dm")
    $ send_phone_message(phone_config["phone_player_name"], "You meant well, and did more than most people would've even tried. So let's stop pointing fingers, yeah?", "aine_dm")
    $ phone_pause(0.5)
    $ send_phone_message("Aine", "😭", "aine_dm")
    $ phone_pause(1.0)
    $ send_phone_message("Aine", "Okay.", "aine_dm")
    jump ch2ep1cont
    label ch2ep1cont:
    if (aineroute and ainepoint == 17):
        $ present_phone_choices([("I miss you", "I miss you.", Jump("ainephonesextrue")), ("Give me something", "Come on... give me something.", Jump("ainephonesexfalse"))], "aine_dm")
        label ainephonesextrue:
        $ lock_phone_screen()
        $ ainephonesex = True
        pause
        $ phone_pause(1.5)
        $ send_phone_message("Aine", "Pfft! It's only been a few hours, [mc]. Cool that {i}thing{/i} down.", "aine_dm")
        $ send_phone_message("Aine", "images/ch2ep1_18.jpg", "aine_dm", 2)
        $ phone_pause(1.0)
        $ send_phone_message("Aine", "You're lucky I'm in the bathroom. Sky thinks I'm neck-deep in spreadsheets.", "aine_dm")
        $ send_phone_message(phone_config["phone_player_name"], "Hot damn! That just made my whole day!", "aine_dm")
        $ phone_pause(2.0)
        $ send_phone_message("Aine", "Haha! You sap. Like we haven't been pulling this stunt for almost six months now.", "aine_dm")
        $ send_phone_message(phone_config["phone_player_name"], "Hey, even tradition's gotta keep up with the times.", "aine_dm")
        $ phone_pause(1.0)
        $ send_phone_message("Aine", "Alright, alright, you big ol' cheese ball.", "aine_dm")
        $ send_phone_message(phone_config["phone_player_name"], "Now all I can think about is burying my face between those gorgeous curves... teasing every inch with my tongue while my fingers trace over your pebbled peaks...", "aine_dm")
        $ send_phone_message(phone_config["phone_player_name"], "... trailing kisses down to your ribs, your stomach, your hips... lower, and lower, until...", "aine_dm")
        $ phone_pause(0.3)
        $ send_phone_message("Aine", "...", "aine_dm")
        $ send_phone_message(phone_config["phone_player_name"], "You're redder than a rose again, aren't you?", "aine_dm")
        $ phone_pause(0.5)
        $ send_phone_message("Aine", "I hate you...", "aine_dm")
        $ phone_pause(0.8)
        $ send_phone_message("Aine", "I love you. Come home safe.", "aine_dm")
        $ send_phone_message(phone_config["phone_player_name"], "Oh, I'll definitely be {i}coming{/i} when I get there...", "aine_dm")
        $ phone_pause(2.0)
        $ unlock_phone_screen()
        show screen phone_blocker
        show screen phone_close_button
        $ send_phone_message("Aine", "... Remind me why I agreed to marry you again?", "aine_dm")
        jump ch2ep1cont2
        label ainephonesexfalse:
        $ lock_phone_screen()
        $ ainephonesex = False
        pause
        $ send_phone_message("Aine", "Pfft! It's only been a few hours, [mc]. You seriously can't survive a single day without me?", "aine_dm")
        $ send_phone_message("Aine", "images/ch2ep1_19.jpg", "aine_dm", 2)
        $ send_phone_message("Aine", "You're lucky I'm in the bathroom. Sky thinks I'm neck-deep in spreadsheets.", "aine_dm")
        $ send_phone_message(phone_config["phone_player_name"], "And yet, somehow, your radiant smile never ceases to make my whole damn day.", "aine_dm")
        $ unlock_phone_screen()
        show screen phone_blocker
        show screen phone_close_button
        $ send_phone_message("Aine", "Alright, alright... you big softie.", "aine_dm")
        jump ch2ep1cont2
    else:
        $ unlock_phone_screen()
        show screen phone_blocker
        show screen phone_close_button
        pause
    label ch2ep1cont2:
    play sound cloth
    scene ch2ep1_20
    with dissolve
    lev "[mc]? We're not done yet."
    mc "Sorry, I need to head home."
    play sound closedoor2
    scene ch2ep1_21
    with dissolve
    pause
    scene ch2ep1_22
    with dissolve
    pause
    scene ch2ep1_23
    with Dissolve(2.0)
    pause

    scene black
    with dissolve
    with fadeq

    $ renpy.music.set_volume(0.5, 1.0)
    play sound3 weather_advisory
    show keidrive
    with dissolve
    pause 19.0

    stop sound3 fadeout 4
    scene black
    with dissolve
    with fade

    $ renpy.music.set_volume(1.0, 1.0)
    show screen day_thursday with dissolve
    $ phone_time_add(minutes=36)
    play sound cityalley fadein 2 loop
    play sound2 cardoorclose
    scene ch2ep1_24
    with dissolve
    $ show_all_phone_channels()
    show screen phone_launcher
    pause
    stop music fadeout 10
    scene ch2ep1_25
    with dissolve
    pause
    scene ch2ep1_26
    with dissolve
    pause
    scene ch2ep1_27
    with dissolve
    pause
    scene ch2ep1_28
    with dissolve
    mc "Yo. Where's your van?"
    shu "It's... not here."
    mc "Yeah, I figured that out on my own. Thought I'd ask before calling the cops."
    shu "Relax, man. It's in the shop."
    play sound2 chairdrag
    scene ch2ep1_29
    with dissolve
    mc "Since when do you put your van in a shop? You usually duct tape it until it stops wheezing."
    shu "Yeah, well... this time she gave out for real. Figured I'd let the pros take a swing."
    mc "Did you sell it?"
    play sound2 woosh
    scene ch2ep1_30
    shu "What? Pfff, no! I love that van. It's got history. Memories. Smells."
    mc "Exactly why I thought you finally snapped and sold it for scrap."
    play sound2 chairdrag
    scene ch2ep1_31
    with Dissolve(0.2)
    shu "Don't insult her like that. She's not junk—she's... vintage."
    mc "Vintage usually runs. Yours just... sat there like a retired war vet on life support."
    shu "She's getting her spine realigned, okay? Suspension work. Maybe a paint job."
    scene ch2ep1_32
    with dissolve
    mc "A paint job? Since when do you care about how she looks?"
    shu "Since I figured that if she's gonna die on the road, she might as well go out looking sharp."
    mc "So you sold her?"
    shu "Yeah, I sold her. Gonna get myself a new ride, baby. Something that doesn't sound like a dying goat when it turns left."
    play sound2 chair3
    scene ch2ep1_33
    with dissolve
    mc "*exhales*"
    mc "Alright, spill. What the hell's been going on with you this past year?"
    shu "What do you mean? We've always been around each other, haven't we?"
    shu "Like Bonnie and Clyde, with all the police chases and deadly shootouts. You screaming like a damsel in distress and me always there to save the day."
    mc "Clearly the exhaust from that old beater has gotten to your brain."
    shu "Yet another reason why I cashed out on her while I still could. In any case, why do you ask?"
    scene ch2ep1_34
    with Dissolve(0.2)
    mc "This one's for the folks clicking through our lives like it's some kind of visual novel. You know... the ones dying to know where you disappeared to."
    shu "... Right. Them."
    play sound2 woosh
    scene ch2ep1_35
    shu "Okay, picture this..."
    stop sound fadeout 2
    play music 'audio/SpiritOfTheWest.mp3'
    scene ch2ep1_36
    with Dissolve(1.0)
    shu "High noon. Middle of nowhere, sun hotter than sin, and I'm in a standoff with some cowboy who looks like he chews barbed wire for breakfast."
    mc "*chuckles* Of course you are."
    scene ch2ep1_37
    with Dissolve(0.2)
    shu "I'm holding the line. There's a girl behind me, shaking like a leaf, yet there's not a scratch on her."
    shu "The guy I'm facing? He's got a six-shooter and an ego the size of Quinara."
    $ renpy.music.set_volume(0.5, 1.0)
    play sound cityalley loop
    scene ch2ep1_38
    with Dissolve(0.2)
    mc "What'd you have?"
    scene ch2ep1_39
    with dissolve
    shu "..."
    scene ch2ep1_40
    with dissolve
    shu "A wrench."
    mc "A wrench?"
    play sound2 metalhit
    scene ch2ep1_41
    shu "Yup. Still made him miss. Dodged the shot, swung the wrench, clocked him so hard he whirlybirded like a fidget spinner."
    mc "... That's not how physics works."
    scene ch2ep1_42
    with Dissolve(0.2)
    shu "Whatever, man..."
    play sound2 woosh
    scene ch2ep1_43
    shu "Anyway, her whole crew came crawling out of hiding after that. Found out I saved a whole caravan of runaway girls."
    shu "They called me their {i}\"guardian angel\"{/i} or some crap like that."
    mc "Let me guess, you rode off into the sunset?"
    play sound2 woosh
    scene ch2ep1_44
    shu "Nah. Sunset rode off into me."
    play sound3 cardooropen
    scene ch2ep1_45
    with dissolve
    ju "I better not be part of whatever delusional bullshit that conversation was."
    play sound2 cardriveaway
    scene ch2ep1_46
    with dissolve
    pause
    scene ch2ep1_47
    with Dissolve(0.2)
    mc "Was she there?"
    shu "She, in fact, was."
    stop music fadeout 5
    $ renpy.music.set_volume(1.0, 5.0)
    play sound2 chair3
    scene ch2ep1_48
    with dissolve
    shu "But enough about my escapades..."
    shu "What about you?"
    scene ch2ep1_49
    with dissolve
    mc "Well? I'm now the regional manager of Best Burger. Started running a charity. Also a member of Sicae Agency. And Klara's depressed."
    scene ch2ep1_50
    shu "GREAT!"
    mc "But you already knew that. This whole conversation's stupid."
    shu "Then hit me with something I don't know."
    scene ch2ep1_51
    with dissolve
    mc "I've been dreaming."
    shu "About what?"
    mc "I'm just in this room. All white. Just... nothing."
    shu "That's awesome!"
    scene ch2ep1_52
    with dissolve
    mc "That's your takeaway?"
    shu "Yup. Sounds peaceful. Or like purgatory. Or IKEA."
    mc "There's no furniture."
    shu "Definitely IKEA."
    scene ch2ep1_53
    with dissolve
    mc "..."
    mc "Anyone home?"
    shu "... Not that I know of. Well, aside from {i}someone{/i}."
    play sound2 cloth
    scene ch2ep1_54
    with dissolve
    mc "You eaten yet?"
    shu "Nope, not yet. You cooking for me?"
    play sound3 camcorder_fastforward loop
    show shucamcorder
    with Dissolve(0.2)
    pause 6.0
    play sound3 camcorder_movement
    scene ch2ep1_55
    with Dissolve(0.2)
    mc "Solid performance."
    mc "Alright, let's head in."
    stop sound fadeout 2
    
    scene black
    with dissolve
    with fade

    $ phone_time_add(hours=1)
    scene ch2ep1_56
    with dissolve
    mc "You gonna be alright on your own?"
    shu "Yeah, yeah, don't sweat it. I'm good."
    shu "Gotta wrap my head around this so-called \"state-of-the-art\" business management stuff anyway."
    mc "Alright then. Knock yourself out."
    play sound voices_klara_world loop
    scene ch2ep1_57a
    with dissolve
    kmother "{sc}{font=Beowolf.ttf}Your sister never stumbled like this. At least she made something of herself."
    kfather "{sc}{font=Beowolf.ttf}Leaving the clan?"
    kfather "{sc}{font=Beowolf.ttf}After everything we carved into you, you're just spitting it back in our faces?"
    stop sound
    scene ch2ep1_57
    pause
    play music 'audio/CleanHeaven.mp3'
    scene black
    with dissolve
    scene ch2ep1_58
    with dissolve
    k "{i}Some rooms swallow sound like it's something sacred."
    k "{i}You step through the door, and the air forgets how to breathe."
    scene ch2ep1_59
    with dissolve
    k "{i}The coffee cools in the same untouched spot."
    scene ch2ep1_60
    with dissolve
    k "{i}The window blinks at the same tired hour."
    scene ch2ep1_61
    with dissolve
    k "{i}Dust moves around like it's minding its manners."
    scene ch2ep1_62
    with dissolve
    k "{i}I count things, sometimes. Seconds, moments that don't ask for much."
    k "{i}The silence between footsteps."
    k "{i}The hush between thoughts that try too hard to matter."
    scene ch2ep1_63
    with dissolve
    k "{i}I'm not stuck. I just never chose which way to fall."
    k "{i}And falling... falling's a commitment."
    k "{i}So I stay. In the quiet. In the in-between."
    k "{i}Where memories are insignificant."
    k "{i}Where the floor doesn't creak unless I let it."
    k "{i}Where nothing ever grows loud enough to wake me."
    k "{i}And that passes for peace."
    scene ch2ep1_64
    with Dissolve(0.1)
    pause
    scene ch2ep1_65
    with dissolve
    k "{i}*exhales*"
    k "{i}... Or maybe I'm only redecorating the cage."
    scene ch2ep1_66
    with dissolve
    k "{i}Every day, I catch myself waiting—hoping—for someone to play that piano again."
    k "{i}God... I miss the sound of it..."
    play sound opendoor2
    scene ch2ep1_67
    with dissolve
    pause
    play sound2 closedoor2
    scene ch2ep1_68
    with dissolve
    pause
    scene ch2ep1_69
    with Dissolve(0.1)
    pause
    scene ch2ep1_70
    with dissolve
    k "{i}But it's never music that finds me. It's footsteps. Steam. An aroma that doesn't belong to dust and decay."
    k "{i}I know that smell like an old promise..."
    k "{i}A boy—no, a man—who says my name without flinching."
    k "{i}It's almost cruel, the way his warmth walks in like it owns the place."
    k "{i}Cruel... and curiously kind."
    scene ch2ep1_71
    with dissolve
    pause
    scene ch2ep1_72
    with Dissolve(0.1)
    pause
    scene ch2ep1_73
    with dissolve
    k "{i}Day three-hundred eighty-three of keeping myself locked away in this room."
    mc "Has that clock always been busted?"
    k "It's been dead since the day we moved in."
    k "I even swapped the battery once... still nothing."
    mc "Huh... that's weird, 'cause I just—"
    k "Hm?"
    scene ch2ep1_74
    with dissolve
    mc "Never mind, doesn't matter."
    k "{i}Breakfast, lunch, even dinner, he leaves everyone else behind and comes here."
    k "{i}Same time, every day. Like it's wired into him... or some kind of routine."
    play sound chair3
    scene ch2ep1_75
    with dissolve
    mc "Want me to take a look at it?"
    k "No, it's fine. The ticking just makes my ears ring anyway."
    mc "You need some sunshine, Klara."
    k "{i}He's always been calling me by name, but lately... his tone's a bit different..."
    k "{i}A sign he's growing up? Or maybe... just growing tired of me?"
    k "I mean... the sun does reach my window, so technically..."
    mc "I meant {i}outside{/i}, lady."
    k "Just pulling your leg."
    play sound platedown
    scene ch2ep1_76
    with dissolve
    k "Thanks, [mc]."
    mc "Day—I already lost count—of trying to get you to step outside."
    k "Three-hundred eighty-three."
    mc "*chuckles* So you've been keeping score. Not bad."
    scene ch2ep1_77
    with dissolve
    k "{i}He grabs his own plate..."
    play sound chair3
    scene ch2ep1_78
    with dissolve
    k "{i}... sits down across from me."
    play sound2 cloth
    scene ch2ep1_79
    with dissolve
    mc "..."
    k "{i}... and says nothing."
    scene ch2ep1_80
    with Dissolve(0.1)
    pause
    scene black
    with dissolve
    k "{i}I know I've disappointed him... but he's never once raised his voice."
    scene ch2ep1_81
    with dissolve
    pause
    play sound3 cloth
    scene ch2ep1_82
    with dissolve
    pause
    scene black
    with dissolve
    play sound chairfall
    scene ch2ep1_83
    pause
    play sound2 tablehit
    scene ch2ep1_84
    with hpunch
    pause
    scene ch2ep1_85
    with dissolve
    k "Dont. Ever. Say that name again..."
    a "I'm sorry, I didn't mean to—"
    scene ch2ep1_86
    with Dissolve(0.2)
    pause
    scene ch2ep1_87
    with dissolve
    pause
    scene ch2ep1_88
    with Dissolve(0.1)
    pause
    scene black
    with dissolve
    play sound2 exhale_female
    pause
    play sound camcorder_fastforward loop
    show klaracamcorder
    with dissolve
    pause 14.0
    play sound camcorder_movement
    scene ch2ep1_89
    with dissolve
    mc "Still not a fan of being on camera, huh?"
    k "You know why. That hasn't changed."
    play sound2 utensilsonplate
    scene ch2ep1_90
    with dissolve
    k "{i}He gets up, takes my plate like always, and—"
    scene ch2ep1_91
    with dissolve
    mc "Anyway, I should get going."
    k "Got somewhere to be?"
    scene ch2ep1_92
    with dissolve
    mc "..."
    k "... Right. I forgot."
    scene ch2ep1_93
    with dissolve
    mc "Do you even know what day it is?"
    k "Monday."
    mc "It's Thursday."
    scene ch2ep1_94
    with dissolve
    k "If you've got things to do, you shouldn't waste your lunch breaks on me, [mc]."
    scene ch2ep1_95
    with dissolve
    mc "I'm not here for the food, Klara."
    scene ch2ep1_96
    with Dissolve(0.2)
    k "!"
    play sound closedoor2
    scene ch2ep1_97
    with dissolve
    pause 0.5
    k "{i}Didn't see that last part coming...{/i}"
    scene ch2ep1_98
    with Dissolve(0.1)
    pause

    scene black
    with dissolve
    with fadeq

    $ phone_time_add(minutes=20)
    scene ch2ep1_99
    with dissolve
    shu "How's she? How's the therapy going?"
    mc "What therapy?"
    shu "Oh, whatever..."
    scene ch2ep1_100
    with dissolve
    shu "Right! You invited everyone to your birthday yet? It's creeping up, man!"
    if naomiroute:
        mc "... There are a few I haven't reached out to. Doubt they'll say yes either way."
        mc "Still... I'll give it another shot."
        shu "Drama?"
        mc "Drama."
        scene ch2ep1_101
        with dissolve
        shu "Hey, not trying to poke around your personal baggage, but..."
        shu "The show must go on, right?"
        mc "*chuckles* Yeah. The show must go on."
    else:
        mc "There are a few I haven't talked to yet."
    scene ch2ep1_102
    with dissolve
    shu "You can leave those. I'll handle the rest once I'm done here."
    mc "One broken glass, one broken bone."
    shu "What do you take me for? I'm not some pampered prince."
    mc "Nah, you're worse."
    scene ch2ep1_103
    with dissolve
    if aoifelives:
        shu "Anyway, there are a couple chicks outside."
        mc "Who?"
        shu "Your wife and... someone I don't recognize."
        stop music fadeout 4
        play music2 'audio/SweetDreams.mp3' fadein 4
        play sound cityalley loop
        scene ch2ep1_104
        with dissolve
        pause
        scene ch2ep1_105
        with dissolve
        ao "Hm... Looks better than the roof we used to have back in the military... Good for you..."
        m "Can you not bring the military up every time?"
        play sound2 closedoor
        scene ch2ep1_106
        with dissolve
        pause
        scene ch2ep1_107
        with dissolve
        ao "I'll remember the address... just in case... Thanks for showing me around..."
        m "Do you even plan on coming back?"
        ao "That's not something I can answer... not even for myself..."
        m "Did you..."
        m "Why? She gave you a way out."
        scene ch2ep1_108
        with dissolve
        ao "We're all chained to something, Moon..." 
        ao "Without this... I'd just spend every waking second thinking of new ways to kill myself..."
        ao "So I'm staying with them... To atone. For good..."
        m "You're starting to sound like another Claire."
        play sound2 cloth
        scene ch2ep1_109
        with dissolve
        ao "Maybe that's just how it is for people like us... We survive, sure... But always in a cage..."
        scene ch2ep1_110
        with dissolve
        ao "The only difference is... you get to live on the other side of it..."
        m "..."
        scene ch2ep1_111
        with dissolve
        mc "Aoife."
        scene ch2ep1_112
        with dissolve
        ao "What is it..."
        scene ch2ep1_113
        with dissolve
        ao "... Tsukigami Kaito...?"
        mc "That's not my name."
        ao "[mc] it is, then..."
        scene ch2ep1_114
        with dissolve
        pause
        scene ch2ep1_115
        with dissolve
        pause 0.2
        scene ch2ep1_116
        with dissolve
        pause
        scene ch2ep1_117
        with dissolve
        ao "What's that for...?"
        mc "Never got the chance to thank you."
        stop sound fadeout 2
        scene ch2ep1_118
        with flash
        pause
        play sound2 gateclose
        scene ch2ep1_119
        with dissolve
        pause
        scene ch2ep1_120
        with dissolve
        mc "You! You told them where I—"
        ao "Save it... I wasn't their scout, and I didn't rat you out... I got the intel from them, not the other way around..."
        scene ch2ep1_121
        with dissolve
        mc "So you can speak."
        ao "And with that... I'll probably lie to someone else tomorrow..."
        mc "Let me out."
        scene ch2ep1_122
        with dissolve
        ao "I can't... And I don't have much time for this..."
        scene ch2ep1_123
        with dissolve
        ao "Tell me, are you really Number Three...?"
        mc "Apparently, yeah. That's me. Or so some crazy people call me."
        scene ch2ep1_124
        with dissolve
        ao "I don't see a thing from you..."
        ao "My eyes have been cursed to see the darkness in people..."
        ao "Every lie..."
        ao "Every fracture in their soul..."
        ao "But you... There's nothing..."
        ao "No darkness... Just... an empty expanse of white..."
        mc "That's..."
        scene ch2ep1_125
        with dissolve
        ao "So someone's told you that too..."
        mc "What the hell is that even supposed to mean?"
        scene ch2ep1_126
        with dissolve
        ao "I don't know... I've never met anyone like you..."
        ao "Maybe one day, you'll figure it out... and let me know..."
        scene ch2ep1_127
        with dissolve
        ao "Here... Eat..."
        mc "What's in it?"
        ao "Just ham, egg... and bread... Or do you want something fancy?"
        mc "..."
        scene ch2ep1_128
        with dissolve
        ao "If it's poisoned, you should probably thank me for sparing you a slow death..."
        mc "..."
        scene ch2ep1_129
        with dissolve
        ao "Eat... And make it quick..."

        scene black
        with dissolve
        with fadeq

        scene ch2ep1_130
        with dissolve
        ao "I'll see you on the other side..."
        mc "Wait!"
        scene ch2ep1_131
        with dissolve
        ao "What is it..."
        scene ch2ep1_132
        with dissolve
        ao "... Subject Number Three...?"
        mc "Tsk. Don't call me that."
        scene ch2ep1_133
        with dissolve
        ao "*laughs* Oh, would you look at that? You and her both have that satisfying little tongue click... I love it..."
        scene ch2ep1_134
        with dissolve
        mc "..."
        ao "Alright, fine... What is it...?"
        scene ch2ep1_135
        with dissolve
        mc "You're with them them, right? So why help me?"
        ao "Call it... curiosity..."
        mc "Seriously? Word is you've been offing your own friends without blinking. Mercy doesn't really suit you."
        scene ch2ep1_136
        with dissolve
        ao "..."
        scene ch2ep1_137
        with dissolve
        ao "\"Mercy\" is what I gave them... A release from the misery they could never escape..."
        mc "You're not some god. You don't get to make that call."
        scene ch2ep1_138
        with dissolve
        ao "Maybe not... but someone has to play god..."
        ao "*scoffs* If anything... you don't have a shred of ground to judge me... You've never felt a serum chewing through you like termites in the beams..."
        mc "Then... is she alive? You went after her, didn't you?"
        scene ch2ep1_139
        with dissolve
        ao "..."
        ao "She was always said to be the strongest among us..."
        ao "Terrible with guns, so she made up for it with blades..."
        ao "And even then, she became a monster on the field..."
        ao "Dozens of missions, same story every time. She came back, the others didn't."
        ao "... That became the foundation of what she is now."
        ao "A Sovereign..."
        ao "Probably the most dangerous one we've ever recorded..."
        mc "A... what? That's not what I asked."
        ao "She's likely on her way here, right now..."
        ao "And when she gets here... I'll be the one to end her suffering... once and for all..."
        ao "And maybe... mine too..."
        play sound cityalley fadein 2 loop
        scene ch2ep1_140
        with flash
        ao "..."
        play sound2 clench
        scene ch2ep1_141
        with dissolve
        pause
        scene ch2ep1_142
        with dissolve
        mc "Maybe one day, I'll be able to tell you what it means."
        ao "I'll save you a glass of whiskey..."
        stop music2 fadeout 4
        scene ch2ep1_143
        with dissolve
        pause
        scene ch2ep1_144
        with dissolve
        pause
        scene ch2ep1_145
        with dissolve
        pause
        image moointmcao:
            "ch2ep1_146.jpg"
            pause 0.1
            "ch2ep1_147.jpg"
            pause 0.1
            repeat
        play music 'audio/FindYourStyle.mp3'
        play sound2 woosh
        show moointmcao
        pause
        m "Private property. Hands off."
        ao "..."
        scene ch2ep1_148
        with Dissolve(0.2)
        hide moointmcao
        ao "*shakes her head* Grow up, Mom..."
        play sound2 ducati_start
        scene ch2ep1_149
        with dissolve
        pause 1.0
        play sound3 ducati_idle
        mc "Mom?"
        ao "What, you didn't know? She's the one who named me. Technically makes her my mother..."
        scene ch2ep1_150
        with dissolve
        ao "Catch you two on the flip side..."
        stop sound3 fadeout 2
        play sound4 ducati_driveaway
        scene ch2ep1_151
        with dissolve
        pause 1.0
        scene ch2ep1_152
        with dissolve
        pause 1.0
        scene ch2ep1_153
        with dissolve
        mc "Really?"
        m "..."
        mc "I'll take that as a yes."
        scene ch2ep1_154
        with dissolve
        mc "Where's the trip to, though? I overheard a bit of your conversation—it sounded serious."
        m "Jess offered her freedom after working with them for a while..."
        m "But she chose to stay on and become a roaming asset like what I used to do. Taking whatever jobs they throw her way."
        m "Undercover work, intel gathering, sabotage, assassination... whatever's on the table."
        scene ch2ep1_155
        with dissolve
        mc "... Aren't we working for the government now?"
        m "Yeah. So?"
        mc "*scoffs* Right... Got it."
        if moonroute:
            play sound2 cloth2
            scene ch2ep1_156
            with Dissolve(0.1)
            play sound3 cloth2
            pause
            scene ch2ep1_157
            with dissolve
            mc "Hm?"
            scene ch2ep1_158
            with dissolve
            pause
            scene ch2ep1_159
            with dissolve
            m "I'm home."
            menu:
                "Just the sweetest little angel":
                    mc "Just the sweetest little angel you are. Welcome home."
                    $ moonpoint += 1
                    $ renpy.notify(moonnotif)
                "Welcome back":
                    mc "Welcome back."
        scene ch2ep1_160
        with dissolve
        mc "You eaten yet?"
        m "Mhm, yeah. Grabbed lunch with Aine and Emma."
        scene ch2ep1_161
        with dissolve
        mc "You've been doing pretty well without me lately. Should I be impressed... or worried?"
        m "You were the one who told me to get used to it."
        mc "I told you to stay calm whenever we're apart. Never said you had to get used to it. I'm not going anywhere."
        m "And that's exactly what I've been doing. I've been managing the time apart... and lately, it hasn't been so bad."
        mc "That's good. You may be my secretary, but I never want you to depend on me like I'm your whole world, alright?"
        m "That's the ninety-seventh time you've said that since I became your aide."
        mc "Starting to sound like a broken record, huh?"
        scene ch2ep1_162
        with dissolve
        m "No. I love the attention."
        mc "*chuckles* Of course, you do."
        scene ch2ep1_163
        with dissolve
        m "By the way, are you planning to head back to the office?"
        mc "Yeah, why?"
        m "Don't bother. I already finished signing off whatever paperwork you had left for today."
        mc "You're a lifesaver. In more ways than one."
        m "Aine and Emma are there too, just in case I missed anything."
        mc "Aine's one thing... but Emma?"
        m "Mhm. I heard they're planning to hit the firing range together."
        mc "Oh... They've really been into that lately. Why don't you join them?"
        scene ch2ep1_164
        with dissolve
        m "Mmmmm..."
        if moonroute:
            mc "Then maybe we can swing by the local dojo next time. How about that?"
            play sound2 woosh
            scene ch2ep1_165
            m "I'd love that~!"
            mc "... Alright, easy with the sparkly eyes. You don't have to melt my heart just to get a sparring match."
            scene ch2ep1_166
            with dissolve
            mc "Let's see who's better, then."
            m "Really? Who's better?"
            mc "Pretty sure it'll count as practice for me."
            play sound2 woosh
            scene ch2ep1_167
            pause
            mc "Real blades."
            play sound2 woosh
            scene ch2ep1_168
            pause
            mc "... I shouldn't have challenged you, should I?"
            scene ch2ep1_169
            with dissolve
            m "No, no~! No backing out now. A husband's got to keep his promises to his wife."
            scene ch2ep1_170
            with dissolve
            mc "Well, I'm actually kinda pumped about this. We've never had the chance to spar before."
            m "Yeah... One year barely felt like enough time for everyone to even breathe, let alone settle down."
            scene ch2ep1_171
            with dissolve
            mc "Anyway, I should get going."
            m "Oh, you've still got plans? I thought—"
            mc "Nah, nothing work-related. Birthday's coming up, so I've got people to invite. And I promised I'd pick Freya up from the burger shack later."
            scene ch2ep1_172
            with dissolve
            m "Got it. Stay safe out there."
            scene ch2ep1_173
            with dissolve
            pause 0.5
            mc "*chuckles* Guess I really got her fired up about the dojo thing..."
        else:
            mc "Right... you're more of a blade girl."
            scene ch2ep1_171
            with dissolve
            mc "Anyway, I should get going."
            m "Oh, you've still got plans? I thought—"
            mc "Nah, nothing work-related. Birthday's coming up, so I've got people to invite. And I promised I'd pick Freya up from the burger shack later."
            scene ch2ep1_172
            with dissolve
            m "Got it. Stay safe out there."
        stop music2 fadeout 2
        stop music fadeout 2
        stop sound fadeout 2
        scene black
        with Dissolve(2.0)
        label aoifepause:
        if _in_replay:
            $ name = persistent.gallery_name
        scene aoifepause
        with dissolve
        $ renpy.pause()
        $ renpy.end_replay()
        play sound 'audio/gamepause.mp3'
        show title at move_slide
        with flash
        $ renpy.notify(imageunlock)
        $ renpy.pause()
    else:
        shu "Anyway, a chick just arrived."
        mc "Who?"
        shu "Your wife."
        stop music fadeout 4
        play music2 'audio/FindYourStyle.mp3' fadein 4

        scene black
        with dissolve
        with fadeq

        play sound cityalley loop
        scene ch2ep1_174
        with dissolve
        mc "Where—"
        play sound2 woosh
        play sound3 cloth2
        scene ch2ep1_175
        with hpunch
        mc "Whoa! You really love sneaking that move in, don't you?"
        m "Because it always works."
        if moonroute:
            scene ch2ep1_176
            with dissolve
            pause
            scene ch2ep1_175
            with dissolve
            m "I'm home."
            menu:
                "Just the sweetest little angel":
                    mc "Just the sweetest little angel you are. Welcome home."
                    $ moonpoint += 1
                    $ renpy.notify(moonnotif)
                "Welcome back":
                    mc "Welcome back."
        scene ch2ep1_177
        with dissolve
        mc "You eaten yet?"
        m "Mhm. Grabbed lunch with Aine and Emma."
        mc "You've been doing pretty well without me lately. Should I be impressed... or jealous?"
        m "You were the one who told me to get used to it."
        mc "I told you to stay calm when we're apart. Never said you had to get used to it. I'm not going anywhere."
        m "And that's exactly what I've been doing. I've been managing the time apart... and lately, it hasn't been so bad."
        mc "That's good. You may be my secretary, but I never want you to depend on me like I'm your whole world, alright?"
        m "That's the ninety-seventh time you've said that since I became your aide."
        mc "Starting to sound like a broken record, huh?"
        scene ch2ep1_178
        with dissolve
        m "No. I love the attention."
        mc "*chuckles* Of course, you do."
        scene ch2ep1_179
        with dissolve
        m "By the way, are you planning to head back to the office?"
        mc "Yeah, why?"
        m "Don't bother. I already finished signing off whatever paperwork you had left for today."
        mc "You're a lifesaver."
        m "Aine and Emma are there too, just in case I missed anything."
        mc "Aine's one thing... but Emma?"
        m "Mhm. I heard they're planning to hit the firing range together."
        mc "Oh... They've really been into that lately. Why don't you join them?"
        scene ch2ep1_180
        with dissolve
        m "Mmmmm..."
        if moonroute:
            mc "Then maybe we can swing by the local dojo next time. How about that?"
            play sound2 woosh
            scene ch2ep1_181
            m "I'd love that~!"
            mc "... Alright, easy with the sparkly eyes. You don't have to melt my heart just to get a sparring match."
            scene ch2ep1_182
            with dissolve
            mc "Let's see who's better, then."
            m "Really? Who's better?"
            mc "Pretty sure it'll count as practice for me."
            play sound2 woosh
            scene ch2ep1_183
            pause
            mc "Real blades."
            play sound3 woosh
            scene ch2ep1_184
            pause
            mc "... I shouldn't have challenged you, should I?"
            scene ch2ep1_185
            with dissolve
            m "No, no~! No backing out now. A husband's got to keep his promises to his wife."
            scene ch2ep1_186
            with dissolve
            mc "Well, I'm actually kinda pumped about this. We've never had the chance to spar before."
            m "Yeah... One year barely felt like enough time for everyone to even breathe, let alone settle down."
            scene ch2ep1_187
            with dissolve
            mc "Anyway, I should get going."
            m "Oh, you've still got plans? I thought—"
            mc "Nah, nothing work-related. Birthday's coming up, so I've got people to invite. And I promised I'd pick Freya up from the burger shack later."
            scene ch2ep1_188
            with dissolve
            m "Got it. Stay safe out there."
            scene ch2ep1_189
            with dissolve
            mc "*chuckles* Guess I really got her fired up about the dojo thing..."
        else:
            mc "Right... you're more of a blade girl."
            scene ch2ep1_187
            with dissolve
            mc "Anyway, I should get going."
            m "Oh, you've still got plans? I thought—"
            mc "Nah, nothing work-related. Birthday's coming up, so I've got people to invite. And I promised I'd pick Freya up from the burger shack later."
            scene ch2ep1_188
            with dissolve
            m "Got it. Stay safe out there."
    stop music2 fadeout 2
    stop music fadeout 2
    stop sound fadeout 2
    $ renpy.sound.set_volume(1.0, 1.0)

    scene black
    with dissolve
    with fade

    $ phone_time_add(minutes=20)
    play music 'audio/EtherealThoughts.mp3'
    play sound sigsauer_indoor_fire
    scene ch2ep1_190
    pause 0.2
    scene ch2ep1_191
    with Dissolve(0.2)
    play sound2 sigsauer_indoor_fire
    scene ch2ep1_190
    pause 0.2
    scene ch2ep1_191
    with Dissolve(0.2)
    play sound3 sigsauer_indoor_fire
    scene ch2ep1_190
    pause 0.2
    scene ch2ep1_191
    with Dissolve(0.2)
    scene ch1ep4_1031
    with dissolve
    bo "*laughs* Failed? No, not at all, Miss Agnor."
    scene ch1ep4_1032
    with dissolve
    bo "Do whatever you wish to me. After all, the die is cast."
    bo "Do you think a lowly human being like me can do the work of the Gods?"
    bo "In the far future, something far more significant will come..."
    bo "In the grand scheme of things, and the future of this world, I am... but a mere observer."
    play sound sigsauer_indoor_fire
    scene ch2ep1_192
    pause 0.2
    scene ch2ep1_193
    with Dissolve(0.2)
    play sound2 sigsauer_indoor_fire
    scene ch2ep1_192
    pause 0.2
    scene ch2ep1_193
    with Dissolve(0.2)
    play sound3 sigsauer_indoor_fire
    scene ch2ep1_192
    pause 0.2
    scene ch2ep1_193
    with Dissolve(0.2)
    scene ch1ep4_1033
    with dissolve
    a "What... the hell are you up to?"
    bo "My tongue is tied; I am forbidden to talk. In any case, I'll be kind enough to give you a warning..."
    bo "Be careful about Francis."
    bo "Now that there's no one to control him, who knows what he'll do."
    a "Don't tell me he's a Number, too?"
    scene ch1ep4_1034
    with dissolve
    bo "No, he is not. My project was long gone before I even found him."
    bo "He's... not what you think he is."
    a "Tell me what he's up to."
    bo "I don't know that either."
    scene ch1ep4_1035
    with dissolve
    bo "All his charades to get Olivia back, his so-called sister... are all in his head."
    bo "\"Olivia\" does not exist." with Dissolve(1.0)
    play sound sigsauer_dry
    scene ch2ep1_194
    pause 0.3
    play sound2 sigsauer_dry
    pause
    scene ch2ep1_195
    with dissolve
    pause
    play sound cloth
    scene ch2ep1_196
    with dissolve
    a "*exhales*"
    scene ch2ep1_197
    with dissolve
    e "So... already a few weeks in. What's the verdict?"
    a "Okay, okay—you win. I'll admit it. It's actually a pretty good stress reliever."
    scene ch2ep1_198
    with dissolve
    e "Told you. Who knew a little controlled violence could do wonders for your mood?"
    e "And look at you, finally shooting something other than snark. I'm so proud."
    scene ch2ep1_199
    with dissolve
    a "... When did you start talking like that?"
    e "Was that too much?"
    a "*chuckles* Yeah...? It's weird coming from you. Cut it out, Em."
    scene ch2ep1_200
    with dissolve
    e "Okay. Just wanted to see if you'd notice the difference."
    a "I've known you since you were still wetting the bed. What did you think was gonna happen?"
    scene ch2ep1_201
    with dissolve
    e "Hey, I was {b}{i}not{/i}{/b} wetting the bed back then. That phase ended ages ago."
    a "Sure it did. But seriously—what's all that about?"
    scene ch2ep1_202
    with dissolve
    e "Well... more and more people keep commenting on my voice. Saying it's too flat."
    a "So you've been trying to sound like... someone else?"
    e "Figured it couldn't hurt to try. Just to see."
    a "Oh, Em..."
    play sound cloth
    scene ch2ep1_203
    with dissolve
    a "Listen... you don't need to bend yourself just to fit someone else's idea of \"normal.\""
    a "Yeah, you've got a quiet presence, but that doesn't make it any less powerful."
    a "Some people have to raise their voices just to get noticed—take me, for example."
    a "But you? You make people lean in."
    a "And that kind of silence sticks with people a lot longer than noise ever will."
    scene ch2ep1_204
    with dissolve
    e "... Now I get it. Why you and [mc] have such a strong connection."
    e "You both just... know exactly what to say when it matters."
    a "Well, maybe. Not as strong as whatever he's got going on with Moon. That one really came out of left field."
    a "But... yeah. I guess so?"
    if allornothingroute:
        scene ch2ep1_205
        with dissolve
        e "Hey... are you really okay with this whole \"harem\" thing? Or whatever we're calling it?"
        a "Hm, I wasn't at first. But now I'm getting used to it. Why?"
        scene ch2ep1_206
        with dissolve
        e "I don't know... I just can't seem to make sense of it."
        a "*sighs* Honestly? Out of all of us, you're probably the only one still holding out for something one-on-one."
        e "Mmm... I'm not so sure about that."
    play sound phonevibrate loop
    scene ch2ep1_207
    with dissolve
    pause
    play sound phoneclick
    scene ch2ep1_208
    with dissolve
    e "You found something?"
    "......."
    "....."
    e "Mhm."
    "..........."
    e "Alright. I'm on my way."
    scene ch2ep1_209
    with dissolve
    a "What was that about?"
    e "Another lead. Might be something on Francis' whereabouts."
    scene ch2ep1_210
    with dissolve
    a "Em... how long are you gonna—"
    e "Aine, please... Just let me do this."
    scene ch2ep1_211
    with dissolve
    a "Alright, alright. I'm not trying to stop you. Just—"
    play sound closedoor2
    scene ch2ep1_212
    with dissolve
    a "Em?"
    a "*sighs*"
    stop music fadeout 2

    $ phone_time_add(minutes=15)
    if naomiroute:
        scene black
        with dissolve
        with fade

        play sound2 cardoorclose
        play sound parkwind loop
        scene ch2ep1_213
        with dissolve
        sc "Oi, if it ain't my boy!"
        mc "Mister Scott, how's it going?"
        scene ch2ep1_214
        with dissolve
        sc "Never better. Fit as a fiddle."
        sc "This about Naomi again?"
        scene ch2ep1_215
        with dissolve
        mc "*exhales* Yeah..."
        sc "Ahh, figured as much. Bad timing, though. She's in a proper foul mood today."
        sc "Then again, she hasn't exactly been all sunshine and rainbows since that day. But you know how it is."
        scene ch2ep1_216
        with dissolve
        sc "Still, if you're keen, I'm not stoppin' ya."
        scene ch2ep1_217
        with dissolve
        mc "What happened?"
        sc "Had a bit of a blow-up with her mum."
        mc "I see. Hope it's not about me."
        sc "Nah, not you, don't worry. Her mum's view's the same as mine, really."
        sc "C'mon then, let's head in."
        scene ch2ep1_218
        with dissolve
        pause
        scene ch2ep1_219
        with dissolve
        pause
        stop sound fadeout 2

        scene black
        with dissolve
        with fade

        play sound2 closedoor
        play music 'audio/CleanHeaven.mp3'
        scene ch2ep1_220
        with dissolve
        sc "Love, [mc]'s here. Get him a cuppa, would ya?"
        scene ch2ep1_221
        with dissolve
        mc "*chuckles* Thanks."
        play sound opendoor
        scene ch2ep1_222
        with dissolve
        n "..."
        show naomigesture
        with dissolve
        pause 3.3
        scene ch2ep1_223
        with dissolve
        pause
        play sound chair3
        scene ch2ep1_224
        with dissolve
        pause
        scene ch2ep1_225
        with dissolve
        n "What?"
        mc "That's one hell of a welcome."
        n "Wasn't expectin' ya, that's all."
        mc "Scott let me in. Said I should brace for impact."
        scene ch2ep1_226
        with dissolve
        n "Yeah, well, he knows better than to leave anything sharp in here when ya show up."
        scene ch2ep1_227
        with dissolve
        mc "Still stingy with the sugar, huh?"
        n "You don't even like sugar. What's wrong with {i}ya{/i}?"
        mc "Right... you remember that."
        n "'Course I do."
        scene ch2ep1_228
        with dissolve
        pause
        scene ch2ep1_229
        with dissolve
        mc "Look, I didn't come here to make things weird... again."
        mc "I just wanted to see how you were doing. And maybe invite you to something."
        scene ch2ep1_230
        with dissolve
        n "Lemme guess. Baby shower? Wedding? Somethin' with flowers and guilt?"
        mc "Okay, ouch."
        mc "No. It's my birthday. Just a small thing. Few friends, maybe a bonfire. I thought maybe you'd—"
        n "Why?"
        scene ch2ep1_231
        with dissolve
        mc "Because I want you there."
        n "And that's not weird?"
        mc "Is it?"
        n "You tell me."
        play sound chairdrag
        scene ch2ep1_232
        with dissolve
        mc "Naomi, come on. You've been cold with me ever since... that night."
        n "Don't. Don't go there if ya don't even know where \"there\" is."
        scene ch2ep1_233
        with dissolve
        mc "That's the thing—I don't. And it's been driving me crazy."
        mc "I remember bits. Laughing. Drinks. Working on your car. The sky looking... weirdly clear."
        mc "And then... nothing."
        mc "But I wake up thinking about it, and I feel like I missed something important."
        scene ch2ep1_234
        with dissolve
        n "You missed a {i}lot{/i}, [mc]."
        mc "Then help me understand."
        n "No. That's not mine to fix."
        scene ch2ep1_235
        with dissolve
        mc "Naomi, please. I need to know what I did. What I said. I know I messed something up, but I can't even own it unless you tell me what happened."
        n "You reckon that's what I want? A little confession and a \"sorry\" wrapped up with a bow?"
        mc "It's a start, isn't it?"
        scene ch2ep1_236
        with dissolve
        n "You really don't get it, do ya?"
        mc "Then explain it to me."
        n "No."
        mc "Why not?"
        n "Because you keep diggin' into something you clearly weren't ready to carry."
        mc "Maybe I wasn't. But I am now."
        n "It's not a bloody machine, [mc]. You don't just tighten a bolt or swap a busted part and call it fixed."
        mc "I just want to make it right."
        n "Right for you, or right for {i}me{/i}?"
        mc "I never meant to hurt you."
        n "Yeah... and that's what makes it worse."
        mc "..."
        scene ch2ep1_237
        with dissolve
        n "If you can't remember... maybe you weren't meant to."
        mc "Is that your way of punishing me?"
        scene ch2ep1_238
        with dissolve
        n "No. It's my way of lettin' you carry your own pain."
        n "You left me with mine."
        mc "I still want you there, Naomi."
        scene ch2ep1_239
        with dissolve
        n "And I still want a lotta things that aren't comin' back."
        n "Go home, [mc]. Please. Just... not today."

        scene black
        with dissolve
        with fade

        play sound parkwind loop
        play sound2 woodhit
        scene ch2ep1_240
        with hpunch
        pause
        scene ch2ep1_241
        with dissolve
        pause
        scene ch2ep1_242
        with dissolve
        mc "..."
        mc "Thanks, but I don't think I should be putting alcohol in my system for a while, Mister Scott. That thing gave a me new kind of PTSD."
        scene ch2ep1_243
        with dissolve
        sc "*laughs* Suit yourself."
        scene ch2ep1_244
        with dissolve
        sc "..."
        scene ch2ep1_245
        with dissolve
        sc "Sorry to hear what happened to ya. Naomi told me a bit."
        mc "I'm alright now. Or... I hope I am."
        scene ch2ep1_246
        with dissolve
        if gwenroute:
            mc "And uh... thanks for still letting me in. You kind of remind me of someone."
            sc "*chuckles* Must be a bloody good bloke, then."
            mc "Yeah. He is."
        else:
            mc "And uh... thanks for still letting me in."
        sc "Whatever's goin' on between you and Naomi, that's your business."
        sc "We didn't raise her to be tied down. Just taught her to stand on her own feet, and deal with whatever comes next."
        mc "Yeah... I can see that. She's strong. Sharp, too. She's... someone worth fighting for, Mister Scott. So I won't stop."
        sc "After that blow-up with her mum? Let her head cool down a bit. Give it some space. Then maybe come back around, yeah?"
        mc "I doubt it'll change the way she sees me... but yeah. I'll try."
        stop sound fadeout 2

        scene black
        with dissolve
        with fadeq

        scene ch2ep1_247
        with dissolve
        pause
        play sound punch_wall
        with hpunch
        pause 0.2
        play sound2 punch_wall
        with hpunch
        pause 0.2
        play sound3 punch_wall2
        scene ch2ep1_248
        with hpunch
        pause
        play sound cloth2
        scene ch2ep1_249
        with Dissolve(0.1)
        sc "Naomi!"
        scene ch2ep1_250
        with dissolve
        sc "Bloody hell—what'd you go and do that for?"
        scene ch2ep1_251
        with dissolve
        sc "Let me see!"
        scene ch2ep1_252
        with dissolve
        sc "This'll leave a mark! You lost the plot or somethin'?"
        n "Sorry... I'm just bloody pissed off."
        sc "At [mc]?"
        scene ch2ep1_253
        with dissolve
        n "... At myself."
        n "'Cause the most painful part is—none of it was his fault..."
    stop music fadeout 2

    scene black
    with dissolve
    with fade

    $ phone_time_add(hours=6)
    play sound traffic fadein 2 loop
    if naomiroute:
        scene ch2ep1_254
        with dissolve
        yt "Fuck... what the hell did I say that night? What did I do to her?"
        yt "How the hell am I supposed to even start—?"
        yt "Damn it. It's messing with my head again..."
        scene ch2ep1_255
        with dissolve
        mc "*deeply exhales*"
    scene ch2ep1_256
    with dissolve
    $ phone_start()
    $ switch_channel_view("aine_dm")
    show screen phone_ui
    $ quick_menu = False
    $ hide_all_phone_channels("aine_dm")
    $ lock_phone_screen()
    $ phone_stamp_rel("aine_dm")
    $ send_phone_message("Aine", "[mc], just a heads-up: I'm crashing at the office tonight. Gonna try and power through a few days' worth of work.", "aine_dm", do_pause=False)
    $ phone_pause(1.5)
    $ send_phone_message("Aine", "Make sure you get some rest, okay?", "aine_dm")
    $ show_all_phone_channels()
    $ unlock_phone_screen()
    show screen phone_blocker
    show screen phone_close_button
    $ send_phone_message(phone_config["phone_player_name"], "Alright. Thanks for the FYI. Just don't push yourself too hard.", "aine_dm")
    mc "..."
    yt "It's not the first time she's taken on a mountain of my paperwork, but..."
    yt "Something feels off."
    scene ch2ep1_257
    with dissolve
    pause
    yt "... How long's it been since this place first opened? Some things really don't change..."
    $ renpy.sound.set_volume(0.3, 1.0)
    play music 'audio/Travellin.mp3'
    scene ch2ep1_258
    with dissolve
    pause
    yt "Speaking of change..."
    scene ch2ep1_259
    with dissolve
    yt "Too much of it..."
    yt "Guess this is what they call a \"late bloomer.\""
    scene ch2ep1_260
    with dissolve
    yt "... Though sadly, all those burgers still didn't make it to the top shelf."
    f "Stop staring at my boobs, [mc]. I know what I'm working with. And I'm damn proud of it."
    scene ch2ep1_261
    with dissolve
    mc "Since when did you start reading minds?"
    f "I don't need to. You've got the subtlety of a neon sign."
    scene ch2ep1_262
    with dissolve
    mc "Or maybe we've developed some weird telepathy now."
    f "Please. If I had any superpower, I'd use it to teleport out of this place, not read your dirty thoughts."
    scene ch2ep1_263
    with dissolve
    mc "Huh... Where's your girl?"
    f "Left early. Said it was an emergency."
    scene ch2ep1_264
    with dissolve
    mc "What kind of emergency?"
    f "Beats me. Just said \"emergency\" and dipped."
    mc "Not this again..."
    mc "Frey, I told you—"
    scene ch2ep1_265
    with Dissolve(0.2)
    mc "... you need to manage your people properly." (multiple=2)
    f "Manage your people properly." (multiple=2)
    mc "And...?"
    scene ch2ep1_266
    with Dissolve(0.2)
    f "I don't like her."
    mc "Come on..."
    play sound2 woosh
    scene ch2ep1_267
    f "Don't \"come on\" me! I'm still mad you left me here!"
    mc "Frey, it's been over two months."
    scene ch2ep1_268
    with dissolve
    f "Whatever. I still hate you."
    mc "I'll make your favorite tonight."
    play sound2 woosh
    scene ch2ep1_269
    f "Wait, seriously~?"
    mc "If that's what it takes to get back in your good graces, sure. Why not?"
    scene ch2ep1_270
    with Dissolve(0.2)
    f "Yesss! God, I haven't had kimchi stew in forever!"
    mc "But hey, you're the branch manager now. If she's really that bad, just fire her and hire someone new."
    scene ch2ep1_271
    with dissolve
    f "Ugh... I hate doing interviews. Too much fake smiling."
    f "And the way she talks {i}really{/i} makes my skin crawl. But I can deal with it for now."
    mc "Just letting you know you've got options if things keep going south. I'll back your call."
    f "Nah, I'm good. I'm used to working..."
    scene ch2ep1_272
    with Dissolve(0.2)
    f "... {b}alone.{/b}"
    mc "Kimchi stew."
    scene ch2ep1_273
    with Dissolve(0.2)
    f "Alright, alright! Ten minutes, damn it!"
    stop sound fadeout 2

    $ phone_time_add(minutes=20)
    if (freyaroute and freyapoint == 10):
        scene black
        with dissolve
        with fade
        
        label freyacarblowjob:
        if _in_replay:
            $ name = persistent.gallery_name
        $ renpy.sound.set_volume(1.0, 1.0)
        play sound traffic fadein 2 loop
        play sound2 cardoorclose
        scene ch2ep1_274
        with dissolve
        "You see Freya already curled up in her seat, playing her game console as soon as you enter the car."
        scene ch2ep1_275
        with dissolve
        mc "Playing again?"
        f  "*murmurs* Knock it down... one, two... GOTCHA!"
        mc "..."
        scene ch2ep1_276
        with Dissolve(0.2)
        f "Oh, sorry! Didn't realize you were already here."
        scene ch2ep1_277
        with dissolve
        "Freya gets back to playing, but this time, she sits properly."
        f "What else would I do? I mean, do you not get bored with... like, I don't know, {b}just{/b} driving? Don't you want to add some {i}flavor{/i} inside here?"
        "You let out a cheeky sigh."
        mc "Well, rather than not wanting it, it's more of an \"I can't\". If I want to stay alive, that is."
        f "Oh right, I forgot that you need to focus on just driving if you're gonna drive."
        yt "This girl..."
        scene ch2ep1_278
        with dissolve
        f "*chuckles* Don't wanna drive, anyway... Guess I'll have no problems with boredom then!"
        f "I got you, right?"
        mc "Of course."
        "You give her a short smile, and she returns it with an even bigger one. Her energy might just be a little bit contagious—even for someone like you."
        scene ch2ep1_279
        with dissolve
        mc "Is this your way of saying I'm your personal driver?"
        f "Aww... you actually found it out..."
        "The two of you laugh it off, and the car's atmosphere feels lighter."
        scene ch2ep1_280
        with dissolve
        mc "We're going, Freya. Close your window. It's starting to drizzle."
        scene ch2ep1_281
        with dissolve
        pause
        "Freya pretends not to hear, eyes glued to the game."
        yt "Alright."
        $ renpy.music.set_volume(0.5, 0.0)
        stop sound fadeout 2
        play sound2 carwindowclose
        scene ch2ep1_282
        with dissolve
        $ renpy.music.set_volume(1.0, 1.0)
        "Without warning, you lean in and hit the window switch with a soft whirr."
        play sound cloth
        scene ch2ep1_283
        with dissolve
        "On your way back, you brush a loose strand behind her ear."
        f "H-Hey—"
        mc "Better."
        "Her fingers freeze over the buttons for a second. Her cheeks warm up."
        play sound woosh
        scene ch2ep1_284
        mc "Cat got your tongue?"
        f "... Shut up."
        mc "I'll take that as a yes."
        image fhandfa:
            "ch2ep1_285.jpg"
            pause 0.2
            "ch2ep1_286.jpg"
            pause 0.2
            repeat
        show fhandfa
        with Dissolve(0.2)
        "She clears her throat and pretends to keep playing."
        f "Phew~! Getting hot in here!"
        yt "Point for me."
        yt "It's fun to win against Freya every once in a while."
        scene ch2ep1_287
        with dissolve
        hide fhandfa
        "You step on the gas pedal as the engine starts. Freya, on the other hand, stays silent—her fingers now clicking away on her console again."
        scene black
        with dissolve
        $ renpy.music.set_volume(0.5, 1.0)
        play sound2 cardriveinterior loop
        scene ch2ep1_288
        with dissolve
        "After driving for a while, you notice how she occasionally glances out at the city passing by."
        scene ch2ep1_289
        with dissolve
        f "Drives are somewhat fun, no?"
        "She says, busily fiddling with her game, a smile on her face as peaceful as the ocean."
        scene ch2ep1_290
        with dissolve
        "You offer her one in return."
        mc "It sure is, until you get stuck in a caterpillar-like hell of traffic. That's what annoys me, most of the time."
        scene ch2ep1_291
        with dissolve
        f "City traffic jams, alright... That's noted."
        "Freya says with a Cheshire cat-like smile curling at her lips."
        yt "Noted?"
        stop sound2 fadeout 2
        play sound traffic fadein 1 loop
        scene ch2ep1_292
        with dissolve
        "Just a few seconds into the drive, you slow the car down. As if the devil himself had spawned to jinx your day, a massive traffic jam stretches out in front of you."
        f "Jinxed it."
        $ renpy.sound.set_volume(0.3, 1.0)
        play sound2 car_idle loop fadein 1
        scene ch2ep1_293
        with dissolve
        mc "No... I can't be seeing what I'm seeing..."
        "You stare at the road in disbelief as your grip tightens on the steering wheel."
        scene ch2ep1_294
        with dissolve
        f "Oh boy... wanna play?"
        "Freya suggests, offering her game console to you."
        mc "You better keep that for yourself. I think this will take a while." 
        f "Sure?"
        "She blinks at you, looking almost worried."
        scene ch2ep1_295
        with dissolve
        mc "Yeah. At least my patience's longer than yours."
        f "What a buzzkill."
        f "Suit yourself, then..."
        scene ch2ep1_296
        with dissolve
        pause
        yt "... And she's back to gaming."
        "You sigh, fidgeting with your hands on the gearstick instead."
        scene black
        with dissolve
        scene ch2ep1_297
        with dissolve
        "A few moments later, you find yourself extremely bored—agitated, even. You can't help but tap, tap, tap your fingers against anything your hands find."
        "All this dawdling is getting under your skin. The car's air conditioning is barely enough to cool your nerves."
        scene ch2ep1_298
        with dissolve
        f "You okay there? Can't we take another route?"
        mc "In theory, but with how close these vehicles are... we can't."
        f "That sucks..."
        f "Loosen up a bit, though. You didn't even notice that I stopped playing."
        scene ch2ep1_299
        with dissolve
        "You glance at her and realize she's actually put down her game console, by some small miracle."
        scene ch2ep1_300
        with dissolve
        f "See? And here I thought my patience was shorter than yours."
        mc "At least you had something to do with your hands a while ago..."
        stop music fadeout 4
        play music2 'audio/MissSeduction.mp3' fadein 4
        $ renpy.music.set_volume(1.0, 1.0)
        scene ch2ep1_301
        with dissolve
        f "Oh yeah?"
        yt "There goes her smile again, but this time's a bit different. She seems... bolder?"
        yt "Shit, I know what she's about to—!"
        scene ch2ep1_302
        with Dissolve(0.2)
        f "Well now that you mention it... my hands {i}are{/i} feeling restless..."
        f "Mind if I occupy them?"
        play sound3 belt
        scene ch2ep1_303
        with dissolve
        mc "What—"
        mc "—Freya?!"
        "Before you can even answer her question, the words catch in your throat the moment her burning hand slips between your legs."
        "She opens your pants—not all the way, just enough for her to snake in and throttle your arousing cock."
        "Freya traces a finger along your tip, slow and deliberate."
        scene ch2ep1_304
        with dissolve
        f "Cool your {i}head{/i}..."
        "She continues to lure you in with her doe-like, amethyst eyes as they find their way to meet yours."
        f "... will you?"
        play sound3 cloth
        scene ch2ep1_305
        with dissolve
        mc "Frey, urgh... W-what do you think you're doing?"
        f "Chill... didn't you imply the traffic was gonna take a hot minute?"
        "She whistles softly as she runs her slender fingers against your base."
        f "What better way to pass the time than play with my favorite console, [mc]?"
        scene ch2ep1_306
        with dissolve
        "Freya closes the distance between her plump lips and your hardening cock."
        "Her hot breath ghosting over the apex, sending your head into a tailspin."
        mc "I'm not sure if this is a great idea, Frey!"
        "You groan, the veins of your arms popping as you tightly clutch the steering wheel."
        f "I can stop if you want..."
        show freya15
        with dissolve
        "You gulp as she presses a kiss to your glans, then takes it in ever so gently."
        yt "How can I tell you to stop if you speak and look at me like that?!" 
        mc "Frey... urgh—!"
        f "Just say the word..."
        "She forces your cock down her throat as deep as she can. Your head falls back in satisfaction."
        f "Mm... You're not complaining now, are you?"
        yt "She feels so good... I'm pretty sure no one would see us here, anyway... Right?"
        f "The car's tinted, isn't it?"
        "Your mind, once cluttered by the chaos of traffic, goes eerily still—save for the parts processing the wet sounds coming from the girl below."
        mc "Yeah... Haaa..."
        "Freya's still in her seat, but now her top half is bent over towards you."
        yt "Towards my cock, rather..."
        mc "Are you not uncomfortable?"
        show freya16
        with dissolve
        hide freya15
        "Instead of replying, what she does instead nearly sends you over the edge."
        "Freya's hands—once just teasing your arousal—are now sloppily rubbing against it."
        pause
        show freya17
        with dissolve
        hide freya16
        "She takes you in whole, her tongue dragging along your cock as if it was a treat to lavish on."
        mc "Fuck—ah!"
        "Your hands almost tremble as you reach for her short, inky locks—gripping them for support as if that'll somehow dull the overwhelming pleasure."
        f "Nggggh—!!"
        yt "Shoot. Was that painful?"
        show freya18
        with dissolve
        hide freya17
        "As if answering your silent plea, Freya picks up the pace—her head bobbing faster, tongue and lips working together in a rhythm that makes your pulse spike."
        mc "Frey... ugh!"
        "Your groans grow louder: her movements nearly make you howl."
        "Her muffled moans, stuffed full with your cock, cut through the haze in your mind so sharply you swear even those in the cars outside can hear."
        mc "Shit... you feel so good, Frey..." 
        "Freya's mouth and hands move in perfect tandem, working you over and dragging you closer to your limit."
        "Her warm palms cup your balls like they belong there, massaging them with deliberate care."
        "At the same time, your tip brushes the back of her throat—you're soaked in sensation, more drenched than ever."
        mc "I-I'm close..."
        pause
        show freya19
        with dissolve
        hide freya18
        f "Hngg..."
        "Your hips now thrust upward, as if welcoming Freya's mouth while she pushes down, taking you even deeper."
        mc "Yeah... nngh—! I'm really close, Frey...!" 
        "Your grip tightens as you shove her head down, forcing her deeper onto you as your neurons fire with abandon."
        mc "That's it, Frey... urgh... haaa..."
        "You both move faster as you feel yourself edging closer to climax."
        yt "This might be the only time I've ever been grateful for traffic..."
        mc "Urgh, I-I'm cumming... mmh..." 
        pause
        scene ch2ep1_307
        with hpunch
        hide freya19
        "As you crash over the edge, you shove Freya's head down deep. Yet still—her mouth never relinquishes your cock as you feel your release gushing out from your tip."
        "Freya almost chokes. But she takes it in. She swallows it all in."
        play sound3 carhorn_multiple
        scene ch2ep1_308
        with Dissolve(0.2)
        pause
        scene ch2ep1_309
        with Dissolve(0.1)
        "Your grip on her hair loosens as you realize she's still buried deep on your cock—thanks to your own naughty hands."
        mc "Oh, fuck. Sorry, Frey!"
        stop sound fadeout 2
        play sound2 cardriveinterior loop
        scene ch2ep1_310
        with Dissolve(0.2)
        "You slam your foot on the gas just as Freya lifts herself off you—both of you too dazed to notice the traffic's already gone."
        f "You're shaking... Mm... Can you drive?"
        scene ch2ep1_311
        with dissolve
        "You watch her lick her fingertips like she just finished a meal."
        "You, on the other hand, feel completely spent, like you were the one devoured."
        "Which technically, you were."
        mc "Y-Yeah..."
        scene ch2ep1_312
        with dissolve
        "You catch Freya eyeing your now-flaccid dick through your open zipper, a knowing smirk on her face."
        f "That was good. I swear I almost saw stars towards the end."
        yt "Man, this is embarrassing..."
        scene ch2ep1_313
        with dissolve
        f "Stop the car for a while. I'm going to clean you up."
        "You glance at her with an unexplainable look."
        f "Or just don't, if you want. This mess may have satisfied the hunger that I've had for a while."
        mc "You're a menace..."
        stop sound2 fadeout 1
        $ renpy.sound.set_volume(1.0, 1.0)
        play sound carmoving loop fadein 1
        play sound3 traffic loop fadein 2
        scene ch2ep1_314
        with dissolve
        f "Close your pants, [mc]! We're almost home. I don't think there's going to be another traffic jam between now and then..."
        "Your ears heat up with embarrassment." 
        mc "I will. Get back to playing your game instead, will you?"
        "You snap back at her light-heartedly."
        f "So mean! But the bulge in your pants might be my favorite game now, how about that—"
        mc "Stop teasing me! No kimchi stew!"
        stop sound3 fadeout 1
        stop sound fadeout 1
        play sound2 cardriveinterior fadein 1 loop
        scene ch2ep1_315
        with dissolve
        f "Aww... I just wanted to get back at you for the window and hair thing, you know?"
        mc "That's one way to put it..."
        f "You knew I'd close it! You were just being a \"menace\"!"
        "You smirk at her."
        mc "Well you got me back, alright."
        "Freya laughs cheekily as you continue on your way back home."
        f "Yeah, I win once again... You're too easy, [mc]."
        mc "You'll be eating those words once my hands go down your pants during round two."
        f "Is that supposed to be a challenge? Or a promise?"
        $ renpy.end_replay()
    stop music fadeout 2
    stop music2 fadeout 2
    stop sound2 fadeout 2
    
    scene black
    with dissolve
    with fade
    
    $ phone_time_add(minutes=30)
    play sound nightambience loop fadein 2
    play music 'audio/CleanHeaven.mp3'
    scene ch2ep1_316
    with dissolve
    f "Thanks~! I'll be there in a few—just need to set up my stream before dinner."
    scene ch2ep1_317
    with dissolve
    f "And don't forget my stew."
    mc "I got you, I got you."
    play sound2 cardriveaway
    scene ch2ep1_318
    with dissolve
    stop sound2 fadeout 4
    play sound3 carpark
    pause
    $ renpy.sound.set_volume(0.3, 1.0)
    stop sound3 fadeout 2
    play sound4 phonemessage
    scene ch2ep1_319
    with dissolve
    pause
    scene ch2ep1_320
    with dissolve
    $ phone_start()
    $ switch_channel_view("emma_dm")
    show screen phone_ui
    $ quick_menu = False
    $ hide_all_phone_channels("emma_dm")
    $ lock_phone_screen()
    $ phone_stamp_rel("emma_dm")
    $ send_phone_message("Emma", "[mc]. [mc]. I don't think I'll make it to dinner tonight. Go ahead without me, alright?", "emma_dm")
    $ send_phone_message(phone_config["phone_player_name"], "I'll save you a plate.", "emma_dm")
    if emmaroute:
        $ phone_pause(1.0)
        $ send_phone_message("Emma", "Thanks. I love you.", "emma_dm")
        $ show_all_phone_channels()
        $ unlock_phone_screen()
        show screen phone_blocker
        show screen phone_close_button
        $ send_phone_message(phone_config["phone_player_name"], "Love you too, Em.", "emma_dm")
    else:
        $ phone_pause(0.5)
        $ show_all_phone_channels()
        $ unlock_phone_screen()
        show screen phone_blocker
        show screen phone_close_button
        $ send_phone_message("Emma", "Thanks.", "emma_dm")
    yt "Guess this is about Francis again."
    stop sound fadeout 2
    scene ch2ep1_321
    with flash
    e "Let me handle it. That's what I'm here for."
    scene ch2ep1_322
    with dissolve
    mc "But Em... we could just—"
    e "No. I won't be able to sleep at night knowing there's still someone out there who could be a threat to us."
    e "Whether or not you're ready to find him... I am."
    play sound nightambience loop fadein 2
    scene ch2ep1_323
    with flash
    mc "*exhales*"
    scene ch2ep1_324
    with dissolve
    pause
    stop sound fadeout 2
    play sound2 phonevibrate loop
    scene ch2ep1_325
    with dissolve
    pause
    scene ch2ep1_326
    with dissolve
    pause
    play sound2 phoneclick
    scene ch2ep1_327
    with dissolve
    lev "Hello?"
    mc "Hey, Doc. It's [mc]."
    lev "[mc]. I wasn't sure I'd hear from you again after this morning."
    play sound nightambience loop fadein 2
    scene ch2ep1_328
    with dissolve
    mc "Yeah... about that. Sorry for bailing on you. Things just got a bit... heavy."
    lev "It's alright. It happens."
    mc "Still, wasn't cool of me. I want to keep going with the sessions."
    lev "Good. That's good to hear."
    lev "Next week, same time? I'll slot you back in."
    mc "Yeah. That works."
    scene ch2ep1_329
    with dissolve
    lev "Alright. And [mc]?"
    mc "Yeah?"
    lev "It's okay to leave; just make sure you come back."
    $ phone_time_add(minutes=5)
    play sound2 phoneclick
    play sound3 cloth
    scene ch2ep1_330
    with dissolve
    mc "*whispers* Working on it..."
    scene ch2ep1_331
    with dissolve
    pause
    scene ch2ep1_332
    with dissolve
    pause
    $ renpy.sound.set_volume(1.0, 1.0)
    stop sound fadeout 2
    play sound2 phonevibrate loop
    scene ch2ep1_333
    with dissolve
    pause
    scene ch2ep1_334
    with dissolve
    pause
    play sound2 phoneclick
    scene ch2ep1_335
    with dissolve
    cl "Is something wrong?"
    mc "Why is it that every time I call, you assume I'm in some kind of mess?"
    cl "First impressions tend to stick around."
    play sound watermovement
    scene ch2ep1_336
    with dissolve
    mc "Fair enough... I guess it is kind of serious. I need to know more about the Serum."
    cl "..."
    mc "Claire?"
    cl "Why ask me? Don't you have a wife for that sort of thing?"
    mc "This isn't about us. I'm looking for technical details. And last I checked, you're still the best in that department."
    scene ch2ep1_337
    with dissolve
    cl "Does she know you're doing this?"
    mc "... No. No one does."
    play sound2 cloth
    scene ch2ep1_338
    with dissolve
    mc "Look, I'm not trying to go behind anyone's back. I just really need your help."
    play sound nightambience loop fadein 2
    scene ch2ep1_339
    with dissolve
    cl "Alright. But I don't give away intel for free."
    mc "How much?"
    cl "Not money."
    stop sound fadeout 2
    play sound2 chair3
    scene ch2ep1_340
    with dissolve
    mc "... Then what?"
    scene ch2ep1_341
    with dissolve
    cl "Your blood."
    mc "My blood? Are you some kind of vampire owl?"
    cl "That's my price. Take it or leave it."
    mc "*sighs* Fine. You've got it."
    cl "Meet me at Jess' café. Tomorrow morning. Nine sharp."
    mc "I'll be there."
    stop music fadeout 4
    play music2 'audio/Togetherness.mp3' fadein 4
    play sound3 phoneclick
    play sound nightambience loop fadein 2
    play sound2 carpark fadein 1
    scene ch2ep1_342
    with dissolve
    pause
    play sound4 cardoorclose
    scene ch2ep1_343
    with dissolve
    mc "Sky."
    play sound2 cardriveaway
    scene ch2ep1_344
    with dissolve
    s "[mc]!"
    scene ch2ep1_345
    with dissolve
    mc "You know I could've picked you up, right?"
    s "It's fine. Gotta carry my own ass sometimes."
    mc "Still... you coming straight from campus?"
    scene ch2ep1_346
    with Dissolve(0.2)
    s "Ugh. Don't even get me started. Being vice principal is like juggling babysitting, janitorial work, politics, and therapy—all before lunch."
    mc "That bad, huh?" # Smirks
    s "Worse."
    s "This morning, a student called me \"Ma'am.\""
    scene ch2ep1_347
    with dissolve
    s "I mean it's okay, but with how they look at me, I wasn't sure if they found me terrifying or were just trying to be polite."
    mc "You don't seem that scary to me."
    scene ch2ep1_348
    with dissolve
    s "Then some kid pulled the fire alarm. Just to check if it worked."
    yt "This sounds like a familiar complaint..."
    mc "Let me guess, that kid again? What was her name? Dorian?"
    scene ch2ep1_349
    with dissolve
    s "Bingo."
    mc "*chuckles* Classic."
    s "I finally get why people say kids are evil. They're little agents of chaos."
    mc "Like you haven't been wrangling them for years."
    scene ch2ep1_350
    with dissolve
    s "*sighs* Yeah, but the office hits different. You get front-row seats to the meltdown."
    mc "So? How'd the staff meeting go?"
    s "*groans* Don't remind me..."
    s "Twenty adults spent forty-five minutes arguing whether they should censor the internet for students. That was a pointless, stupid meeting."
    mc "I assume you were the only one who voted for \"who gives a crap\"?"
    s "Right. Same circus, different clowns."
    play sound3 cloth
    play sound2 chair3
    scene ch2ep1_351
    with dissolve
    pause
    s "Jeez... not a single light on. When did the place start feeling this empty?"
    mc "Everyone's been slammed this week. And the only one inside won't step out of her room."
    scene ch2ep1_352
    with dissolve
    s "How's she holding up?"
    mc "*exhales* Still quiet. Keeps to herself unless you strike up conversation first."
    mc "But she's eating. So that's... uh... something."
    s "Yeah... That's something."
    scene ch2ep1_353
    with dissolve
    mc "Honestly, I'm just glad the mask cracked. She hasn't said it out loud, but..."
    s "Better that I saw it myself. Wouldn't have believed it if someone just told me."
    scene ch2ep1_354
    with dissolve
    s "*laughs softly* You know... it's kinda cool, though. Imagine if I went full goth like her."
    menu:
        "I'd prefer you cuter":
            mc "Nah... I like you just the way you are. Cute suits you better."
            $ skypoint += 1
            $ renpy.notify(skynotif)
        "I can't imagine":
            mc "Hmm, nah... I can't picture you that way at all."
    scene ch2ep1_355
    with dissolve
    s "*sniffs*"
    scene ch2ep1_356
    with dissolve
    s "Wait a sec..."
    mc "What?"
    s "You smell different than you did this morning."
    yt "Uh-oh..."
    s "You smell like..."
    play sound2 woosh
    scene ch2ep1_357
    s "... Freya!"
    mc "Well... I did pick her up from work."
    $ phone_time_add(minutes=8)
    if skyroute:
        image skrubosctoke:
            "ch2ep1_358.jpg" with Dissolve(0.2)
            pause 0.3
            "ch2ep1_359.jpg" with Dissolve(0.2)
            pause 0.3
            "ch2ep1_358.jpg" with Dissolve(0.2)
            pause 0.3
            "ch2ep1_359.jpg" with Dissolve(0.2)
            pause 0.5
            "ch2ep1_360.jpg" with Dissolve(0.2)
            pause 0.3
            "ch2ep1_361.jpg" with Dissolve(0.2)
            pause 0.3
            "ch2ep1_360.jpg" with Dissolve(0.2)
            pause 0.3
            "ch2ep1_361.jpg" with Dissolve(0.2)
            pause 0.5
            "ch2ep1_362.jpg" with Dissolve(0.2)
            pause 0.3
            "ch2ep1_363.jpg" with Dissolve(0.2)
            pause 0.3
            "ch2ep1_362.jpg" with Dissolve(0.2)
            pause 0.3
            "ch2ep1_363.jpg" with Dissolve(0.2)
            pause 0.5
        play sound2 cloth2
        show skrubosctoke
        mc "Uh, Sky?"
        scene ch2ep1_364
        with dissolve
        hide skrubosctoke
        s "*sniffs*"
        scene ch2ep1_365
        with dissolve
        s "*laughs* Now you smell like me. I'm counting that as a win over her."
        mc "*chuckles* That's... not exactly how scent dominance works."
        yt "Some things never change..."
    else:
        s "Hmmm... You sure?"
    mc "You're making this weird."
    s "I {i}am{/i} weird. You just keep pretending to forget."
    if skyroute:
        scene ch2ep1_366
        with dissolve
        yt "If there's one person I haven't made real progress with... it's Sky."
        yt "Funny how we're so close, but when it really matters, we still keep each other at arm's length."
        play sound2 windgrass loop
        scene ch2ep1_367
        with dissolve
        pause
        yt "We've been skirting around the idea of telling Klara. About us. About everything."
        yt "Even had a plan, sort of."
        yt "What we'd say."
        yt "How we'd soften the blow."
        yt "Where we'd sit."
        yt "Hell, I even rehearsed how much sarcasm Sky would throw in."
        yt "But then Klara broke... and all that preparation, all our bottled-up courage just crumbled with her."
        yt "And now we're stuck."
        yt "Still gripping the truth like it's a live grenade, praying that maybe staying quiet will sting less than honesty."
        stop sound2 fadeout 3
        scene ch2ep1_368
        with dissolve
        yt "And... maybe it does."
        yt "More than either of us would ever admit..."
        stop sound fadeout 2
        stop music2 fadeout 2
        scene black
        with Dissolve(2.0)
        label skypause3:
        if _in_replay:
            $ name = persistent.gallery_name
        scene skypause3
        with dissolve
        $ renpy.pause()
        $ renpy.end_replay()
        play sound 'audio/gamepause.mp3'
        show title at move_slide
        with flash
        $ renpy.notify(imageunlock)
        $ renpy.pause()
    stop sound fadeout 2
    stop music2 fadeout 2

    scene black
    with dissolve
    with fade

    $ phone_time_add(hours=1)
    $ renpy.sound.set_volume(1.0, 1.0)
    play music 'audio/LongRoadHome.mp3'
    play sound closedoor2
    scene ch2ep1_369
    with dissolve
    mc "Evening."
    play sound platedown
    scene ch2ep1_370
    with dissolve
    pause
    play sound match_strike
    scene ch2ep1_371
    with Dissolve(0.1)
    pause
    play sound2 match_flamestart
    scene ch2ep1_372
    with dissolve
    pause
    scene ch2ep1_373
    with Dissolve(0.1)
    pause
    scene black
    with Dissolve(0.2)
    scene ch2ep1_374
    with Dissolve(0.2)
    stop sound2 fadeout 2
    k "Why?"
    mc "It's getting darker, Klara."
    play sound2 cloth
    scene ch2ep1_375
    with dissolve
    k "Dark never asked me to change it."  
    mc "Yeah? Well, I did. Hard to chew on mystery meat when I can't see it."  
    play sound chair3
    scene ch2ep1_376
    with dissolve
    pause
    scene ch2ep1_377
    with dissolve
    k "Want a story?"  
    mc "Now?"  
    scene ch2ep1_378
    with Dissolve(0.1)
    pause
    scene black
    with Dissolve(0.2)
    scene ch2ep1_377
    with Dissolve(0.2)
    k "Why not? It's dinner time. Seems appropriate."
    scene ch2ep1_379
    with dissolve
    pause 0.5
    k "There was a woman who lived in a room that forgot itself."  
    k "Once, it carried voices, shelves bending under books, windows that breathed with the weather."  
    k "But someone left. And the walls went still, like they didn't trust sound anymore."  
    k "She shut the door to hold onto what little stayed."  
    k "Eventually, she stopped lighting candles. Said the glow made the quiet lean in too close." 
    scene ch2ep1_380
    with dissolve
    k "The windows crusted over. She told herself the sun would pry too much out of her if she let it in."  
    k "So no one knocked. And she never touched the latch."  
    k "The room sank into waiting, not sure what it was anymore."  
    scene ch2ep1_381
    with dissolve
    k "Then one night, someone walked in. No knock. No fanfare."  
    k "They sat down. Said nothing. Lit a candle."  
    k "Not out of hope. Not out of love, either. Just for that sliver of presence."  
    k "And the room shifted, like it remembered how to hold a heartbeat again."  
    scene ch2ep1_382
    with dissolve
    mc "... Huh?"  
    k "Nothing. Just air I needed to get out."  
    scene ch2ep1_383
    with dissolve
    pause
    play sound utensilsonplate
    scene ch2ep1_384
    with dissolve
    pause
    scene ch2ep1_385
    with dissolve
    pause
    scene ch2ep1_386
    with dissolve
    pause
    play sound wood_drag
    scene ch2ep1_387
    with dissolve
    pause
    scene ch2ep1_388
    with dissolve
    pause
    scene ch2ep1_389
    with dissolve
    pause
    scene ch2ep1_390
    with dissolve
    mc "So... did the person stay?"  
    k "... What?"  
    mc "In your story. The one who lit the candle. Did they stay?"  
    play sound sip
    scene ch2ep1_391
    with Dissolve(0.2)
    pause
    scene ch2ep1_392
    with Dissolve(0.1)
    pause
    scene black
    with Dissolve(0.2)
    scene ch2ep1_391
    with Dissolve(0.2)
    k "Maybe. Depends what they were looking for."  
    mc "And what was that?"  
    scene ch2ep1_393
    with dissolve
    k "Some people hear quiet and think it's peace. Others hear the same quiet and call it dark."  
    mc "*chuckles* Some don't mind either way."  
    k "Some can't even tell which is which."  
    $ renpy.music.set_volume(0.0, 0.0)
    scene ch2ep1_394
    with Dissolve(0.1)
    pause
    play sound sip
    scene ch2ep1_395
    with Dissolve(0.1)
    pause
    stop sound
    play sound2 fire_crackle loop
    scene ch2ep1_396
    with Dissolve(0.1)
    pause
    stop sound2
    scene ch2ep1_397
    with Dissolve(0.1)
    k "... You're about to baptize your shirt in sauce."  
    play sound tablehit
    mc "Ah, shit—" with hpunch
    scene ch2ep1_398
    with dissolve
    k "{i}The room doesn't stay alive for long. But sometimes, a moment's enough to trick it into breathing again."  
    call hide_days from _call_hide_days_36
    with dissolve

    scene black
    with dissolve
    with fadeq

    $ phone_time_add(hours=10)
    show screen day_friday with dissolve
    $ renpy.music.set_volume(1.0, 7.0)
    scene ch2ep1_399
    with dissolve
    mc "Anyone seen Emma?"
    m "She left a few hours ago."
    mc "Did she eat before she took off?"
    s "Hmm... don't think so."
    mc "*exhales* Damn..."
    scene ch2ep1_400
    with dissolve
    k "{i}Day three-hundred eighty-four.{/i}"
    scene ch2ep1_401
    with Dissolve(0.1)
    pause
    scene black
    with Dissolve(0.2)
    play sound match_strike
    scene ch2ep1_402
    with Dissolve(0.2)
    pause
    play sound2 match_flamestart
    scene ch2ep1_403
    with dissolve
    k "{i}Just a little light...{/i}"
    scene ch2ep1_404
    with dissolve
    k "..."
    scene ch2ep1_405
    with Dissolve(0.3)
    pause
    scene ch2ep1_406
    with Dissolve(0.1)
    pause
    scene black
    with Dissolve(0.2)
    play sound chair3
    scene ch2ep1_407
    with Dissolve(0.2)
    k "..."
    play sound closedoor2
    scene ch2ep1_408
    with dissolve
    pause
    scene ch2ep1_409
    with dissolve
    pause
    scene ch2ep1_411
    with dissolve
    mc "... You lit it?"
    scene ch2ep1_410
    with Dissolve(0.1)
    pause
    scene black
    with Dissolve(0.2)
    scene ch2ep1_411
    with Dissolve(0.2)
    k "... It was getting dim."
    scene ch2ep1_412
    with dissolve
    pause
    scene ch2ep1_413
    with dissolve
    mc "*shrugs* Looks good from here."
    play sound platedown
    scene ch2ep1_414
    with dissolve
    pause
    play sound chair3
    scene ch2ep1_415
    with dissolve
    pause
    scene ch2ep1_416
    with dissolve
    pause
    scene ch2ep1_417
    with dissolve
    pause
    scene ch2ep1_418
    with dissolve
    k "[mc], do you..."
    scene ch2ep1_419
    with dissolve
    mc "Yeah?"
    k "... No, it's... nothing."
    scene ch2ep1_420
    with dissolve
    mc "..."
    stop music fadeout 2

    scene black
    with dissolve
    with fade

    $ phone_time_add(minutes=30)
    play sound cityalley loop
    scene ch2ep1_421
    with dissolve
    pause
    play sound2 cardriveaway
    scene ch2ep1_422
    with dissolve
    pause 0.5
    scene ch2ep1_423
    with dissolve
    pause 1.0
    stop sound2 fadeout 3
    play sound3 carpark
    scene ch2ep1_422
    with dissolve
    pause 0.5
    scene ch2ep1_424
    with dissolve
    pause
    play sound2 carwindowclose
    scene ch2ep1_425
    with dissolve
    mc "Bite-size."
    scene ch2ep1_426
    with dissolve
    ju "Protein Shake."
    mc "*nods* Good one."
    play sound2 cardriveaway
    scene ch2ep1_427
    with dissolve
    ju "*groans* Jackass..."
    stop sound fadeout 2
    stop sound2 fadeout 2

    scene black
    with dissolve
    with fade

    $ phone_time_add(hours=1)
    $ phone_time_add(minutes=30)
    play sound cityalley loop
    scene ch2ep1_428
    with dissolve
    mc "Did my watch stop, or are you actually early?"  
    cl "I don't keep people hanging. Waste of time."  
    scene ch2ep1_429
    with dissolve
    cl "You showed up sharp. Good. Half the people I deal with can't even button a jacket straight."  
    scene ch2ep1_430
    with dissolve
    mc "So we're going somewhere?"  
    scene ch2ep1_431
    with dissolve
    cl "Yeah. But not here. Too many shadows leaning in."  
    mc "That bad?"  
    cl "Bad enough. Just follow. Questions later."  
    cl "My car's around the corner. Leave your truck. I'll get you back when we're done."  
    mc "... Fine."  
    stop sound fadeout 2

    scene black
    with dissolve
    with fade

    play music 'audio/MindGame.mp3'
    scene ch2ep1_432
    with dissolve
    mc "Looks like a library... but what's the point of dragging me here?"
    cl "Not a library. Think of it more as an archive."
    scene ch2ep1_433
    with dissolve
    cl "Every serum user—records, scraps, fragments of their lives. All kept here. So the traces don't vanish."
    cl "This has been my work for years."
    mc "... That's... a mountain's worth of obsession."
    scene ch2ep1_434
    with dissolve
    mc "But if their names had to be kept here, I'm guessing most of them didn't walk away clean."
    cl "Not most. No."
    scene ch2ep1_435
    with dissolve
    mc "So some did? Survive, I mean. Other than us?"
    cl "A handful. The ones the serum didn't break. Enough to count on fingers, if you're generous."
    mc "Where are they now?"
    cl "Some under Jess' watch. A few tried to disappear into normal lives... not many managed it."
    mc "Figures."
    scene ch2ep1_436
    with dissolve
    mc "..."
    cl "Someone caught your eye?"
    scene ch2ep1_437
    with dissolve
    mc "Number Thirteen: Serene Rainyday..."
    cl "Ah... her."
    scene ch2ep1_438
    with dissolve
    mc "Can I?"
    cl "Go ahead. Careful with it. She wrote it herself—there's no copy."
    stop music fadeout 4
    play sound chair3
    scene ch2ep1_439
    with dissolve
    pause
    play music2 'audio/ThoughtsInTheRain.mp3' fadein 2
    scene ch2ep1_440
    with dissolve
    ser "My name was Serene."
    ser "At least, that's what I remember. Before the Numbers. Before the cold black rooms."
    play sound sea fadein 2 loop
    scene ch2ep1_441
    with dissolve
    ser "I once lived by the sea with my older brother."
    ser "We crammed ourselves into a corroded flat that coughed with every storm."
    ser "Pipes leaking, heater rattling, windows keening when the wind pressed too hard."
    scene ch2ep1_442
    with dissolve
    ser "Nothing ever worked the way it should, but we made it ours. The cracks carried our voices, and even the broken corners felt alive."
    ser "When silence locked me up, when I couldn't push out a word, he'd give me another one. A name. Something lighter than I felt."
    stop sound fadeout 2
    scene ch2ep1_443
    with dissolve
    ser "\"You're still my sunshine,\" he'd say, brushing the hair out of my eyes. \"Even when the clouds won't move.\""
    ser "I never told him how much I clung to that. How much of my light only existed because he said it did."
    play sound sea fadein 2 loop
    scene ch2ep1_444
    with dissolve
    ser "I was twelve when the men came. They said I was useful. That my blood carried something rare. Dangerous."
    scene ch2ep1_445
    with dissolve
    ser "They handed my brother a paper. A choice dressed up as mercy. His signature bled onto the page while his eyes brimmed red."
    ser "I told him it was okay. That I'd be back. That one day we'd laugh about it."
    stop sound
    scene black
    pause 0.8
    ser "We never did."
    play sound3 opendoor_hydrolic
    scene ch2ep1_446
    with dissolve
    play sound2 number13
    ser "I was taken to a facility. They called it an institute, but it felt more like a terrarium. Glass walls, steel veins, and nowhere to hide."
    ser "They stripped me of my name and gave me a number: Thirteen. I asked if it meant bad luck. They didn't bother answering."
    ser "For the first year, I resisted, not with my fists, but by refusing their ideals. By failing their tests, ignoring their questions, turning my face from their needles until they pinned me down."
    ser "I was silenced with sedation more often than I was acknowledged as human."
    scene ch2ep1_447
    with dissolve
    ser "Then came the serum."
    ser "They called it progress. To me, it felt like trespass."
    ser "My body turned foreign. Dreams slipped away. Sleep stopped visiting often."
    ser "Sight cut like blades. Sound clawed at me. Every sense tuned sharp enough to hurt."
    ser "They applauded my discipline. My adaptability. They said I was one of the proofs that their work had succeeded."
    ser "They called me a model subject. They said obedience was a virtue."
    ser "But obedience is nothing. If there's a mercy, it would be erasure."
    play sound2 war loop fadein 2
    scene ch2ep1_448
    with dissolve
    ser "They shaped me into a weapon. Fed me languages I'll never use for mercy. Sent me on missions built to erase me. But somehow, I always came back."
    scene ch2ep1_449
    with dissolve
    ser "I stopped asking why. Tools don't get to ask."
    ser "But there was one thing they couldn't cauterize, not completely."
    stop sound2 fadeout 2
    play sound sea fadein 2 loop
    scene ch2ep1_450
    with dissolve
    ser "Some nights, in the antiseptic dark, I still drifted back to the sea."
    scene ch2ep1_451
    with dissolve
    ser "The wind shoving at cracked windows."
    scene ch2ep1_452
    with dissolve
    ser "The smell of burnt rice clinging to the walls."
    scene ch2ep1_453
    with dissolve
    ser "My brother's arms around me, his voice giving me a name that meant light."
    scene ch2ep1_454
    with dissolve
    ser "In those dreams, I walk into the ocean. Step after step..."
    play sound watermovement2
    scene black
    ser "... until everything dissolves. Until there's nothing left but hush."
    play sound2 rain_heavy fadein 2 loop
    scene ch2ep1_455
    with Dissolve(0.1)
    ser "And then I wake."
    scene ch2ep1_456
    with dissolve
    ser "But one time, waking was different. No cell. No handler. No orders waiting."
    ser "It was raining."  
    scene ch2ep1_457
    with dissolve
    ser "I lay there, listening to it knock across the roof. A sound I thought I'd lost."
    scene ch2ep1_458
    with dissolve
    ser "In a puddle on the floor, my reflection stared back—blurred, pale, almost erased. And yet behind it, I glimpsed the girl the world tried to smother."
    ser "Not who I was. Not who they built. But still... someone."
    scene ch2ep1_459
    with dissolve
    ser "So I chose a name. One that belonged to both pieces of me—the before, and the after."
    scene ch2ep1_460
    with Dissolve(2.0)
    ser "Serene Rainyday." with Dissolve(2.0)
    ser "Serene, because stillness is the only thing I still chase."
    ser "Rainyday, because once, he called me light."
    stop sound2 fadeout 2
    scene ch2ep1_461
    with dissolve
    ser "When I woke, the world was nothing different. And I was still standing in the battlefield."
    scene ch2ep1_462
    with dissolve
    ser "One day, if the world ever finds its stillness..."
    ser "When the wars are quiet, and the blood has dried..."
    ser "When no child is torn from the arms that love them..."
    ser "And no voice is silenced in the name of power..."
    $ phone_time_add(minutes=10)
    scene ch2ep1_463
    with dissolve
    ser "Let someone remember me."
    ser "Not as a weapon. Not as a Number."
    play sound2 rain_heavy fadein 2 loop
    scene ch2ep1_464
    with Dissolve(2.0)
    ser "But as a girl who once stepped into the rain, hoping to feel the sun again."
    ser "— Serene Rainyday (Number Thirteen)"
    stop sound2 fadeout 2
    scene ch2ep1_465
    with dissolve
    mc "Fuck... I don't think I can finish that."
    cl "Why not? You've barely read the first page."
    scene ch2ep1_466
    with dissolve
    mc "Because I've got enough crawling around in my head already. I don't need to add hers to the pile."
    cl "So now you're spiraling?"
    mc "... Not exactly. Not yet. Maybe."
    cl "Can you please be clearer?"
    scene ch2ep1_467
    with dissolve
    mc "The way she wrote it... it feels too close. Some days I don't feel like myself at all. Like I'm wearing someone else's skin."
    mc "And when I look in the mirror, it isn't even me staring back. It's warped. Like glass that won't stay still."
    cl "Literal, or just a metaphor?"
    mc "Literal."
    cl "Strange... I've never logged a case like that."
    cl "Serene's kind of dissonance was common—people struggling to reconcile who they were with what the serum forced on them."
    cl "But you..."
    scene ch2ep1_469
    with dissolve
    cl "... When did it start?"
    mc "A few weeks after... that incident."
    scene ch2ep1_468
    with dissolve
    cl "So... could it be the serum itself mutating?"
    cl "... I should bring this to Jess, see if—"
    scene ch2ep1_470
    with Dissolve(0.2)
    mc "No. Don't."
    cl "Keeping her out could cost you."
    mc "If I wanted her in, I wouldn't be here with you."
    cl "*sighs* This is exactly why I wanted your blood. You're the anomaly in all of us."
    cl "I've been itching to test it, but Moon makes that... inconvenient."
    scene ch2ep1_471
    with dissolve
    cl "Purely for the data, of course."
    mc "Moon's not a problem. I can—"
    play sound knifepuncture
    scene ch2ep1_472
    pause 0.5
    cl "I know. I've got your permission, don't I?"
    scene ch2ep1_473
    with dissolve
    cl "..."
    scene ch2ep1_474
    with dissolve
    cl "You didn't even blink."
    mc "It's you. I saw it coming. Though a needle would've been civilized."
    cl "Needles waste volume. I prefer raw. We heal fast enough anyway."
    scene ch2ep1_475
    with dissolve
    cl "... This should be enough."
    cl "No promises—I'm not Jess. But I'll see what I can extract."
    mc "And if you do... it stays between us."
    play sound cloth
    scene ch2ep1_476
    with dissolve
    cl "I'm good at keeping secrets. Don't worry."
    mc "What kind of secrets?"
    cl "The kind nobody benefits from dragging into the light."
    scene ch2ep1_477
    with dissolve
    cl "Perfect."
    mc "Even me?"
    scene ch2ep1_478
    with dissolve
    cl "{b}Especially{/b} you."
    play sound chairdrag
    scene ch2ep1_479
    with dissolve
    mc "..."
    scene ch2ep1_480
    with dissolve
    mc "If everything you knew was about to collapse... what would you do?"
    cl "Ugh, really? I don't do philosophical soul-searching."
    mc "First thought, no filter."
    cl "*sighs*"
    scene ch2ep1_481
    with dissolve
    cl "I'd stay put. No running."
    cl "Maybe... take someone's hand. Just to prove I wasn't going alone."
    cl "Because when things fall apart, it's not about fixing them. It's about leaving a mark that says you were there at all."
    scene ch2ep1_482
    with dissolve
    mc "Not bad for someone who hates soul-searching."
    cl "Why, thank you."
    scene ch2ep1_483
    with dissolve
    mc "So... whose hand are you picturing?"
    cl "... Lance's."
    mc "..."
    mc "You two...?"
    scene ch2ep1_484
    with dissolve
    cl "If you're angling for romance gossip, don't. I like him, that's all. That's enough for me."
    mc "Got it."
    cl "Now go back to whatever corner you came from. I'll reach out if I find anything useful."
    scene ch2ep1_485
    with dissolve
    mc "Can I borrow her book?"
    play sound cloth2
    scene ch2ep1_486
    cl "No."
    mc "Please. Just a couple of days."
    cl "Bring it back tomorrow with the moon, the receipt tucked in, and every page breathing."
    mc "... What?"
    scene ch2ep1_487
    with dissolve
    cl "You can borrow anything else in here. Not this. Even you don't get to walk out with it."
    yt "Strange. She never guards things this tightly. Best not to push."
    mc "*sighs* Fine. I'll read it here."
    stop music2 fadeout 2

    scene black
    with dissolve
    with fade

    $ phone_time_add(hours=1)
    play music 'audio/EsLullaby.mp3'
    play sound wallclock_rev loop
    scene ch2ep1_488
    with dissolve
    pause
    scene ch2ep1_489
    with dissolve
    mc "Why do you keep showing up? Who are you supposed to be?"
    scene ch2ep1_490
    with dissolve
    eee "Nothing fixed. Just a frame your head sketches in when it has nowhere else to put me."
    mc "Then why you? Why this shape?"
    scene ch2ep1_491
    with dissolve
    eee "Because you gave it to me."
    mc "This dream... I don't even know what this place is..."
    scene ch2ep1_492
    with dissolve
    eee "Not a dream. Not quite."
    eee "Part of you keeps clawing its way {i}there{/i}—and when it slips, you fall here instead."
    mc "There? Where?"
    eee "Don't ask me. I don't store answers. I sift what you've already buried."
    eee "What you face, I face. What you turn away from, I can't reach."
    eee "This room is the boundary of your existence. A manifestation of where the tethers separating mind and body become slowly undone."
    scene ch2ep1_493
    with Dissolve(0.2)
    mc "What—"
    scene ch2ep1_492
    with Dissolve(0.1)
    eee "Careful."
    eee "Every step is a little surrender."
    scene ch2ep1_494
    with dissolve
    eee "Sit here... and the past stops following you. Whatever you were before doesn't get up again."
    stop sound fadeout 1
    play sound2 kei_fromdream
    scene black
    with Dissolve(0.1)
    scene ch2ep1_495
    with Dissolve(0.2)
    pause
    
    scene black
    with dissolve
    with fadeq

    $ phone_time_add(minutes=4)
    play sound face_wash
    scene ch2ep1_496
    with dissolve
    pause
    stop sound fadeout 2
    scene ch2ep1_497
    with dissolve
    pause
    play sound2 waterphone4
    scene ch2ep1_498
    with Dissolve(0.2)
    pause
    mc "*exhales*"
    play sound closedoor2
    scene ch2ep1_499
    with dissolve
    mar "You good, boss?"
    mc "Mark."
    play sound2 cloth
    scene ch2ep1_500
    with dissolve
    mc "Y...yeah. I'm fine."
    mar "Sure about that? Looked like you were about to cave that sink in."
    mc "Tempting. But pipes cost more than I make in a week."
    scene ch2ep1_501
    with dissolve
    mar "Especially with us patching roofs for two shelters and a halfway house."
    mc "How's that circus going?"
    mar "Same as always—slow, broke, and now apparently housing half the city's cats."
    mc "Cats?"
    scene ch2ep1_502
    with dissolve
    mar "Yeah. Kids keep sneaking them in. One of them even named his after you. Calls it \"Felis [mc]us\"."
    mc "*chuckles* Great. Didn't know I was a hit with the under-twelve crowd."
    mar "Feels less like a shelter, more like a petting zoo."
    mc "Still beats what we used to run."
    mar "Can't argue with that."
    scene ch2ep1_503
    with dissolve
    mar "Oh, food drive next weekend. We're bleeding volunteers again."
    mc "Put me down."
    mar "You sure? Last time you nearly keeled over hauling rice bags."
    mc "*laughs* I need something to keep me busy."
    scene ch2ep1_504
    with dissolve
    mar "Or you could just sleep. I'll dig up extra hands."
    mc "Fair enough. My plate's full the next few weeks anyway."
    mar "I'll cover you, boss."
    play sound cloth2
    scene ch2ep1_505
    with Dissolve(0.2)
    mar "And, boss?"
    mc "Hm?"
    mar "Try sleeping normal hours for once."
    mc "Define \"normal.\""
    mar "The kind where you don't stare down your own reflection like it's some kind of monster."
    play sound closedoor
    scene ch2ep1_506
    with dissolve
    pause
    scene ch2ep1_507
    with dissolve
    yt "Normal, huh...?"
    $ phone_time_add(minutes=2)
    stop music fadeout 2
    scene black
    with dissolve
    scene ch2ep1_508
    with dissolve
    yt "I came here to see if Aine had handled things for me, and the first thing I did was pass out."
    mc "..."
    yt "Or was it actually sleep?"
    scene ch2ep1_509
    with dissolve
    mc "..."
    play sound papermovement
    scene ch2ep1_510
    with dissolve
    mc "A letter? From who?"
    scene ch2ep1_511
    with dissolve
    mc "Mark?"
    scene ch2ep1_512
    with dissolve
    pause
    play sound chair2
    scene ch2ep1_513
    with dissolve
    pause
    play sound papermovement2
    scene ch2ep1_514
    with dissolve
    pause
    yt "Funny how I always instantly recognize your handwriting the second I see it."
    play music 'audio/OhHolyNight.mp3'
    scene ch2ep1_515
    with dissolve
    if gwenroute:
        g "[mc], my love."
        g "I'm sorry. I swore I'd be there for your birthday, and now it's slipping out of my hands."
        g "I marked it everywhere—on my phone, on the calendar, even scrawled it on my hand like a kid. And still... here I am, failing you."
        g "Every morning I tell myself, \"Book the flight today.\" Yet when day turns to night, the hours get stolen away by fate."
        g "I know you'll shrug it off, say it's fine. But it isn't. Not for me."
        g "I hate that a promise as small as showing up feels impossible from here."
        g "I wanted to see your face when you catch me in the crowd. To bring the cake myself, even if I sing off-key and you laugh at me for it."
        g "I wanted to be there in the room—not on a screen, not in a letter."
        g "Please don't take my absence as forgetting. You've never slipped my mind, not even for a moment."
        g "When I can, I'll come back. And once I do, I'll make up for every day I wasn't at your side."
        g "—Your Gwen."
    else:
        g "Hey, [mc]."
        g "I owe you an apology."
        g "Your birthday's right around the corner, and I swore I'd be there."
        g "I plastered the date everywhere—on my phone, on the fridge, even on scraps of paper."
        g "I wanted to bang on your door and give you hell for getting older without me."
        g "But it's not happening this time. Work's chewing me up, and the pile never stops growing."
        g "Every morning I think, \"Book the flight today.\" But when day becomes night, I've already run out of hours."
        g "I know you'll wave it off, but it doesn't sit right with me."
        g "On your day, I should be there. Not in a message. Not in an excuse."
        g "I wanted to show up with the cake in my hands and laugh when you groan about the singing."
        g "Don't mistake this for me forgetting—you've been on my mind more than ever."
        g "I can't promise when, but once I do get there, it won't just be to drop in—it'll be to stay awhile."
        g "Happy birthday, [mc]. Even from here, I'm with you."
        g "—Gwen."

    scene ch2ep1_516
    with Dissolve(2.0)
    mc "..."
    play sound cloth2
    scene ch2ep1_517
    with Dissolve(0.1)
    g "Guess who."
    mc "As if asking will make me forget how beautiful that voice is."
    play sound cloth
    scene ch2ep1_518
    with dissolve
    pause
    scene ch2ep1_519
    with dissolve
    g "Surprise."
    if gwenroute:
        label gwencumback:
        if _in_replay:
            $ name = persistent.gallery_name
            play music 'audio/OhHolyNight.mp3'
        scene ch2ep1_520
        with dissolve
        pause
        play sound cloth2
        scene ch2ep1_521
        with hpunch
        mc "You have no idea how damn happy I am to see you right now."
        scene ch2ep1_522
        with dissolve
        g "That much, huh?"
        scene ch2ep1_523
        with dissolve
        mc "Yeah..."
        g "You okay?"
        mc "... I'm okay. Just tired. Let me hang on a little longer..."
        scene ch2ep1_524
        with dissolve
        g "Hng! Come here."
        scene ch2ep1_525
        with dissolve
        g "I don't remember you being this heavy. What've you been eating these past nine months?"
        menu:
            "Cheese it out":
                show gwencomfort
                with dissolve
                mc "When I'm not home? Mostly takeout. Whatever's quick: burgers, pizza, noodles... the kind of junk you'd nag me for."
                mc "You used to drag me out for real food. Now it's just me."
                mc "Guess I packed on weight 'cause I've been eating my sorrows... missing you across the table."
                g "Must've gone heavy on the pizza, because that was cheesy as hell."
                g "But this is a side of you I'll never get tired of."
                mc "Truth is, I've been starving for something that tastes like you."
                g "*laughs* Oh, so now you're doubling down?"
                mc "Of course. Stuffed crust and all the toppings."
                $ gwenpoint += 1
                $ renpy.notify(gwennotif)
                g "Well, I'm back now. I'll take you out as much as you like."
                mc "So..."
                mc "Those two months you went quiet..."
                mc "I kept wondering if I was saying too much. Or not enough."
                g "*laughs softly* You were perfect."
                g "I read every message. Every dumb joke. Every late-night check-in."
                g "Sometimes I'd reread them just to hear your voice in my head."
                mc "Then why stay silent?"
                g "Because if I answered even once, I knew I'd crack."
                g "And I wanted this \"walking back into your life, seeing your face\" to land."
                mc "That's... some dangerous self-control."
                g "I know."
                g "But it worked, didn't it?"
                mc "Yeah."
                mc "It really did."
                g "Are you mad at me?"
                mc "A little."
                mc "Mostly just relieved you're real again."
                g "Hey..."
                g "I'm proud of you, [mc]."
                mc "..."
                g "Mm. Don't you dare start crying."
                mc "I'm not."
                g "*chuckles* Almost a year later and you're still a big baby."
                mc "But I'm {i}your{/i} big baby, Gwen Wilson."
                g "Mhm."
                g "And don't you ever forget that, baby."
            "Be serious":
                show gwencomfort
                with dissolve
                mc "When I'm not home? Mostly takeout. Whatever's quick: burgers, pizza, noodles... the kind of junk you'd nag me for."
                mc "You used to drag me out for real food. Now it's just me."
                g "Well, I'm back now. I'll take you out as much as you like."
                mc "So..."
                mc "Those two months you went quiet..."
                mc "I kept wondering if I was saying too much. Or not enough."
                g "*laughs softly* You were perfect."
                g "I read every message. Every dumb joke. Every late-night check-in."
                g "Sometimes I'd reread them just to hear your voice in my head."
                mc "Then why stay silent?"
                g "Because if I answered even once, I knew I'd crack."
                g "And I wanted this \"walking back into your life, seeing your face\" to land."
                mc "That's... some dangerous self-control."
                g "I know."
                g "But it worked, didn't it?"
                mc "Yeah."
                mc "It really did."
                g "Are you mad at me?"
                mc "A little."
                mc "Mostly just relieved you're real again."
                g "Hey..."
                g "I'm proud of you, [mc]."
                mc "..."
                g "Mm. Don't you dare start crying."
                mc "I'm not."
                g "*chuckles* Almost a year later and you're still a big baby."
                mc "But I'm {i}your{/i} big baby, Gwen Wilson."
                g "Mhm."
                g "And don't you ever forget that, baby."
        scene ch2ep1_526
        with dissolve
        hide gwencomfort
        g "Oh, hey—speaking of..."
        g "I brought you something."
        mc "Oh?"
        play sound bag_rummage
        scene ch2ep1_527
        with dissolve
        pause
        stop sound fadeout 1
        scene ch2ep1_528
        with dissolve
        pause
        play sound2 cloth
        scene ch2ep1_529
        with dissolve
        pause
        scene ch2ep1_530
        with dissolve
        mc "Let me guess... the key to your heart?"
        g "Close enough. But hear me out."
        scene ch2ep1_531
        with dissolve
        g "Right now, nothing in our lives is certain."
        g "We never saw what happened to you coming... and we sure as hell can't see what's up ahead."
        g "So I want you to {b}promise{/b} me, no matter what happens, you'll keep wearing this necklace. As a reminder that I was here... that I mattered in your life."
        mc "Gwen... don't start making this sound like some kind of farewell."
        g "It's not: I'm not going anywhere. But promise me anyway."
        g "Please, [mc]."
        scene ch2ep1_532
        with dissolve
        mc "..."
        scene ch2ep1_533
        with dissolve
        mc "Alright. I promise. I'll wear it... and I'll remember you every time I do."
        scene ch2ep1_534
        with dissolve
        pause
        stop music fadeout 5
        scene ch2ep1_535
        with dissolve
        g "It's not just that. I've got one more."
        mc "Please don't tell me it's another doomsday premonition."
        g "*chuckles* No, nothing like that. This one's a real surprise. The best kind of souvenir."
        g "But you'll have to turn around for me. I'll tell you when."
        scene ch2ep1_536
        with dissolve
        mc "Alright..."
        play sound belt
        play sound2 cloth
        pause
        scene ch2ep1_537
        with dissolve
        play music 'audio/SexyNight.mp3'
        g "Okay... {b}when{/b}."
        scene ch2ep1_538
        with Dissolve(2.0)
        pause
        mc "*whistles* Damn... you weren't kidding. That really is the best kind of souvenir."
        scene ch2ep1_539
        with dissolve
        g "By god... no one could ever guess how much I've missed your touch. And I'm not going to start my days back in your arms without it."
        "You pause for a long second, letting out a low wolf whistle as you drink in the sight before you."
        scene ch2ep1_540
        with dissolve
        "Gwen weaves her way across the table, slow and deliberate, her ocean-deep eyes locking onto yours."
        yt "She's drowning me without even trying."
        mc "Gwen..."
        scene ch2ep1_541
        with dissolve
        g "Hm? Didn't you say you were craving something that tastes like me?"
        "She hasn't yet touched you, but heat already floods through your veins, restless and sharp."
        yt "Already hard..."
        yt "That's the Gwen effect. Always has been."
        mc "I was."
        yt "Truth is, some things never change. She'll always have me like this, right in the palm of her hand."
        scene ch2ep1_542
        with dissolve
        "Gwen tilts her head, a playful frown tugging at her lips as she spreads her legs atop the table."
        yt "She sits there like she owns the world—and God, she does."
        g "Was?"
        mc "What a view... Fuck, Gwen."
        scene ch2ep1_543
        with dissolve
        "Her folds glisten before you, raw temptation in its purest form—the very thing you've been craving all this time."
        "Gwen hums softly, tilting her head just so."
        scene ch2ep1_544
        with dissolve
        g "Why settle for anything else when you have the real deal right in front of you?"
        "Tantalizingly, she slowly draws a finger along her labia, tracing the soft bumps of the arousal-slicked skin."
        scene ch2ep1_545
        with dissolve
        "Never breaking her smoldering gaze, she brings her fingers to her mouth, licking them clean with purposeful, elongated strokes of her tongue."
        g "Care for a taste?"
        g "Then strip for me."
        menu:
            "Take off your clothes":
                play sound cloth
                scene ch2ep1_546
                with dissolve
                g "That's a good boy..."
                mc "Let's see how long you'll be calling me that."
                g "Mm, challenging. Just how I like it."
                scene ch2ep1_547
                with dissolve
                "She sits up, hands gliding from your chest down to your cock, slow and possessive."
                g "Your turn. Let me take care of you."
            "Don't do anything":
                play sound cloth
                scene ch2ep1_548
                with dissolve
                "Gwen leans in, closing the remaining distance between you."
                "Her fingers hook into the hem of your shirt, tugging you closer before her lips trail teasing kisses across your chest as she works your buttons loose."
                mc "Mmm... Gwen, yeah..."
                g "You like that, don't you?"
                scene ch2ep1_547
                with dissolve
                "You can only hum in response—until Gwen shocks you with a sudden stroke your cock."
                g "Naughty boy... won't even undress when I tell him to."
                "You barely notice when she slips your shirt free, leaving your upper body bare before her hungry eyes."
        scene ch2ep1_549
        with dissolve
        "You don't waste a second. You crash into her lips, kissing her deep, greedy, while your hands roam every inch of her, desperate to reacquaint themselves with her pearly skin."
        yt "God, I've missed her. How long's it been?"
        "Gwen exhales when your mouths part, but you dive back in without hesitation."
        scene ch2ep1_550
        with dissolve
        "Your lips trail down her jaw to her neck, marking her skin with crimson love-bites that bloom like bruised roses."
        "Gwen moans, tilting her head to grant you more of her throat."
        g "Was that a bite? Hnngh... ahh..."
        mc "Yeah? Consider it my answer to your question."
        show gwen28
        with dissolve
        "Her fingers claw at the table's edges as you finally claim her breasts."
        g "Ngh... W-what question?"
        "Your mouth peppers kisses along the swell of her chest as your hands tease her nipples: circling, pinching, coaxing every twitch from her."
        "Gwen's head tips back, a sharp gasp spilling from her lips."
        g "Ah—yeah, [mc]!"
        mc "I've been starving for a taste of you..."
        "To punctuate your point, you nip the curve of her lower bust as your fingers twist her teat, leaving possessive marks on her sensitive skin."
        g "Ahh!!"
        mc "How dare you keep me hungry for so long. Don't you know the effect you have on me?"
        "Your hands give way to your mouth, tongue swirling, lips sucking her hardened gumdrop like a sweet you refuse to let go to waste."
        yt "She's always been eye candy... but fuck, nothing compares to this."
        "You don't stop, hands kneading and rolling as your mouth feasts."
        g "[mc]—! Nghhh—ahhh...!"
        "You bend over the table as Gwen leans back further, gasping and grasping for something to hold onto."
        yt "Damn, I've missed how sensitive she is."
        play sound glasshit
        scene ch2ep1_551
        with hpunch
        hide gwen28
        "Your hand slides down her waist, which molds perfectly into your palm."
        "Gwen lies sprawled across the table, flushed pink, skin blotched with crimson—spent, yet still radiant."
        "She heaves as you pause, head tipped back and chest glistening."
        scene ch2ep1_552
        with dissolve
        mc "You look so damn good, Gwen... perfect."
        g "Then ravish me, [mc]."
        mc "Don't mind if I do."
        show gwen29
        with dissolve
        "Your eyes flick down to Gwen's soaked pussy."
        "You lock her in place as you guide your hardened staff against her folds."
        "The instant your tip brushes through her wetness, a jolt of tingling fire shoots straight to your core."
        mc "You're dripping."
        g "Really? I hadn't noticed."
        "You grin, flexing your cock to make Gwen shudder beneath you, breath catching."
        g "R-right there—ahh...!"
        mc "How about now?"
        g "M-maybe a bit..."
        mc "Hard to tell who needed this more: you, or me."
        g "M-maybe we both did."
        g "*chuckles* Nghh-now less talking, more cocking."
        mc "Yes, ma'am."
        show gwen30
        with dissolve
        hide gwen29
        "Your tip nudges her clit, slick and swollen."
        "Her reaction spurs you on, making you drag your cock harder and faster along her slit."
        g "Oh my god, [mc]...! Hnghhh—ahhh!!!"
        "You tighten your grip on her hips, holding her steady as you grind against her with reckless rhythm."
        play sound cloth2
        scene ch2ep1_553
        with Dissolve(0.1)
        hide gwen30
        "Bending low, you steal another kiss. She kisses back messy and desperate, arms curling tight around your neck."
        scene ch2ep1_554
        with dissolve
        mc "Not yet."
        g "You're insane..."
        "Her whisper shivers against your lips."
        scene ch2ep1_555
        with dissolve
        "You hook her legs over your shoulders, positioning yourself as you finally push inside."
        show gwen31
        with dissolve
        g "Shit!"
        mc "So damn tight... how long's it been?"
        g "T-too long..."
        g "Please... [mc], ngh... faster..."
        "You don't respond. In fact, you pretend to ignore her, keeping your pace slow, steady, almost taunting."
        g "Fuck, heavens... I'm going to go crazy at this pace. Hngh... loosen me up already!"
        mc "So eager, are we? We've been apart for so long, so what's a few more minutes of waiting?"
        "Gwen's face flushes, brows knitting in frustration."
        g "Stop teasing me!"
        play sound cloth2
        scene ch2ep1_556
        with hpunch
        hide gwen31
        "You're caught off guard when her legs hook around you, yanking you closer until you're right against her."
        g "Now move, you ass."
        show gwen32
        with dissolve
        "You smirk as you obey, hips snapping fast and deep."
        mc "Your wish is my command."
        g "Urgh—!"
        g "That's so... corny—ngh... ahh...!"
        show gwen33
        with dissolve
        hide gwen32
        mc "You love it, don't lie."
        g "J-just because you were my first and only, d-mmh... don't get too cocky!"
        mc "But isn't that exactly what I'm doing now?"
        g "... You're-nghh... you're impossible..."
        show gwen34
        with dissolve
        hide gwen33
        g "Yeah—right there—!! Ahhh... nghh...!!"
        mc "God, Gwen, you feel so good... urgh..."
        g "Ugh, [mc]...!! I-I'm close...!"
        mc "M-me too—!!"
        play sound glasshit
        scene ch2ep1_557
        with hpunch
        hide gwen34
        g "HAAAAHNG~!"
        "You pull out just as release surges through you, hot and heavy." 
        scene ch2ep1_558
        with dissolve
        "Your cum, mixed with her own, spills over her, leaving her body dripping with the emulsion you've made together."
        g "What a mess..."
        mc "A beautiful mess, isn't it?"
        g "Indeed..."
        play sound cloth2
        scene ch2ep1_559
        "Before you can reply, Gwen pushes herself up from the table."
        "She loops her arms around your neck again, legs clinging tight around your waist."
        mc "Wha—"
        scene ch2ep1_560
        with dissolve
        g "Why don't we take things over there?"
        "You follow her gaze toward the long meeting table."
        scene ch2ep1_561
        with dissolve
        mc "You sure you're not worn out yet?"
        g "You're gonna put it in deep. No warmups, no playing around."
        g "Shove that dick so hard and far into me that I have to crawl to get anywhere tomorrow."
        g "Do you understand?"
        "She doesn't answer—instead, she gives an order."
        "You can't help the grin tugging at your lips—awed by the raw command in her voice."
        mc "As the lady wishes."
        scene ch2ep1_562
        with dissolve
        "You scoop her up, carrying her over to where she gestured."
        yt "Right. It'll take a hell of a lot more than that to wear her out."
        yt "I know her rhythms by heart—the little tells, the way she moves, the sparks in her eyes."
        yt "Every second with her feels fully rehearsed, yet brand new all at once."
        yt "I've been aching for this, and finally, she's here now, within reach... mine to hold, mine to keep."
        scene ch2ep1_563
        with dissolve
        "You set Gwen down gently; her body spreads out on the polished surface, ready for you again."
        scene ch2ep1_564
        with dissolve
        "She bites her finger, eyes raking over you, before poking the tip of your cock with a sly grin."
        mc "*groans* Gwen..."
        g "Yes, [mc]?"
        scene ch2ep1_565
        with dissolve
        "Overwhelmed, you grab her hand, urging her strokes along your shaft."
        g "Ooh... impatient, are we?"
        g "Fine."
        scene ch2ep1_566
        with dissolve
        "Gwen slips from the table and drops to her knees."
        g "Now... use me."
        scene ch2ep1_567
        with dissolve
        "She smirks before swallowing you whole in one smooth, wicked motion."
        show gwen35
        with dissolve
        "Your hand finds the back of her head, fingers threading through her hair as you guide her rhythm."
        mc "Fuck! Ah, Gwen..."
        "Gwen mumbles something incoherent, her mouth full of you."
        g "Mhmm... hmmff..."
        "Her tongue swirls along your shaft as her head bobs in a rhythm that drives chills up your spine."
        "Your head tips back, breath ragged."
        mc "I'm—shit, I'm close... holy fuck, Gwen... yeah, just like that—!!"
        show gwen36
        with dissolve
        hide gwen35
        "The pace quickens, every stroke wetter, messier, until you're delirious."
        "And the pressure-it builds fast... too fast."
        show gwen37
        with dissolve
        hide gwen36
        "You can't help but move with the tempo, hips twitching to meet her lips, dragged along compulsively by the pleasure."
        mc "I'm gonna—ahh—Gwen, ngh, yes... there!"
        play sound cloth2
        scene ch2ep1_568
        hide gwen37
        "You push her down, burying yourself deep into her oral cavity as your release floods into her throat."
        scene ch2ep1_569
        with dissolve
        "Gwen looks up, a devious, cum-stained grin on her face."
        "Locking eyes with you, she takes just one gulp, vanishing your load down her gullet."
        "She pulls back, wiping her lips with the back of her hand."
        g "Hell, that's hot... damn, you really wanted to fill me up."
        "Not dwelling on the meal you fed her, Gwen cocks her head."
        g "Say [mc], I know I told you I wanted to do it here..."
        scene ch2ep1_570
        with dissolve
        g "... but how about over there? My back's killing me."
        g "And right now, my body's begging to feel you deeper."
        "Her eyes flick toward the sofa behind you. You don't hesitate, lifting her with ease."
        play sound chair
        scene ch2ep1_571
        with hpunch
        g "Ah!"
        "She lets out a soft squeal, then a louder one once you flip her onto her stomach across the cushions."
        "Gwen glances back at you, lips parted, eyes burning."
        g "I can't see you like this."
        mc "Don't worry. This won't take long."
        "You slide your cock between her thighs, finding her entrance. With a slow press, you sink inside."
        mc "You good?"
        g "With you? Never been better."
        show gwen38
        with dissolve
        g "Ohhh! Yes, [mc]...!!"
        "You grab one of her wrists, pinning it behind her like a cop arresting a suspect."
        "And then drive into her—hard."
        mc "I'll pick up the pace... if you can handle it."
        g "Mhm... nghhh..."
        "Her face sinks into the sofa as she moans, muffled but sharp with need. And that's all you need to hear."
        show gwen39
        with dissolve
        hide gwen38
        g "Nghhh! Ahhh..!!"
        g "You're so hard... ohhh, fuck!"
        mc "You're taking me so damn well..."
        g "I missed this—I missed {i}you{/i}... nghh, ahhh..."
        g "Deeper...!! Faster, [mc]...!"
        g "Yes, right there—ahh, fuck—!!"
        show gwen40
        with dissolve
        hide gwen39
        "You lift her hips at the perfect angle. With her back arched, every thrust sinks completely inside."
        g "Fuck—!! You feel so good—ahhh!!!"
        g "God... holy shit, nghhh!!!"
        mc "Gwen..."
        "Her cries turn breathless, overwhelmed."
        g "Yes—fuck, yes!!"
        g "I wish I could see your face right now... nghhh...!!"
        g "Are you close? Ahh... Please say you are..."
        mc "With your pussy swallowing me like that, what do you think?"
        g "Such a way with words... Cum with me, [mc]!"
        play sound cloth
        scene ch2ep1_572
        with Dissolve(0.2)
        hide gwen40
        "Shaking, you pull her up as the edge crashes over you."
        "Gwen clings to you, trembling as you sit back and she straddles your lap."
        g "Nghhh... more..."
        show gwen41
        with dissolve
        "Her hips rise and fall, grinding you deep as she holds you."
        g "[mc]... Can you feel me? Talk to me..."
        mc "Gwen... ahhh... so fucking good. Don't stop—ahhh!!"
        "You match her rhythm, lifting to meet her."
        show gwen42
        with dissolve
        hide gwen41
        g "Mmmffhh... ohhh..."
        mc "Nghhh... ahhh..."
        "Your rhythm builds, both of you clinging like you'll shatter if you let go."
        show gwen43
        with dissolve
        hide gwen42
        g "Inside... ahhh..."
        mc "Fuck—yeah... I'm close!"
        g "Me too... ohhh!!"
        "You feel the strongest climax yet tear through you as you buck your hips with full force."
        play sound chair
        scene ch2ep1_573
        with hpunch
        hide gwen43
        g "Ahhh—!!"
        "With one final thrust, you spill into her. She locks down tight around you, both of you rocking through release."
        scene ch2ep1_574
        with hpunch
        mc "*groans* Ohhh...!!"
        "Your cock stays buried as the warmth spills out, dripping from her as she quakes."
        scene ch2ep1_575
        with dissolve
        "Spent, Gwen collapses into your chest, nuzzling your neck."
        g "God... that was insane..."
        mc "You felt incredible..."
        g "Mhm... you too..."
        "You feel her smile as she murmurs against your skin."
        g "I really, REALLY missed you."
        mc "*chuckles* Welcome home."
        scene ch2ep1_576
        with dissolve
        g "Still hungry?"
        mc "If it's you on the menu..."
        g "Of course it is, Mr. Smooth-talker."
        scene ch2ep1_577
        with dissolve
        mc "... You're not going back overseas anytime soon, are you?"
        g "Not soon, and not anymore. That was a one-time thing."
        scene ch2ep1_578
        with dissolve
        mc "How did it go?"
        g "Well, it looks like it's gonna take a while if we want to expand the company abroad."
        mc "Paperwork?"
        g "Paperwork. Meetings. Licensing. A whole parade of people nodding along and saying, \"let's circle back to this.\""
        mc "Sounds like your typical corporate speak."
        scene ch2ep1_579
        with dissolve
        g "Mm-hm. And you know Klara—patience isn't exactly her strong suit. She wants everything done ASAP."
        mc "And you?"
        g "I keep reminding her we're not running a corner store anymore. Expansion's a marathon. Push too fast and we bleed money."
        mc "Listen to you, sounding like a real VP."
        g "Half my job's just making sure Klara doesn't launch a chair across the room whenever I call her."
        scene ch2ep1_580
        with dissolve
        mc "*laughs* That sounds like her."
        g "It actually happened once."
        g "Remember those wooden chairs we put in her room? Yeah."
        mc "... So what did you do?"
        g "What else? Nothing. I get things done, but I hate the drama. I'd rather keep everyone's masks intact."
        mc "Sounds draining."
        g "It is. But it's ours. We built this from scratch—I can't just walk away."
        scene ch2ep1_581
        with dissolve
        g "Besides... it feels good proving I can stand my ground, even in a room full of suits who think I don't belong there because of my record."
        mc "You've always belonged there, Gwen."
        g "... Thanks."
        if allornothingroute:
            scene ch2ep1_582
            with dissolve
            g "Klara scrapped the trip anyway, so I'm off the hook from that whole work-travel nightmare. At least now we've got a clear picture of what we're dealing with."
            g "Honestly, I'm almost impressed she still manages to get things done while barricading herself in her room."
            stop music
            play sound closedoor2
            scene ch2ep1_583
            with Dissolve(0.2)
            pause
            play music 'audio/Travellin.mp3'
            scene ch2ep1_584
            with Dissolve(0.2)
            a "Oh, for fuck's sake...!"
            play sound bag_rummage
            scene ch2ep1_585
            with dissolve
            g "Well, look who finally crawled out of the shed. I was about ready to file a missing person report after you ghosted my texts for weeks."
            a "Nice to see you too."
            play sound woosh2
            scene ch2ep1_586
            with Dissolve(0.1)
            pause 0.7
            play sound2 cloth2
            scene ch2ep1_587
            pause 0.5
            a "What's this?"
            g "Souvenir."
            play sound cloth
            play sound2 belt
            scene ch2ep1_588
            with dissolve
            g "Wouldn't want you thinking I've {i}{b}forgotten{/b}{/i} you... even if you've clearly forgotten about me."
            a "I've been busy, you buttermilk."
            scene ch2ep1_589
            with dissolve
            g "Then where's my welcome-back kiss?"
            a "Ugh... Would you like fronthand, or backhand?"
            a "And clean yourself up first, idiot. Restroom's down the hall to the left."
            scene ch2ep1_590
            with dissolve
            mc "*chuckles* Man... I missed watching you two bicker over nothing."
            a "You too! Dress up, at least!"
            mc "Alright, alright..."
            scene ch2ep1_591
            with dissolve
            pause
            scene ch2ep1_592
            with dissolve
            a "Hey, Gwen."
            g "Yeah?"
            a "... Welcome back. And thanks."
            scene ch2ep1_593
            with dissolve
            g "Good enough."
            play sound closedoor2
            scene ch2ep1_594
            with dissolve
            a "*exhales deeply*"
            stop music fadeout 5
            play music2 'audio/Togetherness.mp3' fadein 5
            play sound3 cloth
            scene ch2ep1_595
            with dissolve
            a "Anyway... you okay?"
            mc "Whoa, where's this coming from?"
            play sound chair2
            scene ch2ep1_596
            with dissolve
            a "[mc]... we've been together long enough that I can spot even your subtlest tells."
            mc "You mean the paperwork?"
            a "The paperwork."
            scene ch2ep1_597
            with dissolve
            mc "Yeah. I'm fine. Just... still getting used to juggling two jobs at once."
            a "Maybe that wasn't the smartest move. Let me take more of the load here."
            mc "Aren't you already doing that?"
            a "Nope, only half."
            mc "I'll be fine, Aine. If you can handle it, I can handle it too."
            scene ch2ep1_598
            with dissolve
            mc "..."
            a "Oh—that? I was on my way to Emma's office. Sky said she skipped breakfast again."
            scene ch2ep1_599
            with dissolve
            mc "You know she doesn't like visitors."
            a "Yeah, I remember."
            mc "Let me take it."
            a "... Actually, that's a great idea. She's more lenient when you drop by her office."
            mc "..."
            scene ch2ep1_600
            with dissolve
            mc "See something you like?"
            a "No, I—uh, no. I've got work to do."
            mc "You sure you don't wanna come with me?"
            scene ch2ep1_601
            with dissolve
            a "I'll {i}cum{/i} with you as many times as you want, cheese ball—"
            play sound cloth2
            scene ch2ep1_602
            a "You know what? Just go! Get out of here!"
            mc "Alright, alright."
        else:
            g "Klara scrapped the trip anyway, so I'm off the hook from that whole work-travel nightmare. At least now we've got a clear picture of what we're dealing with."
            g "Honestly, I'm almost impressed she still manages to get things done while barricading herself in her room."
            scene ch2ep1_603
            with dissolve
            mc "Yeah... not exactly shocking, but honestly, it could've been worse."
            scene ch2ep1_604
            with dissolve
            mc "Anyway, forget about her for now. I'm just glad you're back."
            scene ch2ep1_605
            with dissolve
            g "And I'm glad to be back."
            mc "You should probably freshen up."
            scene ch2ep1_606
            with dissolve
            g "Good idea. I'll be back real quick."
            play sound cloth
            play sound2 belt
            scene ch2ep1_607
            with dissolve
            mc "Place has changed a bit since you were last here. Restroom's down the hall to the left."
            g "Got it."
            stop music fadeout 5
            play sound3 closedoor2
            scene ch2ep1_608
            with dissolve
            pause
            play music2 'audio/Togetherness.mp3' fadein 5
            play sound opendoor2
            scene ch2ep1_609
            with dissolve
            pause
            play sound2 chair
            scene ch2ep1_610
            with dissolve
            a "... Okay, am I losing my mind, or did Gwen's ghost just stroll past me in the hall? Pretty sure I even heard it talking."
            mc "Oh, god... what did it say?"
            scene ch2ep1_611
            with dissolve
            a "It said, \"I've got a souvenir for you in my bag.\"" 
            mc "... I can't tell if you're being sarcastic or having a stroke right now."
            scene ch2ep1_612
            with dissolve
            a "Wait—"
            a "She's back?!"
            mc "Go ask the ghost yourself."
            a "*sighs* I can talk to her later..."
            scene ch2ep1_613
            with dissolve
            a "Anyway... you okay?"
            mc "Whoa, where's this coming from?"
            a "[mc]... we've been around each other long enough that I can spot even your smallest tells."
            mc "You mean the paperwork?"
            a "The paperwork."
            mc "Yeah. I'm fine. Just... still getting used to juggling two jobs at once."
            a "Maybe that wasn't the smartest move. Let me take more of the load."
            mc "Aren't you already doing that?"
            a "Nope, only half."
            mc "I'll be fine, Aine. If you can handle it, I can handle it too."
            scene ch2ep1_614
            with dissolve
            mc "..."
            a "Oh—that? I was on my way to Emma's office. Sky said she skipped breakfast again."
            scene ch2ep1_615
            with dissolve
            mc "You know she doesn't like visitors."
            a "Yeah, I remember."
            mc "Let me take it."
            a "... Actually, that's a great idea. She's more lenient when you drop by her office."
        $ renpy.end_replay()
    else:
        scene ch2ep1_616
        with dissolve
        mc "... You wrote that letter just to mess with me?"
        g "Just wanted to see how you'd react."
        mc "Oh boy..."
        scene ch2ep1_526
        with dissolve
        g "Oh, hey—speaking of..."
        g "I brought you something."
        mc "Oh?"
        play sound bag_rummage
        scene ch2ep1_527
        with dissolve
        pause
        stop sound fadeout 1
        scene ch2ep1_528
        with dissolve
        pause
        play sound cloth
        scene ch2ep1_529
        with dissolve
        pause
        scene ch2ep1_530
        with dissolve
        mc "Let me guess... the key to your heart?"
        g "Close enough. But hear me out."
        scene ch2ep1_531
        with dissolve
        g "Right now, nothing in our lives is certain."
        g "We never saw what happened to you coming... and we sure as hell can't see what's up ahead."
        g "So I want you to {b}promise{/b} me—no matter what happens—you'll keep wearing this necklace. As a reminder that I was here... that I mattered in your life."
        mc "Gwen... don't start sounding like this is some kind of farewell."
        g "It's not. I'm not going anywhere. But promise me anyway."
        g "Please, [mc]."
        scene ch2ep1_532
        with dissolve
        mc "..."
        scene ch2ep1_533
        with dissolve
        mc "Alright. I promise. I'll wear it... and I'll remember you every time I do."
        stop music fadeout 5
        play music2 'audio/Togetherness.mp3' fadein 5
        scene ch2ep1_617
        with dissolve
        mc "... But you're not going back overseas anytime soon, are you?"
        g "Not soon, and not anymore. That was a one-time thing."
        scene ch2ep1_618
        with dissolve
        mc "How did it go?"
        g "Well, it looks like it's gonna take a while if we want to expand the company abroad."
        mc "Paperwork?"
        play sound chair2
        scene ch2ep1_619
        with dissolve
        g "Paperwork. Meetings. Licensing. A whole parade of people nodding along and saying, \"let's circle back to this.\""
        mc "Sounds like your typical corporate speak."
        g "Mm-hm. And you know Klara—patience isn't exactly her strong suit. She wants everything done ASAP."
        scene ch2ep1_620
        with dissolve
        mc "And you?"
        g "I keep reminding her we're not running a corner store anymore. Expansion's a marathon. Push too fast and we bleed money."
        mc "Listen to you, sounding like a real VP."
        g "Half my job's just making sure Klara doesn't launch a chair across the room whenever I call her."
        mc "*laughs* That sounds like her."
        scene ch2ep1_621
        with dissolve
        g "It actually happened once."
        g "Remember that old wooden chair in her room? Yeah."
        mc "... So what did you do?"
        g "What else? Nothing. I get things done, but I hate the drama. I'd rather keep everyone's masks intact."
        mc "Sounds draining."
        g "It is. But it's ours. We built this from scratch—I can't just walk away."
        scene ch2ep1_622
        with dissolve
        g "Besides... it feels good proving I can stand my ground, even in a room full of suits who think I don't belong there because of my record."
        mc "You always belonged there, Gwen."
        g "... Thanks."
        scene ch2ep1_623
        with dissolve
        g "Klara scrapped the trip anyway, so I'm off the hook from that whole work-travel nightmare. At least now we've got a clear picture of what we're dealing with."
        g "Honestly, I'm almost impressed she still manages to get things done while barricading herself in her room."
        mc "Yeah... not exactly shocking, but honestly, it could've been worse."
        g "That's true..."
        g "Anyway, as much as I like boring you with corporate speak, I could really use a restroom right about now."
        mc "Place has changed a bit since you were last here. Restroom's down the hall to the left."
        g "Got it."
        play sound closedoor2
        scene ch2ep1_624
        with dissolve
        pause
        play sound2 opendoor2
        scene ch2ep1_625
        with dissolve
        pause
        scene ch2ep1_626
        with dissolve
        a "... Okay, am I losing my mind, or did Gwen's ghost just stroll past me in the hall? Pretty sure I even heard it talking."
        mc "Oh, god... what did it say?"
        a "It said, \"I've got a souvenir for you in my bag.\""
        scene ch2ep1_627
        with dissolve
        mc "... I can't tell if you're being sarcastic or having a stroke right now."
        a "Wait—"
        a "She's back?!"
        mc "Go ask the ghost yourself."
        a "*sighs* I can talk to her later..."
        scene ch2ep1_628
        with dissolve
        a "Anyway... you okay?"
        mc "Whoa, where's this coming from?"
        a "[mc]... we've been around each other long enough that I can spot even your smallest tells."
        mc "You mean the paperwork?"
        a "The paperwork."
        mc "Yeah. I'm fine. Just... still getting used to juggling two jobs at once."
        a "Maybe that wasn't the smartest move. Let me take more of the load."
        mc "Aren't you already doing that?"
        a "Nope, only half."
        mc "I'll be fine, Aine. If you can handle it, I can handle it too."
        scene ch2ep1_629
        with dissolve
        mc "..."
        a "Oh—that? I was on my way to Emma's office. Sky said she skipped breakfast again."
        scene ch2ep1_630
        with dissolve
        mc "You know she doesn't like visitors."
        a "Yeah, I remember."
        mc "Let me take it."
        a "... Actually, that's a great idea. She's more lenient when you drop by her office."

    scene black
    with dissolve
    with fade

    play sound windgrass loop
    play sound2 whistle_sport
    scene ch2ep1_655
    with dissolve
    pause
    scene ch2ep1_656
    with Dissolve(0.1)
    l "Megan! You're not even halfway through—don't tell me you're dying already!"
    meg "Ugh, spare me, Lily. Nobody's watching."
    l "I am! And when we're training, it's Coach, not Lily!"
    meg "Sure, Lily."
    scene ch2ep1_657
    with dissolve
    pause
    play sound3 weather_alert loop
    scene ch2ep1_658
    with Dissolve(0.1)
    pause
    stop sound3
    scene ch2ep1_659
    with dissolve
    l "... What's this?"
    $ renpy.music.set_volume(0.5, 1.0, "music2")
    scene ch2ep1_660
    with dissolve
    play sound2 weather_advisory1
    news "This is a final advisory from the Quinara Weather Authority."
    play sound2 weather_advisory2
    news "Tropical Storm \"Pot\" is expected to make landfall along Quinara's eastern coastline within the next two hours."
    play sound2 weather_advisory3
    news "The cities of Chardos and Estora, including the provinces of Velaris and Highmarsh, are now under the highest warning level."
    play sound2 weather_advisory4
    news "Severe winds, torrential rain, and widespread flooding are anticipated in these regions."
    play sound2 weather_advisory5
    news "Residents are urged to shelter indoors, secure belongings, and avoid travel until authorities declare it safe."
    play sound2 weather_advisory6
    news "Other areas of Quinara will experience moderate to heavy rainfall, but no evacuation orders are currently in place."
    $ renpy.music.set_volume(1.0, 1.0, "music2")
    scene ch2ep1_661
    with dissolve
    l "... Forgot to turn off the Quinara alerts."
    l "..."
    l "I hope they're safe."
    stop sound fadeout 2

    scene black
    with dissolve
    with fade

    $ phone_time_add(minutes=30)
    scene ch2ep1_631
    with dissolve
    pause
    play sound doorknock3
    scene ch2ep1_632
    with dissolve
    pause
    e "Come in."
    play sound2 opendoor2
    scene ch2ep1_633
    with dissolve
    mc "Hey."
    scene ch2ep1_634
    with Dissolve(0.2)
    e "Oh..."
    scene ch2ep1_635
    with dissolve
    mc "Figured I'd crash your cave. Haven't seen daylight on your face since yesterday."
    mc "And lately, you've been married to those case files."
    e "You know I can still kick you out?"
    mc "Yeah, but you won't. You've always had a soft spot for me."
    scene ch2ep1_636
    with dissolve
    pause
    play sound closedoor2
    scene ch2ep1_637
    with dissolve
    pause
    scene ch2ep1_638
    with dissolve
    mc "Here, breakfast and lunch."
    e "[mc]—"
    mc "Ah-ah, don't. I already know what you're about to say."
    scene ch2ep1_639
    with dissolve
    e "*soft laugh* Fine... I'll eat it all."
    mc "So... what's the damage?"
    stop music2 fadeout 4
    play music 'audio/MindGame.mp3' fadein 4
    scene ch2ep1_640
    with dissolve
    mc "Another dead end?"
    e "Mm. Yeah. Unfortunately."
    scene ch2ep1_641
    with dissolve
    e "I keep thinking I'm closing in, but every lead turns into a brick wall."
    mc "Feels like you're chasing shadows, Em. At what point do you let them go?" 
    scene ch2ep1_642
    with dissolve
    e "That's exactly why I can't stop: because as you can see, I'm still nowhere close."
    mc "Don't grind yourself down over this. It was never your responsibility."
    e "If not mine, then whose?"
    e "Saving you should've been my duty. And I didn't. I couldn't." 
    e "Why else take this job if I can't even do it right?"
    scene ch2ep1_643
    with dissolve
    mc "Nobody's ever put that blame on you."
    scene ch2ep1_644
    with Dissolve(0.2)
    e "I did."
    mc "Em... you couldn't have stopped it."
    e "I know. That's why I'm doing everything now."
    e "Even if it takes a hundred years, I'll find him."
    scene ch2ep1_645
    with dissolve
    mc "*exhales* So...? Where does that leave us?"
    e "... You're not joining my op again, are you?"
    scene ch2ep1_646
    with dissolve
    mc "Well... I dipped my toe in once. Used a contact to help you."
    scene ch2ep1_647
    with dissolve
    mc "Okay, maybe it was twice."
    scene ch2ep1_648
    with dissolve
    e "And this is why I hate you guys walking in here. You always find yourselves neck-deep before you realize how dangerous this is."
    mc "Not always, but... fair point."
    mc "But tell me, what do you actually have?"
    scene ch2ep1_649
    with dissolve
    e "*sighs* Nothing solid yet."
    e "Just rumors. Reports of people vanishing, movements across borders that don't add up."
    e "On paper, they're scattered cases. Different names, different operators."
    mc "But you think it's him."
    e "I can't prove it. But it has his fingerprints all over it."
    e "Vanishing people under cover, moving through shells... it's his style."
    scene ch2ep1_650
    with dissolve
    mc "So it's a hunch."
    e "One that won't leave me. Every missing name I read feels like another failure stamped with mine. Because he's still out there."
    mc "Em... again, you're chasing someone who knows how to disappear."
    e "*bitter laugh* Disappearing or not, someone's pulling strings. And until I'm sure it isn't him, I'm not stopping."
    scene ch2ep1_651
    with Dissolve(0.1)
    mc "Hold up..."
    mc "Em, these are all—"
    scene ch2ep1_652
    with dissolve
    e "Mm. The part that eats at me most... most of the missing are kids."
    e "Harvest? Traffic? I don't know yet."
    e "All I know is something vile is crawling through this city right now."
    scene ch2ep1_653
    with dissolve
    mc "... I don't care if it's him or not. What do you want to do?"
    scene ch2ep1_654
    with dissolve
    e "..."
    stop music fadeout 2

    scene black
    with dissolve
    with fade

    $ phone_time_add(minutes=30)
    play sound rain_heavy loop fadein 2
    play sound2 wind_gust loop fadein 2
    scene ch2ep1_662
    with dissolve
    mc "Perfect. And guess who left the umbrella at the office?"
    g "Good thing I grabbed that ticket early... didn't even know a storm was sneaking in."
    mc "Don't you have your Quinara weather alerts on?"
    g "I turned it off for... travel reasons."
    play sound3 rain_umbrella loop fadein 0.5
    scene ch2ep1_663
    with dissolve
    pause
    $ renpy.sound.set_volume(0.3, 0.5, "sound3")
    scene ch2ep1_664
    with dissolve
    mc "Well, here comes our savior."
    stop sound3 fadeout 1
    $ renpy.sound.set_volume(1.0, 1.0, "sound3")
    scene ch2ep1_665
    with dissolve
    g "Hey."
    m "'Sup! Back already, or just passing through?"
    g "Mm... plans fell apart."
    scene ch2ep1_666
    with dissolve
    mc "I swear, I've lost count of how many times you've had to rescue my dumb ass."
    scene ch2ep1_667
    with dissolve
    m "Two of you this time."
    m "And yeah... still no garage of our own."
    mc "One thing at a time."
    play sound3 rain_umbrella loop fadein 0.5
    scene ch2ep1_668
    with dissolve
    mc "Anyone else around besides you?"
    m "Doesn't look like it."
    g "Not even Shu?"
    m "Haven't seen him since morning."
    mc "Shu disappearing without a word... that's new."
    stop sound fadeout 2
    stop sound2 fadeout 2
    stop sound3 fadeout 2

    scene black
    with dissolve
    with fade

    $ phone_time_add(hours=1)
    play sound rain_bedroom loop fadein 1
    play music 'audio/LostInTheStatic.mp3' fadein 2
    scene ch2ep1_669
    with dissolve
    k "{i}Rain never asks permission. It just presses on the glass until you notice."
    k "{i}Like it knows a window's still cracked open somewhere."
    k "{i}Back then, weather like this erased me. I'd let the darkness take sound, thought... even the hours."
    scene ch2ep1_670
    with dissolve
    k "{i}I grew up breathing in this color."
    k "{i}On the worst days, it was pitch. On the better ones, a kind of washed-out gray. Never white. Never bright."
    k "{i}Then I met people who made the world look... almost lit from the inside."
    scene ch2ep1_671
    with dissolve
    k "{i}And yet, even then... I kept asking myself—"
    k "{i}Is this me? Is this who I want to be?"
    k "{i}Because when despair found me, I still looked for the dark. Every time."
    k "{i}Because it was familiar. It fit like an old coat."
    k "{i}So I learned to put on a mask instead. A face people could live with. Respectable. Palatable."
    k "{i}The real one—mine—always sent people running. In disgust. Or in fear."
    scene ch2ep1_672
    with dissolve
    k "{i}And now... there's him. He burns bright, but somehow I can look straight at him. Like his light is asking me not to turn away."
    k "{i}It doesn't hurt. It doesn't blind. It simply settles over me."
    scene ch2ep1_673
    with dissolve
    k "{i}Even silence changes shape with him. The creak of the floorboards. The hinge sighing at the door. The scrape of a plate."
    k "{i}And me... pretending I don't wait for his presence. Pretending I don't leave the door open."
    scene ch2ep1_674
    with dissolve
    k "{i}I set the tray down before my tea's even steeped. Two plates are coming. One candle I may or may not light."
    scene ch2ep1_675
    with dissolve
    k "{i}He should be here... right about now."
    play sound2 opendoor2
    scene ch2ep1_676
    with dissolve
    pause
    scene ch2ep1_677
    with dissolve
    k "{i}At this hour, he isn't tired yet. He always comes with a smile... and food that still holds its warmth."
    k "{i}And somehow..."
    k "{i}... it unsettles me."
    k "{i}Why?"
    scene ch2ep1_678
    with dissolve
    k "You're dripping on the floor."
    scene ch2ep1_679
    with dissolve
    pause 0.5
    mc "Well, if I was, I'd change. Wouldn't wanna ruin your holy dust shrine."
    k "{i}These odd little exchanges... they pull at me in ways I can't admit."
    k "That's not what I meant."
    scene ch2ep1_680
    with dissolve
    k "{i}Rain never asks permission. It just presses on the glass until you notice."
    scene ch2ep1_681
    with Dissolve(2.0)
    k "{i}And like the rain... here you are."
    play sound2 platedown
    scene ch2ep1_682
    with dissolve
    k "{i}He sets both plates down..."
    k "{i}... then sits across from me without a word—"
    play sound2 chairdrag
    scene ch2ep1_683
    with dissolve
    mc "So... not much business today. Why don't you tell me some of your pastimes?"
    scene ch2ep1_684
    with dissolve
    pause
    mc "What? Don't tell me that after all these months, you've done nothing in here?"
    k "*nods* Mm-hm."
    mc "Oh, Jesus..."
    scene ch2ep1_685
    with dissolve
    k "Time just passes. But... I do miss the piano."
    mc "Well, if we could squeeze one in here, I'd carry it myself. Heck, I'd even join you."
    scene ch2ep1_686
    with dissolve
    mc "That's why I keep saying—step outside, just once."
    mc "Just once, explore the world outside these four walls, lady."
    scene ch2ep1_687
    with dissolve
    k "Moon's at home. Why not spend your time with her instead of me?"
    menu:  
        "It's much more interesting here":
            scene ch2ep1_688
            with dissolve
            mc "I mean... I could."
            mc "But it's a lot more interesting here."
            k "There's nothing interesting here, [mc]."
            mc "Maybe. But like I said—I'd still rather be here."
        "I'd rather spend time with you":
            scene ch2ep1_688
            with dissolve
            mc "I mean... I could."
            mc "But I'd rather spend time with you."
            k "There's nothing here worth staying for, [mc]. Just dark, dull quiet."
            mc "I told you, Klara. I'd rather spend time with {i}you{/i}."
            $ klarapoint += 1
            $ renpy.notify(klaranotif)
    scene ch2ep1_689
    with dissolve
    play sound2 tablehit
    mc "*winces*" with hpunch
    mc "Damn citrus... smug little bastard. I swear that one just shaved a year off my life."
    scene ch2ep1_690
    with dissolve
    pause
    scene ch2ep1_691
    with dissolve
    k "{i}I want to ask him why. Why me. But I'm afraid of the answer..."
    k "{i}... and the truth behind it."
    stop music fadeout 2
    stop sound fadeout 2
    
    $ phone_time_add(minutes=30)
    if klararoute:
        scene black
        with dissolve
        with fade

        play music2 'audio/KlarasSonata.mp3' fadein 2
        play sound2 voices_klara_world fadein 2 loop
        scene ch2ep1_692
        with dissolve
        pause
        scene ch2ep1_693
        with Dissolve(0.2)
        kmother "{sc}{font=Beowolf.ttf}Your sister never stumbled like this. At least she made something of herself."
        scene ch2ep1_694
        with Dissolve(0.2)
        kfather "{sc}{font=Beowolf.ttf}Leaving the clan?"
        kfather "{sc}{font=Beowolf.ttf}After everything we carved into you, you're just spitting it back in our faces?"
        scene ch2ep1_695
        with Dissolve(0.2)
        kstranger "{sc}{font=Beowolf.ttf}What the hell are you supposed to be?"
        kstranger "{sc}{font=Beowolf.ttf}Don't touch me. Don't even breathe near me."
        scene ch2ep1_696
        with Dissolve(0.2)
        kteacher "{sc}{font=Beowolf.ttf}Silence again? It's disturbing. What's wrong with you?"
        scene ch2ep1_697
        with dissolve
        k "{i}Every note I held back scraped against my throat like glass."
        k "{i}Every smile I put on was a truce I never agreed to."
        k "{i}Every silence... was me slipping further out of sight."
        scene ch2ep1_698
        with dissolve
        k "{i}And even now... their voices drown out anything I could've dared to play."
        scene ch2ep1_699
        with dissolve
        k "{i}Every sharp glance, every unsaid word, still caught in me like score left hanging—"
        stop music2 fadeout 0.2
        stop sound2 fadeout 0.2
        play sound rain_bedroom fadein 0.5 loop
        scene ch2ep1_700
        with Dissolve(0.1)
        mc "The rain's not letting up anytime soon, huh?"
        scene ch2ep1_701
        with dissolve
        k "I don't want it to. Let it stay."
        scene ch2ep1_702
        with Dissolve(0.2)
        pause 0.6
        k "... Did you just roll your eyes at me?"
        scene ch2ep1_703
        with dissolve
        mc "Yeah. That was a little much."
        k "{b}{i}You{/i}{/b} started it. Stop enabling me."
        mc "I wasn't trying to. Put the fangs away."
        play sound2 cloth
        scene ch2ep1_704
        with dissolve
        k "Then what—was that your way of saying you want to leave as soon as you can?"
        scene ch2ep1_705
        with dissolve
        mc "Do you want me to?"
        k "..."
        mc "Do you?"
        k "..."
        mc "Say it."
        scene ch2ep1_706
        with dissolve
        k "{size=-15}Stay...{/size}"
        mc "Didn't catch that."
        scene ch2ep1_707
        with dissolve
        k "I want you to stay."
        scene ch2ep1_708
        with dissolve
        mc "*nods* Good."
        play sound2 tabledrag
        scene ch2ep1_709
        with dissolve
        k "What are you doing?"
        mc "Relax. Just making space."
        scene ch2ep1_710
        with dissolve
        pause 0.3
        play sound2 closedoor2
        scene ch2ep1_711
        with dissolve
        pause
        play sound3 opendoor2
        scene ch2ep1_712
        with dissolve
        mc "Bad news. Our old vinyl's shot."
        k "Our vinyl? And why would you even need that?"
        scene ch2ep1_713
        with dissolve
        mc "Doesn't matter. We'll improvise."
        $ renpy.sound.set_volume(1.0, 1.0)
        $ renpy.music.set_volume(1.0, 1.0)
        play music 'audio/LastTango.mp3'
        scene ch2ep1_714
        with Dissolve(0.2)
        mc "Since you don't have a pastime, let's make one."
        play sound2 chair
        scene ch2ep1_715
        with Dissolve(0.2)
        k "Wait—hey!"
        play sound2 woosh
        scene ch2ep1_716
        pause 0.5
        k "What the hell, [mc]?!"
        mc "Thought you'd forgotten how. Guess not."
        k "This is insane!"
        mc "And yet your hands don't look so eager to leave mine."
        k "They're here because you forced them!"
        mc "But you're holding on."
        k "Don't flatter yourself! If my back snaps, you're paying for it!"
        mc "Then I'll hold you steadier than anyone else could."
        scene ch2ep1_717
        with dissolve
        mc "See? Your body remembers—even if you'd rather it didn't."
        k "[mc]... I'm too old for this."
        mc "And yet..."
        scene ch2ep1_718
        with Dissolve(0.2)
        mc "... you're still moving with me."
        k "Only because you won't let go."
        mc "You would've fallen. Don't worry, I'd catch you anyway."
        scene ch2ep1_719
        with dissolve
        k "You shouldn't talk to me like that."
        mc "Would you rather I sound like a stranger, instead of a partner?"
        k "You're not my partner."
        mc "At this moment? I am."
        scene ch2ep1_720
        with Dissolve(0.2)
        mc "And you match me better than anyone else ever could."
        k "... Oh, [mc]... Don't make me feel like this."
        mc "Don't think. Just move. Trust me."
        scene ch2ep1_721
        with dissolve
        k "... Too close, [mc]."
        mc "Close is the whole point. You taught me that."
        k "Yes, but right now..."
        scene ch2ep1_722
        with dissolve
        k "..."
        mc "Do you want me to stop?"
        k "..."
        scene ch2ep1_723
        with dissolve
        mc "...?"
        scene ch2ep1_724
        with dissolve
        k "... Just... slow down."
        scene ch2ep1_725
        with dissolve
        mc "Alright. Hey Google, play us something easy, yeah?"
        stop music fadeout 2
        play music2 'audio/TangoInShadows.mp3' fadein 2
        pause 2.0
        scene ch2ep1_726
        with dissolve
        mc "Did my boredom get the better of me?"
        k "Just a little. Still... I like this better."
        k "... I know you were just trying to drag me back to... normalcy."
        mc "No. Not really."
        k "Then what—"
        mc "I told you. I'm not here for the food."
        k "Tea?"
        mc "Not for the tea either. You always make it too sweet."
        k "I want it sweet."
        mc "Yeah. I figured."
        scene ch2ep1_727
        with dissolve
        mc "..."
        scene ch2ep1_728
        with dissolve
        mc "I'm not here because someone told me to check in. I'm not here out of pity, either."
        mc "I'm not here to repair you, or diagnose you. You're not some problem I have to solve."
        mc "And I'm not here to pry you open like a locked door."
        play sound2 fire_crackle loop fadein 0.5
        scene ch2ep1_729
        with dissolve
        pause
        stop sound2 fadeout 1
        scene ch2ep1_730
        with dissolve
        mc "I'm here because... this is the only room that doesn't feel empty when I walk into it."
        mc "Even when you don't say a word... it still feels like you're saying something."
        scene ch2ep1_731
        with dissolve
        k "... Again, you shouldn't say things like that. It makes me want to believe them."
        mc "Then believe."
        scene ch2ep1_732
        with dissolve
        mc "This past year... this room's been my salvation."
        mc "I wasn't longing for the dark, but I was searching for the quiet. For your kind of presence."
        mc "*chuckles softly* There's nothing better than the kind of comfort I grew up craving."
        mc "This is the one place that doesn't drag me back into the bad dreams, that doesn't pull me back to the past."
        mc "I like it here. I like being here... with you. And I'm glad you keep the door open for me."
        scene ch2ep1_733
        with dissolve
        k "[mc], I—"
        mc "I know... I know."
        mc "I don't care what anyone else thinks. I don't care how they paint you."
        mc "You're not perfect—and who even wants perfect?"
        mc "I don't know which Klara's real—the one here, or the one \"they\" think they know—but I love them both just the same."
        mc "And I'd still keep coming back here, just the same."
        stop sound fadeout 2
        stop music2 fadeout 7
        play sound2 voices_klara_world fadein 2 loop
        scene ch2ep1_734
        with dissolve
        pause 0.3
        scene ch2ep1_735
        with Dissolve(0.2)
        kmother "{sc}{font=Beowolf.ttf}Your sister never stumbled like this. At least she made something of herself."
        scene ch2ep1_736
        with Dissolve(0.2)
        kfather "{sc}{font=Beowolf.ttf}Leaving the clan?"
        kfather "{sc}{font=Beowolf.ttf}After everything we carved into you, you're just spitting it back in our faces?"
        k "{i}Stop..."
        scene ch2ep1_737
        with Dissolve(0.2)
        kstranger "{sc}{font=Beowolf.ttf}What the hell are you supposed to be?"
        kstranger "{sc}{font=Beowolf.ttf}Don't touch me. Don't even breathe near me."
        scene ch2ep1_738
        with Dissolve(0.2)
        kteacher "{sc}{font=Beowolf.ttf}Silence again? It's disturbing. What's wrong with you?"
        k "{i}I said—"
        k "{i}{sc}{font=Beowolf.ttf}STOP!"
        play sound chime_bell
        scene ch2ep1_739
        with Dissolve(0.2)
        pause
        stop sound2 fadeout 4
        scene ch2ep1_740
        with dissolve
        scene ch2ep1_741
        with dissolve
        scene ch2ep1_742
        with dissolve
        scene ch2ep1_743
        with dissolve
        scene ch2ep1_744
        with dissolve
        pause
        scene ch2ep1_745
        with dissolve
        k "{i}I don't understand..."
        play sound3 woosh_long
        scene ch2ep1_746
        with Dissolve(0.3)
        k "{i}Even here... you still... find me."
        play sound rain_bedroom loop fadein 2
        scene ch2ep1_747
        with dissolve
        k "... You shouldn't hold me like that. It makes it harder to pretend I don't care."
        mc "Then stop pretending." with Dissolve(2.0)
        scene ch2ep1_748
        pause 0.3
        play sound2 wallclock_rev_once
        scene ch2ep1_749
        pause 1.0
        play music ["<from 33.2 to 152>audio/ConfessInTheCandlelight.mp3"]
        queue music 'audio/ConfessInTheCandlelight.mp3' loop
        scene ch2ep1_750
        pause
        play sound2 tablehit
        scene ch2ep1_751
        with hpunch
        pause
        scene ch2ep1_752
        with dissolve
        pause
        play sound3 woosh2
        scene ch2ep1_753
        with Dissolve(0.1)
        pause 0.5
        play sound2 woodhit
        scene ch2ep1_754
        with hpunch
        pause
        play sound3 bodyhit
        scene ch2ep1_755
        pause 0.5
        mc "Why now?"
        scene ch2ep1_756
        with dissolve
        k "... After a year of you sitting here, you really need to ask?"
        mc "I do. Because I've sat across from you for three hundred dinners, and you never once crossed that line."
        k "... You never left. Not once."
        mc "I told you I wouldn't."
        k "That's why."
        mc "That's not an answer."
        scene ch2ep1_757
        with dissolve
        k "It is. You outlasted me."
        k "Every morning, every night, I waited for you to stop coming. But you never did."
        k "Today... the silence was too heavy to keep pretending it meant {b}nothing{/b}."
        scene ch2ep1_758
        with dissolve
        k "And don't act like I'm the only one sitting on this, every single time you walked through that door."
        k "We're not children, [mc]. We don't get to hide behind ignorance anymore."
        scene ch2ep1_759
        with dissolve
        pause
        mc "... So, what now?"
        pause 1.0
        k "Now? Nothing."
        scene ch2ep1_760
        with dissolve
        mc "Nothing?"
        k "Don't look at me like that. You wanted the truth. You dragged it out of me. Well, now you have it."
        mc "And you expect me to just—"
        k "Leave it here."
        mc "Klara—"
        k "Don't, [mc]. If we keep tugging at this thread, the whole thing unravels."
        mc "So you'd rather go back to—?"
        k "I'd rather you go before I make a mistake I can't undo." 
        scene ch2ep1_761
        with Dissolve(0.2)
        pause 0.3
        play sound2 wallclock_once_1
        scene ch2ep1_762
        pause 0.5
        scene ch2ep1_763
        with Dissolve(0.3)
        mc "... That's it?"
        k "Mm... that's it."
        mc "Fine."
        play sound2 closedoor2
        scene ch2ep1_764
        with dissolve
        pause
        $ renpy.music.set_volume(0.3, 1.0)
        stop sound fadeout 2
        play sound2 voices_klara_world fadein 2 loop
        scene ch2ep1_765
        with dissolve
        kmother "{sc}{font=Beowolf.ttf}He'll leave too. That's what they do when the recital ends."
        kstranger "{sc}{font=Beowolf.ttf}Quiet looks better on you. Keep it that way."
        $ renpy.music.set_volume(1.0, 1.0)
        stop sound2 fadeout 1
        play sound rain_bedroom loop fadein 1
        scene ch2ep1_766
        with dissolve
        k "The chair still remembers your weight... and I hate that I'm jealous of it."
        scene ch2ep1_767
        with dissolve
        k "If I had a drink left, I'd raise it to my own stupidity."
        scene ch2ep1_768
        with dissolve
        k "... Why does it have to be you?"
        stop music fadeout 2
        stop sound fadeout 2

        scene black
        with dissolve
        with fadeq

        play sound2 rain_indoor fadein 1 loop
        scene ch2ep1_769
        with dissolve
        pause
        scene ch2ep1_770
        with dissolve
        pause
        scene ch2ep1_771
        with dissolve
        g "And there he goes—the tireless savior himself."
        scene ch2ep1_772
        with dissolve
        g "Saint [mc], healer of the broken and tamer of gloomy women."
        g "With his soft heart, that stupidly patient face..."
        g "A walking invitation for every lost soul to chase."
        scene ch2ep1_773
        with dissolve
        g "God, it's almost poetic. Almost."
        g "For the record, I came up with that. And I'm not drunk, before you even ask."
        scene ch2ep1_774
        with dissolve
        mc "*sighs* Shit went down while you were gone."
        if allornothingroute:
            g "I can tell."
            mc "Nothing too dramatic... just time doing what it does..."
            scene ch2ep1_775
            with dissolve
            g "[mc]... you know I'm not the philosophical type. Explain."
            mc "Kept showing up in her room. Breakfast into lunch, lunch into dinner."
            mc "After a while, the quietude started feeling less like silence and more like... well... a routine."
            g "\"Nothing dramatic,\" huh? Sure."
            mc "Yeah, I don't really know how else to put it."
            g "You two talked?"
            scene ch2ep1_776
            with dissolve
            mc "Not much. She's not the kind you {i}talk with{/i} anymore—not since... well, you know."
            mc "Now she's the kind you learn from by just sitting beside her. Some days she barely says a word. Other days, she asks how I'm doing and pretends she doesn't care about the answer."
            g "And you kept going back anyway?"
            mc "Every day. For a year. Didn't even notice when it stopped being obligation and turned into habit."
            g "*laughs* That's one hell of an unhealthy habit, [mc]. Oh, my poor boy..."
            scene ch2ep1_777
            with dissolve
            mc "Typical you—laughing at my fumbles."
            g "Because you sound like a man who got too comfortable living in someone else's storm."
            mc "... I found something in that storm, Gwen. Something precious I don't want to let go of."
            image gwmctabkl:
                "ch2ep1_778.jpg"
                pause 0.1
                "ch2ep1_779.jpg"
                pause 0.1
                "ch2ep1_778.jpg"
                pause 0.1
                "ch2ep1_779.jpg"
                pause 0.1
                repeat
            show gwmctabkl
            g "Like you always do, huh?"
            mc "Oh, cut it out."
            scene ch2ep1_780
            with dissolve
            hide gwmctabkl
            g "So... who kissed who first?"
            mc "She did. Right before I left."
            g "And...?"
            mc "She's acting like it never happened. And I'm matching her pace."
            g "Figures."
            scene ch2ep1_781
            with dissolve
            mc "What's that supposed to mean?"
            g "You're the kind who keeps things intact by holding your breath."
            mc "*chuckles softly* Guilty as charged."
            scene ch2ep1_782
            with dissolve
            mc "..."
            scene ch2ep1_783
            with dissolve
            mc "She looks more beautiful every time I see her. Why is that?"
            g "That's one way to say you've got it bad. No, both of you. And probably Sky, too."
            g "Anyway, go on—wherever you're heading. I won't keep you."
            scene ch2ep1_784
            with dissolve
            mc "Yeah. I'm heading back to Emma's office."
            g "Oh? Mind if I tag along? Haven't seen her in ages."
            scene ch2ep1_785
            with dissolve
            mc "She'd probably throw you out before you finish saying hi."
            g "Still?"
            mc "Still. Your best friend still hates having visitors—even her own friends."
            g "Guess some habits die harder than roaches."
        else:
            g "Oh I don't even wanna ask."
            g "Go on—wherever you're heading. I won't keep you."
            scene ch2ep1_784
            with dissolve
            mc "Yeah. I'm heading back to Emma's office."
            g "Oh? Mind if I tag along? Haven't seen her in ages."
            scene ch2ep1_785
            with dissolve
            mc "She'd probably throw you out before you finish saying hi."
            g "Still?"
            mc "Still. Your best friend still hates having visitors—even her own friends."
            g "Guess some habits die harder than roaches."
        stop sound2 fadeout 2

        scene black
        with dissolve
        with fadeq

        play sound4 closedoor
        play sound3 wind_gust fadein 2 loop
        play sound rain_heavy fadein 2 loop
        play sound2 rain_indoor fadein 2 loop
        scene ch2ep1_786
        with dissolve
        pause
        scene ch2ep1_787
        with dissolve
        mc "Ugh... when did it get this cold? It was warmer when I was in—"
        scene ch2ep1_788
        with dissolve
        mc "..."
        scene ch2ep1_789
        with dissolve
        pause
    stop sound3 fadeout 2
    stop sound fadeout 2
    stop sound2 fadeout 2

    scene black
    with dissolve
    with fade

    $ phone_time_add(hours=8)
    play sound rain_indoor fadein 2 loop
    scene ch2ep1_790
    with dissolve
    pause
    play sound2 sneeze_male
    scene ch2ep1_791
    with hpunch
    pause 0.5
    mc "Oh man..."
    scene ch2ep1_792
    with dissolve
    e "You're catching something again, aren't you?"
    mc "Probably just the rain."
    e "You've been running on fumes for days."
    mc "You think so?"
    e "I can see it. I was the one who told Aine. Doing two huge jobs at once is insane, [mc]."
    scene ch2ep1_793
    with dissolve
    mc "Figures you'd notice..."
    e "And now you've got that same look again—the one that means you haven't slept properly."
    mc "Relax, detective. I'm clean."
    e "Sure. Until your body files a complaint."
    scene ch2ep1_794
    with dissolve
    e "*sighs* Go home, [mc]. Get some rest before you short-circuit."
    mc "You usually tell me to keep pushing."
    e "Not when you're running yourself into the ground."
    play sound2 chairdrag
    scene ch2ep1_795
    with dissolve
    e "And since I'm not one to disobey my own preaching, I'm packing up too. Okay?"
    mc "Deal. I think the office lights will miss you, though."
    e "*chuckles* They'll live."
    scene ch2ep1_796
    with dissolve
    e "Here, take this. It's colder out there than it looks."
    play sound2 mugdown
    scene ch2ep1_797
    with Dissolve(0.2)
    e "Wait—hold on, that's coffee."
    mc "Coffee? At this hour?"
    scene ch2ep1_798
    with dissolve
    e "Well... I needed my fuel."
    scene ch2ep1_799
    with Dissolve(0.2)
    e "Hold on, I'll grab you something actually hot."
    if emmaroute:
        menu:
            "Slap her ass":
                $ emmaassslapping = True
                mc "No need. There's nothing hotter than this thing right here."
                play sound2 slap
                scene ch2ep1_800
                with hpunch
                pause 0.5
                scene ch2ep1_801
                e "HAAAAHHHNG~!!!"
                play sound2 cloth2
                scene ch2ep1_802
                mc "Easy, officer. The suspect might hear us."
                scene ch2ep1_803
                with dissolve
                pause 0.5
                mc "Starting to enjoy it now, huh?"
                $ emmapoint += 1
                $ renpy.notify(emmanotif)
                e "I never stopped... Do it more often, bad boy..."
                play sound2 woosh
                scene ch2ep1_804
                e "W-We should head home! And you—don't you dare try that again!"
                yt "*chuckles* I'll never get tired of flustered Emma."
            "Let her be":
                $ emmaassslapping = False
                e "Give me one minute. I'll be right back."
    stop sound fadeout 2

    $ phone_time_add(minutes=15)
    if klararoute:
        scene black
        with dissolve
        with fade

        play sound rain_bedroom fadein 2 loop
        play music 'audio/LostInTheStatic.mp3' fadein 2
        scene ch2ep1_805
        with dissolve
        k "{i}He's late."
        k "{i}I told him to go. So why does it feel wrong that he actually did?"
        k "{i}The room feels... wrong too."
        scene ch2ep1_806
        with Dissolve(0.3)
        pause 0.7
        play sound2 wallclock_once_1
        scene ch2ep1_807
        pause 1.0
        play sound3 wallclock_once_2
        scene ch2ep1_808
        pause 1.0
        play sound4 wallclock_once_3
        scene ch2ep1_809
        pause 0.5
        scene ch2ep1_810
        with dissolve
        k "{i}I should be glad. I said what I had to say. I broke the silence. Pushed him out before it got worse."
        k "{i}So why does it feel like I just made it worse anyway?"
        scene ch2ep1_811
        with dissolve
        k "{i}What if he doesn't come back?"
        k "{i}No. He will. He always does..."
        scene ch2ep1_812
        with dissolve
        k "{i}And if he does—what then? What do I even say to him?"
        k "{i}I don't want this. I shouldn't. But I do. God, I do."
        play sound2 doorknob2
        scene ch2ep1_813
        with dissolve
        k "{i}... No. Don't—"
        play sound3 opendoor2
        scene ch2ep1_814
        with dissolve
        mc "Hey, sorry I'm late—"
        $ renpy.music.set_volume(0.0, 0.0)
        play sound2 waterphone
        scene ch2ep1_815
        pause
        scene ch2ep1_816
        with hpunch
        mc "AAAAHHHH!"
        mc "Goddamn it, Klara!" with hpunch
        scene ch2ep1_817
        with dissolve
        k "*laughs* I...I'm sorry. I couldn't help myself."
        mc "..."
        scene ch2ep1_818
        with dissolve
        mc "Don't do that."
        k "Don't do what?"
        $ renpy.music.set_volume(1.0, 2.0)
        scene ch2ep1_819
        with dissolve
        mc "Look... I know what this is."
        mc "You don't have to talk to me if you don't want to. You can be mad at me for breaking your silence."
        mc "But no matter what face you show the world, this is the last thing I want—seeing you force a mask when you're with me."
        scene ch2ep1_820
        with dissolve
        k "..."
        k "People think being quiet is empty space. It's not. It's the only place where no one can get at you."
        k "And when it finally breaks... you don't feel lighter. You just feel... exposed."
        k "And once it's gone, you can't stuff it back. The air changes. Everything sounds different. You start wondering what's left to hide behind."
        k "They all say talking helps. But no one ever tells you about the quiet after, and how much it hurts knowing you broke your silence."
        scene ch2ep1_821
        with dissolve
        k "That's what I gave up, [mc]..."
        k "And now, I know I won't feel safe without it."
        scene ch2ep1_822
        with dissolve
        k "But with you... it doesn't feel like that. And I don't know why."
        scene ch2ep1_823
        with dissolve
        k "[mc], you and I..."
        scene ch2ep1_824
        with dissolve
        k "*exhales* We're not supposed to blur lines like this."
        k "So why does it feel like every part of me is saying it's okay? That it's already been this way for a long time?"
        scene ch2ep1_825
        with dissolve
        k "Why you? Why does it have to be you?"
        k "I hate it! I hate that it's you!"
        k "But I'm happy at the same time! Because whatever {i}this{/i} is, you make something in me feel so—"
        scene ch2ep1_826
        with dissolve
        k "[mc], what is this? Tell me, because I don't know how to name it!"
        scene ch2ep1_827
        with Dissolve(0.2)
        mc "Klara..."
        mc "You don't have to make sense of it right now."
        k "When, then? When it's too late?"
        mc "It's already too late for pretending. You feel it too—I know you do."
        scene ch2ep1_828
        with dissolve
        pause
        scene ch2ep1_829
        with dissolve
        mc "Whatever this is... I don't want to wreck it by saying the wrong thing."
        k "There isn't a \"right\" thing in any of this, [mc]."
        mc "Exactly."
        scene ch2ep1_830
        with dissolve
        mc "Look, I'm not running. But if I stay any longer, I'll just..."
        mc "... make a bigger mess."
        k "You already did. {b}We{/b} already did."
        pause 0.5
        scene ch2ep1_831
        with dissolve
        mc "Yeah..."
        mc "Sky's making dinner. Try to rest, if you can. I'll be here in the morning."
        scene ch2ep1_832
        with dissolve
        pause
        scene ch2ep1_833
        with dissolve
        mc "And, Klara..."
        scene ch2ep1_834
        with dissolve
        mc "Whatever you think this is... you're not the only one feeling it."
        play sound2 closedoor2
        scene ch2ep1_835
        with dissolve
        pause
        scene ch2ep1_836
        with dissolve
        pause

        scene black
        with dissolve
        with fadeq

        play sound2 closedoor
        scene ch2ep1_837
        with dissolve
        mc "\"You don't have to make sense of it right now.\""
        scene ch2ep1_838
        with dissolve
        mc "Yeah... right."
        play sound2 thud2
        scene ch2ep1_839
        with hpunch
        pause 0.5
        mc "Damn. Figures. All this rain has to land somewhere."
        scene ch2ep1_840
        with dissolve
        mc "\"Whatever you think this is... you're not the only one feeling it.\""
        mc "*mutters* Brilliant. Real fucking smooth."
        play sound2 chair
        scene ch2ep1_841
        with dissolve
        mc "Just one night where my head shuts up. Please."
        scene ch2ep1_842
        with dissolve
        mc "Don't... send me back... to that white room..."
        scene ch2ep1_843
        with dissolve
        mc "... again."
        stop music fadeout 2
        stop sound fadeout 2
        call hide_days from _call_hide_days_37
        with dissolve

        scene black
        with dissolve
        with fade
        
        show screen day_saturday with dissolve
        play music 'audio/SweetDreams.mp3'
        play sound rain_bedroom fadein 2 loop
        scene ch2ep1_844
        with dissolve
        pause
        show klaraanxious
        with dissolve
        pause
        k "{i}Something's off...{/i}"
        k "{i}Do I call him? What do I—{/i}"
        play sound2 dyinggasps fadein 0.5 loop
        stop sound fadeout 0.5
        show keiwhiteroom
        with dissolve
        hide klaraanxious
        pause 11
        stop sound2 fadeout 0.5
        play sound rain_bedroom fadein 0.5 loop
        show klaraanxious
        with Dissolve(0.3)
        hide keiwhiteroom
        k "..."
        k "{i}He's just within arm's reach. He's right there... in the next room."
        k "{i}Why am I sitting here like this?"
        stop sound fadeout 0.5
    else:
        call hide_days from _call_hide_days_38
        with dissolve

        scene black
        with dissolve
        with fade

        show screen day_saturday with dissolve
        play music 'audio/SweetDreams.mp3'
        play sound rain_bedroom fadein 2 loop
        scene ch2ep1_844
        with dissolve
        pause
        show klaraanxious
        with dissolve
        pause
        k "{i}He's late.{/i}"
        play sound2 dyinggasps fadein 0.5 loop
        stop sound fadeout 0.5
        show keiwhiteroom
        with dissolve
        hide klaraanxious
        pause 11
    
    $ phone_time_add(minutes=30)
    $ phone_time_add(hours=3)
    play sound2 doorknob2
    scene ch2ep1_845
    with Dissolve(0.1)
    hide klaraanxious
    pause
    play sound rain_bedroom loop
    play sound2 chairdrag
    scene ch2ep1_846
    pause
    play sound3 opendoor2
    scene ch2ep1_847
    with dissolve
    mc "H-hey... sorry... I—"
    scene ch2ep1_848
    with Dissolve(0.2)
    pause 0.5
    play sound2 chairdrag
    scene ch2ep1_849
    k "[mc]!"
    play sound2 thud2
    scene ch2ep1_850
    with hpunch
    k "[mc], you're burning up—"
    scene ch2ep1_851
    with flash
    pause
    scene ch2ep1_852
    with flash
    pause 0.5
    scene ch2ep1_853
    with dissolve
    k "{i}I was so wrapped up in my own pain that I didn't even notice he was burning..."
    k "{i}What's wrong with me...?"
    scene ch2ep1_854
    with dissolve
    mc "*weak chuckle* Must've... left the window open."
    k "There's a time for jokes, [mc]—and now isn't it! You shouldn't even be standing right now."
    mc "Told you I'd... be here in the morning."
    k "This isn't morning: it's the middle of the damn night! What are you—"
    mc "Close enough..."
    k "I can't tell if you're trying to be funny, or if you're—"
    scene ch2ep1_855
    with dissolve
    k "Damn it, come here!"
    k "Slowly. Don't talk."
    mc "Didn't... want to worry you..."
    k "Too late for that."
    play sound2 chair
    scene ch2ep1_856
    with dissolve
    pause
    play sound3 bag_rummage
    scene ch2ep1_857
    with dissolve
    k "Hold on..."
    play sound3 pills_close
    scene ch2ep1_858
    with dissolve
    k "{i}Where the hell are my meds when I need them—"
    scene ch2ep1_859
    with dissolve
    pause
    scene ch2ep1_860
    with dissolve
    k "..."
    k "{i}Right..."
    play sound2 tablehit
    scene ch2ep1_861
    with hpunch
    pause
    scene ch2ep1_862
    with Dissolve(0.2)
    pause 0.3
    scene ch2ep1_863
    with Dissolve(0.2)
    pause
    scene ch2ep1_864
    with Dissolve(0.1)
    k "{i}Someone. Please. Just one person awake at this hour—"
    scene ch2ep1_865
    with Dissolve(0.1)
    pause
    scene ch2ep1_866
    with Dissolve(0.2)
    k "..."
    k "{i}What did I ever give him? A chair to sit on... a silent room... and a woman who never knew how to show up at the right time."
    k "{i}He was hurting, and I froze. Like I always do. Like my bones were carved for running and not standing beside anyone."
    k "{i}And still, he kept coming back. Every day. Like that meant something worth keeping."
    scene ch2ep1_867
    with dissolve
    k "{i}I tell myself he deserves better... but that's not the truth, is it?"
    k "{i}The truth is... I don't know how to be better."
    k "{i}But he walked into my quiet and never flinched."
    scene ch2ep1_868
    with dissolve
    k "{i}So maybe... maybe the least I can do is take one step back toward him."
    play sound2 woodhit2
    scene ch2ep1_869
    with hpunch
    k "{i}If he can walk into my silence without fear..."
    k "{i}Then I can stop treating these walls like they're sacred."
    scene ch2ep1_870
    with dissolve
    k "{i}{sc}{font=Beowolf.ttf}Even if I have to tear these four walls down myself!"
    scene ch2ep1_871
    with dissolve
    k "Stay here. I'll be back."
    stop sound fadeout 1
    scene black
    with dissolve
    play sound2 rain_indoor fadein 1 loop
    play sound3 closedoor
    scene ch2ep1_872
    with dissolve
    pause
    scene ch2ep1_873
    with dissolve
    pause
    scene ch2ep1_874
    with dissolve
    pause
    scene ch2ep1_875
    with dissolve
    pause
    stop sound2 fadeout 1
    play sound rain_heavy fadein 1 loop
    play sound3 closedoor
    scene ch2ep1_876
    with dissolve
    pause
    scene ch2ep1_877
    with dissolve
    pause 0.5
    stop sound fadeout 4
    scene ch2ep1_878
    with Dissolve(2.0)
    pause
    scene ch2ep1_879
    with dissolve
    k "{i}If this is just coincidence... why does it feel like punishment?"
    play sound2 car_unlock
    scene ch2ep1_880
    with Dissolve(0.1)
    pause
    stop music fadeout 2

    scene black
    with dissolve
    with fade

    $ phone_time_add(hours=1)
    play music 'audio/EsLullaby.mp3' fadein 2
    scene ch2ep1_881
    with dissolve
    mc "... Not again..."
    scene ch2ep1_882
    with dissolve
    eee "You keep coming back sooner each time."
    mc "Where am I this time—the real one, or here?"
    scene ch2ep1_883
    with dissolve
    eee "You ask that like there's a real answer."
    mc "You said every step I take is a surrender. So what did I give up this time?"
    scene ch2ep1_884
    with dissolve
    eee "A promise."
    mc "To who?"
    eee "To yourself. The one who swore to keep his distance."
    mc "I never said that."
    eee "Exactly."
    scene ch2ep1_885
    with dissolve
    mc "I don't really get what you're trying to tell me."
    scene ch2ep1_886
    with dissolve
    eee "I told you before... what you face, I face. What you turn away from, I can't reach."
    eee "Strange how it works: you move forward, and this place takes something from you in return."
    scene ch2ep1_887
    with dissolve
    eee "And the more you walk, the less of you there'll be to find." with Dissolve(2.0)
    play sound kei_fromdream
    scene black
    with Dissolve(0.1)
    pause
    stop music fadeout 4
    play sound dawnambient fadein 4 loop
    scene ch2ep1_888
    with Dissolve(2.0)
    pause
    scene ch2ep1_889
    with Dissolve(2.0)
    mc "*murmurs* ... Klara?"
    scene ch2ep1_890
    with dissolve
    k "Careful. You'll spill it."
    play sound2 sip
    scene ch2ep1_891
    with dissolve
    mc "Medicine?"
    k "Just water. You were coughing. I already gave you your meds earlier, don't you remember?"
    mc "... Still a bit foggy."
    play sound2 mugdown
    scene ch2ep1_892
    with dissolve
    k "Your fever dropped fast, but you scared the hell out of me. You always do."
    mc "You went out... in the rain?"
    k "Please, don't make it sound so noble. You're my responsibility."
    play music 'audio/ThoughtsInTheRain.mp3' fadein 4
    play sound2 cloth
    scene ch2ep1_893
    with dissolve
    pause
    scene ch2ep1_894
    with dissolve
    mc "You've been here the whole time?"
    k "Mhm. Watching you like you might stop breathing at any second."
    scene ch2ep1_895
    with dissolve
    k "You talk in your sleep."
    mc "That bad?"
    k "You kept saying my name."
    mc "Sorry..."
    k "Don't be. I don't hate hearing it."
    scene ch2ep1_896
    with dissolve
    pause
    scene ch2ep1_897
    with dissolve
    k "When my parents died, I waited for something to break—a tear, a scream, anything. But nothing came."
    k "It felt like reading the news about strangers. I used to think that made me strong."
    k "Every time someone left, I just—"
    k "*shaking her head* I just adjusted. Like grief was a room I redecorated every few years."
    scene ch2ep1_898
    with dissolve
    k "Except for one person."
    mc "Yeah..."
    scene ch2ep1_899
    with dissolve
    k "It scares me because I don't know what that makes me."
    k "Maybe I'm just wired wrong. Maybe I was never built for loving people the way they need."
    k "Sometimes I wonder if I'm missing something people are born with—a pulse, a switch, whatever makes them care without trying."
    k "And then you show up. Every damn day. Sitting here like I'm worth the wait."
    k "You make me feel like I've been asleep my whole life."
    scene ch2ep1_900
    with dissolve
    k "You made time start moving again."
    if (klararoute and klarapoint == 7):
        k "Just when I'd learned to live without it."
        k "Just when I thought I'd buried the part of me that looked at you... differently."
        stop music fadeout 1
        scene ch2ep1_901
        with Dissolve(0.1)
        pause
        label forbiddenfruit:
        if _in_replay:
            $ name = persistent.gallery_name
        play sound2 cloth
        scene ch2ep1_902
        with Dissolve(0.2)
        play music2 'audio/BendAndBreak.mp3'
        k "*whispers* I don't care anymore."
        k "I don't even need to understand it right now."
        k "All I know is I want this. I want you to {i}stay{/i}."
        scene ch2ep1_903
        with dissolve
        "Klara leans in—hesitant at first, like she's still asking permission. Her breath brushes yours before the space between you disappears."
        "Her hand finds your cheek, unsteady, but she doesn't pull away."
        play sound2 cloth
        scene ch2ep1_904
        with dissolve
        "She guides you down with the kind of care that feels learned, gentle, searching, and real."
        "Her lips brush against yours—soft, steady, and tender, yet laced with a quiet hunger: a need she's too shy to name."
        scene ch2ep1_905
        with dissolve
        "You both pull away slowly, deliberately, as if the moment itself might shatter. It feels fragile—borrowed from a dream you're afraid to wake from."
        "Still, a flicker of hesitation crosses your face."
        scene ch2ep1_906
        with dissolve
        k "Tell me if you want me to stop."
        mc "No. It's just..."
        "Klara's gaze drops, thoughtful, her eyes heavy with emotion."
        scene ch2ep1_907
        with dissolve
        mc "Nothing serious... I'm just worried you might catch whatever it is I've got."
        scene ch2ep1_908
        with dissolve
        "Her eyes soften, a faint light breaking through the usual storm—something rare, something she doesn't show the world."
        mc "You know, I don't think I've ever told you how stunning you look when you smile."
        scene ch2ep1_909
        with dissolve
        k "Is that supposed to be a dagger to the chest after a whole year of me rotting in the dark?"
        "Her tone bites, but there's no venom behind it—just a trace of vulnerability hiding under the sarcasm."
        mc "What? I'm just being honest."
        "Klara exhales a short, sheepish laugh, the sound almost like a sigh of relief."
        k "What did I expect? You're always such a—"
        mc "Such a what?"
        k "A dork."
        mc "Hey, that's harsh. But I guess that's a part of me that hasn't changed much, huh?"
        scene ch2ep1_910
        with dissolve
        "Her head tilts slightly, eyes searching yours as if weighing the risk of falling again."
        k "{i}I want this... maybe more than I should."
        k "{i}And I hate how easily my hands remember the shape of something I shouldn't touch."
        k "{i}Right and wrong blur when you're this close. It's hard to tell which one I'm betraying now."
        scene ch2ep1_911
        with dissolve
        pause 0.5
        mc "In a couple's dance, this is how you steady your partner, right?"
        k "You're not helping, you know that?"
        "She says that, yet her hand stops trembling the moment it meets yours."
        mc "You're... something else, Klara. And I don't want to run from what that means."
        scene ch2ep1_912
        with dissolve
        "The air between you hums, and you both lean in, falling into each other like it's the only thing that makes sense."
        k "Mmh..."
        scene ch2ep1_913
        with dissolve
        "Klara pulls back slightly, her breath shaky, fingertips gliding down your chest in a teasing line."
        k "You like that?"
        mc "Yeah..."
        scene ch2ep1_914
        with dissolve
        "A shiver runs through her, not from fear, but from the dizzying realization of what's about to happen."
        "Even so, she keeps tracing downward, her touch trembling, uncertain yet unwilling to stop."
        scene ch2ep1_915
        with dissolve
        "You notice. When her hands start to drift toward your hem, you catch them gently."
        "Klara freezes, caught off guard, her breath hitching."
        play sound2 cloth
        scene ch2ep1_916
        with dissolve
        "You don't say a word. Instead, you sit up, keeping her settled on your lap, close enough to feel every exhale between you."
        "She doesn't resist. Hesitation lingers in her eyes, but desire burns brighter beneath it."
        play sound2 belt
        scene ch2ep1_917
        with dissolve
        "Then, without breaking eye contact, you slowly pull your shirt over your head. The motion alone feels like a confession."
        mc "I'm yours."
        play sound2 cloth
        scene ch2ep1_918
        with dissolve
        "She doesn't speak further. Instead, she answers quietly, undoing her top..."
        "... then slipping out of her bra."
        "Until all that's left are her bare breasts, ready to be consumed whole."
        "You don't linger to stare—you dive in, drawn by something rawer than lust."
        "But you resist for the moment."
        scene ch2ep1_919
        with dissolve
        "The dim glow shrouding the room turns Klara into something magnetic."
        "Your mouths collide again, fiercer and hungrier, giving testament to your earlier affirmations."
        "Klara's hands tangle in your hair, pulling you closer—protective, almost maternal."
        "You catch a glimpse of her through half-lidded eyes, meeting her gaze before losing yourself again."
        scene ch2ep1_920
        with dissolve
        "You nip her lower lip, the sweetness matching the desserts you shared with each meal together."
        k "Ngh..."
        scene ch2ep1_921
        with dissolve
        "You leave a final kiss on her lips before drifting lower, tracing her throat with the kind of patience that heightens the tension in the air."
        "She tips her head back, an invitation: you take it without hesitation."
        "You find her chin, then her neck, then pause at her collarbone, tasting the faint salinity of her skin."
        "Your tongue gives way to your teeth, scraping against the firm bone as you work your way down the curve of her bosom."
        scene ch2ep1_922
        with dissolve
        k "*gasp*"
        "You graze downwards, teeth gently catching against her nipple on the way to her lower breast."
        "As Klara lets out another silent moan, you move to her other hardened peak, wrapping your lips around the teat and sucking while you nibble the delicate nub."
        scene ch2ep1_923
        with dissolve
        k "[mc]..."
        "She gently guides your head up so she can search your eyes."
        k "You always do that..."
        mc "What?"
        k "You turn my silence into something wonderful."
        "Her smile softens, eyes bright with affection, yet darkened with desire."
        scene ch2ep1_924
        with dissolve
        "Her arms draw you in until her voice is a whisper against your ear."
        k "Everyone else simply fills it with noise."
        mc "Perhaps I got used to the quiet too much."
        k "No... You just listen differently. And that's what makes my heart stop in its tracks."
        play sound2 chair
        scene ch2ep1_925
        with dissolve
        "Before you can answer, she gently pushes you back, shifting the rhythm."
        "Now, she's above you, breath ghosting your cheek as she slowly rolls her hips, turning the thin fabric between you into an excruciating tease."
        mc "Fuck... Klara..."
        mc "You're taking control now?"
        k "When did I stop?"
        scene ch2ep1_926
        with dissolve
        "Her voice deepens with a tremor that's beyond lust—it's something heavy and human."
        k "If you think you can read me now... think again."
        scene ch2ep1_927
        with dissolve
        "She moves, slower, her gaze burning through the dim light."
        mc "Then let me be wrong beside you."
        "Her breath catches; her rhythm faltering but for a moment."
        k "You're really dangerous when you talk like that."
        mc "So are you."
        show klara1
        with dissolve
        "Once Klara begins to move, it doesn't take long for you both to fall into rhythm."
        "Each slow drag of her hips blurs thought into breath, the air thick enough to taste."
        "The friction transfers heat directly to your firming member, amplifying the electricity of arousal."
        "In equal response, you feel the growing heat between Klara's legs, the clothing between you serving as kindling."
        mc "I'm not dreaming, right?"
        k "Mmhh... If this is a dream, please... please don't wake up yet..."
        "Her voice breaks around the words as a faint dampness begins to leak through her bottoms."
        mc "Klara..."
        "Your hands find her waist. The line between who's guiding and who's yielding disappears with each grind, each gasp."
        "She exhales against your neck, steadying herself."
        k "R...Right there... don't move."
        k "Let me take care of you. Of both of us."
        mc "Klara, please—"
        scene ch2ep1_928
        with dissolve
        hide klara1
        "Before you can finish, Klara presses a finger to your lips, silencing you with a look that says a thousand words."
        k "Shh..."
        play sound2 cloth
        play sound3 belt
        scene black
        with dissolve
        pause 1.0
        scene ch2ep1_929
        with dissolve
        "Her hum is soft, almost melodic, as she removes the remainder of her clothing."
        "You follow suit, until there's nothing left between you but skin and heat."
        k "Try not to get sick again, alright?"
        mc "If getting sick means I get to feel you like this... then maybe I should catch a cold more often."
        mc "Damnit. Was it corny that I pretty much reused my previous line?"
        scene ch2ep1_930
        with dissolve
        k "So be it. I've learned that while words themselves carry some meaning..."
        "Klara pauses, the heat of her pussy breathing down onto your naked manhood."
        k "... The intent behind them and actions that follow mean infinitely more."
        show klara2
        with dissolve
        "She leans down and moves her hips faster than before."
        "Your body answers before your mind does, muscles tight as her warmth grazes against you."
        "Once her slick folds meet the pulse of your cock, the sound that leaves you isn't a groan, but a relief."
        "The first grind is measured; the next, hungry."
        "She circles her hips, and your world narrows to the breadth between you."
        k "I'd forgotten what it felt like to feel..."
        mc "Excited? Overwhelmed? Horny and pumped full of hormones?"
        k "{b}Real{/b}."
        show klara3
        with dissolve
        hide klara2
        "Her whisper drags against your mouth, half confession, half surrender."
        mc "Let me help restore your memory."
        "Her forehead rests against yours, her voice quiet but steady."
        k "If I do... I don't know if I'll come back from it."
        mc "Who says you need to go back? Isn't living all about embracing the unknown?"
        "The motion builds, wet skin sliding between you until both heat and pleasure crescendo."
        k "Hngh~! Hahhh~!"
        "Her sound finally breaks free, trembling out of her like something she'd been holding back for too long."
        k "[mc], I want—"
        scene ch2ep1_931
        with dissolve
        hide klara3
        "Klara pauses, positioning herself above you with trembling precision. Her slick labia tease your tip, sending a surge of electricity through your nerves."
        "The moment your cock brushes against her opening, your breath falters—desire clawing at the edges of reason."
        scene ch2ep1_932
        with dissolve
        "She reaches down, steadying you in her hand, but freezes halfway."
        k "..."
        mc "What's wrong?"
        "You murmur, your voice rough with restraint."
        k "I..."
        "The tremor that had once faded returns, stronger this time. You decide not to dance around it."
        scene ch2ep1_933
        with dissolve
        mc "Hey... look at me."
        mc "We've already made it this far. Nothing bad has happened."
        mc "No worrying thoughts, no regrets. Right?" 
        mc "Whatever happens here—let's not fight it. We both deserve to let ourselves satisfy our desires."
        mc "And let ourselves feel what {i}real{/i} is like."
        scene ch2ep1_934
        with dissolve
        "Something in Klara softens. The tension in her shoulders melts as she exhales, her eyes glimmering faintly in the low light."
        "You squeeze her thighs, anchoring her, telling her that you're here, that you're in this together."
        scene ch2ep1_935
        with dissolve
        k "May I?"
        mc "Careful... you're starting to sound too gentle."
        scene ch2ep1_936
        with dissolve
        "Her lips twitch."
        "She gives a glare equal parts offense and challenge, and before you can breathe..."
        play sound2 bodyhit
        scene ch2ep1_937
        with hpunch
        pause
        scene ch2ep1_938
        k "AAAHHNNNGG~!!"
        mc "Holy—!"
        "... she sinks down in one motion, her body shuddering as pleasure and pain rips through her."
        scene ch2ep1_939
        with Dissolve(0.1)
        k "Mnhh! Fuck...! I shouldn't have done that."
        mc "Funny, looks like that knocked your filter loose."
        scene ch2ep1_940
        with dissolve
        k "You cheeky—! Stop enabling me!"
        mc "But it worked, didn't it? You're calmer now. And more like yourself."
        k "*shakes her head* You're impossible..."
        k "Be careful, [mc]... I can still fall in love."
        mc "And I won't tell you not to. You're your own woman, Klara."
        mc "And a beautiful one at that."
        scene ch2ep1_941
        with dissolve
        k "..."
        "A faint, knowing smile crosses her lips as she leans closer."
        scene ch2ep1_942
        with dissolve
        k "Then let me show you..."
        k "... what it's like in my world."
        show klara4
        with dissolve
        yt "Ffuuuccckk!!"
        "You let out a silent exhale as Klara begins to move."
        "Going slowly at first, she rests her palms on your chest and looks down at you, but with a caring undertone to her gaze."
        "Her movements are steady—almost effortless. She clearly knows exactly what she's doing, and it leaves you struggling to keep up."
        "Despite the smooth intensity of her movements, there's a measured restraint to her breath as if she's acutely aware of this, holding back to avoid hurting you."
        k "How's that, [mc]?"
        mc "Fuck, Klara... It's good. You're not hurting me, don't worry."
        mc "It'll just take me a second to get used to you. Believe it or not, I've never been with a woman with so much \"life experience\" before."
        "Klara chuckles, amused, yet digs her nails into your pecs in feigned annoyance."
        mc "Yaggh!"
        k "My, oh my. You certainly aren't the little child that came into my care all those years ago, are you?"
        k "Certainly grown into a {i}big{/i}, strong man, you have."
        k "\"Life experience\"? Don't get cute with me now, [mc]. If you have something to say to this old lady, say it like a man."
        "You return her smirk, then clench your pelvic floor to subtly push yourself deeper into her."
        k "Nghh~!"
        mc "How's that for \"like a man\"?"
        "A devilish grin spreads across the lady's face."
        k "Always have to be the cheeky one, don't you? Very well, I'll show you how I punish such boys."
        show klara5
        with dissolve
        hide klara4
        "Not waiting for your response, she increases the pace, adding circular and lateral movements as she rides you in full force."
        "Her breath quickens, both as a result of her increased exertion and building arousal now that all bets are off."
        "Along with her vaginal walls squeezing your length, Klara also tightens the muscles around her labia, wringing your dick like a wet towel."
        yt "God DAMN! Has she always had this in her?"
        "In front of you, her ample tits bounce with every self-impalement down onto your pike."
        k "Enjoying the view, [mc]?"
        k "I never said you could look, naughty boy."
        "She grabs your hands that were resting on her legs and moves them to her hips."
        k "But that doesn't mean you shouldn't. Tell me, how does {i}experience{/i} feel?"
        "The feeling of her taut glutes in your hands, soft yet still firm, does little to quell the inferno building in your belly."
        "Combined with the slight slickness of her skin sliding against your palms, you feel your arousal growing exponentially as the lady of experience continues riding you."
        mc "I-it feels pretty damn good!"
        k "Good? That's it? Such high expectations kids have nowadays..."
        "Despite her teasing words, Klara's moans and gasps begin to give her own growing pleasure away."
        k "Mmnh~ So that's how it is. Should I stop?"
        show klara6
        with dissolve
        hide klara5
        "As she says this, Klara leans back, giving you the hottest view that you can ever remember seeing."
        mc "Don't you dare even think about it."
        mc "Just like that. Lean back like you did just now. Your moves, your boobs—you are {i}hot{/i}, Klara."
        k "You've always had a way with words when you put your mind to it."
        mc "I just said what I felt like saying. My mind's not really concerned about words right now, for obvious reasons."
        k "*chuckles* Nor is mine. Let's focus on more important matters."
        k "I can feel your throbbing getting more frequent and stronger, [mc]. And I'm pretty sure you can feel mine as well."
        "She's right, of course. During the time you two were bantering, your bodies continued working overtime to bring you both to the edge of climax."
        "Your grunts become shallow, almost guttural as your release knocks on the door, waiting for even the smallest crack in your resolve to break free."
        "And despite the collected look on her face, Klara's hair is disheveled in all directions and her gasps grow raspier and higher by the second."
        show klara7
        with dissolve
        hide klara6
        mc "Klara, I—"
        k "Mmmnhh~! I know, [mc]. I am as well."
        mc "I-"
        k "Finish inside me."
        mc "Are y—"
        k "INSIDE, DAMN IT! I want to feel your warmth completely suffusing through me!" with hpunch
        k "That's all I want right now. If you're concerned about so-called consequences, don't be. Let me handle them should they come."
        "Whether it's the assurance from her words, the alluring aroused tone in her voice, or just from sheer exhaustion, you find yourself no longer able to hold back your impending orgasm."
        scene ch2ep1_943
        with hpunch
        hide klara7
        "With one final grunt, you let yourself loose inside, receiving the full Klara experience as she clamps down on your manhood."
        mc "Klara!"
        "As you scream her name, Klara collapses onto you, biting her lip in a failed attempt to hold back her own climax."
        k "[mc]!"
        play sound2 cloth
        scene ch2ep1_944
        with dissolve
        "Breathless, you two lay there for a moment, legs tangled in an exhausted, euphoric pretzel."
        scene ch2ep1_945
        with dissolve
        "Klara hums quietly, gazing adoringly into your eyes as she strokes your cheek."
        k "Thank you for giving me everything I could have wanted, [mc]."
        "You smile back weakly, brushing a stray strand of hair out of her face."
        mc "For an old lady, you sure move like you're still in your prime."
        play sound2 cloth
        scene ch2ep1_946
        with dissolve
        "Klara swats your shoulder playfully, caressing your head as she holds you to her heart, appreciation and love radiating from each steady beat."
        k "Honestly, I was nervous before we did what we did. It's been longer than I can remember since I've been this intimate with someone."
        k "And I don't think I've ever been with anyone I've cared for as much as I do for you, [mc]. The last thing I want to do is hurt you for my sake."
        mc "I know you, Klara. I know you'd never do that to me. You may be aloof at times, but you've never stopped showing me you care."
        scene ch2ep1_947
        with dissolve
        "Klara smiles, grateful, and kisses you in the deepest way you've ever felt from her."
        scene ch2ep1_948
        with dissolve
        k "Thank you, [mc]. Though I admit, I'm still nervous about... this."
        mc "Don't be. Like you said, I've grown up into my own man thanks to you, so I can make my own decisions on who I love."
        mc "In fact..."
        scene ch2ep1_949
        with dissolve
        k "I know that look. What have you got up your sleeve now?"
        mc "Nothing, nothing. I'm not wearing any, after all."
        k "... Let me rephrase. What have you got up your sleeve other than your trademark \"charm\"?"
        play sound2 chair
        scene ch2ep1_950
        with dissolve
        "You shift with a gentle push, guiding her hips forward before pulling her back to settle between your legs."
        "Klara lets out a soft laugh as her back presses to your chest."
        mc "You got to run your show. Now it's only fair if I get to return the favor."
        k "*laughs under her breath* Youth... always so vigorous and insatiable."
        mc "So you're saying you're all tapped out after your wild ride?"
        k "Don't put words in my mouth, my dear fresh boy. You have no idea what you're in for."
        mc "If that's so, I can't wait to find out."
        scene ch2ep1_951
        with dissolve
        "You angle your hips, lining yourself up with her as your hand—"
        scene ch2ep1_952
        with Dissolve(0.1)
        k "Ah-ah! Let me guide you... slowly."
        scene ch2ep1_953
        with dissolve
        "Her hand wraps around your shaft, and she lifts her hips just enough to ease you inside with a tenderness that contradicts her earlier bravado."
        scene ch2ep1_954
        with dissolve
        "Klara tilts her head back just enough to catch your eyes over her shoulder, fingers sliding along your thigh to pull you deeper."
        k "And one more thing."
        mc "And what would that be?"
        k "Let me see your beautiful face while you take me again."
        show klara8
        with dissolve
        "Her breath shivers as you push deeper, your arms wrapping fully around her."
        "Her hands glide up to your forearms, holding you there, keeping you close."
        k "Ahhhh..."
        "You match your rhythm to the slow rise and fall of her breathing."
        "Though you start gently rocking your hips in tune with hers, for a moment you're taken by surprise at both her words and her actions."
        "It dawns on you: this isn't just about lust tonight."
        "This is about presence. Connection."
        "A woman who has lived in silence wanting to savor the feeling of being loved."
        mc "Klara..."
        "Her eyes stay closed, a quiet, blissful smile resting on her lips as she pulls your arms tighter around her, sealing herself against you."
        "Save for the occasional moan and sharp inhale of pleasure, she remains completely silent, savoring every feeling."
        "You take this opportunity to observe her every detail."
        "The way her crimson hair drapes across her face like a veil of a mysterious lady."
        "The way the faint lines in her face move with every expression, underscoring the life she's lived and the trials she's overcome—for you."
        "The way her chest rises and falls with each breath, heart beating with the vigor of a woman half her age."
        mc "Beautiful..."
        "Once she hears the word, Klara opens her eyes."
        "She turns her head, surprised at first, but quickly replaced with a sincere, grateful smile."
        k "You're really going to make this old woman cry, [mc]."
        mc "Haven't we already done enough crying for one lifetime?"
        show klara9
        with dissolve
        hide klara8
        "Klara shifts her hips, taking you deeper."
        "Her back arches against your chest, her breath catching between gasps."
        k "Perhaps you're right."
        k "Perhaps it's time for us to enjoy these little moments whenever they arise."
        "She deliberately tightens around you, squeezing in time with your thrusts."
        k "And speaking of arise..."
        k "You're getting close again, aren't you?"
        "Your breaths grow shallow, your jaw tightening as you start to move harder inside her."
        mc "Maybe... but with the way you're squeezing me, I bet you're not too far off either."
        k "*chuckles through a gasp* A lady never reveals her secrets."
        mc "Alright then... keep your secrets."
        show klara10
        with dissolve
        hide klara9
        "You slide down to her hips, then pull down and use her body as leverage to slam yourself deeper."
        "Each thrust drives your tip against the front of her pussy wall, forcing sharp moans out of her."
        k "Ngghhhhh~"
        mc "I have other ways of making you {i}spill{/i}."
        "Klara shoots you a sideways glance, half-leer, half-smirk, amused by your ability to crack a joke even now."
        "But Klara's expression quickly shatters. As the speed becomes overwhelming, her mouth falls open, eyes unable to focus."
        "Her breath stutters, thighs trembling as another climax rushes up on her without warning."
        k "[mc]—I'm cum—!"
        mc "Klara, me—mmgh!"
        play sound2 bodyhit
        scene ch2ep1_955
        with hpunch
        "Your rhythm breaks as pleasure slams through, hips locking tight against her."
        "A guttural groan rips from your chest, pulse after pulse forcing your release."
        play sound2 chair
        scene ch2ep1_956
        with hpunch
        k "C-CUMMING~!"
        "The sudden heat flashing inside her pushes Klara over the edge."
        "Her entire body shudders against you, back arching into your chest as she cries your name."
        k "[mc]! [mc]!!!"
        "Klara claws at your forearms, gripping you tight as she gushes around you, coating your cock with her climax."
        scene ch2ep1_957
        with dissolve
        "Your combined release leaks down between her thighs, warm trails rolling onto the sheets."
        "But Klara locks you inside, holding your arms around her as an anchor through the aftershocks."
        play sound2 chair
        scene ch2ep1_958
        with dissolve
        "The two of you slump together, bodies heavy and warm, tangled in sweat and breath and the fading echoes of your orgasms."
        "Neither of you moves. Neither of you speaks."
        scene ch2ep1_959
        with dissolve
        "Until finally... Klara breaks the {i}silence{/i}."
        k "[mc]."
        mc "Hmm?"
        k "How do you feel?"
        mc "*chuckles* You're not asking for another round, are you?"
        scene ch2ep1_960
        with dissolve
        mc "Though... it's hard to say no when you've got all {i}this{/i} working for you."
        scene ch2ep1_961
        with dissolve
        k "Stop joking, [mc]. You need to take care of yourself better. I mean it."
        mc "Seriously Klara, I'm fine. There's no need to worry."
        scene ch2ep1_962
        with dissolve
        mc "I know I've told you this already, but nothing I do for you was, is, or ever will be out of pity."
        mc "I know that this is going to be a bit complicated, but..."
        scene ch2ep1_963
        with dissolve
        pause
        scene ch2ep1_964
        with dissolve
        pause
        scene ch2ep1_965
        with dissolve
        k "\"But if it's for you, I'm willing to go through it\"?"
        k "You're rambling."
        scene ch2ep1_966
        with dissolve
        pause
        scene ch2ep1_967
        with dissolve
        mc "Am I...?"
        scene ch2ep1_968
        with dissolve
        k "*chuckles* Kidding."
        k "I trust you, you know?"
        k "When I'm with you, I feel like I'm breathing new air. Like I'm capable of feeling. Of believing. Of risking being hurt in order to live."
        k "When I saw you come back for me, day after day, even with all of my complications..."
        k "I just knew I had to dive in..."
        k "Because it's you."
        mc "Now who's rambling?"
        scene ch2ep1_969
        with Dissolve(0.2)
        mc "Ow! Fine, point taken."
        scene ch2ep1_970
        with dissolve
        mc "But you feel it, right?"
        k "Hm?"
        mc "That I feel the same way?"
        k "Mhm..."
        k "After what we did tonight, how could I not?"
        mc "Now who's being cheeky?"
        k "Oh, hush. Let an old woman have her moment."
        stop music2 fadeout 8
        scene ch2ep1_971
        with dissolve
        pause
        scene ch2ep1_972
        with dissolve
        k "[mc]... I need to thank you."
        mc "You've done enough of that already, Klara. There's no need."
        k "But you know that I'm not one to just say things like that. Truly, thank you."
        k "For showing up even when I didn't want company."
        k "For anchoring me with your presence when I barely felt like being here myself."
        scene ch2ep1_973
        with dissolve
        k "*exhales* You kept me tethered when I wanted everything to slip away."
        scene ch2ep1_974
        with dissolve
        k "You saved me, [mc]." with Dissolve(2.0)
        scene ch2ep1_975
        with Dissolve(2.0)
        pause
        scene ch2ep1_976
        with Dissolve(2.0)
        pause
        play sound2 cloth
        scene ch2ep1_977
        with dissolve
        pause
        scene ch2ep1_978
        with dissolve
        k "And now... I think I want to {i}stay{/i}."
        scene ch2ep1_979
        with dissolve
        mc "... Then I'm glad you're still here."
        $ renpy.end_replay()
    else:
        k "And... I need to thank you."
        k "For showing up when I didn't even want company."
        k "For sitting here when I barely felt like being here myself."
        scene ch2ep1_980
        with dissolve
        k "*exhales* You kept me tethered when I wanted everything to slip away."
        scene ch2ep1_981
        with dissolve
        k "You saved me, [mc]. Maybe not the way people mean it... but you did."
        scene ch2ep1_982
        with dissolve
        pause
        scene ch2ep1_983
        with dissolve
        pause
        play sound2 cloth
        scene ch2ep1_984
        with dissolve
        pause
        scene ch2ep1_985
        with dissolve
        k "And now... I think I want to {i}stay{/i}."
        scene ch2ep1_986
        with dissolve
        mc "... Then I'm glad you're still here."
    stop sound fadeout 2

    scene black
    with dissolve
    with fade

    $ phone_time_add(hours=4)
    $ renpy.music.set_volume(0.1, 0.0)
    play sound morningambience fadein 2 loop
    scene ch2ep1_987
    with dissolve
    pause
    play music 'audio/KlarasSonata_REVERB.mp3'
    scene ch2ep1_988
    with dissolve
    pause
    scene ch2ep1_989
    with dissolve
    pause
    play sound2 cloth
    scene ch2ep1_990
    with dissolve
    pause
    scene ch2ep1_991
    with dissolve
    pause
    scene ch2ep1_992
    with dissolve
    pause
    scene black
    with dissolve
    pause 0.5
    $ renpy.music.set_volume(0.6, 0.5)
    scene ch2ep1_993
    with dissolve
    pause
    scene ch2ep1_994
    with dissolve
    pause
    scene ch2ep1_995
    with dissolve
    pause
    play sound2 chair3
    $ renpy.music.set_volume(1.0, 0.5)
    scene ch2ep1_996
    with dissolve
    pause
    play sound3 stairsrundown
    scene ch2ep1_997
    with Dissolve(0.2)
    pause
    scene ch2ep1_998
    with dissolve
    pause
    play sound2 cloth2
    scene ch2ep1_999
    with hpunch
    pause
    scene ch2ep1_1000
    with dissolve
    m "You hate this kind of stuff, don't you?"
    g "Yeah. But hiding from it doesn't make it go away."
    scene ch2ep1_1001
    with dissolve
    g "And neither does pretending you're made of stone."
    g "Stop guessing what he would've wanted. Just show up. You're good at that part."
    scene ch2ep1_1002
    with dissolve
    pause
    scene ch2ep1_1003
    with dissolve
    pause
    play sound2 chair2
    scene ch2ep1_1004
    with dissolve
    pause
    scene ch2ep1_1005
    with dissolve
    pause
    play sound2 waterphone
    scene ch2ep1_1006
    with Dissolve(0.2)
    pause
    scene ch2ep1_1007
    with dissolve
    pause
    stop music fadeout 2
    stop sound fadeout 2

    scene black
    with dissolve
    with fade

    $ phone_time_add(hours=13)
    play sound nightambience fadein 2 loop
    play sound2 firewood fadein 2 loop
    scene ch2ep1_1008
    with dissolve
    pause
    play sound3 woodhit2
    play sound4 fire_movement
    scene ch2ep1_1009
    with Dissolve(0.2)
    pause
    scene ch2ep1_1010
    with dissolve
    mc "..."
    scene ch2ep1_1011
    with dissolve
    mc "You sure about this?"
    k "*nods* I kept it around longer than it deserved."
    k "The only reason I held on was because of him. But I don't need to pretend anymore."
    mc "He'd... see the difference. If that means anything."
    if (klararoute and allornothingroute):
        $ allornothingroutev2 = True
        scene ch2ep1_1012
        with dissolve
        k "*chuckles* He wouldn't. He never looked back."
        scene ch2ep1_1013
        with dissolve
        pause
        scene ch2ep1_1014
        with dissolve
        k "... There's something I've been wanting to ask you."
        mc "Ask, then."
        k "You... don't come to me for the same reason as you do with the others, right?"
        scene ch2ep1_1015
        with dissolve
        mc "What do you mean?"
        k "With the other girls. The way you showed up for them."
        k "Is it..."
        k "... is it the same?"
        scene ch2ep1_1016
        with dissolve
        mc "... Yeah."
        k "I see."
        k "So it's not just me that gets that look from you."
        k "*soft exhale* That shouldn't bother me. But it does."
        scene ch2ep1_1017
        with dissolve
        pause
        scene ch2ep1_1018
        with dissolve
        mc "Klara—"
        k "It's stupid, I know. I don't get to—"
        scene ch2ep1_1019
        with dissolve
        pause
        scene ch2ep1_1020
        with dissolve
        k "It sits here. Right under my ribs. Tight."
        mc "... You're jealous."
        scene ch2ep1_1021
        with dissolve
        k "Does... does Sky—"
    elif klararoute:
        scene ch2ep1_1012
        with dissolve
        k "*chuckles* He wouldn't. He never looked back."
    else:
        scene ch2ep1_1012
        with dissolve
        k "I guess so..."
    play sound3 phonevibrate loop
    scene ch2ep1_1022
    with Dissolve(0.2)
    pause
    scene ch2ep1_1023
    with dissolve
    pause
    scene ch2ep1_1024
    with dissolve
    mc "She can wait."
    k "You should answer it."
    k "She stops by outside my room sometimes. I know about Francis."
    scene ch2ep1_1025
    with dissolve
    k "And you two have work. Real work."
    k "Whatever this is... it isn't going to vanish if you pick up the phone."
    mc "*exhales* Okay."
    play sound3 phoneclick
    scene ch2ep1_1026
    with dissolve
    pause
    scene ch2ep1_1027
    with dissolve
    mc "You don't usually call me."
    e "I know, but this one's urgent—something came in. A lead."
    e "It's not a clean lead yet... but it might point us somewhere."
    mc "Where?"
    play sound4 ceilingfan_low fadein 0.5 loop
    stop sound fadeout 0.5
    stop sound2 fadeout 0.5
    scene ch2ep1_1028
    with dissolve
    e "Old freight depot on Harlow Street. Supposed to be dead, but someone forgot to tell the trucks that."
    mc "You going alone?"
    e "That was... my idea. Then I remembered you've been circling this case like a wolf.."
    mc "And your partner?"
    e "She's checking another location—why? You backing out?"
    stop sound4 fadeout 0.5
    play sound nightambience fadein 0.5 loop
    play sound2 firewood fadein 0.5 loop
    scene ch2ep1_1029
    with dissolve
    mc "Me? No. I just know I can't shove myself into your cases whenever I want."
    e "Already cleared it with the boss. As soon as he heard the Agency you're with, he waved it through."
    mc "... He did?"
    e "Yeah. He said if you come back bleeding, that's your problem, not his."
    mc "Charming."
    e "That's one word for him."
    play sound4 ceilingfan_low fadein 0.5 loop
    stop sound fadeout 0.5
    stop sound2 fadeout 0.5
    scene ch2ep1_1030
    with dissolve
    e "Anyway... figured I'd ask. You want to tag along?"
    mc "Are you calling for backup?"
    e "I'm calling because you catch things I miss. And because I trust you more than most of the idiots at the precinct."
    mc "... Most?"
    scene ch2ep1_1031
    with dissolve
    if emmaroute:
        e "*chuckles* You know I love you, but let's be real—you're not the only competent one in my field, [mc]."
    else:
        e "*chuckles* You're brilliant, but let's be real—you're not the only competent one in my field, [mc]."
    mc "Always the realist, huh?"
    stop sound4 fadeout 0.5
    play sound nightambience fadein 0.5 loop
    play sound2 firewood fadein 0.5 loop
    scene ch2ep1_1032
    with dissolve
    mc "So... what's the plan?"
    e "Meet me at the station in twenty. Bring a jacket. The storm's passed, but the cold hasn't."
    mc "Fine, but only because you asked nicely."
    e "Who was begging to join this case again?"
    mc "Guilty as charged, officer."
    e "Twenty minutes, [mc]. You know the drill—don't be late."
    play sound3 phoneclick
    scene ch2ep1_1033
    with dissolve
    pause
    play sound4 cloth
    scene ch2ep1_1034
    with dissolve
    mc "I have to go."
    k "And there's no chance I can talk you out of it, right?"
    mc "I just got better, I know... but I'll come back in one piece. I swear."
    scene ch2ep1_1035
    with dissolve
    k "Promises don't mean much until you keep them."
    k "And don't try to play hero, alright?"
    play sound3 waterphone
    scene ch2ep1_1036
    with Dissolve(0.1)
    mc "I'm not trying—"
    mc "... to be..."
    mc "*sighs*"
    if (klararoute and klarapoint == 7):
        scene ch2ep1_1053
        with dissolve
        yt "Welp... que sera, sera."
        $ phone_start()
        $ switch_channel_view("klara_dm")
        show screen phone_ui
        $ quick_menu = False
        $ hide_all_phone_channels("klara_dm")
        $ lock_phone_screen()
        $ phone_stamp_rel("klara_dm")
        $ send_phone_message(phone_config["phone_player_name"], "images/ch2ep1_1054b.jpg", "klara_dm", 2)
        $ phone_pause(0.3)
        $ send_phone_message("Klara", "i knew it.", "klara_dm")
        $ phone_pause(0.5)
        $ send_phone_message("Klara", "delete that. now.", "klara_dm")
        $ phone_pause(2.0)
        $ send_phone_message("Klara", "i swear on the ashes of my sanity, [mc], if that photo surfaces, so will your obituary.", "klara_dm")
        $ show_all_phone_channels()
        $ unlock_phone_screen()
        show screen phone_blocker
        show screen phone_close_button
        $ send_phone_message(phone_config["phone_player_name"], "No. No, I don't think I will.", "klara_dm")
        play sound3 cloth
        scene ch2ep1_1055
        with dissolve
        pause
    
    stop sound fadeout 2
    stop sound2 fadeout 2
    call hide_days from _call_hide_days_39
    with dissolve
    scene black
    with dissolve
    $ phone_time_add(minutes=15)
    show ch2ep1end
    pause 129
    scene black
    pause
    play sound police_distant fadein 1 loop
    show theproject
    with dissolve
    pause 21.5
    stop sound fadeout 1
    scene black
    with Dissolve(1.0)
    pause



    jump ch2ep2
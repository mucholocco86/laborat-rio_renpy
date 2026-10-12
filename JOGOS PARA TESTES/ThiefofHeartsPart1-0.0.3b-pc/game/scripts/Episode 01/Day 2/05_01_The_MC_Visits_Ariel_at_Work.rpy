init python:
    from datetime import datetime
    now = datetime.now()
    aw_h_hours = now.strftime("%H:%M")
    aw_date = now.strftime("%A, %B %d")
    def acn_ep01_05_01_Ariel_Work_change_hour():
        now = datetime.now()
        globals() ["aw_h_hours"] = now.strftime("%H:%M")
        globals() ["aw_date"] = now.strftime("%A, %B %d")
        renpy.restart_interaction()

init:
    $ v_ep01_05_01_Ariels_Work_Secret = False
    $ v_ep01_05_01_Ariels_Work_Date = False
    $ v_ep01_task03_visit_ariel_work_counter = 0

    image anim_ep01_ariel_work_walking = Movie(channel="movies_with_sound", loop=False, play="images/extras/Episode 01/anim_ep01_ariel_work_walking.webm", image="sc ariel work a012g")
    image anim_ep01_ariel_work_close1 = Movie(channel="anim_ep01_ariel_work_close1", loop=False, play="images/extras/Episode 01/anim_ep01_ariel_work_close1.webm", image="sc ariel work a086")

    screen scr_ep01_05_01_Ariel_Work_Choices:
        default tt = Tooltip("What will you do now?")
        zorder 10 # These should look like part of the scene, so they should go under things like the music player if they overlap
        add "sc ariel work a038"

        imagebutton:
            focus_mask True
            xpos 1338
            ypos 163
            hovered tt.Action("Go apologize" + If(persistent.v_walkthrough_enabled == True,"{color=#33ff33} (Task point){/color}",""))
            idle "images/Episode 01/Day 02/05-Ariel Work/05-01 Ariel Work/sc ariel work a038 door idle.png"
            hover "images/Episode 01/Day 02/05-Ariel Work/05-01 Ariel Work/sc ariel work a038 door hover.png"
            action [Hide("scr_ep01_05_01_Ariel_Work_Choices"),Jump("lb_ep01_05_01_Ariel_Work_3")]

        imagebutton:
            focus_mask True
            xpos 714
            ypos 31
            hovered tt.Action("Wait for her")
            idle "images/Episode 01/Day 02/05-Ariel Work/05-01 Ariel Work/sc ariel work a038 mc idle.png"
            hover "images/Episode 01/Day 02/05-Ariel Work/05-01 Ariel Work/sc ariel work a038 mc hover.png"
            action [Hide("scr_ep01_05_01_Ariel_Work_Choices"),Jump("lb_ep01_05_01_Ariel_Work_2")]

        frame:
            xfill True
            xalign 0.5
            yalign 0.0
            vbox:
                xalign 0.5
                yalign 0.5
                text tt.value

    screen scr_ep01_05_01_Ariel_Work_Computer_Time:
        zorder -10 # These should look like part of the scene, so they should go under things like the music player if they overlap
        add "sc ariel work a077"
        #add "black"
        timer 0.30 action acn_ep01_05_01_Ariel_Work_change_hour repeat False
        text "[aw_h_hours]":
            xalign 0.94
            yalign 0.19
            font "SegUIVar_SemiboldDisplay.ttf"
            color "#ffffff"
            size 120
            bold False
        text "[aw_date]":
            xalign 0.915
            yalign 0.334
            font "SegUIVar_SemiboldDisplay.ttf"
            color "#ffffff"
            size 22
            bold False

    image sc ariel work walk:
        "sc ariel work a012a" with Dissolve(0.2, alpha=True)
        pause 0.5
        "sc ariel work a012b" with Dissolve(0.2, alpha=True)
        pause 0.5
        "sc ariel work a012c" with Dissolve(0.2, alpha=True)
        pause 0.5
        "sc ariel work a012d" with Dissolve(0.2, alpha=True)
        pause 0.5
        "sc ariel work a012e" with Dissolve(0.2, alpha=True)
        pause 0.5
        "sc ariel work a012f" with Dissolve(0.2, alpha=True)
        pause 0.5
        "sc ariel work a012g" with Dissolve(0.2, alpha=True)

    image sc ariel work mc scare:
        "sc ariel work a026" with Dissolve(0.2, alpha=True)
        pause 0.5
        "sc ariel work a027" with Dissolve(0.2, alpha=True)
        pause 1.3
        "sc ariel work a028" with Dissolve(0.2, alpha=True)
        pause 1.3
        "sc ariel work a029" with Dissolve(0.2, alpha=True)
        pause 0.5

    image sc ariel work changing wip:
        "wip_ep01_ariel_work_01a" with Dissolve(0.2, alpha=True)
        pause 1.5
        "wip_ep01_ariel_work_01b" with Dissolve(0.2, alpha=True)
        pause 1.5
        "wip_ep01_ariel_work_01c" with Dissolve(0.2, alpha=True)
        pause 1.5
        "wip_ep01_ariel_work_01d" with Dissolve(0.2, alpha=True)

    layeredimage sc ariel work computer booting:
        always:
            "sc ariel work a075"

        always:
            "sc ariel work computer booting anim"

    image sc ariel work computer booting anim:
        "sc ariel work a075a" with Dissolve(0.2, alpha=True)
        pause 0.5
        "sc ariel work a075b" with Dissolve(0.2, alpha=True)
        pause 0.5
        "sc ariel work a075c" with Dissolve(0.2, alpha=True)
        pause 0.5
        repeat

label lb_ep01_05_01_Ariel_Work_1:
    #SCENE BEGINS
    #scene starts with the MC entering Ariel’s place of work
    #The MC enters the shop and there will be two guys at the front counter. One of them is Asian, of course
    $ renpy.music.set_volume(0.2, 0.0, channel="ambient")
    play ambient "sound effects/01/town_traffic_ambience.ogg" loop fadein 1.0
    play sound "sound effects/01/store_door_chime.mp3"
    scene sc ariel work a001
    with dissolve
    mc"(I’m pretty sure that this the place.)"
    stop sound fadeout 1.0
    show sc ariel work a002
    mc"(I can’t see [a_name] at the counter. Perhaps she’s working in a different department.)"
    mc"(I’m sure one of these guys will know.)"
    #the MC approaches the counter"
    show sc ariel work a003
    mc"Excuse me, I’m looking for [a_name]. Do you know where I can find her?"
    show sc ariel work a004
    clerk1"She’s in the back repairing some computers."
    show sc ariel work a005
    mc"Can I see her?"
    show sc ariel work a006
    clerk2"No can do, buddy."
    clerk2"Only employees are allowed back there."
    show sc ariel work a003
    mc"It would only be for a few minutes."
    show sc ariel work a004
    clerk1"She’ll be here shortly."
    show sc ariel work a006
    clerk2"Or in an hour. Who knows how long she’ll be."
    #the guys don’t look him in the eye when they are speaking to the MC"
    show sc ariel work a007
    mc"(These guys are fucking with me.)"
    show sc ariel work a008
    mc"(And they couldn’t care less what I want.)"
    show sc ariel work a009
    mc"(If only there was a way to distract them. Then I can go see [a_name].)"
    show sc ariel work a010
    clerk1"Dude... Look."
    #clerk 1 looks up at someone entering the computer store and nudges clerk2
    show sc ariel work a011
    clerk2"Woah, dude..."
    #Shortly after, a hot chick enters the shop asking for computer help, which makes the guys drop their jaws.
    #Base her on this chick - https://www.instagram.com/p/CtM1j3zPIg6/
    #IDEA - add in a slow-mo of her walking towards the counter and the MC looking at her with his eyebrows raised
    play sound "sound effects/01/store_door_chime.mp3"
    if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
        scene sc ariel work a012_wip at tt_top
        pause
    elif True:
        scene sc ariel work a012
    mc"(Now that’s one hell of a distraction!)"
    stop sound fadeout 1.0
    $ renpy.music.set_volume(0.5, 0.0, channel="ambient")
    if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
        if persistent.v_anim_enabled:
            scene anim_ep01_ariel_work_walking:
                size (config.screen_width, config.screen_height)
        else:
            show sc ariel work walk
        $ renpy.music.set_volume(0.2, 3.0, channel="ambient")
        pause 1.0
        clerk2"Holy moly!" (multiple=2)
        clerk1"Woah!" (multiple=2)
        clerk2"{i}(*Whispering*){/i}\nShe's so hot that she could wear a retainer or headgear and still be hot!"
        clerk1"{i}(*Whispering*){/i}\nShe's so hot that she'll melt your hard drive!"
        mc"(Wow, that was pretty cringe. Luckily, she couldn't hear them.)"
        mc"(All the right things jiggle so perfectly, I can see why those two are so gobsmacked.)"
        clerk1"{i}(*Whispering*){/i}\nShhh, here she comes..."
        clerk2"{i}(*Whispering*){/i}\nBe cool dude, be cool."
        pause
    elif True:
        $ renpy.music.set_volume(0.2, 3.0, channel="ambient")
        show sc ariel work a012a
        with fast_dissolve
        clerk2"Holy moly!" (multiple=2)
        clerk1"Woah!" (multiple=2)
        show sc ariel work a012b
        with fast_dissolve
        clerk2"{i}(*Whispering*){/i}\nShe's so hot that she could wear a retainer or headgear and still be hot!"
        clerk1"{i}(*Whispering*){/i}\nShe's so hot that she'll melt your hard drive!"
        show sc ariel work a012c
        with fast_dissolve
        mc"(Wow, that was pretty cringe. Luckily, she couldn't hear them.)"
        show sc ariel work a012d
        with fast_dissolve
        mc"(All the right things jiggle so perfectly, I can see why those two are so gobsmacked.)"
        show sc ariel work a012e
        with fast_dissolve
        clerk2"{i}(*Whispering*){/i}\nShhh, here she comes..."
        # maybe clerk1 should say this?
        clerk2"{i}(*Whispering*){/i}\nBe cool dude, be cool."
        pause 1.0
    scene sc ariel work a013
    blonde"Excuse me, I was wondering if you could help me."
    show sc ariel work a014
    clerk2"What seems to be the problem?" (multiple=2)
    clerk1"Anything for you, m’lady." (multiple=2)
    show sc ariel work a015
    blonde"It’s the strangest thing."
    blonde"I went to bed last night. Then I woke up and my phone wouldn’t turn on."
    blonde"It’s brand-new."
    show sc ariel work a016
    clerk2"It probably just needs charging."
    show sc ariel work a017
    blonde"It had like ten percent of battery on it when I went to bed last night."
    blonde"I used it all day yesterday and it worked just fine."
    show sc ariel work a018
    mc"(Oh my God... Is she fucking kidding?)"
    show sc ariel work a019
    clerk1"Yeah, I know. It’s a pain, isn’t it?"
    clerk2"It really could happen to anyone."
    show sc ariel work a020
    with dissolve
    blonde"I have a few more questions if you don’t mind?"
    show sc ariel work a021
    clerk2"No, not at all, miss."
    #show the two clerks who can’t take their eyes off her"
    show sc ariel work a022
    mc"(It looks like these two will be occupied for a while.)"
    stop ambient fadeout 1.0
    #show the MC slipping beyond the two clerks while they attend to the ditzy blonde
    if v_ep01_work_visit_options_1 == "[a_name]" or v_ep01_work_visit_options_2 == "[a_name]":
        #*BONUS SCENE and OPTIONS: Only available if the player chooses to visit Ariel either first or second.
        #If the player chooses to visit her last, then Ariel does not spill the drink on herself.
        #If the player chooses to visit her last, then > GO DOWN TO > "LAST OPTION = ARIEL".
        #The MC finds Ariel sitting at her desk in her work uniform - she’s trying to boot a computer but it doesn’t turn on"
        $ renpy.music.set_volume(1.0, 0.0, channel="ambient")
        show sc ariel work a023
        mc"(There she is.)"
        $ v_ep01_task03_visit_ariel_work_counter += 2
        play sound "sound effects/01/door_open_light.mp3" noloop
        #mc"(While she’s distracted, I'll surprise her.)"
        show sc ariel work a024
        mc"(Hehehe...)"
        stop sound fadeout 1.0
        #show a close-up of Ariel looking at the PC Tower"
        show sc ariel work a025
        a"(Hmm... What am I missing here? Usually I've figured this out by now.)"
        #younger sis picks up her cup of iced mochaccino"
        #the MC puts his hands over her eyes
        show sc ariel work mc scare
        $ ui.timer(0.4, Play("sound", "sound effects/01/taking_a_drink.mp3"))
        $ renpy.pause(2.0, hard=True)
        a"Guess who?{p=1.2}{nw}"
        #younger sister freaks out and spills the drink over herself
        play sound "sound effects/01/girl_scream.mp3" noloop
        play sound2 "sound effects/01/desk_chair_moving.mp3" noloop
        a"Aiii!!{p=1.2}{nw}"
        play sound3 "sound effects/01/male_grunt_gut_punch.mp3" noloop
        show sc ariel work a030
        with hpunch
        mc"(UGH!){p=0.4}{nw}"
        #mc"(Uh-oh.)"
        show sc ariel work a031
        with vpunch
        mc"OH, FUCK ME... MY BOYS!"
        stop sound fadeout 1.0
        stop sound2 fadeout 1.0
        stop sound3 fadeout 1.0
        a"JESUS CHRIST, [y_name!u]!"
        a"What the hell are you doing back here??"
        a"You scared the shit out of me!"
        show sc ariel work a033
        mc"I'm sorry about that. I needed to see you and thought it would be funny to surprise you."
        show sc ariel work a032
        a"That's karma for ya."
        show sc ariel work a034
        mc"Yeah..."
        mc"Ow, shit... You got me right in the sack nuggets! Owww."
        #younger sis stands up and we see the mess all over her work uniform
        show sc ariel work a035
        a"Damn it, [y_name]!"
        play sound "sound effects/01/door_open_light.mp3" noloop
        show sc ariel work a036
        a"Wait right here, and don’t touch anything while I get this cleaned up."
        stop sound fadeout 1.0
        show sc ariel work a037
        mc"Sure thing."
        #younger sis leaves the back office and goes to the bathroom
        show sc ariel work a038
        mc"(Well shit... That was a stupid idea. I feel really bad now.)"
        mc"(Maybe I go should tell her that I'm sorry.)"
        call screen scr_ep01_05_01_Ariel_Work_Choices with Dissolve(0.2) onlayer master
    else:
        #"LAST OPTION = ARIEL"
        #the MC goes out to the back room but it’s empty
        $ renpy.music.set_volume(1.0, 0.0, channel="ambient")
        show sc ariel work a054
        mc"(Hmm... She’s not here.)"
        show sc ariel work a055
        pause 1.0
        play sound "sound effects/01/door_open_light.mp3" noloop
        #Ariel walks in from another room
        show sc ariel work a045
        a"[y_name]!"
        stop sound fadeout 1.0
        show sc ariel work a047
        a"How did you manage to get back here?"
        show sc ariel work a046
        mc"Let’s just say that your co-workers out front are eyeballs deep into a ditzy blonde’s cleavage they’re attending to right now."
        show sc ariel work a051
        a"Yeah, that sure sounds like them."
        show sc ariel work a047
        a"I'm glad you did not go any further back there."
        show sc ariel work a048
        a"I got a tad angry at that PC over there and had an accident with my drink, so I had to go change."
        a"That would have been mortifiying had you walked in on me."
        jump lb_ep01_05_01_Ariel_Work_4

label lb_ep01_05_01_Ariel_Work_2:
    #"Wait for her"
    mc"(I better do as she says so I don’t fuck anything else up!)"
    #screen goes blank
    scene black
    with dissolve
    scene black
    with Pause (2)
    #the MC waits out by Ariel’s computer
    play music "sound effects/01/Canvas Dreams.mp3" loop fadein 1.0
    show sc ariel work a045
    with dissolve
    a"Okay, all better now."
    # Ariel returns and she’s now wearing a clean pair of work clothes
    show sc ariel work a046
    mc"[a_name]... I’m really sorry about what happened."
    mc"It was meant to be a surprise. I didn’t mean to freak you out like that."
    show sc ariel work a047
    a"No harm done. It's good I kept a spare change of clothes here."
    show sc ariel work a048
    a"Though it might be a bit revealing for the workplace, I suppose it's better than walking around in my birthday suit."
    show sc ariel work a049
    a"I just wish I'd kept a spare bra or undershirt here."
    mc"Again, I'm very sorry [a_name]."
    show sc ariel work a050
    a"Don’t worry about it"
    jump lb_ep01_05_01_Ariel_Work_4

label lb_ep01_05_01_Ariel_Work_3:
    #"Go apologize"
    show sc ariel work a039
    mc"(I know she told me to wait here, but I really should go and apologize.)"
    $ v_ep01_task03_visit_ariel_work_counter += 1
    #the MC heads to the other room where Ariel went"
    #screen goes blank
    scene black
    with dissolve
    scene black
    with Pause (2)
    #the MC is in the back area where there a changing rooms and lockers
    show sc ariel work a040
    with dissolve
    mc"[a_name]?"
    mc"Are you here somewhere?"
    show sc ariel work a041a
    mc"(Where did she go?)"
    #the MC looks inside the women’s locker room and sees Ariel. She still has her clothes on with the wet stain on it
    play music "sound effects/01/Touch_and_Tension1.mp3" loop fadein 1.0
    show sc ariel work a041
    with fast_dissolve
    mc"(There she is.)"
    #Ariel undoes her skirt and it slides down her legs
    #IDEA - make this into an animation scene - her skirt being undone and sliding down her legs
    show sc ariel work a042
    mc"(I wonder if I should...)"
    if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
        if persistent.v_anim_enabled:
            scene anim_ep01_ariel_work_close1:
                size (config.screen_width, config.screen_height)
        else:
            scene sc ariel work changing wip at tt_bottom
        pause 1.0
        mc"(Oh!!)"
        #Ariel undoes her top so she only has a bra on
        # mc"(Holy crap! I really shouldn't be here, but I can't seem to look away.)" (duplicate?)
    else:
        show sc ariel work a042a
        mc"(Oh!!)"
        #Ariel undoes her top so she only has a bra on
        show sc ariel work a042b
        # mc"(Holy crap! I really shouldn't be here, but I can't seem to look away.)" (duplicate?)
    mc"(Holy crap! I really shouldn't be here, but I can't seem to look away.)"
    scene sc ariel work a043
    mc"(Wow...)"
    show sc ariel work a043a
    mc"(I never realised how insanely beautiful she is!)"
    #mc"(How have I only just realised how insanely attractive [a_name]?)"
    #Ariel turns around so we can see the back of her in underwear
    show sc ariel work a044
    with faster_dissolve
    mc"(Shit, I better go back before she spots me. I think the apology can wait until she's done.)"
    stop music fadeout 1.0
    #her underwear is riding up between the crack of her ass
    #THREE BONUS RENDERS OF ARIEL (THREE NEW IMAGES OF HER IN HER UNDERWEAR STANDING IN THE WOMEN’S LOCKER ROOM) ADDED TO THE PHOTO GALLERY FOR HER
    #screen goes blank
    scene black
    with dissolve
    scene black
    with Pause (2)
    #the MC waits out by Ariel’s computer
    play music "sound effects/01/Canvas Dreams.mp3" loop fadein 1.0
    show sc ariel work a045
    with dissolve
    a"Okay, all better now."
    # Ariel returns and she’s now wearing a clean pair of work clothes
    show sc ariel work a046
    mc"[a_name]... I’m really sorry about what happened."
    mc"It was meant to be a surprise. I didn’t mean to freak you out like that."
    show sc ariel work a047
    a"No harm done. It's just fortunate that I kept a spare outfit here. I never expected that I would ever need it though."
    show sc ariel work a048
    a"Though it might be a bit revealing for the workplace, I suppose it's better than walking around in my birthday suit."
    show sc ariel work a049
    # remove () to make it consistant with above
    a"I just wish I'd kept a spare bra or undershirt here."
    mc"Again, I'm very sorry [a_name]."
    show sc ariel work a050
    a"Don’t worry about it"


label lb_ep01_05_01_Ariel_Work_4:
    show sc ariel work a047
    a"So what brings you here?"
    show sc ariel work a046
    mc"I wanted to see if I could talk to you regarding yesterday’s job. I wanted to ask you about it this morning but I overslept."
    #Ariel sits down at another computer and starts typing
    #the MC stands to the side and behind her, looking over her shoulder
    show sc ariel work a052
    a"I might have some info for you on that."
    a"I found a few potential sites where that girl could look at selling the drive."
    show sc ariel work a052a
    a"It’s just a matter of when and where she decides to sell it."
    a"If that’s her intention."
    mc"Good work, [mc_a_address]."
    show sc ariel work a053
    a"Any news from [b_name] on the tattoo parlours [mc_vic_address] wants you both to check out?"
    show sc ariel work a056
    if v_ep01_work_visit_options_1 == "[b_name]" or v_ep01_work_visit_options_2 == "[b_name]":
        #"Add these lines if the player has already visited Bella"
        mc"Yeah, I just went to see her at the clothing store."
        mc"We’re going to visit one parlour in particular as soon as her shift finishes."
    else:
        #"Add these lines if the player hasn’t visited Bella yet"
        mc"Not yet, but I’m going to see her at the clothing store shortly."
        mc"I’m pretty sure we’re going to meet up somewhere after her shift finishes."
    show sc ariel work a057
    a"I couldn’t find anything on that tattoo."
    a"Which tells me that it’s a specific design this girl either personally requested, or it’s a design from a club or some underground group."
    show sc ariel work a058
    mc"Well, we’ll find out soon enough."
    show sc ariel work a053
    a"Anyway, I’m glad that you’re here as there was something I wanted to discuss with you."
    show sc ariel work a058
    mc"What did you want to talk about?"
    show sc ariel work a059
    a"[mc_vic_address] has asked me to get two key cards from a security company in town."
    show sc ariel work a060
    mc"Sounds like a big job."
    show sc ariel work a059
    a"You’re not wrong."
    a"And when I say \"get\", I’m pretty sure he means \"steal\"."
    show sc ariel work a061
    mc"Yeah, I kind of figured that."
    show sc ariel work a062
    a"I’m not sure if I can handle this alone. I might ask him for some help with this job."
    show sc ariel work a058
    mc"Do you have any more information about this security company?"
    show sc ariel work a057
    a"Okay, so, pretty much all the rich houses on the other side of town use this company for their security systems."
    a"That includes schools and local businesses. Even churches."
    show sc ariel work a062
    a"Here, take a look."
    #Ariel shows pictures of the company on the computer.
    show sc ariel work a064
    mc"This is the company?"
    show sc ariel work a065
    a"Yeah, that’s the big momma."
    #next she shows him a map of the rich neighbourhood and it also shows the school locations
    show sc ariel work a066
    a"Here’s the map of the neighbourhood surrounding the business."
    show sc ariel work a067
    mc"What’s that place there?"
    #the MC points to the school on the map
    show sc ariel work a066
    a"That’s the local school."
    show sc ariel work a068
    mc"I see."
    #"Add these lines if the player has already visited Bella"
    if v_ep01_04_01_Bella_Work_Date:
        show sc ariel work a056
        mc"Do you know if that school has an art department?"
        show sc ariel work a057
        a"I think so. Let me check."
        #Ariel looks up some information on the school
        show sc ariel work a069
        mc"(If it does, then that could be the place to get the items [b_name] requires.)"
        a"Yes it does. Why do you want to know?"
        show sc ariel work a070
        mc"I’ll tell you when the time is right."
    #scene continues
    show sc ariel work a061
    mc"So how are you planning on getting those cards?"
    show sc ariel work a062
    a"I honestly have no idea."
    a"I’ve been working on passing myself off as someone who works there so I can walk around freely once I'm inside."
    show sc ariel work a065
    a"But after that, I’m not sure."
    a"I’d need to make sure that no one suspects who I am and I'll need enough time to get copies of those cards."
    show sc ariel work a059
    a"If I fail, then it could mean aborting the next job. Those were [mc_vic_address]’s words, not mine."
    show sc ariel work a071
    #[Don’t respond  / Work with her]
    menu:
        "Don’t respond":
            mc"(I could offer to help her, but [mc_vic_address] has assigned [a_name] this job)."
            mc"(Maybe I should wait until she asks me to help her.)"
            #IMPORTANT: Choosing this option will lock any chance of having a special date with Ariel after the task has been completed.
            #Make sure to set up a variable for this choice
        "Work with her"(wt="You will have a 'Special Date' scene with [a_name] at a local cafe + Task Point"):
            #mc"(I can’t let her do this alone.)"
            show sc ariel work a069
            mc"(If [mc_vic_address] finds out that I helped [a_name] and we succeed in our mission, then that can only be a good thing for both of us.)"
            mc"(Plus I kind of owe her for offering to help me try and get the drive back.)"
            $ v_ep01_task02_girls_tattoo_counter += 1
            show sc ariel work a056
            mc"Well, what if I go with you?"
            show sc ariel work a053
            a"Really? You’d help me?"
            show sc ariel work a072
            mc"Yeah, sure I will. You'll need someone to help you get in and out without getting caught."
            $ v_ep01_task03_visit_ariel_work_counter += 2
            show sc ariel work a073
            mc"And also someone to be a distraction so you can do your thing."
            mc"So how about it?"
            show sc ariel work a074
            a"Thanks, [y_name]. That’d be great!"
            $ v_ep01_05_01_Ariels_Work_Date = True
            #Ariel smiles
            #IMPORTANT: Choosing this option will unlock a special date with Ariel after the task has been completed.
            #Make sure to set up a variable for this choice
    #scene continues
    #the computer makes a sound to show it’s now booting up properly
    play sound "sound effects/01/computer_beep.ogg" noloop
    pause 0.5
    if persistent.v_anim_enabled:
        show sc ariel work computer booting
        with faster_dissolve
    else:
        show sc ariel work a075a
        with faster_dissolve
    a"Oh, finally!"
    stop sound fadeout 1.0
    if v_ep01_task03_visit_ariel_work_counter == 5:
        $ task_completed(3,"aa")
        $ v_ep01_ariel_aa_tasks_counter += 1
    if v_ep01_task03_visit_ariel_work_counter == 4:
        $ task_completed(3,"a")
    if v_ep01_task03_visit_ariel_work_counter == 3:
        $ task_completed(3,"b")
    if v_ep01_task03_visit_ariel_work_counter == 2:
        $ task_completed(3,"c")
    if v_ep01_task03_visit_ariel_work_counter <= 1:
        $ task_completed(3,"d")
    a"I was about to give up on this darn thing!"
    mc"Give up? That’s not in your nature."
    mc"You always figure these things out, [a_name]."
    #the screen shows a funny startup image - https://pixhost.to/show/620/443494492_sfw-porn-memes-1.png
    play sound "sound effects/01/computer_boot.ogg" noloop
    scene sc ariel work a076
    scene onlayer anim_layer
    a"Oh!!"
    stop sound fadeout 1.0
    show screen scr_ep01_05_01_Ariel_Work_Computer_Time
    mc"(Well, well... I wasn’t expecting something like this on her work computer.)"
    mc"(It’s pretty funny though.)"
    hide screen scr_ep01_05_01_Ariel_Work_Computer_Time
    show sc ariel work a078
    a"Um... That’s not mine. I swear."
    #Ariel opens up a screen so it’s not showing anymore"
    show sc ariel work a079
    mc"(I get the impression those two dimwits out front are playing a practical joke on her.)"
    mc"Hey, don’t worry about it."
    mc"I met your co-workers so this doesn't surprise to me at all."
    show sc ariel work a080
    a"Oh..."
    show sc ariel work a076a
    mc"However, I’d change it as soon as you can."
    show sc ariel work a081a
    mc"Just in case your boss sees it and thinks that you’re responsible."
    show sc ariel work a081
    a"Yeah, I’ll do that shortly."
    show sc ariel work a082
    a"I'll just hide it for now."
    show sc ariel work a083
    mc"Anyway... I’ll let you get back to work."
    mc"See you at home, [a_name]."
    show sc ariel work a084
    a"Bye, [a_mc_address]."
    stop music fadeout 1.0
    #the MC leaves the back workroom and heads back past the front counter
    #the two guys are still talking with the blonde
    play sound "sound effects/01/door_close_soft.mp3" noloop
    show sc ariel work a085
    with faster_dissolve
    mc"(Ah geez... How the hell is that girl still here?)"
    mc"(Man, I'd hate to be in that line...)"
    #show the MC walking towards the exit and there’s a long queue that has formed behind the blonde - the men are checking her out and the women look pissed off!
    #screen goes blank
    stop sound fadeout 1.0
    scene black
    with dissolve
    scene black
    with Pause (2)
    #END SCENE
    #NEXT SCENE: ToH’s ep01 Scene 06-01

    #TEMP MENU UNTIL INTERACTABLE MENU MADE
    show sc mctown m02
    if(v_ep01_work_visit_options_2 == "" or v_ep01_work_visit_options_3 == ""):
        menu:
            "Clothing Store ([b_name])" if (v_ep01_work_visit_options_1 != "[b_name]" and v_ep01_work_visit_options_2 != "[b_name]"):
                #"If the player clicks on the CLOTHING STORE (scene with BELLA)"
                if v_ep01_work_visit_options_2 == "":
                    $ v_ep01_work_visit_options_2 = "[b_name]"
                else:
                    $ v_ep01_work_visit_options_3 = "[b_name]"
                scene black
                with dissolve
                pause 2.0
                jump lb_ep01_04_01_Bella_Work_1

            "Computer Shop ([a_name])" if (v_ep01_work_visit_options_1 != "[a_name]" and v_ep01_work_visit_options_2 != "[a_name]"):
                #"If the player clicks on the COMPUTER SHOP (scene with ARIEL)"
                if v_ep01_work_visit_options_2 == "":
                    $ v_ep01_work_visit_options_2 = "[a_name]"
                else:
                    $ v_ep01_work_visit_options_3 = "[a_name]"
                #the screen will go blank and take the player to the computer shop
                scene black
                with dissolve
                pause 2.0
                jump lb_ep01_05_01_Ariel_Work_1

            "Restaurant ([v_name])" if (v_ep01_work_visit_options_1 != "[v_name]" and v_ep01_work_visit_options_2 != "[v_name]"):
                #"If the player clicks on the RESTAURANT (scene with Vivian)"
                if v_ep01_work_visit_options_2 == "":
                    $ v_ep01_work_visit_options_2 = "[v_name]"
                else:
                    $ v_ep01_work_visit_options_3 = "[v_name]"
                #the screen will go blank and take the player to the restaurant"
                scene black
                with dissolve
                pause 2.0
                jump lb_ep01_06_01_Vivian_Work_1
    else:
        jump lb_ep01_06_02_Tattoo_Parlour_1

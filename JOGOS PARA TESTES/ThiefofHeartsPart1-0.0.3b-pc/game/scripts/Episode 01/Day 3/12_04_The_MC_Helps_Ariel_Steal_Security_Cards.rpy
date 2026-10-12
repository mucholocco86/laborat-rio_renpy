init:
    $ v_ep01_12_04_card_theft_desk_choice = ""
    $ v_ep01_12_04_card_theft_complete = False
    $ v_ep01_12_04_card_theft_mc_drop_first = False
    $ v_ep01_12_04_card_theft_security_code = ""
    $ v_ep01_task07_help_ariel_counter = 0
    $ v_ep01_12_04_card_theft_code_failed = 0

    transform tt_12_04_Card_Thef_Look_Down:
        xpos 0    ## or anything else slightly outside your screen
        ypos 0
        easein 4 xpos 0 ypos -1065   ## or wherever you want it to end up

    image sc cardtheft elevator open1:
        "sc cardtheft a039" with Dissolve(0.2, alpha=True)
        pause 0.8
        "sc cardtheft a039a" with Dissolve(0.2, alpha=True)
        pause 0.8
        "sc cardtheft a039b" with Dissolve(0.2, alpha=True)

    image sc cardtheft steal badge1:
        "sc cardtheft a047" with Dissolve(0.1, alpha=True)
        pause 0.8
        "sc cardtheft a047a" with Dissolve(0.1, alpha=True)
        pause 0.8
        "sc cardtheft a047b" with Dissolve(0.1, alpha=True)
        pause 0.8
        "sc cardtheft a047c" with Dissolve(0.1, alpha=True)
        pause 0.8
        "sc cardtheft a047d" with Dissolve(0.1, alpha=True)

    image sc cardtheft steal badge2:
        "sc cardtheft a048" with Dissolve(0.2, alpha=True)
        pause 0.8
        "sc cardtheft a048a" with Dissolve(0.2, alpha=True)
        pause 0.8
        "sc cardtheft a048b" with Dissolve(0.2, alpha=True)
        pause 0.8
        "sc cardtheft a048c" with Dissolve(0.2, alpha=True)
        pause 0.8
        "sc cardtheft a047d" with Dissolve(0.2, alpha=True)

    image sc cardtheft steal badge3:
        "sc cardtheft a069" with Dissolve(0.2, alpha=True)
        pause 0.5
        "sc cardtheft a069a" with Dissolve(0.2, alpha=True)

    image sc cardtheft tap cheek:
        "sc cardtheft a074a" with Dissolve(0.2, alpha=True)
        pause 0.6
        "sc cardtheft a074" with Dissolve(0.2, alpha=True)
        pause 0.2
        repeat

    image sc cardtheft elevator close1:
        "sc cardtheft a085" with Dissolve(0.2, alpha=True)
        pause 0.8
        "sc cardtheft a085a" with Dissolve(0.2, alpha=True)
        pause 0.8
        "sc cardtheft a085b" with Dissolve(0.2, alpha=True)

    image sc cardtheft elevator open2:
        "sc cardtheft a097" with Dissolve(0.2, alpha=True)
        pause 0.8
        "sc cardtheft a097a" with Dissolve(0.2, alpha=True)
        pause 0.8
        "sc cardtheft a097b" with Dissolve(0.2, alpha=True)

    image sc cardtheft slide card:
        "sc cardtheft a099" with Dissolve(0.2, alpha=True)
        pause 0.8
        "sc cardtheft a099a" with Dissolve(0.2, alpha=True)
        pause 0.8
        "sc cardtheft a099b" with Dissolve(0.2, alpha=True)

    image sc cardtheft turn on lights:
        "sc cardtheft a101" with Dissolve(0.2, alpha=True)
        pause 0.8
        "sc cardtheft a101a" with Dissolve(0.2, alpha=True)

    image sc cardtheft tap leg1:
        "sc cardtheft a128" with Dissolve(0.2, alpha=True)
        pause 0.5
        "sc cardtheft a128a" with Dissolve(0.2, alpha=True)
        pause 0.5
        "sc cardtheft a128" with Dissolve(0.2, alpha=True)
        pause 0.5
        "sc cardtheft a128a" with Dissolve(0.2, alpha=True)
        pause 0.5

    image sc cardtheft tap leg2:
        "sc cardtheft a128b" with Dissolve(0.2, alpha=True)
        pause 0.5
        "sc cardtheft a128c" with Dissolve(0.2, alpha=True)
        pause 0.5
        "sc cardtheft a128b" with Dissolve(0.2, alpha=True)
        pause 0.5
        "sc cardtheft a128c" with Dissolve(0.2, alpha=True)
        pause 0.5

    image sc cardtheft alarm1:
        "sc cardtheft a150" with Dissolve(0.2, alpha=True)
        pause 0.4
        "sc cardtheft a150a" with Dissolve(0.2, alpha=True)
        pause 0.4
        repeat

    image sc cardtheft alarm2:
        "sc cardtheft a151" with Dissolve(0.2, alpha=True)
        pause 0.4
        "sc cardtheft a151a" with Dissolve(0.2, alpha=True)
        pause 0.4
        repeat

    image sc cardtheft alarm3:
        "sc cardtheft a152" with Dissolve(0.2, alpha=True)
        pause 0.4
        "sc cardtheft a152a" with Dissolve(0.2, alpha=True)
        pause 0.4
        repeat

    image sc cardtheft alarm4:
        "sc cardtheft a153" with Dissolve(0.2, alpha=True)
        pause 0.4
        "sc cardtheft a153a" with Dissolve(0.2, alpha=True)
        pause 0.4
        repeat

    image sc cardtheft alarm5:
        "sc cardtheft a154" with Dissolve(0.2, alpha=True)
        pause 0.4
        "sc cardtheft a154a" with Dissolve(0.2, alpha=True)
        pause 0.4
        repeat

    image sc cardtheft alarm6:
        "sc cardtheft a155" with Dissolve(0.2, alpha=True)
        pause 0.4
        "sc cardtheft a155a" with Dissolve(0.2, alpha=True)
        pause 0.4
        repeat

    image sc cardtheft alarm7:
        "sc cardtheft a156" with Dissolve(0.2, alpha=True)
        pause 0.4
        "sc cardtheft a156a" with Dissolve(0.2, alpha=True)
        pause 0.4
        repeat

    image sc cardtheft open hatch:
        "sc cardtheft a163" with Dissolve(0.2, alpha=True)
        pause 1.0
        "sc cardtheft a163a" with Dissolve(0.2, alpha=True)

    image sc cardtheft tube loop1:
        "sc cardtheft a171" with Dissolve(0.2, alpha=True)
        pause 0.4
        "sc cardtheft a171a" with Dissolve(0.2, alpha=True)
        pause 0.4
        "sc cardtheft a171b" with Dissolve(0.2, alpha=True)
        pause 0.4
        repeat

    image sc cardtheft tube loop2:
        "sc cardtheft a177" with Dissolve(0.2, alpha=True)
        pause 0.4
        "sc cardtheft a177a" with Dissolve(0.2, alpha=True)
        pause 0.4
        "sc cardtheft a177b" with Dissolve(0.2, alpha=True)
        pause 0.4
        repeat

    image sc cardtheft tube drop mc:
        "sc cardtheft a172" with Dissolve(0.2, alpha=True)
        pause 0.1
        "sc cardtheft a172a" with Dissolve(0.2, alpha=True)
        pause 0.1
        "sc cardtheft a172b" with Dissolve(0.2, alpha=True)
        pause 0.1
        "sc cardtheft a172c" with Dissolve(0.2, alpha=True)
        pause 0.1
        "sc cardtheft a172d" with Dissolve(0.2, alpha=True)
        pause 0.1

    image sc cardtheft mc hatch drop ariel1:
        "sc cardtheft a176a" with Dissolve(0.2, alpha=True)
        pause 0.8
        "sc cardtheft a176b" with Dissolve(0.2, alpha=True)

    image sc cardtheft mc hatch drop ariel2:
        "sc cardtheft a196a" with Dissolve(0.2, alpha=True)
        pause 0.8
        "sc cardtheft a196b" with Dissolve(0.2, alpha=True)

    image sc cardtheft mc footsie1:
        "sc cardtheft a203" with Dissolve(0.2, alpha=True)
        pause 2.0
        "sc cardtheft a203a" with Dissolve(0.2, alpha=True)
        pause 2.0
        repeat

    image sc cardtheft mc footsie2:
        "sc cardtheft a204" with Dissolve(0.2, alpha=True)
        pause 1.0
        "sc cardtheft a204a" with Dissolve(0.2, alpha=True)
        pause 1.0
        repeat

    image sc cardtheft mc footsie3:
        "sc cardtheft a204" with Dissolve(0.2, alpha=True)
        pause 0.5
        "sc cardtheft a204a" with Dissolve(0.2, alpha=True)
        pause 0.5
        repeat

    screen scr_ep01_12_04_Vault_Combo:
        zorder -10 # These should look like part of the scene, so they should go under things like the music player if they overlap
        add "sc cardtheft a147"
        text v_ep01_12_04_card_theft_security_code xalign 0.438 yalign 0.235

        imagebutton:
            idle "images/Episode 01/Day 03/12-MC Jobs/12-04 Card Theft/combo_keys_idle.png"
            hover "images/Episode 01/Day 03/12-MC Jobs/12-04 Card Theft/combo_keys_hover.png"
            xalign 0.3915
            yalign 0.302
            focus_mask True
            action [
                Play("sound2","sound effects/01/keypad_beep.ogg"),
                If(len(v_ep01_12_04_card_theft_security_code+"1") < 6,true=SetVariable("v_ep01_12_04_card_theft_security_code",v_ep01_12_04_card_theft_security_code+"1"),false=If(v_ep01_12_04_card_theft_security_code+"1" == "210224",true=Jump("lb_ep01_12_04_card_theft_success"), false=[SetVariable("v_ep01_12_04_card_theft_security_code",""),Jump("lb_ep01_12_04_card_theft_failed")]))
                ]

        imagebutton:
            idle "images/Episode 01/Day 03/12-MC Jobs/12-04 Card Theft/combo_keys_idle.png"
            hover "images/Episode 01/Day 03/12-MC Jobs/12-04 Card Theft/combo_keys_hover.png"
            xalign 0.4351
            yalign 0.302
            focus_mask True
            action [
                Play("sound2","sound effects/01/keypad_beep.ogg"),
                If(len(v_ep01_12_04_card_theft_security_code+"2") < 6,true=SetVariable("v_ep01_12_04_card_theft_security_code",v_ep01_12_04_card_theft_security_code+"2"),false=If(v_ep01_12_04_card_theft_security_code+"2" == "210224",true=Jump("lb_ep01_12_04_card_theft_success"), false=[SetVariable("v_ep01_12_04_card_theft_security_code",""),Jump("lb_ep01_12_04_card_theft_failed")]))
                ]

        imagebutton:
            idle "images/Episode 01/Day 03/12-MC Jobs/12-04 Card Theft/combo_keys_idle.png"
            hover "images/Episode 01/Day 03/12-MC Jobs/12-04 Card Theft/combo_keys_hover.png"
            xalign 0.4792
            yalign 0.302
            focus_mask True
            action [
                Play("sound2","sound effects/01/keypad_beep.ogg"),
                If(len(v_ep01_12_04_card_theft_security_code+"3") < 6,true=SetVariable("v_ep01_12_04_card_theft_security_code",v_ep01_12_04_card_theft_security_code+"3"),false=If(v_ep01_12_04_card_theft_security_code+"3" == "210224",true=Jump("lb_ep01_12_04_card_theft_success"), false=[SetVariable("v_ep01_12_04_card_theft_security_code",""),Jump("lb_ep01_12_04_card_theft_failed")]))
                ]

        imagebutton:
            idle "images/Episode 01/Day 03/12-MC Jobs/12-04 Card Theft/combo_keys_idle.png"
            hover "images/Episode 01/Day 03/12-MC Jobs/12-04 Card Theft/combo_keys_hover.png"
            xalign 0.3915
            yalign 0.38
            focus_mask True
            action [
                Play("sound2","sound effects/01/keypad_beep.ogg"),
                If(len(v_ep01_12_04_card_theft_security_code+"4") < 6,true=SetVariable("v_ep01_12_04_card_theft_security_code",v_ep01_12_04_card_theft_security_code+"4"),false=If(v_ep01_12_04_card_theft_security_code+"4" == "210224",true=Jump("lb_ep01_12_04_card_theft_success"), false=[SetVariable("v_ep01_12_04_card_theft_security_code",""),Jump("lb_ep01_12_04_card_theft_failed")]))
                ]

        imagebutton:
            idle "images/Episode 01/Day 03/12-MC Jobs/12-04 Card Theft/combo_keys_idle.png"
            hover "images/Episode 01/Day 03/12-MC Jobs/12-04 Card Theft/combo_keys_hover.png"
            xalign 0.4351
            yalign 0.38
            focus_mask True
            action [
                Play("sound2","sound effects/01/keypad_beep.ogg"),
                If(len(v_ep01_12_04_card_theft_security_code+"5") < 6,true=SetVariable("v_ep01_12_04_card_theft_security_code",v_ep01_12_04_card_theft_security_code+"5"),false=If(v_ep01_12_04_card_theft_security_code+"5" == "210224",true=Jump("lb_ep01_12_04_card_theft_success"), false=[SetVariable("v_ep01_12_04_card_theft_security_code",""),Jump("lb_ep01_12_04_card_theft_failed")]))
                ]

        imagebutton:
            idle "images/Episode 01/Day 03/12-MC Jobs/12-04 Card Theft/combo_keys_idle.png"
            hover "images/Episode 01/Day 03/12-MC Jobs/12-04 Card Theft/combo_keys_hover.png"
            xalign 0.4792
            yalign 0.38
            focus_mask True
            action [
                Play("sound2","sound effects/01/keypad_beep.ogg"),
                If(len(v_ep01_12_04_card_theft_security_code+"6") < 6,true=SetVariable("v_ep01_12_04_card_theft_security_code",v_ep01_12_04_card_theft_security_code+"6"),false=If(v_ep01_12_04_card_theft_security_code+"6" == "210224",true=Jump("lb_ep01_12_04_card_theft_success"), false=[SetVariable("v_ep01_12_04_card_theft_security_code",""),Jump("lb_ep01_12_04_card_theft_failed")]))
                ]

        imagebutton:
            idle "images/Episode 01/Day 03/12-MC Jobs/12-04 Card Theft/combo_keys_idle.png"
            hover "images/Episode 01/Day 03/12-MC Jobs/12-04 Card Theft/combo_keys_hover.png"
            xalign 0.3915
            yalign 0.46
            focus_mask True
            action [
                Play("sound2","sound effects/01/keypad_beep.ogg"),
                If(len(v_ep01_12_04_card_theft_security_code+"7") < 6,true=SetVariable("v_ep01_12_04_card_theft_security_code",v_ep01_12_04_card_theft_security_code+"7"),false=If(v_ep01_12_04_card_theft_security_code+"7" == "210224",true=Jump("lb_ep01_12_04_card_theft_success"), false=[SetVariable("v_ep01_12_04_card_theft_security_code",""),Jump("lb_ep01_12_04_card_theft_failed")]))
                ]

        imagebutton:
            idle "images/Episode 01/Day 03/12-MC Jobs/12-04 Card Theft/combo_keys_idle.png"
            hover "images/Episode 01/Day 03/12-MC Jobs/12-04 Card Theft/combo_keys_hover.png"
            xalign 0.4351
            yalign 0.46
            focus_mask True
            action [
                Play("sound2","sound effects/01/keypad_beep.ogg"),
                If(len(v_ep01_12_04_card_theft_security_code+"8") < 6,true=SetVariable("v_ep01_12_04_card_theft_security_code",v_ep01_12_04_card_theft_security_code+"8"),false=If(v_ep01_12_04_card_theft_security_code+"8" == "210224",true=Jump("lb_ep01_12_04_card_theft_success"), false=[SetVariable("v_ep01_12_04_card_theft_security_code",""),Jump("lb_ep01_12_04_card_theft_failed")]))
                ]

        imagebutton:
            idle "images/Episode 01/Day 03/12-MC Jobs/12-04 Card Theft/combo_keys_idle.png"
            hover "images/Episode 01/Day 03/12-MC Jobs/12-04 Card Theft/combo_keys_hover.png"
            xalign 0.4792
            yalign 0.46
            focus_mask True
            action [
                Play("sound2","sound effects/01/keypad_beep.ogg"),
                If(len(v_ep01_12_04_card_theft_security_code+"9") < 6,true=SetVariable("v_ep01_12_04_card_theft_security_code",v_ep01_12_04_card_theft_security_code+"9"),false=If(v_ep01_12_04_card_theft_security_code+"9" == "210224",true=Jump("lb_ep01_12_04_card_theft_success"), false=[SetVariable("v_ep01_12_04_card_theft_security_code",""),Jump("lb_ep01_12_04_card_theft_failed")]))
                ]

        imagebutton:
            idle "images/Episode 01/Day 03/12-MC Jobs/12-04 Card Theft/combo_keys_idle.png"
            hover "images/Episode 01/Day 03/12-MC Jobs/12-04 Card Theft/combo_keys_hover.png"
            xalign 0.4351
            yalign 0.539
            focus_mask True
            action [
                Play("sound2","sound effects/01/keypad_beep.ogg"),
                If(len(v_ep01_12_04_card_theft_security_code+"0") < 6,true=SetVariable("v_ep01_12_04_card_theft_security_code",v_ep01_12_04_card_theft_security_code+"0"),false=If(v_ep01_12_04_card_theft_security_code+"0" == "210224",true=Jump("lb_ep01_12_04_card_theft_success"), false=[SetVariable("v_ep01_12_04_card_theft_security_code",""),Jump("lb_ep01_12_04_card_theft_failed")]))
                ]

        if v_ep01_12_04_card_theft_code_failed >= 3:
            textbutton "BYPASS":
                text_outlines [ (absolute(6), "#000", absolute(0), absolute(0)) ]
                xalign 0.432
                yalign 0.628
                focus_mask True
                action Jump("lb_ep01_12_04_card_theft_success")

label lb_ep01_12_04_card_theft1:
    #Thief Of Hearts - Ep 1 Scene 12-04
    #The MC helps Ariel steal security cards
    #SCENE BEGINS
    #Scene begins with the MC and Ariel, in matching uniforms that are the same as the staff that work at this security place - https://pixhost.to/show/1044/447513812_000.jpg
    #They look at the security warehouse and go over the plan
    #Show Ariel and the MC’s faces for the first three lines below
    centered "A short time later...{w=2.0}{nw}" with dissolve
    show text "A short time later..." #THESE LINES ARE NOT DUPLICATES. Needed to fade the text in and out!
    scene bg black with Dissolve(1)
    pause 1.0
    play ambient "sound effects/01/street_sound_day_ambience.ogg" loop fadein 1.0
    scene sc cardtheft a001
    with dissolve
    a"Do you remember what we discussed?"
    show sc cardtheft a002
    mc"Yeah... I’m pretty sure I got it."
    show sc cardtheft a003
    a"And you're wearing the security pass I made up for you."
    #The MC holds the lanyard up that’s around his neck
    show sc cardtheft a004
    mc"Yup!"
    show sc cardtheft a005
    a"Even though this place isn’t a major business, we have to make sure not to underestimate the levels of security that they have on the premises."
    show sc cardtheft a002
    mc"Of course. I mean, they kind of specialise in that, right?"
    show sc cardtheft a007
    a"True, however, they also have a three-star rating online."
    show sc cardtheft a002
    mc"Oh, so they’re not exactly the crème de la crème of security businesses."
    show sc cardtheft a008
    a"Exactly."
    show sc cardtheft a009
    mc"All right... Are we ready to go in?"
    show sc cardtheft a003
    a"I think so. I just wish I wasn’t so nervous."
    a"I’m usually happy and content being in the van for jobs, you know?"
    show sc cardtheft a010
    mc"I get it. But you have nothing to worry about."
    mc"I’ll do all the talking, while you just focus on what you do best."
    mc"It involves looking at a screen and doing a lot of typing."
    #Ariel smiles
    show sc cardtheft a011
    a"Thanks, [y_name]."
    stop ambient fadeout 1.0
    #screen goes blank
    scene black
    with dissolve
    scene black
    with Pause (2)
    #show inside the security facility. Ariel and the MC stand side by side.
    #they have to show their security passes to the front door security - https://mypolice.qld.gov.au/mackay/files/2018/05/vnlk.jpg
    scene sc cardtheft a012
    with dissolve
    mc"There’s the guard."
    show sc cardtheft a013
    mc"Let me handle this."
    #The MC approaches the guard at the reception
    show sc cardtheft a014
    guard"Hold it."
    guard"Identifications, please."
    show sc cardtheft a015
    mc"Sure thing, Sir."
    #The MC shows his ID - https://thumbs.dreamstime.com/b/businessman-suit-wearing-blank-id-tag-name-card-lanyard-exhibition-conference-179947373.jpg
    #The guard looks closely at the ID
    show sc cardtheft a016
    guard"Okay..."
    guard"Thank you, Mister Fong."
    #The MC looks at Ariel and gives her a stupid smile
    show sc cardtheft a017
    guard"And yours, miss."
    #Ariel shows her ID as well with the MC - https://i.etsystatic.com/11848992/r/il/e5e731/935543301/il_570xN.935543301_1ugz.jpg
    #Ariel looks nervous as the guy looks closely at her ID
    show sc cardtheft a018
    guard"Hmm... Hold up one second."
    a"(Oh God, oh God!)"
    show sc cardtheft a019
    mc"Is something wrong?"
    guard"Well how about that?"
    show sc cardtheft a020
    guard"We both have the same birthday!"
    guard"You’re a Capricorn, too, huh?"
    show sc cardtheft a021
    a"Oh, yeah, that’s right!"
    a"We're here to do some repair work on some of your systems on the fifth floor."
    show sc cardtheft a022
    guard"Oh, you must be looking for the administration department."
    show sc cardtheft a023
    a"Yeah, and my understanding is I’m also meant to be given a security pass by you guys."
    show sc cardtheft a024
    guard"Oh..."
    #The guard checks his paperwork
    guard"Hmm..."
    show sc cardtheft a025
    guard"I’m not sure what to tell you, but, there’s no pass here for you, miss."
    show sc cardtheft a022
    guard"But I can call upstairs to let them know that you’re coming."
    show sc cardtheft a026
    mc"No need to do that. We’ve been here numerous times so we can find our way up there."
    mc"Besides we’d kind of like to surprise them."
    show sc cardtheft a027
    guard"Oh, you and Bill know each other?"
    show sc cardtheft a028
    mc"Oh yeah, we go way back. Good ole' William!"
    show sc cardtheft a027
    guard"Well I’m sure he’ll be thrilled to see you both."
    guard"You two have a great day."
    show sc cardtheft a026
    mc"Thanks, uh, man..."
    #show the MC and Ariel walking past the front counter with the guard in the background
    show sc cardtheft a029
    a"{i}(*Whispering*){/i}\nOh wow... My heart nearly jumped out of my chest."
    a"{i}(*Whispering*){/i}\nHow did you make up that story on the spot like that?"
    play sound ["sound effects/01/Metal_Push Door_Open.mp3"]
    play sound2 [ "<silence .5>","sound effects/01/Metal_Push Door_Open.mp3"]
    scene black
    with fast_dissolve
    play sound3 ["sound effects/01/Metal_Push Door_Close.mp3"]
    play sound4 [ "<silence .5>","sound effects/01/Metal_Push Door_Close.mp3"]
    scene sc cardtheft a030
    with fast_dissolve
    mc"You have your set of skills, I have mine."
    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    stop sound3 fadeout 1.0
    stop sound4 fadeout 1.0
    show sc cardtheft a031
    a"Fair point."
    #She smiles back at the MC
    #Show the MC and Ariel walking past several offices
    show sc cardtheft a032
    mc"So these cards are on the fifth level, yeah?"
    show sc cardtheft a033
    a"That’s right."
    a"But the room we need to get inside of requires a security clearance pass."
    a"We’re going to have to acquire one before we get up to that floor."
    #The background needs to change while they are walking
    show sc cardtheft a032
    mc"What does this pass look like?"
    show sc cardtheft a034
    a"It will probably have Level 5 written on it."
    a"I couldn’t forge or copy one because they change the scanning code every day."
    show sc cardtheft a035
    mc"What about breaking into that room?"
    show sc cardtheft a033
    a"Bad idea."
    show sc cardtheft a036
    a"They have security cameras everywhere."
    show sc cardtheft a037
    a"And the alarms will go off if we try anything other than using an approved pass."
    show sc cardtheft a038
    mc"Shit..."
    #The MC and Ariel enter the elevator and they wait - https://www.daz3d.com/elevator-hallway - https://www.daz3d.com/fh-double-elevators
    if persistent.v_anim_enabled:
        show sc cardtheft elevator open1
        play sound "sound effects/01/Elevator_Ding_Door_Open.ogg" noloop
        a"Don’t worry, you’ll think of something."
        play sound2 "sound effects/01/Metal_Push Door_Open.mp3" noloop
        $ ui.timer(1.0, Play("sound2", "sound effects/01/Metal_Push Door_Close.mp3"))
        mc"(Sometimes [a_name] has too much confidence in me.)"
    else:
        play sound "sound effects/01/Elevator_Ding_Door_Open.ogg" noloop
        show sc cardtheft a039
        a"Don’t worry, you’ll think of something."
        play sound2 "sound effects/01/Metal_Push Door_Open.mp3" noloop
        $ ui.timer(1.0, Play("sound2", "sound effects/01/Metal_Push Door_Close.mp3"))
        show sc cardtheft a039a
        mc"(Sometimes [a_name] has too much confidence in me.)"
    #A guy calls out from outside the lift. He has headphones around his neck
    play sound3 "sound effects/01/two_officers_running_effect.mp3" noloop fadein 1.0
    show sc cardtheft a040
    guy"Hold the lift, please, guys!"
    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    show sc cardtheft a041
    mc"Sure thing!"
    #The MC holds the lift and the guy enters
    #mc"(Hmm...)"
    #The MC looks closer at his badge which is clipped onto his left shirt pocket - https://cdn.nametagwizard.com/media/catalog/product/p/h/photo-id-horizontal-alt-6.jpg
    stop sound3 fadeout 1.0
    show sc cardtheft a042
    guy"Thanks for that."
    show sc cardtheft a043
    mc"No problem."
    #The guy looks at the elevator panel which is to his right - https://i.redd.it/3k589ixe6h0a1.jpg
    #The guy chooses Level 4 and the MC stands behind him to his left
    play sound "sound effects/01/Elevator_Door_Close.ogg" noloop
    show sc cardtheft a044
    guy"What level, folks?"
    show sc cardtheft a045
    a"Level five, please."
    #Guy leans forward and his pass from his top pocket enters the MC’s view
    show sc cardtheft a046
    mc"(Oh!)"
    stop sound fadeout 1.0
    play music "sound effects/01/NGGYU_elevator_music.mp3" loop fadein 2.0
    play ambient "sound effects/01/Elevator_Running_Loop2.ogg" loop fadein 1.0
    #[Steal it / Don’t do it]
    menu:
        "Steal it"(wt="Task Point"):
            mc"(Now’s my chance while he's distracted!)"
            #The MC tries to grab it but manages not to
            if persistent.v_anim_enabled:
                show sc cardtheft steal badge1
                $ renpy.pause(2.8, hard=True)
                mc"(Dammit!)"
                $ v_ep01_task07_help_ariel_counter += 1
            else:
                show sc cardtheft a047a
                pause 0.5
                show sc cardtheft a047b
                mc"(Dammit!)"
            #He straightens up, as does the guy in front of him
        "Don’t do it":
            if persistent.v_anim_enabled:
                show sc cardtheft steal badge2
            else:
                show sc cardtheft a048c
            mc"(No, it’s too risky.)"
    #scene continues
    #The guy puts his headphones on in front of them
    show sc cardtheft a049
    mc"{i}(*Whispering*){/i}\n[a_name]..."
    mc"{i}(*Whispering*){/i}\nThat guy has his headphones on, so he can’t hear us."
    mc"(He's lucky, as he doesn't have to suffer listening to this goddamned elevator music!)"
    show sc cardtheft a050
    a"{i}(*Whispering*){/i}\nSo?"
    show sc cardtheft a051
    mc"{i}(*Whispering*){/i}\nHe has a Level 5 pass on him."
    show sc cardtheft a050
    a"{i}(*Whispering*){/i}\nOh..."
    a"{i}(*Whispering*){/i}\nHow are we going to get it?"
    show sc cardtheft a049
    mc"{i}(*Whispering*){/i}\nI have an idea."
    mc"{i}(*Whispering*){/i}\nFall to the floor."
    show sc cardtheft a052
    a"{i}(*Whispering*){/i}\nWhat?"
    a"{i}(*Whispering*){/i}\nWhy?"
    show sc cardtheft a053
    mc"{i}(*Whispering*){/i}\nTo create a distraction."
    show sc cardtheft a054
    a"{i}(*Whispering*){/i}\nI... I don’t know if I can."
    #The MC looks at the panel above them and it shows the number #2
    show sc cardtheft a055
    mc"{i}(*Whispering*){/i}\nDo you want that pass or not?"
    show sc cardtheft a056
    a"{i}(*Whispering*){/i}\nI do."
    mc"{i}(*Whispering*){/i}\nThen don’t think, [a_name]."
    show sc cardtheft a057
    mc"{i}(*Whispering*){/i}\nJust close your eyes and do it."
    mc"{i}(*Whispering*){/i}\nI’ll catch you."
    show sc cardtheft a058
    a"{i}(*Whispering*){/i}\nOh geez..."
    #Ariel pretends to collapse into the MC’s arms
    show sc cardtheft a059
    with hpunch
    mc"Polly!!"
    #The MC brings her down to the floor and calls to the guy in front of him
    mc"I need some help!"
    show sc cardtheft a060
    a"(Oh my goodness [y_name], did you have to catch me like that! You're grabbing... them...)"
    #The guy turns around and takes his headphones off
    show sc cardtheft a061
    guy"Oh, what happened?"
    show sc cardtheft a062
    mc"I’m not sure. She was fine one second and the next, she fainted."
    show sc cardtheft a060
    a"(Hmm, his hands are bigger than I thought they would be, and yet so soft and warm too.)"
    show sc cardtheft a063
    guy"What should we do?"
    show sc cardtheft a064
    mc"I think she's claustrophobic. So maybe you could undo one of her buttons."
    mc"You know, to give her more air."
    show sc cardtheft a065
    a"(Wait, WHAT!)"
    show sc cardtheft a066
    guy"Do you think that’s a good idea?"
    show sc cardtheft a067
    mc"Yeah, for sure."
    mc"Quickly now!"
    show sc cardtheft a068
    a"(Oh my god, [y_name]'s really going to let him do it, what is he thinking!)"
    #While the guy places his hands over Ariel’s chest, the MC sees his badge hanging down and grabs it
    if persistent.v_anim_enabled:
        show sc cardtheft steal badge3
    else:
        show sc cardtheft a069a
    mc"(Yoink!)"
    #The MC takes it and places it in his back pocket
    show sc cardtheft a070
    mc"Actually, on second thought, I better do that."
    show sc cardtheft a071
    mc"Seeing as she’s my co-worker and responsibility."
    show sc cardtheft a072
    guy"R-right."
    show sc cardtheft a073
    a"(Thank you, thank you, thank you... But I also want to kill you [y_name]!)"
    play sound [ "<silence .5>","sound effects/01/slap1.ogg","<silence .26>"] loop
    if persistent.v_anim_enabled:
        show sc cardtheft tap cheek
    else:
        show sc cardtheft a074
    mc"Polly?"
    #her eyes open
    stop sound fadeout 1.0
    show sc cardtheft a075
    a"Oh... What happened?"
    mc"You fainted."
    show sc cardtheft a076
    mc"This gentleman and I tried to help you."
    show sc cardtheft a077
    guy"Are you okay?"
    #The MC winks at Ariel which the guy doesn’t see
    show sc cardtheft a078
    a"Y-yeah... My head’s still a little fuzzy, but overall, I’m good."
    #The door dings for the 4th floor
    stop ambient fadeout 4.0
    play sound "sound effects/01/Elevator_Ding_Door_Open.ogg" noloop
    if persistent.v_sounds_text_on == True:
        "(Ding!)"
    else:
        pause 2.0
    show sc cardtheft a079
    guy"Oh, this is my floor."
    #The door opens
    stop sound fadeout 1.0
    show sc cardtheft a080
    guy"Do you want me to call you an ambulance or for medical assistance?"
    show sc cardtheft a081
    a"No, no... I think I’ll be fine."
    a"Thank you so much for being here for me."
    show sc cardtheft a082
    guy"You’re welcome, miss."
    show sc cardtheft a083
    mc"Yeah, thanks. I’ve got it from here."
    show sc cardtheft a084
    guy"You take care now."
    play sound "sound effects/01/Elevator_Door_Close.ogg" noloop
    #The guy leaves the elevator with a confused look on his face
    if persistent.v_anim_enabled:
        show sc cardtheft elevator close1
        a"I will."
        #The elevator doors close and it starts to move again
        #Ariel looks at the MC have gives him a smack on the arm
        play ambient "sound effects/01/Elevator_Running_Loop2.ogg" loop fadein 1.0
    else:
        show sc cardtheft a085
        a"I will."
        #The elevator doors close and it starts to move again
        #Ariel looks at the MC have gives him a smack on the arm
        play ambient "sound effects/01/Elevator_Running_Loop2.ogg" loop fadein 1.0
        show sc cardtheft a085b
    a"Oh God... That was close."
    stop sound fadeout 1.0
    play sound2 "sound effects/01/punch_to_fist_effect.mp3" noloop
    show sc cardtheft a086
    with hpunch
    if persistent.v_sounds_text_on == True:
        "(THWACK!)"
    mc"OW!"
    stop sound2 fadeout 1.0
    show sc cardtheft a088
    a"Did you have to grab my chest like that, [y_name]!"
    show sc cardtheft a087
    mc"I'm sorry, you sort of fell into me at a weird angle and I couldn't get a good hold of you."
    mc"I can assure you that I didn't do it on purpose."
    show sc cardtheft a089
    a"{i}(*Mumbling*){/i}\nWell, its not like it felt {i}all{/i} bad."
    mc"Huh?"
    show sc cardtheft a090
    a"I uh... Nothing, never mind..."
    show sc cardtheft a091
    a"And another thing, what was with that \"Maybe you could undo one of her buttons\" thing?"
    a"I seriously thought you were going to let him do that."
    show sc cardtheft a092
    mc"Well, I had to keep him focused on something other than me, and what's better than a guy thinking that he'll get to see what's under your shirt?"
    show sc cardtheft a093
    a"Oh, well...{w} You just about gave me a heart attack with that."
    show sc cardtheft a094
    a"But thank you for stopping him from getting that far."
    show sc cardtheft a091
    a"I saw that you got the card at least, so now we can get into that room."
    show sc cardtheft a095
    a"But the only problem is, we only have one pass."
    a"What if someone spots us and wants to see our passes?"
    show sc cardtheft a096
    mc"Don’t worry, we’ll figure it out if that happens."
    #The elevator stops on the fifth floor
    stop ambient fadeout 4.0
    play sound "sound effects/01/Elevator_Ding_Door_Open.ogg" noloop
    if persistent.v_anim_enabled:
        show sc cardtheft elevator open2
    else:
        show sc cardtheft a097a
        pause 0.8
        show sc cardtheft a097b
    if persistent.v_sounds_text_on == True:
        "(Ding!)"
    else:
        pause 1.0
    stop music fadeout 1.0
    stop sound fadeout 1.0
    #Final shot here is the doors opening to the fifth floor
    #screen goes blank
    scene black
    with dissolve
    scene black
    with Pause (2)
    #The MC and Ariel stand outside the office where the admin room
    play music "sound effects/01/Spy Glass.mp3" loop fadein 1.0
    scene sc cardtheft a098
    with dissolve
    a"This should be it."
    show sc cardtheft a098a
    mc"Well hurry. We may not have long until that guy realises his clearance pass is gone."
    #Ariel taps the pass against the plate - https://newsroom.hidglobal.com/sites/default/files/styles/large/public/images/2023-05/pacs-eco-card-signo-40-reader-02.png?itok=dr7gK9JO
    #It changes from a red light to green
    play sound [ "<silence .5>","sound effects/01/card_swipe.ogg"]
    play sound2 [ "<silence 1.6>","sound effects/01/door_buzz.mp3"]
    play sound3 [ "<silence 1.6>","sound effects/01/door_bolt_unlocking.mp3"]
    if persistent.v_anim_enabled:
        show sc cardtheft slide card
        $ renpy.pause(3.0, hard=True)
    else:
        show sc cardtheft a099
        pause 0.8
        show sc cardtheft a099a
        pause 3.0
    #the door unlocks and they open it
    show sc cardtheft a100
    a"All right. we’re in."
    #The MC follows her inside and the office full of computers and desks is unoccupied - https://www.regus.com/work-us/wp-content/uploads/sites/18/2016/12/Ys8jH2JZSn2sgxvWiF9j-6.jpg
    #NOTE: There are blinds along the glass window that looks out to the hallway that the MC looks through - https://i0.wp.com/www.enviroscreen.org.uk/wp-content/uploads/2018/02/enviroscreen-office-blinds-london.jpg?fit=787%2C402&ssl=1
    #IMPORTANT: Make sure there is a recycling garbage shoot in the corner of this room as this will be an escape route for the MC and Ariel later on
    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    stop sound3 fadeout 1.0
    if persistent.v_anim_enabled:
        show sc cardtheft turn on lights
    else:
        show sc cardtheft a101
        pause 0.8
        show sc cardtheft a101a
    mc"So what are we looking for?"
    a"First we need to locate where they keep the security cards specifically for the art gallery."
    show sc cardtheft a102
    a"I’ll see if I can find what we need on this computer while you keep watch."
    #The MC looks outside the office through the blinds
    #mc"(All signs are clear.)"
    #mc"(It’s probably just as well this is only a small business.)"
    #Show Ariel looking at the screen
    show sc cardtheft a103
    mc"Sure, I can do that."
    a"Hmm..."
    a"(The cards are kept in a safety deposit box in the next room.)"
    show sc cardtheft a103a
    a"(The unlock code is 210224.)"
    a"(I better write this down or commit it to memory.)"
    #She writes down the calls out to the MC
    show sc cardtheft a104
    a"[y_name]! I’ve got it!"
    #The MC looks outside the glass window through the blinds - https://i0.wp.com/www.enviroscreen.org.uk/wp-content/uploads/2018/02/enviroscreen-office-blinds-london.jpg?fit=787%2C402&ssl=1
    show sc cardtheft a105
    mc"Oh shit!!"
    show sc cardtheft a106
    mc"Someone’s coming this way!"
    show sc cardtheft a107
    a"What are we going to do??"
    show sc cardtheft a108
    mc"I’m going to hide."
    mc"Just act natural and pretend that you work here."
    show sc cardtheft a109
    a"But where are you going to-"
    #The MC hides underneath the desk Ariel is sitting at
    show sc cardtheft a110
    a"(OH!!)"
    menu:
        "Hide facing toward outside":
            $ v_ep01_12_04_card_theft_desk_choice = "outside"
        "Hide facing toward inside"(wt="Task Point"):
            $ v_ep01_12_04_card_theft_desk_choice = "inside"
    #The staff member opens the door and enters
    show sc cardtheft a111
    a"(Oh, I better hide this badge and then make it look like I’m working on something.)"
    #ys opens up a new tab and whispers to the MC
    show sc cardtheft a112
    a"{i}(*Whispering*){/i}\nHe’s right outside!!"
    #Ariel sees a male worker inside the office
    a"{i}(*Whispering*){/i}\nWhat do I do?"
    play sound2 [ "<silence 1.2>","sound effects/01/door_buzz.mp3"]
    play sound3 [ "<silence 1.2>","sound effects/01/door_bolt_unlocking.mp3"]
    show sc cardtheft a113
    mc"{i}(*Whispering*){/i}\nJust relax and pretend like you’re at your job at the computer shop."
    #The guy stands in front of her desk
    stop sound2 fadeout 1.0
    stop sound3 fadeout 1.0
    show sc cardtheft a114
    staff"Hey..."
    #The MC curls in a ball and looks down. He tries to keep perfectly still
    show sc cardtheft a115
    a"Hi there."
    show sc cardtheft a116
    staff"Hmm... I didn't expect to see anybody in here this afternoon."
    staff"What are you doing exactly?"
    show sc cardtheft a117
    a"I um... I’m working, of course."
    #Ariel shows him her Level 5 pass
    show sc cardtheft a118
    a"See?"
    staff"Oh, right..."
    if v_ep01_12_04_card_theft_desk_choice == "inside":
        show sc cardtheft a119
        staff"Who are you exactly? I’ve never seen you here before."
        $ v_ep01_task07_help_ariel_counter += 1
        show sc cardtheft a115
        a"Oh, I’m... Kim."
        show sc cardtheft a203
        with hpunch
        pause 0.2
        mc"(SHIT!)"
        mc"(Right on the Chuck Dickens!)"
        show sc cardtheft a115
        a"I’m friends with Bill."
        a"Bill... Clay?"
        show sc cardtheft a116
        staff"Oh, right."
        show sc cardtheft mc footsie1
        mc"(Oh good lord, she must be so nervous that she forgot I was here...)"
        if v_ep01_work_visit_options_1 == "[a_name]" or v_ep01_work_visit_options_2 == "[a_name]":
            mc"(Why do I keep finding myself in situations where [a_name] is crushing my dick.)"
        show sc cardtheft a117
        a"He’s off sick today so he asked me if I could cover for him."
        show sc cardtheft a120
        staff"Really?"
        staff"I could have sworn that I saw him just this morning."
        show sc cardtheft a204
        mc"(Shit! Why of all times am I getting hard from this? I hope she can't feel that.)"
        show sc cardtheft a115
        a"Right, well, he- he-"
        show sc cardtheft a207
        a"(Wait...)"
        show sc cardtheft mc footsie2
        a"(What the hell is my foot pressing on?)"
        mc"(Jesus [a_name], please stop!)"
        show sc cardtheft a115
        a"I'm sorry... He had to go home so I’m doing the rest of his shift."
        show sc cardtheft mc footsie3
        a"(What is this? It initially felt like a soft footrest, but now it's really hard.)"
        mc"(Oh good lord, what are you doing [a_name]!? If you don't stop, I'm going to...)"
        $ rewards_unlock ("ariel",3)
        show sc cardtheft a121
        staff"I hope he’s alright."
        show sc cardtheft a121
        a"Me too... Gastroenteritis is no laughing matter."
        show sc cardtheft a122
        staff"That bad, huh?"
        show sc cardtheft a115
        a"Yeah, that’s what he told-"
        play sound "sound effects/01/desk_bang.mp3"
        show sc cardtheft a205
        with vpunch
        if persistent.v_sounds_text_on == True:
            "{i}*BANG!*{/i}"
        else:
            pause 1.0
        mc"(FUCK ME!)"
        show sc cardtheft a120
        staff"Oh... That sounded like you hit your knee really hard. Are you okay?"
        show sc cardtheft a206
        a"I uh, yeah, I just bumped it, I'll be fine, thanks."
        show sc cardtheft a207
        a"(What the hell was that [y_name]! You nearly gave us away.)"
        show sc cardtheft a208
        mc"(STUPID! STUPID! STUPID!)"
        mc"(She can't ever find out what just happened. I'm just glad I wore some thicker underwear today so it doesn't show.)"
        mc"(I better get her to wrap up this chat before something else happens.)"
        #The MC taps Ariel on the leg
        if persistent.v_anim_enabled:
            show sc cardtheft tap leg2
        else:
            show sc cardtheft a128a
    else:
        show sc cardtheft a119a
        staff"Who are you exactly? I’ve never seen you here before."
        show sc cardtheft a115
        a"Oh, I’m... Kim."
        a"I’m friends with Bill."
        a"Bill... Clay?"
        show sc cardtheft a116
        staff"Oh, right."
        show sc cardtheft a117
        a"He’s off sick today so he asked me if I could cover him."
        show sc cardtheft a120
        staff"Really?"
        staff"I could have sworn that I saw him just this morning."
        show sc cardtheft a115
        a"Right, well, he had to go home so I’m covering the afternoon shift."
        show sc cardtheft a116
        staff"I hope he’s alright."
        show sc cardtheft a121
        a"Me too... Gastroenteritis is no laughing matter."
        show sc cardtheft a122
        staff"That bad, huh?"
        show sc cardtheft a115
        a"Yeah, that’s what he told me."
        show sc cardtheft a127
        mc"(I better get her to wrap up this chat.)"
        #The MC taps Ariel on the leg
        if persistent.v_anim_enabled:
            show sc cardtheft tap leg1
        else:
            show sc cardtheft a128a
    a"Um, anyway, it was nice talking with you, but I have a heap of work to catch up on."
    show sc cardtheft a129
    staff"Yes, of course. "
    #The guy turns and then turns back
    show sc cardtheft a130
    $ renpy.pause(1.0, hard=True)
    staff"Say..."
    show sc cardtheft a131
    staff"If you’re free in about an hour, would you maybe want to get some coffee across the street?"
    show sc cardtheft a132
    a"Oh... Well, I um..."
    #Ariel looks nervous
    show sc cardtheft a133
    staff"Oh, I’m sorry. You have a boyfriend or something, right?"
    show sc cardtheft a134
    a"Y-yeah... His name is um..."
    #Ariel looks down at the MC
    show sc cardtheft a135
    a"[y_name]."
    if v_ep01_12_04_card_theft_desk_choice == "inside":
        show sc cardtheft a136a
    else:
        show sc cardtheft a136
    mc"(???)"
    show sc cardtheft a137
    staff"Well, if you don’t mind me saying, he’s a very lucky man."
    #Ariel blushes
    show sc cardtheft a138
    a"Thanks."
    show sc cardtheft a133
    staff"Have a great day, Kim."
    #The staff member leaves
    mc"Is he gone?"
    show sc cardtheft a134
    a"Yeah, for now."
    #The MC comes out from under the table
    show sc cardtheft a139
    mc"Why did you say my name when he asked if you had a boyfriend?"
    show sc cardtheft a140
    a"I’m sorry... I panicked and your name was the first one I could think of."
    show sc cardtheft a141
    mc"Don’t worry about it."
    mc"It seems like you’re already getting better at improvising."
    show sc cardtheft a142
    a"Haha, hardly..."
    if v_ep01_12_04_card_theft_desk_choice == "inside":
        show sc cardtheft a143
        a"Oh, and what was that noise you made? You nearly got us caught."
        show sc cardtheft a144
        mc"Oh, I uh... I'd rather not talk about it. I'm just glad he didn't realize I was under there."
    mc"By the way... Who the hell is Bill Clay?"
    show sc cardtheft a143
    a"I did an initial check on all the staff that are employed here and he's the one I remembered after the guard downstairs mentioned his first name."
    show sc cardtheft a144
    mc"That was lucky."
    mc"All right, let’s get those cards in the safety deposit box and then we can get the hell out of here!!"
    stop music fadeout 1.0
    #screen goes blank
    scene black
    with dissolve
    scene black
    with Pause (2)
    #The MC and Ariel are in the safety deposit box room - https://www.kss.com.au/CMSPages/GetAmazonFile.aspx?path=~%5Ckssmvc%5Cmedia%5Cbody-content-images%5Cdeposit-box-02.jpg&hash=4e2cbbdfdfb3fce8865b5a2d9d5225187bba8f3a137dffd1bfceb7810535f8c4
    show sc cardtheft a145
    with dissolve
    mc"Have you found it?"
    show sc cardtheft a146
    a"Yeah, it’s this one for the art gallery."
    a"But I need to put the code in."
    play music "sound effects/01/Stealth in the Shadows1.mp3" loop fadein 1.0
    a"(What was it again?)"
    #MINI-GAME here - To open the deposit box, the player needs to punch in the correct code to
    #proceed to the next part of the scene. The code was mentioned in the last scene - 210224
    #If they put the wrong code in, then they can’t proceed
    #A keypad comes up on the screen here - https://user-images.githubusercontent.com/6978717/55760430-ed605200-5a10-11e9-8490-9455668cbe3a.png

    #"If the player punches in the wrong code, then a negative beeping sound denying them access will sound"
    scene sc cardtheft a147
    call screen scr_ep01_12_04_Vault_Combo

label lb_ep01_12_04_card_theft_failed:
    #"(Negative beeping sound)"
    play sound "sound effects/01/keypad_negative.ogg"
    a"That’s not it."
    $ v_ep01_12_04_card_theft_code_failed += 1
    call screen scr_ep01_12_04_Vault_Combo
    #The player will get to try again until it’s correct


label lb_ep01_12_04_card_theft_success:
    #"If the player punches in the correct code, then a positive beeping sound denying them access will sound"
    #"(Positive beeping sound)"
    play sound "sound effects/01/keypad_posative.ogg"
    play sound2 [ "<silence 0.5>","sound effects/01/door_bolt_unlocking.mp3"]
    a"That’s it!"
    #The box opens and the set of security cards is in there
    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    show sc cardtheft a148
    with faster_dissolve
    a"I think that's what we're looking for."
    # Only add to the task counter if they unlocked the safe in one try
    if v_ep01_12_04_card_theft_code_failed == 0:
        $ v_ep01_task07_help_ariel_counter += 1
    show sc cardtheft a149
    mc"Sweet!"
    show sc cardtheft a150
    mc"Finally everything is falling into place for once."
    if persistent.v_anim_enabled:
        show sc cardtheft alarm1
    else:
        show sc cardtheft a150a
    pause 0.1
    stop music fadeout 1.0
    play ambient "sound effects/01/security_alarm.ogg" loop
    pause 1.0
    #The MC and Ariel have a look of horror when a security alarm sounds - https://www.youtube.com/watch?v=xz0HvEVCziY&ab_channel=SCP%3ACBsound (with voice-over)
    if persistent.v_anim_enabled:
        show sc cardtheft alarm2
    else:
        show sc cardtheft a151a
    with faster_dissolve
    mc"(Me and my big mouth...)"
    #mc"What the hell is that?"
    a"Oh no..."
    a"That must be their security breach alarm."
    announcer"{i}This is an emergency lockdown. Unauthorised members in the building.{/i}"
    if persistent.v_anim_enabled:
        show sc cardtheft alarm3
    else:
        show sc cardtheft a152a
    mc"Shit, we’ve been made."
    if persistent.v_anim_enabled:
        show sc cardtheft alarm4
    else:
        show sc cardtheft a153a
    a"I knew this would happen. My luck has run out."
    if persistent.v_anim_enabled:
        show sc cardtheft alarm6
    else:
        show sc cardtheft a155a
    a"I should've dyed my hair."
    if persistent.v_anim_enabled:
        show sc cardtheft alarm7
    else:
        show sc cardtheft a156a
    mc"What do you mean?"
    if persistent.v_anim_enabled:
        show sc cardtheft alarm4
    else:
        show sc cardtheft a153a
    a"Isn't it obvious?"
    a"Red hair is a sign of bad luck or a jinx. Dating as far back as Judas."
    if persistent.v_anim_enabled:
        show sc cardtheft alarm6
    else:
        show sc cardtheft a155a
    a"And remember the bad luck you had during the last heist? I was the one feeding you the information."
    if persistent.v_anim_enabled:
        show sc cardtheft alarm7
    else:
        show sc cardtheft a156a
    mc"That wasn't your fault. That was all on me."
    mc"The redhead thing is just a silly superstition, [a_name]."
    if persistent.v_anim_enabled:
        show sc cardtheft alarm4
    else:
        show sc cardtheft a153a
    a"Oh yeah? Well if you can figure a way out of here without us getting caught, I might just believe you."
    if persistent.v_anim_enabled:
        show sc cardtheft alarm5
    else:
        show sc cardtheft a154a
    mc"All right, follow me..."
    stop ambient fadeout 2.0
    #screen goes blank
    scene black
    with dissolve
    scene black
    with Pause (2)
    #The MC and Ariel are back in the office they were in before
    #The MC looks through the blinds again
    play music "sound effects/01/Stealth in the Shadows2.mp3" loop fadein 1.0
    scene sc cardtheft a157
    with dissolve
    mc"Hmm... The exits will be covered outside this office. And there are only a few staff members that I can see from here.)"
    a"What are we going to do?"
    show sc cardtheft a158
    mc"There!"
    #The MC points to the chute
    a"What am I looking at?"
    mc"That’s how we’re getting out of here."
    show sc cardtheft a159
    a"The recycling chute?"
    a"You can’t be serious!"
    show sc cardtheft a160
    mc"Serious like a fox!"
    mc"Besides, do you have any better ideas?"
    show sc cardtheft a161
    a"No..."
    #They head over to the chute
    show sc cardtheft a162
    mc"You should be able to slide down with no problems."
    if persistent.v_anim_enabled:
        show sc cardtheft open hatch
    else:
        show sc cardtheft a163a
    mc"The cardboard and styrofoam should break your fall but it could be a bit of a tight squeeze for me."
    show sc cardtheft a164
    a"Who should go first?"
    #[ I will / [a_name] ]
    menu:
        "I will"(wt="Task Point"):
            #This option will give the player a couple of bonus images of Ariel
            show sc cardtheft a165
            mc"I’ll go first. Just to make sure it's safe. I wouldn't want you to get hurt."
            show sc cardtheft a166
            a"Oh, okay."
            show sc cardtheft a195
            mc"Can I trust you to do this after me, [mc_a_address]?"
            show sc cardtheft a194
            a"I... I guess I’m going to have to."
            show sc cardtheft a167
            mc"All right, let’s see how this goes."
            #The MC hops into the compactor
            show sc cardtheft a168
            mc"Geez... Now I know what tuna feels like in a can."
            show sc cardtheft a169
            mc"Here I go!"
            #Ariel watches him slide down the chute
            $ renpy.music.set_volume(0.3, 0.0, channel="sound3")
            play sound3 "sound effects/01/duct_impacts.ogg" loop
            show sc cardtheft a170
            mc"Super Fun, Happy Slide!!!"
            $ renpy.music.set_volume(1.0, 0.0, channel="sound3")
            if persistent.v_anim_enabled:
                show sc cardtheft tube loop1
            else:
                show sc cardtheft a171
            mc"Weeee!"
            stop sound3 fadeout 1.0
            play ambient "sound effects/01/street_sound_day_ambience.ogg" loop
            play sound ["<silence 0.4>","sound effects/01/plunger_suction.mp3"]
            if persistent.v_anim_enabled:
                show sc cardtheft tube drop mc
            else:
                show sc cardtheft a172c
            pause 0.6
            play sound2 "sound effects/01/dumpster_dive.mp3"
            show sc cardtheft a172e
            with hpunch
            mc"What a rush!"
            #Sound effect to show the MC has hit the bottom
            show sc cardtheft a173
            mc"(Woah, I nearly lost my shirt in there from the friction and static electricty!)"
            $ renpy.music.set_volume(0.0, 0.0, channel="ambient")
            show sc cardtheft a170
            a"[y_name]?!? Are you okay?"
            #he shouts from the bottom
            $ renpy.music.set_volume(1.0, 0.0, channel="ambient")
            show sc cardtheft a174
            mc"I uh, yeah! Come on down, [mc_a_address]!"
            mc"You’ll love it!"
            show sc cardtheft a175
            mc"(She should be fine, right?)"
            #Ariel begins to hop into the chute
            $ renpy.music.set_volume(0.0, 0.0, channel="ambient")
            show sc cardtheft a176c
            a"Oh, please don’t let me die..."
            show sc cardtheft a176
            a"HERE I COME!"
            if persistent.v_anim_enabled:
                show sc cardtheft mc hatch drop ariel1
            else:
                show sc cardtheft a176b
            pause 0.8
            $ renpy.music.set_volume(0.3, 0.0, channel="sound")
            play sound "sound effects/01/duct_impacts.ogg" loop
            a"Oh my God!!"
            #she smiles as she slides down
            $ renpy.music.set_volume(1.0, 0.0, channel="sound")
            if persistent.v_anim_enabled:
                show sc cardtheft tube loop2
            else:
                show sc cardtheft a177
            a"(This is such a wondeful rush!)"
            $ v_ep01_task07_help_ariel_counter += 1
            #she falls out of the chute and lands on top of the MC in the cardboard compactor - https://globaltrashsolutions.com/wp-content/uploads/2020/09/two-garbage-compactors-standing-next-to-each-other.jpg
            scene black
            pause 1.0
            stop sound3 fadeout 1.0
            $ renpy.music.set_volume(1.0, 0.0, channel="ambient")
            play sound "sound effects/01/dumpster_dive.mp3"
            a"Uhhh!!!" with vpunch
            #She raises her head
            a"Huh?"
            show sc cardtheft a178
            show img_blank at tt_eye_blink
            pause 1.0
            show sc cardtheft a178a
            with Dissolve(1.0)
            a"Oh! [y_name]! You caught me. T-Thank you."
            a"Are you okay?"
            show sc cardtheft a179
            mc"Yeah, I’m fine, but um..."
            if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
                show sc cardtheft a180a
                a"Huh?"
                scene sc cardtheft a180 at tt_12_04_Card_Thef_Look_Down
                pause
            elif True:
                show sc cardtheft a180a
                a"Huh?"
                show sc cardtheft a180b
                a"..."
            scene sc cardtheft a181
            with hpunch
            a"EEK!!"
            show sc cardtheft a182
            a"(Oh my god, he saw my, my-)"
            stop music fadeout 1.0
            $ rewards_unlock ("ariel",4)
            show sc cardtheft a183
            mc"I'm sorry, I didn't think that would happen to you."
            mc"I guess a static charge built up after I went down the shoot first."
            mc"I hope you're okay though."
            show sc cardtheft a184
            a"(It does seem like he didn't really mean for it to happen, and somehow being in his arms is sort of reassuring.)"
            #They look each other in the eyes up-close
            show sc cardtheft a185
            mc"Did I at least help to break your fall?"
            show sc cardtheft a186
            a"Yeah, just a little."

            #TWO BONUS RENDERS OF ARIEL (IN HER CURRENT STAFF MEMBER OFFICE OUTFIT) ADDED TO THE PHOTO GALLERY FOR HER PROFILE
            $ v_ep01_12_04_card_theft_mc_drop_first = True
            show sc cardtheft a187
            mc"That was fun though, right?"
            show sc cardtheft a188
            a"Uh-huh."
            show sc cardtheft a188a
            mc"Here, let me help down so you can fix that."
            show sc cardtheft a189
            a"Oh, thanks..."
            show sc cardtheft a190
            mc"Okay, we probably should-"
            #the MC helps Ariel up and allows her to exit the cardboard compactor and they stand looking at each other as if they are going to kiss
            show sc cardtheft a191
            mc"..."
            show sc cardtheft a192
            mc"Um... We probably should get out of here. Just in case someone sees us like this."
            show sc cardtheft a193
            a"Y-yeah, I guess we should..."
            stop ambient fadeout 1.0
            #screen goes blank
            scene black
            with dissolve
            scene black
            with Pause (2)
        "[a_name]":
            show sc cardtheft a165
            mc"You go first."
            mc"If I don’t make it, go straight home and get those cards to [mc_vic_address]."
            show sc cardtheft a194
            a"No! I won’t leave here without you."
            show sc cardtheft a195
            mc"We don’t have time to argue, [a_name]. Now go!"
            #Ariel begins to hop into the chute
            show sc cardtheft a196c
            a"Hey, watch the hand there, grabby!"
            show sc cardtheft a196d
            mc"Sorry, just trying to help."
            show sc cardtheft a196e
            a"(Really [y_name]... First my boobs and now my butt.)"
            a"(It's like he's doing these things on purpose.)"
            show sc cardtheft a196f
            a"(I just wish they didn't feel so good.)"
            show sc cardtheft a196
            a"Oh, please don’t let me die..."
            if persistent.v_anim_enabled:
                show sc cardtheft mc hatch drop ariel2
            else:
                show sc cardtheft a196a
            pause 0.8
            #Ariel drops down and we see her inside the compactor
            $ renpy.music.set_volume(0.3, 0.0, channel="sound")
            play sound "sound effects/01/duct_impacts.ogg" loop
            a"Oh my God!!"
            #she smiles as she slides down
            $ renpy.music.set_volume(1.0, 0.0, channel="sound")
            if persistent.v_anim_enabled:
                show sc cardtheft tube loop2
            else:
                show sc cardtheft a177
            a"(This is such a wondeful rush!)"
            #Sound effect to show Ariel has hit the bottom
            stop sound fadeout 1.0
            $ renpy.music.set_volume(0.3, 0.0, channel="sound2")
            play sound2 "sound effects/01/dumpster_dive.mp3"
            scene sc cardtheft a197
            a"Uhhh!!!"
            $ renpy.music.set_volume(1.0, 0.0, channel="sound2")
            stop sound2 fadeout 1.0
            mc"[a_name]?!? Are you okay?"
            stop music fadeout 1.0
            #she shouts from the bottom
            play music "sound effects/01/Stealth in the Shadows2.mp3" loop fadein 1.0
            play ambient "sound effects/01/street_sound_day_ambience.ogg" loop
            show sc cardtheft a198
            a"It was scary at first, but I'm okay. Come on down, [y_name]!"
            a"You’ll love it!"
            #The MC hops into the compactor
            $ renpy.music.set_volume(0.0, 0.0, channel="ambient")
            show sc cardtheft a167a
            mc"Oh geez... Now I know what tuna feels like in a can."
            show sc cardtheft a199
            mc"HERE I GO!"
            #He slides down the chute and we see him inside there smiling
            $ renpy.music.set_volume(0.3, 0.0, channel="sound3")
            $ ui.timer(0.5, Play("sound3", "sound effects/01/duct_impacts.ogg", loop=True))
            show sc cardtheft a176b
            mc"Super Fun, Happy Slide!!!"
            $ renpy.music.set_volume(1.0, 0.0, channel="sound3")
            if persistent.v_anim_enabled:
                show sc cardtheft tube loop1
            else:
                show sc cardtheft a171
            mc"Weeee!"
            stop sound3 fadeout 1.0
            $ renpy.music.set_volume(1.0, 0.0, channel="ambient")
            play sound ["<silence 0.4>","sound effects/01/plunger_suction.mp3"]
            if persistent.v_anim_enabled:
                show sc cardtheft tube drop mc
            else:
                show sc cardtheft a172c
            pause 0.6
            play sound2 "sound effects/01/dumpster_dive.mp3"
            show sc cardtheft a172e
            with hpunch
            stop sound fadeout 1.0
            stop sound2 fadeout 1.0
            mc"Woah! What a rush!"
            #Sound effect to show the MC has hit the bottom
            show sc cardtheft a200
            a"Are you okay?"
            show sc cardtheft a201
            mc"Yeah, I’m fine."
            mc"That was fun, huh?"
            show sc cardtheft a190
            a"A bit terrifying having to go first but it wasn't as bad as I expected."
            show sc cardtheft a202
            mc"We probably should get out of here. Just in case someone sees us like this."
            show sc cardtheft a202a
            a"Yeah, I guess we should..."
            stop ambient fadeout 1.0
            #screen goes blank
            scene black
            with dissolve
            scene black
            with Pause (2)
    #show the MC and Ariel walking side by side on the sidewalk
    play music "sound effects/01/Walking on Sunshine2.mp3" loop fadein 1.0
    play ambient "sound effects/01/suburb_neighborhood_ambience.ogg" loop fadein 1.0
    show sc cardtheft a209
    with dissolve
    mc"That worked out well, didn’t it?"
    show sc cardtheft a210
    a"Yeah, my heart is beating like crazy."
    a"I just wish I didn’t feel so anxious whenever I’m put in those situations."
    show sc cardtheft a212
    a"How do you cope with it?"
    show sc cardtheft a211
    mc"I don’t know, to be honest."
    mc"I get this adrenaline rush and I’ve grown accustomed to enjoying the thrill of being caught."
    show sc cardtheft a212
    a"I wish I felt the same. But at least we got the cards."
    show sc cardtheft a213
    mc"Which is the main thing to celebrate."
    #She smiles as they reach a street corner near home
    if v_ep01_mc_task_visit_options_3 == "":
        #"Add these lines if the player hasn’t helped Vivian and/or Bella do their tasks yet"
        show sc cardtheft a214
        mc"Um... I’m going to head into town as there’s an errand I need to run."
        mc"Will you be okay to walk home by yourself?"
        show sc cardtheft a215
        a"Sure. It’s only a few blocks from here."
        show sc cardtheft a214
        mc"All right, I’ll see you back at home."
    show sc cardtheft a216
    a"Thanks again for coming with me today."
    $ v_ep01_task07_help_ariel_counter += 1
    a"Maybe one day I’ll be able to do a job like this by myself, once I’m as confident as you are."
    show sc cardtheft a217
    mc"You took a huge step today."
    mc"Don’t worry, you’ll get there."
    if v_ep01_12_04_card_theft_mc_drop_first:
        #She kisses him on the cheek
        play sound "sound effects/01/mwah_short_kissing_sound_effect3.mp3"
        show sc cardtheft a218
        a"Mwah!"
        stop sound fadeout 1.0
        show sc cardtheft a219
        mc"(Hmm... That was unexpected.)"
        mc"(But I’ll always take a compliment of the kissing kind!)"
    if v_ep01_mc_task_visit_options_3 == "":
        #Ariel walks away from him and the MC watches her
        show sc cardtheft a220
        a"Bye, [y_name]."
        if v_ep01_task07_help_ariel_counter == 5:
            $ task_completed(7,"aa")
            $ v_ep01_ariel_aa_tasks_counter += 1
        if v_ep01_task07_help_ariel_counter == 4:
            $ task_completed(7,"a")
        if v_ep01_task07_help_ariel_counter == 3:
            $ task_completed(7,"b")
        if v_ep01_task07_help_ariel_counter == 2:
            $ task_completed(7,"c")
        if v_ep01_task07_help_ariel_counter <= 1:
            $ task_completed(7,"d")
        if v_ep01_12_04_card_theft_desk_choice == "inside":
            show sc cardtheft a219
            mc"(All right, I'd better change and clean up my {i}accident{/i} from earlier before I go anywhere else.)"
            show sc cardtheft a221
            mc"(It's really starting to itch.)"
        #screen goes blank
        stop music fadeout 1.0
        stop ambient fadeout 1.0
        scene black
        with dissolve
        scene black
        with Pause (2)
        if v_ep01_mc_task_visit_options_2 == "":
            jump lb_ep01_The_MC_meets_Zora
        else:
            jump lb_ep01_MC_gets_a_call_from_Megan1
    else:
        show sc cardtheft a222
        a"We’re only a few blocks from home."
        if v_ep01_task07_help_ariel_counter == 5:
            $ task_completed(7,"aa")
            $ v_ep01_ariel_aa_tasks_counter += 1
        if v_ep01_task07_help_ariel_counter == 4:
            $ task_completed(7,"a")
        if v_ep01_task07_help_ariel_counter == 3:
            $ task_completed(7,"b")
        if v_ep01_task07_help_ariel_counter == 2:
            $ task_completed(7,"c")
        if v_ep01_task07_help_ariel_counter <= 1:
            $ task_completed(7,"d")
        #final shot here of the MC and Ariel walking side by side on the sidewalk in the suburbs heading home
        mc"And just in time for dinner!"
        #screen goes blank
        stop ambient fadeout 1.0
        stop music fadeout 1.0
        scene black
        with dissolve
        scene black
        with Pause (2)
        jump lb_ep01_The_MC_sees_Vivian_in_the_bathroom
    #END SCENE
    #NEXT SCENE: ToH’s ep01 Scene 12-05 - The MC gates a phone call from Megan

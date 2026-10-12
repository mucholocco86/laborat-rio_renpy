init:
    $ v_ep01_03_03_Outside_Ariels_Room = False

label lb_ep01_Ariel_Room_1:
    #Ariel's Room (Younger Sister)"
    scene sc arielsroom a02
    mc"(At least I know I can have a nice, normal discussion with [a_name].)"
    show sc arielsroom a03
    mc"(Whether she's still awake is another thing.)"
    play sound "sound effects/01/Door_Knock_Sound_Effect_Free.mp3"
    show sc arielsroom a01
    with dissolve
    if persistent.v_sounds_text_on == True:
        "(Knock, knock, knock)"
    else:
        pause 2.0
    show sc arielsroom a04
    with dissolve
    stop sound fadeout 1.0
    mc"(Hmm...)"
    mc"(She's not answering.)"
    #He tries to open it, but it's locked"
    mc"(And it's locked.)"
    show sc arielsroom a03
    mc"(Perhaps she decided to have an early night and is asleep already.)"
    show sc arielsroom a02
    mc"(However...)"
    #the MC puts his ear to her door"
    show sc arielsroom a05
    mc"(I can hear her talking to someone in there.)"
    #"[Leave her be / Investigate]

    menu:
        "Leave her be":
            show sc arielsroom a04
            mc"(If her door is locked, then she obviously doesn't want to be disturbed.)"
            show sc arielsroom a03
            mc"(I'll try talking to her some other time...)"
            #screen goes blank"
            scene black
            with dissolve
            scene black
            with Pause (2)
            jump lb_ep01_girls_rooms_01

            #the MC stands back in the hallway again, looking at the three bedroom doors"

            #NOTE: The player can choose either the older sister's door or the mom's door, presuming the MC hasn't chosen either of them previously"

        "Investigate"(wt="Best option"):
            show sc arielsroom a05
            mc"(She has me intrigued. Who could she be talking to?)"
            show sc arielsroom a02
            mc"([mc_vic_address] will be furious if he catches her chatting online, especially after what I overheard in his discussion with [mc_v_address].)"
            show sc arielsroom a03
            mc"(I'll have to go outside to see what [a_name] is up to...)"
    #screen goes blank"
    scene black
    with dissolve
    scene black
    with Pause (2)

    #In this next scene, we see the MC up in a tree outside Ariel's window, watching from outside her window so she can't see him"
    play music "sound effects/01/Through the window.mp3" loop fadein 1.0
    play ambient "sound effects/01/Night_Time_Sound_FX.ogg" loop fadein 1.0
    show sc arielsroom a06
    mc"(I'm lucky [mc_vic_address] didn't see or hear me sneak out.)"
    show sc arielsroom a07
    mc"(Anyway, I better make this quick.)"
    #the MC looks inside Ariel's window and sees that she's working on the computer creating a video game"
    #she lays on her bed in front of the laptop, in a singlet and her underwear, and with glasses on"
    show sc arielsroom a08
    mc"(Wait a second... Is that an online game that she's working on?"
    mc"(It certainly looks like it.)"
    mc"(This is awesome!)"
    #He can see a render of a couple on her screen. This shows the player that Ariel is an adult game developer during the evenings.
    show sc arielsroom a09
    mc"(I never expected this from [a_name], though she definitely is blessed with the talent to be able to create her own game.)"
    mc"(Not everybody is.)"
    show sc arielsroom a16
    mc"(However, there's been a few times she's quickly closed her laptop whenever I've tried to talk to her recently.)"
    #the MC gives a quizzical look for the line below"
    show sc arielsroom a19
    mc"(I wonder why.)"
    show sc arielsroom a22
    mc"(She must have been secretly working on this game for weeks.)"
    mc"(Though it still doesn't explain who she was talking to before.)"
    show sc arielsroom a17
    mc"(Maybe she was just talking to herself.)"
    #As the MC is about to leave, Ariel's monitor shows a picture of a guy with a huge dick which surprises the MC"
    #screen shakes"
    show sc arielsroom a18
    mc"(What the hell??)"
    show sc arielsroom a23
    mc"(Oh my God... It's not just any online game that she's creating.)"
    mc"(It's an adult online game!!)"
    mc"(Who would make such a game?)"
    show sc arielsroom a10
    a"(I should probably put my glasses on.)"
    show sc arielsroom a09
    a"(But first.)"
    show sc arielsroom a17
    mc"(You are a kinky little devil, [mc_a_address].)" # We always call them by name - wanted to change that a little bit XD
    $ rewards_unlock ("ariel",1)
    #IMPORTANT (DOTS): There is some sort of reward here for the player if he visits Ariel's room before Bella.
    #The cat would still be locked in Bella's room, so this will make the MC stay for a bit longer without Ariel knowing he's there so the cat can't be spooked"

    if v_ep01_01_bella_room == True:
        #"These lines and scene if the player chose BELLA's ROOM before ARIEL's ROOM (OS)"
        #show the MC seeing the cat in the tree as he tries to leave and the cat screams"
        #screen shakes"
        play sound "sound effects/01/cat_screaming.ogg"
        show sc arielsroom a25
        with hpunch
        "EEEEEEAAAAAAAAAAAAAAARRRRRRRRRRRRRREIR!!!"
        stop sound fadeout 1.0
        show sc arielsroom a24
        mc"(Holy fuck!!!)"
        #Ariel's eyes open and looks away from her screen"
        $ renpy.music.set_volume(0.0, 0.2, channel="ambient")
        show sc arielsroom a10
        a"(What was that??)"
        a"(It sounded like it came from outside.)"
        $ renpy.music.set_volume(1.0, 0.2, channel="ambient")
        show sc arielsroom a18
        mc"(Shit! I better hide!!)"
        #the MC hides behind one of the branches or parts of the tree
        #Ariel goes to the window and looks outside"
        show sc arielsroom a28
        a"(Hmm... Strange.)"
        show sc arielsroom a26
        mc"(Fuck! I hope she doesn't see me.)"
        $ renpy.music.set_volume(0.0, 0.2, channel="ambient")
        show sc arielsroom a27
        a"(I better close my blinds, just in case there's a peeping tom hiding outside my window.)"
        #Ariel closes her blinds"
        $ renpy.music.set_volume(1.0, 0.2, channel="ambient")
        show sc arielsroom a29
        mc"(Oh man... That was close.)"
        #the cat eyeballs the MC and hisses"
        play sound "sound effects/01/cat_hiss.ogg"
        show sc arielsroom a34
        if persistent.v_sounds_text_on == True:
            "Hisssssssss!"
        else:
            pause 1.4
        stop sound fadeout 1.0
        show sc arielsroom a31
        if v_ep01_01_bella_room and v_ep01_03_02_Turned_TV_Off:
            mc"(You again! What the hell's wrong with you?!)"
        else:
            mc"(Well fuck you too!)"
        #the cat scurries off down the tree"
        show sc arielsroom a30
        mc"(I better wait a few minutes before trying to get down from here, and to allow me to calm my nerves.)"
        show sc arielsroom a31
        mc"(That damm cat...)"
        stop music fadeout 1.0
        stop ambient fadeout 1.0
        #screen goes blank"
        scene black
        with dissolve
        scene black
        with Pause (2)
        jump lb_ep01_girls_rooms_01
    else:
        #"These lines and scene if the player chose ARIEL's ROOM before BELLA's ROOM"
        #Ariel closes her eyes and grabs one of her nipples through her top"
        show sc arielsroom a18
        mc"(Oh!)"
        $ renpy.music.set_volume(0.0, 0.2, channel="ambient")
        play sex1 "sound effects/01/sex/female_moaning01.mp3"
        show sc arielsroom a11
        a"Mmm..."
        show sc arielsroom a12
        mc"(She's really getting off on this.)"
        stop sex1 fadeout 1.0
        show sc arielsroom a13
        mc"(Maybe she's not as repressed as I thought she was.)"
        show sc arielsroom a14
        mc"(Interesting.)"
        show sc arielsroom a15
        mc"(Hmm... I should head back inside.)"
        $ renpy.music.set_volume(1.0, 0.2, channel="ambient")
        show sc arielsroom a17
        mc"(But I am so glad that I came out here to see what she was doing and hiding from everyone.)"
        show sc arielsroom a19
        mc"(Perhaps I could use this new info to my advantage some other time...)"
        $ v_ep01_03_03_Outside_Ariels_Room = True
        stop ambient fadeout 1.0
        stop music fadeout 1.0
        #screen goes blank"
        scene black
        with dissolve
        scene black
        with Pause (2)
        jump lb_ep01_girls_rooms_01

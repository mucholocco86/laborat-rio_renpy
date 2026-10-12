init:
    $ v_ep01_ariel_respect_counter = 0
    $ v_ep01_ariel_cocky_counter = 0
    $ v_ep01_ariel_arrogant_counter = 0

label lb_ep01_The_MC_talks_with_Ariel1:
    #The MC heads downstairs and finds Ariel in front of her computer in the main room

    #The desk is set up in the corner and she stares at the screen with her back to the MC before he enters the room
    play music "sound effects/01/Imaginary_Heroes.mp3" loop fadein 1.0
    scene sc arieltalk a01
    with dissolve
    mc"(There she is, working hard as usual.)"

    #[Call out to her / Sneak up on her]
    menu:
        "Call out to her"(wt="Best option"):
            show sc arieltalk a02
            mc"Hey [a_name]."
            $ v_ep01_ariel_respect_counter += 1
            #She turns and panics when she sees the MC
            show sc arieltalk a11a
            a"[y_name]..."
            a"Hey!"
            show sc arieltalk a10a
            a"Give me a moment here."
            #She quickly closes the window tab on her screen and hides what she was working on
            show sc arieltalk a10
            mc"Um... Hey."
            show sc arieltalk a20
            mc"(Is she hiding something from me?)"

        "Sneak up on her":
            #The MC sneaks up on her
            show sc arieltalk a03
            mc"(She didn't hear me come in.)"
            show sc arieltalk a07
            mc"(I'll try and surprise her.)"
            #The MC sneaks up on Ariel from behind and then sees what she's working on
            show sc arieltalk a02
            mc"(Huh?)"
            #Ariel is working on her own gaming character - an insight into what Ariel would look like if she were a superhero with glasses
            show sc arieltalk a06
            mc"(Is that [a_name] as a superhero?)"
            show sc arieltalk a08
            mc"What's all this about?"
            $ v_ep01_ariel_cocky_counter += 1
            #Ariel turns around
            show sc arieltalk a11a
            a"[y_name]..."
            a"Hey!"
            show sc arieltalk a10a
            a"Give me a moment here."
            #She quickly turns back and closes the window tab on her screen and hides what she was working on
            show sc arieltalk a10
            mc"Was that meant to be you in the costumes?"
            show sc arieltalk a22
            a"No, it's just... Something silly I've been working on. It's nothing."
            show sc arieltalk a08
            mc"That was more than nothing."
            mc"It was pretty awesome from what I managed to see."
            show sc arieltalk a21
            a"Thanks..."
            show sc arieltalk a18
            a"But please don't tell anyone about this."
            a"It's not finished yet."
            show sc arieltalk a08
            mc"All right, I won't say anything."
            mc"But when you do finish whatever it is you're working on, promise that you'll show it to me, okay?"
            show sc arieltalk a17
            a"Sure."
            show sc arieltalk a16
            mc"And don't be embarrassed."
            show sc arieltalk a08
            mc"Most people don't even know how to create a render or write a simple scene script, let alone create what you have."
            #Ariel shyly smiles

            #BONUS RENDERS OF ARIEL (TWO NEW IMAGES OF HER IN A SUPERHERO COSTUME) ADDED TO THE PHOTO GALLERY FOR HER

            #scene continues
    show sc arieltalk a04
    mc"So um..."
    show sc arieltalk a09
    mc"I saw [b_name] and she gave me a replacement phone."
    show sc arieltalk a12
    mc"Any luck finding my old one?"
    show sc arieltalk a13
    a"Bad news, I'm afraid."
    show sc arieltalk a18a
    a"I managed to track it's location, but I don't think you'll want to fish it out of a landfill outside of town."
    show sc arieltalk a15
    mc"Oh, really?"
    show sc arieltalk a14
    a"Yeah, but the good news is, the girls never managed to unlock it which is probably why they disposed of it."
    show sc arieltalk a17
    a"And I can transfer all contacts and apps to your new phone."
    #She takes the phone from him
    show sc arieltalk a16
    mc"Thanks, [a_name]."
    show sc arieltalk a09
    mc"Here it is."
    show sc arieltalk a23
    a"Nice phone cover."
    # or  a"Nice case."
    show sc arieltalk a25
    a"It's cute."
    play sound "sound effects/01/Girl_Giggle.mp3"
    a"Haha!"
    show sc arieltalk a27
    mc"It's only temporary."
    stop sound fadeout 1.0
    show sc arieltalk a29
    a"Here you go."
    show sc arieltalk a30
    mc"Cool."
    show sc arieltalk a32
    a"I also have some new IDs for you."
    #She hands him a collection of ID cards and the MC goes through them
    show sc arieltalk a34
    with dissolve
    a"Here."
    #He reads them out
    show sc arieltalk a35
    mc"Sweet!"
    mc"Let me see here."
    show sc arieltalk a37
    mc"Jacques Strappe."
    #He changes to another card
    show sc arieltalk a41
    mc"Hmm..."
    show sc arieltalk a38
    mc"Sir Vey Lantz."
    #He changes to another card
    show sc arieltalk a41
    mc"What about this one?"
    show sc arieltalk a39
    with vpunch
    mc"Homer J. Fong?"
    #The MC looks surprised
    show sc arieltalk a40
    mc"What would I need this one for?"
    show sc arieltalk a42
    a"Sorry, I don't know how that happened."
    show sc arieltalk a31
    a"Let me change that one for you."
    show sc arieltalk a39
    mc"No, no... I'll keep it."
    show sc arieltalk a43
    mc"Who knows? It might be handy if I ever go into Chinatown."
    play sound "sound effects/01/Girl_Giggle.mp3"
    show sc arieltalk a17
    a"Haha!"
    a"Good point."
    stop sound fadeout 1.0
    show sc arieltalk a18
    a"Do you have a replacement wallet?"
    show sc arieltalk a08
    mc"Yeah, [mc_v_address] gave me one."
    stop music fadeout 2.0
    show sc arieltalk a13
    a"Sweet."
    show sc arieltalk a14
    a"Well, it seems like you're all set."
    play music "sound effects/01/Imaginary_Heroes2.mp3" loop fadein 1.0
    show sc arieltalk a12
    mc"I don't suppose you managed to find anything on that gang name yet?"
    show sc arieltalk a13
    a"Not much."
    show sc arieltalk a18a
    a"But I did find a discussion thread about them in one of the forums dating back about twelve months ago."
    #Ariel sits and looks at her computer while the MC stands behind her with a hand on the back of her seat
    #She shows him her screen
    show sc arieltalk a13
    a"The tattoo was originally only inked on girls who were willing to join the gang, and there's mention of the design being requested in local tattoo parlours."
    show sc arieltalk a19
    mc"Like the one [b_name] and I visited yesterday."
    show sc arieltalk a17
    a"Exactly."
    show sc arieltalk a46
    a"But after reading further along, there was a rumour that the gang went underground and haven't been heard from in over a year."
    a"There have been some sightings of girls in town with that {i}Apex Legion{/i} tattoo."
    show sc arieltalk a04
    mc"Is there any mention of what this gang actually does, or did?"
    show sc arieltalk a13
    a"No, nothing concrete."
    show sc arieltalk a18a
    a"One person suggested that the tattoo was given to those who were accepted into a local fraternity, but it was likely done as a prank."
    show sc arieltalk a19
    mc"It could explain why the girl I spoke to last night at the club didn't know much about it, aside from the name."
    show sc arieltalk a15
    mc"(Now's a good time to ask her about the contents of the drive, to see if she knows anything useful.)"
    mc"[a_name], do you have any idea what kind of details were transferred from Mr. Walker's computer to that drive?"
    show sc arieltalk a18
    a"Oh... Not a great deal."
    show sc arieltalk a21
    a"I was asked by [mc_vic_address] to create a program that would search for a computer's contacts and financial records."
    show sc arieltalk a44
    a"Also locations frequented by Mr Walker."
    show sc arieltalk a43
    mc"Is that it?"
    show sc arieltalk a42
    a"I'm afraid so."
    show sc arieltalk a18a
    a"You know [mc_vic_address]. He usually keeps his cards close to his chest."
    show sc arieltalk a16
    mc"Yeah, he certainly does."
    show sc arieltalk a03
    mc"(What does he not want us to know?)"
    mc"(That's the million dollar question.)"
    show sc arieltalk a45
    mc"(Once I get that drive back, I need to see the information stored on it before I hand it over to [mc_vic_address].)"

    #When the MC goes to chat with Ariel, she could tell him that Victor ordered her to create a virus that look for the
    #computer's contacts folder, so Victor might be looking for someone special who attended the party that day or something
    #like that. She doesn't know much either, and they could begin Victor is planning something without telling them.

    show sc arieltalk a18
    a"Is there anything else I can do?"
    show sc arieltalk a04
    mc"Not unless you've invented a time machine that I can use to help fix this mess."
    show sc arieltalk a17
    a"That's the next project I'm working on."
    show sc arieltalk a45
    mc"Well, I'm very much looking forward to that day."
    menu:
        "Glance downwards"(wt="Best option"):
            show sc arieltalk a48
            mc"(Damn... I never realised how nice [a_name]'s legs were before.)"
            mc"(Amongst her other fine assets.)"
            mc"(She should show them more often.)"
            $ rewards_unlock ("ariel",2)
        "Continue talking with her":
            show sc arieltalk a45
            pause 0.1

    show sc arieltalk a16
    mc"Anyway, you've done plenty, [a_name]. But keep looking and see what you can find."
    show sc arieltalk a04
    mc"By the way, have you worked out what you're going to do about those security key cards [mc_vic_address] asked you to get?"
    show sc arieltalk a21
    a"Yeah, I've been meaning to discuss that with you."
    show sc arieltalk a22
    a"I was thinking of checking it out sometime today."
    a"Do you have time to come with me this afternoon?"
    show sc arieltalk a12

    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    if v_ep01_05_01_Ariels_Work_Date == True:
        #These lines if the player chose “Work with her" in Scene 05-01"

        #Ariel re-mentions the details of the previous job which they will do later in the day"
        mc"(Well, I already promised her that I would.)"
        mc"(And I'd feel bad if I didn't and something went wrong.)"
        mc"Yeah, Definitely. I'll go with you."


        #IMPORTANT: If the player originally chose this option, then they have unlocked a special date with Ariel after the task has been completed
        #Make sure to set up a variable for this choice

        #GO DOWN TO > #scene continues

    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    else:
        #These lines if the player chose "Don't respond" in Scene 05-01"

        #The MC agrees to help Ariel with the job which they will do later in the day"

        #Vivian re-mentions the details of the previous job which they will do later in the day"
        mc"(Hmm... I never gave her an answer the other day when she mentioned this.)"
        mc"(But I know I'd feel bad if I didn't go with her and something went wrong.)"
        mc"Yeah, I'm interested."



    #scene continues
    show sc arieltalk a14
    a"Thanks, [y_name]."
    $ task_addnew("Help "+a_name+" steal cards from the Security Company",7)

    if v_ep01_03_03_Outside_Ariels_Room == True:
        #"Add these lines only if the player chose to “Investigate" during Scene 03-03"
        show sc arieltalk a12
        mc"So... Played any good games online, lately?"
        show sc arieltalk a18
        a"Um... What do you mean?"
        show sc arielsroom a07
        with flash(0.25, 0, 0.75, "#fff")
        pause 1.0
        show sc arielsroom a08
        with dissolve
        pause 1.0
        show sc arielsroom a09
        with dissolve
        pause 1.0
        show sc arielsroom a18
        with dissolve
        mc"(What the hell??)"
        show sc arielsroom a23
        mc"(Oh my God... It's not just any online game that she's creating.)"
        mc"(It's an adult online game!!)"
        show sc arieltalk a20
        with flash(0.25, 0, 0.75, "#fff")
        mc"I figured that because you're online all the time and we have a strict curfew, maybe there are games that you sometimes like to play, you know?"
        show sc arieltalk a21
        a"Yeah, of course."
        show sc arieltalk a22
        a"But you're probably not interested in the kind of games that I like."
        show sc arieltalk a19
        mc"You'd be surprised."
        mc"(I don't know if she has any clue as to what I'm alluding to, but it's fun seeing her look so concerned.)"
        show sc arieltalk a20
        mc"(I might press her more with this at another time.)"

    show sc arieltalk a15
    mc"All right, I'll be around whenever you're ready..."
    stop music fadeout 1.0
    #screen goes blank
    scene black
    with dissolve
    scene black
    with Pause (2)
    jump lb_ep01_The_MC_talks_with_Victor1
    #scene continues

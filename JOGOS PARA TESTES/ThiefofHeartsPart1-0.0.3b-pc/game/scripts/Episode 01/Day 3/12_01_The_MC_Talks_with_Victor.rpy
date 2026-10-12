init:
    $ v_ep01_mc_task_visit_options_1 = ""
    $ v_ep01_mc_task_visit_options_2 = ""
    $ v_ep01_mc_task_visit_options_3 = ""

label lb_ep01_The_MC_talks_with_Victor1:
    #the MC enters the living room and finds Victor packing a bag
    scene sc home h01
    with dissolve
    mc"[mc_vic_address]..."
    show sc home h02
    mc"You're here."
    show sc home h03
    vic"Yeah, I just had to pick up a few things and then I'm heading back out again."
    show sc home h06
    vic"What are you doing here? Aren't you meant to be at work?"
    show sc home h11
    mc"It's my day off."
    show sc home h03
    vic"Well, shouldn't you be out doing some investigating?"
    show sc home h04
    vic"Time's a ticking, son."
    show sc home h09
    mc"Yeah, I was just about to do that."
    show sc home h13
    mc"(I don't have any fresh leads, at least, until [a_name] manages to find something.)"
    show sc home h09
    mc"[mc_vic_address], can we talk?"
    show sc home h03
    vic"I'm rather busy, [y_name]."
    show sc home h01
    mc"(He seems a little stressed out.)"
    show sc home h12
    mc"(That's a little unusual.)"
    #Victor's phone rings
    play sound "sound effects/01/Cell_Phone_Ring_Sound_Effect_-_reduced.mp3" loop
    pause 1.0
    show sc home h07
    if persistent.v_sounds_text_on == True:
        "(Phone ringing)"
    else:
        pause 2.0
    show sc home h08
    vic"Excuse me, I really need to take this."
    show sc home h12
    vic"We'll talk when I get home tonight."
    show sc home h11
    mc"But didn't you say that you have to work a shift?"
    #Victor places his hand over the speaker part of the phone
    show sc home h08
    vic"Oh, right..."
    vic"Fine, we'll talk tomorrow."
    show sc home h10
    mc"Uh, sure thing, [mc_vic_address]."
    stop sound fadeout 1.0
    show sc home h14
    vic"Yeah, it's me."
    vic"Why are you calling me?"
    #Victor goes into another room, and the MC listens in
    vic"Yes, yes, I know. The Plaza Hotel."
    show sc home h12
    vic"I know which room and the floor."
    show sc home h14
    vic"Yeah, I'm on my way."
    #Victor leaves and the MC hides in the next room
    show sc home h13
    mc"(The Plaza Hotel?)"
    mc"(That's a long trip from here.)"
    mc"(I guess he really needs the money so he must be trying to fit this job in before the one he has tonight.)"
    show sc home h24
    mc"(Hmm... I know I should be looking for the drive, but the girls also asked me for my help today.)"
    mc"(Given that time is of the essence, it would be better if I tell the girls when we should go rather than waiting on them.)"
    mc"(If it doesn't suit them, then I might not be able to escort them to these places.)"
    #Vivian / Ariel / Bella
    menu:
        "[v_name]":
            #screen goes blank
            scene black
            with dissolve
            scene black
            with Pause (2)
            #The MC visits Vivian who is in the living room
            show sc home h15
            with dissolve
            mc"[mc_v_address!c]?"
            show sc home h20
            v"What's up, sweetheart?"
            show sc home h15
            show screen toh_main_game_screen
            mc"Is there any chance we could go to the theatre now?"
            show sc home h17
            mc"I have a few things I have to do, and if we don't go now, then I can't guarantee that I'll be able to help you later."
            show sc home h21
            v"Oh, well in that case, we can go to the theatre right away!"
            show sc home h22
            v"Let me just get my keys and purse from upstairs and then we can head to the theatre..."
            $ v_ep01_mc_task_visit_options_1 = "[v_name]"
            #screen goes blank
            scene black
            with dissolve
            scene black
            with Pause (2)
            jump lb_ep01_The_MC_and_Vivian_acting_school1

            #SCENE CONTINUES WITH > Scene 12-02- The MC helps Vivian Infiltrate the acting school and steal the wig and dress

    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - - - - - - - - - - -

        "[a_name]":
            #screen goes blank
            scene black
            with dissolve
            scene black
            with Pause (2)
            #The MC visits Ariel who is in her bedroom, lying on her bed on her front, looking at her laptop
            play sound "sound effects/01/Door_Knock_Sound_Effect_Free.mp3"
            show sc arielhome a01
            if persistent.v_sounds_text_on == True:
                "(Knock, knock, knock.)"
            else:
                pause 2.0
            show sc arielhome a04
            with dissolve
            mc"[a_name]?"
            stop sound fadeout 1.0
            show sc arielhome a06
            a"Oh, hey [y_name]. What's up?"
            show sc arielhome a07
            mc"Sorry to bother you, but I was wondering if we could check out that security systems place."
            show sc arielhome a02
            mc"Preferably now."
            show sc arielhome a08
            a"Oh, how come?"
            show sc arielhome a02
            mc"I have a few things I have to do, and if we don't go now, then I can't guarantee that I'll be able to help you later."
            show sc arielhome a07
            a"Hmm..."
            show sc arielhome a08
            a"It's a little sooner than I was planning to go there, but if I move some things around, then it can work."
            #She hops up off the bed
            show sc arielhome a06
            a"All right, give me a few minutes to get ready and then we can head right over..."
            $ v_ep01_mc_task_visit_options_1 = "[a_name]"
            #screen goes blank
            scene black
            with dissolve
            scene black
            with Pause (2)


            #START SCENE HERE IF PLAYER CALLS & CHOOSES ARIEL FOR THEIR 2ND OR 3RD CHOICE TO DO HER TASK
            #The MC waits patiently in the living room for Ariel
            show sc arielhome a10
            with dissolve
            a"Are you ready to leave, [y_name]?"
            #The MC looks up and Ariel has changed into a security systems outfit - https://pixhost.to/show/1044/447513812_000.jpg
            show sc arielhome a09
            mc"Yeah, I'm all set."
            show sc arielhome a16
            mc"What's that you're wearing?"
            show sc arielhome a11
            a"This is the security staff uniform for the place we're going to."
            show sc arielhome a12
            a"I had [mc_v_address] find me a similar dress shirt that matches their uniform."
            show sc arielhome a11
            a"It should help us to blend in."
            show sc arielhome a14
            a"What do you think?"
            #Ariel poses for him
            show sc arielhome a16
            mc"Yeah, you look great."
            show sc arielhome a18
            a"I also made us some fake employee ID cards."
            #She hands the MC a card with the name of the security place and his face on it
            show sc arielhome a17
            mc"Sweet!"
            show sc arielhome a12
            a"I have a shirt for you too."
            #She has him the shirt
            show sc arielhome a13
            a"I left it upstairs in your room though."
            show sc arielhome a11
            a"Once you put it on, we can get going..."
            #Ariel smiles
            show sc arielhome a10
            mc"Sure thing, [a_name]."
            #screen goes blank
            scene black
            with dissolve
            scene black
            with Pause (2)
            jump lb_ep01_12_04_card_theft1

            #SCENE CONTINUES WITH > Scene 12-04 - The MC helps Ariel steal security cards

    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

        "[b_name]":
            #screen goes blank
            scene black
            with dissolve
            scene black
            with Pause (2)

            #The MC visits Bella who is in her room, fixing/brushing her hair while she looks in the mirror
            show sc bellahome b01
            with dissolve
            mc"[b_name]?"

            #She sees the MC's reflection in the mirror so she doesn't have to turn around
            show sc bellahome b04
            b"Oh, it's you."
            show sc bellahome b05
            b"What do you want?"
            show sc bellahome b06
            mc"You probably wanted to go to this art school a little later on, but is there any chance we could go sooner, as in, right now?"
            show sc bellahome b03
            b"Why?"
            show sc bellahome b07
            mc"I have a few things I have to do is all."
            show sc bellahome b09
            b"This is not very convenient, [y_name]."
            show sc bellahome b10
            b"The school will still be in session so there will be lots of students and staff on the grounds if we go now."
            show sc bellahome b11
            b"So it's not a great time."
            show sc bellahome b07
            mc"I understand. However, if we don't go now, then I can't guarantee that I'll be able to help you later."
            show sc bellahome b02
            b"(Sigh...)"
            show sc bellahome b03
            b"All right, fine."
            show sc bellahome b11
            b"I'll have to make some adjustments to the plan on the way there."
            show sc bellahome b12
            b"You go ahead and scope the place out. I have to change out of these clothes and take a quick shower."
            show sc bellahome b10
            b"I'll meet you out near the front of the school in about twenty minutes."
            show sc bellahome b13
            mc"Fine..."
            # or mc"See you there, [b_name]."
            $ v_ep01_mc_task_visit_options_1 = "[b_name]"
            #screen goes blank
            scene black
            with dissolve
            scene black
            with Pause (2)
            jump lb_ep01_The_MC_and_Bella_at_the_art_school

init:
    $ v_ep01_bella_respect_counter = 0
    $ v_ep01_bella_cocky_counter = 0
    $ v_ep01_bella_arrogant_counter = 0

label lb_ep01_The_MC_talks_with_Bella1:
    #show the MC outside Bella's room
    play music "sound effects/01/Family Ties.mp3" loop fadein 1.0
    scene sc bellatalk b00
    with dissolve
    mc"(I better talk to [b_name] to see if she has that replacement phone for me.)"
    scene black
    with dissolve
    scene black
    with Pause (2)
    #Her door is slightly open so she pushes it and then we see Bella in her room
    scene sc bellatalk b10
    with dissolve
    mc"(Woah...)"
    show sc bellatalk b01
    #she's wearing exercise clothing and is facing away from the MC when he arrives at her door
    mc"(She must be about to go out for a run.)"
    #show a close-up of her ass in tight shorts
    show sc bellatalk b05
    mc"(I bet she'll work up a proper sweat in those tight clothes.)"
    #Bella turns and sees the MC
    show sc bellatalk b01
    mc"Ahem!"
    show sc bellatalk b02
    with hpunch
    b"Oh! You startled me."
    #She turns to face him and we see her holding a phone - the replacement she will give to the MC
    #Her look of shock changes to one of anger
    show sc bellatalk b04
    b"Don't you know how to knock, [y_name]?"
    show sc bellatalk b10
    mc"Well, the door was open so I let myself in."
    show sc bellatalk b06
    b"Hmm... Fine then."
    #The MC stares at her cleavage and she doesn't notice him ogling her
    show sc bellatalk b31
    mc"(Geez...)"
    show sc bellatalk b32
    mc"(I know I promised [mc_v_address] that I'd put a hold on hooking up with random girls for the time being...)"
    mc"(But [b_name] is already making things difficult.)"
    show sc bellatalk b07
    mc"(But then [b_name]'s no \"random\" girl.)"
    mc"So what are you up to?"
    show sc bellatalk b09
    b"I've been working on your new phone."
    b"It's fully charged so [a_name] should be able to upload all your contacts once you take it over to her."
    show sc bellatalk b15
    mc"Thanks."
    show sc bellatalk b04
    b"It will be ready for you shortly."
    show sc bellatalk b01
    b"By the way, I found some information on one of the schools I was telling you about yesterday."
    show sc bellatalk b05
    b"It's in the ritzy part of town, at the local college."
    show sc bellatalk b12
    mc"What did you find?"
    show sc bellatalk b21a
    b"It has a pretty big art department."
    b"And it has all the stuff that I'll require to do this forgery."
    show sc bellatalk b26
    mc"That's great news."
    show sc bellatalk b25
    b"So, are you coming with me this afternoon?"

    #These lines if the player chose “Offer to help" in Scene 04-01"
    #Bella re-mentions the details of the previous job which they will do later in the day"
    if v_ep01_04_01_Bella_Work_Date == True:
        show sc bellatalk b14
        mc"(I already agreed to help her with this, so I can't back out now.)"
        show sc bellatalk b16
        mc"(And I do owe [b_name] after she helped to diffuse things with [mc_vic_address].)"

        #IMPORTANT: If the player originally chose this option, then they have unlocked a special date with Bella after the task has been completed
        #Make sure to set up a variable for this choice
    else:
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

        #These lines if the player chose “Take time to consider" in Scene 04-01"
        #The MC agrees to help Bella with the job which they will do later in the day"
        show sc bellatalk b28a
        mc"This afternoon?"
        show sc bellatalk b21a
        b"Yeah, to break into the school. You didn't really give me an answer the other day."
        #Bella looks at him like she's putting pressure on him to say yes
        show sc bellatalk b22a
        mc"(Hmm...)"
        show sc bellatalk b16
        mc"(I kind of owe her after she helped to diffuse the situation with [mc_vic_address].)"


    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    #scene continues
    show sc bellatalk b15
    mc"Sure, count me in."
    $ task_addnew("Help "+b_name+" steal supplies from the Art School",6)
    show sc bellatalk b24
    b"Great. We'll go there in between classes when it's a quiet time of day."
    show sc bellatalk b27
    b"There's normally limited security around during school hours."
    b"I'll come and find you when I'm ready to go."
    show sc bellatalk b08
    mc"Cool."
    show sc bellatalk b09
    b"By the way, here's your phone."
    #Bella hands him the replacement phone
    show sc bellatalk b20
    b"Try not to lose this one."
    show sc bellatalk b19
    mc"Aww... Seriously?"
    show sc bellatalk b25
    b"That's the only case I had."
    show sc bellatalk b20
    mc"Yeah, Yeah, sure it is. But I guess it will have to do."
    show sc bellatalk b21
    b"By the way... How the hell did you lose the other one?"
    show sc bellatalk b22
    mc"You don't wanna know."
    show sc bellatalk b30
    b"Well, I hope she was worth it."
    #Bella makes a side remark
    show sc bellatalk b29
    mc"What the hell is that supposed to mean?"
    show sc bellatalk b21
    b"N-nothing..."
    #Bella changes her demeanour and goes back on the offensive
    show sc bellatalk b27
    b"Anyway, get out of my room. I'm about to go for my run."
    #She turns away from the MC
    show sc bellatalk b28
    mc"Fine, whatever."
    #The MC stands outside Bella's room
    show sc bellatalk b16
    mc"(What the hell is her issue with me now?)"
    menu:
        "Leave":
            show sc bellatalk b14
            with dissolve
            pause 0.1
            $ v_ep01_bella_respect_counter += 1
        "One last look"(wt="Best option"):
            show sc bellatalk b32
            with dissolve
            pause 1.5
            $ v_ep01_bella_cocky_counter += 1
            show sc bellatalk b05
            with dissolve
            pause 1.5
            $ rewards_unlock ("bella",6)
        "Sinful thought":
            show sc bellatalk b32
            mc"(Geez [b_name]... When you dress in such tight clothes, you're simply inviting perverts to ogle you.)"
            show sc bellatalk b05
            mc"(Like me for example...)"
            $ v_ep01_bella_arrogant_counter += 1
    show sc bellatalk b14
    mc"(Maybe she’s just jealous that I managed to hook up last night and I also had a night out on the town.)"
    show sc bellatalk b33
    with dissolve
    mc"(Anyway, that's hardly my problem...)"
    stop music fadeout 1.0
    #screen goes blank
    scene black
    with dissolve
    scene black
    with Pause (2)
    jump lb_ep01_The_MC_talks_with_Ariel1


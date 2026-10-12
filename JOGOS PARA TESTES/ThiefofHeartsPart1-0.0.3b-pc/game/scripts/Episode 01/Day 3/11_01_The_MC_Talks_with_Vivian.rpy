label lb_ep01_The_MC_talks_with_Vivian1:
    #show the MC watching Victor leaving the house and the door closing behind him
    scene sc viviantalk v00
    with dissolve
    mc"(Okay, he's gone. Now I can speak with [mc_v_address].)"
    #show the MC going up the stairs - starts at the bottom
    show sc viviantalk v02
    mc"(I'm not sure how much I'm going to tell her about last night.)"
    #the MC goes up the stairs
    mc"(Then again, I'm not sure how much she'll want to know.)"
    #he arrives at her door and knocks
    #Door knocking sound to match the render
    play sound "sound effects/01/Door_Knock_Sound_Effect_Free.mp3"
    show sc viviantalk v01
    with dissolve
    if persistent.v_sounds_text_on == True:
        "(Knock, knock, knock)"
    else:
        pause 2.0
    stop sound fadeout 1.0
    mc"Hello?"
    v"Come on in."
    #The MC enters the main bedroom and finds Vivian sitting on the end of the bed
    play sound "sound effects/01/Door_Opening.mp3"
    show sc viviantalk v03
    v"Have a seat with me, [y_name]."
    stop sound fadeout 1.0
    show sc viviantalk v04
    mc"Uh, okay..."
    #The MC sits with Vivian on the bed
    play music "sound effects/01/Whispers of Love.mp3" loop fadein 1.0
    show sc viviantalk v06
    with dissolve
    v"So I'll get right to it... What happened last night?"
    v"And I want the real story."
    show sc viviantalk v07
    mc"All right, so after work, Harry and I went to this club."
    show sc viviantalk v08
    mc"There was a guy there who owned the tattoo parlour that [b_name] and I checked out after her shift yesterday."
    show sc viviantalk v17
    v"And did he tell you anything?"
    show sc viviantalk v08
    mc"No, he refused to."
    show sc viviantalk v16
    mc"But as I said to [vic_name], a girl at the club who we met happened to have that same tattoo."
    mc"And later on she gave me the name."
    show sc viviantalk v23
    v"What do you mean by later on?"
    show sc viviantalk v22
    mc"Well... You know?"
    #Vivian looks confused
    if v_ep01_09_01_Tasha_and_Mikayla_Sex_path == True:
        #These lines if the player slept with both Mikayla and Tasha
        show sc viviantalk v22
        mc"I kind of went with them back to their hotel room."
        show sc viviantalk v23
        v"Oh!"
        #Vivian surprised and then looks away from the MC
        show sc viviantalk v17
        v"But what about Harry?"
        show sc viviantalk v07
        mc"I had to send him home in a cab as he was very drunk."
        show sc viviantalk v27
        v"(Wait!... 'Them?'  Did [y_name] go home with two girls last night?)"
    else:
        #These lines if the player slept with Mikayla or Tasha
        show sc viviantalk v22
        mc"Harry and I kind of went with them back to their hotel room."
        show sc viviantalk v23
        v"Oh!"
        #Vivian surprised and then looks away from the MC
        show sc viviantalk v24
        v"I see..."
    #scene continues
    show sc viviantalk v24
    v"Do you know what [vic_name] would say if he knew what you just told me?"
    show sc viviantalk v13
    mc"I know... And I'm sorry."
    menu:
        "Try and justify your actions":
            show sc viviantalk v11
            mc"But I'm a guy, in the prime of my youth."
            show sc viviantalk v25
            mc"I also have certain needs, you know?"
            $ v_ep01_vivian_cocky_counter += 1
            show sc viviantalk v27
            v"(He's not the only one.)"

        "Tell it like it is":
            show sc viviantalk v11
            mc"But I'm a horny young male."
            show sc viviantalk v16
            v"(He's not the only one.)"
            show sc viviantalk v27
            v"(Apart from being young and a male, of course.)"
            show sc viviantalk v08
            mc"What did you expect me to do in that situation?"
            $ v_ep01_vivian_arrogant_counter += 1
            show sc viviantalk v24
            v"I expect you to control yourself better, [y_name]."
            show sc viviantalk v06
            v"If [vic_name] comes down hard on you, he usually comes down hard on all of us."
            show sc viviantalk v13
            mc"Yeah, you're right."
            show sc viviantalk v08
            mc"I'll try not to let it happen again."

    show sc viviantalk v23
    v"It's okay, I understand."
    show sc viviantalk v17
    v"But maybe in light of the circumstances, you should put a hold on hooking up with random girls."
    show sc viviantalk v23
    v"At least until you get that flash drive back."
    show sc viviantalk v20
    v"It might get you back into his good books."
    show sc viviantalk v06
    v"If you keep having things stolen, eventually he is going to find out. And worse, he could kick you out."
    show sc viviantalk v07
    mc"Yeah, maybe you're right."
    show sc viviantalk v21
    mc"({i}Asian Busty Beauties{/i} it is, later tonight!)"
    stop music fadeout 1.0
    show sc viviantalk v08
    mc"So anyway, that's as much as I can tell you about last night."
    show sc viviantalk v22
    mc"Right now I'm hoping that [a_name] finds out more information from that gang name."
    show sc viviantalk v07
    mc"Did you find out anything from Mrs. Walker?"
    play music "sound effects/01/Whispers of Love1.mp3" loop fadein 1.0
    show sc viviantalk v17
    v"I managed to get a copy of the party invite list, but [a_name] checked it and every name was accounted for."
    show sc viviantalk v23
    v"That girl wasn't on it, or she took someone else's place."
    show sc viviantalk v13
    mc"Damn..."
    show sc viviantalk v16
    mc"There's another problem."
    show sc viviantalk v26
    v"Oh, what now?"
    show sc viviantalk v22
    mc"My bike was stolen."
    show sc viviantalk v20b
    v"What?? But how?"
    mc"It's a long story."
    show sc viviantalk v06
    v"Are you going to have any problems getting to work?"
    show sc viviantalk v08
    mc"Don't worry, it's my problem and I'll take care of it."
    show sc viviantalk v07
    mc"I'm not working today so I have time to figure things out."
    show sc viviantalk v24
    v"Speaking of which..."
    show sc viviantalk v20
    v"Are we still on?"
    show sc viviantalk v21
    mc"Um... On for what?"
    show sc viviantalk v23
    v"Remember the job I told you about yesterday when you came to see me at the restaurant?"


    #These lines if the player chose “Agree" in Scene 06-01"

    #Vivian re-mentions the details of the previous job which they will do later in the day"
    if v_ep01_06_01_Vivian_Work_Date == True:
        show sc viviantalk v11
        mc"Yes, of course."
        show sc viviantalk v19
        v"I was hoping to check out a local acting school to get a few things that I need for my costume."
        show sc viviantalk v17
        v"But I'm going to need your help."
        show sc viviantalk v16
        mc"To pull a job I presume?"
        show sc viviantalk v19
        v"Yes, indeed."
        show sc viviantalk v17
        v"So, are you still in?"
        show sc viviantalk v11
        mc"Yes, definitely."
        show sc viviantalk v08
        mc"It's the least I could do after you didn't say anything to [vic_name]."

        #IMPORTANT: If the player originally chose this option, then they have unlocked a special date with Vivian after the task has been completed
        #Make sure to set up a variable for this choice

        #- - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - -
    else:
        #These lines if the player chose “Think about it" in Scene 06-01"

        #Vivian re-mentions the details of the previous job which they will do later in the day"
        show sc viviantalk v22
        mc"Um, kind of."
        show sc viviantalk v23
        v"You told me you'd think about it so I'm wondering if you might be interested in helping me out."
        show sc viviantalk v15
        mc"Okay, what exactly do you need me to do?"
        show sc viviantalk v17
        v"I was hoping to check out a local acting school to get a few things that I need for my costume."
        v"But I'm going to need your help."
        show sc viviantalk v16
        mc"To pull a job I presume?"
        show sc viviantalk v19
        v"Yes, indeed."
        show sc viviantalk v17
        v"So, are you in?"
        show sc viviantalk v11
        mc"Sure, why not."
        show sc viviantalk v21
        mc"It's the least I could do after you didn't say anything to [vic_name]."

    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    #scene continues
    show sc viviantalk v20
    v"You know I would do almost anything for my [mc_v_rel]."
    #Vivian places a hand on the MC's thigh
    show sc viviantalk v53
    v"Just say the word."
    show sc viviantalk v54
    with dissolve
    pause 1.0
    show sc viviantalk v55
    with dissolve
    mc"Um..."
    show sc viviantalk v56
    v"Oh..."
    #Vivian removes her hand and looks away, as she's embarrassed
    show sc viviantalk v57
    v"Anyway."
    show sc viviantalk v06
    v"That acting school has classes going all afternoon."
    v"So today would be the best time to get in and out with what I need."
    show sc viviantalk v19
    v"Are you free this afternoon?"
    show sc viviantalk v11
    mc"Yeah, I don't think I have anything on until later today."
    $ task_addnew("Help "+v_name+" steal items from the Acting Theatre",5)
    show sc viviantalk v20
    v"That's what I like to hear."
    show sc viviantalk v28
    v"Oh, and one more thing."
    #Vivian stands up and goes to a dresser drawer so we can see from behind her
    #The MC stares at her ass
    show sc viviantalk v29
    with dissolve
    mc"..."
    menu:
        "Behave":
            show sc viviantalk v12
            mc"(No, I'll be good.)"
            mc"(After having to deal with the old creep at the diner yesterday, the last thing she needs is to catch me ogling her.)"
            $ v_ep01_vivian_respect_counter += 1
            show sc viviantalk v33
            with dissolve
            v"I've got it."
            show sc viviantalk v41
            mc"Sweet."
        "Take a quick peep"(wt="Best option"):
            show sc viviantalk v30
            mc"(She has no idea what she is showing me.)"
            show sc viviantalk v31
            mc"(I better stop looking, as enticing as it is to continue staring.)"
            mc"(Well, maybe a few more seconds.)"
            $ rewards_unlock ("vivian",4)
            show sc viviantalk v32
            v"(Ah, here it is.)"
            $ v_ep01_vivian_cocky_counter = 0
            show sc viviantalk v33
            with dissolve
            v"I've got it."
            show sc viviantalk v37
            mc"Oh, cool..."
            #Vivian turns and sees the MC looking down rather than up at her eyes
            show sc viviantalk v44
            v"(Hmm... Was he just checking me out?)"
    #Vivian holds up a wallet “
    show sc viviantalk v34
    v"Here."
    #The MC stands up and she hands it to him
    show sc viviantalk v36
    mc"Thanks, [mc_v_address]."
    show sc viviantalk v42
    v"You're welcome."
    #The MC turns and has his head down
    show sc viviantalk v37
    mc"Sigh."
    show sc viviantalk v45
    v"What's wrong, sweetheart?"
    show sc viviantalk v37
    mc"Just these past few days."
    show sc viviantalk v44
    mc"I honestly can't believe how things keep going against me."
    mc"The heist, losing that flash drive, having my bike stolen, and then everything that happened last night..."
    show sc viviantalk v38
    mc"I feel like the unluckiest person right now."
    #Vivian stands next to the MC and places a hand on his shoulder
    show sc viviantalk v45
    v"Well, we all have bad luck from time to time."
    show sc viviantalk v42
    v"But the best advice I can give you is that luck has a way of balancing things out."
    v"In other words, I have a feeling that you've used up all your bad luck, and things will start to turn around soon."
    show sc viviantalk v45
    v"At least, I hope it will. For your sake."
    show sc viviantalk v38
    mc"Huh?"
    show sc viviantalk v52
    v"I'm kidding! Just a joke, dear."
    show sc viviantalk v51
    mc"Oh, haha!"
    #She hugs him to show that she was joking and was being sincere
    show sc viviantalk v46
    v"Mmm..."
    show sc viviantalk v47
    mc"Thanks, [mc_v_address]. I needed to hear that."
    show sc viviantalk v49
    v"You're welcome."
    show sc viviantalk v48
    mc"(Hmm... She's holding on to me a little longer than usual.)"
    show sc viviantalk v50
    mc"(It's like she doesn't want to let me go.)"
    show sc viviantalk v52
    v"Anyway, I have a few things to do as well, so I'll let you know when I'm ready to go."
    v"And I'll explain the plan on the way there."
    show sc viviantalk v51
    mc"Sounds good..."
    #Final shot here of the MC and Vivian looking at each other and smiling
    #screen goes blank
    stop music fadeout 1.0
    scene black
    with dissolve
    scene black
    with Pause (2)
    jump lb_ep01_The_MC_talks_with_Bella1

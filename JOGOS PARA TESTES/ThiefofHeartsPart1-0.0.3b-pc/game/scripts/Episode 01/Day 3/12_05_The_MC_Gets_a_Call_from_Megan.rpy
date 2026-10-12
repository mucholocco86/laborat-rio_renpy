init:
    $ v_ep01_megan_dates_counter = 0


label lb_ep01_MC_gets_a_call_from_Megan1:
    centered "A short time later...{w=2.0}{nw}" with dissolve
    show text "A short time later..." #THESE LINES ARE NOT DUPLICATES. Needed to fade the text in and out!
    scene bg black with Dissolve(1)
    pause 1.0
    #the MC is in his room
    play ambient "sound effects/01/street_sound_day_ambience.ogg" loop fadein 1.0
    scene sc zoras z134c
    with dissolve
    if v_ep01_mc_task_visit_options_2 != "" and not v_ep01_mc_task_visit_options_1 != "":
        mc"(After today's events, I'm looking forward to having a nice relaxing night in.)"
    else:
        mc"(Sigh, there's so much I still need to do.)"
        mc"(I'm looking forward to having a nice relaxing night in, eventually.)"
    play sound "sound effects/01/Cell_Phone_Ring_Sound_Effect_-_reduced.mp3" loop
    if persistent.v_sounds_text_on == True:
        "(Phone ringing)"
    else:
        pause 2.0
    mc"(Of course...)"
    #cell phone sound effect
    show sc zoras z133
    #The MC looks at his phone
    mc"(Oh, well this is a surprise.)"
    stop sound fadeout 1.0
    #He answers the call
    show sc zoras z134
    mc"Hello?"
    $ renpy.music.set_volume(0.3, 0.0, channel="ambient")
    show sc megancall m05
    megan"Good afternoon, young man."
    show sc megancall m06
    megan"You know who this is, right?"
    $ renpy.music.set_volume(1.0, 0.0, channel="ambient")
    show sc zoras z138
    mc"Hi Megan."
    mc"I wasn't expecting to hear from you so soon."
    $ renpy.music.set_volume(0.3, 0.0, channel="ambient")
    show sc megancall m09
    megan"Well, I'm flattered, but this call is important."
    $ renpy.music.set_volume(1.0, 0.0, channel="ambient")
    show sc zoras z134
    mc"How so?"
    $ renpy.music.set_volume(0.3, 0.0, channel="ambient")
    show sc megancall m05
    megan"I happen to come into possession of something you might be looking for."
    $ renpy.music.set_volume(1.0, 0.0, channel="ambient")
    show sc zoras z134b
    mc"You have?"
    mc"What is it?"
    $ renpy.music.set_volume(0.3, 0.0, channel="ambient")
    show sc megancall m13a
    megan"Let's just say that it has two wheels, a seat and a sturdy handlebar. Sound familiar?"
    $ renpy.music.set_volume(1.0, 0.0, channel="ambient")
    show sc zoras z137
    mc"You found my bicycle!"
    mc"But how?"
    $ renpy.music.set_volume(0.3, 0.0, channel="ambient")
    show sc megancall m09
    megan"I'll explain everything when you get here."
    $ renpy.music.set_volume(1.0, 0.0, channel="ambient")
    show sc zoras z134b
    mc"Where am I going to pick it up?"
    $ renpy.music.set_volume(0.3, 0.0, channel="ambient")
    show sc megancall m06a
    megan"At my place. Tonight."
    $ renpy.music.set_volume(1.0, 0.0, channel="ambient")
    show sc zoras z137
    mc"Tonight? But how do you expect me to get there without a bike?"
    $ renpy.music.set_volume(0.3, 0.0, channel="ambient")
    show sc megancall m12
    megan"I thought of that."
    show sc megancall m06
    megan"A car is going to pull up outside your place in about an hour from now."
    show sc megancall m05
    megan"Don't worry, the driver works for me."
    show sc megancall m09
    megan"He'll bring you to my place and then you can ride your bicycle home."
    $ renpy.music.set_volume(1.0, 0.0, channel="ambient")
    show sc zoras z138
    mc"That's it?"
    $ renpy.music.set_volume(0.3, 0.0, channel="ambient")
    show sc megancall m06a
    megan"Pretty much."
    $ renpy.music.set_volume(1.0, 0.0, channel="ambient")
    show sc zoras z138
    mc"Hold on, please."
    show sc zoras z132
    mc"(With [mc_vic_address] at work, I should be able to get back in time before he returns home.)"
    mc"(And the girls won't care if I'm out of the house or not.)"
    mc"([mc_v_address] might though.)"
    show sc zoras z134
    mc"Okay, anything else?"
    $ renpy.music.set_volume(0.3, 0.0, channel="ambient")
    show sc megancall m18a
    megan"Just make sure you're outside when the car arrives. I've instructed my driver not to wait around."
    megan"You want your bicycle back, don't you?"
    $ renpy.music.set_volume(1.0, 0.0, channel="ambient")
    show sc zoras z134a
    mc"Yes, of course."
    $ renpy.music.set_volume(0.3, 0.0, channel="ambient")
    show sc megancall m13a
    megan"Alright, then I'll see you at my place very soon."
    megan"I am {b}so{/b} looking forward to it..."
    $ renpy.music.set_volume(1.0, 0.0, channel="ambient")
    show sc zoras z133
    mc"(Hmm... That was interesting.)"
    show sc zoras z132
    mc"(I'm happy that she found it but what I can't figure out wy she was so insistent on me seeing her tonight.)"
    mc"(And how the hell does she know where I live??)"
    #The MC looks concerned
    show sc zoras z134c
    mc"(In any case, I still have one last job to do.)"

    #IMPORTANT - By this point, the player will have done two of the tasks, therefore, only one of these choices below should come up (whoever is their last choice)
    #Vivian / Ariel / Bella
    #IMPORTANT - only the choices the player hasn't made yet will be available on the screen here
    menu:
        "[v_name]" if not v_ep01_mc_task_visit_options_2 == "[v_name]" and not v_ep01_mc_task_visit_options_1 == "[v_name]":
            $ v_ep01_mc_task_visit_options_3 = "[v_name]"
            show sc zoras z133
            pause 1.0
            play sound "sound effects/01/Phone_call_dialling_sound_effect.mp3"
            show sc zoras z134
            pause 2.0
            stop sound fadeout 1.0
            play music "sound effects/01/Frayed_Relations1.mp3" loop fadein 1.0
            #The MC calls Vivian
            show sc zoras z134
            mc"[mc_v_address]?"
            $ renpy.music.set_volume(0.3, 0.0, channel="ambient")
            show sc zoras z135
            v"What's up, sweetheart?"
            show sc zoras z136
            v"Where are you?"
            $ renpy.music.set_volume(1.0, 0.0, channel="ambient")
            show sc zoras z138
            mc"I'm near the centre of town at the moment."
            show sc zoras z139
            mc"Is there any chance we could go to the theatre now?"
            show sc zoras z137
            mc"I have a few things I have to do, and if we don't go now, then I can't guarantee that I'll be able to help you later."
            $ renpy.music.set_volume(0.3, 0.0, channel="ambient")
            show sc zoras z140
            v"Oh, well in that case, we can go to the theatre right away!"
            show sc zoras z141
            v"I'll pick you up on the way there. Let me know exactly where you are..."
            stop music fadeout 1.0
            stop ambient fadeout 1.0
            #screen goes blank
            scene black
            with dissolve
            scene black
            with Pause (2)
            $ renpy.music.set_volume(1.0, 0.0, channel="ambient")
            jump lb_ep01_The_MC_and_Vivian_acting_school1


    #SCENE CONTINUES WITH > Scene 12-02- The MC helps Vivian Infiltrate the acting school and steal the wig and dress

        "[a_name]" if not v_ep01_mc_task_visit_options_2 == "[a_name]" and not v_ep01_mc_task_visit_options_1 == "[a_name]":
            $ v_ep01_mc_task_visit_options_3 = "[a_name]"
            show sc zoras z133
            pause 1.0
            play sound "sound effects/01/Phone_call_dialling_sound_effect.mp3"
            show sc zoras z134
            pause 2.0
            stop sound fadeout 1.0
            #The MC calls Ariel
            $ renpy.music.set_volume(0.3, 0.0, channel="ambient")
            show sc zoras z142
            a"Hello?"
            $ renpy.music.set_volume(1.0, 0.0, channel="ambient")
            show sc zoras z134
            mc"[a_name]?"
            $ renpy.music.set_volume(0.3, 0.0, channel="ambient")
            show sc zoras z143
            a"Oh, hey [y_name]. What's up?"
            $ renpy.music.set_volume(1.0, 0.0, channel="ambient")
            show sc zoras z138
            mc"Sorry to bother you, but I was wondering if we could check out that security systems place."
            mc"Preferably now."
            $ renpy.music.set_volume(0.3, 0.0, channel="ambient")
            show sc zoras z144
            a"Oh, how come?"
            $ renpy.music.set_volume(1.0, 0.0, channel="ambient")
            show sc zoras z139
            mc"I'm free now, and if we don't go soon, then I might not be able to help you later."
            $ renpy.music.set_volume(0.3, 0.0, channel="ambient")
            show sc zoras z145
            a"It's a little sooner than I was planning to go there, but if I move some things around, then it can work."
            show sc zoras z146
            a"But you're going to need to come home first, as I have something that you'll need."
            $ renpy.music.set_volume(1.0, 0.0, channel="ambient")
            show sc zoras z134
            mc"Um... Okay."
            show sc zoras z138
            mc"I should be home in about fifteen minutes..."
            stop ambient fadeout 1.0
            #screen goes blank
            scene black
            with dissolve
            scene black
            with Pause (2)

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
            a"This is the security staff uniform for the place we'll be going to."
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
            a"Once you've put it on, we can get going..."
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



    #SCENE CONTINUES WITH > Scene 12-04 - The MC helps Ariel steal security cards

        "[b_name]" if not v_ep01_mc_task_visit_options_2 == "[b_name]" and not v_ep01_mc_task_visit_options_1 == "[b_name]":
            $ v_ep01_mc_task_visit_options_3 = "[b_name]"
            show sc zoras z133
            pause 1.0
            play sound "sound effects/01/Phone_call_dialling_sound_effect.mp3"
            show sc zoras z134
            pause 2.0
            stop sound fadeout 1.0
            #The MC calls Bella
            $ renpy.music.set_volume(0.3, 0.0, channel="ambient")
            show sc zoras z149
            b"Hello?"
            $ renpy.music.set_volume(1.0, 0.0, channel="ambient")
            show sc zoras z134
            mc"[b_name]?"
            $ renpy.music.set_volume(0.3, 0.0, channel="ambient")
            show sc zoras z148
            b"Oh, it's you. What do you want?"
            $ renpy.music.set_volume(1.0, 0.0, channel="ambient")
            show sc zoras z138
            mc"You probably wanted to go to this art school a little later on, but is there any chance we could go sooner, as in, right now?"
            $ renpy.music.set_volume(0.3, 0.0, channel="ambient")
            show sc zoras z150
            b"Why?"
            $ renpy.music.set_volume(1.0, 0.0, channel="ambient")
            show sc zoras z139
            mc"I have a few things I have to do is all."
            $ renpy.music.set_volume(0.3, 0.0, channel="ambient")
            show sc zoras z151
            b"This is not very convenient, [y_name]."
            show sc zoras z153
            b"The school will still be in session so there will be lots of students and staff on the grounds if we go now."
            show sc zoras z152
            b"So it's not a great time."
            $ renpy.music.set_volume(1.0, 0.0, channel="ambient")
            show sc zoras z137
            mc"I understand. However, if we don't go now, then I can't guarantee that I'll be able to help you later."
            $ renpy.music.set_volume(0.3, 0.0, channel="ambient")
            show sc zoras z151
            b"(Sigh...)"
            show sc zoras z148
            b"Alright, fine."
            show sc zoras z153
            b"I'll have to make some adjustments to the plan on the way there."
            show sc zoras z149
            b"Where are you right now?"
            $ renpy.music.set_volume(1.0, 0.0, channel="ambient")
            show sc zoras z138
            mc"I'm in the centre of town but I can meet you near the art school."
            $ renpy.music.set_volume(0.3, 0.0, channel="ambient")
            show sc zoras z153
            b"Fine, I'll leave here in a few minutes and meet you there..."
            stop ambient fadeout 1.0
            #screen goes blank
            scene black
            with dissolve
            scene black
            with Pause (2)
            $ renpy.music.set_volume(1.0, 0.0, channel="ambient")
            jump lb_ep01_The_MC_and_Bella_at_the_art_school
